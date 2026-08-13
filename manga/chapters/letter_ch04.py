"""Composite title + dialogue onto Chapter 4 pages, then assemble a reading PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch04"/"raw", HERE/"ch04"/"lettered"

DIALOGUE = {
 "p07": ["Naruto! I haven't seen you in three months - where have you been?",
         "Don't you ever do that to me again. I was worried sick."],
 "p08": ["Three whole months! Then the first six bowls are on the house, kid.",
         "Then make it twenty-six bowls of miso pork. And keep 'em coming!",
         "Twenty... six?"],
 "p09": ["Bowl nineteen! Ayame, get the big pot!",
         "Where does he even put it all?"],
 # balloon order/position per page is checked against find_balloons() geometry,
 # so every line sits with the character who is actually speaking it.
 "p10": ["Aw, quit it! I'm not a baby!",
         "Ha! Let the boy eat like a boy, Ayame.",
         "...Thanks, old man. For real."],
 "p11": ["That's him. That's the one.",
         "Get inside. Don't look at it."],
 "p12": ["I have questions that need answering. Who are you?",
         "Hm. I wondered when you would ask."],
 "p13": ["In one of the history books I gave you there was a man called Uchiha Madara.",
         "The one who fought the Shodaime Hokage. The one who lost.",
         "I am that man."],
 "p14": ["...Huh.",
         "That can't be true. Madara died fighting the Shodaime - it's in the book you gave me.",
         "So the book says."],
 "p15": ["You read them properly, then. Good.",
         "Since you won't believe that - how about I tell you about your parents instead."],
 "p16": ["...You knew them?",
         "Tell me. Tell me everything, right now!",
         "Sit down, Naruto."],
 "p17": ["Okay.",
         "Sit. And listen carefully - I will say this only once.",
         "Your mother was the jinchuuriki of the Kyuubi. Before it was sealed inside you."],
 "p18": ["She had it. Inside her. Before me.",
         "She did. Every day of her life."],
 "p19": ["Her name was Kushina Uzumaki.",
         "Kushina."],
}

FIN.mkdir(parents=True, exist_ok=True)
title_plate(RAW/"00_title.png", FIN/"00_title.png",
            title="KUSHINA",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER FOUR")
print("[title] composited")

for p in sorted(RAW.glob("p*.png")):
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        flag = "" if used == found else f"   <-- found {found}, filled {used}"
        print(f"[{p.stem}] balloons found={found} filled={used}{flag}")
    else:
        Image.open(p).save(dest)
        print(f"[{p.stem}] silent")

pages = [FIN/"00_title.png"] + sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch04"/"Chapter04.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch04/Chapter04.pdf")
