"""Volume 4, Chapter 11 — "The Three Tails". 18 pages.

Source: fic ch11:511-581.  The chapter moves through distinct states in order:
Yagura's crimson cloak, the complete orange Susano'o, the exposed human form,
the full Three-Tails, and the unexplained blue column after the fight.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, ONLY, R, SAY, SFX  # noqa: E402
from prompts_v4 import (GUNBAI_V4, L_KIRI_BATTLE, MEI_V4, MEI_V4_SPEAKER,
                        MANGEKYO_EYE, MOKUTON_STAKES, N16_SPEAKER, N16_SWORD, SANBI_FULL,
                        SUSA_FINAL, WOOD_WALL, YAGURA_CLOAK,
                        YAGURA_HUMAN, YUGAO_V4, YUGAO_V4_SPEAKER)  # noqa: E402

NARUTO_CLONE = "an identical shadow clone of the older blond teen"
CLOAK = "Yagura's human-sized crimson three-tailed chakra cloak"
YAGURA = "Yagura, the short Fourth Mizukage"
SANBI = "the massive full Three-Tails turtle"
REBELS = "distant unnamed Kiri rebels, each an indistinct silhouette"
L_CRATER = (L_KIRI_BATTLE + "The same devastated Kiri battlefield has linked craters, torn earth, "
            "low smoke, and lingering steam; orange chakra is opaque against the grey terrain. ")
OPENING_TITLE = ("LETTERING: write the chapter title in the quiet upper-left smoke shelf, in large "
                 "bold upright English capitals, correctly spelled, reading: \"THE THREE TAILS\". "
                 "Also draw the supplied caption. Draw no other text, balloons, sound effects, "
                 "numbers, or signature on this page. ")


PAGES = [
 ("p01", dict(scene="establishing", light="overcast", cast="two", mood="tense", panels=1),
  N16_SWORD.format(i=1) + YAGURA_CLOAK.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, CLOAK) +
  "CHAPTER OPENING SPLASH. Borderless vertical page. Fireball smoke parts around a human-sized "
  "crimson chakra silhouette with exactly three slow tails and demonic eyes; it is not a turtle. "
  "The approximately sixteen-year-old blond teen in red segmented armour stands small at lower left, "
  "back three-quarters to camera, new plain sash sword sheathed and gunbai still on his back. The "
  "crimson figure dominates the upper right while the unbroken battlefield carries across the page. "
  "Keep the upper left quiet for the title; no aura, blast, or extra combatant. " + L_CRATER +
  OPENING_TITLE + CAP(1, "lower left", "YAGURA ANSWERED WITH EVERYTHING HE HAD."),
  R("naruto_v4_armor_sword", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p02", dict(scene="transformation", light="overcast", cast="two", mood="controlled", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + YAGURA_CLOAK.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, CLOAK) +
  "FIVE uneven panels, with one low-angle dominant bottom panel. PANEL 1: the crimson three-tail "
  "cloak holds perfectly still. PANEL 2: Naruto's visible left eye carries the exact six-bladed EMS. "
  "PANEL 3: armour cords and long blond hair lift in the wind. PANEL 4: pebbles rise around his boots. "
  "PANEL 5 (dominant): Naruto is small beneath a widening but still transparent pressure field, "
  "hands clasping at centre; Yagura's cloak is distant and unmoved. The pressure must precede the "
  "Susano'o and must not become white bloom. " + L_CRATER +
  SAY((5, N16_SPEAKER, "lower right", "THEN I, UCHIHA NARUTO, SHALL RESPOND WITH MY FULL STRENGTH.")),
  R("naruto_v4_armor_sword", "mangekyo_design", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p03", dict(scene="transformation", light="overcast", cast="two", mood="awe", panels=4),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + YAGURA_CLOAK.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, CLOAK) +
  "FOUR uneven panels. PANEL 1: debris spirals away from Naruto. PANEL 2: his clasped hands inside "
  "the rising form. PANEL 3: the cloak's demonic eyes do not blink. PANEL 4 (dominant, taking most "
  "of the page): the complete horned orange Susano'o stands solid around Naruto, with two broad orange "
  "blades and Naruto visibly small inside its torso. Its opaque flat colour and hard black contours "
  "leave every crater edge readable; it is a body, not a glow. " + L_CRATER +
  CAP(4, "lower left", "ORANGE CHAKRA MET CRIMSON."),
  R("naruto_v4_armor_sword", "mangekyo_design", "susanoo_orange_final", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p04", dict(scene="action", light="overcast", cast="two", mood="pressured", panels=6),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + YAGURA_CLOAK.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, CLOAK) +
  "SIX uneven panels with alternating narrow impact crops and one dominant central clash. PANEL 1: "
  "Yagura's crimson fist crosses the frame. PANEL 2: it lands against the orange shell. PANEL 3: "
  "crater earth buckles under the Susano'o. PANEL 4 (dominant): the cloak attacks from three separate "
  "directions around the complete orange form, but the form remains intact; hard impact marks, no "
  "glow. PANEL 5: Naruto's EMS eye calculates. PANEL 6: Yagura lands back at distance, forcing the "
  "reader to see that repeated attacks, not a single strike, are the danger. " + L_CRATER +
  SAY((5, N16_SPEAKER, "upper left", "IF HE HAD NOT STOPPED, MY SUSANOO WOULD HAVE BROKEN.")) +
  SFX(4, "DOK", "Each impact is a hard, small graphic shape."),
  R("naruto_v4_armor_sword", "mangekyo_design", "susanoo_orange_final", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p05", dict(scene="action", light="overcast", cast="two", mood="decisive", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + YAGURA_CLOAK.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, CLOAK) +
  "FIVE uneven panels with a dominant diagonal blade exchange. PANEL 1: the right orange blade cuts "
  "down and misses as Yagura evades. PANEL 2: Yagura commits forward through the missed swing. PANEL 3 "
  "(dominant): the second blade arrives from the opposite diagonal and drives the crimson cloak into "
  "the crater floor. PANEL 4: both blades cross. PANEL 5: an X-shaped opaque orange shockwave marks "
  "the ground around the pinned cloak. This is a damaging answer, not a finishing blow; the cloak is "
  "still visibly present. " + L_CRATER +
  SAY((1, N16_SPEAKER, "upper left", "IT SEEMS YOU ARE DONE."),
      (4, N16_SPEAKER, "lower right", "THEN ALLOW ME TO TAKE MY DANCE.")) +
  SFX(3, "KRAK", "The lettering follows the second blade, never obscuring a face."),
  R("naruto_v4_armor_sword", "mangekyo_design", "susanoo_orange_final", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p06", dict(scene="action", light="overcast", cast="two", mood="reversal", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + YAGURA_CLOAK.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, CLOAK) +
  "FIVE uneven panels. Naruto has dismissed the complete Susano'o after its exchange. PANEL 1: his "
  "plain new sash sword clears its sheath with wind chakra only as a narrow edge effect. PANEL 2: the "
  "blade glances off the crimson skin without cutting it. PANEL 3: Naruto's follow-up kick passes over "
  "Yagura's ducking head. PANEL 4 (dominant): Yagura's crimson punch lands in Naruto's armoured abdomen "
  "and throws him sideways across the crater; the armour absorbs most of it, but Naruto's folded posture "
  "shows the failed tactic hurt. PANEL 5: he lands, still holding the sword low. " + L_CRATER +
  CAP(2, "upper left", "THE CLOAK STILL HELD.") + SFX(4, "THOOM"),
  R("naruto_v4_armor_sword", "mangekyo_design", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p07", dict(scene="action", light="overcast", cast="two", mood="strained", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + GUNBAI_V4.format(i=3) + YAGURA_CLOAK.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, CLOAK) +
  "FIVE uneven panels, built from tight hand, fan, and body crops before one wide result. PANEL 1: "
  "Naruto reaches the dark-purple gunbai on his back. PANEL 2: Yagura descends with a fist. PANEL 3: "
  "the fan catches the punch. PANEL 4: Naruto turns the fan to catch a side kick. PANEL 5 (dominant "
  "wide): both impacts have pushed Naruto backward across peeled earth, his heels carving a hard line; "
  "Yagura's cloak remains aggressive and Naruto has no clean opening. " + L_CRATER +
  SFX(3, "KLANG") + SFX(4, "SKRRR"),
  R("naruto_v4_armor_sword", "mangekyo_design", "gunbai_v4", "yagura_sanbi_cloak", "env_kiri_battlefield_crater"), "high"),

 ("p08", dict(scene="tactic", light="overcast", cast="two", mood="precise", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + GUNBAI_V4.format(i=3) + YAGURA_CLOAK.format(i=4) + MOKUTON_STAKES.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, NARUTO_CLONE, CLOAK) +
  "FIVE uneven panels. PANEL 1: Naruto leaps backward and straps the gunbai flat to his back before "
  "forming seals. PANEL 2: a large fireball travels across the crater. PANEL 3 (dominant): flame clears "
  "around the untouched crimson cloak; this fire has failed to damage it. PANEL 4: reverse-angle reveal "
  "of Naruto's identical shadow clone kneeling behind Yagura. PANEL 5: angular pale wooden stakes pin all "
  "three crimson tails to the ground. The spatial sequence must read clone first, stakes second, trapped "
  "tails third. " + L_CRATER +
  SAY((2, N16_SPEAKER, "upper left", "FIRE RELEASE: GREAT FIREBALL.")) + SFX(2, "FWOOM"),
  R("naruto_v4_armor_sword", "mangekyo_design", "gunbai_v4", "yagura_sanbi_cloak", "mokuton_stakes_serpent", "env_kiri_battlefield_crater"), "high"),

 ("p09", dict(scene="tactic", light="overcast", cast="three", mood="turning", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + YAGURA_HUMAN.format(i=3) + YAGURA_CLOAK.format(i=4) + MOKUTON_STAKES.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, NARUTO_CLONE, YAGURA) +
  "FIVE uneven panels. PANEL 1: Naruto's identical shadow clone kneels behind Yagura and its angular pale "
  "wooden stakes pin all three crimson tails to the ground. PANEL 2: the clone disperses immediately into "
  "flat smoke after the pin is set; it is absent from every later panel. PANEL 3: the real Naruto forms "
  "seals. PANEL 4: his constructed wooden serpent coils around the trapped crimson cloak. PANEL 5 (dominant): "
  "the serpent drains the crimson layer away until Yagura's fully human body, with no tails, shell, or turtle "
  "feature, falls face-first; Naruto approaches with his sword still low. This is the cause of the human-form "
  "defeat, not a magic cut. " + L_CRATER +
  SAY((3, N16_SPEAKER, "upper left", "WOOD RELEASE: WOOD SERPENT.")) + SFX(2, "POOF"),
  R("naruto_v4_armor_sword", "mangekyo_design", "yagura_human", "yagura_sanbi_cloak", "mokuton_stakes_serpent", "env_kiri_battlefield_crater"), "high"),

 ("p10", dict(scene="transformation", light="overcast", cast="two", mood="alarm", panels=3),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + YAGURA_HUMAN.format(i=3) + SANBI_FULL.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, YAGURA, SANBI) +
  "THREE radically uneven panels. PANEL 1: Yagura's prone human body erupts in a burst of debris and "
  "chakra, forcing Naruto to stop with the sword lowered. PANEL 2: Naruto's EMS eye widens. PANEL 3 "
  "(dominant, taking most of the page): when debris clears, the full blue-grey Three-Tails turtle with "
  "a heavy shell, red eye, and exactly three visible tails occupies the far crater edge; Naruto is a "
  "small armoured figure at its feet. This is visibly much larger and fundamentally different from the "
  "earlier crimson human-sized cloak. " + L_CRATER +
  CAP(3, "upper left", "THE BEAST ITSELF STOOD UP."),
  R("naruto_v4_armor_sword", "mangekyo_design", "yagura_human", "sanbi_full", "env_kiri_battlefield_crater"), "high"),

 ("p11", dict(scene="threat", light="overcast", cast="two", mood="urgent", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SANBI_FULL.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, SANBI) +
  "FIVE uneven panels. PANEL 1: the Three-Tails' red eye tracks Naruto. PANEL 2: a dense dark chakra "
  "sphere begins compacting at its mouth. PANEL 3: Naruto recognizes it, EMS active. PANEL 4: his boot "
  "grinds into fractured earth. PANEL 5 (dominant low wide): the completed first bijuudama looms above "
  "the small armoured Naruto while suspended debris curves toward it. The sphere is a readable solid form, "
  "not a white light effect. " + L_CRATER +
  SAY((3, N16_SPEAKER, "upper left", "EVEN SUSANOO WILL NOT HOLD AGAINST THAT.")),
  R("naruto_v4_armor_sword", "mangekyo_design", "sanbi_full", "env_kiri_battlefield_crater"), "high"),

 ("p12", dict(scene="defense", light="overcast", cast="two", mood="urgent", panels=6),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SANBI_FULL.format(i=3) + WOOD_WALL.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, SANBI) +
  "SIX uneven panels with a dominant lower panel devoted to the defense completing before impact. PANEL 1: "
  "the first bijuudama leaves the Three-Tails. PANEL 2: Naruto runs through hand seals. PANEL 3: both "
  "palms hit the ground. PANEL 4: timber pillars erupt from the left. PANEL 5: matching pillars erupt "
  "from the right. PANEL 6 (dominant): the opposed pillars curve together into a solid timber dome with "
  "Naruto visibly enclosed at its centre before the projectile reaches it. " + L_CRATER +
  SAY((3, N16_SPEAKER, "lower right", "WOOD RELEASE: WOOD LOCKING WALL.")) + SFX(4, "KRAK"),
  R("naruto_v4_armor_sword", "mangekyo_design", "sanbi_full", "wood_locking_wall", "env_kiri_battlefield_crater"), "high"),

 ("p13", dict(scene="impact", light="overcast", cast="two", mood="violent", panels=3),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SANBI_FULL.format(i=3) + WOOD_WALL.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, SANBI) +
  "THREE radically uneven panels. PANEL 1 (dominant horizontal): the first bijuudama strikes the wooden "
  "dome, which holds for one readable beat; hard black-and-grey dust rings move outward while the dome "
  "silhouette remains visible. PANEL 2: splintered timber falls. PANEL 3: Naruto's hand braces in the "
  "dirt beneath the broken ribs of the wall. The attack has been survived, but the structural defence is "
  "spent. " + L_CRATER + SFX(1, "BOOOOM"),
  R("naruto_v4_armor_sword", "mangekyo_design", "sanbi_full", "wood_locking_wall", "env_kiri_battlefield_crater"), "high"),

 ("p14", dict(scene="aftermath", light="overcast", cast="two", mood="depleted", panels=5),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SANBI_FULL.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, SANBI) +
  "FIVE uneven panels, quieter after the impact. PANEL 1: dust clears from the hollow where the dome "
  "stood. PANEL 2: Naruto kneels, breathing hard. PANEL 3: his shaking gloved hand studies fallen wood. "
  "PANEL 4: the Three-Tails begins a new, small unfinished dark sphere at its mouth. PANEL 5 (dominant): "
  "Naruto rises unsteadily in the near foreground while the clearly separate second charge grows at the far "
  "crater edge. The first explosion is over before this page begins; do not use a flashback, named figure, "
  "or lecture to explain his depletion. " + L_CRATER +
  SAY((3, N16_SPEAKER, "upper left", "IT HELD. ONLY LONG ENOUGH.")),
  R("naruto_v4_armor_sword", "mangekyo_design", "sanbi_full", "env_kiri_battlefield_crater"), "high"),

 ("p15", dict(scene="counterattack", light="overcast", cast="two", mood="last_resort", panels=4),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + SANBI_FULL.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, SANBI) +
  "FOUR uneven panels with one dominant diagonal confrontation. PANEL 1: Naruto's EMS eye remains active "
  "but strained. PANEL 2: the orange complete Susano'o flares around him and gathers a compact opaque orange "
  "bomb. PANEL 3 (dominant): across an open stretch of crater floor, the Susano'o bomb is fully charged "
  "while the Three-Tails' second bijuudama is still visibly incomplete. PANEL 4: Naruto fires first. The "
  "strict diagonal and unfinished dark sphere must make this an interruption, not two completed blasts trading. "
  + L_CRATER + CAP(4, "lower left", "HE SPENT WHAT REMAINED BEFORE THE SECOND SHOT COULD FORM."),
  R("naruto_v4_armor_sword", "mangekyo_design", "susanoo_orange_final", "sanbi_full", "env_kiri_battlefield_crater"), "high"),

 ("p16", dict(scene="resolution", light="overcast", cast="two", mood="spent", panels=4),
  FILL + N16_SWORD.format(i=1) + MANGEKYO_EYE.format(i=2) + SUSA_FINAL.format(i=3) + SANBI_FULL.format(i=4) + YAGURA_HUMAN.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, SANBI, YAGURA) +
  "FOUR uneven panels. PANEL 1 (dominant): the orange bomb crosses the crater and strikes the unfinished "
  "dark charge at the Three-Tails' mouth, creating one opaque orange-and-black detonation with no washed-out centre. PANEL 2: distant "
  "craters merge into one larger wound. PANEL 3: Yagura lies small and human at the centre of that crater. "
  "PANEL 4: the complete Susano'o fades from Naruto and his visible eye changes from the exact EMS pattern "
  "to plain blue. He remains armoured, sword sheathed, and visibly unsteady. " + L_CRATER +
  SFX(1, "KRA-BOOM", "The hard-edged blast leaves ground and both silhouettes readable."),
  R("naruto_v4_armor_sword", "mangekyo_design", "susanoo_orange_final", "sanbi_full", "yagura_human", "env_kiri_battlefield_crater"), "high"),

 ("p17", dict(scene="aftermath", light="overcast", cast="two", mood="unresolved", panels=4),
  FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YAGURA) +
  "FOUR uneven panels. PANEL 1: Naruto on both knees in the merged crater, no Susano'o or orange aura. "
  "PANEL 2: close-up of his plain blue visible eye, confirming the EMS is inactive. PANEL 3 (dominant tall): "
  "from Naruto's low viewpoint, an unlabelled blue chakra column erupts vertically from Yagura's distant "
  "position and exits the top edge. Naruto is physically separate from it. PANEL 4: the same space is already "
  "empty after the column vanishes. Do not draw a seal, spirit, person, named technique, resolved transformation, "
  "or explanatory reaction. " + L_CRATER +
  SAY((1, N16_SPEAKER, "lower right", "NOT ENOUGH CHAKRA TO CALL THE KYUBI.")),
  R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

 ("p18", dict(scene="hook", light="overcast", cast="small_group", mood="controlled", panels=5),
  FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + MEI_V4.format(i=3) + YUGAO_V4.format(i=4) + ENV.format(i=5) +
  ONLY(N16_SPEAKER, YAGURA, MEI_V4_SPEAKER, YUGAO_V4_SPEAKER, REBELS) +
  "FIVE uneven panels. PANEL 1: low rear view of kneeling Naruto in the foreground, with Yagura small and "
  "down at the merged crater's centre; the blue column is absent. PANEL 2: Mei and Yugao appear at the far "
  "crater lip, worried but still distant. PANEL 3: their unnamed rebel force runs behind them as staggered "
  "non-identifiable silhouettes. PANEL 4: Naruto hears them and turns only his head. PANEL 5 (dominant extreme "
  "close-up): his tired, controlled face has a clean balloon shelf; he is not smiling and no one has reached him. "
  "No debrief, embrace, arrest, named blue-chakra explanation, or cut away. " + L_CRATER +
  SAY((5, N16_SPEAKER, "upper left", "THIS IS GOING TO BE ANNOYING.")),
  R("naruto_v4_armor_sword", "yagura_human", "mei_v4", "yugao_v4", "env_kiri_battlefield_crater"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch11" / "raw", HERE / "v4ch11" / "ledger.json")
