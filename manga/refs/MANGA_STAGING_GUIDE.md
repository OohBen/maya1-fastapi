# Manga staging & composition guide

Practical conventions extracted from the colored Naruto reference set in `refs/style/`
(1119 pages, vols 1, 2, 3, 5, 6, 7). This document is about **staging** — where things go,
how deep the space is, where the camera is, what fills the background. It assumes surface
rendering (halftone, flat fills, borders, linework) is already handled elsewhere;
see `STYLE_TAXONOMY.md` for that.

**Every claim below is either (a) an automated measurement over all 1119 pages, or (b) a hand
observation from 42 pages I read directly.** Automated numbers are marked *[auto]*, hand
observations cite page filenames. Where the sample doesn't support a confident number I say so.

Pages read directly (42, all six volumes):
`v01_p016 p019 p034 p053 p061 p112 p145` ·
`v02_p010 p028 p046 p064 p130 p169` ·
`v03_p040 p077 p092 p120 p150 p195` ·
`v05_p046 p065 p087 p109 p144 p150 p152 p174` ·
`v06_p031 p039 p047 p059 p092 p111 p122 p134` ·
`v07_p013 p038 p058 p070 p091 p143 p153`

---

## 0. The one-line diagnosis

Illustrations put figures **in front of** a scene. These pages put figures **inside a stack of
depths**, and then crop that stack with the panel edge. Almost every anti-AI trick below is a
variant of two moves:

1. **Put something big and partial in the extreme foreground**, usually cropped by the panel edge
   and usually not the subject (a shoulder, a leg, a hat brim, a corpse, a hand).
2. **Put the actual subject small, or turned away, or both.**

---

## 1. Page architecture

### Panel count
*[auto, all 1119 pages; panel detector validated against 42 hand counts — MAE 0.88, exact on
22/42, so read these as ±1]*

| Panels on the page | Share of pages |
|---|---|
| 1–2 | 21.6% |
| 3–5 | 30.8% |
| 6+ | 47.6% |

Mean 4.94, median 5, mode 6. **Six to nine panels is the normal page**, not three or four.
Directly counted examples: 9 panels (`v01_p061`, `v03_p040`), 8 (`v03_p092`, `v03_p120`,
`v06_p059`, `v07_p038`), 6 (`v05_p087`, `v06_p111`, `v07_p058`, `v07_p143`),
4 (`v05_p144`, `v05_p150`, `v06_p031`), 3 (`v02_p064`), 2 (`v05_p174`),
1 (`v02_p046`, `v05_p046`, `v05_p152`, `v06_p047`, `v06_p122`).

### Panels on a page are wildly unequal in size
*[auto]* Median within-page coefficient of variation of panel area is **0.60**. Translation:
on a typical page the biggest panel is roughly 4–8× the area of the smallest.

- The largest panel on a page is a median **32%** of the page (mean 41%).
- On **27%** of pages one panel occupies **>55%** of the page.
- On **15%** of pages one panel occupies **>70%** — a splash or chapter opener.

**Rule: give every page one clearly dominant panel and let the rest be small.**
`v02_p064` = one huge close-up (~62% of page) + two small scenery panels.
`v05_p144` = one huge menace close-up (~60%) + a row of three small ones.
`v06_p031`, `v07_p153`, `v07_p143`, `v05_p150`, `v03_p150` all follow the same shape.

### Panel shape
*[auto, 5525 panels]*

- Individual panels: **29% wider than tall, 48% taller than wide, 23% roughly square.**
  Most panels are tall because rows get split 2–3 across.
- **The largest panel on a page is usually wide: 53% wide vs 24% tall.**
- **6.2%** of all panels are letterbox (AR > 2). Seen directly: the eyes-only strip in
  `v01_p034` (~4:1), the snake-head strip in `v06_p039`, the melee frieze in `v07_p153`
  (~3:1), the floor-level shot in `v05_p065`.

So: **wide for the hero beat, tall/narrow for the reaction beats.**

### Irregularity, insets, borderless, bleed

Honest limits: the scans in this set are trimmed to the artwork, not to the physical page, so I
**cannot** give a reliable automated bleed rate. What I can say:

- *[auto]* **67%** of pages have a clean white paper margin all the way round;
  **1.7%** of pages invert it entirely to a **black page ground with white-bordered panels
  floating on it** — confirmed by eye on `v06_p134`, and the detector flags clusters at
  `v01_p007`, `v02_p072–075`, `v03_p049–062`.
- Full-bleed borderless splashes exist and are borderless *completely* — no frame anywhere:
  `v05_p046` (crowd), `v06_p047` (chapter opener), `v01_p053` (clone army).
- A "full page panel" usually still keeps **a sliver of white paper on one side**:
  `v06_p122` bleeds off top, right and bottom but leaves a thin white strip at the left.
- Borderless with white: `v02_p046` is ~80% blank paper with one figure at the lower right,
  cropped by the page edge, no frame, no ground, no shadow.
- Rows are usually not aligned column-to-column between rows: `v03_p120`, `v06_p059`,
  `v07_p038` all change the number of columns from row to row (3 / 3 / 3 with different widths,
  or 2 / 3 / 2).

Practical prompt target: **one page in six or seven should have a panel that runs off a page
edge; one page in seven or eight should be a single dominant panel; roughly one chapter opener
in two should be fully borderless.**

### Reading order
In this scan set the panels read **left to right** (English release order) while SFX and some
vertical Japanese type are retained (`v07_p143` row 2, `v07_p153` row 2, `v07_p038`). Don't try
to build right-to-left page logic from these files.

---

## 2. How groups of characters are arranged

This is the section that fixes the "everyone in a row facing camera" failure.

**In 42 pages I did not see a single panel where three or more characters stand in a line at the
same depth, evenly spaced, all facing the camera.** Not once. The arrangements are:

### 2.1 The depth stagger (the default two- or three-shot)
Characters occupy **different depths and radically different scales inside one panel**.

- `v06_p092` panel 1: speaker huge in the right foreground (~60% of panel height, cropped by the
  right and bottom edges); the other character tiny (~8% of panel height) embedded in the rock
  face at the far left. Balloons in the empty middle. This is a *quiet conversation*.
- `v02_p169` panel 3: crouched figure large in the left foreground; a body lying midground;
  two characters standing far right at ~25% of the foreground figure's height.
- `v03_p077` row 2: a face cropped by the left panel edge showing only one eye and some hair
  occupies the left quarter; a tiny full figure stands deep in the forest at the lower right.
- `v07_p013` panel 4: foreground figure ~45% of the panel, cropped by the left and bottom edges;
  target figure running in the distance at roughly 1/6 the size.
- `v02_p010` panel 6: three faces at three different scales and depths, the third one *below and
  in front of* the other two, overlapping them.

Scale ratio between nearest and farthest character in the same panel is routinely **4:1 to 10:1**.

### 2.2 Somebody is always cropped by the panel edge
Typically the *nearest* figure, and typically we see only a fragment of them:

- `v07_p058` panel 1: the extreme foreground is a character's **back, hip and pouches**, cropped
  by the top and left edges — we never see his face. Behind him, tigers and a second figure
  cropped by the right edge. Behind them, a tiny figure walking up a path (~4% of panel height).
  **Four depth layers, nobody facing camera, two of three characters cropped.**
- `v05_p174` panel 1: four characters — one crouched left foreground, one standing midground
  turned away, one huge in the right foreground seen from behind and cropped by the right and
  bottom edges (only hat, shoulder and back), plus a fourth cropped by the left edge (an arm).
- `v06_p134` panel 3: an arm and a hand holding a strap enter from the left edge; that's the
  entire foreground character.
- `v05_p046`, `v05_p087` panel 2, `v07_p143` row 3, `v05_p109` panel 6 all do the same.

### 2.3 A large share of characters are turned away
Back-of-head and over-shoulder framings without a visible face are extremely common — I counted
**13+ instances across the 42 pages**, i.e. most pages have at least one:

`v01_p016` (both characters from behind, twice), `v01_p112` bottom panel (three characters seated
in a row *seen from behind*, unevenly spaced, plus a fourth standing far off),
`v03_p077` last panel, `v03_p120` panels 2 and 4, `v05_p109` panel 3 (over-the-shoulder where the
foreground head fills the centre of the frame), `v07_p038` panel 3 (head turned away, only hair
and neck), `v07_p153` panel 1 (a dozen clones, most seen from behind).

### 2.4 Crowds
Two recipes only:

**(a) Bird's-eye scatter with silhouettes.** `v07_p143` panel 1: extreme high angle, the three
protagonists tiny at the exact centre in colour, ~20 enemies drawn as **flat black silhouettes**
with almost no interior detail, scattered at irregular positions in different poses and
rotations, at four or five depths, several cropped by the panel edge. The ground is fully drawn
and visible between them. `v03_p092` panel 2 is the domestic version: eight characters around a
table from ~60° above, all at different orientations, none facing camera, several occluded by
the table.

**(b) Packed overlapping mass, camera inside it.** `v05_p046`: camera at head height *within* the
crowd, tilted; nearest figure cropped to hair and a shoulder; heads overlapping heads at 4–5
receding ranks; **not one of ~25 characters faces the camera frontally.** `v07_p153` panel 1 and
`v01_p053` (clone army, foreground figures cropped by all four edges, mass shrinking to specks at
the horizon) are the action version.

For a melee, drop the environment entirely: `v07_p153` bottom panel is a horizontal frieze of
interpenetrating orange and black figures, all cropped top and bottom by the panel edge, over a
background of nothing but **flat blue horizontal speed-line bands**.

### 2.5 Balloons are part of the staging
Balloons routinely take **40–60% of a panel's area** and the figure is pushed low and to one
side to make room. `v01_p112` panel 5 (balloons fill the upper-left ~60%, character seated small
at the right), `v06_p111` panel 1 (two balloons fill the top 60%, character at the bottom edge),
`v07_p091` panel 3, `v03_p092` panel 1, `v06_p092` (balloons occupy the empty middle *between*
the two characters and thereby define the depth gap).

**Rule: leave a deliberate empty shelf, usually the top third, for lettering; never centre the
figure in the panel.**

---

## 3. Camera

Hand tally across 42 pages (instances, not percentages — the sample is too small for percentages):

| Camera | Observed | Examples |
|---|---|---|
| Extreme high / bird's-eye | ~8 | `v01_p053`, `v01_p061` p1, `v03_p092` p2 & p7, `v05_p087` p3, `v05_p109` p6, `v07_p143` p1, `v02_p130` p5 |
| Extreme low / worm's-eye | ~4 | `v06_p031` p1 (looking up at a chin and throat, head cropped by the panel top), `v05_p065` p2 (camera on the floor), `v03_p092` p6, `v01_p019` p2 |
| From behind / over-shoulder, face hidden | 13+ | see §2.3 |
| Extreme close-up: one eye, or a face slice | ~9 | `v01_p034` p2 (eyes-only letterbox), `v02_p130` p3, `v06_p059` p5 & p8, `v07_p038` p2 & p8, `v02_p010` p3 (half a face fills the page's biggest panel) |
| Body part only, no face at all | ~7 | `v06_p031` p4 (a hand holding an eye), `v06_p092` p3b–c (a clawed hand; an ankle), `v02_p010` p5 (torso and belt), `v03_p120` p6 (jacket and pouch, head cropped off), `v07_p058` p3a (a bruised shoulder) |
| Very wide with a tiny figure (<10% of panel height) | ~10 | `v01_p061` p1 & p3, `v06_p059` p3, `v07_p070` p2–5, `v07_p091` p1 & p4, `v02_p028` p2, `v03_p092` p7 |
| Tilted / dutch | ~3 | `v05_p150` p1 (whole room tilted ~10°), `v05_p046`, `v06_p047` |

Two more camera facts worth prompting:

- **Foreshortening toward the lens.** A hand, fist or weapon thrust at the camera, drawn nearly
  as large as the head: `v07_p091` bottom panel (both hands forward against flat black),
  `v06_p047` (lunging figure, hand in the lens), `v05_p174` panel 2 (a fist holding a form,
  cropped by the left and bottom edges, as big as the face behind it).
- **Shooting through an obstruction.** `v05_p065` panel 1 puts bystanders' legs at both edges,
  cropped, and the action happens between them.

---

## 4. What is actually in the background

**Hand count: 105 panels across 16 pages I read panel-by-panel — only 33 (31%) had a drawn
environment.** The other 69% were flat colour, halftone tone, blank white, flat black, radial
burst, or speed lines.

Pages counted: `v01_p016` (4/5 env), `v01_p019` (1/6), `v01_p034` (1/5), `v01_p061` (3/9),
`v01_p112` (2/7), `v02_p010` (2/7), `v02_p130` (1/5), `v03_p040` (2/9), `v03_p120` (2/8),
`v05_p087` (3/6), `v05_p144` (0/4), `v06_p059` (2/8), `v06_p092` (2/6), `v07_p038` (0/8),
`v07_p058` (4/6), `v07_p143` (4/6).

**For close-ups specifically it is near-total: `v07_p038` has 8 panels and zero drawn
environments; `v05_p144` has 4 and zero; `v02_p130` has 4 flat out of 5.**

The background vocabulary, in rough order of frequency:

1. **Blank white paper** — no ground, no shadow, no horizon. `v01_p034` p3 (a figure recoiling in
   pure white), `v02_p064` p1, `v02_p046`, `v01_p019` p3–p5, `v03_p077` p2.
2. **One flat colour** — pink, lavender, navy, pale blue, pale green. `v01_p019` p2 (flat pink),
   `v03_p120` p3–p4 & p7 (flat lavender), `v07_p038` (flat blue-grey across a whole page),
   `v05_p087` p2 (flat orange halftone).
3. **Flat black void.** `v05_p144` p1, `v06_p031` p2–p4, `v06_p111` p4, `v07_p091` p6,
   `v05_p174` p2, `v05_p087` p1. Used for menace, isolation and interior monologue.
4. **Radial burst** — straight white or coloured spikes converging on the subject's head.
   `v01_p034` p1 and p5, `v01_p061` p4, `v02_p130` p1, `v05_p109` p5, `v06_p134` p1
   (hard-edged yellow wedges), `v07_p070` p1 (orange bars plus pink rays).
5. **Speed lines as the entire background** — parallel or radial. `v01_p016` bottom panel
   (concentric blue arcs behind a foreshortened hand), `v07_p153` bottom panel (flat blue
   horizontal bands), `v07_p038` bottom-left panel, `v06_p059` p4 (vertical lines plus flying
   rock chips), `v07_p058` row 2 panel a (a narrow panel that is *only* speed lines).
6. **Abstract texture panel** — no scene at all. `v06_p111` p5 is flat cyan with white diagonal
   stripes, yellow stars and repeated katakana as pattern, with a caption box floating in it.
   `v03_p040` p5 is a pale blue field with outlined katakana as wallpaper and two slivers of hair
   cropped at the bottom edge.
7. **Fully drawn environment** — reserved for establishing panels, wide shots and the page's
   dominant panel. When it appears it is genuinely detailed (`v07_p143` p1, `v06_p134` p3,
   `v03_p092` p2, `v06_p092` p1, `v02_p064` p2–p3).

**The empty cutaway panel.** Roughly one page in three has a panel with **no characters at all** —
scenery, sky or an object — used as a beat of silence:
`v03_p092` p3 (moon and clouds), `v02_p028` p5 (rooftops and power lines), `v02_p064` p2–p3
(a treehouse; a coastline — two of that page's three panels),
`v01_p016` p4 (a stone carving), `v06_p111` p2 (ground, leaves and a hole),
`v02_p130` p5 (two bloodied kunai on the ground — the emotional payload of the page is an object
still-life), `v01_p019` (a window and sky).

---

## 5. Energy, jutsu and impact

This is where "AI-ish" is most visible, and the reference is unambiguous.

**Energy is never a glow. It is opaque ink laid over a scene that stays completely legible.**

### The floor stays visible
In every effect panel I read, the environment survives the effect:

- `v06_p122` (full-page Konoha Hurricane): the whirl is a **dry-brush swept arc of black and grey
  streaks** — white paper shows through the strokes. Both victims stay fully drawn; the effect
  passes *in front of* parts of them and *behind* others. The ground at the bottom is untouched
  and carries its own purple SFX.
- `v03_p150` (fireball): flame is **flat orange and yellow shapes with hard black outlines**, in
  layered tongues, behind and around the caster with a few tongues crossing in front of his legs.
  The pale ground and the blue hatched sky remain visible through the gaps. In the two small
  panels below, the ice mirrors and the figures stay fully readable with flame tongues sitting at
  the bottom edge.
- `v06_p039` (explosion): a **flat dark-red starburst of tapered spikes** plus pink blob shapes,
  over green grass that is still green and still visible. ~25 small figures flung outward
  radially, each at a different rotation and distance, several cropped by the panel edge.
- `v07_p013` (shadow jutsu): the technique is a **flat dark wedge stretched diagonally across the
  grass** — and the grass texture is still visible inside it, because it is a tone, not a void.
  The spinning-sphere weapon in the same page is a **tight concentric scribble**, like coiled
  wire, with the grass legible right up to its edge.
- `v02_p169` (vanishing jutsu): a **scribbled oval of concentric white line loops**, like a ball
  of yarn, with leaves flying — the branch and sky read straight through it. Smoke, when it
  appears, is **flat white cloud shapes with hard outlines** (`v06_p134`, `v02_p169`).
- `v07_p070` (dōjutsu vision): the effect is **radial brush streaks emanating from the centre of
  each panel**; the forest below stays completely readable.

### The impact vocabulary
Impacts are drawn as separate graphic marks, not as light:

- **Tapered slash strokes** in flat red with a black outline, scattered across the panel and
  attached to nothing: `v05_p150` p1 has about ten of them across a ceiling.
- **Small flat yellow star-flashes** at contact points: `v06_p122`, `v06_p031` p2, `v07_p013` p3.
- **Angular debris chips** — dozens of little white or grey parallelograms: `v06_p122`,
  `v06_p059` p4, `v05_p150` (flying paper).
- **White radiating flash strokes** at the point of contact: `v06_p122`, `v01_p019` p2.
- **Straight radiating motion lines** from the blast centre: `v06_p039`.

### Does it break the panel border?
The *effect art* generally stays inside its panel. The **SFX lettering** is what breaks out — see
§7. The one systematic exception is that effects are routinely **cropped by the panel edge**
(`v07_p013` p2, `v06_p039`), which reads as bigger-than-frame.

---

## 6. Figures, poses and proportions

Measured by eye off full-figure panels — treat as estimates, not measurements:

- **Child characters read at roughly 6 heads tall; adults 7 to 7.5.** (`v06_p047`, `v06_p134` p3,
  `v05_p152`.) Not 8 — these are not fashion-plate proportions.
- **Comedy insert panels drop to 3–4 heads** with a head that fills most of the panel:
  `v03_p077` p5, `v03_p040` p8, `v06_p111` p3.
- Hands and feet are **large and simply drawn**; a foreshortened hand can be as big as the head
  (`v07_p091` p6, `v05_p174` p2, `v01_p016` bottom panel).

Posing:

- **Weight is off-centre.** `v05_p152` (a full-page hero shot) is still contrapposto: arm thrown
  to one side, coat flaring, weight on one leg. Even a centred figure is not a symmetrical figure.
- **Bodies twist.** Falling and recoiling figures are drawn along a diagonal with limbs at
  different angles and at least one limb cropped by the panel edge: `v01_p145` bottom panel
  (a figure lying diagonally, one leg out of frame at the top-right, a hand cropped at the
  bottom), `v01_p034` p3, `v06_p059` p4.
- **Static symmetrical standing figures essentially do not appear** except in a chapter-opener
  portrait, and even then the figure is cropped by the page edge (`v02_p046`).

---

## 7. SFX and lettering as composition

SFX are not stickers placed in a gap — they are **compositional mass**, usually the second
largest element after the figure.

Rules observable in the sample:

1. **They overlap the figures.** `v06_p039` (purple katakana over the blast and the grass),
   `v06_p122` (red katakana over the whirl; the English title set *over* the art and tilted to
   follow the motion arc), `v05_p152` (the figure's coat overlaps the letters and the letters
   overlap the coat), `v05_p065` p3.
2. **They get cropped by the panel edge.** Very common — half a glyph runs off the frame:
   `v06_p031` (a giant black ガ cropped by the panel's top and left), `v06_p122` (one glyph
   cropped top-left, another bottom-right), `v06_p039`, `v05_p144`, `v06_p111`, `v07_p091`.
3. **They cross gutters and bridge panels.** `v06_p059` row 1: one red SFX starts in the left
   panel and continues into the right panel across the gutter. `v07_p070`: a blue SFX runs
   horizontally across the boundary between two rows of panels and extends past the panel block
   into the white margin. `v06_p031` p3 has SFX sitting on the panel border.
4. **Colour is a flat spot colour with a contrasting outline** — red, purple, blue, orange, cyan
   — chosen against the panel's ground: cyan on black (`v07_p091`), black with white gaps on
   white (`v06_p031`), purple over green grass (`v06_p039`), orange over forest (`v07_p153`).
5. **Placement is often symmetrical flanking**, one mass left and one right of the head:
   `v03_p040` p1–p2 (red ガツ on both sides of two different heads, the same gag repeated),
   `v03_p077` p2, `v05_p144`, `v07_p091` p6, `v06_p059` p1–p2.
6. **English hand-lettered SFX runs vertically down a margin**, overlapping the panel border:
   `v02_p028` ("GOTCHA!!" and "MEEOWWW!!!" stacked vertically at the left edge),
   `v01_p145` ("OWW! OW! OW! OW!!!"). Small ones sit in their own little blob balloon:
   `v07_p091` ("SHOVE"), `v05_p150`, `v03_p040` ("SCOWL" with a pointer line).
7. **Titles sit inside the art, not in a box**: `v06_p047`, `v05_p046`, `v01_p145`, `v06_p122`,
   `v03_p150`. Captions, when boxed, are a plain white rectangle *inside* the panel
   (`v06_p111` p5, `v05_p174` p1) and translation footnotes can sit in the white gutter strip
   between panels (`v05_p174`).
8. **Balloon shape carries emotion**: jagged/spiky outlines for shouts and shocks
   (`v05_p150` "!!", `v05_p109`, `v01_p034` "!!"), a **spiky black or white halo** around the
   balloon for a shouted jutsu name (`v07_p013`, `v07_p153`, `v07_p070`),
   soft cloud-lobed outlines for panting and murmurs (`v03_p092`, `v06_p134` "HUF").

---

## 8. Faces and emotion

### Construction
- **Huge white sclera, small iris, tiny pupil.** `v02_p130` p3 (eyes-only panel: enormous whites,
  a small blue iris ring and a black dot), `v06_p059` p1–p2, `v07_p038` p4.
- **Very little modelling.** Shadow is **parallel hatch lines** on cheeks, under eyes and across
  the forehead, not gradient (`v02_p130`, `v06_p059`, `v07_p038` — every panel on that page has
  hatch strokes across the cheeks). No specular highlights, no rim light, no subsurface glow.
- **The nose is a line or two; the mouth is a shape.** In comedy the mouth becomes half the face
  (`v03_p040` p8, `v03_p077` p5).
- **Symbols replace expressions freely**: flame irises (`v06_p111` p3), a floating "?" as an
  entire line of dialogue (`v01_p061` p6, `v03_p120` p5, `v01_p145`), sweat drops, blush hatching.

### Emotion staged without dialogue
`v07_p038` is the exemplar and worth copying wholesale. Eight panels, one balloon on the page.
The escalation is achieved purely by **cropping tighter and turning the head away**:

face with tears → face three-quarter → **back of the head** → **one eye, cropped by all four
edges** → a detail of the marked neck with unboxed display text on the flat background →
face turned back → a wide two-shot with the face *hidden* against the other character →
**one eye with a tear**.

All eight backgrounds are flat lavender/blue-grey or horizontal speed-line bands. **Zero
environment. Zero rendering escalation.** The intensity comes from framing alone.

Other silent-emotion devices seen:
- **A character alone and tiny in a black void**: `v06_p111` p4 (figure ~12% of the panel height
  at the bottom of an otherwise empty black panel), `v05_p087` p1 (a curled-up figure floating in
  black with a line of text repeated ten times around it), `v05_p109` p1 (white text floating
  unboxed on black, no balloon).
- **An object instead of a face**: `v02_p130` p5 (bloodied kunai on the ground).
- **Extreme negative space**: `v02_p046` (one figure in the lower-right corner of an otherwise
  blank page).
- **Turning the head away** (`v03_p120` p2 and p4, `v07_p038` p3).

---

## 9. Comedy conventions

- Proportions collapse to chibi *within a single panel of an otherwise normal page*
  (`v03_p077` p5, `v03_p040` p8, `v06_p111` p3).
- The gag is often **repetition of an identical framing** for two characters in adjacent panels
  (`v03_p040` p1–p2: same crop, same red SFX flanking, different character).
- Background goes to a **radial burst or a flat gag colour** at the punchline (`v03_p040` p6:
  purple-to-white radial with speed lines; `v02_p028` p4: yellow burst).
- An **abstract texture panel** can stand in for a whole beat (`v06_p111` p5, `v03_p040` p5).
- Comedy pages still keep the depth stagger — `v03_p040` p3 puts five characters around a table
  at different depths with one seated back-to-camera cropped at the bottom edge.

---

## 10. Colour and value (brief — surface is already solved)

*[auto]* Mean saturation of non-dark pixels across all 1119 pages is **0.18**; **96.6%** of pages
average below 0.35. This is a print palette, not a screen palette. Directly observed: skin is one
flat tone plus one hatch tone; hair is one flat colour plus a single lighter block;
"night" is a flat navy or a flat black, not a blue gradient (`v05_p087`, `v06_p031`, `v07_p091`).

---

## 11. Anti-pattern checklist

If a generated page shows any of these, it will read as an illustration:

| Tell | What the reference does instead |
|---|---|
| Characters in a row at one depth, evenly spaced, facing camera | Different depths, 4:1+ scale ratio, overlapping, someone cropped by the edge, someone turned away (§2) |
| Every panel the same size, aligned grid | One dominant panel per page (median 32% of area), CV of panel area ~0.6 (§1) |
| Every background fully rendered | ~2 panels in 3 have no drawn environment; close-ups almost never do (§4) |
| Energy as a glow that washes out the scene | Opaque flat shapes / brush strokes / scribbles; ground and figures stay fully visible (§5) |
| Subject centred and fully in frame | Subject low and to one side, with a balloon shelf; nearest object cropped (§2.5) |
| SFX floating in an empty gap | SFX overlapping figures, cropped by the panel edge, crossing gutters (§7) |
| Emotion escalated by adding rendering | Emotion escalated by cropping tighter and turning away (§8) |
| All figures fully visible, no occlusion | Foreground bodies, legs, hats and corpses obstruct the lens (§3) |
| Every panel has a character | ~1 page in 3 has an empty scenery or object panel (§4) |
| 3–4 big panels per page | 6–9 panels is the norm (48% of pages) (§1) |

---

## 12. Prompt fragments

Paste-able sentences. Mix and match; most pages need one from each group.

### Page layout
- "Seven panels in three uneven rows; the rows do not share column positions; one panel occupies
  about 40% of the page and the rest are small."
- "One dominant wide panel across the top taking ~55% of the page, then a row of three narrow
  reaction panels beneath it."
- "Thin black panel borders on white paper; one panel runs off the right and bottom edges of the
  page with no border on those sides."
- "A single full-page panel bleeding off three edges, with a thin strip of white paper remaining
  on the left."
- "Full-bleed borderless splash: art to all four page edges, no panel frame anywhere."
- "One letterbox panel about four times wider than tall containing only the character's eyes."

### Staging a group
- "Stage the group at three different depths: one figure huge in the extreme foreground cropped
  by the panel edge so only a shoulder and the back of the head are visible, one figure at mid
  distance turned three-quarters away, and one figure small in the far background. Do not line
  them up and do not have them face the camera."
- "Two characters talking, but at very different scale: the speaker fills the right third of the
  panel cropped by the right and bottom edges; the listener is small in the far left of the
  frame; speech balloons occupy the empty space between them."
- "Three characters seated in a row seen from behind, unevenly spaced, small in the frame, with
  the empty ground occupying the bottom 40% of the panel."
- "Crowd seen from a high angle: the main characters tiny at the centre in colour, twenty
  onlookers drawn as flat black silhouettes scattered at irregular positions and different
  poses, several cropped by the panel edge, the ground fully visible between them."
- "Camera inside the crowd at head height: the nearest figure cropped to just hair and a
  shoulder, heads overlapping heads at four receding depths, nobody facing the camera."
- "Melee: overlapping interpenetrating figures cropped by the top and bottom panel edges, no
  environment at all, background reduced to flat horizontal speed-line bands."

### Camera
- "Extreme high angle looking down; the figure is less than 8% of the panel height and the
  environment dominates."
- "Extreme low angle looking up at the underside of the chin; the top of the head is cropped by
  the panel edge; flat white background."
- "Shoot past a foreground obstruction: bystanders' legs cropped at both panel edges frame the
  action in the gap between them."
- "Extreme close-up of a single eye, cropped by all four panel edges, flat tone behind it."
- "Body-part panel: a hand, an ankle or a torso only, with no face in the panel at all."
- "A hand thrust toward the camera in extreme foreshortening, drawn nearly as large as the head."

### Backgrounds
- "Background is blank white paper: no ground, no shadow, no horizon."
- "Background is one flat lavender tone with halftone dots and nothing else."
- "Background is flat black void; the figure is separated from it by a thin white contour;
  dialogue is unboxed white text floating on the black."
- "Background is a radial burst of straight white spikes converging behind the character's head."
- "Background is nothing but parallel speed lines and small angular debris chips."
- "An empty panel with no characters: just the moon and flat clouds / rooftops and power lines /
  two kunai lying on the ground."

### Energy and impact
- "Draw the technique as flat opaque shapes with hard black outlines, layered in front of and
  behind the figure. It must not glow and must not wash out the scene: the ground, the
  characters and the sky remain fully drawn and legible through and around it."
- "The whirlwind is a swept dry-brush arc of black and grey streaks with white paper showing
  through; scatter small flat yellow star-flashes at the contact points and dozens of small
  angular debris chips across the panel."
- "The explosion is a flat dark-red starburst of tapered spikes over grass that stays green and
  visible; small figures are flung outward radially, each at a different rotation, several
  cropped by the panel edge."
- "The vanishing is a scribbled oval of concentric white line loops with leaves flying; the
  branch and sky read straight through it."
- "Impact is marked by six flat red tapered slash strokes with black outlines scattered across
  the panel, attached to nothing."

### Figures
- "Child characters about six heads tall, adults about seven; large simply-drawn hands and feet."
- "The figure's weight is off-centre with the body twisted along a diagonal and at least one limb
  cropped by the panel edge. No symmetrical standing pose."
- "One comedy panel drops the character to chibi proportions, three heads tall, mouth filling
  half the face, while the rest of the page stays normally proportioned."

### Faces and emotion
- "Huge white sclera with a small iris and a dot pupil; shadow rendered as parallel hatch lines
  on the cheeks and under the eyes; no gradients, no highlights, no rim light."
- "Stage the emotional beat with no dialogue: four panels escalating by cropping tighter — full
  face, then the back of the turned-away head, then one eye cropped by all four edges, then one
  eye with a tear. Flat tone behind every panel, no environment."
- "The character sits tiny at the bottom of an otherwise empty flat-black panel."
- "A floating '?' or a sweat drop instead of a line of dialogue."

### SFX and lettering
- "Large flat-colour katakana sound effect with a contrasting outline, overlapping the figure and
  cropped by the panel edge so part of the glyph runs off frame."
- "The sound effect crosses the gutter, starting in one panel and continuing into the next."
- "Symmetrical SFX flanking: one mass of lettering to the left of the head and one to the right."
- "Hand-lettered English sound effect stacked vertically down the left margin, overlapping the
  panel border."
- "Speech balloons occupy the top 50% of the panel; the figure is pushed low and to one side."
- "The shouted jutsu name sits in a balloon with a spiky black halo."

---

## 13. Confidence notes

**Solid** (many independent instances, all six volumes): depth staggering and edge-cropping of
groups (§2); flat/blank backgrounds dominating close-ups (§4); energy drawn as opaque graphics
that leave the scene legible (§5); SFX overlapping and cropped (§7); emotion staged by cropping
(§8); panel-count and panel-size distributions (§1, automated over all 1119 pages).

**Reasonably solid but hand-counted on a small sample**: the 31% "drawn environment" figure
(105 panels, 16 pages) — the true figure probably sits between 25% and 40% and varies by scene
type, since establishing-heavy pages like `v07_p058` and `v07_p143` run 4 in 6.
The camera-angle tallies in §3 are instance counts, not rates.

**Weak / do not over-trust**:
- **Bleed rate.** The scans are trimmed to the artwork rather than the physical page, so the
  automated 80% figure is meaningless. Use the hand observation instead: about one page in six or
  seven has art clearly running off a page edge.
- **Figure proportions.** Estimated by eye from a handful of full-figure panels, not measured.
- **Panel counts** carry ±1 error from the detector (validated MAE 0.88).
- **Volume balance.** Vols 1–3 are village/academy material and vols 5–7 are forest/exam combat;
  the "flat black void" and "silhouette crowd" devices come disproportionately from 5–7, and the
  "empty cutaway scenery panel" from 1–3. If a page is quiet and domestic, weight toward the
  vol 1–3 devices; if it is combat, weight toward 5–7.
- **Reading order.** These scans read left to right. Do not infer Japanese page rhythm from them.
