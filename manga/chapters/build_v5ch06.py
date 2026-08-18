"""Volume 5, Chapter 6 — "Mother". 16 pages.

Source: fic ch13:5-77. Translated 1:1 from story/volume_05/drafts/ch06_mother.md — 80
speech balloons and one chapter marker across 16 pages. Reading order is RIGHT TO LEFT
per the approved `name`; every page states it.

Pages 1-14 are a DREAM-MEMORY of the opened inner seal space, not the physical world, and
every one of those pages says so in its own prompt so it cannot read as a place he has
travelled to. Pages 15-16 are the waking camp. Dream Naruto and current Naruto are
deliberately different ages and costumes and never share a page.

This builder must match the `name`, not improve on it. Every balloon below is the draft's
exact final text, in the draft's exact panel and position.

Reference gaps recorded for the owner (never invented here): there is no dedicated
kushina.png sheet, so she is bound from the two-person minato_kushina.png with the blond
half excluded by name; and there is no approved younger-training-period Naruto sheet, so
naruto_13.png carries the dream-memory boy.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import FILL, N13, OFF, ONLY, R, SAY, TITLE, ZET  # noqa: E402
from prompts_v4 import (GUNBAI_V4, N16_BLACK, N16_SWORD, N16_SPEAKER)  # noqa: E402

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
BOY13 = "the younger long-haired blond boy in the black shirt with the red spiral"
KUSHINA_SPEAKER = "the woman with the very long red hair in the green dress"
KUSHINA_PRESENT = ("the present-day red-haired woman in the green dress, who is telling this story "
                   "from OUTSIDE the memory image and is not drawn in this panel")
ZETSU = "the split black-and-white plant creature"
ZOR = ("The plant creature's split NEVER mirrors: seen from the front, its WHITE half is on the "
       "viewer's LEFT and its BLACK half on the viewer's RIGHT in every panel, exactly matching "
       "its reference image. ")

# There is no single-figure Kushina sheet in refs/images; the two-person parents sheet is the only
# source of her exact hair and dress, so the blond half is excluded by name on every page.
KUSHINA = (
    "Image {i} is a TWO-PERSON REFERENCE SHEET. Use ONLY THE RIGHT-HAND FIGURE of that sheet and "
    "COMPLETELY IGNORE the blond man on its left — he never appears as a person anywhere in this "
    "chapter. The right-hand figure is the CHARACTER REFERENCE for the red-haired woman: an adult "
    "woman whose silhouette is VERY LONG straight dark-red hair falling well past her waist, with "
    "blue eyes and a warm open face. She wears a long dark green pinafore dress over a pale cream "
    "short-sleeved blouse with a PALE HIGH COLLAR. Reproduce her face, hair and outfit exactly; "
    "ignore the sheet's white background, its lineup layout and its neutral standing pose. She is "
    "never a generic red-haired woman and never changes outfit. ")

ENV_SEAL = ("Image {i} is the LOCATION REFERENCE for the OPENED inner seal space — reuse its damp "
            "stonework, shallow standing water and colour palette, but the great barred cage is "
            "GONE: only one broken gate edge remains and no bars enclose anything. Do not copy its "
            "camera angle; ignore that it is empty of people. ")
ENV_CAMP = ("Image {i} is the LOCATION REFERENCE for the night forest camp beside the travel road — "
            "reuse its trees, trunks, ground cover and colour palette. Do not copy its camera "
            "angle; ignore that it is empty of people. ")

DREAM = ("THIS PAGE TAKES PLACE INSIDE A DREAM-MEMORY OF THE OPENED INNER SEAL SPACE, not in the "
         "physical world. It is a flooded mindscape: shallow black reflective water underfoot, warm "
         "red-gold seal light, the broken edge of the opened gate and faint drifting seal script — "
         "with NO sky, NO horizon, NO weather, NO forest, NO buildings and NO exterior scenery of "
         "any kind. There is no intact cage, no bars and no fox anywhere. Every seal marking, every "
         "scrap of torn seal paper and every drifting glyph is ILLEGIBLE SCRIBBLE, not readable "
         "words. ")
SOLID = ("The red-haired woman is FULLY SOLID and tangible on this page: opaque everywhere, "
         "deforming her own clothing where he holds her, and disturbing the water she touches. She "
         "is never translucent, never ghostly and never glowing through. ")
BOYSTATE = ("The blond boy in this dream is the YOUNGER training-period version: no red armour, no "
            "gunbai, no sword, no forehead protector, and no Sharingan or six-bladed pattern in "
            "either eye. ")
WAKE = ("The present-day sixteen-year-old is a DIFFERENT, OLDER figure from the boy in the dream, "
        "and the two are never drawn on the same page. His visible left eye carries NO Sharingan "
        "and NO six-bladed pattern anywhere on this page. ")

# ------------------------------------------------------------------ the dissolution clock
# The fade is this chapter's clock and it may ONLY advance. It reset on p12 in the first pass —
# p12 drew her completely solid after p11 had already taken most of a forearm — so the state is
# now declared as a per-page constant instead of being left to each page's prose.
FADE_LAW = ("DISSOLUTION CLOCK — HARD RULE. The red-haired woman is dissolving into red-gold seal "
            "light, and that dissolution only ever ADVANCES from page to page. It never shrinks, "
            "never heals, never pauses and never resets: no later page may show her more solid "
            "than an earlier one. The order across the chapter is fixed — a fingertip, then a "
            "strand of hair, then most of one forearm, then the forearm and the hand, then the "
            "lower body, then almost all of her. Wherever a part of her has already gone, it "
            "stays gone. ")
FADE_07 = (FADE_LAW + "STATE ON THIS PAGE: the dissolution is confined to the TIPS OF THE FINGERS "
           "of ONE hand, breaking into red-gold script. Everything else — both arms, her hair, "
           "her face, her blouse and her long skirt — is completely solid and opaque. ")
FADE_08 = (FADE_LAW + "STATE ON THIS PAGE: the fingers of one hand are gone into red-gold script "
           "AND one long strand of her red hair dissolves at its end. Nothing else has gone yet; "
           "her arms, face and clothing stay solid. ")
FADE_09 = (FADE_LAW + "STATE ON THIS PAGE: the fingers of one hand and one strand of her hair are "
           "gone into red-gold script, and the dissolution has crept up to that WRIST. The hand "
           "she touches him with is her other, still-solid hand. ")
FADE_10 = (FADE_LAW + "STATE ON THIS PAGE: one hand and wrist and one strand of hair are gone "
           "into red-gold script; the LOWER HALF of that forearm has begun to break up as well. "
           "Her other hand, her face, her hair and her clothing are still solid. ")
FADE_11 = (FADE_LAW + "STATE ON THIS PAGE: MOST OF ONE FOREARM has now turned to red-gold script, "
           "from the fingers up nearly to the elbow, with only the palm she presses to his chest "
           "still solid. Her face, hair and clothing remain solid. ")
FADE_12 = (FADE_LAW + "STATE ON THIS PAGE — THIS IS THE PAGE THE CLOCK PREVIOUSLY BROKE ON, SO "
           "DRAW IT DELIBERATELY: MORE of her is gone than on the page before. The WHOLE of one "
           "forearm and hand is now red-gold script — that arm ends at the elbow and there is "
           "clear water and light visible THROUGH where it used to be — and the dissolution has "
           "spread across that shoulder and started at the hem of her long skirt. She is NOT "
           "solid, NOT whole and NOT opaque anywhere on that side. In EVERY panel of this page "
           "where that arm or hand would be — including the panels where she sits upright with "
           "both hands open on her knees and the panel where she looks down into the water — the "
           "missing forearm must be visibly missing. Her face, her hair and her upper body remain "
           "solid so she is still recognisably herself. ")
FADE_13 = (FADE_LAW + "STATE ON THIS PAGE: one whole arm is gone and her LOWER BODY — skirt, hips "
           "and legs — is mostly red-gold script by the last panel. Her face, hair and upper body "
           "remain solid. ")
FADE_14 = (FADE_LAW + "STATE ON THIS PAGE: almost all of her goes. She ends as her face, her "
           "smile, her very long red hair and one hand, then nothing. ")

# Her design is the one thing the chapter's key page got wrong: on p10 she came back as a second
# blond boy in his own shirt. Stated once here, and attached hard to that page.
KUSHINA_LOCK = (
    "THE RED-HAIRED WOMAN IS NOT A SECOND VERSION OF THE BOY. She is an ADULT WOMAN, a full head "
    "taller than him, with a woman's face and figure. Her hair is LONG, STRAIGHT and DARK RED — "
    "falling loose past her waist — and it is NEVER blond, never yellow, never blond streaked "
    "with red, and never cut short or spiked. She wears a PALE CREAM HIGH-COLLARED LONG-SLEEVED "
    "BLOUSE and a LONG SEA-GREEN SKIRT that reaches her ankles. She NEVER wears his black shirt, "
    "NEVER wears a red Uzumaki spiral on her chest, NEVER wears fingerless gloves, NEVER wears "
    "trousers or shorts, and NEVER wears anything he is wearing. Her clothing and his have no "
    "colour, garment or emblem in common. If the two of them appear in the same panel they must "
    "be instantly separable at thumbnail size by hair colour, height and outfit. ")

# p10 is the one image this chapter exists to deliver and the two-person parents sheet failed it:
# the model took the BLOND half and drew her as a second Naruto. refs/images/kushina.png is a
# dedicated SINGLE-FIGURE sheet of her — no blond man on it at all — so that page uses it instead.
KUSHINA_SOLO = (
    "Image {i} is the SINGLE-FIGURE CHARACTER REFERENCE for the red-haired woman, showing her "
    "front, three-quarter and back views. She is an ADULT WOMAN whose defining feature is VERY "
    "LONG STRAIGHT DARK-RED HAIR falling loose past her waist, with two shoulder-length strands "
    "framing her face and a small clip above one ear. Warm blue-violet eyes, a pale cream "
    "HIGH-COLLARED long-sleeved blouse, a LONG SEA-GREEN SKIRT to the ankles, dark sandals. "
    "Reproduce her face, hair, colours and outfit exactly; ignore the sheet's white background "
    "and its three-view lineup layout. There is NO man anywhere on this sheet and no second "
    "figure to borrow from. ")

L_SEAL = ("Lighting: warm red-gold seal light rising off shallow black reflective water, soft "
          "reflected glow from below, no sky and no hard exterior shadows. ")
L_CAMP = ("Lighting: hard cold blue moonlight falling through branches onto dry dark earth, deep "
          "hard black shadows, no campfire and no warm light source. ")

PAGES = [
 # ---- Spread 1: the embrace he cannot control ----------------------------------------
 ("p01", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=4),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + SOLID
  + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER) +
  "FOUR panels. Touch arrives before any explanation. The only text on this page is the chapter "
  "marker.\n"
  "PANEL 1 (narrow upper-right strip): still life with NO characters at all — the torn paper seal "
  "and the broken gate edge hanging above shallow black water, red-gold chakra script drifting "
  "leftward out of the tear. At the LOWER LEFT of this panel, reserve a clear, quiet patch of water "
  "reflection: no figure, effect, script or glow may enter it, and it carries only the chapter "
  "marker.\n"
  "PANEL 2 (tall upper-left): medium two-shot — the younger blond boy stands at SCREEN-LEFT, body "
  "angled toward the right, arms at his sides. The red-haired woman resolves out of the seal light "
  "at SCREEN-RIGHT, facing him. Their eye-line crosses the panel from right to left. His practised "
  "stillness breaks only in his widened eyes.\n"
  "PANEL 3 (shallow middle tier, full width): medium-long shot — she crosses from SCREEN-RIGHT "
  "toward him at SCREEN-LEFT with both arms opening. He stays rooted; his right hand has lifted a "
  "few centimetres and has not decided whether to reach. Her very long red hair streams behind her "
  "and carries the eye leftward.\n"
  "PANEL 4 (dominant bottom half of the page, the focal panel): close two-shot — she folds him into "
  "both arms at centre-left. HER FACE IS HIDDEN beyond his shoulder and must not be readable; his "
  "face is buried against hers. His hands hover for one beat and the nearer one knots into the "
  "cloth at her back. The broken seal glows small and distant at the far right. " + L_SEAL
  + TITLE("CHAPTER 6 — MOTHER",
          where="protected patch of clear water reflection at the LOWER LEFT of PANEL 1"),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "high"),

 ("p02", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + SOLID
  + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER) +
  "SIX panels. Her face is revealed and he names the relationship himself. No balloon may cover his "
  "tears, her hands, or the space between their faces.\n"
  "PANEL 1 (small upper-right close-up): the first fresh wet tear clears his lower lashes and "
  "travels across an otherwise dry cheek. His eye looks down-left into her shoulder.\n"
  "PANEL 2 (small upper-centre close-up): over his shoulder, HER FACE at last — crying and smiling "
  "at the same time, eye-line pointing down-left toward him.\n"
  "PANEL 3 (upper-left medium crop): his suspended second hand finally grips her back, completing "
  "the embrace. Her palm presses firmly between his shoulders.\n"
  "PANEL 4 (wide middle band, full width, the focal panel): they separate only to arm's length. He "
  "stands at SCREEN-LEFT with both hands on her shoulders; she stands at SCREEN-RIGHT with her "
  "hands closed around his forearms. Their eyes meet across clean empty negative space, which is "
  "where the two balloons sit.\n"
  "PANEL 5 (lower-right close two-shot): she cups his face in both hands and studies how much he "
  "has grown. He does not pull away.\n"
  "PANEL 6 (lower-left): medium shot — she lowers herself to sit directly on the reflective water, "
  "which ripples under her, and pats the place beside her. He follows the gesture with his eyes. "
  + L_SEAL
  + SAY((4, BOY13, "upper right of the negative space between them", "MOTHER."),
        (4, KUSHINA_SPEAKER, "below and left of the first balloon", "MY SON."),
        (5, KUSHINA_SPEAKER, "upper right", "LOOK AT YOU. YOU'VE GROWN SO WONDERFULLY."),
        (6, KUSHINA_SPEAKER, "upper right", "SIT WITH ME?")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "medium"),

 # ---- Spread 2: she already knows -----------------------------------------------------
 ("p03", dict(scene="dialogue", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + SOLID
  + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER) +
  "SIX panels. Her first act is to spare him from recounting his childhood.\n"
  "PANEL 1 (wide upper-right): medium two-shot — they sit side by side on the shallow water, she at "
  "SCREEN-RIGHT and he at SCREEN-LEFT, knees angled slightly toward each other. He watches her "
  "profile rather than the seal-space.\n"
  "PANEL 2 (small upper-left close-up): her eyes turn toward him before her head follows.\n"
  "PANEL 3 (middle-right): medium shot — she looks past him toward dim abstract fragments of the "
  "life she watched, floating in the red-gold light: an apartment window, an empty swing, a "
  "training corridor. They are empty of people, carry no readable writing, and show no new event.\n"
  "PANEL 4 (middle-left close-up): his small smile stills. He turns fully toward her, eye-line "
  "rightward.\n"
  "PANEL 5 (dominant lower-right, the focal panel): close two-shot — she turns fully toward him and "
  "lays her right hand over his clenched left hand. Her gaze holds his; his fingers begin to uncurl "
  "under hers.\n"
  "PANEL 6 (lower-left close-up on the JOINED HANDS ONLY, no faces): her fingers close around his. "
  "His hand is now open. " + L_SEAL
  + SAY((1, BOY13, "upper right, over the gap between them", "I HAVE ALWAYS WANTED TO MEET YOU."),
        (2, KUSHINA_SPEAKER, "upper right", "I KNOW."),
        (3, KUSHINA_SPEAKER, "upper right", "I HAVE BEEN WATCHING YOU FROM HERE."),
        (4, BOY13, "upper right", "ALL OF IT?"),
        (5, KUSHINA_SPEAKER, "upper right", "ALL OF IT."),
        (5, BOY13, "below the first balloon", "THEN YOU KNOW."),
        (6, OFF(KUSHINA_SPEAKER), "upper right", "I DO. I WON'T MAKE YOU TELL ME AGAIN.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 ("p04", dict(scene="dialogue", light="dark", cast="two", mood="calm", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + SOLID
  + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER,
         "a younger version of the SAME red-haired woman, appearing ONLY as a small distant "
         "silhouette inside the red-gold chakra vision in panel 3") +
  "SIX panels. She becomes a person with a history, and he finds the source of his old speech "
  "habit.\n"
  "PANEL 1 (upper-right medium): she straightens and plants both palms on her knees, changing the "
  "energy of the scene. His eye-line rises with her.\n"
  "PANEL 2 (upper-left close-up): his mouth lifts slightly; his shoulders are no longer squared for "
  "defence. He gives her his full attention. No text in this panel.\n"
  "PANEL 3 (middle-right): behind the seated woman, red-gold chakra shapes itself into a coastline "
  "that becomes a distant village gate. A YOUNGER version of the same red-haired woman walks toward "
  "it as a small flat silhouette. No readable signs, no crests to decipher, no other people.\n"
  "PANEL 4 (middle-left): the gate dissolves into a single spiral emblem. The present red-haired "
  "woman touches the front of her green dress over her heart as she keeps talking. The boy is in "
  "the left foreground, listening.\n"
  "PANEL 5 (lower-right close two-shot): his eyes widen at her final phrase. She pauses, following "
  "the change in his face.\n"
  "PANEL 6 (dominant lower-left two-shot, the focal panel): he lets out a small surprised laugh and "
  "looks down; she leans toward him with mock offence. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "BUT I CAN TELL YOU WHO YOUR MOTHER WAS."),
        (3, KUSHINA_SPEAKER, "upper right", "I WAS SENT FROM UZUSHIO TO KONOHA TO CARRY THE NINE-TAILS."),
        (4, KUSHINA_SPEAKER, "upper right", "BUT I NEVER STOPPED BEING PROUD TO BE UZUMAKI, YA KNOW!"),
        (5, BOY13, "upper right", "THAT PHRASE. I USED TO SAY IT."),
        (5, KUSHINA_SPEAKER, "below and left of the first balloon", "YOU GOT IT FROM ME."),
        (6, BOY13, "upper right", "SO THAT WAS YOUR FAULT."),
        (6, KUSHINA_SPEAKER, "below and left of the first balloon", "MY GIFT."))
  + "PANEL 6 CARRIES TWO BALLOONS AND BOTH MUST BE LETTERED — the joke has no punchline without "
    "the second. Draw the boy's balloon reading \"SO THAT WAS YOUR FAULT.\" at the UPPER RIGHT of "
    "the panel with its tail to his mouth, and a SECOND, SEPARATE balloon reading \"MY GIFT.\" "
    "below it and to its LEFT, with its own tail running to the red-haired woman's mouth. \"MY "
    "GIFT.\" is two words, spelled M-Y and G-I-F-T, and it is never omitted, never merged into "
    "the first balloon and never left empty. Leave clear space in the lower-left of that panel "
    "for it. ",
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 # ---- Spread 3: both names are hers ---------------------------------------------------
 ("p05", dict(scene="dialogue", light="dark", cast="two", mood="calm", panels=5),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + SOLID
  + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER,
         "a younger version of the SAME red-haired woman and three faceless academy-age children, "
         "appearing ONLY inside one bordered memory inset in panel 1 and drawn as flat indistinct "
         "silhouettes with no readable features") +
  "FIVE panels. He gets to experience his mother as a person rather than as a loss.\n"
  "PANEL 1 (upper-right MEMORY INSET with a hard border and slightly desaturated colour): a younger "
  "version of the red-haired woman stands at SCREEN-RIGHT while three academy-age children point at "
  "her red hair from SCREEN-LEFT. Their faces stay indistinct — flat silhouettes, no features, no "
  "names. The younger woman inside the inset keeps her MOUTH CLOSED; she is not the speaker.\n"
  "PANEL 2 (upper-left, present): close-up — the present red-haired woman rolls one sleeve back a "
  "fraction and flexes her hand, grinning. The boy watches from off-panel to the left and is not "
  "drawn in this panel.\n"
  "PANEL 3 (middle-right): close shot — the boy tilts his head, deliberately solemn.\n"
  "PANEL 4 (middle-left): medium shot — she raises both fists in a compact, playful stance.\n"
  "PANEL 5 (dominant bottom panel, the focal panel): wide two-shot — he laughs openly, head lowered "
  "and one hand briefly over his eyes; she laughs with him at SCREEN-RIGHT. Their shoulders angle "
  "toward each other. This open laugh happens ONLY here inside the remembered encounter. No text in "
  "this panel. " + L_SEAL
  + SAY((1, OFF(KUSHINA_PRESENT), "upper right", "THEY USED TO MOCK MY RED HAIR."),
        (2, KUSHINA_SPEAKER, "upper right", "I CHANGED THEIR MINDS."),
        (3, BOY13, "upper right", "WITH DIPLOMACY?"),
        (4, KUSHINA_SPEAKER, "upper right", "WITH MY FISTS.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 ("p06", dict(scene="dialogue", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + ONLY(BOY13, KUSHINA_SPEAKER) +
  "SIX panels. She is Uchiha by blood and Uzumaki by choice, and she says so herself.\n"
  "The red-haired woman stays FULLY SOLID and opaque through panels 1-5; the very first trace of "
  "fading in this chapter appears in panel 6 and nowhere earlier.\n"
  "PANEL 1 (upper-right): medium two-shot — the laughter settles. She looks down at the water, "
  "where a dark round-and-triangle fan crest interrupts the reflected spiral emblem. He follows her "
  "eye-line.\n"
  "PANEL 2 (upper-left close-up): he looks up from the reflection to her face.\n"
  "PANEL 3 (middle-right close-up): she meets his eyes and nods once.\n"
  "PANEL 4 (middle-left two-shot): she touches the fan crest reflected in the water between them "
  "while his hand stays beside the spiral emblem. Both reflections carry equal visual weight.\n"
  "PANEL 5 (wide lower-right, the focal panel): she places one hand firmly over her own heart and "
  "sits taller. He faces her from SCREEN-LEFT.\n"
  "PANEL 6 (lower-left close crop): he nods. At the very bottom edge of the panel, the tips of her "
  "nearest fingers have just begun to break apart into red-gold seal light. Neither of them has "
  "looked down at it yet. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "THEN I LEARNED WHO MY FATHER WAS."),
        (2, BOY13, "upper right", "MADARA."),
        (3, KUSHINA_SPEAKER, "upper right", "MADARA UCHIHA."),
        (4, KUSHINA_SPEAKER, "upper right", "THAT MAKES ME AS MUCH UCHIHA BY BLOOD AS YOU."),
        (5, KUSHINA_SPEAKER, "upper right", "BUT I AM KUSHINA UZUMAKI. PROUDLY."),
        (6, BOY13, "upper right", "I UNDERSTAND.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 # ---- Spread 4: listen while I can ----------------------------------------------------
 ("p07", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_07 + ONLY(BOY13, KUSHINA_SPEAKER) +
  "FIVE panels. He is given an active objective he cannot complete: keep her here. Her fading is "
  "still confined to one hand — the rest of her stays solid and opaque.\n"
  "PANEL 1 (upper-right close-up): one of her fingertips dissolving into reflected script. His hand "
  "enters from the lower left and has NOT touched it. His mouth is not in this panel.\n"
  "PANEL 2 (upper-left close-up): she looks at the fading edge, then back at him. Her smile is sad "
  "but not frightened.\n"
  "PANEL 3 (dominant middle band, the focal panel): close two-shot — he catches her wrist with both "
  "hands and pulls it toward his chest at SCREEN-LEFT. She stays at SCREEN-RIGHT and covers his "
  "hands with her intact hand. Their eye-lines lock.\n"
  "PANEL 4 (lower-right): medium close-up — she shakes her head once without taking her hand away. "
  "His jaw tightens; he does not release her.\n"
  "PANEL 5 (lower-left, wide): close two-shot — she moves closer until their foreheads nearly "
  "touch, keeping his hands trapped between them. " + L_SEAL
  + SAY((1, OFF(BOY13), "upper right", "YOUR HAND."),
        (2, KUSHINA_SPEAKER, "upper right", "I KNOW."),
        (3, BOY13, "upper right", "THEN STAY."),
        (4, KUSHINA_SPEAKER, "upper right", "I CANNOT."),
        (5, KUSHINA_SPEAKER, "upper right, in the space behind his head", "SO LISTEN WHILE I CAN STILL SAY THIS."))
  + "IN PANEL 3 THE BOY IS THE SPEAKER OF \"THEN STAY.\" — he stands at SCREEN-LEFT and she "
    "stands at SCREEN-RIGHT. Draw a LONG tail that travels all the way from the balloon LEFTWARD "
    "and DOWN to the BLOND BOY'S MOUTH at panel-left, passing clear of the woman entirely. The "
    "tail must NOT point down-right, must NOT end on her hair, her face or her shoulder, and must "
    "not stop short at whichever figure is nearer the balloon. Her reply \"I CANNOT\" comes in "
    "the NEXT panel and is spoken by a different person, so if this tail lands on her the whole "
    "exchange reads as one speaker. ",
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 ("p08", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_08 + ONLY(BOY13, KUSHINA_SPEAKER,
         "the outline of a swaddled infant appearing ONLY inside one explicitly imagined symbolic "
         "inset in panel 2, drawn as a plain empty outline shape rather than a real baby in a real "
         "room") +
  "SIX panels. She grieves the ordinary motherhood she lost before she asks him for anything. Her "
  "fading is still small: one hand and one strand of hair, nothing more. No balloon may cover her "
  "hands or the fading edges of her body.\n"
  "PANEL 1 (upper-right medium): she draws him into a gentler second embrace, her cheek against his "
  "hair. His grip is careful now, as though force would make her disappear faster.\n"
  "PANEL 2 (upper-left SYMBOLIC INSET in warm empty negative space): her two hands cradle the plain "
  "OUTLINE of a swaddled infant. It is explicitly an imagined wish — no room, no furniture, no "
  "date, no face inside the outline, and no other person.\n"
  "PANEL 3 (middle-right close-up): she closes her eyes. One strand of her red hair dissolves at "
  "the end into seal light.\n"
  "PANEL 4 (middle-left): medium two-shot — she opens her eyes and eases him back far enough to see "
  "him. Her hands stay on his shoulders; his stay at her waist.\n"
  "PANEL 5 (wide lower-right, the focal panel): close two-shot — she smiles directly at him with "
  "tears still on her face. His eyes are level with hers and completely unguarded.\n"
  "PANEL 6 (lower-left close-up on HER HAND squeezing his shoulder, no faces): his hand rises to "
  "cover hers. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "I WANTED TO HOLD YOU WHEN YOU WERE A BABY."),
        (2, OFF(KUSHINA_PRESENT), "upper right", "TO FEED YOU. TO HEAR YOU CRY FOR ME."),
        (3, KUSHINA_SPEAKER, "upper right", "THAT LIFE WAS TAKEN FROM US."),
        (4, KUSHINA_SPEAKER, "upper right", "BUT I HAVE YOU NOW."),
        (5, KUSHINA_SPEAKER, "upper right", "AND I AM PROUD TO CALL YOU MY SON."),
        (6, OFF(KUSHINA_SPEAKER), "upper right", "CAN YOU DO SOMETHING FOR YOUR MOTHER?")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 # ---- Spread 5: life between objectives ------------------------------------------------
 ("p09", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=5),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_09 + ONLY(BOY13, KUSHINA_SPEAKER) +
  "FIVE panels. Her request arrives in terms he first takes literally.\n"
  "PANEL 1 (narrow upper-right): close shot — he gives one immediate, solemn nod. Her hand stays on "
  "his shoulder. No text in this panel.\n"
  "PANEL 2 (upper-left close two-shot): she touches his cheek with her intact hand. He looks at her "
  "rather than away.\n"
  "PANEL 3 (wide middle band): two-shot — his brow draws in, not rejecting her but interpreting her "
  "literally; her expression firms in immediate correction. They hold a direct eye-line, he at "
  "SCREEN-LEFT and she at SCREEN-RIGHT.\n"
  "PANEL 4 (dominant lower-right, the focal panel): behind him the water reflects a receding chain "
  "of objects marching away into the dark: a training weight, a single red eye mark with three "
  "black comma marks, a battlefield crater, and a road running out of sight. They are plain visual "
  "shorthand — NO labels, NO writing, NO people inside them. She stands at SCREEN-RIGHT facing "
  "him.\n"
  "PANEL 5 (lower-left): medium two-shot — she steps between him and the reflected road. His "
  "eye-line stops on her. " + L_SEAL
  + SAY((2, KUSHINA_SPEAKER, "upper right", "LIVE, NARUTO."),
        (3, BOY13, "upper right", "I AM ALIVE."),
        (3, KUSHINA_SPEAKER, "below and left of the first balloon", "THAT IS NOT WHAT I SAID."),
        (4, KUSHINA_SPEAKER, "upper right", "YOU COMPLETE ONE OBJECTIVE AND REACH FOR THE NEXT."),
        (5, KUSHINA_SPEAKER, "upper right", "I WANT YOU TO ENJOY THE LIFE BETWEEN THEM."))
  + "PANEL 3 CARRIES TWO BALLOONS AND THEIR ORDER IS THE POINT OF THE PANEL — the statement must "
    "be read before the rebuttal. Do NOT simply park each balloon above its own speaker. Place "
    "the boy's balloon \"I AM ALIVE.\" HIGH and at the RIGHT-HAND END of the panel's empty middle "
    "space, and place the woman's balloon \"THAT IS NOT WHAT I SAID.\" BELOW it and further LEFT, "
    "clearly lower and clearly further left, so that reading right to left and top to bottom "
    "delivers \"I AM ALIVE.\" first. Her balloon is never level with his and never further right "
    "than his. The boy stands at SCREEN-LEFT, so his balloon needs a LONG tail travelling left "
    "and down to his mouth; the woman stands at SCREEN-RIGHT, so hers needs a LONG tail "
    "travelling right to her mouth. The two tails cross in the empty middle of the panel — that "
    "is correct and intended. ",
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "medium"),

 ("p10", dict(scene="emotional_closeup", light="dark", cast="two", mood="calm", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA_SOLO.format(i=2) + ENV_SEAL.format(i=3) + DREAM
  + BOYSTATE + KUSHINA_LOCK + FADE_10
  + ONLY(BOY13, KUSHINA_SPEAKER) +
  "SIX panels. The smile has to be earned, small, and specific to this encounter.\n"
  "PANEL 1 (upper-right): medium shot — he looks down-left at their two reflections, shoulders "
  "tightening again.\n"
  "PANEL 2 (upper-left): close two-shot — she leans DOWN INTO his lowered eye-line instead of "
  "forcing his chin up.\n"
  "PANEL 3 (middle-right): close shot — she taps one finger lightly over his heart. His eyes follow "
  "the gesture, then return to hers. No balloon may cover that chest touch.\n"
  "PANEL 4 (middle-left close-up): she brushes a tear track from his cheek with her thumb.\n"
  "PANEL 5 (dominant lower-right close-up, the focal panel): he looks at her and a small, unforced "
  "smile forms through the remaining tears. It is warm but restrained and closed-mouthed — "
  "recognisably this quiet boy, never a broad open-mouthed grin.\n"
  "PANEL 6 (lower-left close-up): she laughs once through her tears and rests her forehead against "
  "his. " + L_SEAL
  + SAY((1, BOY13, "upper right", "I DON'T KNOW HOW."),
        (2, KUSHINA_SPEAKER, "upper right", "THEN BEGIN SMALL."),
        (3, KUSHINA_SPEAKER, "upper right", "WHEN SOMETHING MAKES YOU HAPPY, LET IT."),
        (4, KUSHINA_SPEAKER, "upper right", "SMILE WHEN THE SMILE IS YOURS."),
        (5, BOY13, "upper right", "LIKE THIS?"),
        (6, KUSHINA_SPEAKER, "upper right", "EXACTLY LIKE THAT."))
  + "THIS PAGE IS THE ONE IMAGE THE CHAPTER EXISTS TO DELIVER, AND PANEL 1 IS WHERE IT PREVIOUSLY "
    "FAILED. In PANEL 1 there are exactly TWO figures and they must be impossible to confuse. The "
    "BOY is short, thirteen, with LONG BLOND hair, a BLACK long-sleeved shirt carrying a LARGE "
    "RED UZUMAKI SPIRAL on the chest, black trousers and black fingerless gloves with small red "
    "spirals. The WOMAN is an ADULT, a full head TALLER than him, with VERY LONG STRAIGHT "
    "DARK-RED HAIR past her waist, a PALE CREAM HIGH-COLLARED BLOUSE and a LONG SEA-GREEN SKIRT "
    "reaching her ankles. She is NOT blond and NOT blond streaked with red; she does NOT wear a "
    "black shirt; she does NOT wear a red Uzumaki spiral anywhere; she does NOT wear fingerless "
    "gloves; she does NOT wear trousers; she is NOT a second version of the boy and NOT the same "
    "height as him. If the panel could be read as two blond children, it is wrong. The PANEL 1 "
    "balloon \"I DON'T KNOW HOW.\" is the BOY'S: its tail must reach HIS mouth and stop there — "
    "never end in the empty space between the two figures, and never touch the woman. ",
  R("naruto_13", "kushina", "env_inner_sewer"),
  "low"),

 # ---- Spread 6: remain yourself ---------------------------------------------------------
 ("p11", dict(scene="dialogue", light="dark", cast="two", mood="somber", panels=5),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_11 + ONLY(BOY13, KUSHINA_SPEAKER) +
  "FIVE panels. She refuses to let her request become an order. Her fading has now reached part of "
  "one forearm; her face, hair and dress remain solid.\n"
  "PANEL 1 (wide upper tier, full width): two-shot — she draws back far enough to watch his smile "
  "fade naturally and raises one cautioning finger between them. He watches the finger, then meets "
  "her eye.\n"
  "PANEL 2 (middle-right two-shot): she lowers the finger and opens the hand instead, refusing any "
  "commanding posture.\n"
  "PANEL 3 (dominant middle-left, the focal panel): close shot — her open palm settles over his "
  "heart and his hand covers it. No balloon may cover that chest touch.\n"
  "PANEL 4 (lower-right): close two-shot — her eye-line is unwavering. More of her forearm has "
  "turned to seal light, but the hand beneath his stays solid.\n"
  "PANEL 5 (lower-left close-up): he nods once. The smile is gone, but the warmth has not left his "
  "eyes. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "BUT DON'T TURN THIS INTO ANOTHER ORDER."),
        (1, BOY13, "below and left of the first balloon", "YOU ASKED ME TO."),
        (2, KUSHINA_SPEAKER, "upper right", "I ASKED YOU TO LIVE. NOT TO PERFORM HAPPINESS FOR ME."),
        (3, KUSHINA_SPEAKER, "upper right", "REMAIN YOURSELF."),
        (4, KUSHINA_SPEAKER, "upper right", "IF YOU BECOME SOMEONE ELSE FOR ME, YOU WILL NEVER BE HAPPY."),
        (5, BOY13, "upper right", "I CAN TRY.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 ("p12", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_12 + ONLY(BOY13, KUSHINA_SPEAKER,
         "an indistinct pale blond reflection lying in the water in panel 6 which NEVER becomes a "
         "person — no face, no features, no body, no cloak detail; it never moves and never "
         "speaks") +
  "SIX panels. She separates understanding from forgiveness and does not argue with his answer.\n"
  "PANEL 1 (upper-right): medium two-shot — her gaze drops. He recognises the shift and waits.\n"
  "PANEL 2 (upper-left close-up): his face closes slightly BEFORE she speaks the name. His eye-line "
  "stays on her.\n"
  "PANEL 3 (dominant middle band, the focal panel): wide two-shot — she sits at SCREEN-RIGHT, "
  "upright with both hands open on her knees. He sits at SCREEN-LEFT and is no longer touching her. "
  "The gap of empty water between them is deliberate and clean.\n"
  "PANEL 4 (lower-right close-up): his jaw sets.\n"
  "PANEL 5 (lower-centre close-up): she accepts the answer with one small nod — no flinch, no "
  "correction.\n"
  "PANEL 6 (lower-left): she looks down into the water. Only a blurred, unreadable pale blond "
  "reflection appears there: it has no face and no features, it is not a man standing anywhere in "
  "the panel, and it never speaks. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "THERE IS ONE MORE THING."),
        (2, BOY13, "upper right", "MINATO."),
        (3, KUSHINA_SPEAKER, "upper right, over the gap between them", "I CANNOT ASK YOU TO FORGIVE HIM."),
        (4, BOY13, "upper right", "I WILL NOT."),
        (5, KUSHINA_SPEAKER, "upper right", "I KNOW."),
        (6, KUSHINA_SPEAKER, "upper right", "BUT HE WAS KIND. TOO TRUSTING. SOMETIMES AN IDIOT.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 # ---- Spread 7: love without conditions --------------------------------------------------
 ("p13", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_13 + ONLY(BOY13, KUSHINA_SPEAKER,
         "an indistinct pale blond reflection lying in the water in panels 1 and 3 which NEVER "
         "becomes a person — no face, no features, no body; it never moves and never speaks") +
  "SIX panels. His anger survives intact and neither of them wins.\n"
  "PANEL 1 (upper-right): medium shot — he looks at the indistinct blond reflection in the water "
  "but NOT toward her.\n"
  "PANEL 2 (upper-left close-up): she does not look away.\n"
  "PANEL 3 (middle-right): close shot — the reflection breaks into ripples under her fingertips and "
  "is gone.\n"
  "PANEL 4 (middle-left close-up): he turns back to her, anger contained rather than absent.\n"
  "PANEL 5 (dominant lower-right, the focal panel): close two-shot — she reaches across the gap and "
  "takes his hand again, meeting his eye at exactly equal height.\n"
  "PANEL 6 (lower-left two-shot): he allows the contact but offers no forgiveness. Her LOWER BODY "
  "is now mostly red-gold script; her face, hair and upper body remain solid. " + L_SEAL
  + SAY((1, BOY13, "upper right", "KINDNESS DID NOT SAVE ME."),
        (2, KUSHINA_SPEAKER, "upper right", "NO."),
        (3, KUSHINA_SPEAKER, "upper right", "IF HE HAD SEEN A BETTER WAY, HE WOULD HAVE TAKEN IT."),
        (4, BOY13, "upper right", "HE DIDN'T."),
        (5, KUSHINA_SPEAKER, "upper right", "NO. AND YOU PAID FOR THAT."),
        (6, KUSHINA_SPEAKER, "upper right", "UNDERSTAND HIM IF YOU CAN. I WON'T ASK MORE.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "low"),

 ("p14", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N13.format(i=1) + KUSHINA.format(i=2) + ENV_SEAL.format(i=3) + DREAM + BOYSTATE
  + FADE_14 + ONLY(BOY13, KUSHINA_SPEAKER) +
  "SIX panels. THE CHAPTER'S EMOTIONAL FOCAL PAGE — the encounter ends on the loss he keeps "
  "dreaming. Her balloons stay ORDINARY white speech balloons with clean black outlines: they never "
  "become wavy, ghostly, broken or faded, because this really happened. No balloon may cover her "
  "hands, his tears, or the dissolving edges of her body.\n"
  "PANEL 1 (upper-right): close-up on their joined hands — hers has become translucent inside his. "
  "He closes both hands around it and light escapes between his fingers. Her face is still in "
  "frame at the top so the tail has a mouth to reach.\n"
  "PANEL 2 (upper-left close two-shot): she uses her fading free hand to touch the same point over "
  "his heart. His eyes stay fixed on hers.\n"
  "PANEL 3 (middle-right): close shot — her FACE remains solid while her body breaks into "
  "seal-script from the edges inward. He leans forward, trying to keep their foreheads together.\n"
  "PANEL 4 (dominant middle-left, the focal panel): she is mostly red-gold light now, her very long "
  "red hair and smiling face still clearly recognisable. He reaches from SCREEN-LEFT and his hand "
  "passes INTO the light without meeting anything. The balloon sits in clear dark space so nothing "
  "of her is covered.\n"
  "PANEL 5 (lower-right): only her eyes, her smile and one hand remain for one last beat, floating "
  "in seal light.\n"
  "PANEL 6 (lower-left): the seal-space is empty except for the boy on both knees, one hand still "
  "suspended in the air where her face was. The last red strand vanishes just beyond his fingers. "
  "His mouth shapes a word but no sound comes: there is NO balloon, NO caption and NO text of any "
  "kind in this panel. " + L_SEAL
  + SAY((1, KUSHINA_SPEAKER, "upper right", "WHATEVER PATH YOU CHOOSE, I WILL NEVER BE ASHAMED OF YOU."),
        (2, KUSHINA_SPEAKER, "upper right", "DON'T FORGET WHO YOU ARE."),
        (3, KUSHINA_SPEAKER, "upper right", "BE WHAT YOUR HEART TELLS YOU TO BE."),
        (4, KUSHINA_SPEAKER, "upper right, in clear dark space", "I LOVE YOU. I ALWAYS WILL."),
        (5, KUSHINA_SPEAKER, "upper right", "THANK YOU FOR LETTING ME BE YOUR MOTHER.")),
  R("naruto_13", "minato_kushina", "env_inner_sewer"),
  "high"),

 # ---- Spread 8: still midnight -----------------------------------------------------------
 ("p15", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + ZET.format(i=2) + GUNBAI_V4.format(i=3)
  + ENV_CAMP.format(i=4) + ZOR + WAKE
  + ONLY(BOY16, ZETSU) +
  "SIX panels. HARD CUT OUT OF THE DREAM. This page is the PHYSICAL WORLD: dry dark earth, real "
  "trees, cold blue moonlight, hard black shadows — there is NO water, NO seal script, NO red-gold "
  "light and NO red-haired woman anywhere on this page. The change of reality must be immediate and "
  "carries no caption.\n"
  "PANEL 1 (narrow upper-right): extreme close-up of the older blond teen's eye snapping open in "
  "hard blue moonlight. A small intake of breath is visible in his face but carries NO sound effect "
  "and no text.\n"
  "PANEL 2 (dominant upper-left, the focal panel): medium shot — he bolts upright on the dark "
  "travel blanket, long blond hair stuck to his sweating face. He wears only the black high-neck "
  "under-layer. His folded repaired red armour lies at SCREEN-LEFT with the plain straight sash "
  "sword and the dark purple gunbai resting separately behind it, both fully visible and not "
  "overlapping. Cold dry earth replaces the dream's water.\n"
  "PANEL 3 (middle-right close-up): he presses his palm flat to the place over his heart. His "
  "fingers tremble once. No text in this panel.\n"
  "PANEL 4 (middle-left): two-shot — the plant creature is half-emerged from a tree at SCREEN-RIGHT, "
  "keeping its distance and giving him space. He sits at SCREEN-LEFT and looks down rather than "
  "meeting its eyes.\n"
  "PANEL 5 (lower-right close-up): he wipes the sweat from his jaw and restores his controlled, "
  "impassive expression. He does NOT smile anywhere on this page.\n"
  "PANEL 6 (lower-left): medium shot — the plant creature glances up through the branches at a moon "
  "still near its zenith. " + L_CAMP
  + SAY((4, ZETSU, "upper right", "THE SAME DREAM?"),
        (5, BOY16, "upper right", "YES."),
        (5, BOY16, "directly below the first balloon, sharing the same tail target", "WHAT TIME IS IT?"),
        (6, ZETSU, "upper right", "STILL MIDNIGHT.")),
  R("naruto_v4_black", "zetsu", "gunbai_v4", "env_wave_forest"),
  "medium"),

 ("p16", dict(scene="establishing", light="dark", cast="two", mood="somber", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + N16_SWORD.format(i=2) + ZET.format(i=3)
  + GUNBAI_V4.format(i=4) + ENV_CAMP.format(i=5) + ZOR + WAKE
  + ONLY(BOY16, ZETSU) +
  "SIX panels. LAST PAGE OF THE CHAPTER. Sleep is impossible, so the journey resumes — nothing has "
  "been resolved. This page is the PHYSICAL WORLD: dry earth, real trees, cold moonlight, no water "
  "and no seal light anywhere.\n"
  "IMAGES 1 AND 2 ARE THE SAME PERSON in two states of dress: use Image 1's black under-layer state "
  "in PANELS 1-3, and Image 2's fully armoured state with the sash sword in PANELS 4-6. Never mix "
  "them inside one panel.\n"
  "PANEL 1 (upper-right, wide): high shot — he lies back down on the blanket with both hands at his "
  "sides, rigid rather than resting, eyes closed. His armour and weapons stay within reach at "
  "SCREEN-LEFT in the same arrangement as before. No text in this panel.\n"
  "PANEL 2 (upper-left, narrow close-up): his eyes are open again in the dark. The pupil is an "
  "ordinary blue eye — NO Sharingan, NO comma marks and NO six-bladed pattern. No text in this "
  "panel.\n"
  "PANEL 3 (middle-right): medium shot — he sits up and reaches for the first red armour plate. The "
  "plant creature turns away from its tree toward the road.\n"
  "PANEL 4 (middle-left): close shot — now wearing the red armour, he tightens an armour cord with "
  "one precise pull, his face returned to its usual impassive set.\n"
  "PANEL 5 (lower-right): medium shot — he straps the plain straight sword at his sash and lifts "
  "the dark purple gunbai onto his back. His gaze is on the route ahead, not on the creature.\n"
  "PANEL 6 (dominant lower-left panel, the focal panel): long exterior — under a deep-midnight sky "
  "with the moon still high, the armoured teen walks SCREEN-LEFT along the road with the plant "
  "creature moving beside and slightly behind him. He is upright and NOT smiling. His forward hand "
  "hangs relaxed rather than clenched — the only visible residue of the encounter. No text in this "
  "panel. " + L_CAMP
  + SAY((3, ZETSU, "upper right", "PERHAPS WE SHOULD CONTINUE."),
        (4, BOY16, "upper right", "THAT SOUNDS GOOD."),
        (5, BOY16, "upper right", "I DON'T THINK I CAN SLEEP AGAIN TONIGHT.")),
  R("naruto_v4_black", "naruto_v4_armor_sword", "zetsu", "gunbai_v4", "env_wave_forest"),
  "medium"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch06" / "raw", HERE / "v5ch06" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
