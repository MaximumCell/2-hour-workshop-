(function () {
  window.initAutomationDemos = function () {
    document.querySelectorAll('.automation-demo').forEach(function (demo) {
      function node(id,x,y,w,title,sub) { return `<g class="wf-node" data-node="${id}" transform="translate(${x} ${y})"><rect width="${w}" height="76" rx="13"/><text x="${w/2}" y="31" class="wf-name">${title}</text><text x="${w/2}" y="55" class="wf-sub">${sub}</text></g>`; }
      demo.innerHTML = `<div class="wf-toolbar"><span>ILLUSTRATIVE RUN · <b class="wf-run"></b></span><button type="button" class="wf-play">Pause</button></div><svg viewBox="0 0 1080 360" role="img" aria-label="Chat trigger connects to an AI agent, supported by model, memory, search and tools. A condition branches to success or needs attention."><defs><marker id="wf-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><g class="wf-wires" fill="none" stroke-width="3" marker-end="url(#wf-arrow)"><path data-wire="input" d="M200 110 H340"/><path data-wire="decision" d="M550 110 H670"/><path data-wire="success" d="M825 110 C860 110 845 53 885 53"/><path data-wire="failure" d="M825 110 C860 110 845 173 885 173"/><path class="wf-support" data-wire="support" d="M230 260 V218 H400 V148"/><path class="wf-support" data-wire="support" d="M405 260 V148"/><path class="wf-support" data-wire="support" d="M580 260 V218 H480 V148"/><path class="wf-support" data-wire="support" d="M755 260 V205 H515 V148"/></g><text x="845" y="47" class="wf-branch">Yes</text><text x="846" y="207" class="wf-branch">No</text>${node('trigger',20,72,180,'Chat received','The trigger')}${node('agent',340,72,210,'AI agent','Understand + act')}${node('condition',670,72,155,'Check result','Condition met?')}${node('success',885,15,175,'Success','Notify the team')}${node('failure',885,135,175,'Needs attention','Send an alert')}${node('model',155,260,150,'AI model','Reason + write')}${node('memory',330,260,150,'Memory','Keep context')}${node('search',505,260,150,'Search','Find information')}${node('tool',680,260,150,'Workflow tool','Perform an action')}<text x="30" y="245" class="wf-legend">SUPPORT</text></svg><div class="wf-caption"></div><div class="wf-controls">${['Trigger','Agent','Resources','Condition','Result'].map((n,i)=>`<button type="button" data-stage="${i}">${i+1} · ${n}</button>`).join('')}</div><div class="wf-foot">Solid lines: execution path <span>Dashed lines: agent resources, used as needed</span></div>`;
      var step=0, success=true, active=false, timer, paused=matchMedia('(prefers-reduced-motion: reduce)').matches;
      function render() {
        demo.classList.toggle("wf-paused", paused);
        var nodes=[['trigger'],['agent'],['agent','model','memory','search','tool'],['condition'],[success?'success':'failure']][step];
        var wires=[[],['input'],['support'],['decision'],[success?'success':'failure']][step];
        demo.querySelectorAll('[data-node]').forEach(function(n){n.classList.toggle('wf-on',nodes.includes(n.dataset.node));});
        demo.querySelectorAll('[data-wire]').forEach(function(n){n.classList.toggle('wf-on',wires.includes(n.dataset.wire));});
        demo.querySelectorAll('[data-stage]').forEach(function(n){var on=Number(n.dataset.stage)===step;n.classList.toggle('wf-selected',on);n.setAttribute('aria-pressed',String(on));});
        demo.querySelector('.wf-run').textContent=success?'Success example':'Needs-attention example';
        demo.querySelector('.wf-caption').textContent=[ 'A new message arrives. The workflow starts automatically.', 'The agent reads the request and decides how to handle it.', 'The model powers the agent; memory and tools provide context and actions as needed.', 'A condition checks the result and chooses one branch.', success?'The check passes → send the team a success notification.':'The check does not pass → send an alert for attention.' ][step];
        demo.querySelector('.wf-play').textContent=paused?'Play':'Pause';
      }
      function schedule(){clearTimeout(timer);if(active&&!paused)timer=setTimeout(function(){step++;if(step>4){step=0;success=!success;}render();schedule();},step===2||step===4?5500:3500);}
      demo.querySelector('.wf-play').addEventListener('click',function(e){e.stopPropagation();paused=!paused;render();schedule();});
      demo.querySelectorAll('[data-stage]').forEach(function(b){b.addEventListener('click',function(e){e.stopPropagation();step=Number(b.dataset.stage);paused=true;render();schedule();});});
      function sync(){active=Reveal.getCurrentSlide().contains(demo);schedule();}
      render();Reveal.on('slidechanged',sync);sync();
    });Reveal.layout();
  };
})();
