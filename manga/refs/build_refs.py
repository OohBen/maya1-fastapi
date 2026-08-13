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
        "A very old, tall, gaunt man. Long wild black hair falling past his shoulders in heavy "
        "spikes. Deeply lined face, hollow cheeks. Red eyes with three black comma-shaped marks "
        "around each pupil. He wears floor-length plain black robes and leans on a plain wooden "
        "walking cane held in his right hand. Expression: unreadable, patient, faintly amused."),
    "hiruzen": SHEET + (
        "An old man in his late sixties, kindly and tired, with a short grey beard and lined face. "
        "He wears white and red ceremonial robes with a wide-brimmed conical hat resting on his back, "
        "and simple sandals. Expression: warm but weighed down."),
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
    print(f"\nledger total: ${LED.spent:.4f}")
