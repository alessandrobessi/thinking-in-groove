# Functional Jazz Progression

*Chapter 37 — Part V, Design: Building Complete Bass Lines. Destinations and voice leading organize moving harmony.*

## The Question

When the chord changes every bar or two, what does the bass actually need to prioritize that a static vamp never had to worry about?

## The Mental Model

A **Functional Jazz Progression** sits at the opposite end of Harmonic Rhythm from the previous chapter's static vamp: the chord changes often enough that where the bass is *going* becomes the dominant design question. Groove decisions don't disappear, but they stop doing most of the work — Motion does. Each new chord is a destination, and the bass's job is to organize the space leading into it: a chromatic Approach Note, a diatonic step, an Enclosing figure surrounding the target from both sides, a stepwise Connecting line — all of this Part II vocabulary exists precisely for this situation.

The common error under fast harmonic rhythm isn't playing a wrong note — every chord root is, by definition, correct under its own chord. It's playing correct roots with no voice leading between them: leaping registers at random from one right answer to the next, rather than treating each arrival as a destination the previous note was actually organized around. A progression built entirely from disconnected correct roots can be harmonically flawless and still fail to feel like it's going anywhere.

## The Microscope

Both panels play the same four-chord progression, root correct on every chord. Only how the bass gets from one root to the next differs.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="jazz-progression-lab">
  <div class="comparison-controls" aria-label="Functional Jazz Progression comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Voice-led</button>
    <button type="button" data-version="B" aria-pressed="false">B — Disjunct roots</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="jazz-progression-voice-led">
      <p class="abc-caption"><strong>A — Voice-led destinations.</strong> Every chord after the first is approached from a half-step or whole-step away.</p>
      <p class="abc-description">A Dm7-G7-Cmaj7-Am7 progression with a chromatic or diatonic approach note leading into each new root.</p>
      <pre class="abc-source">X:1
T:Functional Jazz Progression — voice-led destinations
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 | "Am7"[ace]8 |]
[V:LH] "^ground"D,,8 | "^approach"F,,2 ^F,,2 G,,4 | "^approach"B,,4 C,,4 | "^approach"B,,4 A,,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="jazz-progression-disjunct-roots">
      <p class="abc-caption"><strong>B — Disjunct roots.</strong> Every root is correct; two of them arrive by an unprepared octave leap.</p>
      <p class="abc-description">The identical progression with plain roots, two of which jump a full octave and more from the previous note.</p>
      <pre class="abc-source">X:1
T:Functional Jazz Progression — disjunct roots
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 | "Am7"[ace]8 |]
[V:LH] D,,8 | "^leap"g8 | C,,8 | "^leap"a8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and notice how each new chord feels prepared — you can hear the bass leaning toward the destination before it arrives. Play **Full** on B: every root is unmistakably correct, and yet the line lurches unpredictably from register to register, because nothing before each arrival organized the listener's ear toward it.

## See

In A, bar two's `"^approach"` tag covers a half-step climb into G (`F,, ^F,, G,,`); bar three and four each spend half the bar stepping into their target from a neighbor tone. In B, the same targets (G and A) are simply restated an octave higher than the previous note (`g`, `a`), tagged `"^leap"` — technically the correct pitch class, reached with no preparation at all.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="jazz-progression-two-chords">
  <p class="abc-caption"><strong>Approach the Destination.</strong> Practice a chromatic approach note leading into a new chord's root.</p>
  <p class="abc-description">A held Dm7 root followed by a chromatic climb into G7's root.</p>
  <pre class="abc-source">X:1
T:Approach the Destination
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=100
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

Play the approach and listen for the moment the destination becomes audible before you've actually played it — that anticipation is the entire function of an approach note. Then play the same two bars with the second bar's root alone, no approach, and compare how much less inevitable the arrival feels.

## Vary

Take "Approach the Destination" and replace the chromatic approach with a diatonic one — a whole step instead of a half step into G. Does the destination still feel prepared, or does the chromatic version specifically carry a stronger pull? What does that tell you about why Approach Notes and Enclosing figures are separate entries in this book's vocabulary rather than one term?

## The Music

"Four Destinations" is an eight-bar jazz study cycling through Dm7-G7-Cmaj7-Am7 twice, using a different voice-leading device to arrive at every single chord: a chromatic approach, a diatonic approach from below, an approach from above, a two-sided enclosure, a stepwise connecting run, and a final held resolution — every bar organized entirely around where it's headed next.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="four-destinations-study">
  <p class="abc-caption"><strong>Four Destinations.</strong> Eight bars, six different ways of preparing an arrival.</p>
  <p class="abc-description">An eight-bar jazz study cycling twice through Dm7, G7, Cmaj7, and Am7, voice-leading into every chord.</p>
  <pre class="abc-source">X:1
T:Four Destinations
C:Alessandro Bessi
R:Jazz study
M:4/4
L:1/8
Q:1/4=104
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 | "Am7"[ace]8 |
"Dm7"[dfa]8 | "G7"[gbd]8 | "Cmaj7"[ceg]8 | "Am7"[ace]8 |]
[V:LH] "^ground"D,,8 | "^approach"F,,2 ^F,,2 G,,4 | "^approach"B,,4 C,,4 | "^approach"B,,4 A,,4 |
"^enclose"E,,2 ^C,,2 D,,4 | "^connect"D,,2 E,,2 F,,2 G,,2 | "^approach"B,,4 C,,4 | "^resolve"A,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

The previous chapter's static vamp got almost all of its interest from Groove; "Four Destinations" gets almost all of its interest from Motion, and its Groove is nearly uniform throughout. If you had to design a bass line over harmony that changes at a moderate, in-between rate — not static, not moving every bar — how would you decide how much weight to give each layer?
