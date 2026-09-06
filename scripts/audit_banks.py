"""Reproducible structural/content-risk audit. Does not certify mathematical correctness."""
import json,re,html,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def norm(s):
 s=re.sub(r'<svg\b.*?</svg>',' ',s,flags=re.S)
 return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s))).strip().lower()
def inspect(q,track,seen,ids):
 issues=[]
 if q.get('id') in ids:issues.append('duplicate_id')
 ids.add(q.get('id'))
 if q.get('track')!=track:issues.append('track_mismatch')
 stem=norm(q.get('content',{}).get('en',{}).get('question',''))
 if stem in seen:issues.append('duplicate_english_stem')
 seen.add(stem)
 for lang in ['en','ar']:
  c=q.get('content',{}).get(lang,{})
  for key in ['question','explanation']:
   if not c.get(key,'').strip():issues.append(f'{lang}_missing_{key}')
  if q.get('type')=='MCQ':
   opts=c.get('options',[])
   if len(opts)!=(5 if track=='kangaroo' else 4):issues.append(f'{lang}_option_count')
   if len(set(map(norm,opts)))!=len(opts):issues.append(f'{lang}_duplicate_options')
   try:
    k=int(q.get('correct_index',c.get('correct_index',-1)))
    if not 0<=k<len(opts):issues.append(f'{lang}_invalid_key')
   except (TypeError,ValueError):issues.append(f'{lang}_invalid_key')
 if q.get('type')!='MCQ':issues.append('written_response_requires_human_review')
 if re.search(r'<svg',q.get('content',{}).get('en',{}).get('question','')):issues.append('embedded_diagram_needs_question_specific_review')
 return issues

def main():
 out=[];summary=[]
 for p in sorted((ROOT/'data').glob('*.json')):
  qs=json.loads(p.read_text());seen=set();ids=set();counts=collections.Counter()
  for q in qs:
   issues=inspect(q,p.stem,seen,ids);counts.update(issues)
   out.append({'track':p.stem,'id':q.get('id'),'level':q.get('level'),'issues':issues,'semantic_review':'not_individually_certified'})
  summary.append({'track':p.stem,'total':len(qs),'levels':dict(collections.Counter(q['level'] for q in qs)),'issues':dict(counts)})
 (ROOT/'review').mkdir(exist_ok=True)
 (ROOT/'review/item-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'review/bank-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
