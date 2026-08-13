"""Volume 3, Chapter 1 — "Amaterasu". 22 pages.

Source: fic ch5, opening. Picks up mid-breath from Volume 2's last page.

The chapter has a twist the reader must be able to reconstruct on a reread: the Naruto being
thrown around for the first half is a CLONE. The real one is in the trees with his Sharingan
active, spending a shadow clone to measure an opponent — and even so, what he measures is that
he is outclassed. So p14 has to land cleanly, and pages 4-13 have to be stageable both ways.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ENV, FILL, N13S, ONLY, OFF, ORO, R, SAK, SAS, SAY, SFX,     # noqa: E402
                     TITLE,
                     BOY, GIRL, PALEONE, UCH)

KUSA = ("Image {i} is the CHARACTER REFERENCE for the ninja in the straw hat: tall and slender, a "
        "wide conical straw hat, a long earth-brown robe over a dark bodysuit, very long straight "
        "black hair past the waist, unnaturally pale white skin, GOLDEN-YELLOW EYES WITH VERTICAL "
        "SLIT PUPILS and purple markings around them. Reproduce exactly; ignore its white "
        "background and layout. ")
HAT = "the ninja in the straw hat"
L_FOREST = "Lighting: sunless green-black gloom under a dense canopy, hard shafts of pale light. "
SHAR = ("Whenever the blond boy's eye is shown red it is BLOOD-RED with three black comma-shaped "
        "marks around the pupil, and when it is shown changed it carries a black three-bladed "
        "pinwheel pattern instead. ")

PAGES = [
 ("p01", dict(scene="establishing", light="dark", cast="solo", mood="tense", panels=1),
  ORO.format(i=1) + ONLY(PALEONE) +
  "CHAPTER OPENING SPLASH. The pale one stands halfway up the trunk of a colossal forest tree, "
  "walking on the bark as though it were the floor, seen from far below at a steep angle so the "
  "trunk runs from the bottom of the paper up and off the top right. The figure is small and well "
  "off centre, chalk-white against black bark, the long black hair falling straight down. A great "
  "curving root fills the lower left as the foreground mass, cropped by the edge of the paper. "
  "Coils of an enormous serpent lie slack across the forest floor far below, tiny. Leave the pale "
  "shaft of canopy light at the upper left broad and quiet. "
  "Lighting: green-black gloom, one hard shaft of pale light picking out the white skin. "
  + TITLE("AMATERASU", "pale shaft of light at the upper left"),
  R("orochimaru", "env_forest_of_death"), "high"),

 ("p02", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ENV.format(i=3) + ONLY(BOY, HAT) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): the blond boy's sword lowering, still out.\n"
  "PANEL 2 (small): the straw hat, tipped fully back now, the golden slit eyes plain.\n"
  "PANEL 3 (dominant, middle): the two of them facing each other across the forest floor at very "
  "different depths — the ninja in the straw hat large in the left foreground cropped by the edge, "
  "the blond boy small and squared-off far across the clearing, the serpent's slack coils lying "
  "between them.\n"
  "PANEL 4 (small): the boy's single visible eye.\n"
  "PANEL 5 (small): the pale figure's mouth, curling.\n"
  "PANEL 6 (wide, bottom): the clearing, the two of them, the trees vast above. " + L_FOREST
  + SAY((4, BOY, "upper left", "WHO ARE YOU?"),
        (6, HAT, "upper right", "I AM THE ONE WHO SHOULD BE ASKING QUESTIONS, NARUTO-KUN.")),
  R("naruto_13_sword", "kusa_nin", "env_forest_of_death"), "high"),

 ("p03", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ONLY(BOY, HAT) +
  "SIX panels, uneven, hard diagonals.\n"
  "PANEL 1 (small): the boy's foot driving off the ground, dirt thrown up in flat opaque shapes.\n"
  "PANEL 2 (small): the pale figure's face, delighted, not moving.\n"
  "PANEL 3 (dominant, middle): the boy mid-air with a fist thrown, the pale figure leaning back "
  "away from it by a hand's width — both drawn at the same scale for once, the punch crossing the "
  "whole panel on a hard diagonal, hard speed lines behind.\n"
  "PANEL 4 (small): a foot swinging up as a follow-up.\n"
  "PANEL 5 (small): a chalk-white hand catching the ankle without effort. Hands and ankle only.\n"
  "PANEL 6 (wide, bottom): the two of them locked, the boy off balance. " + L_FOREST
  + SFX(3, "SHUN"),
  R("naruto_13_sword", "kusa_nin"), "high"),

 ("p04", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ONLY(BOY, HAT) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the boy's other fist already coming round while his ankle is still held.\n"
  "PANEL 2 (dominant, middle): the punch landing square on the pale figure's cheek and sending it "
  "off its feet — flat opaque impact shapes with hard black outlines, no injury detail. The pale "
  "figure is large in the foreground cropped by the right edge; the boy is small and low, driving "
  "up from the ground.\n"
  "PANEL 3 (small): the pale figure skidding backwards through leaf litter.\n"
  "PANEL 4 (small): the boy landing, breathing steadily, unimpressed with himself.\n"
  "PANEL 5 (wide, bottom): the clearing, the distance between them reopened. " + L_FOREST
  + SFX(2, "DOGO"),
  R("naruto_13_sword", "kusa_nin"), "high"),

 ("p05", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + KUSA.format(i=1) + N13S.format(i=2) + ONLY(HAT, BOY) +
  "SIX panels, uneven. The exchange reverses on this page and the reader should feel it.\n"
  "PANEL 1 (small): the pale figure straightening up. The head is turned too far round on the neck.\n"
  "PANEL 2 (small): a chalk-white fist coming straight at camera.\n"
  "PANEL 3 (small): the boy's crossed forearms taking it, driven back a step.\n"
  "PANEL 4 (dominant, middle): a full kick landing in the boy's chest and folding him around it, "
  "the pale figure enormous in the foreground cropped by the left edge, the boy small and already "
  "leaving the ground. Flat opaque impact shapes, motion lines, no injury detail.\n"
  "PANEL 5 (small): a tree trunk splintering as he hits it.\n"
  "PANEL 6 (wide, bottom): the boy at the foot of the tree, on one knee, head down. " + L_FOREST
  + SFX(4, "DOGAAN"),
  R("kusa_nin", "naruto_13_sword"), "high"),

 ("p06", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=6),
  FILL + KUSA.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + ONLY(HAT, BOY, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): chalk-white feet stopping in front of a kneeling figure. Feet only.\n"
  "PANEL 2 (dominant, upper): the pale figure standing over the boy, seen from ground level behind "
  "the boy's shoulder so the shoulder is cropped huge and dark in the foreground and the figure "
  "towers into the canopy.\n"
  "PANEL 3 (small): a fist driven into his stomach. Torso and fist only, no faces, flat impact "
  "shapes, no injury detail.\n"
  "PANEL 4 (small): the boy on both knees now, one arm across his middle.\n"
  "PANEL 5 (small): the dark-haired boy watching from cover, eyes enormous — he has never seen "
  "this happen.\n"
  "PANEL 6 (wide, bottom): the clearing from above, the boy down, the pale figure already turning "
  "away from him. " + L_FOREST
  + SAY((2, HAT, "upper left", "YOU ARE BETTER THAN SASUKE-KUN."),
        (2, HAT, "lower right", "BUT I HAVE NO INTEREST IN YOU. AT THE MOMENT.")),
  R("kusa_nin", "naruto_13_sword", "sasuke"), "high"),

 ("p07", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + KUSA.format(i=2) + SAK.format(i=3) + ONLY(UCH, HAT, GIRL, BOY) +
  "SIX panels, uneven. Escalate by cropping tighter.\n"
  "PANEL 1 (small): the dark-haired boy's hands, shaking on the bark.\n"
  "PANEL 2 (small): his face, close — this is fear, not anger.\n"
  "PANEL 3 (small): the pink-haired girl behind him with both hands over her mouth.\n"
  "PANEL 4 (dominant, middle): the pale figure walking toward the dark-haired boy down a long "
  "avenue of trunks, small and unhurried in the middle of the panel, the dark-haired boy cropped "
  "huge and out of focus of the composition in the foreground. The distance closing is the whole "
  "panel.\n"
  "PANEL 5 (small): the golden slit eyes, close.\n"
  "PANEL 6 (wide, bottom): the forest floor, the two of them, and the blond boy still down at the "
  "far edge of frame. " + L_FOREST
  + SAY((5, HAT, "upper right", "NOW. SASUKE-KUN. SHALL WE CONTINUE WHERE WE LEFT OFF?")),
  R("sasuke", "kusa_nin", "sakura"), "high"),

 ("p08", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + KUSA.format(i=2) + ONLY(UCH, HAT) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy's eyes — blood-red with two black comma marks — snapping "
  "wide.\n"
  "PANEL 2 (small): a kunai pulled from a hip pouch. Hand and blade only.\n"
  "PANEL 3 (dominant, middle): the dark-haired boy driving the kunai into the pale figure's "
  "shoulder from behind — and the whole body already crumbling from the point of contact outward "
  "into flat grey dust and flakes, drawn as hard-edged shapes. No injury, no red, no wound: it is "
  "simply coming apart like ash.\n"
  "PANEL 4 (small): his face, uncomprehending — his red eyes did not see it.\n"
  "PANEL 5 (small): a chalk-white hand appearing at the edge of frame behind his head.\n"
  "PANEL 6 (wide, bottom): the dark-haired boy hurled the length of the panel into a trunk. Flat "
  "impact shapes, no injury detail. " + L_FOREST
  + SFX(3, "SARA"),
  R("sasuke", "kusa_nin"), "high"),

 ("p09", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ONLY(BOY, HAT, UCH) +
  "FIVE panels, uneven. Nobody sees this happen except the reader.\n"
  "PANEL 1 (small): the blond boy's hand flat on the forest floor, pushing up.\n"
  "PANEL 2 (small): his head coming up, the long bang hanging over the right side of his face.\n"
  "PANEL 3 (narrow letterbox): his ONE visible eye — and it has gone BLOOD-RED with three black "
  "comma marks around the pupil. Cropped by all four edges, flat black behind it. " + SHAR + "\n"
  "PANEL 4 (dominant, middle): the boy standing alone among the trunks with both hands rising into "
  "a seal, small in a very large panel, the forest enormous and dark around him. Hard radiating "
  "lines converge on him.\n"
  "PANEL 5 (wide, bottom): the pale figure at the far side of the clearing, beginning to turn its "
  "head back toward him. " + L_FOREST,
  R("naruto_13_sword", "kusa_nin"), "high"),

 ("p10", dict(scene="action", light="dark", cast="two", mood="tense", panels=4),
  FILL + N13S.format(i=1) + KUSA.format(i=2) + ONLY(BOY, HAT) +
  "FOUR panels only. This is the page the chapter is named for and it gets the room.\n"
  "PANEL 1 (small): the blond boy's red eye in extreme close-up, the three comma marks spinning "
  "together into a single BLACK THREE-BLADED PINWHEEL shape across the iris. Cropped by all four "
  "edges. " + SHAR + "\n"
  "PANEL 2 (narrow letterbox): the air between them, empty, hard speed lines converging.\n"
  "PANEL 3 (dominant, taking most of the page): BLACK FLAME erupting over the pale figure — drawn "
  "as FLAT, OPAQUE, PURE BLACK hard-edged flame shapes with stark white outlines, layered in front "
  "of and behind the body, climbing the trunks. It does not glow and it does not wash the scene "
  "out: the trees, the ground and the boy all stay fully drawn and legible through and around it. "
  "The boy is small at the bottom edge, one hand still extended.\n"
  "PANEL 4 (wide, bottom): the flame reflected in the boy's single visible eye. " + L_FOREST
  + SFX(3, "GOOOO"),
  R("naruto_13_sword", "kusa_nin"), "high"),

 ("p11", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + KUSA.format(i=1) + ORO.format(i=2) + ONLY(HAT, PALEONE, BOY) +
  "SIX panels, uneven. Something comes out of something else, and it must read clearly.\n"
  "PANEL 1 (small): the black flame shapes eating downward through a shoulder.\n"
  "PANEL 2 (small): the burning figure toppling sideways, still silent.\n"
  "PANEL 3 (small): the figure's mouth opening far, far wider than a jaw allows.\n"
  "PANEL 4 (dominant, middle): a WHOLE UNDAMAGED PERSON rising out of that open mouth head-first — "
  "chalk-white skin, long straight black hair, golden slit eyes, a cream-grey robe — while the "
  "burning husk collapses away beneath them in flat black flame shapes. Seen from a low angle. No "
  "injury detail, no red, no gore: the husk is drawn like a shed skin, papery and empty.\n"
  "PANEL 5 (small): the empty straw hat lying in the leaf litter, burning. Object only.\n"
  "PANEL 6 (wide, bottom): the new figure standing whole in the clearing, the black flame guttering "
  "behind them. " + L_FOREST,
  R("kusa_nin", "orochimaru"), "high"),

 ("p12", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + ORO.format(i=2) + ONLY(BOY, PALEONE) +
  "FIVE panels, uneven. THE TWIST: the one who has been taking the beating was never the real one.\n"
  "PANEL 1 (small): the blond boy standing in the clearing, one hand still out — and he is coming "
  "apart, the edges of him breaking into flat white smoke.\n"
  "PANEL 2 (dominant, middle): a SECOND blond boy, completely unmarked, crouched on a high branch "
  "well above the clearing with his red eye still active, seen from below — while the white smoke "
  "of the first one disperses among the trunks far beneath him. Both are clearly the same boy. The "
  "vertical distance between them is the whole composition.\n"
  "PANEL 3 (small): his red eye closing, and opening plain blue again. " + SHAR + "\n"
  "PANEL 4 (small): the pale one's face below, looking up — genuinely interested for the first "
  "time.\n"
  "PANEL 5 (wide, bottom): the boy dropping down to the forest floor to stand facing him. "
  + L_FOREST
  + SFX(1, "POFU"),
  R("naruto_13_sword", "orochimaru"), "high"),

 ("p13", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + ORO.format(i=2) + ONLY(BOY, PALEONE) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the boy's sandals landing in leaf litter. Feet only.\n"
  "PANEL 2 (small): his face, level, giving away nothing about what he just spent.\n"
  "PANEL 3 (dominant, middle): the pale one in close-up, cropped tight — chalk-white skin, golden "
  "slit eyes, the long black hair. The smile has gone. This is the face of someone doing "
  "arithmetic. Hard parallel hatch lines, flat black behind.\n"
  "PANEL 4 (small): the boy's mouth, flat, saying the name.\n"
  "PANEL 5 (wide, bottom): the two of them alone in the clearing, the burnt husk between them. "
  + L_FOREST
  + SAY((4, BOY, "upper left", "OROCHIMARU.")),
  R("naruto_13_sword", "orochimaru"), "high"),

 ("p14", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + ORO.format(i=1) + N13S.format(i=2) + ONLY(PALEONE, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pale one's golden eyes narrowing.\n"
  "PANEL 2 (small): a chalk-white hand touching a shoulder where the robe is burnt through to bare "
  "unmarked skin. No injury detail.\n"
  "PANEL 3 (dominant, middle): the two of them squared off at very different scales — the pale one "
  "large in the foreground cropped by the left edge, the boy small and central beyond, the black "
  "scorch mark up the trunks behind them both.\n"
  "PANEL 4 (small): the boy's blue eye. Nothing in it.\n"
  "PANEL 5 (small): the pale one's smile returning, worse than before.\n"
  "PANEL 6 (wide, bottom): the clearing, the two of them, the trees. " + L_FOREST
  + SAY((1, PALEONE, "upper left", "BLACK FLAME. THAT IS NOT A JUTSU A GENIN HAS."),
        (3, PALEONE, "upper right", "THAT IS NOT A JUTSU ANYONE HAS — WITHOUT A VERY PARTICULAR PAIR OF EYES."),
        (6, BOY, "upper left", "WHAT IS AN S-RANK CRIMINAL DOING IN A CHUNIN EXAM?")),
  R("orochimaru", "naruto_13_sword"), "high"),

 ("p15", dict(scene="emotional_closeup", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + SAK.format(i=1) + ORO.format(i=2) + SAS.format(i=3) + ONLY(GIRL, PALEONE, UCH, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pink-haired girl's face, going through recognition in stages.\n"
  "PANEL 2 (small): her hands, gripping the roots she is hiding behind.\n"
  "PANEL 3 (dominant, middle): the girl very small at the bottom of a mostly empty panel, crouched "
  "among enormous roots, with the whole black-green forest towering into nothing above her. Her "
  "scale in the frame is the point.\n"
  "PANEL 4 (small): the dark-haired boy slumped against a trunk, watching, unable to stand.\n"
  "PANEL 5 (small): the pale one's back, unbothered by either of them.\n"
  "PANEL 6 (wide, bottom): the clearing, all four of them at four depths. " + L_FOREST
  + SAY((1, GIRL, "upper left", "ONE OF THE THREE SANNIN..."),
        (3, GIRL, "upper right", "WE'RE GENIN. WE'RE ROOKIES.")),
  R("sakura", "orochimaru", "sasuke"), "medium"),

 ("p16", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + ORO.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + ONLY(PALEONE, BOY, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pale one's head turning away from the blond boy toward the dark-haired one.\n"
  "PANEL 2 (small): the dark-haired boy's face, seen past a chalk-white shoulder.\n"
  "PANEL 3 (small): the blond boy's eye, tracking where the pale one is looking.\n"
  "PANEL 4 (dominant, middle): the pale one large in the frame with the dark-haired boy small and "
  "slumped beyond him — and the blond boy at the very edge of the panel, cropped, being looked "
  "past. The composition is about who is NOT being looked at.\n"
  "PANEL 5 (small): the blond boy's mouth, flat, working it out.\n"
  "PANEL 6 (wide, bottom): the three of them, the clearing. " + L_FOREST
  + SAY((1, PALEONE, "upper left", "YOU ARE PROVING TO BE AN INTERESTING GENIN, NARUTO-KUN."),
        (4, PALEONE, "upper right", "BUT AS I SAID. YOU ARE NOT WHAT I CAME FOR."),
        (6, BOY, "upper left", "UCHIHA SASUKE."),
        (6, BOY, "lower right", "WHAT DOES A SANNIN WANT WITH SASUKE?")),
  R("orochimaru", "naruto_13_sword", "sasuke"), "high"),

 ("p17", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + ORO.format(i=1) + N13S.format(i=2) + ONLY(PALEONE, BOY) +
  "SIX panels, uneven, violent diagonals. From here the boy is fighting for real and losing.\n"
  "PANEL 1 (small): the pale one simply gone from where he stood — empty leaf litter, hard speed "
  "lines.\n"
  "PANEL 2 (small): the boy already leaving the ground for a branch.\n"
  "PANEL 3 (dominant, middle): the pale one arriving in front of him IN MID-AIR with an uppercut "
  "thrown, both of them off the ground among the trunks at a steep diagonal, the boy twisting away "
  "from it by inches. Hard speed lines, flat opaque shapes.\n"
  "PANEL 4 (small): the boy's knee coming up to block a kick.\n"
  "PANEL 5 (small): the same knee blocking a second kick from the other side.\n"
  "PANEL 6 (wide, bottom): the two of them trading blows along a branch, drawn small and far off "
  "with the enormous forest around them. " + L_FOREST
  + SAY((3, PALEONE, "upper left", "HAD IT NOT BEEN FOR SASUKE, I WOULD CERTAINLY BE INTERESTED IN YOU.")),
  R("orochimaru", "naruto_13_sword"), "high"),

 ("p18", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + ORO.format(i=1) + N13S.format(i=2) + ONLY(PALEONE, BOY) +
  "FIVE panels, uneven, hard diagonals. Nothing on this page goes his way.\n"
  "PANEL 1 (small): a knee driven into his stomach, torso only, flat impact shapes, no injury "
  "detail.\n"
  "PANEL 2 (small): his head snapping sideways from a punch. Face turned away from camera.\n"
  "PANEL 3 (dominant, middle): a full spinning roundhouse kick catching him at the temple and "
  "throwing him clear across the panel into the trunks, the pale one enormous and mid-rotation in "
  "the foreground cropped by the right edge, the boy small and loose-limbed. Flat opaque impact "
  "shapes, motion lines, no injury detail.\n"
  "PANEL 4 (small): bark exploding off a trunk. No figures.\n"
  "PANEL 5 (wide, bottom): the boy face down in the leaf litter, not moving. " + L_FOREST
  + SFX(3, "DOGAAN"),
  R("orochimaru", "naruto_13_sword"), "high"),

 ("p19", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + ORO.format(i=2) + ONLY(UCH, PALEONE, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy pushing off a trunk, red eyes lit.\n"
  "PANEL 2 (small): his fist thrown at a chalk-white face.\n"
  "PANEL 3 (small): a chalk-white hand closing round that fist and holding it still.\n"
  "PANEL 4 (dominant, middle): the pale one holding the dark-haired boy up by one arm with the "
  "boy's feet off the ground, seen from a low angle — huge, patient, unhurried, the boy small and "
  "kicking. Flat opaque shapes, no injury detail.\n"
  "PANEL 5 (small): the dark-haired boy's face gripped in one hand, only the eyes showing between "
  "the fingers.\n"
  "PANEL 6 (wide, bottom): the dark-haired boy thrown the length of the panel into the trees. "
  + L_FOREST,
  R("sasuke", "orochimaru"), "high"),

 ("p20", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + ORO.format(i=2) + ONLY(BOY, PALEONE) +
  "FIVE panels, uneven. He gets up when nobody expects him to, and it buys him one hit.\n"
  "PANEL 1 (small): one gloved hand closing in the leaf litter. Hand only.\n"
  "PANEL 2 (small): the pale one walking away, not looking back.\n"
  "PANEL 3 (dominant, middle): the boy arriving from off-frame at full speed and putting a foot "
  "into the side of the pale one's face — the kick crossing the whole panel on a hard diagonal, the "
  "pale one's head snapped round, genuine surprise on it for the first time. Flat opaque impact "
  "shapes, hard speed lines, no injury detail.\n"
  "PANEL 4 (small): the pale one skidding sideways through the leaf litter.\n"
  "PANEL 5 (wide, bottom): the boy landed in a crouch, breathing hard, everything costing him. "
  + L_FOREST
  + SFX(3, "BAKI"),
  R("naruto_13_sword", "orochimaru"), "high"),

 ("p21", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + ORO.format(i=1) + N13S.format(i=2) + ONLY(PALEONE, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pale one's face turning back, the smile wider than ever.\n"
  "PANEL 2 (small): the boy charging in again.\n"
  "PANEL 3 (small): a knee meeting him at the stomach, mid-charge. Torso and knee only, flat impact "
  "shapes, no injury detail.\n"
  "PANEL 4 (dominant, middle): the pale one holding the boy's whole head in one hand and driving "
  "him down into the ground, the impact throwing a ring of flat opaque debris shapes outward, a "
  "shallow crater opening. Seen from a low angle. No injury detail, no red.\n"
  "PANEL 5 (small): the boy's hand, open in the dirt, fingers slack.\n"
  "PANEL 6 (wide, bottom): the crater, the boy in it, the pale one standing over. " + L_FOREST
  + SAY((1, PALEONE, "upper left", "YOU DID WELL, NARUTO-KUN. CATCHING ME OFF GUARD LIKE THAT."))
  + SFX(4, "DOGON"),
  R("orochimaru", "naruto_13_sword"), "high"),

 ("p22", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=4),
  FILL + N13S.format(i=1) + ORO.format(i=2) + ONLY(BOY, PALEONE) +
  "FOUR panels only. The chapter ends on the worst thing that has happened to him: being "
  "dismissed.\n"
  "PANEL 1 (small): a chalk-white hand releasing his collar and letting him drop.\n"
  "PANEL 2 (small): the pale one already walking away, seen from ground level, from behind.\n"
  "PANEL 3 (narrow letterbox): the boy's single visible eye at ground level in the dirt, open, "
  "furious, and completely unable to do anything. Cropped by all four edges.\n"
  "PANEL 4 (dominant, bottom): the whole clearing from high above — the boy a small dark shape "
  "face-down in a crater at the bottom of the panel, the pale one small and unhurried walking away "
  "toward the far trees, and the enormous forest swallowing both of them. " + L_FOREST
  + SAY((2, PALEONE, "upper right", "STAY DOWN, NARUTO-KUN."),
        (4, OFF(PALEONE), "upper left", "SASUKE-KUN IS WAITING FOR ME.")),
  R("naruto_13_sword", "orochimaru"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch01" / "raw", HERE / "v3ch01" / "ledger.json")
