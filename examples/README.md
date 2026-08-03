# Examples — ABC Notation Repository

The standalone ABC repository named as its own deliverable in
`BLUEPRINT.md`, independent of the book prose. See
[`docs/notation-conventions.md`](../docs/notation-conventions.md) for
the full file layout, header, and annotation conventions this directory
follows.

- `_template/template.abc` — a skeleton showing the required header
  fields, semantic metadata block, and inline Role/Motion/Groove tags.
  Not a real musical example.
- `by-chapter/` — one subfolder per chapter, each holding that chapter's
  `.abc` + `.tab.txt` pair. Empty until Phase 2 (Musical Language)
  composes the actual examples.
- `INDEX.md` — catalog of every example, populated as they're composed.

`scripts/notation.py` has helpers (`chord_bar`, `note_bar`, `run_bar`,
`tag`, `progression`, `widget`) for authoring these files consistently —
see its module docstring for usage.
