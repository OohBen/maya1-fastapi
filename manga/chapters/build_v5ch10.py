"""Volume 5, Chapter 10 — "Permission". 18 pages.

Source: fic ch15:203-399. Translated 1:1 from story/volume_05/drafts/ch10_permission.md —
122 spoken balloons, two movement SFX and one chapter marker. Reading order is RIGHT TO LEFT
per the approved `name`; every page states it.

The whole chapter plays inside one room: the Hokage office, bound from refs/images on every
page. Fixed geography — Tsunade reader-left behind the desk, Jiraiya reader-right at the
window, Naruto in the central foreground — is restated on every page so the staging cannot
drift.

MISSING REFERENCE SHEETS (reported, never invented): there is no Hanzo sheet and no young-Sannin
sheet in refs/images, so page 13's history panel is drawn as flat anonymous silhouettes exactly
as the `name` specifies, with no reference bound. Akatsuki's leader is deliberately an anonymous
rain-veiled silhouette and needs none.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import ENV, FILL, JIR, OFF, ONLY, R, SAY, SFX  # noqa: E402
from prompts_v4 import N16_ARMOR, TSUNADE, N16_SPEAKER, TSUNADE_SPEAKER  # noqa: E402

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
TSU = TSUNADE_SPEAKER
JIRA = "the big white-haired man with the two red facial stripes"

# Fixed staging, restated on every page so the three-way blocking cannot drift.
GEO = ("FIXED OFFICE GEOGRAPHY on every page of this chapter: the blonde woman in the green haori "
       "is READER-LEFT behind the broad desk, the big white-haired man is READER-RIGHT at the tall "
       "round window, and the blond teen stands in the CENTRAL FOREGROUND before the desk. A "
       "speaker's facing never reverses inside an exchange unless the panel describes the "
       "movement. ")
NOGUNBAI = ("OVERRIDE the reference sheet: the blond teen carries NO gunbai and NO weapon of any "
            "kind in this office — his back is empty and both hips are empty. ")
SHARINGAN = ("OVERRIDE the reference sheet's blue eye: his visible LEFT eye is an ORDINARY ACTIVE "
             "SHARINGAN — a blood-red iris with exactly THREE black comma marks around the pupil — "
             "in every panel. His right eye stays hidden behind the heavy right bang. NEVER draw "
             "the six-bladed Mangekyo pattern anywhere on this page. ")
PALE = ("A slight pallor shows in his face. He never coughs, never sways and never touches his own "
        "body, and nobody in the room remarks on it. ")
CALM = ("His expression changes only through narrowed attention and eye direction: no grin, no "
        "shout, no open mouth, no orange clothing at any point. ")
L_HOK = ("Lighting: clean flat late-morning daylight through the office's tall round window, the "
         "room evenly lit, paperwork bright, no dramatic shadow. ")

# Page-QA gate on ch10 p17 / ch09 p17: the macron in HANZŌ and DANZŌ came back as a tilde on one
# page and an umlaut on another, so one name was spelled two ways inside a single chapter. The
# macron is kept — p13's caption already letters it correctly — and is now described explicitly.
MACRON = ("MACRON RULE FOR THIS PAGE: wherever a capital O carries a macron — HANZŌ, DANZŌ — that "
          "mark is ONE SINGLE STRAIGHT HORIZONTAL BAR sitting directly above the letter, the full "
          "width of the O and no thicker than the lettering stroke. It is NEVER two dots, NEVER a "
          "wavy tilde, NEVER an accent slanting up or down, and never an umlaut. Every occurrence "
          "of the same name in this chapter is lettered identically. ")

PAGES = [
 # ---- Spread 1: the report he did not volunteer ------------------------------------
 ("p01", dict(scene="establishing", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FIVE panels. The room is fixed before anything is argued.\n"
  "PANEL 1 (full-width top establishing strip): the office seen from high near the door. The "
  "blonde woman sits reader-LEFT behind the desk, angled toward the open floor; the white-haired "
  "man stands reader-RIGHT at the window with one shoulder against the frame; the CENTRE "
  "FOREGROUND IS EMPTY. Both eye-lines converge on that empty space. The UPPER RIGHT of this "
  "panel is PROTECTED EMPTY NEGATIVE SPACE — no figure, furniture, shadow or balloon may enter "
  "it — and carries only the chapter marker.\n"
  "PANEL 2 (upper-middle wide band): a clockwise swirl of flat opaque orange-red flame with hard "
  "black outlines opens at reader-RIGHT and carries the blond teen right-to-left into the centre "
  "before the desk. His movement leads directly toward the blonde woman. The white-haired man "
  "turns his head but does not leave the window.\n"
  "PANEL 3 (middle-right narrow close-up): the blonde woman's fingers stop on a closed report. "
  "Her eyes aim down-left toward the blond teen.\n"
  "PANEL 4 (middle-left medium on the blond teen): he finishes materialising, body square to the "
  "desk, face turned slightly reader-left toward her.\n"
  "PANEL 5 (full-width bottom, two-plane panel): the blond teen occupies the foreground "
  "reader-RIGHT; the blonde woman is seated in the background reader-LEFT with the desk a hard "
  "barrier between them. The white-haired man stays at the far right edge behind the blond teen, "
  "watching. " + L_HOK
  + 'LETTERING: in the protected upper-right area of PANEL 1, write the chapter marker '
    'horizontally in bold upright English capitals on one line: "CHAPTER 10 — PERMISSION". It is '
    'a tail-less title, not a balloon, and it stays separate from every balloon on the page. '
  + SFX(2, "WHFF.", "Upper right, integrated into the thinning flame, with no tail.")
  + SAY((3, TSU, "upper right", "YOU CAME BACK THIS MORNING."),
        (4, BOY16, "upper right", "YOU NOTICED."),
        (5, TSU, "upper right above the desk", "YOU WALKED THROUGH MY GATE WITH AN UNREGISTERED FOREIGNER."),
        (5, BOY16, "lower left beside his shoulder", "SHE IS UNDER MY PROTECTION.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FOUR panels. A border violation becomes the real dispute.\n"
  "PANEL 1 (full-width top, medium on the blonde woman and the desk): she slides the gate report "
  "left-to-right across the desk toward the blond teen. The paper's motion carries the eye from "
  "her at reader-left to him at reader-right.\n"
  "PANEL 2 (middle-right insert): the report stops at his side of the desk; his gloved hand rests "
  "near it but does not take it. Only the desktop, the paper and that hand are in the crop — his "
  "face is NOT drawn in this panel. All writing on the report is ILLEGIBLE SCRIBBLE, not readable "
  "words.\n"
  "PANEL 3 (middle-left tight two-shot across the desk): her eyes stay on him; he looks OVER the "
  "report rather than down at it.\n"
  "PANEL 4 (bottom dominant triangular three-shot, the focal panel): the blonde woman reader-left "
  "behind the desk, the blond teen standing centre foreground, the white-haired man reader-right "
  "by the window. She and the blond teen lock eye-lines; the white-haired man watches without "
  "entering the argument. " + L_HOK
  + SAY((1, TSU, "upper right", "YOU LEFT WITHOUT PERMISSION AND RETURNED WITHOUT REPORTING."),
        (2, OFF(BOY16), "upper right", "KARIN UZUMAKI IS UNDER MY PROTECTION."),
        (3, TSU, "upper right", "I'M ASKING WHY SHE ENTERED WITHOUT CLEARANCE."),
        (3, BOY16, "lower left", "ASK HER."),
        (4, TSU, "upper right", "THIS ISN'T ABOUT KARIN."),
        (4, TSU, "lower left", "IT'S ABOUT WHETHER MY ORDERS APPLY TO YOU."))
  + "BOTH PANEL 4 BALLOONS ARE THE BLONDE WOMAN'S. She sits reader-LEFT behind the desk and the "
    "blond teen stands in the centre foreground; each of her two balloons needs a tail that ends "
    "at HER mouth, however far left that is. Neither tail may stop on the blond teen's red "
    "armour, his shoulder or his body — he says nothing at all in PANEL 4, and a tail landing on "
    "him would hand him her line about her own orders. "
  + "The PANEL 1 balloon reads exactly \"YOU LEFT WITHOUT PERMISSION AND RETURNED WITHOUT "
    "REPORTING.\" — LEFT is spelled L-E-F-T, four letters with an F as the third letter. Never "
    "write LEPT, LEFF or any other form of it. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 2: authority versus reach ---------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FOUR panels. A demand for assent that is never given.\n"
  "PANEL 1 (full-width top, medium-wide): the blonde woman stands up behind the desk, rising and "
  "shifting slightly reader-right; the blond teen stays still on the opposite side. The change in "
  "height puts their eyes on one level.\n"
  "PANEL 2 (middle-right close-up on the blonde woman): her question lands hard.\n"
  "PANEL 3 (middle-left close-up on the blond teen's face): he meets her gaze without nodding, "
  "without lowering his chin and without shifting his stance. NO TEXT IN THIS PANEL — the full "
  "silence after her question is the point.\n"
  "PANEL 4 (full-width bottom, over the blond teen's shoulder): she sits and turns the report "
  "over as if an answer had been entered on it; the white-haired man at reader-right notices that "
  "the blond teen never agreed. The blond teen stays motionless in the foreground. " + L_HOK
  + SAY((1, TSU, "upper right", "NO KONOHA SHINOBI LEAVES WITHOUT MY ORDER."),
        (2, TSU, "upper right", "IS THAT CLEAR?"),
        (4, TSU, "upper left", "GOOD. THEN IT WON'T HAPPEN AGAIN.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. A failed search and a lost handle become the pressure.\n"
  "PANEL 1 (top-right tight two-shot on the blonde woman and the blond teen across the desk "
  "edge): their eye-line forms a diagonal running down-left.\n"
  "PANEL 2 (top-left close-up on the blond teen): one word, no movement.\n"
  "PANEL 3 (middle-right medium on the white-haired man): he walks from the window toward the "
  "desk, right-to-left, one hand open in frustration. The blond teen is NOT drawn in this panel.\n"
  "PANEL 4 (middle-left close-up on the white-haired man): his movement stops; his eye-line snaps "
  "down-left. The blond teen is NOT drawn in this panel either.\n"
  "PANEL 5 (narrow silent reaction band): the blonde woman's mouth almost turns upward as she "
  "registers how completely the blond teen caught the white-haired man's overstatement. She masks "
  "it and rises from her chair, one palm coming down on the desk before either man looks at her. "
  "NO TEXT IN THIS PANEL.\n"
  "PANEL 6 (bottom dominant wide, the focal panel): the blonde woman stands reader-left with one "
  "palm flat on the desk; the blond teen stands reader-right, unmoved; the white-haired man now "
  "occupies the middle background. The desk line points from her to him. " + L_HOK
  + SAY((1, TSU, "upper right", "WHERE WERE YOU FOR THREE YEARS?"),
        (2, BOY16, "upper right", "SAFE."),
        (3, JIRA, "upper right", "I SEARCHED EVERYWHERE."),
        (3, OFF(BOY16), "lower left", "NOT EVERYWHERE."),
        (4, JIRA, "upper right", "DON'T PLAY WITH WORDS."),
        (4, OFF(BOY16), "lower left", "YOU FAILED TO FIND ME."),
        (6, BOY16, "upper right", "THAT IS THE FACT YOU DISLIKE."),
        (6, TSU, "upper-left centre", "THE FACT I DISLIKE IS THAT ONE OF MY SHINOBI CAN VANISH BEYOND MY REACH."),
        (6, BOY16, "lower left", "THEN THIS IS ABOUT CONTROL. NOT SAFETY.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "medium"),

 # ---- Spread 3: the price of a straight answer -------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. Three incompatible definitions of trust, none of them resolved.\n"
  "PANEL 1 (top-right close-up on the blonde woman): her anger tightens into calculation; "
  "eye-line down-left.\n"
  "PANEL 2 (top-left close-up on the blond teen): level, unhurried.\n"
  "PANEL 3 (middle-right medium on the white-haired man beside the desk): he leans one hand on "
  "its reader-right corner, closing the triangle.\n"
  "PANEL 4 (middle-centre narrow crop on the blond teen's mouth and collar): the face is cropped "
  "above the eyes; his mouth is clearly inside the panel.\n"
  "PANEL 5 (middle-left close-up on the white-haired man): he looks directly at the blond teen "
  "with no comic expression at all.\n"
  "PANEL 6 (full-width bottom close three-shot): the blond teen's eyes move first to the blonde "
  "woman at reader-left, then back toward the white-haired man at reader-right; neither adult "
  "looks away. " + L_HOK
  + SAY((1, TSU, "upper right", "IT IS ABOUT KNOWING WHETHER YOU ARE A THREAT."),
        (2, BOY16, "upper right", "IF YOU THINK I AM, PROVE IT."),
        (3, JIRA, "upper right", "YOUR SECRETS MAKE THAT HARD."),
        (4, BOY16, "upper right", "THAT IS WHAT SECRETS ARE FOR."),
        (5, JIRA, "upper right", "DO YOU TRUST ANYONE IN THIS ROOM?"),
        (6, BOY16, "lower left", "WITH WHAT?")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 ("p06", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FIVE panels. Verification offered instead of confession.\n"
  "PANEL 1 (top-right close-up on the white-haired man): flat demand.\n"
  "PANEL 2 (top-left medium on the blond teen): he turns his torso a fraction toward the "
  "white-haired man but keeps one shoulder toward the blonde woman, refusing either adult sole "
  "ownership of the exchange.\n"
  "PANEL 3 (middle-right medium on the blonde woman): she sits again without relaxing, moving "
  "down-left into her chair.\n"
  "PANEL 4 (middle-left close-up on the blond teen): unmoved.\n"
  "PANEL 5 (bottom dominant on the white-haired man with the blond teen in foreground profile, "
  "the focal panel): the white-haired man's jaw sets; the blond teen's visible eye sits at the "
  "panel's reader-LEFT edge, watching him. " + L_HOK
  + SAY((1, JIRA, "upper right", "A STRAIGHT ANSWER."),
        (2, BOY16, "upper right", "SEARCH YOUR NETWORK."),
        (2, BOY16, "lower left", "IF YOU FIND THAT I MOVED AGAINST KONOHA, CONFRONT ME WITH EVIDENCE."),
        (3, TSU, "upper right", "AND IF HE FINDS NOTHING?"),
        (4, BOY16, "upper right", "THEN HE LEARNS THE LIMIT OF HIS NETWORK."),
        (5, JIRA, "upper right", "YOU KNOW I WON'T FIND YOUR TRAIL."),
        (5, BOY16, "lower left", "THEN YOU ALREADY KNOW WHY I WON'T GIVE IT TO YOU.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 4: Karin is not evidence ----------------------------------------------
 ("p07", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. The red-haired girl is discussed and NEVER appears — no flashback, no inset, no "
  "silhouette of her anywhere on this page.\n"
  "PANEL 1 (full-width top on the blonde woman seated behind the desk): she pulls the gate report "
  "back toward herself, right-to-left, closing the first line of inquiry.\n"
  "PANEL 2 (middle-right medium on the blond teen): flat delivery.\n"
  "PANEL 3 (middle-centre close-up on the blonde woman): one name, stated rather than asked.\n"
  "PANEL 4 (middle-left medium on the white-haired man): he studies the blond teen rather than "
  "the blonde woman.\n"
  "PANEL 5 (bottom-right close-up on the blond teen): nothing added.\n"
  "PANEL 6 (bottom-left narrow close-up on the blonde woman's eyes): her gaze points up-right "
  "toward the blond teen, who is NOT drawn in this panel. " + L_HOK
  + SAY((1, TSU, "upper right", "WHY OROCHIMARU?"),
        (2, BOY16, "upper right", "HE HELD AN UZUMAKI."),
        (3, TSU, "upper right", "KARIN."),
        (4, JIRA, "upper right", "WHAT MADE HER USEFUL TO HIM?"),
        (5, BOY16, "upper right", "SHE WORKED AS A SCIENTIST."),
        (6, TSU, "upper right", "ONLY THAT?"),
        (6, OFF(BOY16), "lower left", "THAT IS ALL YOU NEED.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 ("p08", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. Protection tested directly; nothing about her ability is shown or drawn.\n"
  "PANEL 1 (top-right medium on the blonde woman): a direct test.\n"
  "PANEL 2 (top-left close-up on the blond teen): one syllable.\n"
  "PANEL 3 (middle-right, over the blonde woman's shoulder toward the blond teen): she is the "
  "foreground shoulder; he faces her across the desk.\n"
  "PANEL 4 (middle-centre close-up on the blond teen's gloved hand at his side): the fingers "
  "close once and then rest. Hand only — no face in this crop. NO TEXT IN THIS PANEL.\n"
  "PANEL 5 (middle-left medium two-shot on the white-haired man and the blond teen): the "
  "white-haired man's eye-line presses down-left; the blond teen looks past him toward the blonde "
  "woman.\n"
  "PANEL 6 (bottom dominant horizontal, the focal panel): the blonde woman reader-left, the blond "
  "teen reader-right, isolated from each other by the empty desktop between them. " + L_HOK
  + SAY((1, TSU, "upper right", "IS SHE DANGEROUS?"),
        (2, BOY16, "upper right", "NO."),
        (3, TSU, "upper right", "DOES SHE HAVE ABILITIES I SHOULD KNOW ABOUT?"),
        (5, JIRA, "upper right", "THERE IT IS AGAIN."),
        (5, BOY16, "lower left", "HER ABILITIES ARE HERS."),
        (6, TSU, "upper right", "AND OROCHIMARU?"),
        (6, BOY16, "upper centre", "DEAD."),
        (6, TSU, "lower centre", "PROOF?"),
        (6, BOY16, "lower left", "I BURNED EVERY PIECE."))
  + "PANEL 6 CARRIES FOUR BALLOONS IN ONE FIXED RIGHT-TO-LEFT, TOP-TO-BOTTOM ORDER, AND THE FIRST "
    "TWO ARE THE TEST: \"AND OROCHIMARU?\" sits at the panel's UPPER RIGHT and \"DEAD.\" sits "
    "BELOW AND TO ITS LEFT, never level with it and never to its right, so the question is read "
    "before the answer. \"PROOF?\" follows below them at the lower centre and \"I BURNED EVERY "
    "PIECE.\" last at the lower left. The two questions tail across to the blonde woman at "
    "reader-left; the two answers tail across to the blond teen at reader-right. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 5: consequences belong to the Hokage ----------------------------------
 ("p09", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FOUR panels. An outcome is not the same thing as a plan.\n"
  "PANEL 1 (full-width top): the white-haired man crosses one step leftward BETWEEN the blonde "
  "woman's and the blond teen's eye-lines without physically blocking either face.\n"
  "PANEL 2 (middle-right close two-shot on the blonde woman and the Kiri report): the report lies "
  "under her hand; all writing on it is ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 3 (middle-left close-up on the blond teen): two words, no defence.\n"
  "PANEL 4 (bottom dominant across the desk, the focal panel): she leans toward him; he neither "
  "retreats nor advances. His answer is withheld for the page turn — he stays silent here. "
  + L_HOK
  + SAY((1, JIRA, "upper right", "AND KIRI?"),
        (1, JIRA, "lower left", "WAS AN ENTIRE VILLAGE AN OBSTRUCTION?"),
        (2, TSU, "upper right", "WHAT YOU DID WAS RECKLESS."),
        (2, TSU, "lower left", "YOU COULD HAVE DIED."),
        (3, BOY16, "upper right", "I DIDN'T."),
        (4, TSU, "upper right", "THAT DOESN'T MAKE IT A PLAN."))
  + "BOTH PANEL 1 BALLOONS ARE THE BIG WHITE-HAIRED MAN'S — \"AND KIRI?\" and \"WAS AN ENTIRE "
    "VILLAGE AN OBSTRUCTION?\" — and they are his only lines on the page. He is crossing the "
    "panel one step leftward, so the lower-left balloon needs a LONG tail that travels all the "
    "way back across the panel to HIS mouth, passing clear of everyone else. That tail must NOT "
    "stop on the blonde woman, her shoulder or her green haori, however much closer to her the "
    "balloon sits; she says nothing in PANEL 1. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 ("p10", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FOUR panels. The Kiri leader is named but NEVER drawn — no portrait, no inset, no silhouette "
  "of her anywhere on this page.\n"
  "PANEL 1 (top-right insert): the blonde woman opens a clean diplomatic letter carrying a wax "
  "seal; her hand moves it right-to-left. Only hands, desk and letter are in the crop, and the "
  "blond teen is NOT drawn in this panel. Every mark on the letter and its seal is ILLEGIBLE "
  "SCRIBBLE, not readable words.\n"
  "PANEL 2 (top-left medium on the blonde woman): she turns the sealed page toward the blond "
  "teen.\n"
  "PANEL 3 (middle dominant overhead, the focal panel): straight down onto the desk — the "
  "alliance letter occupies the centre, the blonde woman is reader-left behind it and the blond "
  "teen reader-right before it, their hands stopping on opposite sides of it.\n"
  "PANEL 4 (bottom full-width wide): the white-haired man plants his palm on the desk beside the "
  "letter, stopping the horizontal argument; both other eye-lines move to him. " + L_HOK
  + SAY((1, OFF(BOY16), "upper right", "IT MADE AN END."),
        (2, TSU, "upper right", "AND A BEGINNING."),
        (2, TSU, "lower left", "MEI WILL ARRIVE IN A FEW DAYS TO DISCUSS AN ALLIANCE."),
        (3, BOY16, "upper right", "THEN ANSWER HER."),
        (4, JIRA, "lower left", "KIRI CAN WAIT. AKATSUKI CAN'T.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "medium"),

 # ---- Spread 6: information has a destination --------------------------------------
 ("p11", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FIVE panels. What the intelligence is for.\n"
  "PANEL 1 (top-right close-up on the white-haired man): the question he came for.\n"
  "PANEL 2 (top-left close-up on the blond teen): compact answer.\n"
  "PANEL 3 (middle full-width opposing profiles): the white-haired man reader-RIGHT facing left; "
  "the blond teen reader-LEFT facing right.\n"
  "PANEL 4 (bottom-right wide on the blond teen, with a FAINT NON-LITERAL COMPOSITION behind him: "
  "five simple abstract village emblem shapes used as graphic anchors on the wall behind his "
  "shoulders, flat and decorative, carrying NO readable writing of any kind and no map "
  "coastlines): the white-haired man leans into the panel from reader-right.\n"
  "PANEL 5 (bottom-left close two-shot on the white-haired man and the blond teen): the blond "
  "teen's eye-line passes the white-haired man toward the sealed Kiri letter on the desk. The "
  "white-haired man makes his inference from the completed village analysis. " + L_HOK
  + SAY((1, JIRA, "upper right", "HOW MUCH DO YOU KNOW ABOUT AKATSUKI?"),
        (2, BOY16, "upper right", "I KNOW THE AKATSUKI MEMBERS."),
        (3, JIRA, "upper right", "ALL OF THEM?"),
        (3, BOY16, "lower left", "ALL THAT I NEED."),
        (4, JIRA, "upper right", "I'D WARN THE OTHER VILLAGES."),
        (4, BOY16, "lower left", "IWA AND TAKI NEGLECT THEIRS. KUMO TRUSTS ITS OWN POWER."),
        (5, BOY16, "upper right", "SAND WILL LISTEN. KIRI HAS NONE LEFT."),
        (5, JIRA, "lower left", "YOU KNOW WHERE EVERY JINCHŪRIKI IS.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "medium"),

 ("p12", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. Ground given, a secret kept, and one lead exposed.\n"
  "PANEL 1 (top-right medium on the blond teen): the bounded offer.\n"
  "PANEL 2 (top-left close-up on the white-haired man): he presses for more.\n"
  "PANEL 3 (middle-right close-up on the blond teen): one word.\n"
  "PANEL 4 (middle-centre narrow crop on the white-haired man's eyes): eyes and brow only.\n"
  "PANEL 5 (middle-left tight exchange in profile): the white-haired man reader-RIGHT facing "
  "left; the blond teen reader-LEFT facing right.\n"
  "PANEL 6 (bottom dominant wide, the focal panel): the white-haired man straightens and turns "
  "his body toward the window at reader-RIGHT, but looks back over his LEFT shoulder to the blond "
  "teen; the movement reads as imminent departure. The blond teen's eyes sharpen for the first "
  "time in the chapter. " + L_HOK
  + SAY((1, BOY16, "upper right", "I WILL GIVE YOU THE MEMBERS' PROFILES."),
        (2, JIRA, "upper right", "INCLUDING THEIR LEADER?"),
        (3, BOY16, "upper right", "NO."),
        (4, JIRA, "upper right", "WHY?"),
        (5, BOY16, "lower left", "BECAUSE YOU DISTRIBUTE INFORMATION BEFORE YOU UNDERSTAND ITS COST."),
        (6, JIRA, "upper right", "I HAVE A LEAD."),
        (6, JIRA, "upper centre", "AME."),
        (6, BOY16, "lower left", "DON'T GO.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 7: the country no spy leaves ------------------------------------------
 ("p13", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16,
         "a masked salamander-helmeted warrior, three much smaller young figures, and one "
         "anonymous rain-veiled figure appearing ONLY as FLAT FEATURELESS BLACK AND GREY "
         "SILHOUETTES inside the symbolic history panel 4, with no faces, no identifying detail "
         "and no presence anywhere else on the page") + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FOUR large panels. The danger is identified without being named.\n"
  "PANEL 1 (top half-width two-shot, reader-right half of the top tier): the white-haired man "
  "stays half-turned toward the window at reader-right; the blond teen is grounded at "
  "reader-left.\n"
  "PANEL 2 (top half-width medium on the blonde woman, reader-left half of the top tier): she "
  "rises again but does not interrupt the other two men's eye-line.\n"
  "PANEL 3 (middle full-width close-up on the blond teen): leave OPEN RAIN-GREY NEGATIVE SPACE "
  "behind his hair — no figure, no furniture, no balloon in it beyond his own.\n"
  "PANEL 4 (bottom dominant symbolic history panel, the focal panel): NOT a witnessed flashback "
  "and NOT a present scene — a flat inferred history image. A tall masked salamander-helmeted "
  "silhouette stands reader-RIGHT above three much smaller young silhouettes; a second, anonymous "
  "rain-veiled silhouette occupies reader-LEFT and forces the salamander shape BACKWARD. Every "
  "figure in this panel is a flat opaque featureless silhouette against falling rain — no face, "
  "no eyes, no readable insignia. The blond teen, the blonde woman and the white-haired man are "
  "not drawn inside this panel. " + L_HOK
  + 'LETTERING: in PANEL 4, in the lower left, draw ONE plain RECTANGULAR BORDERLESS VOICE-OVER '
    'box with NO TAIL AT ALL, containing only the words: "HE DEFEATED HANZŌ. EASILY." It is the '
    'blond teen speaking from outside the panel; it is not a speech balloon and must not point at '
    'any silhouette. '
  + SAY((1, JIRA, "upper right", "THAT SOUNDED LIKE AN ORDER."),
        (1, BOY16, "lower left", "IT WAS A WARNING."),
        (2, TSU, "upper right", "WHAT IS IN AME?"),
        (3, BOY16, "upper right", "AKATSUKI'S LEADER.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "high"),

 ("p14", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM + MACRON +
  "SIX panels. The threat is measured correctly and the mission is taken anyway. No silhouettes, "
  "no history images and no flashback appear on this page.\n"
  "PANEL 1 (top-right close-up on the white-haired man): disbelief without comedy.\n"
  "PANEL 2 (top-left close-up on the blond teen): flat statement.\n"
  "PANEL 3 (middle-right medium on the blonde woman between them): her eyes narrow as the old "
  "intelligence picture changes.\n"
  "PANEL 4 (middle-left close-up on the blonde woman, aimed at the blond teen): the source "
  "question.\n"
  "PANEL 5 (lower-right close-up on the blond teen): he holds her gaze and supplies no answer at "
  "all. NO TEXT IN THIS PANEL.\n"
  "PANEL 6 (bottom-left dominant three-shot, the focal panel): the white-haired man turns fully "
  "from the window and faces the blond teen; the blonde woman remains between their depth planes. "
  + L_HOK
  + SAY((1, JIRA, "upper right", "HANZŌ? THE MAN WHO NAMED US SANNIN?"),
        (2, BOY16, "upper right", "THE MAN ALL THREE OF YOU COULD NOT DEFEAT IN YOUR PRIME."),
        (3, TSU, "upper right", "LAST I HEARD, AME WAS LOCKED IN A CIVIL WAR."),
        (3, TSU, "lower left", "LATELY, NO SPY GOES IN AND COMES OUT."),
        (4, TSU, "upper right", "HOW DO YOU KNOW THIS?"),
        (6, JIRA, "upper right", "IF IT'S TRUE, I HAVE MORE REASON TO GO."),
        (6, BOY16, "lower centre", "IF YOU ENTER AME, AKATSUKI'S LEADER WILL KILL YOU."),
        (6, JIRA, "lower left", "I'M STILL GOING."))
  + "PANEL 6 ATTRIBUTION, AND THE TWO TAILS MUST NOT BE INTERCHANGED: \"IF IT'S TRUE, I HAVE MORE "
    "REASON TO GO.\" and \"I'M STILL GOING.\" are "
    "BOTH the white-haired man's and BOTH their tails must end at HIS mouth. \"IF YOU ENTER AME, "
    "AKATSUKI'S LEADER WILL KILL YOU.\" is the blond teen's alone and its tail must end at HIS "
    "mouth. No tail may cross to the other man: the warning belongs to the teen and the refusal "
    "belongs to the older man. "
  + "The lower PANEL 3 balloon reads exactly \"LATELY, NO SPY GOES IN AND COMES OUT.\" — nine "
    "words and no more. AND is spelled A-N-D, and there is no stray \"AD\", no repeated word and "
    "no extra letter anywhere in the balloon. COMES is spelled C-O-M-E-S with a fully formed "
    "capital M of two clean diagonal strokes between its two verticals. The PANEL 1 balloon reads "
    "exactly \"HANZŌ? THE MAN WHO NAMED US SANNIN?\", with a single straight horizontal bar above "
    "the O of HANZŌ. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 8: equal movement, unequal trust --------------------------------------
 ("p15", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SIX panels. The request grows out of the other man's decision.\n"
  "PANEL 1 (top-right silent close-up on the blond teen): his eyes leave the white-haired man and "
  "travel reader-LEFT toward the blonde woman. NO TEXT IN THIS PANEL.\n"
  "PANEL 2 (top-left medium on the blond teen and the blonde woman — an ordinary rectangle "
  "sharing the top tier with PANEL 1 and the same height as it, never a tall panel running down "
  "the page beside the panels below): he rotates his shoulders "
  "left; she meets the new eye-line.\n"
  "PANEL 3 (middle-right close-up on the blonde woman): flat incredulity.\n"
  "PANEL 4 (middle-centre close-up on the blond teen): three words.\n"
  "PANEL 5 (middle-left wide three-shot): the white-haired man stays reader-right and slightly "
  "separated; the blond teen stands centre; the blonde woman is reader-left. The blond teen's "
  "open hand indicates the white-haired man WITHOUT him looking back.\n"
  "PANEL 6 (full-width bottom reaction exchange): the blonde woman and the blond teen face each "
  "other across the desk; the white-haired man watches between them. " + L_HOK
  + SAY((2, BOY16, "upper right", "THEN I HAVE A REQUEST."),
        (3, TSU, "upper right", "YOU WARN HIM HE'LL DIE, THEN CHANGE THE SUBJECT?"),
        (4, BOY16, "upper right", "HE HAS CHOSEN."),
        (5, BOY16, "upper right", "I NEED THE SAME FREEDOM JIRAIYA HAS—TO LEAVE KONOHA AND ENTER OTHER VILLAGES WITHOUT DELAY."),
        (6, TSU, "upper right", "NO."),
        (6, BOY16, "upper centre", "THAT WAS QUICK."),
        (6, TSU, "lower left", "YOU JUST RETURNED FROM DISAPPEARING FOR THREE YEARS."))
  + "SIX SEPARATE PANELS IN FOUR HORIZONTAL TIERS, NONE OF THEM TALL. Tier 1 is PANEL 1 RIGHT and "
    "PANEL 2 LEFT; tier 2 is PANEL 3 RIGHT and PANEL 4 LEFT; tier 3 is PANEL 5 full width; tier 4 "
    "is PANEL 6 full width. PANEL 2, the two-shot, is an ordinary rectangle confined to tier 1 "
    "and NEVER a tall panel running down the page beside a stacked right-hand column, so \"THEN I "
    "HAVE A REQUEST.\" is read BEFORE \"YOU WARN HIM HE'LL DIE, THEN CHANGE THE SUBJECT?\" "
    "PANEL 6 BALLOON ORDER IS FIXED AND RUNS RIGHT TO LEFT: the refusal \"NO.\" sits at the "
    "panel's UPPER RIGHT, \"THAT WAS QUICK.\" sits to its LEFT, and \"YOU JUST RETURNED FROM "
    "DISAPPEARING FOR THREE YEARS.\" sits lower and further left again. Never place \"NO.\" to "
    "the left of \"THAT WAS QUICK.\" ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 ("p16", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "FIVE panels. Capability is not the same as accountability.\n"
  "PANEL 1 (top-right medium on the blond teen): the comparison stated plainly.\n"
  "PANEL 2 (top-left medium on the blonde woman): she answers it. The white-haired man is NOT "
  "drawn in this panel.\n"
  "PANEL 3 (middle-right close-up on the blonde woman glaring PAST the blond teen at the "
  "white-haired man): the blond teen is only a blurred out-of-focus foreground edge.\n"
  "PANEL 4 (middle-left medium on the blond teen): his own claim.\n"
  "PANEL 5 (bottom dominant across the desk, the focal panel): the blonde woman leans forward "
  "from reader-left; the blond teen mirrors her from reader-right WITHOUT touching the desk. "
  "Their faces occupy equal scale in the frame. " + L_HOK
  + SAY((1, BOY16, "upper right", "JIRAIYA DISAPPEARS WHEN HIS WORK REQUIRES IT."),
        (2, TSU, "upper right", "JIRAIYA REPORTS TO ME."),
        (2, OFF(JIRA), "lower right corner, well clear of her face", "EVENTUALLY."),
        (3, TSU, "upper right", "HE ALSO BUILT ACCESS OVER DECADES."),
        (4, BOY16, "upper right", "I RETURN WITH INFORMATION HE CANNOT FIND."),
        (5, TSU, "upper right", "THAT IS USEFUL."),
        (5, TSU, "upper centre-left", "IT ISN'T THE SAME AS ACCOUNTABLE."),
        (5, BOY16, "lower left", "THEN SET TERMS THAT DO NOT ASK FOR MY SOURCES."))
  + "PANEL 5 CARRIES THREE BALLOONS IN ONE FIXED RIGHT-TO-LEFT ORDER AND GETTING IT BACKWARDS "
    "INVERTS THE WHOLE EXCHANGE: \"THAT IS USEFUL.\" sits FURTHEST RIGHT and is read first, \"IT "
    "ISN'T THE SAME AS ACCOUNTABLE.\" sits to its LEFT and is read second, and \"THEN SET TERMS "
    "THAT DO NOT ASK FOR MY SOURCES.\" sits FURTHEST LEFT and lowest and is read last. The first "
    "two are the blonde woman's and tail to her at reader-left; the third is the blond teen's and "
    "tails across to him at reader-right. "
    "In PANEL 2 the balloon \"EVENTUALLY.\" belongs to the big white-haired man, who is NOT DRAWN "
    "IN THAT PANEL. It sits in the panel's LOWER RIGHT corner — the side he stands on elsewhere "
    "in the room — and carries a clearly VISIBLE off-panel spur: a short straight tail running "
    "from the balloon to the panel's RIGHT border and stopping there, pointing out of the frame. "
    "It must never sit under, beside or level with the blonde woman's mouth, and no part of it "
    "may aim at her, because an untailed balloon near her face turns his interruption into a "
    "second line of hers. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "low"),

 # ---- Spread 9: permission remains withheld ----------------------------------------
 ("p17", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM + MACRON +
  "FIVE panels. Demonstrated value is separated from inherited prestige.\n"
  "PANEL 1 (top-right close-up on the blonde woman): she reaches for the institutional name.\n"
  "PANEL 2 (top-left medium on the blond teen): his eye-line stays on the blonde woman and never "
  "goes hunting for the white-haired man's reaction.\n"
  "PANEL 3 (middle full-width opposing two-shot): the white-haired man steps right-to-left into "
  "the blond teen's eye-line; the blond teen turns only his eyes toward him, not his body.\n"
  "PANEL 4 (narrow silent close-up on the white-haired man): the line lands and he does not joke "
  "it away. NO TEXT IN THIS PANEL.\n"
  "PANEL 5 (bottom dominant low-angle on the blond teen, the focal panel): the two adults frame "
  "him at the far left and far right edges, but his upright figure owns the central vertical of "
  "the panel. His gaze moves from the white-haired man to the blonde woman. " + L_HOK
  + "In PANEL 5 the blonde woman's second balloon is border-cut, its tail running to her at the "
    "panel edge. "
  + SAY((1, TSU, "upper right", "THOSE FREEDOMS BELONG TO THE SANNIN."),
        (2, BOY16, "upper right", "I AM STRONGER THAN JIRAIYA. I JUST GAVE YOU INTELLIGENCE HE DIDN'T HAVE."),
        (3, JIRA, "upper right", "THAT TITLE MEANS SOMETHING."),
        (3, BOY16, "lower left", "IT MEANS HANZŌ LET YOU LIVE."),
        (5, BOY16, "upper right", "I WILL NOT USE ANOTHER MAN'S MERCY AS A MEASURE OF MY WORTH."),
        (5, TSU, "upper centre-left", "YOU WANT THE RIGHTS WITHOUT THE NAME."),
        (5, BOY16, "lower centre", "I WANT MY WORK JUDGED BY ITS RESULTS."),
        (5, TSU, "lower left", "AND I WANT TO KNOW WHERE MY SHINOBI ARE."))
  + "The lower PANEL 3 balloon reads exactly \"IT MEANS HANZŌ LET YOU LIVE.\" — five words. YOU "
    "is spelled Y-O-U, beginning with a Y and never with a D; never write DOU, DOD or YOD. HANZŌ "
    "is lettered H-A-N-Z-O with a single straight horizontal bar above the final O — the same "
    "mark used on the earlier page that names him, never a wavy tilde and never two dots. ",
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "medium"),

 ("p18", dict(scene="emotional_closeup", light="day", cast="small_group", mood="somber", panels=7),
  FILL + RTL + TSUNADE.format(i=1) + JIR.format(i=2) + N16_ARMOR.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, JIRA, BOY16) + GEO + NOGUNBAI + SHARINGAN + PALE + CALM +
  "SEVEN panels. LAST PAGE OF THE CHAPTER — permission stays withheld and the wound is personal.\n"
  "PANEL 1 (top-right medium on the blonde woman): she closes the Kiri letter and puts both hands "
  "flat on it, ending the meeting without yielding anything.\n"
  "PANEL 2 (top-left close-up on the blond teen): three words.\n"
  "PANEL 3 (middle-right medium on the white-haired man): he reaches one hand toward the blond "
  "teen as the blond teen begins to turn away to reader-left.\n"
  "PANEL 4 (middle-centre profile on the blond teen, movement arrested): he looks back over his "
  "shoulder without turning his body.\n"
  "PANEL 5 (middle-left two-shot): the blond teen is foreground reader-LEFT; the white-haired man "
  "is background reader-RIGHT with the window's village skyline behind him.\n"
  "PANEL 6 (bottom-right narrow close-up on the blond teen's impassive visible eye): the "
  "Sharingan is calm and unblinking.\n"
  "PANEL 7 (bottom-left dominant exit panel, the focal panel): the blond teen dissolves "
  "right-to-left into a swirl of flat opaque orange-red flame with hard black outlines. The "
  "white-haired man has ALREADY drawn his reaching hand back; his hurt expression settles and his "
  "eye-line leaves the blond teen's emptying space and returns to the window. The blonde woman "
  "watches the white-haired man recover rather than watching the exit. " + L_HOK
  + "In PANEL 7 the blond teen's balloon is border-cut and its tail enters the flame where his "
    "mouth still is, before he vanishes. "
  + "PANEL 5 CARRIES THE CHAPTER'S CLOSING BEAT AND ITS TWO BALLOONS HAVE DIFFERENT SPEAKERS. The "
    "upper-right balloon \"IF YOU DIE, KONOHA LOOKS WEAK.\" is the blond teen's: its tail runs "
    "down-LEFT to his mouth in the foreground. The lower-left balloon \"SO THAT'S ALL I AM TO "
    "YOU?\" is the BIG WHITE-HAIRED MAN'S, and it needs a LONG tail travelling up-RIGHT across "
    "the whole panel to HIS mouth in the background, passing clear of the blond teen. That tail "
    "must NEVER point up into the blond teen's body, his red armour or his hair — if both "
    "balloons read as the blond teen the page loses the hurt question the chapter ends on. "
  + SFX(7, "WHFF.", "Low left, inside the last curl of flame, with no tail.")
  + SAY((1, TSU, "upper right", "I'LL DISCUSS IT WITH JIRAIYA. YOU HAVE NO PERMISSION YET."),
        (2, BOY16, "upper right", "THEN DISCUSS QUICKLY."),
        (3, JIRA, "upper right", "NARUTO. ABOUT AME—"),
        (4, BOY16, "upper right", "MINATO AND THE THIRD ARE DEAD."),
        (5, BOY16, "upper right", "IF YOU DIE, KONOHA LOOKS WEAK."),
        (5, JIRA, "lower left", "SO THAT'S ALL I AM TO YOU?"),
        (6, BOY16, "upper right", "STRATEGICALLY, YOUR DEATH MATTERS."),
        (7, BOY16, "upper right", "PERSONALLY, I DON'T CARE WHICH YOU CHOOSE.")),
  R("tsunade", "jiraiya", "naruto_v4_armor", "env_hokage_office"), "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch10" / "raw", HERE / "v5ch10" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
