# The Slide Deck

This is the single source for the workshop slides. All content lives in the markdown files in the `slides` folder. Edit those files and the deck updates. You do not need to touch the HTML.

## How to view it

The deck loads its slides from separate files, so it needs a small local web server rather than opening the file directly. This is one command.

1. Open a terminal in this `deck` folder.
2. Run one of these:
   - `python3 -m http.server 8000`
   - or, if you have Node, `npx serve`
3. Open `http://localhost:8000` in your browser.

Press `S` for speaker view, which shows your notes and a timer. Press `F` for full screen. Press `Esc` for a grid overview.

## How to edit content

- Each section is one file, for example `slides/section-04-prompt-hack.md`.
- A line with three dashes starts a new slide.
- A line starting with `Note:` starts the speaker notes for that slide. Notes are only visible in speaker view, not on the slide.
- Keep on-screen text short. Put your talking points and demo cues in the notes.

Recurring components (all defined in `theme.css`):

- `<div class="lesson-no">` — the orange, all-caps kicker label at the top of a slide
- `<div class="progress-chip">Section X of 9</div>` — pacing tracker, top right
- `<span class="tag hook">` / `<span class="tag win">` — small colored chips
- `<div class="codecard">…</div>` — dark, editor-style block for long copy-paste prompts (wrap the prompt text in a fenced code block inside it)
- `<div class="promptcard">…</div>` — lighter card for short one-line prompts
- `<div class="card-grid"><div class="stat-card">…` — 2-column stat/callout cards (add `win` for the green treatment)
- `<div class="qa">…` — before/after or weak/power comparison blocks
- `<div class="steps"><div class="step">…` — numbered step sequences for live demos
- `<div class="reveal-box">…` — "the tool is..." punchline reveal
- `<div class="live-badge">…` — bottom-left live-session badge, use on title/section-break slides
- `<div class="placeholder">` / `.placeholder-row` — dashed-border swap-me boxes for photos, logos, screenshots

Wrap a headline word in `<u>…</u>` to get the accent-colored underline treatment, e.g. `# AI IS NOT <u>OPTIONAL</u> ANYMORE`.

## How to restyle everything

Open `theme.css`. The colours and fonts are set at the top under `:root`. Change them once and the whole deck restyles.

Palette: `--accent` orange `#ff7d00`, `--cream` warm off-white `#fff9f4` (default background), `--win` green `#62c41f` (wins/stats/guarantees), `--dark` near-black `#141312` (hook and reveal moments).

## Adding or reordering sections

Each section is one file in `slides/`, referenced by its own `<section data-markdown="...">` line in `index.html`. Add a new file and a matching line to extend the deck, or reorder the `<section>` lines to change slide order.

## Optional security hardening

The deck loads reveal.js from a public CDN, pinned to version 5. For a local presentation this is low risk. If you ever publish the deck on the public web, add Subresource Integrity hashes (`integrity="sha384-..."` and `crossorigin="anonymous"`) to the script and stylesheet tags, or download reveal.js and serve it locally so nothing is fetched from a third party.

## Exporting to PDF

Add `?print-pdf` to the URL, for example `http://localhost:8000/?print-pdf`, then use the browser print dialog and save as PDF.
