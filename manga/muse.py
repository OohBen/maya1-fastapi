"""Muse Image backend + test harness.

Muse is $0.01 flat per image regardless of reasoning_strength, so we always ask for "high" —
there is never a reason to pay the same price for a single-pass render. It is also agentic with
built-in web/image search, which is the interesting part for this project: it can look up real
Naruto colour pages itself instead of being told about them in 3000 characters of prose.
"""
import base64
import json
import pathlib
import time

import requests

HERE = pathlib.Path(__file__).resolve().parent
KEY = next(l.split("=", 1)[1].strip() for l in (HERE / ".env").read_text().splitlines()
           if l.startswith("MUSE_API_KEY"))
SPEND_LOG = HERE / "models" / "muse_spend.json"
PRICE = 0.01


def _log(n, tag):
    SPEND_LOG.parent.mkdir(parents=True, exist_ok=True)
    d = json.loads(SPEND_LOG.read_text()) if SPEND_LOG.exists() else {"images": 0, "runs": []}
    d["images"] += n
    d["runs"].append({"tag": tag, "n": n})
    SPEND_LOG.write_text(json.dumps(d, indent=1))
    return d["images"] * PRICE


def spent():
    if not SPEND_LOG.exists():
        return 0.0
    return json.loads(SPEND_LOG.read_text())["images"] * PRICE


def generate(prompt, refs=(), size="1152x2048", tag="untagged", fmt="png", timeout=900):
    """Returns (png_bytes, cost). refs are local file paths used as reference images."""
    body = {"model": "muse-image-1.0", "prompt": prompt, "n": 1,
            "reasoning_strength": "high", "size": size, "output_format": fmt}
    if refs:
        body["images"] = [
            {"image_url": "data:image/png;base64,"
                          + base64.b64encode(pathlib.Path(r).read_bytes()).decode()}
            for r in refs
        ]
        url = "https://api.meta.ai/v1/images/edits"
    else:
        url = "https://api.meta.ai/v1/images/generations"
    t0 = time.time()
    r = requests.post(url, headers={"Authorization": f"Bearer {KEY}",
                                    "Content-Type": "application/json"},
                      json=body, timeout=timeout)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:400]}")
    total = _log(1, tag)
    img = base64.b64decode(r.json()["data"][0]["b64_json"])
    print(f"  [{tag}] {time.time()-t0:.0f}s  {len(img)//1024}KB  muse total ${total:.2f}")
    return img, PRICE


def page_prompt(chapter, pid):
    """Rebuild a page's exact production prompt from its builder, without running it."""
    import sys
    sys.path[:0] = [str(HERE), str(HERE / "chapters"), str(HERE / "refs")]
    src = (HERE / "chapters" / f"build_v5{chapter}.py").read_text()
    src = src[:src.index("if __name__")]
    ns = {"__name__": "notmain", "__file__": str(HERE / "chapters" / f"build_v5{chapter}.py")}
    exec(compile(src, f"build_v5{chapter}.py", "exec"), ns)
    from genlib import SPLASH, STAGING, STYLE
    pid_, want, desc, refs, quality = next(p for p in ns["PAGES"] if p[0] == pid)
    stage = SPLASH if want.get("panels") == 1 else STAGING
    return desc, stage, STYLE, refs, quality


def _ref_data_url(path, max_edge=768, quality=82):
    """Downscale a reference sheet before sending. Identity cues survive; payload does not need to."""
    from PIL import Image
    import io
    im = Image.open(path).convert("RGB")
    if max(im.size) > max_edge:
        im.thumbnail((max_edge, max_edge), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def generate_captioned(blocks, tag="untagged", size="1152x2048", fmt="png", timeout=900, tries=4):
    """Responses API: interleave text and images so each reference is captioned INLINE.

    The images/edits endpoint takes an unlabelled array, so binding relies on "Image {i}" text
    sitting thousands of characters away from the picture — which is exactly how Jiraiya and
    Kakashi merged. Here each caption sits immediately before its own image.

    blocks: list of ("text", str) and ("image", path) tuples, in the order the model should read.
    """
    content = []
    for kind, val in blocks:
        if kind == "text":
            content.append({"type": "input_text", "text": val})
        else:
            content.append({"type": "input_image", "image_url": _ref_data_url(val)})
    body = {"model": "muse-image-1.0", "input": [{"role": "user", "content": content}],
            "store": False,
            "tools": [{"type": "image_generation", "reasoning_strength": "high",
                       "output_format": fmt}]}
    t0 = time.time()
    for attempt in range(1, tries + 1):
        r = requests.post("https://api.meta.ai/v1/responses",
                          headers={"Authorization": f"Bearer {KEY}",
                                   "Content-Type": "application/json"},
                          json=body, timeout=timeout)
        if r.status_code == 200:
            break
        if "content_policy" in r.text and attempt < tries:
            print(f"  [{tag}] filtered, retrying ({attempt}/{tries - 1})")
            continue
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:400]}")
    out = r.json()["output"]
    b64 = next(o["result"] for o in out if o["type"] == "image_generation_call")
    note = next((s["text"] for o in out if o["type"] == "reasoning"
                 for s in o.get("summary", [])), "")
    total = _log(1, tag)
    img = base64.b64decode(b64)
    print(f"  [{tag}] {time.time()-t0:.0f}s  {len(img)//1024}KB  ${total:.2f}"
          + (f"  | {note[:90]}" if note else ""))
    return img, PRICE


import re as _re

# Sheets that show several states at once are ambiguous: handing the model a progression strip that
# contains a blue eye and asking for a red one is why the Sharingan kept coming back blue. Where a
# single-state crop exists, prefer it.
SINGLE_STATE = {"sharingan_progression": "eye_3tomoe"}


def captioned_page(chapter, pid, extra_refs=(), eye="eye_3tomoe"):
    """Build Responses-API blocks for a page: every reference captioned inline, immediately
    before its own image, instead of relying on 'Image {i}' index text far away in the prompt."""
    import sys
    sys.path[:0] = [str(HERE), str(HERE / "chapters"), str(HERE / "refs")]
    desc, stage, style, refs, tier = page_prompt(chapter, pid)

    # pull each "Image {i} is the X REFERENCE for ...: ..." paragraph out of the body; it becomes
    # the caption for that same picture, in the same order the refs were passed.
    paras = _re.findall(r'(Image \{?\d+\}? is the .*?)(?=Image \{?\d+\}? is the |$)', desc, _re.S)
    body = desc
    for p in paras:
        body = body.replace(p, "")
    caps = [_re.sub(r'^Image \{?\d+\}? is the ', 'THIS IMAGE IS THE ', p).strip() for p in paras]

    blocks = [("text",
        "Draw ONE finished manga page, PORTRAIT and TALL (about 9 wide by 16 high).\n"
        "First study these reference images. Each caption describes the image that comes "
        "immediately after it. These are DIFFERENT PEOPLE and must never blend into one another: "
        "do not give one character another's hair, mask, vest, headband or facial markings.\n")]
    for i, r in enumerate(refs):
        stem = pathlib.Path(r).stem
        p = HERE / "refs" / "images" / f"{SINGLE_STATE.get(stem, stem)}.png"
        if not p.exists():
            continue
        blocks.append(("text", caps[i] if i < len(caps) else f"Reference for {stem}:"))
        blocks.append(("image", str(p)))
    for x in extra_refs:
        blocks.append(("text", x[0])); blocks.append(("image", x[1]))
    eye_p = HERE / "refs" / "images" / f"{eye}.png"
    if eye_p.exists():
        blocks.append(("text",
            "THIS IMAGE IS THE EYE DESIGN. Wherever the page says a character's eye holds the "
            "ORDINARY ACTIVE THREE-TOMOE SHARINGAN, draw exactly this: a BLOOD-RED iris with a "
            "black pupil and THREE black comma-shaped tomoe evenly spaced around it. Never a plain "
            "red disc, never blue, never grey:"))
        blocks.append(("image", str(eye_p)))
    return blocks, body, stage, style, tier
