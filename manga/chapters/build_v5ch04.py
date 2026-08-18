"""Volume 5, Chapter 4 — "The Open Cage". 18 pages.

Source: fic ch12:395-515. Translated 1:1 from story/volume_05/drafts/ch04_the_open_cage.md —
67 spoken/pain-cry balloons, one thought balloon, one tail-less memory echo, five captions,
one chapter marker and 18 sound effects across 18 pages. Reading order is RIGHT TO LEFT per
the approved `name`; every page states it.

This builder must match the `name`, not improve on it. Every balloon below is the draft's
exact final text, in the draft's exact panel and position. No line is reworded or merged.

Pages 1 (panels 1-2) and 18 (panels 4-5) are PRESENT-DAY Kiri. Everything between them is a
READER-ONLY flashback about one year after Naruto left Konoha; it is editorial framing, not a
memory Naruto experiences, and the present-day cast learns nothing from it. Present-day
Naruto and flashback Naruto are deliberately different ages and costumes; the two pages that
carry both states say so explicitly, panel by panel.

Chakra rule for the whole chapter: every chakra shape is FLAT and OPAQUE with a hard outline,
never glowing and never washing the scene out. Pages that show physical strain state that no
injury detail and no blood appears.

Reference gaps recorded for the owner (never invented here): there is no Dragon Land / basalt
caldera environment plate in refs/images, so the volcanic wilderness and the sheltering
fissure are carried entirely by prose on pages 5, 7, 12-18 and no environment reference is
bound to them; there is no dedicated Minato sheet, so he is bound from the two-person
minato_kushina.png with the red-haired half explicitly excluded; and there is no approved
younger-training-period Naruto sheet, so naruto_v4_black.png carries the flashback boy with an
explicit "read him younger" clause.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, FILL, JIR, KAK, MAN, OFF, ONLY, R, SAGE, SAY, SFX, ZET  # noqa: E402
from prompts_v4 import (KURAMA_FULL, KURAMA_INNER, N16_BLACK, N16_SWORD,     # noqa: E402
                        SASUKE16, YUGAO_V4, KURAMA_SPEAKER, N16_SPEAKER,
                        SASUKE16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
BOY = "the younger long-haired blond boy in the plain black shirt with the red spiral"
FOX = KURAMA_SPEAKER
SAS16 = SASUKE16_SPEAKER
YUG = YUGAO_V4_SPEAKER
MIN = "the blond man in the white flame-hemmed coat"
ZETSU = "the split black-and-white plant creature"
WZ = "the separated WHITE half of the plant creature"
BZ = "the separated BLACK half of the plant creature"

ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")

# Every chakra shape in this chapter obeys this. It is the chapter's single biggest failure mode.
FLAT = ("CHAKRA RULE — every chakra shape on this page (the seal formula, the leaking thread, the "
        "tether, the fox's chakra mass, the settling haze) is drawn as a FLAT, FULLY OPAQUE shape "
        "with a HARD BLACK OUTLINE. It does NOT glow, does NOT bloom, does NOT blur and does NOT "
        "emit light. It never washes the scene out: the environment, the ground, the sky, the "
        "figures and every panel edge stay fully drawn, fully coloured and completely legible "
        "behind, around and through every chakra shape. ")
NOBLOOD = ("No injury detail and no blood appears anywhere on this page: no wounds, no cuts, no "
           "torn flesh, no red spatter and no gore. Physical cost is shown only through posture, "
           "pallor and strain. ")
NOEYE = ("NO EYE-CONTROL EFFECT APPEARS ANYWHERE ON THIS PAGE: no Sharingan reflected in the fox's "
         "eyes, no genjutsu rings, no hypnotic spiral and no visual tether running from anyone's "
         "gaze. ")
SCRIB = ("Every seal marking, every line of the seal formula and every scrap of seal paper anywhere "
         "on this page is ILLEGIBLE SCRIBBLE, not readable words. ")

YOUNGER = ("The blond figure in this flashback is the YOUNGER training-period version, about one "
           "year after he left Konoha: draw him clearly YOUNGER, slighter and shorter than the "
           "present-day sixteen-year-old. He wears no red armour, no gunbai, no sword and no "
           "forehead protector. His visible left eye is an ORDINARY BLUE EYE with no red iris, no "
           "tomoe and no six-bladed pattern. ")
NOW = ("The present-day blond teen is approximately sixteen in his repaired bright red segmented "
       "armour, with the dark purple gunbai on his BACK and the plain straight sash sword in its "
       "sheath at his LEFT HIP. His visible left eye carries the ORDINARY ACTIVE THREE-TOMOE "
       "SHARINGAN — a blood-red iris with a black pupil and exactly three black comma marks, never "
       "the six-bladed pattern and never blue. ")

INNER = ("THIS SPACE IS THE INNER SEAL WORLD INSIDE NARUTO'S OWN BODY, not a place he has travelled "
         "to: a flooded stone sewer with shallow standing water underfoot, no sky, no horizon, no "
         "weather and no exterior scenery of any kind. The GREAT BARRED GATE stands intact and "
         "closed unless the panel says otherwise, with the enormous fox behind it. ")
DRAGON = ("THIS IS THE ANCIENT LAND OF DRAGONS: a Fire-Forest-like wilderness broken by ACTIVE "
          "VOLCANIC VENTS, with dark basalt terraces stepping down from right to left into a "
          "caldera beneath a flat ash-red sky. There is no village, no road, no building and no "
          "other person anywhere in it. ")

MINATO_PARTIAL = (
    "Image {i} is a TWO-PERSON REFERENCE SHEET. Use ONLY THE LEFT-HAND FIGURE — the blond man — and "
    "COMPLETELY IGNORE the red-haired woman on the right of that sheet, who does not appear "
    "anywhere in this chapter. The left-hand figure is the CHARACTER REFERENCE for the blond man: "
    "an adult with short spiky bright-yellow hair, two long chin-length bangs framing his face, "
    "blue eyes, a plain forehead protector, a dark navy long-sleeved uniform under a green flak "
    "vest, and a long WHITE COAT with red flame patterning along its hem. Reproduce his face, hair "
    "and outfit exactly; ignore the sheet's white background, its lineup layout and its neutral "
    "standing pose. HE IS STORED CHAKRA, NOT A LIVING BODY: draw him in a flat, pale, desaturated "
    "palette with a hard visible outline and his edges slightly see-through — with NO glow, NO "
    "light bloom and no ghostly wisps. ")

ENV_SEWER = ("Image {i} is the LOCATION REFERENCE for the inner seal space — reuse its damp "
             "stonework, shallow standing water, great barred gate and colour palette. Do not copy "
             "its camera angle; ignore that it is empty of people. ")
ENV_STREET = ("Image {i} is the LOCATION REFERENCE for the rebuilding Kiri street beneath the "
              "repaired tower — reuse its architecture, scaffolding, wet stone and colour palette. "
              "Do not copy its camera angle; ignore that it is empty of people. ")

L_SEWER = ("Lighting: cold blue-green light off shallow standing water in a windowless stone "
           "sewer, hard flat shadows, no sky and no exterior light source. ")
L_ASH = ("Lighting: flat ash-red daylight under a volcanic sky, dull grey-black basalt, hard "
         "shadows and no sun disc. ")
L_FISSURE = "Lighting: dim sheltered light inside a narrow basalt fissure, cool and flat. "
L_KIRI = "Lighting: clean pale mist-filtered daylight over a village that is still rebuilding. "

PAGES = [
 # ---- Spread 1: the answer Jiraiya does not receive ----------------------------------
 ("p01", dict(scene="establishing", light="dark", cast="small_group", mood="tense", panels=4),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KAK.format(i=3) + SASUKE16.format(i=4)
  + YUGAO_V4.format(i=5) + N16_BLACK.format(i=6) + KURAMA_INNER.format(i=7)
  + ENV_STREET.format(i=8) + ENV_SEWER.format(i=9)
  + ONLY(BOY16, SAGE, MAN, SAS16, YUG,
         "the YOUNGER blond boy, who appears only from PANEL 3 onward inside the reader-only "
         "flashback and is never in the Kiri street",
         "the enormous nine-tailed fox, which appears only in PANEL 4 behind the barred gate")
  + NOW + YOUNGER + FLAT + NOEYE + SCRIB +
  "FOUR panels. PANELS 1-2 ARE PRESENT-DAY KIRI (Image 8). PANELS 3-4 ARE A READER-ONLY FLASHBACK "
  "INSIDE THE INNER SEAL SPACE (Image 9) about one year earlier. The two blond figures are "
  "DIFFERENT AGES and never share a panel: the armoured sixteen-year-old appears only in PANELS "
  "1-2, and the younger boy only in PANELS 3-4.\n"
  + INNER +
  "PANEL 1 (top right, horizontal strip): present-day Kiri, matching the previous chapter's closing "
  "geometry. The armoured blond teen stands at frame RIGHT facing left; the big white-haired man is "
  "a soft out-of-focus foreground shoulder at frame LEFT facing right. The masked silver-haired "
  "man, the older dark-haired teen and the purple-haired kunoichi stay small behind him at the "
  "left. Their eye-lines meet and he gives no answer. His gunbai stays on his back and his sash "
  "sword is visibly equipped at his left hip; if this narrow strip crops below the hilt, THE CAMERA "
  "IS MERELY HIDING THE SWORD — he remains equipped with it. No text in this panel.\n"
  "PANEL 2 (top left, narrow close-up): SILENT — the armoured teen's ordinary three-tomoe Sharingan "
  "fills the panel; there is no six-bladed pattern. Its pupil match-cuts EDITORIALLY, not as a "
  "thought or a memory cue, into a black sewer opening at the panel's left edge: no cloud border, "
  "no ripple frame and no dream border. No text in this panel.\n"
  "PANEL 3 (middle panel, full width): the flashback begins. The YOUNGER blond boy enters the inner "
  "sewer from the RIGHT and walks left through shallow water; his reflected steps lead the eye "
  "toward the unseen cage. RESERVE clean dark-wall negative space at the UPPER LEFT of this panel: "
  "no figure, ripple, reflection, effect or balloon may enter it, and it carries only the chapter "
  "marker.\n"
  "PANEL 4 (dominant bottom panel): the great barred gate spans the LEFT two-thirds. The enormous "
  "nine-tailed fox lies behind it with his head on his paws, facing right. The younger boy stops "
  "small at the LOWER RIGHT, facing left. " + L_SEWER
  + CAP(3, "small upper-right box", "ABOUT ONE YEAR AFTER NARUTO LEFT KONOHA.")
  + SFX(3, "STEP", "Place it low in the water behind his heel.")
  + 'LETTERING: in the protected dark-wall negative space at the UPPER LEFT of PANEL 3, write the '
    'chapter marker in bold upright English capitals on one line: "CHAPTER 4 — THE OPEN CAGE". It '
    'is a tail-less title marker, not a balloon. '
  + SAY((4, BOY, "upper right", "HELLO, KYŪBI."),
        (4, FOX, "upper left", "WHAT DO YOU WANT?"))
  + "The PANEL 4 left balloon belongs to the FOX: thread its tail between the bars of the gate to "
    "his muzzle. The caption box, the chapter marker and the one sound effect specified above are "
    "the only other text permitted on this page. ",
  R("naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16", "yugao_v4", "naruto_v4_black",
    "kurama_inner", "env_mizukage_tower", "env_inner_sewer"), "high"),

 ("p02", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEWER.format(i=3)
  + ONLY(BOY, FOX) + YOUNGER + INNER + FLAT + NOEYE + SCRIB +
  "FIVE panels. The exchange is stated and the history that makes it unacceptable is exposed.\n"
  "AXIS LOCK: the boy stays at reader-RIGHT looking and moving LEFT toward the gate; the fox stays "
  "at reader-LEFT behind the bars looking RIGHT. This axis never flips.\n"
  "PANEL 1 (top right, close-up): the fox's near eye opens, aimed down-right at the boy.\n"
  "PANEL 2 (top left, medium): the boy at frame RIGHT faces left with his arms folded; the gate "
  "bars remain visible along the left border.\n"
  "PANEL 3 (middle right, inset): the fox's muzzle behind one bar.\n"
  "PANEL 4 (middle left, wide): the boy holds the fox's eye-line without advancing.\n"
  "PANEL 5 (dominant bottom panel, the focal panel): the fox raises his head and the bars divide "
  "his face, while the boy remains a small silhouette at the LOWER RIGHT. " + L_SEWER
  + SAY((1, FOX, "upper right", "MAKE IT QUICK."),
        (2, BOY, "upper right", "I WANT TO OFFER YOU SOMETHING."),
        (2, BOY, "upper left", "IN RETURN, I WANT SOMETHING FROM YOU."),
        (3, FOX, "upper right", "WHAT?"),
        (4, BOY, "upper right", "IF I GIVE YOU YOUR FREEDOM, COME WHEN I CALL."),
        (5, FOX, "upper right", "MY FREEDOM—FOR ANOTHER SHARINGAN TO CONTROL ME?"),
        (5, FOX, "upper left", "I WOULD RATHER STAY HERE."))
  + "BALLOON STACKS: the two PANEL 2 balloons are one connected stack with ONE shared visible tail "
    "to the boy; the second balloon inherits that tail and grows no tail of its own. The two PANEL "
    "5 balloons are one connected stack with ONE shared visible tail threading between the bars to "
    "the fox. Every fox balloon's tail passes between the bars and never crosses one. ",
  R("naruto_v4_black", "kurama_inner", "env_inner_sewer"), "low"),

 # ---- Spread 2: freedom without agreement -------------------------------------------
 ("p03", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEWER.format(i=3)
  + ONLY(BOY, FOX) + YOUNGER + INNER + FLAT + NOEYE + SCRIB +
  "SIX panels. Distrust presses the claim instead of letting it stand uncontested.\n"
  "AXIS LOCK: the boy stays at reader-RIGHT facing left; the fox stays at reader-LEFT behind the "
  "bars facing right.\n"
  "PANEL 1 (top right, close-up): the boy, still at frame right and facing left.\n"
  "PANEL 2 (top left, close-up): the fox's lip lifts over one fang.\n"
  "PANEL 3 (middle right, medium): the boy lifts two fingers toward his own eye but activates NO "
  "technique — no eye pattern changes, no chakra appears at his hand and no light is emitted.\n"
  "PANEL 4 (middle left, medium): his hand lowers; the fox watches from behind the bars.\n"
  "PANEL 5 (bottom right, narrow reaction): SILENT — the fox's eye narrows. No text in this panel.\n"
  "PANEL 6 (bottom left, medium): the boy stays motionless with a deliberate stretch of empty water "
  "between him and the gate. " + L_SEWER
  + SAY((1, BOY, "upper right", "I NEVER SAID I WOULD CONTROL YOU."),
        (2, FOX, "upper left", "HUMANS SAY ONE THING."),
        (2, FOX, "immediately below and touching the upper left balloon", "THEN THEY DO ANOTHER."),
        (3, BOY, "upper right", "YOU LIVE INSIDE MY BODY."),
        (4, BOY, "upper right", "YOU KNOW I COULD FORCE YOU."),
        (6, BOY, "upper right", "I HAVE NOT."),
        (6, BOY, "upper left", "CONTROL IS BENEATH ME."))
  + "BALLOON STACKS: the two PANEL 2 balloons are one connected stack with ONE shared visible tail "
    "threading between the bars to the fox. The two PANEL 6 balloons are one connected stack with "
    "ONE shared visible tail to the boy. Continuation balloons grow no tails of their own. ",
  R("naruto_v4_black", "kurama_inner", "env_inner_sewer"), "low"),

 ("p04", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEWER.format(i=3)
  + ONLY(BOY, FOX) + YOUNGER + INNER + FLAT + NOEYE + SCRIB +
  "SIX panels. A failed negotiation becomes an irreversible gift.\n"
  "AXIS LOCK: the boy stays at reader-RIGHT; the fox stays at reader-LEFT behind the closed bars.\n"
  "PANEL 1 (top right, medium): the boy looks up at the fox, eye-line running left and upward.\n"
  "PANEL 2 (top left, close-up): the fox's stare hardens. THE BOY IS NOT DRAWN IN THIS PANEL.\n"
  "PANEL 3 (middle panel, full width): the fox rises behind the gate and leans right; his tails "
  "flare across the LEFT background as flat opaque shapes. The boy does not step back. The bars "
  "hold and the gate stays closed.\n"
  "PANEL 4 (lower right, small): the boy turns his shoulders toward the sewer exit on the RIGHT but "
  "looks back left.\n"
  "PANEL 5 (lower middle, small): the boy takes one step RIGHT, away from the cage.\n"
  "PANEL 6 (dominant lower-left panel, the focal panel): the boy walks into the right-side darkness "
  "with his back to the fox; the open water between him and the barred beast is the image. "
  + L_SEWER
  + SAY((1, BOY, "upper right", "I DO NOT BELIEVE YOU ARE A MINDLESS BEAST."),
        (2, OFF(BOY), "upper right", "BUT YOUR HATRED IS MAKING YOUR CHOICES FOR YOU."),
        (3, FOX, "upper left", "IF THIS CAGE WERE OPEN, I WOULD TEAR YOU APART."),
        (4, BOY, "upper right", "YOU WOULD RATHER I LIED?"),
        (5, BOY, "upper right", "I ASKED FOR YOUR HELP TO MAKE YOU LISTEN."),
        (6, BOY, "upper right", "IT DOES NOT MATTER."),
        (6, BOY, "upper middle", "YOU WILL STILL HAVE YOUR FREEDOM."),
        (6, BOY, "upper left", "I WILL RETURN IN TWO DAYS."))
  + "The PANEL 2 off-panel tail enters from that panel's RIGHT border and stops there; it must not "
    "touch or aim at the fox's face. BALLOON STACK: the THREE PANEL 6 balloons are one connected "
    "stack sharing ONE single visible tail to the boy — the second and third balloons inherit that "
    "one tail and grow no tails of their own. ",
  R("naruto_v4_black", "kurama_inner", "env_inner_sewer"), "low"),

 # ---- Spread 3: three forces against one seal ---------------------------------------
 ("p05", dict(scene="establishing", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(BOY, ZETSU) + YOUNGER + DRAGON + FLAT + NOEYE + SCRIB +
  "FIVE panels. The extraction plan is made legible before the inner and outer worlds intercut.\n"
  "AXIS LOCK for the physical world: the boy is at centre-RIGHT and the plant creature kneels to "
  "his LEFT; everything the pair pulls travels LEFT with the reading direction.\n"
  "PANEL 1 (top band, full width, half the page height): extreme-wide establishing shot — basalt "
  "terraces descend from right to left into a caldera beneath a flat ash-red sky, with active "
  "volcanic vents smoking in the middle distance. The boy and the plant creature are SMALL at "
  "centre-right.\n"
  "PANEL 2 (middle right, medium): the boy kneels at centre-right facing left; the plant creature "
  "crouches to his LEFT, facing right.\n"
  "PANEL 3 (middle left, medium): the plant creature holds the boy's eye-line.\n"
  "PANEL 4 (bottom right, medium): the boy places one hand flat over his own abdomen. No seal "
  "formula has appeared yet.\n"
  "PANEL 5 (bottom left, wide): the boy closes his eyes while the plant creature braces one knee "
  "against the basalt to his LEFT. The caldera slopes carry the eye leftward. " + L_ASH
  + CAP(1, "upper right", "TWO DAYS LATER — ANCIENT LAND OF DRAGONS.")
  + SAY((2, BOY, "upper right", "I WILL WEAKEN MINATO'S SEAL FROM INSIDE."),
        (3, ZETSU, "upper left", "I PULL THE NINE-TAILS OUT FROM HERE."),
        (4, BOY, "upper right", "THE KYŪBI PUSHES FROM THE OTHER SIDE."),
        (5, ZETSU, "upper right", "AND IF THE SEAL HOLDS?"),
        (5, BOY, "upper left", "WE BREAK IT."))
  + "In PANEL 5 the upper-right balloon belongs to the PLANT CREATURE at frame LEFT and the upper-"
    "left balloon belongs to the BOY at frame RIGHT: draw both tails long, thin and clearly "
    "separated so neither can be read as belonging to the nearer figure. The caption specified "
    "above is the only other text on this page. ",
  R("naruto_v4_black", "zetsu"), "medium"),

 ("p06", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ZET.format(i=3)
  + ENV_SEWER.format(i=4) + ZOR + ONLY(BOY, FOX, ZETSU) + YOUNGER + INNER + FLAT + NOEYE + SCRIB
  + NOBLOOD +
  "SIX panels. The three-part action begins in the order he specified.\n"
  "PANELS 1 AND 3-6 ARE THE INNER SEAL WORLD (Image 4). PANEL 2 IS THE PHYSICAL CALDERA: basalt "
  "terraces under an ash-red sky, no sewer stone and no bars.\n"
  "PANEL 1 (top right, medium, inner world): the boy reappears visibly at frame RIGHT facing the "
  "gate; the fox stands behind it at frame LEFT.\n"
  "PANEL 2 (top left, narrow, physical world): SILENT — the plant creature waits to the LEFT of the "
  "boy's kneeling body on the basalt. No text in this panel.\n"
  "PANEL 3 (middle panel, full width, inner world): the fox leans right into the bars; the boy "
  "points once toward him.\n"
  "PANEL 4 (bottom right, close-up, inner world): the black seal formula appears across the boy's "
  "exposed abdomen and his chakra-lit fingers press into its centre. The formula is flat opaque "
  "black line-work and ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 5 (bottom middle, close-up, inner world): his hand turns clockwise and his body twists "
  "against the resistance.\n"
  "PANEL 6 (dominant bottom-left panel, inner world): the seal ink LIQUEFIES and runs downward "
  "while flat opaque orange chakra leaks RIGHTWARD through the bars toward the boy. The fox's eye "
  "opens wider at frame LEFT and the boy winces at the LOWER RIGHT. The stonework and the water "
  "stay fully drawn behind the chakra. " + L_SEWER
  + SAY((1, BOY, "upper right", "I WILL WEAKEN THE SEAL."),
        (1, BOY, "upper left", "ZETSU WILL PULL FROM OUTSIDE."),
        (3, BOY, "upper right", "YOU FORCE YOURSELF OUT."))
  + "BALLOON STACK: the two PANEL 1 balloons are one connected stack sharing ONE single visible "
    "tail to the visible boy; the second balloon grows no tail of its own. "
  + SFX(4, "THRUM", "Place it beside his pressing fingers. ")
  + SFX(5, "CRK", "Curve it around the seal formula. ")
  + SFX(6, "HSSSS", "Keep it low and thin, running beside the right-moving chakra. ")
  + "The three sound effects specified above are the only other text on this page. ",
  R("naruto_v4_black", "kurama_inner", "zetsu", "env_inner_sewer"), "low"),

 # ---- Spread 4: the seal calls its maker ---------------------------------------------
 ("p07", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + KURAMA_INNER.format(i=3) + ZOR
  + ONLY(BOY, ZETSU, FOX) + YOUNGER + FLAT + NOEYE + SCRIB + NOBLOOD +
  "FIVE panels. Leaked chakra is connected to the outside pull and the simultaneous strain is made "
  "readable.\n"
  "PANELS 1-3 AND 5 ARE THE PHYSICAL CALDERA: basalt terraces under a flat ash-red sky with active "
  "volcanic vents. PANEL 4 IS THE INNER SEAL WORLD: damp stone, shallow water and the great barred "
  "gate.\n"
  "PANEL 1 (top right, diagonal): SILENT — the boy's physical body pitches LEFT from his knees; the "
  "plant creature catches his shoulders from the LEFT before his head reaches the basalt. No text "
  "in this panel.\n"
  "PANEL 2 (top left, close-up): liquid-black seal formula slides across the boy's pale abdomen "
  "while one flat opaque orange thread pushes through its centre. The formula is ILLEGIBLE "
  "SCRIBBLE.\n"
  "PANEL 3 (middle panel, full width): the plant creature plants its RIGHT palm on the seal, "
  "catches the orange thread and draws it LEFT; its LEFT hand holds a one-handed seal.\n"
  "PANEL 4 (bottom right, inset, inner world): SILENT — the gate bars BOW toward the right as the "
  "fox drives his shoulder into them from the LEFT. The boy braces at the lower right. No text in "
  "this panel.\n"
  "PANEL 5 (dominant bottom-left panel, physical world): the flat opaque orange tether stretches "
  "from the boy at centre-RIGHT to the plant creature's pulling hand at centre-LEFT. The creature "
  "leans left; the boy's body arches right against the force. The basalt, the terraces and the sky "
  "stay fully drawn behind the tether. " + L_ASH
  + SAY((3, ZETSU, "upper left", "I HAVE IT."))
  + SFX(2, "HSSSS", "Place it beside the orange thread. ")
  + SFX(5, "THRUM", "Write it along the length of the tether. ")
  + "The two sound effects specified above are the only other text on this page. ",
  R("naruto_v4_black", "zetsu", "kurama_inner"), "low"),

 ("p08", dict(scene="action", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ZET.format(i=3)
  + ENV_SEWER.format(i=4) + ZOR + ONLY(BOY, FOX, ZETSU) + YOUNGER + FLAT + NOEYE + SCRIB
  + NOBLOOD +
  "FIVE panels. ENTIRELY WITHOUT BALLOONS — the only text anywhere on this page is one sound "
  "effect. He reaches the final lock and the page ends before what stops him is revealed.\n"
  "PANELS 1, 2, 4 AND 5 ARE THE INNER SEAL WORLD (Image 4). PANEL 3 IS THE PHYSICAL CALDERA: basalt "
  "terraces under a flat ash-red sky.\n"
  "PANEL 1 (top right, narrow, inner world): the boy is down on one knee at frame RIGHT, breathing "
  "through the pain. The gate shudders at the left. No text in this panel.\n"
  "PANEL 2 (top left, narrow, inner world): the fox pushes RIGHT again, claws dug into the floor "
  "behind the bars. No text in this panel.\n"
  "PANEL 3 (middle panel, full width, physical world): the plant creature keeps pulling LEFT and "
  "the flat opaque chakra tether is thicker, but NO fox has emerged outside — the caldera holds "
  "only the two of them. The boy's body remains conscious with his eyes shut. No text in this "
  "panel.\n"
  "PANEL 4 (bottom right, medium, inner world): the boy rises to the PAPER SEAL on the gate and "
  "closes his right hand on its lower edge. The fox watches from the left, still pushing. The "
  "paper's markings are ILLEGIBLE SCRIBBLE.\n"
  "PANEL 5 (dominant bottom-left close-up, inner world): AN UNIDENTIFIED MAN'S BARE HAND clamps "
  "around the boy's wrist before the paper comes free. Show ONLY that hand, a PLAIN DARK SLEEVE "
  "cropped above the wrist, the boy's arrested fingers and the half-lifted paper. NO face, NO hair, "
  "NO shoulder, NO coat hem, NO flame pattern, NO vest, NO crest, NO symbol and NO silhouette that "
  "could identify anyone may appear anywhere in this panel. There is no balloon in this panel. "
  + L_SEWER
  + SFX(4, "RRRIP—",
        "Place it beside the lifting corner of the paper. Its trailing dash must run into PANEL 5 "
        "and visually TERMINATE at the gripping hand. This sound effect is the only text anywhere "
        "on this page — no balloons, no captions and no other lettering of any kind. "),
  R("naruto_v4_black", "kurama_inner", "zetsu", "env_inner_sewer"), "low"),

 # ---- Spread 5: the dead keeper of the cage ------------------------------------------
 ("p09", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=4),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + MINATO_PARTIAL.format(i=3)
  + ENV_SEWER.format(i=4) + ONLY(BOY, FOX, MIN) + YOUNGER + INNER + FLAT + NOEYE + SCRIB
  + NOBLOOD +
  "FOUR panels. The hand is identified and all three characters name the relationship "
  "differently.\n"
  "PANEL 1 (large upper panel, NO MORE THAN 45% OF THE PAGE HEIGHT — it must read as clearly "
  "SMALLER than the dominant panel on the freedom page later in this chapter): the previously "
  "unidentified hand is now the blond man's. He stands at centre-RIGHT holding the boy's wrist and "
  "has pushed him DOWN-RIGHT, away from the paper seal. The fox remains behind the CLOSED gate at "
  "frame LEFT and has stopped pushing in order to glare RIGHT at the man.\n"
  "PANEL 2 (bottom right, close-up): the boy looks up-right at the man with surprise already "
  "controlled. The man remains visible at the panel's LEFT edge and visibly WINCES the moment the "
  "boy uses his name.\n"
  "PANEL 3 (bottom middle, close-up): the fox's muzzle presses near the bars, eye-line hard RIGHT.\n"
  "PANEL 4 (bottom left, close-up): the fox bares his teeth. " + L_SEWER
  + SAY((1, FOX, "high upper left", "YONDAIME."),
        (1, MIN, "upper right, set LOWER on the page than the upper-left balloon", "NARUTO?"),
        (2, BOY, "upper right", "HELLO, MINATO."),
        (3, FOX, "upper left", "COME CLOSER."),
        (4, FOX, "upper left", "I WILL TEAR YOU APART."))
  + "In PANEL 1 the fox's balloon is placed HIGHER on the page than the blond man's so that it "
    "reads first. Each carries ONE short local visible tail — the fox's threads through the bars "
    "nearest it, the man's runs a short distance to him — and neither tail crosses the panel or "
    "the other balloon. ",
  R("naruto_v4_black", "kurama_inner", "minato_kushina", "env_inner_sewer"), "medium"),

 ("p10", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + MINATO_PARTIAL.format(i=3)
  + ENV_SEWER.format(i=4) + ONLY(BOY, FOX, MIN) + YOUNGER + INNER + FLAT + NOEYE + SCRIB
  + NOBLOOD +
  "SIX panels. The interruption ends without expanding into a later conversation.\n"
  "PANEL 1 (top right, two-shot): the blond man releases the boy's wrist. The two face one another "
  "on the RIGHT side of the cage axis; the man looks down-left, the boy up-right.\n"
  "PANEL 2 (top left, close-up): the boy stands.\n"
  "PANEL 3 (middle panel, full width): the man steps LEFT to block the boy's path back to the "
  "paper; the bars remain behind him and the gate stays closed.\n"
  "PANEL 4 (bottom right, medium): the boy steps inside the man's reach and places his open right "
  "palm flat against the man's chest.\n"
  "PANEL 5 (bottom middle, close-up): the man looks at the boy; the boy's hand begins to emit a "
  "FLAT, hard-edged outward pulse — an opaque ring shape with a black outline, not a glow.\n"
  "PANEL 6 (dominant bottom-left panel): the boy drives the pulse LEFT through the man, who "
  "dissolves into flat pale fragments. NO body, NO soul, NO skeleton and NO corpse remains. The fox "
  "watches through the bars behind the fragments. " + L_SEWER
  + SAY((1, MIN, "upper right", "WHY ARE YOU BREAKING THE SEAL?"),
        (2, BOY, "upper right", "IT DOES NOT CONCERN YOU."),
        (3, MIN, "upper right", "I CAN'T LET YOU FREE THE NINE-TAILS."),
        (3, MIN, "upper left", "IT'S DANGEROUS—"),
        (4, BOY, "upper right", "YOU ARE CHAKRA LEFT INSIDE A SEAL."),
        (5, BOY, "upper right", "YOU ARE DEAD."),
        (5, BOY, "upper left", "YOUR ROLE IS FINISHED."),
        (6, BOY, "upper right", "DISAPPEAR, MINATO."))
  + "BALLOON STACKS: the two PANEL 3 balloons are one connected stack sharing ONE visible tail to "
    "the blond man; the two PANEL 5 balloons are one connected stack sharing ONE visible tail to "
    "the boy. Continuation balloons grow no tails of their own. "
  + SFX(6, "FSHH", "Place it among the dissolving pale fragments. "),
  R("naruto_v4_black", "kurama_inner", "minato_kushina", "env_inner_sewer"), "low"),

 # ---- Spread 6: the cage opens, the body fails ---------------------------------------
 ("p11", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEWER.format(i=3)
  + ONLY(BOY, FOX) + YOUNGER + FLAT + NOEYE + SCRIB + NOBLOOD +
  "SIX panels. The seal opens and the fox alone decides whether the boy survives.\n"
  "THIS PAGE IS THE INNER SEAL SPACE, but the great gate OPENS during it: from PANEL 2 onward the "
  "two barred doors swing apart and the threshold between them is empty.\n"
  "PANEL 1 (top right, close-up): the boy's hand returns to the half-lifted paper seal and TEARS IT "
  "FULLY AWAY to the RIGHT. The paper's markings are ILLEGIBLE SCRIBBLE.\n"
  "PANEL 2 (top left, wide): the gate lock releases and the two barred doors begin opening away "
  "from the centre. The fox stands on the LEFT side of the threshold, NOT yet crossing it.\n"
  "PANEL 3 (middle right, medium): the boy at frame RIGHT faces left across the now-open threshold. "
  "He makes NO hand seal and activates NO eye pattern.\n"
  "PANEL 4 (middle left, close-up): the fox studies him without answering. THE BOY IS NOT DRAWN IN "
  "THIS PANEL.\n"
  "PANEL 5 (bottom right, medium): the boy turns RIGHT toward the inner-world exit, deliberately "
  "giving the fox his back.\n"
  "PANEL 6 (dominant bottom-left panel): the boy recedes toward the right-side darkness while the "
  "fox fills the OPEN gateway at the left. " + L_SEWER
  + SAY((3, BOY, "upper right", "LEAVE SOME CHAKRA BEHIND."),
        (4, OFF(BOY), "upper right", "WITHOUT IT, YOUR EXTRACTION MAY KILL ME."),
        (5, BOY, "upper right", "WHEN YOU ARE FREE, I WILL BE UNABLE TO STOP YOU."),
        (6, BOY, "upper right", "IF YOU TRY ANYTHING, I WILL MAKE YOU REGRET IT."))
  + "The PANEL 4 off-panel tail enters from that panel's RIGHT border and stops there; it must not "
    "touch or aim at the fox's face, which fills that panel. "
  + SFX(1, "RIP", "Place it beside the tearing paper. ")
  + SFX(2, "KLANG", "Write it across the separating bars. ")
  + SFX(6, "HNF",
        "Place it low beside the fox's muzzle with NO balloon around it — it is a bare hand-"
        "lettered sound, not speech. "),
  R("naruto_v4_black", "kurama_inner", "env_inner_sewer"), "low"),

 ("p12", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + KURAMA_INNER.format(i=3)
  + KURAMA_FULL.format(i=4) + ZOR + ONLY(BOY, ZETSU, FOX) + YOUNGER + FLAT + NOEYE + SCRIB
  + NOBLOOD +
  "FIVE panels. The physical cost lands immediately and cause stays ahead of result.\n"
  "PANELS 1, 2, 4 AND 5 ARE THE PHYSICAL CALDERA: basalt terraces under a flat ash-red sky. PANEL 3 "
  "IS THE INNER SEAL WORLD, where the gate now stands open.\n"
  "PANEL 1 (top right, close-up): in the caldera, the seal formula ERUPTS from the boy's abdomen "
  "and crawls across his torso as flat opaque black line-work, ILLEGIBLE SCRIBBLE throughout. The "
  "creature's chakra tether stays taut to the LEFT.\n"
  "PANEL 2 (top left, tall panel): the boy's body LIFTS above the basalt, back arched and skin "
  "losing colour. The plant creature braces below-left and keeps pulling. No wound and no blood "
  "appears anywhere on him.\n"
  "PANEL 3 (middle right, inset, inner world): SILENT — the fox crosses the OPEN gate from LEFT to "
  "RIGHT as his chakra streams out of frame toward the physical world. Use Image 3 for this "
  "behind-the-gate form. No text in this panel.\n"
  "PANEL 4 (middle left, close-up): the plant creature's feet skid LEFT through ash, but its "
  "one-handed seal does not break.\n"
  "PANEL 5 (dominant bottom panel): SILENT — a VAST, INCOMPLETE orange silhouette builds on the "
  "LEFT side of the caldera. Use Image 4 only as the shape of the nine-tailed fox, and draw it as a "
  "FLAT OPAQUE unfinished silhouette with a hard outline — no face detail, no complete body and no "
  "glow. The boy hangs at centre-RIGHT inside the seal formula; the plant creature remains between "
  "them, drawing the tether left. THE FOX IS NOT YET FULLY EXTRACTED and must not read as a "
  "finished body. The basalt and sky stay fully drawn behind it. No text in this panel. " + L_ASH
  + SAY((2, BOY, "centred high", "AAAGH—!"),
        (4, ZETSU, "upper left", "IT IS MOVING."))
  + SFX(1, "VRRRM", "Place it around the erupting formula. "),
  R("naruto_v4_black", "zetsu", "kurama_inner", "kurama_full"), "medium"),

 # ---- Spread 7: the fox's first free choice ------------------------------------------
 ("p13", dict(scene="action", light="day", cast="two", mood="somber", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + KURAMA_FULL.format(i=3) + ZOR
  + ONLY(BOY, ZETSU,
         "the enormous nine-tailed fox, which stays an INCOMPLETE silhouette in panels 1-5 and is "
         "deliberately cropped and occluded in panel 6 — its whole body is never visible on this "
         "page") + YOUNGER + DRAGON + FLAT + NOEYE + SCRIB + NOBLOOD +
  "SIX panels. The extraction's duration and danger are given visible weight. The only text on this "
  "page is one caption and one sound effect.\n"
  "AXIS LOCK: the fox mass occupies the LEFT, the plant creature pulls at centre-LEFT, and the "
  "boy hangs at centre-RIGHT. This never flips.\n"
  "PANEL 1 (top right, wide): SILENT — repeat the caldera axis exactly. The sun is high; the "
  "incomplete orange fox silhouette occupies the left, the creature pulls at centre-left and the "
  "boy hangs at centre-right. No text in this panel.\n"
  "PANEL 2 (top left, wide): the SAME locked camera angle much later — the light has moved and the "
  "ash shadows are far longer. The fox's head and shoulders are now SOLID, but the rest of him is "
  "still an unfinished silhouette.\n"
  "PANEL 3 (middle right, close-up): SILENT — the boy's face is bloodless, eyes barely open, breath "
  "shallow. No wound and no blood. No text in this panel.\n"
  "PANEL 4 (middle left, close-up): SILENT — the plant creature's pulling arm shakes; its joined "
  "black-and-white face stays fixed on the tether. No text in this panel.\n"
  "PANEL 5 (bottom right, tall panel): the fox's last trailing chakra thread TEARS FREE of the "
  "boy's abdomen toward the LEFT as a flat opaque shape. The boy begins falling down-right. No "
  "wound is left behind and no blood appears.\n"
  "PANEL 6 (bottom left): SILENT — the extraction completes. The plant creature releases the empty "
  "tether and lunges RIGHT to catch the boy. At the FAR LEFT the now-physical fox is deliberately "
  "CROPPED by the panel edge and OCCLUDED by foreground basalt and settling chakra: show only "
  "partial legs and a few tail arcs, never an unobstructed body and never his full face. No text in "
  "this panel. " + L_ASH
  + CAP(2, "upper right", "ONE HOUR LATER...")
  + SFX(5, "SNAP",
        "Write it along the separating chakra thread. The caption box and this sound effect are the "
        "only text anywhere on this page — no balloons and no other lettering of any kind. "),
  R("naruto_v4_black", "zetsu", "kurama_full"), "low"),

 ("p14", dict(scene="establishing", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + KURAMA_FULL.format(i=1) + N16_BLACK.format(i=2) + ZET.format(i=3) + ZOR
  + ONLY(FOX, BOY, ZETSU) + YOUNGER + DRAGON + FLAT + NOEYE + NOBLOOD +
  "FIVE panels. The fox is given a genuine opportunity to betray the boy and visibly chooses not "
  "to.\n"
  "PANEL 1 (DOMINANT UPPER TWO-THIRDS OF THE PAGE — this is the LARGEST PANEL IN THE ENTIRE CHAPTER "
  "and must read as unmistakably larger than every other panel in it): for the FIRST time the "
  "enormous nine-tailed fox's ENTIRE UNOBSTRUCTED PHYSICAL BODY is visible at frame LEFT, fully "
  "free, with all NINE tails spread into open ash-red sky. There is NO gate, NO bar, NO chain, NO "
  "seal, NO foreground crop and NO chakra haze anywhere over him. The plant creature kneels at "
  "centre-RIGHT over the collapsed, chalk-pale boy. The fox looks DOWN-RIGHT at the boy. He is the "
  "half that was sealed and must not be described or drawn as complete.\n"
  "PANEL 2 (lower right, close-up): SILENT — the fox's eye stays fixed on the helpless boy. No text "
  "in this panel.\n"
  "PANEL 3 (lower middle, close-up): SILENT — one immense claw LIFTS and angles down-right toward "
  "the boy. No text in this panel.\n"
  "PANEL 4 (small inset overlapping the raised claw, lower left): a MEMORY IMAGE, drawn hard-edged "
  "and desaturated — the boy walking away from the barred cage, seen from behind. It is a remembered "
  "image only and does not belong to the caldera.\n"
  "PANEL 5 (bottom strip, full width): SILENT — the fox LOWERS the claw back to the ground at the "
  "LEFT. At the RIGHT, the plant creature lifts the boy and disappears farther right into a narrow "
  "basalt fissure; the beast makes no move to stop him. No text in this panel. " + L_ASH
  + SFX(1, "WHUMM", "Keep it small, low in the settling chakra at the fox's feet. ")
  + 'LETTERING: in PANEL 4 draw ONE pale memory-echo balloon with a soft broken outline and NO TAIL '
    'OF ANY KIND, containing only the words: "YOU WILL STILL HAVE YOUR FREEDOM." It belongs to no '
    'one in the present scene, must not point at anyone, and is the only balloon on this page. '
    'That echo balloon and the one sound effect specified above are the only text anywhere on this '
    'page. ',
  R("kurama_full", "naruto_v4_black", "zetsu"), "high"),

 # ---- Spread 8: what the fox left behind ---------------------------------------------
 ("p15", dict(scene="dialogue", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2)
  + ONLY(BOY, WZ, BZ) + YOUNGER + FLAT + NOEYE + NOBLOOD +
  "SIX panels. Two separate reasons the boy has a chance to live, without any instant recovery.\n"
  "THIS PAGE IS INSIDE A NARROW SHELTERED BASALT FISSURE: dark rock walls close on both sides, no "
  "sky, no volcano and no caldera view.\n"
  "THE PLANT CREATURE SPLITS ON THIS PAGE. From PANEL 2 onward it is TWO separate figures taken "
  "from the same reference: a WHITE figure and a BLACK figure. Before the split, and whenever they "
  "are joined, its WHITE half is on the viewer's LEFT and its BLACK half on the viewer's RIGHT.\n"
  "PANEL 1 (top right, wide): SILENT — inside the fissure, the still-joined plant creature lowers "
  "the boy at centre. He is limp and chalk-pale. There is NO medical equipment, NO bandage and no "
  "other person present. No text in this panel.\n"
  "PANEL 2 (top left, medium): the WHITE half separates away to the RIGHT while the BLACK half "
  "peels LEFT toward the boy's torso. Both are now distinct full figures.\n"
  "PANEL 3 (middle panel, full width): the BLACK figure flows over and INTO the boy's body, taking "
  "control only to keep its failing systems working. The WHITE figure watches from the RIGHT and "
  "stays fully visible.\n"
  "PANEL 4 (bottom right, close-up): flat opaque black markings settle across the boy's chest and "
  "neck, and a weak pulse returns beneath them.\n"
  "PANEL 5 (dominant bottom-middle cutaway panel, the focal panel): a cutaway INSIDE the boy's "
  "chakra pathways — thin flat orange chakra circulates through his own dim chakra lines. It is "
  "ALREADY present: no seal, no eye effect, no command mark and no visible action by anyone "
  "installs it.\n"
  "PANEL 6 (bottom left, close-up): the boy remains unconscious, but the next pulse is firmer. "
  + L_FISSURE
  + SAY((2, WZ, "upper right", "HE MAY NOT SURVIVE."),
        (3, BZ, "upper left", "I WILL SUSTAIN HIM."))
  + 'LETTERING: in PANEL 5, draw ONE thought balloon in the LOWER RIGHT with a soft cloud edge and '
    'NO TAIL, belonging to the black figure, reading: "THE KYŪBI LEFT CHAKRA IN HIS PATHWAYS." '
  + SFX(4, "THUM", "Place it beside the boy's chest. ")
  + SFX(6, "THUM", "Place it beside the boy's chest, matching the panel 4 lettering. "),
  R("naruto_v4_black", "zetsu"), "medium"),

 ("p16", dict(scene="dialogue", light="dark", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(BOY, ZETSU, BZ) + YOUNGER + FLAT + NOEYE + NOBLOOD +
  "SIX panels. The multi-day recovery and his still-incomplete condition are preserved.\n"
  "THIS PAGE IS INSIDE THE SAME NARROW BASALT FISSURE: dark rock walls, no sky and no caldera "
  "view.\n"
  "PANEL 1 (top right, wide): the same fissure a few days later. The boy is still unconscious at "
  "centre with his colour partly returned. The BLACK figure PEELS OUT of him and rejoins the WHITE "
  "figure before the boy wakes, so the creature is joined again by the end of the panel.\n"
  "PANEL 2 (top left, medium): the next day. The joined plant creature is ALREADY fully outside the "
  "boy, seated at the LEFT, when the boy's eyes open at centre-right. NO dialogue in this panel.\n"
  "PANEL 3 (middle right, close-up): the boy pushes himself upright with one hand and forms a small "
  "test seal with the other; BOTH arms shake.\n"
  "PANEL 4 (middle left, two-shot): the plant creature faces RIGHT toward him.\n"
  "PANEL 5 (bottom right, medium): the boy kneels into a reverse-summoning seal, facing LEFT toward "
  "the caldera he means to return to. He is still pale and unsteady.\n"
  "PANEL 6 (dominant bottom-left panel): flat opaque summoning smoke pulls the boy LEFT out of the "
  "fissure; the plant creature remains at the RIGHT edge. " + L_FISSURE
  + CAP(1, "upper right", "A FEW DAYS LATER.")
  + CAP(2, "upper right", "THE NEXT DAY.")
  + SAY((1, BZ, "upper left", "HE IS STABLE."),
        (3, BOY, "upper right", "I CAN MOLD CHAKRA."),
        (4, ZETSU, "upper left", "YOU HAVE NOT RECOVERED."),
        (5, BOY, "upper right", "I DO NOT NEED TO."))
  + SFX(6, "FWOOM", "Embed it inside the summoning smoke. ")
  + "The two caption boxes and the one sound effect specified above are the only other text on this "
    "page. ",
  R("naruto_v4_black", "zetsu"), "low"),

 # ---- Spread 9: terms between equals -------------------------------------------------
 ("p17", dict(scene="establishing", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + KURAMA_FULL.format(i=1) + N16_BLACK.format(i=2)
  + ONLY(FOX, BOY) + YOUNGER + DRAGON + FLAT + NOEYE + NOBLOOD +
  "SIX panels. The absence of the cage does the visual work before the question is asked. THERE ARE "
  "NO BARS, NO GATE AND NO SEAL ANYWHERE ON THIS PAGE.\n"
  "PANEL 1 (top band, full width, half the page height): open caldera. The enormous nine-tailed fox "
  "rests FREELY at frame LEFT with open ash-red sky behind his spread tails; the boy appears out of "
  "flat opaque summoning smoke at the FAR RIGHT, still pale and unsteady. SILENT — no text in this "
  "panel.\n"
  "PANEL 2 (middle right, close-up): SILENT — the fox opens one eye toward the right. No text in "
  "this panel.\n"
  "PANEL 3 (middle left, wide): the boy walks LEFT but stops well OUTSIDE the fox's reach, keeping "
  "clear open ground between them.\n"
  "PANEL 4 (bottom right, close-up): the fox's head remains on his paws.\n"
  "PANEL 5 (bottom middle, medium): the boy stands without smiling, eye-line left.\n"
  "PANEL 6 (bottom left, close-up): the fox's eye fills the panel, aimed right. " + L_ASH
  + SAY((3, BOY, "upper right", "HOW DOES IT FEEL TO BE FREE?"),
        (4, FOX, "upper left", "GOOD."),
        (5, BOY, "upper right", "DO YOU TRUST ME?"),
        (6, FOX, "upper left", "NO."))
  + "The fox's balloons use the same lettering font as everyone else's with a slightly rough "
    "balloon outline; they stay fully legible and are never drawn as decorative monster text. ",
  R("kurama_full", "naruto_v4_black"), "medium"),

 ("p18", dict(scene="dialogue", light="day", cast="crowd", mood="tense", panels=5),
  FILL + RTL + KURAMA_FULL.format(i=1) + N16_BLACK.format(i=2) + N16_SWORD.format(i=3)
  + JIR.format(i=4) + KAK.format(i=5) + SASUKE16.format(i=6) + YUGAO_V4.format(i=7)
  + ENV_STREET.format(i=8)
  + ONLY(FOX, BOY, BOY16, SAGE, MAN, SAS16, YUG) + YOUNGER + NOW + FLAT + NOEYE + NOBLOOD +
  "FIVE panels. LAST PAGE OF THE CHAPTER — the flashback ends on equality and the present-day "
  "conversation closes without sharing its cause.\n"
  "PANELS 1-3 ARE THE FLASHBACK CALDERA: open basalt under an ash-red sky, with NO bars, NO gate "
  "and NO seal. PANELS 4-5 ARE PRESENT-DAY KIRI (Image 8). The two blond figures are DIFFERENT AGES "
  "and never share a panel: the younger boy appears only in PANELS 1-3, the armoured "
  "sixteen-year-old only in PANELS 4-5.\n"
  "PANEL 1 (top right, close-up): SILENT — the boy absorbs the refusal with no change in posture or "
  "gaze. No text in this panel.\n"
  "PANEL 2 (dominant centre panel, the emotional focal panel — but drawn CLEARLY SMALLER than the "
  "freedom panel earlier in this chapter): the enormous nine-tailed fox raises his head against "
  "completely open sky at frame LEFT; the boy stands small at the LOWER RIGHT.\n"
  "PANEL 3 (lower right, medium): the boy holds the fox's eye-line across the open ground.\n"
  "PANEL 4 (lower middle strip, neutral OVERHEAD re-establishing shot, present day): reset the Kiri "
  "geography rather than repeating this chapter's opening axis — the armoured teen now stands ALONE "
  "on the LEFT facing the group on the RIGHT, with the big white-haired man nearest him and the "
  "masked silver-haired man, the older dark-haired teen and the purple-haired kunoichi behind that "
  "man. His gunbai stays on his back and the sash sword stays at his left hip; if the overhead crop "
  "hides the hip, THE CAMERA IS MERELY HIDING THE SWORD — it has not been removed.\n"
  "PANEL 5 (bottom left, narrow panel, present day): the armoured teen's afterimage exits LEFT, "
  "leaving the group at the RIGHT. The white-haired man's eye-line follows left; the others remain "
  "still. SILENT except for one sound effect. " + L_KIRI
  + SAY((2, FOX, "upper right", "BUT I CAN WORK WITH YOU."),
        (2, FOX, "upper middle", "I WILL NOT BECOME YOUR PET."),
        (2, FOX, "upper left", "AND I WILL NOT DO ANYTHING I DO NOT CHOOSE."),
        (3, BOY, "upper right", "THAT IS FINE."),
        (4, BOY16, "upper left", "THAT DOES NOT CONCERN YOU."))
  + "BALLOON STACK: the THREE PANEL 2 balloons are one connected stack sharing ONE single visible "
    "tail to the fox; the second and third balloons inherit that one tail and grow no tails of "
    "their own. The PANEL 4 balloon is local to the armoured teen at frame LEFT and carries one "
    "short visible tail to him; it must not reach across toward the group at the right. "
  + SFX(5, "FSHH", "Keep it small, at the left vanishing edge. "),
  R("kurama_full", "naruto_v4_black", "naruto_v4_armor_sword", "jiraiya", "kakashi",
    "sasuke_16", "yugao_v4", "env_mizukage_tower"), "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch04" / "raw", HERE / "v5ch04" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
