# Legacy — Volume 1 only

Nothing here is used by the current pipeline. It is kept because Volume 1's finished pages were
produced with it and the chapter files would not otherwise be reproducible.

- `letterer.py` — deterministic lettering: flood-fills near-white balloon blobs, fits text into
  them, and writes the result. Superseded from Volume 2 onward, where the **model draws the
  dialogue itself** (see PIPELINE.md, "the lettering reversal"). Model-drawn lettering integrates
  balloon shape with art and reads far better; the tradeoff is that a wrong line costs a full
  page re-render, which is why dialogue is now finalised before any page is generated.
- `letter_ch01.py` … `letter_ch09.py` — the per-chapter lettering passes for Volume 1.

If you ever need deterministic lettering again (e.g. for a translation pass), `letter_page()`
still works. Two defects were fixed in it and are worth knowing about: `fit_text` originally
checked only height so long tokens overran balloons, and band-sorting used a fixed page fraction
which silently swapped speakers on pages with unevenly-placed balloons.
