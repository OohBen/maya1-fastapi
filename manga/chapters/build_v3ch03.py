"""Volume 3, Chapter 3 — "The Tower". 14 pages.

Source: fic ch5, the run to the tower. A quiet chapter on purpose: it sits between the two
worst things that have happened to him and it is where Sakura stops being a burden without
anyone remarking on it. He is bound with N13 from here — the ninjato was lost in Chapter 2.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                       # noqa: E402
from prompts import (CAP, ENV, FILL, N13, ONLY, OFF, R, SAK, SAS, SAY, SFX,   # noqa: E402
                     TITLE, BOY, GIRL, UCH)

FOR = "Lighting: sunless green-black gloom under a dense canopy, hard shafts of pale light. "
DUSK = "Lighting: cold blue dusk, the last orange light going out of the canopy. "
MARK = ("The mark on the dark-haired boy's neck is THREE SMALL BLACK COMMA SHAPES in a circle — a "
        "flat graphic mark on unbroken skin, never a wound, no red, no injury detail. ")
IRU = ("Image {i} is the CHARACTER REFERENCE for the teacher: a man in his mid-twenties with dark "
       "brown hair pulled into a short spiky ponytail, a horizontal scar across the bridge of his "
       "nose, a dark navy uniform under a green flak vest. Expression: warm and tired. Reproduce "
       "exactly; ignore its white background and layout. ")
TEACH = "the man with the scar across his nose"

PAGES = [
 ("p01", dict(scene="establishing", light="dark", cast="none", mood="calm", panels=1),
  ENV.format(i=1) +
  "CHAPTER OPENING SPLASH. A single tall grey stone tower standing in a clearing at the centre of "
  "the forest, seen from within the treeline — the trunks of two colossal trees frame the view "
  "down both sides of the paper as the foreground mass, cropped by the edges, and the tower stands "
  "small and distant between them, its one lit doorway a tiny warm rectangle at the base. Mist "
  "across the clearing floor. No people anywhere. Leave the pale sky above the tower broad and "
  "quiet. "
  "Lighting: cold green-black forest in the foreground, pale open sky beyond the clearing. "
  + TITLE("THE TOWER", "pale sky above the tower"),
  R("env_forest_of_death"), "high"),

 ("p02", dict(scene="action", light="dark", cast="small_group", mood="somber", panels=6),
  FILL + N13.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(BOY, GIRL, UCH) +
  "SIX panels, uneven, columns not aligned. No dialogue on this page.\n"
  "PANEL 1 (small): two pairs of feet hitting a branch in step. Feet only.\n"
  "PANEL 2 (dominant, upper): the blond boy running along a high branch with the unconscious "
  "dark-haired boy over his shoulder, the pink-haired girl keeping pace a little behind — both "
  "small against enormous trunks, seen from below and to the side, the canopy rushing past.\n"
  "PANEL 3 (small): the girl's face, set. She is not complaining and nobody has noticed.\n"
  "PANEL 4 (small): the blond boy's face — worn out, which nobody has ever seen.\n"
  "PANEL 5 (small): the girl glancing sideways at him.\n"
  "PANEL 6 (wide, bottom): the two of them running on, tiny, the forest swallowing the frame. "
  + FOR,
  R("naruto_13", "sakura", "sasuke"), "medium"),

 ("p03", dict(scene="dialogue", light="dark", cast="small_group", mood="somber", panels=6),
  FILL + SAK.format(i=1) + SAS.format(i=2) + N13.format(i=3) + ONLY(GIRL, UCH, BOY) + MARK +
  "SIX panels, uneven. A halt beside a stream.\n"
  "PANEL 1 (small): the unconscious boy laid down on moss, seen from above.\n"
  "PANEL 2 (small): the three black comma marks on his neck, and the skin around them dark.\n"
  "PANEL 3 (small): the girl's hand on his forehead.\n"
  "PANEL 4 (dominant, middle): the girl kneeling over him in the foreground cropped by the bottom "
  "edge, and the blond boy standing well back at the water's edge with his back to both of them, "
  "small — the space between them is the panel.\n"
  "PANEL 5 (small): the blond boy's hand reaching back over his left shoulder out of habit, and "
  "closing on nothing.\n"
  "PANEL 6 (wide, bottom): the stream, the three of them spread across it. " + FOR
  + SAY((3, GIRL, "upper left", "IT'S GETTING WORSE."),
        (6, BOY, "upper right", "THERE IS NOTHING EITHER OF US CAN DO FOR IT HERE.")),
  R("sakura", "sasuke", "naruto_13"), "medium"),

 ("p04", dict(scene="emotional_closeup", light="dark", cast="solo", mood="somber", panels=5),
  FILL + N13.format(i=1) + ONLY(BOY) +
  "FIVE panels, uneven. No dialogue.\n"
  "PANEL 1 (small): still water, and a face reflected in it.\n"
  "PANEL 2 (small): the same reflection broken by a hand going in.\n"
  "PANEL 3 (small): dirt coming off his forearms in the water.\n"
  "PANEL 4 (dominant, middle): the blond boy crouched alone at the stream's edge, small at the "
  "bottom of a panel filled almost entirely by black water and black trees — and the empty strap "
  "across his back is dead centre of the composition.\n"
  "PANEL 5 (wide, bottom): his face in close-up, wet, jaw set. " + FOR,
  R("naruto_13"), "high"),

 ("p05", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + N13.format(i=1)
  + ONLY(BOY, "three teenage genin in unfamiliar dark clothing, none of them recurring") +
  "SIX panels, uneven, hard diagonals. This is over before it starts and should read that way.\n"
  "PANEL 1 (small): three unfamiliar genin dropping out of the canopy into a clearing.\n"
  "PANEL 2 (small): one of them grinning, a scroll held up in his fist.\n"
  "PANEL 3 (dominant, middle): the blond boy already standing among all three of them, having "
  "crossed the ground between — the three of them still mid-landing and only beginning to react, "
  "hard speed lines, flat opaque impact shapes. No injury detail of any kind.\n"
  "PANEL 4 (small): three figures on the ground, out cold, drawn small and slack. No injury "
  "detail.\n"
  "PANEL 5 (small): TWO scrolls in the blond boy's gloved hand, one pale and one dark.\n"
  "PANEL 6 (wide, bottom): the boy walking back out of the clearing, not looking behind him. "
  + FOR
  + SFX(3, "DON"),
  R("naruto_13"), "medium"),

 ("p06", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + SAS.format(i=1) + N13.format(i=2) + SAK.format(i=3) + ONLY(UCH, BOY, GIRL) + MARK +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy's eyes opening.\n"
  "PANEL 2 (small): his hand going straight to the marks on his own neck.\n"
  "PANEL 3 (small): the pink-haired girl's face, flooding with relief.\n"
  "PANEL 4 (dominant, middle): the dark-haired boy sitting up on the moss — and looking past the "
  "girl entirely, at the blond boy standing further off. The girl is between them and out of focus "
  "of the composition; the line of the panel runs from one boy to the other.\n"
  "PANEL 5 (small): the blond boy's single visible eye, returning the look.\n"
  "PANEL 6 (wide, bottom): the three of them at the stream, nobody moving. " + FOR
  + SAY((3, GIRL, "upper left", "SASUKE-KUN — YOU'RE AWAKE!"),
        (4, UCH, "upper right", "WHAT HAPPENED TO HIM? DID YOU FIGHT?"),
        (6, BOY, "upper left", "NO."),
        (6, BOY, "lower right", "WE HAVE BOTH SCROLLS. WE GO NOW.")),
  R("sasuke", "naruto_13", "sakura"), "high"),

 ("p07", dict(scene="establishing", light="dusk", cast="small_group", mood="calm", panels=5),
  FILL + ENV.format(i=1) + N13.format(i=2) + ONLY(BOY, UCH, GIRL) +
  "FIVE panels, uneven. No dialogue.\n"
  "PANEL 1 (small): three figures moving through the canopy, small and distant.\n"
  "PANEL 2 (small): the light in the forest going from green to blue.\n"
  "PANEL 3 (small): the dark-haired boy running under his own power now, jaw tight.\n"
  "PANEL 4 (dominant, middle): the treeline breaking open and the grey tower standing in the "
  "clearing beyond it, seen past the three of them cropped huge and dark in the foreground — they "
  "are silhouettes, the tower is the light.\n"
  "PANEL 5 (wide, bottom): the three of them crossing the open ground toward its doors, tiny. "
  + DUSK,
  R("env_forest_of_death", "naruto_13"), "high"),

 ("p08", dict(scene="dialogue", light="interior", cast="small_group", mood="calm", panels=6),
  FILL + N13.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(BOY, GIRL, UCH) +
  "SIX panels, uneven. A bare stone hall inside the tower.\n"
  "PANEL 1 (small): a heavy door closing behind them.\n"
  "PANEL 2 (small): the two scrolls laid side by side on a stone floor. Objects only.\n"
  "PANEL 3 (small): three hands, one on each scroll, unrolling.\n"
  "PANEL 4 (dominant, middle): both scrolls thrown down as flat white light and dense black seal "
  "markings pour up out of them in hard-edged shapes — the three of them recoiling at three "
  "different depths, one cropped by the panel edge. The markings must be illegible pattern, not "
  "readable words.\n"
  "PANEL 5 (small): flat white smoke filling the frame.\n"
  "PANEL 6 (wide, bottom): a figure standing in the clearing smoke, not yet resolved. "
  "Lighting: cold flat torchlight on grey stone. "
  + SAY((3, GIRL, "upper left", "IT'S A SUMMONING SEAL — THROW THEM DOWN!"))
  + SFX(4, "BOFUN"),
  R("naruto_13", "sakura", "sasuke"), "medium"),

 ("p09", dict(scene="dialogue", light="interior", cast="small_group", mood="calm", panels=6),
  FILL + IRU.format(i=1) + N13.format(i=2) + SAK.format(i=3) + ONLY(TEACH, BOY, GIRL, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the man with the scar across his nose, smiling, one hand raised.\n"
  "PANEL 2 (small): the pink-haired girl's face breaking into relief.\n"
  "PANEL 3 (small): the blond boy's face — nothing, but he has stopped bracing.\n"
  "PANEL 4 (dominant, middle): the four of them in the bare stone hall at four different depths, "
  "the teacher large in the foreground cropped by the left edge with his back half to us, the three "
  "genin small and filthy and still standing.\n"
  "PANEL 5 (small): the teacher's face changing as he takes in the state of them.\n"
  "PANEL 6 (wide, bottom): the hall, a stairway leading up out of it. "
  "Lighting: cold flat torchlight on grey stone. "
  + SAY((1, TEACH, "upper left", "CONGRATULATIONS. YOU'RE THROUGH THE SECOND TEST."),
        (5, TEACH, "upper right", "...WHAT IN GOD'S NAME HAPPENED TO YOU THREE?"),
        (6, BOY, "upper left", "NOTHING WORTH REPORTING.")),
  R("iruka", "naruto_13", "sakura"), "high"),

 ("p10", dict(scene="emotional_closeup", light="interior", cast="two", mood="somber", panels=6),
  FILL + SAS.format(i=1) + N13.format(i=2) + ONLY(UCH, BOY, TEACH) + MARK +
  "SIX panels, uneven. No dialogue.\n"
  "PANEL 1 (small): the dark-haired boy's collar pulled up higher on his neck, hiding something.\n"
  "PANEL 2 (small): his hand still on it.\n"
  "PANEL 3 (small): the blond boy watching him do it, from across the hall.\n"
  "PANEL 4 (small): the teacher, further off, seeing neither of them.\n"
  "PANEL 5 (dominant, middle): the two boys at opposite ends of a long bare stone corridor, both "
  "small, both facing away from each other, the corridor's emptiness filling everything between.\n"
  "PANEL 6 (wide, bottom): a stairway, and two sets of footsteps going up it. "
  "Lighting: cold flat torchlight on grey stone. ",
  R("sasuke", "naruto_13"), "medium"),

 ("p11", dict(scene="emotional_closeup", light="interior", cast="solo", mood="somber", panels=5),
  FILL + N13.format(i=1) + ONLY(BOY) +
  "FIVE panels, uneven. No dialogue. He sleeps, and we have never seen him do it.\n"
  "PANEL 1 (small): a plain bunk room, three narrow beds, bare walls. No people.\n"
  "PANEL 2 (small): black fingerless gloves dropped on a stone floor. Objects only.\n"
  "PANEL 3 (small): the empty strap coiled on a chair, no scabbard in it.\n"
  "PANEL 4 (narrow letterbox): his single visible eye closing.\n"
  "PANEL 5 (dominant, bottom): the blond boy asleep on his side on the bunk, still fully dressed, "
  "seen from across the dark room — small, curled, and for the first and only time in three volumes "
  "looking exactly like a thirteen-year-old. "
  "Lighting: one weak lamp, deep blue shadow. ",
  R("naruto_13"), "high"),

 ("p12", dict(scene="establishing", light="interior", cast="none", mood="tense", panels=4),
  FILL + ENV.format(i=1) +
  "FOUR panels, uneven. NO PEOPLE and no dialogue — the tower filling up overnight.\n"
  "PANEL 1 (small): the tower's doors from outside, at night.\n"
  "PANEL 2 (small): a corridor with more doors than there were, torches lit down its length.\n"
  "PANEL 3 (dominant, middle): the great bare arena hall standing empty and lit — the flat "
  "fighting floor, the two long balconies above it, the huge dark display board on the far wall, "
  "and the two colossal stone hands locked in a seal at the far end. Not one person in it.\n"
  "PANEL 4 (wide, bottom): the display board in close-up, dark and dead. Object only. "
  "Lighting: cold overhead light on grey stone, long shadows. "
  + CAP(1, "upper left", "FIVE DAYS LATER."),
  R("env_prelim_arena"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch03" / "raw", HERE / "v3ch03" / "ledger.json")
