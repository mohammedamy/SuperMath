const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const app=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(s=>s.includes('const appData'));
const elements=new Map(),events=[];
class El {
 constructor(id){this.id=id;this.value='all';this.options=[];this.style={};this.disabled=false;this.classes=new Set();this.classList={add:(...v)=>v.forEach(x=>this.classes.add(x)),remove:(...v)=>v.forEach(x=>this.classes.delete(x)),contains:x=>this.classes.has(x)};this._html=''}
 set innerHTML(v){this._html=v;if(v==='')this.options=[]} get innerHTML(){return this._html}
 setAttribute(k,v){this[k]=v} getContext(){return {}}
 appendChild(el){this.options.push(el)} add(el){this.options.push(el)}
 replaceChildren(...els){this.options=els;this.value=els[0]?.value??''}
 after(){} prepend(){} remove(){} insertBefore(){} focus(){document.activeElement=this} scrollIntoView(){}
 querySelectorAll(){return []}getClientRects(){return [1]}
}
for(const m of html.matchAll(/id="([^"]+)"/g))elements.set(m[1],new El(m[1]));
for(const id of ['frq-answer-input','bank-notice','study-lessons','kaust-mock-exams','kmc-mock-clock','lesson-filter-pill'])elements.set(id,new El(id));
elements.get('practice').parentNode={insertBefore(){}};
elements.get('practice').children=[];
elements.get('print-include-solutions').checked=true;
elements.get('print-include-omr').checked=false;
elements.get('print-custom-title').value='';
elements.get('print-custom-subtitle').value='';
elements.get('print-pct-easy').value='35';
elements.get('print-pct-med').value='40';
elements.get('print-pct-hard').value='25';
const document={documentElement:new El('html'),body:new El('body'),activeElement:null,getElementById:id=>{assert(elements.has(id),'Unknown element '+id);return elements.get(id)},createElement:tag=>new El(tag),querySelectorAll:s=>s==='select'?[...elements.values()].filter(e=>e.id.includes('select')):[],querySelector:()=>new El('main'),addEventListener(){}};
elements.get('slider-q-count').value='1000';
const context=vm.createContext({document,console,Option:class{constructor(text,value){this.text=this.innerText=text;this.value=value}},Chart:class{constructor(ctx,opts){Object.assign(this,opts)}update(){}},matchMedia:()=>({matches:false}),localStorage:{setItem(){}},setTimeout:f=>f(),fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,url),'utf8'))})});
context.window=context;context.addEventListener=(name,fn)=>{if(name==='DOMContentLoaded')events.push(fn)};let prints=0;context.print=()=>prints++;
vm.runInContext(fs.readFileSync(path.join(root,'assets/practice-core.js'),'utf8'),context);
vm.runInContext(app,context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/refinement.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/kaust-study.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/kaust-mocks.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/worksheet-customizer.js'),'utf8'),context);
const run=s=>vm.runInContext(s,context);
(async()=>{
 for(const callback of events)await callback();
 await new Promise(r=>setImmediate(r));
 assert.equal(run('appData.questions.length'),8420);
 assert.equal(run('currentFilteredQuestions.length'),8420);
 assert.deepEqual(elements.get('quiz-kangaroo-level-select').options.map(o=>o.value),['all','PreEcolier','Ecolier','Benjamin','Cadet','Junior','Student']);
 assert.deepEqual(elements.get('quiz-nafes-grade-select').options.map(o=>o.value),['all','Grade 3','Grade 6','Grade 9']);
 assert.deepEqual(elements.get('quiz-olympiad-tier-select').options.map(o=>o.value),['all','Tier 1: Junior Olympiad (Grades 7-8)','Tier 2: Intermediate Olympiad (Grades 9-10)','Tier 3: Senior Olympiad (Grades 11-12)']);
 // Switching away from a selected subtrack must not retain its hidden filter.
 elements.get('quiz-track-select').value='kaust';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),2250);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===5&&q.content.ar.options.length===5&&q.content.en.diagram?.includes("<svg")&&q.content.ar.diagram?.includes("<svg"))'));
 elements.get('quiz-kaust-phase-select').value='Track 1: Grades 6-7';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),750);
 elements.get('quiz-kaust-phase-select').value='Track 2: Grades 8-9';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),750);
 elements.get('quiz-kaust-phase-select').value='Track 3: Grades 10-11';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),750);
 elements.get('quiz-kaust-phase-select').value='all';context.filterQuestions();
 // KAUST KMC exclusively covers Grades 6-11 across its 3 official grade bands.
 for(const g of [1,2,3,4,5,12]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 KAUST questions`);
 }
 for(const [g,expectedLevel] of [[6,'Track 1: Grades 6-7'],[7,'Track 1: Grades 6-7'],[8,'Track 2: Grades 8-9'],[9,'Track 2: Grades 8-9'],[10,'Track 3: Grades 10-11'],[11,'Track 3: Grades 10-11']]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),750);
  assert(run(`currentFilteredQuestions.every(q=>q.level===${JSON.stringify(expectedLevel)})`));
 }
 context.setGradeFilter('all');
 // Verify KAUST geometry SVG diagram & 5-option (E) rendering in quiz card.
 elements.get('quiz-topic-select').value='Geometry';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),490);
 assert(elements.get('question-card-container').innerHTML.includes('<svg'));
 assert(elements.get('question-card-container').innerHTML.includes('>E<')||elements.get('question-card-container').innerHTML.includes('E\n'));
 elements.get('quiz-topic-select').value='all';context.filterQuestions();
 elements.get('quiz-track-select').value='nafes';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),1080);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===4&&q.content.ar.options.length===4)'));
 for(const g of [1,2,4,5,7,8,10,11,12]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 Nafes questions`);
 }
 for(const [g,expectedLevel] of [[3,'Grade 3'],[6,'Grade 6'],[9,'Grade 9']]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),360);
  assert(run(`currentFilteredQuestions.every(q=>q.level===${JSON.stringify(expectedLevel)})`));
 }
 context.setGradeFilter('all');
 elements.get('quiz-nafes-grade-select').value='Grade 3';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),360);
 elements.get('quiz-track-select').value='jee';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),500);
 assert.equal(elements.get('quiz-nafes-grade-select').value,'all');
 // Grade filtering acts on questions, not merely the appearance of track cards.
 // Kangaroo Math covers full Grades 1-12 across PreEcolier (360), Ecolier (360), Benjamin (360), Cadet (360), Junior (360), and Student (360) = 2,160 5-option MCQs.
 elements.get('quiz-track-select').value='kangaroo';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),2160);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===5&&q.content.ar.options.length===5&&[3,4,5].includes(q.kang_points))'));
 for(const [g,expectedLevel] of [[1,'PreEcolier'],[2,'PreEcolier'],[3,'Ecolier'],[4,'Ecolier'],[5,'Benjamin'],[6,'Benjamin'],[7,'Cadet'],[8,'Cadet'],[9,'Junior'],[10,'Junior'],[11,'Student'],[12,'Student']]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),360);
  assert(run(`currentFilteredQuestions.every(q=>q.level===${JSON.stringify(expectedLevel)})`));
 }
 context.setGradeFilter('all');
 // NSMO (Mawhiba) exclusively covers Grades 7, 8, 9, 10 with 1,350 verified 4-option (A-D) MCQs (450 per Phase).
 elements.get('quiz-track-select').value='nsmo';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),1350);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===4&&q.content.ar.options.length===4)'));
 for(const g of [5,6,11,12]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 NSMO questions`);
 }
 context.setGradeFilter(7);
 assert.equal(run('currentFilteredQuestions.length'),450);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 1: Junior Olympiad (Grade 7)")'));
 context.setGradeFilter(8);
 assert.equal(run('currentFilteredQuestions.length'),450);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 2: Intermediate Olympiad (Grades 8-9)")'));
 context.setGradeFilter(9);
 assert.equal(run('currentFilteredQuestions.length'),450);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 2: Intermediate Olympiad (Grades 8-9)")'));
 context.setGradeFilter(10);
 assert.equal(run('currentFilteredQuestions.length'),450);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 3: Senior National Olympiad (Grade 10)")'));
 context.setGradeFilter('all');
 // Check correct and incorrect answers against keys; next question clears state.
 run('selectedOptionIdx=currentFilteredQuestions[0].correct_index');context.submitAnswer();assert(run('checkIsCorrect()'));
 context.nextQuestion();assert.equal(run('selectedOptionIdx'),null);assert.equal(run('isAnswerSubmitted'),false);
 // Math Olympiad covers Grades 7-12 across 3 official graduated tiers (360 each = 1,080 5-option SVG-illustrated MCQs).
 elements.get('quiz-track-select').value='olympiad';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),1080);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===5&&q.content.ar.options.length===5&&q.content.en.diagram?.includes("<svg")&&q.content.ar.diagram?.includes("<svg"))'));
 for(const g of [1,2,3,4,5,6]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 Olympiad questions`);
 }
 for(const [g,expectedLevel] of [[7,'Tier 1: Junior Olympiad (Grades 7-8)'],[8,'Tier 1: Junior Olympiad (Grades 7-8)'],[9,'Tier 2: Intermediate Olympiad (Grades 9-10)'],[10,'Tier 2: Intermediate Olympiad (Grades 9-10)'],[11,'Tier 3: Senior Olympiad (Grades 11-12)'],[12,'Tier 3: Senior Olympiad (Grades 11-12)']]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),360);
  assert(run(`currentFilteredQuestions.every(q=>q.level===${JSON.stringify(expectedLevel)})`));
 }
 context.setGradeFilter('all');
 // Written work survives a hint rerender and can reveal a solution without a fake mark (tested on JEE FRQ items).
 elements.get('quiz-track-select').value='jee';context.filterQuestions();
 const frqIdx=run('currentFilteredQuestions.findIndex(q=>q.type==="FRQ")');
 assert(frqIdx>=0,'JEE must include FRQ items');
 run(`currentQuestionIdx=${frqIdx}`);context.renderQuestionCard();
 run('selectedOptionIdx="My proof uses parity."');context.toggleHint();
 assert.equal(elements.get('frq-answer-input').value,'My proof uses parity.');
 context.submitAnswer();assert(elements.get('question-card-container').innerHTML.includes('self-assessment'));
 assert(!elements.get('question-card-container').innerHTML.includes('undefined'));
 // Printed FRQ keys must not become choice A from an old numeric placeholder.
 context.openPrintModal();elements.get('print-q-count').value='500';context.executePrint();
 assert.equal(prints,1);assert(!elements.get('print-container').innerHTML.includes('undefined'));
 assert(elements.get('print-container').innerHTML.includes('FRQ'));
 // Grade-level print bank size is exact.
 elements.get('print-track-select').value='nafes';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Grade 6';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,360);
 context.togglePrintLesson('NAFS-L2-03');
 assert.equal(elements.get('print-max-q').innerText,60);
 context.clearPrintLessons();
 assert.equal(elements.get('print-max-q').innerText,360);
 elements.get('print-track-select').value='kangaroo';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Junior';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,360);
 context.togglePrintLesson('KANG-L4-02');
 assert.equal(elements.get('print-max-q').innerText,60);
 context.clearPrintLessons();
 assert.equal(elements.get('print-max-q').innerText,360);
 elements.get('print-track-select').value='nsmo';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Phase 1: Junior Olympiad (Grade 7)';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,450);
 elements.get('print-phase-select').value='Phase 3: Senior National Olympiad (Grade 10)';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,450);
 elements.get('print-track-select').value='olympiad';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Tier 2: Intermediate Olympiad (Grades 9-10)';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,360);
 context.togglePrintLesson('OLYM-L2-03');
 assert.equal(elements.get('print-max-q').innerText,60);
 context.clearPrintLessons();
 assert.equal(elements.get('print-max-q').innerText,360);
 elements.get('print-track-select').value='kaust';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Track 1: Grades 6-7';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,750);
 elements.get('print-phase-select').value='Track 2: Grades 8-9';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,750);
 elements.get('print-phase-select').value='Track 3: Grades 10-11';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,750);
 elements.get('print-q-count').value='15';context.executePrint();
 assert.equal(prints,2);assert(!elements.get('print-container').innerHTML.includes('undefined'));
 // Verify Edugates A4 Worksheet Customizer (multi-lesson filter, custom title/subtitle, scratch space, OMR, quick/none key)
 context.openPrintModal();
 elements.get('print-track-select').value='nsmo';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Phase 2: Intermediate Olympiad (Grades 8-9)';context.updatePrintModalMax();
 context.togglePrintLesson('NSMO-L2-05');
 assert.equal(elements.get('print-max-q').innerText,75);
 elements.get('print-custom-title').value='Grade 8-9 Mawhiba Geometry Custom Sheet';
 elements.get('print-custom-subtitle').value='45 Minutes · No Calculator';
 elements.get('print-diff-mode').value='custom';context.onPrintDiffModeChange();
 elements.get('print-scratch-space').value='large';
 elements.get('print-include-omr').checked=true;
 elements.get('print-key-mode').value='quick';context.syncPrintKeyMode('select');
 elements.get('print-q-count').value='6';context.executePrint();
 assert.equal(prints,3);
 assert(elements.get('print-container').innerHTML.includes('Grade 8-9 Mawhiba Geometry Custom Sheet'));
 assert(elements.get('print-container').innerHTML.includes('45 Minutes · No Calculator'));
 assert(elements.get('print-container').innerHTML.includes('eg-omr-sheet'));
 assert(elements.get('print-container').innerHTML.includes('eg-scratch-lg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 elements.get('print-custom-title').value='';
 elements.get('print-custom-subtitle').value='';
 elements.get('print-include-solutions').checked=true;
 context.toggleLanguage();assert.equal(document.documentElement.dir,'rtl');
 context.toggleTheme();
 // A chart CDN failure should not prevent loading the practice banks.
 context.Chart=undefined;context.initCharts();
 // Verify Unified Nafes + Kangaroo + KAUST + NSMO Study Hub & Edugates A4 Print Frame runtime methods
 await new Promise(r=>setImmediate(r));
 assert.equal(run('window.__kaustStudy.nafesLessons.length'),18);
 assert.equal(run('window.__kaustStudy.kangarooLessons.length'),36);
 assert.equal(run('window.__kaustStudy.lessons.length'),18);
 assert.equal(run('window.__kaustStudy.nsmoLessons.length'),18);
 assert.equal(run('window.__kaustStudy.olympiadLessons.length'),18);
 assert(elements.get('study-lessons').innerHTML.includes('Edugates International School'));
 context.setStudyCompetition('olympiad');
 context.openKaustLesson('OLYM-L1-01');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.openKaustLesson('OLYM-L3-05');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('OLYM-L3-05');
 assert.equal(run('currentFilteredQuestions.length'),60);
 assert(run('currentFilteredQuestions.every(q=>q.track==="olympiad"&&q.level==="Tier 3: Senior Olympiad (Grades 11-12)")'));
 context.clearKaustLessonFilter();
 context.setStudyCompetition('nafes');
 context.openKaustLesson('NAFS-L1-01');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('NAFS-L3-04');
 assert.equal(run('currentFilteredQuestions.length'),60);
 assert(run('currentFilteredQuestions.every(q=>q.track==="nafes"&&q.level==="Grade 9")'));
 context.clearKaustLessonFilter();
 context.setStudyCompetition('kangaroo');
 context.openKaustLesson('KANG-L0-01');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.openKaustLesson('KANG-L5-03');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('KANG-L5-02');
 assert.equal(run('currentFilteredQuestions.length'),60);
 assert(run('currentFilteredQuestions.every(q=>q.track==="kangaroo"&&q.level==="Student")'));
 context.practiceKaustLesson('KANG-L2-03');
 assert.equal(run('currentFilteredQuestions.length'),60);
 assert(run('currentFilteredQuestions.every(q=>q.track==="kangaroo"&&q.level==="Benjamin")'));
 context.clearKaustLessonFilter();
 context.setStudyCompetition('kaust');
 context.openKaustLesson('KMC-L3-05');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('KMC-L3-05');
 assert(run('currentFilteredQuestions.length')>50&&run('currentFilteredQuestions.every(q=>q.track==="kaust")'));
 context.clearKaustLessonFilter();
 context.setStudyCompetition('nsmo');
 context.openKaustLesson('NSMO-L2-05');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('NSMO-L2-05');
 assert.equal(run('currentFilteredQuestions.length'),75);
 assert(run('currentFilteredQuestions.every(q=>q.track==="nsmo")'));
 context.clearKaustLessonFilter();
 const prevPrints=prints;
 context.printKaustLesson('KMC-L1-01');
 assert.equal(prints,prevPrints+1);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustLesson('NSMO-L1-01');
 assert.equal(prints,prevPrints+2);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustLessonDrills('NSMO-L2-04');
 assert.equal(prints,prevPrints+3);
 context.printKaustTrackBooklet('Phase 2: Intermediate Olympiad (Grades 8-9)');
 assert.equal(prints,prevPrints+4);
 assert(elements.get('print-container').innerHTML.includes('eg-print-break'));
 context.printKaustLesson('KANG-L1-01');
 assert.equal(prints,prevPrints+5);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustLessonDrills('KANG-L3-04');
 assert.equal(prints,prevPrints+6);
 context.printKaustTrackBooklet('Benjamin');
 assert.equal(prints,prevPrints+7);
 context.printKaustLesson('NAFS-L1-01');
 assert.equal(prints,prevPrints+8);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustLessonDrills('NAFS-L2-02');
 assert.equal(prints,prevPrints+9);
 context.printKaustTrackBooklet('Grade 6');
 assert.equal(prints,prevPrints+10);
 context.printKaustLesson('OLYM-L1-01');
 assert.equal(prints,prevPrints+11);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustLessonDrills('OLYM-L2-04');
 assert.equal(prints,prevPrints+12);
 context.printKaustTrackBooklet('Tier 3: Senior Olympiad (Grades 11-12)');
 assert.equal(prints,prevPrints+13);
 // Verify Unified Nafes (12 papers, 4-opt, +1/0/0), Kangaroo (24 papers, 5-opt, +3/+4/+5 & 0 wrong), KAUST (15 papers, 5-opt, +4/-1/0), NSMO (12 papers, 4-opt, +4/0/0) & Olympiad (12 papers, 5-opt, +6/0/0) Full Mock Simulators
 assert.equal(run('window.__kaustMocks.nafesMocks.length'),12);
 assert.equal(run('window.__kaustMocks.kangarooMocks.length'),24);
 assert.equal(run('window.__kaustMocks.mocks.length'),15);
 assert.equal(run('window.__kaustMocks.nsmoMocks.length'),12);
 assert.equal(run('window.__kaustMocks.olympiadMocks.length'),12);
 // Nafes Timed Mock Simulator: 20 Qs (45 min) for Grade 3, 25 Qs (60 min) for Grade 6, 30 Qs (75 min) for Grade 9, +1 / 0 / 0 scoring
 context.setMockCompetition('nafes');
 context.startKaustMock('NAFS-MOCK-G3-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),20);
 assert.equal(run('window.__kaustMocks.session.remainingSec'),2700);
 context.exitKaustMock(true);
 context.startKaustMock('NAFS-MOCK-G6-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),25);
 assert.equal(run('window.__kaustMocks.session.remainingSec'),3600);
 context.exitKaustMock(true);
 context.startKaustMock('NAFS-MOCK-G9-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),30);
 assert.equal(run('window.__kaustMocks.session.remainingSec'),4500);
 const f0Ok=run('window.__kaustMocks.session.questions[0].correct_index');
 const f1Bad=run('(window.__kaustMocks.session.questions[1].correct_index+1)%4');
 context.selectKaustMockOption(0,f0Ok);
 context.selectKaustMockOption(1,f1Bad);
 context.requestSubmitKaustMock();
 context.confirmSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.report.score'),1); // +1 correct + 0 wrong = 1
 assert.equal(run('window.__kaustMocks.session.report.maxPoints'),30);
 assert.equal(run('window.__kaustMocks.session.report.correct'),1);
 assert.equal(run('window.__kaustMocks.session.report.wrong'),1);
 assert.equal(run('window.__kaustMocks.session.report.blank'),28);
 const nafesMockPrints=prints;
 context.printKaustMockPaper('NAFS-MOCK-G3-01','student');
 assert.equal(prints,nafesMockPrints+1);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-sheet'));
 assert(!elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustMockPaper('NAFS-MOCK-G9-01','full');
 assert.equal(prints,nafesMockPrints+2);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printBlankKaustOmr('Grade 9');
 assert.equal(prints,nafesMockPrints+3);
 context.exitKaustMock(true);
 const customNafesId=context.generateCustomKaustMock('Grade 6');
 assert(customNafesId&&customNafesId.startsWith('NAFS-MOCK-G6-CUSTOM-'));
 assert.equal(run('window.__kaustMocks.nafesMocks.length'),13);
 assert.equal(run(`window.__kaustMocks.nafesMocks.find(p=>p.id===${JSON.stringify(customNafesId)}).duration_minutes`),60);
 assert.equal(run(`window.__kaustMocks.nafesMocks.find(p=>p.id===${JSON.stringify(customNafesId)}).question_count`),25);
 // Kangaroo Timed Mock Simulator: 24 Qs (96 pts) for PreEcolier/Ecolier/Benjamin, 30 Qs (120 pts) for Cadet/Junior/Student, 75 min, +3/+4/+5 tier points & 0 wrong penalty
 context.setMockCompetition('kangaroo');
 context.startKaustMock('KANG-MOCK-PRE-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),24);
 context.exitKaustMock(true);
 context.startKaustMock('KANG-MOCK-STU-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),30);
 context.exitKaustMock(true);
 context.startKaustMock('KANG-MOCK-BEN-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),24);
 context.exitKaustMock(true);
 context.startKaustMock('KANG-MOCK-JUN-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),30);
 const kEasyOk=run('window.__kaustMocks.session.questions[0].correct_index');   // Part A (Easy) -> +3
 const kMedOk=run('window.__kaustMocks.session.questions[10].correct_index');  // Part B (Medium) -> +4
 const kHardOk=run('window.__kaustMocks.session.questions[20].correct_index'); // Part C (Hard) -> +5
 const kWrong=run('(window.__kaustMocks.session.questions[1].correct_index+1)%5'); // Wrong -> 0
 context.selectKaustMockOption(0,kEasyOk);
 context.selectKaustMockOption(10,kMedOk);
 context.selectKaustMockOption(20,kHardOk);
 context.selectKaustMockOption(1,kWrong);
 context.requestSubmitKaustMock();
 context.confirmSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.report.score'),12); // 3 + 4 + 5 + 0 = 12
 assert.equal(run('window.__kaustMocks.session.report.maxPoints'),120);
 assert.equal(run('window.__kaustMocks.session.report.correct'),3);
 assert.equal(run('window.__kaustMocks.session.report.wrong'),1);
 assert.equal(run('window.__kaustMocks.session.report.blank'),26);
 const kangMockPrints=prints;
 context.printKaustMockPaper('KANG-MOCK-ECO-01','student');
 assert.equal(prints,kangMockPrints+1);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-sheet'));
 assert(!elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustMockPaper('KANG-MOCK-JUN-01','full');
 assert.equal(prints,kangMockPrints+2);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printBlankKaustOmr('Cadet');
 assert.equal(prints,kangMockPrints+3);
 context.exitKaustMock(true);
 const customKangId=context.generateCustomKaustMock('Student');
 assert(customKangId&&customKangId.startsWith('KANG-MOCK-')&&customKangId.includes('CUSTOM'));
 assert.equal(run('window.__kaustMocks.kangarooMocks.length'),25);
 context.setMockCompetition('kaust');
 context.startKaustMock('KMC-MOCK-T3-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),30);
 const q0Ok=run('window.__kaustMocks.session.questions[0].correct_index');
 const q1Bad=run('(window.__kaustMocks.session.questions[1].correct_index+1)%5');
 context.selectKaustMockOption(0,q0Ok);
 context.selectKaustMockOption(1,q1Bad);
 context.selectKaustMockOption(2,0);
 context.clearKaustMockOption(2);
 context.toggleKaustMockFlag(1);
 context.setKaustMockViewMode('all');
 assert(!elements.get('kaust-mock-exams').innerHTML.includes('undefined'));
 context.requestSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.confirmSubmit'),true);
 context.confirmSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.mode'),'review');
 assert.equal(run('window.__kaustMocks.session.report.score'),3); // +4 correct -1 wrong + 0 blank = 3
 context.exitKaustMock(true);
 // NSMO Timed Mock Simulator: 25 Qs, 90 min, +4 / 0 / 0 scoring (no negative marking!)
 context.setMockCompetition('nsmo');
 context.startKaustMock('NSMO-MOCK-P3-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),25);
 const n0Ok=run('window.__kaustMocks.session.questions[0].correct_index');
 const n1Bad=run('(window.__kaustMocks.session.questions[1].correct_index+1)%4');
 context.selectKaustMockOption(0,n0Ok);
 context.selectKaustMockOption(1,n1Bad);
 context.requestSubmitKaustMock();
 context.confirmSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.report.score'),4); // +4 correct + 0 wrong = 4!
 assert.equal(run('window.__kaustMocks.session.report.correct'),1);
 assert.equal(run('window.__kaustMocks.session.report.wrong'),1);
 assert.equal(run('window.__kaustMocks.session.report.blank'),23);
 const mockPrints=prints;
 context.printKaustMockPaper('NSMO-MOCK-P3-01','student');
 assert.equal(prints,mockPrints+1);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-sheet'));
 assert(!elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustMockPaper('NSMO-MOCK-P3-01','full');
 assert.equal(prints,mockPrints+2);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printBlankKaustOmr('Phase 1: Junior Olympiad (Grade 7)');
 assert.equal(prints,mockPrints+3);
 context.exitKaustMock(true);
 const customNsmoId=context.generateCustomKaustMock('Phase 1: Junior Olympiad (Grade 7)');
 assert(customNsmoId&&customNsmoId.startsWith('NSMO-MOCK-')&&customNsmoId.includes('CUSTOM'));
 assert.equal(run('window.__kaustMocks.nsmoMocks.length'),13);
 // Olympiad Timed Mock Simulator: 25 Qs (5 options A-E), 90 min (5400 sec), +6 / 0 / 0 scoring (150 max pts)
 context.setMockCompetition('olympiad');
 context.startKaustMock('OLYM-MOCK-T3-01');
 assert.equal(run('window.__kaustMocks.session.questions.length'),25);
 assert.equal(run('window.__kaustMocks.session.remainingSec'),5400);
 const o0Ok=run('window.__kaustMocks.session.questions[0].correct_index');
 const o1Bad=run('(window.__kaustMocks.session.questions[1].correct_index+1)%5');
 context.selectKaustMockOption(0,o0Ok);
 context.selectKaustMockOption(1,o1Bad);
 context.requestSubmitKaustMock();
 context.confirmSubmitKaustMock();
 assert.equal(run('window.__kaustMocks.session.report.score'),6); // +6 correct + 0 wrong = 6
 assert.equal(run('window.__kaustMocks.session.report.maxPoints'),150);
 assert.equal(run('window.__kaustMocks.session.report.correct'),1);
 assert.equal(run('window.__kaustMocks.session.report.wrong'),1);
 assert.equal(run('window.__kaustMocks.session.report.blank'),23);
 const olymMockPrints=prints;
 context.printKaustMockPaper('OLYM-MOCK-T1-01','student');
 assert.equal(prints,olymMockPrints+1);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-sheet'));
 assert(!elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustMockPaper('OLYM-MOCK-T3-01','full');
 assert.equal(prints,olymMockPrints+2);
 assert(elements.get('print-container').innerHTML.includes('eg-omr-shaded'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printBlankKaustOmr('Tier 2: Intermediate Olympiad (Grades 9-10)');
 assert.equal(prints,olymMockPrints+3);
 context.exitKaustMock(true);
 const customOlymId=context.generateCustomKaustMock('Tier 2: Intermediate Olympiad (Grades 9-10)');
 assert(customOlymId&&customOlymId.startsWith('OLYM-MOCK-T2-CUSTOM-'));
 assert.equal(run('window.__kaustMocks.olympiadMocks.length'),13);
 console.log('PASS: startup, 8420 questions, Nafes + Kangaroo + KAUST + NSMO + Olympiad study hubs (108 lessons), Nafes + Kangaroo + KAUST + NSMO + Olympiad timed mock simulators (75 papers), Edugates A4 Worksheet Customizer & OMR print engine, Arabic & theme controls.');
 console.log('Runtime tests use lightweight DOM stubs; this is not browser or visual QA.');
})().catch(e=>{console.error(e);process.exitCode=1});

// ---- Nafes + Kangaroo + KAUST + NSMO study lessons & mock exams static schema test ----
(async()=>{
  // 0a. Nafes KSA Static Contract
  const nafesLessons=JSON.parse(fs.readFileSync(path.join(root,'data/nafes_lessons.json'),'utf8')).lessons;
  const nafesMocksDoc=JSON.parse(fs.readFileSync(path.join(root,'data/nafes_mocks.json'),'utf8'));
  const nafesBank=JSON.parse(fs.readFileSync(path.join(root,'data/nafes.json'),'utf8'));
  assert.equal(nafesBank.length,1080);
  assert(nafesBank.filter(q=>q.content.en.diagram&&q.content.en.diagram.includes('<svg')).length>=900);
  assert.equal(nafesLessons.length,18);
  assert.equal(nafesMocksDoc.mocks.length,12);
  const nafesIds=new Set(nafesBank.map(q=>q.id));
  const nafesLessonUsed=new Set();
  for(const l of nafesLessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert(l.en.concepts.every(c=>c.diagram&&c.diagram.includes('<svg')),l.id+' concept SVG');
    assert.equal(l.bank_example_ids.length,6);
    assert.equal(l.drill_ids.length,6);
    l.bank_example_ids.forEach(i=>{assert(nafesIds.has(i),i);nafesLessonUsed.add(i);});
    l.drill_ids.forEach(i=>{assert(nafesIds.has(i),i);assert(!l.bank_example_ids.includes(i),'overlap '+i);nafesLessonUsed.add(i);});
    for(const e of l.en.examples)assert.equal(e.options.length,4);
  }
  const nafesMockUsed=new Set();
  for(const m of nafesMocksDoc.mocks){
    const exp=m.level==='Grade 3'?20:m.level==='Grade 6'?25:30;
    const expDur=m.level==='Grade 3'?45:m.level==='Grade 6'?60:75;
    assert.equal(m.question_ids.length,exp,m.id);
    assert.equal(m.max_points,exp,m.id);
    assert.equal(m.duration_minutes,expDur,m.id);
    assert.equal(m.points_correct,1,m.id);
    assert.equal(m.points_wrong,0,m.id);
    m.question_ids.forEach(i=>{
      assert(nafesIds.has(i),i);
      assert(!nafesLessonUsed.has(i),'nafes lesson overlap '+i);
      assert(!nafesMockUsed.has(i),'nafes mock duplicate '+i);
      nafesMockUsed.add(i);
    });
  }
  assert.equal(nafesMockUsed.size,300);
  // 0. Kangaroo Math Static Contract
  const kangLessons=JSON.parse(fs.readFileSync(path.join(root,'data/kangaroo_lessons.json'),'utf8')).lessons;
  const kangMocksDoc=JSON.parse(fs.readFileSync(path.join(root,'data/kangaroo_mocks.json'),'utf8'));
  const kangBank=JSON.parse(fs.readFileSync(path.join(root,'data/kangaroo.json'),'utf8'));
  assert.equal(kangBank.length,2160);
  assert.equal(kangBank.filter(q=>q.content.en.diagram&&q.content.en.diagram.includes('<svg')).length,2160);
  assert.equal(kangLessons.length,36);
  assert.equal(kangMocksDoc.mocks.length,24);
  const kangIds=new Set(kangBank.map(q=>q.id));
  const kangLessonUsed=new Set();
  for(const l of kangLessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert(l.en.concepts.every(c=>c.diagram&&c.diagram.includes('<svg')),l.id+' concept SVG');
    assert.equal(l.bank_example_ids.length,6);
    assert.equal(l.drill_ids.length,6);
    l.bank_example_ids.forEach(i=>{assert(kangIds.has(i),i);kangLessonUsed.add(i);});
    l.drill_ids.forEach(i=>{assert(kangIds.has(i),i);assert(!l.bank_example_ids.includes(i),'overlap '+i);kangLessonUsed.add(i);});
    for(const e of l.en.examples)assert.equal(e.options.length,5);
  }
  const kangMockUsed=new Set();
  for(const m of kangMocksDoc.mocks){
    const exp=(m.level==='PreEcolier'||m.level==='Ecolier'||m.level==='Benjamin')?24:30;
    const expPts=(m.level==='PreEcolier'||m.level==='Ecolier'||m.level==='Benjamin')?96:120;
    assert.equal(m.question_ids.length,exp,m.id);
    assert.equal(m.max_points,expPts,m.id);
    assert.equal(m.duration_minutes,75,m.id);
    assert.equal(m.points_wrong,0,m.id);
    assert.deepEqual(m.tier_points,{Easy:3,Medium:4,Hard:5});
    m.question_ids.forEach(i=>{
      assert(kangIds.has(i),i);
      assert(!kangLessonUsed.has(i),'kangaroo lesson overlap '+i);
      assert(!kangMockUsed.has(i),'kangaroo mock duplicate '+i);
      kangMockUsed.add(i);
    });
  }
  assert.equal(kangMockUsed.size,648);

  // 1. KAUST Static Contract
  const lessons=JSON.parse(fs.readFileSync(path.join(root,'data/kaust_lessons.json'),'utf8')).lessons;
  const mocksDoc=JSON.parse(fs.readFileSync(path.join(root,'data/kaust_mocks.json'),'utf8'));
  assert.equal(lessons.length,18);
  assert.equal(mocksDoc.mocks.length,15);
  const ids=new Set(JSON.parse(fs.readFileSync(path.join(root,'data/kaust.json'),'utf8')).map(q=>q.id));
  const lessonUsed=new Set();
  for(const l of lessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert(l.en.concepts.every(c=>c.diagram&&c.diagram.includes('<svg')),l.id+' concept SVG');
    assert.equal(l.bank_example_ids.length,6);
    assert.equal(l.drill_ids.length,6);
    l.bank_example_ids.forEach(i=>{assert(ids.has(i),i);lessonUsed.add(i);});
    l.drill_ids.forEach(i=>{assert(ids.has(i),i);assert(!l.bank_example_ids.includes(i),'overlap '+i);lessonUsed.add(i);});
    for(const e of l.en.examples)assert.equal(e.options.length,5);
  }
  const mockUsed=new Set();
  for(const m of mocksDoc.mocks){
    const exp=m.level==='Track 3: Grades 10-11'?30:24;
    assert.equal(m.question_ids.length,exp,m.id);
    assert.equal(m.duration_minutes,120);
    m.question_ids.forEach(i=>{
      assert(ids.has(i),i);
      assert(!lessonUsed.has(i),'lesson overlap '+i);
      assert(!mockUsed.has(i),'mock duplicate '+i);
      mockUsed.add(i);
    });
  }
  assert.equal(mockUsed.size,390);

  // 2. NSMO (Mawhiba) Static Contract
  const nsmoLessons=JSON.parse(fs.readFileSync(path.join(root,'data/nsmo_lessons.json'),'utf8')).lessons;
  const nsmoMocksDoc=JSON.parse(fs.readFileSync(path.join(root,'data/nsmo_mocks.json'),'utf8'));
  const nsmoBank=JSON.parse(fs.readFileSync(path.join(root,'data/nsmo.json'),'utf8'));
  assert.equal(nsmoBank.length,1350);
  assert.equal(nsmoLessons.length,18);
  assert.equal(nsmoMocksDoc.mocks.length,12);
  const nsmoIds=new Set(nsmoBank.map(q=>q.id));
  const nsmoLessonUsed=new Set();
  for(const l of nsmoLessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert(l.en.concepts.every(c=>c.diagram&&c.diagram.includes('<svg')),l.id+' concept SVG');
    assert.equal(l.bank_example_ids.length,6);
    assert.equal(l.drill_ids.length,6);
    l.bank_example_ids.forEach(i=>{assert(nsmoIds.has(i),i);nsmoLessonUsed.add(i);});
    l.drill_ids.forEach(i=>{assert(nsmoIds.has(i),i);assert(!l.bank_example_ids.includes(i),'overlap '+i);nsmoLessonUsed.add(i);});
    for(const e of l.en.examples)assert.equal(e.options.length,4);
  }
  const nsmoMockUsed=new Set();
  for(const m of nsmoMocksDoc.mocks){
    assert.equal(m.question_ids.length,25,m.id);
    assert.equal(m.duration_minutes,90,m.id);
    assert.equal(m.points_wrong,0,m.id);
    m.question_ids.forEach(i=>{
      assert(nsmoIds.has(i),i);
      assert(!nsmoLessonUsed.has(i),'nsmo lesson overlap '+i);
      assert(!nsmoMockUsed.has(i),'nsmo mock duplicate '+i);
      nsmoMockUsed.add(i);
    });
  }
  assert.equal(nsmoMockUsed.size,300);

  // 3. Math Olympiad Static Contract
  const olymLessons=JSON.parse(fs.readFileSync(path.join(root,'data/olympiad_lessons.json'),'utf8')).lessons;
  const olymMocksDoc=JSON.parse(fs.readFileSync(path.join(root,'data/olympiad_mocks.json'),'utf8'));
  const olymBank=JSON.parse(fs.readFileSync(path.join(root,'data/olympiad.json'),'utf8'));
  assert.equal(olymBank.length,1080);
  assert.equal(olymBank.filter(q=>q.content.en.diagram&&q.content.en.diagram.includes('<svg')&&q.content.ar.diagram&&q.content.ar.diagram.includes('<svg')).length,1080);
  assert.equal(olymLessons.length,18);
  assert.equal(olymMocksDoc.mocks.length,12);
  const olymIds=new Set(olymBank.map(q=>q.id));
  const olymLessonUsed=new Set();
  for(const l of olymLessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert(l.en.concepts.every(c=>c.diagram&&c.diagram.includes('<svg')),l.id+' concept SVG');
    assert.equal(l.bank_example_ids.length,6);
    assert.equal(l.drill_ids.length,6);
    l.bank_example_ids.forEach(i=>{assert(olymIds.has(i),i);olymLessonUsed.add(i);});
    l.drill_ids.forEach(i=>{assert(olymIds.has(i),i);assert(!l.bank_example_ids.includes(i),'overlap '+i);olymLessonUsed.add(i);});
    for(const e of l.en.examples)assert.equal(e.options.length,5);
  }
  const olymMockUsed=new Set();
  for(const m of olymMocksDoc.mocks){
    assert.equal(m.question_ids.length,25,m.id);
    assert.equal(m.max_points,150,m.id);
    assert.equal(m.duration_minutes,90,m.id);
    assert.equal(m.points_correct,6,m.id);
    assert.equal(m.points_wrong,0,m.id);
    m.question_ids.forEach(i=>{
      assert(olymIds.has(i),i);
      assert(!olymLessonUsed.has(i),'olympiad lesson overlap '+i);
      assert(!olymMockUsed.has(i),'olympiad mock duplicate '+i);
      olymMockUsed.add(i);
    });
  }
  assert.equal(olymMockUsed.size,300);

  const css=fs.readFileSync(path.join(root,'assets/refinement.css'),'utf8');
  assert(css.includes('size: A4 portrait')&&css.includes('.eg-omr-sheet')&&css.includes('.eg-scratch-box'));
  const js=fs.readFileSync(path.join(root,'assets/kaust-study.js'),'utf8');
  assert(js.includes('LOGO.jpg')&&js.includes('Edugates International School')&&js.includes('buildEdugatesOmrSheetHtml'));
  assert(fs.existsSync(path.join(root,'LOGO.jpg')));
  console.log('PASS: Static schema verified for 18 Nafes + 36 Kangaroo + 18 KAUST + 18 NSMO + 18 Olympiad lessons (324/324 concept SVGs) + 12 Nafes + 24 Kangaroo + 15 KAUST + 12 NSMO + 12 Olympiad Official Mock Exams (1,998 unique mock Qs), A4 CSS & Edugates OMR.');
})();
