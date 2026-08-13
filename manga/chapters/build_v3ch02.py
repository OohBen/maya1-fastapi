"""Volume 3, Chapter 2 — "A Gift". 20 pages.

Source: fic ch5, the cursed seal. Orochimaru's half of this is quick and the fic moves on; the
half that matters is the four pages afterwards where Naruto looks at his own hands. That is the
first involuntary thing he has done in three volumes and it gets the dominant panel.

Continuity: he loses the ninjato here and does not have it again until it is replaced. From
Chapter 3 he is bound with N13, not N13S.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run                                                       # noqa: E402
from prompts import (FILL, N13S, ONLY, OFF, ORO, R, SAK, SAS, SAY, SFX, TITLE,  # noqa: E402
                     BOY, GIRL, PALEONE, UCH)

FOR = "Lighting: sunless green-black gloom under a dense canopy, hard shafts of pale light. "
MARK = ("The mark on the dark-haired boy's neck is THREE SMALL BLACK COMMA SHAPES arranged in a "
        "circle, like a tiny tattoo. It is a flat black graphic mark on unbroken skin — never a "
        "wound, never broken skin, no red, no injury detail of any kind. ")

PAGES = [
 ("p01", dict(scene="establishing", light="dark", cast="two", mood="tense", panels=1),
  SAS.format(i=1) + ONLY(UCH, PALEONE) +
  "CHAPTER OPENING SPLASH. The dark-haired boy sits slumped at the foot of a colossal tree in the "
  "lower right of the paper, small, one arm hanging, head tipped back against the bark. Thrown "
  "across the trunk above and behind him, enormous, is the SHADOW of a tall slender figure with "
  "very long hair — cast flat and black on the bark, far larger than he is, reaching most of the "
  "way up the paper. The figure casting it is not in frame. A great root fills the lower left as "
  "the foreground mass, cropped by the edge of the paper. Leave the pale shaft of canopy light at "
  "the upper left broad and quiet. "
  "Lighting: green-black gloom, one hard shaft of light throwing the shadow. "
  + TITLE("A GIFT", "pale shaft of light at the upper left"),
  R("sasuke", "env_forest_of_death"), "high"),

 ("p02", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + ORO.format(i=2) + ONLY(UCH, PALEONE) +
  "SIX panels, uneven, columns not aligned.\n"
  "PANEL 1 (small): chalk-white feet taking one unhurried step through leaf litter. Feet only.\n"
  "PANEL 2 (small): the dark-haired boy's back pressed hard against bark, both hands flat on it.\n"
  "PANEL 3 (small): his legs, refusing to move.\n"
  "PANEL 4 (dominant, middle): a long avenue of trunks with the pale one small and central walking "
  "toward camera, and the dark-haired boy cropped enormous and dark in the foreground, only his "
  "shoulder and the back of his head visible. The distance between them is the panel.\n"
  "PANEL 5 (small): his face, cropped tight — terror, undisguised.\n"
  "PANEL 6 (wide, bottom): the two of them at the base of the tree. " + FOR
  + SAY((5, UCH, "upper left", "S-STAY BACK. DON'T COME ANY CLOSER."),
        (6, PALEONE, "upper right", "DO YOU WANT POWER, SASUKE-KUN?")),
  R("sasuke", "orochimaru"), "high"),

 ("p03", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAS.format(i=1) + ORO.format(i=2) + ONLY(UCH, PALEONE) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the dark-haired boy's face — the fear interrupted by confusion.\n"
  "PANEL 2 (small): the pale one crouching down to his eye level, hands on knees.\n"
  "PANEL 3 (dominant, middle): the two of them face to face at the foot of the trunk, the pale one "
  "large in the left foreground cropped by the edge, the boy small and cornered against the bark, "
  "the canopy black above them both.\n"
  "PANEL 4 (small): the boy's eyes, changing — the fear going out and something far worse coming "
  "in.\n"
  "PANEL 5 (small): his hands, closing into fists on the ground.\n"
  "PANEL 6 (wide, bottom): the pale one's smile, wide and patient. " + FOR
  + SAY((3, PALEONE, "upper right", "I KNOW YOU WANT POWER TO KILL ITACHI."),
        (4, OFF(PALEONE), "upper left", "I CAN GIVE YOU THAT POWER.")),
  R("sasuke", "orochimaru"), "high"),

 ("p04", dict(scene="action", light="dark", cast="two", mood="tense", panels=4),
  FILL + ORO.format(i=1) + SAS.format(i=2) + ONLY(PALEONE, UCH) +
  "FOUR panels only. Nothing on this page may be gory — it is a horror image made of SHAPE.\n"
  "PANEL 1 (small): the pale one's mouth opening far wider than a jaw allows, two long thin fangs "
  "showing.\n"
  "PANEL 2 (dominant, taking most of the page): the neck EXTENDING — the head carried away from "
  "the body on a long smooth snaking column of neck that loops right across the panel and down "
  "toward the seated boy, drawn as one clean flowing hard-outlined shape against the trunks. The "
  "boy is small at the bottom edge, frozen. Hard radiating lines behind. No injury, no red, no "
  "contact yet.\n"
  "PANEL 3 (small): the boy's eyes, enormous, seeing it come.\n"
  "PANEL 4 (narrow letterbox, bottom): pure flat black across the whole panel, with only two thin "
  "white speed lines crossing it. Nothing else is shown. " + FOR
  + SFX(2, "SHURURU"),
  R("orochimaru", "sasuke"), "high"),

 ("p05", dict(scene="emotional_closeup", light="dark", cast="two", mood="tense", panels=5),
  FILL + SAS.format(i=1) + ORO.format(i=2) + ONLY(UCH, PALEONE) + MARK +
  "FIVE panels, uneven.\n"
  "PANEL 1 (dominant, top): the dark-haired boy's head thrown back, mouth open, screaming — cropped "
  "very tight on the face from a low angle, hard radiating lines filling everything behind him, "
  "flat black shadow. No injury detail anywhere.\n"
  "PANEL 2 (small): the three small black comma marks appearing on the skin of his neck.\n"
  "PANEL 3 (small): the pale one's head withdrawing along the extended neck, unhurried.\n"
  "PANEL 4 (small): the boy's hand losing its grip on the ground.\n"
  "PANEL 5 (wide, bottom): the boy folded over sideways in the leaf litter, and the pale one "
  "standing over him, straightening his collar. " + FOR
  + SFX(1, "AAAAA"),
  R("sasuke", "orochimaru"), "high"),

 ("p06", dict(scene="action", light="dark", cast="two", mood="tense", panels=6),
  FILL + SAK.format(i=1) + ORO.format(i=2) + SAS.format(i=3) + ONLY(GIRL, PALEONE, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pink-haired girl breaking cover at a dead run.\n"
  "PANEL 2 (small): her face — not brave, just past caring.\n"
  "PANEL 3 (dominant, middle): the girl skidding to her knees beside the fallen boy with the pale "
  "one standing directly over both of them, seen from a low angle so he fills the upper half of the "
  "panel and they are small and low. She is looking UP at him.\n"
  "PANEL 4 (small): the pale one's face, amused by her.\n"
  "PANEL 5 (small): her hands on the fallen boy's shoulder.\n"
  "PANEL 6 (wide, bottom): the three of them at the foot of the tree. " + FOR
  + SAY((1, GIRL, "upper left", "SASUKE-KUN!"),
        (3, GIRL, "upper right", "WHAT DID YOU DO TO HIM?")),
  R("sakura", "orochimaru", "sasuke"), "high"),

 ("p07", dict(scene="dialogue", light="dark", cast="two", mood="tense", panels=6),
  FILL + ORO.format(i=1) + SAK.format(i=2) + N13S.format(i=3) + ONLY(PALEONE, GIRL, BOY, UCH) +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the pale one's mouth, mid-sentence, entirely pleasant.\n"
  "PANEL 2 (small): the girl's face, not understanding the answer.\n"
  "PANEL 3 (dominant, middle): the pale one already SINKING INTO THE GROUND — the earth closing "
  "over him from the feet up as though it were water, drawn with hard-edged ripple shapes, so only "
  "his upper body and head remain above the leaf litter. He is large in the frame and looking "
  "sideways out of it.\n"
  "PANEL 4 (small): what he is looking at — the blond boy lying face-down in a crater far across "
  "the clearing, small, not moving.\n"
  "PANEL 5 (small): the top of a black-haired head disappearing under the ground.\n"
  "PANEL 6 (wide, bottom): flat empty leaf litter where he was. Nothing there at all. " + FOR
  + SAY((1, PALEONE, "upper left", "I GAVE HIM A GIFT."),
        (3, PALEONE, "upper right", "IT WILL HELP HIM AVENGE HIS CLAN.")),
  R("orochimaru", "sakura", "naruto_13_sword"), "high"),

 ("p08", dict(scene="establishing", light="dark", cast="none", mood="somber", panels=5),
  FILL +
  "FIVE panels, uneven. NO PEOPLE ANYWHERE on this page and no dialogue — the forest after.\n"
  "PANEL 1 (small): the burnt husk of a shed skin lying in the leaf litter, papery and empty. "
  "Object only, no injury detail.\n"
  "PANEL 2 (small): a scorch mark climbing a trunk.\n"
  "PANEL 3 (small): a straw hat, half burnt. Object only.\n"
  "PANEL 4 (dominant, middle): the whole clearing seen from high in the canopy, the crater and the "
  "broken trunks small at the bottom, everything else vast and dark and indifferent.\n"
  "PANEL 5 (wide, bottom): a plain straight sword lying in the dirt, half buried, its black "
  "scabbard broken. Object only. " + FOR,
  R("env_forest_of_death"), "medium"),

 ("p09", dict(scene="emotional_closeup", light="dark", cast="solo", mood="somber", panels=4),
  FILL + N13S.format(i=1) + ONLY(BOY) +
  "FOUR panels only. This is the page the chapter exists for. No dialogue anywhere on it.\n"
  "PANEL 1 (small): the blond boy's shoulder, pushing up out of the dirt.\n"
  "PANEL 2 (small): him sitting back on his heels in the crater, head down, hair hanging over his "
  "whole face.\n"
  "PANEL 3 (dominant, taking most of the page): BOTH HIS HANDS held up in front of his face, palms "
  "toward him, filling the panel — dirty, shaking very slightly, and the only thing he is looking "
  "at. His face is behind and between them, out of focus of the composition, and what is on it is "
  "not blankness. Cropped tight, flat tone behind, hard parallel hatching.\n"
  "PANEL 4 (wide, bottom): the boy alone in the crater from far above, very small. " + FOR,
  R("naruto_13_sword"), "high"),

 ("p10", dict(scene="emotional_closeup", light="dark", cast="solo", mood="somber", panels=6),
  FILL + N13S.format(i=1) + ONLY(BOY) +
  "SIX panels, uneven. No dialogue.\n"
  "PANEL 1 (small): his hands closing slowly into fists.\n"
  "PANEL 2 (narrow letterbox): his single visible eye, cropped by all four edges. It is not calm.\n"
  "PANEL 3 (small): his hand reaching back over his left shoulder — and finding nothing there.\n"
  "PANEL 4 (small): the empty diagonal strap across his back where the scabbard should be.\n"
  "PANEL 5 (dominant, middle): the boy standing up in the crater, small and central, with the "
  "enormous empty forest around him and the broken sword lying far off at the edge of the panel, "
  "too far to be worth crossing to.\n"
  "PANEL 6 (wide, bottom): him walking away from it without picking it up. " + FOR,
  R("naruto_13_sword"), "medium"),

 ("p11", dict(scene="dialogue", light="dark", cast="small_group", mood="somber", panels=6),
  FILL + N13S.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(BOY, GIRL, UCH) + MARK +
  "SIX panels, uneven.\n"
  "PANEL 1 (small): the blond boy's sandals arriving beside a kneeling girl. Feet only.\n"
  "PANEL 2 (small): the girl looking up at him, startled by the state of him.\n"
  "PANEL 3 (dominant, middle): the boy crouched over the unconscious dark-haired boy with two "
  "fingers turning his head aside to look at the neck, all three at three clearly different depths, "
  "the girl cropped by the panel edge in the foreground.\n"
  "PANEL 4 (small): the three small black comma marks on the skin, in close-up. A flat graphic "
  "mark on unbroken skin, no wound, no red.\n"
  "PANEL 5 (small): the blond boy's eye, recognising it.\n"
  "PANEL 6 (wide, bottom): the three of them in the clearing, the light going. " + FOR
  + SAY((2, GIRL, "upper left", "NARUTO — YOU'RE HURT."),
        (5, BOY, "upper right", "A CURSED SEAL. HE PUT IT THERE ON PURPOSE.")),
  R("naruto_13_sword", "sakura", "sasuke"), "high"),

 ("p12", dict(scene="dialogue", light="dark", cast="small_group", mood="somber", panels=5),
  FILL + N13S.format(i=1) + SAK.format(i=2) + SAS.format(i=3) + ONLY(BOY, GIRL, UCH) +
  "FIVE panels, uneven.\n"
  "PANEL 1 (small): the girl's hand on the unconscious boy's forehead, then pulling back.\n"
  "PANEL 2 (small): her face — he is burning up.\n"
  "PANEL 3 (small): the blond boy taking the unconscious boy's weight across one shoulder.\n"
  "PANEL 4 (dominant, middle): the blond boy standing with the other boy over his shoulder, seen "
  "from a low angle, worn out and carrying him anyway, the girl small beside him; the black forest "
  "closing in above them both.\n"
  "PANEL 5 (wide, bottom): the three of them setting off, seen from behind, small against the "
  "trunks. " + FOR
  + SAY((2, GIRL, "upper left", "HE'S BURNING UP."),
        (4, BOY, "upper right", "STRAIGHT TO THE TOWER."),
        (5, BOY, "upper left", "I AM NOT SPENDING ANOTHER NIGHT IN THIS FOREST.")),
  R("naruto_13_sword", "sakura", "sasuke"), "high"),
]

if __name__ == "__main__":
    run(PAGES, HERE / "v3ch02" / "raw", HERE / "v3ch02" / "ledger.json")
