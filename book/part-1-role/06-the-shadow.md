# The Driver

*Chapter 6 — Part I, Role: What Is the Bass Responsible For?*

## The Question

When is the bass responsible for keeping the music moving forward?

## The Mental Model

A **Driver** uses recurring bass activity to create propulsion. The pitches still need to agree with the harmony, but their primary responsibility is kinetic: if the bass stops repeating the figure, the music loses forward pressure.

This is not the same as a Pedal. A Pedal is defined by one pitch persisting while the harmony changes. A Driver may follow every chord and use several pitches; what persists is the activity. It is also possible to drive with relatively few notes. The role describes the effect of the line, not a required note count.

## The Microscope

The harmony, roots, form, tempo, register, and total span are identical. A sustains each root. B restrikes the same root on every eighth note. No new pitch information is added.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="driver-lab">
  <div class="comparison-controls" aria-label="Sustained and repeated roots comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Sustained roots</button>
    <button type="button" data-version="B" aria-pressed="false">B — Repeated roots</button>
  </div>
  <div class="comparison-panel" data-version="A"><div class="score-example" id="driver-sustained-roots">
    <p class="abc-caption"><strong>A — Sustained roots.</strong> The bass identifies each chord without generating repeated motion.</p>
    <p class="abc-description">Four whole-note roots beneath sustained harmony.</p>
    <pre class="abc-source">X:1
T:The Driver — sustained roots
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[FAce]8 | "G7"[DFGB]8 | "Cmaj7"[EGBc]8 | "A7"[^CEGA]8 |]
[V:LH] "^state the floor"D,8 | G,,8 | C,8 | A,,8 |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
  <div class="comparison-panel" data-version="B" hidden><div class="score-example" id="driver-repeated-roots">
    <p class="abc-caption"><strong>B — Repeated roots.</strong> The same harmonic information becomes a motor.</p>
    <p class="abc-description">Only the restrikes change; harmony, bass pitch, and tempo remain controlled.</p>
    <pre class="abc-source">X:1
T:The Driver — repeated roots
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[FAce]8 | "G7"[DFGB]8 | "Cmaj7"[EGBc]8 | "A7"[^CEGA]8 |]
[V:LH] "^create propulsion"D, D, D, D, D, D, D, D, | G,, G,, G,, G,, G,, G,, G,, G,, | C, C, C, C, C, C, C, C, | A,, A,, A,, A,, A,, A,, A,, A,, |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
</div>
```

:::

## Listen

With **Harmony only**, A and B are identical. With **Bass only**, both versions communicate D–G–C–A, but only B creates an unbroken stream of attacks. In **Full**, listen for a change in momentum without a change in tempo.

## See

The repeated notes in B do not add harmonic destinations. Their annotation spans the responsibility of the whole figure: propulsion emerges from recurrence, not from any isolated D, G, C, or A.

## Play

Build a one-bar engine from root, fifth, and octave, then move the same design through a short progression.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="driver-exercise">
  <p class="abc-caption"><strong>Keep It Moving.</strong> One recurring attack pattern follows four roots.</p>
  <p class="abc-description">A four-bar exercise that preserves activity while the harmonic floor changes.</p>
  <pre class="abc-source">X:1
T:Keep It Moving
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm7"[FAce]4 z2 [FAce]2 | "G7"[DFGB]4 z2 [DFGB]2 | "Cmaj7"[EGBc]4 z2 [EGBc]2 | "A7"[^CEGA]4 z2 [^CEGA]2 |]
[V:LH] "^same engine"D,2 A,,1 D,1 z1 D,1 A,,2 | G,,2 D,1 G,1 z1 G,1 D,2 | C,2 G,,1 C,1 z1 C,1 G,,2 | A,,2 E,1 A,1 z1 A,1 E,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Remove the attack on beat 3 from every bar, but change nothing else. Does the line still drive, or has its responsibility shifted toward support? Defend the answer by describing the musical effect rather than counting notes.

## The Music

“Redline” is an original eight-bar funk-fusion study. A recurring bass engine follows D minor, G dominant, C major, and A dominant twice. The second pass alters the final notes of each cell while preserving the forward pull.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="redline-study">
  <p class="abc-caption"><strong>Redline.</strong> A compact bass engine carries two passes through the form.</p>
  <p class="abc-description">An eight-bar funk-fusion study with syncopated chord stabs and monophonic driving bass.</p>
  <pre class="abc-source">X:1
T:Redline
C:Alessandro Bessi
R:Funk-fusion driving study
M:4/4
L:1/8
Q:1/4=102
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Dm9"[FAce]2 z2 [FAce]2 z2 | "G13(no5)"z1 [FABe]2 z1 [FABe]2 z2 | "Cmaj9"[EGBd]2 z2 [EGBd]2 z2 | "A7(b9)"z1 [G_B^c]2 z1 [G_B^c]2 z2 | "Dm9"[FAce]2 z2 [FAce]2 z2 | "G13(no5)"z1 [FABe]2 z1 [FABe]2 z2 | "Cmaj9"[EGBd]2 z2 [EGBd]2 z2 | "A7(b9)"z1 [G_B^c]2 z1 [G_B^c]2 z2 |]
[V:LH] "^engine"D, D, A,, z D, A,, C, D, | G,, G,, D, z G, D, F, G, | C, C, G,, z C, G,, B,, C, | A,, A,, E, z A, E, G, A, | "^controlled change"D, D, A,, z D, C, A,, C, | G,, G,, D, z G, F, D, F, | C, C, G,, z C, B,, G,, B,, | A,, A,, E, z G, E, ^C, A,, |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Which features make “Redline” continue to feel like one engine after the bass cells vary in bars 5–8?
