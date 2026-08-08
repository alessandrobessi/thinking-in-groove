# Approaching

*Chapter 11 — Part II, Motion: How Does the Bass Travel?*

## The Question

Why can the note before a chord change make the destination sound inevitable?

## The Mental Model

An **approach** is a note heard in relation to the target that follows it. Its meaning is directional: it points toward an arrival.

The approach may come from a chord tone, a diatonic step, a whole step, or a chromatic half step. What matters is not that the note is “outside,” but that its placement and resolution make the target clear. A chromatic note that never resolves is colour or tension; it becomes an approach only when the next event completes its motion.

## The Microscope

Both versions use the same G7–Cmaj7 harmony, right-hand voicings, rhythm, tempo, register, target, and phrase length. Only the final bass note before C changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="approaching-lab">
  <div class="comparison-controls" aria-label="Direct and chromatic approach comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Chord-tone route</button>
    <button type="button" data-version="B" aria-pressed="false">B — Half-step approach</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="approaching-direct">
      <p class="abc-caption"><strong>A — Chord-tone route.</strong> D moves to C without a semitone pull.</p>
      <p class="abc-description">G7 resolves to C major; the bass moves G–D–C.</p>
      <pre class="abc-source">X:1
T:Approaching — chord-tone route
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "G7"[DFGB]8 | "Cmaj7"[EGBc]8 |]
[V:LH] G,6 "^from the fifth"D2 | "^target"C,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="approaching-chromatic">
      <p class="abc-caption"><strong>B — Half-step approach.</strong> B sits directly below C and intensifies the arrival.</p>
      <p class="abc-description">The identical G7–C-major harmony sounds while the bass moves G–B–C.</p>
      <pre class="abc-source">X:1
T:Approaching — half step
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "G7"[DFGB]8 | "Cmaj7"[EGBc]8 |]
[V:LH] G,6 "^half-step approach"B,2 | "^target"C,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Use **Harmony only** to confirm that the context is identical. Use **Bass only** to isolate D–C from B–C. Then use **Full** and listen to how B belongs to G7 while simultaneously leaning into the next root.

## See

The annotation belongs on B, not C. C is the target; B is the event whose job is to approach it. Written notation shows a metrically placed half step. It does not claim that B is pushed ahead of the beat or that C is laid back.

## Play

Each bar begins on a harmonic destination. Beat 4 supplies the chromatic lower neighbour of the next root.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="approaching-exercise">
  <p class="abc-caption"><strong>Four arrivals.</strong> Preserve the target notes and change only their approaches.</p>
  <p class="abc-description">A four-bar major-key progression whose bass approaches A, D, G, and the returning C by half step.</p>
  <pre class="abc-source">X:1
T:Four Arrivals
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^target"C,6 "^approach"^G,,2 | "^target"A,,6 "^approach"^C,2 | "^target"D,6 "^approach"^F,,2 | "^target"G,,6 "^approach"B,,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

The final B points beyond the printed exercise to C. Repeat the four bars mentally once more so the last approach has a destination.

## Vary

Keep every target, attack, and duration. Replace each chromatic lower approach with a diatonic note from above. Compare the strength and character of the four arrivals.

## The Music

“Corner Lights” is an original eight-bar jazz study in G major, over two passes of Gmaj7–Em7–Am7–D7. Structural roots land on beat 1; beat 4 prepares the next destination with a chromatic approach.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="corner-lights-study">
  <p class="abc-caption"><strong>Corner Lights.</strong> The harmony repeats while the bass varies the route into each root.</p>
  <p class="abc-description">An eight-bar functional-jazz study in G major with compact right-hand voicings and a monophonic walking bass approaching each root chromatically.</p>
  <pre class="abc-source">X:1
T:Corner Lights
C:Alessandro Bessi
R:Jazz study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gmaj7"[Bd^fg]8 | "Em7"[GBde]8 | "Am7"[GAce]8 | "D7"[Acd^f]8 |
"Gmaj7"[Bd^fg]8 | "Em7"[GBde]8 | "Am7"[GAce]8 | "D7"[Acd^f]6 "Gmaj7"[Bd^fg]2 |]
[V:LH] "^target"G,2 B,2 D2 "^approach"^D,2 | "^target"E,2 G,2 B,2 "^approach"^G,2 | "^target"A,2 C2 E2 "^approach"^C,2 | "^target"D,2 ^F,2 A,2 "^approach"^F,2 |
"^target"G,2 D2 B,2 "^approach"^D,2 | "^target"E,2 B,2 G,2 "^approach"^G,2 | "^target"A,2 E,2 C2 "^approach"^C,2 | "^target"D,2 A,2 "^approach"^F,2 "^arrival"G,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Which approach in “Corner Lights” sounds strongest because of its pitch, and which sounds strongest because of where the phrase places it?
