"""Export a LoRA training set from the finished volumes.

Most people hand-caption a LoRA dataset. We don't have to: every finished page was produced by
a deterministic prompt that still exists in `chapters/build_*.py`, so image and caption can be
paired exactly by re-deriving the prompt for each page that made it to disk.

    python3 build_lora_dataset.py --out lora/style.zip                 # style+layout set
    python3 build_lora_dataset.py --out lora/naruto.zip --refs-only    # character sheets

Output is a flat zip of `NNN.png` + `NNN.txt`, which is the format both the fal.ai Klein trainer
and the Replicate FLUX.1 trainer expect.

CAPTIONING NOTE. The full page prompt is ~4000 characters of panel-by-panel staging. That is far
longer than a training caption should be — trainers truncate hard (often ~77-256 tokens) and a
caption that describes panel contents teaches the LoRA to associate our *style* with one
specific scene. So by default we emit a SHORT caption built from the trigger word plus the
page's style-query facts (scene type, lighting, cast size, mood, panel count), which is what we
actually want the LoRA to learn. Use --full-captions to emit the raw prompt instead.
"""
import argparse
import importlib.util
import io
import pathlib
import re
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "chapters"))
sys.path.insert(0, str(HERE / "refs"))

TRIGGER = "uchmanga"   # the token that will summon this style at inference time


def load_chapter(path):
    """Import a build_*.py without running its __main__ block, return its PAGES."""
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:                      # a chapter that no longer imports is skipped
        print(f"  ! {path.name}: {str(e)[:70]}")
        return []
    return getattr(mod, "PAGES", [])


def short_caption(want):
    """Style-and-layout caption. Deliberately not scene-specific — see module docstring."""
    bits = [TRIGGER, "colour manga page"]
    n = want.get("panels")
    if n == 1:
        bits.append("full-page splash illustration, no panel borders")
    elif n:
        bits.append(f"{n} uneven panels filling the page, thin white gutters")
    for key, label in (("scene", ""), ("mood", ""), ("light", "lighting"), ("cast", "cast")):
        v = want.get(key)
        if v:
            bits.append(f"{str(v).replace('_', ' ')} {label}".strip())
    bits += ["black ink linework", "flat cel colour", "halftone screentone"]
    return ", ".join(bits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="lora/style.zip")
    ap.add_argument("--refs-only", action="store_true",
                    help="export refs/images/*.png (character sheets) instead of story pages")
    ap.add_argument("--full-captions", action="store_true",
                    help="emit the raw page prompt as the caption (usually a mistake — see docstring)")
    ap.add_argument("--min-side", type=int, default=1024,
                    help="skip images whose short side is below this (trainers want >=1024)")
    ap.add_argument("--best", type=int, default=0,
                    help="curate to N pages: drop Volume 1, prefer higher quality tiers. "
                         "fal recommends 9-50 for a style LoRA — 413 pages is far too many.")
    ap.add_argument("--max-mb", type=int, default=0,
                    help="downscale longest side until the zip fits roughly this many MB")
    a = ap.parse_args()

    from PIL import Image
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    pairs = []      # (image_path, caption)

    if a.refs_only:
        for p in sorted((HERE / "refs" / "images").glob("*.png")):
            name = p.stem
            kind = "environment plate, no people" if name.startswith("env_") else "character reference sheet, three views, plain white background"
            pairs.append((p, f"{TRIGGER}, {kind}, {name.replace('_', ' ')}, "
                             f"black ink linework, flat cel colour"))
    else:
        for build in sorted((HERE / "chapters").glob("build_*.py")):
            cid = re.sub(r"^build_", "", build.stem)
            raw = HERE / "chapters" / cid / "raw"
            if not raw.exists():
                continue
            pages = load_chapter(build)
            found = 0
            for spec in pages:
                # Volume 1 chapters use a different tuple shape than V2/V3 — the style-query
                # dict is only present from Volume 2 onward. Tolerate both.
                pid = spec[0]
                want = next((x for x in spec[1:3] if isinstance(x, dict)), {})
                body = next((x for x in spec[1:4] if isinstance(x, str)), "")
                img = raw / f"{pid}.png"
                if not img.exists():
                    continue
                cap = body if (a.full_captions and body) else short_caption(want)
                pairs.append((img, cap))
                found += 1
            if found:
                print(f"  {cid}: {found} pages")

    if a.best and not a.refs_only:
        # Volume 1 is excluded outright: the reader rejected its art as "not good enough", so
        # training on it would teach the LoRA the look we moved away from. Within what is left,
        # prefer the tiers we spent most on, which are the pages that were worth the money.
        import json as _json
        rank = {"high": 0, "medium": 1, "low": 2}
        tier = {}
        for led in (HERE / "chapters").glob("*/ledger.json"):
            cid = led.parent.name
            for row in _json.load(led.open()):
                tier[(cid, row.get("page"))] = row.get("quality", "low")
        def key(item):
            pth = item[0]
            cid, pid = pth.parent.parent.name, pth.stem
            return (rank.get(tier.get((cid, pid), "low"), 3), cid, pid)
        pairs = [x for x in pairs if not re.match(r"^ch\d\d$", x[0].parent.parent.name)]
        pairs.sort(key=key)
        pairs = pairs[:a.best]
        print(f"  curated -> {len(pairs)} pages (Volume 1 excluded, best tiers first)")

    kept = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for i, (p, cap) in enumerate(pairs):
            try:
                w, h = Image.open(p).size
            except Exception:
                continue
            if min(w, h) < a.min_side:
                continue
            if a.max_mb:
                im = Image.open(p).convert("RGB")
                im.thumbnail((1536, 1536), Image.LANCZOS)
                buf = io.BytesIO(); im.save(buf, "JPEG", quality=92)
                z.writestr(f"{i:04d}.jpg", buf.getvalue())
                z.writestr(f"{i:04d}.txt", cap)
            else:
                z.write(p, f"{i:04d}.png")
                z.writestr(f"{i:04d}.txt", cap)
            kept += 1

    mb = out.stat().st_size / 1e6
    print(f"\n{kept} image/caption pairs -> {out} ({mb:.0f} MB)")
    print(f"trigger word: {TRIGGER}")
    if kept and not a.refs_only:
        print("\nsample caption:")
        print("  " + pairs[0][1][:200])


if __name__ == "__main__":
    main()
