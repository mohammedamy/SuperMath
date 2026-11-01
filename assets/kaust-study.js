/* KAUST (KMC) Study Academy + Edugates International School Multi-Page A4 Print Engine */
(function () {
  'use strict';

  const LABELS = ['A', 'B', 'C', 'D', 'E'];
  const TRACKS = [
    { level: 'Track 1: Grades 6-7', en: 'Track 1 · Grades 6–7', ar: 'المسار ١ · الصفوف 6–7', shortEn: 'Grades 6–7', shortAr: 'الصفوف 6–7' },
    { level: 'Track 2: Grades 8-9', en: 'Track 2 · Grades 8–9', ar: 'المسار ٢ · الصفوف 8–9', shortEn: 'Grades 8–9', shortAr: 'الصفوف 8–9' },
    { level: 'Track 3: Grades 10-11', en: 'Track 3 · Grades 10–11', ar: 'المسار ٣ · الصفوف 10–11', shortEn: 'Grades 10–11', shortAr: 'الصفوف 10–11' },
  ];
  const TOPIC_AR = {
    'Number Theory': 'نظرية الأعداد',
    'Algebra': 'الجبر والأنماط',
    'Geometry': 'الهندسة والقياس',
    'Combinatorics & Logic': 'التوافيق والمنطق والاحتمالات',
  };

  let lessons = [];
  let activeTrack = TRACKS[0].level;
  let activeLessonId = null;
  let selfTestMode = false;
  let revealedExamples = new Set();
  let selectedTryChoice = {};

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const pick = (o) => (o[isAr() ? 'ar' : 'en'] || o.en);
  const topicLabel = (tp) => (isAr() ? (TOPIC_AR[tp] || tp) : tp);
  const getBankQuestions = () => (typeof appData !== 'undefined' && Array.isArray(appData.questions) ? appData.questions : []);

  function bankExamples(les) {
    const qs = getBankQuestions();
    if (!qs.length) return [];
    const byId = new Map(qs.map((q) => [q.id, q]));
    return (les.bank_example_ids || [])
      .map((id) => byId.get(id))
      .filter(Boolean)
      .map((q, idx) => {
        const c = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
        const diffBadge = q.difficulty ? ` (${q.difficulty})` : '';
        return {
          id: q.id,
          correct_index: q.correct_index,
          title: L(`تطبيق إضافي محلول ${idx + 1} من بنك كاوست${diffBadge}`, `Extra KMC Practice Example ${idx + 1}${diffBadge}`),
          question: c.question || '',
          options: c.options || [],
          explanation: c.explanation || '',
          diagram: c.diagram || q.diagram || '',
          fromBank: true,
        };
      });
  }

  function allExamplesFor(les) {
    const d = pick(les);
    return (d.examples || []).concat(bankExamples(les));
  }

  function cleanExTitle(raw) {
    if (!raw) return '';
    return String(raw).replace(/^(Solved Example \d+\s*[—\-:]\s*|مثال محلول \S+\s*[—\-:]\s*)/, '');
  }

  function exampleCardHtml(ex, num, forPrint) {
    const exKey = `${activeLessonId || 'P'}:${ex.id || num}`;
    const showAnswer = forPrint || !selfTestMode || revealedExamples.has(exKey);
    const chosen = selectedTryChoice[exKey];

    const opts = (ex.options || []).map((opt, idx) => {
      const isCorrect = idx === ex.correct_index;
      let cls = 'eg-opt';
      let badge = '';
      if (showAnswer && isCorrect) {
        cls += ' eg-opt-ok';
        badge = '<span class="eg-tick" aria-hidden="true">✓</span>';
      } else if (!forPrint && selfTestMode && chosen === idx && !isCorrect) {
        cls += ' eg-opt-wrong';
        badge = '<span class="eg-cross" aria-hidden="true">✗</span>';
      }
      if (!forPrint && selfTestMode && !showAnswer) {
        return `<button type="button" onclick="tryKaustExample('${exKey}', ${idx})" class="${cls} eg-opt-interactive"><span class="eg-opt-l">${LABELS[idx]}</span><span class="math-font eg-opt-txt">${opt}</span></button>`;
      }
      return `<div class="${cls}"><span class="eg-opt-l">${LABELS[idx]}</span><span class="math-font eg-opt-txt">${opt}</span>${badge}</div>`;
    }).join('');

    const subTitle = cleanExTitle(ex.title);
    const headerBadge = ex.fromBank
      ? `<span class="eg-ex-tag eg-ex-tag-bank">${L('من بنك كاوست', 'KMC Bank')}</span>`
      : `<span class="eg-ex-tag">${L('مثال أساسي', 'Core Example')}</span>`;

    const solutionBlock = showAnswer
      ? `<div class="eg-sol">
           <div class="eg-sol-h">✅ ${L('الإجابة الصحيحة', 'Correct Answer')}: (${LABELS[ex.correct_index]}) — ${L('خطوات الحل التفصيلية', 'Step-by-Step Solution')}</div>
           <div class="math-font eg-prose">${ex.explanation}</div>
         </div>`
      : `<div class="eg-reveal-bar no-print">
           <span class="text-xs opacity-80">${L('جرّب اختيار الإجابة أعلاه أولاً أو اكشف الحل:', 'Pick an option above to test yourself, or reveal the worked solution:')}</span>
           <button type="button" onclick="revealKaustExample('${exKey}')" class="eg-btn eg-btn-sm">👁️ ${L('إظهار الحل خطوة بخطوة', 'Show Worked Solution')}</button>
         </div>`;

    return `<div class="eg-card eg-example no-break">
      <div class="eg-ex-top">
        <div class="eg-ex-h">${L('مثال محلول', 'Solved Example')} ${num}${subTitle ? ` — ${subTitle}` : ''}</div>
        ${headerBadge}
      </div>
      <div class="eg-q math-font">${ex.question}</div>
      ${ex.diagram ? `<div class="eg-diagram">${ex.diagram}</div>` : ''}
      <div class="eg-opts">${opts}</div>
      ${solutionBlock}
    </div>`;
  }

  function lessonBlocks(les, forPrint) {
    const d = pick(les);
    const tr = TRACKS.find((t) => t.level === les.level) || TRACKS[0];
    const exs = allExamplesFor(les);

    const bannerAndGoals = `
      <div class="eg-banner no-break">
        <div class="eg-banner-meta">
          <span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span>
          <span class="eg-badge eg-badge-alt">${topicLabel(les.topic)}</span>
          <span class="eg-badge eg-badge-soft">${isAr() ? tr.ar : tr.en}</span>
        </div>
        <h2 class="eg-h2">${d.title}</h2>
        <p class="math-font eg-summary">${d.summary}</p>
      </div>
      <div class="eg-card eg-goals no-break">
        <div class="eg-h3">🎯 ${L('أهداف الدرس — ماذا سنتعلّم؟', 'Learning Goals — What You Will Master')}</div>
        <ul class="eg-ul">${(d.goals || []).map((g) => `<li class="math-font">${g}</li>`).join('')}</ul>
      </div>`;

    const conceptBlocks = (d.concepts || []).map((c) => `
      <div class="eg-card eg-concept no-break">
        <div class="eg-h3">${c.title}</div>
        <div class="math-font eg-prose">${c.body}</div>
        ${c.formula ? `<div class="eg-formula math-font" dir="ltr">${c.formula}</div>` : ''}
        ${c.diagram ? `<div class="eg-diagram">${c.diagram}</div>` : ''}
      </div>`);

    const trapsBlock = `
      <div class="eg-card eg-traps no-break">
        <div class="eg-h3">⚠️ ${L('احذر هذه الأخطاء الشائعة في الاختبار!', 'Watch Out — Common KMC Exam Traps!')}</div>
        <ul class="eg-ul">${(d.traps || []).map((t) => `<li class="math-font">${t}</li>`).join('')}</ul>
      </div>`;

    const exampleBlocks = exs.map((ex, i) => {
      const card = exampleCardHtml(ex, i + 1, forPrint);
      if (i === 0) {
        return `<div class="no-break">
          <div class="eg-sec-heading">✏️ ${L('الأمثلة المحلولة بالتفصيل', 'Fully Worked Examples')} (${exs.length})</div>
          ${card}
        </div>`;
      }
      return card;
    });

    return [bannerAndGoals, ...conceptBlocks, trapsBlock, ...exampleBlocks];
  }

  function lessonBodyHtml(les, forPrint) {
    return lessonBlocks(les, !!forPrint).join('');
  }

  /* Multi-page A4 print table builder: repeating <thead> and <tfoot> with Edugates logo on EVERY page */
  window.edugatesPrintSection = function (rows, title, badgeText, rtl, pageBreakBefore) {
    const safeRows = Array.isArray(rows) ? rows : [rows];
    const subLine = rtl
      ? 'أكاديمية التميز للمسابقات الرياضية · بدون آلة حاسبة · ورق A4'
      : 'Mathematics Competition Academy · Official A4 Study & Exam Series';
    const badge = badgeText || (rtl ? 'كاوست KMC · A4' : 'KAUST KMC · A4');
    return `<table class="edugates-print-frame${pageBreakBefore ? ' eg-print-break' : ''}" dir="${rtl ? 'rtl' : 'ltr'}">
      <thead>
        <tr>
          <td>
            <div class="eg-head">
              <div class="eg-logo-wrap"><img src="LOGO.jpg" alt="Edugates International School" class="eg-logo"></div>
              <div class="eg-school">
                <div class="eg-school-en">Edugates International School</div>
                <div class="eg-school-ar" dir="rtl">مدرسة بوابة المعرفة العالمية</div>
                <div class="eg-school-sub">${subLine}</div>
              </div>
              <div class="eg-doc">
                <div class="eg-doc-title">${title}</div>
                <div class="eg-doc-badge">${badge}</div>
              </div>
            </div>
          </td>
        </tr>
      </thead>
      <tbody>
        ${safeRows.map((r) => `<tr class="eg-print-row"><td>${r}</td></tr>`).join('')}
      </tbody>
      <tfoot>
        <tr>
          <td>
            <div class="eg-foot">
              <div class="eg-foot-brand">
                <img src="LOGO.jpg" alt="" class="eg-logo-sm">
                <span><strong>Edugates International School</strong> · مدرسة بوابة المعرفة العالمية</span>
              </div>
              <span class="eg-foot-meta">${title} · A4</span>
            </div>
          </td>
        </tr>
      </tfoot>
    </table>`;
  };

  /* Backwards-compatible wrapper */
  window.edugatesFrame = function (bodyHtml, title, rtl) {
    return window.edugatesPrintSection([bodyHtml], title, rtl ? 'ورقة عمل A4' : 'A4 Worksheet', rtl, false);
  };

  /* Dedicated row-paginated Practice Worksheet + Answer Key builder for executePrint() */
  window.buildEdugatesWorksheetHtml = function (questionsToPrint, docTitle, answerKeyTitle, qLabel, badgeText, includeSolutions, rtl) {
    const studentBar = `<div class="eg-student-bar">
      <div><strong>${rtl ? 'اسم الطالب/ـة:' : 'Student Name:'}</strong> ___________________________</div>
      <div><strong>${rtl ? 'الصف:' : 'Grade:'}</strong> __________</div>
      <div><strong>${rtl ? 'الدرجة:' : 'Score:'}</strong> ____ / ${questionsToPrint.length}</div>
    </div>`;

    const qRows = questionsToPrint.map((q, index) => {
      const qContent = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
      const diag = qContent.diagram || q.diagram || '';
      let optsHtml = '';
      if (qContent.options && qContent.options.length > 0) {
        optsHtml = `<div class="eg-ws-opts">${qContent.options.map((opt, oIdx) => `
          <div class="eg-ws-opt">
            <span class="eg-opt-l">${LABELS[oIdx]}</span>
            <span class="math-font">${opt}</span>
          </div>`).join('')}</div>`;
      } else {
        optsHtml = `<div class="eg-frq-box"></div>`;
      }
      const card = `<div class="eg-ws-q no-break">
        <div class="eg-ws-qh"><span>${qLabel} ${index + 1}</span><span class="eg-ws-qmeta">${q.topic || ''}${q.difficulty ? ' · ' + q.difficulty : ''}</span></div>
        <div class="eg-q math-font">${qContent.question || ''}</div>
        ${diag ? `<div class="eg-diagram">${diag}</div>` : ''}
        ${optsHtml}
      </div>`;
      return index === 0 ? `<div class="no-break">${studentBar}${card}</div>` : card;
    });

    const keyGrid = `<div class="eg-key-box no-break">
      <div class="eg-h3">${answerKeyTitle}</div>
      <div class="eg-key-grid">
        ${questionsToPrint.map((q, idx) => {
          const ans = (q.type === 'MCQ' && q.correct_index !== undefined && q.correct_index !== null)
            ? LABELS[q.correct_index]
            : 'FRQ';
          return `<div class="eg-key-cell"><strong>${idx + 1}.</strong> <span>${ans}</span></div>`;
        }).join('')}
      </div>
    </div>`;

    const detailItems = questionsToPrint
      .map((q, idx) => ({ q, idx }))
      .filter(({ q }) => includeSolutions || q.type !== 'MCQ')
      .map(({ q, idx }) => {
        const c = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
        const ans = (q.type === 'MCQ' && q.correct_index !== undefined && q.correct_index !== null)
          ? `(${LABELS[q.correct_index]})`
          : 'FRQ';
        return `<div class="eg-card eg-sol-card no-break">
          <div class="eg-sol-h">${qLabel} ${idx + 1} — ${rtl ? 'الإجابة' : 'Answer'}: ${ans} <span class="eg-ws-qmeta">(${q.id})</span></div>
          <div class="math-font eg-prose">${c.explanation || ''}</div>
        </div>`;
      });

    const keyRows = [keyGrid, ...detailItems];
    return (
      window.edugatesPrintSection(qRows, docTitle, badgeText, rtl, false) +
      window.edugatesPrintSection(keyRows, answerKeyTitle, badgeText, rtl, true)
    );
  };

  function triggerContainerPrint(container) {
    if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
      const imgs = [...container.querySelectorAll('img')].map((im) =>
        im.complete ? Promise.resolve() : new Promise((r) => { im.onload = im.onerror = r; })
      );
      Promise.all([MathJax.typesetPromise([container]), ...imgs]).then(() => {
        setTimeout(() => { window.print(); }, 350);
      });
    } else {
      window.print();
    }
  }

  window.printKaustLesson = function (id) {
    const les = lessons.find((x) => x.id === id);
    if (!les) return;
    const tr = TRACKS.find((t) => t.level === les.level) || TRACKS[0];
    const c = document.getElementById('print-container');
    const docTitle = `${L('شرح الدرس', 'Study Guide')} ${les.unit_num} — ${pick(les).title}`;
    const badge = `${isAr() ? tr.shortAr : tr.shortEn} · KAUST KMC · A4`;
    c.innerHTML = window.edugatesPrintSection(lessonBlocks(les, true), docTitle, badge, isAr(), false);
    triggerContainerPrint(c);
  };

  window.printKaustTrackBooklet = function (level) {
    const ls = lessons.filter((x) => x.level === level);
    if (!ls.length) return;
    const tr = TRACKS.find((t) => t.level === level) || TRACKS[0];
    const c = document.getElementById('print-container');
    c.innerHTML = ls.map((les, idx) => {
      const docTitle = `${L('درس', 'Lesson')} ${les.unit_num} — ${pick(les).title}`;
      const badge = `${isAr() ? tr.shortAr : tr.shortEn} · ${L('دليل المسار', 'Track Booklet')} · A4`;
      return window.edugatesPrintSection(lessonBlocks(les, true), docTitle, badge, isAr(), idx > 0);
    }).join('');
    triggerContainerPrint(c);
  };

  window.practiceKaustLesson = function (id) {
    const les = lessons.find((x) => x.id === id);
    if (!les) return;
    if (typeof currentSelectedGrade !== 'undefined') currentSelectedGrade = 'all';
    if (typeof renderGradeFilters === 'function') renderGradeFilters();
    const sel = document.getElementById('quiz-track-select');
    sel.value = 'kaust';
    filterQuestions();
    const phaseSel = document.getElementById('quiz-kaust-phase-select');
    if (phaseSel) phaseSel.value = les.level;
    filterQuestions();
    const bpSet = new Set(les.blueprints);
    currentFilteredQuestions = appData.questions.filter((q) => q.track === 'kaust' && bpSet.has(q.kmc_blueprint));
    currentQuestionIdx = 0;
    resetQuestionState();
    if (typeof renderQuestionCard === 'function') renderQuestionCard();

    let pill = document.getElementById('lesson-filter-pill');
    if (!pill) {
      pill = document.createElement('div');
      pill.id = 'lesson-filter-pill';
      pill.className = 'mb-3 inline-flex flex-wrap items-center gap-2 bg-amber-500/20 text-amber-200 border border-amber-400/40 rounded-full px-3.5 py-1.5 text-xs font-bold';
      const sec = document.getElementById('practice');
      sec.insertBefore(pill, sec.children[2] || null);
    }
    pill.innerHTML = `<span>📖 ${L('تدريب مخصّص لدرس', 'Practicing Lesson')} ${les.unit_num}: ${pick(les).title} (${currentFilteredQuestions.length} ${L('سؤال', 'Qs')})</span>
      <button type="button" onclick="clearKaustLessonFilter()" class="underline hover:text-white ms-1">${L('عرض كل أسئلة المسار', 'Show all track Qs')}</button>`;
    document.getElementById('practice').scrollIntoView({ behavior: 'smooth' });
  };

  window.clearKaustLessonFilter = function () {
    const pill = document.getElementById('lesson-filter-pill');
    if (pill) pill.remove();
    filterQuestions();
    if (typeof renderQuestionCard === 'function') renderQuestionCard();
  };

  window.tryKaustExample = function (exKey, choiceIdx) {
    selectedTryChoice[exKey] = choiceIdx;
    const [, exId] = exKey.split(':');
    const les = lessons.find((x) => x.id === activeLessonId);
    if (les) {
      const ex = allExamplesFor(les).find((e, i) => String(e.id || i + 1) === exId);
      if (ex && choiceIdx === ex.correct_index) revealedExamples.add(exKey);
    }
    render();
  };

  window.revealKaustExample = function (exKey) {
    revealedExamples.add(exKey);
    render();
  };

  window.toggleKaustSelfTest = function () {
    selfTestMode = !selfTestMode;
    if (!selfTestMode) {
      revealedExamples.clear();
      selectedTryChoice = {};
    }
    render();
  };

  window.openKaustLesson = function (id) {
    const les = lessons.find((x) => x.id === id);
    if (les) activeTrack = les.level;
    activeLessonId = id;
    render();
    const el = document.getElementById('study-lessons');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  window.closeKaustLesson = function () {
    activeLessonId = null;
    render();
  };

  window.setKaustTrack = function (level) {
    activeTrack = level;
    activeLessonId = null;
    render();
  };

  window.jumpToKaustStudy = function (level) {
    if (level) {
      activeTrack = level;
      activeLessonId = null;
    }
    render();
    const el = document.getElementById('study-lessons');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  function qCount(les) {
    const qs = getBankQuestions();
    if (!qs.length) return 0;
    const s = new Set(les.blueprints);
    return qs.filter((q) => q.track === 'kaust' && s.has(q.kmc_blueprint)).length;
  }

  function render() {
    const root = document.getElementById('study-lessons');
    if (!root || !lessons.length) return;
    root.setAttribute('dir', isAr() ? 'rtl' : 'ltr');

    const tabs = TRACKS.map((t) => {
      const tLessons = lessons.filter((x) => x.level === t.level);
      const exTotal = tLessons.reduce((acc, x) => acc + (pick(x).examples || []).length + (x.bank_example_ids || []).length, 0);
      return `<button type="button" onclick="setKaustTrack('${t.level}')" class="eg-tab${t.level === activeTrack ? ' eg-tab-on' : ''}">
        <span>${isAr() ? t.ar : t.en}</span>
        <span class="eg-tab-count">${tLessons.length} ${L('دروس', 'Lessons')} · ${exTotal} ${L('مثال', 'Ex')}</span>
      </button>`;
    }).join('');

    let inner;
    if (activeLessonId) {
      const trackLessons = lessons.filter((x) => x.level === activeTrack);
      const curIdx = trackLessons.findIndex((x) => x.id === activeLessonId);
      const les = trackLessons[curIdx] || lessons.find((x) => x.id === activeLessonId);
      const prevLes = curIdx > 0 ? trackLessons[curIdx - 1] : null;
      const nextLes = curIdx >= 0 && curIdx < trackLessons.length - 1 ? trackLessons[curIdx + 1] : null;

      inner = `
        <div class="eg-toolbar no-print">
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="closeKaustLesson()" class="eg-btn">${isAr() ? '→' : '←'} ${L('جميع دروس المسار', 'All Track Lessons')}</button>
            <button type="button" onclick="toggleKaustSelfTest()" class="eg-btn${selfTestMode ? ' eg-tab-on' : ''}">
              ${selfTestMode ? '🧠 ' + L('وضع اختبر نفسك (مفعّل)', 'Self-Test Mode: ON') : '👁️ ' + L('جميع الحلول معروضة (اضغط للاختبار الذاتي)', 'All Solutions Shown (Try Self-Test)')}
            </button>
          </div>
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="printKaustLesson('${les.id}')" class="eg-btn eg-btn-main">🖨️ ${L('طباعة الدرس A4 بشعار المدرسة', 'Print Lesson (A4)')}</button>
            <button type="button" onclick="practiceKaustLesson('${les.id}')" class="eg-btn eg-btn-go">⚡ ${L('تدرّب على أسئلة الدرس', 'Practice Lesson')} (${qCount(les)})</button>
          </div>
        </div>
        <div class="eg-reader">${lessonBodyHtml(les, false)}</div>
        <div class="eg-nav-footer no-print">
          ${prevLes ? `<button type="button" onclick="openKaustLesson('${prevLes.id}')" class="eg-btn">${isAr() ? '→' : '←'} ${L('الدرس السابق:', 'Previous:')} ${prevLes.unit_num} ${pick(prevLes).title}</button>` : '<span></span>'}
          ${nextLes ? `<button type="button" onclick="openKaustLesson('${nextLes.id}')" class="eg-btn eg-btn-main">${L('الدرس التالي:', 'Next:')} ${nextLes.unit_num} ${pick(nextLes).title} ${isAr() ? '←' : '→'}</button>` : '<span></span>'}
        </div>`;
    } else {
      const cards = lessons.filter((x) => x.level === activeTrack).map((les) => {
        const d = pick(les);
        const solvedCount = (d.examples || []).length + (les.bank_example_ids || []).length;
        const qc = qCount(les);
        return `<div class="eg-lesson-card">
          <div>
            <div class="flex flex-wrap items-center justify-between gap-1.5 mb-2">
              <div class="flex items-center gap-1.5">
                <span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span>
                <span class="eg-badge eg-badge-alt">${topicLabel(les.topic)}</span>
              </div>
              <span class="eg-lc-pill">${solvedCount} ${L('أمثلة محلولة', 'Solved Examples')}</span>
            </div>
            <h3 class="eg-lc-title" onclick="openKaustLesson('${les.id}')">${d.title}</h3>
            <p class="eg-lc-desc math-font">${d.summary}</p>
          </div>
          <div class="eg-lc-actions">
            <button type="button" onclick="openKaustLesson('${les.id}')" class="eg-btn eg-btn-main eg-btn-sm flex-1">📖 ${L('اقرأ الشرح والأمثلة', 'Study Lesson')}</button>
            <button type="button" onclick="printKaustLesson('${les.id}')" class="eg-btn eg-btn-sm" title="${L('طباعة A4', 'Print A4')}">🖨️ A4</button>
            <button type="button" onclick="practiceKaustLesson('${les.id}')" class="eg-btn eg-btn-go eg-btn-sm" title="${L('تدريب', 'Practice')}">⚡ ${qc}</button>
          </div>
        </div>`;
      }).join('');

      inner = `
        <div class="eg-subbar no-print">
          <div class="text-xs sm:text-sm opacity-85">
            ✨ ${L('كل درس مصمّم بلغة واضحة ومبسّطة خطوة بخطوة مع رسوم هندسية ومخرجات طباعة A4 رسمية تحمل شعار المدرسة في كل صفحة.', 'Every lesson is written step-by-step for easy understanding, loaded with diagrams & worked examples, and formatted for A4 printing with the Edugates logo on every page.')}
          </div>
          <button type="button" onclick="printKaustTrackBooklet('${activeTrack}')" class="eg-btn eg-btn-main shrink-0">
            📚 ${L('طباعة مذكرة المسار كاملةً (A4)', 'Print Full Track Booklet (A4)')}
          </button>
        </div>
        <div class="eg-grid">${cards}</div>`;
    }

    const totalSolvedAll = lessons.reduce((a, x) => a + (x.en.examples || []).length + (x.bank_example_ids || []).length, 0);
    root.innerHTML = `<div class="eg-hub">
      <div class="eg-hub-h">
        <div class="eg-hub-logo-box"><img src="LOGO.jpg" alt="Edugates International School" class="eg-hub-logo"></div>
        <div class="flex-1">
          <div class="eg-hub-kicker">Edugates International School · مدرسة بوابة المعرفة العالمية</div>
          <h2 class="text-2xl sm:text-3xl font-display font-extrabold">📖 ${L('أكاديمية شرح دروس مسابقة كاوست للرياضيات (KMC)', 'KAUST Math Competition (KMC) Study Lessons')}</h2>
          <p class="text-xs sm:text-sm opacity-80 mt-1">${L(`18 درساً شاملاً · ${totalSolvedAll} مثالاً محلولاً بالتفصيل · رسوم توضيحية دقيقة · طباعة A4 رسمية بشعار المدرسة على جميع الصفحات`, `18 Complete Lessons · ${totalSolvedAll} Step-by-Step Solved Examples · Past-Paper Diagrams · Branded A4 Printouts`)}</p>
        </div>
      </div>
      <div class="eg-tabs no-print">${tabs}</div>
      ${inner}
    </div>`;

    if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
      MathJax.typesetPromise([root]).catch(() => {});
    }
  }

  async function init() {
    let sec = document.getElementById('study-lessons');
    if (!sec) {
      const practice = document.getElementById('practice');
      if (!practice || !practice.parentNode) return;
      sec = document.createElement('section');
      sec.id = 'study-lessons';
      sec.className = 'no-print-section';
      practice.parentNode.insertBefore(sec, practice);
    }
    try {
      const res = await fetch('data/kaust_lessons.json');
      if (res.ok) lessons = (await res.json()).lessons || [];
    } catch (e) {
      console.error('Failed to load KAUST study lessons:', e);
      return;
    }
    const t0 = Date.now();
    while (!getBankQuestions().length && Date.now() - t0 < 15000) {
      await new Promise((r) => setTimeout(r, 80));
    }
    render();
    if (typeof window.toggleLanguage === 'function' && !window.__kaustLangHooked) {
      window.__kaustLangHooked = true;
      const origToggle = window.toggleLanguage;
      window.toggleLanguage = function () {
        const res = origToggle.apply(this, arguments);
        render();
        return res;
      };
    }
    if (typeof window.setGradeFilter === 'function' && !window.__kaustGradeHooked) {
      window.__kaustGradeHooked = true;
      const origGrade = window.setGradeFilter;
      window.setGradeFilter = function (g) {
        const res = origGrade.apply(this, arguments);
        if (g === 6 || g === 7) { activeTrack = TRACKS[0].level; activeLessonId = null; render(); }
        else if (g === 8 || g === 9) { activeTrack = TRACKS[1].level; activeLessonId = null; render(); }
        else if (g === 10 || g === 11) { activeTrack = TRACKS[2].level; activeLessonId = null; render(); }
        return res;
      };
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.__kaustStudy = {
    get lessons() { return lessons; },
    render,
    lessonBlocks,
    lessonBodyHtml,
  };
})();
