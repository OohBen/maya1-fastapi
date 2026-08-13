"""Shared prompt vocabulary for Volume 2 chapters.

Character bindings lead with the SILHOUETTE-DEFINING feature — the one shape that identifies
the character at thumbnail size — because that is what survives being drawn small.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from genlib import UNIQUE  # noqa: E402

REFS = HERE.parent / "refs" / "images"


def R(*n):
    return [str(REFS / f"{x}.png") for x in n]


FILL = ("A single complete manga PAGE, portrait. The block of panels FILLS THE WHOLE PAGE out to a "
        "narrow even margin, separated only by thin white gutters — no broad empty white areas. ")

# ---------------------------------------------------------------- cast
N13 = ("Image {i} is the CHARACTER REFERENCE for the blond boy: a lean thirteen-year-old whose hair "
       "is LONG — hanging well past his jaw to his shoulders in heavy strands, two thick bangs "
       "framing his face, the right bang low enough to cover his right eye. His hair is never short "
       "and never spiky. Blue eyes, whisker marks nearly faded, blank expression, black long-sleeved "
       "shirt with a large red spiral on the chest, black trousers, dark sandals, black fingerless "
       "gloves with small red spirals. Reproduce exactly; ignore its white background and layout. "
       + UNIQUE + " ")
N13S = ("Image {i} is the CHARACTER REFERENCE for the blond boy: a lean thirteen-year-old with LONG "
        "blond hair hanging well past his jaw to his shoulders, two thick bangs framing his face, "
        "the right bang covering his right eye — never short, never spiky. Blue eyes, faded whisker "
        "marks, blank expression, black long-sleeved shirt with a large red spiral on the chest, "
        "black trousers, dark sandals, black fingerless gloves. A plain straight sword in a black "
        "scabbard is slung diagonally across his back, its wrapped hilt showing above his left "
        "shoulder. Reproduce exactly; ignore its white background and layout. " + UNIQUE + " ")
KAK = ("Image {i} is the CHARACTER REFERENCE for the masked man: tall, lean, spiky silver-grey hair "
       "swept to one side, dark cloth mask covering his face below the nose, slanted forehead "
       "protector covering his left eye so only his right eye shows, dark navy uniform under a green "
       "flak vest. Reproduce exactly; ignore its white background and layout. ")
HIR = ("Image {i} is the CHARACTER REFERENCE for the old leader: he WEARS ON HIS HEAD a tall white "
       "ceremonial hat with a broad brim, a large red front panel bearing one black brush kanji, and "
       "long white cloth drapes over his ears and shoulders. White ceremonial robes over a red "
       "under-robe, white sash, short grey goatee, deeply lined face, long wooden smoking pipe. "
       "Reproduce exactly; ignore its white background and layout. ")
SAS = ("Image {i} is the CHARACTER REFERENCE for the dark-haired boy: thirteen, pale, black hair "
       "spiked upward at the back with two long bangs at the front, dark eyes, high-collared navy "
       "shirt with a white round-and-triangle fan crest on the back, white arm warmers, scowling. "
       "Reproduce exactly; ignore its white background and layout. ")
SAK = ("Image {i} is the CHARACTER REFERENCE for the pink-haired girl: thirteen, chin-length bright "
       "pink hair with a red cloth headband holding it back, green eyes, an unusually broad "
       "forehead, sleeveless red qipao dress with a white circle crest, dark cycling shorts. "
       "Reproduce exactly; ignore its white background and layout. ")
ZET = ("Image {i} is the CREATURE REFERENCE: a humanoid plant creature split vertically, right half "
       "chalk white and left half pure black, round yellow pupil-less eyes, black cloak, green "
       "venus-flytrap shell around its head. Reproduce exactly; ignore its white background. ")
ZAB = ("Image {i} is the CHARACTER REFERENCE for the swordsman: a very tall heavily-built man whose "
       "silhouette is dominated by an ENORMOUS flat rectangular butcher-blade sword taller than a "
       "man, with a rounded notch and a circular hole through it. The lower half of his face is "
       "wrapped in white bandages. Short spiky black hair, no eyebrows, bare muscular arms, striped "
       "arm and leg warmers, a forehead protector worn slanted sideways on his head. Reproduce "
       "exactly; ignore its white background and layout. ")
HAK = ("Image {i} is the CHARACTER REFERENCE for the masked figure: slender and delicate, wearing a "
       "smooth plain WHITE PORCELAIN MASK over the whole face with two narrow eye slits and a small "
       "red swirl on the forehead. Long black hair tied back with two strands framing the mask, a "
       "pale green-grey full-length haori over dark clothing, brown sash. Reproduce exactly; ignore "
       "its white background and layout. ")
GAT = ("Image {i} is the CHARACTER REFERENCE for the businessman: a short fat smug middle-aged man "
       "barely taller than a child, round black sunglasses, pointed grey beard, black pinstripe "
       "suit, walking cane, one arm in a sling. Reproduce exactly; ignore its white background. ")
GAA = ("Image {i} is the CHARACTER REFERENCE for the red-haired boy: short and slight, twelve, whose "
       "silhouette is dominated by an ENORMOUS sand-coloured clay gourd strapped upright on his back, "
       "nearly as large as he is. Short messy dark red hair, NO EYEBROWS, heavy black rings of "
       "sleeplessness around pale blue-green eyes, a single blood-red kanji tattooed on the upper "
       "left of his forehead, dark maroon full-body outfit with a white sash. Reproduce exactly; "
       "ignore its white background and layout. ")
TEM = ("Image {i} is the CHARACTER REFERENCE for the blonde girl: fifteen, with FOUR separate blonde "
       "pigtails standing out from her head in a fan shape and a HUGE closed iron battle fan strapped "
       "diagonally across her back, taller than her torso. Teal eyes, pale lavender-grey short "
       "kimono dress with a dark sash. Reproduce exactly; ignore its white background and layout. ")
KAN = ("Image {i} is the CHARACTER REFERENCE for the face-painted boy: fourteen, in a black full-body "
       "hooded suit whose hood has two pointed cat-like ear shapes, with a LARGE BANDAGE-WRAPPED "
       "BUNDLE almost his own size strapped upright on his back. His whole face is painted with bold "
       "purple angular stripes. Reproduce exactly; ignore its white background and layout. ")
DAN = ("Image {i} is the CHARACTER REFERENCE for the bandaged old man: elderly, whose silhouette is "
       "defined by a WOODEN WALKING CANE in his left hand and his ENTIRE RIGHT ARM wrapped in white "
       "bandages from shoulder to fingertips and held in a sling across his chest. His RIGHT EYE is "
       "covered by bandages wound round his head; only his left eye shows, cold and narrow. A large "
       "X-shaped scar on his chin. Short dark hair, a plain white robe over dark clothing. "
       "Expression: patient, calculating, entirely without warmth. Reproduce exactly; ignore its "
       "white background and layout. ")
IBI = ("Image {i} is the CHARACTER REFERENCE for the scarred interrogator: a huge broad-shouldered "
       "man whose head is covered by a black bandana-style forehead protector tied down over his "
       "skull, with two long deep diagonal scars across his face and a heavy black trench coat over "
       "a flak vest. Expression: grim and amused. Reproduce exactly; ignore its white background. ")
ANK = ("Image {i} is the CHARACTER REFERENCE for the woman in the tan coat: late twenties, spiky "
       "violet hair pulled up into a short fanned ponytail, brown eyes, a long open tan overcoat "
       "worn over a fitted dark orange skirt and a full-body FISHNET MESH bodysuit, dark shin "
       "guards. Expression: manic, grinning. Reproduce exactly; ignore its white background. ")
KAB = ("Image {i} is the CHARACTER REFERENCE for the grey-haired boy in glasses: about nineteen, "
       "shoulder-length silvery-grey hair tied back, LARGE ROUND BLACK-RIMMED GLASSES, small dark "
       "eyes, a dark purple long-sleeved shirt and dark purple trousers, a shuriken holster on the "
       "right hip. Expression: helpful, pleasant, and not to be trusted. Reproduce exactly; ignore "
       "its white background and layout. ")
LEE = ("Image {i} is the CHARACTER REFERENCE for the boy in green: thirteen, with a SHINY BLACK "
       "BOWL-CUT haircut, ENORMOUS thick black eyebrows, huge round dark eyes, and a skin-tight "
       "bright green full-body jumpsuit with orange leg warmers and bandages wrapped round both "
       "forearms. His forehead protector is worn as a belt at his waist. Expression: earnest and "
       "intense. Reproduce exactly; ignore its white background and layout. ")
KUY = ("Image {i} is the CHARACTER REFERENCE for the black-haired princess: early twenties, long "
       "straight black hair, sharp dark eyes, heavy dark eye makeup. Reproduce exactly; ignore its "
       "white background and layout. ")
SHI = ("Image {i} is the CHARACTER REFERENCE for the bored boy: thirteen, black hair pulled up into "
       "a short spiky pineapple-shaped ponytail, narrow half-lidded eyes, small stud earrings, a "
       "short-sleeved grey-green mesh shirt under an open dark jacket with a green edge. Expression: "
       "permanently unbothered. Reproduce exactly; ignore its white background and layout. ")
INO = ("Image {i} is the CHARACTER REFERENCE for the platinum-blonde girl: thirteen, very long "
       "platinum-blonde hair in a high ponytail with one long bang covering the right side of her "
       "face, pale blue eyes, a purple crop top and matching purple skirt over bandaged legs. "
       "Reproduce exactly; ignore its white background and layout. ")
KIB = ("Image {i} is the CHARACTER REFERENCE for the boy with the dog: thirteen, wild brown hair, "
       "slit-pupil eyes, two bold red fang markings painted on his cheeks, sharp canine teeth, a "
       "grey fur-lined hooded coat — and a SMALL WHITE PUPPY riding on his head or in his hood. "
       "Reproduce exactly; ignore its white background and layout. ")
HIN = ("Image {i} is the CHARACTER REFERENCE for the shy girl: thirteen, short dark blue-black hair "
       "cut level with her jaw, and PALE LAVENDER-WHITE EYES WITH NO VISIBLE PUPILS, a cream hooded "
       "coat with fur trim. Expression: timid, always about to look away. Reproduce exactly; ignore "
       "its white background and layout. ")
SHN = ("Image {i} is the CHARACTER REFERENCE for the hidden boy: thirteen, whose face is almost "
       "entirely concealed — round BLACK SUNGLASSES and a high collar drawn up over his nose and "
       "mouth so only a strip of face and spiky dark brown hair show. A pale grey-green hooded coat. "
       "Reproduce exactly; ignore its white background and layout. ")
ORO = ("Image {i} is the CHARACTER REFERENCE for the pale one: tall and slender, with CHALK-WHITE "
       "paper-coloured skin and GOLDEN-YELLOW EYES WITH VERTICAL BLACK SLIT PUPILS ringed by purple "
       "markings. Very long straight black hair past the waist, parted in the middle. A cream-grey "
       "high-collared robe with a wide dark purple rope belt. A long thin tongue. Expression: a wide "
       "serpentine smile that never reaches the eyes. Reproduce exactly; ignore its white "
       "background and layout. ")
JIR = ("Image {i} is the CHARACTER REFERENCE for the white-haired man: large and powerfully built, "
       "in his fifties, whose silhouette is dominated by an ENORMOUS spiky WHITE mane falling to his "
       "waist and tied back. Two bold red lines run down his face from under each eye. A forehead "
       "protector with two small HORNS. Green kimono top and trousers over mesh armour, a red "
       "sleeveless haori with two yellow circles, a large scroll across his back. Reproduce exactly; "
       "ignore its white background and layout. ")
NEJ = ("Image {i} is the CHARACTER REFERENCE for the long-haired boy: thirteen, whose defining "
       "feature is PALE LAVENDER-WHITE EYES WITH NO VISIBLE PUPILS in a permanently cold stare. Long "
       "straight dark brown hair to the middle of his back, loosely tied near the end, two thin "
       "strands framing his face. A beige high-collared wrap top, dark shorts, bandages wound tightly "
       "round his right arm and right leg. Reproduce exactly; ignore its white background and layout. ")
HAY = ("Image {i} is the CHARACTER REFERENCE for the sickly proctor: a thin unwell man in his "
       "twenties, untidy dark brown hair, deep shadows under tired eyes, a blue bandana-style "
       "forehead protector over his head, dark navy uniform under a green flak vest, a sword across "
       "his back. Reproduce exactly; ignore its white background and layout. ")
GEN = ("Image {i} is the CHARACTER REFERENCE for the proctor with the needle: a lean man in his late "
       "twenties, shoulder-length light brown hair, a bandana-style forehead protector with the "
       "cloth hanging down at the back, dark navy uniform under a green flak vest, and a thin metal "
       "SENBON NEEDLE held in the corner of his mouth like a toothpick. Reproduce exactly; ignore "
       "its white background and layout. ")
ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and lighting. "
       "Do not copy its camera angle; ignore that it is empty of people. ")

# ---------------------------------------------------------------- names used in balloon tails
BOY = "the blond boy"
MAN = "the masked silver-haired man"
OLD = "the old man in the tall hat"
UCH = "the dark-haired boy"
GIRL = "the pink-haired girl"
SWORD = "the bandage-faced swordsman"
MASK = "the figure in the white mask"
RED = "the red-haired boy with the gourd"
HAWK = "the bandaged old man with the cane"
SCAR = "the scarred man in the black bandana"
COAT = "the violet-haired woman in the tan coat"
SPEC = "the grey-haired boy in round glasses"
GREEN = "the boy in the green jumpsuit"
LAZY = "the boy with the pineapple ponytail"
BLONDE = "the platinum-blonde girl with the long ponytail"
DOG = "the boy with the red fang markings and the puppy"
PALE = "the shy girl with the pale eyes"
SHADES = "the boy in the black sunglasses and high collar"
PALEONE = "the pale one with the golden slit eyes"
SAGE = "the big white-haired man"
FATE = "the long-haired boy with the pale eyes"
SICK = "the thin proctor with the bandana"
NEEDLE = "the proctor with the needle in his mouth"
FAN = "the blonde girl with four pigtails"
PAINT = "the boy with purple face paint"

# ---------------------------------------------------------------- light
L_DAY = "Lighting: clean flat daylight. "
L_OFF = "Lighting: warm late-afternoon light slanting through tall arched windows. "
L_DUSK = "Lighting: cool blue dusk. "
L_MIST = "Lighting: cold flat overcast light, thick white sea mist swallowing everything distant. "
L_SNOW = "Lighting: cold blue-white winter light off snow, long hard shadows. "


def ONLY(*names):
    """State the complete cast so no stray characters are invented."""
    return (f"The only people anywhere on this page are {', '.join(names)}. No other character "
            f"appears in any panel, in the foreground or the background. ")


def OFF(speaker):
    """Mark a speaker who is NOT DRAWN in that panel, so the tail runs off-panel."""
    return ("\x00", speaker)


def SAY(*lines):
    """Every balloon names its speaker AND its position. Entries: (panel, who, where, text)."""
    out = ("LETTERING: draw the speech balloons WITH their dialogue written inside, in clean bold "
           "upright English comic lettering, all capitals, correctly spelled. Each balloon must sit "
           "where stated and its TAIL MUST POINT DIRECTLY AT ITS NAMED SPEAKER, clear of every "
           "face. A balloon must never sit nearer to, or point at, any character other than its own "
           "speaker. Use exactly these balloons and no others:\n")
    for panel, speaker, where, text in lines:
        if isinstance(speaker, tuple) and speaker and speaker[0] == "\x00":
            out += (f'  PANEL {panel} — balloon in the {where}, spoken by {speaker[1]}, who is NOT '
                    f'DRAWN ANYWHERE IN THIS PANEL. Draw it as an OFF-PANEL balloon: its tail is a '
                    f'short straight spur running to the nearest panel border and stopping there, '
                    f'pointing out of the panel. The tail must NOT touch, overlap or aim at any '
                    f'face or figure that IS drawn in this panel. Reading: "{text}"\n')
        else:
            out += (f'  PANEL {panel} — balloon in the {where}, tail pointing at {speaker}, '
                    f'reading: "{text}"\n')
    out += "Do not write any other text anywhere on the page. "
    return out


def CAP(panel, where, text):
    """A square narration box — used sparingly, for time and place jumps only."""
    return (f'CAPTION: in PANEL {panel}, in the {where}, draw a plain rectangular narration box '
            f'with a thin black border, no tail, containing only the words: "{text}". It is not a '
            f'speech balloon and must not point at anyone. ')


def TITLE(text, where="upper right sky"):
    return (f'LETTERING: write the chapter title in the quiet {where}, in large bold upright English '
            f'capitals, correctly spelled, reading: "{text}". Draw no other text anywhere on the '
            f'page — no balloons, no sound effects, no numbers, no signature. ')


def SFX(panel, word, note=""):
    return (f'SOUND EFFECT: in PANEL {panel}, draw the hand-lettered manga sound effect "{word}" as '
            f'a large bold graphic shape with a heavy black outline, overlapping the figures and '
            f'cropped by the panel edge. {note}')
