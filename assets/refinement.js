/* Extend the original bilingual static application without changing its hosting. */
Object.assign(dict.en, {
 printTitle:'SuperMath · Practice sheet',printBtnText:'Print Worksheet',appTitle:'SuperMath',appSubtitle:'Edugates International School',
 badgeOverview:'STEM & LANGUAGE PRACTICE · KSA & OLYMPIAD PREP',heroHeading:'Structured preparation across eight national and olympiad tracks.',
 heroDesc:'Select your grade or competition below to practice problems with full solutions, study illustrated lessons, or sit a timed mock paper.',
 sec1Title:'Competitions & Grade Tracks',sec1Desc:'Filter by grade or open Practice, Lessons, or Mock Exams directly.',
 lblFilterGrade:'Filter by Grade (1–12)',
 quizHeading:'Practice Workspace',quizSubheading:'Filter by competition, division, and topic, then work through each problem at your own pace.',
 chart1Title:'Questions by Curriculum Domain',chart1Caption:'Question counts across Math, Science, and English topics in the eight active banks.',
 chart2Title:'Response Formats by Competition',chart2Caption:'Proportion of multiple-choice versus written-response items per bank.',
 sec2Title:'Bank Overview & Curriculum Balance',sec2Desc:'Topic distribution and format breakdown across all 10,220 questions.',
 scaleTitle:'Practice-bank planning',scaleDesc:'An estimate for planning future additions; this is not a count of available questions.',
 stat1Label:'Competitions',stat1Value:'8 Tracks',stat4Label:'Languages',stat4Value:'EN & AR',stat2Label:'Grade Span',stat2Value:'Grades 1–12',
 btnHint:'Show Hint',btnSubmit:'Check Answer',txtCorrect:'Correct — well reasoned.',txtIncorrect:'Not quite — review the worked solution below.',
 btnPrevQ:'← Previous',btnNextQ:'Next →',
 footerText:'© 2026 SuperMath · Edugates International School. Independent practice materials; no exam-board endorsement.'
});
Object.assign(dict.ar, {
 printTitle:'SuperMath · ورقة تدريب',printBtnText:'طباعة ورقة عمل',appTitle:'سوبر ماث',appSubtitle:'مدرسة بوابة المعرفة العالمية',
 badgeOverview:'التدريب العلمي واللغوي والإعداد للمسابقات',heroHeading:'إعداد منظم لثمانية مسارات وطنية وأولمبياد معتمدة.',
 heroDesc:'اختر صفك الدراسي أو المسابقة أدناه لحل المسائل مع الشرح التفصيلي، أو دراسة الدروس المصوّرة، أو خوض اختبار تجريبي موقوت.',
 sec1Title:'المسابقات والمسارات الدراسية',sec1Desc:'صفِّ حسب الصف الدراسي أو افتح التدريب أو الدروس أو الاختبارات مباشرة.',
 lblFilterGrade:'تصفية حسب الصف الدراسي (1–12)',
 quizHeading:'مساحة التدريب وحل المسائل',quizSubheading:'اختر المسابقة والمستوى والموضوع وتدرّب بالسرعة التي تناسبك.',
 sec2Title:'نظرة عامة على البنوك وتوزيع المواضيع',sec2Desc:'توزيع الأسئلة حسب المجالات العلمية والرياضية واللغوية عبر 10,220 سؤالاً.',
 chart1Title:'توزيع الأسئلة حسب المجال الدراسي',chart1Caption:'أعداد الأسئلة في الرياضيات والعلوم والإنجليزية عبر المسارات الثمانية.',
 chart2Title:'أنماط الأسئلة حسب المسار',chart2Caption:'نسبة الاختيار من متعدد مقابل الإجابات المفتوحة في كل بنك.',
 scaleTitle:'تخطيط بنك التدريب',scaleDesc:'تقدير للتوسعات المستقبلية، وليس عدد الأسئلة المتاحة.',
 stat1Label:'المسابقات',stat1Value:'8 مسارات',stat4Label:'اللغات',stat4Value:'عربي & EN',stat2Label:'الصفوف',stat2Value:'الصفوف 1–12',
 btnHint:'إظهار التلميح',btnSubmit:'تحقق من الإجابة',txtCorrect:'إجابة صحيحة — أحسنت الاستنتاج.',txtIncorrect:'إجابة غير صحيحة — راجع خطوات الحل أدناه.',
 btnPrevQ:'→ السابق',btnNextQ:'التالي ←',
 footerText:'© 2026 SuperMath · مدرسة بوابة المعرفة العالمية. مواد تدريب مستقلة غير معتمدة من جهات الاختبارات.'
});
const trackUpdates = {
 kangaroo:{name_en:'Kangaroo Math (Mawhiba)',name_ar:'كانجارو موهبة للرياضيات',format_en:'5-option MCQs (A–E) · 3, 4, 5 pts · No calculator · Grades 1–12',format_ar:'اختيار من متعدد (5 خيارات) · 3 و4 و5 نقاط · بدون آلة حاسبة · الصفوف 1–12',levels_en:'Grades 1–12 · PreEcolier to Student',levels_ar:'مستويات كانجارو: الصفوف 1–12 (بري إيكولير–ستيودنت)',badge_en:'MCQs (5 Options)',badge_ar:'MCQs (5 خيارات)',grades:[1,2,3,4,5,6,7,8,9,10,11,12]},
 nafes:{name_en:'Nafes Math · KSA National Exam (ETEC)',name_ar:'اختبار نافس الوطني · الرياضيات (ETEC)',format_en:'4-option MCQs (A–D) · No calculator · Grades 3, 6 & 9',format_ar:'اختيار من متعدد (4 خيارات) · بدون آلة حاسبة · الصفوف 3 و6 و9',levels_en:'Grades 3, 6 & 9 · ETEC Math Benchmarks',levels_ar:'الصفوف المستهدفة رسمياً: 3 و6 و9',badge_en:'MCQs (4 Options)',badge_ar:'MCQs (4 خيارات)',grades:[3,6,9]},
 nafes_science:{name_en:'Nafes Science · KSA National Exam (ETEC)',name_ar:'اختبار نافس الوطني · العلوم (ETEC)',format_en:'4-option MCQs (A–D) · No calculator · Grades 6 & 9 only',format_ar:'اختيار من متعدد (4 خيارات) · بدون آلة حاسبة · الصفان 6 و9 فقط',levels_en:'Grades 6 & 9 · ETEC Science Benchmarks',levels_ar:'الصفان المستهدفان رسمياً: 6 و9 (لا يُعقد للصف 3)',badge_en:'MCQs (4 Options)',badge_ar:'MCQs (4 خيارات)',grades:[6,9]},
 nafes_english:{name_en:'Nafes English · KSA National Exam (ETEC)',name_ar:'اختبار نافس الوطني · الإنجليزية (ETEC)',format_en:'4-option MCQs (A–D) · CEFR A1/A2/B1 · Grades 3, 6 & 9',format_ar:'اختيار من متعدد (4 خيارات) · قراءة ومفردات ونحو · الصفوف 3 و6 و9',levels_en:'Grades 3, 6 & 9 · ETEC English Benchmarks',levels_ar:'الصفوف المستهدفة رسمياً: 3 و6 و9',badge_en:'MCQs (4 Options)',badge_ar:'MCQs (4 خيارات)',grades:[3,6,9]},
 kaust:{name_en:'KAUST · Math Competition (KMC)',name_ar:'كاوست · مسابقة الرياضيات (KMC)',format_en:'5-option MCQs (A–E) · No calculator · Grades 6–11',format_ar:'اختيار من متعدد (5 خيارات) · بدون آلة حاسبة · الصفوف 6–11',levels_en:'Grades 6–11 · 3 Competition Tracks',levels_ar:'مسارات KMC: الصفوف 6–11',badge_en:'MCQs (5 Options)',badge_ar:'MCQs (5 خيارات)',grades:[6,7,8,9,10,11]},
 nsmo:{name_en:'NSMO · Mawhiba Olympiad',name_ar:'نسمو · الأولمبياد الوطني (موهبة)',format_en:'4-option MCQs (A–D) · No calculator · Grades 7–10',format_ar:'اختيار من متعدد (4 خيارات) · بدون آلة حاسبة · الصفوف 7–10',levels_en:'Grades 7–10 · 3 National Phases',levels_ar:'نطاق الأولمبياد: الصفوف 7–10',badge_en:'MCQs (4 Options)',badge_ar:'MCQs (4 خيارات)',grades:[7,8,9,10]},
 olympiad:{name_en:'Math Olympiad (IMO / BMO / AMC)',name_ar:'الأولمبياد الرياضي (IMO / BMO / AMC)',format_en:'5-option MCQs (A–E) · 90 min · No calculator · Grades 7–12',format_ar:'اختيار من متعدد (5 خيارات) · 90 دقيقة · بدون آلة حاسبة · الصفوف 7–12',levels_en:'Grades 7–12 · 3 Olympiad Tiers',levels_ar:'مستويات الأولمبياد: الصفوف 7–12 (الناشئين · المتوسط · المتقدم)',badge_en:'MCQs (5 Options)',badge_ar:'MCQs (5 خيارات)',grades:[7,8,9,10,11,12]},
 jee:{name_en:'JEE · Mathematics',name_ar:'JEE · الرياضيات',format_en:'Mixed mathematics practice; not a full Main/Advanced mock',format_ar:'تدريب رياضيات متنوع؛ ليس محاكاة كاملة لـ Main أو Advanced'}
};
appData.tracks.forEach(t=>Object.assign(t,trackUpdates[t.id]||{}));
function chooseTrack(id){
 const track=appData.tracks.find(t=>t.id===id);
 if(!track || (currentSelectedGrade!=='all'&&!track.grades.includes(currentSelectedGrade)))return;
 if(id==='nafes'||id==='nafes_science'||id==='nafes_english'||id==='kangaroo'||id==='kaust'||id==='nsmo'||id==='olympiad'){window.setStudyCompetition?.(id);window.setMockCompetition?.(id);}
 document.getElementById('quiz-track-select').value=id;filterQuestions();
 if(typeof window.setAppView==='function')window.setAppView('practice',true);
 document.getElementById('practice').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
 document.getElementById('quiz-track-select').focus({preventScroll:true});
}
const SHORT_TRACK_NAMES = {
 en:{kangaroo:'Kangaroo',nafes:'Nafes Math',nafes_science:'Nafes Sci',nafes_english:'Nafes Eng',nsmo:'NSMO',kaust:'KAUST',olympiad:'Olympiad',jee:'JEE'},
 ar:{kangaroo:'كانجارو',nafes:'نافس رياضيات',nafes_science:'نافس علوم',nafes_english:'نافس إنجليزي',nsmo:'نسمو',kaust:'كاوست',olympiad:'الأولمبياد',jee:'JEE'}
};
function renderCharts(){
 if(!topicRadarChartInstance||!formatBarChartInstance)return;
 const isAr=currentLang==='ar';
 const isDark=document.documentElement.classList.contains('dark');
 const lblCol=isDark?'#cbd5e1':'#334155';
 const gridCol=isDark?'#283548':'#e2e8f0';
 const names=appData.tracks.map(t=>(SHORT_TRACK_NAMES[isAr?'ar':'en'][t.id])||(isAr?t.name_ar:t.name_en));
 const categories=[
  /algebra|function|equation|polynomial|complex|matri|sequence|inequal/i,
  /geometr|area|angle|circle|triangle|volume|spatial|perimeter/i,
  /number|divisib|integer|parity|arithmet|fraction|ratio|percent|decimal|operation|place value/i,
  /combin|logic|count|pattern|graph theory|calculus|integr|deriv|limit|differential|statistic|data|probab/i,
  /life sci|chemistry|matter|physics|force|energy|earth|space/i,
  /reading|text analysis|purpose|vocabulary|context|grammar|sentence/i
 ];
 topicRadarChartInstance.data.labels=isAr
  ?['الجبر','الهندسة','الأعداد','التركيبات والبيانات','العلوم','الإنجليزية']
  :['Algebra','Geometry','Numbers','Combin. & Data','Science','English'];
 const colors=['#e11d48','#2563eb','#0891b2','#7e22ce','#059669','#0d9488','#d97706','#4f46e5'];
 topicRadarChartInstance.data.datasets=appData.tracks.map((t,i)=>({label:names[i],data:categories.map(r=>appData.questions.filter(q=>q.track===t.id&&r.test(q.topic)).length),borderColor:colors[i%colors.length],backgroundColor:colors[i%colors.length]+'18',borderWidth:2,pointRadius:2.5}));
 if(topicRadarChartInstance.options?.scales?.r){
  topicRadarChartInstance.options.scales.r.angleLines={color:gridCol};
  topicRadarChartInstance.options.scales.r.grid={color:gridCol};
  if(topicRadarChartInstance.options.scales.r.pointLabels)topicRadarChartInstance.options.scales.r.pointLabels.color=lblCol;
 }
 if(topicRadarChartInstance.options?.plugins?.legend?.labels)topicRadarChartInstance.options.plugins.legend.labels.color=lblCol;
 formatBarChartInstance.data.labels=names;
 formatBarChartInstance.data.datasets=[{label:isAr?'اختيار من متعدد':'Multiple Choice',backgroundColor:'#2563eb',borderRadius:4,barThickness:16,data:appData.tracks.map(t=>{const c=PracticeCore.formatCounts(appData.questions,t.id);return c.total?Math.round(100*c.mcq/c.total):0})},{label:isAr?'إجابة مكتوبة':'Written Response',backgroundColor:'#d97706',borderRadius:4,barThickness:16,data:appData.tracks.map(t=>{const c=PracticeCore.formatCounts(appData.questions,t.id);return c.total?Math.round(100*c.written/c.total):0})}];
 if(formatBarChartInstance.options?.scales?.x){formatBarChartInstance.options.scales.x.grid={color:gridCol};if(formatBarChartInstance.options.scales.x.ticks)formatBarChartInstance.options.scales.x.ticks.color=lblCol;}
 if(formatBarChartInstance.options?.scales?.y?.ticks)formatBarChartInstance.options.scales.y.ticks.color=lblCol;
 if(formatBarChartInstance.options?.plugins?.legend?.labels)formatBarChartInstance.options.plugins.legend.labels.color=lblCol;
 topicRadarChartInstance.update();formatBarChartInstance.update();
}
const kmcLevelLabelsEn = {
 'Grade 3': 'Grade 3 (Primary)',
 'Grade 6': 'Grade 6 (Primary)',
 'Grade 9': 'Grade 9 (Intermediate)',
 'Science · Grade 6': 'Science · Grade 6 (Primary)',
 'Science · Grade 9': 'Science · Grade 9 (Intermediate)',
 'English · Grade 3': 'English · Grade 3 (CEFR A1)',
 'English · Grade 6': 'English · Grade 6 (CEFR A2)',
 'English · Grade 9': 'English · Grade 9 (CEFR B1)',
 'PreEcolier': 'PreEcolier (Grades 1–2)',
 'Ecolier': 'Ecolier (Grades 3–4)',
 'Benjamin': 'Benjamin (Grades 5–6)',
 'Cadet': 'Cadet (Grades 7–8)',
 'Junior': 'Junior (Grades 9–10)',
 'Student': 'Student (Grades 11–12)',
 'Track 1: Grades 6-7': 'Track 1: Grades 6–7',
 'Track 2: Grades 8-9': 'Track 2: Grades 8–9',
 'Track 3: Grades 10-11': 'Track 3: Grades 10–11',
 'Phase 1: Junior Olympiad (Grade 7)': 'Phase 1: Grade 7 (Junior)',
 'Phase 2: Intermediate Olympiad (Grades 8-9)': 'Phase 2: Grades 8–9 (Intermediate)',
 'Phase 3: Senior National Olympiad (Grade 10)': 'Phase 3: Grade 10 (Senior)',
 'Tier 1: Junior Olympiad (Grades 7-8)': 'Tier 1: Grades 7–8 (Junior)',
 'Tier 2: Intermediate Olympiad (Grades 9-10)': 'Tier 2: Grades 9–10 (Intermediate)',
 'Tier 3: Senior Olympiad (Grades 11-12)': 'Tier 3: Grades 11–12 (Senior)'
};
const kmcLevelLabelsAr = {
 'Grade 3': 'الصف الثالث الابتدائي (رياضيات 3)',
 'Grade 6': 'الصف السادس الابتدائي (رياضيات 6)',
 'Grade 9': 'الصف الثالث المتوسط (رياضيات 9)',
 'Science · Grade 6': 'نافس العلوم · الصف السادس (ETEC)',
 'Science · Grade 9': 'نافس العلوم · الصف الثالث المتوسط (ETEC)',
 'English · Grade 3': 'نافس الإنجليزية · الصف الثالث (A1)',
 'English · Grade 6': 'نافس الإنجليزية · الصف السادس (A2)',
 'English · Grade 9': 'نافس الإنجليزية · الصف الثالث المتوسط (B1)',
 'PreEcolier': 'بري إيكولير (الصفان 1–2)',
 'Ecolier': 'إيكولير (الصفان 3–4)',
 'Benjamin': 'بنجامين (الصفان 5–6)',
 'Cadet': 'كاديت (الصفان 7–8)',
 'Junior': 'جونيور (الصفان 9–10)',
 'Student': 'ستيودنت (الصفان 11–12)',
 'Track 1: Grades 6-7': 'المسار 1: الصفان 6–7',
 'Track 2: Grades 8-9': 'المسار 2: الصفان 8–9',
 'Track 3: Grades 10-11': 'المسار 3: الصفوف 10–11',
 'Phase 1: Junior Olympiad (Grade 7)': 'المرحلة 1: الصف 7 (الناشئين)',
 'Phase 2: Intermediate Olympiad (Grades 8-9)': 'المرحلة 2: الصفان 8–9 (المتوسط)',
 'Phase 3: Senior National Olympiad (Grade 10)': 'المرحلة 3: الصف 10 (المتقدم)',
 'Tier 1: Junior Olympiad (Grades 7-8)': 'المستوى 1: الصفان 7–8 (الناشئين)',
 'Tier 2: Intermediate Olympiad (Grades 9-10)': 'المستوى 2: الصفان 9–10 (المتوسط)',
 'Tier 3: Senior Olympiad (Grades 11-12)': 'المستوى 3: الصفان 11–12 (المتقدم)'
};
const TRACK_SELECT_LABELS = {
 en: {all:'All Competitions',kangaroo:'Kangaroo Math (Grades 1–12)',nafes:'Nafes Math · KSA (Grades 3, 6, 9)',nafes_science:'Nafes Science · KSA (Grades 6, 9)',nafes_english:'Nafes English · KSA (Grades 3, 6, 9)',kaust:'KAUST KMC (Grades 6–11)',nsmo:'NSMO · Mawhiba (Grades 7–10)',olympiad:'Math Olympiad (Grades 7–12)',jee:'JEE Mathematics (Grade 12)'},
 ar: {all:'جميع المسابقات',kangaroo:'كانجارو الرياضيات (الصفوف 1–12)',nafes:'نافس الرياضيات · السعودية (3، 6، 9)',nafes_science:'نافس العلوم · السعودية (6، 9)',nafes_english:'نافس الإنجليزية · السعودية (3، 6، 9)',kaust:'مسابقة كاوست KMC (الصفوف 6–11)',nsmo:'أولمبياد نسمو موهبة (الصفوف 7–10)',olympiad:'الأولمبياد الرياضي (الصفوف 7–12)',jee:'رياضيات JEE (الصف 12)'}
};
function localizePracticeSelects(){
 const isAr=currentLang==='ar';
 const trSel=document.getElementById('quiz-track-select');
 if(trSel&&trSel.options){for(const o of trSel.options){const lbl=TRACK_SELECT_LABELS[isAr?'ar':'en'][o.value];if(lbl)o.text=o.innerText=lbl;}}
 for(const id of ['quiz-nafes-grade-select','quiz-nafes-science-grade-select','quiz-nafes-english-grade-select','quiz-kangaroo-level-select','quiz-kaust-phase-select','quiz-nsmo-phase-select','quiz-olympiad-tier-select']){
  const sel=document.getElementById(id);
  if(!sel||!sel.options)continue;
  for(const o of sel.options){
   if(o.value==='all'){o.text=o.innerText=isAr?'كل المستويات':'All Divisions';}
   else{const lbl=(isAr?kmcLevelLabelsAr:kmcLevelLabelsEn)[o.value];if(lbl)o.text=o.innerText=lbl;}
  }
 }
 const tpSel=document.getElementById('quiz-topic-select');
 if(tpSel&&tpSel.options){for(const o of tpSel.options){if(o.value==='all')o.text=o.innerText=isAr?'كل المواضيع':'All Topics';}}
}
const originalRenderApp=renderApp;
renderApp=function(){
 originalRenderApp();
 localizePracticeSelects();
 for(const select of document.querySelectorAll('select'))select.setAttribute('aria-label',select.id.replace(/-/g,' '));
 let notice=document.getElementById('bank-notice');
 const anchor=document.getElementById('practice-pager')||document.getElementById('quiz-subheading');
 if(!notice&&anchor){notice=document.createElement('p');notice.id='bank-notice';anchor.after(notice)}
 if(notice)notice.textContent=currentLang==='ar'?'مواد تدريب مستقلة؛ الحلول المكتوبة للتقييم الذاتي. المسارات المعتمدة تشمل الدروس المشروحة والاختبارات الموقوتة وأوراق الطباعة A4.':'Independent practice materials; written responses are self-assessed. Supported tracks include Study Lessons, Timed Mocks, and A4 printouts.';
 const jumpEl=document.getElementById('mobile-jump-text');
 if(jumpEl)jumpEl.textContent=currentLang==='ar'?'التدريب':'Practice';
};
const kmcLevelLabels = {
 'Grade 3': 'Grade 3 (Math) / الصف الثالث الابتدائي (رياضيات 3)',
 'Grade 6': 'Grade 6 (Math) / الصف السادس الابتدائي (رياضيات 6)',
 'Grade 9': 'Grade 9 (Math) / الصف الثالث المتوسط (رياضيات 9)',
 'Science · Grade 6': 'Science · Grade 6 / نافس العلوم — السادس الابتدائي',
 'Science · Grade 9': 'Science · Grade 9 / نافس العلوم — الثالث المتوسط',
 'English · Grade 3': 'English · Grade 3 / نافس الإنجليزية — الثالث الابتدائي',
 'English · Grade 6': 'English · Grade 6 / نافس الإنجليزية — السادس الابتدائي',
 'English · Grade 9': 'English · Grade 9 / نافس الإنجليزية — الثالث المتوسط',
 'PreEcolier': 'PreEcolier (Grades 1-2) / بري إيكولير (الصفان 1-2)',
 'Ecolier': 'Ecolier (Grades 3-4) / إيكولير (الصفان 3-4)',
 'Benjamin': 'Benjamin (Grades 5-6) / بنجامين (الصفان 5-6)',
 'Cadet': 'Cadet (Grades 7-8) / كاديت (الصفان 7-8)',
 'Junior': 'Junior (Grades 9-10) / جونيور (الصفان 9-10)',
 'Student': 'Student (Grades 11-12) / ستيودنت (الصفان 11-12)',
 'Track 1: Grades 6-7': 'Track 1: Grades 6-7 / المسار 1: الصفوف 6-7',
 'Track 2: Grades 8-9': 'Track 2: Grades 8-9 / المسار 2: الصفوف 8-9',
 'Track 3: Grades 10-11': 'Track 3: Grades 10-11 / المسار 3: الصفوف 10-11',
 'Phase 1: Junior Olympiad (Grade 7)': 'Phase 1: Grade 7 (Junior) / المرحلة 1: الصف 7',
 'Phase 2: Intermediate Olympiad (Grades 8-9)': 'Phase 2: Grades 8-9 (Intermediate) / المرحلة 2: الصفان 8-9',
 'Phase 3: Senior National Olympiad (Grade 10)': 'Phase 3: Grade 10 (Senior) / المرحلة 3: الصف 10',
 'Tier 1: Junior Olympiad (Grades 7-8)': 'Tier 1: Grades 7-8 (Junior Olympiad) / المستوى 1: الصفان 7-8 (الناشئين)',
 'Tier 2: Intermediate Olympiad (Grades 9-10)': 'Tier 2: Grades 9-10 (Intermediate Olympiad) / المستوى 2: الصفان 9-10 (المتوسط)',
 'Tier 3: Senior Olympiad (Grades 11-12)': 'Tier 3: Grades 11-12 (Senior Olympiad) / المستوى 3: الصفان 11-12 (المتقدم)'
};
const KANG_LEVEL_ORDER = ['PreEcolier','Ecolier','Benjamin','Cadet','Junior','Student'];
const NAFES_LEVEL_ORDER = ['Grade 3','Grade 6','Grade 9','Science · Grade 6','Science · Grade 9','English · Grade 3','English · Grade 6','English · Grade 9'];
loadQuestionsData=async function(){
 const results=await Promise.allSettled(appData.tracks.map(async t=>{const r=await fetch(`data/${t.id}.json`);if(!r.ok)throw Error(t.id);const data=await r.json();if(!Array.isArray(data))throw Error(t.id);return data}));
 appData.questions=results.flatMap(r=>r.status==='fulfilled'?r.value:[]);
 currentFilteredQuestions=[...appData.questions];
 const isAr=currentLang==='ar';
 for(const [track,id] of Object.entries({nafes:'quiz-nafes-grade-select',nafes_science:'quiz-nafes-science-grade-select',nafes_english:'quiz-nafes-english-grade-select',kangaroo:'quiz-kangaroo-level-select',kaust:'quiz-kaust-phase-select',nsmo:'quiz-nsmo-phase-select',olympiad:'quiz-olympiad-tier-select'})){
 const levels=[...new Set(appData.questions.filter(q=>q.track===track).map(q=>q.level))].sort((a,b)=>track==='kangaroo'?KANG_LEVEL_ORDER.indexOf(a)-KANG_LEVEL_ORDER.indexOf(b):track.startsWith('nafes')?NAFES_LEVEL_ORDER.indexOf(a)-NAFES_LEVEL_ORDER.indexOf(b):a.localeCompare(b));
 const select=document.getElementById(id);if(!select)continue;select.replaceChildren(new Option(isAr?'كل المستويات':'All Divisions','all'));
 printPhases[track]=[{val:'all',text:'All levels / كل المستويات'}];
 levels.forEach(level=>{const uiLbl=(isAr?kmcLevelLabelsAr:kmcLevelLabelsEn)[level]||level;const printLbl=kmcLevelLabels[level]||level.replace('Phase','Training level / مستوى تدريب');select.add(new Option(uiLbl,level));printPhases[track].push({val:level,text:printLbl})});
 }
 const failed=results.flatMap((r,i)=>r.status==='rejected'?[appData.tracks[i].name_en]:[]);
 if(failed.length){const alert=document.createElement('p');alert.setAttribute('role','alert');alert.className='p-4 bg-rose-100 text-rose-900 rounded-xl';alert.textContent=`Some banks could not load: ${failed.join(', ')}. Reload to try again. / تعذر تحميل بعض البنوك. أعد تحميل الصفحة.`;document.querySelector('main').prepend(alert)}
};
// Use actual bank levels consistently in both practice and printing.
window.addEventListener('DOMContentLoaded',()=>{
 const closeOnEscape=e=>{if(e.key==='Escape')closePrintModal()};document.addEventListener('keydown',closeOnEscape);
});

// Keep keyboard focus inside the print dialog and restore it on close.
let printReturnFocus=null;
const baseOpenPrint=openPrintModal,baseClosePrint=closePrintModal;
openPrintModal=function(){printReturnFocus=document.activeElement;baseOpenPrint();document.getElementById('print-track-select').focus()};
closePrintModal=function(){baseClosePrint();printReturnFocus?.focus();printReturnFocus=null};
document.addEventListener('keydown',e=>{
 const modal=document.getElementById('print-modal');
 if(e.key!=='Tab'||modal.classList.contains('hidden'))return;
 const els=[...modal.querySelectorAll('button:not([disabled]),select:not([disabled]),input:not([disabled])')].filter(el=>el.getClientRects().length);
 if(!els.length)return;
 const first=els[0],last=els[els.length-1];
 if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
 else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
});
