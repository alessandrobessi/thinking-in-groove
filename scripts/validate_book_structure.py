#!/usr/bin/env python3
"""Check that publish/_quarto.yml's chapter list and book/*.md agree.

Catches the two ways these can drift: a chapter file added to book/ but
never wired into _quarto.yml (silently missing from every build), or a
_quarto.yml entry pointing at a file that no longer exists (a broken
build). Run in CI so a mismatch fails before it reaches Pages.

    python3 scripts/validate_book_structure.py
"""
import sys
from pathlib import Path

import yaml

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
    expected = {
        f"chapters/{f.parent.name}/{f.name}"
        for f in BOOK_DIR.glob("*/*.md")
        if not f.parent.name.startswith("_")  # e.g. book/_templates/, not a real part
    }

    missing_on_disk = sorted(listed - expected)
    missing_in_config = sorted(expected - listed)

    ok = True
    if missing_on_disk:
        ok = False
        print("_quarto.yml lists files that don't exist under book/:")
        for p in missing_on_disk:
            print(f"  {p}")
    if missing_in_config:
        ok = False
        print("book/ has chapter files not listed in _quarto.yml:")
        for p in missing_in_config:
            print(f"  {p}")

    if not ok:
        sys.exit(1)
    print(f"OK: {len(expected)} chapter files match _quarto.yml.")


if __name__ == "__main__":
    main()
