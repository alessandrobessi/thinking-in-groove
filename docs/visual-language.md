# Visual Language

Every musical example in this book is shown as a **four-layer diagram**,
mirroring the book's core idea that a bass line is a stack of
simultaneous decisions.

```
[ ROLE LAYER   ]  icons above the staff        — blue   #2563EB
[ NOTATION/TAB ]  standard staff + bass tab     — black
[ MOTION LAYER ]  arcs/lines below the staff    — amber  #D97706
[ GROOVE LAYER ]  pulse timeline below the tab  — green  #16A34A
```

Integration chapters (Part IV) additionally use a fifth accent color,
purple `#7C3AED`, when showing all layers stacked together.

## Color Key

| Category | Color | Hex |
|---|---|---|
| Role | Blue | `#2563EB` |
| Harmonic Motion | Amber | `#D97706` |
| Groove | Green | `#16A34A` |
| Integration | Purple | `#7C3AED` |

## Role Layer — Icon Set (placed above the staff, at the note it applies to)

| Term | Icon description |
|---|---|
| Anchor | Filled downward triangle with a flat base (weight/grounding) |
| Definer | Filled diamond |
| Connector | Two dots joined by a shallow curved arc (a bridge) |
| Driver | A forward-pointing chevron |
| Colorist | A circle with a small sparkle/burst accent |
| Shadow | A dashed outline duplicate of the notehead |
| Voice-Leader | A short connected zig-zag line through consecutive notes |
| Commentator | A small speech-bubble glyph |

## Motion Layer — Line/Arc Set (placed below the staff)

| Term | Shape |
|---|---|
| Root Motion | Straight diagonal line between the two note stems |
| Pedal | Flat horizontal bracket spanning the sustained span |
| Passing Motion | Shallow arched slur across the passing notes |
| Approach Note | Short hook/arrow curving into the target note |
| Substituted Root | Dotted diagonal line (vs. solid for literal root motion) |
| Deceptive Motion | Diagonal line with a right-angle bend at the diversion point |
| Cadential Motion | Double vertical tick at the resolution point |
| Harmonic Rhythm | Small tick marks under each implied chord change |

## Groove Layer — Pulse Timeline (placed beneath the tab)

A horizontal row of evenly spaced tick marks represents the underlying
pulse subdivision (defined per example). Each bass note is plotted as a
dot:

| Symbol | Meaning |
|---|---|
| Filled dot centered on a tick | On the beat |
| Filled dot shifted left of a tick | Push (ahead of the beat) |
| Filled dot shifted right of a tick | Lay-back (behind the beat) |
| Hollow ring on a tick | Space / intentional rest |
| Bracket spanning several dots | Repetition Cell grouping |
| Bracket with a dashed overlay | Variation Layer (altered repeat of a cell) |

## Typography Conventions

- The first time a vocabulary term is used in a chapter, it is set in
  **bold small caps, in its category color**.
- Every chapter opens with a **Concept Card**: a small callout box with
  the term's name, its icon, and its one-sentence definition, reproduced
  verbatim from [`vocabulary.md`](vocabulary.md).
- A compact master legend (this document, condensed) is reprinted at the
  start of Part I, II, III, and IV so readers don't need to flip back to
  the introduction.

## Web edition note

In the web (HTML) edition, layers are implemented as CSS-positioned
overlays around each abcjs-rendered example rather than baked into the
ABC source itself — see
[`notation-conventions.md`](notation-conventions.md) for how Role/Motion/
Groove tags travel with the `.abc` source as semantic annotations, and
[`publish/assets/notation-head.html`](../publish/assets/notation-head.html)
for the rendering widget. Building the actual overlay renderer is a
Phase 4 (Multimedia) task, not this pass.
