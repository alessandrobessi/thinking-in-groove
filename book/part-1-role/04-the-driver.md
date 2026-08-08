# The Pedal

*Chapter 4 — Part I, Role: What Is the Bass Responsible For?*

## The Question

How can one bass pitch remain responsible for the floor while the harmony above it keeps changing?

## The Mental Model

A **Pedal** is one sustained or repeated bass pitch beneath changing upper harmony. Its identity is relational: a long C under one C-major chord is merely duration, but C held while the right hand moves through Cmaj7, Fmaj7, and G7 creates a pedal point.

The pedal can stabilize the phrase or accumulate tension. Consonant upper chords confirm its authority; less compatible chords make the unchanged bass increasingly charged. The essential decision is not "play a long note," but "refuse to move while the harmony moves."

The tension isn't the bass note clashing with the chord above it — it's the bass note refusing to let a chord that wants to resolve actually resolve. G7/C doesn't sound wrong; it sounds like a dominant seventh being held open past the point where the ear expects it to move, because the note it's straining toward is already sounding underneath it. This is also why a tonic pedal and a dominant pedal aren't the same device wearing different labels. A tonic pedal does double duty: it grounds the tonic chords it agrees with and creates tension under everything else, so the phrase alternates between stability and pull. A dominant pedal never grounds anything — it's built entirely from the note the harmony is supposed to be leaving, which is exactly why film and theater scores reach for a held dominant (or a tritone) to manufacture suspense that never actually settles until the pedal itself finally moves.

This is the sustained extreme of what Chapters 1 through 3 already established: a bass note's Role depends on its relationship to the harmony above it, not on how long it lasts. The next chapter looks at the same device from the opposite angle — instead of one bass note holding still while several chords pass over it, the Reframer asks what a single change of bass note does to one fixed upper structure's identity, at a single instant rather than across a whole phrase.

## The Microscope

The right hand, chord sequence, rhythm, tempo, and register are identical. A follows every chord with its root. B keeps C beneath all four chords, turning the middle sonorities into Fmaj7/C and G7/C.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="pedal-lab">
  <div class="comparison-controls" aria-label="Moving roots and tonic pedal comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Moving roots</button>
    <button type="button" data-version="B" aria-pressed="false">B — C pedal</button>
  </div>
  <div class="comparison-panel" data-version="A"><div class="score-example" id="pedal-moving-roots">
    <p class="abc-caption"><strong>A — Moving roots.</strong> The floor changes with every chord.</p>
    <p class="abc-description">Cmaj7, Fmaj7, G7, and Cmaj7 with their roots in the bass.</p>
    <pre class="abc-source">X:1
T:The Pedal — moving roots
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=84
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Fmaj7"[EFAc]8 | "G7"[DFGB]8 | "Cmaj7"[EGBc]8 |]
[V:LH] "^follow roots"C,8 | F,,8 | G,,8 | C,8 |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
  <div class="comparison-panel" data-version="B" hidden><div class="score-example" id="pedal-fixed-c">
    <p class="abc-caption"><strong>B — C pedal.</strong> The harmony moves while the floor refuses.</p>
    <p class="abc-description">The sounded right hand is unchanged; a sustained C creates slash-chord tension.</p>
    <pre class="abc-source">X:1
T:The Pedal — fixed C
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=84
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Fmaj7/C"[EFAc]8 | "G7/C"[DFGB]8 | "Cmaj7"[EGBc]8 |]
[V:LH] "^tonic pedal"C,8 | C,8 | "^tension grows"C,8 | "^release"C,8 |]</pre>
    <div class="abc-rendered"></div>
  </div></div>
</div>
```

:::

## Listen

Use **Harmony only** to confirm the upper progression is identical. With **Bass only**, A traces C–F–G–C while B remains on C. In **Full**, listen to how G7/C makes the fixed floor feel charged rather than simply stable.

## See

The chord symbols describe the complete sonority. In B, `/C` does not mean the right hand changed; it records the relationship created by the bass. The repeated annotation marks one continuing responsibility, not four unrelated C notes.

## Play

Hold a tonic pedal beneath four upper harmonies, then repeat the exercise with the dominant as pedal.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="pedal-exercise">
  <p class="abc-caption"><strong>Fixed Floor.</strong> Two bars of tonic pedal followed by two bars of dominant pedal.</p>
  <p class="abc-description">A four-bar exercise comparing the stability and tension of C and G pedal points.</p>
  <pre class="abc-source">X:1
T:Fixed Floor
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=84
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[EGBc]8 | "Fmaj7/C"[EFAc]8 | "Cmaj7/G"[EGBc]8 | "G7"[DFGB]8 |]
[V:LH] "^tonic pedal"C,8 | C,8 | "^dominant pedal"G,,8 | G,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Vary

Keep the entire right hand unchanged and replace the C pedal with G. Which upper chord becomes more stable, and which becomes more tense?

## The Music

“Fixed Star” is an original eight-bar fusion study in 7/8. A repeated low C anchors two four-bar harmonic journeys; the second introduces A-flat major above the pedal, increasing tension before the final return.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="fixed-star-study">
  <p class="abc-caption"><strong>Fixed Star.</strong> Changing upper structures orbit one repeated bass pitch.</p>
  <p class="abc-description">An eight-bar fusion pedal-point study in 7/8 with compact syncopated harmony and monophonic bass.</p>
  <pre class="abc-source">X:1
T:Fixed Star
C:Alessandro Bessi
R:Fusion pedal-point study
M:7/8
L:1/8
Q:1/8=176
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj9"[EGBd]5 z2 | "Fmaj7/C"z2 [EFAc]3 z2 | "G7/C"[DFGB]5 z2 | "Cmaj9"z2 [EGBd]3 z2 | "Abmaj7/C"[_Ac_eg]5 z2 | "Fmaj7/C"z2 [EFAc]3 z2 | "G7/C"[DFGB]5 z2 | "Cmaj9"[EGBd]7 |]
[V:LH] "^repeat the pedal"C,2 z1 C,2 C,2 | C,2 z1 C,2 C,2 | C,2 z1 C,2 C,2 | C,2 z1 C,2 C,2 | "^upper tension"C,2 z1 C,2 C,2 | C,2 z1 C,2 C,2 | C,2 z1 C,2 C,2 | "^settle"C,7 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

At which chord in "Fixed Star" does C stop feeling purely stable and begin to feel like a source of tension—and what in the upper harmony causes that change? The pedal never actually moves anywhere in this study — every bar of tension resolves back to the same held note rather than the bass going somewhere new. Would the piece feel more resolved, or less honest about the tension it built, if the final bar finally let the bass leave C?
