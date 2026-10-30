/* KAUST Study Lessons hub + Edugates International School A4 print engine. */
(function () {
  'use strict';
  const LABELS = ['A', 'B', 'C', 'D', 'E'];
  const TRACKS = [
    { level: 'Track 1: Grades 6-7', en: 'Grades 6–7', ar: 'الصفوف 6–7', p: '1' },
    { level: 'Track 2: Grades 8-9', en: 'Grades 8–9', ar: 'الصفوف 8–9', p: '2' },
    { level: 'Track 3: Grades 10-11', en: 'Grades 10–11', ar: 'الصفوف 10–11', p: '3' },
  ];
  let lessons = [];
  let activeTrack = TRACKS[0].level;
  let activeLesson = null;

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const pick = (o) => (o[isAr() ? 'ar' : 'en'] || o.en);

  function bankExamples(les) {
    const byId = new Map(appData.questions.map((q) => [q.id, q]));
    return (les.bank_example_ids || []).map((id) => byId.get(id)).filter(Boolean).map((q) => {
      const c = q.content[isAr() ? 'ar' : 'en'] || q.content.en;
      return { id: q.id, correct_index: q.correct_index, title: L('مثال من بنك الأسئلة', 'Question-bank example'),
        question: c.question, options: c.options, explanation: c.explanation, diagram: c.diagram || q.diagram };
    });
  }

  function exampleHtml(ex, n) {
    const opts = (ex.options || []).map((o, i) => {
      const ok = i === ex.correct_index;
      return `<div class="eg-opt${ok ? ' eg-opt-ok' : ''}"><span class="eg-opt-l">${LABELS[i]}</span><span class="math-font">${o}</span>${ok ? '<span class="eg-tick">✓</span>' : ''}</div>`;
    }).join('');
    return `<div class="eg-card eg-example no-break">
      <div class="eg-ex-h">${L('مثال', 'Example')} ${n}${ex.title ? ' — ' + String(ex.title).replace(/^(Solved Example \d+ — |مثال محلول \S+ — )/, '') : ''}</div>
      <div class="eg-q math-font">${ex.question}</div>
      ${ex.diagram ? `<div class="eg-diagram">${ex.diagram}</div>` : ''}
      <div class="eg-opts">${opts}</div>
      <div class="eg-sol"><div class="eg-sol-h">${L('الحل خطوة بخطوة', 'Step-by-step solution')}</div><div class="math-font">${ex.explanation}</div></div>
    </div>`;
  }

  function lessonBodyHtml(les) {
    const d = pick(les);
    const exs = d.examples.concat(bankExamples(les));
    return `
      <div class="eg-banner no-break"><span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span> <span class="eg-badge eg-badge-alt">${les.topic}</span>
        <h2 class="eg-h2">${d.title}</h2><p class="math-font">${d.summary}</p></div>
      <div class="eg-card no-break"><div class="eg-h3">🎯 ${L('ماذا ستتعلم؟', 'What you will learn')}</div><ul class="eg-ul">${d.goals.map((g) => `<li class="math-font">${g}</li>`).join('')}</ul></div>
      ${d.concepts.map((c) => `<div class="eg-card eg-concept no-break"><div class="eg-h3">${c.title}</div><div class="math-font">${c.body}</div>
        ${c.formula ? `<div class="eg-formula math-font">${c.formula}</div>` : ''}${c.diagram ? `<div class="eg-diagram">${c.diagram}</div>` : ''}</div>`).join('')}
      <div class="eg-card eg-traps no-break"><div class="eg-h3">⚠️ ${L('أخطاء شائعة', 'Common exam traps')}</div><ul class="eg-ul">${d.traps.map((t) => `<li class="math-font">${t}</li>`).join('')}</ul></div>
      <div class="eg-h2 eg-examples-title">✏️ ${L('أمثلة محلولة', 'Solved examples')} (${exs.length})</div>
      ${exs.map((e, i) => exampleHtml(e, i + 1)).join('')}`;
  }

  window.edugatesFrame = function (bodyHtml, title, rtl) {
    const logo = '<img src="LOGO.jpg" alt="Edugates International School logo" class="eg-logo">';
    return `<table class="edugates-print-frame" dir="${rtl ? 'rtl' : 'ltr'}">
      <thead><tr><td><div class="eg-head">${logo}<div class="eg-school"><b>Edugates International School</b><span dir="rtl">مدرسة بوابة المعرفة العالمية</span></div><div class="eg-doc">${title}</div></div></td></tr></thead>
      <tbody><tr><td>${bodyHtml}</td></tr></tbody>
      <tfoot><tr><td><div class="eg-foot"><img src="LOGO.jpg" alt="" class="eg-logo-sm"><span>Edugates International School · مدرسة بوابة المعرفة العالمية</span><span>SuperMath · KAUST KMC · A4</span></div></td></tr></tfoot></table>`;
  };

  function printHtml(body, title) {
    const c = document.getElementById('print-container');
    c.innerHTML = window.edugatesFrame(body, title, isAr());
    const imgs = [...c.querySelectorAll('img')].map((im) => (im.complete ? 0 : new Promise((r) => { im.onload = im.onerror = r; })));
    const math = window.MathJax && MathJax.typesetPromise ? MathJax.typesetPromise([c]) : Promise.resolve();
    Promise.all([math, ...imgs]).then(() => setTimeout(() => window.print(), 400));
  }

  window.printKaustLesson = function (id) {
    const les = lessons.find((x) => x.id === id);
    if (les) printHtml(lessonBodyHtml(les), `${L('شرح الدرس', 'Study Lesson')} ${les.unit_num}`);
  };
  window.printKaustTrackBooklet = function (level) {
    const ls = lessons.filter((x) => x.level === level);
    const tr = TRACKS.find((t) => t.level === level);
    const body = ls.map((x, i) => (i ? '<div class="page-break"></div>' : '') + lessonBodyHtml(x)).join('');
    printHtml(body, `${L('دليل المسار', 'Track Study Booklet')} — ${tr[isAr() ? 'ar' : 'en']}`);
  };

  window.practiceKaustLesson = function (id) {
    const les = lessons.find((x) => x.id === id);
    if (!les) return;
    const sel = document.getElementById('quiz-track-select');
    sel.value = 'kaust';
    filterQuestions();
    const set = new Set(les.blueprints);
    currentFilteredQuestions = appData.questions.filter((q) => q.track === 'kaust' && set.has(q.kmc_blueprint));
    currentQuestionIdx = 0;
    resetQuestionState();
    if (typeof renderQuestionCard === 'function') renderQuestionCard();
    let pill = document.getElementById('lesson-filter-pill');
    if (!pill) {
      pill = document.createElement('div');
      pill.id = 'lesson-filter-pill';
      pill.className = 'mb-3 inline-flex items-center gap-2 bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full px-3 py-1 text-xs font-bold';
      sel.closest('section').insertBefore(pill, sel.closest('section').children[2] || null);
    }
    pill.innerHTML = `${L('درس', 'Lesson')} ${les.unit_num} · ${currentFilteredQuestions.length} ${L('سؤال', 'Qs')} <button onclick="document.getElementById('lesson-filter-pill').remove();filterQuestions();renderQuestionCard();" class="underline">${L('عرض كل الأسئلة', 'Show all')}</button>`;
    document.getElementById('practice').scrollIntoView({ behavior: 'smooth' });
  };

  function qCount(les) {
    const s = new Set(les.blueprints);
    return appData.questions.filter((q) => q.track === 'kaust' && s.has(q.kmc_blueprint)).length;
  }

  window.openKaustLesson = function (id) { activeLesson = id; render(); document.getElementById('study-lessons').scrollIntoView({ behavior: 'smooth' }); };
  window.closeKaustLesson = function () { activeLesson = null; render(); };
  window.setKaustTrack = function (level) { activeTrack = level; activeLesson = null; render(); };

  function render() {
    const root = document.getElementById('study-lessons');
    if (!root) return;
    root.setAttribute('dir', isAr() ? 'rtl' : 'ltr');
    const tabs = TRACKS.map((t) => `<button onclick="setKaustTrack('${t.level}')" class="eg-tab${t.level === activeTrack ? ' eg-tab-on' : ''}">${t[isAr() ? 'ar' : 'en']}</button>`).join('');
    let inner;
    if (activeLesson) {
      const les = lessons.find((x) => x.id === activeLesson);
      inner = `<div class="flex flex-wrap gap-2 mb-4 no-print">
        <button onclick="closeKaustLesson()" class="eg-btn">← ${L('كل الدروس', 'All lessons')}</button>
        <button onclick="printKaustLesson('${les.id}')" class="eg-btn eg-btn-main">🖨️ ${L('اطبع الدرس (A4)', 'Print this lesson (A4)')}</button>
        <button onclick="practiceKaustLesson('${les.id}')" class="eg-btn eg-btn-go">⚡ ${L('تدرّب على الدرس', 'Practice this lesson')} (${qCount(les)})</button></div>
        <div class="eg-reader">${lessonBodyHtml(les)}</div>`;
    } else {
      const cards = lessons.filter((x) => x.level === activeTrack).map((les) => {
        const d = pick(les);
        return `<button onclick="openKaustLesson('${les.id}')" class="eg-lesson-card"><div><span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span> <span class="eg-badge eg-badge-alt">${les.topic}</span></div>
          <div class="eg-lc-title">${d.title}</div><div class="eg-lc-meta">${d.examples.length + 4} ${L('أمثلة محلولة', 'solved examples')} · ${qCount(les)} ${L('سؤال تدريبي', 'practice Qs')}</div></button>`;
      }).join('');
      inner = `<div class="flex flex-wrap gap-2 mb-4 no-print"><button onclick="printKaustTrackBooklet('${activeTrack}')" class="eg-btn eg-btn-main">📚 ${L('اطبع دليل المسار كاملاً (A4)', 'Print full track booklet (A4)')}</button></div><div class="eg-grid">${cards}</div>`;
    }
    root.innerHTML = `<div class="eg-hub"><div class="eg-hub-h"><img src="LOGO.jpg" alt="Edugates" class="eg-hub-logo"><div><h2 class="text-2xl sm:text-3xl font-extrabold">📖 ${L('شرح دروس كاوست', 'KAUST Study Lessons')}</h2>
      <p class="text-sm opacity-80">Edugates International School · ${L('شرح مبسّط مع أمثلة محلولة وقابل للطباعة', 'Clear explanations, solved examples, printable on A4')}</p></div></div>
      <div class="flex flex-wrap gap-2 mb-5 no-print">${tabs}</div>${inner}</div>`;
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([root]).catch(() => {});
  }

  async function init() {
    const practice = document.getElementById('practice');
    if (!practice) return;
    const sec = document.createElement('section');
    sec.id = 'study-lessons';
    sec.className = 'no-print-section';
    practice.parentNode.insertBefore(sec, practice);
    try {
      lessons = (await (await fetch('data/kaust_lessons.json')).json()).lessons;
    } catch (e) { console.error('lessons load failed', e); return; }
    // wait for question bank (loaded by main script)
    const t0 = Date.now();
    while ((!appData.questions || !appData.questions.length) && Date.now() - t0 < 15000) await new Promise((r) => setTimeout(r, 100));
    render();
    const orig = window.toggleLanguage;
    if (typeof orig === 'function') window.toggleLanguage = function () { const r = orig.apply(this, arguments); render(); return r; };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.__kaustStudy = { get lessons() { return lessons; }, render, lessonBodyHtml };
})();
