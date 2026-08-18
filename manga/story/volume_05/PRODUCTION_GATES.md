# Volume 5 production gates

This file assigns production responsibility. It does not replace the source-truth ledger or the
chapter `name`; it prevents a generated draft from becoming an approved page without evidence.

## Roles and handoffs

| Role | Receives | Must deliver | Cannot approve |
|---|---|---|---|
| Source editor | Local source, two chapters before and after | Immutable beats, state, permitted compression, end effect | New plot or knowledge |
| Chapter writer | Source truth and volume engine | Final dialogue, scene pressure, page/spread `name` | Its own source-effect comparison |
| Script reviewer | Source range and completed `name` | Page-specific pass/fail notes and source-effect verdict | A draft it authored |
| Generation worker | Approved manifest and ordered refs | One staged raster plus first-pass defect report | Production `raw/` page |
| Page QA reviewer | Manifest, storyboard, prior/next page, original raster | Pass or exact defect by panel | A page from its own generation task |
| Chapter reader | Approved full-size pages and source context | Sequential comprehension, causality, dialogue, continuity verdict | A chapter with an open material defect |
| Coordinator | All records | Corrected approved pages, provenance, normalized chapter | A volume by sampling or worker summaries |

## Pre-generation gate

Every chapter needs all of the following before a builder is written:

1. source line range and context read;
2. continuity in/out state;
3. scene objectives, resistance, reversal, and end effect;
4. exact final dialogue and SFX;
5. page/panel `name`, balloon order, speaker, tail, and placement;
6. action geography and technique-origin ledger where applicable;
7. source comparison by someone other than the writer; and
8. context-clean reader pass.

Every chapter also reserves readable negative space on Page 1 for the exact in-page marker
`CHAPTER <N> — <TITLE>`. Its placement is part of the `name` and receives the same exact-text QA as
dialogue. PDF outline bookmarks do not replace the printed chapter marker.

## Page review record

No checkbox may be inferred from the worker's report. The reviewer opens the original image and
checks the preceding and following pages when they exist.

| Check | Pass condition |
|---|---|
| Cast and design | Only specified people; correct age, outfit, eyes, weapons, injuries, proportions |
| Panel contract | Required panel count, order, focal panel, gutters, and page-turn beat are readable |
| Dialogue | Exact text, correct page/panel, one occurrence, spelling/punctuation, correct tail or off-panel form |
| SFX and captions | Exact required form; no invented readable text; do not obscure story information |
| Blocking | Positions, facing, eye-lines, movement direction, and landmarks match the `name` |
| Action cause | Preparation and physical origin are visible; effect begins at the correct mouth/eye/palm/weapon/ground |
| Action result | Trajectory, contact/counter, damage, resource cost, and final positions are intelligible |
| Continuity | Prior-page state is inherited and next-page state is possible; no silent reset |
| Style/readability | Modern high-detail Shippuden-era colour-manga feel; clear silhouettes and reading order |
| Source effect | Page advances the approved cause, choice, relationship, or consequence without inventing an outcome |

The reviewer records `PASS` or `FAIL — panel N: <observable defect>`. “Looks fine” is not a review.

## Correction loop

1. A generation worker may make one targeted edit when the defect is clear.
2. If it still fails, the coordinator decides whether the cause is the prompt, reference pack, or
   render. Correct the cause before assigning a fresh attempt.
3. The corrected page returns to page QA with the original defect attached.
4. The reviewer verifies both the correction and that unrelated page facts did not regress.
5. Repeat until pass. If no compliant page can be produced, stop the chapter as blocked and report
   the exact page, requirement, attempts, and remaining failure.

There is no production advantage to knowingly accepting a material defect. Free retries remove the
old cost pressure, but they do not remove the need to diagnose why an attempt failed.

## Chapter and volume gates

After every page passes individually, a reviewer who did not generate the chapter reads every page
in order at full size, using a contact sheet only to navigate. The reviewer must be able to answer:

- Who wants what in each scene, and what changes their tactic?
- Who performs every action, from what physical origin, toward what target, with what result?
- Which line belongs to which speaker, and does any required line move to another page?
- Where is everyone before and after each exchange?
- What damage, weapon, eye, chakra, clothing, location, and relationship state carries forward?
- Does the chapter produce the same source end effect without relying on the adaptation notes?

Every failed page is corrected and the chapter is reread. After all chapters pass, a separate cold
reader performs the same full-volume sequence check and boundary audit. Only then may the PDFs be
assembled. The owner is the reader, not the QA layer.

## Volume 4 lesson carried forward

The Kiri battle demonstrated the failure mode: attractive pages were accepted even when attack
origins, speaker attribution, page placement, action geography, and carryover were wrong or unclear.
The correction is forward-only. Volume 4 remains finished; Volume 5 uses explicit storyboards,
independent page review, correction loops, and chapter rereads before packaging.
