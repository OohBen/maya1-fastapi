"""Volume 2, Chapter 6 — "The Tenth Question". 20 pages.

Source: fic ch4, Ibiki's written exam. The joke of the chapter is that it costs Naruto
nothing: the test is designed to break people who cannot gather information or hold their
nerve, and he has Zetsu and no nerves. Everyone else is being taken apart on the same pages
where he is simply bored.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                        # noqa: E402
from prompts import (ENV, FILL, HIN, IBI, KAB, KIB, N13S, ONLY, OFF, R, SAK,   # noqa: E402
                     SAS, SAY, SFX, TEM, TITLE,
                     BOY, DOG, FAN, GIRL, PALE, SCAR, SPEC, UCH)

HALL = "flat institutional daylight through high windows, hard black shadow. "
CROWD = "the packed hall of seated teenage genin, none of them recurring"

PAGES = [
 ("p01", dict(scene="establishing", light="interior", cast="solo", mood="tense", panels=1),
  IBI.format(i=1) + ONLY(SCAR) +
  "CHAPTER OPENING SPLASH. A huge scarred man in a black head-wrap and a heavy black trench coat "
  "stands at the front of an examination hall, seen from a LOW angle from between the desks so he "
  "towers over the paper, his coat filling most of the frame in flat black. The corner of a wooden "
  "desk and the back of an empty chair are the foreground mass, cropped by the lower left edge. "
  "Behind him a blackboard runs off the right side of the paper, and high windows spill hard white "
  "light down past him. He is looking directly at the viewer. Leave the pale blackboard area at the "
  "upper right broad and quiet. "
  "Lighting: hard white window light from behind, so he is nearly a silhouette with only the scars "
  "and one eye catching the light. " + TITLE("THE TENTH QUESTION", "pale blackboard at the upper right"),
  R("ibiki"), "high"),

 ("p02", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + IBI.format(i=1) + ENV.format(i=2) + ONLY(SCAR, CROWD) +
  "FIVE panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): a great billow of flat white smoke at the front of the hall. No figure.\n"
  "PANEL 2 (small): a black boot landing on the instructor's platform. Boot only.\n"
  "PANEL 3 (dominant, middle): the scarred man standing in the clearing smoke, huge in the "
  "foreground cropped by the right edge, and beyond him the whole hall of genin flattened back into "
  "their chairs at many depths, several cropped by the panel edges, several turned away.\n"
  "PANEL 4 (small): one genin's face, sweating, cropped very tight.\n"
  "PANEL 5 (wide, bottom): the hall in absolute silence, every chair straightened. " + HALL
  + SAY((3, SCAR, "upper left", "I WILL NOT ACCEPT THAT KIND OF BEHAVIOUR IN HERE. UNDERSTOOD?"))
  + SFX(1, "BOFU"),
  R("ibiki", "env_exam_room_301"), "high"),

 ("p03", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + IBI.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(SCAR, BOY, UCH, GIRL, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the scarred man's face, cropped tight, the two long diagonal scars leading the "
  "composition.\n"
  "PANEL 2 (small): rows of genin scrambling into seats, seen from behind as backs and shoulders.\n"
  "PANEL 3 (small): a numbered card on a desk. Object only, the number illegible.\n"
  "PANEL 4 (dominant, middle): the hall from the BACK of the room, every head facing away toward "
  "the tiny figure of the scarred man at the front — a deep one-point perspective down the rows of "
  "desks, several heads cropped huge by the bottom edge.\n"
  "PANEL 5 (small): the blond boy taking a seat, alone in his row.\n"
  "PANEL 6 (wide, bottom): chunin instructors moving down the aisles dropping papers face-down on "
  "each desk, seen only as legs, hands and paper. " + HALL
  + SAY((1, SCAR, "upper left", "I AM MORINO IBIKI. PROCTOR OF THE FIRST TEST."),
        (4, SCAR, "upper right", "ALL RIGHT, YOU MAGGOTS. TAKE YOUR SEATS.")),
  R("ibiki", "naruto_13_sword", "env_exam_room_301"), "high"),

 ("p04", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + IBI.format(i=1) + SAK.format(i=2) + ENV.format(i=3) + ONLY(SCAR, GIRL, BOY, UCH, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a hand rapping a knuckle on a blackboard. Hand and board only.\n"
  "PANEL 2 (dominant, upper): the scarred man in front of the blackboard, arm still raised, seen "
  "from low between two rows of heads cropped huge and dark in the foreground. The blackboard "
  "behind him carries lines of chalk writing that are ILLEGIBLE SCRIBBLE, not readable words.\n"
  "PANEL 3 (small): the pink-haired girl's face, reading, calculating.\n"
  "PANEL 4 (small): a hand flattening a face-down exam paper against a desk.\n"
  "PANEL 5 (small): the scarred man's eyes.\n"
  "PANEL 6 (wide, bottom): the hall, every face front. " + HALL
  + SAY((2, SCAR, "upper left", "TEN POINTS EACH. ONE COMES OFF FOR EVERY WRONG ANSWER."),
        (2, SCAR, "lower right", "YOUR TEAM'S SCORES ARE ADDED TOGETHER."),
        (6, SCAR, "upper left", "GET CAUGHT CHEATING AND YOU LOSE TWO. FIVE TIMES AND YOU ARE OUT — ALL THREE OF YOU.")),
  R("ibiki", "sakura", "env_exam_room_301"), "high"),

 ("p05", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + IBI.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(SCAR, BOY, CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): a clock face on the wall. Object only, the numerals illegible.\n"
  "PANEL 2 (small): rows of hands poised flat on face-down papers.\n"
  "PANEL 3 (dominant, middle): the scarred man from a very low angle with one arm thrown out, the "
  "whole hall of raised paper behind and below him — the most kinetic panel on the page. Hard "
  "radiating lines.\n"
  "PANEL 4 (small): a hundred papers turning over at once, drawn as flat overlapping white shapes.\n"
  "PANEL 5 (wide, bottom): heads going down across the whole hall in a wave. " + HALL
  + SAY((3, SCAR, "upper right", "YOU WILL ANSWER QUESTIONS ONE TO NINE. THE TENTH COMES LATER."),
        (3, SCAR, "lower left", "FORTY-FIVE MINUTES. BEGIN!"))
  + SFX(4, "BASA"),
  R("ibiki", "naruto_13_sword", "env_exam_room_301"), "high"),

 ("p06", dict(scene="dialogue", light="interior", cast="solo", mood="calm", panels=6),
  FILL + N13S.format(i=1) + ONLY(BOY, CROWD) +
  "SIX panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (dominant, top): the exam paper flat on the desk seen from directly above, dense with "
  "diagrams and lines of writing that are ILLEGIBLE SCRIBBLE, and the boy's hands resting either "
  "side of it, not holding a pencil.\n"
  "PANEL 2 (small): one blond eyebrow going up a fraction.\n"
  "PANEL 3 (small): his eyes moving right, not down.\n"
  "PANEL 4 (small): a pencil still lying untouched on the desk. Object only.\n"
  "PANEL 5 (small): his single visible eye, cropped tight, thinking.\n"
  "PANEL 6 (wide, bottom): the boy alone in his row from a high angle, everyone around him already "
  "bent over their papers. " + HALL,
  R("naruto_13_sword"), "high"),

 ("p07", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=8),
  FILL + SAS.format(i=1) + HIN.format(i=2) + ENV.format(i=3) + ONLY(UCH, PALE, BOY, CROWD) +
  "EIGHT panels — deliberately fast FRAGMENTS of the whole room cheating at once. Uneven sizes, "
  "columns not aligned. No dialogue anywhere on this page.\n"
  "PANEL 1 (small): the dark-haired boy's eyes, now red with two black comma marks, flicking "
  "sideways.\n"
  "PANEL 2 (small): the shy girl's pale eyes, veins standing out hard at her temples.\n"
  "PANEL 3 (small): a small round mirror angled on a ceiling beam. Object only.\n"
  "PANEL 4 (small): an insect crawling across a written page. No face.\n"
  "PANEL 5 (small): a hand under a desk, fingers signing.\n"
  "PANEL 6 (small): a thin thread of light between two desks.\n"
  "PANEL 7 (small): the blond boy, chin on his hand, watching ALL of it rather than his own paper.\n"
  "PANEL 8 (wide, bottom): the hall from above, every head down, and one head up. " + HALL,
  R("sasuke", "hinata", "env_exam_room_301"), "high"),

 ("p08", dict(scene="dialogue", light="interior", cast="two", mood="calm", panels=6),
  FILL + HIN.format(i=1) + N13S.format(i=2) + ONLY(PALE, BOY, CROWD) +
  "SIX panels, uneven. No dialogue on this page — it is entirely faces.\n"
  "PANEL 1 (small): the shy girl looking sideways down the row.\n"
  "PANEL 2 (small): what she sees — the blond boy's blank paper.\n"
  "PANEL 3 (small): her hand nudging her own paper an inch toward him.\n"
  "PANEL 4 (small): her face going pink, eyes down.\n"
  "PANEL 5 (dominant, middle): the blond boy from behind and above, the untouched paper in front of "
  "him, the girl small and several desks away — the empty desks between them dominating the panel.\n"
  "PANEL 6 (wide, bottom): the boy finally picking up the pencil. " + HALL,
  R("hinata", "naruto_13_sword"), "medium"),

 ("p09", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=7),
  FILL + IBI.format(i=1) + ENV.format(i=2) + ONLY(SCAR, CROWD) +
  "SEVEN panels — fast, ugly, procedural. Uneven, columns not aligned.\n"
  "PANEL 1 (small): a chunin instructor's finger pointing down a row. Hand only.\n"
  "PANEL 2 (small): a genin's face, caught, mouth open.\n"
  "PANEL 3 (small): a chair going over backwards. No figure.\n"
  "PANEL 4 (small): two more genin standing up without being told to.\n"
  "PANEL 5 (dominant, middle): three genin being walked out of the hall through a door at the back, "
  "seen from the front of the room over the scarred man's shoulder — his shoulder and head cropped "
  "enormous and black in the foreground, the three tiny at the far door.\n"
  "PANEL 6 (small): the hall's remaining faces, none of them looking up.\n"
  "PANEL 7 (wide, bottom): three empty desks in a row. " + HALL
  + SAY((2, "the chunin instructor pointing", "upper left", "NUMBER FIFTY-ONE. OUT."),
        (5, SCAR, "upper right", "AND HIS TEAM WITH HIM.")),
  R("ibiki", "env_exam_room_301"), "medium"),

 ("p10", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + N13S.format(i=1) + SAK.format(i=2) + KIB.format(i=3) + ENV.format(i=4)
  + ONLY(BOY, GIRL, DOG, UCH, CROWD) +
  "SIX panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): the clock again, the hand further round. Object only.\n"
  "PANEL 2 (small): the pink-haired girl writing steadily, the only calm thing about her.\n"
  "PANEL 3 (small): the boy with the fang markings sweating onto his paper.\n"
  "PANEL 4 (small): a white puppy's nose appearing over the edge of a desk.\n"
  "PANEL 5 (dominant, middle): the blond boy writing FAST, hand blurred with hard motion lines, "
  "seen from a low angle across the desk with the paper enormous in the foreground — and his face "
  "showing nothing at all.\n"
  "PANEL 6 (wide, bottom): his completed paper, dense with illegible writing, pushed to the corner "
  "of the desk. " + HALL,
  R("naruto_13_sword", "sakura", "kiba", "env_exam_room_301"), "medium"),

 ("p11", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + IBI.format(i=1) + ENV.format(i=2) + ONLY(SCAR, CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the clock hand arriving. Object only.\n"
  "PANEL 2 (small): pencils going down across a row.\n"
  "PANEL 3 (dominant, middle): the scarred man stepping down off the platform and walking up the "
  "central aisle toward camera, cropped by the bottom edge, the hall of seated genin falling away "
  "behind him on both sides at many depths.\n"
  "PANEL 4 (small): his hands, flexing once.\n"
  "PANEL 5 (wide, bottom): the whole hall, waiting. " + HALL
  + SAY((3, SCAR, "upper left", "PENCILS DOWN."),
        (5, SCAR, "upper right", "NOW. THE TENTH QUESTION.")),
  R("ibiki", "env_exam_room_301"), "high"),

 ("p12", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + IBI.format(i=1) + TEM.format(i=2) + ENV.format(i=3) + ONLY(SCAR, FAN, BOY, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blonde girl with four pigtails standing up in her row.\n"
  "PANEL 2 (small): heads turning toward her.\n"
  "PANEL 3 (dominant, middle): the scarred man and the blonde girl at opposite ends of a deep "
  "perspective down the aisle — she is small and standing in the middle distance, he is enormous in "
  "the foreground cropped by the left edge, and the seated rows between them fill the panel.\n"
  "PANEL 4 (small): his mouth, beginning to enjoy this.\n"
  "PANEL 5 (small): her face, the confidence going out of it.\n"
  "PANEL 6 (wide, bottom): the hall, absolutely still. " + HALL
  + SAY((1, FAN, "upper left", "WAIT — WHAT HAPPENS IF WE CHOOSE NOT TO TAKE IT?"),
        (3, SCAR, "upper right", "YOUR SCORE DROPS TO ZERO. YOU FAIL."),
        (6, SCAR, "upper left", "AND SO DO BOTH OF YOUR TEAMMATES.")),
  R("ibiki", "temari", "env_exam_room_301"), "high"),

 ("p13", dict(scene="emotional_closeup", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + IBI.format(i=1) + ENV.format(i=2) + ONLY(SCAR, CROWD) +
  "SIX panels, uneven. This is the page where he breaks them, and it is done with one sentence.\n"
  "PANEL 1 (dominant, top): the scarred man's face filling the panel, cropped so tight that the "
  "head-wrap and the two long scars are the whole composition. Hard parallel hatch lines. Largest "
  "panel on the page.\n"
  "PANEL 2 (small): a genin's hands, gripping the desk edge white.\n"
  "PANEL 3 (small): another genin's face, breaking.\n"
  "PANEL 4 (small): a third, staring at nothing.\n"
  "PANEL 5 (small): a chair pushed back an inch. No figure.\n"
  "PANEL 6 (wide, bottom): the hall from above, motionless. " + HALL
  + SAY((1, SCAR, "upper left", "IF YOU TAKE THE QUESTION AND GET IT WRONG —"),
        (6, SCAR, "upper right", "YOU WILL NEVER BE PERMITTED TO SIT THIS EXAM AGAIN. NOT EVER.")),
  R("ibiki", "env_exam_room_301"), "high"),

 ("p14", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + KIB.format(i=1) + KAB.format(i=2) + IBI.format(i=3) + ENV.format(i=4)
  + ONLY(DOG, SPEC, SCAR, BOY, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the boy with the fang markings on his feet, shouting.\n"
  "PANEL 2 (small): his hand thrown out, pointing across the hall.\n"
  "PANEL 3 (dominant, middle): what he is pointing at — the grey-haired boy in round glasses seated "
  "calmly several rows away, light flaring flat white across one lens, seen down a deep perspective "
  "with heads cropped huge in the foreground.\n"
  "PANEL 4 (small): the grey-haired boy's pleasant smile, unbothered.\n"
  "PANEL 5 (small): the scarred man's answering smirk.\n"
  "PANEL 6 (wide, bottom): the hall, more people looking at each other now than at the front. "
  + HALL
  + SAY((1, DOG, "upper left", "THAT'S A STUPID RULE! THERE ARE PEOPLE HERE WHO'VE TAKEN IT FOUR TIMES!"),
        (5, SCAR, "upper right", "THEN THEY WERE LUCKY. THIS YEAR THE RULE IS MINE.")),
  R("kiba", "kabuto", "ibiki", "env_exam_room_301"), "high"),

 ("p15", dict(scene="action", light="interior", cast="crowd", mood="somber", panels=7),
  FILL + ENV.format(i=1) + ONLY(CROWD) +
  "SEVEN panels — the room emptying, one team at a time. Uneven, columns not aligned. Nobody named "
  "appears on this page and there is no dialogue.\n"
  "PANEL 1 (small): one hand going up. Hand only.\n"
  "PANEL 2 (small): a chair scraping back.\n"
  "PANEL 3 (small): two more hands going up elsewhere in the room.\n"
  "PANEL 4 (small): a boy's face as he stands, ashamed.\n"
  "PANEL 5 (dominant, middle): a whole column of genin filing out of the door at the back of the "
  "hall in a long line, seen from the front of the room, the empty desks they leave behind opening "
  "up in the foreground.\n"
  "PANEL 6 (small): three empty chairs.\n"
  "PANEL 7 (wide, bottom): the hall, visibly half the size it was. " + HALL,
  R("env_exam_room_301"), "medium"),

 ("p16", dict(scene="emotional_closeup", light="interior", cast="solo", mood="calm", panels=5),
  FILL + N13S.format(i=1) + ENV.format(i=2) + ONLY(BOY, CROWD) +
  "FIVE panels, uneven. No dialogue. The joke of the whole chapter lands here: it has cost him "
  "nothing.\n"
  "PANEL 1 (small): his hand, flat and relaxed on the desk.\n"
  "PANEL 2 (small): the sword's wrapped hilt leaning against the chair beside him.\n"
  "PANEL 3 (narrow letterbox): his single visible eye, cropped by all four edges. He is bored.\n"
  "PANEL 4 (small): the empty desks either side of him, chairs pushed out.\n"
  "PANEL 5 (dominant, bottom): the blond boy seated alone in a widening island of empty desks, seen "
  "from high above, small at the bottom of the panel — the emptiness is the composition. " + HALL,
  R("naruto_13_sword", "env_exam_room_301"), "high"),

 ("p17", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + IBI.format(i=1) + SAK.format(i=2) + ENV.format(i=3) + ONLY(SCAR, GIRL, BOY, UCH, CROWD) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the pink-haired girl's hand, half-lifted, trembling.\n"
  "PANEL 2 (small): her face, deciding.\n"
  "PANEL 3 (small): her hand coming back down flat on the desk.\n"
  "PANEL 4 (dominant, middle): the scarred man surveying what is left of the hall from the "
  "platform, small and central, the thinned rows of desks stretching away on both sides in a deep "
  "perspective, several empty chairs cropped huge in the foreground.\n"
  "PANEL 5 (wide, bottom): the remaining genin, all of them looking at him. " + HALL
  + SAY((4, SCAR, "upper left", "ANYONE ELSE?"),
        (5, SCAR, "upper right", "...NO. THEN I WILL GIVE YOU THE TENTH QUESTION.")),
  R("ibiki", "sakura", "env_exam_room_301"), "high"),

 ("p18", dict(scene="emotional_closeup", light="interior", cast="crowd", mood="tense", panels=4),
  FILL + IBI.format(i=1) + ENV.format(i=2) + ONLY(SCAR, CROWD) +
  "FOUR panels only. Hold the moment before the punchline.\n"
  "PANEL 1 (small): the scarred man's mouth, closed, giving nothing.\n"
  "PANEL 2 (small): a row of held breaths — three genin faces at three depths, none of them "
  "blinking.\n"
  "PANEL 3 (dominant, taking most of the page): the scarred man alone at the front of the hall, "
  "seen from the very back of the room down the full length of the deep perspective, tiny, with the "
  "emptied desks and the backs of the remaining heads filling everything between. Silence drawn as "
  "space.\n"
  "PANEL 4 (wide, bottom): his face, and the first crack of a grin in it. " + HALL
  + SAY((4, SCAR, "upper right", "ALL OF YOU WHO ARE STILL SITTING THERE —")),
  R("ibiki", "env_exam_room_301"), "high"),

 ("p19", dict(scene="dialogue", light="interior", cast="crowd", mood="calm", panels=6),
  FILL + IBI.format(i=1) + TEM.format(i=2) + SAK.format(i=3) + ENV.format(i=4)
  + ONLY(SCAR, FAN, GIRL, BOY, CROWD) +
  "SIX panels, uneven.\n"
  "PANEL 1 (dominant, top): the scarred man with both arms spread, the hall staring up at him from "
  "below, several heads cropped huge and dark along the bottom edge.\n"
  "PANEL 2 (small): the pink-haired girl's face — total incomprehension.\n"
  "PANEL 3 (small): the blonde girl with four pigtails, on her feet again, furious.\n"
  "PANEL 4 (small): the scarred man's grin, wider.\n"
  "PANEL 5 (small): the blond boy, unmoved, chin still on his hand.\n"
  "PANEL 6 (wide, bottom): the hall erupting — everyone talking at once, drawn as overlapping "
  "figures at many depths. " + HALL
  + SAY((1, SCAR, "upper left", "YOU PASS."),
        (3, FAN, "upper right", "WHAT?! WHAT ABOUT THE TENTH QUESTION?")),
  R("ibiki", "temari", "sakura", "env_exam_room_301"), "high"),

 ("p20", dict(scene="emotional_closeup", light="interior", cast="crowd", mood="calm", panels=4),
  FILL + IBI.format(i=1) + N13S.format(i=2) + ENV.format(i=3) + ONLY(SCAR, BOY, CROWD) +
  "FOUR panels only. The chapter's last line gets the biggest panel in it.\n"
  "PANEL 1 (small): a hundred faces turned to the front at once, drawn small and overlapping.\n"
  "PANEL 2 (small): the blond boy's face — the only one already unsurprised.\n"
  "PANEL 3 (dominant, taking most of the page): the scarred man in close-up from a low angle, "
  "cropped tight, the head-wrap and both scars filling the frame, grinning outright for the first "
  "time. Hard radiating lines behind him, flat black shadow.\n"
  "PANEL 4 (wide, bottom): the hall from behind him, every genin on their feet. " + HALL
  + SAY((3, SCAR, "upper left", "THERE IS NO TENTH QUESTION.")),
  R("ibiki", "naruto_13_sword", "env_exam_room_301"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v2ch06" / "raw", HERE / "v2ch06" / "ledger.json")
