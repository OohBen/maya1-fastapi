# PIPELINE — how to make a chapter

Operational handoff. Everything needed to produce a chapter without prior context.
Read this **plus** `story/00_SERIES_BIBLE.md` before generating anything.

---

## 1. The decisions, already made

| Question | Answer | Why |
|---|---|---|
| Provider | **Replicate** | Quality tiers work; **reference images are free** |
| Model | `openai/gpt-image-2` | Best staging + identity + gutter discipline of 7 tested |
| Default tier | **`low`** ($0.012) | 93% of medium's quality at 26% of the price |
| Escalate to | `medium` ($0.047) | Emotional beats, splash pages, final pages |
| `high` ($0.128) | Reference pack, title plates, chapter-opening splashes | |
| Aspect | `2:3` portrait | |
| Dialogue | **Composited afterwards**, never model-drawn | Kills gibberish, wrong-speaker, font drift |
| SFX | **Model-drawn**, integrated into art | Verified — renders clean, correctly spelled, angled with motion |
| Workers | 50 | Replicate allows 600 predictions/min |

### Do NOT use the OpenRouter Responses API for pages
Its `image_generation` tool silently routes to **"GPT-5 Image"**, ignores the `quality`
parameter entirely, and costs a flat **~$0.251/image**. Worse, `usage.cost` in the response
only bills the *mainline* model's tokens — the image cost never appears in the API at all,
only on the billing dashboard. It undercounted spend by ~20×. It is the only path that can
emit several images from one request, but it is 20× the price with no cost control.

---

## 2. Directory layout

```
manga/
  genlib.py              STYLE / NO_TEXT / UNIQUE constants, rep_generate(), Ledger
  letterer.py            balloon detection + text fitting + title plates
  PIPELINE.md            this file
  story/
    00_SERIES_BIBLE.md   cast, design specs, world rules, themes, 50-ch arc map
    volume_01/
      VOLUME_01.md       9-chapter plan
      chNN_*.md          per-chapter beats, refs, dialogue, direction notes
  refs/
    build_refs.py        reference pack builder
    images/*.png         the pack
  chapters/
    build_chNN.py        page specs for one chapter
    letter_chNN.py       lettering + PDF assembly
    chNN/raw/            generated art
    chNN/lettered/       final pages
    chNN/ChapterNN.pdf
```

---

## 3. Making a chapter — the loop

**Step 1. Read the chapter file** (`story/volume_01/chNN_*.md`). It has the beats, page
budget, refs, key dialogue and direction notes. It is the brief.

**Step 2. Write `chapters/build_chNN.py`.** Copy `build_ch01.py` and replace the `PAGES`
list. Each entry is `(page_id, panel_count, description, refs, quality)`.

**Step 3. Generate.** `python3 chapters/build_chNN.py` — resumable, skips existing files.

**Step 4. Review every page visually.** Not optional. Check the failure list in §5.

**Step 5. Fix and regenerate** individual pages: `python3 chapters/build_chNN.py p07 p12`
(delete the PNG first).

**Step 6. Letter.** `python3 chapters/letter_chNN.py` — composites dialogue and builds the PDF.

---

## 4. Writing a page prompt — the required parts

Every page prompt must contain **all** of these. Omitting any one causes a known failure.

1. **Page frame** — "A single complete manga PAGE in portrait orientation, with a clean white
   page margin and clean white gutters between panels, read left to right."
2. **Panel-by-panel composition** — numbered, with camera angle and content. The model infers
   nothing. If it isn't written, it's random.
3. **Reference binding, indexed** — `gpt-image-2` wants explicit roles:
   > "Image 1 is the CHARACTER REFERENCE for the boy: [full design restated]. Reproduce that
   > face, hair and outfit exactly. Ignore Image 1's white background, its three-view layout
   > and its standing pose."
   **Always say what to ignore.** Every reference carries information you don't want.
4. **The UNIQUE clause** on any page with other people — without it the protagonist's blond
   hair and red spiral leak onto background extras.
5. **Lighting logic for that location** — restated every single page (see bible §Tone).
6. **Balloon instruction** if there's dialogue — "Leave N empty white speech balloons with
   clean black outlines in uncluttered areas. Every balloon is left completely blank inside —
   plain white, empty, unlettered."
7. **SFX instruction** if there's impact — "Draw large hand-drawn manga SOUND EFFECT lettering
   integrated into the artwork: a huge jagged impact effect reading "DOSU" across panel 1.
   Drawn as part of the art, angled and distorted with the motion."
8. **STYLE + NO_TEXT** constants from `genlib` appended last.

### Hard prompt rules learned the expensive way

- **Never write emphatic capitalised "NO".** A model rendered the literal word **"NO"** into
  two speech balloons because the prompt said *"NO text, NO letters, NO words."* Phrase
  negatives as *"left completely blank inside — plain white, empty, unlettered."*
- **Bind every character who appears.** Three pages in Ch1 mentioned "the boy" without
  `naruto_06` in refs; all three invented a dark-haired child. If a character is named in the
  description, their reference must be in the list. Check this before running.
- **Genre priors beat adjectives.** "Black shinobi boots" produced open-toe sandals every
  time, on every model. We accepted sandals as canon; don't fight priors you don't need to win.
- Environment refs are generated **empty of people** and bound with "ignore the fact that it
  is empty."

---

## 5. Review checklist — what actually goes wrong

Check each page against this before lettering.

| Failure | Symptom | Fix |
|---|---|---|
| **Unbound character** | A named character rendered with wrong hair/face | Add their ref, regenerate |
| **Character bleed** | Extras with the protagonist's hair colour or clothing motif | Add/strengthen UNIQUE clause |
| **Missing env ref** | Scene set in an invented room | Add env ref, regenerate |
| **Style drift** | Soft shading, depth-of-field blur, painterly faces | Regenerate; restate STYLE |
| **Balloon overflow** | Letterer reports `filled < found` | Fine — spare balloons are ignored |
| **Too few balloons** | `found < len(dialogue)` | Regenerate asking for more balloons |
| **Gibberish text** | Any stray lettering | Regenerate |

Accept minor costume drift (a stripe, a patch, footwear) — chasing it burns budget for no
reader-visible gain. Never accept a wrong face or wrong hair on a named character.

---

## 6. Lettering

`letterer.py` finds balloons by connected-component analysis on near-white regions inside the
page margin, filters by area fraction / fill ratio / aspect, sorts them into reading order
(top-to-bottom by band, then left-to-right), and fits wrapped text at the largest point size
that fits. Dialogue comes from the chapter file's dialogue list, in order.

`title_plate()` composites a chapter title into the reserved upper area of a title page. Title
pages must be generated with **"keep the entire upper third as calm uncluttered night sky for
a title to be placed later."**

---

## 7. Costs (measured)

| Item | Cost |
|---|---|
| Reference pack, 15 images @ high | $0.35 |
| Chapter 1, 25 pages (21 low, 2 med, 2 high) | $0.67 |
| Projected: Volume 1, 9 chapters ≈ 190 pages | **≈ $5–7** |

Every call is logged to a `ledger.json` next to its output with page id, tier, cost and refs.

---

## 8. What Chapter 1 contains (done)

"The Tenth of October" — 25 pages. Festival splash → the mob → the alley → the knife (medium
splash) → the word "Kyūbi" lands → silhouette beating → hospital → the overheard conversation
about Jiraiya refusing him → "people hate what they don't understand" → the boy stops asking.

Produced for $0.673. Three pages regenerated for unbound-character errors. Lettered, PDF built.

## 9. What's next

Chapters 2–9 per `story/volume_01/`. The reference pack needs extending for them — see
`refs/build_refs.py` (`CHARACTERS_V2`, `ENVIRONMENTS_V2`). Then Volume 2 begins at the bell
test (fic ch3 end → ch4), and **there is no Wave arc** — it goes straight to the Chūnin Exams.

---

# ADDENDUM — techniques proven in production

## Model-drawn SFX (adopted)
Sound effects render **correctly spelled, correctly angled, and integrated into the artwork**
in a way compositing cannot match. Tested on an impact page: "DOSU" as a huge jagged white
effect, "KAH" smaller — both clean, both distorted with the motion. **Adopted.** Dialogue
still composites deterministically; only SFX go through the model.

Prompt form:
> "Draw large hand-drawn manga SOUND EFFECT lettering integrated into the artwork: a huge
> jagged impact effect reading "DOSU" across panel 1, and a smaller rough "kah" in panel 2.
> Drawn as part of the art, angled and distorted with the motion. Do not place any other text
> on the page and leave any speech balloons completely blank."

## The register shift — how to draw exposition
The source's worst adaptation problem is long lectures at a table (the Sage of Six Paths in
Ch7, Madara's Akatsuki confession in Ch8). Drawing two men talking for four pages kills them.

**Solution: render the myth in a deliberately different visual idiom** and intercut small
normal-manga panels of the listener. In Ch7 the Sage plates are prompted as:

> "RENDER THIS PAGE IN A DELIBERATELY DIFFERENT, OLDER VISUAL IDIOM from a normal manga page:
> flat flaking mineral pigments, muted ochre, indigo and dull gold on an aged parchment ground,
> thick uneven brush outlines, no cel shading, no modern anime rendering — it should look like
> an ancient painted scroll or woodblock print rather than a comic page."

Critically, **omit the STYLE constant on those pages** — it fights the register shift. The
build script does this automatically by checking for the marker string in the description.

Result: the myth pages read as genuine antique scroll paintings and the contrast makes the
exposition land. This is reusable for any flashback, legend or vision sequence.

## Overriding a reference
When a character reference carries an attribute that is wrong for a given page (e.g. the
age-10 sheet has red Sharingan eyes, but the scene is *before* the awakening), bind the sheet
for build and clothing and override the attribute explicitly:

> "Reproduce his build, hair and outfit exactly, but his eyes must be ORDINARY BLUE — he does
> not have red eyes yet, so ignore the eye colour in Image 1."

This works reliably and avoids generating a second near-duplicate reference sheet.

## Measured costs, whole volume
| | |
|---|---|
| Reference pack, 41 images | $0.94 logged |
| Chapters, ~190 pages | ~$5 |
| Whole volume | **under $10** |

Note the reference-pack figure is the *logged* Replicate number. The earliest packs were built
through the OpenRouter Responses path before that was abandoned; those were billed at ~$0.251
an image and only visible on the dashboard.

## Balloon placement decides who is speaking
Discovered producing Ch2. The letterer fills balloons in reading order, so **where the model
puts a balloon determines which character the line is attributed to.** If two characters are
talking and both balloons land on one character's side of the panel, the reply reads as
though the wrong person said it.

Fix at the prompt, not the letterer: state balloon positions per panel, e.g.
> "Leave one empty balloon in the upper left of panel 1 beside the old man, and one in the
> lower right of panel 1 beside the boy. Panel 2 has no balloon."

Check this while reviewing: for every dialogue page, confirm the balloon on each side belongs
to the character standing there.

## Avoid single unbreakable long tokens in dialogue
The letterer wraps on spaces and shrinks to fit. A line that is one long token (`"...Madara."`)
cannot wrap, so it overruns the balloon outline. Rewrite the line to give it a break point.

## Bind by panel CONTENT, not by named nouns
The unbound-character error recurred in Ch5 from a new direction: the description said *"the
old man's hand lifting toward the boy's face"* without `madara` in the refs, and the model
invented an entirely different man — producing a warm father/son scene that destroyed the page.

The bind check must be *"who is physically present in this panel"*, not *"whose name did I
type"*. A character referred to by role — "the old man", "the vendor", "his sensei" — is just
as unbound as one referred to by name. Before running any chapter, walk each page description
and list every human body that will be drawn, then confirm each has a reference.

## Open problem: art style reads as digital painting, not printed manga
User feedback on Volume 1: the pages look like soft-shaded digital anime illustration
(Ghibli-ish) rather than ink-on-paper manga. The reference look is flat colour fills, heavy
black outlines, hard-edged shadow shapes, panels on white paper.

**Prompt-only fixes were tested and FAILED.** Three escalating style strings — see
`bench/results/t14_style/` — produced output essentially identical to the baseline:
- `v2_printed`: "PRINTED MANGA PAGE… all colour is FLAT… no gradients, no airbrushing, no glow"
- `v3_inkonpaper`: v2 plus "must read as INK ON PAPER, not a digital painting… avoid soft
  shading, painted rendering, cinematic lighting, depth of field, glowing light sources"
- `v4_retro`: "1990s shonen manga official COLOUR EDITION… halftone screentone dots"

None of them moved the render. This is a prompt ceiling, and the established fix for a prompt
ceiling in this pipeline is a **reference image** — the same thing that solved character
consistency. Next step is a STYLE reference slot in the binding set, with the usual ignore
clause: *"Image N is a STYLE reference only. Copy its inking, flat colour fills and shading
technique. Ignore its characters, panel layout, story content and lettering entirely."*

Risk to watch: content bleed from the style reference, worst on pages featuring the
protagonist, since canon designs can drag our age-13 design back toward the orange jumpsuit.
Test on a page without him first.

## Free resolution upgrade
`aspect_ratio="1152x2048"` costs the **same $0.012** at `low` as `1024x1536` — a 33% linear
resolution increase for nothing. Use it on any re-render. Larger sizes up to `2160x3840` are
available but were not price-tested.

## Characters the source never describes need CANON-accurate specs
Madara's first reference was a generic gaunt old wizard and did not read as Madara at all. The
cause: the fic never describes him, because it assumes the reader already knows the character,
so the spec was written from prose alone.

Two lessons:
1. **When the source assumes canon knowledge, the reference spec must supply it.** Check every
   character against how they actually look, not against what the prose says about them.
2. **Describe the SILHOUETTE, not the features.** "Long black hair falling past his shoulders"
   produced a wizard. What made him recognisable was: *"an ENORMOUS wild mane of jet-black hair
   that falls well past his waist and flares outward in huge jagged wind-blown spikes… the
   silhouette is dramatic and unmistakable, far larger than his head."* For strongly-designed
   characters the overall shape carries the identity; itemised features do not.

The previous generic sheet is kept at `refs/images/_madara_OLD_generic.png` for comparison.
**Known inconsistency:** Volume 1 chapters 2, 4, 5, 6, 7, 8 and 9 were generated against the old
sheet, so their Madara is off-model. Not retroactively fixed — Volume 2 onward uses the new one.

---

# REVERSAL — the model should write the dialogue after all

The founding rule "never let the model letter" is **withdrawn**. Tested on a seven-balloon page
(`bench/results/t18_text/A_model_text.png`): every line rendered correctly spelled, in clean
uppercase comic lettering, correctly placed clear of the faces, with no gibberish anywhere.

Give the lines explicitly, panel by panel:

> "LETTERING: draw the speech balloons WITH their dialogue written inside, in clean bold upright
> English comic lettering, all capitals, correctly spelled, centred in each balloon. Use exactly
> these lines, each in its own balloon, in this order:
>   PANEL 1: "RIGHT. WELL DONE."  and  "NEXT UP, UZUMAKI."
>   PANEL 3: "CHANGE!!!"  … etc.
> Place each balloon clear of the faces. Do not write any other text anywhere on the page."

Why this is better than compositing:
- Balloon shape, size and tail all fit the art, because they are drawn with it.
- Speaker attribution is correct by construction — no more band-sorting bugs.
- Balloons can overlap panel borders and figures the way real manga does.
- One pass instead of two.

`letterer.py` is kept as a **fallback** for pages where text comes back wrong, and for any late
dialogue change that isn't worth a re-render.

# CONFIRMED — style references teach style, not content

The first mimic test used a style reference from the same volume and arc as the target page,
which was leakage. Re-run with `v06_p031` — a different volume, different arc, no shared
characters or setting — and the manga rendering still transferred. The reference is teaching
technique, not being copied.

# Staging fixes that measurably worked

Added to the page prompt and visibly effective:
- **Cluster, don't line up.** "arranged as an OVERLAPPING CLUSTER at different depths — one partly
  cropped by the panel edge, one turned away, one leaning in — never a straight row facing camera."
- **Effects are transparent.** "a SWIRLING PALE BLUE TORNADO … but it is TRANSPARENT: the wooden
  floorboards and splintering planks stay clearly VISIBLE THROUGH it."
- **Explicit irregular panel geometry**, given as bands with percentage heights and unequal widths,
  rather than describing panel content and letting the model choose the layout. Left to itself it
  always produces equal horizontal bands.
- **Figure proportions stated numerically**: "about six and a half heads tall, long limbs, narrow
  shoulders, thin necks — never short or thick-set."
- **Demand white**: "keep LARGE AREAS OF FLAT WHITE OR UNDRAWN BACKGROUND."

## Audit EVERY character for its silhouette-defining feature
This failed twice — Madara (the mane) and Hiruzen (the hat). Both were written from the fic's
prose, which never describes them because it assumes canon knowledge, and both came back as
interchangeable old men.

Before generating any reference sheet, ask: **what is the one shape that makes this character
recognisable at thumbnail size, in silhouette, with no colour?** Then make that shape the
dominant clause of the spec.

- Madara → the enormous spiked mane, larger than his head
- Hiruzen → the kage hat WORN ON THE HEAD with its drapes, not carried
- Kakashi → mask plus the slanted headband covering one eye (already correct)
- Zetsu → the split body plus the venus-flytrap shell (already correct)

A character described only by hair colour, age and clothing has no silhouette and will come back
generic. Old sheets are kept as `_<name>_OLD_generic.png` for comparison.

## Staging is now a first-class prompt component
`refs/MANGA_STAGING_GUIDE.md` (573 lines) was produced by reading 42 library pages directly and
running an automated panel detector over all 1119. `genlib.STAGING` encodes its universal rules;
§12 of the guide has ~35 paste-able fragments for per-page specifics.

The measurements that most contradict what we were doing:

| Measured in real manga | What we were generating |
|---|---|
| **6–9 panels per page** (48% of pages; mean 4.94) | 2–4 panels |
| **~2 panels in 3 have no drawn environment** | every panel fully rendered |
| One dominant panel, median 32% of page area | near-equal bands |
| Groups at 4:1–10:1 depth scale ratio, someone cropped, someone turned away | evenly spaced row facing camera |
| Effects are opaque ink; ground stays visible through them | glow that washes out the scene |
| Emotion escalates by cropping tighter | emotion escalates by adding rendering |

**Zero panels in 42 pages had three or more characters at one depth, evenly spaced, facing
camera.** That arrangement does not occur in the source material at all.

## Subagent process warning: image reads can silently return nothing
The research agent reported that its first ~20 image reads silently came back empty, and it only
caught this because it checked. Any agent asked to "look at every page" can therefore believe it
has reviewed work it never saw. Instruct reviewing agents to verify that each image actually
returned content, and to report the count they genuinely viewed.

## Style reference images can trip content moderation
A completely harmless page (an empty clearing, no characters, no violence) was rejected three
times with `E005 flagged as sensitive`. The prompt was not the problem — the **style reference
image** was. A violent library page attached to a benign prompt gets the whole call rejected.

`build_v2ch01.py::build_one` now walks down the ranked style candidates until one passes rather
than failing the page. Two other lessons from the same incident:

- **Never let one page abort a chapter.** `build_one` catches and returns `[FAIL] <page>` so the
  other 19 pages still generate.
- When a page fails moderation, check the style ref before rewriting the prompt.

---

## ADDENDUM — what Volume 2 changed (140 pages, $14.73)

Volume 2 is finished. Six things in here are now load-bearing; a subagent producing Volume 3
should start from `chapters/build_v2ch07.py` as the template, not from any Volume 1 file.

### The chapter file is now just page specs

`runner.py` owns the build loop and `chapters/prompts.py` owns the shared vocabulary — cast
bindings, `SAY` / `OFF` / `ONLY` / `CAP` / `TITLE` / `SFX`. A chapter file declares `PAGES` and
calls `run(PAGES, outdir, ledger)`. Adding a character means adding one binding to `prompts.py`,
not pasting it into six chapters.

### Splash pages must not get STAGING

`STAGING` uses the word "panels" nine times and wins every argument with "draw one illustration",
so `v2ch01 p01` and the first cut of `v2ch02 p01` both came back as six-panel grids of the same
building. `genlib.SPLASH` replaces it — never both — and `runner.run` picks it automatically when
a page's style query says `panels=1`.

### Balloons need a speaker AND a position AND an off-panel case

`SAY((panel, who, where, text), ...)` writes out, per balloon, where it sits and that its tail
points at its named speaker. That fixed most of it. What it did NOT fix was dialogue on a panel
where the speaker isn't drawn: on `v2ch02 p04` Naruto's line sat on a Hiruzen-only close-up and
the model grew a tail out of Hiruzen's mouth. Wrap those speakers in `OFF(...)` and the tail
becomes a short spur running to the panel border instead.

### Every name in ONLY() must be bound to a reference

`ONLY()` stops the model inventing extra characters. It does not stop it *substituting* one: on
`v2ch03 p10`, Kakashi and Sasuke were named but not bound, so Zabuza — who was bound — was drawn
in Sasuke's place. Audit before generating: if a name appears in `ONLY()` or in a panel
description, it needs a reference image in that page's `R(...)`. If the character is only a
distant extra, describe them generically instead ("two other young genin seen only as small
distant figures") and drop the name.

### Refusals must change something; timeouts must not

These are opposite failures and used to be handled identically, which meant a content refusal
burned `retries x style-candidates` calls before giving up. Now `rep_generate` raises `Moderated`
immediately when the error text looks like a content block, and `build_page` escalates by
changing the request: next style reference (the library page is often the actual trigger), then
`soften()`ed prompt, then softened with no style reference at all. Transient errors still retry
with backoff inside `rep_generate`.

### Pacing is a decision, not an inheritance

The fic disposes of the Wave mission in two paragraphs because it was unremarkable *to Naruto*.
That is characterisation and worth keeping — but it is not a reason to draw two panels. Wave got
ten staged pages and still ends on his blank face, which preserves the joke and spends the
volume's best visual material. Snow stayed a genuine one-page montage, and the contrast between
the two is what the prose was doing.

### Small things worth knowing

- **The model renders figures of speech literally.** "Every watching genin turned to stone" on
  `v2ch05 p08` produced actual grey statues. It happened to look good; it usually won't.
- **Illegible-by-design text works.** Asking for "lines of writing that are ILLEGIBLE SCRIBBLE,
  not readable words" on blackboards, exam papers and info cards reliably avoids the model
  inventing misspelled English, while still reading as a page of writing.
- Volume 2 spent $14.73 for 140 pages — about $0.105/page at a mix of `high` for beats and
  `medium`/`low` for connective tissue. `high` is worth it on splashes, fights and any page whose
  whole job is one face.
