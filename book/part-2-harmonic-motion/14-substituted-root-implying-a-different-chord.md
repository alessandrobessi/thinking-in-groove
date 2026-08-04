# Substituted Root — Implying a Different Chord

*Chapter 14 — Part 2, Harmonic Motion: How the Bass Moves the Music.*

**Term:** Substituted Root

**Definition:** Using a note other than the expected root to imply a different underlying chord.

## Intuition

The chart says one chord. The bass plays a note that belongs to a different one. For a moment, the harmony the listener hears is not the harmony that's written — and if the substitution is well chosen, that new implied harmony doesn't fight the original, it reframes it.

## Mental Model

A **Substituted Root** is a bass note, other than the expected root, chosen specifically to imply a different underlying chord than the one written or assumed. This is a stronger, more deliberate move than Passing Motion or an Approach Note, both of which are transient, resolving quickly into the "real" harmony. A Substituted Root doesn't resolve away — it sits there, on purpose, and asks the rest of the ensemble (and the listener) to hear the harmony through its lens for as long as it lasts.

The classic case is the tritone substitution: playing the root a tritone away from a dominant chord, implying a different dominant chord that shares the same tritone (the same 3rd and 7th, reinterpreted). But Substituted Root is broader than that one device. Playing the relative minor's root under a major chord, playing a chord's third in the bass to imply a first-inversion sound, playing an unrelated root that reframes a static vamp as something more colorful — all of these are Substituted Root moves, unified by the same principle: the bass, not the chart, decides what harmony the listener actually hears.

This is also where the bass's Colorist Role and Harmonic Motion intersect most directly: a Substituted Root is very often how a Colorist choice gets executed, because reaching for an unexpected root is one of the most efficient ways to change a chord's implied color without anyone else in the band changing a note.

Three tests separate a Substituted Root from a wrong note:

1. **It's held, not brushed past.** A Substituted Root sits long enough for the reinterpretation to register — a fleeting chromatic neighbor on a weak subdivision is more likely an Approach Note (Chapter 13) than a genuine substitution.
2. **It implies something coherent.** The substituted root should suggest a real, nameable chord of its own (a tritone away, a relative minor, an upper structure's root) — if the resulting sound doesn't cohere into anything a listener could label, it's dissonance rather than reinterpretation.
3. **The rest of the band can still follow it.** A Substituted Root works because it reframes shared harmony, not because it abandons it — if nobody else in the ensemble could plausibly hear the logic, the substitution has crossed over into a different note choice's territory entirely, more Colorist flourish than Harmonic Motion device.

## Visual Explanation

The Motion layer marks a Substituted Root with a dotted diagonal line, in amber (`#D97706`) — the same basic shape as Root Motion's straight diagonal, but dotted to signal "this motion implies a different chord than the one written," distinguishing a deliberate reinterpretation from a literal root change. Where the substitution reinforces a Colorist Role, the Role layer above will typically show the Colorist icon at the substituted note itself.

Compare the dotted line here to Deceptive Motion (Chapter 15)'s bent line: a Substituted Root reinterprets the *current* harmony without changing where the phrase is ultimately headed, while Deceptive Motion changes the destination itself. The two devices can appear in the same phrase — a substitution along the way, a deception at the arrival — without being the same thing.

## Musical Example

The laboratory plays G7's own root, G, in the middle bar:

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The laboratory, stated plainly: the bass states the root of each chord, one whole note per bar. Every chapter's example below is a short variation on exactly this.</p>
<pre class="abc-source">
X:1
T:The Laboratory: Dm7 - G7 - Cmaj7, bass states the root
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=88
K:C
% chapter: lab-baseline
% role: anchor
% motion: root motion
% groove: none (plain reading)
% difficulty: beginner
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression used throughout the book
V:Bass clef=bass
"^[R:Anchor]""_[M:Root Motion]"D,8 | "^[R:Anchor]""_[M:Root Motion]"G,,8 | "^[R:Anchor]""_[M:Root Motion]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

A Substituted Root replaces G entirely with Db — a tritone away, sharing G7's tritone of B and F, respelled as Db7's 3rd and b7. Nothing above the bass changes; only the bass's reinterpretation makes the substitution audible. The resolution into C even gets smoother: Db to C is a half step, where G to C was a fourth.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">Substituted Root: same lab, Db replaces G entirely</p>
<pre class="abc-source">
X:1
T:Substituted Root: same lab, Db replaces G entirely
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=90
K:C
% chapter: 14-substituted-root-implying-a-different-chord
% role: n/a
% motion: substituted root
% groove: sparse
% difficulty: advanced
% harmony: Dm7 | G7 (Db substituted in the bass) | Cmaj7
V:Bass clef=bass
"^[R:Anchor]"D,8 | "_[M:Substituted Root]"_D,8 | "^[R:Anchor]""_[M:Cadential Motion]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

Bar 1's D carries no Motion tag beyond plain `"^[R:Anchor]"` — nothing being reinterpreted yet. The Db in bar 2 carries `"_[M:Substituted Root]"`, marking that this note is standing in for the written G rather than stating it. Compare its dotted-line convention (see `docs/visual-language.md`) against the baseline's solid Root Motion line at the same position — the dotted line is what signals "this implies a different chord than the one written."

*Bass tab for "Substituted Root: same lab, Db replaces G entirely":*

```text
G|--------|--------|--------|
D|--------|--------|--------|
A|--------|--------|--------|
E|10------|9-------|8-------|
```


## Practice Ideas

- Take a single static dominant chord and, underneath it, alternate between its written root and its tritone substitute every two bars. Listen for how much the "flavor" of the chord changes even though nobody above you changed a note.
- Try substituting a chord's third or fifth as the bass note instead of a tritone away, and compare how much milder that reframing feels compared to a full tritone substitution.
- Find a recording where the bass plays something that doesn't match the written chart (common in modern jazz and fusion) and figure out what chord the bass is implying instead.
- Practice returning from a Substituted Root back to the expected root and notice how much relief that return provides — the substitution only works because the listener still remembers what "home" sounded like.

## Summary

A Substituted Root lets the bass overrule the chart for as long as it holds a different note than expected, reframing the harmony above it through implication alone — a quiet but total kind of authority that belongs uniquely to the instrument holding down the bottom of the sound.
