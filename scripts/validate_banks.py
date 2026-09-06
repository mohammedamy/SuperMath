"""Release gate for counts/schema plus independent finite-answer checks."""
import json,re,collections,math,itertools
from fractions import Fraction
from audit_banks import ROOT,norm
from build_practice import TARGETS
rows=[];total=0;generated=0;allids=set();independent=0
for track,levels in TARGETS.items():
 bank=json.loads((ROOT/'data'/f'{track}.json').read_text());stems=set();counts=collections.Counter()
 for q in bank:
  assert q['id'] not in allids,('duplicate id',q['id']);allids.add(q['id'])
  assert q['track']==track
  stem=norm(q['content']['en']['question']);assert stem not in stems,('duplicate stem',q['id']);stems.add(stem)
  counts[q['level']]+=1
  for lang in ['en','ar']:
   c=q['content'][lang];assert c['question'].strip() and c['explanation'].strip()
   assert '\\\\(' not in c['question']
   if q['type']=='MCQ':
    assert len(c['options'])==(5 if track=='kangaroo' else 4)
    assert len(set(map(norm,c['options'])))==len(c['options'])
    assert type(q['correct_index']) is int and 0<=q['correct_index']<len(c['options'])
    assert all('\\\\(' not in s for s in c['options'])
  if q.get('family_id'):
   generated+=1
   assert q['content']['en']['options']==q['content']['ar']['options']
   if q['type']=='MCQ':assert q['content']['en']['options'][q['correct_index']]=='\\( '+q['correct_answer']+' \\)'
   f=q['family_id'];s=q['content']['en']['question'];nums=list(map(int,re.findall(r'(?<![A-Za-z])\b\d+\b',s)))
   expected=None
   if f=='heads-and-legs':
    heads,legs=map(int,re.search(r'(\d+) heads and (\d+) legs',s).groups())
    solutions=[r for r in range(heads+1) if 4*r+2*(heads-r)==legs];assert len(solutions)==1;expected=solutions[0]
   elif f=='grid-border':
    w,h=map(int,re.search(r'(\d+) columns and (\d+) rows',s).groups())
    expected=sum(i in [0,w-1] or j in [0,h-1] for i in range(w) for j in range(h))
   elif f=='count-multiples-interval':
    lo,hi=map(int,re.search(r'from (\d+) through (\d+)',s).groups());expected=len([v for v in range(lo,hi+1) if v%3==0])
   elif f=='coprime-count':
    upper=int(re.search(r'1 to (\d+)',s).group(1));expected=sum(math.gcd(v,upper)==1 for v in range(1,upper+1))
   elif f=='committee-unordered':
    size=int(re.search(r'from (\d+) people',s).group(1));expected=sum(1 for _ in itertools.combinations(range(size),3))
   elif f=='grid-avoid-point':
    w,h=map(int,re.search(r'to \((\d+),(\d+)\)',s).groups());dp={(0,0):1}
    for i in range(w+1):
     for j in range(h+1):
      if (i,j)==(0,0):continue
      dp[i,j]=0 if (i,j)==(1,1) else dp.get((i-1,j),0)+dp.get((i,j-1),0)
    expected=dp[w,h]
   elif f=='without-replacement-pair':
    red,blue=map(int,re.search(r'(\d+) red and (\d+) blue',s).groups());balls=['r']*red+['b']*blue
    pairs=list(itertools.combinations(range(len(balls)),2));expected=Fraction(sum(balls[i]==balls[j]=='r' for i,j in pairs),len(pairs))
   elif f=='handshakes-graph':
    size=int(s.split()[0]);expected=sum(1 for i in range(size) for j in range(size) if i<j)
   if expected is not None:
    ans=q['correct_answer'];fm=re.fullmatch(r'\\frac\{(-?\d+)\}\{(\d+)\}',ans)
    actual=Fraction(int(fm[1]),int(fm[2])) if fm else Fraction(ans)
    assert actual==expected,(q['id'],actual,expected);independent+=1
  total+=1
 for level,minimum in levels.items():assert counts[level]>=minimum,(track,level,counts[level],minimum)
 rows.append({'track':track,'total':len(bank),'levels':dict(counts)})
# Independently verify corrected clock count, assignment minimum and periodic sequence.
clock=sum(max(collections.Counter(f'{h:02d}{m:02d}').values())>=3 for h in range(24) for m in range(60));assert clock==79
cost=[[9,2,7],[6,4,3],[5,8,1]];assert min(sum(cost[i][p[i]] for i in range(3)) for p in itertools.permutations(range(3)))==9
seq=[2,3]
for i in range(2,2024):seq.append(seq[-1]-seq[-2])
assert seq[-1]==3
result={'status':'passed','total':total,'parameterized_additions':generated,'independently_enumerated_generated_answers':independent,'scope_certification':False,'individual_review_of_every_legacy_answer':False,'banks':rows}
(ROOT/'review/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='banks'},indent=2))
