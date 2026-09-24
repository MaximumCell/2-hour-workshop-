<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">11</div>
<div class="progress-chip">Section 11 of 13</div>
<div class="lesson-no">Automation with n8n</div>

## Agents vs Automation

<span class="tag hook">15 min</span>

See where fixed workflows and flexible agents fit.

- Understand automation as a defined process
- Compare automation with a goal-driven agent
- Build a real lead-response workflow in n8n
- Connect prompts, custom GPTs, agents, and automation

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

<!-- .slide: class="workflow-slide" -->

<div class="lesson-no">Section 11c · Inside an automation</div>

# From Trigger to Result

<div class="automation-demo" aria-label="Animated automation workflow with an AI agent and conditional branches"></div>

Note: An illustrative workflow based on the original n8n screenshot. A chat message triggers the agent. Its model, memory, search and workflow tools support the task; these are supporting connections, not four sequential steps. A condition routes to one outcome per run. Alternate success and needs-attention examples explain branching. The concepts apply across automation platforms, although their interfaces and capabilities differ. Use the numbered controls to pause on a stage before the live n8n build.

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
