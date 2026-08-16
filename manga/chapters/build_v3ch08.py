"""Volume 3, Chapter 8 — "Susano'o". 12 pages. Ends Volume 3.

Source: fic ch7. Lee against Gaara, then Naruto against Gaara, then the invasion opens
underneath it. The volume stops the instant Naruto sees the purple barrier go up over the
academy with Orochimaru inside it. The source continues after that point with Naruto's Sound
encounter, Baki's attack, the forest rematch with Gaara, Gaara's defeat and apology, and Naruto's
return to Konoha; those beats are absent from the produced Volume 3 and Volume 4 begins after
them.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ENV, FILL, GAA, GEN, HIR, LEE, N13, ONLY, OFF, R, SAY,      # noqa: E402
                     SFX, TITLE, BOY, GREEN, NEEDLE, OLD, RED)

SUN = "Lighting: bright flat midday daylight, hard short shadows on sand. "
CROWD = "a packed stadium crowd drawn only as small distant heads and shoulders, none of them named"
SUSA = ("SUSANO'O IS DRAWN AS FOLLOWS AND NEVER OTHERWISE: a COLOSSAL humanoid warrior figure made "
        "of flat, translucent, hard-outlined ORANGE shapes standing around and above the boy like "
        "armour many times his size — a ribcage, a skull-like helmed head, and two arms. It is "
        "built from clean flat colour with hard black outlines and internal line-work, exactly like "
        "the rest of the art. It does NOT glow, does not bloom, and does not wash the scene out: "
        "the arena, the sand, the crowd and the boy himself all stay fully drawn and legible "
        "through and around it. ")
MANG = ("When the blond boy's eye is shown changed it is BLOOD-RED with a black three-bladed "
        "pinwheel pattern across the iris. ")

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="two", mood="tense", panels=1),
  N13.format(i=1) + ONLY(BOY) + SUSA + MANG +
  "CHAPTER OPENING SPLASH. The blond boy stands small and off centre in the lower left of the "
  "paper on pale arena sand, and rising around and far above him is the colossal translucent "
  "orange ribcage and helmed skull of a giant warrior figure, its shoulders running off the top "
  "and right edges of the paper. Seen from ground level so the scale difference is overwhelming. "
  "The arena sand and a section of packed stone stands stay fully drawn and legible straight "
  "through the orange shapes. A section of arena wall is the foreground mass, cropped by the lower "
  "right edge. Leave the sky at the upper left quiet. "
  "Lighting: hard bright midday sun. "
  + TITLE("SUSANO'O", "sky at the upper left"),
  R("naruto_13", "env_stadium"), "high"),

 ("p02", dict(scene="action", light="day", cast="two", mood="tense", panels=7),
  FILL + LEE.format(i=1) + GAA.format(i=2) + ENV.format(i=3) + ONLY(GREEN, RED, CROWD) +
  "SEVEN panels — a compressed match in fast fragments. Uneven, columns not aligned.\n"
  "PANEL 1 (small): the boy in the green jumpsuit unwinding a heavy weight from his ankle.\n"
  "PANEL 2 (small): two weights hitting the sand and cratering it.\n"
  "PANEL 3 (small): a green blur crossing the arena, no figure resolvable.\n"
  "PANEL 4 (dominant, middle): flat opaque ribbons of sand rising in a wall around the red-haired "
  "boy as the green blur breaks against it — the sand drawn with hard black outlines, the "
  "green-suited boy cropped by the panel edge mid-strike. The red-haired boy has not moved and his "
  "face is empty.\n"
  "PANEL 5 (small): the green-suited boy landing hard, one knee down, breathing.\n"
  "PANEL 6 (small): the red-haired boy's face in close-up, the black rings, the red kanji.\n"
  "PANEL 7 (wide, bottom): the green-suited boy carried off the sand on a stretcher, and the "
  "red-haired boy standing alone in the middle of the arena. No injury detail. " + SUN
  + SAY((6, RED, "upper right", "MOTHER WANTS MORE.")),
  R("rock_lee", "gaara", "env_stadium"), "high"),

 ("p03", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + GAA.format(i=2) + GEN.format(i=3) + ONLY(BOY, RED, NEEDLE, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the proctor's needle shifting across his mouth.\n"
  "PANEL 2 (small): the blond boy walking out of the tunnel onto the sand.\n"
  "PANEL 3 (dominant, middle): the two of them alone on the arena floor at a great distance apart, "
  "both small, the packed stands wrapping the whole upper half of the panel — sand already "
  "trailing loose off the gourd on one side, and nothing at all happening on the other.\n"
  "PANEL 4 (small): the red-haired boy's pale ringed eyes.\n"
  "PANEL 5 (small): the blond boy's single visible eye.\n"
  "PANEL 6 (wide, bottom): the proctor's arm dropping between them. " + SUN
  + SAY((3, RED, "upper left", "YOU. I HAVE BEEN WAITING."),
        (5, BOY, "upper right", "SO HAVE I. I AM NOT GOING TO HOLD BACK."),
        (6, NEEDLE, "lower left", "BEGIN.")),
  R("naruto_13", "gaara", "genma"), "high"),

 ("p04", dict(scene="action", light="day", cast="two", mood="tense", panels=6),
  FILL + GAA.format(i=1) + N13.format(i=2) + ONLY(RED, BOY, CROWD) +
  "SIX panels, uneven, violent diagonals.\n"
  "PANEL 1 (small): sand pouring out of the gourd in a flat opaque sheet.\n"
  "PANEL 2 (small): the blond boy's feet leaving the ground.\n"
  "PANEL 3 (dominant, middle): a colossal wave of sand crossing the entire arena as flat opaque "
  "hard-outlined ribbons and crescents, filling most of the panel, with the blond boy small and "
  "airborne above it. The stands stay fully drawn and legible behind it.\n"
  "PANEL 4 (small): a great fist of sand closing on empty air.\n"
  "PANEL 5 (small): the red-haired boy's face, beginning to enjoy himself.\n"
  "PANEL 6 (wide, bottom): the arena floor churned up, the two of them still far apart. " + SUN
  + SFX(3, "ZAZAAA"),
  R("gaara", "naruto_13"), "high"),

 ("p05", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + GAA.format(i=2) + ONLY(BOY, RED, CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the blond boy's hands running through a fast chain of seals.\n"
  "PANEL 2 (dominant, middle): a broad sheet of FIRE pouring out across the arena, drawn as flat "
  "opaque orange and yellow shapes with hard black outlines layered in front of and behind the "
  "sand wall — no glow, no wash. The sand fuses where it meets, going to hard-edged dark glass "
  "shapes. Both figures stay small and fully drawn.\n"
  "PANEL 3 (small): sheets of fused dark glass cracking and falling.\n"
  "PANEL 4 (small): the red-haired boy's face through the gap, delighted, unhurt.\n"
  "PANEL 5 (wide, bottom): the whole arena floor scorched black, the two of them in it. " + SUN
  + SFX(2, "GOOOO"),
  R("naruto_13", "gaara"), "high"),

 ("p06", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=5),
  FILL + HIR.format(i=1) + ENV.format(i=2) + ONLY(OLD, "a second kage in green robes and a wide "
    "veiled hat seated beside him, his face hidden by the veil", CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the arena far below seen from the dignitaries' box, two tiny figures in a "
  "scorched circle.\n"
  "PANEL 2 (dominant, upper): inside the box — the old man in the tall hat on the left, the veiled "
  "kage in green robes on the right leaning forward with both hands on the rail, two guards cropped "
  "by the panel edges behind them.\n"
  "PANEL 3 (small): the old man's face, calm.\n"
  "PANEL 4 (small): under the veil, in deep shadow, ONE EYE catching the light — and it is GOLDEN "
  "with a vertical black slit pupil. Only the eye is visible. Nothing else of the face.\n"
  "PANEL 5 (wide, bottom): the box, the two seated figures, the arena below. " + SUN
  + SAY((2, "the veiled kage in green robes", "upper right", "SO FAR HE HAS SHOWN US ONLY FIRE."),
        (3, OLD, "upper left", "SO FAR.")),
  R("hiruzen", "env_stadium"), "high"),

 ("p07", dict(scene="action", light="day", cast="two", mood="tense", panels=4),
  FILL + N13.format(i=1) + GAA.format(i=2) + ONLY(BOY, RED, CROWD) + MANG +
  "FOUR panels only. The eye gets the page.\n"
  "PANEL 1 (small): the blond boy's hand pushing the long bang back off the right side of his "
  "face — the side that has been covered for three volumes.\n"
  "PANEL 2 (dominant, taking most of the page): BOTH his eyes in extreme close-up, cropped by all "
  "four edges — and both are blood-red with a black three-bladed pinwheel across each iris. Flat "
  "black behind, hard radiating lines. No glow.\n"
  "PANEL 3 (small): the red-haired boy's ringed eyes, and for the first time something in them "
  "that is not appetite.\n"
  "PANEL 4 (wide, bottom): the stands, thousands of small figures, and the front rows standing up. "
  + SUN,
  R("naruto_13", "gaara"), "high"),

 ("p08", dict(scene="action", light="day", cast="two", mood="tense", panels=4),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(BOY, RED, CROWD) + SUSA +
  "FOUR panels only. This is the page the volume has been building to.\n"
  "PANEL 1 (small): the sand around the boy's feet lifting straight up off the ground.\n"
  "PANEL 2 (narrow letterbox): flat orange hard-edged shapes racing outward from him across the "
  "whole panel width.\n"
  "PANEL 3 (dominant, taking most of the page): the COLOSSAL translucent orange warrior standing "
  "in the arena around the boy — ribcage, helmed skull, two arms — its head level with the top of "
  "the stadium stands, seen from ground level at the far side of the arena. The boy is a tiny dark "
  "figure at its centre. The sand, the scorched floor, the stone tiers and the crowd all stay "
  "fully drawn and legible through the orange shapes. It does not glow.\n"
  "PANEL 4 (wide, bottom): the red-haired boy at the foot of it, very small, looking up. " + SUN
  + SFX(2, "GOUN"),
  R("naruto_13", "env_stadium"), "high"),

 ("p09", dict(scene="emotional_closeup", light="day", cast="crowd", mood="tense", panels=6),
  FILL + HIR.format(i=1) + ENV.format(i=2) + ONLY(OLD, "a second kage in green robes and a wide "
    "veiled hat, his face hidden", CROWD) +
  "SIX panels, uneven. Nobody in the stadium is watching the fight any more.\n"
  "PANEL 1 (small): a row of spectators on their feet, mouths open.\n"
  "PANEL 2 (small): an older shinobi in the stands, gone white.\n"
  "PANEL 3 (small): the old man in the tall hat, half out of his seat.\n"
  "PANEL 4 (dominant, middle): the dignitaries' box seen from behind and above, both kage small in "
  "it — and the enormous orange figure filling the entire view beyond and above them, its shoulder "
  "higher than the box itself. The stands stay drawn straight through it.\n"
  "PANEL 5 (small): under the veil, the golden slit eye again — wide open now.\n"
  "PANEL 6 (wide, bottom): the whole stadium on its feet. " + SUN
  + SAY((3, OLD, "upper left", "...THAT IS NOT A JUTSU ANY LIVING SHINOBI HAS."),
        (6, "the veiled kage in green robes", "upper right", "NO. IT IS NOT.")),
  R("hiruzen", "env_stadium"), "high"),

 ("p10", dict(scene="action", light="day", cast="crowd", mood="tense", panels=6),
  FILL + ENV.format(i=1) + ONLY(CROWD, "a few masked shinobi appearing among the spectators") +
  "SIX panels, uneven. The invasion opens underneath the fight and Naruto is not on this page.\n"
  "PANEL 1 (small): a single white FEATHER drifting down past a stone railing. Object only.\n"
  "PANEL 2 (small): a dozen more of them falling through the air above the crowd.\n"
  "PANEL 3 (small): a spectator's head tipping forward onto their chest, asleep.\n"
  "PANEL 4 (dominant, middle): a whole tier of the stands slumping into sleep at once, hundreds of "
  "small figures folding over the seats in front of them — while a scattered handful of masked "
  "figures stand upright among them, wide awake, drawing weapons.\n"
  "PANEL 5 (small): a blade coming out of a sheath among the seats. No people struck.\n"
  "PANEL 6 (wide, bottom): the stadium from high above, half of it asleep and the rest breaking "
  "into movement. " + SUN
  + SFX(2, "HIRA HIRA"),
  R("env_stadium"), "high"),

 ("p11", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + GAA.format(i=2) + ONLY(BOY, RED, CROWD) + SUSA +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the blond boy's single visible eye flicking sideways off his opponent.\n"
  "PANEL 2 (small): feathers landing on scorched sand and not affecting him at all.\n"
  "PANEL 3 (dominant, middle): the enormous orange figure standing motionless in the arena as the "
  "fighting starts in the stands all around and above it — small figures grappling along the "
  "tiers, drawn fully and legibly straight through the orange shapes. The red-haired boy is being "
  "pulled away toward a tunnel by two other figures at the panel's edge.\n"
  "PANEL 4 (small): the blond boy's face, entirely uninterested in the fight he was having.\n"
  "PANEL 5 (wide, bottom): the orange figure breaking apart into flat hard-edged shapes and "
  "vanishing, leaving one small boy alone on the sand. " + SUN
  + SAY((1, BOY, "upper left", "GENJUTSU. ACROSS THE WHOLE STADIUM."),
        (4, BOY, "upper right", "SO IT IS AN INVASION.")),
  R("naruto_13", "gaara"), "high"),

 ("p12", dict(scene="emotional_closeup", light="day", cast="solo", mood="tense", panels=4),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "FOUR panels only. LAST PAGE OF VOLUME THREE.\n"
  "PANEL 1 (small): the blond boy landing on the curved stone rim of the stadium roof, crouched.\n"
  "PANEL 2 (small): his head turning to look out across the village.\n"
  "PANEL 3 (dominant, taking most of the page): what he sees — the academy building across the "
  "rooftops with a great PURPLE BARRIER standing over its roof, drawn as four flat translucent "
  "hard-outlined purple walls rising into a box with four small figures kneeling at its corners. "
  "Inside it, tiny and unmistakable, two figures face each other: one in a tall kage hat, one with "
  "very long black hair. The whole burning village lies between the viewer and it. It does not "
  "glow; the rooftops stay drawn through it.\n"
  "PANEL 4 (wide, bottom): the blond boy's face in close-up on the roof rim, cropped tight — and "
  "he has understood all of it at once. No dialogue anywhere on this page except the caption. "
  "Lighting: hard midday sun, black smoke rising off the village. ",
  R("naruto_13", "env_village_street"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch08" / "raw", HERE / "v3ch08" / "ledger.json")
