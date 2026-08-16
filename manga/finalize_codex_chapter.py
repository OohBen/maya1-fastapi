#!/usr/bin/env python3
"""Normalize manually approved native ImageGen pages and write serialized provenance."""

import argparse
import hashlib
import json
import pathlib

from PIL import Image


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def dimensions(value):
    width, height = value.lower().split("x", 1)
    return int(width), int(height)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=pathlib.Path)
    parser.add_argument("raw_dir", type=pathlib.Path)
    parser.add_argument("output_dir", type=pathlib.Path)
    parser.add_argument("ledger", type=pathlib.Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    expected = {row["page"] for row in manifest["pages"]}
    actual = {path.stem for path in args.raw_dir.glob("p*.png")}
    if actual != expected:
        raise ValueError(f"raw page IDs differ: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")

    for page in manifest["pages"]:
        pid = page["page"]
        source = args.raw_dir / f"{pid}.png"
        target_size = dimensions(page["desired_size"])
        with Image.open(source) as image:
            image.verify()
        with Image.open(source) as image:
            actual_size = image.size
            normalized = image.convert("RGB").resize(target_size, Image.Resampling.LANCZOS)
            destination = args.output_dir / f"{pid}.png"
            temporary = destination.with_suffix(".tmp.png")
            normalized.save(temporary)
            temporary.replace(destination)
        rows.append({
            "page": pid,
            "backend": manifest["backend"],
            "quality_requested": page["quality"],
            "prompt_sha256": page["prompt_sha256"],
            "references": [
                {"index": ref["index"], "file": pathlib.Path(ref["path"]).name,
                 "sha256": ref["sha256"], "role": ref["role"]}
                for ref in page["refs"]
            ],
            "source_dimensions": f"{actual_size[0]}x{actual_size[1]}",
            "normalized_dimensions": page["desired_size"],
            "normalization": "direct_resize_lanczos",
            "source_sha256": sha256(source),
            "output_sha256": sha256(destination),
            "review_status": "approved_manual",
            "cost_usd": None,
        })

    args.ledger.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.ledger.with_suffix(".tmp.json")
    temporary.write_text(json.dumps(rows, indent=2) + "\n")
    temporary.replace(args.ledger)
    print(f"finalized {len(rows)} pages -> {args.output_dir}")


if __name__ == "__main__":
    main()
