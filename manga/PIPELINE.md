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
