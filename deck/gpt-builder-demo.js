/* An illustrative local walkthrough; no requests or real account actions. */
(function () {
  window.initGptBuilderDemos = function () {
    document.querySelectorAll('.gpt-builder-demo').forEach(function (demo) {
      demo.innerHTML = `<div class="gb-window">
        <div class="gb-title"><span><b>GPT Builder</b> <small>Illustrative walkthrough</small></span><button class="gb-play" type="button">Pause</button></div>
        <div class="gb-tabs"><b>Configure</b><span>Preview</span></div>
        <div class="gb-columns"><div class="gb-settings">
          <div class="gb-field" data-field="0"><label>Name</label><div class="gb-value gb-name"></div></div>
          <div class="gb-field" data-field="1"><label>Instructions</label><div class="gb-value gb-instructions"></div></div>
          <div class="gb-field" data-field="2"><label>Knowledge</label><div class="gb-value gb-file"></div></div>
        </div><div class="gb-preview" data-field="3"><div class="gb-avatar">✦</div><b>AI Content Strategist</b><p class="gb-placeholder">Test your assistant here</p><div class="gb-question"></div><div class="gb-answer"></div></div></div>
        <div class="gb-caption"></div></div>
        <div class="gb-steps">${['Name','Instructions','Knowledge','Test'].map((s,i)=>`<button type="button" data-step="${i}"><span>${i+1}</span> ${s}</button>`).join('')}</div>`;
      var step = 0, timer = null, active = false;
      var paused = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var play = demo.querySelector('.gb-play');
      var captions = ['Give your assistant a clear job.', 'Set the role, workflow, and output rules.', 'Add reference material it can use.', 'Try a real request. Review and refine.'];
      function render() {
        demo.querySelector('.gb-name').textContent = 'AI Content Strategist';
        demo.querySelector('.gb-instructions').textContent = step >= 1 ? 'Help creators plan LinkedIn content. Ask about their audience and goal. Return 3 ideas with a hook and a clear next step.' : 'Describe how your assistant should work…';
        demo.querySelector('.gb-file').textContent = step >= 2 ? '✓ Brand-guide.pdf' : '+ Upload reference files';
        demo.querySelector('.gb-placeholder').hidden = step >= 3;
        demo.querySelector('.gb-question').textContent = step >= 3 ? 'Give me 3 post ideas about AI for busy professionals.' : '';
        demo.querySelector('.gb-answer').innerHTML = step >= 3 ? '<small>Example response</small><strong>3 ideas, ready to develop</strong><span>1. Turn meeting notes into actions</span><span>2. Draft emails in your own voice</span><span>3. Build a weekly research brief</span>' : '';
        demo.querySelector('.gb-caption').textContent = captions[step];
        demo.querySelectorAll('[data-field]').forEach(function (el) { el.classList.toggle('gb-active', Number(el.dataset.field) === step); });
        demo.querySelectorAll('[data-step]').forEach(function (el) { el.classList.toggle('gb-selected', Number(el.dataset.step) === step); el.setAttribute('aria-pressed', String(Number(el.dataset.step) === step)); });
        play.textContent = paused ? 'Play' : 'Pause';
      }
      function schedule() {
        clearTimeout(timer);
        if (active && !paused) timer = setTimeout(function () { step = (step + 1) % 4; render(); schedule(); }, step === 3 ? 6500 : 3500);
      }
      play.addEventListener('click', function (event) { event.stopPropagation(); paused = !paused; render(); schedule(); });
      demo.querySelectorAll('[data-step]').forEach(function (button) {
        button.addEventListener('click', function (event) { event.stopPropagation(); step = Number(button.dataset.step); paused = true; render(); schedule(); });
      });
      function sync() { active = Reveal.getCurrentSlide().contains(demo); if (active) { render(); } schedule(); }
      render(); Reveal.on('slidechanged', sync); sync();
    });
    Reveal.layout();
  };
})();
