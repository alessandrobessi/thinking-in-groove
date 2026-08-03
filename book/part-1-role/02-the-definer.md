# The Definer

*Chapter 2 — Part 1, Role: What Job Is the Bass Doing?*

**Term:** Definer

**Definition:** A bass note chosen specifically to define chord quality (e.g. the 3rd or 7th) rather than just stating the root.

## Intuition

Play a root by itself — just one note, no context — and it tells you
almost nothing. It doesn't say major or minor. It doesn't say dominant
or maj7. A root is a location, not a description. Now play that same
root, then a third above it. Suddenly you know something you didn't
know a moment ago: whether the chord is bright or dark. That third just
did the work an entire chord symbol usually does, using a single bass
note.

That's a **Definer**: a bass note whose whole purpose is to tell you
what *kind* of chord this is, not just where it lives.

## Mental Model

Every chord has a root, which answers "where are we," and a quality —
major, minor, dominant, half-diminished, and so on — which answers
"what does it feel like to be here." The root almost never answers the
second question by itself. The notes that do answer it are the 3rd
(major or minor) and the 7th (major, minor, or diminished), and to a
lesser extent alterations like a b5 or a #9.

A bass line built entirely from **Anchors** (Chapter 1) tells the
listener where the harmony is centered but stays silent about what
color that harmony is — that job gets left entirely to whatever
instrument is playing the chord above. A Definer changes that division
of labor: the bass itself briefly states the note that reveals quality,
usually in passing, often on a weak beat or as part of a short
approach, rather than settling on it the way a keyboard player would
sustain a full voicing.

This matters most in exactly the situations where nothing else in the
arrangement is defining the chord for you — a horn hit that's just a
unison line, a guitar comping with rootless upper-structure voicings
that omit the 3rd, a moment where the harmony is implied rather than
spelled out. In a trio with a chordal instrument that voices everything
explicitly, the bass can get away with almost never defining anything.
In a stripped-down horn-and-rhythm arrangement, a bass line that never
defines quality can leave the harmony feeling unfinished no matter how
solid its Anchors are.

A useful diagnostic: if you removed every other instrument and left
only the bass, could a listener tell major from minor at each chord
change? If the answer is no more often than you'd like, the line
probably needs more Definer moments, not more notes in general.

## Visual Explanation

The Definer's Role-layer icon is a **filled diamond**, in blue
(`#2563EB`), placed above the specific note doing the defining — the 3rd
or 7th (or altered tone) rather than the root. Unlike the Anchor's
triangle, the diamond has no implied direction; it simply marks "this
note is informationally load-bearing," regardless of how long it lasts.

Because a Definer is often a short, passing event rather than a
sustained one, its diamond frequently appears on a single eighth or
sixteenth note rather than spanning a held duration the way an Anchor's
triangle might. The Motion layer beneath it is often minimal or absent
— defining quality is a harmonic-information job, not necessarily a
directional-motion job — though a Definer that arrives via a half-step
frequently doubles as an **Approach Note** (Chapter 13), in which case
both tags appear together.

## Musical Example

Picture a medium-swing jazz eighth-bar phrase in **C major**, on a
Cmaj7 chord sustained by the rhythm section for the full bar, with a
guitar comping only shell voicings that omit the 3rd (root and 7th
only) — a common, deliberately ambiguous voicing choice. On beat 1, the
bass plays C, a plain root, functioning as an Anchor. On the "and" of
beat 2, instead of staying on C or walking generically, the bass
touches **E** — the major 3rd — for a single eighth note, then returns
to C for beat 3, holding through beat 4.

That one eighth-note E is the entire example's job. Nothing else in the
band states, anywhere in that bar, whether this is Cmaj7 or Cm7. The
guitar's shell voicing is quality-neutral by design. The bass's single
Definer note is what tells the listener's ear, unambiguously, "major."


:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The Definer -- worked example</p>
<pre class="abc-source">
X:1
T:The Definer -- worked example
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=100
K:C
% chapter: 02-the-definer
% role: definer
% motion: root motion
% groove: sparse
% difficulty: beginner
% harmony: Dm7 | Dm7 | G7 | G7 | Cmaj7 | Cmaj7 | Cmaj7 | Cmaj7
V:Bass clef=bass
"^[R:Definer]"F,,8 | F,,8 | "^[R:Definer]"B,,8 | "_[M:Pedal]"B,,8 | B,,8 | B,,8 | "^[R:Anchor]""_[M:Cadential Motion]"C,8 | "_[G:Space]"C,4 z4 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::


## Annotated Notation

Notated, the C on beat 1 carries `"^[R:Anchor]"`. The E on the "and" of
beat 2 carries `"^[R:Definer]"`, with no Motion tag needed underneath it
since it isn't functioning as a passing or approach device — it's a
direct statement of quality, not a device connecting two other points.
The return to C on beat 3 goes back to `"^[R:Anchor]"`.

On the bass tab, this reads as a brief, single-fret departure in the
middle of an otherwise static passage — visually small, but the tab's
caption (per `docs/notation-conventions.md`'s semantic metadata block)
would flag it as the harmonically decisive moment in the bar, since its
importance is completely out of proportion to its duration on the page.

*Bass tab for “The Definer -- worked example” (see `examples/by-chapter/02-the-definer/` for the source files)*

```text
G|--------|--------|--------|--------|--------|--------|--------|--------|
D|--------|--------|--------|--------|--------|--------|--------|--------|
A|--------|--------|--------|--------|--------|--------|--------|--------|
E|1-------|1-------|7-------|7-------|7-------|7-------|8-------|8-------|
```


## Practice Ideas

- Take a tune with a chordal comping instrument. Ask that instrument to
  play only rootless shells (no 3rd) for an entire chorus, and take
  responsibility, in the bass, for stating the 3rd of every chord at
  least once per bar. Notice how little of the bar needs to be spent on
  that note for the quality to read clearly.
- Play a ii–V–I with nothing but roots. Record it. Then play the same
  progression using only roots and a single well-placed 3rd or 7th per
  chord. Compare how much more harmonically "finished" the second
  version sounds despite using almost the same number of notes.
- Practice distinguishing, chord by chord, whether the 3rd or the 7th is
  the more informative Definer for that specific chord. On a dominant
  7th chord, the 3rd tells you major/minor-key context while the b7
  tells you it's dominant at all — sometimes you need the 7th more than
  the 3rd, and knowing which is a Definer decision, not a default.
- On a static one-chord vamp, alternate: one chorus stating the Definer
  tone on beat 1 of every bar, the next chorus stating it only once at
  the very start of the whole vamp. Notice how the harmony's "settled"
  feeling changes depending on how often you re-confirm its quality.

## Summary

A Definer is a bass note whose job is to state chord quality — usually
the 3rd or 7th — often briefly and in passing, precisely because
nothing else in the arrangement can be relied on to do it. Where the
Anchor tells the listener where the harmony is centered, the Definer
tells them what that harmony actually sounds like, and the two Roles
frequently trade off within the same bar rather than competing for the
same note.
