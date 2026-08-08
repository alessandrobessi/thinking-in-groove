# Ballad and Inversion Study

*Chapter 39 — Part V, Design: Building Complete Bass Lines. Sparse inversions create slow emotional direction.*

## The Question

Can a bass line move continuously downward across several bars while playing nothing but correct, plain chord tones — no passing notes, no approach notes, nothing borrowed from outside the harmony?

## The Mental Model

A **Ballad and Inversion Study** applies a device the rest of this book has mostly set aside: the same chord can put a different one of its own chord tones in the bass, and that choice alone — its inversion — can create direction. Cmaj7's root is C, but its seventh, B, is just as legitimate a bass note under the identical chord. Restate Cmaj7 with B in the bass instead of C, and the bass has moved a half step down without the harmony changing at all, using nothing but a different, still entirely correct, voicing of the same chord.

Strung together across a slow ballad, this lets a bass line trace a long, continuous shape — usually descending, sometimes rising — using only sparse, widely spaced notes, each one a true chord tone of whatever's sounding at that instant. This is a genuinely different mechanism from Part II's Passing Motion or Approach Notes, which borrow non-chord tones to connect two points. An inversion doesn't borrow anything: every note the bass plays already belongs to the chord above it. The direction comes entirely from choosing which chord tone, not from adding anything outside the harmony.

## The Microscope

Both panels play the identical two chords, Cmaj7 followed by Am7. Only whether the middle bar uses an inversion changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="ballad-inversion-lab">
  <div class="comparison-controls" aria-label="Ballad and Inversion comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Inversion</button>
    <button type="button" data-version="B" aria-pressed="false">B — Root position only</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="ballad-inversion-descending">
      <p class="abc-caption"><strong>A — A sparse descending line.</strong> Cmaj7's own seventh, in the bass, steps the line down before Am7 even arrives.</p>
      <p class="abc-description">Cmaj7 in root position, then the same Cmaj7 with its seventh in the bass, then Am7 in root position — a continuous C-B-A descent.</p>
      <pre class="abc-source">X:1
T:Ballad and Inversion — a sparse descending line
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=66
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | [ceg]8 | "Am7"[ace]8 |]
[V:LH] "^root"C,,8 | "^inversion"B,,8 | "^root"A,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="ballad-inversion-root-only">
      <p class="abc-caption"><strong>B — Root position only.</strong> The same two chords, but the repeated Cmaj7 restates its root instead of stepping down.</p>
      <p class="abc-description">Cmaj7 in root position, restated in root position, then Am7 in root position — no downward motion at all until the chord itself changes.</p>
      <pre class="abc-source">X:1
T:Ballad and Inversion — root position only
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=66
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | [ceg]8 | "Am7"[ace]8 |]
[V:LH] C,,8 | "^static"C,,8 | A,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A: the bass eases downward, C to B to A, even though the second bar's chord hasn't changed from the first. Play **Full** on B: the same two chords, but the bass sits still for two full bars before it has anywhere to go, and the eventual move to A arrives with no preparation.

## See

Both panels' right hand is identical — the harmony never differs. The entire difference is bar two's left hand: `B,,` in A, the seventh of the still-sounding Cmaj7, tagged `"^inversion"`; `C,,` in B, the same root restated, tagged `"^static"`. Neither note is wrong. Only one of them moves the line somewhere.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="ballad-inversion-two-chords">
  <p class="abc-caption"><strong>Step Down Through an Inversion.</strong> Practice restating one chord in an inversion to continue a descending line.</p>
  <p class="abc-description">Am7 in root position, then the same Am7 with its seventh in the bass.</p>
  <pre class="abc-source">X:1
T:Step Down Through an Inversion
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=66
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | [ace]8 |]
[V:LH] "^root"A,,8 | "^inversion"G,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play both bars slowly and listen for how little has to happen — one note, one chord tone away from the root — to create the sensation of the line going somewhere. Then play the second bar as a repeated root instead, and compare how much of the ballad's forward pull disappears with it.

## Vary

Take "Step Down Through an Inversion" and, instead of using the seventh, use the fifth of Am7 (E) in the bass for the second bar. Does the line still read as descending toward something, or does using a chord tone that isn't adjacent to the root change the character of the motion? Which inversions of a chord create the smoothest bass motion, and which create a more angular one?

## The Music

"Slow Descent" is an eight-bar ballad in B natural minor that traces a continuous B-A-G-F#-E-D line purely through inversions of Bm7, Gmaj7, and Em7 — no note outside any chord's own tones — before a dominant F#7-Bm7 cadence resolves the line home.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="slow-descent-study">
  <p class="abc-caption"><strong>Slow Descent.</strong> Five bars of inversion-driven descent resolve into a plain ii-V-I cadence.</p>
  <p class="abc-description">An eight-bar ballad in B natural minor using inversions of Bm7, Gmaj7, and Em7 to trace a falling bass line before a closing F#7 cadence.</p>
  <pre class="abc-source">X:1
T:Slow Descent
C:Alessandro Bessi
R:Ballad
M:4/4
L:1/8
Q:1/4=64
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Bm7"[d^fb]8 | [d^fb]8 | "Gmaj7"[dgb]8 | [dgb]8 |
"Em7"[egb]8 | [egb]8 | "F#7"[^c^f^a]8 | "Bm7"[d^fb]8 |]
[V:LH] "^root"B,,8 | "^inversion"A,,8 | "^root"G,,8 | "^inversion"^F,,8 |
"^root"E,,8 | "^inversion"D,,8 | "^root"^F,,8 | "^resolve"B,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Every note in "Slow Descent" belongs to the chord sounding above it at that instant — nothing is borrowed the way a Passing Motion or Approach Note would borrow a note from outside the harmony. If a listener heard only the bass line's shape, without the chords, would they be able to tell it apart from a line built with genuine passing tones? What does your answer say about how much of "direction" in a bass line comes from the notes themselves versus from the harmony underneath them?
