"""MAI-Image-2.6 (Azure) backend. EVALUATED, NOT ADOPTED — see models/MAI_REPORT.md.

Endpoint quirks found by probing, all load-bearing:
  * /images/generations IGNORES `size` and always returns 1024x1024 — useless for manga pages.
  * /images/edits (multipart) DOES honour `size` and accepts reference images, so all real work
    goes through edits, passing references even when there is nothing to "edit".
  * The edits endpoint accepts 1-5 image files. Our pages bind 6-10, so references are triaged:
    character sheets carry identity and are kept; environment plates are dropped first because
    they are the most recoverable from prose.
  * Rate limit is 2 requests/minute (MAI_MIN_GAP), so calls are paced, not parallelised.

Content filtering: some pages are refused under a SEXUAL label despite containing nothing
sexual — a conversation scene between four characters was refused deterministically, three times
out of three. DO NOT try to reword prompts to get past this. In particular, do not strip or soften
the wording that establishes a character's age: it is load-bearing for how the character is drawn,
and removing age markers to stop a sexual-content classifier firing is exactly the pattern that
would hide a real problem if one ever existed. The supported response to a refusal is to render
that page with another backend (see backend.py) and move on.
"""
import base64
import io
import pathlib
import time

import requests
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
_env = dict(l.strip().split("=", 1) for l in (HERE / ".env").read_text().splitlines()
            if "=" in l and not l.startswith("#"))
KEY = _env["MAI_KEY"]
GEN = _env["MAI_ENDPOINT"]
EDITS = GEN.replace("/images/generations", "/images/edits")
MODEL = "MAI-Image-2.6"
FLASH = "MAI-Image-2.6-flash"
_last = [0.0]
MIN_GAP = 31.0          # 2 rpm
MAX_REFS = 5            # endpoint rejects >5 image files


def _ref_bytes(p, edge=768):
    im = Image.open(p).convert("RGB")
    im.thumbnail((edge, edge), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, format="PNG")
    return b.getvalue()


def generate(prompt, refs=(), size="1024x1536", tag="untagged", timeout=900,
             model=None, gap=None):
    wait = (MIN_GAP if gap is None else gap) - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    refs = list(refs)
    if len(refs) > MAX_REFS:
        env = [r for r in refs if pathlib.Path(r).stem.startswith("env_")]
        chars = [r for r in refs if r not in env]
        refs = (chars + env)[:MAX_REFS]
    files = [("image", (pathlib.Path(r).name, _ref_bytes(r), "image/png")) for r in refs]
    data = {"model": model or MODEL, "prompt": prompt, "n": "1", "size": size}
    t0 = time.time()
    r = requests.post(EDITS if files else GEN,
                      headers={"api-key": KEY},
                      data=data if files else None,
                      json=None if files else {**data, "n": 1},
                      files=files or None, timeout=timeout)
    _last[0] = time.time()
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
    d = r.json()
    img = base64.b64decode(d["data"][0]["b64_json"])
    print(f"  [{tag}] {time.time()-t0:.0f}s  {len(img)//1024}KB  {d.get('size')}")
    return img
