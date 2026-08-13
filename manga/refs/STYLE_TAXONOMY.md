# Style reference library — taxonomy

583 colored Naruto pages (vols 1–3) in `refs/style/`. Volumes 1–3 chosen deliberately: they are
village/academy/childhood material, which matches our Volume 1's content, and they are free of
the giant glowing chakra effects that dominate late volumes (those would teach the exact
painterly glow we are trying to eliminate).

A sampled subset is labelled so `build_chNN.py` can automatically attach the **best-matching**
style reference to each page instead of the same generic one every time.

## What these pages teach that our prompts could not

Observed by reading pages directly. Every one of these is a way our output currently differs:

| Real colored manga | Our Volume 1 output |
|---|---|
| Thin black panel borders on **white paper ground** | Panels bleed full-dark to the page edge |
| **Flat colour fills**, one solid tone per area | Soft ambient gradients everywhere |
| **Halftone/screentone dots** in shadow areas | Smooth airbrushed shadow |
| **Parallel-line hatching** for shadow and motion | Rendered soft falloff |
| **Speed lines / impact lines** as graphic elements | Photographic motion blur |
| Backgrounds often blank white or one flat colour | Every background fully rendered |
| Simple faces — dot eyes, minimal nose | Semi-realistic anime faces |
| Print-like slightly desaturated palette | Glowing, saturated, cinematic |

## Label schema

Each page gets one JSON record:

```json
{
  "file": "v01_p012.webp",
  "scene": "dialogue | action | establishing | emotional_closeup | crowd | comedy | montage",
  "light": "day | night | interior | flashback | white_void",
  "cast": "none | solo | two | small_group | crowd",
  "panels": 1-9,
  "shot": "mostly_wide | mostly_close | mixed",
  "sfx": true|false,
  "speedlines": true|false,
  "halftone": true|false,
  "mood": "calm | tense | somber | comedic | violent",
  "note": "one short clause describing the page"
}
```

**Field meanings** — keep these strict so selection works:
- `scene` — the dominant activity on the page, not the story context.
- `light` — `flashback` means a desaturated or single-hue tinted page; `white_void` means
  characters on blank white/abstract ground with no drawn environment.
- `cast` — number of *distinct visible characters*, not panel appearances.
- `shot` — whether panels are mostly long shots, mostly faces, or a mix.
- `sfx` — large hand-drawn sound-effect lettering integrated into the art.
- `speedlines` — radial or parallel motion/emphasis lines.
- `halftone` — visible screentone dot texture.

## How the builder uses it

`refs/style_select.py` scores every labelled page against the page being generated and returns
the top match. Weighting: `scene` 3, `light` 3, `cast` 2, `shot` 1, `mood` 1, plus small
bonuses when `sfx`/`speedlines` are requested and present.

The selected page is bound as a **style-only** reference with a hard ignore clause:

> "Image N is a STYLE REFERENCE ONLY. Copy its rendering technique: thin black panel borders on
> white paper, flat colour fills, halftone dot shading, parallel-line hatching, heavy black ink
> linework, simple faces. Ignore absolutely everything else about it — its characters, its
> costumes, its panel layout, its story content and its lettering."

**Known risk:** content bleed. These pages contain canon Naruto, so a style reference can drag
our age-13 design back toward the orange jumpsuit. Test style refs on a page without the
protagonist before trusting them, and check any page that has him for design drift.

## Maintenance — this library must grow with the story

The current library is **volumes 1–3 only**, chosen to match Volume 1's content (village,
academy, childhood). That is deliberate but temporary.

**Before starting each new volume, check coverage and extend.** Later arcs need scene types the
early volumes barely contain:

| Upcoming arc | Scene types the library currently lacks | Suggested source volumes |
|---|---|---|
| Chūnin Exams (Vol 2–4) | tournament crowds, arena wide shots, one-on-one duels | 4–10 |
| Orochimaru / Akatsuki | menace close-ups, dark interiors | 13–17 |
| Nagato / Rinnegan | large-scale destruction, doujutsu close-ups | 24–28 |
| Fourth War | mass battle, mixed casts, huge summons | 55–70 |

Extend with `python3 refs/fetch_style.py <vol> <vol> ...`, re-sample, and label the new pages
into `refs/labels/`. The selector merges every `batch*.json` automatically, so adding files is
all that is required.

**Known coverage weakness right now:** the early volumes are mostly daylight. Volume 1 of our
adaptation is mostly night (festival, alley, hideout). Measure the `light` distribution with
`python3 refs/style_select.py` and pull night-heavy volumes if `night` is thin — a daylight page
cannot teach how this manga renders darkness, which is precisely where our output looks most
like a digital painting.
