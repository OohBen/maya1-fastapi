"""Volume 4 prologue — After the Barrier. 8 pages.

Source: fic ch07:291-565. This bridges Volume 3's final barrier page to the
post-invasion opening of Volume 4 without replaying the public eye/Susano'o reveal.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

from runner import run  # noqa: E402
from prompts import (  # noqa: E402
    CAP,
    ENV,
    FILL,
    GAA,
    KAK,
    KAN,
    N13,
    ONLY,
    R,
    SAS,
    SAY,
    SFX,
    SHI,
    TEM,
    TITLE,
)


NARUTO = "the long-haired blond boy in black"
GAARA = "the red-haired boy with the enormous gourd"
SASUKE = "the dark-haired boy in the high-collared shirt"
KAKASHI = "the masked silver-haired man"
SHIKAMARU = "the boy with the pineapple ponytail"
TEMARI = "the blonde girl with four pigtails"
KANKURO = "the boy with purple face paint"
MANGEKYO = (
    "Image {i} is the EYE-DESIGN REFERENCE. Whenever the blond boy's active Mangekyo is visible, "
    "reproduce its exact six-bladed red pattern; never draw a generic pinwheel or three-bladed pattern. "
)
SAND_COMMANDER = (
    "a cropped adult Sand commander in a tan flak vest and desert head cloth, face mostly out of frame"
)
GREEN_JONIN = (
    "a tall adult Leaf jonin in a plain green jumpsuit, shown mostly from behind or as a cropped silhouette"
)
SOUND_ATTACKERS = "three anonymous Sound shinobi in mismatched grey combat gear"
L_INVASION = (
    "Lighting: dirty late-afternoon smoke light over damaged Konoha, with hard black shadows and no glow. "
)
L_FOREST = (
    "Lighting: hard overcast forest light with scorched ground, snapped branches, and drifting dust. "
)


PAGES = [
    ("p01", dict(scene="transition", light="smoke", cast="group", mood="urgent", panels=5),
     FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(NARUTO, SOUND_ATTACKERS) +
     "FIVE UNEQUAL PANELS. Continue immediately after Volume 3's final purple-barrier page; do not "
     "repeat the stadium, Mangekyo reveal, Susano'o reveal, or barrier formation. PANEL 1, dominant: "
     "the blond boy watches the distant sealed purple barrier through smoke; inside it only two tiny "
     "unreadable adult silhouettes face each other. PANEL 2: a pale snake-like profile is barely "
     "discernible through the barrier. PANEL 3: Naruto turns away, wrongly calm. PANEL 4: three "
     "anonymous Sound shinobi land around him at different depths. PANEL 5: their hands reach for "
     "weapons while Naruto remains still. " + L_INVASION +
     TITLE("AFTER THE BARRIER", "upper-left smoke shelf") +
     SAY((3, NARUTO, "upper right", "THE OLD MAN CAN HANDLE HIM."),
         (5, SOUND_ATTACKERS, "lower left", "OROCHIMARU WANTS YOU ALIVE.")),
     R("naruto_13", "env_village_street"), "high"),

    ("p02", dict(scene="action", light="smoke", cast="group", mood="cold", panels=6),
     FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) +
     ONLY(NARUTO, SOUND_ATTACKERS) +
     "SIX UNEQUAL PANELS. Compress the entire clash into one causal page. PANEL 1: the Sound shinobi "
     "rush from three directions. PANEL 2: the blond boy's visible left eye changes to the supplied "
     "six-bladed Mangekyo. PANEL 3: a flat black fear-genjutsu field, the attackers' weapons halted. "
     "PANEL 4: all three attackers collapse unconscious on intact ground, no blood or injury detail. "
     "PANEL 5: Naruto crouches beside the least-obscured attacker without touching him. PANEL 6, wide: "
     "Naruto walks away toward the forest, leaving the defeated group alive. " + L_INVASION +
     SAY((5, NARUTO, "lower right", "TELL OROCHIMARU TO STOP HUNTING ME."),
         (6, NARUTO, "lower right", "NEXT TIME, I HUNT HIM.")) + SFX(3, "THUM"),
     R("naruto_13", "mangekyo_design", "env_village_street"), "high"),

    ("p03", dict(scene="interception", light="smoke", cast="group", mood="redirected", panels=6),
     FILL + N13.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
     ONLY(NARUTO, KAKASHI, SAND_COMMANDER, GREEN_JONIN) +
     "SIX UNEQUAL PANELS. PANEL 1: a cropped Sand commander blocks Naruto's road and signals toward "
     "him as a target. PANEL 2: the masked silver-haired man intercepts the commander; a tall green-"
     "clad Leaf jonin is only a rear silhouette restraining the attack. PANEL 3: close-up of the "
     "masked man's hand offering a small paper suppression seal. PANEL 4: Naruto takes it. PANEL 5: "
     "a forest direction line beyond the village wall. PANEL 6, dominant: Naruto leaves toward the "
     "forest while the two Leaf jonin hold the Sand commander back. No named Sand or green-clad adult "
     "is shown in a clean face portrait. " + L_INVASION +
     SAY((1, SAND_COMMANDER, "upper left", "TAKE THE FOURTH'S SON."),
         (3, KAKASHI, "upper right", "JIRAIYA SAID THIS CAN SUPPRESS THE BEAST."),
         (5, KAKASHI, "lower right", "SASUKE WENT AFTER GAARA.")),
     R("naruto_13", "kakashi", "env_village_street"), "high"),

    ("p04", dict(scene="rescue", light="overcast", cast="three", mood="decisive", panels=6),
     FILL + N13.format(i=1) + SAS.format(i=2) + GAA.format(i=3) + ENV.format(i=4) +
     ONLY(NARUTO, SASUKE, GAARA) +
     "SIX UNEQUAL PANELS. PANEL 1, wide: in the scarred forest, a partly transformed sand arm pins "
     "the dark-haired boy while the red-haired boy advances. PANEL 2: Naruto knocks the sand arm aside "
     "and lands between them. PANEL 3: close-up of Sasuke's matured three-tomoe Sharingan, not Mangekyo. "
     "PANEL 4: Naruto briefly touches two fingers to Sasuke's forehead, a restrained echo of an older "
     "brother's gesture. PANEL 5: a clean non-gory strike renders Sasuke unconscious before he can "
     "interfere. PANEL 6: Naruto lowers Sasuke safely behind a tree and faces Gaara alone. " + L_FOREST +
     SAY((3, NARUTO, "upper right", "YOUR SHARINGAN MATURED."),
         (4, SASUKE, "middle left", "DON'T PATRONIZE ME."),
         (5, NARUTO, "lower right", "REST.")) + SFX(2, "KRAK"),
     R("naruto_13", "sasuke", "gaara", "env_forest_of_death"), "high"),

    ("p05", dict(scene="action_montage", light="overcast", cast="two", mood="violent", panels=7),
     FILL + N13.format(i=1) + GAA.format(i=2) + MANGEKYO.format(i=3) + ENV.format(i=4) +
     ONLY(NARUTO, GAARA, "one identical wood clone of Naruto") +
     "SEVEN UNEQUAL PANELS compress the rematch without replaying every exchanged blow. PANEL 1: "
     "Gaara's partial sand-beast arm swells. PANEL 2: Naruto's visible left six-bladed Mangekyo tracks "
     "the attack. PANEL 3: Naruto evades across a snapped trunk. PANEL 4: a single wood clone splits "
     "from Naruto. PANEL 5: clone and original cross Gaara at different depths. PANEL 6: a controlled "
     "fire blast tears through the outer sand shell. PANEL 7, dominant: the suppression seal is held "
     "ready in Naruto's gloved hand as the wounded forest remains readable. No Susano'o. " + L_FOREST +
     SFX(3, "SHUN") + SFX(4, "KRRK") + SFX(6, "WHOOOM"),
     R("naruto_13", "gaara", "mangekyo_design", "env_forest_of_death"), "high"),

    ("p06", dict(scene="aftermath_dialogue", light="overcast", cast="three", mood="exhausted", panels=6),
     FILL + N13.format(i=1) + GAA.format(i=2) + SAS.format(i=3) + ENV.format(i=4) +
     ONLY(NARUTO, GAARA, SASUKE) +
     "SIX UNEQUAL PANELS in strict causal order. PANEL 1: Naruto plants the paper seal on Gaara's "
     "sand-covered torso; the beast transformation stops. PANEL 2: both boys collapse apart on "
     "scorched ground, exhausted but conscious. PANEL 3: Gaara asks from ground level. PANEL 4: Naruto "
     "answers without warmth or triumph. PANEL 5: Sasuke wakes against the tree, watches them, and forms "
     "a fire hand seal. PANEL 6: Sasuke's newly copied fire technique burns away only a harmless remnant "
     "of sand at the edge, proving imitation without restarting the fight. " + L_FOREST +
     SAY((3, GAARA, "upper left", "WHY ARE YOU STRONGER?"),
         (4, NARUTO, "middle right", "I TRAINED. THE PEOPLE PRECIOUS TO ME ARE DEAD."),
         (6, SASUKE, "lower left", "I CAN USE IT TOO.")) + SFX(1, "THK") + SFX(6, "FWOOSH"),
     R("naruto_13", "gaara", "sasuke", "env_forest_of_death"), "high"),

    ("p07", dict(scene="release", light="overcast", cast="group", mood="changed", panels=6),
     FILL + N13.format(i=1) + GAA.format(i=2) + TEM.format(i=3) + KAN.format(i=4) + SHI.format(i=5) +
     ONLY(NARUTO, GAARA, TEMARI, KANKURO, SHIKAMARU) +
     "SIX UNEQUAL PANELS. PANEL 1: the boy with the pineapple ponytail crouches near the exhausted "
     "blond boy and checks him; Naruto stays upright. PANEL 2: the blonde girl and face-painted boy "
     "are freed from simple restraints. "
     "PANEL 3: Naruto turns away, ordering release rather than revenge. PANEL 4: the siblings support "
     "Gaara between them. PANEL 5: Gaara looks at each sibling instead of the enemy. PANEL 6, dominant "
     "wide: the three Sand siblings leave together through the damaged forest while Naruto remains "
     "small behind them. " + L_FOREST +
     SAY((1, SHIKAMARU, "upper left", "YOU ALL RIGHT?"),
         (1, NARUTO, "upper right", "I'M FINE. RELEASE THEM."),
         (3, NARUTO, "upper right", "LET THEM GO."),
         (5, GAARA, "middle left", "TEMARI. KANKURO. I'M SORRY.")) +
     CAP(6, "upper left", "THE SAND SIBLINGS LEFT TOGETHER."),
     R("naruto_13", "gaara", "temari", "kankuro", "shikamaru"), "high"),

    ("p08", dict(scene="return", light="dusk", cast="solo", mood="unresolved", panels=5),
     FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(NARUTO) +
     "FIVE UNEQUAL PANELS. PANEL 1, wide: Naruto re-enters Konoha at dusk after the fighting has ended. "
     "PANEL 2: medics and wounded are implied only by empty stretchers and stacked bandages; no other "
     "people are visible. PANEL 3: the distant rooftop where the purple barrier stood is now empty; do "
     "not reveal what happened inside it. PANEL 4: Naruto looks toward it, tired, still believing the "
     "old leader survived. PANEL 5, dominant: he disappears alone down a damaged residential street "
     "toward home. End on silence, not victory. " + L_INVASION +
     CAP(1, "upper left", "KONOHA HAD WON.") +
     CAP(5, "lower right", "NARUTO WENT HOME TO REST."),
     R("naruto_13", "env_village_street"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch00" / "raw", HERE / "v4ch00" / "ledger.json")
