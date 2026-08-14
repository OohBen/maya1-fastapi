"""Composite title + dialogue onto Chapter 3 pages, then assemble a reading PDF.

p01 is both the chapter's title plate and its opening splash, so it gets title_plate()
and is skipped by the dialogue loop.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch03"/"raw", HERE/"ch03"/"lettered"

DIALOGUE = {
 "p02": ["You will start at the Academy on Monday, Naruto-kun.",
         "M-Monday?! For real, jiji?!"],
 "p03": ["I'm gonna be the best one in the whole class!",
         "Is that so.",
         "And then I'm gonna be Hokage! Just you watch, jiji!"],
 "p04": ["Now, Naruto - tell me. What is a shinobi?",
         "Someone who can do all the cool jutsu!"],
 "p05": ["No. A shinobi is someone who fights to protect the people precious to them.",
         "The kind of shinobi you become is decided by the heart you have - not the jutsu.",
         "...I don't get it, jiji."],
 "p06": ["Thanks, jiji! You'll see - I'm gonna be the best one there!",
         "...I believe that you will.",
         "I only hope this village lets you."],
 "p08": ["You see that boy?",
         "Don't talk to him. Don't play with him."],
 "p10": ["...and chakra is physical energy and spiritual energy, mixed. Copy it down.",
         "Every one of you is here to become a shinobi of this village. Act like it."],
 "p11": ["Sensei! Sensei! When do we get to learn the cool jutsu?!",
         "Uzumaki. Sit. Down."],
 "p12": ["Get out of my class.",
         "Come back when you've decided to take my teaching seriously."],
 "p14": ["Hey. You're on our swing.",
         "My dad says we're not even supposed to talk to you.",
         "So don't.",
         "What, you gonna cry about it?"],
 "p15": ["Next time, bring a better lunch.",
         "Ha! See you tomorrow, freak.",
         "...",
         "...Still good."],
 "p17": ["...Who's there?",
         "I brought you food. I saw you were running low.",
         "Saw...? How would you know that?"],
 "p18": ["I let myself in last week, to see what you had in your cupboards.",
         "You broke into my apartment!",
         "I didn't come to steal. I came to help."],
 "p19": ["It's good! It's really good!",
         "Next week I'll bring you books."],
}

FIN.mkdir(parents=True, exist_ok=True)
title_plate(RAW/"p01.png", FIN/"p01.png",
            title="ACADEMY",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER THREE")
print("[title] composited onto p01")

for p in sorted(RAW.glob("p*.png")):
    if p.stem == "p01":
        continue
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        print(f"[{p.stem}] balloons found={found} filled={used}")
    else:
        Image.open(p).save(dest)

pages = sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch03"/"Chapter03.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch03/Chapter03.pdf")
