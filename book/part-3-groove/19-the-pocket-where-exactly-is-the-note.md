# The Pocket — Where Exactly Is the Note

*Chapter 19 — Part 3, Groove: How the Bass Creates Feel.*

**Term:** Pocket

**Definition:** The precise rhythmic placement of a note relative to the underlying pulse (ahead, dead-center, behind).

## Intuition

Play the same eight bars for three different bass players and record all
three. Same notes, same rhythm on paper, same tempo on the metronome.
Listen back and you will hear three different feels — one urgent, one
relaxed, one mechanical. Nothing about *what* they played differs.
What differs is *exactly when*, inside the beat, each note actually
lands. That's the Pocket, and it is the first Groove concept in this
book precisely because it is invisible on the page and unmistakable to
the ear.

Every earlier chapter in this book asked what a note does — its Role,
its harmonic Motion. The Pocket asks something a printed rhythm value
cannot answer: relative to the pulse a listener feels, does this note
arrive early, dead-center, or late?

## Mental Model

Standard notation quantizes time into fixed values — quarter notes,
eighth notes, sixteenth notes — and treats a note as either "on" one of
those grid positions or "off" it, with syncopation as the only
recognized deviation. Pocket describes a much finer, continuous
dimension underneath that grid: *within* a written eighth note, is this
specific attack a few milliseconds ahead of the felt pulse, dead center
on it, or a few milliseconds behind it?

Three reference positions are useful:

- **Ahead of the beat.** The note anticipates the pulse by a small,
  consistent margin. This reads as urgency, forward lean, or
  excitement — common in up-tempo bebop walking lines and aggressive
  funk.
- **Dead-center.** The note lands exactly with the felt pulse. This
  reads as neutral, precise, sometimes mechanical if sustained across
  an entire performance — useful as a deliberate effect, not just a
  default.
- **Behind the beat.** The note arrives a small, consistent margin
  after the pulse. This reads as relaxed, heavy, or laid-back —
  the signature feel of much neo-soul and blues-inflected playing.

The critical word in all three is *consistent*. A note that's early one
bar and late the next isn't demonstrating Pocket, it's demonstrating
poor time. Pocket is a chosen, sustained relationship to the pulse, not
a random scatter around it. A bass line's Role tells you its harmonic
job; its Pocket tells you where in time that job gets done — the two
are independent choices, which is why the same Anchor line can be played
three different ways and feel like three different bass players.

## Visual Explanation

On the Groove-layer pulse timeline (green, `#16A34A`, beneath the tab —
see `docs/visual-language.md`), each bass note is a filled dot plotted
against a row of evenly spaced pulse ticks. Pocket is read directly off
the dot's horizontal position relative to its nearest tick:

- A dot **shifted left** of its tick = ahead of the beat.
- A dot **centered** on its tick = dead-center.
- A dot **shifted right** of its tick = behind the beat (lay-back).

Because Pocket is a whole-line tendency rather than an isolated event,
a chapter's diagram typically shows the *same* small leftward or
rightward offset repeated across every dot in the excerpt — a visibly
consistent lean, not an isolated outlier. (Compare this to Chapter 25,
The Push and Lay-Back, where the offset appears at one specific,
structurally meaningful moment rather than throughout.) The Role layer
above the staff (blue) and the Motion layer below it (amber) are
unaffected by Pocket — the same Anchor-Pedal combination can be drawn
with the dots shifted any of the three ways, which is exactly the point:
Pocket is an independent axis, not a property of Role or Motion.

## Musical Example

An 8-bar illustration works best as three short passes over the same
material rather than one long line, since Pocket only becomes audible in
contrast.

Set a static vamp: **Dm7** for the full 8 bars, a moderate funk tempo
(quarter = 92), 4/4. The bass line itself is intentionally simple and
repetitive — a one-bar cell built from the root and fifth (D and A),
played as steady quarter notes with one eighth-note pickup into bar 2,
4, 6, and 8 — so that the *only* variable across the three passes is
where each attack sits relative to the click:

- **Pass 1 (bars 1–2, repeated as the reference):** every note
  dead-center on the pulse.
- **Pass 2 (bars 3–4):** the identical rhythm, every note shifted
  consistently behind the beat — late enough to be clearly audible
  against a click, not so late it reads as a mistake.
- **Pass 3 (bars 5–6):** the identical rhythm again, shifted ahead of
  the beat instead.
- **Bars 7–8:** return to dead-center, so the ear has a stable reference
  to compare all three against on the way out.

The point of the example is that the pitch content, the rhythm on the
page, and the Role (Anchor throughout — this is a pedal-like, root/fifth
grounding line) never change. Only the Pocket does.

*Notated example pending — see `examples/by-chapter/19-the-pocket-where-exactly-is-the-note/` (Phase 2) and `docs/notation-conventions.md` for the annotation convention.*

## Annotated Notation

Once notated, all three passes share identical Role tags
(`"^[R:Anchor]"`) and identical Motion tags (`"_[M:Pedal]"`) at every
note — reinforcing that Role and Motion are unchanged. The Groove tag is
the only one that differs pass to pass: `"_[G:Center]"` for bars 1–2 and
7–8, `"_[G:Lay-back]"` for bars 3–4, `"_[G:Push]"` for bars 5–6. On the
rendered diagram, this is the only layer whose symbol moves — the green
dots drift right, then left, of their ticks while the blue Role icon and
amber Motion arc stay fixed in place above and below them.

*Notated example pending — see `examples/by-chapter/19-the-pocket-where-exactly-is-the-note/` (Phase 2) and `docs/notation-conventions.md` for the annotation convention.*

## Practice Ideas

- **Three-pocket loop.** Loop a simple one-bar bass figure against a
  metronome or drum machine. Play it dead-center for four bars, then
  deliberately behind for four bars, then deliberately ahead for four
  bars, without changing a single note. Record yourself; most players
  are surprised how small the actual timing shift needs to be to read
  clearly as a feel change.
- **Match a recording's pocket.** Pick a recording known for a specific
  feel (a laid-back neo-soul track, an urgent up-tempo bebop track).
  Play along and try to disappear into its exact pocket rather than
  your own default. This trains you to hear Pocket as a variable you
  control, not a fixed personal trait.
- **Click subdivision test.** Set a metronome to click only on beat 1
  of each bar (not all four beats). Play a steady quarter-note line and
  see how far you drift from dead-center without the constant
  correction of a click on every beat — this reveals your unconscious,
  undeliberate pocket tendency.
- **Waveform check.** Record yourself against a click track in software
  that shows a waveform, and visually measure how far your attacks land
  from the click's own transient. Numbers (in milliseconds) make an
  otherwise subjective feeling concrete and repeatable.

## Summary

The Pocket is the precise, consistent relationship between a note's
actual attack and the pulse a listener feels — ahead, dead-center, or
behind — and it operates completely independently of what a bass line's
notes or Role are on paper. Because it lives underneath standard
notation's grid, it can only be trained by ear and by playing against a
steady reference, not by reading rhythms more carefully. Every example
in the rest of this book carries an implicit Pocket choice; from here on,
listen for it even in chapters that aren't about it.
