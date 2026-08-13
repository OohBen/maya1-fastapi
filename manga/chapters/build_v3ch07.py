"""Volume 3, Chapter 7 — "The Silent Crowd". 14 pages.

Source: fic ch6. Naruto sends a shadow clone to fight Neji and sits down, which is the single
most arrogant thing he does in three volumes — and the author's own note on this chapter is
that Naruto's manner changes when he fights, because Madara succeeded. The crowd is the point
of view: they came to watch a prodigy and they watch something else.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (ENV, FILL, GEN, HIR, N13, NEJ, ONLY, OFF, R, SAY, SFX,      # noqa: E402
                     TITLE, BOY, FATE, NEEDLE, OLD)

SUN = "Lighting: bright flat midday daylight, hard short shadows on sand. "
CROWD = "a packed stadium crowd drawn only as small distant heads and shoulders, none of them named"
EYES = ("When the long-haired boy activates his eyes the pale pupil-less eyes stay pale and the "
        "VEINS AROUND HIS TEMPLES BULGE OUT hard and dark. No colour change, no glow. ")

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=1),
  ENV.format(i=1) + ONLY(CROWD) +
  "CHAPTER OPENING SPLASH. The finals arena seen from the sand looking up and around — steep "
  "tiered stone stands packed with thousands of tiny spectators sweep round the paper from the "
  "left edge to the right, banners on poles along the rim, a covered dignitaries' box high on one "
  "side, and a wide blue sky above. The arena floor in the foreground is empty pale sand, cropped "
  "by the bottom edge. Leave the broad sky at the upper right quiet. "
  "Lighting: hard bright midday sun, short black shadows. "
  + TITLE("THE SILENT CROWD", "sky at the upper right"),
  R("env_stadium"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="crowd", mood="calm", panels=6),
  FILL + GEN.format(i=1) + N13.format(i=2) + NEJ.format(i=3) + ENV.format(i=4)
  + ONLY(NEEDLE, BOY, FATE, CROWD) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): a thin metal needle shifting from one side of a mouth to the other. Mouth "
  "only.\n"
  "PANEL 2 (small): the proctor's raised arm, the crowd noise dying.\n"
  "PANEL 3 (dominant, middle): the two finalists left alone on the sand as the others walk away up "
  "a tunnel behind them — the blond boy and the long-haired boy small and far apart, the enormous "
  "packed stands rising behind and above them and filling the whole upper half of the panel.\n"
  "PANEL 4 (small): the long-haired boy's pale eyes.\n"
  "PANEL 5 (small): the blond boy's single visible eye. His hair is a little longer than it was.\n"
  "PANEL 6 (wide, bottom): the proctor between them, one arm up. " + SUN
  + SAY((2, NEEDLE, "upper left", "FIRST MATCH — UZUMAKI NARUTO AGAINST HYUGA NEJI."),
        (6, NEEDLE, "upper right", "BEGIN.")),
  R("genma", "naruto_13", "neji", "env_stadium"), "high"),

 ("p03", dict(scene="action", light="day", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + NEJ.format(i=2) + ONLY(BOY, FATE, CROWD) +
  "SIX panels, uneven. The insult. It must be perfectly clear what he has just done.\n"
  "PANEL 1 (small): the blond boy's hands coming up into a single seal.\n"
  "PANEL 2 (small): flat white smoke beside him.\n"
  "PANEL 3 (dominant, middle): TWO identical blond boys standing on the sand — and one of them is "
  "already walking backwards away from the fight, while the other stays. Both clearly the same "
  "boy, at slightly different depths, the long-haired boy small and rigid across the arena beyond "
  "them.\n"
  "PANEL 4 (small): the second one sitting down cross-legged on the sand and CLOSING HIS EYES.\n"
  "PANEL 5 (small): the long-haired boy's face — the composure cracking straight down the middle.\n"
  "PANEL 6 (wide, bottom): the whole stands, thousands of small figures, going absolutely silent. "
  + SUN
  + SAY((5, FATE, "upper left", "WHAT IS THIS? YOU AREN'T EVEN GOING TO FIGHT ME?"),
        (6, BOY, "upper right", "MY CLONE WILL DO. I WOULD RATHER NOT SPEND THE ENERGY."))
  + SFX(2, "POFU"),
  R("naruto_13", "neji"), "high"),

 ("p04", dict(scene="action", light="day", cast="two", mood="tense", panels=6),
  FILL + NEJ.format(i=1) + N13.format(i=2) + ONLY(FATE, BOY, CROWD) + EYES +
  "SIX panels, uneven, hard diagonals.\n"
  "PANEL 1 (small): the long-haired boy's pale eyes with the veins standing hard around them.\n"
  "PANEL 2 (small): his feet driving off the sand.\n"
  "PANEL 3 (dominant, middle): him crossing the arena at full speed straight PAST the standing "
  "clone toward the seated one — the seated figure small and cross-legged and eyes shut at the far "
  "end of the panel, the runner cropped huge in the foreground, hard speed lines. He is ignoring "
  "the clone entirely.\n"
  "PANEL 4 (small): the standing one stepping into his path.\n"
  "PANEL 5 (small): two palms colliding, hands only, flat impact shapes.\n"
  "PANEL 6 (wide, bottom): the long-haired boy stopped dead, the clone in front of him, the seated "
  "one still untouched beyond. " + SUN,
  R("neji", "naruto_13"), "high"),

 ("p05", dict(scene="action", light="day", cast="two", mood="tense", panels=6),
  FILL + NEJ.format(i=1) + N13.format(i=2) + ONLY(FATE, BOY, CROWD) + EYES +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a glowing open palm thrust at a chest and finding empty air.\n"
  "PANEL 2 (small): sand kicked up in flat opaque shapes where a figure was.\n"
  "PANEL 3 (dominant, middle): the two of them mid-exchange across the arena floor, the clone "
  "always a fraction out of reach, drawn with the long-haired boy fully committed and the clone "
  "leaning back off the vertical — hard motion lines, flat impact shapes, no contact. The seated "
  "figure is small and unmoved at the panel's edge.\n"
  "PANEL 4 (small): the long-haired boy's teeth, set.\n"
  "PANEL 5 (small): the clone's face — and it is smiling, very slightly, which the real one never "
  "does in a fight.\n"
  "PANEL 6 (wide, bottom): the crowd, leaning forward, still not making a sound. " + SUN
  + SAY((5, BOY, "upper right", "FASTER THAN THAT, PRODIGY.")),
  R("neji", "naruto_13"), "high"),

 ("p06", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=5),
  FILL + HIR.format(i=1) + ENV.format(i=2) + ONLY(OLD, "a second kage in green robes and a wide "
    "veiled hat seated beside him, his face not visible", CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the covered dignitaries' box seen from the arena floor far below, small.\n"
  "PANEL 2 (dominant, upper): inside the box — the old man in the tall hat seated on the left "
  "watching the arena, and beside him a SECOND kage in green robes and a wide veiled hat whose "
  "face is completely hidden by the veil. Two guards stand behind them, cropped by the panel edges. "
  "Neither kage is looking at the other.\n"
  "PANEL 3 (small): the old man's lined face, entirely calm.\n"
  "PANEL 4 (small): the veiled one's hat brim, and beneath it nothing but shadow.\n"
  "PANEL 5 (wide, bottom): the arena floor far below them, two tiny figures and a third sitting "
  "down. " + SUN
  + SAY((2, "the veiled kage in green robes", "upper right", "YOUR GENIN IS ARROGANT, HOKAGE-DONO."),
        (3, OLD, "upper left", "HE IS. HE IS ALSO NOT YET USING BOTH HANDS.")),
  R("hiruzen", "env_stadium"), "high"),

 ("p07", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + NEJ.format(i=1) + N13.format(i=2) + ONLY(FATE, BOY, CROWD) + EYES +
  "FIVE panels, uneven, violent diagonals.\n"
  "PANEL 1 (small): the long-haired boy dropping into a low crouch, both palms out, spinning.\n"
  "PANEL 2 (dominant, middle): a dome of flat hard-edged rotating shapes bursting outward from him "
  "across the sand — drawn as opaque overlapping crescents with hard black outlines, throwing sand "
  "up in flat sheets. It does NOT glow. The clone is caught at the edge of it and coming apart into "
  "white smoke, cropped by the panel edge.\n"
  "PANEL 3 (small): white smoke where the clone was.\n"
  "PANEL 4 (small): the long-haired boy straightening, breathing hard, finally satisfied.\n"
  "PANEL 5 (wide, bottom): the seated figure across the arena — eyes still shut, having not moved "
  "at all. " + SUN
  + SFX(2, "GOOON"),
  R("neji", "naruto_13"), "high"),

 ("p08", dict(scene="emotional_closeup", light="day", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + NEJ.format(i=2) + ONLY(BOY, FATE, CROWD) +
  "FIVE panels, uneven. The author's note on this chapter is that his manner changes when he "
  "fights, because Madara succeeded. This is the page where the reader sees it.\n"
  "PANEL 1 (small): the seated boy's eyes opening.\n"
  "PANEL 2 (small): his hands on his knees, unclenching.\n"
  "PANEL 3 (small): him standing up unhurriedly, brushing sand off.\n"
  "PANEL 4 (dominant, middle): the blond boy in close-up, cropped very tight — and his face is "
  "WRONG. Not blank. The mouth has gone into a thin private smile that belongs to a much older and "
  "much worse person, and the visible eye is half-lidded with interest. Hard parallel hatching, "
  "flat black behind. This is the first time the reader sees his grandfather in him.\n"
  "PANEL 5 (wide, bottom): the long-haired boy across the sand, and the change in his face as he "
  "registers it. " + SUN
  + SAY((4, BOY, "upper left", "GOOD. THAT WAS WORTH GETTING UP FOR.")),
  R("naruto_13", "neji"), "high"),

 ("p09", dict(scene="action", light="day", cast="two", mood="tense", panels=4),
  FILL + N13.format(i=1) + NEJ.format(i=2) + ONLY(BOY, FATE, CROWD) +
  "FOUR panels only. The real match, and it is short.\n"
  "PANEL 1 (narrow letterbox): the sand between them, empty, hard speed lines converging.\n"
  "PANEL 2 (dominant, taking most of the page): the blond boy arriving INSIDE the long-haired "
  "boy's guard with one open palm already flat against his sternum — the long-haired boy's arms "
  "still out wide where the block should have been, pale eyes blown open. Seen from a low "
  "three-quarter angle, hard radiating lines exploding outward as flat opaque shapes. No injury "
  "detail, no red.\n"
  "PANEL 3 (small): the long-haired boy leaving the ground backwards.\n"
  "PANEL 4 (wide, bottom): him laid out on the sand well across the arena, one arm flung out, not "
  "getting up. No injury detail. " + SUN
  + SFX(2, "DOOON"),
  R("naruto_13", "neji"), "high"),

 ("p10", dict(scene="emotional_closeup", light="day", cast="crowd", mood="somber", panels=6),
  FILL + GEN.format(i=1) + N13.format(i=2) + NEJ.format(i=3) + ENV.format(i=4)
  + ONLY(NEEDLE, BOY, FATE, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the proctor's hand going up.\n"
  "PANEL 2 (small): thousands of small faces in the stands, none of them cheering.\n"
  "PANEL 3 (small): the long-haired boy's pale eyes, open, staring at the sky.\n"
  "PANEL 4 (dominant, middle): the blond boy standing over him but not looking down — looking UP "
  "at the silent stands instead, small and central on the enormous empty sand with the packed "
  "tiers rising all round him and saying nothing at all.\n"
  "PANEL 5 (small): his face. The wrong smile is gone; the blankness is back.\n"
  "PANEL 6 (wide, bottom): the arena, one figure standing and one down. " + SUN
  + SAY((1, NEEDLE, "upper left", "WINNER — UZUMAKI NARUTO."),
        (3, FATE, "lower right", "...IT WASN'T FATE. YOU WERE SIMPLY BETTER.")),
  R("genma", "naruto_13", "neji", "env_stadium"), "high"),

 ("p11", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=5),
  FILL + N13.format(i=1) + NEJ.format(i=2) + ONLY(BOY, FATE, CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the blond boy's hand, extended down, open.\n"
  "PANEL 2 (small): the long-haired boy's pale eyes, looking at it.\n"
  "PANEL 3 (dominant, middle): the two of them on the sand — the beaten boy propped on one elbow "
  "looking up, the other standing over him with the hand still out, the whole silent stadium "
  "wrapped round both of them. Neither is performing for it.\n"
  "PANEL 4 (small): a hand taking a hand.\n"
  "PANEL 5 (wide, bottom): the two of them walking off the sand toward the tunnel, apart, neither "
  "speaking. " + SUN
  + SAY((1, BOY, "upper left", "YOUR COUSIN STOOD UP WHEN SHE SHOULD NOT HAVE BEEN ABLE TO."),
        (3, BOY, "upper right", "SO DID YOU. THAT IS NOT NOTHING.")),
  R("naruto_13", "neji"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch07" / "raw", HERE / "v3ch07" / "ledger.json")
