# Manga writing and prose-adaptation guide

This is the writing gate for Volume 5 onward. Volume 4 remains finished; do not restart or broadly
rewrite it from this audit.

## The source is story truth, not a manga script

The fanfiction controls:

- event order and outcomes;
- character motives, knowledge, relationships, and decisions;
- injuries, weapons, techniques, locations, reveals, and future consequences; and
- the emotional effect a scene must leave behind.

It does **not** control scene length, page count, panel count, camera, narration, dialogue density,
page turns, or fight rhythm. Those must be designed for manga. Preserve the same cause, decision,
and consequence without copying the prose's compression or converting its sentences into captions.

Do not add a new plot solution, reveal, ability, relationship change, or character decision. It is
permitted to add medium-specific dramatic material that expresses an existing source fact: a
question, pause, reaction, failed tactic, spatial beat, interruption, or exchange of dialogue. Such
material must not change what happens or what anyone knows.

## What Volume 4 taught us

A static audit of the 215 Volume 4 page specifications found 391 scripted text units and 2,104
scripted words: 1.82 units and 9.8 words per page on average. Forty-three pages had no scripted text.
The last three action-heavy chapters fell to 5.0, 4.2, and 4.1 scripted words per page. These numbers
are diagnostics, not targets.

Silence is not the defect. Naruto often gives impact, movement, or emotional recognition a nearly
wordless page. The defect is **uniform thinness**: too many scenes reduce setup, thought, argument,
reaction, and choice to a caption or a single declarative line. A fight then reads as an inventory
of attacks, and a conversation reads as a receipt confirming that the plot advanced.

The required correction is contrast. A chapter should move deliberately among dialogue-rich
strategy or relationship scenes, terse action, silent impact, reaction, and consequence.

The rendering model is allowed to draw dialogue, balloons, and effects. The observed failure was
not that those jobs were delegated to the model; it was that a plausible-looking result was treated
as approved without a sufficiently strict page and sequence review. Model output is a draft until a
reviewer has checked every required fact at full size.

## The three writing passes

### 1. Source-truth sheet

Read the entire source chapter being adapted plus at least two complete chapters before and after
it. Before inventing pages, record:

| Field | Required record |
|---|---|
| Start state | Location, time, cast, designs, injuries, weapons, knowledge, relationships |
| Scene cause | What creates the immediate problem or conversation |
| Character objectives | What each present character wants, fears, hides, or tests |
| Immutable beats | Source events, decisions, reveals, and outcomes that must survive |
| Permitted compression | Repeated attacks, travel, or prose summary that can become montage |
| Expansion candidates | Decisions, reversals, relationship changes, or discoveries that merit time |
| End effect | What the reader and each character should understand or feel afterward |
| Handoff | Exact state the next scene or chapter inherits |

The source-truth sheet is a continuity document, not page dialogue.

### 2. Dramatic scene script

Turn each source sequence into a scene with pressure and change before assigning pages. Every scene
must answer:

1. Who wants what now?
2. What prevents it?
3. What tactic do they try first?
4. What new information or resistance changes the tactic?
5. What choice, reversal, or cost ends the scene?
6. What state does the next scene inherit?

Write complete dialogue at this stage. Characters should not narrate neutral plot summaries to one
another. A line should normally do at least one of these jobs: question, evade, challenge, infer,
test, threaten, decide, reveal, misdirect, or change the relationship or tactic. If removing a line
does not alter the reader's understanding, tension, voice, or rhythm, remove it.

Quiet Naruto is not mute Naruto. This Naruto probes, withholds, redirects, calculates, and cuts. His
silence should create pressure; when he speaks, the line should reveal his method or change the
scene. Other characters need distinct agendas and speech patterns instead of serving as plot
announcers.

### 3. Manga `name` and spread map

Make a rough storyboard before a builder. Treat every left/right pair as one composition and record
for every page:

- panel rectangles and reading order;
- characters' positions, eye-lines, and movement direction;
- every balloon's exact text, speaker, tail, and placement order;
- the spread's focal panel;
- the information or emotion that changes on the page; and
- the last-panel pressure that earns the page turn.

Solve staging, lettering, and reading flow here. Image generation is final rendering, not the place
to discover the scene.

## Dialogue and balloon rhythm

Do not impose one balloon quota across a chapter. The following are observational ranges for
planning, not pass/fail limits:

| Page function | Typical planning range | Purpose |
|---|---:|---|
| Conversation, strategy, investigation | 4–8 balloons | Questions, competing interpretations, decisions |
| Action and tactical exchange | 0–4 balloons | Calls, reads, counters, short reactions |
| Impact or reveal | 0–2 balloons | Let the image carry the change |
| Emotional pause | 0–3 balloons | Gesture, expression, subtext, or one decisive line |

Keep individual balloons compact and distribute a turn across faces, hands, objects, and reactions
when the reader needs time to absorb it. Balloon placement guides the eye and must be designed with
the panel flow, not pasted over finished art.

Before approving a chapter script, check that dialogue density visibly varies and that the reader
gets enough interpretation between major actions to understand why the next choice follows.

## Fight construction

A readable fight is a chain of decisions, not a list of techniques. Establish geography, objective,
danger, and relative positions before escalation. Then build exchanges with this causal loop:

> attack -> read -> counter -> cost -> adaptation -> reversal -> decision -> consequence

Not every exchange needs all eight beats, but every exchange must change information, position,
resources, confidence, injury, or intent. If an attack changes none of those, compress it.

Required fight checks:

- Show what each fighter is trying to achieve besides “win.”
- Let the opponent interpret, misunderstand, or exploit what just happened.
- Use reaction panels to update the reader's model of the fight, not merely to show surprise.
- Track range, facing, landmarks, weapons, damage, and technique state without silent resets.
- Alternate planning, movement, silence, impact, and consequence; do not use the same beat size for
  an entire fight.
- Use large panels for genuine turns or costs, not every named attack.
- Make the final result express character: the winning choice should follow from temperament,
  knowledge, sacrifice, or relationship.

For every technique, the `name` and later builder must also lock a visible physical chain:

| Field | Required answer |
|---|---|
| Origin | Mouth, eye, palm, weapon, ground, seal, or another explicit source |
| Preparation | What pose, breath, seal, draw, or stance makes the attack possible |
| Emission | The panel where the effect visibly begins at that origin |
| Path | Direction of travel and the landmarks or bodies it crosses |
| Contact | What blocks, evades, redirects, or receives it |
| Carryover | New position, injury, damage, resource cost, or tactical knowledge |

Do not approve an effect because it is attractive. Fire Release fails if the flame appears from a
hand, chest, or empty space when the technique is supposed to be exhaled; eye techniques fail if the
active eye is hidden or the wrong pattern is visible; weapon attacks fail if grip, draw direction,
or blade continuity silently changes. If the origin or consequence is ambiguous, the page fails.

## Model lettering and effects

Integrated model lettering and generated effects remain the default because they can fit the art,
balloon shape, tails, and panel composition better than a generic overlay. Their use creates a QA
obligation, not an assumption of correctness.

Before generation, every text unit must have exact wording, page, panel, speaker, balloon position,
and tail target. After generation, compare the full-size page directly with that record and check:

- every required line exists on the assigned page and panel, exactly once;
- spelling and punctuation are correct;
- the tail points to the correct visible speaker, or the line is explicitly off-panel;
- narration and SFX use the required form and do not become speech;
- no invented text appears; and
- no balloon obscures the action, face, eye-line, or emission point needed to read the panel.

A text or effect defect triggers a targeted edit or regeneration. The legacy deterministic letterer
is an available fallback, not the default and not a substitute for inspecting the finished page.

## Page and chapter QA is production work

Generation workers perform a first check, but they never grant final approval to their own pages.
The coordinator must inspect every page at full size and record a pass or a concrete defect. After
all pages pass individually, a separate chapter reviewer reads them in order and checks dialogue,
action geography, causal continuity, and the source end effect. Corrections return to that reviewer
until the chapter passes. A contact sheet is only a navigation tool; it cannot replace original-size
inspection.

The volume may contain more than two hundred pages; that changes staffing, not the requirement.
Delegate generation and review by chapter, but do not sample pages or infer quality from worker
reports. A page with a known material failure does not enter the chapter PDF. If retries cannot fix
it, mark the chapter blocked and report the exact page and defect.

## Page and spread construction

- Prioritize simple, readable geometry. A beautiful panel that breaks spatial or reading logic
  fails.
- Give a spread one dominant image or idea. Supporting panels should prepare, complicate, or answer
  it.
- Vary shot scale and panel density. Repeated same-size closeups make conversation inert; repeated
  wide impacts make action weightless.
- Use establishing shots whenever location, distance, or combat geometry changes.
- End a spread's final page with an unresolved action, question, arrival, decision, or visual clue
  when the next spread contains its answer.
- Reserve a splash or near-splash for a state change worth pausing on.
- Read the thumbnail spread first, then the full-size lettering, then the chapter without the source
  notes.

## Volume 5 mandatory gate

No Volume 5 builder or final page generation begins until all of these exist:

1. A verified source-truth sheet for the full planned volume after reading the adapted range plus
   required context; Volume 5's completed planning read covered fic chapters 10–20.
2. A complete dramatic scene script for each planned chapter, including final dialogue.
3. A page-and-spread `name` for each chapter with balloon order and page-turn beats.
4. A source comparison confirming the same causes, decisions, relationship changes, and outcomes.
5. A cold read by a reviewer who can understand the script and `name` without the fanfiction open.

Then produce an **8–12-page writing/storyboard pilot**, not finished full-volume art. It must include:

- one conversation or relationship spread;
- one tactical action sequence with a clear reversal;
- one emotional or interpretive reaction spread; and
- at least one deliberate page-turn reveal.

Approve the pilot only when the story reads naturally, the voices are distinct, the fight geography
is clear, and dialogue density varies by scene purpose. Only then write builders and render final
art. The existing 3–5-page visual probe remains a separate art-quality check after the writing pilot.

**Current Volume 5 state:** every item above and the ten-page Chapter 4 pilot pass. The evidence is
in `volume_05/REVIEW_STATUS.md` and `volume_05/STORYBOARD_PILOT.md`. This closes writing
preproduction; it does not start production. Wait for the owner's explicit instruction, then begin
with the reference-gap audit, first builder, and separate 3–5-page visual probe.

## Review questions

### Source effect

- Did every setup, decision, reveal, relationship change, injury, and consequence survive?
- Did any added dialogue give a character knowledge or intent they do not have in the source?
- Does the scene end with the same dramatic and continuity effect even if its pacing changed?

### Reader experience

- Can a reader follow the scene without prose notes or captions that merely summarize events?
- Does each conversation contain competing wants rather than sequential exposition?
- Does each fight exchange make the next choice intelligible?
- Are important reactions present before the story moves on?
- Does every page change information, pressure, position, emotion, or expectation?

### Craft study references

The production standard above was derived from these references and direct page studies in the
[Naruto color volume archive](https://colorizedmangas.com/naruto/volumes):

- *Naruto* color edition, Volume 16 pp. 120–125 and 148–153: contrast between sparse impact pages
  and dialogue-rich explanation, reaction, and threat.
- *Naruto* color edition, Volume 37 pp. 100–105 and 130–146: tactical disagreement, role choice,
  spatial setup, trap/reversal, and consequence.
- *Naruto* color edition, Volume 51 pp. 78–82: technique, false conclusion, reversal, observer
  interpretation, and emotional objective in one short exchange.
- [Masashi Kishimoto interview](https://www.publishersweekly.com/pw/by-topic/industry-news/comics/article/68437-masashi-kishimoto-on-why-his-naruto-manga-is-so-popular.html): script-first workflow and deliberately simple panel flow.
- [Usamaru Furuya interview](https://www.viz.com/blog/posts/interview-with-usamaru-furuya-43): rough `name` practice, spread composition, page-turn panels, and balloons as eye guidance.
- [Shingo Kimura interview](https://naruto-official.com/en/news/01_1493): adapting a Naruto novel through studied linework, framing, camera, and composition rather than copying prose form.
- [Japanese Manga 101: Making a `name`](https://www.manga-audition.com/japanesemanga101_025/): story, dialogue, paneling, and composition are solved before final drawing.
- [Japanese Manga 101: Composition](https://www.manga-audition.com/japanesemanga101_030/): readable layouts, shot variation, one focal panel, and page-turn hooks.
- [Tsukasa Hojo interview](https://www.manga-audition.com/music_to_my_eyes_tsukasa_hojo/): fights need accumulated physical and character beats, not a single declarative action.
- [Yosuke Kokuzawa interview](https://kmanga.kodansha.com/blog/article/7th-prince-yosuke-kokuzawa-part-1/): medium-specific changes to dialogue and wordless action can preserve character and effect more faithfully than literal transfer.
