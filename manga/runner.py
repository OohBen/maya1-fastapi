"""Shared chapter runner. Every chapter file declares PAGES and calls run().

Pulled out of the per-chapter build scripts so the failure handling lives in one place:
transient errors retry, content refusals CHANGE something (next style reference, then a
softened prompt, then no style reference) instead of repeating a request that cannot work.
"""
import concurrent.futures as cf
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "refs"))

from genlib import SPLASH, STAGING, STYLE, STYLE_REF, build_page, Ledger  # noqa: E402
import backend                                                            # noqa: E402
import style_select as ss                                                # noqa: E402


def run(pages, outdir, ledger_path, workers=50, size=None, style_ref=None):
    """pages: list of (pid, style_query, prompt_body, refs, quality).

    size: output resolution "WIDTHxHEIGHT"; defaults per page from the quality tier.
    Set MANGA_BACKEND to swap the image generator — see backend.py and AGENTS.md.
    """
    out = pathlib.Path(outdir)
    led = Ledger(ledger_path)

    def one(spec):
        pid, want, desc, refs, quality = spec
        dest = out / f"{pid}.png"
        if dest.exists() and dest.stat().st_size > 0:
            return f"[skip] {pid}"
        stage = SPLASH if want.get("panels") == 1 else STAGING
        prompt = desc + " " + stage + STYLE_REF.format(i=len(refs) + 1) + STYLE
        # V4 anchored its whole volume to ONE style page and the reader noticed when V5
        # drifted off it. A fixed style_ref now leads the candidate list; the per-page
        # library picks remain only as moderation fallbacks.
        cands = [str(ss.as_png(r["file"]))
                 for r in sorted(ss.library(), key=lambda r: -ss.score(r, want))[:2]]
        if style_ref:
            cands = [str(style_ref)] + cands
        # Resolution is chosen PER PAGE, not per volume: pages carrying one big image earn the
        # larger canvas, ordinary pages do not. NEVER pair "low" with 2160x3840 — it comes back
        # soft and smeary. See models/TIER_REPORT.md, finding 4.
        px = size or ("2160x3840" if quality in ("medium", "high") else "1152x2048")
        try:
            img, cost, sref = build_page(prompt, refs, cands, quality, aspect=px)
        except Exception as e:
            return f"[FAIL] {pid}  {str(e)[-100:]}"
        out.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(".png.part")
        tmp.write_bytes(img)
        tmp.replace(dest)
        led.add(page=pid, quality=quality, size=px, cost=cost,
                style_ref=pathlib.Path(sref).name if sref else None)
        return f"[ok]   {pid}  {quality:6} ${cost:.3f}"

    only = sys.argv[1:] or None
    todo = [p for p in pages if not only or p[0] in only]
    print(f"building {len(todo)} pages -> {out}")
    with cf.ThreadPoolExecutor(max_workers=min(workers, max(1, len(todo)))) as ex:
        for line in ex.map(one, todo):
            print(line)
    print(f"\nchapter ledger: ${led.spent:.3f}")
