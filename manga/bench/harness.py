"""Replicate model bench for the manga pipeline.

Normalises the seven candidate models behind one call signature so the same
prompt + reference set can be run across all of them and compared.
"""
import base64
import concurrent.futures as cf
import json
import mimetypes
import os
import pathlib
import time

import requests

os.environ.setdefault("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt")
os.environ.setdefault("REQUESTS_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")

ROOT = pathlib.Path(__file__).resolve().parent
TOKEN = None
for line in (ROOT.parent / ".env").read_text().splitlines():
    if line.startswith("REPLICATE_API_TOKEN="):
        TOKEN = line.split("=", 1)[1].strip()
H = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# ---------------------------------------------------------------- model table
# price = USD per output image at the tier we run it at (Replicate published).
# max_refs = documented reference-image ceiling. 0 = text-to-image only.
MODELS = {
    "gpt-image-2-low": dict(
        slug="openai/gpt-image-2", price=0.012, max_refs=16,
        params=lambda ar: {"aspect_ratio": ar, "quality": "low",
                           "output_format": "png", "moderation": "low"},
        ref_key="input_images"),
    "gpt-image-2-med": dict(
        slug="openai/gpt-image-2", price=0.047, max_refs=16,
        params=lambda ar: {"aspect_ratio": ar, "quality": "medium",
                           "output_format": "png", "moderation": "low"},
        ref_key="input_images"),
    "gpt-image-2-high": dict(
        slug="openai/gpt-image-2", price=0.128, max_refs=16,
        params=lambda ar: {"aspect_ratio": ar, "quality": "high",
                           "output_format": "png", "moderation": "low"},
        ref_key="input_images"),
    "nano-banana-2": dict(
        slug="google/nano-banana-2", price=0.067, max_refs=14,
        params=lambda ar: {"aspect_ratio": ar, "resolution": "1K",
                           "output_format": "png"},
        ref_key="image_input"),
    "nano-banana-2-lite": dict(
        slug="google/nano-banana-2-lite", price=0.034, max_refs=14,
        params=lambda ar: {"aspect_ratio": ar, "output_format": "png"},
        ref_key="image_input"),
    "seedream-5-pro": dict(
        slug="bytedance/seedream-5-pro", price=0.045, max_refs=10,
        params=lambda ar: {"aspect_ratio": ar, "size": "1K",
                           "output_format": "png"},
        ref_key="image_input"),
    "seedream-5-lite": dict(
        slug="bytedance/seedream-5-lite", price=0.035, max_refs=10,
        params=lambda ar: {"aspect_ratio": ar, "size": "2K",
                           "output_format": "png"},
        ref_key="image_input"),
    "p-image-ideogram": dict(
        slug="prunaai/p-image-ideogram", price=0.015, max_refs=0,
        params=lambda ar: {"aspect_ratio": ar, "image_size": "1K",
                           "thinking": "high", "output_format": "png"},
        ref_key=None),
    "grok-quality": dict(
        slug="xai/grok-imagine-image-quality", price=0.05, max_refs=1,
        params=lambda ar: {"aspect_ratio": ar, "resolution": "1k"},
        ref_key="image"),  # single string, not a list
}


def _data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(
        pathlib.Path(path).read_bytes()).decode()


def run(model, prompt, refs=(), aspect="2:3", timeout=600):
    """Run one prediction. refs = list of local paths or https URLs."""
    m = MODELS[model]
    payload = dict(m["params"](aspect))
    payload["prompt"] = prompt

    refs = list(refs)
    if refs:
        if not m["ref_key"]:
            return dict(model=model, status="skipped",
                        error="model takes no reference images")
        urls = [r if r.startswith("http") else _data_uri(r) for r in refs]
        if m["max_refs"] == 1:
            payload[m["ref_key"]] = urls[0]      # grok: single image
        else:
            payload[m["ref_key"]] = urls[: m["max_refs"]]

    t0 = time.time()
    r = requests.post(
        f"https://api.replicate.com/v1/models/{m['slug']}/predictions",
        headers={**H, "Prefer": "wait"},
        json={"input": payload}, timeout=timeout)
    if r.status_code >= 400:
        return dict(model=model, status="http_error",
                    error=f"{r.status_code} {r.text[:400]}")
    pred = r.json()

    # Prefer:wait may still return before completion — poll if needed.
    while pred.get("status") in ("starting", "processing"):
        if time.time() - t0 > timeout:
            return dict(model=model, status="timeout")
        time.sleep(2)
        pred = requests.get(pred["urls"]["get"], headers=H, timeout=60).json()

    elapsed = time.time() - t0
    if pred.get("status") != "succeeded":
        return dict(model=model, status=pred.get("status"),
                    error=str(pred.get("error"))[:400], seconds=round(elapsed, 1))

    out = pred["output"]
    urls = [out] if isinstance(out, str) else list(out)
    return dict(model=model, status="ok", seconds=round(elapsed, 1),
                urls=urls, price=m["price"],
                metrics=pred.get("metrics", {}), logs=(pred.get("logs") or "")[-600:],
                pred_id=pred.get("id"))


def download(url, dest):
    dest = pathlib.Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(requests.get(url, timeout=180).content)
    return dest


def run_suite(name, prompt, models, refs=(), aspect="2:3", outdir=None):
    """Run one prompt across many models in parallel; save images + manifest."""
    outdir = pathlib.Path(outdir or ROOT / "results" / name)
    outdir.mkdir(parents=True, exist_ok=True)
    results = {}
    with cf.ThreadPoolExecutor(max_workers=len(models)) as ex:
        futs = {ex.submit(run, m, prompt, refs, aspect): m for m in models}
        for f in cf.as_completed(futs):
            m = futs[f]
            try:
                res = f.result()
            except Exception as e:
                res = dict(model=m, status="exception", error=repr(e)[:400])
            if res.get("status") == "ok":
                res["files"] = [
                    str(download(u, outdir / f"{m}{'' if i == 0 else f'_{i}'}.png"))
                    for i, u in enumerate(res["urls"])]
            results[m] = res
            flag = "ok " if res.get("status") == "ok" else "ERR"
            print(f"  [{flag}] {m:20} {res.get('seconds','-'):>6}s  "
                  f"${res.get('price',0):.3f}  {res.get('error','')[:90]}")
    (outdir / "manifest.json").write_text(json.dumps(
        {"test": name, "prompt": prompt, "refs": [str(r) for r in refs],
         "aspect": aspect, "results": results}, indent=1))
    return results
