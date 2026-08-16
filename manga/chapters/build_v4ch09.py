"""Volume 4, Chapter 9 — "What Are You?". 24 pages.

Source: fic ch11:119-375.  The chapter ends before Yagura arrives at :377.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import (CAP, ENV, FILL, ONLY, OFF, R, SAY, SFX, TITLE, ZET)  # noqa: E402
from prompts_v4 import (AO_V4, AO_V4_SPEAKER, GUNBAI_V4, MANGEKYO_EYE, MEI_V4,
                        MEI_V4_SPEAKER, N16_ARMOR, N16_SPEAKER, N16_SWORD, SUSA_FINAL,
                        THOUGHT, YUGAO_V4, YUGAO_V4_SPEAKER)  # noqa: E402


ZETSU = "the split black-and-white plant creature"
REBEL = "unnamed Kiri rebel silhouettes in standard wet-weather shinobi gear"
FORCE = "unnamed Yagura-force shinobi silhouettes in standard armour"
L_BATTLE = ("Lighting: flat hard storm-grey daylight, wet ground and low fog remain legible through "
            "every hard-edged opaque technique effect. ")


PAGES = [
 ("p01", dict(scene="establishing", light="overcast", cast="two", mood="cold", panels=1),
  N16_ARMOR.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, ZETSU, FORCE) +
  "CHAPTER OPENING BORDERLESS SPLASH. Naruto, an approximately sixteen-year-old armoured teen, walks "
  "alone across enormous wet Kiri ground toward a distant broken line of anonymous force silhouettes. "
  "He is small, not posed; the purple-black gunbai is strapped on his back. Zetsu rises at the near "
  "edge in profile. Keep the upper third calm grey sky for the title. " + L_BATTLE +
  TITLE("WHAT ARE YOU?", "quiet upper third of the grey sky") +
  CAP(1, "lower left", "THREE DAYS LATER.") +
  SAY((1, ZETSU, "lower right", "THEY ARE MOVING."),
      (1, N16_SPEAKER, "lower left", "THEN WE BEGIN.")),
  R("naruto_v4_armor", "zetsu", "gunbai_v4", "env_kiri_battlefield_open"), "high"),

 ("p02", dict(scene="dialogue", light="overcast", cast="two", mood="controlled", panels=5),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, MEI_V4_SPEAKER, REBEL, FORCE) +
  "FIVE uneven panels. PANEL 1 (dominant wide): Mei's cropped foreground shoulder reaches toward Naruto, "
  "who is already walking away in the far midground; her rebel line remains distant. PANEL 2: his hand "
  "checks the gunbai strap. PANEL 3: Mei's eye. PANEL 4: the overwhelming opposing force across open wet "
  "ground. PANEL 5: Naruto keeps walking, leaving Mei behind. No Kurama appears. " + L_BATTLE +
  SAY((1, MEI_V4_SPEAKER, "upper left", "YOU WILL FACE THEM ALONE?"),
      (2, N16_SPEAKER, "upper right", "KEEP YOUR PEOPLE BACK."),
      (3, MEI_V4_SPEAKER, "lower left", "AND THE KYUBI?"),
      (5, N16_SPEAKER, "lower right", "NOT FOR THIS.")),
  R("naruto_v4_armor", "mei_v4", "env_kiri_battlefield_open"), "high"),

 ("p03", dict(scene="reaction", light="overcast", cast="group", mood="worried", panels=6),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + YUGAO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, YUGAO_V4_SPEAKER, REBEL, FORCE) +
  "SIX uneven reaction panels from inside the rebel line. Cropped anonymous shoulders and heads frame Naruto "
  "as a distant armoured figure. Yugao starts forward; Mei's arm stops her. A generic rebel eye measures the "
  "distance. End on Naruto as a small silhouette between the two irregular armies. Never arrange Mei, Yugao, "
  "and Naruto as a lineup. " + L_BATTLE +
  SAY((3, YUGAO_V4_SPEAKER, "upper left", "HE CANNOT GO ALONE."),
      (4, MEI_V4_SPEAKER, "upper right", "WATCH.")),
  R("naruto_v4_armor", "mei_v4", "yugao_v4", "env_kiri_battlefield_open"), "high"),

 ("p04", dict(scene="action", light="overcast", cast="group", mood="dismissive", panels=6),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "SIX uneven panels inside the opposing force, keeping every fighter anonymous. PANEL 1: a cropped generic "
  "profile dismisses the lone teen. PANEL 2: ranks overlap at four depths. PANEL 3: Naruto's boots enter a "
  "low letterbox. PANEL 4: he launches. PANEL 5 (dominant): hard-edged orange flame wave opens a corridor, "
  "leaving ground and recoiling silhouettes visible. PANEL 6: Naruto has room to move. Non-graphic impacts only. " + L_BATTLE +
  SAY((1, FORCE, "upper left", "ONE FIGHTER?"),
      (3, N16_SPEAKER, "upper right", "SHALL WE?")) +
  SFX(5, "MAJESTIC FLAME DESTROYER", "Large at the flame edge; do not conceal the escape corridor."),
  R("naruto_v4_armor", "env_kiri_battlefield_open"), "high"),

 ("p05", dict(scene="action", light="overcast", cast="group", mood="measured", panels=7),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "SEVEN uneven, fast panels. Naruto tests taijutsu: duck a sword, turn a generic attacker aside with a kick, "
  "and pass through irregular attackers without lingering on impact. Finish with him springing clear while four "
  "Naruto clones appear at staggered distances and depart in separate directions. The clones are clearly Naruto, "
  "not new people. " + L_BATTLE +
  CAP(1, "upper left", "FIRST: THEIR SPEED.") +
  THOUGHT((6, N16_SPEAKER, "upper right", "INSUFFICIENT.")),
  R("naruto_v4_armor", "env_kiri_battlefield_open"), "high"),

 ("p06", dict(scene="action", light="overcast", cast="group", mood="escalating", panels=6),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "SIX uneven panels. Naruto's palms strike wet earth; pale wooden spikes rise diagonally between scattered "
  "anonymous troops, forcing groups apart without piercing bodies. A water dragon and fire dragon collide in a "
  "tall centre panel and turn to steam. In the final dominant sky panel, four Naruto clone silhouettes at four "
  "compass points hold one immense fire cloud over the field. The field and exits stay visible below. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "WOOD RELEASE: PIERCING SPIKES."),
      (3, FORCE, "upper right", "WATER DRAGON!"),
      (4, N16_SPEAKER, "lower left", "FIRE DRAGON.")),
  R("naruto_v4_armor", "env_kiri_battlefield_open"), "high"),

 ("p07", dict(scene="reaction", light="overcast", cast="group", mood="uneasy", panels=5),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + YUGAO_V4.format(i=3) + AO_V4.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, REBEL) +
  "FIVE uneven panels. The dominant panel is the suspended fire cloud reflected in Ao's implanted eye; Naruto "
  "is tiny and centered below it, visibly controlling the whole overhead shape. Mei and Yugao receive separate "
  "small reaction panels. Keep the rebel line far behind Naruto and make the cloud's edge readable against the sky. " + L_BATTLE +
  SAY((2, REBEL, "upper left", "WHAT IS THAT?"),
      (1, AO_V4_SPEAKER, "upper right", "A TECHNIQUE HELD IN THE AIR.")) +
  THOUGHT((4, MEI_V4_SPEAKER, "lower left", "HOW MUCH CHAKRA DOES THAT TAKE?")),
  R("naruto_v4_armor", "mei_v4", "yugao_v4", "ao_v4", "env_kiri_battlefield_open"), "high"),

 ("p08", dict(scene="action", light="overcast", cast="group", mood="terrifying", panels=3),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "THREE deliberately uneven panels. PANEL 1 (small): Naruto holds a tiger seal beneath the cloud. PANEL 2 "
  "(dominant wide): black-and-orange overhead of the cloud starting to rain flat, opaque fire drops. PANEL 3 "
  "(low bottom): fleeing anonymous silhouette legs and falling flame drops, with wet ground channels and escape "
  "routes still visible. No close-up injuries or burning bodies. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "CRYING HEAVENS.")) +
  SFX(2, "CRYING HEAVENS", "Hard-edged lettering in the cloud, clear of Naruto and the horizon."),
  R("naruto_v4_armor", "env_kiri_battlefield_open"), "high"),

 ("p09", dict(scene="aftermath", light="overcast", cast="group", mood="revulsed", panels=6),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + YUGAO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, YUGAO_V4_SPEAKER, FORCE) +
  "SIX uneven aftermath panels, non-graphic: crumbled earth walls, a collapsed water shield, fighters fleeing "
  "the rain edge, dropped weapons in wet dirt, and one silent panel of the fire cloud overhead. Mei sees Naruto "
  "in profile while Yugao sees the new gaps in the force. The rain did not cover the whole field. " + L_BATTLE +
  CAP(1, "upper left", "THE RAIN DID NOT REACH THE WHOLE FIELD.") +
  THOUGHT((6, MEI_V4_SPEAKER, "lower right", "HE NEVER NEEDED THE KYUBI.")),
  R("naruto_v4_armor", "mei_v4", "yugao_v4", "env_kiri_battlefield_open"), "high"),

 ("p10", dict(scene="action", light="overcast", cast="group", mood="experimental", panels=5),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "FIVE uneven panels with one clear direction: cloud to sphere to ground. Naruto looks up with controlled "
  "satisfaction. The four clones guide the remaining cloud over a dense surviving group, compress it into a "
  "small swirling sphere, and a final clone sends one thin lightning stroke down. The clones disperse before "
  "the sphere reaches the ground. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "NOW, FIREWORKS.")) +
  SFX(5, "LIGHTNING FLAME EXPLOSION", "Along the descending lightning; leave the sphere readable."),
  R("naruto_v4_armor", "env_kiri_battlefield_open"), "high"),

 ("p11", dict(scene="splash", light="overcast", cast="group", mood="shocked", panels=1),
  N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "BORDERLESS SINGLE CRATER EVENT. A flat red-orange starburst and white lightning branches break across an "
  "identifiable wet field; angular debris radiates outward and tiny anonymous figures are thrown back at different "
  "rotations. Naruto is a small armoured silhouette at a safe edge. Ground and horizon remain visible; no figures "
  "or bodies appear in the blast centre. This is the smaller lightning-fire crater, not the later Susano'o crater. " + L_BATTLE +
  SFX(1, "BOOM", "Large at the shockwave edge, not over the crater centre."),
  R("naruto_v4_armor", "env_kiri_battlefield_crater"), "high"),

 ("p12", dict(scene="aftermath", light="overcast", cast="three", mood="analytical", panels=6),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER) +
  "SIX uneven orientation panels. A high angle establishes the first, smaller crater. Ao's cropped profile is "
  "foreground; Mei is small at a separate depth; Naruto is far beyond, inspecting the result rather than posing. "
  "Keep the crater rim and the observer distance legible. " + L_BATTLE +
  SAY((2, MEI_V4_SPEAKER, "upper left", "WHAT HAPPENED?"),
      (3, AO_V4_SPEAKER, "upper right", "THE CLONES COMPRESSED THE FIRE."),
      (4, AO_V4_SPEAKER, "lower left", "THEN LIGHTNING DESTABILIZED IT.")) +
  THOUGHT((6, N16_SPEAKER, "lower right", "IT HELD.")),
  R("naruto_v4_armor", "mei_v4", "ao_v4", "env_kiri_battlefield_crater"), "high"),

 ("p13", dict(scene="action", light="overcast", cast="group", mood="adapting", panels=7),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "SEVEN uneven panels showing the survivors learn. A water jet meets Naruto's fireball; a second jet reinforces "
  "it and pushes it back. Naruto clears the smaller fireball, lands amid scattered anonymous fighters, and "
  "reorients. Attackers occupy different depths and directions, never a uniform firing line. " + L_BATTLE +
  CAP(1, "upper left", "THE SURVIVORS STOPPED RUSHING HIM.") +
  THOUGHT((7, N16_SPEAKER, "lower right", "BETTER.")),
  R("naruto_v4_armor", "env_kiri_battlefield_crater"), "high"),

 ("p14", dict(scene="action", light="overcast", cast="group", mood="coordinated", panels=6),
  FILL + N16_ARMOR.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, FORCE) +
  "SIX uneven barrage panels. Naruto uses a generic attacker as a moving silhouette shield, deflects an explosive "
  "tag, sweeps tagged kunai aside with Wind Palm, escapes earth spikes, then a wind dragon catches him. Final "
  "panel: full-body three-quarter Naruto lands crouched and dusts himself; scratches mark red armour, never skin. " + L_BATTLE +
  SAY((3, N16_SPEAKER, "upper left", "WIND PALM."),
      (4, FORCE, "upper right", "KEEP HIM MOVING!"),
      (6, N16_SPEAKER, "lower left", "THEY ARE COORDINATING.")),
  R("naruto_v4_armor", "env_kiri_battlefield_crater"), "high"),

 ("p15", dict(scene="action", light="overcast", cast="group", mood="answering", panels=4),
  FILL + N16_ARMOR.format(i=1) + GUNBAI_V4.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "FOUR uneven panels. A hundred shuriken form a dark, irregular sky swarm. Naruto unstraps the purple-black "
  "gunbai and swings it across the dominant panel; one visible wind arc redirects projectiles to the frame edges. "
  "Small panels establish three wind tornadoes, then the final panel merges them into one. " + L_BATTLE +
  SAY((4, N16_SPEAKER, "lower right", "WIND TORNADO.")) +
  SFX(2, "WHUMM", "Along the gunbai wind arc; never cover the fan or redirected projectiles."),
  R("naruto_v4_armor", "gunbai_v4", "env_kiri_battlefield_crater"), "high"),

 ("p16", dict(scene="action", light="overcast", cast="group", mood="dread", panels=4),
  FILL + N16_ARMOR.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "FOUR uneven panels. PANEL 1 is an eyes-only letterbox: Naruto's visible eye establishes the exact Eternal "
  "Mangekyo pattern from its reference. PANEL 2: the merged tornado catches opaque black flame. PANEL 3 "
  "(dominant): the black-flame tornado crosses the field while water attacks strike its edge and fail; it stays "
  "contained and ground remains visible. PANEL 4: black flame patches remain on the wet ground from high above. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "AMATERASU.")) +
  CAP(4, "lower right", "WATER COULD NOT PUT IT OUT."),
  R("naruto_v4_armor", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p17", dict(scene="action", light="overcast", cast="group", mood="contested", panels=5),
  FILL + N16_ARMOR.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "FIVE uneven panels. Naruto releases another broad flame wave. Multiple anonymous water walls join into one "
  "barrier; their contest creates a split dominant panel of steam, with Naruto already a small moving shape through "
  "it. Steam may divide space but must not hide the direction of either force. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "MAJESTIC FLAME DESTROYER."),
      (3, FORCE, "upper right", "WATER ENCAMPMENT WALL!")),
  R("naruto_v4_armor", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p18", dict(scene="action", light="overcast", cast="group", mood="trapping", panels=5),
  FILL + N16_ARMOR.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "FIVE uneven panels. Naruto comes through steam from above and releases Majestic Fire Destruction, forcing the "
  "remaining force farther apart. One calm insert of his level eye interrupts the hard impacts, showing a measured "
  "test. Final panel: two anonymous fighters converge from opposite sides while a wider ring prepares hand seals. " + L_BATTLE +
  SAY((1, FORCE, "upper left", "HE IS COMING!"),
      (3, N16_SPEAKER, "upper right", "MAJESTIC FIRE DESTRUCTION.")),
  R("naruto_v4_armor", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p19", dict(scene="action", light="overcast", cast="group", mood="trap", panels=6),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "SIX deliberately readable close-combat panels. Naruto draws the plain straight sword from his left sash before "
  "using it: parry the front attacker, turn, block the rear attacker, then kick the first away. Do not show an "
  "impalement. Cut from Naruto's fixed eye to the surviving decoy's alarm and the surrounding anonymous attackers "
  "forming hand seals. The sword stays visible in every relevant action panel. " + L_BATTLE +
  SAY((5, N16_SPEAKER, "upper left", "DECOYS."),
      (6, FORCE, "lower right", "NOW!")),
  R("naruto_v4_armor_sword", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p20", dict(scene="action", light="overcast", cast="group", mood="impossible", panels=3),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "THREE unequal panels. PANEL 1 (dominant): the first multi-element volley converges on Naruto in one dense, "
  "hard-edged impact, with no invented shield or explanatory mechanism. PANEL 2: dust clears; Naruto stands intact "
  "with the exact Eternal Mangekyo active and his sword sheathed. PANEL 3: a second wave closes from every side as "
  "he stands arms folded. The army's successful-looking tactic fails twice. " + L_BATTLE +
  SAY((1, FORCE, "upper left", "WE HIT HIM."),
      (3, FORCE, "lower right", "AGAIN!")),
  R("naruto_v4_armor_sword", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p21", dict(scene="action", light="overcast", cast="group", mood="permission", panels=6),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + ENV.format(i=3) + ONLY(N16_SPEAKER, FORCE) +
  "SIX uneven panels. Naruto raises Deep Forest Emergence; massive roots surge toward the surviving force. For the "
  "first time their fire, lightning, earth, and wind attacks visibly combine and cancel the roots in one clear "
  "central collision. Final small panel: Naruto's slight smile, neither rage nor joy, gives them a larger answer. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "upper left", "DEEP FOREST EMERGENCE."),
      (4, FORCE, "upper right", "TOGETHER!"),
      (6, N16_SPEAKER, "lower left", "YOU STOPPED IT.")),
  R("naruto_v4_armor_sword", "mangekyo_design", "env_kiri_battlefield_crater"), "high"),

 ("p22", dict(scene="transformation", light="overcast", cast="group", mood="terror", panels=4),
  FILL + N16_ARMOR.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, FORCE) +
  "FOUR uneven panels. Opaque orange Susano'o rises around Naruto, large enough to dwarf anonymous troops but with "
  "hard-edged flat chakra and fully readable ground. Naruto remains visible on the protected side within it. Naruto "
  "and the construct make the same tiger seal; its readable mouth forms a compressed orange sphere above the field. " + L_BATTLE +
  SAY((2, FORCE, "upper left", "WHAT IS THAT?"),
      (4, FORCE, "lower right", "MOVE!")),
  R("naruto_v4_armor", "mangekyo_design", "susanoo_orange_final", "env_kiri_battlefield_crater"), "high"),

 ("p23", dict(scene="splash", light="overcast", cast="group", mood="catastrophic", panels=1),
  N16_ARMOR.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + ENV.format(i=4) + ONLY(N16_SPEAKER, FORCE) +
  "BORDERLESS SINGLE EVENT. The compressed orange sphere stops amid the anonymous force and detonates into an "
  "immense opaque orange ring and starburst over an identifiable wet field. Debris and silhouettes flee outward; "
  "the completed orange Susano'o wraps Naruto's side of the page as protection. The new crater is visibly much "
  "wider than the lightning-fire crater on page 11. No gore and no Yagura. " + L_BATTLE +
  SAY((1, N16_SPEAKER, "lower left", "EXPLODE.")) +
  SFX(1, "BOOM", "Large at the outer blast ring; leave Naruto and the orange construct legible."),
  R("naruto_v4_armor", "mangekyo_design", "susanoo_orange_final", "env_kiri_battlefield_crater"), "high"),

 ("p24", dict(scene="aftermath", light="overcast", cast="group", mood="frightened", panels=5),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + YUGAO_V4.format(i=3) + AO_V4.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, REBEL, FORCE) +
  "FIVE uneven quiet panels, no new action. PANEL 1: dust clears on the much larger crater. PANEL 2: Naruto "
  "inside it as orange Susano'o disperses into fragments. PANEL 3: his exact Eternal Mangekyo returns to normal "
  "blue. PANELS 4 and 5 share the bottom row across a gutter: Mei, Yugao, Ao, and unnamed rebel faces on one side; "
  "surviving anonymous enemy silhouettes on the other. Both groups carry the same frightened look. The final caption "
  "bridges both groups with no tail and no proximity to Naruto. No Yagura, water strike, rebel advance, or new threat. " + L_BATTLE +
  CAP(5, "across both bottom-row groups", "WHAT IS HE?"),
  R("naruto_v4_armor", "mei_v4", "yugao_v4", "ao_v4", "env_kiri_battlefield_crater"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch09" / "raw", HERE / "v4ch09" / "ledger.json")
