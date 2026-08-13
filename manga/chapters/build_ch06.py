"""Chapter 6 — "Traitors". 20 pages (p01 doubles as the title plate).

The volume's only ensemble chapter, and the reader's only look at the classmates
before Volume 2. Six of them, so every page carries the full binding set plus an
explicit distinctness clause — this is the highest character-bleed risk in the book.

Naruto is 7-8 throughout: orange jumpsuit, goggles on the forehead.

gpt-image-2 on Replicate. Resumable — existing pages are skipped.
Run: python3 chapters/build_ch06.py   (or with page ids to rebuild individual pages)
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch06" / "raw"
LED = Ledger(HERE / "ch06" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

SILENT = "This page carries no dialogue: leave it entirely free of speech balloons. "

# ------------------------------------------------------------------ bindings
BIND_N7 = ("Image 1 is the CHARACTER REFERENCE for the blond boy: a small seven-year-old with short "
           "spiky bright-blond hair, blue eyes and three faint whisker marks on each cheek, wearing "
           "a bright orange tracksuit jumpsuit with a tall dark navy collar, a navy waistband and "
           "navy trim, a pair of goggles with a dark navy strap pushed up onto his forehead, and "
           "black open-toe shinobi sandals. Reproduce that face, hair, goggles and outfit exactly. "
           "Ignore Image 1's white background, its three-view layout and its standing pose. ")

BIND_SHIKA = ("Image {i} is the CHARACTER REFERENCE for the lazy boy: black hair pulled up into a "
              "short spiky pineapple-shaped ponytail, narrow bored half-lidded eyes, a grey "
              "short-sleeved jacket with green trim over a dark mesh shirt, and brown trousers. "
              "Reproduce that face, hair and outfit exactly, but draw him as a child of about eight "
              "— the same age and height as the other children in this scene. Ignore Image {i}'s "
              "white background, its three-view layout and its standing pose. ")

BIND_CHOJI = ("Image {i} is the CHARACTER REFERENCE for the heavyset boy: round-faced and plump, "
              "spiky reddish-brown hair, small friendly eyes, and one red spiral marking on each "
              "cheek, wearing an open green short-sleeved jacket over a plain white shirt and dark "
              "shorts. Reproduce that face, hair, cheek markings and outfit exactly, but draw him "
              "as a child of about eight — the same age as the other children in this scene. Ignore "
              "Image {i}'s white background, its three-view layout and its standing pose. ")

BIND_HINATA = ("Image {i} is the CHARACTER REFERENCE for the shy girl: short straight dark "
               "blue-black hair cut in a blunt fringe just above the eyebrows, and very pale "
               "lavender-white eyes with no visible pupils, wearing a cream hooded jacket with "
               "turned-back cuffs and dark navy trousers. Reproduce that face, hair, pale eyes and "
               "outfit exactly, but draw her as a child of about eight — the same age as the other "
               "children in this scene. Ignore Image {i}'s white background, its three-view layout "
               "and its standing pose. ")

BIND_SASUKE = ("Image {i} is the CHARACTER REFERENCE for the black-haired boy: black hair spiking "
               "upward at the back with two long bangs framing his face, dark eyes, wearing a "
               "high-collared dark navy blue short-sleeved shirt with a wide upturned collar, white "
               "arm warmers and white shorts. Reproduce that face, hair and outfit exactly, but "
               "draw him as a child of about eight — the same age as the other children in this "
               "scene. Ignore Image {i}'s white background, its three-view layout and its standing "
               "pose. ")

BIND_SAKURA = ("Image {i} is the CHARACTER REFERENCE for the pink-haired girl: chin-length pink "
               "hair, a wide forehead and green eyes, wearing a red sleeveless high-collared "
               "qipao-style dress with white trim over dark cycling shorts. Reproduce that face, "
               "hair and outfit exactly, but draw her as a child of about eight — the same age as "
               "the other children in this scene. Ignore Image {i}'s white background, its "
               "three-view layout and its standing pose. ")

BIND_INO = ("Image {i} is the CHARACTER REFERENCE for the ponytailed girl: very long pale ash-blonde "
            "hair worn in a high ponytail down her back with a long fringe falling over the right "
            "side of her face, light blue eyes, wearing a sleeveless purple crop top and matching "
            "purple skirt with her lower legs wrapped in pale bandages. Reproduce that face, hair "
            "and outfit exactly, but draw her as a child of about eight — the same age as the other "
            "children in this scene. Ignore Image {i}'s white background, its three-view layout and "
            "its standing pose. ")

BIND_IRUKA = ("Image {i} is the CHARACTER REFERENCE for the instructor: a young adult man with brown "
              "hair pulled up into a short spiky ponytail, a straight horizontal scar across the "
              "bridge of his nose, a dark navy long-sleeved shirt under a green flak vest, and a "
              "dark cloth headband whose metal plate is completely smooth and blank. Reproduce that "
              "face and outfit exactly. Ignore Image {i}'s white background, its three-view layout, "
              "its standing pose, and any markings on the metal plate — the plate is plain polished "
              "metal with nothing on it. ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the tall gaunt old man: a very old man with "
               "a long, deeply lined, pale hollow-cheeked face, dark red eyes, and long spiked "
               "coal-black hair falling well past his shoulders, wearing a plain black full-length "
               "robe with wide sleeves and dark shoes, and leaning on a plain wooden walking cane. "
               "Reproduce that face, hair, robe and cane exactly. Ignore Image {i}'s white "
               "background, its three-view layout and its standing pose. ")

BIND_ZETSU = ("Image {i} is the CREATURE REFERENCE: a humanoid plant creature split cleanly down the "
              "vertical middle, its right half chalk white and its left half pure black, with round "
              "yellow pupil-less eyes, a long black cloak, and two halves of a large open green "
              "venus-flytrap shell standing up around its head. Reproduce it exactly. Ignore Image "
              "{i}'s white background, its three-view layout and its standing pose. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore the fact that it is empty "
            "of people. ")

BIND_MOB = ("Image {i} shows the four villager archetypes. Use these faces and clothes as the basis "
            "for the adult villagers. Ignore its white background and lineup layout. ")

# The bleed guard. Six classmates on one chapter — this clause goes on every populated page.
DISTINCT = ("Every named character on this page is a separate individual and must be drawn as a "
            "clearly different person from all the others: a different face, a different hair "
            "colour and hairstyle, and different clothing. Any additional students or villagers in "
            "the background are unnamed extras who must not share any named character's hair "
            "colour, hairstyle, clothing or facial markings. ")

# ------------------------------------------------------------------ lighting
L_ACAD = ("Lighting: flat unromantic morning daylight, pale blue sky, bleached dirt ground, short "
          "hard shadows, nothing glamorous about it. ")
L_CLASS = ("Lighting: flat unromantic daylight through the tall window bank falling across the "
           "tiered wooden benches, warm dull browns, ordinary and undramatic. ")
L_STREET = ("Lighting: flat overcast colourless daylight on stone paving and wooden shopfronts, no "
            "warmth in it, shadows thin and grey. ")
L_HIDE = ("Lighting: near-black underground stone, hard cold rim light picking out edges only, one "
          "small cold colourless light source, deep black filling everything else, and no warm "
          "tones anywhere in the image. ")

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 ("p01", 1,
  "A single full-bleed illustration filling the whole page, no interior panel divisions. A wide "
  "eye-level view across the dirt yard toward the front of the wooden two-storey shinobi academy "
  "building on an ordinary morning, with the big tree and its rope swing at the right of frame. "
  "Children of about eight are streaming toward the arched entrance in twos and threes. Walking in "
  "among them, small in the frame and seen from behind, is one seven-year-old boy in a bright "
  "orange jumpsuit with goggles pushed up on his forehead. Keep the entire upper third of the image "
  "as calm uncluttered pale sky with a few flat clouds and nothing else in it, for a title to be "
  "placed later. " + BIND_N7 + UNIQUE + " " + BIND_ENV.format(i=2) + L_ACAD + SILENT,
  R("naruto_07", "env_academy_ext"), "low"),

 ("p02", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_SHIKA.format(i=2) + BIND_ENV.format(i=3) + DISTINCT +
  "PANEL 1 (wide, top): the academy classroom interior seen from the front — tiered rows of long "
  "wooden benches filling with eight-year-old children, the small blond boy in the orange jumpsuit "
  "climbing the tiers toward the back row. PANEL 2 (middle): at a back bench, the boy with the "
  "short spiky pineapple-shaped ponytail is face down asleep on his folded arms; the blond boy's "
  "hand is shoving his shoulder. PANEL 3 (bottom, wide): the ponytailed boy has lifted his head, "
  "eyes half open and thoroughly unimpressed, speaking without moving anything else; the blond boy "
  "is sitting down beside him, grinning. " + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "shikamaru", "env_classroom"), "low"),

 ("p03", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_CHOJI.format(i=2) + BIND_ENV.format(i=3) + DISTINCT +
  "PANEL 1 (top): the round heavyset boy with reddish-brown spiky hair and red spiral cheek "
  "markings sits at the next bench with a large open paper bag of crisps in his lap, eating "
  "steadily and contentedly. PANEL 2 (middle, large): he has turned and tilted the open bag toward "
  "the blond boy, offering it, entirely matter-of-fact about it. PANEL 3 (bottom): tight insert on "
  "the blond boy's hand, stopped in mid-air just above the open bag — hesitating, because this has "
  "not happened to him before. " + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "choji", "env_classroom"), "low"),

 ("p04", 2,
  PAGE + "A deliberately quiet page with only TWO large panels and generous calm empty space. "
  + BIND_N7 + UNIQUE + " " + BIND_SHIKA.format(i=2) + BIND_CHOJI.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "PANEL 1 (large, top two thirds): the three of them in a row along one back bench — on the left "
  "the round heavyset boy with reddish-brown hair and red spiral cheek markings, still eating and "
  "talking with his mouth full; in the middle the small blond boy in the orange jumpsuit; on the "
  "right the boy with the pineapple ponytail with his chin flat on his folded arms, eyes shut "
  "again. Ordinary, unremarkable, and for the blond boy completely unprecedented. PANEL 2 (bottom "
  "third): close on the blond boy's face alone. This is not the huge open-mouthed grin he performs "
  "in public — his mouth is small and closed and slightly crooked, and the feeling reaches all the "
  "way up into his eyes, which are narrowed and creased warm at the outer corners. "
  + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "shikamaru", "choji", "env_classroom"), "low"),

 ("p05", 4,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_HINATA.format(i=2) + BIND_SHIKA.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "Play this page as odd and faintly unsettling, seen entirely from the blond boy's point of view — "
  "not as romance. PANEL 1 (top, wide): across the tiered classroom, two rows down and off to one "
  "side, the shy girl with the blunt dark blue-black fringe and pale pupil-less eyes is sitting "
  "bolt upright with her hands flat in her lap, staring directly up at the blond boy. She is far "
  "too still, and she does not blink. PANEL 2 (middle left): the blond boy notices, and looks "
  "straight back at her, puzzled. PANEL 3 (middle right): her head has snapped down and away, chin "
  "tucked, face hidden behind her fringe, shoulders drawn up around her ears. PANEL 4 (bottom, "
  "wide): the blond boy has already turned away and is leaning over to the ponytailed boy beside "
  "him, thumb jerked back over his shoulder, his face flat and mildly contemptuous — no curiosity "
  "in it and no warmth either. " + L_CLASS + BALLOONS.format(k="three"),
  R("naruto_07", "hinata", "shikamaru", "env_classroom"), "low"),

 ("p06", 3,
  PAGE + BIND_SASUKE.format(i=1) + BIND_SAKURA.format(i=2) + BIND_INO.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "The blond boy does not appear anywhere on this page. PANEL 1 (top, large): the classroom door "
  "has slid open and the black-haired boy with the upward-spiking hair and the high-collared dark "
  "navy shirt is standing in it, walking in without looking at anybody, face closed and cold. PANEL "
  "2 (middle, wide): behind and around him, a whole row of eight-year-old girls has turned in their "
  "seats to watch him cross the room, faces lit up. PANEL 3 (bottom): in the front row, two of them "
  "are half out of their seats and arguing across a bench at each other — on the left the girl with "
  "chin-length pink hair and a red sleeveless dress, on the right the girl with the very long pale "
  "blonde ponytail and the purple crop top. " + L_CLASS + BALLOONS.format(k="two"),
  R("sasuke", "sakura", "ino", "env_classroom"), "low"),

 ("p07", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_SASUKE.format(i=2) + BIND_SHIKA.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "PANEL 1 (top, wide): the black-haired boy with the upward-spiking hair has taken a bench beside "
  "the tall windows and sits alone with his chin resting on his laced fingers, looking out, "
  "completely sealed off from the noisy room around him. PANEL 2 (middle): up at the back bench, "
  "the small blond boy in the orange jumpsuit and the boy with the pineapple ponytail, both looking "
  "down across the room at him. PANEL 3 (bottom, large): close on the blond boy's face, flat and "
  "unimpressed, entirely unconvinced by whatever everyone else can see. "
  + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "sasuke", "shikamaru", "env_classroom"), "low"),

 ("p08", 3,
  PAGE + BIND_ENV.format(i=1) + BIND_IRUKA.format(i=2) + BIND_MOB.format(i=3) + DISTINCT +
  "The morning the news breaks. The blond boy does not appear on this page. PANEL 1 (wide, top): an "
  "ordinary village street of wooden two-storey shopfronts at first light — and every masked and "
  "uniformed shinobi on it is running the same direction along the rooftops at full speed, a dozen "
  "small hard figures against the pale sky. PANEL 2 (middle): a knot of five or six adult villagers "
  "stopped dead in the middle of the paving, heads together, one with a hand pressed over her "
  "mouth, every face gone grey. PANEL 3 (bottom, wide): the young instructor with the scar across "
  "his nose standing alone further down the street, a split shopping bag on the stones at his feet "
  "with vegetables rolling away from it, staring off-panel and not seeing any of it. "
  + L_STREET + BALLOONS.format(k="three"),
  R("env_village_street", "iruka", "mob_archetypes"), "low"),

 ("p09", 1,
  "A single full-page illustration filling the whole page, no interior panel divisions. "
  + BIND_N7 + UNIQUE + " " + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) +
  "The aftermath, and nothing of the event itself. Looking down the length of a village street "
  "toward the sealed entrance of a clan district at the far end: a heavy wooden gateway, thick "
  "rope barriers strung across the road in front of it, tall blank white cloth screens erected "
  "right across the street behind the ropes so that absolutely nothing beyond them is visible, and "
  "four masked shinobi in grey standing at the ropes, motionless, arms at their sides. Pressed up "
  "against the ropes is a silent crowd of adult villagers, thirty or forty of them, packed shoulder "
  "to shoulder and completely still — no one is shouting. Down at the front of the crowd, small and "
  "low in the frame, half-swallowed by the adults around him, stands the seven-year-old boy in the "
  "bright orange jumpsuit with goggles on his forehead, looking up at the screens. There is no "
  "blood, no body and no violence anywhere in this image — only the barrier and the crowd. "
  + L_STREET + SILENT,
  R("naruto_07", "env_village_street", "mob_archetypes"), "medium"),

 ("p10", 3,
  PAGE + BIND_HINATA.format(i=1) + BIND_ENV.format(i=2) + BIND_MOB.format(i=3) + DISTINCT +
  "The clans shutting themselves in. The blond boy does not appear on this page. PANEL 1 (top): a "
  "pair of heavy timber compound gates being shoved closed from the inside by two adult guards in "
  "dark robes, seen from the street, the gap between them already narrow. PANEL 2 (middle): at "
  "another closing gate, an adult's hand has closed around the wrist of the small shy girl with the "
  "blunt dark blue-black fringe and pale pupil-less eyes and is drawing her back inside; she is "
  "looking back out through the last of the gap. PANEL 3 (wide, bottom): the emptied street — "
  "shutters down over every shopfront, a hanging cloth awning rolled and tied, one dropped wooden "
  "child's toy lying alone on the paving, not a single person left in frame. "
  + L_STREET + SILENT,
  R("hinata", "env_village_street", "mob_archetypes"), "low"),

 ("p11", 3,
  PAGE + BIND_SASUKE.format(i=1) + BIND_SAKURA.format(i=2) + BIND_INO.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "Days later. The blond boy does not appear on this page. PANEL 1 (wide, top): the classroom, far "
  "quieter than it should be — the black-haired boy with the upward-spiking hair sits at his bench "
  "by the window, and there is a conspicuous ring of empty bench space all the way around him "
  "although the rest of the room is full. PANEL 2 (middle, wide): the girl with the chin-length "
  "pink hair and the girl with the long pale blonde ponytail sitting in their own seats a few rows "
  "away, both looking over at him, neither of them moving and neither of them speaking. The "
  "squabbling is finished. PANEL 3 (bottom, large): close on the black-haired boy's face. The "
  "arrogance is gone and nothing has replaced it — his eyes are fixed on the bare bench in front of "
  "him and focused on nothing at all. " + L_CLASS + SILENT,
  R("sasuke", "sakura", "ino", "env_classroom"), "low"),

 ("p12", 2,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_SASUKE.format(i=2) + BIND_CHOJI.format(i=3)
  + BIND_ENV.format(i=4) + DISTINCT +
  "PANEL 1 (large, top two thirds): shot from behind the blond boy's shoulder at the back of the "
  "classroom, looking down across the tiers at the black-haired boy alone at the window bench far "
  "below. The round heavyset boy with the reddish-brown hair and red spiral cheek markings is "
  "leaning in at the blond boy's other shoulder, talking quietly. PANEL 2 (bottom third): close on "
  "the blond boy's face in three-quarter view. He is a little sorry and completely unmoved — mild, "
  "calm, and already turning his head away first. " + L_CLASS + BALLOONS.format(k="two"),
  R("naruto_07", "sasuke", "choji", "env_classroom"), "low"),

 ("p13", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the bare underground stone room — rough block walls, a cold empty hearth, a "
  "rough wooden table with two chairs, one small cold light source. The tall gaunt old man in the "
  "black robe sits at one side of the table with both hands folded over the head of his wooden "
  "cane; the small blond boy in the orange jumpsuit sits opposite him with an untouched bowl in "
  "front of him. PANEL 2 (middle): the boy has looked up from the bowl and is asking a question, "
  "face plain and direct. PANEL 3 (bottom, wide): the old man's face, half of it in total blackness "
  "and half edged in hard cold light. He is not surprised by the question in the slightest. "
  + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_hideout_kitchen"), "low"),

 ("p14", 2,
  PAGE + BIND_MADARA.format(i=1) + BIND_ENV.format(i=2) +
  "The first genuinely unpleasant thing this man does — let it land. The blond boy does not appear "
  "on this page. PANEL 1 (large, top two thirds): the tall gaunt old man across the rough table, "
  "one side of his lined face caught by the single cold light and the whole of the rest of him "
  "swallowed in blackness. He is smiling: a small, closed, slow, deeply satisfied smile, the "
  "expression of a man hearing something he has waited a long time for. PANEL 2 (bottom third): "
  "extreme close-up of his dark red eyes with the edge of that smile still in frame beneath them. "
  "Nothing in this image is warm. " + L_HIDE + BALLOONS.format(k="two"),
  R("madara", "env_hideout_kitchen"), "low"),

 ("p15", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_ENV.format(i=2) +
  "The chapter's moral turn, played completely flat — there is nothing triumphant anywhere on this "
  "page and no shock either, and that is the point. PANEL 1 (top, wide): the small blond boy across "
  "the rough wooden table in the dark stone room, taking in what he has just been told with no "
  "reaction at all — no widened eyes, no recoil, nothing. PANEL 2 (middle): close on his face as he "
  "nods, once, small, agreeing. His expression is calm and mildly approving, the face of a child "
  "agreeing that the weather is fine. PANEL 3 (bottom, wide): his hands, unhurried, picking his "
  "chopsticks back up and going on with his food. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "env_hideout_kitchen"), "low"),

 ("p16", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top, wide): in the dark stone room the tall gaunt old man has taken one hand off the "
  "head of his cane and opened it flat on the table, explaining, unhurried and precise. PANEL 3 is "
  "below; PANEL 2 sits between them as an inset. PANEL 2 (middle, a wide symbolic inset panel with "
  "a heavy black border, clearly a picture of something being described rather than the room): "
  "rendered entirely as flat black silhouettes against a cold grey ground — thirty motionless "
  "figures in high-collared robes standing in close ranks with their backs to us, facing away "
  "downhill toward the distant tiled rooftops of a sleeping village. No faces, no interior detail, "
  "no violence, only the massed shapes and the village below them. PANEL 3 (bottom, wide): the "
  "small blond boy on the other side of the table, listening, absolutely still, the single cold "
  "light catching one side of his face. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_hideout_kitchen"), "medium"),

 ("p17", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): close on the small blond boy's eyes narrowing very slightly as he puts it "
  "together — the only movement in his face. PANEL 2 (middle): the tall gaunt old man watching him "
  "work it out, head tipped a little to one side, patient. PANEL 3 (bottom, large): the boy has "
  "said it out loud, and the old man's mouth has curved into open approval. That approval is the "
  "warmest thing in the whole scene, which is exactly the problem with it. "
  + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_hideout_kitchen"), "low"),

 ("p18", 3,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_ZETSU.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top, wide): tight on the flagstone floor of the dark stone room beside a chair leg — "
  "the solid stone has bulged and rippled upward as though it had gone soft. PANEL 2 (middle, "
  "large): the head and shoulders of the plant creature have risen up out of the floor beside the "
  "table, split cleanly down the vertical middle with its right half chalk white and its left half "
  "pure black, round yellow pupil-less eyes, the two halves of the big green venus-flytrap shell "
  "standing up around its head. PANEL 3 (bottom, wide): neither the small blond boy nor the old man "
  "has so much as looked round at it. The boy goes on eating. " + L_HIDE + BALLOONS.format(k="one"),
  R("naruto_07", "zetsu", "env_hideout_kitchen"), "low"),

 ("p19", 2,
  PAGE + BIND_N7 + UNIQUE + " " + BIND_MADARA.format(i=2) + BIND_ZETSU.format(i=3)
  + BIND_ENV.format(i=4) +
  "PANEL 1 (large, top two thirds): the plant creature now stands fully upright out of the floor "
  "beside the seated old man, hands folded in front of it, the hard cold rim light running down the "
  "chalk white right half of its body while the pure black left half disappears completely into the "
  "darkness of the room. The old man has not turned his head toward it. PANEL 2 (bottom third): the "
  "small blond boy looking up at the creature from his chair, unafraid and openly curious, while "
  "the old man's lined hand gestures toward it without ceremony. " + L_HIDE
  + BALLOONS.format(k="three"),
  R("naruto_07", "madara", "zetsu", "env_hideout_kitchen"), "low"),

 ("p20", 1,
  "A single full-page illustration filling the whole page, no interior panel divisions. "
  + BIND_N7 +
  "This page deliberately contains TWO boys who are exact duplicates of one another — identical "
  "face, identical spiky blond hair, identical goggles on the forehead, identical orange jumpsuit. "
  "That duplication is intentional and must be drawn precisely. Apart from those two boys and the "
  "old man there is nobody else in the image. " + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "COMPOSITION: a low camera at the foot of a long flight of rough stone steps rising away from us "
  "through near-black underground rock toward a small distant rectangle of pale daylight at the "
  "very top. Climbing the steps about two thirds of the way up, small in the frame and seen from "
  "behind, is one boy in the orange jumpsuit walking up toward that opening. Standing in the black "
  "foreground at the bottom of the steps, close to camera, seen from behind and much larger in "
  "frame, is the second identical boy, watching him go, arms at his sides. At the left edge of "
  "frame the tall gaunt old man in the black robe leans on his cane, rendered almost entirely as a "
  "flat black silhouette with only a hard cold rim of light down one edge of him. "
  + L_HIDE + "The far rectangle of daylight is pale, cold and colourless — there is no warm tone "
  "anywhere in this image. " + BALLOONS.format(k="one"),
  R("naruto_07", "madara", "env_hideout_corridor"), "low"),
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
