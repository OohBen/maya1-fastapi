"""Chapter 4 — "Kushina". 20 images: title plate + 19 story pages.

Structure: warmth, then the drop. Three months of dinners -> the monument (he never
sits on the Fourth) -> Ichiraku, the warmest pages in the volume -> the walk home ->
"Who are you?" -> "I am that man." -> the pivot -> her name.

gpt-image-2 on Replicate. References are free there, so every page carries its full
binding set. Resumable — existing pages are skipped. Run: python3 chapters/build_ch04.py
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch04" / "raw"
LED = Ledger(HERE / "ch04" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")

BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# ----------------------------------------------------------------- bindings
BIND_N7 = ("Image 1 is the CHARACTER REFERENCE for the boy: a small skinny seven-year-old with "
           "short spiky bright blond hair, blue eyes and three faint whisker marks on each cheek, "
           "wearing a bright orange tracksuit jumpsuit with a dark navy collar and a dark navy "
           "waistband, a pair of dark round-lensed goggles on a navy strap worn up on his forehead, "
           "and black open-toe shinobi sandals. Reproduce that face, hair, goggles and outfit "
           "exactly. Ignore Image 1's white background, its three-view layout, its standing pose "
           "and its fixed grin — his expression on this page is whatever the panel describes. "
           + UNIQUE + " ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the old man: an elderly man with a long "
               "heavy mane of spiked black hair falling well past his shoulders, a gaunt "
               "deeply-lined pale face, dark red irises, a plain floor-length black robe with wide "
               "sleeves, black shoes and a plain wooden walking cane. Reproduce that face, hair, "
               "robe and cane exactly. Ignore Image {i}'s white background, its three-view layout "
               "and its standing pose. ")

BIND_AYAME = ("Image {i} is the CHARACTER REFERENCE for the young woman who works the ramen stall: "
              "a warm young woman in her late teens with medium-length brown hair and brown eyes, a "
              "white cloth bandana tied over her head, a white kimono-style cook's top with the "
              "sleeves rolled to the elbow, a long white apron and dark shoes. Reproduce her face "
              "and outfit exactly. Ignore Image {i}'s white background, its three-view layout and "
              "its standing pose. ")

BIND_TEUCHI = ("Image {i} is the CHARACTER REFERENCE for the older cook who runs the ramen stall: a "
               "stocky middle-aged man with a grey moustache, narrow crinkled smiling eyes, a white "
               "cloth bandana tied over his head, a white kimono-style cook's top, a long white "
               "apron, dark grey trousers and dark sandals. Reproduce his face and outfit exactly. "
               "Ignore Image {i}'s white background, its three-view layout and its standing pose. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, props, colour palette and "
            "lighting exactly. Do not copy its camera angle, and ignore the fact that it is empty "
            "of people. ")

BIND_MON = ("Image {i} is the LOCATION REFERENCE for the Hokage Monument — reuse its cliff face, its "
            "carved-stone rendering, its stone walkway and the tiled village roofs spread out below "
            "it. Do not copy its camera angle, and ignore the fact that it is empty of people. Image "
            "{i} shows only the first three carved heads; this page also includes a FOURTH carved "
            "stone head further along the same cliff — a much younger man's face with a broad spiked "
            "fringe of stone hair falling either side of it and a plain band across the brow, "
            "obviously the newest carving of the row. Re-light the scene for dusk rather than for "
            "deep night. ")

BIND_STREET = ("Image {i} is the LOCATION REFERENCE for the village street — reuse its two-storey "
               "wooden shopfronts, tiled roofs, sliding paper doors and pale flagstone paving "
               "exactly. Do not copy its camera angle and do not copy its daytime lighting: this "
               "scene is at night. Ignore the fact that it is empty of people. ")

# ----------------------------------------------------------------- lighting
LIGHT_APT = ("Lighting: one bare bulb hanging low over the table — a small hard pool of dim yellow-"
             "white light with hard-edged shadows, and cold blue-grey darkness everywhere beyond "
             "it. The room is cold and the light is not enough. ")
LIGHT_MON = ("Lighting: cold blue dusk. The carved stone reads as flat pale blue-grey, the sky is a "
             "thin band of dull orange at the horizon going to deep blue overhead, shadows are hard-"
             "edged and long. No warm light touches the boy. ")
LIGHT_ICHI = ("Lighting: warm orange lantern light spilling out of the stall over the counter, the "
              "stools and everybody's faces, with the street beyond falling away into deep blue-"
              "black night. This warm pool of light is the only warmth anywhere in the chapter — "
              "make it generous and inviting. ")
LIGHT_STREET = ("Lighting: night. Cold blue-grey shadow across the street and paving, a few small "
                "patches of warm yellow window light from the shopfronts, hard-edged shadows. ")

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 ("00_title", 1,
  "A single full-bleed illustration, no panels and no gutters. A wide dusk view along the top of "
  "the great carved stone monument above the village: the row of enormous carved stone faces set "
  "into the cliff, seen from behind and above at a shallow angle, with the whole village of tiled "
  "roofs spread out far below and beyond them. On the crown of the FIRST carved head, at the far "
  "left of the row, sits one very small boy in a bright orange jumpsuit with goggles on his "
  "forehead, knees drawn up, tiny against the vast pale stone, looking out over the village away "
  "from us. Further along the cliff to the right, smaller in the frame, the FOURTH carved head is "
  "clearly visible — a young man's face with a broad spiked stone fringe and a plain band across "
  "the brow — and nobody is on it. Keep the entire upper third of the image as calm uncluttered "
  "dusk sky for a title to be placed later. " + BIND_N7 + BIND_MON.format(i=2) + LIGHT_MON,
  R("naruto_07", "env_monument"), "high"),

 # ---- beat 1: three months of dinners --------------------------------
 ("p01", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "Three months of dinners, told without words. PANEL 1 (wide, top): a flat side-on two-shot of the "
  "shabby one-room apartment — the small blond boy on one wooden stool and the old man in black on "
  "the other, at the small wooden table, both eating from bowls. Two paper grocery bags stand on "
  "the kitchen counter behind them. The old man's cane leans against the table edge. PANEL 2 "
  "(middle, small insert): a tight shot of three thick hardback books stacked at the corner of the "
  "table beside a bowl. PANEL 3 (wide, bottom): the same two-shot, a different night — the table "
  "now crowded with empty bowls and open books, the boy talking with his mouth full and gesturing "
  "with his chopsticks, the old man sitting very still and listening to him. " + LIGHT_APT,
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p02", 4,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "Four panels in one identical repeated composition: every panel uses the exact same overhead "
  "camera looking straight down at the same small wooden tabletop from directly above, the table in "
  "the same place in every frame, so that only the objects change between them. PANEL 1: two full "
  "steaming bowls of noodles side by side, two pairs of chopsticks, a stack of three new hardback "
  "books at the edge. PANEL 2: the same table later — the bowls half emptied, one book lying open "
  "showing an illustrated diagram of two hands folded into a sign, a small boy's hand and a long "
  "bony old man's hand both reaching into frame. PANEL 3: the same table, another night — bowls "
  "empty and stacked, books squared up neatly, the head of a plain wooden cane leaning into one "
  "corner of the frame. PANEL 4: the same table, another night again — two bowls pushed aside, the "
  "boy's spiky blond head and folded arms resting on the tabletop as he sleeps on it, and at the "
  "edge of frame the old man's lined hand laying a folded blanket down beside him. " + LIGHT_APT,
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 # ---- beat 2: the monument -------------------------------------------
 ("p03", 3,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "PANEL 1 (wide, top): seen from behind and below, the small boy climbing the last few steps of a "
  "long carved stone stairway cut up the back of the cliff, dusk sky above him. PANEL 2 (middle, "
  "small): a tight low shot of his black sandals stepping up onto the flat stone walkway at the "
  "top. PANEL 3 (wide, bottom): a wide establishing shot along the stone walkway behind the row of "
  "enormous carved heads, the boy tiny at the left-hand edge of the frame, the village far below "
  "and beyond. He does this every week and he knows exactly where he is going. " + LIGHT_MON,
  R("naruto_07", "env_monument"), "low"),

 ("p04", 3,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "The page is about what he refuses to look at. PANEL 1 (large, top half): a steep low angle "
  "looking up at the FOURTH carved stone head from the walkway beside it — a young man's calm "
  "serene face in pale stone, a broad spiked stone fringe falling either side of it, a plain band "
  "carved across the brow. It fills the panel and dominates the page. PANEL 2 (middle): a close "
  "profile of the boy's face as he walks past below it, eyes fixed dead ahead, jaw set, "
  "deliberately not turning his head even slightly. PANEL 3 (wide, bottom): a wide side view of the "
  "walkway — the boy small, walking on past the base of that fourth head without breaking stride, "
  "heading for the far left end of the row. " + LIGHT_MON,
  R("naruto_07", "env_monument"), "low"),

 ("p05", 2,
  PAGE + BIND_N7 + BIND_MON.format(i=2) +
  "PANEL 1 (large, top two thirds): a wide shot from behind and slightly above. The boy sits "
  "cross-legged on the crown of the FIRST carved stone head at the far left of the row — a tiny "
  "orange shape on an enormous mass of pale carved stone hair — looking out over the whole village "
  "at dusk. Far off to the right along the same cliff, small in the frame, the FOURTH carved head "
  "is visible, and it is empty. PANEL 2 (bottom): a tight profile close-up of the boy's face at "
  "rest — no grin, no performance, just a tired seven-year-old with the wind moving his hair. "
  + LIGHT_MON, R("naruto_07", "env_monument"), "low"),

 # ---- beat 3: Ichiraku, the warmest pages in the volume ---------------
 ("p06", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "PANEL 1 (wide, top): a dark blue village street at night, and halfway down it one small wooden "
  "ramen stall glowing warm orange — a hanging paper lantern, short cloth curtains strung above the "
  "counter, steam rising from the pots. The boy is a small dark silhouette at the near end of the "
  "street, stopped, just looking at it. PANEL 2 (middle, small): his hand pushing one of the "
  "hanging cloth curtains aside. PANEL 3 (wide, bottom): reverse angle from inside the stall — the "
  "boy's face appearing under the curtain, lit warm orange from the side. It is the first warm "
  "light on him in the whole chapter. " + LIGHT_ICHI,
  R("naruto_07", "env_ichiraku"), "low"),

 ("p07", 3,
  PAGE + BIND_N7 + BIND_AYAME.format(i=2) + BIND_ENV.format(i=3) +
  "This is the emotional centre of the whole book. Draw it plainly and tenderly, with no irony. "
  "PANEL 1 (top): the young woman behind the counter turning around with a stack of clean bowls in "
  "her arms and catching sight of him — her whole face opening up. PANEL 2 (middle, small): the "
  "stack of bowls set down hard and crooked on the counter, one of them still wobbling, abandoned. "
  "PANEL 3 (large, bottom half): she has come out around the end of the counter, dropped to her "
  "knees on the street beside the stall, and pulled the small boy into a full tight hug with both "
  "arms right around him, her cheek against his hair. His arms are still hanging straight down at "
  "his sides and his eyes are wide open over her shoulder — nobody has ever done this to him and he "
  "has no idea what to do with it. Warm orange lantern light falls over both of them; the street "
  "behind is deep blue night. " + LIGHT_ICHI + BALLOONS.format(k="two"),
  R("naruto_07", "ayame", "env_ichiraku"), "medium"),

 ("p08", 3,
  PAGE + BIND_N7 + BIND_TEUCHI.format(i=2) + BIND_AYAME.format(i=3) + BIND_ENV.format(i=4) +
  "A comedy page, played completely straight. PANEL 1 (top): the older cook leans out over the "
  "counter on both forearms, grinning under his moustache, eyes crinkled shut, making an "
  "announcement. PANEL 2 (middle): the boy is up on a stool, so short that his chin is nearly level "
  "with the countertop, holding up both hands with all ten fingers spread, his face absolutely "
  "solemn and businesslike. PANEL 3 (wide, bottom): the cook and the young woman both frozen "
  "completely still behind the counter, looking sideways at each other, deadpan. " + LIGHT_ICHI
  + BALLOONS.format(k="three"),
  R("naruto_07", "teuchi", "ayame", "env_ichiraku"), "low"),

 ("p09", 4,
  PAGE + BIND_N7 + BIND_TEUCHI.format(i=2) + BIND_AYAME.format(i=3) + BIND_ENV.format(i=4) +
  "PANEL 1 (wide, top): behind the counter, the older cook working three pots at once in a blur of "
  "motion, sweating, sleeves shoved up, shouting something over his shoulder. PANEL 2 (middle "
  "left): extreme close-up of the boy's face mid-mouthful — cheeks completely packed, eyes squeezed "
  "shut in pure bliss, broth on his chin. PANEL 3 (middle right, narrow and tall): a precarious "
  "leaning tower of empty stacked bowls on the counter beside him, far taller than he is. PANEL 4 "
  "(wide, bottom): the young woman leaning on the counter with her chin in both hands, laughing "
  "openly at him, thoroughly delighted. " + LIGHT_ICHI + BALLOONS.format(k="two"),
  R("naruto_07", "teuchi", "ayame", "env_ichiraku"), "low"),

 ("p10", 3,
  PAGE + BIND_N7 + BIND_AYAME.format(i=2) + BIND_TEUCHI.format(i=3) + BIND_ENV.format(i=4) +
  "The point of the whole sequence: this is the only place in the village where he is treated as a "
  "child. PANEL 1 (top): the young woman reaches across the counter and wipes the broth off his "
  "chin with a folded cloth, exactly the way you would with a much smaller child; he has screwed "
  "his eyes shut and is enduring it, squirming slightly. PANEL 2 (middle, small): the older cook "
  "laughing, one flat hand slapped down on the counter. PANEL 3 (large, bottom half): close on the "
  "boy's face a moment later, once they have both turned away — a small, real, slightly stunned "
  "smile. It is nothing like a performed grin: the mouth is small and closed and the eyes are soft "
  "and lowered. Nobody in the panel is looking at him. " + LIGHT_ICHI + BALLOONS.format(k="two"),
  R("naruto_07", "ayame", "teuchi", "env_ichiraku"), "low"),

 # ---- beat 4: the walk home ------------------------------------------
 ("p11", 4,
  PAGE + BIND_N7 + BIND_STREET.format(i=2) +
  "PANEL 1 (wide, top): the boy walking away from us down the middle of the night village street, "
  "small, unhurried, hands shoved in his jumpsuit pockets. PANEL 2 (middle left): two adult "
  "villagers stopped in a lit doorway, heads together, one of them covering her mouth as she "
  "speaks, both watching him go. PANEL 3 (middle right): a shopkeeper pulling a small child indoors "
  "by the wrist and sliding the door shut. PANEL 4 (wide, bottom): close on the boy's face as he "
  "walks, completely level — he does not flinch, does not speed up and does not look at any of "
  "them. He has somewhere better to be now. " + LIGHT_STREET + BALLOONS.format(k="two"),
  R("naruto_07", "env_village_street"), "low"),

 # ---- beat 5: the question -------------------------------------------
 ("p12", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the dim one-room apartment, the bare bulb hanging low over the small wooden "
  "table. The old man in black sits on one stool with his cane leaning beside him, the boy on the "
  "other, two steaming bowls between them. PANEL 2 (middle, small insert): the boy's hands laying "
  "his chopsticks down flat across the top of his bowl. The bowl has not been touched. PANEL 3 "
  "(bottom, large): the boy looking straight up across the table at the old man, his face serious "
  "in a way it has not been anywhere else in this chapter. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 # ---- beat 6: "I am that man" ----------------------------------------
 ("p13", 3,
  PAGE + BIND_MADARA.format(i=1) + BIND_ENV.format(i=2) +
  "The old man is alone in every panel of this page. PANEL 1 (top): a close profile of the old man "
  "in the apartment — he does not answer at once; half his lined face is in the bulb's hard light "
  "and half is in flat black shadow. PANEL 2 (middle, small insert): his long bony hand resting "
  "over the head of the plain wooden cane. PANEL 3 (bottom, large): the old man turned to face "
  "straight out at the camera, and for the first time both of his eyes are fully lit — dark red "
  "irises, calm, level and entirely serious. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("madara", "env_apartment_int"), "low"),

 ("p14", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The gravity is punctured immediately. PANEL 1 (top): the boy's face across the table, blank for "
  "a beat while he processes it. PANEL 2 (middle): a flat deadpan close-up of the boy — half-lidded "
  "eyes, mouth a flat line. He does not believe a single word of it. PANEL 3 (wide, bottom): the "
  "boy jerking a thumb back at the stack of thick history books on the end of the table while "
  "talking with his mouth full and picking his bowl back up; across from him the old man sits "
  "unreadable, hands folded. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 # ---- beat 7: the pivot ----------------------------------------------
 ("p15", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The old man does not argue, because he does not need to. PANEL 1 (top): a close shot of the old "
  "man letting it go — the smallest tilt of the head, something almost amused at the corner of his "
  "mouth. PANEL 2 (middle, small insert): his hand turning a small cup slowly a quarter-turn on the "
  "tabletop while he chooses what to say. PANEL 3 (wide, bottom): a two-shot straight across the "
  "table — the old man speaking evenly, the boy on the far side still chewing, not really "
  "listening yet. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p16", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "Total, instant capitulation. PANEL 1 (top, small): the boy's chopsticks stop dead halfway to his "
  "open mouth. PANEL 2 (middle, small insert): a single noodle sliding off the stalled chopsticks "
  "and dropping back into the bowl, entirely unnoticed. PANEL 3 (large, bottom half): the boy has "
  "come straight up off his stool and is leaning right out across the table on both flat hands, "
  "face pushed forward, eyes enormous and shining, every trace of the deadpan gone — he is seven "
  "years old and he has never wanted anything this badly. The old man sits back from him, watching "
  "this land exactly as he intended it to. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 # ---- beat 8: her name ------------------------------------------------
 ("p17", 3,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the old man puts one flat hand out across the table — sit down. The boy "
  "sits, rigid, right on the front edge of the stool, hands on his knees. PANEL 2 (middle): a close "
  "shot of the old man speaking, careful and deliberate, choosing every word. PANEL 3 (bottom): a "
  "close shot from the side of the boy's lap and middle — both his fists closed tight on his knees, "
  "the forgotten bowl going cold on the table above them. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "madara", "env_apartment_int"), "low"),

 ("p18", 3,
  PAGE + BIND_N7 + BIND_ENV.format(i=2) +
  "PANEL 1 (top): the boy's face in the apartment, lit hard from above by the bulb — it has not "
  "landed yet. PANEL 2 (middle, large): a symbolic insert panel with no room and no furniture in it "
  "at all — the small orange figure of the boy standing alone in a flat empty black field, lit only "
  "from directly above, one hand pressed flat over his own stomach. Nothing else whatsoever is in "
  "this panel. PANEL 3 (bottom): back in the apartment, the boy looking up and asking a question, "
  "his shoulders small and his voice clearly quiet. " + LIGHT_APT + BALLOONS.format(k="two"),
  R("naruto_07", "env_apartment_int"), "low"),

 ("p19", 2,
  PAGE + BIND_N7 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The final page of the "
  "chapter. PANEL 1 (a narrow strip across the top): an extreme close-up of the old man's mouth and "
  "lined jaw as he speaks, everything else in the panel falling into black. PANEL 2 (enormous, the "
  "entire rest of the page): the boy's face straight on and very close, filling the frame. His eyes "
  "are wide and utterly still, pupils small. He is not crying and he is not smiling — he has just "
  "been handed the only thing anyone has ever given him for nothing, which is a name. The whole "
  "room has dropped away into darkness behind him and only his face is lit, hard, by the bare bulb "
  "above. Show his face and nothing else: there is no woman anywhere in this image, no second "
  "figure, no memory, no vision, no ghostly image behind him. " + LIGHT_APT + BALLOONS.format(k="one"),
  R("naruto_07", "madara", "env_apartment_int"), "medium"),
]


def build_one(spec):
    pid, panels, desc, refs, quality = spec
    dest = OUT / f"{pid}.png"
    if dest.exists():
        return f"[skip] {pid}"
    prompt = desc + " " + STYLE + " " + NO_TEXT
    img, cost = rep_generate(prompt, refs=refs, quality=quality, aspect="2:3")
    OUT.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(img)
    LED.add(page=pid, quality=quality, cost=cost, refs=[pathlib.Path(r).stem for r in refs])
    return f"[ok]   {pid}  {quality:6} ${cost:.3f}"


if __name__ == "__main__":
    only = sys.argv[1:] or None
    todo = [p for p in PAGES if not only or p[0] in only]
    print(f"building {len(todo)} pages -> {OUT}")
    with cf.ThreadPoolExecutor(max_workers=50) as ex:
        for line in ex.map(build_one, todo):
            print(line)
    print(f"\nchapter ledger: ${LED.spent:.3f}")
