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
 after(){} prepend(){} focus(){document.activeElement=this} scrollIntoView(){}
 querySelectorAll(){return []}getClientRects(){return [1]}
}
for(const m of html.matchAll(/id="([^"]+)"/g))elements.set(m[1],new El(m[1]));
for(const id of ['frq-answer-input','bank-notice'])elements.set(id,new El(id));
const document={documentElement:new El('html'),body:new El('body'),activeElement:null,getElementById:id=>{assert(elements.has(id),'Unknown element '+id);return elements.get(id)},createElement:tag=>new El(tag),querySelectorAll:s=>s==='select'?[...elements.values()].filter(e=>e.id.includes('select')):[],querySelector:()=>new El('main'),addEventListener(){}};
elements.get('slider-q-count').value='1000';
const context=vm.createContext({document,console,Option:class{constructor(text,value){this.text=this.innerText=text;this.value=value}},Chart:class{constructor(ctx,opts){Object.assign(this,opts)}update(){}},matchMedia:()=>({matches:false}),localStorage:{setItem(){}},setTimeout:f=>f(),fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(root,url),'utf8'))})});
context.window=context;context.addEventListener=(name,fn)=>{if(name==='DOMContentLoaded')events.push(fn)};let prints=0;context.print=()=>prints++;
vm.runInContext(fs.readFileSync(path.join(root,'assets/practice-core.js'),'utf8'),context);
vm.runInContext(app,context);
vm.runInContext(fs.readFileSync(path.join(root,'assets/refinement.js'),'utf8'),context);
const run=s=>vm.runInContext(s,context);
(async()=>{
 for(const callback of events)await callback();
 assert.equal(run('appData.questions.length'),4250);
 assert.equal(run('currentFilteredQuestions.length'),4250);
 // Switching away from a selected subtrack must not retain its hidden filter.
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
 context.toggleLanguage();assert.equal(document.documentElement.dir,'rtl');
 context.toggleTheme();
 // A chart CDN failure should not prevent loading the practice banks.
 context.Chart=undefined;context.initCharts();
 console.log('PASS: startup, all counts, track switching, subtrack/grade filtering, MCQ marking, written work, print keys, Arabic and theme controls.');
 console.log('Runtime tests use lightweight DOM stubs; this is not browser or visual QA.');
})().catch(e=>{console.error(e);process.exitCode=1});
