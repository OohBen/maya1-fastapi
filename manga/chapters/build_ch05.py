"""Chapter 5 — "Grandfather". 20 story pages.

Two halves that must read as two different books.
  p01-p13  GRIEF. The apartment, then the monument at night. Minato named, the rage that
           pulls Kyuubi chakra out of him, the resemblance, "your grandfather", the tears.
  p14      THE CUT. A full-width black panel. Nothing survives it.
  p15-p20  A MACHINE STARTING UP. The hideout: near-black, hard cold rim light, zero warm
           tone anywhere. "Your childhood is over." Weights, laps, collapse, the grin.

First appearance of Madara's hideout — the lighting rule established here is never broken
again: near-black, hard cold rim light on edges only, no warm colour in the frame at all.
It is the exact visual opposite of Ichiraku in chapter 4.

gpt-image-2 on Replicate. References are free there, so every page carries its full
binding set. Resumable — existing pages are skipped. Run: python3 chapters/build_ch05.py
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch05" / "raw"
LED = Ledger(HERE / "ch05" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# ----------------------------------------------------------------- bindings
# Naruto at seven. Same design as chapters 2-4.
N7_DESIGN = ("Image 1 is the CHARACTER REFERENCE for the boy: a small skinny seven-year-old with "
             "short spiky bright blond hair, blue eyes and three faint whisker marks on each cheek, "
             "wearing a bright orange tracksuit jumpsuit with a dark navy collar and a dark navy "
             "waistband, a pair of dark round-lensed goggles on a navy strap worn up on his "
             "forehead, and black open-toe shinobi sandals. Reproduce that face, hair, goggles and "
             "outfit exactly. Ignore Image 1's white background, its three-view layout, its "
             "standing pose and its fixed grin — his expression on this page is whatever the panel "
             "describes. ")

BIND_N7 = N7_DESIGN + UNIQUE + " "

# On the pages where his father appears the resemblance IS the page, so the uniqueness
# clause is replaced rather than dropped — it would otherwise force the two apart.
BIND_N7_KIN = (N7_DESIGN + "On this page one other person is deliberately allowed to resemble him: "
               "the tall blond man described below is his father and the likeness between their "
               "faces and hair is the entire point of the page. Every other person present, if any, "
               "must look completely different from both of them. ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the old man: an elderly man with a long "
               "heavy mane of spiked black hair falling well past his shoulders, a gaunt "
               "deeply-lined pale face, dark red irises, a plain floor-length black robe with wide "
               "sleeves, black shoes and a plain wooden walking cane. Reproduce that face, hair, "
               "robe and cane exactly. Ignore Image {i}'s white background, its three-view layout "
               "and its standing pose. ")

BIND_PARENTS = ("Image {i} is a TWO-PERSON CHARACTER REFERENCE SHEET showing the boy's dead "
                "parents side by side. The figure on the LEFT of that sheet is his FATHER: a young "
                "man with bright spiky blond hair and blue eyes, a headband across his brow, and a "
                "long white sleeveless coat worn open over dark navy clothing, the hem of the coat "
                "carrying a band of red flame shapes. The figure on the RIGHT of that sheet is his "
                "MOTHER: a young woman with very long straight dark red hair falling past her "
                "waist, blue eyes, and a long dark green pinafore dress over a pale cream "
                "short-sleeved blouse. Reproduce both faces, hair and outfits exactly. Ignore "
                "Image {i}'s white background, its lineup layout and its neutral standing poses. ")

BIND_ZETSU = ("Image {i} is the CHARACTER REFERENCE for the plant creature: a tall smooth humanoid "
              "figure split perfectly down the vertical midline, one half chalk white and the "
              "other half pure matte black, with round flat yellow pupil-less eyes and a wide "
              "fixed grin of small square teeth, wearing a long plain black cloak, and framed by a "
              "large open shell of green leaves standing up around its head like a collar. "
              "Reproduce it exactly. Ignore Image {i}'s white background and its three-view "
              "layout. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, props, colour palette "
            "and lighting exactly. Do not copy its camera angle, and ignore the fact that it is "
            "empty of people. ")

BIND_MON = ("Image {i} is the LOCATION REFERENCE for the Hokage Monument — reuse its cliff face, "
            "its carved-stone rendering, its stone walkway with the low parapet, and the tiled "
            "village roofs spread out far below. Do not copy its camera angle, and ignore the fact "
            "that it is empty of people. Image {i} shows only the first three carved heads; this "
            "page also includes a FOURTH carved stone head further along the same cliff — a much "
            "younger man's face with a broad spiked fringe of stone hair falling either side of it "
            "and a plain band carved across the brow, obviously the newest carving of the row. ")

BIND_CORR = ("Image {i} is the LOCATION REFERENCE for the underground corridor — reuse its rough "
             "hewn black rock walls, its cracked pale flagstone floor, its enormous scale and its "
             "near-black palette exactly. Do not copy its camera angle, and ignore the fact that "
             "it is empty of people. ")

BIND_TRAIN = ("Image {i} is the LOCATION REFERENCE for the underground training cavern — reuse its "
              "vast black rock vault, its pale sand floor, its scattered upright wooden training "
              "posts, its low grey boulders and its single narrow shaft of cold white light "
              "falling from above. Do not copy its camera angle, and ignore the fact that it is "
              "empty of people. ")

# ----------------------------------------------------------------- lighting
L_APT = ("Lighting: one bare bulb hanging low over the table — a small hard pool of dim "
         "yellow-white light with hard-edged shadows, and cold blue-grey darkness everywhere "
         "beyond it. The room is cold and the light is not enough. ")
L_APT_RED = ("Lighting: the bare bulb over the table is overwhelmed. The dominant light source is "
             "the boy himself — a hard red-orange glow coming off his own skin, throwing harsh "
             "red-edged shadows outward onto the walls and ceiling, everything beyond him crushed "
             "to blue-black. ")
L_MON = ("Lighting: night on the cliff top. Cold blue-white moonlight from high and behind, the "
         "carved stone reading as flat pale blue-grey with hard-edged black shadow in every cut of "
         "it, the sky deep blue-black. Nothing warm touches the boy anywhere in this scene. ")
L_HIDE = ("Lighting: the underground hideout — near-black. Hard cold blue-white rim light picking "
          "out edges and contours only, everything else falling to flat black. There are no warm "
          "tones anywhere in the frame: no orange, no yellow, no firelight, no candle. Even the "
          "boy's orange jumpsuit reads as a dull desaturated brown-grey down here. ")

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 # ======================= FIRST HALF — GRIEF ==========================
 # ---- beat 1: the name -----------------------------------------------
 ("p01", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The scene continues from the previous chapter — the same night, the same table, the meal gone "
  "cold. PANEL 1 (wide, top): a flat side-on two-shot of the shabby one-room apartment, the old man "
  "in black on one stool and the small blond boy on the other, the small wooden table between them "
  "and the bare bulb hanging above it. The old man is speaking, both hands folded on the head of "
  "his cane, entirely calm. The boy has stopped eating, chopsticks still half-raised. PANEL 2 "
  "(middle): a close shot of the old man's face, lined and unhurried, dark red eyes level. He is "
  "delivering this the way a man reads out a weather report. PANEL 3 (wide, bottom): the boy's face "
  "straight on and close, lit hard from above by the bulb. His expression has not changed yet at "
  "all — the words have arrived but they have not opened. " + L_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p02", 2,
  PAGE + BIND_N7_KIN + BIND_PARENTS.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (large, the top two thirds): a symbolic memory plate with no room and no furniture in it "
  "at all — a flat empty black field, and standing in it, drawn in cold pale blue-grey as an image "
  "remembered rather than seen, the young blond man in the white flame-hemmed coat and the young "
  "red-haired woman in the dark green dress, side by side, calm, looking straight out at the "
  "reader. There is nothing else whatsoever in this panel: no room, no furniture, no other figure. "
  "PANEL 2 (a narrow strip across the bottom): back in the apartment, a tight shot of the tabletop "
  "— the boy's chopsticks lying where they have been put down, and both his small hands flat on the "
  "wood either side of the cold bowl. " + L_APT + BALLOONS.format(k="one"),
  R("naruto_07", "minato_kushina", "env_apartment_int"), "low"),

 # ---- beat 2: the rage ------------------------------------------------
 ("p03", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The page where it opens. PANEL 1 (top, small): an extreme close-up of the boy's eyes only — the "
  "pupils shrinking to points. PANEL 2 (middle): he is on his feet, the stool going over behind "
  "him, both fists on the tabletop, shouting down at the old man, his whole small body shaking. The "
  "bowl has tipped. PANEL 3 (wide, bottom): reverse angle past the boy's shoulder — the old man has "
  "not moved a muscle and has not raised his voice, hands still folded on the cane, watching the "
  "boy the way a man watches a kettle he put on himself. " + L_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p04", 1,
  "A single full-page illustration filling the entire page, no panel divisions and no gutters. "
  + BIND_N7 + BIND_ENV.format(i=2) +
  "The rage pulls something out of him that he does not know he has. The seven-year-old boy stands "
  "in the middle of the dark one-room apartment, seen from slightly below, head down and fists "
  "clenched at his sides, screaming. Thick white STEAM is boiling off his bare skin — off his face, "
  "his neck, the backs of his hands — in visible curling plumes. A thin skin of angry red-orange "
  "energy clings to his outline and frays outward at the edges of his body into ragged flame-like "
  "wisps, brightest at his shoulders and knuckles. His eyes have gone flat red with a hard vertical "
  "slit pupil and his whisker marks have thickened into heavy dark bars. The bare bulb above him is "
  "swinging and the floorboards under his feet are splitting outward in a ring. This is the single "
  "most violent image in the chapter. " + L_APT_RED +
  "Draw one huge hand-drawn manga sound effect integrated into the artwork behind him, a jagged "
  "shape reading \"GOOO\", drawn as part of the art and distorted outward with the blast. ",
  R("naruto_07", "env_apartment_int"), "medium"),

 ("p05", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The moment after the surge. PANEL 1 (wide, top): the room seen wide — the boy down on his hands "
  "and knees on the split floorboards, hair hanging, thin wisps of steam still rising off his back "
  "and shoulders, the red gone. The overturned stool, the spilled bowl, the bulb still swinging on "
  "its flex. The old man is still sitting exactly where he was. PANEL 2 (middle, small): a tight "
  "insert of the old man's face — and for the first time he is faintly, unmistakably pleased. Not "
  "smiling; interested. PANEL 3 (bottom): the boy's face close, tipped down at the floor, wrung "
  "out, breathing hard, hair stuck to his forehead with sweat. " + L_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 # ---- beat 3: the resemblance -----------------------------------------
 ("p06", 3,
  PAGE + BIND_N7_KIN + BIND_PARENTS.format(i=2) + BIND_MADARA.format(i=3) + BIND_ENV.format(i=4) +
  "The blond man is dead and is never physically present in this apartment. He appears on this page "
  "only as a reflection inside the window glass in panel 2, and nowhere else. The only two people "
  "actually standing in the room on this page are the small boy and the old man in black robes. "
  "PANEL 1 (top): a close shot of the boy standing, half turned away, and the dark window of the "
  "apartment beside him with his own reflection in the black glass — small, blond, spiky-haired. "
  "PANEL 2 (middle, the same framing repeated exactly): the identical shot of the same window, but "
  "the reflection inside the glass is now the grown blond man in the white flame-hemmed coat, the "
  "same hair, the same face aged up, looking back out of the glass. The boy himself is unchanged in "
  "the foreground and there is still nobody beside him. The two panels must line up so the swapped "
  "reflection is the only difference between them. PANEL 3 (wide, bottom): a two-shot of the boy "
  "and the OLD MAN IN BLACK ROBES only — the old man has reached out with one long bony lined hand "
  "and tilted the boy's chin up to look at his face, studying it, the way a man compares two "
  "things. Nobody else is in this panel. " + L_APT + BALLOONS.format(k="two"),
  R("naruto_07", "minato_kushina", "madara", "env_apartment_int"), "low"),

 ("p07", 2,
  PAGE + BIND_N7_KIN + BIND_PARENTS.format(i=2) +
  "PANEL 1 (large, top): the boy has both hands clamped over his own face, fingers dug in hard at "
  "his hairline, head down, shoulders up around his ears — a child trying to take his own face off. "
  "Everything around him has dropped away into flat black; only he is lit. PANEL 2 (bottom, wide): "
  "a symbolic split panel with no room in it at all — a single face fills the frame, divided down "
  "the middle by a hard vertical line: the left half is the seven-year-old boy's face, the right "
  "half is the grown blond man's face from the reference sheet, the hairlines and the eyes lining "
  "up exactly across the join. Flat black behind it, nothing else in the panel. "
  + L_APT + BALLOONS.format(k="two"),
  R("naruto_07", "minato_kushina"), "low"),

 # ---- beat 4: the monument at night ------------------------------------
 ("p08", 2,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "PANEL 1 (large, the top two thirds): a very wide establishing shot of the cliff-top monument at "
  "night, seen from far off along the walkway — the row of enormous carved stone heads in cold "
  "moonlight, the village asleep and dark far below and beyond. One tiny orange figure is standing "
  "on the walkway at the base of the FOURTH carved head, so small he is almost lost in the frame. "
  "PANEL 2 (a narrow strip across the bottom): a tight low shot of his black sandals stopped on the "
  "cold flagstones, one lace of the walkway parapet's shadow across them. " + L_MON,
  R("naruto_07", "env_monument"), "low"),

 ("p09", 2,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "Image 3 is a two-person reference sheet; use ONLY the man on its left — a young man with bright "
  "spiky blond hair swept back in a broad fringe with two long jaw-length bangs framing his face, a "
  "straight nose and calm narrow eyes, and a plain band across his brow. He is the man the FOURTH "
  "carved head on this cliff is a portrait of. Carve that exact face and that exact spiked fringe "
  "into the rock: the stone hair must read as a broad upswept spiked mane with two long points "
  "hanging down either side of the face, not as long straight flowing hair. Ignore Image 3's "
  "colours, its clothing, its white background and the woman standing beside him — he appears on "
  "this page only as grey carved stone. "
  "PANEL 1 (large, top): a steep low angle from the walkway looking up at that FOURTH carved stone "
  "head — the young man's serene face in pale moonlit stone, the broad spiked stone fringe either "
  "side of it, the plain band across the brow. It is enormous, calm and completely indifferent, and "
  "it fills the panel. He used to sit up there. PANEL 2 (bottom): the boy from behind and below, "
  "tiny at the base of that same head, head tipped back to stare up at it, both fists closed at his "
  "sides. He is not crying yet. " + L_MON + BALLOONS.format(k="one"),
  R("naruto_07", "env_monument", "minato_kushina"), "low"),

 # ---- beat 5: your grandfather -----------------------------------------
 ("p10", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_MON.format(i=3) +
  "The line the whole chapter turns on. PANEL 1 (wide, top): the boy in the foreground with his back "
  "to us at the base of the great carved head, and far behind him along the moonlit walkway the old "
  "man in black robes has appeared, leaning on his cane, a thin dark upright shape against the "
  "night sky. He has come a long way on a bad leg. PANEL 2 (middle): the old man closer now, "
  "stopped a few paces short, speaking — his face three-quarter, lit hard down one side by the "
  "moon, the other side in flat black. This is not cruelty and it is not comfort; it is a fact he "
  "has carried for seven years. PANEL 3 (large, bottom): the boy has turned around. His face fills "
  "the panel, tipped up, mouth slightly open, eyes enormous — the exact instant a word he has never "
  "had before is handed to him. " + L_MON + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_monument"), "medium"),

 ("p11", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_MON.format(i=3) +
  "PANEL 1 (top): the boy takes a step toward the old man and stops, one hand half out, asking — "
  "his face is not grateful, it is accusing. PANEL 2 (middle): a close shot of the old man, eyes "
  "lowered for the first time in the chapter, one hand tightening on the head of the cane. PANEL 3 "
  "(wide, bottom): a wide two-shot along the empty moonlit walkway, the pair of them small and a "
  "clear gap of cold flagstone between them, the vast carved heads above and the sleeping village "
  "below. " + L_MON + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_monument"), "low"),

 # ---- beat 6: he cries -------------------------------------------------
 ("p12", 2,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "He promised himself he would never do this again. He does it once. PANEL 1 (a narrow strip "
  "across the top): an extreme close-up of his eyes only, rimmed red, brimming, the surface tension "
  "about to go. PANEL 2 (enormous, the whole rest of the page): his face straight on and very "
  "close, filling the frame, lit hard and cold blue-white from one side. His mouth is pulled "
  "sideways and his eyes are screwed almost shut and there are real tears running clean down both "
  "cheeks and off his jaw. This is a seven-year-old crying properly, ugly and silent, with no "
  "dignity in it at all — draw it plainly and without any prettiness. The monument and the sky have "
  "gone soft and dark behind him and only his face is lit. " + L_MON + BALLOONS.format(k="one"),
  R("naruto_07", "env_monument"), "medium"),

 ("p13", 2,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_MON.format(i=3) +
  "No words on this page. PANEL 1 (top): a tight shot from behind the boy's shoulder — the old "
  "man's long bony hand comes down and rests flat on the top of the boy's spiky blond head. Just "
  "that. PANEL 2 (large, bottom): pull all the way back — a very wide shot of the cliff top from a "
  "great distance, the two of them a single small dark clump on the walkway at the foot of the "
  "enormous carved heads, the moon high, the village black and asleep below. Enormous empty space "
  "around them. " + L_MON,
  R("naruto_07", "madara", "env_monument"), "low"),

 # ======================= THE CUT =====================================
 ("p14", 2,
  PAGE +
  "This page is a hard cut between two halves of the chapter and it must feel like a door closing. "
  + BIND_N7 + BIND_MADARA.format(i=2) + BIND_CORR.format(i=3) +
  "PANEL 1 (a full-width band across the top half of the page, edge to edge): a solid flat pure "
  "black rectangle. There is nothing inside it at all — no figure, no object, no texture, no "
  "detail, no light. Pure black. PANEL 2 (the bottom half, wide): a long flight of rough stone "
  "steps cut down into black rock, seen from above and behind, descending away from the camera into "
  "total darkness. Two small figures are already well down the steps with their backs to us — the "
  "tall old man in black robes with his cane, and the small boy following him. They are lit only by "
  "a hard cold edge of blue-white on their shoulders. Nothing warm is in this panel. " + L_HIDE,
  R("naruto_07", "madara", "env_hideout_corridor"), "low"),

 # ======================= SECOND HALF — THE MACHINE ===================
 ("p15", 1,
  "A single full-page illustration, no panel divisions. " + BIND_N7 + BIND_MADARA.format(i=2)
  + BIND_CORR.format(i=3) +
  "The first proper look at the hideout. A colossal underground stone corridor of rough hewn black "
  "rock, cracked pale flagstones underfoot, the ceiling lost in blackness far overhead. The camera "
  "is low and far back, looking down the length of it. The old man in black robes walks ahead with "
  "his cane, and the small boy walks a few paces behind him, both tiny in the frame and dwarfed by "
  "the scale of the place. The only light is a hard cold blue-white rim along the tops of their "
  "shoulders and along one edge of every rock face. The boy's orange jumpsuit is the only colour "
  "that survives at all down here, and even it is drained to a dull brown-grey. Overwhelming, "
  "silent and completely without comfort. " + L_HIDE,
  R("naruto_07", "madara", "env_hideout_corridor"), "low"),

 ("p16", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_TRAIN.format(i=3) +
  "PANEL 1 (wide, top): the training cavern opens out — a vast black rock vault, a pale sand floor, "
  "scattered upright wooden posts, one narrow shaft of cold white light falling from a crack far "
  "above. The boy has stopped at the edge of the sand and is staring at it. PANEL 2 (middle): the "
  "old man has walked out into the middle of the floor and turned back to face him, both hands on "
  "the cane, small in the enormous space. PANEL 3 (large, bottom): a close shot of the old man's "
  "face, lit hard from one side by that cold shaft, the other half of his face in flat black. There "
  "is no kindness in it whatsoever. Nothing in his expression is cruel either — he is simply a man "
  "with very little time left. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_hideout_training"), "low"),

 ("p17", 3,
  PAGE + BIND_N7 + BIND_ZETSU.format(i=2) + BIND_TRAIN.format(i=3) +
  "PANEL 1 (top): the pale sand of the cavern floor bulges and splits and the head and shoulders of "
  "the black-and-white plant creature rise straight up out of the ground beside the boy, its round "
  "yellow eyes and fixed grin catching the cold light. The boy has flinched back a step. PANEL 2 "
  "(middle): the creature is buckling heavy dull grey metal weight-bands around the boy's forearms "
  "and shins — thick, plain, obviously far too heavy for him. PANEL 3 (large, bottom): the boy "
  "trying to take his first step in them. One knee has already gone down into the sand, both arms "
  "hanging like they are full of stone, his face astonished. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "zetsu", "env_hideout_training"), "low"),

 ("p18", 4,
  PAGE + BIND_N7 + BIND_TRAIN.format(i=2) +
  "Four panels of the same task repeating until it stops being a task. Use an identical wide camera "
  "for panels 1, 2 and 3 — the same view across the sand floor of the cavern with the same wooden "
  "posts in the same places — so that only the boy changes between them. PANEL 1: the small boy "
  "running along the far side of the cavern floor in the weight-bands, upright, arms pumping, "
  "furious. PANEL 2: the same view later — he is slower, bent forward, sand kicked up behind him, "
  "shoulders dropped. PANEL 3: the same view later again — he is barely moving, dragging one leg, "
  "head down, a long ragged trail of footprints looping the whole floor behind him. PANEL 4 (a "
  "tight insert across the bottom): an extreme close-up of one of his sandalled feet coming down in "
  "the sand, the ankle folding sideways. " + L_HIDE +
  "Draw one hand-drawn manga sound effect integrated into the artwork in panel 1, a hard slanted "
  "shape reading \"ZA ZA ZA\" trailing behind the running boy, drawn as part of the art. ",
  R("naruto_07", "env_hideout_training"), "low"),

 ("p19", 3,
  PAGE + BIND_N7 + BIND_ZETSU.format(i=2) + BIND_MADARA.format(i=3) +
  "Image 4 is the LOCATION REFERENCE for the sleeping quarters — reuse its rough dark stone "
  "blockwork walls, its cracked flagstone floor, its heavy timber ceiling beam and its near-black "
  "palette exactly. Do not copy its camera angle, ignore the fact that it is empty of people, and "
  "leave out its table, its chairs and its fireplace. "
  "PANEL 1 (wide, top): the boy face down in the pale sand of the cavern floor, arms flung out, "
  "completely still, the weight-bands still buckled on him. Not dead — finished. PANEL 2 (middle): "
  "the black-and-white plant creature has picked him up and carries him slung over one shoulder "
  "like a rolled rug, walking away from camera down a black stone passage, entirely unbothered. "
  "PANEL 3 (wide, bottom): a bare stone room of rough dark blockwork, one plain wooden cot against "
  "the wall. The creature is laying the boy down on it. The old man in black robes stands in the "
  "doorway behind them with his cane, watching, a black shape with one hard cold edge of light down "
  "his side. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_07", "zetsu", "madara", "env_hideout_kitchen"), "low"),

 ("p20", 1,
  "A single full-page illustration, no panel divisions. " + BIND_MADARA.format(i=1)
  + BIND_CORR.format(i=2) +
  "The last page of the chapter, and it should be genuinely unpleasant to look at. An extreme "
  "close-up of the old man's face in three-quarter view, filling almost the whole page, standing in "
  "the near-black of the underground hideout. A single hard cold blue-white rim light runs down the "
  "edge of his brow, his cheekbone and his jaw; everything else, including most of his hair and all "
  "of his robe, is crushed to flat featureless black. His visible eye is a dark red iris with three "
  "small black comma-shaped marks spaced evenly around the pupil, and it is catching the light. He "
  "is SMILING — a wide, slow, closed-mouth smile that pulls the deep lines of his face upward and "
  "does not reach his eye at all. Everything warm and grandfatherly about him for the last four "
  "chapters cracks open here for one panel. Hold the camera very close and let a large area of the "
  "page be plain black around him. " + L_HIDE,
  R("madara", "env_hideout_corridor"), "medium"),
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
