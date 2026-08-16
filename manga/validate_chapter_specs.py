#!/usr/bin/env python3
"""Validate manga chapter builders before any image-generation calls are made."""

import argparse
import importlib.util
import pathlib
import re
import sys


IMAGE_INDEX = re.compile(r"\bImage (\d+)\b")


def load_builder(path):
    path = path.resolve()
    sys.path.insert(0, str(path.parent.parent))
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(path, expected_pages, extra_ref_roots, max_page_refs):
    errors = []
    source = path.read_text()
    if "/Users/" in source:
        errors.append("builder contains an absolute user path")

    module = load_builder(path)
    pages = getattr(module, "PAGES", None)
    if not isinstance(pages, list):
        return ["PAGES is not a list"]

    expected_ids = [f"p{i:02d}" for i in range(1, expected_pages + 1)]
    actual_ids = [page[0] for page in pages if isinstance(page, tuple) and page]
    if actual_ids != expected_ids:
        errors.append(f"page IDs are {actual_ids!r}; expected {expected_ids!r}")

    for row_number, page in enumerate(pages, start=1):
        if not isinstance(page, tuple) or len(page) != 5:
            errors.append(f"row {row_number}: expected a five-item tuple")
            continue
        pid, style_query, prompt, refs, quality = page
        if not isinstance(style_query, dict):
            errors.append(f"{pid}: style query is not a dictionary")
        elif not isinstance(style_query.get("panels"), int) or style_query["panels"] < 1:
            errors.append(f"{pid}: missing positive integer panel count")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{pid}: empty prompt")
            continue
        if not isinstance(refs, list) or not refs:
            errors.append(f"{pid}: references are not a non-empty list")
            continue
        if len(refs) > max_page_refs:
            errors.append(f"{pid}: {len(refs)} page refs exceed the {max_page_refs}-ref budget")
        if quality not in {"low", "medium", "high"}:
            errors.append(f"{pid}: invalid quality {quality!r}")

        indices = sorted({int(value) for value in IMAGE_INDEX.findall(prompt)})
        expected_indices = list(range(1, len(refs) + 1))
        if indices != expected_indices:
            errors.append(f"{pid}: prompt image indices {indices} do not match refs {expected_indices}")

        for ref in refs:
            ref_path = pathlib.Path(ref)
            if ref_path.is_file():
                continue
            if not any((root / ref_path.name).is_file() for root in extra_ref_roots):
                errors.append(f"{pid}: missing reference {ref_path.name}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("builder", type=pathlib.Path)
    parser.add_argument("--expected-pages", type=int, required=True)
    parser.add_argument("--extra-ref-root", action="append", default=[], type=pathlib.Path)
    parser.add_argument("--max-page-refs", type=int, default=15,
                        help="reserve one additional slot for the style reference")
    args = parser.parse_args()

    errors = validate(args.builder, args.expected_pages,
                      [path.resolve() for path in args.extra_ref_root], args.max_page_refs)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)
    print(f"PASS {args.builder.name}: {args.expected_pages} pages")


if __name__ == "__main__":
    main()
