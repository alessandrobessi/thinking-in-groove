# Notation Style — Piano Edition

This document is authoritative for newly migrated examples. Legacy bass-only examples remain in the repository until their migration decision is executed.

## Canonical score

- Use a grand staff with `%%score { RH LH }`.
- Name the upper voice `Harmony` and the lower voice `Bass`.
- Put chord symbols above the upper staff.
- Treat chord symbols as silent analytical labels; synthesized playback must set `chordsOff: true` so only written staff notes sound.
- Keep the bass monophonic and generally within E1–G3.
- Use two or four measures per system when the renderer permits it.
- Use `C:Alessandro Bessi` in every new source file.
- Do not add tablature, fingering, fret/string labels, or note-name labels to chord stacks.

## Musical claims

Notation may claim metric placement, subdivision, duration, accent, articulation, pitch, and register. It must not describe a written displacement as subtle microtiming. “Push,” “lay back,” and “pocket” belong to performed feel unless a playback simulation explicitly applies timing offsets.

## Comparisons

An A/B laboratory is two to four bars. Preserve harmony, upper-voice rhythm, tempo, register, dynamics, and phrase length. Change only the bass decision being taught. State that difference in the caption and accessible description.

## Source template

```abc
X:1
T:Example title
C:Alessandro Bessi
R:Concept study
M:4/4
L:1/8
Q:1/4=88
%%score { RH LH }
V:RH clef=treble name="Harmony"
V:LH clef=bass name="Bass"
K:C
[V:RH] ...
[V:LH] ...
```
