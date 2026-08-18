"""Volume 5, Chapter 7 — "The Snake's Last Skin". 24 pages.

Source: fic ch14:9-371, with continuity carried from ch13:67-77. Translated 1:1 from
story/volume_05/drafts/ch07_the_snakes_last_skin.md — every balloon, card and sound effect in
the `name` appears here with its exact panel, position and wording. Reading order is RIGHT TO
LEFT; every multi-panel page states it.

This is the volume's fight chapter and it contains deaths. Every violent page states that impact
is drawn as FLAT OPAQUE shapes with hard outlines, motion lines and posture, with no injury
detail, no blood and no gore — a moderation refusal costs a whole page.

NOTE ON MISSING REFERENCE SHEETS: Ōnoki, his granddaughter and the four Sound guards have no
reference images in refs/images. They are therefore bound by full written description instead,
the same way the Root agents were handled in v5ch01 p03, and every page that uses them says so.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, KAB, OFF, ONLY, ORO, PALEONE, R, SAY, SFX, SPEC, ZET  # noqa: E402
from prompts_v4 import (KIRI_REBELS, MANGEKYO_EYE, N16_SPEAKER, N16_SWORD,  # noqa: E402
                        YAGURA_HUMAN)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")

# ---------------------------------------------------------------- names used in balloon tails
NAR = N16_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZWHITE = "the plant creature's chalk-white half"
ZBLACK = "the plant creature's pure black half"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")

# ---------------------------------------------------------------- cast without reference sheets
ONOKI_D = ("the Tsuchikage — he has NO reference sheet and must be drawn from this description "
           "alone: a tiny ancient man barely waist-high to an adult, with a large rounded red "
           "nose, a small triangular grey moustache and chin beard, a heavy lined brow, a flat "
           "wide-brimmed kage hat with a red front panel, and layered green and red robes")
ONOKI = "the tiny old Tsuchikage with the red nose and the grey beard"
GDAU_D = ("his granddaughter — she has NO reference sheet and must be drawn from this description "
          "alone: a young Iwa kunoichi with straight black hair cut level with her jaw, pink "
          "eyes, a sleeveless dark red top over a mesh undershirt, and a plain forehead protector")
GDAU = "the young black-haired Iwa kunoichi in the doorway"

SOUND4 = ("the four Sound guards — none of them has a reference sheet, so all four must be drawn "
          "from this description alone and must look completely different from one another. "
          "JIRŌBŌ is a very large heavy-set teenage boy with short orange hair standing in a wide "
          "crest and a dark high-collared tunic. TAYUYA is a slim girl with long dark red hair "
          "under a close-fitting black cap carrying two short horn-like points, a bamboo flute at "
          "her belt. SAKON is a slender pale youth with light grey-blue hair falling over his "
          "right eye and dark green markings under both eyes. KIDŌMARU is a lean dark-skinned "
          "youth with black hair pulled into a topknot, a spider-marked forehead protector and "
          "extra arms folded along his sides")
JIRO = "the very large orange-crested Sound boy"
TAY = "the red-haired Sound girl in the horned black cap"
SAK = "the grey-blue-haired Sound youth with the green face markings"
KIDO = "the dark-skinned six-armed Sound archer with the topknot"

# ---------------------------------------------------------------- Sound Four identity
# NONE of the four has a reference sheet in refs/images, so nothing binds their faces to an
# "Image {i}" index and the model silently substitutes one for another whenever two of them share
# a panel. First pass: Kidōmaru was drawn with Sakon's design on p12, Tayuya was drawn firing
# Kidōmaru's bow on p14, and a dead Sakon stood in the living file on p11. Written description is
# the only lever available, so it is stated ONCE here and attached to every page holding more than
# one of them.
FOUR = (
    "SOUND FOUR IDENTITY LOCK — READ THIS AS IF IT WERE FOUR REFERENCE SHEETS. None of these four "
    "has a reference image, so they are drawn from this description alone and they are NOT "
    "interchangeable. They differ in SKIN TONE, HAIR COLOUR, HAIR SHAPE, SEX, BUILD and NUMBER OF "
    "ARMS, and no panel may swap, merge, mirror or substitute one for another:\n"
    "  JIRŌBŌ — a very large heavy-set BOY, by far the biggest and widest of the four, pale-tan "
    "skin, SHORT BRIGHT ORANGE hair standing up in one wide crest, no headgear, a dark "
    "high-collared sleeveless tunic. Exactly TWO arms. He carries no weapon.\n"
    "  TAYUYA — the only GIRL of the four and the smallest, slim, with LONG DARK-RED HAIR falling "
    "from under a close-fitting BLACK CAP that carries two short horn-like points, and a bamboo "
    "FLUTE at her belt. Exactly TWO arms. She NEVER holds a bow and NEVER shoots an arrow.\n"
    "  SAKON — a slender youth with VERY PALE skin and LIGHT GREY-BLUE hair falling over his "
    "right eye, dark green markings under both eyes, a cream sleeveless top. Exactly TWO arms and "
    "ordinary human anatomy. He has NO bow, NO topknot, NO spider marking and NO extra arms.\n"
    "  KIDŌMARU — THE ARCHER. A lean youth with DARK BROWN SKIN, the darkest skin of anyone on "
    "the page, BLACK hair pulled tightly into a high TOPKNOT, a forehead protector marked with a "
    "spider, and SIX ARMS: the ordinary pair plus TWO EXTRA PAIRS folded along his sides, all six "
    "visible whenever his torso is in frame. Every bow and every arrow in this chapter belongs to "
    "HIM and to nobody else. He is never pale-skinned, never blue- or red-haired, never female, "
    "and never has only two arms.\n"
    "Before drawing any guard, decide which of these four he is and give him ALL of that entry's "
    "features. A figure that mixes two entries is a failed page. ")

# ---------------------------------------------------------------- the death ledger
# The chapter's dominant first-pass failure was not reading order: it was dead combatants standing
# back up. This states, page by page, who is dead, in what visible state, and where the remains
# lie, and it is attached to every page from p09 (the first death) to p16 (the state panel).
DEATHS = (
    "DEATH LEDGER — A HARD CONTINUITY RULE THAT OUTRANKS ANY PANEL DESCRIPTION IT CONFLICTS WITH. "
    "A guard who has died NEVER stands, walks, fights, dodges, speaks, reacts, holds a weapon, "
    "fires an arrow or appears whole again on any later page. He stays exactly where he fell, in "
    "exactly the state listed here, in every panel that shows that part of the floor:\n"
    "  SAKON (pale skin, light grey-blue hair over the right eye, green eye markings, two arms) "
    "dies on PAGE 9, ignited by black flame. From PAGE 10 onward he is a still, flat, BLACKENED "
    "BODY lying at WEST-OF-CENTRE, and he is dead for the whole of pages 10 to 24.\n"
    "  TAYUYA (the girl — long dark-red hair, horned black cap, flute) dies on PAGE 11 under a "
    "contact lightning discharge. From that moment she is a HEAP OF FLAT GREY ASH beside the "
    "EASTERN pillar — no body, no limbs, no face, no cap — and she is dead for the whole of pages "
    "12 to 24. She never fires a bow, because she never had one.\n"
    "  JIRŌBŌ (the very large orange-crested boy) dies on PAGE 14. From that moment he is a SLACK "
    "BODY: held upright against the EAST wall, then stuck full of arrows, then hung in white web "
    "at west-of-centre from PAGE 15 onward. He is dead for the whole of pages 15 to 24.\n"
    "  KIDŌMARU (dark brown skin, black topknot, six arms — the archer) is the LAST of the four "
    "alive and the ONLY one who ever holds a bow. He dies on PAGE 15. From that moment he is FLAT "
    "CHARRED BLACK-GREY REMAINS at WEST-OF-CENTRE, and he is dead for the whole of pages 16 to "
    "24.\n"
    "COUNT THE LIVING GUARDS BEFORE DRAWING. Page 9 opens with four and closes with three. Pages "
    "10 and 11 open with three; page 11 closes with two. Pages 12, 13 and 14 open with two; page "
    "14 closes with one. Page 15 opens with one and closes with none. Page 16 onward has none at "
    "all. Never draw more living guards than that count, and never place a dead one among the "
    "living. ")

# ---------------------------------------------------------------- forms and perceived-world tails
WSNAKE = ("Image {i} is the FORM REFERENCE for the giant serpent's ANATOMY AND SCALE ONLY — take "
          "its coiled body mass, its head shape and its size against a human being, and nothing "
          "else. Orochimaru's true form is CHALK-WHITE, never brown or tan, and its whole body is "
          "packed together out of hundreds of smaller white snakes, with a pale human-like face "
          "set at the front of the head. Ignore the reference's colours, its patterns, its "
          "layout and its white background. ")
NARP = "the blond teen standing inside the perceived world"
PMOUTH = "the perceived white snake's open mouth"
PFACE = "the perceived pale snake-face of Orochimaru"

# ---------------------------------------------------------------- state locks
GEAR = ("His red segmented armour is clean and repaired, the dark purple gunbai stays strapped "
        "flat across his back in every panel and never becomes a sword, and his plain replacement "
        "sash sword sits sheathed at his LEFT hip unless this page says he has drawn, dropped or "
        "sheathed it. It is a plain straight sword and is never Kusanagi. ")
ARM = ("His LEFT forearm is bruised and numb: it hangs lower than the right, trembles slightly, "
       "and he never grabs, blocks or bears weight with it. There is no open wound and no blood. ")
EMS = ("Naruto's left eye is ACTIVE: a blood-red iris with one black centre ring and six broad "
       "black blades. This is a physical eye pattern painted on the eye itself, never a glow, an "
       "aura or a light beam. ")
IMPACT = ("VIOLENCE RULE FOR THIS PAGE: every impact, death and technique contact is drawn as "
          "FLAT OPAQUE graphic shapes with hard black outlines, motion lines, speed lines and "
          "posture alone — no injury detail, no blood, no gore, no wounds, no torn clothing and "
          "no red fluid anywhere on this page. A body that has stopped moving is shown by slack "
          "posture and a flat silhouette, never by damage. ")
FLAT = ("All lightning, wind, black flame, fire and chakra are FLAT OPAQUE shapes with hard black "
        "outlines. They do NOT glow and do NOT wash the scene out: the stone floor, both pillars, "
        "the dais, the walls and every figure stay fully drawn and legible through and around "
        "them. ")
ROOM = ("Fixed geography: a rectangular underground stone hall with the raised dais and throne "
        "against the NORTH wall, the only entrance in the SOUTH wall, and two square stone "
        "pillars — P-W on the west side and P-E on the east side — standing at the same distance "
        "from the entrance. No panel may invent another exit, pillar, balcony, stair or window, "
        "or change the distance between these landmarks. ")

# ---------------------------------------------------------------- light
L_IWA = "Lighting: hard dry morning light through a stone window, dust in the air, flat shadows. "
L_ROCK = "Lighting: clean high morning light over bare grey Earth Country rock, hard black shadows. "
L_HALL = ("Lighting: cold torch-lit gloom inside a windowless underground stone hall — hard pools "
          "of light with deep flat black between them. ")
L_VOID = ("Lighting: no environment light at all — an endless black field crossed by hard flat red "
          "bands, the figures lit evenly with no floor, no horizon and no scenery. ")
L_EXIT = "Lighting: flat pale Earth Country daylight against a dry cliff face, dust hanging low. "

PAGES = [
 # ---- Spread 1: the threat Iwa refused to see --------------------------------------
 ("p01", dict(scene="establishing", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1)
  + ONLY(ONOKI_D, GDAU_D,
         "the blond older teen appearing ONLY as a printed portrait inside the open bingo book, "
         "never present in the room and never drawn as a person here") +
  "FIVE panels. A distant village turns a report into a strategic problem.\n"
  "PANEL 1 (narrow strip across the top): wide exterior of a stone-spired mountain village and "
  "its broad round kage tower under a hard morning sky. NO people. The UPPER RIGHT of this panel "
  "is EMPTY SKY — no rock, cloud, bird, balloon or effect may enter it — and carries only the "
  "chapter marker; the LOWER LEFT is a second clear patch reserved for the location card.\n"
  "PANEL 2 (upper right of the stepped middle row): close on an open book lying on a desk. The "
  "right-hand page carries a printed portrait of the blond older teen in red armour with an "
  "S-rank mark beside it; the portrait and that single mark are the only legible things. ALL "
  "other printed body text on both pages is ILLEGIBLE SCRIBBLE, not readable words. A small "
  "wrinkled hand pins the lower edge of the page.\n"
  "PANEL 3 (middle centre): tight close-up of the tiny old man's visible eye travelling down the "
  "portrait, from the long blond hair to the red armour and the active red eye.\n"
  "PANEL 4 (middle left): a second close angle on the same printed page, tilted — the portrait's "
  "long-haired armoured silhouette deliberately echoes an old Uchiha war-figure. Do NOT draw a "
  "ghost, an apparition or a second figure; the echo is in the silhouette only.\n"
  "PANEL 5 (wide band across the bottom): the old man sits very small behind the desk in deep "
  "space while the open book dominates the foreground, cropped by the panel edge; the young "
  "kunoichi leans in through a doorway at the far left. " + L_IWA +
  'LETTERING: in the protected EMPTY SKY at the upper right of PANEL 1, write the chapter marker '
  'in bold upright English capitals on one line: "CHAPTER 7 — THE SNAKE\'S LAST SKIN". It is a '
  'tail-less title, not a balloon. In the protected clear patch at the LOWER LEFT of PANEL 1, '
  'draw a plain rectangular narration box with a thin black border, no tail, containing only the '
  'word: "IWAGAKURE". '
  + SAY((3, ONOKI, "upper right", "MINATO'S SON."),
        (4, ONOKI, "upper right", "AN UCHIHA."),
        (4, ONOKI, "upper left", "AND NOW HE LOOKS LIKE HIM."),
        (5, GDAU, "upper right", "OLD MAN? YOU LOOK LIKE YOU'VE SEEN A GHOST.")),
  R("naruto_v4_armor_sword"), "high"),

 ("p02", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV.format(i=4)
  + ONLY(ONOKI_D, GDAU_D,
         "the blond older teen appearing ONLY as a printed portrait in the book and as a "
         "reflection in the old man's eyes",
         "the short Fourth Mizukage and the surviving Kiri rebels appearing ONLY inside one "
         "hard-edged recalled report image, never in the office") +
  "FIVE panels. Fear is converted into observation, not an attack order.\n"
  "PANEL 1 (top right): medium close-up — the old man closes the book halfway, keeping one finger "
  "inside the page, eyes lowered.\n"
  "PANEL 2 (top left): medium — the young kunoichi folds her arms in the doorway, facing right "
  "toward him.\n"
  "PANEL 3 (thin strip across the middle, full width): a HARD-EDGED recalled report image with "
  "slightly desaturated colour — a ruined battlefield crater under drained grey light, the short "
  "Fourth Mizukage lying motionless and small at the far left, surviving mist-shinobi converging "
  "along the crater rim behind him. No orange warrior, no black fire and no invented combat "
  "appears in this image.\n"
  "PANEL 4 (dominant lower right): extreme close-up of both of the old man's eyes filling the "
  "panel — the armoured portrait is reflected small and identical in each eye.\n"
  "PANEL 5 (low band across the bottom): low angle across the desktop — he shuts the book flat "
  "and leaves his hand resting on it instead of filing it away. " + L_IWA
  + SAY((1, ONOKI, "upper right", "NOT A GHOST."),
        (2, GDAU, "upper right", "THEN WHAT?"),
        (3, OFF(ONOKI), "upper right", "A BOY I REFUSED TO SEE."),
        (4, ONOKI, "upper right", "S-RANK IS NO LONGER AN EXAGGERATION."),
        (5, ONOKI, "upper right", "NO MOVE YET."),
        (5, ONOKI, "upper left", "I WANT EVERY REPORT."))
  + "THE PANEL 4 BALLOON IS THE MOST IMPORTANT LINE ON THIS PAGE AND ITS FIRST LETTER CARRIES THE "
    "WHOLE MEANING. It reads exactly \"S-RANK IS NO LONGER AN EXAGGERATION.\" The first word is "
    "spelled with the single capital letter S, then a hyphen, then R-A-N-K — S-hyphen-R-A-N-K. It "
    "is NEVER A-RANK, never B-RANK, never C-RANK and never any letter other than S. The printed "
    "bingo-book page in PANEL 2 carries an S mark for the same reason, and a later page has a "
    "guard ask \"THIS IS THE S-RANK?\" — any other letter inverts the line's meaning and "
    "contradicts the rest of the chapter. Letter every balloon on this page once, with no "
    "doubled, ghosted or overprinted text. ",
  R("naruto_v4_armor_sword", "yagura_human", "kiri_rebel_mob", "env_kiri_battlefield_crater"),
  "low"),

 # ---- Spread 2: risk by choice -----------------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ZOR + ONLY(NAR, ZETSU) + GEAR +
  "SIX panels. He gives up certainty on purpose; the creature tests the decision.\n"
  "PANEL 1 (wide band across the top): long shot — the blond teen at the RIGHT and the plant "
  "creature at the LEFT travel right-to-left through a broken ridge of bare grey rock. Neither "
  "looks at the other. The upper right of this panel stays clear for the location card.\n"
  "PANEL 2 (middle right): side two-shot at walking pace — the teen at right in profile facing "
  "left, the creature half a pace behind him at the left edge. Neither slows.\n"
  "PANEL 3 (middle left): close-up — the creature turns its two-toned face right toward the teen "
  "outside the panel.\n"
  "PANEL 4 (lower right): tight profile close-up — the teen faces left, eyes down on the trail, "
  "not on the creature.\n"
  "PANEL 5 (lower centre): close-up — the creature faces right, mouth open on the question, eyes "
  "narrowed rather than amused.\n"
  "PANEL 6 (long strip across the bottom): wide side shot — the teen steps over a narrow ravine "
  "without looking down, right foot leading; the creature follows through the rock behind him. "
  + L_ROCK
  + CAP(1, "upper right", "EARTH COUNTRY")
  + SAY((2, NAR, "upper right", "REMOVE THE SPORE FROM DANZŌ."),
        (3, ZWHITE, "upper right", "YOU WANT TO STOP WATCHING HIM?"),
        (4, NAR, "upper right", "I WANT TO STOP KNOWING EVERY MOVE BEFORE HE MAKES IT."),
        (5, ZBLACK, "upper right", "INFORMATION KEEPS YOU ALIVE."),
        (6, NAR, "upper right", "UNCERTAINTY KEEPS ME ALERT.")),
  R("naruto_v4_armor_sword", "zetsu"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ZOR
  + ONLY(NAR, ZETSU) + GEAR +
  "SIX panels. The choice is locked and the two jobs are split.\n"
  "PANEL 1 (top right): medium — the creature rises out of a rock face slightly ahead of the teen "
  "and turns back toward him; the teen enters from the right edge.\n"
  "PANEL 2 (top left): medium close-up — the teen stops walking for the first time, weight "
  "settling, facing left.\n"
  "PANEL 3 (middle right): tight close-up — the creature's two halves turn toward each other, "
  "then both eyes come back to the right toward the teen off-panel.\n"
  "PANEL 4 (middle left): medium profile — the teen resumes walking left, shoulder cropped by the "
  "panel edge.\n"
  "PANEL 5 (dominant panel, lower right and running most of the page width): medium-long shot of "
  "a disguised stone seal set into the base of a dry cliff — a flat disc of carved rock flush "
  "with the stone. The teen stands at the RIGHT of it facing left; the creature rises out of the "
  "ground at the LEFT of it. Any carving on the seal is ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 6 (narrow strip across the bottom): split departure — at the right the teen's gloved "
  "hands press the seal open on a black gap; at the left the creature is already sinking through "
  "the ground, only its head and shoulders left above the rock. " + L_ROCK
  + SAY((1, ZETSU, "upper right", "DANZŌ HAS AN ARMY. HE DOES NOT NEED LEGAL GROUND."),
        (2, NAR, "upper right", "HE IS A THREAT."),
        (2, NAR, "upper left", "HE HAS NOT YET EARNED DEATH."),
        (3, ZWHITE, "upper right", "AND IF THE RISK COSTS YOU?"),
        (4, NAR, "upper right", "THEN I PAY FOR CHOOSING IT."),
        (5, NAR, "upper right", "KARIN HAS WAITED LONG ENOUGH."),
        (5, ZWHITE, "upper left", "SHE NEARLY TORE MY CLONE APART."),
        (6, NAR, "upper right", "FIND THE MASK."),
        (6, ZETSU, "upper left", "YOU TAKE THE SNAKE.")),
  R("naruto_v4_armor_sword", "zetsu", "env_oto_hidden_base"), "low"),

 # ---- Spread 3: the throne is bait -------------------------------------------------
 ("p05", dict(scene="establishing", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4)
  + ENV.format(i=5) + ONLY(NAR, PALEONE, SPEC, SOUND4) + GEAR + ROOM 
  + FOUR +
  "SIX panels. Route, room geometry, every weapon, and a false calm.\n"
  "PANEL 1 (top band, full width): wide corridor shot — the teen walks alone away from the reader "
  "down a low stone corridor; two taut trip-wires cross the passage and a raised pressure plate "
  "sits between them, and his stride threads the gap. No text in this panel.\n"
  "PANEL 2 (narrow strip under it): extreme close-up of his right eye, the red pattern turned "
  "up-left as it follows a faint trail of residue toward the far end. No text in this panel.\n"
  "PANEL 3 (tall dominant panel occupying the right half of the lower page): high establishing "
  "angle from above the SOUTH doorway looking north — the whole rectangular hall is visible at "
  "once. The blond teen stands just inside the doorway at south-centre; the four Sound guards "
  "stand shoulder to shoulder in one west-to-east line across the middle of the room; the pale "
  "long-haired man sits on the throne on the raised dais against the north wall; the grey-haired "
  "medic in round glasses stands at the eastern stair of that dais. Both square pillars are "
  "visible. NOBODY HAS MOVED YET.\n"
  "PANEL 4 (upper left of the lower half): medium — the pale man on the throne, chin resting on "
  "one hand, facing forward.\n"
  "PANEL 5 (middle left): medium — the teen still just inside the door, gunbai flat on his back, "
  "sword sheathed at his left hip, arms loose.\n"
  "PANEL 6 (bottom left): tight close-up — the pale man's smile holds while the fingers propping "
  "his cheek visibly tense. " + L_HALL
  + SAY((4, PALEONE, "upper right", "WELCOME, NARUTO-KUN."),
        (4, PALEONE, "upper left", "KIRI MADE YOU DIFFICULT TO IGNORE."),
        (5, NAR, "upper right", "YOU COULD NOT HAVE TOUCHED YAGURA IN THAT BODY."),
        (6, PALEONE, "upper right", "THINGS WILL NOT PROCEED AS THEY DID LAST TIME.")),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_hideout_corridor",
    "env_oto_throne_hall"), "medium"),

 ("p06", dict(scene="action", light="interior", cast="small_group", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3)
  + MANGEKYO_EYE.format(i=4) + ENV.format(i=5)
  + ONLY(NAR, PALEONE, SPEC, SOUND4) + GEAR + EMS + ROOM + FLAT 
  + FOUR +
  "SEVEN panels. The medic is removed before the fight starts.\n"
  "PANEL 1 (top right): extreme close-up — the teen's left eye changes state on the page: the "
  "six-bladed red pattern replaces the ordinary one. It is a change of the eye itself.\n"
  "PANEL 2 (top left): insert close-up — two pale fingers lift from the throne's stone arm; the "
  "four guards' heads turn toward the signal in the blurred background.\n"
  "PANEL 3 (middle right): medium over the teen's shoulder — his gaze sweeps past the seated pale "
  "man and, for one frame, meets the medic at the eastern dais stair. A thin reflected red "
  "six-bladed pattern crosses the medic's round glasses. No text in this panel.\n"
  "PANEL 4 (middle centre): tight close-up — the medic's pupils stop tracking; his hands stay "
  "loose at his sides; he stands upright and does not fall. Nobody looks back at him. No text in "
  "this panel.\n"
  "PANEL 5 (middle left): medium — the red-haired girl in the horned cap steps one pace forward "
  "from the eastern end of the guards' line, facing right toward the teen.\n"
  "PANEL 6 (a narrow strip running the FULL WIDTH of the page, directly ABOVE the bottom panel — "
  "nothing sits to its left or to its right): medium close-up — the teen's eye-line returns from "
  "the dais to the four guards, head level. His two balloons sit inside this strip, the first "
  "further right than the second.\n"
  "PANEL 7 (dominant panel running the FULL WIDTH of the page across the very BOTTOM, below "
  "PANEL 6 — the last panel read): overhead angle looking straight down — the four "
  "guards sprint out of their line into a diamond around the teen at south-centre: the very large "
  "orange-crested boy two paces NORTH of him, the red-haired girl two paces EAST, the "
  "grey-blue-haired youth two paces WEST, and the dark-skinned archer further north on the open "
  "line toward the dais. The medic is still frozen upright at the eastern stair and the pale man "
  "is still seated. " + L_HALL
  + SAY((1, NAR, "upper right", "YOU BROUGHT CHILDREN TO SPEND FOR YOU."),
        (2, OFF(PALEONE), "upper left", "GIVE OUR GUEST A PROPER WELCOME."),
        (5, TAY, "upper right", "WHO DO YOU THINK YOU ARE?"),
        (6, NAR, "upper right", "THE SOUND FOUR."),
        (6, NAR, "upper left", "YOUR LEADER IS ALREADY DEAD."),
        (7, NAR, "upper right", "COME, THEN."))
  + "THIS PAGE HAS EXACTLY SEVEN PANELS — do not invent an eighth. THE ANSWER MUST BE READ BEFORE "
    "THE CHALLENGE. \"THE SOUND FOUR.\" and \"YOUR LEADER IS ALREADY DEAD.\" are his reply to the "
    "red-haired girl's question and belong ONLY inside PANEL 6, the full-width strip. \"COME, "
    "THEN.\" is the challenge that follows and belongs ONLY inside PANEL 7, the overhead "
    "formation panel across the very bottom of the page; it never appears in a separate "
    "close-up, never sits beside PANEL 6, and never sits above or to the RIGHT of PANEL 6's two "
    "balloons. If \"COME, THEN.\" is read before \"THE SOUND FOUR.\", the page is wrong. ",
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "mangekyo_design",
    "env_oto_throne_hall"), "medium"),

 # ---- Spread 4: their strength is sequence -----------------------------------------
 ("p07", dict(scene="action", light="interior", cast="small_group", mood="violent", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, SOUND4) + GEAR + ROOM + IMPACT + FLAT 
  + FOUR +
  "SIX panels. A four-part relay, and the first physical cost. This page has NO speech balloons "
  "and NO captions — only the sound effects listed below.\n"
  "PANEL 1 (top right, canted): the orange-crested boy drives an unarmed left uppercut from the "
  "NORTH downward toward the teen at south-centre; the teen leans back to the south and the fist "
  "misses his chin by centimetres. Both his feet stay planted.\n"
  "PANEL 2 (top left, canted the other way): the red-haired girl's right-leg roundhouse enters "
  "from the EAST while he is still leaned back; he drops into a crouch and her heel crosses above "
  "his hair; she lands to his south-west.\n"
  "PANEL 3 (middle right): the grey-blue-haired youth jumps in from the WEST behind her landing; "
  "his descending right heel meets the teen's crossed forearms above his head. The teen is pinned "
  "low but nothing touches his skull.\n"
  "PANEL 4 (SMALL panel at the centre of the page, surrounded by the others): tight insert — the "
  "teen's red six-bladed eye looks past the pinning leg toward the EMPTY SPACE behind that "
  "attacker, not at the attacker. No text in this panel.\n"
  "PANEL 5 (middle left): the orange-crested boy completes the relay with a right kick from the "
  "NORTH into the teen's back. The kick lands flat on the dark purple gunbai strapped across that "
  "back — the fan takes the whole blow — and the momentum launches the teen south toward the "
  "entrance while the grey-blue-haired youth springs clear to the west.\n"
  "PANEL 6 (wide band across the bottom): the teen lands on both feet just inside the SOUTH wall "
  "and slides half a pace east along it, never touching or crossing it. The four reset between "
  "him and the dais — the orange-crested boy at centre, the red-haired girl east, the "
  "grey-blue-haired youth west, the archer north. His forearms still tremble. " + L_HALL
  + SFX(1, "WHUM", "Place it along the arc of the fist. ")
  + SFX(2, "KSHH", "Place it above the arc of the heel. ")
  + SFX(3, "KRAK", "Place it at the forearm-and-heel contact point. ")
  + SFX(5, "GONG", "Place it directly on the gunbai at the moment of contact. "),
  R("naruto_v4_armor_sword", "env_oto_throne_hall"), "low"),

 ("p08", dict(scene="action", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ENV.format(i=4) + ONLY(NAR, PALEONE, SOUND4) + GEAR + EMS + ROOM + IMPACT + FLAT 
  + FOUR +
  "SIX panels. He reads the relay and names the real problem.\n"
  "PANEL 1 (tall panel down the right edge): the dark-skinned archer stands at north-centre, feet "
  "planted, a pre-formed golden bow in his left hand and one golden arrow drawn back to his cheek "
  "with the right. The arrowhead points due SOUTH along the open lane. No text in this panel.\n"
  "PANEL 2 (tall panel beside it): the release — the arrow travels north to south past the teen's "
  "right cheek as he tilts west, then buries itself in the SOUTH wall beside the entrance. Draw "
  "the arrow's path as a hard straight line, not a blur.\n"
  "PANEL 3 (middle right): medium — the four stand shoulder to shoulder again at room centre, "
  "facing south, mistaking his defence for control.\n"
  "PANEL 4 (middle left): medium — the pale man watches from the dais with his chin on his hand. "
  "He does not warn them and does not look toward the frozen medic. No text in this panel.\n"
  "PANEL 5 (dominant panel, lower right, running most of the page width): the teen's red "
  "six-bladed eye fills the panel, and inside its reflection the sequence is drawn as FOUR flat "
  "linked arrows in order — displace, lower, fix, then the long straight arrow from the north. "
  "The reflection is a flat diagram, not a second scene.\n"
  "PANEL 6 (bottom left): medium close-up — the teen raises one hand into a single seal at chest "
  "height, all four still untransformed in the background. " + L_HALL
  + SAY((3, SAK, "upper right", "THIS IS THE S-RANK?"),
        (5, NAR, "upper right", "YOUR STRENGTH IS THE HANDOFF."),
        (6, NAR, "upper right", "THEN I END YOU BEFORE THE SEALS OPEN."))
  + SFX(2, "TWANG", "Small, at the bowstring. ")
  + SFX(2, "KRAK", "Large, at the wall where the arrow lands, cropped by the panel edge. "),
  R("naruto_v4_armor_sword", "orochimaru", "mangekyo_design", "env_oto_throne_hall"), "low"),

 # ---- Spread 5: break the handoff --------------------------------------------------
 ("p09", dict(scene="action", light="interior", cast="small_group", mood="violent", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3)
  + ONLY(NAR, SOUND4) + GEAR + EMS + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SIX panels. The formation breaks and their rescue instinct kills one of them.\n"
  "PANEL 1 (top right): medium — the teen finishes one hand seal just inside the SOUTH wall, "
  "inhales, and opens his mouth.\n"
  "PANEL 2 (wide band, upper left and across): a widening cone of wind leaves his MOUTH and "
  "travels south to north, drawn as flat hard-edged wedges with black outlines. The "
  "orange-crested boy and the red-haired girl lose their footing and slide north; the "
  "grey-blue-haired youth jumps clear to the WEST toward the western pillar and the archer jumps "
  "clear to the EAST toward the eastern pillar. The floor and both pillars stay fully drawn "
  "through the wind.\n"
  "PANEL 3 (middle right): fast medium — he ignores the two blown north and flashes WEST instead, "
  "arriving beside the grey-blue-haired youth's landing point at the western pillar.\n"
  "PANEL 4 (middle centre): the low sweep — his leg travels south to north; the youth jumps "
  "horizontal over it; the teen converts the miss into an upward kick that meets the youth's "
  "sternum and sends him north. Flat impact shapes only.\n"
  "PANEL 5 (middle left): the red-haired girl recovers to the east and kicks at his temple; he "
  "catches her ankle in both hands. The orange-crested boy charges from the north to rescue her; "
  "the teen rotates once and throws her straight into him and he catches her. The "
  "grey-blue-haired youth sprints in from the west to protect them both.\n"
  "PANEL 6 (dominant panel across the bottom): the teen's red six-bladed eye is fixed on the "
  "sprinting youth's chest — NOTHING leaves his hands and NOTHING leaves his mouth. Flat opaque "
  "BLACK flame with hard white outlines ignites directly at that point on the chest before "
  "contact; the youth collapses at exact west-of-centre and stays there. The teen holds one pace "
  "east of him; the other two are still tangled to the north; the archer is isolated at the "
  "eastern pillar. Black flame, no injury detail. " + L_HALL
  + SAY((1, NAR, "upper right", "WIND RELEASE—"),
        (2, NAR, "upper left", "GREAT BREAKTHROUGH."),
        (6, NAR, "upper right", "AMATERASU."))
  + SFX(2, "WHOOOM", "Inside the wind cone, cropped by the panel edge. ")
  + SFX(4, "THUD", "At the sternum contact point. ")
  + SFX(6, "FSSSH", "Embedded in the black flame shapes. "),
  R("naruto_v4_armor_sword", "mangekyo_design", "env_oto_throne_hall"), "medium"),

 ("p10", dict(scene="action", light="interior", cast="small_group", mood="violent", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, SOUND4) + GEAR + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SEVEN panels. An arrow answer, a clone, and a lost firing lane.\n"
  "PANEL 1 (tall panel down the right edge): the grey-blue-haired youth writhes at west-of-centre "
  "with flat black flame fixed to his torso; the teen draws his plain sash sword from his LEFT "
  "hip with the right hand, wind chakra running from his right palm along the edge as flat hard "
  "wedges, and raises it above the youth's neck. No injury detail.\n"
  "PANEL 2 (tall panel beside it): the archer at the eastern pillar draws an arrow level with the "
  "teen's ribs across the room.\n"
  "PANEL 3 (small panel, upper left): the teen lowers the sword and slides it back into the "
  "left-hip sheath, eyes never leaving the archer.\n"
  "PANEL 4 (middle band, full width): three arrows leave the bow in a staggered line from "
  "north-east to south-west. The teen backflips SOUTH once, then again; on the second inversion "
  "his hands cross into a clone seal hidden behind his torso. Draw the flip as one figure with "
  "ghosted motion phases, not two separate people.\n"
  "PANEL 5 (the RIGHT-HAND panel of a row of EXACTLY TWO small panels — PANEL 6 is its only "
  "neighbour and sits directly to its LEFT): the continuing figure reaches the SOUTH wall and the "
  "third arrow enters its chest. It is the clone. Flat shapes, no injury detail.\n"
  "PANEL 6 (the LEFT-HAND panel of that same two-panel row, immediately LEFT of PANEL 5): the "
  "struck figure bursts into a flat opaque smoke cloud against the wall.\n"
  "PANEL 7 (wide reveal running the FULL WIDTH of the page across the very BOTTOM, BELOW that "
  "two-panel row — nothing sits to its left or right): the archer has turned fully SOUTH toward "
  "the smoke, "
  "his back exposed to the north. The real teen is NOT in that sightline — he is pressed against "
  "the NORTH face of the eastern pillar, hidden from him. The grey-blue-haired youth lies still "
  "and blackened at exact west-of-centre. The orange-crested boy and the red-haired girl have "
  "moved east to cover the archer and now stand with him in one straight north-to-south file "
  "beside that pillar, all three facing SOUTH, none of them able to see the teen behind it. No "
  "text in this panel. " + L_HALL
  + SAY((1, NAR, "upper right", "I CAN END THIS QUICKLY."),
        (2, KIDO, "upper right", "TAKE ONE MORE STEP."),
        (3, NAR, "upper right", "THEN WATCH HIM BURN."))
  + SFX(4, "TWANG—TWANG—TWANG", "Three separate marks, one at each bow release. ")
  + SFX(6, "POOF", "Inside the smoke cloud. ")
  + "THE PANEL 2 BALLOON READS EXACTLY \"TAKE ONE MORE STEP.\" — four words, and the last one is "
    "STEP, spelled S-T-E-P. It is never MOTEP, MOTER, STEB or any other invented word. The PANEL "
    "1 balloon reads exactly \"I CAN END THIS QUICKLY.\" and the PANEL 3 balloon reads exactly "
    "\"THEN WATCH HIM BURN.\" Letter each of the three balloons ONCE, every word spelled out in "
    "full in ordinary English capitals, with no doubled, ghosted or overprinted text, no "
    "reversed or mirrored letters, and no invented words.\n"
    "THIS PAGE HAS EXACTLY SEVEN PANELS — do not add an eighth, and do not draw an empty stone "
    "corner as a panel of its own. THE CLONE IS HIT BEFORE IT BURSTS. The panel showing the arrow "
    "ENTERING the figure at the south wall must sit to the RIGHT of the panel showing the smoke "
    "cloud, so that reading right to left gives the strike first and the POOF second. The smoke "
    "cloud is NEVER to the right of the arrow strike, and the wide bottom reveal is never to the "
    "right of either — it runs the full width of the page below them both. ",
  R("naruto_v4_armor_sword", "env_oto_throne_hall"), "low"),

 # ---- Spread 6: two seals open -----------------------------------------------------
 ("p11", dict(scene="action", light="interior", cast="small_group", mood="violent", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, SOUND4) + GEAR + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SIX panels. The reposition pays off and costs him a great deal of chakra.\n"
  "PANEL 1 (narrow strip across the top): rear reveal — the teen steps out from the NORTH face of "
  "the eastern pillar one pace behind the orange-crested boy at the north end of the file. He "
  "forms two hand seals; flat lightning shapes crawl from his shoulders along both forearms and "
  "gather between his joined palms.\n"
  "PANEL 2 (wide diagonal band under it): a lightning dragon's head leaves the space between his "
  "palms and travels in ONE straight north-to-south line through the aligned backs of all three. "
  "All three are driven one pace further south and left paralysed with flat lightning branches "
  "clinging to their limbs. The floor and the pillar stay fully drawn through the lightning.\n"
  "PANEL 3 (middle right): ONE continuous action panel with FOUR ghosted phases of a single "
  "figure — never four separate people, and he never passes through a body. The teen flashes "
  "clockwise around the east side of the paralysed file to the archer at its south end, grips his "
  "throat left-handed, punches the gut, knees the ribs, throws him upward and kicks him "
  "west-north-west into the WESTERN pillar. Flat impact shapes only.\n"
  "PANEL 4 (middle left): medium — he pivots and kicks the orange-crested boy EAST, one pace clear "
  "of the file, keeping the same north-south position; the red-haired girl is left alone on her "
  "knees where she was.\n"
  "PANEL 5 (lower right): close two-shot — his right palm lies flat on the kneeling girl's "
  "forehead before the paralysis ends; flat lightning gathers through his whole body and converges "
  "into that palm, and his outline flares once as a hard-edged shape.\n"
  "PANEL 6 (dominant panel across the bottom): the contact discharge runs straight down through "
  "her from the forehead; she collapses into a heap of flat grey ASH at exactly the place she was "
  "kneeling. No body, no injury detail, no gore. The teen withdraws a smoking right hand and "
  "exhales once. " + L_HALL
  + SAY((1, NAR, "upper right", "LIGHTNING RELEASE—"),
        (2, NAR, "upper left", "LIGHTNING DRAGON."),
        (5, NAR, "upper right", "SIGH OF THE YELLOW DRAGON."))
  + SFX(2, "KRA-KOOOM", "Running the whole length of the dragon's path. ")
  + SFX(3, "KRAK", "At the western pillar where the archer lands. ")
  + SFX(6, "ZZZRAAAM", "Vertically through the discharge. ")
  + "EXACTLY THREE SOUND GUARDS ARE ALIVE ON THIS PAGE AND THIS IS THE PAGE THAT PREVIOUSLY GOT "
    "THEM WRONG. The north-to-south file that the lightning dragon passes through in PANEL 1 and "
    "PANEL 2 contains exactly these three, in this order: JIRŌBŌ, the very large orange-crested "
    "boy, at the NORTH end nearest the teen; TAYUYA, the slim GIRL with long dark-red hair under "
    "the horned black cap, in the MIDDLE; and KIDŌMARU, the dark-brown-skinned archer with the "
    "black topknot and SIX ARMS, at the SOUTH end. All three are drawn from behind with the "
    "dragon striking their aligned backs, and the red-haired girl is clearly present and clearly "
    "visible in BOTH panels — she does not vanish from the file and then reappear kneeling.\n"
    "SAKON IS DEAD. He was burned by black flame on the previous page. On this page he appears "
    "ONLY as a still, flat, blackened body lying on the floor at WEST-OF-CENTRE, far away from "
    "the file and from every action. He is NEVER standing, NEVER in the file, NEVER struck by the "
    "lightning, NEVER kicked, and NEVER drawn upright in any panel. No living figure anywhere on "
    "this page has his pale skin, his light grey-blue hair or his green under-eye markings. There "
    "are never more than three living guards in any panel; if a fourth upright guard appears, the "
    "page is wrong. ",
  R("naruto_v4_armor_sword", "env_oto_throne_hall"), "medium"),

 ("p12", dict(scene="action", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4)
  + ONLY(NAR, PALEONE, SPEC, SOUND4) + GEAR + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SIX panels. His prevention attempt fails for a reason the reader can see.\n"
  "PANEL 1 (top right): medium — the orange-crested boy digs both hands into the stone floor to "
  "stop his slide, east of the file; a dark curse pattern spreads from his neck across his face "
  "and torso as flat black markings. No text in this panel.\n"
  "PANEL 2 (top left): medium — the archer pulls himself off the cracked WESTERN pillar; the same "
  "flat black pattern spreads over him while a golden blade grows out of hardened material along "
  "his right forearm into his hand. His bow lies dropped beside the pillar.\n"
  "PANEL 3 (middle right): medium — the teen turns away from the heap of ash and flashes toward "
  "them; his right hand still smokes and his outline carries no chakra shape at all now.\n"
  "PANEL 4 (middle left): the orange-crested boy rips a slab of floor up and hurls it "
  "west-north-west straight across the teen's interception line toward the western pillar; the "
  "teen has to cut SOUTH to avoid it and the slab shatters against the pillar. The two curse "
  "patterns finish spreading in that bought second.\n"
  "PANEL 5 (dominant panel, lower right and running most of the width): both survivors stand fully "
  "transformed on opposite sides of the heap of ash — the orange-crested boy east of the file, the "
  "archer west at the cracked pillar. The teen is south of the ash along the same line and, as the "
  "broken slab passes him, draws the plain sash sword from his LEFT hip with his right hand and "
  "runs flat wind wedges from palm through hilt to edge. In the background the blackened body lies "
  "unmoved at west-of-centre, the pale man is still seated on the north dais, and the medic is "
  "still frozen upright at the eastern stair.\n"
  "PANEL 6 (bottom left): close-up — the teen adjusts the sword's angle, his red six-bladed eye "
  "tracking both of them. " + L_HALL
  + SAY((3, NAR, "upper right", "TOO SLOW."),
        (5, JIRO, "upper right", "NOW TRY."),
        (6, NAR, "upper right", "THE SEALS BOUGHT POWER."),
        (6, NAR, "upper left", "NOT JUDGMENT."))
  + SFX(4, "BRAK-KOOM", "At the pillar where the floor slab shatters, crossing the gutter. ")
  + "THE GUARD AT THE CRACKED WESTERN PILLAR IS KIDŌMARU AND NOBODY ELSE. In PANEL 2 and in PANEL "
    "5 the figure pulling himself off that pillar and growing the golden forearm blade has DARK "
    "BROWN SKIN, BLACK hair pulled into a high TOPKNOT, a spider-marked forehead protector, and "
    "SIX ARMS — the ordinary pair plus two extra pairs along his sides, all six drawn. He is NOT "
    "pale-skinned, NOT light-blue-haired, does NOT have hair falling over one eye, and NEVER has "
    "only two arms. SAKON IS DEAD: he lies as a still blackened body at west-of-centre in the "
    "background and is never the figure at the pillar and never upright anywhere on this page. "
    "Exactly TWO living guards appear on this page — Kidōmaru at the western pillar and JIRŌBŌ, "
    "the very large orange-crested boy, east of the file — plus Tayuya's heap of grey ash beside "
    "the eastern pillar, which is ash and not a person.\n"
    "Once the flat black curse-seal markings have spread over Kidōmaru and Jirōbō in PANELS 1, 2 "
    "and 5, those blotched black markings stay on their faces, arms and torsos in EVERY remaining "
    "panel of this page and on every later page either of them appears on. Their skin is never "
    "clean again. ",
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_oto_throne_hall"), "low"),

 # ---- Spread 7: power without judgment ---------------------------------------------
 ("p13", dict(scene="action", light="interior", cast="small_group", mood="violent", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, SOUND4) + GEAR + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SIX panels. The blade panels narrow; the last one is the biggest on the page.\n"
  "PANEL 1 (top right): the transformed archer charges east-south-east from the western pillar "
  "with the golden blade in his right hand; his downward cut forces the teen one pace SOUTH. The "
  "blades meet; nothing touches the teen's body. In the same panel's background the transformed "
  "orange-crested boy begins crossing WEST, passing north of the heap of ash.\n"
  "PANEL 2 (top left, narrower): the archer reverses into a horizontal neck cut travelling west to "
  "east; the teen catches it on the wind-coated edge and yields one pace WEST, sparks moving east "
  "as flat chips. In the clear background the orange-crested boy continues west along the same "
  "line — his route is seen, never hidden.\n"
  "PANEL 3 (middle right, narrower still): three fast thrusts at chest, sword wrist and thigh. The "
  "teen's red eye reads each one but the plain sword's shorter reach keeps him reacting and yields "
  "him one more pace WEST. Behind the blade line the orange-crested boy turns SOUTH and runs down "
  "to the teen's latitude, ending three paces due west of him.\n"
  "PANEL 4 (small panel, middle left): close-up on the archer noticing that the teen's LEFT hand "
  "hovers open instead of supporting the hilt. The orange-crested boy stands planted in the "
  "background; there is no hidden reposition.\n"
  "PANEL 5 (narrow strip): the archer abruptly crouches — a deliberate signal, not fatigue. The "
  "orange-crested boy drives due EAST at the teen with his right fist aimed at the face, while the "
  "archer body-flickers due WEST out of the engagement along the same latitude.\n"
  "PANEL 6 (dominant panel across the bottom): the teen catches the incoming fist on both "
  "forearms, the sword still trapped awkwardly in his right grip. The punch folds the guard and "
  "launches him four paces due EAST into the fixed EAST wall, his back embedded shallowly in the "
  "stone; the plain sword is torn out of his right hand and falls to the floor one pace inside "
  "that wall. His LEFT forearm is left hanging and numb — flat impact shapes, no injury detail and "
  "no blood. In the background the archer completes his flicker at west-of-centre, turns to face "
  "east and begins reforming the golden bow. " + L_HALL
  + SAY((4, KIDO, "upper right", "YOUR OFF HAND IS LATE."))
  + SFX(1, "KLANG", "At the blade clash. ")
  + SFX(6, "DOOM", "Large, at the forearms, overlapping both figures. ")
  + SFX(6, "KRAK", "Secondary, smaller, at the wall behind his back. ")
  + "EXACTLY TWO SOUND GUARDS ARE ALIVE ON THIS PAGE: KIDŌMARU, the dark-brown-skinned archer "
    "with the black topknot, the spider-marked forehead protector and SIX ARMS, and JIRŌBŌ, the "
    "very large orange-crested boy. Sakon and Tayuya are dead and appear nowhere on this page, "
    "not even in the background. BOTH survivors still carry the flat black CURSE-SEAL MARKINGS "
    "that spread over them on the previous page: dark blotched patterns across the face, arms and "
    "torso, clearly drawn in EVERY panel where their skin is visible, including the close-up of "
    "the archer noticing the late off hand. Neither of them is ever drawn clean-skinned or "
    "untransformed on this page. ",
  R("naruto_v4_armor_sword", "env_oto_throne_hall"), "low"),

 ("p14", dict(scene="action", light="interior", cast="two", mood="violent", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3)
  + ONLY(NAR, SOUND4) + GEAR + ARM + EMS + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SEVEN panels. Close range becomes eye contact, and the body becomes cover.\n"
  "PANEL 1 (tall panel down the right edge): the teen is still set into the EAST wall. The "
  "transformed orange-crested boy steps around the fallen sword without touching it, closes to "
  "half a pace and punches at his head with the left fist; the teen moves only his head south and "
  "the fist goes into the stone beside his ear.\n"
  "PANEL 2 (tall panel beside it): the attacker leans in close to pull his fist free and his eyes "
  "meet the teen's active red six-bladed eye. The teen's left forearm hangs lower than the right "
  "and visibly trembles.\n"
  "PANEL 3 (thin eye strip across the page): two eyes only, at less than a pace — the teen's red "
  "six-bladed left eye at the right of the strip and the attacker's widening eye at the left. No "
  "bodies, flat black behind.\n"
  "PANEL 4 (middle right): the transformed body goes completely slack; the teen catches the weight "
  "on his RIGHT arm alone, keeping the numb left clear of it.\n"
  "PANEL 5 (middle left): close insert — the teen's right index and middle fingertips rest on the "
  "slack chest over the heart; flat lightning leaves ONLY those two fingertips, passes through and "
  "exits into the wall behind. No injury detail, no blood, no gore.\n"
  "PANEL 6 (lower right): medium — he pulls the slack body off the wall and turns it to face "
  "west, holding it upright with the right arm, while at west-of-centre the archer completes the "
  "golden bow and looses a fan of arrows due EAST.\n"
  "PANEL 7 (wide band across the bottom): the arrows travel west to east and bury themselves in "
  "the back of the body he is holding; the teen is entirely behind it against the EAST wall. The "
  "archer stays at west-of-centre. The dropped plain sword still lies untouched on the floor one "
  "pace inside the east wall, exactly where it fell. Flat arrow shafts, no injury detail. "
  + L_HALL
  + SAY((2, NAR, "upper right", "NO ONE WARNED YOU?"),
        (3, NAR, "upper right", "TSUKUYOMI."),
        (5, NAR, "upper right", "FALSE DARKNESS."))
  + SFX(1, "KRAK", "At the wall beside his ear. ")
  + SFX(5, "TZAK", "At the fingertip contact point. ")
  + SFX(7, "THK—THK—THK", "Three separate marks across the arrows. ")
  + "THE ARCHER IN PANEL 6 AND PANEL 7 IS KIDŌMARU. He stands at west-of-centre, forms the golden "
    "bow and looses the fan of arrows due EAST, and he is a MALE youth with DARK BROWN SKIN, "
    "BLACK hair pulled into a high TOPKNOT, a spider-marked forehead protector, SIX ARMS and the "
    "black curse-seal markings from the previous pages. He is NEVER drawn as a girl, NEVER "
    "red-haired, NEVER wearing a horned black cap, and never has only two arms. TAYUYA IS DEAD — "
    "she was reduced to a heap of grey ash three pages ago — so no red-haired girl and no horned "
    "cap appears anywhere on this page, in any panel, in the foreground or the background. Apart "
    "from the blond teen and the slack body he is holding, Kidōmaru is the only living person on "
    "this page. ",
  R("naruto_v4_armor_sword", "mangekyo_design", "env_oto_throne_hall"), "low"),

 # ---- Spread 8: the last guard -----------------------------------------------------
 ("p15", dict(scene="action", light="interior", cast="two", mood="violent", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, SOUND4) + GEAR + ARM + ROOM + IMPACT + FLAT 
  + FOUR + DEATHS +
  "SIX panels. Distraction, rear reposition, and the second expensive finish.\n"
  "PANEL 1 (top right, diagonal): the teen throws the arrow-filled body WEST across the room "
  "toward the archer; it crosses the centre of the hall and blocks the archer's view of him.\n"
  "PANEL 2 (top left): the archer opens his mouth and spits a rope of flat white web from MOUTH to "
  "body — this mouth-to-target line must be fully visible — and the web catches the body and hangs "
  "it one pace east of him, directly in front of his east-facing stance.\n"
  "PANEL 3 (middle right): the archer leans around the east side of the hanging body. The teen is "
  "NOT there. The dropped plain sword still lies untouched on the floor beside the east wall, "
  "proving he moved without it.\n"
  "PANEL 4 (the LEFT-hand panel of the middle row, immediately LEFT of PANEL 3): BOTH FIGURES ARE "
  "IN THIS PANEL. The archer stands at west-of-centre with his back to the reader, facing WEST "
  "away from the camera; the teen stands two paces directly BEHIND him and extends his right "
  "index and middle fingers. A narrow flat lightning beam leaves those fingertips, crosses the "
  "two paces and passes through the archer's RIGHT SHOULDER from back to front, exiting the "
  "front of it and stunning the bow arm. The teen is never alone in this panel and never points "
  "at empty space; the archer is never absent from it.\n"
  "PANEL 5 (the RIGHT-hand panel of the row BELOW that middle row, read after PANEL 4): he closes "
  "the two paces before the archer can turn and plants his RIGHT "
  "palm flat on the sternum; his left arm stays lowered and is not used. Flat lightning begins "
  "converging through his body into that palm.\n"
  "PANEL 6 (dominant panel across the bottom): the point-blank discharge — the archer collapses "
  "into flat charred black-grey remains at west-of-centre, no body detail and no gore. The teen "
  "stands over them with his right palm smoking, shoulders lower than before. " + L_HALL
  + SAY((4, NAR, "upper right", "LIGHTNING BEAM."),
        (6, NAR, "upper right", "SIGH OF THE YELLOW DRAGON."))
  + SFX(2, "SPTCH", "Along the web rope. ")
  + SFX(4, "TZAK", "Where the beam exits the shoulder. ")
  + SFX(6, "ZZZRAAAM", "Through the contact point, cropped by the panel edge. ")
  + "THE BEAM HAS A TARGET AND IT COMES BEFORE THE PALM. The lightning-beam panel must contain "
    "KIDŌMARU — the dark-brown-skinned archer with the black topknot, the spider-marked forehead "
    "protector and SIX ARMS — seen from behind at west-of-centre, with the beam entering the back "
    "of his RIGHT SHOULDER and coming out of the front. The teen is never shown alone pointing "
    "two fingers into empty air. That beam panel must be read BEFORE the panel where the teen's "
    "right palm meets the sternum: it sits higher on the page and further right in its own row, "
    "and the palm-contact panel sits in the row BELOW it. Once the shoulder has been pierced it "
    "STAYS pierced — in the palm-contact panel and in the bottom panel the archer's right "
    "shoulder and bow arm are visibly slack and hanging, never sound and never raised. He is the "
    "last living guard on this page; Sakon, Tayuya and Jirōbō are all dead and none of them "
    "stands, moves or acts anywhere on it. ",
  R("naruto_v4_armor_sword", "env_oto_throne_hall"), "medium"),

 ("p16", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4)
  + ONLY(NAR, PALEONE, SPEC,
         "the four dead Sound guards, present ONLY as unmoving remains that never reset: a "
         "blackened body at west-of-centre, a heap of grey ash beside the eastern pillar, an "
         "arrow-filled body hanging in white web at west-of-centre, and charred remains beneath "
         "it") + GEAR + ARM + ROOM + IMPACT 
  + FOUR + DEATHS +
  "SEVEN panels. The guards are gone; the unmoving fifth person becomes visible again.\n"
  "PANEL 1 (top right): close insert — the teen lifts the plain sash sword from its exact floor "
  "point beside the EAST wall with his right hand and slides it home at his LEFT hip. His left "
  "forearm swells visibly at the armour gap; he flexes those fingers once and they answer "
  "incompletely. No text in this panel.\n"
  "PANEL 2 (wide state panel across the page): the whole hall from the south, everything exactly "
  "where it was left — the blackened body unmoved at west-of-centre; the heap of grey ash beside "
  "the eastern pillar; the arrow-filled body still hanging in white web one pace east of the "
  "charred remains at west-of-centre; the teen standing beside the east wall with the sword now "
  "sheathed; the pale man still on the north dais; the medic still upright at the eastern stair. "
  "The WESTERN pillar is cracked, the EASTERN pillar is intact. Nothing is cleaned up. No text in "
  "this panel.\n"
  "PANEL 3 (middle right): close-up — the pale man finally turns his head toward the eastern "
  "stair.\n"
  "PANEL 4 (middle centre): medium — he rises from the throne, crosses the dais to the east, "
  "descends to the stair and taps the frozen medic's forehead with one finger.\n"
  "PANEL 5 (middle left): the medic topples sideways off the bottom stair onto the floor beside "
  "it; an inset at the corner of the same panel shows his throat close up — chest moving, eyes "
  "open and fixed, no wound of any kind.\n"
  "PANEL 6 (lower right): medium close-up — the teen watches the pale man, not the fallen medic.\n"
  "PANEL 7 (dominant panel across the bottom): the pale man straightens beside the stair far too "
  "slowly and braces his left palm on the dais edge; the empty throne sits well to the west, "
  "untouched. The teen's red six-bladed eye reads the tremor in that hand and the shallow breath. "
  + L_HALL
  + SAY((3, PALEONE, "upper right", "KABUTO."),
        (6, NAR, "upper right", "YOU NEVER NOTICED."),
        (7, NAR, "upper right", "YOU ARE SEVERELY WEAKENED."),
        (7, NAR, "upper left", "YOU NEVER INTENDED TO HELP THEM."))
  + SFX(5, "THUD", "Beside the shoulder where it meets the floor. ")
  + "PANEL 2 IS THE MOST IMPORTANT PANEL ON THIS PAGE AND IT PREVIOUSLY CAME BACK EMPTY. It is "
    "the one panel that carries the whole fight forward, so it must be FULL. Draw all of the "
    "following at once, all clearly visible in the same wide shot of the hall seen from the "
    "south, and do not leave any of them out:\n"
    "  (a) SAKON'S blackened body lying flat and unmoved on the floor at WEST-OF-CENTRE;\n"
    "  (b) TAYUYA'S heap of flat grey ASH on the floor beside the EASTERN pillar;\n"
    "  (c) JIRŌBŌ'S slack body, stuck full of arrow shafts, HANGING off the floor in a white web "
    "sling one pace east of west-of-centre;\n"
    "  (d) KIDŌMARU'S flat charred black-grey remains on the floor beneath that hanging body;\n"
    "  (e) the blond teen in red armour standing beside the EAST wall with his sword now sheathed "
    "at his left hip;\n"
    "  (f) the pale long-haired man STILL SEATED ON THE THRONE on the north dais — the throne is "
    "OCCUPIED in this panel, never empty, because he does not stand up until two panels later;\n"
    "  (g) the grey-haired medic in round glasses still standing frozen upright at the eastern "
    "dais stair.\n"
    "The WESTERN pillar is cracked, the EASTERN pillar is intact, the floor is broken, and nothing "
    "has been cleaned away. An empty hall, an empty throne, a missing body or a missing ash heap "
    "makes this panel fail. ",
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_oto_throne_hall"), "low"),

 # ---- Spread 9: the fight he never wanted ------------------------------------------
 ("p17", dict(scene="action", light="interior", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + ENV.format(i=3)
  + ONLY(NAR, PALEONE,
         "the immobilised grey-haired medic lying still on the floor beside the eastern stair in "
         "the background only") + GEAR + ARM + ROOM + IMPACT + FLAT +
  "SEVEN panels. A conventional duel that is really a search for a breathing lane.\n"
  "PANEL 1 (tall panel down the right edge): the pale man opens his mouth unnaturally wide and a "
  "small snake climbs out of it carrying a long thin straight sword crosswise in its own jaws. He "
  "takes the hilt in his left hand, then settles it into his right. Show the whole grotesque "
  "origin in one shot — do not crop it away.\n"
  "PANEL 2 (top left): medium — the teen stands east of centre with his arms at his sides and does "
  "NOT draw his own sword.\n"
  "PANEL 3 (the RIGHT-HAND panel of the middle row, read before PANELS 4 and 5, which sit to its "
  "LEFT in that order): LONG RANGE — the pale man charges south from the eastern stair at "
  "ordinary human speed across three metres of open floor and swings the long sword diagonally "
  "across the teen's chest; the teen jumps one pace south and the blade misses the armour. The "
  "gap between the two men is wide and clearly readable. No text in this panel.\n"
  "PANEL 4 (the MIDDLE panel of that same row, immediately LEFT of PANEL 3): CLOSE QUARTERS, "
  "inside arm's length — the follow-up horizontal cut at the face; the teen ducks, and the pale "
  "man's left foot immediately kicks at the lowered head. The teen blocks that kick on his RIGHT "
  "forearm only, keeping the bruised left tucked in, and hops south-east.\n"
  "PANEL 5 (middle left): the pale man plants the long sword point-first in the floor beside his "
  "right foot, lets go of the hilt, forms two-handed seals, inhales and emits a gust from his "
  "MOUTH travelling north to south. The sword stays standing in the floor.\n"
  "PANEL 6 (wide band, lower): the teen body-flickers clear to the south-west of the cone and the "
  "gust strikes the SOUTH wall; as it passes, the pale man pulls the long sword back out of the "
  "floor into his right hand. They end three paces apart, the pale man at centre and the teen "
  "south-west of him. Only the dead guards and broken floor lie behind them — no snakes have "
  "appeared from his sleeve yet.\n"
  "PANEL 7 (bottom left): close-up — the teen alone in frame, folding his arms; the LEFT one sits "
  "visibly lower than the right. The pale man is NOT drawn in this panel. " + L_HALL
  + SAY((1, PALEONE, "upper right", "YOU STILL UNDERESTIMATE ME."),
        (2, NAR, "upper right", "IN THAT BODY, KILLING YOU IS NOT A FIGHT."),
        (5, PALEONE, "upper right", "WIND RELEASE: GREAT BREAKTHROUGH."),
        (7, OFF(PALEONE), "upper right", "YOU ARE NOT EVEN TRYING."),
        (7, NAR, "upper left", "THAT TOOK YOU TOO LONG."))
  + SFX(4, "THK", "At the right-forearm block. ")
  + "THE DUEL ESCALATES INWARD AND MUST NOT READ BACKWARDS. The panel showing the pale man's "
    "OPENING LUNGE from three metres of open floor sits to the RIGHT of the panel showing the "
    "close-quarters cut, the ducked head and the \"THK\" forearm block. Reading right to left the "
    "reader gets the long-range charge FIRST and the close-quarters block SECOND; the \"THK\" "
    "panel is never to the right of the lunge panel.\n"
    "PANEL 7 CONTAINS ONLY THE BLOND TEEN — the pale man is not drawn in it at all — and it "
    "carries TWO balloons that must not read as one speaker. \"YOU ARE NOT EVEN TRYING.\" is the "
    "pale man's OFF-PANEL line: give it a short straight spur tail that runs to the nearest panel "
    "border and STOPS there, pointing out of the panel, clear of the teen's face and body. It is "
    "never tail-less and never aimed at the teen. \"THAT TOOK YOU TOO LONG.\" is the teen's line "
    "and carries an ordinary tail reaching his mouth. Both balloons must have a visible tail. ",
  R("naruto_v4_armor_sword", "orochimaru", "env_oto_throne_hall"), "low"),

 ("p18", dict(scene="action", light="interior", cast="two", mood="violent", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ENV.format(i=4) + ONLY(NAR, PALEONE) + GEAR + ARM + EMS + ROOM + IMPACT + FLAT +
  "SEVEN panels. The poison, with its preparation and its contact both visible.\n"
  "PANEL 1 (top right, diagonal): the pale man moves the long sword into his LEFT hand, "
  "body-flickers to one pace directly behind the teen at south-west of centre and thrusts his "
  "empty right forearm forward; several snakes pour out of the MOUTH OF HIS RIGHT SLEEVE across "
  "that one-pace gap toward the teen's back.\n"
  "PANEL 2 (top left): the teen turns clockwise and his red six-bladed eye meets the snakes. Flat "
  "opaque BLACK flame with hard white outlines ignites directly on them before any of them "
  "reaches him; nothing leaves his hands or mouth.\n"
  "PANEL 3 (middle right): through the burning obstruction — the burnt snakes have fallen between "
  "the two men and hide everything below their shoulders. The pale man plants the long sword "
  "point-first beside his left foot, lets go, cups his now-empty LEFT hand beside his own mouth, "
  "compresses a breath and leans forward. The teen has finished turning and faces him at one "
  "pace. No text in this panel.\n"
  "PANEL 4 (middle left): he exhales a dense flat PURPLE aerosol from his MOUTH; it crosses the "
  "one-pace gap above the burning snakes as a hard-edged cone and reaches the teen's face before "
  "his weight can shift.\n"
  "PANEL 5 (dominant panel, lower right and running most of the width): contact — the leading "
  "purple edge enters the teen's open nostrils and mouth on his first involuntary breath, drawn "
  "as flat opaque purple shapes against his face. He is already pushing off to jump south-west. "
  "Do NOT draw a mask, a held breath, an immunity aura or a collapse.\n"
  "PANEL 6 (lower centre): he lands in a crouch further south-west with one hand at his mouth; the "
  "pale man pulls the long sword out of the floor into his right hand and holds his exhale point. "
  "They are three paces apart.\n"
  "PANEL 7 (bottom left): close-up — the pale man's grin, the first fully confident expression he "
  "has shown on any page. " + L_HALL
  + SAY((1, PALEONE, "upper right", "MANY HIDDEN SNAKES."),
        (2, NAR, "upper right", "AMATERASU."),
        (6, NAR, "upper right", "POISON?"),
        (7, PALEONE, "upper right", "MADE AFTER OUR LAST MEETING."),
        (7, PALEONE, "upper left", "THIS ONE HAS NO ANTIDOTE—EXCEPT ME."))
  + SFX(4, "HSSSS", "Inside the aerosol cone. ")
  + "THE POISON COMES OUT OF HIS MOUTH AND OUT OF NOTHING ELSE. In the panel where the purple "
    "aerosol is emitted, and in the contact panel that follows it, the pale man's MOUTH IS OPEN "
    "and his cupped LEFT HAND is raised beside that open mouth. The flat opaque purple cone "
    "BEGINS AT HIS LIPS and widens away from his face. NOTHING purple leaves either of his hands: "
    "his right arm is not outstretched toward the teen, no stream, mist or spray issues from any "
    "palm or fingertip, and his mouth is never closed while the poison is in the air.\n"
    "The balloon \"POISON?\" belongs to the BLOND TEEN, who crouches at the FAR LEFT of his "
    "panel. Draw a LONG tail that travels all the way across the panel to HIS mouth at "
    "panel-left, passing clear of the pale man. The tail must never end on the pale man's head, "
    "face or body at panel-right, and never stop short at whichever figure is nearer the "
    "balloon. ",
  R("naruto_v4_armor_sword", "orochimaru", "mangekyo_design", "env_oto_throne_hall"), "medium"),

 # ---- Spread 10: the body is the objective -----------------------------------------
 ("p19", dict(scene="action", light="interior", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + WSNAKE.format(i=3)
  + MANGEKYO_EYE.format(i=4) + ENV.format(i=5)
  + ONLY(NAR, PALEONE) + GEAR + ARM + EMS + ROOM + IMPACT + FLAT +
  "SEVEN panels. The real objective is revealed and the trigger begins.\n"
  "PANEL 1 (top right): medium close-up — the teen rises. There is no visible effect from the "
  "poison at all; the low left forearm is still his only visible injury.\n"
  "PANEL 2 (top left): close-up — the pale man LOWERS the long sword instead of raising it, arms "
  "loose.\n"
  "PANEL 3 (middle band, full width): the teen flashes three paces north-east, punches him in the "
  "face with the right fist, catches an ankle, rotates and throws him NORTH across the room into "
  "the wall below the dais. The pale man gives no counter at all; the long sword leaves his hand "
  "and lands at the north-WEST edge of the dais. Flat impact shapes, no injury detail.\n"
  "PANEL 4 (middle right): the dust clears — the human body splits open and an enormous "
  "CHALK-WHITE snake body, built out of hundreds of smaller white snakes, rises from the debris at "
  "north-centre with a pale human-like face at the front of its head, turned SOUTH toward the "
  "teen.\n"
  "PANEL 5 (middle left): the white form opens that mouth and lunges six paces SOUTH; the teen is "
  "moving north to continue his attack and is squarely in the line.\n"
  "PANEL 6 (thin trigger strip across the page): two eyes at the instant of contact — the teen's "
  "active red six-bladed eye at the right, the white form's wide open eye at the left. No hand "
  "seal, no mouth emission, no projectile of any kind.\n"
  "PANEL 7 (band across the bottom): the panel BORDER ITSELF liquefies from stone-grey into "
  "black-and-red. Inside it the physical state is unchanged: the teen still stands at "
  "centre-north, the white form still lunges from north-centre, and NEITHER has swallowed or "
  "entered the other. No text in this panel. " + L_HALL
  + SAY((1, NAR, "upper right", "YOU ARE CONFIDENT IN A POISON YOU HAVE NOT SEEN WORK."),
        (2, PALEONE, "upper right", "I ONLY NEED YOU CLOSE."))
  + SFX(3, "KRA-KOOM", "At the wall below the dais, cropped by the panel edge. "),
  R("naruto_v4_armor_sword", "orochimaru", "giant_snake", "mangekyo_design",
    "env_oto_throne_hall"), "medium"),

 ("p20", dict(scene="emotional_closeup", light="white_void", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + WSNAKE.format(i=3)
  + ONLY(NAR, PALEONE) + GEAR + ARM + FLAT +
  "SIX panels. EVERY IMAGE ON THIS PAGE IS A PERCEPTION, NOT PHYSICAL REALITY. Every panel border "
  "is drawn in black and red instead of plain black, and there is no stone floor, no dais, no "
  "pillar and no throne room anywhere on this page.\n"
  "PANEL 1 (near-splash: one very large panel filling the upper two thirds of the page, with the "
  "remaining panels stacked small below it): the enormous chalk-white snake mouth appears to close "
  "around the blond teen, the white coils filling the frame. The floor of the world is absent — "
  "flat black and red behind everything. The upper right of this panel stays clear for the "
  "perception card.\n"
  "PANEL 2 (small, upper right of the lower band): the teen stands calmly on nothing inside an "
  "endless black-and-red plane; the white coils ring him at a distance.\n"
  "PANEL 3 (small, upper left of the lower band): the coils fill the whole background as though "
  "they own every horizon; the teen is small at the lower right, not struggling.\n"
  "PANEL 4 (the RIGHT-HAND panel of the next row down — PANEL 5 is its only neighbour and sits "
  "directly to its LEFT): medium — the teen looks up and along the coils rather than at the face, "
  "hands at his sides. Both of his balloons sit inside THIS panel.\n"
  "PANEL 5 (the LEFT-HAND panel of that same row, immediately LEFT of PANEL 4, read after it): "
  "the pale snake-face leans in close from the left, huge against the teen at the right edge.\n"
  "PANEL 6 (dominant bottom panel): false-victory close-up — the pale snake-face smiles, and the "
  "teen is reflected small and upright in its pupil. " + L_VOID
  + CAP(1, "upper right", "WHAT OROCHIMARU PERCEIVES")
  + SAY((2, PMOUTH, "upper right", "THIS IS MY WORLD."),
        (2, PMOUTH, "upper left", "YOU CANNOT ESCAPE ME."),
        (3, NARP, "upper right", "SO THIS WAS THE FIGHT."),
        (4, NARP, "upper right", "THE GUARDS BOUGHT YOUR ATTENTION."),
        (4, NARP, "upper left", "THE POISON BOUGHT YOUR OPENING."),
        (5, PFACE, "upper right", "AND FREED KURAMA BOUGHT ME YOUR BODY."),
        (6, PFACE, "upper right", "YOU ARE MINE, NARUTO-KUN."))
  + "THE LIST MUST BE SPOKEN BEFORE THE LINE THAT CONTINUES IT. The panel carrying \"THE GUARDS "
    "BOUGHT YOUR ATTENTION.\" and \"THE POISON BOUGHT YOUR OPENING.\" sits to the RIGHT of the "
    "panel carrying \"AND FREED KURAMA BOUGHT ME YOUR BODY.\", so that reading right to left "
    "delivers the teen's two lines first and the snake-face's answer second. The line beginning "
    "with the word AND completes a list that has not been spoken yet if it is read first, so its "
    "panel is NEVER to the right of, and never level with and rightward of, the teen's panel. "
    "Within the teen's own panel, \"THE GUARDS BOUGHT YOUR ATTENTION.\" sits further RIGHT than "
    "\"THE POISON BOUGHT YOUR OPENING.\" ",
  R("naruto_v4_armor_sword", "orochimaru", "giant_snake"), "medium"),

 # ---- Spread 11: before my eyes ----------------------------------------------------
 ("p21", dict(scene="emotional_closeup", light="white_void", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ORO.format(i=2) + WSNAKE.format(i=3)
  + MANGEKYO_EYE.format(i=4) + ENV.format(i=5)
  + ONLY(NAR, PALEONE,
         "the immobilised grey-haired medic lying still on the floor beside the eastern stair, "
         "visible only in the last two panels") + GEAR + ARM + EMS + ROOM + FLAT +
  "SEVEN panels. THE CHAPTER'S KEY PAGE: a perceived world is taken away and the unchanged "
  "physical room is underneath it. PANELS 1 TO 4 keep the black-and-red borders and the empty "
  "black-and-red void of the previous page; PANELS 5 TO 7 return to plain black borders and the "
  "fully drawn stone hall.\n"
  "PANEL 1 (top right): close-up inside the perceived world — the teen finally raises his eye-line "
  "to the perceived snake's eyes.\n"
  "PANEL 2 (top left): the perceived white coils STOP tightening; the pale snake-face pulls back "
  "slightly.\n"
  "PANEL 3 (middle right): tight close-up on the teen's active red six-bladed eye inside the "
  "perceived world, nothing else in frame.\n"
  "PANEL 4 (middle left): the same eye larger, and inside its reflection sits the image the pale "
  "man WANTED — a completed transfer, drawn flat and small like a printed picture, not a scene.\n"
  "PANEL 5 (dominant panel, lower right and running most of the page width): the black-and-red "
  "world breaks like sheet glass into hard angular shards, and through the gaps the OBJECTIVE "
  "physical hall is visible exactly as page 19 left it — the teen standing at centre-north, the "
  "white form stalled mid-lunge from north-centre with its mouth still open but NOT around him. "
  "No body has been transferred and nobody has moved.\n"
  "PANEL 6 (lower centre): fully back in the stone hall — the white form recoils NORTH; the teen "
  "stands three paces south of its head. The medic lies breathing on the floor beside the eastern "
  "stair and the long thin sword still lies at the north-west edge of the dais.\n"
  "PANEL 7 (bottom left): medium close-up — the teen draws the plain sash sword from his LEFT hip "
  "with his right hand and runs flat wind wedges from palm through hilt to edge. " + L_HALL
  + SAY((1, NARP, "upper right", "WHO SAID THIS WORLD WAS YOURS?"),
        (2, PMOUTH, "upper right", "WHAT ARE YOU SAYING?"),
        (3, NARP, "upper right", "WHEN YOU SHOWED ME YOUR TRUE FORM, I SAW THE OBJECTIVE."),
        (4, NARP, "upper right", "I GAVE YOU WHAT YOU WANTED TO SEE."),
        (4, NARP, "upper left", "GENJUTSU."),
        (6, NAR, "upper right", "ITACHI WARNED YOU ONCE."),
        (7, NAR, "upper right", "OROCHIMARU—BEFORE MY EYES, YOUR NINJUTSU IS USELESS."))
  + SFX(5, "KRRSH", "Across the breaking perception, crossing the gutter. "),
  R("naruto_v4_armor_sword", "orochimaru", "giant_snake", "mangekyo_design",
    "env_oto_throne_hall"), "high"),

 ("p22", dict(scene="action", light="interior", cast="two", mood="violent", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + WSNAKE.format(i=2) + MANGEKYO_EYE.format(i=3)
  + ENV.format(i=4) + ONLY(NAR, PALEONE) + GEAR + ARM + EMS + ROOM + IMPACT + FLAT +
  "SEVEN panels. The last physical reversal, then the body is fixed in place.\n"
  "PANEL 1 (top right): the white form lunges SOUTH on an extended neck; the teen jumps one pace "
  "south and the jaws miss his face. The plain sword stays in his right hand; the left arm stays "
  "low.\n"
  "PANEL 2 (top left): he crouches under the travelling neck and swings the wind-sharpened blade "
  "horizontally from EAST to WEST; the edge cuts only the forward cluster of the small white "
  "snakes that make up the body. Cut shapes are flat and clean — no injury detail, no blood.\n"
  "PANEL 3 (the RIGHT-HAND panel of the middle row — PANEL 4 is its only neighbour and sits "
  "directly to its LEFT): the severed white snakes release a flat pale gas from their cut ends; "
  "the teen sees it and pushes off SOUTH before breathing any of it. The gas does not touch him "
  "and does not remove the purple poison already inside him.\n"
  "PANEL 4 (the LEFT-HAND panel of that same row, immediately LEFT of PANEL 3 and read after it): "
  "the white form's tail sweeps west to east UNDER the gas and catches his "
  "left side, because the bruised left forearm cannot set a full guard. He is thrown five paces "
  "EAST; the sword stays in his right hand. Flat impact shapes only.\n"
  "PANEL 5 (lower right): he twists once and lands on both feet at east-of-centre, sliding. The "
  "left forearm hangs lower still; his breathing is controlled. The white form coils at "
  "north-centre facing south.\n"
  "PANEL 6 (lower centre): close-up — he raises his active red six-bladed eye-line to the pale "
  "face and the visual focus fixes exactly between its eyes. No hand seal.\n"
  "PANEL 7 (dominant panel across the bottom): flat opaque BLACK flame with hard white outlines "
  "ignites directly across that face; the charge stops and the whole white body coils in on "
  "itself. The skin around the teen's own eye tightens, but the eye stays open. No injury detail, "
  "no blood, no gore. " + L_HALL
  + SAY((6, NAR, "upper right", "YOU SURPRISED ME ONCE."),
        (7, NAR, "upper right", "YOU WILL NOT DO IT TWICE."))
  + SFX(2, "SHRAK", "Along the sword edge. ")
  + SFX(4, "THOOM", "At the rib-and-armour contact. ")
  + SFX(7, "FSSSH", "Inside the black flame shapes. ")
  + "THE GAS IS RELEASED BEFORE THE TAIL LANDS. The panel showing the severed white snakes venting "
    "pale gas — with the teen still unhurt and pushing off south, dodging — sits to the RIGHT of "
    "the panel showing the tail sweep, the \"THOOM\" impact and the teen thrown east. The impact "
    "panel is NEVER to the right of the gas panel: he must be seen dodging the gas before the "
    "tail catches him, or the whole beat reads backwards. ",
  R("naruto_v4_armor_sword", "giant_snake", "mangekyo_design", "env_oto_throne_hall"), "low"),

 # ---- Spread 12: nothing left to shed ----------------------------------------------
 ("p23", dict(scene="action", light="interior", cast="two", mood="violent", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + WSNAKE.format(i=2) + KAB.format(i=3)
  + MANGEKYO_EYE.format(i=4) + ENV.format(i=5)
  + ONLY(NAR, PALEONE,
         "the immobilised grey-haired medic lying still and breathing on the floor beside the "
         "eastern stair in the background") + GEAR + ARM + EMS + ROOM + IMPACT + FLAT +
  "SEVEN panels. A methodical execution in a readable order.\n"
  "PANEL 1 (top right): close-up — the teen sheathes the plain sword at his LEFT hip to free both "
  "hands for seals; behind him the white form claws at the flat black flame across its face.\n"
  "PANEL 2 (wide diagonal band): he forms two hand seals, flat lightning gathers along both "
  "forearms, and a lightning dragon leaves the space between his joined palms travelling six paces "
  "north-west from east-of-centre into the coiled white torso at north-centre. The floor, dais and "
  "pillars stay fully drawn through it.\n"
  "PANEL 3 (middle right): the many-snake body convulses but still moves; the teen resets exactly "
  "the same two seals, and the repeated preparation is clearly the same pair of hands doing the "
  "same thing again.\n"
  "PANEL 4 (dominant panel, middle left and running most of the width): a SECOND lightning dragon "
  "leaves the joined palms and strikes the full length of the body. All movement and all hissing "
  "stop here. Flat lightning shapes, no injury detail.\n"
  "PANEL 5 (the RIGHT-HAND panel of a row of EXACTLY TWO panels — PANEL 6 is its only neighbour "
  "and sits directly to its LEFT): he forms fire seals, inhales and emits a great fireball from "
  "his MOUTH, travelling north-west into the electrically locked remains at north-centre. The "
  "white body is still WHOLE and coiled in this panel. The fireball is a flat opaque shape with a "
  "hard outline and does not wash out the hall.\n"
  "PANEL 6 (the LEFT-HAND panel of that same two-panel row, immediately LEFT of PANEL 5 and read "
  "after it): after the ordinary fire passes he redraws the plain sword, runs flat "
  "wind wedges from palm through hilt to edge, and cuts the cooked white mass into separated "
  "sections in ONE continuous motion sequence with ghosted phases — never duplicate figures, never "
  "any injury detail.\n"
  "PANEL 7 (band across the bottom, SILENT): a fresh sustained sweep of flat black flame moves "
  "across the separated sections until each one is burnt black. There is no intact host, no head "
  "and no escaping snake anywhere. The teen stands at east-of-centre; the medic still breathes on "
  "the floor beside the eastern stair; the long thin sword still lies at the north-west edge of "
  "the dais. The skin around his active eye is tight with strain but the eye stays open. No text "
  "in this panel. " + L_HALL
  + SAY((1, NAR, "upper right", "YOU FORCED A FIGHT I DID NOT WANT."),
        (1, NAR, "upper left", "NOW THERE WILL BE NOTHING LEFT TO SHED."),
        (2, NAR, "upper right", "LIGHTNING RELEASE: LIGHTNING DRAGON."),
        (4, NAR, "upper right", "AGAIN."),
        (5, NAR, "upper right", "FIRE RELEASE: GREAT FIREBALL."))
  + SFX(2, "KRA-KOOOM", "At the torso contact point. ")
  + SFX(4, "KRA-KOOOM", "Running down the length of the body. ")
  + SFX(5, "WHOOF", "Inside the fireball. ")
  + "THE BODY IS BURNED WHOLE, THEN CUT, AND IT NEVER REASSEMBLES. The panel containing the great "
    "fireball — where the white mass is still WHOLE and coiled — sits to the RIGHT of the panel "
    "containing the sword cutting it into separated sections. Reading right to left the reader "
    "gets: whole body burned, then body cut apart, then the bottom band of separated sections "
    "burning black. The cutting panel is NEVER to the right of the fireball panel, and the white "
    "body must NEVER appear whole or coiled again in any panel that is read after it has been "
    "cut. This page has EXACTLY SEVEN panels; do not add an eighth. ",
  R("naruto_v4_armor_sword", "giant_snake", "kabuto", "mangekyo_design",
    "env_oto_throne_hall"), "medium"),

 ("p24", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=8),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + KAB.format(i=3) + ENV.format(i=4)
  + ENV.format(i=5) + ZOR
  + ONLY(NAR, ZETSU,
         "the grey-haired medic in round glasses, lying immobilised and breathing on the floor "
         "beside the eastern stair") + GEAR + ARM +
  "EIGHT panels. LAST PAGE OF THE CHAPTER — four separate facts have to survive it: the snake is "
  "dead, the medic is alive, the mask is recovered, and the hideout is left standing.\n"
  "PANEL 1 (top right): the plant creature's head emerges UPSIDE DOWN from the stone ceiling above "
  "the dais; the teen looks up from the burnt remains.\n"
  "PANEL 2 (top left): the creature drops onto the dais and folds back enough cloth from a wrapped "
  "bundle to show a pale horned demon mask, intact and undamaged.\n"
  "PANEL 3 (middle right): the teen kneels once beside the medic on the floor beside the eastern "
  "stair and places two right fingers at his neck; the medic's eyes stay open and fixed and his "
  "chest moves. The teen does not strike him. The plant creature is NOT drawn in this panel.\n"
  "PANEL 4 (middle centre): medium — the teen stands and lifts the long thin sword by its hilt "
  "from the north-west edge of the dais. He keeps his own plain sash sword sheathed at his left "
  "hip; the two weapons are clearly different objects.\n"
  "PANEL 5 (the LEFT-HAND panel of the middle row, at the end of the row that begins with PANELS "
  "3 and 4 — nothing on this page sits to its RIGHT except those two panels of its own row): he "
  "throws the long thin sword hilt-first to the creature, which catches it in one hand while the "
  "other keeps the wrapped mask against its shoulder.\n"
  "PANEL 6 (a narrow strip running the FULL WIDTH of the page, BELOW the whole middle row — "
  "nothing sits to its left or to its right): rear two-shot — the two of them walk SOUTH away "
  "from the reader down the entrance corridor. The dark purple GUNBAI is strapped flat across the "
  "blond teen's back and fills most of it; his back is never bare. The creature already carries "
  "the wrapped mask and the long thin sword it was given in PANEL 5. Behind them the hall is "
  "structurally whole: the bodies, the ash, the cracked western pillar, the fallen medic and the "
  "shelves of valuables are all still there. No text in this panel.\n"
  "PANEL 7 (a panel BELOW the full-width strip of PANEL 6, at the right of its own row): outside "
  "now — the creature turns its head back toward the intact sealed cliff entrance, which has not "
  "collapsed.\n"
  "PANEL 8 (dominant panel across the bottom): wide exterior — the teen walks LEFT TO RIGHT into "
  "flat Earth Country daylight with the gunbai on his back and the plain sword at his hip, his "
  "left forearm held close and the skin around his active eye tight; the creature follows with the "
  "wrapped mask and the long thin sword. The sealed entrance stands undamaged behind them. "
  + L_EXIT
  + SAY((1, ZETSU, "upper right", "DID I MISS ANYTHING?"),
        (2, ZWHITE, "upper right", "I FOUND IT."),
        (2, NAR, "upper left", "GOOD."),
        (3, OFF(ZBLACK), "upper right", "THE MEDIC?"),
        (3, NAR, "upper left", "ALIVE."),
        (4, NAR, "upper right", "LEAVE HIM."),
        (5, NAR, "upper right", "KEEP THIS SAFE WITH THE MASK."),
        (7, ZWHITE, "upper right", "YOU ARE LEAVING THE HIDEOUT?"),
        (8, NAR, "upper right", "IT STILL HAS VALUE."))
  + "THE PANEL 1 BALLOON READS EXACTLY \"DID I MISS ANYTHING?\" — MISS is spelled M-I-S-S, with "
    "EXACTLY TWO letter S at the end of the word, never three and never MISSS. Letter every "
    "balloon on this page once, spelled in full, with no doubled, ghosted or overprinted text and "
    "no repeated letters inside a word.\n"
    "THE SWORD IS HANDED OVER BEFORE THE DEPARTURE PANELS. The panel where the blond teen throws "
    "the long thin sword to the plant creature is read BEFORE the corridor strip and before the "
    "cliff-door panel: it sits in the MIDDLE row, and both the corridor strip and the cliff-door "
    "panel sit in rows BELOW it. The creature is therefore already carrying that sword the first "
    "time it is seen with one, and \"YOU ARE LEAVING THE HIDEOUT?\" is never read before the "
    "handoff.\n"
    "THE GUNBAI NEVER LEAVES HIS BACK. In EVERY panel of this page where the blond teen's back is "
    "visible — the corridor rear two-shot above all, and the wide exterior at the bottom — the "
    "large dark purple GUNBAI with its chain is strapped flat across that back and clearly drawn. "
    "His back is never bare, and the gunbai is never absent, never dropped, never carried by the "
    "creature and never replaced by the sword. ",
  R("naruto_v4_armor_sword", "zetsu", "kabuto", "env_oto_throne_hall",
    "env_oto_hidden_base"), "low"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch07" / "raw", HERE / "v5ch07" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
