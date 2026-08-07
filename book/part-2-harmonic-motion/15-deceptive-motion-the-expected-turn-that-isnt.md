# Arpeggiating

*Chapter 13 — Part II, Motion: How Does the Bass Travel?*

## The Question

What turns a series of leaps into something that sounds intentional rather than random?

## The Mental Model

**Arpeggiating** means outlining two or more tones of the *current* chord in a directed melodic sequence — the bass tracing the harmony's own structure rather than borrowing a shape from outside it.

A single leap isn't yet an arpeggio. Leaping (Chapter 14) covers the general device of a large interval used for emphasis, whether or not it lands on a chord tone or continues anywhere afterward. The moment a leap keeps going — continuing on to state a second and third chord tone in sequence — it becomes something more specific: an Arpeggiating gesture that outlines the chord itself.

## The Microscope

Both versions start with the same leap from C. Only whether it continues changes what the gesture is.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="arpeggiating-lab">
  <div class="comparison-controls" aria-label="Arpeggiating comparison">
    <button type="button" data-version="A" aria-pressed="true">A — A single leap</button>
    <button type="button" data-version="B" aria-pressed="false">B — Becomes an arpeggio</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="arpeggiating-single-leap">
      <p class="abc-caption"><strong>A — A single leap.</strong> C jumps to A, a color tone, and stops.</p>
      <p class="abc-description">One bar: a root leaping up a sixth to the 13th, with nothing following it.</p>
      <pre class="abc-source">X:1
T:Arpeggiating — a single leap
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 |]
[V:LH] "^leap"C,4 A,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="arpeggiating-continued">
      <p class="abc-caption"><strong>B — The same opening leap, continued.</strong> C, E, G, B trace the chord's own structure.</p>
      <p class="abc-description">The same bar, now outlining root, third, fifth, and seventh in sequence.</p>
      <pre class="abc-source">X:1
T:Arpeggiating — the same leap, continued
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 |]
[V:LH] "^arpeggio"C,2 E,2 G,2 B,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A's leap to A is a single, isolated color choice — it doesn't explain itself any further. B's continuation makes the harmonic logic audible: every note names a specific chord tone, in order, so the ear can follow the chord's own shape rather than just registering one jump.

## See

B's four notes — C, E, G, B — are exactly Cmaj7's stacked thirds, read straight off the chord symbol above. That's the visual test for Arpeggiating: can you name each bass note as a specific numbered chord tone in sequence? If the notes don't map onto the current chord's own structure, the line is doing something else — Stepping, Leaping, or Connecting Chords instead.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="arpeggiating-outline-the-chord">
  <p class="abc-caption"><strong>Outline the Chord.</strong> A full ascending arpeggio under each of four different chords.</p>
  <p class="abc-description">Four bars, each bass line tracing its own chord's root, third, fifth, and seventh.</p>
  <pre class="abc-source">X:1
T:Outline the Chord
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^arpeggio"C,2 E,2 G,2 B,2 | "^arpeggio"A,2 C2 E2 G2 | "^arpeggio"D,2 F,2 A,2 C2 | "^arpeggio"G,2 B,2 D2 F2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Before playing each bar, say the four chord-tone numbers out loud — "root, third, fifth, seventh" — then play them. If you can't name a note's number without stopping, you're not yet arpeggiating that chord; you're guessing at a shape.

## Vary

Play the same four arpeggios in a different order (root, fifth, third, seventh, for instance) instead of strict ascending thirds. Does the line still read as an outline of the chord, or does breaking the ascending order make it start to sound like something else?

## The Music

"Full Outline" is an original eight-bar jazz study built entirely from ascending and descending arpeggios, one full outline per chord.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="full-outline-study">
  <p class="abc-caption"><strong>Full Outline.</strong> Every bar traces its chord fully, alternating ascending and descending direction.</p>
  <p class="abc-description">An eight-bar jazz study outlining Cmaj7, Am7, Dm7, and G7 in turn.</p>
  <pre class="abc-source">X:1
T:Full Outline
C:Alessandro Bessi
R:Jazz study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 | "Am7"[ACEG]8 | "Am7"[ACEG]8 |
"Dm7"[DFAC]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 | "G7"[DFGB]8 |]
[V:LH] "^arpeggio"C,2 E,2 G,2 B,2 | "^arpeggio"C2 B,2 G,2 E,2 | "^arpeggio"A,2 C2 E2 G2 | "^arpeggio"G2 E2 C2 A,2 |
"^arpeggio"D,2 F,2 A,2 C2 | "^arpeggio"C2 A,2 F,2 D,2 | "^arpeggio"G,2 B,2 D2 F2 | "^arpeggio: settle"G,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"Full Outline" never leaves its current chord to arpeggiate — every note in a given bar belongs to that bar's own harmony. What would change about the piece's character if one bar's arpeggio borrowed a tone from the *next* chord instead?
