# The Connector

*Chapter 3 — Part 1, Role: What Job Is the Bass Doing?*

**Term:** Connector

**Definition:** A note whose job is to link two harmonic areas, functioning as directional passing motion.

## Intuition

If someone asks you for directions and you say "it's near the old
bakery," you've named a location. If instead you say "keep walking past
the bakery and you'll see it," you've described a path. Most of the
Roles in this Part name locations — a note that grounds, a note that
defines. A **Connector** describes a path. It isn't especially
interested in where it currently is; it's interested in getting you
convincingly to where you're going next.

You've heard this without naming it: a bass line that walks up or down
by step between two chords, filling the gap so smoothly that the arrival
feels inevitable rather than sudden. That stepwise walk is a Connector
doing its one job — making two harmonic areas feel like they were always
headed toward each other.

## Mental Model

A Connector is defined relationally: it only exists in reference to
where the bass line came from and where it's about to go. A single note
in isolation can never be identified as a Connector — you need its
neighbors. This is the sharpest contrast with the **Anchor** (Chapter 1),
which is defined by staying put regardless of context, and with the
**Definer** (Chapter 2), which is defined by what it reveals about a
single chord in place. A Connector's meaning is entirely in its
trajectory.

Two properties make a note read as a Connector rather than just an
incidental passing tone:

1. **Directionality.** The listener should be able to feel, before the
   destination arrives, that the line is headed somewhere specific —
   usually because the motion is stepwise and consistent in direction
   across the connecting notes.
2. **Placement between two structurally important points.** A Connector
   matters because of what it's between, not because of what it is. The
   same pitch, played in a context where it isn't between two
   significant harmonic events, is just a note — arguably an Anchor,
   arguably nothing in particular.

Connecting motion is closely related to, but not identical with,
**Passing Motion** (Chapter 12). The distinction this book draws: Role
answers "what job is this bass line doing," Motion answers "what
harmonic device is producing that job." A Connector is the Role; Passing
Motion is very often — though not exclusively — the Motion mechanism
that realizes it. You can also connect two harmonic areas via a leap
(an **Approach Note**, Chapter 13, taken from a distance) rather than a
stepwise walk; the Role is the same, the Motion mechanism differs.

## Visual Explanation

The Connector's Role-layer icon is **two dots joined by a shallow
curved arc** — a small bridge — in blue (`#2563EB`), spanning from the
first connecting note to the last. Unlike the Anchor's single fixed
triangle or the Definer's single diamond, the Connector's icon is
inherently plural: it needs at least two notes to draw, because the
Role itself only exists across a span.

Beneath it, the Motion layer typically shows the shallow arched slur
used for Passing Motion (amber, `#D97706`), and the Groove layer
usually shows evenly spaced, moderate-density dots — a Connector rarely
wants to be so rhythmically busy that its directional clarity gets
buried, nor so sparse that the ear loses the thread between the two
points it's bridging.

## Musical Example

The laboratory, stated plainly: the bass states the root of each
chord, one whole note per bar.

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

Same progression; short connecting runs (E-F#, A-B) fill the space
right before each new chord instead of leaping straight to the root.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The Connector: same lab, short runs instead of leaps</p>
<pre class="abc-source">
X:1
T:The Connector: same lab, short runs instead of leaps
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=92
K:C
% chapter: 03-the-connector
% role: connector
% motion: passing motion
% groove: moderate-density
% difficulty: beginner
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression
V:Bass clef=bass
"^[R:Anchor]"D,6 "^[R:Connector]""_[M:Passing Motion]"E,1 ^F,1 | G,,6 A,,1 B,,1 | "^[R:Anchor]""_[M:Cadential Motion]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

D carries `"^[R:Anchor]"` for the first six eighths of bar 1; the last
two eighths, E and F#, carry `"^[R:Connector]"` with
`"_[M:Passing Motion]"` beneath them — a short stepwise run pointing
directly at G. The same shape repeats at the end of bar 2 (A, B)
pointing at C, where the tag reverts to `"^[R:Anchor]"` the instant it
lands.

*Bass tab for "The Connector: same lab, short runs instead of leaps" (see `examples/by-chapter/03-the-connector/` for the source files)*

```text
G|--------|--------|--------|
D|--------|--------|--------|
A|-------9|--------|--------|
E|10----12|3-----57|8-------|
```


## Practice Ideas

- Take any four-chord vamp you know. Play only roots on beat 1 of each
  measure, then fill every remaining beat with a stepwise line
  connecting the current root to the next one, in whichever direction
  is shorter. Notice how the choice of direction changes the character
  of the arrival.
- Isolate the last beat of a measure before a chord change. Practice
  arriving at the new root from a half step below, then from a whole
  step above, then from a scale step below, on the same progression.
  Compare how each approach direction changes the emotional color of
  the arrival, even though all three "work."
- Practice deliberately overshooting: connect toward a target a beat
  early or a beat late relative to the chord change, and notice at what
  point the connection stops sounding intentional and starts sounding
  like a mistake. That boundary is useful information about how much
  rhythmic freedom a Connector can take before it stops reading as
  purposeful.
- Play a tune's bridge using only Anchors (root on beat 1, nothing else)
  for one chorus, then only Connectors (stepwise motion filling every
  bar) for the next chorus. Notice which sections of the form want to
  feel settled and which want to feel like they're always arriving
  somewhere.

## Summary

A Connector is a bass note or short run of notes whose entire meaning
comes from what it links — it exists to make two harmonic areas feel
like a single continuous idea rather than two separate events joined by
a jump. Where an Anchor is defined by staying still and a Definer by
what it reveals about one chord, a Connector is defined by motion with a
destination, and it disappears as a concept the moment you consider it
in isolation from its neighbors.
