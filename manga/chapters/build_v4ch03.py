"""Volume 4, Chapter 3 — "Brothers". 16 pages.

Source: fic ch08:203-267.  The encounter is an information duel, never a fight:
Itachi and Kisame scout, Naruto proves too much knowledge, and Naruto decides to
train alone before the chapter cuts to the two-week card.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
from runner import run  # noqa: E402
from prompts_v4 import (BOY, CAP, ENV, FILL, ITACHI, ITACHI_SPEAKER, KISAME,  # noqa: E402
                        KISAME_SPEAKER, N13, ONLY, R, SAY, SFX, ZET)

MANGEKYO = ("Image {i} is the EYE-DESIGN REFERENCE for the blond boy's custom Mangekyo: "
            "a six-bladed black pattern in a blood-red iris, distinct from Itachi's eye. Use this "
            "exact custom design whenever his Mangekyo is active; never draw a generic pinwheel. ")
L_OUTSKIRTS = ("Lighting: overcast late-afternoon forest light on a quiet road outside Konoha; "
               "the distant village wall is small and inactive. ")
L_COMPOUND = ("Lighting: quiet late-afternoon blue-grey light across intact traditional timber "
              "homes, clean tiled roofs, and empty lanes. ")
L_SHRINE = ("Lighting: hard cool overhead and slanting light in a sealed ancestral stone chamber; "
            "the tablet and stone pillars stay legible, with no glow effects. ")
ZETSU_SYMBOL = "the faint symbolic split plant silhouette"

PAGES = [
 ("p01", dict(scene="establishing", light="overcast", cast="two", mood="tense", panels=6),
  FILL + ITACHI.format(i=1) + KISAME.format(i=2) + ENV.format(i=3) + ONLY(ITACHI_SPEAKER, KISAME_SPEAKER) +
  "SIX panels, uneven three rows. The dominant wide top panel takes about forty-five percent of "
  "the page; three narrow lower panels compress information into glances and objects.\n"
  "PANEL 1 (dominant, top): from a high tree branch, two black red-cloud-cloaked men walk away "
  "from Konoha down a forest road, small in frame. Both straw hats hide their faces; the taller "
  "man's bandage-wrapped sword cuts his silhouette. Keep the distant village wall calm and tiny, "
  "with clear upper sky for captions.\n"
  "PANEL 2 (narrow): low crop on paired red-cloud cloaks moving in opposite step.\n"
  "PANEL 3 (narrow): bandage-wrapped Samehada across the taller man's back; no face.\n"
  "PANEL 4 (small detached): abstract rumour motifs only — an Uchiha eye, a Nine-Tails seal, and "
  "blank paper fragments; no readable in-world writing.\n"
  "PANEL 5 (small): under the shorter man's hat brim, one red Mangekyo eye turns back toward Konoha.\n"
  "PANEL 6 (wide bottom): the tall man recedes while the shorter man remains motionless in the "
  "foreground. " + L_OUTSKIRTS
  + CAP(1, "upper left sky", "THEY CAME FOR THE NINE-TAILS HOST.")
  + CAP(1, "upper right sky", "IN KONOHA, THEY FOUND RUMOURS OF AN UCHIHA WITH A MANGEKYO."),
  R("itachi", "kisame", "env_konoha_outskirts"), "high"),

 ("p02", dict(scene="departure", light="overcast", cast="two", mood="tense", panels=5),
  FILL + ITACHI.format(i=1) + KISAME.format(i=2) + ENV.format(i=3) + ONLY(ITACHI_SPEAKER, KISAME_SPEAKER) +
  "FIVE panels, uneven. The last panel is a silent object beat.\n"
  "PANEL 1 (medium): over the tall shark-faced man's cropped shoulder, the shorter man stands "
  "across the road, directing him onward.\n"
  "PANEL 2 (small): the tall man half-turns, his mouth set to reply; leave a clear balloon shelf.\n"
  "PANEL 3 (dominant): the shorter man dissolves into a diagonal murder of opaque black crows and "
  "hard-edged feathers, not smoke, glow, or a crows attack.\n"
  "PANEL 4 (small): high rear view of the tall man walking alone, Samehada the one dominant shape.\n"
  "PANEL 5 (wide bottom): empty forest road with scattered black feathers. " + L_OUTSKIRTS
  + SAY((1, ITACHI_SPEAKER, "upper left", "GO ON TO THE MEETING POINT, KISAME."),
        (1, ITACHI_SPEAKER, "upper right", "I WANT TO CONFIRM SOMETHING."))
  + SFX(3, "FWHRR", "Black feather silhouettes cross the word."),
  R("itachi", "kisame", "env_konoha_outskirts"), "high"),

 ("p03", dict(scene="establishing", light="late_afternoon", cast="solo", mood="somber", panels=6),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ONLY(BOY) +
  "SIX panels, uneven. The gate owns the dominant opening; Naruto carries no weapon.\n"
  "PANEL 1 (wide dominant): rear view of the blond thirteen-year-old approaching the Uchiha "
  "compound gate, small beneath its weathered timber span. He wears the black shirt with red "
  "Uzumaki spiral, black trousers, gloves and boots; shoulder-length blond hair hides his right eye.\n"
  "PANEL 2 (small): his black-gloved hand and red chest spiral near the gate wood.\n"
  "PANEL 3 (small): his visible left eye narrows toward the empty street.\n"
  "PANEL 4 (medium): beyond the gate, intact closed homes and only light grass at the edges; no people.\n"
  "PANEL 5 (small): Naruto walks alone lower right, swallowed by the street's negative space.\n"
  "PANEL 6 (small, flat white): profile close-up, expression closed rather than nostalgic. " + L_COMPOUND
  + CAP(6, "upper left", "THE COMPOUND WOULD MAKE HIM HARDER TO REACH.")
  + CAP(6, "lower right", "SASUKE WOULD MAKE IT HARDER TO LIVE HERE."),
  R("naruto_13", "mangekyo_design", "env_uchiha_compound"), "high"),

 ("p04", dict(scene="environmental", light="late_afternoon", cast="solo", mood="somber", panels=7),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ONLY(BOY) +
  "SEVEN panels, uneven. The high-angle compound page is dominant and must show intact emptiness, "
  "never massacre ruins.\n"
  "PANEL 1 (dominant, top): high angle over clean roofs, paths, courtyards and one tiny Naruto.\n"
  "PANEL 2 (small): a child-height handrail and a closed sliding door; nobody present.\n"
  "PANEL 3 (small): Naruto's boots pass a swept threshold, cropped at the knees.\n"
  "PANEL 4 (small memory-register): the same lane with only pale anonymous halftone silhouettes; "
  "not a literal flashback and no identifiable people.\n"
  "PANEL 5 (small): the present lane from the same view, vacant.\n"
  "PANEL 6 (small): Naruto's unreadable face; one eye stays largely hidden by hair.\n"
  "PANEL 7 (wide bottom): his back as he turns toward the deeper shrine path. " + L_COMPOUND
  + CAP(1, "upper left", "THE UCHIHA COMPOUND WAS STILL INTACT.")
  + CAP(5, "upper right", "ONLY THE PEOPLE WERE GONE."),
  R("naruto_13", "mangekyo_design", "env_uchiha_compound"), "high"),

 ("p05", dict(scene="revelation", light="cool", cast="solo", mood="tense", panels=6),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ENV.format(i=4) + ONLY(BOY) +
  "SIX panels, uneven. The shrine threshold is the dominant beat.\n"
  "PANEL 1 (small): narrow forested stone approach to Naka Shrine, Naruto tiny at its foot.\n"
  "PANEL 2 (small): extreme close-up of Naruto's active custom six-bladed Mangekyo eye, never a "
  "generic pinwheel.\n"
  "PANEL 3 (small): his gloved hand makes the specific shrine pass gesture, cropped by the edge.\n"
  "PANEL 4 (dominant): the threshold opens to a cool shadowed ancestral stone chamber; Naruto is a "
  "small silhouette crossing inward and the clan tablet anchors the geometry.\n"
  "PANEL 5 (small): tablet carvings as abstract illegible lines, no invented writing.\n"
  "PANEL 6 (narrow bottom): Naruto alone inside; the doorway is a hard rectangle of pale light. "
  + L_SHRINE + CAP(4, "upper left", "ONLY UCHIHA MAY ENTER."),
  R("naruto_13", "mangekyo_design", "env_uchiha_compound", "env_naka_shrine"), "high"),

 ("p06", dict(scene="revelation", light="cool", cast="solo", mood="tense", panels=6),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ENV.format(i=4) + ONLY(BOY) +
  "SIX panels, uneven. The dominant panel is Naruto dwarfed by the tablet, not a new revelation.\n"
  "PANEL 1 (medium): three-quarter rear view of Naruto at the tablet; his Mangekyo red is the only warm colour.\n"
  "PANEL 2 (small): his visible eye tracks abstract carvings that remain unreadable.\n"
  "PANEL 3 (small symbolic): a black ring behind a second sealed stone layer, an unreachable visual "
  "metaphor rather than a new object.\n"
  "PANEL 4 (small): his finger stops at an unresponsive portion of the tablet.\n"
  "PANEL 5 (small memory fragment): a dark hideout tablet copy and an indistinct robed silhouette, "
  "with no readable text and no named figure visible.\n"
  "PANEL 6 (dominant bottom): Naruto turns away unchanged; the private chamber, not discovery, is "
  "what matters. " + L_SHRINE
  + CAP(2, "upper left", "THE MANGEKYO READS ONLY PART OF THE TABLET.")
  + CAP(3, "lower left", "ONLY THE RINNEGAN CAN READ THE REMAINING SEALED LAYER.")
  + CAP(5, "upper right", "MADARA HAD ALREADY TAUGHT HIM WHAT HE COULD USE."),
  R("naruto_13", "mangekyo_design", "env_naka_shrine", "env_madara_eye_vault"), "high"),

 ("p07", dict(scene="revelation", light="cool", cast="two", mood="tense", panels=7),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ITACHI.format(i=3) + ENV.format(i=4) +
  ONLY(BOY, ITACHI_SPEAKER) +
  "SEVEN panels, uneven. The final distant two-shot is dominant; this is recognition, not a fight.\n"
  "PANEL 1 (small): Naruto's visible left eye narrowing.\n"
  "PANEL 2 (small): red-cloud cloak hem enters the shrine's far shadow.\n"
  "PANEL 3 (small): Naruto turns only his shoulders; the newcomer stays backlit and mostly faceless.\n"
  "PANEL 4 (medium): hat-off silhouette of Itachi in the doorway, long black hair and high cloak collar "
  "framed by the tablet and stone pillars.\n"
  "PANEL 5 (small): Naruto low in frame, with space for a precise small balloon.\n"
  "PANEL 6 (small): Itachi's distinct red Mangekyo framed by long black hair; he wears no hat inside the shrine.\n"
  "PANEL 7 (dominant bottom): radically deep two-shot — Naruto's cropped foreground shoulder and back, "
  "Itachi small near the tablet. No combat stance, weapon, chakra effect, or attack. " + L_SHRINE
  + SAY((5, BOY, "upper left", "UCHIHA ITACHI.")),
  R("naruto_13", "mangekyo_design", "itachi", "env_naka_shrine"), "high"),

 ("p08", dict(scene="dialogue", light="cool", cast="two", mood="tense", panels=6),
  FILL + ITACHI.format(i=1) + N13.format(i=2) + MANGEKYO.format(i=3) + ENV.format(i=4) +
  ONLY(ITACHI_SPEAKER, BOY) +
  "SIX panels, uneven. The overhead tablet composition is dominant.\n"
  "PANEL 1 (small): hatless Itachi's bare hand settles at his high collar as he studies Naruto, long black hair "
  "framing his narrow face.\n"
  "PANEL 2 (small): he steps closer but stops with unmistakable empty space between them; his Mangekyo activates.\n"
  "PANEL 3 (narrow): split close-up of two distinct eyes — Naruto's custom six-bladed pattern and "
  "Itachi's own pattern, never merged.\n"
  "PANEL 4 (medium): Itachi states the proof calmly, no shock performance.\n"
  "PANEL 5 (small): Naruto side profile against flat black, refusing an ancestry explanation.\n"
  "PANEL 6 (dominant): from high above, the two stand on opposite sides of the tablet, small and "
  "separated by it. " + L_SHRINE
  + SAY((4, ITACHI_SPEAKER, "upper left", "SO IT IS TRUE. YOU ARE OF MY CLAN."),
        (4, ITACHI_SPEAKER, "upper right", "HOW THAT CAME TO BE RAISES MANY QUESTIONS."),
        (5, BOY, "upper left", "ACCEPT WHAT YOU CAN SEE.")),
  R("itachi", "naruto_13", "mangekyo_design", "env_naka_shrine"), "high"),

 ("p09", dict(scene="dialogue", light="cool", cast="two", mood="tense", panels=7),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ITACHI.format(i=3) + ENV.format(i=4) +
  ONLY(BOY, ITACHI_SPEAKER) +
  "SEVEN panels, uneven. One silent cloak/object panel breaks the verbal rhythm.\n"
  "PANEL 1 (small): Naruto's mouth in close crop asks the question.\n"
  "PANEL 2 (small): Itachi's face nearly still.\n"
  "PANEL 3 (small silent): a red-cloud cloak pattern on flat black.\n"
  "PANEL 4 (medium): Itachi answers without any capture or attack imagery.\n"
  "PANEL 5 (small): Naruto's visible eye, unblinking, as Itachi asks his source.\n"
  "PANEL 6 (small): Naruto dismisses Jiraiya as that source.\n"
  "PANEL 7 (dominant bottom): empty shrine lantern and hard stone wall, carrying the unexplained gap. "
  + L_SHRINE
  + SAY((1, BOY, "upper left", "HAS AKATSUKI BEGUN HUNTING BIJUU?"),
        (4, ITACHI_SPEAKER, "upper left", "NO. WE ARE ONLY COLLECTING INFORMATION ON JINCHURIKI."),
        (5, ITACHI_SPEAKER, "upper right", "HOW DO YOU KNOW?"),
        (6, BOY, "upper left", "JIRAIYA HAS TOLD ME NOTHING USEFUL.")),
  R("naruto_13", "mangekyo_design", "itachi", "env_naka_shrine"), "high"),

 ("p10", dict(scene="dialogue", light="cool", cast="two", mood="tense", panels=6),
  FILL + ITACHI.format(i=1) + N13.format(i=2) + MANGEKYO.format(i=3) + ENV.format(i=4) +
  ONLY(ITACHI_SPEAKER, BOY) +
  "SIX panels, uneven. The partner is recalled only as a Samehada object inset, never present in the shrine.\n"
  "PANEL 1 (small): Itachi asks again in a narrow calm close-up.\n"
  "PANEL 2 (small): Naruto looks past him toward the exit.\n"
  "PANEL 3 (small inset): Samehada alone — the bandage-wrapped sword fills the flat-black inset, with "
  "no body, face, or recognizable silhouette; it is not a simultaneous location scene.\n"
  "PANEL 4 (small): Itachi's eye widens only a fraction.\n"
  "PANEL 5 (medium): Naruto's gloved hand rests on the tablet, claiming control of the room's information.\n"
  "PANEL 6 (dominant bottom): both in profile, separated by a black gutter-like band of empty space. "
  + L_SHRINE
  + SAY((2, BOY, "upper left", "I EXPECTED THAT QUESTION FROM YOUR PARTNER."),
        (6, ITACHI_SPEAKER, "upper right", "HOW MUCH DO YOU KNOW?")),
  R("itachi", "naruto_13", "mangekyo_design", "env_naka_shrine"), "high"),

 ("p11", dict(scene="dialogue", light="cool", cast="two", mood="tense", panels=6),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ITACHI.format(i=3) + ENV.format(i=4) +
  ONLY(BOY, ITACHI_SPEAKER) +
  "SIX panels, uneven. Naruto's statement under empty stone is dominant.\n"
  "PANEL 1 (dominant, top): Naruto low in frame beneath a great field of empty dark stone, level and still.\n"
  "PANEL 2 (small): Itachi eye close-up, widening only slightly.\n"
  "PANEL 3 (small abstract diagram): four unlabelled black points, with Naruto and Itachi as the "
  "only legible foreground figures; the other two are non-human symbolic marks, not revealed people.\n"
  "PANEL 4 (medium): Naruto's cold acknowledgement of the massacre's effect on the clan name.\n"
  "PANEL 5 (small): Itachi in grey halftone, an unreadable smile beginning then gone.\n"
  "PANEL 6 (wide bottom): a red cloud pattern crosses the panel border, tightening the air. " + L_SHRINE
  + SAY((1, BOY, "upper left", "I KNOW AKATSUKI. I KNOW FOUR UCHIHA ARE ALIVE."),
        (4, BOY, "upper left", "I THANK YOU. THE UCHIHA NAME WOULD HAVE BEEN DEGRADED."),
        (5, ITACHI_SPEAKER, "upper right", "YOU HAVE MATURED, NARUTO-KUN.")),
  R("naruto_13", "mangekyo_design", "itachi", "env_naka_shrine"), "high"),

 ("p12", dict(scene="dialogue", light="cool", cast="two", mood="somber", panels=7),
  FILL + ITACHI.format(i=1) + N13.format(i=2) + MANGEKYO.format(i=3) + ENV.format(i=4) +
  ONLY(ITACHI_SPEAKER, BOY) +
  "SEVEN panels, uneven. It is a cold calculation, not an angry threat.\n"
  "PANEL 1 (small): Itachi in side view asks about Sasuke.\n"
  "PANEL 2 (small): Naruto's gloved hand closes over the red spiral on his chest.\n"
  "PANEL 3 (small symbolic): an unlabelled lone dark silhouette in a blank white field, with no "
  "massacre image and no identifiable third character.\n"
  "PANEL 4 (medium): Naruto's visible eye, flat and without softening.\n"
  "PANEL 5 (small): Itachi turns away, hair and high collar concealing most of his expression.\n"
  "PANEL 6 (dominant): silent medium view with tablet between them, Naruto cropped close and Itachi small distant.\n"
  "PANEL 7 (small): Itachi's eye, care shown only by restraint. " + L_SHRINE
  + SAY((1, ITACHI_SPEAKER, "upper left", "DO YOU INTEND TO TELL SASUKE THE TRUTH?"),
        (4, BOY, "upper right", "IF I DO, I WILL HAVE TO KILL HIM.")),
  R("itachi", "naruto_13", "mangekyo_design", "env_naka_shrine"), "high"),

 ("p13", dict(scene="departure", light="cool", cast="two", mood="somber", panels=5),
  FILL + ITACHI.format(i=1) + N13.format(i=2) + MANGEKYO.format(i=3) + ENV.format(i=4) +
  ONLY(ITACHI_SPEAKER, BOY) +
  "FIVE panels, uneven. The empty shrine after the departure is dominant.\n"
  "PANEL 1 (small): Itachi turns toward the exit, cloak moving slightly; no hand sign or strike.\n"
  "PANEL 2 (medium): close-up as he names the next meeting, controlled and quiet.\n"
  "PANEL 3 (small): Naruto from behind does not answer; the tablet remains in view.\n"
  "PANEL 4 (small): Itachi's cloak enters the bright doorway rectangle.\n"
  "PANEL 5 (dominant bottom): the shrine empty except for Naruto, a small dark figure before the tablet; "
  "the space Itachi leaves feels physical. " + L_SHRINE
  + SAY((2, ITACHI_SPEAKER, "upper left", "NEXT TIME WE MEET, IT WILL BE IN BATTLE."),
        (2, ITACHI_SPEAKER, "lower right", "BE STRONGER THEN.")),
  R("itachi", "naruto_13", "mangekyo_design", "env_naka_shrine"), "high"),

 ("p14", dict(scene="decision", light="late_afternoon", cast="solo", mood="somber", panels=6),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ENV.format(i=4) + ENV.format(i=5) + ONLY(BOY) +
  "SIX panels, uneven. Naruto's departure through the compound is the dominant visual decision.\n"
  "PANEL 1 (small): Naruto's profile in shrine shadow, one custom Mangekyo still active.\n"
  "PANEL 2 (small): quiet exterior rooftops and a distant Konoha wall, contained and unalarmed.\n"
  "PANEL 3 (small symbolic): an abstract red cloud overlay above the village, with no Akatsuki attack.\n"
  "PANEL 4 (medium): Naruto's boot crosses the shrine threshold toward the compound street.\n"
  "PANEL 5 (small): hard-lit fragment of a remote hideout entrance; no person or Zetsu appears.\n"
  "PANEL 6 (dominant bottom): rear wide shot of Naruto walking away from the compound, small in a long village corridor. "
  + L_COMPOUND
  + CAP(3, "upper left", "AKATSUKI IS MOVING.")
  + CAP(6, "upper right", "KONOHA CANNOT GIVE HIM UNINTERRUPTED TRAINING."),
  R("naruto_13", "mangekyo_design", "env_naka_shrine", "env_uchiha_compound", "env_madara_hideout_exit"), "high"),

 ("p15", dict(scene="decision", light="dusk", cast="solo", mood="somber", panels=5),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ZET.format(i=3) + ENV.format(i=4) + ENV.format(i=5) + ENV.format(i=6) + ONLY(BOY, ZETSU_SYMBOL) +
  "FIVE panels, uneven. The hideout image is only Naruto's destination thought, not a present meeting.\n"
  "PANEL 1 (small): an empty close-up of Naruto's apartment key beside a closed door; no one is present.\n"
  "PANEL 2 (small): Naruto's gloved hand grips his gear strap, cropped by the edge; no sword.\n"
  "PANEL 3 (dominant): black-background symbolic panel. Naruto is tiny at bottom; a distant hideout "
  "silhouette rises behind him and a separate faint split Venus-flytrap outline suggests Zetsu, clearly "
  "as a future destination rather than a person physically with Naruto.\n"
  "PANEL 4 (small): tight active custom Mangekyo eye, controlled resolve without rage or a smile.\n"
  "PANEL 5 (wide bottom): Naruto leaves frame through a deep Konoha alley, destination undisclosed to the village. "
  "Lighting: blue-grey dusk, long hard shadows, no other people. "
  + CAP(3, "upper left", "HE NEEDS YEARS AWAY TO TRAIN.")
  + CAP(3, "lower right", "AT THE HIDEOUT, NO ONE WILL INTERRUPT HIM."),
  R("naruto_13", "mangekyo_design", "zetsu", "env_apartment_ext", "env_madara_hideout_exit", "env_alley"), "high"),

 ("p16", dict(scene="time_jump", light="night", cast="solo", mood="somber", panels=2),
  FILL + N13.format(i=1) + MANGEKYO.format(i=2) + ENV.format(i=3) + ONLY(BOY) +
  "TWO panels only, uneven. PANEL 1 is the dominant large borderless panel, taking most of the page: night over "
  "Konoha, Naruto a small silhouette on a roofline looking outward, off-centre and never heroic; keep "
  "the upper third as substantial empty night sky. PANEL 2 is a smaller plain black field with a clean "
  "central deterministic time card. Do not show Tsunade, Shizune, Jiraiya, a celebration, the Hokage "
  "office, or any future event. No speech balloons. "
  "Lighting: deep blue-black night, quiet rooflines, no glow. "
  + CAP(2, "center", "TWO WEEKS LATER"),
  R("naruto_13", "mangekyo_design", "env_konoha_after_invasion"), "high"),
]


if __name__ == "__main__":
    run(PAGES, HERE / "v4ch03" / "raw", HERE / "v4ch03" / "ledger.json")
