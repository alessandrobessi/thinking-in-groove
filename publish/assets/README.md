# Assets

`notation-head.html` is the abcjs rendering/audio widget used by every
inline musical example in the HTML build — copied over from the
Thinking in Layers companion project unchanged, since it's generic to
any abcjs-rendered `.score-example` block.

## Missing image assets (needed before a full Quarto render)

Not yet created — building `publish/` locally will fail on these until
they're added:

- `cover.png` — full book cover, referenced by `typst-show.typ` (PDF)
  and `_quarto.yml`'s commented-out `cover-image` key (HTML).
- `cover-epub.png` — EPUB-specific cover, referenced by `_quarto.yml`'s
  commented-out `epub-cover-image` key.
- `author.png` — author photo, referenced by `about-the-author.qmd`.

Adding these and un-commenting the two `_quarto.yml` keys is Phase 4/6
work (Multimedia / Publication in `ROADMAP.md`), not this pass.
