"""Download colored Naruto pages to use as STYLE references."""
import concurrent.futures as cf, pathlib, sys, requests, os
os.environ.setdefault("SSL_CERT_FILE","/root/.ccr/ca-bundle.crt")
REF="c73b899122fa02a02fe4912ec7b3dcc52bf6ae2f"
B=f"https://cdn.jsdelivr.net/gh/anon6968/naruto-color-pages@{REF}/pages"
OUT=pathlib.Path(__file__).resolve().parent/"style"

def grab(job):
    vol,n=job
    dest=OUT/f"v{vol:02d}_p{n:03d}.webp"
    if dest.exists(): return None
    try:
        r=requests.get(f"{B}/{vol}/{n:03d}.webp",timeout=60)
        if r.status_code!=200 or len(r.content)<5000: return None
        dest.write_bytes(r.content); return dest.name
    except Exception:
        return None

if __name__=="__main__":
    vols=[int(v) for v in sys.argv[1:]] or [1,2,3,68]
    OUT.mkdir(parents=True,exist_ok=True)
    jobs=[(v,n) for v in vols for n in range(1,201)]
    got=0
    with cf.ThreadPoolExecutor(max_workers=40) as ex:
        for r in ex.map(grab,jobs):
            if r: got+=1
    print(f"downloaded {got} new pages; total on disk: {len(list(OUT.glob('*.webp')))}")
