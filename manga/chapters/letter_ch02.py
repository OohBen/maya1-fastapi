"""Composite title + dialogue onto Chapter 2 pages, then assemble a reading PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch02"/"raw", HERE/"ch02"/"lettered"

# Lines are assigned to balloons in reading order (top-to-bottom band, then left-to-right),
# so each list below is ordered to land on the balloon whose tail points at the speaker.
DIALOGUE = {
 "p02": ["Another Tenth of October. The whole village will be drinking tonight.",
         "Some of them will do more than drink.",
         "You mean the Uzumaki boy.",
         "Keep your voice down. The Sandaime made it law."],
 "p03": ["They still talk like the boy is the fox.",
         "The Kyuubi is sealed inside him. He's the cage. Not the beast."],
 "p08": ["Open up, demon.",
         "We know you're in there.",
         "Come on, then. Outside."],
 "p10": ["Nowhere left to run, brat.",
         "Not so many of us tonight.",
         "Doesn't take many."],
 "p14": ["Your savior.",
         "...Savior?"],
 "p15": ["Why did you save me? No one in this village does that for me.",
         "I could not stand and watch foolish men beat a child."],
 "p17": ["Don't tell your Hokage anything about me.",
         "If he asks, you didn't see who saved you.",
         "...Okay. I won't."],
 "p18": ["Then at least tell me your name.",
         "My name is... Madara.",
         "Madara. I won't forget."],
 "p19": ["Did you tell him?",
         "No. Not yet. I need to gain his trust first."],
}

FIN.mkdir(parents=True, exist_ok=True)
title_plate(RAW/"00_title.png", FIN/"00_title.png",
            title="THE OLD MAN\nIN BLACK",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER TWO")
print("[title] composited")

for p in sorted(RAW.glob("p*.png")):
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        flag = "" if found >= len(DIALOGUE[p.stem]) else "   <-- too few balloons"
        print(f"[{p.stem}] balloons found={found} filled={used}{flag}")
    else:
        Image.open(p).save(dest)

pages = [FIN/"00_title.png"] + sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch02"/"Chapter02.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch02/Chapter02.pdf")
