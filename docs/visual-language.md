# Visual Language

This document originally specified a four-layer color-coded diagram
(Role icons, Motion arcs, a Groove pulse-timeline, all overlaid on a
single bass-clef staff plus tab) for the book's pre-pivot single-voice
format. None of it was ever built, and it doesn't fit the book's
actual format since the piano pivot — grand-staff notation carries the
harmonic context those overlays were meant to supply. This page now
describes what a chapter's visual presentation actually is today.

## What every chapter's notation actually looks like

Every musical example renders as plain two-voice grand-staff notation
via [abcjs](https://abcjs.net) — harmony in the treble clef, bass in
the bass clef — with no icon, color, or diagram overlay of any kind.
The book's four categories (Role, Motion, Groove, Interaction) are not
visually color-coded; they're distinguished entirely by which chapter
and which vocabulary term a passage is discussing, named in prose and
in the notation's own inline text tags.

**Semantic annotation** is a single short text tag — `"^ground"`,
`"^approach"`, `"^cell"`, and so on — rendered by abcjs directly above
the staff at the note it applies to, exactly as ABC's own text
annotation syntax draws it. See
[`notation-conventions.md`](notation-conventions.md) for the full tag
convention. There is no separate colored arc, icon, or pulse-dot
layer underneath it.

**The Microscope** (every chapter's controlled comparison) is a
two-button toggle — `data-version="A"` / `data-version="B"` — that
swaps which of two otherwise-identical grand-staff examples is
visible, implemented in plain HTML/CSS/JS in
[`publish/assets/notation-head.html`](../publish/assets/notation-head.html),
not as a custom diagram.

**Playback** offers Full, Bass only, and Harmony only controls per
example, with the view auto-scrolling to follow the playhead on any
example wide enough to need horizontal scrolling. This is the entire
current "visual language" beyond standard music notation: two voices,
one text tag per note of interest, one comparison toggle, three
playback buttons.

## What's deliberately not built

`AGENTS.md`'s Example Curator role and `BLUEPRINT.md` both still name
an eventual richer visual/animation layer — "Notaroll animation" per
example — as a longer-term goal, distinct from and unrelated to this
document's original icon-set design. That remains a real possibility
for a future phase, but nothing about its actual look, its
integration with the grand-staff notation above, or which concepts it
would visualize has been designed yet. Do not resurrect this
document's retired icon/color/pulse-timeline specification as a
substitute for that decision — if and when a Notaroll-based visual
layer is designed, it should be specified fresh, against the book's
actual current format, not against the single-voice-plus-tab format
this page used to describe.

## Typography

- The first time a vocabulary term is used in a chapter, set it in
  **bold**; do not re-bold it on later mentions in the same chapter
  (see `style-guide.md`).
- Chord symbols are shown on the staff (via ABC's own chord-symbol
  syntax) but rendered silent during playback (`chordsOff: true`) so
  only the two notated voices actually sound.
