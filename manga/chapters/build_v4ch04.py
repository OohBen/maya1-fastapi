"""Volume 4, Chapter 4 — "Two Weeks". 20 pages.

Source: fic ch8:267-547.  Naruto has already left alone before the office
meeting; the Naruto who receives Jiraiya's proposal is his clone.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                          # noqa: E402
from prompts_v4 import (CAP, DAN, ENV, FILL, JIR, KAK, N13, ONLY, OFF, R, SAK, # noqa: E402
                        SAS, SAY, SFX, SHI, ZET, HOMURA, KOHARU, SHIKAKU,
                        SHIZUNE, TSUNADE, HIASHI, TSUME, MANGEKYO_EYE,
                        HIASHI_SPEAKER, TSUME_SPEAKER)

NARUTO = "the long-haired blond thirteen-year-old in black"
SHIKAMARU = "the black-haired boy with the pineapple ponytail"
JIRAIYA = "the big white-haired man"
DANZO = "the bandaged old man with the cane"
KAKASHI = "the masked silver-haired man"
SASUKE = "the dark-haired boy"
SAKURA = "the pink-haired girl"
ZETSU = "the split black-and-white plant creature"
COUNCIL = "unnamed seated council members"
TSUNADE_SPEAKER = "the blonde woman in the green haori"
SHIZUNE_SPEAKER = "the dark-haired medical aide"

L_DAY = "Lighting: clean flat Konoha daylight, with hard ink shadows and no warm glow. "
L_HIDEOUT = "Lighting: near-black stone, hard white rim light, no warm palette and no glow. "

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="small_group", mood="tense", panels=5),
  FILL + TSUNADE.format(i=1) + SHIZUNE.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(TSUNADE_SPEAKER, SHIZUNE_SPEAKER, NARUTO, "unnamed villagers")
  + "FIVE panels, uneven. The return is public aftermath, never a recruitment journey.\n"
  "PANEL 1 (small): reconstructed roofline under flat daylight.\n"
  "PANEL 2 (dominant, upper): Konoha gate crowd from inside overlapping shoulders and banners; the "
  "new Hokage is small and partly hidden, her aide at a different depth.\n"
  "PANEL 3 (small): low angle on the green haori against the Hokage building.\n"
  "PANEL 4 (small): Naruto, tiny and back-turned on an apartment roof, watching from far away.\n"
  "PANEL 5 (wide, bottom): his visible eye, level and not celebratory. " + L_DAY
  + CAP(5, "upper right", "HE HAS ALREADY PREPARED TO LEAVE."),
  R("tsunade", "shizune", "naruto_13", "env_konoha_after_invasion"), "high"),

 ("p02", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + TSUNADE.format(i=1) + SHIZUNE.format(i=2) + JIR.format(i=3) + N13.format(i=4)
  + SHI.format(i=5) + ENV.format(i=6)
  + ONLY(TSUNADE_SPEAKER, SHIZUNE_SPEAKER, JIRAIYA, NARUTO, SHIKAMARU)
  + "SIX panels, uneven, in Tsunade's office.\n"
  "PANEL 1 (small): two chuunin flak jackets on the desk, seen from above.\n"
  "PANEL 2 (small): Shikamaru arrives through Jiraiya's cropped window-side shoulder.\n"
  "PANEL 3 (small): Naruto's brief private smile against white.\n"
  "PANEL 4 (small): Jiraiya notices it, puzzled.\n"
  "PANEL 5 (dominant, middle): Tsunade behind the desk, Jiraiya cropped in the window foreground, "
  "the two boys at different mid-depths; she announces the promotions.\n"
  "PANEL 6 (wide, bottom): the jackets arc separately toward them; neither celebrates. " + L_DAY
  + SAY((2, SHIKAMARU, "upper left", "OF COURSE THIS IS TROUBLESOME."),
        (3, NARUTO, "upper right", "YOU MAKE EVERYTHING SOUND THAT WAY."),
        (5, TSUNADE_SPEAKER, "upper left", "THE EXAM JUDGES HAVE PROMOTED YOU BOTH.")),
  R("tsunade", "shizune", "jiraiya", "naruto_13", "shikamaru", "env_hokage_office"), "high"),

 ("p03", dict(scene="transition", light="day", cast="small_group", mood="tense", panels=5),
  FILL + TSUNADE.format(i=1) + JIR.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(TSUNADE_SPEAKER, JIRAIYA, NARUTO, "unnamed council attendants")
  + "FIVE panels, uneven.\n"
  "PANEL 1 (small): Tsunade directs Naruto toward the council chamber.\n"
  "PANEL 2 (small): Naruto sets the unused flak jacket over one arm; he remains in black.\n"
  "PANEL 3 (small): Jiraiya's sandals stop at the threshold.\n"
  "PANEL 4 (dominant, upper): from behind a cropped attendant, Naruto walks small between Tsunade "
  "and Jiraiya toward tall chamber doors.\n"
  "PANEL 5 (wide, bottom): Naruto crosses alone into the black doorway, with quiet clear space "
  "above him for the next page's pressure. " + L_DAY
  + SAY((1, TSUNADE_SPEAKER, "upper left", "COME TO THE COUNCIL CHAMBER.")),
  R("tsunade", "jiraiya", "naruto_13", "env_konoha_council_chamber"), "high"),

 ("p04", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=7),
  FILL + N13.format(i=1) + TSUNADE.format(i=2) + JIR.format(i=3) + DAN.format(i=4)
  + SHIKAKU.format(i=5) + HIASHI.format(i=6) + TSUME.format(i=7) + ENV.format(i=8)
  + ONLY(NARUTO, TSUNADE_SPEAKER, JIRAIYA, DANZO, "the man with the long pineapple ponytail",
         HIASHI_SPEAKER, TSUME_SPEAKER, COUNCIL)
  + "SEVEN panels, uneven. Never stage the council as an even line.\n"
  "PANEL 1 (dominant, upper): bird's-eye chamber: Naruto alone at the foot of a long table; "
  "irregular councillor layers ring him, Tsunade at the Hokage seat and Jiraiya behind.\n"
  "PANEL 2 (small): Tsunade offers a chair; Naruto composed.\n"
  "PANEL 3 (small): Naruto's visible eye scans the room.\n"
  "PANEL 4 (narrow): Hiashi's pale-eyed silhouette, partially obscured.\n"
  "PANEL 5 (small): Shikaku watches in shadow.\n"
  "PANEL 6 (small): Tsume leans forward from the layered table.\n"
  "PANEL 7 (wide, bottom): Naruto's plain answer in a small composition. " + L_DAY
  + SAY((6, TSUME_SPEAKER, "upper left", "ARE YOU TRULY UCHIHA?"),
        (7, NARUTO, "upper left", "YES.")),
  R("naruto_13", "tsunade", "jiraiya", "danzo", "shikaku", "hiashi", "tsume",
    "env_konoha_council_chamber"), "high"),

 ("p05", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + N13.format(i=1) + DAN.format(i=2) + HOMURA.format(i=3) + TSUNADE.format(i=4)
  + JIR.format(i=5) + ENV.format(i=6)
  + ONLY(NARUTO, DANZO, "the elderly male adviser in dark formal robes", TSUNADE_SPEAKER, JIRAIYA, COUNCIL)
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): Danzo asks how Naruto can be Uchiha.\n"
  "PANEL 2 (small): Naruto's still profile refuses the family question.\n"
  "PANEL 3 (small): Homura presses from behind foreground papers.\n"
  "PANEL 4 (dominant, middle): extreme low angle past the table edge toward Naruto, which blocks "
  "half his body and makes the room enormous.\n"
  "PANEL 5 (small): deserted institutional corridor, an object-memory rather than a flashback crowd.\n"
  "PANEL 6 (wide, bottom): Tsunade and Jiraiya exchange a difficult look. " + L_DAY
  + SAY((4, NARUTO, "upper left", "I WILL ANSWER FOR MY DUTY. MY BLOOD IS NOT YOURS TO INVENTORY."),
        (4, NARUTO, "lower right", "YOU WITHHELD MY FAMILY, THEN DEMAND I EXPLAIN IT.")),
  R("naruto_13", "danzo", "homura", "tsunade", "jiraiya", "env_konoha_council_chamber"), "high"),

 ("p06", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + N13.format(i=1) + SHIKAKU.format(i=2) + ENV.format(i=3)
  + ONLY(NARUTO, "the man with the long pineapple ponytail", COUNCIL)
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): an anonymous councillor demands an answer.\n"
  "PANEL 2 (small): Naruto turns the question back toward those who knew his parents.\n"
  "PANEL 3 (small): Shikaku's faint knowing smile.\n"
  "PANEL 4 (small): another anonymous demand: why hide the Sharingan?\n"
  "PANEL 5 (dominant, middle): Naruto's cropped face at the right third; councillors tiny at far "
  "left with a clean balloon gap between.\n"
  "PANEL 6 (wide, bottom): confused, angry, and silent reactions at four different depths. " + L_DAY
  + SAY((5, NARUTO, "upper left", "AFTER WHAT HAPPENED TO THAT CLAN, SECRECY WAS SURVIVAL.")),
  R("naruto_13", "shikaku", "env_konoha_council_chamber"), "high"),

 ("p07", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=5),
  FILL + N13.format(i=1) + MANGEKYO_EYE.format(i=2) + JIR.format(i=3) + DAN.format(i=4) + ENV.format(i=5)
  + ONLY(NARUTO, JIRAIYA, DANZO, COUNCIL)
  + "FIVE panels, uneven. The active eye is accusation, not emitted light.\n"
  "PANEL 1 (small): Jiraiya asks for a direct answer, dissatisfied.\n"
  "PANEL 2 (small): Naruto turns his back to the table against white.\n"
  "PANEL 3 (small): he makes Konoha's treatment the subject of the room.\n"
  "PANEL 4 (dominant, letterbox): the six-blade Mangekyo in hard black hatching; councillors "
  "reflect in it, no glow.\n"
  "PANEL 5 (wide, bottom): Danzo's narrowed silhouette with that eye reflected in the visible eye area. "
  + L_DAY
  + SAY((3, NARUTO, "upper left", "YOU LEFT ME ALONE WITH THAT BURDEN. DO NOT QUESTION WHY I KEPT MY OWN COUNSEL."),
        (3, NARUTO, "lower right", "I STAYED. THAT IS THE ANSWER.")),
  R("naruto_13", "mangekyo_design", "jiraiya", "danzo", "env_konoha_council_chamber"), "high"),

 ("p08", dict(scene="dialogue", light="day", cast="group", mood="tense", panels=6),
  FILL + SHIKAKU.format(i=1) + JIR.format(i=2) + KOHARU.format(i=3) + TSUNADE.format(i=4)
  + N13.format(i=5) + ENV.format(i=6)
  + ONLY("the man with the long pineapple ponytail", JIRAIYA, "the elderly female adviser with the pale hair bun",
         TSUNADE_SPEAKER, NARUTO, COUNCIL)
  + "SIX panels, uneven.\n"
  "PANEL 1 (dominant, upper): Shikaku small at the head of a long negative-space panel, speaking "
  "while layered silhouettes listen.\n"
  "PANEL 2 (small): clan heads at different depths, nodding or withholding judgment.\n"
  "PANEL 3 (small): Jiraiya concedes without becoming pleased.\n"
  "PANEL 4 (small): Koharu's cropped mouth gives a future warning.\n"
  "PANEL 5 (small): Tsunade ends the interrogation sharply.\n"
  "PANEL 6 (wide, bottom): Naruto exits small through a tall sunlit doorway; the council remains behind. " + L_DAY
  + SAY((1, "the man with the long pineapple ponytail", "upper left", "NO PLAN AGAINST KONOHA IS EVIDENCED."),
        (4, "the elderly female adviser with the pale hair bun", "upper right", "NEXT TIME, DISRESPECT WILL BE TREATED AS TREASON."),
        (5, TSUNADE_SPEAKER, "upper left", "HE IS EXCUSED. WE HAVE OTHER BUSINESS.")),
  R("shikaku", "jiraiya", "koharu", "tsunade", "naruto_13", "env_konoha_council_chamber"), "high"),

 ("p09", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=5),
  FILL + TSUNADE.format(i=1) + JIR.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(TSUNADE_SPEAKER, JIRAIYA, NARUTO)
  + "FIVE panels, uneven; next-day office colder and cluttered with reports.\n"
  "PANEL 1 (small): untouched sake bottle and towering paperwork.\n"
  "PANEL 2 (small): Naruto enters, still without the offered jacket.\n"
  "PANEL 3 (dominant, middle): Tsunade at the rear desk, Jiraiya perched in the window, Naruto "
  "seated low left at another depth.\n"
  "PANEL 4 (small): Jiraiya's face turns serious.\n"
  "PANEL 5 (wide, bottom): calm Konoha through the window, danger entirely off-panel. " + L_DAY
  + SAY((3, TSUNADE_SPEAKER, "upper left", "JIRAIYA HAS SOMETHING IMPORTANT TO SAY.")),
  R("tsunade", "jiraiya", "naruto_13", "env_hokage_office"), "high"),

 ("p10", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + JIR.format(i=1) + N13.format(i=2) + ENV.format(i=3)
  + ONLY(JIRAIYA, NARUTO, "generic distant cloud-cloak silhouettes")
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): Jiraiya explains an organisation hunting jinchuriki.\n"
  "PANEL 2 (small): two generic distant cloud-cloak silhouettes under rain, no action flashback.\n"
  "PANEL 3 (small): Jiraiya reaches the name Itachi.\n"
  "PANEL 4 (small): Naruto raises one hand to stop him.\n"
  "PANEL 5 (small): Naruto's visible eye; he already knows.\n"
  "PANEL 6 (dominant, lower): Jiraiya in near-profile foreground, Naruto very small behind him, "
  "with the clean upper gap holding the exchange. " + L_DAY
  + SAY((1, JIRAIYA, "upper left", "THEY ARE HUNTING THE VESSELS."),
        (4, NARUTO, "upper right", "I KNOW WHO THEY ARE."),
        (6, NARUTO, "lower left", "THEY WANT WHAT IS SEALED IN ME.")),
  R("jiraiya", "naruto_13", "env_hokage_office"), "high"),

 ("p11", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + JIR.format(i=1) + TSUNADE.format(i=2) + N13.format(i=3) + ENV.format(i=4)
  + ONLY(JIRAIYA, TSUNADE_SPEAKER, NARUTO)
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): Jiraiya says Naruto cannot meet two S-rank attackers alone.\n"
  "PANEL 2 (small): he offers three years of training.\n"
  "PANEL 3 (small): Naruto begins to refuse.\n"
  "PANEL 4 (dominant, middle): Tsunade lays a signed travel document across the desk; Naruto's "
  "gloved hand does not reach for it.\n"
  "PANEL 5 (small): paper detail, all writing intentional illegible scribble except the seal.\n"
  "PANEL 6 (wide, bottom): Naruto's eye remains flat. " + L_DAY
  + SAY((2, JIRAIYA, "upper left", "TRAIN WITH ME. THREE YEARS."),
        (4, TSUNADE_SPEAKER, "upper right", "YOUR LEAVE IS AUTHORIZED."),
        (6, NARUTO, "upper left", "YOU MISUNDERSTAND. THE REAL NARUTO LEFT TO TRAIN ALONE.")),
  R("jiraiya", "tsunade", "naruto_13", "env_hokage_office"), "high"),

 ("p12", dict(scene="reveal", light="day", cast="small_group", mood="tense", panels=5),
  FILL + N13.format(i=1) + TSUNADE.format(i=2) + JIR.format(i=3) + ENV.format(i=4)
  + ONLY(NARUTO, TSUNADE_SPEAKER, JIRAIYA)
  + "FIVE panels, uneven. The clone reveal must be unmistakable.\n"
  "PANEL 1 (small): Naruto says he has already left Konoha.\n"
  "PANEL 2 (small): Tsunade asks what that means.\n"
  "PANEL 3 (dominant, middle): close crop as Naruto explains he is a clone, while Tsunade and "
  "Jiraiya are distant in separate depth layers.\n"
  "PANEL 4 (small): the empty chair's surrounding negative space becomes the reader's realization.\n"
  "PANEL 5 (wide, bottom): Tsunade and Jiraiya in separate reaction crops, never one shared pose. " + L_DAY
  + SAY((1, NARUTO, "upper left", "I HAVE ALREADY LEFT KONOHA."),
        (3, NARUTO, "upper right", "I AM A CLONE."),
        (3, NARUTO, "lower left", "THE REAL NARUTO IS NOT TRAVELING WITH JIRAIYA.")),
  R("naruto_13", "tsunade", "jiraiya", "env_hokage_office"), "high"),

 ("p13", dict(scene="reveal", light="day", cast="small_group", mood="tense", panels=6),
  FILL + N13.format(i=1) + TSUNADE.format(i=2) + JIR.format(i=3) + ENV.format(i=4)
  + ONLY(NARUTO, TSUNADE_SPEAKER, JIRAIYA)
  + "SIX panels, uneven. Naruto never leaves with Jiraiya.\n"
  "PANEL 1 (small): Tsunade warns that departure without the document risks missing-nin status.\n"
  "PANEL 2 (small): the clone says solitary training was necessary.\n"
  "PANEL 3 (dominant, central vertical): the clone's outline breaks into flat white smoke above the "
  "crisp travel document; no empty balloon, no glowing effect.\n"
  "PANEL 4 (small): empty chair and one smoke curl.\n"
  "PANEL 5 (small): Jiraiya launches from the open window, floor-level through papers and desk edge.\n"
  "PANEL 6 (wide, bottom): Tsunade alone grips the document, angry and worried. " + L_DAY
  + SAY((2, NARUTO, "upper left", "THE AUTHORIZATION HELPS. IT DOES NOT CHANGE THE CHOICE."),
        (5, JIRAIYA, "upper right", "I'LL FIND HIM."))
  + SFX(3, "POFU"),
  R("naruto_13", "tsunade", "jiraiya", "env_hokage_office"), "high"),

 ("p14", dict(scene="transition", light="day", cast="solo", mood="somber", panels=6),
  FILL + TSUNADE.format(i=1) + ENV.format(i=2) + ONLY(TSUNADE_SPEAKER)
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): later that day card.\n"
  "PANEL 2 (small): reports about rebuilding and stability, objects not a prose lecture.\n"
  "PANEL 3 (small): Tsunade rubs her temple; sake remains untouched.\n"
  "PANEL 4 (dominant, middle): her green haori sleeve crushes the travel authorisation over a vast "
  "paperwork field.\n"
  "PANEL 5 (small): Tsunade makes the private decision to preserve the public cover.\n"
  "PANEL 6 (wide, bottom): Hokage tower exterior under a calm sky, empty cutaway. " + L_DAY
  + CAP(1, "upper left", "LATER THAT DAY")
  + CAP(5, "upper right", "OFFICIALLY, NARUTO TRAINS WITH JIRAIYA."),
  R("tsunade", "env_hokage_office"), "high"),

 ("p15", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + TSUNADE.format(i=1) + KAK.format(i=2) + ENV.format(i=3)
  + ONLY(TSUNADE_SPEAKER, KAKASHI, "an abstract serpentine shadow")
  + "SIX panels, uneven; one restrained chibi reaction only.\n"
  "PANEL 1 (small): Kakashi arrives late, reading an orange book.\n"
  "PANEL 2 (small): Tsunade tells him to put it away, with a nonviolent absurd threat.\n"
  "PANEL 3 (small): Kakashi immediately complies, tiny chibi reaction.\n"
  "PANEL 4 (dominant, middle): Tsunade fills left foreground, fist planted by the desk; Kakashi "
  "small right, half hidden by the book.\n"
  "PANEL 5 (small): Kakashi's eye tightens at Sasuke's name.\n"
  "PANEL 6 (wide, bottom): black abstract serpentine/cursed shadow, a concern not an Orochimaru appearance. " + L_DAY
  + SAY((2, TSUNADE_SPEAKER, "upper left", "PUT THE BOOK AWAY OR I WILL HEAL YOU BETWEEN LESSONS."),
        (4, TSUNADE_SPEAKER, "upper right", "I CALLED YOU ABOUT SASUKE.")),
  R("tsunade", "kakashi", "env_hokage_office"), "high"),

 ("p16", dict(scene="dialogue", light="day", cast="small_group", mood="tense", panels=6),
  FILL + TSUNADE.format(i=1) + KAK.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + ENV.format(i=5)
  + ONLY(TSUNADE_SPEAKER, KAKASHI, SASUKE, SAKURA)
  + "SIX panels, uneven.\n"
  "PANEL 1 (small): Tsunade explains that Orochimaru may lure Sasuke with power.\n"
  "PANEL 2 (small): Kakashi acknowledges the danger.\n"
  "PANEL 3 (dominant, middle): Tsunade and Kakashi deeply staggered across the office; a narrow "
  "insert has Sasuke alone in darkness, facing away.\n"
  "PANEL 4 (small): Kakashi accepts a three-year trip for himself and Sasuke.\n"
  "PANEL 5 (small): Tsunade assigns Sakura to medical training based on her chakra control.\n"
  "PANEL 6 (wide, bottom): Naruto's absent seat and the travel document as objects. " + L_DAY
  + SAY((3, TSUNADE_SPEAKER, "upper left", "SASUKE GETS THE TRAINING HE WILL CHASE ELSEWHERE."),
        (5, TSUNADE_SPEAKER, "upper right", "SAKURA TRAINS WITH ME.")),
  R("tsunade", "kakashi", "sasuke", "sakura", "env_hokage_office"), "high"),

 ("p17", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + TSUNADE.format(i=1) + KAK.format(i=2) + ENV.format(i=3)
  + ONLY(TSUNADE_SPEAKER, KAKASHI)
  + "SIX panels, uneven. A privacy-seal motif encloses them; Naruto is absent in the desk's negative space.\n"
  "PANEL 1 (small): Tsunade forms the privacy seal.\n"
  "PANEL 2 (small): she tells Kakashi Naruto has left; he fears defection.\n"
  "PANEL 3 (small): Tsunade corrects him: Naruto is training, but left without permission.\n"
  "PANEL 4 (dominant, middle): the two separated by the wide desk and the empty space where Naruto "
  "would be; Kakashi argues Jiraiya would be safer.\n"
  "PANEL 5 (small): Tsunade says Naruto deliberately avoided a refusal.\n"
  "PANEL 6 (wide, bottom): Kakashi accepts the discreet search while travelling. " + L_DAY
  + SAY((2, TSUNADE_SPEAKER, "upper left", "HE DID NOT DEFECT. HE CHOSE A PLACE WE DO NOT KNOW."),
        (5, TSUNADE_SPEAKER, "upper right", "HE DID NOT NEED JIRAIYA."),
        (6, TSUNADE_SPEAKER, "lower left", "TO THE COUNCIL, HE IS WITH JIRAIYA. KEEP IT THAT WAY.")),
  R("tsunade", "kakashi", "env_hokage_office"), "high"),

 ("p18", dict(scene="establishing", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + ZET.format(i=2) + ENV.format(i=3)
  + ONLY(NARUTO, ZETSU)
  + "FIVE panels, uneven, near-black and hard rim lit.\n"
  "PANEL 1 (small): time/place card.\n"
  "PANEL 2 (dominant, middle): full-width eye vault: Naruto small at the lower edge, hundreds of "
  "sealed eye jars and shelves receding as object masses, never body horror.\n"
  "PANEL 3 (small): Naruto understands that Madara likely preserved his original eyes.\n"
  "PANEL 4 (small): Zetsu rises from wall-shadow, split black-and-white body and flytrap shell clear.\n"
  "PANEL 5 (wide, bottom): Naruto asks whether the original pair remains. " + L_HIDEOUT
  + CAP(1, "upper left", "A FEW DAYS LATER — NARUTO'S HIDEOUT")
  + SAY((5, NARUTO, "upper left", "HIS FIRST EYES. BEFORE THE ETERNAL PAIR."),
        (5, ZETSU, "upper right", "THEY WERE PRESERVED.")),
  R("naruto_13", "zetsu", "env_madara_eye_vault"), "high"),

 ("p19", dict(scene="transition", light="dark", cast="two", mood="tense", panels=5),
  FILL + N13.format(i=1) + MANGEKYO_EYE.format(i=2) + ZET.format(i=3) + ENV.format(i=4)
  + ONLY(NARUTO, ZETSU)
  + "FIVE panels, uneven; an abstract non-graphic procedure.\n"
  "PANEL 1 (small): Naruto states he needs the Eternal Mangekyo but will not confront Nagato.\n"
  "PANEL 2 (small): Zetsu returns with a sealed pair after an implied time jump.\n"
  "PANEL 3 (dominant, middle): Naruto lies only as a hard-rim-lit silhouette beneath a narrow "
  "overhead light; Zetsu's hand and the eye case occupy opposite edges. Hands, bandages, closed eye, "
  "no surgery detail.\n"
  "PANEL 4 (small): closed eyelid and a dark transition.\n"
  "PANEL 5 (wide, bottom): opened Eternal Mangekyo, using the canonical six-bladed eye design and no aura. " + L_HIDEOUT
  + CAP(4, "upper left", "THREE DAYS LATER")
  + SAY((1, NARUTO, "upper left", "I NEED THE ETERNAL MANGEKYO."),
        (3, NARUTO, "upper right", "IMPLANT THEM.")),
  R("naruto_13", "mangekyo_design", "zetsu", "env_madara_eye_vault"), "high"),

 ("p20", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + ZET.format(i=2) + ENV.format(i=3)
  + ONLY(NARUTO, ZETSU, "Naruto's shadow-clone copies")
  + "SIX panels, uneven. End on work, never a victory pose.\n"
  "PANEL 1 (small): Zetsu watches Naruto test the EMS in the shadowed training ground.\n"
  "PANEL 2 (small): Naruto orders a search through every nation for any living Uzumaki.\n"
  "PANEL 3 (small): Zetsu sinks into the ground, leaving a split shadow.\n"
  "PANEL 4 (small): Naruto studies his gloved hands and chooses clone-accelerated training.\n"
  "PANEL 5 (small): tight ram-seal hands.\n"
  "PANEL 6 (dominant, lower): low wide training ground: Naruto small at lower left forms the ram "
  "seal as a field of clone silhouettes fills the right and recedes into black rock, every copy at a "
  "different depth and crop; hard outlines, no glowing chakra. " + L_HIDEOUT
  + SAY((2, NARUTO, "upper left", "FIND ANY LIVING UZUMAKI."),
        (4, NARUTO, "upper right", "WHILE YOU SEARCH, I WILL SHORTEN THE DISTANCE MYSELF."))
  + SFX(6, "TAJUU KAGE BUNSHIN"),
  R("naruto_13", "zetsu", "env_hideout_training"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch04" / "raw", HERE / "v4ch04" / "ledger.json")
