# The Pedal — Stillness Under Change

*Chapter 11 — Part 2, Harmonic Motion: How the Bass Moves the Music.*

**Term:** Pedal

**Definition:** Sustaining or repeating one bass note underneath changing harmony above it.

## Intuition

Hold one note. Let the harmony above you keep moving — chords rise, fall, resolve, reharmonize — while your note refuses to follow. The tension this creates is not a malfunction; it is one of the oldest and most reliable devices in harmony, because it lets a listener hear exactly how far the moving harmony has traveled by measuring it against something that stayed still.

## Mental Model

A **Pedal** is a bass note sustained or repeated while the harmony above it changes. It is a Harmonic Motion concept built on an apparent contradiction: the bass isn't moving, and yet the Pedal is precisely what makes the surrounding motion audible. Without a fixed reference point, a listener has to reconstruct harmonic distance chord by chord; with a Pedal underneath, every new chord is instantly measured against the same ground.

It's worth separating Pedal from the Role called Anchor. Anchor describes a job a single note performs in the moment — grounding the harmony. Pedal describes a specific technique: literal repetition or sustain of one pitch across multiple harmonic changes. A note can be an Anchor without being a Pedal (a root played once per bar, changing bar to bar, is anchoring each chord individually). A Pedal is nearly always functioning as an Anchor, but it's the sustained, unmoving quality across changes that makes it a Pedal specifically — and that unmoving quality is what generates the tension a plain Anchor doesn't.

Two flavors matter in practice. A tonic pedal holds the key center while the harmony moves away from and back to it — used to open or close a piece, or to underscore a moment of unresolved anticipation before a cadence. A dominant pedal holds the fifth degree while harmony above it moves through chords that would, without the pedal, sound resolved on their own — manufacturing suspense that only releases when the pedal finally moves.

Three things distinguish a genuine Pedal from a bass line that merely happens to repeat a note:

1. **Harmonic independence.** The note held is chosen for its relationship to the key center (usually the tonic or the dominant), not because it happens to be convenient under the first chord and gets left there by accident.
2. **Duration relative to the harmony above.** A Pedal spans multiple harmonic events — if the "chord" above only changes once, you likely have an Anchor (Chapter 1) doing ordinary work, not yet a Pedal earning its own name.
3. **A deliberate release.** A Pedal that never moves isn't a device, it's just the piece's key center; what makes it legible as a Pedal is that the listener can eventually hear it let go, and that release is where most of the term's expressive payoff lives.

## Visual Explanation

The Motion layer marks a Pedal with a flat horizontal bracket, in amber (`#D97706`), spanning the entire duration the note is held or repeated — visually distinct from Root Motion's diagonal lines precisely because nothing is moving. Above the bracket, the Role layer will typically show the Anchor icon repeated at each reiteration if the note is restruck, or a single Anchor icon at the onset if it's a genuine sustain. Seeing a long flat bracket under a busy, chord-symbol-dense passage is itself the point: the diagram makes visible how much harmonic activity is happening over how little bass motion.

A Pedal's Groove layer is almost always low-**Density** (Chapter 24) — sparse, widely spaced dots, since a note that's sustaining has little reason to be rearticulated often — and it frequently shows a **Space** (Chapter 21) marking right before the release, a beat or two of silence that sets up the walk-off. If the Groove layer under a claimed Pedal looks busy or syncopated, check whether the note is really a Pedal or has quietly turned into a **Repetition Cell** (Chapter 22) instead — the two can look similar on the page but serve very different jobs.

## Musical Example

Picture a 12-measure fusion ballad passage in D, around 66 bpm, built to showcase a dominant pedal. Bars 1-4: bass holds A (the fifth of D) in a slow, breathing rhythm — dotted-quarter, eighth, half — while the harmony above moves Bm7 to G6/9 to F#m7 to Em7, none of it resolving. Bars 5-8: the same A pedal continues, now under an Fmaj7#11 and an Ebmaj7#11 — chords increasingly distant from D major, the pedal the only thing telling the ear "we have not left D, we have only wandered from it." Bars 9-12: the pedal finally releases, walking down by step, A-G-F#-E-D, arriving on a low D exactly as the harmony above resolves to Dmaj7 — the release of both tensions, harmonic and rhythmic, at once.

A shorter, contrasting 4-bar tag could show the other flavor: a tonic pedal opening a piece, D held under a Dmaj7-Em7-Fmaj7#11-Dmaj7 progression that never really leaves home — no release needed here, because the point of a tonic pedal is usually to establish "we are here" before the piece moves anywhere at all, rather than to manufacture suspense the way the dominant pedal above does.


:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The Pedal -- worked example</p>
<pre class="abc-source">
X:1
T:The Pedal -- worked example
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=66
K:D
% chapter: 11-the-pedal-stillness-under-change
% role: anchor
% motion: pedal
% groove: low-density
% difficulty: intermediate
% harmony: Bm7 | Bm7 | G6/9 | G6/9 | F#m7 | Em7 | Fmaj7#11 | Fmaj7#11 | Ebmaj7#11 | Ebmaj7#11 | (release) | Dmaj7
V:Bass clef=bass
"^[R:Anchor]""_[M:Pedal]"A,,8 | A,,8 | A,,8 | A,,8 | A,,8 | A,,8 | A,,8 | A,,8 | "_[M:Root Motion]"A,,8 | G,,8 | ^F,,8 | E,,4 "^[R:Anchor]""_[M:Cadential Motion]"D,4 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::


## Annotated Notation

The annotated score would show one continuous amber bracket running under bars 1-8, broken only where the pedal note is restruck (visible as repeated Anchor icons in the Role layer along its length), and then a clean transition into a short Root Motion diagonal line for the stepwise release in bars 9-12 — letting a reader see, at a glance, exactly where "held" gives way to "moving" and how that moment lines up with the harmonic resolution above it.

*Bass tab for “The Pedal -- worked example” (see `examples/by-chapter/11-the-pedal-stillness-under-change/` for the source files)*

```text
G|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
D|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
A|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
E|5-------|5-------|5-------|5-------|5-------|5-------|5-------|5-------|5-------|3-------|2-------|0---10--|
```


## Practice Ideas

- Pick any four chords you like the sound of. Play them as a comping pattern on piano or guitar (or loop them) while holding a single bass note underneath all four. Try the root of the first chord, then try the fifth. Notice how differently the same four chords feel depending on which note anchors them.
- Practice releasing a pedal at different points — early, late, exactly on the downbeat of the resolving chord — and notice how the timing of the release changes the sense of relief.
- Find a recording with an obvious pedal point (dominant pedals are common at the end of a tune, right before the final tonic) and transcribe only the bass note and its rhythm. How often is it restruck versus truly sustained?
- Improvise a bass line that stays on one note for eight bars while imagining (or having someone else play) a harmony that moves freely above it. Resist the urge to move early.

## Summary

A Pedal turns stillness into a measuring stick: by refusing to move while everything above it does, a single sustained or repeated bass note makes the distance and tension of that motion audible, and its eventual release becomes one of the most dependable payoffs in the harmonic vocabulary.
