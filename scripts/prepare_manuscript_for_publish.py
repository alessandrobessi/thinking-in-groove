#!/usr/bin/env python3
"""Copy book/*.md into publish/chapters/, mirroring the part/back-matter
directory structure Quarto's _quarto.yml expects.

This step runs identically in CI, so publish/chapters/ can stay
gitignored build output rather than a second copy of the source that
has to be kept in sync by hand.

    python3 scripts/prepare_manuscript_for_publish.py
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
OUT_DIR = ROOT / "publish" / "chapters"


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
        shutil.copyfile(src, dest)
        print(f"wrote {dest.relative_to(ROOT)}")

    print(f"\n{len(chapter_files)} chapters prepared in {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
