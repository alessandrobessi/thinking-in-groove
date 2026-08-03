# Chapter Map (Phase 1 Deliverable)

30 sections: 1 unnumbered introduction (front matter) + 29 numbered
concept chapters across 4 parts, plus a back-matter set of appendices.
Each chapter introduces exactly one idea (Book Architect acceptance
criterion in `AGENTS.md`) and is ordered for progressive learning
(Curriculum Designer goal).

File paths below are the actual `book/` layout on disk — this table is
the single source of truth that `publish/_quarto.yml` and
`scripts/validate_book_structure.py` must agree with.

## Introduction (unnumbered front matter)

**How This Book Thinks** — lives in `publish/preface.qmd`, not under
`book/`. Orients the reader to the Role / Motion / Groove mental model
and the four-layer visual language, before any numbered chapter uses
them.

## Part I — Role: What Job Is the Bass Doing?

| # | Title | File |
|---|---|---|
| 1 | The Anchor | `book/part-1-role/01-the-anchor.md` |
| 2 | The Definer | `book/part-1-role/02-the-definer.md` |
| 3 | The Connector | `book/part-1-role/03-the-connector.md` |
| 4 | The Driver | `book/part-1-role/04-the-driver.md` |
| 5 | The Colorist | `book/part-1-role/05-the-colorist.md` |
| 6 | The Shadow | `book/part-1-role/06-the-shadow.md` |
| 7 | The Voice-Leader | `book/part-1-role/07-the-voice-leader.md` |
| 8 | The Commentator | `book/part-1-role/08-the-commentator.md` |
| 9 | Role Shift — When the Job Changes Mid-Phrase *(synthesis)* | `book/part-1-role/09-role-shift-when-the-job-changes-mid-phrase.md` |

## Part II — Harmonic Motion: How the Bass Moves the Music

| # | Title | File |
|---|---|---|
| 10 | Root Motion — The Bass Line as Harmonic Skeleton | `book/part-2-harmonic-motion/10-root-motion-the-bass-line-as-harmonic-skeleton.md` |
| 11 | The Pedal — Stillness Under Change | `book/part-2-harmonic-motion/11-the-pedal-stillness-under-change.md` |
| 12 | Passing Motion — Connecting Two Points | `book/part-2-harmonic-motion/12-passing-motion-connecting-two-points.md` |
| 13 | The Approach Note — Arriving with Intention | `book/part-2-harmonic-motion/13-the-approach-note-arriving-with-intention.md` |
| 14 | Substituted Root — Implying a Different Chord | `book/part-2-harmonic-motion/14-substituted-root-implying-a-different-chord.md` |
| 15 | Deceptive Motion — The Expected Turn That Isn't | `book/part-2-harmonic-motion/15-deceptive-motion-the-expected-turn-that-isnt.md` |
| 16 | Cadential Motion — Tension and Release | `book/part-2-harmonic-motion/16-cadential-motion-tension-and-release.md` |
| 17 | Harmonic Rhythm — Who Decides When the Chord Changes | `book/part-2-harmonic-motion/17-harmonic-rhythm-who-decides-when-the-chord-changes.md` |
| 18 | Motion Profile — The Shape of a Phrase *(synthesis)* | `book/part-2-harmonic-motion/18-motion-profile-the-shape-of-a-phrase.md` |

## Part III — Groove: How the Bass Creates Feel

| # | Title | File |
|---|---|---|
| 19 | The Pocket — Where Exactly Is the Note | `book/part-3-groove/19-the-pocket-where-exactly-is-the-note.md` |
| 20 | Syncopation Points — Avoiding the Obvious Beat | `book/part-3-groove/20-syncopation-points-avoiding-the-obvious-beat.md` |
| 21 | Space as Content — The Power of Not Playing | `book/part-3-groove/21-space-as-content-the-power-of-not-playing.md` |
| 22 | The Repetition Cell — The Riff Atom | `book/part-3-groove/22-the-repetition-cell-the-riff-atom.md` |
| 23 | The Variation Layer — Keeping a Groove Alive | `book/part-3-groove/23-the-variation-layer-keeping-a-groove-alive.md` |
| 24 | Density — Controlling Energy Through Note Count | `book/part-3-groove/24-density-controlling-energy-through-note-count.md` |
| 25 | Push and Lay-Back — Playing Around the Beat | `book/part-3-groove/25-push-and-lay-back-playing-around-the-beat.md` |
| 26 | The Groove Signature — What Makes a Line Recognizable *(synthesis)* | `book/part-3-groove/26-the-groove-signature-what-makes-a-line-recognizable.md` |

## Part IV — Integration: Composing With All Three Layers

| # | Title | File |
|---|---|---|
| 27 | The Layer Stack — Role, Motion, and Groove at Once | `book/part-4-integration/27-the-layer-stack-role-motion-and-groove-at-once.md` |
| 28 | The Groove Contract — Setting and Breaking Expectations | `book/part-4-integration/28-the-groove-contract-setting-and-breaking-expectations.md` |
| 29 | Designing a Bass Line from Scratch — A Worked Case Study *(capstone)* | `book/part-4-integration/29-designing-a-bass-line-from-scratch-a-worked-case-study.md` |

## Back Matter — Integrated Study and Appendices

| # | Title | File |
|---|---|---|
| 1 | One Groove, Many Roles | `book/back-matter/01-one-groove-many-roles.md` |
| 2 | The Role / Motion / Groove Map | `book/back-matter/02-the-role-motion-groove-map.md` |
| 3 | A Mental Model You Can Forget While Playing | `book/back-matter/03-a-mental-model-you-can-forget-while-playing.md` |
| 4 | Designing Your Own Bass Lines | `book/back-matter/04-designing-your-own-bass-lines.md` |

## Progression Logic

- Part I precedes Part II: you must be able to name a note's job before
  discussing how it moves harmony.
- Part II precedes Part III: harmonic motion is discussed independent of
  time-feel before groove mechanics are introduced, avoiding conflating
  "what" with "when."
- Part III precedes Part IV: all three vocabularies must exist before
  showing them combined.
- Each Part ends with a synthesis chapter that only recombines
  already-introduced terms — no new vocabulary — reinforcing retention
  before moving to the next Part.
- Back matter assumes the entire vocabulary and is not part of the
  linear teaching sequence — analogous to Thinking in Layers'
  "Integrated Study and Appendices" section.
