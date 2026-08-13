"""Assemble Volume 3: combined PDF, contact sheet, and a README with the real numbers."""
import json
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE / "chapters"
OUT = HERE / "volume_03"

CHAPTERS = [
    ("v3ch01", "Amaterasu", '"Stay down, Naruto-kun."'),
    ("v3ch02", "A Gift", "Naruto looking at his own hands"),
    ("v3ch03", "The Tower", "The first time we see him sleep"),
    ("v3ch04", "The Preliminaries", "Two Hyuga on the board"),
    ("v3ch05", "Fate", 'Hinata: "It isn\'t myself I\'m trying to change."'),
    ("v3ch06", "The Toad Sage", "He refuses Jiraiya and disappears"),
    ("v3ch07", "The Silent Crowd", "The first time his grandfather shows"),
    ("v3ch08", "Susano'o", "The purple barrier over the academy"),
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
    pdf = OUT / "Volume_03.pdf"
    ims[0].save(pdf, save_all=True, append_images=ims[1:], resolution=150.0)

    cols, tw = 10, 200
    th = int(tw * ims[0].height / ims[0].width)
    nrows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * th), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
    sheet.save(OUT / "volume_03_contact_sheet.jpg", quality=85)

    md = ["# Volume 3 — *The Difference Between Us*", "",
          f"**{len(all_pages)} pages across {len(rows)} chapters. ${total:.2f} of generation.**", "",
          "Covers fic ch5-7, the Orochimaru ambush through the opening of the invasion. Naruto "
          "meets someone he cannot beat on page one, and every chapter after it costs him another "
          "story he told about himself.", "",
          "| Ch | Title | Pages | Cost | Ends on |", "|---|---|---|---|---|"]
    for cid, title, n, c, ends in rows:
        md.append(f"| {cid[-2:]} | {title} | {n} | ${c:.2f} | {ends} |")
    md += ["", f"| | **Total** | **{len(all_pages)}** | **${total:.2f}** | |", "",
           "## Notes", "",
           "- The Chapter 1 fight is staged so its twist reconstructs on a reread: the Naruto "
           "being thrown around for the first half is a shadow clone.",
           "- He loses the ninjato to Orochimaru and does not have it again — from Chapter 3 he "
           "is bound without it, and Chapter 2 spends a panel on him reaching for it.",
           "- Chapter 5 gives Naruto four panels and no dialogue. Neji vs Hinata is the only "
           "thing in three volumes that visibly reaches him.",
           "- The volume stops the instant he sees the barrier go up over the academy. The fic "
           "reports the invasion's outcome retroactively in ch8, so that is Volume 4's opening.", ""]
    (OUT / "README.md").write_text("\n".join(md))
    print(f"{len(all_pages)} pages, ${total:.2f} -> {pdf}")


if __name__ == "__main__":
    main()
