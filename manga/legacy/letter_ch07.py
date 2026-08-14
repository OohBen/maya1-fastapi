"""Letter Chapter 7 and assemble its PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page
from PIL import Image
HERE=pathlib.Path(__file__).resolve().parent
RAW,FIN=HERE/"ch07"/"raw",HERE/"ch07"/"lettered"
DIALOGUE={
 "p01":["Do you remember the room I told you about? The one with the tablets.",
        "Only an Uchiha can read them."],
 "p05":["The Sage had two sons.","The elder inherited his eyes. The younger, his body.",
        "Everything since has been those two halves trying to kill each other."],
 "p07":["I want to infuse my cells, and Hashirama's, into you.",
        "Will I have his face in my chest too?"],
 "p18":["Stop crying.","Your grandfather did not build you to weep."],
 "p19":["Is this the price of power?","..."],
 "p20":["Is this the price of power?"],
}
FIN.mkdir(parents=True,exist_ok=True)
for p in sorted(RAW.glob("p*.png")):
    dest=FIN/p.name
    if p.stem in DIALOGUE:
        used,found=letter_page(p,DIALOGUE[p.stem],dest); print(f"[{p.stem}] found={found} filled={used}")
    else:
        Image.open(p).save(dest)
pages=sorted(FIN.glob("p*.png"))
ims=[Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch07"/"Chapter07.pdf",save_all=True,append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages")
