# Doubling

*Chapter 28 — Part IV, Interaction: What Happens Between Bass and Harmony? Opens the Part: the bass reinforces a pitch actually stated in the upper voice.*

## The Question

When the bass and the right hand land on the same pitch class, has the bass "doubled" anything — or did the two lines just happen to cross?

## The Mental Model

**Doubling** means the bass reinforces a pitch or line that the upper voice actually states, in unison or at the octave. The bass isn't just present under the harmony — it's tracking specific melodic content the right hand is playing right now.

This is a claim about relationship, not coincidence. A single shared note, surrounded by otherwise unrelated lines, proves nothing: the two voices could have landed on the same pitch class by chance while going about independent business. Doubling requires the bass to follow the upper voice's actual contour — enough of it that a listener can hear one line being reinforced, not two lines briefly touching.

The common error is calling any shared pitch class "doubling" without checking whether the bass is actually tracking the line above it. A bass note that matches the melody's pitch class on beat one, then diverges completely, hasn't doubled anything — it has coincided with it once.

## The Microscope

Both panels open on the identical shared pitch. Only one of them keeps tracking.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="doubling-lab">
  <div class="comparison-controls" aria-label="Doubling comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Doubling</button>
    <button type="button" data-version="B" aria-pressed="false">B — Coincidental unison</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="doubling-tracks-the-melody">
      <p class="abc-caption"><strong>A — The bass tracks the melody.</strong> Every bass note matches the right hand's contour, two octaves below.</p>
      <p class="abc-description">A one-bar Cmaj7 melody doubled exactly at the double octave.</p>
      <pre class="abc-source">X:1
T:Doubling — the bass tracks the melody
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"C2 D2 E2 D2 |]
[V:LH] "^double"C,,2 D,,2 E,,2 D,,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="doubling-coincidental-unison">
      <p class="abc-caption"><strong>B — A coincidental unison.</strong> The bass shares its first pitch class with the melody, then moves on its own business.</p>
      <p class="abc-description">The identical right-hand melody over an unrelated left-hand contour that only touches it once.</p>
      <pre class="abc-source">X:1
T:Doubling — a coincidental unison
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"C2 D2 E2 D2 |]
[V:LH] "^coincidental"G,,2 C,,2 F,,2 A,,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and notice how the bass reads as an echo of the melody, an octave register below it — one idea, stated twice. Play **Full** on B: the opening pitch class lines up, but nothing else does, and the ear stops hearing a relationship after the first beat.

## See

In A, every bass attack matches the melody's letter name, offset by two octaves — `C,, D,, E,, D,,` under `C D E D`. In B, only the first note matches; `C,, F,, A,,` after it belongs to a different, unrelated shape. The label under each staff names exactly what's happening: `"^double"` versus `"^coincidental"`.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="doubling-track-the-line">
  <p class="abc-caption"><strong>Track the Line.</strong> Practice locking the bass to a stated upper-voice contour across two chords.</p>
  <p class="abc-description">Two bars of bass doubling a right-hand melody two octaves below, first over Am7, then over Dm7.</p>
  <pre class="abc-source">X:1
T:Track the Line
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=92
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"A2 c2 B2 A2 | "Dm7"D2 F2 E2 D2 |]
[V:LH] "^double"A,,2 c,2 B,,2 A,,2 | "^double"D,,2 F,,2 E,,2 D,,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play both bars, listening for the moment your left hand stops feeling like an accompaniment and starts feeling like the same line, restated. Then play only the right hand, then only the left — confirm the left hand is a legitimate melody on its own, not just a shadow that only makes sense underneath the other staff.

## Vary

Take bar one of "Track the Line" and change a single left-hand note so it no longer matches the right hand's contour at that beat. Has it become Coincidental Unison, or something else entirely? What's the fewest notes you can change before a listener stops hearing "doubling" at all?

## The Music

"Same Voice" is an eight-bar jazz-funk study built from two contrasting bass behaviors under the same four-chord progression: on the first bar of each chord the bass doubles the right hand's melodic figure two octaves below; on the second bar it drops to a plain sustained root. The alternation is the point — doubling reads as a deliberate event only because the bass doesn't do it constantly.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="same-voice-study">
  <p class="abc-caption"><strong>Same Voice.</strong> Doubling alternates with plain roots so the doubled bars stand out as a choice, not a habit.</p>
  <p class="abc-description">An eight-bar jazz-funk study over Cmaj7, Am7, Dm7, and G7, pairing one doubled bar with one root-only bar per chord.</p>
  <pre class="abc-source">X:1
T:Same Voice
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/4
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"C E G E | E G E C | "Am7"A C E C | E C A C |
"Dm7"D F A F | A F D F | "G7"G B d B | d B G G |]
[V:LH] "^double"C,, E,, G,, E,, | "^root"C,,4 | "^double"A,, C,, E,, C,, | "^root"A,,4 |
"^double"D,, F,, A,, F,, | "^root"D,,4 | "^double"G,, B,, D, B,, | "^resolve"G,,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Every doubled bar in "Same Voice" shares its entire contour with the right hand; every root-only bar shares none of it. Where would you place a bass line that doubles just the first two notes of a four-note figure, then breaks off — is that closer to Doubling or to Independence, the next chapter's subject?
