#!/usr/bin/env python3
"""Validate the authoritative 40-chapter map and Vocabulary v2 contract."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    chapter_map = (ROOT / "docs" / "chapter-map.md").read_text()
    vocabulary = (ROOT / "docs" / "vocabulary-v2.md").read_text()
    errors: list[str] = []

    rows = re.findall(r"^\|\s*(\d+)\s*\|", chapter_map, re.MULTILINE)
    numbers = [int(value) for value in rows]
    if numbers != list(range(1, 41)):
        errors.append(f"chapter map must enumerate 1–40 exactly, found {numbers}")
    if chapter_map.count("## Part ") != 5:
        errors.append("chapter map must contain exactly five parts")

    terms = (
        "Ground", "Definer", "Inverter", "Pedal", "Reframer", "Driver",
        "Supporter", "Conversationalist", "Approach", "Enclosure", "Connection",
        "Syncopation", "Anticipation", "Duration", "Space", "Microtiming", "Pocket",
    )
    for term in terms:
        match = re.search(
            rf"^### {re.escape(term)}\n(.*?)(?=^### |^## |\Z)",
            vocabulary,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            errors.append(f"Vocabulary v2 is missing {term}")
            continue
        section = match.group(1)
        for field in ("Means", "Does not mean", "Positive", "Contrast", "Common error"):
            if f"**{field}:**" not in section:
                errors.append(f"{term} is missing field: {field}")

    if errors:
        raise SystemExit("\n".join(errors))
    print("OK: five-part chapter map enumerates 40 chapters; Vocabulary v2 defines 17 terms completely.")


if __name__ == "__main__":
    main()
