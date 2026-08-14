# Quality tier and output size — controlled test

Run because three volumes had drifted from the original "low by default, escalate when it
matters" policy to ~90% `high` without that being a decision. Nine images: three page types
(dense dialogue, action beat, splash) x three tiers, identical prompt and identical style
reference in each triplet, so only `quality` varies.

## Finding 1 — the tier does NOT change resolution

Every tier returns **1152x2048**. `quality` buys rendering effort, not pixels.

| | pixels | file size |
|---|---|---|
| low | 1152x2048 | 3.4-4.2 MB |
| medium | 1152x2048 | 4.8-5.1 MB |
| high | 1152x2048 | 4.1-5.2 MB |

## Finding 2 — CORRECTED: `low` is much better than I first claimed

My first read of this test said `low` "goes flat and empty, hatching disappears". **That was
wrong**, and it was wrong in a way that would have cost real money. It came from the bark
close-up crop — `low`'s worst case — and from memory of Volume 1, rather than from the full
pages this test actually produced.

Looking at the full `low` dialogue page at reading size: the forest has depth and light shafts,
the trunks carry halftone, the faces are clean, the lettering is sharp. It is a usable page. I
would not have flagged it in a read-through.

Volume 1 was `low` **and** an immature pipeline — no style-reference library, no STAGING rules,
weaker character bindings, no per-page style selection. Attributing "not good enough" to the
tier alone conflated the two. With today's pipeline, `low` is a different proposition.

Where `low` does lose to `medium`, at 1152: fine texture. Bark hatching is smoother, background
screentone is coarser. On a dialogue page it is hard to see; on a texture-heavy splash it shows.

## Finding 4 — tier and resolution INTERACT, and low+big is the worst config

`low` at 2160x3840 is **worse than `low` at 1152x2048**, not better. Backgrounds go soft and
smeary, trunk linework turns mushy, and the halftone becomes a visibly coarse grid. The model
does not spend enough rendering effort to fill the larger canvas.

So resolution cannot simply be cranked. More pixels need more effort behind them.

| config | verdict |
|---|---|
| `low` @ 1152 | good — genuinely usable, cheapest |
| `medium` @ 1152 | good, marginally finer texture |
| `high` @ 1152 | marginally better again; not worth 10x low |
| `medium` @ 2160 | **best looking** — fine print-screen halftone, crisp thin linework |
| `low` @ 2160 | **worst** — soft, smeary, coarse. Do not use |

## Recommended policy (revised)

| Page type | Tier | Size | ~cost |
|---|---|---|---|
| Chapter splash, single-dominant-panel page | `medium` | 2160x3840 | $0.047 |
| Fight beats, emotional close-ups | `medium` | 2160x3840 | $0.047 |
| Standard dialogue / montage / establishing | `low` | 1152x2048 | $0.012 |
| never | `low` | 2160x3840 | — |

A ~110-page volume at roughly 25 big pages + 85 standard: **~$2.20**, versus $12.37 for
Volume 3. The saving comes from admitting `low` was fine all along, not from cutting quality.

## Cost of this test

11 images, $0.61.
