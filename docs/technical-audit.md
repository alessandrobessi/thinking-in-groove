# Technical Audit — Piano Migration

Audited 5 August 2026.

## Current pipeline

1. Authors edit Markdown under `book/` and manually duplicate ABC inside each chapter.
2. `scripts/prepare_manuscript_for_publish.py` replaces `publish/chapters/` with a mirrored copy.
3. Quarto builds HTML, EPUB, and Typst/PDF from `publish/_quarto.yml`.
4. HTML loads abcjs 6.4.4 from jsDelivr through `publish/assets/notation-head.html`.
5. CI validates the chapter list, renders the book, publishes GitHub Pages, and attaches book formats to a rolling release.

## Reusable components

- abcjs already renders ABC and synthesizes playback in the browser.
- The Quarto raw-HTML wrapper is reusable across chapters.
- The preparation and structure-validation scripts give the manuscript a stable source/build split.
- Existing ABC metadata can inform migration even though its bass-only score is insufficient.

## Tab-specific surface

- 30 `.tab.txt` files exist under `examples/` (29 chapter files plus the shared laboratory).
- All 29 legacy chapter pages contain a bass-tab block or reference.
- `scripts/notation.py`, `docs/notation-conventions.md`, `docs/visual-language.md`, `examples/README.md`, `examples/INDEX.md`, and the project README encode tab as required output.
- Tab is content-level, not renderer-generated; removal can proceed per migrated chapter without risking the ABC parser.

## Prototype changes

The shared player now renders two named voices, provides Full/Bass only/Harmony only playback modes, Loop, Restart, three bounded tempos, current-event highlighting, accessible labels/status, mobile horizontal overflow, reduced-motion handling, and graceful audio failure. A comparison wrapper switches A/B panels. Audio initializes only after a user action.

## Known technical risks

- ABC remains duplicated between standalone files and chapter HTML; a build-time include/schema is needed before broad conversion.
- Voice isolation currently relies on stable RH/LH ordering and abcjs `voicesOff`; automated browser coverage must lock this contract down.
- Looping repeats the complete tune, not an arbitrary measure region.
- A/B switching does not yet preserve playhead position.
- CDN dependence means notation cannot initialize offline, although textual content remains available.
- PDF/EPUB intentionally omit interactive HTML and need a future static-score path.

## Mobile assessment

The old widget scaled a score down to container width, risking unreadable notation. The prototype maintains a minimum score width and permits horizontal scrolling. Transport controls wrap and remain adjacent. This is a code-level proof; Safari, Firefox, real-device, and screen-reader checks remain quality-gate work.

## Deployment

`.github/workflows/validate.yml` runs the Python structure validator and an HTML render sanity check. `.github/workflows/build-book.yml` prepares the manuscript, renders the outputs, deploys Pages, and updates the rolling release. No deployment mutation was performed during this audit.
