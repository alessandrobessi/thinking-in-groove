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

Same progression; the bass states the defining tone of each chord
instead of the root — F (the b3 that makes Dm7 minor), then B (the 3rd
of G7), which turns out to already be the 7th Cmaj7 needs.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The Definer: same lab, defining tones instead of roots</p>
<pre class="abc-source">
X:1
T:The Definer: same lab, defining tones instead of roots
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=92
K:C
% chapter: 02-the-definer
% role: definer
% motion: root motion
% groove: sparse
% difficulty: beginner
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression
V:Bass clef=bass
"^[R:Definer]"F,,8 | "^[R:Definer]"B,,8 | "^[R:Definer]""_[M:Pedal]"B,,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

F carries `"^[R:Definer]"` in bar 1 — the note that makes Dm7 minor
rather than major. B carries the same tag in bar 2, defining G7 as
dominant. In bar 3 the tag repeats on the identical pitch, now with a
Pedal tag underneath: B hasn't moved, but its meaning has — it's gone
from "the 3rd of G7" to "the 7th of Cmaj7" without changing.

*Bass tab for "The Definer: same lab, defining tones instead of roots" (see `examples/by-chapter/02-the-definer/` for the source files)*

```text
G|--------|--------|--------|
D|--------|--------|--------|
A|--------|--------|--------|
E|1-------|7-------|7-------|
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
