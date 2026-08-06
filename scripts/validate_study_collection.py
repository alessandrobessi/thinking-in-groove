#!/usr/bin/env python3
"""Validate the reader-facing collection of complete musical studies."""

import re
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
STUDIES = ROOT / "examples" / "studies"
INDEX = ROOT / "publish" / "studies.qmd"


def voice_bars(text: str, voice: str, following: Optional[str] = None) -> int:
    section = text.partition(f"[V:{voice}]")[2]
    if following:
        section = section.partition(f"[V:{following}]")[0]
    return section.replace("|]", "|").count("|")


def main() -> None:
    files = sorted(STUDIES.glob("*.abc"))
    errors: list[str] = []
    index = INDEX.read_text()
    if len(files) < 5:
        errors.append(f"collection requires at least five studies, found {len(files)}")

    for path in files:
        text = path.read_text()
        title_match = re.search(r"^T:(.+)$", text, re.MULTILINE)
        title = title_match.group(1) if title_match else path.stem
        rh_bars = voice_bars(text, "RH", "LH")
        lh_bars = voice_bars(text, "LH")
        if not 8 <= rh_bars <= 16:
            errors.append(f"{path.name}: expected 8–16 bars, found {rh_bars}")
        if rh_bars != lh_bars:
            errors.append(f"{path.name}: RH/LH bar mismatch ({rh_bars} != {lh_bars})")
        if f"[{title}](" not in index:
            errors.append(f"{path.name}: missing from publish/studies.qmd")
        for marker in ("%%score { RH LH }", 'name="Harmony"', 'name="Bass"'):
            if marker not in text:
                errors.append(f"{path.name}: missing {marker}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: {len(files)} indexed studies contain 8–16 matched grand-staff bars.")


if __name__ == "__main__":
    main()
