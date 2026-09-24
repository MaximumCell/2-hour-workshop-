<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">06</div>
<div class="progress-chip">Section 6 of 13</div>
<div class="lesson-no">Prompting</div>

## Stop Guessing What to Type

<span class="tag hook">15 min</span>

Better context and clearer instructions produce better output.

- Compare weak, good, and 4D prompts on one video-script task
- Use 4D: Define, Describe, Demonstrate, Deliver
- Compare the results live and take the winning script into HeyGen

Note: Section title card. This section produces the actual HeyGen script we'll use live in Section 10 — make sure that connection lands.

---

<div class="lesson-no">Section 6b · The demo task</div>

# One Task, Three Prompt Levels

Create a short promotional video script for our AI workshop.

<div class="prompt-comparison">
<div>
<h3>Level 1 · Bad / Weak</h3>
<div class="codecard">
<div class="cc-bar"><span class="cc-label">Weak prompt</span></div>
<pre><code>Write a script for my AI workshop video.</code></pre>
</div>
<p>No audience, length, tone, structure, or call to action.</p>
</div>
<div>
<h3>Level 2 · Good</h3>
<div class="codecard">
<div class="cc-bar"><span class="cc-label">Good prompt</span></div>
<pre><code>Write a 60-second promotional script for an AI workshop. The audience is beginners who want to learn practical AI skills. Make it engaging, easy to understand, and persuasive. Explain what they will learn and end with a clear call to action to register.</code></pre>
</div>
<p>Defines the audience, length, tone, objective, and call to action.</p>
</div>
</div>

<p class="rule"><b>Next: Level 3</b> Add the 4D framework for a more specific, repeatable result.</p>

Note: Use the same task and model throughout. Run the weak prompt first, then the good prompt, and compare results. The next slide adds 4D. The winning script becomes the real HeyGen input in Section 10.

---

<!-- .slide: class="prompt-reading" -->

<div class="lesson-no">Section 6b · Level 3</div>

# The 4D Framework Prompt

Define → Describe → Demonstrate → Deliver. <span class="reading-hint">Scroll inside the prompt to read all four parts.</span>

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Level 3 — 4D</span></div>

```text
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
