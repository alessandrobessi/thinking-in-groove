# Repeated Cells

*Chapter 24 — Part III, Groove: How Is Motion Organized in Time?*

## The Question

What makes a groove recognizable as itself, bar after bar?

## The Mental Model

A **Repeated Cell** is a short pattern of recurring attacks, rests, and durations — the rhythmic shape that establishes a groove's identity, sometimes called its "riff atom." The word to hold onto is *rhythmic*: a cell is defined by its pattern of attacks and rests recurring, not by any particular pitch recurring.

That distinction matters because a repeated pitch played with a different rhythm every time isn't a cell at all — it's just a note that keeps coming back. A Repeated Cell survives a change of chord, a change of register, even a change of every pitch involved, as long as the underlying attack-rest-attack-attack pattern stays intact.

Defining a cell by rhythm rather than pitch isn't an arbitrary choice — it's the only definition that lets a groove survive the harmony actually moving. Pitch identity is tied to chord function: the root that makes a cell "itself" under Cm7 is a different note entirely under Abmaj7. If a cell's identity depended on repeating the same pitches, it could only ever exist over a single unchanging chord, which would make "one groove across four different chords" a contradiction rather than the achievement "Riff Atom" demonstrates. Rhythm is the one property that genuinely can stay constant while everything else in the harmony changes underneath it, which is exactly why it's the property this chapter chooses to define identity by. The next chapter asks the natural follow-up question: once a cell is established this firmly, how much of it can actually change before a listener stops recognizing it as the same cell at all?

## The Microscope

The bass plays the same pitch, C, both times. Only whether the rhythm around it repeats changes whether it's a cell.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="repeated-cells-lab">
  <div class="comparison-controls" aria-label="Repeated Cells comparison">
    <button type="button" data-version="A" aria-pressed="true">A — A genuine cell</button>
    <button type="button" data-version="B" aria-pressed="false">B — Not a cell</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="repeated-cells-genuine">
      <p class="abc-caption"><strong>A — A genuine cell.</strong> The identical attack-rest-attack-attack rhythm repeats exactly.</p>
      <p class="abc-description">Two bars, same pitch and same rhythm both times.</p>
      <pre class="abc-source">X:1
T:Repeated Cells — a genuine cell
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^cell"C,2 z2 C,2 C,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="repeated-cells-not-a-cell">
      <p class="abc-caption"><strong>B — Same pitch, not a cell.</strong> The rhythm changes completely in bar 2 even though the pitch doesn't.</p>
      <p class="abc-description">Two bars, same pitch throughout, but the second bar's rhythm is unrelated to the first.</p>
      <pre class="abc-source">X:1
T:Repeated Cells — same pitch, not a cell
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^same pitch"C,2 z2 C,2 C,2 | "^different rhythm -- not a cell"C,4 z2 C,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A repeats a recognizable groove — you could tap along with bar 2 before it happens, because it's identical to bar 1. B gives you nothing to predict: knowing bar 1's rhythm tells you nothing about bar 2's, even though the pitch never moved.

## See

Look at the rhythm values alone, ignoring pitch entirely: A's two bars are visually identical shapes. B's two bars share a notehead but not a rhythm. That's the test for a Repeated Cell on the page — cover the noteheads and check whether the durations and rests still match.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="repeated-cells-carry-the-rhythm">
  <p class="abc-caption"><strong>Carry the Rhythm.</strong> One cell, applied to four different chord roots.</p>
  <p class="abc-description">Four bars, identical attack-rest-attack-attack rhythm, a new root each bar.</p>
  <pre class="abc-source">X:1
T:Carry the Rhythm
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^cell"A,2 z2 A,2 A,2 | "^cell"D,2 z2 D,2 D,2 | "^cell"G,2 z2 G,2 G,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play all four bars and notice that your hand does the same physical rhythm each time, even though it lands on a different key. That physical repetition, independent of pitch, is what a Repeated Cell actually is.

## Vary

Keep the rhythm identical across all four bars, but replace each root with its fifth instead. Does the exercise still feel like "the same cell," or does changing every pitch make it feel like a different groove even though the rhythm never moved?

## The Music

"Riff Atom" is an original eight-bar funk study in C natural minor, built from one repeated cell, carried through four different chords without ever changing its rhythm.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="riff-atom-study">
  <p class="abc-caption"><strong>Riff Atom.</strong> The same rhythmic cell, unchanged, under every chord of the phrase.</p>
  <p class="abc-description">An eight-bar funk study in C natural minor: one attack-rest-attack-attack cell tracking Cm7, Abmaj7, Bb7, and Fm7.</p>
  <pre class="abc-source">X:1
T:Riff Atom
C:Alessandro Bessi
R:Funk study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cm7"[c_eg_b]8 | "Cm7"[c_eg_b]8 | "Abmaj7"[_ac'_e'g']8 | "Abmaj7"[_ac'_e'g']8 |
"Bb7"[_bd'f'_a']8 | "Bb7"[_bd'f'_a']8 | "Fm7"[f_ac'_e']8 | "Fm7"[f_ac'_e']8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^cell"C,2 z2 C,2 C,2 | "^cell"_A,2 z2 _A,2 _A,2 | "^cell"_A,2 z2 _A,2 _A,2 |
"^cell"_B,2 z2 _B,2 _B,2 | "^cell"_B,2 z2 _B,2 _B,2 | "^cell"F,2 z2 F,2 F,2 | "^cell"F,2 z2 F,2 F,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"Riff Atom" never varies its cell once in eight bars. What does that unbroken repetition buy the groove, and at what point (if you kept extending the piece) would you expect a listener to want it to change?
