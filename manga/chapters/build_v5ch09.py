"""Volume 5, Chapter 9 — "Home". 18 pages.

Source: fic ch15:5-201. Translated 1:1 from story/volume_05/drafts/ch09_home.md —
123 spoken balloons, nine SFX, two location cards and one chapter marker. Reading order is
RIGHT TO LEFT per the approved `name`; every page states it.

The chapter returns to Konoha: the road and the main gate, the shinobi district, Naruto's old
apartment, and the Uchiha compound (street, training ground, garden and library). Every page
binds its environment plate from refs/images.

MISSING REFERENCE SHEETS (reported, never invented): there is no Ōnoki sheet, no Iwagakure
office plate, no Konoha main-gate plate, no masked-ANBU sheet and no Uchiha-library plate in
refs/images. Pages 1-2 therefore reuse the kage-office architecture plate with an explicit
"different village" override and describe Ōnoki, the messenger and the Iwa ANBU in prose only;
the gate and library pages reuse the nearest Konoha and Uchiha plates the same way.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, KAK, MAN, OFF, ONLY, R, SAY, SFX  # noqa: E402
from prompts_v4 import (GUNBAI_V4, KARIN, N16_ARMOR, N16_SWORD, SASUKE16,   # noqa: E402
                        KARIN_SPEAKER, N16_SPEAKER, SASUKE16_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
KAR = KARIN_SPEAKER
SAS16 = SASUKE16_SPEAKER
KAKA = MAN

# ---------------------------------------------------------------- crowd binding
MOB = ("Image {i} is the CROWD REFERENCE for unnamed Konoha villagers and off-duty shinobi: "
       "ordinary civilian clothes and plain dark shinobi wear with deliberately varied builds, "
       "ages, hair and faces. They stay anonymous and must never resemble a named character. "
       "Reproduce the visual vocabulary, not the sheet arrangement. ")

# ---------------------------------------------------------------- prose-only cast
# No reference sheet exists for any of these; each is described completely so the model has no
# room to substitute a familiar face. See the module docstring.
ONOKI = ("one very short, very old male village leader — barely waist-high to an adult, with a "
         "large red bulbous nose, a thick grey handlebar moustache, a pointed grey chin beard, "
         "small narrow eyes, and heavy dark formal kage robes over a wide stiff collar; he is NOT "
         "a Leaf character and wears no Leaf symbol")
ONO = "the tiny old village leader with the big red nose and the handlebar moustache"
MESSENGER = ("one breathless young male messenger in a plain dark uniform with a rolled paper "
             "report in his hand, unnamed and non-recurring")
MSGR = "the young messenger holding the rolled report"
IWA_ANBU = ("four kneeling masked agents in plain featureless pale porcelain animal masks with "
            "narrow eye slits and grey-brown hooded cloaks, none of them ever unmasked")
GUARD_DESC = ("one Konoha gate guard: an unnamed adult male chunin in a dark navy uniform under a "
              "green flak vest with a Leaf forehead protector, non-recurring and never unmasked "
              "because he wears no mask")
GUARD = "the gate guard in the green flak vest"
WATCHERS = ("three tiny distant masked Leaf watchers standing on separate far rooftops, each too "
            "small and too far away to identify, in plain pale animal masks and grey cloaks")
LEAF_ANBU = ("one kneeling masked Leaf agent in a plain pale porcelain animal mask, grey cloak and "
             "dark shoulder armour, never unmasked")
ANBU = "the kneeling masked Leaf agent"

# ---------------------------------------------------------------- lettering
# Page-QA gate on ch09 p17 / ch10 p17: the macron in DANZŌ and HANZŌ came back as an umlaut on one
# balloon and a tilde on the next, so the same name was spelled two different ways on one page.
# The macron is kept (the rest of the volume already letters it correctly); it is now described.
MACRON = ("MACRON RULE FOR THIS PAGE: wherever a capital O carries a macron — DANZŌ, HANZŌ, "
          "MANGEKYŌ, DŌJUTSU — that mark is ONE SINGLE STRAIGHT HORIZONTAL BAR sitting directly "
          "above the letter, the full width of the O and no thicker than the lettering stroke. It "
          "is NEVER two dots, NEVER a wavy tilde, NEVER an accent slanting up or down, and never "
          "an umlaut. Every occurrence of the same name on this page is lettered identically. ")

# ---------------------------------------------------------------- Naruto's carried state
ARMED = ("On this page he carries BOTH the dark purple gunbai on his back AND a plain straight "
         "sword in a dark sash sheath at his left hip. That sash sword is a plain, undecorated new "
         "blade — it is NOT the lost ninjato and NOT a grass-cutter sword — and it stays SHEATHED "
         "in every panel. ")
UNARMED = ("OVERRIDE the reference sheet on this page: he carries NO gunbai and NO sword of any "
           "kind. His back is empty and both hips are empty, because the war fan and the sheathed "
           "sword were left standing in his room. ")
PALE = ("A slight pallor shows in his face on this page. He never coughs, never staggers and never "
        "touches his own body; nobody reacts to it unless the panel says so. ")

# ---------------------------------------------------------------- light
L_IWA = ("Lighting: warm low lamplight in a night office, the window black, deep shadow beyond the "
         "desk and a single pool of light on the paperwork. ")
L_ROAD = ("Lighting: pale gold morning haze along the approach road, long soft shadows, the "
          "village wall still cool and blue in the distance. ")
L_STREET = "Lighting: clean flat midday daylight between village rooftops, short hard shadows. "
L_HOUSE = ("Lighting: dusty interior daylight through half-shuttered windows, soft, still, with "
           "slow motes hanging in the beams. ")
L_COMP = ("Lighting: flat overcast afternoon light across an empty walled compound — even, "
          "shadowless and without warmth. ")
L_GARDEN = ("Lighting: low amber late-afternoon light raking across a walled garden, long shadows "
            "reaching along the veranda boards. ")
L_LIB = ("Lighting: cool even light diffused through paper screens inside a shelved archive room, "
         "the shelf tops falling into soft shadow. ")

PAGES = [
 # ---- Spread 1: a delayed report ---------------------------------------------------
 ("p01", dict(scene="dialogue", light="night", cast="two", mood="tense", panels=5),
  FILL + RTL + ENV.format(i=1)
  + "OVERRIDE the location plate's identity: this is a DIFFERENT VILLAGE'S kage office, not the "
    "Leaf one. Reuse only its general room construction, desk scale and window proportion; make "
    "the walls carved stone-brown, and remove every Leaf leaf-spiral symbol, banner and portrait. "
  + ONLY(ONO, MESSENGER) +
  "FIVE panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width. Tier 2 is "
  "PANEL 2 on the reader-right half and PANEL 3 on the reader-left half. Tier 3 is PANEL 4 full "
  "width. Tier 4 is PANEL 5 full width and the tallest.\n"
  "PANEL 1 (full-width top strip): night in the stone kage office. The tiny old leader sits at "
  "the LEFT behind a low field of stacked paperwork, gaze down at his brush; the closed door "
  "stands at the FAR RIGHT, so the eye travels from the entrance leftward to him. The UPPER LEFT "
  "WALL of this panel is PROTECTED EMPTY NEGATIVE SPACE — no figure, furniture, shadow or balloon "
  "may enter it — and carries only the chapter marker. A separate patch of blank wall at the "
  "upper right carries the location card. Leave clear blank wall between the two text units; they "
  "never share a box.\n"
  "PANEL 2 (second tier, reader-right rectangle): the door bursts inward from right to left. The "
  "breathless young messenger leans into the room, one hand braced on the frame, the rolled "
  "report held forward.\n"
  "PANEL 3 (second tier, reader-left rectangle): the old leader's head comes up toward the "
  "messenger away at page-right; the stopped brush in his hand points LEFT, carrying the read on.\n"
  "PANEL 4 (full-width third tier): the messenger in the foreground at right, the old leader small "
  "in the background at left. The messenger holds the report out in the space between them and "
  "does not approach the desk.\n"
  "PANEL 5 (full-width bottom, the focal panel and the tallest): the old leader's hand closes "
  "around the near edge of the report; his one visible eye is sharp above it, aimed off-panel "
  "RIGHT toward the messenger, who is cropped out. " + L_IWA
  + 'LETTERING: in the protected upper-left wall area of PANEL 1, write the chapter marker in '
    'bold upright English capitals on one line: "CHAPTER 9 — HOME". It is a tail-less title, not '
    'a balloon, and it must not touch the location card. '
  + CAP(1, "upper right on blank wall", "IWAGAKURE.")
  + SFX(2, "BANG", "Angled leftward beside the flung door, cropped by the panel edge.")
  + SAY((2, MSGR, "upper right", "TSUCHIKAGE-SAMA!"),
        (3, ONO, "upper right", "WHAT IS IT?"),
        (4, MSGR, "upper right", "UCHIHA NARUTO ENTERED EARTH COUNTRY A WEEK AGO."),
        (4, MSGR, "upper left", "HE LEFT THE SAME DAY."),
        (5, ONO, "upper right", "WHY AM I HEARING THIS NOW?")),
  R("env_hokage_office"), "high"),

 ("p02", dict(scene="dialogue", light="night", cast="small_group", mood="tense", panels=5),
  FILL + RTL + ENV.format(i=1)
  + "OVERRIDE the location plate's identity exactly as on the previous page: a DIFFERENT "
    "VILLAGE'S stone kage office, no Leaf symbol anywhere. "
  + ONLY(ONO, MESSENGER, IWA_ANBU) +
  "FIVE panels. The order becomes an investigation.\n"
  "PANEL 1 (small, upper right): the messenger bows lower, eyes on the floor. The old leader is "
  "off-panel to the left and is not drawn.\n"
  "PANEL 2 (small, upper left): the old leader reads the single sheet. The messenger is only a "
  "blurred shoulder at the right edge, preserving their eye-line.\n"
  "PANEL 3 (wide, middle band): the messenger points to a marked border sector on the sheet laid "
  "flat across the desk; the mark sits toward page-LEFT, guiding the eye onward. Every mark and "
  "label on the sheet is ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 4 (thin reaction band): the old leader's visible eye narrows to a slit. The room behind "
  "him is empty.\n"
  "PANEL 5 (dominant bottom panel, the focal panel): four kneeling masked agents form a shallow "
  "arc across the foreground from right to left, backs to the reader, every masked face angled "
  "UP. The old leader stands behind the desk at upper left, holding the report so it points down "
  "toward them. " + L_IWA
  + SFX(4, "SHFF", "Small, low left behind his chair, where the agents arrive.")
  + SAY((1, MSGR, "upper right", "THE REPORT REACHED ME TONIGHT."),
        (2, ONO, "upper right", "WHERE WAS HE SEEN?"),
        (3, MSGR, "upper right", "AT THE EARTH COUNTRY BORDER."),
        (4, ONO, "upper right", "ANBU."),
        (5, ONO, "upper right", "FIND WHERE HE WENT."),
        (5, ONO, "upper left", "FIND WHAT HE DID.")),
  R("env_hokage_office"), "medium"),

 # ---- Spread 2: the terms of arrival -----------------------------------------------
 ("p03", dict(scene="establishing", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR) + ARMED + PALE +
  "SIX panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width. Tier 2 is "
  "PANEL 2 reader-right and PANEL 3 reader-left in equal rectangles. Tier 3 is PANEL 4 "
  "reader-right and PANEL 5 reader-left in equal rectangles. Tier 4 is PANEL 6 full width and the "
  "tallest.\n"
  "PANEL 1 (full-width top establishing strip): the village's great gate sits FAR LEFT in morning "
  "haze. The blond teen walks from the right toward it in red armour. The red-haired girl in "
  "glasses walks beside him, half a pace FARTHER FROM THE VILLAGE and never behind him. Both look "
  "left. The location card sits at the upper right on open sky. No balloon in this panel.\n"
  "PANEL 2 (second tier, reader-right): medium profile two-shot — he watches the road, she keeps "
  "her eyes on the gate.\n"
  "PANEL 3 (second tier, reader-left): close on the red-haired girl, shoulders held tight under "
  "her coat; she glances sideways to her right toward him.\n"
  "PANEL 4 (third tier, reader-right): close on the blond teen. His eye-line stays on the gate.\n"
  "PANEL 5 (third tier, reader-left): close on the red-haired girl ALONE — the blond teen is NOT "
  "drawn in this panel. She looks from where his blond hair was toward the gates, unconvinced.\n"
  "PANEL 6 (full-width bottom, the focal panel): he is one stride ahead but looks back over his "
  "shoulder; she meets his eye rather than hurrying to close the gap. The gate is behind them. "
  + L_ROAD
  + CAP(1, "upper right", "KONOHA.")
  + SAY((2, BOY16, "upper right", "HAVE YOU BEEN HERE BEFORE?"),
        (3, KAR, "upper right", "NO."),
        (3, KAR, "upper left", "OROCHIMARU KEPT ME MOVING BETWEEN BASES."),
        (4, BOY16, "upper right", "MY MOTHER WAS MOCKED FOR HER RED HAIR WHEN SHE ARRIVED HERE."),
        (5, OFF(BOY16), "upper right", "I DO NOT EXPECT THAT TO HAPPEN TO YOU."),
        (5, KAR, "upper left", "THAT IS SUPPOSED TO REASSURE ME?"),
        (6, BOY16, "upper right", "IT WAS INFORMATION."),
        (6, KAR, "upper left", "YOU ARE BAD AT REASSURANCE."))
  + "THE TWO PAIRED TIERS ARE THE WHOLE TEST OF THIS PAGE. In tier 2, PANEL 2 (the profile "
    "two-shot) is the RIGHT-hand rectangle and PANEL 3 (close on the red-haired girl) is the LEFT "
    "one, so his question \"HAVE YOU BEEN HERE BEFORE?\" is read BEFORE her answer \"NO.\" / "
    "\"OROCHIMARU KEPT ME MOVING BETWEEN BASES.\" In tier 3, PANEL 4 (close on the blond teen) is "
    "the RIGHT-hand rectangle and PANEL 5 (the girl alone) is the LEFT one, so \"MY MOTHER WAS "
    "MOCKED FOR HER RED HAIR WHEN SHE ARRIVED HERE.\" is read BEFORE \"I DO NOT EXPECT THAT TO "
    "HAPPEN TO YOU.\" / \"THAT IS SUPPOSED TO REASSURE ME?\" Never place PANEL 3 to the right of "
    "PANEL 2, and never place PANEL 5 to the right of PANEL 4. ",
  R("naruto_v4_armor_sword", "karin", "env_konoha_outskirts"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR) + ARMED + PALE +
  "SIX panels. What he is protecting meets what she refuses to give up.\n"
  "PANEL 1 (medium walking two-shot, upper right): the two of them level again, moving "
  "right-to-left along the road.\n"
  "PANEL 2 (close on the red-haired girl, upper left): she pushes her glasses up with one finger, "
  "looking forward.\n"
  "PANEL 3 (inset close-up, middle right): her fingers pull her sleeve down over the edge of OLD, "
  "FAINT, HEALED bite scars on her forearm — no wound, no blood, no fresh mark. Only her hand and "
  "sleeve are in the crop; her face and mouth are outside it. The blond teen is off-panel right "
  "and is not drawn at all.\n"
  "PANEL 4 (medium on the blond teen, middle left): he turns his face toward her but keeps "
  "walking; his body stays aimed at the village.\n"
  "PANEL 5 (tight reaction on the red-haired girl, lower right): her mouth hardens, her eye-line "
  "cutting left toward him.\n"
  "PANEL 6 (dominant bottom-left panel, the focal panel): she has STOPPED at page-right. He has "
  "taken one more step left and then turned fully back. The space between them is clear and "
  "neither touches the other; their eye-line crosses the panel. " + L_ROAD
  + "In PANEL 3 the girl's balloon tail runs down-right toward her mouth just outside the crop "
    "and must not touch her hand or sleeve. "
  + SAY((1, BOY16, "upper right", "YOU KNOW MEDICAL NINJUTSU."),
        (2, KAR, "upper right", "ENOUGH TO KNOW I AM NOT A MEDIC."),
        (3, OFF(BOY16), "upper right", "AND YOUR HEALING?"),
        (3, KAR, "upper left", "YOU KNOW HOW IT WORKS."),
        (4, BOY16, "upper right", "NO ONE HERE LEARNS IT FROM YOU."),
        (5, KAR, "upper right", "YOU KEEP TELLING ME WHAT MY LIFE WILL BE."),
        (6, BOY16, "upper right", "THEN TELL ME."),
        (6, BOY16, "upper left", "WHAT DO YOU WANT FIRST?"))
  + "SIX SEPARATE PANELS IN THREE HORIZONTAL TIERS, NONE OF THEM TALL. Tier 1 is PANEL 1 RIGHT "
    "and PANEL 2 LEFT; tier 2 is PANEL 3 RIGHT and PANEL 4 LEFT; tier 3 is PANEL 5 RIGHT and "
    "PANEL 6 LEFT. PANEL 4 is an ordinary rectangle confined to tier 2 and NEVER a tall panel "
    "running down the page beside a stacked right-hand column, so \"NO ONE HERE LEARNS IT FROM "
    "YOU.\" is read BEFORE \"YOU KEEP TELLING ME WHAT MY LIFE WILL BE.\" "
    "The balloon \"YOU KNOW HOW IT WORKS.\" belongs INSIDE PANEL 3, the sleeve-and-scar inset, at "
    "its upper left; it is the red-haired girl's, its tail runs down-right toward her mouth just "
    "outside the crop, and it must never be lettered inside PANEL 4, which holds the blond teen "
    "alone and in which she does not speak. "
    "BOTH balloons in PANEL 6 are the blond teen's: he stands at the reader-LEFT, she has stopped "
    "at the reader-RIGHT, and each of his tails travels across the gap to HIS mouth. Neither tail "
    "may stop at, touch or aim at the red-haired girl, however much closer to her the balloon "
    "sits. She says nothing in PANEL 6. ",
  R("naruto_v4_armor_sword", "karin", "env_konoha_outskirts"), "low"),

 # ---- Spread 3: under protection ---------------------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR, GUARD_DESC) + ARMED + PALE +
  "SIX panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 on the reader-right "
  "two-thirds and PANEL 2 on the reader-left third. Tier 2 is PANEL 3 reader-right and PANEL 4 "
  "reader-left in equal rectangles. Tier 3 is PANEL 5 full width and thin. Tier 4 is PANEL 6 full "
  "width and the tallest.\n"
  "PANEL 1 (top tier, reader-right wide rectangle): the red-haired girl stands at the right, the "
  "blond teen at the left, the gate distant behind him. She looks directly at him.\n"
  "PANEL 2 (top tier, reader-left narrow rectangle): close on the blond teen; his face stays "
  "controlled and his gaze holds hers.\n"
  "PANEL 3 (second tier, reader-right): she resumes walking left on her own, passing level with "
  "him.\n"
  "PANEL 4 (second tier, reader-left): he falls into step beside her, leaving a deliberate arm's "
  "length of clear space between them.\n"
  "PANEL 5 (full-width third-tier close-up band): her eye stays forward; the corner of her mouth "
  "lifts without any warmth in it.\n"
  "PANEL 6 (full-width bottom, the focal panel): the great gate fills the panel. The guard in the "
  "green flak vest stands at the LEFT and thrusts one flat palm out; the blond teen and the "
  "red-haired girl enter from the RIGHT and stop together. " + L_ROAD
  + SAY((1, KAR, "upper right", "A DOOR I CAN CLOSE."),
        (2, BOY16, "upper right", "YOU WILL HAVE ONE."),
        (3, KAR, "upper right", "AND I CHOOSE WHAT I DO BEHIND IT."),
        (4, BOY16, "upper right", "UNLESS IT EXPOSES YOU."),
        (5, KAR, "upper right", "THAT IS A LIMIT."),
        (5, KAR, "upper left", "NOT A LIFE."),
        (6, GUARD, "upper right", "HALT!")),
  R("naruto_v4_armor_sword", "karin", "env_konoha_outskirts"), "low"),

 ("p06", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR, GUARD_DESC) + ARMED + PALE +
  "SIX panels. Protection demonstrated without making her passive.\n"
  "PANEL 1 (medium gate triangle, upper right): the guard in the foreground at left faces the "
  "blond teen at centre-right; the red-haired girl stands behind his shoulder line but stays "
  "clearly visible at the far right. The guard squints, then recognises him.\n"
  "PANEL 2 (close on the guard, upper left): his attention shifts PAST the blond teen toward the "
  "girl.\n"
  "PANEL 3 (two-shot, middle right): she opens her mouth to answer. The blond teen extends one "
  "forearm across the GUARD'S EYE-LINE — never across her body, never touching her — and answers "
  "first. Her eyes move to him.\n"
  "PANEL 4 (close on the guard, middle left): his confidence returns as he points toward the "
  "checkpoint desk away at page-left.\n"
  "PANEL 5 (narrow reaction band): the red-haired girl's hand tightens once at her side. Her feet "
  "stay planted; she does not retreat. NO TEXT IN THIS PANEL.\n"
  "PANEL 6 (dominant bottom panel, the focal panel): the blond teen steps LEFT into the guard's "
  "path, shoulders square. She steps left at the same moment and stops BESIDE him, not behind "
  "him. The guard yields a half-step toward the far left. The blond teen looks only at the guard; "
  "she watches the blond teen. " + L_ROAD
  + SAY((1, GUARD, "upper right", "UCHIHA NARUTO...?"),
        (2, GUARD, "upper right", "HER TRAVEL PASS."),
        (3, BOY16, "upper right", "SHE DOES NOT HAVE ONE."),
        (4, GUARD, "upper right", "THEN SHE WAITS HERE."),
        (6, BOY16, "upper right", "SHE IS UNDER MY PROTECTION."),
        (6, BOY16, "upper centre-left", "LOG HER AS MY GUEST."),
        (6, GUARD, "upper left", "Y-YES."))
  + "PANEL 6 TAIL ATTRIBUTION, THE POINT OF THE PAGE: \"SHE IS UNDER MY PROTECTION.\" and \"LOG "
    "HER AS MY GUEST.\" are BOTH spoken by the blond teen, and BOTH of their tails must travel "
    "all the way to HIS mouth, however near the red-haired girl standing beside him they happen "
    "to sit. Neither tail may touch, graze or terminate on her head, her hair or her shoulder — "
    "she does not speak anywhere on this page, and a tail landing on her would make her claim "
    "protection over herself. \"Y-YES.\" is the guard's and tails to the guard at the far left. ",
  R("naruto_v4_armor_sword", "karin", "env_konoha_outskirts"), "low"),

 # ---- Spread 4: leave their sight --------------------------------------------------
 ("p07", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + MOB.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, KAR,
         "unnamed Konoha civilians and off-duty shinobi pausing along both sides of the street, "
         "none of them named or recurring", WATCHERS) + ARMED + PALE +
  "FIVE panels. Her value, his secrecy, and consent — in that order.\n"
  "PANEL 1 (wide street panel, full-width upper tier): the two of them move RIGHT-TO-LEFT through "
  "the shinobi district. Villagers pause on both sides to look at his red armour. THREE TINY "
  "MASKED SILHOUETTES stand on three SEPARATE far rooftops in the deep background, each far too "
  "small to identify.\n"
  "PANEL 2 (close on the blond teen, middle right): his eye shifts toward ONE roof without his "
  "head turning at all.\n"
  "PANEL 3 (close on the red-haired girl, middle left): she glances toward a DIFFERENT roof, then "
  "back to him. The blond teen is off-panel left and is not drawn.\n"
  "PANEL 4 (medium two-shot, lower right): he stops at the left and extends an open gloved hand "
  "BACK toward her at the right. He does NOT touch her. The nearest masked rooftop silhouette "
  "leans forward above.\n"
  "PANEL 5 (dominant lower-left panel, the focal panel): close on HER BARE HAND closing around "
  "HIS OFFERED WRIST — not his hand. Her grip is the sharp centre of the panel; both bodies are "
  "already breaking apart LEFTWARD into flat opaque orange-red flame shapes with hard black "
  "outlines. Her face and mouth are outside the crop. " + L_STREET
  + "In PANEL 5 the girl's balloon tail runs down-left toward her mouth just outside the crop and "
    "must not cross the gripping hands. "
  + SFX(5, "FWSSSH", "Flowing leftward along the flame shapes and cropped by the panel edge.")
  + SAY((1, KAR, "upper right", "THREE ANBU SQUADS."),
        (2, BOY16, "upper right", "I SENSED ONE."),
        (3, KAR, "upper right", "ARE YOU GOING TO TELL THEM WHAT I CAN DO?"),
        (3, OFF(BOY16), "upper left", "NO."),
        (4, BOY16, "upper right", "WE CAN WALK UNDER THEIR EYES."),
        (4, BOY16, "upper left", "OR LEAVE."),
        (5, KAR, "upper right", "LEAVE.")),
  R("naruto_v4_armor_sword", "karin", "mob_archetypes", "env_village_street"), "medium"),

 ("p08", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR) + ARMED + PALE +
  "SIX panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width. Tier 2 is "
  "PANEL 2 on the reader-right third and PANEL 3 on the reader-left two-thirds. Tier 3 is PANEL 4 "
  "reader-right and PANEL 5 reader-left in equal rectangles. Tier 4 is PANEL 6 full width and the "
  "tallest.\n"
  "PANEL 1 (full-width top rectangle): flat opaque orange-red flame clears from RIGHT to LEFT "
  "inside a small unused sitting room. The blond teen appears near the right wall; the red-haired "
  "girl releases his wrist and steps left to inspect the room. Dust and dust-sheeted furniture "
  "read as ABSENCE, not ruin — nothing is broken.\n"
  "PANEL 2 (second tier, reader-right narrow rectangle): he stays exactly where he materialised, "
  "giving her the room.\n"
  "PANEL 3 (second tier, reader-left wide rectangle, from HER point of view): an empty kitchen "
  "doorway at the left, the hall at the centre, the locked front door at the right. Thin, faintly "
  "visible sealing arrays trace the door and window frames as fine geometric line-work with NO "
  "readable characters of any kind — ILLEGIBLE SCRIBBLE, not readable words. The blond teen is a "
  "small figure at the FAR RIGHT EDGE.\n"
  "PANEL 4 (third tier, reader-right): close on her as she looks back over her shoulder toward "
  "him.\n"
  "PANEL 5 (third tier, reader-left): his body angles toward the exit while his eyes stay on her.\n"
  "PANEL 6 (full-width bottom, the focal panel): she stands INSIDE the room at page-right; he "
  "stands at the THRESHOLD at page-left. The full doorframe separates them and stays open. "
  + L_HOUSE
  + "In PANEL 3 the balloon sits at the upper centre-left and its tail is a long one running "
    "down-right to the small figure of the blond teen at the far right edge, clear of every other "
    "shape. "
  + SFX(1, "FSSS", "Small and fading at the upper right where the last flame thins out.")
  + SAY((2, BOY16, "upper right", "THIS WAS MY HOUSE."),
        (3, BOY16, "upper centre-left", "IT IS YOURS NOW."),
        (4, KAR, "upper right", "YOU ARE NOT STAYING?"),
        (5, BOY16, "upper right", "I WILL LIVE IN THE UCHIHA COMPOUND."),
        (6, KAR, "upper right", "WHY GIVE ME THIS?"),
        (6, BOY16, "upper left", "BECAUSE YOU ARE NOT COMFORTABLE WITH ME.")),
  R("naruto_v4_armor_sword", "karin", "env_apartment_int"), "low"),

 # ---- Spread 5: two houses ---------------------------------------------------------
 ("p09", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + KARIN.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, KAR) + ARMED + PALE +
  "SEVEN panels. The key changes hands without a hand in the frame.\n"
  "PANEL 1 (close on the red-haired girl, upper right): surprise breaks her guarded expression; "
  "her eyes stay on him.\n"
  "PANEL 2 (close on the blond teen, upper left): flat, direct eye contact straight across the "
  "gutter.\n"
  "PANEL 3 (inset, middle right): his gloved hand sets a single key down on the table between "
  "them and withdraws. The key POINTS LEFT toward her. Only hands and table are in the crop; his "
  "face and mouth are outside it.\n"
  "PANEL 4 (medium on the red-haired girl, middle left): she does not pick the key up yet.\n"
  "PANEL 5 (narrow reaction band on the blond teen): no offence and no amusement — level.\n"
  "PANEL 6 (close on hands, lower right, the focal panel): SHE takes the key herself. HIS HANDS "
  "ARE ENTIRELY OUTSIDE THIS PANEL. Her face and mouth are outside the crop.\n"
  "PANEL 7 (wide, lower left): he exits LEFT through the front door with the gunbai on his back "
  "and the sash sword still sheathed at his hip. She stays inside at page-right with the key "
  "closed in her fist and does not follow. " + L_HOUSE
  + "In PANELS 3, 6 and 7 every tail runs to its speaker's mouth or, where the mouth is outside "
    "the crop, toward the panel edge nearest that mouth, and must never cross a hand or the key. "
  + SAY((1, KAR, "upper right", "YOU NOTICED."),
        (2, BOY16, "upper right", "YES."),
        (3, BOY16, "upper right", "THIS ROOM IS YOURS."),
        (3, BOY16, "upper left", "I WILL LEAVE YOU TO SETTLE IN."),
        (4, KAR, "upper right", "YOU ARE TRUSTING ME WITH YOUR HOUSE."),
        (5, BOY16, "upper right", "I AM GIVING IT TO YOU."),
        (6, KAR, "upper right", "THEN I ACCEPT. THANK YOU."),
        (7, BOY16, "upper right", "STAY HERE UNTIL I RETURN."),
        (7, KAR, "upper centre", "WHERE ARE YOU GOING?"),
        (7, BOY16, "upper left", "TO SASUKE."))
  + "SEVEN SEPARATE PANELS IN FOUR HORIZONTAL TIERS, NONE OF THEM TALL. Tier 1 is PANEL 1 RIGHT "
    "and PANEL 2 LEFT; tier 2 is PANEL 3 RIGHT and PANEL 4 LEFT; tier 3 is PANEL 5 full width; "
    "tier 4 is PANEL 6 RIGHT and PANEL 7 LEFT. PANEL 4 is an ordinary rectangle confined to tier "
    "2 and NEVER a tall panel running down beside a stacked right-hand column of three. The "
    "resulting order is fixed: \"YOU ARE TRUSTING ME WITH YOUR HOUSE.\" is read BEFORE \"I AM "
    "GIVING IT TO YOU.\", which is read before \"THEN I ACCEPT. THANK YOU.\" ",
  R("naruto_v4_armor_sword", "karin", "env_apartment_int"), "low"),

 ("p10", dict(scene="establishing", light="overcast", cast="solo", mood="somber", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + GUNBAI_V4.format(i=2) + SASUKE16.format(i=3)
  + KAK.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16,
         "the older dark-haired teen and the masked silver-haired man appearing ONLY as two tiny "
         "distant sparring figures far below in panel 5, too small and too far away for any face "
         "to be legible, and nowhere else on the page") + ARMED + PALE +
  "FIVE panels. ENTIRELY WITHOUT SPEECH — no balloons of any kind, only one location card and two "
  "small sound effects. The empty compound is the subject.\n"
  "PANEL 1 (wide establishing panel, full-width upper tier): the walled compound gate dominates "
  "the RIGHT; its empty main street recedes away to the LEFT. The blond teen enters from the far "
  "right and moves left ALONE, gunbai on his back and the sash sword sheathed at his hip. The "
  "location card sits at the upper right on blank wall. No figure but him.\n"
  "PANEL 2 (tall silent panel, middle right): he walks down the centre of the deserted street. "
  "Closed doors and one unused child's ball sit at the edges. NO ghost figures, NO transparent "
  "silhouettes, NO memory insets. His eye-line stays on the former clan-head house at the far "
  "left.\n"
  "PANEL 3 (medium exterior, middle left): he slides that house's door open from right to left "
  "and crosses the threshold with BOTH the gunbai and the sheathed sword still on him.\n"
  "PANEL 4 (small interior, lower right, the focal panel): in an upstairs room he unstraps the "
  "gunbai, unbuckles the still-sheathed plain sword, and rests BOTH securely side by side against "
  "the LEFT wall — the first objects he places in the room. The sword stays sheathed and is "
  "plainly a different, undecorated blade.\n"
  "PANEL 5 (wide, lower left): with the war fan and the sheathed sword standing in the room "
  "BEHIND him, he pauses UNARMED at the open window on the right — nothing on his back, nothing "
  "at his hips. Far below and to the left, two tiny distant figures collide on the compound "
  "training ground, too small for any face. His head turns toward the sound. " + L_COMP
  + CAP(1, "upper right on blank wall", "UCHIHA COMPOUND.")
  + SFX(4, "THNK", "Small, beside the gunbai base and the sword scabbard where they touch the floor.")
  + SFX(5, "KLAK", "Small and distant, out over the training ground far below and left.")
  + "Do not write any other text anywhere on the page — no speech balloons, no thought balloons, "
    "no signature. ",
  R("naruto_v4_armor_sword", "gunbai_v4", "sasuke_16", "kakashi", "env_uchiha_compound"), "high"),

 # ---- Spread 6: the return seen ----------------------------------------------------
 ("p11", dict(scene="action", light="overcast", cast="small_group", mood="tense", panels=6),
  FILL + RTL + SASUKE16.format(i=1) + KAK.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(SAS16, KAKA, BOY16) + UNARMED + PALE +
  "SIX panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width. Tier 2 is "
  "PANEL 2 on the reader-right third and PANEL 3 on the reader-left two-thirds. Tier 3 is PANEL 4 "
  "on the reader-right third and PANEL 5 on the reader-left two-thirds. Tier 4 is PANEL 6 full "
  "width.\n"
  "PANEL 1 (full-width top rectangle): establish the compound training ground. The older "
  "dark-haired teen starts at page-RIGHT, the masked silver-haired man at page-LEFT, twelve "
  "metres apart; the clan-head house and the approach path sit in the centre background. BOTH "
  "have ACTIVE SHARINGAN — blood-red irises with three black comma marks, the masked man's in his "
  "single uncovered eye. They drive toward each other, right-to-left and left-to-right.\n"
  "PANEL 2 (second tier, reader-right narrow): the dark-haired teen's three tomoe track the "
  "masked man's lead shoulder. NO TEXT IN THIS PANEL.\n"
  "PANEL 3 (second tier, reader-left wide): the dark-haired teen cuts left across the masked "
  "man's guard; the masked man pivots clockwise and catches the strike on a kunai. Their bodies "
  "form an arrow pointing page-LEFT.\n"
  "PANEL 4 (third tier, reader-right narrow): the masked man's visible Sharingan tracks the "
  "dark-haired teen's recovery while his feet retreat one step — slower, but already placed for "
  "the next counter. NO TEXT IN THIS PANEL.\n"
  "PANEL 5 (third tier, reader-left wide): the blond teen stands just inside the training-ground "
  "fence at page-RIGHT, still and UNARMED — no war fan, no sword. The other two are in the far "
  "left background mid-turn; both eye-lines snap toward him.\n"
  "PANEL 6 (full-width bottom, the focal panel): the dark-haired teen in the foreground right and "
  "the masked silver-haired man in the foreground left have fully stopped and lowered their "
  "guards. The red irises and three tomoe VISIBLY FADE — the dark-haired teen's two eyes and the "
  "masked man's uncovered eye are ORDINARY DARK EYES here, before either approaches. The blond "
  "teen walks between their converging eye-lines from the background, moving toward page-left. "
  + L_COMP
  + SFX(3, "KLAK", "Between the crossed weapons, angled leftward.")
  + SAY((6, BOY16, "upper right", "YOU HAVE BOTH IMPROVED.")),
  R("sasuke_16", "kakashi", "naruto_v4_armor", "env_uchiha_compound"), "medium"),

 ("p12", dict(scene="dialogue", light="overcast", cast="small_group", mood="calm", panels=7),
  FILL + RTL + SASUKE16.format(i=1) + KAK.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(SAS16, KAKA, BOY16) + UNARMED + PALE +
  "SEVEN panels. Every Sharingan is OFF from here on: the dark-haired teen's eyes and the masked "
  "man's uncovered eye are ordinary dark eyes in every panel of this page.\n"
  "PANEL 1 (medium on the masked silver-haired man, upper right): he approaches from the left, "
  "tired but smiling with his now ordinary visible eye. The blond teen stands opposite at "
  "page-right.\n"
  "PANEL 2 (close on the blond teen, upper left): his eye-line rests on the masked man, not on "
  "the smile. The masked man is NOT drawn in this panel.\n"
  "PANEL 3 (three-shot, middle right): the blond teen at the centre looks from the masked man on "
  "the left to the dark-haired teen on the right. The dark-haired teen's eyes stay ordinary; he "
  "folds his arms but leans into the exchange.\n"
  "PANEL 4 (close on the dark-haired teen, middle centre): his old irritation surfaces; his gaze "
  "cuts left toward the blond teen.\n"
  "PANEL 5 (close on the blond teen, middle left, the focal panel): a small smile, held inside "
  "the dark-haired teen's eye-line.\n"
  "PANEL 6 (two-shot, lower right): the dark-haired teen steps one pace toward the blond teen; "
  "the blond teen does not yield the space. The masked man stands between them in the background "
  "with an eye-smile.\n"
  "PANEL 7 (wide, lower left): the masked man's expression turns serious as he moves toward the "
  "exit at page-left. The blond teen gives one silent shrug at the centre; the dark-haired teen "
  "watches from page-right. " + L_COMP
  + SAY((1, KAKA, "upper right", "NARUTO. GOOD TO SEE YOU BACK IN ONE PIECE."),
        (2, OFF(KAKA), "upper right", "WHEN DID YOU RETURN?"),
        (2, BOY16, "upper left", "A FEW MINUTES AGO."),
        (3, BOY16, "upper right", "EVEN YOU CHANGED, KAKASHI."),
        (4, SAS16, "upper right", "EVEN HIM?"),
        (5, BOY16, "upper right", "IF YOU COULD CHANGE, ANYTHING IS POSSIBLE."),
        (6, SAS16, "upper right", "WHAT IS THAT SUPPOSED TO MEAN?"),
        (6, KAKA, "upper left", "OLD HABITS."),
        (7, KAKA, "upper right", "NARUTO—CAN WE TALK TOMORROW?"),
        (7, KAKA, "lower left", "SEE YOU TOMORROW, SASUKE."))
  + "The PANEL 1 balloon reads exactly \"NARUTO. GOOD TO SEE YOU BACK IN ONE PIECE.\" — BACK is "
    "spelled B-A-C-K, four letters with a single A. Never write BAACK or any other doubled-vowel "
    "form of it. "
  + "SEVEN SEPARATE PANELS IN FOUR HORIZONTAL TIERS, NONE OF THEM TALL. Tier 1 is PANEL 1 RIGHT "
    "and PANEL 2 LEFT; tier 2 is PANEL 3 RIGHT, PANEL 4 CENTRE and PANEL 5 LEFT; tier 3 is PANEL "
    "6 RIGHT; tier 4 is PANEL 7. PANEL 5 is an ordinary rectangle confined to tier 2 and NEVER a "
    "tall panel running down the page beside a stacked right-hand column, so \"IF YOU COULD "
    "CHANGE, ANYTHING IS POSSIBLE.\" is read BEFORE \"WHAT IS THAT SUPPOSED TO MEAN?\" ",
  R("sasuke_16", "kakashi", "naruto_v4_armor", "env_uchiha_compound"), "low"),

 # ---- Spread 7: what belonged to him -----------------------------------------------
 ("p13", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + UNARMED + PALE +
  "SIX panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width and tall. "
  "Tier 2 is PANEL 2 on the reader-right third and PANEL 3 on the reader-left two-thirds. Tier 3 "
  "is PANEL 4 reader-right and PANEL 5 reader-left in equal rectangles. Tier 4 is PANEL 6 full "
  "width.\n"
  "PANEL 1 (full-width top rectangle): later, in the house garden. The blond teen sits on the "
  "veranda at page-LEFT facing the empty garden. The older dark-haired teen enters from "
  "page-RIGHT with damp hair after washing and sits an arm's length away; both face left. His "
  "eyes are ordinary dark eyes.\n"
  "PANEL 2 (second tier, reader-right narrow): the blond teen does not look away from the "
  "garden.\n"
  "PANEL 3 (second tier, reader-left wide): the dark-haired teen angles his shoulders toward the "
  "blond teen, who stays facing forward.\n"
  "PANEL 4 (third tier, reader-right): close on the blond teen; the answer is immediate.\n"
  "PANEL 5 (third tier, reader-left): the dark-haired teen's brow tightens; his eye-line moves "
  "over the red armour as if checking it for damage.\n"
  "PANEL 6 (full-width bottom, the focal panel): the blond teen finally turns his head toward the "
  "dark-haired teen. The empty garden fills the space behind them both. " + L_GARDEN
  + SAY((1, SAS16, "upper right", "I DID NOT EXPECT YOU BACK SO SOON."),
        (2, BOY16, "upper right", "THE WORK ENDED EARLIER THAN I EXPECTED."),
        (3, SAS16, "upper right", "WHERE DID YOU GO AFTER KIRI?"),
        (4, BOY16, "upper right", "EARTH COUNTRY."),
        (5, SAS16, "upper right", "IWA WOULD KILL A LEAF SHINOBI THEY FOUND THERE."),
        (6, BOY16, "upper right", "THEY WOULD HAVE TRIED."))
  + "PANEL 6 HOLDS ONE BALLOON AND IT IS THE BLOND TEEN'S. Its tail must reach HIS mouth as he "
    "turns his head, and must not touch, cross or terminate on the older dark-haired teen's head, "
    "hair or the back of his skull, even though he sits nearer the balloon. The dark-haired teen "
    "does not speak in PANEL 6 — he has just warned that Iwa would kill a Leaf shinobi, and this "
    "is the answer to him. ",
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "low"),

 ("p14", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + UNARMED + PALE +
  "SEVEN panels, same veranda and garden. One answer given, one question withdrawn.\n"
  "PANEL 1 (medium on the dark-haired teen, upper right): he now sits fully turned toward the "
  "blond teen.\n"
  "PANEL 2 (close on the blond teen, upper left): his face is impassive; the dark-haired teen's "
  "dark shoulder anchors the right edge.\n"
  "PANEL 3 (narrow reaction on the dark-haired teen, middle right): his eyes sharpen, but he does "
  "not rise.\n"
  "PANEL 4 (narrow reaction on the blond teen, middle left): stillness arrives before the word "
  "does.\n"
  "PANEL 5 (two-shot, lower right): the dark-haired teen looks directly at him; the blond teen "
  "has turned back to the garden.\n"
  "PANEL 6 (silent close-up, lower centre, the focal panel): the dark-haired teen's mouth closes "
  "on the next question. His eye-line drops from the blond teen's face to the blond teen's EMPTY "
  "HANDS. NO TEXT IN THIS PANEL.\n"
  "PANEL 7 (wide, lower left): the dark-haired teen leans back, choosing not to press, and in the "
  "same motion studies the blond teen's pale profile. The blond teen stays upright. " + L_GARDEN
  + SAY((1, SAS16, "upper right", "WHO WAS THE TARGET?"),
        (2, BOY16, "upper right", "OROCHIMARU."),
        (3, SAS16, "upper right", "DID YOU GET HIM?"),
        (4, BOY16, "upper right", "YES."),
        (5, SAS16, "upper right", "WHY HIM?"),
        (5, BOY16, "upper left", "HE HAD SOMETHING THAT BELONGED TO ME."),
        (7, SAS16, "upper right", "YOU LOOK PALE."),
        (7, BOY16, "upper left", "I AM FINE.")),
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "low"),

 # ---- Spread 8: the restored library -----------------------------------------------
 ("p15", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + UNARMED + PALE +
  "SEVEN panels. Weakness converted into political urgency.\n"
  "PANEL 1 (close on the blond teen, upper right): his gaze shifts back to the dark-haired teen.\n"
  "PANEL 2 (close on the dark-haired teen, upper left): one measured nod.\n"
  "PANEL 3 (medium two-shot, middle right): the blond teen rises at page-left; the dark-haired "
  "teen stays seated at page-right and looks up.\n"
  "PANEL 4 (medium on the dark-haired teen, middle left): he rises more slowly, still watching "
  "the blond teen's pallor.\n"
  "PANEL 5 (walking two-shot, lower right, the focal panel): the blond teen leads LEFT toward the "
  "house; the dark-haired teen follows one step behind, the concern replaced by focus.\n"
  "PANEL 6 (close on the dark-haired teen, lower centre): his eye moves to the compound walls.\n"
  "PANEL 7 (wide, lower left): both enter the shadowed house, the blond teen at the left and the "
  "dark-haired teen at the right. Empty compound streets stay visible through the open door "
  "behind them. " + L_GARDEN
  + SAY((1, BOY16, "upper right", "ARE YOU SATISFIED?"),
        (2, SAS16, "upper right", "FOR NOW."),
        (3, BOY16, "upper right", "THEN WE DISCUSS THE CLAN."),
        (4, SAS16, "upper right", "YOU SHOULD REST."),
        (5, BOY16, "upper right", "ONE OF US MUST TAKE THE UCHIHA SEAT AT THE NEXT COUNCIL."),
        (6, SAS16, "upper right", "IS IT SAFE TO SPEAK HERE?"),
        (7, BOY16, "upper right", "NO ONE ELSE IS INSIDE THE COMPOUND."),
        (7, BOY16, "upper left", "THE ANBU WILL FIND ME SOON.")),
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "low"),

 ("p16", dict(scene="establishing", light="day", cast="two", mood="tense", panels=7),
  FILL + RTL + SASUKE16.format(i=1) + N16_ARMOR.format(i=2) + ENV.format(i=3)
  + ONLY(SAS16, BOY16) + UNARMED + PALE +
  "SEVEN panels in four non-overlapping horizontal tiers. Tier 1 is PANEL 1 full width and tall. "
  "Tier 2 is PANEL 2 on the reader-right third and PANEL 3 on the reader-left two-thirds. Tier 3 "
  "divides into PANEL 4 reader-right, PANEL 5 centre and PANEL 6 reader-left in three equal "
  "rectangles. Tier 4 is PANEL 7 full width.\n"
  "This is the clan's restored library inside the compound house: a shelved archive room of "
  "ordered scroll racks, paper screens and dark timber. Take the compound's architecture, "
  "materials and palette from the location plate and build the shelving from them.\n"
  "PANEL 1 (full-width top rectangle): the older dark-haired teen slides the library door open "
  "from right to left. Ordered shelves of scrolls fill the room. The blond teen stands behind him "
  "at page-right, looking PAST him into the room rather than at him.\n"
  "PANEL 2 (second tier, reader-right narrow): the blond teen crosses the threshold toward the "
  "shelves.\n"
  "PANEL 3 (second tier, reader-left wide): the dark-haired teen walks along the RIGHT shelf; the "
  "blond teen mirrors him along the LEFT, their paths converging toward the back of the room.\n"
  "PANEL 4 (third tier, reader-right): the blond teen's glove hovers over a scroll rack without "
  "taking anything; his mouth is outside the crop.\n"
  "PANEL 5 (third tier, centre): the dark-haired teen looks across the aisle toward him.\n"
  "PANEL 6 (third tier, reader-left): the blond teen's eye-line shifts from the scrolls to the "
  "dark-haired teen.\n"
  "PANEL 7 (full-width bottom, the focal panel): the dark-haired teen stands framed between two "
  "full shelves; the blond teen's gloved hand rests on the end of one scroll in the foreground "
  "right. The dark-haired teen answers toward him. All writing on every scroll, label and spine "
  "anywhere on this page is ILLEGIBLE SCRIBBLE, not readable words. " + L_LIB
  + SAY((1, SAS16, "upper right", "THEY RETURNED THE CLAN PROPERTY."),
        (2, BOY16, "upper right", "THE LIBRARY?"),
        (3, SAS16, "upper right", "RESTORED."),
        (3, SAS16, "upper left", "I HAD GENIN PUT EVERYTHING BACK IN ORDER."),
        (4, BOY16, "upper right", "WE NEED A BARRIER."),
        (5, SAS16, "upper right", "AGREED."),
        (6, BOY16, "upper right", "HOW LONG DID THEY TAKE TO RETURN THEM?"),
        (7, SAS16, "upper right", "A WEEK.")),
  R("sasuke_16", "naruto_v4_armor", "env_uchiha_compound"), "medium"),

 # ---- Spread 9: what was copied ----------------------------------------------------
 ("p17", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + UNARMED + PALE + MACRON +
  "SEVEN panels in four non-overlapping horizontal tiers, still inside the restored library. Tier "
  "1 is PANEL 1 reader-right and PANEL 2 reader-left in equal rectangles. Tier 2 is PANEL 3 on "
  "the reader-right two-thirds and PANEL 4 on the reader-left third. Tier 3 is PANEL 5 full "
  "width. Tier 4 is PANEL 6 on the reader-right third and PANEL 7 on the reader-left two-thirds. "
  "EXACTLY ELEVEN BALLOONS on this page and no more; no balloon crosses a face, an object, a "
  "panel border or another balloon.\n"
  "PANEL 1 (close on the blond teen, upper right): his fingers close around a scroll but do not "
  "draw it out.\n"
  "PANEL 2 (close on the dark-haired teen, upper left): his eyes narrow; he looks past the blond "
  "teen toward the door as if re-checking the room's safety.\n"
  "PANEL 3 (two-shot across the aisle, middle right): scroll shelves separate the blond teen on "
  "the LEFT from the dark-haired teen on the RIGHT.\n"
  "PANEL 4 (medium on the dark-haired teen, middle left): he turns fully back to the blond teen.\n"
  "PANEL 5 (single full-width object panel, NO people at all): ONE continuous shelf composition "
  "carrying, from reader-right to reader-left, a bound clan historical record, a folded diagram "
  "of eye-pattern maturation, and a sealed technique scroll. There are NO internal borders and NO "
  "inset rectangles inside this panel. ALL interior writing on every object is ILLEGIBLE "
  "SCRIBBLE, not readable words. The blond teen is established off-panel to the reader-LEFT and "
  "is not drawn.\n"
  "PANEL 6 (fourth tier, reader-right): close on the dark-haired teen; recognition turns into "
  "alarm.\n"
  "PANEL 7 (fourth tier, reader-left wide, the focal panel): the blond teen and the dark-haired "
  "teen face each other at opposite ends of the aisle; the returned scrolls tower between and "
  "behind them. " + L_LIB
  + SAY((1, BOY16, "upper right", "THE ADVISERS LIKELY COPIED THEM DURING THAT WEEK."),
        (2, SAS16, "upper right", "AND DANZŌ?"),
        (3, BOY16, "upper right", "DANZŌ HAD ALREADY COPIED SOME."),
        (3, BOY16, "upper left", "THE ADVISERS HELD THE ORIGINALS."),
        (4, SAS16, "upper right", "WHAT WAS WORTH COPYING?"),
        (5, OFF(BOY16), "upper right over the first object", "OUR DŌJUTSU."),
        (5, OFF(BOY16), "upper centre over the second object", "ITS HISTORY."),
        (5, OFF(BOY16), "upper left over the third object", "MANGEKYŌ TECHNIQUES."),
        (6, SAS16, "upper right", "I THOUGHT THAT WAS KEPT AT NAKA SHRINE."),
        (7, BOY16, "upper right", "THE SHRINE HOLDS THE WHOLE TRUTH."),
        (7, BOY16, "upper left", "THESE HOLD ENOUGH TO BE DANGEROUS."))
  + "THE NAME DANZŌ APPEARS TWICE ON THIS PAGE AND MUST BE LETTERED IDENTICALLY BOTH TIMES: "
    "D-A-N-Z-O with a single straight horizontal bar above the final O. The PANEL 2 balloon reads "
    "exactly \"AND DANZŌ?\" and the PANEL 3 balloon reads exactly \"DANZŌ HAD ALREADY COPIED "
    "SOME.\" Neither may carry two dots over the O and neither may carry a wavy tilde. The same "
    "single straight bar sits over the O of DŌJUTSU and of MANGEKYŌ in PANEL 5. ",
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "low"),

 ("p18", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16, LEAF_ANBU) + UNARMED + PALE +
  "SIX panels. LAST PAGE OF THE CHAPTER — it ends on a summons and a departure.\n"
  "PANEL 1 (medium on the blond teen, upper right): he turns back to the rack, one finger marking "
  "the scroll's place.\n"
  "PANEL 2 (medium on the dark-haired teen, upper left): he starts to answer, but the blond teen "
  "raises one hand between them and looks toward the open garden side of the library.\n"
  "PANEL 3 (thin silent panel, middle right): a masked shadow drops past the paper screen outside "
  "from upper right to lower left. The blond teen's raised fingers stay visible at the left edge. "
  "NO TEXT IN THIS PANEL.\n"
  "PANEL 4 (wide, middle left): a masked Leaf agent lands KNEELING just inside the garden "
  "threshold at page-right; the blond teen stands centre-left facing him; the dark-haired teen is "
  "behind the blond teen at the far left. The agent's arrival line drives the eye leftward "
  "across both of them.\n"
  "PANEL 5 (medium two-shot, lower right): the blond teen turns his back on the agent and looks "
  "to the dark-haired teen, who meets his eye. The agent is only a cropped shoulder at the far "
  "right.\n"
  "PANEL 6 (dominant lower-left panel, the focal panel): the agent rises and reaches one hand "
  "toward the blond teen from page-right. The blond teen's body is already dissolving LEFTWARD "
  "into flat opaque orange-red flame shapes with hard black outlines before the hand reaches him. "
  "The dark-haired teen stays beside the scroll shelves at page-left, watching him go. " + L_LIB
  + "In PANEL 6 the blond teen's balloon tail descends into the centre of the flame where his "
    "mouth was. All writing on every scroll and label is ILLEGIBLE SCRIBBLE, not readable words. "
  + SFX(4, "THP", "Small, beside the kneeling agent's leading foot.")
  + SFX(6, "FWSSSH", "Large, flowing off the page-left edge along the flame shapes.")
  + SAY((1, BOY16, "upper right", "THE ACTIVATION METHOD IS NOT HERE."),
        (2, SAS16, "upper right", "I DID NOT—"),
        (4, ANBU, "upper right", "UCHIHA NARUTO."),
        (4, ANBU, "upper left", "THE HOKAGE REQUESTS YOUR PRESENCE. NOW."),
        (5, BOY16, "upper right", "I WILL RETURN FOR YOU AFTER THE MEETING."),
        (6, ANBU, "upper right", "UCHI—"),
        (6, BOY16, "upper left", "I HEARD YOU.")),
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch09" / "raw", HERE / "v5ch09" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
