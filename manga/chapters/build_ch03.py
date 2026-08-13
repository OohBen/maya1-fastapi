"""Chapter 3 — "Academy". 20 pages (p01 doubles as the title plate).

The volume's breather: the only chapter that costs him nothing. Sits before the
chapter that breaks him. Warm at the end.

gpt-image-2 on Replicate. References are free there, so every page carries its full
binding set. Resumable — existing pages are skipped. Run: python3 chapters/build_ch03.py
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch03" / "raw"
LED = Ledger(HERE / "ch03" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# ------------------------------------------------------------------ bindings
BIND_N7 = ("Image 1 is the CHARACTER REFERENCE for the boy: a small seven-year-old with short "
           "spiky bright-blond hair, blue eyes and three faint whisker marks on each cheek, wearing "
           "a bright orange tracksuit jumpsuit with a tall dark navy collar, a navy waistband and "
           "navy trim, a pair of goggles with a dark navy strap pushed up onto his forehead, and "
           "black open-toe shinobi sandals. Reproduce that face, hair, goggles and outfit exactly. "
           "Ignore Image 1's white background, its three-view layout and its standing pose. "
           + UNIQUE + " ")

BIND_HIRUZEN = ("Image {i} is the CHARACTER REFERENCE for the old man: an elderly man with short "
                "grey hair, a short grey beard and a lined kind face, wearing long white robes with "
                "dark red cuffs and hem over a dark red under-robe with a tan sash, and a wide "
                "conical straw hat hanging on his back. Reproduce that face and outfit exactly. "
                "Ignore Image {i}'s white background, its three-view layout and its standing pose. ")

BIND_IRUKA = ("Image {i} is the CHARACTER REFERENCE for the instructor: a young adult man with "
              "brown hair pulled up into a short spiky ponytail, a straight horizontal scar across "
              "the bridge of his nose, a dark navy long-sleeved shirt under a green flak vest, and "
              "a dark cloth headband whose metal plate is completely smooth and blank. Reproduce "
              "that face and outfit exactly. Ignore Image {i}'s white background, its three-view "
              "layout, its standing pose, and any markings on the metal plate — the plate is plain "
              "polished metal with nothing on it. ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the tall gaunt old man: a very old man "
               "with a long, deeply lined, pale hollow-cheeked face, dark red eyes, and long spiked "
               "coal-black hair falling well past his shoulders, wearing a plain black full-length "
               "robe with wide sleeves and dark shoes, and leaning on a plain wooden walking cane. "
               "Reproduce that face, hair, robe and cane exactly. Ignore Image {i}'s white "
               "background, its three-view layout and its standing pose. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore the fact that it is empty "
            "of people. ")

BIND_MOB = ("Image {i} shows the four villager archetypes. Use these faces and clothes as the basis "
            "for the adult villagers. Ignore its white background and lineup layout. ")

# ------------------------------------------------------------------ lighting
LIGHT_OFFICE = ("Lighting: warm amber late-afternoon daylight through the tall arched windows, "
                "honey-brown wood everywhere, soft warm shadows, calm and still. ")
LIGHT_ACADEMY = ("Lighting: flat unromantic midday daylight, pale blue sky, bleached dirt ground, "
                 "short hard shadows, nothing glamorous about it. ")
LIGHT_CLASS = ("Lighting: flat daylight through the tall window bank falling across the wooden "
               "benches, warm dull browns, unromantic and ordinary. ")
LIGHT_APT = ("Lighting: dim and cold — one bare bulb hanging from the ceiling, cracked grey-green "
             "walls, cold blue-grey shadow filling the corners of the room. ")

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 ("p01", 1,
  "A single full-bleed illustration filling the whole page, no interior panel divisions. A wide "
  "eye-level view across the empty dirt training yard toward the front of the wooden two-storey "
  "shinobi academy building, with the big tree and its rope swing at the right of frame. Standing "
  "alone in the middle of the wide empty yard, small in the frame and seen from behind, is one "
  "seven-year-old boy in a bright orange jumpsuit with goggles on his forehead, looking up at the "
  "building. Nobody else is present. Keep the entire upper third of the image as calm uncluttered "
  "pale blue sky with a few flat clouds, for a title to be placed later. "
  + BIND_N7 + BIND_ENV.format(i=2) + LIGHT_ACADEMY,
  R("naruto_07", "env_academy_ext"), "high"),

 ("p02", 3,
  PAGE + BIND_N7 + BIND_HIRUZEN.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): establishing interior of the round Hokage office — the old man in white and "
  "red robes seated behind the big wooden desk stacked with paperwork, the small blond boy standing "
  "in front of the desk, barely taller than its edge. PANEL 2 (middle): over the old man's "
  "shoulder, close on his hand pressing a small wooden stamp down onto a blank enrolment form. "
  "PANEL 3 (wide, bottom): the boy up on tiptoe with both hands on the desk edge, trying to see "
  "what was stamped. " + LIGHT_OFFICE + BALLOONS.format(k="two"),
  R("naruto_07", "hiruzen", "env_hokage_office"), "low"),

 ("p03", 3,
  PAGE + BIND_N7 + BIND_HIRUZEN.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the small blond boy has both fists thrown up in the air in triumph, goggles "
  "knocked askew on his forehead, mouth wide open, delighted. PANEL 2 (middle): the old man watching "
  "him from behind the desk, chin resting on his folded hands, amused and fond, a thin line of pipe "
  "smoke rising. PANEL 3 (bottom, large): close on the boy's face — an enormous wide open-mouthed "
  "grin, all teeth, very loud. Draw it deliberately as a performance: the mouth is huge and bright "
  "but the eyes above it stay flat, watchful and unsmiling. " + LIGHT_OFFICE + BALLOONS.format(k="two"),
  R("naruto_07", "hiruzen", "env_hokage_office"), "low"),

 ("p04", 2,
  PAGE + "A deliberately quiet page with only TWO large panels and generous empty space. Keep the "
  "staging simple and uncluttered — very few objects, plain surfaces, calm negative space. "
  + BIND_N7 + BIND_HIRUZEN.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (large, top two thirds): the old man has set his long pipe down in a tray and looks "
  "directly across the desk at the boy, calm and serious. Behind him only the plain office wall and "
  "one tall arched window — clear the paperwork out of this frame. PANEL 2 (bottom third): the boy "
  "with both hands flat on the edge of the desk, answering instantly without thinking, mouth open "
  "mid-word, pleased with his own answer. " + LIGHT_OFFICE + BALLOONS.format(k="two"),
  R("naruto_07", "hiruzen", "env_hokage_office"), "medium"),

 ("p05", 3,
  PAGE + "A quiet page. Keep every panel simple and uncluttered — plain surfaces, calm negative "
  "space, very few objects. " + BIND_N7 + BIND_HIRUZEN.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (large, top half): the old man leans forward across the desk, one hand lifted slightly, "
  "speaking gently and directly to the boy. Behind him only plain wall and window light — clear the "
  "paper stacks out of this frame. Place TWO speech balloons in this panel, well apart from one "
  "another with a clear band of background visible between them, so they never touch, overlap or "
  "join up — one high in the upper left corner of the panel, the other low on the right side of the "
  "panel. PANEL 2 (small, middle): tight insert of the boy's small hands "
  "gone still on the edge of the desk. PANEL 3 (wide, bottom): the boy's face looking up, quiet for "
  "once — not understanding it yet, but listening. One speech balloon in this panel. "
  + LIGHT_OFFICE + BALLOONS.format(k="three"),
  R("naruto_07", "hiruzen", "env_hokage_office"), "medium"),

 ("p06", 3,
  PAGE + BIND_N7 + BIND_HIRUZEN.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the boy at the office door on his way out, half turned back, one arm up in a huge "
  "wave, grinning. PANEL 2 (middle): the door now closed. The old man alone behind the desk, the "
  "smile gone from his face, looking at the shut door. PANEL 3 (wide, bottom): high wide shot of the "
  "whole round office — the old man very small behind his desk in the middle of the tall stacks of "
  "paperwork, drawing on his pipe. " + LIGHT_OFFICE + BALLOONS.format(k="one"),
  R("naruto_07", "hiruzen", "env_hokage_office"), "low"),

 ("p07", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "First morning of school. PANEL 1 (wide, top): the front of the wooden academy building across the "
  "dirt yard, families arriving — adult villagers walking their children toward the doors, a few "
  "carrying satchels for them. PANEL 2 (middle): the small blond boy in the orange jumpsuit coming "
  "up the path completely alone with no adult beside him, walking fast, grinning hugely. PANEL 3 "
  "(wide, bottom): as he passes, a row of parents' heads turning to follow him, their expressions "
  "hardening. " + LIGHT_ACADEMY,
  R("naruto_07", "env_academy_ext", "mob_archetypes"), "low"),

 ("p08", 3,
  PAGE + BIND_ENV.format(i=1) + BIND_MOB.format(i=2) +
  "The blond boy is not in frame anywhere on this page; these are the parents watching him go. "
  "PANEL 1 (top): a mother crouched down beside her small dark-haired son at the academy gate, one "
  "hand on his shoulder, speaking quietly into his ear while her eyes stay fixed on something "
  "off-panel. PANEL 2 (middle): a father's hand closing around his daughter's wrist and drawing her "
  "back a step. PANEL 3 (wide, bottom): four adult villagers standing together in the yard, all "
  "turned the same way, every face gone flat and cold. " + LIGHT_ACADEMY + BALLOONS.format(k="two"),
  R("env_academy_ext", "mob_archetypes"), "low"),

 ("p09", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "A silent page — leave it entirely free of speech balloons. PANEL 1 (wide, top): the small blond "
  "boy from behind, small in the frame, walking on across the dirt yard between the watching adult "
  "villagers. PANEL 2 (middle): three-quarter close on his face — the huge grin is still there, "
  "wide and bright and completely fixed in place, but his eyes are flat and aimed down at the "
  "ground, meeting nobody. PANEL 3 (bottom, large): extreme close-up of his eyes alone above the "
  "grinning mouth — no warmth in them at all, the faint whisker marks at the edge of frame. Draw "
  "the gap between the mouth and the eyes as the whole point of the page. " + LIGHT_ACADEMY,
  R("naruto_07", "env_academy_ext", "mob_archetypes"), "low"),

 ("p10", 3,
  PAGE + BIND_N7 + BIND_IRUKA.format(i=2) + BIND_ENV.format(i=3) + BIND_MOB.format(i=4) +
  "PANEL 1 (wide, top): the classroom interior seen from the back — tiered wooden benches filled "
  "with children of about seven, the scarred young instructor standing at the lectern in front of "
  "the blackboard. The blackboard is completely clean and blank. PANEL 2 (middle): the small blond "
  "boy sitting alone on a bench at the very back, the seats on both sides of him conspicuously "
  "empty although the rest of the room is full. PANEL 3 (bottom): the instructor mid-lecture with a "
  "stick of chalk in his hand, addressing the front rows and not once looking at the back. "
  + LIGHT_CLASS + BALLOONS.format(k="one"),
  R("naruto_07", "iruka", "env_classroom", "mob_archetypes"), "low"),

 ("p11", 3,
  PAGE + BIND_N7 + BIND_IRUKA.format(i=2) + BIND_ENV.format(i=3) + BIND_MOB.format(i=4) +
  "PANEL 1 (top): the small blond boy standing up on his back bench with both arms flung out, "
  "mouth wide open, clowning loudly for the whole room — a deliberate performance. PANEL 2 "
  "(middle): the other children reacting — two laughing, the rest looking away, bored or annoyed; "
  "nobody sitting near him. PANEL 3 (bottom, large): the young instructor turned toward the back of "
  "the room, open contempt on his scarred face, the chalk snapped in his fist. " + LIGHT_CLASS
  + BALLOONS.format(k="two"),
  R("naruto_07", "iruka", "env_classroom", "mob_archetypes"), "low"),

 ("p12", 3,
  PAGE + BIND_N7 + BIND_IRUKA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the young scarred instructor with his arm thrown straight out, pointing at the "
  "classroom door, jaw set. PANEL 2 (middle): the small blond boy in the open doorway seen from "
  "behind, one hand on the frame, shoulders up around his ears, still grinning back over his "
  "shoulder at the room. PANEL 3 (wide, bottom): the wooden corridor outside — the closed classroom "
  "door, and the boy sitting on the floor with his back against the wall beside it, knees up, "
  "completely alone. The grin is gone; his face is empty. " + LIGHT_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "iruka", "env_classroom"), "low"),

 ("p13", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "Every single person on this page is a schoolchild of about seven years old, in plain simple "
  "village clothes. There are no grown-ups anywhere on this page — no adults, no teachers, no "
  "villagers, only small children. "
  "Lunch break, no speech balloons on this page. PANEL 1 (wide, top): the academy playground yard — "
  "groups of small children playing tag and sitting in circles eating their lunches across the open "
  "dirt, the big tree at one side. "
  "PANEL 2 (middle): the small blond boy sitting by himself on the rope swing under the tree, well "
  "away from everyone, a cloth-wrapped lunch open on his knees. PANEL 3 (bottom): close on the lunch "
  "itself — one plain rice ball and a few pickled vegetables, arranged neatly in a battered tin box. "
  "Clearly packed by a child for himself. " + LIGHT_ACADEMY,
  R("naruto_07", "env_playground"), "low"),

 ("p14", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "Two older boys of about eleven appear on this page: both are heavier and a head taller than the "
  "blond boy, one with cropped dark brown hair and one with black hair, in plain dull green and grey "
  "village clothes. They look nothing like the blond boy. PANEL 1 (top): the two older boys standing "
  "over him where he sits on the swing, one with a hand gripping the swing rope, both smirking. "
  "PANEL 2 (middle): a hand knocking the tin lunch box off his knees — rice and pickles scattering "
  "across the dirt. PANEL 3 (bottom): the small blond boy sitting on the ground where the swing "
  "tipped him, looking up at them, his face carefully and completely blank. " + LIGHT_ACADEMY
  + BALLOONS.format(k="two"),
  R("naruto_07", "env_playground"), "low"),

 ("p15", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "The same two older boys as before: heavier, a head taller, one with cropped dark brown hair and "
  "one with black hair, in plain dull green and grey village clothes, looking nothing like the blond "
  "boy. PANEL 1 (top): the two older boys walking away across the yard with their backs to us, "
  "laughing to each other. PANEL 2 (middle): tight insert on the rice ball lying in the dirt. PANEL "
  "3 (wide, bottom): the small blond boy crouched down, picking it up, brushing the dirt off it with "
  "his thumb — and eating it anyway. His face gives away nothing at all. " + LIGHT_ACADEMY
  + BALLOONS.format(k="one"),
  R("naruto_07", "env_playground"), "low"),

 ("p16", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "Evening, home alone. PANEL 1 (wide, top): the small one-room apartment seen from the doorway — "
  "cracked grey-green walls, a bare bulb on a cord, a small wooden table with two stools, a narrow "
  "bed against the far wall. The small blond boy is a little figure crossing the room, dropping his "
  "bag on the floor. PANEL 2 (middle): a kitchen cupboard door hanging open on empty shelves — one "
  "dented tin standing alone, nothing else. PANEL 3 (bottom, wide): a single paper cup of instant "
  "noodles on the table under the bulb, steam rising from it, the boy sitting on a stool with his "
  "chin down on the tabletop, watching it, still in the orange jumpsuit with the goggles on his "
  "forehead. " + LIGHT_APT,
  R("naruto_07", "env_apartment_int"), "low"),

 ("p17", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the boy's head snapping up from the table toward the flat apartment door — "
  "somebody has knocked. PANEL 2 (middle, large): the door open. Standing outside in the dim "
  "walkway is the tall gaunt old man in the black robe with long spiked black hair, leaning on his "
  "wooden cane, two brown paper grocery bags full of vegetables and packets held in his other arm. "
  "PANEL 3 (bottom): the small blond boy in the doorway staring up at him, noodles forgotten, "
  "caught between suspicion and shock. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p18", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the tall gaunt old man in black is already inside, unhurried, setting the paper "
  "grocery bags down on the kitchen counter beside the sink, his back half turned. PANEL 2 (middle): "
  "the small blond boy behind him with both fists clenched at his sides, indignant, shouting up at "
  "him. PANEL 3 (wide, bottom): the old man looking back down over his shoulder at the boy — no "
  "apology anywhere in his face, and no unkindness in it either. " + LIGHT_APT
  + BALLOONS.format(k="three"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p19", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the two of them at the small wooden table under the bare bulb — the old man "
  "seated on one stool with both hands folded over the head of his cane, the boy on the other stool "
  "with a full bowl of food in front of him, eating fast with both elbows on the table. PANEL 2 "
  "(middle): tight insert on the old man's lined hands resting on the head of the cane, still. "
  "PANEL 3 (bottom, wide): the old man at the open apartment door on his way out, half in shadow, "
  "pausing to look back into the room. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p20", 2,
  PAGE + "The final page of the chapter, and the warmest image in the book so far. "
  + BIND_N7 + BIND_ENV.format(i=2) +
  "PANEL 1 (a narrow strip across the top): the closed apartment door seen from inside the room, "
  "the old man gone. PANEL 2 (very large, filling the rest of the page): the small blond boy alone "
  "in the middle of the room, one brown paper grocery bag still hugged against his chest, looking "
  "back at the shut door — and smiling. This smile is small, closed-mouthed and slightly crooked, "
  "nothing whatsoever like the huge open-mouthed grin he performs in public. The eyes carry the "
  "whole page: draw them as soft narrowed curves, creased and lifted at the outer corners, with a "
  "bright round highlight in each one and the lower lids pushed up by the smile, so that the "
  "feeling clearly reaches all the way up into them; a faint flush across his nose and cheeks. "
  "This is the warmest, happiest face in the whole book — draw it that way. Frame him close, a "
  "chest-up three-quarter view, his face large and filling much of the panel. "
  "Lighting: the bare bulb hanging just above him burns bright and warm, throwing a strong golden "
  "amber pool of light down over his hair, face and the paper bag — his skin is warmly lit and his "
  "eyes catch the light. Only the far corners of the cracked room stay cold blue-grey, so the warm "
  "light around him reads as the single bright thing on the page.",
  R("naruto_07", "env_apartment_int"), "medium"),
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
    with cf.ThreadPoolExecutor(max_workers=50) as ex:
        for line in ex.map(build_one, todo):
            print(line)
    print(f"\nchapter ledger: ${LED.spent:.3f}")
