#!/usr/bin/env python3
"""Export chapter page specs for Codex's native, tool-mediated image generator."""

import argparse
import hashlib
import importlib.util
import json
import math
import pathlib
import re
import sys

from genlib import SPLASH, STAGING, STYLE, STYLE_REF
from PIL import Image, ImageOps


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_builder(path):
    path = path.resolve()
    sys.path.insert(0, str(path.parent.parent))
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_ref(raw, roots):
    path = pathlib.Path(raw)
    if path.is_file():
        return path.resolve()
    for root in roots:
        candidate = root / path.name
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(f"missing reference: {path.name}")


def build_bundle(pid, refs, bundle_dir):
    """Pack overflow refs into ordered, unlabeled tiles for the five-path tool limit."""
    tile = 640
    columns = min(3, len(refs))
    rows = math.ceil(len(refs) / columns)
    canvas = Image.new("RGB", (columns * tile, rows * tile), "white")
    for index, ref in enumerate(refs):
        with Image.open(ref) as source:
            fitted = ImageOps.contain(source.convert("RGB"), (tile, tile), Image.Resampling.LANCZOS)
        x = (index % columns) * tile + (tile - fitted.width) // 2
        y = (index // columns) * tile + (tile - fitted.height) // 2
        canvas.paste(fitted, (x, y))
    bundle_dir.mkdir(parents=True, exist_ok=True)
    path = bundle_dir / f"{pid}_content_bundle.png"
    canvas.save(path)
    return path.resolve()


def pack_refs(pid, prompt, refs, bundle_dir):
    """Return at most four content paths and rewrite overflow image bindings to tile bindings."""
    if len(refs) <= 4:
        return prompt, refs, None
    kept = refs[:3]
    overflow = refs[3:]
    bundle = build_bundle(pid, overflow, bundle_dir)
    for source_index in range(len(refs), 3, -1):
        tile_index = source_index - 3
        prompt = re.sub(rf"\bImage {source_index}\b",
                        f"tile {tile_index} of Image 4", prompt)
    prefix = (
        "REFERENCE PACKING: Image 4 is an unlabeled composite plate. Its separate source tiles "
        "are arranged left to right, then top to bottom. The bindings below identify each tile; "
        "never blend identities, costumes, creatures, props, or environments across tiles. "
    )
    return prefix + prompt, kept + [bundle], [str(path) for path in overflow]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("builder", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("--style-ref", required=True, type=pathlib.Path)
    parser.add_argument("--ref-root", action="append", default=[], type=pathlib.Path)
    parser.add_argument("--size", default="1152x2048")
    parser.add_argument("--bundle-dir", type=pathlib.Path)
    parser.add_argument("--page", action="append", help="export only this page ID; repeatable")
    args = parser.parse_args()

    builder = load_builder(args.builder)
    style_ref = args.style_ref.resolve()
    if not style_ref.is_file():
        raise FileNotFoundError(style_ref)
    roots = [root.resolve() for root in args.ref_root]
    selected = set(args.page or [])
    bundle_dir = (args.bundle_dir or (args.output.parent / "bundles")).resolve()
    rows = []

    for pid, style_query, desc, raw_refs, quality in builder.PAGES:
        if selected and pid not in selected:
            continue
        source_refs = [resolve_ref(raw, roots) for raw in raw_refs]
        desc, refs, bundled_sources = pack_refs(pid, desc, source_refs, bundle_dir)
        ordered_refs = refs + [style_ref]
        if len(ordered_refs) > 5:
            raise ValueError(f"{pid}: {len(ordered_refs)} total refs exceed the native five-path cap")
        stage = SPLASH if style_query.get("panels") == 1 else STAGING
        prompt = desc + " " + stage + STYLE_REF.format(i=len(refs) + 1) + STYLE
        rows.append({
            "page": pid,
            "style_query": style_query,
            "quality": quality,
            "desired_size": args.size,
            "prompt": prompt,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "source_refs": [str(path) for path in source_refs],
            "bundled_sources": bundled_sources,
            "refs": [
                {"index": index, "path": str(path), "sha256": sha256(path),
                 "role": "style" if index == len(ordered_refs) else "content"}
                for index, path in enumerate(ordered_refs, start=1)
            ],
            "status": "pending",
            "attempts": [],
        })

    if selected - {row["page"] for row in rows}:
        raise ValueError(f"unknown page IDs: {sorted(selected - {row['page'] for row in rows})}")
    payload = {
        "schema_version": 1,
        "backend": "codex_builtin_imagegen_tool",
        "builder": str(args.builder.resolve()),
        "builder_sha256": sha256(args.builder.resolve()),
        "normalization_target": args.size,
        "pages": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {len(rows)} pages -> {args.output}")


if __name__ == "__main__":
    main()
