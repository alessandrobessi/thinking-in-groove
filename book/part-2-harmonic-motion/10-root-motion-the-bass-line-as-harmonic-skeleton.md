# Root Motion — The Bass Line as Harmonic Skeleton

*Chapter 10 — Part 2, Harmonic Motion: How the Bass Moves the Music.*

**Term:** Root Motion

**Definition:** The interval and direction between successive chord roots as stated by the bass.

## Intuition

Play a bass note. Play another. Before either has a Role, before either has a groove, the fact that you moved from one pitch to the other already carries information: it moved up, or down, by some distance. That movement — independent of what the bass is doing on top, independent of feel — is the harmony's skeleton. Take any progression away from its melody, its voicings, its rhythm, and the bass roots by themselves still trace something the ear can follow.

Sing just the roots of a tune you know, with no rhythm, no harmony above it, nothing but the sequence of pitches a bass player would land on. It still sounds like something. That residual shape, left over after everything else has been stripped away, is Root Motion.

## Mental Model

**Root Motion** is the interval and direction between the roots of successive chords, exactly as the bass states them. It is the most literal layer of Harmonic Motion: not what a note implies (Substituted Root, Chapter 14), not where a note is heading (Approach Note, Chapter 13), just the plain fact of "we were on this pitch, now we are on that one, and here is the distance and direction between them."

Three things make Root Motion worth naming as its own concept rather than something you absorb by osmosis:

1. **Distance changes weight.** A leap of a fourth or fifth reads as structural, almost architectural — the harmony's foundation visibly shifting. A step reads as incremental, almost conversational. The size of the interval is information a listener processes before they've identified a single chord quality.
2. **Direction changes character even at identical distance.** A descending fifth (G to C) reads as resolution, almost by physical law of the overtone series — it's the interval a fundamental and its strongest overtone share, and Western tonal harmony has trained several centuries of listeners to hear it as arrival. An ascending fourth is the same two pitch classes and, taken as raw acoustics, nearly the same relationship — yet it reads as a push forward rather than a settling, because rising motion in general carries more urgency than falling motion for most listeners.
3. **Repeated patterns name a harmonic language.** A passage that moves mostly by fourths and fifths is speaking functional, cycle-of-fifths harmony. One that moves mostly by step is closer to modal or through-composed writing. One that favors thirds is often in more chromatic, cinematic territory. Naming the dominant interval in a passage tells you what kind of harmonic language you're in before you've analyzed a single chord symbol.

Root Motion is also the term every other concept in this Part either specializes or complicates. An Anchor (Chapter 1) is, from the Motion side, often just a moment of zero Root Motion — the same root repeated rather than changed. A Connector (Chapter 3) is a Role built almost entirely out of directional Root Motion aimed at a destination. Cadential Motion (Chapter 16) is Root Motion's strongest pattern — the descending fifth — deployed specifically at a phrase's end. Deceptive Motion (Chapter 15) is a Root Motion path that changes destination mid-flight, and a Substituted Root (Chapter 14) is a root chosen to reinterpret rather than simply state the harmony. None of these replace Root Motion; they all borrow it for a more specific purpose, which is why it's introduced first in this Part — everything after it in Part II assumes you can already hear plain interval and direction on their own.

## Visual Explanation

In the four-layer diagram from `docs/visual-language.md`, Root Motion is drawn as a straight diagonal line between the two note stems it connects, in the Motion layer's amber (`#D97706`). The line's slope is not decorative: a steep line signals a large leap (a fourth or more), a shallow line signals stepwise motion, and the direction of the slope — rising left to right or falling — is the direction of the root movement itself. Where a bass line contains several consecutive Root Motion events, the diagram reads almost like a simple melodic contour drawn underneath the actual notation: you can see the skeleton's shape before you've read a single pitch name.

This is the plainest of the Motion-layer shapes, and every other Motion symbol in this Part is a variation on it: Substituted Root (Chapter 14) uses the same diagonal line but dotted, to mark a root that's reinterpreting the harmony rather than literally changing it; Deceptive Motion (Chapter 15) uses the same diagonal line but with a bend in it, to mark a path that changed destination mid-flight; Cadential Motion (Chapter 16) adds a double-tick at the end of a Root Motion line to mark that this particular arrival is also a phrase boundary. Learning to read a plain diagonal line first is what makes those later, modified versions legible.

## Musical Example

Imagine an 8-measure funk-jazz phrase in C, tempo around 96 bpm, built specifically to make Root Motion audible on its own, stripped of harmonic color. Bars 1-2: root on C, held as a Driver-style eighth-note pulse, then a leap down a fifth to F for bars 3-4 — a classic descending-fifth motion, the strongest possible directional pull in the vocabulary. Bars 5-6: from F, a leap up a fourth to Bb, restating the same distance in the opposite direction, so the ear can compare "down a fifth" against "up a fourth" (the same two pitch classes, opposite motion, different effect). Bars 7-8: a stepwise descent, Bb to A to G, arriving back at C by contrary means — proving that you can reach the same destination by leap or by step, and that the journey changes the character of the arrival even when the destination doesn't change.

A second, contrasting 4-bar tag could extend the idea into third-related motion: from the C arrival, a leap down a major third to Ab, then back up a major third to C — a relationship common in more chromatic, cinematic harmony and audibly different in character from the cycle-of-fifths motion in bars 1-6, even though both are still, plainly, Root Motion.

Each root change would carry a `"_[M:Root Motion]"` tag in the annotated score, letting a reader see exactly where the interval changes even before comparing pitches by ear.


:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">Root Motion -- worked example</p>
<pre class="abc-source">
X:1
T:Root Motion -- worked example
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=100
K:C
% chapter: 10-root-motion-the-bass-line-as-harmonic-skeleton
% role: n/a
% motion: root motion
% groove: moderate-density
% difficulty: beginner
% harmony: Dm7 | Dm7 | G7 | G7 | Cmaj7 | Cmaj7 | Am7 | Am7
V:Bass clef=bass
"_[M:Root Motion]"D,8 | D,8 | "_[M:Root Motion]"G,,8 | G,,8 | "_[M:Root Motion]"C,8 | C,8 | "_[M:Root Motion]"A,,8 | A,,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::


## Annotated Notation

Once notated, this example's annotated score would show a Motion-layer diagonal line at each of the three root changes in the main phrase: a steep downward line (fifth) between bars 2 and 3, a steep upward line (fourth) between bars 4 and 5, and three shallow stepwise lines across bars 6 through 8. The optional third-related tag would add two more diagonal lines of a visibly different steepness (a third is neither a leap nor a step), giving a reader three distinct slopes to compare side by side. Comparing the steepness and direction of these lines is the fastest way to internalize how much information is carried by root movement alone, before any chord quality is even glanced at.

*Bass tab for “Root Motion -- worked example” (see `examples/by-chapter/10-root-motion-the-bass-line-as-harmonic-skeleton/` for the source files)*

```text
G|--------|--------|--------|--------|--------|--------|--------|--------|
D|--------|--------|--------|--------|--------|--------|--------|--------|
A|--------|--------|--------|--------|--------|--------|--------|--------|
E|10------|10------|3-------|3-------|8-------|8-------|5-------|5-------|
```


## Practice Ideas

- Take any tune you already know and, away from your instrument, sing or hum only the root of each chord change in time. Notice which changes feel like falling into place and which feel like a push.
- On your instrument, play only roots through a full chorus of a standard, in quarter notes, ignoring rhythm, color, and role entirely. Ask yourself after each change: was that a leap or a step, and which direction?
- Take a ii-V-I and play its roots in as many different Root Motion "routes" as you can invent — by leap, by step, ascending, descending — while keeping the underlying harmony identical. Notice how much the harmony's felt direction changes even though the chords themselves haven't.
- Transcribe eight bars of a bass line you admire and reduce it to nothing but its root-to-root intervals. Does the piece favor fourths and fifths, steps, or thirds? What does that tell you about its harmonic language, and does it match what you'd guess from the genre alone?

## Summary

Root Motion is the plainest fact a bass line states — how far, and which way, the harmony's foundation just moved — and it shapes a listener's sense of direction and resolution independent of chord quality, rhythm, or anything layered on top of it. Every other Harmonic Motion concept in this Part refines or complicates this one fact; none of them replace it.
