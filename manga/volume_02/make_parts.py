"""Split the full-resolution volume PDF into deliverable parts.

The whole volume is ~57 MB and the file-delivery cap is 30 MB. Grouping is by MEASURED
OUTPUT size, not by source PNG bytes — PIL recompresses on save, so a chapter's PNGs on disk
run roughly twice its share of the finished PDF and packing by source size over-splits.
"""
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE.parent / "chapters"
PARTS = [["v2ch01", "v2ch02", "v2ch03"], ["v2ch04", "v2ch05", "v2ch06"], ["v2ch07"]]

for i, chs in enumerate(PARTS, 1):
    ps = [p for c in chs for p in sorted((CH / c / "raw").glob("p*.png"))]
    ims = [Image.open(p).convert("RGB") for p in ps]
    f = HERE / f"Volume_02_part{i}_of_{len(PARTS)}.pdf"
    ims[0].save(f, save_all=True, append_images=ims[1:], resolution=150.0)
    print(f"part {i}: {len(ps)} pages, {f.stat().st_size/1e6:.1f} MB -> {f.name}")
