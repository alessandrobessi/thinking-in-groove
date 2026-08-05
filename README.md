# Thinking in Groove

### A Mental Model for Designing Bass Lines Through Harmony, Motion, and Time

Thinking in Groove is an interactive, piano-score-based book about how
musicians understand and design bass lines. The left hand is the bass;
the right hand makes its harmonic and rhythmic context audible.

Just as [Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers)
teaches harmony through superimposed musical layers, Thinking in Groove
organizes each decision as **Role → Motion → Groove → Interaction →
Variation**.

## Project status

**Role pilot complete.** The published piano edition currently contains
three finished chapters: **The Ground**, **The Definer**, and **The
Inverter**. Every musical example is a piano grand staff with independent
harmony/bass playback, looping, bounded tempo, highlighting, a controlled
laboratory, an exercise, and an eight-bar study.

See `docs/content-audit.md`, `docs/technical-audit.md`, and
`docs/migration-matrix.md` for the explicit migration status. Legacy
chapters have not yet passed the new musical, pedagogical, editorial,
or technical gates.

## How the project is organized

| | |
|---|---|
| [`BLUEPRINT.md`](BLUEPRINT.md) | Vision, core promise, audience, pillars, deliverables. |
| [`ROADMAP.md`](ROADMAP.md) | Legacy phase plan; superseded by the piano-edition roadmap being executed through the audit and migration documents. |
| [`AGENTS.md`](AGENTS.md) | Conceptual editorial roles (Book Architect, Composer, Harmony Reviewer, etc.) — reference only; not wired up as automated agents in this pass. |
| [`docs/`](docs/) | Vocabulary, migration audits, and the canonical piano notation/accompaniment guides. |
| [`book/`](book/) | Three canonical piano chapters plus the unpublished legacy manuscript retained as migration source. |
| [`examples/`](examples/) | Legacy chapter sources plus canonical `laboratories/`, `exercises/`, and `studies/` grand-staff sources. |
| [`scripts/notation.py`](scripts/notation.py) | Authoring-time helpers for spelling ABC bass lines with correct octave placement and Role/Motion/Groove annotation tags. Not part of the build. |
| [`scripts/prepare_manuscript_for_publish.py`](scripts/prepare_manuscript_for_publish.py) | Copies `book/*.md` into `publish/chapters/` ahead of every Quarto render. |
| [`scripts/validate_book_structure.py`](scripts/validate_book_structure.py) | Ensures every published chapter exists, contains only grand-staff examples, and has no tablature dependency. |
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
```

## License

See [`LICENSE`](LICENSE) — CC BY-NC-ND 4.0 for the manuscript, notation,
and prose.
