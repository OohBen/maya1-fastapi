"""Letter Chapter 8 and assemble its PDF."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from letterer import letter_page, title_plate
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
RAW, FIN = HERE/"ch08"/"raw", HERE/"ch08"/"lettered"

DIALOGUE = {
 "p03": ["Ooh - he's dispelled the clone again. That does look like it hurts.",
         "A year of another boy's life, arriving all at once. It will pass. It always passes."],
 "p04": ["You said you would tell me all of it. Tonight.",
         "Sit. This wall is older than the village is."],
 "p05": ["I found a young Uchiha boy during the war.",
         "Half-crushed under a landslide. Half-dead. His own team had already written him off.",
         "I rebuilt him. I gave him my plan, my purpose, and my name to use. His name was Obito."],
 "p06": ["He built an organisation out of what I gave him. He calls it Akatsuki.",
         "The Rinnegan I once carried sits in another man's skull now. Nagato. A boy out of Ame.",
         "Ten of the strongest shinobi alive.",
         "And every one of them believes they are following me."],
 "p07": ["He betrayed me. He uses my name to gather the strongest shinobi in the world.",
         "Every crime that fool commits, the world files under mine.",
         "Then he is a thief."],
 "p08": ["You are the last of my blood, Naruto.",
         "What is it you want me to do?",
         "Take back everything that belongs to me. Restore the Uchiha."],
 "p09": ["Take Konoha from the fools who rule it - and if they will not make you Hokage, "
         "take it by force.",
         "And the man wearing your name?",
         "Kill the fool. Do what you like with the Rinnegan."],
 "p11": ["Uchiha.",
         "Uchiha Naruto."],
 "p16": ["Come closer. There is one thing left.",
         "You didn't come down to the cavern this morning."],
 "p17": ["Take this. It is my gift to you."],
 "p18": ["It's heavier than it looks.",
         "I am proud of you."],
 "p19": ["Never forget what I taught you.",
         "You say that every time.",
         "Keep my words in your heart."],
}

FIN.mkdir(parents=True, exist_ok=True)
for p in sorted(RAW.glob("p*.png")):
    dest = FIN/p.name
    if p.stem in DIALOGUE:
        used, found = letter_page(p, DIALOGUE[p.stem], dest)
        print(f"[{p.stem}] found={found} filled={used}")
    else:
        Image.open(p).save(dest)

title_plate(FIN/"p01.png", FIN/"p01.png",
            title="INHERITANCE",
            subtitle="UCHIHA NARUTO: THE SAGE   .   VOLUME ONE",
            chapter="CHAPTER EIGHT")
print("[title] composited onto p01")

pages = sorted(FIN.glob("p*.png"))
ims = [Image.open(x).convert("RGB") for x in pages]
ims[0].save(HERE/"ch08"/"Chapter08.pdf", save_all=True, append_images=ims[1:])
print(f"\nPDF: {len(ims)} pages -> chapters/ch08/Chapter08.pdf")
