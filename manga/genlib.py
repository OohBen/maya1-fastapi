"""Generation library for the manga pipeline.

Uses the OpenRouter Responses API with the image_generation tool, because it is the
only path that emits MULTIPLE images from a single request under one shared reasoning
pass — which is what holds continuity across a run of sequential pages.

See models/BENCH_REPORT.md addendum for why the plain images endpoint can't do this.
"""
import base64
import json
import os
import pathlib
import time

import requests

os.environ.setdefault("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt")
os.environ.setdefault("REQUESTS_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")

ROOT = pathlib.Path(__file__).resolve().parent
URL = "https://openrouter.ai/api/v1/responses"


def _key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("OPENROUTER_API_KEY missing from manga/.env")


H = {"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"}

# ---------------------------------------------------------------- house style
STYLE = (
    "Premium 2D shonen manga artwork, full colour. "
    "Clean confident black ink linework with varied line weight. "
    "Flat digital cel colouring: two to three tonal values per material, hard-edged shadows, "
    "no soft gradients. Hair drawn as distinct clusters and wedges, never individual strands. "
    "Avoid depth-of-field blur, avoid photorealistic skin texture, avoid any 3D or CGI look, "
    "avoid painterly or oil-paint rendering, avoid lens flare, avoid watermarks and signatures."
)

# Never write emphatic capitalised "NO" — text-rendering models draw the token.
# See BENCH_REPORT.md prompt lessons.
NO_TEXT = (
    "The image must be entirely free of writing: no letters, words, numerals or symbols anywhere."
)

UNIQUE = (
    "This is the only character in the image who looks like this. Every other person present must "
    "look completely different from him, with different hair colour, different clothing and a "
    "different face."
)


def _data_uri(path):
    b = pathlib.Path(path).read_bytes()
    return "data:image/png;base64," + base64.b64encode(b).decode()


def generate(prompt, refs=(), n=1, quality="low", model="openai/gpt-5.6",
             timeout=1800, retries=3):
    """Return a list of PNG byte strings.

    refs : local image paths fed in as visual references.
    n    : how many images to ask for. The prompt must describe each one.
    """
    content = [{"type": "input_text", "text": prompt}]
    for r in refs:
        content.append({"type": "input_image", "image_url": _data_uri(r)})

    body = {
        "model": model,
        "input": [{"role": "user", "content": content}],
        "tools": [{"type": "image_generation", "quality": quality}],
    }
    if n > 1:
        body["n"] = n

    last = None
    for attempt in range(retries):
        try:
            r = requests.post(URL, headers=H, json=body, timeout=timeout)
            if r.status_code >= 400:
                last = f"HTTP {r.status_code}: {r.text[:300]}"
                time.sleep(4 * (attempt + 1))
                continue
            # OpenRouter pads long responses with keepalive whitespace, which can
            # trip a strict JSON parse. Find the actual object.
            try:
                d = r.json()
            except ValueError:
                txt = r.text
                i = txt.find("{")
                if i < 0:
                    last = "no JSON object in response"
                    time.sleep(4 * (attempt + 1))
                    continue
                d = json.loads(txt[i:])
            imgs = []
            for o in d.get("output", []):
                if "image" not in str(o.get("type", "")):
                    continue
                res = o.get("result") or ""
                if res.startswith("data:"):
                    res = res.split(",", 1)[1]
                if len(res) > 500:
                    imgs.append(base64.b64decode(res))
            if imgs:
                return imgs, (d.get("usage") or {}).get("cost", 0.0)
            last = "no images in response: " + str(
                [o.get("type") for o in d.get("output", [])])
        except Exception as e:  # network / decode
            last = repr(e)[:300]
        time.sleep(4 * (attempt + 1))
    raise RuntimeError(f"generate failed after {retries} tries — {last}")


def save(images, outdir, names):
    """Write images to outdir under the given names; returns written paths."""
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    paths = []
    for img, name in zip(images, names):
        p = outdir / f"{name}.png"
        p.write_bytes(img)
        paths.append(p)
    return paths


class Ledger:
    """Append-only cost + provenance log. Every call gets recorded."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.rows = json.loads(self.path.read_text()) if self.path.exists() else []

    def add(self, **kw):
        self.rows.append(kw)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.rows, indent=1))

    @property
    def spent(self):
        return sum(r.get("cost", 0) or 0 for r in self.rows)


# ---------------------------------------------------------------- Replicate path
# The Responses API image tool silently uses "GPT-5 Image" at a flat ~$0.251/image and
# IGNORES the quality parameter, so it has no cost control. For page production we go
# direct to gpt-image-2 on Replicate: quality tiers work, references are free, and low
# is $0.012/image. Verified against the OpenRouter dashboard, not the response body.
REPLICATE_URL = "https://api.replicate.com/v1/models/openai/gpt-image-2/predictions"


def _rep_key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("REPLICATE_API_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("REPLICATE_API_TOKEN missing from manga/.env")


REP_PRICE = {"low": 0.012, "medium": 0.047, "high": 0.128}


def rep_generate(prompt, refs=(), quality="low", aspect="2:3", timeout=900, retries=3):
    """One page from gpt-image-2 on Replicate. Returns (png_bytes, cost)."""
    h = {"Authorization": f"Bearer {_rep_key()}", "Content-Type": "application/json",
         "Prefer": "wait"}
    payload = {"prompt": prompt, "aspect_ratio": aspect, "quality": quality,
               "output_format": "png", "moderation": "low", "number_of_images": 1}
    if refs:
        payload["input_images"] = [_data_uri(r) for r in refs]

    last = None
    for attempt in range(retries):
        try:
            r = requests.post(REPLICATE_URL, headers=h, json={"input": payload}, timeout=timeout)
            if r.status_code >= 400:
                last = f"HTTP {r.status_code}: {r.text[:300]}"
                time.sleep(5 * (attempt + 1)); continue
            pred = r.json()
            t0 = time.time()
            while pred.get("status") in ("starting", "processing"):
                if time.time() - t0 > timeout:
                    last = "timeout"; break
                time.sleep(3)
                pred = requests.get(pred["urls"]["get"], headers=h, timeout=60).json()
            if pred.get("status") != "succeeded":
                last = f"{pred.get('status')}: {str(pred.get('error'))[:200]}"
                time.sleep(5 * (attempt + 1)); continue
            out = pred["output"]
            url = out if isinstance(out, str) else out[0]
            return requests.get(url, timeout=180).content, REP_PRICE.get(quality, 0)
        except Exception as e:
            last = repr(e)[:300]
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"rep_generate failed — {last}")


# ---------------------------------------------------------------- style reference
# Prompt-only style control hit a ceiling (see PIPELINE.md and bench/results/t14_style).
# The fix is the same one that solved character consistency: a reference image. This clause
# binds a real colored-manga page as a STYLE-ONLY reference, with a hard ignore list so its
# content does not bleed into ours.
STYLE_REF = (
    "Image {i} is a STYLE REFERENCE ONLY — it is a page from a printed colour manga, included "
    "solely to show you how to RENDER. Copy its rendering technique exactly: thin black panel "
    "borders sitting on a white paper background, flat solid colour fills with no gradients, "
    "halftone screentone dot texture in the shadow areas, parallel-line hatching instead of soft "
    "shading, heavy black brush inking with clear line-weight variation, and simplified faces "
    "with small simple eyes and minimal nose detail. Match its slightly desaturated print-like "
    "palette rather than a glowing digital one. "
    "Ignore absolutely everything else about Image {i}: ignore its characters and their designs, "
    "ignore their costumes and hair, ignore its panel layout, ignore its story content, and "
    "ignore all of its lettering and sound effects. Take only the drawing and colouring "
    "technique from it. "
)


# ---------------------------------------------------------------- staging
# Derived from refs/MANGA_STAGING_GUIDE.md: 42 pages read directly plus automated
# panel measurement over all 1119 library pages. These are the UNIVERSAL rules that
# belong on every page; per-page specifics come from the guide's §12 fragments.
STAGING = (
    "PAGE ARCHITECTURE: the block of panels FILLS THE WHOLE PAGE, running out to a narrow even "
    "margin on all four sides, separated only by THIN white gutters. Never leave broad empty white "
    "fields around or between panels — the page must read as a dense printed comic page, not as "
    "panels floating on paper. Panels sit in uneven rows whose column positions do not line up, and "
    "their sizes are markedly unequal, with one panel clearly dominant. Thin black borders. "
    "Choose the panel count from what the beat needs — busier pages run six to nine, quieter ones "
    "fewer — but never a stack of equal horizontal bands. "
    "GROUPS ARE NEVER A ROW: stage characters at clearly different depths with a large scale "
    "difference between nearest and farthest, overlapping each other, at least one figure cropped "
    "by the panel edge showing only a shoulder or the back of a head, and at least one turned away "
    "from camera. Nobody stands evenly spaced facing the viewer. "
    "BACKGROUNDS: do not render full scenery in every panel. Many panels — especially close-ups — "
    "drop the environment entirely for blank paper, one flat tone with halftone dots, a flat black "
    "void, or nothing but speed lines. Use this to control pace, not as a quota: an empty panel "
    "should isolate a beat, never just sit there dead. "
    "ENERGY AND IMPACT: draw effects as flat opaque shapes with hard black outlines, layered in "
    "front of and behind the figure. Effects must NOT glow and must not wash the scene out — the "
    "ground, the characters and the sky stay fully drawn and legible through and around them. "
    "FIGURES: children about six heads tall, adults about seven, with large simply-drawn hands and "
    "feet. Weight off-centre, body twisted along a diagonal, at least one limb cropped by the panel "
    "edge. No symmetrical standing poses. "
    "FACES: huge white sclera with a small iris and a dot pupil; shadow as parallel hatch lines on "
    "the cheeks and under the eyes; no gradients, no highlights, no rim light. Escalate emotion by "
    "CROPPING TIGHTER and turning the head away, never by adding rendering. "
    "BALLOONS ARE STAGING: let balloons occupy the upper half of a panel and push the figure low "
    "and to one side. "
    "SFX ARE COMPOSITIONAL MASS: sound effects overlap figures, are cropped by panel edges, and may "
    "cross a gutter from one panel into the next. Never a small effect floating in an empty gap. "
)
