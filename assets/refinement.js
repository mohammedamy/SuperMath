/* Extend the original bilingual static application without changing its hosting. */
Object.assign(dict.en, {
 printTitle:'SuperMath · Practice sheet',printBtnText:'Print practice',appTitle:'SuperMath',appSubtitle:'Edugates International School · Mathematics practice',
 badgeOverview:'PRACTISE · REASON · PROGRESS',heroHeading:'Find your next mathematical challenge.',
 heroDesc:'Choose your track and level. Work through each problem, use a hint when you need one, and learn from the solution.',
 sec1Title:'Choose your track',sec1Desc:'Select a card to open its question bank. Use your grade to narrow the choice.',
 quizHeading:'Your practice workspace',quizSubheading:'Select a level and topic, then work at your own pace.',
 chart1Title:'Topics in the current banks',chart1Caption:'Question counts by broad topic. These are bank statistics, not official exam weights.',
 chart2Title:'Question formats in the current banks',chart2Caption:'Actual multiple-choice and written-response proportions. Written solutions are self-assessed.',
 sec2Title:'Explore the banks',sec2Desc:'Understand the content available for practice.',
 scaleTitle:'Practice-bank planning',scaleDesc:'An estimate for planning future additions; this is not a count of available questions.',
 stat1Label:'Practice tracks',stat1Value:'6 tracks',stat4Value:'English & Arabic',stat2Value:'Grades 3–12',
 footerText:'© 2026 SuperMath · Edugates International School. Independent practice materials; no exam-board endorsement.'
});
Object.assign(dict.ar, {
 printTitle:'SuperMath · ورقة تدريب',printBtnText:'طباعة التدريب',appTitle:'SuperMath | سوبر ماث',appSubtitle:'مدرسة بوابة المعرفة العالمية · تدريب الرياضيات',
 badgeOverview:'تدرّب · فكّر · تقدّم',heroHeading:'ابدأ تحدّيك الرياضي التالي.',
 heroDesc:'اختر المسار والمستوى. حاول حل السؤال، واستعن بالتلميح عند الحاجة، ثم تعلّم من خطوات الحل.',
 sec1Title:'اختر مسارك',sec1Desc:'اضغط على بطاقة لفتح بنك الأسئلة. يمكنك تحديد صفك لتضييق الاختيار.',
 quizHeading:'مساحة التدريب',quizSubheading:'اختر المستوى والموضوع، وتدرّب بالسرعة التي تناسبك.',
 sec2Title:'استكشف البنوك',sec2Desc:'تعرّف على المحتوى المتاح للتدريب.',
 chart1Title:'الموضوعات في البنوك الحالية',chart1Caption:'أعداد الأسئلة حسب المجالات العامة، وليست الأوزان الرسمية للاختبارات.',
 chart2Title:'أنماط الأسئلة في البنوك الحالية',chart2Caption:'النسب الفعلية للاختيار من متعدد والإجابة المكتوبة. الحلول المكتوبة للتقييم الذاتي.',
 scaleTitle:'تخطيط بنك التدريب',scaleDesc:'تقدير للتوسعات المستقبلية، وليس عدد الأسئلة المتاحة.',
 stat1Label:'مسارات التدريب',stat1Value:'6 مسارات',stat4Value:'العربية والإنجليزية',stat2Value:'الصفوف 3–12',
 footerText:'© 2026 SuperMath · مدرسة بوابة المعرفة العالمية. مواد تدريب مستقلة غير معتمدة من جهات الاختبارات.'
});
const trackUpdates = {
 kangaroo:{levels_en:'Available: Grades 3–10',levels_ar:'المتاح: الصفوف 3–10',grades:[3,4,5,6,7,8,9,10]},
 kaust:{name_en:'KAUST · STEM preparation',name_ar:'كاوست · إعداد رياضي STEM',format_en:'Independent enrichment levels; placement-test scope unverified',format_ar:'مستويات إثرائية مستقلة؛ نطاق اختبار القبول غير موثق',badge_en:'STEM enrichment',badge_ar:'إثراء رياضي'},
 nsmo:{name_en:'NSMO · Olympiad preparation',name_ar:'نسمو · إعداد للأولمبياد',format_en:'SuperMath training levels; not official competition rounds',format_ar:'مستويات تدريب سوبر ماث، وليست جولات المسابقة الرسمية',levels_en:'Training: Grades 5–12',levels_ar:'تدريب: الصفوف 5–12',grades:[5,6,7,8,9,10,11,12]},
 olympiad:{name_en:'Olympiad · Proof practice',name_ar:'الأولمبياد · تدريب البراهين',format_en:'Full written reasoning; foundation to advanced practice',format_ar:'حلول مكتوبة مبررة؛ تدريب تأسيسي ومتقدم'},
 jee:{name_en:'JEE · Mathematics',name_ar:'JEE · الرياضيات',format_en:'Mixed mathematics practice; not a full Main/Advanced mock',format_ar:'تدريب رياضيات متنوع؛ ليس محاكاة كاملة لـ Main أو Advanced'}
};
appData.tracks.forEach(t=>Object.assign(t,trackUpdates[t.id]||{}));
function chooseTrack(id){
 const track=appData.tracks.find(t=>t.id===id);
 if(!track || (currentSelectedGrade!=='all'&&!track.grades.includes(currentSelectedGrade)))return;
 document.getElementById('quiz-track-select').value=id;filterQuestions();
 document.getElementById('practice').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
 document.getElementById('quiz-track-select').focus({preventScroll:true});
}
function renderCharts(){
 if(!topicRadarChartInstance||!formatBarChartInstance)return;
 const isAr=currentLang==='ar';
 const names=appData.tracks.map(t=>isAr?t.name_ar:t.name_en);
 const categories=[/algebra|function|equation|polynomial|complex|matri|sequence|inequal/i,/geometr|area|angle|circle|triangle|volume|spatial|perimeter/i,/number|divisib|integer|parity|arithmet|fraction|ratio|percent|decimal|operation|place value/i,/combin|logic|count|pattern|graph theory/i,/calculus|integr|deriv|limit|differential/i,/statistic|data|probab/i];
 topicRadarChartInstance.data.labels=isAr?['الجبر','الهندسة','الأعداد','العد والمنطق','التحليل','البيانات والاحتمالات']:['Algebra','Geometry','Numbers','Counting & logic','Calculus','Data & probability'];
 const colors=['#fb7185','#60a5fa','#34d399','#2dd4bf','#fbbf24','#c084fc'];
 topicRadarChartInstance.data.datasets=appData.tracks.map((t,i)=>({label:names[i],data:categories.map(r=>appData.questions.filter(q=>q.track===t.id&&r.test(q.topic)).length),borderColor:colors[i],backgroundColor:colors[i]+'18',borderWidth:2}));
 formatBarChartInstance.data.labels=names;
 formatBarChartInstance.data.datasets=[{label:isAr?'اختيار من متعدد':'Multiple choice',backgroundColor:'#3b82f6',data:appData.tracks.map(t=>{const c=PracticeCore.formatCounts(appData.questions,t.id);return c.total?100*c.mcq/c.total:0})},{label:isAr?'إجابة مكتوبة':'Written response',backgroundColor:'#f59e0b',data:appData.tracks.map(t=>{const c=PracticeCore.formatCounts(appData.questions,t.id);return c.total?100*c.written/c.total:0})}];
 topicRadarChartInstance.update();formatBarChartInstance.update();
}
const originalRenderApp=renderApp;
renderApp=function(){
 originalRenderApp();
 for(const select of document.querySelectorAll('select'))select.setAttribute('aria-label',select.id.replace(/-/g,' '));
 let notice=document.getElementById('bank-notice');
 if(!notice){notice=document.createElement('p');notice.id='bank-notice';document.getElementById('quiz-subheading').after(notice)}
 notice.textContent=currentLang==='ar'?'مواد تدريب مستقلة. الحلول المكتوبة للتقييم الذاتي. مستويات كاوست ونسمو هنا مستويات تدريبية وليست مراحل رسمية للاختبار.':'Independent practice materials. Written responses are self-assessed. KAUST and NSMO levels here are training levels, not official exam stages.';
};
loadQuestionsData=async function(){
 const results=await Promise.allSettled(appData.tracks.map(async t=>{const r=await fetch(`data/${t.id}.json`);if(!r.ok)throw Error(t.id);const data=await r.json();if(!Array.isArray(data))throw Error(t.id);return data}));
 appData.questions=results.flatMap(r=>r.status==='fulfilled'?r.value:[]);
 currentFilteredQuestions=[...appData.questions];
 for(const [track,id] of Object.entries({nafes:'quiz-nafes-grade-select',kangaroo:'quiz-kangaroo-level-select',kaust:'quiz-kaust-phase-select',nsmo:'quiz-nsmo-phase-select'})){
 const levels=[...new Set(appData.questions.filter(q=>q.track===track).map(q=>q.level))].sort();
 const select=document.getElementById(id);select.replaceChildren(new Option('All levels / كل المستويات','all'));
 printPhases[track]=[{val:'all',text:'All levels / كل المستويات'}];
 levels.forEach(level=>{const label=level.replace('Phase','Training level / مستوى تدريب');select.add(new Option(label,level));printPhases[track].push({val:level,text:label})});
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
