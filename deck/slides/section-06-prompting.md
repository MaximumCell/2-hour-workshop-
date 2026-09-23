<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">06</div>
<div class="progress-chip">Section 6 of 13</div>
<div class="lesson-no">Prompting</div>

## Stop Guessing What to Type

<span class="tag hook">15 min</span>

A repeatable framework for talking to AI — one you'll reuse for the rest of today.

Note: Section title card. This section produces the actual HeyGen script we'll use live in Section 10 — make sure that connection lands.

---

<div class="lesson-no">Section 6a · Core principle</div>

# Bad Input, Unpredictable Output

Better context + clearer instructions → better output.

Prompting is increasingly part of a broader skill: giving AI the right **task, context, examples, constraints, and output requirements**.

Note: Set this up as the thesis for the whole section before the demo — everything that follows just proves this one line.

---

<div class="lesson-no">Section 6b · The demo task</div>

# One Task, Three Prompt Levels

Same task throughout, so the difference is impossible to miss.

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">The Task</span></div>

```
Create a HeyGen script for a short promotional video for our
AI workshop.
```

</div>

Note: This exact task carries through the rest of the section, and its winning output becomes the real script used live in Section 10 — say that out loud now so the room knows this isn't just an exercise.

---

<div class="lesson-no">Section 6b · Level 1</div>

# Bad / Weak Prompt

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Level 1 — Weak</span></div>

```
Write a script for my AI workshop video.
```

</div>

<div class="uc-grid">
<div class="uc">No clear objective</div>
<div class="uc">No audience</div>
<div class="uc">No context about the workshop</div>
<div class="uc">No tone or style</div>
<div class="uc">No length</div>
<div class="uc">No structure</div>
<div class="uc">No CTA or success criteria</div>
</div>

Note: Run this one live first so the room sees the generic output before anything else. Let the weakness be self-evident from the result, then walk the checklist of what's missing.

---

<div class="lesson-no">Section 6b · Level 2</div>

# Good Prompt

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Level 2 — Good</span></div>

```
Write a 60-second promotional script for an AI workshop. The
audience is beginners who want to learn practical AI skills. Make
it engaging, easy to understand, and persuasive. Explain what they
will learn and end with a clear call to action to register.
```

</div>

<div class="uc-grid">
<div class="uc">The task is clearer</div>
<div class="uc">Audience is defined</div>
<div class="uc">Length is specified</div>
<div class="uc">Tone and objective are clearer</div>
<div class="uc">CTA is included</div>
</div>

Note: Run this live too and compare the output directly against Level 1 — the room should visibly see the jump in quality already, before the 4D version even shows up.

---

<div class="lesson-no">Section 6b · Level 3</div>

# The 4D Framework Prompt

Define → Describe → Demonstrate → Deliver.

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Level 3 — 4D</span></div>

```
DEFINE
Create a 60-second promotional video script for our AI workshop.
The goal is to make viewers understand the value of attending and
motivate them to register.

DESCRIBE
The audience is beginners, professionals, creators, freelancers,
and business owners who want to use AI practically but feel
overwhelmed by the number of tools. The workshop covers AI
fundamentals, prompting, agentic browsers, custom GPTs, Claude app
building, AI video creation, agents, automation, and selling AI
skills. Keep the language beginner-friendly, energetic, credible,
and easy to speak naturally on camera.

DEMONSTRATE
Use this structure as the model:
1. Hook that creates curiosity
2. Identify the audience's problem
3. Show what they will learn
4. Give one concrete transformation/example
5. Finish with a strong CTA
Avoid generic AI buzzwords and exaggerated claims. Write
conversationally, as if a real instructor is speaking directly to
the viewer.

DELIVER
Return one polished 60-second HeyGen-ready script. Use short
spoken sentences, natural pauses, and clear paragraph breaks. Do
not include stage directions unless useful for the avatar/video
production. End with a direct registration CTA.
```

</div>

Note: This is the longest prompt of the whole workshop — give the room a moment to actually copy it (Copy button top-right of the block). This exact prompt's output becomes the real Section 10 HeyGen script.

---

<div class="lesson-no">Section 6c · Live comparison</div>

# All Three, Side by Side

<div class="qa">
<div class="qa-item">
<div class="qa-q">Bad prompt</div>
<div class="qa-line"><span class="qa-tag weak">Generic and unpredictable</span><span class="qa-why">No task, no audience, no constraints — the model has to guess.</span></div>
</div>
<div class="qa-item">
<div class="qa-q">Good prompt</div>
<div class="qa-line"><span class="qa-tag weak">Much more useful</span><span class="qa-why">Task and context are clearer, but still generic in places.</span></div>
</div>
<div class="qa-item">
<div class="qa-q">4D prompt</div>
<div class="qa-line"><span class="qa-tag power">Structured and specific</span><span class="qa-why">Repeatable, and aligned to the exact output needed.</span></div>
</div>
</div>

<span class="demo">Live demo</span>

Note: Run all three against the same model, paste outputs side by side on screen if possible. This is the moment the whole section has been building to — let the difference speak for itself.
