/* Wireframe behaviours: tiny, dependency-free. Data attributes drive everything. */
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const show = id => { const e = document.getElementById(id); if (e) e.classList.remove('hidden'); };
  const hide = id => { const e = document.getElementById(id); if (e) e.classList.add('hidden'); };
  const list = s => (s || '').split(' ').filter(Boolean);

  document.addEventListener('click', e => {
    const t = e.target.closest('[data-act]');
    if (!t) return;
    const a = t.dataset.act;

    if (a === 'reveal') {
      list(t.dataset.target).forEach(show);
      list(t.dataset.hide).forEach(hide);
      if (t.dataset.self === 'hide') t.classList.add('hidden');
    } else if (a === 'toggle') {
      const x = document.getElementById(t.dataset.target);
      if (x) x.classList.toggle('hidden');
    } else if (a === 'select') {
      const g = t.closest('[data-group]');
      if (g) $$('.sel', g).forEach(x => x.classList.remove('sel'));
      t.classList.add('sel');
      list(t.dataset.target).forEach(show);
    } else if (a === 'pill') {
      t.parentElement.querySelectorAll('.opt').forEach(x => x.classList.remove('sel'));
      t.classList.add('sel');
      list(t.dataset.show).forEach(show);
      list(t.dataset.hide).forEach(hide);
    } else if (a === 'tab') {
      const c = t.closest('[data-tabs]');
      $$('[data-tab]', c).forEach(x => x.classList.toggle('on', x === t));
      $$('[data-panel]', c).forEach(p => p.classList.toggle('hidden', p.dataset.panel !== t.dataset.tab));
    } else if (a === 'check') {
      const c = t.closest('[data-q]');
      const ch = $('[data-choice].sel', c);
      const cf = $('[data-conf].sel', c);
      const w = $('.need', c);
      if (!ch || !cf) { if (w) w.classList.remove('hidden'); return; }
      if (w) w.classList.add('hidden');
      $$('[data-choice]', c).forEach(o => {
        if (o.dataset.correct) o.classList.add('ok'); else if (o === ch) o.classList.add('no');
      });
      const fb = $('.fb', c);
      if (fb) { fb.classList.remove('hidden'); const f = $('.fbtxt', fb); if (f) f.textContent = ch.dataset.fb || ''; }
      const cal = $('.cal', c);
      if (cal) cal.textContent = (ch.dataset.correct ? 'Right' : 'Not quite') + ' at ' + cf.dataset.conf + '% confidence.';
      t.classList.add('hidden');
    } else if (a === 'ask') {
      if (t.disabled) return;
      const box = $('#chat');
      const n = $('#asks');
      let left = +n.textContent;
      if (left <= 0) return;
      box.insertAdjacentHTML('beforeend',
        '<div class="bubble me">' + t.dataset.q + '</div><div class="bubble"><span class="tag">' + t.dataset.who + '</span><br>' +
        t.dataset.a + (t.dataset.unlock ? '<br><span class="chip dark">Unlocked ' + t.dataset.unlock + '</span>' : '') + '</div>');
      if (t.dataset.unlock) { const ex = document.getElementById('ex-' + t.dataset.unlock); if (ex) ex.classList.remove('locked'); }
      t.disabled = true; t.classList.add('locked');
      n.textContent = --left;
      if (left === 0) { $$('[data-act=ask]').forEach(b => { b.disabled = true; }); show('asksdone'); }
    } else if (a === 'req') {
      const v = ($('#reqin').value || '').toLowerCase();
      const out = $('#reqout');
      let hit = null;
      $$('[data-alias]').forEach(x => { if (!hit && x.dataset.alias.split('|').some(k => v.includes(k))) hit = x; });
      if (hit) { hit.classList.remove('locked'); hit.classList.add('sel'); out.textContent = 'Requested: ' + hit.dataset.name + '. Logged for your Questioning score.'; }
      else out.textContent = 'No exhibit matches that. Try naming the data you would want, for example what it measures and for which period.';
    } else if (a === 'hint') {
      const n = $$('.hint.hidden')[0];
      if (n) n.classList.remove('hidden');
      const used = $$('.hint:not(.hidden)').length;
      const c = $('#hintcount');
      if (c) c.textContent = 'Highest level used: L' + used + ' (logged, never penalized)';
      if (!$$('.hint.hidden').length) t.disabled = true;
    } else if (a === 'pick') {
      $$('.chip.pick').forEach(x => x.classList.remove('sel'));
      t.classList.add('sel');
    } else if (a === 'place') {
      const cur = $('.chip.pick.sel');
      if (cur && !t.classList.contains('fill')) {
        t.textContent = cur.textContent; t.classList.add('fill');
        if (cur.dataset.bad) t.dataset.bad = '1';
        cur.classList.add('hidden'); cur.classList.remove('sel');
      } else if (t.classList.contains('fill')) {
        t.textContent = t.dataset.empty || 'Tap a chip, then tap here'; t.classList.remove('fill', 'bad'); delete t.dataset.bad;
      }
    } else if (a === 'treecheck') {
      $$('.slot.fill').forEach(s => { if (s.dataset.bad) s.classList.add('bad'); });
      show('treefb');
    } else if (a === 'width') {
      const p = $('.phone');
      p.classList.toggle('wide');
      t.textContent = p.classList.contains('wide') ? 'Phone width' : 'Desktop width';
    }
  });

  document.addEventListener('change', e => {
    const c = e.target.closest('[data-ticks]');
    if (!c) return;
    const boxes = $$('input[type=checkbox]', c);
    const n = boxes.filter(b => b.checked).length;
    const cnt = $('.tickcount', c);
    if (cnt) cnt.textContent = n + ' of ' + boxes.length;
    const yes = n >= Math.ceil(boxes.length * 0.6);
    const v = $('.tickverdict', c);
    if (v) v.textContent = yes ? 'Mostly yes, so you see the concession.' : 'Mostly no, so you see the escalation.';
    const con = document.getElementById('con'), esc = document.getElementById('esc');
    if (con && esc && c.dataset.decided) { con.classList.toggle('hidden', !yes); esc.classList.toggle('hidden', yes); }
  });
})();
