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
for(const id of ['frq-answer-input','bank-notice','study-lessons','lesson-filter-pill'])elements.set(id,new El(id));
elements.get('practice').parentNode={insertBefore(){}};
elements.get('practice').children=[];
elements.get('print-include-solutions').checked=true;
const document={documentElement:new El('html'),body:new El('body'),activeElement:null,getElementById:id=>{assert(elements.has(id),'Unknown element '+id);return elements.get(id)},createElement:tag=>new El(tag),querySelectorAll:s=>s==='select'?[...elements.values()].filter(e=>e.id.includes('select')):[],querySelector:()=>new El('main'),addEventListener(){}};
elements.get('slider-q-count').value='1000';
const context=vm.createContext({document,console,Option:class{constructor(text,value){this.text=this.innerText=text;this.value=value}},Chart:class{constructor(ctx,opts){Object.assign(this,opts)}update(){}},matchMedia:()=>({matches:false}),localStorage:{setItem(){}},setTimeout:f=>f(),fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,url),'utf8'))})});
context.window=context;context.addEventListener=(name,fn)=>{if(name==='DOMContentLoaded')events.push(fn)};let prints=0;context.print=()=>prints++;
vm.runInContext(fs.readFileSync(path.join(root,'assets/practice-core.js'),'utf8'),context);
vm.runInContext(app,context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/refinement.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/kaust-study.js'),'utf8'),context);
const run=s=>vm.runInContext(s,context);
(async()=>{
 for(const callback of events)await callback();
 assert.equal(run('appData.questions.length'),4850);
 assert.equal(run('currentFilteredQuestions.length'),4850);
 // Switching away from a selected subtrack must not retain its hidden filter.
 elements.get('quiz-track-select').value='kaust';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),1350);
 assert(run('currentFilteredQuestions.every(q=>q.content.en.options.length===5&&q.content.ar.options.length===5)'));
 elements.get('quiz-kaust-phase-select').value='Track 1: Grades 6-7';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),450);
 elements.get('quiz-kaust-phase-select').value='Track 2: Grades 8-9';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),450);
 elements.get('quiz-kaust-phase-select').value='Track 3: Grades 10-11';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),450);
 elements.get('quiz-kaust-phase-select').value='all';context.filterQuestions();
 // KAUST KMC exclusively covers Grades 6-11 across its 3 official grade bands.
 for(const g of [1,2,3,4,5,12]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 KAUST questions`);
 }
 for(const [g,expectedLevel] of [[6,'Track 1: Grades 6-7'],[7,'Track 1: Grades 6-7'],[8,'Track 2: Grades 8-9'],[9,'Track 2: Grades 8-9'],[10,'Track 3: Grades 10-11'],[11,'Track 3: Grades 10-11']]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),450);
  assert(run(`currentFilteredQuestions.every(q=>q.level===${JSON.stringify(expectedLevel)})`));
 }
 context.setGradeFilter('all');
 // Verify KAUST geometry SVG diagram & 5-option (E) rendering in quiz card.
 elements.get('quiz-topic-select').value='Geometry';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),340);
 assert(elements.get('question-card-container').innerHTML.includes('<svg'));
 assert(elements.get('question-card-container').innerHTML.includes('>E<')||elements.get('question-card-container').innerHTML.includes('E\n'));
 elements.get('quiz-topic-select').value='all';context.filterQuestions();
 elements.get('quiz-track-select').value='nafes';context.filterQuestions();
 elements.get('quiz-nafes-grade-select').value='Grade 3';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),250);
 elements.get('quiz-track-select').value='jee';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),500);
 assert.equal(elements.get('quiz-nafes-grade-select').value,'all');
 // Grade filtering acts on questions, not merely the appearance of track cards.
 elements.get('quiz-track-select').value='kangaroo';context.setGradeFilter(4);
 assert.equal(run('currentFilteredQuestions.length'),250);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Ecolier")'));
 context.setGradeFilter('all');
 // NSMO is exclusively for grades 7, 8, 9, 10
 elements.get('quiz-track-select').value='nsmo';context.filterQuestions();
 assert.equal(run('currentFilteredQuestions.length'),750);
 for(const g of [5,6,11,12]){
  context.setGradeFilter(g);
  assert.equal(run('currentFilteredQuestions.length'),0,`Grade ${g} must yield 0 NSMO questions`);
 }
 context.setGradeFilter(7);
 assert.equal(run('currentFilteredQuestions.length'),250);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 1: Junior Olympiad (Grade 7)")'));
 context.setGradeFilter(8);
 assert.equal(run('currentFilteredQuestions.length'),250);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 2: Intermediate Olympiad (Grades 8-9)")'));
 context.setGradeFilter(9);
 assert.equal(run('currentFilteredQuestions.length'),250);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 2: Intermediate Olympiad (Grades 8-9)")'));
 context.setGradeFilter(10);
 assert.equal(run('currentFilteredQuestions.length'),250);
 assert(run('currentFilteredQuestions.every(q=>q.level==="Phase 3: Senior National Olympiad (Grade 10)")'));
 context.setGradeFilter('all');
 // Check correct and incorrect answers against keys; next question clears state.
 run('selectedOptionIdx=currentFilteredQuestions[0].correct_index');context.submitAnswer();assert(run('checkIsCorrect()'));
 context.nextQuestion();assert.equal(run('selectedOptionIdx'),null);assert.equal(run('isAnswerSubmitted'),false);
 // Written work survives a hint rerender and can reveal a solution without a fake mark.
 elements.get('quiz-track-select').value='olympiad';context.filterQuestions();
 run('selectedOptionIdx="My proof uses parity."');context.toggleHint();
 assert.equal(elements.get('frq-answer-input').value,'My proof uses parity.');
 context.submitAnswer();assert(elements.get('question-card-container').innerHTML.includes('self-assessment'));
 assert(!elements.get('question-card-container').innerHTML.includes('undefined'));
 // Printed FRQ keys must not become choice A from an old numeric placeholder.
 context.openPrintModal();elements.get('print-q-count').value='2';context.executePrint();
 assert.equal(prints,1);assert(!elements.get('print-container').innerHTML.includes('undefined'));
 assert(elements.get('print-container').innerHTML.includes('FRQ'));
 // Grade-level print bank size is exact.
 elements.get('print-track-select').value='kangaroo';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Junior';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,250);
 elements.get('print-track-select').value='nsmo';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Phase 1: Junior Olympiad (Grade 7)';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,250);
 elements.get('print-phase-select').value='Phase 3: Senior National Olympiad (Grade 10)';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,250);
 elements.get('print-track-select').value='kaust';context.updatePrintPhaseOptions();
 elements.get('print-phase-select').value='Track 1: Grades 6-7';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,450);
 elements.get('print-phase-select').value='Track 2: Grades 8-9';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,450);
 elements.get('print-phase-select').value='Track 3: Grades 10-11';context.updatePrintModalMax();
 assert.equal(elements.get('print-max-q').innerText,450);
 elements.get('print-q-count').value='15';context.executePrint();
 assert.equal(prints,2);assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.toggleLanguage();assert.equal(document.documentElement.dir,'rtl');
 context.toggleTheme();
 // A chart CDN failure should not prevent loading the practice banks.
 context.Chart=undefined;context.initCharts();
 // Verify KAUST Study Hub & Edugates A4 Print Frame runtime methods
 await new Promise(r=>setImmediate(r));
 assert.equal(run('window.__kaustStudy.lessons.length'),18);
 assert(elements.get('study-lessons').innerHTML.includes('Edugates International School'));
 context.openKaustLesson('KMC-L3-05');
 assert(elements.get('study-lessons').innerHTML.includes('<svg'));
 assert(!elements.get('study-lessons').innerHTML.includes('undefined'));
 context.practiceKaustLesson('KMC-L3-05');
 assert(run('currentFilteredQuestions.length')>50&&run('currentFilteredQuestions.every(q=>q.track==="kaust")'));
 context.clearKaustLessonFilter();
 const prevPrints=prints;
 context.printKaustLesson('KMC-L1-01');
 assert.equal(prints,prevPrints+1);
 assert(elements.get('print-container').innerHTML.includes('edugates-print-frame'));
 assert(elements.get('print-container').innerHTML.includes('LOGO.jpg'));
 assert(!elements.get('print-container').innerHTML.includes('undefined'));
 context.printKaustTrackBooklet('Track 2: Grades 8-9');
 assert.equal(prints,prevPrints+2);
 assert(elements.get('print-container').innerHTML.includes('eg-print-break'));
 console.log('PASS: startup, all counts, track switching, subtrack/grade filtering, MCQ marking, written work, print keys, KAUST study lessons & Edugates A4 print, Arabic and theme controls.');
 console.log('Runtime tests use lightweight DOM stubs; this is not browser or visual QA.');
})().catch(e=>{console.error(e);process.exitCode=1});

// ---- KAUST study lessons static schema test ----
(async()=>{
  const lessons=JSON.parse(fs.readFileSync(path.join(root,'data/kaust_lessons.json'),'utf8')).lessons;
  assert.equal(lessons.length,18);
  const ids=new Set(JSON.parse(fs.readFileSync(path.join(root,'data/kaust.json'),'utf8')).map(q=>q.id));
  for(const l of lessons){
    assert(l.en.examples.length>=4&&l.ar.examples.length>=4,l.id);
    assert.equal(l.bank_example_ids.length,5);
    l.bank_example_ids.forEach(i=>assert(ids.has(i),i));
    for(const e of l.en.examples)assert.equal(e.options.length,5);
  }
  const css=fs.readFileSync(path.join(root,'assets/refinement.css'),'utf8');
  assert(css.includes('size: A4 portrait'));
  const js=fs.readFileSync(path.join(root,'assets/kaust-study.js'),'utf8');
  assert(js.includes('LOGO.jpg')&&js.includes('Edugates International School'));
  assert(fs.existsSync(path.join(root,'LOGO.jpg')));
  console.log('PASS: 18 KAUST lessons (167 solved examples), A4 CSS, Edugates branded print frame.');
})();
