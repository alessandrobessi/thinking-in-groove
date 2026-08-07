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
    "part-1-role/04-the-driver.md",
    "part-1-role/05-the-colorist.md",
    "part-1-role/06-the-shadow.md",
    "part-1-role/07-the-voice-leader.md",
    "part-1-role/08-the-commentator.md",
    "part-2-harmonic-motion/13-the-approach-note-arriving-with-intention.md",
    "part-2-harmonic-motion/12-passing-motion-connecting-two-points.md",
    "part-2-harmonic-motion/16-cadential-motion-tension-and-release.md",
    "part-2-harmonic-motion/11-the-pedal-stillness-under-change.md",
    "part-2-harmonic-motion/10-root-motion-the-bass-line-as-harmonic-skeleton.md",
    "part-2-harmonic-motion/14-substituted-root-implying-a-different-chord.md",
    "part-2-harmonic-motion/15-deceptive-motion-the-expected-turn-that-isnt.md",
    "part-2-harmonic-motion/leaping.md",
    "part-2-harmonic-motion/18-motion-profile-the-shape-of-a-phrase.md",
    "part-3-groove/19-the-pocket-where-exactly-is-the-note.md",
    "part-3-groove/25-push-and-lay-back-playing-around-the-beat.md",
    "part-3-groove/21-space-as-content-the-power-of-not-playing.md",
    "part-3-groove/20-syncopation-points-avoiding-the-obvious-beat.md",
    "part-3-groove/26-the-groove-signature-what-makes-a-line-recognizable.md",
}

LEGACY_PIANO_EXAMPLES = {
    "part-1-role/09-role-shift-when-the-job-changes-mid-phrase.md": "role-shift.abc",
    "part-2-harmonic-motion/17-harmonic-rhythm-who-decides-when-the-chord-changes.md": "harmonic-rhythm.abc",
    "part-3-groove/22-the-repetition-cell-the-riff-atom.md": "repetition-cell.abc",
    "part-3-groove/23-the-variation-layer-keeping-a-groove-alive.md": "variation-layer.abc",
    "part-3-groove/24-density-controlling-energy-through-note-count.md": "density-curve.abc",
    "part-4-integration/27-the-layer-stack-role-motion-and-groove-at-once.md": "layer-stack.abc",
    "part-4-integration/28-the-groove-contract-setting-and-breaking-expectations.md": "groove-contract.abc",
    "part-4-integration/29-designing-a-bass-line-from-scratch-a-worked-case-study.md": "design-study.abc",
}


def replacement_example(filename: str) -> str:
    abc = (ROOT / "examples" / "chapters" / filename).read_text().strip()
    title = re.search(r"^T:(.+)$", abc, re.MULTILINE).group(1)
    style = re.search(r"^R:(.+)$", abc, re.MULTILINE).group(1)
    slug = Path(filename).stem
    return (
        "## Musical Example\n\n"
        ':::{.content-hidden when-format="epub"}\n\n'
        "```{=html}\n"
        f'<div class="score-example" id="{slug}-example">\n'
        f'<p class="abc-caption"><strong>{title}.</strong> A checked piano example for this chapter.</p>\n'
        f'<p class="abc-description">{style} for harmony and monophonic bass, with semantic bass annotations.</p>\n'
        f'<pre class="abc-source">{abc}</pre>\n'
        '<div class="abc-rendered"></div>\n</div>\n'
        "```\n\n:::\n\n"
    )


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
    filename = LEGACY_PIANO_EXAMPLES.get(relative)
    if filename is None:
        raise ValueError(f"legacy score has no piano replacement: {relative}")
    replacement = replacement_example(filename)
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
