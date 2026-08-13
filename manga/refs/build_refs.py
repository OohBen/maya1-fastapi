"""Reference pack builder.

Batches related sheets into single multi-image requests so a whole batch shares one
reasoning pass — which keeps the art style consistent across the cast, not just within
each sheet.

Resumable: anything already on disk is skipped.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, generate, save, Ledger  # noqa: E402

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
    """items: {ref_id: prompt}. Generates the whole batch in ONE request."""
    todo = {k: v for k, v in items.items() if not (OUT / f"{k}.png").exists()}
    if not todo:
        print(f"[{batch_name}] all present, skipping")
        return
    ids = list(todo)
    header = (f"Generate {len(ids)} SEPARATE reference images, one per subject listed below, in "
              f"this exact order. Each image is a standalone reference sheet showing only its own "
              f"subject. Render all of them in one single consistent art style.\n\n")
    body = "".join(f"IMAGE {i+1} — {k}:\n{todo[k]}\n\n" for i, k in enumerate(ids))
    prompt = header + body + STYLE + " " + NO_TEXT

    print(f"[{batch_name}] requesting {len(ids)}: {', '.join(ids)}")
    imgs, cost = generate(prompt, n=len(ids), quality=quality)
    print(f"[{batch_name}] got {len(imgs)} images, cost ${cost:.4f}")
    names = ids if len(imgs) == len(ids) else [f"{batch_name}_{i+1}" for i in range(len(imgs))]
    paths = save(imgs, OUT, names)
    LED.add(batch=batch_name, ids=ids, returned=len(imgs), cost=cost, quality=quality,
            files=[str(p) for p in paths])
    for p in paths:
        print("   ->", p.name)


# ---------------------------------------------------------------- Volume 1, ch2-9
CHARACTERS_V2 = {
    "naruto_10": SHEET + (
        "A TEN-year-old boy, wiry and physically hardened from years of training. Blond hair grown "
        "to just below the ears, starting to fall in two bangs. Whisker marks faint. His eyes are "
        "RED with three small black comma-shaped marks around each pupil. Completely blank "
        "expression. He wears a plain dark grey long-sleeved training top, black trousers and dark "
        "open-toe sandals."),
    "iruka": SHEET + (
        "A man in his mid-twenties with dark brown hair pulled into a short spiky ponytail and a "
        "horizontal scar across the bridge of his nose. Standard dark navy long-sleeved uniform "
        "under a dark green flak vest, dark trousers, open-toe sandals. Expression: stern and "
        "closed off."),
    "ayame": SHEET + (
        "A friendly young woman of about twenty with shoulder-length brown hair tied back under a "
        "white bandana, dark eyes. She wears a simple white cook's tunic with sleeves rolled up and "
        "a white apron. Expression: bright, open, genuinely kind."),
    "teuchi": SHEET + (
        "A stocky cheerful man in his fifties with a lined weathered face, thin moustache, and a "
        "white cook's bandana tied over his head. White cook's tunic and apron. Expression: warm "
        "and unbothered."),
    "shikamaru": SHEET + (
        "A twelve-year-old boy with black hair pulled up into a short spiky pineapple-shaped "
        "ponytail, narrow bored eyes. He wears a grey short-sleeved jacket with green trim over a "
        "dark mesh shirt, brown trousers. Expression: half-asleep and unimpressed."),
    "choji": SHEET + (
        "A heavyset twelve-year-old boy with spiky reddish-brown hair, small friendly eyes, and two "
        "red swirl markings on his cheeks. He wears a green short-sleeved jacket over a white shirt "
        "with a stylised symbol, and dark shorts. Expression: cheerful and eating."),
    "hinata": SHEET + (
        "A shy twelve-year-old girl with short dark blue-black hair cut in a straight fringe, and "
        "very pale lavender-white eyes with no visible pupils. She wears a cream hooded jacket with "
        "fur trim at the cuffs and dark navy trousers. Expression: timid, looking down and away."),
    "sasuke": SHEET + (
        "A twelve-year-old boy with black hair that spikes upward at the back and two long bangs "
        "framing his face, dark eyes. He wears a high-collared dark navy blue shirt with a wide "
        "collar and white shorts, with white arm warmers. Expression: cold, closed, arrogant."),
    "sakura": SHEET + (
        "A twelve-year-old girl with chin-length pink hair, a wide forehead and green eyes, wearing "
        "a red sleeveless qipao-style dress with white trim over dark shorts. Expression: eager "
        "and a little sharp."),
    "ino": SHEET + (
        "A twelve-year-old girl with long pale blonde hair in a high ponytail with a long fringe "
        "over one eye, and light blue eyes. She wears a purple crop top and matching purple skirt "
        "with bandaged legs. Expression: confident and teasing."),
    "minato_kushina": (
        "A character reference sheet on a plain flat white background showing TWO adults standing "
        "side by side, full body, front view, at the same scale. LEFT: a tall man in his late "
        "twenties with bright spiky blond hair and blue eyes, wearing a white long coat with red "
        "flame patterns along the hem over a dark blue uniform. RIGHT: a woman in her late twenties "
        "with very long straight deep-red hair falling past her waist and violet eyes, wearing a "
        "simple pale green dress. Both have warm, gentle expressions. They must look completely "
        "different from one another."),
}

ENVIRONMENTS_V2 = {
    "env_jonin_lounge": ENV + (
        "An empty military lounge room: low couches, a long table with scattered scrolls and cups, "
        "a notice board, wooden floor, tall windows. Warm dim afternoon light."),
    "env_apartment_ext": ENV + (
        "The exterior walkway of a shabby low-rise apartment block at night. A concrete balcony "
        "corridor with peeling paint, a row of identical worn doors, a single flickering light. "
        "Cold blue night with one weak warm bulb."),
    "env_hokage_office": ENV + (
        "An empty circular office at the top of a tower. A large wooden desk buried under stacks of "
        "paper, a tall leather chair, wide arched windows looking out over a village, framed "
        "portraits on the wall, bookshelves. Warm late-afternoon light."),
    "env_academy_ext": ENV + (
        "The empty front courtyard of a ninja academy building in daylight — a broad wooden "
        "building with a tiled roof and a large arched entrance, a swing hanging from a tree in the "
        "yard, low boundary wall. Flat unromantic daylight."),
    "env_playground": ENV + (
        "An empty school playground with packed dirt ground, a single large tree with a rope swing, "
        "a low fence, wooden benches, the academy building behind. Flat daylight."),
    "env_monument": ENV + (
        "An enormous cliff face carved with four colossal stone faces, seen from the narrow flat "
        "ledge running along the top of their stone hair. A vast village of tiled roofs spreads out "
        "far below and behind. Night, cold blue moonlight."),
    "env_ichiraku": ENV + (
        "A tiny empty ramen stand at night: a short wooden counter with five stools, hanging cloth "
        "noren curtains across the front, steam-stained wooden walls, shelves of bowls, a warm "
        "paper lantern. Warm amber light, the only warm place in the village."),
    "env_village_street": ENV + (
        "An ordinary empty village street in daylight — wooden two-storey buildings with sliding "
        "screen doors, shop awnings, stone paving, distant rooftops. Flat plain daylight."),
    "env_hideout_corridor": ENV + (
        "A vast empty underground stone corridor, almost entirely black. Rough carved rock walls "
        "vanishing into darkness, a floor of flat stone slabs, no light source visible. Near-black "
        "with hard cold rim light on the edges only. No warm tones anywhere."),
    "env_hideout_kitchen": ENV + (
        "A bare underground stone room with a rough wooden table and two chairs, a cold hearth, "
        "stone walls. Almost entirely dark, lit by one small cold light. No warm tones."),
    "env_hideout_training": ENV + (
        "An enormous empty underground cavern used as a training ground: a wide flat floor of packed "
        "earth and stone, jagged rock walls rising into blackness, scattered wooden training posts "
        "and heavy stone weights. Cold hard light from above. No warm tones."),
    "env_hideout_tablets": ENV + (
        "A small underground stone chamber, empty. One wall is a single enormous ancient stone "
        "tablet covered edge to edge in dense carved spiral glyphs. Cold pale light rakes across "
        "the carving. No warm tones."),
    "env_bandit_camp": ENV + (
        "An empty bandit camp in a forest clearing at dusk: crude patched tents, a smouldering "
        "cookfire, stacked crates and stolen goods, weapons leaning against a log, trampled mud. "
        "Grey-orange failing light."),
    "env_burial": ENV + (
        "A bare windswept hillside at dawn, empty. A single fresh mound of dark earth with one plain "
        "unmarked stone set at its head, long dry grass bent by wind, a pale colourless sky."),
}

PROPS_V2 = {
    "sharingan_progression": (
        "A study sheet on a plain flat white background showing FOUR versions of the same eye in a "
        "row, left to right, drawn large and identical in size and framing. EYE 1: an ordinary blue "
        "human eye. EYE 2: a deep red iris with ONE small black comma-shaped mark beside the pupil. "
        "EYE 3: a deep red iris with THREE black comma-shaped marks evenly spaced around the pupil. "
        "EYE 4: a deep red iris with a small solid black ring at the centre and exactly SIX straight "
        "black blades radiating out from that ring to the rim. Flat colour, heavy black ink outline, "
        "perfectly consistent shape and size across all four."),
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
    print(f"\nledger total: ${LED.spent:.4f}")
