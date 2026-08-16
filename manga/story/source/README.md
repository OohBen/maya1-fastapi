# Local source workflow

The manga adapts *Uchiha Naruto: The Sage* by The Omnipresent Sage:

- FanFiction.net story ID: `9891190`
- Canonical URL: `https://www.fanfiction.net/s/9891190/1/Uchiha-Naruto-The-Sage`
- Length: 50 chapters
- Status: complete

The complete prose is kept outside Git under `manga/.source/`. Fetch and split it with:

```bash
python3 manga/story/source/fetch_source.py
```

This creates:

```text
manga/.source/uchiha-naruto-the-sage/
├── ch01.txt
├── ...
├── ch50.txt
└── manifest.json
```

The command resolves the current EPUB through FicHub, validates that the archive contains all
50 numbered chapters, writes UTF-8 plain text, and records the source URL and EPUB checksum.
It uses only the Python standard library.

To rebuild from an already-downloaded EPUB without network access:

```bash
python3 manga/story/source/fetch_source.py --epub /absolute/path/to/story.epub
```

Before scripting a volume, read its source chapters end to end. Commit derived story briefs,
continuity notes, and page plans; leave the downloaded prose under the ignored `.source/` tree.
