"""Volume 4 prompt additions.

The shared vocabulary remains in ``prompts``. These bindings cover only the new Volume 4
reference sheets and keep their silhouette-defining feature first.
"""
from prompts import *  # noqa: F401,F403


# ---------------------------------------------------------------- Volume 4 cast
HOMURA = ("Image {i} is the CHARACTER REFERENCE for the elderly male adviser: a narrow old man "
          "whose silhouette is a dark formal robe and squared cap line. Reserved posture, lined "
          "face, restrained expression. Reproduce exactly; ignore its white background and layout. ")
KOHARU = ("Image {i} is the CHARACTER REFERENCE for the elderly female adviser: a compact old woman "
          "whose silhouette is a severe swept-back pale hair bun above layered formal robes. "
          "Reserved posture, lined face. Reproduce exactly; ignore its white background and layout. ")
TSUNADE = ("Image {i} is the CHARACTER REFERENCE for the blonde leader: a tall, broad-shouldered "
           "adult woman with two long blonde tails and a dark diamond mark centered on her forehead, "
           "wearing a green haori over a grey wrap top. Commanding squared stance, never a fan-service "
           "pose. Reproduce exactly; ignore its white background and layout. ")
SHIZUNE = ("Image {i} is the CHARACTER REFERENCE for the dark-haired medical aide: a slight adult "
           "woman whose silhouette is a single high ponytail above a dark kimono-style medical "
           "assistant outfit. Reproduce exactly; ignore its white background and layout. ")
SHIKAKU = ("Image {i} is the CHARACTER REFERENCE for the Nara clan head: an adult man whose silhouette "
           "is a long, high pineapple ponytail above a green jonin vest. Composed, slightly slouched "
           "posture. Reproduce exactly; ignore its white background and layout. ")
HIASHI = ("Image {i} is the CHARACTER REFERENCE for the Hyuga clan head: a stern middle-aged man "
          "whose silhouette is long straight dark-brown hair over formal cream-grey clan robes. "
          "His eyes are pale lavender and pupil-less. Reproduce exactly; ignore its white "
          "background and layout. ")
TSUME = ("Image {i} is the CHARACTER REFERENCE for the Inuzuka clan head: a fierce middle-aged WOMAN "
         "whose silhouette is wild long brown hair above a green jonin vest. Red fang markings cross "
         "BOTH of her cheeks, one on each side. She is female and must NEVER be drawn as a man: no "
         "beard, no moustache, no goatee, no stubble, no heavy male jaw — give her a female jaw and "
         "throat line. Reproduce exactly; ignore its white background and layout. ")
ITACHI = ("Image {i} is the CHARACTER REFERENCE for the Uchiha man: an adult whose silhouette is long "
          "black hair framing a narrow face and a high black Akatsuki collar over a cloak patterned "
          "with red clouds. Red Mangekyo eye when active; straw hat only when the panel specifies it. "
          "Reproduce exactly; ignore its white background and layout. ")
KISAME = ("Image {i} is the CHARACTER REFERENCE for the shark-faced man: a very tall blue-grey adult "
          "whose silhouette is dominated by the huge bandage-wrapped Samehada strapped across his "
          "back. Black cloak with red clouds, shark-like face, straw hat only when specified. "
          "Reproduce exactly; ignore its white background and layout. ")
KURAMA_INNER = ("Image {i} is the CREATURE REFERENCE for the fox behind the seal: an enormous orange "
                "nine-tailed fox, seen behind the barred inner-seal gate as red slit eyes, heavy "
                "muzzle and huge paws emerging from shadow. It must dwarf Naruto and never have a "
                "human face. Reproduce exactly; ignore its white background and layout. ")
KURAMA_FULL = ("Image {i} is the CREATURE REFERENCE for the nine-tailed fox: an enormous orange fox "
               "whose silhouette is nine separate tails, heavy muzzle, giant paws, and red slit "
               "eyes. It must dwarf every human and never have a humanized face. Reproduce exactly; "
               "ignore its white background and layout. ")

# These are three exact, mutually exclusive post-skip states. Do not substitute N13 or N13S.
N16_ARMOR = ("Image {i} is the CHARACTER REFERENCE for the blond older teen: approximately sixteen "
             "years old, an older teen rather than an adult, lean and long-limbed. His silhouette is "
             "shoulder-length heavy straight blond hair, with the long right bang covering his right "
             "eye. Blue left eye, faded whisker marks, closed level expression. He wears a partly "
             "visible Leaf forehead protector, bright red segmented samurai armour over a black "
             "high-neck under-suit, black gloves, black trousers and dark shinobi sandals. The dark "
             "purple gunbai with its chain is carried on his back. This state is swordless. "
             "Reproduce exactly; ignore its white background and layout. " + ALT + UNIQUE + " ")
N16_SWORD = ("Image {i} is the CHARACTER REFERENCE for the blond older teen: approximately sixteen "
             "years old, an older teen rather than an adult, lean and long-limbed. His silhouette is "
             "shoulder-length heavy straight blond hair, with the long right bang covering his right "
             "eye. Blue left eye, faded whisker marks, closed level expression. He wears a partly "
             "visible Leaf forehead protector, bright red segmented samurai armour over a black "
             "high-neck under-suit, black gloves, black trousers and dark shinobi sandals. A plain "
             "straight sword in a dark sash sheath is at his left hip, and the dark purple gunbai "
             "with its chain is carried on his back. This is a new sash sword, distinct from the lost ninjato. "
             "Reproduce exactly; ignore its white background and layout. " + ALT + UNIQUE + " ")
N16_BLACK = ("Image {i} is the CHARACTER REFERENCE for the blond older teen: approximately sixteen "
             "years old, an older teen rather than an adult, lean and long-limbed. His silhouette is "
             "shoulder-length heavy straight blond hair, with the long right bang covering his right "
             "eye. Blue left eye, faded whisker marks, closed level expression. He wears only the "
             "plain black high-neck long-sleeved shirt with a small red Uzumaki spiral on the chest, "
             "black trousers, black gloves and dark shinobi sandals. This state is without armour, "
             "forehead protector, gunbai, or sword. Reproduce exactly; "
             "ignore its white background and layout. " + ALT + UNIQUE + " ")

SASUKE16 = ("Image {i} is the CHARACTER REFERENCE for the older dark-haired teen: a tall, lean "
            "sixteen-year-old whose silhouette is upward-spiked black hair and a high-collared dark "
            "travel shirt marked by the Uchiha fan crest. Mature adolescent proportions, pale face, "
            "dark eyes, scowling expression. Reproduce exactly; ignore its white background and layout. ")
KARIN = ("Image {i} is the CHARACTER REFERENCE for the red-haired captive: a slim older teen, "
         "approximately sixteen, whose "
         "silhouette is long bright red hair and rectangular glasses. Guarded posture, subdued Oto "
         "captive clothing. Reproduce exactly; ignore its white background and layout. ")
YUGAO_V4 = ("Image {i} is the CHARACTER REFERENCE for the purple-haired Leaf kunoichi: a lean adult "
            "woman whose silhouette is purple hair tied high behind her head and a travel-worn dark "
            "shinobi outfit. Her face must carry clear wary, alarmed reactions without changing her "
            "identity. Reproduce exactly; ignore its white background and layout. ")
AO_V4 = ("Image {i} is the CHARACTER REFERENCE for the Kiri commander: a broad adult man whose "
         "silhouette is a dark wrap and vest, with an eyepatch framing his implanted Byakugan eye. "
         "Guarded crossed-arm posture. Reproduce exactly; ignore its white background and layout. ")
MEI_V4 = ("Image {i} is the CHARACTER REFERENCE for the Kiri rebel leader: a tall adult woman whose "
          "silhouette is long auburn hair gathered into a high braided topknot. Green eyes, dark "
          "blue dress over mesh, dignified command posture. She is the rebel leader rather than the Mizukage. "
          "Reproduce exactly; ignore its white background and layout. ")
CHOJURO_V4 = ("Image {i} is the CHARACTER REFERENCE for the young Kiri swordsman: a slim younger man "
              "whose silhouette is shaggy pale-blue hair and an oversized wrapped sword making his "
              "back look broad. Deferential posture. Reproduce exactly; ignore its white background "
              "and layout. ")
YAGURA_HUMAN = ("Image {i} is the CHARACTER REFERENCE for the Fourth Mizukage: a short adult man "
                "whose compact silhouette is dark clothing and a long hooked staff or coral-club. "
                "He is fully human in this state: no chakra cloak, tails, shell, or turtle features. "
                "Reproduce exactly; ignore its white background and layout. ")

# ---------------------------------------------------------------- creatures, forms, and props
YAGURA_CLOAK = ("Image {i} is the FORM REFERENCE for Yagura's chakra cloak: a human-sized crimson chakra "
                "silhouette with exactly three tails and demonic eyes. No turtle shell, no fourth "
                "tail, and no full beast body. Reproduce exactly; ignore its white background and layout. ")
SANBI_FULL = ("Image {i} is the CREATURE REFERENCE for the Three-Tails: a massive blue-grey turtle with a "
              "heavy ridged shell and body, exactly three visible tails, one red eye, and pale underplates. It must "
              "read as a turtle, not a fox, dragon, or Susano'o. Reproduce exactly; ignore its white "
              "background and layout. ")
MANDA = ("Image {i} is the CREATURE REFERENCE for the giant serpent: a colossal purple-grey snake "
         "whose silhouette is a horned, browed head and enormous dark-patterned coils. Its head and "
         "coils must stay legible against broken ground. Reproduce exactly; ignore its white "
         "background and layout. ")
SUSA_RIBCAGE = ("Image {i} is the FORM REFERENCE for the partial orange Susano'o: an opaque orange "
                "skeletal rib cage around Naruto, heavy black contour lines, with no finished humanoid "
                "body, helmet, arms, or weapons. Reproduce exactly; ignore its white background and layout. ")
SUSA_FINAL = ("Image {i} is the FORM REFERENCE for the final orange Susano'o: a colossal opaque orange "
              "armoured humanoid with a horned head and two broad blade forms. Keep the form solid, "
              "not translucent, and leave ground and fighters readable around it. Reproduce exactly; "
              "ignore its white background and layout. ")
GUNBAI_V4 = ("Image {i} is the PROP REFERENCE for the war fan: a large dark-purple gunbai with a "
             "bandaged handle and chain. Its face bears an Uzumaki spiral and Uchiha crest, never "
             "three tomoe. Reproduce exactly; ignore its white background and layout. ")
MOKUTON_STAKES = ("Image {i} is the TECHNIQUE REFERENCE for the Wood Release restraint: angular pale "
                  "wooden stakes and one coiling wooden serpent. It must read as a constructed restraint, "
                  "not a living snake. Reproduce exactly; ignore its white background and layout. ")
WOOD_WALL = ("Image {i} is the TECHNIQUE REFERENCE for the Wood Release barrier: a curved timber dome "
             "built from opposing pillars, solid and structural rather than a leafy hedge. Reproduce "
             "exactly; ignore its white background and layout. ")
WATER_TECHNIQUES = ("Image {i} is the TECHNIQUE REFERENCE for Yagura's Water Release: use its separate "
                    "opaque blue-grey forms for a faceless water clone, serpentine water dragon, or "
                    "curved defensive water wall as the page specifies. Keep hard inked edges and no "
                    "soft glow. Reproduce exactly; ignore its white background and layout. ")
KIRI_REBELS = ("Image {i} is the CROWD REFERENCE for unnamed Kiri rebels and scouts: practical dark "
                "blue-grey mist-shinobi clothing with deliberately varied builds, hair, face wraps, "
                "and vests. They remain anonymous and must not resemble named characters. Reproduce "
                "the visual vocabulary, not the sheet arrangement. ")
EYE_3TOMOE = ("Image {i} is the DETAIL REFERENCE for the ORDINARY ACTIVE THREE-TOMOE SHARINGAN: "
              "a blood-red iris with a black pupil and EXACTLY THREE black comma-shaped tomoe "
              "spaced evenly around it. Wherever this page says a character's eye holds the "
              "ordinary active Sharingan, draw exactly this design, at every scale including small "
              "and distant faces. It is never blue, never grey, and never a plain red disc without "
              "tomoe. Use it only for the ordinary Sharingan, never for the Mangekyo. ")

MANGEKYO_EYE = ("Image {i} is the DETAIL REFERENCE for Naruto's active eye pattern: a blood-red iris "
                 "with one black centre ring and exactly six broad black blades radiating outward. "
                 "This same canonical six-bladed design represents both his Mangekyo and its Eternal "
                 "state in this adaptation. Use it only when the page explicitly says the eye is active. ")

# Keys passed to R(...). Environment plates deliberately share the generic ENV binding imported
# from prompts.py; every character, creature, form, prop, and technique has a dedicated binding.
V4_REF_BINDINGS = {
    "homura": HOMURA,
    "koharu": KOHARU,
    "tsunade": TSUNADE,
    "shizune": SHIZUNE,
    "shikaku": SHIKAKU,
    "hiashi": HIASHI,
    "tsume": TSUME,
    "itachi": ITACHI,
    "kisame": KISAME,
    "kurama_inner": KURAMA_INNER,
    "kurama_full": KURAMA_FULL,
    "naruto_v4_armor": N16_ARMOR,
    "naruto_v4_armor_sword": N16_SWORD,
    "naruto_v4_black": N16_BLACK,
    "sasuke_16": SASUKE16,
    "karin": KARIN,
    "yugao_v4": YUGAO_V4,
    "ao_v4": AO_V4,
    "mei_v4": MEI_V4,
    "chojuro_v4": CHOJURO_V4,
    "yagura_human": YAGURA_HUMAN,
    "yagura_sanbi_cloak": YAGURA_CLOAK,
    "sanbi_full": SANBI_FULL,
    "manda": MANDA,
    "susanoo_orange_ribcage": SUSA_RIBCAGE,
    "susanoo_orange_final": SUSA_FINAL,
    "gunbai_v4": GUNBAI_V4,
    "mokuton_stakes_serpent": MOKUTON_STAKES,
    "wood_locking_wall": WOOD_WALL,
    "water_clone_dragon": WATER_TECHNIQUES,
    "kiri_rebel_mob": KIRI_REBELS,
    "mangekyo_design": MANGEKYO_EYE,
    "eye_3tomoe": EYE_3TOMOE,
    "env_konoha_outskirts": ENV,
    "env_konoha_after_invasion": ENV,
    "env_konoha_council_chamber": ENV,
    "env_inner_sewer": ENV,
    "env_uchiha_compound": ENV,
    "env_naka_shrine": ENV,
    "env_madara_eye_vault": ENV,
    "env_madara_hideout_exit": ENV,
    "env_orochimaru_lab": ENV,
    "env_oto_hidden_base": ENV,
    "env_oto_throne_hall": ENV,
    "env_oto_broken_exterior": ENV,
    "env_training_scarred_field": ENV,
    "env_wave_boat": ENV,
    "env_wave_forest": ENV,
    "env_valley_of_end": ENV,
    "env_konoha_alley": ENV,
    "env_kiri_fogline": ENV,
    "env_kiri_mist_gate": ENV,
    "env_kiri_rebel_camp": ENV,
    "env_mei_tent": ENV,
    "env_naruto_tent": ENV,
    "env_kiri_moonlit_hill": ENV,
    "env_mizukage_tower": ENV,
    "env_kiri_battlefield_open": ENV,
    "env_kiri_water_crater": ENV,
    "env_kiri_battlefield_crater": ENV,
}

# ---------------------------------------------------------------- names used in balloon tails
HOMURA_SPEAKER = "the elderly male adviser in dark formal robes"
KOHARU_SPEAKER = "the elderly female adviser with the pale hair bun"
TSUNADE_SPEAKER = "the blonde woman in the green haori"
SHIZUNE_SPEAKER = "the dark-haired medical aide"
SHIKAKU_SPEAKER = "the man with the long pineapple ponytail"
HIASHI_SPEAKER = "the stern long-haired Hyuga clan head"
TSUME_SPEAKER = "the wild-haired Inuzuka clan head with red cheek markings"
ITACHI_SPEAKER = "the black-haired man in the red-cloud cloak"
KISAME_SPEAKER = "the blue-grey shark-faced man"
KURAMA_SPEAKER = "the enormous nine-tailed fox"
N16_SPEAKER = "the older blond teen with the long hair over his right eye"
SASUKE16_SPEAKER = "the older dark-haired teen with the Uchiha crest"
KARIN_SPEAKER = "the red-haired girl in rectangular glasses"
YUGAO_V4_SPEAKER = "the purple-haired Leaf kunoichi"
AO_V4_SPEAKER = "the broad Kiri commander with the eyepatch"
MEI_V4_SPEAKER = "the auburn-haired Kiri rebel leader"
CHOJURO_V4_SPEAKER = "the pale-blue-haired Kiri swordsman"
YAGURA_SPEAKER = "the short Fourth Mizukage with the hooked staff"


def THOUGHT(*lines):
    """Untailed thought balloons. Entries: (panel, thinker, position, exact text)."""
    out = ("LETTERING: draw these thoughts in clean bold upright English comic lettering, all "
           "capitals and correctly spelled. Each thought sits in an untailed cloud-edged balloon "
           "near its named thinker. Use exactly these thoughts and no others:\n")
    for panel, thinker, where, text in lines:
        out += (f'  PANEL {panel} — untailed thought balloon in the {where}, belonging to '
                f'{thinker}, reading: "{text}"\n')
    return out + "Do not write any other text anywhere on the page. "

# ---------------------------------------------------------------- Kiri light
L_KIRI_MIST = "Lighting: cold blue-grey sea mist, wet stone reflections, distant forms swallowed by fog. "
L_KIRI_TENT = "Lighting: muted amber command-lamp light against damp blue-grey night. "
L_KIRI_MOON = "Lighting: hard pale moonlight over a dark grassy hill and low drifting mist. "
L_KIRI_BATTLE = "Lighting: flat storm-grey daylight, wet ground, steam and smoke kept separate from figures. "

GUREN = ("Image {i} is the CHARACTER REFERENCE for the blue-haired Oto commander: an adult woman "
         "whose defining feature is CHIN-LENGTH BLUE-VIOLET HAIR in a sharp bob with a long "
         "straight fringe swept across her forehead and two longer strands at the jaw. Narrow dark "
         "eyes. A sleeveless pale lavender wrap top with a wide dark sash, dark close-fitting "
         "trousers, dark arm wraps. Expression: guarded and proud. Reproduce exactly; ignore its "
         "white background and layout. ")
GUREN_SPEAKER = "the blue-haired woman in the lavender wrap top"
KUSHINA = ("Image {i} is the CHARACTER REFERENCE for the red-haired woman: an adult whose defining "
           "feature is VERY LONG STRAIGHT DARK-RED HAIR falling loose past her waist, with two "
           "shoulder-length strands framing her face. Warm violet-grey eyes, a pale cream "
           "high-collared blouse and a long sea-green skirt. Expression: warm and direct. "
           "Reproduce exactly; ignore its white background and layout. ")
KUSHINA_SPEAKER = "the long red-haired woman in the green skirt"
