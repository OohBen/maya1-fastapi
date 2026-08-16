"""Volume 4, Chapter 8 — "The Tower". 20 pages.

Source: fic ch10:417-493; ch11:7-117; plus the isolated ch11:119 "THREE DAYS
LATER" card. The response battle remains Chapter 9 material.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, ONLY, R, SAY, SFX, TITLE  # noqa: E402
from prompts_v4 import (AO_V4, AO_V4_SPEAKER, CHOJURO_V4, CHOJURO_V4_SPEAKER,
                        KURAMA_FULL, KURAMA_SPEAKER, L_KIRI_MOON,
                        KIRI_REBELS, L_KIRI_TENT, MEI_V4, MEI_V4_SPEAKER,
                        N16_BLACK, N16_SPEAKER, YUGAO_V4,
                        YUGAO_V4_SPEAKER)  # noqa: E402

SCOUT = "unnamed adult Kiri rebel scout or officer from the bound Kiri rebel crowd reference"
L_HILL = L_KIRI_MOON
L_CAMP = "Lighting: cold blue-grey dawn or day mist over wet canvas, with figures and tents kept legible. "
L_TOWER = "Lighting: flat storm-grey daylight and sea mist; the distant Mizukage tower is a separate landmark, never a rebel building. "
L_NARUTO_TENT = "Lighting: muted camp-lamp amber inside Naruto's spare tent, blue-grey camp activity outside. "


PAGES = [
 ("p01", dict(scene="establishing", light="moon", cast="small_group", mood="watchful", panels=1),
  N16_BLACK.format(i=1) + KIRI_REBELS.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, SCOUT) +
  "CHAPTER OPENING SPLASH. Borderless vertical moonlit hill outside the Kiri rebel camp. The "
  "approximately sixteen-year-old blond teen sits small in profile near the crest, black outfit only, "
  "with the empty field stretching away. Exactly five unconscious adult scouts lie peacefully at "
  "different depths at the foot of the hill; one boot and one shoulder crop the foreground. They are "
  "sleeping, uninjured. Keep the upper third calm for title and time card. " + L_HILL +
  TITLE("THE TOWER", "upper third sky") + CAP(1, "lower left", "THREE NIGHTS LATER."),
  R("naruto_v4_black", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "high"),

 ("p02", dict(scene="surveillance", light="moon", cast="small_group", mood="bored", panels=6),
  FILL + N16_BLACK.format(i=1) + KIRI_REBELS.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, SCOUT) +
  "SIX uneven panels. PANEL 1 (narrow letterbox): Naruto's single visible left eye has a controlled "
  "blood-red Sharingan, cropped by all edges. PANELS 2-5 (small, unequal): five separate peaceful "
  "details establish each scout sleeping rather than injured: loose hand, boot, slow breath, relaxed "
  "shoulder, closed eye. PANEL 6 (dominant wide bottom): Naruto scans the clear field from the crest, "
  "bored and entirely unarmoured. " + L_HILL +
  CAP(6, "upper left", "THE CAMP HAD BEEN QUIET.") +
  SAY((6, N16_SPEAKER, "lower right", "TOO QUIET.")),
  R("naruto_v4_black", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "high"),

 ("p03", dict(scene="dialogue", light="moon", cast="small_group", mood="guarded", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, SCOUT) +
  "FIVE uneven panels. Mei, the auburn-haired Kiri rebel leader in conservative dark-blue night "
  "clothes, climbs from below with a closed food container in foreground. Naruto remains seated high "
  "and distant. PANEL 1 is Mei climbing; PANEL 2 is the container; PANEL 3 shows the five sleeping "
  "scouts below; PANEL 4 Naruto in profile; PANEL 5 (dominant) puts Mei low in foreground and Naruto "
  "small at the crest. Never stage a side-by-side pose. " + L_HILL +
  SAY((3, MEI_V4_SPEAKER, "upper left", "WHAT HAPPENED TO THEM?"),
      (4, N16_SPEAKER, "upper right", "THEY ARE SLEEPING.")),
  R("naruto_v4_black", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "high"),

 ("p04", dict(scene="dialogue", light="moon", cast="two", mood="assessing", panels=6),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "SIX uneven panels. The closed food container stays between them. PANEL 1: Mei's cropped shoulder "
  "in foreground. PANEL 2: Naruto low and far looking over the field. PANEL 3: Mei assessing him. "
  "PANEL 4: Naruto accepts the container without looking at her. PANEL 5: his level expression. "
  "PANEL 6 (dominant wide): the distance remains between them. No suggestive camera or physical contact. " + L_HILL +
  SAY((1, MEI_V4_SPEAKER, "upper left", "AO'S OBSERVERS?"),
      (2, N16_SPEAKER, "upper right", "THEY WERE BECOMING A DISTRACTION."),
      (4, MEI_V4_SPEAKER, "lower left", "THEN EAT.")),
  R("naruto_v4_black", "mei_v4", "env_kiri_moonlit_hill"), "high"),

 ("p05", dict(scene="dialogue", light="moon", cast="two", mood="probing", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "FIVE uneven panels. PANEL 1: an empty moon and mist panel. PANEL 2: Mei in three-quarter view "
  "with a clear balloon shelf above. PANEL 3: Naruto's face cropped hard at the right edge, expression "
  "unchanged. PANEL 4: the food container, still closed. PANEL 5 (dominant): the two remain separated "
  "by broad grass and empty space. This is a clinical conversation, never flirtation or romance. " + L_HILL +
  SAY((2, MEI_V4_SPEAKER, "upper left", "MOST MEN MAKE THEIR INTEREST OBVIOUS."),
      (2, MEI_V4_SPEAKER, "lower right", "WHY DON'T YOU?")),
  R("naruto_v4_black", "mei_v4", "env_kiri_moonlit_hill"), "high"),

 ("p06", dict(scene="dialogue", light="moon", cast="two", mood="disconnected", panels=6),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "SIX uneven panels with flat midnight-blue and white reaction grounds. PANEL 1: Naruto's controlled "
  "red eye. PANEL 2: his gloved hand on the closed food container. PANEL 3: Mei's baffled profile. "
  "PANEL 4: a broad empty gap. PANEL 5: Naruto distant. PANEL 6 (dominant bottom): the two-shot "
  "remains separated by the gap. No flashback and no literal allusion imagery. " + L_HILL +
  SAY((1, N16_SPEAKER, "upper left", "I DO NOT THINK LIKE MOST MEN."),
      (3, MEI_V4_SPEAKER, "upper right", "THAT IS AN ANSWER WITHOUT AN ANSWER.")),
  R("naruto_v4_black", "mei_v4", "env_kiri_moonlit_hill"), "high"),

 ("p07", dict(scene="interiority", light="graphic", cast="two", mood="clinical", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "FIVE uneven graphic panels on flat black and white. PANEL 1: Naruto's face in flat black. PANEL 2: "
  "a simple Uchiha fan crest beside empty chairs, a symbolic objective only. PANEL 3: a closed notebook "
  "and training weights. PANEL 4: Mei's surprised but composed reaction. PANEL 5 (dominant): Naruto "
  "and Mei facing across empty black ground. This page means instrumental planning, never sex education, "
  "a memory, or an encounter. " +
  SAY((1, N16_SPEAKER, "upper left", "RESTORING MY CLAN IS AN OBJECTIVE."),
      (2, N16_SPEAKER, "upper right", "KNOWLEDGE IS PART OF AN OBJECTIVE."),
      (4, MEI_V4_SPEAKER, "lower left", "YOU MAKE EVERYTHING SOUND LIKE TRAINING.")),
  R("naruto_v4_black", "mei_v4"), "high"),

 ("p08", dict(scene="departure", light="moon", cast="small_group", mood="closed", panels=6),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, SCOUT) +
  "SIX uneven panels. Naruto rises and starts down the slope. Mei follows at a distance. PANELS 1-3 "
  "track Naruto's rise, Mei's stillness, and the path. PANEL 4 shows the five scouts now awake and "
  "retreating into mist; they are not attacked again. PANEL 5 is Naruto's back. PANEL 6 (dominant) "
  "shows both figures at different depths as he moves away. " + L_HILL +
  SAY((2, MEI_V4_SPEAKER, "upper left", "YOU CANNOT LIVE ONLY FOR OBJECTIVES."),
      (5, N16_SPEAKER, "lower right", "I DID NOT COME HERE TO DISCUSS THIS.")),
  R("naruto_v4_black", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "high"),

 ("p09", dict(scene="departure", light="moon", cast="two", mood="closed", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "FIVE uneven descent panels in staggered depth. PANEL 1: Naruto's back cropped in foreground, Mei "
  "small behind. PANEL 2: the hand shutting the food container. PANEL 3: Mei on the slope. PANEL 4: "
  "the path disappears toward dim camp light. PANEL 5 (dominant wide): Naruto walks ahead without "
  "looking back. " + L_HILL +
  SAY((1, N16_SPEAKER, "upper left", "A MIND IS TRAINED TOWARD A RESULT."),
      (3, MEI_V4_SPEAKER, "upper right", "LIKE A MACHINE?"),
      (5, N16_SPEAKER, "lower left", "IF IT MUST BE.")),
  R("naruto_v4_black", "mei_v4", "env_kiri_moonlit_hill", "env_kiri_rebel_camp"), "high"),

 ("p10", dict(scene="aftermath", light="moon", cast="two", mood="unanswered", panels=4),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "FOUR uneven panels. PANEL 1: Naruto in hard profile says Mei is a distraction. PANEL 2: tiny inset "
  "of Mei's realizing face. PANEL 3 (dominant): Naruto walks out of panel down the hill, leaving a "
  "large empty wake. PANEL 4 (tall): Mei alone beneath the moon, frozen as the word lands. No touch, "
  "blush, kiss, or romantic payoff. " + L_HILL +
  SAY((1, N16_SPEAKER, "upper left", "YOU ARE PROVING TO BE A DISTRACTION."),
      (2, MEI_V4_SPEAKER, "upper right", "HOW?"),
      (3, N16_SPEAKER, "lower left", "YOU HAVE NOT FOUND A SUITABLE MATE.")),
  R("naruto_v4_black", "mei_v4", "env_kiri_moonlit_hill"), "high"),

 ("p11", dict(scene="time_passage", light="dawn", cast="solo", mood="restless", panels=3),
  FILL + N16_BLACK.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER) +
  "THREE uneven panels. PANEL 1 (dominant): an empty misty Kiri rebel camp at dawn, no visible people. "
  "PANEL 2 (small): Naruto sits alone at an uneventful day watch, bored, black outfit only. PANEL 3 "
  "(narrow black-bordered): the time card. This is a one-week passage and introduces no approaching "
  "force, observer chorus, or battle preparation. " + L_CAMP +
  CAP(2, "lower right", "STILL NO BATTLE.") + CAP(3, "center", "ONE WEEK LATER."),
  R("naruto_v4_black", "env_kiri_rebel_camp"), "high"),

 ("p12", dict(scene="command_conflict", light="tent", cast="small_group", mood="fracturing", panels=7),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + CHOJURO_V4.format(i=4) +
  KIRI_REBELS.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER, SCOUT) +
  "SEVEN uneven command-tent panels. PANEL 1: Mei at the map desk. PANEL 2: Ao's implanted-eye "
  "silhouette in extreme foreground. PANEL 3: Chojuro small near the rear. PANEL 4: exactly three "
  "unnamed adult rebel officers layered behind the map. PANEL 5: Naruto enters without ceremony. "
  "PANEL 6: Mei's controlled reaction. PANEL 7 (dominant bottom): Naruto states his decision while "
  "the group remains at staggered depths, never a meeting lineup. Mei is visibly the rebel leader. " + L_KIRI_TENT +
  SAY((7, N16_SPEAKER, "upper left", "I AM GOING TO FORCE YAGURA OUT."),
      (6, MEI_V4_SPEAKER, "upper right", "WE ARE NOT READY."),
      (2, AO_V4_SPEAKER, "lower left", "NEITHER IS HE.")),
  R("naruto_v4_black", "mei_v4", "ao_v4", "chojuro_v4", "kiri_rebel_mob", "env_mei_tent"), "high"),

 ("p13", dict(scene="command_conflict", light="tent", cast="small_group", mood="fracturing", panels=6),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + CHOJURO_V4.format(i=4) +
  KIRI_REBELS.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER, SCOUT) +
  "SIX uneven panels; the argument fractures across close-ups instead of becoming a meeting tableau. "
  "PANEL 1: a map hand. PANEL 2: Ao's guarded eye. PANEL 3: Mei's restrained expression. PANEL 4: "
  "Naruto at the tent opening turned away. PANEL 5: Chojuro silent in the rear. PANEL 6 (dominant): "
  "Naruto's departure line crosses the tent's deep space; the three officers remain background-only. " + L_KIRI_TENT +
  SAY((2, AO_V4_SPEAKER, "upper left", "THIS IS NOT YOUR COMMAND."),
      (4, N16_SPEAKER, "upper right", "THEN DO NOT FOLLOW."),
      (3, MEI_V4_SPEAKER, "lower left", "YOU WOULD START A WAR BEFORE MY PEOPLE ARE READY?")),
  R("naruto_v4_black", "mei_v4", "ao_v4", "chojuro_v4", "kiri_rebel_mob", "env_mei_tent"), "high"),

 ("p14", dict(scene="decision", light="tent", cast="four", mood="resolved", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + CHOJURO_V4.format(i=4) +
  ENV.format(i=5) + ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "FIVE uneven panels. PANEL 1: Naruto exits. PANEL 2 (small): Mei catches his wrist; it is a direct "
  "leadership stop, not intimacy. PANEL 3: he turns only enough to meet her eyes. PANEL 4: Mei lets "
  "go. PANEL 5 (dominant): Mei releases him while Ao and Chojuro stand behind her at a distance; "
  "she chooses to follow after recognizing she cannot physically stop him. " + L_KIRI_TENT +
  SAY((3, N16_SPEAKER, "upper left", "THEY ARE SAFE UNLESS THEY STAND IN MY WAY."),
      (5, MEI_V4_SPEAKER, "lower right", "AO. CHOJURO. COME WITH US.")),
  R("naruto_v4_black", "mei_v4", "ao_v4", "chojuro_v4", "env_mei_tent"), "high"),

 ("p15", dict(scene="approach", light="mist", cast="four", mood="watchful", panels=5),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + CHOJURO_V4.format(i=4) +
  ENV.format(i=5) + ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "FIVE uneven silent-travel panels. Naruto remains in his plain black outfit with no armour, gunbai, "
  "or sword. Mist and wet ground place the figures "
  "at four different depth scales. PANEL 3: Ao scans the horizon with his implanted Byakugan. PANEL 5 "
  "(dominant wide): the distant Mizukage tower appears as a separate landmark. No Yagura or army is "
  "visible. " + L_TOWER +
  CAP(1, "upper left", "ONE HOUR LATER.") +
  SAY((3, AO_V4_SPEAKER, "lower right", "NO AMBUSH.")),
  R("naruto_v4_black", "mei_v4", "ao_v4", "chojuro_v4", "env_mizukage_tower"), "high"),

 ("p16", dict(scene="summoning", light="mist", cast="four", mood="controlled", panels=4),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + CHOJURO_V4.format(i=4) +
  ENV.format(i=5) + ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "FOUR uneven panels. PANEL 1: Naruto stops well ahead of the others and sets a clear safety line. "
  "PANEL 2: his hands form seals in foreground. PANEL 3: a summoning seal spreads over wet earth. "
  "PANEL 4 (dominant): controlled smoke begins to eclipse the distant Mizukage tower while Mei, Ao, "
  "and Chojuro remain behind the line. No seal breaking, possession, or rampage. " + L_TOWER +
  SAY((1, N16_SPEAKER, "upper left", "STAY THERE."),
      (2, N16_SPEAKER, "lower right", "SUMMONING JUTSU.")) + SFX(4, "POOF"),
  R("naruto_v4_black", "mei_v4", "ao_v4", "chojuro_v4", "env_mizukage_tower"), "high"),

 ("p17", dict(scene="summoning", light="mist", cast="five", mood="awe", panels=1),
  N16_BLACK.format(i=1) + KURAMA_FULL.format(i=2) + MEI_V4.format(i=3) + AO_V4.format(i=4) +
  CHOJURO_V4.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, KURAMA_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "BORDERLESS FULL-PAGE controlled reveal. Kurama, an enormous full nine-tailed fox with red slit "
  "eyes, stands in the clearing with tails slow and contained. Naruto, in the plain black outfit with "
  "no armour, gunbai, or sword, "
  "is small at one paw with arms folded. Mei, Ao, and Chojuro are tiny at the safe panel edge, recoiling. "
  "The tower remains distant and intact. Kurama is free and cooperative, not possessed, feral, or attacking. " + L_TOWER +
  SAY((1, KURAMA_SPEAKER, "upper left", "WHY HAVE YOU CALLED ME?"),
      (1, N16_SPEAKER, "lower right", "ONE TASK.")),
  R("naruto_v4_black", "kurama_full", "mei_v4", "ao_v4", "chojuro_v4", "env_mizukage_tower"), "high"),

 ("p18", dict(scene="command", light="mist", cast="five", mood="controlled", panels=6),
  FILL + N16_BLACK.format(i=1) + KURAMA_FULL.format(i=2) + MEI_V4.format(i=3) + AO_V4.format(i=4) +
  CHOJURO_V4.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, KURAMA_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "SIX uneven panels. PANEL 1: Kurama's slit eye. PANEL 2: Naruto's unmoved profile. PANEL 3: Ao "
  "stunned. PANEL 4: Chojuro stunned and silent. PANEL 5: Mei calculating. PANEL 6 (dominant): "
  "Kurama and the distant Mizukage tower share a direct sightline. The dry sleep complaint is not "
  "comic or chibi; the instruction is one bounded target, the tallest building only. " + L_TOWER +
  SAY((1, KURAMA_SPEAKER, "upper left", "MAKE IT QUICK."),
      (2, N16_SPEAKER, "upper right", "FIRE AT THE TALLEST BUILDING."),
      (6, KURAMA_SPEAKER, "lower left", "THEN I RETURN TO MY NAP.")),
  R("naruto_v4_black", "kurama_full", "mei_v4", "ao_v4", "chojuro_v4", "env_mizukage_tower"), "high"),

 ("p19", dict(scene="strike", light="mist", cast="five", mood="decisive", panels=5),
  FILL + N16_BLACK.format(i=1) + KURAMA_FULL.format(i=2) + MEI_V4.format(i=3) + AO_V4.format(i=4) +
  CHOJURO_V4.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, KURAMA_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER, CHOJURO_V4_SPEAKER) +
  "FIVE uneven panels. PANEL 1 (dominant wide): a compact bijuudama leaves Kurama toward only the "
  "distant Mizukage tower, peeling a narrow directional scar through empty ground. PANEL 2: the tower "
  "impact. PANEL 3: a contained distant blast cloud; no civilians or surrounding city are hit. PANEL 4: "
  "Naruto already turns away. PANEL 5: Kurama departs in summoning smoke. This is a targeted military "
  "strike, not a citywide catastrophe. " + L_TOWER +
  SAY((4, N16_SPEAKER, "upper left", "YOU MAY GO."),
      (4, N16_SPEAKER, "lower right", "YAGURA WILL ANSWER IN DAYS.")) + SFX(2, "DOOOOM"),
  R("naruto_v4_black", "kurama_full", "mei_v4", "ao_v4", "chojuro_v4", "env_mizukage_tower"), "high"),

 ("p20", dict(scene="consequence", light="tent", cast="two", mood="withdrawal", panels=6),
  FILL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
  "SIX uneven consequence panels. PANEL 1: distant anonymous camp activity is visible only beyond the "
  "tent opening, with no distinct person. PANEL 2: inside Naruto's tent, Yugao sits in shadow "
  "on his bed. PANEL 3: her eye recalls Konoha's old terror through hard abstract fox-shadow shapes, "
  "not a flashback scene. PANEL 4: Naruto nods once. PANEL 5 (dominant): he leaves through the tent flap. PANEL 6 "
  "is an empty black field carrying only the final time card. No armour, battle, Zetsu, army, or next "
  "chapter preparation appears after the card. " + L_NARUTO_TENT +
  SAY((3, YUGAO_V4_SPEAKER, "upper left", "KONOHA WILL FEAR WHAT YOU CAN RELEASE."),
      (5, N16_SPEAKER, "lower right", "DO NOT CONCERN YOURSELF WITH WHAT I DO.")) +
  CAP(6, "center", "THREE DAYS LATER."),
  R("naruto_v4_black", "yugao_v4", "env_kiri_rebel_camp", "env_naruto_tent"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch08" / "raw", HERE / "v4ch08" / "ledger.json")
