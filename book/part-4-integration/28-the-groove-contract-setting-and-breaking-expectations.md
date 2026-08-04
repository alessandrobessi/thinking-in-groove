# The Groove Contract — Setting and Breaking Expectations

*Chapter 28 — Part 4, Integration: Composing With All Three Layers.*

**Term:** Groove Contract

**Definition:** The implicit rhythmic promise established in a piece's opening measures, which a listener expects honored — or knowingly broken.

## Intuition

The first few bars of almost any bass line teach the listener how to listen to the rest of it. Once a line has played four bars of steady quarter notes on the **Pocket**, the listener's ear has quietly agreed to a set of expectations — about **Density**, about where the **Repetition Cell** will fall, about how far from the beat a note is allowed to sit. Nobody signs anything, and nobody says it out loud, but the agreement is real: the audience can feel it the moment it's broken. That agreement is a **Groove Contract**, and — unlike Role, Motion, and Groove themselves — it doesn't live inside a single note. It lives across the whole opening of a piece, and its entire purpose is to be either honored or broken later, on purpose.

## Mental Model

A Groove Contract has two moments, not one: the moment it is *set*, and the moment it is *paid off* — either by being kept, or by being broken in a way the listener can feel as broken rather than as a mistake.

Setting the contract usually happens fast, often within the first one or two **Repetition Cells** of a piece. Whatever combination of **Pocket**, **Density**, and cell-length appears there becomes the implicit baseline — the **Groove Signature** the rest of the piece will be measured against, whether or not it's ever repeated identically again.

Keeping the contract means every subsequent **Variation Layer** stays recognizably related to that baseline — same cell, ornamented; same pocket, occasionally pushed for one beat then returned. The listener's trust is rewarded, and the groove reads as coherent.

Breaking the contract means introducing a change large enough that it can't be heard as a variation of the baseline at all — a **Role Shift**, a sudden change in **Density**, a **Pocket** that moves from behind the beat to sharply ahead of it with no transition. Breaking a Groove Contract is not automatically wrong; it is one of the strongest tools this book has for signalling structural change (a new section, a climax, a joke). What makes it work is that the contract was genuinely established first — you cannot meaningfully break a promise you never made. A piece with no stable opening groove has no contract to break, and its rhythmic surprises will read as noise rather than as events.

## Visual Explanation

The Groove Contract is the first term in this book that is drawn across an entire phrase rather than at a single note, so its diagram spans the whole excerpt rather than pointing at one location. Using the Integration accent color, purple `#7C3AED`: a horizontal bracket is drawn beneath the opening measures where the contract is established, labeled "contract set." A second bracket, in the same purple, marks the measure where the contract is either renewed (dashed border, matching the Variation Layer convention from `docs/visual-language.md`) or broken (solid border, with a small break-mark glyph at the exact beat the departure occurs).

## Musical Example

The cell this whole example loops is the laboratory itself, played as a repeating root-fifth figure rather than one note per bar:

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

The laboratory progression looped four times: the groove is set (bars 1-3), renewed (bars 4-6), broken with a sudden dense, displaced figure (bars 7-8), then restored (bars 9-11) and closed on a held Anchor.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The Groove Contract: the lab looped, set, broken, restored</p>
<pre class="abc-source">
X:1
T:The Groove Contract: the lab looped, set, broken, restored
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=94
K:C
% chapter: 28-the-groove-contract-setting-and-breaking-expectations
% role: n/a
% motion: n/a
% groove: set / renewed / broken / restored
% difficulty: advanced
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression, looped 4x with a break in bars 7-8
% contract: set (bars 1-3), renewed (bars 4-6), broken (bars 7-8), restored (bars 9-11), close (bar 12)
V:Bass clef=bass
"_[G:Groove Contract]"D,2 A,2 D,2 A,2 | G,,2 D,2 G,,2 D,2 | C,2 G,2 C,2 G,2 | D,2 A,2 D,2 A,2 | G,,2 D,2 G,,2 D,2 | C,2 G,2 C,2 G,2 | D,1 A,1 D1 A,1 D1 A,1 D,1 A,1 | D,1 A,1 D1 A,1 D1 A,1 D,1 A,1 | D,2 A,2 D,2 A,2 | G,,2 D,2 G,,2 D,2 | C,2 G,2 C,2 G,2 | "^[R:Anchor]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

Because this term spans measures rather than marking a single note, its notation carries a `% contract:` comment line (the phrase-level convention in `docs/notation-conventions.md`) naming which bars set, renew, break, and restore the groove, in addition to the one per-note `Groove Contract` tag marking where the cell first appears. The break itself (bars 7-8) needs no tag of its own — it's audible as a break because bars 1-6 already established what "normal" sounds like.

*Bass tab for the Groove Contract example (see `examples/by-chapter/28-the-groove-contract-setting-and-breaking-expectations/` for the source files)*

```text
G|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
D|--------|--------|--------|--------|--------|--------|--1212--|--1212--|--------|--------|--------|--------|
A|--12--12|--------|--10--10|--12--12|--------|--10--10|-1212121|-1212121|--12--12|--------|--10--10|--------|
E|10--10--|3-103-10|8---8---|10--10--|3-103-10|8---8---|10----10|10----10|10--10--|3-103-10|8---8---|8-------|
```


## Practice Ideas

- Listen to the first four bars of a bass line you know well, in isolation, and try to state its Groove Contract out loud in one sentence: "steady eighth notes, slightly behind, repeating every two bars." Then listen to the rest of the piece and note every place the contract is kept versus broken.
- Improvise a four-bar groove with a clear, simple contract. Then improvise a fifth bar that breaks it as loudly as possible without changing key or tempo — Density and Pocket alone are usually enough.
- Do the same exercise again, but this time break the contract as subtly as possible — the smallest change that a listener would still consciously register as a departure. This trains the edge of perceptibility, which is where the most effective contract-breaks in real playing tend to live.
- Take a groove with no clear contract (irregular from the start) and notice how differently a break lands, or fails to land, compared to a groove with an established one.

## Summary

A Groove Contract is not a property of any single note — it is the trust a piece's opening measures build with the listener about how time will keep behaving, and the payoff of that trust comes later, either by being kept or by being broken in a way the ear can clearly hear as intentional. Establishing a contract before you break it is what separates a deliberate rhythmic surprise from a line that simply sounds inconsistent.
