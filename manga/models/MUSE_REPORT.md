# Muse Image — evaluation for this project

**Verdict: do NOT switch. Stay on gpt-image-2.** Muse is 4.7x cheaper and produces a more
authentically *manga-looking* page, but on a controlled blind comparison it produced **55 defects
to gpt-image-2's 20** across the same 10-page chapter, and one of its failure modes is
disqualifying for this project.

## The test

Volume 5 chapter 5, all 10 pages, rendered by both systems from **identical page scripts and
identical character reference sheets**. Both sets were then scored by a reviewer that was not told
which system produced which, against the chapter draft and the build spec, counting defects by
category.

| Category | gpt-image-2 | Muse |
|---|---:|---:|
| Lettering | 3 | 15 |
| Cast correctness | 2 | 5 |
| Reading order | 2 | 6 |
| Continuity | 11 | 11 |
| Art finish (unfinished backgrounds) | **0** | **8** |
| Anatomy | 1 | 3 |
| Panel count / layout vs spec | 1 | 7 |
| **Total** | **20** | **55** |

Pages needing regeneration rather than touch-up: gpt-image-2 **0**, Muse **at least 3**.

## Why it fails here specifically

1. **It invents dialogue.** On a page whose spec reads "that single caption box is the ONLY text
   anywhere on this page", Muse dropped the required caption and wrote five lines of its own,
   including a thought balloon and two speeches by characters not permitted on the page. In this
   project the dialogue is written, reviewed and final before a page is ever drawn. A generator
   that writes its own lines cannot be trusted with a script.
2. **It leaves backgrounds unfinished on 8 of 10 pages** — grey uncoloured line-sketch behind
   fully-coloured figures. That is the exact "looks like a colouring book" problem the owner
   rejected, and gpt-image-2 after the V5.2 restyle scores zero on it.
3. **It rewrites the layout.** 7 panel-count/layout deviations against the spec, versus 1.

## What is genuinely better about it

Stated plainly, because these are real and worth stealing rather than dismissing:

- **$0.01 flat per image**, regardless of reasoning strength, versus $0.012 / $0.047 / $0.128.
  A 232-page volume costs ~$2.30 instead of ~$8.40. Retries are nearly free.
- **Real manga page furniture** — cream paper stock, halftone screentone fields, radial focus
  lines, black voids. Its pages *read* like printed manga; ours *look* more expensive.
- **It staged several beats better** than our version: a near-contact focal close-up our render
  re-opened, and a departure long-shot resolving three silhouettes cleanly.
- **Fast**: ~40s a page, 10 pages in parallel in about a minute.

## Techniques found while tuning it (worth keeping)

- **Caption each reference image inline.** The `images/edits` endpoint takes an unlabelled array, so
  binding relies on "Image {i} is..." text thousands of characters away — that is how Jiraiya and
  Kakashi fused into one character. The Responses API allows interleaved text and images, so each
  caption sits immediately before its own picture. This alone stopped the merge.
- **Never hand a model a multi-state reference sheet.** `sharingan_progression.png` shows four eyes
  including a *blue* one; feeding it while asking for a red Sharingan is why the eye kept coming
  back blue. Single-state crops (`eye_3tomoe`, `eye_mangekyo`, ...) fixed it.
- **Describe what you want, not what you don't.** "Not a thin white thread" produced thin white
  threads. Specifying a solid black triangular spike produced solid black spikes.
- **Hoist the load-bearing constraints.** Eye state and panel count sat at 36% into a 20k-character
  prompt and were ignored; restated in a HARD CONSTRAINTS header at the top, they were obeyed.
- **The safety filter is probabilistic, not a hard block.** 5 of 9 of the volume's most violent
  pages were refused on first attempt; every one cleared within two retries.
- **Undocumented limits**: the Responses API rejects the `size` field the docs list (it returns
  1152x2048 anyway), and a request carrying nine full-size reference sheets exceeds a ~26MB cap —
  downscaling references to 768px fixes it with no loss, since they are only identity cues.

## What transferred back to the production pipeline

The multi-state-reference finding applies to our own pipeline: **no gpt-image-2 page bound an eye
reference at all**, which is why review gates kept reporting "a plain red disc with no tomoe" and
"the eye reverts to blue". Binding the new single-state `eye_3tomoe` sheet on ch05 p06 turned a
tomoe-less red disc into a correct three-tomoe Sharingan on the first try.

`EYE_3TOMOE` is now defined in `chapters/prompts_v4.py` and bound on ch05 p06 as the proof. Applying
it to every page whose prose asks for an active Sharingan is a ready-to-run improvement, pending
credit.

## Cost of the evaluation

$0.66 of Muse credit (66 images), $0.012 of Replicate for the transfer test.
