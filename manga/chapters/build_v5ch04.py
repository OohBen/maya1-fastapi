"""Volume 5, Chapter 4 — "The Open Cage". 18 pages.

Source: fic ch12:395-515. Translated 1:1 from story/volume_05/drafts/ch04_the_open_cage.md —
67 spoken/pain-cry balloons, one thought balloon, five captions, one chapter marker, 18 sound
effects and one untailed memory echo across 18 pages. Reading order is RIGHT TO LEFT per the
approved `name`; every page states it.

Page 1 panels 1-2 and page 18 panels 4-5 are the present-day Kiri frame. Everything between
them is a READER-ONLY FLASHBACK about one year after Naruto left Konoha — it is editorial
framing, not a memory Naruto experiences, so no thought cue, no ripple border and no dream
haze marks the cut. Flashback Naruto is the YOUNGER training-period boy in dark layers;
present-day Naruto is the sixteen-year-old in repaired red armour. They are drawn as two
different figures and never share a panel.

This builder must match the `name`, not improve on it. Every balloon below is the draft's
exact final text, in the draft's exact panel and position.

Reference gaps recorded for the owner (never invented here):
  * There is NO reference plate for the Ancient Land of Dragons — no volcanic wilderness,
    basalt terrace, caldera or fissure sheet exists in refs/images. Pages 5, 7, 8 (physical
    half), 12-17 and page 18 panels 1-3 therefore carry it as written description only, the
    same way v5ch07 handled the cast without sheets.
  * There is NO single-figure minato.png. Pages 8-10 bind him from the LEFT-HAND figure of the
    two-person minato_kushina.png, with the red-haired woman excluded by name.
  * There is NO approved younger-training-period Naruto sheet, so naruto_13.png carries the
    flashback boy, exactly as in v5ch05 and v5ch06.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import (CAP, FILL, JIR, KAK, MAN, N13, OFF, ONLY, R, SAGE, SAY,  # noqa: E402
                     SFX, ZET)
from prompts_v4 import (KURAMA_FULL, KURAMA_INNER, KURAMA_SPEAKER, N16_SWORD,  # noqa: E402
                        N16_SPEAKER, SASUKE16, SASUKE16_SPEAKER, THOUGHT,
                        YUGAO_V4, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")

# ---------------------------------------------------------------- names used in balloon tails
BOY16 = N16_SPEAKER
BOY13 = "the younger long-haired blond boy in the black shirt with the red spiral"
KURAMA = KURAMA_SPEAKER
MIN = "the tall blond man in the white flame-hemmed coat"
YUG = YUGAO_V4_SPEAKER
SAS16 = SASUKE16_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZWHITE = "the chalk-white half of the plant creature"
ZBLACK = "the pure black half of the plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")

# There is no single-figure Minato sheet in refs/images; the two-person parents sheet is the only
# source of his exact hair, coat and uniform, so the red-haired half is excluded by name.
MINATO = (
    "Image {i} is a TWO-PERSON REFERENCE SHEET. Use ONLY THE LEFT-HAND FIGURE and COMPLETELY "
    "IGNORE the red-haired woman on its right — she does not appear anywhere in this chapter. That "
    "left-hand figure is the CHARACTER REFERENCE for the tall blond man: spiky bright yellow-blond "
    "hair with two long jaw-length bangs, blue eyes, a Leaf forehead protector, a dark navy "
    "long-sleeved uniform under a green flak vest, and a white short-sleeved full-length coat with "
    "a red flame pattern licking up its hem. Reproduce his face, hair and outfit exactly; ignore "
    "the sheet's white background, its lineup layout and its neutral standing pose. ")

# Page 8 shows the same man as an unidentified hand only, so the sheet is deliberately starved.
MINATO_HAND = (
    "Image {i} is a TWO-PERSON REFERENCE SHEET, and on THIS page almost nothing is taken from it. "
    "Use ONLY the LEFT-HAND figure's adult male hand and the plain dark navy sleeve on his "
    "forearm. COMPLETELY IGNORE the red-haired woman on the sheet's right, and completely ignore "
    "the blond man's face, hair, eyes, forehead protector, flak vest, white flame-hemmed coat and "
    "every cuff band or stripe. NO face, NO head, NO hair, NO shoulder, NO body, NO silhouette, NO "
    "crest and NO symbol belonging to him may be visible anywhere on this page — he must remain "
    "completely unidentifiable. Ignore the sheet's white background and its lineup layout. ")

# ---------------------------------------------------------------- locations
ENV_KIRI = ("Image {i} is the LOCATION REFERENCE for the rebuilt Kiri street — reuse its "
            "architecture, wet stone, colour palette and mist-filtered daylight. Do not copy its "
            "camera angle; ignore that it is empty of people. ")
ENV_SEAL = ("Image {i} is the LOCATION REFERENCE for the inner seal space — reuse its damp "
            "stonework, huge scale, ankle-deep black standing water and colour palette. Do not "
            "copy its camera angle; ignore that it is empty of people. ")

# Dragon Land has NO reference plate anywhere in refs/images. It is written out in full instead.
DRAGON = ("THE ANCIENT LAND OF DRAGONS HAS NO REFERENCE PLATE and must be drawn from this "
          "description alone, identically on every page that uses it: a Fire-Country-style forested "
          "wilderness torn open by ACTIVE VOLCANIC VENTS — stepped black basalt terraces descending "
          "from reader-RIGHT down to reader-LEFT into a wide shallow caldera, drifting pale ash, "
          "low sulphur steam at the vents, scattered scorched conifers on the high ground, and a "
          "flat ash-red sky. There is no village, no road, no building, no banner and no signpost "
          "anywhere in it. ")
FISSURE = ("The shelter is a narrow sheltering fissure in the basalt: sheer dark rock walls close "
           "on both sides, a strip of ash-red sky far above, dry ash on the floor. There is no "
           "bedding, no lamp, no fire, no medical equipment and no other person of any kind. ")

# ---------------------------------------------------------------- continuity locks
FB = ("The blond boy on this page is the YOUNGER, PRE-KIRI TRAINING-PERIOD version: visibly "
      "younger, shorter and slighter than the sixteen-year-old of the present day, wearing ONLY "
      "his dark training layers — the black high-neck long-sleeved shirt with the large red spiral "
      "and black trousers. He carries NO red armour, NO gunbai, NO sword and NO forehead protector "
      "anywhere on this page. Wherever his visible left eye is drawn open it carries the ORDINARY "
      "THREE-TOMOE SHARINGAN — a red iris with three small black comma marks — instead of the "
      "reference sheet's blue eye, and NEVER a six-bladed pattern. His right eye stays hidden "
      "behind his long right bang. ")
GEAR = ("Present-day equipment, fixed: clean fully repaired red plate armour, the dark purple "
        "gunbai with its chain carried on his back, and a PLAIN straight sword in a dark sash "
        "sheath at his left hip — an ordinary undecorated sword, NOT the lost Volume 3 ninjato. If "
        "the camera crop hides the hip, the camera is merely hiding the sword; he remains equipped "
        "with it and it is never removed. His visible left eye carries the ORDINARY three-tomoe "
        "Sharingan, three small black comma marks on a red iris, with NO six-bladed pattern "
        "anywhere. ")
AXIS_IN = ("INNER-SEAL AXIS, LOCKED: the boy stays on the reader's RIGHT, looking and moving LEFT "
           "toward the gate; the fox stays on the reader's LEFT behind the bars, looking RIGHT. Do "
           "not flip, mirror or swap this axis in any panel. ")
AXIS_OUT = ("PHYSICAL AXIS, LOCKED: the boy's body is at centre-RIGHT, the plant creature works to "
            "his LEFT, and every chakra pull, tether and escaping shape travels RIGHT-TO-LEFT with "
            "the reading direction. ")
CAGE = ("The cage is a colossal barred gate of dark iron reaching out of frame, with a single "
        "paper seal tag pasted across the join of its two doors. Every marking on that tag, and "
        "every seal glyph anywhere on the page, is ILLEGIBLE SCRIBBLE and not readable words. ")
FLAT = ("ALL chakra, seal-formula and summoning effects on this page are FLAT OPAQUE SHAPES with "
        "hard black outlines — solid orange chakra, solid black seal ink, solid pale fragments, "
        "solid white smoke. They do NOT glow, do NOT bloom, do NOT emit light, do NOT go "
        "translucent and do NOT wash out or bleach anything behind them. Every figure, every bar, "
        "every rock face and the whole environment stay fully drawn, fully coloured and completely "
        "legible through and around them. ")
NOHARM = ("This page shows physical strain and exhaustion only: no injury detail, no wounds, no "
          "blood and no gore anywhere on it. ")
NOCONTROL = ("NO eye-control effect appears anywhere on this page: no Sharingan reflected in the "
             "fox's eyes, no genjutsu rings, no hypnotic spirals and no line of force running from "
             "the boy's gaze. The only tether that may ever be drawn is chakra physically pulled "
             "through the seal. ")
FOXTALK = ("The fox's balloons use the SAME clean upright lettering as every human balloon, inside "
           "an ordinary balloon whose outline is only slightly rougher. Never draw his words as "
           "jagged, dripping, decorative or monstrous display text, and never make them less "
           "legible than anyone else's. ")
HALF = ("The fox is the half sealed away by the blond man — never captioned, labelled or marked as "
        "complete, and no second fox appears anywhere. ")
ONLYTEXT = ("The balloons, caption boxes, chapter marker, echo and sound effects listed above are "
            "the COMPLETE text of this page. Write no other words, numbers, signs or signatures "
            "anywhere on it, and render any writing on seal paper, seal formula, rock or "
            "scaffolding as ILLEGIBLE SCRIBBLE rather than readable words. ")

L_KIRI = "Lighting: clean pale mist-filtered daylight over a rebuilding village, the fog thin and high. "
L_SEAL = ("Lighting: dim cold blue-grey light off ankle-deep black reflective water inside a vast "
          "windowless stone space; no sky, no horizon, no weather and no exterior shadows. ")
L_DRAGON = ("Lighting: flat hard light under a low ash-red sky, pale ash haze, dull grey-black "
            "basalt, long soft shadows lying to the left. ")
L_FISSURE = ("Lighting: a single narrow band of ash-red daylight falling from far above into a deep "
             "dark rock cleft; everything else in cool shadow. ")


def CONNECT(panel, balloons, speaker):
    """Draft rule: a connected stack carries exactly one shared visible tail."""
    return (f'CONNECTED BALLOON STACK: in PANEL {panel}, the balloons reading {balloons} are ONE '
            f'connected stack — their outlines touch, they read in the listed order, and the whole '
            f'stack has EXACTLY ONE visible tail, which leaves the FIRST balloon of the stack and '
            f'points at {speaker}. The continuation balloons inherit that single shared tail and '
            f'must never grow tails of their own. ')


def ECHO(panel, where, text):
    """An untailed pale memory echo — not a speech balloon and not a thought balloon."""
    return (f'MEMORY ECHO: in PANEL {panel}, in the {where}, draw a PALE echo balloon with a soft '
            f'broken outline and faded grey lettering, containing only the words: "{text}". It has '
            f'NO TAIL of any kind, points at nobody, and is not a speech balloon. ')


PAGES = [
 # ---- Spread 1: the answer Jiraiya does not receive ---------------------------------
 ("p01", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=4),
  FILL + RTL + N16_SWORD.format(i=1) + JIR.format(i=2) + KAK.format(i=3) + SASUKE16.format(i=4)
  + YUGAO_V4.format(i=5) + ENV_KIRI.format(i=6) + N13.format(i=7) + KURAMA_INNER.format(i=8)
  + ENV_SEAL.format(i=9)
  + ONLY(BOY16, SAGE, MAN, SAS16, YUG,
         BOY13 + ", who is a SEPARATE, YOUNGER figure appearing ONLY in panels 3 and 4 and never "
         "in the present-day street",
         "the enormous nine-tailed fox, appearing ONLY in panel 4")
  + GEAR + FB + CAGE + AXIS_IN + FOXTALK + HALF + NOCONTROL +
  "FOUR panels. PANELS 1-2 ARE THE PRESENT DAY in Kiri (Image 6). PANELS 3-4 ARE A READER-ONLY "
  "FLASHBACK about one year earlier, inside the inner seal space (Image 9). The cut between them "
  "is an EDITORIAL MATCH CUT, not a memory: no ripple border, no soft haze, no thought bubble and "
  "no dream cue may mark it. The older armoured teen and the younger boy are two different figures "
  "and must NEVER appear in the same panel.\n"
  "PANEL 1 (shallow horizontal strip across the top, full width): present-day Kiri street. The "
  "sixteen-year-old in repaired red armour stands at reader-RIGHT facing LEFT. The big white-haired "
  "man is a soft out-of-focus foreground shoulder and jaw at reader-LEFT, facing right. The masked "
  "silver-haired man, the older dark-haired teen and the purple-haired kunoichi stay small behind "
  "him on the left. The teen's eye-line meets the white-haired man's and he gives no answer; his "
  "mouth stays closed. No text in this panel.\n"
  "PANEL 2 (narrow close-up, upper left): the armoured teen's ORDINARY three-tomoe Sharingan fills "
  "the panel — a red iris with three small black comma marks and nothing else. The black pupil "
  "opens out at the panel's LEFT edge into the black mouth of a flooded stone tunnel. No text in "
  "this panel.\n"
  "PANEL 3 (middle band, full width): the inner seal space. The YOUNGER blond boy in dark training "
  "layers enters from the RIGHT and walks LEFT through ankle-deep black water, his reflection "
  "leading the eye toward the unseen cage off the left edge. The UPPER LEFT of this panel is a "
  "protected rectangle of clean dark wall — no figure, ripple, effect, balloon or tail may enter "
  "it — and it carries only the chapter marker.\n"
  "PANEL 4 (dominant bottom panel): the barred gate spans the LEFT two-thirds of the frame. The "
  "enormous nine-tailed fox lies behind it with his head down on his paws, facing RIGHT. The "
  "younger boy stops small at lower-RIGHT, facing LEFT. " + L_SEAL
  + 'LETTERING: in the protected upper-left area of PANEL 3, write the chapter marker in bold '
    'upright English capitals on one line: "CHAPTER 4 — THE OPEN CAGE". It is a tail-less title, '
    'not a balloon, and nothing overlaps it. '
  + CAP(3, "small box in the upper right", "ABOUT ONE YEAR AFTER NARUTO LEFT KONOHA.")
  + SAY((4, BOY13, "upper right", "HELLO, KYŪBI."),
        (4, KURAMA, "upper left", "WHAT DO YOU WANT?"))
  + "In PANEL 4 the fox's balloon tail threads cleanly BETWEEN the bars of the gate to his mouth "
    "and never touches the boy. "
  + SFX(3, "STEP.", "Keep this one SMALL, low and quiet in the water directly behind his heel; it "
                    "must not be large, must not be cropped by the panel edge and must not enter "
                    "the protected upper-left area. ")
  + ONLYTEXT,
  R("naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16", "yugao_v4", "env_mizukage_tower",
    "naruto_13", "kurama_inner", "env_inner_sewer"),
  "high"),

 ("p02", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEAL.format(i=3)
  + ONLY(BOY13, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + NOCONTROL +
  "FIVE panels. The exchange is stated, and the history that makes it unacceptable answers it.\n"
  "PANEL 1 (top right, close-up): the fox's near eye opens behind the bars and aims DOWN-RIGHT "
  "toward the boy outside the frame. Only the eye, brow and part of the muzzle are in shot.\n"
  "PANEL 2 (top left, medium): the boy stands at reader-RIGHT facing LEFT with his arms folded. "
  "The gate bars stay visible along the panel's left border.\n"
  "PANEL 3 (middle right, small inset): the fox's muzzle pushed forward behind one bar.\n"
  "PANEL 4 (middle left, wide): the boy holds the fox's eye-line without advancing a single step; "
  "the black water between them is unbroken.\n"
  "PANEL 5 (dominant bottom panel): the fox raises his head and the bars divide his face into "
  "vertical bands. The boy stays a small dark silhouette at lower-RIGHT. " + L_SEAL
  + SAY((1, KURAMA, "upper right", "MAKE IT QUICK."),
        (2, BOY13, "upper right", "I WANT TO OFFER YOU SOMETHING."),
        (2, BOY13, "upper left", "IN RETURN, I WANT SOMETHING FROM YOU."),
        (3, KURAMA, "upper right", "WHAT?"),
        (4, BOY13, "upper right", "IF I GIVE YOU YOUR FREEDOM, COME WHEN I CALL."),
        (5, KURAMA, "upper right", "MY FREEDOM—FOR ANOTHER SHARINGAN TO CONTROL ME?"),
        (5, KURAMA, "upper left", "I WOULD RATHER STAY HERE."))
  + CONNECT(2, '"I WANT TO OFFER YOU SOMETHING." and "IN RETURN, I WANT SOMETHING FROM YOU."', BOY13)
  + CONNECT(5, '"MY FREEDOM—FOR ANOTHER SHARINGAN TO CONTROL ME?" and "I WOULD RATHER STAY HERE."',
            KURAMA)
  + "Every fox balloon's tail threads cleanly BETWEEN the bars to his mouth. " + ONLYTEXT,
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "low"),

 # ---- Spread 2: freedom without agreement -------------------------------------------
 ("p03", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEAL.format(i=3)
  + ONLY(BOY13, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + NOCONTROL +
  "SIX panels. Distrust presses the claim instead of letting him explain uncontested.\n"
  "PANEL 1 (top right, close-up): the boy, still at reader-RIGHT and facing LEFT, level and "
  "unhurried.\n"
  "PANEL 2 (top left, close-up): the fox's lip lifts clear of one fang behind the bars.\n"
  "PANEL 3 (middle right, medium): the boy lifts TWO FINGERS toward his own Sharingan eye and "
  "stops there. He does NOT form a hand seal and NO technique activates — no light, no pattern "
  "change, no effect of any kind leaves his eye.\n"
  "PANEL 4 (middle left, medium): his hand lowers back to his side; the fox watches him from "
  "behind the bars without moving.\n"
  "PANEL 5 (bottom right, narrow reaction panel): the fox's eye narrows to a slit. No text in this "
  "panel.\n"
  "PANEL 6 (bottom left, medium): the boy stands completely motionless with a deliberate span of "
  "empty black water left between him and the gate. " + L_SEAL
  + SAY((1, BOY13, "upper right", "I NEVER SAID I WOULD CONTROL YOU."),
        (2, KURAMA, "upper left", "HUMANS SAY ONE THING."),
        (2, KURAMA, "space immediately below the first balloon, touching it",
         "THEN THEY DO ANOTHER."),
        (3, BOY13, "upper right", "YOU LIVE INSIDE MY BODY."),
        (4, BOY13, "upper right", "YOU KNOW I COULD FORCE YOU."),
        (6, BOY13, "upper right", "I HAVE NOT."),
        (6, BOY13, "upper left", "CONTROL IS BENEATH ME."))
  + CONNECT(2, '"HUMANS SAY ONE THING." and "THEN THEY DO ANOTHER."', KURAMA)
  + CONNECT(6, '"I HAVE NOT." and "CONTROL IS BENEATH ME."', BOY13)
  + "Every fox balloon's tail threads cleanly BETWEEN the bars to his mouth. " + ONLYTEXT,
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "low"),

 ("p04", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEAL.format(i=3)
  + ONLY(BOY13, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + NOCONTROL + FLAT +
  "SIX panels. A failed negotiation becomes an irreversible gift.\n"
  "PANEL 1 (top right, medium): the boy looks up and LEFT toward the fox, chin raised.\n"
  "PANEL 2 (top left, close-up): the fox's stare hardens. The boy is NOT DRAWN anywhere in this "
  "panel.\n"
  "PANEL 3 (middle band, full width): the fox rises to his feet behind the gate and leans RIGHT "
  "into the bars; his nine tails flare across the whole LEFT background as solid opaque shapes. "
  "The boy holds his ground at the right and does not step back.\n"
  "PANEL 4 (lower right, small panel): the boy turns his shoulders toward the sewer exit on the "
  "RIGHT but keeps his head turned back LEFT.\n"
  "PANEL 5 (lower middle, small panel): he takes one step RIGHT, away from the cage.\n"
  "PANEL 6 (dominant lower left panel, the focal panel): he walks away into the darkness at the "
  "RIGHT of frame with his back to the fox. The wide stretch of open black water between him and "
  "the barred beast is the subject of the image. " + L_SEAL
  + SAY((1, BOY13, "upper right", "I DO NOT BELIEVE YOU ARE A MINDLESS BEAST."),
        (2, OFF(BOY13), "upper right", "BUT YOUR HATRED IS MAKING YOUR CHOICES FOR YOU."),
        (3, KURAMA, "upper left", "IF THIS CAGE WERE OPEN, I WOULD TEAR YOU APART."),
        (4, BOY13, "upper right", "YOU WOULD RATHER I LIED?"),
        (5, BOY13, "upper right", "I ASKED FOR YOUR HELP TO MAKE YOU LISTEN."),
        (6, BOY13, "upper right", "IT DOES NOT MATTER."),
        (6, BOY13, "upper middle", "YOU WILL STILL HAVE YOUR FREEDOM."),
        (6, BOY13, "upper left", "I WILL RETURN IN TWO DAYS."))
  + "In PANEL 2 the off-panel tail is a short straight spur entering from the panel's RIGHT border "
    "and stopping there; it must not touch or aim at the fox. "
  + CONNECT(6, '"IT DOES NOT MATTER.", "YOU WILL STILL HAVE YOUR FREEDOM." and "I WILL RETURN IN '
               'TWO DAYS."', BOY13)
  + "The PANEL 3 balloon's tail threads cleanly BETWEEN the bars to the fox's mouth. " + ONLYTEXT,
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "low"),

 # ---- Spread 3: three forces against one seal ---------------------------------------
 ("p05", dict(scene="establishing", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(BOY13, ZETSU) + FB + DRAGON + AXIS_OUT + NOCONTROL +
  "FIVE panels. The extraction plan is made legible before inner and outer space begin "
  "intercutting. Every panel is the PHYSICAL world.\n"
  "PANEL 1 (top panel, full width, half the page height): extreme-wide establishing shot of the "
  "volcanic wilderness. Basalt terraces step down from reader-RIGHT to reader-LEFT into the "
  "caldera, vents steaming, the ash-red sky filling the top third. The boy and the JOINED plant "
  "creature are small figures together at centre-RIGHT.\n"
  "PANEL 2 (middle right, medium): the boy kneels at centre-RIGHT facing LEFT. The joined plant "
  "creature crouches to his LEFT, facing RIGHT.\n"
  "PANEL 3 (middle left, medium): the creature holds the boy's eye-line, its two-toned face fully "
  "in frame.\n"
  "PANEL 4 (bottom right, medium): the boy lays one flat hand over his own abdomen.\n"
  "PANEL 5 (bottom left, wide): the boy closes his eyes while the creature braces one knee against "
  "the basalt to his LEFT. The caldera slopes behind them carry the eye LEFT and out of frame. "
  + L_DRAGON
  + CAP(1, "upper right", "TWO DAYS LATER — ANCIENT LAND OF DRAGONS.")
  + SAY((2, BOY13, "upper right", "I WILL WEAKEN MINATO'S SEAL FROM INSIDE."),
        (3, ZETSU, "upper left", "I PULL THE NINE-TAILS OUT FROM HERE."),
        (4, BOY13, "upper right", "THE KYŪBI PUSHES FROM THE OTHER SIDE."),
        (5, ZETSU, "upper right", "AND IF THE SEAL HOLDS?"),
        (5, BOY13, "upper left", "WE BREAK IT."))
  + "In PANEL 3 the creature's tail points at the single JOINED mouth of its two-toned face. "
  + ONLYTEXT,
  R("naruto_13", "zetsu"), "medium"),

 ("p06", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ZET.format(i=3) + ENV_SEAL.format(i=4)
  + ZOR + ONLY(BOY13, KURAMA, ZETSU) + FB + CAGE + AXIS_IN + AXIS_OUT + FOXTALK + HALF
  + FLAT + NOHARM + NOCONTROL +
  "SIX panels. The three-part action begins in the order he specified. PANELS 1, 3, 4, 5 and 6 are "
  "the INNER SEAL SPACE (Image 4). PANEL 2 is the PHYSICAL volcanic wilderness. " + DRAGON +
  "PANEL 1 (top right, medium, inner world): the boy is drawn plainly at reader-RIGHT, facing the "
  "gate. The fox stands behind the bars on the LEFT.\n"
  "PANEL 2 (top left, narrow, physical world): the plant creature waits to the LEFT of the boy's "
  "kneeling body on the basalt. Nothing has happened yet. This panel is silent — no text in it.\n"
  "PANEL 3 (middle band, full width, inner world): the fox leans RIGHT into the bars; the boy "
  "raises one arm and points once toward him.\n"
  "PANEL 4 (bottom right, close-up, inner world): the black seal formula surfaces across the boy's "
  "bared abdomen as a flat opaque black spiral of hard-edged glyphs. His chakra-lit fingers press "
  "into its centre. Skin and clothing stay fully drawn and undamaged.\n"
  "PANEL 5 (bottom middle, close-up, inner world): his hand turns CLOCKWISE and his whole torso "
  "twists against the resistance.\n"
  "PANEL 6 (dominant bottom left panel, inner world): the seal ink liquefies and runs downward in "
  "flat black rivulets while solid orange chakra leaks RIGHTWARD through the bars toward the boy. "
  "The fox's eye opens wider at reader-LEFT; the boy winces at lower-RIGHT. The bars, the water and "
  "the stonework remain completely legible through and around the chakra. " + L_SEAL
  + SAY((1, BOY13, "upper right", "I WILL WEAKEN THE SEAL."),
        (1, BOY13, "upper left", "ZETSU WILL PULL FROM OUTSIDE."),
        (3, BOY13, "upper right", "YOU FORCE YOURSELF OUT."))
  + CONNECT(1, '"I WILL WEAKEN THE SEAL." and "ZETSU WILL PULL FROM OUTSIDE."', BOY13)
  + SFX(4, "THRUM.", "Place it directly beside his pressing fingers. ")
  + SFX(5, "CRK.", "Curve it around the seal formula. ")
  + SFX(6, "HSSSS.", "Keep this one LOW AND THIN beside the right-moving chakra; it must not be "
                     "large and must not cover the fox's eye. ")
  + ONLYTEXT,
  R("naruto_13", "kurama_inner", "zetsu", "env_inner_sewer"), "medium"),

 # ---- Spread 4: the seal calls its maker --------------------------------------------
 ("p07", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + KURAMA_INNER.format(i=3) + ENV_SEAL.format(i=4)
  + ZOR + ONLY(BOY13, ZETSU, KURAMA) + FB + CAGE + AXIS_IN + AXIS_OUT + FOXTALK + HALF
  + FLAT + NOHARM + NOCONTROL +
  "FIVE panels. Leaked chakra is connected to the creature's pull and the simultaneous strain is "
  "made readable. PANELS 1, 2, 3 and 5 are the PHYSICAL volcanic wilderness; PANEL 4 is the INNER "
  "SEAL SPACE (Image 4). " + DRAGON +
  "PANEL 1 (top right, steep diagonal, physical world): the boy pitches LEFT off his knees. The "
  "plant creature catches both his shoulders from the LEFT before his head reaches the basalt. No "
  "text in this panel.\n"
  "PANEL 2 (top left, close-up, physical world): the liquefied black formula slides across the "
  "boy's pale abdomen as flat opaque ink, and one solid orange thread pushes out through its "
  "centre. No wound, no blood, no broken skin.\n"
  "PANEL 3 (middle band, full width, physical world): the creature plants its RIGHT palm flat on "
  "the seal, closes on the orange thread and draws it LEFT. Its LEFT hand is locked in a "
  "one-handed seal and holds it.\n"
  "PANEL 4 (bottom right, inset, inner world): the gate bars bow toward the RIGHT as the fox drives "
  "his shoulder into them from the LEFT. The boy braces at lower-RIGHT. No text in this panel.\n"
  "PANEL 5 (dominant bottom left panel, physical world): the flat opaque orange tether stretches "
  "from the boy at centre-RIGHT to the creature's pulling hand at centre-LEFT. The creature leans "
  "LEFT; the boy's body arches RIGHT against the force. The basalt and the ash-red sky stay fully "
  "drawn behind the tether. " + L_DRAGON
  + SAY((3, ZETSU, "upper left", "I HAVE IT."))
  + SFX(2, "HSSSS.", "Small and thin, directly beside the orange thread. ")
  + SFX(5, "THRUM.", "Write it ALONG the length of the tether. ")
  + ONLYTEXT,
  R("naruto_13", "zetsu", "kurama_inner", "env_inner_sewer"), "medium"),

 ("p08", dict(scene="action", light="dark", cast="small_group", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ZET.format(i=3)
  + MINATO_HAND.format(i=4) + ENV_SEAL.format(i=5) + ZOR
  + ONLY(BOY13, KURAMA, ZETSU,
         "one UNIDENTIFIED man, who is present ONLY in panel 5 as a single bare adult hand and a "
         "plain dark sleeved forearm cropped at the panel edge — no face, head, hair, shoulder, "
         "body, silhouette, crest, symbol or name of him may be visible anywhere on this page")
  + FB + CAGE + AXIS_IN + AXIS_OUT + HALF + FLAT + NOHARM + NOCONTROL +
  "FIVE panels. The boy reaches the final lock and the page ends before revealing what stops him. "
  "PANELS 1, 2, 4 and 5 are the INNER SEAL SPACE (Image 5); PANEL 3 is the PHYSICAL volcanic "
  "wilderness. " + DRAGON +
  "PANEL 1 (top right, narrow, inner world): the boy is down on one knee at reader-RIGHT, "
  "breathing through the pain, eyes open. The gate shudders at the LEFT. No text in this panel.\n"
  "PANEL 2 (top left, narrow, inner world): the fox pushes RIGHT again with his claws dug into the "
  "floor behind the bars. No text in this panel.\n"
  "PANEL 3 (middle band, full width, physical world): the plant creature keeps pulling LEFT and the "
  "chakra tether is visibly thicker, but NOTHING of the fox has emerged outside — the caldera "
  "beyond the tether is empty. The boy stays conscious with his eyes shut. No text in this panel.\n"
  "PANEL 4 (bottom right, medium, inner world): the boy has risen to the paper seal pasted across "
  "the gate and closes his RIGHT hand on its lower edge. The corner lifts. The fox watches from the "
  "LEFT, still pushing.\n"
  "PANEL 5 (dominant bottom left, close-up): an unidentified man's bare hand clamps around the "
  "boy's wrist before the paper comes free. Show ONLY that hand, a plain dark sleeve cropped at the "
  "forearm before any cuff, band or stripe, the boy's arrested fingers, and the half-lifted paper. "
  "No face, no hair, no head, no shoulder, no silhouette, no crest and no symbol anywhere. No "
  "balloon in this panel. " + L_SEAL
  + SFX(4, "RRRIP—", "Place it beside the lifting corner of the paper. The long dash must run "
                     "downward and TERMINATE exactly at the gripping hand in panel 5's direction, "
                     "and no part of it may suggest a face or figure. ")
  + ONLYTEXT,
  R("naruto_13", "kurama_inner", "zetsu", "minato_kushina", "env_inner_sewer"), "medium"),

 # ---- Spread 5: the dead keeper of the cage -----------------------------------------
 ("p09", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=4),
  FILL + RTL + N13.format(i=1) + MINATO.format(i=2) + KURAMA_INNER.format(i=3)
  + ENV_SEAL.format(i=4)
  + ONLY(BOY13, MIN, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + FLAT + NOCONTROL +
  "FOUR panels. The hand is identified and all three read the relationship differently. The blond "
  "man is STORED CHAKRA, not a living body: he is drawn as a normal solid figure with a faint "
  "hard-edged pale outline, and he is never a ghost, never an animated corpse, never bandaged, "
  "never cracked and never accompanied by grave soil, coffin or afterlife imagery.\n"
  "PANEL 1 (large upper panel taking NO MORE THAN 45% of the page height — it must be clearly "
  "smaller than page 14's top panel): the blond man in the white flame-hemmed coat stands at "
  "centre-RIGHT holding the boy's wrist and has pushed him DOWN-RIGHT, away from the paper seal. "
  "The fox stays behind the still-CLOSED gate at the LEFT and has stopped pushing to glare RIGHT at "
  "the man.\n"
  "PANEL 2 (bottom right, close-up): the boy looks up-RIGHT at the man, his surprise already back "
  "under control. The man remains visible at the panel's LEFT edge and visibly WINCES at hearing "
  "his own name.\n"
  "PANEL 3 (bottom middle, close-up): the fox's muzzle presses close to the bars, eye-line hard "
  "RIGHT.\n"
  "PANEL 4 (bottom left, close-up): the fox bares his teeth. " + L_SEAL
  + SAY((1, KURAMA, "upper left, placed high so it reads first", "YONDAIME."),
        (1, MIN, "upper right, placed lower than the other balloon", "NARUTO?"),
        (2, BOY13, "upper right", "HELLO, MINATO."),
        (3, KURAMA, "upper left", "COME CLOSER."),
        (4, KURAMA, "upper left", "I WILL TEAR YOU APART."))
  + "In PANEL 1 both balloons are LOCAL and short-tailed: the fox's balloon sits beside him and its "
    "one short tail passes through the nearest bar to his mouth, and the man's balloon sits beside "
    "him with one short tail to his mouth. The fox's balloon is placed HIGHER so it reads first. "
    "Neither tail crosses the panel and neither crosses or touches the other balloon. " + ONLYTEXT,
  R("naruto_13", "minato_kushina", "kurama_inner", "env_inner_sewer"), "low"),

 ("p10", dict(scene="dialogue", light="dark", cast="small_group", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + MINATO.format(i=2) + KURAMA_INNER.format(i=3)
  + ENV_SEAL.format(i=4)
  + ONLY(BOY13, MIN, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + FLAT + NOCONTROL +
  "SIX panels. The interruption ends without becoming a father-and-son conversation: no embrace, "
  "no tears, no reconciliation, no mention or image of a mother, and no third party. The blond man "
  "remains STORED CHAKRA drawn as a solid figure with a faint hard-edged pale outline.\n"
  "PANEL 1 (top right, two-shot): the man opens his fingers and releases the boy's wrist. They face "
  "one another on the RIGHT side of the cage axis; the man looks down-LEFT, the boy up-RIGHT.\n"
  "PANEL 2 (top left, close-up): the boy is back on his feet, expression level.\n"
  "PANEL 3 (middle band, full width): the man steps LEFT to block the boy's path back to the paper "
  "seal; the bars stay behind him across the whole left background.\n"
  "PANEL 4 (bottom right, medium): the boy steps inside the man's reach and sets his open RIGHT "
  "palm flat against the man's chest.\n"
  "PANEL 5 (bottom middle, close-up): the man looks down at the boy while the boy's hand begins to "
  "emit a FLAT, OPAQUE outward pulse — a hard-edged pale ring, not a glow and not a flash.\n"
  "PANEL 6 (dominant bottom left panel): the boy drives the pulse LEFT through the man, who breaks "
  "into flat opaque pale fragments drifting left. NO body, NO skeleton, NO soul shape, NO corpse "
  "and NO grave imagery is left behind. The fox watches through the bars behind the fragments and "
  "stays fully drawn and legible between them. " + L_SEAL
  + SAY((1, MIN, "upper right", "WHY ARE YOU BREAKING THE SEAL?"),
        (2, BOY13, "upper right", "IT DOES NOT CONCERN YOU."),
        (3, MIN, "upper right", "I CAN'T LET YOU FREE THE NINE-TAILS."),
        (3, MIN, "upper left", "IT'S DANGEROUS—"),
        (4, BOY13, "upper right", "YOU ARE CHAKRA LEFT INSIDE A SEAL."),
        (5, BOY13, "upper right", "YOU ARE DEAD."),
        (5, BOY13, "upper left", "YOUR ROLE IS FINISHED."),
        (6, BOY13, "upper right", "DISAPPEAR, MINATO."))
  + CONNECT(3, '"I CAN\'T LET YOU FREE THE NINE-TAILS." and "IT\'S DANGEROUS—"', MIN)
  + CONNECT(5, '"YOU ARE DEAD." and "YOUR ROLE IS FINISHED."', BOY13)
  + SFX(6, "FSHH.", "Place it among the pale fragments; keep it small enough that the fox behind "
                    "them stays visible. ")
  + ONLYTEXT,
  R("naruto_13", "minato_kushina", "kurama_inner", "env_inner_sewer"), "low"),

 # ---- Spread 6: the cage opens, the body fails --------------------------------------
 ("p11", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV_SEAL.format(i=3)
  + ONLY(BOY13, KURAMA) + FB + CAGE + AXIS_IN + FOXTALK + HALF + FLAT + NOCONTROL +
  "SIX panels. The seal opens and the fox alone decides whether he helps the boy survive. The boy "
  "makes NO hand seal, activates NO eye and issues NO command anywhere on this page.\n"
  "PANEL 1 (top right, close-up): the boy's hand returns to the half-lifted paper seal and tears it "
  "fully away to the RIGHT.\n"
  "PANEL 2 (top left, wide): the gate lock releases. THE ENV PLATE IS OVERRIDDEN FROM HERE ON: the "
  "two barred doors swing APART from the centre and no longer enclose anything. The fox stands on "
  "the LEFT side of the open threshold and has not yet crossed it.\n"
  "PANEL 3 (middle right, medium): the boy at reader-RIGHT faces LEFT across the now-open "
  "threshold, hands empty and open at his sides.\n"
  "PANEL 4 (middle left, close-up): the fox studies him and gives no answer; his mouth stays shut. "
  "The boy is NOT DRAWN anywhere in this panel.\n"
  "PANEL 5 (bottom right, medium): the boy turns RIGHT toward the inner-world exit and deliberately "
  "gives the fox his back.\n"
  "PANEL 6 (dominant bottom left panel): the boy recedes into the darkness at the RIGHT while the "
  "fox fills the open gateway at the LEFT, both doors standing wide and no bars between them. "
  + L_SEAL
  + SAY((3, BOY13, "upper right", "LEAVE SOME CHAKRA BEHIND."),
        (4, OFF(BOY13), "upper right", "WITHOUT IT, YOUR EXTRACTION MAY KILL ME."),
        (5, BOY13, "upper right", "WHEN YOU ARE FREE, I WILL BE UNABLE TO STOP YOU."),
        (6, BOY13, "upper right", "IF YOU TRY ANYTHING, I WILL MAKE YOU REGRET IT."))
  + "In PANEL 4 the off-panel tail is a short straight spur entering from the panel's RIGHT border "
    "and stopping there; it must not touch or aim at the fox. "
  + SFX(1, "RIP.", "Place it beside the tearing paper. ")
  + SFX(2, "KLANG.", "Write it ACROSS the separating bars as the doors part. ")
  + SFX(6, "HNF.", "Keep this one small and LOW beside the fox's muzzle. It is a bare sound effect "
                   "with NO balloon and NO tail. ")
  + ONLYTEXT,
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "medium"),

 ("p12", dict(scene="action", light="day", cast="two", mood="violent", panels=5),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + KURAMA_INNER.format(i=3)
  + KURAMA_FULL.format(i=4) + ENV_SEAL.format(i=5) + ZOR
  + ONLY(BOY13, ZETSU, KURAMA) + FB + AXIS_OUT + AXIS_IN + HALF + FLAT + NOHARM + NOCONTROL +
  "FIVE panels. The physical cost lands immediately, and cause always precedes result. PANELS 1, "
  "2, 4 and 5 are the PHYSICAL caldera; PANEL 3 is the INNER SEAL SPACE (Image 5), where THE ENV "
  "PLATE IS OVERRIDDEN — the gate now stands WIDE OPEN with its two barred doors swung apart and "
  "nothing enclosing the fox. Image 3 is the fox INSIDE the seal in panel 3; Image 4 is his "
  "INCOMPLETE physical mass in panel 5. " + DRAGON +
  "PANEL 1 (top right, close-up): out in the caldera the seal formula erupts from the boy's abdomen "
  "and crawls across his torso as flat opaque black glyph-work. The creature's chakra tether stays "
  "taut off the LEFT edge. Skin unbroken — no wound and no blood.\n"
  "PANEL 2 (top left, tall panel): the boy's body lifts clear above the basalt, back arched, skin "
  "draining to grey. The plant creature braces below-LEFT and keeps pulling.\n"
  "PANEL 3 (middle right, inset, inner world): the fox crosses the OPEN gateway from LEFT to RIGHT "
  "as his chakra streams out of frame toward the physical world. No bars close behind him. No text "
  "in this panel.\n"
  "PANEL 4 (middle left, close-up): the creature's feet skid LEFT through the ash, but its "
  "one-handed seal does not break.\n"
  "PANEL 5 (dominant bottom panel, the focal panel): a vast INCOMPLETE orange silhouette builds on "
  "the LEFT side of the caldera — a flat opaque mass with hard outlines in which only bulk and a "
  "few tail arcs have formed, cut off and unfinished, never a whole fox. The boy hangs centre-RIGHT "
  "inside the black formula; the creature stays between them, drawing the tether LEFT. The basalt "
  "terraces and ash-red sky remain fully drawn and legible behind and through the orange mass. "
  + L_DRAGON
  + SAY((2, BOY13, "upper centre, centred high in the panel", "AAAGH—!"),
        (4, ZETSU, "upper left", "IT IS MOVING."))
  + SFX(1, "VRRRM.", "Wrap it around the seal formula. ")
  + ONLYTEXT,
  R("naruto_13", "zetsu", "kurama_inner", "kurama_full", "env_inner_sewer"), "medium"),

 # ---- Spread 7: the Nine-Tails' first free choice -----------------------------------
 ("p13", dict(scene="action", light="day", cast="two", mood="violent", panels=6),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + KURAMA_FULL.format(i=3) + ZOR
  + ONLY(BOY13, ZETSU, KURAMA) + FB + DRAGON + AXIS_OUT + HALF + FLAT + NOHARM + NOCONTROL +
  "SIX panels, all in the PHYSICAL caldera. The extraction's duration and danger are given visible "
  "weight. THE FOX IS NEVER SHOWN WHOLE ON THIS PAGE — he is incomplete, cropped or occluded in "
  "every panel he appears in.\n"
  "PANEL 1 (top right, wide): the locked caldera axis. The sun is high. The INCOMPLETE orange fox "
  "mass occupies the LEFT, the plant creature pulls at centre-LEFT, the boy hangs centre-RIGHT.\n"
  "PANEL 2 (top left, wide): the SAME locked camera angle later — the sun has moved and the ash "
  "shadows are far longer. The fox's head and shoulders are now solid, but the rest of him is still "
  "unformed.\n"
  "PANEL 3 (middle right, close-up): the boy's face is bloodless, his eyes barely open, his breath "
  "shallow. No wounds and no blood.\n"
  "PANEL 4 (middle left, close-up): the creature's pulling arm shakes while its joined "
  "black-and-white face stays fixed on the tether.\n"
  "PANEL 5 (bottom right, tall panel): the fox's last trailing chakra tears free of the boy's "
  "abdomen toward the LEFT. The boy begins to fall DOWN-RIGHT.\n"
  "PANEL 6 (bottom left): the extraction completes. The creature drops the empty tether and lunges "
  "RIGHT to catch the falling boy. At the FAR LEFT the now-physical fox is deliberately cropped by "
  "the panel edge and occluded by foreground basalt and settling chakra — only partial legs and a "
  "few tail arcs are visible, NEVER an unobstructed body. No text in this panel. " + L_DRAGON
  + CAP(2, "upper right", "ONE HOUR LATER...")
  + SFX(5, "SNAP.", "Write it ALONG the separating thread. ")
  + ONLYTEXT,
  R("naruto_13", "zetsu", "kurama_full"), "medium"),

 ("p14", dict(scene="establishing", light="day", cast="two", mood="somber", panels=5),
  FILL + RTL + KURAMA_FULL.format(i=1) + N13.format(i=2) + ZET.format(i=3) + ENV_SEAL.format(i=4)
  + ZOR
  + ONLY(KURAMA, BOY13, ZETSU,
         "the same boy also appearing ONLY inside the small panel-4 memory image, walking away "
         "from the barred cage")
  + FB + DRAGON + AXIS_OUT + HALF + FLAT + NOHARM + NOCONTROL +
  "FIVE panels. The fox is given a real opportunity to kill the helpless boy, and visibly chooses "
  "not to. PANEL 4 is a small bordered MEMORY IMAGE of the inner seal space (Image 4); every other "
  "panel is the PHYSICAL caldera.\n"
  "PANEL 1 (dominant panel filling the upper TWO-THIRDS of the page — THE LARGEST PANEL IN THE "
  "WHOLE CHAPTER, unequivocally larger than page 9's top panel): for the first time the fox's "
  "ENTIRE physical body is visible and completely UNOBSTRUCTED on the LEFT, fully free, all nine "
  "tails spread out into open ash-red sky. There is NO gate, NO bars, NO chain, NO seal, NO "
  "foreground crop and NO chakra haze anywhere on him — nothing overlaps or cuts his body. The "
  "plant creature kneels at centre-RIGHT over the collapsed, chalk-pale boy. The fox looks "
  "DOWN-RIGHT at the boy.\n"
  "PANEL 2 (lower right, close-up): the fox's eye stays fixed on the helpless boy. No text in this "
  "panel.\n"
  "PANEL 3 (lower middle, close-up): one immense claw lifts and angles DOWN-RIGHT toward the boy. "
  "It has not touched him. No text in this panel.\n"
  "PANEL 4 (small bordered inset lying over the raised claw, lower left): a memory image of the "
  "YOUNGER boy walking away from the barred cage, drawn small, quiet and slightly desaturated with "
  "a hard border. It is a remembered image, not a second scene.\n"
  "PANEL 5 (bottom strip, full width): the fox lowers the claw back down to the ground on the LEFT. "
  "At the RIGHT the plant creature lifts the boy and carries him farther RIGHT into a basalt "
  "fissure; the beast makes no move to stop them. No text in this panel. " + L_DRAGON
  + SFX(1, "WHUMM.", "Keep it SMALL and low in the settling chakra at the fox's feet; it must not "
                     "overlap his body or his tails and must not crop his silhouette. ")
  + ECHO(4, "upper area of the inset", "YOU WILL STILL HAVE YOUR FREEDOM.")
  + ONLYTEXT,
  R("kurama_full", "naruto_13", "zetsu", "env_inner_sewer"), "high"),

 # ---- Spread 8: what the Nine-Tails left behind -------------------------------------
 ("p15", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(BOY13, ZETSU + ", joined in panel 1 only", ZWHITE, ZBLACK) + FB + FISSURE + FLAT + NOHARM + NOCONTROL +
  "SIX panels inside the sheltering basalt fissure. Two separate reasons the boy has a chance to "
  "live are kept visually distinct. THE PLANT CREATURE SEPARATES ON THIS PAGE: from panel 2 onward "
  "its chalk-WHITE half and its pure BLACK half are two complete separate bodies, each built from "
  "its own colour of the reference image. The white half stays visible and outside the boy in every "
  "panel, so nothing here can be mistaken for the fox's chakra, a medical technique or an invented "
  "healer. There is no fox anywhere on this page.\n"
  "PANEL 1 (top right, wide): the still-JOINED plant creature lowers the boy to the fissure floor at "
  "centre. He is limp and pale. No medical equipment, no bandages and no other person. No text in "
  "this panel.\n"
  "PANEL 2 (top left, medium): the white half separates and stands clear to the RIGHT while the "
  "black half peels LEFT toward the boy's torso.\n"
  "PANEL 3 (middle band, full width): the black half flows over and INTO the boy's body, taking "
  "control only far enough to keep his failing systems working. The white half watches from the "
  "RIGHT, fully drawn.\n"
  "PANEL 4 (bottom right, close-up): flat opaque black markings settle across the boy's chest and "
  "neck, and one weak pulse returns beneath them. Skin unbroken, no wound, no blood.\n"
  "PANEL 5 (dominant bottom middle panel, the focal panel): a cutaway INSIDE the boy's chakra "
  "pathways — his own chakra drawn as dim grey-blue channels with thin SOLID ORANGE chakra already "
  "circulating through them. It is simply present: no seal, no eye effect, no command mark, no "
  "hand, no creature and no action of any kind is shown installing it.\n"
  "PANEL 6 (bottom left, close-up): the boy is still unconscious, but the next pulse under the "
  "black markings is firmer. " + L_FISSURE
  + SAY((2, ZWHITE, "upper right", "HE MAY NOT SURVIVE."),
        (3, ZBLACK, "upper left", "I WILL SUSTAIN HIM."))
  + THOUGHT((5, ZBLACK, "lower right", "THE KYŪBI LEFT CHAKRA IN HIS PATHWAYS."))
  + SFX(4, "THUM.", "Small, directly beside his chest. ")
  + SFX(6, "THUM.", "Small, directly beside his chest, matching panel 4's placement. ")
  + ONLYTEXT,
  R("naruto_13", "zetsu"), "low"),

 ("p16", dict(scene="dialogue", light="dark", cast="two", mood="calm", panels=6),
  FILL + RTL + N13.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(BOY13, ZETSU, ZWHITE, ZBLACK) + FB + FISSURE + FLAT + NOHARM + NOCONTROL +
  "SIX panels inside the same fissure across several days. The recovery is partial and never "
  "instant: he stays pale, thin and unsteady in every panel. PANEL 1 still shows the creature's two "
  "halves separate; from PANEL 2 onward it is JOINED again and wholly outside his body.\n"
  "PANEL 1 (top right, wide): the same fissure a few days later. The boy lies unconscious at "
  "centre with only part of his colour returned. The black half peels back OUT of him and rejoins "
  "the white half at the LEFT before he wakes.\n"
  "PANEL 2 (top left, medium): the next day. The rejoined plant creature is already seated well "
  "clear of him at the LEFT, entirely outside his body, when the boy's eyes open at centre-RIGHT. "
  "No dialogue in this panel.\n"
  "PANEL 3 (middle right, close-up): the boy pushes himself upright with one hand and forms a small "
  "test seal with the other. Both arms shake visibly.\n"
  "PANEL 4 (middle left, two-shot): the creature turns to face RIGHT toward him.\n"
  "PANEL 5 (bottom right, medium): the boy kneels into a reverse-summoning seal, facing LEFT toward "
  "the caldera he means to return to. A flat opaque summoning ring of ILLEGIBLE SCRIBBLE glyphs "
  "spreads on the ash beneath his hands.\n"
  "PANEL 6 (dominant bottom left panel): flat opaque white summoning smoke pulls him LEFT and out "
  "of the fissure. The plant creature stays at the far RIGHT edge, unmoving. The rock walls stay "
  "fully drawn through the smoke. " + L_FISSURE
  + CAP(1, "upper right", "A FEW DAYS LATER.")
  + CAP(2, "upper right", "THE NEXT DAY.")
  + SAY((1, ZBLACK, "upper left", "HE IS STABLE."),
        (3, BOY13, "upper right", "I CAN MOLD CHAKRA."),
        (4, ZETSU, "upper left", "YOU HAVE NOT RECOVERED."),
        (5, BOY13, "upper right", "I DO NOT NEED TO."))
  + SFX(6, "FWOOM.", "Embed it inside the summoning smoke. ")
  + ONLYTEXT,
  R("naruto_13", "zetsu"), "low"),

 # ---- Spread 9: terms between equals ------------------------------------------------
 ("p17", dict(scene="establishing", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N13.format(i=1) + KURAMA_FULL.format(i=2)
  + ONLY(BOY13, KURAMA) + FB + DRAGON + FOXTALK + HALF + FLAT + NOCONTROL +
  "SIX panels in the open caldera. The absence of the cage does the work before anything is asked: "
  "THERE ARE NO BARS, NO GATE, NO CHAIN, NO SEAL PAPER and NO enclosure of any kind anywhere in any "
  "panel on this page. The boy is still pale, thin and unsteady throughout.\n"
  "PANEL 1 (top panel, full width, half the page height): wide establishing shot of the open "
  "caldera. The fox rests freely on the LEFT with open ash-red sky behind his spread tails; the boy "
  "arrives out of dissipating flat white summoning smoke at the far RIGHT. No text in this panel.\n"
  "PANEL 2 (middle right, close-up): the fox opens ONE eye toward the RIGHT. No text in this "
  "panel.\n"
  "PANEL 3 (middle left, wide): the boy walks LEFT but stops well outside the fox's reach, leaving "
  "a broad span of open ash-covered ground between them.\n"
  "PANEL 4 (bottom right, close-up): the fox's head stays down on his paws.\n"
  "PANEL 5 (bottom middle, medium): the boy stands without smiling, eye-line LEFT.\n"
  "PANEL 6 (bottom left, close-up): the fox's eye fills the panel, aimed RIGHT. " + L_DRAGON
  + SAY((3, BOY13, "upper right", "HOW DOES IT FEEL TO BE FREE?"),
        (4, KURAMA, "upper left", "GOOD."),
        (5, BOY13, "upper right", "DO YOU TRUST ME?"),
        (6, KURAMA, "upper left", "NO."))
  + ONLYTEXT,
  R("naruto_13", "kurama_full"), "medium"),

 ("p18", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + KURAMA_FULL.format(i=2) + N16_SWORD.format(i=3) + JIR.format(i=4)
  + KAK.format(i=5) + SASUKE16.format(i=6) + YUGAO_V4.format(i=7) + ENV_KIRI.format(i=8)
  + ONLY(BOY13 + " and the enormous nine-tailed fox, both appearing ONLY in the flashback of "
         "panels 1-3", BOY16, SAGE, MAN, SAS16, YUG,
         "the last four appearing ONLY in the present-day panels 4-5")
  + FB + GEAR + DRAGON + FOXTALK + HALF + FLAT + NOCONTROL +
  "FIVE panels. LAST PAGE OF THE CHAPTER. PANELS 1-3 END THE FLASHBACK in the open caldera — no "
  "bars, no gate, no seal and no enclosure anywhere in them. PANELS 4-5 RETURN TO PRESENT-DAY KIRI "
  "(Image 8). The younger boy and the sixteen-year-old are two different figures and must NEVER "
  "appear in the same panel; the cut back is a plain editorial cut with no haze and no memory cue.\n"
  "PANEL 1 (top right, close-up, silent, flashback): the younger boy absorbs the refusal with no "
  "change in posture and no change in his gaze. No text in this panel.\n"
  "PANEL 2 (dominant centre panel, flashback, the emotional focal panel — but still visibly SMALLER "
  "than page 14's top panel): the fox raises his head against completely open ash-red sky on the "
  "LEFT, nothing enclosing or overlapping him. The boy stands small at lower-RIGHT.\n"
  "PANEL 3 (lower right, medium, flashback): the boy holds the fox's eye-line steadily across the "
  "open ground.\n"
  "PANEL 4 (lower middle strip, neutral OVERHEAD re-establishing shot, present day): a high "
  "straight-down-angled view of the Kiri street that RESETS the geography. The sixteen-year-old in "
  "repaired red armour now stands ALONE on the reader's LEFT, facing the group on the reader's "
  "RIGHT; the big white-haired man is nearest him, with the masked silver-haired man, the older "
  "dark-haired teen and the purple-haired kunoichi behind the white-haired man. If the overhead "
  "crop hides his hip, the camera is merely hiding the sword — it is still equipped.\n"
  "PANEL 5 (bottom left, narrow panel, present day): the sixteen-year-old's afterimage exits "
  "through the LEFT edge, leaving the group standing at the RIGHT. The white-haired man's eye-line "
  "follows LEFT; the other three do not move. " + L_KIRI
  + SAY((2, KURAMA, "upper right", "BUT I CAN WORK WITH YOU."),
        (2, KURAMA, "upper middle", "I WILL NOT BECOME YOUR PET."),
        (2, KURAMA, "upper left", "AND I WILL NOT DO ANYTHING I DO NOT CHOOSE."),
        (3, BOY13, "upper right", "THAT IS FINE."),
        (4, BOY16, "upper left, directly beside him", "THAT DOES NOT CONCERN YOU."))
  + CONNECT(2, '"BUT I CAN WORK WITH YOU.", "I WILL NOT BECOME YOUR PET." and "AND I WILL NOT DO '
               'ANYTHING I DO NOT CHOOSE."', KURAMA)
  + "In PANEL 4 the balloon is LOCAL to the armoured teen on the left, with ONE short visible tail "
    "to his mouth; it must not drift toward or point at anyone in the group on the right. "
  + SFX(5, "FSHH.", "Keep it SMALL at the left vanishing edge, beside the afterimage. ")
  + ONLYTEXT,
  R("naruto_13", "kurama_full", "naruto_v4_armor_sword", "jiraiya", "kakashi", "sasuke_16",
    "yugao_v4", "env_mizukage_tower"),
  "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch04" / "raw", HERE / "v5ch04" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
