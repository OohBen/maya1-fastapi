# Volume 4, Chapter 5 — *Orange*

**Source span:** fic ch9, `ch09.txt:11-427`.  This chapter deliberately stops before the Oto-wide aftermath, the Konoha report, Karin's on-page introduction, and the Yugao hook (`ch09.txt:437-525`).

**Target:** 24 portrait pages.  **Engine:** Naruto comes out of hiding to take two things—Karin and the Shinigami mask—but the chapter's dramatic answer is that his power is immense, expensive, and still cannot force Orochimaru to yield.

## Continuity in

- Two years and eight months have passed since ch8. Naruto is now an older teen, approximately sixteen: taller, with long blond hair below his shoulders still hiding his right eye. He wears red Madara-style plated armour over black, a partly obscured Konoha protector, a modified gunbai, and a **new** sword at his sash (`manga/.source/uchiha-naruto-the-sage/ch09.txt:11-16`). This is not the ninjato lost in Volume 3.
- Naruto left Konoha alone, did not become Jiraiya's student, and trained in Madara's hideout. Zetsu remains his only on-page companion at the opening (`ch09.txt:13-31`).
- Kakashi trains Sasuke; Jiraiya has failed to find Naruto. Keep the parallel scene brief: it measures Naruto's absence instead of treating it as a second plot (`ch09.txt:35-71`).
- Naruto has Eternal Mangekyō Sharingan in both eyes. The orange Susano'o must not resemble the purple Volume 3 form; ch9 explicitly changes its colour to match his chakra (`ch09.txt:3-5`, `371-381`).

## Required references before scripting

| Asset key | Use | Non-negotiable design/state |
|---|---|---|
| `naruto_16_armored` | Every Naruto page | Approximately sixteen, lean and long-limbed; below-shoulder blond hair with right eye hidden; black base clothes; bright red segmented samurai-like armour; partial Konoha protector; modified gunbai on back; **new plain straight sword in sash**. No orange jumpsuit, grin, or lost ninjato. |
| `zetsu` | pp. 1–2, 24 | Split white/black body, yellow eyes, flytrap collar; never substitute a human companion. |
| `kakashi_16`, `sasuke_16`, `jiraiya` | pp. 3–4 only | Post-training-trip versions; Sasuke is an older teen, not a child, and does not wear Naruto's armour. |
| `orochimaru`, `kabuto` | pp. 6–24 as present | Bind both whenever their bodies are visible. Orochimaru: white skin, long black hair, slit yellow eyes; Kabuto: silver hair, round glasses. |
| `manda` | pp. 15–19 | Colossal purple-grey serpent, far larger than Naruto; show scale through terrain and a small Naruto, not by shrinking Manda. |
| `susanoo_orange` | pp. 17–18 | Giant opaque orange armoured humanoid; hood, two forward horns, plate-like guards, two swords fused into one. Effects remain legible around it. |
| `env_madara_hideout_exit`, `env_oto_hidden_base`, `env_oto_throne_hall`, `env_oto_broken_exterior` | Location anchors | Hideout is rock-carved and dark; throne hall has the snake statue; exterior is the collapse breach under clear daylight. |

**Reference-order rule:** list character references in the same order they are named in the page prompt, then the environment and a style page last. Bind a character if any part of their body is drawn; do not use an unbound "opponent," "old man," or "assistant" as a loophole (`manga/PIPELINE.md:244-258`).

## Technique and damage ledger

| Beat | Naruto state | Opponent state | Carry-forward rule |
|---|---|---|---|
| Opening | Rested; Sharingan active when leaving | None | Armour, gunbai, and new sash sword all present. |
| Underground duel | Uses taijutsu, sword, fire, then rib-cage Susano'o | Orochimaru repeatedly evades/sheds skin; Kabuto joins after the mask demand | The sword parries Kusanagi only while wind-chakra reinforced (`ch09.txt:189-201`). |
| Collapse / exterior | EMS active; left eye strains/bleeds after Amaterasu | Kabuto has cuts and regenerates at chakra cost; Orochimaru is depleted but mobile | Keep the sword wound on Naruto's **right shoulder** and broken right shoulder plate after Kusanagi (`ch09.txt:325-331`). |
| Manda climax | Uses gunbai, finished orange Susano'o, fire, Amaterasu, wind+Amaterasu | Manda withdraws under black flame; Orochimaru and Kabuto are drained | Susano'o drops before the final fire/Amaterasu sequence; do not keep it active invisibly (`ch09.txt:371-389`). |
| End | Chakra-depleted; gunbai used as a cane; EMS deactivated | Orochimaru and Kabuto escape | Naruto wins the encounter but fails both objectives in this chapter. |

## Page script

All speech below is an adaptation paraphrase, not source wording. Lock final lettering before image generation. Maintain a left-to-right reading path, unequal panel areas, deliberate blank shelves for balloons, and no even line-up of three characters (`manga/refs/MANGA_STAGING_GUIDE.md:35-71`, `135-177`).

### p01 — The door opens — 1 panel, chapter-opening splash

- **Staging/camera:** Borderless vertical splash from behind Naruto, small at the black mouth of Madara's hideout while a hard white daylight wedge cuts across the cavern floor. Gunbai and sword silhouette dominate; Zetsu is only a half-seen plant shape emerging from the wall, far below frame left.
- **Action:** Naruto leaves after 2 years, 8 months of isolation; Zetsu notes that he is finally going out (`ch09.txt:11-19`).
- **Lettering:** Caption: “TWO YEARS, EIGHT MONTHS LATER.” Zetsu, off-panel: “You are leaving at last.” Naruto: “I have trained enough.”
- **SFX:** None. Preserve a calm upper third for the title plate.

### p02 — What he is taking — 5 panels

- **Staging/camera:** Top dominant horizontal: profile close-up of Naruto's visible Sharingan against sun. Three thin descending panels: the red plates, the gunbai face (Uzumaki swirl and Uchiha crest), then his gloved hand settling on the new sword's sash. Bottom wide panel: Zetsu sinks into shadow while Naruto walks toward light.
- **Action:** Naruto names the Oto hideout, Karin, and the Shinigami mask; he dismisses the chance of meeting Orochimaru and tells Zetsu to stay hidden (`ch09.txt:20-31`).
- **Lettering:** Naruto: “Orochi's border base. The Uzumaki girl and the mask.” Zetsu: “Jiraiya and Konoha will see you once you surface.” Naruto: “Then I will deal with them.”
- **SFX:** Small boot echo: “KLANG.”

### p03 — The people left looking — 6 panels

- **Staging/camera:** Hard cut to River Country. Establishing top strip: burned grass and splintered trees, no people. Dominant middle panel: Kakashi and Jiraiya in depth—Kakashi's masked shoulder huge/cropped in foreground, Jiraiya a smaller full figure across the scarred ground. Small inset: Sasuke, turned away, wiping blood from a spar.
- **Action:** Show that Kakashi and Sasuke have been training during Naruto's absence and have gained strength (`ch09.txt:33-49`).
- **Lettering:** Jiraiya: “You have both outgrown drills.” Kakashi: “Then he needs missions.” Sasuke, small: “And Naruto?”
- **SFX:** Wind over wrecked grass: “SHHH.”

### p04 — No trail — 5 panels

- **Staging/camera:** Top narrow close-up on Jiraiya's eye, then a white-space panel of Sasuke's narrowed face. Dominant lower wide: the three figures separated at different depths, Jiraiya walking out of frame while Kakashi occupies a cropped foreground edge and Sasuke remains alone in the distance.
- **Action:** Jiraiya admits he has no lead on Naruto; Kakashi refuses to estimate Naruto's strength. One week later, Naruto reaches the Oto base (`ch09.txt:53-81`).
- **Lettering:** Jiraiya: “No trail. He chose to vanish.” Kakashi: “We will find out when he wants us to.” Caption: “ONE WEEK LATER — OTŌ BORDER.”
- **SFX:** On the page turn/bottom strip, Naruto's fireball blows open the false stone entrance: “WHOOOM.”

### p05 — Entering the nest — 6 panels

- **Staging/camera:** Top wide establishes the blasted stone aperture in a natural cliff. Three tall corridor panels pull Naruto inward from a rear view; red armour is the only warm colour. A small black panel shows three passages. Bottom dominant: Naruto walks down the middle passage, armour plates ringing into darkness.
- **Action:** He chooses the path Zetsu mapped toward Orochimaru's throne room; do not introduce guards the source does not show (`ch09.txt:75-87`).
- **Lettering:** Naruto, thought/caption: “The central passage.” No dialogue in the final two panels.
- **SFX:** “KLANG… KLANG…” from armour. Keep black negative space between the echoes.

### p06 — The throne hall — 5 panels

- **Staging/camera:** Dominant upper panel: low angle from behind Naruto into the cavernous throne room, with Orochimaru seated tiny beneath the giant snake statue and Kabuto standing offset—not a row. Lower close-ups: Kabuto's round glasses, Orochimaru's slit pupil, Naruto folding his arms.
- **Action:** Orochimaru and Kabuto have expected him. Naruto states he came to take a person and an object (`ch09.txt:87-99`).
- **Lettering:** Naruto: “You kept something and someone that are mine.” Orochimaru: “You have grown into a familiar silhouette.”
- **SFX:** Quiet cave drip: “TIK.”

### p07 — The offer becomes a challenge — 6 panels

- **Staging/camera:** Start with a cropped Orochimaru smile; shift to a black-background profile of Naruto as Orochimaru identifies Uchiha/Senju traits. Dominant lower panel: Naruto's fireball passes between Orochimaru and Kabuto and destroys the throne, silhouettes rimmed by flame.
- **Action:** Orochimaru probes Naruto's blood and offers revenge against Konoha. Naruto rejects the recruitment with a deliberate fireball and Orochimaru elects to test him himself (`ch09.txt:99-125`).
- **Lettering:** Orochimaru: “You carry two bloodlines.” Naruto: “You have noticed enough.” Naruto: “I did not come to join you.” Orochimaru: “Then show me what two years bought.”
- **SFX:** Throne impact: “KRAAASH.”

### p08 — First exchange — 7 panels

- **Staging/camera:** Use seven quick uneven panels: foot against forearm, intercepted kicks, locked hands, Naruto's face half hidden by hair, a shockwave viewed from floor level, Kabuto observing from a cropped edge, and a dominant bottom panel of Naruto forcing Orochimaru toward one knee.
- **Action:** Begin as taijutsu. Naruto reads attacks with Sharingan and wins the strength contest, but Orochimaru's speed can still launch him into the wall (`ch09.txt:129-177`).
- **Lettering:** Naruto: “That is your test?” Orochimaru: “A test requires effort.” Naruto: “Then use more.”
- **SFX:** “THOOM,” “KRAK,” “WHUMP.” Effects are opaque ink shapes; stone floor remains readable.

### p09 — Steel against snakes — 6 panels

- **Staging/camera:** Top letterbox: snakes burst from Orochimaru's sleeve toward the lens. Two tall panels: Naruto's new sword clears them in a single controlled arc, then a close-up of Orochimaru's mouth opening around Kusanagi. Dominant bottom: crossed blades in three depth layers—Naruto's shoulder foreground, blades center, Orochimaru small beyond.
- **Action:** Naruto shows sword skill. Orochimaru produces Kusanagi; Naruto reinforces his own new blade with wind chakra to keep it intact (`ch09.txt:151-201`).
- **Lettering:** Orochimaru: “The fan. The eyes. Why hide them?” Naruto: “Because you have not earned them.”
- **SFX:** Blade cuts: “SHHK.” Blade lock: “KLANG.”

### p10 — Too much fire — 5 panels

- **Staging/camera:** Begin with a near-black narrow panel of Naruto's hand seals. Dominant diagonal panel: his fire release fills a deep corridor, but pillars, rock, and exit line remain visible. Three small reaction panels: Orochimaru escaping, supports cracking, Naruto realizing the ceiling is coming down.
- **Action:** Naruto's wide fire attack melts supports and destabilizes the underground base; he uses the rib-cage Susano'o to take the returning mud dragon (`ch09.txt:205-219`).
- **Lettering:** Naruto, small: “Too much.” Orochimaru, off-panel: “Mud Dragon.”
- **SFX:** “FWOOSH,” “KRRRKK.” Do not make the rib-cage form the finished humanoid Susano'o yet.

### p11 — The mask question — 6 panels

- **Staging/camera:** Wide panel of half-collapsed throne hall under a new daylight shaft. Inset close-up: Orochimaru, scorched then reformed, on one knee. Kabuto enters from an extreme foreground crop. Bottom dominant: Naruto releases dense, dark-edged chakra that lifts debris; figures remain visible through the effect.
- **Action:** Naruto asks about the Shinigami mask. Orochimaru stalls; Naruto's annoyance breaks the remaining structure open (`ch09.txt:223-261`).
- **Lettering:** Naruto: “The mask. Did you take it?” Orochimaru: “Perhaps.” Naruto: “I am done asking.”
- **SFX:** Cave break: “GROOOOM.”

### p12 — Kabuto's answer — 7 panels

- **Staging/camera:** Seven fast panels with a dominant center panel: Naruto's wind blades cut Kabuto across the torso. Surround it with small inserts of Kabuto's wound closing, glasses being pushed up, glowing scalpels, and Naruto registering the regenerative technique. Final wide strip: both Orochimaru and Kabuto bracket Naruto at different depths.
- **Action:** Kabuto regenerates by spending chakra. Naruto becomes interested, then the two opponents force him out through the collapsed breach (`ch09.txt:263-291`).
- **Lettering:** Kabuto: “Damaged cells can be restarted.” Naruto: “Show me again.”
- **SFX:** Wind blades: “SHRAK.” Collapse/exit: “KRA-BOOM.”

### p13 — Open ground, two-on-one — 6 panels

- **Staging/camera:** Establish exterior in a calm, detailed wide panel: broken hill and smoke under clean sky, sixteen-year-old Naruto tiny between Orochimaru and Kabuto. Then use narrow attacks from opposite sides. Dominant lower panel: Kabuto's scalpel sparks against Naruto's metal chest plate; Naruto's face is visible only as a cold eye through hair.
- **Action:** Outside, Orochimaru and Kabuto flank Naruto. The armour stops Kabuto's first scalpel strike; their combined wind attacks force Naruto to raise a defensive Susano'o (`ch09.txt:291-311`).
- **Lettering:** Kabuto: “Together.” Orochimaru: “He will fall.” Naruto: “You are still measuring me.”
- **SFX:** “FSSHH,” “TANG,” “WHOOOM.”

### p14 — The cut that matters — 6 panels

- **Staging/camera:** Dominant first panel: Kusanagi's elongated line crosses the page and pierces Naruto's **right shoulder plate**. Follow with a tight hand on the bleeding wound, then a small white-background panel of Naruto's blank reaction. Lower wide: black Amaterasu begins on Orochimaru while Kabuto looks up from the foreground.
- **Action:** Naruto is genuinely caught and poisoned. He remains physically resilient, but the page must mark this as a real wound and a lapse in control (`ch09.txt:313-341`).
- **Lettering:** Naruto: “Careless.” Orochimaru: “The blade carries poison.” Naruto: “It will not be enough.”
- **SFX:** Piercing metal/flesh: “SHNK.” Black flame: “FSSSS.”

### p15 — Forest, then serpent — 5 panels

- **Staging/camera:** Upper wide: wooden branches erupt diagonally, ground and opponents visible in gaps. Small side panels: Orochimaru pulls Kabuto underground; Naruto's gaze follows water bullets. Dominant final panel is a low-angle silhouette of Manda materializing through smoke, Naruto a small figure below it.
- **Action:** Naruto drives them with Wood Release. They evade; Orochimaru summons Manda to reverse the scale of the fight (`ch09.txt:315-365`).
- **Lettering:** Naruto: “It would have been cleaner if it crushed you.” Orochimaru: “Manda.” Manda: “You called for help.”
- **SFX:** Wood eruption: “GROOO.” Summon: “POOM.”

### p16 — The fan holds — 6 panels

- **Staging/camera:** Use low angles and severe scale: Manda's fangs arrive from the top edge; Naruto is framed from below, gunbai held in both hands. Three small beats show dodges through Manda's coils. Dominant bottom panel: the gunbai catches Manda's head but Naruto is pushed backward, boots carving through dirt.
- **Action:** Naruto tries giant wooden hands, abandons them, then relies on the gunbai when Manda overpowers him (`ch09.txt:365-371`).
- **Lettering:** Naruto, small: “A snake is not a handhold.” Manda: “Small Uchiha.”
- **SFX:** “THUDD,” “SKRRR.”

### p17 — Orange — 1 panel, full-page splash

- **Staging/camera:** Borderless, low and distant: Manda's huge coil makes a dark foreground ring; within it the finished orange Susano'o rises around Naruto. Its hooded head has two forward horns, plate guards, and two glowing swords joining into one. Naruto is a tiny, readable silhouette within the rib/torso space. Keep the sky, dust, and scale visible; no orange glow haze.
- **Action:** The incomplete shield develops into Naruto's full orange Susano'o (`ch09.txt:371-381`).
- **Lettering:** Manda: “What is that?” Orochimaru, small/off-panel: “A Mangekyō defence.”
- **SFX:** The only large lettering: “WOOOOOM.” Reserve no title area; this is the chapter's visual answer.

### p18 — The blade waves — 6 panels

- **Staging/camera:** Wide top: orange chakra blade wave skims ground and peels earth, Manda tiny in the distance. Four tightly cropped action panels show Manda avoiding each swing and the Susano'o sword coming down. Bottom narrow: the Susano'o dissipates; Naruto drops to one knee, small against white space.
- **Action:** The finished Susano'o cannot land a killing blow and drains Naruto. He immediately chooses fire over trying to sustain it (`ch09.txt:379-383`).
- **Lettering:** Naruto, breathless: “Then burn.”
- **SFX:** “SHRAAA,” “KROOM.”

### p19 — Black flame on a giant — 5 panels

- **Staging/camera:** Dominant upper panel: Manda crosses the page through orange fire; Orochimaru leaps away as a tiny silhouette. Two vertical reaction panels show Manda shedding and then charging. Bottom dominant close crop of Naruto's hidden right side: one eye closes; black flames take Manda's head and tail in separate, readable frames.
- **Action:** Fire forces Manda to shed skin; two Amaterasu strikes drive him back to the summoning world (`ch09.txt:383-389`).
- **Lettering:** Manda: “I will remember this.” Naruto: “Leave.”
- **SFX:** Fire “FWHOO,” black flame “SSSSS,” departure “POFF.”

### p20 — A two-headed answer — 6 panels

- **Staging/camera:** Begin with Orochimaru's sword meeting gunbai in a tight diagonal. Dominant center panel: two-headed wind dragon surges across the ground with black Amaterasu threaded in separate hard-edged tongues, terrain still readable beneath. Bottom panels: Kabuto stumbles in, Naruto catches him by the arm.
- **Action:** After Manda leaves, Naruto fuses Wind Dragon with Amaterasu and lands it on Orochimaru. Kabuto returns despite exhaustion (`ch09.txt:391-399`).
- **Lettering:** Naruto: “Wind Dragon.” Then, separate balloon: “Amaterasu.”
- **SFX:** “WRAAASH.” Do not depict the black fire as an amorphous glow.

### p21 — The answer he will not give — 6 panels

- **Staging/camera:** Top panels: Naruto slams Kabuto down and pins his arm. Dominant lower panel: a hard, unnaturally quiet Tsukuyomi moment—Kabuto's face in extreme close-up against flat black, a single ring/blade eye reflection. Final small panel: Kabuto falls, not visibly mutilated.
- **Action:** Naruto demands the secret of Kabuto's regeneration. Kabuto refuses; Naruto ends the interrogation with Tsukuyomi (`ch09.txt:397-405`).
- **Lettering:** Naruto: “Explain how you repair yourself.” Kabuto: “I would rather die.” Naruto: “Then you can answer somewhere else.”
- **SFX:** Arm break implied by a cropped hand and “KRAK.” Tsukuyomi: no lettering.

### p22 — It is not finished — 5 panels

- **Staging/camera:** Dominant first panel: Naruto's repeated kick/slam sequence uses small overlapping silhouettes against a flat white speed-line field, avoiding a row of poses. Lower panels tighten to his boot on Orochimaru's chest, then an extreme close-up of Orochimaru's mouth/body beginning to reshape into snakes. End with the escaping mass diagonally tearing out of the panel.
- **Action:** Naruto presses the mask demand, apparently kills Orochimaru, then learns the body can escape with Kabuto (`ch09.txt:407-419`).
- **Lettering:** Naruto: “Where is it?” Orochimaru: “You will not keep me.”
- **SFX:** “THOOM,” “SSSSSK.” Keep violence present but not anatomically explicit.

### p23 — The cost of orange — 4 panels

- **Staging/camera:** Top wide empty battlefield, smoke and the escape trail already gone. Dominant middle panel: Naruto on one knee, armour scraped, right shoulder plate broken, his gunbai planted like a cane; he is not posing triumphantly. Two narrow panels: Zetsu rises at his side; Naruto's EMS returns to normal eyes.
- **Action:** Naruto admits the fight took more chakra than expected; Zetsu says he was not fully serious. Naruto accepts the escape as unfinished business and redirects to Karin (`ch09.txt:421-435`).
- **Lettering:** Naruto: “That cost more than it should have.” Zetsu: “You made him suffer first.” Naruto: “Next time is shorter. Find the girl.”
- **SFX:** Only cooling fire: “TSSS.”

### p24 — The next thing taken — 2 panels, end page

- **Staging/camera:** Top wide: Naruto and Zetsu leave the ruined Oto base in opposite depth layers—Naruto a small, armoured figure walking toward the horizon; Zetsu is a cropped foreground shape sinking into grass. Bottom narrow close-up: Naruto's hand passes over the new sword's hilt without drawing it; the damaged shoulder plate remains visible.
- **Action:** End on motion toward Karin, not a false victory. The mask remains missing, Orochimaru lives, and Naruto is visibly drained (`ch09.txt:421-435`).
- **Lettering:** Caption: “THE MASK WAS NOT THERE.” Naruto, off-panel: “We search the other nests.”
- **SFX:** Armour receding: “KLANG… KLANG…”

## Continuity out

- Naruto has publicly re-entered the world in his red armour, but Chapter 5 does **not** show the later Konoha witnesses/report. Keep the public consequence for the following chapter (`ch09.txt:437-481`).
- Orochimaru and Kabuto survive. Orochimaru has spent multiple skins and is depleted; Kabuto has been wounded, exhausted, and struck with Tsukuyomi (`ch09.txt:245-267`, `397-419`).
- Naruto has not recovered the Shinigami mask. He has not yet met Karin on page. He leaves to search other Oto hideouts with Zetsu (`ch09.txt:427-435`).
- Naruto carries a persistent right-shoulder injury/armour break and is chakra-depleted at the final page. Do not reset these before a recovery beat.

## Clarity risks and manual review gate

| Risk | Review question | Reject/regenerate if |
|---|---|---|
| Time jump | Does p01 immediately establish a sixteen-year-old Naruto and the 2y8m gap? | He reads as Volume 3's thirteen-year-old or his old black-only outfit. |
| Sword continuity | Is every page clear that this is a new sash sword? | It is drawn as the previously lost back-slung ninjato, or omitted when a sword beat requires it. |
| Fight geography | Can a reader follow throne hall → collapse breach → open ground without a caption? | A page moves the fight outdoors before p12 or loses where Kabuto/Orochimaru are positioned. |
| Escalation | Do sword, fire, EMS, Wood Release, Manda, full Susano'o, then Amaterasu occur in order? | Finished orange Susano'o appears before p17 or remains active after p18. |
| Cost | Does the final image show Naruto drained despite winning the exchange? | He stands immaculate/triumphant or the broken right shoulder plate disappears. |
| Character integrity | Are Zetsu, Orochimaru, Kabuto, Manda, and Naruto bound whenever visible? | Any named combatant has wrong hair, humanized Zetsu, or Naruto's familiar orange design. |
| Reader comprehension | Can a first-time reader state Naruto's two goals, what he won, and what he failed to take? | The mask/Karin goal disappears under spectacle, or Orochimaru's escape is ambiguous. |

**Mandatory review sequence:** read the lettered pages in order at normal device size; inspect every full-resolution image actually returned; then make one continuity pass against the technique ledger and a separate balloon/speaker pass. Regenerate only the failing pages, re-read the whole chapter after each replacement. The chapter is complete only when a reviewer can follow the fight without the source text.
