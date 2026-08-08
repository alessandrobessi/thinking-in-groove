# Anticipation

*Chapter 23 — Part III, Groove: How Is Motion Organized in Time?*

## The Question

What changes when the bass announces the next harmony before that harmony formally begins?

## The Mental Model

An **anticipation** is an attack that presents an upcoming structural note before its formal chord or bar boundary. The note belongs to the destination, but it first sounds while the previous harmony is still active.

Anticipation is more specific than syncopation. Both may use a weak-position attack, but an anticipation points to a known future event—often the next root—and continues or resolves into that event. It is also not a microtiming “push”: an eighth-note anticipation occupies a written subdivision that every player can count.

## The Microscope

Both versions keep Cmaj7–Am7–Dm7–G7, the right hand, bass roots, sounded durations, register, and tempo fixed. A attacks each root on its chord’s downbeat. B attacks A, D, and G on the “and” of beat 4 in the preceding bar and ties each across the chord boundary.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="anticipation-lab">
  <div class="comparison-controls" aria-label="Downbeat and anticipated root comparison">
    <button type="button" data-version="A" aria-pressed="true">A — At the boundary</button>
    <button type="button" data-version="B" aria-pressed="false">B — Before the boundary</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="anticipation-boundary">
      <p class="abc-caption"><strong>A — At the boundary.</strong> Every root begins with its chord.</p>
      <p class="abc-description">Four functional chords with short root attacks on each downbeat.</p>
      <pre class="abc-source">X:1
T:Anticipation — at the boundary
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^with chord"C,2 z6 | A,,2 z6 | D,2 z6 | G,,2 z6 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="anticipation-before-boundary">
      <p class="abc-caption"><strong>B — Before the boundary.</strong> Each upcoming root begins one eighth early.</p>
      <p class="abc-description">The harmony still changes on downbeats; the bass anticipates A, D, and G from the previous bars.</p>
      <pre class="abc-source">X:1
T:Anticipation — before the boundary
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^present"C,2 z4 z1 "^anticipate A"A,,1- | A,,1 z6 "^anticipate D"D,1- | D,1 z6 "^anticipate G"G,,1- | G,,1 z4 z2 z1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Use **Harmony only** to locate each formal chord change. With **Bass only**, hear the roots lean across the bar lines. In **Full**, the brief overlap with the old harmony should sound directional because each early note becomes the next chord’s root.

## See

The chord symbols remain at the beginnings of bars. In B, each tied bass note has only one attack: before the bar line. Its continuation after the bar line is not played again.

## Play

Begin with every root on the downbeat, then anticipate one destination at a time.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="anticipation-exercise">
  <p class="abc-caption"><strong>Lean Into Tomorrow.</strong> Three boundaries, three controlled anticipations.</p>
  <p class="abc-description">A four-bar functional exercise moving each upcoming root to the final eighth of the prior bar.</p>
  <pre class="abc-source">X:1
T:Lean Into Tomorrow
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
[V:LH] C,2 G,2 E,2 z1 "^next root"A,,1- | A,,1 E,2 C,2 z2 "^next root"D,1- | D,1 A,2 F,2 z2 "^next root"G,,1- | G,,1 D,2 B,,2 z3 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Keep the anticipation on the “and” of 4 but replace the upcoming root with another chord tone. Does it still announce the destination as clearly, or does it become a general approach note?

## The Music

“Early Light” is an original eight-bar jazz study in Gb major. Each bar develops a compact chord-tone idea, then the next root enters on the final eighth and ties across the boundary. The second four bars vary the internal line while preserving that anticipatory phrase rhythm.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="early-light-study">
  <p class="abc-caption"><strong>Early Light.</strong> Every destination is heard just before it officially arrives.</p>
  <p class="abc-description">An eight-bar functional-jazz miniature with sustained piano harmony and tied root anticipations.</p>
  <pre class="abc-source">X:1
T:Early Light
C:Alessandro Bessi
R:Jazz study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gbmaj7"[_B_df_g]8 | "Ebm7"[_G_B_d_e]8 | "Abm7"[_G_AB_e]8 | "Db7"[_AB_df]8 | "Gbmaj7"[_B_df_g]8 | "Ebm7"[_G_B_d_e]8 | "Abm7"[_G_AB_e]8 | "Db7"[_AB_df]8 |]
[V:LH] "^anticipatory phrase"_G,2 _D2 _B,2 z1 _E,1- | _E,1 _B,2 _G,2 z2 _A,1- | _A,1 _E2 B,2 z2 _D,1- | _D,1 _A,2 B,2 z2 _G,1- | _G,1 _B,2 F,2 z2 _E,1- | _E,1 _G,2 _D2 z2 _A,1- | _A,1 B,2 _G,2 z2 _D,1- | _D,1 F,2 _A,2 z2 "^points beyond the excerpt"_G,1 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

When does the early root in “Early Light” feel like tension against the old chord, and when does it make the new chord feel as though it has already begun?
