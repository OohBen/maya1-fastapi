"""Chapter 8 — "Inheritance". 20 pages.

fic ch2 end -> ch3 open. Two time skips (age 10 -> 13) handled with a montage strip
and a clean cut, not dramatised. The quiet climax is the name.

AGE BINDING IS THE RISK ON THIS CHAPTER:
  p01-p12  -> naruto_10  (wiry, hair just below the ears, red three-tomoe eyes,
                          plain dark grey training top)
  p13-p20  -> naruto_13  (shoulder-length hair, right bang over the right eye,
                          black shirt with a large red spiral, gloves)
p12 is the seam: it is deliberately faceless silhouettes and body inserts so the two
designs never share a page.
"""
import concurrent.futures as cf
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from genlib import STYLE, NO_TEXT, UNIQUE, rep_generate, Ledger  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE.parent / "refs" / "images"
OUT = HERE / "ch08" / "raw"
LED = Ledger(HERE / "ch08" / "ledger.json")

R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

PAGE = ("A single complete manga PAGE in portrait orientation, with a clean white page margin and "
        "clean white gutters between panels, read left to right. ")
FULL = "A single full-page illustration filling the whole page, no panel divisions. "
BALLOONS = ("Leave {k} empty white speech balloons with clean black outlines in uncluttered areas. "
            "Every balloon is left completely blank inside — plain white, empty, unlettered. ")

# ------------------------------------------------------------------ bindings
BIND_N10 = ("Image 1 is the CHARACTER REFERENCE for the boy: a wiry, physically hardened "
            "TEN-year-old with blond hair grown to just below his ears and falling in two bangs, "
            "faint whisker marks, and RED eyes with three small black comma-shaped marks arranged "
            "around each pupil. He wears a plain dark grey long-sleeved training top, black "
            "trousers and dark open-toe sandals. Reproduce that face, hair, eye colour and outfit "
            "exactly. Ignore Image 1's white background, its three-view layout and its standing "
            "pose. " + UNIQUE + " ")

# Age-13 design, public / ordinary eyes.
BIND_N13 = ("Image 1 is the CHARACTER REFERENCE for the boy: a lean thirteen-year-old with blond "
            "hair to his shoulders, two heavy bangs with the RIGHT bang hanging low enough to "
            "cover his right eye completely, whisker marks almost faded, a blank expression, "
            "wearing a black long-sleeved shirt with a large red spiral covering the chest, black "
            "trousers, dark sandals, and black fingerless gloves with a small red spiral on the "
            "back of each hand. Reproduce that face, hair and outfit exactly. Ignore Image 1's "
            "white background, its three-view layout and its standing pose. " + UNIQUE + " ")

# Age-13 design with the Sharingan left on, as he keeps it in private.
BIND_N13R = BIND_N13 + ("One change from Image 1: his single visible left eye is RED with three "
                        "small black comma-shaped marks around the pupil, replacing the reference "
                        "sheet's blue eye colour. His right eye stays hidden behind his bang. ")

BIND_MADARA = ("Image {i} is the CHARACTER REFERENCE for the old man: very old, tall, gaunt, long "
               "wild black hair in heavy spikes past his shoulders, a deeply lined face, red eyes "
               "with three black comma-shaped marks, floor-length plain black robes, and a plain "
               "wooden walking cane he leans on. Reproduce his face, hair and robes exactly. "
               "Ignore Image {i}'s white background and three-view layout. ")

BIND_ZETSU = ("Image {i} is the CREATURE REFERENCE: a humanoid plant creature split vertically "
              "down the middle, the right half chalk white and the left half pure black, with "
              "round yellow pupil-less eyes, a long black cloak, and two halves of a large open "
              "green venus-flytrap shell framing its head. Reproduce it exactly. Ignore Image "
              "{i}'s white background and three-view layout. ")

BIND_GUNBAI = ("Image {i} is the PROP REFERENCE for the war fan: a very large wide rounded war "
               "fan with a deep purple face, a thick black rim, and three large black comma-shaped "
               "marks arranged in a circle at its centre, mounted on a long straight handle that "
               "is wrapped in pale bandages at its base, with a heavy dark iron chain attached to "
               "the end of the handle. Reproduce that object exactly, at the scale of a shield. "
               "Ignore Image {i}'s white background and its isolated floating presentation. ")

BIND_EYE = ("Image {i} is the EYE DESIGN REFERENCE sheet. Use only the THIRD eye in its row: a "
            "deep red iris with three black comma-shaped marks evenly spaced around the pupil. "
            "Reproduce that pattern exactly. Ignore Image {i}'s white background, its row layout "
            "and the other three eyes on the sheet. ")

BIND_ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, carving, colour palette "
            "and lighting exactly. Do not copy its camera angle, and ignore the fact that it is "
            "empty of people. ")

# ------------------------------------------------------------------ lighting
L_MON = ("Lighting: night, cold blue moonlight from above, flat deep shadow, no warm tones "
         "anywhere. ")
L_HIDE = ("Lighting: near-black underground, hard cold rim light picking out edges only, no warm "
          "tones anywhere. ")
L_ACAD = "Lighting: flat unromantic daylight, plain and unglamorous. "

# --------------------------------------------------------------------- pages
# (id, panel-count, description, refs, quality)
PAGES = [
 # ---- beat 1: two years on. age 10, Sharingan permanently active. ----------
 ("p01", 1,
  FULL + BIND_N10 + BIND_ENV.format(i=2) +
  "COMPOSITION: the enormous carved cliff of colossal stone faces at night, seen from a middle "
  "distance and slightly below, with the village a vast field of tiled roofs far below and behind. "
  "Standing on the flat stone top of the leftmost carved head, tiny against the sky, is one small "
  "blond boy in a dark grey training top, arms at his sides, facing out over the village. He is a "
  "very small figure in a very large frame. Keep the entire upper third of the image as calm "
  "uncluttered night sky for a title to be placed later. " + L_MON,
  R("naruto_10", "env_monument"), "medium"),

 ("p02", 3,
  PAGE + BIND_N10 + BIND_EYE.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the ten-year-old boy seen from behind, standing on the narrow flat ledge "
  "along the top of the carved stone heads, the village lights spread out far below him. "
  "PANEL 2 (middle): his face in three-quarter view, close, wind moving his hair, expression "
  "completely blank. "
  "PANEL 3 (bottom, large): an extreme close-up of one of his eyes — a deep red iris with three "
  "black comma-shaped marks around the pupil, held wide open and steady. He no longer switches it "
  "off. " + L_MON, R("naruto_10", "sharingan_progression", "env_monument"), "low"),

 # ---- beat 2: the blood clone's memories arriving all at once -------------
 ("p03", 3,
  PAGE + BIND_N10 + BIND_ZETSU.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the boy in an enormous dark underground training cavern, caught mid-stride and "
  "stopping dead, one hand going to his temple. "
  "PANEL 2 (middle, large): he is down on one knee on the packed earth floor, both hands clamped "
  "over his skull, teeth bared. Around the edges of the panel float four small faint washed-out "
  "ghost images of things that did not happen to him — a school desk, a blackboard, a corridor of "
  "lockers, a ring of laughing children's faces — drawn pale and half-dissolved. "
  "PANEL 3 (wide, bottom): the plant creature has risen halfway out of the solid rock wall behind "
  "him, only its upper body clear of the stone, watching him without moving. " + L_HIDE
  + BALLOONS.format(k="two"), R("naruto_10", "zetsu", "env_hideout_training"), "low"),

 # ---- beat 3: the tablet room, Madara's confession (4pp) ------------------
 ("p04", 3,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, large, top): a wide shot of a small underground stone chamber whose entire far "
  "wall is one enormous ancient stone tablet covered edge to edge in dense carved interlocking "
  "spiral glyphs. The very old man in floor-length black robes stands before it with his back to "
  "us, leaning on his wooden cane. The blond ten-year-old boy is small in the foreground, facing "
  "him. "
  "PANEL 2 (middle): a close study of the carved stone surface itself — dense spirals, cold light "
  "raking across the cut grooves. "
  "PANEL 3 (bottom): the boy's face in close-up, red three-comma eyes, waiting without impatience. "
  + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p05", 3,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "The confession is told through the carvings, not through the men. "
  "PANEL 1 (top): the old man's hand, deeply lined, pressed flat against the carved tablet wall. "
  "PANEL 2 (middle, very large): the carving under his hand has become a picture. Cut into the "
  "same grey stone and in the same carved-groove line style as the glyphs around it is a "
  "bas-relief scene: a young shinobi boy pinned under a collapsed slab of rock in a tunnel, one "
  "whole side of his body crushed beneath it, one arm still reaching upward. Render it as carved "
  "stone relief with hard chiselled edges — stone, not a photograph and not an ordinary "
  "illustration. "
  "PANEL 3 (small, bottom): a tight insert on the blond boy's single red eye, the carved relief "
  "reflected small in it. " + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p06", 4,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top, wide): a second bas-relief cut into the same tablet wall — a ring of ten "
  "identical faceless figures in high-collared full-length cloaks patterned with round cloud "
  "shapes, standing in a circle facing inward. Carved grey stone, hard chiselled grooves. "
  "PANEL 2 (middle left): a carved relief of one wide human eye whose iris is a set of many "
  "concentric circular rings around a small pupil. Stone, not flesh. "
  "PANEL 3 (middle right, small): the blond ten-year-old's face in close-up, listening, his "
  "expression not changing at all. "
  "PANEL 4 (bottom, wide): the very old man in profile against the carved wall, jaw set, both "
  "hands stacked on the head of his cane. " + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p07", 3,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top, large): a third bas-relief cut into the tablet wall — a tall figure in a "
  "high-collared cloak standing with its back to us in front of that same carved wall, occupying "
  "the exact place where the old man's own carved likeness ought to be. Carved grey stone, an "
  "impostor standing in another man's outline. "
  "PANEL 2 (middle): an extreme close-up of the old man's eye — deep red iris, three black "
  "comma-shaped marks, absolutely hard. "
  "PANEL 3 (bottom, large): the blond boy's face front-on. For the first time in the chapter "
  "something moves in it: a flat, cold, entirely adult anger on a ten-year-old face. " + L_HIDE
  + BALLOONS.format(k="three"), R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 # ---- beat 4: the instruction --------------------------------------------
 ("p08", 3,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): a low camera looking up. The very old man has turned to face the boy and "
  "stands dead centre against the enormous carved wall, cane planted, black robes falling straight "
  "to the floor. The angle makes him enormous. "
  "PANEL 2 (middle): the blond boy from behind and below, small in the frame, looking up at him. "
  "PANEL 3 (bottom): the old man's free hand opening slowly, palm upward, offering. " + L_HIDE
  + BALLOONS.format(k="three"), R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 ("p09", 3,
  PAGE + BIND_N10 + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top, large): the old man's face in close-up, lit almost entirely from below by the red "
  "glow of his own eyes, the carved spirals of the tablet wall behind him falling into blackness. "
  "PANEL 2 (middle): the blond ten-year-old in profile, asking a question, perfectly calm. "
  "PANEL 3 (bottom): an extreme close-up of the old man's mouth and jaw — the faintest curl at one "
  "corner. " + L_HIDE + BALLOONS.format(k="three"),
  R("naruto_10", "madara", "env_hideout_tablets"), "low"),

 # ---- beat 5: he chooses the name. two clean pages, no action. ------------
 ("p10", 1,
  FULL + BIND_N10 + BIND_ENV.format(i=2) +
  "COMPOSITION: the old man has gone and the boy is alone in the tablet chamber. The enormous "
  "carved spiral tablet wall fills almost the entire page. The blond ten-year-old stands very "
  "small at the bottom of the frame with his back to us, facing it, arms at his sides. The "
  "polished lower band of the stone throws back a dim distorted reflection of him in which almost "
  "nothing reads except two small burning red points where his eyes are. Absolute stillness — "
  "nothing on this page is moving. " + L_HIDE,
  R("naruto_10", "env_hideout_tablets"), "medium"),

 ("p11", 2,
  PAGE + BIND_N10 + BIND_ENV.format(i=2) +
  "PANEL 1 (small, top): an extreme close-up of the boy's hand, one fingertip following the cut "
  "groove of a single carved spiral. "
  "PANEL 2 (very large, bottom, filling most of the page): his face front-on and close, red eyes "
  "with three black comma marks, hair to just below his ears. He is not angry and not grieving. "
  "Something has simply been decided and will not be revisited. The carved wall stays crisp and "
  "sharp behind him. This is the quietest and most important page in the chapter — hold it "
  "completely still. " + L_HIDE + BALLOONS.format(k="one"),
  R("naruto_10", "env_hideout_tablets"), "medium"),

 # ---- beat 6: the time skip. faceless montage, then the cut. --------------
 ("p12", 5,
  PAGE + BIND_N10 + BIND_ENV.format(i=2) +
  "A time-passing montage strip. No face is visible in any panel on this page — the boy is shown "
  "only as silhouette and as body detail. "
  "PANEL 1 (wide, top): the vast dark underground training cavern; a lone small figure caught in "
  "mid-air between two wooden training posts, rendered as a hard flat black silhouette against the "
  "cold light falling from above. "
  "PANEL 2 (small): a close study of two bare feet planted hard in packed earth, dust lifting. "
  "PANEL 3 (small): a close study of two hands wrapped in dirty bandages gripping a heavy carved "
  "stone weight. "
  "PANEL 4 (small): a bare back seen from behind, shoulders visibly broader than before, cold rim "
  "light raking across worked muscle. Head cropped out of frame. "
  "PANEL 5 (wide, bottom): the same black silhouette again, taller now, standing upright and still "
  "in a field of shattered and splintered training posts. " + L_HIDE,
  R("naruto_10", "env_hideout_training"), "low"),

 ("p13", 1,
  FULL + BIND_N13R + BIND_ENV.format(i=2) +
  "COMPOSITION: three years have passed and this is the first clear look at him. The "
  "thirteen-year-old stands alone in the exact centre of the enormous dark underground training "
  "cavern, full figure, front on, feet apart, arms loose at his sides, looking straight out at the "
  "reader. Blond hair to the shoulders, the right bang hanging low over his right eye; black "
  "long-sleeved shirt with the large red spiral across the chest; black fingerless gloves with a "
  "small red spiral on the back of each hand. His single visible eye is red with three black comma "
  "marks. Cold hard light falls from directly overhead; the cavern drops away into total blackness "
  "on every side. " + L_HIDE, R("naruto_13", "env_hideout_training"), "low"),

 # ---- beat 7: graduation, the forehead protector --------------------------
 ("p14", 3,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (wide, top): the front courtyard of the ninja academy in flat daylight, crowded with "
  "newly graduated students and their parents, everyone talking at once, headbands being tied on, "
  "an ordinary happy noisy afternoon. The blond boy is not in this panel. "
  "PANEL 2 (middle, large): the thirteen-year-old walking out alone through the building's arched "
  "entrance, a plain metal forehead protector on a dark cloth band hanging loose from one gloved "
  "hand. Not one adult in the crowd is looking at him. "
  "PANEL 3 (bottom): seen past his shoulder — a parent crouching to fasten a headband onto a "
  "delighted child's forehead. He is not looking at them either. The other students and parents "
  "are ordinary villagers with dark or brown hair in plain civilian clothes. " + L_ACAD,
  R("naruto_13", "env_academy_ext"), "low"),

 ("p15", 2,
  PAGE + BIND_N13 + BIND_ENV.format(i=2) +
  "PANEL 1 (large, top): an extreme close-up of the metal plate of a forehead protector held flat "
  "on an open black-gloved palm, the small red spiral on the back of the glove visible at the edge "
  "of frame. The polished metal throws back a narrow reflection of one blue eye. "
  "PANEL 2 (wide, bottom): his hand closes around it and lowers, letting the dark cloth band hang "
  "at his side against his black trousers as he walks. He has not put it on and is not going to. "
  + L_ACAD, R("naruto_13", "env_academy_ext"), "low"),

 # ---- beat 8: the Gunbai --------------------------------------------------
 ("p16", 3,
  PAGE + BIND_N13R + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (wide, top): the underground tablet chamber again, the enormous carved spiral wall "
  "behind everything. The very old man is sitting on a low stone bench in front of it. Across his "
  "knees lies a long object wrapped in dark cloth. He looks smaller and far more tired than "
  "before. "
  "PANEL 2 (middle): the thirteen-year-old standing in the chamber's stone doorway, still, his "
  "single visible eye red with three comma marks. "
  "PANEL 3 (bottom): a close study of the old man's hand resting flat on the cloth bundle, not "
  "yet unwrapping it. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_13", "madara", "env_hideout_tablets"), "low"),

 ("p17", 1,
  FULL + BIND_N13R + BIND_MADARA.format(i=2) + BIND_GUNBAI.format(i=3) + BIND_ENV.format(i=4) +
  "COMPOSITION: the handover, shot square-on from the side at eye level. The very old man stands "
  "and holds the enormous purple war fan out horizontally in both hands; the thirteen-year-old has "
  "both gloved hands under it and is taking its full weight, his arms braced for how heavy it is. "
  "The heavy iron chain hangs in a loop between them. The war fan is the largest and brightest "
  "object on the page, its three black comma marks clearly readable. Neither of them is looking at "
  "the fan — they are looking at each other. Behind them, the whole enormous carved spiral tablet "
  "wall. " + L_HIDE + BALLOONS.format(k="one"),
  R("naruto_13", "madara", "gunbai", "env_hideout_tablets"), "medium"),

 ("p18", 3,
  PAGE + BIND_N13R + BIND_MADARA.format(i=2) + BIND_GUNBAI.format(i=3) + BIND_ENV.format(i=4) +
  "PANEL 1 (top): a close study of the boy's black-gloved hands closing around the bandaged base "
  "of the war fan's long handle, testing the weight; the heavy iron chain swinging below. "
  "PANEL 2 (middle): the old man's lined hand comes down and settles on the boy's shoulder. Only "
  "the hand, the sleeve and the boy's shoulder are in frame. "
  "PANEL 3 (bottom, large): the boy's face in close-up, the dark rim of the war fan just clipping "
  "the edge of frame. For one second his blank expression fails him and he looks, briefly, like a "
  "child. " + L_HIDE + BALLOONS.format(k="two"),
  R("naruto_13", "madara", "gunbai", "env_hideout_tablets"), "low"),

 # ---- beat 9: the farewell neither of them names --------------------------
 ("p19", 3,
  PAGE + BIND_N13R + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (top): the old man has already turned away and is lowering himself back down onto the "
  "stone bench, both hands stacked on his cane, taking his own weight very carefully, like "
  "something that hurts. "
  "PANEL 2 (middle): the thirteen-year-old at the chamber threshold with the huge war fan slung "
  "across his back, half turned back toward him. "
  "PANEL 3 (bottom, large): the old man's face in three-quarter view, looking not at the boy but "
  "at the carved wall. Whatever is in that face, he is not going to explain it. " + L_HIDE
  + BALLOONS.format(k="three"), R("naruto_13", "madara", "env_hideout_tablets"), "low"),

 ("p20", 2,
  PAGE + BIND_N13R + BIND_MADARA.format(i=2) + BIND_ENV.format(i=3) +
  "PANEL 1 (small, top): a close-up of the thirteen-year-old's face in the black underground "
  "corridor outside the chamber, stopped mid-step, his single visible red eye shifted fractionally "
  "back the way he came. He has half-noticed something and cannot name it. "
  "PANEL 2 (very large, bottom, filling most of the page): a long shot straight down the vast "
  "black underground stone corridor from just behind the boy's shoulder. At the far end, tiny, "
  "framed in the one lit stone doorway of the tablet chamber, the very old man sits alone on the "
  "bench with both hands on his cane, not looking after him. The corridor between them is enormous "
  "and completely empty. The boy is walking away and does not turn round. Final page of the "
  "chapter — quiet, still, not dramatic. " + L_HIDE,
  R("naruto_13", "madara", "env_hideout_corridor"), "medium"),
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
