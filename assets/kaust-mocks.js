/* KAUST Mathematics Competition (KMC) Official Full Mock Exams — Timed Simulator + Edugates A4 Print & OMR Suite */
(function () {
  const TRACKS = [
    {
      level: 'Track 1: Grades 6-7',
      code: 'T1',
      qCount: 24,
      en: 'Track 1 · Grades 6–7',
      ar: 'المسار 1 · الصفوف 6–7',
      shortEn: 'Grades 6–7 (Junior)',
      shortAr: 'الصفوف 6–7 (التأسيسي)',
    },
    {
      level: 'Track 2: Grades 8-9',
      code: 'T2',
      qCount: 24,
      en: 'Track 2 · Grades 8–9',
      ar: 'المسار 2 · الصفوف 8–9',
      shortEn: 'Grades 8–9 (Intermediate)',
      shortAr: 'الصفوف 8–9 (المتوسط)',
    },
    {
      level: 'Track 3: Grades 10-11',
      code: 'T3',
      qCount: 30,
      en: 'Track 3 · Grades 10–11',
      ar: 'المسار 3 · الصفوف 10–11',
      shortEn: 'Grades 10–11 (Senior)',
      shortAr: 'الصفوف 10–11 (المتقدم)',
    },
  ];

  const TOPIC_AR = {
    'Number Theory': 'نظرية الأعداد',
    Algebra: 'الجبر والأنماط',
    Geometry: 'الهندسة والقياس',
    'Combinatorics & Logic': 'التركيبات والمنطق',
    'Data & Probability': 'البيانات والاحتمالات',
  };

  const DIFF_AR = { Easy: 'أساسي (Part A)', Medium: 'متوسط (Part B)', Hard: 'متقدم (Part C)' };
  const DIFF_EN = { Easy: 'Part A · Easy', Medium: 'Part B · Medium', Hard: 'Part C · Hard' };
  const LABELS = ['A', 'B', 'C', 'D', 'E'];
  const STORAGE_KEY = 'supermath_kaust_mock_best_v1';

  let mocksDoc = null;
  let mocks = [];
  let customMocks = [];
  let activeTrack = TRACKS[0].level;
  let bestScores = {};

  // Active exam/review session state
  let session = null; // { mode: 'exam'|'review', paper, questions, answers: {}, flags: {}, currentIdx: 0, viewMode: 'single'|'all', remainingSec: 7200, elapsedSec: 0, paused: false, confirmSubmit: false, confirmExit: false, reviewFilter: 'all', report: null }
  let timerHandle = null;

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const pick = (obj) => (obj ? (isAr() ? obj.ar : obj.en) || obj.en || {} : {});
  const topicLabel = (t) => (isAr() ? TOPIC_AR[t] || t : t);

  const getBankQuestions = () =>
    typeof appData !== 'undefined' && Array.isArray(appData.questions) ? appData.questions : [];

  function loadBestScores() {
    try {
      if (typeof localStorage !== 'undefined' && typeof localStorage.getItem === 'function') {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) bestScores = JSON.parse(raw) || {};
      }
    } catch (_) {
      bestScores = {};
    }
  }

  function saveBestScore(paperId, score, maxPoints, correctCount, totalQ) {
    const prev = bestScores[paperId];
    if (!prev || score > prev.score) {
      bestScores[paperId] = { score, maxPoints, correctCount, totalQ };
      try {
        if (typeof localStorage !== 'undefined' && typeof localStorage.setItem === 'function') {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(bestScores));
        }
      } catch (_) {}
    }
  }

  function allPapers() {
    return [...mocks, ...customMocks];
  }

  function findPaper(id) {
    return allPapers().find((p) => p.id === id) || null;
  }

  function resolvePaperQuestions(paper) {
    const qs = getBankQuestions();
    if (!qs.length || !paper) return [];
    const byId = new Map(qs.filter((q) => q.track === 'kaust').map((q) => [q.id, q]));
    return (paper.question_ids || []).map((id) => byId.get(id)).filter(Boolean);
  }

  function formatClock(sec) {
    const s = Math.max(0, Math.floor(sec));
    const hh = Math.floor(s / 3600);
    const mm = Math.floor((s % 3600) / 60);
    const ss = s % 60;
    const pad = (n) => String(n).padStart(2, '0');
    return hh > 0 ? `${pad(hh)}:${pad(mm)}:${pad(ss)}` : `${pad(mm)}:${pad(ss)}`;
  }

  function stopTimer() {
    if (timerHandle && typeof clearInterval === 'function') {
      clearInterval(timerHandle);
    }
    timerHandle = null;
  }

  function startTimer() {
    stopTimer();
    if (typeof setInterval !== 'function') return;
    timerHandle = setInterval(() => {
      if (!session || session.mode !== 'exam' || session.paused) return;
      session.remainingSec = Math.max(0, session.remainingSec - 1);
      session.elapsedSec += 1;
      const clk = document.getElementById('kmc-mock-clock');
      if (clk) {
        clk.textContent = formatClock(session.remainingSec);
        clk.classList.toggle('eg-clock-warn', session.remainingSec <= 900 && session.remainingSec > 300);
        clk.classList.toggle('eg-clock-crit', session.remainingSec <= 300);
      }
      if (session.remainingSec <= 0) {
        finalizeSubmission();
      }
    }, 1000);
  }

  function computeReport(paper, questions, answers, elapsedSec) {
    const ptsCorrect = paper.points_correct ?? 4;
    const ptsWrong = paper.points_wrong ?? -1;
    const ptsBlank = paper.points_blank ?? 0;

    let correct = 0;
    let wrong = 0;
    let blank = 0;
    const byDiff = {
      Easy: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
      Medium: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
      Hard: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
    };
    const byTopic = {};
    const weakLessons = new Map();

    const bpMap = (mocksDoc && mocksDoc.blueprint_to_lesson) || {};
    const qLesMap = paper.question_lessons || {};

    questions.forEach((q, idx) => {
      const choice = answers[idx];
      const d = byDiff[q.difficulty] || byDiff.Medium;
      d.total += 1;
      if (!byTopic[q.topic]) byTopic[q.topic] = { total: 0, correct: 0, wrong: 0, blank: 0 };
      byTopic[q.topic].total += 1;

      const lid = qLesMap[q.id] || bpMap[q.kmc_blueprint] || null;

      if (choice === undefined || choice === null) {
        blank += 1;
        d.blank += 1;
        d.points += ptsBlank;
        byTopic[q.topic].blank += 1;
        if (lid) weakLessons.set(lid, (weakLessons.get(lid) || 0) + 1);
      } else if (choice === q.correct_index) {
        correct += 1;
        d.correct += 1;
        d.points += ptsCorrect;
        byTopic[q.topic].correct += 1;
      } else {
        wrong += 1;
        d.wrong += 1;
        d.points += ptsWrong;
        byTopic[q.topic].wrong += 1;
        if (lid) weakLessons.set(lid, (weakLessons.get(lid) || 0) + 1);
      }
    });

    const rawScore = correct * ptsCorrect + wrong * ptsWrong + blank * ptsBlank;
    const score = Math.max(0, rawScore);
    const maxPoints = questions.length * ptsCorrect;
    const pct = maxPoints > 0 ? Math.round((score / maxPoints) * 100) : 0;

    return {
      score,
      rawScore,
      maxPoints,
      pct,
      correct,
      wrong,
      blank,
      total: questions.length,
      elapsedSec,
      byDiff,
      byTopic,
      weakLessonIds: [...weakLessons.entries()].sort((a, b) => b[1] - a[1]).map(([lid]) => lid),
    };
  }

  function finalizeSubmission() {
    if (!session) return;
    stopTimer();
    session.mode = 'review';
    session.confirmSubmit = false;
    session.confirmExit = false;
    session.report = computeReport(session.paper, session.questions, session.answers, session.elapsedSec);
    saveBestScore(
      session.paper.id,
      session.report.score,
      session.report.maxPoints,
      session.report.correct,
      session.report.total
    );
    render();
    const el = document.getElementById('kaust-mock-exams');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }

  /* ---- Dynamic Balanced Official Mock Generator ---- */
  window.generateCustomKaustMock = function (level) {
    const targetLevel = level || activeTrack;
    const tr = TRACKS.find((t) => t.level === targetLevel) || TRACKS[0];
    const bank = getBankQuestions().filter((q) => q.track === 'kaust' && q.level === tr.level);
    if (!bank.length) return;

    const perTier = tr.qCount / 3; // 8 for 24, 10 for 30
    const usedBps = new Set();
    const chosen = [];
    const bpMap = (mocksDoc && mocksDoc.blueprint_to_lesson) || {};

    ['Hard', 'Easy', 'Medium'].forEach((diff) => {
      const pool = bank.filter((q) => q.difficulty === diff);
      const shuffled = [...pool].sort(() => Math.random() - 0.5);
      const lessonCounts = {};
      // First pass: distinct blueprints + lesson balance
      shuffled.sort((a, b) => (lessonCounts[bpMap[a.kmc_blueprint]] || 0) - (lessonCounts[bpMap[b.kmc_blueprint]] || 0));
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= perTier) break;
        if (usedBps.has(q.kmc_blueprint)) continue;
        const lid = bpMap[q.kmc_blueprint] || 'misc';
        const cap = tr.qCount === 30 ? 2 : 2;
        if ((lessonCounts[lid] || 0) >= cap) continue;
        usedBps.add(q.kmc_blueprint);
        lessonCounts[lid] = (lessonCounts[lid] || 0) + 1;
        chosen.push(q);
      }
      // Top-up if needed while keeping distinct IDs
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= perTier) break;
        if (chosen.some((x) => x.id === q.id)) continue;
        if (!usedBps.has(q.kmc_blueprint)) {
          usedBps.add(q.kmc_blueprint);
          chosen.push(q);
        }
      }
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= perTier) break;
        if (!chosen.some((x) => x.id === q.id)) chosen.push(q);
      }
    });

    const ordered = [
      ...chosen.filter((q) => q.difficulty === 'Easy'),
      ...chosen.filter((q) => q.difficulty === 'Medium'),
      ...chosen.filter((q) => q.difficulty === 'Hard'),
    ];

    const customIdx = customMocks.filter((p) => p.level === tr.level).length + 1;
    const svgCnt = ordered.filter((q) => q.content && q.content.en && q.content.en.diagram).length;
    const topicCounts = {};
    const qLessons = {};
    ordered.forEach((q) => {
      topicCounts[q.topic] = (topicCounts[q.topic] || 0) + 1;
      if (bpMap[q.kmc_blueprint]) qLessons[q.id] = bpMap[q.kmc_blueprint];
    });

    const paper = {
      id: `KMC-MOCK-${tr.code}-CUSTOM-${customIdx}`,
      paper_num: 5 + customIdx,
      is_custom: true,
      level: tr.level,
      track_code: tr.code,
      grades_en: tr.shortEn,
      grades_ar: tr.shortAr,
      question_count: ordered.length,
      duration_minutes: 120,
      points_correct: 4,
      points_wrong: -1,
      points_blank: 0,
      max_points: ordered.length * 4,
      svg_count: svgCnt,
      topic_counts: topicCounts,
      sections: [
        {
          id: 'A',
          difficulty: 'Easy',
          start_q: 1,
          end_q: perTier,
          en: `Part A — Core Reasoning & Speed (Questions 1–${perTier})`,
          ar: `الجزء الأول (A) — التفكير الأساسي والسرعة (الأسئلة 1–${perTier})`,
        },
        {
          id: 'B',
          difficulty: 'Medium',
          start_q: perTier + 1,
          end_q: perTier * 2,
          en: `Part B — Multi-Step Contest Problems (Questions ${perTier + 1}–${perTier * 2})`,
          ar: `الجزء الثاني (B) — المسائل التنافسية متعددة الخطوات (الأسئلة ${perTier + 1}–${perTier * 2})`,
        },
        {
          id: 'C',
          difficulty: 'Hard',
          start_q: perTier * 2 + 1,
          end_q: ordered.length,
          en: `Part C — Olympiad Elimination Challenge (Questions ${perTier * 2 + 1}–${ordered.length})`,
          ar: `الجزء الثالث (C) — تحدي التصفيات الأولمبية (الأسئلة ${perTier * 2 + 1}–${ordered.length})`,
        },
      ],
      en: {
        title: `Custom Official KMC Mock #${customIdx} — Fresh Balanced Simulation`,
        focus: `Dynamically sampled ${ordered.length}-question official paper across ${usedBps.size} distinct KMC blueprints.`,
      },
      ar: {
        title: `اختبار كاوست تجريبي مخصص #${customIdx} — محاكاة متوازنة جديدة`,
        focus: `ورقة اختبار رسمية مولّدة من ${ordered.length} سؤالاً عبر ${usedBps.size} نمطاً مختلفاً من أنماط المسابقة.`,
      },
      question_ids: ordered.map((q) => q.id),
      question_lessons: qLessons,
    };

    customMocks.unshift(paper);
    activeTrack = tr.level;
    render();
    return paper.id;
  };

  /* ---- Simulator Controls ---- */
  window.setKaustMockTrack = function (level) {
    activeTrack = level;
    render();
  };

  window.jumpToKaustMocks = function (level) {
    if (level) activeTrack = level;
    render();
    const el = document.getElementById('kaust-mock-exams');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  window.startKaustMock = function (paperId) {
    const paper = findPaper(paperId);
    if (!paper) return;
    const qs = resolvePaperQuestions(paper);
    if (!qs.length) return;
    activeTrack = paper.level;
    session = {
      mode: 'exam',
      paper,
      questions: qs,
      answers: {},
      flags: {},
      currentIdx: 0,
      viewMode: 'single',
      remainingSec: (paper.duration_minutes || 120) * 60,
      elapsedSec: 0,
      paused: false,
      confirmSubmit: false,
      confirmExit: false,
      reviewFilter: 'all',
      report: null,
    };
    startTimer();
    render();
    const el = document.getElementById('kaust-mock-exams');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  window.selectKaustMockOption = function (qIdx, optIdx) {
    if (!session || session.mode !== 'exam') return;
    if (session.answers[qIdx] === optIdx) {
      delete session.answers[qIdx];
    } else {
      session.answers[qIdx] = optIdx;
    }
    session.confirmSubmit = false;
    render();
  };

  window.clearKaustMockOption = function (qIdx) {
    if (!session || session.mode !== 'exam') return;
    delete session.answers[qIdx];
    render();
  };

  window.toggleKaustMockFlag = function (qIdx) {
    if (!session || session.mode !== 'exam') return;
    session.flags[qIdx] = !session.flags[qIdx];
    render();
  };

  window.goKaustMockQuestion = function (qIdx) {
    if (!session || session.mode !== 'exam') return;
    const bounded = Math.max(0, Math.min(session.questions.length - 1, qIdx));
    session.currentIdx = bounded;
    render();
  };

  window.setKaustMockViewMode = function (mode) {
    if (!session || session.mode !== 'exam') return;
    session.viewMode = mode === 'all' ? 'all' : 'single';
    render();
  };

  window.toggleKaustMockPause = function () {
    if (!session || session.mode !== 'exam') return;
    session.paused = !session.paused;
    render();
  };

  window.requestSubmitKaustMock = function () {
    if (!session || session.mode !== 'exam') return;
    const answeredCount = Object.keys(session.answers).length;
    if (answeredCount === session.questions.length) {
      finalizeSubmission();
      return;
    }
    session.confirmSubmit = true;
    session.confirmExit = false;
    render();
  };

  window.confirmSubmitKaustMock = function () {
    finalizeSubmission();
  };

  window.cancelSubmitKaustMock = function () {
    if (!session) return;
    session.confirmSubmit = false;
    render();
  };

  window.exitKaustMock = function (force) {
    if (!session) return;
    if (session.mode === 'exam' && Object.keys(session.answers).length > 0 && !force) {
      session.confirmExit = true;
      session.confirmSubmit = false;
      render();
      return;
    }
    stopTimer();
    session = null;
    render();
  };

  window.cancelExitKaustMock = function () {
    if (!session) return;
    session.confirmExit = false;
    render();
  };

  window.setKaustMockReviewFilter = function (f) {
    if (!session || session.mode !== 'review') return;
    session.reviewFilter = f;
    render();
  };

  /* ---- Edugates Branded A4 OMR Bubble Sheet + Exam Booklet + Worked Key Builder ---- */
  function buildOmrBubbleGridHtml(totalQ, shadedMap, studentAnswers, rtl) {
    const half = Math.ceil(totalQ / 2);
    const renderCol = (startIdx, endIdx) => {
      const rows = [];
      for (let i = startIdx; i < endIdx; i++) {
        const correctOpt = shadedMap ? shadedMap[i] : null;
        const studentOpt = studentAnswers ? studentAnswers[i] : null;
        const bubbles = LABELS.map((lbl, oIdx) => {
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
      return `<div class="eg-omr-col">${rows.join('')}</div>`;
    };

    const legend = shadedMap
      ? `<div class="eg-omr-legend">${
          rtl
            ? '● الدائرة المظللة تمثل الإجابة الصحيحة المعتمدة في مفتاح التصحيح.'
            : '● Filled dark bubble indicates the official correct answer choice.'
        }</div>`
      : `<div class="eg-omr-legend">${
          rtl
            ? 'ظلّل دائرة واحدة فقط (A–E) لكل سؤال بقلم رصاص داكن أو حبر جاف: ● (صحيح)   ✗ ○ (خطأ)'
            : 'Shade ONE bubble (A–E) completely per question using dark pen/pencil: ● (valid)   ✗ ○ (invalid)'
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
        <span class="eg-omr-tag" dir="ltr">+4 / −1 / 0</span>
      </div>
      ${legend}
      <div class="eg-omr-cols" dir="ltr">
        ${renderCol(0, half)}
        ${renderCol(half, totalQ)}
      </div>
    </div>`;
  }

  function buildCoverPageRowHtml(paper, totalQ, rtl) {
    const pText = rtl ? paper.ar : paper.en;
    const grades = rtl ? paper.grades_ar : paper.grades_en;
    const maxPts = totalQ * 4;
    const coverBanner = `<div class="eg-mock-cover no-break">
      <div class="eg-mock-cover-top">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <span class="eg-badge">${rtl ? 'مسابقة كاوست للرياضيات (KMC)' : 'KAUST Mathematics Competition (KMC)'}</span>
          <span class="eg-badge eg-badge-alt">${grades}</span>
          <span class="eg-badge eg-badge-soft">${rtl ? 'الزمن: 120 دقيقة · بدون آلة حاسبة' : 'Time: 120 Minutes · No Calculator'}</span>
        </div>
        <h2 class="eg-mock-cover-title">${pText.title}</h2>
        <div class="eg-mock-cover-specs">
          <span><strong>${rtl ? 'عدد الأسئلة:' : 'Questions:'}</strong> ${totalQ} MCQ (A–E)</span>
          <span><strong>${rtl ? 'الدرجة العظمى:' : 'Maximum Score:'}</strong> ${maxPts} ${rtl ? 'نقطة' : 'pts'}</span>
          <span><strong>${rtl ? 'نظام التصحيح:' : 'Scoring:'}</strong> <span dir="ltr">+4</span> ${rtl ? 'صحيح' : 'Correct'} · <span dir="ltr">−1</span> ${rtl ? 'خطأ' : 'Wrong'} · <span dir="ltr">0</span> ${rtl ? 'متروك' : 'Blank'}</span>
        </div>
      </div>

      <div class="eg-mock-cand-grid">
        <div><strong>${rtl ? 'اسم الطالب/ـة الرباعي:' : 'Candidate Full Name:'}</strong> _______________________________</div>
        <div><strong>${rtl ? 'الصف والشعبة:' : 'Grade / Section:'}</strong> ___________________</div>
        <div><strong>${rtl ? 'رقم الجلوس / الهوية:' : 'Seat / Student ID:'}</strong> ___________________</div>
        <div><strong>${rtl ? 'التاريخ:' : 'Exam Date:'}</strong> ____ / ____ / 202__</div>
        <div><strong>${rtl ? 'صحيح / خطأ / متروك:' : 'C / W / Blank:'}</strong> ___ / ___ / ___</div>
        <div><strong>${rtl ? 'الدرجة النهائية:' : 'Final Score:'}</strong> ______ / ${maxPts}</div>
      </div>

      <div class="eg-mock-rules">
        <div class="eg-mock-rules-h">📋 ${rtl ? 'تعليمات الاختبار الرسمية:' : 'Official Examination Instructions:'}</div>
        <ul>
          <li>${
            rtl
              ? `يتكوّن هذا الاختبار من <strong>${totalQ} سؤالاً</strong> متدرج الصعوبة في ثلاثة أجزاء (Part A, B, C) وزمن الإجابة <strong>ساعتان (120 دقيقة)</strong>.`
              : `This examination consists of <strong>${totalQ} multiple-choice questions</strong> across three graduated tiers (Parts A, B, C) to be completed in <strong>120 minutes</strong>.`
          }</li>
          <li>${
            rtl
              ? 'يُمنع منعاً باتاً استخدام الآلات الحاسبة أو الهواتف الذكية أو الساعات الرقمية أو أي مراجع خارجية.'
              : 'Calculators, smart devices, rulers with formulas, and external notes are strictly prohibited.'
          }</li>
          <li>${
            rtl
              ? 'طريقة احتساب الدرجات: <strong>+4 نقاط</strong> لكل إجابة صحيحة، و<strong>خصم نقطة واحدة (−1)</strong> لكل إجابة خاطئة، و<strong>0 نقطة</strong> للسؤال المتروك بدون تظليل.'
              : 'Contest scoring: <strong>+4 points</strong> for each correct choice, <strong>−1 point</strong> for each incorrect choice, and <strong>0 points</strong> for each blank question.'
          }</li>
        </ul>
      </div>

      ${buildOmrBubbleGridHtml(totalQ, null, null, rtl)}
    </div>`;
    return coverBanner;
  }

  function buildMockExamPrintHtml(paper, questions, mode, rtl, gradedSession) {
    // mode: 'full' (cover+OMR + questions + master key + solutions) | 'student' (cover+OMR + questions) | 'key' (master key + solutions)
    const pText = rtl ? paper.ar : paper.en;
    const grades = rtl ? paper.grades_ar : paper.grades_en;
    const badge = `${grades} · KMC · A4`;
    const totalQ = questions.length;
    const printSection = window.edugatesPrintSection;
    if (typeof printSection !== 'function') return '';

    const parts = [];

    if (mode === 'full' || mode === 'student') {
      // Page 1: Dedicated Official Cover + Candidate Info + Instructions + Blank OMR Bubble Sheet
      parts.push(
        printSection(
          [buildCoverPageRowHtml(paper, totalQ, rtl)],
          pText.title,
          badge,
          rtl,
          false
        )
      );

      // Page 2+: Exam Booklet Questions with Part A / B / C section headers glued cleanly to their 1st question
      const sectionStarts = new Map();
      (paper.sections || []).forEach((s) => {
        sectionStarts.set((s.start_q || 1) - 1, s);
      });

      const qRows = questions.map((q, idx) => {
        const sec = sectionStarts.get(idx);
        const secBanner = sec
          ? `<div class="eg-sec-heading">${rtl ? sec.ar : sec.en}</div>`
          : '';
        const qContent = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
        const diag = qContent.diagram || q.diagram || '';
        const diffCls = q.difficulty === 'Easy' ? 'eg-diff-easy' : q.difficulty === 'Hard' ? 'eg-diff-hard' : 'eg-diff-med';
        const diffLbl = rtl ? DIFF_AR[q.difficulty] || q.difficulty : DIFF_EN[q.difficulty] || q.difficulty;
        const optsHtml = `<div class="eg-ws-opts">${(qContent.options || [])
          .map(
            (opt, oIdx) => `<div class="eg-ws-opt"><span class="eg-opt-l">${LABELS[oIdx]}</span><span class="math-font">${opt}</span></div>`
          )
          .join('')}</div>`;
        const card = `<div class="eg-ws-q no-break">
          <div class="eg-ws-qh">
            <span>${rtl ? 'سؤال' : 'Question'} ${idx + 1}</span>
            <span class="flex items-center gap-1.5">
              <span class="eg-ws-qmeta">${topicLabel(q.topic)}</span>
              <span class="eg-ex-tag ${diffCls}">${diffLbl}</span>
            </span>
          </div>
          <div class="eg-q math-font">${qContent.question || ''}</div>
          ${diag ? `<div class="eg-diagram">${diag}</div>` : ''}
          ${optsHtml}
        </div>`;
        return secBanner ? `<div class="no-break">${secBanner}${card}</div>` : card;
      });

      parts.push(
        printSection(
          qRows,
          `${pText.title} — ${rtl ? 'كراسة الأسئلة' : 'Question Booklet'}`,
          badge,
          rtl,
          true
        )
      );
    }

    if (mode === 'full' || mode === 'key') {
      const shadedMap = {};
      questions.forEach((q, idx) => {
        shadedMap[idx] = q.correct_index;
      });
      const stuAns = gradedSession && gradedSession.paper.id === paper.id ? gradedSession.answers : null;
      const rep = gradedSession && gradedSession.paper.id === paper.id ? gradedSession.report : null;

      const reportBanner = rep
        ? `<div class="eg-banner no-break">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <strong>📊 ${rtl ? 'تقرير أداء الطالب في الاختبار التجريبي' : 'Student Graded Mock Exam Report'}</strong>
              <span class="eg-badge">${rtl ? 'الدرجة الرسمية:' : 'Official KMC Score:'} ${rep.score} / ${rep.maxPoints} (${rep.pct}%)</span>
            </div>
            <div class="eg-summary" style="margin-top:1.5mm">
              ${rtl ? 'إجابات صحيحة:' : 'Correct:'} <strong>${rep.correct}</strong> (+${rep.correct * 4}) ·
              ${rtl ? 'إجابات خاطئة:' : 'Wrong:'} <strong>${rep.wrong}</strong> (−${rep.wrong}) ·
              ${rtl ? 'أسئلة متروكة:' : 'Blank:'} <strong>${rep.blank}</strong> (0) ·
              ${rtl ? 'الزمن المستغرق:' : 'Time Used:'} <strong dir="ltr">${formatClock(rep.elapsedSec)}</strong>
            </div>
          </div>`
        : '';

      const quickKey = `<div class="eg-key-box no-break">
        <div class="eg-h3">🔑 ${rtl ? 'جدول الإجابات السريع' : 'Quick Answer Key Reference'} (1–${totalQ})</div>
        <div class="eg-key-grid">
          ${questions
            .map(
              (q, idx) =>
                `<div class="eg-key-cell" dir="ltr"><strong>${idx + 1}.</strong> <span>(${LABELS[q.correct_index]})</span></div>`
            )
            .join('')}
        </div>
      </div>`;

      const solCards = questions.map((q, idx) => {
        const c = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
        const stuChoice = stuAns ? stuAns[idx] : undefined;
        let stuNote = '';
        if (stuAns) {
          if (stuChoice === undefined || stuChoice === null) {
            stuNote = ` · ${rtl ? 'إجابتك: متروك (0)' : 'Your choice: Blank (0)'}`;
          } else if (stuChoice === q.correct_index) {
            stuNote = ` · ✓ ${rtl ? 'إجابتك صحيحة (+4)' : 'Your choice: Correct (+4)'}`;
          } else {
            stuNote = ` · ✗ ${rtl ? `إجابتك: (${LABELS[stuChoice]}) (−1)` : `Your choice: (${LABELS[stuChoice]}) (−1)`}`;
          }
        }
        return `<div class="eg-card eg-sol-card no-break">
          <div class="eg-sol-h">${rtl ? 'سؤال' : 'Question'} ${idx + 1} — ${rtl ? 'الإجابة الصحيحة:' : 'Correct Answer:'} (${LABELS[q.correct_index]})${stuNote} <span class="eg-ws-qmeta">(${q.id})</span></div>
          <div class="math-font eg-prose">${c.explanation || ''}</div>
        </div>`;
      });

      const keyRows = [
        ...(reportBanner ? [reportBanner] : []),
        buildOmrBubbleGridHtml(totalQ, shadedMap, stuAns, rtl),
        quickKey,
        ...solCards,
      ];

      parts.push(
        printSection(
          keyRows,
          `${rtl ? 'مفتاح التصحيح والحلول التفصيلية' : 'Official Answer Key & Worked Solutions'} — ${rtl ? `نموذج ${paper.paper_num}` : `Mock #${paper.paper_num}`}`,
          badge,
          rtl,
          mode === 'full'
        )
      );
    }

    return parts.join('');
  }

  function triggerPrintContainer(c) {
    if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
      const imgs = [...c.querySelectorAll('img')].map((im) =>
        im.complete ? Promise.resolve() : new Promise((r) => { im.onload = im.onerror = r; })
      );
      Promise.all([MathJax.typesetPromise([c]), ...imgs]).then(() => {
        setTimeout(() => { window.print(); }, 350);
      });
    } else {
      window.print();
    }
  }

  window.printKaustMockPaper = function (paperId, mode) {
    const paper = findPaper(paperId);
    if (!paper) return;
    const qs = resolvePaperQuestions(paper);
    if (!qs.length) return;
    const c = document.getElementById('print-container');
    if (!c) return;
    const printMode = mode || 'full';
    const graded = session && session.mode === 'review' && session.paper.id === paper.id ? session : null;
    c.innerHTML = buildMockExamPrintHtml(paper, qs, printMode, isAr(), graded);
    triggerPrintContainer(c);
  };

  window.printBlankKaustOmr = function (level) {
    const targetLevel = level || activeTrack;
    const tr = TRACKS.find((t) => t.level === targetLevel) || TRACKS[0];
    const templatePaper = {
      paper_num: 1,
      grades_en: tr.shortEn,
      grades_ar: tr.shortAr,
      en: { title: `Official KMC Optical Answer Sheet (${tr.qCount} Questions)` },
      ar: { title: `ورقة رصد وتظليل الإجابات الرسمية لمسابقة كاوست (${tr.qCount} سؤالاً)` },
    };
    const c = document.getElementById('print-container');
    if (!c || typeof window.edugatesPrintSection !== 'function') return;
    c.innerHTML = window.edugatesPrintSection(
      [buildCoverPageRowHtml(templatePaper, tr.qCount, isAr())],
      isAr() ? templatePaper.ar.title : templatePaper.en.title,
      `${isAr() ? tr.shortAr : tr.shortEn} · OMR · A4`,
      isAr(),
      false
    );
    triggerPrintContainer(c);
  };

  /* ---- Screen Rendering ---- */
  function renderExamQuestionCard(q, idx, total) {
    const qContent = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
    const diag = qContent.diagram || q.diagram || '';
    const selected = session.answers[idx];
    const flagged = !!session.flags[idx];
    const diffCls = q.difficulty === 'Easy' ? 'eg-diff-easy' : q.difficulty === 'Hard' ? 'eg-diff-hard' : 'eg-diff-med';
    const diffLbl = isAr() ? DIFF_AR[q.difficulty] || q.difficulty : DIFF_EN[q.difficulty] || q.difficulty;

    const opts = (qContent.options || [])
      .map((opt, oIdx) => {
        const isSel = selected === oIdx;
        return `<button type="button" onclick="selectKaustMockOption(${idx}, ${oIdx})" class="eg-opt eg-opt-btn${isSel ? ' eg-mock-opt-sel' : ''}">
          <span class="eg-opt-l">${LABELS[oIdx]}</span>
          <span class="math-font eg-opt-txt">${opt}</span>
          ${isSel ? '<span class="eg-opt-check">●</span>' : ''}
        </button>`;
      })
      .join('');

    return `<article class="eg-card eg-mock-qcard" id="kmc-mock-q-${idx}">
      <div class="eg-ex-head">
        <div class="flex flex-wrap items-center gap-2">
          <span class="eg-ex-h">${L('السؤال', 'Question')} ${idx + 1} / ${total}</span>
          <span class="eg-ex-tag ${diffCls}">${diffLbl}</span>
          <span class="eg-badge eg-badge-alt">${topicLabel(q.topic)}</span>
        </div>
        <div class="flex flex-wrap items-center gap-1.5">
          ${
            selected !== undefined
              ? `<button type="button" onclick="clearKaustMockOption(${idx})" class="eg-btn eg-btn-sm">↺ ${L('مسح التظليل (0 نقطة)', 'Clear Choice (0 pt)')}</button>`
              : `<span class="eg-lc-pill">${L('متروك (0 نقطة)', 'Blank (0 pts)')}</span>`
          }
          <button type="button" onclick="toggleKaustMockFlag(${idx})" class="eg-btn eg-btn-sm${flagged ? ' eg-flag-on' : ''}">
            🚩 ${flagged ? L('معلّم للمراجعة', 'Flagged') : L('تعليم للمراجعة', 'Flag')}
          </button>
        </div>
      </div>
      <div class="eg-q math-font">${qContent.question || ''}</div>
      ${diag ? `<div class="eg-diagram">${diag}</div>` : ''}
      <div class="eg-opts">${opts}</div>
    </article>`;
  }

  function renderExamView() {
    const p = session.paper;
    const pText = pick(p);
    const total = session.questions.length;
    const answeredCount = Object.keys(session.answers).length;
    const blankCount = total - answeredCount;
    const flagCount = Object.values(session.flags).filter(Boolean).length;
    const clockWarn = session.remainingSec <= 900 && session.remainingSec > 300 ? ' eg-clock-warn' : '';
    const clockCrit = session.remainingSec <= 300 ? ' eg-clock-crit' : '';

    const paletteBtns = session.questions
      .map((q, idx) => {
        const isCur = session.viewMode === 'single' && session.currentIdx === idx;
        const isAns = session.answers[idx] !== undefined;
        const isFlg = !!session.flags[idx];
        let cls = 'eg-pal-btn';
        if (isCur) cls += ' eg-pal-cur';
        if (isAns) cls += ' eg-pal-ans';
        if (isFlg) cls += ' eg-pal-flag';
        const ansLetter = isAns ? LABELS[session.answers[idx]] : '';
        return `<button type="button" onclick="goKaustMockQuestion(${idx})" class="${cls}" title="${L('سؤال', 'Q')} ${idx + 1}">
          <span>${idx + 1}</span>
          ${ansLetter ? `<small>${ansLetter}</small>` : ''}
        </button>`;
      })
      .join('');

    const confirmBanner = session.confirmSubmit
      ? `<div class="eg-mock-alert">
          <div>
            <strong>⚠️ ${L('تأكيد تسليم ورقة الاختبار:', 'Confirm Exam Submission:')}</strong>
            ${L(
              `أجبت عن ${answeredCount} سؤالاً وتركت ${blankCount} بدون إجابة (الأسئلة المتروكة تحصل على 0 نقطة دون خصم). هل تريد إنهاء الاختبار وإصدار التقرير الآن؟`,
              `You answered ${answeredCount} of ${total} questions and left ${blankCount} blank (blanks score 0 pts with no penalty). Submit and grade now?`
            )}
          </div>
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="confirmSubmitKaustMock()" class="eg-btn eg-btn-go">✅ ${L('نعم، سلّم وصحّح الآن', 'Yes, Submit & Grade')}</button>
            <button type="button" onclick="cancelSubmitKaustMock()" class="eg-btn">${L('متابعة الحل', 'Keep Solving')}</button>
          </div>
        </div>`
      : session.confirmExit
      ? `<div class="eg-mock-alert">
          <div>
            <strong>${L('الخروج من الاختبار الجاري؟', 'Exit Active Mock Exam?')}</strong>
            ${L('سيتم إلغاء المحاولة الحالية غير المسلّمة.', 'Your current unsubmitted attempt will be discarded.')}
          </div>
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="exitKaustMock(true)" class="eg-btn eg-btn-danger">${L('نعم، اخرج للقائمة', 'Discard & Exit')}</button>
            <button type="button" onclick="cancelExitKaustMock()" class="eg-btn">${L('البقاء في الاختبار', 'Stay in Exam')}</button>
          </div>
        </div>`
      : '';

    let bodyCards = '';
    if (session.paused) {
      bodyCards = `<div class="eg-card text-center" style="padding:2.5rem 1.5rem">
        <div class="text-3xl mb-2">⏸️</div>
        <h3 class="eg-h3">${L('الاختبار متوقف مؤقتاً', 'Exam Timer Paused')}</h3>
        <p class="eg-prose opacity-80 mb-4">${L('تم إخفاء الأسئلة لحفظ نزاهة التوقيت. اضغط استئناف للمتابعة.', 'Questions are hidden while the clock is paused. Click Resume to continue.')}</p>
        <button type="button" onclick="toggleKaustMockPause()" class="eg-btn eg-btn-main">▶️ ${L('استئناف الاختبار', 'Resume Exam')}</button>
      </div>`;
    } else if (session.viewMode === 'all') {
      bodyCards = session.questions.map((q, idx) => renderExamQuestionCard(q, idx, total)).join('');
    } else {
      const idx = session.currentIdx;
      const prevBtn =
        idx > 0
          ? `<button type="button" onclick="goKaustMockQuestion(${idx - 1})" class="eg-btn">${isAr() ? '→' : '←'} ${L('السؤال السابق', 'Previous Question')}</button>`
          : '<span></span>';
      const nextBtn =
        idx < total - 1
          ? `<button type="button" onclick="goKaustMockQuestion(${idx + 1})" class="eg-btn eg-btn-main">${L('السؤال التالي', 'Next Question')} ${isAr() ? '←' : '→'}</button>`
          : `<button type="button" onclick="requestSubmitKaustMock()" class="eg-btn eg-btn-go">✅ ${L('مراجعة وتسليم الورقة', 'Finish & Submit Paper')}</button>`;
      bodyCards = `${renderExamQuestionCard(session.questions[idx], idx, total)}
        <div class="eg-nav-footer no-print">${prevBtn}${nextBtn}</div>`;
    }

    return `
      <div class="eg-mock-topbar no-print">
        <div class="flex flex-wrap items-center gap-2">
          <button type="button" onclick="exitKaustMock(false)" class="eg-btn eg-btn-sm">${isAr() ? '→' : '←'} ${L('قائمة الاختبارات', 'Exit')}</button>
          <span class="font-bold text-sm">${pText.title}</span>
        </div>
        <div class="flex flex-wrap items-center gap-2">
          <div class="eg-clock-box">
            <span>⏱️</span>
            <span id="kmc-mock-clock" dir="ltr" class="eg-clock${clockWarn}${clockCrit}">${formatClock(session.remainingSec)}</span>
            <button type="button" onclick="toggleKaustMockPause()" class="eg-btn eg-btn-sm" title="${L('إيقاف مؤقت / استئناف', 'Pause / Resume')}">${session.paused ? '▶️' : '⏸️'}</button>
          </div>
          <span class="eg-lc-pill">${L('المجاب:', 'Answered:')} ${answeredCount}/${total} · ${L('متروك:', 'Blank:')} ${blankCount}${flagCount ? ` · 🚩 ${flagCount}` : ''}</span>
          <button type="button" onclick="setKaustMockViewMode('${session.viewMode === 'single' ? 'all' : 'single'}')" class="eg-btn eg-btn-sm">
            ${session.viewMode === 'single' ? '📜 ' + L('عرض الورقة كاملة', 'Full Paper View') : '🎯 ' + L('سؤال بسؤال', 'Single Question')}
          </button>
          <button type="button" onclick="requestSubmitKaustMock()" class="eg-btn eg-btn-go">✅ ${L('تسليم وتصحيح الاختبار', 'Submit & Grade')}</button>
        </div>
      </div>
      ${confirmBanner}
      <div class="eg-pal-wrap no-print">
        <div class="eg-pal-label">${L('لوحة التنقل السريع (OMR):', 'Question & Bubble Navigator:')} <span class="opacity-75 font-normal">(${L('+4 صحيح · −1 خطأ · 0 متروك · بدون آلة حاسبة', '+4 Correct · −1 Wrong · 0 Blank · No Calculator')})</span></div>
        <div class="eg-pal-grid" dir="ltr">${paletteBtns}</div>
      </div>
      <div class="eg-reader">${bodyCards}</div>`;
  }

  function renderReviewView() {
    const p = session.paper;
    const pText = pick(p);
    const rep = session.report;
    const total = session.questions.length;

    let tierBadge = '';
    if (rep.pct >= 75) {
      tierBadge = `<span class="eg-badge" style="background:#dcfce7;color:#166534">🏆 ${L('مستوى تأهل للمرحلة النهائية (ممتاز)', 'Final-Round Contender Pace')}</span>`;
    } else if (rep.pct >= 50) {
      tierBadge = `<span class="eg-badge" style="background:#fef3c7;color:#92400e">⭐ ${L('أداء تنافسي قوي — واصل التدريب', 'Strong Competitive Qualifier Pace')}</span>`;
    } else {
      tierBadge = `<span class="eg-badge eg-badge-alt">📈 ${L('فرصة ممتازة لتقوية الأساسيات عبر الدروس المقترحة أدناه', 'Build Core Mastery with the Recommended Lessons Below')}</span>`;
    }

    const tierCards = ['Easy', 'Medium', 'Hard']
      .map((dKey) => {
        const st = rep.byDiff[dKey];
        const lbl = isAr() ? DIFF_AR[dKey] : DIFF_EN[dKey];
        return `<div class="eg-stat-card">
          <div class="text-xs font-extrabold opacity-75">${lbl}</div>
          <div class="text-lg font-extrabold mt-0.5">${st.correct} / ${st.total} ${L('صحيح', 'Correct')}</div>
          <div class="text-xs opacity-80 mt-0.5">${L('خطأ:', 'Wrong:')} ${st.wrong} · ${L('متروك:', 'Blank:')} ${st.blank} · <strong dir="ltr">${st.points >= 0 ? '+' + st.points : st.points} pts</strong></div>
        </div>`;
      })
      .join('');

    const topicPills = Object.entries(rep.byTopic)
      .map(
        ([t, st]) =>
          `<span class="eg-lc-pill"><strong>${topicLabel(t)}:</strong> ${st.correct}/${st.total}</span>`
      )
      .join(' ');

    const studyLessons = (window.__kaustStudy && window.__kaustStudy.lessons) || [];
    const recBtns = rep.weakLessonIds
      .slice(0, 4)
      .map((lid) => {
        const les = studyLessons.find((x) => x.id === lid);
        if (!les) return '';
        const lTitle = isAr() ? les.ar.title : les.en.title;
        return `<button type="button" onclick="if(window.openKaustLesson){openKaustLesson('${les.id}');document.getElementById('study-lessons').scrollIntoView({behavior:'smooth'});}" class="eg-btn eg-btn-sm">📖 ${L('راجع درس', 'Review Lesson')} ${les.unit_num}: ${lTitle}</button>`;
      })
      .filter(Boolean)
      .join('');

    const filters = [
      ['all', `${L('الكل', 'All')} (${total})`],
      ['wrong', `${L('الخاطئة', 'Incorrect')} (${rep.wrong})`],
      ['blank', `${L('المتروكة', 'Blank')} (${rep.blank})`],
      ['correct', `${L('الصحيحة', 'Correct')} (${rep.correct})`],
      ['flagged', `🚩 ${L('المعلّمة', 'Flagged')} (${Object.values(session.flags).filter(Boolean).length})`],
    ]
      .map(
        ([fKey, fLbl]) =>
          `<button type="button" onclick="setKaustMockReviewFilter('${fKey}')" class="eg-btn eg-btn-sm${session.reviewFilter === fKey ? ' eg-tab-on' : ''}">${fLbl}</button>`
      )
      .join('');

    const reviewCards = session.questions
      .map((q, idx) => {
        const choice = session.answers[idx];
        const isBlank = choice === undefined || choice === null;
        const isOk = !isBlank && choice === q.correct_index;
        const isWr = !isBlank && choice !== q.correct_index;
        const isFlg = !!session.flags[idx];

        if (session.reviewFilter === 'wrong' && !isWr) return '';
        if (session.reviewFilter === 'blank' && !isBlank) return '';
        if (session.reviewFilter === 'correct' && !isOk) return '';
        if (session.reviewFilter === 'flagged' && !isFlg) return '';

        const qContent = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
        const diag = qContent.diagram || q.diagram || '';
        const statusTag = isOk
          ? `<span class="eg-ex-tag eg-diff-easy">✓ +4 ${L('نقاط (صحيحة)', 'pts (Correct)')}</span>`
          : isWr
          ? `<span class="eg-ex-tag eg-diff-hard">✗ −1 ${L('نقطة (خاطئة)', 'pt (Incorrect)')}</span>`
          : `<span class="eg-ex-tag eg-diff-med">○ 0 ${L('نقاط (متروك)', 'pts (Blank)')}</span>`;

        const opts = (qContent.options || [])
          .map((opt, oIdx) => {
            let cls = 'eg-opt';
            let badge = '';
            if (oIdx === q.correct_index) {
              cls += ' eg-opt-ok';
              badge = '<span class="eg-opt-check">✓</span>';
            } else if (choice === oIdx) {
              cls += ' eg-opt-wrong';
              badge = '<span class="eg-opt-x">✗</span>';
            }
            return `<div class="${cls}"><span class="eg-opt-l">${LABELS[oIdx]}</span><span class="math-font eg-opt-txt">${opt}</span>${badge}</div>`;
          })
          .join('');

        return `<article class="eg-card eg-example">
          <div class="eg-ex-head">
            <div class="flex flex-wrap items-center gap-2">
              <span class="eg-ex-h">${L('سؤال', 'Question')} ${idx + 1}</span>
              ${statusTag}
              <span class="eg-badge eg-badge-alt">${topicLabel(q.topic)}</span>
            </div>
            <span class="eg-ws-qmeta">${q.id}</span>
          </div>
          <div class="eg-q math-font">${qContent.question || ''}</div>
          ${diag ? `<div class="eg-diagram">${diag}</div>` : ''}
          <div class="eg-opts">${opts}</div>
          <div class="eg-sol">
            <div class="eg-sol-h">✅ ${L('الحل التفصيلي خطوة بخطوة — الإجابة الصحيحة:', 'Step-by-Step Solution — Correct Answer:')} (${LABELS[q.correct_index]})</div>
            <div class="math-font eg-prose">${qContent.explanation || ''}</div>
          </div>
        </article>`;
      })
      .filter(Boolean)
      .join('');

    return `
      <div class="eg-toolbar no-print">
        <div class="flex flex-wrap gap-2">
          <button type="button" onclick="exitKaustMock(true)" class="eg-btn">${isAr() ? '→' : '←'} ${L('جميع الاختبارات التجريبية', 'All Mock Exams')}</button>
          <button type="button" onclick="startKaustMock('${p.id}')" class="eg-btn">🔄 ${L('إعادة المحاولة', 'Retake Paper')}</button>
        </div>
        <div class="flex flex-wrap gap-2">
          <button type="button" onclick="printKaustMockPaper('${p.id}', 'key')" class="eg-btn eg-btn-main">🖨️ ${L('طباعة تقرير الدرجة والحلول (A4)', 'Print Graded Report & Solutions (A4)')}</button>
          <button type="button" onclick="printKaustMockPaper('${p.id}', 'full')" class="eg-btn">📦 ${L('طباعة الحزمة الكاملة (A4)', 'Print Full Exam Package (A4)')}</button>
        </div>
      </div>

      <div class="eg-banner">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
          <span class="font-extrabold text-sm">${pText.title}</span>
          ${tierBadge}
        </div>
        <div class="eg-score-hero">
          <div class="eg-score-main">
            <div class="text-xs uppercase font-extrabold opacity-75">${L('الدرجة الرسمية (نظام كاوست +4/−1/0)', 'Official KMC Contest Score (+4 / −1 / 0)')}</div>
            <div class="text-3xl sm:text-4xl font-extrabold mt-0.5" dir="ltr">${rep.score} <span class="text-lg opacity-70">/ ${rep.maxPoints} pts (${rep.pct}%)</span></div>
          </div>
          <div class="flex flex-wrap gap-2">
            <span class="eg-lc-pill">✓ ${L('صحيح:', 'Correct:')} <strong>${rep.correct}</strong></span>
            <span class="eg-lc-pill">✗ ${L('خطأ:', 'Wrong:')} <strong>${rep.wrong}</strong></span>
            <span class="eg-lc-pill">○ ${L('متروك:', 'Blank:')} <strong>${rep.blank}</strong></span>
            <span class="eg-lc-pill">⏱️ ${L('الزمن:', 'Time:')} <strong dir="ltr">${formatClock(rep.elapsedSec)}</strong></span>
          </div>
        </div>
        <div class="eg-stat-grid mt-3">${tierCards}</div>
        <div class="flex flex-wrap gap-1.5 mt-3">${topicPills}</div>
        ${
          recBtns
            ? `<div class="mt-3 pt-3 border-t border-teal-500/25">
                <div class="text-xs font-extrabold mb-1.5">🎯 ${L('دروس مقترحة للمراجعة السريعة بناءً على إجاباتك:', 'Recommended KAUST Study Lessons to Review Next:')}</div>
                <div class="flex flex-wrap gap-1.5">${recBtns}</div>
              </div>`
            : ''
        }
      </div>

      <div class="flex flex-wrap items-center justify-between gap-2 my-3 no-print">
        <div class="font-extrabold text-sm">📝 ${L('مراجعة الأسئلة والحلول التفصيلية:', 'Detailed Question-by-Question Review:')}</div>
        <div class="flex flex-wrap gap-1.5">${filters}</div>
      </div>
      <div class="eg-reader">${reviewCards || `<div class="eg-card text-center opacity-75">${L('لا توجد أسئلة ضمن هذا الفلتر.', 'No questions match this filter.')}</div>`}</div>`;
  }

  function renderHubView() {
    const tr = TRACKS.find((t) => t.level === activeTrack) || TRACKS[0];
    const trackPapers = allPapers().filter((p) => p.level === activeTrack);

    const tabs = TRACKS.map((t) => {
      const cnt = allPapers().filter((p) => p.level === t.level).length;
      return `<button type="button" onclick="setKaustMockTrack('${t.level}')" class="eg-tab${t.level === activeTrack ? ' eg-tab-on' : ''}">
        <span>${isAr() ? t.ar : t.en}</span>
        <span class="eg-tab-count">${cnt} ${L('نماذج رسمية', 'Mock Papers')} · ${t.qCount} ${L('سؤالاً', 'Qs')} · 120 ${L('دقيقة', 'min')}</span>
      </button>`;
    }).join('');

    const cards = trackPapers
      .map((p) => {
        const pText = pick(p);
        const best = bestScores[p.id];
        const topicTags = Object.entries(p.topic_counts || {})
          .map(([k, v]) => `${topicLabel(k)}: ${v}`)
          .join(' · ');

        return `<div class="eg-lesson-card eg-mock-card">
          <div>
            <div class="flex flex-wrap items-center justify-between gap-1.5 mb-2">
              <div class="flex flex-wrap items-center gap-1.5">
                <span class="eg-badge">${p.is_custom ? '🎲 ' + L('نموذج مخصص', 'Custom') : L('نموذج رسمي', 'Mock Paper') + ' #' + p.paper_num}</span>
                <span class="eg-badge eg-badge-alt">${p.question_count} ${L('سؤالاً', 'Qs')} · 120 ${L('د', 'min')}</span>
              </div>
              <span class="eg-lc-pill">${best ? `🏆 ${best.score}/${best.maxPoints}` : `🖼️ ${p.svg_count} ${L('رسمة', 'SVGs')} · ${p.max_points} ${L('نقطة', 'pts')}`}</span>
            </div>
            <h3 class="eg-lc-title" onclick="startKaustMock('${p.id}')">${pText.title}</h3>
            <p class="eg-lc-desc">${pText.focus}</p>
            <div class="text-xs opacity-75 mt-2">${topicTags}</div>
          </div>
          <div class="eg-mock-actions">
            <button type="button" onclick="startKaustMock('${p.id}')" class="eg-btn eg-btn-go eg-btn-sm w-full">
              ⏱️ ${L('ابدأ الاختبار الموقوت (120 دقيقة)', 'Start Live Timed Exam (120 min)')}
            </button>
            <div class="flex flex-wrap gap-1.5 w-full">
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'full')" class="eg-btn eg-btn-main eg-btn-sm flex-1" title="${L('طباعة الغلاف + ورقة التظليل OMR + الأسئلة + المفتاح والحلول', 'Print Cover + OMR Bubble Sheet + Exam + Worked Key')}">
                🖨️ ${L('حزمة كاملة A4', 'Full Pack A4')}
              </button>
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'student')" class="eg-btn eg-btn-sm" title="${L('طباعة ورقة الطالب والتظليل فقط بدون الإجابات', 'Student Exam + OMR Bubble Sheet Only (No Answers)')}">
                🫧 ${L('ورقة الطالب', 'Exam + OMR')}
              </button>
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'key')" class="eg-btn eg-btn-sm" title="${L('طباعة مفتاح التصحيح المظلل والحلول فقط', 'Pre-Shaded OMR Master Key & Worked Solutions Only')}">
                🔑 ${L('المفتاح', 'Key')}
              </button>
            </div>
          </div>
        </div>`;
      })
      .join('');

    return `
      <div class="eg-tabs no-print">${tabs}</div>
      <div class="eg-subbar no-print">
        <div class="text-xs sm:text-sm opacity-90">
          🎯 ${L(
            `نظام التصفيات الرسمي لمسابقة كاوست (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤالاً</strong> في <strong>120 دقيقة</strong> بدون آلة حاسبة · <strong>+4</strong> للإجابة الصحيحة، <strong>−1</strong> للخاطئة، <strong>0</strong> للمتروك.`,
            `Official KMC Elimination Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (A–E)</strong> in <strong>120 minutes</strong>, No Calculator · <strong>+4</strong> Correct, <strong>−1</strong> Wrong, <strong>0</strong> Blank.`
          )}
        </div>
        <div class="flex flex-wrap gap-2 shrink-0">
          <button type="button" onclick="generateCustomKaustMock('${activeTrack}')" class="eg-btn eg-btn-go">
            🎲 ${L('توليد نموذج تجريبي جديد', 'Generate Fresh Mock')}
          </button>
          <button type="button" onclick="printBlankKaustOmr('${activeTrack}')" class="eg-btn eg-btn-main">
            🫧 ${L('طباعة ورقة تظليل OMR فارغة (A4)', 'Print Blank OMR Sheet (A4)')}
          </button>
        </div>
      </div>
      <div class="eg-grid">${cards}</div>`;
  }

  function render() {
    const root = document.getElementById('kaust-mock-exams');
    if (!root || !mocks.length) return;
    root.setAttribute('dir', isAr() ? 'rtl' : 'ltr');

    const totalPapers = allPapers().length;
    const totalUniqueQs = mocks.reduce((acc, p) => acc + (p.question_count || 0), 0);

    const inner = !session
      ? renderHubView()
      : session.mode === 'exam'
      ? renderExamView()
      : renderReviewView();

    root.innerHTML = `<div class="eg-hub eg-mock-hub">
      <div class="eg-hub-h">
        <div class="eg-hub-logo-box"><img src="LOGO.jpg" alt="Edugates International School" loading="eager" decoding="sync" class="eg-hub-logo"></div>
        <div class="flex-1">
          <div class="eg-hub-kicker">Edugates International School · مدرسة بوابة المعرفة العالمية</div>
          <h2 class="text-2xl sm:text-3xl font-display font-extrabold">⏱️ ${L('محاكي الاختبارات الرسمية الكاملة لمسابقة كاوست (KMC)', 'KAUST Math Competition (KMC) Full Mock Exams')}</h2>
          <p class="text-xs sm:text-sm opacity-80 mt-1">${L(
            `${totalPapers} نموذج اختبار رسمي كامل (${totalUniqueQs} سؤالاً مستقلاً) · مؤقت حي 120 دقيقة · أوراق تظليل بصري OMR ومفاتيح حلول مفصلة جاهزة للطباعة على ورق A4`,
            `${totalPapers} Full Official Simulation Papers (${totalUniqueQs} dedicated KMC questions) · 120-Min Live Exam Simulator · Printable A4 Exam Booklets, OMR Bubble Sheets & Worked Keys`
          )}</p>
        </div>
      </div>
      ${inner}
    </div>`;

    if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
      MathJax.typesetPromise([root]).catch(() => {});
    }
  }

  async function init() {
    loadBestScores();
    let sec = document.getElementById('kaust-mock-exams');
    if (!sec) {
      const practice = document.getElementById('practice');
      if (!practice || !practice.parentNode) return;
      sec = document.createElement('section');
      sec.id = 'kaust-mock-exams';
      sec.className = 'no-print-section';
      practice.parentNode.insertBefore(sec, practice);
    }

    try {
      const res = await fetch('data/kaust_mocks.json');
      if (res.ok) {
        mocksDoc = await res.json();
        mocks = (mocksDoc && mocksDoc.mocks) || [];
      }
    } catch (e) {
      console.error('Failed to load KAUST mock exams:', e);
      return;
    }

    const t0 = Date.now();
    while (!getBankQuestions().length && Date.now() - t0 < 15000) {
      await new Promise((r) => setTimeout(r, 80));
    }

    render();

    if (typeof window.toggleLanguage === 'function' && !window.__kaustMockLangHooked) {
      window.__kaustMockLangHooked = true;
      const origToggle = window.toggleLanguage;
      window.toggleLanguage = function () {
        const res = origToggle.apply(this, arguments);
        const navTxt = document.getElementById('nav-mocks-text');
        if (navTxt) navTxt.innerText = isAr() ? 'اختبارات كاوست' : 'KAUST Mocks';
        render();
        return res;
      };
    }

    if (typeof window.setGradeFilter === 'function' && !window.__kaustMockGradeHooked) {
      window.__kaustMockGradeHooked = true;
      const origGrade = window.setGradeFilter;
      window.setGradeFilter = function (g) {
        const res = origGrade.apply(this, arguments);
        if (!session) {
          if (g === 6 || g === 7) {
            activeTrack = TRACKS[0].level;
            render();
          } else if (g === 8 || g === 9) {
            activeTrack = TRACKS[1].level;
            render();
          } else if (g === 10 || g === 11) {
            activeTrack = TRACKS[2].level;
            render();
          }
        }
        return res;
      };
    }

    window.__kaustMocks = {
      get mocks() {
        return allPapers();
      },
      get session() {
        return session;
      },
      render,
    };
  }

  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
