"""Volume 3, Chapter 4 — "The Preliminaries". 14 pages.

Source: fic ch5, the preliminary round. The fic runs all eleven matches; we stage two — his
own, which is over in a single movement, and Gaara's, which is the one that tells him he was
wrong about the room. The rest is a montage, same trick as Volume 2's Snow Country.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ENV, FILL, GAA, HAY, KAK, KIB, N13, NEJ, ONLY, OFF, R,      # noqa: E402
                     SAS, SAY, SFX, TITLE,
                     BOY, DOG, FATE, MAN, RED, SICK, UCH)

HALL = "Lighting: cold flat overhead light on grey stone, long hard shadows. "
CROWD = "the other genin and their jonin instructors watching from the balconies, none of them named"

PAGES = [
 ("p01", dict(scene="establishing", light="interior", cast="crowd", mood="tense", panels=1),
  ENV.format(i=1) + ONLY(CROWD) +
  "CHAPTER OPENING SPLASH. The great arena hall seen from the fighting floor looking UP — the two "
  "long spectator balconies run away down both sides of the paper crowded with small figures "
  "leaning on the railings, the huge dark display board hangs high on the far wall, and the two "
  "colossal stone hands locked in a seal rise at the far end and off the top of the paper. The "
  "near balcony railing is the foreground mass, cropped by the lower left edge. The fighting floor "
  "below is empty. Leave the pale wall beneath the display board broad and quiet. "
  "Lighting: cold hard overhead light, deep shadow under the balconies. "
  + TITLE("THE PRELIMINARIES", "pale wall beneath the display board"),
  R("env_prelim_arena"), "high"),

 ("p02", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + HAY.format(i=1) + ENV.format(i=2) + ONLY(SICK, BOY, UCH, CROWD) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): the thin proctor's fist at his mouth, coughing.\n"
  "PANEL 2 (dominant, upper): the proctor alone on the wide fighting floor seen from a high "
  "balcony angle, small and central, the emptiness of the floor around him filling the panel, and "
  "the packed balcony railings cropped huge and dark across the top of the frame.\n"
  "PANEL 3 (small): rows of genin faces along a railing at different depths.\n"
  "PANEL 4 (small): the display board lighting up, its characters illegible scribble.\n"
  "PANEL 5 (small): the blond boy's single visible eye, uninterested.\n"
  "PANEL 6 (wide, bottom): the whole hall. " + HALL
  + SAY((2, SICK, "upper left", "TWENTY-TWO OF YOU. ELEVEN MATCHES. WINNERS GO TO THE FINALS."),
        (6, SICK, "upper right", "THE RULES ARE SIMPLE. THERE ARE NONE. IT ENDS WHEN ONE OF YOU CANNOT STAND.")),
  R("hayate", "env_prelim_arena"), "high"),

 ("p03", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=8),
  FILL + SAS.format(i=1) + ENV.format(i=2) + ONLY(UCH, CROWD) +
  "EIGHT panels — deliberately fast FRAGMENTS of match after match, nothing given room. Uneven "
  "sizes, columns not aligned. No dialogue anywhere on this page.\n"
  "PANEL 1 (small): the display board flicking over to a new pair of names, illegible scribble.\n"
  "PANEL 2 (small): a fist and a forearm colliding. No faces.\n"
  "PANEL 3 (small): the dark-haired boy landing a kick, red eyes lit.\n"
  "PANEL 4 (small): a body hitting the stone floor. Small, slack, no injury detail.\n"
  "PANEL 5 (small): the proctor's raised hand.\n"
  "PANEL 6 (small): a different pair, mid-throw, drawn small and far off.\n"
  "PANEL 7 (small): the board flicking over again.\n"
  "PANEL 8 (wide, bottom): the balcony railing, the watching genin thinning out as names come off "
  "the board. " + HALL,
  R("sasuke", "env_prelim_arena"), "medium"),

 ("p04", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + KIB.format(i=1) + N13.format(i=2) + ENV.format(i=3) + ONLY(DOG, BOY, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the display board, two new names in illegible scribble.\n"
  "PANEL 2 (small): the boy with the red fang markings vaulting the balcony railing, grinning, the "
  "white puppy on his head.\n"
  "PANEL 3 (small): the blond boy walking down a stair, unhurried.\n"
  "PANEL 4 (dominant, middle): the two of them facing each other across the wide stone floor at "
  "very different depths — the fanged boy large in the left foreground cropped by the edge and "
  "crouched to spring, the blond boy small and standing perfectly straight with his hands at his "
  "sides, the whole floor between them.\n"
  "PANEL 5 (small): the fanged boy's face, all teeth.\n"
  "PANEL 6 (wide, bottom): the balconies looking down on the two of them. " + HALL
  + SAY((2, DOG, "upper left", "FINALLY! I'VE BEEN WAITING TO GET A SHOT AT YOU!"),
        (4, DOG, "upper right", "NO HARD FEELINGS WHEN I PUT YOU DOWN, HUH?")),
  R("kiba", "naruto_13", "env_prelim_arena"), "high"),

 ("p05", dict(scene="action", light="interior", cast="two", mood="tense", panels=4),
  FILL + N13.format(i=1) + KIB.format(i=2) + ONLY(BOY, DOG, SICK) +
  "FOUR panels only. The whole match is one movement and the page must be over as fast as it is.\n"
  "PANEL 1 (small): the proctor's hand dropping.\n"
  "PANEL 2 (narrow letterbox): the blond boy's half of the floor — EMPTY. Nothing but stone and "
  "hard speed lines. No figure at all.\n"
  "PANEL 3 (dominant, taking most of the page): the blond boy already standing behind the fanged "
  "boy with one open hand extended flat at the back of his neck, having crossed the entire floor — "
  "the fanged boy still crouched in his starting spring, eyes wide, not yet aware. Seen from a low "
  "three-quarter angle, hard radiating lines, no contact and no injury detail.\n"
  "PANEL 4 (wide, bottom): the fanged boy folded on the stone, out cold, the white puppy standing "
  "beside him barking, and the blond boy already walking back toward the stair. No injury detail. "
  + HALL
  + SFX(2, "SHUN"),
  R("naruto_13", "kiba"), "high"),

 ("p06", dict(scene="emotional_closeup", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + HAY.format(i=1) + KAK.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(SICK, MAN, BOY, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the proctor's face, having missed it too.\n"
  "PANEL 2 (small): a whole balcony railing of genin faces, silent.\n"
  "PANEL 3 (small): the masked silver-haired man's single visible eye — not surprised, which is "
  "worse.\n"
  "PANEL 4 (dominant, middle): the blond boy climbing the stair back up to the balcony, small and "
  "alone on it, with the crowded railings above him on both sides and every single face turned to "
  "follow him. Nobody is speaking.\n"
  "PANEL 5 (small): his own face, entirely blank, not looking at any of them.\n"
  "PANEL 6 (wide, bottom): the hall, the empty floor, the boy rejoining the rail. " + HALL
  + SAY((1, SICK, "upper left", "...HE IS UNABLE TO CONTINUE."),
        (2, OFF(SICK), "upper right", "WINNER — UZUMAKI NARUTO.")),
  R("hayate", "kakashi", "naruto_13", "env_prelim_arena"), "high"),

 ("p07", dict(scene="action", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + GAA.format(i=1) + HAY.format(i=2) + ENV.format(i=3)
  + ONLY(RED, SICK, BOY, "a teenage girl genin with long black hair, not recurring", CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the red-haired boy standing alone on the floor, the gourd enormous behind him.\n"
  "PANEL 2 (small): a black-haired girl genin with both hands raised, palms out, forfeiting.\n"
  "PANEL 3 (small): the proctor's mouth opening to call it.\n"
  "PANEL 4 (dominant, middle): sand pouring out of the gourd and crossing the floor toward her "
  "anyway, drawn as flat opaque hard-outlined ribbons filling the lower half of the panel — she is "
  "small and backing away, he has not moved at all. No contact, no injury detail.\n"
  "PANEL 5 (small): the proctor between them with the girl pulled behind him, one arm out.\n"
  "PANEL 6 (wide, bottom): the sand hanging in the air, stopped, and the red-haired boy's blank "
  "face across the floor. " + HALL
  + SAY((5, SICK, "upper left", "SHE FORFEITED. WHY ARE YOU STILL ATTACKING HER?"))
  + "The red-haired boy does not answer and has no balloon anywhere on this page. ",
  R("gaara", "hayate", "env_prelim_arena"), "high"),

 ("p08", dict(scene="emotional_closeup", light="interior", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + GAA.format(i=2) + ONLY(BOY, RED, CROWD) +
  "FIVE panels, uneven. No dialogue. This is the page where he revises his opinion of the room.\n"
  "PANEL 1 (small): the blond boy's hands on the balcony rail, still.\n"
  "PANEL 2 (small): the red-haired boy far below, being walked off the floor, sand retracting.\n"
  "PANEL 3 (small): the red-haired boy's eyes turning up toward the balcony — straight at him.\n"
  "PANEL 4 (narrow letterbox): the blond boy's single visible eye, cropped by all four edges. He "
  "is, for the first time all chapter, paying attention.\n"
  "PANEL 5 (dominant, bottom): the two of them at opposite ends of the enormous hall — the boy "
  "small on the high balcony, the red-haired boy small on the floor far below and across, and the "
  "whole cold grey volume of the arena between them. " + HALL,
  R("naruto_13", "gaara"), "high"),

 ("p09", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=7),
  FILL + ENV.format(i=1)
  + ONLY("a boy in a bright green jumpsuit with a bowl cut and thick eyebrows",
         "a hunched genin in a fur-collared coat with most of his face bandaged", CROWD) +
  "SEVEN panels — the montage resumes. Fast fragments, uneven, columns not aligned. No dialogue.\n"
  "PANEL 1 (small): the board flicking over.\n"
  "PANEL 2 (small): a bright green blur crossing the floor, no figure resolvable.\n"
  "PANEL 3 (small): a bandaged arm raised to block.\n"
  "PANEL 4 (dominant, middle): the boy in the green jumpsuit mid-air upside down with one leg "
  "extended in a full kick, the hunched bandaged genin folding away from it, both cropped by the "
  "panel edges, hard speed lines. Flat opaque impact shapes, no injury detail.\n"
  "PANEL 5 (small): a body on the stone. Small, slack, no injury detail.\n"
  "PANEL 6 (small): the green-suited boy's fist, thrust up in triumph.\n"
  "PANEL 7 (wide, bottom): the board, another two names gone. " + HALL,
  R("env_prelim_arena"), "medium"),

 ("p10", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + NEJ.format(i=1) + ENV.format(i=2) + ONLY(FATE, BOY, CROWD) +
  "FIVE panels, uneven. The chapter ends by naming the next two, and one of them is family.\n"
  "PANEL 1 (small): the display board flicking over.\n"
  "PANEL 2 (small): a balcony gone very quiet — three or four faces turning the same way at once.\n"
  "PANEL 3 (dominant, middle): the long-haired boy with the pale pupil-less eyes walking to the "
  "head of the stair, seen from behind and below, small against the height of the hall, everyone "
  "else on the balcony leaning back out of his way.\n"
  "PANEL 4 (small): his face in close-up — pale blank eyes, no expression whatsoever.\n"
  "PANEL 5 (wide, bottom): the empty floor waiting below him. " + HALL
  + SAY((2, "a genin at the railing", "upper left", "THOSE TWO ARE BOTH HYUGA."),
        (2, "a second genin at the railing", "lower right", "THEY'RE COUSINS.")),
  R("neji", "env_prelim_arena"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch04" / "raw", HERE / "v3ch04" / "ledger.json")
