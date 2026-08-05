#!/usr/bin/env python3
"""Check that every published manuscript chapter exists and is piano-ready.

Legacy drafts may remain under book/ while they are migrated, but they
must not be published. Run in CI so missing files, tablature, or a
bass-only score cannot reach Pages.

    python3 scripts/validate_book_structure.py
"""
import sys
from pathlib import Path

import yaml

from prepare_manuscript_for_publish import prepare_text

ROOT = Path(__file__).resolve().parent.parent
QUARTO_YML = ROOT / "publish" / "_quarto.yml"
BOOK_DIR = ROOT / "book"


def collect_chapter_paths(node):
    """Recursively pull every string path out of book.chapters, whether
    it's a bare entry or nested under a part: group."""
    paths = []
    for item in node:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict) and "chapters" in item:
            paths.extend(collect_chapter_paths(item["chapters"]))
    return paths


def main():
    config = yaml.safe_load(QUARTO_YML.read_text())
    all_paths = collect_chapter_paths(config["book"]["chapters"])

    # Only the book/*.md-derived entries are checked here; front-matter
    # pages (index.qmd, preface.qmd, about-the-author.qmd) live in
    # publish/ directly and aren't part of this cross-check.
    listed = {p for p in all_paths if p.startswith("chapters/")}
    available = {
        f"chapters/{f.parent.name}/{f.name}"
        for f in BOOK_DIR.glob("*/*.md")
        if not f.parent.name.startswith("_")  # e.g. book/_templates/, not a real part
    }

    missing_on_disk = sorted(listed - available)
    missing_in_config = sorted(available - listed)

    ok = True
    if missing_on_disk:
        ok = False
        print("_quarto.yml lists files that don't exist under book/:")
        for p in missing_on_disk:
            print(f"  {p}")
    if missing_in_config:
        ok = False
        print("book chapters missing from the complete table of contents:")
        for p in missing_in_config:
            print(f"  {p}")
    for published in sorted(listed & available):
        relative = published.removeprefix("chapters/")
        text = prepare_text(BOOK_DIR / relative)
        if "Bass tab" in text or ".tab.txt" in text:
            ok = False
            print(f"published chapter depends on tablature: {relative}")
        score_count = text.count('<div class="score-example"')
        if score_count and text.count("%%score { RH LH }") != score_count:
            ok = False
            print(f"published chapter has a non-grand-staff score: {relative}")

    if not ok:
        sys.exit(1)
    print(
        f"OK: all {len(listed)} chapters are visible; published examples are "
        "piano grand staff or explicitly marked as in preparation."
    )


if __name__ == "__main__":
    main()
