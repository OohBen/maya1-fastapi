"""Composite title + dialogue onto Chapter 6 pages, then assemble a reading PDF.

p01 doubles as the chapter title plate (its upper third was reserved for it).
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch06"/"raw", HERE/"ch06"/"lettered"

DIALOGUE = {
 "p02": ["Troublesome blonde.",
         "Do you have to wake me every time you find me sleeping?"],
 "p03": ["Hey.", "You want some?", "...You sure?"],
 "p04": ["We're getting barbecue after class. You can come if you want.",
         "...Yeah. Okay."],
 "p05": ["That girl keeps staring at me. Then she hides.",
         "She's never said one word to anyone. That's just pathetic."],
 "p06": ["Sasuke-kun! Over here!",
         "Move it, forehead. He's sitting with me."],
 "p07": ["That's Sasuke Uchiha. Top of the class.",
         "Every girl in the room. Troublesome.",
         "What's so great about that guy?"],
 "p08": ["The whole compound. Every one of them.",
         "It was his own son. Itachi.",
         "...In one night?"],
 "p12": ["They say he found them himself. His whole family.",
         "At least he had them for a while."],
 "p13": ["Grandfather. Do you know about the Uchiha massacre?",
         "Yes."],
 "p14": ["Those traitors got what they deserved.",
         "Every one of them."],
 "p15": ["Does that trouble you?",
         "Good."],
 "p16": ["They were killed because of their own ignorance.",
         "They were attempting a coup against the village."],
 "p17": ["Well? Say it.",
         "So Itachi killed his whole clan to stop a civil war?"],
 "p18": ["You catch on fast.",
         "The village is in lockdown. Nobody is counting children this week.",
         "...Who is that?"],
 "p19": ["This is Zetsu.",
         "My spy. My creation.",
         "I have been watching you since you were six."],
 "p20": ["The clone will take your place at the academy. It will not know that it is a clone.",
         "For the next year you will not go back to Konoha."],
}

FIN.mkdir(parents=True, exist_ok=True)

title_plate(RAW/"p01.png", FIN/"p01.png",
            title="TRAITORS",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER SIX")
print("[title] p01 composited")

for p in sorted(RAW.glob("p*.png")):
    if p.stem == "p01":
        continue
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        flag = "" if used == len(DIALOGUE[p.stem]) else "  <-- short"
        print(f"[{p.stem}] balloons found={found} filled={used}{flag}")
    else:
        Image.open(p).save(dest)
        print(f"[{p.stem}] silent")

pages = sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch06"/"Chapter06.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch06/Chapter06.pdf")
