"""Assemble Volume 5: combined PDF, contact sheet, and a README with the real numbers."""
import argparse
import json
import pathlib

from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE / "chapters"
OUT = HERE / "volume_05"
TITLE = "Volume 5 - What We Build"
MASTER_PDF = "Volume_05.pdf"
COMPRESSED_PDF = "Volume_05_compressed.pdf"
COMPRESSED_JPEG_QUALITY = 50
# Volume 5 mixes 1152x2048 and 2160x3840 pages. The reading PDF normalises every page down to
# the smaller height so the tall pages stop tripling the file size for no visible gain.
COMPRESSED_MAX_HEIGHT = 2048
# GitHub refuses any file over 100MB, so the master ships as parts.
PART_MAX_BYTES = 90 * 1024 * 1024

CHAPTERS = [
    ("v5ch01", "After the Blue", "Zetsu reveals Jiraiya is bringing Sasuke home"),
    ("v5ch02", "Peace", "Mei asks why he will not use his power for peace"),
    ("v5ch03", "The Other Uchiha", "Naruto and Sasuke agree to rebuild the clan"),
    ("v5ch04", "The Open Cage", "Kurama is freed without being controlled"),
    ("v5ch05", "Goodbye, Mizukage", "He leaves Kiri and enters the recurring dream"),
    ("v5ch06", "Mother", "Kushina asks him to live as himself"),
    ("v5ch07", "The Snake's Last Skin", "Orochimaru dies; Naruto takes the mask"),
    ("v5ch08", "A New Sound", "Guren accepts a new life rebuilding Oto"),
    ("v5ch09", "Home", "Karin enters Konoha; Tsunade summons him"),
    ("v5ch10", "Permission", "He warns Jiraiya away from Ame"),
    ("v5ch11", "Family", "Clan, Karin and Police plans form"),
    ("v5ch12", "Head of the Uchiha", "He claims the council seat"),
    ("v5ch13", "The Police Force", "The Uchiha stand up again"),
]


def pages(cid):
    d = CH / cid / "raw"
    return sorted(d.glob("p*.png")) if d.exists() else []


def cost(cid):
    f = CH / cid / "ledger.json"
    return sum(r.get("cost", 0) or 0 for r in json.load(f.open())) if f.exists() else 0.0


def add_navigation(pdf, rows):
    """Add metadata and nested chapter bookmarks without re-encoding page images."""
    reader = PdfReader(pdf)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.add_metadata({
        "/Title": TITLE,
        "/Subject": "Full-colour manga adaptation, Volume 5",
    })
    volume = writer.add_outline_item(TITLE, 0)
    start = 0
    for cid, title, count, _chapter_cost, _ends in rows:
        number = int(cid[-2:])
        label = f"Prologue: {title}" if number == 0 else f"Chapter {number}: {title}"
        writer.add_outline_item(
            label, start, parent=volume
        )
        start += count
    writer.root_object[NameObject("/PageMode")] = NameObject("/UseOutlines")
    writer.root_object[NameObject("/PageLayout")] = NameObject("/TwoPageRight")
    prefs = DictionaryObject()
    prefs[NameObject("/Direction")] = NameObject("/R2L")
    writer.root_object[NameObject("/ViewerPreferences")] = prefs

    temp = pdf.with_name(f".{pdf.name}.tmp")
    with temp.open("wb") as stream:
        writer.write(stream)
    temp.replace(pdf)


def downscale(images, max_height):
    out = []
    for im in images:
        if im.height > max_height:
            w = round(im.width * max_height / im.height)
            im = im.resize((w, max_height), Image.LANCZOS)
        out.append(im)
    return out


def split_master(pdf, out_dir, stem):
    """Split the master into parts that each fit under GitHub's file-size ceiling."""
    for stale in out_dir.glob(f"{stem}_part*_of_*.pdf"):
        stale.unlink()
    reader = PdfReader(pdf)
    n = len(reader.pages)
    parts = max(1, -(-pdf.stat().st_size // PART_MAX_BYTES))
    while True:
        per = -(-n // parts)
        paths, ok = [], True
        for i in range(parts):
            chunk = reader.pages[i * per:(i + 1) * per]
            if not chunk:
                continue
            w = PdfWriter()
            for page in chunk:
                w.add_page(page)
            dest = out_dir / f"{stem}_part{i + 1}_of_{parts}.pdf"
            with dest.open("wb") as fh:
                w.write(fh)
            paths.append(dest)
            if dest.stat().st_size > PART_MAX_BYTES:
                ok = False
        if ok:
            return paths
        for dest in paths:
            dest.unlink()
        parts += 1


def save_compressed_pdf(images, pdf, rows):
    images = downscale(images, COMPRESSED_MAX_HEIGHT)
    images[0].save(
        pdf,
        save_all=True,
        append_images=images[1:],
        resolution=150.0,
        quality=COMPRESSED_JPEG_QUALITY,
        optimize=True,
        subsampling=2,
    )
    add_navigation(pdf, rows)


def save_master_pdf(images, pdf, rows):
    temporary = pdf.with_name(f".{pdf.stem}.rebuild.pdf")
    images[0].save(
        temporary,
        save_all=True,
        append_images=images[1:],
        resolution=150.0,
    )
    add_navigation(temporary, rows)
    temporary.replace(pdf)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rebuild-master",
        action="store_true",
        help="rebuild the full-quality master from chapter PNGs before adding navigation",
    )
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    all_pages, rows, total = [], [], 0.0
    for cid, title, ends in CHAPTERS:
        ps = pages(cid)
        if not ps:
            continue
        all_pages += ps
        c = cost(cid)
        total += c
        rows.append((cid, title, len(ps), c, ends))

    ims = [Image.open(p).convert("RGB") for p in all_pages]
    pdf = OUT / MASTER_PDF
    if args.rebuild_master or not pdf.exists():
        save_master_pdf(ims, pdf, rows)
    else:
        add_navigation(pdf, rows)

    compressed_pdf = OUT / COMPRESSED_PDF
    save_compressed_pdf(ims, compressed_pdf, rows)
    parts = split_master(pdf, OUT, pdf.stem)

    cols, tw = 10, 200
    th = int(tw * ims[0].height / ims[0].width)
    nrows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * th), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
    sheet.save(OUT / "volume_05_contact_sheet.jpg", quality=85)

    md = ["# Volume 5 — *What We Build*", "",
          f"**{len(all_pages)} pages across {len(rows)} chapters. ${total:.2f} of generation.**", "",
          "`Volume_05.pdf` is the full-quality master. `Volume_05_compressed.pdf` keeps "
          "the same pages normalised to a single height with light JPEG compression for "
          "smoother reading. `Volume_05_part*.pdf` are the master split to fit GitHub's "
          "100MB per-file limit; concatenate them to recover the master. "
          "Both PDFs include a nested chapter outline/bookmarks panel.", "",
          "## Reading direction", "",
          "**This is a right-to-left manga.** Panel 1 is the TOP-RIGHT panel of a page; panels "
          "run right to left across a row before dropping to the next row, and balloons inside a "
          "panel read the same way. Both PDFs declare right-to-left binding "
          "(`/Direction /R2L`) and open in two-page spreads with page 1 on the right, so a "
          "viewer that honours those flags will pair and order the spreads correctly. If your "
          "reader ignores them and shows page 1 on the LEFT of a spread, your eye will land on "
          "the wrong page first — switch the reader to right-to-left or single-page mode.", "",
          "Covers fic chapters 12-16. Volume 4 ended with Yagura down and an unexplained blue "
          "chakra column over Kiri; this volume opens in that aftermath and asks what Naruto "
          "builds with the reputation winning there bought him. Each chapter turns destructive "
          "power into something that can last - freedom for Kurama, a working bond with Sasuke, "
          "protection for Karin, a successor state in Oto, a restored clan seat, and a new "
          "Police Force - while every constructive act also pushes his private power further "
          "beyond anyone's oversight.", "",
          "| Ch | Title | Pages | Cost | Ends on |", "|---|---|---|---|---|"]
    for cid, title, n, c, ends in rows:
        md.append(f"| {cid[-2:]} | {title} | {n} | ${c:.2f} | {ends} |")
    md += ["", f"| | **Total** | **{len(all_pages)}** | **${total:.2f}** | |", "",
           "## Notes", "",
           "- Kurama is released rather than controlled; the seal is opened by choice, not broken.",
           "- Kushina appears in the recurring dream and asks him to live as himself, not to complete objectives.",
           "- Orochimaru dies here and Naruto takes his mask; Guren inherits the rebuilding of Oto.",
           "- Karin enters Konoha under Naruto's protection, as promised in Volume 3.",
           "- Naruto claims the Uchiha council seat and stands the Police Force back up.",
           "- He warns Jiraiya away from Ame - a refusal that is left to pay off later.", ""]
    (OUT / "README.md").write_text("\n".join(md))
    print(f"{len(all_pages)} pages, ${total:.2f} -> {pdf}, {compressed_pdf}")
    for part in parts:
        print(f"  part: {part.name}  {part.stat().st_size / 1024 / 1024:.0f}MB")


if __name__ == "__main__":
    main()
