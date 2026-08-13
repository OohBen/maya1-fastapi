"""Assemble Volume 2: combined PDF, contact sheet, and a README with the real numbers."""
import json
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE / "chapters"
OUT = HERE / "volume_02"

CHAPTERS = [
    ("v2ch01", "Shall We Dance?", "Naruto hands back both bells"),
    ("v2ch02", "Entitled to My Secrets", 'Zetsu: "Your sensei."'),
    ("v2ch03", "Six Months", "Gaara asks his name"),
    ("v2ch04", "The War Hawk", "Danzo's standing offer"),
    ("v2ch05", "Room 301", '"The rest are weak. They are annoyances."'),
    ("v2ch06", "The Tenth Question", 'Ibiki: "There is no tenth question."'),
    ("v2ch07", "The Forest of Death", "The first thing he has ever wanted"),
]


def pages(cid):
    d = CH / cid / "raw"
    return sorted(d.glob("p*.png")) if d.exists() else []


def cost(cid):
    f = CH / cid / "ledger.json"
    return sum(r.get("cost", 0) or 0 for r in json.load(f.open())) if f.exists() else 0.0


def main():
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
    pdf = OUT / "Volume_02.pdf"
    ims[0].save(pdf, save_all=True, append_images=ims[1:], resolution=150.0)

    cols, tw = 10, 200
    th = int(tw * ims[0].height / ims[0].width)
    nrows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * th), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
    sheet.save(OUT / "volume_02_contact_sheet.jpg", quality=85)

    md = ["# Volume 2 — *Entitled to My Secrets*", "",
          f"**{len(all_pages)} pages across {len(rows)} chapters. ${total:.2f} of generation.**", "",
          "Covers the end of fic ch3 through fic ch4. Konoha decides Naruto is a threat and is "
          "right for the wrong reasons; every chapter costs him another kind of privacy, and the "
          "volume ends with him walking into a forest designed to kill him and enjoying it.", "",
          "| Ch | Title | Pages | Cost | Ends on |", "|---|---|---|---|---|"]
    for cid, title, n, c, ends in rows:
        md.append(f"| {cid[-2:]} | {title} | {n} | ${c:.2f} | {ends} |")
    md += ["", f"| | **Total** | **{len(all_pages)}** | **${total:.2f}** | |", "",
           "## What changed from Volume 1", "",
           "- **Dialogue and SFX are drawn by the model**, given verbatim per panel. Every balloon "
           "names its speaker and its position, and `OFF()` marks a speaker who is not drawn in "
           "that panel so the tail runs off-panel instead of out of the wrong character's mouth.",
           "- **`ONLY()` states the complete cast per page**, and every name in it is bound to a "
           "reference image. Unbound names get substituted by whatever else is bound.",
           "- **Splash pages use `SPLASH`, never `STAGING`** — STAGING says \"panels\" nine times "
           "and always won the argument, so chapter openers came back as six-panel grids.",
           "- **Refusals change something instead of repeating.** `rep_generate` raises `Moderated` "
           "immediately on a content block; `build_page` walks to the next style reference, then a "
           "softened prompt, then no style reference.",
           "- **Pacing is ours, not the prose's.** The fic disposes of the Wave mission in two "
           "paragraphs; here it is ten staged pages that still end on his blank face.", ""]
    (OUT / "README.md").write_text("\n".join(md))
    print(f"{len(all_pages)} pages, ${total:.2f} -> {pdf}")


if __name__ == "__main__":
    main()
