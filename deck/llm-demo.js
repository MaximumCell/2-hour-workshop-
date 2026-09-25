(function () {
  // "How an LLM works" explainer: tokenize → embed → compare → predict, same stepper pattern as vibe-demo.js
  window.initLlmDemos = function () {
    document.querySelectorAll('.llm-demo').forEach(function (demo) {
      var cells = function (vals) { return vals.map(function (v) { return '<i style="opacity:' + v + '"></i>'; }).join(''); };
      var screens = [
        '<div class="vc-who">STEP 1 · YOUR PROMPT</div><div class="lm-sentence">The cat sat on the</div><div class="lm-tokens"><span>The</span><span>cat</span><span>sat</span><span>on</span><span>the</span></div><div class="lm-hint">5 tokens → the model never sees “words”, only these pieces</div>',
        '<div class="vc-who">STEP 2 · TOKENS → NUMBERS (EMBEDDINGS)</div><div class="lm-vecs">' +
          '<div><b>cat</b><span class="lm-cells">' + cells([.9, .2, .8, .3, .7, .1, .6, .4]) + '</span><em>[0.9, 0.2, 0.8 …]</em></div>' +
          '<div><b>dog</b><span class="lm-cells">' + cells([.8, .3, .8, .2, .6, .2, .7, .4]) + '</span><em>[0.8, 0.3, 0.8 …]</em></div>' +
          '<div><b>car</b><span class="lm-cells">' + cells([.1, .9, .2, .8, .1, .9, .2, .7]) + '</span><em>[0.1, 0.9, 0.2 …]</em></div>' +
        '</div><div class="lm-hint">cat and dog get similar numbers. car looks completely different.</div>',
        '<div class="vc-who">STEP 3 · THE MEANING MAP</div><svg class="lm-map" viewBox="0 0 500 200">' +
          '<text class="lm-zone" x="40" y="22">ANIMALS</text><text class="lm-zone" x="330" y="22">VEHICLES</text><text class="lm-zone" x="230" y="192">PLACES TO SIT</text>' +
          '<line class="lm-link" x1="95" y1="80" x2="160" y2="55"/><line class="lm-link" x1="95" y1="80" x2="130" y2="130"/>' +
          '<g class="lm-pt far"><circle cx="400" cy="70" r="7"/><text x="412" y="75">car</text></g>' +
          '<g class="lm-pt far"><circle cx="440" cy="120" r="7"/><text x="452" y="125">bus</text></g>' +
          '<g class="lm-pt mid"><circle cx="260" cy="150" r="7"/><text x="272" y="155">mat</text></g>' +
          '<g class="lm-pt mid"><circle cx="320" cy="165" r="7"/><text x="332" y="170">sofa</text></g>' +
          '<g class="lm-pt near"><circle cx="160" cy="55" r="7"/><text x="172" y="60">dog</text></g>' +
          '<g class="lm-pt near"><circle cx="130" cy="130" r="7"/><text x="142" y="135">kitten</text></g>' +
          '<g class="lm-pt me"><circle cx="95" cy="80" r="10"/><text x="60" y="108">cat</text></g>' +
        '</svg><div class="lm-hint">Close = related. The model compares every token with the others this way.</div>',
        '<div class="vc-who">STEP 4 · GUESS THE NEXT TOKEN</div><div class="lm-sentence">The cat sat on the <u>mat</u></div><div class="lm-bars">' +
          '<div class="win"><b>mat</b><span><i style="--w:62%"></i></span><em>62%</em></div>' +
          '<div><b>floor</b><span><i style="--w:21%"></i></span><em>21%</em></div>' +
          '<div><b>sofa</b><span><i style="--w:11%"></i></span><em>11%</em></div>' +
          '<div><b>car</b><span><i style="--w:1%"></i></span><em>1%</em></div>' +
        '</div>' +
        '<div class="lm-next">↻ “mat” joins the sentence → The cat sat on the mat <span>▍</span></div>'
      ];
      // the step list lives beside the panel (left column); the panel only holds the animation
      var steps = demo.closest('section').querySelectorAll('.lm-steps [data-vc]');
      demo.innerHTML = '<div class="vc-top"><span>HOW AN LLM THINKS</span><button type="button" class="vc-play">Pause</button></div><div class="vc-stage"></div><div class="vc-loop">↻ Add the new token, then do it all again, one token at a time</div>';
      var stage = demo.querySelector('.vc-stage'), step = 0, timer, active = false;
      var paused = matchMedia('(prefers-reduced-motion: reduce)').matches;
      function render() {
        stage.innerHTML = screens[step];
        demo.querySelector('.vc-play').textContent = paused ? 'Play' : 'Pause';
        steps.forEach(function (b) { var selected = Number(b.dataset.vc) === step; b.classList.toggle('vc-selected', selected); b.setAttribute('aria-pressed', String(selected)); });
      }
      function schedule() { clearTimeout(timer); if (active && !paused) timer = setTimeout(function () { step = (step + 1) % 4; render(); schedule(); }, step === 2 || step === 3 ? 6000 : 4500); }
      demo.querySelector('.vc-play').addEventListener('click', function (e) { e.stopPropagation(); paused = !paused; render(); schedule(); });
      steps.forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); step = Number(b.dataset.vc); paused = true; render(); schedule(); }); });
      function sync() { var now = Reveal.getCurrentSlide().contains(demo); if (now && !active) { step = 0; render(); } active = now; schedule(); }
      render(); Reveal.on('slidechanged', sync); sync();
    });
  };
})();
