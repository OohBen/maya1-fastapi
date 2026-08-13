"""Chapter 2 — "The Old Man in Black". 20 images: title plate + 19 story pages.

The volume's hook chapter. The vanishing mob (p13) is the image the whole chapter
exists to deliver, and beats 5->6 are staged as a page turn: the last panel of p12 is
his shut eyes, the first thing on p13 is the empty alley. How they vanished is never
shown, on any page.

gpt-image-2 on Replicate. References are free there, so every page carries its full
binding set. Resumable — existing pages are skipped. Run: python3 chapters/build_ch02.py
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch02" / "raw"
LED = Ledger(HERE / "ch02" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# ------------------------------------------------------------------ bindings
BIND_N7 = ("Image 1 is the CHARACTER REFERENCE for the boy: a small seven-year-old with short "
           "spiky blond hair, blue eyes and three faint whisker marks on each cheek, wearing a "
           "bright orange tracksuit jumpsuit with a dark navy collar and a dark navy waistband, a "
           "pair of round goggles on a navy strap worn on his forehead above his eyes, and black "
           "open-toe shinobi sandals. Reproduce that face, hair, goggles and outfit exactly. "
           "Ignore Image 1's white background, its three-view layout, its standing pose and its "
           "wide grin — his expression is described per panel below. " + UNIQUE + " ")

BIND_MAD = ("Image {i} is the CHARACTER REFERENCE for the old man: a tall gaunt elderly man in a "
            "long plain black robe with wide sleeves, very long spiked black hair falling well "
            "past his shoulders and framing his face, a deeply lined hollow-cheeked face, and a "
            "plain wooden walking cane he leans on. Reproduce that face, hair, robe and cane "
            "exactly. Ignore Image {i}'s white background, its three-view layout and its standing "
            "pose. ")

BIND_ZET = ("Image {i} is the CHARACTER REFERENCE for the plant creature: a humanoid figure whose "
            "body is split straight down the middle, one half pure white and the other half pure "
            "black, with round yellow eyes and a wide fixed grin, and a huge green venus-flytrap "
            "collar of pointed leaves closing around its head. Reproduce it exactly. Ignore Image "
            "{i}'s white background and its three-view layout. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore the fact that it is empty "
            "of people. ")

BIND_MOB = ("Image {i} shows the four villager archetypes. Use these faces and clothes for the "
            "adult villagers. Ignore its white background and its lineup layout. ")

SHINOBI = ("The adult shinobi all wear the same uniform: dark navy long-sleeved shirts and "
           "trousers under dark green sleeveless flak vests, with a metal-plated cloth band tied "
           "round the forehead. They are ordinary adults with dark or brown hair. ")

HALF_SHADOW = ("The old man's face is kept deliberately half in shadow: the upper half of his face "
               "is swallowed in hard flat black, only the mouth and jaw lit. ")

# ------------------------------------------------------------------ lighting
LIGHT_LOUNGE = ("Lighting: low amber late-afternoon sun coming through the tall windows in hard "
                "slanted shafts, everything away from the windows in deep warm brown shadow. ")
LIGHT_STREET_DAY = ("Lighting: flat unromantic overhead daylight, warm sandy plaster walls, plain "
                    "hard-edged shadows, nothing romantic about it. ")
LIGHT_APT_INT = ("Lighting: dim and cold — one bare yellow bulb hanging from the ceiling as the "
                 "only source, harsh shadows, the corners of the room nearly black. ")
LIGHT_APT_EXT = ("Lighting: night. The open concrete walkway is cold blue-black, with one small "
                 "warm yellow bulb over the doors as the only warm light in the frame. ")
LIGHT_ALLEY = ("Lighting: the alley is in deep blue-black shadow, with warm orange light spilling "
               "in from the alley mouth behind and from one lit doorway partway down. ")
LIGHT_NIGHT_ST = ("Lighting: night on a deserted village street — cold blue-black shadow across "
                  "the stone, a few small warm window lights far in the background. ")
LIGHT_NOWHERE = ("Lighting: near-black. Hard cold rim light picking out edges only, no warm tones "
                 "anywhere in the frame. ")

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 ("00_title", 1,
  "A single full-bleed illustration, no panels. A wide low view straight down a sunlit village "
  "street of wooden and sandy-plaster shopfronts. Walking toward the camera down the middle of the "
  "street, alone, is one small seven-year-old boy in a bright orange jumpsuit with goggles on his "
  "forehead, hands behind his head, grinning hugely. On both sides of him the adult townspeople "
  "have all stopped whatever they were doing and turned to watch him pass, every face flat and "
  "cold, and there is a clear ring of empty ground around him that nobody steps into. Keep the "
  "entire upper third of the image as calm uncluttered open sky above the rooftops for a title to "
  "be placed later. " + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) + LIGHT_STREET_DAY,
  R("naruto_07", "env_village_street", "mob_archetypes"), "high"),

 ("p01", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + SHINOBI +
  "PANEL 1 (wide, top): interior of a wooden shinobi common room — two dark green couches facing "
  "a low wooden table strewn with rolled scrolls and cups, tall windows along one wall. Three "
  "adult shinobi sit around the low table talking, relaxed, none of them looking around. PANEL 2 "
  "(small, middle): a sliding wooden door standing slightly ajar, and through the narrow gap a "
  "sliver of bright orange fabric. PANEL 3 (wide, bottom): camera down at floorboard level — the "
  "small blond boy in the orange jumpsuit lies flat on his stomach in the shadow behind the far "
  "couch, chin on the boards, completely still. The adults are out-of-frame legs beyond him. "
  + LIGHT_LOUNGE, R("naruto_07", "env_jonin_lounge"), "low"),

 ("p02", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + SHINOBI +
  "PANEL 1 (top, wide): two of the adult shinobi mid-conversation across the low table, one "
  "leaning back with a cup, both tired and unguarded. PANEL 2 (middle): close on the boy's face "
  "in the shadow behind the couch — eyes wide, absolutely focused, listening. PANEL 3 (bottom, "
  "wide): the third shinobi glances toward the door and lowers his voice, one hand half-raised. "
  + LIGHT_LOUNGE + BALLOONS.format(k="three"),
  R("naruto_07", "env_jonin_lounge"), "low"),

 ("p03", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + SHINOBI +
  "PANEL 1 (top, wide): the three adult shinobi around the low table, one of them speaking flatly, "
  "the other two not enjoying it. PANEL 2 (middle, large): extreme close-up of one wide blue eye "
  "of the hidden boy, the pupil shrinking to a point. PANEL 3 (bottom): tight insert on his two "
  "small hands flat on the floorboards, the fingers slowly curling in. " + LIGHT_LOUNGE
  + BALLOONS.format(k="two"), R("naruto_07", "env_jonin_lounge"), "low"),

 ("p04", 2,
  PAGE + BIND_N7 +
  "PANEL 1 (large, top two thirds): a symbolic illustration on a flat black field, not a real "
  "place. In the centre, the small blond boy in the orange jumpsuit stands facing the viewer, "
  "arms at his sides, drawn small. Filling the whole black field behind and around him, contained "
  "entirely within a faint outline the same shape as the boy, is the enormous shadow of a "
  "nine-tailed fox in dull red — its many tails fanning out, one single eye open and looking "
  "straight out at the viewer. Across the boy's stomach, glowing pale, is a spiral seal of "
  "black brush strokes. The fox is clearly inside the boy's shape, not behind him. PANEL 2 "
  "(small strip, bottom): back in the real world — a tight insert of the boy's own hand pressed "
  "flat against his own stomach through the orange jacket. " + LIGHT_NOWHERE,
  R("naruto_07"), "low"),

 ("p05", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "PANEL 1 (top, wide): a long empty wooden corridor of the shinobi building, seen from behind — "
  "the small boy walking away from the camera, tiny at the far end, one hand trailing the wall. "
  "PANEL 2 (middle): he has stopped walking. A small figure standing still in a long corridor, "
  "shot from the side. PANEL 3 (bottom, large): his face in close-up in the corridor shadow — no "
  "tears, no shock, no anger. Something has simply been slotted into place behind his eyes. "
  + LIGHT_LOUNGE, R("naruto_07", "env_jonin_lounge"), "low"),

 ("p06", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (top, wide): high angle looking down on a busy village street — the small boy in the "
  "orange jumpsuit walking along it with a clear ring of empty ground around him that the crowd "
  "leaves open. PANEL 2 (middle): three adult villagers' faces in a row across the panel, all "
  "watching him pass, all cold. PANEL 3 (bottom, wide): a mother takes her own small child by the "
  "wrist and pulls him across to the far side of the street. " + LIGHT_STREET_DAY,
  R("naruto_07", "env_village_street", "mob_archetypes"), "low"),

 ("p07", 2,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): close on the boy's face from the front — he puts the grin on. A huge "
  "loud open-mouthed grin, eyes crinkled shut, hands going up behind his head. It is a performance "
  "and it is a good one. PANEL 2 (large, bottom): the same boy a few steps further on, seen from "
  "behind now, walking away down the street. The grin is gone from the set of his shoulders. "
  "Nothing about his life has changed. " + LIGHT_STREET_DAY,
  R("naruto_07", "env_village_street"), "low"),

 ("p08", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (top, wide): a cramped one-room apartment at night — an unmade bed, a low table with "
  "empty instant-noodle cups, peeling walls. The small boy sits cross-legged on the floor eating. "
  "PANEL 2 (middle): the flimsy front door shuddering inward in its frame under heavy blows from "
  "outside, the boy's head turning toward it. PANEL 3 (bottom, wide): the door bursts open and "
  "three adult villagers stand in the doorway as near-silhouettes against the blue night behind "
  "them. " + LIGHT_APT_INT + BALLOONS.format(k="two"),
  R("naruto_07", "env_apartment_int", "mob_archetypes"), "low"),

 ("p09", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (top, wide): the open concrete walkway outside the apartment doors at night — two "
  "adult villagers haul the small boy out through his doorway by the back of his collar. He does "
  "not struggle. PANEL 2 (small, middle): tight insert on a dropped noodle cup rolling on the "
  "concrete. PANEL 3 (bottom, wide): looking down the exterior stairwell from above — the group "
  "descending, the boy carried between them like luggage. Every other door on the walkway stays "
  "shut. " + LIGHT_APT_EXT, R("naruto_07", "env_apartment_ext", "mob_archetypes"), "low"),

 ("p10", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (top): the boy thrown forward, landing hard on his hands and knees on wet stone, "
  "speed lines behind him. PANEL 2 (middle): looking back over his shoulder — four adult "
  "villagers standing across the mouth of the alley, backlit by warm orange light from the street "
  "beyond, their faces in shadow. Only four of them tonight. PANEL 3 (bottom, wide): a wide "
  "two-shot down the length of the alley — the small orange boy against the far fence, the four "
  "adults walking in toward him, a wide gap of empty stone between. " + LIGHT_ALLEY
  + BALLOONS.format(k="two"), R("naruto_07", "env_alley", "mob_archetypes"), "low"),

 ("p11", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "PANEL 1 (top): the boy pushes himself up onto his knees on the stone, head down, the goggles "
  "knocked askew on his forehead. PANEL 2 (middle): the four villagers' faces looking down into "
  "the camera, lit hard from below, eager. PANEL 3 (bottom, wide): a single adult arm at the very "
  "top of its swing, and the small kneeling boy beneath it, tiny at the bottom of the frame. "
  + LIGHT_ALLEY, R("naruto_07", "env_alley", "mob_archetypes"), "low"),

 ("p12", 2,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "Two panels only, stacked. PANEL 1 (top third): the cluster of adults standing over him, drawn "
  "entirely as flat black silhouettes against the warm orange alley mouth behind them, arms "
  "raised, with no interior detail at all. PANEL 2 (the bottom two thirds — the last panel on the "
  "page, and it must be the largest): an extreme close-up of the boy's face filling the whole "
  "panel, nothing else in it. Both of his eyes are squeezed tightly shut, brows drawn down, jaw "
  "set. He is waiting for the pain to arrive. " + LIGHT_ALLEY,
  R("naruto_07", "env_alley", "mob_archetypes"), "low"),

 ("p13", 1,
  "A single full-page splash illustration filling the whole page, with no panel divisions and no "
  "gutters. " + BIND_N7 + BIND_ENV.format(i=2) +
  "The camera sits low, close to the wet stone ground, looking down the length of the narrow "
  "alley toward its open mouth in the distance. THE ALLEY IS COMPLETELY EMPTY OF ADULTS — every "
  "one of the four villagers who was standing over him a second ago is simply gone, and the warm "
  "orange light from the street at the alley mouth now falls unobstructed all the way down the "
  "stone toward the camera because there is nobody left standing in it. Kneeling on the stone in "
  "the near foreground, drawn small, is the seven-year-old boy in the bright orange jumpsuit. He "
  "has just opened his eyes: both eyes are WIDE OPEN, staring straight down the empty alley, his "
  "mouth slightly parted in astonishment. The ground in front of him is clean and undisturbed — "
  "plain wet stone, an unmoved wooden crate. There is nothing at all in the frame to explain "
  "where the adults went: no smoke, no dust cloud, no scattered clothing, no marks on the stone, "
  "no glow, no motion streaks, no debris, no bodies. The emptiness is the subject of the picture. "
  + LIGHT_ALLEY, R("naruto_07", "env_alley"), "medium"),

 ("p14", 3,
  PAGE + BIND_N7 + BIND_MAD.format(i=2) + BIND_ENV.format(i=3) + HALF_SHADOW +
  "PANEL 1 (top): the boy still on his knees, head turning, looking around an alley with nobody "
  "in it. PANEL 2 (middle, wide): the alley mouth seen from where he kneels — one tall figure in "
  "a long black robe stands there leaning on a walking cane, rendered as a complete flat black "
  "silhouette against the warm orange street light behind him. PANEL 3 (bottom, large): closer "
  "on the old man. His black robe, his long spiked black hair and the cane are clearly drawn, but "
  "the upper half of his face is still lost in hard black shadow, with a single point of red "
  "light where one eye should be. " + LIGHT_ALLEY + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_alley"), "low"),

 ("p15", 3,
  PAGE + BIND_N7 + BIND_MAD.format(i=2) + BIND_ENV.format(i=3) + HALF_SHADOW +
  "PANEL 1 (top): low camera behind the kneeling boy, looking up past his shoulder — he is very "
  "small in the frame and the robed old man is very tall. PANEL 2 (middle, large): the old man "
  "takes one step into the alley, cane first. He is lit from one side only; the upper half of his "
  "face stays in hard black shadow, and set into that shadow is one visible red eye with three "
  "small black comma-shaped marks around its pupil. PANEL 3 (bottom): close on the boy's face "
  "looking up — wary, guarded, not grateful. " + LIGHT_ALLEY +
  "Leave exactly two empty white speech balloons with clean black outlines, placed like this: one "
  "in the upper left corner of PANEL 1 close above the kneeling boy, and one in the upper right "
  "of PANEL 2 beside the old man's head, its tail pointing to his mouth. Both balloons are left "
  "completely blank inside — plain white, empty, unlettered. Panel 3 contains no speech balloon "
  "at all. ", R("naruto_07", "madara", "env_alley"), "low"),

 ("p16", 3,
  PAGE + BIND_N7 + BIND_MAD.format(i=2) + BIND_ENV.format(i=3) + HALF_SHADOW +
  "This page is silent — no speech balloons anywhere on it. PANEL 1 (top, wide): a high wide shot "
  "of a deserted night village street. The tall black-robed old man walks slowly ahead with his "
  "cane; the small orange boy follows a few paces behind. Both are small in a large empty frame. "
  "PANEL 2 (small, middle): tight insert on the tip of the wooden cane meeting the stone. PANEL 3 "
  "(bottom, wide): the boy glances sideways and up at the old man, who is looking straight ahead "
  "and does not look back. " + LIGHT_NIGHT_ST,
  R("naruto_07", "madara", "env_village_street"), "low"),

 ("p17", 3,
  PAGE + BIND_N7 + BIND_MAD.format(i=2) + BIND_ENV.format(i=3) + HALF_SHADOW +
  "PANEL 1 (top, wide): the open concrete walkway outside the boy's apartment door at night. The "
  "old man has stopped at the head of the outdoor stairs and turned back. PANEL 2 (middle, "
  "large): he looks down at the boy — the upper half of his face still in hard black shadow, one "
  "red eye visible in it, mouth speaking. PANEL 3 (bottom): the boy's face from above, looking "
  "up, taking the instruction in. " + LIGHT_APT_EXT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_ext"), "low"),

 ("p18", 3,
  PAGE + BIND_N7 + BIND_MAD.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (small, top): the small boy at the bottom of a tall frame on the night walkway, "
  "looking up and asking a question. PANEL 2 (the large central panel filling most of the page, "
  "and the most important image on it): the old man's face in close-up, and for the first time "
  "there is no shadow across it at all — it is evenly lit and completely visible. A gaunt, "
  "deeply lined old face, long spiked black hair framing it, and BOTH eyes clearly readable as "
  "deep red irises, each with three small black comma-shaped marks arranged around the pupil. His "
  "expression is almost gentle. PANEL 3 (thin strip, bottom): the same stretch of empty concrete "
  "walkway one moment later — the old man is simply not there any more, and the boy stands alone "
  "looking at the space where he was. " + LIGHT_APT_EXT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_ext"), "medium"),

 ("p19", 2,
  PAGE + BIND_MAD.format(i=1) + BIND_ZET.format(i=2) +
  "Somewhere else entirely. PANEL 1 (large, top two thirds): a bare rocky clearing under dead "
  "bare trees at night, almost entirely black. The tall old man in the long black robe stands "
  "with his back mostly to the camera, both hands resting on his cane. Rising up out of the flat "
  "rock at his feet, emerged only as far as its waist so that the lower half of its body is still "
  "in the ground, is the split white-and-black plant creature with the huge green flytrap collar "
  "of pointed leaves around its head. PANEL 2 (bottom third, wide): close on the creature's face "
  "— one half white, one half black, round yellow eyes, wide fixed grin, looking up out of "
  "frame at the old man. " + LIGHT_NOWHERE +
  "Leave exactly two empty white speech balloons, both of them inside PANEL 1 and none anywhere "
  "else: the first high in the upper right of panel 1 just above the plant creature's head, and "
  "the second lower down at the left of panel 1 beside the old man's shoulder, its tail pointing "
  "toward him. Both balloons are left completely blank inside — plain white, empty, unlettered. "
  "Panel 2 contains no speech balloon at all. ", R("madara", "zetsu"), "low"),
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
