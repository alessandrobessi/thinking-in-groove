# The Inverter

*Chapter 3 — Part I, Role: What Is the Bass Responsible For?*

## The Question

Why can one low note make an unchanged chord feel settled, open, or as if it must keep moving?

## The Mental Model

The bass does more than add weight to a chord. It tells the ear which pitch is the floor. Put C beneath a C-major voicing and the sonority is in root position. Put E beneath that same voicing and it becomes C/E, a first inversion. Put G beneath it and it becomes C/G, a less settled second inversion.

An **Inverter** is a non-root chord tone in the bass that reorganizes a familiar harmony. The upper notes need not change. What changes is their relationship to the lowest note—and therefore the harmony's balance and direction.

This is not merely colour. E below C major changes the inversion. G changes it again. B beneath the notes C, E, and G does something stronger: the upper structure now sounds like Cmaj7/B, an unstable sonority that invites stepwise motion. A bass note should be named by what it makes the whole sonority do.

## The Microscope

The right hand, rhythm, register, tempo, and phrase length are identical in A and B. Only the bass changes: C in A, E in B.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="inverter-lab">
  <div class="comparison-controls" aria-label="Root position and first inversion comparison">
    <button type="button" data-version="A" aria-pressed="true">A — C root</button>
    <button type="button" data-version="B" aria-pressed="false">B — E bass</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="inverter-lab-root">
      <p class="abc-caption"><strong>A — Root position.</strong> C is both the chord root and the lowest note.</p>
      <p class="abc-description">Two bars of repeated C-major right-hand chords over a sustained low C.</p>
      <pre class="abc-source">X:1
T:The Inverter — root position
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C"[CEG]4 [CEG]4 | "C"[CEG]4 [CEG]4 |]
[V:LH] "^Root: grounded"C,8 | C,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="inverter-lab-first-inversion">
      <p class="abc-caption"><strong>B — First inversion.</strong> The same upper harmony now balances over E.</p>
      <p class="abc-description">The right hand is unchanged; a sustained low E turns C major into C over E.</p>
      <pre class="abc-source">X:1
T:The Inverter — first inversion
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C/E"[CEG]4 [CEG]4 | "C/E"[CEG]4 [CEG]4 |]
[V:LH] "^Third in bass: lift"E,8 | E,8 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

First use **Harmony only** on both versions: it should sound identical. Then use **Full** and switch A/B. Finally use **Bass only** to identify the single controlled difference.

## See

The chord symbol names the whole result, not just the right hand. In A, `C` says that C major has C in the bass. In B, `C/E` says that the same chord has E in the bass. The annotation is attached to the bass because that single decision produces the inversion.

The notation shows written pitch, attack, and duration. Playback is a reference performance; it does not prove subtle pocket, touch, or microtiming.

## Play

Play this four-bar laboratory at the piano, as bass beneath a partner, or by recording the right hand first. Keep the upper voicing unchanged while the bass moves through four interpretations.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="inverter-exercise">
  <p class="abc-caption"><strong>Four floors.</strong> Root, first inversion, second inversion, then directed instability.</p>
  <p class="abc-description">A repeated C-major voicing sounds above bass notes C, E, G, and B, one per bar.</p>
  <pre class="abc-source">X:1
T:Four Floors
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "C"[CEG]4 [CEG]4 | "C/E"[CEG]4 [CEG]4 | "C/G"[CEG]4 [CEG]4 | "Cmaj7/B"[CEG]4 [CEG]4 |]
[V:LH] "^root"C,8 | "^first inversion"E,8 | "^second inversion"G,8 | "^directed tension"B,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Notice that B is a chord tone of Cmaj7, but the voicing above contains only the C-major triad. Calling the result “colour” would miss its directed pull toward C.

## Vary

Preserve the right-hand notes, rhythm, tempo, and register. Change only the final bass note from B to G. Which version asks more strongly for another bar, and where does each version want to go?

## The Music

“Glass Stairs” is an original eight-bar fusion ballad. Its right hand keeps a compact rhythmic identity while the bass uses inversions to turn a simple harmonic loop into a continuous line. The lower staff remains monophonic and lies in a practical bass register.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="glass-stairs-study">
  <p class="abc-caption"><strong>Glass Stairs.</strong> Eight bars; inversions create the descending path C–B–A–G, then F–E–D–G.</p>
  <p class="abc-description">A sparse fusion ballad for harmony and monophonic bass. Slash chords make the bass route explicit.</p>
  <pre class="abc-source">X:1
T:Glass Stairs
C:Alessandro Bessi
R:Fusion ballad
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj9"[EGBd]6 z2 | "G/B"[DGB]4 z2 [DGB]2 | "Am9"[CEGB]6 z2 | "C/G"[CEG]4 z4 |
"Fmaj9"[EFAc]6 z2 | "C/E"[CEG]4 z2 [CEG]2 | "Dm9"[FACe]6 z2 | "G13"[FGBE]4 z2 [FGBD]2 |]
[V:LH] "^ground"C,4 G,2 C2 | "^invert: descend"B,6 D2 | "^arrive"A,4 E2 G2 | "^invert: open"G,6 z2 |
"^new ground"F,4 C2 E2 | "^invert: continue"E,6 G2 | "^prepare"D,4 A,2 C2 | "^dominant: return"G,6 z2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Practise the bass alone until its contour feels like one sentence. Then play the harmony alone and notice its separate rhythm. In full playback, listen for bars 2, 4, and 6: the slash chords are not exceptions but the steps that make the phrase cohere.

## Reflection

If the right-hand voicing never changes, at what point does a new bass note stop sounding like a different view of the same chord and start sounding like a new harmonic destination?
