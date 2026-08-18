"""Volume 5, Chapter 11 — "Family". 18 pages.

Translated 1:1 from story/volume_05/drafts/ch11_family.md — every balloon, its panel, its
speaker, its stated position and its exact text. Reading order is RIGHT TO LEFT on every
multi-panel page. Source: fic ch15:401-639 and ch16:7-111.

MISSING REFERENCE SHEETS (report, never invent):
  * guren.png — page 14's borderless Oto report image. She is drawn as an unnamed,
    back-three-quarter site overseer until a sheet exists; add the sheet and bind her before
    generating page 14.
  * no interior plate exists for the Uchiha house (sitting room, kitchen, hallway). Pages 1,
    10, 15, 16, 17 and 18 bind env_uchiha_compound for architecture and palette only and
    state the interior in prose.
  * no ANBU mask sheet exists. The owl-masked messenger on pages 17-18 stays anonymous and
    is never unmasked, following the Root-agent precedent in build_v5ch01.py.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, DAN, ENV, FILL, HAWK, OFF, ONLY, R, SAY, SFX, ZET  # noqa: E402
from prompts_v4 import (GUNBAI_V4, HOMURA, KARIN, KOHARU, N16_ARMOR, N16_BLACK,   # noqa: E402
                        SASUKE16, YUGAO_V4, HOMURA_SPEAKER, KARIN_SPEAKER,
                        KOHARU_SPEAKER, N16_SPEAKER, SASUKE16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
SAS16 = SASUKE16_SPEAKER
KAR = KARIN_SPEAKER
YUG = YUGAO_V4_SPEAKER
KOH = KOHARU_SPEAKER
HOM = HOMURA_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")
ANBU = ("one owl-masked ANBU in a plain porcelain animal mask, grey armour and a short cloak, "
        "never unmasked and never individually recognisable")
ANBU_S = "the owl-masked ANBU"
ARMOUR = ("He wears his clean red segmented samurai armour over the black under-suit on this "
          "page, with the dark purple gunbai on his back. ")
SLEEP = ("On this page he is bare-chested in dark sleep shorts: no shirt, no armour, no forehead "
         "protector and no gunbai worn on his body. ")
BLACKFIT = ("He wears the fitted long-sleeved black shirt carrying BOTH the Uchiha fan crest and "
            "the Uzumaki spiral on its back, black trousers and black gloves — no armour, no "
            "forehead protector and no gunbai on his body. ")
ROOM = ("Karin's sitting room keeps ONE unbroken 180-degree axis on every page: the entrance and "
        "its floor seal array at frame RIGHT, the couch at frame LEFT, the low table between them, "
        "the red-haired girl on the left side, the dark-haired teen on the right side and the "
        "blond "
        "teen at the far centre beyond the table. The axis is never mirrored. ")
TABLE = ("The Uchiha kitchen table is one long horizontal axis: the dark-haired teen on frame LEFT "
         "with tea and a closed book, the blond teen on frame RIGHT. The axis is never mirrored. ")
# The page-QA gate found the same two defects again and again across this chapter: a balloon
# tailed to whoever stood nearest instead of its named speaker, and a balloon left tail-less on
# top of the wrong face. This is the chapter-wide law; every reissued page carries it.
TAILS = ("BALLOON TAILS ARE CHECKED ON THIS PAGE. Every balloon has ONE clearly drawn tail whose "
         "point ENDS AT ITS NAMED SPEAKER'S MOUTH. No balloon is tail-less, none carries a short "
         "stub that stops on a nearer character's head, hair, shoulder or sleeve, and none floats "
         "above a face it does not belong to. Where the named speaker stands on the far side of "
         "the panel from the balloon, the tail is drawn LONG and travels the whole way across to "
         "them, passing clear of every other face. An off-panel balloon's spur runs to the panel "
         "BORDER and stops on the border line, touching and aiming at no figure inside the panel. ")

L_SITTING = "Lighting: warm low evening lamplight in a wooden interior, deep quiet shadows. "
L_SEALED = ("Lighting: even indoor lamplight in a clean modern room; the faint blue seal lines in "
            "floor, window lattice and tabletop are the only cool accent. ")
L_NIGHT = "Lighting: cold blue night over the empty compound against one warm-lit doorway. "
L_ROOT = ("Lighting: one hard shaft from above into a windowless underground chamber; everything "
          "else falls to black. ")
L_MORNING = "Lighting: thin pale early-morning light through a shuttered window, colour drained. "
L_LAB = "Lighting: cold grey hideout stone with one low warm lamp over the steaming medicine pot. "
L_KITCHEN = "Lighting: flat clean morning light across a wooden kitchen table. "
L_DOORS = "Lighting: hard flat daylight on tall stone council doors, long shadows on the approach. "

PAGES = [
 # ---- Spread 1: inside the barrier -------------------------------------------------
 ("p01", dict(scene="dialogue", light="dusk", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + ARMOUR +
  "FIVE panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width, "
  "across the top of the page. TIER 2 holds PANEL 2 in its RIGHT half and PANEL 3 in its LEFT "
  "half. TIER 3, the bottom tier, holds PANEL 4 in its RIGHT half and PANEL 5 in its LEFT half. "
  "PANEL 4 therefore sits BELOW panels 2 and 3, never beside or above them. Image 3 supplies "
  "Uchiha architecture, palette and crest motifs only; this page is "
  "an INTERIOR sitting room in that compound, not a street.\n"
  "PANEL 1 (top band, full width): wide evening interior — the dark-haired teen sits at frame left "
  "with an open book; the blond teen stands at frame right in red armour just inside the garden "
  "doorway. Their eye-line runs flat across the low table between them. The UPPER LEFT wall of "
  "this panel is PROTECTED EMPTY NEGATIVE SPACE — no figure, object, effect or balloon may enter "
  "it — and carries only the chapter marker.\n"
  "PANEL 2 (middle right, vertical): medium on the dark-haired teen — he closes the book around "
  "one finger and looks up-left toward the blond teen.\n"
  "PANEL 3 (middle left, vertical): medium on the blond teen — his body is already angled toward "
  "the exit while his eyes stay rightward toward the dark-haired teen.\n"
  "PANEL 4 (bottom right, small horizontal): close on the dark-haired teen's hand shutting the "
  "book; his face is visible at the upper edge of the panel, eye-line left.\n"
  "PANEL 5 (bottom left, large horizontal): the blond teen stands frame right and the dark-haired "
  "teen has joined him at frame left inside the first curl of ORANGE-RED shunshin flame, drawn as "
  "flat opaque flame shapes. They face the same direction for the first time on the page. "
  + L_SITTING +
  'LETTERING: in the protected upper-left wall space of PANEL 1, write the chapter marker in bold '
  'upright English capitals on one line: "CHAPTER 11 — FAMILY". It is a tail-less title, not a '
  'balloon. '
  + SAY((1, BOY16, "upper right", "COME WITH ME."),
        (2, SAS16, "upper right", "WHERE?"),
        (3, BOY16, "upper right", "KARIN'S HOUSE."),
        (3, BOY16, "upper left", "THE COMPOUND IS NOT PRIVATE ENOUGH YET."),
        (4, SAS16, "upper right", "YOU GAVE HER YOUR HOUSE?"),
        (5, BOY16, "upper right", "I WASN'T USING IT."))
  + TAILS + "PANELS 2 and 3 occupy the ENTIRE middle row — PANEL 2 at reader-RIGHT, PANEL 3 at "
    "reader-LEFT — and PANEL 4 sits in the BOTTOM row at reader-RIGHT, wholly below both of them. "
    "No part of PANEL 4 may sit in the middle row or above PANEL 3, so the dark-haired teen's "
    "\"YOU GAVE HER YOUR HOUSE?\" is read AFTER the blond teen has said \"KARIN'S HOUSE.\", never "
    "before it.",
  R("naruto_v4_armor", "sasuke_16", "env_uchiha_compound"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "FIVE panels. The trust triangle is established and the room is proved secure.\n"
  "PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. Three horizontal "
  "tiers, each running the full width of the paper and separated by an unbroken horizontal "
  "gutter; inside a tier the panels read RIGHT TO LEFT. TIER 1 is PANEL 1 alone, full width. "
  "TIER 2 holds PANEL 2 — the medium three-shot in which the blond teen names them both — "
  "TOUCHING THE PAGE'S RIGHT MARGIN, and PANEL 3 — the close on the seated dark-haired teen "
  "— TOUCHING THE PAGE'S LEFT MARGIN. The three-shot is the right-hand panel of that tier "
  "and the single close-up is the left-hand one, never the other way round. TIER 3 holds "
  "PANEL 4 at the RIGHT and PANEL 5 at the LEFT.\n"
  "PANEL 1 (top band, full width): wide reveal — the red-haired girl sits frame left on the couch, "
  "bored, as orange-red flame leaves the blond teen and the dark-haired teen standing on the entry "
  "seal at frame right. He faces left; she faces right; the dark-haired teen stands half a step "
  "behind him and looks across him at her.\n"
  "PANEL 2 (middle right, horizontal): medium three-shot — the blond teen steps to the far side of "
  "the low table, leaving her at panel left and the dark-haired teen at panel right with an "
  "unobstructed first look at each other.\n"
  "PANEL 3 (middle left, horizontal): close on the dark-haired teen seated frame right of the "
  "table, shoulders squared toward her at frame left.\n"
  "PANEL 4 (bottom right, large vertical, the focal panel): three-shot — the blond teen stands at "
  "the back centre; she looks up-right at him from foreground left; the dark-haired teen looks "
  "up-left at him from foreground right. His hands rest on the chair between them, joining the two "
  "without touching either.\n"
  "PANEL 5 (bottom left, narrow vertical): the dark-haired teen's eye tracks the visible seal "
  "lines "
  "around the window; the blond teen is in three-quarter profile at frame right with his mouth "
  "clearly visible, looking the same way. " + L_SEALED
  + SAY((1, KAR, "upper right", "YOU COULD KNOCK."),
        (1, BOY16, "upper left", "THIS IS STILL MY SEAL ARRAY."),
        (2, BOY16, "upper right", "UZUMAKI KARIN. UCHIHA SASUKE."),
        (3, SAS16, "upper right", "UCHIHA SASUKE."),
        (4, BOY16, "upper right", "KARIN, YOU CAN TRUST HIM."),
        (4, KAR, "upper left", "YOU DECIDED THAT QUICKLY."),
        (4, BOY16, "lower right", "NO. I DECIDED IT CAREFULLY."),
        (5, SAS16, "upper right", "KAKASHI SAID ANBU COULDN'T ENTER THIS HOUSE."),
        (5, BOY16, "lower left", "JIRAIYA DID ONCE. I CORRECTED THE ERROR."))
  + TAILS + "In PANEL 5 BOTH teens are drawn: the dark-haired teen at frame LEFT with his mouth visible "
    "as he tracks the seal lines, and the blond teen in three-quarter profile at frame RIGHT. "
    "\"KAKASHI SAID ANBU COULDN'T ENTER THIS HOUSE.\" is the DARK-HAIRED teen's line — place the "
    "balloon at the upper right as stated but draw a long tail travelling down-LEFT across the "
    "panel to HIS mouth, never stopping at the blond teen. In PANEL 4 \"NO. I DECIDED IT "
    "CAREFULLY.\" belongs to the BLOND TEEN standing at the back centre; its tail runs to HIS "
    "mouth and never up-right to the dark-haired teen in the foreground.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "medium"),

 # ---- Spread 2: what belongs to them -----------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "SIX panels. The copied scrolls become an active ownership dispute.\n"
  "PANEL 1 (top band, full width): SILENT high wide shot — the low table divides the three "
  "positions clearly; the blond teen sets one returned scroll at its centre and all three look at "
  "it. No text in this panel.\n"
  "PANEL 2 (middle right, vertical): two-shot — the blond teen sits upper-left within the panel, "
  "the dark-haired teen lower-right looking up-left at him.\n"
  "PANEL 3 (middle centre, narrow vertical): insert close-up of the blond teen's fingers resting "
  "BESIDE the scroll, not on it. Hand and tabletop only, no face and no mouth.\n"
  "PANEL 4 (middle left, vertical): close on the blond teen — he looks down-right toward the "
  "scroll, then up-right toward the dark-haired teen.\n"
  "PANEL 5 (bottom right, horizontal): close on the dark-haired teen, eye-line left toward the "
  "blond teen.\n"
  "PANEL 6 (bottom left, large horizontal): three-shot over the scroll — the blond teen is "
  "background centre, the dark-haired teen right foreground, the red-haired girl left foreground, "
  "listening rather than excluded. The scroll carries ILLEGIBLE SCRIBBLE only, not readable words. "
  + L_SEALED
  + SAY((2, BOY16, "upper right", "THE ELDERS KEPT OUR SCROLLS FOR YEARS."),
        (2, SAS16, "lower left", "THEY RETURNED THEM."),
        (3, OFF(BOY16), "upper right", "AFTER A WEEK."),
        (4, BOY16, "upper right", "ENOUGH TIME TO COPY WHAT THEY WANTED."),
        (5, SAS16, "upper right", "WHAT WAS WORTH COPYING?"),
        (6, BOY16, "upper right", "CLAN HISTORY. SHARINGAN RESEARCH. A FEW FORBIDDEN TECHNIQUES."),
        (6, SAS16, "on the RIGHT of the panel directly above the dark-haired teen's head "
            "at frame right, clearly BELOW the highest balloon's bottom edge", "THE NAKA SHRINE HOLDS THE DANGEROUS SECRETS."),
        (6, BOY16, "lower left, the LOWEST balloon in the panel", "THAT DOESN'T MAKE THESE THEIRS."))
  + TAILS + "PANEL 6's three balloons are ordered by HEIGHT, not by side, so each can sit over its own "
    "speaker: \"CLAN HISTORY. SHARINGAN RESEARCH. A FEW FORBIDDEN TECHNIQUES.\" is the "
    "HIGHEST balloon in the panel, \"THE NAKA SHRINE HOLDS THE DANGEROUS SECRETS.\" sits "
    "clearly BELOW its bottom edge, and \"THAT DOESN'T MAKE THESE THEIRS.\" is lower still. "
    "The shrine line is the DARK-HAIRED teen's: place it on the RIGHT of the panel directly "
    "above HIS head and run a SHORT tail straight down to HIS mouth. Its tail must never "
    "point left, never cross the panel, and never end on the red-haired girl at frame left "
    "or on the blond teen at the centre.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "SEVEN panels. Their shared rule is stated and tested.\n"
  "PANEL 1 (top right, horizontal): medium on the blond teen looking left toward the dark-haired "
  "teen, the scroll low in frame.\n"
  "PANEL 2 (top left, horizontal): medium on the dark-haired teen — a slight smile pulls at one "
  "corner, eye-line right.\n"
  "PANEL 3 (middle right, small square): close on the red-haired girl leaning into the exchange "
  "from frame left, eyes right toward the blond teen.\n"
  "PANEL 4 (middle centre, small square): close on the blond teen turning his EYES, not his head, "
  "from his right to his left.\n"
  "PANEL 5 (middle left, small square): two-shot — the red-haired girl foreground and the "
  "dark-haired teen behind her; both look right at the blond teen and the teen's smile is now "
  "visible.\n"
  "PANEL 6 (bottom right, large horizontal): low angle — the scroll fills foreground right, the "
  "blond teen stays controlled at background left.\n"
  "PANEL 7 (bottom left, horizontal): the red-haired girl looks right at the dark-haired teen and "
  "he looks left at her, with the blond teen's shoulder between them at the top edge. " + L_SEALED
  + SAY((1, BOY16, "upper right", "AT THE COUNCIL, THEY BURN EVERY COPY."),
        (2, SAS16, "upper right", "YOU'RE GOING TO LECTURE THEM ABOUT LAW?"),
        (3, KAR, "upper right", "HE ONLY OBEYS HIS OWN."),
        (4, BOY16, "upper right", "YOU MAKE ME SOUND HYPOCRITICAL."),
        (5, SAS16, "upper right", "ARE WE WRONG?"),
        (6, BOY16, "upper right", "I DON'T TAKE WHAT ISN'T MINE."),
        (6, BOY16, "upper left", "WHAT BELONGS TO THE CLAN COMES BACK—LAWFULLY OR OTHERWISE."),
        (7, KAR, "very top of the panel above the red-haired girl at frame left, as the "
            "HIGHEST balloon in this panel", "AND AFTER THE SCROLLS?"),
        (7, SAS16, "lower right, clearly BELOW the other balloon, beside the dark-haired "
            "teen at frame right", "WE RESTORE THE CLAN."))
  + TAILS + "PANEL 7's two balloons are stacked by HEIGHT, not placed side by side. \"AND AFTER THE "
    "SCROLLS?\" is the HIGHEST balloon in the panel, at its very top above the red-haired "
    "girl, and \"WE RESTORE THE CLAN.\" sits clearly LOWER, below the first "
    "balloon's bottom edge, beside the dark-haired teen. The higher balloon is read first, "
    "so the question always precedes the answer; the answer never sits above it or level "
    "with it. In PANEL 6 the second balloon reads exactly \"WHAT BELONGS TO THE "
    "CLAN COMES BACK — LAWFULLY OR OTHERWISE.\" with ONE single long dash between BACK and "
    "LAWFULLY: never a run of two or three hyphens, never \"BACK---LAWFULLY\", and never a hyphen "
    "breaking a word across lines.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "low"),

 # ---- Spread 3: recent history -----------------------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "SIX panels. The red-haired girl takes the centre of the argument.\n"
  "PANEL 1 (top band, full width): medium three-shot — the dark-haired teen sits right, the girl "
  "left, the blond teen background centre. The teen's eye-line goes to the blond teen; she is "
  "already watching the teen.\n"
  "PANEL 2 (middle right, vertical): close on the blond teen looking down-right.\n"
  "PANEL 3 (middle centre, narrow vertical): close on the dark-haired teen — the confidence leaves "
  "his expression; he looks left but avoids both faces.\n"
  "PANEL 4 (middle left, vertical): medium on the red-haired girl leaning across the table, "
  "eye-line cutting right toward both Uchiha. The dark-haired teen is NOT drawn in this panel.\n"
  "PANEL 5 (bottom right, horizontal): the girl foreground left, the dark-haired teen background "
  "right; she holds his eye-line and does not let him look away.\n"
  "PANEL 6 (bottom left, large horizontal): she turns from the dark-haired teen toward the blond "
  "teen — he is frame left and unreadable, she is centre, the dark-haired teen stays frame right "
  "and listens. " + L_SEALED
  + SAY((1, SAS16, "upper right", "WE STILL HAVE TO DISCUSS HOW."),
        (2, BOY16, "upper right", "HAVE YOU FOUND SUITABLE FEMALES?"),
        (3, SAS16, "upper right", "NO."),
        (4, KAR, "upper right", "SOMEONE. NOT 'SUITABLE FEMALES.'"),
        (4, OFF(SAS16), "lower left", "I DIDN'T SAY THAT."),
        (5, KAR, "upper right", "THEN DON'T TALK ABOUT A FAMILY LIKE A RECRUITMENT QUOTA."),
        (6, KAR, "upper right", "IF YOU REBUILD IT, DO IT WITH SOMEONE YOU LOVE."),
        (6, KAR, "upper left", "ALTHOUGH HE MAY NOT UNDERSTAND THE DISTINCTION."))
  + TAILS + "In PANEL 5 the balloon \"THEN DON'T TALK ABOUT A FAMILY LIKE A RECRUITMENT QUOTA.\" belongs "
    "to the RED-HAIRED GIRL in the foreground at frame left; it carries a clearly drawn tail "
    "running down to HER mouth and is never tail-less and never rests against the dark-haired "
    "teen's head. In PANEL 4 the dark-haired teen is NOT drawn anywhere, so \"I DIDN'T SAY "
    "THAT.\" is an off-panel balloon whose short spur runs to the LOWER-LEFT panel border and "
    "stops on the border line itself, touching no part of the red-haired girl — not her sleeve, "
    "her hand, nor her hair.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "low"),

 ("p06", dict(scene="emotional_closeup", light="day", cast="small_group", mood="calm", panels=8),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "EIGHT panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 holds PANEL 1 at the RIGHT and "
  "PANEL 2 at the LEFT. TIER 2 is PANEL 3 alone, full width. TIER 3 holds PANEL 4 at the RIGHT and "
  "PANEL 5 at the LEFT. TIER 4, the bottom tier, holds PANEL 6 at the RIGHT, PANEL 7 in the CENTRE "
  "and PANEL 8 at the LEFT. Panels 6, 7 and 8 all sit BELOW panels 4 and 5. Humour exposes how new "
  "their cooperation is; it must never read as childhood "
  "friendship.\n"
  "PANEL 1 (top right, square): close on the red-haired girl looking left.\n"
  "PANEL 2 (top left, square): close on the dark-haired teen looking right, flat and immediate.\n"
  "PANEL 3 (upper-middle band, full width): two-shot — the blond teen frame left, the dark-haired "
  "teen frame right; the blond teen's eyes travel right toward him.\n"
  "PANEL 4 (middle right, horizontal): reverse two-shot — the dark-haired teen looks left at the "
  "blond teen with an old competitive edge.\n"
  "PANEL 5 (middle left, horizontal): the red-haired girl laughs once into her hand; both Uchiha "
  "are blurred on either side behind her.\n"
  "PANEL 6 (bottom right, small square): the dark-haired teen, answering immediately, eye-line "
  "left toward her.\n"
  "PANEL 7 (bottom centre, horizontal): the blond teen left and the dark-haired teen right in "
  "profile facing inward; neither smiles now.\n"
  "PANEL 8 (bottom left, large reaction panel, the focal panel): the red-haired girl foreground "
  "centre looks from one to the other in open disbelief; the two Uchiha share a brief eye-line "
  "across her, each newly aware of how naturally the exchange came. " + L_SEALED
  + SAY((1, KAR, "upper right", "SASUKE, HAVE YOU EVER BEEN IN LOVE?"),
        (2, SAS16, "upper right", "NO."),
        (3, BOY16, "upper right", "HE HAD NO INTEREST BEYOND REVENGE."),
        (4, SAS16, "upper right", "YOU CALLED EVERY GIRL AN ANNOYANCE."),
        (5, KAR, "upper right", "HOW LONG HAVE YOU TWO BEEN FRIENDS?"),
        (6, SAS16, "upper right", "WE AREN'T."),
        (7, BOY16, "very top of the panel, as the HIGHEST balloon in this panel", "WE WERE CIVIL IN KIRI."),
        (7, SAS16, "clearly BELOW the other balloon, under its bottom edge, beside the "
            "dark-haired teen at frame right", "A FEW WEEKS AGO. BEFORE THAT, WE HATED EACH OTHER."),
        (8, KAR, "upper right", "YOU DON'T ACT LIKE IT."))
  + TAILS + "PANELS 1 and 2 form the TOP row, PANEL 3 is a full-width band beneath them, PANELS 4 and 5 "
    "form the MIDDLE row with 4 at reader-RIGHT and 5 at reader-LEFT, and PANELS 6, 7 and 8 form "
    "the BOTTOM row with 6 at reader-RIGHT, 7 in the centre and 8 at reader-LEFT. PANEL 6 sits "
    "wholly BELOW panel 5, never beside it, so \"WE AREN'T.\" is read after \"HOW LONG HAVE YOU "
    "TWO BEEN FRIENDS?\" PANEL 7's two balloons are stacked by HEIGHT, not placed side by side. \"WE WERE CIVIL "
    "IN KIRI.\" is the HIGHEST balloon in the panel, at its very top, and carries a long "
    "tail running down-LEFT across the panel to the blond teen's mouth at frame left. \"A "
    "FEW WEEKS AGO. BEFORE THAT, WE HATED EACH OTHER.\" sits clearly LOWER, below that "
    "balloon's bottom edge, beside the dark-haired teen at frame right, with a short tail to "
    "HIS mouth. The higher balloon is read first; the second never sits above it or level "
    "with it.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "medium"),

 # ---- Spread 4: seat and shield ----------------------------------------------------
 ("p07", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "SIX panels. Clan responsibility is divided explicitly.\n"
  "PANEL 1 (top band, full width): medium three-shot — the laughter has passed; the blond teen "
  "looks right toward the dark-haired teen, the red-haired girl sits back at left and watches.\n"
  "PANEL 2 (middle right, vertical): close on the blond teen, the sealed window lattice behind his "
  "shoulder.\n"
  "PANEL 3 (middle left, vertical): close on the dark-haired teen, eyes lowering toward the fan "
  "crest on the table.\n"
  "PANEL 4 (bottom right, small horizontal): two-shot across the table — the blond teen looks "
  "left, the dark-haired teen looks right.\n"
  "PANEL 5 (bottom centre, horizontal): the dark-haired teen foreground, the blond teen beyond; "
  "the teen holds his eye-line without deference.\n"
  "PANEL 6 (bottom left, large vertical, the focal panel): the dark-haired teen is centred against "
  "the plain sealed window; the blond teen's shoulder is frame right with his mouth OUT of frame, "
  "the girl's shoulder frame left. The returned clan scroll forms the lower edge and both "
  "foreground figures look toward him. " + L_SEALED
  + SAY((1, BOY16, "upper right", "EASE DOESN'T SETTLE THE CLAN SEAT."),
        (2, BOY16, "upper right", "ONE OF US TAKES IT."),
        (3, SAS16, "upper right", "MY FATHER HELD IT."),
        (4, BOY16, "upper right", "THEN TAKE IT."),
        (4, SAS16, "upper left", "NO."),
        (5, SAS16, "upper right", "I DEALT WITH THE ADVISERS ONCE. YOU'RE BETTER AT MAKING THEM ANSWER."),
        (5, BOY16, "lower left", "FINE. I TAKE THE CLAN SEAT."),
        (6, OFF(BOY16), "upper right", "WHAT WILL YOU TAKE?"),
        (6, SAS16, "lower left", "THE POLICE FORCE.")),
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "low"),

 ("p08", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + KARIN.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, KAR) + ARMOUR + ROOM +
  "SEVEN panels. The institution belongs to the dark-haired teen; the blond teen supports it.\n"
  "PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. Three horizontal "
  "tiers, each full width and separated by an unbroken horizontal gutter; inside a tier the "
  "panels read RIGHT TO LEFT. TIER 1 is PANEL 1 alone, full width. TIER 2 holds PANEL 2 "
  "TOUCHING THE PAGE'S RIGHT MARGIN, PANEL 3 in the centre and PANEL 4 TOUCHING THE PAGE'S "
  "LEFT MARGIN. TIER 3 holds PANEL 5 — the single close on the blond teen — TOUCHING THE "
  "PAGE'S RIGHT MARGIN, PANEL 6 — the high two-shot over the small table — in the CENTRE, "
  "and PANEL 7 TOUCHING THE PAGE'S LEFT MARGIN. The panel carrying \"WITH THE COUNCIL. "
  "INTELLIGENCE. TRAINING.\" is the RIGHT-HAND panel of the bottom tier and the high "
  "two-shot is to its LEFT, never the reverse.\n"
  "PANEL 1 (top band, full width): low two-shot — the dark-haired teen sits frame left and the "
  "blond teen frame right with the returned clan scroll between them; their eye-lines meet at the "
  "centre.\n"
  "PANEL 2 (middle right, vertical): close on the dark-haired teen, gaze level.\n"
  "PANEL 3 (middle centre, narrow vertical): close on the blond teen — no correction in his "
  "posture, only in his words.\n"
  "PANEL 4 (middle left, vertical): the dark-haired teen, not yielding the larger point.\n"
  "PANEL 5 (bottom right, horizontal): the blond teen in three-quarter profile, eye-line left.\n"
  "PANEL 6 (bottom centre, horizontal): high view of the two Uchiha at the small table; the empty "
  "seats around them make the lack of members visible.\n"
  "PANEL 7 (bottom left, large horizontal): the dark-haired teen stands and closes his book; the "
  "blond teen stays seated looking up; the red-haired girl is visible at far left following the "
  "exchange. " + L_SEALED
  + SAY((1, SAS16, "upper right", "THE UCHIHA FOUNDED THE POLICE FORCE. IT DIED WITH THE CLAN."),
        (2, SAS16, "upper right", "I WANT IT RESTORED. I WILL COMMAND IT."),
        (3, BOY16, "upper right", "TOBIRAMA FOUNDED IT AND HANDED IT TO THE UCHIHA."),
        (4, SAS16, "upper right", "I KNOW WHAT IT BECAME. WILL YOU HELP ME CONVINCE THEM?"),
        (5, BOY16, "upper right", "WITH THE COUNCIL. INTELLIGENCE. TRAINING."),
        (6, BOY16, "upper right", "BUT TWO UCHIHA AREN'T A FORCE."),
        (6, SAS16, "upper left", "WE ASK TSUNADE FOR RECRUITS."),
        (7, SAS16, "upper right", "THEN WE TRAIN THEM."))
  + TAILS + "In PANEL 1 the balloon \"THE UCHIHA FOUNDED THE POLICE FORCE. IT DIED WITH THE CLAN.\" "
    "belongs to the DARK-HAIRED teen sitting at frame LEFT. Draw a long tail that crosses the "
    "panel to HIS mouth and never a stub stopping at the blond teen at frame right, who says "
    "nothing at all in this panel.",
  R("naruto_v4_armor", "sasuke_16", "karin", "env_shinobi_apartment"), "low"),

 # ---- Spread 5: protection is not presence -----------------------------------------
 ("p09", dict(scene="emotional_closeup", light="day", cast="two", mood="somber", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + KARIN.format(i=2) + SASUKE16.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, KAR, SAS16) + ARMOUR + ROOM +
  "SEVEN panels. The dark-haired teen appears only in PANEL 1, leaving at frame right.\n"
  "PANEL 1 (top right, horizontal): SILENT medium — the dark-haired teen exits at frame right; the "
  "blond teen at background centre turns left toward the red-haired girl; she watches the door "
  "close. No text in this panel.\n"
  "PANEL 2 (top left, horizontal): SILENT close on the girl looking right toward him with wary "
  "resignation as he takes the chair opposite her. No text in this panel.\n"
  "PANEL 3 (middle right, vertical): two-shot across the table — the blond teen right, the girl "
  "left, eye-lines level.\n"
  "PANEL 4 (middle left, vertical): the blond teen foreground right, the girl background left; he "
  "does not advance into her space.\n"
  "PANEL 5 (bottom right, large horizontal, the focal panel): close on the girl; the blond teen is "
  "only a dark shoulder at frame right with NO mouth in frame. Her prior defiance is interrupted.\n"
  "PANEL 6 (bottom centre, narrow vertical): insert on the blond teen's gloved fingertips beside "
  "one spiral of the table's barrier array; the girl is reflected faintly in the polished wood. No "
  "face and no mouth in this panel. The array marks are ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 7 (bottom left, horizontal): balanced two-shot — she sits straighter at frame left, he "
  "stays frame right; the table still separates them but both hands now rest on it. " + L_SEALED
  + SAY((3, BOY16, "upper right", "I BROUGHT YOU HERE TO KEEP YOU SAFE."),
        (3, KAR, "upper left", "I NEVER ASKED TO COME."),
        (4, BOY16, "upper right", "NO. BUT YOU AGREED TO LIVE. YOU HAVE CHAKRA, SENSOR ABILITY, UZUMAKI BLOOD—AND NO TRAINING."),
        (5, KAR, "upper right", "I CAN SENSE THEM. I CAN RUN."),
        (5, OFF(BOY16), "upper left", "NOT ALWAYS. I CAN'T ALWAYS PROTECT YOU."),
        (6, OFF(BOY16), "upper right", "IF I'M NOT THERE, YOU HOLD THEM UNTIL I AM. MY MOTHER COULD DEFEND HERSELF. SHE TAUGHT THE FOURTH SEALS."),
        (7, BOY16, "upper right", "FŪINJUTSU. TAIJUTSU. USE YOUR HEALING CHAKRA WITHOUT BEING BITTEN."),
        (7, KAR, "upper left", "FINE. BASICS.")),
  R("naruto_v4_armor", "karin", "sasuke_16", "env_shinobi_apartment"), "medium"),

 ("p10", dict(scene="dialogue", light="dark", cast="small_group", mood="calm", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + SASUKE16.format(i=2) + YUGAO_V4.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, YUG) + ARMOUR +
  "SEVEN panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT, PANEL 3 in the CENTRE and PANEL 4 at the LEFT. TIER 3, the bottom "
  "tier, holds PANEL 5 at the RIGHT, PANEL 6 in the CENTRE and PANEL 7 at the LEFT. Panel 5 sits "
  "BELOW panel 4, never beside it. Image 4 supplies Uchiha architecture and palette; the scene "
  "plays at the house "
  "door of that compound at night.\n"
  "PANEL 1 (top band, full width): night exterior — the purple-haired kunoichi stands frame right "
  "at the Uchiha house door, the empty compound receding left. Keep the upper right quiet for the "
  "time card.\n"
  "PANEL 2 (middle right, vertical): doorway two-shot — the dark-haired teen opens from frame "
  "left, the kunoichi stays frame right outside; they look directly at each other.\n"
  "PANEL 3 (middle centre, narrow vertical): deep hallway view — the blond teen descends from "
  "background centre in red armour; the kunoichi is a FOREGROUND SILHOUETTE outside with her face "
  "and mouth not visible; the dark-haired teen steps aside.\n"
  "PANEL 4 (middle left, vertical): close on the blond teen at the threshold, eye-line right.\n"
  "PANEL 5 (bottom right, horizontal): close on the kunoichi — surprise softening into resolve, "
  "eye-line left.\n"
  "PANEL 6 (bottom centre, horizontal): close two-shot across the threshold — the blond teen gives "
  "a small genuine smile and she catches it.\n"
  "PANEL 7 (bottom left, large horizontal): the door has closed; the blond teen stands foreground "
  "right with the smile nearly gone; the dark-haired teen leans in the hallway at frame left with "
  "his book. " + L_NIGHT
  + CAP(1, "upper right", "LATER.")
  + SAY((2, SAS16, "upper right", "YUGAO-SAN?"),
        (2, YUG, "upper left", "IS NARUTO HERE?"),
        (3, OFF(YUG), "upper right", "I HEARD YOU RETURNED. I WANTED TO SEE IF YOU WERE WELL."),
        (4, BOY16, "upper right", "IT'S GOOD TO SEE YOU WELL."),
        (5, YUG, "upper right", "DINNER. TOMORROW NIGHT?"),
        (6, BOY16, "upper right", "YES."),
        (6, YUG, "upper left", "PLEASE DON'T WEAR THE ARMOUR."),
        (7, SAS16, "upper right", "A DATE?"),
        (7, BOY16, "upper left", "PERHAPS."))
  + SFX(1, "KNOCK", "Small, at the lower left beside her knuckles; it must not cover her face.")
  + TAILS + "EVERY SCRIPTED BALLOON MUST APPEAR. PANEL 7 carries BOTH \"A DATE?\" and "
    "\"PERHAPS.\" — \"A DATE?\" at the upper right beside the dark-haired teen and "
    "\"PERHAPS.\" to its LEFT beside the blond teen — and neither may be omitted. The "
    "sound effect is spelled exactly K-N-O-C-K, five letters, with no doubled letter. "
    "In PANEL 6 the two balloons must not exchange speakers: \"YES.\" is the BLOND TEEN's and its "
    "tail ends at his mouth, and \"PLEASE DON'T WEAR THE ARMOUR.\" is the PURPLE-HAIRED "
    "KUNOICHI's and its tail ends at hers. PANEL 4 closes the MIDDLE row at reader-LEFT and PANEL "
    "5 opens the BOTTOM row at reader-RIGHT, wholly below it, so the blond teen's \"IT'S GOOD TO "
    "SEE YOU WELL.\" is read before her \"DINNER. TOMORROW NIGHT?\" In PANEL 7 \"A DATE?\" is the "
    "RIGHTMOST balloon and \"PERHAPS.\" sits to its LEFT.",
  R("naruto_v4_armor", "sasuke_16", "yugao_v4", "env_uchiha_compound"), "low"),

 # ---- Spread 6: the response -------------------------------------------------------
 ("p11", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + RTL + DAN.format(i=1) + KOHARU.format(i=2) + HOMURA.format(i=3)
  + ONLY(HAWK, KOH, HOM,
         "two distant masked Root guards at the rear wall in plain featureless white oval masks, "
         "never unmasked and never individually recognisable") +
  "SIX panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page is "
  "divided into horizontal TIERS that each run the full width of the paper, stacked top to bottom, "
  "separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier the "
  "panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT and PANEL 3 at the LEFT. TIER 3, the bottom tier, holds PANEL 4 — "
  "the medium on the male adviser — TOUCHING THE PAGE'S RIGHT MARGIN, PANEL 5 — the profile of the "
  "bandaged old man between the two low adviser silhouettes — in the CENTRE, and PANEL 6 TOUCHING "
  "THE PAGE'S LEFT MARGIN. The panel carrying \"WITH A RED-HAIRED WOMAN.\" is the RIGHT-HAND panel "
  "of the bottom tier and the panel carrying \"SHE WORKED UNDER OROCHIMARU.\" is to its LEFT, "
  "never the reverse. Panel 4 sits BELOW panel 3, never beside it. A deep underground Root chamber "
  "holds a rigid triangle: the bandaged old man "
  "elevated at the far centre, the elderly female adviser entering from frame right, the elderly "
  "male adviser from frame left. No Root agent stands close enough to imply a specific operation, "
  "and NO object, gesture or document hints at any method.\n"
  "PANEL 1 (top band, full width): SILENT deep establishing shot — the bandaged old man is small "
  "on the raised chair at the far centre; the female adviser descends the right stair, the male "
  "adviser the left; two masked guards stay featureless at the rear wall. No text in this panel.\n"
  "PANEL 2 (middle right, vertical): medium on the female adviser looking up-left.\n"
  "PANEL 3 (middle left, vertical): medium on the bandaged old man, his visible eye down-right.\n"
  "PANEL 4 (bottom right, horizontal): medium on the male adviser looking up-right through his "
  "lenses.\n"
  "PANEL 5 (bottom centre, horizontal): the bandaged old man in profile; the two advisers are LOW "
  "SILHOUETTES on opposite sides with their faces and mouths out of frame, keeping the triangle "
  "intact.\n"
  "PANEL 6 (bottom left, large horizontal): low angle from behind the advisers, whose backs fill "
  "the lower corners with no mouths visible; the old man is elevated and centred and looks past "
  "them rather than at either face. " + L_ROOT
  + SAY((2, KOH, "upper right", "SO IT'S TRUE."),
        (3, HAWK, "upper right", "NARUTO RETURNED."),
        (4, HOM, "upper right", "WITH A RED-HAIRED WOMAN."),
        (5, HAWK, "upper right", "SHE WORKED UNDER OROCHIMARU."),
        (5, OFF(KOH), "upper left", "THEN SHE'S USEFUL."),
        (6, HAWK, "upper right", "USEFUL ENOUGH FOR HIM TO BRING INTO KONOHA."),
        (6, OFF(HOM), "upper centre", "HE WON'T LET US QUESTION HER."),
        (6, HAWK, "upper left", "AND FORCE WOULD WASTE ROOT LIVES."))
  + TAILS + "PANEL 4 (the male adviser, \"WITH A RED-HAIRED WOMAN.\") opens the BOTTOM row at "
    "reader-RIGHT and PANEL 5 sits to its LEFT in that same row, so \"WITH A RED-HAIRED WOMAN.\" "
    "is read before \"SHE WORKED UNDER OROCHIMARU.\" and \"THEN SHE'S USEFUL.\" In PANEL 6 the "
    "male adviser is one of the two BACKS filling the lower corners with no mouth in frame, so "
    "\"HE WON'T LET US QUESTION HER.\" is an off-panel balloon whose spur runs DOWN-LEFT to the "
    "LOWER-LEFT panel border and stops on the border line; it must never run down onto, touch or "
    "aim at the bandaged old man, who is the elevated central figure.",
  R("danzo", "koharu", "homura"), "low"),

 ("p12", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=7),
  FILL + RTL + DAN.format(i=1) + KOHARU.format(i=2) + HOMURA.format(i=3) + ONLY(HAWK, KOH, HOM) +
  "SEVEN panels. Separate facts become one threat model and stop there. NO object, operative, "
  "gesture or line may preview a method, target, date or crime.\n"
  "PANEL 1 (top right, horizontal): the female adviser foreground looking up-left, the bandaged "
  "old man beyond looking down-right.\n"
  "PANEL 2 (top left, horizontal): insert close-up of the old man's fingers against the chair arm, "
  "perfectly still. Hand and chair only, no face and no mouth.\n"
  "PANEL 3 (middle right, vertical): the male adviser turns his head left toward the female "
  "adviser, then up toward the old man.\n"
  "PANEL 4 (middle centre, narrow vertical): extreme close-up of the old man's visible EYE only, "
  "eye-line down-left. No mouth in frame.\n"
  "PANEL 5 (middle left, vertical): two-shot of the advisers — she looks right at him, he looks "
  "left at her, both now level rather than looking up.\n"
  "PANEL 6 (bottom right, horizontal): low angle on the old man, his chair's shadow cutting "
  "between the advisers below, whose faces are turned away.\n"
  "PANEL 7 (bottom left, dominant panel, the focal panel): extreme close-up of the old man's "
  "visible eye; the two advisers are soft silhouettes at the lower corners. No object or person "
  "hints at any later method. " + L_ROOT
  + SAY((1, KOH, "upper right", "THEN WE USE THE AUTHORITY OF THE COUNCIL."),
        (2, OFF(HAWK), "upper right", "HE EXPECTS THAT."),
        (3, HOM, "upper right", "SASUKE COULDN'T HAVE KNOWN ABOUT THE SCROLLS."),
        (4, OFF(HAWK), "upper right", "NARUTO TOLD HIM."),
        (5, KOH, "very top of the panel above the elderly female adviser, as the HIGHEST "
            "balloon in this panel", "HE KNOWS TOO MUCH."),
        (5, HOM, "lower right, clearly BELOW the other balloon, beside the elderly male "
            "adviser", "AND HE DOESN'T ANSWER TO US."),
        (6, HAWK, "upper right", "HE HAS MADE HIMSELF UNMANAGEABLE."),
        (6, OFF(KOH), "lower left", "THEN WHAT DO WE DO?"),
        (7, OFF(HAWK), "upper right", "I'VE ALREADY PREPARED A RESPONSE."))
  + TAILS + "LETTERING IS CRITICAL ON THIS PAGE: each balloon contains its words and NOTHING else. There "
    "is no extra line beneath the text, no stray dash, hyphen, underscore, dot, tick or mark of "
    "any kind inside or below any balloon, and no hyphen splitting a word across two lines. In "
    "PANEL 5 the two balloons are stacked by HEIGHT, not placed side by side: \"HE KNOWS TOO "
    "MUCH.\" is the HIGHEST balloon in the panel, at its very top above the elderly female "
    "adviser, and \"AND HE DOESN'T ANSWER TO US.\" sits clearly LOWER, below the "
    "first balloon's bottom edge, beside the elderly male adviser. The higher balloon is "
    "read first; the second never sits above it or level with it.",
  R("danzo", "koharu", "homura"), "low"),

 # ---- Spread 7: what the schedule costs --------------------------------------------
 ("p13", dict(scene="transition", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4)
  + ZOR + ONLY(BOY16, ZETSU) + SLEEP +
  "SIX panels. An unexplained physical problem is shown ONLY through observable cost and action — "
  "no wound, no named illness, no diagnosis, no flashback.\n"
  "PANEL 1 (top right, horizontal): SILENT close on a bedside clock in morning light; the blond "
  "teen's eye opens out of focus behind it. No text in this panel.\n"
  "PANEL 2 (top left, horizontal): SILENT medium — he sits at the bed edge in dark sleep shorts "
  "and no shirt, one hand braced on the mattress, the other pressed to his temple; his skin is "
  "pale and he looks down, not at the reader. No text in this panel.\n"
  "PANEL 3 (middle band, full width): SILENT three-beat continuous motion laid out RIGHT TO LEFT "
  "across the band. The RIGHTMOST beat, at the right edge of the panel, is his hand reaching up to "
  "the wall-mounted gunbai. The CENTRE beat is him biting his thumb. The LEFTMOST beat, at the "
  "left "
  "edge, is the bloodied thumb pressed to the seal. Never lay these three beats out left to right "
  "and never put the pressed thumb on the right. The repeated figure must read as ONE movement in "
  "time, never as clones. No text in this panel.\n"
  "PANEL 4 (bottom right, vertical): three-beat continuous action down the panel — at the top his "
  "hands complete two distinct seals in sequence; at the centre both palms plant on the bare floor "
  "and a circular array grows outward beneath them; at the bottom the gunbai base strikes the "
  "finished array's centre while his bare feet stay unsteady at the panel top. The array marks are "
  "ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 5 (bottom centre, vertical): continuous transition down the panel — at the top he "
  "materializes in his hideout room holding the gunbai; at the centre he leaves it on the wall "
  "rack; at the bottom he steps into the lab from frame right, where the plant creature stands "
  "frame left beside a steaming pot and turns its head right toward him.\n"
  "PANEL 6 (bottom left, large vertical, the focal panel): he grips the table with his left hand "
  "and lifts a cup of dark steaming liquid with his right; the creature's hand hovers near the pot "
  "without touching him; his eye-line stays on the cup and the creature is CROPPED OUT of this "
  "panel. " + L_LAB + L_MORNING
  + SAY((5, ZETSU, "upper right", "I CAN'T BELIEVE YOU CAN STILL WALK."),
        (5, BOY16, "upper left", "BARELY."),
        (5, BOY16, "lower right", "IS IT READY?"),
        (6, OFF(ZETSU), "upper right", "YES."),
        (6, OFF(ZETSU), "upper left", "LET IT COOL."),
        (6, BOY16, "lower left", "HOT OR COLD DOESN'T MATTER."))
  + SFX(4, "THUM", "At the lower left beside the seal; keep it clear of his hands.")
  + TAILS + "PANEL 3's three-beat continuous motion runs RIGHT TO LEFT with the reading direction: the "
    "RIGHTMOST beat is his hand reaching for the wall-mounted gunbai, the CENTRE beat is the "
    "thumb being bitten, and the LEFTMOST beat is the bloodied thumb pressed to the seal. Never "
    "reverse that order and never lay the three beats out left to right.",
  R("naruto_v4_black", "zetsu", "gunbai_v4", "env_hideout_kitchen"), "medium"),

 ("p14", dict(scene="dialogue", light="dark", cast="two", mood="calm", panels=7),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4)
  + ZOR + ONLY(BOY16, ZETSU,
               "in PANEL 5 only, an unnamed Oto site overseer at the head of a table with her back "
               "three-quarters to the reader and her face not individually recognisable, and "
               "anonymous contractors on both sides of her, none of them named or recurring")
  + SLEEP +
  "SEVEN panels. The medicine restores him only provisionally; nothing connects his condition to "
  "any person.\n"
  "PANEL 1 (top right, horizontal): SILENT close on him drinking — the cup covers his mouth, his "
  "fingers stay tight around it, steam crosses his closed eyes. No text in this panel.\n"
  "PANEL 2 (top left, horizontal): close on the empty cup lowering; his face tightens at the "
  "bitterness and his skin tone begins to return. The plant creature is NOT drawn in this panel.\n"
  "PANEL 3 (middle right, vertical): close on his eye as the three-tomoe Sharingan resolves into "
  "focus; his eye-line turns left. Eye only — no mouth in frame.\n"
  "PANEL 4 (middle centre, vertical): the plant creature beside the pot, looking right toward "
  "him.\n"
  "PANEL 5 (middle left): A BORDERLESS REPORT IMAGE. It has NO panel border, NO frame line, "
  "NO black outline and no gutter of its own on ANY side — its edges dissolve softly into "
  "the bare paper of the page, so it reads as visualized information and never as a live "
  "cut to another location. Do not draw a rectangle around it. It shows an "
  "Oto meeting table seen straight on, the overseer at its head with her back three-quarters to "
  "the reader, anonymous contractors on both sides, rolled building plans between them. Nobody "
  "speaks inside the report image and all plan markings are ILLEGIBLE SCRIBBLE.\n"
  "PANEL 6 (bottom right, horizontal): two-shot across the lab table — the creature left, the "
  "blond teen right, eye-lines meeting.\n"
  "PANEL 7 (bottom left, large horizontal): through the lab doorway at frame left he lifts the "
  "gunbai from the hideout-room wall rack, steady again; the creature stays frame right by the "
  "medicine; he looks at the weapon, not back at it. " + L_LAB
  + SAY((2, OFF(ZETSU), "upper right", "IT'S WORKING."),
        (2, BOY16, "upper left", "FOR NOW."),
        (3, OFF(BOY16), "upper right", "REPORT."),
        (4, ZETSU, "upper right", "GUREN IS HIRING CONTRACTORS. CONSTRUCTION BEGINS WITHIN A WEEK."),
        (5, OFF(BOY16), "upper right", "MAKE CERTAIN IT DOES."),
        (6, ZETSU, "upper right", "MOST ARE CELEBRATING OROCHIMARU'S DEATH. A FEW WANT REVENGE."),
        (6, BOY16, "lower right", "IF THEY INTERFERE, QUIET THEM."),
        (7, ZETSU, "upper right", "YOU'LL BE BUSY?"),
        (7, BOY16, "upper left", "THE COUNCIL. DANZŌ'S RESPONSE. MEI'S ALLIANCE. KEEP OTO MOVING."))
  + TAILS + "In PANEL 6 \"MOST ARE CELEBRATING OROCHIMARU'S DEATH. A FEW WANT REVENGE.\" is the RIGHTMOST "
    "and highest balloon and \"IF THEY INTERFERE, QUIET THEM.\" sits BELOW AND LEFT of it, so the "
    "order is only given after the report that prompts it. PANEL 5 is a BORDERLESS report image: "
    "it has NO panel border, NO frame line and NO gutter of its own, bleeding softly into the "
    "surrounding page as visualized information rather than reading as a live cut to another "
    "location.",
  R("naruto_v4_black", "zetsu", "gunbai_v4", "env_hideout_kitchen"), "low"),

 # ---- Spread 8: a place for the Police ---------------------------------------------
 ("p15", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=7),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + GUNBAI_V4.format(i=3)
  + ENV.format(i=4) + ONLY(BOY16, SAS16) + BLACKFIT + TABLE +
  "SEVEN panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT, PANEL 3 in the CENTRE and PANEL 4 at the LEFT. TIER 3, the bottom "
  "tier, holds PANEL 5 — the small close on the blond teen asking \"WHERE IN IT?\" — TOUCHING THE "
  "PAGE'S RIGHT MARGIN, PANEL 6 — the silent close on the dark-haired teen — in the CENTRE, and "
  "PANEL 7 — the LARGEST panel of the tier, the high angle along the table carrying three balloons "
  "— TOUCHING THE PAGE'S LEFT MARGIN. The large three-balloon panel is at the LEFT EDGE of the "
  "page and is read LAST; the small \"WHERE IN IT?\" panel is at the RIGHT EDGE and is read FIRST. "
  "Panels 5, 6 and 7 are each ONE TIER TALL ONLY — none is a tall column reaching up into tier 2 — "
  "so panel 5 sits wholly BELOW panel 4. Image 4 supplies Uchiha architecture and palette only; "
  "this is the INTERIOR "
  "kitchen of that house.\n"
  "PANEL 1 (top band, full width): wide kitchen — the dark-haired teen sits frame left reading "
  "with tea; the blond teen enters frame right, hair still damp; his three-quarter BACK view shows "
  "both the Uchiha fan and the Uzumaki spiral. The teen looks over the book toward him; the blond "
  "teen looks toward the empty chair, not at him.\n"
  "PANEL 2 (middle right, small horizontal): SILENT close on the blond teen sitting; he gives no "
  "answer. The gunbai is visible through the doorway, hanging back on his bedroom wall. No text in "
  "this panel.\n"
  "PANEL 3 (middle centre, horizontal): two-shot down the table — the blond teen right, the "
  "dark-haired teen left, eye-lines meeting.\n"
  "PANEL 4 (middle left, small horizontal): close on the dark-haired teen, eyes drifting up-right "
  "in thought.\n"
  "PANEL 5 (tier 3, RIGHT — a small panel ONE TIER TALL, never a column reaching up into tier 2): "
  "the blond teen looking left without changing expression.\n"
  "PANEL 6 (bottom centre, narrow vertical): SILENT close on the dark-haired teen with no "
  "immediate answer, his book lowering. No text in this panel.\n"
  "PANEL 7 (bottom left, large vertical): high angle along the table — the blond teen's gloved "
  "hand taps three empty places on a BLANK sheet between them WITHOUT drawing anything; the "
  "dark-haired teen follows each point with his eyes. The sheet stays blank; any stray marking is "
  "ILLEGIBLE SCRIBBLE, not readable words. " + L_KITCHEN
  + SAY((1, SAS16, "upper right", "YOU'RE UP LATE."),
        (3, BOY16, "upper right", "WHERE WILL YOU BASE THE POLICE FORCE?"),
        (4, SAS16, "upper right", "THE COMPOUND."),
        (5, BOY16, "upper right", "WHERE IN IT?"),
        (7, BOY16, "upper right", "WHERE DO YOU STORE CASE FILES?"),
        (7, BOY16, "upper centre", "HOLD BRIEFINGS?"),
        (7, BOY16, "upper left", "SEPARATE POLICE WORK FROM CLAN BUSINESS?"))
  + TAILS + "PANEL 4 (the dark-haired teen, \"THE COMPOUND.\") closes the MIDDLE row at reader-LEFT and "
    "PANEL 5 (the blond teen, \"WHERE IN IT?\") opens the BOTTOM row at reader-RIGHT, wholly "
    "below it. Neither is a tall panel, and NO panel anywhere on this page spans two rows, so "
    "\"WHERE IN IT?\" can never be read before \"THE COMPOUND.\"",
  R("naruto_v4_black", "sasuke_16", "gunbai_v4", "env_uchiha_compound"), "low"),

 ("p16", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16) + BLACKFIT + TABLE +
  "SIX panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page is "
  "divided into horizontal TIERS that each run the full width of the paper, stacked top to bottom, "
  "separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier the "
  "panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 holds PANEL 1 at the RIGHT and "
  "PANEL 2 at the LEFT. TIER 2 holds PANEL 3 at the RIGHT and PANEL 4 at the LEFT. TIER 3, the "
  "bottom tier, holds PANEL 5 at the RIGHT and PANEL 6 at the LEFT. Panel 5 sits BELOW panel 4, "
  "never beside it. The headquarters stays a blank sheet and its resources stay unresolved.\n"
  "PANEL 1 (top right, horizontal): the dark-haired teen looks down at the blank sheet, his tea "
  "and closed book above it; his eye-line follows the page toward the blond teen at frame right.\n"
  "PANEL 2 (top left, horizontal): the blond teen in profile looking right.\n"
  "PANEL 3 (middle right, vertical): the dark-haired teen reaches for a brush; the motion runs "
  "RIGHT TO LEFT with the reading direction.\n"
  "PANEL 4 (middle left, vertical): the blond teen slides the blank sheet fully toward him; his "
  "hand stops at the midpoint and the teen receives it.\n"
  "PANEL 5 (bottom right, horizontal): close on the dark-haired teen — the brush pauses above the "
  "blank sheet and he looks up-right rather than starting the first line.\n"
  "PANEL 6 (bottom left, dominant horizontal, the focal panel): the blank headquarters sheet fills "
  "the foreground; the dark-haired teen's hand holds the brush a hair above it at frame left; the "
  "blond teen has withdrawn his hand at frame right and meets his eye-line across the empty paper. "
  "The sheet carries NO drawing and NO readable words. " + L_KITCHEN
  + SAY((1, SAS16, "upper right", "THE OLD FORCE USED THE COMPOUND."),
        (2, BOY16, "upper right", "AND THE NAKA SHRINE FOR SECRET MEETINGS."),
        (2, BOY16, "upper left", "THAT DOESN'T MAKE IT A HEADQUARTERS."),
        (3, SAS16, "upper right", "THEN WE BUILD ONE. WE'LL NEED RESOURCES."),
        (4, BOY16, "upper right", "FIRST, DRAW THE PLANS."),
        (5, SAS16, "upper right", "YOU HAVEN'T ANSWERED."),
        (6, BOY16, "upper left", "THE COUNCIL COMES FIRST."))
  + TAILS + "PANEL 4 (the blond teen, \"FIRST, DRAW THE PLANS.\") closes the MIDDLE row at reader-LEFT "
    "and PANEL 5 (the dark-haired teen, \"YOU HAVEN'T ANSWERED.\") opens the BOTTOM row at "
    "reader-RIGHT, wholly below it, so the instruction is read before the complaint about it. In "
    "PANEL 6 the balloon \"THE COUNCIL COMES FIRST.\" belongs to the BLOND TEEN at frame RIGHT: "
    "place it in the upper left as stated but draw a long tail crossing the panel to HIS mouth, "
    "clear of the dark-haired teen's head and hair at frame left.",
  R("naruto_v4_black", "sasuke_16", "env_uchiha_compound"), "low"),

 # ---- Spread 9: called to account --------------------------------------------------
 ("p17", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=7),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, SAS16, ANBU) + BLACKFIT + TABLE +
  "SEVEN panels. PAGE GRID — THIS IS THE PANEL LAYOUT AND NOTHING MAY CROSS A TIER LINE. The page "
  "is divided into horizontal TIERS that each run the full width of the paper, stacked top to "
  "bottom, separated by an unbroken horizontal gutter that crosses the whole page. Inside a tier "
  "the panels are read RIGHT TO LEFT. No panel is taller than its own tier and no panel spans, "
  "straddles or reaches into the tier above or below it. TIER 1 is PANEL 1 alone, full width. TIER "
  "2 holds PANEL 2 at the RIGHT and PANEL 3 at the LEFT. TIER 3, the bottom tier, holds PANEL 4 at "
  "the RIGHT, PANEL 5 in the CENTRE, and in its LEFT third PANEL 6 stacked directly above PANEL 7. "
  "Panel 4 sits BELOW panel 3, and panel 6 sits to the LEFT of panel 5. Public authority "
  "interrupts private planning.\n"
  "PANEL 1 (top band, full width): wide kitchen — the blond teen eats in silence at frame right, "
  "the dark-haired teen studies the blank headquarters sheet at frame left; both look toward the "
  "unseen front door in the same instant.\n"
  "PANEL 2 (middle right, vertical): doorway — the dark-haired teen opens from frame left; the "
  "owl-masked ANBU stands frame right outside, mask directed at him, eyes hidden.\n"
  "PANEL 3 (middle left, vertical): reverse on the ANBU with the teen's shoulder foreground left.\n"
  "PANEL 4 (bottom right, small horizontal): the dark-haired teen closes the door between them; "
  "the ANBU stays visible through the narrowing gap; the teen looks left into the house.\n"
  "PANEL 5 (bottom centre, horizontal): the teen returns to the kitchen; the blond teen has "
  "already stood at frame right and looks toward him.\n"
  "PANEL 6 (bottom left upper, horizontal): close on the blond teen fastening one glove, eye-line "
  "left. The dark-haired teen is NOT drawn in this panel.\n"
  "PANEL 7 (bottom left lower, horizontal): two-shot — the blond teen right and the dark-haired "
  "teen left stand on either side of the still-blank headquarters sheet; they look down once, then "
  "at each other. " + L_KITCHEN
  + SAY((2, SAS16, "upper right", "WHAT IS IT?"),
        (3, ANBU_S, "upper right", "YOU AND NARUTO ARE WANTED IN THE COUNCIL CHAMBER. NOW."),
        (4, SAS16, "upper right", "I'LL GET HIM."),
        (5, SAS16, "upper right", "WE'RE SUMMONED."),
        (6, BOY16, "upper right", "THEY'RE IMPATIENT."),
        (6, OFF(SAS16), "upper left", "ABOUT THE CLAN SEAT?"),
        (7, BOY16, "upper right", "ABOUT EVERYTHING THEY CAN'T CONTROL."),
        (7, SAS16, "upper centre", "THAT WORKS FOR YOU?"),
        (7, BOY16, "upper left", "YES."))
  + SFX(1, "KNOCK", "Upper left near the hallway; keep it clear of both faces.")
  + TAILS + "PANEL 3 (the owl-masked ANBU's summons) closes the MIDDLE row at reader-LEFT, and PANELS 4, "
    "5, 6 and 7 all sit BELOW it: PANEL 4 at bottom-right, PANEL 5 in the bottom centre, PANEL 6 "
    "above PANEL 7 in the bottom-left corner. So the summons is heard before \"I'LL GET HIM.\", "
    "and \"WE'RE SUMMONED.\" is read before \"THEY'RE IMPATIENT.\" In PANEL 7 the balloon "
    "\"YES.\" is the BLOND TEEN's and he stands at frame RIGHT, so its tail is drawn "
    "LONG: it leaves the balloon on the left of the panel and travels the whole way across "
    "to his mouth at frame right, passing clear of the dark-haired teen. It is never "
    "tail-less and its point never stops on the dark-haired teen's head, hair or shoulder "
    "at frame left.",
  R("naruto_v4_black", "sasuke_16", "env_uchiha_compound"), "low"),

 ("p18", dict(scene="establishing", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + SASUKE16.format(i=2) + ENV.format(i=3) + ENV.format(i=4)
  + ONLY(BOY16, SAS16, ANBU) + BLACKFIT +
  "FIVE panels. LAST PAGE OF THE CHAPTER — it stops OUTSIDE the closed council doors. Image 3 is "
  "the Uchiha house entry, image 4 the council chamber exterior. Nobody reaches for a handle and "
  "the doors never open.\n"
  "PANEL 1 (top right, horizontal): interior entry — the dark-haired teen stands frame left by the "
  "closed door and looks right at the blond teen approaching from the hall. The waiting ANBU is "
  "NOT visible through the wall.\n"
  "PANEL 2 (top left, horizontal): the teen reopens the door with his left hand as the blond teen "
  "passes him toward the centre of the entry seal; the blond teen's eye-line is forward, the teen "
  "turns to follow.\n"
  "PANEL 3 (middle right, vertical): SILENT — the blond teen disappears upward-left in a "
  "controlled curl of ORANGE-RED flame drawn as flat opaque shapes. No text in this panel.\n"
  "PANEL 4 (middle left, vertical): SILENT — the dark-haired teen disappears upward-right in a "
  "separate swirl of leaves; through the open door behind him the owl-masked ANBU has just turned "
  "to launch after them. No text in this panel.\n"
  "PANEL 5 (bottom band, full width, dominant, the focal panel): SILENT low frontal exterior of "
  "the tall closed council doors — the blond teen has materialized frame right and the dark-haired "
  "teen frame left, shoulder to shoulder with a deliberate hand-width of space between them, both "
  "facing the still-closed doors. The owl-masked ANBU lands small in the deep background between "
  "the orange-red flame trail and the leaf trail. No text in this panel. " + L_DOORS
  + SAY((1, SAS16, "upper LEFT of the panel, immediately ABOVE the dark-haired teen's head "
            "at frame left", "HE'S STILL WAITING."),
        (2, BOY16, "upper right", "HE'LL FOLLOW."))
  + TAILS + "PANEL 5 shows the COUNCIL CHAMBER exterior from Image 4 and takes nothing from Image 3: tall "
    "formal stone administrative doors in a civic facade. There is NO Uchiha fan crest anywhere "
    "on those doors, walls, banners, lanterns or ground, no wooden clan gate, no compound gateway "
    "and no residential wall — the shunshin must plainly end somewhere else than where it "
    "started. In PANEL 1 \"HE'S STILL WAITING.\" belongs to the DARK-HAIRED teen standing at "
    "frame LEFT by the closed door. It is the only balloon in the panel, so place it on the "
    "LEFT of the panel directly above HIS head and draw a SHORT tail straight down to HIS "
    "mouth. It must not sit in the panel's upper-right corner, and its tail must never "
    "reach, point at or end on the blond teen approaching from the hall at frame right.",
  R("naruto_v4_black", "sasuke_16", "env_uchiha_compound", "env_konoha_council_chamber"), "high"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch11" / "raw", HERE / "v5ch11" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
