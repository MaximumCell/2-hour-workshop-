# -*- coding: utf-8 -*-
"""
AI Mastery Workshop — deck generator (MakeFirstMillion series)
Builds a 16:9 .pptx from python-pptx implementing the brand design system:
  - Primary accent:  #FF7D00 (orange)
  - Background base: #FFF9F4 (warm off-white) on most slides
  - Secondary/wins:  #62C41F (green)
  - Near-black text: #1A1A1A
  - High-contrast "hook" slides: near-black bg + orange/off-white text
Run:  py build/generate_deck.py
Output: output/AI-Mastery-Workshop.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

# ---------------------------------------------------------------- palette --
ORANGE = RGBColor(0xFF, 0x7D, 0x00)
BG_LIGHT = RGBColor(0xFF, 0xF9, 0xF4)
GREEN = RGBColor(0x62, 0xC4, 0x1F)
INK = RGBColor(0x1A, 0x1A, 0x1A)
DARK_BG = RGBColor(0x14, 0x13, 0x12)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MUTED = RGBColor(0x6B, 0x64, 0x5C)          # muted body text on light bg
MUTED_ON_DARK = RGBColor(0xC9, 0xC2, 0xB8)
CARD_BORDER = RGBColor(0xEA, 0xDE, 0xCF)
CODE_BG = RGBColor(0x1E, 0x1B, 0x18)
CODE_GREEN = RGBColor(0x8FE39A)  if False else RGBColor(0x8F, 0xE3, 0x9A)
CODE_ORANGE = RGBColor(0xFF, 0xB0, 0x5C)
CODE_TEXT = RGBColor(0xE8, 0xE3, 0xDC)

HEAD_FONT = "Montserrat"
BODY_FONT = "Calibri"
MONO_FONT = "Consolas"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
TOTAL_SECTIONS = 9

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]

# ------------------------------------------------------------- utilities --

def add_slide(bg=BG_LIGHT):
    s = prs.slides.add_slide(BLANK)
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    r.fill.solid()
    r.fill.fore_color.rgb = bg
    r.line.fill.background()
    r.shadow.inherit = False
    # send to back
    sp = r._element
    sp.getparent().remove(sp)
    s.shapes._spTree.insert(2, sp)
    return s


def _set_no_autofit(tf):
    el = tf._txBody
    bodyPr = el.find(qn('a:bodyPr'))
    for tag in ('a:normAutofit', 'a:spAutoFit'):
        e = bodyPr.find(qn(tag))
        if e is not None:
            bodyPr.remove(e)
    bodyPr.append(el.makeelement(qn('a:noAutofit'), {}))


def textbox(slide, x, y, w, h, text, size=18, color=INK, bold=False,
            font=BODY_FONT, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
            spacing=None, line_spacing=1.0, wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    _set_no_autofit(tf)
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = font
        run.font.color.rgb = color
        if spacing is not None:
            _letter_spacing(run, spacing)
    return tb


def _letter_spacing(run, pts):
    rPr = run._r.get_or_add_rPr()
    rPr.set('spc', str(int(pts * 100)))


def rich_textbox(slide, x, y, w, h, runs, size=18, font=BODY_FONT,
                  align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0):
    """runs: list of (text, color, bold) rendered on one paragraph/line."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    _set_no_autofit(tf)
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    for text, color, bold in runs:
        run = p.add_run()
        run.text = text
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = font
        run.font.color.rgb = color
    return tb


def rect(slide, x, y, w, h, fill=None, line_color=None, line_w=Pt(1), shadow=False, radius=None):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    sh = slide.shapes.add_shape(shape_type, x, y, w, h)
    if radius:
        try:
            sh.adjustments[0] = radius
        except Exception:
            pass
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line_color is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line_color
        sh.line.width = line_w
    sh.shadow.inherit = False
    if shadow:
        _soft_shadow(sh)
    return sh


def _soft_shadow(shape):
    spPr = shape._element.spPr
    existing = spPr.find(qn('a:effectLst'))
    if existing is not None:
        spPr.remove(existing)
    xml = (
        '<a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:outerShdw blurRad="180000" dist="30000" dir="5400000" rotWithShape="0">'
        '<a:srgbClr val="1A1A1A"><a:alpha val="18000"/></a:srgbClr>'
        '</a:outerShdw></a:effectLst>'
    )
    from lxml import etree
    spPr.append(etree.fromstring(xml))


def kicker(slide, text, x=Inches(0.7), y=Inches(0.5), color=ORANGE, on_dark=False):
    textbox(slide, x, y, Inches(9), Inches(0.4), text.upper(), size=13, color=color,
            bold=True, font=BODY_FONT, spacing=2.2)


def progress_tag(slide, section_num, total=TOTAL_SECTIONS, on_dark=False):
    c = MUTED_ON_DARK if on_dark else MUTED
    textbox(slide, Inches(10.6), Inches(0.5), Inches(2.2), Inches(0.35),
            f"SECTION {section_num} OF {total}", size=11, color=c, bold=True,
            align=PP_ALIGN.RIGHT, spacing=1.4)


def underline(slide, x, y, w, color=ORANGE, h=Pt(6)):
    rect(slide, x, y, w, h, fill=color)


def headline(slide, text, x=Inches(0.7), y=Inches(1.1), w=Inches(11.9), size=44,
             color=INK, align=PP_ALIGN.LEFT):
    return textbox(slide, x, y, w, Inches(2.2), text, size=size, color=color,
                    bold=True, font=HEAD_FONT, align=align, line_spacing=1.02)


def live_badge(slide, on_dark=True):
    y = Inches(6.9)
    dot_color = ORANGE
    dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.7), y + Inches(0.06), Inches(0.12), Inches(0.12))
    dot.fill.solid(); dot.fill.fore_color.rgb = dot_color
    dot.line.fill.background(); dot.shadow.inherit = False
    color = BG_LIGHT if on_dark else INK
    textbox(slide, Inches(0.92), y, Inches(7), Inches(0.35),
            "LIVE SESSION  |  MAKEFIRSTMILLION SERIES", size=11, color=color,
            bold=True, spacing=1.4)


def footer_page(slide, n):
    textbox(slide, Inches(12.5), Inches(7.08), Inches(0.6), Inches(0.3), str(n),
            size=10, color=MUTED, align=PP_ALIGN.RIGHT)


def stat_card(slide, x, y, w, h, value, label, value_color=ORANGE):
    rect(slide, x, y, w, h, fill=WHITE, line_color=CARD_BORDER, line_w=Pt(1),
         shadow=True, radius=0.06)
    textbox(slide, x + Inches(0.25), y + Inches(0.2), w - Inches(0.5), Inches(0.7),
            value, size=26, color=value_color, bold=True, font=HEAD_FONT)
    textbox(slide, x + Inches(0.25), y + h - Inches(0.65), w - Inches(0.5), Inches(0.5),
            label, size=13, color=MUTED, bold=False)


def code_block(slide, x, y, w, h, lines, label="PROMPT", title_color=CODE_ORANGE):
    rect(slide, x, y, w, h, fill=CODE_BG, radius=0.03, shadow=True)
    # traffic-light dots
    for i, c in enumerate([RGBColor(0xFF, 0x5F, 0x56), RGBColor(0xFF, 0xBD, 0x2E), RGBColor(0x27, 0xC9, 0x3F)]):
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.22) + Inches(0.22) * i, y + Inches(0.18), Inches(0.12), Inches(0.12))
        dot.fill.solid(); dot.fill.fore_color.rgb = c
        dot.line.fill.background(); dot.shadow.inherit = False
    textbox(slide, x + w - Inches(2.3), y + Inches(0.14), Inches(2.05), Inches(0.3),
            label.upper(), size=10.5, color=title_color, bold=True, font=MONO_FONT,
            align=PP_ALIGN.RIGHT, spacing=1.2)
    body = "\n".join(lines)
    textbox(slide, x + Inches(0.3), y + Inches(0.55), w - Inches(0.6), h - Inches(0.75),
            body, size=13, color=CODE_TEXT, font=MONO_FONT, line_spacing=1.25)


def bullets(slide, items, x, y, w, h, size=16, color=INK, gap=0.12, marker_color=ORANGE, bold_marker=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    _set_no_autofit(tf)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap * 72)
        p.line_spacing = 1.15
        r1 = p.add_run(); r1.text = "—  "
        r1.font.size = Pt(size); r1.font.bold = True; r1.font.color.rgb = marker_color; r1.font.name = BODY_FONT
        r2 = p.add_run(); r2.text = item
        r2.font.size = Pt(size); r2.font.color.rgb = color; r2.font.name = BODY_FONT
    return tb


def placeholder_box(slide, x, y, w, h, label):
    rect(slide, x, y, w, h, fill=RGBColor(0xF0, 0xE8, 0xDC), line_color=ORANGE, line_w=Pt(1.25), radius=0.05)
    textbox(slide, x, y + h/2 - Inches(0.25), w, Inches(0.5), f"[ {label} ]", size=13,
            color=ORANGE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def section_break(slide_bg, section_num, kicker_text, title, subtitle=None):
    s = add_slide(bg=DARK_BG)
    kicker(s, kicker_text, color=ORANGE)
    progress_tag(s, section_num, on_dark=True)
    headline(s, title, y=Inches(2.7), size=48, color=BG_LIGHT)
    underline(s, Inches(0.72), Inches(4.35), Inches(2.1), color=ORANGE)
    if subtitle:
        textbox(s, Inches(0.7), Inches(4.65), Inches(10.5), Inches(1.2), subtitle,
                size=18, color=MUTED_ON_DARK, line_spacing=1.3)
    live_badge(s, on_dark=True)
    return s


def content_header(s, section_num, kicker_text, title, title_size=34):
    kicker(s, kicker_text)
    progress_tag(s, section_num)
    headline(s, title, y=Inches(0.95), size=title_size)
    underline(s, Inches(0.72), Inches(0.95) + Inches(0.02) + Emu(int(title_size * 12700 * 1.15)), Inches(1.6))


page_num = [0]

def new_content_slide(section_num, kicker_text, title, title_size=32, bg=BG_LIGHT):
    s = add_slide(bg=bg)
    kicker(s, kicker_text)
    progress_tag(s, section_num)
    headline(s, title, y=Inches(0.95), size=title_size)
    page_num[0] += 1
    footer_page(s, page_num[0])
    return s


# =============================================================================
# SECTION 1 — HOOK & HOUSEKEEPING (0:00-0:05)
# =============================================================================

s = add_slide(bg=DARK_BG)
kicker(s, "AI MASTERY WORKSHOP", color=ORANGE)
headline(s, "AI IS NOT\nOPTIONAL\nANYMORE", y=Inches(1.5), size=64, color=BG_LIGHT)
underline(s, Inches(0.72), Inches(4.55), Inches(2.6), color=ORANGE, h=Pt(8))
textbox(s, Inches(0.72), Inches(4.85), Inches(9.5), Inches(1.3),
        "In the next 2 hours 10 minutes you'll join the top 1% of AI users — run your\n"
        "first automation live, and vibe-code any app you want.",
        size=18, color=MUTED_ON_DARK, line_spacing=1.3)
rect(s, Inches(0.72), Inches(5.9), Inches(8.6), Inches(0.9), fill=RGBColor(0x24, 0x20, 0x1C), radius=0.12)
textbox(s, Inches(1.0), Inches(6.02), Inches(8.1), Inches(0.7),
        "“Awaz clear aa rahi hai? Comment mein bata dijiye.”\n(Confirming audio is clear — drop a comment.)",
        size=14, color=ORANGE, bold=False, line_spacing=1.2)
live_badge(s, on_dark=True)
footer_page(s, 1); page_num[0] = 1

s = add_slide(bg=BG_LIGHT)
kicker(s, "AI MASTERY WORKSHOP")
progress_tag(s, 1)
headline(s, "Before we start...", y=Inches(1.0), size=38)
underline(s, Inches(0.72), Inches(1.85), Inches(2.0))
rect(s, Inches(0.72), Inches(2.4), Inches(6.2), Inches(1.5), fill=WHITE, line_color=ORANGE, line_w=Pt(1.5), radius=0.08, shadow=True)
textbox(s, Inches(1.05), Inches(2.7), Inches(5.6), Inches(0.9),
        "\U0001F4CD  Drop your city in the chat right now", size=20, color=INK, bold=True)
textbox(s, Inches(1.05), Inches(3.15), Inches(5.6), Inches(0.6),
        "Let's see how far this workshop reaches today.", size=14, color=MUTED)
footer_page(s, 2)

# =============================================================================
# SECTION 2 — CREDIBILITY / SELF-INTRO (0:05-0:12)
# =============================================================================

s = new_content_slide(2, "Credibility", "Why Listen to Me?", title_size=36)
placeholder_box(s, Inches(0.72), Inches(2.0), Inches(3.1), Inches(3.6), "PRESENTER PHOTO")
textbox(s, Inches(4.1), Inches(2.15), Inches(4.5), Inches(0.6), "Badar", size=30, color=INK, bold=True, font=HEAD_FONT)
textbox(s, Inches(4.1), Inches(2.75), Inches(6.5), Inches(0.5), "Founder — Aaghaz AI", size=17, color=ORANGE, bold=True)
textbox(s, Inches(4.1), Inches(3.25), Inches(8.3), Inches(1.5),
        "Runs an AI startup studio for US clients. Worked with HeyGen, Higgsfield,\n"
        "Wondershare, and Hostinger. Delivers guest masterclasses on major tech\n"
        "channels. Aaghaz is Asia's first AI startup institute.",
        size=14, color=MUTED, line_spacing=1.3)
cards = [("10,000+", "Students Trained"), ("5+ Years", "AI Engineer → AI Marketing"),
         ("Mini Courses", "On Big Tech Platforms"), ("MakeFirstMillion", "AI Content Channel")]
cx, cy, cw, ch, gap = Inches(4.1), Inches(4.55), Inches(3.9), Inches(1.25), Inches(0.3)
for i, (val, lbl) in enumerate(cards):
    col, row = i % 2, i // 2
    x = cx + col * (cw + gap)
    y = cy + row * (ch + Inches(0.25))
    stat_card(s, x, y, cw, ch, val, lbl)

s = new_content_slide(2, "Credibility", "The Proof", title_size=36)
textbox(s, Inches(0.72), Inches(1.9), Inches(11.9), Inches(0.5),
        "Guest masterclasses on channels reaching hundreds of thousands of AI learners.",
        size=15, color=MUTED)
logos = ["Kashif Majeed", "HBA Services", "Lets Uncover", "Meet Mughals"]
lx, lw, lgap = Inches(0.72), Inches(2.75), Inches(0.3)
for i, name in enumerate(logos):
    x = lx + i * (lw + lgap)
    placeholder_box(s, x, Inches(2.6), lw, Inches(1.6), name.upper() + " LOGO")
rect(s, Inches(0.72), Inches(4.7), Inches(11.9), Inches(1.3), fill=WHITE, line_color=CARD_BORDER, radius=0.06, shadow=True)
textbox(s, Inches(1.05), Inches(4.9), Inches(11.2), Inches(0.9),
        "Want daily proof, not just today's slides?\nFollow the journey on LinkedIn — new wins posted every week.",
        size=16, color=INK, line_spacing=1.3, bold=False)

# =============================================================================
# SECTION 3 — WORKSHOP RULES & COMMITMENT (0:12-0:15)
# =============================================================================

s = new_content_slide(3, "Ground Rules", "Get the Most Out of Today", title_size=34)
tips = ["Pen and paper ready — you'll want to write a few things down",
        "Mobile is fine, but a laptop is better if you plan to build along live"]
bullets(s, tips, Inches(0.72), Inches(2.0), Inches(11.5), Inches(1.5), size=18)

s = new_content_slide(3, "Ground Rules", "There's a Bonus Waiting", title_size=32, bg=DARK_BG)
for tb in s.shapes:
    pass
# override title/kicker colors for dark bg
for shp in list(s.shapes):
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            for r in p.runs:
                if r.font.color.rgb == INK:
                    r.font.color.rgb = BG_LIGHT
rect(s, Inches(0.72), Inches(2.0), Inches(11.9), Inches(4.4), fill=RGBColor(0x24, 0x20, 0x1C),
     line_color=ORANGE, line_w=Pt(1.5), radius=0.05, shadow=True)
textbox(s, Inches(1.1), Inches(2.3), Inches(3.5), Inches(0.5), "\U0001F512  LOCKED", size=16, color=ORANGE, bold=True, spacing=1.5)
unlock_items = ["A curated book list", "The full AI tools stack list", "Live Q&A with direct answers", "A special announcement"]
bullets(s, unlock_items, Inches(1.1), Inches(2.9), Inches(10.8), Inches(2.2), size=18, color=BG_LIGHT)
textbox(s, Inches(1.1), Inches(5.55), Inches(10.8), Inches(0.6),
        "Unlocks only if you stay till the very end.", size=15, color=ORANGE, bold=True)

s = new_content_slide(3, "Ground Rules", "Why No Recording?", title_size=34)
textbox(s, Inches(0.72), Inches(2.1), Inches(11.0), Inches(1.5),
        "This session isn't being recorded on purpose. Learning sticks best when\n"
        "you're fully present, building live, not watching later.",
        size=19, color=INK, line_spacing=1.35)

s = add_slide(bg=DARK_BG)
kicker(s, "Commitment", color=ORANGE)
progress_tag(s, 3, on_dark=True)
headline(s, "Type YES if\nyou're in.", y=Inches(2.4), size=56, color=BG_LIGHT)
underline(s, Inches(0.72), Inches(4.5), Inches(2.0))
live_badge(s, on_dark=True)
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(3, "Today's Roadmap", "What You'll Walk Away With", title_size=32)
recap = ["The 3-second prompt hack", "Custom GPTs / AI employees", "The top 1% tool stack",
         "HeyGen content creation", "Claude mastery", "20 hours of research in 2 minutes",
         "1-minute presentations", "Personal AI agents & automations"]
half = len(recap) // 2
bullets(s, recap[:half], Inches(0.72), Inches(2.0), Inches(5.7), Inches(4.5), size=16, gap=0.22)
bullets(s, recap[half:], Inches(6.6), Inches(2.0), Inches(5.7), Inches(4.5), size=16, gap=0.22)

# =============================================================================
# SECTION 4 — AI FUNDAMENTALS + THE 3-SECOND PROMPT HACK (0:15-0:30)
# =============================================================================

s = section_break(BG_LIGHT, 4, "AI Fundamentals", "The 3-Second Prompt Hack",
                   "Why most people get bad results from AI — and the fix that takes seconds to apply.")
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(4, "Core Concept", "Bad Prompt = Bad Result.\nGood Prompt = Good Result.", title_size=32)
textbox(s, Inches(0.72), Inches(3.3), Inches(11.0), Inches(1.2),
        "The model didn't get worse. Your instructions did all the work — and\n"
        "vague instructions always produce vague output.",
        size=18, color=MUTED, line_spacing=1.3)

s = new_content_slide(4, "Example", "A Weak Prompt", title_size=30)
code_block(s, Inches(0.72), Inches(1.95), Inches(11.9), Inches(2.0),
           ["Role: you are a world class expert youtube hook writer",
            "Context: rewrite my hook, make it more better and attention grabbing",
            "Be creative"], label="Weak Prompt", title_color=RGBColor(0xFF, 0x8A, 0x80))
textbox(s, Inches(0.72), Inches(4.2), Inches(11.0), Inches(1.0),
        "Vague role. No real context. No format. No constraints. The model has to guess\n"
        "what “better” means — so it guesses safely, and safely is boring.",
        size=15, color=MUTED, line_spacing=1.3)

s = new_content_slide(4, "The Hack", "The Meta-Prompt", title_size=30)
meta_lines = [
    "Role: Act as an elite Prompt Engineering Consultant.",
    "Objective: Transform any prompt I provide into a high-performance",
    "prompt that maximizes clarity, accuracy, relevance, and output quality",
    "from AI models.",
    "Process: Understand the original intent. Remove ambiguity and",
    "unnecessary wording. Add missing context where beneficial. Improve",
    "structure and readability. Optimize instructions, constraints, and",
    "output format. Preserve the original meaning and goal.",
    "Deliverables:",
    "1. Optimized Prompt",
    "2. Rationale for Changes",
    "3. Optional Advanced Version (if further optimization is possible)",
    "Original Prompt: {PASTE_PROMPT_HERE}",
]
code_block(s, Inches(0.72), Inches(1.9), Inches(11.9), Inches(5.15), meta_lines, label="The Hack — copy this")

s = new_content_slide(4, "Payoff", "Before vs. After", title_size=32)
rect(s, Inches(0.72), Inches(2.0), Inches(5.7), Inches(4.3), fill=WHITE, line_color=CARD_BORDER, radius=0.05, shadow=True)
textbox(s, Inches(1.0), Inches(2.25), Inches(5.2), Inches(0.4), "WEAK PROMPT OUTPUT", size=12, color=RGBColor(0xC4,0x4A,0x2A), bold=True, spacing=1.2)
textbox(s, Inches(1.0), Inches(2.75), Inches(5.1), Inches(3.3),
        "“Check out this amazing video, you won't\nbelieve what happens next!”\n\n"
        "Generic. Overused. Sounds like every\nother hook on the platform.",
        size=15, color=MUTED, line_spacing=1.35)
rect(s, Inches(6.9), Inches(2.0), Inches(5.7), Inches(4.3), fill=RGBColor(0x24,0x20,0x1C), radius=0.05, shadow=True)
textbox(s, Inches(7.2), Inches(2.25), Inches(5.2), Inches(0.4), "POWER PROMPT OUTPUT", size=12, color=GREEN, bold=True, spacing=1.2)
textbox(s, Inches(7.2), Inches(2.75), Inches(5.1), Inches(3.3),
        "“I spent 40 hours doing this so you don't\nhave to — here's exactly what broke,\nand the 3-line fix.”\n\n"
        "Specific. Personal stakes. Promises a\nconcrete payoff in the first 3 seconds.",
        size=15, color=BG_LIGHT, line_spacing=1.35)

s = new_content_slide(4, "Bonus", "Build a Prompt Library", title_size=32)
textbox(s, Inches(0.72), Inches(2.0), Inches(11.0), Inches(0.7),
        "Never write the same prompt twice. Organize every prompt that works in Notion.",
        size=17, color=MUTED)
cats = [("Scripting", "Hooks, outlines, video scripts"), ("Research", "Deep-dive & summary prompts"),
        ("Marketing", "Ads, captions, funnels")]
cw2 = Inches(3.7); gap2 = Inches(0.35)
for i, (name, desc) in enumerate(cats):
    x = Inches(0.72) + i * (cw2 + gap2)
    rect(s, x, Inches(2.9), cw2, Inches(2.6), fill=WHITE, line_color=CARD_BORDER, radius=0.08, shadow=True)
    rect(s, x + Inches(0.3), Inches(3.15), Inches(0.5), Pt(6), fill=ORANGE)
    textbox(s, x + Inches(0.3), Inches(3.35), cw2 - Inches(0.6), Inches(0.5), name, size=18, color=INK, bold=True, font=HEAD_FONT)
    textbox(s, x + Inches(0.3), Inches(3.9), cw2 - Inches(0.6), Inches(1.3), desc, size=13, color=MUTED, line_spacing=1.3)

# =============================================================================
# SECTION 5 — CLAUDE DEEP DIVE (0:30-0:50)
# =============================================================================

s = section_break(BG_LIGHT, 5, "Claude Deep Dive", "Meet Your Real Thought Partner",
                   "Not a search engine. Not autocomplete. A collaborator that holds context and builds with you.")
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(5, "Mental Model", "How Claude Actually Thinks", title_size=32)
mm = ["Context windows: Claude remembers everything you've told it in this\nconversation — use that, don't repeat yourself",
      "Instructions matter more than the model: a clear brief beats a\n“smarter” model with a vague one",
      "Claude as thought partner, not search engine: ask it to reason,\ncritique, and iterate — not just retrieve"]
bullets(s, mm, Inches(0.72), Inches(2.1), Inches(11.5), Inches(4.5), size=17, gap=0.35)

s = new_content_slide(5, "Live Build", "From Weak Ask to Working App", title_size=30)
code_block(s, Inches(0.72), Inches(1.9), Inches(11.9), Inches(1.3),
           ["mujhe ek barber shop ke liye booking app chahiye"],
           label="Original ask", title_color=RGBColor(0xFF, 0x8A, 0x80))
textbox(s, Inches(0.72), Inches(3.35), Inches(9.5), Inches(0.5), "↓  Run it through the meta-prompt from Section 4, paste into Claude", size=15, color=MUTED)
rect(s, Inches(0.72), Inches(4.0), Inches(5.6), Inches(2.4), fill=WHITE, line_color=CARD_BORDER, radius=0.06, shadow=True)
textbox(s, Inches(1.0), Inches(4.6), Inches(5.0), Inches(1.2),
        "10–15 DAYS", size=30, color=RGBColor(0xC4,0x4A,0x2A), bold=True, font=HEAD_FONT, align=PP_ALIGN.CENTER)
textbox(s, Inches(1.0), Inches(5.5), Inches(5.0), Inches(0.5), "Traditional dev timeline", size=13, color=MUTED, align=PP_ALIGN.CENTER)
rect(s, Inches(6.6), Inches(4.0), Inches(5.6), Inches(2.4), fill=RGBColor(0x24,0x20,0x1C), radius=0.06, shadow=True)
textbox(s, Inches(6.9), Inches(4.6), Inches(5.0), Inches(1.2),
        "~2 MINUTES", size=30, color=GREEN, bold=True, font=HEAD_FONT, align=PP_ALIGN.CENTER)
textbox(s, Inches(6.9), Inches(5.5), Inches(5.0), Inches(0.5), "Live, with Claude", size=13, color=BG_LIGHT, align=PP_ALIGN.CENTER)

s = new_content_slide(5, "Claude Connectors", "Job-Hunting on Autopilot", title_size=30)
steps = ["Upload your resume", "Ask Claude to find ~10 remote jobs matching your role & salary target",
         "Connect the Indeed connector → live results appear", "Personalize your resume for 4 selected roles"]
sy = Inches(1.95)
for i, st in enumerate(steps):
    y = sy + Inches(1.15) * i if i < 2 else None
for i, st in enumerate(steps):
    y = Inches(1.95) + Inches(1.15) * i
    circ = slide_shape = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.72), y, Inches(0.55), Inches(0.55))
    circ.fill.solid(); circ.fill.fore_color.rgb = ORANGE; circ.line.fill.background(); circ.shadow.inherit = False
    tf = circ.text_frame; tf.word_wrap = False
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(i + 1); r.font.bold = True; r.font.size = Pt(18); r.font.color.rgb = WHITE; r.font.name = HEAD_FONT
    textbox(s, Inches(1.5), y + Inches(0.05), Inches(10.8), Inches(0.5), st, size=16, color=INK, anchor=MSO_ANCHOR.MIDDLE)

s = new_content_slide(5, "Connectors — Prompt A", "Find the Roles", title_size=28)
code_block(s, Inches(0.72), Inches(1.9), Inches(11.9), Inches(2.0),
           ["Find ~10 remote job listings for a [ROLE] with a target salary of",
            "[SALARY]. Prioritize postings from the last 14 days. For each, return:",
            "title, company, salary range, key requirements, and a direct link."],
           label="Prompt — find jobs")

s = new_content_slide(5, "Connectors — Prompt B", "Personalize for Each Role", title_size=28)
code_block(s, Inches(0.72), Inches(1.9), Inches(11.9), Inches(2.0),
           ["Using my uploaded resume and the job description for [ROLE / COMPANY],",
            "rewrite my resume summary and top 3 bullet points to mirror the",
            "language and priorities of this specific posting. Keep every claim true."],
           label="Prompt — personalize")

# =============================================================================
# SECTION 6 — LIVE AUTOMATION BUILD (0:50-1:00)
# =============================================================================

s = section_break(BG_LIGHT, 6, "Live Automation", "Build One Real Automation, Live, in n8n",
                   "Something that works while you sleep — built from scratch, on screen, right now.")
page_num[0] += 1; footer_page(s, page_num[0])

# =============================================================================
# SECTION 7 — BUILD ANYTHING FAST (1:00-1:30)
# =============================================================================

s = section_break(BG_LIGHT, 7, "Build Anything Fast", "Research, Slides & Vibe-Coded Sites",
                   "Three tools, three payoffs: deep research in minutes, a live presentation, and a working website.")
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(7, "NotebookLM — 1:00–1:12", "Deep Research, Compressed", title_size=28)
nb_lines = [
    "Act as a senior research analyst. Produce a deep research report on:",
    "\"How many jobs are being lost because of AI?\"",
    "Structure the output as:",
    "1. Executive Summary  2. Key Findings  3. Data & Statistics",
    "4. Industry Breakdown  5. Regional Differences  6. Counterarguments",
    "7. Expert Opinions  8. Historical Precedent  9. Near-Term Outlook",
    "10. Practical Takeaways  11. References / Sources",
]
code_block(s, Inches(0.72), Inches(1.85), Inches(11.9), Inches(3.6), nb_lines, label="Deep Research prompt")
textbox(s, Inches(0.72), Inches(5.65), Inches(11.5), Inches(0.6),
        "Then: paste a podcast link → summarize it → ask follow-up questions, all inside NotebookLM.",
        size=14, color=MUTED)

s = new_content_slide(7, "NotebookLM", "One Source, Four Formats", title_size=30)
feats = [("\U0001F5FA  Mind Map", "Visual breakdown of every key idea"),
         ("\U0001F4CA  Infographic", "Shareable summary, ready to post"),
         ("\U0001F3AC  Generated Video", "A narrated walkthrough of the research"),
         ("\U0001F3A7  Audio Overview", "A podcast-style discussion of your topic")]
fw, fh, fgap = Inches(5.7), Inches(1.7), Inches(0.3)
for i, (name, desc) in enumerate(feats):
    col, row = i % 2, i // 2
    x = Inches(0.72) + col * (fw + fgap)
    y = Inches(2.0) + row * (fh + Inches(0.25))
    rect(s, x, y, fw, fh, fill=WHITE, line_color=CARD_BORDER, radius=0.06, shadow=True)
    textbox(s, x + Inches(0.3), y + Inches(0.25), fw - Inches(0.6), Inches(0.5), name, size=18, color=INK, bold=True, font=HEAD_FONT)
    textbox(s, x + Inches(0.3), y + Inches(0.85), fw - Inches(0.6), Inches(0.7), desc, size=13, color=MUTED, line_spacing=1.3)

s = new_content_slide(7, "1:12–1:20", "Research → 1-Minute Presentation", title_size=28)
textbox(s, Inches(0.72), Inches(2.0), Inches(11.2), Inches(0.8),
        "Take the NotebookLM research from the last step and paste it straight into\na presentation builder.",
        size=17, color=MUTED, line_spacing=1.3)
rect(s, Inches(0.72), Inches(3.1), Inches(11.9), Inches(2.6), fill=DARK_BG, radius=0.05, shadow=True)
textbox(s, Inches(0.72), Inches(3.5), Inches(11.9), Inches(0.5), "THE TOOL IS...", size=14, color=MUTED_ON_DARK, bold=True, align=PP_ALIGN.CENTER, spacing=2)
textbox(s, Inches(0.72), Inches(4.1), Inches(11.9), Inches(1.0), "Genspark / Chronicle", size=40, color=ORANGE, bold=True, font=HEAD_FONT, align=PP_ALIGN.CENTER)
textbox(s, Inches(0.72), Inches(5.15), Inches(11.9), Inches(0.5), "A full presentation, built in under a minute.", size=15, color=BG_LIGHT, align=PP_ALIGN.CENTER)

s = new_content_slide(7, "1:20–1:30", "Vibe-Coded Website — Stitch → AI Studio", title_size=27)
code_block(s, Inches(0.72), Inches(1.85), Inches(11.9), Inches(2.1),
           ["Redesign the landing page at aaghaz.ai/programs/ai-workshop for a",
            "premium, high-conversion feel. Warm off-white background, bold",
            "orange accent, heavy display headline font, card-based sections,",
            "clear CTA above the fold. Keep the copy, change the design system."],
           label="Redesign prompt")
textbox(s, Inches(0.72), Inches(4.15), Inches(11.5), Inches(0.5), "Stitch produces the design.", size=15, color=MUTED, bold=True)
textbox(s, Inches(0.72), Inches(4.6), Inches(11.5), Inches(0.5), "Export to Google AI Studio → a live, working site.", size=15, color=MUTED, bold=True)
rect(s, Inches(0.72), Inches(5.3), Inches(11.9), Inches(1.1), fill=RGBColor(0x24,0x20,0x1C), radius=0.06, shadow=True)
textbox(s, Inches(0.72), Inches(5.55), Inches(11.9), Inches(0.6), "This is what “vibe code any app you want” means.", size=18, color=ORANGE, bold=True, align=PP_ALIGN.CENTER)

# =============================================================================
# SECTION 8 — HEYGEN DEEP DIVE (1:30-1:50)
# =============================================================================

s = section_break(BG_LIGHT, 8, "HeyGen Deep Dive", "Studio-Quality Content, No Studio",
                   "AI avatars, cloned voices, and instant localization — built on real production work.")
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(8, "Why HeyGen", "Replaces a Full Production Team", title_size=30)
why = ["AI avatars that deliver your script on camera, without a camera",
       "Voice cloning — your voice, at any scale",
       "Multi-language localization from a single script",
       "Studio-quality output without a studio",
       "Built on direct production work with the HeyGen team"]
bullets(s, why, Inches(0.72), Inches(2.0), Inches(11.5), Inches(4.5), size=17, gap=0.28)

s = new_content_slide(8, "Live Walkthrough", "Inside the HeyGen Studio", title_size=30)
libs = [("Avatar Library", "Dozens of realistic presenters to choose from"),
        ("Voice Library", "Match tone, language, and accent to your brand"),
        ("Project Templates", "Start from a layout instead of a blank canvas")]
lw2 = Inches(3.75); lgap2 = Inches(0.3)
for i, (name, desc) in enumerate(libs):
    x = Inches(0.72) + i * (lw2 + lgap2)
    rect(s, x, Inches(2.2), lw2, Inches(2.6), fill=WHITE, line_color=CARD_BORDER, radius=0.07, shadow=True)
    textbox(s, x + Inches(0.3), Inches(2.5), lw2 - Inches(0.6), Inches(0.6), name, size=17, color=INK, bold=True, font=HEAD_FONT)
    textbox(s, x + Inches(0.3), Inches(3.15), lw2 - Inches(0.6), Inches(1.4), desc, size=13, color=MUTED, line_spacing=1.3)

s = new_content_slide(8, "Live Build", "Script → Finished Video", title_size=30)
seq = ["Script input", "Avatar selection", "Voice pairing", "Render & preview"]
seg_w = Inches(2.75); gap3 = Inches(0.2)
for i, st in enumerate(seq):
    x = Inches(0.72) + i * (seg_w + gap3)
    fill = ORANGE if i == len(seq) - 1 else WHITE
    txt_color = WHITE if i == len(seq) - 1 else INK
    rect(s, x, Inches(2.6), seg_w, Inches(1.4), fill=fill, line_color=CARD_BORDER if fill == WHITE else None, radius=0.1, shadow=True)
    textbox(s, x, Inches(3.05), seg_w, Inches(0.5), st, size=14, color=txt_color, bold=True, align=PP_ALIGN.CENTER)
    if i < len(seq) - 1:
        textbox(s, x + seg_w, Inches(2.95), gap3, Inches(0.6), "→", size=20, color=ORANGE, align=PP_ALIGN.CENTER)
placeholder_box(s, Inches(0.72), Inches(4.5), Inches(11.9), Inches(2.0), "LIVE DEMO / FINISHED CONTENT REVEAL")

s = new_content_slide(8, "Why This Matters", "Scale Without Filming", title_size=30)
matters = ["Produce content at scale without ever picking up a camera",
           "Localize instantly into any language your audience speaks",
           "Fits directly into the automated content pipeline from Section 6"]
bullets(s, matters, Inches(0.72), Inches(2.1), Inches(11.5), Inches(4.0), size=18, gap=0.35)

# =============================================================================
# SECTION 9 — OUTRO & PROGRAM REVEAL (1:50-2:10)
# =============================================================================

s = add_slide(bg=DARK_BG)
kicker(s, "Wrapping Up", color=ORANGE)
progress_tag(s, 9, on_dark=True)
headline(s, "Everything today was\nmaybe 2% of AI.", y=Inches(2.4), size=42, color=BG_LIGHT)
underline(s, Inches(0.72), Inches(3.85), Inches(2.2))
rect(s, Inches(0.72), Inches(4.4), Inches(6.5), Inches(1.1), fill=ORANGE, radius=0.15, shadow=True)
textbox(s, Inches(0.72), Inches(4.65), Inches(6.5), Inches(0.6), "Type ME in the chat if you want to see the rest.", size=17, color=INK, bold=True, align=PP_ALIGN.CENTER)
live_badge(s, on_dark=True)
page_num[0] += 1; footer_page(s, page_num[0])

s = add_slide(bg=DARK_BG)
kicker(s, "The Reveal", color=ORANGE)
progress_tag(s, 9, on_dark=True)
textbox(s, Inches(0.72), Inches(1.7), Inches(11.5), Inches(0.5), "INTRODUCING", size=16, color=MUTED_ON_DARK, bold=True, spacing=2)
headline(s, "3-Month AI\nHands-On Program", y=Inches(2.2), size=48, color=BG_LIGHT)
underline(s, Inches(0.72), Inches(3.85), Inches(2.6))
stats3 = [("40+", "Hours of Content"), ("30+", "Tools Mastered"), ("1", "Completion Certificate")]
sw = Inches(3.7); sgap = Inches(0.35)
for i, (val, lbl) in enumerate(stats3):
    x = Inches(0.72) + i * (sw + sgap)
    rect(s, x, Inches(4.5), sw, Inches(1.9), fill=RGBColor(0x24,0x20,0x1C), radius=0.08, shadow=True)
    textbox(s, x, Inches(4.8), sw, Inches(0.8), val, size=40, color=ORANGE, bold=True, font=HEAD_FONT, align=PP_ALIGN.CENTER)
    textbox(s, x, Inches(5.65), sw, Inches(0.5), lbl, size=13, color=BG_LIGHT, align=PP_ALIGN.CENTER)
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(9, "The Curriculum", "5 Modules, Start to Finish", title_size=30)
modules = ["AI Fundamentals & Ethics", "ChatGPT / Claude / Gemini Mastery & Prompt Engineering",
           "AI Content Creation System", "AI Agents & Freelance Income",
           "No-Code AI Development & Client-Ready Websites"]
my = Inches(1.95)
for i, m in enumerate(modules):
    y = my + Inches(0.92) * i
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.72), y, Inches(0.5), Inches(0.5))
    circ.fill.solid(); circ.fill.fore_color.rgb = ORANGE; circ.line.fill.background(); circ.shadow.inherit = False
    tf = circ.text_frame; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = str(i + 1); r.font.bold = True; r.font.size = Pt(16); r.font.color.rgb = WHITE; r.font.name = HEAD_FONT
    textbox(s, Inches(1.45), y + Inches(0.03), Inches(10.8), Inches(0.5), m, size=16, color=INK, anchor=MSO_ANCHOR.MIDDLE)
    if i < len(modules) - 1:
        rect(s, Inches(0.955), y + Inches(0.5), Pt(2), Inches(0.42), fill=CARD_BORDER)

s = add_slide(bg=DARK_BG)
kicker(s, "The Offer", color=ORANGE)
progress_tag(s, 9, on_dark=True)
textbox(s, Inches(0.72), Inches(1.6), Inches(11.5), Inches(0.5), "WORKSHOP-ONLY PRICE — FIRST 40 PEOPLE", size=14, color=MUTED_ON_DARK, bold=True, spacing=1.5)
rich_textbox(s, Inches(0.72), Inches(2.1), Inches(11.5), Inches(0.9),
             [("PKR 436,000", MUTED_ON_DARK, True)], size=30, font=HEAD_FONT)
# strikethrough via line
rect(s, Inches(0.75), Inches(2.42), Inches(3.3), Pt(3), fill=RGBColor(0x8a,0x5a,0x3a))
rich_textbox(s, Inches(0.72), Inches(2.85), Inches(11.5), Inches(1.6),
             [("PKR 48,899", ORANGE, True)], size=70, font=HEAD_FONT)
textbox(s, Inches(0.72), Inches(4.55), Inches(11.5), Inches(0.5), "3 easy installments: PKR 10,000  /  15,600  /  15,600", size=16, color=BG_LIGHT)
rect(s, Inches(0.72), Inches(5.25), Inches(4.4), Inches(0.7), fill=GREEN, radius=0.2)
textbox(s, Inches(0.72), Inches(5.42), Inches(4.4), Inches(0.4), "SAVE OVER 88%", size=15, color=INK, bold=True, align=PP_ALIGN.CENTER)
page_num[0] += 1; footer_page(s, page_num[0])

s = new_content_slide(9, "Zero Risk", "100% Money-Back Guarantee", title_size=32)
rect(s, Inches(0.72), Inches(2.1), Inches(11.9), Inches(1.6), fill=RGBColor(0xEE,0xF8,0xE4), line_color=GREEN, line_w=Pt(1.5), radius=0.08)
textbox(s, Inches(1.05), Inches(2.35), Inches(11.2), Inches(1.1),
        "If you don't feel this program is worth it, request a refund — no lengthy\nforms, no runaround. That's the whole process.",
        size=17, color=INK, line_spacing=1.35)

s = new_content_slide(9, "Bonuses", "Included at No Extra Cost", title_size=32)
bon = [("Client Acquisition System", "A repeatable framework for landing your first paying clients"),
       ("Sales Call Mastery", "How to run a sales call that closes, without feeling salesy")]
bw = Inches(5.7); bgap = Inches(0.4)
for i, (name, desc) in enumerate(bon):
    x = Inches(0.72) + i * (bw + bgap)
    rect(s, x, Inches(2.2), bw, Inches(3.0), fill=WHITE, line_color=CARD_BORDER, radius=0.07, shadow=True)
    rect(s, x + Inches(0.3), Inches(2.5), Inches(0.5), Pt(6), fill=ORANGE)
    textbox(s, x + Inches(0.3), Inches(2.7), bw - Inches(0.6), Inches(0.6), name, size=19, color=INK, bold=True, font=HEAD_FONT)
    textbox(s, x + Inches(0.3), Inches(3.4), bw - Inches(0.6), Inches(1.5), desc, size=14, color=MUTED, line_spacing=1.35)

s = new_content_slide(9, "Social Proof", "What Students Say", title_size=32)
placeholder_box(s, Inches(0.72), Inches(2.0), Inches(3.75), Inches(2.3), "TESTIMONIAL SCREENSHOT")
placeholder_box(s, Inches(4.62), Inches(2.0), Inches(3.75), Inches(2.3), "TESTIMONIAL SCREENSHOT")
placeholder_box(s, Inches(8.52), Inches(2.0), Inches(3.75), Inches(2.3), "TESTIMONIAL SCREENSHOT")
rect(s, Inches(0.72), Inches(4.6), Inches(11.9), Inches(1.1), fill=RGBColor(0x24,0x20,0x1C), radius=0.1, shadow=True)
textbox(s, Inches(0.72), Inches(4.88), Inches(11.9), Inches(0.6), "●  31 slots booked — 19 left", size=20, color=ORANGE, bold=True, align=PP_ALIGN.CENTER)

s = new_content_slide(9, "Worst Case", "The Only Two Outcomes", title_size=32)
oc = [("Worst case", "You don't love it — you get a full refund."),
      ("Best case", "You walk away with a new skillset in 3 months.")]
ow = Inches(5.7); ogap = Inches(0.4)
for i, (name, desc) in enumerate(oc):
    x = Inches(0.72) + i * (ow + ogap)
    fill = WHITE if i == 0 else RGBColor(0xEE,0xF8,0xE4)
    border = CARD_BORDER if i == 0 else GREEN
    rect(s, x, Inches(2.3), ow, Inches(2.5), fill=fill, line_color=border, line_w=Pt(1.5), radius=0.07, shadow=True)
    textbox(s, x + Inches(0.3), Inches(2.6), ow - Inches(0.6), Inches(0.5), name.upper(), size=13, color=MUTED, bold=True, spacing=1.5)
    textbox(s, x + Inches(0.3), Inches(3.15), ow - Inches(0.6), Inches(1.4), desc, size=18, color=INK, bold=True, line_spacing=1.3)
textbox(s, Inches(0.72), Inches(5.1), Inches(11.9), Inches(0.6), "Zero real risk, either way.", size=17, color=MUTED, align=PP_ALIGN.CENTER)

s = add_slide(bg=DARK_BG)
kicker(s, "Closing", color=ORANGE)
progress_tag(s, 9, on_dark=True)
headline(s, "Let's Talk.\nLive Q&A.", y=Inches(2.6), size=54, color=BG_LIGHT)
underline(s, Inches(0.72), Inches(4.1), Inches(2.2))
textbox(s, Inches(0.72), Inches(4.4), Inches(10.5), Inches(0.7), "First 40 people get the workshop price. It closes when the timer does.", size=17, color=MUTED_ON_DARK)
live_badge(s, on_dark=True)
page_num[0] += 1; footer_page(s, page_num[0])

# ------------------------------------------------------------------- save --
import os
out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "AI-Mastery-Workshop.pptx")
prs.save(out_path)
print(f"Saved {len(prs.slides)} slides -> {out_path}")
