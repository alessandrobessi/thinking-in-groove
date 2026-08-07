# Complete Capstone

*Chapter 40 — Part V, Design: Building Complete Bass Lines. Closes the book: one sixteen-bar composition demonstrates the entire method.*

## The Question

Can one piece of music actually carry a Ground, an Approach Note, a Connecting run, a Repeated Cell, a Variation, a Space, a Density Balance choice, a Call and Response, and an Inversion — and still sound like one coherent line rather than a checklist?

## The Mental Model

Every chapter before this one demonstrated one idea in isolation, because isolation is how a single idea gets learned clearly. A finished bass line never works that way — it stacks every layer at once, the way Chapter 35's Design Algorithm described, and this closing chapter is that algorithm run in full, across a real sixteen-bar piece instead of a three-chord laboratory.

The **Complete Capstone** below moves through four four-bar sections, each adding one more layer on top of what came before, in the same order the Design Algorithm names them:

- **Bars 1–4** fix the harmonic situation and establish a plain Ground on every chord — nothing else yet.
- **Bars 5–8** add Motion: an Approach Note, a stepwise Connecting run, and a second Approach Note prepare each new chord.
- **Bars 9–12** add Groove: a Repeated Cell, a controlled pitch Variation, and a full bar of Space.
- **Bars 13–16** add Interaction and resolve: a Density Balance passage, a Call and Response handoff, one more Approach, and a final Ground that closes the piece.

Nothing in the last four bars contradicts anything decided in the first four — the opening Ground is still there in spirit at the very end, just surrounded by everything the book added since Chapter 1. That's the entire claim of this chapter: complexity is additive, not a replacement for the fundamentals, and a finished line is still checkable one layer at a time even after every layer is present at once.

## The Microscope

Both panels use the piece's actual opening four bars, note for note the same chords. Only whether the bass line was designed changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="capstone-lab">
  <div class="comparison-controls" aria-label="Complete Capstone comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Designed</button>
    <button type="button" data-version="B" aria-pressed="false">B — Arbitrary</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="capstone-opening-designed">
      <p class="abc-caption"><strong>A — Designed.</strong> A plain Ground on every chord, exactly as the capstone piece actually opens.</p>
      <p class="abc-description">The Complete Capstone's real opening four bars: Cmaj7, Am7, Dm7, and G7, each answered by its own root.</p>
      <pre class="abc-source">X:1
T:The Capstone's Opening — designed
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |]
[V:LH] "^ground"C,,8 | "^ground"A,,8 | "^ground"D,,8 | "^ground"G,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="capstone-opening-arbitrary">
      <p class="abc-caption"><strong>B — Arbitrary.</strong> The identical four chords, with every bass note a correct but undecided chord tone.</p>
      <p class="abc-description">The same four-chord opening with a bass line built from legal chord tones placed without a governing Role.</p>
      <pre class="abc-source">X:1
T:The Capstone's Opening — arbitrary
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |]
[V:LH] "^arbitrary"E,,2 z1 G,,1 C,,4 | "^arbitrary"C,,4 E,,4 | "^arbitrary"A,,2 F,,2 D,,4 | "^arbitrary"D,,4 B,,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and hear four plain, settled arrivals — nothing demanding attention yet, which is exactly right for an opening the rest of the piece is about to build on. Play **Full** on B: every note is a correct chord tone, and the passage is not unpleasant, but it commits to nothing a listener could point back to later as "the way this piece started."

## See

This is Chapter 35's own demonstration, reused on the capstone's real material instead of the three-chord laboratory: A's four bars are tagged `"^ground"` throughout, one plain, deliberate choice per bar. B's bars are tagged `"^arbitrary"`, built from chord tones with no shared logic between them. The rest of the capstone below is built by adding to A's foundation — B is only here to show what the piece would have sounded like without one.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="capstone-two-chords">
  <p class="abc-caption"><strong>Name It, Then Play It.</strong> Practice naming a Role and a Motion before playing the exact figure the capstone uses at its own chord change.</p>
  <p class="abc-description">A held Dm7 Ground followed by the chromatic Approach Note the capstone itself uses twice.</p>
  <pre class="abc-source">X:1
T:Name It, Then Play It
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 |]
[V:LH] "^ground"D,,8 | "^approach"F,,2 ^F,,2 G,,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Say the Role and the Motion out loud before you play each bar, the same discipline Chapter 35 asked for. Then find both bars inside the full capstone below — bar 3 and bar 8 use this exact same approach figure — and notice that a technique worth naming once is usually worth reusing deliberately, not just once for a demonstration.

## Vary

Choose any single bar from the capstone below and redesign it by changing exactly one layer — its Role, its Motion, its Groove, or its Interaction — while leaving the other three untouched. Does the piece still hold together, or does that one change ripple into bars around it? A design that survives a single deliberate change without falling apart is a stronger design than one that merely sounded fine before you tested it.

## The Music

**The Complete Capstone** is a sixteen-bar jazz-funk piece over Cmaj7, Am7, Dm7, and G7, built in four four-bar stages that add Ground, then Motion, then Groove, then Interaction, before a closing Approach and a final resolved Ground bring it home — the entire book's method, run once, start to finish.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="complete-capstone">
  <p class="abc-caption"><strong>The Complete Capstone.</strong> Four four-bar stages, each adding one more layer without erasing what came before.</p>
  <p class="abc-description">A sixteen-bar jazz-funk capstone cycling Cmaj7, Am7, Dm7, and G7, building from a plain Ground through Motion, Groove, and Interaction to a final resolution.</p>
  <pre class="abc-source">X:1
T:The Complete Capstone
C:Alessandro Bessi
R:Jazz-funk capstone
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
%%barsperstaff 4
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |
"Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |
"Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |
"Dm7"[dfa]8 | "G7"[gbd]4 z4 | "Cmaj7"[ceg]8 | "Cmaj7"[ceg]8 |]
[V:LH] "^ground"C,,8 | "^ground"A,,8 | "^ground"D,,8 | "^ground"G,,8 |
"^ground"C,,8 | "^approach"B,,4 A,,4 | "^connect"A,,2 B,,2 C,,2 D,,2 | "^approach"F,,2 ^F,,2 G,,4 |
"^cell"z1 C,,1 z1 E,,1 C,,2 z2 | "^cell"z1 A,,1 z1 C,,1 A,,2 z2 | "^varied"z1 D,,1 z1 A,,1 D,,2 z2 | "^space"z8 |
"^dense"D,,1 E,,1 F,,1 E,,1 D,,1 E,,1 F,,1 E,,1 | z4 "^response"G,,2 B,,2 | "^approach"B,,4 C,,4 | "^resolve"C,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Forty chapters ago, this book opened by asking what job a single bass note is doing underneath a chord. The Complete Capstone closes by showing that every one of this book's questions — what job, what motion, what timing, what relationship to the layer above — can still be asked and answered about a single note, even inside a finished sixteen-bar piece built from all of them at once. That was always the point of naming things this precisely: not to make you think about all of it while you play, but to give you a way to find, and fix, the one bar that isn't working — without having to guess which layer is actually responsible.
