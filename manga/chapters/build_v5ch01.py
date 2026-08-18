"""Volume 5, Chapter 1 — "After the Blue". 16 pages.

Source: fic ch12:7-125, with a two-page silent-capable continuity bridge from the exact
ch11:577-581 handoff. Translated 1:1 from story/volume_05/drafts/ch01_after_the_blue.md —
72 balloons, one time card, one chapter marker. Reading order is RIGHT TO LEFT per the
approved `name`; every page states it.

Owner authorized production start ("go"). Pre-generation gates 1-8 were completed in
preproduction (see story/volume_05/REVIEW_STATUS.md); this builder must match the `name`,
not improve on it.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, DAN, ENV, FILL, KAK, OFF, ONLY, R, SAS, SAY, ZET, HAWK, UCH  # noqa: E402
from prompts_v4 import (KURAMA_FULL, MEI_V4, N16_ARMOR, YAGURA_HUMAN, YUGAO_V4,      # noqa: E402
                        KIRI_REBELS, MEI_V4_SPEAKER, N16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
YUG = YUGAO_V4_SPEAKER
MEI = MEI_V4_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")
ROOT = ("three kneeling Root agents in plain featureless white oval masks with narrow eye and "
        "mouth slits, hooded grey cloaks, none of them ever unmasked")
ROOT1 = "the rightmost kneeling white-masked Root agent"
ROOTC = "the centre kneeling white-masked Root agent"
DAMAGE = ("His red plate armour is BATTLE-DAMAGED on this page: cracked lacquer, a split shoulder "
          "plate, dust and scorch marks — but no wounds and no blood. ")
REPAIRED = "His red plate armour is clean and fully repaired on this page. "
L_CRATER = ("Lighting: cold blue-grey morning over a devastated battlefield, dust hanging, the "
            "light flat and drained. ")
L_CHAMBER = "Lighting: one hard shaft from above into a windowless dark council chamber; everything else black. "
L_KIRI = "Lighting: clean pale mist-filtered daylight, the fog finally lifting off a rebuilding village. "
L_RIDGE = "Lighting: silver-grey overcast on a bare coastal ridge, wind-driven mist, hard horizon. "
L_DUSKR = "Lighting: low amber sunset raking across the ridge, long shadows, the village lights kindling below. "

PAGES = [
 # ---- Spread 1: somebody else finishes the war -------------------------------------
 ("p01", dict(scene="aftermath", light="day", cast="small_group", mood="somber", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + MEI_V4.format(i=3)
  + YAGURA_HUMAN.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, YUG, MEI, "the short Fourth Mizukage lying motionless and distant",
         "surviving Kiri rebels far away on the crater rim") + DAMAGE +
  "FIVE panels. This page continues the final image of the previous volume exactly: the fight is "
  "over, nobody celebrates.\n"
  "PANEL 1 (tall right strip, full page height): extreme-wide high angle — the blond teen small "
  "on both knees at the centre of a vast crater, back three-quarters to the reader, facing left "
  "toward the tiny distant fallen Mizukage at upper left. The upper right quarter of this panel is "
  "EMPTY BLUE-GREY SKY — no figure, cloud, effect or balloon may enter it — and carries only the "
  "chapter marker.\n"
  "PANEL 2 (top centre): long shot, downward motion — the purple-haired kunoichi drops from upper "
  "right toward the kneeling teen at lower left, eyes fixed on him; the auburn-haired leader "
  "descends behind her at the panel's far right edge.\n"
  "PANEL 3 (top left): medium over the kunoichi's shoulder — the teen still kneels, body facing "
  "the fallen Mizukage, only his head turned right to meet her eyes.\n"
  "PANEL 4 (bottom centre): tight ground-level two-shot — the kunoichi kneels at his right, two "
  "fingers hovering at the side of his neck; he stays upright and still; the auburn-haired leader "
  "crosses the blurred background toward the fallen Mizukage.\n"
  "PANEL 5 (bottom left): medium-long profile — the auburn-haired leader stands centred facing "
  "right toward the two of them, the fallen Mizukage behind her at lower left, rebels holding on "
  "the rim far behind. " + L_CRATER +
  'LETTERING: in the protected sky area of PANEL 1, write the chapter marker in bold upright '
  'English capitals on one line: "CHAPTER 1 — AFTER THE BLUE". It is a tail-less title, not a '
  'balloon. '
  + SAY((2, YUG, "upper right", "NARUTO."),
        (3, BOY16, "upper left", "YOU TOOK YOUR TIME."),
        (4, YUG, "upper centre", "HIS CHAKRA IS ALMOST GONE."),
        (5, MEI, "upper left", "THEN DON'T MOVE.")),
  R("naruto_v4_armor", "yugao_v4", "mei_v4", "yagura_human", "env_kiri_battlefield_crater"),
  "high"),

 ("p02", dict(scene="aftermath", light="day", cast="crowd", mood="somber", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + MEI_V4.format(i=3)
  + KIRI_REBELS.format(i=4) + ENV.format(i=5)
  + ONLY(BOY16, YUG, MEI, "surviving Kiri rebels on both sides of the crater") + DAMAGE +
  "FIVE panels. Agency transfers from the boy to Kiri.\n"
  "PANEL 1 (top right): medium low angle — the blond teen plants his right boot and starts to "
  "rise toward frame left, looking up-left; the purple-haired kunoichi at frame right turns her "
  "torso toward him and reaches across his movement.\n"
  "PANEL 2 (top left): tight diagonal two-shot — her left palm presses his near shoulder down; "
  "she faces left into his profile; he looks up at her and does not resist further.\n"
  "PANEL 3 (wide middle band, the focal panel): extreme-wide eye-level tableau — the "
  "auburn-haired leader stands centred between the downed loyalists on the left and the rebels on "
  "the right, facing the gap between the two groups, feet planted, arms lowered. The teen and the "
  "kunoichi are small in the lower-right background.\n"
  "PANEL 4 (bottom right): medium reaction — three rebels face left toward the leader, shoulders "
  "loosening in a right-to-left ripple; none celebrates yet.\n"
  "PANEL 5 (bottom left): extreme close-up — the teen's face at right facing left, his eye-line "
  "passing the kunoichi toward an empty patch of sky. " + L_CRATER
  + SAY((1, BOY16, "upper right", "THAT ORDER ARRIVES LATE."),
        (2, YUG, "upper left", "FOR ONCE, LET SOMEONE ELSE FINISH THE WORK."),
        (3, MEI, "top centre", "THE WAR IS OVER."),
        (4, "the front rebel", "upper right", "OVER...?"),
        (5, BOY16, "upper left", "THERE IS NOTHING LEFT TO FINISH.")),
  R("naruto_v4_armor", "yugao_v4", "mei_v4", "kiri_rebel_mob", "env_kiri_battlefield_crater"),
  "medium"),

 # ---- Spread 2: Danzō receives a different Naruto ----------------------------------
 ("p03", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + RTL + DAN.format(i=1) + ONLY(HAWK, ROOT) +
  "SIX panels. A strategic interrogation in a windowless chamber.\n"
  "PANEL 1 (top band, full width): extreme-wide symmetrical shot — the bandaged old man sits "
  "elevated at centre back facing forward; three white-masked Root agents kneel in a shallow "
  "triangle below him, eye-lines lowered, nobody moving.\n"
  "PANEL 2 (middle right): tight close-up — the old man's visible eye and mouth fill the panel, "
  "angled down-left toward the agents; he does not move.\n"
  "PANEL 3 (middle centre): tight frontal close-up — the speaking masked agent faces forward, "
  "eyes lowered.\n"
  "PANEL 4 (middle left): insert close-up — the old man's right fingers stopped midway across the "
  "chair arm. Hand and chair arm only, no face.\n"
  "PANEL 5 (bottom right): medium close-up from the old man's viewpoint — the centre agent bows "
  "lower, facing upper left toward him.\n"
  "PANEL 6 (bottom left): tight frontal close-up — the old man centred and motionless, his "
  "visible eye looking straight down at the agents. " + L_CHAMBER
  + SAY((1, ROOT1, "upper right", "THE FOURTH MIZUKAGE IS DEAD."),
        (2, HAWK, "upper right", "BY THE REBELS?"),
        (3, ROOTC, "upper centre", "BY ONE LEAF SHINOBI."),
        (4, OFF(HAWK), "upper left", "NAME HIM."),
        (5, ROOTC, "upper right", "UCHIHA NARUTO."),
        (6, HAWK, "upper left", "CONTINUE.")),
  R("danzo"), "medium"),

 ("p04", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=5),
  FILL + RTL + DAN.format(i=1) + N16_ARMOR.format(i=2) + KURAMA_FULL.format(i=3)
  + ONLY(HAWK, ROOT,
         "the blond older teen and the nine-tailed fox appearing ONLY inside hard-edged recalled "
         "memory images, never in the chamber") +
  "FIVE panels. The old man's model of the boy changes from asset to threat. Recalled images are "
  "drawn as hard-edged inset memories with slightly desaturated colour.\n"
  "PANEL 1 (top right): canted memory montage — the reporting agent stays as a black shoulder "
  "silhouette at lower right facing left; beyond him a recalled image shows the blond teen in red "
  "armour advancing left through a broken forest with BLACK FIRE trailing behind him, drawn as "
  "flat opaque black flame shapes with white outlines.\n"
  "PANEL 2 (top left): extreme-wide recalled image — the nine-tailed fox's silhouette towers at "
  "right facing left over a destroyed tower; the teen is tiny at lower right looking the same "
  "direction.\n"
  "PANEL 3 (middle right): tight three-quarter close-up — the old man leans right, visible eye "
  "fixed down on the agent.\n"
  "PANEL 4 (middle left): close-up — the speaking masked agent faces upper right toward him, "
  "perfectly still.\n"
  "PANEL 5 (dominant bottom, full width): wide low angle — the old man centred deep in frame "
  "facing forward, the chair's shadow climbing around him, the three agents small black shapes "
  "along the bottom edge looking up. " + L_CHAMBER
  + SAY((1, ROOT1, "upper right", "HE BROKE YAGURA'S ARMY ALONE."),
        (2, OFF(ROOT1), "upper left", "WOOD RELEASE. BLACK FIRE. AN ORANGE WARRIOR—AND THE NINE-TAILS ANSWERING HIS CALL."),
        (3, HAWK, "upper right", "YOU SAW THE FOX?"),
        (4, ROOTC, "upper left", "KIRI DID."),
        (5, HAWK, "upper centre", "BRING ME KOHARU AND HOMURA.")),
  R("danzo", "naruto_v4_armor", "kurama_full"), "high"),

 # ---- Spread 3: a hero who rejects the name ----------------------------------------
 ("p05", dict(scene="establishing", light="day", cast="crowd", mood="calm", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV.format(i=4)
  + ONLY(BOY16, YUG, "Kiri workers, shinobi, civilians and children rebuilding the street, none "
         "of them named or recurring — the civilians and workers wear NO forehead protectors, NO "
         "headband plates and NO village symbols of any kind") + REPAIRED +
  "SIX panels. Rebuilding shown through labour and crowd behaviour.\n"
  "PANEL 1 (top band, full width): extreme-wide street shot — the blond teen walks right-to-left "
  "along the centre lane in clean repaired red armour; workers on both sides face inward; shinobi "
  "lift beams with earth and water techniques drawn as flat opaque shapes. The purple-haired "
  "kunoichi follows one pace behind at his right, watching the crowd.\n"
  "PANEL 2 (middle right): medium reaction — a civilian at left turns sharply toward the teen "
  "crossing the background, pointing arm carrying the eye-line left.\n"
  "PANEL 3 (middle centre): low medium shot — two children run right-to-left beside the teen, "
  "looking up at him; he continues without turning.\n"
  "PANEL 4 (middle left): medium profile — an older worker bows from the left toward the teen at "
  "right; his stride carries him past the bow, eyes forward.\n"
  "PANEL 5 (bottom right): tracking medium two-shot — the teen in right foreground moving left; "
  "the kunoichi behind at far right watching his profile. THE BALLOON IN THIS PANEL IS SPOKEN BY "
  "THE BLOND TEEN — its tail must touch HIS mouth and must not approach the kunoichi. She is "
  "silent in this panel, mouth closed.\n"
  "PANEL 6 (bottom left): reverse tracking two-shot — the kunoichi now holds the right half, "
  "still moving left; the teen exits at the left edge; the crowd behind her watches them go. "
  + L_KIRI
  + CAP(1, "upper right", "TWO WEEKS LATER.")
  + SAY((2, "the pointing civilian", "upper right", "THERE HE IS!"),
        (3, "the lead child", "upper centre", "THE HERO OF KIRI!"),
        (4, "the bowing older worker", "upper left", "YOU GAVE US OUR HOME BACK."),
        (5, BOY16, "upper right", "I REMOVED YAGURA."),
        (6, YUG, "upper left", "THEY HEAR THE DIFFERENCE.")),
  R("naruto_v4_armor", "yugao_v4", "kiri_rebel_mob", "env_mizukage_tower"), "medium"),

 ("p06", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + MEI_V4.format(i=1) + N16_ARMOR.format(i=2) + YUGAO_V4.format(i=3) + ENV.format(i=4)
  + ONLY(MEI, BOY16, YUG, "one blurred Kiri worker in the far background") + REPAIRED +
  "FIVE panels. The auburn-haired leader contests his self-description.\n"
  "PANEL 1 (top right): medium-long doorway shot — she steps out of a rebuilt administrative "
  "doorway at left and turns into the teen's path; he and the kunoichi enter from the right "
  "moving left, eye-lines shifting to her.\n"
  "PANEL 2 (top left): medium two-shot — the teen passes her on the right-to-left line, turning "
  "only his eyes back; she pivots to keep pace.\n"
  "PANEL 3 (middle band, full width): close profile two-shot — she at left faces right into his "
  "profile at right; their eye-lines meet across the centre. THE BALLOON IN THIS PANEL IS SPOKEN "
  "BY THE AUBURN-HAIRED WOMAN — its tail must touch HER mouth and must not approach the teen; his "
  "mouth is closed.\n"
  "PANEL 4 (dominant bottom right): close-up — the teen fills the right half facing left, "
  "controlled; a blurred worker and a red-and-white fan crest motif sit far behind at left.\n"
  "PANEL 5 (bottom left): medium close-up — she stands at right facing left, watching his back "
  "leave through the left edge, still. " + L_KIRI
  + SAY((1, MEI, "upper right", "I DON'T."),
        (2, BOY16, "upper left", "I CAME TO TEST MYSELF."),
        (3, MEI, "upper right", "AND YAGURA?"),
        (4, BOY16, "upper right", "HE MADE JINCHŪRIKI LOOK LIKE MONSTERS—AND THE UCHIHA LOOK LIKE BUTCHERS."),
        (5, MEI, "upper left", "THAT IS STILL A REASON.")),
  R("mei_v4", "naruto_v4_armor", "yugao_v4", "env_mizukage_tower"), "medium"),

 # ---- Spread 4: the missing Three-Tails --------------------------------------------
 ("p07", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ENV.format(i=3)
  + ONLY(BOY16, ZETSU) + REPAIRED +
  "FIVE panels. A tactical discovery on a bare ridge above the village.\n"
  "PANEL 1 (top band, full width): extreme-wide ridge shot — the teen stands at right facing "
  "left toward distant Kiri; the plant creature rises vertically out of the rock at lower left, "
  "two-toned face turned right toward him.\n"
  "PANEL 2 (middle right): medium rear three-quarter — the teen with his back to the creature, "
  "looking left toward the village; the creature a blurred half-figure at lower left.\n"
  "PANEL 3 (middle left): close-up — the creature centred facing right, eye-line fixed on the "
  "teen outside the panel.\n"
  "PANEL 4 (bottom right): tight profile close-up — the teen faces left, still; mist moves "
  "left-to-right behind him.\n"
  "PANEL 5 (bottom left): tight frontal close-up — the creature faces slightly right, grin "
  "opening, eyes still on him. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "YOU COULD HAVE TAKEN THE THREE-TAILS."),
        (2, BOY16, "upper right", "YAGURA DIED WITH IT."),
        (3, ZETSU, "upper left", "IT WILL REFORM."),
        (4, BOY16, "upper right", "NOT FOR YEARS."),
        (5, ZETSU, "upper left", "AKATSUKI CANNOT SEAL THE FOURTH BEFORE THE THIRD.")),
  R("naruto_v4_armor", "zetsu", "env_kiri_fogline"), "low"),

 ("p08", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ONLY(BOY16, ZETSU,
    "a sand-coloured one-tailed tanuki silhouette and a blue-flamed two-tailed cat silhouette, "
    "each appearing ONLY as a distant symbolic background shape") + REPAIRED +
  "SEVEN panels. His counter-strategy, named target by target.\n"
  "PANEL 1 (top right): close-up — the teen faces left toward the creature off-panel, no body "
  "movement.\n"
  "PANEL 2 (top centre): close-up — the creature faces right toward him off-panel.\n"
  "PANEL 3 (top left): tight face close-up — the teen faces left, eye and mouth steady.\n"
  "PANEL 4 (middle right): symbolic medium-long image — the creature as a black shoulder "
  "silhouette at right facing left; a huge SAND-COLOURED one-tailed tanuki silhouette fills the "
  "left background, flat and featureless.\n"
  "PANEL 5 (middle left): symbolic medium-long image — the creature's silhouette now anchors the "
  "left facing right; a BLUE-FLAMED two-tailed cat silhouette fills the right background, drawn "
  "as flat opaque blue flame shapes.\n"
  "PANEL 6 (bottom right): medium low angle — the teen steps one pace left toward the ridge edge "
  "and squares his shoulders toward both distant silhouettes; the creature behind at far right, "
  "watching.\n"
  "PANEL 7 (bottom left, the focal panel): tight frontal close-up against storm clouds — the teen "
  "centred, looking up-left into the coming weather, wind pushing his long hair left. " + L_RIDGE
  + SAY((1, BOY16, "upper right", "THEIR ORDER IS BROKEN."),
        (2, ZETSU, "upper centre", "WILL YOU HUNT THEM?"),
        (3, BOY16, "upper left", "NO. WATCH THEM."),
        (4, ZETSU, "upper right", "AND WHEN THEY MOVE FOR SHUKAKU?"),
        (5, ZETSU, "upper left", "OR THE TWO-TAILS?"),
        (6, BOY16, "upper right", "I STAND IN THE WAY."),
        (7, BOY16, "upper left", "OBITO WILL HAVE TO STOP THINKING OF ME AS A CHILD.")),
  R("naruto_v4_armor", "zetsu"), "medium"),

 # ---- Spread 5: force Obito's hand, then the nearer plan ---------------------------
 ("p09", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ONLY(BOY16, ZETSU) + REPAIRED +
  "SIX panels. The creature tests each inference.\n"
  "PANEL 1 (top band, full width): SILENT medium profile two-shot — the teen at right facing "
  "left, the creature at left facing right, studying him across a clear gap; neither moves. No "
  "text in this panel.\n"
  "PANEL 2 (middle right): close-up — the creature faces right, chin lifted toward him.\n"
  "PANEL 3 (middle centre): close-up — the teen faces left, lowering his eye-line toward the "
  "creature.\n"
  "PANEL 4 (middle left): tight close-up — the creature faces right, one brow ridge rising.\n"
  "PANEL 5 (bottom right): medium close-up — the teen faces left but turns his eyes down-right "
  "in calculation.\n"
  "PANEL 6 (bottom left): close-up — the creature faces right, smiling wider; the teen's "
  "shoulder edge enters from far right. " + L_RIDGE
  + SAY((2, ZETSU, "upper right", "HE COULD COME HIMSELF."),
        (3, BOY16, "upper centre", "NOT WHILE NAGATO LIVES."),
        (4, ZETSU, "upper left", "THEN HE SENDS NAGATO."),
        (5, BOY16, "upper right", "IF HIS PRIDE IS AS RELIABLE AS YOU SAY."),
        (6, ZETSU, "upper left", "THINGS ARE BECOMING INTERESTING.")),
  R("naruto_v4_armor", "zetsu"), "low"),

 ("p10", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + SAS.format(i=3) + KAK.format(i=4)
  + ONLY(BOY16, ZETSU,
         "the younger dark-haired boy and the masked silver-haired man appearing ONLY inside one "
         "pale hard-edged memory image, never on the ridge") + REPAIRED +
  "SIX panels. An approach interrupts his future war.\n"
  "PANEL 1 (top right): tight close-up — the creature faces right; its smile drops, eyes fixing "
  "on the teen.\n"
  "PANEL 2 (top centre): tight face close-up — the teen keeps his head forward while his visible "
  "eye shifts left toward the creature; his mouth stays in frame.\n"
  "PANEL 3 (top left): close-up — the creature faces right, gaze level.\n"
  "PANEL 4 (middle band, full width): shallow-focus memory shot — the present teen is a dark "
  "profile at right facing left; in the pale desaturated background the YOUNGER dark-haired boy "
  "walks left beside the masked silver-haired man, both facing away.\n"
  "PANEL 5 (bottom right): SILENT medium tracking shot — the teen turns from the ridge and walks "
  "right toward Kiri, eyes on the path; the creature pivots to follow one pace behind. No text in "
  "this panel.\n"
  "PANEL 6 (bottom left, the focal panel): tight two-shot, creature foreground — the creature "
  "fills the left facing right toward the teen's back at far right; the teen continues without "
  "looking back. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "JIRAIYA FOUND YOU."),
        (2, BOY16, "upper centre", "ALONE?"),
        (3, ZETSU, "upper left", "KAKASHI. SASUKE."),
        (4, BOY16, "upper right", "HE FINISHED TRAINING."),
        (6, ZETSU, "upper left", "DANZŌ AND THE ADVISERS HAVE A PLAN FOR BOTH OF YOU.")),
  R("naruto_v4_armor", "zetsu", "sasuke", "kakashi"), "medium"),

 # ---- Spread 6: the clan as a village resource -------------------------------------
 ("p11", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ONLY(BOY16, ZETSU) + REPAIRED +
  "FIVE panels. Political ownership, not romance.\n"
  "PANEL 1 (top right): medium side shot — the teen walks right in the foreground looking "
  "forward; the creature follows at left facing right.\n"
  "PANEL 2 (top left): close-up — the creature faces right, eyes on the teen off-panel.\n"
  "PANEL 3 (middle band, full width): tight profile — the teen occupies the right facing right "
  "but glances back left toward the creature.\n"
  "PANEL 4 (bottom right, the focal panel): symbolic overhead insert, NO people — two blank "
  "council documents lie parallel on dark wood beside a red-and-white fan crest. The documents "
  "carry ILLEGIBLE SCRIBBLE only, no readable words.\n"
  "PANEL 5 (bottom left): medium close-up — the creature stands at right facing left toward the "
  "teen outside the panel, expression curious rather than teasing. " + L_RIDGE
  + SAY((1, BOY16, "upper right", "THE CLAN RESTORATION ACT."),
        (2, ZETSU, "upper left", "YOU KNEW?"),
        (3, BOY16, "upper right", "THEY SEE TWO PAIRS OF EYES."),
        (4, OFF(BOY16), "upper right", "THEY WANT A VILLAGE SUPPLY."),
        (5, ZETSU, "upper left", "YOU STILL NEED HEIRS.")),
  R("naruto_v4_armor", "zetsu"), "low"),

 ("p12", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ONLY(BOY16, ZETSU) + REPAIRED +
  "SIX panels. He evades one question and advances the other.\n"
  "PANEL 1 (top right): close-up — the creature faces left toward the teen and tilts its head.\n"
  "PANEL 2 (top centre): SILENT extreme close-up — the teen's flat eye-line points left at the "
  "creature; he does not move. No text in this panel.\n"
  "PANEL 3 (top left): medium close-up — the teen at right facing left; the creature's shoulder "
  "enters from far left.\n"
  "PANEL 4 (middle band, full width): tracking two-shot — the teen turns his head forward and "
  "resumes walking right; the creature follows, eyes staying on him.\n"
  "PANEL 5 (bottom right): close-up — the creature faces right toward the teen off-panel, mouth "
  "curving in acknowledgement of the evasion.\n"
  "PANEL 6 (bottom left): tight frontal close-up — the teen centred, walking toward the reader "
  "before turning right out of frame, eye-line level. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "HAVE YOU CHOSEN ANYONE?"),
        (3, BOY16, "upper left", "I HAVE NOT STARTED LOOKING."),
        (4, BOY16, "upper right", "HAVE YOU FOUND OROCHIMARU?"),
        (5, ZETSU, "upper right", "STONE COUNTRY. THE BODY YOU DAMAGED IS FAILING."),
        (6, BOY16, "upper left", "GOOD.")),
  R("naruto_v4_armor", "zetsu"), "low"),

 # ---- Spread 7: waiting for Sasuke -------------------------------------------------
 ("p13", dict(scene="dialogue", light="overcast", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ENV.format(i=3)
  + ONLY(BOY16, ZETSU) + REPAIRED +
  "FIVE panels. He waits for one person, and it is not the one expected.\n"
  "PANEL 1 (top band, full width): wide side shot — the teen and the creature walk right along "
  "the ridge, the teen one body-length ahead; both face right, the creature's eyes on him.\n"
  "PANEL 2 (middle right): close-up — the teen faces right and does not slow.\n"
  "PANEL 3 (middle centre): close-up — the creature faces right but looks up-left toward him.\n"
  "PANEL 4 (middle left): tight profile close-up — the teen faces right, eyes fixed ahead.\n"
  "PANEL 5 (bottom band, full width): medium-long two-shot — the creature stops at left and "
  "begins sinking straight down into the rock while facing right; the teen stops at right but "
  "does not turn. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "JIRAIYA WILL REACH KIRI IN A FEW DAYS."),
        (2, BOY16, "upper right", "THEN OROCHIMARU WAITS."),
        (3, ZETSU, "upper centre", "FOR JIRAIYA?"),
        (4, BOY16, "upper left", "FOR SASUKE."),
        (5, ZETSU, "upper left", "I'LL RETURN WITHIN A WEEK—MAYBE BEFORE THEY ARRIVE.")),
  R("naruto_v4_armor", "zetsu", "env_kiri_fogline"), "low"),

 ("p14", dict(scene="establishing", light="dusk", cast="solo", mood="somber", panels=4),
  FILL + RTL + N16_ARMOR.format(i=1) + ZET.format(i=2) + ZOR + ENV.format(i=3)
  + ONLY(BOY16, "the plant creature's upper face, sinking away in panel 1 only") + REPAIRED +
  "FOUR panels. ENTIRELY SILENT — no balloons, no captions, no sound effects, no text of any "
  "kind anywhere on this page.\n"
  "PANEL 1 (top right): medium shot — only the creature's upper face remains above the rock at "
  "lower left, looking right; the teen stands at far right facing away toward the village. The "
  "creature continues downward.\n"
  "PANEL 2 (top left): ground-level insert — the creature is gone; a closing ripple in the rock "
  "travels right-to-left and stops beside the teen's stationary boot at far right. No face.\n"
  "PANEL 3 (bottom right): extreme-wide sunset — the teen alone at lower right facing left "
  "toward the village, wind driving his hair and the ridge grass left.\n"
  "PANEL 4 (bottom left, the focal panel): medium rear shot — the teen fills the right half with "
  "his back to the reader, head angled left toward the village lights below; the empty space "
  "where the creature stood holds the left half. " + L_DUSKR,
  R("naruto_v4_armor", "zetsu", "env_kiri_moonlit_hill"), "medium"),

 # ---- Spread 8: Sasuke, the snake, the missing half --------------------------------
 ("p15", dict(scene="establishing", light="dusk", cast="solo", mood="somber", panels=4),
  FILL + RTL + SAS.format(i=1) + N16_ARMOR.format(i=2) + ENV.format(i=3)
  + ONLY(BOY16, "the younger dark-haired boy appearing ONLY inside one bordered memory panel")
  + REPAIRED +
  "FOUR panels. His sequence puts a person before a target.\n"
  "PANEL 1 (top band, full width): SILENT extreme-wide dusk exterior, NO characters — the empty "
  "road out of Kiri runs from lower right toward the far-left horizon, mist drifting slowly left "
  "across it. No traveller, no silhouette. No text in this panel.\n"
  "PANEL 2 (middle right): true-memory medium close-up with a HARD WHITE BORDER and desaturated "
  "colour — the YOUNGER dark-haired boy, exactly as last seen years ago, centred and still, "
  "facing right, his eye-line meeting the reader's side of the panel.\n"
  "PANEL 3 (middle left): overhead insert, NO people — a route map lying still, drawn as a "
  "diagonal from a coastal mark at upper right to a mountain mark at lower left with a small "
  "snake mark at the endpoint; all map text is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 4 (bottom band, full width): SILENT tracking medium profile — the teen turns left-to-"
  "right and starts down the ridge toward the village, right foot leading, eyes on the road "
  "ahead. No text in this panel. " + L_DUSKR
  + SAY((2, OFF(BOY16), "upper right", "SASUKE FIRST."),
        (3, OFF(BOY16), "upper left", "THEN OROCHIMARU."))
  + "Both balloons are TAIL-LESS THOUGHT BALLOONS with a soft cloud edge, not speech balloons. ",
  R("sasuke", "naruto_v4_armor", "env_kiri_mist_gate"), "medium"),

 ("p16", dict(scene="emotional_closeup", light="dusk", cast="solo", mood="tense", panels=4),
  FILL + RTL + N16_ARMOR.format(i=1) + KURAMA_FULL.format(i=2) + SAS.format(i=3)
  + ONLY(BOY16,
         "the nine-tailed fox appearing ONLY as a half-dissolved symbolic silhouette, and the "
         "younger dark-haired boy's single red eye appearing ONLY inside the panel-3 sequence "
         "image") + REPAIRED +
  "FOUR panels. LAST PAGE OF THE CHAPTER — it ends on a fatal decision.\n"
  "PANEL 1 (top right): close-up insert — the teen's gloved hand rests over the centre of his "
  "own stomach where a seal once sat, torso facing right, fingers closing slightly inward.\n"
  "PANEL 2 (top left): abstract remembered wide shot — the nine-tailed fox stands at right "
  "facing left, but HALF of his nine-tailed silhouette dissolves into empty white space at the "
  "left; the teen is a tiny figure below, facing up-right toward him.\n"
  "PANEL 3 (bottom right): narrow vertical sequence image, NO full characters — from top to "
  "bottom, static and evenly spaced: a single blood-red eye with three black comma marks; a "
  "small purple-grey snake emblem; the fox's divided silhouette.\n"
  "PANEL 4 (bottom left, the focal panel): tight low-angle close-up — the teen fills the panel "
  "facing right into darkness, long hair moving left, visible eye level, mouth barely moving. "
  + L_DUSKR
  + SAY((1, OFF(BOY16), "upper right", "KURAMA IS STILL MISSING HALF OF HIMSELF."),
        (2, OFF(BOY16), "upper left", "I PROMISED TO RETURN IT."),
        (4, OFF(BOY16), "upper left", "THIS TIME, OROCHIMARU WILL NOT SURVIVE."))
  + "All three balloons are TAIL-LESS THOUGHT BALLOONS with a soft cloud edge, not speech "
    "balloons. ",
  R("naruto_v4_armor", "kurama_full", "sasuke"), "high"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch01" / "raw", HERE / "v5ch01" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
