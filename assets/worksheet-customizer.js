/* Edugates International School — A4 Worksheet & Exam Customizer Studio
 * Upgrades #print-modal with multi-topic & study-lesson pickers, Easy/Medium/Hard mix,
 * diagram density filter, custom title/subtitle, student scratch-work boxes, and Page 1 OMR bubble sheet.
 */
(function () {
  'use strict';

  const TOPIC_AR = {
    'Numbers & Operations': 'الأعداد والعمليات عليها',
    'Number Theory': 'نظرية الأعداد',
    Algebra: 'الجبر والأنماط',
    Inequalities: 'المتباينات والقيم القصوى',
    Geometry: 'الهندسة والقياس',
    'Combinatorics & Logic': 'التركيبات والمنطق',
    'Data & Probability': 'البيانات والاحتمالات',
    Calculus: 'التفاضل والتكامل',
    Combinatorics: 'التركيبات والعد',
    Logic: 'المنطق الرياضي',
    Patterns: 'الأنماط والمتتاليات',
    Fractions: 'الكسور والنسب',
    Measurement: 'القياس',
    'Numbers and Operations': 'الأعداد والعمليات',
  };

  let selectedTopics = new Set();
  let selectedLessonIds = new Set();
  let explicitKeyMode = null; // 'full' | 'quick' | 'none' | null

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const topicLabel = (tp) => (isAr() ? TOPIC_AR[tp] || tp : tp);
  const escHtml = (s) =>
    String(s || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');

  function normDiff(q) {
    const d = String((q && q.difficulty) || '').toLowerCase();
    if (d.startsWith('e')) return 'Easy';
    if (d.startsWith('h')) return 'Hard';
    return 'Medium';
  }

  function hasSvg(q) {
    const enD = q && q.content && q.content.en && q.content.en.diagram;
    return Boolean(enD || (q && q.diagram));
  }

  function shuffleCopy(arr) {
    const out = [...arr];
    for (let i = out.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [out[i], out[j]] = [out[j], out[i]];
    }
    return out;
  }

  function getActiveEffectiveTrack() {
    const trackSel = document.getElementById('print-track-select');
    const tr = trackSel ? trackSel.value : 'current';
    if (tr !== 'current') return tr;
    const quizSel = document.getElementById('quiz-track-select');
    return quizSel && quizSel.value !== 'all' ? quizSel.value : 'current';
  }

  function getBaseTrackPhasePool() {
    const track = document.getElementById('print-track-select').value;
    const phase = document.getElementById('print-phase-select').value;
    if (track === 'current') {
      return typeof currentFilteredQuestions !== 'undefined' ? [...currentFilteredQuestions] : [];
    }
    const allQs = (typeof appData !== 'undefined' && Array.isArray(appData.questions)) ? appData.questions : [];
    return allQs.filter((q) => {
      if (q.track !== track) return false;
      if (phase !== 'all' && q.level !== phase) return false;
      return true;
    });
  }

  function getLessonsForActiveSelection() {
    const effTrack = getActiveEffectiveTrack();
    if (effTrack !== 'nafes' && effTrack !== 'kangaroo' && effTrack !== 'kaust' && effTrack !== 'nsmo' && effTrack !== 'olympiad') return [];
    const study = window.__kaustStudy;
    if (!study) return [];
    const list = effTrack === 'olympiad'
      ? (study.olympiadLessons || [])
      : effTrack === 'nafes'
      ? (study.nafesLessons || [])
      : effTrack === 'kangaroo'
      ? (study.kangarooLessons || [])
      : effTrack === 'nsmo'
      ? (study.nsmoLessons || [])
      : (study.lessons || []);
    const track = document.getElementById('print-track-select').value;
    const phase = document.getElementById('print-phase-select').value;
    if (track !== 'current' && phase !== 'all') {
      return list.filter((l) => l.level === phase);
    }
    if (track === 'current') {
      const phaseSelId = effTrack === 'olympiad'
        ? 'quiz-olympiad-tier-select'
        : effTrack === 'nafes'
        ? 'quiz-nafes-grade-select'
        : effTrack === 'kangaroo'
        ? 'quiz-kangaroo-level-select'
        : effTrack === 'nsmo'
        ? 'quiz-nsmo-phase-select'
        : 'quiz-kaust-phase-select';
      const pEl = document.getElementById(phaseSelId);
      if (pEl && pEl.value && pEl.value !== 'all') {
        return list.filter((l) => l.level === pEl.value);
      }
    }
    return list;
  }

  function getFilteredPool() {
    let pool = getBaseTrackPhasePool();

    if (selectedTopics.size > 0) {
      pool = pool.filter((q) => selectedTopics.has(q.topic));
    }

    if (selectedLessonIds.size > 0) {
      const lessons = getLessonsForActiveSelection().filter((l) => selectedLessonIds.has(l.id));
      const allowedBps = new Set();
      lessons.forEach((l) => (l.blueprints || []).forEach((bp) => allowedBps.add(bp)));
      if (allowedBps.size > 0) {
        pool = pool.filter((q) => allowedBps.has(q.kmc_blueprint) || allowedBps.has(q.nsmo_blueprint) || allowedBps.has(q.kangaroo_blueprint) || allowedBps.has(q.nafes_blueprint) || allowedBps.has(q.olympiad_blueprint));
      }
    }

    const diffModeEl = document.getElementById('print-diff-mode');
    const diffMode = diffModeEl ? diffModeEl.value : 'graduated';
    if (diffMode === 'easy_only') pool = pool.filter((q) => normDiff(q) === 'Easy');
    else if (diffMode === 'medium_only') pool = pool.filter((q) => normDiff(q) === 'Medium');
    else if (diffMode === 'hard_only') pool = pool.filter((q) => normDiff(q) === 'Hard');

    const diagModeEl = document.getElementById('print-diagram-mode');
    const diagMode = diagModeEl ? diagModeEl.value : 'any';
    if (diagMode === 'only_svg') {
      pool = pool.filter(hasSvg);
    }

    return pool;
  }

  function renderFilterChips() {
    const basePool = getBaseTrackPhasePool();
    const topicBox = document.getElementById('print-topic-chips');
    if (topicBox) {
      const counts = new Map();
      basePool.forEach((q) => {
        if (q.topic) counts.set(q.topic, (counts.get(q.topic) || 0) + 1);
      });
      // Prune stale topics
      [...selectedTopics].forEach((tp) => {
        if (!counts.has(tp)) selectedTopics.delete(tp);
      });

      const entries = [...counts.entries()].sort((a, b) => b[1] - a[1]);
      if (entries.length <= 1) {
        topicBox.innerHTML = entries.length === 1
          ? `<span class="eg-cust-chip eg-cust-chip-on">${escHtml(topicLabel(entries[0][0]))} (${entries[0][1]})</span>`
          : `<span class="text-xs text-slate-400">${L('لا توجد مواضيع متاحة', 'No topics available')}</span>`;
      } else {
        const allOn = selectedTopics.size === 0;
        const allBtn = `<button type="button" onclick="clearPrintTopics()" class="eg-cust-chip${allOn ? ' eg-cust-chip-on' : ''}">${L('كل المواضيع', 'All Topics')} (${basePool.length})</button>`;
        const tpBtns = entries
          .map(([tp, cnt]) => {
            const on = selectedTopics.has(tp);
            return `<button type="button" data-topic="${escHtml(tp)}" onclick="togglePrintTopic(this.getAttribute('data-topic'))" class="eg-cust-chip${on ? ' eg-cust-chip-on' : ''}">${escHtml(topicLabel(tp))} (${cnt})</button>`;
          })
          .join('');
        topicBox.innerHTML = allBtn + tpBtns;
      }
    }

    const lessonsWrap = document.getElementById('print-lessons-wrap');
    const lessonBox = document.getElementById('print-lesson-chips');
    const lessons = getLessonsForActiveSelection();
    if (lessonsWrap && lessonBox) {
      const validIds = new Set(lessons.map((l) => l.id));
      [...selectedLessonIds].forEach((id) => {
        if (!validIds.has(id)) selectedLessonIds.delete(id);
      });

      if (!lessons.length) {
        lessonsWrap.style.display = 'none';
        lessonBox.innerHTML = '';
      } else {
        lessonsWrap.style.display = 'block';
        const allOn = selectedLessonIds.size === 0;
        const allBtn = `<button type="button" onclick="clearPrintLessons()" class="eg-cust-chip${allOn ? ' eg-cust-chip-on' : ''}">${L('كل الدروس', 'All Lessons')} (${lessons.length})</button>`;
        const lBtns = lessons
          .map((les) => {
            const on = selectedLessonIds.has(les.id);
            const tObj = isAr() ? les.ar : les.en;
            const shortTitle = tObj && tObj.title ? tObj.title : les.id;
            return `<button type="button" onclick="togglePrintLesson('${les.id}')" class="eg-cust-chip${on ? ' eg-cust-chip-on' : ''}" title="${escHtml(shortTitle)}">${les.unit_num} · ${escHtml(shortTitle)}</button>`;
          })
          .join('');
        lessonBox.innerHTML = allBtn + lBtns;
      }
    }
  }

  function syncModalLocaleText() {
    const map = [
      ['print-modal-title', L('🖨️ مصمّم أوراق العمل والاختبارات (Edugates A4)', '🖨️ Edugates A4 Worksheet & Exam Customizer')],
      ['print-modal-desc', L('خصّص عنوان الورقة، المواضيع أو الدروس، توزيع الصعوبة، مساحة الحل، وورقة التظليل البصري OMR للطباعة الفورية على ورق A4.', 'Customize title, topics/lessons, Easy/Medium/Hard mix, scratch-work boxes, and an optional Page 1 OMR bubble sheet on A4 paper.')],
      ['print-custom-title-lbl', L('عنوان الورقة المخصّص (اختياري)', 'Custom Worksheet Title (Optional)')],
      ['print-custom-subtitle-lbl', L('بيانات الصف / المعلم / الزمن (اختياري)', 'Class / Teacher / Time Note (Optional)')],
      ['print-modal-track-lbl', L('المسار (Track)', 'Source Track')],
      ['print-modal-phase-lbl', L('المرحلة / الصف (Phase / Grade)', 'Track Band / Phase')],
      ['print-topics-lbl', L('تصفية حسب المواضيع (يمكن اختيار أكثر من موضوع)', 'Filter by Topics (Multi-Select)')],
      ['print-lessons-lbl', L('تصفية حسب دروس الأكاديمية (نافس / كانجارو / كاوست / نسمو / الأولمبياد)', 'Filter by Study Academy Lessons (Multi-Select)')],
      ['print-diff-lbl', L('توزيع وتدرّج الصعوبة', 'Difficulty Mix & Ordering')],
      ['print-diagram-lbl', L('الرسوم الهندسية والتوضيحية (SVG)', 'Visual Diagrams (SVG)')],
      ['print-scratch-lbl', L('مساحة مسودة الحل تحت كل سؤال', 'Student Scratch-Work Space')],
      ['print-key-lbl', L('مفتاح التصحيح والحلول في نهاية الورقة', 'Answer Key & Worked Solutions')],
      ['print-include-omr-lbl', L('إرفاق غلاف رسمي + ورقة تظليل بصري OMR في الصفحة الأولى', 'Prepend Page 1 Official Cover + Optical OMR Bubble Sheet')],
      ['print-include-solutions-lbl', L('تضمين خطوات الحل التفصيلية في المفتاح', 'Include full step-by-step worked solutions in key')],
      ['print-edugates-note', L('الوضع الافتراضي A4 · شعار مدرسة بوابة المعرفة العالمية يتكرر تلقائياً في جميع الصفحات', 'Default A4 Paper · Edugates International School header & logo repeat on every page')],
      ['print-study-shortcut-lbl', L('طباعة شرح دروس نافس وكانجارو وكاوست ونسمو والأولمبياد والأمثلة المحلولة (A4)', 'Print Nafes, Kangaroo, KAUST, NSMO & Olympiad Study Guides + Drills (A4)')],
      ['print-mocks-shortcut-lbl', L('طباعة الاختبارات الكاملة وأوراق التظليل OMR (نافس + كانجارو + كاوست + نسمو + الأولمبياد)', 'Print Full Official Mock Exams & OMR Sheets (Nafes, Kangaroo, KAUST, NSMO & Olympiad)')],
      ['print-btn-cancel', L('إلغاء', 'Cancel')],
      ['print-btn-confirm', L('🖨️ توليد وطباعة (A4)', '🖨️ Generate & Print (A4)')],
    ];
    map.forEach(([id, txt]) => {
      const el = document.getElementById(id);
      if (el) el.innerText = txt;
    });

    const titleInput = document.getElementById('print-custom-title');
    if (titleInput) {
      titleInput.placeholder = L('مثال: ورقة عمل الأسبوع الرابع — أولمبياد الرياضيات', 'e.g., Grade 8 Olympiad Weekly Quiz #4');
    }
    const subInput = document.getElementById('print-custom-subtitle');
    if (subInput) {
      subInput.placeholder = L('مثال: الزمن 45 دقيقة · بدون آلة حاسبة · قسم الرياضيات', 'e.g., Time: 45 min · No Calculator · Dept. of Mathematics');
    }

    const selectOptionMaps = {
      'print-diff-mode': {
        graduated: L('متدرج الصعوبة (سهل ← متوسط ← متقدم)', 'Graduated (Easy → Medium → Hard)'),
        random: L('عشوائي متنوع', 'Randomized Mix'),
        custom: L('نسب صعوبة مخصّصة (%)', 'Custom % Mix (Easy / Med / Hard)'),
        easy_only: L('تأسيسي / سهل فقط', 'Easy / Foundation Only'),
        medium_only: L('متوسط الصعوبة فقط', 'Medium / Multi-Step Only'),
        hard_only: L('متقدم / أولمبياد فقط', 'Hard / Olympiad Only'),
      },
      'print-diagram-mode': {
        any: L('توزيع تلقائي', 'Standard Mix'),
        prefer_svg: L('أولوية للأسئلة المصوّرة', 'Prefer Diagrams'),
        only_svg: L('أسئلة برسوم SVG فقط', 'Diagrams Only'),
      },
      'print-scratch-space': {
        none: L('مدمج (بدون مربع مسودة)', 'Compact (No Box)'),
        medium: L('مربع مسودة متوسط', 'Medium Work Box'),
        large: L('شبكة مسودة أولمبية كبيرة', 'Large Olympiad Grid'),
      },
      'print-key-mode': {
        full: L('مفتاح + خطوات الحل التفصيلية', 'Key + Worked Solutions'),
        quick: L('مفتاح إجابات سريع فقط', 'Quick Key Only'),
        none: L('بدون مفتاح (نسخة الطالب)', 'No Key (Student Only)'),
      },
    };
    Object.entries(selectOptionMaps).forEach(([selId, valMap]) => {
      const sel = document.getElementById(selId);
      if (sel && sel.options && sel.options.length) {
        for (let i = 0; i < sel.options.length; i++) {
          const opt = sel.options[i];
          if (opt && valMap[opt.value]) {
            opt.text = valMap[opt.value];
            opt.innerText = valMap[opt.value];
          }
        }
      }
    });
  }

  function refreshPoolStatsAndMax() {
    const pool = getFilteredPool();
    const maxSpan = document.getElementById('print-max-q');
    const input = document.getElementById('print-q-count');
    const btnConfirm = document.getElementById('print-btn-confirm');
    const badge = document.getElementById('print-pool-badge');

    const maxQ = pool.length;
    if (maxSpan) maxSpan.innerText = maxQ;
    if (input) {
      input.max = maxQ;
      const cur = parseInt(input.value, 10) || 0;
      if (maxQ === 0) {
        input.value = 0;
        input.disabled = true;
      } else {
        input.disabled = false;
        if (cur > maxQ || cur <= 0) input.value = Math.min(20, maxQ);
      }
    }
    if (btnConfirm) btnConfirm.disabled = maxQ === 0;

    if (badge) {
      const svgCnt = pool.filter(hasSvg).length;
      const eCnt = pool.filter((q) => normDiff(q) === 'Easy').length;
      const mCnt = pool.filter((q) => normDiff(q) === 'Medium').length;
      const hCnt = pool.filter((q) => normDiff(q) === 'Hard').length;
      badge.innerText = L(
        `المتاح: ${maxQ} سؤالاً (${eCnt} سهل · ${mCnt} متوسط · ${hCnt} متقدم · ${svgCnt} رسمة SVG)`,
        `Matching Pool: ${maxQ} Qs (${eCnt} Easy · ${mCnt} Med · ${hCnt} Hard · ${svgCnt} SVGs)`
      );
    }

    const mixBox = document.getElementById('print-custom-mix-box');
    const diffModeEl = document.getElementById('print-diff-mode');
    if (mixBox && diffModeEl) {
      mixBox.style.display = diffModeEl.value === 'custom' ? 'grid' : 'none';
    }
  }

  function selectQuestionsFromPool(pool, count) {
    const diffModeEl = document.getElementById('print-diff-mode');
    const diffMode = diffModeEl ? diffModeEl.value : 'graduated';
    const diagModeEl = document.getElementById('print-diagram-mode');
    const preferSvg = diagModeEl && diagModeEl.value === 'prefer_svg';

    const orderCandidates = (arr) => {
      const shuf = shuffleCopy(arr);
      if (preferSvg) {
        shuf.sort((a, b) => (hasSvg(b) ? 1 : 0) - (hasSvg(a) ? 1 : 0));
      }
      return shuf;
    };

    if (diffMode === 'random' || diffMode === 'easy_only' || diffMode === 'medium_only' || diffMode === 'hard_only') {
      return orderCandidates(pool).slice(0, count);
    }

    const byTier = {
      Easy: orderCandidates(pool.filter((q) => normDiff(q) === 'Easy')),
      Medium: orderCandidates(pool.filter((q) => normDiff(q) === 'Medium')),
      Hard: orderCandidates(pool.filter((q) => normDiff(q) === 'Hard')),
    };

    let wE = 35;
    let wM = 40;
    let wH = 25;
    if (diffMode === 'custom') {
      wE = Math.max(0, parseInt((document.getElementById('print-pct-easy') || {}).value, 10) || 0);
      wM = Math.max(0, parseInt((document.getElementById('print-pct-med') || {}).value, 10) || 0);
      wH = Math.max(0, parseInt((document.getElementById('print-pct-hard') || {}).value, 10) || 0);
      if (wE + wM + wH <= 0) {
        wE = 35; wM = 40; wH = 25;
      }
    }

    const wSum = wE + wM + wH;
    let qE = Math.round((count * wE) / wSum);
    let qM = Math.round((count * wM) / wSum);
    let qH = Math.max(0, count - qE - qM);
    while (qE + qM + qH > count) {
      if (qM > 0) qM--;
      else if (qE > 0) qE--;
      else qH--;
    }

    const pickedIds = new Set();
    const takeFrom = (arr, k) => {
      const res = [];
      for (const item of arr) {
        if (res.length >= k) break;
        if (!pickedIds.has(item.id)) {
          pickedIds.add(item.id);
          res.push(item);
        }
      }
      return res;
    };

    const chosenE = takeFrom(byTier.Easy, qE);
    const chosenM = takeFrom(byTier.Medium, qM);
    const chosenH = takeFrom(byTier.Hard, qH);
    let combined = [...chosenE, ...chosenM, ...chosenH];

    if (combined.length < count) {
      const topUp = takeFrom(orderCandidates(pool), count - combined.length);
      combined = combined.concat(topUp);
    }

    const rank = { Easy: 0, Medium: 1, Hard: 2 };
    combined.sort((a, b) => rank[normDiff(a)] - rank[normDiff(b)]);
    return combined.slice(0, count);
  }

  /* ---- Global UI Handlers ---- */
  window.togglePrintTopic = function (topic) {
    if (!topic) return;
    if (selectedTopics.has(topic)) selectedTopics.delete(topic);
    else selectedTopics.add(topic);
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.clearPrintTopics = function () {
    selectedTopics.clear();
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.togglePrintLesson = function (lessonId) {
    if (!lessonId) return;
    if (selectedLessonIds.has(lessonId)) selectedLessonIds.delete(lessonId);
    else selectedLessonIds.add(lessonId);
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.clearPrintLessons = function () {
    selectedLessonIds.clear();
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.setPrintQuickCount = function (n) {
    const input = document.getElementById('print-q-count');
    if (!input || input.disabled) return;
    const maxQ = parseInt(document.getElementById('print-max-q').innerText, 10) || 0;
    if (maxQ > 0) input.value = Math.min(n, maxQ);
  };

  window.onPrintDiffModeChange = function () {
    refreshPoolStatsAndMax();
  };

  window.onPrintDiagramModeChange = function () {
    refreshPoolStatsAndMax();
  };

  window.syncPrintKeyMode = function (source) {
    const sel = document.getElementById('print-key-mode');
    const chk = document.getElementById('print-include-solutions');
    if (!sel || !chk) return;
    if (source === 'select') {
      explicitKeyMode = sel.value;
      chk.checked = sel.value === 'full';
    } else {
      explicitKeyMode = chk.checked ? 'full' : 'quick';
      sel.value = explicitKeyMode;
    }
  };

  /* ---- Upgrade Existing Print Modal Hooks while Preserving Full Runtime Contracts ---- */
  const origUpdatePhase = window.updatePrintPhaseOptions;
  window.updatePrintPhaseOptions = function () {
    selectedTopics.clear();
    selectedLessonIds.clear();
    if (typeof origUpdatePhase === 'function') origUpdatePhase();
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.updatePrintModalMax = function () {
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  const prevOpenPrint = window.openPrintModal;
  window.openPrintModal = function () {
    selectedTopics.clear();
    selectedLessonIds.clear();
    explicitKeyMode = null;

    const diffEl = document.getElementById('print-diff-mode');
    if (diffEl) diffEl.value = 'graduated';
    const diagEl = document.getElementById('print-diagram-mode');
    if (diagEl) diagEl.value = 'any';
    const scratchEl = document.getElementById('print-scratch-space');
    if (scratchEl) scratchEl.value = 'none';
    const omrEl = document.getElementById('print-include-omr');
    if (omrEl) omrEl.checked = false;
    const chkSol = document.getElementById('print-include-solutions');
    const keySel = document.getElementById('print-key-mode');
    if (keySel && chkSol) keySel.value = chkSol.checked ? 'full' : 'quick';

    syncModalLocaleText();
    if (typeof prevOpenPrint === 'function') prevOpenPrint();
    renderFilterChips();
    refreshPoolStatsAndMax();
  };

  window.executePrint = function () {
    const count = parseInt(document.getElementById('print-q-count').value, 10) || 0;
    const track = document.getElementById('print-track-select').value;
    const pool = getFilteredPool();
    if (count <= 0 || pool.length === 0) return;

    closePrintModal();

    const t = dict[currentLang];
    const rtl = isAr();
    const container = document.getElementById('print-container');

    const questionsToPrint = selectQuestionsFromPool(pool, count);
    const includeSolutions = document.getElementById('print-include-solutions')
      ? !!document.getElementById('print-include-solutions').checked
      : false;
    const keyMode = explicitKeyMode === 'none' ? 'none' : (includeSolutions ? 'full' : 'quick');

    const customTitleEl = document.getElementById('print-custom-title');
    const customSubEl = document.getElementById('print-custom-subtitle');
    const scratchEl = document.getElementById('print-scratch-space');
    const omrEl = document.getElementById('print-include-omr');

    const effTrack = getActiveEffectiveTrack();
    const trackMeta = appData.tracks.find((tr) => tr.id === (track === 'current' ? effTrack : track));
    const defaultTitle = trackMeta
      ? `${rtl ? trackMeta.name_ar : trackMeta.name_en} — ${t.printTitle}`
      : t.printTitle;
    const finalTitle = (customTitleEl && customTitleEl.value && customTitleEl.value.trim())
      ? customTitleEl.value.trim()
      : defaultTitle;
    const finalSubtitle = (customSubEl && customSubEl.value && customSubEl.value.trim())
      ? customSubEl.value.trim()
      : '';
    const badgeLabel = trackMeta
      ? `${rtl ? trackMeta.name_ar : trackMeta.name_en} · A4`
      : (rtl ? 'ورقة اختبار A4' : 'A4 Exam Sheet');

    container.innerHTML = window.buildEdugatesWorksheetHtml(
      questionsToPrint,
      finalTitle,
      t.printAnswerKey,
      t.printQNum,
      badgeLabel,
      includeSolutions,
      rtl,
      {
        subtitle: finalSubtitle,
        scratchSpace: scratchEl ? scratchEl.value : 'none',
        includeOmr: omrEl ? !!omrEl.checked : false,
        keyMode,
      }
    );

    if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
      const logoWait = [...container.querySelectorAll('img')].map((im) =>
        im.complete ? Promise.resolve() : new Promise((r) => { im.onload = im.onerror = r; })
      );
      Promise.all([MathJax.typesetPromise([container]), ...logoWait]).then(() => {
        setTimeout(() => {
          window.print();
        }, 400);
      });
    } else {
      window.print();
    }
  };

  window.__edugatesCustomizer = {
    get selectedTopics() { return [...selectedTopics]; },
    get selectedLessonIds() { return [...selectedLessonIds]; },
    getFilteredPool,
    selectQuestionsFromPool,
  };
})();

