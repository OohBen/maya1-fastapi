"""Deterministic lettering pass.

The image model is never allowed to write text — it leaves clean empty balloons and we
composite dialogue in afterwards. This eliminates gibberish lettering, duplicated
balloons, wrong-speaker attribution and inconsistent fonts in one move.

Balloons are found automatically: large near-white blobs with a dark outline, sitting
inside the page rather than on the margin.
"""
import pathlib

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = pathlib.Path("/usr/share/fonts/truetype")
BODY = FONT_DIR / "liberation" / "LiberationSans-Bold.ttf"
TITLE = FONT_DIR / "dejavu" / "DejaVuSerif-Bold.ttf"


def find_balloons(img, min_frac=0.004, max_frac=0.16):
    """Return balloon boxes (x0,y0,x1,y1), largest first.

    Looks for connected near-white regions away from the page edge. Uses a simple
    flood-fill label pass so we don't need scipy.
    """
    a = np.asarray(img.convert("L"))
    h, w = a.shape
    white = a > 233
    # ignore a margin band — page gutters are white too
    m = int(min(h, w) * 0.035)
    mask = np.zeros_like(white)
    mask[m:h - m, m:w - m] = white[m:h - m, m:w - m]

    seen = np.zeros_like(mask, dtype=bool)
    boxes = []
    area_total = h * w
    ys, xs = np.nonzero(mask)
    for y0, x0 in zip(ys[::7], xs[::7]):          # sparse seeding is enough
        if seen[y0, x0]:
            continue
        # iterative flood fill over a coarse grid, then refine bbox
        stack = [(y0, x0)]
        seen[y0, x0] = True
        minx = maxx = x0
        miny = maxy = y0
        n = 0
        while stack:
            y, x = stack.pop()
            n += 1
            if n > 400000:
                break
            if x < minx: minx = x
            if x > maxx: maxx = x
            if y < miny: miny = y
            if y > maxy: maxy = y
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    stack.append((ny, nx))
        bw, bh = maxx - minx, maxy - miny
        if bw < 40 or bh < 30:
            continue
        frac = (bw * bh) / area_total
        if not (min_frac <= frac <= max_frac):
            continue
        fill = n / max(bw * bh, 1)
        if fill < 0.55:                            # balloons are convex-ish blobs
            continue
        if bw / max(bh, 1) > 4 or bh / max(bw, 1) > 4:
            continue
        boxes.append((minx, miny, maxx, maxy))
    boxes.sort(key=lambda b: -( (b[2]-b[0]) * (b[3]-b[1]) ))
    return boxes


def _wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if draw.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = wd
    if cur:
        lines.append(cur)
    return lines


def fit_text(draw, box, text, font_path=BODY, pad=0.16, max_pt=44, min_pt=11):
    """Largest point size that fits the text inside box; returns (lines, font, lh)."""
    x0, y0, x1, y1 = box
    bw, bh = (x1 - x0), (y1 - y0)
    inner_w, inner_h = bw * (1 - 2 * pad), bh * (1 - 2 * pad)
    for pt in range(max_pt, min_pt - 1, -1):
        f = ImageFont.truetype(str(font_path), pt)
        lines = _wrap(draw, text, f, inner_w)
        lh = int(pt * 1.22)
        if len(lines) * lh <= inner_h:
            return lines, f, lh
    f = ImageFont.truetype(str(font_path), min_pt)
    return _wrap(draw, text, f, inner_w), f, int(min_pt * 1.22)


def letter_page(src, dialogue, dest):
    """dialogue: list of strings, assigned to balloons in reading order."""
    img = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(img)
    boxes = find_balloons(img)
    # reading order: top-to-bottom, then left-to-right within a band
    band = img.height * 0.08
    boxes.sort(key=lambda b: (round(b[1] / band), b[0]))
    used = 0
    for box, text in zip(boxes, dialogue):
        lines, font, lh = fit_text(d, box, text)
        x0, y0, x1, y1 = box
        cy = (y0 + y1) / 2 - (len(lines) * lh) / 2
        for i, ln in enumerate(lines):
            tw = d.textlength(ln, font=font)
            d.text(((x0 + x1) / 2 - tw / 2, cy + i * lh), ln, font=font, fill=(15, 15, 15))
        used += 1
    dest = pathlib.Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)
    return used, len(boxes)


def title_plate(src, dest, title, subtitle=None, chapter=None):
    """Composite the chapter title into the reserved upper area."""
    img = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(img)
    W, H = img.size
    f_title = ImageFont.truetype(str(TITLE), int(W * 0.082))
    f_sub = ImageFont.truetype(str(BODY), int(W * 0.030))
    f_ch = ImageFont.truetype(str(BODY), int(W * 0.024))

    y = int(H * 0.085)
    if chapter:
        tw = d.textlength(chapter, font=f_ch)
        d.text((W / 2 - tw / 2, y), chapter, font=f_ch, fill=(214, 196, 160))
        y += int(W * 0.052)
    for line in title.split("\n"):
        tw = d.textlength(line, font=f_title)
        # soft dark backing so the type reads over sky
        d.text((W / 2 - tw / 2 + 3, y + 3), line, font=f_title, fill=(0, 0, 0))
        d.text((W / 2 - tw / 2, y), line, font=f_title, fill=(245, 240, 230))
        y += int(W * 0.095)
    if subtitle:
        tw = d.textlength(subtitle, font=f_sub)
        d.text((W / 2 - tw / 2, y + int(W * 0.012)), subtitle, font=f_sub,
               fill=(198, 176, 140))
    dest = pathlib.Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)
    return dest
