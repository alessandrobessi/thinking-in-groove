# Thinking in Groove

### A Mental Model for Bass Harmony, Groove, and Musical Motion

Thinking in Groove is not a bass method. It is a book about how bass
players think.

Just as [Thinking in Layers](https://github.com/alessandrobessi/thinking-in-layers)
teaches harmony through superimposed musical layers, Thinking in Groove
teaches bass through a new conceptual vocabulary: **Role**, **Harmonic
Motion**, and **Groove**. See [`BLUEPRINT.md`](BLUEPRINT.md) for the
full vision and [`ROADMAP.md`](ROADMAP.md) for the phase plan.

## Project status

**Phase 1 — Foundations is complete** (see `docs/`: conceptual
vocabulary, visual language, notation conventions, final chapter map).

**Phase 2 and Phase 3 have a full first draft.** All 29 chapters have
composed ABC examples + bass tabs (`examples/by-chapter/`) and full
chapter prose (`book/`), with the examples embedded directly in the
relevant Musical Example / Annotated Notation sections. Part II
(Harmonic Motion) chapters are more concise than Parts I/III and are
being brought up to matching depth. None of this has been reviewed —
Phase 5 (Technical Review) hasn't started, and Phase 4 (Multimedia)
and Phase 6 (Publication) are largely open beyond the Quarto/Typst
scaffold and cover/author art already in place.

## How the project is organized

| | |
|---|---|
| [`BLUEPRINT.md`](BLUEPRINT.md) | Vision, core promise, audience, pillars, deliverables. |
| [`ROADMAP.md`](ROADMAP.md) | The six-phase plan from foundations to publication. |
| [`AGENTS.md`](AGENTS.md) | Conceptual editorial roles (Book Architect, Composer, Harmony Reviewer, etc.) — reference only; not wired up as automated agents in this pass. |
| [`docs/`](docs/) | Phase 1 deliverables: `vocabulary.md`, `visual-language.md`, `notation-conventions.md`, `chapter-map.md`, plus `glossary.md` and `style-guide.md`. |
| [`book/`](book/) | The manuscript, one file per chapter, organized by Part, plus a `back-matter/` folder for the integrated study and appendices. All 29 chapters + 4 appendices have full first-draft prose with embedded musical examples. |
| [`examples/`](examples/) | The ABC notation example repository named as its own deliverable in `BLUEPRINT.md`: one `.abc` + one `.tab.txt` per musical example, cataloged in `examples/INDEX.md`. All 29 composed. |
| [`scripts/notation.py`](scripts/notation.py) | Authoring-time helpers for spelling ABC bass lines with correct octave placement and Role/Motion/Groove annotation tags. Not part of the build. |
| [`scripts/prepare_manuscript_for_publish.py`](scripts/prepare_manuscript_for_publish.py) | Copies `book/*.md` into `publish/chapters/` ahead of every Quarto render. |
| [`scripts/validate_book_structure.py`](scripts/validate_book_structure.py) | Checks that `publish/_quarto.yml`'s chapter list and `book/`'s files on disk agree; run in CI. |
| [`publish/`](publish/) | The Quarto book project: `_quarto.yml`, front-matter pages, and the abcjs notation/audio widget (`publish/assets/notation-head.html`). |

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
