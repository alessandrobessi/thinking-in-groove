# Notation Conventions

Every musical example has one source-of-truth file: an **ABC notation**
file. Bass tab is a hand-authored companion file kept in sync with it.
This mirrors the approach used in the companion project
[Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers),
adapted for a single bass-clef voice instead of a two-hand piano grand
staff, and extended with the Role/Motion/Groove semantic tags this book
needs that a piano-harmony book does not.

## The Laboratory Progression

Following Thinking in Layers' method of fixing one progression
(**Dm7 – G7 – Cmaj7**) so the ear can isolate what changes between
examples, every chapter's musical examples are built on that same
three-chord laboratory rather than a new key/groove per chapter. This
also means a Groove/Role/Motion chapter shows its idea as a *variation
on a shared, already-familiar baseline* rather than as a new standalone
piece:

1. **The baseline widget** — the laboratory stated plainly: the bass
   states the root of each chord, one whole note per bar, no rhythmic
   or harmonic device applied. This widget's `.abc` is identical
   everywhere it appears (`examples/_lab/laboratory.abc`), so a reader
   who has seen it once recognizes it immediately in every later
   chapter.
2. **One or two term-specific widgets** — the *same* three-bar
   laboratory, with exactly one variable changed to demonstrate the
   chapter's term, each captioned precisely about what differs from
   the baseline (e.g. "Same progression; the bass holds D under G7
   instead of moving to G"). This mirrors Thinking in Layers' practice
   of pairing a "stacked" and an "arpeggiated" version of the same
   material rather than composing a new, unrelated example each time.

Examples stay short — typically 3-4 bars, one per chord of the
laboratory (occasionally a 4th turnaround bar) — not the 8-16 measure
miniature compositions `ROADMAP.md`'s Phase 2 originally described.
Longer, freely-composed pieces belonging to that original vision may
still be worth producing later as a separate "repertoire" pass, but
the primary teaching examples embedded in each chapter now follow this
laboratory-and-variation model instead.

A few Integration-category terms (the Groove Contract, in particular)
describe a promise made and kept/broken across a full phrase, which
can't be isolated in 3-4 bars — those examples loop the laboratory
several times rather than shrinking it, and stay phrase-length.

## Two places notation lives

1. **`examples/by-chapter/<NN>-<term-slug>/`** — the standalone ABC
   repository named as its own deliverable in `BLUEPRINT.md`. One example
   = one `.abc` file + one companion `.tab.txt` file. This is the
   source of truth, independently versionable and reusable outside the
   book.
2. **Inline in `book/part-*/NN-*.md`** — when Phase 3 writing embeds an
   example directly in the prose (so sound and explanation stay
   adjacent, as in Thinking in Layers), it uses the same `.abc` content
   wrapped in the widget markup produced by `scripts/notation.py`'s
   `widget()` helper. The standalone file under `examples/` and the
   embedded copy must stay identical — `widget()` is the single place
   that formats the wrapper, so there is only one place to update.

## File Layout Per Example

```
examples/_lab/
├── laboratory.abc              # the shared baseline widget, referenced by every chapter
└── laboratory.tab.txt

examples/by-chapter/<NN>-<term-slug>/
├── <NN>-<term-slug>.abc        # primary term-specific widget
├── <NN>-<term-slug>.tab.txt
├── <NN>-<term-slug>-2.abc      # optional second contrasting widget
└── <NN>-<term-slug>-2.tab.txt
```

- `NN` = two-digit chapter number (from `docs/chapter-map.md`), e.g. `01`.
- `term-slug` = kebab-case chapter concept, e.g. `the-anchor` → `01-the-anchor`.
- A chapter's `## Musical Example` section embeds the baseline widget
  first, then its own term-specific widget(s), each with a caption
  that names the one thing that changed. Once the baseline has been
  shown a few times (e.g. by Part II), a chapter whose own widget is
  itself nearly identical to the baseline may cross-reference an
  earlier chapter by number instead of re-embedding it a fourth or
  fifth time — judgment over mechanical repetition.

## Required ABC Header Fields

Every `.abc` file must declare these explicitly — never rely on ABC
implicit defaults, so rendering is predictable across tools (abcjs
today, other renderers later):

```
X:1
T:<Example title>
C:Thinking in Groove
M:<meter, e.g. 4/4>
L:<default note length, e.g. 1/8>
Q:<tempo, e.g. 1/4=100>
K:<key>
```

Following `scripts/notation.py`'s convention, examples use a single
shared unit length, `L:1/8`, so every bar is a genuine measure at that
meter with no scaled fictions.

## Semantic Annotation Block (whole-piece metadata)

A `%` comment block (plain comment lines, ignored by every ABC
renderer — deliberately *not* `%%` directives, which some renderers do
interpret) immediately follows the header:

```
% chapter: 01-the-anchor
% role: anchor
% motion: pedal
% groove: syncopated, low-density
% difficulty: beginner
```

## Inline Semantic Annotations (per-note tags)

ABC supports positioned text annotations around a note: `"^text"` above
the staff, `"_text"` below. We standardize their use as follows:

- **Role tag** (above the staff): `"^[R:Anchor]"`
- **Motion + Groove tags** (below the staff, combined with a pipe):
  `"_[M:Pedal|G:Push]"`

Example fragment:

```abc
X:1
T:The Anchor — worked fragment
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=90
K:Cmaj
% chapter: 01-the-anchor
% role: anchor
% motion: pedal
% groove: low-density
"^[R:Anchor]"C,4 "_[M:Pedal]"C,4 | C,2 "^[R:Connector]"D,2 "_[M:Passing Motion]"E,2 F,2 |
```

## Phrase-Level Annotations

Most semantic tags mark a single note. A few Integration-category terms
(Chapter 28's Groove Contract, in particular) describe a span of
measures instead. For these, add a `%` comment line at the start of the
relevant measure group, in addition to whatever per-note Role/Motion/
Groove tags those measures already carry:

```
% contract: set
% contract: broken
% contract: restored
```

## Bass Tab Convention

Tab is authored manually (auto-generation from ABC is a Phase 4 tooling
candidate, not built now) as a plain ASCII 4-string tab block, string
order G/D/A/E top-to-bottom, aligned by beat with the `.abc` file's
rhythm:

```
G|----------------|
D|----------------|
A|----------------|
E|0---0---1---3---|
```

- Default target instrument: 4-string bass, standard tuning (E A D G).
- 5-string/extended-range notation is deferred to a later phase.

## Naming, Numbering, and Indexing

- One tune (`X:1`) per file — keeps each example independently
  embeddable, matching Thinking in Layers' one-`X:1`-per-widget rule.
  A chapter needing more than one comparison widget uses more files
  (see File Layout above), never multiple `X:` tunes packed into one.
- Every new example is added to `examples/INDEX.md` with: chapter,
  title, role/motion/groove tags, difficulty.
- Chapter numbering in `examples/`, `book/`, and `publish/_quarto.yml`
  must always agree — this is exactly what
  `scripts/validate_book_structure.py` checks for `book/`, and the same
  discipline applies by convention to `examples/`.
