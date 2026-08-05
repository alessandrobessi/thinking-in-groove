#!/usr/bin/env python3
"""Copy book/*.md into publish/chapters/, mirroring the part/back-matter
directory structure Quarto's _quarto.yml expects.

This step runs identically in CI, so publish/chapters/ can stay
gitignored build output rather than a second copy of the source that
has to be kept in sync by hand.

    python3 scripts/prepare_manuscript_for_publish.py
"""
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
OUT_DIR = ROOT / "publish" / "chapters"
PIANO_CHAPTERS = {
    "part-1-role/01-the-ground.md",
    "part-1-role/02-the-definer.md",
    "part-1-role/03-the-inverter.md",
    "part-2-harmonic-motion/13-the-approach-note-arriving-with-intention.md",
    "part-2-harmonic-motion/12-passing-motion-connecting-two-points.md",
}


def prepare_text(src: Path) -> str:
    """Keep legacy prose readable without publishing obsolete notation.

    A chapter becomes fully interactive only after it joins PIANO_CHAPTERS.
    Until then, its bass-only score and tab sections are replaced in the
    generated manuscript; source material remains untouched for migration.
    """
    text = src.read_text()
    relative = src.relative_to(BOOK_DIR).as_posix()
    if relative in PIANO_CHAPTERS or 'class="score-example"' not in text:
        return text
    replacement = (
        "## Musical Example\n\n"
        "> **Piano score in preparation.** This chapter's legacy example is "
        "being rebuilt as a checked grand-staff score with independent "
        "harmony and bass playback.\n\n"
    )
    migrated, count = re.subn(
        r"^## Musical Example\n.*?(?=^## Practice Ideas\n)",
        replacement,
        text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )
    if count != 1:
        raise ValueError(f"could not isolate legacy example sections in {relative}")
    return migrated


def main():
    chapter_files = sorted(
        f for f in BOOK_DIR.glob("*/*.md") if not f.parent.name.startswith("_")
    )
    if not chapter_files:
        raise SystemExit(f"no chapter files found under {BOOK_DIR}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)

    for src in chapter_files:
        dest = OUT_DIR / src.parent.name / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(prepare_text(src))
        print(f"wrote {dest.relative_to(ROOT)}")

    print(f"\n{len(chapter_files)} chapters prepared in {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
