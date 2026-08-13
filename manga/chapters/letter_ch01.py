"""Composite title + dialogue onto Chapter 1 pages, then assemble a reading PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch01"/"raw", HERE/"ch01"/"lettered"

DIALOGUE = {
 "p08": ["Oho. The little demon finally stopped running.",
         "What do you have to say for yourself?"],
 "p09": ["Today we're going to judge you for your crimes, demon!",
         "You will answer me when I'm talking to you!"],
 "p14": ["You're stubborn today, eh...", "Kyuubi?"],
 "p15": ["Hey! You know we aren't supposed to say that. The Sandaime forbid it.",
         "Ah, that old fool can't do anything.",
         "Let's just get our revenge and get back to the party."],
 "p20": ["Hokage-sama. Why don't you ask Jiraiya-sama to come back and take Naruto out of the village?",
         "I have already tried. He told me he can't raise a boy while running a spy network.",
         "He's his godson."],
 "p21": ["Then let me take care of him. I owe that much to his father.",
         "No. You are one of the strongest shinobi in this village. We cannot lose you.",
         "Then what are we going to do?"],
 "p23": ["It's good that you're awake, Naruto-kun.",
         "Jiji... what did I do to make them hate me?",
         "Naruto-kun. People will always hate what they don't understand."],
 "p24": ["Why don't I have parents, Jiji?",
         "We've been through this. Come - let me take you back."],
}

FIN.mkdir(parents=True, exist_ok=True)
title_plate(RAW/"00_title.png", FIN/"00_title.png",
            title="THE TENTH\nOF OCTOBER",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER ONE")
print("[title] composited")

for p in sorted(RAW.glob("p*.png")):
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        print(f"[{p.stem}] balloons found={found} filled={used}")
    else:
        Image.open(p).save(dest)

pages = [FIN/"00_title.png"] + sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch01"/"Chapter01.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch01/Chapter01.pdf")
