# AGENTS.md

Instructions for any agent working in this repository. Codex reads this file automatically.

---

## 1. What this project is

An **AI-generated, full-colour manga adaptation** of the Naruto fan fiction
*"Uchiha Naruto: The Sage"* by The Omnipresent Sage (50 chapters). It is a personal-enjoyment
project for the repository owner. Not for publication, not for sale.

**Four volumes are finished — 664 pages.** The work is real and the quality bar is set; your
job is to continue it, not to redesign it.

| | Pages | Chapters | Covers | State |
|---|---|---|---|---|
| Volume 1 — *The Greatest Sin* | 207 | 9 | fic ch1–3 | Done |
| Volume 2 — *Entitled to My Secrets* | 140 | 7 | fic ch3–4 | Done |
| Volume 3 — *The Difference Between Us* | 102 | 8 | fic ch5–7 | Done |
| Volume 4 — *What Are You?* | 215 | prologue + 11 | omitted ch7 seam, then ch8–11 | Done |

Source text is intentionally not tracked. Run `python3 manga/story/source/fetch_source.py`; it
retrieves and validates all 50 chapters into the ignored local source workspace. Use `--epub`
for an already-downloaded copy. Do not plan from headings or summaries.

### Why you are being asked to do this

The work moved here because **you have a built-in image generation tool and the previous host
did not.** The prior pipeline called `openai/gpt-image-2` on Replicate at $0.012–$0.128 per page
and consumed roughly $35 of the owner's budget across three volumes. That budget is exhausted.
Your native tool makes generation free, which is the entire reason for the move.

Three consequences you must internalise:

1. **The prompts are the asset, not the API calls.** Everything in `manga/` builds prompt
   strings. Preserve them verbatim and preserve reference order.
2. **Cost stops being the constraint, so quality discipline must not slip.** The old pipeline
   made tier tradeoffs to save money. You don't have to — but read
   `manga/models/TIER_REPORT.md` anyway, because one of its findings is that **more pixels at
   low effort looks WORSE, not better.** Free does not mean "crank everything".
3. **The native tool is agent-mediated.** It is not callable from ordinary Python and exposes no
   size or quality parameter. Generate through a manifest, then inspect and normalize approved
   rasters to 1152x2048.

---

## 2. Native ImageGen workflow

`manga/backend.py` still serves the ordinary HTTP runner. Its `codex` branch is intentionally
unavailable because the built-in ImageGen tool has no Python bridge. Do not claim that setting an
environment variable makes the Python runner use the native tool.

For native generation:

1. Validate the chapter with `manga/validate_chapter_specs.py`.
2. Export exact prompts and ordered refs with `manga/export_codex_manifest.py`.
3. The native tool accepts at most five local reference paths. The exporter reserves the last
   path for the shared style page and packs overflow content refs into an ordered composite.
4. Send a bounded first batch to separate generation workers. Each worker makes one call, writes
   only its own staged raster, and may make one targeted retry for a material visual defect.
5. The coordinator—not the workers—reads every page at full size and in sequence, approves it,
   then runs `manga/finalize_codex_chapter.py` to normalize it to 1152x2048 and serialize provenance.
6. Package the chapter with `manga/pack_chapter.py`; assemble the volume only after the chapter
   passes the reader-flow protocol.

Reference order is load-bearing. If the manifest says Image 1 is Naruto and Image 2 is a location,
pass exactly that sequence. Never summarize or rewrite a manifest prompt during the first call.

---

## 3. How a page is made

```
chapters/build_v<N>ch<NN>.py   page specs: prompt body, references, tier
        │  imports
        ├── chapters/prompts.py    shared vocabulary: character bindings, SAY/OFF/ONLY/CAP/TITLE/SFX
        └── runner.py              build loop, per-page resolution, parallelism
                │
                ├── genlib.py      STYLE / STAGING / SPLASH / STYLE_REF, escalation on refusal
                ├── refs/style_select.py   picks a real manga page as a style reference
                └── backend.py     HTTP backend only; native generation uses exported manifests
```

The ordinary HTTP path runs a builder directly and skips existing pages. The native path exports
the builder to a manifest and never asks a worker to write the production `raw/` directory. Read
`manga/AGENTS_QUICKSTART.md` for exact commands.

### A page prompt is assembled from

1. **`FILL`** — page fills the paper, thin gutters, no white margins.
2. **Character bindings** — `N13.format(i=1) + SAS.format(i=2)` … numbered to match `refs`.
3. **`ONLY(...)`** — the complete cast. Anyone who appears must be named AND bound.
4. **Panel-by-panel description** — numbered, each stating shot size and what is in it.
5. **`SAY(...)`** — every balloon: panel, speaker, position, exact text.
6. **`STAGING`** (or **`SPLASH`** for single-illustration pages) — appended by the runner.
7. **`STYLE_REF`** + a real colour manga page — appended by the runner.
8. **`STYLE`** — the house style string.

---

## 4. Hard-won rules — violating these reintroduces fixed bugs

Every one of these came from an observed failure. `manga/PIPELINE.md` has the full history.

- **Bind every name you use.** Any character named in `ONLY()` or a panel description needs a
  reference image in that page's `R(...)`. Unbound names get *substituted* by whatever else is
  bound — this is how Zabuza once got drawn where Sasuke should have been. If someone is a
  distant extra, describe them generically instead ("two other genin seen only as small distant
  figures") and don't name them.
- **Splash pages get `SPLASH`, never `STAGING`.** `STAGING` says "panels" nine times and wins
  every argument with "draw one illustration". Chapter openers came back as six-panel grids
  until this was separated. The runner picks by `panels=1` in the style query.
- **Off-panel speakers need `OFF()`.** A balloon whose speaker isn't drawn in that panel will
  otherwise grow a tail out of the wrong character's mouth.
- **Dialogue is final before generation.** The model draws the lettering, so a wrong line costs
  a full page re-render. Write and read the whole chapter's dialogue first.
- **Refusals must CHANGE something.** `genlib.build_page` escalates: next style reference →
  softened prompt → no style reference. Never retry a content refusal unchanged.
- **The model renders idioms literally.** "Every genin turned to stone" produced actual statues.
- **Ask for illegible text where text appears.** Blackboards, exam papers, signs: say
  "ILLEGIBLE SCRIBBLE, not readable words" or you get misspelled invented English.
- **Thirteen-year-olds are adolescents.** `STAGING` distinguishes them from young children;
  Sasuke read as ten years old until his binding stated height and build, not just age.
- **The canon design fights back.** `prompts.ALT` is attached to both Naruto bindings — the
  familiar orange, spiky-haired, grinning version is one of the most-drawn figures in training
  data and reasserts itself wherever his description is short.
- **Never pair `low` with 2160×3840.** Soft, smeary, coarse halftone. See TIER_REPORT finding 4.

---

## 5. Adaptation principles

- **The fanfiction is story truth, not a manga script.** Preserve its plot, character state,
  decisions, reveals, relationships, and consequences. Rebuild scene duration, dialogue rhythm,
  page turns, paneling, camera, and fight construction for manga. Never inherit prose pacing by
  converting summary sentences directly into captions.
- **Follow the fic's plot.** It is the spine. Do not invent arcs.
- **Do not cut story outcomes.** Physical exchanges may be compressed, but their setup, result,
  character decision, and continuity consequence must survive. A fight's resolution can matter
  even when the individual attacks do not.
- **Audit every volume boundary against the source.** Read the source covered by the previous
  volume's final page through the new volume's opening before planning pages. Never assume that a
  chapter break means the intervening action happened off-page.
- **Read context before every chapter.** Read the entire source chapter being adapted plus at
  least two complete source chapters before it and two after it. Record current relationships,
  designs, injuries, weapons, knowledge, and unresolved promises before writing page specs.
- **Read for causality after every render.** A visually strong page still fails if its result
  precedes its cause, a character knows something too early, or the next page silently resets an
  injury, outfit, weapon, relationship, or location.
- **Run an independent cold-reader gate after assembly.** Give a context-clean reviewer the full
  adapted source range, at least two source chapters before and after it, every builder/dialogue
  spec, every generated page, and the assembled PDF. The reviewer must inspect every page image,
  not infer quality from filenames or the producing agent's notes. Contact sheets are navigation;
  any ambiguity requires the original full-size page.
- **Judge the same end effect, not identical pacing.** The manga may compress attacks, expand a
  relationship beat, or stage prose differently, but each source setup, result, decision,
  relationship/knowledge change, injury/weapon state, and future consequence must survive. Review
  every chapter handoff and the full-volume read without relying on the planning notes.
- **Pacing is yours.** Prose compresses; comics don't have to. The Wave mission is two
  paragraphs in the fic and ten staged pages in Volume 2 ch3 — but it still ends on Naruto's
  blank face, because "it was unremarkable *to him*" is the characterisation and must survive.
  Conversely, Snow Country stayed a one-page montage. Expand what earns it, compress what doesn't.
- **Write before prompting.** Complete the source-truth sheet, dramatic scene script with final
  dialogue, and rough manga `name`/spread map in `manga/story/MANGA_WRITING_GUIDE.md` before any
  chapter builder. Image generation renders a solved scene; it does not discover the writing.
- **Silence must be deliberate, not uniform.** Conversation and strategy need questions,
  disagreement, inference, reaction, and decision. Action can be sparse, but a fight must remain a
  causal chain of reads, counters, costs, adaptations, and consequences rather than an attack list.
- **This Naruto is not canon Naruto.** He is cold, long-haired, deliberate, and raised by Madara.
  He does not shout, grin, or wear orange. When in doubt, make him quieter.
- **Give each volume an engine.** V1: power bought with loss. V2: every chapter costs him
  privacy. V3: every chapter costs him a story he told about himself. V4: every
  chapter he takes something previously withheld.

---

## 6. Where things are

| Path | What |
|---|---|
| `manga/PIPELINE.md` | Full operational history and every reversal, with reasons |
| `manga/AGENTS_QUICKSTART.md` | Shortest path to generating your first chapter |
| `manga/models/TIER_REPORT.md` | Tier/resolution experiment — **read before choosing settings** |
| `manga/story/00_SERIES_BIBLE.md` | Characters, designs, continuity |
| `manga/story/ROADMAP.md` | Completed scope and source-verified next-volume boundary |
| `manga/story/MANGA_WRITING_GUIDE.md` | Required prose-to-manga writing, dialogue, fight, and `name` gate |
| `manga/story/volume_0N/` | Per-volume plans and chapter breakdowns |
| `manga/story/volume_04/REVIEW_PROTOCOL.md` | Page, sequence, chapter, PDF, and independent cold-reader checks |
| `manga/story/source/fetch_source.py` | Fetches and validates the ignored 50-chapter local source copy |
| `manga/chapters/prompts.py` | Shared prompt vocabulary — add new characters here |
| `manga/refs/images/` | 70+ character/environment reference sheets |
| `manga/refs/build_refs.py` | Builds new reference sheets |
| `manga/refs/style_select.py` | Picks a real manga page as style reference |
| `manga/refs/MANGA_STAGING_GUIDE.md` | Panel-layout research from reading real volumes |
| `manga/legacy/` | Volume 1's deterministic letterer — superseded, kept for reproducibility |
| `manga/volume_0N/` | Assembled PDFs and per-volume READMEs |

Not in git: `manga/refs/style/` (276 MB of source pages, re-downloadable),
`manga/refs/style_png/` (derived cache), `manga/.env` (secrets).

---

## 7. Continuity you must carry beyond Volume 4

- **The V3 ninjato is gone.** It was lost to Orochimaru and never recovered. Post-skip Naruto
  later carries a different plain sash sword of unspecified origin.
- **The Mangekyō is public.** Revealed in V3 ch8 in front of a full stadium and two kage. He
  cannot un-reveal it; the village's posture toward him should show that.
- **Susano'o is orange** — the fic changed its colour explicitly because his chakra is orange.
- **Zetsu has a spore on Danzō** since V2 ch4, and fic ch8 puts Danzō in play for Hokage.
- **The Sandaime is dead** and Naruto does not attend the funeral.
- **Gaara's first moral turn happened.** Naruto defeated and released him; Gaara apologized to
  Temari and Kankuro.
- **Karin is under Naruto's protection.** She knows his mother was an Uzumaki and that he intends
  to take her to Konoha when it is safe.
- **Kiri ends unresolved here.** Yagura is down, Naruto is depleted, and the blue chakra column is
  deliberately unnamed until the later source explains it.

---

## 8. Working agreements

- **Commit locally to `claude/new-manga-folder-d64x17`. Push only after the owner explicitly
  approves that push and GitHub authentication is working.**
- **Review your own pages.** Look at every page you generate. The owner reads for enjoyment and
  should not be your QA. Check: right characters, right proportions, balloons pointing at the
  right speakers, no misspellings.
- **Generate ~5 pages, review, refine, then do the rest.** This loop caught most known bugs.
- **Do not broadly redo finished volumes.** Correct a finished page or boundary only when a source
  audit finds a material story/continuity failure or the owner requests it.
- **Report honestly.** If a page failed, say so. If you're unsure, say that too.
- **Ship navigable volume PDFs.** Every assembled volume needs nested chapter outline bookmarks.
  Keep the full-quality master and add a lightly compressed, full-resolution reading copy.

---

## 9. Current state and next work

Volume 4 is complete at 215 pages: an eight-page prologue repairs the omitted end of fic chapter
7, followed by eleven chapters covering fic chapters 8–11. Its master and compressed reading PDF
live in `manga/volume_04/`; both carry nested prologue/chapter bookmarks.

The next planned work is Volume 5, expected to cover the conclusion of the Kiri arc beginning in
fic chapter 12. The exact end boundary and chapter count are **not verified**. Before planning it:

1. Fetch/verify the local source.
2. Read fic chapters 10–16 in full, which provides two chapters of lead-in and at least two after
   the likely ch12–14 scope.
3. Reconcile the unexplained blue-column handoff and every surviving Kiri relationship/state.
4. Write the Volume 5 engine, source-truth sheets, source map, and chapter endings.
5. Complete every chapter's dramatic scene script, final dialogue, and manga `name`/spread map.
6. Pass a source comparison and context-clean script/`name` cold read.
7. Produce and review the 8–12-page writing/storyboard pilot required by
   `manga/story/MANGA_WRITING_GUIDE.md`.
8. Only then write the first builder and run the separate 3–5-page visual-quality probe.
