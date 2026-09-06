"""Draw only geometry encoded in the individual question, never keyword illustrations."""
import json,re
from audit_banks import ROOT
count=0
for path in (ROOT/'data').glob('*.json'):
 bank=json.loads(path.read_text())
 for q in bank:
  f=q.get('family_id');s=q['content']['en']['question'];body=None;w=300;h=200
  if f=='grid-border':
   cols,rows=map(int,re.search(r'(\d+) columns and (\d+) rows',s).groups());unit=20;w=cols*unit+40;h=rows*unit+40
   body=''.join(f'<rect x="{20+i*unit}" y="{20+j*unit}" width="{unit}" height="{unit}" fill="{("#e4edff" if i in (0,cols-1) or j in (0,rows-1) else "#ffffff")}" stroke="#536a8c"/>' for i in range(cols) for j in range(rows))
  elif f=='joined-squares-perimeter':
   n,side=map(int,re.search(r'(\d+) squares of side (\d+)',s).groups());unit=32;w=n*unit+40;h=92
   body=''.join(f'<rect x="{20+i*unit}" y="20" width="32" height="32" fill="#e4edff" stroke="#244c83" stroke-width="2"/>' for i in range(n))+f'<text x="20" y="78" fill="#172a46" font-size="16">{side} cm / سم</text>'
  elif f=='cut-corners-perimeter':
   side=int(re.search(r'side (\d+) cm',s).group(1));unit=20;edge=side*unit;w=edge+60;h=edge+60
   coords=[(unit,0),(edge-unit,0),(edge-unit,unit),(edge,unit),(edge,edge-unit),(edge-unit,edge-unit),(edge-unit,edge),(unit,edge),(unit,edge-unit),(0,edge-unit),(0,unit),(unit,unit)]
   pts=' '.join(f'{x+20},{y+20}' for x,y in coords)
   body=f'<rect x="20" y="20" width="{edge}" height="{edge}" fill="none" stroke="#889bb5" stroke-dasharray="5 5"/><polygon points="{pts}" fill="#e4edff" stroke="#244c83" stroke-width="2"/><text x="20" y="{edge+48}" fill="#172a46" font-size="16">{side} cm / سم</text>'
  elif q['id']=='NSMO-006':
   w=270;h=220
   body='<path d="M40 30 L40 174 L232 174 Z" fill="#e4edff" stroke="#244c83" stroke-width="2"/><path d="M40 158 H56 V174" fill="none" stroke="#244c83"/><text x="18" y="105" font-size="18" fill="#172a46">6</text><text x="130" y="200" font-size="18" fill="#172a46">8</text><text x="148" y="92" font-size="18" fill="#172a46">?</text>'
   q['difficulty']='Easy'
  if body:
   svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="Question geometry / رسم السؤال" style="display:block;max-width:100%;width:440px;max-height:320px;margin:16px auto;background:white;border-radius:8px"><title>Question-specific geometry / رسم مطابق لمعطيات السؤال</title>{body}</svg>'
   for lang in ['en','ar']:q['content'][lang]['diagram']=svg
   q['diagram_review']='constructed_from_question_dimensions';count+=1
 path.write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
print('Added',count,'question-specific diagrams.')
