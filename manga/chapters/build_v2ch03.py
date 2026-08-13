"""Volume 2, Chapter 3 — "Six Months". 22 pages.

Source: fic ch4, opening. The fic disposes of both of Team 7's major missions in two
paragraphs, because to Naruto they were unremarkable. That characterisation is the point and
is kept — but two paragraphs is not a reason to draw two panels. Wave gets ten staged pages
and ends on his blank face; Snow stays a true one-page montage, and the contrast between the
two does the work the prose did.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                       # noqa: E402
from prompts import (CAP, ENV, FILL, GAA, GAT, HAK, KAK, KAN, KUY, N13, N13S, ONLY, OFF, R,  # noqa: E402,E501
                     SAK, SAS, SAY, SFX, TEM, TITLE, ZAB, ZET,
                     BOY, FAN, GIRL, MAN, MASK, PAINT, RED, SWORD, UCH,
                     L_DAY, L_DUSK, L_MIST, L_SNOW)

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="solo", mood="calm", panels=1),
  N13S.format(i=1) + ONLY(BOY) +
  "CHAPTER OPENING SPLASH. Dawn over the hidden village from a high rooftop. The blond boy stands "
  "at the very edge of a tiled roof in the lower left of the paper, small, seen from behind and "
  "slightly below, the sword on his back cutting a hard diagonal. Beyond and below him the whole "
  "village falls away in rooftops and water towers to the carved stone faces of the cliff on the "
  "far horizon. A large dark chimney stack is the foreground mass, cropped by the left edge of the "
  "paper. Leave the upper right sky broad and quiet. "
  "Lighting: cold early-morning light, the sun not yet over the cliff, everything blue except a "
  "thin band of gold along the top of the monument. "
  + TITLE("SIX MONTHS"),
  R("naruto_13_sword"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + N13.format(i=1) + KAK.format(i=2) + SAS.format(i=3) + SAK.format(i=4)
  + ONLY(BOY, MAN, UCH, GIRL) +
  "SIX panels, uneven, columns not aligned. A tedious chore-mission in a walled vegetable garden.\n"
  "PANEL 1 (dominant, top): the four of them in the garden at four clearly different depths — the "
  "pink-haired girl nearest, cropped by the bottom edge; the dark-haired boy mid-ground with his "
  "back to us; the blond boy further off, kneeling in the rows; the masked man furthest, leaning on "
  "the wall with an open book.\n"
  "PANEL 2 (small): the girl beaming sideways at the dark-haired boy.\n"
  "PANEL 3 (small): the dark-haired boy, not looking at her.\n"
  "PANEL 4 (small): the masked man's book, held up — but his single visible eye is looking OVER the "
  "top of it, off to the side, not at the page.\n"
  "PANEL 5 (small): what he is looking at — the blond boy's hands in the dirt. No face.\n"
  "PANEL 6 (wide, bottom): the garden from behind the masked man's shoulder, cropped huge and dark "
  "in the foreground, the blond boy small and central beyond him. " + L_DAY
  + SAY((2, GIRL, "upper left", "SASUKE-KUN! WE COULD GET RAMEN AFTER THIS!"),
        (3, UCH, "upper right", "NO.")),
  R("naruto_13", "kakashi", "sasuke", "sakura"), "medium"),

 ("p03", dict(scene="dialogue", light="dusk", cast="small_group", mood="tense", panels=6),
  FILL + KAK.format(i=1) + N13.format(i=2) + ZET.format(i=3)
  + ONLY(MAN, BOY, "the split black-and-white plant creature") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the masked man raising a hand in farewell, already turning away.\n"
  "PANEL 2 (small): his back, walking off down a lane.\n"
  "PANEL 3 (dominant, middle): the same masked man STILL leaning against the garden wall, exactly "
  "where he was — two of him, one small and distant walking away at the top of the panel, one large "
  "in the foreground cropped by the right edge, reading. The blond boy stands between them, small, "
  "looking at neither.\n"
  "PANEL 4 (small): the blond boy's single visible eye, flat.\n"
  "PANEL 5 (small): a garden wall at dusk, apparently empty.\n"
  "PANEL 6 (wide, bottom): the plant creature's head and shoulders emerging out of the solid wall "
  "beside the boy as though the brick were water, the boy not turning to look at it. " + L_DUSK
  + SAY((1, MAN, "upper left", "I HAVE A REPORT TO FILE. CARRY ON WITHOUT ME."),
        (4, BOY, "upper right", "HE HAS NOT LEFT ME ALONE ONCE IN SIX MONTHS."),
        (6, "the plant creature", "upper left", "HE IS THOROUGH. I ALMOST ADMIRE HIM.")),
  R("kakashi", "naruto_13", "zetsu"), "medium"),

 # ---------------------------------------------------------------- WAVE
 ("p04", dict(scene="establishing", light="overcast", cast="small_group", mood="somber", panels=5),
  FILL + ENV.format(i=1) + N13.format(i=2) + SAK.format(i=3) + KAK.format(i=4)
  + ONLY(BOY, GIRL, MAN, "one other young genin", "a stocky grey-haired old man in a straw hat and "
         "round glasses with a towel round his neck") +
  "FIVE panels, uneven. A small rowing boat crossing flat grey water in heavy sea mist.\n"
  "PANEL 1 (small): the prow of the boat cutting still water. No people.\n"
  "PANEL 2 (small): the pink-haired girl gripping the gunwale, wide-eyed.\n"
  "PANEL 3 (small): the blond boy in the stern, looking at nothing, entirely unafraid.\n"
  "PANEL 4 (dominant, middle): the boat tiny at the bottom of the panel as an ENORMOUS unfinished "
  "bridge rears out of the mist above and ahead of it, bare girders and scaffolding vanishing "
  "upward and away. Overwhelming scale difference.\n"
  "PANEL 5 (wide, bottom): the poor stilt village of weathered shacks emerging from the fog. "
  + L_MIST
  + CAP(1, "upper left", "WAVE COUNTRY. FIVE MONTHS AGO.")
  + SAY((2, GIRL, "upper right", "IT'S SO QUIET...")),
  R("env_wave_bridge", "naruto_13", "sakura", "kakashi"), "high"),

 ("p05", dict(scene="action", light="overcast", cast="small_group", mood="tense", panels=5),
  FILL + KAK.format(i=1) + ZAB.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(MAN, SWORD, BOY, "two other young genin seen only as small distant figures",
         "a stocky grey-haired old man in a straw hat") +
  "FIVE panels, uneven, violent diagonals.\n"
  "PANEL 1 (small): a forest road in fog. Nothing moving.\n"
  "PANEL 2 (narrow letterbox): the masked man's single eye snapping wide.\n"
  "PANEL 3 (dominant, middle): an ENORMOUS flat butcher-blade sword spinning end over end straight "
  "at the camera out of the fog, filling the panel, the tiny figures of the group flattening "
  "themselves below it. The blade is the whole composition.\n"
  "PANEL 4 (small): the blade buried deep in a tree trunk, still shuddering.\n"
  "PANEL 5 (wide, bottom): the bandage-faced swordsman standing balanced on the hilt of his own "
  "sword high in the tree, seen from far below, huge against a white sky. " + L_MIST
  + SAY((2, MAN, "upper left", "GET DOWN!"),
        (5, SWORD, "upper right", "KAKASHI OF THE SHARINGAN. HAND OVER THE BRIDGE BUILDER."))
  + SFX(3, "SHUNN", "It crosses the gutter into the panel below."),
  R("kakashi", "zabuza", "naruto_13", "env_wave_village"), "high"),

 ("p06", dict(scene="action", light="overcast", cast="two", mood="tense", panels=6),
  FILL + KAK.format(i=1) + ZAB.format(i=2) + ENV.format(i=3) + ONLY(MAN, SWORD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the masked man's gloved hand pushing the slanted forehead protector up off his "
  "left eye. Hand and metal only.\n"
  "PANEL 2 (small): the eye revealed — blood-red with three black comma marks around the pupil, "
  "scarred vertically. Cropped tight, flat black behind it.\n"
  "PANEL 3 (dominant, middle): the two of them fighting ON TOP OF flat grey water, the swordsman "
  "huge in the foreground mid-swing cropped by the right edge, the masked man small and low, "
  "skidding backwards across the surface, spray thrown in flat opaque shapes.\n"
  "PANEL 4 (small): the water surface exploding upward. No figures.\n"
  "PANEL 5 (small): the swordsman's eyes above the bandages, delighted.\n"
  "PANEL 6 (wide, bottom): both of them at a distance across the water, mist closing in, tiny. "
  + L_MIST
  + SAY((5, SWORD, "upper left", "COPYING ME ALREADY. THAT EYE IS EVERYTHING THEY SAY IT IS."))
  + SFX(3, "ZSHAA"),
  R("kakashi", "zabuza", "env_wave_village"), "high"),

 ("p07", dict(scene="action", light="overcast", cast="small_group", mood="tense", panels=7),
  FILL + ZAB.format(i=1) + KAK.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + N13.format(i=5)
  + ONLY(SWORD, MAN, UCH, GIRL, BOY) +
  "SEVEN panels, uneven and crowded.\n"
  "PANEL 1 (small): the swordsman's hand closing flat against a sphere of water.\n"
  "PANEL 2 (dominant, upper): the masked man sealed inside a perfect sphere of water, suspended, "
  "one hand pressed uselessly against the inside of it; the swordsman stands beside it with his arm "
  "buried in the sphere to the shoulder, enormous in the foreground, cropped by the left edge.\n"
  "PANEL 3 (small): the pink-haired girl frozen with both hands over her mouth.\n"
  "PANEL 4 (small): the dark-haired boy already running, teeth bared.\n"
  "PANEL 5 (small): a huge backhand blow catching him mid-air. Flat impact shapes, no injury "
  "detail.\n"
  "PANEL 6 (small): the dark-haired boy face down, not moving.\n"
  "PANEL 7 (wide, bottom): the blond boy standing perfectly still at the edge of the water, hands "
  "at his sides, watching. He has not moved at all. " + L_MIST
  + SAY((2, MAN, "upper right", "RUN. ALL OF YOU."),
        (2, SWORD, "lower left", "TOO SLOW."))
  + SFX(5, "DOGA"),
  R("zabuza", "kakashi", "sasuke", "sakura", "naruto_13"), "high"),

 ("p08", dict(scene="action", light="overcast", cast="small_group", mood="tense", panels=6),
  FILL + N13.format(i=1) + ZAB.format(i=2) + SAS.format(i=3) + KAK.format(i=4)
  + ONLY(BOY, SWORD, UCH, MAN) +
  "SIX panels, uneven. This page is a SLEIGHT OF HAND: the reader sees who really acted, the "
  "characters do not.\n"
  "PANEL 1 (narrow letterbox): the blond boy's fingers, low at his hip, releasing a single shuriken "
  "almost without moving. Hand only, cropped by all four edges.\n"
  "PANEL 2 (small): the shuriken crossing flat grey water in a dead straight line.\n"
  "PANEL 3 (dominant, middle): the swordsman wrenching his arm out of the water sphere to slap the "
  "shuriken away — and the sphere collapsing into falling flat sheets of water behind him, the "
  "masked man dropping free through them. The swordsman is huge, the collapse fills the panel.\n"
  "PANEL 4 (small): the dark-haired boy staring at his own open hand, bewildered.\n"
  "PANEL 5 (small): the blond boy's hand, empty, already lowered to his side. No face.\n"
  "PANEL 6 (wide, bottom): the swordsman's head turning — and looking straight at the DARK-HAIRED "
  "boy, not at the blond one. " + L_MIST
  + SAY((6, SWORD, "upper left", "...THE UCHIHA BRAT THREW THAT?"))
  + SFX(3, "PASHA"),
  R("naruto_13", "zabuza", "sasuke", "kakashi"), "high"),

 ("p09", dict(scene="action", light="overcast", cast="small_group", mood="somber", panels=6),
  FILL + HAK.format(i=1) + ZAB.format(i=2) + KAK.format(i=3) + N13.format(i=4)
  + ONLY(MASK, SWORD, MAN, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a spray of long thin steel needles crossing the mist.\n"
  "PANEL 2 (dominant, upper): the swordsman going down full length, needles in the side of his "
  "collar, seen from a low angle with the white sky behind him. No injury detail, no red.\n"
  "PANEL 3 (small): a slender figure in a plain white porcelain mask standing in the branches "
  "above, seen from below.\n"
  "PANEL 4 (small): the masked figure lifting the enormous body across its shoulders, tiny under "
  "the weight.\n"
  "PANEL 5 (small): the masked man on one knee in the road, exhausted, one eye closed.\n"
  "PANEL 6 (wide, bottom): the empty road, the fog closing, the blond boy standing looking at the "
  "place where they were. " + L_MIST
  + SAY((3, MASK, "upper left", "THANK YOU. I HAVE BEEN HUNTING HIM A LONG TIME."),
        (5, MAN, "upper right", "A HUNTER DISPOSES OF THE BODY WHERE IT FALLS."),
        (6, BOY, "upper left", "HE DIDN'T.")),
  R("haku", "zabuza", "kakashi", "naruto_13"), "high"),

 ("p10", dict(scene="action", light="overcast", cast="small_group", mood="tense", panels=6),
  FILL + ZAB.format(i=1) + HAK.format(i=2) + N13.format(i=3) + SAS.format(i=4) + KAK.format(i=5)
  + ONLY(SWORD, MASK, BOY, UCH, MAN) +
  "SIX panels, uneven. On the unfinished bridge, deep in mist.\n"
  "PANEL 1 (small): bare bridge decking vanishing into white. No people.\n"
  "PANEL 2 (small): the bandage-faced swordsman's eyes opening in the fog.\n"
  "PANEL 3 (small): the masked man's shoulders squaring.\n"
  "PANEL 4 (dominant, middle): a DOME of tall flat mirrors made of ice standing in a ring on the "
  "bridge deck, each one holding the same reflection of the white-masked figure — a dozen "
  "identical reflections around a circle. The blond boy and the dark-haired boy are small and "
  "trapped at the centre, seen from high above.\n"
  "PANEL 5 (small): one mirror in close-up, the masked face inside it.\n"
  "PANEL 6 (wide, bottom): the dark-haired boy braced and furious, the blond boy beside him "
  "standing quite loose, hands at his sides. " + L_MIST
  + SAY((2, SWORD, "upper left", "DID YOU MISS ME, KAKASHI?"),
        (5, MASK, "upper right", "I DO NOT WISH TO HURT YOU. PLEASE DO NOT MAKE ME."))
  + SFX(4, "KIIIN"),
  R("zabuza", "haku", "naruto_13", "sasuke", "kakashi"), "high"),

 ("p11", dict(scene="action", light="overcast", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + HAK.format(i=2) + N13.format(i=3) + ONLY(UCH, MASK, BOY) +
  "SIX panels, uneven. Inside the ring of ice mirrors.\n"
  "PANEL 1 (small): needles coming from every direction at once, drawn as flat converging lines.\n"
  "PANEL 2 (small): the dark-haired boy knocked sideways, arms up.\n"
  "PANEL 3 (small): him on his knees, head down, breathing hard. No injury detail.\n"
  "PANEL 4 (dominant, middle): his head coming up — both eyes now BLOOD RED with two black comma "
  "marks curling around each pupil. Cropped very tight on the face, flat black behind, hard "
  "radiating lines. This is the biggest panel on the page.\n"
  "PANEL 5 (small): a mirror reflection blurring as the masked figure moves between them.\n"
  "PANEL 6 (wide, bottom): the dark-haired boy on his feet again, tracking the movement, the blond "
  "boy behind him not moving at all. "
  + L_MIST
  + SAY((3, UCH, "upper left", "WHY DID MY BODY MOVE ON ITS OWN?"))
  + SFX(4, "DOKUN"),
  R("sasuke", "haku", "naruto_13"), "high"),

 ("p12", dict(scene="emotional_closeup", light="overcast", cast="two", mood="somber", panels=6),
  FILL + N13.format(i=1) + HAK.format(i=2) + SAS.format(i=3) + ONLY(BOY, MASK, UCH) +
  "SIX panels, uneven. Escalate by cropping tighter, not by adding rendering.\n"
  "PANEL 1 (small): the white porcelain mask filling the panel, close enough to see the two narrow "
  "eye slits.\n"
  "PANEL 2 (small): the dark-haired boy down on the deck behind the blond boy, out of focus of the "
  "composition — small, at the panel's edge.\n"
  "PANEL 3 (small): the blond boy's hands. Open. Empty. Completely relaxed.\n"
  "PANEL 4 (narrow letterbox): his single visible eye, cropped by all four edges, giving nothing.\n"
  "PANEL 5 (small): the masked figure, head tilted, genuinely puzzled by him.\n"
  "PANEL 6 (dominant, bottom): the two of them facing each other inside the ring of mirrors, the "
  "blond boy small and still at the bottom of a mostly empty panel, the mirrors towering. " + L_MIST
  + SAY((1, MASK, "upper right", "YOUR COMRADE IS DYING. AND YOU HAVE NOT MOVED."),
        (4, BOY, "upper left", "HE IS NOT MY COMRADE."),
        (6, BOY, "upper right", "AND HE IS NOT DYING.")),
  R("naruto_13", "haku", "sasuke"), "high"),

 ("p13", dict(scene="action", light="overcast", cast="small_group", mood="somber", panels=6),
  FILL + GAT.format(i=1) + ZAB.format(i=2) + HAK.format(i=3) + ENV.format(i=4)
  + ONLY(SWORD, MASK, "the short fat man in sunglasses and a black suit",
         "a crowd of ragged hired mercenaries with mismatched weapons") +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the far end of the bridge crowded with a mob of ragged hired "
  "mercenaries, the short fat man in the black suit standing small and smug in front of them, seen "
  "from a low angle so the mob fills the sky behind him.\n"
  "PANEL 2 (small): the fat man's round black sunglasses, close.\n"
  "PANEL 3 (small): the swordsman on one knee, head down, sword point-down in the decking.\n"
  "PANEL 4 (small): his eyes above the bandages — nothing left in them but purpose.\n"
  "PANEL 5 (small): the mob scattering backwards away from something, flat motion lines, no "
  "figures struck.\n"
  "PANEL 6 (wide, bottom): the swordsman lying full length on the bridge deck beside the slender "
  "masked figure, both quite still, snow beginning to fall on them. No injury detail, no red. "
  + L_MIST
  + SAY((1, "the short fat man in sunglasses", "upper left", "YOU'RE FINISHED, ZABUZA. I NEVER INTENDED TO PAY YOU."),
        (4, SWORD, "upper right", "THEN I HAVE NO EMPLOYER. AND NO REASON TO LEAVE YOU STANDING.")),
  R("gato", "zabuza", "haku", "env_wave_bridge"), "high"),

 ("p14", dict(scene="emotional_closeup", light="day", cast="small_group", mood="calm", panels=5),
  FILL + ENV.format(i=1) + N13.format(i=2) + SAK.format(i=3) + SAS.format(i=4)
  + ONLY(BOY, GIRL, UCH, "their silver-haired sensei") +
  "FIVE panels, uneven. The point of this page is that none of it touched him.\n"
  "PANEL 1 (dominant, top): the FINISHED bridge in clean sunlight, its full span crossing the "
  "water, tiny figures of the four of them walking away from camera along it.\n"
  "PANEL 2 (small): the pink-haired girl half-turning, talking.\n"
  "PANEL 3 (small): the dark-haired boy, not turning.\n"
  "PANEL 4 (small): the boy's sandals on new decking. No face.\n"
  "PANEL 5 (wide, bottom): the blond boy's face in close-up, cropped tight. Absolutely blank. Not "
  "sad, not relieved — simply not interested. No balloon anywhere in this panel. " + L_DAY
  + SAY((2, GIRL, "upper left", "DO YOU THINK THEY'LL NAME IT AFTER US?"),
        (3, UCH, "upper right", "NO.")),
  R("env_wave_bridge", "naruto_13", "sakura", "sasuke"), "high"),

 # ---------------------------------------------------------------- SNOW: a true montage
 ("p15", dict(scene="establishing", light="day", cast="small_group", mood="calm", panels=8),
  FILL + ENV.format(i=1) + KUY.format(i=2) + N13.format(i=3)
  + ONLY(BOY, "the black-haired princess",
         "three other Konoha ninja seen only as small distant figures") +
  "EIGHT panels — deliberately FRAGMENTS, small and quick, nothing given room. Uneven sizes, "
  "columns not aligned.\n"
  "PANEL 1 (small): a snowfield under a pale sky, black pines, four tiny figures crossing it.\n"
  "PANEL 2 (small): the black-haired woman in a plain travelling coat, sullen, arms folded.\n"
  "PANEL 3 (small): a film camera and lights standing abandoned in the snow. Objects only.\n"
  "PANEL 4 (small): a dark stone castle with steep snow-laden roofs, distant.\n"
  "PANEL 5 (small): armoured soldiers running on ice, drawn small and flat, no faces.\n"
  "PANEL 6 (small): a broken sheet of ice tilting into black water. No figures.\n"
  "PANEL 7 (small): the blond boy watching all of it from a ridge, hands at his sides, bored.\n"
  "PANEL 8 (wide, bottom): the same woman in ornate white-and-red royal robes and a tall formal "
  "headdress, standing straight before a crowd seen only as heads and shoulders from behind. "
  + L_SNOW
  + CAP(1, "upper left", "SNOW COUNTRY. THREE MONTHS AGO.")
  + SAY((2, "the black-haired princess", "upper right", "I AM NOT A PRINCESS. I AM AN ACTRESS.")),
  R("env_snow_country", "kuyoki", "naruto_13"), "medium"),

 # ---------------------------------------------------------------- back to the present
 ("p16", dict(scene="establishing", light="day", cast="solo", mood="calm", panels=5),
  FILL + N13S.format(i=1) + ENV.format(i=2) + ZET.format(i=3) + KAK.format(i=4)
  + ONLY(BOY, "the split black-and-white plant creature", MAN,
         "ordinary villagers in the street who pay him no attention") +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the sword's wrapped hilt above the boy's left shoulder, from behind. No face.\n"
  "PANEL 2 (dominant, middle): a busy village street from a high angle, the blond boy walking away "
  "from camera down the middle of it, villagers at the edges of frame at different depths, several "
  "turned away, none of them looking at him.\n"
  "PANEL 3 (small): a rooftop above the street — the masked silver-haired man crouched on the "
  "ridge, small, watching down.\n"
  "PANEL 4 (small): a DIFFERENT rooftop, further off — the same masked man again, identical, also "
  "watching. Two of him on one page.\n"
  "PANEL 5 (wide, bottom): the boy passing a shaded wall, the plant creature's white-and-black face "
  "half-emerged from the brickwork beside him at waist height. He does not look at it. " + L_DAY
  + SAY((5, "the plant creature", "upper left", "STILL TWO OF THEM."),
        (5, BOY, "upper right", "LET HIM WATCH. HE WILL SEE A GENIN WALK TO AN EXAM.")),
  R("naruto_13_sword", "env_village_street", "zetsu", "kakashi"), "medium"),

 ("p17", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + ENV.format(i=1) + N13S.format(i=2)
  + ONLY(BOY, "crowds of teenage foreign ninja from many different villages, none of them named or "
         "recurring, all dressed differently from each other") +
  "FIVE panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): a forehead protector with an unfamiliar hourglass symbol. Object only.\n"
  "PANEL 2 (small): a different one with a musical note. Object only.\n"
  "PANEL 3 (dominant, middle): the plaza outside the academy packed with foreign teenage ninja in "
  "unfamiliar clothing, standing in tight groups at many different depths, several cropped by the "
  "panel edges, several turned away from camera. Nobody evenly spaced, nobody facing the viewer.\n"
  "PANEL 4 (small): two of them noticing something off-panel and going quiet.\n"
  "PANEL 5 (wide, bottom): the blond boy walking into the plaza from the right, small, the crowd "
  "parting fractionally around him without anyone appearing to intend it. " + L_DAY,
  R("env_academy_ext", "naruto_13_sword"), "medium"),

 ("p18", dict(scene="action", light="day", cast="small_group", mood="tense", panels=6),
  FILL + N13S.format(i=1) + KAN.format(i=2) + TEM.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, PAINT, FAN) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): two shoulders colliding, cropped tight. No faces.\n"
  "PANEL 2 (small): the boy with purple face paint rounding on him, snarling.\n"
  "PANEL 3 (dominant, middle): the face-painted boy has taken a fistful of the blond boy's shirt "
  "and lifted him half off his feet — the face-painted boy huge in the foreground cropped by the "
  "left edge, the blond boy's face small and utterly calm at the centre, the blonde girl with four "
  "pigtails standing further back with her arms folded.\n"
  "PANEL 4 (small): the blond boy's feet, one sandal barely touching the ground.\n"
  "PANEL 5 (small): the blonde girl's face, irritated rather than alarmed.\n"
  "PANEL 6 (wide, bottom): the three of them in the street, a ring of foreign genin backing away at "
  "the edges of frame. " + L_DAY
  + SAY((2, PAINT, "upper left", "WATCH WHERE YOU'RE GOING, BRAT!"),
        (5, FAN, "upper right", "KANKURO. WHAT ARE YOU DOING?")),
  R("naruto_13_sword", "kankuro", "temari", "env_village_street"), "high"),

 ("p19", dict(scene="action", light="day", cast="small_group", mood="tense", panels=6),
  FILL + KAN.format(i=1) + N13S.format(i=2) + TEM.format(i=3) + ONLY(PAINT, BOY, FAN) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the face-painted boy grinning, close.\n"
  "PANEL 2 (narrow letterbox): the blond boy's fist already moving. Hand and forearm only, cropped "
  "by all four edges, hard motion lines.\n"
  "PANEL 3 (dominant, middle): the punch landing in the face-painted boy's stomach — flat opaque "
  "impact shapes with hard black outlines, the face-painted boy folding forward over the fist, the "
  "blond boy's expression completely unchanged. No injury detail.\n"
  "PANEL 4 (small): the blond boy's shirt falling out of a slackened hand.\n"
  "PANEL 5 (small): the face-painted boy on one knee, both arms round his middle.\n"
  "PANEL 6 (wide, bottom): the blonde girl's hand frozen halfway to the fan on her back, having not "
  "seen it happen. " + L_DAY
  + SAY((1, PAINT, "upper left", "I'M TEACHING THIS BRAT TO RESPECT HIS ELDERS."),
        (5, PAINT, "upper right", "...THAT HURT."))
  + SFX(3, "DOSU"),
  R("kankuro", "naruto_13_sword", "temari"), "high"),

 ("p20", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=6),
  FILL + GAA.format(i=1) + KAN.format(i=2) + TEM.format(i=3) + ONLY(RED, PAINT, FAN) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a bare tree branch above the street, apparently empty.\n"
  "PANEL 2 (small): the face-painted boy's head snapping round, all the colour gone out of him.\n"
  "PANEL 3 (small): the blonde girl going rigid.\n"
  "PANEL 4 (dominant, middle): the red-haired boy standing UPSIDE DOWN on the underside of the "
  "branch, the enormous gourd on his back hanging over him, seen from below against a white sky. "
  "He is small in the panel and it is entirely about him.\n"
  "PANEL 5 (small): his face — no eyebrows, black rings, the red kanji on his forehead. Blank.\n"
  "PANEL 6 (wide, bottom): the face-painted boy on his knees looking up, the red-haired boy landing "
  "in the street, sand trailing off the gourd in flat opaque ribbons. " + L_DAY
  + SAY((1, OFF(RED), "upper right", "THAT IS WHAT HAPPENS WHEN YOU ACT LIKE A FOOL."),
        (5, RED, "upper left", "YOU ARE EMBARRASSING OUR VILLAGE."),
        (6, PAINT, "lower left", "S-SORRY, GAARA!")),
  R("gaara", "kankuro", "temari"), "high"),

 ("p21", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + N13S.format(i=1) + GAA.format(i=2) + KAN.format(i=3) + TEM.format(i=4)
  + ONLY(BOY, RED, PAINT, FAN) +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the blond boy in the foreground turned three-quarters away from camera, "
  "the three sand ninja beyond him at three clearly different depths, the red-haired boy furthest "
  "and smallest and still the one the composition points at.\n"
  "PANEL 2 (small): the blonde girl's eyes widening.\n"
  "PANEL 3 (small): the face-painted boy's, wider.\n"
  "PANEL 4 (small): the blond boy's mouth only, flat, mid-sentence.\n"
  "PANEL 5 (small): the face-painted boy's own hand, held close against his chest now.\n"
  "PANEL 6 (wide, bottom): the blond boy already walking away from all three of them, seen from "
  "behind, not looking back. " + L_DAY
  + SAY((1, BOY, "upper left", "THE SAND SIBLINGS. THE CHILDREN OF THE FOURTH KAZEKAGE."),
        (2, OFF(BOY), "upper right", "SABAKU NO GAARA. JINCHURIKI OF THE ICHIBI."),
        (4, BOY, "upper left", "TOUCH ME AGAIN AND I WILL CUT OFF YOUR HAND AND FEED IT TO YOU."),
        (6, BOY, "upper right", "YOU DO NOT ATTACK SOMEONE WITHOUT MEASURING THEM FIRST.")),
  R("naruto_13_sword", "gaara", "kankuro", "temari"), "high"),

 ("p22", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=5),
  FILL + GAA.format(i=1) + N13S.format(i=2) + KAN.format(i=3) + TEM.format(i=4)
  + ONLY(RED, BOY, PAINT, FAN) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the red-haired boy in the empty street, small, the gourd enormous behind him.\n"
  "PANEL 2 (small): the blond boy stopped mid-step with his back to camera, half-turned.\n"
  "PANEL 3 (narrow letterbox): the blond boy's single visible eye and the red-haired boy's pale "
  "ringed eyes in the SAME panel, split by a hard vertical black bar down the middle.\n"
  "PANEL 4 (small): the empty street where the blond boy was standing. Nobody there.\n"
  "PANEL 5 (dominant, bottom): the red-haired boy grinning — an enormous, delighted, entirely wrong "
  "grin, cropped tight, hard radiating lines behind him. His brother and sister are small at the "
  "edge of the panel, watching him with open fear. " + L_DAY
  + SAY((1, RED, "upper right", "WHAT IS YOUR NAME?"),
        (2, BOY, "upper left", "UZUMAKI NARUTO."),
        (2, BOY, "lower right", "I WILL SEE YOU AT THE EXAMS, SABAKU NO GAARA.")),
  R("gaara", "naruto_13_sword", "kankuro", "temari"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v2ch03" / "raw", HERE / "v2ch03" / "ledger.json")
