# The Bass-Line Design Algorithm

*Chapter 35 — Part V, Design: Building Complete Bass Lines. Opens the Part: a repeatable sequence turns harmony into a tested bass line.*

## The Question

Given nothing but a chord chart, what's the actual order of decisions that turns it into a bass line — and how would you know if you'd skipped one?

## The Mental Model

Every earlier chapter in this book isolated one question at a time: what job is this note doing (Role), where is it going harmonically (Motion), how does it sit in time (Groove), and how does it relate to the layer above it (Interaction). In real playing, none of these get answered separately — every note answers all four at once. The **Design Algorithm** names the order in which to answer them deliberately, before they collapse into a single physical note played from habit instead of choice:

1. **Read the harmonic rhythm.** How often does the chord actually change? This constrains everything that follows — a slow harmonic rhythm invites Staying or a Pedal; a fast one invites Connecting Chords.
2. **Choose a Role for each structurally important moment.** Ground, Definer, Inverter, Colorist, Shadow, Voice-Leader, or Commentator — what job does this note need to do?
3. **Choose the Motion that connects those moments.** Stepping, Approaching, Enclosing, Arpeggiating, Leaping, Connecting Chords, or Contrary Motion — how does the bass travel between the Roles you just placed?
4. **Choose the Groove that places those notes in time.** Subdivision, Attack Placement, Duration, Space, Syncopation, Repeated Cells, Variation, Phrase Rhythm — when, exactly, does each note land?
5. **Choose the Interaction between the two layers.** Doubling, Independence, Interlock, Call and Response, Density Balance, Register and Separation — how does the bass relate to whatever the harmony is doing at that same instant?
6. **Test it by ear, then vary one layer at a time.** If something doesn't work, isolate which of the five decisions above is the actual cause before changing anything else.

A bass line produced this way is traceable: point at any note and you can name the Role, Motion, Groove, and Interaction choice that put it there. That traceability is the entire value of the algorithm — not that it produces a single correct answer (it doesn't; two players can walk every step and land on different, equally valid lines), but that it guarantees every note was actually decided rather than defaulted into.

## The Microscope

Both panels sit over the identical harmony. Only whether the bass line is traceable to a decision changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="design-algorithm-lab">
  <div class="comparison-controls" aria-label="Design Algorithm comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Traceable</button>
    <button type="button" data-version="B" aria-pressed="false">B — Arbitrary</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="design-algorithm-traceable">
      <p class="abc-caption"><strong>A — A traceable choice at every bar.</strong> Ground on Dm7, a stepwise connection into G7, a resolved Ground on Cmaj7.</p>
      <p class="abc-description">The book's three-chord laboratory progression, Dm7-G7-Cmaj7, with every bass note answering a specific Role and Motion decision.</p>
      <pre class="abc-source">X:1
T:The Design Algorithm — a traceable choice at every bar
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 |]
[V:LH] "^ground"D,,8 | "^connect"D,,2 E,,2 F,,2 G,,2 | "^resolve"C,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="design-algorithm-arbitrary">
      <p class="abc-caption"><strong>B — The same harmony, no traceable choice.</strong> Every note is a legal chord tone; none of them answers a specific question.</p>
      <p class="abc-description">The identical progression with a bass line built from correct chord tones placed without a governing Role, Motion, or Groove decision.</p>
      <pre class="abc-source">X:1
T:The Design Algorithm — the same harmony, no traceable choice
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 |]
[V:LH] "^arbitrary"F,,2 z1 A,,1 D,,4 | "^arbitrary"B,,4 D,,4 | "^arbitrary"E,,2 G,,2 C,,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A: the bass reads as a small, coherent story — settle, travel, arrive. Play **Full** on B: every individual note is a correct chord tone, and nothing about it is wrong, but it doesn't build toward anything, because no single decision governs where the notes came from.

## See

In A, bar one is a plain Ground (the root, held); bar two is a Connecting Motion stepping from D up to G one letter at a time; bar three resolves onto Cmaj7's Ground. Each tag — `"^ground"`, `"^connect"`, `"^resolve"` — names an actual decision from the algorithm above. In B, `F,, A,, D,,` in bar one are all legal Dm7 tones, but nothing links their order, their rhythm, or their register to a Role or a Motion; the `"^arbitrary"` tag marks exactly that absence.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="design-algorithm-two-chords">
  <p class="abc-caption"><strong>Walk the Algorithm.</strong> Practice naming a Role and a Motion before you play, across a chord change.</p>
  <p class="abc-description">A held Ground on Am7 connected by a stepwise line into Dm7.</p>
  <pre class="abc-source">X:1
T:Walk the Algorithm
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | "Dm7"[dfa]8 |]
[V:LH] "^ground"A,,8 | "^connect"A,,2 B,,2 C,,2 D,,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Before you play either bar, say out loud which Role and which Motion you're about to play. Then play it, and check whether what you heard matches what you said. If it doesn't, the mismatch is more informative than either the plan or the result alone.

## Vary

Take "Walk the Algorithm" and change only step 5 of the process: instead of a plain Ground on Am7, choose a Density Balance decision — make the bass busy under a sustained chord instead. Everything else (the Role's target pitch, the connecting motion into Dm7) can stay the same. How much of the phrase's identity survives changing just one layer of the stack?

## The Music

"By the Book" is an eight-bar jazz-funk study that walks a different step of the algorithm in every bar — Ground, a stepwise Connection, a Colorist choice, Independence, Density Balance, Register and Separation, a Call-and-Response handoff, and a final resolved Ground — over four changing chords, deliberately touring the vocabulary this whole book has built rather than settling into one recurring pattern.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="by-the-book-study">
  <p class="abc-caption"><strong>By the Book.</strong> Eight bars, eight distinct, traceable decisions.</p>
  <p class="abc-description">An eight-bar jazz-funk study over Cmaj7, Am7, Dm7, and G7, touring a different Role, Motion, Groove, or Interaction choice in each bar.</p>
  <pre class="abc-source">X:1
T:By the Book
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |
"Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]4 z4 | "G7"[gbd]8 |]
[V:LH] "^ground"C,,8 | "^connect"C,,2 B,,2 A,,4 | "^colorist"E,,8 | "^independent"z1 G,,1 z1 B,,1 z1 D,,1 z1 B,,1 |
"^dense"C,,1 D,,1 E,,1 D,,1 C,,1 D,,1 E,,1 D,,1 | "^separated"A,,8 | z4 "^response"D,,2 F,,2 | "^resolve"G,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"By the Book" never repeats a decision across its eight bars — every bar demonstrates a different step of the algorithm in isolation. A real bass line usually repeats the same handful of choices throughout a whole piece instead. Does walking the algorithm only matter the first time you set a groove, or does it stay useful every time you're deciding whether to keep repeating that choice or change it?
