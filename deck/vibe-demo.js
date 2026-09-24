(function () {
  window.initVibeDemos = function () {
    document.querySelectorAll('.vibe-demo').forEach(function (demo) {
      var names = ['Describe', 'Generate', 'Test', 'Refine'];
      var captions = ['Start with a real need and clear requirements.', 'AI turns your description into a first version.', 'Run it yourself. Find what is missing.', 'Give specific feedback. Build, test, repeat.'];
      demo.innerHTML = `<div class="vc-top"><span>IDEA → WORKING APP</span><button type="button" class="vc-play">Pause</button></div><div class="vc-flow">${names.map((n,i)=>`<button type="button" data-vc="${i}"><b>${i+1}</b>${n}</button>`).join('')}</div><div class="vc-stage"></div><div class="vc-caption"></div><div class="vc-loop">↻ Each round: describe → build → test → improve</div>`;
      var stage = demo.querySelector('.vc-stage'), step = 0, timer, active = false;
      var paused = matchMedia('(prefers-reduced-motion: reduce)').matches;
      var screens = [
        '<div class="vc-who">YOU · THE IDEA</div><div class="vc-prompt">“Build a simple task planner for my week. Let me add tasks and mark them done.”</div><div class="vc-requirements"><span>+ Add a task</span><span>✓ Mark it complete</span><span>▦ See the week</span></div>',
        '<div class="vc-who">AI · FIRST BUILD</div><div class="vc-code"><span>Creating task list…</span><span>Adding a completion toggle…</span><span>Connecting the interactions…</span></div><div class="vc-build"><i></i></div><div class="vc-result">First version ready to preview →</div>',
        '<div class="vc-who">YOU · RUN & INSPECT</div><div class="vc-app"><div class="vc-app-title">My week <small>Version 1</small></div><div>✓ Draft the newsletter</div><div>□ Prepare the presentation</div><div>□ Review this week’s goals</div></div><div class="vc-feedback">Missing something: when is each task due?</div>',
        '<div class="vc-who">YOU + AI · NEXT VERSION</div><div class="vc-feedback">“Add due dates and highlight overdue tasks.”</div><div class="vc-app"><div class="vc-app-title">My week <small>Version 2</small></div><div>✓ Draft the newsletter <em>Today</em></div><div>□ Prepare the presentation <em class="vc-overdue">Overdue</em></div><div>□ Review this week’s goals <em>Friday</em></div></div><div class="vc-result">Now test the dates and completion behaviour ↻</div>'
      ];
      function render() {
        stage.innerHTML = screens[step];
        demo.querySelector('.vc-caption').textContent = captions[step];
        demo.querySelector('.vc-play').textContent = paused ? 'Play' : 'Pause';
        demo.querySelectorAll('[data-vc]').forEach(function (b) { var selected = Number(b.dataset.vc) === step; b.classList.toggle('vc-selected', selected); b.setAttribute('aria-pressed', String(selected)); });
      }
      function schedule() { clearTimeout(timer); if (active && !paused) timer = setTimeout(function () { step = (step+1)%4; render(); schedule(); }, step === 3 ? 6500 : 4500); }
      demo.querySelector('.vc-play').addEventListener('click', function (e) { e.stopPropagation(); paused = !paused; render(); schedule(); });
      demo.querySelectorAll('[data-vc]').forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); step = Number(b.dataset.vc); paused = true; render(); schedule(); }); });
      function sync() { active = Reveal.getCurrentSlide().contains(demo); schedule(); }
      render(); Reveal.on('slidechanged', sync); sync();
    });
    Reveal.layout();
  };
})();
