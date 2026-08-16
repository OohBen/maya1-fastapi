"""Assemble Volume 4: combined PDF, contact sheet, and a README with the real numbers."""
import json
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE / "chapters"
OUT = HERE / "volume_04"

CHAPTERS = [
    ("v4ch01", "The Professor", "Kabuto leaves with Naruto's preserved blood sample"),
    ("v4ch02", "Not Cut Out for It", "Kurama remains distrustful behind the seal"),
    ("v4ch03", "Brothers", "Naruto chooses solitary training"),
    ("v4ch04", "Two Weeks", "The Eternal Mangekyo opens"),
    ("v4ch05", "Orange", "Orochimaru escapes the completed orange Susano'o"),
    ("v4ch06", "The Debt", "Naruto and Yugao approach Kiri through the fog"),
    ("v4ch07", "Kiri", "Mei accepts Naruto's bounded help"),
    ("v4ch08", "The Tower", "Kurama's controlled strike destroys the tower"),
    ("v4ch09", "What Are You?", "Both armies confront the Susano'o crater"),
    ("v4ch10", "The Mizukage", "Human Yagura disappears inside Naruto's fireball"),
    ("v4ch11", "The Three Tails", "An unexplained blue chakra column rises"),
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
    pdf = OUT / "Volume_04.pdf"
    ims[0].save(pdf, save_all=True, append_images=ims[1:], resolution=150.0)

    cols, tw = 10, 200
    th = int(tw * ims[0].height / ims[0].width)
    nrows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, nrows * th), "white")
    for i, im in enumerate(ims):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
    sheet.save(OUT / "volume_04_contact_sheet.jpg", quality=85)

    md = ["# Volume 4 — *What Are You?*", "",
          f"**{len(all_pages)} pages across {len(rows)} chapters. ${total:.2f} of generation.**", "",
          "Covers fic ch8-11, from the invasion aftermath through the unresolved blue chakra "
          "column in Kiri. Hiruzen's death removes Naruto's political buffer; each chapter then "
          "shows what he takes, reveals, or spends once that restraint is gone.", "",
          "| Ch | Title | Pages | Cost | Ends on |", "|---|---|---|---|---|"]
    for cid, title, n, c, ends in rows:
        md.append(f"| {cid[-2:]} | {title} | {n} | ${c:.2f} | {ends} |")
    md += ["", f"| | **Total** | **{len(all_pages)}** | **${total:.2f}** | |", "",
           "## Notes", "",
           "- Naruto refuses Jiraiya and leaves alone; the permission meeting is with his clone.",
           "- Mei is the rebel leader while Yagura remains the Fourth Mizukage.",
           "- The post-skip sash sword is new, not the ninjato lost in Volume 3.",
           "- The final blue chakra column is deliberately left unnamed and unexplained.", ""]
    (OUT / "README.md").write_text("\n".join(md))
    print(f"{len(all_pages)} pages, ${total:.2f} -> {pdf}")


if __name__ == "__main__":
    main()
