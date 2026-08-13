"""Chapter 9 — "The Greatest Sin". 26 pages (extra-length finale).

The volume's payoff: patricide, the Mangekyo, and the reveal.
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch09" / "raw"
LED = Ledger(HERE / "ch09" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")
BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# Naruto is 13 throughout. Age-13 "reveal" design.
BIND_N13 = ("Image 1 is the CHARACTER REFERENCE for the boy: a lean thirteen-year-old with blond "
            "hair to his shoulders, two heavy bangs with the RIGHT bang hanging low enough to cover "
            "his right eye, blue eyes, whisker marks almost faded, a completely blank expression, "
            "wearing a black long-sleeved shirt with a large red spiral covering the chest, black "
            "trousers, dark sandals, and black fingerless gloves with a small red spiral on the back "
            "of each hand. Reproduce that face, hair and outfit exactly. Ignore Image 1's white "
            "background, its three-view layout and its standing pose. " + UNIQUE + " ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the old man: very old, tall, gaunt, long "
               "wild black hair in heavy spikes past his shoulders, deeply lined face, floor-length "
               "plain black robes. Reproduce his face and robes exactly. Ignore its white background "
               "and three-view layout. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore that it is empty of people. ")

L_APT = "Lighting: night interior, almost entirely dark, one weak cold light source, deep shadow. "
L_HIDE = ("Lighting: near-black, hard cold rim light picking out edges only, no warm tones anywhere. ")
L_DAWN = "Lighting: cold colourless dawn, flat grey light, no warmth. "
L_CLASS = "Lighting: flat unromantic daylight through tall windows. "

PAGES = [
 ("p01", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N13 + BIND_ENV.format(i=2) +
  "A dark cramped one-room apartment at night. The thirteen-year-old boy is asleep on a narrow bed, "
  "on his back, one arm flung out, utterly unguarded. The room is silent and still. Camera is high "
  "and slightly distant, looking down — the composition should feel like someone is watching him. "
  + L_APT, R("naruto_13", "env_apartment_int"), "medium"),

 ("p02", 3,
  PAGE + BIND_ENV.format(i=1) +
  "PANEL 1 (wide, top): the apartment door standing very slightly open, a sliver of blackness. "
  "PANEL 2 (middle): a floorboard, and the edge of a bare foot in shadow at the frame's edge. "
  "PANEL 3 (wide, bottom): a tall figure in floor-length black robes standing at the foot of the bed, "
  "rendered as a pure black silhouette with no interior detail whatsoever, face unreadable. "
  + L_APT, R("env_apartment_int"), "low"),

 ("p03", 3,
  PAGE + BIND_N13 +
  "PANEL 1 (top): the black-robed silhouette leaning down over the sleeping boy. PANEL 2 (middle): "
  "one hand clamps hard over the boy's eyes, blocking his sight completely; the other closes around "
  "his throat. PANEL 3 (bottom): the boy's body jolts awake, back arching. The attacker stays a "
  "featureless black silhouette. " + L_APT, R("naruto_13", "env_apartment_int"), "low"),

 ("p04", 3,
  PAGE + BIND_N13 +
  "PANEL 1 (top): extreme close-up — the boy's mouth open, no sound coming out, a hand across the "
  "upper half of his face. PANEL 2 (middle): his legs kicking against the bedding. PANEL 3 (bottom): "
  "his hands clawing uselessly at the wrist at his throat. The attacker remains a black silhouette. "
  + L_APT, R("naruto_13", "env_apartment_int"), "low"),

 ("p05", 2,
  PAGE + BIND_N13 +
  "PANEL 1 (large, top): the boy's right hand stops clawing and slides sideways, groping underneath "
  "the pillow. PANEL 2 (bottom): his fingers close around the handle of a small straight blade "
  "hidden there. " + L_APT, R("naruto_13", "env_apartment_int"), "low"),

 ("p06", 2,
  PAGE + BIND_N13 +
  "PANEL 1 (large, top): a fast upward stabbing motion in near-darkness — a blur of movement, motion "
  "lines, the blade catching one point of light. Impact implied, not graphic. PANEL 2 (bottom): the "
  "hand over his eyes goes slack and begins to slide away. " + L_APT
  + "Draw one large hand-drawn manga sound effect integrated into the artwork in panel 1, a sharp "
    "jagged shape reading \"ZAKU\", angled with the motion of the strike. ",
  R("naruto_13", "env_apartment_int"), "low"),

 ("p07", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N13 + BIND_MADARA.format(i=2) +
  "The boy is half sitting up in the dark bedroom, eyes now open and enormous, staring down in front "
  "of him. Kneeling and slumping away from him is the very old man in black robes, one hand still "
  "half-raised, a small blade buried in the side of his neck. Blood is dark and minimal. The old "
  "man's face is fully lit for the first time — and he is SMILING, gently, with satisfaction. The "
  "boy's expression is pure uncomprehending horror. " + L_APT,
  R("naruto_13", "madara", "env_apartment_int"), "medium"),

 ("p08", 3,
  PAGE + BIND_N13 + BIND_MADARA.format(i=2) +
  "PANEL 1 (top): the old man on his back on the floorboards, still smiling up at the boy. PANEL 2 "
  "(middle): the boy on his knees beside him, hands hovering, not knowing where to touch. PANEL 3 "
  "(bottom): extreme close-up of the old man's eyes closing. " + L_APT
  + BALLOONS.format(k="two"), R("naruto_13", "madara", "env_apartment_int"), "low"),

 ("p09", 2,
  PAGE + BIND_N13 +
  "PANEL 1 (large, top): the boy kneeling over the body, mouth open, head tipped back — a scream "
  "with no sound drawn. PANEL 2 (bottom): his hands, shaking violently, covered in dark blood. "
  + L_APT + BALLOONS.format(k="two"), R("naruto_13", "env_apartment_int"), "low"),

 ("p10", 1,
  "A single full-page illustration filling the entire page, no panel divisions. " + BIND_N13 +
  "Image 2 is the EYE DESIGN REFERENCE — the boy's eye must match it exactly: a deep blood-red iris "
  "with a small solid black ring at the centre and exactly SIX straight black blades radiating from "
  "that ring out to the rim of the iris. Reproduce that pattern precisely; ignore Image 2's white "
  "background. "
  "COMPOSITION: an extreme close-up of the boy's face filling the whole page, tears on his cheeks, "
  "mouth open. His visible left eye has just transformed — it is the red six-bladed eye from Image "
  "2, glowing faintly, lighting his face from within. The other eye is hidden behind his hanging "
  "bang. Everything around him falls into blackness. This is the most important image in the "
  "chapter. " + L_APT, R("naruto_13", "mangekyo_design"), "high"),

 ("p11", 1,
  "A single full-page illustration, no panel divisions. " +
  "Image 1 is the CREATURE REFERENCE: a humanoid plant creature split vertically down the middle, "
  "the right half chalk white and the left half pure black, with round yellow pupil-less eyes, a "
  "long black cloak, and two halves of a large open green venus-flytrap shell around its head. "
  "Reproduce it exactly; ignore its white background and three-view layout. "
  "COMPOSITION: seen from behind and below, the creature walks away down a vast black underground "
  "stone corridor carrying two limp bodies over its shoulders — a boy over one, an old man in black "
  "robes over the other. Enormous scale, tiny figure, overwhelming darkness. " + L_HIDE,
  R("zetsu", "env_hideout_corridor"), "medium"),

 ("p12", 3,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy lying on a bare stone floor in near-darkness, waking. PANEL 2 (middle): "
  "he sits up sharply, one hand going to his own face, to his eye. PANEL 3 (bottom): his eyes — one "
  "hidden by his bang, the visible one back to ordinary blue. Bewildered. " + L_HIDE,
  R("naruto_13", "env_hideout_corridor"), "low"),

 ("p13", 3,
  PAGE + BIND_N13 +
  "Image 2 is the CREATURE REFERENCE: a humanoid plant creature split vertically, right half chalk "
  "white and left half pure black, round yellow pupil-less eyes, long black cloak, green flytrap "
  "shell around its head. Reproduce exactly; ignore its white background and layout. "
  "PANEL 1 (top): the creature stands over the seated boy in the dark stone chamber. PANEL 2 "
  "(middle): the boy staring up at it, wrecked. PANEL 3 (bottom): the creature's yellow eyes, "
  "expressionless. " + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_13", "zetsu", "env_hideout_corridor"), "low"),

 ("p14", 3,
  PAGE + BIND_N13 +
  "Image 2 is the plant creature reference (split white/black body, yellow eyes, black cloak) — "
  "reproduce exactly, ignore its white background. "
  "PANEL 1 (top): close on the boy's face as understanding arrives — it was arranged. PANEL 2 "
  "(middle): the creature turning away, uninterested. PANEL 3 (bottom, large): the boy alone in the "
  "dark, sitting very still, arms limp. " + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_13", "zetsu", "env_hideout_corridor"), "low"),

 ("p15", 2,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): a bare windswept hillside at dawn. The boy stands alone beside a fresh mound "
  "of dark earth with one plain unmarked stone at its head, seen from a great distance — he is small "
  "in a vast empty landscape. PANEL 2 (bottom): his face in close-up. Completely dry. He is not "
  "crying and will not. " + L_DAWN, R("naruto_13", "env_burial"), "medium"),

 ("p16", 2,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (top): his hand pressing flat against the grave stone. PANEL 2 (large, bottom): he turns "
  "and walks away from the grave toward the camera, the mound behind him, expression closed and "
  "final. " + L_DAWN, R("naruto_13", "env_burial"), "low"),

 ("p17", 1,
  "A single full-width illustration filling the page, no panel divisions. " + BIND_ENV.format(i=1) +
  "The exterior of the ninja academy building in flat daylight, seen from the empty front courtyard. "
  "Ordinary, unremarkable, indifferent. No people. Keep the lower third relatively plain for a "
  "caption to be placed later. " + L_CLASS, R("env_academy_ext"), "low"),

 ("p18", 2,
  PAGE + BIND_ENV.format(i=1) +
  "PANEL 1 (wide, top): the interior of a packed academy classroom — tiered wooden desks full of "
  "twelve and thirteen-year-old students chattering, ordinary and loud. PANEL 2 (wide, bottom): the "
  "classroom door beginning to slide open, and every head in the front rows starting to turn toward "
  "it. " + L_CLASS, R("env_classroom"), "low"),

 ("p19", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N13 + BIND_ENV.format(i=2) +
  "The thirteen-year-old boy stands alone in the open classroom doorway, backlit from the corridor "
  "so his black clothes read almost as a silhouette with the large red spiral on his chest catching "
  "the light. Full figure, dead centre, absolutely still, expression completely blank. He is not "
  "looking at anyone. The classroom around him has gone silent — a sea of staring faces at the edges "
  "of frame. His hair is clearly SHOULDER LENGTH with the right bang hanging over his right eye. "
  "The other students are academy trainees in practical dark ninja clothing, seated at tiered "
  "wooden desks. " + L_CLASS, R("naruto_13", "env_classroom"), "medium"),

 ("p20", 3,
  PAGE + BIND_ENV.format(i=1) +
  "Reaction shots, three panels, no protagonist visible. PANEL 1: a black-haired boy with an upward-"
  "spiking hairstyle and a high-collared dark navy shirt, staring, jaw tight. PANEL 2: a pink-haired "
  "girl in a red dress, mouth open. PANEL 3: a bored-looking boy with a short spiky ponytail, sitting "
  "up straight for the first time in his life. " + L_CLASS,
  R("env_classroom", "sasuke", "sakura", "shikamaru"), "low"),

 ("p21", 3,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy walking down the aisle between the desks, not looking left or right. "
  "PANEL 2 (middle): students leaning back slightly as he passes. PANEL 3 (bottom): he sits, alone, "
  "and looks out of the window. " + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_13", "env_classroom"), "low"),

 ("p22", 2,
  PAGE + BIND_N13 +
  "Image 2 is the reference for the black-haired boy: upward-spiking black hair with two long bangs "
  "framing his face, dark eyes, a high-collared dark navy blue shirt. Reproduce exactly; ignore its "
  "white background and layout. "
  "PANEL 1 (top): the black-haired boy has come to stand at the blond boy's desk, demanding, angry. "
  "PANEL 2 (large, bottom): the blond boy does not even turn his head to look at him. " + L_CLASS
  + BALLOONS.format(k="two"), R("naruto_13", "sasuke", "env_classroom"), "low"),

 ("p23", 2,
  PAGE + BIND_N13 +
  "PANEL 1 (top): the blond boy finally turns his head, slowly. PANEL 2 (large, bottom): an extreme "
  "close-up of his face in three-quarter view — the visible eye cold and entirely empty, the right "
  "bang hanging over the other. This is the chapter's line landing. " + L_CLASS
  + BALLOONS.format(k="two"), R("naruto_13", "env_classroom"), "medium"),

 ("p24", 3,
  PAGE + BIND_ENV.format(i=1) +
  "PANEL 1 (top): the black-haired boy standing frozen beside the desk, thrown. PANEL 2 (middle): "
  "the silent classroom, every student staring. PANEL 3 (bottom): a hand on the classroom doorframe "
  "— an adult has been standing there listening. Only the hand and sleeve are visible. " + L_CLASS,
  R("env_classroom", "sasuke"), "low"),

 ("p25", 2,
  PAGE + "Image 1 is the CHARACTER REFERENCE for the man: tall and lean, spiky silver-grey hair swept "
  "to one side, a dark cloth mask covering his face below the nose, and a slanted forehead protector "
  "covering his left eye so only his right eye is visible, dark navy uniform under a green flak vest. "
  "Reproduce exactly; ignore its white background and three-view layout. "
  "PANEL 1 (top): the silver-haired masked man leaning in the classroom doorway, having watched the "
  "whole exchange. PANEL 2 (large, bottom): extreme close-up of his single visible eye, narrowing. "
  + L_CLASS, R("kakashi", "env_classroom"), "medium"),

 ("p26", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N13 +
  "A wide high shot of the classroom from behind and above the blond boy's shoulder. He sits alone "
  "at his desk at the back, small in the frame, looking out of the window at nothing. Every other "
  "student in the room is turned toward him, and none of them are near him. An enormous amount of "
  "empty space around him. Final page of the volume — quiet, not dramatic. " + L_CLASS,
  R("naruto_13", "env_classroom"), "medium"),
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
