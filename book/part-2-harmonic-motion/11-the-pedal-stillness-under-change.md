# Staying

*Chapter 9 — Part II, Motion: How Does the Bass Travel?*

## The Question

What does it mean for the bass to choose not to move, even when the harmony would let it?

## The Mental Model

Motion is not only about where the bass goes — it's also about the choice to go nowhere. **Staying** is that choice made deliberately: the bass holds its ground across a span of music, functioning as a real motion decision, not the absence of one.

Staying is easy to confuse with a Pedal (Chapter 4), because both look identical on the page: one note, held or repeated. The difference is what happens *above* the bass while it holds. A Pedal requires the harmony to change while the note persists — that's what generates its characteristic tension. Staying requires no such change: the bass holds because the harmony isn't asking it to do anything else. The same physical note, held the same way, is Staying under one unchanging chord and a Pedal the instant the chord above it starts to move.

The common error runs in the opposite direction from what you might expect: it isn't mistaking a Pedal for Staying, it's assuming a held note is automatically doing nothing simply because it isn't a Pedal. Staying is still a Motion decision — the bass had chord tones, neighboring notes, and passing options available and declined all of them, on purpose, because the moment didn't call for travel. The rest of this Part is going to hand the bass increasingly elaborate ways to travel between harmonic destinations — Stepping, Approaching, Enclosing, Arpeggiating, Leaping. Staying is what all of that motion is measured against: without a real, deliberate choice to hold still, "the bass moved" stops meaning anything in particular.

## The Microscope

The bass plays the identical note both times. Only the harmony above it changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="staying-lab">
  <div class="comparison-controls" aria-label="Staying comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Staying</button>
    <button type="button" data-version="B" aria-pressed="false">B — Becomes a Pedal</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="staying-static">
      <p class="abc-caption"><strong>A — Staying.</strong> The chord never changes, so the held bass note is simply staying.</p>
      <p class="abc-description">Two bars of an unchanging Cm triad over a held bass C.</p>
      <pre class="abc-source">X:1
T:Staying — static harmony
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:Cm
[V:RH] "Cm"[C_EG]4 [C_EG]4 | "Cm"[C_EG]4 [C_EG]4 |]
[V:LH] "^stay"C,4 C,4 | "^stay"C,4 C,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="staying-pedal">
      <p class="abc-caption"><strong>B — The same choice, now a Pedal.</strong> The chord moves to Fm while the bass note refuses to follow.</p>
      <p class="abc-description">The identical held bass C, now under a chord change from Cm to Fm.</p>
      <pre class="abc-source">X:1
T:Staying — becomes a pedal
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:Cm
[V:RH] "Cm"[C_EG]4 [C_EG]4 | "Fm"[F_Ac]4 [F_Ac]4 |]
[V:LH] "^stay"C,4 C,4 | "^pedal: same note, harmony moved"C,4 C,4 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Hear **Harmony only** first on both versions: A holds one chord throughout; B changes chord in bar 2. Now hear **Full**. The bass note is identical in both — same pitch, same rhythm, same touch. What changed is entirely above it, yet that change is what turns a resting note into a taut one.

## See

Nothing in the bass staff itself distinguishes Staying from a Pedal — the annotation must reference the harmony above to tell them apart. This is a reminder that Motion terms are relationships, not properties of a single staff read in isolation.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="staying-hold-the-floor">
  <p class="abc-caption"><strong>Hold the Floor.</strong> The same held note plays two different roles across four bars.</p>
  <p class="abc-description">A held C under two bars of Cmaj7, one bar of Fmaj7, and a final released bar.</p>
  <pre class="abc-source">X:1
T:Hold the Floor
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 | "Fmaj7"[FAce]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^stay"C,8 | "^stay"C,8 | "^stay: now a pedal"C,8 | "^released"C,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Hold the bass note through all four bars without rearticulating it if your instrument allows it. Notice the exact bar where your held note stops being passive and starts creating tension — it's bar 3, the moment the chord above moves and you don't.

## Vary

Keep the bass note and its rhythm identical. Change only bar 3's chord from Fmaj7 to Abmaj7. Does the tension change in kind, or only in color? What does that tell you about what a Pedal actually depends on — the specific chord, or simply the fact that a chord changes at all?

## The Music

"Low Tide" is an original eight-bar funk study. Six bars stay on one chord before the harmony finally moves in bar 7 — proof that staying is not the same as having nothing to say.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="low-tide-study">
  <p class="abc-caption"><strong>Low Tide.</strong> Six bars of held ground, then a brief departure before the loop restarts.</p>
  <p class="abc-description">An eight-bar funk study: six bars on Cm, a move through Ab, and a G that resolves back to the top.</p>
  <pre class="abc-source">X:1
T:Low Tide
C:Alessandro Bessi
R:Funk study
M:4/4
L:1/8
Q:1/4=90
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:Cm
[V:RH] "Cm"z2 [C_EG]2 z2 [C_EG]2 | z [C_EG]2 z [C_EG]2 z2 | "Cm"z2 [C_EG]2 z2 [C_EG]2 | z [C_EG]2 z [C_EG]2 z2 |
"Cm"z2 [C_EG]2 z2 [C_EG]2 | z [C_EG]2 z [C_EG]2 z2 | "Ab"z2 [_Ac_e]2 z2 [_Ac_e]2 | "G"z [GBd]2 z [GBd]2 z2 |]
[V:LH] "^stay"C,4 z C,2 z | "^stay"C,4 z C,2 z | "^stay"C,4 z C,2 z | "^stay"C,4 z C,2 z |
"^stay"C,4 z C,2 z | "^stay"C,4 z C,2 z | "^leave"_A,,4 z _A,,2 z | "^stay ends"G,,8 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

Six of "Low Tide"'s eight bars stay on the same chord. Does the bass line feel static for six bars, or does something else keep it interesting while the harmony holds still? The bass note itself never changes pitch during those six bars — only its rhythm varies slightly from bar to bar. If even the rhythm had been frozen identically bar after bar, would "staying" have tipped over into simply sounding unplanned?
