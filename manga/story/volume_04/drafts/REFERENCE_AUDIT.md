# Volume 4 visual-reference audit

**Finding:** the existing library covers the early-Konoha cast, but the post-time-skip Naruto, Kiri cast, transformations, and nearly every Volume 4-specific location need purpose-built references before those pages are generated.

**Scope checked:** source chapters 8–11 in the local source cache; the current source-grounded Volume 4 drafts; `manga/refs/images/`; `manga/refs/build_refs.py`; and `manga/chapters/prompts.py` / `manga/runner.py`. This is a planning ledger, not a generation request.

## Verified constraints

- `R(...)` resolves each ordered asset key to `manga/refs/images/<key>.png` (`manga/chapters/prompts.py:16-17`). Page prompt order is therefore the reference order.
- The runner appends one style image after the page references (`manga/runner.py:35`), and `build_page` sends the supplied references plus that style candidate (`manga/genlib.py:283`).
- The repository has no checked cap on the number of references. Treat a **16-image total** as a working native-tool limit until it is independently retested; that leaves at most **15 `R(...)` images** when a style image is present. This limit is not verified by the repository code.
- `naruto_13_sword.png` depicts the earlier 13-year-old sword state, while ch9 introduces an older Naruto with a new sash sword (`manga/.source/uchiha-naruto-the-sage/ch09.txt:15-16`). It must not stand in for the post-skip state.
- The existing `gunbai.png` has a purple face and three tomoe; ch9 specifies Naruto's later gunbai uses the Uzumaki swirl and Uchiha crest instead (`ch09.txt:15-16`). It is not a correct close-up reference for Volume 4's later weapon.

## Ordered-reference convention

1. Character or creature sheets in the order their bindings appear in the prompt.
2. A dedicated prop/form sheet only when a close-up or transformation needs it; do not attach a redundant prop if it is already clear on the character sheet.
3. One location plate.
4. The runner's style reference is appended automatically.

Every new sheet below should be a three-view white-background turnaround unless it is an environment, creature/form, or prop plate. Each character description begins with the silhouette that must survive at thumbnail size. Source gives no physical design for several named people; those specifications are proposed art direction and require one review approval before the first reference batch.

## Characters

| Character | Volume 4 use | Existing reference | New-sheet requirement / silhouette-first spec | Required state variants |
|---|---|---|---|---|
| Naruto, 13 | ch1–4, ch8 aftermath / Konoha and hideout scenes | Yes — `manga/refs/images/naruto_13.png` | None for the base state. Bind the existing long-haired black outfit; do not use the old sword sheet merely to add a weapon. | Blue eye; custom Mangekyō close-up may use `mangekyo_design.png`. No sword. |
| Naruto, post-skip | ch5–11; Oto, Wave, Kiri | No | **New `naruto_v4_armor`**: taller post-skip silhouette, below-shoulder blond hair framing the face and hiding the right eye; bright red segmented samurai-like plates over a black suit; partly obscured Leaf protector; black gloves and boots; custom gunbai carried on back. His approximately-sixteen age is an inference from the stated elapsed time, not a source-stated age. | `naruto_v4_armor`; `naruto_v4_armor_sword` with the new plain sash sword; `naruto_v4_black` without armour for late ch10 camp scenes. One shared face/hair/eye design across all three. |
| Hiruzen | ch1 memorial / aftermath only | Yes — `manga/refs/images/hiruzen.png` | No new sheet. He is dead; use portrait, memorial, or recalled silhouette only. | Never present as a living participant. |
| Jiraiya | ch1–4; ch5 training report | Yes — `manga/refs/images/jiraiya.png` | No new base sheet. White mane, red facial marks, scroll remain the quick read. | Travel / training dust can be prompt state, not a sheet. |
| Homura | ch1, ch4 council | No | **New `homura`**: elderly narrow male adviser, rectangular silhouette through a dark formal robe and squared cap/forehead line; reserved posture. The source names him but does not specify appearance. | Council seated only. |
| Koharu | ch1, ch4 council | No | **New `koharu`**: elderly compact female adviser, pale hair in a severe swept-back bun and layered formal robe; recognisable smaller silhouette against Homura. Source gives no physical design. | Council seated only. |
| Tsunade | ch4 Konoha installation / office | No | **New `tsunade`**: tall adult woman with blonde twin tails, diamond forehead mark, green haori over grey wrap top; strong squared stance, not a fan-service pose. | Hokage hat/office variant can be prompted; no separate sheet needed. |
| Shizune | ch4 | No | **New `shizune`**: slight adult attendant, straight dark hair with a single high ponytail, dark kimono-style medical aide outfit; clipboard/stacked files as recognisable office prop. Source does not detail the design. | Office only. |
| Shikamaru | ch4 promotion | Yes — `manga/refs/images/shikamaru.png` | No new sheet; he is still in the pre-skip chapter. | Chūnin vest is an optional prompt-state only. |
| Shikaku | ch4 council | No | **New `shikaku`**: adult Nara man with dark hair tied high in a longer pineapple tail, green jōnin vest, composed slouched posture. Source identifies him as the political reader; visual spec needs approval. | Council seated. |
| Tsume | ch4 council | No | **New `tsume`** if she remains named and visible: adult Inuzuka woman, wild brown hair and red fang cheek marks, assertive forward lean. If adapted as an unnamed clan-head silhouette, no named sheet is needed. | Council seated. |
| Hiashi | ch4 council | No | **New `hiashi`** if named/visible: long dark hair, pale Byakugan eyes, high-collared pale clan robes, upright formal silhouette. If only a distant unnamed pale-eyed clan-head, keep generic. | Council seated. |
| Danzō | ch1–5 / council threat | Yes — `manga/refs/images/danzo.png` | No new sheet; keep bandaged arm, covered right eye, cane. | Seated council and dark cutaway state. |
| Kakashi | ch4 transition; ch5 training; possible report | Yes — `manga/refs/images/kakashi.png` | No new base sheet. | `kakashi_16` is optional only if the time-skip training page needs an older, travel-worn body scale; do not mix the child-scale Sasuke sheet beside an older Naruto. |
| Sasuke | ch2–3, ch4 transition, ch5 training | Yes — `manga/refs/images/sasuke.png` | Early ch8 uses existing adolescent sheet. **New `sasuke_16`** for the ch9 time-skip training insert: taller teen, same hair/crest lineage, mature proportions. | `sasuke` (age 13); `sasuke_16` (post-skip). |
| Sakura | ch4 future-training handoff only | Yes — `manga/refs/images/sakura.png` | No new sheet unless the plan expands her beyond a brief, pre-skip handoff. | Existing age-13 state only. |
| Orochimaru | ch1 lab; ch5 Oto fight | Yes — `manga/refs/images/orochimaru.png` | No new base sheet. | Failing-vessel / scorched-regenerating states are prompt treatment; use a separate Kusanagi prop only for close combat. |
| Kabuto | ch1 lab; ch5 Oto fight | Yes — `manga/refs/images/kabuto.png` | No new base sheet. | Glasses must stay present; damage/regeneration is prompt state. |
| Zetsu | ch4 hideout; ch5, ch7–11 intelligence scenes | Yes — `manga/refs/images/zetsu.png` | No new sheet. | Ground-emergence and shadow-only states are prompt treatment. |
| Itachi | ch3 | No | **New `itachi`**: adult Uchiha, long black hair framing a narrow face, high Akatsuki collar and black cloak with red clouds; exterior straw hat; a distinct red Mangekyō eye. | Hat-on exterior; hat-off Naka Shrine. |
| Kisame | ch3 separation only | No | **New `kisame`**: very tall blue-grey adult with shark-like face, black/red-cloud cloak and huge bandage-wrapped Samehada dominating the back silhouette. | Exterior/straw-hat state only; he never enters Naka Shrine in this volume. |
| Kurama / Kyūbi | ch2 inner seal; ch11 external summoning | No | **New `kurama`**: enormous nine-tailed orange fox, red slit eyes, heavy muzzle and paws; scale must dwarf Naruto. Avoid a humanized face. | `kurama_inner` behind the seal gate (eyes/muzzle/paws in shadow); `kurama_full` for the exterior summoning. |
| Karin | ch5 aftermath / extraction | No | **New `karin`**: slim red-haired Uzumaki girl with rectangular glasses, red hair as the silhouette anchor, guarded posture. Source gives no exact outfit in this chapter; choose one review-approved Oto-captive outfit. | Captive, then travelling-with-Zetsu state only if both are on-page. |
| Yugao | ch6–11 | Yes — `manga/refs/images/yugao.png` | Existing sheet covers identity, but **new `yugao_v4` is recommended**: same purple-haired Leaf kunoichi with travel-worn/recovered state and readable moral-reaction expressions. | Injured/recovering boat state; recovered Kiri observer state. |
| Ao | ch7–11 | No | **New `ao_v4`**: broad adult Kiri commander, dark wrap/vest and an eyepatch framing his implanted Byakugan; guarded crossed-arm stance. | Mist-gate / camp observer. |
| Mei | ch7–11 | No | **New `mei_v4`**: tall adult rebel leader, long auburn hair in a high braided/topknot silhouette, green eyes, dark blue dress over mesh; dignified command posture. She is not yet Mizukage. | Camp command; hill conversation; distant battle observer. |
| Chōjūrō | ch7–11 | No | **New `chojuro_v4`**: slim younger Kiri swordsman, shaggy pale-blue hair, oversized wrapped sword / broad back silhouette, visibly deferential posture. Source names him but gives no design. | Camp and Mei bodyguard only. |
| Yagura | ch10–11 | No | **New `yagura_human`**: short adult Mizukage, compact silhouette, dark clothing, long hooked staff / coral-club silhouette if retained after design approval. Source's fight requires a clearly human baseline before transformations. | Human, injured human, and distant crater aftermath. |
| Tamashi | ch11 command-tent objection | No | **Conditional `tamashi`**: only create if the adaptation keeps his name and face. Source gives no physical design; a distinct adult rebel-adviser silhouette is required if named. Otherwise make him an unnamed rebel adviser. | Tent meeting only. |
| Madara | ch3 tablet-memory; ch4 eye vault context only | Yes — `manga/refs/images/madara.png` | No new sheet. Keep him a memory/shadow, not a revived on-page participant. | Ancient hideout silhouette only. |

### Named but non-visual unless a later page deliberately adds a source-grounded recollection

| Name | Volume 4 source use | Existing reference | Reference decision |
|---|---|---|---|
| Minato and Kushina | Parentage is discussed by Jiraiya/Naruto; neither appears in the planned adaptation. | Yes — `manga/refs/images/minato_kushina.png` | Do not attach or show them without an approved recollection page; a portrait would imply a scene the source does not stage. |
| Nagato | Mentioned only in Naruto's EMS/Rinnegan reasoning. | No | No sheet needed; do not visualize him in the eye-vault scene. |
| Hashirama | Mentioned in DNA, Wood Release, and Naruto's post-bijuudama comparison. | No | No sheet needed; use an abstract thought insert or narration, not a flashback. |
| Tobi | Named only as an off-page Uchiha in Naruto/Itachi's information exchange. | No | No sheet needed; do not add him to Naka Shrine. |
| Kisara | Named as the Wave weapons-shop keeper holding Yugao's sword; not a planned on-page scene. | No | No sheet unless the Wave shop is explicitly adapted; otherwise keep the sword-storage fact in dialogue/caption only. |

## Creatures, forms, and important props

| Asset / subject | Volume 4 use | Existing reference | New-sheet requirement / silhouette-first spec | State variants |
|---|---|---|---|---|
| Custom Mangekyō / EMS eye | ch3–5, ch10–11 | Yes — `manga/refs/images/mangekyo_design.png` | Existing six-blade graphic eye may be used. Source names the later eyes EMS but does not specify a new visual pattern; do not invent a different pattern without approval. | Active red / inactive blue is prompt colour-state. |
| Post-skip gunbai | ch5, ch7, ch10–11 | Existing `manga/refs/images/gunbai.png` is not source-accurate | **New `gunbai_v4`**: large dark-purple war fan with a bandaged handle and chain; face bears an Uzumaki spiral and Uchiha crest rather than three tomoe. It should also appear on the Naruto sheets. | Back carry; hand-held barrier; cane after depletion. |
| New sash sword | ch5 and ch10–11 | No correct state | **New `naruto_v4_sword`** only if a close-up is needed; otherwise include it in `naruto_v4_armor_sword`. Plain straight blade, dark sash sheath, no claim it is the Volume 3 ninjato. | Sheathed; wind-chakra reinforced. |
| Kusanagi | ch5 duel | No | **Conditional `kusanagi`**: long pale straight blade associated with Orochimaru, made as a prop plate only if blade-lock close-ups fail with Orochimaru's sheet. | Blade lock / oral emergence should stay non-graphic. |
| Manda | ch5 climax | Existing `manga/refs/images/giant_snake.png` is a generic brown snake, not Manda | **New `manda`**: colossal purple-grey serpent with horned/browed head and dark scale pattern; head and coils must be readable against destroyed terrain. | Coiled / rearing / retreating-under-black-flame. |
| Orange Susano'o, partial | ch5 underground collapse | No | **New `susanoo_orange_ribcage`**: opaque orange skeletal rib cage around Naruto, heavy black contour, no finished humanoid body. | Only ch5 early defence. |
| Orange Susano'o, final | ch5 and ch10–11 | No | **New `susanoo_orange_final`**: giant opaque orange armoured humanoid, horned head and two broad blade forms; maintain visible ground and fighters through the composition. | Twin/fused-blade battle state; charged orange bomb state. |
| Yagura three-tail cloak | ch10 | No | **New `yagura_sanbi_cloak`**: human-sized crimson chakra silhouette with exactly three tails and demonic eyes; no turtle shell. | Cloak only; then remove before full beast. |
| Full Three-Tails / Sanbi | ch10–11 | No | **New `sanbi_full`**: massive three-tailed turtle, heavy shell/body and three visible tails, dark/crimson-accented chakra; distinct from Kurama and Susano'o. | Standing in crater; forming first/second bijūdama. |
| Bijūdama | ch11 | No | **New `bijuudama` optional**: dense dark spherical mass with tight high-contrast edge, not a glowing fireball. Use only if the full-Sanbi sheet cannot carry the charge clearly. | Charging / in-flight / interrupted. |
| Wood Release techniques | ch10–11 | No | **New `mokuton_stakes_serpent`**: angular pale wood spikes and a single coiling wooden serpent that reads as a restraint, not a living snake. **New `wood_locking_wall`**: curved timber dome built from opposing pillars. | Tail pinning / chakra drain; intact dome / shattered debris. |
| Shinigami mask | ch5 objective | No verified on-page visual requirement | **Conditional `shinigami_mask`**: create only if a page shows it. The ch5 draft keeps the objective and failed search, so do not fabricate a mask reveal solely to justify a sheet. | Unused unless visually shown. |
| Blood vial / preserved sample | ch1 lab | No | No sheet needed; a generic unlabeled vial is sufficient. Keep label unreadable. | Lab close-up only. |
| Chūnin vests / office papers / sake | ch4 | No | No sheet needed; use generic props and illegible papers. | Do not use readable text. |

## Environments

| Environment | Volume 4 use | Existing reference | New-sheet requirement / silhouette-first spec | State variants |
|---|---|---|---|---|
| Post-invasion Konoha | ch1 | No direct match | **New `env_konoha_after_invasion`**: intact village skyline under rain/low cloud, a few broken roofs and repair scaffolds; mourning cloths but no staged funeral. | Rooftop / street / memorial distance. |
| Hiruzen mourning / burial aftermath | ch1 | Partial — `manga/refs/images/env_burial.png` | Existing plate may support distant mourning only after visual check. Do not show a funeral ceremony; source places the burial before the elders' scene. | Memorial crowd / portrait insert. |
| Hokage office | ch1, ch4 | Yes — `manga/refs/images/env_hokage_office.png` | Reuse. Prompt rain, a vacant desk, papers, or Tsunade's workload as needed. | Vacant-Hokage / Tsunade office. |
| Naruto apartment | ch1–2 | Yes — `manga/refs/images/env_apartment_int.png`, `manga/refs/images/env_apartment_ext.png` | Reuse. Keep cold, orderly, and defensive rather than cosy. | Day / single-bulb night. |
| Council chamber | ch4 | No | **New `env_konoha_council_chamber`**: long irregular council table/ring, raised Hokage chair, layers for depth; avoid a courtroom lineup. | Full chamber / tight table edge. |
| Uchiha compound | ch3 | No | **New `env_uchiha_compound`**: intact empty traditional clan street and gate; no ruins, bodies, or fire. | Exterior gate / interior lane. |
| Naka Shrine | ch3 | No | **New `env_naka_shrine`**: sealed cool-stone ancestral chamber, central Uchiha tablet, few pillars, hard narrow overhead light; must not look like a generic cave. | Approach / tablet chamber. |
| Inner-seal sewer | ch2 | No | **New `env_inner_sewer`**: vast wet brick channel, black vanishing depth, immense barred gate, centered seal paper; Naruto is tiny against it. | Empty depth / Kurama eye-light behind gate. |
| Madara hideout / eye vault | ch4–5 | Partial — `env_hideout_training.png`, `env_hideout_tablets.png`, `env_hideout_corridor.png` exist but do not prove the needed eye-vault layout | **New `env_madara_eye_vault`**: near-black stone room with ordered sealed eye-storage shelves and a clinical bed; procedure implied, not graphic. **New `env_madara_hideout_exit`** if the daylight cave-mouth opener cannot be obtained from the existing training plate. | Eye vault / training cavern / cave exit. |
| Oto hidden base / lab | ch1, ch5 | Existing `env_hideout_corridor.png` is visually a blue-doored generic corridor and does not match the rock-carved source base | **New `env_orochimaru_lab`**: cramped dim clinical chamber for ch1. **New `env_oto_hidden_base`**: false-rock entrance plus three rock-carved passages. | Exterior breach / corridor. |
| Oto throne hall / collapse exterior | ch5 | No | **New `env_oto_throne_hall`**: cavernous hall, raised throne, enormous snake statue. **New `env_oto_broken_exterior`**: collapse breach, blasted stone, clear daylight. | Intact hall / half-collapsed / exterior rubble. |
| River Country training scar | ch5 parallel insert | No | **New `env_training_scarred_field`**: burned grass, broken trees, no war architecture. This is a brief continuity insert; avoid spending a full reference batch if a generic terrain plate can be approved. | Day / post-spar. |
| Wave boat / coastal exit | ch6–7 | Partial — `manga/refs/images/env_wave_village.png` and `env_wave_bridge.png` | Existing Wave plates may support establishing shots only. **New `env_wave_boat`** for the small boat, fog, and travel staging if the chapter keeps the crossing. | Night boat / mist approach. |
| Kiri gate / mist port | ch7 | No | **New `env_kiri_mist_gate`**: wet stone gate and low harbour edge swallowed by cold sea fog. | Arrival / follower test. |
| Kiri rebel camp | ch7–10 | No | **New `env_kiri_rebel_camp`**: improvised occupied camp with damp paths, tents, guards and civilians, central command area. **New `env_mei_tent`**: map desk and command chairs under muted lamplight. | Day command / night camp. |
| Kiri hill | ch8 | No | **New `env_kiri_moonlit_hill`**: open grassy rise over misty camp, five-spy ambush space, moonlit blue-grey negative space. | Empty / Mei-and-Naruto conversation. |
| Mizukage tower | ch10–11 | No | **New `env_mizukage_tower`**: distant tallest Kiri landmark, recognisable vertical mass through mist; it is the Kyūbi's target, not an interior setting. | Intact distant / destroyed silhouette. |
| Kiri army field | ch10 | No | **New `env_kiri_battlefield_open`**: broad wet/dry battlefield with a distant army horizon and room for fire effects. | Pre-flood / aftermath. |
| Water-filled crater | ch10 | No | **New `env_kiri_water_crater`**: a single large battle crater filled with shallow water, broken earth rim, sight lines for water dragon and sword duel. | Flooded / steaming / drained. |
| Linked crater aftermath | ch10–11 | No | **New `env_kiri_battlefield_crater`**: connected impact craters, torn earth, smoke and low dust; keeps Yagura at center and Naruto nearer the foreground rim. | Before full Sanbi / merged after Susano'o bomb / blue-column aftermath. |

## Page reference-count budget

| Page class | Typical ordered page refs (`R`) | + runner style | Total | Direction |
|---|---:|---:|---:|---|
| Quiet two-person dialogue | 2 characters + 1 environment = 3 | 1 | 4 | Keep one location plate; do not add prop sheets unless the prop is the beat. |
| Council page | Naruto + 3 named speakers + 1 environment = 5 | 1 | 6 | Rotate visible speakers across pages; use anonymous layered silhouettes for the remaining council. |
| Oto duel | Naruto state + Orochimaru + Kabuto + 1 environment = 4 | 1 | 5 | Add Manda *or* a Susano'o state only on the page that reveals it. |
| Kiri command/tower page | Naruto + Mei + Ao + Chōjūrō + 1 environment = 5 | 1 | 6 | Keep unnamed rebels generic. Do not place Kurama and the full command group in the same close page. |
| Kiri climax | Naruto state + Yagura/Sanbi + one form/technique + 1 environment = 4–5 | 1 | 5–6 | Split transformations by page: human → cloak → full Sanbi. |
| Worst plausible page | Naruto + 6 named council members + environment + prop/eye sheet = 10 | 1 | 11 | Under the 16-image working budget, but visually overcrowded; split it anyway. |

### Pages at risk of needless over-reference

| Risk page | What would inflate it | Required limit |
|---|---|---|
| ch4 council confrontation | Binding every council attendee plus Naruto, Tsunade, Jiraiya, and the chamber | No more than 4 named non-Naruto speakers in one page; other attendees are distant generic silhouettes. |
| ch5 Manda / Susano'o climax | Naruto, Orochimaru, Kabuto, Manda, full Susano'o, separate gunbai and sword, plus terrain | Do not show every combatant/form in a single panel. A close combat page should use the relevant Naruto state, the active opponent/form, and one terrain plate. |
| ch10–11 transformation finale | Human Yagura, cloak, full Sanbi, Naruto, Susano'o, Kurama, Mei, Yugao, Ao, rebels, multiple technique plates | Each state has its own page. Kurama is off-page in the final Three-Tails exchange; Mei/Yugao arrive only after it. |

## Build sequence

1. **Konoha pack:** `homura`, `koharu`, `tsunade`, `shizune`, `shikaku`, required council heads; `env_konoha_after_invasion`, `env_konoha_council_chamber`, `env_inner_sewer`, `kurama_inner`, `itachi`, `kisame`, `env_uchiha_compound`, `env_naka_shrine`.
2. **Time-skip/Oto pack:** all three `naruto_v4_*` states, `gunbai_v4`, `sasuke_16`, `karin`, `manda`, both orange Susano'o forms, plus the Madara/Oto environment plates.
3. **Kiri pack:** `yugao_v4`, `ao_v4`, `mei_v4`, `chojuro_v4`, `yagura_human`, cloak/full-Sanbi forms, Mokuton plates, and the six Kiri locations in their listed state variants.

Do not start an image page whose named visible character, creature/form, or location is marked new above. The safe fallback is to stage the source beat on a different page after its reference exists, not to substitute a canon-trained look or an unrelated existing sheet.
