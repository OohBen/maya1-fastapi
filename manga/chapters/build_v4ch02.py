"""Volume 4, Chapter 2 — "Not Cut Out For It". 16 pages.

Source: fic ch08:95-201. The chapter holds one continuous chain: Sasuke's bid for kinship,
Jiraiya's bid for an apprentice, and Naruto's promise to the imprisoned Kyubi.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts_v4 import (CAP, ENV, FILL, JIR, KURAMA_INNER, KURAMA_SPEAKER,  # noqa: E402
                        MANGEKYO_EYE, N13, ONLY, OFF, R, SAS, SAY, SFX, THOUGHT,
                        BOY, SAGE, UCH)


L_APARTMENT = "Lighting: cold late-afternoon to night single-bulb light, sparse apartment shadows. "
L_SEWER = "Lighting: cold blue-grey reflected water under black brick depth; red is only the fox's eyes. "

PAGES = [
 ("p01", dict(scene="establishing", light="overcast", cast="two", mood="guarded", panels=5),
  FILL + N13.format(i=1) + SAS.format(i=2) + ENV.format(i=3) + ONLY(BOY, UCH) +
  "FIVE panels, uneven, with a large opening panel and narrow interruption panels below it. "
  "PANEL 1 (dominant, upper): wide exterior of late-afternoon Konoha under dull post-invasion clouds; "
  "the blond boy is a tiny black-clad figure at his apartment window. Keep the calm upper third clear. "
  "PANEL 2 (medium): from behind his shoulder at a neat low table, maps and sealed notes arranged with "
  "geometric precision under a cold single bulb. PANEL 3 (small): extreme close-up of his blue left eye "
  "under the long right bang. PANEL 4 (narrow): a knock at the door; his head turns without alarm. "
  "PANEL 5 (wide, bottom): low angle from inside as the door opens and the dark-haired boy is a small "
  "figure in the hall behind the blond boy's cropped foreground shoulder. No one else is visible. " + L_APARTMENT +
  CAP(3, "upper right", "HE HAD ENEMIES TO PREPARE HIMSELF FOR. KONOHA COULD WAIT.")
  + SAY((5, BOY, "lower left", "WHAT CAN I DO FOR YOU?"))
  + SFX(4, "KNOCK", "Small, beside the door; do not cover the blond boy."),
  R("naruto_13", "sasuke", "env_apartment_int"), "high"),

 ("p02", dict(scene="dialogue", light="overcast", cast="two", mood="guarded", panels=6),
  FILL + SAS.format(i=1) + N13.format(i=2) + ENV.format(i=3) + ONLY(UCH, BOY) +
  "SIX panels, uneven, with the floor's negative space separating them. PANEL 1 (dominant, upper): "
  "the dark-haired boy enters and studies the tidy apartment floor instead of looking at the blond boy. "
  "PANEL 2 (small): clenched hand beside his thigh. PANEL 3 (medium): profile close-up as he asks the "
  "question. PANEL 4 (small): the blond boy remains seated in three-quarter back view. PANEL 5 (thin "
  "eye-strip): frustration changes to brief unwanted hope. PANEL 6 (wide, bottom): the two boys at "
  "opposite depths, blond boy large and cropped in foreground, dark-haired boy small by the door. " + L_APARTMENT +
  CAP(6, "upper right", "IF NARUTO WAS UCHIHA, SASUKE WAS NOT ALONE ANYMORE.")
  + SAY((3, UCH, "upper left", "ARE YOU REALLY AN UCHIHA?"),
        (4, BOY, "upper right", "I HAVE ALREADY GIVEN YOU AN ANSWER TO THAT.")),
  R("sasuke", "naruto_13", "env_apartment_int"), "high"),

 ("p03", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + N13.format(i=2) + MANGEKYO_EYE.format(i=3) + ENV.format(i=4) + ONLY(UCH, BOY) +
  "SIX panels, uneven. PANEL 1 (small): over the dark-haired boy's shoulder, the blond boy's face is "
  "deliberately blank. PANEL 2 (small): his flat answer. PANEL 3 (medium): dark-haired face cropped "
  "at the brow as he asks who was lost. PANEL 4 (narrow letterbox): the blond boy's custom Mangekyo "
  "appears for one beat, then his visible eye returns blue; do not depict a victim or flashback. PANEL 5 "
  "(dominant, middle): he turns the question aside and names the Naka Shrine. PANEL 6 (wide, bottom): "
  "the dark-haired boy recoils half a step at Naruto knowing the shrine and tablet; leave the bottom-right "
  "open. " + L_APARTMENT +
  SAY((1, UCH, "upper left", "WHY DIDN'T YOU EVER SAY ANYTHING TO ME?"),
        (2, BOY, "upper right", "BECAUSE I DID NOT WANT TO."),
        (3, UCH, "lower left", "WHO DID YOU KILL TO AWAKEN THEM?"),
        (5, BOY, "upper left", "THE NAKA SHRINE. YOU ARE MAKING USE OF IT."),
        (6, UCH, "upper right", "YOU KNOW ABOUT IT? HOW?")),
  R("sasuke", "naruto_13", "mangekyo_design", "env_apartment_int"), "high"),

 ("p04", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + SAS.format(i=1) + N13.format(i=2) + ENV.format(i=3) + ONLY(UCH, BOY) +
  "FIVE panels, uneven. PANEL 1 (small): the dark-haired boy in medium close-up, black hair and high "
  "collar sharp against a white field. PANEL 2 (small): the blond boy corrects him without triumph. "
  "PANEL 3 (dominant, middle): depth-staggered room, dark-haired boy tiny in the far room while the "
  "blond boy's dark shoulder fills the near foreground. PANEL 4 (small): the dark-haired boy swallowing "
  "pride, no dialogue. PANEL 5 (wide, bottom): the blond boy ends the visit, gaze moving past him toward "
  "something unseen within the apartment. " + L_APARTMENT +
  SAY((1, UCH, "upper left", "I REALLY DON'T LIKE YOU, NARUTO."),
        (2, BOY, "upper right", "NO. YOU JUST ENVY ME."),
        (3, UCH, "upper left", "THERE ARE ONLY TWO UCHIHA LEFT IN KONOHA. WE SHOULD TALK."),
        (5, BOY, "upper right", "ALL IN DUE TIME, SASUKE. NOW I MUST TELL YOU TO LEAVE.")),
  R("sasuke", "naruto_13", "env_apartment_int"), "high"),

 ("p05", dict(scene="dialogue", light="overcast", cast="three", mood="uneasy", panels=5),
  FILL + N13.format(i=1) + JIR.format(i=2) + SAS.format(i=3) + ENV.format(i=4) + ONLY(BOY, SAGE, UCH) +
  "FIVE panels, uneven. PANEL 1 (small): the dark-haired boy exits into the hall from behind while the "
  "blond boy is only a dark partial silhouette in the doorway; he does not reappear after this panel. "
  "PANEL 2 (small): the door closed and one beat of cold empty room. PANEL 3 (medium): the blond boy "
  "faces the empty room and detects a crossed barrier. PANEL 4 (dominant, middle): the white-haired man "
  "materializes in the rear corner, partially occluded by the blond boy's enormous foreground shoulder; "
  "his reaction is sheepish, not heroic. PANEL 5 (wide, bottom): gloved hand beside a faint seal-marked "
  "floor edge; the white-haired man's widened eye and sweat bead are visible beyond it. " + L_APARTMENT +
  SAY((3, BOY, "upper left", "YOU BROKE THROUGH MY BARRIER."),
        (5, BOY, "upper left", "YOU ARE LUCKY I WAS INSIDE. THIS APARTMENT WOULD HAVE SELF DESTRUCTED.")),
  R("naruto_13", "jiraiya", "sasuke", "env_apartment_int"), "high"),

 ("p06", dict(scene="dialogue", light="overcast", cast="two", mood="guarded", panels=6),
  FILL + JIR.format(i=1) + N13.format(i=2) + ENV.format(i=3) + ONLY(SAGE, BOY) +
  "SIX panels, uneven. PANEL 1 (small): the white-haired man leans into the room, probing the extreme "
  "defence. PANEL 2 (small): the blond boy gives no answer. PANEL 3 (dominant, middle): the white-haired "
  "man sits beside him but they are at different depths, never companionably side by side. PANEL 4 "
  "(medium): he asks about the Sharingan and Naruto's parents. PANEL 5 (small): Naruto sends the "
  "spymaster to investigate. PANEL 6 (wide, bottom): levity gone from the white-haired man's face as he "
  "warns of a mind search; do not show the council. " + L_APARTMENT +
  SAY((1, SAGE, "upper left", "WHAT COULD YOU HAVE HIDDEN IN HERE?"),
        (2, BOY, "upper right", "MIGHT BE SO. WHAT DO YOU WANT?"),
        (4, SAGE, "upper left", "HOW CAN YOU USE THE SHARINGAN? I KNEW BOTH OF YOUR PARENTS."),
        (5, BOY, "upper right", "USE YOUR SPY NETWORK AND GATHER INTEL ON ME."),
        (6, SAGE, "upper left", "THE COUNCIL MAY FORCE SOMEONE TO ENTER YOUR MIND.")),
  R("jiraiya", "naruto_13", "env_apartment_int"), "high"),

 ("p07", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + JIR.format(i=2) + ENV.format(i=3) + ONLY(BOY, SAGE) +
  "FIVE panels, uneven. PANEL 1 (small): Naruto's blue eye, level and unafraid. PANEL 2 (small): the "
  "white-haired man changes tack. PANEL 3 (small): Naruto remains seated and refuses. PANEL 4 "
  "(dominant, middle): the white-haired man's open hand looms large in foreground as he explains the "
  "Tsunade-search mission, while Naruto stays smaller beyond it. PANEL 5 (wide, bottom): Naruto's refusal "
  "lands; end on the white-haired man's narrowed considering gaze. " + L_APARTMENT +
  SAY((1, BOY, "upper left", "MAKE ME? I WOULD LIKE TO SEE THEM TRY."),
        (2, SAGE, "upper right", "I CAME WITH YOU FOR A MISSION WHICH YOU WILL DO WITH ME."),
        (3, BOY, "upper left", "I'M NOT INTERESTED IN DOING A MISSION WITH YOU."),
        (4, SAGE, "upper left", "WE HAVE TO FIND MY FORMER TEAMMATE AND CONVINCE HER TO BE HOKAGE."),
        (5, BOY, "upper right", "IF YOU FORCE ME OUTSIDE THE VILLAGE, I WON'T RETURN.")),
  R("naruto_13", "jiraiya", "env_apartment_int"), "high"),

 ("p08", dict(scene="dialogue", light="overcast", cast="two", mood="tense", panels=6),
  FILL + JIR.format(i=1) + N13.format(i=2) + ENV.format(i=3) + ONLY(SAGE, BOY) +
  "SIX panels, uneven. PANEL 1 (dominant, upper): a long quiet panel, white-haired silhouette filling "
  "the doorway while the blond boy remains unmoved at the table. PANEL 2 (small): Jiraiya frames the trip "
  "as service. PANEL 3 (small): Naruto's closed face rejects that frame. PANEL 4 (small): Minato's name "
  "is invoked. PANEL 5 (nearly blank close-up): Naruto has no visible reaction. PANEL 6 (wide, bottom): "
  "Naruto names the real aim; the white-haired man is small at the edge, caught but not villainized. " + L_APARTMENT +
  CAP(5, "upper right", "MINATO'S OPINION MEANT NOTHING TO HIM.")
  + SAY((2, SAGE, "upper left", "YOU WILL BE RENDERING A SERVICE TO KONOHA."),
        (4, SAGE, "upper left", "YOUR FATHER WOULD BE DISAPPOINTED IN YOU."),
        (6, BOY, "upper left", "YOU WANT TO GET CLOSE TO ME AND TURN ME INTO YOUR APPRENTICE."),
        (6, BOY, "lower right", "I WOULD SERVE NO PURPOSE IN CONVINCING TSUNADE TO BE HOKAGE.")),
  R("jiraiya", "naruto_13", "env_apartment_int"), "high"),

 ("p09", dict(scene="dialogue", light="night", cast="two", mood="somber", panels=5),
  FILL + N13.format(i=1) + JIR.format(i=2) + ENV.format(i=3) + ONLY(BOY, SAGE) +
  "FIVE panels, uneven. PANEL 1 (small): the white-haired man lowers his shoulders, conceding. PANEL 2 "
  "(small): tired close-up, his request in a small upper-left balloon. PANEL 3 (medium): Naruto says "
  "there is nothing to settle. PANEL 4 (dominant, middle): large quiet profile beneath the cold bulb, "
  "ample shelf above the balloon. PANEL 5 (wide, bottom): the white-haired man accepts the boundary with "
  "a restrained sad smile. No embrace, handshake, or promise of travel. " + L_APARTMENT +
  SAY((2, SAGE, "upper left", "I KNOW I SCREWED UP. CAN'T YOU GIVE ME A CHANCE TO MAKE UP FOR THAT?"),
        (3, BOY, "upper right", "I DON'T HATE YOU FOR ABANDONING ME. THERE IS NOTHING FOR YOU TO SETTLE."),
        (4, BOY, "upper left", "I DON'T NEED EMOTIONAL ATTACHMENTS WITH YOU OR ANYONE."),
        (5, SAGE, "upper right", "I GUESS I WILL SEE YOU WHEN I RETURN WITH THE NEW HOKAGE.")),
  R("naruto_13", "jiraiya", "env_apartment_int"), "high"),

 ("p10", dict(scene="transition", light="night", cast="two", mood="inward", panels=4),
  FILL + N13.format(i=1) + JIR.format(i=2) + ENV.format(i=3) + ONLY(BOY, SAGE) +
  "FOUR panels, uneven. PANEL 1 (small): the white-haired man leaves through the window, white hair and "
  "red haori cropped by the frame; he is exiting and not otherwise on the page. PANEL 2 (medium): empty "
  "apartment with Naruto alone at the table, weighing the private act he has resisted. PANEL 3 (small): "
  "Naruto makes the decision, then closes his eyes as the single-bulb light drops into black. PANEL 4 "
  "(dominant, bottom, borderless): his reflected face fragments "
  "in black water while apartment linework dissolves into wet brick. No fox is visible. " + L_APARTMENT +
  CAP(2, "upper right", "LATER THAT NIGHT")
  + THOUGHT((3, BOY, "upper left", "SOMETHING I HAVE BEEN RELENTING TO DO."))
  + SFX(4, "DRIP", "Small hand-drawn water lettering at the lower edge."),
  R("naruto_13", "jiraiya", "env_apartment_int"), "high"),

 ("p11", dict(scene="establishing", light="dark", cast="two", mood="ominous", panels=5),
  FILL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV.format(i=3) + ONLY(BOY, KURAMA_SPEAKER) +
  "FIVE panels, uneven. PANEL 1 (dominant, upper): full-width establishing panel of an immense old sewer, "
  "water ankle-deep and reflective; Naruto is tiny at centre walking toward a black vanishing point. "
  "PANEL 2 (small): tight downward crop of sandals making ripples. PANEL 3 (vertical): Naruto stops "
  "before a barred gate that overwhelms panel height, paper seal centered high on the bars. PANEL 4 "
  "(small): two giant red eyes open in shadow beyond the gate. PANEL 5 (wide, bottom): low close-up of "
  "heavy fox muzzle and enormous paws behind bars, still mostly shadow; never humanize the fox. " + L_SEWER +
  SAY((5, KURAMA_SPEAKER, "upper left", "SO MY JAILOR HAS FINALLY DECIDED TO GRACE ME WITH HIS PRESENCE."),
        (5, KURAMA_SPEAKER, "lower right", "HAVE YOU COME TO TELL ME MY PRISON SENTENCE HAS BEEN CUT SHORT?"))
  + SFX(2, "SPLASH", "Small and hand-drawn beside the sandal; do not cover the ripple."),
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "high"),

 ("p12", dict(scene="dialogue", light="dark", cast="two", mood="hostile", panels=6),
  FILL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV.format(i=3) + ONLY(BOY, KURAMA_SPEAKER) +
  "SIX panels, uneven. PANEL 1 (small): Naruto from behind, tiny against the gate, needling the fox's "
  "captivity. PANEL 2 (small): one red eye tightens in anger. PANEL 3 (narrow): the gate and eye only; "
  "the fox is not otherwise visible in this panel. PANEL 4 (medium): Naruto side profile, waterline at "
  "his sandals, observing the seal's limited strength. PANEL 5 (small symbolic inset): two complementary "
  "red-orange chakra shapes divided by a black seal fissure; no Minato or flashback. PANEL 6 (dominant, "
  "bottom): Naruto names the missing half as the fox falls silent. " + L_SEWER +
  SAY((1, BOY, "upper left", "IS THIS WHAT THE GREAT KYUUBI HAS BEEN REDUCED TO?"),
        (3, OFF(KURAMA_SPEAKER), "upper right", "THIS CAGE CANNOT HOLD ME FOREVER."),
        (4, BOY, "upper left", "IF YOU WERE COMPLETE, YOU WOULD HAVE ALREADY BROKEN OUT."),
        (6, BOY, "upper right", "YOUR OTHER HALF IS MISSING. THAT IS WHY YOU ARE NOT WHOLE.")),
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "high"),

 ("p13", dict(scene="dialogue", light="dark", cast="two", mood="grave", panels=5),
  FILL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV.format(i=3) + ONLY(BOY, KURAMA_SPEAKER) +
  "FIVE panels, uneven. PANEL 1 (dominant, upper): Naruto is small in a wide black-water panel, speaking "
  "toward the caged fox. PANEL 2 (small): fox eye changing from anger to attention. PANEL 3 (medium): "
  "Naruto states the insult in calling a being like this mindless. PANEL 4 (vertical): the paper seal "
  "divides Naruto from the enormous eye. PANEL 5 (wide, bottom): close-up of Naruto's level face; the "
  "promise is not a power boast. " + L_SEWER +
  SAY((1, BOY, "upper left", "I KNOW HUMANS TREATED YOUR KIND AS WEAPONS RATHER THAN PEOPLE."),
        (3, BOY, "upper right", "YOU ARE NOT A MINDLESS BEAST THAT NEEDS TO BE GUIDED."),
        (5, BOY, "upper left", "AS FOR YOUR IMPERFECTION, I PLAN TO FIX THAT.")),
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "high"),

 ("p14", dict(scene="emotional_closeup", light="dark", cast="two", mood="somber", panels=4),
  FILL + N13.format(i=1) + KURAMA_INNER.format(i=2) + ENV.format(i=3) + ONLY(BOY, KURAMA_SPEAKER) +
  "FOUR panels, uneven. PANEL 1 (dominant, upper): Naruto turns away from the gate, reflected upside-down "
  "in water; he promises the prison will end in time. PANEL 2 (small): the fox pupil tightens, with Naruto "
  "a small receding figure so scale and vulnerability belong to the caged creature. PANEL 3 (medium): "
  "silent shadowed memory-impression of chains, barred horizon, and tiny ambiguous beast silhouettes; no "
  "named historical character and no new text. PANEL 4 (wide, bottom): Naruto vanishes from the sewer, "
  "leaving ripples spreading toward the gate, a quiet exit without teleportation spectacle. " + L_SEWER +
  SAY((1, BOY, "upper left", "FOR YOUR PRISON SENTENCE, YOU WILL HAVE YOUR FREEDOM SOON.")),
  R("naruto_13", "kurama_inner", "env_inner_sewer"), "high"),

 ("p15", dict(scene="emotional_closeup", light="dark", cast="solo", mood="distrustful", panels=3),
  FILL + KURAMA_INNER.format(i=1) + ENV.format(i=2) + ONLY(KURAMA_SPEAKER) +
  "THREE panels, uneven. PANEL 1 (small): the sewer is still; one red eye remains in darkness beyond the "
  "gate. PANEL 2 (dominant, middle): the fox rests its head on huge paws, much smaller than the gate but "
  "still vast. PANEL 3 (narrow bottom): close-up of the seal paper, red eye blurred behind it. Do not "
  "resolve the promise or soften the fox. " + L_SEWER +
  CAP(2, "upper left", "HUMANS HAD PROVED THEY COULD NOT BE TRUSTED.")
  + CAP(3, "lower right", "THE BIJUU WERE NOTHING BUT WEAPONS TO THEM."),
  R("kurama_inner", "env_inner_sewer"), "high"),

 ("p16", dict(scene="splash", light="dark", cast="solo", mood="unresolved", panels=1),
  KURAMA_INNER.format(i=1) + ENV.format(i=2) + ONLY(KURAMA_SPEAKER) +
  "CHAPTER ENDING BORDERLESS SPLASH. From inside the cage, one immense red slit eye occupies most of the "
  "page behind black bars and the centered paper seal. The fox is vast, imprisoned, and wholly distrustful. "
  "At the very bottom, Naruto's departing water ripples survive only as a tiny reflection; Naruto himself "
  "does not appear. Keep the upper-left quiet for end treatment. No opened bars, softened expression, or "
  "additional character. " + L_SEWER,
  R("kurama_inner", "env_inner_sewer"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch02" / "raw", HERE / "v4ch02" / "ledger.json")
