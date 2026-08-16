"""Volume 4, Chapter 1 — "The Professor". 16 pages.

Source: fic ch08:5-93, with the apartment-door handoff at :95-101.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import (CAP, DAN, ENV, FILL, HIR, JIR, KAB, N13, ORO, R, SAY, SFX,
                     ZET, ONLY, BOY, HAWK, OLD, PALEONE, SAGE, SPEC)  # noqa: E402
from prompts_v4 import (HOMURA, HOMURA_SPEAKER, ITACHI, KOHARU, KOHARU_SPEAKER, MANGEKYO_EYE,
                        )  # noqa: E402


MOURNERS = "unnamed Konoha mourners and repair crews, visible only as distant silhouettes"
ANBU = "unnamed ANBU silhouettes"
ZETSU = "the split black-and-white plant creature"
VISITOR = "one face-hidden short dark-haired adolescent visitor"
L_KONOHA = "Lighting: low slate storm clouds, cold rain-blue reflections, no warmth. "
L_OFFICE = "Lighting: cold grey daylight through rain-streaked windows; the office is stripped of warmth. "
L_LAB = "Lighting: clinical green-grey low light, cramped and dim; metal and glass stay legible. "
L_APARTMENT = "Lighting: cold single-bulb apartment light against blue-grey evening. "


PAGES = [
 ("p01", dict(scene="establishing", light="storm", cast="crowd", mood="somber", panels=1),
  ENV.format(i=1) + ONLY(MOURNERS) +
  "CHAPTER OPENING SPLASH. Borderless vertical high view across Konoha beneath low slate clouds: "
  "broken roofs, tiny repair crews, damp streets, and memorial cloths. The village stands but the "
  "frame is drained rather than victorious. No protagonist. Keep the upper third quiet for title "
  "lettering. " + L_KONOHA +
  "LETTERING: in the quiet upper third, write the chapter title in large bold upright English "
  "capitals: \"THE PROFESSOR\". " +
  CAP(1, "lower left", "KONOHA SURVIVED.") +
  CAP(1, "lower right", "IT STILL PAID."),
  R("env_konoha_after_invasion"), "high"),

 ("p02", dict(scene="mourning", light="storm", cast="crowd", mood="somber", panels=5),
  "Image 1 is the PORTRAIT-LIKENESS REFERENCE for the deceased Third Hokage. It may appear solely "
  "inside the framed memorial portrait in PANEL 4; the deceased man must never appear living, in "
  "the crowd, or anywhere else on this page. " + ENV.format(i=2) + ONLY(MOURNERS) +
  "FIVE uneven panels. PANEL 1 (dominant wide): a mourning crowd moving toward a distant memorial, "
  "seen through cropped foreground umbrellas and shoulders. PANEL 2 (small): a cracked Hokage "
  "monument detail. PANEL 3 (small): incense smoke. PANEL 4 (small): Hiruzen's framed portrait. "
  "PANEL 5 (narrow bottom): an empty seat beneath the portrait. This is communal mourning and "
  "aftermath only — do not stage a burial ceremony. Do not draw readable incidental writing or "
  "symbols anywhere on the page beyond the exact supplied caption. " + L_KONOHA +
  CAP(1, "upper left", "THE THIRD HOKAGE WAS GONE."),
  R("hiruzen", "env_konoha_after_invasion"), "high"),

 ("p03", dict(scene="isolation", light="storm", cast="solo", mood="distant", panels=4),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(BOY, MOURNERS) +
  "FOUR uneven panels. PANEL 1 (dominant): Naruto sits very small on his apartment roof, back "
  "three-quarters to camera with knees raised; distant mourners are barely visible far below. "
  "PANEL 2 (small): a flat-black close-up of his blank blue eye. PANEL 3 (small): rain on roof "
  "tile, no figure. PANEL 4 (narrow bottom): Naruto still above the village, physically apart. "
  "Make his absence from the communal mourning legible through distance, not spoken explanation. "
  "No sword, no orange clothing, and no active eye technique. " + L_KONOHA +
  CAP(1, "upper left", "NARUTO DID NOT GO."),
  R("naruto_13", "env_apartment_ext"), "high"),

 ("p04", dict(scene="thought", light="cold", cast="small_group", mood="calculating", panels=5),
  FILL + N13.format(i=1) + HIR.format(i=2) + DAN.format(i=3) + ZET.format(i=4) +
  MANGEKYO_EYE.format(i=5) + ENV.format(i=6) + ONLY(BOY, OLD, HAWK, ZETSU) +
  "FIVE uneven interior-thought panels with flat black and cold blue backgrounds. PANEL 1 "
  "(dominant): Naruto's face cropped by the right edge, alone in thought. PANEL 2 (small): "
  "Hiruzen's portrait dissolving into a chess-piece-like Hokage hat. PANEL 3 (small): Danzō's "
  "empty chair. PANEL 4 (small): Zetsu's split black-and-white profile half-submerged in shadow, "
  "a contingency image only — no assassination or action. PANEL 5 (wide bottom): Naruto looks "
  "toward the village, fist loosened. Keep a small, non-power-display reflection of his active "
  "Mangekyō only in panel 1: a blood-red iris with one black centre ring and exactly six broad "
  "black blades radiating outward. " + L_KONOHA +
  CAP(1, "upper left", "A SHIELD HAD BEEN REMOVED.") +
  CAP(5, "lower right", "IF SOMEONE ELSE SET THE RULES, HE WOULD BREAK THEM HIMSELF."),
  R("naruto_13", "hiruzen", "danzo", "zetsu", "mangekyo_design", "env_apartment_ext"), "high"),

 ("p05", dict(scene="dialogue", light="cold", cast="three", mood="pressure", panels=5),
  FILL + JIR.format(i=1) + HOMURA.format(i=2) + KOHARU.format(i=3) + ENV.format(i=4) +
  ONLY(SAGE, HOMURA_SPEAKER, KOHARU_SPEAKER) +
  "FIVE uneven panels. PANEL 1 (dominant wide): from behind the two elders, Jiraiya is small by "
  "the rain-streaked window with the vacant Hokage desk between them. PANEL 2 (small): a hand on "
  "the desk. PANEL 3 (small): Jiraiya's tired eye. PANEL 4 (small): the closed office door behind "
  "him. PANEL 5 (narrow bottom): all three at staggered depths, never a lineup. " + L_OFFICE +
  SAY((1, HOMURA_SPEAKER, "upper left", "THE VILLAGE NEEDS A LEADER."),
      (3, SAGE, "upper right", "I KNOW WHY YOU CALLED.")),
  R("jiraiya", "homura", "koharu", "env_hokage_office"), "high"),

 ("p06", dict(scene="dialogue", light="cold", cast="three", mood="pressure", panels=6),
  FILL + JIR.format(i=1) + HOMURA.format(i=2) + KOHARU.format(i=3) + ENV.format(i=4) +
  ONLY(SAGE, HOMURA_SPEAKER, KOHARU_SPEAKER) +
  "SIX uneven panels; conversation as pressure, not a lineup. PANEL 1: Koharu's cropped shoulder "
  "dominates foreground. PANEL 2: Jiraiya sits distant by the window. PANEL 3: Homura appears only "
  "in reflection. PANEL 4: Jiraiya's mouth. PANEL 5: a file marked only with an illegible seal. "
  "PANEL 6 (dominant bottom): Jiraiya's hand refusing the Hokage hat over the vacant desk. " + L_OFFICE +
  SAY((4, SAGE, "upper left", "I CANNOT TAKE THE TITLE."),
      (1, KOHARU_SPEAKER, "upper right", "YOU ARE THE STRONGEST ONE LEFT."),
      (6, SAGE, "lower left", "STRENGTH IS NOT THE JOB.")),
  R("jiraiya", "homura", "koharu", "env_hokage_office"), "high"),

 ("p07", dict(scene="dialogue", light="cold", cast="three", mood="decision", panels=4),
  FILL + JIR.format(i=1) + HOMURA.format(i=2) + KOHARU.format(i=3) + ENV.format(i=4) +
  ONLY(SAGE, HOMURA_SPEAKER, KOHARU_SPEAKER) +
  "FOUR uneven panels. PANEL 1 (dominant wide): Jiraiya turns away from the elders, silhouetted "
  "against the ruined village through the office window. PANEL 2 (narrow): elder eyes. PANEL 3 "
  "(narrow): Jiraiya's profile. PANEL 4 (narrow): a blank white panel holding the name before it "
  "lands. " + L_OFFICE +
  SAY((1, SAGE, "upper left", "THERE IS ANOTHER SANNIN."),
      (2, KOHARU_SPEAKER, "upper right", "TSUNADE?"),
      (4, SAGE, "center", "GIVE ME TWO WEEKS.")),
  R("jiraiya", "homura", "koharu", "env_hokage_office"), "high"),

 ("p08", dict(scene="dialogue", light="cold", cast="three", mood="tense", panels=6),
  FILL + JIR.format(i=1) + HOMURA.format(i=2) + KOHARU.format(i=3) + ENV.format(i=4) +
  ONLY(SAGE, HOMURA_SPEAKER, KOHARU_SPEAKER) +
  "SIX uneven panels. PANEL 1 (dominant letterbox): the elders framed across the vacant desk. "
  "PANEL 2: Jiraiya's tired profile. PANEL 3: an elder hand at the desk edge. PANEL 4: Jiraiya "
  "exiting through the window on a diagonal. PANEL 5: low-angle view of the two elders left behind. "
  "PANEL 6: wet window and empty room. Naruto is absent; adults are assigning him a role without "
  "him. " + L_OFFICE +
  SAY((1, KOHARU_SPEAKER, "upper left", "BRING HER BACK, OR TAKE THE OFFICE."),
      (4, SAGE, "upper right", "NO ANBU. I WILL ASK NARUTO."),
      (5, HOMURA_SPEAKER, "lower left", "HE MUST ANSWER FOR WHAT HE REVEALED.")),
  R("jiraiya", "homura", "koharu", "env_hokage_office"), "high"),

 ("p09", dict(scene="aftermath", light="cold", cast="three", mood="guarded", panels=4),
  FILL + HOMURA.format(i=1) + KOHARU.format(i=2) + ENV.format(i=3) + ONLY(HOMURA_SPEAKER, KOHARU_SPEAKER, ANBU) +
  "FOUR uneven panels. PANEL 1 (dominant): after Jiraiya leaves, an ANBU silhouette reflected in "
  "the wet office window, deliberately distant and unreadable. PANEL 2: Homura and Koharu exchange "
  "a guarded look over the desk. PANEL 3: Koharu's hand closing on a file. PANEL 4: the rain-streaked "
  "window, the reflected silhouette still there. " + L_OFFICE +
  SAY((2, KOHARU_SPEAKER, "upper left", "PUT EYES ON THEM."),
      (2, HOMURA_SPEAKER, "upper right", "EVEN WITH JIRAIYA?"),
      (3, KOHARU_SPEAKER, "lower left", "ESPECIALLY THEN.")),
  R("homura", "koharu", "env_hokage_office"), "high"),

 ("p10", dict(scene="establishing", light="dark", cast="solo", mood="failing", panels=3),
  FILL + ORO.format(i=1) + ENV.format(i=2) + ONLY(PALEONE) +
  "THREE uneven panels. PANEL 1 (dominant wide): hard location cut to a near-black Orochimaru "
  "hideout; Orochimaru sits low with his body slack and silhouette swallowed by darkness. PANEL 2 "
  "(small): a trembling hand against the floor. PANEL 3 (small): a slack sleeve and bowed shoulder. "
  "Convey failure without graphic transformation or any medicine objects before Kabuto arrives. " + L_LAB +
  CAP(1, "upper left", "ELSEWHERE.") +
  SAY((1, PALEONE, "lower right", "THIS VESSEL IS FAILING.")),
  R("orochimaru", "env_orochimaru_lab"), "high"),

 ("p11", dict(scene="dialogue", light="dark", cast="two", mood="failing", panels=6),
  FILL + ORO.format(i=1) + KAB.format(i=2) + ENV.format(i=3) + ONLY(PALEONE, SPEC) +
  "SIX uneven panels. Kabuto enters from the foreground, cropped to glasses and a tray carrying a "
  "glass of water and tablets; Orochimaru is small and deep in the room. PANEL 1: Kabuto's glasses "
  "and tray with water and tablets. PANEL 2: Orochimaru distant. "
  "PANEL 3: discarded empty chair or bed, suggesting time running out. PANEL 4: Orochimaru's narrowed "
  "eye. PANEL 5: Kabuto's attentive profile. PANEL 6 (dominant bottom): the two at deep staggered "
  "depths. Do not add Sasuke. " + L_LAB +
  SAY((1, SPEC, "upper left", "HOW SOON?"),
      (6, PALEONE, "lower right", "SOON ENOUGH THAT I NEED ANOTHER BODY.")),
  R("orochimaru", "kabuto", "env_orochimaru_lab"), "high"),

 ("p12", dict(scene="memory", light="dark", cast="three", mood="calculating", panels=5),
  FILL + ORO.format(i=1) + HIR.format(i=2) + ITACHI.format(i=3) + ENV.format(i=4) +
  ONLY(PALEONE, OLD, "the black-haired man in the red-cloud cloak") +
  "FIVE uneven panels, with graphic memory plates. PANEL 1: a shadow-memory of the black-haired "
  "man in a red-cloud cloak overpowering Orochimaru, impressionistic and non-graphic. PANEL 2: "
  "Hiruzen's sealing silhouette, only a past-failure plate. PANEL 3: present Orochimaru's hand "
  "crushing a tablet. PANEL 4: his narrowed golden eye. PANEL 5 (dominant bottom): Orochimaru alone "
  "in the clinical dark. No extra fight sequence. " + L_LAB +
  SAY((5, PALEONE, "upper left", "I HAVE MISJUDGED OPPONENTS BEFORE.")) +
  CAP(5, "lower right", "HE WOULD NOT REPEAT IT."),
  R("orochimaru", "hiruzen", "itachi", "env_orochimaru_lab"), "high"),

 ("p13", dict(scene="investigation", light="dark", cast="two", mood="predatory", panels=5),
  FILL + ORO.format(i=1) + KAB.format(i=2) + MANGEKYO_EYE.format(i=3) + ENV.format(i=4) + ONLY(PALEONE, SPEC) +
  "FIVE uneven panels. PANEL 1: Kabuto presents a labeled-but-illegible sample vial in extreme "
  "foreground; Orochimaru is distant. PANEL 2: Kabuto's glasses catching the vial light. PANEL 3: "
  "an abstract close-up of Naruto's active Mangekyō eye against flat black: a blood-red iris with "
  "one black centre ring and exactly six broad black blades radiating outward, the vial reflected "
  "in it. This is a disembodied graphic reflection only: never draw Naruto's face or body in the "
  "laboratory. PANEL 4: Orochimaru's smile. "
  "PANEL 5 (dominant bottom): vial and eye reflection join village fear to Orochimaru's curiosity. "
  "No extra text on the vial. " + L_LAB +
  SAY((1, SPEC, "upper left", "THE SAMPLE WAS PRESERVED."),
      (5, PALEONE, "lower right", "THEN STUDY IT.")),
  R("orochimaru", "kabuto", "mangekyo_design", "env_orochimaru_lab"), "high"),

 ("p14", dict(scene="dialogue", light="dark", cast="two", mood="predatory", panels=4),
  FILL + ORO.format(i=1) + KAB.format(i=2) + ENV.format(i=3) + ONLY(PALEONE, SPEC) +
  "FOUR uneven panels. PANEL 1 (dominant tall): Orochimaru's profile nearly fills the frame. "
  "PANEL 2: Kabuto turned away in the far background, leaving with the vial. PANEL 3: the vial "
  "crossing a dark doorway. PANEL 4 (wide bottom): Orochimaru alone in darkness, eyes open. Keep "
  "the question scientific and predatory, never an exposition dump. " + L_LAB +
  SAY((1, PALEONE, "upper left", "I SUSPECT UCHIHA BLOOD."),
      (4, PALEONE, "lower right", "FIND THE BLOODLINE BENEATH THEM.")),
  R("orochimaru", "kabuto", "env_orochimaru_lab"), "high"),

 ("p15", dict(scene="transition", light="dusk", cast="solo", mood="controlled", panels=3),
  FILL + N13.format(i=1) + ENV.format(i=2) + ENV.format(i=3) + ONLY(BOY) +
  "THREE uneven panels. PANEL 1: exterior apartment at blue-grey evening, one lit window in an "
  "otherwise dark building. PANEL 2 (dominant wide): inside, Naruto sits at the table in an orderly "
  "room, back to camera. PANEL 3 (small): his eyes track an approaching chakra presence off-panel. "
  "No visitor is visible yet. No sword, orange clothing, or active eye technique. " + L_APARTMENT +
  CAP(2, "upper left", "NARUTO HAD PLANS OF HIS OWN."),
  R("naruto_13", "env_apartment_ext", "env_apartment_int"), "high"),

 ("p16", dict(scene="hook", light="cold", cast="two", mood="controlled", panels=4),
  FILL + N13.format(i=1) + ENV.format(i=2) + ONLY(BOY, VISITOR) +
  "FOUR uneven panels. PANEL 1: Naruto rises in profile from the table. PANEL 2: close-up of the "
  "plain apartment lock and door detail. PANEL 3: Naruto's hand at the door. PANEL 4 (dominant): "
  "from inside the hall, Naruto opens the door only a fraction, his face foregrounded; beyond the "
  "threshold is only the cropped silhouette of a short dark-haired adolescent visitor, with no face "
  "shown. The order Naruto, door, visitor must read at thumbnail size. This is the handoff, not the "
  "conversation: no dialogue, no name, and no visible ANBU or Jiraiya markers. " + L_APARTMENT,
  R("naruto_13", "env_apartment_int"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch01" / "raw", HERE / "v4ch01" / "ledger.json")
