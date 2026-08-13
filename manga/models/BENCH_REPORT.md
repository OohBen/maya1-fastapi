# Model bench — results and routing decision

Five test rounds, 38 generations, ~$1.40 total spend. Every image is in `bench/results/`.

| Test | What it measured | Models |
|---|---|---|
| T1 | Character sheet from text, spec-heavy | 8 |
| T2 | Multi-panel manga page from text | 8 |
| T3a/b | Identity preservation, ref → two unrelated scenes | 6 × 2 |
| T4 | **Page + locked reference** — the real production case | 4 |
| T5 | T4 re-run with the negation bug fixed | 2 |

## Headline results

**1. Every serious contender can actually build a manga page.** This was the open risk and it's
gone. Correct panel counts, clean gutters, page margins, left-to-right ordering, and — critically —
**empty speech balloons with no lettering**. The deterministic-lettering plan is viable on all of them.

**2. References are free on Replicate.** Flat per-output-image pricing with no input-image line item
(Grok excepted). Ref count is now purely a quality decision. The old "$0.10/page with 5 refs" number
is dead — a reference-bound page costs the model's flat rate.

**3. Tier gaps are task-dependent, and this is the important one.** On T1 (character sheet)
`gpt-image-2` low and medium were near-indistinguishable. On T2/T4 (pages) they clearly separated:
medium delivers better crowd depth, cleaner gutters and much better *staging* — whether the panel
actually lands the story beat. Your instinct to force a page was right; the character sheet test
would have led to the wrong call.

**4. `high` is not worth it for pages.** $0.128 and 111s bought richer wood texture over medium and
slightly *worse* spec adherence on the panel-1 blocking. Reserve it for the reference pack and splashes.

## Scored on the production case (T4/T5: page + locked reference)

Weighted: identity 25%, layout 20%, bleed 15%, text discipline 15%, staging 15%, render 10%.

| | layout | identity | bleed | text | staging | render | **score** | price | time |
|---|---|---|---|---|---|---|---|---|---|
| **gpt-image-2-med** | 95 | 95 | 90 | 100 | 95 | 92 | **94.7** | $0.047 | 60s |
| **gpt-image-2-low** | 80 | 92 | 85 | 100 | 85 | 82 | **87.7** | $0.012 | 35s |
| **nano-banana-2-lite** | 90 | 90 | 85 | 100 | 72 | 85 | **87.6** | $0.034 | **7.3s** |
| nano-banana-2 | 85 | 90 | 88 | 100 | 75 | 84 | 87.4 | $0.067 | 15s |

## Value, on your 90%-for-50% rule

| | quality vs best | price vs best | verdict |
|---|---|---|---|
| gpt-image-2-med | 100% | 100% | quality anchor |
| **gpt-image-2-low** | **93%** | **26%** | ★ clears your bar decisively |
| nano-banana-2-lite | 93% | 72% | fails on price, **wins on speed (8×)** |
| nano-banana-2 | 92% | 143% | strictly dominated — **cut** |

`gpt-image-2-low` is 93% of the quality for 26% of the price. That is a better trade than the
"90% for 50%" threshold you set. `nano-banana-2-lite` matches it on quality but costs 2.8× more —
its currency is **latency**: 7.3s against 60s. Across 190 pages that's 23 minutes versus 3.2 hours.

## Survivors and routing

| Job | Model | Why |
|---|---|---|
| Reference pack (one-time) | `gpt-image-2-high` | Everything inherits it; 30 images ≈ $3.84 |
| Composition drafts / blocking | `nano-banana-2-lite` | 7s turnaround, iterate live |
| **Final pages** | `gpt-image-2-med` | Best staging, identity and gutter discipline |
| Cheap bulk / second passes | `gpt-image-2-low` | 93% quality at 26% price |
| Splash pages | `gpt-image-2-high` | Ch1 opener, Ch9 Mangekyō |

**Cut, and not worth re-running:**

- `prunaai/p-image-ideogram` — takes no input images at all. Structurally cannot do reference
  binding. Also lost the character completely on T2 (brown hair, generic face). Only redeeming trait
  is a `seed` parameter, the sole reproducible model in the set.
- `xai/grok-imagine-image-quality` — one reference image, as a string. Cannot bind character +
  environment + prop together. Also rendered a page number "12" when told not to write text.
- `bytedance/seedream-5-pro` — hung in `processing` for 10+ minutes and never returned.
- `bytedance/seedream-5-lite` — weakest identity retention; lost the hair length and the
  bang-over-eye, inverted the chest/back spiral sizes, and drifted the face between panels.
- `google/nano-banana-2` — good model, but dominated: costs 43% more than `gpt-image-2-med` for a
  7-point lower score. Its lite sibling is the better buy.

## Prompt lessons (both cost us a generation)

**Never write emphatic capitalised "NO" in a prompt.** `nano-banana-2-lite` rendered the literal word
**"NO"** into both speech balloons on T4, because the prompt said *"NO text, NO letters, NO words, NO
symbols."* Rephrasing to *"left completely blank inside — plain white, empty, unlettered"* fixed it
entirely on T5. Text-rendering models will draw the tokens you emphasise, including your negations.

**Reference-binding syntax differs by model family**, and the docs disagree:
- `gpt-image-2` — explicit indexed roles: *"Image 1 is the CHARACTER REFERENCE… use it only to fix
  his face, hair and outfit."*
- `nano-banana-2` — no special syntax exists. Google's docs use ordinal prose ("the first image") and
  explicitly recommend **restating the character's distinctive features in text** rather than relying
  on image order. Note the reference budget also differs: Gemini 3.1 Flash Image allots 10 object +
  4 character + 3 style refs, but **Flash Lite is 14 object refs only** — no dedicated character slot.

Both families are handled separately in `bench/prompts.py::BIND`.

**Genre priors override explicit wording.** Every model drew open-toe sandals when the prompt said
"black shinobi boots" — the Naruto prior is stronger than the adjective. Needs "closed-toe boots, not
open sandals."

**Character bleed is the universal failure mode.** The protagonist's traits leak onto background
extras — duplicate blonds, spare red spirals on other students' shirts. Adding *"he is the ONLY
character on this page who looks like this; every other person must look completely different"*
largely fixed it on `gpt-image-2-med`. Keep that clause in every page prompt.

## What this does to the budget

Volume 1 at 190 pages, with references now free:

| | one clean pass | with ~1.8× revision |
|---|---|---|
| all `gpt-image-2-med` | $8.93 | ~$16 |
| all `gpt-image-2-low` | $2.28 | ~$4 |
| recommended mix + ref pack + splashes | ~$13 | **~$20** |

Against the earlier $35–45 estimate. The reference-cost inversion is most of the difference. A
Chapter 1 pilot (24 pages + pack) lands around **$5–6**.
