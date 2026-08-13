"""Pack one chapter's raw pages into a reading PDF plus a contact sheet.

    python3 pack_chapter.py v2ch02 "Entitled to My Secrets"

Volume 2 pages are model-lettered, so there is no lettering pass — raw/ IS the finished art.
"""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent


def pack(cid, title):
    d = HERE / "chapters" / cid
    src = d / "lettered" if (d / "lettered").exists() else d / "raw"
    pages = sorted(src.glob("p*.png"))
    if not pages:
        raise SystemExit(f"no pages in {src}")

    ims = [Image.open(p).convert("RGB") for p in pages]
    vol = cid[1] if cid.startswith("v") else "1"
    name = f"V{vol}_Chapter{cid[-2:]}.pdf"
    ims[0].save(d / name, save_all=True, append_images=ims[1:], resolution=150.0)

    cols = 5
    tw = 300
    th = int(tw * ims[0].height / ims[0].width)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
    sheet.save(d / f"{cid}_contact_sheet.jpg", quality=88)

    print(f"{cid} — {title}: {len(pages)} pages -> {d/name}")


if __name__ == "__main__":
    pack(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
