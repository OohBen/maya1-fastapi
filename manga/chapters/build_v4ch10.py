"""Volume 4, Chapter 10 — "The Mizukage". 17 pages.

Source: fic ch11:377-509. Stops with human Yagura engulfed by the Great Fireball.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, OFF, ONLY, R, SAY, SFX, TITLE  # noqa: E402
from prompts_v4 import (GUNBAI_V4, MEI_V4, MEI_V4_SPEAKER,
                        N16_SPEAKER, N16_SWORD, YAGURA_HUMAN,
                        YAGURA_SPEAKER, WATER_TECHNIQUES)  # noqa: E402


LOYALISTS = "distant unnamed Kiri loyalist silhouettes, all too small to identify"
TERRIFIED_LOYALIST = "one terrified unnamed Kiri loyalist man in the near foreground"
REBELS = "distant unnamed Kiri rebel silhouettes, all too small to identify"
L_CRATER = ("Lighting: flat storm-grey daylight over a torn Kiri crater; water, steam, smoke, "
            "and both fighters remain separated by hard black contours. ")
HUMAN_LOCK = ("Yagura is fully human in every panel. Do not show any transformed anatomy, energy "
              "aura, tails, beast shape, giant construct, plant restraint, or unexplained sky effect. ")


PAGES = [
    ("p01", dict(scene="battlefield_aftermath", light="storm", cast="small_group", mood="quiet", panels=1),
     N16_SWORD.format(i=1) + ENV.format(i=2) + ONLY(N16_SPEAKER, TERRIFIED_LOYALIST, LOYALISTS) +
     "CHAPTER OPENING SPLASH. High view into an immense fractured Kiri battlefield crater. The older "
     "blond teen in red segmented armour is a small upright figure near the lower edge, his plain new "
     "sash sword sheathed and dark-purple gunbai on his back. The terrified unnamed loyalist Naruto "
     "had been confronting is visibly recoiling at lower foreground, one hand at his throat and eyes "
     "fixed on Naruto. A broad hard-edged wave cuts diagonally across the crater toward them. The only "
     "other people are scattered, distant loyalist silhouettes; no bodies or close-up injuries. Keep "
     "the upper third calm for the title. " + L_CRATER +
     TITLE("THE MIZUKAGE", "quiet upper third") + CAP(1, "lower left", "THE BATTLEFIELD HAD GONE QUIET."),
     R("naruto_v4_armor_sword", "env_kiri_battlefield_crater"), "high"),

    ("p02", dict(scene="intervention", light="storm", cast="four", mood="challenge", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + MEI_V4.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER, MEI_V4_SPEAKER, REBELS) +
     "SIX uneven panels with a dominant wide middle panel. PANEL 1: the water wave throws Naruto back; "
     "he flips through spray while Yagura is not drawn. PANEL 2: Naruto lands cleanly on broken ground. "
     "PANEL 3: Yagura walks alone from the far end of the crater. PANEL 4: Mei and distant rebel "
     "silhouettes arrive from a different rim. PANEL 5 (dominant): the two men face across torn ground "
     "at different depths, never posed as a lineup. PANEL 6: Yagura's cropped shoulder dominates the "
     "foreground while Naruto remains small beyond it. " + L_CRATER + HUMAN_LOCK +
     SAY((1, OFF(YAGURA_SPEAKER), "upper left", "SO YOU ARE THE NUISANCE THAT HAS CRIPPLED MY ARMY."),
         (6, N16_SPEAKER, "lower right", "YAGURA.")),
     R("naruto_v4_armor_sword", "yagura_human", "mei_v4", "env_kiri_battlefield_crater"), "high"),

    ("p03", dict(scene="challenge", light="storm", cast="three", mood="controlled", panels=5),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + MEI_V4.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER, MEI_V4_SPEAKER, REBELS) +
     "FIVE unequal conversation panels arranged as a triangle, never a lineup. PANEL 1: Yagura's "
     "profile large and cropped at left. PANEL 2: Naruto centered far back. PANEL 3: Mei arrives in "
     "right foreground. PANEL 4: Naruto's level visible eye. PANEL 5 (dominant): Mei's concerned "
     "close-up after seeing that Naruto is unmarked, while Yagura remains distant. " + L_CRATER + HUMAN_LOCK +
     SAY((1, YAGURA_SPEAKER, "upper left", "I HAVE COME TO END YOU."),
         (5, MEI_V4_SPEAKER, "lower right", "ARE YOU ALRIGHT, NARUTO?")),
     R("naruto_v4_armor_sword", "yagura_human", "mei_v4", "env_kiri_battlefield_crater"), "high"),

    ("p04", dict(scene="claiming_the_duel", light="storm", cast="four", mood="contained", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + MEI_V4.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER, MEI_V4_SPEAKER, REBELS) +
     "SIX uneven quiet-pressure panels. PANEL 1: Mei's concerned hand. PANEL 2: Naruto's unreadable "
     "eye. PANEL 3: Yagura waiting across the ruined field. PANEL 4: Naruto turns away from Mei toward "
     "Yagura. PANEL 5 (dominant wide): Naruto makes a single hand seal; wind lifts dust and loose cloth "
     "as he releases stored chakra. PANEL 6 (narrow): Mei withdraws toward the distant rebels, still "
     "watching. The release restores working reserves but does not imply endless chakra. " + L_CRATER + HUMAN_LOCK +
     SAY((2, N16_SPEAKER, "upper right", "I'M FINE."),
         (4, N16_SPEAKER, "lower left", "I WILL TAKE CARE OF THE MIZUKAGE."),
         (5, N16_SPEAKER, "upper left", "KAI."),
         (6, MEI_V4_SPEAKER, "lower right", "I WILL NOT BE FAR.")),
     R("naruto_v4_armor_sword", "yagura_human", "mei_v4", "env_kiri_battlefield_crater"), "high"),

    ("p05", dict(scene="dry_taijutsu", light="storm", cast="two", mood="testing", panels=7),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SEVEN sharply unequal combat panels. PANEL 1 (narrow letterbox): Yagura's fist and Naruto's "
     "counter-fist collide with a small star-flash. PANEL 2: roundhouse block. PANEL 3: Naruto falls "
     "to his hands. PANEL 4: Yagura descends. PANEL 5: Naruto falls back and crosses his arms. PANEL 6 "
     "(dominant diagonal): Yagura's heel drives Naruto into a shallow crater, but the defense holds. "
     "PANEL 7: Naruto is already rising in front of him. No sword is drawn. " + L_CRATER + HUMAN_LOCK +
     SFX(1, "KRAK", "Keep the impact small and clear of both faces."),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

    ("p06", dict(scene="fire_breath_clone", light="storm", cast="two", mood="escalating", panels=8),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + WATER_TECHNIQUES.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "EIGHT uneven close-range panels. Naruto kicks Yagura free, then the figures move through block, "
     "knee, duck, and throw without repeating a pose. PANEL 5 (dominant low angle): Yagura flies "
     "diagonally toward the right page edge. PANEL 6: Naruto forms seals. PANEL 7: Fire Breath reaches "
     "the airborne Yagura. PANEL 8: the flame strikes a human-shaped water clone that collapses into "
     "water, while the real Yagura forms seals behind Naruto. Make the clone visibly water, not energy. "
     + L_CRATER + HUMAN_LOCK +
     SAY((6, N16_SPEAKER, "upper left", "FIRE RELEASE: FIRE BREATH.")) +
     SFX(5, "WHAM", "The thrown body crosses the panel diagonally."),
     R("naruto_v4_armor_sword", "yagura_human", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p07", dict(scene="flooded_field", light="storm", cast="two", mood="tactical_shift", panels=5),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "FIVE strongly uneven panels. PANEL 1: Yagura rides a huge water wave through the crater. PANEL 2 "
     "(dominant wide): the hard-edged wave swallows Naruto and fills the entire crater. PANEL 3: a still "
     "horizontal water surface. PANEL 4 (tall): Naruto stands dry inside a visible barrier with the dark "
     "purple gunbai held forward; water hangs and breaks around it instead of hiding him. PANEL 5: he "
     "re-straps the gunbai as the crater is left a shallow sea. " + L_CRATER + HUMAN_LOCK +
     SAY((1, YAGURA_SPEAKER, "upper left", "WATER RELEASE: EXPLODING WATER SHOCK WAVE!"),
         (4, N16_SPEAKER, "lower right", "GUNBAI BARRIER.")),
     R("naruto_v4_armor_sword", "yagura_human", "gunbai_v4", "env_kiri_battlefield_crater"), "high"),

    ("p08", dict(scene="water_surface_fight", light="storm", cast="two", mood="pressure", panels=7),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + WATER_TECHNIQUES.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SEVEN uneven water-surface combat panels. Naruto and Yagura fight on the shallow sea, their feet "
     "leaving hard ripples and spray. PANEL 1: Yagura's opening punch. PANEL 2: Naruto blocks. PANEL 3: "
     "a diving two-foot strike. PANEL 4: Naruto evades. PANEL 5: a water clone appears behind him. PANEL "
     "6: the two Yaguras kick Naruto away; one collapses back into water. PANEL 7 (dominant): Naruto "
     "lands on chakra-supported feet and regains his balance on the water. " + L_CRATER + HUMAN_LOCK +
     CAP(7, "upper left", "THE CRATER HAD BECOME YAGURA'S GROUND."),
     R("naruto_v4_armor_sword", "yagura_human", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p09", dict(scene="dragon_fire_clash", light="storm", cast="two", mood="reversal", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + WATER_TECHNIQUES.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SIX uneven panels. PANEL 1: Naruto blocks the diving kick. PANEL 2: he reads Yagura's next "
     "approach. PANEL 3: Naruto kicks him from behind. PANEL 4: Yagura crashes through the water. PANEL "
     "5: soaked Yagura creates a large water dragon with clear water anatomy. PANEL 6 (dominant): "
     "Majestic Fire Destruction collides with the dragon; fire and water are opaque outlined shapes, "
     "with the crater contours readable beneath the steam. " + L_CRATER + HUMAN_LOCK +
     SAY((5, YAGURA_SPEAKER, "upper left", "WATER RELEASE: WATER DRAGON!"),
         (6, N16_SPEAKER, "lower right", "FIRE RELEASE: MAJESTIC FIRE DESTRUCTION!")),
     R("naruto_v4_armor_sword", "yagura_human", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p10", dict(scene="reserve_and_sword", light="steam", cast="two", mood="measured", panels=5),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "FIVE unequal panels over a pitted, partly drained battlefield. PANEL 1: steam breaks around the "
     "two fighters. PANEL 2: Yagura pants, still upright. PANEL 3: Naruto's controlled breath, tired "
     "but steady after the earlier release. PANEL 4: Yagura attacks again. PANEL 5 (dominant object "
     "close-up): Naruto draws the plain straight sword from his sash; it is visibly distinct from the "
     "gunbai and is not a recovered weapon. " + L_CRATER + HUMAN_LOCK +
     CAP(3, "upper left", "THE STORED CHAKRA HAD RESTORED HIS RESERVES."),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

    ("p11", dict(scene="sword_pressure", light="steam", cast="two", mood="advantage", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SIX uneven sword-combat panels. PANEL 1: Yagura evades the vertical slash. PANEL 2: Naruto's "
     "left-foot kick disrupts Yagura's balance. PANEL 3 (dominant diagonal): the sword tip makes only "
     "a shallow cut across Yagura's chest, no graphic gore. PANEL 4: Naruto's knee lands. PANEL 5: a "
     "spinning kick sends Yagura away. PANEL 6: Naruto flicks the blade clean and resheathes it. " +
     L_CRATER + HUMAN_LOCK + SFX(3, "SHNK", "Keep the mark shallow and readable."),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

    ("p12", dict(scene="draining_the_field", light="steam", cast="two", mood="attrition", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + WATER_TECHNIQUES.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SIX uneven panels. PANEL 1: Yagura stands again, chest cut shallow and breathing hard. PANEL 2: "
     "Naruto forms seals. PANEL 3: a broad hard-edged flame wave advances. PANEL 4: Yagura builds a "
     "water wall. PANEL 5 (dominant): the fire breaks through the wall, converting water to readable "
     "steam without hiding either fighter. PANEL 6: the crater is scorched dry; Yagura kneels at the "
     "distant edge, burned and breathing hard. " + L_CRATER + HUMAN_LOCK +
     SAY((2, N16_SPEAKER, "upper left", "FIRE RELEASE: MAJESTIC FLAME DESTRUCTION.")),
     R("naruto_v4_armor_sword", "yagura_human", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p13", dict(scene="close_pressure", light="storm", cast="two", mood="relentless", panels=7),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SEVEN uneven attack panels on the newly dry cracked crater. PANEL 1: Naruto closes distance. "
     "PANEL 2: he ducks Yagura's punch. PANEL 3: a gut punch. PANEL 4: two rapid face strikes. PANEL "
     "5: Naruto grips Yagura by the neck. PANEL 6 (dominant diagonal): the slam cracks the ground. "
     "PANEL 7: Naruto leaps clear, forms seals, and releases Phoenix Flower fireballs down toward "
     "Yagura before he can recover. " + L_CRATER + HUMAN_LOCK +
     SAY((7, N16_SPEAKER, "upper right", "FIRE RELEASE: PHOENIX FLOWER.")) +
     SFX(6, "KRAK", "The crack radiates through dry ground, not through Yagura's body."),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

    ("p14", dict(scene="water_counter", light="storm", cast="two", mood="counterstrike", panels=6),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + WATER_TECHNIQUES.format(i=3) + ENV.format(i=4) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "SIX unequal response panels. PANEL 1: Phoenix Flower fireballs descend toward Yagura. PANEL 2: "
     "Yagura's Water Wall catches them. PANEL 3: Naruto lands on dry ground. PANEL 4: Wind Palm hits "
     "the still Yagura. PANEL 5: that figure dissolves into a puddle. PANEL 6 (dominant): the real "
     "Yagura behind Naruto launches a dense swirling water bomb. The clone reveal is legible before "
     "the projectile arrives. " + L_CRATER + HUMAN_LOCK +
     SAY((4, N16_SPEAKER, "upper right", "WIND RELEASE: WIND PALM."),
         (6, YAGURA_SPEAKER, "lower left", "WATER RELEASE: WATER BOMB!")),
     R("naruto_v4_armor_sword", "yagura_human", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p15", dict(scene="gunbai_defense", light="storm", cast="two", mood="held", panels=5),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + GUNBAI_V4.format(i=3) + WATER_TECHNIQUES.format(i=4) + ENV.format(i=5) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "FIVE strongly uneven panels. PANEL 1: Naruto unstraps the gunbai as the bomb closes. PANEL 2 "
     "(dominant): the water bomb detonates against a visible barrier around the gunbai; large water "
     "forms wrap it, but Naruto and the dry crater remain readable. PANEL 3: the water clears. PANEL 4: "
     "Naruto lowers and re-straps the gunbai only now. PANEL 5: Yagura is again on one knee in the "
     "distance, exhausted but wholly human. " + L_CRATER + HUMAN_LOCK +
     SAY((2, N16_SPEAKER, "lower right", "GUNBAI BARRIER.")),
     R("naruto_v4_armor_sword", "yagura_human", "gunbai_v4", "water_clone_dragon", "env_kiri_battlefield_crater"), "high"),

    ("p16", dict(scene="great_fireball", light="storm", cast="two", mood="suspended", panels=4),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "FOUR strongly unequal pre-cliffhanger panels. PANEL 1 (dominant close-up): Naruto holds one "
     "tiger seal, expression blank. PANEL 2: Yagura's tired eyes, still human. PANEL 3: the first "
     "hard-edged orange flame grows in Naruto's profile. PANEL 4: Yagura is small, wounded, and framed "
     "by the empty dry crater beyond the approaching fire. " + L_CRATER + HUMAN_LOCK +
     SAY((1, N16_SPEAKER, "upper left", "FIRE RELEASE: GREAT FIREBALL.")),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),

    ("p17", dict(scene="fireball_cliffhanger", light="fire", cast="two", mood="unresolved", panels=2),
     FILL + N16_SWORD.format(i=1) + YAGURA_HUMAN.format(i=2) + ENV.format(i=3) +
     ONLY(N16_SPEAKER, YAGURA_SPEAKER) +
     "TWO deliberately unequal cliffhanger panels. PANEL 1 (huge dominant): the Great Fireball engulfs "
     "the fully human Yagura completely, hard-edged orange flame and black smoke contained within the "
     "dry crater. PANEL 2 (narrow final): Naruto in profile, still and watchful, flame reflected in his "
     "visible eye. Do not show any body, silhouette, transformation, or answer inside the fire. " +
     L_CRATER + HUMAN_LOCK + CAP(2, "lower left", "THE FIRE TOOK YAGURA."),
     R("naruto_v4_armor_sword", "yagura_human", "env_kiri_battlefield_crater"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch10" / "raw", HERE / "v4ch10" / "ledger.json")
