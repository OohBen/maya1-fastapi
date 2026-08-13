# Volume 3 — *The Difference Between Us*

**Covers:** fic ch5 → ch7 (the Orochimaru ambush through the Sound/Sand invasion).
**8 chapters · ~162 pages.**

**Arc:** Naruto meets someone he cannot beat, and finds out what he is under the composure.

Volume 2 was the village noticing him and him giving it nothing. Volume 3 takes the thing that
made that possible — the certainty that he is simply better than everyone in the room — and
breaks it on page one. Orochimaru throws him around like a doll in front of Sasuke. The rest of
the volume is him deciding what to do about that, and the answer is not reassuring: he turns
down Jiraiya, vanishes from the village for three weeks, and comes back fighting like his
grandfather.

## The spine — what each chapter takes from him

Volume 1's engine was *power bought with loss*. Volume 2's was *every chapter costs him
privacy*. Volume 3's is **every chapter costs him the story he tells about himself.**

1. His superiority — someone beats him without trying
2. His detachment — he finds out he minds
3. His cover — the tower makes him visible to every jonin in the village
4. His measure — he watches the others fight and revises upward
5. Nothing — Hinata takes the beating, and it is the one thing that reaches him
6. His mentor — he refuses Jiraiya, and there is no one above him left to ask
7. His restraint — the crowd sees what he actually is
8. His last excuse — the Hokage dies and "I am not strong enough yet" stops working

## Chapters

| Ch | Title | Pages | Ends on |
|---|---|---|---|
| 1 | Amaterasu | 22 | *"Stay down, Naruto-kun."* |
| 2 | A Gift | 20 | Naruto looking at his own hands |
| 3 | The Tower | 18 | Both scrolls opened |
| 4 | The Preliminaries | 20 | His own match, over in one movement |
| 5 | Fate | 20 | Hinata: *"What I want to change is you."* |
| 6 | The Toad Sage | 18 | He turns Jiraiya down and disappears |
| 7 | The Silent Crowd | 22 | Naruto vs Neji — he sends a clone |
| 8 | Invasion | 22 | The Sandaime dead; *"I am done waiting."* |

## Source fidelity

The fic is followed beat for beat. Where it compresses, we expand; where it dwells, we cut.

- **Expanded:** the Orochimaru fight (fic gives it ~15 exchanges of prose, we give it two
  chapters), and the invasion (the fic summarises the aftermath retroactively in ch8).
- **Compressed:** the preliminary matches. The fic runs them one by one; only Neji/Hinata and
  Naruto's own match get staged, the rest are a montage page. Same trick as Volume 2's Snow
  Country, and for the same reason — the ones that matter are the ones he reacts to.
- **Kept verbatim:** *"You are better than Sasuke-kun, but I have no interest in you — at the
  moment."*, *"I gave him a gift that will help him avenge his clan."*, *"Fate cannot be
  changed."*, *"What I want to change is you."*

## New references required

`orochimaru` (true form), `jiraiya`, `neji`, `hayate` (prelim proctor), `genma` (finals
proctor), `env_prelim_arena`, `env_stadium`. Every one leads with its silhouette-defining
feature — see PIPELINE.md. Neji is the pale pupil-less eyes and the long dark hair; Jiraiya the
white mane and the horned protector; Orochimaru the chalk-white skin and golden slit eyes.

## Production

Same pipeline as Volume 2 — `chapters/prompts.py` + `runner.py`, model-drawn dialogue with
`SAY`/`OFF`, `ONLY()` bound to references, `SPLASH` for chapter openers. Default tier is
`medium` this volume with `high` reserved for splashes and the two or three beats per chapter
that carry it, because Volume 2 showed `medium` holds up on dialogue pages.
