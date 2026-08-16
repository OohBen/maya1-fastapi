# AGENTS.md

Instructions for any agent working in this repository. Codex reads this file automatically.

---

## 1. What this project is

An **AI-generated, full-colour manga adaptation** of the Naruto fan fiction
*"Uchiha Naruto: The Sage"* by The Omnipresent Sage (50 chapters). It is a personal-enjoyment
project for the repository owner. Not for publication, not for sale.

**Three volumes are finished — 351 pages.** The work is real and the quality bar is set; your
job is to continue it, not to redesign it.

| | Pages | Chapters | Covers | State |
|---|---|---|---|---|
| Volume 1 — *The Greatest Sin* | 207 | 9 | fic ch1–3 | Done |
| Volume 2 — *Entitled to My Secrets* | 140 | 7 | fic ch3–4 | Done |
| Volume 3 — *The Difference Between Us* | 102 | 8 | fic ch5–7 | Done |
| Volume 4 — *What Are You?* | ~110 | 8 | fic ch8–11 | **Planned, not generated** |

Source text: the fic is not in the repo (it is someone else's writing). Fetch it with the FicHub
API — `https://fichub.net/api/v0/epub?q=<fanfiction.net url>` returns a zip containing the full
HTML. FanFiction.net itself returns 403 behind Cloudflare; don't bother scraping it directly.
Split the HTML into per-chapter text files and work from those.

### Why you are being asked to do this

The work moved here because **you have a built-in image generation tool and the previous host
did not.** The prior pipeline called `openai/gpt-image-2` on Replicate at $0.012–$0.128 per page
and consumed roughly $35 of the owner's budget across three volumes. That budget is exhausted.
Your native tool makes generation free, which is the entire reason for the move.

Two consequences you must internalise:

1. **The prompts are the asset, not the API calls.** Everything in `manga/` builds prompt
   strings; only `manga/backend.py` knows how a prompt becomes a PNG. Port that one file.
2. **Cost stops being the constraint, so quality discipline must not slip.** The old pipeline
   made tier tradeoffs to save money. You don't have to — but read
   `manga/models/TIER_REPORT.md` anyway, because one of its findings is that **more pixels at
   low effort looks WORSE, not better.** Free does not mean "crank everything".

---

## 2. Porting the image backend — do this first

`manga/backend.py` is the only seam. Implement the `codex` branch:

```python
generate(prompt, refs, quality, size) -> (png_bytes, cost_usd)
```

- `prompt` — the fully assembled page prompt. Pass it through verbatim. Do not summarise,
  truncate, or "improve" it; every clause in it was added to fix an observed failure.
- `refs` — **list of local image paths, and ORDER IS LOAD-BEARING.** The prompt says
  "Image 1 is the CHARACTER REFERENCE for the blond boy…", "Image 2 is…". If your tool
  reorders or drops reference images, the book falls apart — character consistency across 351
  pages rests entirely on these.
- `quality` — `"low" | "medium" | "high"`. If your tool has no tier control (it is reportedly
  always medium), ignore this parameter.
- `size` — `"WIDTHxHEIGHT"`, 9:16 portrait. Request it explicitly; do not accept a host default
  aspect ratio, or pages will not assemble into a book.
- Return raw PNG bytes and `0.0`.

**If your tool cannot accept reference images, stop and tell the owner.** Do not generate a
volume without them — it will not match the first three and the work will be wasted.

Then verify before committing to a volume: generate 3–5 pages, look at them, and confirm the
characters match `manga/refs/images/*.png`. `manga/chapters/build_v3ch01.py` is a good probe.

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
                └── backend.py     ← the seam you port
```

Run a chapter: `python3 chapters/build_v3ch01.py` (all pages) or `... p01 p02` (named pages).
Finished pages land in `chapters/<id>/raw/`. Re-running **skips pages that already exist**, so
delete a page to regenerate it. Then `python3 pack_chapter.py v3ch01 "Amaterasu"` and
`python3 assemble_v3.py`.

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

- **Follow the fic's plot.** It is the spine. Do not invent arcs.
- **Do not cut story outcomes.** Physical exchanges may be compressed, but their setup, result,
  character decision, and continuity consequence must survive. A fight's resolution can matter
  even when the individual attacks do not.
- **Audit every volume boundary against the source.** Read the source covered by the previous
  volume's final page through the new volume's opening before planning pages. Never assume that a
  chapter break means the intervening action happened off-page.
- **Pacing is yours.** Prose compresses; comics don't have to. The Wave mission is two
  paragraphs in the fic and ten staged pages in Volume 2 ch3 — but it still ends on Naruto's
  blank face, because "it was unremarkable *to him*" is the characterisation and must survive.
  Conversely, Snow Country stayed a one-page montage. Expand what earns it, compress what doesn't.
- **This Naruto is not canon Naruto.** He is cold, long-haired, deliberate, and raised by Madara.
  He does not shout, grin, or wear orange. When in doubt, make him quieter.
- **Give each volume an engine.** V1: power bought with loss. V2: every chapter costs him
  privacy. V3: every chapter costs him a story he told about himself. V4 (planned): every
  chapter he takes something previously withheld.

---

## 6. Where things are

| Path | What |
|---|---|
| `manga/PIPELINE.md` | Full operational history and every reversal, with reasons |
| `manga/AGENTS_QUICKSTART.md` | Shortest path to generating your first chapter |
| `manga/models/TIER_REPORT.md` | Tier/resolution experiment — **read before choosing settings** |
| `manga/story/00_SERIES_BIBLE.md` | Characters, designs, continuity |
| `manga/story/volume_0N/` | Per-volume plans and chapter breakdowns |
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

## 7. Continuity you must carry into Volume 4

- **No ninjato.** Lost to Orochimaru in V3 ch2 and never recovered. Bind `N13`, not `N13S`.
- **The Mangekyō is public.** Revealed in V3 ch8 in front of a full stadium and two kage. He
  cannot un-reveal it; the village's posture toward him should show that.
- **Susano'o is orange** — the fic changed its colour explicitly because his chakra is orange.
- **Zetsu has a spore on Danzō** since V2 ch4, and fic ch8 puts Danzō in play for Hokage.
- **The Sandaime is dead** and Naruto does not attend the funeral.

---

## 8. Working agreements

- **Commit and push to `claude/new-manga-folder-d64x17`** unless told otherwise.
- **Review your own pages.** Look at every page you generate. The owner reads for enjoyment and
  should not be your QA. Check: right characters, right proportions, balloons pointing at the
  right speakers, no misspellings.
- **Generate ~5 pages, review, refine, then do the rest.** This loop caught most known bugs.
- **Don't redo finished volumes.** The owner has read them; re-reading has no value to them.
- **Report honestly.** If a page failed, say so. If you're unsure, say that too.
- **Ship navigable volume PDFs.** Every assembled volume needs nested chapter outline bookmarks.
  Keep the full-quality master and add a lightly compressed, full-resolution reading copy.
