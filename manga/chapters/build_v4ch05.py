"""Volume 4, Chapter 5 — Orange. 24 pages."""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts_v4 import *  # noqa: F401,F403,E402


PAGES = [
 ("p01", dict(scene="establishing", light="hard_day", cast="two", mood="resolute", panels=1),
  FILL + N16_SWORD.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, "the split black-and-white plant creature") +
  "CHAPTER-OPENING BORDERLESS VERTICAL SPLASH. Naruto is an approximately sixteen-year-old teen, never an adult, small at the black mouth of Madara's rock-carved hideout, seen from behind. His red armour, gunbai, and NEW PLAIN STRAIGHT SASH SWORD make a sharp silhouette against a hard white daylight wedge. Zetsu is only a half-seen plant shape emerging from the wall at far lower left. Preserve the calm upper third for the title and caption. "
  + "TITLE LETTERING: in the quiet upper third, write the chapter title in large bold upright English capitals, correctly spelled: \"ORANGE\". The title does not prohibit the caption, balloons, or sound effects specified below. " + CAP(1, "upper left", "TWO YEARS, EIGHT MONTHS LATER.")
  + SAY((1, OFF("the split black-and-white plant creature"), "upper right", "YOU ARE LEAVING AT LAST."),
        (1, N16_SPEAKER, "lower right", "I HAVE TRAINED ENOUGH.")),
  R("naruto_v4_armor_sword", "zetsu", "env_madara_hideout_exit"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="two", mood="controlled", panels=5),
  FILL + N16_SWORD.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, "the split black-and-white plant creature") +
  "FIVE UNEQUAL PANELS. PANEL 1, dominant top horizontal: profile close-up of Naruto's visible Sharingan against sun. PANELS 2–4, thin descending details: red armour plates; gunbai face; then his gloved hand settling on the NEW SWORD'S SASH, never a back-slung lost ninjato. PANEL 5, wide bottom: Zetsu sinks into shadow while Naruto walks toward light. "
  + SAY((1, N16_SPEAKER, "upper right", "OROCHI'S BORDER BASE. THE UZUMAKI GIRL AND THE MASK."),
        (5, "the split black-and-white plant creature", "lower left", "JIRAIYA AND KONOHA WILL SEE YOU ONCE YOU SURFACE."),
        (5, N16_SPEAKER, "lower right", "THEN I WILL DEAL WITH THEM.")) + SFX(5, "KLANG"),
  R("naruto_v4_armor_sword", "zetsu", "gunbai_v4", "env_madara_hideout_exit"), "high"),

 ("p03", dict(scene="dialogue", light="day", cast="three", mood="absence", panels=6),
  FILL + KAK.format(i=1) + JIR.format(i=2) + SASUKE16.format(i=3) + ENV.format(i=4) + ONLY(MAN, SAGE, SASUKE16_SPEAKER) +
  "SIX UNEQUAL PANELS. Top strip: burned grass and splintered trees. Dominant middle panel staggers Kakashi's cropped masked shoulder huge in foreground, Jiraiya a smaller full figure across scarred ground, and Sasuke in a distant inset wiping blood from a spar. No line-up. Bottom panels leave Sasuke apart. "
  + SAY((2, SAGE, "upper left", "YOU HAVE BOTH OUTGROWN DRILLS."),
        (3, MAN, "upper right", "THEN HE NEEDS MISSIONS."),
        (5, SASUKE16_SPEAKER, "middle right", "ITACHI IS STILL MINE."),
        (6, SASUKE16_SPEAKER, "lower left", "AND NARUTO?")) + SFX(1, "SHHH"),
  R("kakashi", "jiraiya", "sasuke_16", "env_training_scarred_field"), "high"),

 ("p04", dict(scene="transition", light="day", cast="four", mood="uneasy", panels=5),
  FILL + KAK.format(i=1) + JIR.format(i=2) + SASUKE16.format(i=3) + N16_SWORD.format(i=4) + ENV.format(i=5) + ENV.format(i=6) + ONLY(MAN, SAGE, SASUKE16_SPEAKER, N16_SPEAKER) +
  "FIVE PANELS. Close Jiraiya eye, then white-space Sasuke reaction. Dominant lower wide separates Jiraiya walking away, cropped Kakashi foreground, and Sasuke distant. Final bottom strip jumps one week: Naruto's fireball opens Oto's false stone entrance; no guards. "
  + SAY((1, SAGE, "upper left", "NO TRAIL. HE CHOSE TO VANISH."),
        (3, MAN, "upper right", "WE WILL FIND OUT WHEN HE WANTS US TO."))
  + CAP(4, "upper left", "ONE WEEK LATER — OTŌ BORDER.") + SFX(5, "WHOOOM"),
  R("kakashi", "jiraiya", "sasuke_16", "naruto_v4_armor_sword", "env_training_scarred_field", "env_oto_hidden_base"), "high"),

 ("p05", dict(scene="establishing", light="dark", cast="solo", mood="infiltration", panels=6),
  FILL + N16_SWORD.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER) +
  "SIX UNEQUAL PANELS. Top wide establishes the blasted aperture in a natural cliff. Three tall corridor panels pull Naruto inward from rear view, armour the only warm colour. A small black panel shows three passages. Dominant bottom panel follows him down the middle passage, plates ringing into darkness. "
  + CAP(4, "upper left", "THE CENTRAL PASSAGE.") + SFX(6, "KLANG… KLANG…"),
  R("naruto_v4_armor_sword", "env_oto_hidden_base"), "high"),

 ("p06", dict(scene="dialogue", light="dark", cast="three", mood="threat", panels=5),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "FIVE PANELS. Dominant upper low angle looks past Naruto into the cavernous throne hall: Orochimaru sits tiny beneath the snake statue and Kabuto stands offset at his right. Lower close-ups: Kabuto's glasses, Orochimaru's slit pupil, Naruto folding his arms. "
  + SAY((1, N16_SPEAKER, "upper right", "YOU KEPT SOMETHING AND SOMEONE THAT ARE MINE."),
        (3, PALEONE, "lower left", "YOU HAVE GROWN INTO A FAMILIAR SILHOUETTE.")) + SFX(5, "TIK"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_oto_throne_hall"), "high"),

 ("p07", dict(scene="action", light="fire", cast="three", mood="challenge", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SIX UNEQUAL PANELS. Cropped Orochimaru smile, then Naruto profile against black. Dominant lower panel: Naruto's fireball passes between Orochimaru and Kabuto, destroys the throne, and leaves both bodies readable through hard flame shapes. "
  + SAY((1, PALEONE, "upper left", "YOU CARRY TWO BLOODLINES."), (2, N16_SPEAKER, "upper right", "YOU HAVE NOTICED ENOUGH."),
        (5, N16_SPEAKER, "lower left", "I DID NOT COME TO JOIN YOU."), (6, PALEONE, "lower right", "THEN SHOW ME WHAT TWO YEARS BOUGHT.")) + SFX(5, "KRAAASH"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_oto_throne_hall"), "high"),

 ("p08", dict(scene="action", light="dark", cast="three", mood="escalating", panels=7),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SEVEN QUICK UNEQUAL PANELS: foot against forearm, intercepted kicks, locked hands, Naruto's hair-hidden face, floor-level shockwave, Kabuto at a cropped edge, then dominant bottom panel Naruto forcing Orochimaru toward one knee. Keep all action in the throne hall. "
  + SAY((2, N16_SPEAKER, "upper right", "THAT IS YOUR TEST?"), (4, PALEONE, "middle left", "A TEST REQUIRES EFFORT."),
        (7, N16_SPEAKER, "lower right", "THEN USE MORE.")) + SFX(3, "THOOM") + SFX(5, "KRAK") + SFX(7, "WHUMP"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "env_oto_throne_hall"), "high"),

 ("p09", dict(scene="action", light="dark", cast="two", mood="precision", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, PALEONE) +
  "SIX PANELS. Top letterbox: sleeve snakes toward lens. Tall panels show Naruto's NEW SASH SWORD clearing them and Orochimaru producing Kusanagi. Dominant bottom crossed-blade lock has Naruto shoulder foreground, blades center, Orochimaru beyond. Wind chakra reinforces Naruto's new blade so it survives; it is never V3's lost ninjato. "
  + SAY((2, PALEONE, "upper left", "THE FAN. THE EYES. WHY HIDE THEM?"), (6, N16_SPEAKER, "lower right", "BECAUSE YOU HAVE NOT EARNED THEM.")) + SFX(1, "SHHK") + SFX(6, "KLANG"),
  R("naruto_v4_armor_sword", "orochimaru", "env_oto_throne_hall"), "high"),

 ("p10", dict(scene="action", light="fire", cast="two", mood="overreach", panels=5),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + SUSA_RIBCAGE.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, PALEONE) +
  "FIVE PANELS. Near-black hand seals, then fire release fills the corridor while pillars, rock, and exit remain visible. Naruto ACTIVATES HIS EMS; his active left eye uses the supplied Mangekyō pattern. Reactions show Orochimaru escaping and supports cracking. Final panel: the returning mud dragon hits ONLY an opaque orange skeletal rib cage around Naruto—no finished body, helmet, arms, or weapons. EMS remains active. "
  + SAY((2, N16_SPEAKER, "upper right", "TOO MUCH."), (5, OFF(PALEONE), "middle left", "MUD DRAGON.")) + SFX(3, "FWOOSH") + SFX(4, "KRRRKK"),
  R("naruto_v4_armor_sword", "orochimaru", "susanoo_orange_ribcage", "mangekyo_design", "env_oto_hidden_base"), "high"),

 ("p11", dict(scene="action", light="day", cast="three", mood="demand", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SIX PANELS IN CAUSAL ORDER. PANEL 1: Naruto's active EMS left eye strains and a dark mark trails below it. PANEL 2: hard-edged black Amaterasu hits Orochimaru. PANEL 3: Orochimaru skin-sheds, a whole reformed body escaping the black flame. PANEL 4: Naruto follows immediately with fire, forcing Orochimaru down near the breach. PANEL 5: Kabuto intercepts Naruto's advance; only then does Naruto demand the mask. Dominant PANEL 6: Orochimaru stalls while Naruto's dense dark-edged chakra lifts debris; all bodies remain legible. EMS remains active. "
  + SAY((5, N16_SPEAKER, "upper right", "THE MASK. DID YOU TAKE IT?"), (6, PALEONE, "middle left", "PERHAPS."),
        (6, N16_SPEAKER, "lower right", "I AM DONE ASKING.")) + SFX(6, "GROOOOM"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "mangekyo_design", "env_oto_throne_hall"), "high"),

 ("p12", dict(scene="action", light="day", cast="three", mood="discovery", panels=7),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SEVEN FAST PANELS. Dominant center panel: hard-edged wind blades cut Kabuto across the torso. Small inserts show wound closing, glasses pushed up, scalpels, and Naruto registering regeneration. Final wide strip places Orochimaru and Kabuto at different depths around Naruto as collapse drives them through the breach. Naruto's EMS remains visibly active. "
  + SAY((2, SPEC, "upper left", "DAMAGED CELLS CAN BE RESTARTED."), (4, N16_SPEAKER, "middle right", "SHOW ME AGAIN.")) + SFX(4, "SHRAK") + SFX(7, "KRA-BOOM"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "mangekyo_design", "env_oto_throne_hall"), "high"),

 ("p13", dict(scene="action", light="day", cast="three", mood="pressure", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + SUSA_RIBCAGE.format(i=4) + MANGEKYO_EYE.format(i=5) + ENV.format(i=6) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SIX PANELS. Calm exterior establish: broken hill and smoke under clear sky, Naruto small between Orochimaru and Kabuto. Kabuto's scalpel first sparks on Naruto's chest plate. Orochimaru's GREAT WIND BREAKTHROUGH then hurls Naruto back; his WIND DRAGON follows. Dominant lower panel: active-EMS Naruto raises the opaque orange RIB-CAGE Susano'o defensively, which catches the Wind Dragon. First open-ground page. "
  + SAY((2, SPEC, "upper left", "TOGETHER."), (2, PALEONE, "upper right", "HE WILL FALL."), (6, N16_SPEAKER, "lower right", "YOU ARE STILL MEASURING ME.")) + SFX(4, "TANG"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "susanoo_orange_ribcage", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p14", dict(scene="action", light="day", cast="three", mood="pressure", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SIX PANELS. Active-EMS Naruto first places hard-edged black Amaterasu on Orochimaru's hand. He follows with Wood Release: branches erupt diagonally with ground and opponents readable between gaps. Orochimaru takes Kabuto underground to evade it; show this escape visually with no dialogue. Narrow panels follow their reappearance and Orochimaru's water bullets; Naruto dodges them toward camera. Dominant final panel: Naruto closes on both opponents, intact right shoulder plate still visible. "
  + SAY((4, N16_SPEAKER, "upper right", "IT WOULD HAVE BEEN CLEANER IF IT CRUSHED YOU.")) + SFX(1, "FSSSS") + SFX(2, "GROOO") + SFX(5, "FSSHH"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p15", dict(scene="action", light="day", cast="four", mood="scale", panels=5),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + MANDA.format(i=4) + MANGEKYO_EYE.format(i=5) + ENV.format(i=6) + ONLY(N16_SPEAKER, PALEONE, SPEC, "the colossal purple-grey serpent") +
  "FIVE PANELS. Water bullets continue as Naruto closes in. Dominant first panel: Kusanagi extends and pierces Naruto's RIGHT shoulder plate; a tight second panel confirms the broken plate and mark. Naruto's active EMS fires hard-edged black Amaterasu at Orochimaru. Final low-angle silhouette: Manda materializes through smoke, Naruto small below it; do not shrink Manda. "
  + SAY((1, N16_SPEAKER, "upper right", "CARELESS."), (2, PALEONE, "upper left", "THE BLADE CARRIES POISON."), (4, PALEONE, "middle left", "MANDA."),
        (5, "the colossal purple-grey serpent", "lower left", "YOU CALLED FOR HELP.")) + SFX(1, "GROOO") + SFX(5, "POOM"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "manda", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p16", dict(scene="action", light="day", cast="two", mood="overpowered", panels=6),
  FILL + N16_SWORD.format(i=1) + MANDA.format(i=2) + GUNBAI_V4.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, "the colossal purple-grey serpent") +
  "SIX LOW-ANGLE PANELS. Active-EMS Naruto's Manda-scaled wood hands fail to catch the serpent; Manda's fangs enter from the top edge. Naruto grips gunbai with both hands. Three small dodge beats pass through giant coils. Dominant bottom panel: gunbai catches Manda's head but Naruto is driven backward, boots carving dirt. New sash sword remains sheathed. "
  + SAY((2, N16_SPEAKER, "upper right", "A SNAKE IS NOT A HANDHOLD."), (6, "the colossal purple-grey serpent", "lower left", "SMALL UCHIHA.")) + SFX(6, "THUDD") + SFX(6, "SKRRR"),
  R("naruto_v4_armor_sword", "manda", "gunbai_v4", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p17", dict(scene="reveal", light="day", cast="two", mood="awe", panels=1),
  FILL + N16_SWORD.format(i=1) + MANDA.format(i=2) + SUSA_FINAL.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, "the colossal purple-grey serpent") +
  "BORDERLESS FULL-PAGE SPLASH. Low and distant: Manda's enormous coil makes a dark foreground ring. Within it the FINISHED OPAQUE ORANGE Susano'o rises around tiny readable Naruto: hooded head, two forward horns, plate guards, two swords fusing into one. Terrain, sky and dust remain legible, without orange haze. Orochimaru is not drawn. "
  + SAY((1, "the colossal purple-grey serpent", "upper left", "WHAT IS THAT?"), (1, OFF(PALEONE), "upper right", "A MANGEKYŌ DEFENCE.")) + SFX(1, "WOOOOOM"),
  R("naruto_v4_armor_sword", "manda", "susanoo_orange_final", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p18", dict(scene="action", light="day", cast="two", mood="cost", panels=6),
  FILL + N16_SWORD.format(i=1) + MANDA.format(i=2) + SUSA_FINAL.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, "the colossal purple-grey serpent") +
  "SIX PANELS. Wide top: orange blade wave skims ground and peels earth, Manda distant. Cropped action panels show Manda avoiding swings and the Susano'o blade falling. Bottom narrow panel: the finished form dissipates and active-EMS Naruto falls to one knee in white space. It must not remain active after this page. "
  + SAY((6, N16_SPEAKER, "lower right", "THEN BURN.")) + SFX(1, "SHRAAA") + SFX(6, "KROOM"),
  R("naruto_v4_armor_sword", "manda", "susanoo_orange_final", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p19", dict(scene="action", light="fire", cast="three", mood="rout", panels=5),
  FILL + N16_SWORD.format(i=1) + MANDA.format(i=2) + ORO.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, "the colossal purple-grey serpent", PALEONE) +
  "FIVE PANELS. Dominant upper panel: Manda crosses orange fire as Orochimaru leaps away tiny. Two vertical reactions show Manda shedding then charging. Bottom dominant crop: Naruto's active EMS left eye strains; separate hard-edged black flames seize Manda's head and tail. No Susano'o. "
  + SAY((3, "the colossal purple-grey serpent", "middle left", "I WILL REMEMBER THIS."), (5, N16_SPEAKER, "lower right", "LEAVE.")) + SFX(1, "FWHOO") + SFX(5, "SSSSS") + SFX(5, "POFF"),
  R("naruto_v4_armor_sword", "manda", "orochimaru", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p20", dict(scene="action", light="day", cast="three", mood="counterattack", panels=6),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + GUNBAI_V4.format(i=4) + MANGEKYO_EYE.format(i=5) + ENV.format(i=6) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "SIX PANELS. Kusanagi meets gunbai in a tight diagonal. Dominant center: active-EMS Naruto's two-headed wind dragon crosses readable ground, with separate hard-edged Amaterasu tongues threaded through it. Bottom panels: exhausted Kabuto stumbles in and Naruto catches his arm. "
  + SAY((3, N16_SPEAKER, "center left", "WIND DRAGON."), (3, N16_SPEAKER, "center right", "AMATERASU.")) + SFX(3, "WRAAASH"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "gunbai_v4", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p21", dict(scene="interrogation", light="day", cast="two", mood="cold", panels=6),
  FILL + N16_SWORD.format(i=1) + KAB.format(i=2) + MANGEKYO_EYE.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, SPEC) +
  "SIX PANELS. Active-EMS Naruto slams Kabuto down and pins his arm. Dominant lower panel is a quiet Tsukuyomi moment: Kabuto close against flat black, one ring-like eye reflection. Final small panel: Kabuto falls; the arm break is cropped and implied, not anatomically explicit. "
  + SAY((2, N16_SPEAKER, "upper right", "EXPLAIN HOW YOU REPAIR YOURSELF."), (3, SPEC, "middle left", "I WOULD RATHER DIE."),
        (5, N16_SPEAKER, "lower right", "THEN YOU CAN ANSWER SOMEWHERE ELSE.")) + SFX(2, "KRAK"),
  R("naruto_v4_armor_sword", "kabuto", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p22", dict(scene="action", light="day", cast="three", mood="escape", panels=5),
  FILL + N16_SWORD.format(i=1) + ORO.format(i=2) + KAB.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ONLY(N16_SPEAKER, PALEONE, SPEC) +
  "FIVE PANELS. Active-EMS Naruto uses overlapping kick-and-slam silhouettes against a flat white speed-line field, never a row. Lower panels tighten to Naruto's boot on Orochimaru's chest. He then DRAWS THE NEW PLAIN SASH SWORD and strikes through Orochimaru's neck in stylised non-gory comic action: hard ink silhouette, no anatomical detail. Next panel shows head and body reconnecting through flat snake shapes. Final diagonal snake mass escapes carrying Kabuto. Stop at their escape. "
  + SAY((3, N16_SPEAKER, "lower right", "WHERE IS IT?"), (4, PALEONE, "lower left", "YOU WILL NOT KEEP ME.")) + SFX(1, "THOOM") + SFX(5, "SSSSSK"),
  R("naruto_v4_armor_sword", "orochimaru", "kabuto", "mangekyo_design", "env_oto_broken_exterior"), "high"),

 ("p23", dict(scene="aftermath", light="day", cast="two", mood="depleted", panels=4),
  FILL + N16_SWORD.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, "the split black-and-white plant creature") +
  "FOUR PANELS. Top wide empty battlefield: smoke and escape trail gone. Dominant middle: Naruto kneels, armour scraped, RIGHT shoulder plate broken, gunbai planted as a cane; no triumph pose. Two narrow panels show Zetsu rising and Naruto's EMS deactivating to normal eyes. "
  + SAY((2, N16_SPEAKER, "upper right", "THAT COST MORE THAN IT SHOULD HAVE."), (3, "the split black-and-white plant creature", "middle left", "YOU MADE HIM SUFFER FIRST."),
        (4, N16_SPEAKER, "lower right", "NEXT TIME IS SHORTER. FIND THE GIRL.")) + SFX(1, "TSSS"),
  R("naruto_v4_armor_sword", "zetsu", "gunbai_v4", "env_oto_broken_exterior"), "high"),

 ("p24", dict(scene="departure", light="day", cast="two", mood="unresolved", panels=2),
  FILL + N16_SWORD.format(i=1) + ZET.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, "the split black-and-white plant creature") +
  "TWO PANELS, END PAGE. Top wide: Naruto and Zetsu leave the ruined Oto base in opposite depth layers—Naruto a small armoured teen walking toward horizon, Zetsu cropped foreground sinking into grass. Bottom narrow close-up: Naruto's hand passes over the NEW SASH SWORD hilt without drawing it; the damaged right shoulder plate remains visible. End on search, not victory. "
  + CAP(1, "upper left", "THE MASK WAS NOT THERE.") + SAY((2, OFF(N16_SPEAKER), "lower right", "WE SEARCH THE OTHER NESTS.")) + SFX(1, "KLANG… KLANG…"),
  R("naruto_v4_armor_sword", "zetsu", "env_oto_broken_exterior"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch05" / "raw", HERE / "v4ch05" / "ledger.json")
