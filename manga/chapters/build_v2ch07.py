"""Volume 2, Chapter 7 — "The Forest of Death". 22 pages. Ends Volume 2.

Source: fic ch4, Anko's briefing through the Kusa-nin ambush. The volume plan had this
ending on three Rain genin; the fic itself runs straight past them into the ambush, which
is a far better last page — the volume closes on the first opponent Naruto has met that he
knows he cannot beat, and on a snake the size of a house.

What the chapter costs him: his patience. He is about to stop being careful.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ANK, ENV, FILL, IBI, N13S, ONLY, OFF, R, SAK, SAS, SAY,     # noqa: E402
                     SFX, TITLE, UNIQUE,
                     BOY, COAT, GIRL, SCAR, UCH)

CROWD = "the crowd of teenage genin from many villages, none of them recurring"
KUSA = ("Image {i} is the CHARACTER REFERENCE for the ninja in the straw hat: tall and slender, a "
        "wide conical straw hat worn low over the face, a long earth-brown robe over a dark "
        "bodysuit, very long straight black hair falling past the waist, unnaturally pale white "
        "skin. When the hat tips back the face shows GOLDEN-YELLOW EYES WITH VERTICAL SLIT PUPILS "
        "and purple markings around them, and a long thin tongue extended far further than any "
        "human tongue should reach. Reproduce exactly; ignore its white background and layout. ")
SNAKE = ("Image {i} is the CREATURE REFERENCE: a COLOSSAL brown-and-tan serpent as thick as a tree "
         "trunk and many times the length of a house, blunt wedge-shaped head, heavy overlapping "
         "scales, pale banded underbelly, huge golden eyes with vertical black slit pupils, long "
         "curved fangs. It is an animal, not a person. Reproduce exactly; ignore its white "
         "background and layout. ")
HAT = "the ninja in the straw hat"
L_FOREST = "Lighting: sunless green-black gloom under a dense canopy, hard shafts of pale light. "

PAGES = [
 ("p01", dict(scene="establishing", light="dark", cast="solo", mood="tense", panels=1),
  N13S.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "CHAPTER OPENING SPLASH. Looking INTO the forest through a gap in a tall chain-link perimeter "
  "fence. The trees beyond are colossally oversized — trunks many metres thick, roots like walls — "
  "and the canopy closes over into pure black at the top of the paper. The blond boy stands small "
  "and off centre at the bottom of the paper with his back to us, at the very edge of the light, "
  "about to step in; the sword on his back cuts a hard diagonal. A great curving root is the "
  "foreground mass, cropped by the lower right edge. Leave a pale shaft of light falling through "
  "the canopy at the upper left broad and quiet. "
  "Lighting: cold light behind the viewer, the forest ahead swallowing all of it — the boy is "
  "almost a silhouette. " + TITLE("THE FOREST OF DEATH", "pale shaft of light at the upper left"),
  R("naruto_13_sword", "env_forest_of_death"), "high"),

 ("p02", dict(scene="action", light="interior", cast="crowd", mood="calm", panels=6),
  FILL + ANK.format(i=1) + IBI.format(i=2) + ENV.format(i=3) + ONLY(COAT, SCAR, BOY, CROWD) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): the blond boy's head turning toward a window nobody else is looking at.\n"
  "PANEL 2 (small): a dark shape hurtling at the glass from outside.\n"
  "PANEL 3 (dominant, middle): the window blowing inward in a spray of flat hard-edged glass "
  "shards, and a woman in a long open tan overcoat coming through it feet-first — she is huge in "
  "the foreground cropped by the top edge, the seated genin small and recoiling below her at many "
  "depths. A cloth banner unfurls behind her carrying illegible scribble, not readable words.\n"
  "PANEL 4 (small): the scarred man in the head-wrap putting a hand over his eyes.\n"
  "PANEL 5 (small): the woman's face, grinning much too widely.\n"
  "PANEL 6 (wide, bottom): the wrecked window, the banner, the whole hall staring. "
  "Lighting: flat institutional daylight. "
  + SAY((5, COAT, "upper left", "NO TIME FOR CELEBRATIONS, BRATS. I'M THE SECOND PROCTOR."),
        (6, COAT, "upper right", "FOLLOW ME."))
  + SFX(3, "GASHAAN"),
  R("anko", "ibiki", "env_exam_room_301"), "high"),

 ("p03", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + ANK.format(i=1) + ENV.format(i=2) + N13S.format(i=3) + ONLY(COAT, BOY, UCH, GIRL, CROWD) +
  "FIVE panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): boots on a dirt track. Feet only.\n"
  "PANEL 2 (small): the woman in the tan coat walking ahead, seen from behind, hands in pockets.\n"
  "PANEL 3 (dominant, middle): a long column of genin walking away from camera down a track toward "
  "a treeline, small and strung out at many depths, several cropped by the panel edges — and ahead "
  "of them the forest rising like a wall, drawn far larger than it should be.\n"
  "PANEL 4 (small): a tall chain-link fence, and a warning sign whose writing is illegible "
  "scribble. Objects only.\n"
  "PANEL 5 (wide, bottom): the crowd stopped at the fence, all of them looking up. " + L_FOREST,
  R("anko", "env_forest_of_death", "naruto_13_sword"), "high"),

 ("p04", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=6),
  FILL + ANK.format(i=1) + SAK.format(i=2) + ENV.format(i=3) + ONLY(COAT, GIRL, BOY, UCH, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the woman in the tan coat looking up at the trees with genuine affection.\n"
  "PANEL 2 (dominant, upper): the forest beyond the fence — colossal trunks vanishing up out of "
  "frame, roots like walls, mist between them, the canopy solid black overhead. The crowd of genin "
  "is a thin line of small figures along the bottom edge of the panel. Overwhelming scale "
  "difference.\n"
  "PANEL 3 (small): the pink-haired girl's face, shrinking.\n"
  "PANEL 4 (small): the blond boy's face — visibly, openly BORED, which nobody else is.\n"
  "PANEL 5 (small): the woman's smirk.\n"
  "PANEL 6 (wide, bottom): the fence line, the crowd, the trees. " + L_FOREST
  + SAY((1, COAT, "upper left", "TRAINING GROUND FORTY-FOUR. WE CALL IT THE FOREST OF DEATH."),
        (3, GIRL, "upper right", "THIS PLACE GIVES ME THE CREEPS."),
        (5, COAT, "lower right", "YOU'LL FIND OUT SOON ENOUGH WHY WE CALL IT THAT.")),
  R("anko", "sakura", "env_forest_of_death"), "high"),

 ("p05", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=6),
  FILL + ANK.format(i=1) + ENV.format(i=2) + ONLY(COAT, BOY, UCH, GIRL, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a fan of papers held up in one hand. Objects only, writing illegible.\n"
  "PANEL 2 (small): a genin's face reading one, going white.\n"
  "PANEL 3 (small): another genin's hands, refusing to take it.\n"
  "PANEL 4 (dominant, middle): the woman in the tan coat holding the papers out over the heads of "
  "the crowd, seen from below, the fence and the black forest filling everything behind her.\n"
  "PANEL 5 (small): her face, delighted by the reaction.\n"
  "PANEL 6 (wide, bottom): the crowd, nobody stepping forward yet. " + L_FOREST
  + SAY((4, COAT, "upper left", "SIGN THESE FIRST."),
        (5, COAT, "upper right", "PEOPLE DIE IN THIS TEST. I'D RATHER NOT BE BLAMED FOR IT.")),
  R("anko", "env_forest_of_death"), "high"),

 ("p06", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=7),
  FILL + ANK.format(i=1) + ENV.format(i=2) + ONLY(COAT, BOY, CROWD) +
  "SEVEN panels — a briefing, so it moves fast in fragments. Uneven, columns not aligned.\n"
  "PANEL 1 (small): a hand holding up a rolled scroll with a plain seal. Object only.\n"
  "PANEL 2 (small): a second, identical scroll in the other hand. Objects only.\n"
  "PANEL 3 (small): a locked iron gate in the perimeter fence. No people.\n"
  "PANEL 4 (dominant, middle): a wide aerial view of the whole training ground drawn as if from far "
  "above — a vast circle of black forest ringed by fence, a river crossing it, and a single tall "
  "tower at the dead centre, tiny. No people anywhere in this panel.\n"
  "PANEL 5 (small): the woman in the tan coat, counting on her fingers.\n"
  "PANEL 6 (small): a genin's face doing the arithmetic and not liking it.\n"
  "PANEL 7 (wide, bottom): the crowd at the fence. " + L_FOREST
  + SAY((1, COAT, "upper left", "ONE SCROLL PER TEAM. HEAVEN OR EARTH."),
        (4, COAT, "upper right", "REACH THE TOWER WITH BOTH KINDS. FIVE DAYS. NO QUITTING."),
        (7, COAT, "upper left", "LOSE A TEAMMATE AND YOU FAIL. OPEN YOUR SCROLL AND YOU FAIL.")),
  R("anko", "env_forest_of_death"), "high"),

 ("p07", dict(scene="dialogue", light="day", cast="crowd", mood="calm", panels=6),
  FILL + ANK.format(i=1) + ENV.format(i=2)
  + ONLY(COAT, BOY, GIRL, UCH, "a round-cheeked heavyset boy with a bag of snacks", CROWD) +
  "SIX panels, uneven. A joke page, and a nasty one.\n"
  "PANEL 1 (small): a hand deep in a crinkling snack bag. Hand and bag only.\n"
  "PANEL 2 (small): a round-cheeked heavyset boy mid-chew, entirely sincere.\n"
  "PANEL 3 (small): the woman in the tan coat's face, going bright and helpful.\n"
  "PANEL 4 (dominant, middle): what she is describing — a dark tangle of forest floor crawling with "
  "oversized insects and thick fleshy plants, drawn as an inset with a ragged torn-paper border. No "
  "people in this panel at all.\n"
  "PANEL 5 (small): several genin faces at once, all of them regretting this.\n"
  "PANEL 6 (wide, bottom): the crowd, visibly smaller in spirit than a page ago. " + L_FOREST
  + SAY((2, "the round-cheeked heavyset boy with the snacks", "upper left", "UM — WHAT ABOUT FOOD?"),
        (3, COAT, "upper right", "THE FOREST IS FULL OF FOOD!"),
        (4, OFF(COAT), "lower left", "JUST AVOID THE MAN-EATING INSECTS. AND THE POISONOUS PLANTS.")),
  R("anko", "env_forest_of_death"), "medium"),

 ("p08", dict(scene="action", light="day", cast="crowd", mood="tense", panels=6),
  FILL + ANK.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(COAT, BOY, UCH, GIRL, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a signed waiver being handed over. Hands and paper only.\n"
  "PANEL 2 (small): a curtained booth, a scroll passed through a slot. No faces.\n"
  "PANEL 3 (small): the blond boy's gloved hand closing round a scroll. Hand only.\n"
  "PANEL 4 (dominant, middle): the teams dispersing along the fence line to their separate gates, "
  "drawn small and scattered across a very wide view of the perimeter, the black forest towering "
  "over all of them.\n"
  "PANEL 5 (small): the woman in the tan coat alone, watching them go.\n"
  "PANEL 6 (wide, bottom): her face in close-up, grinning like something is funny. " + L_FOREST
  + SAY((6, COAT, "upper right", "LAST PIECE OF ADVICE — TRY NOT TO DIE!")),
  R("anko", "naruto_13_sword", "env_forest_of_death"), "high"),

 ("p09", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=5),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, UCH, GIRL) +
  "FIVE panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): a heavy chain and padlock on an iron gate. Objects only.\n"
  "PANEL 2 (small): the padlock falling open.\n"
  "PANEL 3 (small): three pairs of feet, braced.\n"
  "PANEL 4 (dominant, middle): the gate swinging inward and the three of them going through it, "
  "seen from INSIDE the forest looking back out — they are small silhouettes in a bright rectangle "
  "of gateway, and the enormous dark trunks crowd in around the frame from every side.\n"
  "PANEL 5 (wide, bottom): the gate shutting behind them, the light going. " + L_FOREST
  + SFX(4, "GOOON"),
  R("naruto_13_sword", "sasuke", "sakura", "env_forest_of_death"), "high"),

 ("p10", dict(scene="establishing", light="dark", cast="small_group", mood="somber", panels=4),
  FILL + ENV.format(i=1) + N13S.format(i=2) + ONLY(BOY, UCH, GIRL) +
  "FOUR panels only — the forest gets a full slow page to establish its scale. No dialogue.\n"
  "PANEL 1 (small): a shaft of pale light falling through the canopy onto nothing.\n"
  "PANEL 2 (small): something small moving in the undergrowth. Not resolvable.\n"
  "PANEL 3 (dominant, taking most of the page): the three of them drawn TINY at the base of a "
  "single tree trunk so vast it fills the whole panel and runs off all four edges — the roots alone "
  "are twice their height. Mist between the trunks, the canopy black overhead.\n"
  "PANEL 4 (wide, bottom): the forest floor stretching away in every direction, identical, "
  "trackless. " + L_FOREST,
  R("env_forest_of_death", "naruto_13_sword"), "high"),

 ("p11", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ONLY(BOY, UCH, GIRL) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): three figures running along a branch high above the ground, small and distant.\n"
  "PANEL 2 (small): the pink-haired girl's face, already labouring.\n"
  "PANEL 3 (small): her hand catching a branch to steady herself.\n"
  "PANEL 4 (dominant, middle): the blond boy and the dark-haired boy stopped ahead on a branch "
  "waiting, both large in the foreground cropped by the top edge, the girl small and far behind "
  "them at the bottom of the panel — the gap between them is the composition.\n"
  "PANEL 5 (small): the dark-haired boy's face, impatient.\n"
  "PANEL 6 (wide, bottom): the three of them stopped on a branch, the forest falling away below. "
  + L_FOREST
  + SAY((6, GIRL, "upper left", "WHAT ABOUT THE TENTS? IF WE DON'T REACH THE TOWER TODAY—"),
        (6, BOY, "lower right", "WE WILL MAKE IT.")),
  R("naruto_13_sword", "sasuke", "sakura"), "medium"),

 ("p12", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + SAS.format(i=1) + N13S.format(i=2) + SAK.format(i=3) + ONLY(UCH, BOY, GIRL) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a bundle of rolled canvas tents dumped on the ground. Objects only.\n"
  "PANEL 2 (small): the dark-haired boy's face, resenting the order and obeying it anyway.\n"
  "PANEL 3 (small): his hands in a seal, then at his mouth.\n"
  "PANEL 4 (dominant, middle): a broad flat sheet of fire pouring down onto the tents, drawn as "
  "FLAT OPAQUE ORANGE AND YELLOW SHAPES with hard black outlines — no glow, no wash. The three of "
  "them stand back at three different depths, the trunks behind still fully drawn and legible "
  "through and around the flame.\n"
  "PANEL 5 (small): the pink-haired girl's face lit from below.\n"
  "PANEL 6 (wide, bottom): black ash on the forest floor and the three of them already leaving "
  "frame at the top. " + L_FOREST
  + SAY((1, BOY, "upper left", "BURN THEM."))
  + SFX(4, "GOOO"),
  R("sasuke", "naruto_13_sword", "sakura"), "high"),

 ("p13", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, UCH, GIRL) +
  "SIX panels, uneven. Escalate by cropping tighter.\n"
  "PANEL 1 (small): the three of them running along a high branch, from behind.\n"
  "PANEL 2 (small): the blond boy's foot planting hard, stopping dead.\n"
  "PANEL 3 (small): the other two overshooting and turning back.\n"
  "PANEL 4 (narrow letterbox): the blond boy's single visible eye, cropped by all four edges.\n"
  "PANEL 5 (dominant, middle): the three of them motionless on the branch, drawn small and low in "
  "the panel, with the enormous empty forest canopy filling everything above and around them — and "
  "nothing visible in it. The emptiness is the threat.\n"
  "PANEL 6 (wide, bottom): the leaves overhead, absolutely still. " + L_FOREST
  + SAY((4, BOY, "upper left", "SOMEONE STRONG IS FOLLOWING US.")),
  R("naruto_13_sword", "sasuke", "sakura", "env_forest_of_death"), "high"),

 ("p14", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=5),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ONLY(BOY, UCH, GIRL) +
  "FIVE panels, uneven, violent diagonals. No dialogue on this page.\n"
  "PANEL 1 (narrow letterbox): the forest bending — every leaf and branch laid flat in one "
  "direction. No figures.\n"
  "PANEL 2 (dominant, middle): all three of them thrown off the branch and hurled backwards through "
  "the air, limbs loose, at three clearly different depths and scales, one of them cropped by the "
  "panel edge — with the wind drawn as flat opaque hard-edged sheets layered in front of and behind "
  "them. No injury detail.\n"
  "PANEL 3 (small): a hand skidding down bark, tearing at it.\n"
  "PANEL 4 (small): the pink-haired girl slammed against a trunk. Flat impact shapes, no injury "
  "detail.\n"
  "PANEL 5 (wide, bottom): the three of them scattered on the forest floor, the branch they were on "
  "stripped bare far above. " + L_FOREST
  + SFX(2, "GOUUU", "It crosses the gutter into the panel below."),
  R("naruto_13_sword", "sasuke", "sakura"), "high"),

 ("p15", dict(scene="emotional_closeup", light="dark", cast="small_group", mood="tense", panels=5),
  FILL + KUSA.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(HAT, BOY, UCH, GIRL) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): a straw hat brim, from below. No face visible under it.\n"
  "PANEL 2 (small): bare white feet settling onto a branch without a sound.\n"
  "PANEL 3 (dominant, middle): the ninja in the straw hat standing high on a branch above them, "
  "seen from the forest floor at a steep low angle so the figure is small against an enormous "
  "canopy — utterly still, the long black hair hanging. The three genin are cropped huge and dark "
  "along the bottom edge of the panel, out of focus of the composition.\n"
  "PANEL 4 (small): the hat brim tipping up a fraction. Still no eyes.\n"
  "PANEL 5 (wide, bottom): the three of them looking up, tiny. " + L_FOREST,
  R("kusa_nin", "naruto_13_sword", "env_forest_of_death"), "high"),

 ("p16", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + SAK.format(i=1) + SAS.format(i=2) + KUSA.format(i=3) + ONLY(GIRL, UCH, HAT, BOY) +
  "SIX panels, uneven. This page is PRESSURE, not violence — nobody is touched on it.\n"
  "PANEL 1 (small): the pink-haired girl down on both knees, hands flat in the dirt.\n"
  "PANEL 2 (small): her eyes, blown wide, seeing something that is not there.\n"
  "PANEL 3 (dominant, middle): what she is seeing — an inset drawn with a ragged torn-paper border, "
  "in flat black and white with no colour at all: her own small figure standing alone in an empty "
  "white void with an enormous black shape closing over her from above. No injury, no blood, no "
  "detail — just the shape.\n"
  "PANEL 4 (small): the dark-haired boy on one knee, teeth clenched, unable to stand.\n"
  "PANEL 5 (small): his hand shaking on the ground.\n"
  "PANEL 6 (wide, bottom): the three of them pinned to the forest floor, and the small still figure "
  "on the branch above doing nothing at all. " + L_FOREST
  + SFX(3, "ZUUN"),
  R("sakura", "sasuke", "kusa_nin"), "high"),

 ("p17", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=6),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ONLY(BOY, HAT, UCH, GIRL) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): sweat running down the blond boy's jaw. No eyes.\n"
  "PANEL 2 (small): his hand, opening and closing once.\n"
  "PANEL 3 (small): his foot, sliding forward. He is standing up.\n"
  "PANEL 4 (dominant, middle): the blond boy ON HIS FEET among his two kneeling teammates, seen "
  "from a low angle, the only upright figure in the panel — looking straight up at the branch. His "
  "expression is not defiance. It is assessment.\n"
  "PANEL 5 (small): the straw hat brim tipping further back, amused.\n"
  "PANEL 6 (wide, bottom): the two of them, far apart, the forest between. " + L_FOREST
  + SAY((6, HAT, "upper right", "OH. YOU SHOOK IT OFF.")),
  R("naruto_13_sword", "kusa_nin"), "high"),

 ("p18", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=4),
  FILL + KUSA.format(i=1) + N13S.format(i=2) + ONLY(HAT, BOY) +
  "FOUR panels only. The reveal gets room.\n"
  "PANEL 1 (small): the hat lifting clear of the face.\n"
  "PANEL 2 (dominant, taking most of the page): the face beneath it in close-up — chalk-white skin, "
  "GOLDEN-YELLOW EYES WITH VERTICAL BLACK SLIT PUPILS, purple markings around them, and a long thin "
  "tongue extended out and curling right around the outside of the mouth. Cropped very tight, hard "
  "parallel hatch lines, flat black behind. Nothing else on the page competes with it.\n"
  "PANEL 3 (small): the blond boy's single visible eye — and for the first time in the volume there "
  "is something in it.\n"
  "PANEL 4 (wide, bottom): the two of them, the branch, the forest floor. " + L_FOREST,
  R("kusa_nin", "naruto_13_sword"), "high"),

 ("p19", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + KUSA.format(i=1) + SAS.format(i=2) + N13S.format(i=3) + ONLY(HAT, UCH, BOY, GIRL) +
  "SIX panels, uneven, violent diagonals.\n"
  "PANEL 1 (small): the figure on the branch simply gone — the empty branch, hard speed lines.\n"
  "PANEL 2 (small): the dark-haired boy driving a kunai into his own thigh to break the pressure. "
  "Show the hand, the blade and the leg only, from behind, with flat impact shapes and NO injury "
  "detail and no red.\n"
  "PANEL 3 (dominant, middle): the dark-haired boy hurling himself sideways off the ground as the "
  "pale figure lands exactly where he was, both bodies drawn at very different scales with the "
  "figure huge in the foreground cropped by the right edge. Flat opaque impact shapes.\n"
  "PANEL 4 (small): the dark-haired boy landed on a branch, breathing hard, red eyes with two comma "
  "marks.\n"
  "PANEL 5 (small): the pale figure's face, turning, pleased.\n"
  "PANEL 6 (wide, bottom): the clearing, the three of them scattered wide apart now. " + L_FOREST
  + SFX(3, "DOGAN"),
  R("kusa_nin", "sasuke", "naruto_13_sword"), "high"),

 ("p20", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + SNAKE.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(BOY) +
  "FIVE panels, uneven. There are no other people on this page — only the boy and the animal.\n"
  "PANEL 1 (small): the forest floor beside the blond boy's feet, buckling upward.\n"
  "PANEL 2 (small): a single enormous golden eye with a vertical black slit pupil, cropped by all "
  "four edges. Nothing else visible.\n"
  "PANEL 3 (dominant, middle): a COLOSSAL serpent rearing up out of the undergrowth, its body thick "
  "as a tree trunk coiling off all four edges of the panel, head drawn back to strike — and the "
  "blond boy TINY at the bottom of the panel, looking up at it. Overwhelming scale difference.\n"
  "PANEL 4 (small): his hand closing on the sword hilt over his shoulder.\n"
  "PANEL 5 (wide, bottom): the serpent's open mouth filling the whole panel from the side, fangs "
  "curved, and one small dark figure leaping clear at the very edge of frame. No injury detail. "
  + L_FOREST
  + SFX(3, "SHAAA"),
  R("giant_snake", "naruto_13_sword", "env_forest_of_death"), "high"),

 ("p21", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + SNAKE.format(i=2) + ONLY(BOY) +
  "FIVE panels, uneven, hard diagonals. Nobody else on this page.\n"
  "PANEL 1 (small): the blade clearing the scabbard. Hands and steel only.\n"
  "PANEL 2 (small): the blade edge going pale white as air tears along it, drawn as flat hard-edged "
  "shapes, not a glow.\n"
  "PANEL 3 (dominant, middle): the blond boy landed on top of the serpent's head, one hand braced "
  "in the scales, the sword driven down two-handed — the head enormous and filling most of the "
  "panel, the boy small on top of it, the whole thing at a steep diagonal. Flat opaque impact "
  "shapes with hard black outlines, motion lines, and NO injury detail, no red.\n"
  "PANEL 4 (small): the serpent's head slamming through a tree trunk, the trunk shearing. No "
  "figures.\n"
  "PANEL 5 (wide, bottom): the boy landing in a crouch on the forest floor, the serpent's coils "
  "still moving behind him across the whole width of the panel. " + L_FOREST
  + SFX(3, "ZAN"),
  R("naruto_13_sword", "giant_snake"), "high"),

 ("p22", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=4),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ENV.format(i=3) + ONLY(BOY, HAT) +
  "FOUR panels only. This is the last page of VOLUME TWO and it ends on his face.\n"
  "PANEL 1 (small): the serpent's coils, far off, going still.\n"
  "PANEL 2 (small): the pale figure watching from a branch high above, small, arms folded, "
  "delighted.\n"
  "PANEL 3 (small): blood-flecked leaves settling. Leaves only, no bodies, no injury detail.\n"
  "PANEL 4 (dominant, taking most of the page): the blond boy in close-up, cropped very tight — "
  "hair hanging, the sword still out and low, the forest black behind him. And he is SMILING. Not "
  "the small warm one he gave Shikamaru: a thin, private, entirely wrong smile, the first thing in "
  "two volumes that he has actually wanted. Hard radiating lines, flat black shadow. No dialogue "
  "anywhere on this page. " + L_FOREST,
  R("naruto_13_sword", "kusa_nin", "env_forest_of_death"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v2ch07" / "raw", HERE / "v2ch07" / "ledger.json")
