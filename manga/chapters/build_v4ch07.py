"""Volume 4, Chapter 7 — "Kiri". 18 pages.

Source: fic ch10:97-415. Stops before the three-nights-later hill scene.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts import CAP, ENV, FILL, OFF, ONLY, R, SAY, SFX, TITLE  # noqa: E402
from prompts_v4 import (AO_V4, AO_V4_SPEAKER, GUNBAI_V4, L_KIRI_MIST,
                        L_KIRI_TENT, MEI_V4, MEI_V4_SPEAKER, N16_ARMOR,
                        MANGEKYO_EYE, N16_BLACK, N16_SPEAKER, YUGAO_V4,
                        YUGAO_V4_SPEAKER)  # noqa: E402

N16_ARMOR += (" In this chapter his eyes are active: the visible LEFT eye is a blood-red "
              "three-tomoe Sharingan. The normally hair-covered RIGHT eye carries the active "
              "six-bladed Mangekyo only when a panel explicitly reveals it. ")
N16_BLACK += (" In this uninterrupted active-eye sequence, the visible LEFT eye is a blood-red "
              "three-tomoe Sharingan. The normally hair-covered RIGHT eye remains hidden unless a "
              "panel explicitly parts the long bang and reveals its active six-bladed Mangekyo. ")
AO_V4 += (" His implanted eye stays hidden behind the eyepatch in every panel; show its perception "
          "only through an implied Byakugan field-view, never by revealing the eye. ")

SCOUT = "one unnamed Kiri scout, face indistinct in the mist"
GUARDS = "unnamed Kiri rebel guards, each a distant non-identifiable silhouette"
CAMPERS = "unnamed rebel camp residents and guards, distant varied silhouettes only"
L_CAMP = "Lighting: cold mist-blue dusk, wet paths, and restrained amber tent lamps. "


PAGES = [
 ("p01", dict(scene="establishing", light="mist", cast="two", mood="resolute", panels=1),
  N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
  "CHAPTER OPENING SPLASH. Kiri's wet port at the edge of a cold grey sea, with dense mist "
  "swallowing the village beyond the stone entry gate. The older blond teen in red segmented "
  "armour steps off a small departing boat with the dark purple gunbai low at his side; the "
  "purple-haired Leaf kunoichi follows several paces behind. Make him approximately sixteen, "
  "not an adult. He has no sword. Naruto is the red accent in an otherwise restrained blue-grey "
  "page. He is entering by deliberate choice; Yugao is present but not posed with him. Leave the "
  "upper third quiet for the title. " + L_KIRI_MIST + TITLE("KIRI", "quiet upper third"),
  R("naruto_v4_armor", "yugao_v4", "env_kiri_mist_gate"), "high"),

 ("p02", dict(scene="arrival", light="mist", cast="two", mood="alert", panels=6),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
  "SIX uneven panels with an off-centre dominant middle panel. PANEL 1: the boat receding as a "
  "small silhouette on flat water. PANEL 2: Naruto's armoured sandal on wet stone. PANEL 3 "
  "(dominant): Yugao large in cropped foreground, turned toward the armoured Naruto walking into "
  "mist far beyond her; his armour's hard shapes are audible before he is fully seen. PANEL 4: "
  "Naruto's unreadable eye. PANEL 5: Yugao choosing to follow, now beside rather than behind him. "
  "PANEL 6: the gate dissolving into fog. Their different depths must make this a choice, never a "
  "romantic walk. " + L_KIRI_MIST +
  SAY((3, YUGAO_V4_SPEAKER, "upper left", "KIRI IS AT WAR."),
      (5, N16_SPEAKER, "lower right", "THAT IS WHY I CAME.")) +
  SFX(3, "KLANG", "The armour sound is small and hard-edged, never covering a face."),
  R("naruto_v4_armor", "yugao_v4", "env_kiri_mist_gate"), "high"),

 ("p03", dict(scene="suspense", light="mist", cast="three", mood="watchful", panels=7),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, SCOUT) +
  "SEVEN uneven panels, with the dominant panel a tall, near-empty mist corridor. PANEL 1: wet "
  "stones disappearing into flat blue-grey. PANEL 2: Yugao's hand near but not on her weapon. "
  "PANEL 3: Naruto pauses, small in the long corridor. PANEL 4 (dominant): his close-cropped "
  "left eye turns right while the scout is only a distant, barely resolved silhouette at the far "
  "edge. PANEL 5: the scout's hidden foot on wet stone. PANEL 6: Yugao notices Naruto's stop. "
  "PANEL 7: empty mist between hunter and target. Naruto is not surprised: he already knows the "
  "rebel camp location from intelligence. " + L_KIRI_MIST +
  CAP(4, "lower left", "SOMEONE WAS FOLLOWING."),
  R("naruto_v4_armor", "yugao_v4", "env_kiri_mist_gate"), "high"),

 ("p04", dict(scene="action", light="mist", cast="three", mood="cold", panels=6),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, SCOUT) +
  "SIX uneven panels, built around one dominant horizontal action panel. PANEL 1: the unnamed "
  "scout lunging from mist. PANEL 2: Naruto's armoured hand catching the scout's throat, shown "
  "in foreshortened hand-to-lens perspective. PANEL 3 (dominant): Naruto and the scout at hard "
  "diagonal depths; Naruto holds a ram seal in his free hand while Yugao is small, alarmed, in a "
  "separate background plane. PANEL 4: the scout's eyes taking on a Sharingan-like pattern. "
  "PANEL 5: Naruto's blank mouth. PANEL 6: Yugao's interrupted reaction. This is an imperfect "
  "control test, not a triumphant fight. No graphic injury. " + L_KIRI_MIST +
  SAY((3, N16_SPEAKER, "upper left", "OBEY."),
      (5, N16_SPEAKER, "lower right", "HURT YOURSELF."),
      (6, YUGAO_V4_SPEAKER, "upper left", "NARUTO—")) +
  SFX(2, "GRIP", "A compact hard-edged impact mark beside the hand only."),
  R("naruto_v4_armor", "yugao_v4", "env_kiri_mist_gate"), "high"),

 ("p05", dict(scene="aftermath", light="mist", cast="three", mood="disturbed", panels=5),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, SCOUT) +
  "FIVE uneven panels. PANEL 1: the scout's extreme close-up refusal. PANEL 2: a white impact "
  "field and snapped silhouette, with Naruto's hand releasing; no neck detail, no blood, no gore. "
  "PANEL 3 (dominant): Yugao's face cropped tightly in foreground, disturbed and morally clear; "
  "Naruto is small and already walking away through the mist. PANEL 4: the scout's body only as a "
  "distant, non-graphic shape on wet ground. PANEL 5: Yugao walks beside Naruto rather than behind "
  "him, looking away. His result caused the killing; do not make it heroic. " + L_KIRI_MIST +
  SAY((3, YUGAO_V4_SPEAKER, "upper left", "WAS THAT NECESSARY?"),
      (5, N16_SPEAKER, "lower right", "HE RESISTED. THE GENJUTSU IS IMPERFECT.")),
  R("naruto_v4_armor", "yugao_v4", "env_kiri_mist_gate"), "high"),

 ("p06", dict(scene="gate_watch", light="mist", cast="group", mood="defensive", panels=7),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, GUARDS) +
  "SEVEN uneven panels. PANEL 1: a Byakugan-like field view of Naruto's unusually vast chakra "
  "network, with Ao not drawn in this panel. PANEL 2: Ao's closed eyepatch, with the perception "
  "implied by the preceding field-view and no eye shown. "
  "PANEL 3: unnamed guards forming an irregular depth-staggered defensive cluster, never a line. "
  "PANEL 4 (dominant): Naruto and Yugao emerge very small below the wet Kiri gate, while Ao is "
  "large and cropped in the foreground. PANEL 5: a guard's hand on a weapon. PANEL 6: Naruto's "
  "Konoha protector and active red eye. PANEL 7: fog closing the distance. Do not show Yagura. "
  + L_KIRI_MIST +
  SAY((1, OFF(AO_V4_SPEAKER), "upper left", "TWO INCOMING."),
      (3, AO_V4_SPEAKER, "lower right", "IF THEY ARE HOSTILE, I TAKE THE ARMORED ONE.")),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "env_kiri_mist_gate"), "high"),

 ("p07", dict(scene="gate_parley", light="mist", cast="group", mood="guarded", panels=6),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, GUARDS) +
  "SIX uneven panels. PANEL 1: Ao large in foreground, half-turned, with Naruto and Yugao small "
  "below the gate. PANEL 2: Naruto's Leaf protector. PANEL 3: his red Sharingan eye. PANEL 4 "
  "(dominant): Naruto and Ao face each other at radically different depths, their sight-lines "
  "meeting across wet stone; hidden guards appear only as cropped edge shapes. PANEL 5: Yugao's "
  "controlled reaction. PANEL 6: the misty route into camp. The political question is the action. "
  + L_KIRI_MIST +
  SAY((1, AO_V4_SPEAKER, "upper left", "STATE YOUR BUSINESS."),
      (4, N16_SPEAKER, "lower right", "TAKE ME TO YOUR LEADER."),
      (5, AO_V4_SPEAKER, "upper left", "WHO ARE YOU?"),
      (6, N16_SPEAKER, "lower right", "UCHIHA NARUTO. OR UZUMAKI NARUTO.")),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "env_kiri_mist_gate"), "high"),

 ("p08", dict(scene="gate_parley", light="mist", cast="group", mood="threatened", panels=7),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, GUARDS) +
  "SEVEN uneven panels. PANEL 1: Yugao answers with Naruto still and distant beyond her shoulder. "
  "PANEL 2: Ao's guarded eyepatch, taut at the temple. PANEL 3: Naruto's left eye, dominant and cropped by all edges. "
  "PANEL 4: Ao recoiling only slightly. PANEL 5 (dominant): Naruto and Ao separated by a broad "
  "wet-stone gap, Naruto small but immovable and Yugao on a third depth plane. PANEL 6: a guard "
  "lowering a weapon a fraction. PANEL 7: Ao turns toward camp. No fight starts. " + L_KIRI_MIST +
  SAY((1, YUGAO_V4_SPEAKER, "upper left", "HE WANTS TO JOIN YOUR WAR."),
      (2, AO_V4_SPEAKER, "upper right", "IF YOU THREATEN MEI, I WILL KILL YOU BOTH."),
      (5, N16_SPEAKER, "lower left", "THREATEN HER AGAIN, AND YOU WILL NOT BE ALL RIGHT."),
      (7, AO_V4_SPEAKER, "lower right", "FOLLOW ME.")),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "env_kiri_mist_gate"), "high"),

 ("p09", dict(scene="establishing", light="dusk", cast="group", mood="hopeful", panels=6),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, CAMPERS) +
  "SIX uneven panels. PANEL 1 (dominant high angle): the gate-side rebel camp is an irregular "
  "field of tents, damp paths, residents and guards at different scales, with activity and hope "
  "under war pressure. PANEL 2: anonymous hands repairing gear. PANEL 3: an unnamed child carrying "
  "water past a guard. PANEL 4: Ao leading Naruto and Yugao at staggered depths. PANEL 5: Naruto's "
  "blank observation. PANEL 6: the command tent ahead, warmer than the blue camp. Camp residents "
  "are varied civilians and rebels, not a bloodline-only population. " + L_CAMP +
  CAP(1, "upper left", "THE REBELS HELD THE GATE SIDE OF KIRI.") +
  CAP(5, "lower right", "THEY STILL BELIEVED THEY COULD WIN."),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "env_kiri_rebel_camp"), "high"),

 ("p10", dict(scene="command", light="tent", cast="two", mood="measured", panels=6),
  FILL + AO_V4.format(i=1) + MEI_V4.format(i=2) + ENV.format(i=3) +
  ONLY(AO_V4_SPEAKER, MEI_V4_SPEAKER) +
  "SIX uneven panels inside the rebel command tent before the visitors enter. PANEL 1: Mei at her "
  "desk, maps present only as illegible marks. PANEL 2: Ao at a lower foreground angle, report in "
  "hand. PANEL 3: Mei's green eye, calculating. PANEL 4 (dominant): command map surface between "
  "them, Mei larger but not protected, Ao in a separate foreground depth. PANEL 5: Ao's guarded "
  "eyepatch silhouette. PANEL 6: Mei's hand indicating the entrance. Mei is the rebel leader; "
  "Yagura is the current Mizukage and remains off-panel. " + L_KIRI_TENT +
  SAY((2, AO_V4_SPEAKER, "upper left", "A KONOHA SHINOBI ASKS FOR YOU. I DO NOT TRUST HIM."),
      (6, MEI_V4_SPEAKER, "lower right", "BRING THEM IN.")),
  R("ao_v4", "mei_v4", "env_mei_tent"), "high"),

 ("p11", dict(scene="introduction", light="tent", cast="four", mood="professional", panels=7),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + MEI_V4.format(i=4) +
  ENV.format(i=5) + ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, MEI_V4_SPEAKER) +
  "SEVEN uneven panels. PANEL 1: Mei enters foreground with a professional welcome, Naruto and "
  "Yugao contained in doorway depth. PANEL 2: Ao watches from a third plane. PANEL 3: Naruto's "
  "level eye. PANEL 4 (dominant): the handshake at lower centre; their hands are clear while Mei "
  "and Naruto's faces remain visible at different scales, with Yugao and Ao separate in background "
  "depth. PANEL 5: Mei's composed face. PANEL 6: Yugao's concise introduction. PANEL 7: the desk "
  "beyond them. This is professional recognition, never flirtation or fan service. " + L_KIRI_TENT +
  SAY((1, N16_SPEAKER, "upper left", "MEI TERUMI. DUAL BLOODLINE HOLDER. REBEL LEADER."),
      (3, MEI_V4_SPEAKER, "upper right", "AND YOU ARE?"),
      (5, N16_SPEAKER, "lower left", "NARUTO. UZUMAKI OR UCHIHA."),
      (6, MEI_V4_SPEAKER, "lower right", "THEN, UCHIHA UZUMAKI NARUTO.")),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "mei_v4", "env_mei_tent"), "high"),

 ("p12", dict(scene="separation", light="tent", cast="four", mood="guarded", panels=6),
  FILL + N16_ARMOR.format(i=1) + YUGAO_V4.format(i=2) + AO_V4.format(i=3) + MEI_V4.format(i=4) +
  GUNBAI_V4.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER, AO_V4_SPEAKER, MEI_V4_SPEAKER) +
  "SIX uneven panels. PANEL 1: Mei issues the instruction while Ao's cropped shoulder objects in "
  "foreground. PANEL 2: Yugao hesitates, protective and concerned for Naruto rather than jealous. "
  "PANEL 3: Naruto gives her a blank, self-possessed look. PANEL 4 (dominant): Yugao and Ao exit "
  "on opposite depth planes, leaving Naruto small by Mei's desk. PANEL 5: Naruto unstraps the dark "
  "purple gunbai and sets it beside his chair. PANEL 6: Mei and Naruto remain separated by desk "
  "space. The gunbai is a named prop and must match its reference. " + L_KIRI_TENT +
  SAY((1, MEI_V4_SPEAKER, "upper left", "AO, SHOW YUGAO THE CAMP."),
      (3, N16_SPEAKER, "lower right", "GO."),
      (6, MEI_V4_SPEAKER, "upper left", "WHY ARE YOU HERE?"),
      (6, N16_SPEAKER, "lower right", "I AM OFFERING MY SERVICES.")),
  R("naruto_v4_armor", "yugao_v4", "ao_v4", "mei_v4", "gunbai_v4", "env_mei_tent"), "high"),

 ("p13", dict(scene="negotiation", light="tent", cast="two", mood="testing", panels=7),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "SEVEN uneven panels, conversation conveyed through movement and scale. PANEL 1: Naruto small "
  "beyond the desk, gunbai resting beside his chair. PANEL 2: Mei's intent close-up. PANEL 3: a "
  "war-map detail with only illegible marks and an abstract off-panel-force marker, never Yagura's "
  "body. PANEL 4 (dominant broad): Mei cropped in foreground, Naruto smaller across the desk; the "
  "negative space is their disagreement. PANEL 5: Naruto's one thin, non-warm smile. PANEL 6: Mei "
  "does not yield. PANEL 7: the warm lamp against storm-dark tent wall. Naruto is here to test his "
  "strength and jutsu, without Konoha authorization. " + L_KIRI_TENT +
  SAY((1, MEI_V4_SPEAKER, "upper left", "DID KONOHA SEND YOU?"),
      (2, N16_SPEAKER, "upper right", "THE HOKAGE DOES NOT KNOW I AM HERE."),
      (4, N16_SPEAKER, "lower left", "I CAME TO TEST MY STRENGTH AND MY JUTSU. YAGURA MUST BE STOPPED."),
      (6, MEI_V4_SPEAKER, "upper right", "ONE PERSON CHANGES NOTHING."),
      (7, N16_SPEAKER, "lower left", "NUMBERS ARE NOT THE POINT. QUALITY IS.")),
  R("naruto_v4_armor", "mei_v4", "gunbai_v4", "env_mei_tent"), "high"),

 ("p14", dict(scene="reveal", light="tent", cast="two", mood="grave", panels=5),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + GUNBAI_V4.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER) +
  "FIVE uneven panels with deliberate negative space. PANEL 1: Mei leans in only to hear Naruto's "
  "low professional whisper, alert and controlled. PANEL 2: Naruto's level mouth. PANEL 3 "
  "(dominant): their profiles close over the near edge of the desk as Naruto gives the private "
  "reveal; they do not touch, exchange no soft looks, and the framing is explicitly non-romantic. "
  "PANEL 4: Mei's widened eye. PANEL 5: empty storm-dark canvas outside the tent, rain and lamp "
  "glow only. The Kyubi is a future promise; do not depict it, a transformation, a tower, or a "
  "fight. " + L_KIRI_TENT +
  SAY((3, N16_SPEAKER, "upper left", "I CAN BRING THE KYUBI AGAINST YAGURA'S FORCES."),
      (4, MEI_V4_SPEAKER, "upper right", "THE KYUBI WAS SEALED."),
      (5, N16_SPEAKER, "lower left", "NOT ANYMORE. YOU WILL SEE IT IN DAYS."),
      (5, MEI_V4_SPEAKER, "lower right", "THEN I WILL TAKE YOUR HELP.")),
  R("naruto_v4_armor", "mei_v4", "gunbai_v4", "env_mei_tent"), "high"),

 ("p15", dict(scene="transition", light="dusk", cast="group", mood="settling", panels=6),
  FILL + N16_ARMOR.format(i=1) + MEI_V4.format(i=2) + N16_BLACK.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, CAMPERS) +
  "SIX uneven transition panels. PANEL 1: Mei leads armoured Naruto down a wet camp path, residents "
  "kept distant and varied. PANEL 2: Naruto turns toward a small assigned tent. PANEL 3: Mei stays "
  "outside the threshold, leading rather than lingering. PANEL 4 (dominant): Naruto alone inside "
  "the tent after removing his armour off-panel; he now wears only the plain black under-suit, with "
  "no forehead protector, gunbai, or sword; his visible LEFT eye remains a blood-red three-tomoe "
  "Sharingan and the RIGHT eye stays beneath the long bang. PANEL 5: the red armour set aside as an object, not a "
  "second person. PANEL 6: Naruto lies awake, isolated by the tent's dark upper space. This is a "
  "time transition for one person, not two Narutos. " + L_CAMP +
  SAY((2, MEI_V4_SPEAKER, "upper left", "WE DISCUSS TERMS TOMORROW."),
      (3, N16_SPEAKER, "lower right", "SEPARATE TENTS.")),
  R("naruto_v4_armor", "mei_v4", "naruto_v4_black", "env_kiri_rebel_camp"), "high"),

 ("p16", dict(scene="private_talk", light="dusk", cast="two", mood="uneasy", panels=7),
  FILL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) + ENV.format(i=4) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
  "SEVEN uneven panels inside Naruto's plain camp tent. PANEL 1: Yugao enters, foreground/back to "
  "camera, while Naruto lies low on the far side of the bed. PANEL 2: separate close-up of Yugao's "
  "concern. PANEL 3: Naruto's flat reply. PANEL 4 (dominant): the two seated far apart with clear "
  "space between them; no intimate pose and no shared-bed framing. PANEL 5: a small inset memory "
  "of an empty Konoha council chamber, no people and no current-location change. PANEL 6: Naruto's "
  "hand relaxed but unyielding, his visible LEFT eye a blood-red three-tomoe Sharingan while the "
  "RIGHT remains beneath his long bang. "
  "PANEL 7: Yugao's alarmed moral reaction. " + L_CAMP +
  SAY((1, YUGAO_V4_SPEAKER, "upper left", "KONOHA REFUSED THE REBELS BEFORE."),
      (3, N16_SPEAKER, "upper right", "THAT MAKES THIS EASIER."),
      (4, YUGAO_V4_SPEAKER, "lower left", "YOU DO NOT FEAR THE ELDERS?"),
      (6, N16_SPEAKER, "lower right", "THEY CANNOT CONTROL ME. IF BANISHED, I LEAVE—AND RETURN WHEN THEY ARE GONE.")),
  R("naruto_v4_black", "yugao_v4", "env_kiri_rebel_camp", "env_konoha_council_chamber"), "high"),

 ("p17", dict(scene="aftermath", light="night", cast="two", mood="quiet", panels=6),
  FILL + N16_BLACK.format(i=1) + YUGAO_V4.format(i=2) + ENV.format(i=3) +
  ONLY(N16_SPEAKER, YUGAO_V4_SPEAKER) +
  "SIX uneven panels, quiet and restrained. PANEL 1: rain and mist against Naruto's tent wall. "
  "PANEL 2: Yugao asks how long, foregrounded at a cautious distance. PANEL 3: Naruto's response. "
  "PANEL 4 (dominant): an unlettered object-memory of a sheathed sword resting on a plain Wave "
  "shop counter, no sign and no named person; Naruto and Yugao are seen only as small separate "
  "reaction insets at different depths. PANEL 5: Yugao's relief. PANEL 6: she leaves through the "
  "tent flap, Naruto still alone; his visible LEFT eye remains a blood-red three-tomoe Sharingan "
  "and his RIGHT eye stays hidden beneath the long bang. Do not make the exchange romantic. " + L_CAMP +
  SAY((2, N16_SPEAKER, "upper left", "TWO OR THREE WEEKS."),
      (3, YUGAO_V4_SPEAKER, "upper right", "WILL YOU RETURN TO KONOHA?"),
      (3, N16_SPEAKER, "lower left", "NOT YET."),
      (4, YUGAO_V4_SPEAKER, "upper right", "THEN I WILL STAY AND GET USED TO KIRI."),
      (4, YUGAO_V4_SPEAKER, "lower left", "MY SWORD?"),
      (5, N16_SPEAKER, "lower left", "AT KISARA'S WEAPONS SHOP IN WAVE. YOU CAN RECLAIM IT WHEN YOU RETURN."),
      (6, YUGAO_V4_SPEAKER, "lower right", "THANK YOU.")),
  R("naruto_v4_black", "yugao_v4", "env_kiri_rebel_camp"), "high"),

 ("p18", dict(scene="aftermath", light="night", cast="three", mood="watchful", panels=6),
  FILL + N16_BLACK.format(i=1) + MEI_V4.format(i=2) + AO_V4.format(i=3) + MANGEKYO_EYE.format(i=4) + ENV.format(i=5) + ENV.format(i=6) +
  ONLY(N16_SPEAKER, MEI_V4_SPEAKER, AO_V4_SPEAKER) +
  "SIX uneven parallel-aftermath panels. PANEL 1: Naruto alone in a small black-and-blue panel, "
  "bored in a camp with no peace. A rain-shifted long bang parts for this one panel: his visible "
  "LEFT eye is blood-red three-tomoe Sharingan, while the newly revealed RIGHT eye carries the "
  "canonical active six-bladed Mangekyo pattern. PANEL 2: wet command-tent exterior and its single "
  "lamp. PANEL 3: Ao arrives in Mei's tent. PANEL 4 (dominant): Mei and Ao at staggered depths over "
  "an illegible map, Ao guarded in foreground and Mei measured beyond him. PANEL 5: Mei's hand "
  "settling beside the lamp. PANEL 6: the command-tent lamp in wet night, the off-panel pressure of "
  "Yagura unresolved. Do not introduce Chojuro, the hill, a tower, or any battle. " + L_KIRI_TENT +
  SAY((4, AO_V4_SPEAKER, "upper left", "THE WOMAN IS HONEST. NARUTO BROUGHT HER HERE AFTER SAVING HER."),
      (5, MEI_V4_SPEAKER, "lower right", "THEN ACCEPTING HIS HELP WAS RIGHT.")),
  R("naruto_v4_black", "mei_v4", "ao_v4", "mangekyo_design", "env_kiri_rebel_camp", "env_mei_tent"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch07" / "raw", HERE / "v4ch07" / "ledger.json")
