"""Volume 2, Chapter 2 — "Entitled to My Secrets". 20 pages.

Applies the Chapter 1 review notes:
  1. EXPLICIT balloon attribution — every balloon names its speaker and its position, because
     tails kept pointing at the wrong character.
  2. NAMED CAST PER PAGE — pages state exactly who is present AND that nobody else appears,
     because Ch1 p18 rendered the wrong two characters walking away.
  3. PACING — scene changes get a transition beat instead of hard-cutting between locations.
     The source is prose and compresses; we are free to expand, and should.
"""
import concurrent.futures as cf
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "refs"))
from genlib import SPLASH, STAGING, STYLE, STYLE_REF, UNIQUE, rep_generate, Ledger  # noqa: E402
import style_select as ss                                                    # noqa: E402

REFS = HERE.parent / "refs" / "images"
OUT = HERE / "v2ch02" / "raw"
LED = Ledger(HERE / "v2ch02" / "ledger.json")
R = lambda *n: [str(REFS / f"{x}.png") for x in n]  # noqa: E731

FILL = ("A single complete manga PAGE, portrait. The block of panels FILLS THE WHOLE PAGE out to a "
        "narrow even margin, separated only by thin white gutters — no broad empty white areas. ")

N13 = ("Image {i} is the CHARACTER REFERENCE for the blond boy: a lean thirteen-year-old whose hair "
       "is LONG — hanging well past his jaw to his shoulders in heavy strands, two thick bangs "
       "framing his face, the right bang low enough to cover his right eye. His hair is never short "
       "and never spiky. Blue eyes, whisker marks nearly faded, blank expression, black long-sleeved "
       "shirt with a large red spiral on the chest, black trousers, dark sandals, black fingerless "
       "gloves with small red spirals. Reproduce exactly; ignore its white background and layout. "
       + UNIQUE + " ")
KAK = ("Image {i} is the CHARACTER REFERENCE for the masked man: tall, lean, spiky silver-grey hair "
       "swept to one side, dark cloth mask covering his face below the nose, slanted forehead "
       "protector covering his left eye so only his right eye shows, dark navy uniform under a green "
       "flak vest. Reproduce exactly; ignore its white background and layout. ")
HIR = ("Image {i} is the CHARACTER REFERENCE for the old leader: he WEARS ON HIS HEAD a tall white "
       "ceremonial hat with a broad brim, a large red front panel bearing one black brush kanji, and "
       "long white cloth drapes over his ears and shoulders. White ceremonial robes over a red "
       "under-robe, white sash, short grey goatee, deeply lined face, long wooden smoking pipe. "
       "Reproduce exactly; ignore its white background and layout. ")
ZET = ("Image {i} is the CREATURE REFERENCE: a humanoid plant creature split vertically, right half "
       "chalk white and left half pure black, round yellow pupil-less eyes, black cloak, green "
       "venus-flytrap shell around its head. Reproduce exactly; ignore its white background. ")
KUR = ("Image {i} is the CHARACTER REFERENCE for the red-eyed woman: late twenties, long wavy black "
       "hair, striking red eyes, a one-piece dress resembling white bandage wrapping with a single "
       "red right sleeve. Reproduce exactly; ignore its white background and layout. ")
YUG = ("Image {i} is the CHARACTER REFERENCE for the purple-haired woman: twenties, very long "
       "straight purple hair past her waist, a slim straight sword across her back, dark navy "
       "uniform under a grey flak vest. Reproduce exactly; ignore its white background and layout. ")
ENV = ("Image {i} is the LOCATION REFERENCE — reuse its architecture, colour palette and lighting. "
       "Do not copy its camera angle; ignore that it is empty of people. ")

def ONLY(*names):
    """Fix #2 — state the complete cast so no stray characters are invented."""
    return (f"The only people anywhere on this page are {', '.join(names)}. No other character "
            f"appears in any panel, in the foreground or the background. ")

L_OFF = "Lighting: warm late-afternoon light slanting through tall arched windows. "
L_DUSK = "Lighting: cool blue dusk. "
L_APT = "Lighting: clean even daylight through a window. "


def OFF(speaker):
    """Mark a speaker who is NOT VISIBLE in that panel.

    v2ch02 p04 showed why this is needed: Naruto's line sat on a Hiruzen-only close-up and the
    model happily grew a tail out of Hiruzen's mouth. Off-panel speech needs an off-panel tail.
    """
    return ("\x00", speaker)


def SAY(*lines):
    """Fix #1 — every balloon names its speaker AND its position in the panel.

    Entries are (panel, speaker_description, where_in_panel, text). Wrap the speaker in OFF(...)
    when they are not drawn in that panel.
    """
    out = ("LETTERING: draw the speech balloons WITH their dialogue written inside, in clean bold "
           "upright English comic lettering, all capitals, correctly spelled. Each balloon must sit "
           "where stated and its TAIL MUST POINT DIRECTLY AT ITS NAMED SPEAKER, clear of every "
           "face. A balloon must never sit nearer to, or point at, any character other than its own "
           "speaker. Use exactly these balloons and no others:\n")
    for panel, speaker, where, text in lines:
        if isinstance(speaker, tuple) and speaker and speaker[0] == "\x00":
            who = speaker[1]
            out += (f'  PANEL {panel} — balloon in the {where}, spoken by {who}, who is NOT DRAWN '
                    f'ANYWHERE IN THIS PANEL. Draw it as an OFF-PANEL balloon: its tail is a short '
                    f'straight spur running to the nearest panel border and stopping there, '
                    f'pointing out of the panel. The tail must NOT touch, overlap or aim at any '
                    f'face or figure that IS drawn in this panel. Reading: "{text}"\n')
        else:
            out += (f'  PANEL {panel} — balloon in the {where}, tail pointing at {speaker}, '
                    f'reading: "{text}"\n')
    out += "Do not write any other text anywhere on the page. "
    return out


BOY = "the blond boy"
MAN = "the masked silver-haired man"
OLD = "the old man in the tall hat"

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="solo", mood="tense", panels=1),
  N13.format(i=1) + ENV.format(i=2) + ONLY("the blond boy") +
  "CHAPTER OPENING SPLASH. A steep low angle from the foot of a long outdoor stone stair: the "
  "Hokage tower rears up and away from the viewer, its broad round red roof cutting a hard diagonal "
  "across the top of the paper, the carved stone faces of the cliff rising behind it. The blond boy "
  "is a small dark figure climbing the stair, well off centre and near the bottom, his back to us, "
  "one shoulder cropped by nothing — he is tiny against the building. A stone balustrade is the "
  "large foreground mass, cropped by the lower left edge of the paper. Late-afternoon sun comes "
  "from behind the tower so the building is a heavy near-silhouette and the stair is in shadow. "
  "Leave the upper right sky broad and quiet. " + L_OFF
  + 'LETTERING: write the chapter title in the quiet upper right sky, in large bold upright English '
    'capitals, correctly spelled, on two lines, reading: "ENTITLED TO / MY SECRETS". Draw no other '
    'text anywhere on the page — no balloons, no sound effects, no numbers, no signature. ',
  R("naruto_13", "env_hokage_office"), "high"),

 ("p02", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + HIR.format(i=1) + N13.format(i=2) + KAK.format(i=3) + ENV.format(i=4)
  + ONLY("the old man in the tall hat", "the blond boy", "the masked silver-haired man") +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (dominant, top): the round office interior. The old man sits behind a paper-buried desk, "
  "small and far away against the tall windows. The blond boy stands near the door in the extreme "
  "foreground, cropped by the bottom edge so only his shoulder and the back of his head show. The "
  "masked man leans against the wall at mid distance, turned three-quarters away. Three clear depths.\n"
  "PANEL 2 (small): the old man's lined face beneath the hat brim, studying.\n"
  "PANEL 3 (small): the boy's face, entirely blank. Flat tone background, no scenery.\n"
  "PANEL 4 (small): the masked man's single visible eye, watching them both.\n"
  "PANEL 5 (small): a hand setting down a long wooden pipe. Object only, no face.\n"
  "PANEL 6 (wide, bottom): the office from behind the old man's chair, the boy small and alone "
  "across the room. " + L_OFF
  + SAY((2, OLD, "upper left", "NARUTO. WHAT HAPPENED TO YOU?"),
        (3, BOY, "upper right", "I DON'T UNDERSTAND THE QUESTION."),
        (6, OLD, "upper left", "LAST WEEK YOU WERE NOT LIKE THIS.")),
  R("hiruzen", "naruto_13", "kakashi", "env_hokage_office"), "medium"),

 ("p03", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + HIR.format(i=2) + ENV.format(i=3)
  + ONLY("the blond boy", "the old man in the tall hat") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the boy in profile, unmoved.\n"
  "PANEL 2 (dominant, upper): a low angle from beside the desk — the old man large in the "
  "foreground cropped by the left edge, the boy small and squared-off across the room, the space "
  "between them dominating the panel.\n"
  "PANEL 3 (small): the old man's eyes narrowing under the hat.\n"
  "PANEL 4 (small): the boy's hand, relaxed at his side. No face.\n"
  "PANEL 5 (narrow letterbox): only the boy's visible eye, cropped by all four edges, flat black.\n"
  "PANEL 6 (wide, bottom): the two of them either side of the desk, the paperwork between them. "
  + L_OFF
  + SAY((1, BOY, "upper right", "MY APPEARANCE, YOU MEAN. AND MY MANNER."),
        (2, OLD, "upper left", "WHY WILL YOU NOT TELL ME?"),
        (5, BOY, "upper right", "IT IS NOT A MATTER OF TRUST."),
        (6, BOY, "lower right", "I SIMPLY DO NOT WISH TO. I THINK I AM ENTITLED TO MY SECRETS.")),
  R("naruto_13", "hiruzen", "env_hokage_office"), "high"),

 ("p04", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + HIR.format(i=1) + N13.format(i=2) + KAK.format(i=3) + ENV.format(i=4)
  + ONLY("the old man in the tall hat", "the blond boy", "the masked silver-haired man") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the old man half-rising, one hand flat on the desk.\n"
  "PANEL 2 (small): the masked man straightening off the wall, alert.\n"
  "PANEL 3 (dominant, middle): the boy, still, in the near foreground turned three-quarters away, "
  "the old man small behind him across the room. The boy is not looking at him.\n"
  "PANEL 4 (small): the old man's face — the exact moment the words land. Flat tone behind.\n"
  "PANEL 5 (small): the masked man's eye, gone completely still.\n"
  "PANEL 6 (wide, bottom): the office silent, the three of them at three different depths. " + L_OFF
  + SAY((1, OLD, "upper left", "EVERYTHING YOU DO, I MUST KNOW OF."),
        (3, BOY, "upper right", "IRONIC, ISN'T IT."),
        (4, OFF(BOY), "lower left", "YOU DISLIKE ME KEEPING THINGS FROM YOU — WHILE YOU HAVE DONE EXACTLY THAT MY WHOLE LIFE."),
        (6, BOY, "upper right", "YOU THOUGHT I WOULD NEVER FIND OUT.")),
  R("hiruzen", "naruto_13", "kakashi", "env_hokage_office"), "high"),

 ("p05", dict(scene="emotional_closeup", light="interior", cast="two", mood="somber", panels=6),
  FILL + N13.format(i=1) + HIR.format(i=2) + ENV.format(i=3)
  + ONLY("the blond boy", "the old man in the tall hat") +
  "SIX panels, uneven. Escalate by cropping tighter, not by adding rendering.\n"
  "PANEL 1 (small): the old man's whole figure, suddenly looking his age, seen from a high angle.\n"
  "PANEL 2 (small): his hands, loose on the desk. No face.\n"
  "PANEL 3 (small): the boy's mouth only, flat.\n"
  "PANEL 4 (small): the old man's eyes, closing.\n"
  "PANEL 5 (narrow letterbox): the boy's visible eye, cropped by all four edges.\n"
  "PANEL 6 (dominant, bottom): the boy small at the bottom of an otherwise almost empty panel, the "
  "office falling away into flat dark tone above him. " + L_OFF
  + SAY((3, BOY, "upper left", "I KNOW ABOUT THE FOX."),
        (4, OLD, "upper right", "...ONLY THAT?"),
        (6, BOY, "upper left", "AND MY MOTHER.")),
  R("naruto_13", "hiruzen", "env_hokage_office"), "medium"),

 ("p06", dict(scene="dialogue", light="interior", cast="two", mood="somber", panels=5),
  FILL + N13.format(i=1) + HIR.format(i=2) + ENV.format(i=3)
  + ONLY("the blond boy", "the old man in the tall hat") +
  "FIVE panels, uneven.\n"
  "PANEL 1 (dominant, top): the boy facing the windows with his back to the old man, the light "
  "behind him, the old man small and seated far away. \n"
  "PANEL 2 (small): the old man's face, stricken.\n"
  "PANEL 3 (small): the boy's profile, hard.\n"
  "PANEL 4 (small): a framed photograph on the office wall, deliberately turned away from camera so "
  "its subject cannot be seen. Object only.\n"
  "PANEL 5 (wide, bottom): the room, the distance between them, the light going amber. " + L_OFF
  + SAY((1, BOY, "upper right", "I ALSO KNOW WHO IS RESPONSIBLE FOR MY BIRTH."),
        (3, BOY, "upper left", "BUT HE WAS NEVER MY FATHER."),
        (5, BOY, "upper right", "THE ONLY PARENT I HAD WAS MY MOTHER.")),
  R("naruto_13", "hiruzen", "env_hokage_office"), "high"),

 ("p07", dict(scene="dialogue", light="interior", cast="two", mood="somber", panels=6),
  FILL + HIR.format(i=1) + N13.format(i=2) + ENV.format(i=3)
  + ONLY("the old man in the tall hat", "the blond boy") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the old man leaning forward, pleading.\n"
  "PANEL 2 (small): the boy, unmoved, cropped tight. Flat tone background.\n"
  "PANEL 3 (dominant, middle): the old man alone in a wide shot of the office, small behind the "
  "enormous desk, the empty chairs and paperwork dwarfing him.\n"
  "PANEL 4 (small): the boy's hand on the door frame.\n"
  "PANEL 5 (small): the old man's face, failing to meet his eyes.\n"
  "PANEL 6 (wide, bottom): the open office door, the boy already a silhouette in the corridor "
  "beyond it. " + L_OFF
  + SAY((1, OLD, "upper left", "I AM SORRY. YOUR FATHER HAD ENEMIES — WE FEARED THEY WOULD COME FOR YOU."),
        (2, BOY, "upper right", "THOSE ARE EXCUSES."),
        (3, OFF(BOY), "lower right", "HAVE YOU FORGOTTEN WHAT THEY DID TO ME ON MY BIRTHDAYS?"),
        (5, OLD, "upper left", "...I AM SORRY I FAILED TO PROTECT YOU."),
        (6, BOY, "upper right", "I NEVER HATED YOU.")),
  R("hiruzen", "naruto_13", "env_hokage_office"), "medium"),

 ("p08", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + HIR.format(i=1) + KAK.format(i=2) + ENV.format(i=3)
  + ONLY("the old man in the tall hat", "the masked silver-haired man") +
  "SIX panels, uneven. The boy has GONE — he must not appear anywhere on this page.\n"
  "PANEL 1 (small): the office door clicking shut. Door only.\n"
  "PANEL 2 (dominant, upper): the old man behind the desk and the masked man standing before it, at "
  "very different scale — the masked man huge in the foreground cropped by the right edge, the old "
  "man small and seated beyond him.\n"
  "PANEL 3 (small): the old man striking a match for his pipe, hands only.\n"
  "PANEL 4 (small): the masked man's single eye, unhappy.\n"
  "PANEL 5 (small): smoke curling in front of the window. No people.\n"
  "PANEL 6 (wide, bottom): the two of them in the darkening office, the empty chair where the boy "
  "stood in the foreground. " + L_OFF
  + SAY((2, OLD, "upper left", "NOTHING WENT WELL. HE ANSWERED NOTHING."),
        (4, MAN, "upper right", "IF HE LEARNS YOU SET ME TO WATCH HIM, HE MAY NEVER FORGIVE YOU."),
        (6, OLD, "upper left", "THAT IS A PRICE I AM WILLING TO PAY FOR THIS VILLAGE.")),
  R("hiruzen", "kakashi", "env_hokage_office"), "medium"),

 ("p09", dict(scene="establishing", light="interior", cast="none", mood="tense", panels=4),
  FILL + ENV.format(i=1) +
  "FOUR panels, uneven. No characters at all and no dialogue on this page.\n"
  "PANEL 1 (small): the emptied office, chairs pushed back, pipe smoke hanging.\n"
  "PANEL 2 (small): a ceiling beam in deep shadow.\n"
  "PANEL 3 (dominant, middle): a corner of the ceiling where the shadow is fractionally wrong — a "
  "shape that is almost, but not quite, part of the woodgrain.\n"
  "PANEL 4 (narrow letterbox, bottom): two round YELLOW EYES open in that darkness, cropped by all "
  "four edges. Nothing else visible. " + L_OFF,
  R("env_hokage_office"), "medium"),

 # --- pacing fix: an explicit transition beat instead of a hard cut between locations ---
 ("p10", dict(scene="establishing", light="day", cast="solo", mood="calm", panels=5),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY("the blond boy") +
  "FIVE panels, uneven. This page exists to MOVE HIM ACROSS THE VILLAGE — the reader must see him "
  "leave one place and arrive at another.\n"
  "PANEL 1 (small): the tower doors from outside, the boy stepping out, small at the base of a "
  "large building.\n"
  "PANEL 2 (small): his sandals on a stone street. No face.\n"
  "PANEL 3 (dominant, middle): a wide village street, the boy walking away from camera, small and "
  "central; townspeople at the edges of frame at different depths, several turned away, none of "
  "them looking at him. \n"
  "PANEL 4 (small): a hand-painted plate beside a stairwell. Object only, no readable writing.\n"
  "PANEL 5 (wide, bottom): a different building entirely — a clean modern apartment block, the boy "
  "climbing an outdoor stair. " + L_DUSK,
  R("naruto_13", "env_village_street"), "low"),

 ("p11", dict(scene="dialogue", light="interior", cast="solo", mood="calm", panels=6),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY("the blond boy and his identical wood clones") +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): a bare new apartment, larger and cleaner than his last. The boy stands "
  "in the middle of the empty floor with a scroll unrolled, and around him THREE identical copies "
  "of himself are carrying furniture — a couch, a table, a chair — at three different depths, one "
  "cropped by the panel edge, none facing camera.\n"
  "PANEL 2 (small): a scroll seal flaring flat white as an object appears from it. Flat background.\n"
  "PANEL 3 (small): two identical hands setting down a table leg.\n"
  "PANEL 4 (small): the boy's face, faintly — very faintly — satisfied.\n"
  "PANEL 5 (small): the clones dissolving into flat pale shapes. No faces.\n"
  "PANEL 6 (wide, bottom): the furnished room, the boy alone in it, the window showing village "
  "rooftops. " + L_APT
  + "Draw a hand-drawn manga sound effect in PANEL 2, a soft 'PON' shape overlapping the seal. ",
  R("naruto_13", "env_shinobi_apartment"), "medium"),

 ("p12", dict(scene="dialogue", light="interior", cast="small_group", mood="calm", panels=6),
  FILL + N13.format(i=1) + YUG.format(i=2) + KUR.format(i=3) + ENV.format(i=4)
  + ONLY("the blond boy", "the purple-haired woman", "the red-eyed woman") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a fist knocking on a door, hand only.\n"
  "PANEL 2 (dominant, upper): the boy opening the door — he is large in the foreground cropped by "
  "the left edge, only his shoulder and jaw visible; the two women stand outside at mid distance, "
  "at different depths, one half-turned.\n"
  "PANEL 3 (small): the purple-haired woman's face, recognising him, surprised.\n"
  "PANEL 4 (small): the red-eyed woman glancing sideways at her companion.\n"
  "PANEL 5 (small): the boy's blank face.\n"
  "PANEL 6 (wide, bottom): the corridor, the two women walking away, the boy's door closing behind "
  "them. " + L_APT
  + SAY((2, "the purple-haired woman", "upper right", "SORRY — WE HEARD NOISE. NOBODY LIVES IN THIS UNIT."),
        (3, "the purple-haired woman", "upper left", "...NARUTO?"),
        (5, BOY, "upper right", "I WAS MOVING FURNITURE."),
        (6, "the red-eyed woman", "upper left", "THEN IT SEEMS WE'RE NEIGHBOURS.")),
  R("naruto_13", "yugao", "kurenai", "env_shinobi_apartment"), "low"),

 ("p13", dict(scene="dialogue", light="interior", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + ZET.format(i=2) + ENV.format(i=3)
  + ONLY("the blond boy", "the split black-and-white plant creature") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the door closing, the room quiet.\n"
  "PANEL 2 (dominant, middle): the boy turning to find the plant creature already sitting on his new "
  "couch as though it lives there — the creature large in the foreground cropped by the right edge, "
  "the boy small across the room.\n"
  "PANEL 3 (small): the creature's split face, grinning.\n"
  "PANEL 4 (small): the boy's face, entirely unsurprised. Flat tone background.\n"
  "PANEL 5 (narrow letterbox): the creature's yellow eyes, cropped by all four edges.\n"
  "PANEL 6 (wide, bottom): the two of them in the furnished room, the window dark now. " + L_APT
  + SAY((2, "the plant creature", "upper left", "YOU WERE RIGHT."),
        (3, "the plant creature", "upper right", "HE DOES NOT TRUST YOU."),
        (4, BOY, "lower left", "I EXPECTED AS MUCH. WHO DID HE SEND?"),
        (6, "the plant creature", "upper right", "YOUR SENSEI.")),
  R("naruto_13", "zetsu", "env_shinobi_apartment"), "high"),

 ("p14", dict(scene="emotional_closeup", light="interior", cast="solo", mood="calm", panels=5),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY("the blond boy") +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the boy at the window, seen from behind, the village lights below.\n"
  "PANEL 2 (small): his reflection in the dark glass, doubled and faint.\n"
  "PANEL 3 (small): his hand flat against the pane.\n"
  "PANEL 4 (narrow letterbox): his visible eye in the reflection, cropped by all four edges.\n"
  "PANEL 5 (dominant, bottom): the boy very small at the bottom of the frame, the enormous dark "
  "window and the sleeping village filling everything above him. " + L_DUSK
  + SAY((3, BOY, "upper left", "LET THEM LOOK."),
        (5, BOY, "upper right", "THEY WILL FIND NOTHING I DO NOT GIVE THEM.")),
  R("naruto_13", "env_shinobi_apartment"), "high"),
]


def build_one(spec):
    pid, want, desc, refs, quality = spec
    dest = OUT / f"{pid}.png"
    if dest.exists():
        return f"[skip] {pid}"
    idx = len(refs) + 1
    stage = SPLASH if want.get("panels") == 1 else STAGING
    prompt = desc + " " + stage + STYLE_REF.format(i=idx) + STYLE
    # Style reference images can themselves trip moderation — walk the ranked candidates.
    lib = sorted(ss.library(), key=lambda r: -ss.score(r, want))[:6]
    img = cost = sref = None
    last = "no style candidates"
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
    return f"[ok]   {pid}  {quality:6} ${cost:.3f}"


if __name__ == "__main__":
    only = sys.argv[1:] or None
    todo = [p for p in PAGES if not only or p[0] in only]
    print(f"building {len(todo)} pages -> {OUT}")
    with cf.ThreadPoolExecutor(max_workers=min(50, len(todo))) as ex:
        for line in ex.map(build_one, todo):
            print(line)
    print(f"\nchapter ledger: ${LED.spent:.3f}")
