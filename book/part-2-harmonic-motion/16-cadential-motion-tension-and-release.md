# Contrary Motion

*Chapter 16 — Part II, Motion: How Does the Bass Travel?*

## The Question

What happens when the bass travels one way while the upper voice travels the other?

## The Mental Model

**Contrary motion** means that two voices move in opposite directions: one rises while the other falls. It is a relationship between lines, not a special kind of bass note. The piano grand staff makes that relationship visible and audible at once.

Contrary motion can widen the musical space, keep inner voices independent, and turn a chord progression into a coordinated gesture. It does not require chromatic notes or new harmony. The bass can often create it by choosing chord-tone inversions instead of roots.

Two mechanisms are doing the work here, and it's worth separating them. First, the registral one: when the bass falls as the top voice rises, the total distance between the outermost notes grows every bar, and a widening span simply occupies more of the ear's available pitch space — the texture reads as opening up because it literally is. Second, the independence one: opposite directions are the strongest possible signal that two voices are genuinely separate lines rather than one idea doubled at a distance. Compare this to the most extreme opposite case a later chapter examines — a bass line doubling the melody note for note, in unison — where identical direction fuses two voices into what the ear hears as one thicker event. Contrary motion is that fusion's mirror image: maximum independence instead of maximum unity, using nothing more exotic than which chord tone the bass happens to stand on.

## The Microscope

The right hand, harmony, rhythm, tempo, and register are identical in A and B. Its top note rises B–C–D–F. A uses roots in the bass. B chooses chord tones that descend E–C–A–G, creating a clear contrary line.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="contrary-motion-lab">
  <div class="comparison-controls" aria-label="Root path and contrary-motion path comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Root path</button>
    <button type="button" data-version="B" aria-pressed="false">B — Contrary path</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="contrary-root-path">
      <p class="abc-caption"><strong>A — Root path.</strong> The bass identifies each chord but does not form a single opposing contour.</p>
      <p class="abc-description">An ascending right-hand top voice over root-position Cmaj7, Am7, Dm7, and G7.</p>
      <pre class="abc-source">X:1
T:Contrary Motion — root path
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGB]8 | "Am7"[EGAc]8 | "Dm7"[FAd]8 | "G7"[DFBf]8 |]
[V:LH] "^root"C,8 | "^root"A,,8 | "^root"D,8 | "^root"G,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="contrary-descending-path">
      <p class="abc-caption"><strong>B — Contrary path.</strong> The bass descends E–C–A–G while the upper voice rises.</p>
      <p class="abc-description">The sounded right hand is unchanged; chord-tone bass inversions create the opposing contour.</p>
      <pre class="abc-source">X:1
T:Contrary Motion — descending path
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7/E"[EGB]8 | "Am7/C"[EGAc]8 | "Dm7/A"[FAd]8 | "G7"[DFBf]8 |]
[V:LH] "^begin descent"E,8 | "^opposite"C,8 | "^continue"A,,8 | "^arrive"G,,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Use **Harmony only** to learn the rising top line. Use **Bass only** to hear the two lower routes. In **Full**, B should sound like one expanding gesture rather than two unrelated melodies.

## See

Follow only the outermost notes. In B, the upper endpoints climb while the bass endpoints fall. The inner chord tones support the harmony, but they are not the concept under examination.

## Play

Play the four-bar contrary path, then exchange directions: make the right-hand top note descend while the bass rises through chord tones.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="contrary-motion-exercise">
  <p class="abc-caption"><strong>Opening and closing.</strong> Two bars widen, then two bars contract.</p>
  <p class="abc-description">A four-bar exercise pairing ascending and descending outer voices over chord-tone bass notes.</p>
  <pre class="abc-source">X:1
T:Opening and Closing
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7/E"[EGB]4 "Am7/C"[EGAc]4 | "Dm7/A"[FAd]4 "G7"[DFBf]4 | "Fmaj7"[FAce]4 "G7"[FGBd]4 | "Am7"[EGAc]4 "G7/B"[DFGB]4 |]
[V:LH] "^fall"E,4 C,4 | A,,4 G,,4 | "^rise"F,,4 G,,4 | A,,4 B,,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Keep every chord and the entire right hand unchanged. Replace only one bass inversion with its root. Which break in the descending contour is most noticeable?

## The Music

“Crossing Lines” is an original eight-bar fusion study in D major, in 7/8. The first phrase opens as the upper voice rises and the bass falls; the second closes as those directions reverse. A repeated short–long chord rhythm gives the two contours a shared pulse.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="crossing-lines-study">
  <p class="abc-caption"><strong>Crossing Lines.</strong> Opposing contours shape two four-bar phrases.</p>
  <p class="abc-description">An eight-bar fusion miniature in D major, in 7/8, with syncopated piano voicings and monophonic chord-tone bass.</p>
  <pre class="abc-source">X:1
T:Crossing Lines
C:Alessandro Bessi
R:Fusion study
M:7/8
L:1/8
Q:1/8=184
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dmaj7/F#"[^FA^c]3 z1 [^FA^c]2 z1 | "Bm7/D"[^FABd]3 z1 [^FABd]2 z1 | "Em7/B"[GBe]3 z1 [GBe]2 z1 | "A7"[EG^cg]3 z1 [EG^cg]2 z1 | "Gmaj7"[GBd^f]3 z1 [GBd^f]2 z1 | "A7"[GA^ce]3 z1 [GA^ce]2 z1 | "Bm7"[^FABd]3 z1 [^FABd]2 z1 | "A7/C#"[EGA^c]3 z1 [EGA^c]2 z1 |]
[V:LH] "^open: bass falls"^F,2 z1 ^F,2 ^F,2 | D,2 z1 D,2 D,2 | B,,2 z1 B,,2 B,,2 | A,,2 z1 A,,2 A,,2 | "^close: bass rises"G,,2 z1 G,,2 G,,2 | A,,2 z1 A,,2 A,,2 | B,,2 z1 B,,2 B,,2 | ^C,2 z1 ^C,2 ^C,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

When the outer voices move apart, does the phrase feel more open because of the register, the harmonic inversions, or the coordinated direction—and how could you test those causes separately?
