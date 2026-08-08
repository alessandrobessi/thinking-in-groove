# Subdivision

*Chapter 18 — Part III, Groove: How Is Motion Organized in Time?*

## The Question

Before you can say a note is early or late, what has to be agreed on first?

## The Mental Model

**Subdivision** is the shared temporal grid — eighths, sixteenths, triplets — that makes rhythmic locations countable at all. It comes before every other Groove concept in this Part, because "the note lands on the and of beat 2" only means something once both the writer and the reader have agreed on what grid "and" refers to.

Subdivision is not the same question as Attack Placement (Chapter 19). Subdivision defines the ruler; Attack Placement is where a specific note falls once that ruler exists. A finer subdivision doesn't change where a note *sounds* — it changes how precisely the page can *say* where it sounds.

## The Microscope

The bass lands at what's conversationally called "just after beat 1" both times. Only the grid used to say exactly where changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="subdivision-lab">
  <div class="comparison-controls" aria-label="Subdivision comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Eighth-note grid</button>
    <button type="button" data-version="B" aria-pressed="false">B — Sixteenth-note grid</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="subdivision-eighth-grid">
      <p class="abc-caption"><strong>A — An eighth-note grid.</strong> The finest position this grid can name is "the and of beat 1."</p>
      <p class="abc-description">One bar at L:1/8: a chord arriving on the and of beat 1.</p>
      <pre class="abc-source">X:1
T:Subdivision — an eighth-note grid
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 |]
[V:LH] z1 "^and of beat 1"C,7 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="subdivision-sixteenth-grid">
      <p class="abc-caption"><strong>B — A sixteenth-note grid.</strong> The same bar can now name a position the eighth-note grid has no name for at all.</p>
      <p class="abc-description">One bar at L:1/16: a chord arriving on the "e" of beat 1, a sixteenth earlier than A's arrival.</p>
      <pre class="abc-source">X:1
T:Subdivision — a sixteenth-note grid
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/16
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]16 |]
[V:LH] z1 "^e of beat 1 -- no eighth-grid equivalent"C,15 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A's arrival sits on a position an eighth-note grid can name precisely: the and of beat 1. B's arrival is earlier still — a position that only exists once the beat is divided into four, not two.

## See

Look at the `L:` field in each source: `1/8` versus `1/16`. That single field changes what every duration number in the rest of the tune means, and it's the reason the exact same conversational description — "right after beat 1" — needed a finer grid in B to actually pin down.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="subdivision-find-the-grid">
  <p class="abc-caption"><strong>Find the Grid.</strong> Two bars at sixteenth-note resolution, naming three distinct positions.</p>
  <p class="abc-description">Two bars: the and of beat 2, the e of beat 1, and the and of beat 3.</p>
  <pre class="abc-source">X:1
T:Find the Grid
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/16
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]16 | "Cmaj7"[CEGB]16 |]
[V:LH] z6 "^and of beat 2"C,10 | z1 "^e of beat 1"C,3 z6 "^and of beat 3"C,6 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Before playing, count each bar out loud using the full sixteenth-note syllables: "1 e and a, 2 e and a, 3 e and a, 4 e and a." Land on each annotated note exactly on its named syllable.

## Vary

Rewrite the second bar's "e of beat 1" arrival using only an eighth-note grid (`L:1/8`). Can you name a position close to it, or does the eighth-note grid genuinely have no way to say what you just played?

## The Music

"Fine Grid" is an original eight-bar funk study in Db major, written entirely on a sixteenth-note grid, even though most of its attacks still fall on positions an eighth-note grid could also name.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="fine-grid-study">
  <p class="abc-caption"><strong>Fine Grid.</strong> A sixteenth-note grid used for precision, not necessarily for busier rhythm.</p>
  <p class="abc-description">An eight-bar funk study in Db major at L:1/16 moving through Dbmaj7, Bbm7, Ebm7, and Ab7.</p>
  <pre class="abc-source">X:1
T:Fine Grid
C:Alessandro Bessi
R:Funk study
M:4/4
L:1/16
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dbmaj7"z4 [_DF_Ac]4 z4 [_DF_Ac]4 | "Dbmaj7"z4 [_DF_Ac]4 z4 [_DF_Ac]4 | "Bbm7"z4 [_DF_A_B]4 z4 [_DF_A_B]4 | "Bbm7"z4 [_DF_A_B]4 z4 [_DF_A_B]4 |
"Ebm7"z4 [_D_E_G_B]4 z4 [_D_E_G_B]4 | "Ebm7"z4 [_D_E_G_B]4 z4 [_D_E_G_B]4 | "Ab7"z4 [_E_G_Ac]4 z4 [_E_G_Ac]4 | "Ab7"z4 [_E_G_Ac]4 z4 [_E_G_Ac]4 |]
[V:LH] "^grid"_D,4 z2 _D,2 z4 _D,4 | "^grid"_D,4 z2 _D,2 z4 _D,4 | "^grid"_B,4 z2 _B,2 z4 _B,4 | "^grid"_B,4 z2 _B,2 z4 _B,4 |
"^grid"_E,4 z2 _E,2 z4 _E,4 | "^grid"_E,4 z2 _E,2 z4 _E,4 | "^grid"_A,4 z2 _A,2 z4 _A,4 | "^grid"_A,4 z2 _A,2 z4 _A,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Every attack in "Fine Grid" actually falls on a position an eighth-note grid could have named too. Why write it at sixteenth-note resolution at all — what does the finer grid make possible for the chapters still to come in this Part?
