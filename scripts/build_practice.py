"""Deterministic original practice variants. Family IDs make repetition explicit.
This generator verifies construction and answer keys, not official exam equivalence.
"""
import json,math,random,collections,itertools
from fractions import Fraction as F
from pathlib import Path
from audit_banks import ROOT,norm
R=random.Random(6092026)
def m(x):return '\\( '+str(x)+' \\)'
def val(x):
 if isinstance(x,F):return str(x.numerator) if x.denominator==1 else f'\\frac{{{x.numerator}}}{{{x.denominator}}}'
 return str(x)
def item(family,topic,en,ar,answer,solen,solar,diff='Medium',distractors=None):
 return dict(family=family,topic=topic,en=en,ar=ar,answer=answer,solen=solen,solar=solar,difficulty=diff,distractors=distractors)
def junior(k,n,g):
 a=R.randint(2,8+g);b=R.randint(2,7+g);c=R.randint(2,6);t=R.randint(2,5);x=R.randint(3,12+g)
 if k==0:
  total=a*b+c
  return item('equal-groups-leftover','Numbers and Operations',f'{a} identical boxes each contain the same number of counters. With {c} extra counters there are {total} counters altogether. How many are in each box?',f'تحتوي {a} علب متماثلة على العدد نفسه من القطع. ومع {c} قطع إضافية يصبح المجموع {total}. كم قطعة في كل علبة؟',b,f'Remove the extra counters, then divide: ({total} − {c}) ÷ {a} = {b}.',f'نطرح القطع الإضافية ثم نقسم: ({total} − {c}) ÷ {a} = {b}.','Easy')
 if k==1:
  d=R.randint(2,5);v=R.randint(2,9);terms=[v+d*i for i in range(4)]
  return item('constant-step-gap','Patterns',f'A sequence increases by the same amount each time: {terms[0]}, {terms[1]}, ?, {terms[3]}. Find the missing number.',f'تزداد المتتالية بمقدار ثابت: {terms[0]}، {terms[1]}، ؟، {terms[3]}. أوجد العدد الناقص.',terms[2],f'The step is {terms[1]} − {terms[0]} = {d}. Add it to {terms[1]} to get {terms[2]}.',f'الزيادة {terms[1]} − {terms[0]} = {d}. بإضافتها إلى {terms[1]} نحصل على {terms[2]}.','Easy')
 if k==2:
  return item('row-position','Logic',f'Sara is {a}th from the front and {b}th from the back of a line. How many people are in the line?',f'ترتيب سارة {a} من بداية صف و{b} من نهايته. كم شخصًا في الصف؟',a+b-1,f'Adding the positions counts Sara twice. Total = {a} + {b} − 1 = {a+b-1}.',f'جمع الترتيبين يحسب سارة مرتين. العدد = {a} + {b} − 1 = {a+b-1}.')
 if k==3:
  w=a+2;h=b+2
  return item('grid-border','Geometry',f'A rectangle of {w} columns and {h} rows is made of unit squares. How many squares touch its outer boundary?',f'مستطيل من مربعات وحدة به {w} أعمدة و{h} صفوف. كم مربعًا يلامس حدوده الخارجية؟',2*w+2*h-4,f'Top and bottom contribute 2×{w}. The middle rows contribute 2×({h}−2). Total {2*w+2*h-4}.',f'الصفان العلوي والسفلي يساهمان بـ2×{w}، والصفوف الوسطى بـ2×({h}−2). المجموع {2*w+2*h-4}.')
 if k==4:
  return item('joined-squares-perimeter','Geometry',f'{a} squares of side {b} cm are joined edge to edge in one straight row, with no gaps. What is the perimeter in cm?',f'وُصلت {a} مربعات طول ضلع كل منها {b} سم في صف مستقيم دون فراغات. ما المحيط بالسنتيمتر؟',2*b*(a+1),f'The row is a rectangle {a*b} cm long and {b} cm wide. Perimeter = 2({a*b}+{b}) = {2*b*(a+1)}.',f'ينتج مستطيل طوله {a*b} سم وعرضه {b} سم. المحيط = 2({a*b}+{b}) = {2*b*(a+1)}.')
 if k==5:
  ans=(a-1)*c;end=8*60+b*5;start=end-ans
  return item('intervals-not-objects','Measurement',f'{a} trees stand in one straight row. The gap between neighboring trees is {c} m. How far is the first tree from the last, in metres?',f'تقف {a} أشجار في صف مستقيم، والمسافة بين كل شجرتين متجاورتين {c} م. كم مترًا بين الأولى والأخيرة؟',ans,f'{a} trees create {a-1} gaps. Distance = {a-1} × {c} = {ans}.',f'عدد الفجوات {a-1}. المسافة = {a-1} × {c} = {ans}.','Easy')
 if k==6:
  nbox=c+1;nball=nbox*(a-1)+1
  return item('pigeonhole-guarantee','Logic',f'{nball} counters are placed in {nbox} boxes. What is the smallest number of counters that at least one box must contain?',f'وُزعت {nball} قطعة على {nbox} صناديق. ما أصغر عدد من القطع نضمن وجوده في صندوق واحد على الأقل؟',a,f'If every box had at most {a-1}, there would be at most {nbox*(a-1)} counters. Thus one has at least {a}. Distributing as evenly as possible attains this bound.',f'إذا احتوى كل صندوق على {a-1} قطع كحد أقصى فلن يتجاوز المجموع {nbox*(a-1)}. لذا يحتوي أحدها على {a} على الأقل، والتوزيع المتوازن يحقق هذا الحد.')
 if k==7:
  total=a*b;used=(a-1)*b
  return item('fraction-complement','Fractions',f'A ribbon is {total} cm long. A piece of length {used} cm is cut off. What fraction of the original ribbon remains?',f'طول شريط {total} سم، قُطعت منه قطعة طولها {used} سم. ما الكسر الذي يمثل الجزء المتبقي من الشريط الأصلي؟',F(1,a),f'The remaining length is {b} cm, so the fraction is {m(str(b)+"/"+str(total))} = {m(val(F(1,a)))}.',f'المتبقي {b} سم، إذن الكسر {m(str(b)+"/"+str(total))} = {m(val(F(1,a)))}.')
 if k==8:
  # Difference-and-total problem constructed with a unique integer solution.
  small=a;large=a+2*c;total=small+large
  return item('sum-and-difference','Algebra',f'Two baskets hold {total} apples altogether. One has {2*c} more apples than the other. How many apples are in the smaller basket?',f'في سلتين {total} تفاحة، وتزيد إحداهما على الأخرى بـ{2*c} تفاحات. كم تفاحة في السلة الأصغر؟',small,f'Remove the difference: {total}−{2*c}={2*small}. Divide equally between the two baskets to obtain {small}.',f'نطرح الفرق: {total}−{2*c}={2*small}، ثم نقسم على 2 فنحصل على {small}.')
 if k==9:
  red=a;blue=b;take=max(a,b)+1
  return item('guarantee-two-colours','Logic',f'A bag has {red} red and {blue} blue counters. Without looking, how many must you take to guarantee at least one of each colour?',f'في كيس {red} قطع حمراء و{blue} زرقاء. كم قطعة يجب سحبها دون نظر لضمان وجود قطعة من كل لون؟',take,f'You could first take all {max(a,b)} counters of the more numerous colour. One further counter guarantees the other colour: {take}.',f'قد تسحب أولًا القطع الـ{max(a,b)} من اللون الأكثر عددًا. قطعة أخرى تضمن اللون الثاني، أي {take}.')
 if k==10:
  days=c+2;ans=(n+days)%7
  return item('cycle-remainder','Patterns',f'A machine prints the repeating cycle 1, 2, 3, 4, 5, 6, 7, starting at 1. What number is printed in position {a*7+c}?',f'تطبع آلة الدورة المتكررة 1، 2، 3، 4، 5، 6، 7 بدءًا من 1. ما العدد في الموضع {a*7+c}؟',c,f'{a*7+c} = 7×{a}+{c}. After {a} complete cycles, the next position is {c}.',f'{a*7+c} = 7×{a}+{c}. بعد {a} دورات كاملة يكون الموضع التالي {c}.','Easy')
 if k==11:
  return item('heads-and-legs','Logic',f'A farm has chickens and rabbits: {a+b} heads and {2*a+4*b} legs. How many rabbits are there?',f'في مزرعة دجاج وأرانب، مجموع الرؤوس {a+b} والأرجل {2*a+4*b}. كم أرنبًا فيها؟',b,f'If all were chickens there would be {2*(a+b)} legs. The extra {2*b} legs come from rabbits, two extra legs each. Thus {b} rabbits.',f'لو كانت كلها دجاجًا لكان عدد الأرجل {2*(a+b)}. الزيادة {2*b}، ولكل أرنب رجلان إضافيتان؛ إذن عدد الأرانب {b}.')
 if k==12:
  lo=a*10;hi=lo+b*3
  ans=sum(i%3==0 for i in range(lo,hi+1))
  return item('count-multiples-interval','Number Theory',f'How many integers from {lo} through {hi}, including both endpoints, are divisible by 3?',f'كم عددًا صحيحًا من {lo} إلى {hi} شاملًا الطرفين يقبل القسمة على 3؟',ans,f'The first is {((lo+2)//3)*3} and the last is {(hi//3)*3}. Count the steps of 3 and add 1: {ans}.',f'أول مضاعف {((lo+2)//3)*3} وآخر مضاعف {(hi//3)*3}. نعد الفواصل بطول 3 ونضيف 1، فنحصل على {ans}.')
 if k==13:
  return item('reverse-two-operations','Algebra',f'I think of a number, multiply it by {c}, then add {a}. The result is {x*c+a}. What was my number?',f'فكرت في عدد، وضربته في {c} ثم أضفت {a} فكانت النتيجة {x*c+a}. ما العدد؟',x,f'Undo the operations in reverse order: ({x*c+a}−{a})÷{c}={x}.',f'نعكس العمليات: ({x*c+a}−{a})÷{c}={x}.','Easy')
 if k==14:
  return item('choice-product','Combinatorics',f'A café offers {a} sandwiches and {b} drinks. A meal contains one sandwich and one drink. How many different meals can be chosen?',f'يقدم مقهى {a} أنواع من الشطائر و{b} أنواع من المشروبات. تتكون الوجبة من شطيرة ومشروب. كم وجبة مختلفة يمكن اختيارها؟',a*b,f'Each of {a} sandwiches can be paired with any of {b} drinks, giving {a}×{b}={a*b}.',f'لكل شطيرة {b} اختيارات للمشروب، فيكون العدد {a}×{b}={a*b}.','Easy')
 if k==15:
  seq=[a,a+2,a+4,a+6];missing=a+8
  return item('mean-missing-observation','Statistics',f'The mean of five numbers is {a+4}. Four of them are {", ".join(map(str,seq))}. Find the fifth.',f'المتوسط الحسابي لخمسة أعداد {a+4}. أربعة منها هي {"، ".join(map(str,seq))}. أوجد الخامس.',missing,f'The total must be 5×{a+4}={5*(a+4)}. Subtract the known total {sum(seq)} to obtain {missing}.',f'المجموع المطلوب 5×{a+4}={5*(a+4)}. نطرح مجموع الأعداد المعروفة {sum(seq)} فنحصل على {missing}.')
 if k==16:
  return item('shared-edge-two-rectangles','Geometry',f'Two {a} cm by {b} cm rectangles are joined along a whole side of length {b} cm without overlap. What is the perimeter of the resulting rectangle?',f'وُصل مستطيلان أبعاد كل منهما {a} سم و{b} سم على طول ضلع كامل طوله {b} سم دون تداخل. ما محيط المستطيل الناتج؟',4*a+2*b,f'The new dimensions are {2*a} by {b}. Perimeter = 2({2*a}+{b})={4*a+2*b}.',f'الأبعاد الجديدة {2*a} و{b}. المحيط = 2({2*a}+{b})={4*a+2*b}.')
 if k==17:
  h=R.randint(8,11);minute=R.randint(0,5)*5;duration=a*5;end=h*60+minute+duration
  return item('elapsed-time','Measurement',f'A lesson starts at {h}:{minute:02d} a.m. and lasts {duration} minutes. How many minutes after 8:00 a.m. does it finish?',f'بدأ درس الساعة {h}:{minute:02d} صباحًا واستمر {duration} دقيقة. بعد كم دقيقة من الساعة 8:00 صباحًا ينتهي؟',end-480,f'The start is {(h-8)*60+minute} minutes after 8:00. Add {duration} to obtain {end-480}.',f'البداية بعد {(h-8)*60+minute} دقيقة من 8:00. نضيف {duration} فنحصل على {end-480}.')
 if k==18:
  return item('cut-corners-perimeter','Geometry',f'A square has side {a+2} cm. A 1 cm square is cut from each corner. What is the perimeter of the remaining shape, in cm?',f'مربع طول ضلعه {a+2} سم. قُطع مربع طول ضلعه 1 سم من كل ركن. ما محيط الشكل المتبقي بالسنتيمتر؟',4*(a+2),f'At each corner, two 1 cm boundary segments are removed and two 1 cm segments are added. The perimeter stays 4×{a+2}={4*(a+2)}.',f'عند كل ركن نحذف قطعتين طول كل منهما 1 سم ونضيف مثلهما. يبقى المحيط 4×{a+2}={4*(a+2)}.')
 if k==19:
  return item('balance-equal-objects','Algebra',f'A balanced scale has {c} identical blocks and a {a} g weight on one side, and a {c*x+a} g weight on the other. What is the mass of one block in grams?',f'في كفة ميزان متزن {c} مكعبات متماثلة وثقل {a} جم، وفي الأخرى ثقل {c*x+a} جم. ما كتلة المكعب بالجرام؟',x,f'The blocks together weigh {c*x+a}−{a}={c*x} g. Divide by {c}: {x} g.',f'كتلة المكعبات {c*x+a}−{a}={c*x} جم. بالقسمة على {c} نحصل على {x} جم.')
 raise ValueError(k)

def senior(k,n,g):
 a=R.randint(2,12);b=R.randint(2,10);c=R.randint(2,7);x=R.randint(2,12)
 if k==0:
  total=a+b+c
  return item('inclusion-exclusion-union','Sets',f'In a class of {total+5} students, {a+c} study French, {b+c} study Spanish, and {c} study both. How many study neither?',f'في فصل {total+5} طالبًا، يدرس {a+c} الفرنسية و{b+c} الإسبانية و{c} اللغتين. كم طالبًا لا يدرس أيًا منهما؟',5,f'The union has {a+c}+{b+c}−{c}={total} students. Subtract from {total+5}: 5.',f'عدد الاتحاد {a+c}+{b+c}−{c}={total}. نطرح من {total+5} فنحصل على 5.')
 if k==1:
  nset=a+1;ans=2**nset-2
  return item('nontrivial-subsets','Sets',f'A set has {nset} elements. How many subsets are neither empty nor equal to the whole set?',f'لمجموعة {nset} عنصرًا. كم مجموعة جزئية ليست خالية وليست مساوية للمجموعة الأصلية؟',ans,f'There are 2^{nset} subsets; exclude the empty set and whole set: 2^{nset}−2={ans}.',f'عدد المجموعات الجزئية 2^{nset}. نستبعد الخالية والأصلية: 2^{nset}−2={ans}.')
 if k==2:
  ans=a*a+b*b
  return item('quadratic-root-squares','Quadratic Equations',f'If α and β are the roots of {m(f"z^2-{a+b}z+{a*b}=0")}, find {m("α^2+β^2")} .',f'إذا كان α وβ جذري المعادلة {m(f"z^2-{a+b}z+{a*b}=0")}، أوجد {m("α^2+β^2")} .',ans,f'Vieta gives α+β={a+b} and αβ={a*b}. Hence α²+β²=({a+b})²−2({a*b})={ans}.',f'من علاقات فييتا α+β={a+b} وαβ={a*b}. إذن α²+β²=({a+b})²−2({a*b})={ans}.')
 if k==3:
  ans=a*a+b*b
  return item('complex-conjugate-product','Complex Numbers',f'Let {m(f"z={a}+{b}i")}. Find {m("z\\overline{z}")} .',f'ليكن {m(f"z={a}+{b}i")}. أوجد {m("z\\overline{z}")} .',ans,f'z times its conjugate equals |z|²={a}²+{b}²={ans}.',f'حاصل ضرب العدد في مرافقه يساوي مربع معياره: {a}²+{b}²={ans}.','Easy')
 if k==4:
  ans=a*c-b
  return item('determinant-parameter','Matrices and Determinants',f'The determinant of {m(f"\\begin{{pmatrix}}{a}&1\\\\{b}&t\\end{{pmatrix}}") } is {ans}. Find t.',f'محدد المصفوفة {m(f"\\begin{{pmatrix}}{a}&1\\\\{b}&t\\end{{pmatrix}}")} يساوي {ans}. أوجد t.',c,f'The determinant is {a}t−{b}. Thus {a}t={ans+b}, giving t={c}.',f'المحدد {a}t−{b}. إذن {a}t={ans+b}، ومنه t={c}.')
 if k==5:
  people=a+3;ans=math.comb(people,3)
  return item('committee-unordered','Combinatorics',f'How many three-person committees can be formed from {people} people, with no roles assigned?',f'كم لجنة من ثلاثة أشخاص يمكن تشكيلها من {people} شخصًا دون توزيع مناصب؟',ans,f'Order does not matter, so use combinations: {people}×{people-1}×{people-2}/6={ans}.',f'الترتيب غير مهم؛ نستخدم التوافيق: {people}×{people-1}×{people-2}/6={ans}.')
 if k==6:
  degree=a+2;ans=math.comb(degree,2)*b*b
  return item('binomial-coefficient','Binomial Theorem',f'Find the coefficient of {m("x^2")} in {m(f"(1+{b}x)^{{{degree}}}")} .',f'أوجد معامل {m("x^2")} في مفكوك {m(f"(1+{b}x)^{{{degree}}}")} .',ans,f'Choose the x term from two factors: C({degree},2)×{b}²={ans}.',f'نختار حد x من عاملين: C({degree},2)×{b}²={ans}.')
 if k==7:
  terms=a+4;ans=F(terms*(2*b+(terms-1)*c),2)
  return item('arithmetic-series','Sequences',f'An arithmetic progression starts with {b} and has common difference {c}. Find the sum of its first {terms} terms.',f'متتابعة حسابية حدها الأول {b} وفرقها {c}. أوجد مجموع أول {terms} حدًا.',ans,f'The last term is {b+(terms-1)*c}. Sum = {terms}({b}+{b+(terms-1)*c})/2={val(ans)}.',f'الحد الأخير {b+(terms-1)*c}. المجموع = {terms}({b}+{b+(terms-1)*c})/2={val(ans)}.')
 if k==8:
  ans=F(a*b,b-1)
  return item('geometric-infinite','Sequences',f'Find the sum of the infinite geometric series with first term {a} and common ratio {m(val(F(1,b)))}.',f'أوجد مجموع المتسلسلة الهندسية غير المنتهية التي حدها الأول {a} وأساسها {m(val(F(1,b)))}.',ans,f'The ratio has absolute value below 1, so S=a/(1−r)={m(val(ans))}.',f'القيمة المطلقة للأساس أقل من 1، لذا المجموع a/(1−r)={m(val(ans))}.')
 if k==9:
  ans=2*a
  return item('removable-discontinuity','Limits and Continuity',f'For x≠{a}, {m(f"f(x)=\\frac{{x^2-{a*a}}}{{x-{a}}}")}. What value of f({a}) makes f continuous?',f'عندما x≠{a}، تكون {m(f"f(x)=\\frac{{x^2-{a*a}}}{{x-{a}}}")}. ما قيمة f({a}) التي تجعل الدالة متصلة؟',ans,f'Factor x²−{a*a}=(x−{a})(x+{a}). Away from the missing point f(x)=x+{a}, whose limit is {2*a}.',f'نحلل البسط إلى (x−{a})(x+{a})، فتكون الدالة x+{a} خارج النقطة المحذوفة، ونهايتها {2*a}.')
 if k==10:
  ans=3*a*x*x+2*b*x+c
  return item('polynomial-tangent-slope','Differential Calculus',f'Find the slope of the tangent to {m(f"y={a}x^3+{b}x^2+{c}x")} at x={x}.',f'أوجد ميل المماس للمنحنى {m(f"y={a}x^3+{b}x^2+{c}x")} عند x={x}.',ans,f'Differentiate: y′={3*a}x²+{2*b}x+{c}. At x={x}, the slope is {ans}.',f'بالتفاضل y′={3*a}x²+{2*b}x+{c}. عند x={x} يكون الميل {ans}.')
 if k==11:
  ans=F(a,3)+F(b,2)+c
  return item('integral-polynomial','Integral Calculus',f'Evaluate {m(f"\\int_0^1 ({a}x^2+{b}x+{c})\\,dx")} .',f'احسب {m(f"\\int_0^1 ({a}x^2+{b}x+{c})\\,dx")} .',ans,f'Integrate term by term and evaluate at 1 and 0: {a}/3+{b}/2+{c}={m(val(ans))}.',f'نكامل حدًا حدًا ونعوض بالحدين 1 و0: {a}/3+{b}/2+{c}={m(val(ans))}.')
 if k==12:
  ans=a*x*x+b
  return item('initial-value-polynomial','Differential Equations',f'A function satisfies {m(f"y'={2*a}x")} and y(0)={b}. Find y({x}).',f'تحقق دالة {m(f"y'={2*a}x")} وy(0)={b}. أوجد y({x}).',ans,f'Integrating gives y={a}x²+C. The initial value gives C={b}. Thus y({x})={ans}.',f'بالتكامل y={a}x²+C، والشرط الابتدائي يعطي C={b}. إذن y({x})={ans}.')
 if k==13:
  ans=(a+b)/2
  return item('line-intercept-triangle','Coordinate Geometry',f'A line joins ({2*a},0) and (0,{2*b}). Find the area of the triangle it forms with the coordinate axes.',f'يصل مستقيم بين ({2*a}،0) و(0،{2*b}). أوجد مساحة المثلث الذي يكونه مع محوري الإحداثيات.',2*a*b,f'The perpendicular base and height are {2*a} and {2*b}. Area = ½×{2*a}×{2*b}={2*a*b}.',f'القاعدة والارتفاع المتعامدان {2*a} و{2*b}. المساحة = ½×{2*a}×{2*b}={2*a*b}.')
 if k==14:
  ans=a*a+b*b+c*c
  return item('space-distance-squared','3D Geometry',f'Find the square of the distance between P(1,2,3) and Q({a+1},{b+2},{c+3}).',f'أوجد مربع المسافة بين P(1،2،3) وQ({a+1}،{b+2}،{c+3}).',ans,f'The coordinate differences are {a},{b},{c}; squared distance is {a}²+{b}²+{c}²={ans}.',f'فروق الإحداثيات {a} و{b} و{c}؛ مربع المسافة {a}²+{b}²+{c}²={ans}.')
 if k==15:
  ans=-(a+b)
  return item('orthogonal-vector-parameter','Vectors',f'The vectors ({a},{b},1) and (1,1,t) are perpendicular. Find t.',f'المتجهان ({a}،{b}،1) و(1،1،t) متعامدان. أوجد t.',ans,f'Perpendicular vectors have dot product zero: {a}+{b}+t=0, so t={ans}.',f'الضرب القياسي لمتجهين متعامدين يساوي صفرًا: {a}+{b}+t=0، ومنه t={ans}.')
 if k==16:
  ans=F(a*(a-1),(a+b)*(a+b-1))
  return item('without-replacement-pair','Probability',f'A bag contains {a} red and {b} blue balls. Two are drawn uniformly without replacement. What is the probability both are red?',f'في كيس {a} كرات حمراء و{b} زرقاء. سُحبت كرتان عشوائيًا دون إرجاع. ما احتمال أن تكونا حمراوين؟',ans,f'Multiply the conditional probabilities: {a}/{a+b} × {a-1}/{a+b-1} = {m(val(ans))}.',f'نضرب الاحتمالين الشرطيين: {a}/{a+b} × {a-1}/{a+b-1} = {m(val(ans))}.')
 if k==17:
  ans=F(2*b*b,3)
  return item('population-variance','Statistics',f'Find the population variance of {a-b}, {a}, {a+b}.',f'أوجد تباين المجتمع للأعداد {a-b} و{a} و{a+b}.',ans,f'The mean is {a}. The squared deviations are {b*b},0,{b*b}. Divide their sum by 3: {m(val(ans))}.',f'المتوسط {a}، ومربعات الانحرافات {b*b} و0 و{b*b}. نقسم مجموعها على 3: {m(val(ans))}.')
 if k==18:
  ans=F(2*a*b,a*a+b*b)
  return item('trig-double-angle','Trigonometry',f'For an acute angle θ, {m(f"\\tan θ={val(F(a,b))}")}. Find {m("\\sin 2θ")} .',f'لزاوية حادة θ، {m(f"\\tan θ={val(F(a,b))}")}. أوجد {m("\\sin 2θ")} .',ans,f'Use sin(2θ)=2tanθ/(1+tan²θ). Substitution gives {m(val(ans))}.',f'نستخدم sin(2θ)=2tanθ/(1+tan²θ). بالتعويض نحصل على {m(val(ans))}.')
 if k==19:
  mod=R.choice([5,7,11,13,17]);exp=a+5;ans=pow(b,exp,mod)
  return item('power-modulo','Number Theory',f'Find the remainder when {m(f"{b}^{{{exp}}}")} is divided by {mod}.',f'أوجد باقي قسمة {m(f"{b}^{{{exp}}}")} على {mod}.',ans,f'Reduce successive products modulo {mod}. The residues of powers 1 through {exp} are '+', '.join(str(pow(b,j,mod)) for j in range(1,exp+1))+f'. The last residue is {ans}.',f'نختزل الضرب المتكرر بترديد {mod}. بواقي القوى من 1 إلى {exp} هي '+ '، '.join(str(pow(b,j,mod)) for j in range(1,exp+1))+f'. الباقي الأخير {ans}.')
 if k==20:
  w=a+2;h=b+2;u=1;v=1;ans=math.comb(w+h,w)-math.comb(2,1)*math.comb(w+h-2,w-1)
  return item('grid-avoid-point','Combinatorics',f'A path from (0,0) to ({w},{h}) uses only unit steps right or up. How many such paths avoid (1,1)?',f'مسار من (0،0) إلى ({w}،{h}) يستخدم خطوات وحدة يمينًا أو إلى أعلى فقط. كم مسارًا لا يمر بالنقطة (1،1)؟',ans,f'All paths: C({w+h},{w})={math.comb(w+h,w)}. Paths through (1,1): 2×C({w+h-2},{w-1})={2*math.comb(w+h-2,w-1)}. Subtract to get {ans}.',f'كل المسارات: C({w+h}،{w})={math.comb(w+h,w)}. المارة بالنقطة (1،1): 2×C({w+h-2}،{w-1})={2*math.comb(w+h-2,w-1)}. بالطرح نحصل على {ans}.','Hard')
 if k==21:
  ans=sum(math.gcd(i,a*b)==1 for i in range(1,a*b+1))
  factors=[p for p in range(2,a*b+1) if a*b%p==0 and all(p%d for d in range(2,math.isqrt(p)+1))]
  return item('coprime-count','Number Theory',f'How many integers from 1 to {a*b} inclusive are relatively prime to {a*b}?',f'كم عددًا صحيحًا من 1 إلى {a*b} شاملًا الطرفين أولي نسبيًا مع {a*b}؟',ans,f'The distinct prime factors are {factors}. Euler’s product gives φ({a*b}) = {a*b} × '+ ' × '.join(f'(1−1/{p})' for p in factors)+f' = {ans}.',f'العوامل الأولية المختلفة {factors}. باستخدام دالة أويلر: φ({a*b}) = {a*b} × '+' × '.join(f'(1−1/{p})' for p in factors)+f' = {ans}.','Hard')
 if k==22:
  ans=(a+b)**2
  return item('fixed-sum-minimum-square','Inequalities',f'Positive real numbers x and y satisfy x+y={2*(a+b)}. Find the smallest possible value of {m("(x^2+y^2)/2")} .',f'عددان حقيقيان موجبان x وy يحققان x+y={2*(a+b)}. أوجد أصغر قيمة لـ{m("(x^2+y^2)/2")} .',ans,f'From (x−y)²≥0, (x²+y²)/2≥((x+y)/2)²={ans}. Equality is attained at x=y={a+b}.',f'من (x−y)²≥0 نحصل على (x²+y²)/2≥((x+y)/2)²={ans}. تتحقق المساواة عندما x=y={a+b}.')
 if k==23:
  ans=F(a+b,c)
  return item('rational-equation-exclusion','Algebra',f'Solve {m(f"\\frac{{{a}}}{{x}}+\\frac{{{b}}}{{x}}={c}")} for real x≠0.',f'حل المعادلة {m(f"\\frac{{{a}}}{{x}}+\\frac{{{b}}}{{x}}={c}")} حيث x حقيقي لا يساوي صفرًا.',ans,f'Combine the fractions: {a+b}/x={c}. Multiply by x and divide by {c}: x={m(val(ans))}, which is nonzero.',f'بجمع الكسرين {a+b}/x={c}. نضرب في x ونقسم على {c}: x={m(val(ans))}، وهي قيمة غير صفرية.')
 if k==24:
  total=a+5;ans=total*(total-1)//2
  return item('handshakes-graph','Combinatorics',f'{total} people each shake hands with every other person exactly once. How many handshakes occur?',f'يتصافح {total} شخصًا بحيث يصافح كل منهم جميع الآخرين مرة واحدة. كم مصافحة تحدث؟',ans,f'Each person has {total-1} partners. Dividing the total {total}({total-1}) by 2 prevents counting each handshake twice: {ans}.',f'لكل شخص {total-1} شريكًا. نقسم {total}({total-1}) على 2 لعدم حساب المصافحة مرتين: {ans}.')
 if k==25:
  ans=math.gcd(a*b,a*c)
  return item('greatest-square-tiling','Number Theory',f'A {a*b} cm by {a*c} cm rectangle is tiled with identical squares of integer side length, aligned with its sides, without cuts. What is the largest possible square side length?',f'نغطي مستطيلًا أبعاده {a*b} سم و{a*c} سم بمربعات متطابقة أطوال أضلاعها أعداد صحيحة، موازية لأضلاعه ودون قص. ما أكبر طول ممكن لضلع المربع؟',ans,f'The side must divide both dimensions. Their greatest common divisor is gcd({a*b},{a*c})={ans}.',f'يجب أن يقسم طول الضلع البعدين. القاسم المشترك الأكبر gcd({a*b}،{a*c})={ans}.')
 raise ValueError(k)

def proof(k,n):
 a=R.randint(2,18);b=R.randint(2,17);c=R.randint(2,9)
 def q(f,t,en,ar,se,sa,d='Medium'):return item(f,t,en,ar,None,se,sa,d)
 if k==0:
  return q('proof-divisibility-remainder','Number Theory',f'Find all positive integers n for which n+{a} divides n²+{b}. Prove that your list is complete.',f'أوجد جميع الأعداد الصحيحة الموجبة n التي يكون فيها n+{a} قاسمًا لـn²+{b}. أثبت اكتمال قائمتك.',f'Modulo n+{a}, n≡−{a}, so n²+{b}≡{a*a+b}. Therefore n+{a} must be a positive divisor d of {a*a+b} with d>{a}. Conversely every such divisor works. The complete list is '+', '.join(str(d-a) for d in range(a+1,a*a+b+1) if (a*a+b)%d==0)+'.',f'بترديد n+{a} لدينا n≡−{a}، ومن ثم n²+{b}≡{a*a+b}. إذن n+{a} قاسم موجب d للعدد {a*a+b} وd>{a}. والعكس صحيح لكل قاسم كهذا. القائمة الكاملة: '+'، '.join(str(d-a) for d in range(a+1,a*a+b+1) if (a*a+b)%d==0)+'.')
 if k==1:
  return q('proof-reciprocal-diophantine','Number Theory',f'Find all ordered pairs of positive integers (x,y) satisfying 1/x+1/y=1/{a}. Justify completeness.',f'أوجد جميع الأزواج المرتبة من الأعداد الصحيحة الموجبة (x،y) التي تحقق 1/x+1/y=1/{a}. برر اكتمال الحل.',f'Clearing denominators and factoring gives (x−{a})(y−{a})={a*a}. Each variable is greater than {a}, since its reciprocal is smaller than 1/{a}. For each positive divisor d of {a*a}, x={a}+d and y={a}+{a*a}/d. These and only these pairs work.',f'بتوحيد المقامات والتحليل نجد (x−{a})(y−{a})={a*a}. كل متغير أكبر من {a} لأن مقلوبه أصغر من 1/{a}. لكل قاسم موجب d للعدد {a*a} نأخذ x={a}+d وy={a}+{a*a}/d. هذه الأزواج كلها تحقق المعادلة ولا توجد غيرها.')
 if k==2:
  return q('proof-close-factor-squares','Number Theory',f'Find all integers x,y with x²−y²={4*a}. Give a complete parameterization.',f'أوجد جميع الأعداد الصحيحة x وy التي تحقق x²−y²={4*a}. أعط تمثيلًا كاملاً للحلول.',f'Write u=x−y and v=x+y. Then uv={4*a} and u,v have the same parity. Conversely, for every ordered integer factor pair (u,v) of {4*a} with the same parity, x=(u+v)/2 and y=(v−u)/2 are integers solving the equation. This includes negative factor pairs and proves completeness.',f'ضع u=x−y وv=x+y. إذن uv={4*a} ولهما التكافؤ نفسه. والعكس: لكل زوج عوامل صحيح مرتب (u،v) للعدد {4*a} ولهما التكافؤ نفسه، فإن x=(u+v)/2 وy=(v−u)/2 حلان صحيحان. نضم أزواج العوامل السالبة، فيكون التمثيل كاملاً.')
 if k==3:
  return q('proof-consecutive-selection','Combinatorics',f'Prove that any choice of {a+1} distinct integers from 1 through {2*a} contains two consecutive integers. Show that {a} choices need not have this property.',f'أثبت أن اختيار {a+1} عددًا مختلفًا من 1 إلى {2*a} يضمن وجود عددين متتاليين. وبيّن أن اختيار {a} أعداد لا يضمن ذلك.',f'Partition into {a} pairs (1,2),(3,4),…,({2*a-1},{2*a}). By the pigeonhole principle, {a+1} choices put both elements in one pair. Choosing all odd numbers gives {a} choices with no consecutive pair, so the bound is sharp.',f'نقسم الأعداد إلى {a} أزواج (1،2)، (3،4)، …، ({2*a-1}،{2*a}). بمبدأ الحمام يضع اختيار {a+1} عددًا عنصرين في زوج واحد. اختيار جميع الأعداد الفردية يعطي {a} أعداد دون متتاليين، فالحد حاد.')
 if k==4:
  return q('proof-equal-remainders','Combinatorics',f'Prove that among any {a+1} integers, two have a difference divisible by {a}. Is the number {a+1} best possible?',f'أثبت أنه من بين أي {a+1} عددًا صحيحًا يوجد عددان فرقهما يقبل القسمة على {a}. هل العدد {a+1} هو أصغر ضمان ممكن؟',f'There are {a} residue classes modulo {a}. Two of {a+1} integers share a class, so their difference is divisible by {a}. The {a} integers 0,1,…,{a-1} have different residues, showing optimality.',f'يوجد {a} فئات بواقٍ بترديد {a}. من بين {a+1} عددًا يتساوى باقي عددين، فيقبل فرقهما القسمة على {a}. والأعداد {a} من 0 إلى {a-1} بواقيها مختلفة، مما يثبت أن الحد هو الأفضل.')
 if k==5:
  return q('proof-divisible-subsequence','Number Theory',f'Given any sequence of {a} integers, prove that some nonempty consecutive block has sum divisible by {a}.',f'أثبت أنه في أي متتالية من {a} عددًا صحيحًا توجد كتلة متتالية غير خالية مجموعها يقبل القسمة على {a}.',f'Consider the {a} prefix sums. If one is 0 modulo {a}, that prefix works. Otherwise they lie in the {a-1} nonzero residue classes, so two share a residue. Their difference is the sum of the nonempty block between their endpoints and is divisible by {a}.',f'ننظر إلى المجاميع الجزئية الـ{a}. إذا كان أحدها صفرًا بترديد {a} فقد وجدنا الكتلة. وإلا فهي موزعة على {a-1} باقيًا غير صفري، فيتساوى باقي مجموعين. فرقهما مجموع كتلة متتالية غير خالية ويقبل القسمة على {a}.','Hard')
 if k==6:
  return q('proof-symmetric-quadratic-bound','Inequalities',f'For real x,y with x+y={2*a}, prove x²+y²≥{2*a*a} and determine exactly when equality holds.',f'لعددين حقيقيين x وy يحققان x+y={2*a}، أثبت x²+y²≥{2*a*a} وحدد شرط المساواة بدقة.',f'Use 2(x²+y²)=(x+y)²+(x−y)²≥{4*a*a}. Divide by 2. Equality requires x=y; together with the sum condition this gives x=y={a}.',f'لدينا 2(x²+y²)=(x+y)²+(x−y)²≥{4*a*a}. نقسم على 2. تتطلب المساواة x=y، ومع شرط المجموع نحصل على x=y={a}.')
 if k==7:
  return q('proof-reciprocal-bound','Inequalities',f'Positive x,y satisfy xy={a*a}. Prove x+y≥{2*a} and 1/x+1/y≥{m(val(F(2,a)))}. Find all equality cases.',f'عددان موجبان x وy يحققان xy={a*a}. أثبت x+y≥{2*a} و1/x+1/y≥{m(val(F(2,a)))}. حدد جميع حالات المساواة.',f'Because (√x−√y)²≥0, x+y≥2√(xy)={2*a}. Also 1/x+1/y=(x+y)/{a*a}≥{m(val(F(2,a)))}. Both equalities hold exactly at x=y={a}.',f'من (√x−√y)²≥0 نجد x+y≥2√(xy)={2*a}. كذلك 1/x+1/y=(x+y)/{a*a}≥{m(val(F(2,a)))}. تتحقق المساواتان فقط عند x=y={a}.')
 if k==8:
  return q('proof-weighted-square','Inequalities',f'For real x,y, prove {a}x²+{b}y²≥{m(val(F(a*b,a+b)))}(x+y)². Determine the equality condition.',f'لعددين حقيقيين x وy، أثبت {a}x²+{b}y²≥{m(val(F(a*b,a+b)))}(x+y)². حدد شرط المساواة.',f'Multiply by {a+b}. The difference between the two sides becomes ({a}x−{b}y)²≥0. Equality holds exactly when {a}x={b}y.',f'نضرب في {a+b}. يصبح الفرق بين الطرفين ({a}x−{b}y)²≥0. تتحقق المساواة إذا وفقط إذا {a}x={b}y.')
 if k==9:
  return q('proof-product-fixed-sum','Algebra',f'Real x,y satisfy x+y={2*a}. Find the greatest possible value of xy, and prove it is attained.',f'عددان حقيقيان x وy يحققان x+y={2*a}. أوجد أكبر قيمة لـxy وأثبت تحققها.',f'(x−y)²≥0 implies 4xy≤(x+y)²={4*a*a}. Thus xy≤{a*a}. Equality is attained at x=y={a}.',f'من (x−y)²≥0 نجد 4xy≤(x+y)²={4*a*a}. إذن xy≤{a*a}. وتتحقق المساواة عند x=y={a}.')
 if k==10:
  return q('proof-affine-functional-equation','Functional Equations',f'Find all functions f:ℝ→ℝ such that f(x+y)=f(x)+{a}y for every real x,y, and f(0)={b}. Prove your answer.',f'أوجد جميع الدوال f:ℝ→ℝ التي تحقق f(x+y)=f(x)+{a}y لكل x وy حقيقيين، وf(0)={b}. أثبت جوابك.',f'Set x=0 to obtain f(y)={b}+{a}y for every y, so this is the only possible function. Substitution gives f(x+y)={a}x+{a}y+{b}=f(x)+{a}y and f(0)={b}, proving sufficiency.',f'بوضع x=0 نحصل على f(y)={b}+{a}y لكل y، فتلك الدالة الوحيدة المحتملة. بالتعويض f(x+y)={a}x+{a}y+{b}=f(x)+{a}y وf(0)={b}، مما يثبت الكفاية.')
 if k==11:
  return q('proof-integer-recurrence','Functional Equations',f'A function f:ℤ→ℤ satisfies f(0)={b} and f(n+1)−f(n)={2*a}n+{a} for every integer n. Find f(n) for all integers and prove uniqueness.',f'تحقق دالة f:ℤ→ℤ الشرطين f(0)={b} وf(n+1)−f(n)={2*a}n+{a} لكل عدد صحيح n. أوجد f(n) لجميع الأعداد الصحيحة وأثبت الوحدانية.',f'The candidate is f(n)={a}n²+{b}, whose forward difference is {a}(2n+1). It has the correct value at zero. The recurrence determines each next value and each previous value, so induction in both directions proves uniqueness on ℤ.',f'الدالة المقترحة f(n)={a}n²+{b}، وفرقها الأمامي {a}(2n+1)، وقيمتها عند الصفر صحيحة. العلاقة تحدد القيمة التالية والسابقة، فالاستقراء في الاتجاهين يثبت الوحدانية على ℤ.')
 if k==12:
  return q('proof-odd-sum-induction','Number Theory',f'Prove for every positive integer n that the sum of the first n terms of {a}, {3*a}, {5*a}, … equals {a}n².',f'أثبت لكل عدد صحيح موجب n أن مجموع أول n حدًا من {a}، {3*a}، {5*a}، … يساوي {a}n².',f'For n=1 the result holds. If the first n terms sum to {a}n², adding {a}(2n+1) gives {a}(n²+2n+1)={a}(n+1)². Induction completes the proof.',f'عند n=1 تصح النتيجة. إذا كان مجموع أول n حدًا {a}n²، فبإضافة {a}(2n+1) يصبح المجموع {a}(n²+2n+1)={a}(n+1)². يكتمل البرهان بالاستقراء.')
 if k==13:
  return q('proof-coprime-consecutive-affine','Number Theory',f'Prove that for every integer n, any common positive divisor of {a}n+1 and {a}n+{a+1} must divide {a}, and deduce that the two numbers are coprime.',f'أثبت أنه لكل عدد صحيح n، كل قاسم موجب مشترك للعددين {a}n+1 و{a}n+{a+1} يقسم {a}، واستنتج أن العددين أوليان نسبيًا.',f'A common divisor d divides their difference {a}. It therefore divides {a}n. Since it also divides {a}n+1, it divides 1. Thus d=1, proving coprimality.',f'يقسم القاسم المشترك d الفرق {a}، فيقسم {a}n. وبما أنه يقسم {a}n+1 فهو يقسم 1؛ إذن d=1 ويكون العددان أوليين نسبيًا.')
 if k==14:
  return q('proof-similar-triangle-area','Geometry',f'In triangle ABC, points D on AB and E on AC satisfy AD/AB=AE/AC={m(val(F(a,a+b)))}. Prove DE∥BC and find the ratio of the areas of triangles ADE and ABC.',f'في المثلث ABC، النقطتان D على AB وE على AC تحققان AD/AB=AE/AC={m(val(F(a,a+b)))}. أثبت DE∥BC وأوجد نسبة مساحتي ADE وABC.',f'The included angle at A is common and the adjacent side ratios agree, so SAS similarity gives ADE∼ABC. Corresponding angles imply DE∥BC. Areas scale as the square of the side ratio, giving {m(val(F(a*a,(a+b)**2)))}.',f'الزاوية المحصورة عند A مشتركة ونسبتا الضلعين متساويتان، فيتشابه ADE وABC بضلعين والزاوية المحصورة. تساوي الزوايا المتناظرة يعطي DE∥BC. نسبة المساحتين مربع نسبة الأطوال، أي {m(val(F(a*a,(a+b)**2)))}.')
 if k==15:
  return q('proof-median-area-split','Geometry',f'In triangle ABC, D lies on BC with BD:DC={a}:{b}. Prove that area(ABD):area(ACD)={a}:{b}.',f'في المثلث ABC تقع D على BC بحيث BD:DC={a}:{b}. أثبت أن مساحة ABD إلى مساحة ACD تساوي {a}:{b}.',f'Both triangles have the same perpendicular height from A to line BC. Using area=½×base×height, their area ratio equals BD/DC={a}/{b}.',f'للمثلثين الارتفاع العمودي نفسه من A إلى المستقيم BC. وباستخدام المساحة=½×القاعدة×الارتفاع تكون نسبة المساحتين BD/DC={a}/{b}.')
 if k==16:
  return q('proof-polygon-diagonals','Combinatorics',f'Find the number of diagonals in a convex {a+3}-gon. Prove your counting formula without counting an edge as a diagonal.',f'أوجد عدد أقطار مضلع محدب له {a+3} ضلعًا. أثبت صيغة العد دون حساب الأضلاع أقطارًا.',f'Each vertex connects by a diagonal to {a} vertices, excluding itself and its two neighbors. Multiplying by {a+3} counts each diagonal twice, so the answer is {((a+3)*a)//2}.',f'يتصل كل رأس بقطر إلى {a} رؤوس بعد استبعاد نفسه وجاريه. الضرب في {a+3} يحسب كل قطر مرتين، لذا العدد {((a+3)*a)//2}.')
 if k==17:
  return q('proof-subset-complement-pairs','Combinatorics',f'A set S has {a+2} elements and a distinguished element u. Prove that exactly {2**(a+1)} subsets of S contain u.',f'لمجموعة S عدد {a+2} من العناصر وعنصر مميز u. أثبت أن {2**(a+1)} مجموعة جزئية بالضبط تحتوي على u.',f'There is a bijection between subsets T of S without u and subsets containing u, given by T↦T∪{{u}}. More directly, choose any subset of the remaining {a+1} elements, then add u. There are 2^{a+1}={2**(a+1)} choices.',f'نختار أي مجموعة جزئية من العناصر الـ{a+1} الباقية ثم نضيف u. هذا تقابل واحد لواحد مع المجموعات الجزئية التي تحتوي على u. عدد الاختيارات 2^{a+1}={2**(a+1)}.')
 if k==18:
  return q('proof-even-degree-parity','Combinatorics',f'A simple graph has {a+4} vertices. Prove that the number of vertices of odd degree is even. Explain why the total number of vertices does not change the argument.',f'لرسم بياني بسيط {a+4} رؤوس. أثبت أن عدد الرؤوس ذات الدرجة الفردية زوجي، وفسر لماذا لا يغير عدد الرؤوس الكلي البرهان.',f'Every edge contributes 2 to the sum of all degrees, so that sum is even. The even-degree vertices contribute an even total. Hence the sum of the odd degrees is even, which requires an even number of odd summands. The argument works for any finite vertex count.',f'يساهم كل ضلع بمقدار 2 في مجموع الدرجات، فيكون المجموع زوجيًا. مساهمة الرؤوس ذات الدرجات الزوجية زوجية، لذا مجموع الدرجات الفردية زوجي، وهذا يتطلب عددًا زوجيًا من الحدود الفردية. يعمل البرهان لأي عدد منتهٍ من الرؤوس.')
 if k==19:
  return q('proof-modular-impossibility','Number Theory',f'Prove that no integers x,y satisfy x²+y²={4*a+3}.',f'أثبت أنه لا توجد أعداد صحيحة x وy تحقق x²+y²={4*a+3}.',f'Every integer square is 0 or 1 modulo 4. A sum of two squares can therefore be only 0,1,2 modulo 4. The right side is 3 modulo 4, a contradiction.',f'باقي مربع أي عدد صحيح بترديد 4 هو 0 أو1. إذن باقي مجموع مربعين هو 0 أو1 أو2 فقط. الطرف الأيمن باقيه 3 بترديد 4، وهذا تناقض.')
 raise ValueError(k)


def render(spec,track,level,index):
 ans=spec['answer'];written=track=='olympiad'
 out={'id':f'{track.upper()}-SM26-{index:04d}','track':track,'level':level,'topic':spec['topic'],'type':'FRQ' if written else 'MCQ','difficulty':spec['difficulty'],
      'family_id':spec['family'],'variant':index,'source':'Original SuperMath parameterized practice',
      'review':{'structural':'passed','mathematical':'construction_checked','scope':'practice_not_official_paper'},'content':{}}
 opts=[];key=None
 if not written:
  ans=F(ans); candidates=[ans]
  # Exact rational distractors, distinct from the correct answer and each other.
  # Keep nonnegative options for counts and valid [0,1] values for probability.
  if spec['topic']=='Probability':
   pool=[F(i,j) for j in range(2,13) for i in range(j+1)]
  elif ans.denominator!=1:pool=[ans+F(d,ans.denominator) for d in [-2,-1,1,2,3]]+[ans*2,ans/2]
  else:pool=[ans-1,ans+1,ans-2,ans+2,ans*2,ans+3,ans+4]
  pool=[v for v in pool if v!=ans and (v>=0 or ans<0)]
  R.shuffle(pool)
  for v in pool:
   if v not in candidates:candidates.append(v)
   if len(candidates)==(5 if track=='kangaroo' else 4):break
  while len(candidates)<(5 if track=='kangaroo' else 4):
   v=ans+len(candidates)+7
   if v not in candidates:candidates.append(v)
  R.shuffle(candidates);key=candidates.index(ans);opts=[m(val(v)) for v in candidates]
  assert len(set(opts))==len(opts) and candidates[key]==ans
  out['correct_index']=key;out['correct_answer']=val(ans)
 else:out['assessment']='self_assessment'
 for lang in ['en','ar']:
  out['content'][lang]={'question':spec[lang],'options':opts.copy(),'hint':('Identify the conditions and work backwards from what is required. Explain why your method applies.' if lang=='en' else 'حدد المعطيات والمطلوب، ثم برر اختيار طريقة الحل.'),'explanation':spec['solen' if lang=='en' else 'solar']}
 return out

TARGETS={
 'kangaroo':{'Ecolier':250,'Benjamin':250,'Cadet':250,'Junior':250},
 'nafes':{'Grade 3':250,'Grade 6':250,'Grade 9':250},
 'kaust':{'Phase 1: Foundation Research':250,'Phase 2: Advanced Analysis':250,'Phase 3: Elite Research':250},
 'nsmo':{'Phase 1: Junior Olympiad (Grades 5-7)':250,'Phase 2: Intermediate Olympiad (Grades 8-9)':250,'Phase 3: Senior National Olympiad (Grades 10-12)':250},
 'jee':{'Grade 12':500},'olympiad':{'High School':500}}

def make_banks():
 report=[]
 for track,levels in TARGETS.items():
  path=ROOT/'data'/f'{track}.json';bank=json.loads(path.read_text());bank=[q for q in bank if not q.get('family_id')]
  seen={norm(q['content']['en']['question']) for q in bank};idx=1
  for level,target in levels.items():
   have=sum(q['level']==level for q in bank);added=0;attempt=0;family_counts=collections.Counter()
   while have+added<target:
    k=attempt;attempt+=1
    if attempt>20000:raise RuntimeError((track,level,'not enough unique questions'))
    if track=='olympiad':spec=proof(k%20,k//20)
    elif track=='jee':
     # JEE's 14 syllabus units: concentrate additions on underrepresented algebra,
     # counting, matrices, vectors, probability, statistics and trigonometry.
     allowed=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23]
     spec=senior(allowed[k%len(allowed)],k//len(allowed),12)
    elif track=='kaust':spec=senior(k%26,k//26,11)
    elif track=='nsmo':
     # No calculus in olympiad mathematics. Keep training stages explicitly internal.
     allowed=[0,1,2,5,7,19,20,21,22,23,24,25]
     if 'Phase 1' in level and k%2==0:spec=junior((k//2)%20,k//40,6)
     else:spec=senior(allowed[k%len(allowed)],k//len(allowed),9)
    elif track=='kangaroo':
     g={'Ecolier':4,'Benjamin':6,'Cadet':8,'Junior':10}[level]
     allowed=[0,1,2,5,7,19,20,22,23,24,25]
     if g>=8 and k%2:spec=senior(allowed[(k//2)%len(allowed)],k//22,g)
     else:spec=junior((k//2 if g>=8 else k)%20,k//40,g)
    else:
     g=int(level.split()[-1]);allowed=[0,1,2,4,5,10,13,14,17,19] if g==3 else list(range(20))
     spec=junior(allowed[k%len(allowed)],k//len(allowed),g)
     # School-assessment framing and age-appropriate topic selection.
    stem=norm(spec['en'])
    if stem in seen:continue
    # Prevent a single family dominating any level.
    if family_counts[spec['family']]>=30:continue
    q=render(spec,track,level,idx);idx+=1;seen.add(stem);bank.append(q);added+=1;family_counts[spec['family']]+=1
   report.append({'track':track,'level':level,'retained':have,'added':added,'total':have+added,'new_families':dict(family_counts)})
  path.write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'review/expansion-summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps([{k:v for k,v in row.items() if k!='new_families'} for row in report],indent=2))
if __name__=='__main__':make_banks()
