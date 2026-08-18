"""Volume 5, Chapter 3 — "The Other Uchiha". 16 pages.

Source: fic ch12:283-394. Translated 1:1 from story/volume_05/drafts/ch03_the_other_uchiha.md —
74 dialogue balloons, one time card and one chapter marker across 16 pages. Reading order is
RIGHT TO LEFT per the approved `name`; every page states it.

This builder must match the `name`, not improve on it. Every balloon below is the draft's
exact final text, in the draft's exact panel and position. No line is reworded or merged.

Eye-state lock from the `name`, enforced page by page below: pages 1 and 9-16 use the
ordinary active three-tomoe Sharingan; page 2 uses three tomoe through panel 4 and changes
to the six-bladed Eternal Mangekyo only in panel 5; pages 3-7 hold the six-bladed pattern
for the whole Tsukuyomi mindscape; page 8 opens with it in panel 1 and returns to three
tomoe from panel 2 onward.

Zetsu does not appear anywhere in this chapter, so the ZOR mirror-lock constant is
deliberately absent.

Reference gap recorded for the owner (never invented here): there is no Tsukuyomi-mindscape
environment plate in refs/images, so the black reflective plane under the red sky is carried
entirely by prose on pages 3-8 and no environment reference is bound to those pages.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, FILL, JIR, KAK, MAN, OFF, ONLY, R, SAGE, SAY  # noqa: E402
from prompts_v4 import (KIRI_REBELS, KURAMA_FULL, MANGEKYO_EYE, N16_SWORD,   # noqa: E402
                        SASUKE16, SUSA_FINAL, YUGAO_V4, N16_SPEAKER,
                        SASUKE16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
SAS16 = SASUKE16_SPEAKER
YUG = YUGAO_V4_SPEAKER

# Cast-state and equipment locks. These apply on every page the character appears on and override
# any shorter panel wording.
GEAR = ("EQUIPMENT LOCK for the blond teen on this page: his repaired bright red segmented armour "
        "is clean and undamaged, his partly visible Leaf forehead protector is worn and never "
        "removed or concealed, the dark purple gunbai with its chain stays on his BACK, and the "
        "plain straight sash sword stays in its dark sheath at his LEFT HIP. A camera crop may hide "
        "the sword or the gunbai, but neither is ever unequipped and neither is ever replaced by "
        "another weapon. He carries no injury and no bandage. ")
SAS_LOCK = ("EQUIPMENT LOCK for the older dark-haired teen on this page: high-collared dark travel "
            "shirt with the Uchiha fan crest, dark trousers, forearm guards and shinobi sandals. "
            "His eyes stay ORDINARY DARK — no Sharingan, no red iris, no six-bladed pattern and no "
            "curse-seal markings anywhere on him. His hands stay EMPTY: he carries no sword and no "
            "other exposed large weapon. He carries no injury. ")
KAK_LOCK = ("EQUIPMENT LOCK for the masked silver-haired man on this page: dark navy uniform, green "
            "flak vest, gloves, sandals and a right-thigh kunai holster. He draws no weapon and "
            "carries no injury. ")
JIR_LOCK = ("EQUIPMENT LOCK for the big white-haired man on this page: green kimono top and "
            "trousers over mesh, red sleeveless haori, horned forehead protector, the large scroll "
            "across his back. His hands stay empty, he draws no weapon and he carries no injury. ")
YUG_LOCK = ("EQUIPMENT LOCK for the purple-haired Leaf kunoichi on this page: travel-worn dark "
            "shinobi outfit, fully recovered and uninjured. HER SWORD REMAINS IN WAVE COUNTRY: she "
            "carries no sword, no scabbard and no drawn weapon of any kind. ")

SHAR3 = ("EYE STATE: the blond teen's visible left eye carries the ORDINARY ACTIVE THREE-TOMOE "
         "SHARINGAN — a blood-red iris with a black pupil and exactly three black comma-shaped "
         "tomoe around it. It is never blue, never plain black and never the six-bladed pattern on "
         "this page. ")
EMS = ("EYE STATE: the blond teen's visible left eye carries the SIX-BLADED pattern — a blood-red "
       "iris with one black centre ring and exactly SIX broad black blades radiating outward. It is "
       "never three tomoe, never blue and never plain black on this page. ")

TSUKU = ("THIS PAGE TAKES PLACE ENTIRELY INSIDE THE TSUKUYOMI ILLUSION, not in the physical world: "
         "a flat BLACK REFLECTIVE PLANE stretching to a hard horizon beneath a flat RED SKY, with "
         "no buildings, no crowd, no scaffolds, no weather and no Kiri architecture of any kind. "
         "The palette is limited to black, red and desaturated grey. Both figures keep their real "
         "bodies and real equipment; neither is distorted, ghostly or transparent. ")
CROWD = ("The Kiri workers and civilians are unnamed and non-recurring, and they wear NO forehead "
         "protectors, NO headband plates and NO village symbols of any kind. ")

# ---- V5 ch03 page-QA gate, chapter-wide locks --------------------------------------------
# The gate found Kakashi's orange book present on p01, p08 and p11, gone entirely on p09, p13
# and p15, then open again on p14 where the draft has him closing it. Carried by p09/p13/p15.
KAK_BOOK = ("The masked silver-haired man carries his orange book in one hand in every panel that "
            "shows his hands. ")
# The same gate found Jiraiya's forehead plate alternating between a correct 油, a garbled
# non-word kanji (p13/p14) and a blank plate (p08/p15). Carried by p01/p08/p13/p14/p15.
JIR_KANJI = ("The big white-haired man's forehead protector always bears the single kanji 油, drawn "
             "identically on every panel and every page; never a blank plate and never any other "
             "character. "
             # Round 1 leaked this kanji onto Kakashi's plate on p01; scope it to Jiraiya only.
             "That kanji belongs to HIM ALONE: the masked silver-haired man's forehead "
             "protector carries the plain Leaf spiral symbol and no kanji, and no other "
             "character's headband plate carries any kanji at all. ")

ENV_STREET = ("Image {i} is the LOCATION REFERENCE for the rebuilding Kiri street beneath the "
              "repaired tower — reuse its architecture, scaffolding, wet stone and colour palette. "
              "The street is under active reconstruction and carries NO battlefield damage. Do not "
              "copy its camera angle; ignore that it is empty of people. ")

L_KIRI = "Lighting: clean pale mist-filtered daylight over a village that is still rebuilding. "
L_TSUK = ("Lighting: flat red illusion light with no visible sun, hard black shadows and a mirrored "
          "reflection rising off the black ground. ")
L_BLACK = "Lighting: a single hard key light against a field of pure black, no environment behind. "

PAGES = [
 # ---- Spread 1: measure the survivor -------------------------------------------------
 ("p01", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + KAK.format(i=3) + JIR.format(i=4)
  + KIRI_REBELS.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAS16, MAN, SAGE,
         "unnamed Kiri workers and civilians leaving a clear lane along the street")
  + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + SHAR3 + CROWD +
  "FIVE panels. His new reputation is made visible before he chooses whom to address.\n"
  "PANEL 1 (wide top band, full width): a rebuilding street near the repaired Kiri tower. Scaffolds "
  "rise at frame LEFT; workers and civilians leave a clear lane as the blond teen enters from the "
  "RIGHT and walks left. The white-haired man, the masked silver-haired man and the dark-haired "
  "teen wait as a compact group at frame LEFT, all three looking right toward him. His repaired "
  "armour, back-carried gunbai and left-hip sash sword are all visible. RESERVE a clean strip of "
  "pale mist sky across the UPPER CENTRE-LEFT of this panel: no scaffold, hair, weapon, face, "
  "effect or balloon may enter that protected space, and it carries only the chapter marker. Nobody "
  "poses for the crowd.\n"
  "PANEL 2 (tall right-middle panel): SILENT shot from behind the blond teen's shoulder — the three "
  "arrivals come into focus. The dark-haired teen is nearest the centre line and meets his gaze; "
  "the masked man stands behind him with his orange book LOWERED enough to watch over it; the "
  "white-haired man is farthest left. Workers glance between the men. No text in this panel.\n"
  "PANEL 3 (small upper-left reaction): the masked man's visible eye creases while his lowered book "
  "stays in frame; his eye-line runs right toward the blond teen.\n"
  "PANEL 4 (narrow lower-right): the white-haired man studies the blond teen's hair, armour and "
  "face rather than greeting him. The masked man is a blurred shoulder at frame left, preserving "
  "their shared eye-line.\n"
  "PANEL 5 (wide lower-left): the masked man answers without taking his eye off the blond teen, who "
  "crosses the foreground from right to left and gives neither older man a glance; the dark-haired "
  "teen remains the point he is walking toward. " + L_KIRI
  + CAP(1, "upper right", "TWO DAYS LATER.")
  + 'LETTERING: in the protected pale sky strip at the upper centre-left of PANEL 1, write the '
    'chapter marker in bold upright English capitals on one line: "CHAPTER 3 — THE OTHER UCHIHA". '
    'It is a tail-less title marker, not a balloon. '
  + SAY((3, MAN, "upper right", "SOMEONE HAS BEEN BUSY."),
        (4, SAGE, "upper right", "HE DOES LOOK A LOT LIKE HIM, DOESN'T HE, KAKASHI?"),
        (5, MAN, "upper right",
         "GIVE HIM BLACK HAIR AND THE ELDERS WOULD PROBABLY CALL FOR HIS EXECUTION."))
  + "The masked man's mouth is covered by cloth: his balloon tails point at the covered mouth. The "
    "time card and the chapter marker specified above are the only other text on this page. "
  + "In EVERY panel of this page the blond teen's visible eye is a BLOOD-RED iris with a black "
    "pupil and exactly THREE black comma-shaped tomoe — never plain black, never blue, never one "
    "or two tomoe. His hair is heavy, straight, shoulder-length blond in every panel; it is never "
    "spiky or jagged. "
  + JIR_KANJI,
  R("naruto_v4_armor_sword", "sasuke_16", "kakashi", "jiraiya", "kiri_rebel_mob",
    "env_mizukage_tower"), "high"),

 ("p02", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + KAK.format(i=3) + JIR.format(i=4)
  + MANGEKYO_EYE.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAS16, MAN, SAGE) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK +
  "FIVE panels. Mutual respect without warmth, then an observed reunion becomes a private "
  "negotiation.\n"
  "EYE STATE ON THIS PAGE: in PANELS 1-4 the blond teen's visible left eye carries the ORDINARY "
  "THREE-TOMOE SHARINGAN — a blood-red iris with a black pupil and exactly three black comma marks. "
  "ONLY IN PANEL 5 does it become the six-bladed pattern of Image 5. His eye is never blue and "
  "never plain black anywhere on this page.\n"
  "PANEL 1 (wide top band, full width): SILENT — the blond teen stops at frame RIGHT, one body "
  "length from the dark-haired teen at frame LEFT. Their shoulders are square and their eye-line is "
  "level. The masked man and the white-haired man remain BEHIND the dark-haired teen, outside the "
  "line between the two of them. No text in this panel.\n"
  "PANEL 2 (medium right): the blond teen's gaze moves once over the dark-haired teen's stance, "
  "hands and balanced weight; the dark-haired teen holds still under the assessment.\n"
  "PANEL 3 (tight medium-left reaction): SILENT — the dark-haired teen's jaw and empty right hand "
  "tighten in a competitive reflex as his eyes move over the gunbai, the left-hip sash sword and "
  "the red armour. The reaction is rivalry, not hostility; his eyes stay ordinary dark and no curse "
  "seal appears. No text in this panel.\n"
  "PANEL 4 (thin horizontal reaction strip, full width): the dark-haired teen releases his hand, "
  "locks back on the blond teen's face and gives the earned assessment; the blond teen answers with "
  "one small nod. The masked man and the white-haired man exchange a brief side glance behind "
  "them.\n"
  "PANEL 5 (dominant bottom panel, the focal panel): extreme close-up of the blond teen's eye "
  "changing from the three-tomoe Sharingan into the SIX-BLADED pattern of Image 5. The dark-haired "
  "teen's face is reflected small in the pupil, still looking directly at him. The gutters nearest "
  "this panel darken toward red-black. " + L_KIRI
  + SAY((2, BOY16, "upper right", "KAKASHI TRAINED YOU WELL."),
        (4, SAS16, "upper right", "AND YOU'VE BECOME STRONGER."),
        (5, OFF(BOY16), "upper right", "TSUKUYOMI."))
  + "The PANEL 5 balloon is small and sharp-edged. Its off-panel tail must run to the LOWER-RIGHT "
    "panel border and stop there, pointing down toward the blond teen's mouth below the eye crop. "
    "It must never touch or point at the eye itself. "
  + "On the middle tier, PANEL 2 (the blond teen speaking) is the RIGHT-hand panel and PANEL 3 "
    "(the dark-haired teen's silent reaction) is the LEFT-hand panel. In PANEL 5 the balloon's "
    "tail is a short straight spur running to the LOWER-RIGHT panel border and stopping there; it "
    "must never touch, cross or point at the eye. "
  + "The PANEL 5 tail STOPS AT the panel's lower-right border line and does not extend into the "
    "panel interior at all: no part of it may reach the eyelashes, the iris, the pupil or any "
    "pattern inside the eye. ",
  R("naruto_v4_armor_sword", "sasuke_16", "kakashi", "jiraiya", "mangekyo_design",
    "env_mizukage_tower"), "high"),

 # ---- Spread 2: family as a question -------------------------------------------------
 ("p03", dict(scene="establishing", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ONLY(BOY16, SAS16) + GEAR + SAS_LOCK + TSUKU + EMS +
  "FIVE panels. The private space is dangerous before its new use is defined.\n"
  "PANEL 1 (near-splash occupying the upper two-thirds of the page): the black reflective plane "
  "under the red sky. The dark-haired teen lands at frame LEFT in a defensive crouch, facing right. "
  "The blond teen already stands at frame RIGHT, arms at rest, gunbai on his back and sash sword at "
  "his left hip. FAR BEHIND the dark-haired teen, distorted vertical shadows only suggest the place "
  "that was once used against him — no torture, no victim, no blood and no third figure is drawn. "
  "No text in this panel.\n"
  "PANEL 2 (small lower-right inset): SILENT — the dark-haired teen's fingers tense and one foot "
  "slides back; his eye-line searches the shadows behind the blond teen rather than trusting the "
  "calm figure. No text in this panel.\n"
  "PANEL 3 (small lower-centre): the blond teen does not approach; he holds the other's gaze from "
  "across the empty plane.\n"
  "PANEL 4 (small lower-left): tight on the dark-haired teen's eyes. The tension remains, but he "
  "stops moving backward.\n"
  "PANEL 5 (narrow footer strip, full width): equal-profile two-shot with a deliberate gap between "
  "them — the blond teen at right, the dark-haired teen at left. The blond teen's posture stays "
  "open; the other's remains guarded. " + L_TSUK
  + SAY((3, BOY16, "upper right", "YOU REMEMBER THIS PLACE."),
        (4, SAS16, "upper right", "I REMEMBER."),
        (5, BOY16, "upper right", "I DIDN'T BRING YOU HERE TO HARM YOU."),
        (5, SAS16, "upper left", "I FIGURED THAT OUT.")),
  R("naruto_v4_armor_sword", "sasuke_16", "mangekyo_design"), "medium"),

 ("p04", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ONLY(BOY16, SAS16) + GEAR + SAS_LOCK + TSUKU + EMS +
  "SIX panels. The word family stops being an old claim and becomes a present test.\n"
  "PANEL 1 (medium upper-right): the blond teen in three-quarter view, still not closing the "
  "physical gap. His eye-line is direct, not nostalgic.\n"
  "PANEL 2 (medium upper-left): the dark-haired teen faces him without the earlier crouch; the red "
  "horizon cuts across behind his shoulders.\n"
  "PANEL 3 (narrow middle strip, full width): the empty black ground between their feet, with NO "
  "faces in frame. In the reflection, two small Uchiha round-and-triangle fan crests face a much "
  "larger field of darkness. They are a symbolic reflection, not an object lying on the ground, and "
  "carry no writing of any kind.\n"
  "PANEL 4 (dominant lower-right): wide two-shot — the two of them now occupy equal visual weight "
  "on opposite sides of the panel, the blond teen at RIGHT and the dark-haired teen at LEFT, both "
  "looking toward the empty centre rather than at each other.\n"
  "PANEL 5 (small lower-centre): the dark-haired teen turns his eyes back to the blond teen; the "
  "guard in his shoulders eases by one degree.\n"
  "PANEL 6 (small lower-left): the blond teen meets the look. This panel cuts closer than any "
  "previous shot of the two of them together. " + L_TSUK
  + SAY((1, BOY16, "upper right", "YOU CALLED US FAMILY ONCE."),
        (2, SAS16, "upper right", "I MEANT IT."),
        (3, OFF(BOY16), "upper right",
         "YOU AND I ARE THE UCHIHA WHO WILL GIVE THE CLAN A NEW GENERATION."),
        (4, BOY16, "upper right", "THAT REQUIRES US TO WORK TOGETHER."),
        (5, SAS16, "upper right", "THAT WAS WHY I CAME TO YOU AFTER THE EXAMS."),
        (6, BOY16, "upper right", "THEN ANSWER ME AGAIN."))
  + "In PANEL 4 the blond teen is visible at frame right: that balloon's tail runs directly to HIS "
    "mouth and must not approach the dark-haired teen at frame left. "
  + "In PANEL 1 the visible eye is a blood-red iris with one black centre ring and exactly SIX "
    "broad black blades radiating outward — never a plain red disc. He wears the segmented red "
    "pauldron on BOTH shoulders, matching the reference exactly. "
  + "In PANEL 2 the balloon reads exactly I MEANT IT. — three characters of text, with no full "
    "stop, dot, dash or any other mark before or inside the word MEANT. On the bottom tier PANEL "
    "5 is the RIGHT-hand panel and PANEL 6 the LEFT-hand panel. ",
  R("naruto_v4_armor_sword", "sasuke_16", "mangekyo_design"), "low"),

 # ---- Spread 3: recover what was taken -----------------------------------------------
 ("p05", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ONLY(BOY16, SAS16) + GEAR + SAS_LOCK + TSUKU + EMS +
  "SIX panels. The partnership is secured and immediately turned into work.\n"
  "PANEL 1 (wide top band, full width): the blond teen at frame RIGHT and the dark-haired teen at "
  "frame LEFT face each other across the reflective ground. Nothing in the setting moves.\n"
  "PANEL 2 (dominant centre panel, the focal panel): close on the dark-haired teen, level-eyed and "
  "still. No smile, no oath pose and no hesitation.\n"
  "PANEL 3 (small lower-right): the blond teen accepts the answer with one downward tilt of his "
  "chin.\n"
  "PANEL 4 (small lower-centre): the blond teen turns left and begins walking; the empty plane "
  "reshapes ahead of him into a distant INCOMPLETE outline of a clan compound gate. The dark-haired "
  "teen pivots to follow, staying ONE STEP BEHIND rather than beside him.\n"
  "PANEL 5 (medium lower-left): the outline sharpens. The blond teen gestures once toward it "
  "without looking back.\n"
  "PANEL 6 (narrow footer strip, full width): the dark-haired teen's eye-line follows that gesture "
  "to the incomplete gate. The blond teen is NOT drawn in this panel. " + L_TSUK
  + SAY((1, BOY16, "upper right", "WILL YOU WORK WITH ME?"),
        (2, SAS16, "upper right", "YES."),
        (3, BOY16, "upper right", "GOOD."),
        (4, BOY16, "upper right", "THEN BEGIN IN KONOHA."),
        (5, BOY16, "upper right", "WHEN YOU RETURN, GO TO TSUNADE OR THE COUNCIL."),
        (6, OFF(BOY16), "upper right", "DEMAND EVERYTHING CONFISCATED AFTER THE MASSACRE."))
  + "The PANEL 6 off-panel tail is a short straight spur entering from the panel's RIGHT edge and "
    "stopping there; it must not touch or aim at the dark-haired teen who is drawn in that panel. "
  + "In PANEL 1 the dark purple gunbai with its Uchiha crest and Uzumaki spiral is clearly "
    "strapped to his BACK and fully visible in profile. Draw no other object, blade, pouch or "
    "metallic shape at his hip beyond the plain straight sword in its dark sheath; every piece of "
    "his armour has a clean unbroken black outline. ",
  R("naruto_v4_armor_sword", "sasuke_16", "mangekyo_design"), "low"),

 ("p06", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ONLY(BOY16, SAS16) + GEAR + SAS_LOCK + TSUKU + EMS +
  "SIX panels. The estate is defined precisely and the compound becomes a joint project.\n"
  "PANEL 1 (medium upper-right): the dark-haired teen stops walking. The incomplete compound "
  "outline sits over his shoulder and his eyes stay on it rather than on the blond teen.\n"
  "PANEL 2 (medium upper-left): the blond teen stops one step ahead and looks back over his "
  "shoulder.\n"
  "PANEL 3 (narrow middle-right): symbolic rows of clan scrolls appear in the black reflection, "
  "their shelves broken by absence. NO people are drawn in this panel. Every scroll label is "
  "ILLEGIBLE SCRIBBLE, not readable words, and no title is invented.\n"
  "PANEL 4 (small middle-left): the dark-haired teen's hand closes at his side, controlled anger "
  "replacing surprise.\n"
  "PANEL 5 (wide lower panel, full width): the two stand on the SAME side of the frame for the "
  "first time, both facing the compound outline at frame LEFT. The dark-haired teen closes the last "
  "half-step and draws level with the blond teen; neither leads nor trails. They are newly aligned, "
  "not suddenly intimate — no embrace, no handshake and no contact.\n"
  "PANEL 6 (narrow footer close-up): the dark-haired teen turns his eyes toward the blond teen "
  "without turning his head. " + L_TSUK
  + SAY((1, SAS16, "upper right", "THE COMPOUND. THE MONEY."),
        (2, BOY16, "upper right", "ALL OF IT."),
        (3, OFF(BOY16), "upper right", "THE SCROLLS TAKEN FROM THE LIBRARY TOO."),
        (4, OFF(BOY16), "upper right", "MAKE THEM RETURN EVERYTHING."),
        (5, BOY16, "upper right", "WHEN I RETURN, WE BEGIN REBUILDING THE COMPOUND."),
        (6, SAS16, "upper right", "IF THEY REFUSE?"))
  + "The PANEL 3 off-panel tail enters from that panel's UPPER-LEFT border; the PANEL 4 off-panel "
    "tail enters from that panel's RIGHT edge. Neither may touch or aim at the dark-haired teen. "
  + "In PANEL 2 the balloon reads exactly ALL OF IT. — three words, and the word OF appears "
    "exactly once. ",
  R("naruto_v4_armor_sword", "sasuke_16", "mangekyo_design"), "low"),

 # ---- Spread 4: an unfamiliar "we" ---------------------------------------------------
 ("p07", dict(scene="emotional_closeup", light="dark", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ONLY(BOY16, SAS16) + GEAR + SAS_LOCK + TSUKU + EMS +
  "FIVE panels. Suspicion of the council survives while the two men discover a brief, dangerous "
  "ease with each other.\n"
  "PANEL 1 (medium upper-right): the blond teen turns fully back toward the dark-haired teen; the "
  "compound outline is now behind BOTH of them.\n"
  "PANEL 2 (small upper-left): SILENT — the dark-haired teen blinks once, caught by the question's "
  "obvious answer. No text in this panel.\n"
  "PANEL 3 (wide middle strip, full width): the dark-haired teen lets out one short chuckle. His "
  "posture does NOT become friendly; the release is involuntary and clearly surprises him.\n"
  "PANEL 4 (medium lower-right): he recovers, folds his arms and looks past the blond teen toward "
  "the symbolic village beyond the compound outline.\n"
  "PANEL 5 (dominant lower-left, the focal panel): the blond teen gives the dark-haired teen one "
  "small, genuine smile — the first in their relationship — while the red-black world begins to "
  "FRACTURE behind him into hard-edged shards. " + L_TSUK
  + SAY((1, BOY16, "upper right", "SINCE WHEN DO YOU ACCEPT NO?"),
        (3, SAS16, "upper right", "NEVER."),
        (4, SAS16, "upper right", "BUT THE COUNCIL CAN BE DIFFICULT."),
        (5, BOY16, "upper right", "THEN WE'LL MAKE THEM SEE REASON.")),
  R("naruto_v4_armor_sword", "sasuke_16", "mangekyo_design"), "medium"),

 ("p08", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + SASUKE16.format(i=2) + KAK.format(i=3) + JIR.format(i=4)
  + MANGEKYO_EYE.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAS16, MAN, SAGE) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + CROWD +
  "SIX panels. The illusion ends inside the same public instant and nobody learns what was said.\n"
  "EYE STATE ON THIS PAGE: in PANEL 1 the blond teen's visible left eye still carries the "
  "SIX-BLADED pattern of Image 5. From PANEL 2 onward it is the ORDINARY THREE-TOMOE SHARINGAN — a "
  "blood-red iris with a black pupil and exactly three black comma marks. It is never blue and "
  "never plain black.\n"
  "PANEL 1 (wide top band, full width): SILENT — the black-and-red illusion landscape splits into "
  "hard black shards. The blond teen and the dark-haired teen face each other through the break; "
  "the dark-haired teen's answering half-smile is the last image to vanish. No text in this panel.\n"
  "PANEL 2 (narrow upper-right): SILENT match cut to the Kiri street. NO public time has visibly "
  "passed: every figure stands exactly as in the illusion's opening. The blond teen's six-bladed "
  "pattern contracts back to the three-tomoe Sharingan; the dark-haired teen stands exactly as "
  "before. No text in this panel.\n"
  "PANEL 3 (narrow upper-left): SILENT — the white-haired man and the masked man both register the "
  "eye change. The masked man's orange book is FULLY LOWERED now. Neither of them asks anything. No "
  "text in this panel.\n"
  "PANEL 4 (wide middle band, full width): the blond teen breaks eye contact with the dark-haired "
  "teen and turns his head toward the masked man behind him. The dark-haired teen stays still, "
  "keeping the private agreement off his face.\n"
  "PANEL 5 (medium lower-right): the masked man takes one step forward, visible eye widened, his "
  "eye-line moving from the blond teen out toward the surrounding roofs.\n"
  "PANEL 6 (wide lower-left): the blond teen has already turned left and begun to walk out of the "
  "group's formation. The white-haired man steps into the lane at frame LEFT, blocking the visual "
  "exit; the dark-haired teen remains between the masked man and the two of them. " + L_KIRI
  + SAY((4, BOY16, "upper right", "BEFORE YOU LEAVE, FIND YUGAO. SHE'S SOMEWHERE IN THE VILLAGE."),
        (5, MAN, "upper right", "YUGAO IS HERE?"),
        (6, SAGE, "upper right", "WHERE ARE YOU GOING?"))
  + "In PANEL 6 the white-haired man stands at frame LEFT while the balloon sits at the upper "
    "right: draw a long clear tail crossing to HIS visible mouth at the left, passing clear of the "
    "blond teen and the dark-haired teen, whose mouths are closed in that panel. "
  + "From PANEL 2 onward the blond teen stands at reader-RIGHT facing LEFT and the dark-haired "
    "teen, masked man and white-haired man are at reader-LEFT. PANEL 2 is a tight close-up of the "
    "blond teen's eye in which the six-bladed pattern visibly contracts back into three comma "
    "tomoe. In PANEL 3 the masked man's orange book is CLOSED and held down at his side. In PANEL "
    "4 the balloon's tail runs to the BLOND TEEN'S mouth at frame right and must not point at the "
    "masked man. "
  + JIR_KANJI,
  R("naruto_v4_armor_sword", "sasuke_16", "kakashi", "jiraiya", "mangekyo_design",
    "env_mizukage_tower"), "low"),

 # ---- Spread 5: tell them you failed -------------------------------------------------
 ("p09", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KAK.format(i=3) + SASUKE16.format(i=4)
  + ENV_STREET.format(i=5)
  + ONLY(BOY16, SAGE, MAN, SAS16) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + SHAR3 + CROWD +
  "SIX panels. A less confrontational question comes first, then the exchange becomes an "
  "interrogation.\n"
  "PANEL 1 (medium upper-right): the blond teen stops but turns only his head. The white-haired man "
  "blocks the leftward exit; their opposing eye-lines cross over the dark-haired teen's shoulder in "
  "the background.\n"
  "PANEL 2 (small upper-left): the white-haired man leans forward, anger beginning to lift one "
  "hand. He draws no weapon.\n"
  "PANEL 3 (wide middle-right): the masked man speaks across the white-haired man WITHOUT touching "
  "him; his body stays angled toward the blond teen rather than taking the other man's side of the "
  "lane.\n"
  "PANEL 4 (medium middle-left): the blond teen turns enough to face the masked man. The answer is "
  "neutral, not defiant.\n"
  "PANEL 5 (medium lower-right): the white-haired man pushes back into the exchange, now square to "
  "the blond teen.\n"
  "PANEL 6 (wide lower-left): the blond teen's eyes narrow. The masked man watches the tactic fail; "
  "the dark-haired teen looks aside, already knowing the answer will not be given. " + L_KIRI
  + SAY((1, BOY16, "upper right", "WHERE I WISH."),
        (2, SAGE, "upper right", "NARU—"),
        (3, MAN, "upper right", "AREN'T YOU COMING BACK TO KONOHA WITH US?"),
        (4, BOY16, "upper right", "NO."),
        (5, SAGE, "upper right", "WHAT BUSINESS?"),
        (6, BOY16, "upper right", "YOU'RE INTERROGATING ME, JIRAIYA. I DON'T LIKE IT."))
  + "Do not stack two panels in one column beside a tall panel. Lay the middle out as three equal "
    "tiers or as PANEL 3 right / PANEL 4 left on one tier and PANEL 5 as a band beneath, so the "
    "reading runs 3, 4, 5 in strict right-to-left, top-to-bottom order. "
  + KAK_BOOK,
  R("naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16", "env_mizukage_tower"), "low"),

 ("p10", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KAK.format(i=3) + SASUKE16.format(i=4)
  + YUGAO_V4.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAGE, MAN, SAS16, YUG) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + YUG_LOCK
  + SHAR3 + CROWD +
  "SIX panels. Loyalty is separated from obedience, then the escalation is interrupted.\n"
  "PANEL 1 (tall upper-right): the white-haired man steps closer and fills the foreground, forcing "
  "the blond teen smaller at frame LEFT without actually moving him.\n"
  "PANEL 2 (medium upper-left): the white-haired man points back in Konoha's direction. The masked "
  "man's eye shifts to that hand; the dark-haired teen's stays on the blond teen.\n"
  "PANEL 3 (narrow middle strip, full width): close on the blond teen's LEAF FOREHEAD PROTECTOR "
  "beneath his long hair, cropped above his mouth. The metal catches the Kiri daylight; it is "
  "neither removed nor concealed. Its engraved leaf symbol is the only marking and carries no "
  "words.\n"
  "PANEL 4 (medium lower-right): the blond teen looks directly at the white-haired man again. He "
  "does NOT reach for a weapon and does not raise his voice.\n"
  "PANEL 5 (dominant lower-centre, the focal panel): the blond teen turns LEFT around the "
  "white-haired man, keeping the forehead protector clearly visible in profile. The older man's "
  "planted stance has failed to stop the movement.\n"
  "PANEL 6 (inset breaking the lower-left border): SILENT — the purple-haired kunoichi drops from "
  "the upper-right roofline into the centre of the group's axis. Her landing turns every head "
  "toward her and visually cuts the line between the blond teen and the white-haired man. SHE "
  "CARRIES NO SWORD. No text in this panel. " + L_KIRI
  + SAY((1, SAGE, "upper right", "LISTEN, BRAT."),
        (2, SAGE, "upper right", "TSUNADE AND THE ELDERS ORDERED ME TO BRING YOU BACK."),
        (3, OFF(BOY16), "upper right", "THIS SHOULD BE ENOUGH TO TELL YOU I'M STILL ONE OF YOU."),
        (4, BOY16, "upper right", "YOUR ORDERS DO NOT MATTER TO ME."),
        (5, BOY16, "upper right", "TELL THEM YOU FAILED."))
  + "The PANEL 3 off-panel tail exits the LOWER-RIGHT panel border and stops there, pointing down "
    "toward the blond teen's mouth below the forehead-protector crop. "
  + "The purple-haired kunoichi appears in PANEL 6 ONLY, dropping from the upper-right roofline. "
    "She must NOT be drawn, even partly or in the background, in PANELS 1, 2, 3, 4 or 5; in those "
    "panels the only people are the blond teen, the big white-haired man, the masked "
    "silver-haired man and the dark-haired teen. ",
  R("naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16", "yugao_v4",
    "env_mizukage_tower"), "low"),

 # ---- Spread 6: a witness against force ----------------------------------------------
 ("p11", dict(scene="emotional_closeup", light="day", cast="crowd", mood="calm", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + YUGAO_V4.format(i=2) + KAK.format(i=3) + JIR.format(i=4)
  + SASUKE16.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, YUG, MAN, SAGE, SAS16) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + YUG_LOCK
  + SHAR3 + CROWD +
  "SEVEN panels. The reunion is paid off and the witness is placed INSIDE the dispute.\n"
  "PANEL 1 (medium upper-right): the purple-haired kunoichi straightens from her landing at centre. "
  "Her serious face changes the instant she sees the masked man at frame LEFT.\n"
  "PANEL 2 (small upper-centre): the masked man takes one surprised step toward her, his orange "
  "book forgotten at his side.\n"
  "PANEL 3 (dominant panel filling the upper-left and middle of the page, the focal panel): SILENT "
  "— she crosses left and HUGS the masked man; he returns the embrace with ONE arm and his visible "
  "eye closes in relief. The blond teen remains at FAR RIGHT, watching without interrupting; the "
  "white-haired man's anger is suspended, not gone. No text in this panel.\n"
  "PANEL 4 (small lower-right): they separate. The masked man keeps both hands lightly on her "
  "shoulders to verify she is unhurt.\n"
  "PANEL 5 (small lower-centre): she gives him an apologetic look and glances once toward the blond "
  "teen.\n"
  "PANEL 6 (medium lower-left): the white-haired man takes in her recovered, unarmed condition. His "
  "manner is official rather than welcoming.\n"
  "PANEL 7 (narrow footer strip, full width): she turns from the masked man toward the white-haired "
  "man but keeps the blond teen in the far background of her eye-line. " + L_KIRI
  + SAY((1, YUG, "upper right", "SENPAI."),
        (2, MAN, "upper right", "YUGAO."),
        (4, MAN, "upper right", "WHAT ARE YOU DOING HERE?"),
        (5, YUG, "upper right", "LONG STORY."),
        (6, SAGE, "upper right", "UZUKI YUGAO. YOU'VE BEEN MISSING FOR A MONTH."),
        (7, YUG, "upper right", "I'LL EXPLAIN LATER."))
  + "Place PANEL 3, the embrace, as a wide band directly BELOW panels 1 and 2, with PANEL 4 "
    "beginning the next tier at the right. The embrace must be read before panel 4, never after "
    "it. "
  + "On the tier that carries PANELS 4, 5 and 6, PANEL 4 (the balloon reading WHAT ARE YOU DOING "
    "HERE?) is the RIGHT-hand panel of that tier, PANEL 5 (LONG STORY.) is the CENTRE panel and "
    "PANEL 6 (UZUKI YUGAO. YOU'VE BEEN MISSING FOR A MONTH.) is the LEFT-hand panel; never the "
    "reverse. ",
  R("naruto_v4_armor_sword", "yugao_v4", "kakashi", "jiraiya", "sasuke_16",
    "env_mizukage_tower"), "medium"),

 ("p12", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + YUGAO_V4.format(i=2) + JIR.format(i=3) + KAK.format(i=4)
  + ENV_STREET.format(i=5)
  + ONLY(BOY16, YUG, SAGE, MAN) + GEAR + KAK_LOCK + JIR_LOCK + YUG_LOCK + SHAR3 + CROWD +
  "SEVEN panels. She names the failed tactic and then contradicts a Sannin in front of everyone.\n"
  "PANEL 1 (wide top band, full width): the purple-haired kunoichi looks from the white-haired man "
  "at frame LEFT to the blond teen at frame RIGHT. The blond teen has stopped leaving but has not "
  "rejoined the group.\n"
  "PANEL 2 (small upper-left): the white-haired man folds his arms, reclaiming the conversation.\n"
  "PANEL 3 (medium middle-right): she faces him fully. The masked man watches from behind her; the "
  "blond teen is visible over her opposite shoulder.\n"
  "PANEL 4 (medium middle-left): the white-haired man looms larger in frame and thumbs his own "
  "chest. His movement points the next eye path DOWN toward her, not toward the blond teen.\n"
  "PANEL 5 (narrow lower-right): her eyes flick to the blond teen's gunbai and back to the "
  "white-haired man. She does not smile or soften.\n"
  "PANEL 6 (wide lower-centre): she holds the white-haired man's eye-line. The blond teen is small "
  "but perfectly still in the background, making her warning read as evidence rather than "
  "flattery.\n"
  "PANEL 7 (narrow footer close-up): the white-haired man's expression loses its bluster. The "
  "purple-haired kunoichi is NOT drawn in this panel. " + L_KIRI
  + SAY((1, YUG, "upper right", "YOU'RE TRYING TO MAKE HIM RETURN TO KONOHA."),
        (2, SAGE, "upper right", "THAT'S THE IDEA."),
        (3, YUG, "upper right", "DON'T BOTHER. HE WON'T BUDGE."),
        (4, SAGE, "upper right", "I'M A SANNIN."),
        (4, SAGE, "lower right", "I'LL TAKE HIM BY FORCE IF I HAVE TO."),
        (5, YUG, "upper right", "WITH ALL DUE RESPECT, JIRAIYA-SAMA—"),
        (6, YUG, "upper right", "THAT TITLE MEANS NOTHING TO HIM."),
        (7, OFF(YUG), "upper right", "AND YOU CANNOT FORCE HIM."))
  + "Both PANEL 4 balloons belong to the white-haired man and both tails run to HIS mouth. The "
    "PANEL 7 off-panel tail enters from that panel's RIGHT edge and stops there; it must not touch "
    "or aim at the white-haired man's face, which fills that panel. "
  + "Strict right-to-left ordering on every tier: PANEL 2 occupies the RIGHT of its tier and "
    "PANEL 3 the LEFT; PANEL 4 occupies the RIGHT of its tier and PANEL 5 the LEFT. The "
    "lower-numbered panel is always the right-hand panel of its tier. ",
  R("naruto_v4_armor_sword", "yugao_v4", "jiraiya", "kakashi", "env_mizukage_tower"), "low"),

 # ---- Spread 7: change the question --------------------------------------------------
 ("p13", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + YUGAO_V4.format(i=2) + JIR.format(i=3) + KAK.format(i=4)
  + SASUKE16.format(i=5) + SUSA_FINAL.format(i=6) + ENV_STREET.format(i=7)
  + ONLY(BOY16, YUG, SAGE, MAN, SAS16,
         "the huge orange armoured warrior form appearing ONLY inside the hard-edged remembered "
         "background fragment of PANEL 3, never in the present-day street")
  + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + YUG_LOCK + SHAR3 + CROWD +
  "SIX panels. Her claim is grounded in witnessed power and learned behaviour.\n"
  "PANEL 1 (medium upper-right): the white-haired man looks past the purple-haired kunoichi to the "
  "blond teen and back, testing whether her certainty is fear, loyalty or judgement.\n"
  "PANEL 2 (small upper-left): the masked man's visible eye fixes on her. The question is quiet, "
  "not a challenge.\n"
  "PANEL 3 (middle tier, RIGHT — it occupies roughly the right half of the tier and is NOT "
  "full-width; PANEL 4 sits beside it on the SAME tier at the LEFT, and the two of them "
  "together fill that tier): her memory appears as a HARD-EDGED, desaturated BACKGROUND FRAGMENT "
  "behind her — the huge orange armoured warrior form towering over a ruined battlefield with a "
  "tiny blond figure standing inside it. That form is drawn as FLAT OPAQUE shapes with hard "
  "outlines; it does NOT glow and does NOT wash out the panel, and the present-day street stays "
  "legible around it. The present-day kunoichi remains foregrounded and looks at the masked man, "
  "NOT at the memory.\n"
  "PANEL 4 (middle tier, LEFT — directly beside PANEL 3 on the same tier, read after it): the "
  "present-day blond teen in profile, impassive under the "
  "attention. The kunoichi and the masked man are BLURRED on opposite sides behind him.\n"
  "PANEL 5 (LOWER tier, RIGHT — a new tier below panels 3 and 4, read first on that tier): she faces the whole group now. The dark-haired teen watches her "
  "with a neutral, assessing expression; the white-haired man no longer crowds the frame.\n"
  "PANEL 6 (LOWER tier, LEFT — beside PANEL 5, read after it): she turns specifically to the masked man. He is at frame LEFT and the "
  "blond teen remains at frame RIGHT beyond them, creating a line through two people who knew him "
  "at different ages. " + L_KIRI
  + SAY((1, SAGE, "upper right", "YOU SOUND VERY CERTAIN."),
        (2, MAN, "upper right", "HOW DO YOU KNOW?"),
        (3, YUG, "upper right", "I SAW HIM FIGHT IN THE CIVIL WAR."),
        (4, OFF(YUG), "upper right", "I'VE ALSO SPENT A MONTH WITH HIM."),
        (5, YUG, "upper right", "NO ONE MAKES HIM DO WHAT HE DOESN'T WANT."),
        (6, YUG, "upper right", "YOU SPENT TIME WITH HIM AS A GENIN. YOU KNOW THAT."))
  + "The PANEL 4 off-panel tail enters from that panel's LEFT edge and stops there; it must not "
    "touch or aim at the blond teen's face, which fills that panel. "
  + "PANEL 4 occupies the RIGHT of its tier and PANEL 5 the LEFT. In PANEL 3 the orange armoured "
    "warrior sits inside a hard ragged-edged remembered inset, flat and desaturated, clearly "
    "separated from the present-day foreground; it is a memory image only and must never look "
    "present in the Kiri street. "
  + "On the tier that carries PANELS 4 and 5, the panel whose balloon reads I'VE ALSO SPENT A "
    "MONTH WITH HIM. is the RIGHT-hand panel of that tier and the panel whose balloon reads NO "
    "ONE MAKES HIM DO WHAT HE DOESN'T WANT. is the LEFT-hand panel — never the reverse. "
  + KAK_BOOK
  + JIR_KANJI,
  R("naruto_v4_armor_sword", "yugao_v4", "jiraiya", "kakashi", "sasuke_16",
    "susanoo_orange_final", "env_mizukage_tower"), "medium"),

 ("p14", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KAK.format(i=3) + SASUKE16.format(i=4)
  + YUGAO_V4.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAGE, MAN, SAS16, YUG) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + YUG_LOCK
  + SHAR3 + CROWD +
  "SIX panels. The return argument ends and the question changes from control to information.\n"
  "PANEL 1 (medium upper-right): the masked man closes his orange book with one hand. His visible "
  "eye is sober and he looks at the WHITE-HAIRED MAN rather than at the kunoichi.\n"
  "PANEL 2 (small upper-left): SILENT — the dark-haired teen shifts his weight toward the path back "
  "to Konoha but keeps watching the white-haired man. He does not expose the private agreement. No "
  "text in this panel.\n"
  "PANEL 3 (wide middle band, full width): SILENT — the white-haired man and the blond teen face "
  "each other again across the space the kunoichi opened. The older man's arms drop; the blond teen "
  "has not moved. No text in this panel.\n"
  "PANEL 4 (small lower-right): the white-haired man exhales through his nose and gives up the "
  "order for now.\n"
  "PANEL 5 (medium lower-centre): his expression hardens into something more serious. He steps "
  "sideways OUT of the blond teen's exit path but keeps his eye-line locked on him.\n"
  "PANEL 6 (dominant lower-left): tight two-shot with the white-haired man in the foreground at "
  "LEFT and the blond teen in the background at RIGHT. The masked man, the dark-haired teen and the "
  "kunoichi fall OUTSIDE this crop and are not drawn in it. The open path behind the blond teen is "
  "visible but no longer the subject. " + L_KIRI
  + SAY((1, MAN, "upper right", "SHE'S RIGHT."),
        (4, SAGE, "upper right", "FINE."),
        (5, SAGE, "upper right", "THEN ANSWER SOMETHING ELSE."),
        (6, SAGE, "upper right", "WHAT IS THIS I HEARD ABOUT THE NINE-TAILS?"))
  + "In PANEL 6 the balloon sits at the upper right while the white-haired man occupies the "
    "foreground at the LEFT: draw a firm tail crossing to HIS mouth, clear of the blond teen behind "
    "him, whose mouth is closed in that panel. "
  + "Lay the lower half of the page out as: PANEL 4 (small) at the upper RIGHT, PANEL 5 (medium) "
    "directly to its LEFT on the same tier, and PANEL 6 as one dominant full-width band BELOW "
    "them both. Panel 6 must never sit to the right of panels 4 and 5. In PANEL 1 he is CLOSING "
    "the orange book with one hand — the covers are shut, not open and not being read. "
  + JIR_KANJI,
  R("naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16", "yugao_v4",
    "env_mizukage_tower"), "low"),

 # ---- Spread 8: no public answer -----------------------------------------------------
 ("p15", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + SASUKE16.format(i=3) + KAK.format(i=4)
  + YUGAO_V4.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(BOY16, SAGE, SAS16, MAN, YUG) + GEAR + SAS_LOCK + KAK_LOCK + JIR_LOCK + YUG_LOCK
  + SHAR3 + CROWD +
  "FIVE panels. The whole group understands that the subject has changed, and nobody learns how.\n"
  "PANEL 1 (medium upper-right): the blond teen raises one eyebrow. His body stays angled toward "
  "the open path; only his eyes return to the white-haired man.\n"
  "PANEL 2 (medium upper-left): the white-haired man's hand closes at his side. He reads the "
  "question as evasion.\n"
  "PANEL 3 (narrow middle-right): SILENT — the dark-haired teen looks from the white-haired man to "
  "the blond teen. The private clan ease has vanished behind a guarded public face. No text in this "
  "panel.\n"
  "PANEL 4 (narrow middle-left): SILENT — the masked man's visible eye narrows; the kunoichi "
  "watches the blond teen rather than the white-haired man. Neither of them speaks for him. No text "
  "in this panel.\n"
  "PANEL 5 (wide lower panel, full width): the white-haired man occupies frame LEFT and the blond "
  "teen frame RIGHT, with the other three staggered between them in depth. The rebuilding village "
  "continues behind the frozen group, indifferent to the secret at the centre. " + L_KIRI
  + SAY((1, BOY16, "upper right", "WHAT ABOUT IT?"),
        (2, SAGE, "upper right", "DON'T PLAY STUPID WITH ME."),
        (5, SAGE, "upper right", "YOU KNOW EXACTLY WHAT I'M ASKING."))
  + "In PANEL 5 the white-haired man stands at the LEFT: draw a long clear tail from the upper "
    "right balloon to HIS mouth, passing clear of the three figures staggered between them. "
  + "On the top tier PANEL 1 (the blond teen, WHAT ABOUT IT?) is the RIGHT-hand panel and PANEL 2 "
    "(the white-haired man, DON'T PLAY STUPID WITH ME.) is the LEFT-hand panel. "
  + KAK_BOOK
  + JIR_KANJI,
  R("naruto_v4_armor_sword", "jiraiya", "sasuke_16", "kakashi", "yugao_v4",
    "env_mizukage_tower"), "low"),

 ("p16", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=4),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KURAMA_FULL.format(i=3)
  + ONLY(BOY16, SAGE,
         "the enormous nine-tailed fox appearing ONLY as a faint non-diegetic outline of nine tails "
         "in the empty black negative space of PANEL 4 — no character sees it, it is not physically "
         "present in the street, and no part of its body or face is drawn")
  + GEAR + JIR_LOCK + SHAR3 +
  "FOUR panels. LAST PAGE OF THE CHAPTER — it ends on withheld information, not an answer. The "
  "backgrounds fall away to flat black across the page; no Kiri architecture, crowd or scaffold "
  "appears in any panel.\n"
  "PANEL 1 (wide top band, full width): SILENT profile two-shot — the white-haired man at frame "
  "LEFT leans slightly forward; the blond teen at frame RIGHT stands straight. Their eye-line is "
  "level. The other three characters are REMOVED from the composition entirely. No text in this "
  "panel.\n"
  "PANEL 2 (small middle-right): SILENT close on the white-haired man's eyes. Concern and suspicion "
  "have replaced his earlier anger. No text in this panel.\n"
  "PANEL 3 (small middle-left): SILENT close on the blond teen's face. His Sharingan is the "
  "ordinary three-tomoe pattern, his mouth is still, and no hand moves toward his stomach. The "
  "background falls to pure black. No text in this panel.\n"
  "PANEL 4 (dominant bottom panel, the focal panel): the blond teen stands in clean SILHOUETTE at "
  "frame RIGHT against a black field. A faint, thin, non-diegetic OUTLINE of nine tails fills the "
  "negative space behind him — drawn as flat line only, not glowing, not solid and not seen by "
  "anyone in the scene. The white-haired man is cropped at frame LEFT with only his jaw and "
  "shoulder visible. " + L_BLACK
  + SAY((4, SAGE, "upper right", "WELL?"))
  + "The PANEL 4 balloon begins above the cropped white-haired man at the LEFT edge and its tail "
    "runs to his cropped mouth there, forcing the reader's eye across the empty space toward the "
    "blond teen's silence at the right. ",
  R("naruto_v4_armor_sword", "jiraiya", "kurama_full"), "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch03" / "raw", HERE / "v5ch03" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
