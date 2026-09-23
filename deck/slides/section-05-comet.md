<!-- .slide: data-background-color="#141312" class="dark" -->

<div class="mod-num">05</div>
<div class="progress-chip">Section 5 of 13</div>
<div class="lesson-no">Perplexity Comet</div>

## The Agentic Browser

<span class="tag hook">10 min</span>

From AI that answers questions to AI that can perform multi-step browser tasks.

<div class="agent-demo" data-prompt="Find the 3 cheapest flights to Dubai next month and compare them">
<div class="ad-step" data-tab="google.com/flights" data-label="Searching flights" data-pick="0">
<div class="ad-row"><b>flydubai</b><span>Direct · 3h 10m</span><em>PKR 48,200</em></div>
<div class="ad-row"><b>Qatar Airways</b><span>1 stop · 6h 40m</span><em>PKR 55,900</em></div>
<div class="ad-row"><b>Saudia</b><span>1 stop · 7h 15m</span><em>PKR 58,100</em></div>
<div class="ad-row"><b>Emirates</b><span>Direct · 3h 05m</span><em>PKR 62,400</em></div>
</div>
<div class="ad-step" data-tab="skyscanner.com" data-label="Checking Skyscanner" data-pick="1">
<div class="ad-row"><b>Saudia</b><span>1 stop · 7h 15m</span><em>PKR 57,300</em></div>
<div class="ad-row"><b>flydubai</b><span>Direct · 3h 10m</span><em>PKR 47,900</em></div>
<div class="ad-row"><b>Qatar Airways</b><span>1 stop · 6h 40m</span><em>PKR 55,400</em></div>
</div>
<div class="ad-step" data-tab="emirates.com" data-label="Reading Emirates" data-pick="0">
<div class="ad-row"><b>EK 613 · Lahore → Dubai</b><span>Direct · 3h 05m</span><em>PKR 62,400</em></div>
<div class="ad-row"><b>Baggage</b><span>30 kg included</span><em>✓</em></div>
<div class="ad-row"><b>Meals</b><span>Included</span><em>✓</em></div>
</div>
<div class="ad-step" data-tab="Summary" data-label="Comparing prices"></div>
<div class="ad-result"><h4>Top 3 flights to Dubai <em>sample data</em></h4><div class="row"><b>flydubai · direct</b><span class="best">PKR 47,900 · cheapest</span></div><div class="row"><b>Qatar Airways · 1 stop</b><span>PKR 55,400</span></div><div class="row"><b>Emirates · direct</b><span>PKR 62,400 · bags + meals</span></div></div>
</div>

Note: Section title card. This is the first taste of "AI does the task," not just "AI answers the question" — the bridge into agents later in the workshop.

---

<div class="lesson-no">Section 5 · What is an agentic browser?</div>

# Search vs. Delegate

<div class="qa">
<div class="qa-item">
<div class="qa-q">Traditional search</div>
<div class="qa-line"><span class="qa-tag weak">You do the work</span><span class="qa-why">You search → read → click → compare → decide, one step at a time.</span></div>
</div>
<div class="qa-item">
<div class="qa-q">Agentic browser</div>
<div class="qa-line"><span class="qa-tag power">The agent does the work</span><span class="qa-why">You give a goal — the agent navigates, researches, compares, and completes steps with less manual work.</span></div>
</div>
</div>

Note: The value isn't "Comet is another browser" — it's delegating a multi-step knowledge task to an AI system that can interact with the web.

---

<div class="lesson-no">Section 5 · What this looks like</div>

# Comet, Mid-Task

<div class="figure-side"><img src="assets/comet-demo.png" alt="Perplexity Comet completing a multi-step research task" /></div>

Note: A quick still before the live demo, so the room knows what to expect the interface to look like once you switch over.

---

<div class="lesson-no">Section 5 · Live demo</div>

# Delegate a Real Task

<div class="uc-grid">
<div class="uc">Research competitors</div>
<div class="uc">Compare products</div>
<div class="uc">Find potential leads</div>
<div class="uc">Research a travel plan</div>
<div class="uc">Gather info from multiple sites and summarize it</div>
</div>

<span class="demo">Live demo</span>

<p class="rule"><b>Teaching point</b> The value is delegating a multi-step knowledge task, not the browser itself.</p>

Note: Pick one task live — competitor research or a travel plan both land well with a general audience. Keep a backup task ready in case the first one stalls on a slow page load.
