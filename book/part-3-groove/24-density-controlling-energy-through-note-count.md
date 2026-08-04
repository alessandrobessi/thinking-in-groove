# Density — Controlling Energy Through Note Count

*Chapter 24 — Part 3, Groove: How the Bass Creates Feel.*

**Term:** Density

**Definition:** The number of note-events per beat/measure, controlling perceived energy.

## Intuition

A bass line built from four whole notes and a bass line built from
thirty-two sixteenth notes can sit under the exact same chord, at the
exact same tempo, played by a bassist with the exact same technical
command — and still produce completely different amounts of perceived
energy. Neither line is more correct. They are simply set to different
Density: how many note-events happen per unit of time. Density is
independent of volume, tempo, and technical difficulty; it is purely a
question of how many events the ear has to track per beat.

## Mental Model

Density is best thought of as a dial, not a binary. Useful reference
points along that dial:

- **Very low density** — one note per bar or slower (whole notes, tied
  notes across bar lines). Reads as spacious, patient, often used
  under a busy melody or solo where the harmony needs to breathe.
- **Low density** — one note per beat (quarter notes in 4/4). The
  default "walking" feel in many styles; present but unobtrusive.
- **Moderate density** — two notes per beat (eighth notes). Active
  enough to drive the time forward without overwhelming other voices.
- **High density** — four or more notes per beat (sixteenth notes,
  triplets, ghost-noted funk patterns). Reads as urgent, virtuosic, or
  aggressive, and tends to compete for the listener's attention with
  anything else happening rhythmically at the same time.

Density interacts with, but is distinct from, everything covered so far
in Part III. A high-density line can still sit in a relaxed Pocket
(Chapter 19); a low-density line can still contain a sharp Syncopation
Point (Chapter 20). A Repetition Cell (Chapter 22) has an inherent
density baked into its rhythm, but the same cell's *density* can be
raised or lowered independently by adding or removing subdivisions,
while its identity (its syncopations, its rests, its overall shape)
stays recognizable — density is one more axis a Variation Layer
(Chapter 23) can act on.

The reason Density earns its own chapter, rather than being folded into
the Repetition Cell, is that it is often the single most direct lever
for controlling a section's energy across a whole arrangement — raising
density under a bridge, or dropping it to near nothing under a vocal
entrance, without changing harmony, Role, or tempo at all.

## Visual Explanation

Density is read directly off the Groove-layer pulse timeline (green,
`#16A34A`) as the count of filled dots occupying a given stretch of
ticks — a sparse timeline with wide gaps between dots represents low
density; a timeline crowded with dots on nearly every tick represents
high density. Unlike the other Groove terms in this Part, Density has no
dedicated symbol of its own — it is read from the overall population of
the existing dot notation, which is why it pairs so naturally with
side-by-side comparison: two timelines of equal length, one sparse and
one crowded, make the concept visible at a glance without needing a new
graphic convention.

## Musical Example

Take the laboratory progression and change the note count under the
middle chord only.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The laboratory, stated plainly: the bass states the root of each chord, one whole note per bar. Every chapter's example below is a short variation on exactly this.</p>
<pre class="abc-source">
X:1
T:The Laboratory: Dm7 - G7 - Cmaj7, bass states the root
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=88
K:C
% chapter: lab-baseline
% role: anchor
% motion: root motion
% groove: none (plain reading)
% difficulty: beginner
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression used throughout the book
V:Bass clef=bass
"^[R:Anchor]""_[M:Root Motion]"D,8 | "^[R:Anchor]""_[M:Root Motion]"G,,8 | "^[R:Anchor]""_[M:Root Motion]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

Same progression; Dm7 and Cmaj7 stay at the laboratory's original low
density, but G7 explodes into eight notes per bar — density as a
deliberate, temporary choice, not a constant setting.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">Density: same lab, G7 explodes into eight notes</p>
<pre class="abc-source">
X:1
T:Density: same lab, G7 explodes into eight notes
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=96
K:C
% chapter: 24-density-controlling-energy-through-note-count
% role: n/a
% motion: n/a
% groove: contrast: low then high density
% difficulty: beginner
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression
V:Bass clef=bass
"_[G:Density]"D,8 | G,,1 A,,1 G,,1 A,,1 G,,1 A,,1 G,,1 A,,1 | C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

Bars 1 and 3 keep the laboratory's single whole-note root, untagged for
Groove. Bar 2 carries `"_[G:Density]"` at its first note, where eight
separate eighth-note attacks (alternating G and its 9th, A) replace the
single whole note the baseline used — the Role (`"^[R:Anchor]"`,
unstated but implied by continuity) hasn't changed, only how many times
per bar it gets restated.

*Bass tab for "Density: same lab, G7 explodes into eight notes"*

```text
G|--------|--------|--------|
D|--------|--------|--------|
A|--------|--------|--------|
E|10------|35353535|8-------|
```


## Practice Ideas

- **Four-density ladder.** Take one simple harmonic idea (a single
  chord, or a short progression) and play it at four increasing
  densities in succession — one note per bar, one per beat, two per
  beat, four per beat — without changing pitch content. Notice at
  which step the perceived energy shift feels largest.
- **Density under a melody.** Practice accompanying a melody or a
  soloist at deliberately low density during their most active
  passages, and higher density during their sparsest ones — using
  Density as a conversational, complementary tool rather than a fixed
  personal setting.
- **Match a record's density curve.** Transcribe how a bass line's note
  count per bar changes across a full arrangement (verse, chorus,
  bridge) on a recording you admire, and identify where the arranger
  used a density shift to mark a structural change.
- **Constant density, changing everything else.** As a contrast drill,
  hold density perfectly fixed (say, strictly one note per beat) across
  a full chorus while varying Role, Motion, and pitch freely — this
  isolates Density as its own axis by proving how much else can change
  while it stays constant.

## Summary

Density is the number of note-events per beat or measure, and it
functions as an independent, direct control over a bass line's
perceived energy — separate from Role, Motion, Pocket, or pitch content
entirely. Because it can be changed without altering anything else, it
is one of the most efficient tools available for shaping the energy of
a section, and it is a natural parameter for the Variation Layer
(Chapter 23) to act on when keeping a Repetition Cell alive over time.
