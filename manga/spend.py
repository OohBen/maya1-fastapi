"""Total Replicate spend across every chapter ledger, with budget remaining."""
import json, pathlib, sys
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 26.0
# Resolve against this file, not the cwd: running it from the repo root used to glob nothing
# and report a confident $0.00 spent.
HERE = pathlib.Path(__file__).resolve().parent
tot = 0.0
rows = []
for f in sorted((HERE / "chapters").glob("v5ch*/ledger.json")):
    v = sum(r.get("cost", 0) or 0 for r in json.load(f.open()))
    tot += v
    pages = len(list((f.parent / "raw").glob("p*.png")))
    rows.append((f.parent.name, pages, v))
for cid, n, v in rows:
    print(f"  {cid}  {n:3} pages  ${v:6.2f}")
SPENT_BEFORE_RESTYLE = 17.20  # calibrated to the owner's reported balance of $0.70 on
# 2026-08-18, not derived from ledgers: retries, refusals and the tier/style experiments
# never reached a chapter ledger, so ledger sums run roughly $1 light. Trust the balance.
print(f"\n  this pass:      ${tot:.2f}")
print(f"  before restyle: ${SPENT_BEFORE_RESTYLE:.2f}  (ledgers were reset; not on disk)")
print(f"  VOLUME 5 TOTAL: ${tot + SPENT_BEFORE_RESTYLE:.2f} of ${BUDGET:.2f}   remaining ${BUDGET - tot - SPENT_BEFORE_RESTYLE:.2f}")
