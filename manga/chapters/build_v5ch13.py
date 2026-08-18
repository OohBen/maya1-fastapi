"""Volume 5, Chapter 13 — "The Police Force". 22 pages. VOLUME FINALE.

Translated 1:1 from story/volume_05/drafts/ch13_the_police_force.md — every balloon, thought,
card and sound effect, with its panel, speaker, stated position and exact text. Reading order
is RIGHT TO LEFT on every page. Source: fic ch16:309-683.

Pages 1-12 continue Chapter 12's council master on the same breath: the map does not reset and
is never mirrored. Every document, statute, ledger, agenda, map and menu carries ILLEGIBLE
SCRIBBLE only.

MISSING REFERENCE SHEETS (report, never invent):
  * onoki.png — the Tsuchikage on page 16. He is described in prose as an unnamed, very short
    elderly village leader; add the sheet and bind him before generating page 16.
  * env_iwa_tsuchikage_office.png — page 16 binds env_hokage_office for the desk-and-window
    layout only and states Iwa's rough stone interior in prose.
  * env_lunch_shop.png — pages 17-22 bind env_ichiraku for the small-eatery palette only; the
    triangular three-seat table is stated in prose.
  * tobirama.png — page 5's borderless historical image. The founder figure is drawn from
    behind with his face not shown until a sheet exists.
  * no ANBU mask sheet exists; the Iwa scouts on pages 15-16 stay anonymous and are never
    unmasked, following the Root-agent precedent in build_v5ch01.py.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import (ANK, COAT, DAN, ENV, FILL, HAWK, KAB, KAK, OFF, ONLY, R, SAY,  # noqa: E402
                     SFX, SPEC)
from prompts_v4 import (HIASHI, HOMURA, KARIN, KOHARU, N16_BLACK,                 # noqa: E402
                        SASUKE16, SHIKAKU, TSUME, TSUNADE, YUGAO_V4,
                        HIASHI_SPEAKER, HOMURA_SPEAKER, KARIN_SPEAKER, KOHARU_SPEAKER,
                        N16_SPEAKER, SASUKE16_SPEAKER, SHIKAKU_SPEAKER, TSUME_SPEAKER,
                        TSUNADE_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
KURENAI = ("Image {i} is the CHARACTER REFERENCE for the red-eyed woman: late twenties, long wavy "
           "black hair, striking red eyes, a one-piece dress resembling white bandage wrapping "
           "with a single red right sleeve. Reproduce exactly; ignore its white background and "
           "layout. ")
BOY16 = N16_SPEAKER
SAS16 = SASUKE16_SPEAKER
TSU = TSUNADE_SPEAKER
KOH = KOHARU_SPEAKER
HOM = HOMURA_SPEAKER
SHIK = SHIKAKU_SPEAKER
HIA = HIASHI_SPEAKER
TSUM = TSUME_SPEAKER
YUG = YUGAO_V4_SPEAKER
KUR = "the red-eyed woman with long wavy black hair"
ANKO = COAT
KAR = KARIN_SPEAKER
OLDKAGE = "the very short elderly village leader behind the desk"
IWA_CAP = "the kneeling masked Iwa scout captain"
IWA_SCOUT = "the masked Iwa scout beside the covered body"
IWA_MEDIC = "the kneeling masked Iwa medic"
ATTEND = ("other seated clan heads on the east arc, plus faceless attendants and two masked door "
          "guards outside the seating oval, none of them individually recognisable and none of "
          "them ever speaking")
MAP = ("THE CHAMBER MAP IS UNCHANGED FROM THE PREVIOUS CHAPTER AND IS NEVER MIRRORED: ONE "
       "CONTINUOUS OVAL TABLE; the blonde woman in the green haori alone at the NORTH head facing "
       "south-southeast; the three elderly advisers on the WEST arc at reader-LEFT looking "
       "screen-right; the clan heads on the EAST arc at reader-RIGHT looking screen-left; the "
       "carved Uchiha chair at the near SOUTHEAST end where the blond teen sits facing north-west; "
       "the dark-haired teen one pace behind his right shoulder, stepping around that same right "
       "side to the outer rim when he speaks and retracing the path afterwards. Nobody enters the "
       "interior of the oval and no document ever crosses it. ")
DOCS = ("Every agenda, statute copy, ledger, note, map and menu on this page carries ILLEGIBLE "
        "SCRIBBLE, not readable words. ")
BLACKFIT = ("The blond teen wears the fitted long-sleeved black shirt carrying BOTH the Uchiha fan "
            "crest and the Uzumaki spiral on its back, black trousers and black gloves — no "
            "armour, no forehead protector, no gunbai and no visible sign of illness. ")
EYES_N = ("His visible left eye holds the ORDINARY three-tomoe Sharingan: never a Mangekyō "
          "pattern, never a technique, never a glow. ")
L_CHAMBER = ("Lighting: cool even daylight from high slit windows onto pale stone and dark wood, "
             "hard ink shadows under the table, no glow anywhere. ")
L_HOUSE = "Lighting: flat clean midday light across a low wooden table in a quiet Uchiha interior. "
L_CAVE = "Lighting: cold grey daylight down a rocky cut, then black stone lit by hard hand-lamps. "
L_IWA = "Lighting: hard low west light through a rock-cut window across a stone office. "
L_SHOP = ("Lighting: warm afternoon light through a small eatery's noren and street opening. "
          # The first pass let this closing scene drift soft and pencil-sketchy while the council
          # act stayed crisp; the volume must not change hands on its last six pages.
          "RENDERING IS IDENTICAL TO THE REST OF THE CHAPTER: flat cel colour with two to three "
          "hard-edged tonal values per material and clean confident black brush linework at full "
          "weight. The street and shop interior behind the figures are INKED, not sketched — no "
          "pencil texture, no scratchy construction lines, no washed-out or faded mid-tones, no "
          "soft gradients, and no lighter line weight than the council chamber pages. ")

PAGES = [
 # ---- Spread 1: a watcher in the team ----------------------------------------------
 ("p01", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + DAN.format(i=4) + SHIKAKU.format(i=5) + TSUME.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, TSU, HAWK, SHIK, TSUM,
         "the two other elderly advisers on the west arc, seen in lost profile and never "
         "individually recognisable", ATTEND)
  + MAP + DOCS + BLACKFIT + EYES_N +
  "FIVE panels. The meeting continues on the SAME BREATH as the previous chapter's last panel — "
  "no time card, no location reset, no folder movement.\n"
  "PANEL 1 (top strip, full width): exact continuation of the previous master — the blonde woman "
  "north, advisers west at reader-left, clan heads east at reader-right, the blond teen at the "
  "southeast place facing north-west, the dark-haired teen behind his right shoulder. The bandaged "
  "old man answers without a pause and touches no document. The UPPER CENTRE of this panel is "
  "PROTECTED EMPTY NEGATIVE SPACE carrying only the chapter marker — no figure, object or balloon "
  "may enter it.\n"
  "PANEL 2 (middle right): the bandaged old man folds his hands on the west arc and looks "
  "screen-right toward the Uchiha place.\n"
  "PANEL 3 (middle left): the bandaged old man foreground left; the two Uchiha stay across the "
  "continuous oval in deep focus.\n"
  "PANEL 4 (lower right, narrow reaction panel): the man with the long pineapple ponytail rests "
  "his chin on clasped hands from the east arc.\n"
  "PANEL 5 (bottom left, dominant): the wild-haired clan head with the red cheek markings sits at "
  "the near end of the east arc and looks north toward the table head; the clear central tabletop "
  "keeps the two factions legible and the blonde woman answers from the far north head. "
  + L_CHAMBER +
  'LETTERING: in the protected upper-centre negative space of PANEL 1, write the chapter marker in '
  'bold upright English capitals on one line: "CHAPTER 13 — THE POLICE FORCE". It is a tail-less '
  'title, not a balloon. '
  + SAY((1, HAWK, "upper right", "THEN LET US DISCUSS HOW THEIR STRENGTH SERVES THE VILLAGE."),
        (2, HAWK, "upper right", "NARUTO. SASUKE. ONE ROOT OPERATIVE."),
        (3, HAWK, "upper right", "A TEAM TO SURPASS THE SANNIN."),
        (4, SHIK, "upper right", "THE TWO UCHIHA ALONE WOULD ALREADY BE FORMIDABLE."),
        (5, TSUM, "upper right", "THEY WERE TEAMMATES ONCE."),
        (5, TSU, "upper left", "THEY WERE. THEY ARE NOT THE PROBLEM IN HIS PROPOSAL."))
  + "The wild-haired clan head with the red fang markings is a FIERCE MIDDLE-AGED WOMAN and must never be drawn as a man: no beard, no moustache, no goatee, no stubble, a female jaw and throat line, and a red fang marking on BOTH cheeks. ",
  R("naruto_v4_black", "sasuke_16", "tsunade", "danzo", "shikaku", "tsume",
    "env_konoha_council_chamber"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + DAN.format(i=4) + KOHARU.format(i=5) + KAK.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, TSU, HAWK, KOH,
         "the masked silver-haired man appearing ONLY inside one small borderless memory inset in "
         "PANEL 6, never physically present in the chamber", ATTEND)
  + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. Root is exposed as surveillance and replaced with an elite team under the Hokage.\n"
  "PANEL 1 (top right): the blonde woman leans forward, eye-line down-left along the west arc.\n"
  "PANEL 2 (top left): the bandaged old man's visible eye does not move.\n"
  "PANEL 3 (middle band, full width): diagonal two-shot across the table — the blond teen near "
  "right in the foreground, the bandaged old man far left in the background, clear negative space "
  "between them.\n"
  "PANEL 4 (lower right, the focal panel): close on the blond teen, perfectly calm; the "
  "dark-haired teen's hand is visible behind the chair and still.\n"
  "PANEL 5 (lower left, upper): SILENT — the bandaged old man understands; the elderly female "
  "adviser turns toward him. No text in this panel.\n"
  "PANEL 6 (bottom band, full width): the blonde woman cuts across the table with one raised hand. "
  "The masked silver-haired man appears ONLY as a small BORDERLESS memory inset behind the two "
  "Uchiha, desaturated and hard-edged; he is never in the room. The dark-haired teen answers from "
  "the background with his mouth visible. " + L_CHAMBER
  + SAY((1, TSU, "upper right", "YOU HAVE SOMEONE WHO CAN KEEP UP WITH THEM?"),
        (2, HAWK, "upper right", "ROOT."),
        (3, BOY16, "upper right", "A WATCHER."),
        (3, HAWK, "upper left", "A TEAMMATE."),
        (4, BOY16, "upper right", "THEN CHOOSE SOMEONE YOU CAN AFFORD TO LOSE."),
        (4, BOY16, "upper left", "I BECOME CARELESS WHEN A FIGHT INTERESTS ME."),
        (6, TSU, "upper right", "NO ROOT."),
        (6, TSU, "upper centre", "KAKASHI JOINS THEM FOR MISSIONS ORDINARY TEAMS CANNOT TAKE."),
        (6, SAS16, "upper left", "NO OBJECTION.")),
  R("naruto_v4_black", "sasuke_16", "tsunade", "danzo", "koharu", "kakashi",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 2: Sasuke's proposal --------------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + KOHARU.format(i=4) + TSUME.format(i=5) + HIASHI.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, TSU, KOH, TSUM, HIA, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "FIVE panels. The proposal belongs to the dark-haired teen alone.\n"
  "PANEL 1 (top strip, full width): the blonde woman looks around the oval from the north head.\n"
  "PANEL 2 (tall right, the focal panel): the dark-haired teen steps around the blond teen's RIGHT "
  "side to the outer southeast rim beside the chair; he never crosses him and never enters the "
  "table's interior. The blond teen stays seated and does not prompt him.\n"
  "PANEL 3 (upper left): the elderly female adviser jerks toward him from the west arc.\n"
  "PANEL 4 (middle left): the wild-haired clan head with the red cheek markings, seen from the "
  "east arc, does not share the shock.\n"
  "PANEL 5 (bottom left): the stern long-haired clan head's fingers touch the table once. "
  + L_CHAMBER
  + SAY((1, TSU, "upper right", "THE ELITE TEAM IS APPROVED."),
        (1, TSU, "upper left", "IS THERE ANYTHING ELSE?"),
        (2, SAS16, "upper right", "YES."),
        (2, SAS16, "upper left", "I PROPOSE THAT KONOHA RESTORE THE MILITARY POLICE FORCE."),
        (3, KOH, "upper right", "ABSOLUTELY NOT."),
        (4, TSUM, "upper right", "IT KEPT ORDER. EFFECTIVELY."),
        (5, HIA, "upper right", "AND IT BARRED EVERY CLAN BUT THE UCHIHA."))
  + "The wild-haired clan head with the red fang markings is a FIERCE MIDDLE-AGED WOMAN and must never be drawn as a man: no beard, no moustache, no goatee, no stubble, a female jaw and throat line, and a red fang marking on BOTH cheeks. In EVERY panel where the blond teen's face is visible, including the PANEL 2 profile, his visible left eye is the RED ordinary three-tomoe Sharingan, never a dark, brown or blue eye. ",
  R("naruto_v4_black", "sasuke_16", "tsunade", "koharu", "tsume", "hiashi",
    "env_konoha_council_chamber"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + HOMURA.format(i=3)
  + KOHARU.format(i=4) + DAN.format(i=5) + ENV.format(i=6)
  + ONLY(BOY16, SAS16, HOM, KOH, HAWK, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. The opposition is forced to name an actual institutional harm.\n"
  "PANEL 1 (top right): the male adviser faces screen-right from the west arc.\n"
  "PANEL 2 (top centre): the dark-haired teen stands in the same outer-rim aisle, shoulders "
  "square.\n"
  "PANEL 3 (top left): the elderly female adviser answers for the adviser block.\n"
  "PANEL 4 (middle band, full width): the blond teen finally turns his chair a few degrees toward "
  "the west arc — a movement small enough to command the room.\n"
  "PANEL 5 (bottom right): SILENT tight three-shot of the bandaged old man and the two elderly "
  "advisers; none of them answers and the old man's eye stays on the Uchiha place. No text in this "
  "panel.\n"
  "PANEL 6 (bottom left): the dark-haired teen watches their silence rather than the blond teen. "
  + L_CHAMBER
  + SAY((1, HOM, "upper right", "WE WILL NOT REVIVE IT."),
        (2, SAS16, "upper right", "WHY?"),
        (3, KOH, "upper right", "THE OLD FORCE BECAME AN UCHIHA POWER BASE."),
        (4, BOY16, "upper right", "NAME THE POWER IT TOOK."),
        (4, BOY16, "upper left", "NAME THE PROBLEM IT CAUSED."),
        (6, SAS16, "upper right", "YOU CANNOT."))
  + "In PANEL 4 the blond teen's visible left eye is the RED ordinary three-tomoe Sharingan, clearly readable at this framing and never drawn dark, brown or blue. ",
  R("naruto_v4_black", "sasuke_16", "homura", "koharu", "danzo",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 3: visible power ------------------------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + DAN.format(i=3)
  + ENV.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, SAS16, HAWK,
         "in PANEL 1 only, a white-haired armoured founder-era figure seen FROM BEHIND with his "
         "face never shown, and in PANEL 5 only, generic historical police officers and hooded "
         "underground agents, none of them named, recurring or individually recognisable", ATTEND)
  + MAP + DOCS + BLACKFIT + EYES_N +
  "FIVE panels. Image 4 is the council chamber; image 5 supplies the sunlit Konoha street used "
  "ONLY inside the historical image.\n"
  "PANEL 1 (top band, full width): BORDERLESS historical image, desaturated — the founder-era "
  "figure stands with his back to the reader before an older Uchiha police crest, the clan behind "
  "him visually directed AWAY from the distant leader's tower. No readable document text and no "
  "dialogue inside the historical image itself.\n"
  "PANEL 2 (middle right): back in the chamber, the dark-haired teen faces the east-arc clan "
  "heads from the outer rim.\n"
  "PANEL 3 (middle left): his hand settles on the empty table place beside the chair; his MOUTH IS "
  "OUTSIDE THE FRAME.\n"
  "PANEL 4 (narrow bridge, full width): SILENT — the blond teen's gaze shifts from the dark-haired "
  "teen to the bandaged old man. No text in this panel.\n"
  "PANEL 5 (bottom band, full width, dominant, the focal panel): a READER-ONLY non-diegetic "
  "split-depth comparison, never a current street and never a literal split panel — in the upper "
  "right field a desaturated memory of the former Uchiha police walking a sunlit Konoha street; in "
  "the lower left field a dark underground corridor receding beneath the bandaged old man. No "
  "current recruit, patrol or restored uniform appears. The blond teen sits small in near-right "
  "foreground profile with his mouth visible. " + L_CHAMBER
  + SAY((1, OFF(BOY16), "upper right", "TOBIRAMA CREATED THE FORCE."),
        (1, OFF(BOY16), "upper left", "HE GAVE IT TO THE UCHIHA TO KEEP THE CLAN BUSY—AND APART FROM POLITICAL POWER."),
        (2, SAS16, "upper right", "EVERY CLAN CONTRIBUTES WHAT IT DOES BEST."),
        (3, OFF(SAS16), "upper right", "OURS CAN KEEP THE VILLAGE'S PEACE."),
        (5, BOY16, "upper right", "THE POLICE WORK IN THE STREET, UNDER LAW, WHERE THE HOKAGE CAN SEE THEM."),
        (5, BOY16, "upper left", "ROOT ANSWERS UNDERGROUND TO ONE MAN."))
  + "The founder-era figure's own armour carries NO Uchiha fan crest anywhere on it; the fan crest appears only on the police officers ranked in front of him and on the older police crest he stands before. ",
  R("naruto_v4_black", "sasuke_16", "danzo", "env_konoha_council_chamber",
    "env_village_street"), "medium"),

 ("p06", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + KOHARU.format(i=3)
  + HOMURA.format(i=4) + DAN.format(i=5) + TSUNADE.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, KOH, HOM, HAWK, TSU, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. The legal route to approval and Hokage oversight are made explicit.\n"
  "PANEL 1 (top right): the elderly female adviser, chin lifted.\n"
  "PANEL 2 (top left): the blond teen looks past her toward the north head.\n"
  "PANEL 3 (middle band, full width): master view re-establishing the axis — the blond teen "
  "indicates the north head, then the east clan-head arc, with an open palm.\n"
  "PANEL 4 (bottom right, narrow): the male adviser adjusts his glasses.\n"
  "PANEL 5 (bottom centre, narrow): the blonde woman studies the dark-haired teen; the blond teen "
  "is OUTSIDE this frame entirely.\n"
  "PANEL 6 (bottom left, dominant): the bandaged old man raises one finger before the female "
  "adviser can continue; she is smaller in the background with her mouth visible. " + L_CHAMBER
  + SAY((1, KOH, "upper right", "WE STILL OBJECT."),
        (2, BOY16, "upper right", "YOU ADVISE THE HOKAGE. YOU DO NOT REPLACE HER."),
        (3, BOY16, "upper right", "IF THE HOKAGE APPROVES AND THE COUNCIL MAJORITY SUPPORTS HER, YOUR VETO FAILS."),
        (4, HOM, "upper right", "THE HOKAGE DID NOT CONTROL THE OLD FORCE."),
        (5, OFF(BOY16), "upper right", "SHE WILL OVERSEE THIS ONE."),
        (6, HAWK, "upper right", "THEN I SUPPORT RESTORATION."),
        (6, KOH, "upper left", "DANZŌ?")),
  R("naruto_v4_black", "sasuke_16", "koharu", "homura", "danzo", "tsunade",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 4: an open force under Sasuke -----------------------------------------
 ("p07", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + DAN.format(i=3)
  + HIASHI.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, SAS16, HAWK, HIA, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. The staffing calculation is shown to the reader and answered with open "
  "standards-based recruitment.\n"
  "PANEL 1 (top right): the bandaged old man looks at the two Uchiha positions — one seated, one "
  "standing on the outer rim.\n"
  "PANEL 2 (top left): extreme close-up of his visible EYE; a faint blank Root mask silhouette is "
  "reflected in it without identifying any operative.\n"
  "PANEL 3 (middle band, full width): the dark-haired teen shifts half a pace closer to the table "
  "along the same outer southeast rim, staying on the blond teen's right side.\n"
  "PANEL 4 (bottom right): the blond teen addresses the east arc rather than the west.\n"
  "PANEL 5 (bottom centre): the stern long-haired clan head's pale eyes narrow.\n"
  "PANEL 6 (bottom left): the dark-haired teen answers directly, with no glance toward the blond "
  "teen. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "A FORCE OF TWO IS NOT A FORCE."),
        (2, HAWK, "upper left", "AN OPEN DOOR CAN ADMIT OTHER EYES."),
        (3, SAS16, "upper right", "WE WILL RECRUIT OUTSIDE THE UCHIHA."),
        (4, BOY16, "upper right", "HYŪGA INCLUDED."),
        (5, HIA, "upper right", "UNDER UCHIHA COMMAND?"),
        (6, SAS16, "upper right", "UNDER POLICE COMMAND."),
        (6, SAS16, "upper left", "CLAN DOES NOT EXEMPT ANYONE FROM THE STANDARD."))
  + "The PANEL 2 balloon is a TAIL-LESS THOUGHT BALLOON with a soft cloud edge belonging to the "
    "bandaged old man; it is not a speech balloon and has no tail. "
  + "The PANEL 2 balloon is a TAIL-LESS thought balloon with a soft scalloped cloud edge and no tail, spike or pointer of any kind touching the eye. ",
  R("naruto_v4_black", "sasuke_16", "danzo", "hiashi", "env_konoha_council_chamber"), "low"),

 ("p08", dict(scene="dialogue", light="day", cast="group", mood="calm", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + SHIKAKU.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, SAS16, TSU, SHIK, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. Command is named and the training path defined.\n"
  "PANEL 1 (tall right, the focal panel): the blonde woman at the north head and the dark-haired "
  "teen beside the southeast chair hold one clear diagonal eye-line across unobstructed tabletop.\n"
  "PANEL 2 (upper left, right cell): SILENT — the blond teen remains seated, neither surprised nor "
  "possessive. No text in this panel.\n"
  "PANEL 3 (upper left, left cell): the blonde woman nods once.\n"
  "PANEL 4 (lower left, right cell): the dark-haired teen looks toward the east clan-head arc.\n"
  "PANEL 5 (lower left, left cell): the man with the long pineapple ponytail opens one hand in "
  "question.\n"
  "PANEL 6 (bottom strip, full width): the two Uchiha share the frame, but the dark-haired teen "
  "stands closer to the chamber centre. " + L_CHAMBER
  + SAY((1, TSU, "upper right", "WHO HEADS IT?"),
        (1, SAS16, "upper left", "I WILL."),
        (3, TSU, "upper right", "THEN I WILL DRAFT THE CHARTER."),
        (4, SAS16, "upper right", "LET ACADEMY GRADUATES AND SERVING SHINOBI APPLY VOLUNTARILY."),
        (5, SHIK, "upper right", "WHAT TRAINING? HOW LONG?"),
        (6, BOY16, "upper right", "WE DESIGN THE PROGRAM. TSUNADE REVIEWS IT."),
        (6, BOY16, "upper centre", "ACADEMY GRADUATES GET UP TO THREE YEARS."),
        (6, SAS16, "upper left", "NO ONE ENTERS BY NAME ALONE."))
  + "This page has EXACTLY SIX panels: the four small left-hand cells form a two-by-two grid whose UPPER-RIGHT cell is a SILENT panel of the blond teen still seated, calm and unpossessive, carrying no balloon at all. ",
  R("naruto_v4_black", "sasuke_16", "tsunade", "shikaku", "env_konoha_council_chamber"), "low"),

 # ---- Spread 5: what begins with money ---------------------------------------------
 ("p09", dict(scene="dialogue", light="day", cast="group", mood="calm", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, TSU,
         "the west-arc advisers and east-arc clan heads seen in lost profile or from behind, none "
         "of them individually recognisable", ATTEND)
  + MAP + DOCS + BLACKFIT + EYES_N +
  "FIVE panels. Accountability is settled before money enters the room.\n"
  "PANEL 1 (top right): the blonde woman writes a short note; every mark is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 2 (top centre): her pen stops.\n"
  "PANEL 3 (top left): the dark-haired teen inclines his head.\n"
  "PANEL 4 (middle band, full width): the east clan-head arc relaxes by degrees; the west adviser "
  "arc does not.\n"
  "PANEL 5 (bottom band, full width): she looks to the dark-haired teen, but the blond teen "
  "answers from the near-right seat. " + L_CHAMBER
  + SAY((1, TSU, "upper right", "RECRUITMENT FILES GO TO SASUKE."),
        (2, TSU, "upper right", "THE TRAINING STANDARD COMES BACK TO ME."),
        (3, SAS16, "upper right", "AGREED."),
        (4, TSU, "upper right", "THE POLICE FORCE IS APPROVED UNDER HOKAGE OVERSIGHT."),
        (5, TSU, "upper right", "WHAT DO YOU NEED TO BEGIN?"),
        (5, BOY16, "upper left", "A HEADQUARTERS. AND THE FUNDS TO BUILD IT.")),
  R("naruto_v4_black", "sasuke_16", "tsunade", "env_konoha_council_chamber"), "low"),

 ("p10", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + TSUNADE.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, TSU, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. Inheritance is allocated; only the reader sees the second allocation.\n"
  "PANEL 1 (top right): the blond teen places two fingers on the table.\n"
  "PANEL 2 (top left): tight three-quarter view including his raised second finger and his visible "
  "LOWER FACE and mouth.\n"
  "PANEL 3 (middle right): the blonde woman's brow tightens.\n"
  "PANEL 4 (middle centre): the blond teen's expression does not shift.\n"
  "PANEL 5 (middle left): she exhales through her nose.\n"
  "PANEL 6 (bottom band, full width, dominant, the focal panel): a READER-ONLY financial "
  "visualization divided by a dark diagonal, containing NO person and NO mouth anywhere — on the "
  "right an account seal beside a police allocation ledger; on the left a rolled, partly open "
  "schematic of conceptual linework only beside a fund ledger. The schematic shows NO ground, lot, "
  "workers, materials, scaffolds or construction, and nobody in the council sees this image. All "
  "ledger and schematic markings are ILLEGIBLE SCRIBBLE. " + L_CHAMBER
  + SAY((1, BOY16, "upper right", "UNFREEZE THE UCHIHA ACCOUNTS."),
        (2, BOY16, "upper right", "AND THE FOURTH HOKAGE'S."),
        (3, TSU, "upper right", "YOU REJECT HIM UNTIL HIS MONEY IS USEFUL?"),
        (4, BOY16, "upper right", "IS IT MINE?"),
        (5, TSU, "upper right", "TWENTY-FIVE PERCENT OF THE UCHIHA FUNDS. HALF OF MINATO'S."),
        (5, TSU, "upper left", "THE REST RETURNS MONTHLY."),
        (6, OFF(TSU), "upper right", "YOU SAID THERE WERE TWO REQUESTS."),
        (6, OFF(BOY16), "upper left", "YES."))
  + "In PANEL 1's wide master the dark-haired teen stands silently one pace behind the blond teen's right shoulder at his fixed mark, visibly present in the shot but taking no balloon anywhere on this page. ",
  R("naruto_v4_black", "tsunade", "env_konoha_council_chamber"), "medium"),

 # ---- Spread 6: copies burn --------------------------------------------------------
 ("p11", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + KOHARU.format(i=4) + HOMURA.format(i=5) + ENV.format(i=6)
  + ONLY(BOY16, SAS16, TSU, KOH, HOM, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. The accusation is precise and leaves the advisers no ambiguity.\n"
  "PANEL 1 (top band, full width): the blond teen turns fully toward the west arc for the first "
  "time; the dark-haired teen retraces his right-side path to the fixed mark behind the blond "
  "teen's right shoulder.\n"
  "PANEL 2 (middle right, upper): the blonde woman looks sharply toward the two elderly advisers.\n"
  "PANEL 3 (middle left, upper): the elderly female adviser's hands flatten on the table.\n"
  "PANEL 4 (middle right, lower): close on the blond teen.\n"
  "PANEL 5 (middle left, lower): the male adviser looks over his lenses.\n"
  "PANEL 6 (bottom band, full width): the east-arc clan heads exchange hard looks, each "
  "understanding the clan-secret precedent; the blonde woman is small at the north background with "
  "her mouth visible; the blond teen is OUTSIDE this frame entirely. " + L_CHAMBER
  + SAY((1, BOY16, "upper right", "BY THE END OF TODAY, EVERY COPY YOU MADE OF UCHIHA SCROLLS WILL BE BURNED."),
        (2, TSU, "upper right", "COPIES?"),
        (3, KOH, "upper right", "WE RETURNED EVERY SCROLL."),
        (4, BOY16, "upper right", "AFTER A WEEK."),
        (5, HOM, "upper right", "WHAT PROOF DO YOU HAVE?"),
        (6, OFF(BOY16), "upper right", "ENOUGH TO KNOW WHICH SECRETS YOU CHOSE."),
        (6, TSU, "upper left", "IF THIS IS TRUE, YOU DISOBEYED A DIRECT ORDER."))
  + "The blond teen's back carries exactly ONE clean, correctly proportioned Uchiha fan crest — never two crests, never a stacked, doubled or duplicated emblem. ",
  R("naruto_v4_black", "sasuke_16", "tsunade", "koharu", "homura",
    "env_konoha_council_chamber"), "low"),

 ("p12", dict(scene="emotional_closeup", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + DAN.format(i=3)
  + HOMURA.format(i=4) + KOHARU.format(i=5) + TSUNADE.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, HAWK, HOM, KOH, TSU, ATTEND) + MAP + DOCS + BLACKFIT + EYES_N +
  "SIX panels. The threat is VERBAL ONLY: no technique activates and no flame, target, damage or "
  "damaged object appears anywhere on this page.\n"
  "PANEL 1 (tall right): the blond teen's visible left eye holds the ordinary three-tomoe "
  "Sharingan, never a Mangekyō pattern; both hands stay still and visible on the tabletop and his "
  "mouth is in frame.\n"
  "PANEL 2 (upper left, top): SILENT — the bandaged old man's visible eye fixes on him while the "
  "male adviser's proof challenge dies behind a rigid expression. Both react to the credibility of "
  "a future threat, not to any live effect. No text in this panel.\n"
  "PANEL 3 (upper left, bottom, the focal panel): the elderly female adviser yields through "
  "clenched teeth while the blond teen stays motionless across the table.\n"
  "PANEL 4 (reaction strip, full width): the blonde woman leans in before she can qualify the "
  "surrender.\n"
  "PANEL 5 (bottom right): the blond teen stands; the dark-haired teen is already aligned behind "
  "him toward the south exit.\n"
  "PANEL 6 (bottom left): the blonde woman points to the south door for the clan heads, then back "
  "to the three advisers. " + L_CHAMBER
  + SAY((1, BOY16, "upper right", "REFUSE, AND I WILL BURN THE UNDERGROUND ARCHIVE AROUND THEM WITH BLACK FLAMES."),
        (3, KOH, "upper right", "FINE."),
        (4, TSU, "upper right", "THEN YOU HAVE JUST ADMITTED IT."),
        (5, BOY16, "upper right", "IF UCHIHA SECRETS ARE STOLEN AGAIN, I REMOVE THE SECRET FROM THE THIEF—OR THE THIEF."),
        (6, TSU, "upper right", "EVERYONE ELSE IS DISMISSED."),
        (6, TSU, "upper left", "DANZŌ. KOHARU. HOMURA. YOU STAY.")),
  R("naruto_v4_black", "sasuke_16", "danzo", "homura", "koharu", "tsunade",
    "env_konoha_council_chamber"), "medium"),

 # ---- Spread 7: the push and the limits --------------------------------------------
 ("p13", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + DOCS + BLACKFIT + EYES_N +
  "SIX panels. Image 3 supplies Uchiha architecture and palette only; every panel is INSIDE the "
  "Uchiha house. Its south door is behind the two men, the low kitchen table is at the centre, the "
  "blond teen keeps the EAST side and the dark-haired teen the WEST side of that table.\n"
  "PANEL 1 (top right, BORDERLESS inset): a swirl of leaves and ember-dark chakra clearing from "
  "the council's south corridor. No figure is identifiable inside the swirl.\n"
  "PANEL 2 (top right, panel): the two arrive inside the house's south door — the blond teen moves "
  "east toward the kitchen, the dark-haired teen west toward the table.\n"
  "PANEL 3 (top left): the blond teen sets a kettle down without looking back.\n"
  "PANEL 4 (middle band, full width): fixed side view across the low table — the dark-haired teen "
  "west at frame left, the blond teen east at frame right.\n"
  "PANEL 5 (bottom right): the blond teen pours tea.\n"
  "PANEL 6 (bottom left, the focal panel): the blond teen finally meets the dark-haired teen's "
  "eyes across the table. " + L_HOUSE
  + SAY((2, SAS16, "upper right", "THAT WENT BETTER THAN I EXPECTED."),
        (3, BOY16, "upper right", "WHAT DID YOU EXPECT?"),
        (4, SAS16, "upper right", "TO FIGHT FOR THE FORCE."),
        (4, SAS16, "upper centre", "NOT TO LEAVE WITH THE FORCE, THE MONEY, AND THREE NEW ENEMIES."),
        (5, BOY16, "upper right", "THEY WERE ALREADY ENEMIES."),
        (6, BOY16, "upper right", "I PUSHED THEM UNTIL THEY FELT POWERLESS."),
        (6, BOY16, "upper left", "I WANTED THEM TO MAKE A DRASTIC MOVE."))
  + SFX(1, "FSSSH", "Lower left inside the borderless inset; it must not touch either figure.")
  + "The borderless transition inset is the TOP-RIGHT element of the page and is read first. In PANEL 4 the balloon \"TO FIGHT FOR THE FORCE.\" sits at the UPPER RIGHT of the panel and \"NOT TO LEAVE WITH THE FORCE, THE MONEY, AND THREE NEW ENEMIES.\" sits to its LEFT, in that right-to-left order. ",
  R("naruto_v4_black", "sasuke_16", "env_uchiha_compound"), "low"),

 ("p14", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + DOCS + BLACKFIT + EYES_N +
  "SIX panels, EVERY ONE INSIDE the Uchiha house; no panel leaves it. The cord-wrapped packet "
  "travels EAST TO WEST across the table and stays on the dark-haired teen's west side for the "
  "rest of the scene. Both mouths stay visible for every ordinary balloon tail.\n"
  "PANEL 1 (top right): the dark-haired teen's eyes narrow, unimpressed, while the blond teen "
  "closes the kettle lid across the table.\n"
  "PANEL 2 (top left): SILENT — the blond teen places a plain cord-wrapped packet of loose sheets "
  "on the table's east edge. Only a small Root emblem is visible; there is NO folder and NO "
  "readable text, and the dark-haired teen watches the packet rather than him. No text in this "
  "panel.\n"
  "PANEL 3 (middle band, full width): he slides the packet west while both faces stay visible in "
  "profile; the dark-haired teen reaches to receive it.\n"
  "PANEL 4 (lower right, dominant, the focal panel): the dark-haired teen closes one hand over the "
  "packet and the blond teen releases it; the wider framing keeps both profiles visible.\n"
  "PANEL 5 (lower left): the blond teen stands at the table's east side; the dark-haired teen "
  "remains seated with the Root packet and NO authorization papers.\n"
  "PANEL 6 (bottom band, full width): still inside the house, the blond teen reaches the south "
  "door as a warm RED-ORANGE teleportation swirl begins to close around him, drawn as flat opaque "
  "shapes; the dark-haired teen stays at the table with the packet. " + L_HOUSE
  + SAY((1, SAS16, "upper right", "WHY INVITE IT?"),
        (1, BOY16, "upper left", "TO SEE WHAT THEY CHOOSE UNDER PRESSURE."),
        (3, BOY16, "upper right", "ROOT'S FOUNDING. STRUCTURE. KNOWN OPERATIONS."),
        (4, BOY16, "upper right", "YOU COMMAND THE POLICE FORCE. I SUPPLY INTELLIGENCE, TRAINING, AND MONEY."),
        (5, BOY16, "upper right", "COLLECT THE PAPERWORK FROM TSUNADE BEFORE THE END OF THE DAY."),
        (5, BOY16, "upper left", "THEN SEE SHIKAMARU ABOUT THE PLANS."),
        (6, SAS16, "upper right", "WHERE ARE YOU GOING?"),
        (6, BOY16, "upper left", "TO SEE KARIN."))
  + "The PANEL 4 balloon reads exactly \"YOU COMMAND THE POLICE FORCE. I SUPPLY INTELLIGENCE, TRAINING, AND MONEY.\" with INTELLIGENCE spelled I-N-T-E-L-L-I-G-E-N-C-E and ordinary commas between the three nouns. This page has EXACTLY SIX panels and the packet-handoff close-up is the DOMINANT LOWER-RIGHT panel; do not add any extra silent panel anywhere. ",
  R("naruto_v4_black", "sasuke_16", "env_uchiha_compound"), "low"),

 # ---- Spread 8: the survivor in Earth Country --------------------------------------
 ("p15", dict(scene="establishing", light="day", cast="small_group", mood="somber", panels=5),
  FILL + RTL + KAB.format(i=1) + ENV.format(i=2) + ENV.format(i=3)
  + ONLY(SPEC,
         "masked Iwa scouts in plain porcelain animal masks and rock-country field gear, never "
         "unmasked and never individually recognisable, and one unidentifiable body lying under a "
         "sheet with no face ever shown")
  + DOCS +
  "FIVE panels. Image 2 is the concealed hillside entrance, image 3 the stripped hall inside.\n"
  "PANEL 1 (top band, full width): Earth Country by day — masked scouts descend a rocky cut toward "
  "a concealed entrance. Keep the lower right quiet for the location card.\n"
  "PANEL 2 (middle right): SILENT — the hall is stripped: bare shelves, empty laboratory brackets, "
  "scorch scars, nobody in it. No text in this panel.\n"
  "PANEL 3 (middle centre): one unidentifiable body lies under a sheet, its face never shown; a "
  "masked scout kneels to check it with his mouth hidden behind the mask.\n"
  "PANEL 4 (middle left): another masked scout finds the grey-haired young man in round glasses "
  "collapsed but intact against the wall, his mouth hidden behind the mask.\n"
  "PANEL 5 (bottom band, full width, the focal panel): the grey-haired young man's glasses lie "
  "cracked beside his open, unfocused eye while a medic's two fingers confirm a pulse. The medic's "
  "MOUTH IS OUTSIDE THE FRAME. He is visibly alive and cannot speak. " + L_CAVE +
  'LOCATION CARD: in PANEL 1, at the lower right, write "EARTH COUNTRY." in bold upright English '
  'capitals as a BORDERLESS tail-less card — not a balloon, not a bordered box, pointing at no '
  'one. '
  + SAY((3, OFF(IWA_SCOUT), "upper right", "ONE DEAD."),
        (4, OFF(IWA_MEDIC), "upper right", "THIS ONE IS BREATHING."),
        (5, OFF(IWA_MEDIC), "upper right", "YAKUSHI KABUTO. ALIVE."))
  + "In PANEL 2 the shelves and laboratory brackets are COMPLETELY BARE — no jars, bottles, scrolls or equipment remain anywhere in the hall, only empty fittings, dust and scorch scars. ",
  R("kabuto", "env_oto_hidden_base", "env_oto_throne_hall"), "medium"),

 ("p16", dict(scene="dialogue", light="dusk", cast="two", mood="tense", panels=5),
  FILL + RTL + ENV.format(i=1)
  + ONLY(OLDKAGE,
         "one kneeling masked Iwa scout captain in a plain porcelain mask and rock-country field "
         "gear, never unmasked and never individually recognisable")
  + DOCS +
  "FIVE panels. Image 1 supplies the desk-and-window office layout ONLY: this room is IWAGAKURE'S "
  "stone office — rough rock walls, a rock-cut west window and a stone map wall, never a wooden "
  "Konoha interior. The old village leader is a very short, stout, elderly man in a heavy kage "
  "coat and hat; he sits NORTH behind the desk, the kneeling masked scout is SOUTH before it, the "
  "country map is on the EAST wall and the WEST window supplies the only hard light.\n"
  "PANEL 1 (top strip, full width): the village at dusk from outside, west light cutting across "
  "the tower. Keep the upper right quiet for the location card.\n"
  "PANEL 2 (tall right): fixed office geography — the old leader north behind the desk, the masked "
  "scout kneeling south, the map east.\n"
  "PANEL 3 (upper left): the masked scout reports without raising his face; his mouth is hidden "
  "behind the mask.\n"
  "PANEL 4 (middle left): the old leader turns his eyes to a marked entry point on the east-wall "
  "map; every label on it is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 5 (bottom left): his finger lands on the route between the hideout and the leaf village; "
  "the place names stay unreadable and his mouth is visible. " + L_IWA +
  'LOCATION CARD: in PANEL 1, at the upper right, write "IWAGAKURE." in bold upright English '
  'capitals as a BORDERLESS tail-less card — not a balloon, not a bordered box, pointing at no '
  'one. '
  + SAY((2, OLDKAGE, "upper right", "WHAT DID YOU FIND?"),
        (3, OFF(IWA_CAP), "upper right", "OROCHIMARU'S HIDEOUT. STRIPPED CLEAN."),
        (3, OFF(IWA_CAP), "upper left", "KABUTO SURVIVED, BUT CANNOT SPEAK."),
        (4, OLDKAGE, "upper right", "WAS THE UCHIHA THERE?"),
        (4, OFF(IWA_CAP), "upper left", "HIS TRACE WAS."),
        (5, OLDKAGE, "upper right", "PUT ALPHA AND BETA ON IT."),
        (5, OLDKAGE, "upper left", "KONOHA IS BUILDING STRENGTH AGAIN."))
  + "The second PANEL 5 balloon is a TAIL-LESS THOUGHT BALLOON with a soft cloud edge belonging to "
    "the old village leader; it is not a speech balloon and has no tail. "
  + "The second PANEL 5 balloon is a TAIL-LESS thought balloon with a soft scalloped cloud edge and no tail or spike of any kind. The old village leader wears the same round spectacles in EVERY panel of this page. ",
  R("env_hokage_office"), "low"),

 # ---- Spread 9: a life beyond ANBU -------------------------------------------------
 ("p17", dict(scene="establishing", light="day", cast="small_group", mood="calm", panels=5),
  FILL + RTL + YUGAO_V4.format(i=1) + KURENAI.format(i=2) + ANK.format(i=3)
  + ENV.format(i=4) + ENV.format(i=5)
  + ONLY(YUG, KUR, ANKO,
         "unnamed lunch-shop customers and one waiter in the background, none of them named, "
         "recurring or individually recognisable")
  + DOCS +
  "FIVE panels. Image 4 is the Konoha street, image 5 the small eatery's palette and fittings; the "
  "shop holds a small TRIANGULAR three-seat table with the purple-haired kunoichi NORTH, the "
  "red-eyed woman SOUTHEAST at reader-right and the violet-haired woman in the tan coat SOUTHWEST "
  "at reader-left. That triangle never changes and is never mirrored.\n"
  "PANEL 1 (top band, full width): Konoha afternoon — the purple-haired kunoichi walks from the "
  "ANBU quarter toward the small lunch shop, her plain porcelain mask HELD AT HER SIDE rather than "
  "worn.\n"
  "PANEL 2 (middle right): SILENT — she enters the shop and sees the red-eyed woman and the "
  "violet-haired woman waiting at the triangular table. No text in this panel.\n"
  "PANEL 3 (middle centre): the fixed seating — the red-eyed woman at reader-right notices her "
  "smile.\n"
  "PANEL 4 (middle left): the violet-haired woman leans in from reader-left.\n"
  "PANEL 5 (bottom band, full width): the kunoichi reaches for her tea to hide a wider smile; the "
  "violet-haired woman refuses to let the pause pass. " + L_SHOP
  + SAY((1, YUG, "upper right", "ANBU USED TO BE ENOUGH."),
        (1, YUG, "upper left", "NOW I WANT TIME THAT BELONGS TO ME."),
        (3, KUR, "upper right", "YOU SEEM HAPPY."),
        (4, ANKO, "upper right", "THAT SMILE IS NOT ABOUT ANBU."),
        (5, ANKO, "upper right", "SO WHO IS HE?"))
  + "BOTH PANEL 1 balloons are TAIL-LESS THOUGHT BALLOONS with soft cloud edges belonging to the "
    "purple-haired kunoichi; they are not speech balloons and have no tails. "
  + "In PANEL 5 the balloon \"SO WHO IS HE?\" belongs to the violet-haired woman in the tan coat at reader-LEFT and its tail must run down-LEFT to her visible mouth, never toward the red-eyed woman at reader-right. ",
  R("yugao_v4", "kurenai", "anko", "env_village_street", "env_ichiraku"), "medium"),

 ("p18", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + RTL + YUGAO_V4.format(i=1) + KURENAI.format(i=2) + ANK.format(i=3) + ENV.format(i=4)
  + ONLY(YUG, KUR, ANKO,
         "one unnamed waiter and unnamed background customers, none of them individually "
         "recognisable and none of them ever speaking")
  + DOCS +
  "SIX panels. The triangular seating is unchanged: the purple-haired kunoichi north, the red-eyed "
  "woman southeast at reader-right, the violet-haired woman in the tan coat southwest at "
  "reader-left.\n"
  "PANEL 1 (top strip, full width): a waiter sets down two lunches plus dango and a small sake "
  "flask; he has NO balloon and every menu mark is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 2 (middle right): SILENT — the kunoichi looks from one friend to the other. No text in "
  "this panel.\n"
  "PANEL 3 (middle centre): the red-eyed woman waits without teasing.\n"
  "PANEL 4 (middle left): the violet-haired woman points across the table.\n"
  "PANEL 5 (bottom right): SILENT — the kunoichi steadies her cup, then lowers it. No text in this "
  "panel.\n"
  "PANEL 6 (bottom left, the focal panel): she chooses a direct answer. " + L_SHOP
  + SAY((3, KUR, "upper right", "WHEN DID YOU LAST LOOK THIS HAPPY?"),
        (4, ANKO, "upper right", "STOP MAKING US GUESS."),
        (6, YUG, "upper right", "I AM GOING OUT TONIGHT."))
  + "The red-eyed woman's single red sleeve is always on her RIGHT arm and her opposite shoulder is bare white wrapping; this asymmetry must not flip in any panel. ",
  R("yugao_v4", "kurenai", "anko", "env_ichiraku"), "low"),

 # ---- Spread 10: Naruto ------------------------------------------------------------
 ("p19", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + RTL + YUGAO_V4.format(i=1) + KURENAI.format(i=2) + ANK.format(i=3) + ENV.format(i=4)
  + ONLY(YUG, KUR, ANKO,
         "unnamed background customers, none of them individually recognisable and none of them "
         "ever speaking")
  + DOCS +
  "SIX panels. Same triangular seating, never mirrored.\n"
  "PANEL 1 (top right): the violet-haired woman raises a triumphant fist.\n"
  "PANEL 2 (top centre): the red-eyed woman stays measured.\n"
  "PANEL 3 (top left): the kunoichi's confidence flickers only slightly.\n"
  "PANEL 4 (middle band, full width, the focal panel): the violet-haired woman leans over her "
  "plate; the kunoichi answers across the table with her mouth visible.\n"
  "PANEL 5 (bottom right): the red-eyed woman's eyes widen.\n"
  "PANEL 6 (bottom left): close on the kunoichi with no embarrassment in her face. " + L_SHOP
  + SAY((1, ANKO, "upper right", "I KNEW IT."),
        (2, KUR, "upper right", "LIKE A DATE?"),
        (3, YUG, "upper right", "I DO NOT KNOW. IT MIGHT BE."),
        (4, ANKO, "upper right", "FORGET THAT. WHO IS HE?"),
        (4, YUG, "upper left", "NARUTO."),
        (5, KUR, "upper right", "YOU MEAN THE NARUTO?"),
        (6, YUG, "upper right", "YES."))
  + "In every panel the purple-haired kunoichi is NORTH at the top of the frame, the red-eyed woman SOUTHEAST at reader-right and the violet-haired woman in the tan coat SOUTHWEST at reader-left; this seating triangle does not rotate or mirror in the wide PANEL 4. ",
  R("yugao_v4", "kurenai", "anko", "env_ichiraku"), "low"),

 ("p20", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=7),
  FILL + RTL + YUGAO_V4.format(i=1) + KURENAI.format(i=2) + ANK.format(i=3) + ENV.format(i=4)
  + ONLY(YUG, KUR, ANKO,
         "unnamed background customers and unnamed passers-by in the street beyond the shop, none "
         "of them individually recognisable and none of them ever speaking")
  + DOCS +
  "SEVEN panels. The four top panels read RIGHT TO LEFT across the page.\n"
  "PANEL 1 (top far right, small): SILENT — the violet-haired woman bursts into laughter; the "
  "reaction carries the beat with no balloon. No text in this panel.\n"
  "PANEL 2 (top right centre, small): her laughter stops when the kunoichi does not move.\n"
  "PANEL 3 (top left centre, small): SILENT — the kunoichi nods once. No text in this panel.\n"
  "PANEL 4 (top far left, small): the red-eyed woman studies her friend.\n"
  "PANEL 5 (middle right): the kunoichi answers the red-eyed woman rather than the violet-haired "
  "one.\n"
  "PANEL 6 (middle left): the violet-haired woman waves the objection away.\n"
  "PANEL 7 (bottom band, full width, the focal panel): the violet-haired woman gestures toward the "
  "street beyond the shop; the kunoichi goes completely still. No red-haired woman is drawn in "
  "this panel. " + L_SHOP
  + SAY((2, ANKO, "upper right", "YOU ARE SERIOUS."),
        (4, KUR, "upper right", "IS HE NOT YOUNGER THAN YOU?"),
        (5, YUG, "upper right", "AGE DOES NOT CHANGE MY ANSWER."),
        (6, ANKO, "upper right", "AGE IS A NUMBER."),
        (7, ANKO, "upper right", "I SAW HIM AN HOUR AGO WITH A YOUNG RED-HAIRED WOMAN."))
  + "In the middle row the purple-haired kunoichi's panel with \"AGE DOES NOT CHANGE MY ANSWER.\" is the RIGHT panel and the violet-haired woman's panel with \"AGE IS A NUMBER.\" is the LEFT panel, so the exchange reads right to left in that order. ",
  R("yugao_v4", "kurenai", "anko", "env_ichiraku"), "low"),

 # ---- Spread 11: the question she will ask -----------------------------------------
 ("p21", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + YUGAO_V4.format(i=1) + KURENAI.format(i=2) + ANK.format(i=3) + KARIN.format(i=4)
  + ENV.format(i=5) + ENV.format(i=6)
  + ONLY(YUG, KUR, ANKO,
         KAR + " appearing ONLY inside the borderless memory image in PANEL 1, never in the lunch "
         "shop",
         "unnamed background customers, none of them individually recognisable")
  + DOCS +
  "SIX panels. Image 5 is the lunch shop, image 6 the doorway interior remembered in PANEL 1.\n"
  "PANEL 1 (top band, full width): BORDERLESS memory image, slightly desaturated — the doorway of "
  "the blond teen's old house, the young red-haired girl standing inside it while the purple-haired "
  "kunoichi remains outside. She is not named, and there is no implication of romance or "
  "hostility. Nobody speaks inside the memory image.\n"
  "PANEL 2 (middle right): back at the lunch table, the red-eyed woman watches the kunoichi absorb "
  "the information.\n"
  "PANEL 3 (middle left): the kunoichi looks directly at her.\n"
  "PANEL 4 (bottom right): the violet-haired woman tilts her head.\n"
  "PANEL 5 (bottom centre): the violet-haired woman lowers her voice, honestly confused.\n"
  "PANEL 6 (bottom left): the kunoichi's answer is calm. " + L_SHOP
  + SAY((1, YUG, "upper right", "THE WOMAN AT HIS HOME."),
        (2, KUR, "upper right", "ARE YOU SURE ABOUT THIS, YUGAO?"),
        (3, YUG, "upper right", "I WANT TO TRY."),
        (4, ANKO, "upper right", "HOW DID THIS EVEN HAPPEN?"),
        (5, ANKO, "upper right", "I THOUGHT HE WAS NOT INTERESTED IN WOMEN."),
        (6, YUG, "upper right", "NARUTO IS NOT GAY."),
        (6, YUG, "upper left", "SPEND TIME WITH HIM AND YOU UNDERSTAND."))
  + "The PANEL 1 balloon is a TAIL-LESS THOUGHT BALLOON with a soft cloud edge belonging to the "
    "purple-haired kunoichi; it is not a speech balloon and has no tail. "
  + "LETTERING IS CRITICAL: render every balloon's text ONCE with no doubled, overlapping, ghosted or overprinted lettering, and spell each line out in full — PANEL 2 reads exactly \"ARE YOU SURE ABOUT THIS, YUGAO?\" and PANEL 3 reads exactly \"I WANT TO TRY.\" The borderless memory element at the top of the page is a SEPARATE borderless inset that must not be merged into the present-day shop panel or share its frame. ",
  R("yugao_v4", "kurenai", "anko", "karin", "env_ichiraku", "env_shinobi_apartment"), "low"),

 ("p22", dict(scene="emotional_closeup", light="day", cast="solo", mood="calm", panels=4),
  FILL + RTL + YUGAO_V4.format(i=1) + KARIN.format(i=2) + KURENAI.format(i=3) + ANK.format(i=4)
  + ENV.format(i=5) + ENV.format(i=6)
  + ONLY(YUG,
         "the red-eyed woman and the violet-haired woman in the tan coat, present ONLY as soft "
         "out-of-focus background shapes with no balloons",
         KAR + " appearing ONLY inside the borderless memory image in PANEL 2, never in the lunch "
         "shop")
  + DOCS +
  "FOUR panels. LAST PAGE OF THE CHAPTER AND OF THE VOLUME. It ends on a decision and previews "
  "nothing: no dinner, no retaliation, no adviser, no target and no later scene may appear. Image "
  "5 is the lunch shop, image 6 the remembered doorway.\n"
  "PANEL 1 (top band, full width): the lunch resumes around the purple-haired kunoichi, but the "
  "red-eyed woman and the violet-haired woman are SOFT OUT-OF-FOCUS background shapes with no "
  "balloons; the kunoichi looks down into her tea.\n"
  "PANEL 2 (middle right): BORDERLESS memory image — the young red-haired girl framed ALONE in the "
  "old doorway, supplying no answer. She does not speak.\n"
  "PANEL 3 (middle left): close on the kunoichi's eyes as curiosity replaces the earlier smile.\n"
  "PANEL 4 (bottom band, full width, dominant, the chapter and volume focal panel): she lifts her "
  "gaze from the cup, settled on a direct course. Nobody else receives dialogue. " + L_SHOP
  + SAY((1, YUG, "upper right", "HE WOULD SAY HE HAS FAR BETTER THINGS TO DO."),
        (2, YUG, "upper right", "WHAT IS HER RELATIONSHIP WITH HIM?"),
        (3, YUG, "upper right", "I WANT TO KNOW."),
        (4, YUG, "upper right", "I WILL ASK HIM—POLITELY—TONIGHT."))
  + "ALL FOUR balloons on this page are TAIL-LESS THOUGHT BALLOONS with soft cloud edges belonging "
    "to the purple-haired kunoichi; none of them is a speech balloon and none of them has a tail. "
  + "The memory panel shows the red-haired girl in an INTERIOR DOORWAY of the eatery, not out in a street, matching the interior established on the previous page. ",
  R("yugao_v4", "karin", "kurenai", "anko", "env_ichiraku", "env_shinobi_apartment"), "high"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch13" / "raw", HERE / "v5ch13" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
