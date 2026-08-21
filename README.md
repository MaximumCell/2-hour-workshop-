# AI Mastery Workshop — Deck

Standalone repo, no connection to the `claude-course` project. Generates a 16:9
`.pptx` for the 2h10m "AI Mastery Workshop" live webinar (MakeFirstMillion series).

## Build it

```
py -m pip install python-pptx
py build/generate_deck.py
```

Output lands at `output/AI-Mastery-Workshop.pptx`.

## Design system

- Primary accent / CTA: `#FF7D00` (orange)
- Background base: `#FFF9F4` (warm off-white) — default for most slides
- Secondary / wins: `#62C41F` (green) — stats, checkmarks, guarantees
- Near-black text: `#1A1A1A`
- Dark near-black slides (`#141312`) reserved for hook, section-break, and
  reveal moments — mixed deliberately with light slides for pacing.

Headline font: Montserrat (bold). Body font: Calibri. Code/prompt blocks:
Consolas on a dark editor-style panel. If Montserrat isn't installed on the
presenting machine, PowerPoint will substitute a default sans and everything
still renders — install Montserrat for the exact intended look.

All code/prompt blocks are real editable text, not images.

## Placeholders to swap before presenting

- Presenter photo (Section 2)
- Guest-channel logos: Kashif Majeed, HBA Services, Lets Uncover, Meet Mughals
- Testimonial screenshots (Section 9)
- Live-demo screen recordings (Sections 6-8, where noted)

## Editing content

All slide content lives in `build/generate_deck.py`, organized by section
(Section 1 through Section 9, matching the workshop run-of-show). Edit the
text/values there and re-run the build command.
