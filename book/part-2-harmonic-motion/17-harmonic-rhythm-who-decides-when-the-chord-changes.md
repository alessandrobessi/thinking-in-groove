# Harmonic Rhythm

*Chapter 34 — Part IV, Interaction: What Happens Between Bass and Harmony? Closing chapter: the rate at which the upper harmony changes chords constrains which bass strategies from every earlier Part are viable.*

## The Question

Does a bass line's own note-attack rate tell you anything about how fast the harmony underneath it is actually changing?

## The Mental Model

**Harmonic Rhythm** is the rate at which the upper harmony changes chords — and it constrains which bass strategies from every earlier Part are actually viable at a given moment. A slow harmonic rhythm, one chord held for many bars, invites Staying or a Pedal: there's nothing new to connect to, so the bass can simply live inside the one harmony. A fast harmonic rhythm, a new chord every two beats, invites Connecting Chords or Arpeggiating: the bass has somewhere new to arrive at, often enough that its whole job becomes steering from one arrival to the next.

This is a different axis from Density Balance, and the two are easy to collapse into each other. Density Balance asks how many notes the bass plays. Harmonic Rhythm asks how often the chord itself changes. A dense, busy bass line can sit under a very slow harmonic rhythm — running eighth notes decorating a single held chord for four bars — and a sparse, minimal bass line can sit under a fast one. The common error is hearing "the harmony is moving quickly" and "the bass is playing a lot of notes" as the same observation; they are independent variables, and this chapter's whole purpose is separating them before Part V asks you to choose both deliberately for a real piece.

## The Microscope

Both panels use the identical bass line, note for note. Only the rate of chord change above it changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="harmonic-rhythm-lab">
  <div class="comparison-controls" aria-label="Harmonic Rhythm comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Slow</button>
    <button type="button" data-version="B" aria-pressed="false">B — Fast</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="harmonic-rhythm-slow">
      <p class="abc-caption"><strong>A — Slow, under a busy bass.</strong> One chord held across two full bars while the bass runs continuously beneath it.</p>
      <p class="abc-description">A two-bar Cmaj7 chord held motionless under a running eighth-note bass line.</p>
      <pre class="abc-source">X:1
T:Harmonic Rhythm — slow, under a busy bass
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | [ceg]8 |]
[V:LH] "^dense"C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 | C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="harmonic-rhythm-fast">
      <p class="abc-caption"><strong>B — Fast, under the same busy bass.</strong> Four different chords across the same two bars, with the bass line completely unchanged.</p>
      <p class="abc-description">The identical running bass line, now under a chord changing every two beats instead of every two bars.</p>
      <pre class="abc-source">X:1
T:Harmonic Rhythm — fast, under the same busy bass
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]4 "Am7"[ace]4 | "Dm7"[dfa]4 "G7"[gbd]4 |]
[V:LH] "^dense"C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 | C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A: one harmony sits still for two full bars while the bass stays continuously active underneath it. Play **Full** on B: the harmony now changes four times in the same span, and the bass — attacking exactly as often as before — suddenly has to relate to a new chord every couple of beats instead of decorating one chord at length.

## See

The left-hand staff is identical in both panels, note for note: `C,, D,, E,, F,, G,, F,, E,, D,,`, repeated once. The right hand is the only thing that changes — one chord symbol across two bars in A, four chord symbols in the same span in B. The bass's own attack rate, visible in its rhythm, never moves; only the rate of the chord symbols above it does.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="harmonic-rhythm-match-the-rate">
  <p class="abc-caption"><strong>Match the Rate.</strong> Practice choosing a bass strategy that fits the harmonic rhythm it's placed under.</p>
  <p class="abc-description">A slow bar inviting a held pedal, followed by a fast bar inviting a stepwise connection between two chord roots.</p>
  <pre class="abc-source">X:1
T:Match the Rate
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]4 "Dm7"[dfa]4 |]
[V:LH] "^stay"C,,8 | "^connect"A,,2 B,,2 C,,2 D,,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play the first bar and let the bass simply live inside the one chord — resist adding motion it doesn't need yet. Then play the second bar and feel how the doubled chord-change rate turns the same amount of bass activity into a genuine journey between two roots, rather than decoration around one.

## Vary

Take "Match the Rate" and swap the strategies: hold a pedal under the fast bar, and walk a stepwise connection under the slow one. Does the pedal under two changing chords sound like a deliberate choice or a missed one? Does the stepwise motion under a single held chord sound purposeful, or does it sound like it's connecting to nothing?

## The Music

"Change of Pace" is an eight-bar jazz-funk study that spends four bars in a slow harmonic rhythm — one chord held across each pair of bars, the bass staying inside it — before doubling the rate for two bars of chord-per-half-bar motion, where the bass shifts to stepwise connections between roots, then returns to the slow rate to close.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="change-of-pace-study">
  <p class="abc-caption"><strong>Change of Pace.</strong> The bass strategy shifts exactly when the harmonic rhythm does, and not before.</p>
  <p class="abc-description">An eight-bar jazz-funk study moving from a slow, one-chord-per-two-bars harmonic rhythm into a fast, chord-per-half-bar passage and back.</p>
  <pre class="abc-source">X:1
T:Change of Pace
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | [ceg]8 | "Am7"[ace]8 | [ace]8 |
"Dm7"[dfa]4 "G7"[gbd]4 | "Cmaj7"[ceg]4 "Am7"[ace]4 | "G7"[gbd]8 | "Cmaj7"[ceg]8 |]
[V:LH] "^stay"C,,8 | C,,8 | "^stay"A,,8 | A,,8 |
"^connect"C,,2 D,,2 F,,2 G,,2 | "^connect"B,,2 C,,2 B,,2 A,,2 | "^stay"G,,8 | "^resolve"C,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
```

:::

## Reflection

Part IV opened by asking whether the bass reinforces, ignores, or answers the upper voice moment to moment. Harmonic Rhythm closes it by asking a slower-moving version of the same question: once you know how often the chord itself is going to change, which of this Part's — and every earlier Part's — strategies are even available to choose from? Which of your own habits do you reach for by default, regardless of whether the harmonic rhythm around you actually supports it?
