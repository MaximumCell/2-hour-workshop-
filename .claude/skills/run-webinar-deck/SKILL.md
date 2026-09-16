---
name: run-webinar-deck
description: Build, run, and screenshot the AI Mastery Workshop reveal.js slide deck, and build the legacy .pptx export. Use when asked to run the deck, start the slide server, take a screenshot of a slide, export the deck to PDF, or build the .pptx.
---

This repo has two deliverables: the reveal.js browser deck in `deck/`
(the primary, editable source of truth — see [deck/README.md](../../../deck/README.md))
and a legacy standalone `.pptx` generator in `build/`. Drive the deck
by starting its static file server, then controlling headless Chromium
via the Playwright driver at
`.claude/skills/run-webinar-deck/driver.mjs`.

All paths below are relative to the repo root.

## Prerequisites

Node 18+ and Python 3 (as `py` on Windows, `python3` elsewhere) on
PATH. Install the driver's dependency and its headless browser once:

```bash
cd .claude/skills/run-webinar-deck
npm install
npx playwright install chromium
```

## Run: the reveal.js deck (agent path)

1. Start the no-cache dev server from `deck/`, in the background:

```bash
cd deck
py serve.py &        # macOS/Linux: python3 serve.py &
timeout 20 bash -c 'until curl -sf http://localhost:8000 >/dev/null; do sleep 0.5; done'
```

2. Drive it with the Playwright driver (from repo root, or adjust the
   path):

```bash
cd .claude/skills/run-webinar-deck
node driver.mjs shot /tmp/shots/title.png        # screenshot slide 1 (title)
node driver.mjs goto 20 /tmp/shots/slide20.png    # jump to slide index 20 (0-based) and screenshot
node driver.mjs next /tmp/shots/next.png          # press ArrowRight, then screenshot
node driver.mjs errors                            # click through 12 slides, print any console errors
node driver.mjs pdf /tmp/shots/deck.pdf           # full ?print-pdf export via browser print
```

Screenshots/PDFs land wherever you point the output path (examples
above use `/tmp/shots/`, create it first with `mkdir -p /tmp/shots`).
`goto <n>` uses reveal.js's URL hash (`#/<n>`), 0-indexed across the
whole deck (title.md is slide 0), not per-section.

| command | what it does |
|---|---|
| `shot <out.png> [n]` | Navigate (to slide `n` if given) and screenshot |
| `next <out.png>` | Press ArrowRight from the current/first slide, then screenshot |
| `goto <n> <out.png>` | Deep-link to `#/<n>` and screenshot |
| `pdf <out.pdf>` | Load `?print-pdf` and save a full-deck browser-rendered PDF |
| `errors` | Step through 12 slides, print any page console errors |

3. Stop the server when done:

```bash
lsof -ti:8000 -sTCP:LISTEN | xargs -r kill   # macOS/Linux
# Windows: find the py serve.py process and kill it, e.g.
#   taskkill //F //IM py.exe
```

## Run: the reveal.js deck (human path)

```bash
cd deck
py serve.py     # or: python3 -m http.server 8000 / npx serve
```

Open `http://localhost:8000`. `S` = speaker view, `F` = fullscreen,
`Esc` = grid overview, `?print-pdf` query param = print-to-PDF layout.
Ctrl-C to stop.

## Build: the legacy .pptx export

```bash
py -m pip install python-pptx
py build/generate_deck.py
```

Output: `output/AI-Mastery-Workshop.pptx`. All content for this path
lives in `build/generate_deck.py` itself (Section 1 through 9), not in
`deck/slides/` — the two decks are maintained independently. Prefer
editing `deck/slides/*.md` (the reveal.js deck) unless you're
specifically asked to update the `.pptx`.

## Test

No automated test suite in this repo. Verification is visual: run the
driver's `shot`/`goto` commands and inspect the PNG, or `errors` to
confirm no JS exceptions during navigation.

---

## Gotchas

- **`python3` is not on PATH on this Windows box** — it resolves to
  the Microsoft Store app-execution-alias stub and exits immediately
  with "Python was not found...". Use `py` instead (both invoke the
  same Python 3.13 install).
- **The driver needs its own `npm install`.** `playwright` is a
  dependency of the driver package in
  `.claude/skills/run-webinar-deck/`, not of the repo root (which has
  no `package.json`) — `npx playwright` alone only gets you the CLI,
  not the importable module `driver.mjs` needs.
- **`goto <n>` is 0-based and counts across the whole deck**, not
  within a section — `title.md` is slide 0, and each subsequent
  `slides/section-NN-*.md` file contributes further indices in the
  order listed in `deck/index.html`.
- **Fresh `nav` needs a settle wait.** reveal.js finishes its slide
  transition/layout a beat after `load` fires; the driver already
  waits ~300ms after `waitForSelector(".present")` — don't strip that
  if you extend the script, or screenshots can catch a mid-transition
  frame.
