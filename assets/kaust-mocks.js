/* KAUST (KMC) & NSMO (Mawhiba) Official Full Mock Exams — Timed Simulator + Edugates A4 Print & Adaptive OMR Suite */
(function () {
  const COMP_CONFIG = {
    kaust: {
      id: 'kaust',
      bpField: 'kmc_blueprint',
      optCount: 5,
      ptsCorrect: 4,
      ptsWrong: -1,
      ptsBlank: 0,
      durationMin: 120,
      pillEn: 'KAUST KMC · G6–11',
      pillAr: 'كاوست KMC · 6–11',
      hubTitleEn: 'KAUST Math Competition (KMC) Full Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة لمسابقة كاوست (KMC)',
      badgeEn: 'KAUST KMC',
      badgeAr: 'كاوست KMC',
      examNameEn: 'KAUST Mathematics Competition (KMC)',
      examNameAr: 'مسابقة كاوست للرياضيات (KMC)',
      scoreTag: '+4 / −1 / 0',
      tracks: [
        {
          level: 'Track 1: Grades 6-7',
          code: 'T1',
          qCount: 24,
          tiers: { Easy: 8, Medium: 8, Hard: 8 },
          en: 'Track 1 · Grades 6–7',
          ar: 'المسار 1 · الصفوف 6–7',
          shortEn: 'Grades 6–7 (Junior)',
          shortAr: 'الصفوف 6–7 (التأسيسي)',
        },
        {
          level: 'Track 2: Grades 8-9',
          code: 'T2',
          qCount: 24,
          tiers: { Easy: 8, Medium: 8, Hard: 8 },
          en: 'Track 2 · Grades 8–9',
          ar: 'المسار 2 · الصفوف 8–9',
          shortEn: 'Grades 8–9 (Intermediate)',
          shortAr: 'الصفوف 8–9 (المتوسط)',
        },
        {
          level: 'Track 3: Grades 10-11',
          code: 'T3',
          qCount: 30,
          tiers: { Easy: 10, Medium: 10, Hard: 10 },
          en: 'Track 3 · Grades 10–11',
          ar: 'المسار 3 · الصفوف 10–11',
          shortEn: 'Grades 10–11 (Senior)',
          shortAr: 'الصفوف 10–11 (المتقدم)',
        },
      ],
    },
    nsmo: {
      id: 'nsmo',
      bpField: 'nsmo_blueprint',
      optCount: 4,
      ptsCorrect: 4,
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 90,
      pillEn: 'NSMO Mawhiba · G7–10',
      pillAr: 'نسمو موهبة · 7–10',
      hubTitleEn: 'NSMO / Mawhiba National Olympiad Full Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة لأولمبياد نسمو — موهبة',
      badgeEn: 'NSMO Mawhiba',
      badgeAr: 'نسمو موهبة',
      examNameEn: 'NSMO / Mawhiba National Mathematics Olympiad',
      examNameAr: 'أولمبياد العلوم والرياضيات الوطني (نسمو — موهبة)',
      scoreTag: '+4 / 0 / 0',
      tracks: [
        {
          level: 'Phase 1: Junior Olympiad (Grade 7)',
          code: 'P1',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Phase 1 · Grade 7 (Junior)',
          ar: 'المرحلة 1 · الصف 7 (الناشئين)',
          shortEn: 'Grade 7 (Junior Olympiad)',
          shortAr: 'الصف 7 (أولمبياد الناشئين)',
        },
        {
          level: 'Phase 2: Intermediate Olympiad (Grades 8-9)',
          code: 'P2',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Phase 2 · Grades 8–9 (Intermediate)',
          ar: 'المرحلة 2 · الصفان 8–9 (المتوسط)',
          shortEn: 'Grades 8–9 (Intermediate Olympiad)',
          shortAr: 'الصفان 8–9 (الأولمبياد المتوسط)',
        },
        {
          level: 'Phase 3: Senior National Olympiad (Grade 10)',
          code: 'P3',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Phase 3 · Grade 10 (Senior)',
          ar: 'المرحلة 3 · الصف 10 (المتقدم)',
          shortEn: 'Grade 10 (Senior Olympiad)',
          shortAr: 'الصف 10 (الأولمبياد المتقدم)',
        },
      ],
    },
    kangaroo: {
      id: 'kangaroo',
      bpField: 'kangaroo_blueprint',
      optCount: 5,
      ptsCorrect: 4,
      tierPoints: { Easy: 3, Medium: 4, Hard: 5 },
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 75,
      pillEn: 'Kangaroo · G1–12',
      pillAr: 'كانجارو · 1–12',
      hubTitleEn: 'Kangaroo Math Competition Full Official Mock Exams (Grades 1–12)',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة لمسابقة كانجارو موهبة للرياضيات (الصفوف 1–12)',
      badgeEn: 'Kangaroo Math',
      badgeAr: 'كانجارو موهبة',
      examNameEn: 'Kangaroo Math Competition (Mawhiba / KSF)',
      examNameAr: 'مسابقة كانجارو موهبة للرياضيات',
      scoreTag: '+3/+4/+5 · 0',
      tracks: [
        {
          level: 'PreEcolier',
          code: 'PRE',
          qCount: 24,
          tiers: { Easy: 8, Medium: 8, Hard: 8 },
          en: 'PreEcolier · Grades 1–2',
          ar: 'بري إيكولير · الصفان 1–2',
          shortEn: 'PreEcolier · Grades 1–2',
          shortAr: 'بري إيكولير · الصفان 1–2',
        },
        {
          level: 'Ecolier',
          code: 'ECO',
          qCount: 24,
          tiers: { Easy: 8, Medium: 8, Hard: 8 },
          en: 'Ecolier · Grades 3–4',
          ar: 'إيكولير · الصفان 3–4',
          shortEn: 'Ecolier · Grades 3–4',
          shortAr: 'إيكولير · الصفان 3–4',
        },
        {
          level: 'Benjamin',
          code: 'BEN',
          qCount: 24,
          tiers: { Easy: 8, Medium: 8, Hard: 8 },
          en: 'Benjamin · Grades 5–6',
          ar: 'بنجامين · الصفان 5–6',
          shortEn: 'Benjamin · Grades 5–6',
          shortAr: 'بنجامين · الصفان 5–6',
        },
        {
          level: 'Cadet',
          code: 'CAD',
          qCount: 30,
          tiers: { Easy: 10, Medium: 10, Hard: 10 },
          en: 'Cadet · Grades 7–8',
          ar: 'كاديت · الصفان 7–8',
          shortEn: 'Cadet · Grades 7–8',
          shortAr: 'كاديت · الصفان 7–8',
        },
        {
          level: 'Junior',
          code: 'JUN',
          qCount: 30,
          tiers: { Easy: 10, Medium: 10, Hard: 10 },
          en: 'Junior · Grades 9–10',
          ar: 'جونيور · الصفان 9–10',
          shortEn: 'Junior · Grades 9–10',
          shortAr: 'جونيور · الصفان 9–10',
        },
        {
          level: 'Student',
          code: 'STU',
          qCount: 30,
          tiers: { Easy: 10, Medium: 10, Hard: 10 },
          en: 'Student · Grades 11–12',
          ar: 'ستيودنت · الصفان 11–12',
          shortEn: 'Student · Grades 11–12',
          shortAr: 'ستيودنت · الصفان 11–12',
        },
      ],
    },
    nafes: {
      id: 'nafes',
      bpField: 'nafes_blueprint',
      optCount: 4,
      ptsCorrect: 1,
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 60,
      durationRangeLabel: '45–75',
      pillEn: 'Nafes Math · G3/6/9',
      pillAr: 'نافس رياضيات · 3/6/9',
      hubTitleEn: 'Nafes KSA Mathematics (ETEC) Official Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة لمادة الرياضيات — نافس (ETEC)',
      badgeEn: 'Nafes Math',
      badgeAr: 'نافس رياضيات',
      examNameEn: 'Nafes National Mathematics Assessment (ETEC — KSA)',
      examNameAr: 'اختبار نافس الوطني للرياضيات — هيئة تقويم التعليم والتدريب',
      scoreTag: '+1 / 0 / 0',
      tracks: [
        {
          level: 'Grade 3',
          code: 'G3',
          qCount: 20,
          durationMin: 45,
          tiers: { Easy: 7, Medium: 8, Hard: 5 },
          en: 'Grade 3 · Primary (20 Qs)',
          ar: 'الصف الثالث الابتدائي (20 سؤالاً)',
          shortEn: 'Grade 3 (Primary Benchmark)',
          shortAr: 'الصف الثالث الابتدائي (نافس 3)',
        },
        {
          level: 'Grade 6',
          code: 'G6',
          qCount: 25,
          durationMin: 60,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Grade 6 · Upper Primary (25 Qs)',
          ar: 'الصف السادس الابتدائي (25 سؤالاً)',
          shortEn: 'Grade 6 (Upper Primary Benchmark)',
          shortAr: 'الصف السادس الابتدائي (نافس 6)',
        },
        {
          level: 'Grade 9',
          code: 'G9',
          qCount: 30,
          durationMin: 75,
          tiers: { Easy: 10, Medium: 11, Hard: 9 },
          en: 'Grade 9 · Intermediate (30 Qs)',
          ar: 'الصف الثالث المتوسط (30 سؤالاً)',
          shortEn: 'Grade 9 (Intermediate Benchmark)',
          shortAr: 'الصف الثالث المتوسط (نافس 9)',
        },
      ],
    },
    nafes_science: {
      id: 'nafes_science',
      bpField: 'nafes_science_blueprint',
      optCount: 4,
      ptsCorrect: 1,
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 60,
      durationRangeLabel: '60–75',
      pillEn: 'Nafes Science · G6/9',
      pillAr: 'نافس علوم · 6/9',
      hubTitleEn: 'Nafes KSA National Science (ETEC) Official Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة لمادة العلوم — نافس (ETEC)',
      badgeEn: 'Nafes Science',
      badgeAr: 'نافس علوم',
      examNameEn: 'Nafes National Science Assessment (ETEC — KSA)',
      examNameAr: 'اختبار نافس الوطني للعلوم — هيئة تقويم التعليم والتدريب',
      scoreTag: '+1 / 0 / 0',
      tracks: [
        {
          level: 'Science · Grade 6',
          code: 'G6',
          qCount: 25,
          durationMin: 60,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Science · Grade 6 (25 Qs)',
          ar: 'العلوم · الصف السادس الابتدائي (25 سؤالاً)',
          shortEn: 'Science · Grade 6 Benchmark',
          shortAr: 'العلوم · الصف السادس الابتدائي (نافس 6)',
        },
        {
          level: 'Science · Grade 9',
          code: 'G9',
          qCount: 30,
          durationMin: 75,
          tiers: { Easy: 10, Medium: 11, Hard: 9 },
          en: 'Science · Grade 9 (30 Qs)',
          ar: 'العلوم · الصف الثالث المتوسط (30 سؤالاً)',
          shortEn: 'Science · Grade 9 Benchmark',
          shortAr: 'العلوم · الصف الثالث المتوسط (نافس 9)',
        },
      ],
    },
    nafes_english: {
      id: 'nafes_english',
      bpField: 'nafes_english_blueprint',
      optCount: 4,
      ptsCorrect: 1,
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 60,
      durationRangeLabel: '45–75',
      pillEn: 'Nafes English · G3/6/9',
      pillAr: 'نافس إنجليزي · 3/6/9',
      hubTitleEn: 'Nafes KSA National English (ETEC) Official Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة للغة الإنجليزية — نافس (ETEC)',
      badgeEn: 'Nafes English',
      badgeAr: 'نافس إنجليزي',
      examNameEn: 'Nafes National English Assessment (ETEC — KSA)',
      examNameAr: 'اختبار نافس الوطني للغة الإنجليزية — هيئة تقويم التعليم والتدريب',
      scoreTag: '+1 / 0 / 0',
      tracks: [
        {
          level: 'English · Grade 3',
          code: 'G3',
          qCount: 20,
          durationMin: 45,
          tiers: { Easy: 7, Medium: 7, Hard: 6 },
          en: 'English · Grade 3 (20 Qs)',
          ar: 'الإنجليزية · الصف الثالث الابتدائي (20 سؤالاً)',
          shortEn: 'English · Grade 3 Benchmark',
          shortAr: 'الإنجليزية · الصف الثالث الابتدائي (نافس 3)',
        },
        {
          level: 'English · Grade 6',
          code: 'G6',
          qCount: 25,
          durationMin: 60,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'English · Grade 6 (25 Qs)',
          ar: 'الإنجليزية · الصف السادس الابتدائي (25 سؤالاً)',
          shortEn: 'English · Grade 6 Benchmark',
          shortAr: 'الإنجليزية · الصف السادس الابتدائي (نافس 6)',
        },
        {
          level: 'English · Grade 9',
          code: 'G9',
          qCount: 30,
          durationMin: 75,
          tiers: { Easy: 10, Medium: 11, Hard: 9 },
          en: 'English · Grade 9 (30 Qs)',
          ar: 'الإنجليزية · الصف الثالث المتوسط (30 سؤالاً)',
          shortEn: 'English · Grade 9 Benchmark',
          shortAr: 'الإنجليزية · الصف الثالث المتوسط (نافس 9)',
        },
      ],
    },
    olympiad: {
      id: 'olympiad',
      bpField: 'olympiad_blueprint',
      optCount: 5,
      ptsCorrect: 6,
      ptsWrong: 0,
      ptsBlank: 0,
      durationMin: 90,
      pillEn: 'Olympiad · G7–12',
      pillAr: 'الأولمبياد · 7–12',
      hubTitleEn: 'Math Olympiad (IMO / BMO / AMC) Full Mock Exams',
      hubTitleAr: 'محاكي الاختبارات الرسمية الكاملة للأولمبياد الرياضي (IMO / BMO / AMC)',
      badgeEn: 'Math Olympiad',
      badgeAr: 'الأولمبياد الرياضي',
      examNameEn: 'International & National Mathematical Olympiad Screening',
      examNameAr: 'اختبارات التصفيات الأولمبية للرياضيات (IMO / BMO / AMC)',
      scoreTag: '+6 / 0 / 0',
      tracks: [
        {
          level: 'Tier 1: Junior Olympiad (Grades 7-8)',
          code: 'T1',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Tier 1 · Grades 7–8 (Junior)',
          ar: 'المستوى 1 · الصفان 7–8 (الناشئين)',
          shortEn: 'Grades 7–8 (Junior Olympiad)',
          shortAr: 'الصفان 7–8 (أولمبياد الناشئين)',
        },
        {
          level: 'Tier 2: Intermediate Olympiad (Grades 9-10)',
          code: 'T2',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Tier 2 · Grades 9–10 (Intermediate)',
          ar: 'المستوى 2 · الصفان 9–10 (المتوسط)',
          shortEn: 'Grades 9–10 (Intermediate Olympiad)',
          shortAr: 'الصفان 9–10 (الأولمبياد المتوسط)',
        },
        {
          level: 'Tier 3: Senior Olympiad (Grades 11-12)',
          code: 'T3',
          qCount: 25,
          tiers: { Easy: 9, Medium: 9, Hard: 7 },
          en: 'Tier 3 · Grades 11–12 (Senior)',
          ar: 'المستوى 3 · الصفان 11–12 (المتقدم)',
          shortEn: 'Grades 11–12 (Senior Olympiad)',
          shortAr: 'الصفان 11–12 (الأولمبياد المتقدم)',
        },
      ],
    },
  };

  const TOPIC_AR = {
    'Numbers & Operations': 'الأعداد والعمليات عليها',
    'Number Theory': 'نظرية الأعداد',
    Algebra: 'الجبر والأنماط',
    Inequalities: 'المتباينات والقيم القصوى',
    Geometry: 'الهندسة والقياس',
    Combinatorics: 'التركيبات والعد',
    'Combinatorics & Logic': 'التركيبات والمنطق',
    'Data & Probability': 'البيانات والاحتمالات',
    'Life Sciences': 'علوم الحياة',
    'Chemistry & Matter': 'الكيمياء والمادة',
    'Physics: Forces & Energy': 'الفيزياء: القوى والطاقة',
    'Earth & Space Sciences': 'علوم الأرض والفضاء',
    'Reading Comprehension': 'فهم المقروء',
    'Text Analysis & Purpose': 'تحليل النص والغرض',
    'Vocabulary & Context Clues': 'المفردات ودلالات السياق',
    'Grammar & Sentence Structure': 'القواعد وبنية الجملة',
  };

  const DIFF_AR = { Easy: 'أساسي (Part A)', Medium: 'متوسط (Part B)', Hard: 'متقدم (Part C)' };
  const DIFF_EN = { Easy: 'Part A · Easy', Medium: 'Part B · Medium', Hard: 'Part C · Hard' };
  const LABELS = ['A', 'B', 'C', 'D', 'E'];
  const STORAGE_KEY = 'supermath_kaust_mock_best_v1';

  let kaustDoc = null;
  let nsmoDoc = null;
  let kangarooDoc = null;
  let nafesDoc = null;
  let nafesScienceDoc = null;
  let nafesEnglishDoc = null;
  let olympiadDoc = null;
  let kaustMocks = [];
  let nsmoMocks = [];
  let kangarooMocks = [];
  let nafesMocks = [];
  let nafesScienceMocks = [];
  let nafesEnglishMocks = [];
  let olympiadMocks = [];
  let customKaustMocks = [];
  let customNsmoMocks = [];
  let customKangarooMocks = [];
  let customNafesMocks = [];
  let customNafesScienceMocks = [];
  let customNafesEnglishMocks = [];
  let customOlympiadMocks = [];
  let activeComp = 'kaust';
  let activeTrackByComp = {
    kaust: COMP_CONFIG.kaust.tracks[0].level,
    nsmo: COMP_CONFIG.nsmo.tracks[0].level,
    kangaroo: COMP_CONFIG.kangaroo.tracks[0].level,
    nafes: COMP_CONFIG.nafes.tracks[0].level,
    nafes_science: COMP_CONFIG.nafes_science.tracks[0].level,
    nafes_english: COMP_CONFIG.nafes_english.tracks[0].level,
    olympiad: COMP_CONFIG.olympiad.tracks[0].level,
  };
  let bestScores = {};

  let session = null;
  let timerHandle = null;

  const isAr = () => (typeof currentLang !== 'undefined' ? currentLang === 'ar' : false);
  const L = (ar, en) => (isAr() ? ar : en);
  const pick = (obj) => (obj ? (isAr() ? obj.ar : obj.en) || obj.en || {} : {});
  const topicLabel = (t) => (isAr() ? TOPIC_AR[t] || t : t);

  const getBankQuestions = () =>
    typeof appData !== 'undefined' && Array.isArray(appData.questions) ? appData.questions : [];

  function compForPaper(paper) {
    if (!paper) return COMP_CONFIG[activeComp];
    if (
      paper.track === 'olympiad' ||
      String(paper.id || '').startsWith('OLYM-') ||
      String(paper.level || '').startsWith('Tier ')
    ) {
      return COMP_CONFIG.olympiad;
    }
    if (
      paper.track === 'nafes_science' ||
      String(paper.id || '').startsWith('NAFS-SCI-') ||
      String(paper.level || '').startsWith('Science ')
    ) {
      return COMP_CONFIG.nafes_science;
    }
    if (
      paper.track === 'nafes_english' ||
      String(paper.id || '').startsWith('NAFS-ENG-') ||
      String(paper.level || '').startsWith('English ')
    ) {
      return COMP_CONFIG.nafes_english;
    }
    if (
      paper.track === 'nafes' ||
      String(paper.id || '').startsWith('NAFS-') ||
      ['Grade 3', 'Grade 6', 'Grade 9'].includes(paper.level)
    ) {
      return COMP_CONFIG.nafes;
    }
    if (
      paper.track === 'kangaroo' ||
      String(paper.id || '').startsWith('KANG-') ||
      ['PreEcolier', 'Ecolier', 'Benjamin', 'Cadet', 'Junior', 'Student'].includes(paper.level)
    ) {
      return COMP_CONFIG.kangaroo;
    }
    if (paper.track === 'nsmo' || String(paper.id || '').startsWith('NSMO-') || String(paper.level || '').startsWith('Phase ')) {
      return COMP_CONFIG.nsmo;
    }
    return COMP_CONFIG.kaust;
  }

  function compForLevel(level) {
    if (String(level || '').startsWith('Tier ')) return COMP_CONFIG.olympiad;
    if (String(level || '').startsWith('Science ')) return COMP_CONFIG.nafes_science;
    if (String(level || '').startsWith('English ')) return COMP_CONFIG.nafes_english;
    if (['Grade 3', 'Grade 6', 'Grade 9'].includes(level)) return COMP_CONFIG.nafes;
    if (['PreEcolier', 'Ecolier', 'Benjamin', 'Cadet', 'Junior', 'Student'].includes(level)) return COMP_CONFIG.kangaroo;
    return String(level || '').startsWith('Phase ') ? COMP_CONFIG.nsmo : COMP_CONFIG.kaust;
  }

  function docForComp(compId) {
    if (compId === 'olympiad') return olympiadDoc;
    if (compId === 'nafes_science') return nafesScienceDoc;
    if (compId === 'nafes_english') return nafesEnglishDoc;
    if (compId === 'nafes') return nafesDoc;
    if (compId === 'kangaroo') return kangarooDoc;
    if (compId === 'nsmo') return nsmoDoc;
    return kaustDoc;
  }

  function qPointsFor(paper, q, cfg) {
    const tp = (paper && paper.tier_points) || (cfg && cfg.tierPoints) || null;
    if (tp && q && tp[q.difficulty]) return tp[q.difficulty];
    if (q && q.kang_points && cfg && cfg.id === 'kangaroo') return q.kang_points;
    return (paper && paper.points_correct) ?? (cfg && cfg.ptsCorrect) ?? 4;
  }

  function diffBadgeLabel(q, paper, cfg, rtl) {
    const tp = (paper && paper.tier_points) || (cfg && cfg.tierPoints) || null;
    if (tp && q && tp[q.difficulty]) {
      const pts = tp[q.difficulty];
      const part = q.difficulty === 'Easy' ? 'A' : q.difficulty === 'Hard' ? 'C' : 'B';
      return rtl ? `${pts} نقاط (Part ${part})` : `Part ${part} · ${pts} pts`;
    }
    return rtl ? DIFF_AR[q.difficulty] || q.difficulty : DIFF_EN[q.difficulty] || q.difficulty;
  }

  function allKaustPapers() {
    return [...kaustMocks, ...customKaustMocks];
  }

  function allNsmoPapers() {
    return [...nsmoMocks, ...customNsmoMocks];
  }

  function allKangarooPapers() {
    return [...kangarooMocks, ...customKangarooMocks];
  }

  function allNafesPapers() {
    return [...nafesMocks, ...customNafesMocks];
  }

  function allNafesSciencePapers() {
    return [...nafesScienceMocks, ...customNafesScienceMocks];
  }

  function allNafesEnglishPapers() {
    return [...nafesEnglishMocks, ...customNafesEnglishMocks];
  }

  function allOlympiadPapers() {
    return [...olympiadMocks, ...customOlympiadMocks];
  }

  function allPapersAcrossComps() {
    return [
      ...allKaustPapers(),
      ...allNsmoPapers(),
      ...allKangarooPapers(),
      ...allNafesPapers(),
      ...allNafesSciencePapers(),
      ...allNafesEnglishPapers(),
      ...allOlympiadPapers(),
    ];
  }

  function currentCompPapers() {
    if (activeComp === 'olympiad') return allOlympiadPapers();
    if (activeComp === 'nafes_science') return allNafesSciencePapers();
    if (activeComp === 'nafes_english') return allNafesEnglishPapers();
    if (activeComp === 'nafes') return allNafesPapers();
    if (activeComp === 'kangaroo') return allKangarooPapers();
    if (activeComp === 'nsmo') return allNsmoPapers();
    return allKaustPapers();
  }

  function findPaper(id) {
    return allPapersAcrossComps().find((p) => p.id === id) || null;
  }

  function resolvePaperQuestions(paper) {
    const qs = getBankQuestions();
    if (!qs.length || !paper) return [];
    const cfg = compForPaper(paper);
    const byId = new Map(qs.filter((q) => q.track === cfg.id).map((q) => [q.id, q]));
    return (paper.question_ids || []).map((id) => byId.get(id)).filter(Boolean);
  }

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
    const cfg = compForPaper(paper);
    const ptsCorrect = paper.points_correct ?? cfg.ptsCorrect;
    const ptsWrong = paper.points_wrong ?? cfg.ptsWrong;
    const ptsBlank = paper.points_blank ?? cfg.ptsBlank;

    let correct = 0;
    let wrong = 0;
    let blank = 0;
    let earnedCorrectPts = 0;
    let maxPoints = 0;
    const byDiff = {
      Easy: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
      Medium: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
      Hard: { total: 0, correct: 0, wrong: 0, blank: 0, points: 0 },
    };
    const byTopic = {};
    const weakLessons = new Map();

    const doc = docForComp(cfg.id);
    const bpMap = (doc && doc.blueprint_to_lesson) || {};
    const qLesMap = paper.question_lessons || {};

    questions.forEach((q, idx) => {
      const choice = answers[idx];
      const qPts = qPointsFor(paper, q, cfg);
      maxPoints += qPts;
      const d = byDiff[q.difficulty] || byDiff.Medium;
      d.total += 1;
      if (!byTopic[q.topic]) byTopic[q.topic] = { total: 0, correct: 0, wrong: 0, blank: 0 };
      byTopic[q.topic].total += 1;

      const lid = qLesMap[q.id] || bpMap[q[cfg.bpField]] || null;

      if (choice === undefined || choice === null) {
        blank += 1;
        d.blank += 1;
        d.points += ptsBlank;
        byTopic[q.topic].blank += 1;
        if (lid) weakLessons.set(lid, (weakLessons.get(lid) || 0) + 1);
      } else if (choice === q.correct_index) {
        correct += 1;
        d.correct += 1;
        d.points += qPts;
        earnedCorrectPts += qPts;
        byTopic[q.topic].correct += 1;
      } else {
        wrong += 1;
        d.wrong += 1;
        d.points += ptsWrong;
        byTopic[q.topic].wrong += 1;
        if (lid) weakLessons.set(lid, (weakLessons.get(lid) || 0) + 1);
      }
    });

    const rawScore = earnedCorrectPts + wrong * ptsWrong + blank * ptsBlank;
    const score = Math.max(0, rawScore);
    const pct = maxPoints > 0 ? Math.round((score / maxPoints) * 100) : 0;

    return {
      score,
      rawScore,
      earnedCorrectPts,
      maxPoints,
      pct,
      correct,
      wrong,
      blank,
      ptsCorrect,
      ptsWrong,
      ptsBlank,
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

  /* ---- Dynamic Balanced Official Mock Generator (Supports Kangaroo, KAUST & NSMO) ---- */
  window.generateCustomKaustMock = function (level) {
    const targetLevel = level || activeTrackByComp[activeComp];
    const cfg = compForLevel(targetLevel);
    const tr = cfg.tracks.find((t) => t.level === targetLevel) || cfg.tracks[0];
    const bank = getBankQuestions().filter((q) => q.track === cfg.id && q.level === tr.level);
    if (!bank.length) return;

    const usedBps = new Set();
    const chosen = [];
    const doc = docForComp(cfg.id);
    const bpMap = (doc && doc.blueprint_to_lesson) || {};

    ['Hard', 'Easy', 'Medium'].forEach((diff) => {
      const targetTierCount = tr.tiers[diff];
      const pool = bank.filter((q) => q.difficulty === diff);
      const shuffled = [...pool].sort(() => Math.random() - 0.5);
      const lessonCounts = {};
      shuffled.sort((a, b) => (lessonCounts[bpMap[a[cfg.bpField]]] || 0) - (lessonCounts[bpMap[b[cfg.bpField]]] || 0));
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= targetTierCount) break;
        if (usedBps.has(q[cfg.bpField])) continue;
        const lid = bpMap[q[cfg.bpField]] || 'misc';
        if ((lessonCounts[lid] || 0) >= 2) continue;
        usedBps.add(q[cfg.bpField]);
        lessonCounts[lid] = (lessonCounts[lid] || 0) + 1;
        chosen.push(q);
      }
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= targetTierCount) break;
        if (chosen.some((x) => x.id === q.id)) continue;
        if (!usedBps.has(q[cfg.bpField])) {
          usedBps.add(q[cfg.bpField]);
          chosen.push(q);
        }
      }
      for (const q of shuffled) {
        if (chosen.filter((x) => x.difficulty === diff).length >= targetTierCount) break;
        if (!chosen.some((x) => x.id === q.id)) chosen.push(q);
      }
    });

    const ordered = [
      ...chosen.filter((q) => q.difficulty === 'Easy'),
      ...chosen.filter((q) => q.difficulty === 'Medium'),
      ...chosen.filter((q) => q.difficulty === 'Hard'),
    ];

    const customList =
      cfg.id === 'olympiad'
        ? customOlympiadMocks
        : cfg.id === 'nafes_science'
        ? customNafesScienceMocks
        : cfg.id === 'nafes_english'
        ? customNafesEnglishMocks
        : cfg.id === 'nafes'
        ? customNafesMocks
        : cfg.id === 'kangaroo'
        ? customKangarooMocks
        : cfg.id === 'nsmo'
        ? customNsmoMocks
        : customKaustMocks;
    const baseList =
      cfg.id === 'olympiad'
        ? olympiadMocks
        : cfg.id === 'nafes_science'
        ? nafesScienceMocks
        : cfg.id === 'nafes_english'
        ? nafesEnglishMocks
        : cfg.id === 'nafes'
        ? nafesMocks
        : cfg.id === 'kangaroo'
        ? kangarooMocks
        : cfg.id === 'nsmo'
        ? nsmoMocks
        : kaustMocks;
    const baseCountForLevel = baseList.filter((p) => p.level === tr.level).length;
    const customIdx = customList.filter((p) => p.level === tr.level).length + 1;
    const svgCnt = ordered.filter((q) => q.content && q.content.en && q.content.en.diagram).length;
    const topicCounts = {};
    const qLessons = {};
    ordered.forEach((q) => {
      topicCounts[q.topic] = (topicCounts[q.topic] || 0) + 1;
      if (bpMap[q[cfg.bpField]]) qLessons[q.id] = bpMap[q[cfg.bpField]];
    });

    const eCnt = tr.tiers.Easy;
    const mCnt = tr.tiers.Medium;
    const prefix =
      cfg.id === 'olympiad'
        ? 'OLYM'
        : cfg.id === 'nafes_science'
        ? 'NAFS-SCI'
        : cfg.id === 'nafes_english'
        ? 'NAFS-ENG'
        : cfg.id === 'nafes'
        ? 'NAFS'
        : cfg.id === 'kangaroo'
        ? 'KANG'
        : cfg.id === 'nsmo'
        ? 'NSMO'
        : 'KMC';
    const maxPts = cfg.tierPoints
      ? eCnt * cfg.tierPoints.Easy + mCnt * cfg.tierPoints.Medium + tr.tiers.Hard * cfg.tierPoints.Hard
      : ordered.length * cfg.ptsCorrect;
    const isNafes = cfg.id === 'nafes';
    const isNafesSci = cfg.id === 'nafes_science';
    const isNafesEng = cfg.id === 'nafes_english';

    const paper = {
      id: `${prefix}-MOCK-${tr.code}-CUSTOM-${customIdx}`,
      track: cfg.id,
      option_count: cfg.optCount,
      paper_num: baseCountForLevel + customIdx,
      is_custom: true,
      level: tr.level,
      track_code: tr.code,
      grades_en: tr.shortEn,
      grades_ar: tr.shortAr,
      question_count: ordered.length,
      duration_minutes: tr.durationMin || cfg.durationMin,
      tier_points: cfg.tierPoints || null,
      points_correct: cfg.ptsCorrect,
      points_wrong: cfg.ptsWrong,
      points_blank: cfg.ptsBlank,
      max_points: maxPts,
      svg_count: svgCnt,
      topic_counts: topicCounts,
      sections: [
        {
          id: 'A',
          difficulty: 'Easy',
          start_q: 1,
          end_q: eCnt,
          en: isNafesSci
            ? `Part A — Scientific Knowledge & Recall (Questions 1–${eCnt})`
            : isNafesEng
            ? `Part A — Literal Comprehension & Core Usage (Questions 1–${eCnt})`
            : isNafes
            ? `Part A — Knowing & Direct Recall (Questions 1–${eCnt})`
            : cfg.tierPoints
            ? `Part A — 3-Point Problems (Questions 1–${eCnt})`
            : `Part A — Core Reasoning & Speed (Questions 1–${eCnt})`,
          ar: isNafesSci
            ? `الجزء الأول (A) — المعرفة والاستدعاء العلمي (الأسئلة 1–${eCnt})`
            : isNafesEng
            ? `الجزء الأول (A) — الفهم الحرفي والاستخدام الأساسي (الأسئلة 1–${eCnt})`
            : isNafes
            ? `الجزء الأول (A) — المعرفة والاستدعاء المباشر (الأسئلة 1–${eCnt})`
            : cfg.tierPoints
            ? `الجزء الأول (A) — مسائل الـ 3 نقاط (الأسئلة 1–${eCnt})`
            : `الجزء الأول (A) — التفكير الأساسي والسرعة (الأسئلة 1–${eCnt})`,
        },
        {
          id: 'B',
          difficulty: 'Medium',
          start_q: eCnt + 1,
          end_q: eCnt + mCnt,
          en: isNafesSci
            ? `Part B — Scientific Application & Inquiry (Questions ${eCnt + 1}–${eCnt + mCnt})`
            : isNafesEng
            ? `Part B — Context Clues & Sentence Structure (Questions ${eCnt + 1}–${eCnt + mCnt})`
            : isNafes
            ? `Part B — Applying Concepts & Multi-Step Skills (Questions ${eCnt + 1}–${eCnt + mCnt})`
            : cfg.tierPoints
            ? `Part B — 4-Point Problems (Questions ${eCnt + 1}–${eCnt + mCnt})`
            : `Part B — Multi-Step Contest Problems (Questions ${eCnt + 1}–${eCnt + mCnt})`,
          ar: isNafesSci
            ? `الجزء الثاني (B) — التطبيق والاستقصاء العلمي (الأسئلة ${eCnt + 1}–${eCnt + mCnt})`
            : isNafesEng
            ? `الجزء الثاني (B) — دلالات السياق وبنية الجملة (الأسئلة ${eCnt + 1}–${eCnt + mCnt})`
            : isNafes
            ? `الجزء الثاني (B) — التطبيق وحل المسائل (الأسئلة ${eCnt + 1}–${eCnt + mCnt})`
            : cfg.tierPoints
            ? `الجزء الثاني (B) — مسائل الـ 4 نقاط (الأسئلة ${eCnt + 1}–${eCnt + mCnt})`
            : `الجزء الثاني (B) — المسائل التنافسية متعددة الخطوات (الأسئلة ${eCnt + 1}–${eCnt + mCnt})`,
        },
        {
          id: 'C',
          difficulty: 'Hard',
          start_q: eCnt + mCnt + 1,
          end_q: ordered.length,
          en: isNafesSci
            ? `Part C — Scientific Reasoning & Analysis (Questions ${eCnt + mCnt + 1}–${ordered.length})`
            : isNafesEng
            ? `Part C — Inference, Purpose & Textual Reasoning (Questions ${eCnt + mCnt + 1}–${ordered.length})`
            : isNafes
            ? `Part C — Mathematical Reasoning & Problem Solving (Questions ${eCnt + mCnt + 1}–${ordered.length})`
            : cfg.tierPoints
            ? `Part C — 5-Point Problems (Questions ${eCnt + mCnt + 1}–${ordered.length})`
            : `Part C — Olympiad Qualifier Challenge (Questions ${eCnt + mCnt + 1}–${ordered.length})`,
          ar: isNafesSci
            ? `الجزء الثالث (C) — الاستدلال العلمي وتحليل الأدلة (الأسئلة ${eCnt + mCnt + 1}–${ordered.length})`
            : isNafesEng
            ? `الجزء الثالث (C) — الاستنتاج وتحليل الغرض والاستدلال النصي (الأسئلة ${eCnt + mCnt + 1}–${ordered.length})`
            : isNafes
            ? `الجزء الثالث (C) — الاستدلال الرياضي المتقدم (الأسئلة ${eCnt + mCnt + 1}–${ordered.length})`
            : cfg.tierPoints
            ? `الجزء الثالث (C) — مسائل الـ 5 نقاط (الأسئلة ${eCnt + mCnt + 1}–${ordered.length})`
            : `الجزء الثالث (C) — تحدي التصفيات الأولمبية (الأسئلة ${eCnt + mCnt + 1}–${ordered.length})`,
        },
      ],
      en: {
        title: `Custom Official ${cfg.badgeEn} Mock #${customIdx} — Fresh Balanced Simulation`,
        focus: `Dynamically sampled ${ordered.length}-question official paper across ${usedBps.size} distinct ${cfg.badgeEn} blueprints.`,
      },
      ar: {
        title: `اختبار ${cfg.badgeAr} تجريبي مخصص #${customIdx} — محاكاة متوازنة جديدة`,
        focus: `ورقة اختبار رسمية مولّدة من ${ordered.length} سؤالاً عبر ${usedBps.size} نمطاً مختلفاً من أنماط المسابقة.`,
      },
      question_ids: ordered.map((q) => q.id),
      question_lessons: qLessons,
    };

    customList.unshift(paper);
    activeComp = cfg.id;
    activeTrackByComp[cfg.id] = tr.level;
    render();
    return paper.id;
  };

  /* ---- Simulator Controls ---- */
  window.setMockCompetition = function (compId) {
    if (
      compId !== 'kaust' &&
      compId !== 'nsmo' &&
      compId !== 'kangaroo' &&
      compId !== 'nafes' &&
      compId !== 'nafes_science' &&
      compId !== 'nafes_english' &&
      compId !== 'olympiad'
    ) return;
    if (compId === 'nsmo' && !nsmoMocks.length) return;
    if (compId === 'kangaroo' && !kangarooMocks.length) return;
    if (compId === 'nafes' && !nafesMocks.length) return;
    if (compId === 'nafes_science' && !nafesScienceMocks.length) return;
    if (compId === 'nafes_english' && !nafesEnglishMocks.length) return;
    if (compId === 'olympiad' && !olympiadMocks.length) return;
    if (session && session.mode === 'exam') return;
    session = null;
    activeComp = compId;
    render();
  };

  window.setKaustMockTrack = function (level) {
    const cfg = compForLevel(level);
    activeComp = cfg.id;
    activeTrackByComp[cfg.id] = level;
    render();
  };

  window.jumpToKaustMocks = function (levelOrComp) {
    if (!session) {
      if (
        levelOrComp === 'kaust' ||
        levelOrComp === 'nsmo' ||
        levelOrComp === 'kangaroo' ||
        levelOrComp === 'nafes' ||
        levelOrComp === 'nafes_science' ||
        levelOrComp === 'nafes_english' ||
        levelOrComp === 'olympiad'
      ) {
        if (
          (levelOrComp !== 'nsmo' || nsmoMocks.length) &&
          (levelOrComp !== 'kangaroo' || kangarooMocks.length) &&
          (levelOrComp !== 'nafes' || nafesMocks.length) &&
          (levelOrComp !== 'nafes_science' || nafesScienceMocks.length) &&
          (levelOrComp !== 'nafes_english' || nafesEnglishMocks.length) &&
          (levelOrComp !== 'olympiad' || olympiadMocks.length)
        ) {
          activeComp = levelOrComp;
        }
      } else if (levelOrComp) {
        const cfg = compForLevel(levelOrComp);
        if (
          (cfg.id !== 'nsmo' || nsmoMocks.length) &&
          (cfg.id !== 'kangaroo' || kangarooMocks.length) &&
          (cfg.id !== 'nafes' || nafesMocks.length) &&
          (cfg.id !== 'nafes_science' || nafesScienceMocks.length) &&
          (cfg.id !== 'nafes_english' || nafesEnglishMocks.length) &&
          (cfg.id !== 'olympiad' || olympiadMocks.length)
        ) {
          activeComp = cfg.id;
          activeTrackByComp[cfg.id] = levelOrComp;
        }
      }
    }
    if (typeof window.setAppView === 'function') window.setAppView('mocks', true);
    render();
    const el = document.getElementById('kaust-mock-exams');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  window.startKaustMock = function (paperId) {
    const paper = findPaper(paperId);
    if (!paper) return;
    const qs = resolvePaperQuestions(paper);
    if (!qs.length) return;
    const cfg = compForPaper(paper);
    activeComp = cfg.id;
    activeTrackByComp[cfg.id] = paper.level;
    session = {
      mode: 'exam',
      paper,
      questions: qs,
      answers: {},
      flags: {},
      currentIdx: 0,
      viewMode: 'single',
      remainingSec: (paper.duration_minutes || cfg.durationMin) * 60,
      elapsedSec: 0,
      paused: false,
      confirmSubmit: false,
      confirmExit: false,
      reviewFilter: 'all',
      report: null,
    };
    if (typeof window.setAppView === 'function') window.setAppView('mocks', true);
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
  function buildOmrBubbleGridHtml(totalQ, optCount, shadedMap, studentAnswers, rtl, scoreTag) {
    if (typeof window.buildEdugatesOmrSheetHtml === 'function') {
      return window.buildEdugatesOmrSheetHtml(totalQ, optCount, shadedMap, studentAnswers, rtl, scoreTag);
    }
    return '';
  }

  function buildCoverPageRowHtml(paper, totalQ, rtl) {
    const cfg = compForPaper(paper);
    const optCount = paper.option_count || cfg.optCount;
    const optRange = optCount === 4 ? 'A–D' : 'A–E';
    const dur = paper.duration_minutes || cfg.durationMin;
    const ptsCorrect = paper.points_correct ?? cfg.ptsCorrect;
    const ptsWrong = paper.points_wrong ?? cfg.ptsWrong;
    const tp = paper.tier_points || cfg.tierPoints || null;
    const pText = rtl ? paper.ar : paper.en;
    const grades = rtl ? paper.grades_ar : paper.grades_en;
    const maxPts = paper.max_points || (tp ? Math.round((totalQ / 3) * (tp.Easy + tp.Medium + tp.Hard)) : totalQ * ptsCorrect);
    const wrongTxtAr = ptsWrong < 0 ? `<span dir="ltr">${ptsWrong}</span> خطأ` : '0 خطأ (بدون خصم)';
    const wrongTxtEn = ptsWrong < 0 ? `<span dir="ltr">${ptsWrong}</span> Wrong` : '0 Wrong (No Penalty)';

    const scoringSpecHtml = tp
      ? `<span dir="ltr">+${tp.Easy} / +${tp.Medium} / +${tp.Hard}</span> ${rtl ? 'صحيح' : 'Correct'} · ${rtl ? wrongTxtAr : wrongTxtEn} · <span dir="ltr">0</span> ${rtl ? 'متروك' : 'Blank'}`
      : `<span dir="ltr">+${ptsCorrect}</span> ${rtl ? 'صحيح' : 'Correct'} · ${rtl ? wrongTxtAr : wrongTxtEn} · <span dir="ltr">0</span> ${rtl ? 'متروك' : 'Blank'}`;

    const scoringRuleLi = tp
      ? rtl
        ? `طريقة احتساب درجات كانجارو: <strong>+${tp.Easy} نقاط</strong> لكل سؤال في الجزء A، و<strong>+${tp.Medium} نقاط</strong> في الجزء B، و<strong>+${tp.Hard} نقاط</strong> في الجزء C، و<strong>بدون خصم درجات (0)</strong> للإجابات الخاطئة أو المتروكة.`
        : `Kangaroo scoring: <strong>+${tp.Easy} points</strong> in Part A, <strong>+${tp.Medium} points</strong> in Part B, and <strong>+${tp.Hard} points</strong> in Part C, with <strong>no penalty (0 points)</strong> for wrong or blank answers.`
      : ptsWrong < 0
      ? rtl
        ? `طريقة احتساب الدرجات: <strong>+${ptsCorrect} نقاط</strong> لكل إجابة صحيحة، و<strong>خصم نقطة واحدة (−1)</strong> لكل إجابة خاطئة، و<strong>0 نقطة</strong> للسؤال المتروك بدون تظليل.`
        : `Contest scoring: <strong>+${ptsCorrect} points</strong> for each correct choice, <strong>−1 point</strong> for each incorrect choice, and <strong>0 points</strong> for each blank question.`
      : rtl
      ? `طريقة احتساب الدرجات: <strong>+${ptsCorrect} ${ptsCorrect === 1 ? 'نقطة' : 'نقاط'}</strong> لكل إجابة صحيحة، و<strong>بدون خصم درجات (0)</strong> للإجابات الخاطئة أو المتروكة.`
      : `${(cfg.id === 'nafes' || cfg.id === 'nafes_science' || cfg.id === 'nafes_english') ? 'Official ETEC Nafes' : 'Olympiad'} scoring: <strong>+${ptsCorrect} ${ptsCorrect === 1 ? 'point' : 'points'}</strong> for each correct choice, with <strong>no penalty (0 points)</strong> for wrong or blank responses.`;

    return `<div class="eg-mock-cover no-break">
      <div class="eg-mock-cover-top">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <span class="eg-badge">${rtl ? cfg.examNameAr : cfg.examNameEn}</span>
          <span class="eg-badge eg-badge-alt">${grades}</span>
          <span class="eg-badge eg-badge-soft">${rtl ? `الزمن: ${dur} دقيقة · بدون آلة حاسبة` : `Time: ${dur} Minutes · No Calculator`}</span>
        </div>
        <h2 class="eg-mock-cover-title">${pText.title}</h2>
        <div class="eg-mock-cover-specs">
          <span><strong>${rtl ? 'عدد الأسئلة:' : 'Questions:'}</strong> ${totalQ} MCQ (${optRange})</span>
          <span><strong>${rtl ? 'الدرجة العظمى:' : 'Maximum Score:'}</strong> ${maxPts} ${rtl ? 'نقطة' : 'pts'}</span>
          <span><strong>${rtl ? 'نظام التصحيح:' : 'Scoring:'}</strong> ${scoringSpecHtml}</span>
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
              ? `يتكوّن هذا الاختبار من <strong>${totalQ} سؤالاً</strong> متدرج الصعوبة في ثلاثة أجزاء (Part A, B, C) وزمن الإجابة <strong>${dur} دقيقة</strong>.`
              : `This examination consists of <strong>${totalQ} multiple-choice questions (${optRange})</strong> across three graduated tiers (Parts A, B, C) to be completed in <strong>${dur} minutes</strong>.`
          }</li>
          <li>${
            rtl
              ? 'يُمنع منعاً باتاً استخدام الآلات الحاسبة أو الهواتف الذكية أو الساعات الرقمية أو أي مراجع خارجية.'
              : 'Calculators, smart devices, rulers with formulas, and external notes are strictly prohibited.'
          }</li>
          <li>${scoringRuleLi}</li>
        </ul>
      </div>

      ${buildOmrBubbleGridHtml(totalQ, optCount, null, null, rtl, cfg.scoreTag)}
    </div>`;
  }

  function buildMockExamPrintHtml(paper, questions, mode, rtl, gradedSession) {
    const cfg = compForPaper(paper);
    const optCount = paper.option_count || cfg.optCount;
    const pText = rtl ? paper.ar : paper.en;
    const grades = rtl ? paper.grades_ar : paper.grades_en;
    const badge = `${grades} · ${rtl ? cfg.badgeAr : cfg.badgeEn} · A4`;
    const totalQ = questions.length;
    const printSection = window.edugatesPrintSection;
    if (typeof printSection !== 'function') return '';

    const parts = [];

    if (mode === 'full' || mode === 'student') {
      parts.push(printSection([buildCoverPageRowHtml(paper, totalQ, rtl)], pText.title, badge, rtl, false));

      const sectionStarts = new Map();
      (paper.sections || []).forEach((s) => {
        sectionStarts.set((s.start_q || 1) - 1, s);
      });

      const qRows = questions.map((q, idx) => {
        const sec = sectionStarts.get(idx);
        const secBanner = sec ? `<div class="eg-sec-heading">${rtl ? sec.ar : sec.en}</div>` : '';
        const qContent = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
        const diag = qContent.diagram || q.diagram || '';
        const diffCls = q.difficulty === 'Easy' ? 'eg-diff-easy' : q.difficulty === 'Hard' ? 'eg-diff-hard' : 'eg-diff-med';
        const diffLbl = diffBadgeLabel(q, paper, cfg, rtl);
        const optsHtml = `<div class="eg-ws-opts">${(qContent.options || [])
          .map((opt, oIdx) => `<div class="eg-ws-opt"><span class="eg-opt-l">${LABELS[oIdx]}</span><span class="math-font">${opt}</span></div>`)
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

      parts.push(printSection(qRows, `${pText.title} — ${rtl ? 'كراسة الأسئلة' : 'Question Booklet'}`, badge, rtl, true));
    }

    if (mode === 'full' || mode === 'key') {
      const shadedMap = {};
      questions.forEach((q, idx) => {
        shadedMap[idx] = q.correct_index;
      });
      const stuAns = gradedSession && gradedSession.paper.id === paper.id ? gradedSession.answers : null;
      const rep = gradedSession && gradedSession.paper.id === paper.id ? gradedSession.report : null;
      const wrongPts = paper.points_wrong ?? cfg.ptsWrong;

      const reportBanner = rep
        ? `<div class="eg-banner no-break">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <strong>${rtl ? 'تقرير أداء الطالب في الاختبار التجريبي' : 'Student Graded Mock Exam Report'}</strong>
              <span class="eg-badge">${rtl ? 'الدرجة الرسمية:' : 'Official Score:'} ${rep.score} / ${rep.maxPoints} (${rep.pct}%)</span>
            </div>
            <div class="eg-summary" style="margin-top:1.5mm">
              ${rtl ? 'إجابات صحيحة:' : 'Correct:'} <strong>${rep.correct}</strong> (+${rep.earnedCorrectPts ?? rep.correct * rep.ptsCorrect}) ·
              ${rtl ? 'إجابات خاطئة:' : 'Wrong:'} <strong>${rep.wrong}</strong> (${wrongPts < 0 ? '−' + rep.wrong : '0'}) ·
              ${rtl ? 'أسئلة متروكة:' : 'Blank:'} <strong>${rep.blank}</strong> (0) ·
              ${rtl ? 'الزمن المستغرق:' : 'Time Used:'} <strong dir="ltr">${formatClock(rep.elapsedSec)}</strong>
            </div>
          </div>`
        : '';

      const quickKey = `<div class="eg-key-box no-break">
        <div class="eg-h3">${rtl ? 'جدول الإجابات السريع' : 'Quick Answer Key Reference'} (1–${totalQ})</div>
        <div class="eg-key-grid">
          ${questions
            .map((q, idx) => `<div class="eg-key-cell" dir="ltr"><strong>${idx + 1}.</strong> <span>(${LABELS[q.correct_index]})</span></div>`)
            .join('')}
        </div>
      </div>`;

      const solCards = questions.map((q, idx) => {
        const c = (q.content && (q.content[rtl ? 'ar' : 'en'] || q.content.en)) || {};
        const stuChoice = stuAns ? stuAns[idx] : undefined;
        const qPts = qPointsFor(paper, q, cfg);
        let stuNote = '';
        if (stuAns) {
          if (stuChoice === undefined || stuChoice === null) {
            stuNote = ` · ${rtl ? 'إجابتك: متروك (0)' : 'Your choice: Blank (0)'}`;
          } else if (stuChoice === q.correct_index) {
            stuNote = ` · ✓ ${rtl ? `إجابتك صحيحة (+${qPts})` : `Your choice: Correct (+${qPts})`}`;
          } else {
            const wLbl = wrongPts < 0 ? '−1' : '0';
            stuNote = ` · ✗ ${rtl ? `إجابتك: (${LABELS[stuChoice]}) (${wLbl})` : `Your choice: (${LABELS[stuChoice]}) (${wLbl})`}`;
          }
        }
        return `<div class="eg-card eg-sol-card no-break">
          <div class="eg-sol-h">${rtl ? 'سؤال' : 'Question'} ${idx + 1} — ${rtl ? 'الإجابة الصحيحة:' : 'Correct Answer:'} (${LABELS[q.correct_index]})${stuNote} <span class="eg-ws-qmeta">(${q.id})</span></div>
          <div class="math-font eg-prose">${c.explanation || ''}</div>
        </div>`;
      });

      const keyRows = [
        ...(reportBanner ? [reportBanner] : []),
        buildOmrBubbleGridHtml(totalQ, optCount, shadedMap, stuAns, rtl, cfg.scoreTag),
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
    const targetLevel = level || activeTrackByComp[activeComp];
    const cfg = compForLevel(targetLevel);
    const tr = cfg.tracks.find((t) => t.level === targetLevel) || cfg.tracks[0];
    const templatePaper = {
      track: cfg.id,
      option_count: cfg.optCount,
      duration_minutes: tr.durationMin || cfg.durationMin,
      tier_points: cfg.tierPoints || null,
      points_correct: cfg.ptsCorrect,
      points_wrong: cfg.ptsWrong,
      max_points: cfg.tierPoints
        ? tr.tiers.Easy * cfg.tierPoints.Easy + tr.tiers.Medium * cfg.tierPoints.Medium + tr.tiers.Hard * cfg.tierPoints.Hard
        : tr.qCount * cfg.ptsCorrect,
      paper_num: 1,
      grades_en: tr.shortEn,
      grades_ar: tr.shortAr,
      en: { title: `Official ${cfg.badgeEn} Optical Answer Sheet (${tr.qCount} Questions)` },
      ar: { title: `ورقة رصد وتظليل الإجابات الرسمية (${cfg.badgeAr} · ${tr.qCount} سؤالاً)` },
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
    const cfg = compForPaper(session.paper);
    const qContent = (q.content && (q.content[isAr() ? 'ar' : 'en'] || q.content.en)) || {};
    const diag = qContent.diagram || q.diagram || '';
    const selected = session.answers[idx];
    const flagged = !!session.flags[idx];
    const diffCls = q.difficulty === 'Easy' ? 'eg-diff-easy' : q.difficulty === 'Hard' ? 'eg-diff-hard' : 'eg-diff-med';
    const diffLbl = diffBadgeLabel(q, session.paper, cfg, isAr());

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
              ? `<button type="button" onclick="clearKaustMockOption(${idx})" class="eg-btn eg-btn-sm">${L('مسح التظليل (0 نقطة)', 'Clear Choice (0 pt)')}</button>`
              : `<span class="eg-lc-pill">${L('متروك (0 نقطة)', 'Blank (0 pts)')}</span>`
          }
          <button type="button" onclick="toggleKaustMockFlag(${idx})" class="eg-btn eg-btn-sm${flagged ? ' eg-flag-on' : ''}">
            ${flagged ? L('معلّم للمراجعة', 'Flagged') : L('تعليم للمراجعة', 'Flag')}
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
    const cfg = compForPaper(p);
    const pText = pick(p);
    const total = session.questions.length;
    const answeredCount = Object.keys(session.answers).length;
    const blankCount = total - answeredCount;
    const flagCount = Object.values(session.flags).filter(Boolean).length;
    const clockWarn = session.remainingSec <= 900 && session.remainingSec > 300 ? ' eg-clock-warn' : '';
    const clockCrit = session.remainingSec <= 300 ? ' eg-clock-crit' : '';
    const wrongPts = p.points_wrong ?? cfg.ptsWrong;

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
            <strong>${L('تأكيد تسليم ورقة الاختبار:', 'Confirm Exam Submission:')}</strong>
            ${L(
              `أجبت عن ${answeredCount} سؤالاً وتركت ${blankCount} بدون إجابة. هل تريد إنهاء الاختبار وإصدار التقرير الآن؟`,
              `You answered ${answeredCount} of ${total} questions and left ${blankCount} blank. Submit and grade now?`
            )}
          </div>
          <div class="flex flex-wrap gap-2">
            <button type="button" onclick="confirmSubmitKaustMock()" class="eg-btn eg-btn-go">${L('نعم، سلّم وصحّح الآن', 'Yes, Submit & Grade')}</button>
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
        <h3 class="eg-h3">${L('الاختبار متوقف مؤقتاً', 'Exam Timer Paused')}</h3>
        <p class="eg-prose opacity-80 mb-4">${L('تم إخفاء الأسئلة لحفظ نزاهة التوقيت. اضغط استئناف للمتابعة.', 'Questions are hidden while the clock is paused. Click Resume to continue.')}</p>
        <button type="button" onclick="toggleKaustMockPause()" class="eg-btn eg-btn-main">${L('استئناف الاختبار', 'Resume Exam')}</button>
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
          : `<button type="button" onclick="requestSubmitKaustMock()" class="eg-btn eg-btn-go">${L('مراجعة وتسليم الورقة', 'Finish & Submit Paper')}</button>`;
      bodyCards = `${renderExamQuestionCard(session.questions[idx], idx, total)}
        <div class="eg-nav-footer no-print">${prevBtn}${nextBtn}</div>`;
    }

    const tp = p.tier_points || cfg.tierPoints || null;
    const ptsOk = p.points_correct ?? cfg.ptsCorrect;
    const scoreHint = tp
      ? L(`+${tp.Easy} / +${tp.Medium} / +${tp.Hard} نقاط · 0 خطأ (بدون خصم) · بدون آلة حاسبة`, `+${tp.Easy} / +${tp.Medium} / +${tp.Hard} pts · 0 Wrong (No Penalty) · No Calculator`)
      : wrongPts < 0
      ? L(`+${ptsOk} صحيح · −1 خطأ · 0 متروك · بدون آلة حاسبة`, `+${ptsOk} Correct · −1 Wrong · 0 Blank · No Calculator`)
      : L(`+${ptsOk} صحيح · 0 خطأ (بدون خصم) · بدون آلة حاسبة`, `+${ptsOk} Correct · 0 Wrong (No Penalty) · No Calculator`);

    return `
      <div class="eg-mock-topbar no-print">
        <div class="flex flex-wrap items-center gap-2">
          <button type="button" onclick="exitKaustMock(false)" class="eg-btn eg-btn-sm">${isAr() ? '→' : '←'} ${L('قائمة الاختبارات', 'Exit')}</button>
          <span class="font-bold text-sm">${pText.title}</span>
        </div>
        <div class="flex flex-wrap items-center gap-2">
          <div class="eg-clock-box">
            <span id="kmc-mock-clock" dir="ltr" class="eg-clock${clockWarn}${clockCrit}">${formatClock(session.remainingSec)}</span>
            <button type="button" onclick="toggleKaustMockPause()" class="eg-btn eg-btn-sm" title="${L('إيقاف مؤقت / استئناف', 'Pause / Resume')}">${session.paused ? L('استئناف', 'Resume') : L('إيقاف', 'Pause')}</button>
          </div>
          <span class="eg-lc-pill">${L('المجاب:', 'Answered:')} ${answeredCount}/${total} · ${L('متروك:', 'Blank:')} ${blankCount}${flagCount ? ` · ${L('معلّم:', 'Flagged:')} ${flagCount}` : ''}</span>
          <button type="button" onclick="setKaustMockViewMode('${session.viewMode === 'single' ? 'all' : 'single'}')" class="eg-btn eg-btn-sm">
            ${session.viewMode === 'single' ? L('عرض الورقة كاملة', 'Full Paper View') : L('سؤال بسؤال', 'Single Question')}
          </button>
          <button type="button" onclick="requestSubmitKaustMock()" class="eg-btn eg-btn-go">${L('تسليم وتصحيح الاختبار', 'Submit & Grade')}</button>
        </div>
      </div>
      ${confirmBanner}
      <div class="eg-pal-wrap no-print">
        <div class="eg-pal-label">${L('لوحة التنقل السريع (OMR):', 'Question & Bubble Navigator:')} <span class="opacity-75 font-normal">(${scoreHint})</span></div>
        <div class="eg-pal-grid" dir="ltr">${paletteBtns}</div>
      </div>
      <div class="eg-reader">${bodyCards}</div>`;
  }

  function renderReviewView() {
    const p = session.paper;
    const cfg = compForPaper(p);
    const pText = pick(p);
    const rep = session.report;
    const total = session.questions.length;

    let tierBadge = '';
    if (rep.pct >= 75) {
      tierBadge = `<span class="eg-badge" style="background:#dcfce7;color:#166534">${L('مستوى تأهل للمرحلة المتقدمة (ممتاز)', 'Final-Round Contender Pace')}</span>`;
    } else if (rep.pct >= 50) {
      tierBadge = `<span class="eg-badge" style="background:#fef3c7;color:#92400e">${L('أداء تنافسي قوي — واصل التدريب', 'Strong Competitive Qualifier Pace')}</span>`;
    } else {
      tierBadge = `<span class="eg-badge eg-badge-alt">${L('فرصة ممتازة لتقوية الأساسيات عبر الدروس المقترحة أدناه', 'Build Core Mastery with the Recommended Lessons Below')}</span>`;
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
      .map(([t, st]) => `<span class="eg-lc-pill"><strong>${topicLabel(t)}:</strong> ${st.correct}/${st.total}</span>`)
      .join(' ');

    const studyLessons = (window.__kaustStudy && (window.__kaustStudy.allLessons || window.__kaustStudy.lessons)) || [];
    const recBtns = rep.weakLessonIds
      .slice(0, 4)
      .map((lid) => {
        const les = studyLessons.find((x) => x.id === lid);
        if (!les) return '';
        const lTitle = isAr() ? les.ar.title : les.en.title;
        return `<button type="button" onclick="if(window.openKaustLesson){openKaustLesson('${les.id}');document.getElementById('study-lessons').scrollIntoView({behavior:'smooth'});}" class="eg-btn eg-btn-sm">${L('راجع درس', 'Review Lesson')} ${les.unit_num}: ${lTitle}</button>`;
      })
      .filter(Boolean)
      .join('');

    const filters = [
      ['all', `${L('الكل', 'All')} (${total})`],
      ['wrong', `${L('الخاطئة', 'Incorrect')} (${rep.wrong})`],
      ['blank', `${L('المتروكة', 'Blank')} (${rep.blank})`],
      ['correct', `${L('الصحيحة', 'Correct')} (${rep.correct})`],
      ['flagged', `${L('المعلّمة', 'Flagged')} (${Object.values(session.flags).filter(Boolean).length})`],
    ]
      .map(
        ([fKey, fLbl]) =>
          `<button type="button" onclick="setKaustMockReviewFilter('${fKey}')" class="eg-btn eg-btn-sm${session.reviewFilter === fKey ? ' eg-tab-on' : ''}">${fLbl}</button>`
      )
      .join('');

    const wrongPenaltyBadge = rep.ptsWrong < 0
      ? `✗ −1 ${L('نقطة (خاطئة)', 'pt (Incorrect)')}`
      : `✗ 0 ${L('نقاط (خاطئة)', 'pts (Incorrect)')}`;

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
        const qPts = qPointsFor(p, q, cfg);
        const statusTag = isOk
          ? `<span class="eg-ex-tag eg-diff-easy">✓ +${qPts} ${L(qPts === 1 ? 'نقطة (صحيحة)' : 'نقاط (صحيحة)', qPts === 1 ? 'pt (Correct)' : 'pts (Correct)')}</span>`
          : isWr
          ? `<span class="eg-ex-tag eg-diff-hard">${wrongPenaltyBadge}</span>`
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
            <div class="eg-sol-h">${L('الحل التفصيلي خطوة بخطوة — الإجابة الصحيحة:', 'Step-by-Step Solution — Correct Answer:')} (${LABELS[q.correct_index]})</div>
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
          <button type="button" onclick="startKaustMock('${p.id}')" class="eg-btn">${L('إعادة المحاولة', 'Retake Paper')}</button>
        </div>
        <div class="flex flex-wrap gap-2">
          <button type="button" onclick="printKaustMockPaper('${p.id}', 'key')" class="eg-btn eg-btn-main">${L('طباعة تقرير الدرجة والحلول (A4)', 'Print Graded Report & Solutions (A4)')}</button>
          <button type="button" onclick="printKaustMockPaper('${p.id}', 'full')" class="eg-btn">${L('طباعة الحزمة الكاملة (A4)', 'Print Full Exam Package (A4)')}</button>
        </div>
      </div>

      <div class="eg-banner">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
          <span class="font-extrabold text-sm">${pText.title}</span>
          ${tierBadge}
        </div>
        <div class="eg-score-hero">
          <div class="eg-score-main">
            <div class="text-xs uppercase font-extrabold opacity-75">${L(`الدرجة الرسمية (${cfg.badgeAr} · ${cfg.scoreTag})`, `Official ${cfg.badgeEn} Score (${cfg.scoreTag})`)}</div>
            <div class="text-3xl sm:text-4xl font-extrabold mt-0.5" dir="ltr">${rep.score} <span class="text-lg opacity-70">/ ${rep.maxPoints} pts (${rep.pct}%)</span></div>
          </div>
          <div class="flex flex-wrap gap-2">
            <span class="eg-lc-pill">✓ ${L('صحيح:', 'Correct:')} <strong>${rep.correct}</strong></span>
            <span class="eg-lc-pill">✗ ${L('خطأ:', 'Wrong:')} <strong>${rep.wrong}</strong></span>
            <span class="eg-lc-pill">○ ${L('متروك:', 'Blank:')} <strong>${rep.blank}</strong></span>
            <span class="eg-lc-pill">${L('الزمن:', 'Time:')} <strong dir="ltr">${formatClock(rep.elapsedSec)}</strong></span>
          </div>
        </div>
        <div class="eg-stat-grid mt-3">${tierCards}</div>
        <div class="flex flex-wrap gap-1.5 mt-3">${topicPills}</div>
        ${
          recBtns
            ? `<div class="mt-3 pt-3 border-t border-teal-500/25">
                <div class="text-xs font-extrabold mb-1.5">${L('دروس مقترحة للمراجعة السريعة بناءً على إجاباتك:', 'Recommended Study Lessons to Review Next:')}</div>
                <div class="flex flex-wrap gap-1.5">${recBtns}</div>
              </div>`
            : ''
        }
      </div>

      <div class="flex flex-wrap items-center justify-between gap-2 my-3 no-print">
        <div class="font-extrabold text-sm">${L('مراجعة الأسئلة والحلول التفصيلية:', 'Detailed Question-by-Question Review:')}</div>
        <div class="flex flex-wrap gap-1.5">${filters}</div>
      </div>
      <div class="eg-reader">${reviewCards || `<div class="eg-card text-center opacity-75">${L('لا توجد أسئلة ضمن هذا الفلتر.', 'No questions match this filter.')}</div>`}</div>`;
  }

  function renderHubView() {
    const cfg = COMP_CONFIG[activeComp];
    const activeTrack = activeTrackByComp[activeComp];
    const tr = cfg.tracks.find((t) => t.level === activeTrack) || cfg.tracks[0];
    const compPapers = currentCompPapers();
    const trackPapers = compPapers.filter((p) => p.level === activeTrack);
    const optRange = cfg.optCount === 4 ? 'A–D' : 'A–E';

    const compSwitcher = (nsmoMocks.length || kangarooMocks.length || nafesMocks.length || nafesScienceMocks.length || nafesEnglishMocks.length || olympiadMocks.length)
      ? `<div class="eg-comp-switch no-print" role="tablist" aria-label="Mock Exam Competition">
          ${nafesMocks.length ? `<button type="button" onclick="setMockCompetition('nafes')" class="eg-comp-btn${activeComp === 'nafes' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nafes.pillAr : COMP_CONFIG.nafes.pillEn}</button>` : ''}
          ${nafesScienceMocks.length ? `<button type="button" onclick="setMockCompetition('nafes_science')" class="eg-comp-btn${activeComp === 'nafes_science' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nafes_science.pillAr : COMP_CONFIG.nafes_science.pillEn}</button>` : ''}
          ${nafesEnglishMocks.length ? `<button type="button" onclick="setMockCompetition('nafes_english')" class="eg-comp-btn${activeComp === 'nafes_english' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nafes_english.pillAr : COMP_CONFIG.nafes_english.pillEn}</button>` : ''}
          ${kangarooMocks.length ? `<button type="button" onclick="setMockCompetition('kangaroo')" class="eg-comp-btn${activeComp === 'kangaroo' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.kangaroo.pillAr : COMP_CONFIG.kangaroo.pillEn}</button>` : ''}
          <button type="button" onclick="setMockCompetition('kaust')" class="eg-comp-btn${activeComp === 'kaust' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.kaust.pillAr : COMP_CONFIG.kaust.pillEn}</button>
          ${nsmoMocks.length ? `<button type="button" onclick="setMockCompetition('nsmo')" class="eg-comp-btn${activeComp === 'nsmo' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.nsmo.pillAr : COMP_CONFIG.nsmo.pillEn}</button>` : ''}
          ${olympiadMocks.length ? `<button type="button" onclick="setMockCompetition('olympiad')" class="eg-comp-btn${activeComp === 'olympiad' ? ' eg-comp-btn-on' : ''}">${isAr() ? COMP_CONFIG.olympiad.pillAr : COMP_CONFIG.olympiad.pillEn}</button>` : ''}
        </div>`
      : '';

    const tabs = cfg.tracks.map((t) => {
      const cnt = compPapers.filter((p) => p.level === t.level).length;
      const tDur = t.durationMin || cfg.durationMin;
      return `<button type="button" onclick="setKaustMockTrack('${t.level}')" class="eg-tab${t.level === activeTrack ? ' eg-tab-on' : ''}">
        <span>${isAr() ? t.ar : t.en}</span>
        <span class="eg-tab-count">${cnt} ${L('نماذج رسمية', 'Mock Papers')} · ${t.qCount} ${L('سؤالاً', 'Qs')} · ${tDur} ${L('دقيقة', 'min')}</span>
      </button>`;
    }).join('');

    const cards = trackPapers
      .map((p) => {
        const pText = pick(p);
        const best = bestScores[p.id];
        const dur = p.duration_minutes || cfg.durationMin;
        const topicTags = Object.entries(p.topic_counts || {})
          .map(([k, v]) => `${topicLabel(k)}: ${v}`)
          .join(' · ');

        return `<div class="eg-lesson-card eg-mock-card">
          <div>
            <div class="flex flex-wrap items-center justify-between gap-1.5 mb-2">
              <div class="flex flex-wrap items-center gap-1.5">
                <span class="eg-badge">${p.is_custom ? L('نموذج مخصص', 'Custom') : L('نموذج رسمي', 'Mock Paper') + ' #' + p.paper_num}</span>
                <span class="eg-badge eg-badge-alt">${p.question_count} ${L('سؤالاً', 'Qs')} (${optRange}) · ${dur} ${L('د', 'min')}</span>
              </div>
              <span class="eg-lc-pill">${best ? `${best.score}/${best.maxPoints}` : `${p.svg_count} ${L('رسمة', 'SVGs')} · ${p.max_points} ${L('نقطة', 'pts')}`}</span>
            </div>
            <h3 class="eg-lc-title" onclick="startKaustMock('${p.id}')">${pText.title}</h3>
            <p class="eg-lc-desc">${pText.focus || pText.subtitle || ''}</p>
            <div class="text-xs opacity-75 mt-2">${topicTags}</div>
          </div>
          <div class="eg-mock-actions">
            <button type="button" onclick="startKaustMock('${p.id}')" class="eg-btn eg-btn-go eg-btn-sm w-full">
              ${L(`ابدأ الاختبار الموقوت (${dur} دقيقة)`, `Start Live Timed Exam (${dur} min)`)}
            </button>
            <div class="flex flex-wrap gap-1.5 w-full">
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'full')" class="eg-btn eg-btn-main eg-btn-sm flex-1" title="${L('طباعة الغلاف + ورقة التظليل OMR + الأسئلة + المفتاح والحلول', 'Print Cover + OMR Bubble Sheet + Exam + Worked Key')}">
                ${L('حزمة كاملة A4', 'Full Pack A4')}
              </button>
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'student')" class="eg-btn eg-btn-sm" title="${L('طباعة ورقة الطالب والتظليل فقط بدون الإجابات', 'Student Exam + OMR Bubble Sheet Only (No Answers)')}">
                ${L('ورقة الطالب', 'Exam + OMR')}
              </button>
              <button type="button" onclick="printKaustMockPaper('${p.id}', 'key')" class="eg-btn eg-btn-sm" title="${L('طباعة مفتاح التصحيح المظلل والحلول فقط', 'Pre-Shaded OMR Master Key & Worked Solutions Only')}">
                ${L('المفتاح', 'Key')}
              </button>
            </div>
          </div>
        </div>`;
      })
      .join('');

    const maxDivPts = tr.tiers.Easy * 3 + tr.tiers.Medium * 4 + tr.tiers.Hard * 5;
    const trDur = tr.durationMin || cfg.durationMin;
    const subText = (cfg.id === 'nafes' || cfg.id === 'nafes_science' || cfg.id === 'nafes_english')
      ? L(
          `نظام اختبارات نافس الوطنية الرسمي (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤال اختيار من متعدد (${optRange})</strong> في <strong>${trDur} دقيقة</strong> بدون آلة حاسبة · <strong>+1 نقطة</strong> لكل إجابة صحيحة (${tr.qCount} نقطة عظمى) و<strong>بدون خصم (0)</strong> للخاطئة أو المتروكة.`,
          `Official ETEC Nafes Assessment Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (${optRange})</strong> in <strong>${trDur} minutes</strong>, No Calculator · <strong>+1 pt</strong> per correct answer (${tr.qCount} max pts) and <strong>0</strong> penalty for wrong/blank.`
        )
      : cfg.id === 'kangaroo'
      ? L(
          `نظام كانجارو موهبة الرسمي (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤال اختيار من متعدد (${optRange})</strong> في <strong>${cfg.durationMin} دقيقة</strong> بدون آلة حاسبة · <strong>3 / 4 / 5 نقاط</strong> حسب الجزء (${maxDivPts} نقطة عظمى) و<strong>بدون خصم (0)</strong> للخاطئة أو المتروكة.`,
          `Official Mawhiba Kangaroo Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (${optRange})</strong> in <strong>${cfg.durationMin} minutes</strong>, No Calculator · <strong>+3 / +4 / +5 pts</strong> across Parts A, B, C (${maxDivPts} max pts) and <strong>0</strong> penalty for wrong/blank.`
        )
      : cfg.id === 'olympiad'
      ? L(
          `نظام التصفيات الأولمبية للرياضيات (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤال اختيار من متعدد (${optRange})</strong> في <strong>${cfg.durationMin} دقيقة</strong> بدون آلة حاسبة · <strong>+6 نقاط</strong> لكل إجابة صحيحة (150 نقطة عظمى) و<strong>بدون خصم (0)</strong> للخاطئة أو المتروكة.`,
          `Official Olympiad Screening Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (${optRange})</strong> in <strong>${cfg.durationMin} minutes</strong>, No Calculator · <strong>+6 pts</strong> Correct (150 max pts), <strong>0</strong> Wrong (No Penalty), <strong>0</strong> Blank.`
        )
      : cfg.id === 'nsmo'
      ? L(
          `نظام أولمبياد نسمو — موهبة (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤال اختيار من متعدد (${optRange})</strong> في <strong>${cfg.durationMin} دقيقة</strong> بدون آلة حاسبة · <strong>+4</strong> للصحيحة و<strong>بدون خصم (0)</strong> للخاطئة أو المتروكة.`,
          `Official NSMO / Mawhiba Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (${optRange})</strong> in <strong>${cfg.durationMin} minutes</strong>, No Calculator · <strong>+4</strong> Correct, <strong>0</strong> Wrong (No Penalty), <strong>0</strong> Blank.`
        )
      : L(
          `نظام التصفيات الرسمي لمسابقة كاوست (${isAr() ? tr.shortAr : tr.shortEn}): <strong>${tr.qCount} سؤالاً (${optRange})</strong> في <strong>${cfg.durationMin} دقيقة</strong> بدون آلة حاسبة · <strong>+4</strong> للإجابة الصحيحة، <strong>−1</strong> للخاطئة، <strong>0</strong> للمتروك.`,
          `Official KMC Elimination Format (${tr.shortEn}): <strong>${tr.qCount} MCQs (${optRange})</strong> in <strong>${cfg.durationMin} minutes</strong>, No Calculator · <strong>+4</strong> Correct, <strong>−1</strong> Wrong, <strong>0</strong> Blank.`
        );

    return `
      ${compSwitcher}
      <div class="eg-tabs no-print">${tabs}</div>
      <div class="eg-subbar no-print">
        <div class="text-xs sm:text-sm opacity-90">${subText}</div>
        <div class="flex flex-wrap gap-2 max-w-full">
          <button type="button" onclick="generateCustomKaustMock('${activeTrack}')" class="eg-btn eg-btn-go">
            ${L('توليد نموذج تجريبي جديد', 'Generate Fresh Mock')}
          </button>
          <button type="button" onclick="printBlankKaustOmr('${activeTrack}')" class="eg-btn eg-btn-main">
            ${L('طباعة ورقة تظليل OMR فارغة (A4)', 'Print Blank OMR Sheet (A4)')}
          </button>
        </div>
      </div>
      <div class="eg-grid">${cards}</div>`;
  }

  function render() {
    const root = document.getElementById('kaust-mock-exams');
    const compPapers = currentCompPapers();
    if (!root || !compPapers.length) return;
    root.setAttribute('dir', isAr() ? 'rtl' : 'ltr');

    const cfg = session ? compForPaper(session.paper) : COMP_CONFIG[activeComp];
    const basePapers =
      cfg.id === 'olympiad'
        ? olympiadMocks
        : cfg.id === 'nafes_science'
        ? nafesScienceMocks
        : cfg.id === 'nafes_english'
        ? nafesEnglishMocks
        : cfg.id === 'nafes'
        ? nafesMocks
        : cfg.id === 'kangaroo'
        ? kangarooMocks
        : cfg.id === 'nsmo'
        ? nsmoMocks
        : kaustMocks;
    const totalPapers = (
      cfg.id === 'olympiad'
        ? allOlympiadPapers()
        : cfg.id === 'nafes_science'
        ? allNafesSciencePapers()
        : cfg.id === 'nafes_english'
        ? allNafesEnglishPapers()
        : cfg.id === 'nafes'
        ? allNafesPapers()
        : cfg.id === 'kangaroo'
        ? allKangarooPapers()
        : cfg.id === 'nsmo'
        ? allNsmoPapers()
        : allKaustPapers()
    ).length;
    const totalUniqueQs = basePapers.reduce((acc, p) => acc + (p.question_count || 0), 0);
    const durTag = cfg.durationRangeLabel || cfg.durationMin;

    const inner = !session
      ? renderHubView()
      : session.mode === 'exam'
      ? renderExamView()
      : renderReviewView();

    root.innerHTML = `<div class="eg-hub eg-mock-hub${session ? ' eg-hub-active-exam' : ''}">
      <div class="eg-hub-h">
        <div class="eg-hub-logo-box hidden sm:block"><img src="LOGO.jpg" alt="Edugates International School" loading="eager" decoding="sync" class="eg-hub-logo"></div>
        <div class="flex-1 min-w-0">
          <h2 class="text-xl sm:text-2xl font-display font-bold">${isAr() ? cfg.hubTitleAr : cfg.hubTitleEn}</h2>
          <p class="text-xs sm:text-sm opacity-80 mt-0.5">${L(
            `Edugates International School · ${totalPapers} نموذج اختبار رسمي (${totalUniqueQs} سؤالاً) · مؤقت حي ${durTag} دقيقة · أوراق تظليل OMR وطباعة A4`,
            `Edugates International School · ${totalPapers} Official Simulation Papers (${totalUniqueQs} questions) · ${durTag}-Min Timed Simulator · Printable A4 & OMR Sheets`
          )}</p>
        </div>
      </div>
      ${inner}
    </div>`;

    if (root.querySelectorAll) {
      root.querySelectorAll('.eg-comp-btn-on, .eg-tab-on, .eg-pal-cur').forEach((btn) => {
        const p = btn.parentElement;
        if (p && p.scrollWidth > p.clientWidth) {
          p.scrollLeft = Math.max(0, btn.offsetLeft - (p.clientWidth - btn.offsetWidth) / 2);
        }
      });
    }

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

    const [kRes, nRes, gRes, fRes, fsRes, feRes, oRes] = await Promise.allSettled([
      fetch('data/kaust_mocks.json'),
      fetch('data/nsmo_mocks.json'),
      fetch('data/kangaroo_mocks.json'),
      fetch('data/nafes_mocks.json'),
      fetch('data/nafes_science_mocks.json'),
      fetch('data/nafes_english_mocks.json'),
      fetch('data/olympiad_mocks.json'),
    ]);
    if (kRes.status === 'fulfilled' && kRes.value && kRes.value.ok) {
      try {
        kaustDoc = await kRes.value.json();
        kaustMocks = (kaustDoc && kaustDoc.mocks) || [];
      } catch (_) {}
    }
    if (nRes.status === 'fulfilled' && nRes.value && nRes.value.ok) {
      try {
        nsmoDoc = await nRes.value.json();
        nsmoMocks = (nsmoDoc && nsmoDoc.mocks) || [];
      } catch (_) {}
    }
    if (gRes.status === 'fulfilled' && gRes.value && gRes.value.ok) {
      try {
        kangarooDoc = await gRes.value.json();
        kangarooMocks = (kangarooDoc && kangarooDoc.mocks) || [];
      } catch (_) {}
    }
    if (fRes.status === 'fulfilled' && fRes.value && fRes.value.ok) {
      try {
        nafesDoc = await fRes.value.json();
        nafesMocks = (nafesDoc && nafesDoc.mocks) || [];
      } catch (_) {}
    }
    if (fsRes.status === 'fulfilled' && fsRes.value && fsRes.value.ok) {
      try {
        nafesScienceDoc = await fsRes.value.json();
        nafesScienceMocks = (nafesScienceDoc && nafesScienceDoc.mocks) || [];
      } catch (_) {}
    }
    if (feRes.status === 'fulfilled' && feRes.value && feRes.value.ok) {
      try {
        nafesEnglishDoc = await feRes.value.json();
        nafesEnglishMocks = (nafesEnglishDoc && nafesEnglishDoc.mocks) || [];
      } catch (_) {}
    }
    if (oRes.status === 'fulfilled' && oRes.value && oRes.value.ok) {
      try {
        olympiadDoc = await oRes.value.json();
        olympiadMocks = (olympiadDoc && olympiadDoc.mocks) || [];
      } catch (_) {}
    }
    if (!kaustMocks.length && !nsmoMocks.length && !kangarooMocks.length && !nafesMocks.length && !nafesScienceMocks.length && !nafesEnglishMocks.length && !olympiadMocks.length) return;

    const t0 = Date.now();
    while (!getBankQuestions().length && Date.now() - t0 < 15000) {
      await new Promise((r) => setTimeout(r, 80));
    }

    render();

    if (typeof window !== 'undefined' && window.location && window.location.search) {
      const mid = new URLSearchParams(window.location.search).get('mock');
      if (mid) window.startKaustMock(mid);
    }

    if (typeof window.toggleLanguage === 'function' && !window.__kaustMockLangHooked) {
      window.__kaustMockLangHooked = true;
      const origToggle = window.toggleLanguage;
      window.toggleLanguage = function () {
        const res = origToggle.apply(this, arguments);
        const navTxt = document.getElementById('nav-mocks-text');
        if (navTxt) navTxt.innerText = isAr() ? 'الاختبارات' : 'Mock Exams';
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
          if (activeComp === 'nafes') {
            if (g === 3) { activeTrackByComp.nafes = 'Grade 3'; render(); }
            else if (g === 6) { activeTrackByComp.nafes = 'Grade 6'; render(); }
            else if (g === 9) { activeTrackByComp.nafes = 'Grade 9'; render(); }
          } else if (activeComp === 'nafes_science') {
            if (g === 6) { activeTrackByComp.nafes_science = 'Science · Grade 6'; render(); }
            else if (g === 9) { activeTrackByComp.nafes_science = 'Science · Grade 9'; render(); }
          } else if (activeComp === 'nafes_english') {
            if (g === 3) { activeTrackByComp.nafes_english = 'English · Grade 3'; render(); }
            else if (g === 6) { activeTrackByComp.nafes_english = 'English · Grade 6'; render(); }
            else if (g === 9) { activeTrackByComp.nafes_english = 'English · Grade 9'; render(); }
          } else if (activeComp === 'kangaroo') {
            if (g === 1 || g === 2) { activeTrackByComp.kangaroo = 'PreEcolier'; render(); }
            else if (g === 3 || g === 4) { activeTrackByComp.kangaroo = 'Ecolier'; render(); }
            else if (g === 5 || g === 6) { activeTrackByComp.kangaroo = 'Benjamin'; render(); }
            else if (g === 7 || g === 8) { activeTrackByComp.kangaroo = 'Cadet'; render(); }
            else if (g === 9 || g === 10) { activeTrackByComp.kangaroo = 'Junior'; render(); }
            else if (g === 11 || g === 12) { activeTrackByComp.kangaroo = 'Student'; render(); }
          } else if (activeComp === 'olympiad') {
            if (g === 7 || g === 8) { activeTrackByComp.olympiad = COMP_CONFIG.olympiad.tracks[0].level; render(); }
            else if (g === 9 || g === 10) { activeTrackByComp.olympiad = COMP_CONFIG.olympiad.tracks[1].level; render(); }
            else if (g === 11 || g === 12) { activeTrackByComp.olympiad = COMP_CONFIG.olympiad.tracks[2].level; render(); }
          } else if (activeComp === 'nsmo') {
            if (g === 7) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[0].level; render(); }
            else if (g === 8 || g === 9) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[1].level; render(); }
            else if (g === 10) { activeTrackByComp.nsmo = COMP_CONFIG.nsmo.tracks[2].level; render(); }
          } else {
            if (g === 6 || g === 7) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[0].level; render(); }
            else if (g === 8 || g === 9) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[1].level; render(); }
            else if (g === 10 || g === 11) { activeTrackByComp.kaust = COMP_CONFIG.kaust.tracks[2].level; render(); }
          }
        }
        return res;
      };
    }

    window.__kaustMocks = {
      get mocks() {
        return allKaustPapers();
      },
      get nsmoMocks() {
        return allNsmoPapers();
      },
      get kangarooMocks() {
        return allKangarooPapers();
      },
      get nafesMocks() {
        return allNafesPapers();
      },
      get nafesScienceMocks() {
        return allNafesSciencePapers();
      },
      get nafesEnglishMocks() {
        return allNafesEnglishPapers();
      },
      get olympiadMocks() {
        return allOlympiadPapers();
      },
      get allMocks() {
        return allPapersAcrossComps();
      },
      get activeComp() {
        return activeComp;
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
