"""Volume 4, Chapter 6 — "The Debt". 18 pages.

Source: fic ch09:421-525 and ch10:5-95.  The chapter begins in the Oto
aftermath and ends at sea before the Kiri port, patrol, or rebels appear.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

from runner import run  # noqa: E402
from prompts import R  # noqa: E402
from prompts_v4 import (  # noqa: E402
    CAP,
    ENV,
    FILL,
    GUNBAI_V4,
    JIR,
    KARIN,
    KARIN_SPEAKER,
    N16_ARMOR,
    N16_SPEAKER,
    ONLY,
    SAY,
    SFX,
    TITLE,
    TSUNADE,
    TSUNADE_SPEAKER,
    YUGAO_V4,
    YUGAO_V4_SPEAKER,
    ZET,
)


ZETSU_SPEAKER = "the split white-and-black plant creature"
JIRAIYA_SPEAKER = "the white-haired man with the red face markings"
YOUNG_NARUTO_SPEAKER = "the younger blond child"
N06 = ("Image {i} is the CHARACTER REFERENCE for the younger blond child: about six years old, "
       "small and slight, with short untidy blond hair, faded whisker marks, and a guarded expression. "
       "He wears a plain dark child-sized shirt and shorts. Reproduce exactly; ignore its white "
       "background and layout. ")
EMS = ("Whenever the older blond teen's eyes are visible, they are both six-bladed Mangekyo eyes; "
       "his right eye is normally hidden by the heavy right bang. Never draw a plain blue eye. ")

# Each page declares the reference order once.  B() assigns the prompt's Image indices from that
# order, and _check_pages() verifies the resolved paths before a generation run begins.
REF_ORDER = {
    "p01": ("naruto_v4_armor", "gunbai_v4", "zetsu", "env_oto_broken_exterior"),
    "p02": ("naruto_v4_armor", "gunbai_v4", "zetsu", "env_oto_broken_exterior"),
    "p03": ("naruto_v4_armor", "gunbai_v4", "env_oto_broken_exterior"),
    "p04": ("tsunade", "jiraiya", "env_hokage_office"),
    "p05": ("tsunade", "jiraiya", "naruto_v4_armor", "gunbai_v4", "env_hokage_office"),
    "p06": ("naruto_v4_armor", "gunbai_v4", "zetsu", "karin", "env_valley_of_end"),
    "p07": ("yugao_v4", "env_wave_forest"),
    "p08": ("naruto_v4_armor", "gunbai_v4", "yugao_v4", "env_wave_forest"),
    "p09": ("naruto_v4_armor", "gunbai_v4", "yugao_v4", "env_wave_boat"),
    "p10": ("naruto_v4_armor", "yugao_v4", "env_wave_boat"),
    "p11": ("naruto_v4_armor", "yugao_v4", "env_wave_boat"),
    "p12": ("naruto_06", "yugao_v4", "naruto_v4_armor", "env_konoha_alley"),
    "p13": ("naruto_v4_armor", "yugao_v4", "env_wave_boat"),
    "p14": ("naruto_v4_armor", "yugao_v4", "env_wave_boat", "env_kiri_fogline"),
    "p15": ("naruto_v4_armor", "yugao_v4", "env_wave_boat"),
    "p16": ("naruto_v4_armor", "gunbai_v4", "yugao_v4", "env_wave_boat"),
    "p17": ("naruto_v4_armor", "yugao_v4", "env_wave_boat"),
    "p18": ("naruto_v4_armor", "gunbai_v4", "yugao_v4", "env_wave_boat", "env_kiri_fogline"),
}

REF_BINDING = {
    "naruto_v4_armor": N16_ARMOR + EMS,
    "gunbai_v4": GUNBAI_V4,
    "zetsu": ZET,
    "tsunade": TSUNADE,
    "jiraiya": JIR,
    "karin": KARIN,
    "yugao_v4": YUGAO_V4,
    "naruto_06": N06,
    "env_oto_broken_exterior": ENV,
    "env_hokage_office": ENV,
    "env_valley_of_end": ENV,
    "env_wave_forest": ENV,
    "env_wave_boat": ENV,
    "env_konoha_alley": ENV,
    "env_kiri_fogline": ENV,
}


def B(page_id):
    """Bind prompt images in exactly the same order as R() receives them."""
    return "".join(REF_BINDING[key].format(i=index)
                   for index, key in enumerate(REF_ORDER[page_id], start=1))


def RR(page_id):
    return R(*REF_ORDER[page_id])


L_OTO = "Lighting: flat ash-grey aftermath light, smoke and dust separated into hard-edged shapes. "
L_OFFICE = "Lighting: quiet warm window light across a scarred desk and open office window. "
L_VALLEY = "Lighting: hard overcast daylight over the two colossal Valley of the End statues and river. "
L_WAVE = "Lighting: rain-dark overcast forest light, wet branches and leaves with crisp black contour lines. "
L_SEA = "Lighting: cold blue-grey open-sea daylight, hard wave shadows, no soft glow. "


PAGES = [
    ("p01", dict(scene="aftermath_splash", light="overcast", cast="two", mood="spent", panels=1),
     B("p01") + ONLY(N16_SPEAKER, ZETSU_SPEAKER) +
     "CHAPTER OPENING SPLASH. Wide low horizon across the collapsed Oto exterior. The older blond "
     "teen is small at the lower right, kneeling into the broad purple war fan for support; his red "
     "armour is scuffed and the same shoulder plate broken in the preceding chapter is visibly gone, but there is no injury "
     "detail. Broken earth, black smoke columns, and the "
     "collapsed base fill the rest of the page. The split-faced plant creature rises far behind him, "
     "partly cropped by the page edge. The upper third is a quiet smoke shelf for the title. Cost, "
     "not victory. " + L_OTO + TITLE("THE DEBT", "quiet upper-third smoke shelf"),
     RR("p01"), "high"),

    ("p02", dict(scene="dialogue", light="overcast", cast="two", mood="controlled", panels=4),
     FILL + B("p02") + ONLY(N16_SPEAKER, ZETSU_SPEAKER) +
     "FOUR uneven panels, with the third panel dominant and no aligned grid. PANEL 1 (small): a crack "
     "in broken stone, the split face and yellow eyes of the plant creature emerging from it. PANEL 2 "
     "(narrow): the older blond teen straightening, breath measured, his red armour scarred with the "
     "same shoulder plate still visibly broken away. "
     "PANEL 3 (dominant): he re-straps the purple war fan across his back against the ruined exterior, "
     "while the plant creature remains low at a different depth. PANEL 4 (narrow close-up): his visible "
     "eye, cold and decisive. " + L_OTO +
     SAY((1, ZETSU_SPEAKER, "upper left", "KARIN WAS MOVED. THE OTHER HIDEOUTS REMAIN."),
         (3, N16_SPEAKER, "upper right", "THEN WE FIND HER. AND THE MASK.")),
     RR("p02"), "high"),

    ("p03", dict(scene="montage", light="overcast", cast="solo_with_extras", mood="relentless", panels=5),
     FILL + B("p03") + ONLY(N16_SPEAKER, "small unnamed fleeing guard silhouettes") +
     "FIVE uneven montage panels; only the armoured teen and small unnamed guard silhouettes appear. "
     "PANEL 1 (small): a distant Oto base observed through reeds. PANEL 2 (tall): the older blond teen "
     "in red armour crossing its threshold, gunbai on his back. PANEL 3 (small): an empty warning bell "
     "swinging above an abandoned passage. PANEL 4 (dominant): a different base collapsing into dust, "
     "with tiny faceless guards fleeing far from the impact; no bodies or injury detail. PANEL 5 (wide): "
     "multiple smoke columns across the horizon imply eight different sites without repeating eight "
     "identical panels. " + L_OTO + CAP(5, "upper left", "EIGHT HIDEOUTS FELL. KARIN WAS FOUND. THE MASK WAS NOT."),
     RR("p03"), "high"),

    ("p04", dict(scene="office_dialogue", light="warm", cast="two", mood="grave", panels=4),
     FILL + B("p04") + ONLY(TSUNADE_SPEAKER, JIRAIYA_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): time card over the quiet Hokage office. PANEL 2 (small): the "
     "blonde woman in the green haori looks up from the desk. PANEL 3 (dominant): over-shoulder depth "
     "stagger, her shoulder large in the foreground, the white-haired man small at the open broken window, "
     "and the desk separating them; his serious expression removes all comedy. PANEL 4 (wide): the office "
     "holds a heavy silence after his report. " + L_OFFICE +
     CAP(1, "upper left", "ONE WEEK LATER — KONOHA.") +
     SAY((3, JIRAIYA_SPEAKER, "upper right", "EIGHT OF OROCHIMARU'S HIDEOUTS FELL IN ONE DAY.")),
     RR("p04"), "high"),

    ("p05", dict(scene="report_reaction", light="warm", cast="two", mood="recognition", panels=4),
     FILL + B("p05") + ONLY(TSUNADE_SPEAKER, JIRAIYA_SPEAKER) +
     "FOUR uneven panels. The only people physically present are the blonde woman and the white-haired "
     "man; all report inserts are cropped non-human object or feature fragments, never Naruto physically "
     "in Konoha. PANEL 1 (small report inset): scarred bright red segmented armour and the edge of a black "
     "under-suit. PANEL 2 (small report inset): the broad dark-purple war fan, handle and chain. PANEL 3 "
     "(dominant): the blonde woman's close-up as the report describes long blond hair over a right eye and "
     "a red Mangekyo eye; the recognition lands on her face. PANEL 4 (narrow): her mouth saying the name. "
     + L_OFFICE +
     SAY((2, JIRAIYA_SPEAKER, "upper left", "RED ARMOUR. A WAR FAN. LONG BLOND HAIR. SHARINGAN."),
         (4, TSUNADE_SPEAKER, "upper right", "NARUTO.")),
     RR("p05"), "high"),

    ("p06", dict(scene="valley_departure", light="overcast", cast="three", mood="guarded", panels=6),
     FILL + B("p06") + ONLY(N16_SPEAKER, ZETSU_SPEAKER, KARIN_SPEAKER) +
     "SIX uneven panels. PANEL 1 (wide establishing): the Valley of the End statues under hard overcast "
     "light; the older blond teen stands high on Madara's statue, while the red-haired girl with glasses "
     "and the plant creature stand at a lower depth. PANEL 2 (small): the girl's fully clothed wary face, "
     "not objectified, as she senses his chakra. PANEL 3 (narrow symbolic insert): hard-edged black chakra "
     "shapes hold one small clear white core; no creature or romance imagery. PANEL 4 (dominant): the teen "
     "faces her directly but keeps a respectful distance while naming his mother. PANEL 5: he promises "
     "protection and eventual safety in Konoha; she remains cautious rather than instantly affectionate. "
     "PANEL 6 (wide): he directs the plant creature toward the forest; the girl and plant creature depart "
     "together while the teen remains alone above the river. " + L_VALLEY +
     SAY((1, N16_SPEAKER, "upper left", "THE MASK WAS NOT THERE."),
         (2, KARIN_SPEAKER, "upper right", "YOUR CHAKRA... SO DARK. BUT THERE IS LIGHT INSIDE IT."),
         (4, N16_SPEAKER, "middle left", "MY MOTHER WAS AN UZUMAKI."),
         (5, N16_SPEAKER, "middle right", "YOU ARE UNDER MY PROTECTION. WHEN IT IS SAFE, I WILL TAKE YOU TO KONOHA."),
         (6, N16_SPEAKER, "lower right", "ZETSU. TAKE KARIN TO THE HIDEOUT.")),
     RR("p06"), "high"),

    ("p07", dict(scene="forest_escape", light="rain", cast="solo_with_extras", mood="exhausted", panels=5),
     FILL + B("p07") + ONLY(YUGAO_V4_SPEAKER, "distant unnamed attacker silhouettes") +
     "FIVE uneven panels. The only visible people are the purple-haired Leaf kunoichi and distant faceless "
     "attacker silhouettes. PANEL 1 (small): time card over rain-dark forest. PANEL 2 (small): a broken "
     "branch under a sandal. PANEL 3 (narrow): dark staining on a sleeve only, no wound close-up. PANEL 4 "
     "(small): distant pursuit glimpsed as faceless silhouettes through wet trees. PANEL 5 (dominant "
     "vertical): her strength fails high among branches and she falls, reaching for a branch just beyond "
     "her hand. Do not show squadmates or explicit injuries. " + L_WAVE +
     CAP(1, "upper left", "ONE WEEK LATER — OUTSIDE WAVE COUNTRY.") +
     CAP(2, "upper right", "ON A MISSION IN WAVE COUNTRY.") +
     CAP(4, "upper right", "AMBUSHED BY A-RANK MISSING-NIN."),
     RR("p07"), "high"),

    ("p08", dict(scene="rescue", light="rain", cast="two", mood="sudden", panels=2),
     FILL + B("p08") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "TWO deliberately unequal panels. PANEL 1 (narrow top): the purple-haired kunoichi falls through "
     "rain-dark branches, tiny against the immense wet forest. PANEL 2 (dominant): from a distant, non-body-"
     "focused angle, the red-armoured older blond teen catches her securely mid-fall; his face is mostly "
     "hidden by the long right bang and camera angle, and the gunbai is carried on his back. She is limp, "
     "fully clothed, and framed as an injured professional rescued from danger. No wound close-up or intimate "
     "contact. " + L_WAVE + SFX(2, "SHUN", "Hard speed lines between branches."),
     RR("p08"), "high"),

    ("p09", dict(scene="boat_wake", light="sea", cast="three", mood="uneasy", panels=4),
     FILL + B("p09") + ONLY(N16_SPEAKER, "an identical shadow clone of the older blond teen", YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (wide establishing): the small boat alone on open water, visibly holding "
     "the original armoured teen, his identical clone at the tiller, and the purple-haired kunoichi under a "
     "blanket. PANEL 2 (small): her bandaged hands and forearms grip the blanket; only ordinary loose travel "
     "clothes and non-intimate bandaging are visible. PANEL 3 (dominant): she sits upright and takes in too "
     "much open water; the clone steers at the rear, original Naruto sits forward with the gunbai beside him. "
     "PANEL 4 (narrow): original Naruto looks toward the horizon, not at her. " + L_SEA +
     CAP(1, "upper left", "TWO NIGHTS LATER — AT SEA.") +
     SAY((4, N16_SPEAKER, "upper right", "YOU ARE FINALLY AWAKE.")),
     RR("p09"), "high"),

    ("p10", dict(scene="recognition", light="sea", cast="two", mood="distance", panels=4),
     FILL + B("p10") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): blond hair with the heavy right bang. PANEL 2 (small): the "
     "visible red Mangekyo eye, then the faint Leaf protector in the same cropped read. PANEL 3 (dominant): "
     "a full two-shot across the small boat, with a broad empty sky shelf between them to make the distance "
     "inside the boat visible. PANEL 4 (narrow): the purple-haired kunoichi's wide-eyed recognition. "
     + L_SEA +
     SAY((3, YUGAO_V4_SPEAKER, "upper left", "NARUTO?"),
         (4, YUGAO_V4_SPEAKER, "upper right", "HOW LONG WAS I OUT?"),
         (3, N16_SPEAKER, "lower right", "TWO NIGHTS.")),
     RR("p10"), "high"),

    ("p11", dict(scene="medical_question", light="sea", cast="two", mood="relief", panels=4),
     FILL + B("p11") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): a folded spare travel shirt and a clean bandage roll on the boat "
     "floor; no flashback and no clothing change. PANEL 2 (small): the purple-haired kunoichi's bandaged "
     "forearm, fully clothed and composed. PANEL 3 (dominant): she asks from one side of the gunwale while "
     "the armoured teen looks away toward the sea, care presented as ordinary medical necessity. PANEL 4 "
     "(narrow): her quieter relief, not embarrassment. " + L_SEA +
     SAY((3, YUGAO_V4_SPEAKER, "upper left", "DID YOU BANDAGE ME?"),
         (3, N16_SPEAKER, "upper right", "YES.")),
     RR("p11"), "high"),

    ("p12", dict(scene="memory_fragments", light="sea", cast="two_with_memory", mood="unsettling", panels=5),
     FILL + B("p12") + ONLY(YOUNG_NARUTO_SPEAKER, N16_SPEAKER, YUGAO_V4_SPEAKER,
                             "an unnamed ANBU guard shown only as a gloved shoulder and hand in memory",
                             "an unnamed hostile adult shown only as an off-frame shadow in memory") +
     "FIVE uneven panels. PANEL 1 (dominant present): the purple-haired kunoichi thanks the armoured teen "
     "across the boat; his face stays closed. PANEL 2 (narrow memory fragment): a much younger blond child, "
     "small behind an unnamed ANBU guard's shoulder in a Konoha alley. PANEL 3 (narrow memory fragment): a "
     "gloved hand blocks a hostile adult only seen as an off-frame shadow; no detailed violence and no text. "
     "PANEL 4 (small present): Yugao realizes what he remembers. PANEL 5 (close-up): Naruto's visible eye "
     "is blank, not softened. Memory fragments use flat hard-edged grey-blue printing, not glow. " + L_SEA +
     SAY((1, YUGAO_V4_SPEAKER, "upper left", "THANK YOU FOR SAVING ME."),
         (5, N16_SPEAKER, "upper right", "IF YOU WERE SOMEONE ELSE, I WOULD HAVE LEFT YOU THERE.")),
     RR("p12"), "high"),

    ("p13", dict(scene="debt_explained", light="sea", cast="two", mood="precise", panels=4),
     FILL + B("p13") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): the two gunwales create a hard visual divider between them. "
     "PANEL 2 (small): Yugao's wary question. PANEL 3 (dominant): Naruto sits on the forward side of the "
     "divider, face level and closed, while Yugao remains on the other; this is personal reciprocity, not "
     "reconciliation with the village. PANEL 4 (narrow): Yugao absorbs the boundary in silence. " + L_SEA +
     SAY((2, YUGAO_V4_SPEAKER, "upper left", "EVEN IF I WERE KONOHA?"),
         (3, N16_SPEAKER, "upper right", "THAT WOULD NOT MATTER. YOU HELPED ME WHEN I WAS A CHILD.")),
     RR("p13"), "high"),

    ("p14", dict(scene="destination", light="storm_fog", cast="two", mood="unease", panels=4),
     FILL + B("p14") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): Yugao turns from open water to ask. PANEL 2 (small): Naruto's "
     "unmoving profile, no port or land. PANEL 3 (dominant): the small boat crosses dark water "
     "toward a distant wall of pale storm-fog at the page edge; it is only an offshore fogline, never a gate, patrol, "
     "or settlement. PANEL 4 (narrow): Yugao grips the gunwale as the political danger lands. " + L_SEA +
     SAY((1, YUGAO_V4_SPEAKER, "upper left", "WHERE ARE WE GOING?"),
         (2, N16_SPEAKER, "upper right", "KIRIGAKURE."),
         (4, YUGAO_V4_SPEAKER, "upper left", "IT IS IN THE MIDDLE OF A CIVIL WAR. I HAVE TO REPORT BACK."),
         (3, N16_SPEAKER, "lower right", "KONOHA CAN WAIT. LEAVE WHEN WE REACH KIRI.")),
     RR("p14"), "high"),

    ("p15", dict(scene="test", light="storm_fog", cast="two", mood="foreboding", panels=3),
     FILL + B("p15") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "THREE strongly unequal panels. PANEL 1 (dominant): Naruto at the prow in red armour, expression nearly "
     "unchanged, the sea and distant offshore fogline empty behind him. PANEL 2 (tall side panel): Yugao "
     "gives a small, deliberate nod that she will continue to Kiri, then asks her question as the boat tilts "
     "in the swell. PANEL 3 (narrow): water slaps the hull below the gunwale. "
     + L_SEA +
     SAY((2, YUGAO_V4_SPEAKER, "upper left", "WHY GO THERE?"),
         (1, N16_SPEAKER, "upper right", "I AM GOING TO TEST A FEW THINGS.")),
     RR("p15"), "high"),

    ("p16", dict(scene="crossing_fragments", light="sea", cast="two", mood="observant", panels=5),
     FILL + B("p16") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FIVE uneven conversation fragments, not a continuous interview. PANEL 1 (small): time card beside the "
     "oar and tiller. PANEL 2 (small): Yugao asks across a calm stretch of water. PANEL 3 (small): Naruto "
     "answers without looking back. PANEL 4 (dominant vertical): a sudden broad wave rears beside the boat; "
     "Yugao braces herself, while Naruto is merely annoyed and steady. PANEL 5 (narrow): the gunbai rests "
     "silent beside him. Naruto never asks about Konoha. " + L_SEA +
     CAP(1, "upper left", "LATER ON THE CROSSING.") +
     SAY((2, YUGAO_V4_SPEAKER, "upper left", "WHERE HAVE YOU BEEN?"),
         (3, N16_SPEAKER, "upper right", "TRAINING SOMEWHERE SAFE.")) +
     SFX(4, "WHOOOSH", "Spray is hard-edged graphic shapes, not a glow."),
     RR("p16"), "high"),

    ("p17", dict(scene="observation", light="sea", cast="two", mood="loaded", panels=4),
     FILL + B("p17") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "FOUR uneven panels. PANEL 1 (small): red armour resting at the prow, not heroic display. PANEL 2 "
     "(small): Naruto's steady hand on the gunwale during a dangerous swell. PANEL 3 (dominant): Yugao "
     "observes him across the pitching boat, recognizing that he does not panic. PANEL 4 (narrow close-up): "
     "her cautious invocation meets his hard refusal. Do not explain or resolve any Minato conflict. " + L_SEA +
     SAY((4, YUGAO_V4_SPEAKER, "upper left", "YOUR FATHER—"),
         (4, N16_SPEAKER, "upper right", "DO NOT CALL HIM THAT.")),
     RR("p17"), "high"),

    ("p18", dict(scene="closing_hook", light="fog", cast="two", mood="fixed", panels=2),
     FILL + B("p18") + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
     "TWO unequal panels. PANEL 1 (dominant wide): the small boat approaches a wall of pale fog across the "
     "entire horizon; Kiri remains completely unseen. PANEL 2 (small final): from behind Yugao, Naruto stands "
     "at the prow in red armour, gunbai silhouetted against the fog, fixed on what waits ahead. No landfall, "
     "gate, patrol, Ao, Mei, rebel camp, violence, or other Kiri figure appears. " + L_SEA +
     CAP(2, "upper left", "HE IS GOING TO TEST HIMSELF."),
     RR("p18"), "high"),
]


def _check_pages():
    expected_ids = [f"p{number:02d}" for number in range(1, 19)]
    actual_ids = [page[0] for page in PAGES]
    assert actual_ids == expected_ids, actual_ids
    assert len(PAGES) == 18
    for page_id, _style, description, refs, quality in PAGES:
        assert quality == "high", (page_id, quality)
        assert tuple(pathlib.Path(ref).stem for ref in refs) == REF_ORDER[page_id], page_id
        for index in range(1, len(refs) + 1):
            assert f"Image {index} is" in description, (page_id, index)


if __name__ == "__main__":
    _check_pages()
    run(PAGES, HERE / "v4ch06" / "raw", HERE / "v4ch06" / "ledger.json")
