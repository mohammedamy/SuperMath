"""Deterministic original practice variants. Family IDs make repetition explicit.
This generator verifies construction and answer keys, not official exam equivalence.
"""
import json, math, random, collections, itertools, re
from fractions import Fraction as F
from pathlib import Path
from audit_banks import ROOT, norm
import junior_families, senior_families, proof_families

R = random.Random(6092026)

def m(x): return "\\( " + str(x) + " \\)"
def val(x):
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"\\frac{{{x.numerator}}}{{{x.denominator}}}"
    return str(x)

def item(family, topic, en, ar, answer, solen, solar, diff="Medium", distractors=None):
    return dict(family=family, topic=topic, en=en, ar=ar, answer=answer, solen=solen, solar=solar, difficulty=diff, distractors=distractors)


def junior(k, n, g):
    if k >= 61:
        return junior_families.junior_extra(k, n, g)
    r_local = random.Random(6092026 + k * 10007 + n * 997 + g * 31)
    old_R = R
    try:
        globals()["R"] = r_local
        return _orig_junior(k, n, g)
    finally:
        globals()["R"] = old_R

def _orig_junior(k, n, g):
    a = R.randint(2, 8 + g); b = R.randint(2, 7 + g); c = R.randint(2, 6); t = R.randint(2, 5); x = R.randint(3, 12 + g)
    if k == 0:
        total = a * b + c
        return item('equal-groups-leftover', 'Numbers and Operations',
                    f'{a} identical boxes each contain the same number of counters. With {c} extra counters there are {total} counters altogether. How many are in each box?',
                    f'تحتوي {a} علب متماثلة على العدد نفسه من القطع. ومع {c} قطع إضافية يصبح المجموع {total}. كم قطعة في كل علبة؟',
                    b, f'Remove the extra counters, then divide: ({total} − {c}) ÷ {a} = {b}.',
                    f'نطرح القطع الإضافية ثم نقسم: ({total} − {c}) ÷ {a} = {b}.', 'Easy')
    if k == 1:
        d = R.randint(2, 5); v = R.randint(2, 9); terms = [v + d * i for i in range(4)]
        return item('constant-step-gap', 'Patterns',
                    f'A sequence increases by the same amount each time: {terms[0]}, {terms[1]}, ?, {terms[3]}. Find the missing number.',
                    f'تزداد المتتالية بمقدار ثابت: {terms[0]}، {terms[1]}، ؟، {terms[3]}. أوجد العدد الناقص.',
                    terms[2], f'The step is {terms[1]} − {terms[0]} = {d}. Add it to {terms[1]} to get {terms[2]}.',
                    f'الزيادة {terms[1]} − {terms[0]} = {d}. بإضافتها إلى {terms[1]} نحصل على {terms[2]}.', 'Easy')
    if k == 2:
        return item('row-position', 'Logic',
                    f'Sara is {a}th from the front and {b}th from the back of a line. How many people are in the line?',
                    f'ترتيب سارة {a} من بداية صف و{b} من نهايته. كم شخصًا في الصف؟',
                    a + b - 1, f'Adding the positions counts Sara twice. Total = {a} + {b} − 1 = {a + b - 1}.',
                    f'جمع الترتيبين يحسب سارة مرتين. العدد = {a} + {b} − 1 = {a + b - 1}.')
    if k == 3:
        w = a + 2; h = b + 2
        return item('grid-border', 'Geometry',
                    f'A rectangle of {w} columns and {h} rows is made of unit squares. How many squares touch its outer boundary?',
                    f'مستطيل من مربعات وحدة به {w} أعمدة و{h} صفوف. كم مربعًا يلامس حدوده الخارجية؟',
                    2 * w + 2 * h - 4, f'Top and bottom contribute 2×{w}. The middle rows contribute 2×({h}−2). Total {2 * w + 2 * h - 4}.',
                    f'الصفان العلوي والسفلي يساهمان بـ2×{w}، والصفوف الوسطى بـ2×({h}−2). المجموع {2 * w + 2 * h - 4}.')
    if k == 4:
        return item('joined-squares-perimeter', 'Geometry',
                    f'{a} squares of side {b} cm are joined edge to edge in one straight row, with no gaps. What is the perimeter in cm?',
                    f'وُصلت {a} مربعات طول ضلع كل منها {b} سم في صف مستقيم دون فراغات. ما المحيط بالسنتيمتر؟',
                    2 * b * (a + 1), f'The row is a rectangle {a * b} cm long and {b} cm wide. Perimeter = 2({a * b}+{b}) = {2 * b * (a + 1)}.',
                    f'ينتج مستطيل طوله {a * b} سم وعرضه {b} سم. المحيط = 2({a * b}+{b}) = {2 * b * (a + 1)}.')
    if k == 5:
        ans = (a - 1) * c
        return item('intervals-not-objects', 'Measurement',
                    f'{a} trees stand in one straight row. The gap between neighboring trees is {c} m. How far is the first tree from the last, in metres?',
                    f'تقف {a} أشجار في صف مستقيم، والمسافة بين كل شجرتين متجاورتين {c} م. كم مترًا بين الأولى والأخيرة؟',
                    ans, f'{a} trees create {a - 1} gaps. Distance = {a - 1} × {c} = {ans}.',
                    f'عدد الفجوات {a - 1}. المسافة = {a - 1} × {c} = {ans}.', 'Easy')
    if k == 6:
        nbox = c + 1; nball = nbox * (a - 1) + 1
        return item('pigeonhole-guarantee', 'Logic',
                    f'{nball} counters are placed in {nbox} boxes. What is the smallest number of counters that at least one box must contain?',
                    f'وُزعت {nball} قطعة على {nbox} صناديق. ما أصغر عدد من القطع نضمن وجوده في صندوق واحد على الأقل؟',
                    a, f'If every box had at most {a - 1}, there would be at most {nbox * (a - 1)} counters. Thus one has at least {a}.',
                    f'إذا احتوى كل صندوق على {a - 1} قطع كحد أقصى فلن يتجاوز المجموع {nbox * (a - 1)}. لذا يحتوي أحدها على {a} على الأقل.')
    if k == 7:
        return item('fraction-complement', 'Fractions',
                    f'A ribbon is {a * b} cm long. A piece of length {(a - 1) * b} cm is cut off. What fraction of the original ribbon remains?',
                    f'طول شريط {a * b} سم، قُطعت منه قطعة طولها {(a - 1) * b} سم. ما الكسر الذي يمثل الجزء المتبقي من الشريط الأصلي؟',
                    F(1, a), f'The remaining length is {b} cm, so the fraction is {m(str(b) + "/" + str(a * b))} = {m(val(F(1, a)))}.',
                    f'المتبقي {b} سم، إذن الكسر {m(str(b) + "/" + str(a * b))} = {m(val(F(1, a)))}.')
    if k == 8:
        small = a; large = a + 2 * c; total = small + large
        return item('sum-and-difference', 'Algebra',
                    f'Two baskets hold {total} apples altogether. One has {2 * c} more apples than the other. How many apples are in the smaller basket?',
                    f'في سلتين {total} تفاحة، وتزيد إحداهما على الأخرى بـ{2 * c} تفاحات. كم تفاحة في السلة الأصغر؟',
                    small, f'Remove the difference: {total}−{2 * c}={2 * small}. Divide equally to obtain {small}.',
                    f'نطرح الفرق: {total}−{2 * c}={2 * small}، ثم نقسم على 2 فنحصل على {small}.')
    if k == 9:
        red = a; blue = b; take = max(a, b) + 1
        return item('guarantee-two-colours', 'Logic',
                    f'A bag has {red} red and {blue} blue counters. Without looking, how many must you take to guarantee at least one of each colour?',
                    f'في كيس {red} قطع حمراء و{blue} زرقاء. كم قطعة يجب سحبها دون نظر لضمان وجود قطعة من كل لون؟',
                    take, f'Take all {max(a, b)} of the larger colour plus 1 to guarantee the other: {take}.',
                    f'نسحب {max(a, b)} من اللون الأكبر وزيادة 1 لضمان اللون الآخر: {take}.')
    if k == 10:
        ans = (c % 7) or 7
        return item('cycle-remainder', 'Patterns',
                    f'A machine prints the repeating cycle 1, 2, 3, 4, 5, 6, 7, starting at 1. What number is printed in position {a * 7 + c}?',
                    f'تطبع آلة الدورة المتكررة 1، 2، 3، 4، 5، 6، 7 بدءًا من 1. ما العدد في الموضع {a * 7 + c}؟',
                    ans, f'{a * 7 + c} = 7×{a}+{c}. After {a} complete cycles, the position in the cycle is {ans}.',
                    f'{a * 7 + c} = 7×{a}+{c}. بعد {a} دورات، الموضع في الدورة هو {ans}.', 'Easy')
    if k == 11:
        return item('heads-and-legs', 'Logic',
                    f'A farm has chickens and rabbits: {a + b} heads and {2 * a + 4 * b} legs. How many rabbits are there?',
                    f'في مزرعة دجاج وأرانب، مجموع الرؤوس {a + b} والأرجل {2 * a + 4 * b}. كم أرنبًا فيها؟',
                    b, f'If all were chickens there would be {2 * (a + b)} legs. The extra {2 * b} legs come from rabbits, two extra legs each: {b}.',
                    f'لو كانت كلها دجاجًا لكان عدد الأرجل {2 * (a + b)}. الزيادة {2 * b} تعود للأرانب، رجلان لكل أرنب: {b}.')
    if k == 12:
        lo = a * 10; hi = lo + b * 3
        ans = sum(i % 3 == 0 for i in range(lo, hi + 1))
        return item('count-multiples-interval', 'Number Theory',
                    f'How many integers from {lo} through {hi}, including both endpoints, are divisible by 3?',
                    f'كم عددًا صحيحًا من {lo} إلى {hi} شاملًا الطرفين يقبل القسمة على 3؟',
                    ans, f'Count the multiples of 3 in [{lo}, {hi}]: {ans}.',
                    f'عدد مضاعفات 3 في الفترة [{lo}، {hi}] هو {ans}.')
    if k == 13:
        return item('reverse-two-operations', 'Algebra',
                    f'I think of a number, multiply it by {c}, then add {a}. The result is {x * c + a}. What was my number?',
                    f'فكرت في عدد، وضربته في {c} ثم أضفت {a} فكانت النتيجة {x * c + a}. ما العدد؟',
                    x, f'Undo the operations: ({x * c + a}−{a})÷{c}={x}.',
                    f'نعكس العمليات: ({x * c + a}−{a})÷{c}={x}.', 'Easy')
    if k == 14:
        return item('choice-product', 'Combinatorics',
                    f'A café offers {a} sandwiches and {b} drinks. A meal contains one sandwich and one drink. How many different meals can be chosen?',
                    f'يقدم مقهى {a} أنواع من الشطائر و{b} أنواع من المشروبات. تتكون الوجبة من شطيرة ومشروب. كم وجبة مختلفة يمكن اختيارها؟',
                    a * b, f'Multiply choices: {a}×{b}={a * b}.',
                    f'نضرب عدد الخيارات: {a}×{b}={a * b}.', 'Easy')
    if k == 15:
        seq = [a, a + 2, a + 4, a + 6]; missing = a + 8
        return item('mean-missing-observation', 'Statistics',
                    f'The mean of five numbers is {a + 4}. Four of them are {", ".join(map(str, seq))}. Find the fifth.',
                    f'المتوسط الحسابي لخمسة أعداد {a + 4}. أربعة منها هي {"، ".join(map(str, seq))}. أوجد الخامس.',
                    missing, f'Total is 5×{a + 4}={5 * (a + 4)}. Subtract {sum(seq)} to get {missing}.',
                    f'المجموع 5×{a + 4}={5 * (a + 4)}. نطرح {sum(seq)} فنحصل على {missing}.')
    if k == 16:
        return item('shared-edge-two-rectangles', 'Geometry',
                    f'Two {a} cm by {b} cm rectangles are joined along a whole side of length {b} cm without overlap. What is the perimeter of the resulting rectangle?',
                    f'وُصل مستطيلان أبعاد كل منهما {a} سم و{b} سم على طول ضلع كامل طوله {b} سم دون تداخل. ما محيط المستطيل الناتج؟',
                    4 * a + 2 * b, f'The new dimensions are {2 * a} by {b}. Perimeter = 2({2 * a}+{b})={4 * a + 2 * b}.',
                    f'الأبعاد الجديدة {2 * a} و{b}. المحيط = 2({2 * a}+{b})={4 * a + 2 * b}.')
    if k == 17:
        # Varied elapsed time contexts
        h = R.randint(8, 11); minute = R.randint(0, 5) * 5; duration = a * 5; end = h * 60 + minute + duration
        scenarios = [
            (f'A chemistry experiment begins at {h}:{minute:02d} a.m. and lasts {duration} minutes. How many minutes after 8:00 a.m. does it finish?',
             f'بدأت تجربة كيميائية الساعة {h}:{minute:02d} صباحًا واستمرت {duration} دقيقة. بعد كم دقيقة من الساعة 8:00 صباحًا تنتهي؟'),
            (f'A train departs at {h}:{minute:02d} a.m. and travels for {duration} minutes. How many minutes after 8:00 a.m. does it arrive at its destination?',
             f'انطلق قطار الساعة {h}:{minute:02d} صباحًا واستغرقت رحلته {duration} دقيقة. بعد كم دقيقة من الساعة 8:00 صباحًا يصل وجهته؟'),
            (f'A robotics session starts at {h}:{minute:02d} a.m. and continues for {duration} minutes. How many minutes after 8:00 a.m. does it conclude?',
             f'بدأت جلسة روبوتات الساعة {h}:{minute:02d} صباحًا واستمرت {duration} دقيقة. بعد كم دقيقة من الساعة 8:00 صباحًا تُختتم؟'),
            (f'A cycling race begins at {h}:{minute:02d} a.m. and lasts {duration} minutes. How many minutes after 8:00 a.m. does it end?',
             f'بدأ سباق دراجات الساعة {h}:{minute:02d} صباحًا واستمر {duration} دقيقة. بعد كم دقيقة من الساعة 8:00 صباحًا ينتهي؟')
        ]
        q_en, q_ar = scenarios[n % len(scenarios)]
        return item('elapsed-time', 'Measurement', q_en, q_ar, end - 480,
                    f'Start is {(h - 8) * 60 + minute} minutes after 8:00. Add {duration} to get {end - 480}.',
                    f'البداية بعد {(h - 8) * 60 + minute} دقيقة من 8:00. نضيف {duration} فنحصل على {end - 480}.')
    if k == 18:
        return item('cut-corners-perimeter', 'Geometry',
                    f'A square has side {a + 2} cm. A 1 cm square is cut from each corner. What is the perimeter of the remaining shape, in cm?',
                    f'مربع طول ضلعه {a + 2} سم. قُطع مربع طول ضلعه 1 سم من كل ركن. ما محيط الشكل المتبقي بالسنتيمتر؟',
                    4 * (a + 2), f'Perimeter is unchanged: 4×{a + 2}={4 * (a + 2)}.',
                    f'المحيط لا يتغير: 4×{a + 2}={4 * (a + 2)}.')
    if k == 19:
        return item('balance-equal-objects', 'Algebra',
                    f'A balanced scale has {c} identical blocks and a {a} g weight on one side, and a {c * x + a} g weight on the other. What is the mass of one block in grams?',
                    f'في كفة ميزان متزن {c} مكعبات متماثلة وثقل {a} جم، وفي الأخرى ثقل {c * x + a} جم. ما كتلة المكعب بالجرام؟',
                    x, f'Subtract {a}: {c * x} g. Divide by {c}: {x} g.',
                    f'نطرح {a}: {c * x} جم، ثم نقسم على {c}: {x} جم.')
    # NEW JUNIOR FAMILIES (20 through 60)
    if k == 20:
        ang1 = 30 + a * 5; ang2 = 40 + b * 5; ang3 = 180 - ang1 - ang2
        return item('triangle-third-angle', 'Geometry',
                    f'Two angles of a triangle are {ang1}° and {ang2}°. Find the measure of the third angle in degrees.',
                    f'قياسا زاويتين في مثلث هما {ang1}° و{ang2}°. أوجد قياس الزاوية الثالثة بالدرجات.',
                    ang3, f'Angles sum to 180°: 180° − {ang1}° − {ang2}° = {ang3}°.',
                    f'مجموع زوايا المثلث 180°: 180° − {ang1}° − {ang2}° = {ang3}°.')
    if k == 21:
        ans = a * b * c
        return item('cuboid-volume', 'Measurement',
                    f'A rectangular prism has length {a} cm, width {b} cm, and height {c} cm. What is its volume in cm³?',
                    f'شبه مكعب طوله {a} سم، وعرضه {b} سم، وارتفاعه {c} سم. ما حجمه بالسنتيمتر المكعب؟',
                    ans, f'Volume = length × width × height = {a} × {b} × {c} = {ans}.',
                    f'الحجم = الطول × العرض × الارتفاع = {a} × {b} × {c} = {ans}.')
    if k == 22:
        speed = 40 + a * 5; time_h = c; dist = speed * time_h
        return item('speed-distance-time', 'Measurement',
                    f'A car travels at a constant speed of {speed} km/h for {time_h} hours. How many kilometres does it travel?',
                    f'تسير سيارة بسرعة ثابتة مقدارها {speed} كم/ساعة لمدة {time_h} ساعات. كم كيلومترًا تقطع؟',
                    dist, f'Distance = speed × time = {speed} × {time_h} = {dist} km.',
                    f'المسافة = السرعة × الزمن = {speed} × {time_h} = {dist} كم.')
    if k == 23:
        total = b * x; ans = a * x
        return item('fraction-of-quantity', 'Fractions',
                    f'What is {m(f"\\frac{{{a}}}{{{b}}}")} of {total}?',
                    f'ما قيمة {m(f"\\frac{{{a}}}{{{b}}}")} من {total}؟',
                    ans, f'Divide by denominator then multiply by numerator: ({total} ÷ {b}) × {a} = {ans}.',
                    f'نقسم على المقام ثم نضرب في البسط: ({total} ÷ {b}) × {a} = {ans}.')
    if k == 24:
        price = a * 20; pct = 10 * c; discount = (price * pct) // 100
        return item('percentage-discount', 'Numbers and Operations',
                    f'A jacket originally costs {price} riyals. During a sale, it is discounted by {pct}%. How many riyals is the discount?',
                    f'سعر سترة أصلي {price} ريالًا. خُفِّض سعرها في التخفيضات بنسبة {pct}%. كم ريالًا قيمة التخفيض؟',
                    discount, f'Discount = {pct}% of {price} = ({pct}/100) × {price} = {discount} riyals.',
                    f'قيمة التخفيض = {pct}% من {price} = ({pct}/100) × {price} = {discount} ريالًا.')
    if k == 25:
        ans = (a * b) // math.gcd(a, b)
        return item('lcm-word-problem', 'Number Theory',
                    f'Two timers beep every {a} minutes and every {b} minutes, respectively. If they beep together now, in how many minutes will they next beep together?',
                    f'يصدر مؤقتان رنينًا كل {a} دقائق وكل {b} دقائق على التوالي. إذا رنا معًا الآن، بعد كم دقيقة سيرنان معًا مجددًا؟',
                    ans, f'The next time is the least common multiple: LCM({a}, {b}) = {ans}.',
                    f'الوقت التالي هو المضاعف المشترك الأصغر: LCM({a}، {b}) = {ans}.')
    if k == 26:
        ans = a * b; perim = 2 * (a + b)
        return item('rectangle-area-from-perimeter', 'Geometry',
                    f'A rectangle has a perimeter of {perim} cm and a width of {b} cm. What is its area in cm²?',
                    f'مستطيل محيطه {perim} سم وعرضه {b} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans, f'Semi-perimeter is {a + b} cm. Length = {a + b} − {b} = {a} cm. Area = {a} × {b} = {ans} cm².',
                    f'نصف المحيط {a + b} سم. الطول = {a + b} − {b} = {a} سم. المساحة = {a} × {b} = {ans} سم².')
    if k == 27:
        mult = c + 1; son = a + 2; father = son * mult; total_age = son + father
        return item('age-ratio-sum', 'Algebra',
                    f'The sum of the ages of a father and his son is {total_age} years. The father is {mult} times as old as the son. How old is the son?',
                    f'مجموع عمري أب وابنه {total_age} سنة. عمر الأب {mult} أمثال عمر ابنه. كم عمر الابن؟',
                    son, f'Let son be s. Then s + {mult}s = {total_age} ⇒ {mult + 1}s = {total_age} ⇒ s = {son}.',
                    f'بفرض عمر الابن s، فإن {mult + 1}s = {total_age} ومنه s = {son}.')
    if k == 28:
        d1 = a; d2 = b; d3 = c; rem = (d1 + d2 + d3) % 9; missing = (9 - rem) % 9
        return item('divisibility-digit-nine', 'Number Theory',
                    f'The four-digit number {d1}{d2}D{d3} is divisible by 9. What single digit is D?',
                    f'العدد المكون من أربعة أرقام {d1}{d2}D{d3} يقبل القسمة على 9. ما الرقم المفرد D؟',
                    missing, f'The digit sum {d1}+{d2}+D+{d3} = {d1+d2+d3}+D must be a multiple of 9, giving D = {missing}.',
                    f'مجموع الأرقام {d1+d2+d3}+D يجب أن يقبل القسمة على 9، إذن D = {missing}.')
    if k == 29:
        nums = [a, a + 3, a + 5]; fourth = a + 8; mean_val = (sum(nums) + fourth) // 4
        # Adjust fourth so mean is exact integer
        rem = (sum(nums) + fourth) % 4
        fourth += (4 - rem) % 4
        mean_val = (sum(nums) + fourth) // 4
        return item('arithmetic-mean-four', 'Statistics',
                    f'The mean of four test scores is {mean_val}. Three of the scores are {nums[0]}, {nums[1]}, and {nums[2]}. What is the fourth score?',
                    f'المتوسط الحسابي لأربع درجات اختبار هو {mean_val}. ثلاث من الدرجات هي {nums[0]} و{nums[1]} و{nums[2]}. ما الدرجة الرابعة؟',
                    fourth, f'Total sum is 4 × {mean_val} = {4 * mean_val}. Fourth = {4 * mean_val} − {sum(nums)} = {fourth}.',
                    f'المجموع الكلي 4 × {mean_val} = {4 * mean_val}. الدرجة الرابعة = {4 * mean_val} − {sum(nums)} = {fourth}.')
    if k == 30:
        diff_ang = 2 * a; smaller = (90 - diff_ang) // 2
        return item('complementary-angles', 'Geometry',
                    f'Two complementary angles have measures differing by {diff_ang}°. Find the measure of the smaller angle in degrees.',
                    f'زاويتان متتامتان الفرق بين قياسيهما {diff_ang}°. أوجد قياس الزاوية الصغرى بالدرجات.',
                    smaller, f'x + (x + {diff_ang}) = 90 ⇒ 2x = {90 - diff_ang} ⇒ x = {smaller}°.',
                    f'x + (x + {diff_ang}) = 90 ⇒ 2x = {90 - diff_ang} ⇒ x = {smaller}°.')
    if k == 31:
        rad = a + 3; diam = 2 * rad
        return item('circle-diameter-radius', 'Measurement',
                    f'A circle has a diameter of {diam} cm. What is its radius in cm?',
                    f'دائرة قطرها {diam} سم. ما نصف قطرها بالسنتيمتر؟',
                    rad, f'Radius = diameter ÷ 2 = {diam} ÷ 2 = {rad} cm.',
                    f'نصف القطر = القطر ÷ 2 = {diam} ÷ 2 = {rad} سم.', 'Easy')
    if k == 32:
        start = a + 1; ans = start + 2; total_sum = 3 * start + 3
        return item('consecutive-integers-sum', 'Algebra',
                    f'The sum of three consecutive integers is {total_sum}. What is the largest of these integers?',
                    f'مجموع ثلاثة أعداد صحيحة متتالية هو {total_sum}. ما أكبر هذه الأعداد؟',
                    ans, f'Let the integers be n, n+1, n+2. 3n + 3 = {total_sum} ⇒ n = {start}. Largest = {ans}.',
                    f'الأعداد n، n+1، n+2. إذن 3n + 3 = {total_sum} ومنه n = {start}، والأكبر {ans}.')
    if k == 33:
        t_dig = a; u_dig = b; ans = t_dig * u_dig
        return item('digits-product-two-digit', 'Number Theory',
                    f'What is the product of the digits of the two-digit number {t_dig}{u_dig}?',
                    f'ما حاصل ضرب رقمي العدد المكون من منزلتين {t_dig}{u_dig}؟',
                    ans, f'Multiply tens digit by units digit: {t_dig} × {u_dig} = {ans}.',
                    f'نضرب رقم العشرات في رقم الآحاد: {t_dig} × {u_dig} = {ans}.', 'Easy')
    if k == 34:
        # Probability of rolling a number > threshold on a fair 6-sided die
        thresh = c % 4 + 2; favorable = 6 - thresh
        return item('simple-probability-die', 'Probability',
                    f'A fair 6-sided die is rolled once. What is the probability of rolling a number strictly greater than {thresh}?',
                    f'أُلقي نرد عادل ذو 6 أوجه مرة واحدة. ما احتمال ظهور عدد أكبر قطعيًا من {thresh}؟',
                    F(favorable, 6), f'Numbers greater than {thresh} are {list(range(thresh + 1, 7))}, so {favorable} out of 6.',
                    f'الأعداد الأكبر من {thresh} عددها {favorable} من أصل 6، فالاحتمال {m(val(F(favorable, 6)))}.')
    if k == 35:
        sides = c + 4; ans = (sides - 2) * 180
        return item('polygon-interior-angles', 'Geometry',
                    f'What is the sum of the interior angles of a convex polygon with {sides} sides, in degrees?',
                    f'ما مجموع قياسات الزوايا الداخلية لمضلع محدب له {sides} أضلاع بالدرجات؟',
                    ans, f'Sum = (n − 2) × 180° = ({sides} − 2) × 180° = {ans}°.',
                    f'المجموع = (n − 2) × 180° = ({sides} − 2) × 180° = {ans}°.')
    if k == 36:
        # Combined rate
        rate1 = a; rate2 = b; ans = rate1 + rate2
        return item('work-rate-joint', 'Algebra',
                    f'Pump A fills {rate1} litres per minute and Pump B fills {rate2} litres per minute. How many litres do both pumps fill together in one minute?',
                    f'تضخ المضخة A كمية {rate1} لترًا في الدقيقة والمضخة B كمية {rate2} لترًا في الدقيقة. كم لترًا تضخ المضختان معًا في الدقيقة الواحدة؟',
                    ans, f'Add their rates: {rate1} + {rate2} = {ans} litres per minute.',
                    f'نجمع المعدلين: {rate1} + {rate2} = {ans} لترًا في الدقيقة.', 'Easy')
    if k == 37:
        part_a = a; part_b = b; unit = x; total_coins = (part_a + part_b) * unit; ans = max(part_a, part_b) * unit
        return item('ratio-proportional-sharing', 'Numbers and Operations',
                    f'A prize of {total_coins} coins is shared between two students in the ratio {part_a}:{part_b}. How many coins does the student with the larger share receive?',
                    f'قُسمت جائزة قدرها {total_coins} قطعة نقدية بين طالبين بنسبة {part_a}:{part_b}. كم قطعة يحصل عليها صاحب النصيب الأكبر؟',
                    ans, f'Total parts = {part_a + part_b}. Value per part = {total_coins} ÷ {part_a + part_b} = {unit}. Larger share = {max(part_a, part_b)} × {unit} = {ans}.',
                    f'مجموع الأجزاء = {part_a + part_b}. قيمة الجزء = {unit}. النصيب الأكبر = {ans}.')
    if k == 38:
        primes = [2, 3, 5, 7, 11]
        p1, p2 = R.sample(primes, 2); num = p1 * p2
        return item('prime-factor-count', 'Number Theory',
                    f'How many distinct prime factors does the number {num} have?',
                    f'كم عاملًا أوليًا مختلفًا للعدد {num}؟',
                    2, f'The prime factorization is {p1} × {p2}, so there are 2 distinct prime factors.',
                    f'التحليل إلى عوامل أولية هو {p1} × {p2}، إذن يوجد عاملان أوليان مختلفان.')
    if k == 39:
        b1 = a * 2; b2 = b * 2; h_trap = c; ans = ((b1 + b2) * h_trap) // 2
        return item('trapezoid-area', 'Geometry',
                    f'A trapezoid has parallel bases of lengths {b1} cm and {b2} cm, and a height of {h_trap} cm. What is its area in cm²?',
                    f'شبه منحرف طول قاعدتيه المتوازيتين {b1} سم و{b2} سم، وارتفاعه {h_trap} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans, f'Area = ½ × (b₁ + b₂) × h = ½ × ({b1} + {b2}) × {h_trap} = {ans} cm².',
                    f'المساحة = ½ × ({b1} + {b2}) × {h_trap} = {ans} سم².')
    if k == 40:
        h1 = 8 + a % 3; m1 = (b % 4) * 15; dur_h = 1 + c % 3; dur_m = (a % 3) * 15
        total_min = dur_h * 60 + dur_m
        return item('elapsed-train-journey', 'Measurement',
                    f'A high-speed train travels for {dur_h} hour(s) and {dur_m} minutes. How many total minutes does the trip take?',
                    f'تسير رحلة قطار سريع لمدة {dur_h} ساعة و{dur_m} دقيقة. كم دقيقة تستغرق الرحلة إجمالاً؟',
                    total_min, f'Convert hours to minutes and add: {dur_h} × 60 + {dur_m} = {total_min} minutes.',
                    f'نحول الساعات إلى دقائق ونجمع: {dur_h} × 60 + {dur_m} = {total_min} دقيقة.')
    if k == 41:
        ans = 2 * (a * b + a * c + b * c)
        return item('cuboid-surface-area', 'Geometry',
                    f'Find the total surface area in cm² of a rectangular box with dimensions {a} cm by {b} cm by {c} cm.',
                    f'أوجد المساحة الكلية لسطح صندوق مستطيل أبعاده {a} سم و{b} سم و{c} سم بالسنتيمتر المربع.',
                    ans, f'Surface area = 2(lw + lh + wh) = 2({a * b} + {a * c} + {b * c}) = {ans} cm².',
                    f'المساحة الكلية = 2(lw + lh + wh) = {ans} سم².')
    if k == 42:
        w_step = a + 4; h_step = b + 3; perim_step = 2 * (w_step + h_step)
        return item('perimeter-step-shape', 'Geometry',
                    f'An L-shaped polygon fits inside a bounding box of width {w_step} cm and height {h_step} cm with only horizontal and vertical edges. What is its perimeter in cm?',
                    f'مضلع على شكل حرف L محاط بمستطيل عرضه {w_step} سم وارتفاعه {h_step} سم وجميع أضلاعه أفقية أو رأسية. ما محيطه بالسنتيمتر؟',
                    perim_step, f'The perimeter equals that of the bounding rectangle: 2 × ({w_step} + {h_step}) = {perim_step} cm.',
                    f'المحيط يساوي محيط المستطيل المحيط: 2 × ({w_step} + {h_step}) = {perim_step} سم.')
    if k == 43:
        mult_pyth = c; leg1 = 3 * mult_pyth; leg2 = 4 * mult_pyth; hyp = 5 * mult_pyth
        return item('pythagorean-triple-hypotenuse', 'Geometry',
                    f'A right-angled triangle has legs of length {leg1} cm and {leg2} cm. Find the length of the hypotenuse in cm.',
                    f'مثلث قائم الزاوية طولا ساقيه {leg1} سم و{leg2} سم. أوجد طول الوتر بالسنتيمتر.',
                    hyp, f'Pythagorean theorem: √({leg1}² + {leg2}²) = √({leg1**2 + leg2**2}) = {hyp} cm.',
                    f'مبرهنة فيثاغورس: √({leg1}² + {leg2}²) = {hyp} سم.')
    if k == 44:
        p_val = 2; q_val = 3; num_val = (p_val ** a) * (q_val ** b); total_div = (a + 1) * (b + 1)
        return item('number-of-factors', 'Number Theory',
                    f'How many positive divisors does the number {num_val} have?',
                    f'كم قاسمًا موجبًا للعدد {num_val}؟',
                    total_div, f'The prime factorization is 2^{a} × 3^{b}. Number of divisors = ({a}+1)({b}+1) = {total_div}.',
                    f'التحليل إلى عوامل أولية 2^{a} × 3^{b}. عدد القواسم = ({a}+1)({b}+1) = {total_div}.')
    if k == 45:
        hour_val = a % 11 + 1; ang_clock = min(hour_val * 30, (12 - hour_val) * 30)
        return item('clock-angle-hours', 'Measurement',
                    f'What is the smaller angle between the hour hand and the minute hand of a clock at {hour_val}:00, in degrees?',
                    f'ما قياس الزاوية الصغرى بين عقربي الساعات والدقائق في الساعة {hour_val}:00 بالدرجات؟',
                    ang_clock, f'Each hour corresponds to 360° ÷ 12 = 30°. Angle = {ang_clock}°.',
                    f'كل ساعة تمثل 30°. الزاوية = {ang_clock}°.')
    if k == 46:
        n_a = a + 10; n_b = b + 8; both = c + 2; total_stud = n_a + n_b - both + 5
        return item('venn-two-sets-overlap', 'Logic',
                    f'In a school club of {total_stud} students, {n_a} play soccer, {n_b} play basketball, and {both} play both. How many students play neither?',
                    f'في نادٍ مدرسي يضم {total_stud} طالبًا، يلعب {n_a} كرة القدم و{n_b} كرة السلة و{both} اللعبتين معًا. كم طالبًا لا يلعب أيًا منهما؟',
                    5, f'Union = {n_a} + {n_b} − {both} = {n_a + n_b - both}. Neither = {total_stud} − {n_a + n_b - both} = 5.',
                    f'عدد من يلعب إحداهما على الأقل = {n_a + n_b - both}. من لا يلعب أيًا منهما = 5.')
    if k == 47:
        base_list = sorted([a, a + 2, a + 5, a + 8, a + 11])
        median_val = base_list[2]
        return item('median-odd-list', 'Statistics',
                    f'Find the median of the data set: {base_list[0]}, {base_list[1]}, {base_list[2]}, {base_list[3]}, {base_list[4]}.',
                    f'أوجد الوسيط لمجموعة البيانات: {base_list[0]}، {base_list[1]}، {base_list[2]}، {base_list[3]}، {base_list[4]}.',
                    median_val, f'In ordered order, the middle element is the 3rd number: {median_val}.',
                    f'في الترتيب التصاعدي، العنصر الأوسط هو الثالث: {median_val}.', 'Easy')
    if k == 48:
        rep_count = a + 3; term_val = b + 2; ans_rep = rep_count * term_val
        return item('repeated-addition-multiplication', 'Numbers and Operations',
                    f'If the number {term_val} is added to itself {rep_count} times, what is the result?',
                    f'إذا جُمع العدد {term_val} مع نفسه {rep_count} مرات، فما الناتج؟',
                    ans_rep, f'Repeated addition is multiplication: {rep_count} × {term_val} = {ans_rep}.',
                    f'الجمع المتكرر هو الضرب: {rep_count} × {term_val} = {ans_rep}.', 'Easy')
    if k == 49:
        side_sq = 2 * a; area_sq = side_sq * side_sq
        return item('square-inscribed-circle', 'Geometry',
                    f'A circle of radius {a} cm is inscribed inside a square. What is the area of the square in cm²?',
                    f'دائرة نصف قطرها {a} سم مرسومة داخل مربع وتمس أضلاعه. ما مساحة المربع بالسنتيمتر المربع؟',
                    area_sq, f'Side of square = 2 × radius = {side_sq} cm. Area = {side_sq}² = {area_sq} cm².',
                    f'طول ضلع المربع = 2 × نصف القطر = {side_sq} سم. المساحة = {side_sq}² = {area_sq} سم².')
    if k == 50:
        p_money = a * 100; r_rate = 5; t_time = c; interest = (p_money * r_rate * t_time) // 100
        return item('simple-interest-total', 'Numbers and Operations',
                    f'A deposit of {p_money} riyals earns simple interest at {r_rate}% per year for {t_time} years. How much interest is earned in riyals?',
                    f'وديعة قدرها {p_money} ريال تُحقق فائدة بسيطة بنسبة {r_rate}% سنويًا لمدة {t_time} سنوات. كم ريالًا مقدار الفائدة؟',
                    interest, f'Interest = P × r × t ÷ 100 = ({p_money} × {r_rate} × {t_time}) ÷ 100 = {interest} riyals.',
                    f'الفائدة = P × r × t ÷ 100 = {interest} ريالًا.')
    if k == 51:
        scale_val = a * 5; map_cm = b; real_km = scale_val * map_cm
        return item('scale-drawing-distance', 'Measurement',
                    f'On a map, 1 cm represents {scale_val} km in reality. How many kilometres does {map_cm} cm represent?',
                    f'على خريطة، يمثل كل 1 سم مسافة {scale_val} كم في الواقع. كم كيلومترًا تمثل {map_cm} سم؟',
                    real_km, f'Real distance = {map_cm} × {scale_val} = {real_km} km.',
                    f'المسافة الواقعية = {map_cm} × {scale_val} = {real_km} كم.', 'Easy')
    if k == 52:
        edge = a + 1; vol_cube = edge ** 3
        return item('cube-volume-from-surface', 'Geometry',
                    f'A cube has an edge length of {edge} cm. What is its volume in cm³?',
                    f'مكعب طول حرفه {edge} سم. ما حجمه بالسنتيمتر المكعب؟',
                    vol_cube, f'Volume = edge³ = {edge}³ = {vol_cube} cm³.',
                    f'الحجم = طول الحرف³ = {edge}³ = {vol_cube} سم³.')
    if k == 53:
        n_zeros = a + 2; sub_val = b; val_res = 10**n_zeros - sub_val; sum_digits = sum(map(int, str(val_res)))
        return item('digit-sum-divisibility', 'Number Theory',
                    f'What is the sum of the digits of the integer equal to {m(f"10^{{{n_zeros}}} - {sub_val}")}?',
                    f'ما مجموع أرقام العدد الصحيح الناتج من {m(f"10^{{{n_zeros}}} - {sub_val}")}؟',
                    sum_digits, f'Evaluating gives {val_res}. Sum of digits is {sum_digits}.',
                    f'القيمة هي {val_res}، ومجموع أرقامها {sum_digits}.')
    if k == 54:
        players = a * 4 + 4; matches = players - 1
        return item('tournament-knockout-matches', 'Combinatorics',
                    f'In a single-elimination table tennis tournament with {players} players, each match eliminates one player. How many total matches are played to determine the champion?',
                    f'في بطولة كرة طاولة بنظام خروج المغلوب تضم {players} لاعبًا، تُقصي كل مباراة خاسرًا واحدًا. كم مباراة تُلعب إجمالاً لتحديد البطل؟',
                    matches, f'Each match eliminates one player, so {players} − 1 = {matches} matches are required.',
                    f'كل مباراة تُقصي لاعبًا واحدًا، لذا يلزم {players} − 1 = {matches} مباراة.')
    if k == 55:
        int1 = 35 + a * 5; int2 = 45 + b * 5; ext_ang = int1 + int2
        return item('triangle-exterior-angle', 'Geometry',
                    f'An exterior angle of a triangle equals the sum of the two opposite interior angles. If these interior angles measure {int1}° and {int2}°, find the exterior angle in degrees.',
                    f'الزاوية الخارجية للمثلث تساوي مجموع الزاويتين الداخليتين المقابلتين. إذا كان قياساهما {int1}° و{int2}°، فما قياس الزاوية الخارجية بالدرجات؟',
                    ext_ang, f'Exterior angle = {int1}° + {int2}° = {ext_ang}°.',
                    f'الزاوية الخارجية = {int1}° + {int2}° = {ext_ang}°.')
    if k == 56:
        ans_rate = a + 2; cost_tot = ans_rate * b
        return item('unit-rate-comparison', 'Numbers and Operations',
                    f'A buyer pays {cost_tot} riyals for {b} notebooks of the same kind. What is the price of one notebook in riyals?',
                    f'دفع مشترٍ {cost_tot} ريالًا ثمنًا لـ{b} دفاتر من النوع نفسه. ما سعر الدفتر الواحد بالريال؟',
                    ans_rate, f'Unit price = {cost_tot} ÷ {b} = {ans_rate} riyals.',
                    f'سعر الوحدة = {cost_tot} ÷ {b} = {ans_rate} ريالًا.', 'Easy')
    if k == 57:
        n_even = 2 * a; ans_prod = n_even * (n_even + 2)
        return item('consecutive-even-product', 'Number Theory',
                    f'What is the product of the two consecutive even integers {n_even} and {n_even + 2}?',
                    f'ما حاصل ضرب العددين الزوجيين المتتاليين {n_even} و{n_even + 2}؟',
                    ans_prod, f'Multiply: {n_even} × {n_even + 2} = {ans_prod}.',
                    f'الضرب: {n_even} × {n_even + 2} = {ans_prod}.')
    if k == 58:
        base_p = a + 5; alt_p = b + 3; area_p = base_p * alt_p
        return item('parallelogram-area-base', 'Geometry',
                    f'A parallelogram has a base of {base_p} cm and a corresponding height of {alt_p} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {base_p} سم والارتفاع المناظر لها {alt_p} سم. ما مساحته بالسنتيمتر المربع؟',
                    area_p, f'Area = base × height = {base_p} × {alt_p} = {area_p} cm².',
                    f'المساحة = القاعدة × الارتفاع = {base_p} × {alt_p} = {area_p} سم².')
    if k == 59:
        den_f = c + 3; num_f = 1; add_litres = a * den_f; total_cap = add_litres * den_f // (den_f - num_f)
        # Simplify: empty fraction is 1/den_f, so adding fills (den_f - 1)/den_f
        # Let us make it integer:
        total_cap = (a + 2) * den_f
        added_litres = total_cap - (a + 2)
        return item('water-tank-capacity', 'Measurement',
                    f'A water tank is {m(f"\\frac{{1}}{{{den_f}}}")} full. Adding {added_litres} litres fills it completely. What is the full capacity of the tank in litres?',
                    f'خزان ماء ممتلئ بنسبة {m(f"\\frac{{1}}{{{den_f}}}")}. إضافة {added_litres} لترًا تملؤه تمامًا. ما سعة الخزان الكاملة باللتر؟',
                    total_cap, f'The empty part is {den_f - 1}/{den_f} of the tank. Full capacity = {added_litres} × {den_f}/({den_f - 1}) = {total_cap} litres.',
                    f'الجزء الفارغ يمثل {den_f - 1}/{den_f}. السعة الكلية = {total_cap} لترًا.')
    if k == 60:
        ans_cyl = a * a * c
        return item('cylinder-volume-factor', 'Geometry',
                    f'A circular cylinder has base radius {a} cm and height {c} cm. What is its volume divided by π, in cm³?',
                    f'أسطوانة دائرية نصف قطر قاعدتها {a} سم وارتفاعها {c} سم. ما حجمها مقسومًا على π بالسنتيمتر المكعب؟',
                    ans_cyl, f'Volume/π = r²h = {a}² × {c} = {ans_cyl}.',
                    f'الحجم مقسومًا على π = r²h = {a}² × {c} = {ans_cyl}.')
    raise ValueError(k)

def senior(k, n, g):
    if k >= 77:
        return senior_families.senior_extra(k, n, g)
    r_local = random.Random(6092026 + k * 10007 + n * 997 + g * 31)
    old_R = R
    try:
        globals()["R"] = r_local
        return _orig_senior(k, n, g)
    finally:
        globals()["R"] = old_R

def _orig_senior(k, n, g):
    a = R.randint(2, 12); b = R.randint(2, 10); c = R.randint(2, 7); x = R.randint(2, 12)
    if k == 0:
        ans_neither = R.randint(2, 9); total = a + b + c
        subjects = [("French", "Spanish", "الفرنسية", "الإسبانية"),
                    ("Art", "Music", "الرسم", "الموسيقى"),
                    ("Physics", "Chemistry", "الفيزياء", "الكيمياء"),
                    ("Swimming", "Running", "السباحة", "الجري")]
        s1, s2, a1, a2 = subjects[n % len(subjects)]
        return item('inclusion-exclusion-union', 'Sets',
                    f'In a class of {total + ans_neither} students, {a + c} study {s1}, {b + c} study {s2}, and {c} study both. How many study neither?',
                    f'في فصل {total + ans_neither} طالبًا، يدرس {a + c} {a1} و{b + c} {a2} و{c} الاثنين معًا. كم طالبًا لا يدرس أيًا منهما؟',
                    ans_neither,
                    f'The union has {a + c}+{b + c}−{c}={total} students. Subtract from {total + ans_neither}: {ans_neither}.',
                    f'عدد الاتحاد {a + c}+{b + c}−{c}={total}. نطرح من {total + ans_neither} فنحصل على {ans_neither}.')
    if k == 1:
        nset = a + 1; ans = 2**nset - 2
        return item('nontrivial-subsets', 'Sets',
                    f'A set has {nset} elements. How many subsets are neither empty nor equal to the whole set?',
                    f'لمجموعة {nset} عنصرًا. كم مجموعة جزئية ليست خالية وليست مساوية للمجموعة الأصلية؟',
                    ans, f'There are 2^{nset} subsets; exclude the empty set and whole set: 2^{nset}−2={ans}.',
                    f'عدد المجموعات الجزئية 2^{nset}. نستبعد الخالية والأصلية: 2^{nset}−2={ans}.')
    if k == 2:
        ans = a * a + b * b
        return item('quadratic-root-squares', 'Quadratic Equations',
                    f'If α and β are the roots of {m(f"z^2-{a+b}z+{a*b}=0")}, find {m("α^2+β^2")} .',
                    f'إذا كان α وβ جذري المعادلة {m(f"z^2-{a+b}z+{a*b}=0")}، أوجد {m("α^2+β^2")} .',
                    ans, f'Vieta gives α+β={a+b} and αβ={a*b}. Hence α²+β²=({a+b})²−2({a*b})={ans}.',
                    f'من علاقات فييتا α+β={a+b} وαβ={a*b}. إذن α²+β²=({a+b})²−2({a*b})={ans}.')
    if k == 3:
        ans = a * a + b * b
        return item('complex-conjugate-product', 'Complex Numbers',
                    f'Let {m(f"z={a}+{b}i")}. Find {m("z\\overline{z}")} .',
                    f'ليكن {m(f"z={a}+{b}i")}. أوجد {m("z\\overline{z}")} .',
                    ans, f'z times its conjugate equals |z|²={a}²+{b}²={ans}.',
                    f'حاصل ضرب العدد في مرافقه يساوي مربع معياره: {a}²+{b}²={ans}.', 'Easy')
    if k == 4:
        ans = a * c - b
        return item('determinant-parameter', 'Matrices and Determinants',
                    f'The determinant of {m(f"\\begin{{pmatrix}}{a}&1\\\\{b}&t\\end{{pmatrix}}") } is {ans}. Find t.',
                    f'محدد المصفوفة {m(f"\\begin{{pmatrix}}{a}&1\\\\{b}&t\\end{{pmatrix}}")} يساوي {ans}. أوجد t.',
                    c, f'The determinant is {a}t−{b}. Thus {a}t={ans+b}, giving t={c}.',
                    f'المحدد {a}t−{b}. إذن {a}t={ans+b}، ومنه t={c}.')
    if k == 5:
        people = a + 3; ans = math.comb(people, 3)
        return item('committee-unordered', 'Combinatorics',
                    f'How many three-person committees can be formed from {people} people, with no roles assigned?',
                    f'كم لجنة من ثلاثة أشخاص يمكن تشكيلها من {people} شخصًا دون توزيع مناصب؟',
                    ans, f'Order does not matter, so use combinations: {people}×{people-1}×{people-2}/6={ans}.',
                    f'الترتيب غير مهم؛ نستخدم التوافيق: {people}×{people-1}×{people-2}/6={ans}.')
    if k == 6:
        degree = a + 2; ans = math.comb(degree, 2) * b * b
        return item('binomial-coefficient', 'Binomial Theorem',
                    f'Find the coefficient of {m("x^2")} in {m(f"(1+{b}x)^{{{degree}}}")} .',
                    f'أوجد معامل {m("x^2")} في مفكوك {m(f"(1+{b}x)^{{{degree}}}")} .',
                    ans, f'Choose the x term from two factors: C({degree},2)×{b}²={ans}.',
                    f'نختار حد x من عاملين: C({degree},2)×{b}²={ans}.')
    if k == 7:
        terms = a + 4; ans = F(terms * (2 * b + (terms - 1) * c), 2)
        return item('arithmetic-series', 'Sequences',
                    f'An arithmetic progression starts with {b} and has common difference {c}. Find the sum of its first {terms} terms.',
                    f'متتابعة حسابية حدها الأول {b} وفرقها {c}. أوجد مجموع أول {terms} حدًا.',
                    ans, f'The last term is {b+(terms-1)*c}. Sum = {terms}({b}+{b+(terms-1)*c})/2={val(ans)}.',
                    f'الحد الأخير {b+(terms-1)*c}. المجموع = {terms}({b}+{b+(terms-1)*c})/2={val(ans)}.')
    if k == 8:
        ans = F(a * b, b - 1)
        return item('geometric-infinite', 'Sequences',
                    f'Find the sum of the infinite geometric series with first term {a} and common ratio {m(val(F(1,b)))}.',
                    f'أوجد مجموع المتسلسلة الهندسية غير المنتهية التي حدها الأول {a} وأساسها {m(val(F(1,b)))}.',
                    ans, f'The ratio has absolute value below 1, so S=a/(1−r)={m(val(ans))}.',
                    f'القيمة المطلقة للأساس أقل من 1، لذا المجموع a/(1−r)={m(val(ans))}.')
    if k == 9:
        ans = 2 * a
        return item('removable-discontinuity', 'Limits and Continuity',
                    f'For x≠{a}, {m(f"f(x)=\\frac{{x^2-{a*a}}}{{x-{a}}}")}. What value of f({a}) makes f continuous?',
                    f'عندما x≠{a}، تكون {m(f"f(x)=\\frac{{x^2-{a*a}}}{{x-{a}}}")}. ما قيمة f({a}) التي تجعل الدالة متصلة؟',
                    ans, f'Factor x²−{a*a}=(x−{a})(x+{a}). Away from the missing point f(x)=x+{a}, whose limit is {2*a}.',
                    f'نحلل البسط إلى (x−{a})(x+{a})، فتكون الدالة x+{a} خارج النقطة المحذوفة، ونهايتها {2*a}.')
    if k == 10:
        ans = 3 * a * x * x + 2 * b * x + c
        return item('polynomial-tangent-slope', 'Differential Calculus',
                    f'Find the slope of the tangent to {m(f"y={a}x^3+{b}x^2+{c}x")} at x={x}.',
                    f'أوجد ميل المماس للمنحنى {m(f"y={a}x^3+{b}x^2+{c}x")} عند x={x}.',
                    ans, f'Differentiate: y′={3*a}x²+{2*b}x+{c}. At x={x}, the slope is {ans}.',
                    f'بالتفاضل y′={3*a}x²+{2*b}x+{c}. عند x={x} يكون الميل {ans}.')
    if k == 11:
        ans = F(a, 3) + F(b, 2) + c
        return item('integral-polynomial', 'Integral Calculus',
                    f'Evaluate {m(f"\\int_0^1 ({a}x^2+{b}x+{c})\\,dx")} .',
                    f'احسب {m(f"\\int_0^1 ({a}x^2+{b}x+{c})\\,dx")} .',
                    ans, f'Integrate term by term and evaluate at 1 and 0: {a}/3+{b}/2+{c}={m(val(ans))}.',
                    f'نكامل حدًا حدًا ونعوض بالحدين 1 و0: {a}/3+{b}/2+{c}={m(val(ans))}.')
    if k == 12:
        ans = a * x * x + b
        return item('initial-value-polynomial', 'Differential Equations',
                    f'A function satisfies {m(f"y\x27={2*a}x")} and y(0)={b}. Find y({x}).',
                    f'تحقق دالة {m(f"y\x27={2*a}x")} وy(0)={b}. أوجد y({x}).',
                    ans, f'Integrating gives y={a}x²+C. The initial value gives C={b}. Thus y({x})={ans}.',
                    f'بالتكامل y={a}x²+C، والشرط الابتدائي يعطي C={b}. إذن y({x})={ans}.')
    if k == 13:
        return item('line-intercept-triangle', 'Coordinate Geometry',
                    f'A line joins ({2*a},0) and (0,{2*b}). Find the area of the triangle it forms with the coordinate axes.',
                    f'يصل مستقيم بين ({2*a}،0) و(0،{2*b}). أوجد مساحة المثلث الذي يكونه مع محوري الإحداثيات.',
                    2 * a * b, f'The perpendicular base and height are {2*a} and {2*b}. Area = ½×{2*a}×{2*b}={2*a*b}.',
                    f'القاعدة والارتفاع المتعامدان {2*a} و{2*b}. المساحة = ½×{2*a}×{2*b}={2*a*b}.')
    if k == 14:
        ans = a * a + b * b + c * c
        return item('space-distance-squared', '3D Geometry',
                    f'Find the square of the distance between P(1,2,3) and Q({a+1},{b+2},{c+3}).',
                    f'أوجد مربع المسافة بين P(1،2،3) وQ({a+1}،{b+2}،{c+3}).',
                    ans, f'The coordinate differences are {a},{b},{c}; squared distance is {a}²+{b}²+{c}²={ans}.',
                    f'فروق الإحداثيات {a} و{b} و{c}؛ مربع المسافة {a}²+{b}²+{c}²={ans}.')
    if k == 15:
        ans = -(a + b)
        return item('orthogonal-vector-parameter', 'Vectors',
                    f'The vectors ({a},{b},1) and (1,1,t) are perpendicular. Find t.',
                    f'المتجهان ({a}،{b}،1) و(1،1،t) متعامدان. أوجد t.',
                    ans, f'Perpendicular vectors have dot product zero: {a}+{b}+t=0, so t={ans}.',
                    f'الضرب القياسي لمتجهين متعامدين يساوي صفرًا: {a}+{b}+t=0، ومنه t={ans}.')
    if k == 16:
        ans = F(a * (a - 1), (a + b) * (a + b - 1))
        return item('without-replacement-pair', 'Probability',
                    f'A bag contains {a} red and {b} blue balls. Two are drawn uniformly without replacement. What is the probability both are red?',
                    f'في كيس {a} كرات حمراء و{b} زرقاء. سُحبت كرتان عشوائيًا دون إرجاع. ما احتمال أن تكونا حمراوين؟',
                    ans, f'Multiply the conditional probabilities: {a}/{a+b} × {a-1}/{a+b-1} = {m(val(ans))}.',
                    f'نضرب الاحتمالين الشرطيين: {a}/{a+b} × {a-1}/{a+b-1} = {m(val(ans))}.')
    if k == 17:
        ans = F(2 * b * b, 3)
        return item('population-variance', 'Statistics',
                    f'Find the population variance of {a-b}, {a}, {a+b}.',
                    f'أوجد تباين المجتمع للأعداد {a-b} و{a} و{a+b}.',
                    ans, f'The mean is {a}. The squared deviations are {b*b},0,{b*b}. Divide their sum by 3: {m(val(ans))}.',
                    f'المتوسط {a}، ومربعات الانحرافات {b*b} و0 و{b*b}. نقسم مجموعها على 3: {m(val(ans))}.')
    if k == 18:
        ans = F(2 * a * b, a * a + b * b)
        return item('trig-double-angle', 'Trigonometry',
                    f'For an acute angle θ, {m(f"\\tan θ={val(F(a,b))}")}. Find {m("\\sin 2θ")} .',
                    f'لزاوية حادة θ، {m(f"\\tan θ={val(F(a,b))}")}. أوجد {m("\\sin 2θ")} .',
                    ans, f'Use sin(2θ)=2tanθ/(1+tan²θ). Substitution gives {m(val(ans))}.',
                    f'نستخدم sin(2θ)=2tanθ/(1+tan²θ). بالتعويض نحصل على {m(val(ans))}.')
    if k == 19:
        mod = R.choice([5, 7, 11, 13, 17]); exp = a + 5; ans = pow(b, exp, mod)
        return item('power-modulo', 'Number Theory',
                    f'Find the remainder when {m(f"{b}^{{{exp}}}")} is divided by {mod}.',
                    f'أوجد باقي قسمة {m(f"{b}^{{{exp}}}")} على {mod}.',
                    ans, f'Reduce successive products modulo {mod}. The residue is {ans}.',
                    f'نختزل الضرب المتكرر بترديد {mod}. الباقي {ans}.')
    if k == 20:
        w = a + 2; h = b + 2; ans = math.comb(w + h, w) - math.comb(2, 1) * math.comb(w + h - 2, w - 1)
        return item('grid-avoid-point', 'Combinatorics',
                    f'A path from (0,0) to ({w},{h}) uses only unit steps right or up. How many such paths avoid (1,1)?',
                    f'مسار من (0،0) إلى ({w}،{h}) يستخدم خطوات وحدة يمينًا أو إلى أعلى فقط. كم مسارًا لا يمر بالنقطة (1،1)؟',
                    ans, f'All paths: C({w+h},{w}). Avoid (1,1): subtract 2×C({w+h-2},{w-1}) = {ans}.',
                    f'كل المسارات C({w+h}،{w})، نطرح المارة بـ(1،1): {ans}.', 'Hard')
    if k == 21:
        ans = sum(math.gcd(i, a * b) == 1 for i in range(1, a * b + 1))
        return item('coprime-count', 'Number Theory',
                    f'How many integers from 1 to {a*b} inclusive are relatively prime to {a*b}?',
                    f'كم عددًا صحيحًا من 1 إلى {a*b} شاملًا الطرفين أولي نسبيًا مع {a*b}؟',
                    ans, f'Euler totient φ({a*b}) = {ans}.',
                    f'دالة أويلر φ({a*b}) = {ans}.', 'Hard')
    if k == 22:
        ans = (a + b)**2
        return item('fixed-sum-minimum-square', 'Inequalities',
                    f'Positive real numbers x and y satisfy x+y={2*(a+b)}. Find the smallest possible value of {m("(x^2+y^2)/2")} .',
                    f'عددان حقيقيان موجبان x وy يحققان x+y={2*(a+b)}. أوجد أصغر قيمة لـ{m("(x^2+y^2)/2")} .',
                    ans, f'By AM-QM inequality, (x²+y²)/2 ≥ ((x+y)/2)² = {ans}.',
                    f'من متراجحة الوسطين، (x²+y²)/2 ≥ {ans}.')
    if k == 23:
        ans = F(a + b, c)
        return item('rational-equation-exclusion', 'Algebra',
                    f'Solve {m(f"\\frac{{{a}}}{{x}}+\\frac{{{b}}}{{x}}={c}")} for real x≠0.',
                    f'حل المعادلة {m(f"\\frac{{{a}}}{{x}}+\\frac{{{b}}}{{x}}={c}")} حيث x حقيقي لا يساوي صفرًا.',
                    ans, f'Combine fractions: {a+b}/x={c} ⇒ x={m(val(ans))}.',
                    f'بجمع الكسرين {a+b}/x={c} إذن x={m(val(ans))}.')
    if k == 24:
        total = a + 5; ans = total * (total - 1) // 2
        return item('handshakes-graph', 'Combinatorics',
                    f'{total} people each shake hands with every other person exactly once. How many handshakes occur?',
                    f'يتصافح {total} شخصًا بحيث يصافح كل منهم جميع الآخرين مرة واحدة. كم مصافحة تحدث؟',
                    ans, f'Total handshakes = {total}×{total-1}/2 = {ans}.',
                    f'عدد المصافحات = {total}×{total-1}/2 = {ans}.')
    if k == 25:
        ans = math.gcd(a * b, a * c)
        return item('greatest-square-tiling', 'Number Theory',
                    f'A {a*b} cm by {a*c} cm rectangle is tiled with identical squares of integer side length, aligned with its sides, without cuts. What is the largest possible square side length?',
                    f'نغطي مستطيلًا أبعاده {a*b} سم و{a*c} سم بمربعات متطابقة أطوال أضلاعها أعداد صحيحة، موازية لأضلاعه ودون قص. ما أكبر طول ممكن لضلع المربع؟',
                    ans, f'Side length must be gcd({a*b}, {a*c}) = {ans}.',
                    f'طول الضلع هو القاسم المشترك الأكبر gcd({a*b}، {a*c}) = {ans}.')
    # NEW SENIOR FAMILIES (26 through 76)
    if k == 26:
        ans_pair = a * b + b * c + c * a
        return item('vieta-cubic-sum-products', 'Algebra',
                    f'If α, β, and γ are the roots of {m(f"x^3 - {a+b+c}x^2 + {ans_pair}x - {a*b*c} = 0")}, find the value of {m("αβ + βγ + γα")}.',
                    f'إذا كان α وβ وγ جذور المعادلة {m(f"x^3 - {a+b+c}x^2 + {ans_pair}x - {a*b*c} = 0")}، فما قيمة {m("αβ + βγ + γα")}؟',
                    ans_pair, f'By Vieta’s formulas, the sum of pairwise products of roots is the coefficient of x: {ans_pair}.',
                    f'من علاقات فييتا، مجموع حواصل ضرب الجذور مثنى مثنى هو معامل x: {ans_pair}.')
    if k == 27:
        p_exp = c + 2
        return item('logarithm-change-base', 'Algebra',
                    f'Evaluate {m(f"\\log_{{{a}}}({b}) \\cdot \\log_{{{b}}}({a}^{{{p_exp}}})")}.',
                    f'احسب قيمة {m(f"\\log_{{{a}}}({b}) \\cdot \\log_{{{b}}}({a}^{{{p_exp}}})")}.',
                    p_exp, f'By change of base: (ln({b})/ln({a})) × ({p_exp} ln({a})/ln({b})) = {p_exp}.',
                    f'بتغيير الأساس نحصل على {p_exp}.')
    if k == 28:
        diam_circ = 2 * a
        return item('trig-sine-rule', 'Trigonometry',
                    f'In triangle ABC, side a = {a} cm and the opposite angle A = 30°. Find the diameter of the circumcircle in cm.',
                    f'في المثلث ABC، طول الضلع a = {a} سم والزاوية المقابلة A = 30°. ما طول قطر الدائرة المحيطة بالسنتيمتر؟',
                    diam_circ, f'By the Law of Sines, diameter 2R = a / sin(30°) = {a} / 0.5 = {diam_circ} cm.',
                    f'بقانون الجيوب، القطر 2R = a / sin(30°) = {diam_circ} سم.')
    if k == 29:
        return item('definite-integral-odd-symmetric', 'Integral Calculus',
                    f'Evaluate {m(f"\\int_{{-{a}}}^{{{a}}} ({b}x^3 + {c}x)\\,dx")}.',
                    f'احسب {m(f"\\int_{{-{a}}}^{{{a}}} ({b}x^3 + {c}x)\\,dx")}.',
                    0, f'The integrand is an odd function integrated over a symmetric interval [−{a}, {a}], so the integral is 0.',
                    f'الدالة فردية ومجال التكامل متماثل حول الصفر [−{a}، {a}]، فالناتج 0.')
    if k == 30:
        ans_tr = a + c
        return item('matrix-trace', 'Matrices and Determinants',
                    f'Find the trace of the matrix {m(f"\\begin{{pmatrix}} {a} & {b} \\\\ {x} & {c} \\end{{pmatrix}}")}.',
                    f'أوجد أثر المصفوفة {m(f"\\begin{{pmatrix}} {a} & {b} \\\\ {x} & {c} \\end{{pmatrix}}")}.',
                    ans_tr, f'Trace is the sum of main diagonal entries: {a} + {c} = {ans_tr}.',
                    f'أثر المصفوفة هو مجموع عناصر القطر الرئيسي: {a} + {c} = {ans_tr}.', 'Easy')
    if k == 31:
        ans_dist = abs(b - c) or 1
        return item('circle-tangent-radius', 'Coordinate Geometry',
                    f'A circle centered at ({a}, {b}) is tangent to the horizontal line y = {b - ans_dist}. Find its radius.',
                    f'دائرة مركزها ({a}، {b}) وتمس المستقيم الأفقي y = {b - ans_dist}. أوجد نصف قطرها.',
                    ans_dist, f'The radius is the perpendicular distance from the center to the tangent line: |{b} − ({b - ans_dist})| = {ans_dist}.',
                    f'نصف القطر هو البعد العمودي من المركز إلى المماس: {ans_dist}.')
    if k == 32:
        return item('conditional-card-probability', 'Probability',
                    f'A card is drawn from a standard 52-card deck. Given that the card is a face card (Jack, Queen, King), what is the probability that it is a King?',
                    f'سُحبت بطاقة من حزمة لعب عادية تحوي 52 بطاقة. إذا عُلم أن البطاقة صورة (ولد، بنت، شايب)، فما احتمال أن تكون شايبًا؟',
                    F(1, 3), f'There are 12 face cards in total, 4 of which are Kings. Probability = 4/12 = 1/3.',
                    f'يوجد 12 بطاقة صورة منها 4 شيبان. الاحتمال = 4/12 = 1/3.')
    if k == 33:
        ans_geom = a * (2**4 - 1)
        return item('geometric-sum-finite', 'Sequences',
                    f'Find the sum of the first 4 terms of a geometric progression with first term {a} and common ratio 2.',
                    f'أوجد مجموع أول 4 حدود من متتالية هندسية حدها الأول {a} وأساسها 2.',
                    ans_geom, f'Sum = a(r⁴ − 1)/(r − 1) = {a}(16 − 1)/1 = {ans_geom}.',
                    f'المجموع = {a}(16 − 1) = {ans_geom}.')
    if k == 34:
        ans_dot = a * b
        return item('vector-dot-product-angle', 'Vectors',
                    f'Find the dot product of the vectors u = ({a}, 0) and v = ({b}, {c}).',
                    f'أوجد الضرب القياسي للمتجهين u = ({a}، 0) وv = ({b}، {c}).',
                    ans_dot, f'Dot product = ({a})({b}) + (0)({c}) = {ans_dot}.',
                    f'الضرب القياسي = ({a})({b}) + 0 = {ans_dot}.', 'Easy')
    if k == 35:
        return item('limit-exponential-form', 'Limits and Continuity',
                    f'Evaluate {m(f"\\lim_{{x \\to 0}} \\frac{{e^{{{a}x}} - 1}}{{x}}")}.',
                    f'احسب {m(f"\\lim_{{x \\to 0}} \\frac{{e^{{{a}x}} - 1}}{{x}}")}.',
                    a, f'Using L’Hôpital’s Rule or the definition of derivative, the limit is {a}.',
                    f'باستخدام قاعدة لوبيتال أو تعريف المشتقة، النهاية هي {a}.')
    if k == 36:
        ans_sq = a * a + b * b
        return item('complex-modulus-square', 'Complex Numbers',
                    f'If {m(f"z = {a} + {b}i")}, find {m("|z|^2")}.',
                    f'إذا كان {m(f"z = {a} + {b}i")}، فما قيمة {m("|z|^2")}؟',
                    ans_sq, f'|z|² = a² + b² = {a}² + {b}² = {ans_sq}.',
                    f'|z|² = {a}² + {b}² = {ans_sq}.', 'Easy')
    if k == 37:
        return item('parabola-vertex-abscissa', 'Coordinate Geometry',
                    f'Find the x-coordinate of the vertex of the parabola {m(f"y = {a}x^2 - {2*a*b}x + {c}")}.',
                    f'أوجد الإحداثي السيني لرأس القطع المكافئ {m(f"y = {a}x^2 - {2*a*b}x + {c}")}.',
                    b, f'The vertex occurs at x = −b/(2a) = {2*a*b}/(2×{a}) = {b}.',
                    f'إحداثي الرأس x = −b/(2a) = {b}.')
    if k == 38:
        ans_leg = 10 // 2 + 10 // 4 + 10 // 8
        return item('legendre-formula-factorial', 'Number Theory',
                    f'What is the highest power of 2 that divides 10! (ten factorial)?',
                    f'ما أكبر قوة للعدد 2 تقسم !10 (مضروب 10)؟',
                    ans_leg, f'By Legendre’s formula: ⌊10/2⌋ + ⌊10/4⌋ + ⌊10/8⌋ = 5 + 2 + 1 = {ans_leg}.',
                    f'بصيغة ليجاندر: 5 + 2 + 1 = {ans_leg}.')
    if k == 39:
        ans_ev = F(7 * a, 2)
        return item('expected-value-fair-die', 'Probability',
                    f'A game pays {a} times the number rolled on a fair 6-sided die. What is the expected payout in riyals?',
                    f'لعبة تدفع {a} أضعاف الرقم الظاهر على نرد عادل ذي 6 أوجه. ما القيمة المتوقعة للمكسب بالريال؟',
                    ans_ev, f'Expected roll is 3.5. Expected payout = {a} × 3.5 = {m(val(ans_ev))}.',
                    f'توقع النرد 3.5. المكسب المتوقع = {m(val(ans_ev))}.')
    if k == 40:
        people_c = c + 1; ans_circ = math.factorial(people_c - 1)
        return item('circular-permutations', 'Combinatorics',
                    f'In how many distinct ways can {people_c} people be arranged around a circular table, where rotations are considered equivalent?',
                    f'بكم طريقة مختلفة يمكن جلوس {people_c} أشخاص حول طاولة دائرية، مع اعتبار التدوير متكافئًا؟',
                    ans_circ, f'Circular permutations = (n − 1)! = ({people_c} − 1)! = {ans_circ}.',
                    f'التباديل الدائرية = (n − 1)! = {ans_circ}.')
    if k == 41:
        ans_quot = F(a, b)
        return item('derivative-quotient-rule', 'Differential Calculus',
                    f'Find the derivative of {m(f"f(x) = \\frac{{{a}x}}{{x + {b}}}")} evaluated at x = 0.',
                    f'أوجد مشتقة الدالة {m(f"f(x) = \\frac{{{a}x}}{{x + {b}}}")} عند x = 0.',
                    ans_quot, f'f′(x) = {a*b}/(x+{b})². At x=0, f′(0) = {a*b}/{b**2} = {m(val(ans_quot))}.',
                    f'المشتقة f′(0) = {m(val(ans_quot))}.')
    if k == 42:
        return item('roots-of-unity-sum', 'Complex Numbers',
                    f'What is the sum of all {a + 3} distinct complex roots of the equation {m(f"z^{{{a+3}}} = 1")}?',
                    f'ما مجموع جميع الجذور المركبة المختلفة الـ{a+3} للمعادلة {m(f"z^{{{a+3}}} = 1")}؟',
                    0, f'The sum of all n-th roots of unity for n ≥ 2 is 0.',
                    f'مجموع الجذور النونية للواحد الصحيح لأي n ≥ 2 يساوي 0.')
    if k == 43:
        ans_cos = a
        return item('trig-cosine-law-equilateral', 'Trigonometry',
                    f'In triangle ABC, side b = {a} cm, side c = {a} cm, and angle A = 60°. Find the length of side a in cm.',
                    f'في المثلث ABC، طول b = {a} سم وc = {a} سم والزاوية A = 60°. ما طول الضلع a بالسنتيمتر؟',
                    ans_cos, f'By the Law of Cosines, a² = b² + c² − 2bc cos(60°) = {a}² + {a}² − {a}² = {a}², so a = {a} cm.',
                    f'بقانون جيوب التمام ينتج a = {a} سم.')
    if k == 44:
        ans_foc = a * a - b * b if a > b else b * b - a * a
        if ans_foc == 0: ans_foc = 7
        return item('ellipse-focal-distance-squared', 'Coordinate Geometry',
                    f'For the ellipse {m(f"\\frac{{x^2}}{{{max(a,b)**2}}} + \\frac{{y^2}}{{{min(a,b)**2}}} = 1")}, find the square of the focal distance c².',
                    f'للقطع الناقص {m(f"\\frac{{x^2}}{{{max(a,b)**2}}} + \\frac{{y^2}}{{{min(a,b)**2}}} = 1")}، أوجد مربع البعد البؤري c².',
                    ans_foc, f'c² = a² − b² = {max(a,b)**2} − {min(a,b)**2} = {ans_foc}.',
                    f'c² = {ans_foc}.')
    if k == 45:
        return item('derangements-count-four', 'Combinatorics',
                    f'How many derangements (permutations where no element appears in its original position) exist for a set of 4 distinct items?',
                    f'كم عدد التباديل اللاموضعية (التي لا يبقى فيها أي عنصر في موضعه الأصلي) لمجموعة من 4 عناصر مختلفة؟',
                    9, f'D(4) = 4!(1 − 1/1! + 1/2! − 1/3! + 1/4!) = 24(1/2 − 1/6 + 1/24) = 9.',
                    f'عدد التباديل اللاموضعية لأربعة عناصر هو 9.')
    if k == 46:
        p_wilson = R.choice([5, 7, 11, 13])
        return item('wilson-theorem-residue', 'Number Theory',
                    f'Find the remainder when ({p_wilson} − 1)! is divided by {p_wilson}.',
                    f'أوجد باقي قسمة !({p_wilson} − 1) على {p_wilson}.',
                    p_wilson - 1, f'By Wilson’s Theorem, (p − 1)! ≡ −1 ≡ p − 1 (mod p). So the remainder is {p_wilson - 1}.',
                    f'بمبرهنة ويلسون، الباقي هو {p_wilson - 1}.')
    if k == 47:
        ans_area = F(a, 6)
        return item('area-between-curves-parabola', 'Integral Calculus',
                    f'Find the area of the region enclosed between the curve {m(f"y = {a}x^2")} and the line {m(f"y = {a}x")} for x ≥ 0.',
                    f'أوجد مساحة المنطقة المحصورة بين المنحنى {m(f"y = {a}x^2")} والمستقيم {m(f"y = {a}x")} حيث x ≥ 0.',
                    ans_area, f'Intersections at x=0 and x=1. Area = ∫₀¹ ({a}x − {a}x²) dx = {a}(1/2 − 1/3) = {m(val(ans_area))}.',
                    f'المساحة = {m(val(ans_area))}.')
    if k == 48:
        ans_slope = F(b, a)
        return item('hyperbola-asymptotes-slope', 'Coordinate Geometry',
                    f'Find the positive slope of the asymptotes of the hyperbola {m(f"\\frac{{x^2}}{{{a*a}}} - \\frac{{y^2}}{{{b*b}}} = 1")}.',
                    f'أوجد الميل الموجب لخطوط التقارب للقطع الزائد {m(f"\\frac{{x^2}}{{{a*a}}} - \\frac{{y^2}}{{{b*b}}} = 1")}.',
                    ans_slope, f'The asymptotes are y = ±(b/a)x. The positive slope is {b}/{a} = {m(val(ans_slope))}.',
                    f'الميل الموجب هو b/a = {m(val(ans_slope))}.')
    if k == 49:
        return item('binomial-probability-coin-three', 'Probability',
                    f'A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads?',
                    f'أُلقيت قطعة نقدية عادلة 3 مرات. ما احتمال الحصول على صورتين بالضبط؟',
                    F(3, 8), f'Number of ways = C(3, 2) = 3. Total outcomes = 2³ = 8. Probability = 3/8.',
                    f'عدد الطرق = 3 من أصل 8، فاحتمالها 3/8.')
    if k == 50:
        ans_prod_diag = a * c
        return item('matrix-determinant-triangular', 'Matrices and Determinants',
                    f'Find the determinant of the upper triangular matrix {m(f"\\begin{{pmatrix}} {a} & {b} \\\\ 0 & {c} \\end{{pmatrix}}")}.',
                    f'أوجد محدد المصفوفة المثلثية العلوية {m(f"\\begin{{pmatrix}} {a} & {b} \\\\ 0 & {c} \\end{{pmatrix}}")}.',
                    ans_prod_diag, f'The determinant of a triangular matrix is the product of its diagonal entries: {a} × {c} = {ans_prod_diag}.',
                    f'محدد المصفوفة المثلثية هو حاصل ضرب عناصر القطر: {ans_prod_diag}.', 'Easy')
    if k == 51:
        ans_hm = F(2 * a * b, a + b)
        return item('harmonic-mean-two-numbers', 'Sequences',
                    f'Find the harmonic mean of the numbers {a} and {b}.',
                    f'أوجد المتوسط التوافقي للعددين {a} و{b}.',
                    ans_hm, f'Harmonic mean = 2ab / (a + b) = 2({a})({b})/({a}+{b}) = {m(val(ans_hm))}.',
                    f'المتوسط التوافقي = 2ab / (a + b) = {m(val(ans_hm))}.')
    if k == 52:
        ans_cross = a * b
        return item('vector-cross-product-magnitude', 'Vectors',
                    f'Find the magnitude of the cross product of u = ({a}, 0, 0) and v = (0, {b}, 0).',
                    f'أوجد مقدار حاصل الضرب الاتجاهي للمتجهين u = ({a}، 0، 0) وv = (0، {b}، 0).',
                    ans_cross, f'u × v = (0, 0, {a*b}), so |u × v| = {ans_cross}.',
                    f'مقدار الضرب الاتجاهي = {ans_cross}.', 'Easy')
    if k == 53:
        return item('mod-inverse-prime', 'Number Theory',
                    f'Find the multiplicative inverse of 3 modulo 7 in the range {{1, 2, ..., 6}}.',
                    f'أوجد المعكوس الضربي للعدد 3 بترديد 7 في النطاق {{1، 2، ...، 6}}.',
                    5, f'3 × 5 = 15 ≡ 1 (mod 7), so the inverse is 5.',
                    f'3 × 5 = 15 ≡ 1 بترديد 7، إذن المعكوس 5.')
    if k == 54:
        return item('inflection-point-cubic', 'Differential Calculus',
                    f'Find the x-coordinate of the inflection point of the cubic curve {m(f"y = x^3 - {3*a}x^2 + {b}x + {c}")}.',
                    f'أوجد الإحداثي السيني لنقطة الانقلاب لمنحنى الدالة التكعيبية {m(f"y = x^3 - {3*a}x^2 + {b}x + {c}")}.',
                    a, f'y″ = 6x − {6*a} = 0 ⇒ x = {a}.',
                    f'المشتقة الثانية y″ = 6x − {6*a} = 0 ومنه x = {a}.')
    if k == 55:
        ans_param = b - 1
        return item('continuous-piecewise-parameter', 'Limits and Continuity',
                    f'A function is defined by f(x) = ax + 2 for x ≤ 1 and f(x) = x² + {b} for x > 1. Find the value of a that makes f continuous at x = 1.',
                    f'دالة معرّفة بـ f(x) = ax + 2 عندما x ≤ 1، وf(x) = x² + {b} عندما x > 1. أوجد قيمة a التي تجعل الدالة متصلة عند x = 1.',
                    ans_param, f'Continuity requires a(1) + 2 = 1² + {b} ⇒ a + 2 = 1 + {b} ⇒ a = {ans_param}.',
                    f'الاتصال يتطلب a + 2 = 1 + {b} ومنه a = {ans_param}.')
    if k == 56:
        s_val = 2 * a; ans_cs = F(4, s_val)
        return item('cauchy-schwarz-minimum-reciprocal', 'Inequalities',
                    f'For positive real numbers x and y such that x + y = {s_val}, find the minimum value of {m("\\frac{1}{x} + \\frac{1}{y}")}.',
                    f'لعددين حقيقيين موجبين x وy يحققان x + y = {s_val}، أوجد أصغر قيمة لـ{m("\\frac{1}{x} + \\frac{1}{y}")}.',
                    ans_cs, f'By Cauchy-Schwarz, (x+y)(1/x+1/y) ≥ 4 ⇒ 1/x+1/y ≥ 4/{s_val} = {m(val(ans_cs))}.',
                    f'من كوشي-شفارتز، 1/x+1/y ≥ {m(val(ans_cs))}.')
    if k == 57:
        rate_diff = a * b
        return item('separable-differential-linear', 'Differential Equations',
                    f'If y satisfies {m(f"\\frac{{dy}}{{dx}} = {a}y")} and y(0) = {b}, find the value of {m("y\x27(0)")}.',
                    f'إذا كانت y تحقق {m(f"\\frac{{dy}}{{dx}} = {a}y")} وy(0) = {b}، فما قيمة {m("y\x27(0)")}؟',
                    rate_diff, f'y′(0) = {a} × y(0) = {a} × {b} = {rate_diff}.',
                    f'y′(0) = {a} × {b} = {rate_diff}.', 'Easy')
    if k == 58:
        p_phi = 3; ans_phi = p_phi**2 - p_phi
        return item('euler-totient-prime-power', 'Number Theory',
                    f'Compute the value of Euler’s totient function φ({p_phi**2}).',
                    f'احسب قيمة دالة أويلر φ({p_phi**2}).',
                    ans_phi, f'φ(p²) = p² − p = {p_phi}² − {p_phi} = {ans_phi}.',
                    f'φ(p²) = {ans_phi}.', 'Easy')
    if k == 59:
        return item('stars-and-bars-two-bins', 'Combinatorics',
                    f'How many ways are there to distribute {a} identical coins into 2 distinct piggy banks?',
                    f'بكم طريقة يمكن توزيع {a} قطع نقدية متطابقة على حصالتين مختلفتين؟',
                    a + 1, f'By stars and bars, the number of ways is C({a}+2−1, 2−1) = {a + 1}.',
                    f'باستخدام النجوم والقواطع، عدد الطرق هو {a + 1}.')
    if k == 60:
        rad_pol = a + 2; ans_pol = rad_pol * rad_pol
        return item('polar-to-cartesian-radius-sq', 'Coordinate Geometry',
                    f'A point in polar coordinates has radius r = {rad_pol}. What is the value of {m("x^2 + y^2")} in Cartesian coordinates?',
                    f'نقطة بإحداثيات قطبية نصف قطرها r = {rad_pol}. ما قيمة {m("x^2 + y^2")} بالإحداثيات الديكارتية؟',
                    ans_pol, f'x² + y² = r² = {rad_pol}² = {ans_pol}.',
                    f'x² + y² = r² = {ans_pol}.', 'Easy')
    if k == 61:
        return item('trig-tangent-addition-one', 'Trigonometry',
                    f'If acute angles A and B satisfy tan A = 1/2 and tan B = 1/3, find tan(A + B).',
                    f'إذا كانت الزاويتان الحادتان A وB تحققان tan A = 1/2 وtan B = 1/3، فما قيمة tan(A + B)؟',
                    1, f'tan(A+B) = (tan A + tan B)/(1 − tan A tan B) = (5/6)/(1 − 1/6) = 1.',
                    f'tan(A+B) = (5/6)/(5/6) = 1.')
    if k == 62:
        return item('orthogonal-projection-length-axis', 'Vectors',
                    f'Find the length of the orthogonal projection of the vector v = ({a}, {b}) onto the x-axis.',
                    f'أوجد طول المسقط العمودي للمتجه v = ({a}، {b}) على محور السينات.',
                    a, f'The projection onto the x-axis is ({a}, 0), whose length is {a}.',
                    f'المسقط على محور السينات هو ({a}، 0) وطوله {a}.', 'Easy')
    if k == 63:
        ans_sq_int = F(a**3, 3)
        return item('integral-monomial-square', 'Integral Calculus',
                    f'Evaluate {m(f"\\int_0^{{{a}}} x^2\\,dx")}.',
                    f'احسب {m(f"\\int_0^{{{a}}} x^2\\,dx")}.',
                    ans_sq_int, f'Antiderivative is x³/3 evaluated from 0 to {a}: {a}³/3 = {m(val(ans_sq_int))}.',
                    f'التكامل هو x³/3 بالتعويض من 0 إلى {a}: {m(val(ans_sq_int))}.')
    if k == 64:
        return item('chinese-remainder-simple', 'Number Theory',
                    f'Find the smallest positive integer that leaves a remainder of 1 when divided by 2 and a remainder of 1 when divided by 3.',
                    f'أوجد أصغر عدد صحيح موجب يعطي باقيًا قدره 1 عند قسمته على 2 وباقيًا قدره 1 عند قسمته على 3.',
                    7, f'The integers leaving remainder 1 mod 6 are 1, 7, 13... The smallest greater than 1 is 7.',
                    f'الأعداد هي 1، 7، 13... الأصغر بعد الواحد هو 7.')
    if k == 65:
        ans_amgm = 2 * a
        return item('arithmetic-geometric-mean-min', 'Inequalities',
                    f'For positive real x, find the minimum value of {m(f"x + \\frac{{{a*a}}}{{x}}")}.',
                    f'لكل عدد حقيقي موجب x، أوجد أصغر قيمة لـ{m(f"x + \\frac{{{a*a}}}{{x}}")}.',
                    ans_amgm, f'By AM-GM, x + {a*a}/x ≥ 2√(x × {a*a}/x) = 2×{a} = {ans_amgm}.',
                    f'من متراجحة الوسطين، القيمة الصغرى هي {ans_amgm}.')
    if k == 66:
        n_comb = a + 3; ans_sym = 2 * n_comb
        return item('combination-symmetry-sum', 'Combinatorics',
                    f'Evaluate {m(f"\\binom{{{n_comb}}}{{1}} + \\binom{{{n_comb}}}{{{n_comb-1}}}")}.',
                    f'احسب قيمة {m(f"\\binom{{{n_comb}}}{{1}} + \\binom{{{n_comb}}}{{{n_comb-1}}}")}.',
                    ans_sym, f'C({n_comb}, 1) = {n_comb} and C({n_comb}, {n_comb-1}) = {n_comb}. Sum = {ans_sym}.',
                    f'المجموع = {n_comb} + {n_comb} = {ans_sym}.', 'Easy')
    if k == 67:
        n_elem = c + 1; ans_subsets = 2**n_elem
        return item('power-set-cardinality-count', 'Sets',
                    f'A set contains {n_elem} distinct elements. How many total subsets does it have?',
                    f'تحتوي مجموعة على {n_elem} عناصر مختلفة. كم مجموعة جزئية لها إجمالاً؟',
                    ans_subsets, f'A set with n elements has 2^n subsets: 2^{{{n_elem}}} = {ans_subsets}.',
                    f'عدد المجموعات الجزئية = 2^{{{n_elem}}} = {ans_subsets}.', 'Easy')
    if k == 68:
        chord_len = 8 * c
        return item('circle-chord-distance-pyth', 'Geometry',
                    f'A circle has radius {5*c} cm. A chord is at a distance of {3*c} cm from the centre. What is the length of the chord in cm?',
                    f'دائرة نصف قطرها {5*c} سم، يبعد وتر فيها مسافة {3*c} سم عن المركز. ما طول الوتر بالسنتيمتر؟',
                    chord_len, f'Half-chord = √(({5*c})² − ({3*c})²) = {4*c} cm. Full chord = 2 × {4*c} = {chord_len} cm.',
                    f'نصف الوتر = {4*c} سم، إذن طول الوتر = {chord_len} سم.')
    if k == 69:
        return item('derivative-trig-product-origin', 'Differential Calculus',
                    f'Find the value of the derivative of {m("f(x) = x^2 \\sin x")} at x = 0.',
                    f'أوجد قيمة مشتقة الدالة {m("f(x) = x^2 \\sin x")} عند x = 0.',
                    0, f'f′(x) = 2x sin x + x² cos x. At x = 0, f′(0) = 0.',
                    f'f′(0) = 0.', 'Easy')
    if k == 70:
        ans_gp4 = a * 8
        return item('geometric-progression-fourth-term', 'Sequences',
                    f'A geometric progression has first term {a} and common ratio 2. Find the fourth term.',
                    f'متتالية هندسية حدها الأول {a} وأساسها 2. أوجد الحد الرابع.',
                    ans_gp4, f'a₄ = a₁ × r³ = {a} × 2³ = {ans_gp4}.',
                    f'الحد الرابع = {a} × 8 = {ans_gp4}.', 'Easy')
    if k == 71:
        return item('distance-point-to-line-origin', 'Coordinate Geometry',
                    f'Find the perpendicular distance from the origin (0, 0) to the line {m(f"3x + 4y = {5*c}")}.',
                    f'أوجد البعد العمودي من نقطة الأصل (0، 0) إلى المستقيم {m(f"3x + 4y = {5*c}")}.',
                    c, f'Distance = |c| / √(3² + 4²) = {5*c} / 5 = {c}.',
                    f'البعد = {5*c} / 5 = {c}.')
    if k == 72:
        ans_tr_prod = a * c + b * x
        return item('trace-diagonal-product', 'Matrices and Determinants',
                    f'Find the trace of the product of diagonal matrices {m(f"\\text{{diag}}({a}, {b})")} and {m(f"\\text{{diag}}({c}, {x})")}.',
                    f'أوجد أثر حاصل ضرب المصفوفتين القطريتين {m(f"\\text{{diag}}({a}, {b})")} و{m(f"\\text{{diag}}({c}, {x})")}.',
                    ans_tr_prod, f'Product is diag({a*c}, {b*x}), trace = {a*c} + {b*x} = {ans_tr_prod}.',
                    f'أثر حاصل الضرب = {ans_tr_prod}.', 'Easy')
    if k == 73:
        n_binom = a + 2; ans_sum_coef = 2**n_binom
        return item('binomial-sum-coefficients-eval', 'Binomial Theorem',
                    f'Find the sum of all coefficients in the expansion of {m(f"(1 + x)^{{{n_binom}}}")}.',
                    f'أوجد مجموع جميع المعاملات في مفكوك {m(f"(1 + x)^{{{n_binom}}}")}.',
                    ans_sum_coef, f'Set x = 1: (1 + 1)^{{{n_binom}}} = 2^{{{n_binom}}} = {ans_sum_coef}.',
                    f'بوضع x = 1 نحصل على {ans_sum_coef}.', 'Easy')
    if k == 74:
        ans_scaled_var = (a**2) * b
        return item('variance-scaled-variable-prop', 'Statistics',
                    f'A random variable X has variance {b}. What is the variance of {a}X?',
                    f'متغير عشوائي X تباينه {b}. ما تباين المتغير العشوائي {a}X؟',
                    ans_scaled_var, f'Var(aX) = a² Var(X) = {a}² × {b} = {ans_scaled_var}.',
                    f'التباين = {a}² × {b} = {ans_scaled_var}.')
    if k == 75:
        ans_sq_eval = a * a
        return item('integral-linear-slope', 'Integral Calculus',
                    f'Evaluate {m(f"\\int_0^{{{a}}} 2x\\,dx")}.',
                    f'احسب {m(f"\\int_0^{{{a}}} 2x\\,dx")}.',
                    ans_sq_eval, f'Antiderivative is x² from 0 to {a}: {a}² = {ans_sq_eval}.',
                    f'التكامل يعطي x² بالتعويض: {ans_sq_eval}.', 'Easy')
    if k == 76:
        ans_log_arg = a * b
        return item('log-product-property-eval', 'Algebra',
                    f'If log(x) = log({a}) + log({b}), find the positive value of x.',
                    f'إذا كان log(x) = log({a}) + log({b})، فما القيمة الموجبة لـ x؟',
                    ans_log_arg, f'log(a) + log(b) = log(ab) = log({ans_log_arg}), so x = {ans_log_arg}.',
                    f'log({a}) + log({b}) = log({ans_log_arg})، إذن x = {ans_log_arg}.', 'Easy')
    raise ValueError(k)

def proof(k, n):
    if k >= 20:
        return proof_families.proof_extra(k, n)
    r_local = random.Random(6092026 + k * 10007 + n * 997)
    old_R = R
    try:
        globals()["R"] = r_local
        return _orig_proof(k, n)
    finally:
        globals()["R"] = old_R

def _orig_proof(k, n):
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


def clean_opt_tuple(options):
    return tuple(sorted(re.sub(r"[\s\$\\{\}\(\)]+", "", str(o)).strip().lower() for o in options))

def render(spec, track, level, index, seen_opts=None):
    ans = spec["answer"]
    written = track == "olympiad"
    out = {
        "id": f"{track.upper()}-SM26-{index:04d}",
        "track": track,
        "level": level,
        "topic": spec["topic"],
        "type": "FRQ" if written else "MCQ",
        "difficulty": spec["difficulty"],
        "family_id": spec["family"],
        "variant": index,
        "source": "Original SuperMath parameterized practice",
        "review": {"structural": "passed", "mathematical": "construction_checked", "scope": "practice_not_official_paper"},
        "content": {}
    }
    opts = []
    key = None
    if not written:
        ans = F(ans)
        num_opts = 5 if track == "kangaroo" else 4
        attempts = 0
        while True:
            attempts += 1
            candidates = [ans]
            if spec["topic"] == "Probability":
                pool = [F(i, j) for j in range(2, 20) for i in range(j + 1) if F(i, j) != ans]
            elif ans.denominator != 1:
                den = ans.denominator
                base_offsets = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, -6, 7, 8, -7, 9]
                if attempts > 1:
                    R.shuffle(base_offsets)
                pool = [ans + F(d, den) for d in base_offsets] + [ans * 2, ans / 2, ans + 1, ans - 1, ans + F(attempts, den)]
            else:
                base_offsets = [-4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, -5, -6, 8, 9, 10, -7, 11, 12, 13]
                if attempts > 1:
                    R.shuffle(base_offsets)
                pool = [ans + d for d in base_offsets] + [ans * 2, ans * 3, ans // 2 if ans % 2 == 0 else ans + 5, ans + attempts + 2]
                
            if spec["topic"] == "Probability":
                pool = [v for v in pool if 0 <= v <= 1 and v != ans]
            else:
                pool = [v for v in pool if v != ans and (v >= 0 or ans < 0)]
                
            R.shuffle(pool)
            for v in pool:
                if v not in candidates:
                    candidates.append(v)
                if len(candidates) == num_opts:
                    break
            extra = 1
            while len(candidates) < num_opts:
                v = ans + extra + 7 + attempts
                if v not in candidates:
                    candidates.append(v)
                extra += 1
                
            canonical = clean_opt_tuple([m(val(v)) for v in candidates])
            if seen_opts is None or canonical not in seen_opts or attempts > 200:
                if seen_opts is not None:
                    seen_opts.add(canonical)
                break
                
        R.shuffle(candidates)
        key = candidates.index(ans)
        opts = [m(val(v)) for v in candidates]
        assert len(set(opts)) == len(opts) and candidates[key] == ans
        out["correct_index"] = key
        out["correct_answer"] = val(ans)
    else:
        out["assessment"] = "self_assessment"
        
    for lang in ["en", "ar"]:
        out["content"][lang] = {
            "question": spec[lang],
            "options": opts.copy(),
            "hint": ("Identify the conditions and work backwards from what is required. Explain why your method applies." if lang == "en" else "حدد المعطيات والمطلوب، ثم برر اختيار طريقة الحل."),
            "explanation": spec["solen" if lang == "en" else "solar"]
        }
    return out

TARGETS = {
    "kangaroo": {"Ecolier": 250, "Benjamin": 250, "Cadet": 250, "Junior": 250},
    "nafes": {"Grade 3": 250, "Grade 6": 250, "Grade 9": 250},
    "kaust": {"Track 1: Grades 6-7": 450, "Track 2: Grades 8-9": 450, "Track 3: Grades 10-11": 450},
    "nsmo": {"Phase 1: Junior Olympiad (Grade 7)": 250, "Phase 2: Intermediate Olympiad (Grades 8-9)": 250, "Phase 3: Senior National Olympiad (Grade 10)": 250},
    "jee": {"Grade 12": 500},
    "olympiad": {"High School": 500}
}

TOTAL_JUNIOR = 261
TOTAL_SENIOR = 457
TOTAL_PROOF = 290

SENIOR_NOCALC = [i for i in range(TOTAL_SENIOR) if i not in {9, 10, 11, 12, 29, 35, 41, 47, 54, 55, 57, 63, 69, 75, 77, 78}]

def make_banks():
    report = []
    global_seen_stems = set()
    global_seen_opts = set()
    legacy_banks = {}
    
    # 1. Preload legacy
    for track in TARGETS.keys():
        path = ROOT / "data" / f"{track}.json"
        bank = json.loads(path.read_text())
        bank = [q for q in bank if not q.get("family_id")]
        legacy_banks[track] = bank
        for q in bank:
            global_seen_stems.add(norm(q["content"]["en"]["question"]))
            if q.get("type") == "MCQ":
                o = q.get("content", {}).get("en", {}).get("options", [])
                if o:
                    global_seen_opts.add(clean_opt_tuple(o))
                    
    all_banks = {}
    for track, levels in TARGETS.items():
        path = ROOT / "data" / f"{track}.json"
        if track == "kaust":
            # KAUST is strictly built by scripts/build_kaust_kmc.py (official KMC Grades 6-11 scope)
            kmc_bank = json.loads(path.read_text())
            for level in levels:
                cnt = sum(q["level"] == level for q in kmc_bank)
                report.append({"track": track, "level": level, "retained": cnt, "added": 0, "total": cnt, "new_families": {}})
            continue
        bank = list(legacy_banks[track])
        idx = 1
        for level, target in levels.items():
            have = sum(q["level"] == level for q in bank)
            needed = target - have
            added = 0
            family_counts = collections.Counter()
            cap = 1 # STRICTLY 1 PER LESSON: EVERY QUESTION IN ANY LESSON IS A UNIQUE IDEA!
            
            # Select available family sequence for this track/level
            if track == "olympiad":
                available_families = list(range(TOTAL_PROOF))
            elif track == "jee":
                available_families = list(range(TOTAL_SENIOR))
            elif track == "kaust":
                available_families = list(range(TOTAL_SENIOR))
            elif track == "nsmo":
                if "Phase 1" in level:
                    available_families = [("j", i) for i in range(TOTAL_JUNIOR)]
                elif "Phase 2" in level:
                    available_families = []
                    for i in range(max(TOTAL_JUNIOR, len(SENIOR_NOCALC))):
                        if i < TOTAL_JUNIOR: available_families.append(("j", i))
                        if i < len(SENIOR_NOCALC): available_families.append(("s", SENIOR_NOCALC[i]))
                else:
                    available_families = list(range(TOTAL_SENIOR))
            elif track == "kangaroo":
                if level in ["Ecolier", "Benjamin"]:
                    available_families = [("j", i) for i in range(TOTAL_JUNIOR)]
                elif level == "Cadet":
                    available_families = []
                    for i in range(max(TOTAL_JUNIOR, len(SENIOR_NOCALC))):
                        if i < TOTAL_JUNIOR: available_families.append(("j", i))
                        if i < len(SENIOR_NOCALC): available_families.append(("s", SENIOR_NOCALC[i]))
                else: # Junior
                    available_families = [("s", i) for i in SENIOR_NOCALC]
            else: # nafes
                g = int(level.split()[-1])
                if g in [3, 6]:
                    available_families = [("j", i) for i in range(TOTAL_JUNIOR)]
                else:
                    available_families = [("s", i) for i in SENIOR_NOCALC]
                    
            fam_ptr = 0
            while added < needed and fam_ptr < len(available_families):
                fam_item = available_families[fam_ptr]
                fam_ptr += 1
                
                # Determine generator and grade parameter
                if track == "olympiad":
                    gen = lambda n: proof(fam_item, n)
                elif track == "jee":
                    gen = lambda n: senior(fam_item, n, 12)
                elif track == "kaust":
                    offset = 1 if "Phase 1" in level else (2 if "Phase 2" in level else 3)
                    gen = lambda n: senior(fam_item, n * 3 + offset, 11)
                elif track == "nsmo":
                    if "Phase 1" in level:
                        gen = lambda n: junior(fam_item[1], n + 2, 7)
                    elif "Phase 2" in level:
                        tag, fid = fam_item
                        if tag == "j": gen = lambda n: junior(fid, n + 3, 8)
                        else: gen = lambda n: senior(fid, n + 3, 8)
                    else:
                        gen = lambda n: senior(fam_item, n + 7, 10)
                elif track == "kangaroo":
                    g = {"Ecolier": 4, "Benjamin": 6, "Cadet": 8, "Junior": 10}[level]
                    if level in ["Ecolier", "Benjamin"]:
                        tag, fid = fam_item
                        offset = 1 if level == "Ecolier" else 4
                        gen = lambda n: junior(fid, n + offset, g)
                    elif level == "Cadet":
                        tag, fid = fam_item
                        if tag == "j": gen = lambda n: junior(fid, n + 5, g)
                        else: gen = lambda n: senior(fid, n + 1, g)
                    else:
                        tag, fid = fam_item
                        gen = lambda n: senior(fid, n + 2, g)
                else: # nafes
                    g = int(level.split()[-1])
                    if g in [3, 6]:
                        tag, fid = fam_item
                        offset = 6 if g == 3 else 8
                        gen = lambda n: junior(fid, n + offset, g)
                    else:
                        tag, fid = fam_item
                        gen = lambda n: senior(fid, n + 4, g)
                        
                # Try candidate n_variants until unique stem found
                chosen_spec = None
                for n_var in range(50):
                    spec = gen(n_var)
                    stem = norm(spec["en"])
                    if stem not in global_seen_stems and family_counts[spec["family"]] < cap:
                        chosen_spec = spec
                        break
                        
                if not chosen_spec:
                    continue
                    
                q = render(chosen_spec, track, level, idx, global_seen_opts)
                idx += 1
                global_seen_stems.add(norm(chosen_spec["en"]))
                bank.append(q)
                added += 1
                family_counts[chosen_spec["family"]] += 1
                
            report.append({"track": track, "level": level, "retained": have, "added": added, "total": have + added, "new_families": dict(family_counts)})
        path.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n")
        
    (ROOT / "review/expansion-summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps([{k: v for k, v in row.items() if k != "new_families"} for row in report], indent=2))

if __name__ == "__main__":
    make_banks()
