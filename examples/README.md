# Examples — ABC Notation Repository

The standalone ABC repository named as its own deliverable in
`BLUEPRINT.md`, independent of the book prose. See
[`docs/notation-conventions.md`](../docs/notation-conventions.md) for
the full file layout, header, and annotation conventions this directory
follows — in particular the Laboratory Progression convention: every
chapter's examples are short (3-4 bar) variations on one fixed
**Dm7 – G7 – Cmaj7** progression, in the style of the companion project
[Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers),
rather than standalone 8-16 measure pieces.

- `_lab/laboratory.abc` — the shared baseline widget (the progression
  stated plainly, root per bar), embedded at the start of every
  chapter's Musical Example section.
- `_template/template.abc` — a skeleton showing the required header
  fields, semantic metadata block, and inline Role/Motion/Groove tags.
  Not a real musical example.
- `by-chapter/` — one subfolder per chapter, each holding that
  chapter's term-specific widget(s): `NN-slug.abc` (+ `.tab.txt`), and
  an optional second contrasting widget `NN-slug-2.abc` (+ `.tab.txt`).
- `INDEX.md` — catalog of every example, including the shared baseline.

`scripts/notation.py` has helpers (`chord_bar`, `note_bar`, `run_bar`,
`tag`, `progression`, `widget`) for authoring these files consistently —
see its module docstring for usage.
