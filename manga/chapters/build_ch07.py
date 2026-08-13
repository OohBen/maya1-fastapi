"""Chapter 7 — "The Price". 20 pages.

The volume's thesis chapter and the hardest to stage: the source is a lecture at a table.
Solution is a REGISTER SHIFT — the Sage myth is rendered as full-bleed plates in a
deliberately older, flatter, woodblock/scroll idiom, intercut with small panels of a
nine-year-old listening. The shift is what makes exposition readable.
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch07" / "raw"
LED = Ledger(HERE / "ch07" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")
BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# Naruto is 8-9 here. Body/hair from the age-10 sheet, but eyes are still ORDINARY BLUE
# until the awakening on p14 — the reference has them already red, so override explicitly.
BIND_N_PRE = ("Image 1 is the CHARACTER REFERENCE for the boy's build, hair and clothing: a wiry "
              "nine-year-old with blond hair to just below the ears, in a plain dark grey "
              "long-sleeved training top and black trousers. Reproduce his build, hair and outfit "
              "exactly, but his eyes must be ORDINARY BLUE — he does not have red eyes yet, so "
              "ignore the eye colour in Image 1. Ignore its white background and three-view layout. "
              + UNIQUE + " ")

BIND_N_POST = ("Image 1 is the CHARACTER REFERENCE for the boy: a wiry nine-year-old with blond "
               "hair to just below the ears, in a plain dark grey long-sleeved training top and "
               "black trousers, with RED eyes each carrying three small black comma-shaped marks "
               "around the pupil. Reproduce him exactly including the red eyes. Ignore Image 1's "
               "white background and three-view layout. " + UNIQUE + " ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the old man: very old, tall, gaunt, long "
               "wild black hair in heavy spikes, deeply lined face, floor-length plain black robes, "
               "a plain wooden walking cane. Reproduce his face, hair and robes exactly. Ignore its "
               "white background and three-view layout. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore that it is empty of people. ")

L_HIDE = "Lighting: near-black, hard cold rim light picking out edges only, no warm tones anywhere. "
L_CAMP = "Lighting: failing grey-orange dusk light, long shadows, a low cookfire the only warm source. "

# The myth plates use a deliberately DIFFERENT idiom from the rest of the book.
MYTH = ("RENDER THIS PAGE IN A DELIBERATELY DIFFERENT, OLDER VISUAL IDIOM from a normal manga page: "
        "flat flaking mineral pigments, muted ochre, indigo and dull gold on an aged parchment "
        "ground, thick uneven brush outlines, no cel shading, no modern anime rendering — it should "
        "look like an ancient painted scroll or woodblock print rather than a comic page. ")

PAGES = [
 ("p01", 3,
  PAGE + BIND_N_PRE + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): a small underground stone chamber. One entire wall is a single enormous "
  "ancient stone tablet covered edge to edge in dense carved spiral glyphs. The old man stands "
  "before it, back to us; the boy is small beside him. PANEL 2 (middle): the boy's face tipped up, "
  "looking at the carving. PANEL 3 (bottom): a tight detail of the carved glyphs, deep and worn. "
  + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_10", "madara", "env_hideout_tablets"), "medium"),

 ("p02", 1,
  "A single full-page illustration, no panel divisions. " + MYTH +
  "A colossal robed figure stands alone against a vast empty sky, seen from far below and behind — "
  "an ancient sage with a horned silhouette and a staff, immense and remote. Beneath his feet the "
  "world is small. Nine faint animal shapes circle at the edges of the composition like constellations. "
  "Ancient, mythic, unreachable.", (), "high"),

 ("p03", 2,
  PAGE + MYTH +
  "PANEL 1 (large, top): the same ancient sage, now seated, with TWO sons standing before him — one "
  "on the left with pale robes and open hands, one on the right with dark robes and shadowed eyes. "
  "The composition is perfectly symmetrical and formal, like a scroll illustration. "
  "PANEL 2 (bottom): a stark division — the left son's hands glowing with life, the right son's eyes "
  "burning. The elder brother received the eyes; the younger, the body.", (), "medium"),

 ("p04", 2,
  PAGE + MYTH +
  "PANEL 1 (top): the two brothers' descendants at war across centuries — two masses of tiny figures "
  "clashing, rendered flat and patterned like a battle scroll, no individual detail. "
  "PANEL 2 (large, bottom): a single enormous eye with a rippled concentric ring pattern, filling the "
  "panel, painted in the same ancient idiom. The eye of a god.", (), "medium"),

 ("p05", 3,
  PAGE + BIND_N_PRE + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "Back to normal manga rendering. PANEL 1 (top): the boy in the tablet chamber, still staring up, "
  "the myth over. PANEL 2 (middle): the old man's face in profile, lit hard from one side, talking "
  "about himself now. PANEL 3 (bottom): the boy's expression shifting from wonder to unease. "
  + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p06", 3,
  PAGE + BIND_MADARA.format(i=1) + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the old man's hand pulling the front of his black robe aside at the chest. "
  "PANEL 2 (middle, large): what is underneath — a pale grafted mass of foreign flesh set into his "
  "chest, with the faint suggestion of another man's closed face within it. Disturbing but not gory. "
  "PANEL 3 (bottom): the boy's face, silent, taking it in. " + L_HIDE,
  R("madara", "env_hideout_tablets", "naruto_10"), "medium"),

 ("p07", 2,
  PAGE + BIND_N_PRE + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (large, top): the old man holds out one hand toward the boy, an offer and an instruction "
  "at once. PANEL 2 (bottom): the boy looking at the offered hand, then past it — he has already "
  "understood he does not actually have a choice. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p08", 3,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy lying flat on a bare stone slab in near-darkness, shirt removed, arms at "
  "his sides. PANEL 2 (middle): an old hand pressing flat against his sternum, veins of pale light "
  "spreading out under the skin from the point of contact. PANEL 3 (bottom): the boy's back arching "
  "off the stone, mouth open, eyes screwed shut. Body horror by implication — no wounds, no blood. "
  + L_HIDE
  + "Draw one large hand-drawn manga sound effect integrated into the artwork across panel 3, a "
    "jagged crackling shape reading \"BIKI\", angled with the spasm. ",
  R("naruto_10", "env_hideout_training"), "medium"),

 ("p09", 2,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): the boy unconscious on the slab, utterly still, the light under his skin "
  "fading. PANEL 2 (bottom): total blackness with one small shape at the centre — falling. " + L_HIDE,
  R("naruto_10", "env_hideout_training"), "low"),

 ("p10", 3,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy's eyes opening — daylight, outdoors, the wrong place entirely. PANEL 2 "
  "(middle): he is on his knees in the dirt at the edge of a bandit camp: crude patched tents, a "
  "smouldering cookfire, stacked crates. PANEL 3 (bottom): he turns his head sharply — whatever "
  "brought him here is gone. He is completely alone. " + L_CAMP,
  R("naruto_10", "env_bandit_camp"), "low"),

 ("p11", 2,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "PANEL 1 (wide, top): shot from behind the boy's small shoulders — twenty-odd large filthy bandit "
  "men across the camp have all stopped what they are doing and turned to look at him. They are "
  "enormous compared to him. PANEL 2 (bottom): one of them starts walking toward him, drawing a "
  "blade, unhurried. " + L_CAMP, R("naruto_10", "env_bandit_camp"), "low"),

 ("p12", 4,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "The fight, four panels, fast and fragmentary — never a clean wide shot of the killing. PANEL 1: "
  "the boy ducking under a swinging arm. PANEL 2: a dropped blade spinning in the dirt. PANEL 3: a "
  "large hand closing on his ankle. PANEL 4 (wide, bottom): he is thrown, small body mid-air against "
  "the dusk sky. " + L_CAMP
  + "Draw hand-drawn manga sound effects integrated into the artwork: a jagged \"GAKI\" in panel 2 "
    "and a heavy \"DON\" across panel 4, angled with the motion. ",
  R("naruto_10", "env_bandit_camp"), "low"),

 ("p13", 3,
  PAGE + BIND_N_PRE + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy on his back in the dirt, badly hurt, blood at his mouth. PANEL 2 (middle): "
  "a boot descending toward his face. PANEL 3 (bottom, large): extreme close-up of his blue eye, wide "
  "— this is the moment he is about to die. " + L_CAMP, R("naruto_10", "env_bandit_camp"), "low"),

 ("p14", 1,
  "A single full-page illustration filling the entire page, no panel divisions. " + BIND_N_POST +
  "Image 2 is the EYE PROGRESSION REFERENCE — use the THIRD eye in that row: a deep red iris with "
  "exactly THREE black comma-shaped marks evenly spaced around the pupil. Reproduce that pattern "
  "precisely; ignore Image 2's white background and its other eyes. "
  "COMPOSITION: extreme close-up of the boy's face filling the page, dirt and blood on his cheek, "
  "teeth bared. Both eyes have just turned — deep red with three black comma marks each, catching "
  "the last of the dusk light. Everything else falls away into darkness. The moment the price is "
  "first paid. " + L_CAMP, R("naruto_10", "sharingan_progression"), "high"),

 ("p15", 3,
  PAGE + BIND_N_POST + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy back on his feet, red eyes, moving too fast for the men around him — shown "
  "as a blur and the reactions of the bandits, not the strikes. PANEL 2 (middle): a bandit's face "
  "registering that something has changed. PANEL 3 (bottom): the boy standing still in the middle of "
  "the camp, chest heaving. " + L_CAMP, R("naruto_10", "env_bandit_camp"), "low"),

 ("p16", 2,
  PAGE + BIND_ENV.format(i=1) +
  "Image 2 is the CREATURE REFERENCE: a humanoid plant creature split vertically, right half chalk "
  "white and left half pure black, round yellow pupil-less eyes, long black cloak, green flytrap "
  "shell around its head. Reproduce exactly; ignore its white background and layout. "
  "PANEL 1 (large, top): the creature rises silently out of the ground at the edge of the camp. "
  "PANEL 2 (bottom): the camp afterwards, seen in wide shot at dusk — scattered dropped weapons, an "
  "overturned pot, the fire still smoking. Bodies implied by shapes at the frame's edge, never shown "
  "clearly. " + L_CAMP, R("env_bandit_camp", "zetsu"), "medium"),

 ("p17", 2,
  PAGE + BIND_N_POST + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): the boy on his knees in the middle of the emptied camp, red eyes open, "
  "staring at nothing. PANEL 2 (bottom): his own hands held out in front of him, shaking, dark with "
  "blood that is not his. " + L_CAMP, R("naruto_10", "env_bandit_camp"), "medium"),

 ("p18", 3,
  PAGE + BIND_N_POST + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the underground training cavern. The boy kneels on the stone floor, crying, red "
  "eyes streaming. PANEL 2 (middle): the old man's wooden cane comes down hard across his back. "
  "PANEL 3 (bottom): the boy's face, tears stopping — not from comfort but from being taught that "
  "grief is a weakness. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_10", "madara", "env_hideout_training"), "low"),

 ("p19", 2,
  PAGE + BIND_N_POST + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the old man walking away into the dark, cane tapping, not looking back. PANEL 2 "
  "(large, bottom): the boy alone on the stone floor, red eyes dry now, looking at his own open "
  "palms. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_10", "madara", "env_hideout_training"), "low"),

 ("p20", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N_POST + BIND_ENV.format(i=2) +
  "Final page. An enormous underground cavern, almost entirely black. The boy is a very small figure "
  "at the centre of a vast empty stone floor, sitting with his knees drawn up, red eyes the only "
  "points of colour in the whole frame. Overwhelming scale, overwhelming emptiness. Quiet, not "
  "dramatic. Leave clean dark space in the lower third for a caption. " + L_HIDE
  + BALLOONS.format(k="one"), R("naruto_10", "env_hideout_training"), "medium"),
]


def build_one(spec):
    pid, panels, desc, refs, quality = spec
    dest = OUT / f"{pid}.png"
    if dest.exists():
        return f"[skip] {pid}"
    prompt = desc + " " + (STYLE + " " if "OLDER VISUAL IDIOM" not in desc else "") + NO_TEXT
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
