"""Bench prompts. Drawn from real Volume 1 material so results are directly useful."""

STYLE = (
    "Premium 2D shonen manga illustration, full color. "
    "Clean confident black ink linework with varied line weight. "
    "Flat digital cel coloring: two to three tonal values per material, hard-edged shadows, no gradients. "
    "Hair drawn as distinct clusters and wedges, never individual strands. "
    "NEGATIVE: no depth-of-field blur, no photorealistic skin texture, no 3D render or CGI look, "
    "no painterly or oil-paint rendering, no lens flare, no watermark, no signature."
)

# ---------------------------------------------------------------- T1: char sheet
# Design spec is taken verbatim from fic ch3. Every clause is a scorable checkbox.
T1_CHARSHEET = (
    "Character reference sheet for a 13-year-old male ninja, three full-body views "
    "side by side on a plain white background: front view, three-quarter view, back view. "
    "Consistent height and proportions across all three. "
    "DESIGN: shoulder-length blond hair with two heavy bangs framing the face, the right bang "
    "hanging low enough to cover his right eye. Blue eyes. Three faint whisker marks on each cheek, "
    "barely visible. Completely blank, emotionless expression. "
    "He wears a black long-sleeved shirt with a LARGE red spiral emblem covering the whole chest, "
    "and a small matching red spiral between the shoulder blades on the back view. "
    "Black tapered trousers, black shinobi boots, and black fingerless gloves with a small red "
    "spiral on the back of each hand. "
    "No text, no labels, no lettering anywhere in the image. "
    + STYLE
)

# ---------------------------------------------------------------- T2: manga page
# Volume 1, Chapter 2 — the mob vanishes. The decisive test: can the model build
# a real multi-panel page with gutters and leave lettering space clean?
T2_PAGE = (
    "A single complete manga PAGE laid out as five panels with clean white gutters between them "
    "and a white page margin, portrait orientation, read left to right. "
    "PANEL 1 (wide, top third): night alley between two wooden buildings, a small blond boy in an "
    "orange jacket backed against the end wall, five adult villagers advancing on him as dark "
    "silhouettes from the left, lit from behind by distant festival lanterns. "
    "PANEL 2 (small, middle left): extreme close-up of the boy's face, eyes squeezed shut, braced for impact. "
    "PANEL 3 (small, middle right): the same alley from the boy's eye level — the villagers are GONE. "
    "Empty ground, a dropped lantern still rolling. "
    "PANEL 4 (small, lower left): the boy's eyes snapping open wide in confusion. "
    "PANEL 5 (wide, bottom third): low upward angle on an old man standing at the mouth of the alley, "
    "long black robes, long spiked black hair, a wooden walking cane, glowing red eyes, "
    "face half in shadow, absolutely still. "
    "Leave two or three EMPTY white speech balloons with clean black outlines in uncluttered areas — "
    "the balloons must contain NO text, NO letters, NO words, NO symbols of any kind. "
    "Do not write any text anywhere on the page. "
    + STYLE
)

# ---------------------------------------------------------------- T3: consistency
# Reference binding. Same locked character sheet -> two unrelated scenes.
# States what to TAKE from the reference and what to IGNORE in it.
_BIND = (
    "REFERENCE IMAGE 1 defines this character exactly: his face, his shoulder-length blond hair "
    "with the right bang covering his right eye, his faint whisker marks, and his full outfit "
    "(black long-sleeved shirt with the large red spiral on the chest, black trousers, black boots, "
    "black fingerless gloves with red spirals). Reproduce that character design precisely. "
    "IGNORE the reference's plain white background, IGNORE its three-view side-by-side layout, and "
    "IGNORE its neutral standing pose — draw him in the new scene described below. "
)

T3_SCENE_A = (
    _BIND +
    "SCENE: interior of a ninja academy classroom in daylight, tiered wooden desks full of "
    "twelve-year-old students who have all turned to stare at him in stunned silence. "
    "He stands alone in the doorway at the left, backlit from the corridor, expression completely blank, "
    "not looking at any of them. Wide shot from inside the room. Single illustration, not a multi-panel page. "
    "Leave one empty white speech balloon with a clean black outline. No text, no letters anywhere. "
    + STYLE
)

T3_SCENE_B = (
    _BIND +
    "SCENE: night, on top of a cliff carved with enormous stone faces, overlooking a lantern-lit village far below. "
    "He sits on the edge of the stone hair of one carved head, one knee up, seen from behind and slightly to the side, "
    "head turned in profile so his face is visible. Cold blue moonlight, wind moving his hair. "
    "Single illustration, not a multi-panel page. No speech balloons. No text, no letters anywhere. "
    + STYLE
)

# ---------------------------------------------------------------- T4: page + refs
# THE production case: multi-panel page bound to a locked character reference.
# Reference-binding syntax differs by model family (see models/CATALOG.md):
#   gpt-image-2 -> explicit indexed roles, "Image 1 is ..., use as ..."
#   nano-banana -> no special syntax; ordinal prose + restate features in text
CHAR_DESC = (
    "a 13-year-old boy with shoulder-length blond hair, two heavy bangs, the right bang covering "
    "his right eye, blue eyes, faint whisker marks, and a completely blank expression, wearing a "
    "black long-sleeved shirt with a large red spiral covering the chest, black trousers, black "
    "boots, and black fingerless gloves with a small red spiral on the back of each hand"
)

BIND = {
    "gpt": ("Image 1 is the CHARACTER REFERENCE for the boy: " + CHAR_DESC + ". "
            "Use Image 1 only to fix his face, hair and outfit — reproduce them exactly. "
            "Ignore Image 1's white background, its three-view layout and its standing pose. "
            "He is the ONLY character on this page who looks like this; every other person must "
            "look completely different, with different hair colour, clothes and face. "),
    "nano": ("The first image is a character sheet for the boy in this scene: " + CHAR_DESC + ". "
             "Reproduce that exact face, hair and outfit in the new scene. "
             "Do not copy the first image's white background, its three-view layout or its pose. "
             "He is the ONLY character on this page who looks like this; every other person must "
             "look completely different, with different hair colour, clothes and face. "),
}

_PAGE = (
    "A single complete manga PAGE laid out as four panels with clean white gutters and a white "
    "page margin, portrait orientation, read left to right. "
    "PANEL 1 (wide, top): interior of a ninja academy classroom, tiered wooden desks packed with "
    "twelve-year-old students, all of them turned and staring in stunned silence toward the doorway. "
    "PANEL 2 (tall, middle left): the boy standing alone in the open doorway, backlit from the "
    "corridor, full figure, expression blank, not looking at anyone. "
    "PANEL 3 (small, middle right): close-up of a black-haired boy at a desk, scowling, unsettled. "
    "PANEL 4 (wide, bottom): extreme close-up of the blond boy's face in three-quarter view, "
    "the visible eye cold and empty, the right bang hanging over the other eye. "
    "Leave two empty white speech balloons with clean black outlines in uncluttered areas. "
    "Every balloon must be left completely blank inside — plain white, empty, unlettered. "
    "The entire page must be free of writing, letters, numerals and symbols of any kind. "
)

def t4(family):
    return BIND[family] + _PAGE + STYLE
