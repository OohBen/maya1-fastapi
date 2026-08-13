"""Volume 3, Chapter 5 — "Fate". 14 pages.

Source: fic ch5, Neji vs Hinata. The one chapter of the volume Naruto is not in the middle of.
He watches it, and it is the only thing in three volumes that visibly reaches him — which is
why he gets exactly four panels in it and none of them have dialogue.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ENV, FILL, HAY, HIN, N13, NEJ, ONLY, OFF, R, SAY, SFX,      # noqa: E402
                     TITLE, BOY, FATE, PALE, SICK)

HALL = "Lighting: cold flat overhead light on grey stone, long hard shadows. "
CROWD = "the other genin and their jonin instructors watching from the balconies, none of them named"
EYES = ("Whenever either of them activates their eyes, the pale pupil-less eyes stay pale and the "
        "VEINS AROUND THE TEMPLES AND EYE SOCKETS BULGE OUT hard and dark. No colour change, no "
        "glow. ")

PAGES = [
 ("p01", dict(scene="establishing", light="interior", cast="two", mood="tense", panels=1),
  NEJ.format(i=1) + HIN.format(i=2) + ONLY(FATE, PALE) +
  "CHAPTER OPENING SPLASH. The two of them alone on the wide stone fighting floor, seen from very "
  "high above and slightly to one side — the long-haired boy standing squared and still in the "
  "lower right of the paper, the short-haired girl small and half-turned away at the far left, and "
  "an enormous expanse of bare grey floor between them taking up most of the page. Their two long "
  "shadows reach toward each other across it and do not meet. The corner of a balcony railing is "
  "the foreground mass, cropped by the upper left edge of the paper. Leave the pale empty floor at "
  "the lower left broad and quiet. "
  "Lighting: cold hard overhead light, two long hard shadows. "
  + TITLE("FATE", "pale empty floor at the lower left"),
  R("neji", "hinata"), "high"),

 ("p02", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + ENV.format(i=3) + ONLY(FATE, PALE, SICK, CROWD) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): the girl's hands, gripping the hem of her coat.\n"
  "PANEL 2 (small): the long-haired boy's face, pale eyes level and cold.\n"
  "PANEL 3 (dominant, middle): the two of them across the floor at very different depths — he is "
  "large in the right foreground cropped by the edge, she is small and far off and NOT in a stance, "
  "shoulders turned in on herself.\n"
  "PANEL 4 (small): her face, eyes down.\n"
  "PANEL 5 (small): the balcony above, faces at the railing.\n"
  "PANEL 6 (wide, bottom): the two of them, the floor, the shadows. " + HALL
  + SAY((2, FATE, "upper left", "FORFEIT THE MATCH, HINATA-SAMA."),
        (3, FATE, "upper right", "YOU CANNOT DEFEAT ME."),
        (6, FATE, "upper left", "YOU LACK CONFIDENCE. SOMEONE WITH NO CONFIDENCE IS FATED TO LOSE.")),
  R("neji", "hinata", "env_prelim_arena"), "high"),

 ("p03", dict(scene="emotional_closeup", light="interior", cast="two", mood="tense", panels=6),
  FILL + HIN.format(i=1) + NEJ.format(i=2) + ONLY(PALE, FATE, CROWD) + EYES +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): her fingers, poking together in front of her, the old habit.\n"
  "PANEL 2 (small): the fingers stopping.\n"
  "PANEL 3 (dominant, middle): the girl sliding into a full open-palmed stance, one hand forward "
  "and one back, seen from a low angle so she fills the frame for the first time — small, "
  "trembling, and doing it anyway. Hard radiating lines behind her.\n"
  "PANEL 4 (small): the long-haired boy's face, faintly insulted.\n"
  "PANEL 5 (small): her pale eyes, the veins standing out hard around them.\n"
  "PANEL 6 (wide, bottom): the two of them, both in stance now, mirrored. " + HALL
  + SAY((4, FATE, "upper left", "YOU DON'T LISTEN."),
        (6, FATE, "upper right", "THEN I WILL PROVE TO YOU THAT YOU ARE A LOSER AND ALWAYS WILL BE.")),
  R("hinata", "neji"), "high"),

 ("p04", dict(scene="action", light="interior", cast="two", mood="tense", panels=6),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + ONLY(FATE, PALE, CROWD) + EYES +
  "SIX panels, uneven, hard diagonals.\n"
  "PANEL 1 (small): two open palms colliding, hands and forearms only.\n"
  "PANEL 2 (small): a second pair, from the other side.\n"
  "PANEL 3 (dominant, middle): the two of them mid-exchange at the centre of the floor, both "
  "drawn at the same scale for once, arms crossing between them in a blur of hard motion lines and "
  "flat opaque impact shapes. Neither has the advantage in this panel. No injury detail.\n"
  "PANEL 4 (small): her feet skidding backwards on stone.\n"
  "PANEL 5 (small): her face, teeth set, still up.\n"
  "PANEL 6 (wide, bottom): the two of them apart again, breathing, the balconies watching. "
  + HALL
  + SFX(3, "TAN TAN TAN"),
  R("neji", "hinata"), "high"),

 ("p05", dict(scene="action", light="interior", cast="two", mood="tense", panels=5),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + ONLY(FATE, PALE, CROWD) +
  "FIVE panels, uneven. The gap opens on this page.\n"
  "PANEL 1 (small): the long-haired boy's foot planting, and the stone cracking under it.\n"
  "PANEL 2 (dominant, middle): a full kick landing in the girl's chest and lifting her clean off "
  "the floor — he is large in the left foreground cropped by the edge, she is small and already "
  "airborne and folded around it. Flat opaque impact shapes with hard black outlines, motion lines. "
  "No injury detail.\n"
  "PANEL 3 (small): her back hitting the stone.\n"
  "PANEL 4 (small): his face, not even slightly winded.\n"
  "PANEL 5 (wide, bottom): the girl on her hands and knees on the floor, small, and him standing "
  "over the distance not bothering to close it. " + HALL
  + SFX(2, "DOGA"),
  R("neji", "hinata"), "high"),

 ("p06", dict(scene="emotional_closeup", light="interior", cast="two", mood="tense", panels=6),
  FILL + HIN.format(i=1) + N13.format(i=2) + ONLY(PALE, BOY, FATE, CROWD) +
  "SIX panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): her palm flat on the stone, pushing.\n"
  "PANEL 2 (small): her knee coming under her.\n"
  "PANEL 3 (small): her face, hair hanging in it, getting up anyway.\n"
  "PANEL 4 (small): a balcony railing — and the blond boy's hands on it, gone tight.\n"
  "PANEL 5 (dominant, middle): the girl standing back up alone in the middle of the enormous empty "
  "floor, very small at the bottom of a panel that is nearly all bare grey stone and shadow.\n"
  "PANEL 6 (wide, bottom): the long-haired boy's face, watching her do it, and disliking it. "
  + HALL,
  R("hinata", "naruto_13"), "high"),

 ("p07", dict(scene="action", light="interior", cast="two", mood="tense", panels=4),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + ONLY(FATE, PALE, CROWD) +
  "FOUR panels only. The blow that ends it gets the room.\n"
  "PANEL 1 (small): his pale eyes, the veins hard around them, choosing a spot.\n"
  "PANEL 2 (narrow letterbox): the floor between them, empty, hard speed lines converging.\n"
  "PANEL 3 (dominant, taking most of the page): the open palm arriving flat against the centre of "
  "her chest — he is fully extended into it, she is lifted onto her toes with her head thrown back "
  "and her arms flung wide, both cropped by the panel edges, hard radiating lines exploding "
  "outward from the point of contact as flat opaque shapes. No injury detail, no red.\n"
  "PANEL 4 (wide, bottom): the girl folded down onto her knees on the stone, head down, one hand "
  "at her chest. " + HALL
  + SFX(3, "DOOON"),
  R("neji", "hinata"), "high"),

 ("p08", dict(scene="dialogue", light="interior", cast="two", mood="somber", panels=6),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + HAY.format(i=3) + ONLY(FATE, PALE, SICK, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the long-haired boy already turning his back on her.\n"
  "PANEL 2 (small): the girl on her knees, head down, hair over her face.\n"
  "PANEL 3 (dominant, middle): him walking away across the floor toward the stair, small and "
  "central, and her kneeling far behind him cropped by the bottom edge of the panel — his back is "
  "the whole composition.\n"
  "PANEL 4 (small): the thin proctor stepping forward, one hand raised.\n"
  "PANEL 5 (small): the proctor's mouth, opening.\n"
  "PANEL 6 (wide, bottom): the hall, the two of them, the raised hand. " + HALL
  + SAY((1, FATE, "upper left", "I TOLD YOU. A LOSER STAYS A LOSER."),
        (3, FATE, "upper right", "FATE CANNOT BE CHANGED."),
        (5, SICK, "lower left", "WINNER — HYU—")),
  R("neji", "hinata", "hayate"), "high"),

 ("p09", dict(scene="emotional_closeup", light="interior", cast="two", mood="somber", panels=5),
  FILL + HIN.format(i=1) + HAY.format(i=2) + ONLY(PALE, SICK, FATE, CROWD) +
  "FIVE panels, uneven. No dialogue.\n"
  "PANEL 1 (small): the proctor's raised hand stopping in mid-air.\n"
  "PANEL 2 (small): his face, looking past his own hand.\n"
  "PANEL 3 (small): one of the girl's feet, finding the floor.\n"
  "PANEL 4 (dominant, middle): the girl standing up — swaying badly, one arm hanging, absolutely "
  "upright — small and alone at the centre of the vast bare floor, seen from a low angle so the "
  "hall towers over her. Hard radiating lines converge on her. No injury detail.\n"
  "PANEL 5 (wide, bottom): the long-haired boy stopped dead halfway to the stair, seen from "
  "behind, not yet turned round. " + HALL,
  R("hinata", "hayate"), "high"),

 ("p10", dict(scene="emotional_closeup", light="interior", cast="two", mood="somber", panels=4),
  FILL + HIN.format(i=1) + NEJ.format(i=2) + ONLY(PALE, FATE, CROWD) +
  "FOUR panels only. This is the line the chapter is built around.\n"
  "PANEL 1 (small): the long-haired boy's head turning back over his shoulder.\n"
  "PANEL 2 (small): his pale eyes, and something behind them that was not there before.\n"
  "PANEL 3 (dominant, taking most of the page): the girl in close-up, cropped tight — hair stuck "
  "to her face, barely upright, looking straight at him and not down. Flat pale tone behind her, "
  "no hard shadow, no radiating lines. The calmest-drawn panel in the chapter.\n"
  "PANEL 4 (wide, bottom): the two of them across the floor, her standing, him turned round. "
  + HALL
  + SAY((3, PALE, "upper left", "IT'S TRUE THAT I LACK CONFIDENCE."),
        (3, PALE, "lower right", "BUT I HAVE SEEN PEOPLE CHANGE."),
        (4, PALE, "upper right", "AND IT ISN'T MYSELF I'M TRYING TO CHANGE, NEJI. IT'S YOU.")),
  R("hinata", "neji"), "high"),

 ("p11", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + NEJ.format(i=1) + HIN.format(i=2) + HAY.format(i=3) + ONLY(FATE, PALE, SICK, CROWD) +
  "FIVE panels, uneven, violent diagonals.\n"
  "PANEL 1 (small): the long-haired boy's face — the composure gone completely.\n"
  "PANEL 2 (small): his feet driving off the stone.\n"
  "PANEL 3 (dominant, middle): him crossing the floor at full speed with an open palm drawn back, "
  "the girl small and unmoving at the far end of the panel — and THREE adult shinobi arriving from "
  "three different directions at once, cropped by three different panel edges, converging on him. "
  "Hard speed lines, flat opaque shapes, no contact yet.\n"
  "PANEL 4 (small): his arm caught and held at the wrist by an adult hand. Hands only.\n"
  "PANEL 5 (wide, bottom): the long-haired boy held between three adults, the girl still standing "
  "beyond them. " + HALL
  + SFX(3, "DAN"),
  R("neji", "hinata", "hayate"), "high"),

 ("p12", dict(scene="dialogue", light="interior", cast="crowd", mood="somber", panels=6),
  FILL + NEJ.format(i=1) + HAY.format(i=2) + ENV.format(i=3) + ONLY(FATE, SICK, PALE, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the long-haired boy's arm being released.\n"
  "PANEL 2 (small): his face, contemptuous again, the mask back on.\n"
  "PANEL 3 (small): the adults stepping back from him.\n"
  "PANEL 4 (dominant, middle): him walking up the stair to the balcony alone, everyone on it "
  "leaning away, seen from behind and below.\n"
  "PANEL 5 (small): the girl being lifted onto a stretcher on the floor far below. No injury "
  "detail.\n"
  "PANEL 6 (wide, bottom): the empty floor, one raised hand, the board. " + HALL
  + SAY((2, FATE, "upper left", "IS THIS ANOTHER SPECIAL ALLOWANCE FOR THE MAIN HOUSE?"),
        (6, SICK, "upper right", "WINNER — HYUGA NEJI.")),
  R("neji", "hayate", "env_prelim_arena"), "high"),

 ("p13", dict(scene="emotional_closeup", light="interior", cast="two", mood="somber", panels=5),
  FILL + N13.format(i=1) + NEJ.format(i=2) + ONLY(BOY, FATE, CROWD) +
  "FIVE panels, uneven. NO DIALOGUE ANYWHERE ON THIS PAGE. It is the only time in three volumes "
  "that something visibly reaches him, and it must be played entirely in the face.\n"
  "PANEL 1 (small): the blond boy's hands on the balcony rail, knuckles pale.\n"
  "PANEL 2 (small): the stretcher going out through a door far below.\n"
  "PANEL 3 (narrow letterbox): the blond boy's single visible eye, cropped by all four edges. Not "
  "blank. Not cold. Something else, and it is not comfortable to look at.\n"
  "PANEL 4 (small): the long-haired boy arriving at the same railing several places along it, not "
  "looking at anyone.\n"
  "PANEL 5 (dominant, bottom): the two of them on the same long balcony, well apart, both facing "
  "out over the empty floor, neither looking at the other — and the blond boy's head is turned "
  "very slightly toward him. " + HALL,
  R("naruto_13", "neji"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch05" / "raw", HERE / "v3ch05" / "ledger.json")
