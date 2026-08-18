"""Volume 5, Chapter 8 — "A New Sound". 20 pages.

Source: fic ch14:373-659. Translated 1:1 from story/volume_05/drafts/ch08_a_new_sound.md —
every balloon, location card, chapter marker and sound effect appears here with its exact panel,
position and wording. Reading order is RIGHT TO LEFT; every multi-panel page states it.

Continuity inherited from Chapter 7: the Earth Country hideout is left STANDING, Zetsu carries
the wrapped Shinigami mask and Kusanagi, Naruto carries the gunbai and his own distinct plain
sash sword, and his left forearm is bruised and numb.

NOTE ON MISSING REFERENCE SHEETS: Guren, Yukimaru's mother and the Kusa/Oto rank-and-file have
no reference images in refs/images. Guren is therefore bound by full written description on
every page she appears on, the same way the Root agents were handled in v5ch01 p03.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import (CAP, ENV, FILL, JIR, KAB, KAK, MAN, OFF, ONLY, ORO,  # noqa: E402
                     R, SAGE, SAY, SFX, ZET)
from prompts_v4 import (MANGEKYO_EYE, N16_SPEAKER, N16_SWORD, SASUKE16,  # noqa: E402
                        SASUKE16_SPEAKER, TSUNADE, TSUNADE_SPEAKER, YUGAO_V4,
                        YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")

# ---------------------------------------------------------------- names used in balloon tails
NAR = N16_SPEAKER
ZETSU = "the split black-and-white plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")
YUG = YUGAO_V4_SPEAKER
TSU = TSUNADE_SPEAKER
SASU = SASUKE16_SPEAKER

# ---------------------------------------------------------------- cast without reference sheets
GUREN_D = ("Guren — she has NO reference sheet and must be drawn from this description alone: an "
           "adult woman in her mid-twenties with straight LIGHT BLUE hair cut level with her jaw "
           "and a long fringe swept across her forehead, sharp pale blue eyes, a fitted dark "
           "sleeveless combat top over a mesh undershirt, a wide belt, dark trousers and shin "
           "wraps. Her expression is hard and unsmiling. She is the only person in this chapter "
           "with light blue hair")
GUREN = "the light-blue-haired woman"
# Page-QA gate on ch08 p19 found her drawn with a blunt straight fringe and both eyes clear,
# breaking the design she carries on p10-p18 and p20. Locked on every page she appears on.
GUREN_HAIR = ("GUREN'S HAIR IS LOCKED AND IDENTICAL IN EVERY PANEL OF THIS PAGE: straight LIGHT "
              "BLUE hair cut level with the jaw, and a LONG SWEPT FRINGE that falls diagonally "
              "across her forehead in one heavy sheet, its points reaching past her eyebrow and "
              "partly covering one eye. She NEVER has a blunt straight fringe cut level across "
              "the brow, and she is never drawn with both eyes fully clear of hair. ")
# Same gate: the room she occupies after Tsukuyomi (p13-p18) came back as a chemistry laboratory
# instead of the scroll-rack office established on p10. One description, restated on every page.
OFFICE = ("THE ROOM IS THE SAME OFFICE ESTABLISHED EARLIER AND NEVER CHANGES: a windowless "
          "underground room with cracked dark stone walls and one bare hanging bulb, ONE BROAD "
          "WOODEN DESK with an open ledger and rolled scrolls lying on it, tall WOODEN RACKS OF "
          "SCROLLS AND BOUND RECORD FILES filling the wall behind the desk, a metal record "
          "cabinet, and one heavy door. IT IS NOT A LABORATORY: there are NO metal counters, NO "
          "sink or taps, NO chemical bottles, NO glassware, NO tubing and NO specimen jars "
          "anywhere in it. ")
MOB = ("Image {i} shows ordinary civilian archetypes. Use these faces, builds and everyday clothes "
       "for the unnamed people on this page. Ignore its white background and lineup layout. ")
GUARDS_D = ("two anonymous Kusa gate guards in plain dark hideout uniforms, faces ordinary and "
            "unremarkable, never resembling any named character")
GUARD_L = "the left-hand gate guard"
CAPTIVES_D = ("unaltered civilian captives — ordinary adults and children in plain worn clothing "
              "behind bars, with no mutations, no markings and no injuries")
SOUND2_D = ("two trusted Sound shinobi in plain dark uniforms, anonymous and never resembling any "
            "named character")
MEMORY_D = ("Yukimaru's mother and a much younger Guren appearing ONLY inside one borderless "
            "memory image, never in the present-day room: the mother a gentle-faced dark-haired "
            "woman sheltering an unconscious blue-haired girl")
S4_DEAD = ("the four dead Sound guards, appearing ONLY inside one borderless evidence image and "
           "drawn from this description alone: a very large orange-crested boy, a red-haired girl "
           "in a horned black cap, a slender grey-blue-haired youth and a lean dark-skinned youth "
           "with a topknot, all of them motionless and unmarked")

# ---------------------------------------------------------------- state locks
GEAR = ("His red segmented armour is clean, the Leaf forehead protector is partly visible, the "
        "dark purple gunbai stays strapped flat across his back in every panel, and his own PLAIN "
        "STRAIGHT SASH SWORD stays sheathed at his LEFT hip. That plain sword is never Kusanagi "
        "and is never exchanged for it. ")
ARM = ("His LEFT forearm is bruised and numb: it hangs guarded close to his torso, he never grabs "
       "or blocks with it, and it carries no open wound and no blood. ")
CARRY = ("The plant creature carries TWO separate objects that never leave its control and never "
         "merge: a cloth-wrapped bundle holding a pale horned demon mask, and a long thin "
         "sheathed sword. Both are clearly different objects from the blond teen's own sword. ")
NOTEXT = ("Any writing that appears on architectural plans, office papers, records, labels or "
          "signs anywhere on this page is ILLEGIBLE SCRIBBLE, not readable words. ")
FLAT = ("All chakra, killing intent and genjutsu effects are FLAT OPAQUE shapes with hard black "
        "outlines. They do NOT glow and do NOT wash the scene out: the room, the furniture and "
        "every figure stay fully drawn and legible through and around them. ")

# ---------------------------------------------------------------- light
L_ROCK = "Lighting: clean early Earth Country daylight on dry grey rock, hard black shadows. "
L_RIDGE = "Lighting: broad flat daylight over open empty country, a high pale sky, long horizon. "
L_KONOHA = "Lighting: warm clear village daylight, soft green shade under the roof lines. "
L_OFFICE = "Lighting: warm late-morning light slanting through tall office windows. "
L_ROOF = "Lighting: bright open daylight over tiled rooftops, hard shadow under every eave. "
L_CELL = ("Lighting: dim underground lamp light in a stone corridor — hard pools of light with "
          "flat black between them. ")
L_DESK = ("Lighting: one hard lamp over a working desk in a windowless stone office, the corners "
          "falling into flat black. ")
L_VOID = ("Lighting: no environment light at all — an endless BLOOD-RED and black field with no "
          "floor, no horizon and no scenery, the figures lit flat and evenly. ")

PAGES = [
 # ---- Spread 1: the base is more valuable intact -----------------------------------
 ("p01", dict(scene="establishing", light="day", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ZOR
  + ONLY(NAR, ZETSU) + GEAR + ARM + CARRY +
  "FIVE panels. The first constructive act of the chapter is NOT destroying something.\n"
  "PANEL 1 (narrow strip across the top, full width): wide exterior in early daylight. The INTACT "
  "stone mouth of a cliff hideout fills the right third — undamaged, unsealed, nothing burning. "
  "The blond teen has already crossed to centre-left and is moving further LEFT along the path, "
  "his left forearm held close to his torso. The plant creature emerges from the ground behind "
  "him at the right, carrying the wrapped bundle and the long thin sheathed sword. Their "
  "eye-lines do not meet. The UPPER LEFT of this panel is CLEAN EMPTY SKY — no head, weapon, "
  "smoke or high-contrast rock may cross it — and carries only the chapter marker.\n"
  "PANEL 2 (small inset, upper right of the second row): view back over the teen's shoulder "
  "through the entrance — dark laboratory benches, sealed cabinets and shelves of scrolls "
  "receding into the base. Nobody is inside. No text in this panel.\n"
  "PANEL 3 (middle row, RIGHT — read first): medium profile two-shot — the teen at the LEFT still moving left, "
  "the creature one pace behind at the RIGHT with its face turned back toward the base. The "
  "teen's mouth is visible.\n"
  "PANEL 4 (middle row, LEFT — read after panel 3): the creature closes the gap and turns its head toward the teen; "
  "the teen keeps his eyes forward. Both mouths are visible.\n"
  "PANEL 5 (deep wide panel across the bottom): the path narrows between rock walls. The teen is "
  "foreground LEFT, the creature midground RIGHT, and the intact entrance is now small behind "
  "them both. Both faces stay large enough for their mouths to read. " + L_ROCK +
  'LETTERING: in the protected CLEAN EMPTY SKY at the upper left of PANEL 1, write the chapter '
  'marker in bold upright English capitals on one line: "CHAPTER 8 — A NEW SOUND". It is a '
  'tail-less title, not a balloon. '
  + SAY((1, ZETSU, "upper right", "YOU LEFT IT STANDING."),
        (3, NAR, "upper right", "THE LABS AND RECORDS HAVE VALUE."),
        (3, NAR, "lower left", "SO DOES THE NETWORK AROUND THEM."),
        (4, ZETSU, "upper right", "YOU WANT HIS VILLAGE."),
        (4, NAR, "upper left", "I WANT WHAT IT CAN BECOME."),
        (5, ZETSU, "upper right", "WITHOUT OROCHIMARU, OTO WILL BREAK APART."),
        (5, NAR, "lower left", "THEN IT NEEDS A NEW CENTRE."))
  + "MIDDLE ROW ORDER, THE ONE THING THIS PAGE MUST GET RIGHT: PANEL 3 is the middle row's "
    "RIGHT-HAND panel and PANEL 4 sits entirely to its LEFT, so the blond teen's setup \"THE LABS "
    "AND RECORDS HAVE VALUE.\" / \"SO DOES THE NETWORK AROUND THEM.\" is read BEFORE the plant "
    "creature's inference \"YOU WANT HIS VILLAGE.\" Never place PANEL 4 to the right of PANEL 3. ",
  R("naruto_v4_armor_sword", "zetsu", "env_oto_hidden_base"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=5),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(NAR, ZETSU) + GEAR + ARM + CARRY +
  "FIVE panels. A real village is defined as infrastructure; his interest is defined as concealed "
  "strength.\n"
  "PANEL 1 (top right): frontal two-shot — the teen on the reader's LEFT and the creature on the "
  "reader's RIGHT, both still travelling left; the creature's eye-line now crosses to him. Both "
  "mouths are visible.\n"
  "PANEL 2 (top left): close on his right gloved hand counting three points off and then closing "
  "into a fist. HIS FACE AND MOUTH ARE OUTSIDE THIS PANEL.\n"
  "PANEL 3 (middle right): medium of the creature alone, intrigued rather than surprised, mouth "
  "visible. THE TEEN IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 4 (small inset, middle left): tight crop on the teen's visible left eye shifting to the "
  "road ahead. HIS MOUTH IS OUTSIDE THE CROP.\n"
  "PANEL 5 (half-page landscape across the bottom): the two of them are SMALL on a ridge, "
  "travelling left, empty open country opening ahead of them with no village anywhere in it. The "
  "teen is slightly ahead of the creature. Both are far too small for a balloon tail to reach a "
  "mouth. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "A REAL VILLAGE?"),
        (1, NAR, "upper left", "HOMES. A HOSPITAL. A SCHOOL."),
        (2, OFF(NAR), "upper right", "ADMINISTRATION. TRADE. SHINOBI WHO ANSWER TO ONE CENTRE."),
        (3, ZETSU, "upper right", "YOU ARE GOING TO BUILD IT?"),
        (3, OFF(NAR), "lower left", "NO."),
        (4, OFF(NAR), "upper left", "I NEED A LEADER OTO ALREADY KNOWS."),
        (5, OFF(ZETSU), "upper right", "AND YOU STAY INVISIBLE."),
        (5, OFF(NAR), "upper centre-left", "KONOHA DOES NOT NEED TO SEE EVERY PIECE I MOVE."),
        (5, OFF(NAR), "lower left", "A VILLAGE CAN BE POWER WITHOUT CARRYING MY NAME."))
  + "The PANEL 2 balloon reads exactly \"ADMINISTRATION. TRADE. SHINOBI WHO ANSWER TO ONE "
    "CENTRE.\" — ANSWER is spelled A-N-S-W-E-R, six letters with an N after the A. Never write "
    "ASWER, ANSER or any other form of it. ",
  R("naruto_v4_armor_sword", "zetsu"), "low"),

 # ---- Spread 2: assign the visible leader ------------------------------------------
 ("p03", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ZOR
  + ONLY(NAR, ZETSU) + GEAR + ARM + CARRY +
  "SIX panels. One name, and why it is the right one.\n"
  "PANEL 1 (top right): the creature leans forward from the RIGHT trying to catch the teen's "
  "profile; its mouth is visible.\n"
  "PANEL 2 (top left): close on the teen, face level and forward, mouth visible.\n"
  "PANEL 3 (middle right): close on the creature; the wrapped bundle and the long thin sword stay "
  "behind its shoulder and are never set down. Its expression is new information landing, not "
  "recognition of a person it already knows. Its mouth is visible.\n"
  "PANEL 4 (middle left): alternating close on the teen, mouth visible.\n"
  "PANEL 5 (narrow SILENT strip): the creature studies the teen and the teen finally meets its "
  "eye-line. His plain sash sword and guarded left forearm stay visible along the bottom edge of "
  "the panel. No text in this panel.\n"
  "PANEL 6 (wide two-shot across the bottom): both stopped at a fork in the road, the teen "
  "centre-LEFT and the creature centre-RIGHT. Both mouths are visible. " + L_RIDGE
  + SAY((1, ZETSU, "upper right", "WHO?"),
        (2, NAR, "upper left", "GUREN. SHE RUNS OROCHIMARU'S KUSA HIDEOUT."),
        (3, ZETSU, "upper right", "YOU KNOW HER?"),
        (4, NAR, "upper left", "I KNOW HER ROLE. SHE IS STRONG."),
        (4, NAR, "lower left", "OTO KNOWS HER."),
        (6, ZETSU, "upper right", "WILL SHE TURN?"),
        (6, NAR, "upper left", "SHE WILL HEAR THE OFFER."),
        (6, NAR, "lower left", "THE ANSWER MUST BE HERS.")),
  R("naruto_v4_armor_sword", "zetsu"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ZOR
  + ONLY(NAR, ZETSU) + GEAR + ARM + CARRY +
  "SIX panels. Exact assignments, then the road divides.\n"
  "PANEL 1 (wide establishing panel across the top): high three-quarter view of the fork, close "
  "enough that both faces stay readable. The LEFT branch runs toward distant wooded country; the "
  "UPPER RIGHT branch doubles back into the rocks. The teen faces left, the creature faces upper "
  "right. Both mouths are visible.\n"
  "PANEL 2 (middle right): the teen in three-quarter profile giving instructions while the "
  "creature listens from the opposite panel edge. His mouth is visible.\n"
  "PANEL 3 (middle left): the creature alone, attentive. THE TEEN IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 4 (lower right): the creature shifts the wrapped bundle and the long thin sword higher "
  "on its shoulder; its mouth is visible. THE TEEN IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 5 (lower left): close on the wrapped bundle and the long thin sword held together, with "
  "the intact cliff hideout small in the far background behind the creature's shoulder. NEITHER "
  "SPEAKER'S MOUTH IS VISIBLE in this panel.\n"
  "PANEL 6 (full-width departure panel across the bottom, SILENT): the teen walks LEFT down the "
  "left branch without looking back; the creature sinks into the earth at the far RIGHT facing "
  "the other way; the empty fork lies between them. No text in this panel. " + L_ROCK
  + SAY((1, ZETSU, "upper right", "AND KARIN?"),
        (1, NAR, "lower left", "KUSA IS ON THE WAY. SHE WAITS A FEW HOURS."),
        (2, NAR, "upper left", "GO TO OTO. SPREAD WORD THAT OROCHIMARU IS DEAD."),
        (3, OFF(NAR), "upper left", "COUNT WHO REMAINS, WHAT THEY NEED, AND WHO CAN BUILD."),
        (4, ZETSU, "upper right", "AND UZUSHIO?"),
        (4, OFF(NAR), "lower left", "SURVEY THE ISLAND. RECORD EVERYTHING. ALTER NOTHING."),
        (5, OFF(ZETSU), "upper right", "I'LL SECURE THE MASK AND KUSANAGI AT OUR HIDEOUT FIRST."),
        (5, OFF(NAR), "mid-left", "THEN RETURN AND STRIP THIS ONE."),
        (5, OFF(NAR), "lower left",
         "SECURE EVERY RECORD, SAMPLE, AND USEFUL INSTRUMENT BEFORE IWA FINDS IT."))
  + "LOWER ROW ORDER: PANEL 4 (the creature shifting the bundle and the sword higher) is the "
    "lower row's RIGHT-HAND panel and PANEL 5 (the close-up of the wrapped bundle and the long "
    "thin sword) sits entirely to its LEFT. The question \"AND UZUSHIO?\" must therefore be read "
    "BEFORE \"I'LL SECURE THE MASK AND KUSANAGI AT OUR HIDEOUT FIRST.\" Never place PANEL 5 to "
    "the right of PANEL 4. ",
  R("naruto_v4_armor_sword", "zetsu", "env_oto_hidden_base"), "low"),

 # ---- Spread 3: home turns reports into claims -------------------------------------
 ("p05", dict(scene="establishing", light="day", cast="small_group", mood="calm", panels=6),
  FILL + RTL + JIR.format(i=1) + KAK.format(i=2) + SASUKE16.format(i=3) + YUGAO_V4.format(i=4)
  + TSUNADE.format(i=5) + ENV.format(i=6) + ENV.format(i=7)
  + ONLY(SAGE, MAN, SASU, YUG, TSU) + NOTEXT +
  "SIX panels. The returning party turns events into official consequences.\n"
  "PANEL 1 (wide strip across the top): the tall village gateway in daylight. The big white-haired "
  "man leads at the far RIGHT, the masked silver-haired man and the older dark-haired teen walk "
  "at centre, and the purple-haired kunoichi is slightly separated at the far LEFT, looking into "
  "the village rather than at them. Everyone moves LEFT. The white-haired man's face is large "
  "enough for his mouth to read. The upper right stays clear for the location card.\n"
  "PANEL 2 (narrow horizontal strip, SILENT): feet and shadows only, no faces — the kunoichi's "
  "shadow hesitates for half a step, then continues. No text in this panel.\n"
  "PANEL 3 (middle right): office establishing shot — the blonde woman in the green haori sits "
  "behind a desk at the reader's LEFT; the door opens from the RIGHT and the masked man and the "
  "dark-haired teen enter first while the white-haired man appears at the window behind her. Her "
  "mouth is visible.\n"
  "PANEL 4 (middle left): her eye-line crosses the room to the kunoichi entering last at the far "
  "right. Her mouth is visible.\n"
  "PANEL 5 (lower right, taller): the kunoichi kneels at centre-right facing the desk; the masked "
  "man stands behind her with his one visible eye on her rather than on the desk. Her mouth is "
  "visible.\n"
  "PANEL 6 (lower left, tallest): closer two-shot across the desk. Both women's mouths are "
  "visible. " + L_OFFICE
  + CAP(1, "upper right", "KONOHA")
  + SAY((1, SAGE, "upper centre", "HOME AT LAST."),
        (3, TSU, "upper left", "KAKASHI. SASUKE. YOU'RE BACK."),
        (4, TSU, "upper left", "YUGAO?"),
        (5, YUG, "upper right", "MY SQUAD WAS KILLED."),
        (5, YUG, "upper centre", "NARUTO FOUND ME. I STAYED IN KIRI."),
        (6, YUG, "upper right", "I'LL GIVE ANBU A FULL REPORT."),
        (6, TSU, "upper left", "ANKO AND KURENAI WILL BE RELIEVED.")),
  R("jiraiya", "kakashi", "sasuke_16", "yugao_v4", "tsunade", "env_konoha_outskirts",
    "env_hokage_office"), "low"),

 ("p06", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + RTL + JIR.format(i=1) + KAK.format(i=2) + SASUKE16.format(i=3) + YUGAO_V4.format(i=4)
  + TSUNADE.format(i=5) + ENV.format(i=6)
  + ONLY(SAGE, MAN, SASU, YUG, TSU) + NOTEXT +
  "SIX panels. A victory abroad becomes council pressure and a first claim at home.\n"
  "PANEL 1 (top right): the white-haired man stands by the window at the reader's RIGHT; the "
  "blonde woman turns her chair toward him. His mouth is visible.\n"
  "PANEL 2 (top centre): the kunoichi in profile, still kneeling, her eye-line level now instead "
  "of lowered. Her mouth is visible.\n"
  "PANEL 3 (top left): the blonde woman pinches the bridge of her nose and looks toward a stack "
  "of council messages on the desk; her mouth stays visible below her hand. Every mark on those "
  "messages is ILLEGIBLE SCRIBBLE.\n"
  "PANEL 4 (wide band across the middle): the whole office — she gestures toward the door; the "
  "masked man and the kunoichi begin moving RIGHT toward it; the dark-haired teen stays fixed at "
  "centre. Her mouth is visible.\n"
  "PANEL 5 (tall panel, lower right): the dark-haired teen stands alone before the desk, "
  "shoulders square, eye-line straight at her. Both mouths are visible.\n"
  "PANEL 6 (tall focal panel, lower left): shot from behind the blonde woman with her face held "
  "in readable three-quarter profile; the dark-haired teen dominates the opposite side, still "
  "standing. Both mouths are visible. " + L_OFFICE
  + SAY((1, SAGE, "upper right", "THE REPORTS ARE TRUE. NARUTO ENDED YAGURA'S RULE."),
        (2, YUG, "upper right", "I SAW THE FINAL BATTLE."),
        (3, TSU, "upper left", "THEN THE ADVISERS HAVE HEARD ENOUGH TO START PLANNING."),
        (4, TSU, "upper left", "KAKASHI, SASUKE—WELCOME HOME. YUGAO, REPORT TO ANBU."),
        (5, SASU, "upper right", "ONE REQUEST. RETURN EVERYTHING SEIZED FROM THE UCHIHA COMPOUND."),
        (5, TSU, "upper left", "I WASN'T HERE FOR THE MASSACRE."),
        (5, SASU, "lower right", "THE ADVISERS WERE."),
        (6, TSU, "upper left", "I'LL SPEAK TO THEM. ANYTHING ELSE?"),
        (6, SASU, "lower right", "ONE MATTER. IT WAITS FOR NARUTO.")),
  R("jiraiya", "kakashi", "sasuke_16", "yugao_v4", "tsunade", "env_hokage_office"), "low"),

 # ---- Spread 4: alive is not the same as reached -----------------------------------
 ("p07", dict(scene="dialogue", light="day", cast="two", mood="somber", panels=6),
  FILL + RTL + YUGAO_V4.format(i=1) + KAK.format(i=2) + ENV.format(i=3)
  + ONLY(YUG, MAN) +
  "SIX panels. He wants a personal answer; she refuses to let 'alive' be the measure.\n"
  "PANEL 1 (wide rooftop strip across the top, SILENT): village rooftops in daylight. The "
  "purple-haired kunoichi moves LEFT across the foreground; the masked silver-haired man follows "
  "one roof behind at the far right, matching her pace without calling out. No text in this "
  "panel.\n"
  "PANEL 2 (narrow panel, upper right of the second row): she stops at the left roof edge without "
  "turning; he lands behind and to her right. Both bodies face LEFT and their eye-lines do not "
  "meet. Her mouth is visible in profile.\n"
  "PANEL 3 (narrow panel in the SAME second row, immediately to the LEFT of PANEL 2 and the same "
  "height as it): he straightens but keeps one pace of distance. His "
  "cloth-mask-covered mouth is clearly shaped and visible under the fabric, and it is the tail "
  "target.\n"
  "PANEL 4 (middle left): close on her turning her head halfway; he is only a blurred shape "
  "behind her and HIS MOUTH CANNOT BE READ.\n"
  "PANEL 5 (lower right): close on her with a direct eye-line back at him. Her mouth is visible.\n"
  "PANEL 6 (lower left): close on his one visible eye opening slightly. SHE IS NOT IN THIS PANEL "
  "AT ALL. " + L_ROOF
  + SAY((2, YUG, "upper left", "YOU COULD HAVE ASKED IN THE OFFICE."),
        (3, MAN, "upper right", "I WANTED YOUR ANSWER."),
        (3, MAN, "lower right", "NOT YOUR REPORT."),
        (4, OFF(MAN), "upper right", "HOW IS HE?"),
        (5, YUG, "upper left", "ALIVE. CAPABLE."),
        (5, YUG, "lower left", "AND LONELY."),
        (6, OFF(YUG), "upper left", "HE DOESN'T KNOW IT."),
        (6, OFF(YUG), "lower left", "HE NEVER STOPS LONG ENOUGH."))
  + "SECOND ROW ORDER: PANEL 2 (the purple-haired kunoichi stopping at the roof edge) is that "
    "row's RIGHT-HAND panel and PANEL 3 (the masked man straightening) sits immediately to its "
    "LEFT, so \"YOU COULD HAVE ASKED IN THE OFFICE.\" is read BEFORE \"I WANTED YOUR ANSWER.\" / "
    "\"NOT YOUR REPORT.\" Never place PANEL 3 to the right of PANEL 2. "
    "PANEL 6 CONTAINS ONLY THE MASKED SILVER-HAIRED MAN'S FACE, and BOTH of its balloons are the "
    "purple-haired kunoichi's — she is NOT drawn in it. Each of those two balloons is an "
    "off-panel balloon whose tail is a short straight spur to the nearest panel border, pointing "
    "OUT of the panel. Neither tail may touch, cross, overlap or aim at his face, his eye or his "
    "mask; if a tail would reach him, shorten it. He does not speak in PANEL 6. ",
  R("yugao_v4", "kakashi", "env_village_street"), "low"),

 ("p08", dict(scene="dialogue", light="day", cast="two", mood="somber", panels=6),
  FILL + RTL + KAK.format(i=1) + YUGAO_V4.format(i=2) + N16_SWORD.format(i=3) + ENV.format(i=4)
  + ONLY(YUG, MAN,
         "the blond older teen appearing ONLY inside one soft borderless memory fragment, never "
         "on the rooftop") +
  "SIX panels. He is told that caring is still available to him, not that it has already worked.\n"
  "PANEL 1 (top right): the masked man looks out over the village instead of at her. His "
  "cloth-mask-covered mouth is clearly shaped and visible, and it is the tail target.\n"
  "PANEL 2 (top left): she turns fully toward him. Her mouth is visible.\n"
  "PANEL 3 (wide two-shot across the middle): she stands at the reader's LEFT on the higher roof "
  "tile, he stands at the reader's RIGHT one step lower. Her mouth and his mask-covered mouth are "
  "both visible.\n"
  "PANEL 4 (small close-up, lower right): his gloved hand tightening around a small book. HIS "
  "FACE AND MOUTH ARE OUTSIDE THIS PANEL.\n"
  "PANEL 5 (small memory fragment, lower centre, NO hard border and softly faded at the edges): "
  "the blond older teen in red armour standing in pale mist, turned partly away while speaking. "
  "It is one still image only — no new event, no reproduced dialogue, and NEITHER present-day "
  "speaker appears in it.\n"
  "PANEL 6 (half-page focal panel across the bottom): she has resumed moving LEFT but looks back "
  "over her shoulder; he stays still at the RIGHT and meets her eye-line. Both mouths are "
  "visible. " + L_ROOF
  + SAY((1, MAN, "upper right", "AT LEAST HE'S ALIVE."),
        (2, YUG, "upper left", "THAT ISN'T THE SAME AS BEING FINE."),
        (3, MAN, "upper right", "I'VE TRIED TO REACH HIM."),
        (3, YUG, "upper left", "TRY AGAIN."),
        (4, OFF(MAN), "upper right", "WHY WOULD THIS TIME BE DIFFERENT?"),
        (5, OFF(YUG), "upper left",
         "HE SPOKE OF PEOPLE PRECIOUS TO HIM. YOU WERE ONE OF THEM."),
        (6, MAN, "upper right", "YOU'RE SURE?"),
        (6, YUG, "lower left", "YES. WHEN HE RETURNS, SPEAK TO HIM.")),
  R("kakashi", "yugao_v4", "naruto_v4_armor_sword", "env_village_street"), "low"),

 # ---- Spread 5: enter without wasting what remains ---------------------------------
 ("p09", dict(scene="establishing", light="interior", cast="solo", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + MOB.format(i=3)
  + ENV.format(i=4)
  + ONLY(NAR, GUARDS_D, CAPTIVES_D) + GEAR + ARM + NOTEXT + FLAT +
  "SEVEN panels. A nonlethal entry, and the one thing inside that is not an asset.\n"
  "PANEL 1 (wide location strip across the top): a wooded ravine around a concealed stone door. "
  "The blond teen is a small figure at the far RIGHT moving LEFT toward it, red armour, gunbai, "
  "gloves, forehead protector and sheathed plain sash sword all readable, left arm held close. "
  "The upper right stays clear for the location card.\n"
  "PANEL 2 (narrow descent panel, upper right of the second row): two guards frame the doorway, "
  "one on each side; the teen enters their shared eye-line from the RIGHT. The LEFT guard's mouth "
  "is visible and is the tail target.\n"
  "PANEL 3 (narrow panel in the SAME second row, immediately to the LEFT of PANEL 2 and the same "
  "height as it): close on the teen's active red six-bladed left eye — a flat "
  "printed eye pattern, never a glow — with both guards' shapes going out of focus in the "
  "reflection. No text in this panel.\n"
  "PANEL 4 (middle right): both guards slump asleep against opposite walls as he passes between "
  "them, still moving LEFT. Neither has any wound, mark or blood. No text in this panel.\n"
  "PANEL 5 (wide interior junction panel across the middle): a stone corridor junction. Down the "
  "LEFT-hand evacuation corridor, ordinary barred cells hold unaltered civilian captives — adults "
  "and children with no mutations. On the RIGHT a separate REINFORCED door seals another wing; "
  "only distorted silhouettes show through two thick observation slits and the door stays locked. "
  "The teen walks between the two routes with his gaze forward.\n"
  "PANEL 6 (lower right): a small child's hand reaches out through a civilian cell bar from the "
  "reader's LEFT. His stride stops one step past it; his body stays facing left but his eye-line "
  "drops back to the hand. The sealed reinforced door stays visible behind his right shoulder. No "
  "text in this panel.\n"
  "PANEL 7 (SILENT close-up across the bottom): he looks from the child to the next locked cell. "
  "His face stays controlled — the pause carries the recognition, not an expression. No text in "
  "this panel. " + L_CELL
  + CAP(1, "upper right", "KUSAGAKURE — ONE DAY LATER")
  + SAY((2, GUARD_L, "upper left", "WHO ARE—"))
  + "SECOND ROW ORDER: PANEL 2 (the two guards framing the doorway, carrying the challenge \"WHO "
    "ARE—\") is that row's RIGHT-HAND panel and PANEL 3 (the close-up of the active red "
    "six-bladed left eye) sits immediately to its LEFT. The challenge must be read BEFORE the eye "
    "that interrupts it; never place the eye close-up to the right of the guards' panel. ",
  R("naruto_v4_armor_sword", "mangekyo_design", "mob_archetypes", "env_hideout_corridor"),
  "medium"),

 ("p10", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + FLAT + GUREN_HAIR + OFFICE +
  "SIX panels. She owns the room physically right up to the last panel.\n"
  "PANEL 1 (tall doorway panel down the RIGHT edge): the office door at the reader's right. The "
  "light-blue-haired woman sits behind a desk on the LEFT surrounded by scroll racks and record "
  "files; every label and every mark on them is ILLEGIBLE SCRIBBLE. The teen enters from the "
  "RIGHT without checking for traps, his plain sash sword sheathed and his left forearm close to "
  "his torso. Their eye-lines lock across the room and both mouths are visible.\n"
  "PANEL 2 (upper left): he advances to centre; she stands behind the desk with her hands planted "
  "wide on it. Both mouths are visible.\n"
  "PANEL 3 (middle right): she comes around the LEFT side of the desk toward him; he stops and "
  "lets her have the approach. Both mouths are visible.\n"
  "PANEL 4 (dominant panel, middle left and running most of the width): she seizes his collar "
  "with her RIGHT hand and pulls him half a step LEFT; he keeps the numb left forearm out of it "
  "and closes his RIGHT hand around her wrist, stopping a second pull. His sheathed plain sword "
  "stays clear of both bodies. Their faces and mouths are visible and their eye-lines are level. "
  "She is established immediately to the LEFT of him.\n"
  "PANEL 5 (narrow eye strip): her glare on the LEFT and his red six-bladed pattern forming on "
  "the RIGHT — eyes only, NEITHER MOUTH IS IN THIS PANEL.\n"
  "PANEL 6 (wide transition panel across the bottom): the office blacks out from the edges inward "
  "and flat red lines swallow the desk, while the two of them stay locked hand-to-wrist and "
  "collar at the centre, fully drawn and legible through the effect. His left forearm is still "
  "unused. His mouth is visible. " + L_DESK
  + SAY((1, GUREN, "upper left", "WHO THE HELL ARE YOU?"),
        (1, GUREN, "mid-left", "WHAT ARE YOU DOING IN MY BASE?"),
        (2, NAR, "upper right", "YOU'RE GUREN."),
        (2, GUREN, "upper left", "YOU STILL HAVEN'T ANSWERED."),
        (3, NAR, "upper right", "I CAME THROUGH THE FRONT ENTRANCE."),
        (3, GUREN, "upper left", "THAT WASN'T THE QUESTION."),
        (4, GUREN, "upper left", "GIVE ME ONE REASON NOT TO KILL YOU."),
        (4, NAR, "lower right", "I DID NOT COME TO FIGHT."),
        (5, OFF(GUREN), "upper left", "THEN YOU CAME TO THE WRONG ROOM."),
        (6, NAR, "lower right", "TSUKUYOMI.")),
  R("naruto_v4_armor_sword", "mangekyo_design", "env_orochimaru_lab"), "medium"),

 # ---- Spread 6: proof does not produce consent -------------------------------------
 ("p11", dict(scene="action", light="white_void", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + FLAT + GUREN_HAIR +
  "SIX panels. Inside the illusion. There is NO office, NO furniture, NO floor and NO horizon "
  "anywhere on this page — only flat blood-red and black space behind every figure.\n"
  "PANEL 1 (full-width establishing strip across the top): the light-blue-haired woman stands "
  "alone at centre-LEFT; the blond teen stands distant at the RIGHT. Nothing else exists in the "
  "frame. Her mouth is visible.\n"
  "PANEL 2 (upper right of the second row, SILENT): she drives left to right at him with one hand "
  "reaching for his throat. No text in this panel.\n"
  "PANEL 3 (upper left, SILENT): four identical illusion copies of the teen appear around her at "
  "the four cardinal points and catch both her wrists and both shoulders; her forward movement "
  "stops dead. No text in this panel.\n"
  "PANEL 4 (restraint panel — the RIGHT-HAND panel of the middle row; taller than it is wide, but "
  "it stays inside that one row and never spans down past PANEL 5): the four copies pull away and vanish, leaving "
  "her bound upright against a flat black cross at centre-LEFT. The real teen walks closer from "
  "the reader's RIGHT and never touches her. Her mouth is visible.\n"
  "PANEL 5 (middle left): tight two-shot — she is foreground LEFT, he is background RIGHT. Both "
  "mouths are visible.\n"
  "PANEL 6 (wide reveal panel across the bottom): he stops directly in front of her, still outside "
  "arm's reach. She pulls once against the restraints, then fixes her eye-line on him. Both "
  "mouths are visible. " + L_VOID
  + SAY((1, GUREN, "upper left", "LET ME OUT."),
        (4, GUREN, "upper left", "WHAT DO YOU WANT?"),
        (5, NAR, "upper right", "YOU."),
        (5, GUREN, "upper left", "WHAT?"),
        (5, NAR, "lower right", "YOUR POSITION. NOT YOUR BODY."),
        (6, NAR, "upper right", "I WANT YOU TO WORK WITH ME."),
        (6, GUREN, "upper left", "I WORK FOR OROCHIMARU-SAMA."),
        (6, NAR, "lower right", "OROCHIMARU IS DEAD."))
  + "MIDDLE ROW ORDER: the tall restraint panel PANEL 4 is the middle row's RIGHT-HAND panel and "
    "PANEL 5 sits entirely to its LEFT. Her question \"WHAT DO YOU WANT?\" must be read BEFORE "
    "the exchange \"YOU.\" / \"WHAT?\" / \"YOUR POSITION. NOT YOUR BODY.\" Never place PANEL 5 to "
    "the right of PANEL 4. ",
  R("naruto_v4_armor_sword"), "medium"),

 ("p12", dict(scene="emotional_closeup", light="white_void", cast="two", mood="somber", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + KAB.format(i=2) + ORO.format(i=3) + ENV.format(i=4)
  + ONLY(NAR, GUREN_D, S4_DEAD,
         "the grey-haired medic in round glasses, appearing ONLY inside one borderless evidence "
         "image, lying intact and plainly breathing",
         "the pale long-haired man, appearing ONLY inside two borderless evidence images and only "
         "in his enormous CHALK-WHITE true snake form") + GEAR + ARM + FLAT + GUREN_HAIR +
  "SEVEN panels. The proof is accurate, and it does not buy agreement.\n"
  "VIOLENCE RULE FOR THIS PAGE: the evidence images show unmoving bodies and flat black flame "
  "only — no injury detail, no blood, no gore, no wounds and no red fluid anywhere.\n"
  "PANEL 1 (top right): close on the light-blue-haired woman, fury arriving over the first beat "
  "of shock. Her mouth is visible.\n"
  "PANEL 2 (BORDERLESS evidence shard, top left): a stone throne hall with the four dead Sound "
  "guards lying motionless and unmarked across its floor. The teen's face stays visible at the "
  "LOWER RIGHT of the shard with his mouth unobscured.\n"
  "PANEL 3 (BORDERLESS evidence shard, middle right): the grey-haired medic in round glasses "
  "collapsed on stone with his eyes open and unfocused, physically intact, his chest plainly "
  "moving. NEITHER THE WOMAN NOR THE TEEN IS VISIBLE IN THIS SHARD.\n"
  "PANEL 4 (BORDERLESS evidence shard, middle left): an enormous CHALK-WHITE snake body — built "
  "out of hundreds of smaller white snakes with a pale human-like face at the front of the head — "
  "held inside flat opaque BLACK flame with hard white outlines. THE WOMAN IS NOT VISIBLE IN THIS "
  "SHARD.\n"
  "PANEL 5 (BORDERLESS evidence shard, lower right): the teen walking away out of the throne hall "
  "with his BACK to the reader while the last flat black flames finish behind him. HIS MOUTH IS "
  "NOT VISIBLE.\n"
  "PANEL 6 (lower left): back in the flat red-and-black space — she leans as far forward as the "
  "black cross allows; his posture does not change at all. Both mouths are visible.\n"
  "PANEL 7 (wide panel across the bottom, SILENT): the cross and the red space fracture like sheet "
  "glass around her; her body pitches forward into the returning office while he is already one "
  "step back, balanced and waiting. No text in this panel. " + L_VOID
  + SAY((1, GUREN, "upper left", "LIAR."),
        (2, NAR, "upper right", "LOOK."),
        (3, OFF(NAR), "lower right", "KABUTO LIVES. I IMMOBILIZED HIM."),
        (4, OFF(GUREN), "upper left", "NO."),
        (5, OFF(NAR), "upper right", "HE DIED."),
        (6, GUREN, "upper right", "RELEASE ME. I'LL KILL YOU."),
        (6, NAR, "lower left", "KILLING ME IS BEYOND YOU."))
  + "In PANEL 6 the two balloons cross the panel diagonally: the upper-right balloon's tail runs "
    "down-LEFT to the light-blue-haired woman and the lower-left balloon's tail runs up-RIGHT to "
    "the blond teen. Neither tail may approach the other speaker. "
  + "LOWER ROW ORDER: the borderless evidence shard PANEL 5 (the teen walking away with his back "
    "to the reader) is the lower row's RIGHT-HAND element and PANEL 6 (the two of them back in "
    "the red-and-black space) sits entirely to its LEFT. The evidence line \"HE DIED.\" must be "
    "read BEFORE \"RELEASE ME. I'LL KILL YOU.\" / \"KILLING ME IS BEYOND YOU.\" Never place PANEL "
    "6 to the right of PANEL 5. ",
  R("naruto_v4_armor_sword", "kabuto", "orochimaru", "env_oto_throne_hall"), "low"),

 # ---- Spread 7: coercion opens the argument ----------------------------------------
 ("p13", dict(scene="action", light="interior", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + FLAT + GUREN_HAIR + OFFICE +
  "SIX panels. Force stops a threat and buys nothing else.\n"
  "PANEL 1 (top right): the office is back. She catches herself on the desk at the reader's LEFT, "
  "then drives one step toward him at the reader's RIGHT, her right hand empty but raised to "
  "strike. Her mouth is visible.\n"
  "PANEL 2 (top left): close on him, eye-line fixed on her centre mass, not advancing. His mouth "
  "is visible.\n"
  "PANEL 3 (HALF-PAGE dominant panel from floor level): the room bends under his killing intent, "
  "drawn as hard-edged pressure lines and flat leaning geometry, never as a glow. She is forced "
  "onto both knees at centre-LEFT with one palm braced on the floor; he stands at the far RIGHT "
  "with his long hair and red-armour ties lifted by the pressure. His plain sash sword stays "
  "sheathed, his numb left forearm stays guarded, and he does not touch her. Papers hang in the "
  "air. His mouth is visible.\n"
  "PANEL 4 (lower right): the pressure is gone and papers settle. She coughs once, plants one boot "
  "and begins pushing herself up; he has not moved.\n"
  "PANEL 5 (lower centre): she stands using the desk edge, breathing hard but meeting his eyes. "
  "Her mouth is visible.\n"
  "PANEL 6 (level two-shot across the bottom): she is at the LEFT and he is at the RIGHT with the "
  "desk between them, now a negotiating line rather than her wall. Both mouths are visible. "
  + L_DESK
  + SAY((1, GUREN, "upper left", "I SWEAR I'LL—"),
        (2, NAR, "upper right", "ENOUGH."),
        (3, NAR, "upper right", "I LEFT YOUR PEOPLE ALIVE."),
        (3, NAR, "mid-right", "DO NOT MAKE THEIR LEADER THE EXCEPTION."),
        (5, GUREN, "upper left", "IF FEAR IS YOUR OFFER, YOU DON'T NEED A LEADER."),
        (5, GUREN, "lower left", "YOU NEED ANOTHER PRISONER."),
        (6, NAR, "upper right", "I NEEDED YOU TO LISTEN."),
        (6, GUREN, "upper left", "I'M LISTENING."),
        (6, GUREN, "lower right", "THAT IS NOT AGREEMENT."),
        (6, NAR, "lower left", "GOOD."))
  + "In PANEL 6 the two lower balloons cross the panel diagonally: the lower-right balloon's tail "
    "runs down-LEFT to the light-blue-haired woman and the lower-left balloon's tail runs "
    "down-RIGHT to the blond teen. Neither tail may approach the other speaker. "
  + "PANEL 6 BALLOON ORDER IS FIXED: the LOWER-RIGHT balloon reads \"THAT IS NOT AGREEMENT.\" and "
    "the LOWER-LEFT balloon reads \"GOOD.\", in that right-to-left order, so his one-word answer "
    "is read AFTER the line it answers. Never put \"GOOD.\" to the right of \"THAT IS NOT "
    "AGREEMENT.\" "
  + "PANEL 4 IS ONE SINGLE PANEL, never split into two and never repeated: inside that one frame "
    "the light-blue-haired woman is already MID-RISE — one boot planted, one hand pushing off the "
    "floor, her shoulders coming up — with the loosed papers still settling around her. The page "
    "never shows her going back down onto all fours after standing; her recovery only ever runs "
    "upward, from PANEL 3's knees, through PANEL 4's push, to PANEL 5's stand. "
  + SFX(4, "FLUTTER", "In the lower centre, beside the falling papers. "),
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "medium"),

 ("p14", dict(scene="dialogue", light="interior", cast="two", mood="somber", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D, MEMORY_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SEVEN panels. Her old loyalty is taken apart, and she names what that gives him.\n"
  "PANEL 1 (top right): he stands at the reader's RIGHT, she stands behind the desk at the "
  "reader's LEFT, eye-lines holding. Both mouths are visible.\n"
  "PANEL 2 (upper left): close on him, mouth visible.\n"
  "PANEL 3 (middle right): close on her, chin raised, mouth visible.\n"
  "PANEL 4 (BORDERLESS memory image occupying the CENTRE of the middle row — immediately to the "
  "LEFT of PANEL 3 and immediately to the RIGHT of PANEL 5, softly faded at its edges): a gentle-faced "
  "dark-haired woman shelters an unconscious younger blue-haired girl; behind them a second much "
  "smaller silhouette shows that same girl carrying out an order she regrets. The violence stays "
  "entirely implicit — no injury, no blood, no weapon in contact. NEITHER PRESENT-DAY SPEAKER "
  "APPEARS IN THIS IMAGE.\n"
  "PANEL 5 (middle left): close on him, mouth visible, with no triumph anywhere in the "
  "expression.\n"
  "PANEL 6 (wide panel, lower right): she grips the desk with her left hand until the knuckles go "
  "pale and her eye-line drops for the first time. HE IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 7 (wide two-shot across the bottom): she looks up sharply from the reader's LEFT; he "
  "stays at the reader's RIGHT with his right hand open and his bruised left forearm guarded "
  "beside the sheathed plain sword. Both mouths are visible. " + L_DESK
  + SAY((1, NAR, "upper right", "WHY WERE YOU LOYAL TO HIM?"),
        (1, GUREN, "upper left", "HE TOOK ME IN WHEN EVERYONE ELSE TURNED AWAY."),
        (2, NAR, "upper right", "WHAT DID HIS ACCEPTANCE COST?"),
        (3, GUREN, "upper left", "YOU KNOW NOTHING ABOUT IT."),
        (4, OFF(NAR), "upper right", "YUKIMARU'S MOTHER."),
        (4, OFF(GUREN), "lower left", "STOP."),
        (5, NAR, "upper right",
         "HE ORDERED YOU TO KILL THE WOMAN WHO SAVED YOU—THEN GAVE YOU HER SON."),
        (6, OFF(NAR), "upper right",
         "HE WOULD HAVE ORDERED YUKIMARU'S DEATH WHEN THE BOY STOPPED BEING USEFUL."),
        (6, OFF(NAR), "lower right",
         "HE PROMISED YOU WOULD BE HIS NEXT VESSEL. HE ALWAYS CHOSE ANOTHER."),
        (7, GUREN, "upper left", "YOU CRAWLED THROUGH MY HEAD SO YOU CAN USE IT TOO."),
        (7, NAR, "lower right", "SO YOU KNOW I COULD."))
  + "PANEL LAYOUT IS FIXED AND MUST NOT BE REORDERED. PANELS 3, 4 and 5 form ONE middle tier read "
    "right to left: PANEL 3 (close on her) at the tier's RIGHT edge, the BORDERLESS memory image "
    "PANEL 4 in the CENTRE immediately to its left, PANEL 5 (close on him) at the tier's LEFT "
    "edge. PANELS 6 and 7 sit entirely BELOW that tier, PANEL 6 above PANEL 7. Consequences that "
    "must hold: \"YOU KNOW NOTHING ABOUT IT.\" is read BEFORE the memory image and its \"YUKIMARU'S "
    "MOTHER.\" / \"STOP.\"; and \"HE ORDERED YOU TO KILL THE WOMAN WHO SAVED YOU—THEN GAVE YOU HER "
    "SON.\" is read BEFORE \"HE WOULD HAVE ORDERED YUKIMARU'S DEATH WHEN THE BOY STOPPED BEING "
    "USEFUL.\" Never place the memory image to the right of PANEL 3, and never place PANEL 6 "
    "above or to the right of PANEL 5. ",
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "low"),

 # ---- Spread 8: name the hidden ownership ------------------------------------------
 ("p15", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SIX panels. Blackmail is refused and replaced by a bounded choice.\n"
  "PANEL 1 (narrow panel, top right): close on him with both hands still open. His mouth is "
  "visible.\n"
  "PANEL 2 (top left — an ordinary rectangle sharing the top row with PANEL 1 and the same height "
  "as it; it never runs down the page beside the panels below): close on her, suspicious. Her "
  "mouth is visible.\n"
  "PANEL 3 (middle right): he turns one palm downward, closing the subject instead of pressing "
  "it. His mouth is visible.\n"
  "PANEL 4 (wide panel across the middle): the two of them across the desk, he at the RIGHT and "
  "she at the LEFT, heads at equal height. Both mouths are visible.\n"
  "PANEL 5 (lower right): she pulls the desk chair upright but does NOT sit in it — the movement "
  "is entirely hers and breaks his rhythm. Her mouth is visible above the chair back.\n"
  "PANEL 6 (large panel across the bottom — a SEPARATE frame lying BELOW PANEL 5 with a real "
  "gutter between them, never merged with PANEL 5 into a single frame): he stands outside the "
  "RIGHT edge of the desk; she "
  "stands behind the chair on the LEFT, occupying the future leader's position. His mouth is "
  "visible. " + L_DESK
  + SAY((1, NAR, "upper right", "I WON'T."),
        (2, GUREN, "upper left", "WHY SHOULD I BELIEVE YOU?"),
        (3, NAR, "upper right", "BECAUSE I DO NOT NEED YOUR SHAME."),
        (4, NAR, "upper right",
         "REFUSE, AND I FIND ANOTHER LEADER. STAND IN MY WAY, AND I KILL YOU."),
        (4, GUREN, "upper left", "THAT IS STILL A THREAT."),
        (4, NAR, "lower right", "YES."),
        (5, GUREN, "upper left", "THEN STATE THE WORK."),
        (6, NAR, "upper right", "REBUILD OTOGAKURE AS A REAL VILLAGE. LEAD IT."))
  + "SIX SEPARATE PANELS IN FOUR HORIZONTAL TIERS, NONE OF THEM TALL AND NONE OF THEM MERGED. "
    "Tier 1 holds PANEL 1 at the RIGHT and PANEL 2 immediately to its LEFT; PANEL 2 is an "
    "ordinary rectangle confined to that tier and NEVER a tall panel running down the page beside "
    "a stacked right-hand column. Tier 2 is PANEL 3, tier 3 is PANEL 4, tier 4 holds PANEL 5 at "
    "the RIGHT and PANEL 6 immediately to its LEFT, separated by a real gutter and NEVER merged "
    "into one frame. Consequences that must hold: \"WHY SHOULD I BELIEVE YOU?\" is read BEFORE "
    "\"BECAUSE I DO NOT NEED YOUR SHAME.\", and \"THEN STATE THE WORK.\" is read BEFORE \"REBUILD "
    "OTOGAKURE AS A REAL VILLAGE. LEAD IT.\" ",
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "low"),

 ("p16", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SEVEN panels. Visible leadership and invisible ownership share one frame without becoming the "
  "same thing.\n"
  "PANEL 1 (top right): she finally sits down in the chair at the reader's LEFT; he stays standing "
  "at the reader's RIGHT. Both mouths are visible.\n"
  "PANEL 2 (top left): she leans forward over the desk. Her mouth is visible.\n"
  "PANEL 3 (middle right): close on him, mouth visible, his plain sash sword still at the bottom "
  "of the frame and his left forearm guarded.\n"
  "PANEL 4 (middle centre): close on her as the inference lands. Her mouth is visible.\n"
  "PANEL 5 (middle left): medium on him with the dark doorway behind him, suggesting he can step "
  "out of the public frame whenever he likes. His mouth is visible.\n"
  "PANEL 6 (narrow SILENT movement strip): she rises and circles around the desk into the LIT "
  "reader-RIGHT foreground with the leader's chair behind her, while he steps back into the "
  "reader-LEFT doorway shadow. They hold eye contact and their paths do not cross. No text in "
  "this panel.\n"
  "PANEL 7 (HALF-PAGE focal two-shot across the bottom): she stands in the light at the far RIGHT "
  "with her chair and desk directly behind her; he stands in doorway shadow at the far LEFT. Both "
  "mouths are visible. THE EMPTY CENTRE FLOOR OF THIS PANEL STAYS COMPLETELY CLEAR — no body, no "
  "balloon and no tail may cross it, and all four balloons use SHORT DIRECT tails to the nearest "
  "speaker. " + L_DESK
  + SAY((1, GUREN, "upper left", "WHY ME?"),
        (1, NAR, "lower right", "YOU'RE STRONG. OTO KNOWS YOU. YOU CAN HOLD WHAT REMAINS TOGETHER."),
        (2, GUREN, "upper left", "WHY DOES A KONOHA SHINOBI WANT OTO?"),
        (3, NAR, "upper right", "POWER. KONOHA DOES NOT KNOW."),
        (4, GUREN, "upper left", "I WOULD BE THE FACE OF YOUR HIDDEN VILLAGE."),
        (5, NAR, "upper right",
         "YOU WOULD LEAD IT. I PROVIDE THE PLAN, MONEY, CONTACTS, AND DIRECTION."),
        (7, GUREN, "upper right", "DIRECTION IS A CLEAN WORD FOR CONTROL."),
        (7, NAR, "upper left", "CALL IT WHAT YOU LIKE. THE VILLAGE SURVIVES HIM."),
        (7, GUREN, "lower right", "AND BECOMES YOURS."),
        (7, NAR, "lower left", "ITS STRENGTH DOES.")),
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "medium"),

 # ---- Spread 9: the plan before the answer -----------------------------------------
 ("p17", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=7),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SEVEN panels. The complete plan reaches her hands BEFORE she answers. From here on she holds "
  "the reader-RIGHT side of every panel and he holds the reader-LEFT doorway side.\n"
  "PANEL 1 (wide panel across the top): across the desk — she stays at the reader-RIGHT with the "
  "leader's chair behind her, he stays at the reader-LEFT near the doorway. With his RIGHT hand he "
  "begins pulling the glove off his bruised LEFT hand; his plain sword stays sheathed and clear "
  "of the motion. His mouth is visible.\n"
  "PANEL 2 (small insert, upper right of the second row): close on his bandaged left hand and the "
  "sealing tattoo on its palm, his right fingertips running across the mark. The injured arm stays "
  "lowered and bears no weight. Any marking in the tattoo is ILLEGIBLE SCRIBBLE. No text in this "
  "panel.\n"
  "PANEL 3 (tight insert in the SAME second row, immediately to the LEFT of PANEL 2): smoke bursts from the tattoo as a flat opaque shape and a "
  "large scroll begins forming directly above the left palm; his right hand closes around it as it "
  "appears.\n"
  "PANEL 4 (large handoff panel across the middle): he throws the scroll RIGHTWARD with his right "
  "hand and she catches it with both hands at the reader-RIGHT. He stays at the reader-LEFT with "
  "his mouth visible and the plain sword still sheathed at his sash.\n"
  "PANEL 5 (lower right): she spreads the first section of the scroll open across the right side "
  "of the desk. It carries CLEAR ARCHITECTURAL DIAGRAMS — housing blocks, a school, a hospital, "
  "streets and an administrative centre — and every annotation on it is ILLEGIBLE SCRIBBLE, never "
  "readable words. He is visible at the reader-LEFT pulling the glove back over his left hand with "
  "his right; his mouth is visible.\n"
  "PANEL 6 (lower centre): he turns toward the reader-LEFT doorway after securing the glove; she "
  "looks up from the scroll at the reader-RIGHT. Both mouths are visible.\n"
  "PANEL 7 (bottom): he looks back over his shoulder from the reader-LEFT; she stays behind the "
  "open scroll at the reader-RIGHT. Both mouths are visible. " + L_DESK
  + SAY((1, NAR, "upper left", "THEN LOOK AT WHAT YOU WOULD BUILD."),
        (4, NAR, "upper left", "THAT SCROLL HOLDS EVERY CONSTRUCTION PLAN."),
        (5, NAR, "upper left", "EVERYTHING NEEDED WILL BE PROVIDED."),
        (6, GUREN, "upper right", "I HAVEN'T SAID YES."),
        (7, NAR, "upper left", "YOU HAVEN'T SAID NO."))
  + "SECOND ROW ORDER: PANEL 2 (the close-up of the bandaged left palm and its sealing tattoo) is "
    "that row's RIGHT-HAND insert and PANEL 3 (the burst of smoke with the scroll forming and the "
    "POOF effect) sits immediately to its LEFT. The palm that causes the summoning is read BEFORE "
    "the burst it causes; never place the POOF panel to the right of the palm panel. "
    "LOWER ROW ORDER: PANEL 5 (she spreads the plan across the desk) is the RIGHT-HAND panel of "
    "its row, PANEL 6 sits to its LEFT and PANEL 7 is the bottom panel below them both, so "
    "\"EVERYTHING NEEDED WILL BE PROVIDED.\" is read BEFORE \"I HAVEN'T SAID YES.\", which is "
    "immediately followed by \"YOU HAVEN'T SAID NO.\" Never place PANEL 6 to the right of PANEL 5. "
  + SFX(3, "POOF", "Beside the smoke at the upper left of the panel. "),
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "low"),

 ("p18", dict(scene="emotional_closeup", light="interior", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SIX panels. The hesitation is given room, and then she accepts.\n"
  "PANEL 1 (top right): close on her at the reader-RIGHT gripping the open scroll without rolling "
  "it shut. Her mouth is visible. HE IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 2 (SILENT insert, top left): her fingers trace the drawn road from the housing and school "
  "blocks to the central administrative building. The plan stays diagrams and ILLEGIBLE SCRIBBLE "
  "annotations, never readable words. No text in this panel.\n"
  "PANEL 3 (SILENT medium, middle right): she looks up from the open plan toward the wall that "
  "separates the office from the civilian-cell corridor. He waits at the reader-LEFT near the "
  "doorway without approaching. Her eye-line does NOT go toward the sealed reinforced wing. No "
  "text in this panel.\n"
  "PANEL 4 (wide panel across the middle): the whole room — he at the reader-LEFT, she at the "
  "reader-RIGHT behind the open scroll. HIS MOUTH IS VISIBLE; HER MOUTH IS CLOSED.\n"
  "PANEL 5 (lower right): she rolls the plan shut at the reader-RIGHT and holds it against her "
  "side, eyes staying on him at the reader-LEFT. Her mouth is visible.\n"
  "PANEL 6 (HALF-PAGE acceptance panel across the bottom): she stays at the reader-RIGHT with the "
  "scroll under her arm and the leader's chair behind her; he stays at the reader-LEFT near the "
  "doorway and gives one small restrained smile. HIS MOUTH IS VISIBLE; HER MOUTH IS CLOSED. "
  + L_DESK
  + SAY((1, GUREN, "upper right", "WELL..."),
        (4, NAR, "upper left", "I DON'T SEE ANYONE REFUSING A CHANCE TO START A NEW LIFE."),
        (4, NAR, "lower left", "OR TO MAKE OTHER LIVES BETTER."),
        (5, GUREN, "upper right", "YES."),
        (5, GUREN, "lower right", "I DON'T HAVE ANYTHING BETTER TO DO."),
        (6, NAR, "upper left", "GOOD.")),
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "low"),

 # ---- Spread 10: the first order of the new Sound ----------------------------------
 ("p19", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + ENV.format(i=2)
  + ONLY(NAR, GUREN_D, CAPTIVES_D) + GEAR + ARM + NOTEXT + GUREN_HAIR + OFFICE +
  "SIX panels. Every operational instruction, given only after her acceptance.\n"
  "PANEL 1 (top right): he turns toward the reader-LEFT doorway; she moves out from the "
  "reader-RIGHT with the scroll. His mouth is visible, his left glove is back on, his bruised "
  "forearm is guarded and his plain sword is sheathed.\n"
  "PANEL 2 (top left): corridor-facing two-shot — her eye-line checks the ordinary barred civilian "
  "cells at the reader-RIGHT while the REINFORCED, still-locked wing door stays at the "
  "reader-LEFT. He is beside her. Both mouths are visible.\n"
  "PANEL 3 (insert, middle right): locked record cabinets, racked weapons and supply seals along "
  "the office wall; every label on them is ILLEGIBLE SCRIBBLE. HE IS NOT IN THIS PANEL AT ALL.\n"
  "PANEL 4 (middle left): she looks back from the doorway toward the reinforced wing door; he "
  "stays visible at the reader-LEFT. Both mouths are visible.\n"
  "PANEL 5 (lower right): he steps into the corridor shadow at the reader-LEFT; she stops in the "
  "office light at the reader-RIGHT. Both mouths are visible.\n"
  "PANEL 6 (wide threshold panel across the bottom): she stays at the reader-RIGHT and he stays at "
  "the reader-LEFT; their bodies face the same exit while their eye-lines cross back to each "
  "other. HIS MOUTH IS VISIBLE; HER MOUTH IS CLOSED. " + L_CELL
  + SAY((1, NAR, "upper left", "TAKE YOUR MOST TRUSTED PEOPLE AND THE INNOCENTS TO OTO."),
        (2, GUREN, "upper right", "THE CIVILIANS?"),
        (2, NAR, "lower left", "IF THEY HAVE FAMILIES, LET THEM LEAVE."),
        (3, OFF(NAR), "upper left", "SEAL EVERYTHING VALUABLE."),
        (4, GUREN, "upper right", "AND THAT WING?"),
        (4, NAR, "lower left", "KEEP IT SEALED. DESTROY THE HIDEOUT WITH THE EXPERIMENTS INSIDE."),
        (5, GUREN, "upper right", "WHO HANDLES CONSTRUCTION?"),
        (5, NAR, "mid-left", "MY TRUSTED FRIEND, ZETSU, WILL FIND YOU IN OTO."),
        (5, NAR, "lower left", "HE'LL GIVE YOU INSTRUCTIONS AND CONNECTIONS."),
        (6, NAR, "lower left", "KEEP MY NAME OUT OF EVERYTHING."))
  + "CHECK HER HAIR IN PANELS 1, 4, 5 AND 6 IN PARTICULAR: the long swept fringe must fall "
    "diagonally across her forehead in each of them exactly as it does on the pages before and "
    "after this one. A blunt straight fringe, or both eyes drawn fully clear of hair, is wrong in "
    "every panel of this page. ",
  R("naruto_v4_armor_sword", "env_orochimaru_lab"), "low"),

 ("p20", dict(scene="establishing", light="interior", cast="small_group", mood="calm", panels=6),
  FILL + RTL + N16_SWORD.format(i=1) + MOB.format(i=2) + ENV.format(i=3)
  + ONLY(NAR, GUREN_D, SOUND2_D, CAPTIVES_D) + GEAR + ARM + NOTEXT + GUREN_HAIR +
  "SIX panels. LAST PAGE OF THE CHAPTER — the name, then the first order she gives as leader.\n"
  "PANEL 1 (narrow panel, top right): she stays at the reader-RIGHT threshold while he walks away "
  "down the corridor toward the reader-LEFT. Her mouth is visible.\n"
  "PANEL 2 (narrow panel, top left): he half-turns out of the shadow at the reader-LEFT; she stays "
  "in the light at the reader-RIGHT; their eye-lines meet across the threshold. His mouth is "
  "visible.\n"
  "PANEL 3 (SILENT horizontal strip): his silhouette disappears around the far-LEFT corner with "
  "the plain sword still at his sash. She turns RIGHT toward the civilian-cell corridor, reversing "
  "her attention from him to the people. No text in this panel.\n"
  "PANEL 4 (middle band): she crosses RIGHTWARD with the scroll secured under her arm; two "
  "anonymous Sound shinobi come up and wait for her direction. Her mouth is visible. The "
  "reinforced wing door stays CLOSED behind them.\n"
  "PANEL 5 (small insert, SILENT): close on a ring of cell keys passing from a shinobi's hand at "
  "the LEFT into her hand at the RIGHT. No text in this panel.\n"
  "PANEL 6 (HALF-PAGE final panel across the bottom): she stands centre-foreground facing the "
  "civilian-cell corridor with the two Sound shinobi waiting behind her; unaltered civilians, and "
  "the SAME small child whose hand reached through the bars earlier, look out through the bars at "
  "the RIGHT. The reinforced wing door stays locked in the deep-LEFT background. She points at the "
  "civilian locks ONLY, her weight already carrying forward. Her mouth is visible. " + L_CELL
  + SAY((1, GUREN, "upper right", "YOU NEVER GAVE ME YOUR NAME."),
        (2, NAR, "upper left", "UCHIHA NARUTO."),
        (4, GUREN, "upper centre", "BRING THE CIVILIAN KEYS. LEAVE THE EXPERIMENT WING SEALED."),
        (6, GUREN, "upper centre", "OPEN THE CIVILIAN CELLS."),
        (6, GUREN, "lower centre-left", "WE'RE LEAVING FOR OTO."))
  + "THERE IS EXACTLY ONE LIGHT-BLUE-HAIRED WOMAN IN THE WORLD OF THIS PAGE AND SHE APPEARS ONCE "
    "PER PANEL. PANEL 2 holds ONLY TWO FIGURES: the blond teen half-turned in the shadow at the "
    "reader-LEFT, and the one light-blue-haired woman standing in the light at the reader-RIGHT. "
    "Do NOT flank him with a second blue-haired or bare-shouldered figure, do not add a mirrored "
    "or out-of-focus copy of her on his other side, and do not put any blurred foreground body in "
    "the frame. The same rule holds in every other panel: one of her, never two. ",
  R("naruto_v4_armor_sword", "mob_archetypes", "env_hideout_corridor"), "high"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch08" / "raw", HERE / "v5ch08" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
