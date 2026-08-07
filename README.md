# Thinking in Groove

### A Mental Model for Designing Bass Lines Through Harmony, Motion, and Time

Thinking in Groove is an interactive, piano-score-based book about how
musicians understand and design bass lines. The left hand is the bass;
the right hand makes its harmonic and rhythmic context audible.

Just as [Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers)
teaches harmony through superimposed musical layers, Thinking in Groove
organizes each decision as **Role → Motion → Groove → Interaction →
Design**.

## Project status

**All 40 chapters complete.** The published piano edition covers the
full five-part architecture — Role (1–8), Motion (9–17), Groove
(18–27), Interaction (28–34), and Design (35–40) — with over 160
canonical grand-staff examples. The study collection includes 40
original studies plus the closing sixteen-bar capstone, each with
independent Full/Bass/Harmony playback and current-note highlighting.
No missing-example notices or legacy bass-only scores remain in the
published book, and five automated validators (structure, piano
prototype, study collection, architecture docs, and drift detection)
run on every push.

See `docs/migration-matrix.md` for the per-file migration record, and
`docs/content-audit.md` / `docs/technical-audit.md` for the dated
audits that motivated the piano pivot. Remaining open items: a
`Notaroll`-based visual/animation layer (named in `AGENTS.md` and
`BLUEPRINT.md`) is still undesigned, and the print-formatting pass
(PDF/EPUB polish) has not had a dedicated review.

## How the project is organized

| | |
|---|---|
| [`BLUEPRINT.md`](BLUEPRINT.md) | Vision, core promise, audience, pillars, deliverables. |
| [`ROADMAP.md`](ROADMAP.md) | The six-phase plan, updated for the piano-based grand-staff edition and its nine-section chapter structure. |
| [`AGENTS.md`](AGENTS.md) | Conceptual editorial roles (Book Architect, Composer, Harmony Reviewer, etc.) — reference only; not wired up as automated agents in this pass. |
| [`docs/`](docs/) | The 40-chapter map (`chapter-map.md`), authoritative `vocabulary-v2.md` (the legacy `vocabulary.md` has been removed), migration audits, and canonical notation/accompaniment guides. |
| [`book/`](book/) | Canonical chapter prose, including the fully rewritten pilot chapters. |
| [`examples/`](examples/) | Canonical laboratories, exercises, chapter examples, complete grand-staff studies, and the closing capstone. |
| [`scripts/notation.py`](scripts/notation.py) | Authoring-time helpers for spelling ABC bass lines with correct octave placement and Role/Motion/Groove annotation tags. Not part of the build. |
| [`scripts/prepare_manuscript_for_publish.py`](scripts/prepare_manuscript_for_publish.py) | Copies `book/*.md` into `publish/chapters/` ahead of every Quarto render. |
| [`scripts/validate_book_structure.py`](scripts/validate_book_structure.py) | Ensures every published chapter exists, contains only grand-staff examples, and has no tablature dependency. |
| [`scripts/validate_no_drift.py`](scripts/validate_no_drift.py) | Catches nav-order drift against `chapter-map.md`, orphaned legacy `.abc` placeholders, and stale bookkeeping entries. |
| [`publish/`](publish/) | The Quarto book project: `_quarto.yml`, front-matter pages, and the abcjs notation/audio widget (`publish/assets/notation-head.html`). |
| [`.github/workflows/`](.github/workflows/) | `validate.yml` checks manuscript structure and does an HTML render sanity check on every push/PR; `build-book.yml` renders the full book and deploys it on every push to `main`. |

## Reading the built book

**[Read it online](https://alessandrobessi.github.io/thinking-in-groove/)**
— rebuilt automatically on every push to `main`. A PDF and EPUB of the
same build are attached to the repo's
[latest release](../../releases/tag/latest-build), also updated on
every push.

## Building the book locally

Requires [Quarto](https://quarto.org) and [Typst](https://typst.app)
(`brew install --cask quarto && brew install typst`). From the repo
root:

```sh
python3 scripts/prepare_manuscript_for_publish.py
cd publish && quarto render
```

Cover and author images are in place (`publish/assets/cover.png`,
`cover-epub.png`, `author.png`) — see
[`publish/assets/README.md`](publish/assets/README.md) for the one
open item (an EPUB-specific cover crop).

## Validating the manuscript structure

```sh
pip install -r requirements.txt
python3 scripts/validate_book_structure.py
python3 scripts/validate_piano_prototype.py
python3 scripts/validate_study_collection.py
python3 scripts/validate_architecture_docs.py
python3 scripts/validate_no_drift.py
```

## License

See [`LICENSE`](LICENSE) — CC BY-NC-ND 4.0 for the manuscript, notation,
and prose.
