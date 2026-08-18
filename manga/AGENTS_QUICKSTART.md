# Quickstart — generating your first chapter

Read `/AGENTS.md` first. This is the shortest path from a clean checkout to finished pages.

## Current handoff

Volume 5 writing/storyboard preproduction is complete: 13 chapters, 232 scripted pages, and 1,327
planned panels. The review record and approved ten-page pilot are in `story/volume_05/`. Production
is stopped until the owner explicitly says to start producing. Once authorized, audit the missing
references, write the first builder, and run a 3–5-page visual probe before any larger batch. The
Volume 4 commands below are tested examples of the transport, not permission to regenerate it.

## 0. Choose the generation transport

The ordinary Python runner uses the configured HTTP backend. The native Codex ImageGen tool is
not callable from `backend.py`; its `codex` branch remains intentionally unavailable. For native
tool generation, validate the builder and export a tool manifest instead:

```bash
cd manga
python3 validate_chapter_specs.py chapters/build_v4ch01.py --expected-pages 16 \
  --extra-ref-root refs/images
python3 export_codex_manifest.py chapters/build_v4ch01.py /tmp/v4ch01_manifest.json \
  --style-ref refs/images/style_v01_p094.png --ref-root refs/images
```

The native tool accepts at most five image paths. The exporter reserves the last for the shared
style page and automatically packs logical content refs beyond four into an ordered composite
plate, rewriting their prompt bindings to tile bindings. Preserve manifest order exactly.

## 1. Get the source text

```bash
python3 story/source/fetch_source.py
```

This retrieves the FicHub EPUB, validates all 50 sequential chapter files, and writes the local
working copy under ignored `manga/.source/`. Volume 4 uses fic chapters 8–11; Volume 5 uses fic
chapters 12–16, with chapters 10–11 and 17–20 read for boundary context. To work offline, pass an
existing EPUB with `--epub /path/to/story.epub`.

## 2. Add any new characters

New cast goes in `chapters/prompts.py` or the volume prompt module as a binding, and in
`refs/images/` as a generated sheet.
**Lead with the silhouette-defining feature** — the one shape that identifies them at thumbnail
size. "Long black hair" produced a generic old wizard for Madara; "an ENORMOUS wild mane that
flares outward in huge jagged spikes" produced Madara.

Volume 4's additions and exact page bindings are in `chapters/prompts_v4.py`; validate that every
named reference resolves before generation.

## 3. Write the chapter

Copy `chapters/build_v3ch01.py` as the template — it is the most current. For each page supply:

```python
("p01",                                            # page id
 dict(scene="dialogue", light="dark", cast="two",  # style-selector query
      mood="tense", panels=6),                     # panels=1 switches to SPLASH
 FILL + N13.format(i=1) + ORO.format(i=2)          # bindings, numbered to match R(...)
 + ONLY(BOY, PALEONE) +                            # the COMPLETE cast
 "SIX panels, uneven.\n"
 "PANEL 1 (small): ...\n"                          # every panel, with shot size
 + SAY((1, PALEONE, "upper left", "LINE.")),       # every balloon
 R("naruto_13", "orochimaru"),                     # refs, SAME ORDER as bindings
 "medium"),                                        # tier
```

**Write and read the entire chapter's dialogue before generating anything.** The model letters
the page, so a wrong line means re-rendering it.

Then audit every page: is each name in `ONLY()` and in the panel text also in `R(...)`? If not,
either bind it or make it generic.

## 4. Generate, review, finish

For native generation, send the first five manifest rows to separate bounded workers. Each worker
uses the row's exact prompt and ordered refs, returns one raster, and writes no shared ledger state.
The coordinator inspects the five pages individually and as a sequence before dispatching the rest.

After review, normalize approved pages to the manifest's `1152x2048` target, place them in
`chapters/v4ch01/raw/`, write provenance serially, then package:

```bash
python3 pack_chapter.py v4ch01 "The Professor"
```

For the HTTP backend, the existing `python3 chapters/build_v4ch01.py p01 ...` runner remains the
resumable path and skips existing outputs.

## 5. Assemble the volume

Use `assemble_v4.py` as the template for later volume assemblers, update `CHAPTERS` and output
names, then:

```bash
python3 assemble_v4.py
```

Produces `volume_04/Volume_04.pdf`, `volume_04/Volume_04_compressed.pdf`, a contact sheet, and a
README with real page counts. Both PDFs must include nested chapter outline bookmarks; the
compressed reading copy keeps the same page dimensions as the master.
If the PDF exceeds a delivery size limit, copy `volume_03/make_parts.py` to split it.

## Common failures and their causes

| Symptom | Cause |
|---|---|
| Wrong character drawn | Name used but not bound in `R(...)` |
| Splash came back as a panel grid | `panels=1` missing from the style query |
| Balloon tail points at the wrong person | Speaker not drawn in that panel — wrap in `OFF()` |
| Naruto looks canon (orange, spiky, grinning) | `ALT` clause missing from the binding |
| Characters look like small children | Binding states age but not height/build |
| Misspelled invented English on a sign | Didn't ask for "ILLEGIBLE SCRIBBLE" |
| Page is soft and smeary | `low` tier at 2160×3840 — never pair those |
