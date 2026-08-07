# Stepping

*Chapter 10 — Part II, Motion: How Does the Bass Travel?*

## The Question

What makes a bass line sound smooth rather than jumpy, independent of where it eventually ends up?

## The Mental Model

**Stepping** is motion by adjacent (second) intervals — a series of steps that produces a smooth melodic contour. It's a statement about *shape*, not about *destination*.

That distinction matters because Stepping is easy to confuse with Connecting Chords (Chapter 15). A stepwise line can simply wander within one unchanging harmony, going nowhere in particular — that's Stepping on its own. The moment those same steps are aimed specifically at landing on the next chord's root as the harmony changes, the line is doing something more specific: it's Connecting Chords. Every Connecting Chords route may use steps, but not every stepwise line is connecting anything.

## The Microscope

The bass plays the same three ascending steps both times. Only whether the harmony moves to meet them changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="stepping-lab">
  <div class="comparison-controls" aria-label="Stepping comparison">
    <button type="button" data-version="A" aria-pressed="true">A — No destination</button>
    <button type="button" data-version="B" aria-pressed="false">B — Becomes a destination</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="stepping-no-destination">
      <p class="abc-caption"><strong>A — Stepping, no destination.</strong> The harmony never changes, so the steps are pure contour.</p>
      <p class="abc-description">Two bars of unchanging Cmaj7 while the bass steps up and back down.</p>
      <pre class="abc-source">X:1
T:Stepping — smooth contour, no destination
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^step"C,2 D,2 E,2 D,2 | "^step"C,2 D,2 E,2 D,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="stepping-destination">
      <p class="abc-caption"><strong>B — The same steps, now a destination.</strong> The harmony changes to Dm7 exactly as the steps arrive on D.</p>
      <p class="abc-description">The identical opening three steps, now landing precisely on the new chord's root.</p>
      <pre class="abc-source">X:1
T:Stepping — the same steps, now a destination
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Dm7"[DFAC]8 |]
[V:LH] "^step"C,2 D,2 E,2 z2 | "^arrive: this is Connecting Chords now"D,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Harmony only** on both: A holds one chord for two bars; B changes chord exactly when the steps would logically continue. Now play **Full** and compare. The bass gesture in bar 1 is identical in both versions — the difference only becomes audible once bar 2 either repeats the same harmony (A) or arrives somewhere new (B).

## See

In A, the steps end where they started (C up to E, back down toward D) — a shape with no destination stated anywhere on the page. In B, the final step lands exactly on the new chord symbol's root, at the exact moment it appears. The notation itself shows the difference: alignment between a bass arrival and a chord symbol is what turns Stepping into Connecting Chords.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="stepping-smooth-ground">
  <p class="abc-caption"><strong>Smooth Ground.</strong> A four-bar stepwise contour under one unchanging chord.</p>
  <p class="abc-description">Four bars of Cmaj7 while the bass climbs, descends, climbs again, and settles.</p>
  <pre class="abc-source">X:1
T:Smooth Ground
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^step"C,2 D,2 E,2 F,2 | "^step"G,2 F,2 E,2 D,2 | "^step"C,2 D,2 E,2 F,2 | "^step: settle"G,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play all four bars without letting any note announce itself as more important than the others — the point is the shape of the line, not any one arrival. Then notice: the line never had anywhere it had to go, and it was still satisfying to play.

## Vary

Keep every pitch and rhythm identical. Add a new chord symbol under bar 4's final G (say, a C/G or a G7). Does the line retroactively feel like it was heading toward that destination all along, even though nothing about the bass part itself changed?

## The Music

"Even Ground" is an original eight-bar jazz study built almost entirely from stepwise motion, even as the harmony itself moves through four different chords.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="even-ground-study">
  <p class="abc-caption"><strong>Even Ground.</strong> A continuously stepwise bass line under a moving ii-V-based progression.</p>
  <p class="abc-description">An eight-bar jazz study: Cmaj7, Am7, Dm7, and G7, connected almost entirely by adjacent motion.</p>
  <pre class="abc-source">X:1
T:Even Ground
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
[V:LH] "^step"C,2 D,2 E,2 F,2 | "^step"E,2 D,2 C,2 D,2 | "^step"E,2 F,2 G,2 A,2 | "^step"G,2 F,2 E,2 F,2 |
"^step"G,2 A,2 B,2 C2 | "^step"B,2 A,2 G,2 F,2 | "^step"G,2 A,2 B,2 C2 | "^step: settle"D2 C2 B,2 G,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Several notes in "Even Ground" land exactly on a new chord's root or a close chord tone as the harmony changes — moments that are arguably Connecting Chords, not pure Stepping. Find one and explain what makes it a destination rather than just another step in the contour.
