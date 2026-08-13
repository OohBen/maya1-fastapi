"""Letter Chapter 9 and assemble its PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page
from PIL import Image
HERE=pathlib.Path(__file__).resolve().parent
RAW,FIN=HERE/"ch09"/"raw",HERE/"ch09"/"lettered"
DIALOGUE={
 "p08":["G-grandfather-",
        "No... no, don't die. I didn't mean to. I didn't know it was you."],
 "p09":["Come back. Come back!","Grandfather!"],
 "p13":["It was not your fault.","Madara wanted to die by your hands.",
        "Why would he want me to kill him?"],
 "p14":["He was going to die soon regardless. Either he died on his own and left you as you are - or he died by your hand and left you with the Mangekyou.",
        "He said it was the greatest power he could leave you.",
        "Your grandfather would be disappointed to see you like this. I should know. I am his will."],
 "p21":["Is that... Naruto?","He looks completely different."],
 "p22":["Dobe. What is with the change?","..."],
 "p23":["I didn't change.","I was always like this. You were just too blind to see it."],
}
FIN.mkdir(parents=True,exist_ok=True)
for p in sorted(RAW.glob("p*.png")):
    dest=FIN/p.name
    if p.stem in DIALOGUE:
        used,found=letter_page(p,DIALOGUE[p.stem],dest)
        print(f"[{p.stem}] found={found} filled={used}")
    else:
        Image.open(p).save(dest)
pages=sorted(FIN.glob("p*.png"))
ims=[Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch09"/"Chapter09.pdf",save_all=True,append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages")
