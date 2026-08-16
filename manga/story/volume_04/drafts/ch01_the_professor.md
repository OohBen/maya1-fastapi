# Volume 4, Chapter 1 — "The Professor"

**16 pages** · **Source:** fic ch8, `manga/.source/uchiha-naruto-the-sage/ch08.txt:5-93`; handoff at `:95-101`.

**Cast:** Naruto (13), Jiraiya, Homura, Koharu, Orochimaru, Kabuto; Konoha mourners and ANBU are unnamed silhouettes.

**Locations:** storm-dark Konoha rooftops, Hokage office, Orochimaru's dim laboratory/hideout, Naruto's apartment exterior/interior.

**Source coverage:** Konoha's costly victory and public mourning (`:5-14`); Naruto's absence, private view of Hiruzen's death, and concern about Danzō (`:15-21`); the elders' offer to Jiraiya, his refusal, Tsunade plan, two-week deadline, and proposal to take Naruto (`:23-65`); the elders' decision to tail him (`:67-69`); Orochimaru's failing vessel and order to investigate Naruto's blood (`:71-93`). The closing handoff uses the immediately following apartment setup (`:95-101`) without adapting Sasuke's conversation yet.

## Chapter engine

Konoha calls Hiruzen irreplaceable; Naruto treats his death as the removal of a political buffer. In parallel, the adults who think they can contain him make plans around him, while Orochimaru converts Naruto's revealed Mangekyō into a new investigation. The emotional line is **public grief versus private calculation**: Naruto is not loudly cruel or triumphant; he is alone, quiet, and already moving past the village's loss.

The chapter must not imply that Naruto accepts Jiraiya's trip. Jiraiya only obtains permission to propose the trip; Naruto's refusal belongs in the next chapter. Do not depict a funeral itself: the source establishes that burial has occurred before the office scene and that Naruto did not attend (`ch08.txt:15,25`).

## Continuity

| State | Requirement |
|---|---|
| In | Volume 3 ends with Naruto returning to Konoha after the invasion; Hiruzen dies in that invasion. Naruto's Mangekyō was publicly seen, and he has no ninjato. Use `naruto_13`, never `naruto_13_sword`. |
| Through | Naruto's concern is freedom of movement if Danzō becomes Hokage, not grief. Jiraiya does not become Hokage; he sets out to recruit Tsunade within two weeks. Orochimaru does not yet possess Sasuke and urgently needs another vessel. |
| Out | Naruto is in his orderly, guarded apartment deciding his next move. The next chapter opens with Sasuke at his door (`ch08.txt:95-101`). Do not show Sasuke before that opening beat. |

## Reference requirements

| Ref | Use | Status / constraint |
|---|---|---|
| `naruto_13` | Pages 3–4, 16 | Existing. Shoulder-length blond hair, black clothing/red swirl; public Mangekyō is available but should appear only as a small visual reminder, not a power display. |
| `hiruzen` | Pages 1–2, 12 | Existing. Use only as a memorial image/silhouette in the Konoha sequence; page 12 is a brief past-failure plate. |
| `jiraiya` | Pages 5–8 | Existing. He is burdened and practical, never comic-relief here. |
| `orochimaru`, `kabuto` | Pages 9–14 | Existing. Orochimaru is physically failing; Kabuto is an attentive subordinate. |
| `danzo`, `zetsu` | Page 4 | Existing. They appear only as a political-threat image: Danzō's possible accession and Zetsu as Naruto's unshown answer. Do not stage an assassination. |
| `env_hokage_office` | Pages 5–8 | Existing. Strip it of warmth; broken village rooflines and rain belong outside its windows. |
| `env_apartment_ext`, `env_apartment_int` | Page 16 | Existing. Cold single-bulb apartment lighting per series bible. |
| `homura`, `koharu` | Pages 5–8 | New character refs required before generation. The source names them but does not describe their appearance; encode the approved established design rather than inventing physical traits in the page prompt. |
| `itachi` | Page 12 | New character ref required before generation. He appears only in one shadow-memory plate to represent Orochimaru's past miscalculation. |
| `env_konoha_after_invasion`, `env_orochimaru_lab` | Pages 1–4, 9–14 | New environment refs required. Keep Konoha damaged but standing; keep Orochimaru's room clinical, cramped, and dim. |

## Page-by-page script

Dialogue below is for the lettering pass. It is concise adaptation dialogue, not source text to send to the image model. All dialogue balloons remain empty during art generation.

| Pg | Panels | Staging / camera and story beat | Dialogue / captions | Refs | Tier |
|---|---:|---|---|---|---|
| **1** | Splash | Borderless vertical opener. High view across Konoha under low slate clouds: broken roofs, repair crews as tiny silhouettes, damp streets, memorial cloths. No protagonist. Keep the upper third quiet for title lettering. The village stands, but the frame should feel drained rather than victorious. | Caption: “Konoha survived.” Small second caption: “It still paid.” | `env_konoha_after_invasion` | high |
| 2 | 5 | Uneven page: a large wide panel shows a mourning crowd moving toward a distant memorial; foreground umbrellas and shoulders crop the view. Small inserts: a cracked Hokage monument detail; incense smoke; Hiruzen's framed portrait; an empty seat beneath the portrait. Do not stage a burial ceremony. | Caption: “The Third Hokage was gone.” | `hiruzen`, `env_konoha_after_invasion` | medium |
| 3 | 4 | Cut away from the crowd. Naruto sits very small on his apartment roof, back three-quarters to camera, knees raised; the distant mourners are barely visible below. Then a flat-black close-up of his blank eye, then a still-life of rain on roof tile. Make the absence from the funeral legible through distance, not a spoken explanation. | Caption: “Naruto did not go.” Off-panel crowd murmur, indistinct. | `naruto_13`, `env_apartment_ext` | medium |
| 4 | 5 | Interior-thought page with flat black and cold blue backgrounds: Naruto's face cropped by the right edge; Hiruzen's portrait dissolving into a chess-piece-like Hokage hat; a small inset of Danzō's empty chair and Zetsu's split black-and-white profile half-submerged in shadow, a contingency rather than an action; Naruto's fist loosens. End on Naruto looking toward the village from above. | Captions: “A shield had been removed.” / “If someone else set the rules, he would break them himself.” | `naruto_13`, `hiruzen`, `danzo`, `zetsu`, `env_apartment_ext` | medium |
| 5 | 5 | Establish the Hokage office after the burial. Wide dominant panel from behind the two elders: Jiraiya is small by the rain-streaked window, the vacant Hokage desk between them. Inserts of a hand on the desk, Jiraiya's tired eye, and the office door closed behind him. Keep all three at staggered depths. | HOMURA: “The village needs a leader.” JIRAIYA: “I know why you called.” | `jiraiya`, `homura`, `koharu`, `env_hokage_office` | medium |
| 6 | 6 | Conversation as pressure, not a lineup: Koharu's cropped shoulder dominates foreground; Jiraiya sits distant by the window; Homura seen only in reflection. Small panels isolate Jiraiya's mouth, a file marked only with an illegible seal, and his hand refusing the Hokage hat. | JIRAIYA: “I cannot take the title.” KOHARU: “You are the strongest one left.” JIRAIYA: “Strength is not the job.” | `jiraiya`, `homura`, `koharu`, `env_hokage_office` | medium |
| **7** | 4 | Dominant wide panel: Jiraiya turned away from the elders, his silhouette facing the ruined village through the office window. Three narrow reaction panels: elder eyes, Jiraiya's profile, a blank white panel holding the name before it lands. | JIRAIYA: “There is another Sannin.” KOHARU: “Tsunade?” JIRAIYA: “Give me two weeks.” | `jiraiya`, `homura`, `koharu`, `env_hokage_office` | medium |
| 8 | 6 | The negotiations tighten. Use a letterbox of the elders framed across the vacant desk; then Jiraiya exiting through the window in a diagonal panel. A low-angle inset of the two elders left behind. Keep Naruto absent: this is adults assigning him a role without him. | KOHARU: “Bring her back, or take the office.” JIRAIYA: “No ANBU. I will take Naruto.” HOMURA: “He must answer for what he revealed.” | `jiraiya`, `homura`, `koharu`, `env_hokage_office` | medium |
| 9 | 4 | After Jiraiya leaves, the office goes still. The dominant panel is an ANBU silhouette reflected in the wet window, deliberately distant and unreadable. A small panel shows Homura and Koharu exchanging a guarded look over the desk. | KOHARU: “Put eyes on them.” HOMURA: “Even with Jiraiya?” KOHARU: “Especially then.” | `homura`, `koharu`, `env_hokage_office` | low |
| **10** | 3 | Hard location cut. Near-black Orochimaru hideout: a single wide panel of Orochimaru seated low beside a metal tray, his body slack and his silhouette swallowed by darkness. Two small body-detail inserts—trembling hand, medicine glass—convey failure without graphic transformation. | Caption: “Elsewhere.” OROCHIMARU: “This vessel is failing.” | `orochimaru`, `env_orochimaru_lab` | medium |
| 11 | 6 | Kabuto enters from the foreground, cropped to glasses and tray; Orochimaru is small and deep in the room. Insert a discarded empty chair/bed to suggest time running out, then a close-up of Orochimaru's narrowed eye. Do not add Sasuke: the source says he is unavailable, not present. | KABUTO: “How soon?” OROCHIMARU: “Soon enough that I need another body.” | `orochimaru`, `kabuto`, `env_orochimaru_lab` | medium |
| 12 | 5 | Intercut memory as graphic plates: a one-panel shadow of Itachi overpowering Orochimaru, then Hiruzen's sealing silhouette, then back to Orochimaru's current hand crushing a tablet. Keep these as impressionistic reminders of past underestimation; no extra fight sequence. | OROCHIMARU: “I have misjudged opponents before.” Caption: “He would not repeat it.” | `orochimaru`, `hiruzen`, `env_orochimaru_lab` | medium |
| 13 | 5 | Kabuto presents a labeled-but-illegible sample vial in extreme foreground; Orochimaru sits distant. Then an abstract close-up of Naruto's six-bladed Mangekyō eye against black, with the vial reflected in it. It visually joins the village's fear to Orochimaru's curiosity. | KABUTO: “The sample was preserved.” OROCHIMARU: “Then study it.” | `orochimaru`, `kabuto`, `naruto_13`, `env_orochimaru_lab` | medium |
| 14 | 4 | The conclusion of the laboratory scene. Orochimaru's profile nearly fills a tall panel; Kabuto is turned away in the far background leaving with the vial. The final panel is Orochimaru alone in the dark, eyes open. Keep the question scientific and predatory, not an exposition dump. | OROCHIMARU: “His eyes are not borrowed.” OROCHIMARU: “Find the bloodline beneath them.” | `orochimaru`, `kabuto`, `env_orochimaru_lab` | medium |
| 15 | 3 | Silent transition back to Naruto. Exterior apartment at blue-grey evening: one lit window in an otherwise dark building; then an interior wide with Naruto seated at the table, orderly room, back to camera. A final small panel shows his eyes tracking an approaching chakra presence off-panel. | Caption: “Naruto had plans of his own.” | `naruto_13`, `env_apartment_ext`, `env_apartment_int` | low |
| **16** | 4 | Cold, controlled final page. Naruto rises in profile from the table; a close-up of the apartment-door lock and barrier seal; final dominant panel from inside the hall: Naruto opens the door only a fraction, his face in foreground, a dark-haired adolescent silhouette cropped beyond the threshold with no face shown. This is the handoff, not the conversation. | No dialogue. | `naruto_13`, `env_apartment_int` | medium |

## Final-page hook

The last page promises a confrontation about the Uchiha connection without consuming it. The visitor must remain an unbound, face-hidden silhouette so that the next chapter can introduce and bind Sasuke correctly. Do not call him Sasuke in the art prompt or lettering on this page.

## Reader-clarity risks

| Risk | Required treatment |
|---|---|
| Readers may assume Naruto mourns Hiruzen because the town does. | Page 3 must make Naruto's physical absence and emotional distance unmistakable before page 4's political calculation. |
| Jiraiya's Tsunade mission can read as Naruto accepting an escort. | Pages 7–9 must say only that Jiraiya asks to take Naruto and the elders authorize surveillance. Naruto is not consulted in this chapter. |
| Orochimaru's scene can feel unrelated. | Repeat the visual bridge: Naruto's public Mangekyō eye on page 13 and the blood vial. It establishes the next threat without explaining the whole secret. |
| The final silhouette can be mistaken for Jiraiya or an ANBU. | Give the visitor a short, dark-haired adolescent outline and reserve Jiraiya/ANBU visual markers for prior pages. Do not reveal the visitor's face until the next chapter. |
| Funeral imagery can accidentally contradict the source. | Show communal mourning and the aftermath only; neither Naruto nor the reader witnesses an on-page funeral. |

## Manual QA before generation

- [ ] Read source `ch08.txt:5-93` against the page table: every listed beat is present, and no funeral scene, Naruto/Jiraiya departure, Tsunade arrival, or Sasuke conversation has been pulled forward.
- [ ] Read the lettered dialogue in page order. The causal sequence must be: invasion aftermath → Naruto's reaction → leadership vacancy → Jiraiya's plan → surveillance decision → Orochimaru's investigation → visitor arrives.
- [ ] Verify Naruto is bound as `naruto_13` on every page he appears; he carries no sword and does not wear an orange canon outfit.
- [ ] Verify each named visible character has its own reference. If `homura`, `koharu`, `itachi`, or either new environment ref is not built, stop before page generation rather than substituting another elder, room, or face.
- [ ] Inspect page 2 and page 3 side by side: page 2 belongs to the grieving village; page 3 isolates Naruto. The contrast must read with dialogue removed.
- [ ] Inspect pages 5–9 for staging: no three adults posed in a row; use depth staggering, cropped foregrounds, and balloon shelves.
- [ ] Inspect pages 10–14 for a clean location break and for non-graphic illness staging. Kabuto leaves with the sample; Sasuke never appears.
- [ ] Inspect page 16 at thumbnail size: Naruto, door, and a clearly adolescent dark-haired visitor silhouette must read in that order. No visible face, name, or dialogue.
- [ ] Confirm every generated dialogue balloon is empty before deterministic lettering, and check the final lettered pages for speaker order, spelling, and tails.
