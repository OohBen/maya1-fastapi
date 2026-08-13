"""Split the full-resolution Volume 3 PDF into deliverable parts.

The whole volume is ~44 MB and the file-delivery cap is 30 MB. Grouping is by MEASURED
OUTPUT size, not by source PNG bytes — PIL recompresses on save, so packing by source size
over-splits. See volume_02/make_parts.py for the same note.
"""
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE.parent / "chapters"
PARTS = [["v3ch01", "v3ch02", "v3ch03", "v3ch04"], ["v3ch05", "v3ch06", "v3ch07", "v3ch08"]]

for i, chs in enumerate(PARTS, 1):
    ps = [p for c in chs for p in sorted((CH / c / "raw").glob("p*.png"))]
    ims = [Image.open(p).convert("RGB") for p in ps]
    f = HERE / f"Volume_03_part{i}_of_{len(PARTS)}.pdf"
    ims[0].save(f, save_all=True, append_images=ims[1:], resolution=150.0)
    print(f"part {i}: {len(ps)} pages, {f.stat().st_size/1e6:.1f} MB -> {f.name}")
