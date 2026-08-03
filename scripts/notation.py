#!/usr/bin/env python3
"""Helpers for authoring the book's embedded ABC notation + audio widgets.

Not part of the Quarto build -- this is an authoring-time tool used
while writing the book/*.md chapter files and the examples/ ABC
repository by hand.

Adapted from the sibling project Thinking in Layers' scripts/notation.py
for a single bass-clef voice (bass guitar has one voice, not two hands)
and extended with the Role/Motion/Groove inline annotation tags this
book's notation conventions require -- see docs/notation-conventions.md.

Every widget in the book uses one shared unit length, L:1/8, and every
bar is a genuine 4/4 measure: exactly 8 eighth-note units, always. This
lets chord blocks (`chord_bar`), rests (`rest_bar`), sustained roots
(`note_bar`), and short runs (`run_bar`) sit in the same tune without
ever changing L: mid-piece, and means the displayed time signature is
never a scaled fiction.

    >>> from notation import note_bar, tag, progression
    >>> progression([
    ...     tag(note_bar("C", 2), role="Anchor", motion="Pedal"),
    ...     tag(note_bar("C", 2), groove="Push"),
    ... ])
"""
import re

BAR_UNITS = 8  # eighth-note units per 4/4 bar, at L:1/8

LETTER_POS = {"C": 0, "D": 1, "E": 2, "F": 3, "G": 4, "A": 5, "B": 6}


def _spell(name: str):
    """'C', 'C#', 'Bb' -> (letter, accidental_prefix)."""
    letter = name[0].upper()
    acc = ""
    if len(name) > 1:
        if name[1] == "#":
            acc = "^"
        elif name[1] == "b":
            acc = "_"
    return letter, acc


def _to_abc(letter: str, octave: int) -> str:
    if octave >= 5:
        return letter.lower() + ("'" * (octave - 5))
    return letter.upper() + ("," * (4 - octave))


def _ascending_tokens(names, base_octave):
    """Ascend note-by-note, bumping the octave only when the letter
    genuinely wraps downward (e.g. G then C). Consecutive notes on the
    *same* letter (C then C#, a chromatic neighbor) must NOT bump the
    octave -- they're a half step apart, not a 7th."""
    out = []
    octave = base_octave
    prev_pos = -1
    for name in names:
        letter, acc = _spell(name)
        pos = LETTER_POS[letter]
        if pos < prev_pos:
            octave += 1
        out.append(acc + _to_abc(letter, octave))
        prev_pos = pos
    return out


def chord(names, base_octave=2):
    """Spell `names` (e.g. ["E","G","B"]) as an ascending closed voicing
    starting at `base_octave` (2 = a low bass register)."""
    return "".join(_ascending_tokens(names, base_octave))


def note(name, octave=2):
    """Single note token, e.g. note('E', 2) -> 'E,,'; note('G', 3) -> 'G,'."""
    letter, acc = _spell(name)
    return acc + _to_abc(letter, octave)


def chord_bar(names, base_octave=2, units=BAR_UNITS):
    """One full 4/4 bar: `names` stacked as a chord, held for the whole bar."""
    return f"[{chord(names, base_octave)}]{units}"


def rest_bar(units=BAR_UNITS):
    """One full 4/4 bar of silence."""
    return f"z{units}"


def note_bar(name, octave=2, units=BAR_UNITS):
    """One full 4/4 bar: a single sustained note (typically the root)."""
    return f"{note(name, octave)}{units}"


def run_bar(names, base_octave=2, note_units=1):
    """A short melodic run within one 4/4 bar: each note in `names` gets
    `note_units` eighth-units, left-aligned, padded with a trailing rest
    to fill out the bar. Raises if the run doesn't fit."""
    tokens = _ascending_tokens(names, base_octave)
    used = len(tokens) * note_units
    if used > BAR_UNITS:
        raise ValueError(f"run of {len(tokens)} notes at {note_units} units each "
                          f"needs {used} units, more than one 4/4 bar ({BAR_UNITS})")
    out = " ".join(t + (str(note_units) if note_units != 1 else "") for t in tokens)
    remainder = BAR_UNITS - used
    if remainder:
        out += f" z{remainder}"
    return out


def custom_bar(token_units):
    """A bar built from explicit (token, units) pairs, e.g.
    custom_bar([("E,,",1), ("z",1), ("G,,",2), ("z",4)]) for a hand-timed
    rhythm. Units must sum to BAR_UNITS."""
    total = sum(u for _, u in token_units)
    if total != BAR_UNITS:
        raise ValueError(f"bar sums to {total} units, not {BAR_UNITS}")
    return " ".join(f"{tok}{u}" for tok, u in token_units)


def tag(token: str, role: str = None, motion: str = None, groove: str = None) -> str:
    """Prefix `token` (the first note/chord of a bar, or a whole bar
    string) with Role/Motion/Groove inline annotations per
    docs/notation-conventions.md: Role goes above the staff, Motion and
    Groove are combined below it.

        >>> tag(note_bar("E", 2), role="Anchor", motion="Pedal")
        '"^[R:Anchor]""_[M:Pedal]"E,,8'
    """
    prefix = ""
    if role:
        prefix += f'"^[R:{role}]"'
    below_parts = []
    if motion:
        below_parts.append(f"M:{motion}")
    if groove:
        below_parts.append(f"G:{groove}")
    if below_parts:
        prefix += f'"_[{"|".join(below_parts)}]"'
    return prefix + token


def widget(caption: str, abc_body: str) -> str:
    abc_body = abc_body.strip("\n")
    return (
        '\n:::{.content-hidden when-format="epub"}\n\n'
        "```{=html}\n"
        '<div class="score-example">\n'
        f'<p class="abc-caption">{caption}</p>\n'
        '<pre class="abc-source">\n'
        f"{abc_body}\n"
        "</pre>\n"
        '<div class="abc-rendered"></div>\n'
        '<button class="abc-play" type="button">▶ Play</button>\n'
        "</div>\n"
        "```\n\n"
        ":::\n"
    )


def progression(bars, key="C", clef="bass"):
    """Assemble a single-voice bass tune. Every bar is a real 4/4
    measure at L:1/8 -- see module docstring. `bars` is a list of
    already-built bar strings (chord_bar/rest_bar/note_bar/run_bar/tag,
    etc.), one per measure."""
    line = " | ".join(bars) + " |]"
    header = f"X:1\nM:4/4\nL:1/8\nK:{key}\n"
    return header + f"V:Bass clef={clef}\n" + line


if __name__ == "__main__":
    # smoke test
    print(chord_bar(["E", "G", "B"]))
    print(note_bar("E", 2))
    print(run_bar(["E", "G", "A", "B", "D"], base_octave=2, note_units=1))
    print(tag(note_bar("E", 2), role="Anchor", motion="Pedal"))
    print(widget("Test", progression([
        tag(note_bar("C", 2), role="Anchor", motion="Pedal", groove="Push"),
        tag(note_bar("C", 2), motion="Pedal"),
        tag(run_bar(["C", "D", "E", "F"], base_octave=2), role="Connector", motion="Passing Motion"),
    ])))
