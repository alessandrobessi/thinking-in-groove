# Density Balance

*Chapter 32 — Part IV, Interaction: What Happens Between Bass and Harmony? The relative note-count and activity level between the bass and harmony layers is a deliberate, relational choice.*

## The Question

Is a bass line "busy" on its own terms, or only busy compared to what the other hand is doing at the same moment?

## The Mental Model

**Density Balance** means the relative note-count and activity level between the bass and harmony layers is a deliberate, relational choice. It is not a property of the bass line alone. A running eighth-note bass line under sustained whole-note chords reads as active and driving; the identical bass line under an equally busy right hand reads as cluttered, because now two dense layers are competing for the same attention instead of one dense layer being supported by a still one.

The common error is judging a bass line's density in isolation — counting its note attacks and calling it "busy" or "sparse" without checking what the harmony layer is doing at that same instant. The same sixteen eighth notes can be a balanced foundation or a crowded mess, depending entirely on what's stacked against them.

This is the same relativity Chapter 26 established for a single bass line across time — a bar's density only means something next to its neighboring bars — applied here across the two staves at the same instant instead. And the underlying stakes are the ones Chapter 7's Supporter already named: attention is limited, and two equally busy layers compete for the same slice of it rather than adding up to "twice as much good material." Density Balance is that same competition, examined as its own deliberate design decision rather than a rule about when the bass specifically should get out of the way.

## The Microscope

Both panels use the identical bass line. Only the right hand changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="density-balance-lab">
  <div class="comparison-controls" aria-label="Density Balance comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Balanced</button>
    <button type="button" data-version="B" aria-pressed="false">B — Competing</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="density-balance-relational">
      <p class="abc-caption"><strong>A — A relational choice.</strong> A busy bass line paired with a single sustained chord stays clear and driving.</p>
      <p class="abc-description">An eight-note running Cmaj7 bass line under one sustained whole-note chord.</p>
      <pre class="abc-source">X:1
T:Density Balance — a relational choice
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEG]8 |]
[V:LH] "^dense"C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="density-balance-competing">
      <p class="abc-caption"><strong>B — The same bass, now competing.</strong> The identical bass line under an equally busy right hand crowds the same texture.</p>
      <p class="abc-description">The identical eight-note bass line, now paired with an equally active right-hand line instead of a sustained chord.</p>
      <pre class="abc-source">X:1
T:Density Balance — the same bass, now competing
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"C1 D1 E1 F1 G1 F1 E1 D1 |]
[V:LH] "^competing"C,,1 D,,1 E,,1 F,,1 G,,1 F,,1 E,,1 D,,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A: the running bass line has room to be heard clearly against the still chord above it. Play **Full** on B: the exact same bass notes are still there, but now they're fighting the right hand's equally busy line for the ear's attention, and the texture feels crowded rather than driving.

## See

The left-hand staff is byte-for-byte identical in both panels — `"^dense"`/`"^competing"` is the only label that changes, and it changes because the relationship changed, not the bass line itself. In A, the right hand is a single eight-unit sustained chord (`[CEG]8`); in B, it's the same eight-unit space filled with eight separate attacks. Nothing about the bass line's own note count tells you which panel you're in.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="density-balance-two-chords">
  <p class="abc-caption"><strong>Busy Under Sparse.</strong> Practice keeping a running bass line legible under sustained harmony, across a chord change.</p>
  <p class="abc-description">Two bars of an eight-note running bass line under a single sustained chord per bar, over Am7 then Dm7.</p>
  <pre class="abc-source">X:1
T:Busy Under Sparse
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[ACE]8 | "Dm7"[DFA]8 |]
[V:LH] "^dense"A,,1 C,,1 E,,1 C,,1 A,,1 C,,1 E,,1 C,,1 | "^dense"D,,1 F,,1 A,,1 F,,1 D,,1 F,,1 A,,1 F,,1 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play both bars, then play the right-hand chord as a matching eight-note run instead of a sustained chord, and compare how the identical bass line reads in each case. The bass hand should not need to change anything to feel the difference.

## Vary

Take "Busy Under Sparse" and reduce the right hand from a single sustained chord to two half-note chords per bar — still far less active than the bass, but no longer a single unbroken sustain. Does the bass line still read as balanced against it, or does the balance start to shift? At what point does raising the right hand's activity turn balance into competition?

## The Music

"Give and Take" is an eight-bar jazz-funk study that trades which layer carries the density: on the first bar of each chord the bass runs while the right hand sustains, and on the second bar the roles reverse, with the right hand running while the bass drops to a single sustained root. The balance holds throughout — only which layer is busy ever changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="give-and-take-study">
  <p class="abc-caption"><strong>Give and Take.</strong> The two layers trade which one runs and which one sustains, chord by chord.</p>
  <p class="abc-description">An eight-bar jazz-funk study in B major over Bmaj7, G#m7, C#m7, and F#7, alternating a running bass under sustained harmony with a running harmony under a sustained bass.</p>
  <pre class="abc-source">X:1
T:Give and Take
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Bmaj7"[B^d^f]8 | "Bmaj7"B1 ^c1 ^d1 ^c1 B1 ^c1 ^d1 ^c1 | "G#m7"[B^d^g]8 | "G#m7"^g1 B1 ^d1 B1 ^g1 B1 ^d1 B1 |
"C#m7"[^ce^g]8 | "C#m7"^c1 e1 ^g1 e1 ^c1 e1 ^g1 e1 | "F#7"[^c^f^a]8 | "F#7"[^c^f^a]8 |]
[V:LH] "^dense"B,,1 ^C,1 ^D,1 ^C,1 B,,1 ^C,1 ^D,1 ^C,1 | "^sparse"B,,8 | "^dense"^G,1 B,,1 ^D,1 B,,1 ^G,1 B,,1 ^D,1 B,,1 | "^sparse"^G,8 |
"^dense"^C,1 E,1 ^G,1 E,1 ^C,1 E,1 ^G,1 E,1 | "^sparse"^C,8 | "^dense"^F,1 ^A,1 ^C,1 ^A,1 ^F,1 ^A,1 ^C,1 ^A,1 | "^resolve"^F,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

In "Give and Take," the busy layer and the sparse layer swap on every second bar, but the two never run at the same time. What would you expect to happen to the texture's clarity if, just once, both layers ran busy together for a single bar — and would that necessarily be a mistake, or could it serve a purpose the rest of the piece doesn't?
