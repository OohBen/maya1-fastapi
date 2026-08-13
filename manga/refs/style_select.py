"""Pick the best-matching style reference page for a page being generated.

The style library is ~195 labelled colored-manga pages (see STYLE_TAXONOMY.md). Rather than
binding the same generic style reference to every page, each page gets the labelled page whose
scene type, lighting, cast size and mood most closely match it — so a quiet night dialogue page
is taught by a quiet night dialogue page, not by a daylight fight.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LABELS = HERE / "labels"
STYLE = HERE / "style"
CACHE = HERE / "style_png"          # webp -> png, so every model path accepts it

_LIB = None


def library():
    """Merged label records from every batch file."""
    global _LIB
    if _LIB is None:
        rows = []
        for f in sorted(LABELS.glob("*.json")):
            try:
                data = json.loads(f.read_text())
            except Exception:
                continue
            rows += [r for r in data if isinstance(r, dict) and r.get("file")]
        # drop records whose image is missing
        _LIB = [r for r in rows if (STYLE / r["file"]).exists()]
    return _LIB


WEIGHTS = {"scene": 3, "light": 3, "cast": 2, "shot": 1, "mood": 1}


def score(rec, want):
    s = 0
    for k, w in WEIGHTS.items():
        if want.get(k) and rec.get(k) == want[k]:
            s += w
    # bonuses only when the page being generated actually wants these
    if want.get("sfx") and rec.get("sfx"):
        s += 2
    if want.get("speedlines") and rec.get("speedlines"):
        s += 1
    if rec.get("halftone"):
        s += 1                      # halftone is always desirable — it's the look we lack
    # prefer a similar panel count
    if want.get("panels") and rec.get("panels"):
        s += max(0, 2 - abs(int(rec["panels"]) - int(want["panels"])))
    return s


def as_png(name):
    """Return a PNG path for a library page, converting from webp once and caching."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / (pathlib.Path(name).stem + ".png")
    if not dest.exists():
        from PIL import Image
        Image.open(STYLE / name).convert("RGB").save(dest)
    return dest


def pick(n=1, **want):
    """Return up to n style-reference PNG paths best matching the described page.

    Example: pick(scene="dialogue", light="night", cast="small_group", mood="tense", panels=3)
    """
    lib = library()
    if not lib:
        return []
    ranked = sorted(lib, key=lambda r: -score(r, want))
    return [str(as_png(r["file"])) for r in ranked[:n]]


def explain(**want):
    """Debug helper: show the top 5 matches and their scores."""
    lib = library()
    ranked = sorted(lib, key=lambda r: -score(r, want))[:5]
    return [(r["file"], score(r, want), r.get("note", "")) for r in ranked]


if __name__ == "__main__":
    lib = library()
    print(f"style library: {len(lib)} labelled pages")
    if lib:
        import collections
        for k in ("scene", "light", "cast", "mood", "shot"):
            print(f"  {k:6}", dict(collections.Counter(r.get(k) for r in lib).most_common()))
        print("\nexample query — night dialogue, small group, tense:")
        for f, s, note in explain(scene="dialogue", light="night",
                                  cast="small_group", mood="tense", panels=3):
            print(f"   {s:>3}  {f}  {note}")
