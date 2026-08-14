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

## Finding 2 — the real jump is low -> medium, not medium -> high

- **low** fails in a specific, recognisable way: **backgrounds go flat and empty, hatching
  disappears, halftone texture vanishes.** A close-up gets a plain colour field behind it
  instead of screentone; bark goes smooth instead of cross-hatched. This is exactly the
  "not good enough / stumpy" complaint from Volume 1, and it is why Volume 1 read as cheap.
- **medium** restores all of it — halftone screens, cross-hatching, background texture. On a
  six-panel dialogue page it is very hard to tell from `high`.
- **high** adds a little more depth in backgrounds and slightly finer line detail. It is worth
  it where one image carries the whole page and nowhere else.

## Finding 3 — resolution is a separate lever, and a big one

The API rejects arbitrary sizes but accepts a fixed list, which includes **2160x3840** — the
same 9:16 portrait shape we already use, at **3.5x the pixels** (8.3 MP vs 2.36 MP).

At `medium`/2160x3840 the halftone reads as a fine print screen rather than chunky dots, and the
linework is thin and crisp instead of soft. Side by side at native scale, `medium` at 2160 looks
markedly more like printed manga than `high` at 1152 does.

**This is the lever that was actually wanted.** Pushing the tier was buying the wrong thing.

> Caveat not yet resolved: `REP_PRICE` in `genlib.py` is a hardcoded per-tier table, so the
> ledger reports $0.047 for the 2160 image because it was `medium`. Whether Replicate bills more
> for a larger output has NOT been verified against the dashboard. Do that before committing a
> whole volume to 2160.

## Recommended policy

| Page type | Tier | Size |
|---|---|---|
| Chapter splash, single-dominant-panel page | `high` | 2160x3840 |
| Fight beat, emotional close-up page | `medium` | 2160x3840 |
| Standard dialogue page | `medium` | 2160x3840 |
| Montage / object / establishing fragments | `medium` | 1152x2048 |
| anything | ~~`low`~~ | never — it is what made Volume 1 look cheap |

Est. for a ~110-page volume: **~$6**, versus $12.37 for Volume 3 at 90% `high`/1152 — and it
should look better, because the pixels are where the gain is.

## Cost of this test

10 images, $0.60.
