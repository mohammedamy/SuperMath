/* KAUST (KMC) & NSMO (Mawhiba) Study Academy + Interactive Practice Drills + Edugates International School Multi-Page A4 Print Engine */
(function () {
  'use strict';

  const LABELS = ['A', 'B', 'C', 'D', 'E'];

  const COMP_CONFIG = {
    kaust: {
      id: 'kaust',
      bpField: 'kmc_blueprint',
      quizSelectId: 'quiz-kaust-phase-select',
      pillEn: '🏛️ KAUST KMC (Grades 6–11 · 5 Options)',
      pillAr: '🏛️ مسابقة كاوست KMC (الصفوف 6–11 · 5 خيارات)',
      hubTitleEn: 'KAUST Math Competition (KMC) Study Lessons',
      hubTitleAr: 'أكاديمية شرح دروس مسابقة كاوست للرياضيات (KMC)',
      badgeEn: 'KAUST KMC',
      badgeAr: 'كاوست KMC',
      bankTagEn: 'KMC Bank',
      bankTagAr: 'من بنك كاوست',
      trapsTitleEn: 'Watch Out — Common KMC Exam Traps!',
      trapsTitleAr: 'احذر هذه الأخطاء الشائعة في اختبار كاوست!',
      tracks: [
        { level: 'Track 1: Grades 6-7', en: 'Track 1 · Grades 6–7', ar: 'المسار ١ · الصفوف 6–7', shortEn: 'Grades 6–7', shortAr: 'الصفوف 6–7' },
        { level: 'Track 2: Grades 8-9', en: 'Track 2 · Grades 8–9', ar: 'المسار ٢ · الصفوف 8–9', shortEn: 'Grades 8–9', shortAr: 'الصفوف 8–9' },
        { level: 'Track 3: Grades 10-11', en: 'Track 3 · Grades 10–11', ar: 'المسار ٣ · الصفوف 10–11', shortEn: 'Grades 10–11', shortAr: 'الصفوف 10–11' },
      ],
    },
    nsmo: {
      id: 'nsmo',
      bpField: 'nsmo_blueprint',
      quizSelectId: 'quiz-nsmo-phase-select',
      pillEn: '🥇 NSMO · Mawhiba (Grades 7–10 · 4 Options)',
      pillAr: '🥇 أولمبياد نسمو — موهبة (الصفوف 7–10 · 4 خيارات)',
      hubTitleEn: 'NSMO / Mawhiba National Olympiad Study Lessons',
      hubTitleAr: 'أكاديمية شرح دروس أولمبياد نسمو الوطني — موهبة',
      badgeEn: 'NSMO Mawhiba',
      badgeAr: 'نسمو موهبة',
      bankTagEn: 'NSMO Bank',
      bankTagAr: 'من بنك نسمو',
      trapsTitleEn: 'Watch Out — Common Mawhiba / NSMO Olympiad Traps!',
      trapsTitleAr: 'احذر هذه الأخطاء الشائعة في أولمبياد نسمو (موهبة)!',
      tracks: [
        { level: 'Phase 1: Junior Olympiad (Grade 7)', en: 'Phase 1 · Grade 7 (Junior)', ar: 'المرحلة ١ · الصف 7 (الناشئين)', shortEn: 'Grade 7', shortAr: 'الصف 7' },
        { level: 'Phase 2: Intermediate Olympiad (Grades 8-9)', en: 'Phase 2 · Grades 8–9 (Intermediate)', ar: 'المرحلة ٢ · الصفان 8–9 (المتوسط)', shortEn: 'Grades 8–9', shortAr: 'الصفان 8–9' },
        { level: 'Phase 3: Senior National Olympiad (Grade 10)', en: 'Phase 3 · Grade 10 (Senior)', ar: 'المرحلة ٣ · الصف 10 (المتقدم)', shortEn: 'Grade 10', shortAr: 'الصف 10' },
      ],
    },
    kangaroo: {
      id: 'kangaroo',
      bpField: 'kangaroo_blueprint',
      quizSelectId: 'quiz-kangaroo-level-select',
      pillEn: '🦘 Kangaroo Math (Grades 1–12 · 5 Options)',
      pillAr: '🦘 كانجارو موهبة (الصفوف 1–12 · 5 خيارات)',
      hubTitleEn: 'Kangaroo Math Competition Study Lessons (Grades 1–12)',
      hubTitleAr: 'أكاديمية شرح دروس مسابقة كانجارو موهبة للرياضيات (الصفوف 1–12)',
      badgeEn: 'Kangaroo Math',
      badgeAr: 'كانجارو موهبة',
      bankTagEn: 'Kangaroo Bank',
      bankTagAr: 'من بنك كانجارو',
      trapsTitleEn: 'Watch Out — Common Kangaroo Math Puzzle Traps!',
      trapsTitleAr: 'احذر هذه الأخطاء الشائعة في ألغاز مسابقة كانجارو!',
      tracks: [
        { level: 'PreEcolier', en: 'PreEcolier · Grades 1–2', ar: 'بري إيكولير · الصفان 1–2', shortEn: 'Grades 1–2 (PreEcolier)', shortAr: 'الصفان 1–2 (بري إيكولير)' },
        { level: 'Ecolier', en: 'Ecolier · Grades 3–4', ar: 'إيكولير · الصفان 3–4', shortEn: 'Grades 3–4 (Ecolier)', shortAr: 'الصفان 3–4 (إيكولير)' },
        { level: 'Benjamin', en: 'Benjamin · Grades 5–6', ar: 'بنجامين · الصفان 5–6', shortEn: 'Grades 5–6 (Benjamin)', shortAr: 'الصفان 5–6 (بنجامين)' },
        { level: 'Cadet', en: 'Cadet · Grades 7–8', ar: 'كاديت · الصفان 7–8', shortEn: 'Grades 7–8 (Cadet)', shortAr: 'الصفان 7–8 (كاديت)' },
        { level: 'Junior', en: 'Junior · Grades 9–10', ar: 'جونيور · الصفان 9–10', shortEn: 'Grades 9–10 (Junior)', shortAr: 'الصفان 9–10 (جونيور)' },
        { level: 'Student', en: 'Student · Grades 11–12', ar: 'ستيودنت · الصفان 11–12', shortEn: 'Grades 11–12 (Student)', shortAr: 'الصفان 11–12 (ستيودنت)' },
      ],
    },
    nafes: {
      id: 'nafes',
      bpField: 'nafes_blueprint',
      quizSelectId: 'quiz-nafes-grade-select',
      pillEn: '🇸🇦 Nafes KSA (Grades 3, 6 & 9 · 4 Options)',
      pillAr: '🇸🇦 اختبارات نافس الوطنية (الصفوف 3 و6 و9 · 4 خيارات)',
      hubTitleEn: 'Nafes KSA National Assessment (ETEC) Study Lessons',
      hubTitleAr: 'أكاديمية شرح دروس اختبارات نافس الوطنية — هيئة تقويم التعليم والتدريب',
      badgeEn: 'Nafes KSA',
      badgeAr: 'نافس الوطني',
      bankTagEn: 'Nafes Bank',
      bankTagAr: 'من بنك نافس',
      trapsTitleEn: 'Watch Out — Common ETEC Nafes Assessment Traps!',
      trapsTitleAr: 'احذر هذه الأخطاء الشائعة في اختبارات نافس الوطنية!',
      tracks: [
        { level: 'Grade 3', en: 'Grade 3 · Primary Benchmark', ar: 'الصف الثالث الابتدائي (نافس 3)', shortEn: 'Grade 3 (Primary)', shortAr: 'الصف الثالث الابتدائي' },
        { level: 'Grade 6', en: 'Grade 6 · Upper Primary Benchmark', ar: 'الصف السادس الابتدائي (نافس 6)', shortEn: 'Grade 6 (Primary)', shortAr: 'الصف السادس الابتدائي' },
        { level: 'Grade 9', en: 'Grade 9 · Intermediate Benchmark', ar: 'الصف الثالث المتوسط (نافس 9)', shortEn: 'Grade 9 (Intermediate)', shortAr: 'الصف الثالث المتوسط' },
      ],
    },
  };

  const TOPIC_AR = {
    'Numbers & Operations': 'الأعداد والعمليات عليها',
    'Number Theory': 'نظرية الأعداد',
    'Algebra': 'الجبر والأنماط',
    'Geometry': 'الهندسة والقياس',
    'Combinatorics & Logic': 'التوافيق والمنطق والاحتمالات',
    'Data & Probability': 'البيانات والاحتمالات',
  };
  const DIFF_AR = {
    Easy: 'سهل',
    Medium: 'متوسط',
    Hard: 'متقدم',
  };

  let kaustLessons = [];
  let nsmoLessons = [];
  let kangarooLessons = [];
  let nafesLessons = [];
  let activeComp = 'kaust';
  let activeTrackByComp = {
    kaust: COMP_CONFIG.kaust.tracks[0].level,
    nsmo: COMP_CONFIG.nsmo.tracks[0].level,
    kangaroo: COMP_CONFIG.kangaroo.tracks[0].level,
    nafes: COMP_CONFIG.nafes.tracks[0].level,
  };
  let activeLessonId = null;
  let selfTestMode = false;
  let revealedExamples = new Set();
  let selectedTryChoice = {};
  let drillChoice = {};
  let revealedDrills = new Set();
  let shownDrillHints = new Set();

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const pick = (o) => (o[isAr() ? 'ar' : 'en'] || o.en);
  const topicLabel = (tp) => (isAr() ? (TOPIC_AR[tp] || tp) : tp);
  const diffLabel = (df) => (isAr() ? (DIFF_AR[df] || df) : df);
  const getBankQuestions = () => (typeof appData !== 'undefined' && Array.isArray(appData.questions) ? appData.questions : []);

  function allLessons() {
    return kaustLessons.concat(nsmoLessons, kangarooLessons, nafesLessons);
  }

  function currentLessons() {
    if (activeComp === 'nafes') return nafesLessons;
    if (activeComp === 'nsmo') return nsmoLessons;
    if (activeComp === 'kangaroo') return kangarooLessons;
    return kaustLessons;
  }

  function compForLesson(les) {
    if (!les) return COMP_CONFIG[activeComp];
    if (les.track === 'nafes' || String(les.id || '').startsWith('NAFS-') || ['Grade 3', 'Grade 6', 'Grade 9'].includes(les.level)) {
      return COMP_CONFIG.nafes;
    }
    if (les.track === 'kangaroo' || String(les.id || '').startsWith('KANG-') || ['PreEcolier', 'Ecolier', 'Benjamin', 'Cadet', 'Junior', 'Student'].includes(les.level)) {
      return COMP_CONFIG.kangaroo;
    }
    if (les.track === 'nsmo' || String(les.id || '').startsWith('NSMO-') || String(les.level || '').startsWith('Phase ')) {
      return COMP_CONFIG.nsmo;
    }
    return COMP_CONFIG.kaust;
  }

  function trackMetaForLesson(les) {
    const cfg = compForLesson(les);
    return cfg.tracks.find((t) => t.level === les.level) || cfg.tracks[0];
  }

  function bankExamples(les) {
    const qs = getBankQuestions();
    if (!qs.length) return [];
    const cfg = compForLesson(les);
    const byId = new Map(qs.map((q) => [q.id, q]));
    return (les.bank_example_ids || [])
      .map((id) => byId.get(id))
      .filter(Boolean)
      .map((q, idx) => {
        const c = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
        const diffBadge = q.difficulty ? ` (${diffLabel(q.difficulty)})` : '';
        return {
          id: q.id,
          correct_index: q.correct_index,
          title: L(
            `تطبيق إضافي محلول ${idx + 1} (${cfg.bankTagAr})${diffBadge}`,
            `Extra ${cfg.badgeEn} Worked Example ${idx + 1}${diffBadge}`
          ),
          question: c.question || '',
          options: c.options || [],
          explanation: c.explanation || '',
          diagram: c.diagram || q.diagram || '',
          fromBank: true,
          bankTagAr: cfg.bankTagAr,
          bankTagEn: cfg.bankTagEn,
        };
      });
  }

  function lessonDrillQuestions(les) {
    const qs = getBankQuestions();
    if (!qs.length) return [];
    const byId = new Map(qs.map((q) => [q.id, q]));
    return (les.drill_ids || []).map((id) => byId.get(id)).filter(Boolean);
  }

  function lessonDrills(les) {
    return lessonDrillQuestions(les).map((q) => {
      const c = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
      return {
        id: q.id,
        difficulty: q.difficulty || 'Medium',
        topic: q.topic || les.topic,
        correct_index: q.correct_index,
        question: c.question || '',
        options: c.options || [],
        hint: c.hint || '',
        explanation: c.explanation || '',
        diagram: c.diagram || q.diagram || '',
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
      ? `<span class="eg-ex-tag eg-ex-tag-bank">${L(ex.bankTagAr || 'من البنك', ex.bankTagEn || 'Contest Bank')}</span>`
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

  function drillCardHtml(lesId, dr, num, forPrint) {
    const dKey = `${lesId}:${dr.id}`;
    const chosen = drillChoice[dKey];
    const isRevealed = !forPrint && revealedDrills.has(dKey);
    const showHint = !forPrint && shownDrillHints.has(dKey);
    const diffCls = dr.difficulty === 'Easy' ? 'eg-diff-easy' : (dr.difficulty === 'Hard' ? 'eg-diff-hard' : 'eg-diff-med');

    const opts = (dr.options || []).map((opt, idx) => {
      if (forPrint) {
        return `<div class="eg-ws-opt"><span class="eg-opt-l">${LABELS[idx]}</span><span class="math-font eg-opt-txt">${opt}</span></div>`;
      }
      const isCorrect = idx === dr.correct_index;
      let cls = 'eg-opt eg-opt-interactive';
      let badge = '';
      if (isRevealed && isCorrect) {
        cls = 'eg-opt eg-opt-ok';
        badge = '<span class="eg-tick" aria-hidden="true">✓</span>';
      } else if (chosen === idx && isCorrect) {
        cls = 'eg-opt eg-opt-ok';
        badge = '<span class="eg-tick" aria-hidden="true">✓</span>';
      } else if (chosen === idx && !isCorrect) {
        cls += ' eg-opt-wrong';
        badge = '<span class="eg-cross" aria-hidden="true">✗</span>';
      }
      if (isRevealed) {
        return `<div class="${cls}"><span class="eg-opt-l">${LABELS[idx]}</span><span class="math-font eg-opt-txt">${opt}</span>${badge}</div>`;
      }
      return `<button type="button" onclick="answerKaustDrill('${dKey}', ${idx})" class="${cls}"><span class="eg-opt-l">${LABELS[idx]}</span><span class="math-font eg-opt-txt">${opt}</span>${badge}</button>`;
    }).join('');

    const interactiveFooter = forPrint
      ? ''
      : `
        <div class="eg-drill-actions no-print">
          <div class="flex flex-wrap items-center gap-2">
            ${dr.hint ? `<button type="button" onclick="toggleKaustDrillHint('${dKey}')" class="eg-btn eg-btn-sm">💡 ${showHint ? L('إخفاء التلميح', 'Hide Hint') : L('تلميح ذكي', 'Hint')}</button>` : ''}
            ${!isRevealed ? `<button type="button" onclick="revealKaustDrill('${dKey}')" class="eg-btn eg-btn-sm">👁️ ${L('إظهار الحل التفصيلي', 'Show Step-by-Step Solution')}</button>` : ''}
          </div>
          <span class="eg-drill-id">${dr.id}</span>
        </div>
        ${showHint && dr.hint ? `<div class="eg-drill-hint math-font no-print">💡 <strong>${L('تلميح:', 'Hint:')}</strong> ${dr.hint}</div>` : ''}
        ${isRevealed ? `<div class="eg-sol no-print">
          <div class="eg-sol-h">✅ ${L('الإجابة الصحيحة', 'Correct Answer')}: (${LABELS[dr.correct_index]}) — ${L('الشرح التفصيلي', 'Step-by-Step Solution')}</div>
          <div class="math-font eg-prose">${dr.explanation}</div>
        </div>` : ''}`;

    return `<div class="eg-card eg-drill no-break">
      <div class="eg-ex-top">
        <div class="eg-drill-h">📝 ${L('تدريب تطبيقي', 'Practice Drill')} ${num}</div>
        <div class="flex items-center gap-1.5">
          <span class="eg-diff-pill ${diffCls}">${diffLabel(dr.difficulty)}</span>
        </div>
      </div>
      <div class="eg-q math-font">${dr.question}</div>
      ${dr.diagram ? `<div class="eg-diagram">${dr.diagram}</div>` : ''}
      <div class="${forPrint ? 'eg-ws-opts' : 'eg-opts'}">${opts}</div>
      ${interactiveFooter}
    </div>`;
  }

  function lessonBlocks(les, forPrint) {
    const d = pick(les);
    const cfg = compForLesson(les);
    const tr = trackMetaForLesson(les);
    const exs = allExamplesFor(les);
    const drills = lessonDrills(les);

    const bannerAndGoals = `
      <div class="eg-banner no-break">
        <div class="eg-banner-meta">
          <span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span>
          <span class="eg-badge eg-badge-alt">${topicLabel(les.topic)}</span>
          <span class="eg-badge eg-badge-soft">${isAr() ? tr.ar : tr.en} · ${isAr() ? cfg.badgeAr : cfg.badgeEn}</span>
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
        <div class="eg-h3">⚠️ ${L(cfg.trapsTitleAr, cfg.trapsTitleEn)}</div>
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

    let drillBlocks = [];
    if (drills.length) {
      const solvedDrills = drills.filter((dr) => drillChoice[`${les.id}:${dr.id}`] === dr.correct_index).length;
      const allDrillsOpen = drills.every((dr) => revealedDrills.has(`${les.id}:${dr.id}`));

      const drillIntro = forPrint
        ? `<div class="eg-sec-heading">📝 ${L('تدريبات الطالب للتطبيق الذاتي — حلّ بدون آلة حاسبة', 'End-of-Lesson Student Practice Drills — Solve Without Calculator')} (${drills.length})</div>`
        : `<div class="eg-drill-bar no-print">
            <div>
              <div class="eg-sec-heading" style="margin:0;border:0;padding:0">📝 ${L('تدريبات نهاية الدرس — اختبر فهمك الآن', 'End-of-Lesson Practice Drills — Test Your Mastery')} (${drills.length})</div>
              <p class="text-xs opacity-80 mt-0.5">${L('مدرّجة من السهل إلى المتقدم تماماً مثل ورقة المسابقة الرسمية. اختر الإجابة للتحقق الفوري أو اطبعها كورقة عمل مستقلة!', 'Graduated Easy → Medium → Hard just like an official competition paper. Click an option to check instantly, or print as a standalone A4 worksheet!')}</p>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <span class="eg-lc-pill">${L('النتيجة:', 'Solved:')} ${solvedDrills} / ${drills.length}</span>
              <button type="button" onclick="toggleAllKaustDrills('${les.id}')" class="eg-btn eg-btn-sm">${allDrillsOpen ? '🔄 ' + L('إعادة ضبط التدريبات', 'Reset Drills') : '👁️ ' + L('إظهار جميع الحلول', 'Show All Solutions')}</button>
              <button type="button" onclick="printKaustLessonDrills('${les.id}')" class="eg-btn eg-btn-main eg-btn-sm">🖨️ ${L('طباعة ورقة التدريبات (A4)', 'Print Drills Worksheet (A4)')}</button>
            </div>
          </div>`;

      drillBlocks = drills.map((dr, i) => {
        const card = drillCardHtml(les.id, dr, i + 1, forPrint);
        return i === 0 ? `<div class="no-break">${drillIntro}${card}</div>` : card;
      });

      if (forPrint) {
        const keyCells = drills.map((dr, idx) => `<div class="eg-key-cell" dir="ltr"><strong>${idx + 1}.</strong> <span>(${LABELS[dr.correct_index]})</span></div>`).join('');
        drillBlocks.push(`<div class="eg-key-box no-break">
          <div class="eg-h3">🔑 ${L('مفتاح إجابات تدريبات نهاية الدرس', 'Answer Key — End-of-Lesson Practice Drills')} (${L('درس', 'Lesson')} ${les.unit_num})</div>
          <div class="eg-key-grid">${keyCells}</div>
        </div>`);
      }
    }

    return [bannerAndGoals, ...conceptBlocks, trapsBlock, ...exampleBlocks, ...drillBlocks];
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
              <div class="eg-logo-wrap"><img src="LOGO.jpg" alt="Edugates International School" loading="eager" decoding="sync" class="eg-logo"></div>
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
                <img src="LOGO.jpg" alt="" loading="eager" decoding="sync" class="eg-logo-sm">
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

  /* Reusable Adaptive 4-Option (A–D) or 5-Option (A–E) Optical OMR Bubble Grid */
  window.buildEdugatesOmrSheetHtml = function (totalQ, optCount, shadedMap, studentAnswers, rtl, scoreTag) {
    const nOpts = optCount === 4 ? 4 : 5;
    const optLabels = LABELS.slice(0, nOpts);
    const rangeTxt = `A–${optLabels[nOpts - 1]}`;
    const cols = totalQ > 32 ? 3 : 2;
    const perCol = Math.ceil(totalQ / cols);

    const colBlocks = [];
    for (let c = 0; c < cols; c++) {
      const sIdx = c * perCol;
      const eIdx = Math.min(totalQ, (c + 1) * perCol);
      if (sIdx >= eIdx) continue;
      const rows = [];
      for (let i = sIdx; i < eIdx; i++) {
        const correctOpt = shadedMap ? shadedMap[i] : null;
        const studentOpt = studentAnswers ? studentAnswers[i] : null;
        const bubbles = optLabels.map((lbl, oIdx) => {
          let cls = 'eg-omr-bubble';
          if (correctOpt === oIdx) cls += ' eg-omr-shaded';
          else if (studentOpt === oIdx && correctOpt !== null && studentOpt !== correctOpt) cls += ' eg-omr-wrong';
          return `<span class="${cls}">${lbl}</span>`;
        }).join('');
        rows.push(`<div class="eg-omr-row" dir="ltr">
          <span class="eg-omr-qnum">${i + 1}.</span>
          <div class="eg-omr-bubbles">${bubbles}</div>
        </div>`);
      }
      colBlocks.push(`<div class="eg-omr-col">${rows.join('')}</div>`);
    }

    const legend = shadedMap
      ? `<div class="eg-omr-legend">${
          rtl
            ? `● الدائرة المظللة (${rangeTxt}) تمثل الإجابة الصحيحة المعتمدة في مفتاح التصحيح.`
            : `● Filled dark bubble (${rangeTxt}) indicates the official correct answer choice.`
        }</div>`
      : `<div class="eg-omr-legend">${
          rtl
            ? `ظلّل دائرة واحدة فقط (${rangeTxt}) لكل سؤال بقلم رصاص داكن أو حبر جاف: ● (صحيح)   ✗ ○ (خطأ)`
            : `Shade ONE bubble (${rangeTxt}) completely per question using dark pen/pencil: ● (valid)   ✗ ○ (invalid)`
        }</div>`;

    return `<div class="eg-omr-sheet no-break">
      <div class="eg-omr-head">
        <span>🫧 ${
          shadedMap
            ? rtl
              ? `نموذج التظليل البصري المظلل (OMR Master Key · 1–${totalQ})`
              : `Pre-Shaded Master OMR Answer Sheet (Questions 1–${totalQ})`
            : rtl
            ? `ورقة رصد وتظليل الإجابات البصرية (OMR Answer Sheet · 1–${totalQ})`
            : `Official OMR Optical Answer Bubble Sheet (Questions 1–${totalQ})`
        }</span>
        <span class="eg-omr-tag" dir="ltr">${scoreTag || rangeTxt}</span>
      </div>
      ${legend}
      <div class="eg-omr-cols${cols === 3 ? ' eg-omr-cols-3' : ''}" dir="ltr">
        ${colBlocks.join('')}
      </div>
    </div>`;
  };

  /* Dedicated row-paginated Practice Worksheet + Optional OMR Cover + Scratch Boxes + Answer Key builder */
  window.buildEdugatesWorksheetHtml = function (questionsToPrint, docTitle, answerKeyTitle, qLabel, badgeText, includeSolutions, rtl, customOpts) {
    const opts = customOpts || {};
    const keyMode = opts.keyMode || (includeSolutions ? 'full' : 'quick');
    const scratchSpace = opts.scratchSpace || 'none'; // 'none' | 'medium' | 'large'
    const subtitle = opts.subtitle ? String(opts.subtitle).trim() : '';
    const includeOmr = !!opts.includeOmr;

    const mcqCount = questionsToPrint.filter((q) => q.type === 'MCQ').length;
    const maxOptLen = questionsToPrint.reduce((mx, q) => {
      const c = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
      return Math.max(mx, Array.isArray(c.options) ? c.options.length : 0);
    }, 4);
    const optCount = maxOptLen >= 5 ? 5 : 4;

    const subtitleBanner = subtitle
      ? `<div class="eg-ws-subtitle">${subtitle}</div>`
      : '';

    const studentBar = `<div class="eg-student-bar">
      <div><strong>${rtl ? 'اسم الطالب/ـة:' : 'Student Name:'}</strong> ___________________________</div>
      <div><strong>${rtl ? 'الصف / الشعبة:' : 'Grade / Class:'}</strong> __________</div>
      <div><strong>${rtl ? 'الدرجة:' : 'Score:'}</strong> ____ / ${questionsToPrint.length}</div>
    </div>`;

    const scratchLabel = rtl ? 'مساحة خطوات الحل والمسودة:' : 'Scratch Work & Reasoning:';
    const scratchHtml = scratchSpace === 'large'
      ? `<div class="eg-scratch-box eg-scratch-lg"><span>${scratchLabel}</span></div>`
      : scratchSpace === 'medium'
      ? `<div class="eg-scratch-box eg-scratch-md"><span>${scratchLabel}</span></div>`
      : '';

    const qRows = questionsToPrint.map((q, index) => {
      const qContent = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
      const diag = qContent.diagram || q.diagram || '';
      let optsHtml = '';
      if (qContent.options && qContent.options.length > 0) {
        optsHtml = `<div class="eg-ws-opts">${qContent.options.map((opt, oIdx) => `
          <div class="eg-ws-opt">
            <span class="eg-opt-l">${LABELS[oIdx]}</span>
            <span class="math-font">${opt}</span>
          </div>`).join('')}</div>${scratchHtml}`;
      } else {
        optsHtml = `<div class="eg-frq-box${scratchSpace === 'large' ? ' eg-frq-box-lg' : ''}"></div>`;
      }
      const card = `<div class="eg-ws-q no-break">
        <div class="eg-ws-qh"><span>${qLabel} ${index + 1}</span><span class="eg-ws-qmeta">${topicLabel(q.topic || '')}${q.difficulty ? ' · ' + diffLabel(q.difficulty) : ''}${q.kang_points ? ' · ' + q.kang_points + (rtl ? ' نقاط' : ' pts') : ''}</span></div>
        <div class="eg-q math-font">${qContent.question || ''}</div>
        ${diag ? `<div class="eg-diagram">${diag}</div>` : ''}
        ${optsHtml}
      </div>`;
      if (index === 0 && !includeOmr) {
        return `<div class="no-break">${subtitleBanner}${studentBar}${card}</div>`;
      }
      return card;
    });

    const parts = [];

    if (includeOmr && mcqCount > 0) {
      const omrCover = `<div class="eg-mock-cover no-break">
        <div class="eg-mock-cover-top">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="eg-badge">${badgeText}</span>
            <span class="eg-badge eg-badge-soft">${rtl ? 'بدون آلة حاسبة · ورق A4 رسمي' : 'No Calculator · Official A4 Sheet'}</span>
          </div>
          <h2 class="eg-mock-cover-title">${docTitle}</h2>
          ${subtitle ? `<div class="text-xs font-semibold opacity-80 mb-1">${subtitle}</div>` : ''}
          <div class="eg-mock-cover-specs">
            <span><strong>${rtl ? 'عدد الأسئلة:' : 'Total Questions:'}</strong> ${questionsToPrint.length} (${optCount === 5 ? 'A–E' : 'A–D'})</span>
            <span><strong>${rtl ? 'تعليمات:' : 'Instructions:'}</strong> ${rtl ? 'ظلّل دائرة واحدة فقط لكل سؤال في ورقة الرصد أدناه' : 'Shade exactly ONE bubble per question on the OMR grid below'}</span>
          </div>
        </div>
        <div class="eg-mock-cand-grid">
          <div><strong>${rtl ? 'اسم الطالب/ـة الرباعي:' : 'Student Full Name:'}</strong> _______________________________</div>
          <div><strong>${rtl ? 'الصف والشعبة:' : 'Grade / Section:'}</strong> ___________________</div>
          <div><strong>${rtl ? 'الرقم الأكاديمي:' : 'Student ID:'}</strong> ___________________</div>
          <div><strong>${rtl ? 'التاريخ:' : 'Date:'}</strong> ____ / ____ / 202__</div>
          <div><strong>${rtl ? 'الإجابات الصحيحة:' : 'Correct Answers:'}</strong> ______ / ${questionsToPrint.length}</div>
          <div><strong>${rtl ? 'الدرجة النهائية:' : 'Final Score:'}</strong> ____________</div>
        </div>
        ${window.buildEdugatesOmrSheetHtml(questionsToPrint.length, optCount, null, null, rtl, optCount === 5 ? 'A–E' : 'A–D')}
      </div>`;
      parts.push(window.edugatesPrintSection([omrCover], docTitle, badgeText, rtl, false));
      parts.push(window.edugatesPrintSection(qRows, `${docTitle} — ${rtl ? 'الأسئلة' : 'Questions'}`, badgeText, rtl, true));
    } else {
      parts.push(window.edugatesPrintSection(qRows, docTitle, badgeText, rtl, false));
    }

    if (keyMode !== 'none') {
      const shadedMap = {};
      questionsToPrint.forEach((q, idx) => {
        if (q.type === 'MCQ' && typeof q.correct_index === 'number') shadedMap[idx] = q.correct_index;
      });

      const keyGrid = `<div class="eg-key-box no-break">
        <div class="eg-h3">${answerKeyTitle}</div>
        <div class="eg-key-grid">
          ${questionsToPrint.map((q, idx) => {
            const ans = (q.type === 'MCQ' && q.correct_index !== undefined && q.correct_index !== null)
              ? LABELS[q.correct_index]
              : 'FRQ';
            return `<div class="eg-key-cell" dir="ltr"><strong>${idx + 1}.</strong> <span>${ans}</span></div>`;
          }).join('')}
        </div>
      </div>`;

      const showDetailed = keyMode === 'full';
      const detailItems = questionsToPrint
        .map((q, idx) => ({ q, idx }))
        .filter(({ q }) => showDetailed || q.type !== 'MCQ')
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

      const keyRows = [
        ...(includeOmr && mcqCount > 0 ? [window.buildEdugatesOmrSheetHtml(questionsToPrint.length, optCount, shadedMap, null, rtl, 'KEY')] : []),
        keyGrid,
        ...detailItems,
      ];
      parts.push(window.edugatesPrintSection(keyRows, answerKeyTitle, badgeText, rtl, true));
    }

    return parts.join('');
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
    const les = allLessons().find((x) => x.id === id);
    if (!les) return;
    const cfg = compForLesson(les);
    const tr = trackMetaForLesson(les);
    const c = document.getElementById('print-container');
    const docTitle = `${L('شرح الدرس', 'Study Guide')} ${les.unit_num} — ${pick(les).title}`;
    const badge = `${isAr() ? tr.shortAr : tr.shortEn} · ${isAr() ? cfg.badgeAr : cfg.badgeEn} · A4`;
    c.innerHTML = window.edugatesPrintSection(lessonBlocks(les, true), docTitle, badge, isAr(), false);
    triggerContainerPrint(c);
  };

  window.printKaustLessonDrills = function (id) {
    const les = allLessons().find((x) => x.id === id);
    if (!les) return;
    const drillQs = lessonDrillQuestions(les);
    if (!drillQs.length) return;
    const cfg = compForLesson(les);
    const tr = trackMetaForLesson(les);
    const c = document.getElementById('print-container');
    const docTitle = `${L('ورقة تدريبات الدرس', 'Practice Drills Worksheet')} ${les.unit_num} — ${pick(les).title}`;
    const keyTitle = `${L('مفتاح الإجابات والحلول التفصيلية — درس', 'Answer Key & Step-by-Step Solutions — Lesson')} ${les.unit_num}`;
    const qLbl = L('تدريب', 'Drill');
    const badge = `${isAr() ? tr.shortAr : tr.shortEn} · ${L('ورقة تدريبات A4', 'A4 Drills')} · ${isAr() ? cfg.badgeAr : cfg.badgeEn}`;
    c.innerHTML = window.buildEdugatesWorksheetHtml(drillQs, docTitle, keyTitle, qLbl, badge, true, isAr());
    triggerContainerPrint(c);
  };

  window.printKaustTrackBooklet = function (level) {
    const ls = allLessons().filter((x) => x.level === level);
    if (!ls.length) return;
    const cfg = compForLesson(ls[0]);
    const tr = trackMetaForLesson(ls[0]);
    const c = document.getElementById('print-container');
    c.innerHTML = ls.map((les, idx) => {
      const docTitle = `${L('درس', 'Lesson')} ${les.unit_num} — ${pick(les).title}`;
      const badge = `${isAr() ? tr.shortAr : tr.shortEn} · ${isAr() ? cfg.badgeAr : cfg.badgeEn} · A4`;
      return window.edugatesPrintSection(lessonBlocks(les, true), docTitle, badge, isAr(), idx > 0);
    }).join('');
    triggerContainerPrint(c);
  };

  window.practiceKaustLesson = function (id) {
    const les = allLessons().find((x) => x.id === id);
    if (!les) return;
    const cfg = compForLesson(les);
    if (typeof currentSelectedGrade !== 'undefined') currentSelectedGrade = 'all';
    if (typeof renderGradeFilters === 'function') renderGradeFilters();
    const sel = document.getElementById('quiz-track-select');
    sel.value = cfg.id;
    filterQuestions();
    const phaseSel = document.getElementById(cfg.quizSelectId);
    if (phaseSel) phaseSel.value = les.level;
    filterQuestions();
    const bpSet = new Set(les.blueprints);
    currentFilteredQuestions = appData.questions.filter((q) => q.track === cfg.id && bpSet.has(q[cfg.bpField]));
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
    const les = allLessons().find((x) => x.id === activeLessonId);
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

  window.answerKaustDrill = function (dKey, choiceIdx) {
    drillChoice[dKey] = choiceIdx;
    const [lesId, qId] = dKey.split(':');
    const les = allLessons().find((x) => x.id === lesId);
    if (les) {
      const dr = lessonDrills(les).find((x) => x.id === qId);
      if (dr && choiceIdx === dr.correct_index) revealedDrills.add(dKey);
    }
    render();
  };

  window.toggleKaustDrillHint = function (dKey) {
    if (shownDrillHints.has(dKey)) shownDrillHints.delete(dKey);
    else shownDrillHints.add(dKey);
    render();
  };

  window.revealKaustDrill = function (dKey) {
    revealedDrills.add(dKey);
    render();
  };

  window.toggleAllKaustDrills = function (lesId) {
    const les = allLessons().find((x) => x.id === lesId);
    if (!les) return;
    const keys = (les.drill_ids || []).map((id) => `${lesId}:${id}`);
    const allOpen = keys.length > 0 && keys.every((k) => revealedDrills.has(k));
    keys.forEach((k) => {
      if (allOpen) {
        revealedDrills.delete(k);
        shownDrillHints.delete(k);
        delete drillChoice[k];
      } else {
        revealedDrills.add(k);
      }
    });
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

  window.setStudyCompetition = function (compId) {
    if (compId !== 'kaust' && compId !== 'nsmo' && compId !== 'kangaroo' && compId !== 'nafes') return;
    if (compId === 'nsmo' && !nsmoLessons.length) return;
    if (compId === 'kangaroo' && !kangarooLessons.length) return;
    if (compId === 'nafes' && !nafesLessons.length) return;
    activeComp = compId;
    activeLessonId = null;
    render();
  };

  window.openKaustLesson = function (id) {
    const les = allLessons().find((x) => x.id === id);
    if (les) {
      const cfg = compForLesson(les);
      activeComp = cfg.id;
      activeTrackByComp[cfg.id] = les.level;
    }
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
    if (['Grade 3', 'Grade 6', 'Grade 9'].includes(level)) {
      activeComp = 'nafes';
      activeTrackByComp.nafes = level;
    } else if (['PreEcolier', 'Ecolier', 'Benjamin', 'Cadet', 'Junior', 'Student'].includes(level)) {
      activeComp = 'kangaroo';
      activeTrackByComp.kangaroo = level;
    } else if (String(level || '').startsWith('Phase ')) {
      activeComp = 'nsmo';
      activeTrackByComp.nsmo = level;
    } else {
      activeComp = 'kaust';
      activeTrackByComp.kaust = level;
    }
    activeLessonId = null;
    render();
  };

  window.jumpToKaustStudy = function (levelOrComp) {
    if (levelOrComp === 'kaust' || levelOrComp === 'nsmo' || levelOrComp === 'kangaroo' || levelOrComp === 'nafes') {
      if (
        (levelOrComp !== 'nsmo' || nsmoLessons.length) &&
        (levelOrComp !== 'kangaroo' || kangarooLessons.length) &&
        (levelOrComp !== 'nafes' || nafesLessons.length)
      ) {
        activeComp = levelOrComp;
      }
      activeLessonId = null;
    } else if (levelOrComp) {
      window.setKaustTrack(levelOrComp);
    }
    render();
    const el = document.getElementById('study-lessons');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  function qCount(les) {
    const qs = getBankQuestions();
    if (!qs.length) return 0;
    const cfg = compForLesson(les);
    const s = new Set(les.blueprints);
    return qs.filter((q) => q.track === cfg.id && s.has(q[cfg.bpField])).length;
  }

  function render() {
    const root = document.getElementById('study-lessons');
    const lessons = currentLessons();
    if (!root || !lessons.length) return;
    root.setAttribute('dir', isAr() ? 'rtl' : 'ltr');

    const cfg = COMP_CONFIG[activeComp];
    const activeTrack = activeTrackByComp[activeComp];

    const compSwitcher = (nsmoLessons.length || kangarooLessons.length || nafesLessons.length)
      ? `<div class="eg-comp-switch no-print" role="tablist" aria-label="Study Competition">
          ${nafesLessons.length ? `<button type="button" onclick="setStudyCompetition('nafes')" class="eg-comp-btn${activeComp === 'nafes' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nafes.pillAr : COMP_CONFIG.nafes.pillEn}</button>` : ''}
          ${kangarooLessons.length ? `<button type="button" onclick="setStudyCompetition('kangaroo')" class="eg-comp-btn${activeComp === 'kangaroo' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.kangaroo.pillAr : COMP_CONFIG.kangaroo.pillEn}</button>` : ''}
          <button type="button" onclick="setStudyCompetition('kaust')" class="eg-comp-btn${activeComp === 'kaust' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.kaust.pillAr : COMP_CONFIG.kaust.pillEn}</button>
          ${nsmoLessons.length ? `<button type="button" onclick="setStudyCompetition('nsmo')" class="eg-comp-btn${activeComp === 'nsmo' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nsmo.pillAr : COMP_CONFIG.nsmo.pillEn}</button>` : ''}
        </div>`
      : '';

    const tabs = cfg.tracks.map((t) => {
      const tLessons = lessons.filter((x) => x.level === t.level);
      const exTotal = tLessons.reduce((acc, x) => acc + (pick(x).examples || []).length + (x.bank_example_ids || []).length, 0);
      const drTotal = tLessons.reduce((acc, x) => acc + (x.drill_ids || []).length, 0);
      return `<button type="button" onclick="setKaustTrack('${t.level}')" class="eg-tab${t.level === activeTrack ? ' eg-tab-on' : ''}">
        <span>${isAr() ? t.ar : t.en}</span>
        <span class="eg-tab-count">${tLessons.length} ${L('دروس', 'Lessons')} · ${exTotal} ${L('مثال', 'Ex')} · ${drTotal} ${L('تدريب', 'Drills')}</span>
      </button>`;
    }).join('');

    let inner;
    if (activeLessonId) {
      const trackLessons = lessons.filter((x) => x.level === activeTrack);
      const curIdx = trackLessons.findIndex((x) => x.id === activeLessonId);
      const les = trackLessons[curIdx] || allLessons().find((x) => x.id === activeLessonId);
      const prevLes = curIdx > 0 ? trackLessons[curIdx - 1] : null;
      const nextLes = curIdx >= 0 && curIdx < trackLessons.length - 1 ? trackLessons[curIdx + 1] : null;

      inner = `
        <div class="eg-toolbar no-print">
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="closeKaustLesson()" class="eg-btn">${isAr() ? '→' : '←'} ${L('جميع دروس المسار', 'All Track Lessons')}</button>
            <button type="button" onclick="toggleKaustSelfTest()" class="eg-btn${selfTestMode ? ' eg-tab-on' : ''}">
              ${selfTestMode ? '🧠 ' + L('وضع اختبر نفسك (مفعّل)', 'Self-Test Mode: ON') : '👁️ ' + L('الأمثلة المحلولة معروضة', 'Worked Solutions Shown')}
            </button>
          </div>
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="printKaustLesson('${les.id}')" class="eg-btn eg-btn-main">🖨️ ${L('طباعة الدرس + التدريبات (A4)', 'Print Lesson + Drills (A4)')}</button>
            <button type="button" onclick="printKaustLessonDrills('${les.id}')" class="eg-btn">📝 ${L('طباعة ورقة التدريبات فقط (A4)', 'Print Drills Sheet (A4)')}</button>
            <button type="button" onclick="practiceKaustLesson('${les.id}')" class="eg-btn eg-btn-go">⚡ ${L('بنك الدرس', 'Practice Bank')} (${qCount(les)})</button>
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
        const drillCount = (les.drill_ids || []).length;
        const qc = qCount(les);
        return `<div class="eg-lesson-card">
          <div>
            <div class="flex flex-wrap items-center justify-between gap-1.5 mb-2">
              <div class="flex items-center gap-1.5">
                <span class="eg-badge">${L('درس', 'Lesson')} ${les.unit_num}</span>
                <span class="eg-badge eg-badge-alt">${topicLabel(les.topic)}</span>
              </div>
              <span class="eg-lc-pill">${solvedCount} ${L('مثال محلول', 'Solved')} · ${drillCount} ${L('تدريبات', 'Drills')}</span>
            </div>
            <h3 class="eg-lc-title" onclick="openKaustLesson('${les.id}')">${d.title}</h3>
            <p class="eg-lc-desc math-font">${d.summary}</p>
          </div>
          <div class="eg-lc-actions">
            <button type="button" onclick="openKaustLesson('${les.id}')" class="eg-btn eg-btn-main eg-btn-sm flex-1">📖 ${L('الشرح والأمثلة والتدريبات', 'Study & Drills')}</button>
            <button type="button" onclick="printKaustLesson('${les.id}')" class="eg-btn eg-btn-sm" title="${L('طباعة الدرس A4', 'Print Lesson A4')}">🖨️ A4</button>
            <button type="button" onclick="printKaustLessonDrills('${les.id}')" class="eg-btn eg-btn-sm" title="${L('طباعة ورقة تدريبات الدرس A4', 'Print Drills Worksheet A4')}">📝</button>
            <button type="button" onclick="practiceKaustLesson('${les.id}')" class="eg-btn eg-btn-go eg-btn-sm" title="${L('بنك الأسئلة', 'Question Bank')}">⚡ ${qc}</button>
          </div>
        </div>`;
      }).join('');

      inner = `
        <div class="eg-subbar no-print">
          <div class="text-xs sm:text-sm opacity-85">
            ✨ ${L('كل درس مزوّد برسوم توضيحية وأمثلة محلولة خطوة بخطوة وتدريبات ختامية متدرجة قابلة للطباعة على ورق A4 بشعار مدرسة بوابة المعرفة العالمية في كل صفحة.', 'Every lesson includes custom diagrams, step-by-step solved examples, and graduated end-of-lesson practice drills — ready to print on A4 paper with the Edugates logo on every page.')}
          </div>
          <div class="flex flex-wrap gap-2 shrink-0">
            <button type="button" onclick="if(window.jumpToKaustMocks)jumpToKaustMocks('${activeTrack}');" class="eg-btn eg-btn-go">
              ⏱️ ${L('الاختبارات التجريبية الكاملة', 'Full Official Mock Exams')}
            </button>
            <button type="button" onclick="printKaustTrackBooklet('${activeTrack}')" class="eg-btn eg-btn-main">
              📚 ${L('طباعة مذكرة المسار كاملةً (A4)', 'Print Full Track Booklet (A4)')}
            </button>
          </div>
        </div>
        <div class="eg-grid">${cards}</div>`;
    }

    const totalSolvedAll = lessons.reduce((a, x) => a + (x.en.examples || []).length + (x.bank_example_ids || []).length, 0);
    const totalDrillsAll = lessons.reduce((a, x) => a + (x.drill_ids || []).length, 0);
    root.innerHTML = `<div class="eg-hub">
      <div class="eg-hub-h">
        <div class="eg-hub-logo-box"><img src="LOGO.jpg" alt="Edugates International School" loading="eager" decoding="sync" class="eg-hub-logo"></div>
        <div class="flex-1">
          <div class="eg-hub-kicker">Edugates International School · مدرسة بوابة المعرفة العالمية</div>
          <h2 class="text-2xl sm:text-3xl font-display font-extrabold">📖 ${isAr() ? cfg.hubTitleAr : cfg.hubTitleEn}</h2>
          <p class="text-xs sm:text-sm opacity-80 mt-1">${L(`${lessons.length} درساً مصوّراً · ${totalSolvedAll} مثالاً محلولاً بالتفصيل · ${totalDrillsAll} تدريباً تطبيقياً · طباعة A4 رسمية بشعار المدرسة على جميع الصفحات`, `${lessons.length} Illustrated Lessons · ${totalSolvedAll} Step-by-Step Solved Examples · ${totalDrillsAll} Printable Practice Drills · Branded A4 Printouts`)}</p>
        </div>
      </div>
      ${compSwitcher}
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
    const [kRes, nRes, gRes, fRes] = await Promise.allSettled([
      fetch('data/kaust_lessons.json'),
      fetch('data/nsmo_lessons.json'),
      fetch('data/kangaroo_lessons.json'),
      fetch('data/nafes_lessons.json'),
    ]);
    if (kRes.status === 'fulfilled' && kRes.value && kRes.value.ok) {
      try {
        kaustLessons = ((await kRes.value.json()).lessons) || [];
      } catch (_) {}
    }
    if (nRes.status === 'fulfilled' && nRes.value && nRes.value.ok) {
      try {
        nsmoLessons = ((await nRes.value.json()).lessons) || [];
      } catch (_) {}
    }
    if (gRes.status === 'fulfilled' && gRes.value && gRes.value.ok) {
      try {
        kangarooLessons = ((await gRes.value.json()).lessons) || [];
      } catch (_) {}
    }
    if (fRes.status === 'fulfilled' && fRes.value && fRes.value.ok) {
      try {
        nafesLessons = ((await fRes.value.json()).lessons) || [];
      } catch (_) {}
    }
    if (!kaustLessons.length && !nsmoLessons.length && !kangarooLessons.length && !nafesLessons.length) return;

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
        const navStudy = document.getElementById('nav-study-text');
        if (navStudy) navStudy.innerText = isAr() ? 'دروس المسابقات' : 'Study Academy';
        render();
        return res;
      };
    }
    if (typeof window.setGradeFilter === 'function' && !window.__kaustGradeHooked) {
      window.__kaustGradeHooked = true;
      const origGrade = window.setGradeFilter;
      window.setGradeFilter = function (g) {
        const res = origGrade.apply(this, arguments);
        if (activeComp === 'nafes') {
          if (g === 3) { activeTrackByComp.nafes = 'Grade 3'; activeLessonId = null; render(); }
          else if (g === 6) { activeTrackByComp.nafes = 'Grade 6'; activeLessonId = null; render(); }
          else if (g === 9) { activeTrackByComp.nafes = 'Grade 9'; activeLessonId = null; render(); }
        } else if (activeComp === 'kangaroo') {
          if (g === 1 || g === 2) { activeTrackByComp.kangaroo = 'PreEcolier'; activeLessonId = null; render(); }
          else if (g === 3 || g === 4) { activeTrackByComp.kangaroo = 'Ecolier'; activeLessonId = null; render(); }
          else if (g === 5 || g === 6) { activeTrackByComp.kangaroo = 'Benjamin'; activeLessonId = null; render(); }
          else if (g === 7 || g === 8) { activeTrackByComp.kangaroo = 'Cadet'; activeLessonId = null; render(); }
          else if (g === 9 || g === 10) { activeTrackByComp.kangaroo = 'Junior'; activeLessonId = null; render(); }
          else if (g === 11 || g === 12) { activeTrackByComp.kangaroo = 'Student'; activeLessonId = null; render(); }
        } else if (activeComp === 'nsmo') {
          if (g === 7) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[0].level; activeLessonId = null; render(); }
          else if (g === 8 || g === 9) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[1].level; activeLessonId = null; render(); }
          else if (g === 10) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[2].level; activeLessonId = null; render(); }
        } else {
          if (g === 6 || g === 7) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[0].level; activeLessonId = null; render(); }
          else if (g === 8 || g === 9) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[1].level; activeLessonId = null; render(); }
          else if (g === 10 || g === 11) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[2].level; activeLessonId = null; render(); }
        }
        return res;
      };
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.__kaustStudy = {
    get lessons() { return kaustLessons; },
    get nsmoLessons() { return nsmoLessons; },
    get kangarooLessons() { return kangarooLessons; },
    get nafesLessons() { return nafesLessons; },
    get allLessons() { return allLessons(); },
    get activeComp() { return activeComp; },
    render,
    lessonBlocks,
    lessonBodyHtml,
  };
})();
