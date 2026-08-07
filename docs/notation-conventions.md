# Notation Conventions

Every musical example is a two-voice **ABC notation** file — piano
grand staff, harmony in the right hand, bass in the left — rendered
with [abcjs](https://abcjs.net) and played back through the shared
widget in `publish/assets/notation-head.html`. There is no separate
bass tab: the two-hand notation already carries the harmonic context
tab alone can't show (see `AGENTS.md`'s Example Curator role).

This mirrors the companion project
[Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers),
whose grand-staff format this book adopted directly, extended with the
single-word semantic annotation tags this book's vocabulary needs that
a piano-harmony book does not.

## Required ABC Header

Every canonical `.abc` file must declare these fields, in this order,
explicitly — never rely on ABC implicit defaults, so rendering is
predictable across tools:

```
X:1
T:<Example title>
C:Alessandro Bessi
R:<short style/purpose description, e.g. "Concept study", "Exercise", "Jazz-funk study", "Ballad", "Jazz-funk capstone">
M:<meter, e.g. 4/4>
L:<default note length, e.g. 1/8>
Q:<tempo, e.g. 1/4=92>
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:<key>
```

`scripts/validate_piano_prototype.py` enforces every one of these
markers (including the exact `C:Alessandro Bessi` composer credit and
the exact `%%score { RH LH }` / voice-declaration strings) on every
file under the canonical directories below — a file missing any of
them fails CI, not just review.

## Canonical Directories

```
examples/
├── laboratories/   # The Microscope: paired (or grouped) A/B/C comparison widgets,
│                    # one variable changed between panels, everything else identical
├── exercises/       # Play: one short, practicable drill per chapter
├── studies/          # The Music: one 8-16 bar original piece per chapter, indexed
│                    # in publish/studies.qmd
├── capstone/         # The one 16-bar Complete Capstone (Chapter 40) — its own
│                    # directory because it is not a per-chapter study
└── chapters/         # Legacy replacement widgets for any chapter not yet fully
                     # migrated to a canonical laboratories/exercises/studies set;
                     # wired up via LEGACY_PIANO_EXAMPLES in
                     # scripts/prepare_manuscript_for_publish.py
```

Every file's `T:` title must be unique across the whole repository —
it is the join key `validate_piano_prototype.py` uses to confirm the
standalone file and its embedded copy inside a chapter's markdown stay
byte-identical.

## Where a Chapter Embeds Its Examples

A chapter's markdown embeds the exact same ABC source as its
standalone file, inside a `<pre class="abc-source">` block wrapped in
a `<div class="score-example">` (see `book/_templates/chapter-template.md`
for the full nine-section chapter shape: Question, Mental Model,
Microscope, Listen, See, Play, Vary, The Music, Reflection). The
Microscope's two-or-more panels use a toggle instead of two static
blocks:

```html
<div data-comparison-group="some-chapter-lab">
  <div class="comparison-controls" aria-label="... comparison">
    <button type="button" data-version="A" aria-pressed="true">A — ...</button>
    <button type="button" data-version="B" aria-pressed="false">B — ...</button>
  </div>
  <div class="comparison-panel" data-version="A"> ... </div>
  <div class="comparison-panel" data-version="B" hidden> ... </div>
</div>
```

The standalone file and the embedded copy are never generated from one
another — both are hand-authored and must match exactly, which is
exactly what the validator checks.

## Inline Semantic Annotations

ABC supports positioned text annotations attached to a note:
`"^text"` renders above the staff. This book uses a short, lowercase
phrase — usually one word, sometimes two or three where a single word
would be ambiguous — attached to the left-hand (bass) voice at the
note where the concept becomes audible, never a combined multi-part
tag in the old `"^[R:...]" "_[M:...|G:...]"` style:

```abc
[V:LH] "^ground"C,,8 | "^approach"F,,2 ^F,,2 G,,4 |]
```

(Note the difference between an annotation and an accidental: `"^approach"`
is a quoted string annotation; the un-quoted `^F,,2` right after it is
an ABC sharp accidental on F. The two look similar but are unrelated
syntax.)

A tag names the one decision a bar's `## See` prose should be pointing
at, not a description of the pitch — `"^ground"`, `"^approach"`,
`"^connect"`, `"^cell"`, `"^varied"`, `"^dense"`, `"^separated"`,
`"^ostinato"`, `"^resolve"`, and their deliberate contrast tags
(`"^arbitrary"`, `"^static"`, `"^competing"`, `"^muddy"`, `"^tracks"`,
`"^coincidental"`) are typical examples, not an exhaustive or reserved
list — invent the word each new chapter actually needs.

## Multi-System Engraving

A long study that would otherwise render as one dense, hard-to-read
system can force a bar count per line with a score-local directive
placed after `%%score { RH LH }`:

```
%%barsperstaff 4
```

The player (`publish/assets/notation-head.html`) preserves this
directive per score rather than overriding it, and any example wider
than its container becomes horizontally scrollable automatically, with
the view auto-scrolling to follow the playhead during playback.

## Playback

Every embedded example gets **Full**, **Bass only**, and **Harmony
only** playback controls for free from the shared player — this is
not something an individual `.abc` file's author needs to configure.
Chord symbols are rendered but kept silent (`chordsOff: true`) so only
the two notated voices actually sound.

## Naming and Numbering

- One tune (`X:1`) per file — a chapter needing more than two
  Microscope panels uses more files, never multiple `X:` tunes packed
  into one.
- File names are kebab-case and describe the concept, not the chapter
  number (`doubling-tracks-the-melody.abc`, not `28a.abc`) — chapter
  numbers live in `docs/chapter-map.md` and in `publish/_quarto.yml`'s
  inline `# Ch.N` comments, not in filenames.
- `scripts/validate_no_drift.py` checks that every file referenced by
  `LEGACY_PIANO_EXAMPLES` and `PIANO_CHAPTERS` in
  `scripts/prepare_manuscript_for_publish.py` actually exists, and
  that no orphaned placeholder is left behind under `examples/chapters/`
  after a chapter's legacy score is retired.
