#!/usr/bin/env python3
"""Fetch and split the Uchiha Naruto: The Sage source into local chapter text files."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import tempfile
import urllib.parse
import urllib.request
import zipfile
from xml.etree import ElementTree


STORY_URL = "https://www.fanfiction.net/s/9891190/1/Uchiha-Naruto-The-Sage"
FICHUB_API = "https://fichub.net/api/v0/epub"
EXPECTED_CHAPTERS = 50


def _download(url: str, destination: pathlib.Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "maya1-source-fetch/1"})
    with urllib.request.urlopen(request, timeout=120) as response:
        with destination.open("wb") as stream:
            shutil.copyfileobj(response, stream)


def _resolve_epub_url(story_url: str) -> tuple[str, dict]:
    query = urllib.parse.urlencode({"q": story_url})
    request = urllib.request.Request(
        f"{FICHUB_API}?{query}", headers={"User-Agent": "maya1-source-fetch/1"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = json.load(response)
    if payload.get("err") != 0:
        raise RuntimeError(f"FicHub returned an error: {payload!r}")
    relative_url = (payload.get("urls") or {}).get("epub")
    if not relative_url:
        raise RuntimeError("FicHub response did not contain urls.epub")
    return urllib.parse.urljoin("https://fichub.net", relative_url), payload


def _chapter_number(path: str) -> int:
    match = re.search(r"chap_(\d+)\.xhtml$", path)
    if not match:
        raise ValueError(f"not a chapter path: {path}")
    return int(match.group(1))


def _chapter_text(raw: bytes) -> str:
    root = ElementTree.fromstring(raw)
    body = next((element for element in root.iter() if element.tag.endswith("}body")), None)
    if body is None:
        raise ValueError("chapter XHTML has no body element")
    blocks: list[str] = []
    for element in body.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag not in {"h1", "h2", "h3", "p", "li", "blockquote"}:
            continue
        text = " ".join("".join(element.itertext()).split())
        if text:
            blocks.append(text)
    return "\n\n".join(blocks).strip() + "\n"


def _sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_local_source(epub: pathlib.Path, output_dir: pathlib.Path, metadata: dict) -> None:
    if not zipfile.is_zipfile(epub):
        raise ValueError(f"download is not a valid EPUB/ZIP archive: {epub}")
    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(epub) as archive:
        chapters = sorted(
            (name for name in archive.namelist() if re.search(r"chap_\d+\.xhtml$", name)),
            key=_chapter_number,
        )
        if len(chapters) != EXPECTED_CHAPTERS:
            raise ValueError(
                f"expected {EXPECTED_CHAPTERS} chapters, found {len(chapters)}"
            )
        expected_numbers = list(range(1, EXPECTED_CHAPTERS + 1))
        actual_numbers = [_chapter_number(name) for name in chapters]
        if actual_numbers != expected_numbers:
            raise ValueError(f"chapter sequence is incomplete: {actual_numbers}")
        for number, archive_path in zip(actual_numbers, chapters):
            destination = output_dir / f"ch{number:02}.txt"
            destination.write_text(_chapter_text(archive.read(archive_path)), encoding="utf-8")

    manifest = {
        "title": "Uchiha Naruto: The Sage",
        "author": "The Omnipresent Sage",
        "fanfiction_net_story_id": "9891190",
        "source_url": STORY_URL,
        "chapter_count": EXPECTED_CHAPTERS,
        "epub_sha256": _sha256(epub),
        "fichub": {
            "slug": metadata.get("slug"),
            "url_id": metadata.get("urlId"),
            "info": metadata.get("info"),
        },
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def main() -> None:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-url", default=STORY_URL)
    parser.add_argument(
        "--out",
        type=pathlib.Path,
        default=repo_root / "manga" / ".source" / "uchiha-naruto-the-sage",
    )
    parser.add_argument(
        "--epub",
        type=pathlib.Path,
        help="Use an existing EPUB instead of downloading it.",
    )
    args = parser.parse_args()

    metadata: dict = {}
    if args.epub:
        epub = args.epub.resolve()
        if not epub.is_file():
            raise SystemExit(f"EPUB not found: {epub}")
    else:
        epub_url, metadata = _resolve_epub_url(args.source_url)
        args.out.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(suffix=".epub", delete=False) as stream:
            epub = pathlib.Path(stream.name)
        try:
            _download(epub_url, epub)
            build_local_source(epub, args.out, metadata)
        finally:
            epub.unlink(missing_ok=True)
        print(f"source ready: {args.out} ({EXPECTED_CHAPTERS} chapters)")
        return

    build_local_source(epub, args.out, metadata)
    print(f"source ready: {args.out} ({EXPECTED_CHAPTERS} chapters)")


if __name__ == "__main__":
    main()
