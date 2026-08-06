# The Reframer

*Chapter 5 — Part I, Role: What Is the Bass Responsible For?*

## The Question

How can one bass note make an unchanged upper structure mean something new?

## The Mental Model

A **Reframer** places a bass note beneath an upper structure and changes the harmony listeners infer. The upper notes do not need to move. C–E–G over C sounds like C major; the same C–E–G over A sounds like A minor 7. The bass is not merely adding colour—it is supplying a new harmonic frame.

This differs from an inversion. An inversion reorganizes one chord by placing one of its chord tones in the bass. Reframing can make the combined notes belong to a differently named harmony whose root is supplied from below.

## The Microscope

The right-hand pitches, register, duration, tempo, and dynamics are identical. Only the bass changes. A places C below C–E–G; B places A below it.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="reframer-lab">
  <div class="comparison-controls" aria-label="C floor and A floor comparison">
    <button type="button" data-version="A" aria-pressed="true">A — C floor</button>
    <button type="button" data-version="B" aria-pressed="false">B — A floor</button>
  </div>
  <div class="comparison-panel" data-version="A"><div class="score-example" id="reframer-c-floor">
    <p class="abc-caption"><strong>A — C floor.</strong> C–E–G is heard as C major.</p>
    <p class="abc-description">The bass confirms the root already implied by the upper structure.</p>
    <pre class="abc-source">X:1
T:The Reframer — C floor
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=82
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C"[CEG]8 | [CEG]8 |]
[V:LH] "^confirms C"C,8 | C,8 |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
  <div class="comparison-panel" data-version="B" hidden><div class="score-example" id="reframer-a-floor">
    <p class="abc-caption"><strong>B — A floor.</strong> The same C–E–G becomes A minor 7.</p>
    <p class="abc-description">Nothing in the right hand changes; A supplies a new root and harmonic identity.</p>
    <pre class="abc-source">X:1
T:The Reframer — A floor
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=82
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Am7"[CEG]8 | [CEG]8 |]
[V:LH] "^reframes as Am7"A,,8 | A,,8 |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
</div>
```

:::

## Listen

Choose **Harmony only** in both versions: they are sonically identical. Then choose **Bass only** to isolate the single changed pitch. In **Full**, notice that A does more than darken C major; it makes A feel like the root of a minor-seventh chord.

## See

The right-hand tokens are exactly `[CEG]8` in both scores. The chord symbol changes only because the total sonority changes. The annotation belongs to the bass note because the new frame originates there.

## Play

Keep C–E–G fixed and place four different bass notes beneath it. Name the total sonority after listening, not before.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="reframer-exercise">
  <p class="abc-caption"><strong>One Shape, Four Floors.</strong> C–E–G remains fixed over C, A, F, and G.</p>
  <p class="abc-description">A four-bar exercise in hearing the bass as the source of harmonic context.</p>
  <pre class="abc-source">X:1
T:One Shape, Four Floors
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=82
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C"[CEG]8 | "Am7"[CEG]8 | "Fmaj9(no3)"[CEG]8 | "C/G"[CEG]8 |]
[V:LH] "^ground"C,8 | "^new root"A,,8 | "^new root"F,,8 | "^inversion, not reframe"G,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Replace the A in bar 2 with E. The result is C/E, an inversion of C rather than a newly rooted chord. Explain why A reframes the upper structure but E only reorganizes it.

## The Music

“Borrowed Ceiling” is an original eight-bar jazz-funk study. One syncopated C-major upper shape persists while the bass supplies a sequence of roots and inversions. The first four bars establish the vocabulary; the final four intensify it before C regains the floor.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="borrowed-ceiling-study">
  <p class="abc-caption"><strong>Borrowed Ceiling.</strong> One upper shape, eight changing floors.</p>
  <p class="abc-description">An eight-bar jazz-funk study with fixed right-hand pitch content and a monophonic bass groove.</p>
  <pre class="abc-source">X:1
T:Borrowed Ceiling
C:Alessandro Bessi
R:Jazz-funk reframing study
M:4/4
L:1/8
Q:1/4=94
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C"[CEG]2 z2 [CEG]2 z2 | "Am7"z1 [CEG]2 z1 [CEG]2 z2 | "Fmaj9(no3)"[CEG]2 z2 [CEG]2 z2 | "C/G"z1 [CEG]2 z1 [CEG]2 z2 | "C/E"[CEG]2 z2 [CEG]2 z2 | "D11(no3)"z1 [CEG]2 z1 [CEG]2 z2 | "Cmaj7/B"[CEG]2 z2 [CEG]2 z2 | "C"[CEG]2 z1 [CEG]2 z1 [CEG]2 |]
[V:LH] "^ground"C,2 G,1 z1 C2 G,2 | "^reframe"A,,2 E,1 z1 G,1 A,1 E,2 | "^reframe"F,,2 C,1 z1 E,1 F,1 C,2 | "^inversion"G,,2 D,1 z1 E,1 G,1 C2 | "^inversion"E,2 B,,1 z1 C1 E1 G,2 | "^reframe"D,2 A,,1 z1 C1 D1 G,2 | "^inversion"B,,2 F,1 z1 G,1 B,1 E,2 | "^home"C,2 G,,1 C,1 E,1 G,1 C2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

In “Borrowed Ceiling,” which bass notes create a newly rooted harmony, and which merely invert C major? What evidence do you hear in the unchanged right hand?
