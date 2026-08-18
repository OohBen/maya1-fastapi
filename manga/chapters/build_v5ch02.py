"""Volume 5, Chapter 2 — "Peace". 16 pages.

Source: fic ch12:127-281. Translated 1:1 from story/volume_05/drafts/ch02_peace.md —
103 balloons and one chapter marker across 16 pages, 101 panels. Reading order is
RIGHT TO LEFT per the approved `name`; every page states it.

This builder must match the `name`, not improve on it. Every balloon below is the draft's
exact final text, in the draft's exact panel and position. No line is reworded, shortened
or merged.

Zetsu does not appear anywhere in this chapter, so the ZOR mirror-lock constant is
deliberately absent.

Reference gaps recorded for the owner (never invented here): there is no dedicated Kiri
lodging-room plate, so env_shinobi_apartment carries Naruto's rented room; and there is no
dedicated "quiet Kiri training ground with one isolated tree" plate, so
env_kiri_moonlit_hill is re-purposed under daylight and the tree is described in prose.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, FILL, OFF, ONLY, R, SAY  # noqa: E402
from prompts_v4 import (KIRI_REBELS, MEI_V4, N16_ARMOR, N16_BLACK, SUSA_FINAL,  # noqa: E402
                        YUGAO_V4, MEI_V4_SPEAKER, N16_SPEAKER, YUGAO_V4_SPEAKER)

RTL = ("READING ORDER IS RIGHT TO LEFT, top to bottom: PANEL 1 is the TOP RIGHT panel and the "
       "sequence flows right-to-left before dropping a row. Balloon order follows the same flow. ")
BOY16 = N16_SPEAKER
YUG = YUGAO_V4_SPEAKER
MEI = MEI_V4_SPEAKER

# Two mutually exclusive costume states for the same teen. Pages 1-3 are the night room, where the
# armour is off; from page 4 he is dressed and stays dressed.
UNDER = ("On this page the blond teen wears ONLY the fitted black high-neck long-sleeved under-layer "
         "with the small red spiral, black trousers and no footwear detail: no red armour on his "
         "body, no gunbai, no sword and no forehead protector. He shows no injury, no bandage and "
         "no recovery posture. ")
REPAIRED = ("On this page the blond teen wears his bright red segmented armour, clean and fully "
            "repaired — no cracks, no scorch marks, no dust and no battle damage. He walks and "
            "stands normally, with no injury, no bandage and no recovery posture. ")
ARMOUR_PROP = ("Image {i} shows the same blond teen wearing his bright red segmented samurai "
               "armour. On THIS page that image is a PROP REFERENCE ONLY: copy the armour's red "
               "segmented plates, their colour and their fittings for the FOLDED ARMOUR resting on "
               "the chair. The figure in that image is NOT a second person and must not be drawn "
               "anywhere on this page. ")
EMS_OFF = ("His visible left eye is an ordinary blue eye on this page: no red iris, no tomoe and no "
           "six-bladed pattern in either eye. ")
CROWD = ("The Kiri workers, shinobi, civilians and children are unnamed and non-recurring, and they "
         "wear NO forehead protectors, NO headband plates and NO village symbols of any kind. ")
NOWRITE = ("Every scrap of paperwork, every document, every banner and every sign anywhere on this "
           "page carries ILLEGIBLE SCRIBBLE, not readable words. ")

ENV_ROOM = ("Image {i} is the LOCATION REFERENCE for the plain rented Kiri lodging room — reuse its "
            "walls, window, floorboards, simple furniture and colour palette. Do not copy its "
            "camera angle; ignore that it is empty of people. ")
ENV_STREET = ("Image {i} is the LOCATION REFERENCE for the rebuilding Kiri street beneath the "
              "repaired tower — reuse its architecture, scaffolding, wet stone and colour palette. "
              "Do not copy its camera angle; ignore that it is empty of people. ")
ENV_GROUND = ("Image {i} is the LOCATION REFERENCE for open ground above Kiri — reuse its grass, "
              "bare slope, horizon line and colour palette, but re-light it as ordinary daylight "
              "rather than night. On this page it is an EMPTY DISUSED TRAINING GROUND with ONE "
              "isolated tree; do not copy its camera angle and ignore that it is empty of people. ")

L_NIGHT = "Lighting: cold blue night interior, one low lamp, deep flat shadows on plain walls. "
L_MORN = "Lighting: pale grey-white morning light through one window, flat and undramatic. "
L_KIRI = "Lighting: clean pale mist-filtered daylight over a village that is still rebuilding. "
L_OPEN = ("Lighting: soft overcast daylight on open ground above the village, flat light, no hard "
          "sun and no long shadows. ")

PAGES = [
 # ---- Spread 1: Yugao enters, then cannot answer -------------------------------------
 ("p01", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ARMOUR_PROP.format(i=3)
  + ENV_ROOM.format(i=4) + ONLY(BOY16, YUG) + UNDER + EMS_OFF +
  "SIX panels. A night room conversation that begins the moment she opens the door.\n"
  "PANEL 1 (top band, full page width, the top third of the page): wide night interior — the blond "
  "teen lies awake across the bed at frame left, head toward frame right, eyes on the closed door "
  "at far right. His repaired red armour is FOLDED on a chair beside the bed. PROTECT the upper "
  "left quarter of this panel as a plain unbroken wall: no figure, furniture, shadow edge, effect, "
  "texture or balloon may enter that lettering-safe negative space, and it carries only the chapter "
  "marker. The knock is implied by his eye-line and is NOT lettered.\n"
  "PANEL 2 (middle right, one third width): medium doorway shot — the purple-haired kunoichi enters "
  "from the right moving left and closes the door behind her with her left hand; the teen's head is "
  "visible at lower left, watching her.\n"
  "PANEL 3 (middle centre, one third width): medium close-up — she stands centred facing left "
  "toward him, her right hand still on the latch behind her; their eye-lines meet across the panel "
  "boundary.\n"
  "PANEL 4 (middle left, one third width): close-up — the teen has pushed himself upright at frame "
  "right and faces left toward her; he does not otherwise move.\n"
  "PANEL 5 (bottom right, half width): close reaction — she occupies the right facing left, "
  "shoulders pausing, eyes widening toward him outside the panel.\n"
  "PANEL 6 (bottom left, half width): tight profile — the teen sits at right facing left, eye-line "
  "steady on her. " + L_NIGHT
  + 'LETTERING: in the protected plain wall area of PANEL 1, write the chapter marker in bold '
    'upright English capitals on one line: "CHAPTER 2 — PEACE". It is a tail-less title marker, '
    'not a balloon. '
  + SAY((1, BOY16, "upper right", "IT'S OPEN."),
        (2, BOY16, "upper right", "YOU FOUND ME QUICKLY."),
        (3, YUG, "upper centre", "I AM A SENSOR."),
        (4, BOY16, "upper left", "A GOOD ONE."),
        (5, YUG, "upper right", "WAS THAT PRAISE?"),
        (6, BOY16, "upper left", "AN OBSERVATION."))
  + "In PANEL 2 the balloon belongs to the BLOND TEEN, whose head is visible at the lower left of "
    "that panel: its tail must run down-left to HIS mouth and must not point at the kunoichi, whose "
    "mouth is closed there. The chapter marker specified above is the only other text on this page. ",
  R("naruto_v4_black", "yugao_v4", "naruto_v4_armor", "env_shinobi_apartment"), "high"),

 ("p02", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ENV_ROOM.format(i=3)
  + ONLY(BOY16, YUG) + UNDER + EMS_OFF +
  "SEVEN panels. The relationship scene takes its turns and she deflects the direct question.\n"
  "PANEL 1 (top right, one third width): medium-long side shot — the kunoichi crosses from right to "
  "left and sits at the far left end of the bed, keeping one full body-length between herself and "
  "the teen at right; both face inward.\n"
  "PANEL 2 (top centre, one third width): tight close-up — the teen at right faces left and studies "
  "her.\n"
  "PANEL 3 (top left, one third width): medium close-up — she faces right toward him, her eye-line "
  "dropping briefly to his hands.\n"
  "PANEL 4 (middle band, full width): balanced two-shot — she sits at left facing right and he sits "
  "at right facing left; the empty bedspread forms a visual gulf between them while their eye-lines "
  "meet.\n"
  "PANEL 5 (bottom right, one third width): SILENT insert close-up — her right hand tightens "
  "against the blanket and drags the fabric left. NO faces are visible and no text appears in this "
  "panel.\n"
  "PANEL 6 (bottom centre, the focal panel): tight frontal close-up — the teen is centred facing "
  "forward, but his eyes angle left toward her; he remains completely still.\n"
  "PANEL 7 (bottom left, narrow): full-figure reaction — she rises sharply at left, body turning "
  "toward the door off-panel right while her eyes avoid him behind her. " + L_NIGHT
  + SAY((1, YUG, "upper right", "I CAME TO CHECK ON YOU."),
        (2, BOY16, "upper centre", "YOU WERE AT THE CRATER."),
        (3, YUG, "upper left", "THEN I CAME TO SEE YOU."),
        (4, BOY16, "upper right", "YOU SEEK ME OUT WHENEVER I AM ALONE."),
        (6, BOY16, "upper centre", "ARE YOU INTERESTED IN ME, YUGAO?"),
        (7, YUG, "upper left", "WHEN ARE WE LEAVING KIRI?")),
  R("naruto_v4_black", "yugao_v4", "env_shinobi_apartment"), "low"),

 # ---- Spread 2: other business, then governing ---------------------------------------
 ("p03", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=8),
  FILL + RTL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ENV_ROOM.format(i=3)
  + ONLY(BOY16, YUG) + UNDER + EMS_OFF +
  "EIGHT panels. He answers her practical question and refuses to lose her unanswered one.\n"
  "PANEL 1 (top right, one third width): medium shot matching the previous page's final angle — she "
  "stands at left facing the door to the right; he remains seated at far right behind her and looks "
  "toward her back.\n"
  "PANEL 2 (top centre, one third width): tight profile two-shot — he sits at right facing left; "
  "she keeps her back three-quarters to him at left but turns one eye right.\n"
  "PANEL 3 (top left, one third width): close reaction — she faces right over her shoulder, her "
  "eye-line now meeting his.\n"
  "PANEL 4 (middle right, one third width): close-up — he faces left and holds her gaze; he gives "
  "away no destination.\n"
  "PANEL 5 (middle centre, one third width): medium shot — she crosses right toward the door and "
  "places her hand on the latch; her body faces right while her eyes look back left.\n"
  "PANEL 6 (middle left, one third width): tight face close-up — he faces left toward her; his "
  "visible eye and mouth remain in frame and he does not move.\n"
  "PANEL 7 (bottom right, half width): diagonal two-shot — she stands at the door on the right "
  "facing right, hand on the latch; he sits deep at left facing her.\n"
  "PANEL 8 (bottom left, half width): medium doorway shot — she opens the door toward the reader "
  "and moves right through it, looking left at him one last time while he stays seated in the far "
  "background. " + L_NIGHT
  + SAY((1, BOY16, "upper right", "JIRAIYA WILL ARRIVE IN A FEW DAYS."),
        (2, BOY16, "upper centre", "YOU WILL RETURN WITH HIM."),
        (3, YUG, "upper left", "AND YOU?"),
        (4, BOY16, "upper right", "I HAVE OTHER BUSINESS."),
        (5, YUG, "upper centre", "HOW LONG BEFORE YOU RETURN TO KONOHA?"),
        (6, BOY16, "upper left", "WHY?"),
        (7, YUG, "upper right", "I SHOULD LET YOU REST."),
        (7, BOY16, "lower left", "THAT WAS NOT AN ANSWER."),
        (8, YUG, "upper left", "NEITHER WAS YOURS.")),
  R("naruto_v4_black", "yugao_v4", "env_shinobi_apartment"), "low"),

 ("p04", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + MEI_V4.format(i=1) + N16_ARMOR.format(i=2) + ENV_ROOM.format(i=3)
  + ONLY(MEI, BOY16) + REPAIRED + EMS_OFF + NOWRITE +
  "SIX panels. Morning. The new Mizukage is introduced through exhaustion, not a status caption.\n"
  "PANEL 1 (top band, full width): wide morning doorway shot — the teen opens the door at left and "
  "steps back; the auburn-haired woman crosses from right to left past him without waiting, a thick "
  "bundle of paperwork clutched to her chest. His eye-line follows her.\n"
  "PANEL 2 (middle right, the focal panel, filling the right half of the middle band): wide low "
  "angle — she falls face-first from right to left across the bed, arms and papers spreading left; "
  "he remains framed in the doorway at far right, facing her.\n"
  "PANEL 3 (middle left): medium full figure — he stands at right facing left toward her outside "
  "the panel; one hand remains on the open door.\n"
  "PANEL 4 (bottom right, one third width): close reaction — she lifts her face and one eye from "
  "the papers, looking right toward him.\n"
  "PANEL 5 (bottom centre, one third width): insert medium close-up — she raises a thick stack of "
  "paperwork upward with both hands; her face at lower left turns right toward him.\n"
  "PANEL 6 (bottom left, one third width): tight profile — he faces left toward her, unchanged. "
  + L_MORN
  + SAY((1, MEI, "upper right", "DO NOT SAY ANYTHING."),
        (2, MEI, "upper right", "BEING MIZUKAGE IS EXHAUSTING."),
        (3, BOY16, "upper left", "YOU ACCEPTED THE POSITION AFTER A CIVIL WAR."),
        (4, MEI, "upper right", "I FOUGHT FOR THE VILLAGE."),
        (5, MEI, "upper centre", "THIS WAS NOT IN THE SPEECH."),
        (6, BOY16, "upper left", "DELEGATE."))
  + "In PANEL 2 her face is turned sideways against the bedspread: the balloon's tail must reach "
    "HER turned mouth and must not point at the teen in the doorway. ",
  R("mei_v4", "naruto_v4_armor", "env_shinobi_apartment"), "low"),

 # ---- Spread 3: support, then public gratitude ---------------------------------------
 ("p05", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=6),
  FILL + RTL + MEI_V4.format(i=1) + N16_ARMOR.format(i=2) + ENV_ROOM.format(i=3)
  + ONLY(MEI, BOY16) + REPAIRED + EMS_OFF + NOWRITE +
  "SIX panels. He offers real support in his own voice, then immediately refuses intimacy.\n"
  "PANEL 1 (top right, half width): medium on the bed — she sits upright at left facing right with "
  "papers stacked across her knees, pointing at the new pile, while he stands near the door at far "
  "right.\n"
  "PANEL 2 (top left, half width): medium two-shot — he steps one pace left into the room and faces "
  "her at left; she looks up-right at him.\n"
  "PANEL 3 (middle right, half width): close reaction — she turns from left toward right, "
  "surprised, papers lowering, her eye-line rising to him.\n"
  "PANEL 4 (middle left, half width): medium profile — he pivots right toward the door and looks "
  "forward, away from her.\n"
  "PANEL 5 (bottom right, half width): moving medium shot — she swings her feet off the bed and "
  "follows right after him, eye-line fixed on his back, one hand reaching but NOT touching him; he "
  "looks forward as both move right.\n"
  "PANEL 6 (bottom left, half width): doorway two-shot — he stands at right and opens the door "
  "outward, facing right; she stands just behind at left, facing him. NO touch of any kind occurs "
  "anywhere on this page. " + L_MORN
  + SAY((1, MEI, "upper right", "I DID. THEY BROUGHT ME MORE PAPER."),
        (2, BOY16, "upper left", "YOU ARE STRONG. YOU WILL MANAGE."),
        (3, MEI, "upper right", "THAT MAY BE THE KINDEST THING YOU HAVE SAID TO ME."),
        (4, BOY16, "upper left", "DO NOT BECOME ACCUSTOMED TO IT."),
        (5, MEI, "upper right", "STAY. LET ME ENJOY THE MOMENT."),
        (6, BOY16, "upper right", "I WAS LEAVING."),
        (6, MEI, "lower left", "OF COURSE YOU WERE.")),
  R("mei_v4", "naruto_v4_armor", "env_shinobi_apartment"), "low"),

 ("p06", dict(scene="establishing", light="day", cast="crowd", mood="calm", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_STREET.format(i=4)
  + ONLY(BOY16, MEI, "Kiri workers, shinobi, civilians and children rebuilding the street, none of "
         "them named or recurring") + REPAIRED + EMS_OFF + CROWD + NOWRITE +
  "SIX panels. The crowd exposes how differently the two of them define attachment.\n"
  "PANEL 1 (top band, full width, the focal panel, occupying the top third): extreme-wide "
  "rebuilding street — the teen and the auburn-haired woman enter from the right moving left; "
  "civilians and workers occupy both sides with every eye-line turning toward them; she lifts her "
  "right hand leftward while he keeps both arms down.\n"
  "PANEL 2 (middle right, one third width): close-up — he faces left but turns his eyes right "
  "toward her.\n"
  "PANEL 3 (middle centre, one third width): medium on the woman — she walks left and waves up-left "
  "to the crowd; her eyes follow the civilians.\n"
  "PANEL 4 (middle left, one third width): tight profile — he continues left, eye-line on the "
  "workers rather than on her.\n"
  "PANEL 5 (bottom right, half width): medium two-shot — she stands at right facing left and lowers "
  "her waving hand toward him at left; he keeps moving left.\n"
  "PANEL 6 (bottom left, half width): close-up — he is centred facing left, eyes forward. " + L_KIRI
  + SAY((1, MEI, "upper right", "WAVE."),
        (2, BOY16, "upper right", "WHY?"),
        (3, MEI, "upper centre", "BECAUSE THEY LOVE YOU."),
        (4, BOY16, "upper left", "THEY ARE GRATEFUL."),
        (5, MEI, "upper right", "THAT IS OFTEN HOW LOVE BEGINS."),
        (6, BOY16, "upper left", "THEN IT IS IMPRECISE.")),
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_mizukage_tower"), "medium"),

 # ---- Spread 4: construction, departure, destination ---------------------------------
 ("p07", dict(scene="establishing", light="day", cast="crowd", mood="calm", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_STREET.format(i=4)
  + ONLY(BOY16, MEI, "two unnamed former fighters working on opposite scaffolds, and other unnamed "
         "Kiri workers behind them") + REPAIRED + EMS_OFF + CROWD + NOWRITE +
  "SIX panels. Rebuilding becomes an argument about what he actually accomplished.\n"
  "PANEL 1 (top band, full width, the focal panel, occupying the top two-fifths): extreme-wide low "
  "angle — two former fighters stand on opposite scaffolds, one at right facing left and one at "
  "left facing right, lifting the same roof beam upward; the teen and the auburn-haired woman are "
  "small below at centre, both looking up.\n"
  "PANEL 2 (middle right, one third width): insert close-up with NO faces visible — two pairs of "
  "hands move the timber left into its join.\n"
  "PANEL 3 (middle centre, one third width): medium close-up — she stands at right facing left "
  "toward him outside the panel; the raised beam crosses behind her, running upward.\n"
  "PANEL 4 (middle left, one third width): close profile — he faces left and looks UP at the beam "
  "rather than back at her.\n"
  "PANEL 5 (bottom right, half width): tracking two-shot — she at right and he at left continue "
  "walking left; she looks at him while he looks ahead.\n"
  "PANEL 6 (bottom left, half width): low insert with his profile — the beam locks into place at "
  "upper left; his face occupies the lower right, facing left and watching the joint. " + L_KIRI
  + SAY((1, MEI, "upper right", "TWO WEEKS AGO, THOSE HANDS CARRIED WEAPONS."),
        (2, OFF(BOY16), "upper right", "NOW THEY CARRY TIMBER."),
        (3, MEI, "upper centre", "YOU MADE THAT POSSIBLE."),
        (4, BOY16, "upper left", "I REMOVED AN OBSTRUCTION."),
        (5, MEI, "upper right", "YOU MAKE MERCY SOUND LIKE ENGINEERING."),
        (6, BOY16, "upper left", "ENGINEERING IS RELIABLE."))
  + "In PANEL 1 the balloon belongs to the AUBURN-HAIRED WOMAN standing small at the bottom centre "
    "of the panel: draw a long clear tail that reaches all the way down to HER mouth without "
    "touching either scaffold worker. In PANEL 2 nobody is drawn, so the balloon's tail is a short "
    "straight spur to the panel's right border. ",
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_mizukage_tower"), "medium"),

 ("p08", dict(scene="dialogue", light="day", cast="two", mood="calm", panels=8),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + ENV_STREET.format(i=3)
  + ENV_GROUND.format(i=4) + ONLY(BOY16, MEI) + REPAIRED + EMS_OFF + NOWRITE +
  "EIGHT panels. He names a destination without ever claiming he travels alone.\n"
  "PANELS 1-6 USE IMAGE 3 (the rebuilding street). PANELS 7-8 USE IMAGE 4 (the empty training "
  "ground above the village).\n"
  "PANEL 1 (top right, one third width): medium side shot — the two leave the crowded street moving "
  "left; she at right looks left toward him.\n"
  "PANEL 2 (top centre, one third width): close-up — he faces left, walking.\n"
  "PANEL 3 (top left, one third width): close reaction — she faces left, eye-line on him.\n"
  "PANEL 4 (middle right, one third width): close profile — he faces left.\n"
  "PANEL 5 (middle centre, one third width): close-up — she turns her chin left, eye-line following "
  "him while her body continues left.\n"
  "PANEL 6 (middle left, one third width): tight profile — he faces left and keeps moving.\n"
  "PANEL 7 (bottom right, half width): SILENT extreme-wide establishing shot — the two enter an "
  "empty training ground from the right moving left; the rebuilt tower stands behind at far right "
  "and ONE isolated tree anchors the far left. Their eye-lines travel toward the tree. No text in "
  "this panel.\n"
  "PANEL 8 (bottom left, half width): medium-long shot beneath the tree — he sits at right facing "
  "left; she remains standing at left facing right, beginning to sit. " + L_OPEN
  + SAY((1, MEI, "upper right", "WHEN ARE YOU LEAVING?"),
        (2, BOY16, "upper centre", "IN A FEW DAYS."),
        (3, MEI, "upper left", "KONOHA?"),
        (4, BOY16, "upper right", "STONE COUNTRY."),
        (5, MEI, "upper centre", "WHAT WILL YOU DO THERE?"),
        (6, BOY16, "upper left", "OTHER BUSINESS."),
        (8, MEI, "upper right", "YOU ANSWER LOCATIONS MORE EASILY THAN MOTIVES."),
        (8, BOY16, "lower left", "LOCATIONS ARE SIMPLER.")),
  R("naruto_v4_armor", "mei_v4", "env_mizukage_tower", "env_kiri_moonlit_hill"), "low"),

 # ---- Spread 5: battle as dance, then whose peace ------------------------------------
 ("p09", dict(scene="dialogue", light="overcast", cast="two", mood="calm", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + SUSA_FINAL.format(i=3)
  + ENV_GROUND.format(i=4)
  + ONLY(BOY16, MEI,
         "the huge orange armoured warrior form appearing ONLY as a faint flat memory silhouette "
         "inside PANEL 4, never as a present figure and never on any other panel")
  + REPAIRED + EMS_OFF +
  "SIX panels. Battle-as-dance is defined in dialogue before the quiet becomes a peace argument.\n"
  "PANEL 1 (top right, half width): wide two-shot beneath the tree — she sits at left facing right; "
  "he sits at right facing left, with a blurred Kiri in the distance between them.\n"
  "PANEL 2 (top left, half width): close profile — he faces left toward her but looks past her "
  "toward the empty ground.\n"
  "PANEL 3 (middle right, half width): close on the woman — she faces right and studies his "
  "profile; her eye-line is direct.\n"
  "PANEL 4 (middle left, the focal panel): layered medium close-up — he fills the right foreground "
  "facing left; BEHIND him a faint memory silhouette of the huge orange armoured warrior's BLADE "
  "sweeps right-to-left across a distant battlefield. That silhouette is drawn as a FLAT OPAQUE "
  "shape with a hard outline, does NOT glow and does NOT wash out the panel; no additional present "
  "character is added.\n"
  "PANEL 5 (bottom right, half width): medium on the woman leaning forward — she shifts from left "
  "toward right across the gap, eyes fixed on him.\n"
  "PANEL 6 (bottom left, half width): tight frontal close-up — he is centred facing forward, eyes "
  "angled right toward her. " + L_OPEN
  + SAY((1, MEI, "upper right", "YOU CHOOSE QUIET AFTER EVERY BATTLE."),
        (2, BOY16, "upper left", "NOISE IS USEFUL ONLY WHEN IT CHANGES SOMETHING."),
        (3, MEI, "upper right", "THE WAY YOU FOUGHT DID NOT LOOK PEACEFUL."),
        (4, BOY16, "upper left",
         "THE BATTLEFIELD OFFERS ME A CHANCE TO DANCE. THIS PLACE OFFERS PEACE."),
        (5, MEI, "upper right", "THEN CHANGE MORE."),
        (6, BOY16, "upper left", "BE PRECISE.")),
  R("naruto_v4_armor", "mei_v4", "susanoo_orange_final", "env_kiri_moonlit_hill"), "low"),

 ("p10", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_GROUND.format(i=4)
  + ONLY(BOY16, MEI, "unnamed Kiri children and workers, tiny and distant in the street below "
         "PANEL 6 only") + REPAIRED + EMS_OFF + CROWD +
  "SIX panels. She names a concrete objective; he interrogates whom an imposed peace would serve.\n"
  "PANEL 1 (top right, half width): medium close-up — she sits at left facing right toward him; the "
  "rebuilt village sits behind her.\n"
  "PANEL 2 (top left, half width): tighter close-up on the woman — she remains facing right and "
  "holds his eye-line.\n"
  "PANEL 3 (middle right, one third width): tight face close-up — he faces left toward her; his "
  "visible eye and mouth stay in frame and he remains still.\n"
  "PANEL 4 (middle centre, one third width): tight frontal close-up — she is centred facing "
  "forward, eye-line locked on him.\n"
  "PANEL 5 (middle left, one third width): close profile — he faces left toward her, still.\n"
  "PANEL 6 (bottom band, full width): wide low angle with the village behind — she sits at left "
  "facing right toward him at far right; between them, small distant children help carry salvaged "
  "boards leftward across the street below. " + L_OPEN
  + SAY((1, MEI, "upper right", "YOU CAN FORCE THE WORLD TO LISTEN."),
        (2, MEI, "upper left", "WHY NOT MAKE IT PEACEFUL?"),
        (3, BOY16, "upper right", "FOR WHOM?"),
        (4, MEI, "upper centre", "EVERYONE."),
        (5, BOY16, "upper left", "EVERYONE WANTS A DIFFERENT PEACE."),
        (6, MEI, "upper left",
         "THEN BEGIN WITH ONE THAT DOES NOT BURY CHILDREN FOR THEIR BLOOD.")),
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "low"),

 # ---- Spread 6: reasons and the strong who watched -----------------------------------
 ("p11", dict(scene="dialogue", light="overcast", cast="small_group", mood="somber", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_GROUND.format(i=4)
  + ONLY(BOY16, MEI,
         "unnamed Kiri rebels and unnamed fleeing civilians appearing ONLY inside the remembered "
         "background of PANEL 4") + REPAIRED + EMS_OFF +
  "FIVE panels. Her objective is grounded in the blood purge, and a chosen reason is separated from "
  "an assigned destiny. No injury detail and no blood appears anywhere on this page.\n"
  "PANEL 1 (top band, full width): SILENT memory insert, high-angle long shot with NO people at all "
  "— a burned Kiri doorway sits at left, one abandoned child's shoe at centre points right, and ash "
  "drifts right-to-left. No body, no wound and no blood. No text in this panel.\n"
  "PANEL 2 (middle right, half width): close profile — he faces left toward the memory's direction, "
  "not toward the woman.\n"
  "PANEL 3 (middle left, half width): medium close-up — she sits at left facing right toward him, "
  "shoulders square.\n"
  "PANEL 4 (bottom right, the focal panel, filling most of the bottom band's right side): wide "
  "remembered profile — the present-day auburn-haired woman is a close silhouette at right facing "
  "left; BEHIND her, in a hard-edged desaturated remembered image, unnamed rebels move left to "
  "shield civilians moving right, holding an evacuation line. Nobody is injured and no blood "
  "appears.\n"
  "PANEL 5 (bottom left): tight two-shot — he is at right facing left and she is at left facing "
  "right; their eye-lines meet. " + L_OPEN
  + SAY((2, BOY16, "upper right", "YOU ASSUME THEY WOULD KEEP IT."),
        (3, MEI, "upper left", "NO ONE GAVE ME A DESTINY TO LEAD."),
        (4, MEI, "upper right", "I CHOSE IT BECAUSE PEOPLE I LOVED WOULD DIE."),
        (5, BOY16, "upper right", "YOU HAD A REASON."),
        (5, MEI, "lower left", "SO DO YOU."))
  + "In PANEL 4 the balloon belongs to the PRESENT-DAY woman in the foreground silhouette, not to "
    "anyone inside the remembered image behind her: its tail must reach her foreground mouth. ",
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill"), "medium"),

 ("p12", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + ENV_GROUND.format(i=3)
  + ONLY(BOY16, MEI) + REPAIRED + EMS_OFF +
  "FIVE panels. His refusal is set against Konoha's earlier refusal to aid Kiri.\n"
  "PANEL 1 (top right, half width): tight profile on the teen — he faces left toward her; his "
  "eye-line does not shift.\n"
  "PANEL 2 (top left, half width): close-up — she faces right toward him.\n"
  "PANEL 3 (middle band, full width): balanced wide two-shot — he sits at right facing left and she "
  "sits at left facing right; Kiri's repaired wall forms a horizontal line behind them.\n"
  "PANEL 4 (bottom right, the focal panel, dominant): close-up on the woman — she fills the panel "
  "facing right, expression hard, her eye-line staying on him outside the frame.\n"
  "PANEL 5 (bottom left, narrower): medium close-up on the teen — he faces left but tilts his chin "
  "slightly down, testing the inference. " + L_OPEN
  + SAY((1, BOY16, "upper right", "MY REASON IS NOT THEIR PEACE."),
        (2, MEI, "upper left", "IT COULD BECOME ONE."),
        (3, BOY16, "upper right", "WHAT DID KONOHA'S REFUSAL TEACH YOU?"),
        (4, MEI, "upper right", "THAT GOOD MEN CAN WATCH EVIL WHEN HELPING IS INCONVENIENT."),
        (5, BOY16, "upper left",
         "AND NOW YOU WANT ANOTHER STRONG MAN TO PROMISE HE WILL ALWAYS HELP.")),
  R("naruto_v4_armor", "mei_v4", "env_kiri_moonlit_hill"), "low"),

 # ---- Spread 7: consequences and the limit of possession -----------------------------
 ("p13", dict(scene="establishing", light="overcast", cast="crowd", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_GROUND.format(i=4) + ENV_STREET.format(i=5)
  + ONLY(BOY16, MEI, "unnamed Kiri workers and families moving through the reconstruction far below "
         "in PANEL 5") + REPAIRED + EMS_OFF + CROWD +
  "SIX panels. She identifies the consequence of his claimed indifference.\n"
  "PANELS 1-4 AND 6 USE IMAGE 4 (the open ground). PANEL 5 LOOKS DOWN OVER IMAGE 5 (the rebuilding "
  "street).\n"
  "PANEL 1 (top band, full width): medium-wide two-shot — she leans right at left toward him; he "
  "remains upright at right facing left; their eye-lines meet over the open space.\n"
  "PANEL 2 (middle right, one third width): close profile — he faces left.\n"
  "PANEL 3 (middle centre, one third width): tight close-up — she faces right without blinking.\n"
  "PANEL 4 (middle left, one third width): tight face close-up — he faces right; his visible eye "
  "sharpens toward her and his mouth remains in frame.\n"
  "PANEL 5 (bottom right, the focal panel, dominant): high-angle wide view over Kiri — the two of "
  "them are SMALL at upper right, both facing left, over workers and families moving through the "
  "reconstruction below.\n"
  "PANEL 6 (bottom left, narrower): tight profile on the teen — he faces left toward the village, "
  "not toward her. " + L_OPEN
  + SAY((1, MEI, "upper right",
         "I WANT THE STRONG TO STOP PRETENDING THEY ARE SEPARATE FROM CONSEQUENCES."),
        (2, BOY16, "upper right", "I DO NOT CARE WHAT HAPPENS TO THE WORLD."),
        (3, MEI, "upper centre", "THAT IS NOT TRUE."),
        (4, BOY16, "upper left", "YOU PRESUME."),
        (5, MEI, "upper right",
         "YOU CROSSED AN OCEAN AND ENDED A WAR YOU CALLED NONE OF YOUR BUSINESS."),
        (6, BOY16, "upper left", "FOR MY OWN REASONS."))
  + "In PANEL 5 both figures are tiny: draw a long clear tail from the balloon down to the "
    "AUBURN-HAIRED WOMAN'S small figure, clear of the blond teen beside her. ",
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill",
    "env_mizukage_tower"), "medium"),

 ("p14", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + ENV_GROUND.format(i=3)
  + ONLY(BOY16, MEI) + REPAIRED + EMS_OFF +
  "SIX panels. She wins one point without changing his stated philosophy.\n"
  "PANEL 1 (top band, full width): medium two-shot with Kiri behind — she is at left facing right; "
  "he is at right facing left but looks down toward Kiri.\n"
  "PANEL 2 (middle right, one third width): SILENT close reaction — he faces left, his eye-line "
  "lowers and the wind moves one strand of hair left. No text in this panel.\n"
  "PANEL 3 (middle centre, one third width): tight profile — he turns his eye-line right toward her "
  "without moving his body.\n"
  "PANEL 4 (middle left, one third width): close-up — she faces right at him.\n"
  "PANEL 5 (bottom right, half width): medium close-up — he faces left and looks level at her.\n"
  "PANEL 6 (bottom left, half width): close reaction on the woman — she faces right, then shifts "
  "her eye-line downward toward children who are BEYOND the panel edge and are not drawn. " + L_OPEN
  + SAY((1, MEI, "upper right", "REASONS CAN BEGIN SELFISHLY AND STILL SAVE SOMEONE."),
        (3, BOY16, "upper centre", "IF EVIL TOUCHES WHAT IS MINE, I REMOVE IT."),
        (4, MEI, "upper left", "AND EVERYONE ELSE?"),
        (5, BOY16, "upper right", "BUILD STRENGTH."),
        (6, MEI, "upper left", "CHILDREN TOO?")),
  R("naruto_v4_armor", "mei_v4", "env_kiri_moonlit_hill"), "low"),

 # ---- Spread 8: choice without a cage ------------------------------------------------
 ("p15", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + ENV_GROUND.format(i=3)
  + ONLY(BOY16, MEI) + REPAIRED + EMS_OFF + NOWRITE +
  "SEVEN panels. His objection to a forced peace is stated in full.\n"
  "PANEL 1 (top band, full width): SILENT extreme-wide — he sits at right and she sits at left "
  "beneath the tree, both facing the village at centre; the rebuilt tower's banner moves left in "
  "the wind while neither person moves. No text in this panel.\n"
  "PANEL 2 (middle right, one third width): medium close-up — she faces right toward him.\n"
  "PANEL 3 (middle centre, one third width): tighter close-up on the woman — she remains facing "
  "right and holds his eye-line.\n"
  "PANEL 4 (middle left, one third width): tight face close-up on the teen — he faces left; his "
  "visible eye looks toward her and his mouth remains in frame.\n"
  "PANEL 5 (bottom right, one third width): tight profile — he faces left, chin level.\n"
  "PANEL 6 (bottom centre, one third width): close-up on the woman — she faces right and leans "
  "slightly toward him.\n"
  "PANEL 7 (bottom left, the focal panel, narrow): medium close-up on the teen against a fence "
  "shadow — he faces left while vertical tree-shadow bars cross the ground behind him; his face "
  "remains completely unobscured. THE AUBURN-HAIRED WOMAN IS NOT DRAWN IN THIS PANEL. " + L_OPEN
  + SAY((2, MEI, "upper right", "POWER GAVE YOU CHOICE."),
        (3, MEI, "upper centre", "YOU TREAT THAT AS PERMISSION TO CHOOSE NOTHING."),
        (4, BOY16, "upper left", "NO."),
        (5, BOY16, "upper right", "IT GIVES ME PERMISSION TO CHOOSE PRECISELY."),
        (6, MEI, "upper centre", "THEN CHOOSE PEACE."),
        (7, BOY16, "upper left",
         "NOT BY CHOOSING FOR EVERYONE. A PEACE THAT TAKES THEIR CHOICE IS ANOTHER CAGE."),
        (7, OFF(MEI), "lower left", "AND TODAY?")),
  R("naruto_v4_armor", "mei_v4", "env_kiri_moonlit_hill"), "low"),

 ("p16", dict(scene="establishing", light="overcast", cast="crowd", mood="calm", panels=7),
  FILL + RTL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + KIRI_REBELS.format(i=3)
  + ENV_GROUND.format(i=4) + ENV_STREET.format(i=5)
  + ONLY(BOY16, MEI, "unnamed Kiri workers, families and shinobi rebuilding in the valley below in "
         "PANEL 3") + REPAIRED + EMS_OFF + CROWD +
  "SEVEN panels. LAST PAGE OF THE CHAPTER — the abstract argument resolves into a concrete result.\n"
  "PANELS 1-2 AND 4-7 USE IMAGE 4 (the open ground). PANEL 3 LOOKS DOWN OVER IMAGE 5 (the "
  "rebuilding street).\n"
  "PANEL 1 (top right, half width): medium profile — he stands at right facing left over Kiri; she "
  "remains seated at lower left and looks up-right at him.\n"
  "PANEL 2 (top left, half width): medium reaction — she rises at left facing right toward him and "
  "folds her arms loosely.\n"
  "PANEL 3 (dominant middle band, full width, the focal panel): extreme-wide high angle — he stands "
  "at FAR RIGHT facing left and she stands at FAR LEFT facing right; workers, families and shinobi "
  "rebuild in the valley between their eye-lines.\n"
  "PANEL 4 (bottom right, upper tier, half width): quiet medium two-shot — he turns left from the "
  "view at right to face her at left; she meets his eye-line.\n"
  "PANEL 5 (bottom left, upper tier, half width): close-up — she faces right toward him.\n"
  "PANEL 6 (bottom right, lower tier, half width): tight face close-up — he faces left at her; his "
  "visible eye and mouth remain in frame and he does not move.\n"
  "PANEL 7 (bottom left, lower tier, half width): tight frontal close-up — she faces forward but "
  "holds his eye-line to the right. " + L_OPEN
  + SAY((1, BOY16, "upper right", "TODAY I CHOOSE NOT TO RULE THE WORLD."),
        (2, MEI, "upper left",
         "I DO NOT NEED YOU TO RULE IT. JUST ADMIT YOUR CHOICES ALREADY SHAPE IT."),
        (3, MEI, "upper right", "BECAUSE YOU CHOSE TO DANCE."),
        (3, BOY16, "upper left", "BECAUSE YOU CHOSE TO LEAD."),
        (3, MEI, "lower centre", "THEN PERHAPS BOTH WERE NEEDED."),
        (4, BOY16, "upper right", "YOU DID NOT COME HERE TO DEBATE PEACE."),
        (5, MEI, "upper left", "NO. I CAME BECAUSE YOU LEAVE IN DAYS."),
        (6, BOY16, "upper right", "AND?"),
        (7, MEI, "upper left", "I DISLIKE UNFINISHED CONVERSATIONS."))
  + "PANEL 3 carries three balloons whose tails cross the panel: the upper right balloon and the "
    "lower centre balloon both tail LEFT to the auburn-haired woman at the far left edge, and the "
    "upper left balloon tails RIGHT to the blond teen at the far right edge. Draw the three tails "
    "long, thin and clearly separated so no tail can be read as belonging to the nearer figure. ",
  R("naruto_v4_armor", "mei_v4", "kiri_rebel_mob", "env_kiri_moonlit_hill",
    "env_mizukage_tower"), "high"),
]

if __name__ == "__main__":
    # Same fixed style anchor Codex used for all of Volume 4, so the volumes read as one book.
    run(PAGES, HERE / "v5ch02" / "raw", HERE / "v5ch02" / "ledger.json",
        style_ref=HERE.parent / "refs" / "images" / "style_v01_p094.png")
