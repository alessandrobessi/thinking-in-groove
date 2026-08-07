# Examples — ABC Notation Repository

## Piano-edition sources

All new and published examples are piano grand-staff ABC files. The
right hand is labelled `Harmony`; the left hand is labelled `Bass`.
See [`docs/notation-conventions.md`](../docs/notation-conventions.md)
for the full header, directory, and annotation contract this
directory follows.

```
laboratories/  # The Microscope: controlled A/B/C comparison widgets
exercises/     # Play: one short drill per chapter
studies/       # The Music: one 8-16 bar original piece per chapter,
               # indexed in publish/studies.qmd
capstone/      # The one 16-bar Complete Capstone (Chapter 40)
chapters/      # Legacy replacement widgets for chapters not yet fully
               # migrated, wired up via LEGACY_PIANO_EXAMPLES in
               # scripts/prepare_manuscript_for_publish.py
```

Every file here must pass `python3 scripts/validate_piano_prototype.py`
and `python3 scripts/validate_no_drift.py`.

`by-chapter/` and `_lab/` contain unpublished bass-only/tab-era
material retained solely as migration source, from before this book's
pivot to a two-voice piano grand staff. Do not use those formats for
new work, do not publish their `.tab.txt` companions, and do not treat
their 3-4 bar single-progression convention as current practice.

`scripts/notation.py` also predates the piano pivot — its helpers
generate single-voice bass content with the old combined
`"^[R:...]"`/`"_[M:...|G:...]"` tag syntax and are not used by any
canonical piano-edition example in this repository. Hand-author new
`.abc` files directly against `docs/notation-conventions.md` instead.

This directory is the standalone ABC repository named as its own
deliverable in `BLUEPRINT.md`, independent of the book prose — every
file embedded in a chapter's markdown has an identical standalone copy
here, and `validate_piano_prototype.py` checks that the two never
drift apart.
