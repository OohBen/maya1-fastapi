# Volume 2 — *Entitled to My Secrets*

**Covers:** end of fic ch3 → fic ch4 (through the Forest of Death opening).
**7 chapters · ~146 pages.**

**Arc:** Konoha decides Naruto is a threat, and is right for the wrong reasons.

Volume 1 was a boy being made into a weapon in private. Volume 2 is the village *noticing*,
and every institution in it — the Hokage, the council, Danzō, his own sensei — quietly turning
surveillance on a thirteen-year-old. He gives them nothing. The volume ends with him walking
into a forest designed to kill him, bored.

## Correction to the series bible

**The Wave arc is not absent — it happens off-page.** Fic ch4 summarises it retroactively in a
single paragraph: Zabuza, Haku, Gatō, and Sasuke awakening his Sharingan on the bridge. A Snow
Country mission (Princess Kuyoki) is summarised the same way. Neither is dramatised.

This is a gift, not a problem. Both become a **montage sequence in Chapter 3** — the two biggest
missions of Naruto's genin career rendered as a page and a half of fragments, because to him
they were unremarkable. That characterises him more sharply than dramatising them would.

## Chapters

| Ch | Title | Pages | Ends on |
|---|---|---|---|
| 1 | Shall We Dance? | 22 | Naruto hands back both bells |
| 2 | Entitled to My Secrets | 20 | Zetsu: *"Your sensei."* |
| 3 | Six Months | 22 | The Sand siblings; Gaara asks his name |
| 4 | The War Hawk | 20 | Danzō's standing offer |
| 5 | Room 301 | 20 | *"The rest are weak. They are annoyances."* |
| 6 | The Tenth Question | 20 | Ibiki: *"There is no tenth question."* |
| 7 | The Forest of Death | 22 | Three Rain genin drop out of the trees |

## The spine — what each chapter costs him

Volume 1's engine was *power bought with loss*. Volume 2's is different and should be played
differently: **every chapter costs him privacy.**

1. His cover — Kakashi now knows he is dangerous
2. His deniability — he tells the Hokage he knows everything
3. His solitude — he is watched everywhere, permanently
4. His obscurity — Danzō has personally marked him
5. His anonymity — every genin in the room now knows his face
6. Nothing. He passes without effort, and that is the joke
7. His patience — he is about to stop being careful

## Production notes — this volume uses everything Volume 1 taught

| | |
|---|---|
| Model | `openai/gpt-image-2` on Replicate, `1152x2048` |
| Tier | `low` default, `medium` for beats, `high` for chapter splashes |
| Dialogue | **Model-drawn**, given verbatim per panel — see PIPELINE.md reversal |
| Style refs | Auto-selected per page via `refs/style_select.py` |
| SFX | Model-drawn, integrated |
| Character refs | Rebuilt Madara and Hiruzen; new sheets needed (see below) |

### New references required before Chapter 1

`gaara`, `temari`, `kankuro`, `danzo`, `ibiki`, `anko`, `kabuto`, `rock_lee`, `kiba`, `shino`,
`kurenai`, `yugao`, `naruto_13_sword` (the ninjato added at the exams), and environments:
`env_training_ground_7`, `env_exam_room_301`, `env_forest_of_death`, `env_academy_corridor`,
`env_shinobi_district_apartment`.

Every one of these must lead with its **silhouette-defining feature** — see PIPELINE.md. Gaara
is the gourd; Temari the four pigtails and battle fan; Kankuro the face paint and the wrapped
bundle; Danzō the bandaged right arm, bandaged right eye and X-scar on the chin; Anko the
overcoat over mesh; Lee the bowl cut, thick brows and green jumpsuit.

## Dialogue is locked before art

Because the model now draws the lettering, **a wrong line costs a full page re-render.** So
each chapter file must contain the finished, final dialogue — read through for sense and rhythm
— before a single page is generated. Volume 1's chapter files held beats and key lines; that is
not sufficient any more.

Most of Volume 2's dialogue can be lifted close to verbatim from the source, which is
unusually strong in these chapters. Notably:

- *"Shall we dance, Kakashi-sensei?"*
- *"This dance should be entertaining."*
- *"It is not a matter of trust. I just don't want to tell you, and I think I am entitled to my secrets."*
- *"Ironic, isn't it. You don't like me keeping things from you — while you have been doing exactly that my whole life."*
- *"He never was my father. The only parent I had was my mother."*
- *"Next time you touch me like that, I will cut off your hand and feed it to you."*
- *"As much as I love to dance, I have no interest in a pointless one."*
- *"There are no other strong contestants. The rest are weak. They are nothing but annoyances."*
- *"There is no tenth question."*
