# Model shootout — can anything beat gpt-image-2 on price AND quality?

Candidates drawn from the Image Arena / Artificial Analysis leaderboards, filtered to models
that (a) exist on Replicate and (b) **accept reference images**, which is non-negotiable —
character consistency across 350+ pages rests entirely on them.

Every model got the SAME page: the six-panel Orochimaru dialogue page from `TIER_REPORT.md`,
same three reference images, same assembled prompt. Directly comparable to the gpt-image-2
low/medium/high renders already in that report.

## Reference-image support (the first filter)

| Model | ref param | verdict |
|---|---|---|
| `google/nano-banana-2` | `image_input[]` | tested |
| `bytedance/seedream-4` | `image_input[]` | tested |
| `reve/reve-2.1` | `reference_images[]` | **upstream API down** (`PARTNER_API_CLOSED`) — untested |
| `qwen/qwen-image` | `image` (single) | disqualified — one reference only |
| `black-forest-labs/flux-2-klein-9b-base-lora` | `images[]`, max 5 | needs a LoRA; see LORA_RESEARCH.md |
| not on Replicate | — | seedream-5.0-pro, mai-image-2.5, gemini-3.1-flash-image, qwen-image-2.0-pro |

## Results

**`google/nano-banana-2` — the only genuine competitor.**
Three page types tested, all three succeeded:
- *Dialogue page*: correct six-panel uneven layout, **perfectly legible correctly-attributed
  lettering**, characters on-model, halftone and hatching present, 1696x2528 (4.3 MP — larger
  than gpt-image-2's 1152x2048).
- *Action page*: five panels, SFX crossing the gutter, hard speed lines, correct adolescent
  proportions. One stray unrequested "ZAP!".
- *Splash*: honoured `SPLASH` (no panel grid), clean title lettering, dense cross-hatching.

Roughly 20s/page. Minor flaw: some canon drift in Naruto's hair on small figures.

**`bytedance/seedream-4` — cheapest viable, but fails.**
Art quality is fine; prompt adherence is not. It **copied the style reference's content** —
invented its own dialogue ("AND I WILL!!", "CATCH UP WITH SASUKE!"), drew canon orange-clad
Naruto, and reproduced the reference page's scene. This is precisely the failure `STYLE_REF`'s
ignore-list exists to prevent, and which gpt-image-2 and nano-banana-2 both respect. Unusable
without abandoning the style-reference system.

**`qwen/qwen-image`** — single reference image only, so it can't carry our bindings. Text-only
render produced canon Naruto, no lettering, character-sheet layout. Structurally disqualified.

## Pricing — and the answer to the question

Replicate does not publish per-image prices for these on its pricing page or the model pages
(both are JS-rendered), and there is no balance/billing API endpoint. **The figures below are
Google's published rates and third-party aggregators, NOT verified against the dashboard.**
Check the dashboard before acting on them.

| Option | ~price/image | Arena Elo | verdict |
|---|---|---|---|
| gpt-image-2 `low` | **$0.012** | — | still the cost champion, and TIER_REPORT found it genuinely good |
| bytedance/seedream-4 | $0.027 | 1230 | cheap, but fails prompt adherence |
| gpt-image-2 `medium` | $0.047 | 1381 | current default |
| nano-banana-2 @ 1K | ~$0.067 | 1327 | |
| nano-banana-2 @ 2K | ~$0.101 | 1327 | quality competitive/better, larger output |
| gpt-image-2 `high` | $0.128 | 1376 | |

**Answer: no — nothing tested is both highly ranked and cheaper than gpt-image-2 at the tiers we
actually use.** Nano Banana 2 sits *between* `medium` and `high`.

The one real win available: **if you were going to spend `high` ($0.128), nano-banana-2 at 2K
(~$0.101) is cheaper and at least as good, with 4.3 MP output instead of 2.4 MP.** Against
`medium` it costs ~2x, and against `low` ~8x.

## Recommendation

1. Keep gpt-image-2 `low` as the default. Three volumes and the tier test say it is fine.
2. Use **nano-banana-2 @ 2K in place of gpt-image-2 `high`** for splashes and single-dominant
   -panel pages — cheaper than `high`, and a bigger, better-inked image.
3. Do not adopt seedream-4 at any price while it ignores the style-reference ignore-list.
4. Re-test `reve/reve-2.1` when its upstream comes back — it ranked 2nd on Artificial Analysis
   (1329) and was the strongest candidate I could not evaluate.
5. Verify all prices on the dashboard first.

Adding a model is a two-line change in `backend.py` — the payload shape differs per model
(`image_input` vs `images` vs `reference_images`) but nothing above that layer changes.
