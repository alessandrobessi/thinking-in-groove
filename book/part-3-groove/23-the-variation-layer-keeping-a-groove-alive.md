# Variation Without Collapse

*Chapter 25 — Part III, Groove: How Is Motion Organized in Time?*

## The Question

How much can you change about a groove before it stops being recognizably the same groove?

## The Mental Model

**Variation Without Collapse** changes exactly one parameter of a Repeated Cell (Chapter 24) while leaving enough of it intact for the identity to survive. Displace the attack by an eighth, substitute one pitch, add one ornamental note — any one of these, alone, and a listener can still hear "the same cell, varied."

Change more than one parameter at once — rhythm and register and pitch together — and the result stops reading as a variation. It becomes a new cell, indistinguishable in kind from just switching grooves outright. That's the "collapse" in the term's name: not that anything breaks technically, but that the identity the cell was carrying doesn't survive the accumulation of changes.

The one-parameter rule isn't arbitrary caution — it's about how much redundancy a listener's recognition needs. A cell's identity is carried by several cues at once: its rhythm, its register, its contour, its specific pitches. Changing one of those cues still leaves the rest intact for the ear to anchor on, which is why Panel A still reads as "the same cell" even though something audibly moved. Changing several at once removes multiple anchors simultaneously, faster than recognition can keep up, and there's nothing left to confirm the identity against. This chapter operates bar to bar; the next asks the same question at a larger scale — how much a groove's behavior can shift across a two-, four-, or eight-bar span and still read as one coherent phrase rather than several unrelated ones.

## The Microscope

Both bars start from the identical cell. Only how much changes in bar 2 differs.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="variation-lab">
  <div class="comparison-controls" aria-label="Variation Without Collapse comparison">
    <button type="button" data-version="A" aria-pressed="true">A — One change</button>
    <button type="button" data-version="B" aria-pressed="false">B — Collapse</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="variation-without-collapse-displaced">
      <p class="abc-caption"><strong>A — One parameter changes.</strong> The cell shifts an eighth-note later; nothing else about it moves.</p>
      <p class="abc-description">Two bars: the established cell, then the same cell displaced by one eighth note.</p>
      <pre class="abc-source">X:1
T:Variation Without Collapse — one parameter changes
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^displaced -- one parameter changed"z1 C,2 z2 C,2 C,1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="variation-without-collapse-collapsed">
      <p class="abc-caption"><strong>B — Collapse.</strong> Register and rhythm both change at once; the identity doesn't survive.</p>
      <p class="abc-description">Two bars: the established cell, then a bar that shares no recognizable rhythm or register with it.</p>
      <pre class="abc-source">X:1
T:Variation Without Collapse — everything changes at once
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^register and rhythm both changed -- collapse"c4 z2 c1 c1 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Bass only** on both. A's second bar is obviously related to its first — the ear tracks it as one groove breathing. B's second bar could belong to an entirely different piece; nothing about it points back to bar 1.

## See

In A, three of the cell's four rhythmic values are untouched — only the starting position shifted. In B, register jumped an octave and the rhythm's proportions changed completely. Counting how many parameters moved is a reliable way to predict, before you even listen, whether a variation will collapse.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="variation-without-collapse-one-change-at-a-time">
  <p class="abc-caption"><strong>One Change at a Time.</strong> The same cell, varied by substitution, then by ornament.</p>
  <p class="abc-description">Three bars: the cell, a one-note pitch substitution, and a one-note ornamental addition.</p>
  <pre class="abc-source">X:1
T:One Change at a Time
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=96
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 | "Cmaj7"[CEGB]8 |]
[V:LH] "^cell"C,2 z2 C,2 C,2 | "^substituted"C,2 z2 E,2 C,2 | "^ornamented"C,1 D,1 z2 C,2 C,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play all three bars back to back and identify, out loud, exactly which single parameter changed in bar 2 and which single parameter changed in bar 3. If you can't name the one thing that moved, you've likely changed more than one without noticing.

## Vary

Take bar 3's ornamented cell and add a second, independent change on top of it — a register jump, say. Does the cell survive two simultaneous changes, or does this specific combination already start to feel like collapse?

## The Music

"Same Bones" is an original eight-bar jazz-funk study in G natural minor, swung: one cell, varied by a different single parameter every two bars, always returning to the plain cell by the end.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="same-bones-study">
  <p class="abc-caption"><strong>Same Bones.</strong> Displacement, substitution, and ornament, each applied once, never combined.</p>
  <p class="abc-description">A swung eight-bar jazz-funk study in G natural minor: the cell, displaced, restated, substituted, restated, ornamented, then returned to plain.</p>
  <pre class="abc-source">X:1
T:Same Bones
C:Alessandro Bessi
R:Jazz-funk study
M:4/4
L:1/8
Q:1/4=98
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gm7"[g_bd'f']8 | "Gm7"[g_bd'f']8 | "Ebmaj7"[_eg_bd']8 | "Ebmaj7"[_eg_bd']8 |
"Fmaj7"[fac'e']8 | "Fmaj7"[fac'e']8 | "Cm7"[c_eg_b]8 | "Cm7"[c_eg_b]8 |]
[V:LH] "^cell"G,2 z2 G,>G, | "^displaced"z1 G,2 z2 G,2 G,1 | "^cell"_E,2 z2 _E,>_E, | "^substituted"_E,2 z2 _B,>_E, |
"^cell"F,2 z2 F,>F, | "^ornamented"F,1 G,1 z2 F,>F, | "^cell"C,2 z2 C,>C, | "^cell: return"C,2 z2 C,>C, |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

## Reflection

"Same Bones" never combines two variation types in the same bar. Pick two of its individual variations (displacement, substitution, ornament) and predict, before trying it, whether combining them in one bar would still count as a single "one-parameter" change or would tip into collapse.
