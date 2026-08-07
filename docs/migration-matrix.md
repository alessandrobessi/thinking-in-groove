# Migration Matrix

Decisions use the new 40-chapter architecture. “Rewrite” means no legacy page is publishable unchanged; “merge” means useful material moves into the named destination; “remove” means the old classification is retired, while original music may still be curated later.

| Existing file | Decision | Destination / reason |
|---|---|---|
| `part-1-role/01-the-anchor.md` | Migrated | Ch. 1 The Ground now distinguishes root weight from sustained chord tone. |
| `part-1-role/02-the-definer.md` | Migrated | Ch. 2 The Definer now provides audible upper harmony. |
| `part-1-role/03-the-connector.md` | Migrated/merge pending | Its chapter slot is now Ch. 3 The Inverter; useful Connector material moves later to Ch. 15. |
| `part-1-role/04-the-driver.md` | Migrated | Transitional file slot now publishes Ch. 4 The Pedal; Driver has moved to its final Ch. 6 slot. |
| `part-1-role/05-the-colorist.md` | Migrated | Transitional file slot now publishes Ch. 5 The Reframer; “colour” is retired because it hides harmonic reinterpretation. |
| `part-1-role/06-the-shadow.md` | Migrated/merge pending | Transitional file slot now publishes Ch. 6 The Driver; useful Shadow material moves to Ch. 28 Doubling and Ch. 8 The Conversationalist. |
| `part-1-role/07-the-voice-leader.md` | Migrated/merge pending | Transitional file slot now publishes Ch. 7 The Supporter; useful Voice-Leader material remains in Ch. 15 Connecting Chords and Ch. 16 Contrary Motion. |
| `part-1-role/08-the-commentator.md` | Migrated/merge pending | Transitional file slot now publishes Ch. 8 The Conversationalist; detailed interaction technique moves to Ch. 31 Call and Response. |
| `part-1-role/09-role-shift-when-the-job-changes-mid-phrase.md` | Merge | Ch. 35 design algorithm and capstone analysis. |
| `part-2-harmonic-motion/10-root-motion-the-bass-line-as-harmonic-skeleton.md` | Merge | Ch. 1 The Ground and Ch. 15 Connecting Chords. |
| `part-2-harmonic-motion/11-the-pedal-stillness-under-change.md` | Merge | Pedal role is now Ch. 4; controlled immobility remains for Ch. 9 Staying. |
| `part-2-harmonic-motion/12-passing-motion-connecting-two-points.md` | Migrated | Connecting Chords now compares routes over shared functional harmony. |
| `part-2-harmonic-motion/13-the-approach-note-arriving-with-intention.md` | Migrated | Approaching now uses controlled grand-staff comparison and shared functional harmony. |
| `part-2-harmonic-motion/14-substituted-root-implying-a-different-chord.md` | Merge | Useful material has moved to Ch. 5 The Reframer; the old classification is retired. |
| `part-2-harmonic-motion/15-deceptive-motion-the-expected-turn-that-isnt.md` | Merge | Ch. 15 Connecting Chords and variation studies. |
| `part-2-harmonic-motion/16-cadential-motion-tension-and-release.md` | Migrated | Contrary Motion now uses opposing outer voices over shared functional harmony. |
| `part-2-harmonic-motion/17-harmonic-rhythm-who-decides-when-the-chord-changes.md` | Rewrite | Ch. 34 Harmonic Rhythm. |
| `part-2-harmonic-motion/18-motion-profile-the-shape-of-a-phrase.md` | Rewrite | Ch. 17 Motion Maps. |
| `part-3-groove/19-the-pocket-where-exactly-is-the-note.md` | Migrated | Attack Placement now separates the written grid from microtiming and performed pocket. |
| `part-3-groove/20-syncopation-points-avoiding-the-obvious-beat.md` | Migrated | Syncopation now demonstrates weak-position attacks tied across a continuing metrical reference. |
| `part-3-groove/21-space-as-content-the-power-of-not-playing.md` | Migrated | Space now removes expected bass attacks beneath continuing right-hand context. |
| `part-3-groove/22-the-repetition-cell-the-riff-atom.md` | Rewrite | Ch. 24 Repeated Cells. |
| `part-3-groove/23-the-variation-layer-keeping-a-groove-alive.md` | Rewrite | Ch. 25 Variation Without Collapse. |
| `part-3-groove/24-density-controlling-energy-through-note-count.md` | Merge | Ch. 32 Density Balance; density is relational. |
| `part-3-groove/25-push-and-lay-back-playing-around-the-beat.md` | Migrated | Duration now isolates note endings from attacks and performed feel. |
| `part-3-groove/26-the-groove-signature-what-makes-a-line-recognizable.md` | Migrated | Anticipation now separates early destination notes from chord boundaries and microtiming. |
| `part-4-integration/27-the-layer-stack-role-motion-and-groove-at-once.md` | Merge | Ch. 35 design algorithm. |
| `part-4-integration/28-the-groove-contract-setting-and-breaking-expectations.md` | Removed | Superseded by Ch. 24–26 groove identity and phrase rhythm; file deleted, no direct Part V replacement. |
| `part-4-integration/29-designing-a-bass-line-from-scratch-a-worked-case-study.md` | Rewrite | Ch. 40 Complete Capstone (Ch. 35's algorithm draws on file 27, not this one). |
| `back-matter/01-one-groove-many-roles.md` | Retain/rewrite | Same eight-reinterpretation structure, rewritten against the actual v2 Role mechanisms (Ground, Definer, Inverter, Pedal, Reframer, Driver, Supporter, Conversationalist) in place; not merged elsewhere. |
| `back-matter/02-the-role-motion-groove-map.md` | Rewrite | Five-part map (Role/Motion/Groove/Interaction/Design) and vocabulary v2. |
| `back-matter/03-a-mental-model-you-can-forget-while-playing.md` | Retain/rewrite | Closing essay after capstone; term references updated in place. |
| `back-matter/04-designing-your-own-bass-lines.md` | Rewrite | Restates Ch. 35's algorithm verbatim as a checklist; sketches point to Ch. 36/37 instead of duplicating them. |

## Example inventory decision

All 29 legacy chapter `.abc` files and their `.tab.txt` companions are retained temporarily as migration sources. None is approved as a canonical piano example. The shared bass-only laboratory is retired for new work. New sources live by purpose under `examples/laboratories/`, `examples/exercises/`, `examples/studies/`, and later `examples/comparisons/` and `examples/capstone/`.
