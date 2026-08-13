"""Volume 2, Chapter 4 — "The War Hawk". 20 pages.

Source: fic ch4, the training-ground nomination through the Hokage-monument meeting with
Danzo. Dialogue is lifted close to verbatim; the fic is at its sharpest here.

What the chapter costs him: his obscurity. Danzo has now personally marked him — and the
page where he slips his watchers to be alone for ten minutes is the only privacy he gets in
the whole volume, which is why it is given a full quiet page before Danzo walks into it.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts import (DAN, ENV, FILL, KAK, N13, N13S, ONLY, OFF, R, SAK, SAS, SAY,  # noqa: E402
                     SFX, TITLE, ZET,
                     BOY, GIRL, HAWK, MAN, UCH, L_DAY, L_DUSK)

CREATURE = "the split black-and-white plant creature"

PAGES = [
 ("p01", dict(scene="establishing", light="dusk", cast="two", mood="tense", panels=1),
  N13S.format(i=1) + DAN.format(i=2) + ONLY(BOY, HAWK) +
  "CHAPTER OPENING SPLASH. Sunset on the carved stone heads of the cliff above the village. The "
  "blond boy sits on the very crown of one colossal stone head in the lower right of the paper, "
  "small, seen from behind, one knee up, the sword laid across it — the whole village spread out "
  "far below and behind him in flat bands of orange haze. The enormous carved stone brow is the "
  "foreground mass, cropped by the bottom edge of the paper. Far back at the top left of the stone, "
  "where the rock meets the sky, one small dark figure of an OLD MAN LEANING ON A CANE has stopped "
  "walking and is watching him. The old man is tiny and easy to miss. Leave the upper right sky "
  "broad and quiet. "
  "Lighting: low red sunset light raking across the stone, everything else falling into blue "
  "shadow. " + TITLE("THE WAR HAWK"),
  R("naruto_13_sword", "danzo"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + KAK.format(i=4) + ENV.format(i=5)
  + ONLY(BOY, UCH, GIRL, MAN) +
  "SIX panels, uneven, columns not aligned. The training clearing with its three wooden posts.\n"
  "PANEL 1 (small): the three weathered upright posts against the treeline. No people.\n"
  "PANEL 2 (dominant, upper): the blond boy leaning against the furthest post in the foreground, "
  "cropped by the right edge, arms folded; the dark-haired boy and the pink-haired girl walking in "
  "together from the treeline far behind him at a much smaller scale.\n"
  "PANEL 3 (small): the dark-haired boy glancing at him, then away.\n"
  "PANEL 4 (small): the girl looking between the two of them.\n"
  "PANEL 5 (small): a puff of flat white smoke in mid-air. No figures.\n"
  "PANEL 6 (wide, bottom): the masked silver-haired man standing in the clearing with one hand up "
  "in greeting and an orange book in the other, the three genin staring at him. " + L_DAY
  + SAY((6, MAN, "upper left", "YO."),
        (6, GIRL, "lower right", "SENSEI... WHY AREN'T YOU LATE?")),
  R("naruto_13_sword", "sasuke", "sakura", "kakashi", "env_training_ground_7"), "medium"),

 ("p03", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + KAK.format(i=1) + SAS.format(i=2) + N13S.format(i=3) + SAK.format(i=4)
  + ONLY(MAN, UCH, BOY, GIRL) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the masked man's single visible eye curved into a cheerful crescent.\n"
  "PANEL 2 (small): the dark-haired boy, scowling, unimpressed.\n"
  "PANEL 3 (small): the masked man flipping a page of the orange book, not looking up.\n"
  "PANEL 4 (small): the dark-haired boy's fists.\n"
  "PANEL 5 (dominant, middle): the masked man closing the book one-handed — the first time he has "
  "looked at any of them properly. He is large in the foreground cropped by the left edge; the "
  "three genin are small and beyond him at three different depths.\n"
  "PANEL 6 (wide, bottom): the four of them in the clearing, the posts between them. " + L_DAY
  + SAY((1, MAN, "upper left", "IS IT REALLY THAT SURPRISING?"),
        (2, UCH, "upper right", "WHY DID YOU BRING US HERE? WE'RE STILL ON LEAVE."),
        (3, MAN, "lower left", "CAN'T A TEAM SIMPLY SPEND TIME TOGETHER?"),
        (5, BOY, "upper right", "THEN LET'S HEAR IT.")),
  R("kakashi", "sasuke", "naruto_13_sword", "sakura"), "medium"),

 ("p04", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + KAK.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + N13S.format(i=4)
  + ONLY(MAN, UCH, GIRL, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the masked man holding out three folded paper forms in a fan, hand "
  "enormous in the foreground cropped by the bottom edge, the three genin small beyond it, all "
  "three reacting differently.\n"
  "PANEL 2 (small): the dark-haired boy's face — an actual, hungry smile.\n"
  "PANEL 3 (small): the pink-haired girl's face — not a smile at all.\n"
  "PANEL 4 (small): the blond boy's face — nothing whatsoever. Flat tone behind him.\n"
  "PANEL 5 (small): one paper form in a black-gloved hand. Object only.\n"
  "PANEL 6 (wide, bottom): the three of them holding their forms at three different depths, the "
  "masked man already half-turned away. " + L_DAY
  + SAY((1, MAN, "upper left", "I'VE NOMINATED ALL THREE OF YOU FOR THE CHUNIN SELECTION EXAMS."),
        (6, MAN, "upper right", "ROOM 301. TOMORROW, EIGHT A.M. — IF YOU WANT IT.")),
  R("kakashi", "sasuke", "sakura", "naruto_13_sword"), "high"),

 ("p05", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + SAK.format(i=1) + KAK.format(i=2) + SAS.format(i=3) + ONLY(GIRL, MAN, UCH, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pink-haired girl gripping her form with both hands.\n"
  "PANEL 2 (small): the masked man's eye, kinder than usual.\n"
  "PANEL 3 (dominant, middle): the clearing from behind the girl's shoulder, cropped huge and dark "
  "in the foreground, the masked man small and central beyond her with one hand raised.\n"
  "PANEL 4 (small): the girl's face going pale at something said.\n"
  "PANEL 5 (small): a puff of flat white smoke where he was standing. No figure.\n"
  "PANEL 6 (wide, bottom): the three genin left alone in the clearing, well apart from each other. "
  + L_DAY
  + SAY((1, GIRL, "upper left", "SENSEI — ARE YOU SURE WE'RE READY?"),
        (2, MAN, "upper right", "IF I DIDN'T BELIEVE IT, I WOULD NEVER HAVE PUT YOUR NAMES IN."),
        (3, MAN, "lower right", "THOUGH YOU MAY MEET GENIN AS STRONG AS NARUTO. OR AS STRONG AS HAKU."),
        (4, OFF(MAN), "upper left", "YOU REMEMBER HAKU."))
  + SFX(5, "POFU"),
  R("sakura", "kakashi", "sasuke"), "medium"),

 ("p06", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=5),
  FILL + SAS.format(i=1) + N13S.format(i=2) + ONLY(UCH, BOY, GIRL) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy's hand closing tight on his form, creasing it.\n"
  "PANEL 2 (dominant, upper): the dark-haired boy stopped in front of the blond boy — the blond boy "
  "huge in the foreground cropped by the right edge showing only his shoulder and jaw, the "
  "dark-haired boy small and facing him, smiling for the first time in the volume.\n"
  "PANEL 3 (small): the blond boy's single visible eye. Unmoved.\n"
  "PANEL 4 (small): the dark-haired boy walking away toward the treeline, seen from behind, still "
  "holding the form.\n"
  "PANEL 5 (wide, bottom): the blond boy alone by the wooden posts, the form hanging from one hand, "
  "the empty clearing around him. " + L_DAY
  + SAY((2, UCH, "upper left", "I HOPE YOU ENTER. I REALLY WANT TO FIGHT YOU, NARUTO.")),
  R("sasuke", "naruto_13_sword"), "high"),

 ("p07", dict(scene="dialogue", light="day", cast="solo", mood="calm", panels=5),
  FILL + N13S.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "FIVE panels, uneven. No dialogue on this page at all.\n"
  "PANEL 1 (small): the paper form held up, seen edge-on. Object only, writing illegible.\n"
  "PANEL 2 (small): the blond boy's face looking down at it, tired rather than blank — the only "
  "moment in the chapter where he looks like a thirteen-year-old.\n"
  "PANEL 3 (small): the form folded once and pushed into a pocket.\n"
  "PANEL 4 (narrow letterbox): his eye, cropped by all four edges.\n"
  "PANEL 5 (wide, bottom): the empty training ground behind him as he walks out of frame at the "
  "right edge, half cropped. " + L_DAY,
  R("naruto_13_sword", "env_training_ground_7"), "medium"),

 ("p08", dict(scene="action", light="day", cast="solo", mood="tense", panels=6),
  FILL + N13S.format(i=1) + KAK.format(i=2) + ENV.format(i=3) + ONLY(BOY, MAN) +
  "SIX panels, uneven. This page is a TRICK the reader must be able to follow: he splits himself "
  "in two and gives his watchers the wrong one.\n"
  "PANEL 1 (small): two fingers crossed in a seal in front of his face. Hand only.\n"
  "PANEL 2 (small): flat white smoke beside him in a narrow alley.\n"
  "PANEL 3 (dominant, middle): TWO identical blond boys standing in the alley, one already turning "
  "left and one right, at different depths, one cropped by the panel edge. Above and behind them, "
  "small on a rooftop, the masked silver-haired man is watching.\n"
  "PANEL 4 (small): the masked man's single eye tracking — following the WRONG one.\n"
  "PANEL 5 (small): one blond boy walking on into a busy street. From behind.\n"
  "PANEL 6 (wide, bottom): the other one alone in an empty back lane, nobody above him, nobody "
  "behind him. The first empty rooftops in the whole volume. " + L_DAY
  + SFX(2, "POFU"),
  R("naruto_13_sword", "kakashi", "env_village_street"), "high"),

 ("p09", dict(scene="establishing", light="dusk", cast="solo", mood="calm", panels=4),
  FILL + N13S.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "FOUR panels only — this page is deliberately QUIET and slow, and it is the only privacy he gets "
  "in the whole volume. No dialogue anywhere on it.\n"
  "PANEL 1 (small): the carved stone faces of the cliff seen from far below, tiny against the sky.\n"
  "PANEL 2 (small): sandals on bare stone, walking. No face.\n"
  "PANEL 3 (dominant, middle): the blond boy sitting alone on the crown of an enormous carved stone "
  "head, small and off centre, the whole village laid out below him in flat bands of orange haze to "
  "a far horizon. Nobody else anywhere in the panel.\n"
  "PANEL 4 (wide, bottom): his face in profile, cropped tight, the sword laid across his knee. His "
  "expression is the closest thing to peace he has. " + L_DUSK,
  R("naruto_13_sword", "env_monument"), "high"),

 ("p10", dict(scene="emotional_closeup", light="dusk", cast="two", mood="tense", panels=6),
  FILL + N13S.format(i=1) + DAN.format(i=2) + ENV.format(i=3) + ONLY(BOY, HAWK) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blond boy's eye opening. It has stopped being peaceful.\n"
  "PANEL 2 (small): a wooden cane tip setting down on stone. Object only, no figure.\n"
  "PANEL 3 (small): the boy's head beginning to turn, from behind.\n"
  "PANEL 4 (dominant, middle): the bandaged old man standing on the stone against the red sky, seen "
  "from a LOW angle so he towers, the whole right side of his body wrapped in white and held in a "
  "sling, one eye bandaged, leaning on the cane. The boy is small and seated at the bottom edge of "
  "the panel with his back to us.\n"
  "PANEL 5 (small): the old man's single uncovered eye, close.\n"
  "PANEL 6 (wide, bottom): the two of them on the stone head, far apart, the village below. "
  + L_DUSK
  + SAY((6, BOY, "upper left", "SHIMURA DANZO."),
        (6, BOY, "lower right", "I WAS WONDERING WHEN YOU WOULD COME.")),
  R("naruto_13_sword", "danzo", "env_monument"), "high"),

 ("p11", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + DAN.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(HAWK, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the old man's bandaged right hand resting on the head of the cane.\n"
  "PANEL 2 (dominant, upper): both of them looking out over the village rather than at each other — "
  "the old man standing large in the foreground cropped by the left edge, the boy seated small and "
  "far to the right, the whole village between and below them.\n"
  "PANEL 3 (small): the boy in profile, entirely unimpressed.\n"
  "PANEL 4 (small): the X-shaped scar on the old man's chin, cropped tight.\n"
  "PANEL 5 (small): the village lights coming on far below. No people.\n"
  "PANEL 6 (wide, bottom): the old man's back as he turns fractionally toward the boy. " + L_DUSK
  + SAY((2, HAWK, "upper left", "THE VILLAGE LOOKS PEACEFUL FROM UP HERE, DOES IT NOT?"),
        (3, BOY, "upper right", "IT IS LOVELY."),
        (6, BOY, "upper right", "GET TO THE POINT. YOU DID NOT CLIMB THIS FAR TO DISCUSS THE VIEW.")),
  R("danzo", "naruto_13_sword", "env_monument"), "high"),

 ("p12", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + DAN.format(i=1) + N13S.format(i=2) + ONLY(HAWK, BOY) +
  "SIX panels, uneven. Escalate by cropping tighter.\n"
  "PANEL 1 (small): the old man's mouth, thin and level.\n"
  "PANEL 2 (small): the boy's face, flat, three-quarters away.\n"
  "PANEL 3 (dominant, middle): the boy standing up for the first time — he is small and the old man "
  "is large, but the composition puts the boy at the top of the frame and the old man below him on "
  "the slope of the stone, so the height advantage is the boy's.\n"
  "PANEL 4 (small): the old man's uncovered eye narrowing by a fraction.\n"
  "PANEL 5 (narrow letterbox): the boy's single visible eye, cropped by all four edges, flat black "
  "behind it.\n"
  "PANEL 6 (wide, bottom): the two of them squared off on the stone against the last of the light. "
  + L_DUSK
  + SAY((1, HAWK, "upper left", "I HAVE A PROPOSITION FOR YOU."),
        (3, BOY, "upper right", "I HAVE NO INTEREST IN JOINING YOUR ROOT."),
        (5, BOY, "upper left", "IN FACT I HAVE NO INTEREST IN ASSOCIATING MYSELF WITH YOU AT ALL.")),
  R("danzo", "naruto_13_sword"), "high"),

 ("p13", dict(scene="emotional_closeup", light="dusk", cast="two", mood="tense", panels=6),
  FILL + DAN.format(i=1) + N13S.format(i=2) + ONLY(HAWK, BOY) +
  "SIX panels, uneven. This is the page where the old man is genuinely thrown, and it must be "
  "visible in ONE eye only.\n"
  "PANEL 1 (dominant, top): the old man's face filling the panel, cropped so tightly that the "
  "bandaged right side and the single open left eye are all there is. Hard hatch lines. This is the "
  "biggest panel on the page.\n"
  "PANEL 2 (small): his bandaged hand tightening on the cane.\n"
  "PANEL 3 (small): the boy, unbothered, hands at his sides.\n"
  "PANEL 4 (small): the cane tip grinding a fraction against the stone.\n"
  "PANEL 5 (small): the boy's mouth, mid-sentence, flat.\n"
  "PANEL 6 (wide, bottom): the two of them, the sky behind them almost gone. " + L_DUSK
  + SAY((1, HAWK, "upper left", "HOW DO YOU KNOW OF ROOT?"),
        (3, BOY, "upper right", "ROOT IS NOT MUCH OF A SECRET."),
        (5, BOY, "upper left", "WHAT YOU DO WITH IT IS THE SECRET."),
        (6, BOY, "lower right", "I AM NOT A THREAT TO THIS VILLAGE. WHATEVER YOU HAVE DECIDED.")),
  R("danzo", "naruto_13_sword"), "high"),

 ("p14", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=5),
  FILL + DAN.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(HAWK, BOY) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the old man turning away, the cane taking his weight.\n"
  "PANEL 2 (small): his back, the sling and the bandaged arm.\n"
  "PANEL 3 (dominant, middle): the old man walking away along the top of the carved stone head, "
  "small against an enormous darkening sky, the boy standing motionless in the foreground cropped "
  "by the bottom edge showing only his shoulder and the back of his head.\n"
  "PANEL 4 (small): the stone where he was standing. Empty.\n"
  "PANEL 5 (wide, bottom): the boy alone again, the village lit below him. " + L_DUSK
  + SAY((3, HAWK, "upper left", "MY OFFER STANDS."),
        (3, HAWK, "lower right", "I CAN MAKE YOU GREAT. I CAN TEACH YOU TO CONTROL THE FOX.")),
  R("danzo", "naruto_13_sword", "env_monument"), "high"),

 ("p15", dict(scene="dialogue", light="dusk", cast="two", mood="calm", panels=6),
  FILL + N13S.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ONLY(BOY, CREATURE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): bare stone at the boy's feet. Nothing there.\n"
  "PANEL 2 (small): the same stone, with a split black-and-white head now protruding from it like a "
  "mushroom — no body, just the head and the green shell.\n"
  "PANEL 3 (small): the boy looking down at it without any surprise at all.\n"
  "PANEL 4 (dominant, middle): the two of them on the stone head at dusk, the creature's head at "
  "ankle height in the foreground cropped huge by the bottom edge, the boy standing small beyond "
  "it, the village far below.\n"
  "PANEL 5 (small): the creature's split face, grinning.\n"
  "PANEL 6 (wide, bottom): both of them looking out at the village, neither facing the other. "
  + L_DUSK
  + SAY((3, BOY, "upper left", "HOW LONG HAVE YOU BEEN THERE?"),
        (5, "the plant creature", "upper right", "LONG ENOUGH TO HEAR ALL OF IT.")),
  R("naruto_13_sword", "zetsu", "env_monument"), "medium"),

 ("p16", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + N13S.format(i=1) + ZET.format(i=2) + DAN.format(i=3) + ONLY(BOY, CREATURE, HAWK) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the boy in profile against the last light.\n"
  "PANEL 2 (small): the creature's yellow eyes, pleased with itself.\n"
  "PANEL 3 (dominant, middle): a FLASHBACK-style inset of the bandaged old man walking away down a "
  "stone stair, and clinging unnoticed to the shoulder of his white robe a tiny pale seed-like "
  "SPORE, drawn small but unmistakable. Draw this panel with a ragged torn-paper border to mark it "
  "as elsewhere.\n"
  "PANEL 4 (small): the spore in extreme close-up on white cloth. Object only.\n"
  "PANEL 5 (small): the boy's mouth, the nearest thing to satisfaction he shows.\n"
  "PANEL 6 (wide, bottom): the boy and the creature's head on the stone, night now, the village a "
  "field of small lights. " + L_DUSK
  + SAY((1, BOY, "upper left", "DID YOU PUT A SPORE ON HIM?"),
        (2, "the plant creature", "upper right", "I ASSUMED YOU WOULD WANT ONE."),
        (5, BOY, "upper left", "GOOD. THAT MAN IS SLIPPERY."),
        (6, BOY, "lower right", "NOW I WILL KNOW WHERE HE GOES AND WHO HE SPEAKS TO.")),
  R("naruto_13_sword", "zetsu", "danzo"), "high"),

 ("p17", dict(scene="dialogue", light="dusk", cast="two", mood="somber", panels=6),
  FILL + N13S.format(i=1) + ZET.format(i=2) + ONLY(BOY, CREATURE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the creature's split face, head tilted, asking.\n"
  "PANEL 2 (small): the boy's face, giving nothing.\n"
  "PANEL 3 (small): his hand on the hilt of the sword over his shoulder.\n"
  "PANEL 4 (dominant, middle): the boy seen from BEHIND and far away, small at the edge of the "
  "enormous carved stone head, the whole night village below him — the loneliest composition in the "
  "chapter.\n"
  "PANEL 5 (small): the creature sinking back into the stone, only the top of the shell showing.\n"
  "PANEL 6 (wide, bottom): the boy alone, from the front, cropped tight. " + L_DUSK
  + SAY((1, "the plant creature", "upper left", "WHEN DO YOU MOVE AGAINST HIM?"),
        (2, BOY, "upper right", "IN TIME. I AM NOT STRONG ENOUGH YET."),
        (6, "the plant creature", "upper left", "STAYING IN THIS VILLAGE IS NOT MAKING YOU STRONGER.")),
  R("naruto_13_sword", "zetsu"), "high"),

 ("p18", dict(scene="emotional_closeup", light="dusk", cast="solo", mood="somber", panels=5),
  FILL + N13S.format(i=1) + ENV.format(i=2) + ONLY(BOY) +
  "FIVE panels, uneven. Escalate by cropping tighter, not by adding rendering.\n"
  "PANEL 1 (small): his hand flat on cold stone.\n"
  "PANEL 2 (small): the folded paper form pulled half out of his pocket.\n"
  "PANEL 3 (narrow letterbox): his single visible eye, cropped by all four edges.\n"
  "PANEL 4 (small): the stone where the creature was. Nothing there now.\n"
  "PANEL 5 (dominant, bottom): the boy very small at the bottom of the panel, the enormous night "
  "sky and the carved stone filling everything above him. " + L_DUSK
  + SAY((3, BOY, "upper left", "I KNOW."),
        (5, BOY, "upper right", "I WILL THINK OF SOMETHING AFTER THE EXAMS.")),
  R("naruto_13_sword", "env_monument"), "high"),

 ("p19", dict(scene="establishing", light="dusk", cast="none", mood="tense", panels=5),
  FILL + ENV.format(i=1) +
  "FIVE panels, uneven. NO CHARACTERS AT ALL on this page and no dialogue — it is the village "
  "watching itself.\n"
  "PANEL 1 (small): a shuttered window with a light behind it.\n"
  "PANEL 2 (small): an empty rooftop, a weather vane, nobody on it.\n"
  "PANEL 3 (dominant, middle): a long dark corridor somewhere underground, lit by a single lamp, "
  "with many identical blank ANIMAL MASKS hanging on the wall in a row — no faces behind them, no "
  "people anywhere in the panel.\n"
  "PANEL 4 (small): one mask in close-up, plain and expressionless. Object only.\n"
  "PANEL 5 (wide, bottom): the exam academy building at night, seen from across the plaza, every "
  "window dark except one on the third floor. " + L_DUSK,
  R("env_hideout_corridor"), "medium"),

 ("p20", dict(scene="establishing", light="day", cast="small_group", mood="calm", panels=5),
  FILL + N13S.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, UCH, GIRL) +
  "FIVE panels, uneven. Morning. The chapter ends by putting the three of them at a door.\n"
  "PANEL 1 (small): the academy steps in clean morning light. No people.\n"
  "PANEL 2 (small): the dark-haired boy and the pink-haired girl waiting at the entrance, at "
  "different depths, one half-turned.\n"
  "PANEL 3 (dominant, middle): the blond boy arriving from the right, the sword clear across his "
  "back, seen at an angle from behind and below so the sword dominates his silhouette; the other "
  "two small and beyond him.\n"
  "PANEL 4 (small): the dark-haired boy's eyes on the sword.\n"
  "PANEL 5 (wide, bottom): the three of them going in through the academy doors, seen from inside "
  "the dark entrance hall so they are silhouettes against the bright doorway. " + L_DAY
  + SAY((4, UCH, "upper left", "YOU KNOW HOW TO USE A SWORD?"),
        (5, BOY, "upper right", "NOT WELL."),
        (5, BOY, "lower left", "IT IS USEFUL FOR DEALING WITH ANNOYANCES.")),
  R("naruto_13_sword", "sasuke", "sakura", "env_academy_ext"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v2ch04" / "raw", HERE / "v2ch04" / "ledger.json")
