#!/usr/bin/env python3
"""Validate the structural contract of canonical piano-edition ABC files."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIRS = ("laboratories", "exercises", "studies", "comparisons", "capstone")
REQUIRED = (
    "X:",
    "T:",
    "C:Alessandro Bessi",
    "R:",
    "M:",
    "L:",
    "Q:",
    "%%score { RH LH }",
    'V:RH clef=treble name="Harmony"',
    'V:LH clef=bass name="Bass"',
    "K:",
    "[V:RH]",
    "[V:LH]",
)


def bars(voice: str) -> int:
    return voice.replace("|]", "|").count("|")


def main() -> None:
    files = sorted(
        path
        for name in CANONICAL_DIRS
        for path in (ROOT / "examples" / name).glob("*.abc")
    )
    if not files:
        raise SystemExit("no canonical piano examples found")

    errors: list[str] = []
    player = (ROOT / "publish/assets/notation-head.html").read_text()
    if "chordsOff: true" not in player:
        errors.append("player must keep chord symbols silent with chordsOff: true")
    if "var result = await synth.prime()" not in player or "|| 4" in player:
        errors.append("player must time completion from prime() without a short fallback")
    sources_by_title: dict[str, tuple[Path, str]] = {}
    for path in files:
        text = path.read_text()
        title_match = re.search(r"^T:(.+)$", text, re.MULTILINE)
        if title_match:
            sources_by_title[title_match.group(1)] = (path, text.strip())
        for marker in REQUIRED:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing {marker!r}")
        if "tab" in text.lower():
            errors.append(f"{path.relative_to(ROOT)}: tablature reference in canonical source")
        rh = text.partition("[V:RH]")[2].partition("[V:LH]")[0]
        lh = text.partition("[V:LH]")[2]
        if bars(rh) != bars(lh):
            errors.append(
                f"{path.relative_to(ROOT)}: RH/LH bar mismatch ({bars(rh)} != {bars(lh)})"
            )
        if path.parent.name == "studies" and not 8 <= bars(rh) <= 16:
            errors.append(
                f"{path.relative_to(ROOT)}: study must contain 8–16 bars, found {bars(rh)}"
            )

    a = (ROOT / "examples/laboratories/inverter-root.abc").read_text()
    b = (ROOT / "examples/laboratories/inverter-first-inversion.abc").read_text()
    a_rh = a.partition("[V:RH]")[2].partition("[V:LH]")[0]
    b_rh = b.partition("[V:RH]")[2].partition("[V:LH]")[0]
    # Chord-symbol text names the resulting inversion; sounded RH tokens must match.
    strip_symbols = lambda value: "".join(value.split('"')[::2]).strip()
    if strip_symbols(a_rh) != strip_symbols(b_rh):
        errors.append("inverter A/B pair changes sounded right-hand material")

    embedded_by_title: dict[str, str] = {}
    for chapter in sorted((ROOT / "book/part-1-role").glob("*.md")):
        for abc in re.findall(
            r'<pre class="abc-source">(.*?)</pre>', chapter.read_text(), re.DOTALL
        ):
            title_match = re.search(r"^T:(.+)$", abc, re.MULTILINE)
            if title_match:
                embedded_by_title[title_match.group(1)] = abc.strip()
    for title, (path, source) in sources_by_title.items():
        embedded = embedded_by_title.get(title)
        if embedded is None:
            errors.append(f"{path.relative_to(ROOT)}: not embedded in a piano chapter")
        elif embedded != source:
            errors.append(f"{path.relative_to(ROOT)}: embedded ABC copy has drifted")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: {len(files)} canonical piano examples satisfy the prototype contract.")


if __name__ == "__main__":
    main()
