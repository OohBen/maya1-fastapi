"""Volume 5, Chapter 12 — "Head of the Uchiha". 20 pages.

Translated 1:1 from story/volume_05/drafts/ch12_head_of_the_uchiha.md — every balloon, its
panel, its speaker, its stated position and its exact text. Reading order is RIGHT TO LEFT on
every page. Source: fic ch16:113-307.

The council map is fixed for all 20 pages and continues unchanged into Chapter 13; no shot may
mirror it. Every document, agenda, statute copy and strategic map carries ILLEGIBLE SCRIBBLE
only, and no paper ever crosses the table. SEATING below is the single seating law and is
carried by every page; CAST is the single cast-integrity law and is carried by every page.

REFERENCE GAP — this is why the chamber was not a stable room on the first pass:
  * inoichi.png and shibi.png DO NOT EXIST. Inoichi and Shibi are named in the draft's seating
    table and carry the inter-clan marriage and attachment argument, but no sheet exists for
    either, so page 11's two east-arc speakers stay deliberately unnamed. Hiashi and Shikaku,
    who DO have sheets, are now bound on the pages whose east arc is in frame (p01, p02, p06,
    p11 alongside p03, p05, p08, p09, p12, p18) so the arc has recognisable anchors instead of
    interchangeable extras. Add the two sheets and bind them to promote the p11 speakers.
  * choza.png — named only in the draft's seating table, never in a panel; no page needs it.
  * The blonde woman at the north head and the dark-haired teen at the southeast place are named
    by SEATING on EVERY page, so tsunade and sasuke_16 must stay bound on every page where their
    place can be in frame. Leaving either unbound is what replaced Tsunade with a stranger on
    p18, deleted Sasuke on p14 and grew a duplicate blond Naruto on p04.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import DAN, ENV, FILL, HAWK, OFF, ONLY, R, SAY  # noqa: E402
from prompts_v4 import (HIASHI, HOMURA, KOHARU, N16_BLACK, SASUKE16, SHIKAKU,     # noqa: E402
                        TSUNADE, HIASHI_SPEAKER, HOMURA_SPEAKER, KOHARU_SPEAKER,
                        N16_SPEAKER, SASUKE16_SPEAKER, SHIKAKU_SPEAKER, TSUNADE_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
SAS16 = SASUKE16_SPEAKER
TSU = TSUNADE_SPEAKER
KOH = KOHARU_SPEAKER
HOM = HOMURA_SPEAKER
SHIK = SHIKAKU_SPEAKER
HIA = HIASHI_SPEAKER
EAST_HAND = "the open-handed clan head on the east arc"
EAST_GLASS = "the clan head in dark round glasses on the east arc"
EAST_HAND_D = ("one seated clan head on the east arc who opens one hand as he speaks — an ordinary "
               "unnamed adult man in plain clan robes who must not resemble any other named "
               "character")
EAST_GLASS_D = ("one seated clan head on the east arc in dark round glasses and a high collar — an "
                "ordinary unnamed adult man whose eyes are never visible")
ATTEND = ("the remaining seated clan heads on the east arc — adult men and women of visibly "
          "different ages, builds, hair and clan robes, each drawn as an individual rather than a "
          "copy of his neighbour, none of them ever speaking — plus attendants and two masked door "
          "guards who stand OUTSIDE the seating oval against the wall")
# ---------------------------------------------------------------- the fixed chamber
# The first pass proved the chamber was not a stable room: named clan heads were replaced by
# interchangeable elderly men, Hiashi turned up among the advisers on p03, a stranger held the
# north head on p18 and Danzo vanished from the closing master on p20. The old MAP constant
# stated the layout but not the POLITICS of the layout, and it named the blonde woman and the
# dark-haired teen on pages where neither was bound to a reference image, which is how they got
# substituted. This is the single seating law for the whole chapter; every page carries it, and
# every name it uses is bound on the pages where that figure can be in frame.
SEATING = (
    "THE COUNCIL CHAMBER IS ONE FIXED ROOM WITH ONE FIXED POLITICAL GEOGRAPHY. It never rotates, "
    "never mirrors, never changes its population between panels or pages, and is identical in "
    "every shot of this chapter. "
    "THE TABLE: ONE CONTINUOUS UNBROKEN OVAL with a single smooth rim — never a horseshoe, never "
    "an open centre, never split into separate slabs or disjointed sections. Nobody ever enters "
    "the interior of the oval and no document ever crosses it. "
    "NORTH HEAD: the blonde woman in the green haori — two long blonde tails, a dark diamond mark "
    "centred on her forehead — sits ALONE at the north head behind her low desk, one shallow step "
    "above the table, facing south-southeast. Whenever the north head is in frame it is HER, "
    "seated at that desk. She is never replaced by, swapped with or redrawn as a grey-haired "
    "elder, a robed stranger or any other figure, and the north head is never left empty. "
    "WEST ARC, at reader-LEFT: EXACTLY THREE elderly advisers and nobody else — the bandaged old "
    "man with the cane and the slung bandaged right arm, the elderly female adviser with the "
    "severe pale hair bun, and the elderly male adviser in the small round glasses. Always those "
    "three, always three, never a fourth filled seat, never a second copy of any of them, never a "
    "young person, never a blond figure, never anyone in a shinobi flak vest. They look "
    "screen-right, south-east, across the table. "
    "EAST ARC, at reader-RIGHT: the CLAN HEADS. Each is a distinct adult with clearly different "
    "age, build, hair and clan robes from his neighbours — they are never a row of interchangeable "
    "elderly men, never identical to one another, never blank-faced or featureless, and never a "
    "rank of uniformed ninja in matching green flak vests or masks. The stern long-haired Hyuga "
    "clan head with the pale pupil-less eyes and the man with the long pineapple ponytail sit on "
    "THIS arc whenever they appear, and NEVER on the west arc among the advisers. They look "
    "screen-left, south, across the table. "
    "SOUTHEAST: the carved high-backed Uchiha chair stands at the near south-east end of the oval, "
    "reader-right of the south entrance. The blond teen sits in it facing north-west, and the "
    "dark-haired teen holds his mark one pace behind the blond teen's right shoulder, between the "
    "chair and the south wall, never crossing behind him. Whenever the southeast place is in "
    "frame, both of them are in it. "
    "No adviser ever sits on the east arc and no clan head ever sits on the west arc. "
)

# The other repeating failure was cast integrity rather than geography: a duplicate blond Naruto
# appeared three times, faces came back blank or doubled, and one panel rendered empty.
CAST = (
    "EXACTLY ONE blond person exists anywhere on this page — the blond teen in the carved Uchiha "
    "chair at the southeast place. There is never a second blond figure, never a duplicate or "
    "mirrored copy of him, and nobody seated on the west or east arc wears a black shirt with a "
    "red Uzumaki spiral. Only the blond teen and the dark-haired teen carry the Uchiha fan crest; "
    "no other figure in the chamber, foreground or background, wears a fan crest. Every face on "
    "the page is fully drawn with eyes, nose and mouth — none is blank, featureless, smeared, "
    "garbled or doubled, nobody has two overlapping heads, and no second face hides inside "
    "anyone's "
    "hair. Every panel contains its described drawing; no panel is left blank, beige or "
    "unrendered. "
)

DOCS = ("Every agenda sheet, statute copy and strategic map on the table carries ILLEGIBLE "
        "SCRIBBLE, not readable words, and no document is ever handed over or crosses the table. ")
BLACKFIT = ("The blond teen wears the fitted long-sleeved black shirt carrying BOTH the Uchiha fan "
            "crest and the Uzumaki spiral on its back, black trousers and black gloves — no "
            "armour, no forehead protector, no gunbai and no sign of illness. ")
EYES_N = ("His visible left eye holds the ORDINARY three-tomoe Sharingan on every page: never a "
          "Mangekyō pattern, never a glow, never a technique. ")
EYES_S_OFF = "The dark-haired teen's eyes are ordinary dark eyes on this page; his Sharingan is OFF. "
EYES_S_ON = ("The dark-haired teen's eyes are RED with three black tomoe each on this page; his "
             "Sharingan is active but he never moves against anyone. ")
L_CHAMBER = ("Lighting: cool even daylight from high slit windows onto pale stone and dark wood, "
             "hard ink shadows under the table, no glow anywhere. ")

PAGES = [
 # ---- Spread 1: the empty chair ----------------------------------------------------
 ("p01", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + DAN.format(i=4) + KOHARU.format(i=5) + HOMURA.format(i=6) + HIASHI.format(i=7)
  + SHIKAKU.format(i=8) + ENV.format(i=9)
  + ONLY(BOY16, SAS16, TSU, HAWK, KOH, HOM, HIA, SHIK, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_OFF +
  "FIVE panels. The summoned pair enter as apparent subjects; the unused chair gives the blond "
  "teen another route through the meeting.\n"
  "PANEL 1 (top band, full width): high establishing shot from the south wall — the blonde woman "
  "anchors the north head of the continuous oval, the three elderly advisers hold the west arc at "
  "reader-left and the clan heads the east arc at reader-right. The blond teen enters and turns "
  "toward the unused southeast chair; the dark-haired teen follows into the mark behind his right "
  "shoulder without crossing him. The blond teen's back shows both the Uchiha fan and the Uzumaki "
  "spiral. Every visible face turns toward them. The UPPER CENTRE of this panel is PROTECTED EMPTY "
  "NEGATIVE SPACE carrying only the chapter marker — no figure, object or balloon may enter it.\n"
  "PANEL 2 (middle right): tight on the blond teen continuing forward without looking at the male "
  "adviser; his three tomoe track the empty chair instead.\n"
  "PANEL 3 (middle centre): the dark-haired teen's point of view past the blond teen — the empty "
  "high-backed chair at the southeast end carries the Uchiha fan crest; the bandaged old man and "
  "the adviser arc are visible across its north-west eye-line.\n"
  "PANEL 4 (middle left): the elderly female adviser turns in profile on the west arc, eyes "
  "cutting screen-right.\n"
  "PANEL 5 (bottom band, full width): low close shot from behind the southeast chair — the blond "
  "teen's gloved right hand settles on its back, only part of his mouth in frame; the dark-haired "
  "teen stops one pace behind his right shoulder; the continuous tabletop and the adviser arc form "
  "the diagonal beyond. " + L_CHAMBER +
  'LETTERING: in the protected upper-centre negative space of PANEL 1, write the chapter marker in '
  'bold upright English capitals on one line: "CHAPTER 12 — HEAD OF THE UCHIHA". It is a tail-less '
  'title, not a balloon. '
  + SAY((1, HOM, "upper right", "YOU KEPT THE COUNCIL WAITING."),
        (4, KOH, "upper left", "STAND WHERE YOU WERE SUMMONED."),
        (5, BOY16, "upper right", "I AM."))
  + "In PANEL 1 the balloon \"YOU KEPT THE COUNCIL WAITING.\" belongs to the elderly male adviser "
    "in the small round glasses, seated on the WEST arc at reader-LEFT; draw a long tail "
    "travelling all the way across to HIS mouth and never to any figure on the east arc. The west "
    "arc carries only the bandaged old man, the elderly female adviser and the elderly male "
    "adviser — there is no second woman with a pale hair bun anywhere in the chamber. The east "
    "arc carries the stern long-haired Hyuga clan head with the pale pupil-less eyes and the man "
    "with the long pineapple ponytail among clan heads of visibly different ages and robes, never "
    "five interchangeable elderly men. In PANEL 5 the blond teen has ONE head and ONE cleanly "
    "drawn face — no second, ghosted or overlapping head — and his balloon \"I AM.\" tails to HIS "
    "mouth, never to the dark-haired teen behind his right shoulder.",
  R("naruto_v4_black", "sasuke_16", "tsunade", "danzo", "koharu", "homura", "hiashi",
    "shikaku", "env_konoha_council_chamber"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + KOHARU.format(i=3)
  + HOMURA.format(i=4) + TSUNADE.format(i=5) + HIASHI.format(i=6) + SHIKAKU.format(i=7)
  + ENV.format(i=8)
  + ONLY(BOY16, SAS16, KOH, HOM, TSU, HIA, SHIK, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_OFF +
  "FIVE panels. He makes the claim explicit before anyone can define his status for him.\n"
  "PANEL 1 (top right): side view along the southeast rim — he pulls the chair out and turns it "
  "north-west; the female adviser is visible across the table on the west arc.\n"
  "PANEL 2 (top left): he lowers into the chair, gaze north-west toward her and the adviser arc; "
  "the dark-haired teen holds the fixed mark behind his right shoulder.\n"
  "PANEL 3 (middle right): the male adviser leans forward, his glasses catching the red eyes "
  "across the table.\n"
  "PANEL 4 (middle left): the blond teen places both forearms on the chair arms, completely "
  "still.\n"
  "PANEL 5 (bottom band, full width): long diagonal two-shot — the blond teen at the southeast "
  "place and the blonde woman at the north head with the continuous tabletop between them; the "
  "dark-haired teen is a dark vertical behind his right shoulder. " + L_CHAMBER
  + SAY((1, KOH, "upper right", "WHO TOLD YOU TO SIT?"),
        (2, BOY16, "upper right", "I KNOW WHICH SEAT IS MINE."),
        (3, HOM, "upper right", "YOU WERE CALLED TO ANSWER. YOU ARE NOT A COUNCIL MEMBER."),
        (4, BOY16, "upper right", "THEN YOU CALLED THE WRONG MAN."),
        (5, BOY16, "upper right", "YOU SUMMONED THE HEAD OF THE UCHIHA."))
  + "In PANEL 5 the balloon \"YOU SUMMONED THE HEAD OF THE UCHIHA.\" belongs to the BLOND TEEN "
    "seated at the southeast place: its tail must reach HIS mouth and must never run down-right "
    "onto the dark-haired teen, who speaks nothing on this page. The east-arc clan heads are the "
    "SAME individuals at the same ages and in the same clan robes as on the previous page — the "
    "stern long-haired Hyuga clan head and the man with the long pineapple ponytail among them — "
    "never a fresh set of younger figures.",
  R("naruto_v4_black", "sasuke_16", "koharu", "homura", "tsunade", "hiashi", "shikaku",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 2: who grants a clan --------------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + DAN.format(i=3)
  + KOHARU.format(i=4) + HIASHI.format(i=5) + ENV.format(i=6)
  + ONLY(BOY16, SAS16, HAWK, KOH, HIA, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_OFF +
  "SIX panels. The argument moves from manners to the legal boundary around clan succession.\n"
  "PANEL 1 (top right): tight three-quarter view of the bandaged old man on the west arc, his "
  "visible eye aimed screen-right and diagonally south-east.\n"
  "PANEL 2 (top centre): the blond teen seen squarely over the Uchiha crest on the chair back.\n"
  "PANEL 3 (top left): the elderly female adviser's palm lands flat on the table.\n"
  "PANEL 4 (middle right): the blond teen looks toward her without turning his shoulders away from "
  "the north head.\n"
  "PANEL 5 (middle left): the stern long-haired clan head sits rigid on the east arc, pale eyes "
  "moving from her to the blond teen.\n"
  "PANEL 6 (bottom band, full width): wide room reaction — advisers still west at reader-left, "
  "clan heads still east at reader-right, nobody backing her claim over clan succession; the blond "
  "teen is at the southeast place with the dark-haired teen behind his right shoulder. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "YOU CLAIM CLAN HEADSHIP?"),
        (2, BOY16, "upper right", "I AM SITTING IN THE ANSWER."),
        (3, KOH, "upper right", "WE GAVE NO CONSENT."),
        (4, BOY16, "upper right", "SINCE WHEN DO ADVISERS SELECT CLAN HEADS?"),
        (5, HIA, "upper right", "CLAN SUCCESSION IS A CLAN MATTER."),
        (6, BOY16, "lower right of the panel, immediately ABOVE the blond teen's head at "
            "the near southeast place", "NOTHING HERE REQUIRES YOUR PERMISSION."))
  + "The stern long-haired Hyuga clan head with the pale pupil-less eyes sits on the EAST arc at "
    "reader-RIGHT in PANELS 5 and 6 — never on the west arc, never beside the bandaged old man or "
    "the elderly female adviser, and never among the advisers in any shot. Every seated clan head "
    "has a fully drawn face with eyes, nose and mouth; none is blank, featureless or smoothed "
    "over. In PANEL 6 the balloon \"NOTHING HERE REQUIRES YOUR PERMISSION.\" belongs to the "
    "BLOND TEEN at the near southeast place. Place that balloon LOW IN THE PANEL, directly "
    "above his head, and draw a SHORT tail straight down to his mouth. It must not sit up in "
    "the top corner of the panel, and its tail must never stop in empty air over the table "
    "or end on a clan head seated on the east arc.",
  R("naruto_v4_black", "sasuke_16", "danzo", "koharu", "hiashi",
    "env_konoha_council_chamber"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + KOHARU.format(i=1) + TSUNADE.format(i=2) + N16_BLACK.format(i=3)
  + SASUKE16.format(i=4) + ENV.format(i=5)
  + ONLY(KOH, TSU, BOY16, SAS16, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N
  + EYES_S_OFF +
  "SIX panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page is "
  "divided into horizontal TIERS that each run the full width of the paper, stacked top to bottom, "
  "separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier the "
  "panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. This page has EXACTLY SIX panels in a "
  "two-column, three-tier grid and no seventh panel of any kind. TIER 1 holds PANEL 1 at the RIGHT "
  "and PANEL 2 at the LEFT. TIER 2 holds PANEL 3 at the RIGHT and PANEL 4 at the LEFT. TIER 3 "
  "holds PANEL 5 at the RIGHT and PANEL 6 at the LEFT. PANEL 4 is the drawn close-up of the blond "
  "teen's eyes and its balloon sits INSIDE that same panel — never in a separate strip of its own. "
  "The Hokage keeps authority over the meeting and refuses ownership of the clan.\n"
  "PANEL 1 (top right): the elderly female adviser turns north from the west arc toward the north "
  "head, presenting her back to the southeast place.\n"
  "PANEL 2 (top left): the blonde woman front-on, hands folded over an illegibly marked agenda.\n"
  "PANEL 3 (middle right): the female adviser looks back screen-right and south-east, jaw tight.\n"
  "PANEL 4 (middle left): close on the blond teen's EYES only, calm tomoe centred on her; his "
  "mouth is outside this frame.\n"
  "PANEL 5 (bottom right): low three-quarter view of the blond teen in the chair, the fan crest "
  "filling the chair back behind his head.\n"
  "PANEL 6 (bottom left): the blonde woman raises two fingers and the room's eye-lines snap north "
  "to her. " + L_CHAMBER
  + SAY((1, KOH, "upper right", "HOKAGE-SAMA, WILL YOU ALLOW THIS?"),
        (2, TSU, "upper right", "THE HOKAGE DOES NOT APPOINT CLAN HEADS."),
        (3, KOH, "upper right", "A CHAIR DOES NOT MAKE THIS BOY OUR EQUAL."),
        (4, OFF(BOY16), "upper right", "THE CLAN DOES."),
        (5, BOY16, "upper right", "AND ITS HEAD IS NOT 'BOY' TO AN ADVISER."),
        (6, TSU, "upper right", "THE UCHIHA SEAT STANDS. THE MEETING BEGINS."))
  + "PANEL 2's balloon reads exactly \"THE HOKAGE DOES NOT APPOINT CLAN HEADS.\" — the word CLAN "
    "is present, spelled C-L-A-N, and the whole line is lettered complete. It must never read "
    "\"THE HOKAGE DOES NOT APPOINT HEADS.\" PANEL 4 is a fully drawn close-up of the blond teen's "
    "eyes and brow with its off-panel balloon \"THE CLAN DOES.\" inside it; no panel on this page "
    "is left blank, beige or unrendered. In PANEL 6 the only blond person in the chamber is the "
    "one SEATED in the carved Uchiha chair — the figure standing at his right shoulder is the "
    "DARK-HAIRED teen with black upswept hair and the Uchiha fan on his back, never a second "
    "blond in a spiral shirt.",
  R("koharu", "tsunade", "naruto_v4_black", "sasuke_16", "env_konoha_council_chamber"), "low"),

 # ---- Spread 3: security or possession ---------------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + DAN.format(i=1) + HOMURA.format(i=2) + N16_BLACK.format(i=3)
  + SHIKAKU.format(i=4) + SASUKE16.format(i=5) + ENV.format(i=6)
  + ONLY(HAWK, HOM, BOY16, SHIK, SAS16, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N
  + EYES_S_OFF +
  "SIX panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page is "
  "divided into horizontal TIERS that each run the full width of the paper, stacked top to bottom, "
  "separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier the "
  "panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT, PANEL 3 in the CENTRE and PANEL 4 at the LEFT. TIER 3, the bottom "
  "tier, holds PANEL 5 at the RIGHT and PANEL 6 at the LEFT, both wholly below tier 2. The demand "
  "for his training history is forced into the open as a security claim.\n"
  "PANEL 1 (top band, full width): the bandaged old man's HAND taps the first item on the "
  "illegible agenda sheet already lying before him on the west arc; his face and mouth are outside "
  "this frame and nothing moves across the table.\n"
  "PANEL 2 (tier 2, RIGHT): the male adviser raises ONE finger — the first of three points, a "
  "single finger up and no others.\n"
  "PANEL 3 (tier 2, CENTRE): the same angle a moment later — a SECOND finger joins the first, TWO "
  "fingers now raised.\n"
  "PANEL 4 (tier 2, LEFT): the same angle again — a THIRD finger joins them, THREE fingers now "
  "raised and pointing across the table. The count rises one, two, three with the reading order "
  "and never counts down.\n"
  "PANEL 5 (bottom right): the blond teen answers from the southeast seat without touching any "
  "document.\n"
  "PANEL 6 (bottom left): the man with the long pineapple ponytail props one elbow on the northern "
  "end of the east arc and looks screen-left toward the west arc rather than south. " + L_CHAMBER
  + SAY((1, OFF(HAWK), "upper right", "FIRST: NARUTO'S DISAPPEARANCE."),
        (2, HOM, "upper right", "WHY DID YOU LEAVE WITHOUT JIRAIYA?"),
        (3, HOM, "upper right", "HOW DID YOU LEAVE UNSEEN?"),
        (4, HOM, "upper right", "WHERE DID YOU TRAIN?"),
        (5, BOY16, "upper right", "I DID NOT NEED JIRAIYA. MY METHOD IS PRIVATE. MY LOCATION IS NOT YOURS."),
        (6, SHIK, "upper right", "IS THIS DISCIPLINE, OR AN INTELLIGENCE INQUIRY?"))
  + "PANELS 2, 3 and 4 run RIGHT TO LEFT across the middle row and the finger count RISES with "
    "the reading order: PANEL 2 at reader-RIGHT shows ONE finger raised, PANEL 3 in the centre "
    "shows TWO, and PANEL 4 at reader-LEFT shows THREE pointing across the table. Never count "
    "down. PANEL 5 (the blond teen's answer) opens the BOTTOM row at reader-RIGHT and PANEL 6 "
    "(\"IS THIS DISCIPLINE, OR AN INTELLIGENCE INQUIRY?\") sits to its LEFT in that same bottom "
    "row, so the answer is read before the question about it.",
  R("danzo", "homura", "naruto_v4_black", "shikaku", "sasuke_16",
    "env_konoha_council_chamber"), "low"),

 ("p06", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=6),
  FILL + RTL + DAN.format(i=1) + SHIKAKU.format(i=2) + KOHARU.format(i=3) + HOMURA.format(i=4)
  + N16_BLACK.format(i=5) + TSUNADE.format(i=6) + SASUKE16.format(i=7) + HIASHI.format(i=8)
  + ENV.format(i=9)
  + ONLY(HAWK, SHIK, KOH, HOM, BOY16, TSU, SAS16, HIA, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N
  + EYES_S_OFF +
  "SIX panels. The advisers are made to reveal that they are exercising command, not advising.\n"
  "PANEL 1 (top right): the bandaged old man, chin slightly raised.\n"
  "PANEL 2 (top centre): the man with the long pineapple ponytail moves his eyes north toward the "
  "table head.\n"
  "PANEL 3 (top left): the elderly female adviser cuts in before the north head can respond.\n"
  "PANEL 4 (middle right): the blond teen's gaze shifts along the adviser row from the bandaged "
  "old man to her.\n"
  "PANEL 5 (middle left): tight on the female and male advisers sharing one frame, the bandaged "
  "old man a blurred vertical behind them. The blond teen is NOT drawn in this panel.\n"
  "PANEL 6 (bottom band, full width): long south-side master-axis view angled slightly upward "
  "toward the blonde woman at the far north head; the blond teen holds the near southeast place "
  "with the dark-haired teen behind his right shoulder, advisers west at reader-left and clan "
  "heads "
  "east at reader-right, with no mirrored side. His distant mouth stays visible. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "VILLAGE SECURITY."),
        (2, SHIK, "upper right", "THEN THE HOKAGE'S FINDING MATTERS."),
        (3, KOH, "upper right", "THE VILLAGE MUST CONTROL ITS SHINOBI."),
        (4, BOY16, "upper right", "THE VILLAGE HAS A HOKAGE."),
        (5, OFF(BOY16), "upper right", "YOU SPEAK AS IF HER SHINOBI ARE YOURS."),
        (6, BOY16, "lower right of the panel, immediately ABOVE the blond teen's head at "
            "the near southeast place", "WHICH PART OF THIS IS ADVICE?"))
  + "In PANEL 5 the blond teen is NOT drawn, so \"YOU SPEAK AS IF HER SHINOBI ARE YOURS.\" is an "
    "off-panel balloon whose short spur runs UP to the TOP panel border and stops on the border "
    "line, pointing out of the panel; it must never touch or aim down at the male or female "
    "adviser drawn inside it. In PANEL 6 \"WHICH PART OF THIS IS ADVICE?\" belongs to the "
    "BLOND TEEN at the near southeast place. Place that balloon LOW IN THE PANEL, directly "
    "above his head, with a SHORT tail running straight down to his visible mouth. It must "
    "not sit up in the top corner of the panel, and its tail must never end on a clan head "
    "seated on the east arc or on the dark-haired teen behind his shoulder. The east arc in PANEL "
    "6 holds individually distinct "
    "clan heads in clan robes, including the stern long-haired Hyuga clan head and the man with "
    "the long pineapple ponytail — never four identical ninja in matching green flak vests.",
  R("danzo", "shikaku", "koharu", "homura", "naruto_v4_black", "tsunade", "sasuke_16",
    "hiashi", "env_konoha_council_chamber"), "medium"),

 # ---- Spread 4: the answer they cannot take ----------------------------------------
 ("p07", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + HOMURA.format(i=1) + SASUKE16.format(i=2) + N16_BLACK.format(i=3)
  + DAN.format(i=4) + TSUNADE.format(i=5) + ENV.format(i=6)
  + ONLY(HOM, SAS16, BOY16, HAWK, TSU, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_OFF +
  "SIX panels. The threat to invade his mind becomes the advisers' overreach.\n"
  "PANEL 1 (top right): the male adviser leans forward from the west arc; his reflection in the "
  "continuous tabletop points south-east.\n"
  "PANEL 2 (top left): the dark-haired teen bends from behind the blond teen's right shoulder, "
  "mouth near his ear; the blond teen does not turn.\n"
  "PANEL 3 (middle right): the male adviser's glasses go opaque as he issues the threat.\n"
  "PANEL 4 (middle left): the blond teen's three tomoe stay perfectly still, his mouth barely "
  "moving at the lower edge of frame.\n"
  "PANEL 5 (bottom right): the bandaged old man watches without joining the forward lean.\n"
  "PANEL 6 (bottom left): the blond teen angles his head just enough to put the old man in a "
  "direct eye-line. " + L_CHAMBER
  + SAY((1, HOM, "upper right", "A CHILD WHO DEFIES HIS ELDERS DOES NOT DESERVE THAT SEAT."),
        (2, SAS16, "upper right", "YOU ARE ENJOYING THIS."),
        (3, HOM, "upper right", "ANSWER, OR WE WILL TAKE THE ANSWER FROM YOUR MIND."),
        (4, BOY16, "upper right", "YOU CANNOT."),
        (5, HAWK, "upper right", "UNACCOUNTED POWER IS A THREAT."),
        (6, BOY16, "upper right", "ARE YOU NAMING THE UCHIHA CLAN HEAD A THREAT TO KONOHA?"))
  + "Every balloon is lettered in SOLID BLACK at full weight on EVERY line: no line is drawn "
    "faded, grey, hollow or outline-only, and \"UNACCOUNTED POWER IS A THREAT.\" is fully inked "
    "across all of its lines. In PANEL 1 the table is ONE continuous unbroken oval with a single "
    "smooth rim, never split into separate slabs or disjointed sections. EXACTLY TWO PEOPLE "
    "occupy the near southeast place in PANEL 1: ONE blond teen seated in the carved Uchiha "
    "chair and ONE dark-haired teen standing behind his right shoulder. There is no second "
    "blond head, no second black shirt with a red Uzumaki spiral, and no third figure of any "
    "kind in that corner of the room. Only those two wear the Uchiha fan crest; no extra "
    "figure stands in the foreground with a fan crest on his back, and nobody else in the "
    "chamber carries that crest at all.",
  R("homura", "sasuke_16", "naruto_v4_black", "danzo", "tsunade",
    "env_konoha_council_chamber"), "low"),

 ("p08", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + RTL + DAN.format(i=1) + N16_BLACK.format(i=2) + KOHARU.format(i=3)
  + TSUNADE.format(i=4) + SHIKAKU.format(i=5) + HIASHI.format(i=6) + SASUKE16.format(i=7)
  + ENV.format(i=8)
  + ONLY(HAWK, BOY16, KOH, TSU, SHIK, HIA, SAS16, ATTEND) + SEATING + CAST + DOCS + BLACKFIT
  + EYES_N + EYES_S_OFF +
  "SIX panels. The competent authority has already settled the matter and the clan heads close "
  "ranks around procedure.\n"
  "PANEL 1 (top right): the bandaged old man's visible eye narrows, declining the trap.\n"
  "PANEL 2 (top centre): the blond teen settles back a fraction.\n"
  "PANEL 3 (top left): the elderly female adviser pivots north.\n"
  "PANEL 4 (middle right): the blonde woman keeps one hand flat on the illegible agenda.\n"
  "PANEL 5 (middle left): the man with the long pineapple ponytail speaks from the northern east "
  "arc; the stern long-haired clan head is visible farther south on the same side, both looking "
  "north.\n"
  "PANEL 6 (bottom band, full width): the bandaged old man turns from the first agenda line to the "
  "statute copy already lying before him on the west arc, his face angled away and his mouth out "
  "of frame; the blond teen remains at the far southeast place and NO document crosses the oval. "
  + L_CHAMBER
  + SAY((1, HAWK, "upper right", "I AM NAMING A QUESTION."),
        (2, BOY16, "upper right", "THEN ASK THE HOKAGE. SHE SETTLED IT YESTERDAY."),
        (3, KOH, "upper right", "IS THAT TRUE?"),
        (4, TSU, "upper right", "YES. AND I WILL NOT SHARE A PRIVATE SECURITY DISCUSSION."),
        (5, SHIK, "upper right", "THEN THERE IS NO UNRESOLVED FINDING BEFORE THIS COUNCIL."),
        (5, HIA, "upper left", "AGREED."),
        (6, OFF(HAWK), "upper right", "THEN WE WILL DISCUSS THE CLAN'S SURVIVAL."))
  + "In PANEL 5 the two east-arc speakers are clearly drawn as SEPARATE men: the man with the "
    "long pineapple ponytail at the northern end of the arc, and the stern long-haired Hyuga clan "
    "head with the pale pupil-less eyes farther south on the same arc. \"AGREED.\" is the HYUGA "
    "clan head's line and carries its own clearly drawn tail running to HIS mouth — never "
    "tail-less, never resting on the ponytailed man's chest, who speaks only \"THEN THERE IS NO "
    "UNRESOLVED FINDING BEFORE THIS COUNCIL.\"",
  R("danzo", "naruto_v4_black", "koharu", "tsunade", "shikaku", "hiashi", "sasuke_16",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 5: a village supply of eyes -------------------------------------------
 ("p09", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + DAN.format(i=1) + HIASHI.format(i=2) + N16_BLACK.format(i=3)
  + SASUKE16.format(i=4) + TSUNADE.format(i=5) + KOHARU.format(i=6) + HOMURA.format(i=7)
  + ENV.format(i=8)
  + ONLY(HAWK, HIA, BOY16, SAS16, TSU, KOH, HOM, ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_OFF +
  "FIVE panels. The Act is put before the room and the preservation premise is accepted.\n"
  "PANEL 1 (top band, full width): the bandaged old man opens his OWN council copy of the statute "
  "on the west arc; the matching copy already lying at the Uchiha place stays untouched and no "
  "document crosses the table.\n"
  "PANEL 2 (middle right): he looks screen-right toward the southeast place.\n"
  "PANEL 3 (middle centre): insert on his finger resting on the illegible statute text — hand and "
  "paper only, no face and no mouth.\n"
  "PANEL 4 (middle left): the stern long-haired clan head on the east arc looks diagonally south.\n"
  "PANEL 5 (bottom band, full width): full oval-table reaction — the clan heads stay composed and "
  "nobody voices opposition; the blond teen faces north-west from the near-right place with the "
  "dark-haired teen fixed behind his right shoulder; the blonde woman holds the north head. "
  + L_CHAMBER
  + SAY((1, HAWK, "upper right", "TWO UCHIHA REMAIN."),
        (2, HAWK, "upper right", "KONOHA CANNOT ALLOW THE SHARINGAN TO DISAPPEAR."),
        (3, OFF(HAWK), "upper right", "THE CLAN RESTORATION ACT EXISTS FOR THIS."),
        (4, HIA, "upper right", "RESTORING A FOUNDING CLAN STRENGTHENS KONOHA."),
        (5, OFF(HAWK), "upper right", "THE PREMISE IS ACCEPTED."))
  + "The west arc in PANEL 5 carries the bandaged old man, the elderly female adviser with the "
    "pale hair bun and the elderly male adviser in the small round glasses, all three clearly "
    "recognisable in their fixed seats — never two unnamed grey-haired men in their places. In "
    "PANEL 5 the bandaged old man's mouth is not in frame, so \"THE PREMISE IS ACCEPTED.\" is an "
    "off-panel balloon whose spur runs LEFT to the WEST edge of the panel and stops on the border "
    "line; it must never reach down onto a clan head on the east arc at reader-right.",
  R("danzo", "hiashi", "naruto_v4_black", "sasuke_16", "tsunade", "koharu", "homura",
    "env_konoha_council_chamber"), "medium"),

 ("p10", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=3),
  FILL + RTL + DAN.format(i=1) + HOMURA.format(i=2) + N16_BLACK.format(i=3)
  + SASUKE16.format(i=4) + KOHARU.format(i=5) + ENV.format(i=6)
  + ONLY(HAWK, HOM, BOY16, SAS16, KOH, ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N +
  "THREE panels. The weapon logic is stated plainly and the dark-haired teen's restrained anger "
  "becomes visible.\n"
  "PANEL 1 (top right): the bandaged old man indicates two dark tokens on an unreadable strategic "
  "map kept on the west arc; every mark on it is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 2 (top left): the male adviser looks across the oval at the Uchiha crest rather than at "
  "either face.\n"
  "PANEL 3 (bottom band, full width, dominant, the focal panel): the eye-activation panel — the "
  "blond teen stays seated at the southeast place in foreground right; behind his right shoulder "
  "the dark-haired teen's eyes turn RED with three black tomoe locking into place. The west-arc "
  "advisers sit in his north-west sightline. He does not move, speak or step forward. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "KUMO FIELDS TWO JINCHŪRIKI WHO COMMAND THEIR BIJŪ."),
        (1, HAWK, "upper left", "KONOHA MUST PRESERVE EVERY POWER IT HAS."),
        (2, HOM, "upper right", "THE FUTURE SHARINGAN ARE A VILLAGE INTEREST."),
        (3, BOY16, "upper right", "SAY IT PLAINLY."),
        (3, BOY16, "upper left", "YOU WANT THEIR CHILDREN AS FUTURE WEAPONS."))
  + "In PANEL 3 there is EXACTLY ONE blond figure on the whole page: the blond teen seated in the "
    "carved Uchiha chair at the southeast place in foreground right. The west adviser arc holds "
    "only the bandaged old man, the elderly female adviser and the elderly male adviser in dark "
    "formal robes — no blond figure, no black shirt with a red Uzumaki spiral, and no duplicate "
    "of the blond teen sits anywhere on the west or east arc or between an adviser and the table.",
  R("danzo", "homura", "naruto_v4_black", "sasuke_16", "koharu",
    "env_konoha_council_chamber"), "high"),

 # ---- Spread 6: attachments --------------------------------------------------------
 ("p11", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + HOMURA.format(i=3)
  + HIASHI.format(i=4) + SHIKAKU.format(i=5) + TSUNADE.format(i=6) + ENV.format(i=7)
  + ONLY(BOY16, SAS16, HOM, HIA, SHIK, TSU, EAST_HAND_D, EAST_GLASS_D, ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FIVE panels. The proposal expands from preservation to inter-clan marriage and attachment. The "
  "two east-arc speakers are ordinary unnamed clan heads and must not resemble any other named "
  "character on the page.\n"
  "PANEL 1 (top right): the open-handed clan head opens one hand from the east arc at "
  "reader-right.\n"
  "PANEL 2 (top left): the clan head in dark round glasses sits beside the other clan heads, his "
  "lenses reflecting the two Uchiha.\n"
  "PANEL 3 (middle right): SILENT — the dark-haired teen stays behind the blond teen's right "
  "shoulder, his active red eyes fixed north-west on the speakers; he does not move or interrupt. "
  "No text in this panel.\n"
  "PANEL 4 (middle left): the blond teen finishes the unspoken conclusion from the Uchiha seat.\n"
  "PANEL 5 (bottom band, full width): the male adviser nods toward the east arc, then recognizes "
  "that the blond teen spoke. " + L_CHAMBER
  + SAY((1, EAST_HAND, "upper right", "THEN LET THEM MARRY FROM THE CLANS ALREADY HERE."),
        (2, EAST_GLASS, "upper right", "IT CREATES HEALTHY RELATIONSHIPS."),
        (2, EAST_GLASS, "upper left", "ATTACHMENTS MAKE DEPARTURE COSTLY."),
        (4, BOY16, "upper right", "REDUCING THE CHANCE OF BETRAYAL."),
        (5, HOM, "upper right", "EXACTLY."))
  + "In PANEL 1 the open-handed clan head is ONE SPECIFIC seated man on the east arc — a broad "
    "adult in pale clan robes, plainly distinct from every other figure in the room — and \"THEN "
    "LET THEM MARRY FROM THE CLANS ALREADY HERE.\" carries a tail that ends on HIS mouth. The "
    "stern long-haired Hyuga clan head and the man with the long pineapple ponytail are also "
    "seated on that arc and say nothing. In PANEL 5 \"EXACTLY.\" belongs to the elderly male "
    "adviser in the small round glasses on the WEST arc: its tail must END ON HIS MOUTH and never "
    "stop in mid-air over the table, over an empty seat, or short of any figure.",
  R("naruto_v4_black", "sasuke_16", "homura", "hiashi", "shikaku", "tsunade",
    "env_konoha_council_chamber"), "low"),

 ("p12", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=4),
  FILL + RTL + HIASHI.format(i=1) + N16_BLACK.format(i=2) + DAN.format(i=3)
  + TSUNADE.format(i=4) + SASUKE16.format(i=5) + ENV.format(i=6)
  + ONLY(HIA, BOY16, HAWK, TSU, SAS16, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. He accepts that the clan must survive and refuses council ownership of the "
  "method.\n"
  "PANEL 1 (top right): the stern long-haired clan head stays formal on the east arc, pale gaze on "
  "the southeast place.\n"
  "PANEL 2 (top left): the blond teen's hand rests on the carved Uchiha chair arm, his face and "
  "mouth in frame above it.\n"
  "PANEL 3 (middle right): the bandaged old man closes his hand over his own copy of the statute "
  "without moving it from the west arc.\n"
  "PANEL 4 (bottom band, full width): the blond teen turns his eyes north-north-west toward the "
  "north head; the east-arc clan heads and west-arc advisers follow that new diagonal a beat "
  "later, "
  "seen mostly from behind. The dark-haired teen holds his mark with red eyes. " + L_CHAMBER
  + SAY((1, HIA, "upper right", "A CLAN HEAD CANNOT IGNORE EXTINCTION."),
        (2, BOY16, "upper right", "I AM NOT IGNORING IT."),
        (2, BOY16, "upper left", "I AM REFUSING YOUR OWNERSHIP OF THE ANSWER."),
        (3, HAWK, "upper right", "THEN OFFER SECURITY THIS COUNCIL CAN ENFORCE."),
        (4, BOY16, "lower centre of the panel, immediately ABOVE the blond teen's head at "
            "the near southeast place", "APPLY YOUR PRECEDENT CONSISTENTLY."))
  + "In EVERY panel where the blond teen's eye is visible, including the PANEL 2 view of his face "
    "above the carved chair arm, his visible left eye is the RED ordinary three-tomoe Sharingan — "
    "never plain blue, never grey, never a dark eye. In PANEL 4 \"APPLY YOUR PRECEDENT "
    "CONSISTENTLY.\" belongs to the BLOND TEEN at the near southeast place. Place that "
    "balloon LOW IN THE PANEL, directly above his head, with a SHORT tail running straight "
    "down to his mouth. It must not sit up in the top corner, and its tail must never end on "
    "the dark-haired teen behind his right shoulder or on a clan head on the east arc.",
  R("hiashi", "naruto_v4_black", "danzo", "tsunade", "sasuke_16",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 7: the last Senju -----------------------------------------------------
 ("p13", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=4),
  FILL + RTL + N16_BLACK.format(i=1) + TSUNADE.format(i=2) + SASUKE16.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, TSU, SAS16,
         "the west-arc advisers and east-arc clan heads seen from behind or in lost profile, none "
         "of them individually recognisable", ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT and PANEL 3 at the LEFT. TIER 3 is PANEL 4 alone, full width. The "
  "Act's own principle is made to touch the last member of the other founding "
  "clan.\n"
  "PANEL 1 (top band, full width): long diagonal from BEHIND the blond teen at the southeast place "
  "to the blonde woman at the north head; his head and shoulders are seen from the back and his "
  "mouth is not visible anywhere in this panel.\n"
  "PANEL 2 (middle right): SILENT — the adviser and clan-head arcs turn north, the accepted "
  "premise now pointing at the north head. No text in this panel.\n"
  "PANEL 3 (middle left): SILENT — the blonde woman's fingers stop over her agenda. No text in "
  "this panel.\n"
  "PANEL 4 (bottom band, full width): the blond teen in near-right profile with his mouth clearly "
  "visible, the blonde woman held small in the distance along his north-north-west eye-line. "
  + L_CHAMBER
  + SAY((1, OFF(BOY16), "upper right", "THE HOKAGE IS THE LAST SENJU."),
        (1, OFF(BOY16), "upper left", "PLACE HER UNDER THE SAME ACT."),
        (4, BOY16, "upper right", "IF FOUNDING BLOOD MUST SURVIVE, WHY WAS THIS NOT RAISED WHEN SHE RETURNED?"))
  + "In PANEL 4 the blond teen is in NEAR-RIGHT PROFILE with his mouth clearly visible, and the "
    "balloon \"IF FOUNDING BLOOD MUST SURVIVE, WHY WAS THIS NOT RAISED WHEN SHE RETURNED?\" "
    "carries a clearly drawn tail that ends AT HIS MOUTH; it is never tail-less and never floats "
    "between two figures. The dark-haired teen is NOT drawn in PANEL 4 at all. In PANEL 1 the "
    "blond teen is seen from BEHIND with no mouth in frame, so both balloons are off-panel "
    "balloons whose short spurs run to the RIGHT panel border and stop on the border line, "
    "touching and aiming at no figure inside the panel.",
  R("naruto_v4_black", "tsunade", "sasuke_16", "env_konoha_council_chamber"), "low"),

 ("p14", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + N16_BLACK.format(i=2) + SASUKE16.format(i=3)
  + ENV.format(i=4)
  + ONLY(TSU, BOY16, SAS16, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. The application is rejected, answered, and turned back to the statute.\n"
  "PANEL 1 (top band, full width, dominant): frontal panel of the blonde woman at the north head, "
  "both palms flat on the table.\n"
  "PANEL 2 (middle right): her jaw tightens.\n"
  "PANEL 3 (middle left): the blond teen answers without triumph.\n"
  "PANEL 4 (bottom band, full width): she points diagonally south-east toward the southeast place, "
  "reasserting control of the meeting. " + L_CHAMBER
  + SAY((1, TSU, "upper right", "DO NOT EVEN THINK ABOUT IT."),
        (1, TSU, "upper left", "IT WILL NOT HAPPEN."),
        (2, TSU, "upper right", "I AM PAST THE AGE FOR CHILDREN."),
        (3, BOY16, "upper right", "A CIVILIAN MIGHT BE."),
        (3, BOY16, "upper left", "THE GREATEST MEDICAL NINJA IS NOT."),
        (4, TSU, "upper right", "ANSWER THE PROPOSAL DIRECTLY, NARUTO."))
  + "In PANEL 4, and in every panel where the southeast place is in frame, the DARK-HAIRED TEEN "
    "is drawn at his fixed mark one pace behind the blond teen's right shoulder, plainly present "
    "although he speaks nothing on this page. The southeast place is never shown with that mark "
    "empty and the blond teen is never alone in it.",
  R("tsunade", "naruto_v4_black", "sasuke_16", "env_konoha_council_chamber"), "low"),

 # ---- Spread 8: consent for now ----------------------------------------------------
 ("p15", dict(scene="emotional_closeup", light="day", cast="solo", mood="tense", panels=3),
  FILL + RTL + N16_BLACK.format(i=1) + ENV.format(i=2) + ONLY(BOY16, ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N +
  "THREE panels. The objection becomes an operative refusal.\n"
  "PANEL 1 (top band, full width): the blond teen draws the pre-positioned Uchiha-seat copy of the "
  "statute closer by a few inches; it never leaves the southeast section of tabletop. His finger "
  "stops beside an illegible clause.\n"
  "PANEL 2 (bottom right, tall): the blond teen with the Uchiha crest filling the chair back "
  "behind him.\n"
  "PANEL 3 (bottom left, tall): large still close-up of his face and ordinary three-tomoe "
  "Sharingan. " + L_CHAMBER
  + SAY((1, BOY16, "upper right", "THE ACT CANNOT COMPEL SOMEONE UNDER EIGHTEEN WITHOUT CONSENT."),
        (2, BOY16, "upper right", "I AM UNDER EIGHTEEN."),
        (2, BOY16, "upper left", "TODAY, IT REQUIRES MY AGREEMENT."),
        (3, BOY16, "upper right", "I REFUSE COMPULSORY ENROLLMENT."))
  + "In PANEL 3 the blond teen's hair is clean flat inked hair only: there is no second face, no "
    "partial or fragmentary face, and nothing smeared or garbled hidden inside or at the edge of "
    "it. Exactly ONE face appears in that panel. In PANEL 2 the carved chair back behind him "
    "carries exactly ONE clean, correctly proportioned Uchiha fan crest and his shirt carries "
    "exactly ONE red Uzumaki spiral — never a doubled, stacked, duplicated or malformed second "
    "emblem anywhere.",
  R("naruto_v4_black", "env_konoha_council_chamber"), "low"),

 ("p16", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=4),
  FILL + RTL + DAN.format(i=1) + N16_BLACK.format(i=2) + HOMURA.format(i=3)
  + SASUKE16.format(i=4) + TSUNADE.format(i=5) + ENV.format(i=6)
  + ONLY(HAWK, BOY16, HOM, SAS16, TSU, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 holds PANEL 1 at the RIGHT and "
  "PANEL 2 at the LEFT, side by side and the same height. TIER 2 is PANEL 3 alone, spanning the "
  "FULL WIDTH of the page beneath both of them. TIER 3 is PANEL 4 alone, full width. The page is "
  "never built as two vertical columns, and PANEL 3 never sits in a right-hand column directly "
  "under PANEL 1. The limit is named: a delay, not immunity.\n"
  "PANEL 1 (top right): the bandaged old man keeps his own statute copy beneath one hand on the "
  "west arc.\n"
  "PANEL 2 (top left): the blond teen meets his screen-left gaze.\n"
  "PANEL 3 (tier 2, a FULL-WIDTH band beneath panels 1 and 2): the male adviser touches the edge "
  "of the west-arc copy from his seat, the clear tabletop running away to either side of him.\n"
  "PANEL 4 (bottom band, full width): the blond teen keeps both the adviser arc and the clan-head "
  "arc in view without turning his chair; the bandaged old man's mouth stays visible on the west "
  "arc and the dark-haired teen holds his mark behind the right shoulder. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "THE CONSENT LIMIT ENDS AT EIGHTEEN."),
        (2, BOY16, "upper right", "THEN TODAY IS ALL THIS COUNCIL MAY RULE ON."),
        (3, HOM, "upper right", "THE COUNCIL MAY PRESENT SUITABLE CANDIDATES."),
        (4, BOY16, "upper right", "THE ACT DOES NOT CHOOSE WHOM I MARRY."),
        (4, BOY16, "upper left", "NEITHER DO YOU."),
        (4, HAWK, "lower left", "SASUKE. DOES YOUR ANSWER DIFFER?"))
  + "PANELS 1 and 2 form the TOP row — PANEL 1 (the bandaged old man) at reader-RIGHT and PANEL 2 "
    "(the blond teen's reply) at reader-LEFT. PANEL 3 (the male adviser, \"THE COUNCIL MAY "
    "PRESENT SUITABLE CANDIDATES.\") opens the MIDDLE row at reader-RIGHT, entirely BELOW both of "
    "them; it must never sit beside or above PANEL 2, so the council's offer is read after the "
    "blond teen's reply, not before it.",
  R("danzo", "naruto_v4_black", "homura", "sasuke_16", "tsunade",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 9: Sasuke's family ----------------------------------------------------
 ("p17", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + DAN.format(i=3)
  + TSUNADE.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, SAS16, HAWK, TSU,
         "the other west-arc advisers seen in lost profile, never individually recognisable", ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. He takes ownership of his own separate answer.\n"
  "PANEL 1 (top band, full width): the blond teen lifts two fingers toward his right without "
  "looking back; the dark-haired teen steps from behind his right shoulder AROUND THAT SAME SIDE "
  "to "
  "the outer southeast rim beside the chair. He never enters the table's interior and never "
  "crosses "
  "the blond teen's back.\n"
  "PANEL 2 (middle right): the dark-haired teen faces north-west toward the adviser arc, his "
  "Sharingan hard but controlled.\n"
  "PANEL 3 (middle left): the bandaged old man's visible eye sharpens; the dark-haired teen is NOT "
  "drawn in this panel and does not look to anyone for permission.\n"
  "PANEL 4 (bottom band, full width, dominant, the focal panel): the dark-haired teen at the blond "
  "teen's right side, his closed hand resting away from any weapon. " + L_CHAMBER
  + SAY((1, BOY16, "upper right", "SASUKE."),
        (2, SAS16, "upper right", "OUR ANSWERS DIFFER."),
        (2, SAS16, "upper left", "I WILL NOT BE COMPELLED INTO THE ACT."),
        (3, OFF(SAS16), "upper right", "I EXPECT TO MARRY BEFORE EIGHTEEN—VOLUNTARILY."),
        (4, SAS16, "upper right beside the dark-haired teen on the outer southeast rim, as "
            "the HIGHEST balloon in this panel", "YOU WILL NOT CHOOSE HER."),
        (4, SAS16, "directly BELOW the other balloon and still on the RIGHT of the panel "
            "beside the dark-haired teen", "AND YOU WILL NOT TREAT MY CHILDREN AS WEAPONS."))
  + "In PANEL 3 the dark-haired teen is NOT drawn, so \"I EXPECT TO MARRY BEFORE "
    "EIGHTEEN—VOLUNTARILY.\" is an off-panel balloon whose short spur runs to the nearest panel "
    "BORDER and stops on the border line; it must never touch, cross or aim at the bandaged old "
    "man's face, which is the only face in that panel. In PANEL 1 \"SASUKE.\" is spoken by the "
    "BLOND TEEN and its tail reaches HIS mouth, never the dark-haired teen he is calling. In "
    "PANEL 4 BOTH balloons belong to the DARK-HAIRED teen standing at the blond teen's right "
    "side, so BOTH sit on the RIGHT of the panel beside him and are stacked by HEIGHT: "
    "\"YOU WILL NOT CHOOSE HER.\" is the higher and is read first, and \"AND YOU WILL "
    "NOT TREAT MY CHILDREN AS WEAPONS.\" sits directly below it. Each carries a SHORT tail "
    "down to his mouth. Neither balloon is placed on the left of the panel and neither tail "
    "runs across the oval toward the advisers on the west arc.",
  R("naruto_v4_black", "sasuke_16", "danzo", "tsunade",
    "env_konoha_council_chamber"), "medium"),

 ("p18", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=4),
  FILL + RTL + HIASHI.format(i=1) + SASUKE16.format(i=2) + N16_BLACK.format(i=3)
  + KOHARU.format(i=4) + HOMURA.format(i=5) + DAN.format(i=6) + TSUNADE.format(i=7)
  + ENV.format(i=8)
  + ONLY(HIA, SAS16, BOY16, KOH, HOM, HAWK, TSU, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. Clan protection is defined around future children without pretending the statute "
  "has disappeared.\n"
  "PANEL 1 (top right): the stern long-haired clan head answers from the east arc.\n"
  "PANEL 2 (top left): the dark-haired teen holds his gaze from the outer southeast rim.\n"
  "PANEL 3 (middle band, full width): the blond teen remains seated; the dark-haired teen stands "
  "beside his right arm.\n"
  "PANEL 4 (bottom band, full width): compressed view across the oval to the west arc — the "
  "elderly female and male advisers glare and the bandaged old man is unreadable. Neither Uchiha "
  "is drawn in this panel. " + L_CHAMBER
  + SAY((1, HIA, "upper right", "RESTORING THE CLAN WAS YOUR STATED AIM."),
        (2, SAS16, "upper right", "RESTORING IT DOES NOT MAKE IT YOURS."),
        (3, BOY16, "upper right", "HIS CHILDREN WILL BE UCHIHA."),
        (3, BOY16, "upper left", "THE CLAN PROTECTS THEM FROM ANYONE WHO CLAIMS THEM."),
        (4, OFF(BOY16), "upper right", "BY THE TIME THEY ARE OUR AGE, YOU WILL LIKELY BE DEAD."))
  + "In PANEL 3 the north head is occupied by the BLONDE WOMAN IN THE GREEN HAORI — two long "
    "blonde tails, the dark diamond mark on her forehead — seated behind her low Hokage desk. She "
    "is never a grey-haired elder, never a stranger in dark robes, never malformed, and the north "
    "head is never deskless or empty. BOTH PANEL 3 balloons belong to the BLOND TEEN seated at "
    "the southeast place: draw each tail to HIS mouth, never onto the dark-haired teen beside him "
    "and never across to the west-arc advisers.",
  R("hiashi", "sasuke_16", "naruto_v4_black", "koharu", "homura", "danzo", "tsunade",
    "env_konoha_council_chamber"), "low"),

 # ---- Spread 10: a draw ------------------------------------------------------------
 ("p19", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=4),
  FILL + RTL + TSUNADE.format(i=1) + N16_BLACK.format(i=2) + SASUKE16.format(i=3) + ENV.format(i=4)
  + ONLY(TSU, BOY16, SAS16,
         "the west-arc advisers seen from behind or in lost profile, never individually "
         "recognisable", ATTEND)
  + SEATING + CAST + DOCS + BLACKFIT + EYES_N + EYES_S_ON +
  "FOUR panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT and PANEL 3 at the LEFT, side by side and the same height. TIER 3 "
  "is PANEL 4 alone, full width. The ruling closes the present proposal only.\n"
  "PANEL 1 (top band, full width): the blonde woman rises at the north head, the tallest figure in "
  "the chamber for the first time.\n"
  "PANEL 2 (middle right): the blond teen stays seated beside his untouched section of the statute "
  "copy; the north head is NOT drawn in this panel.\n"
  "PANEL 3 (middle left): the dark-haired teen stands beside the blond teen's right arm, Sharingan "
  "still active; the north head is NOT drawn in this panel.\n"
  "PANEL 4 (bottom band, full width): she looks from the west-arc advisers to the southeast Uchiha "
  "place. " + L_CHAMBER
  + SAY((1, TSU, "upper right", "ENOUGH."),
        (2, OFF(TSU), "upper right", "NARUTO IS UNDER EIGHTEEN AND DOES NOT CONSENT."),
        (2, OFF(TSU), "upper left", "HE WILL NOT BE ENTERED INTO THE ACT TODAY."),
        (3, OFF(TSU), "upper right", "SASUKE REFUSES COMPULSION AND HAS STATED HIS VOLUNTARY INTENT."),
        (4, TSU, "upper right", "NO SPOUSE IS ASSIGNED. THE PRESENT PROPOSAL ENDS HERE."))
  + "In PANELS 2 and 3 the blond teen's visible left eye is the RED ordinary three-tomoe "
    "Sharingan, never plain grey, blue or dark. PANEL 2 — the blond teen, carrying the ruling "
    "about him — sits at reader-RIGHT of the middle row and PANEL 3 — the dark-haired teen, "
    "carrying the ruling about him — sits to its LEFT, so the ruling on the blond teen is read "
    "first. The blonde woman is NOT drawn in either panel, so each of those balloons is an "
    "off-panel balloon whose spur runs UP to the TOP panel border and stops on the border line, "
    "pointing out of the panel and never down at the blond teen or the dark-haired teen.",
  R("tsunade", "naruto_v4_black", "sasuke_16", "env_konoha_council_chamber"), "low"),

 ("p20", dict(scene="dialogue", light="day", cast="crowd", mood="calm", panels=3),
  FILL + RTL + DAN.format(i=1) + SASUKE16.format(i=2) + TSUNADE.format(i=3)
  + N16_BLACK.format(i=4) + KOHARU.format(i=5) + HOMURA.format(i=6) + ENV.format(i=7)
  + ONLY(HAWK, SAS16, TSU, BOY16, KOH, HOM, ATTEND) + SEATING + CAST + DOCS + BLACKFIT + EYES_N +
  "THREE panels. LAST PAGE OF THE CHAPTER — a temporary draw flows straight into the next matter "
  "with no folder handoff and no time break.\n"
  "PANEL 1 (top right): the bandaged old man closes ONLY his own copy of the statute on the west "
  "arc; his hands touch no other document.\n"
  "PANEL 2 (top left): the dark-haired teen retraces the same short path around the blond teen's "
  "right side to the mark behind his right shoulder, and his Sharingan DEACTIVATES to ordinary "
  "dark "
  "eyes in this panel.\n"
  "PANEL 3 (bottom band, full width, dominant): master of the unchanged continuous oval — the "
  "blonde woman north, the three advisers west at reader-left, the clan heads east at "
  "reader-right, "
  "the blond teen at the southeast place facing north-west and the dark-haired teen behind his "
  "right shoulder with ordinary dark eyes. Nobody moves a folder or a paper. " + L_CHAMBER
  + SAY((1, HAWK, "upper right", "THE STATUTE REMAINS WHEN NARUTO TURNS EIGHTEEN."),
        (2, SAS16, "upper right", "A DRAW."),
        (3, TSU, "upper right", "I BELIEVE THAT SETTLES THE MATTER."),
        (3, TSU, "upper left", "GOOD. WE MOVE TO THE NEXT MATTER. DANZŌ?"))
  + "In PANEL 3 the bandaged old man — cane in his left hand, right arm wrapped and slung, right "
    "eye bandaged, X-shaped scar on his chin — is clearly drawn on the WEST arc in the seat "
    "NEAREST the north head, unmistakably present in this closing master. He is never absent from "
    "it and never replaced by an unnamed grey-haired man. The west arc holds him, the elderly "
    "female adviser and the elderly male adviser: exactly three.",
  R("danzo", "sasuke_16", "tsunade", "naruto_v4_black", "koharu", "homura",
    "env_konoha_council_chamber"), "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch12" / "raw", HERE / "v5ch12" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
