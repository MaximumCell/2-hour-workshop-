// Animated "agentic browser" mock-up for the Comet title slide. Loops while its slide is showing.
//
// Markup (in a slide):
//   <div class="agent-demo" data-prompt="...">
//     <div class="ad-step" data-tab="skyscanner.com" data-label="Checking Skyscanner" data-pick="1">
//       <div class="ad-row"><b>name</b><span>detail</span><em>price</em></div>   (rows shown on that "site")
//     </div>
//     <div class="ad-result">...summary HTML...</div>
//   </div>
//
// Each step: its rows slide in, a highlight sweeps down them ("reading"), then the
// cursor moves to row data-pick and clicks it. A step with no rows shows a thinking state.
(function () {
  var TYPE_MS = 32, STEP_MS = 3200, RESULT_MS = 4800;

  function build(el) {
    var steps = [].map.call(el.querySelectorAll('.ad-step'), function (s) {
      return {
        tab: s.getAttribute('data-tab'),
        label: s.getAttribute('data-label'),
        pick: +s.getAttribute('data-pick') || 0,
        rows: s.innerHTML.trim()
      };
    });
    var result = el.querySelector('.ad-result');
    el.innerHTML =
      '<div class="ad-win">' +
      '<div class="ad-top"><span class="ad-dots"><i></i><i></i><i></i></span><div class="ad-tabs"></div></div>' +
      '<div class="ad-url"><span class="ad-spark">✦</span><span class="ad-typed"></span><span class="ad-caret"></span></div>' +
      '<div class="ad-body">' +
      '<div class="ad-page"><div class="ad-site"></div><div class="ad-rows"></div>' +
      '<div class="ad-think"><i></i><i></i><i></i></div>' +
      '<div class="ad-cursor"></div><div class="ad-result">' + (result ? result.innerHTML : '') + '</div></div>' +
      '<div class="ad-panel"><div class="ad-panel-h">Comet assistant</div><ul class="ad-steps">' +
      steps.map(function (s) { return '<li>' + s.label + '</li>'; }).join('') +
      '</ul></div></div></div>';
    el._ad = { steps: steps, prompt: el.getAttribute('data-prompt') || '', run: 0 };
    reset(el);
  }

  function $(el, sel) { return el.querySelector(sel); }

  // setTimeout that is silently dropped once the loop has been restarted or stopped
  function later(el, run, ms, fn) {
    setTimeout(function () { if (el._ad.run === run) fn(); }, ms);
  }

  function reset(el) {
    el.classList.remove('ad-working', 'ad-thinking', 'ad-done');
    $(el, '.ad-typed').textContent = '';
    $(el, '.ad-tabs').innerHTML = '<span class="ad-tab on">New tab</span>';
    $(el, '.ad-site').textContent = '';
    $(el, '.ad-rows').innerHTML = '';
    [].forEach.call(el.querySelectorAll('.ad-steps li'), function (li) { li.className = ''; });
    var c = $(el, '.ad-cursor');
    c.className = 'ad-cursor';
    c.style.left = '70%';
    c.style.top = '85%';
  }

  function showStep(el, run, i) {
    var d = el._ad, s = d.steps[i];
    $(el, '.ad-tabs').innerHTML = d.steps.slice(0, i + 1).map(function (t, k) {
      return '<span class="ad-tab' + (k === i ? ' on' : '') + '">' + t.tab + '</span>';
    }).join('');
    [].forEach.call(el.querySelectorAll('.ad-steps li'), function (li, k) {
      li.className = k < i ? 'done' : k === i ? 'active' : '';
    });
    $(el, '.ad-site').textContent = s.tab;
    var rows = $(el, '.ad-rows');
    rows.innerHTML = s.rows; // re-inserting restarts the slide-in + sweep animations
    el.classList.toggle('ad-working', !!s.rows);
    el.classList.toggle('ad-thinking', !s.rows);
    if (!s.rows) { $(el, '.ad-cursor').classList.remove('on'); return; }

    // after the sweep finishes, glide the cursor onto the chosen row and click it
    var target = rows.querySelectorAll('.ad-row')[s.pick];
    later(el, run, 1300, function () {
      var c = $(el, '.ad-cursor');
      c.classList.add('on');
      c.style.left = (target.offsetLeft + target.offsetWidth * 0.62) + 'px';
      c.style.top = (rows.offsetTop + target.offsetTop + target.offsetHeight * 0.55) + 'px';
      later(el, run, 750, function () {
        c.classList.remove('click'); void c.offsetWidth; c.classList.add('click');
        target.classList.add('picked');
      });
    });
  }

  function loop(el) {
    var d = el._ad, run = ++d.run;
    reset(el);
    var t = 500;
    // 1. the prompt types itself
    later(el, run, t, function () {
      var node = $(el, '.ad-typed'), k = 0;
      (function tick() {
        if (d.run !== run) return;
        node.textContent = d.prompt.slice(0, ++k);
        if (k < d.prompt.length) setTimeout(tick, TYPE_MS);
      })();
    });
    t += d.prompt.length * TYPE_MS + 600;
    // 2. one step at a time
    d.steps.forEach(function (s, i) {
      later(el, run, t, function () { showStep(el, run, i); });
      t += s.rows ? STEP_MS : 1600;
    });
    // 3. the answer
    later(el, run, t, function () {
      [].forEach.call(el.querySelectorAll('.ad-steps li'), function (li) { li.className = 'done'; });
      el.classList.remove('ad-working', 'ad-thinking');
      $(el, '.ad-cursor').classList.remove('on');
      el.classList.add('ad-done');
    });
    t += RESULT_MS;
    later(el, run, t, function () { loop(el); });
  }

  function sync() {
    var current = Reveal.getCurrentSlide();
    document.querySelectorAll('.agent-demo').forEach(function (el) {
      var here = !!current && current.contains(el);
      if (here && !el._running) { el._running = true; loop(el); }
      else if (!here && el._running) { el._running = false; el._ad.run++; reset(el); }
    });
  }

  window.initAgentDemos = function () {
    document.querySelectorAll('.agent-demo').forEach(build);
    Reveal.layout(); // re-centre: before build() the raw rows made the slide look taller
    Reveal.on('slidechanged', sync);
    sync();
  };
})();
