# Volume 4, Chapter 7 — *Kiri*

**Status:** Builder-ready source-grounded draft.
**Source span:** fic ch10, `manga/.source/uchiha-naruto-the-sage/ch10.txt:97-415`.
**Page target:** 18 finished pages.
**Hard stop:** End after Mei accepts Naruto's help and the first-night camp aftermath. Do **not** include the `Three nights later` hill scene, which starts at source line 417.

## Purpose and engine

Naruto enters a civil war to measure himself, but every person he meets reads a different danger: Yugao sees cold cruelty, Ao sees an unknown threat, and Mei sees an impossible weapon. The chapter must make those readings legible before the next chapter turns the political promise into action.

This is not an arrival in a place where nobody knows Naruto. Yugao knows him, Zetsu has already mapped the rebel camp, Ao identifies his Konoha headband and Sharingan, and Mei has been briefed by Ao. Naruto is unknown to the rebels as a person, not unobserved. `ch10.txt:101-103, 141-145, 201-215`

## Chronology and continuity

| Item | Required state on page 1 | Source / continuity basis |
|---|---|---|
| Time and location | Immediately after the Wave-to-Kiri boat crossing; Naruto and Yugao disembark at Kiri's misty port. | `ch10.txt:97-105` |
| Naruto | Approximately sixteen, long-haired Naruto in red samurai-like armor with both active Sharingan/Mangekyo eyes, Konoha forehead protector, and Madara's gunbai. He has no ninjato. | `ch10.txt:97, 109-111, 145, 251`; prior-volume weapon continuity |
| Yugao | Alive and physically recovered enough to travel; she chooses to follow Naruto into Kiri rather than return directly to Konoha. | `ch10.txt:97, 101` |
| Kiri | Civil war: Mei's rebels hold this gate-side territory; Yagura's side has numbers, while the rebels are slowly taking ground. | `ch10.txt:127, 183, 187` |
| Naruto's intelligence | Zetsu has already surveyed Kiri and supplied the camp location and rebel leadership. Do not depict Naruto guessing his way through the mist. | `ch10.txt:103, 141, 221` |
| Mei's office | Mei Terumi is **leader of the rebels**, not Mizukage. Yagura is the current Fourth Mizukage and opponent. | `ch10.txt:127, 183, 191, 223` |
| Naruto's motivation | He offers help to test his strength and jutsu, and wants Yagura stopped; this is not a Konoha mission and he does not seek council approval. | `ch10.txt:261-265, 343-355` |

**Continuity in:** v4ch06 ends with Naruto bringing Yugao safely from Wave toward Kiri. Preserve his impassive, deliberate demeanor; preserve the gunbai and the absence of the lost ninjato.

**Continuity out:** Mei has accepted his help provisionally; Naruto has said the Kyubi can be seen within days; Yugao stays in Kiri and her sword remains at Kisara's weapons shop in Wave. The next chapter begins three nights later, with Naruto bored and being watched at the hill outside camp. `ch10.txt:301-303, 363-379, 417-420`

## Reference pack required before page generation

| Reference ID | Must establish | Usage |
|---|---|---|
| `naruto_v4_armor` | Sixteen-year-old Naruto: shoulder-length blond hair, unreadable face, custom Mangekyo, red samurai-like armor, black under-suit, Konoha protector, gunbai; no sword. | Pages 1-14 |
| `naruto_v4_black` | Same sixteen-year-old Naruto in the plain black suit after he removes armor; gunbai absent unless explicitly carried. | Pages 15-18 |
| `yugao_v4` | Adult Leaf kunoichi, subdued palette, recently recovered but mobile; make her face readable in moral reaction shots. | Pages 1-18 |
| `ao_v4` | Adult Kiri rebel commander: eyepatch over the implanted Byakugan; recognisable silhouette and guarded posture. | Pages 6-12, 18 |
| `mei_v4` | Adult rebel leader: ankle-length auburn hair in the source's herringbone/topknot silhouette, green eyes, dark-blue dress over mesh. Keep her dignified and battle-ready; do not frame her as fan service. | Pages 10-18 |
| `env_kiri_mist_gate` | Dense cold mist, wet stone entry gate, low visibility. | Pages 1-8 |
| `env_kiri_rebel_camp` | Improvised occupied camp with a central command tent, damp paths, civilians and guards; hopeful activity under war pressure. | Pages 9-18 |
| `env_mei_tent` | Command tent with desk, chairs, map surfaces, muted lamplight; keep a clear balloon shelf. | Pages 10-15, 18 |

Use generic, visually varied rebel guards for unnamed patrols and camp residents. Do not name or bind individual background guards. Every named body physically present in a page must have its reference bound.

## Page script

Dialogue below is adaptation dialogue: preserve the intent and order, but keep lettering concise. All spoken dialogue must be final before generation. Pages with dialogue require deliberately positioned empty balloons or the project's model-lettering format, according to the active build path.

| Page | Panels / staging | Story and final dialogue | Source anchor |
|---|---|---|---|
| 1 | **One borderless splash.** Kiri port, cold grey sea at lower left, mist swallowing the village. Naruto steps from the boat in red armor, gunbai low at his side; Yugao follows several paces behind, small in the frame. Reserve calm upper third for title. | Title: *KIRI*. No dialogue. Establish that Naruto is entering the war zone by choice, not arriving as a tourist. | `97-99` |
| 2 | **6 panels.** Naruto walks into mist; Yugao follows. Include a small cutaway of water and a silhouette of the boat departing. In the dominant panel, Naruto's armor is heard before he is fully seen; Yugao is foreground, turned toward him, alert. | Yugao (thought/caption): “Kiri is at war.” Naruto: “That is why I came.” Keep the decision to follow as Yugao's, not an order from Naruto. | `97-105` |
| 3 | **7 panels.** Dense mist reduces the environment to flat blue-grey with only wet stones and sound marks. Naruto pauses; close crop of his eye turning right; a distant unnamed Kiri scout is a barely seen silhouette. | Naruto (thought/caption): “Someone is following.” No dialogue from the scout. Build quiet menace without making Naruto surprised. | `105-109` |
| 4 | **6 panels, one dominant horizontal action panel.** The scout lunges; Naruto catches his throat in a foreshortened hand-to-lens shot. Then ram seal, close-up of the scout's eyes taking on Sharingan pattern, Yugao behind at a different depth. | Naruto: “Obey.” Naruto: “Hurt yourself.” Yugao: “Naruto—” The control test begins; do not label it a successful perfect technique. | `109-115` |
| 5 | **5 panels.** Avoid graphic injury: first the scout's refusal in an extreme close-up, then a white impact field with a snapped silhouette/hand releasing, then the body on wet ground in the far background. Main emotional panel is Yugao, face cropped tightly, disturbed. | Yugao: “Was that necessary?” Naruto: “He resisted. The genjutsu is imperfect.” Final silent panel: Yugao walks beside him, not behind him, but looks away. Her moral discomfort is required; do not turn this into flirtation or approval. | `117-125` |
| 6 | **7 panels.** Mist opens on the Kiri gates. Cut to Ao's eyepatch/Byakugan view and the huge, unusual chakra network he sees in Naruto. Patrol forms a depth-staggered defensive cluster, not a line. | Ao: “Two incoming.” Ao: “If they are hostile, I take the armored one.” Use generic guards only. | `127-139` |
| 7 | **6 panels.** At the gate, Naruto and Yugao small below; Ao large foreground, half turned. Hidden guards are only partial shapes at edges. Keep Naruto's headband and Sharingan visible in one reaction panel. | Ao: “State your business.” Naruto: “Take me to your leader.” Ao: “Who are you?” Naruto: “Call me Uchiha Naruto. Or Uzumaki Naruto.” | `141-153` |
| 8 | **7 panels.** Yugao answers while Naruto stays still; Ao's threat changes the temperature. Dominant close-up: Naruto's left eye, then Ao recoils subtly. No fight occurs. | Yugao: “He wants to join your war.” Ao: “If you threaten Mei, I will kill you both.” Naruto: “Threaten her again, and you will not be all right.” Ao: “Follow me.” | `155-179` |
| 9 | **6 panels.** Establish rebel camp from a high angle: irregular tents, children/civilians and guards at different scales, hope amid damp war conditions. Then an intimate depth-staggered walk to the command tent. One small cutaway: rebel hands repairing gear. | Minimal dialogue. Caption: “The rebels held the gate side of Kiri.” Naruto's private observation can be a short caption: “They still believe they can win.” Do not make the whole camp a bloodline-only population. | `181-189` |
| 10 | **6 panels.** Inside Mei's tent before the visitors enter. Mei at her desk, Ao at a lower/foreground angle, command maps between them. She responds to his warning as an equal leader, not a passive protected figure. | Ao: “A Konoha shinobi asks for you. I do not trust him.” Mei: “Bring them in.” | `191-215` |
| 11 | **7 panels.** Mei enters foreground with a professional greeting; Naruto and Yugao remain in doorway depth. Use a handshake as the dominant panel: their hands at lower center, their eyes visible at different scales. Do not sexualize the encounter. | Naruto: “Mei Terumi. Dual bloodline holder. Rebel leader.” Mei: “And you are?” Naruto: “Naruto. Uzumaki or Uchiha.” Mei: “Then, Uchiha Uzumaki Naruto.” | `217-235` |
| 12 | **6 panels.** Mei sends Yugao with Ao to see the camp. Yugao's hesitation is protective concern for Naruto, not jealousy. Naruto gives her a blank, self-possessed look. Last panel: gunbai unstrapped beside Naruto's chair in Mei's tent. | Mei: “Ao, show Yugao the camp.” Yugao: “...” Naruto: “Go.” Mei: “Why are you here?” Naruto: “I am offering my services.” | `239-257` |
| 13 | **7 panels.** Conversation must move through visual beats: Naruto small beyond the desk; Mei's intent close-up; a cutaway of war map and Yagura's symbol; Naruto's thin smile only once. Use a broad central panel, smaller reactions beneath. | Mei: “Did Konoha send you?” Naruto: “The Hokage does not know I am here.” Naruto: “I came to test my strength and my jutsu. Yagura must be stopped.” Mei: “One person changes nothing.” Naruto: “Numbers are not the point. Quality is.” | `259-283` |
| 14 | **5 panels.** Use close framing and negative space for the private reveal. Mei leans toward Naruto; he speaks close enough that the balloon can be small and correctly assigned. Reaction is Mei's widened eye, then an empty storm-dark exterior cutaway. | Naruto: “I can bring the Kyubi against Yagura's forces.” Mei: “The Kyubi was sealed.” Naruto: “Not anymore. You will see it in days.” Mei: “Then I will take your help.” This is a promise, not the Kyubi's appearance. | `287-303` |
| 15 | **6 panels.** Transition through camp: Mei leads Naruto to a tent, rebels look on from uneven depths. Naruto is still armored in the first two panels, then remove armor off-panel; final panel has him alone in black under-suit, gunbai not in hand. | Mei: “We discuss terms tomorrow.” Naruto: “Separate tents.” Keep Mei's light interest only as a brief tonal contrast; it must not consume the page or change Naruto's unreadable response. | `305-327` |
| 16 | **7 panels.** Yugao enters Naruto's tent. Stage them cautiously: Naruto low on bed in far background, Yugao foreground/back-to-camera cropped, then a separate close-up for each. No intimate pose. Make the council discussion a visual comparison: small inset of Konoha council chamber / an empty Hokage silhouette, clearly a memory-image, not a new current scene. | Yugao: “Konoha refused the rebels before.” Naruto: “That makes this easier.” Yugao: “You do not fear the elders?” Naruto: “They cannot control me. If banished, I leave—and return when they are gone.” | `323-357` |
| 17 | **6 panels.** Slow, quiet close: rain/mist outside tent; Yugao asks duration and then about her sword. Insert an empty object panel of a sheathed sword at a Wave weapons-shop counter, labelled only by visual context—no readable sign. Naruto remains flat, Yugao visibly relieved. | Naruto: “Two or three weeks.” Yugao: “Will you return to Konoha?” Naruto: “Not yet.” Yugao: “My sword?” Naruto: “At Kisara's weapons shop in Wave. You can reclaim it when you return.” Yugao: “Thank you.” | `361-381` |
| 18 | **6 panels.** Parallel aftermath: Naruto alone in a small black/blue quiet panel, bored by a camp that has no peace; Mei and Ao in her tent in the dominant panel, with Ao's guarded posture and Mei's considered resolve. Final panel is the command-tent lamp in wet night, not the hill. | Ao: “The woman is honest. Naruto brought her here after saving her.” Mei: “Then accepting him was right.” Keep Yagura as the looming off-panel force; do not introduce Chojuro or the hill yet. | `383-415` |

## Builder constraints

- Use six to nine panels for most pages; pages 1 and 14 may be more spacious because they carry the location and the Kyubi reveal.
- Every two-person conversation must use depth staggering: one character cropped in foreground, the other smaller or turned away. Do not place Naruto, Yugao, Ao, or Mei in a flat row.
- Kiri's palette is cold mist blue, wet stone grey, desaturated green, and warm command-tent amber. Naruto's red armor is the deliberate recurring accent.
- Page 5's death is consequence and moral fracture, not spectacle. Use a cutaway/body silhouette rather than a graphic neck injury.
- Yagura never appears in person. Treat him as pressure in maps, guard behavior, and the Kyubi conversation only.
- Do not write readable camp signs, maps, or shop lettering. Use illegible marks where needed.

## Manual review gate

Review in sequence before lettering/export. A failed gate means regenerate the affected page before advancing.

| Gate | Check | Pass condition |
|---|---|---|
| Source order | Compare pages 1-18 against the source anchors above. | Port → mist follower → control-test killing → gate/Ao → camp → Mei offer/Kyubi promise → first-night Yugao conversation → Mei/Ao aftermath. No hill material. |
| Character logic | Read every balloon and silent reaction as a first-time reader. | Yugao clearly disapproves of the killing; Ao is cautious; Mei is a leader evaluating a weapon; Naruto is testing limits, not aiding Konoha. |
| Identity | Inspect every named face, eye, weapon, and outfit. | Naruto's sixteen-year-old armor/black-suit transition is correct; gunbai remains; no ninjato; Ao's eyepatch/Byakugan and Mei's auburn silhouette remain distinct. |
| Political clarity | Read pages 6-14 without source notes. | A reader understands Yagura is current Mizukage, Mei leads rebels, the rebels need help, and Naruto acts without Konoha authorization. |
| Dialogue | Inspect balloon count, tail, position, spelling, and reading order page by page. | Every line points to the intended speaker; no invented text; no balloon overlaps a face; no long unbreakable token. |
| Visual staging | Inspect each rendered page at full-page and panel scale. | One dominant panel per page, depth-staggered groups, purposeful empty space, cold Kiri palette, no centered lineup, no painterly drift. |
| End hook | Read page 18 then the planned first page of v4ch08. | Mei's acceptance and Naruto's unease create anticipation; the next chapter can cleanly jump to three nights later. |

## Known clarity risks

| Risk | Required treatment |
|---|---|
| Mei incorrectly read as Mizukage | Call her “rebel leader” in script metadata and dialogue context; reserve “Mizukage” for Yagura. |
| Naruto's violence read as heroic | Hold on Yugao's discomfort and his technical, emotionless explanation. Do not give him a triumphant action pose after the kill. |
| Naruto's help read as loyalty to Konoha | State that the Hokage does not know he is there and that his goal is self-testing. |
| Kyubi claim mistaken for immediate battle | End the reveal with a promise that Mei accepts; do not draw the Kyubi in this chapter. |
| Yugao's camp stay made ambiguous | Explicitly state she chooses to stay, expects two or three weeks in Kiri, and will recover her sword at Wave when returning to Konoha. |
