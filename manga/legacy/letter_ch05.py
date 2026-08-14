"""Letter Chapter 5 and assemble its PDF.

Lines are ordered to match the balloons the letterer actually finds on each page
(top-to-bottom by band, then left-to-right), so speaker attribution lands correctly.
The second half of the chapter is nearly silent by design: p13-p15, p18 and p20 carry
no dialogue at all.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch05"/"raw", HERE/"ch05"/"lettered"

DIALOGUE = {
 # ---- the name -------------------------------------------------------
 "p01": ["Your father was Minato Namikaze. The Yondaime Hokage.",
         "...The Yondaime?",
         "That fool and your mother died sealing the Kyuubi inside you."],
 "p02": ["The man they carved into the mountain. Their hero.",
         "He chose you for it himself."],
 # ---- the rage -------------------------------------------------------
 "p03": ["He put it in me.",
         "His own kid?! He's the reason all of them hate me!",
         "Minato was a fool to think this village would ever accept you as a hero."],
 "p05": ["Haa... haa...",
         "That was not your chakra, boy.",
         "What's... happening to me...?"],
 # ---- the resemblance ------------------------------------------------
 "p06": ["Don't touch me.",
         "You look a lot like him. Have you noticed?"],
 "p07": ["Get it off. Get it off me.",
         "You can't. It is the only thing he left you."],
 # ---- the monument ---------------------------------------------------
 "p09": ["Some hero.",
         "You never even asked me."],
 # ---- your grandfather -----------------------------------------------
 "p10": ["There is one more thing, boy.",
         "I know all of this because I was Kushina's father. Which makes me your grandfather.",
         "...Grand... father?"],
 "p11": ["If you're truly my grandfather - where were you?",
         "Dying. In a hole in the ground, too far away to reach you."],
 # ---- he cries -------------------------------------------------------
 "p12": ["I said I'd never do this again.",
         "I promised."],
 # ---- the machine starts ---------------------------------------------
 "p16": ["Listen, boy. I don't have much time.",
         "Your childhood is over."],
 "p17": ["Hello, little one. I am to look after you.",
         "Arms and legs. They stay on until he says otherwise.",
         "I can't- I can't even stand up."],
 "p19": ["It only hurts this much because it's the first day.",
         "He cannot hear you. He has been asleep since the fortieth lap."],
}

FIN.mkdir(parents=True, exist_ok=True)
for p in sorted(RAW.glob("p*.png")):
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        flag = "" if used == len(DIALOGUE[p.stem]) else "   <-- short"
        print(f"[{p.stem}] balloons found={found} filled={used}{flag}")
    else:
        Image.open(p).save(dest)
        print(f"[{p.stem}] silent")

pages = sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch05"/"Chapter05.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch05/Chapter05.pdf")
