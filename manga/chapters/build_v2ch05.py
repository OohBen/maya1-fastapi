"""Volume 2, Chapter 5 — "Room 301". 22 pages.

Source: fic ch4, the academy corridor through Kabuto's info cards. Two things carry it:
the Lee exchange, which is the only time Naruto draws the sword in the volume, and the
smile he gives Shikamaru, which is the only warm thing he does in the whole book. Both get
a dominant panel.

What the chapter costs him: his anonymity. Every genin in the room now knows his face.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                            # noqa: E402
from prompts import (ENV, FILL, HIN, INO, KAB, KIB, LEE, N13S, ONLY, OFF, R, SAK,  # noqa: E402
                     SAS, SAY, SFX, SHI, SHN, TITLE,
                     BLONDE, BOY, DOG, GIRL, GREEN, LAZY, MAN, PALE, SHADES, SPEC, UCH,
                     KAK, L_DAY)

PAGES = [
 ("p01", dict(scene="establishing", light="day", cast="crowd", mood="tense", panels=1),
  N13S.format(i=1) + ONLY(BOY, "a crowd of teenage foreign ninja, none of them recurring") +
  "CHAPTER OPENING SPLASH. A steep view UP a wide wooden academy staircase crowded with teenage "
  "ninja from many different villages, packed shoulder to shoulder and climbing away from the "
  "viewer. The blond boy is near the bottom of the paper and well off centre, the only one facing "
  "back down the stairs toward us, the sword clear across his back — a single still figure in a "
  "moving crowd. A heavy carved wooden newel post is the foreground mass, cropped by the lower left "
  "edge of the paper. The stairwell rises into a bright open doorway at the top right. Leave that "
  "bright area broad and quiet. "
  "Lighting: hard flat daylight from the doorway above, everything below it in warm brown shadow. "
  + TITLE("ROOM 301", "bright doorway at the top right"),
  R("naruto_13_sword"), "high"),

 ("p02", dict(scene="action", light="day", cast="small_group", mood="tense", panels=6),
  FILL + LEE.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + SAK.format(i=4) + ENV.format(i=5)
  + ONLY(GREEN, BOY, UCH, GIRL) +
  "SIX panels, uneven, columns not aligned. A wooden school corridor.\n"
  "PANEL 1 (small): the three of them walking down the corridor, from behind, at different depths.\n"
  "PANEL 2 (small): a flat green streak of motion crossing the corridor. No figure resolvable.\n"
  "PANEL 3 (dominant, middle): the boy in the green jumpsuit landed square in front of them with "
  "his back to the wall — huge in the foreground cropped by the left edge, thick black eyebrows and "
  "bowl cut unmistakable; the three of them small and stopped beyond him at three depths.\n"
  "PANEL 4 (small): the pink-haired girl's face, already dreading it.\n"
  "PANEL 5 (small): the green boy's hand giving an enormous thumbs up.\n"
  "PANEL 6 (wide, bottom): the corridor, the four of them, other genin flowing past at the edges of "
  "frame without stopping. " + L_DAY
  + SAY((3, GREEN, "upper right", "YOU MUST BE HARUNO SAKURA! I AM ROCK LEE!")),
  R("rock_lee", "naruto_13_sword", "sasuke", "sakura", "env_academy_corridor"), "high"),

 ("p03", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + LEE.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(GREEN, GIRL, UCH, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the green boy's face, earnest, faintly flushed.\n"
  "PANEL 2 (small): the pink-haired girl's face, appalled.\n"
  "PANEL 3 (small): the dark-haired boy's face — the closest thing to hope he shows all chapter.\n"
  "PANEL 4 (dominant, middle): the girl having stepped bodily backwards, one hand up, the green boy "
  "large in the foreground cropped by the bottom edge; the blond boy stands well to one side, "
  "turned away, entirely uninvolved.\n"
  "PANEL 5 (small): the dark-haired boy's face again — hope gone.\n"
  "PANEL 6 (wide, bottom): the corridor, the green boy standing straighter, undented. " + L_DAY
  + SAY((1, GREEN, "upper left", "WILL YOU GO OUT WITH ME? I WILL PROTECT YOU WITH MY LIFE!"),
        (4, GIRL, "upper right", "...NO!")),
  R("rock_lee", "sakura", "sasuke"), "medium"),

 ("p04", dict(scene="dialogue", light="day", cast="two", mood="tense", panels=6),
  FILL + LEE.format(i=1) + N13S.format(i=2) + ONLY(GREEN, BOY, GIRL, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the green boy's head turning, the eyes going hard and level.\n"
  "PANEL 2 (dominant, upper): the two of them facing each other down the length of the corridor at "
  "very different scales — the green boy near and large in the left foreground, the blond boy small "
  "and far away at the right, the whole corridor between them.\n"
  "PANEL 3 (small): the blond boy's single visible eye, mildly bored.\n"
  "PANEL 4 (small): the green boy's bandaged fists.\n"
  "PANEL 5 (small): other genin in the corridor stopping to watch, seen only as shoulders and "
  "backs of heads.\n"
  "PANEL 6 (wide, bottom): the corridor gone quiet, a clear space opening between the two of them. "
  + L_DAY
  + SAY((1, GREEN, "upper left", "YOU ARE UZUMAKI NARUTO."),
        (2, GREEN, "lower left", "GAI-SENSEI SAYS YOU ARE THE BEST TAIJUTSU USER OF ANY GENIN."),
        (6, GREEN, "upper right", "FIGHT ME. IF I AM TO BE THE BEST, I MUST BEAT THE BEST.")),
  R("rock_lee", "naruto_13_sword"), "high"),

 ("p05", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + N13S.format(i=1) + LEE.format(i=2) + SAK.format(i=3) + ONLY(BOY, GREEN, GIRL, UCH) +
  "SIX panels, uneven. This page is a JOKE and must be timed like one — beat, beat, punchline.\n"
  "PANEL 1 (small): the blond boy's mouth, flat, mid-sentence.\n"
  "PANEL 2 (small): the green boy's face — total, blank incomprehension.\n"
  "PANEL 3 (small): the same face, a fraction more confused.\n"
  "PANEL 4 (dominant, middle): the pink-haired girl sighing with one hand over her eyes, large in "
  "the foreground cropped by the right edge; the two boys small beyond her, still staring at each "
  "other.\n"
  "PANEL 5 (small): the blond boy, having not moved at all.\n"
  "PANEL 6 (wide, bottom): the corridor, the watchers closer now. " + L_DAY
  + SAY((1, BOY, "upper left", "AS MUCH AS I LOVE TO DANCE, I HAVE NO INTEREST IN A POINTLESS DANCE."),
        (2, GREEN, "upper right", "...DANCE?"),
        (4, GIRL, "upper left", "HE MEANS FIGHT. HE ALWAYS SAYS DANCE.")),
  R("naruto_13_sword", "rock_lee", "sakura"), "high"),

 ("p06", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + LEE.format(i=1) + N13S.format(i=2) + ONLY(GREEN, BOY) +
  "FIVE panels, uneven, hard diagonals.\n"
  "PANEL 1 (small): the green boy's sandal sliding back into a stance. Feet only.\n"
  "PANEL 2 (small): one hand coming up, palm open, the other tucked behind his back.\n"
  "PANEL 3 (dominant, middle): the green boy in a full open taijutsu stance, seen from a LOW angle "
  "so he fills the frame, hard radiating lines behind him.\n"
  "PANEL 4 (small): the blond boy's hand, still at his side. Not moving.\n"
  "PANEL 5 (wide, bottom): the two of them in the corridor, the space between them measured out. "
  + L_DAY
  + SAY((3, GREEN, "upper left", "I AM AFRAID I MUST INSIST.")),
  R("rock_lee", "naruto_13_sword"), "high"),

 ("p07", dict(scene="action", light="day", cast="two", mood="tense", panels=5),
  FILL + N13S.format(i=1) + LEE.format(i=2) + ONLY(BOY, GREEN) +
  "FIVE panels, uneven. He is simply GONE — the reader must not see the movement either.\n"
  "PANEL 1 (small): the blond boy standing exactly where he was.\n"
  "PANEL 2 (narrow letterbox): the SAME framing, now completely empty. Nothing but the corridor "
  "floor and hard speed lines. No figure at all.\n"
  "PANEL 3 (small): the green boy's eyes blowing wide open, cropped very tight.\n"
  "PANEL 4 (small): a hand closing on a sword hilt over a shoulder. Hand and hilt only.\n"
  "PANEL 5 (wide, bottom): the corridor from far back, the green boy alone in his stance and "
  "nobody in front of him — with a single flat black streak of motion crossing the whole panel. "
  + L_DAY
  + SFX(2, "SHUN", "It crosses the gutter into the panel below."),
  R("naruto_13_sword", "rock_lee"), "high"),

 ("p08", dict(scene="action", light="day", cast="two", mood="tense", panels=4),
  FILL + N13S.format(i=1) + LEE.format(i=2) + ONLY(BOY, GREEN) +
  "FOUR panels only — this is the page the chapter is built around, so it is given room.\n"
  "PANEL 1 (small): the green boy's face from below, frozen, eyes enormous.\n"
  "PANEL 2 (small): a plain straight blade held flat and level, an inch from the side of a neck. "
  "Blade and collar only, no faces, no contact, no injury.\n"
  "PANEL 3 (dominant, taking most of the page): the blond boy down on one knee low beneath the "
  "green boy's guard, having come in UNDER the stance, the sword up and extended in a single "
  "straight line to the green boy's collar. Seen from a low three-quarter angle. The green boy is "
  "still in his stance and has not moved at all. Hard radiating lines, flat opaque shapes, no "
  "injury detail of any kind.\n"
  "PANEL 4 (wide, bottom): the corridor from far back — the two of them locked in that shape, and "
  "every watching genin turned to stone. " + L_DAY
  + SAY((3, BOY, "upper right", "I REFUSE.")),
  R("naruto_13_sword", "rock_lee"), "high"),

 ("p09", dict(scene="emotional_closeup", light="day", cast="small_group", mood="tense", panels=6),
  FILL + SAS.format(i=1) + SAK.format(i=2) + LEE.format(i=3) + N13S.format(i=4)
  + ONLY(UCH, GIRL, GREEN, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy's fist, clenched hard enough to shake.\n"
  "PANEL 2 (small): his face — hatred, and underneath it something worse, which is knowing.\n"
  "PANEL 3 (small): the pink-haired girl's face, simply frightened.\n"
  "PANEL 4 (small): the green boy giving a single slow nod, the blade still at his collar.\n"
  "PANEL 5 (dominant, middle): the blond boy rising and sheathing the sword in one motion, seen "
  "from behind over the green boy's shoulder — the green boy huge and out of focus of the "
  "composition in the foreground, the blond boy small and already turning away.\n"
  "PANEL 6 (wide, bottom): the corridor, the blond boy walking on, his two teammates falling in "
  "behind him, the green boy left standing. " + L_DAY
  + SAY((4, BOY, "upper left", "GOOD.")),
  R("sasuke", "sakura", "rock_lee", "naruto_13_sword"), "high"),

 ("p10", dict(scene="dialogue", light="day", cast="small_group", mood="calm", panels=6),
  FILL + KAK.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + N13S.format(i=4) + ENV.format(i=5)
  + ONLY(MAN, GIRL, UCH, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a pair of doors at the end of a corridor, a numbered plate above them.\n"
  "PANEL 2 (small): a swirl of flat drawn leaves in mid-air. No figure.\n"
  "PANEL 3 (dominant, middle): the masked silver-haired man standing with his back to the doors, "
  "blocking them, orange book in hand — large in the foreground cropped by the right edge; the "
  "three genin stopped small beyond him.\n"
  "PANEL 4 (small): the pink-haired girl's face, surprised.\n"
  "PANEL 5 (small): the masked man closing the book.\n"
  "PANEL 6 (wide, bottom): the four of them in front of the doors. " + L_DAY
  + SAY((4, GIRL, "upper left", "SENSEI? WHAT ARE YOU DOING HERE?"),
        (6, MAN, "upper right", "I'M GLAD ALL THREE OF YOU CAME. IT HAD TO BE ALL THREE.")),
  R("kakashi", "sakura", "sasuke", "naruto_13_sword", "env_academy_corridor"), "medium"),

 ("p11", dict(scene="dialogue", light="day", cast="small_group", mood="somber", panels=6),
  FILL + KAK.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(MAN, GIRL, UCH, BOY) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the masked man's single visible eye, level and serious for once.\n"
  "PANEL 2 (small): the pink-haired girl's face going through relief and then shame.\n"
  "PANEL 3 (small): the dark-haired boy, not looking at her.\n"
  "PANEL 4 (dominant, middle): the girl small and alone in the centre of the panel with the three "
  "of them ranged around her at different depths, all facing slightly away — the composition "
  "isolates her.\n"
  "PANEL 5 (small): a swirl of flat drawn leaves where the masked man was standing.\n"
  "PANEL 6 (wide, bottom): the three genin left in front of the doors. " + L_DAY
  + SAY((1, MAN, "upper left", "THE EXAM ONLY TAKES TEAMS OF THREE. IF YOU HAD STAYED HOME, NEITHER OF THEM COULD ENTER."),
        (2, GIRL, "upper right", "...WHY DIDN'T YOU TELL US YESTERDAY?"),
        (4, MAN, "upper left", "BECAUSE THEN IT WOULD NOT HAVE BEEN YOUR CHOICE."),
        (5, OFF(MAN), "upper right", "SAKURA — DON'T LET YOURSELF BE A BURDEN TO THEM.")),
  R("kakashi", "sakura", "sasuke"), "high"),

 ("p12", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + N13S.format(i=1) + ENV.format(i=2)
  + ONLY(BOY, UCH, GIRL, "a large crowd of teenage foreign ninja, none of them recurring") +
  "FIVE panels, uneven. No dialogue on this page.\n"
  "PANEL 1 (small): a hand flat on a door. Hand only.\n"
  "PANEL 2 (narrow letterbox): the door opening a crack, hard black shadow spilling out.\n"
  "PANEL 3 (dominant, middle): the doorway from INSIDE the exam hall — the three of them small and "
  "silhouetted in a bright rectangle of light, and the whole packed room of seated genin turned "
  "toward them at once. Dozens of faces at many depths, several cropped by the panel edges, several "
  "turned away. Heavy flat black shapes crowd in from the panel borders.\n"
  "PANEL 4 (small): the pink-haired girl's hands, gripping each other.\n"
  "PANEL 5 (wide, bottom): the blond boy's face, completely unaffected, cropped tight. "
  "Lighting: flat institutional daylight through high windows, hard black shadow. "
  + SFX(3, "ZAWA", "Repeat it several times at different sizes across the panel."),
  R("naruto_13_sword", "env_exam_room_301"), "high"),

 ("p13", dict(scene="dialogue", light="interior", cast="crowd", mood="calm", panels=6),
  FILL + INO.format(i=1) + SAS.format(i=2) + SAK.format(i=3) + ENV.format(i=4)
  + ONLY(BLONDE, UCH, GIRL, BOY, "seated foreign genin in the background, none of them recurring") +
  "SIX panels, uneven. Comic timing, and it should feel like a relief after the last page.\n"
  "PANEL 1 (small): the platinum-blonde girl launching herself across the room.\n"
  "PANEL 2 (dominant, upper): her landed on the dark-haired boy's back with her chin on his "
  "shoulder, both large in the foreground cropped by the left edge; the pink-haired girl small "
  "beyond them going incandescent.\n"
  "PANEL 3 (small): the dark-haired boy's eye, twitching.\n"
  "PANEL 4 (small): the pink-haired girl's face, close, furious.\n"
  "PANEL 5 (small): the blond boy elsewhere in the room, arms folded, not watching any of it.\n"
  "PANEL 6 (wide, bottom): the corner of the hall, the three girls and boys tangled up, other "
  "genin at the edges of frame pointedly ignoring them. "
  "Lighting: flat institutional daylight. "
  + SAY((2, BLONDE, "upper right", "SASUKE-KUN! YOU'RE LATE!"),
        (4, GIRL, "upper left", "GET OFF HIM, INO-PIG!"),
        (6, BLONDE, "upper right", "BIG-FOREHEAD SAKURA. I THOUGHT YOU'D BE AT HOME PLAYING WITH MAKE-UP.")),
  R("ino", "sasuke", "sakura", "env_exam_room_301"), "medium"),

 ("p14", dict(scene="emotional_closeup", light="interior", cast="small_group", mood="calm", panels=6),
  FILL + SHI.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + SAK.format(i=4)
  + ONLY(LAZY, BOY, UCH, GIRL) +
  "SIX panels, uneven. This is the warmest page in the entire book and it must be played quietly.\n"
  "PANEL 1 (small): the boy with the pineapple ponytail slouching over with his hands in his "
  "pockets, half-lidded.\n"
  "PANEL 2 (small): the blond boy turning his head toward him.\n"
  "PANEL 3 (dominant, middle): the blond boy SMILING. Small, real, and completely unguarded — "
  "cropped tight on his face, flat pale tone behind him, no hard lines, no shadow. It is the only "
  "time he does this and the panel must be the largest on the page.\n"
  "PANEL 4 (small): the dark-haired boy staring at him as though at a stranger.\n"
  "PANEL 5 (small): the pink-haired girl's face doing the same.\n"
  "PANEL 6 (wide, bottom): the ponytailed boy giving a small nod back, the two of them at ease, the "
  "other two still staring. "
  "Lighting: flat institutional daylight. "
  + SAY((1, LAZY, "upper left", "YOU'RE TAKING THIS TROUBLESOME EXAM TOO? WHAT A DRAG."),
        (5, GIRL, "upper right", "SASUKE-KUN... DID NARUTO JUST SMILE?")),
  R("shikamaru", "naruto_13_sword", "sasuke", "sakura"), "high"),

 ("p15", dict(scene="dialogue", light="interior", cast="crowd", mood="calm", panels=6),
  FILL + KIB.format(i=1) + HIN.format(i=2) + SHN.format(i=3) + SAS.format(i=4) + ENV.format(i=5)
  + ONLY(DOG, PALE, SHADES, UCH, BOY, GIRL, LAZY, BLONDE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the boy with the red fang markings shoving through the crowd, the white puppy "
  "on his head.\n"
  "PANEL 2 (small): the boy in the black sunglasses behind him, saying nothing.\n"
  "PANEL 3 (small): the shy pale-eyed girl going pink and looking at the floor.\n"
  "PANEL 4 (dominant, middle): NINE Konoha genin gathered in the corner of the hall at clearly "
  "different depths, overlapping each other, three of them cropped by the panel edges and two "
  "turned away from camera. Nobody evenly spaced, nobody facing the viewer in a row.\n"
  "PANEL 5 (small): the dark-haired boy's smirk.\n"
  "PANEL 6 (wide, bottom): the same group from further back, and the whole rest of the hall "
  "watching them. "
  "Lighting: flat institutional daylight. "
  + SAY((1, DOG, "upper left", "FOUND YOU! LOOKS LIKE EVERYONE'S HERE."),
        (4, DOG, "upper right", "TOGETHER WE MAKE THE ROOKIE NINE!"),
        (5, UCH, "lower left", "YOU SEEM CONFIDENT.")),
  R("kiba", "hinata", "shino", "sasuke", "env_exam_room_301"), "medium"),

 ("p16", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + KAB.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + ENV.format(i=4)
  + ONLY(SPEC, BOY, UCH, GIRL, DOG, LAZY,
         "other Konoha genin standing in the group, and seated foreign genin behind them") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blond boy's head turning away from the group, having heard something first.\n"
  "PANEL 2 (dominant, upper): the grey-haired boy in round glasses walking up to the group with his "
  "hands loose at his sides — large in the foreground cropped by the right edge, light flaring flat "
  "white across one lens; the rookies small and clustered beyond him.\n"
  "PANEL 3 (small): the dark-haired boy bristling.\n"
  "PANEL 4 (small): the glasses in close-up, both lenses gone flat opaque white. No eyes visible.\n"
  "PANEL 5 (small): the blond boy watching him — the only one in the group who is.\n"
  "PANEL 6 (wide, bottom): the group and the newcomer, the packed hall behind. "
  "Lighting: flat institutional daylight. "
  + SAY((2, SPEC, "upper left", "YOU SHOULD ALL BE QUIET. YOU'RE THE ROOKIES, AREN'T YOU?"),
        (2, SPEC, "lower right", "YOU'RE SCREAMING LIKE SCHOOLGIRLS. THIS ISN'T A PICNIC."),
        (3, UCH, "upper right", "WHO THE HELL DO YOU THINK YOU ARE?")),
  R("kabuto", "naruto_13_sword", "sasuke", "env_exam_room_301"), "high"),

 ("p17", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + KAB.format(i=1) + N13S.format(i=2) + ONLY(SPEC, BOY, UCH, GIRL, DOG) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): a deck of blank cards fanned in one hand. Objects only.\n"
  "PANEL 2 (small): one card spun down onto the floor, still blank.\n"
  "PANEL 3 (dominant, middle): the card lying on the floorboards with an image and dense writing "
  "now burned onto its face, seen from directly above, the ring of genin's feet and knees crowded "
  "round it at the panel edges. The card is the whole composition. Any writing on it is illegible "
  "scribble, not readable words.\n"
  "PANEL 4 (small): the grey-haired boy's pleasant, pleasant smile.\n"
  "PANEL 5 (small): the blond boy's face, unreadable.\n"
  "PANEL 6 (wide, bottom): the group crouched round the cards, the hall behind them. "
  "Lighting: flat institutional daylight. "
  + SAY((1, SPEC, "upper left", "NIN-INFO CARDS. I HAVE EVERY CANDIDATE IN THIS ROOM."),
        (5, BOY, "upper right", "GIVE ME WHAT YOU HAVE ON SABAKU NO GAARA.")),
  R("kabuto", "naruto_13_sword"), "high"),

 ("p18", dict(scene="dialogue", light="interior", cast="small_group", mood="tense", panels=6),
  FILL + KAB.format(i=1) + N13S.format(i=2) + SAS.format(i=3) + KIB.format(i=4)
  + ONLY(SPEC, BOY, UCH, DOG, GIRL) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the grey-haired boy's finger on a card.\n"
  "PANEL 2 (small): the boy with the fang markings, sweating.\n"
  "PANEL 3 (small): the dark-haired boy's jaw tightening.\n"
  "PANEL 4 (dominant, middle): the ring of rookies crouched around the cards, every one of them "
  "reacting except ONE — the blond boy standing upright behind them all, arms folded, entirely "
  "unmoved. He is the smallest figure in the panel and the composition points at him.\n"
  "PANEL 5 (small): the grey-haired boy glancing up at him rather than at the cards.\n"
  "PANEL 6 (wide, bottom): the group breaking apart, the hall noise returning. "
  "Lighting: flat institutional daylight. "
  + SAY((1, SPEC, "upper left", "THREE A-RANK MISSIONS. AND HE HAS NEVER COME BACK INJURED. NOT ONCE."),
        (5, BOY, "upper right", "NOTHING I DID NOT ALREADY KNOW.")),
  R("kabuto", "naruto_13_sword", "sasuke", "kiba"), "high"),

 ("p19", dict(scene="dialogue", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + N13S.format(i=1) + KAB.format(i=2) + ENV.format(i=3)
  + ONLY(BOY, SPEC, UCH, GIRL, "the packed hall of seated foreign genin, none of them recurring") +
  "FIVE panels, uneven. He says this too loudly and the whole room hears it.\n"
  "PANEL 1 (small): the grey-haired boy mid-sentence, one finger raised, being cut off.\n"
  "PANEL 2 (dominant, middle): the blond boy standing among the seated rows, the ONLY one upright, "
  "seen from a low angle; behind and around him dozens of heads turning toward him at once, at many "
  "depths, several cropped by the panel edges. He is not shouting and that is worse.\n"
  "PANEL 3 (small): a foreign genin's face, insulted.\n"
  "PANEL 4 (small): another, angrier.\n"
  "PANEL 5 (wide, bottom): the hall, every face now pointed one way. "
  "Lighting: flat institutional daylight. "
  + SAY((1, SPEC, "upper left", "NOW, THE CANDIDATES YOU'LL WANT TO AVOID ARE—"),
        (2, BOY, "upper right", "THERE ARE NO STRONG CANDIDATES HERE."),
        (5, BOY, "upper left", "THE REST ARE WEAK. THEY ARE NOTHING BUT ANNOYANCES.")),
  R("naruto_13_sword", "kabuto", "env_exam_room_301"), "high"),

 ("p20", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=6),
  FILL + N13S.format(i=1) + ENV.format(i=2)
  + ONLY(BOY, "three foreign genin in dark clothing and grey camouflage-print scarves, none of them "
         "recurring", "the packed hall of seated genin") +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): three chairs pushed back at once. Chairs and legs only.\n"
  "PANEL 2 (small): one of the three foreign genin's faces, close, ugly with it.\n"
  "PANEL 3 (small): a bandaged hand flexing.\n"
  "PANEL 4 (dominant, middle): the three of them coming down the rows toward the blond boy, "
  "cropped hard by the panel edges and drawn from a low angle so they loom; the blond boy small at "
  "the far end of the panel, hands at his sides, not turning round.\n"
  "PANEL 5 (small): the blond boy's single visible eye. Interested, faintly.\n"
  "PANEL 6 (wide, bottom): the whole hall on its feet. "
  "Lighting: flat institutional daylight. "
  + SAY((2, "the foreign genin in the grey scarf", "upper left", "LET'S SHOW THE BLOND WHO'S WEAK.")),
  R("naruto_13_sword", "env_exam_room_301"), "high"),

 ("p21", dict(scene="action", light="interior", cast="crowd", mood="tense", panels=5),
  FILL + ENV.format(i=1)
  + ONLY("a hall packed with seated and standing teenage genin, none of them recurring") +
  "FIVE panels, uneven. NOBODY named appears on this page — it is the room reacting to a pressure.\n"
  "PANEL 1 (small): a great billow of flat white smoke at the front of the hall.\n"
  "PANEL 2 (small): every window in the room rattling in its frame. No people.\n"
  "PANEL 3 (dominant, middle): the whole hall seen from the front — rows and rows of teenage genin "
  "flattened back into their seats by something out of frame, heads down, hands gripping desks, at "
  "many depths, several cropped by the edges. Heavy flat black shapes press in from the top of the "
  "panel.\n"
  "PANEL 4 (small): one pair of hands, white-knuckled on a desk edge.\n"
  "PANEL 5 (wide, bottom): the hall gone absolutely silent and still. "
  "Lighting: flat institutional daylight, heavy black shadow. "
  + SFX(3, "GOOO"),
  R("env_exam_room_301"), "medium"),

 ("p22", dict(scene="emotional_closeup", light="interior", cast="crowd", mood="tense", panels=4),
  FILL + N13S.format(i=1) + ENV.format(i=2)
  + ONLY(BOY, "the hall of seated genin behind him, none of them recurring") +
  "FOUR panels only. The chapter ends on him.\n"
  "PANEL 1 (small): rows of bowed heads, seen from behind.\n"
  "PANEL 2 (small): three foreign genin sitting back down without ever having reached him.\n"
  "PANEL 3 (narrow letterbox): the blond boy's single visible eye, cropped by all four edges, "
  "entirely unbothered by whatever has just flattened the room.\n"
  "PANEL 4 (dominant, bottom): the hall from behind him — his shoulders and the sword hilt enormous "
  "in the foreground cropped by the bottom edge, and beyond them a hundred genin sitting rigid in "
  "their rows, all facing the front, none of them facing him. No dialogue anywhere on this page. "
  "Lighting: flat institutional daylight, hard black shadow. ",
  R("naruto_13_sword", "env_exam_room_301"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v2ch05" / "raw", HERE / "v2ch05" / "ledger.json")
