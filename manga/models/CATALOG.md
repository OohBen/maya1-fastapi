# Model catalog — Replicate image models for the manga pipeline

Schemas pulled live from the Replicate API (`/v1/models/{owner}/{name}`), pricing from the
published model pages. Not from memory — see `raw_schemas.json` for the dumps.

## The headline finding: references are free here

On OpenRouter, every reference image passed into a call cost ~$0.012 in input tokens, which
made reference count the dominant cost driver — a 5-ref page cost 2.5× a bare one.

**On Replicate that is not true.** Every model except Grok bills a flat rate *per output image*
with no input-image line item at all. Passing eight references costs exactly what passing zero
costs. Grok is the sole exception, at $0.01 per input-image megapixel.

This inverts the earlier planning:

- Reference count is now a **quality** decision, not a budget decision. The only reason to keep
  ref sets tight is attention dilution.
- The earlier "$0.10 per page with 5 refs" figure is dead. A reference-bound page is now just
  the model's flat image price.
- Cheap tiers get genuinely cheap again, because there's no fixed reference tax swamping them.

Worth re-verifying against a real invoice once we've spent a few dollars — published pricing
tables occasionally lag actual billing.

## Capability matrix

| Model | Refs in | 2:3 portrait | Resolutions | Seed | Price / image |
|---|---|---|---|---|---|
| `openai/gpt-image-2` | **16** (array) | ✅ | up to 3840×2160 | ❌ | low **$0.012** · med **$0.047** · high **$0.128** |
| `google/nano-banana-2` | **14** (array) | ✅ | 1K / 2K / 4K | ❌ | 1K **$0.067** · 2K **$0.101** · 4K **$0.151** |
| `google/nano-banana-2-lite` | **14** (array) | ✅ | fixed | ❌ | flat **$0.034** |
| `bytedance/seedream-5-pro` | **10** (array) | ✅ | 1K / 2K | ❌ | 1K **$0.045** · 2K **$0.090** |
| `bytedance/seedream-5-lite` | **10** (array) | ✅ | 2K / 3K | ❌ | flat **$0.035** |
| `prunaai/p-image-ideogram` | **0** — none | ✅ | 1K / 2K | ✅ | $0.003 – $0.030 |
| `xai/grok-imagine-image-quality` | **1** (single) | ✅ | 1k / 2k | ❌ | 1k **$0.05** · 2k **$0.07** + $0.01/input MP |

Two of the seven are structurally disqualified from page generation before any quality test runs:

**`p-image-ideogram` accepts no input images at all.** The schema has no image field. It cannot
participate in a reference-bound pipeline, full stop. It is however the **only model here with a
`seed`**, which makes it the only reproducible one — and at $0.003 for a very-low-thinking 1K
image it is 4× cheaper than anything else. That makes it a real candidate for *reference pack
drafting* and cheap composition blocking, where you generate from text anyway and want to be able
to regenerate an exact image later.

**`grok-imagine-image-quality` takes exactly one image**, as a string, not a list. It is an
editing model, not a multi-reference compositor. It cannot bind a character sheet plus an
environment plate plus a prop sheet into one page. Its niche is single-image touch-ups and style
passes on an already-generated page.

## Per-model notes

### openai/gpt-image-2
Highest reference ceiling (16) and the widest resolution range. Three real quality tiers with a
**10× spread** between low and high, which is a much bigger lever than any other model here
offers. `moderation: "low"` is available and will matter — Volume 1 has a child beaten by a mob,
a massacre, and a patricide. 20.1M runs, by far the most battle-tested.

### google/nano-banana-2 / -lite
14 refs and the readme leads on **character consistency across scenes**, which is precisely our
core problem. Unique among the group: `google_search` and `image_search` grounding, which could
pull real reference imagery — potentially useful for matching canon Naruto designs rather than
inventing them. The lite variant drops the resolution control and costs half.

### bytedance/seedream-5-pro / -lite
10 refs. The lite variant has something none of the others do: `sequential_image_generation:
"auto"` with `max_images`, which generates a **consistent sequence in a single call**. For a
medium that is inherently sequential, that is worth testing directly — it may hold continuity
across a run of panels better than independent calls with shared references. Oddly the lite tier
starts at 2K where pro starts at 1K, so lite is cheaper *and* higher resolution at base.

### prunaai/p-image-ideogram
Text-to-image only. Seeded. Cheapest by a wide margin. Four `thinking` levels crossed with two
sizes gives eight price points from $0.003 to $0.03.

### xai/grok-imagine-image-quality
Single-image editing. The only model that bills for input. Priced like a mid-tier generator
without the multi-reference capability that would justify it, for our use.

## Latency (measured, T1 run)

| Model | Time |
|---|---|
| nano-banana-2-lite | 4.3s |
| grok-quality | 6.7s |
| p-image-ideogram | 6.7s |
| nano-banana-2 | 11.0s |
| gpt-image-2-low | 17.5s |
| gpt-image-2-med | 38.0s |
| seedream-5-lite | 45.2s |

A ~10× spread. Across a 190-page volume that is the difference between a 15-minute run and a
2.5-hour one, and it compounds with every revision pass. Latency is a real selection criterion
here, not a footnote.
