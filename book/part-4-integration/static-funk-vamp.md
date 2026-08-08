# Static Funk Vamp

*Chapter 36 — Part V, Design: Building Complete Bass Lines. Repetition, space, and controlled mutation sustain static harmony.*

## The Question

If the harmony doesn't change for eight bars, what actually keeps a bass line from going stale?

## The Mental Model

A **Static Funk Vamp** is the genre case where Harmonic Rhythm is about as slow as it gets: one chord, held for a long stretch, with no new harmonic destination to travel toward. That removes an entire category of design decision — there's nothing to connect to, so Motion in the sense of Stepping, Approaching, or Connecting Chords mostly falls away. What's left to carry the line is Groove: a Repeated Cell establishes the vamp's identity, Space keeps the cell from feeling mechanical, and a series of controlled mutations — Variation Without Collapse — keeps a listener's attention across repetitions that would otherwise sound identical.

This is the Design Algorithm from the previous chapter applied to a specific, common situation, and it reveals something the algorithm doesn't say outright: which of its five layers actually matters is different depending on the harmony you're given. Over static harmony, Role and Motion do very little work; Groove does almost all of it. A static vamp built from a cell that never changes at all reads as dead, no matter how funky the cell is on its first playing. The same cell, repeated with a deliberate substitution partway through and a bar of silence before its final return, reads as alive — using the identical harmonic material throughout.

Role and Motion both depend on there being more than one harmonic destination to choose between — a Role is a job relative to *this* chord, a Motion is a route toward the *next* one. With only one chord in play for eight bars, both collapse to essentially the same trivial answer every time, which is exactly why they stop being useful design levers here. Groove inherits the entire remaining design space by default, not by any special virtue of its own. The next chapter studies the mirror-image situation, where the harmony moves so often that Motion and Role reclaim most of that space and Groove becomes comparatively uniform instead.

## The Microscope

Both panels sit over the same held Am7, for the same four bars, with the same rhythmic cell. Only whether that cell ever changes differs.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="static-vamp-lab">
  <div class="comparison-controls" aria-label="Static Funk Vamp comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Controlled mutation</button>
    <button type="button" data-version="B" aria-pressed="false">B — Dead repetition</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="static-vamp-controlled-mutation">
      <p class="abc-caption"><strong>A — Controlled mutation.</strong> The cell repeats twice, changes one pitch on its third statement, then returns to close.</p>
      <p class="abc-description">A four-bar Am7 vamp with a syncopated cell, one pitch substitution, and a resolved final statement.</p>
      <pre class="abc-source">X:1
T:Static Funk Vamp — controlled mutation
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | [ace]8 | [ace]8 | [ace]8 |]
[V:LH] "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^varied"z1 A,,1 z1 E,,1 A,,2 z2 | "^resolve"z1 A,,1 z1 C,,1 A,,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="static-vamp-dead-repetition">
      <p class="abc-caption"><strong>B — Dead repetition.</strong> The identical cell, unchanged across all four bars.</p>
      <p class="abc-description">The same four-bar Am7 vamp with the same cell repeated exactly, with no substitution and no space.</p>
      <pre class="abc-source">X:1
T:Static Funk Vamp — dead repetition
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | [ace]8 | [ace]8 | [ace]8 |]
[V:LH] "^static"z1 A,,1 z1 C,,1 A,,2 z2 | "^static"z1 A,,1 z1 C,,1 A,,2 z2 | "^static"z1 A,,1 z1 C,,1 A,,2 z2 | "^static"z1 A,,1 z1 C,,1 A,,2 z2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A: the third bar's single changed note gives the ear something to notice, and the final bar's held resolution reads as an ending rather than just another repetition. Play **Full** on B: the same funky cell, note for note, but by the fourth identical bar it has stopped registering as a groove and started registering as a loop.

## See

Bars one and two are identical in both panels — this isn't a chapter about the cell itself, which is equally good in both. The difference is entirely in bar three: A substitutes one pitch (`E,,` for `C,,`) and tags it `"^varied"`; B repeats the original pitch again and tags it `"^static"`. Bar four in A extends the final note into a resolution; bar four in B is the fourth identical copy of the same bar.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="static-vamp-cell-and-mutation">
  <p class="abc-caption"><strong>Cell, Then One Change.</strong> Practice stating a cell once, then mutating exactly one note on its repeat.</p>
  <p class="abc-description">Two bars of a syncopated Dm7 cell, the second bar substituting one pitch.</p>
  <pre class="abc-source">X:1
T:Cell, Then One Change
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | [dfa]8 |]
[V:LH] "^cell"z1 D,,1 z1 F,,1 D,,2 z2 | "^varied"z1 D,,1 z1 A,,1 D,,2 z2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play the two bars back to back and notice how little has to change for the repetition to stop sounding identical — one pitch, same rhythm, same register. Then try changing a second note in the same bar and listen for the point where "one controlled mutation" starts to feel like "a different cell."

## Vary

Take "Cell, Then One Change" and replace the pitch substitution with a rhythmic displacement instead — shift the whole cell earlier or later by a single eighth note, keeping every pitch the same. Does a rhythmic mutation read as more or less disruptive to the cell's identity than a pitch mutation? Which would you reach for first if a static vamp needed to feel `restless` rather than merely `varied`?

## The Music

"Held Ground" is an eight-bar funk study that never leaves Am7. It states the cell twice, mutates it by substitution, restates it, mutates it again by rhythmic displacement, then spends a full bar in silence before the cell returns and finally resolves — repetition, mutation, and space, in that order, doing the entire job that a chord change would otherwise do.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="held-ground-study">
  <p class="abc-caption"><strong>Held Ground.</strong> One chord, eight bars, and a full bar of silence that makes the cell's return land harder.</p>
  <p class="abc-description">An eight-bar funk study over a single held Am7, combining repetition, two distinct controlled mutations, and a silent bar.</p>
  <pre class="abc-source">X:1
T:Held Ground
C:Alessandro Bessi
R:Funk study
M:4/4
L:1/8
Q:1/4=98
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | [ace]8 | [ace]8 | [ace]8 |
[ace]8 | [ace]8 | [ace]8 | [ace]8 |]
[V:LH] "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^varied"z1 A,,1 z1 E,,1 A,,2 z2 | "^cell"z1 A,,1 z1 C,,1 A,,2 z2 |
"^varied"A,,1 z1 C,,1 z1 A,,2 z2 | "^space"z8 | "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^resolve"z1 A,,1 z1 C,,1 A,,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"Held Ground" never plays a single note outside Am7's own chord tones, and the harmony never changes once in eight bars — every bit of interest comes from Groove decisions alone. What does that suggest about how much of what listeners call "a good bass line" actually depends on harmonic choices at all, versus decisions this book didn't get to until Part III?
