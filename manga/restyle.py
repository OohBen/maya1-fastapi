"""Re-render selected pages with a style reference attached.

Imports an existing chapter's PAGES list, appends the best-matching style-library page as an
extra reference, and writes to a separate directory so the original stays intact for comparison.

    python3 restyle.py 09 p07 p10 --scene action --light night --mood tense
"""
import argparse
import concurrent.futures as cf
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "refs"))
from genlib import STYLE_REF, rep_generate, Ledger      # noqa: E402
import style_select as ss                                # noqa: E402


def load_chapter(num):
    path = HERE / "chapters" / f"build_ch{num}.py"
    spec = importlib.util.spec_from_file_location(f"build_ch{num}", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def restyle(num, page_ids, want, quality=None, aspect="1152x2048", n_style=1):
    mod = load_chapter(num)
    out = HERE / "chapters" / f"ch{num}" / "restyled"
    out.mkdir(parents=True, exist_ok=True)
    led = Ledger(HERE / "chapters" / f"ch{num}" / "ledger_restyle.json")

    picks = ss.pick(n=n_style, **want)
    print(f"style refs: {[pathlib.Path(p).name for p in picks]}")

    todo = [p for p in mod.PAGES if p[0] in page_ids]
    if not todo:
        print(f"no matching pages in ch{num}; available: {[p[0] for p in mod.PAGES][:8]}...")
        return

    def one(spec):
        pid, panels, desc, refs, q = spec
        q = quality or q
        idx = len(refs) + 1
        marker = str(idx) if n_style == 1 else f"{idx} and Image {idx+1}"
        prompt = desc + " " + STYLE_REF.format(i=marker) + mod.STYLE + " " + mod.NO_TEXT
        img, cost = rep_generate(prompt, refs=list(refs) + picks, quality=q, aspect=aspect)
        (out / f"{pid}.png").write_bytes(img)
        led.add(page=pid, quality=q, cost=cost, style_refs=[pathlib.Path(p).name for p in picks])
        return f"[ok] ch{num} {pid}  {q:6} ${cost:.3f}"

    with cf.ThreadPoolExecutor(max_workers=len(todo)) as ex:
        for line in ex.map(one, todo):
            print(line)
    print(f"-> {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--scene", default="dialogue")
    ap.add_argument("--light", default="night")
    ap.add_argument("--cast", default="small_group")
    ap.add_argument("--mood", default="tense")
    ap.add_argument("--panels", type=int, default=3)
    ap.add_argument("--quality", default=None)
    ap.add_argument("--nstyle", type=int, default=1)
    a = ap.parse_args()
    restyle(a.chapter, set(a.pages),
            dict(scene=a.scene, light=a.light, cast=a.cast, mood=a.mood, panels=a.panels),
            quality=a.quality, n_style=a.nstyle)
