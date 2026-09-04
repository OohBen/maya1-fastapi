# MAI-Image-2.6 / 2.6-flash (Azure) — evaluation

**Status: evaluated, not adopted.** Backend kept at `manga/mai.py` so the findings are not lost.

## Access

- Endpoint base: `https://<resource>.services.ai.azure.com/mai/v1/`
- Auth header is **`api-key`**, not `Authorization: Bearer`.
- Model ids that work: `MAI-Image-2.6` and `MAI-Image-2.6-flash` (both on the same path).
- Rate limit 2 requests/minute on 2.6; flash tolerated a ~5s gap in testing.
- Key lives in `manga/.env` (gitignored) as `MAI_KEY` / `MAI_ENDPOINT`.

## Endpoint quirks — these matter

| Behaviour | `/images/generations` | `/images/edits` |
|---|---|---|
| `size` respected | **No** — always returns 1024x1024 | **Yes** — 1024x1536 confirmed |
| Reference images | not supported | yes, **multipart/form-data**, max **5 files** |

A manga page needs tall portrait and reference images, so **all real work must go through
`/images/edits`**, passing references even when there is nothing to "edit". Using the obvious
generations endpoint silently produces square pages.

The 5-file cap is a real constraint: our pages bind 6-10 references. `mai.py` triages — character
sheets kept, environment plates dropped first, since environments are the most recoverable from
prose alone.

## What was good

- **Reference adherence was excellent.** In a two-character test, Jiraiya and Naruto both came back
  correct and clearly distinct — no bleed, no merging. That is the exact failure mode Muse could
  not hold without heavy prompt engineering.
- **The house look was liked by the owner** — a soft, clean, full-colour anime finish with real
  depth in the backgrounds. Noted as close to the target style, and worth chasing on whichever
  backend ends up doing production.

## Why it was not adopted

**Content filtering blocks ordinary pages.** Volume 5 ch03 p14 — four characters holding a
conversation in a street, with no violence and nothing sexual anywhere in it — was refused under
`MultiSeverity_SexualScore`, deterministically, on every attempt, on both 2.6 and 2.6-flash.

The refusal appears to be a false positive driven by wording, not by content. **That does not make
rewording the right fix.** The words carrying the most weight were the ones establishing that a
character is sixteen, and building tooling that strips age markers until a sexual-content
classifier stops firing is a bad pattern regardless of how innocuous the underlying page is: the
same tooling would conceal a genuine problem if one ever arose. An attempt to build exactly that
was abandoned, and the script deleted.

**The supported response to a refusal is to render that page on another backend.** The project
already has two working generators; a refused page costs nothing but a re-route.

Ordinary rewording that is not about age — for example "tight two-shot" to "close framing on both
figures" — is fine and remains available, but it did not need to be systematised.

## Open questions if this is revisited

- Per-image cost on this Azure deployment is unknown and was never established.
- What fraction of the 232-page volume the filter refuses was never measured, because measuring it
  was not worth the direction the work was heading.
