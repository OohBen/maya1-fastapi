"""Generation library for the manga pipeline.

Holds the prompt constants every page is built from — STYLE, STAGING, SPLASH, STYLE_REF —
and the refusal-escalation logic in build_page().

NOTE ON STRUCTURE: this module still contains the Replicate transport (rep_generate) and a
dead OpenRouter path (generate), for historical reasons. New code should NOT call either
directly — go through backend.generate(), which is the swappable seam. See AGENTS.md.

The OpenRouter `generate()` below is retained only because models/BENCH_REPORT.md refers to
it; it is unused and its API key may be exhausted.
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


try:                                    # dead OpenRouter path; must not break imports
    H = {"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"}
except Exception:                       # no .env / no key — fine, nothing uses it
    H = {}

# ---------------------------------------------------------------- house style
# STYLE HISTORY — read before changing this string.
#   V1-V4 used a "flat digital cel" string. The reader judged Volume 4 "decent... a good
#   starting ground", so that is the BASELINE.
#   A full swing to traditional watercolour was then tried and rejected: dark chamber pages went
#   seinen ink-wash and the bright daylight crowd page came back "terrible".
#   Current string = the Volume 4 baseline PLUS only the corrections that move it toward printed
#   colour manga without abandoning cel colouring: cream paper, screentone, simpler faces,
#   sparser backgrounds, matte finish. Work UP from here in small steps; do not swing again.
STYLE = (
    # STYLE HISTORY — do not swing this wholesale again; each revision was a reader response.
    # V4 baseline was approved as "decent". A full watercolour swing was rejected outright.
    # V5 revision added print/paper correction. THIS revision (V5.2) answers "it looks more like a
    # colour book than a manga": the previous text told the model to keep backgrounds LIGHTER and
    # MUTED than the figures, and it obeyed by leaving them as pale uncoloured line sketch behind
    # flat-filled characters — the exact pasted-on look that reads as a colouring book. The target
    # named by the reader is late-Shippuden Kishimoto colour work.
    "Premium 2D shonen manga artwork, full colour, in the style of a LATE-SERIES Naruto colour "
    "chapter — Kishimoto's mature Shippuden-era work, not his early style. "
    "Clean confident black ink linework with strongly varied line weight — brush-drawn, tapering "
    "and swelling, heavy where a form turns away from the light and fine on interior detail, "
    "never uniform-weight vector outlines. "
    "SOLID BLACKS: spot true black generously — in hair, in cast shadow, inside folds, under jaws "
    "and in the darkest corners of the panel. The page must carry real black weight, not only "
    "outlines around coloured shapes. "
    "COLOUR: cel-shaded with hard-edged shadow boundaries, but RICH — three or four values per "
    "material plus a reflected-light tone, deep saturated darks and clean lights. Not two flat "
    "fills with a line around them. Hair drawn as distinct clusters and wedges, never individual "
    "strands. "
    "THE WHOLE PANEL IS FINISHED TO THE SAME LEVEL. This is the most important rule here: the "
    "background is painted in full colour with the same cel-shaded finish, the same line quality "
    "and the same black weight as the characters. Buildings, ground, foliage, sky and interiors "
    "are COLOURED, never left as pale sepia or grey line sketch, never left as bare uncoloured "
    "pencil or etching behind coloured figures, and never washed out to a faint tint. Characters "
    "and their environment must look drawn and coloured by the same hand in the same pass, lit by "
    "the SAME light source, sharing one colour temperature, so the figures sit INSIDE the scene "
    "rather than being pasted on top of a sketch. "
    "DELIBERATE EMPTY PANELS ARE STILL ALLOWED and should be used for pace — a close-up may drop "
    "its background entirely for one flat saturated colour field, a black void, screentone or "
    "speed lines. That is a designed choice and must read as intentional; it is NOT the same "
    "thing as a scene rendered weakly. When a panel shows a place, that place is fully coloured. "
    "DEPTH: separate foreground, midground and background by VALUE and colour temperature — "
    "atmospheric recession, cooler and lighter with distance — rather than by leaving the "
    "distance uncoloured. "
    "PAPER: the page sits on a warm off-white paper tone, not pure digital white, with a matte "
    "printed finish rather than a glossy screen finish. "
    "SHADOW: use halftone screentone dots and parallel-line hatching within the shadow areas, over "
    "the colour rather than instead of it. "
    "PALETTE: clear readable colours, print-like rather than glowing or neon. "
    "FACES: simply drawn in Kishimoto's manner — large clear expressive eyes, a small minimal "
    "nose, a simple mouth, smooth cheeks and very little skin shading. Never a semi-realistic or "
    "painted portrait face. "
    "Avoid depth-of-field blur, avoid photorealistic skin texture, avoid any 3D or CGI look, "
    "avoid painterly or oil-paint rendering, avoid watercolour wash and ink-wash looks, avoid "
    "sepia or monochrome backgrounds, avoid lens flare, avoid watermarks and signatures."
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


class Moderated(RuntimeError):
    """The request was refused on content grounds. Retrying it unchanged cannot work."""


# Moderation refusals and transient failures both arrive as a failed prediction, but they need
# opposite handling: a timeout wants the same request again, a refusal wants a DIFFERENT request.
# Retrying a refusal just burns retries x style-candidates worth of calls before giving up.
_MOD_MARKERS = ("e005", "moderation", "content policy", "content_policy", "safety system",
                "flagged", "not allowed", "violates", "rejected as sensitive")


def _is_moderation(msg):
    m = (msg or "").lower()
    return any(k in m for k in _MOD_MARKERS)


def rep_generate(prompt, refs=(), quality="low", aspect="2:3", timeout=900, retries=3):
    """One page from gpt-image-2 on Replicate. Returns (png_bytes, cost).

    Raises Moderated immediately (no retries) if the request was refused on content grounds —
    the caller must change the prompt or the reference images, not try again.
    """
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
                if _is_moderation(last):
                    raise Moderated(last)
                time.sleep(5 * (attempt + 1)); continue
            pred = r.json()
            t0 = time.time()
            while pred.get("status") in ("starting", "processing"):
                if time.time() - t0 > timeout:
                    last = "timeout"; break
                time.sleep(3)
                pred = requests.get(pred["urls"]["get"], headers=h, timeout=60).json()
            if pred.get("status") != "succeeded":
                last = f"{pred.get('status')}: {str(pred.get('error'))[:300]}"
                if _is_moderation(last):
                    raise Moderated(last)
                time.sleep(5 * (attempt + 1)); continue
            out = pred["output"]
            url = out if isinstance(out, str) else out[0]
            return requests.get(url, timeout=180).content, REP_PRICE.get(quality, 0)
        except Moderated:
            raise
        except Exception as e:
            last = repr(e)[:300]
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"rep_generate failed — {last}")


# When a page IS refused, changing something means changing the words that read as real-world
# harm. These are the substitutions that have actually cleared refusals on fight pages.
SOFTEN = [
    ("blood", "dark spatter"), ("bloody", "dark-stained"), ("bleeding", "wounded"),
    ("gore", "damage"), ("corpse", "still figure"), ("dead body", "still figure"),
    ("stabs", "strikes"), ("stabbing", "striking"), ("stab", "strike"),
    ("slits his throat", "strikes him down"), ("throat", "collar"),
    ("kills", "defeats"), ("killing", "defeating"), ("kill", "defeat"),
    ("murder", "defeat"), ("slaughter", "rout"), ("execute", "finish"),
    ("impaled", "pinned"), ("impales", "pins"), ("severed", "broken"),
    ("wound", "mark"), ("wounds", "marks"), ("dying", "fading"), ("dies", "falls"),
]


def soften(prompt):
    """Rewrite a refused prompt into the same picture with less alarming words."""
    out = prompt
    for a, b in SOFTEN:
        out = out.replace(a, b).replace(a.capitalize(), b.capitalize())
        out = out.replace(a.upper(), b.upper())
    return out + ("Draw this as stylised printed comic action: no realistic injury detail, no red "
                  "fluid, no visible harm to any body. Impact is shown with flat graphic shapes, "
                  "motion lines and posture alone. ")


def build_page(prompt, refs, style_candidates, quality, aspect="1152x2048"):
    """Generate one page, escalating only when a refusal says the request must change.

    Transient failures are already retried inside rep_generate. This ladder handles refusals:

      1. prompt as written, best style reference
      2. refused -> NEXT style reference. The library page itself is often the trigger; a
         harmless empty-clearing page was refused once purely because of its style ref.
      3. still refused after three references -> soften the PROMPT and walk the references again
      4. still refused -> softened prompt with no style reference at all

    Returns (png_bytes, cost, style_ref_path_or_None).
    """
    heads = list(style_candidates[:3])
    attempts = [(prompt, c) for c in heads]
    attempts += [(soften(prompt), c) for c in heads]
    attempts += [(soften(prompt), None)]

    # Lazy import: backend imports genlib, so a module-level import would be circular.
    from backend import generate as _gen

    refused = None
    for text, cand in attempts:
        try:
            img, cost = _gen(text, refs=list(refs) + ([cand] if cand else []),
                             quality=quality, size=aspect)
            return img, cost, cand
        except Moderated as e:
            refused = str(e)[-120:]
        except RuntimeError as e:            # transient, already retried inside
            refused = str(e)[-120:]
    raise RuntimeError(f"all variants refused — {refused}")


# ---------------------------------------------------------------- style reference
# Prompt-only style control hit a ceiling (see PIPELINE.md and bench/results/t14_style).
# The fix is the same one that solved character consistency: a reference image. This clause
# binds a real colored-manga page as a STYLE-ONLY reference, with a hard ignore list so its
# content does not bleed into ours.
STYLE_REF = (
    "Image {i} is a STYLE REFERENCE ONLY — it is a real page from a printed colour manga, "
    "included solely to show you how to RENDER. Match its warm paper tone, its brush-inked line "
    "quality, its flat print-like colour, its halftone screentone, and its simply-drawn faces "
    "with large clear eyes and minimal nose detail. Your page should look like it was printed in "
    "the same book — if your output looks glossier, more saturated, more photographic or more "
    "digitally rendered than Image {i}, it is WRONG. "
    "Ignore absolutely everything else about Image {i}: ignore its characters and their designs, "
    "ignore their costumes and hair, ignore its panel layout, ignore its story content, and "
    "ignore all of its lettering and sound effects. Take only the drawing and colouring "
    "technique from it. "
)


# ---------------------------------------------------------------- staging
# Derived from refs/MANGA_STAGING_GUIDE.md: 42 pages read directly plus automated
# panel measurement over all 1119 library pages. These are the UNIVERSAL rules that
# belong on every page; per-page specifics come from the guide's §12 fragments.
# Volume 5's review gates found reversed panel order on roughly forty pages across seven
# chapters — consistently delivering an answer before the question it answers. The per-page
# RTL note was not enough on its own, so the contract is restated here, where every page
# gets it, as a rule about panel NUMBERS rather than about reading direction in the abstract.
RTL_LAW = (
    "PANEL ORDER IS A HARD RULE, NOT A PREFERENCE. This is a right-to-left manga page. "
    "Within any row of panels, a LOWER-NUMBERED panel is always further RIGHT than a "
    "higher-numbered one: PANEL 1 is the TOP-RIGHT panel, and the numbers increase "
    "leftward across each row before dropping to the next row down. PANEL 2 is never to the "
    "right of PANEL 1, PANEL 3 is never to the right of PANEL 2, and so on for every pair. "
    "A tall panel spanning two rows sits to the LEFT of the panels it is read after. "
    "The same rule governs balloons: within one panel, the balloon that is read first sits "
    "further RIGHT (or higher) than the one read after it. Getting this backwards makes the "
    "page deliver answers before their questions and is the single worst error you can make "
    "on this page. "
)

STAGING_BODY = (
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
    "FIGURES: THIRTEEN-YEAR-OLDS ARE ADOLESCENTS, NOT SMALL CHILDREN — draw them about six and a "
    "half heads tall, long-limbed, with adult proportions at teenage scale, standing roughly chin "
    "height to an adult. Never chibi, never squat, never big-headed, never toddler-proportioned. "
    "Young children under ten are about six heads tall, adults about seven and a half, with large "
    "simply-drawn hands and "
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

STAGING = RTL_LAW + STAGING_BODY

# STAGING always wins an argument with "draw one illustration" — it says "panels" nine times, so
# splash pages came back as six-panel grids of the same subject (v2ch01 p01, v2ch02 p01). Splash
# pages get THIS instead of STAGING, never both.
SPLASH = (
    "THIS PAGE IS A SINGLE SPLASH ILLUSTRATION. It has NO panels, NO panel borders, NO gutters and "
    "NO divisions of any kind. One continuous drawing bleeds off all four edges of the paper. Do "
    "not repeat the subject at several angles — this is one view, once. "
    "COMPOSE IT LIKE A CHAPTER OPENER: a strong diagonal or a steep low angle, a large foreground "
    "mass cropped by the edge of the paper, deep space behind it, and one clear focal figure or "
    "shape placed well off centre. Leave one broad quiet area of sky, wall or ground for the title. "
    "RENDER: heavy black brush inking, flat colour fills, halftone dot texture in the shadows, "
    "parallel-line hatching. No gradients, no glow, no blur. "
)
