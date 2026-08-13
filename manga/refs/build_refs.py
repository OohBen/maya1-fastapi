"""Reference pack builder.

Batches related sheets into single multi-image requests so a whole batch shares one
reasoning pass — which keeps the art style consistent across the cast, not just within
each sheet.

Resumable: anything already on disk is skipped.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import concurrent.futures as cf  # noqa: E402
from genlib import STYLE, NO_TEXT, rep_generate, Ledger  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "images"
LED = Ledger(pathlib.Path(__file__).resolve().parent / "ledger.json")

SHEET = ("A character reference sheet on a plain flat white background: three full-body views of "
         "ONE character side by side — front view, three-quarter view, and rear view — at identical "
         "height and identical proportions across all three. Neutral standing pose, arms at sides. ")

ENV = ("An empty environment reference plate. The location is completely deserted — there are no "
       "people, no figures and no animals anywhere in the frame. Wide establishing angle. ")

# ---------------------------------------------------------------- the pack
# Design specs are verbatim from the source. See story/00_SERIES_BIBLE.md.
CHARACTERS = {
    "naruto_06": SHEET + (
        "A small, thin, underfed SIX-year-old boy. Short spiky blond hair, large blue eyes, three "
        "faint whisker marks on each cheek. He wears a white short-sleeved shirt with a red spiral "
        "emblem on the chest, orange shorts, and blue open-toe sandals. Expression: guarded and "
        "blank, not smiling."),
    "naruto_07": SHEET + (
        "A thin SEVEN-year-old boy. Short spiky blond hair, blue eyes, three faint whisker marks on "
        "each cheek. He wears a bright orange tracksuit-style jumpsuit with a blue collar, a pair of "
        "goggles pushed up onto his forehead, and black open-toe sandals. Expression: a wide forced "
        "grin that does not reach his eyes."),
    "naruto_13": SHEET + (
        "A THIRTEEN-year-old boy, lean and physically hard. Blond hair grown to shoulder length with "
        "two heavy bangs framing his face, the right bang hanging low enough to completely cover his "
        "right eye. Blue eyes. Whisker marks almost faded away. Completely blank, emotionless "
        "expression. He wears a black long-sleeved shirt with a LARGE red spiral emblem covering the "
        "whole chest, and a small matching red spiral between the shoulder blades on the rear view. "
        "Black tapered trousers. Black CLOSED-TOE boots that fully cover the toes — not open sandals. "
        "Black fingerless gloves with a small red spiral on the back of each hand."),
    "madara": SHEET + (
        # The SILHOUETTE is the character. "Long black hair" produced a generic old wizard;
        # the mane has to be described as the dominant shape or he is not recognisable.
        "An ancient, tall, gaunt man. His defining feature is an ENORMOUS wild mane of jet-black "
        "hair that falls well past his waist and flares outward in huge jagged wind-blown spikes, "
        "with two especially heavy spiked masses sweeping forward down either side of his face and "
        "a great spiked bulk behind — the silhouette is dramatic and unmistakable, far larger than "
        "his head. Very pale skin. A severe angular face with a heavy prominent brow ridge, "
        "deep-set eyes and hollow cheeks. Red eyes, each with three black comma-shaped marks around "
        "the pupil. Floor-length plain black robes with a high collar, leaning on a plain wooden "
        "walking cane. He is extremely old and close to death — the black hair is shot through with "
        "streaks of iron grey, the face deeply lined and sunken. Expression: unreadable, patient, "
        "faintly amused."),
    "hiruzen": SHEET + (
        # The HAT is the silhouette. "Hat resting on his back" produced a generic old man.
        "An old man in his late sixties, the leader of a ninja village. He WEARS ON HIS HEAD a tall "
        "wide ceremonial kage hat: a white conical cap with a broad flat brim, a large rounded RED "
        "front panel bearing one bold black brush-painted kanji character, and long white cloth "
        "drapes hanging from the brim down over his ears, shoulders and back — the hat is large and "
        "dominates his silhouette. Under it, full-length white ceremonial robes with wide sleeves "
        "over a red under-robe, and a white sash. Short neat grey goatee beard and moustache. Deeply "
        "lined weathered face, heavy creases under kind tired eyes. He holds a long slim wooden "
        "smoking pipe. Expression: warm, patient, weighed down."),
    "kakashi": SHEET + (
        "A tall lean man in his late twenties. Spiky silver-grey hair swept to one side. A dark cloth "
        "mask covers his face from the nose down, and a slanted forehead protector covers his left "
        "eye, leaving only his right eye visible. Dark navy long-sleeved uniform under a dark green "
        "flak vest, dark trousers, open-toe sandals. Expression: bored and unreadable."),
    "zetsu": SHEET + (
        "A humanoid plant creature. Its body is split vertically down the centre: the entire right "
        "half is chalk white, the entire left half is pure black. Round yellow eyes with no visible "
        "pupils. It wears a long black cloak. Around its head and shoulders are the two halves of a "
        "large open venus-flytrap-like green shell. Expression: a wide unsettling smile."),
}

MOB = ("A character reference sheet on a plain flat white background: a lineup of FOUR different "
       "adult villagers standing side by side, full body, front view, evenly spaced, at identical "
       "scale. They are ordinary rural townspeople in a feudal Japanese village, wearing simple "
       "worn yukata, work clothes and aprons in muted browns, greys and dull blues. From left to "
       "right: a heavyset bearded man in his forties; a thin sharp-faced man in his thirties; a "
       "middle-aged woman with her hair tied back; an older man with a shaved head. All four share "
       "the same expression — cold, hard, hateful. Each of the four must look completely different "
       "from the others in face, build and clothing.")

ENVIRONMENTS = {
    "env_festival_street": ENV + (
        "A wide street in a feudal Japanese village at night during a festival. Rows of glowing "
        "orange paper lanterns strung overhead in receding lines. Wooden two-storey buildings with "
        "sliding screen doors on both sides, food stalls with cloth awnings, stone-flagged ground. "
        "Warm orange lantern light from above, deep blue-black shadows. Beautiful and inviting."),
    "env_alley": ENV + (
        "A narrow dead-end alley between two wooden village buildings at night. Rough vertical plank "
        "walls, a tall wooden fence closing off the far end, cracked stone paving, a few crates and "
        "a drainage channel. Distant warm orange festival lantern light spills in from the alley "
        "mouth at one end; the far end is in deep blue-black shadow."),
    "env_hospital": ENV + (
        "A small plain hospital room in daylight, empty. A single narrow bed with white sheets, a "
        "steel-framed window with thin curtains, a wooden side table, pale green-grey walls, flat "
        "white ceiling. Cold flat daylight, clinical and cheerless."),
    "env_apartment_int": ENV + (
        "The interior of a small rundown one-room apartment, empty of people. A low kitchen counter "
        "with a single hotplate, a small square table with two stools, a narrow bed against the far "
        "wall, peeling wallpaper, a bare hanging bulb. Dim, cold, lonely, lit by one weak light."),
    "env_classroom": ENV + (
        "An empty ninja academy classroom in daylight. Tiered rows of long wooden desks and benches "
        "rising away from a lectern and a large blackboard, tall windows down one side, wooden floor "
        "and ceiling beams. Flat unromantic daylight."),
}

PROPS = {
    "mangekyo_design": (
        "An extreme close-up study of a single human eye on a plain flat white background, drawn "
        "large and centred, filling the frame. The iris is deep blood red. At the exact centre of "
        "the iris is a small solid black ring. Radiating outward from that central ring are exactly "
        "SIX identical straight black blade shapes, evenly spaced like the spokes of a wheel, each "
        "one reaching all the way out to the outer rim of the iris. Sharp graphic geometry, perfect "
        "symmetry, flat colour, heavy black ink outline."),
    "gunbai": (
        "A single object study on a plain flat white background: a large ornate war fan. The fan "
        "head is a wide flat rounded shape with a deep purple-tinted face and a thick black border, "
        "bearing three large black comma-shaped marks arranged in a circle at its centre. It has a "
        "long straight handle wrapped in bandages at the base, and a heavy chain attached to the end "
        "of the handle. Shown at a slight three-quarter angle. Weighty and battle-worn."),
}


def build(batch_name, items, quality="high"):
    """items: {ref_id: prompt}. One Replicate call per sheet, run in parallel.

    Previously one batched OpenRouter call for cross-sheet style consistency, but that
    path costs ~$0.251/image, ignores the quality parameter, and exhausted the key's
    credit (see PIPELINE.md). Replicate is $0.128 at high and honours the tier. Style
    consistency now comes from binding a finished sheet as an anchor reference instead.
    """
    todo = {k: v for k, v in items.items() if not (OUT / f"{k}.png").exists()}
    if not todo:
        print(f"[{batch_name}] all present, skipping")
        return
    anchor = OUT / "naruto_13.png"
    refs = [str(anchor)] if anchor.exists() else []
    anchor_clause = (
        "Image 1 is a STYLE ANCHOR from the same character-sheet set: match its line weight, "
        "colouring, level of detail and sheet layout so this sheet belongs to the same set. "
        "Ignore its character entirely — do not copy that person's face, hair, age or clothing. "
        if refs else "")

    def one(kv):
        rid, desc = kv
        img, cost = rep_generate(anchor_clause + desc + STYLE + " " + NO_TEXT,
                                 refs=refs, quality=quality, aspect="1024x1024")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{rid}.png").write_bytes(img)
        LED.add(batch=batch_name, id=rid, cost=cost, quality=quality)
        return f"   -> {rid}.png  ${cost:.3f}"

    print(f"[{batch_name}] requesting {len(todo)}: {', '.join(todo)}")
    with cf.ThreadPoolExecutor(max_workers=min(10, len(todo))) as ex:
        for line in ex.map(one, todo.items()):
            print(line)



# ---------------------------------------------------------------- Volume 2
# Silhouette-first: lead every spec with the one shape that identifies the character at
# thumbnail size. See PIPELINE.md — this failed twice (Madara, Hiruzen) before the rule.
CHARACTERS_V3 = {
    "gaara": SHEET + (
        "A short, slight TWELVE-year-old boy whose defining feature is an ENORMOUS sand-coloured "
        "clay gourd strapped upright on his back — nearly as large as he is, dominating his "
        "silhouette from every angle. Short messy dark red hair. NO EYEBROWS AT ALL. Heavy black "
        "rings of sleeplessness around pale blue-green eyes with no visible pupils. A single "
        "blood-red kanji character tattooed on the upper left of his forehead. Long-sleeved dark "
        "maroon-brown full-body outfit, white sash across the chest holding the gourd. Expression: "
        "utterly blank and unblinking."),
    "temari": SHEET + (
        "A confident FIFTEEN-year-old girl whose defining features are FOUR separate blonde "
        "pigtails standing out from her head in a fan shape, and a HUGE closed iron battle fan "
        "strapped diagonally across her back, taller than her torso. Teal-green eyes. Single-piece "
        "pale lavender-grey short kimono dress with a dark sash, dark fingerless gloves. "
        "Expression: sharp, amused, superior."),
    "kankuro": SHEET + (
        "A FOURTEEN-year-old boy whose defining features are a black full-body hooded suit whose "
        "hood has two pointed cat-like ear shapes, and a LARGE BANDAGE-WRAPPED BUNDLE almost his "
        "own size strapped upright on his back. His whole face is painted with bold purple face "
        "paint in angular stripes. Expression: cocky, sneering."),
    "danzo": SHEET + (
        "An old man whose defining features are BANDAGES: his entire right eye and the right side "
        "of his forehead wrapped in white bandages, and his whole right arm bandaged and carried in "
        "a sling under his robe. A prominent X-shaped scar on his chin. Short dark grey hair. One "
        "visible dark eye, cold and calculating. Plain white robe over a dark grey high-collared "
        "under-robe, leaning on a plain wooden cane. Expression: expressionless, patient, predatory."),
    "ibiki": SHEET + (
        "A tall heavily built man whose defining features are a LONG BLACK LEATHER TRENCH COAT over "
        "dark clothing, and a black cloth bandana headband with a metal plate covering all of his "
        "hair. Deep diagonal scars across his face. Expression: intimidating, hard, faintly amused."),
    "anko": SHEET + (
        "A woman in her twenties whose defining features are a light tan ankle-length overcoat worn "
        "open over a FULL-BODY DARK MESH FISHNET BODYSUIT, with a short dark orange skirt. Violet "
        "hair in a short spiky ponytail. Expression: manic, grinning, dangerous."),
    "kabuto": SHEET + (
        "A calm young man of about twenty whose defining features are LARGE ROUND BLACK-RIMMED "
        "GLASSES and silver-grey hair in a short low ponytail. Dark purple long-sleeved shirt and "
        "trousers, shuriken holster on the right hip. Expression: mild, helpful, slightly wrong."),
    "rock_lee": SHEET + (
        "A THIRTEEN-year-old boy whose defining features are a shiny black BOWL-CUT haircut, "
        "ENORMOUS thick black eyebrows, and a skin-tight BRIGHT GREEN full-body jumpsuit. Orange "
        "leg warmers over the shins, bandages around the forearms and hands, forehead protector "
        "worn as a belt at the waist. Expression: earnest, intense, sincere."),
    "kiba": SHEET + (
        "A THIRTEEN-year-old boy whose defining features are two bold RED FANG-SHAPED MARKINGS "
        "painted down his cheeks, spiky brown hair, sharp canine teeth, and a grey hooded jacket "
        "with thick fur trim. A SMALL WHITE PUPPY sits on top of his head. Expression: brash, "
        "grinning, competitive."),
    "shino": SHEET + (
        "A THIRTEEN-year-old boy whose defining features are opaque ROUND DARK SUNGLASSES and a "
        "grey-green hooded coat with an EXTREMELY HIGH COLLAR covering his face from the nose down "
        "— only the glasses and a strip of forehead ever visible. Spiky dark brown hair. "
        "Expression: unreadable, completely still."),
}

ENVIRONMENTS_V3 = {
    "env_training_ground_7": ENV + (
        "An empty forest training clearing with THREE upright weathered wooden posts standing in a "
        "row in open ground, a treeline behind, a river and a stone memorial nearby. Flat morning "
        "daylight."),
    "env_exam_room_301": ENV + (
        "A large empty examination hall: many long rows of individual wooden desks and chairs "
        "facing a blackboard and a raised instructor's platform, tall windows down one side. Flat "
        "institutional daylight."),
    "env_forest_of_death": ENV + (
        "An empty forest of colossally oversized dark trees with trunks many metres thick, roots "
        "like walls, a dense black canopy blotting out the sky, mist between the trunks, and a "
        "tall chain-link perimeter fence in the foreground. Sunless green-black gloom, ominous."),
    "env_academy_corridor": ENV + (
        "An empty wooden school corridor with sliding doors down one side, tall windows down the "
        "other, a staircase at the far end. Flat daylight."),
    "env_shinobi_apartment": ENV + (
        "The interior of a clean modern apartment, empty of people: a low couch, a small dining "
        "table, plain walls, a window with village roofs beyond. Sparse and impersonal, almost no "
        "possessions. Cool even daylight."),
}


# --- V4: the Wave / Snow montage in Volume 2 Chapter 3, plus Naruto's ninjato ---
CHARACTERS_V4 = {
    "zabuza": SHEET + (
        "A very tall, heavily-built adult man whose defining feature is an ENORMOUS flat "
        "rectangular butcher-blade sword, taller and broader than a man, carried on his back — it "
        "has a rounded notch cut out near the hilt and a circular hole through the blade. The lower "
        "half of his face is wrapped in white bandages like a mask. Short spiky black hair, no "
        "eyebrows, narrow brown eyes with tiny pupils. Bare muscular arms, striped grey-and-white "
        "arm and leg warmers, a slanted forehead protector worn sideways on his head. Expression: "
        "murderous, amused."),
    "haku": SHEET + (
        "A slender, delicate-featured teenager of ambiguous appearance whose defining feature is a "
        "smooth WHITE PORCELAIN MASK covering the whole face — plain, with two narrow eye slits and "
        "a single small red swirl marking on the forehead. Long black hair pulled back with two "
        "strands framing the mask. A pale green-grey full-length kimono-style haori over dark "
        "clothing, brown sash. Show the same figure a second time with the mask pushed up onto the "
        "forehead, revealing a soft pale face with large dark brown eyes."),
    "gato": SHEET + (
        "A short, fat, smug middle-aged businessman: barely taller than a child, round black "
        "sunglasses, a neat pointed grey beard, thinning slicked hair, an expensive black pinstripe "
        "business suit, a walking cane, one arm in a sling. Expression: greedy and contemptuous."),
    "kuyoki": SHEET + (
        "A young woman in her early twenties, a princess in hiding: long straight black hair, sharp "
        "dark eyes, heavy dark eye makeup. Show her twice — once in a plain travelling coat with a "
        "sullen bitter expression, and once in ornate white-and-red snow-country royal robes with a "
        "tall formal headdress, standing straight."),
    "naruto_13_sword": SHEET + (
        "A lean THIRTEEN-year-old boy with LONG blond hair hanging well past his jaw to his "
        "shoulders in heavy strands, two thick bangs framing his face, the right bang low enough to "
        "cover his right eye. His hair is never short and never spiky. Blue eyes, faded whisker "
        "marks, blank expression. Black long-sleeved shirt with a large red spiral on the chest, "
        "black trousers, dark sandals, black fingerless gloves with small red spirals. NEW: a plain "
        "straight single-edged NINJATO in a black lacquered scabbard slung diagonally across his "
        "back, its square guard and wrapped hilt showing above his left shoulder. Show him from the "
        "front, from behind so the sword is clearly visible, and drawing the blade."),
}

CHARACTERS_V5 = {
    "kusa_nin": SHEET + (
        "A tall slender ninja of ambiguous appearance in a wide conical STRAW HAT worn low over the "
        "face, and a plain long earth-brown poncho-like robe over a dark bodysuit, with a forehead "
        "protector bearing a single grass-blade symbol. Very long straight black hair falling from "
        "under the hat past the waist. Unnaturally pale, almost white skin. Show the same figure a "
        "second time with the hat tipped back, revealing GOLDEN-YELLOW EYES WITH VERTICAL SLIT "
        "PUPILS, purple markings around them, and a long thin tongue extended far further than any "
        "human tongue should reach. Expression: delighted, predatory."),
    "giant_snake": SHEET + (
        "A COLOSSAL brown-and-tan serpent, thick as a tree trunk and many times the length of a "
        "house — not a person, an animal. Blunt wedge-shaped head, heavy overlapping scales, a pale "
        "banded underbelly, huge golden eyes with vertical black slit pupils, and long curved fangs "
        "in an open mouth. Show the head in close-up, the mouth open wide from the front, and the "
        "whole coiled body at a distance for scale with a small human figure beside it."),
}

ENVIRONMENTS_V4 = {
    "env_wave_bridge": ENV + (
        "An enormous unfinished suspension bridge over grey sea water, empty of people: bare steel "
        "girders and wooden decking, scaffolding, cranes, the far end vanishing into thick white "
        "sea mist. Cold flat overcast light."),
    "env_wave_village": ENV + (
        "A poor coastal fishing village on stilts over shallow water, empty of people: weathered "
        "wooden shacks, sagging walkways, moored rowing boats, grey water, low mist. Bleak."),
    "env_snow_country": ENV + (
        "A frozen northern landscape, empty of people: a snowfield under a pale sky, black pines "
        "heavy with snow, a jagged ice ridge, and a dark stone castle with steep roofs in the far "
        "distance. Cold blue-white light, long shadows."),
}


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "cast1"):
        build("cast1", {k: CHARACTERS[k] for k in
                        ["naruto_06", "naruto_07", "naruto_13", "madara"]})
    if which in ("all", "cast2"):
        build("cast2", {**{k: CHARACTERS[k] for k in ["hiruzen", "kakashi", "zetsu"]},
                        "mob_archetypes": MOB})
    if which in ("all", "env"):
        build("env", ENVIRONMENTS)
    if which in ("all", "props"):
        build("props", PROPS)
    if which in ("all", "cast3"):
        build("cast3", {k: CHARACTERS_V2[k] for k in
                        ["naruto_10", "iruka", "ayame", "teuchi", "minato_kushina"]})
    if which in ("all", "cast4"):
        build("cast4", {k: CHARACTERS_V2[k] for k in
                        ["shikamaru", "choji", "hinata", "sasuke", "sakura", "ino"]})
    if which in ("all", "env2"):
        build("env2", {k: ENVIRONMENTS_V2[k] for k in
                       ["env_jonin_lounge", "env_apartment_ext", "env_hokage_office",
                        "env_academy_ext", "env_playground"]})
    if which in ("all", "env3"):
        build("env3", {k: ENVIRONMENTS_V2[k] for k in
                       ["env_monument", "env_ichiraku", "env_village_street", "env_burial"]})
    if which in ("all", "env4"):
        build("env4", {k: ENVIRONMENTS_V2[k] for k in
                       ["env_hideout_corridor", "env_hideout_kitchen", "env_hideout_training",
                        "env_hideout_tablets", "env_bandit_camp"]})
    if which in ("all", "props2"):
        build("props2", PROPS_V2)
    if which in ("all", "v2cast1"):
        build("v2cast1", {k: CHARACTERS_V3[k] for k in
                          ["gaara", "temari", "kankuro", "danzo", "ibiki"]})
    if which in ("all", "v2cast2"):
        build("v2cast2", {k: CHARACTERS_V3[k] for k in
                          ["anko", "kabuto", "rock_lee", "kiba", "shino"]})
    if which in ("all", "v2env"):
        build("v2env", ENVIRONMENTS_V3)
    if which in ("all", "v2cast3"):
        build("v2cast3", CHARACTERS_V4)
    if which in ("all", "v2env2"):
        build("v2env2", ENVIRONMENTS_V4)
    if which in ("all", "v2cast4"):
        build("v2cast4", CHARACTERS_V5)
    print(f"\nledger total: ${LED.spent:.4f}")
