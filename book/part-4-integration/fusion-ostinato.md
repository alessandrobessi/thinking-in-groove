# Fusion Ostinato

*Chapter 38 — Part V, Design: Building Complete Bass Lines. A repeated bass cell can remain stable beneath upper change.*

## The Question

If the same two-note bass figure sits under four different chords without changing a single pitch, is that a mistake — or the entire point?

## The Mental Model

A **Fusion Ostinato** takes the previous chapter's premise and flips it: instead of the bass following the harmony's destinations, the bass holds a fixed shape and lets the harmony move past it. The identity of an ostinato is defined by what it *doesn't* do — it doesn't track the chord above it, doesn't approach each new root, doesn't voice-lead anywhere. The same fixed pitches simply mean something different against each new chord: a note that was the root under one chord becomes a fifth, a seventh, or a color tone under the next, entirely because the harmony above it moved, not because the bass did.

The common error is building something that *looks* like an ostinato — a short, repeated rhythmic shape — but secretly changes its pitches to match each new chord. That's not a flaw in the shape; it's a different technique entirely, a moving root-fifth pattern, and it's a perfectly good tool, just not this one. An ostinato's entire value is the stability it offers underneath change: if the pitches move every time the chord does, there's no longer a fixed point for the ear to measure the harmony's motion against.

This is Chapter 4's Pedal, generalized from a single held note to a short repeated figure, and it works for exactly the reason a Pedal does — a genuinely fixed reference is what lets the ear register everything else as moving. Take the fixed point away and there's nothing left to measure the harmony's motion against; the whole texture just becomes a sequence of unrelated moments instead of change happening *relative to* something.

## The Microscope

Both panels use the identical two-note rhythmic shape under the same four chords. Only whether the pitches stay fixed changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="fusion-ostinato-lab">
  <div class="comparison-controls" aria-label="Fusion Ostinato comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Constant</button>
    <button type="button" data-version="B" aria-pressed="false">B — Tracking</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="fusion-ostinato-stable">
      <p class="abc-caption"><strong>A — Constant beneath upper change.</strong> The identical G-D figure repeats under all four chords without changing a note.</p>
      <p class="abc-description">A fixed two-note ostinato under Cmaj7, Am7, Dm7, and G7, reinterpreted freshly by each chord.</p>
      <pre class="abc-source">X:1
T:Fusion Ostinato — constant beneath upper change
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |]
[V:LH] "^ostinato"G,,2 D,,2 G,,2 D,,2 | "^ostinato"G,,2 D,,2 G,,2 D,,2 | "^ostinato"G,,2 D,,2 G,,2 D,,2 | "^ostinato"G,,2 D,,2 G,,2 D,,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="fusion-ostinato-tracking">
      <p class="abc-caption"><strong>B — A shape that tracks the chord instead.</strong> The identical rhythm, but the pitches change every bar to become each chord's own root and fifth.</p>
      <p class="abc-description">The same rhythmic figure restated as a moving root-fifth pattern under Cmaj7, Am7, Dm7, and G7.</p>
      <pre class="abc-source">X:1
T:Fusion Ostinato — a shape that tracks the chord instead
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[ceg]8 | "Am7"[ace]8 | "Dm7"[dfa]8 | "G7"[gbd]8 |]
[V:LH] "^tracks"C,,2 G,,2 C,,2 G,,2 | "^tracks"A,,2 E,,2 A,,2 E,,2 | "^tracks"D,,2 A,,2 D,,2 A,,2 | "^tracks"G,,2 D,,2 G,,2 D,,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and notice that the same two notes read completely differently against each chord — grounded under G7, colorful and slightly outside under Dm7 — without the bass line itself ever moving. Play **Full** on B: the bass now sounds like a conventional walking root-fifth pattern, competent and correct, but with none of the fixed-point character A has.

## See

The right-hand staff is identical in both panels. In A, the left hand is the exact same four notes, `G,, D,, G,, D,,`, copy-pasted across all four bars — that literal repetition is what makes it an ostinato. In B, the letter names change every bar to match the chord above (`C,, G,,` under Cmaj7, `A,, E,,` under Am7, and so on) — the rhythm is identical, but the pitches are not, which is exactly why it's tagged `"^tracks"` instead of `"^ostinato"`.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="fusion-ostinato-two-chords">
  <p class="abc-caption"><strong>Hold the Cell.</strong> Practice keeping an ostinato's pitches fixed across a chord change.</p>
  <p class="abc-description">The identical G-D ostinato figure held under Am7 and then Dm7 without changing a note.</p>
  <pre class="abc-source">X:1
T:Hold the Cell
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ace]8 | "Dm7"[dfa]8 |]
[V:LH] "^ostinato"G,,2 D,,2 G,,2 D,,2 | "^ostinato"G,,2 D,,2 G,,2 D,,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play both bars and resist the very strong pull to slide the second bar's notes toward Dm7's own root and fifth — that impulse is exactly what an ostinato asks you to override. The chord is allowed to reinterpret the bass; the bass doesn't have to reinterpret itself for the chord.

## Vary

Take "Hold the Cell" and change only the second bar, letting the ostinato shift to Dm7's own root and fifth. At what point in a longer passage would that kind of shift stop being "the ostinato tracking the chord" and start being a deliberate, occasional variation on an otherwise-stable ostinato — closer to Variation Without Collapse than to abandoning the device entirely?

## The Music

"Fixed Point" is an eight-bar fusion study in E natural minor that holds the identical B-F# ostinato under seven bars of changing harmony — Em7, Cmaj7, D7, and Bm7, twice through — before letting the ostinato dissolve into a single sustained B in the final bar, the one moment where the bass's fixed pitch and the harmony's actual root finally line up.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="fixed-point-study">
  <p class="abc-caption"><strong>Fixed Point.</strong> Seven bars of an unmoving ostinato resolve into the one bar where it was the root all along.</p>
  <p class="abc-description">An eight-bar fusion study in E natural minor over Em7, Cmaj7, D7, and Bm7 (twice), holding a fixed B-F# ostinato until the final bar's resolution.</p>
  <pre class="abc-source">X:1
T:Fixed Point
C:Alessandro Bessi
R:Fusion study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Em7"[egb]8 | "Cmaj7"[ceg]8 | "D7"[d^fa]8 | "Bm7"[d^fb]8 |
"Em7"[egb]8 | "Cmaj7"[ceg]8 | "D7"[d^fa]8 | "Bm7"[d^fb]8 |]
[V:LH] "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 |
"^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^ostinato"B,,2 ^F,,2 B,,2 ^F,,2 | "^resolve"B,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

For seven bars, "Fixed Point" plays B under chords where B is a fifth, a seventh, and a thirteenth before finally landing on a bar where B is the root. Did the ostinato change meaning seven times, or did it mean the same thing throughout and the harmony simply caught up to it in the last bar? Which of those two descriptions is more useful to a bassist actually playing the part?
