# Volume 5 — review after the STYLE V5.2 re-render

Three independent read-only gates viewed all 232 pages at full size against their builders and
drafts. Nothing here was regenerated: the Replicate budget was spent (~$25.30 of $26).

## The style change worked

The reader's complaint was that the art "looks more like a colour book than a manga". The cause was
two lines in `genlib.STYLE` telling the model to keep backgrounds LIGHTER and MORE MUTED than the
figures; it complied by leaving them as pale sepia line-sketch behind flat-filled characters.

After the rewrite, backgrounds are fully painted and lit with the figures on essentially every page.
Only four pages still show the old look — **ch02 p15, ch02 p09, ch02 p08, ch05 p02**, plus one
arguable case (ch06 p08's infant inset, which may be an intentional outline symbol). Deliberate
empty panels — flat colour field, black void, screentone, speed lines — are correct by design and
were not counted as regressions.

## What the re-roll cost

Re-rendering re-rolls every page, so pages that had already passed review came back with new flaws.
The dominant new failure mode is **lettering**: doubled words stamped over themselves, dropped
words, and balloons that vanished entirely. This is the class a reader cannot ignore, and it is the
right place to spend the next credit.

**Clean pages: roughly 102 of 232.** ch01 14/16 · ch02 4/16 · ch03 7/16 · ch04 10/18 · ch05 4/10 ·
ch06 6/16 · ch07 8/24 · ch08 9/20 · ch09 9/18 · ch10 10/18 · ch11 9/17 · ch12 7/20 · ch13 5/13.

## Fix list, worst first

Tier is the page's quality setting, which is what a re-render of it would cost
(low $0.012 / medium $0.047 / high $0.128).

### 1. Garbled, doubled or missing lettering
| Page | Defect | Tier |
|---|---|---|
| ch08 p06 | Balloon wrecked: ENOUGH dropped, two ink blobs where words should be, stray glyphs | low |
| ch09 p17 | "THE **A** ADVISERS LIKELY COPIED THEM **DURNG DURNS** THAT WEEK." | low |
| ch07 p16 | "NEVEE / NOTICED." — NEVER stamped twice, and the word YOU missing | low |
| ch12 p01 | Koharu's balloon "STAND WHERE YOU WERE SUMMONED." absent entirely | high |
| ch04 p11 | Balloon "IF YOU TRY ANYTHING, I WILL MAKE YOU REGRET IT." absent entirely | medium |
| ch13 p18 | Kurenai's balloon "WHEN DID YOU LAST LOOK THIS HAPPY?" absent | low |
| ch04 p10 | DOES rendered as broken half-letterforms overprinted on the line above | low |
| ch11 p09 | A whole balloon printed twice on the page | medium |
| ch03 p12 | "WITH ALL DUE RESPECT" renders ALL as TILL | low |
| ch10 p03 | "LEAVES **LEAE**" — half-printed a second time | low |
| ch10 p16 | "JIRAIYA **DISAFPEARS**" | low |
| ch08 p14 | "YUKIMARU'S **NOTHER**." | low |
| ch07 p20 | "**YOUJR** OPENING." | medium |
| ch13 p12 | "**ADMIT'TED**" — stray tick splits the word | medium |
| ch13 p13 | Dropped word "I" plus ghosted overprint | low |
| ch06 p05 | "**WITĪ** MY FISTS." | low |

### 2. Wrong or duplicated characters
| Page | Defect | Tier |
|---|---|---|
| ch11 p09 | Two identical Narutos seated side by side | medium |
| ch06 p04 | Two Narutos in one panel; the foreground face is a melted smear | low |
| ch05 p04 | A second blond figure in the same armour in a solo panel | low |
| ch05 p06 | A second blond head fused into Naruto's profile | low |
| ch12 p03/p04/p05/p09/p11/p13/p16 | West arc grows a fourth seat; Koharu or Homura duplicated | low–med |
| ch07 p11 | "Ghosted phases" drawn as eight solid figures | medium |
| ch07 p08 | Kidōmaru drawn with two arms instead of six | low |

### 3. Reading order (answer before question)
ch11 p02 · ch11 p04 · ch11 p16 · ch11 p17 · ch11 p03 · ch11 p10 · ch13 p09 · ch13 p11 · ch13 p14 ·
ch08 p01 · ch08 p05 · ch08 p08 · ch08 p17 · ch09 p04 · ch09 p10 · ch09 p12 · ch07 p04 · ch07 p08 ·
ch07 p09 · ch07 p14 · ch07 p24 · ch06 p14 · ch03 p13 · ch04 p03 · ch04 p10 · ch04 p16 · ch05 p05 ·
ch05 p10 · ch10 p08 · ch12 p17

Two are worth doing first because they damage a focal beat: **ch06 p14**, where Kushina's closing
"I LOVE YOU. I ALWAYS WILL." is read third from last, and **ch09 p10**, a silent page whose walk to
the house is read after he has already gone inside.

The mechanism is known and documented in `AGENTS.md`: a panel that renders taller or wider than
intended swallows its neighbours, and appended prose never beats it — only a body-level layout edit
does. Where two balloons keep swapping sides, stacking them by height survives the mirroring.

### 4. Continuity worth fixing
- **ch07 p21** — the chapter's key page; the active eye reverts to ordinary blue on the closing line.
- **ch09 p01** — Ōnoki drawn bald and beardless, contradicting his ch07 design.
- **ch04 p01** — the Kiri street is night-lit and Edo-style in an instant that is daylight either side.
- **ch01 p16** — a lit village below, which the page explicitly forbids.
- **ch03 p01 / p02** — Sharingan renders as a plain red disc with no tomeo.
- **ch06 p08 / p12** — Kushina's dissolution resets, then stalls.
- **ch08 p12** — blood on the evidence shard, against the page's own violence rule.

## Two process bugs found and fixed
- `runner.py` treated a 0-byte PNG as a finished page, so a page killed mid-write would never come
  back. It now re-renders empty files and writes atomically via a temp file.
- `spend.py` under-reported by about $8 after the ledgers were reset, and ledger sums run roughly a
  dollar light anyway because retries and refusals never reach a ledger. The baseline is now
  calibrated to the owner's real balance, with a comment saying to trust the balance, not the sum.
