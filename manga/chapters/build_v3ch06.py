"""Volume 3, Chapter 6 — "The Toad Sage". 12 pages.

Source: fic ch5, the draw through Jiraiya. He turns down the one person alive who could have
taught him and then removes himself from the village for three weeks. After this there is
nobody above him left to ask, which is the whole point of the chapter.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (CAP, ENV, FILL, HIR, JIR, KAK, N13, NEJ, ONLY, OFF, R,      # noqa: E402
                     SAY, SFX, SHI, TITLE, ZET,
                     BOY, FATE, LAZY, MAN, OLD, SAGE)

HALL = "Lighting: cold flat overhead light on grey stone, long hard shadows. "
DUSK = "Lighting: cool blue dusk, the village lights coming on below. "
CREATURE = "the split black-and-white plant creature"

PAGES = [
 ("p01", dict(scene="establishing", light="dusk", cast="solo", mood="calm", panels=1),
  JIR.format(i=1) + ONLY(SAGE) +
  "CHAPTER OPENING SPLASH. A big white-haired man sitting alone on the wide flat top of a stone "
  "wall above a river at dusk, seen from behind and below — he is in the lower right of the paper, "
  "one knee up, an open scroll across it, the enormous white mane the loudest shape on the page. "
  "Beyond and below him the village falls away in rooftops to the carved stone faces of the cliff "
  "on the horizon. A stone lantern is the foreground mass, cropped by the lower left edge. Leave "
  "the broad open sky at the upper left quiet. "
  "Lighting: low orange dusk from the left, everything else going blue. "
  + TITLE("THE TOAD SAGE", "open sky at the upper left"),
  R("jiraiya"), "high"),

 ("p02", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + N13.format(i=1) + NEJ.format(i=2) + SHI.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, FATE, LAZY, "the other surviving genin standing in a line, none of them named") +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): a hand drawing a folded paper slip out of a wooden box. Hand and box only.\n"
  "PANEL 2 (small): the slip unfolded, its writing illegible scribble.\n"
  "PANEL 3 (dominant, middle): the surviving genin standing in a loose line across the arena floor "
  "at clearly different depths, several cropped by the panel edges, two turned away — and the huge "
  "dark display board behind them lighting up with the bracket, all of it illegible scribble "
  "except that the reader can see two names sit at the very top of it.\n"
  "PANEL 4 (small): the blond boy's single visible eye, reading it.\n"
  "PANEL 5 (small): the long-haired boy's pale eyes, reading the same line.\n"
  "PANEL 6 (wide, bottom): the two of them standing several places apart in the same line, both "
  "facing front, neither turning. " + HALL
  + SAY((3, "the proctor", "upper left", "FIRST MATCH OF THE FINALS — UZUMAKI NARUTO AGAINST HYUGA NEJI."),
        (6, LAZY, "upper right", "ONE MONTH TO PREPARE. WHAT A DRAG.")),
  R("naruto_13", "neji", "shikamaru", "env_prelim_arena"), "high"),

 ("p03", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=5),
  FILL + KAK.format(i=1) + N13.format(i=2) + ONLY(MAN, BOY) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): a corridor emptying, genin filing out past camera as legs and shoulders.\n"
  "PANEL 2 (small): a gloved hand catching the blond boy's shoulder from behind. Hands only.\n"
  "PANEL 3 (dominant, middle): the masked silver-haired man and the boy alone in the stone "
  "corridor, the man large in the foreground cropped by the right edge and turned three-quarters "
  "away, the boy small and stopped beyond him.\n"
  "PANEL 4 (small): the man's single visible eye, and it is not friendly this time.\n"
  "PANEL 5 (wide, bottom): the empty corridor, the boy alone in it. " + HALL
  + SAY((3, MAN, "upper left", "TRAINING GROUND. TOMORROW MORNING."),
        (4, MAN, "upper right", "AND NARUTO — I SAW THE MATCH. SO DID EVERY JONIN IN THE BUILDING.")),
  R("kakashi", "naruto_13"), "high"),

 ("p04", dict(scene="dialogue", light="dusk", cast="two", mood="calm", panels=6),
  FILL + N13.format(i=1) + JIR.format(i=2) + ENV.format(i=3) + ONLY(BOY, SAGE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blond boy alone on a wall above a river, from behind.\n"
  "PANEL 2 (small): his head turning sharply — he did not hear anyone arrive.\n"
  "PANEL 3 (dominant, middle): the big white-haired man sitting on the same wall an arm's length "
  "away, having simply appeared there, huge in the foreground cropped by the left edge, the boy "
  "small and squared-off beyond him. The size difference is the panel.\n"
  "PANEL 4 (small): the boy's hand, which has moved to where a sword hilt is not.\n"
  "PANEL 5 (small): the white-haired man's face, cheerful and reading him carefully.\n"
  "PANEL 6 (wide, bottom): the two of them on the wall, the village below. " + DUSK
  + SAY((3, SAGE, "upper right", "RELAX. IF I'D COME TO KILL YOU, YOU'D BE DEAD."),
        (6, SAGE, "upper left", "JIRAIYA. I HEAR YOU'RE INTERESTING.")),
  R("naruto_13", "jiraiya", "env_monument"), "high"),

 ("p05", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + JIR.format(i=1) + N13.format(i=2) + ONLY(SAGE, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the white-haired man's hand offered, palm up, between them.\n"
  "PANEL 2 (small): the boy's face, level.\n"
  "PANEL 3 (small): the man's face, still cheerful, watching for the answer.\n"
  "PANEL 4 (dominant, middle): the two of them on the wall in wide shot from far off, both small, "
  "the whole village and the carved cliff behind them — and the offered hand still out between "
  "them, unmistakable even at that scale.\n"
  "PANEL 5 (small): the boy's own hands, staying exactly where they are.\n"
  "PANEL 6 (wide, bottom): the man's face, the cheer draining out of it. " + DUSK
  + SAY((1, SAGE, "upper left", "ONE MONTH. I'LL TEACH YOU MYSELF."),
        (3, SAGE, "upper right", "YOUR FATHER WAS MY STUDENT. I OWE HIM THAT MUCH."),
        (5, BOY, "upper left", "NO."),
        (6, BOY, "lower right", "HE WAS NEVER MY FATHER. AND I DO NOT WANT ANYTHING YOU OWE HIM.")),
  R("jiraiya", "naruto_13"), "high"),

 ("p06", dict(scene="emotional_closeup", light="dusk", cast="two", mood="somber", panels=5),
  FILL + JIR.format(i=1) + N13.format(i=2) + ONLY(SAGE, BOY) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the offered hand closing and withdrawing.\n"
  "PANEL 2 (small): the white-haired man's face in close-up — no anger in it, which is worse.\n"
  "PANEL 3 (small): the boy already standing, already leaving.\n"
  "PANEL 4 (dominant, middle): the boy walking away along the top of the wall, small, with the big "
  "man still sitting where he was, cropped huge and dark in the foreground and not turning to "
  "watch him go.\n"
  "PANEL 5 (wide, bottom): the empty wall, the river, the village lights. " + DUSK
  + SAY((2, SAGE, "upper left", "YOU'LL REGRET THAT."),
        (4, OFF(BOY), "upper right", "I REGRET VERY LITTLE.")),
  R("jiraiya", "naruto_13"), "high"),

 ("p07", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ONLY(BOY, CREATURE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a bare apartment wall, apparently empty.\n"
  "PANEL 2 (small): the split black-and-white face emerging out of it at shoulder height.\n"
  "PANEL 3 (dominant, middle): the boy sitting on the floor of a bare room with his back against a "
  "couch, small and low in the frame, and the creature's head and shoulders standing out of the "
  "wall above and behind him — neither looking at the other.\n"
  "PANEL 4 (small): the creature's yellow eyes.\n"
  "PANEL 5 (small): the boy's face, taking it in without reacting.\n"
  "PANEL 6 (wide, bottom): the room, the window, the dark village beyond it. "
  "Lighting: one weak lamp, deep blue shadow. "
  + SAY((3, CREATURE, "upper left", "YAKUSHI KABUTO. FORMER ROOT — DANZO'S OWN SPY."),
        (4, CREATURE, "upper right", "HE HAS INFILTRATED EVERY GREAT VILLAGE. HE IS A MEDIC SECOND ONLY TO SENJU TSUNADE."),
        (6, CREATURE, "lower left", "AND HE HAS WORKED FOR OROCHIMARU FOR YEARS.")),
  R("naruto_13", "zetsu", "env_shinobi_apartment"), "high"),

 ("p08", dict(scene="emotional_closeup", light="dusk", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + ZET.format(i=2) + ONLY(BOY, CREATURE) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the boy's hand, flat on the floorboards.\n"
  "PANEL 2 (small): his single visible eye, working.\n"
  "PANEL 3 (small): the creature's split face, waiting for an instruction.\n"
  "PANEL 4 (dominant, middle): the boy standing at the dark window with the village below him, "
  "small at the bottom of a panel that is mostly black glass and reflected room — and his own faint "
  "doubled reflection is the only other figure in it.\n"
  "PANEL 5 (wide, bottom): the creature sinking back into the wall, only the shell showing. "
  "Lighting: one weak lamp, deep blue shadow. "
  + SAY((2, BOY, "upper left", "THEN OROCHIMARU IS NOT FINISHED WITH THIS VILLAGE."),
        (4, BOY, "upper right", "I HAVE ONE MONTH. IT WILL HAVE TO BE ENOUGH.")),
  R("naruto_13", "zetsu"), "high"),

 ("p09", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=6),
  FILL + HIR.format(i=1) + KAK.format(i=2) + ENV.format(i=3) + ONLY(OLD, MAN, "masked ANBU in "
    "plain animal masks and grey armour, none of them named") +
  "SIX panels, uneven. No dialogue from Naruto — he is not on this page at all.\n"
  "PANEL 1 (small): an apartment door, shut. Object only.\n"
  "PANEL 2 (small): a masked figure in a plain animal mask crouched on the roof opposite it.\n"
  "PANEL 3 (small): pale pupil-less eyes with the veins hard around them, staring at a wall — and "
  "seeing flat grey nothing.\n"
  "PANEL 4 (dominant, middle): the old man in the tall hat standing at his office window with his "
  "back to us, small against the glass, and three masked figures kneeling in a row behind him with "
  "their heads down, reporting failure. Deep space between him and them.\n"
  "PANEL 5 (small): the masked silver-haired man in the corner of the office, arms folded.\n"
  "PANEL 6 (wide, bottom): the office, the village beyond the window. "
  "Lighting: warm late-afternoon light through tall arched windows. "
  + CAP(1, "upper left", "THREE WEEKS.")
  + SAY((4, OLD, "upper right", "THREE WEEKS AND NOT ONE OF YOU CAN TELL ME WHERE HE IS."),
        (6, MAN, "upper left", "HE ISN'T IN THE VILLAGE. HIS CHAKRA ISN'T ANYWHERE.")),
  R("hiruzen", "kakashi", "env_hokage_office"), "high"),

 ("p10", dict(scene="emotional_closeup", light="dark", cast="solo", mood="tense", panels=5),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "FIVE panels, uneven. No dialogue. Where he actually went.\n"
  "PANEL 1 (small): a stone corridor cut into rock, torchlit, deep underground.\n"
  "PANEL 2 (small): a wall of carved stone tablets covered in dense illegible markings.\n"
  "PANEL 3 (small): the boy's single visible eye, blood-red with three black comma marks, "
  "reflecting the markings.\n"
  "PANEL 4 (dominant, middle): the boy standing alone in a vast underground chamber facing the "
  "tablet wall, very small at the bottom of the panel, the carved rock rising into darkness above "
  "and around him on every side.\n"
  "PANEL 5 (wide, bottom): his hand flat against the stone. "
  "Lighting: two torches, everything else black. ",
  R("naruto_13", "env_hideout_tablets"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch06" / "raw", HERE / "v3ch06" / "ledger.json")
