<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">11</div>
<div class="progress-chip">Section 11 of 13</div>
<div class="lesson-no">Automation with n8n</div>

## Agents vs Automation

<span class="tag hook">15 min</span>

Note: Section title card. This section builds one real, working n8n workflow live — have a backup workflow ready in case of connectivity issues.

---

<div class="lesson-no">Section 11a · What is automation?</div>

# A Defined Process

<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-t">Trigger</div></div>
<div class="step"><div class="step-n">2</div><div class="step-t">Step 1</div></div>
<div class="step"><div class="step-n">3</div><div class="step-t">Step 2</div></div>
<div class="step"><div class="step-n">4</div><div class="step-t">Step 3</div></div>
<div class="step"><div class="step-n">5</div><div class="step-t">Result</div></div>
</div>

<p class="rule"><b>Example</b> New form submission → add lead to CRM → send email → notify sales team.</p>

Note: Automation is predictable and fixed — every run follows the exact same path. That predictability is the setup for the contrast on the next slide.

---

<div class="lesson-no">Section 11b · What is an AI agent?</div>

# A Flexible, Goal-Driven Process

<div class="figure-side"><img src="assets/AI_agent_navigating_toward_goal_202608281245.jpeg" alt="An AI agent navigating toward a goal, adapting as it goes" /></div>

- Goal → decide steps → use tools
- Observe results → adapt → complete task

Note: Same "goal → tools → adapt" loop introduced in Section 9's OpenClaw slide — call that back explicitly.

---

<div class="lesson-no">Section 11 · Side by side</div>

# Automation vs. Agent

<table>
<thead><tr><th>Automation</th><th>AI Agent</th></tr></thead>
<tbody>
<tr><td>Predefined workflow</td><td>Goal-driven workflow</td></tr>
<tr><td>Predictable steps</td><td>Can choose next steps</td></tr>
<tr><td>Great for repetitive processes</td><td>Great for complex/variable tasks</td></tr>
<tr><td>Easier to test</td><td>More flexible, but needs stronger controls</td></tr>
</tbody>
</table>

Note: Anthropic's own agent guidance draws this same distinction — fixed workflow patterns vs. agents that reason, use tools, and adapt their approach. Read the table one row at a time.

---

<div class="lesson-no">Section 11c · Live demo</div>

# One Real n8n Workflow

<p class="rule"><b>Example</b> Lead comes in → AI analyzes lead → classifies intent → generates personalized response → stores lead → notifies salesperson.</p>

<div class="steps">
<div class="step"><div class="step-n">1</div><div class="step-t">Trigger</div></div>
<div class="step"><div class="step-n">2</div><div class="step-t">Data transformation</div></div>
<div class="step"><div class="step-n">3</div><div class="step-t">AI decision / generation step</div></div>
<div class="step"><div class="step-n">4</div><div class="step-t">Action</div></div>
<div class="step"><div class="step-n">5</div><div class="step-t">Final result</div></div>
</div>

<span class="demo">Live demo</span>

<div class="figure-corner"><img src="assets/n8n-screenshot-readme.png" alt="n8n workflow canvas" /></div>

Note: Build one workflow the audience can immediately understand — the lead-response example above works well because everyone recognizes the problem. Explain each node as you add it: what it does and why it's there.

---

<div class="lesson-no">Section 11d · The bigger mental model</div>

# Four Building Blocks

<div class="card-grid">
<div class="stat-card"><div class="sc-val">Prompt</div><div class="sc-lbl">One task</div></div>
<div class="stat-card"><div class="sc-val">Custom GPT</div><div class="sc-lbl">Reusable assistant</div></div>
<div class="stat-card"><div class="sc-val">Agent</div><div class="sc-lbl">AI that pursues a goal using tools</div></div>
<div class="stat-card win"><div class="sc-val">Automation</div><div class="sc-lbl">Repeatable system that runs without manual effort</div></div>
</div>

<p class="rule"><b>Combine them</b> AI-powered automation = agent + automation, together.</p>

Note: This slide ties together Sections 5, 7, 9, and 11 into one clean mental model — worth pausing on, it's the connective tissue for the whole second half of the workshop.
