"""Chapter 1 — "The Tenth of October". 25 images: title plate + 24 story pages.

gpt-image-2 on Replicate. References are free there, so every page carries its full
binding set. Resumable — existing pages are skipped. Run: python3 chapters/build_ch01.py
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch01" / "raw"
LED = Ledger(HERE / "ch01" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

BIND_N6 = ("Image 1 is the CHARACTER REFERENCE for the boy: a small underfed six-year-old with short "
           "spiky blond hair, blue eyes and faint whisker marks, in a white short-sleeved shirt with "
           "a red spiral on the chest, orange shorts and dark sandals. Reproduce that face, hair and "
           "outfit exactly. Ignore Image 1's white background, its three-view layout and its standing "
           "pose. " + UNIQUE + " ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and lighting "
            "exactly. Do not copy its camera angle, and ignore the fact that it is empty of people. ")

BIND_MOB = ("Image {i} shows the four villager archetypes. Use these faces and clothes for the adults. "
            "Ignore its white background and lineup layout. ")

LIGHT_FEST = "Lighting: warm orange paper-lantern light from overhead, deep blue-black shadows. "
LIGHT_ALLEY = ("Lighting: the alley is in deep blue-black shadow, with warm orange festival light "
               "spilling in from the alley mouth behind the adults. ")
LIGHT_HOSP = "Lighting: flat cold clinical daylight, pale and cheerless. "

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 ("00_title", 1,
  "A single full-bleed illustration, no panels. A high wide view looking down a festival street in a "
  "feudal Japanese village at night: rows of glowing orange paper lanterns receding into the "
  "distance, food stalls, a dense crowd of townspeople in yukata seen from behind and above, warm "
  "light. In the very centre of the crowd, tiny and alone and facing the opposite way to everyone "
  "else, stands one small blond boy in a white shirt and orange shorts. Keep the entire upper third "
  "of the image as calm uncluttered night sky for a title to be placed later. " + LIGHT_FEST,
  R("naruto_06", "env_festival_street"), "high"),

 ("p01", 1,
  "A single full-page splash illustration, no interior panel divisions. High wide shot looking down "
  "the festival street at night — lanterns strung overhead in receding rows, food stalls with cloth "
  "awnings, a dense happy crowd in yukata. No protagonist visible anywhere. Keep the upper third as "
  "open sky. " + LIGHT_FEST, R("env_festival_street"), "high"),

 ("p02", 3,
  PAGE + "PANEL 1 (wide, top): a stall rack hung with painted fox festival masks. PANEL 2 (middle): a "
  "mother lifting a small child onto her shoulders to see over the crowd, both laughing. PANEL 3 "
  "(wide, bottom): two old men sharing sake at a low table, mid-laugh. Everyone is warm and happy. "
  + LIGHT_FEST, R("env_festival_street"), "low"),

 ("p03", 4,
  PAGE + "The mood turns. PANEL 1: a stall vendor's smile drops as he looks off-panel. PANEL 2: two "
  "women stop mid-conversation, faces going flat. PANEL 3: close-up of a hand setting a cup down on "
  "a table. PANEL 4 (wide, bottom): a dozen townspeople in the crowd, all turned to look the same "
  "way, every expression cold and hard. " + BIND_MOB.format(i=2) + LIGHT_FEST,
  R("env_festival_street", "mob_archetypes"), "low"),

 ("p04", 3,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "PANEL 1 (wide, top): very low camera at knee height — the small blond boy weaving between the "
  "legs of adults in the crowded festival street. PANEL 2: close on his face, breathing hard, not "
  "panicking, resigned — he has done this before. PANEL 3 (wide, bottom): a large adult hand grabs "
  "at his collar from behind and just misses. " + LIGHT_FEST,
  R("naruto_06", "env_festival_street"), "low"),

 ("p05", 4,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "A chase through narrow back alleys, four panels. PANEL 1: the boy rounding a corner at speed. "
  "PANEL 2: his sandals splashing through a puddle. PANEL 3: an overturned crate behind him. PANEL "
  "4 (wide, bottom): a high wide shot of the boy tiny at the bottom of a tall narrow alley, dwarfed "
  "by the buildings. Keep him small in every panel. " + LIGHT_ALLEY,
  R("naruto_06", "env_alley"), "low"),

 ("p06", 2,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top two thirds): wide shot from behind — the boy has stopped dead at the closed "
  "far end of the alley, his back to us, facing the fence. He is completely still. PANEL 2 (small, "
  "bottom): tight insert on his hands at his sides as his fists slowly unclench. " + LIGHT_ALLEY,
  R("naruto_06", "env_alley"), "low"),

 ("p07", 3,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (wide, top): shot from behind the boy's shoulder — five adult villagers round the corner "
  "into the alley and fan out to fill the frame, lit from below by a dropped lantern. PANEL 2: their "
  "faces, hard and eager. PANEL 3 (wide, bottom): the boy small against the fence, the adults "
  "closing in as a wall of bodies. " + LIGHT_ALLEY,
  R("naruto_06", "env_alley", "mob_archetypes"), "low"),

 ("p08", 2,
  PAGE + BIND_N6 + BIND_MOB.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): extreme close-up of a grinning adult mouth, teeth showing. PANEL 2 (large, "
  "bottom): wide two-shot down the length of the alley — the group of adults on one side, the small "
  "boy alone against the fence on the other, a wide empty gap of stone ground between them. "
  + LIGHT_ALLEY + BALLOONS.format(k="two"),
  R("naruto_06", "mob_archetypes", "env_alley"), "low"),

 ("p09", 3,
  PAGE + BIND_N6 + BIND_MOB.format(i=2) +
  "PANEL 1 (top): a heavyset bearded villager crouches down to the boy's eye level, hands on knees. "
  "PANEL 2 (middle, large): the boy's face in close-up — completely blank. No fear, no defiance, "
  "nothing at all. PANEL 3 (bottom): the villager's grin faltering, unsettled by the silence. "
  + LIGHT_ALLEY + BALLOONS.format(k="two"),
  R("naruto_06", "mob_archetypes"), "low"),

 ("p10", 3,
  PAGE + BIND_N6 + BIND_MOB.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): a boot driving into the small boy's stomach — shot from the side, impact implied "
  "not graphic. PANEL 2 (middle): the boy folded over on the stone ground, coughing. PANEL 3 "
  "(bottom): his face on the ground, eyes still open, still silent. " + LIGHT_ALLEY,
  R("naruto_06", "mob_archetypes", "env_alley"), "low"),

 ("p11", 2,
  PAGE + BIND_N6 +
  "PANEL 1 (top): a hand reaching into a worn coat and drawing out a plain domestic kitchen knife — "
  "an ordinary household object, not a weapon. PANEL 2 (large, bottom): the small boy on the ground "
  "looking up at the blade with no reaction whatsoever. " + LIGHT_ALLEY,
  R("naruto_06", "env_alley"), "low"),

 ("p12", 1,
  "A single full-page splash illustration, no panel divisions. " + BIND_N6 +
  "The moment AFTER. The small blond boy lies on wet stone ground in a dark alley. One of his hands "
  "is pinned to the ground with a plain kitchen knife standing upright in it; dark blood spreads "
  "across the stone around it. The camera is close on HIS FACE, which is doing absolutely nothing — "
  "no scream, no tears, entirely blank. The wound itself is not shown in detail, only the knife "
  "handle and the spreading dark on the stone. " + LIGHT_ALLEY,
  R("naruto_06", "env_alley"), "medium"),

 ("p13", 3,
  PAGE + BIND_MOB.format(i=1) +
  "PANEL 1 (top): the group of adults standing over him, waiting, expectant. PANEL 2 (middle, "
  "wide): nothing happens. Silence. Their expectant faces beginning to change. PANEL 3 (bottom): two "
  "of them exchanging a sideways look — uneasy. For the first time the child has unsettled them. "
  + LIGHT_ALLEY, R("mob_archetypes", "env_alley"), "low"),

 ("p14", 3,
  PAGE + BIND_N6 + BIND_MOB.format(i=2) +
  "PANEL 1 (top): the thin sharp-faced villager leans down close to the boy's face, speaking. PANEL "
  "2 (middle): the boy's eyes SNAP WIDE OPEN — the first real expression he has shown in the whole "
  "chapter. PANEL 3 (bottom, large): extreme close-up of one blue eye, pupil small. Something has "
  "landed. " + LIGHT_ALLEY + BALLOONS.format(k="two"),
  R("naruto_06", "mob_archetypes"), "low"),

 ("p15", 3,
  PAGE + BIND_N6 + BIND_MOB.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): another villager rounds on the one who spoke, alarmed. PANEL 2 (middle): the two "
  "of them arguing, the older bald man gesturing sharply. PANEL 3 (bottom): a dismissive wave of a "
  "hand, the argument settled, the group turning back toward the boy. " + LIGHT_ALLEY
  + BALLOONS.format(k="three"), R("naruto_06", "mob_archetypes", "env_alley"), "low"),

 ("p16", 2,
  PAGE + BIND_ENV.format(i=1) +
  "PANEL 1 (large, top): the beating resumes, rendered ENTIRELY as flat black silhouettes against "
  "the warm orange lantern-lit alley mouth behind them — a cluster of adult shapes, arms raised, no "
  "interior detail at all. PANEL 2 (small, bottom): a strip of empty stone ground at the bottom of "
  "the frame, with one small dropped sandal lying on it. " + LIGHT_ALLEY,
  R("env_alley"), "low"),

 ("p17", 2,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): high wide shot of the now-empty alley. The small boy is a crumpled shape "
  "alone on the stone ground. PANEL 2 (wide, bottom): looking out of the alley mouth toward the "
  "festival street beyond — lanterns still glowing warm, the celebration still going on, completely "
  "indifferent. " + LIGHT_ALLEY, R("naruto_06", "env_alley"), "low"),

 ("p18", 1,
  "A single full-width illustration filling the whole page, no panel divisions. Looking straight up "
  "at a plain flat hospital ceiling — white boards, a simple light fitting, a slight water stain in "
  "one corner. Completely empty and silent. Keep the lower third relatively plain for a caption to "
  "be placed later. " + LIGHT_HOSP, R("env_hospital"), "low"),

 ("p19", 3,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "PANEL 1 (wide, top): the small boy lying in a hospital bed, most of his body and one hand wrapped "
  "in white bandages, eyes closed. PANEL 2 (middle): extreme close-up of one closed eye — he is "
  "awake and listening. PANEL 3 (wide, bottom): two adult figures blurred and indistinct through the "
  "frosted glass panel of the door, seen from inside the room. " + LIGHT_HOSP,
  R("naruto_06", "env_hospital"), "low"),

 ("p20", 3,
  PAGE + "Image 1 is the reference for the elderly man in white and red robes with a short grey "
  "beard. Image 2 is the reference for the tall younger man with spiky silver hair, a dark cloth "
  "mask covering his face below the nose, and a slanted headband covering his left eye. Reproduce "
  "both faces and outfits exactly; ignore their white backgrounds and three-view layouts. "
  "PANEL 1 (top): the two men standing in a hospital corridor, talking quietly. PANEL 2 (middle): "
  "close on the old man, tired and grave. PANEL 3 (bottom): close on the silver-haired man, his one "
  "visible eye hard. " + LIGHT_HOSP + BALLOONS.format(k="three"),
  R("hiruzen", "kakashi", "env_hospital"), "low"),

 ("p21", 3,
  PAGE + "Image 1 is the elderly man in white and red robes; Image 2 is the silver-haired masked "
  "man. Reproduce both exactly, ignoring their white backgrounds and layouts. "
  "PANEL 1 (top): the silver-haired man steps forward, appealing, one hand half-raised. PANEL 2 "
  "(middle): the old man refuses — a small firm shake of the head, eyes lowered. PANEL 3 (bottom, "
  "close): the silver-haired man's hand slowly closing into a fist at his side. " + LIGHT_HOSP
  + BALLOONS.format(k="three"), R("hiruzen", "kakashi"), "low"),

 ("p22", 3,
  PAGE + BIND_N6 + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the empty hospital corridor through the door glass — the two adults have gone. "
  "PANEL 2 (middle, wide): the bandaged boy in the bed, eyes still shut, absolutely still. PANEL 3 "
  "(bottom, large): extreme close-up of one blue eye opening. He has family. They did not want him. "
  + LIGHT_HOSP, R("naruto_06", "env_hospital"), "low"),

 ("p23", 3,
  PAGE + BIND_N6 +
  "Image 2 is the reference for the elderly man in white and red robes with a short grey beard — "
  "reproduce his face and outfit exactly, ignoring its white background and layout. "
  "PANEL 1 (top): the old man sits on a stool beside the hospital bed, smiling warmly at the boy. "
  "PANEL 2 (middle): the bandaged boy looking up at him and asking a question, face open. PANEL 3 "
  "(bottom): the old man's answer — still smiling, but the smile does not reach his eyes. "
  + LIGHT_HOSP + BALLOONS.format(k="three"), R("naruto_06", "hiruzen", "env_hospital"), "low"),

 ("p24", 2,
  PAGE + BIND_N6 +
  "Image 2 is the elderly man in white and red robes — reproduce him exactly, ignoring the white "
  "background and layout. Image 3 is the hospital room LOCATION reference — the scene takes place in "
  "that room, at the bedside. PANEL 1 (top): the old man has already stood up and half-turned away "
  "toward the door, deflecting, changing the subject. The boy watches him go. PANEL 2 (large, "
  "bottom, the final panel of the chapter): the boy's face very close in the foreground, sharp and "
  "still, looking directly out at the reader — he has stopped asking. The old man is a soft "
  "out-of-focus shape far behind him. " + LIGHT_HOSP + BALLOONS.format(k="two"),
  R("naruto_06", "hiruzen", "env_hospital"), "medium"),
]


def build_one(spec):
    pid, panels, desc, refs, quality = spec
    dest = OUT / f"{pid}.png"
    if dest.exists():
        return f"[skip] {pid}"
    prompt = desc + " " + STYLE + " " + NO_TEXT
    img, cost = rep_generate(prompt, refs=refs, quality=quality, aspect="2:3")
    OUT.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(img)
    LED.add(page=pid, quality=quality, cost=cost, refs=[pathlib.Path(r).stem for r in refs])
    return f"[ok]   {pid}  {quality:6} ${cost:.3f}"


if __name__ == "__main__":
    only = sys.argv[1:] or None
    todo = [p for p in PAGES if not only or p[0] in only]
    print(f"building {len(todo)} pages -> {OUT}")
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        for line in ex.map(build_one, todo):
            print(line)
    print(f"\nchapter ledger: ${LED.spent:.3f}")
