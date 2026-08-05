# Duration

*Groove Pilot — How Is Motion Organized in Time?*

## The Question

Why can two bass lines with identical attacks and pitches create different grooves?

## The Mental Model

**Duration** is how long a note continues after its attack. Rhythm is not only a list of beginnings: every note also has an ending. A full-value note occupies the grid until the next attack; a shortened note releases early and leaves audible space.

Duration is distinct from attack placement. If two notes begin on beat 2 but one ends on the “and” while the other lasts to beat 3, their attack placement is identical and their duration differs. It is also distinct from touch: notation can specify a written length or articulation, but playback cannot reproduce every physical nuance of a bassist’s release.

## The Microscope

The harmony, right hand, bass pitches, attacks, register, and tempo are identical. A gives every bass note its full quarter-note value. B shortens each to an eighth note and uses the remaining eighth as silence.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="duration-lab">
  <div class="comparison-controls" aria-label="Full-value and shortened duration comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Full value</button>
    <button type="button" data-version="B" aria-pressed="false">B — Shortened</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="duration-full-value">
      <p class="abc-caption"><strong>A — Full value.</strong> Each bass note continues until the next attack.</p>
      <p class="abc-description">Two bars of quarter-note chord tones under sustained Cmaj7 and Am7 harmony.</p>
      <pre class="abc-source">X:1
T:Duration — full value
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 |]
[V:LH] "^full value"C,2 E,2 G,2 B,2 | A,,2 C,2 E,2 G,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="duration-shortened">
      <p class="abc-caption"><strong>B — Shortened.</strong> The attacks stay put, but each note releases halfway to the next one.</p>
      <p class="abc-description">The same notes attack on the same beats, shortened to eighth notes with written rests.</p>
      <pre class="abc-source">X:1
T:Duration — shortened
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 |]
[V:LH] "^short release"C,1 z1 E,1 z1 G,1 z1 B,1 z1 | A,,1 z1 C,1 z1 E,1 z1 G,1 z1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Use **Bass only** to confirm that both versions begin the same pitches on beats 1–4. Then use **Full**: the sustained harmony makes the gaps in B audible without stopping the harmonic context.

## See

A fills each two-eighth-note beat with sound. B divides that same beat into one eighth note and one eighth rest. Nothing has moved earlier or later; only the release point has changed.

## Play

Alternate full and shortened values without changing your attack grid.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="duration-exercise">
  <p class="abc-caption"><strong>Hold and Release.</strong> One attack pattern, four duration treatments.</p>
  <p class="abc-description">A four-bar exercise moving from full values to shortened notes and back.</p>
  <pre class="abc-source">X:1
T:Hold and Release
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Am7"[ACEG]8 | "Dm7"[DFAC]8 | "G7"[DFGB]8 |]
[V:LH] "^full"C,2 E,2 G,2 B,2 | "^short"A,,1 z1 C,1 z1 E,1 z1 G,1 z1 | "^short"D,1 z1 F,1 z1 A,1 z1 C1 z1 | "^full"G,,2 B,,2 D,2 F,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Keep all four attacks in one bar. Lengthen only the final note so it continues into the next harmony. Does that ending connect the bars or blur the change?

## The Music

“Afterimage” is an original eight-bar fusion ballad. Its bass uses a recurring contrast between tones that linger and tones that release early. The right hand continues through the gaps, so every bass ending remains audible as a deliberate part of the groove.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="afterimage-study">
  <p class="abc-caption"><strong>Afterimage.</strong> Long and short releases shape an eight-bar phrase.</p>
  <p class="abc-description">A restrained fusion study with sustained harmony and a monophonic bass duration motif.</p>
  <pre class="abc-source">X:1
T:Afterimage
C:Alessandro Bessi
R:Fusion ballad
M:4/4
L:1/8
Q:1/4=84
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj9"[EGBd]6 z2 | "Am9"[CEGB]8 | "Dm9"[FACe]6 z2 | "G13"[FGBE]8 | "Cmaj9"[EGBd]6 z2 | "Am9"[CEGB]8 | "Dm9"[FACe]6 z2 | "G13"[FGBE]6 "Cmaj9"[EGBd]2 |]
[V:LH] "^linger"C,4 G,2 z2 | "^release"A,,2 z2 E,2 z2 | "^linger"D,6 z2 | "^release"G,,2 z2 B,,2 z2 | "^linger"C,4 B,,2 z2 | "^release"A,,2 z2 E,2 z2 | "^linger"D,4 A,2 z2 | "^connect"G,,2 z2 B,,2 C,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

In “Afterimage,” which bass endings create forward connection, and which create punctuation—even though the attack pattern remains sparse throughout?
