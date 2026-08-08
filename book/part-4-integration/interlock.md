# Interlock

*Chapter 30 — Part IV, Interaction: What Happens Between Bass and Harmony? Bass and upper voice alternate attacks so tightly that neither line alone carries the full rhythm.*

## The Question

If two staves take turns playing, when does that turn-taking become one fused rhythm instead of two separate voices trading places?

## The Mental Model

**Interlock** means the bass and the upper voice alternate attacks so tightly that neither line alone carries the full rhythm — only the two together form one composite groove. Play either staff by itself and you hear a sparse, gapped fragment; play them together and the gaps disappear, because each voice is filling exactly the silence the other one left.

The distance between the attacks is what makes this Interlock rather than Call and Response, the chapter that follows. Call and Response is a genuine handoff: one voice completes a full statement, then the other replies into the space that statement vacated — the turns are long enough to register as separate musical sentences. Interlock's attacks are continuous and fast, weaving together at the level of individual notes, not phrases. The common error is calling any back-and-forth between two staves "interlock," when a slower, phrase-length alternation is really Call and Response with a different name attached.

There's a real perceptual mechanism behind why speed is the deciding factor, not just a convenient rule of thumb. Hearing tracks separate sound sources by grouping nearby events in time and pitch into one stream; give it two things happening within roughly a sixteenth note of each other and it stops trying to track "who played what" and instead groups the whole sequence into a single perceived rhythm. Slow the same alternation down to phrase length and the gap between turns becomes wide enough for hearing to keep the two sources separately tracked, which is exactly why the same physical technique — one voice filling the other's silence — reads as one fused idea at high speed and as two voices taking turns at low speed.

## The Microscope

Both panels alternate between the two staves. Only the spacing of that alternation changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="interlock-lab">
  <div class="comparison-controls" aria-label="Interlock comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Interlock</button>
    <button type="button" data-version="B" aria-pressed="false">B — Call and response</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="interlock-fused-texture">
      <p class="abc-caption"><strong>A — A fused texture.</strong> The two staves trade sixteenth notes continuously; together they read as one uninterrupted line.</p>
      <p class="abc-description">A Cmaj7 arpeggio split between the hands, one sixteenth note at a time.</p>
      <pre class="abc-source">X:1
T:Interlock — a fused texture
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/16
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"C1z1E1z1G1z1E1z1 C1z1E1z1G1z1E1z1 |]
[V:LH] "^interlock"z1C,,1z1E,,1z1G,,1z1E,,1 z1C,,1z1E,,1z1G,,1z1E,,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="interlock-call-and-response">
      <p class="abc-caption"><strong>B — A call and response is not interlock.</strong> The right hand states a complete chord, then rests; the bass answers into the vacated space.</p>
      <p class="abc-description">A two-beat chordal call followed by a two-beat bass reply, with no overlap and no continuous weave.</p>
      <pre class="abc-source">X:1
T:Interlock — a call and response is not interlock
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEG]4 z4 |]
[V:LH] z4 "^response"C,,2 E,,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and notice that no single beat sounds empty — the moment the right hand's note decays, the bass fills the gap, and the ear reads a single continuous stream. Play **Full** on B: there's an unmistakable pause between the chord and the bass reply, and the rhythm reads as two separate statements, not one fused line.

## See

In A, the right hand's `"^interlock"` bass line occupies the exact sixteenth-note slots the melody leaves empty — read horizontally, no two staves ever attack at the same instant, and no gap is longer than a sixteenth note. In B, the bass is silent (`z4`) for the entire two-beat call, then plays its own two-beat answer; the gap between "call ends" and "response begins" is the whole reason it's labeled `"^response"` rather than `"^interlock"`.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="interlock-two-chords">
  <p class="abc-caption"><strong>Trade the Sixteenths.</strong> Practice keeping a continuous sixteenth-note weave across a chord change.</p>
  <p class="abc-description">Two bars of interlocking sixteenth notes between the hands, over Am7 then Dm7.</p>
  <pre class="abc-source">X:1
T:Trade the Sixteenths
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/16
Q:1/4=84
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"A1z1C1z1E1z1C1z1 A1z1C1z1E1z1C1z1 | "Dm7"D1z1F1z1A1z1F1z1 D1z1F1z1A1z1F1z1 |]
[V:LH] "^interlock"z1A,,1z1C,,1z1E,,1z1C,,1 z1A,,1z1C,,1z1E,,1z1C,,1 | "^interlock"z1D,,1z1F,,1z1A,,1z1F,,1 z1D,,1z1F,,1z1A,,1z1F,,1 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play slowly enough that you can feel each hand landing in the other's silence, then bring the tempo up until the two staves genuinely disappear into a single perceived line. If you can still hear "two hands taking turns" at speed, the interlock isn't tight enough yet.

## Vary

Take bar one of "Trade the Sixteenths" and delete every other bass attack, so the bass plays only on the first and third sixteenth-note gaps instead of all four. Does the texture still fuse into one line, or does it start to sound like two separate, sparser parts? At what point does thinning out the weave turn Interlock back into something closer to ordinary accompaniment?

## The Music

"Single Weave" is an eight-bar jazz-funk study in D major built entirely from continuous sixteenth-note interlock across four changing chords, then deliberately breaks the pattern in its final bar: both hands land together on one sustained chord, the first and only moment in the piece where the two staves attack at the same instant.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="single-weave-study">
  <p class="abc-caption"><strong>Single Weave.</strong> Seven bars of continuous interlock resolve into one shared final attack.</p>
  <p class="abc-description">An eight-bar jazz-funk study in D major over Dmaj7, Bm7, Em7, and A7, with sixteenth-note interlock throughout and a unison arrival in the last bar.</p>
  <pre class="abc-source">X:1
T:Single Weave
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/16
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dmaj7"D1z1^F1z1A1z1^F1z1D1z1^F1z1A1z1^F1z1 | "Bm7"B1z1D1z1^F1z1D1z1B1z1D1z1^F1z1D1z1 |
"Em7"E1z1G1z1B1z1G1z1E1z1G1z1B1z1G1z1 | "A7"A1z1^c1z1E1z1^c1z1A1z1^c1z1E1z1^c1z1 |
"Dmaj7"A1z1^F1z1D1z1^F1z1A1z1^F1z1D1z1^F1z1 | "Bm7"^F1z1D1z1B1z1D1z1^F1z1D1z1B1z1D1z1 |
"Em7"B1z1G1z1E1z1G1z1B1z1G1z1E1z1G1z1 | "A7"[A^ce]16 |]
[V:LH] "^interlock"z1D,,1z1^F,,1z1A,,1z1^F,,1z1D,,1z1^F,,1z1A,,1z1^F,,1 | "^interlock"z1B,,1z1D,,1z1^F,,1z1D,,1z1B,,1z1D,,1z1^F,,1z1D,,1 |
"^interlock"z1E,,1z1G,,1z1B,,1z1G,,1z1E,,1z1G,,1z1B,,1z1G,,1 | "^interlock"z1A,,1z1^C,1z1E,,1z1^C,1z1A,,1z1^C,1z1E,,1z1^C,1 |
"^interlock"z1A,,1z1^F,,1z1D,,1z1^F,,1z1A,,1z1^F,,1z1D,,1z1^F,,1 | "^interlock"z1^F,,1z1D,,1z1B,,1z1D,,1z1^F,,1z1D,,1z1B,,1z1D,,1 |
"^interlock"z1B,,1z1G,,1z1E,,1z1G,,1z1B,,1z1G,,1z1E,,1z1G,,1 | "^resolve"A,,16 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"Single Weave" spends seven bars making sure neither hand ever attacks at the same instant as the other, then breaks that rule exactly once, in the final bar. Why does landing together read as an arrival here, when the same unison attack at the start of the piece would have just sounded like an ordinary chord?
