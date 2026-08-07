#!/usr/bin/env python3
"""Validate the authoritative 40-chapter map and Vocabulary v2 contract.

Unlike an earlier version of this script, the required-term list is
derived from docs/chapter-map.md itself (via CHAPTER_TO_TERM below)
rather than hardcoded as a snapshot of whatever terms happened to
exist at one point in time. That snapshot approach is exactly how the
vocabulary silently fell behind the chapter map before: chapter-map.md
grew to 40 chapters while the validator kept checking the same 17
terms and reporting success, because nothing tied its checklist back
to the map it was supposedly validating against.

Every current chapter title matches its vocabulary heading exactly,
but CHAPTER_TO_TERM keeps them as an explicit mapping (not a bare set
of titles) so a future chapter whose title diverges from its term --
or a Part V chapter needing no term at all -- stays a one-line edit
here instead of a silent gap.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Chapter title (as it appears in chapter-map.md) -> required vocabulary-v2.md
# ### heading, or None if that chapter deliberately introduces no new term
# (Part V, Design, applies prior vocabulary rather than defining new terms).
CHAPTER_TO_TERM = {
    "The Ground": "Ground",
    "The Definer": "Definer",
    "The Inverter": "Inverter",
    "The Pedal": "Pedal",
    "The Reframer": "Reframer",
    "The Driver": "Driver",
    "The Supporter": "Supporter",
    "The Conversationalist": "Conversationalist",
    "Staying": "Staying",
    "Stepping": "Stepping",
    "Approaching": "Approaching",
    "Enclosing": "Enclosing",
    "Arpeggiating": "Arpeggiating",
    "Leaping": "Leaping",
    "Connecting Chords": "Connecting Chords",
    "Contrary Motion": "Contrary Motion",
    "Motion Maps": "Motion Maps",
    "Subdivision": "Subdivision",
    "Attack Placement": "Attack Placement",
    "Duration": "Duration",
    "Space": "Space",
    "Syncopation": "Syncopation",
    "Anticipation": "Anticipation",
    "Repeated Cells": "Repeated Cells",
    "Variation Without Collapse": "Variation Without Collapse",
    "Phrase Rhythm": "Phrase Rhythm",
    "Performed Feel": "Performed Feel",
    "Doubling": "Doubling",
    "Independence": "Independence",
    "Interlock": "Interlock",
    "Call and Response": "Call and Response",
    "Density Balance": "Density Balance",
    "Register and Separation": "Register and Separation",
    "Harmonic Rhythm": "Harmonic Rhythm",
    "The Bass-Line Design Algorithm": None,
    "Static Funk Vamp": None,
    "Functional Jazz Progression": None,
    "Fusion Ostinato": None,
    "Ballad and Inversion Study": None,
    "Complete Capstone": None,
}

# Cross-cutting terms referenced by name in multiple chapters (e.g. Attack
# Placement's and Harmonic Rhythm's own entries contrast themselves against
# these) rather than being one chapter's own title.
SUPPLEMENTARY_TERMS = ("Pocket", "Microtiming")

REQUIRED_FIELDS = ("Means", "Does not mean", "Positive", "Contrast", "Common error")


def check_term(vocabulary: str, term: str, errors: list) -> None:
    match = re.search(
        rf"^### {re.escape(term)}\n(.*?)(?=^### |^## |\Z)",
        vocabulary,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        errors.append(f"Vocabulary v2 is missing {term}")
        return
    section = match.group(1)
    for field in REQUIRED_FIELDS:
        if f"**{field}:**" not in section:
            errors.append(f"{term} is missing field: {field}")


def main() -> None:
    chapter_map = (ROOT / "docs" / "chapter-map.md").read_text()
    vocabulary = (ROOT / "docs" / "vocabulary-v2.md").read_text()
    errors: list[str] = []

    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", chapter_map, re.MULTILINE)
    numbers = [int(value) for value, _title in rows]
    if numbers != list(range(1, 41)):
        errors.append(f"chapter map must enumerate 1-40 exactly, found {numbers}")
    if chapter_map.count("## Part ") != 5:
        errors.append("chapter map must contain exactly five parts")

    unmapped = [title for _num, title in rows if title not in CHAPTER_TO_TERM]
    if unmapped:
        errors.append(
            "chapter-map.md has chapters with no entry in this script's "
            f"CHAPTER_TO_TERM (update the mapping): {unmapped}"
        )

    required_terms = sorted(set(
        term for term in CHAPTER_TO_TERM.values() if term is not None
    ) | set(SUPPLEMENTARY_TERMS))
    for term in required_terms:
        check_term(vocabulary, term, errors)

    if errors:
        raise SystemExit("\n".join(errors))
    print(
        f"OK: five-part chapter map enumerates 40 chapters; "
        f"Vocabulary v2 defines all {len(required_terms)} required terms "
        f"(one per Part I-IV chapter, plus {len(SUPPLEMENTARY_TERMS)} "
        f"cross-cutting terms) completely."
    )


if __name__ == "__main__":
    main()
