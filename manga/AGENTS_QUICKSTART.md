# Quickstart — generating your first chapter

Read `/AGENTS.md` first. This is the shortest path from a clean checkout to finished pages.

## 0. Port the backend (once)

Implement the `codex` branch of `backend.py`, then:

```bash
export MANGA_BACKEND=codex
```

Smoke-test it before anything else — 2 pages, then LOOK at them:

```bash
cd manga
rm -f chapters/v3ch01/raw/p02.png chapters/v3ch01/raw/p03.png
python3 chapters/build_v3ch01.py p02 p03
```

Compare the faces against `refs/images/naruto_13.png` and `refs/images/orochimaru.png`. If they
don't match, your reference images aren't reaching the model — fix that before continuing.
Restore the originals with `git checkout -- chapters/v3ch01/raw/` when done.

## 1. Get the source text

```bash
curl -sL "https://fichub.net/api/v0/epub?q=<fanfiction.net-url>" -o fic.zip
```

Unzip, split the HTML on chapter headings, write `chNN.txt` per chapter into a scratch dir.
Volume 4 needs fic chapters 8–11.

## 2. Add any new characters

New cast goes in `chapters/prompts.py` as a binding, and in `refs/build_refs.py` as a sheet.
**Lead with the silhouette-defining feature** — the one shape that identifies them at thumbnail
size. "Long black hair" produced a generic old wizard for Madara; "an ENORMOUS wild mane that
flares outward in huge jagged spikes" produced Madara.

```bash
python3 refs/build_refs.py v4cast1     # builds a named batch
```

Volume 4 needs: `tsunade`, `shizune`, `homura`, `koharu`, `mei`, `env_funeral`,
`env_kiri_village`, `env_tsunade_bar`.

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

```bash
python3 chapters/build_v4ch01.py p01 p02 p03 p04 p05   # first five
# LOOK AT THEM. Fix prompts. Then:
python3 chapters/build_v4ch01.py                        # the rest (skips existing)
python3 pack_chapter.py v4ch01 "The Professor"
```

Failures print `[FAIL] pNN` and do not abort the chapter. Re-run to retry just those.

## 5. Assemble the volume

Copy `assemble_v3.py` to `assemble_v4.py`, update `CHAPTERS`, then:

```bash
python3 assemble_v4.py
```

Produces `volume_04/Volume_04.pdf`, a contact sheet, and a README with real page counts.
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
