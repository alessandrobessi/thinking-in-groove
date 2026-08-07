#!/usr/bin/env python3
"""Catch the specific classes of drift that have previously slipped in by
hand: chapters listed out of chapter-map.md order within a Part, .abc
placeholders left behind under examples/chapters/ after a chapter's legacy
score is retired, and LEGACY_PIANO_EXAMPLES/PIANO_CHAPTERS entries that no
longer point at a real file.

    python3 scripts/validate_no_drift.py
"""
import re
import sys
from pathlib import Path

from prepare_manuscript_for_publish import BOOK_DIR, LEGACY_PIANO_EXAMPLES, PIANO_CHAPTERS

ROOT = Path(__file__).resolve().parent.parent
QUARTO_YML = ROOT / "publish" / "_quarto.yml"
LEGACY_EXAMPLES_DIR = ROOT / "examples" / "chapters"

CHAPTER_COMMENT = re.compile(r"^\s*-\s*(chapters/\S+\.md)\s*#\s*Ch\.\s*(\d+)")
PART_HEADING = re.compile(r'^\s*-\s*part:\s*"')


def check_nav_order() -> list[str]:
    errors = []
    current_part = None
    last_num = None
    for line in QUARTO_YML.read_text().splitlines():
        if PART_HEADING.match(line):
            current_part = line.strip()
            last_num = None
            continue
        match = CHAPTER_COMMENT.match(line)
        if not match:
            continue
        num = int(match.group(2))
        if last_num is not None and num < last_num:
            errors.append(
                f"nav order drift under {current_part}: "
                f"Ch.{num} ({match.group(1)}) appears after Ch.{last_num}"
            )
        last_num = num
    return errors


def check_legacy_examples() -> list[str]:
    errors = []
    referenced = set(LEGACY_PIANO_EXAMPLES.values())
    on_disk = {f.name for f in LEGACY_EXAMPLES_DIR.glob("*.abc")}

    for chapter, filename in LEGACY_PIANO_EXAMPLES.items():
        if not (BOOK_DIR / chapter).exists():
            errors.append(f"LEGACY_PIANO_EXAMPLES: chapter file missing: {chapter}")
        if filename not in on_disk:
            errors.append(f"LEGACY_PIANO_EXAMPLES: {filename!r} has no file under examples/chapters/")

    orphaned = sorted(on_disk - referenced)
    for filename in orphaned:
        errors.append(
            f"examples/chapters/{filename} is orphaned: no LEGACY_PIANO_EXAMPLES "
            "entry points at it (delete it, or the chapter that once used it)"
        )
    return errors


def check_piano_chapters() -> list[str]:
    errors = []
    for chapter in PIANO_CHAPTERS:
        if not (BOOK_DIR / chapter).exists():
            errors.append(f"PIANO_CHAPTERS: chapter file missing: {chapter}")
    overlap = PIANO_CHAPTERS & set(LEGACY_PIANO_EXAMPLES)
    for chapter in sorted(overlap):
        errors.append(f"{chapter} is listed in both PIANO_CHAPTERS and LEGACY_PIANO_EXAMPLES")
    return errors


def main() -> None:
    errors = check_nav_order() + check_legacy_examples() + check_piano_chapters()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(
        "OK: nav order matches chapter-map.md numbering, no orphaned "
        "examples/chapters/ files, and LEGACY_PIANO_EXAMPLES/PIANO_CHAPTERS "
        "entries all resolve."
    )


if __name__ == "__main__":
    main()
