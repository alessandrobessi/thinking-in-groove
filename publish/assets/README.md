# Assets

`notation-head.html` is the abcjs rendering/audio widget used by every
inline musical example in the HTML build — copied over from the
Thinking in Layers companion project unchanged, since it's generic to
any abcjs-rendered `.score-example` block.

## Image assets

- `cover.png` — full book cover. Wired up in `_quarto.yml`'s
  `cover-image` key and used unconditionally by `typst-show.typ` (PDF).
- `author.png` — author photo, used by `about-the-author.qmd`.
- `cover-epub.png` — currently a copy of `cover.png`. `_quarto.yml`'s
  `epub-cover-image` key is left commented out: the cover is a dense
  diagram-and-text design meant to be read at full size, and EPUB
  readers typically shrink covers to a small thumbnail, so this asset
  may need a simplified, EPUB-specific crop before enabling that key.
  Revisit as part of Phase 6 (Publication).
