"""Volume 5, Chapter 5 — "Goodbye, Mizukage". 10 pages.

Source: fic ch12:517-555, with the travel-state handoff supported by ch13:67-75 and
ch14:37-39. Translated 1:1 from story/volume_05/drafts/ch05_goodbye_mizukage.md —
19 spoken balloons, one time card, one chapter marker. Reading order is RIGHT TO LEFT
per the approved `name`; every page states it.

This builder must match the `name`, not improve on it. Every balloon below is the
draft's exact final text, in the draft's exact panel and position.

Reference gap recorded for the owner (never invented here): there is no dedicated
kushina.png sheet, so page 10's single lock of red hair is bound from the two-person
minato_kushina.png with the blond half explicitly excluded; and there is no approved
younger-training-period Naruto sheet, so naruto_13.png carries the dream-memory boy.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, FILL, JIR, KAK, MAN, N13, OFF, ONLY, R, SAGE, SAY, ZET  # noqa: E402
from prompts_v4 import (GUNBAI_V4, KIRI_REBELS, MEI_V4, N16_ARMOR, N16_BLACK,   # noqa: E402
                        N16_SWORD, SASUKE16, YUGAO_V4, MEI_V4_SPEAKER,
                        N16_SPEAKER, SASUKE16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
BOY13 = "the younger long-haired blond boy in the black shirt with the red spiral"
YUG = YUGAO_V4_SPEAKER
MEI = MEI_V4_SPEAKER
SAS16 = SASUKE16_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")

# There is no single-figure Kushina sheet in refs/images; the two-person parents sheet is the
# only source of her exact hair and dress, so the blond half is excluded by name.
KUSHINA_PARTIAL = (
    "Image {i} is a TWO-PERSON REFERENCE SHEET. Use ONLY THE RIGHT-HAND FIGURE — the young woman "
    "with VERY LONG straight dark-red hair falling past her waist and a long dark green dress over "
    "a pale cream blouse — and COMPLETELY IGNORE the blond man on the left of that sheet, who does "
    "not appear anywhere on this page. On this page even the woman is almost entirely hidden: only "
    "her hair colour and length and one bare forearm are taken from the sheet. Ignore the sheet's "
    "white background, its lineup layout and its neutral standing pose. ")

# Environment plates. Two different locations share some pages, so each gets a named binding
# instead of the generic ENV line, and every index is stated.
ENV_STREET = ("Image {i} is the LOCATION REFERENCE for the rebuilding Kiri street — reuse its "
              "architecture, scaffolding, wet stone, colour palette and lighting. Do not copy its "
              "camera angle; ignore that it is empty of people. ")
ENV_GATE = ("Image {i} is the LOCATION REFERENCE for the misted Kiri village gate and the empty "
            "road outside it — reuse its architecture, colour palette and dense white sea mist. "
            "Do not copy its camera angle; ignore that it is empty of people. ")
ENV_ROAD = ("Image {i} is the LOCATION REFERENCE for the wooded travel road and forest stopping "
            "point — reuse its trees, trunks, ground cover and colour palette. Do not copy its "
            "camera angle; ignore that it is empty of people. ")
ENV_SEAL = ("Image {i} is the LOCATION REFERENCE for the OPENED inner seal space — reuse its damp "
            "stonework, shallow standing water and colour palette, but the great barred cage is "
            "GONE: only one broken gate edge remains and no bars enclose anything. Do not copy its "
            "camera angle; ignore that it is empty of people. ")

# Continuity locks carried by every page that shows the present-day teen.
GEAR = ("His equipment state is fixed for this whole chapter: the dark purple gunbai with its "
        "chain on his back, and a PLAIN straight sword in a dark sash sheath at his left hip. That "
        "sword is undecorated and ordinary — it is NOT the lost Volume 3 ninjato and carries none "
        "of its design features. His red plate armour is clean and fully repaired. ")
EMS_OFF = ("His right eye stays hidden behind his long right bang; the visible left eye carries NO "
           "six-bladed pattern — the Eternal Mangekyō is INACTIVE everywhere on this page. ")
MEI_WORK = ("The auburn-haired woman wears her practical dark reconstruction-era Kiri work clothes "
            "— no ceremonial kage robes, no kage hat, no escort and no guards anywhere. ")
DAMAGE = ("In that remembered image only, his red plate armour is BATTLE-DAMAGED: cracked lacquer, "
          "a split shoulder plate, dust and scorch marks — but no wounds and no blood. ")

L_STREET = ("Lighting: clean pale mist-filtered late-afternoon daylight over a rebuilding village "
            "under scaffolds, the fog thin and high. ")
L_GATE = ("Lighting: cold flat overcast light, dense white sea mist swallowing everything distant, "
          "wet stone reflections underfoot. ")
L_ROAD = ("Lighting: low late-afternoon light through thinning mist on a wooded road, long soft "
          "shadows lying to the left. ")
L_NIGHT = ("Lighting: hard cold blue moonlight falling through branches onto dry dark earth, deep "
           "hard shadows, no campfire and no warm light source. ")
L_SEAL = ("Lighting: warm red-gold seal light rising off shallow black reflective water; no sky, "
          "no horizon, no weather and no hard exterior shadows. ")

PAGES = [
 # ---- Spread 1: the place beside him -----------------------------------------------
 ("p01", dict(scene="dialogue", light="day", cast="small_group", mood="somber", panels=6),
  FILL + RTL + JIR.format(i=1) + KAK.format(i=2) + SASUKE16.format(i=3) + YUGAO_V4.format(i=4)
  + ENV_STREET.format(i=5)
  + ONLY(SAGE, MAN, SAS16, YUG,
         "a few Kiri workers seen only as small blurred distant figures far behind the group, none "
         "of them named or recurring") +
  "SIX panels. The blond teen they are discussing has ALREADY GONE and must NOT be drawn anywhere "
  "on this page, in any panel, in the foreground or the background. The empty space he left is the "
  "subject.\n"
  "PANEL 1 (shallow strip across the top, full width): wide eye-level establishing shot on the "
  "rebuilding Kiri street. The big white-haired man stands in the foreground at screen-RIGHT facing "
  "the empty screen-LEFT; the masked silver-haired man, the older dark-haired teen and the "
  "purple-haired kunoichi remain clustered behind him at centre-right. The ENTIRE LEFT HALF of this "
  "panel stays open and unoccupied — nobody has crossed into it. Inside that open left half, reserve "
  "a bounded rectangle of clear negative space: no figure, effect, balloon, tail or eye-line may "
  "enter it, and it carries only the chapter marker.\n"
  "PANEL 2 (upper right, tall vertical): medium shot — the purple-haired kunoichi turns away from "
  "the empty space back toward the others, shoulders squared, one hand still half-raised in the "
  "direction he left.\n"
  "PANEL 3 (upper left, tall vertical): close shot — her raised hand lowering. Her lower face stays "
  "in frame at the top of the panel so the balloon tail has a mouth to reach.\n"
  "PANEL 4 (middle band, full width): wide shot — the same centre-right cluster behind the "
  "white-haired man, unchanged. The older dark-haired teen shifts only his eye-line toward the "
  "kunoichi; he does not change sides and does not move into the open left half. The masked "
  "silver-haired man watches from behind her shoulder. NO balloon and NO tail may enter the empty "
  "left half of this panel.\n"
  "PANEL 5 (lower right, square): medium two-shot — the kunoichi meets the dark-haired teen's eye "
  "rather than looking at the masked man.\n"
  "PANEL 6 (bottom left, wide): medium-long shot — the group stays concentrated on the right. The "
  "kunoichi stands at the left edge of that cluster and looks off into the still-empty left half "
  "toward the route he took; the masked man, the dark-haired teen and the white-haired man remain "
  "behind and to her right. " + L_STREET +
  'LETTERING: in the protected rectangle of clear negative space in PANEL 1, write the chapter '
  'marker in bold upright English capitals on one line: "CHAPTER 5 — GOODBYE, MIZUKAGE". It is a '
  'tail-less title, not a balloon, and nothing overlaps it. '
  + SAY((2, YUG, "upper right", "WHEN I SAID TO STOP TRYING TO FORCE HIM BACK TO KONOHA..."),
        (3, YUG, "upper left", "I LEFT OUT THE PART WHERE SOMEONE SHOULD GO WITH HIM."),
        (4, SAS16, "upper centre-right, directly above the right-side cluster", "I DON'T THINK HE WOULD HAVE AGREED."),
        (5, YUG, "upper right", "IF I HAD OFFERED, HE MIGHT HAVE."),
        (6, YUG, "upper centre, directly above her", "HE NEEDS SOMEONE AT HIS SIDE."))
  + "The PANEL 5 balloon reads exactly \"IF I HAD OFFERED, HE MIGHT HAVE.\" with OFFERED spelled "
    "O-F-F-E-R-E-D — one letter O, then two letter F's, then E-R-E-D. It is never OFEERED, OFERED "
    "or OFFEERED. Letter every balloon on this page once, with no doubled, ghosted or overprinted "
    "text and no invented or dropped letters inside any word. ",
  R("jiraiya", "kakashi", "sasuke_16", "yugao_v4", "env_mizukage_tower"),
  "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + RTL + KAK.format(i=1) + YUGAO_V4.format(i=2) + SASUKE16.format(i=3) + JIR.format(i=4)
  + N16_ARMOR.format(i=5) + ENV_STREET.format(i=6)
  + ONLY(MAN, YUG, SAS16, SAGE,
         "the blond older teen in red armour, appearing ONLY inside one soft desaturated remembered "
         "battlefield image behind her in panel 3 and never physically present on this street")
  + DAMAGE +
  "SIX panels. The group pulls the personal claim out of her practical argument.\n"
  "PANEL 1 (upper right): close-up — the masked silver-haired man's visible eye curved with "
  "restrained teasing, looking down-left toward the kunoichi off-panel.\n"
  "PANEL 2 (upper left): close-up — the purple-haired kunoichi looks right at him, a slight flush "
  "high on her cheeks. This is composure cracking, NOT a comic outburst: her mouth stays small and "
  "her eyes stay open normally.\n"
  "PANEL 3 (dominant middle band, full width, the focal panel): tight three-quarter view of the "
  "kunoichi looking LEFT, away from the masked man. Behind her, occupying the upper background "
  "only, floats a soft desaturated remembered fragment of the final battlefield with the blond "
  "older teen in his cracked, scorched red armour — clearly a memory image with drained colour and "
  "soft edges, not a person standing on this street.\n"
  "PANEL 4 (lower right, tall vertical): medium shot — the older dark-haired teen folds his arms "
  "and looks left toward her, calm rather than mocking.\n"
  "PANEL 5 (lower middle, narrow vertical): close shot — the dark-haired teen's eye steady, mouth "
  "moving; the big white-haired man's irritated profile pushes in at the right edge of the panel.\n"
  "PANEL 6 (bottom left, wide): medium-long shot — the white-haired man turns the group back into "
  "Kiri toward reader-RIGHT; the masked man and the dark-haired teen follow that rightward "
  "movement. The kunoichi begins to follow but takes one last look back LEFT toward the route he "
  "took. " + L_STREET
  + SAY((1, MAN, "upper right", "IS YUGAO-CHAN WORRIED ABOUT NARUTO?"),
        (2, YUG, "upper left", "IF YOU HAD SEEN HIM IN THE CIVIL WAR, YOU WOULD BE WORRIED."),
        (3, YUG, "upper right", "HE IS RECKLESS WHEN HE CHARGES AN OPPONENT."),
        (4, SAS16, "upper right", "YOU SAID HE WAS STRONGER THAN JIRAIYA-SAMA."),
        (5, SAS16, "upper left", "I DOUBT ANYTHING WILL HAPPEN TO HIM."),
        (6, SAGE, "upper right", "COME ON. LET'S GO HOME."))
  + "EVERY balloon on this page carries a visible tail that reaches its named speaker's mouth; "
    "not one of them is tail-less. The PANEL 3 balloon \"HE IS RECKLESS WHEN HE CHARGES AN "
    "OPPONENT.\" is spoken by the purple-haired kunoichi at PANEL-LEFT, so its tail runs down and "
    "LEFT to HER mouth. It must not touch, overlap or point into the soft desaturated remembered "
    "battlefield fragment in the upper background — the blond teen inside that memory image is a "
    "picture, not a speaker, and no balloon on this page may tail to him. The PANEL 6 balloon "
    "\"COME ON. LET'S GO HOME.\" is spoken by the BIG WHITE-HAIRED MAN WITH THE ENORMOUS SPIKY "
    "WHITE MANE AND THE TWO RED FACE LINES: draw a tail that travels all the way to HIS mouth, "
    "however far across the panel he stands, and never a stub ending on the masked silver-haired "
    "man or on anyone else who happens to be nearer the balloon. ",
  R("kakashi", "yugao_v4", "sasuke_16", "jiraiya", "naruto_v4_armor", "env_mizukage_tower"),
  "low"),

 # ---- Spread 2: intercepted at the mist ---------------------------------------------
 ("p03", dict(scene="establishing", light="day", cast="crowd", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + KIRI_REBELS.format(i=2) + ENV_STREET.format(i=3)
  + ENV_GATE.format(i=4)
  + ONLY(BOY16, "Kiri workers and civilians rebuilding the street, seen only as small unnamed "
         "background figures who never approach him and never recur") + GEAR + EMS_OFF +
  "FIVE panels. He leaves the village he freed without giving anyone another goodbye. Image 3 is "
  "the street in panels 1-3; Image 4 is the gate and the road outside it in panels 4-5.\n"
  "PANEL 1 (wide top establishing panel, full width): extreme-wide eye-level street shot — Kiri "
  "still under scaffolds in late afternoon, workers and civilians small in the background. The "
  "blond older teen crosses the FOREGROUND from right to left in clean repaired red armour, the "
  "gunbai strapped across his back.\n"
  "PANEL 2 (upper middle right): medium shot — he passes a rebuilt doorway. Two background workers "
  "notice him and turn their heads; he does not stop, does not look at them, and they do not "
  "approach.\n"
  "PANEL 3 (upper middle left): low ground-level shot, NO faces — his boots crossing wet stone from "
  "right to left, with the lower edge of the gunbai, the armour skirt, and the plain sash sword at "
  "his left hip all clearly readable in the same frame.\n"
  "PANEL 4 (lower right, tall panel): medium-long shot — the village gate stands open onto dense "
  "white mist. He is a dark vertical figure walking into it, face held in profile.\n"
  "PANEL 5 (bottom left, wide): wide shot from OUTSIDE the gate — he advances left along the empty "
  "road while Kiri recedes behind him on the right, already softening in the mist. " + L_GATE
  + CAP(1, "upper right", "A FEW MINUTES LATER.")
  + "That single caption box is the ONLY text anywhere on this page. There are no speech balloons, "
    "no thought balloons, no sound effects and no signs on any panel; any writing visible on the "
    "scaffolding or the gate is ILLEGIBLE SCRIBBLE, not readable words. ",
  R("naruto_v4_armor_sword", "kiri_rebel_mob", "env_mizukage_tower", "env_kiri_mist_gate"),
  "medium"),

 ("p04", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + MEI_V4.format(i=2) + ENV_GATE.format(i=3)
  + ONLY(BOY16, MEI) + GEAR + EMS_OFF + MEI_WORK +
  "FIVE panels. She stops him with a private grievance, not with authority.\n"
  "PANEL 1 (upper right, wide): medium-long shot — the blond older teen continues LEFT along the "
  "misted road with his back to Kiri. The auburn-haired woman is NOT DRAWN in this panel at all; "
  "her voice arrives from behind him, off the right edge.\n"
  "PANEL 2 (upper left, narrow vertical): low insert, NO faces — his forward boot stopped in the "
  "air before touching the road, mist still streaming past it to the left.\n"
  "PANEL 3 (middle right, tall vertical): medium shot — the auburn-haired woman enters from the far "
  "right of frame and walks briskly left toward him in her practical dark work clothes.\n"
  "PANEL 4 (middle left, tall vertical): close shot — he turns his head and shoulders back to the "
  "right. A small, genuine smile begins at his mouth only; it does not reach or light his eye.\n"
  "PANEL 5 (dominant bottom panel, full width, the focal panel): eye-level two-shot — he stands on "
  "the LEFT facing right, she stands on the RIGHT facing left, with two full strides of empty "
  "misted road still between them. Their eye-line runs cleanly across the panel with nothing "
  "crossing it. " + L_GATE
  + SAY((1, OFF(MEI), "upper right", "I'M SO HURT THAT YOU WERE LEAVING WITHOUT EVEN SAYING GOODBYE."),
        (3, MEI, "upper right", "I HAD TO HEAR FROM MY MEN THAT YOU WERE LEAVING."),
        (5, BOY16, "upper left", "I DID NOT THINK MY DEPARTURE WOULD HURT YOU.")),
  R("naruto_v4_armor_sword", "mei_v4", "env_kiri_mist_gate"),
  "low"),

 # ---- Spread 3: no return promised ---------------------------------------------------
 ("p05", dict(scene="dialogue", light="overcast", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + MEI_V4.format(i=2) + ENV_GATE.format(i=3)
  + ONLY(BOY16, MEI) + GEAR + EMS_OFF + MEI_WORK +
  "FIVE panels. She names what she wants, and he lets her close the distance without pretending he "
  "started it.\n"
  "PANEL 1 (wide top panel, full width): medium-long two-shot — she crosses the first stride from "
  "right to left; he stays at the left edge of frame, shoulders open but entirely unmoving.\n"
  "PANEL 2 (upper middle, close-up): close-up on him — he looks right at her with a trace of "
  "amusement, not surprise.\n"
  "PANEL 3 (middle right, narrow vertical): insert, NO faces — the hem of her dark work coat "
  "sweeping left through the mist as she crosses the second stride.\n"
  "PANEL 4 (middle left, narrow vertical): insert, NO faces — his gloved hand hanging relaxed "
  "beside his red armour. It neither reaches out nor withdraws.\n"
  "PANEL 5 (dominant bottom panel, full width): close profile two-shot — she now stands one inch "
  "from him, on the RIGHT facing left; he is on the LEFT facing right. Both profiles and the "
  "eye-line between them are completely unobstructed, and the mist ABOVE their heads is left empty "
  "and quiet — nothing may be drawn or lettered in it. " + L_GATE
  + SAY((1, MEI, "upper right", "YOU WERE LEAVING WITHOUT ME GIVING YOU A GOODBYE KISS."),
        (2, BOY16, "upper left", "IT SEEMS THAT WAY.")),
  R("naruto_v4_armor_sword", "mei_v4", "env_kiri_mist_gate"),
  "low"),

 ("p06", dict(scene="emotional_closeup", light="overcast", cast="two", mood="somber", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + MEI_V4.format(i=2) + ENV_GATE.format(i=3)
  + ONLY(BOY16, MEI) + GEAR + EMS_OFF + MEI_WORK +
  "FIVE panels. The refusal to promise a return lands immediately BEFORE she acts, so nothing that "
  "follows can read as a promise.\n"
  "PANEL 1 (upper right): close-up on her eyes — she looks left into his.\n"
  "PANEL 2 (upper left): close-up on his eyes and upper face, gaze directed right. His visible left "
  "eye shows the ORDINARY three-tomoe Sharingan: a red iris with three small black comma marks and "
  "nothing else. No six-bladed pattern anywhere.\n"
  "PANEL 3 (middle right, small panel): close shot — she absorbs the answer without stepping back. "
  "Her eyes soften while her mouth sets with decision.\n"
  "PANEL 4 (middle left, small panel): close shot — she closes her eyes and begins to lean left. He "
  "stays still, eyes on her.\n"
  "PANEL 5 (dominant bottom panel, full width, the focal panel): their two profiles fill the frame. "
  "Her lips are a breath from his and HAVE NOT TOUCHED. She is on the RIGHT moving left with the "
  "reading direction; he is on the LEFT. Restrained and quiet: no embrace, no body contact, no "
  "sexualized framing. " + L_GATE
  + SAY((1, MEI, "upper right", "WHEN WILL YOU RETURN?"),
        (2, BOY16, "upper left", "I HAVE NO PLANS TO RETURN HERE."))
  + "PANEL 5 IS THE FOCAL PANEL AND ITS DISTANCE IS FIXED: the two heads FILL the panel in tight "
    "profile and their faces are ALMOST TOUCHING — her lips are one breath, a centimetre or two, "
    "from his and have NOT made contact. Their noses nearly meet and their profiles overlap at "
    "the edges of the frame. This is an extreme close-up of two faces, not a shot of two people "
    "standing apart: there is NO street between them, NO gap wide enough to see through, and the "
    "village gate, the road, the mist bank and every piece of background architecture are "
    "completely OUT OF FRAME behind their heads. The distance across the chapter only ever "
    "closes: page 5 ended one inch apart, this panel is a breath apart, and page 7 is contact. "
    "Never re-open the gap. ",
  R("naruto_v4_armor_sword", "mei_v4", "env_kiri_mist_gate"),
  "low"),

 # ---- Spread 4: one moment, then departure -------------------------------------------
 ("p07", dict(scene="emotional_closeup", light="overcast", cast="two", mood="calm", panels=4),
  FILL + RTL + N16_SWORD.format(i=1) + MEI_V4.format(i=2) + ENV_GATE.format(i=3)
  + ONLY(BOY16, MEI) + GEAR + EMS_OFF + MEI_WORK +
  "FOUR panels. THE CHAPTER'S FOCAL PAGE. ENTIRELY SILENT — no balloons, no captions, no thought "
  "balloons, no sound effects, no text of any kind anywhere on this page. She initiates; he returns "
  "it briefly; he decides when it ends.\n"
  "PANEL 1 (narrow strip across the top, full width): close profile two-shot — she completes the "
  "last fraction of movement from right to left. His eyes close only at the instant of contact.\n"
  "PANEL 2 (dominant BORDERLESS panel occupying roughly two-thirds of the page, the focal panel): "
  "clean side-profile close-up of one brief CLOSED-MOUTH goodbye kiss. She remains on the RIGHT, he "
  "remains on the LEFT. Tender but restrained: mouths closed, no tongues, no bodies pressed "
  "together, no embrace, no sexualized framing, no spectators and no background crowd. The panel "
  "has no ruled border — it bleeds softly into the surrounding mist.\n"
  "PANEL 3 (lower right, small panel): close insert — his gloved hand comes to her UPPER ARM as he "
  "returns the kiss for a single beat. The angle must clearly show reciprocal contact, not passive "
  "surprise.\n"
  "PANEL 4 (bottom left, wide panel): medium close-up — the SAME hand now applies gentle distance "
  "at her upper arm. Their lips have separated and their torsos never touched. Her eyes open; his "
  "face is composed. " + L_GATE,
  R("naruto_v4_armor_sword", "mei_v4", "env_kiri_mist_gate"),
  "high"),

 ("p08", dict(scene="emotional_closeup", light="overcast", cast="two", mood="somber", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + MEI_V4.format(i=2) + ENV_GATE.format(i=3)
  + ONLY(BOY16, MEI) + GEAR + EMS_OFF + MEI_WORK +
  "FIVE panels. He gives her a warm image of himself and no commitment whatsoever.\n"
  "PANEL 1 (upper right): close two-shot — a breath of space remains between them. She looks left "
  "at him, surprised by the reciprocation; he looks right at her.\n"
  "PANEL 2 (upper left): close-up on him — a warm, SMALL smile, entirely unlike his public "
  "impassiveness. It is quiet and closed-mouthed, never a broad grin and never open-mouthed.\n"
  "PANEL 3 (middle band, full width): medium-long shot — he turns away and resumes moving right to "
  "left. She stays fixed on the right; only her eye-line follows him left.\n"
  "PANEL 4 (lower right, tall panel): long shot — his figure diminishing in the mist, with the "
  "gunbai, the plain sash sword and his long blond hair still readable as three separate "
  "silhouettes.\n"
  "PANEL 5 (dominant lower left panel): wide shot — she stands alone at the edge of Kiri. His "
  "silhouette vanishes at the far left, leaving only white mist between her and the panel edge. Her "
  "expression is warmed by what happened: not triumphant, not tearful. " + L_GATE
  + SAY((2, BOY16, "upper left", "GOODBYE, GODAIME MIZUKAGE.")),
  R("naruto_v4_armor_sword", "mei_v4", "env_kiri_mist_gate"),
  "low"),

 # ---- Spread 5: the mist becomes a dream ---------------------------------------------
 ("p09", dict(scene="establishing", light="dusk", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + N16_BLACK.format(i=2) + ZET.format(i=3)
  + GUNBAI_V4.format(i=4) + ENV_ROAD.format(i=5) + ZOR
  + ONLY(BOY16, ZETSU) + EMS_OFF +
  "FIVE panels. ENTIRELY SILENT — no balloons, no captions, no thought balloons, no sound effects, "
  "no text of any kind anywhere on this page.\n"
  "IMAGES 1 AND 2 ARE THE SAME PERSON in two different states of dress: use Image 1's armoured "
  "state in PANELS 1-4, and Image 2's black under-layer state in PANEL 5 only. Never mix them "
  "inside one panel.\n"
  "PANEL 1 (wide top panel, full width): extreme-wide travelling shot — beyond Kiri the white mist "
  "thins into a wooded road. He walks right to left at an even pace in repaired red armour with the "
  "gunbai on his back and the plain sash sword at his hip. Kiri is no longer visible anywhere.\n"
  "PANEL 2 (upper middle right): medium shot — the plant creature rises soundlessly straight out of "
  "the earth AHEAD of him, at the left side of the panel. He continues toward it without surprise "
  "and without breaking stride.\n"
  "PANEL 3 (upper middle left): medium-long two-shot — the two of them move together from right to "
  "left, the armoured teen one half-step ahead. Neither looks back.\n"
  "PANEL 4 (lower right, narrow landscape panel): long shot — the same two silhouettes crossing a "
  "ridge as the late-afternoon light lowers behind them.\n"
  "PANEL 5 (dominant lower left panel): NIGHT at a quiet forest stopping point. He sits on a dark "
  "travel blanket with his back against a tree, wearing ONLY the fitted black high-neck under-layer "
  "— no armour on his body, no sword at his belt. ALL of his gear is locked at SCREEN-LEFT of him "
  "within arm's reach and laid out in this exact order: the folded repaired red armour is the "
  "nearest object to him; BEHIND it, resting separately and both FULLY VISIBLE, are the plain "
  "straight sash sword and the dark purple gunbai. None of the three silhouettes overlaps another "
  "or overlaps him. The plant creature stays partially merged into another trunk at the FAR RIGHT, "
  "watching the road. There is no campfire, no lamp and no signpost. " + L_NIGHT
  + "PANEL 2 AND PANEL 3 ARE CAUSE AND EFFECT AND MUST NOT BE SWAPPED. In the upper-middle row "
    "PANEL 2 — the plant creature rising out of the bare earth ahead of the still-alone armoured "
    "teen — is the RIGHT-hand panel and is read FIRST. PANEL 3 — the two of them already walking "
    "together side by side — is the LEFT-hand panel of that same row and is read SECOND. The "
    "creature is never already walking beside him in a panel that sits to the right of the panel "
    "where it emerges from the ground. ",
  R("naruto_v4_armor_sword", "naruto_v4_black", "zetsu", "gunbai_v4", "env_wave_forest"),
  "medium"),

 ("p10", dict(scene="establishing", light="dark", cast="two", mood="somber", panels=5),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + N13.format(i=4)
  + KUSHINA_PARTIAL.format(i=5) + ENV_ROAD.format(i=6) + ENV_SEAL.format(i=7) + ZOR
  + ONLY(BOY16, ZETSU,
         "the YOUNGER blond boy, who appears ONLY inside the dream-memory of panels 4 and 5 and is "
         "never physically present at the camp",
         "one unidentified woman who enters the extreme right edge of panel 5 ONLY as a lock of "
         "very long red hair and the beginning of a bare forearm — no face, no head, no shoulder "
         "and no body may be visible, and she appears nowhere else on this page") + EMS_OFF +
  "FIVE panels. ENTIRELY SILENT — no balloons, no captions, no thought balloons, no sound effects, "
  "no text of any kind anywhere on this page.\n"
  "PANELS 1-2 ARE THE WAKING WORLD (Image 6). PANELS 3-5 ARE A DREAM INSIDE HIS OWN SEALED MIND "
  "(Image 7), not a place he has travelled to: a flooded mindscape with no sky, no horizon, no "
  "weather and no forest.\n"
  "PANEL 1 (wide top panel, full width): high wide shot — later the same night, the present-day "
  "blond teen lies ASLEEP beneath the same tree on the same dark blanket, still wearing only the "
  "black under-layer. Reproduce PAGE 9 PANEL 5's exact gear coordinates at SCREEN-LEFT of him: the "
  "folded repaired red armour nearest him, and behind it the plain straight sash sword and the dark "
  "purple gunbai lying separately and both fully visible. Do not flip, reorder, overlap, crop or "
  "move any of those three objects. The plant creature is a distant, motionless silhouette at the "
  "far right edge.\n"
  "PANEL 2 (upper middle, close-up): extreme close-up on his closed eye and relaxed brow. No sweat, "
  "no tears, no strain yet.\n"
  "PANEL 3 (middle BORDERLESS strip, full width): a transition image with NO characters at all — "
  "white travel mist flows across the panel and then darkens beneath itself into shallow black "
  "seal-water. The forest dissolves as the BROKEN edge of the opened inner gate rises at "
  "SCREEN-RIGHT; torn seal paper and faint seal script drift through red-gold chakra light. There "
  "is no intact cage, no bars and no fox. All seal script is ILLEGIBLE SCRIBBLE, not readable "
  "words.\n"
  "PANEL 4 (lower right, gutters softened or absent): medium shot inside the dream — the YOUNGER "
  "blond boy stands at SCREEN-LEFT in his dark training layers, body angled right across the "
  "shallow black water. The broken gate edge and the red-gold seal script remain at SCREEN-RIGHT. "
  "He looks right toward someone still outside the frame. The present-day armoured teen does NOT "
  "enter the dream and is not drawn here.\n"
  "PANEL 5 (dominant lower left panel, the focal panel): closer shot inside the dream — the younger "
  "boy remains at SCREEN-LEFT facing right as his practised stillness opens into recognition. From "
  "the EXTREME RIGHT EDGE, only a lock of very long red hair and the beginning of a woman's bare "
  "forearm reach leftward toward him. NO face, NO head and NO body may be shown, and the embrace "
  "has not begun. Shallow black water, the broken gate edge, faint illegible seal script and "
  "red-gold light stay continuous. " + L_SEAL,
  R("naruto_v4_black", "zetsu", "gunbai_v4", "naruto_13", "minato_kushina",
    "env_wave_forest", "env_inner_sewer"),
  "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch05" / "raw", HERE / "v5ch05" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
