# Enclosing

*Chapter 12 — Part II, Motion: How Does the Bass Travel?*

## The Question

How can two notes on either side of a target make its arrival feel more inevitable than a single approach note does?

## The Mental Model

**Enclosing** surrounds a target with an upper neighbour and a lower neighbour immediately before it arrives. It's a stronger, more deliberate cousin of Approaching (Chapter 11): where Approaching commits to one direction, Enclosing frames the target from both sides at once, so the arrival reads as the resolution of a small, self-contained gesture rather than a single directional nudge.

An arbitrary three-note turn isn't automatically an Enclosure — both neighbour notes have to actually point at the *same* target. Ab and F# only enclose G because both sit a half step away from it, one above and one below. Swap either neighbour for a note that doesn't share that relationship to G, and the figure stops enclosing anything.

An Approach note leans; an Enclosure closes. A single directional approach still leaves the ear with an open question — it points at a target but hasn't ruled anything out except the one direction it came from. Framing the target from both sides at once removes that remaining ambiguity: there's no direction left for the target to have arrived from, so the gesture reads as a complete, self-contained shape rather than a lean that happened to land. That's the real reason Enclosing sounds more "prepared" than Approaching even at the identical tempo and target — it isn't more emphatic, it's more exhaustive.

Arpeggiating, next, moves in the opposite direction from both of these techniques: instead of decorating the space immediately around one target, it uses a chord's own tones — often spanning a wider interval than any neighbour tone here — to build an entire directed phrase.

## The Microscope

Both versions arrive on the same G. Only how many notes surround the arrival changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="enclosing-lab">
  <div class="comparison-controls" aria-label="Enclosing comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Direct approach</button>
    <button type="button" data-version="B" aria-pressed="false">B — Enclosure</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="enclosing-direct-approach">
      <p class="abc-caption"><strong>A — A direct approach.</strong> One neighbour, F#, leads into G from below.</p>
      <p class="abc-description">A single approach note into the G7 root.</p>
      <pre class="abc-source">X:1
T:Enclosing — a direct approach
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "G7"[DFGB]8 |]
[V:LH] "^approach"C,6 ^F,2 | "^arrive"G,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="enclosing-neighbours">
      <p class="abc-caption"><strong>B — An enclosure.</strong> Ab from above and F# from below both surround G before it arrives.</p>
      <p class="abc-description">The same arrival, now framed by both neighbour tones in sequence.</p>
      <pre class="abc-source">X:1
T:Enclosing — upper and lower neighbours
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "G7"[DFGB]8 |]
[V:LH] "^enclose"C,4 _A,2 ^F,2 | "^arrive"G,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A's approach note gives G a single, clear direction to resolve from. B's two neighbour notes create a small orbit around G before landing — listen for how much more "prepared" the arrival feels with both sides represented, even though the target note itself is identical.

## See

In B, Ab sits a half step above G and F# sits a half step below it — both neighbours are visibly equidistant from the target on the staff. That symmetry is what the notation shows and what distinguishes a genuine Enclosure from two unrelated ornamental notes that happen to precede an arrival.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="enclosing-surround-the-target">
  <p class="abc-caption"><strong>Surround the Target.</strong> Two enclosures, each resolving to a different chord's root.</p>
  <p class="abc-description">Four bars alternating an enclosure figure with its resolution.</p>
  <pre class="abc-source">X:1
T:Surround the Target
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Am7"[ACEG]8 | "Cmaj7"[CEGB]8 | "Dm7"[DFAC]8 |]
[V:LH] "^enclose"C,4 _B,2 ^G,2 | "^arrive"A,8 | "^enclose"C,4 _E,2 ^C,2 | "^arrive"D,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Say the neighbour relationship out loud before you play each enclosure: "half step above, half step below, then the target." Naming the relationship before playing it is usually faster than finding it by ear alone.

## Vary

Reverse the order of the two neighbour notes in each enclosure (lower neighbour first, then upper). Does the target still feel enclosed, or does reordering change which neighbour reads as the "real" approach and which reads as decoration?

## The Music

"Encircle" is an original eight-bar jazz study in E major, swung throughout, that uses an enclosure to introduce each new chord's root.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="encircle-study">
  <p class="abc-caption"><strong>Encircle.</strong> Every new chord root in this study is framed by its own enclosure first.</p>
  <p class="abc-description">A swung eight-bar jazz study in E major moving through Emaj7, C#m7, F#m7, and B7, each arrival enclosed.</p>
  <pre class="abc-source">X:1
T:Encircle
C:Alessandro Bessi
R:Jazz study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Emaj7"[E^GB^d]8 | "Emaj7"[E^GB^d]8 | "C#m7"[E^GB^c]8 | "C#m7"[E^GB^c]8 |
"F#m7"[E^FA^c]8 | "F#m7"[E^FA^c]8 | "B7"[^FAB^d]8 | "B7"[^FAB^d]8 |]
[V:LH] "^stay"E,8 | "^enclose"E,4 D>C | "^arrive"^C8 | "^stay"^C8 |
"^enclose"^C4 G,>F, | "^arrive"^F,8 | "^enclose"^F,4 C>^A, | "^arrive"B,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Every arrival in "Encircle" is enclosed the same way: hold, then upper neighbour, then lower neighbour, then land. Would the study lose anything if one arrival used a plain Approaching instead — or does the repetition of the full enclosure figure itself become part of the piece's identity?
