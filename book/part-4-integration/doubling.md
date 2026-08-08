# Doubling

*Chapter 28 — Part IV, Interaction: What Happens Between Bass and Harmony? Opens the Part: the bass reinforces a pitch actually stated in the upper voice.*

## The Question

When the bass and the right hand land on the same pitch class, has the bass "doubled" anything — or did the two lines just happen to cross?

## The Mental Model

**Doubling** means the bass reinforces a pitch or line that the upper voice actually states, in unison or at the octave. The bass isn't just present under the harmony — it's tracking specific melodic content the right hand is playing right now.

Doubling isn't a decoration; it's a decision about weight. Two instruments stating the identical contour don't just get louder together — their attacks lock, their overtones reinforce each other, and the ear tends to fuse the pair into a single, thicker event rather than hearing two independent lines. That fusion is exactly why arrangers reach for it: a hook that needs to land hard, a melodic idea important enough that the whole band should commit to it, a cadence that should feel unified rather than layered. It's also exactly why doubling everything, all the time, is a trap — if the bass always tracks whatever the right hand is doing, the ear never gets two things to compare, and the texture stops having a foreground and a background at all. The next chapter's subject, Independence, exists because most of a real piece needs the bass doing its *own* job; Doubling is what happens at the specific moments the piece wants unified weight instead.

This is a claim about relationship, not coincidence. A single shared note, surrounded by otherwise unrelated lines, proves nothing: the two voices could have landed on the same pitch class by chance while going about independent business. Doubling requires the bass to follow the upper voice's actual contour — enough of it that a listener can hear one line being reinforced, not two lines briefly touching. And it comes in degrees: a bass line can double an entire phrase, or double just its opening gesture and then release into its own business partway through — a real, useful middle case, not a flaw in either direction.

The common error is calling any shared pitch class "doubling" without checking whether the bass is actually tracking the line above it. A bass note that matches the melody's pitch class on beat one, then diverges completely, hasn't doubled anything — it has coincided with it once.

## The Microscope

All three panels open on the identical phrase, in the right hand, over the same two chords. Only how long the bass keeps tracking it changes.

:::{.content-hidden when-format="epub"}

```{=html}
<div data-comparison-group="doubling-lab">
  <div class="comparison-controls" aria-label="Doubling comparison">
    <button type="button" data-version="A" aria-pressed="true">A — Doubling</button>
    <button type="button" data-version="B" aria-pressed="false">B — Coincidental unison</button>
    <button type="button" data-version="C" aria-pressed="false">C — Partial, then released</button>
  </div>
  <div class="comparison-panel" data-version="A">
    <div class="score-example" id="doubling-tracks-the-melody">
      <p class="abc-caption"><strong>A — The bass tracks the melody.</strong> Every bass note matches the right hand's contour, two octaves below, across both chords.</p>
      <p class="abc-description">A two-bar Gm7-C7 melodic phrase doubled exactly at the double octave throughout.</p>
      <pre class="abc-source">X:1
T:Doubling — the bass tracks the melody
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gm7"g2 _b2 d'2 _b2 | "C7"a2 g2 _b2 g2 |]
[V:LH] "^double"G,2 _B,2 D2 _B,2 | "^double"A,2 G,2 _B,2 G,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="B" hidden>
    <div class="score-example" id="doubling-coincidental-unison">
      <p class="abc-caption"><strong>B — A coincidental unison.</strong> The bass shares its opening pitch with the melody, then moves on its own business for both bars.</p>
      <p class="abc-description">The identical right-hand phrase over an unrelated, independently walking left-hand line that only touches it once.</p>
      <pre class="abc-source">X:1
T:Doubling — a coincidental unison
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gm7"g2 _b2 d'2 _b2 | "C7"a2 g2 _b2 g2 |]
[V:LH] "^coincidental"G,2 D,2 F,2 _B,2 | "^coincidental"C,2 G,2 E,2 _B,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
  <div class="comparison-panel" data-version="C" hidden>
    <div class="score-example" id="doubling-partial">
      <p class="abc-caption"><strong>C — Partial, then released.</strong> The bass doubles the first bar exactly, then lets go into its own line for the second.</p>
      <p class="abc-description">The identical two-bar phrase, doubled for one full bar and independent for the next.</p>
      <pre class="abc-source">X:1
T:Doubling — partial, then released
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gm7"g2 _b2 d'2 _b2 | "C7"a2 g2 _b2 g2 |]
[V:LH] "^double"G,2 _B,2 D2 _B,2 | "^diverges"C,2 G,2 E,2 _B,2 |]</pre>
      <div class="abc-rendered"></div>
    </div>
  </div>
</div>
```

:::

## Listen

Play **Full** on A and notice the fusion: the two staves don't sound like a melody with accompaniment underneath, they sound like one thick event, stated at two registers at once. Play **Full** on B: the opening pitch lines up by coincidence, and the ear briefly expects a relationship that never develops — by the second bar it's clearly heard two unrelated lines the whole time. Play **Full** on C and listen for the exact moment the fusion lets go, partway through — that release is audible as a specific event, not just a fade.

## See

In A, every left-hand attack matches the right hand's letter name, two octaves down, for both bars — `G, _B, D _B,` under `g _b d' _b`, then `A, G, _B, G,` under `a g _b g`. In B, only the opening pitch class matches; everything after belongs to an unrelated, independently walking line built from the same chords' tones but a different contour entirely. In C, bar one is byte-for-byte the same doubling gesture as A's first bar, and bar two is byte-for-byte B's independent second bar — the same two ingredients this Microscope already demonstrated separately, now shown as a single deliberate choice inside one phrase.

## Play

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="doubling-track-the-line">
  <p class="abc-caption"><strong>Track the Line.</strong> Practice locking the bass to a stated upper-voice contour across a chord change.</p>
  <p class="abc-description">Two bars of bass doubling a right-hand melody two octaves below, over Fmaj7 then Dm7 — the other half of this chapter's harmonic world.</p>
  <pre class="abc-source">X:1
T:Track the Line
C:Alessandro Bessi
R:Exercise
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Fmaj7"f2 a2 c'2 a2 | "Dm7"c'2 a2 f2 a2 |]
[V:LH] "^double"F,2 A,2 C2 A,2 | "^double"C2 A,2 F,2 A,2 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Play both bars, listening for the moment your left hand stops feeling like an accompaniment and starts feeling like the same line, restated an octave (and another octave) lower. Then play only the right hand, then only the left — confirm the left hand is a legitimate melody on its own, not just a shadow that only makes sense underneath the other staff.

## Vary

Take "Track the Line" and release the doubling after the first two notes of bar two, letting the last two notes go their own way instead of finishing the phrase. Does the result read as a smaller version of Panel C's partial doubling, or does releasing this early feel like it never really committed to doubling at all? Is there a shortest length a doubled gesture needs to be before a listener's ear registers it as doubling rather than another coincidental unison?

## The Music

"Long Shadow" is a sixteen-bar jazz-fusion study that opens in F major — Gm7, C7, Fmaj7, Dm7 — then, instead of simply repeating itself, modulates up a whole step into G major for its second half before a reharmonized turnaround pulls it back home. In every phrase, the bass doubles the right hand's melodic hook for the phrase's first half and releases into an independent, syncopated line of its own for the second half, until the final phrase reverses the pattern to close on a doubled, unison resolution.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example" id="long-shadow-study">
  <p class="abc-caption"><strong>Long Shadow.</strong> Every phrase opens doubled and releases into independence — until the modulation resolves home on a doubled unison instead.</p>
  <p class="abc-description">A sixteen-bar jazz-fusion study opening in F major (Gm7, C7, Fmaj7, Dm7), modulating up a whole step into G major (Am7, D7, Gmaj7), then reharmonizing Gmaj7 as Gm7 to pivot back to a final Fmaj7.</p>
  <pre class="abc-source">X:1
T:Long Shadow
C:Alessandro Bessi
R:Jazz-fusion study
M:4/4
L:1/8
Q:1/4=100
%%score { RH LH }
%%barsperstaff 4
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] "Gm7"g2 _b2 d'2 _b2 | "Gm7"a2 g2 _b2 g2 | "C7"[ceg_b]8 | "C7"[ceg_b]8 |
"Fmaj7"f2 a2 c'2 a2 | "Fmaj7"c'2 a2 f2 a2 | "Dm7"[dfac']8 | "Dm7"[dfac']8 |
"Am7"a2 c'2 e'2 c'2 | "Am7"b2 a2 c'2 a2 | "D7"[d^fac']8 | "D7"[d^fac']8 |
"Gmaj7"g2 b2 d'2 b2 | "Gmaj7"d'2 b2 g2 b2 | "Gm7"d'2 c'2 _b2 g2 | "Fmaj7"a4 f4 |]
[V:LH] "^double"G,2 _B,2 D2 _B,2 | "^double"A,2 G,2 _B,2 G,2 | "^independent"z1 C,1 z1 E,1 G,2 z2 | "^independent"z1 G,1 z1 _B,1 C2 z2 |
"^double"F,2 A,2 C2 A,2 | "^double"C2 A,2 F,2 A,2 | "^independent"z1 D,1 z1 F,1 A,2 z2 | "^independent"z1 F,1 z1 A,1 D2 z2 |
"^double"A,2 C2 E2 C2 | "^double"B,2 A,2 C2 A,2 | "^independent"z1 D,1 z1 ^F,1 A,2 z2 | "^independent"z1 A,1 z1 C,1 D2 z2 |
"^double"G,2 B,2 D2 B,2 | "^double"D2 B,2 G,2 B,2 | "^double"D2 C2 _B,2 G,2 | "^resolve"A,4 F,4 |]</pre>
  <div class="abc-rendered"></div>
</div>
```

:::

Notice that the independent bars aren't just "not doubling" — they're a real, syncopated funk-bass idea in their own right, built from each chord's own tones, including the D7's raised F-sharp once the piece modulates. Doubling only reads as a deliberate event here because the bass clearly has other things it could be doing, and chooses this one on purpose at specific moments — and the modulation's own return, from Gmaj7 reinterpreted as Gm7, is doubled too, so the bass states the pivot as plainly as everything else it's chosen to reinforce.

## Reflection

"Long Shadow" doubles at the start of every phrase, releases into independence through most of them, then breaks that pattern twice at the end: it stays doubled through the reharmonized turnaround (Gmaj7 pivoting to Gm7) instead of releasing, and closes on unison instead of independence. Why might a piece want its bass to stay doubled specifically through a key change, when independence would have been the established habit by then — and what would a listener actually lose if the modulation itself were left to the right hand alone?
