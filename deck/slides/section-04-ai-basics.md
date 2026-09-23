<div class="lesson-no">Section 4a · What is AI?</div>

# What is AI?

AI is a broad category of software that can **recognize patterns, learn from data, and produce useful outputs**. It is not one single tool or product — it's the larger category that contains different models and systems.

<div class="uc-grid">
<div class="uc">A map app reroutes you around traffic</div>
<div class="uc">A bank flags an unusual purchase</div>
<div class="uc">A customer-support chatbot answers common questions</div>
<div class="uc">A recommendation system predicts what you'll want next</div>
</div>

Note: Uses the OpenAI Academy definition as the foundation rather than the older dictionary-style definition. All four examples are things the room already uses daily — the point is AI has been invisible in their life for years already.

---

<div class="lesson-no">Section 4a.1 · The mental model</div>

# AI → Model → LLM → ChatGPT

<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-t"><strong>AI</strong> — the overall field / category</div></div>
<div class="step"><div class="step-n">2</div><div class="step-t"><strong>Models</strong> — trained systems that perform particular tasks</div></div>
<div class="step"><div class="step-n">3</div><div class="step-t"><strong>LLMs</strong> — models specialized in understanding and generating language</div></div>
<div class="step"><div class="step-n">4</div><div class="step-t"><strong>ChatGPT</strong> — a product/interface that lets people use an LLM effectively</div></div>
</div>

<p class="rule"><b>Key takeaway</b> Don't think of AI as one tool. Think of it as an ecosystem of models and products designed for different kinds of work.</p>

<a class="link-pill" href="https://academy.openai.com/" target="_blank" rel="noopener"><span class="lp-src">OpenAI Academy ·</span> AI Fundamentals</a>

Note: This is the single most important mental model of the section — everything else builds on it. Read it as a chain, top to bottom, pausing on "ChatGPT is a product, not the model itself."

---

<div class="lesson-no">Section 4b · Evolution</div>

# From Rules to Generative AI

<div class="steps">
<div class="step"><div class="step-n">1990s</div><div class="step-t">Spam filters and rule-based systems</div></div>
<div class="step"><div class="step-n">1997</div><div class="step-t">Deep Blue defeats chess champion Garry Kasparov</div></div>
<div class="step"><div class="step-n">2000s</div><div class="step-t">Search ranking and information retrieval mature</div></div>
<div class="step"><div class="step-n">2010s</div><div class="step-t">Recommendation systems, computer vision, Face ID, speech recognition mature</div></div>
<div class="step"><div class="step-n">2020s</div><div class="step-t">Generative AI produces text, images, audio, video, and code</div></div>
</div>

<p class="rule"><b>Why now?</b> Three pieces came together: enormous computing power, huge amounts of data, and modern architectures like transformers.</p>

Note: Move through the timeline quickly, this is context not a history lesson. Land hard on the "why now" line — that's the actual teaching point.

---

<div class="lesson-no">Section 4c · The AI hierarchy</div>

# AI → ML → Deep Learning → GenAI / LLMs

<div class="figure-side"><img src="assets/ai-hierarchy-diagram.png" alt="AI, Machine Learning, Deep Learning, and Generative AI shown as nested layers" /></div>

- **AI** — the broad outer layer
- **Machine Learning** — learns patterns from data
- **Deep Learning** — ML using neural networks
- **Generative AI / LLMs** — the innermost layer, creates new content

<p class="rule"><b>Takeaway</b> These aren't separate competing categories — they're nested layers of one stack.</p>

Note: This is the "zoom out" slide — connect it explicitly back to 4a.1's AI→Model→LLM chain, they're the same idea from two angles.

---

<div class="lesson-no">Section 4f · What is an LLM?</div>

# Large Language Model

An LLM is a type of AI model trained on very large amounts of text and other data to understand and generate language. The models behind tools like ChatGPT and Claude are examples.

<p class="rule"><b>Mental model</b> An LLM takes the context you give it, processes the relationships between the tokens, and generates a response one token at a time.</p>

<p class="rule"><b>Important distinction</b> ChatGPT or Claude are applications that use models — an LLM is the underlying model technology.</p>

Note: The distinction between "the app" and "the model underneath it" is subtle but important — it's what makes the AI→Model→LLM→ChatGPT chain from 4a.1 click for people.

---

<div class="lesson-no">Section 4g · How LLMs work</div>

# The Five-Step Loop

<div class="figure-side"><img src="assets/llm-loop-diagram.png" alt="Tokenize, embed, attend, predict, loop diagram" /></div>

<p class="rule"><b>Core takeaway</b> An LLM generates language by repeatedly predicting the next token based on context — not simple "autocomplete." Modern models can perform complex reasoning-like behavior through learned representations and computation.</p>

Note: Keep this simple and don't get stuck on the "just autocomplete" framing — the rule at the bottom is the correction to that common misconception, land on it clearly.

---

<div class="lesson-no">Section 4h · Narrow AI vs AGI</div>

# Narrow AI vs AGI

<div class="qa">
<div class="qa-item">
<div class="qa-q">Narrow AI</div>
<div class="qa-line"><span class="qa-tag power">What exists today</span><span class="qa-why">Powerful at defined tasks, not generally intelligent across every domain.</span></div>
</div>
<div class="qa-item">
<div class="qa-q">AGI</div>
<div class="qa-line"><span class="qa-tag weak">Not a settled, existing system</span><span class="qa-why">The long-term idea of broad, human-level intelligence that transfers across domains.</span></div>
</div>
</div>

<p class="rule"><b>Why it matters</b> This distinction becomes important later when we discuss agents and OpenClaw.</p>

Note: Be precise here — AGI does not currently exist as a settled, universally agreed-upon system. This sets up Section 9 correctly, don't overstate what agents can do.

---

<div class="lesson-no">Section 4i · Limitations</div>

# AI Limitations

- Hallucinations / incorrect information
- Knowledge may be outdated depending on the model/tool
- Prompt and context quality affect output quality
- AI can sound confident even when wrong

<p class="rule"><b>Rule</b> Use AI for leverage, but verify important information.</p>

Note: Close the section on this grounded, practical note before moving into prompting — it earns trust to show the limits, not just the wins.
