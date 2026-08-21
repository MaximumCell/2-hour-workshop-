<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">05</div>
<div class="progress-chip">Section 5 of 9</div>
<div class="lesson-no">Claude deep dive</div>

## Meet Your Real Thought Partner

<span class="tag hook">0:30 – 0:50</span>

Not a search engine. Not autocomplete. A collaborator that holds context and builds with you.

Note: Section title card. This is the longest single block of the workshop — mental model, a live app build, then the Connectors job-hunting demo.

---

<div class="lesson-no">Section 5 · Mental model</div>

# How Claude actually thinks

- **Context windows** — Claude remembers everything you've told it in this conversation, use that, don't repeat yourself
- **Instructions matter more than the model** — a clear brief beats a "smarter" model with a vague one
- **Claude as thought partner, not search engine** — ask it to reason, critique, and iterate, not just retrieve

Note: Set the frame before the live build. This is the conceptual anchor for everything that follows in this section.

---

<div class="lesson-no">Section 5 · Live build</div>

# From weak ask to working app

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Original Ask</span></div>

```
mujhe ek barber shop ke liye booking app chahiye
```

</div>

Run it through the meta-prompt from Section 4, then paste the result straight into Claude.

<div class="card-grid">
<div class="stat-card"><div class="sc-val">10–15 days</div><div class="sc-lbl">Traditional dev timeline</div></div>
<div class="stat-card win"><div class="sc-val">~2 minutes</div><div class="sc-lbl">Live, with Claude</div></div>
</div>

<span class="demo">Live demo</span>

Note: Build the barber-shop booking app live on screen, start to finish. Let the "10-15 days to 2 minutes" stat land as a visible gap, not just a claim.

---

<div class="lesson-no">Section 5 · Claude Connectors</div>

# Job-hunting on autopilot

<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-t">Upload your resume</div></div>
<div class="step"><div class="step-n">2</div><div class="step-t">Ask Claude to find ~10 remote jobs matching your role & salary target</div></div>
<div class="step"><div class="step-n">3</div><div class="step-t">Connect the Indeed connector → live results appear</div></div>
<div class="step"><div class="step-n">4</div><div class="step-t">Personalize your resume for 4 selected roles</div></div>
</div>

Note: Four-step sequence, walk through it as a numbered demo. The next two slides carry the exact prompts for steps 2 and 4.

---

<div class="lesson-no">Section 5 · Connectors — prompt A</div>

# Find the roles

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Find Jobs</span></div>

```
Find ~10 remote job listings for a [ROLE] with a target salary of
[SALARY]. Prioritize postings from the last 14 days. For each,
return: title, company, salary range, key requirements, and a
direct link.
```

</div>

Note: Fill in ROLE and SALARY live with an audience suggestion for maximum relevance.

---

<div class="lesson-no">Section 5 · Connectors — prompt B</div>

# Personalize for each role

<div class="codecard">
<div class="cc-bar"><span class="cc-dot r"></span><span class="cc-dot y"></span><span class="cc-dot g"></span><span class="cc-label">Personalize Resume</span></div>

```
Using my uploaded resume and the job description for
[ROLE / COMPANY], rewrite my resume summary and top 3 bullet
points to mirror the language and priorities of this specific
posting. Keep every claim true.
```

</div>

Note: Emphasize "keep every claim true" — this is a tailoring prompt, not a fabrication prompt. Run it on one of the 4 selected roles live.
