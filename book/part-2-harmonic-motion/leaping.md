# Leaping

*Chapter 14 — Part II, Motion: How Does the Bass Travel?*

## The Question

Why does a big leap in a bass line seem to demand something afterward, and what happens if it doesn't get it?

## The Mental Model

**Leaping** is motion by a large interval, used deliberately for emphasis. Unlike Arpeggiating (Chapter 13), a leap doesn't have to land on a chord tone or continue outlining the harmony — a leap to a color tone, or an octave displacement, is still Leaping even with nothing following it. What Leaping does require is an honest reckoning with what comes next: a leap creates a registral gap, and that gap asks to be recovered, usually by stepping back toward where the line came from.

A leap that isn't followed by any recovery — another leap somewhere unrelated, with no settling — tends to read as disjointed rather than emphatic. The emphasis only lands cleanly when the ear can hear the leap *and* its resolution as one gesture.

Why does a step work as recovery when another leap doesn't? Chapter 10 established that adjacent motion asks the least possible recalibration of anywhere a line could go next; a leap spends a large amount of registral "energy" all at once, and a step is the cheapest, most legible way to spend the rest of it back down to a stable footing. A second leap doesn't resolve anything — it just opens a new gap before the first one closed, which is exactly why Panel A reads as unsettled rather than doubly emphatic. The common error is assuming that *any* motion after a leap counts as a recovery; the Vary exercise below tests this directly by continuing in the same direction instead of stepping back, which is worth predicting before you try it.

## The Microscope

Both versions leap the same distance, from the same note. Only what happens immediately afterward changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="leaping-lab">
  <div class="comparison-controls" aria-label="Leaping comparison">
    <button type="button" data-version="A" aria-pressed="true">A — No recovery</button>
    <button type="button" data-version="B" aria-pressed="false">B — With recovery</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="leaping-without-recovery">
      <p class="abc-caption"><strong>A — Leaping without recovery.</strong> A second, unrelated leap follows instead of a settle.</p>
      <p class="abc-description">A root leaps up a sixth, then leaps again to an unrelated note.</p>
      <pre class="abc-source">X:1
T:Leaping — without recovery
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
[V:LH] "^leap"C,4 A,2 D2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="leaping-with-recovery">
      <p class="abc-caption"><strong>B — Leaping with recovery.</strong> The same leap, followed by a step back down.</p>
      <p class="abc-description">The identical opening leap, this time settling by step.</p>
      <pre class="abc-source">X:1
T:Leaping — with recovery
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
[V:LH] "^leap"C,4 A,2 G,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A's second leap keeps the line unsettled — the ear never gets confirmation that the first leap meant anything in particular. B's step back down closes the gesture: leap, then land nearby, exactly like a held breath being released.

## See

In B, the final note (G) is directly adjacent to the leap's landing note (A) — a visible step, immediately after a visible leap. In A, the second interval is itself another leap of similar size. The notation makes the contrast obvious: one gesture closes with a step, the other keeps opening with more leaps.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="leaping-reach-and-settle">
  <p class="abc-caption"><strong>Reach and Settle.</strong> Four leaps, each recovered by a step in the opposite direction.</p>
  <p class="abc-description">Four bars, each a root leaping up roughly a sixth before stepping back down.</p>
  <pre class="abc-source">X:1
T:Reach and Settle
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
[V:LH] "^leap"C,4 A,2 G,2 | "^leap"A,4 F2 E2 | "^leap"D,4 B,2 A,2 | "^leap"G,4 E2 D2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play the leap boldly and the recovery quietly — the dynamic contrast itself helps the ear hear the gesture as one shape rather than two unrelated events.

## Vary

Replace each bar's step-down recovery with a step *up* instead (in the same direction as the leap). Does the gesture still feel resolved, or does continuing in the same direction start to feel like the beginning of a second leap rather than a recovery?

## The Music

"Reach and Return" is an original eight-bar fusion study in A major, in 7/8, alternating leaps with held recoveries across four chords.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="reach-and-return-study">
  <p class="abc-caption"><strong>Reach and Return.</strong> Each leap is followed by a settled, held recovery before the next chord.</p>
  <p class="abc-description">An eight-bar fusion study in A major, in 7/8: four leap-and-settle gestures across Amaj7, F#m7, Bm7, and E7.</p>
  <pre class="abc-source">X:1
T:Reach and Return
C:Alessandro Bessi
R:Fusion study
M:7/8
L:1/8
Q:1/8=192
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Amaj7"[A^ce^g]7 | "Amaj7"[A^ce^g]7 | "F#m7"[A^ce^f]7 | "F#m7"[A^ce^f]7 |
"Bm7"[ABd^f]7 | "Bm7"[ABd^f]7 | "E7"[Bde^g]7 | "E7"[Bde^g]7 |]
[V:LH] "^leap"A,3 ^F2 E2 | "^stay"E4 z3 | "^leap"^F3 d2 ^c2 | "^stay"^c2 z1 B2 z2 |
"^leap"B,3 ^G2 ^F2 | "^stay"^F4 z3 | "^leap"E3 ^c2 B2 | "^settle"E7 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Every leap in "Reach and Return" is followed immediately by a settle, then held stillness (Staying, Chapter 9) before the next leap. What would the piece lose if the recoveries were removed and the leaps simply followed one another directly?
