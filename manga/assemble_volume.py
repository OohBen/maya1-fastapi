"""Assemble Volume 1: combined PDF, contact sheet, and a README with real numbers."""
import glob
import json
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
CH = HERE / "chapters"
OUT = HERE / "volume_01"

TITLES = {
    "ch01": "The Tenth of October", "ch02": "The Old Man in Black", "ch03": "Academy",
    "ch04": "Kushina", "ch05": "Grandfather", "ch06": "Traitors",
    "ch07": "The Price", "ch08": "Inheritance", "ch09": "The Greatest Sin",
}
ENDS = {
    "ch01": "He stops asking adults for the truth",
    "ch02": '"My name is... Madara."',
    "ch03": "The first genuine smile",
    "ch04": '"Her name was Kushina Uzumaki."',
    "ch05": "Madara's grin - the one that promises pain",
    "ch06": '"For the next year you will not go back to Konoha."',
    "ch07": '"Is this the price of power?"',
    "ch08": '"Never forget what I taught you."',
    "ch09": '"You were just too blind to see it."',
}


def chapter_pages(cid):
    d = CH / cid / "lettered"
    if not d.exists():
        d = CH / cid / "raw"
    if not d.exists():
        return []
    title = sorted(d.glob("00_*.png"))
    return title + sorted(d.glob("p*.png"))


def cost(cid):
    f = CH / cid / "ledger.json"
    if not f.exists():
        return 0.0
    return sum(r.get("cost", 0) or 0 for r in json.load(f.open()))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    found, all_pages, rows, total = [], [], [], 0.0
    for cid in sorted(TITLES):
        pages = chapter_pages(cid)
        if not pages:
            continue
        found.append(cid)
        all_pages += pages
        c = cost(cid)
        total += c
        rows.append((cid, TITLES[cid], len(pages), c, ENDS[cid]))

    if not all_pages:
        print("no pages found"); return

    # combined PDF
    ims = [Image.open(p).convert("RGB") for p in all_pages]
    pdf = OUT / "Volume01.pdf"
    ims[0].save(pdf, save_all=True, append_images=ims[1:])

    # contact sheet
    cols, tw = 10, 240
    th = int(tw * ims[0].height / ims[0].width)
    rws = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * 6, rws * th + (rws + 1) * 6), (22, 22, 26))
    for i, im in enumerate(ims):
        r, c2 = divmod(i, cols)
        sheet.paste(im.resize((tw, th)), (6 + c2 * (tw + 6), 6 + r * (th + 6)))
    sheet.save(OUT / "volume_01_contact_sheet.jpg", quality=86)

    refs_cost = sum(r.get("cost", 0) or 0
                    for r in json.load((HERE / "refs" / "ledger.json").open()))

    lines = [
        "# Volume 1 — *The Price of Power*", "",
        "*Uchiha Naruto: The Sage* — manga adaptation of the fanfic by The Omnipresent Sage.",
        "Adapts fic chapters 1–3: the Madara origin arc, from the beating on Naruto's sixth",
        "birthday to the Mangekyo and the academy reveal.", "",
        f"**{len(found)} chapters · {len(all_pages)} pages · full colour · lettered**", "",
        "| Ch | Title | Pages | Cost | Ends on |", "|---|---|---|---|---|",
    ]
    for cid, t, n, c, e in rows:
        lines.append(f"| {cid[-2:]} | {t} | {n} | ${c:.2f} | {e} |")
    lines += [
        f"| | **Total** | **{len(all_pages)}** | **${total:.2f}** | |", "",
        "## The arc", "",
        "Each chapter costs the protagonist something. That is the spine:", "",
        "1. **The Tenth of October** — his belief that adults will tell him the truth",
        "2. **The Old Man in Black** — his solitude; he now has a secret",
        "3. **Academy** — nothing. The only free chapter, placed deliberately before the break",
        "4. **Kushina** — the comfortable blank where his parents used to be",
        "5. **Grandfather** — his childhood",
        "6. **Traitors** — a year of his life, and his moral floor",
        "7. **The Price** — his innocence. Twenty-five men, arranged for him",
        "8. **Inheritance** — his name",
        "9. **The Greatest Sin** — his grandfather, by his own hand", "",
        "## Production", "",
        f"- Art: `openai/gpt-image-2` on Replicate. Reference pack of 41 images (${refs_cost:.2f}).",
        "- Default tier `low`; `medium` for emotional beats; `high` for splashes and the pack.",
        "- Dialogue composited deterministically after generation; SFX drawn by the model.",
        "- Chapter 7 uses a deliberate register shift — the Sage myth renders as antique",
        "  scroll painting rather than manga, which is what makes four pages of source",
        "  exposition readable.", "",
        "## Next", "",
        "Volume 2 opens on the bell test (fic ch3 end → ch4). **There is no Wave arc** — the",
        "fic skips it entirely and goes to the Chunin Exams. See `story/00_SERIES_BIBLE.md`",
        "for the full 50-chapter map and `PIPELINE.md` for how to build it.",
    ]
    (OUT / "README.md").write_text("\n".join(lines))
    print(f"chapters: {', '.join(found)}")
    print(f"pages   : {len(all_pages)}")
    print(f"art cost: ${total:.2f} (+ ${refs_cost:.2f} refs)")
    print(f"-> {pdf}")


if __name__ == "__main__":
    main()
