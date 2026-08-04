# Designing a Bass Line from Scratch — A Worked Case Study

*Chapter 29 — Part 4, Integration: Composing With All Three Layers.*

**Term:** (capstone — no new term; recombines the full vocabulary)

**Definition:** A worked, start-to-finish design of one original bass line, narrating every Role/Motion/Groove decision made along the way.

## Intuition

Every chapter before this one gave you a single tool and a small, controlled example to see it work in isolation. That is the right way to learn a tool. It is not the right way to design a real bass line, because a real bass line never asks you to apply one tool at a time — it asks you to make dozens of small decisions, fast, in an order that mostly isn't visible even to the player making them. This chapter slows that process down to a crawl and narrates it out loud, decision by decision, so you can see where every one of this book's terms actually earns its place in a finished line rather than in a demonstration.

## Mental Model

Designing a bass line from scratch is not a single decision. It is a short, repeatable sequence of decisions, and this chapter's method states it explicitly:

1. **Fix the harmonic situation.** What progression, what harmonic rhythm, what's already implied.
2. **Choose a Motion Profile for the phrase as a whole** — before choosing a single note, decide the overall harmonic shape you want the line to trace.
3. **Choose a Groove Signature for the phrase as a whole** — before choosing a single rhythm, decide the overall pocket, density, and repetition-cell identity.
4. **Assign a Role to each structurally important note**, in light of the harmonic situation and the Motion Profile already chosen.
5. **Fill in Motion between those notes**, connecting the Role-assigned notes with the specific Motion terms (passing motion, approach notes, substitutions) that satisfy the chosen Motion Profile.
6. **Fill in Groove**, placing every note precisely in time according to the chosen Groove Signature, including deliberate departures from it.
7. **State the Groove Contract** the opening bars establish, and decide, deliberately, whether the rest of the phrase keeps it or breaks it.
8. **Review the whole thing as a set of Layer Stacks**, note by note, and adjust anything where the three layers accidentally contradict each other.

The order matters. Notice that Motion Profile and Groove Signature — both *phrase-level* decisions — come before any single note is chosen. This is the opposite of how most bass lines get composed by instinct, which is usually note-by-note from the first beat forward. Working top-down, from the whole phrase's shape inward to individual notes, is slower the first few times you do it deliberately, and considerably faster once it becomes habit, because it eliminates the trial-and-error of playing four bars forward before realizing the shape doesn't work.

## Visual Explanation

This chapter's diagram is the fullest version of the four-layer stack introduced across the whole book: every marked note in the three-bar phrase below carries its own Role icon (blue), Motion arc (amber), and Groove pulse-dot (green), with a purple Layer Stack bracket at each structurally important note. Reading this diagram from left to right, bar by bar, is effectively reading a transcript of every decision this chapter narrates below.

## Musical Example

**The situation.** The same laboratory progression used throughout this book, **Dm7 – G7 – Cmaj7**, one bar each, around 84 BPM. Every decision below is made against this three-bar frame — the phrase-level decisions (Steps 1–3 and 7 in the Mental Model above) matter just as much in a longer piece, but a fuller worked-out example of *those* belongs in a real composition, not a three-bar laboratory excerpt. What a three-bar frame can show concretely is Steps 4–6 and 8: naming a Role, filling in Motion, placing Groove, and checking the result.

The laboratory, stated plainly, as a reference point:

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

**Step 4 — Assign Role to structural notes.** D opens Dm7 as **Anchor**; F, arriving in the second half of bar 1, is the **Definer** that confirms the b3 right before the harmony moves. G opens G7 as **Connector**; B, in the second half of bar 2, is the **Colorist** — the major 3rd of G7, voiced high. C closes Cmaj7 as **Anchor** again. That's a **Role Shift** arc in three bars: Anchor → Definer → Connector → Colorist → Anchor.

**Step 5 — Fill in Motion.** D to F is **Pedal**-adjacent stillness resolving into a Definer, not a leap. G to B moves by **Passing Motion** into an **Approach Note** — a chromatic neighbor a half step below B, arriving just before it. The final C arrives by **Cadential Motion**.

**Step 6 — Fill in Groove.** D sits on the **Pocket**. The Connector run into G7 is **Push**ed — arriving slightly ahead. The final C is **Lay-back** — arriving slightly behind — so the phrase opens on time and settles late, a small deliberate asymmetry.

**Step 8 — Review as Layer Stacks.** Checking the Colorist B: Role = Colorist, Motion = Approach Note, Groove = mid-bar, unhurried. All three agree on the same effect — brightness, arriving with intention rather than rushed — so the stack is coherent and the note is kept as designed. This is the check every one of this book's short examples has secretly been teaching you to run.

:::{.content-hidden when-format="epub"}

```{=html}
<div class="score-example">
<p class="abc-caption">The laboratory progression with every decision named: D as Anchor/Pedal, F as Definer, G as Connector, B as Colorist (voiced high, approached chromatically), and C as the final Anchor, laid back.</p>
<pre class="abc-source">
X:1
T:Designing a Bass Line: the lab, every layer named
C:Thinking in Groove
M:4/4
L:1/8
Q:1/4=84
K:C
% chapter: 29-designing-a-bass-line-from-scratch-a-worked-case-study
% role: full arc
% motion: full arc
% groove: full arc
% difficulty: advanced
% harmony: Dm7 | G7 | Cmaj7 -- the fixed laboratory progression
V:Bass clef=bass
"^[R:Anchor]""_[M:Pedal|G:Pocket]"D,4 "^[R:Definer]"F,,4 | "^[R:Connector]""_[M:Passing Motion]"G,,4 "^[R:Colorist]""_[M:Approach Note]"B,4 | "^[R:Anchor]""_[M:Cadential Motion|G:Lay-back]"C,8 |]
</pre>
<div class="abc-rendered"></div>
<button class="abc-play" type="button">▶ Play</button>
</div>
```

:::

## Annotated Notation

Every note in this example carries a full Role/Motion tag, and two carry a Groove tag as well, per `docs/notation-conventions.md`'s combined-tag syntax — the densest tagging in the book relative to the number of bars, since the whole point of a capstone example is that no layer goes unnamed. Read left to right, the tags are literally Steps 4–6 of the Mental Model's method, transcribed onto the staff.

*Bass tab for the worked case study (see `examples/by-chapter/29-designing-a-bass-line-from-scratch-a-worked-case-study/` for the source files)*

```text
G|--------|--------|--------|
D|--------|----9---|--------|
A|--------|--------|--------|
E|10--1---|3-------|8-------|
```


## Practice Ideas

- Take any progression you already play over regularly and run the eight-step method above on paper before touching your instrument: fix the harmony, choose a Motion Profile, choose a Groove Signature, assign Roles, fill in Motion, fill in Groove, state the Groove Contract, review as Layer Stacks. Only then play what you designed.
- Compare a line you designed top-down this way against a line you improvise the usual way, note by note, over the same progression. Neither is "better" — the goal is to notice specifically where they differ, since that difference is what conscious design adds to instinct.
- Redo Step 2 and Step 3 for the same Dm7–G7–Cmaj7 laboratory with a completely different Motion Profile (say, cyclical instead of ascending-then-cadential) and Groove Signature (say, dense and on-top-of-the-beat instead of sparse and behind it), and notice how much of the phrase's identity comes from those two decisions alone, before a single Role has even been assigned.
- Try designing a phrase where you intentionally make Step 8 fail — build a Layer Stack where the three layers contradict each other on purpose (an Anchor with Deceptive Motion pushed hard ahead of the beat) — and listen for what that contradiction actually sounds like. Knowing what a broken stack sounds like sharpens your ear for why the coherent ones work.

## Summary

Designing a bass line from scratch is not a bigger version of any single chapter's idea — it's the discipline of making the same handful of decisions this book has been naming since Chapter 1, in a consistent order, for every note in a phrase instead of one demonstration note at a time. The vocabulary was never the point. The point was always to give you a small, checkable set of questions to ask about a line before you commit to playing it.
