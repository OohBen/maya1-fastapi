"""Volume 2, Chapter 1 — "Shall We Dance?"  The bell test. 22 pages.

Everything Volume 1 taught is applied here:
  - model-drawn dialogue (given verbatim per panel) — see PIPELINE.md reversal
  - genlib.STAGING (depth stagger, panels fill the page, opaque effects, crop for emotion)
  - auto-selected style reference per page via refs/style_select.py
  - 1152x2048 (free resolution bump over 1024x1536 at the same tier)

Dialogue is LOCKED. The model draws it, so a wrong line costs a full page re-render.
"""
import concurrent.futures as cf
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "refs"))
from genlib import STAGING, STYLE, STYLE_REF, UNIQUE, rep_generate, Ledger  # noqa: E402
import style_select as ss                                                    # noqa: E402

REFS = HERE.parent / "refs" / "images"
OUT = HERE / "v2ch01" / "raw"
LED = Ledger(HERE / "v2ch01" / "ledger.json")
R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

FILL = ("A single complete manga PAGE, portrait. The block of panels FILLS THE WHOLE PAGE out to a "
        "narrow even margin, separated only by thin white gutters — no broad empty white areas. ")

# --- character bindings -------------------------------------------------------
N13 = ("Image {i} is the CHARACTER REFERENCE for the blond boy: a lean thirteen-year-old whose hair is LONG — it hangs well past his jaw and reaches his shoulders in heavy strands, with two thick bangs framing his face and the right bang hanging low enough to cover his right eye. His hair is never short and never spiky. Blue eyes, "
       "whisker marks nearly faded, blank expression, black long-sleeved shirt with a large red "
       "spiral on the chest, black trousers, dark sandals, black fingerless gloves with small red "
       "spirals. Reproduce exactly; ignore its white background and three-view layout. " + UNIQUE + " ")
KAK = ("Image {i} is the CHARACTER REFERENCE for the masked man: tall and lean, spiky silver-grey "
       "hair swept to one side, dark cloth mask covering his face below the nose, slanted forehead "
       "protector covering his left eye so only his right eye shows, dark navy uniform under a green "
       "flak vest. Reproduce exactly; ignore its white background and layout. ")
SAS = ("Image {i} is the CHARACTER REFERENCE for the black-haired boy: upward-spiking black hair with "
       "two long bangs, dark eyes, high-collared dark navy shirt, white shorts, white arm warmers. "
       "Reproduce exactly; ignore its white background and layout. ")
SAK = ("Image {i} is the CHARACTER REFERENCE for the pink-haired girl: chin-length pink hair, wide "
       "forehead, green eyes, red sleeveless qipao dress with white trim over dark shorts. "
       "Reproduce exactly; ignore its white background and layout. ")
ZET = ("Image {i} is the CREATURE REFERENCE: a humanoid plant creature split vertically, right half "
       "chalk white and left half pure black, round yellow pupil-less eyes, black cloak, green "
       "venus-flytrap shell around its head. Reproduce exactly; ignore its white background. ")
ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and lighting. "
       "Do not copy its camera angle; ignore that it is empty of people. ")

L_DAWN = "Lighting: cold pale dawn, long low shadows, mist between the trees. "
L_DAY = "Lighting: flat clear morning daylight. "

def SAY(*lines):
    """Model-drawn lettering with EXPLICIT speaker attribution.

    Each entry is (panel_no, speaker_description, where_in_panel, text). Naming the
    speaker and pinning the balloon's position is the only reliable way to stop the
    tail pointing at the wrong character — the recurring defect in review.
    """
    out = ("LETTERING: draw the speech balloons WITH their dialogue written inside, in clean bold "
           "upright English comic lettering, all capitals, correctly spelled. Each balloon must sit "
           "in the position given and its TAIL MUST POINT DIRECTLY AT THE NAMED SPEAKER, clear of "
           "every face. A balloon must never sit nearer to, or point at, anyone other than its "
           "speaker. Use exactly these, and nothing else:\n")
    for panel, speaker, where, text in lines:
        out += (f'  PANEL {panel} — balloon in the {where}, tail pointing at {speaker}, '
                f'reading: "{text}"\n')
    out += "Do not write any other text anywhere on the page. "
    return out


STYLE_Q = dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6)

# --------------------------------------------------------------------- pages
PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="none", mood="calm", panels=1),
  "A single full-page illustration, no panel divisions, art running to all four page edges. "
  + ENV.format(i=1) +
  "Training ground seven at dawn: three weathered upright wooden posts standing in open grass, "
  "treeline behind, mist low across the ground, the sky pale and empty. No people anywhere. Keep "
  "the upper third as calm open sky for a title to be placed later. " + L_DAWN,
  R("env_training_ground_7"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=5),
  FILL + N13.format(i=1) + ZET.format(i=2) + ENV.format(i=3) +
  "FIVE panels, uneven, columns not aligned.\n"
  "PANEL 1 (dominant, top): a low angle up into a tree — the blond boy sits along a high branch, "
  "one knee up, small in the frame against a pale dawn sky, the three wooden posts tiny far below. "
  "PANEL 2 (small): the trunk beside him, where a plant creature's head has silently emerged from "
  "the bark, only the head, at the very edge of frame.\n"
  "PANEL 3 (small): the boy's face in profile, not turning to look at it.\n"
  "PANEL 4 (narrow letterbox): the creature's yellow eyes, cropped by all four edges, flat black "
  "behind them.\n"
  "PANEL 5 (wide, bottom): the empty training ground from the boy's height in the tree — the posts, "
  "the mist, nobody there yet. " + L_DAWN
  + SAY((1, ["DO YOU HAVE SOMETHING TO TELL ME?"]),
        (2, ["NO."]),
        (3, ["THEN YOU WERE BORED.", "YOU DON'T HAVE MADARA TO TALK TO ANY MORE."]),
        (4, ["WHICH OF YOUR SKILLS WILL YOU SHOW THEM TODAY?"]),
        (5, ["TAIJUTSU. NOTHING ELSE."])),
  R("naruto_13", "zetsu", "env_training_ground_7"), "medium"),

 ("p03", dict(scene="dialogue", light="day", cast="two", mood="comedic", panels=6),
  FILL + SAS.format(i=1) + SAK.format(i=2) + ENV.format(i=3) +
  "SIX panels, uneven.\n"
  "PANEL 1 (wide, top): the black-haired boy and the pink-haired girl arrive at the posts, seen "
  "from high above and behind so they are small; the empty ground dominates.\n"
  "PANEL 2 (small): the girl leaning in toward him, delighted; he is cropped by the panel edge and "
  "already turning away. Flat white background, no scenery.\n"
  "PANEL 3 (small): his face only, bored, three-quarters away from camera.\n"
  "PANEL 4 (small): the sun a little higher over the treeline. No characters.\n"
  "PANEL 5 (small): the girl sitting on the ground now, chin on her hands, wilting. Flat tone "
  "background.\n"
  "PANEL 6 (wide, bottom): the sun higher again; the two of them tiny at the bottom of the frame, "
  "the empty sky taking three quarters of the panel. " + L_DAY
  + SAY((2, ["SASUKE-KUN! WE'RE THE FIRST ONES HERE!"]),
        (3, ["HN."]),
        (5, ["...HE'S LATE AGAIN."])),
  R("sasuke", "sakura", "env_training_ground_7"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + N13.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blond boy's sandals landing in the grass, no face in frame.\n"
  "PANEL 2 (dominant, upper): he walks away from camera toward the treeline, back to us, the other "
  "two small in the mid distance behind him at very different scale, the girl half-risen. Nobody "
  "faces the camera.\n"
  "PANEL 3 (small): the girl's face, outraged, cropped tight, flat tone behind.\n"
  "PANEL 4 (small): the black-haired boy half-turned, watching him go.\n"
  "PANEL 5 (narrow letterbox): only the blond boy's visible eye, cropped by all four edges.\n"
  "PANEL 6 (wide, bottom): the empty treeline he has walked into; the other two left tiny at the "
  "far edge of frame. " + L_DAY
  + SAY((3, ["WHERE ARE YOU GOING?! WE HAVE A TEST!"]),
        (4, ["...DOBE."]),
        (5, ["I AM AWARE OF THE TEST."]),
        (6, ["I DON'T HAVE THE PATIENCE FOR OUR SENSEI'S TARDINESS.",
             "TELL HIM I'LL BE AT MY APARTMENT. IF HE IS SERIOUS, HE WILL COME AND FETCH ME."])),
  R("naruto_13", "sasuke", "sakura", "env_training_ground_7"), "medium"),

 ("p05", dict(scene="comedy", light="day", cast="small_group", mood="comedic", panels=5),
  FILL + KAK.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (dominant, top): the masked silver-haired man has appeared at the posts in a swirl of "
  "leaves, one hand raised in a lazy greeting, an orange book in the other. He is huge in the "
  "foreground cropped by the right edge; the two children are small and far away to the left. "
  "PANEL 2 (small): the pink-haired girl mid-shout, mouth enormous, cropped by the panel edge, flat "
  "white background with radiating speed lines behind her.\n"
  "PANEL 3 (small): the man's single visible eye, unbothered.\n"
  "PANEL 4 (small): the black-haired boy, arms folded, looking off-panel.\n"
  "PANEL 5 (wide, bottom): the empty grass where a third child should be standing — just the three "
  "posts and a gap. " + L_DAY
  + SAY((1, ["YO. SORRY — A BLACK CAT CROSSED MY PATH."]),
        (2, ["YOU'RE LATE!!"]),
        (3, ["...WHERE IS NARUTO?"]),
        (4, ["HE LEFT. AN HOUR AGO."]),
        (5, ["...I'LL BE BACK IN TEN MINUTES."])),
  R("kakashi", "sasuke", "sakura", "env_training_ground_7"), "low"),
 ("p06", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=5),
  FILL + N13.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (dominant, top): the interior of a small apartment, almost entirely bare — sealed boxes "
  "stacked against one wall, no furniture, one window. The masked man stands just inside the door, "
  "huge in the foreground and cropped by the left edge, only his shoulder and the back of his head "
  "visible. The blond boy is small and far away across the empty room.\n"
  "PANEL 2 (small): the man's single visible eye, narrowed, taking in the room.\n"
  "PANEL 3 (small): a stack of sealed boxes and a rolled mattress. No people.\n"
  "PANEL 4 (small): the boy's face, entirely neutral, flat tone behind him.\n"
  "PANEL 5 (wide, bottom): the two of them at opposite ends of the bare room, the empty floor "
  "occupying most of the panel. " + L_DAY
  + SAY((1, ["YOU'RE MOVING OUT?"]),
        (4, ["THIS PLACE IS FALLING APART. IT IS NOT SUITABLE FOR A SHINOBI."]),
        (5, ["...WHERE WILL YOU LIVE?", "THE SHINOBI DISTRICT."])),
  R("naruto_13", "kakashi", "env_apartment_int"), "low"),

 ("p07", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + KAK.format(i=1) + N13.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + ENV.format(i=5) +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the masked man stands at the three posts holding up TWO small silver "
  "bells on strings. He is large on the right, cropped by the edge; the three children are staggered "
  "at three clearly different depths to the left, none facing camera squarely.\n"
  "PANEL 2 (small): a tight shot of the two bells hanging, catching the light. No faces.\n"
  "PANEL 3 (small): the pink-haired girl counting on her fingers, alarmed. Flat tone background.\n"
  "PANEL 4 (small): the black-haired boy, eyes narrowing.\n"
  "PANEL 5 (small): the blond boy, expression unchanged, uninterested.\n"
  "PANEL 6 (wide, bottom): the man tucking the bells into his belt, an alarm clock set down on a "
  "post beside him. " + L_DAY
  + SAY((1, ["YOUR TASK IS TO TAKE A BELL FROM ME BEFORE NOON."]),
        (3, ["BUT SENSEI — THERE ARE ONLY TWO BELLS!"]),
        (6, ["THEN ONE OF YOU GOES BACK TO THE ACADEMY.",
             "COME AT ME WITH THE INTENT TO KILL. BEGIN."])),
  R("kakashi", "naruto_13", "sasuke", "sakura", "env_training_ground_7"), "medium"),

 ("p08", dict(scene="action", light="day", cast="small_group", mood="tense", panels=5),
  FILL + ENV.format(i=1) +
  "FIVE panels, uneven. No dialogue anywhere on this page.\n"
  "PANEL 1 (wide, top): the empty clearing, three figures already gone, only dust settling. "
  "PANEL 2 (small): a branch shaking, leaves falling, no character visible.\n"
  "PANEL 3 (small): sunlight through the canopy, dappled leaves, nothing else.\n"
  "PANEL 4 (small): a training shuriken lodged in bark, object only.\n"
  "PANEL 5 (dominant, bottom): the masked man alone in the middle of the clearing, small and "
  "centred, calmly opening an orange book. The empty ground and treeline take most of the panel. "
  + L_DAY, R("env_training_ground_7"), "low"),

 ("p09", dict(scene="emotional_closeup", light="day", cast="two", mood="tense", panels=6),
  FILL + SAK.format(i=1) + SAS.format(i=2) +
  "SIX panels, uneven. A genjutsu sequence — the backgrounds go abstract.\n"
  "PANEL 1 (small): the pink-haired girl crouched in undergrowth, looking around.\n"
  "PANEL 2 (small): her eyes unfocusing, pupils shrinking. Flat white background.\n"
  "PANEL 3 (dominant, middle): the black-haired boy staggering toward her out of a swirling void, "
  "battered and pierced with weapons, reaching for her. The background is nothing but radiating "
  "black speed lines. Drawn flat and graphic, not glowing.\n"
  "PANEL 4 (small): her face, absolute horror, mouth open, cropped by all four edges.\n"
  "PANEL 5 (narrow letterbox): pure flat black, empty.\n"
  "PANEL 6 (wide, bottom): the girl collapsed unconscious in the grass, seen from high above, tiny "
  "in the frame. " + L_DAY
  + SAY((3, ["S-SAKURA... HELP..."]),
        (4, ["SASUKE-KUUUN!!"]))
  + "Draw one large hand-drawn manga sound effect in PANEL 6, a heavy 'THUD' shape, overlapping the "
    "panel edge. ",
  R("sakura", "sasuke"), "medium"),

 ("p10", dict(scene="action", light="day", cast="two", mood="violent", panels=7),
  FILL + SAS.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "SEVEN panels, uneven, fast cutting.\n"
  "PANEL 1 (small): the black-haired boy launching forward, one limb cropped by the panel edge.\n"
  "PANEL 2 (small): a fist stopped by an open palm, hands only, flat white background.\n"
  "PANEL 3 (small): a knee driving up, blocked by a forearm, no faces.\n"
  "PANEL 4 (dominant, middle): a wide low shot of the exchange — the boy mid-spin, the masked man "
  "leaning back out of range while still holding his book, both figures cropped by panel edges, "
  "background reduced to flat horizontal speed lines.\n"
  "PANEL 5 (small): the man's visible eye, mildly surprised.\n"
  "PANEL 6 (small): the boy's fingertips brushing the bells at the man's belt — hands and belt only.\n"
  "PANEL 7 (wide, bottom): the man leaping back, the boy landing in a crouch, wide gap between them. "
  + L_DAY
  + "Draw hand-drawn manga sound effects integrated into the art: a sharp 'PAK' in PANEL 2 and a "
    "heavy 'DON' across PANEL 4, overlapping the figures and cropped by the panel edges. ",
  R("sasuke", "kakashi", "env_training_ground_7"), "medium"),

 ("p11", dict(scene="action", light="day", cast="two", mood="violent", panels=5),
  FILL + SAS.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the black-haired boy's hands snapping through seals, hands only, cropped tight.\n"
  "PANEL 2 (small): his cheeks filling with air, eyes hard.\n"
  "PANEL 3 (dominant, middle, tall): an enormous ball of fire erupting from his mouth toward camera. "
  "Draw the fire as FLAT OPAQUE overlapping tongues with hard black outlines and layered flat "
  "orange, red and yellow shapes — it must not glow or wash anything out, and the trees, the ground "
  "and the boy stay fully drawn and legible.\n"
  "PANEL 4 (small): where the man was standing there is now a scorched split log. No people.\n"
  "PANEL 5 (wide, bottom): the boy alone in the smoke, turning sharply, realising. " + L_DAY
  + SAY((2, ["FIRE STYLE!"]),
        (5, ["...A SUBSTITUTION."]))
  + "Draw a large hand-drawn manga sound effect across PANEL 3, a roaring 'GOOO' shape angled with "
    "the blast, overlapping the flames and cropped by the panel edge. ",
  R("sasuke", "kakashi", "env_training_ground_7"), "medium"),

 ("p12", dict(scene="comedy", light="day", cast="two", mood="comedic", panels=6),
  FILL + SAS.format(i=1) + KAK.format(i=2) + SAK.format(i=3) + ENV.format(i=4) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): two hands bursting up out of the earth and seizing a pair of ankles.\n"
  "PANEL 2 (dominant, middle): the black-haired boy buried to his neck in the ground, only his head "
  "above the soil, glaring. The masked man crouches beside him hugely in the foreground, cropped by "
  "the right edge, reading his book.\n"
  "PANEL 3 (small): the boy's face, furious, cropped tight, flat tone background.\n"
  "PANEL 4 (small): the pink-haired girl arriving at a run, seen from behind.\n"
  "PANEL 5 (small): her face going white.\n"
  "PANEL 6 (wide, bottom): her tugging uselessly at the buried head while the man walks away out of "
  "frame. " + L_DAY
  + SAY((2, ["GET ME OUT OF HERE."]),
        (3, ["NO."]),
        (5, ["SASUKE-KUUUN!!"])),
  R("sasuke", "kakashi", "sakura", "env_training_ground_7"), "low"),

 ("p13", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): sandals dropping into frame from above, landing in grass.\n"
  "PANEL 2 (small): the masked man's eye flicking sideways.\n"
  "PANEL 3 (dominant, middle): the blond boy walking unhurried into the clearing, small and low in "
  "the frame; the man stands large in the foreground with his back to camera, cropped by the bottom "
  "edge. The buried head and the girl are tiny in the far background.\n"
  "PANEL 4 (small): the boy settling into a taijutsu stance, weight low, body twisted on a diagonal, "
  "one arm cropped by the panel edge. Flat tone background.\n"
  "PANEL 5 (wide, bottom): a wide two-shot, the gap of empty ground between them dominating. " + L_DAY
  + SAY((5, ["SHALL WE DANCE, KAKASHI-SENSEI?"])),
  R("naruto_13", "kakashi", "env_training_ground_7"), "high"),

 ("p14", dict(scene="action", light="day", cast="two", mood="violent", panels=7),
  FILL + N13.format(i=1) + KAK.format(i=2) +
  "SEVEN panels, uneven, very fast cutting. Backgrounds are mostly abstract.\n"
  "PANEL 1 (small): the blond boy simply gone — empty grass where he stood, a scuff of torn turf.\n"
  "PANEL 2 (small): the masked man's single eye blowing wide open.\n"
  "PANEL 3 (dominant, middle): the boy already inside his guard, fist driving in, the man's forearm "
  "barely intercepting. Both cropped by panel edges. Background is nothing but radiating white "
  "speed lines.\n"
  "PANEL 4 (small): the orange book spinning out of the man's hand, book only.\n"
  "PANEL 5 (small): boots skidding backward, gouging two furrows in the dirt, no faces.\n"
  "PANEL 6 (small): the boy's visible eye, cold, faintly alight. Flat black behind it.\n"
  "PANEL 7 (wide, bottom): the two of them apart again, the man's stance now serious, book gone. "
  + L_DAY
  + SAY((7, ["THIS DANCE SHOULD BE ENTERTAINING."]))
  + "Draw hand-drawn manga sound effects: a huge 'DOSU' across PANEL 3 overlapping both figures and "
    "cropped by the edge, and a smaller 'ZAA' in PANEL 5. ",
  R("naruto_13", "kakashi"), "high"),

 ("p15", dict(scene="action", light="day", cast="two", mood="violent", panels=6),
  FILL + N13.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a foot arcing toward a head, blocked by a crossed forearm, limbs only.\n"
  "PANEL 2 (small): the boy airborne above the treeline, small against open sky.\n"
  "PANEL 3 (dominant, middle): the masked man slammed down into the earth from above — a shallow "
  "crater of flat cracked plates radiating outward, dust drawn as flat opaque shapes with hard "
  "outlines, the boy already pushing off and away. The ground stays fully visible through the dust.\n"
  "PANEL 4 (small): the man's hand flat on the crater floor, pushing himself up.\n"
  "PANEL 5 (small): the boy landing lightly, back to camera.\n"
  "PANEL 6 (wide, bottom): the man upright again, one eye fixed on the boy, genuinely assessing him "
  "for the first time. " + L_DAY
  + SAY((6, ["...YOU ARE FAR BETTER THAN I WAS TOLD."]))
  + "Draw a huge hand-drawn manga sound effect across PANEL 3, a heavy 'ZUUN' impact shape crossing "
    "the gutter into PANEL 4. ",
  R("naruto_13", "kakashi", "env_training_ground_7"), "medium"),

 ("p16", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + KAK.format(i=1) + N13.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + ENV.format(i=5) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the alarm clock on the post, hammer rattling. Object only, no people.\n"
  "PANEL 2 (small): the masked man straightening out of his stance, disappointed.\n"
  "PANEL 3 (dominant, middle): the three children lined up unevenly at very different depths in "
  "front of him — the girl nearest and cropped by the frame, the black-haired boy mid-ground and "
  "dishevelled, the blond boy furthest and unmarked. The man is a large dark shape in the "
  "foreground with his back to camera.\n"
  "PANEL 4 (small): the black-haired boy's dirt-covered face.\n"
  "PANEL 5 (small): the blond boy's hand rising, holding TWO small silver bells on strings.\n"
  "PANEL 6 (wide, bottom): the man's eye, wide open, staring at his own empty belt. " + L_DAY
  + SAY((2, ["TIME'S UP. NONE OF YOU TOOK A BELL — YOU FAIL."]),
        (6, ["...WHEN DID YOU TAKE THOSE?"])),
  R("kakashi", "naruto_13", "sasuke", "sakura", "env_training_ground_7"), "medium"),

 ("p17", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + N13.format(i=1) + KAK.format(i=2) + SAK.format(i=3) + ENV.format(i=4) +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the blond boy in the near foreground turned three-quarters away, the "
  "bells hanging from his fingers; the masked man small and still in the mid distance; the other two "
  "tiny behind him. Three clear depths.\n"
  "PANEL 2 (small): a flashback fragment drawn flat and pale — a fist connecting, a hand closing on "
  "a belt at the same instant. Bleached background, no detail.\n"
  "PANEL 3 (small): the man's eye, understanding.\n"
  "PANEL 4 (small): the pink-haired girl looking between them, lost.\n"
  "PANEL 5 (small): the blond boy's face, flat and unimpressed.\n"
  "PANEL 6 (wide, bottom): all four in the clearing, the empty ground taking half the panel. "
  + L_DAY
  + SAY((1, ["WHEN I PUT YOU IN THE GROUND."]),
        (3, ["YOU WERE SO BUSY MEASURING ME THAT YOU FORGOT YOUR OWN TEST."]),
        (5, ["THE BELLS WERE NEVER THE POINT. THREE GENIN CANNOT BEAT A JONIN.",
             "THE TEST WAS TEAMWORK."])),
  R("naruto_13", "kakashi", "sakura", "env_training_ground_7"), "medium"),

 ("p18", dict(scene="dialogue", light="day", cast="small_group", mood="somber", panels=6),
  FILL + KAK.format(i=1) + N13.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + ENV.format(i=5) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the masked man's eye, thoughtful.\n"
  "PANEL 2 (small): the pink-haired girl looking down and away, ashamed. Flat tone background.\n"
  "PANEL 3 (small): the black-haired boy staring at the ground, jaw set.\n"
  "PANEL 4 (dominant, middle): the blond boy tossing the two bells back underhand; they hang in the "
  "air mid-panel; the man's hand rising to catch them. The two of them at very different scale, the "
  "boy already half-turned away.\n"
  "PANEL 5 (small): the bells landing in the man's palm.\n"
  "PANEL 6 (wide, bottom): the boy walking away toward the treeline, the other three left standing. "
  + L_DAY
  + SAY((1, ["THEN WHY DIDN'T YOU WORK WITH THEM?"]),
        (4, ["NEITHER OF THEM WOULD HAVE ACCEPTED HELP FROM ME."]),
        (6, ["...YOU PASS. ALL THREE OF YOU."])),
  R("kakashi", "naruto_13", "sasuke", "sakura", "env_training_ground_7"), "medium"),

 ("p19", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + KAK.format(i=2) + ENV.format(i=3) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (wide, top): the other two children already small and distant, walking away; the man and "
  "the blond boy left alone at opposite sides of the empty clearing.\n"
  "PANEL 2 (small): the man's eye, no longer lazy at all.\n"
  "PANEL 3 (small): the boy in profile, not looking at him.\n"
  "PANEL 4 (narrow letterbox): only the boy's visible eye, cropped by all four edges, flat black.\n"
  "PANEL 5 (dominant, bottom): a wide low shot of the two of them, the three posts between them, "
  "the sky taking the upper half of the panel. " + L_DAY
  + SAY((2, ["NOT YOU. WE'RE GOING TO SEE THE HOKAGE."]),
        (5, ["I ASSUMED WE WOULD BE."])),
  R("naruto_13", "kakashi", "env_training_ground_7"), "medium"),

 ("p20", dict(scene="establishing", light="day", cast="none", mood="somber", panels=4),
  FILL + ENV.format(i=1) +
  "FOUR panels, uneven. No characters and no dialogue anywhere on this page.\n"
  "PANEL 1 (small): the two bells lying in the grass where they were dropped.\n"
  "PANEL 2 (small): the alarm clock, stopped, on the wooden post.\n"
  "PANEL 3 (small): the shallow crater in the dirt, cracked plates radiating out.\n"
  "PANEL 4 (dominant, bottom): the empty training ground from far away and high up, the three posts "
  "small, the treeline dark, nobody in it. " + L_DAY,
  R("env_training_ground_7"), "low"),
]


def build_one(spec):
    pid, want, desc, refs, quality = spec
    dest = OUT / f"{pid}.png"
    if dest.exists():
        return f"[skip] {pid}"
    idx = len(refs) + 1
    prompt = desc + " " + STAGING + STYLE_REF.format(i=idx) + STYLE
    # Style reference images can themselves trip content moderation (a violent library
    # page attached to a harmless prompt gets the whole call rejected). Walk down the
    # ranked candidates until one passes.
    lib = sorted(ss.library(), key=lambda r: -ss.score(r, want))[:6]
    last = "no style candidates"
    img = cost = sref = None
    for rec in lib:
        cand = [str(ss.as_png(rec["file"]))]
        try:
            img, cost = rep_generate(prompt, refs=list(refs) + cand, quality=quality,
                                     aspect="1152x2048")
            sref = cand
            break
        except Exception as e:
            last = str(e)[-90:]
    if img is None:
        return f"[FAIL] {pid}  {last}"
    OUT.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(img)
    LED.add(page=pid, quality=quality, cost=cost,
            style_ref=[pathlib.Path(p).name for p in sref])
    return f"[ok]   {pid}  {quality:6} ${cost:.3f}  style={pathlib.Path(sref[0]).name if sref else '-'}"


if __name__ == "__main__":
    only = sys.argv[1:] or None
    todo = [p for p in PAGES if not only or p[0] in only]
    print(f"building {len(todo)} pages -> {OUT}")
    with cf.ThreadPoolExecutor(max_workers=min(50, len(todo))) as ex:
        for line in ex.map(build_one, todo):
            print(line)
    print(f"\nchapter ledger: ${LED.spent:.3f}")
