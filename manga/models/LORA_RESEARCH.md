# LoRA / FLUX research — can we get off gpt-image-2?

Motivation: gpt-image-2 costs $0.012–$0.128 per page and ~40–100s per page. The question is
whether a fine-tuned FLUX.2 [klein] LoRA gives comparable output with API control at lower cost.

## What was actually tested

Two probes against `black-forest-labs/flux-2-klein-9b-base-lora` **with no LoRA attached**:

| Test | Result |
|---|---|
| Full 6-panel page prompt + 3 reference images | Incoherent. Panels overlapped and ran off the page, lettering was gibberish, no character likeness, and it hallucinated a "COLOREDMANGA.COM" watermark. |
| Single illustration, no panels, no text, 1 character reference | The character was absent entirely — absorbed into the tree bark. |

**These are not a fair verdict on the approach.** The model is described as *"a version of
FLUX.2 [klein] 9B-base that supports fast fine-tuned lora inference"* — the base is meant to be
driven by a LoRA, and running it bare is not its intended use. Recorded here so nobody repeats
the same two probes and draws the wrong conclusion.

What the probes *did* establish, usefully:

- **It is fast.** 3.5–5.6s predict time, versus 40–100s for gpt-image-2. A 10–20x speedup.
- **`disable_safety_checker` exists.** The moderation refusals that forced the escalation ladder
  in `genlib.build_page` would simply not happen.
- **Hard cap of 5 reference images.** We routinely pass 4–6 (characters + environment + style
  page). A style LoRA would free the style-reference slot, which makes 5 workable — but it is a
  real constraint, not a detail.

## Platform situation

| | Klein 9B inference | Klein 9B training |
|---|---|---|
| Replicate | Yes — `flux-2-klein-9b-base-lora`, takes `lora_weights` as a list of URLs, "Supports ComfyUI and native Flux Klein format LoRAs" | **No trainer.** Only `ostris/flux-dev-lora-trainer` for FLUX.1-dev |
| fal.ai | Yes | Yes — `fal-ai/flux-2-klein-9b-base-trainer` |

So the path is **train on fal, infer on either**. Untested assumption: that a fal-produced Klein
LoRA loads on Replicate's endpoint. Verify before planning around it.

### Cost

- **Training (fal):** `0.0043 * steps`. 1000 steps = **$4.30**. Dataset is a zip of images with
  optional per-image `.txt` captions; fal recommends 9–50 images for a style LoRA, minimum
  1024x1024.
- **Inference:** Replicate does not publish a per-image figure where I could find one. Prediction
  metrics report `image_input_megapixel_count` and `image_output_megapixel_count`, so it is
  almost certainly billed per megapixel like the other FLUX.2 variants ($0.012/MP for dev).
  **At 2MP out + 3MP in that would be ~$0.06/page — five times gpt-image-2 at `low`.**
  This needs checking on the billing dashboard before any decision. If Klein is billed per
  megapixel at dev rates, the cost case collapses and only the speed case survives.

## The blocker a LoRA does NOT solve

**Flux cannot render legible English lettering.** A style LoRA teaches style and layout; it does
not teach orthography. Our Volume 2/3 pipeline depends on the model drawing dialogue into
balloons, and that capability is specific to gpt-image-2.

But this is not fatal, because the fix is already in this repo.

## The architecture that would actually work

1. **Train a style+layout LoRA** on the 351 finished pages. They are all one consistent style
   and they already show the panel grammar we want — uneven panels, thin gutters, full bleed.
2. **Generate pages with deliberately BLANK balloons.** We know how to ask for this; Volume 1
   did exactly that ("left completely blank inside — plain white, empty, unlettered").
3. **Letter deterministically** with `legacy/letterer.py`, which already exists and works.

This is strictly better than the current pipeline in one respect that has cost us real money:
**dialogue becomes editable for free.** Today a single wrong line means re-rendering the whole
page, which is why chapter dialogue has to be finalised before generation. With deterministic
lettering, text is a separate cheap layer.

Tradeoff: model-drawn balloons integrate with the art better than pasted ones. That was the
reason for the Volume 2 reversal in the first place. This would be trading some visual polish
for cost, speed, and editability.

## Dataset

`build_lora_dataset.py` exports training zips from what we already have. The unusual advantage
here: **every finished page still has the deterministic prompt that produced it** in
`chapters/build_*.py`, so image/caption pairs are derived automatically rather than
hand-written.

    python3 build_lora_dataset.py --out lora/style.zip                # story pages
    python3 build_lora_dataset.py --out lora/refs.zip --refs-only     # character sheets

Captions are deliberately SHORT by default (trigger word + scene type + lighting + mood + panel
count), not the full 4000-character page prompt. Trainers truncate captions hard, and a caption
describing specific panel contents would teach the LoRA to bind our style to one scene. Use
`--full-captions` to override.

Note fal recommends 9–50 images for a style LoRA. We have 351. That is likely *too many* and
they are not equally good — curate to the best 40–60 pages before spending on training.

## Recommendation

**Do not switch the production pipeline to this yet.** In order:

1. Check the Replicate dashboard for what the two test predictions actually cost. If Klein bills
   per megapixel at FLUX.2-dev rates, it is more expensive than gpt-image-2 `low` and the whole
   premise fails.
2. If the economics survive, curate ~50 pages and train one LoRA on fal (~$4.30) as a
   single decisive experiment.
3. Test that LoRA on the three page types in `TIER_REPORT.md`. The question to answer is not
   "does it look nice" but **"does it produce a correctly laid out page with blank balloons in
   our style, with recognisable characters, from a 5-reference budget."**
4. Only then consider the deterministic-lettering rebuild.

Meanwhile the free native-image-tool path (see `/AGENTS.md`) costs nothing and is already
running, which weakens the case for spending anything here at all.
