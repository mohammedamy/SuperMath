import math
from fractions import Fraction as F

def m(x): return "\\( " + str(x) + " \\)"
def val(x):
    if isinstance(x, F):
        return f"\\frac{{{x.numerator}}}{{{x.denominator}}}" if x.denominator != 1 else str(x.numerator)
    return str(x)

def item(family, topic, en, ar, answer, solen, solar, diff="Medium", distractors=None):
    return {
        "family": family, "topic": topic, "en": en, "ar": ar,
        "answer": answer, "solen": solen, "solar": solar,
        "difficulty": diff, "distractors": distractors or []
    }

def junior_extra(k, n, g):
    # Generates junior families from 61 to 260
    a = (n * 3 + 4) % 17 + 2
    b = (n * 5 + 7) % 19 + 3
    c = (n * 2 + 3) % 13 + 2
    d = (n * 7 + 1) % 11 + 2

    if k == 61:
        p1, p2 = [3, 5, 7, 11, 13][n % 5], [4, 8, 9, 16, 25][(n + 1) % 5]
        ans = p1 * p2
        return item('lcm-coprime-pair', 'Number Theory',
                    f'What is the least common multiple (LCM) of {p1} and {p2}?',
                    f'ما هو المضاعف المشترك الأصغر (م.م.أ) للعددين {p1} و{p2}؟',
                    ans, f'Since gcd({p1}, {p2}) = 1, LCM({p1}, {p2}) = {p1} × {p2} = {ans}.',
                    f'بما أن العددين أوليان فيما بينهما، فإن م.م.أ = {p1} × {p2} = {ans}.', 'Easy')

    if k == 62:
        g0 = c + 3
        ans = g0
        x1, x2 = g0 * a, g0 * (a + 1)
        return item('gcd-consecutive-multiples', 'Number Theory',
                    f'What is the greatest common divisor (GCD) of {x1} and {x2}?',
                    f'ما هو القاسم المشترك الأكبر (ق.م.أ) للعددين {x1} و{x2}؟',
                    ans, f'Consecutive multiples {x1} and {x2} have difference {x2 - x1} = {ans}. Since {ans} divides both, GCD = {ans}.',
                    f'الفرق بين المضاعفين المتتاليين هو {ans}، وهو يقسم كلاً منهما، إذن ق.م.أ = {ans}.', 'Easy')

    if k == 63:
        ang1 = 30 + (n * 5) % 40
        ang2 = 40 + (n * 7) % 50
        ans = ang1 + ang2
        return item('triangle-exterior-angle', 'Geometry',
                    f'In a triangle, two interior opposite angles measure {ang1}° and {ang2}°. What is the measure of their exterior angle in degrees?',
                    f'في مثلث، قياس زاويتين داخليتين غير متجاورتين هما {ang1}° و{ang2}°. ما قياس الزاوية الخارجية المقابلة لهما بالدرجات؟',
                    ans, f'An exterior angle equals the sum of the two opposite interior angles: {ang1}° + {ang2}° = {ans}°.',
                    f'الزاوية الخارجية للمثلث تساوي مجموع الزاويتين الداخليتين المقابلتين: {ang1}° + {ang2}° = {ans}°.', 'Easy')

    if k == 64:
        d1 = 2 * (a + 3)
        d2 = 2 * (b + 2)
        ans = (d1 * d2) // 2
        return item('rhombus-area-diagonals', 'Geometry',
                    f'A rhombus has diagonals of lengths {d1} cm and {d2} cm. What is its area in cm²?',
                    f'معين طولا قطريه {d1} سم و{d2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans, f'Area of a rhombus = (d1 × d2) / 2 = ({d1} × {d2}) / 2 = {ans} cm².',
                    f'مساحة المعين = (القطر الأول × القطر الثاني) ÷ 2 = {ans} سم².', 'Easy')

    if k == 65:
        mins = ((n * 5) % 55) + 5
        ans = mins * 6
        return item('clock-minute-hand-degrees', 'Measurement',
                    f'How many degrees does the minute hand of a clock rotate in {mins} minutes?',
                    f'كم درجة يدور عقرب الدقائق في الساعة خلال {mins} دقيقة؟',
                    ans, f'The minute hand rotates 360° in 60 minutes, which is 6° per minute. In {mins} minutes: {mins} × 6° = {ans}°.',
                    f'يدور عقرب الدقائق 6 درجات في الدقيقة الواحدة: {mins} × 6° = {ans}°.', 'Easy')

    if k == 66:
        w = a + 2
        l = 2 * w
        ans = 2 * (l + w)
        return item('rectangle-perimeter-ratio-ratio', 'Geometry',
                    f'A rectangle has width {w} cm, and its length is twice its width. What is its perimeter in cm?',
                    f'مستطيل عرضه {w} سم، وطوله ضعف عرضه. ما محيطه بالسنتيمتر؟',
                    ans, f'Length is 2 × {w} = {l} cm. Perimeter = 2 × ({l} + {w}) = 2 × {l + w} = {ans} cm.',
                    f'الطول = {l} سم. المحيط = 2 × ({l} + {w}) = {ans} سم.', 'Easy')

    if k == 67:
        val1 = (n * 7 + 206) % 29 + 3
        val2 = (n * 5 + 471) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 67) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-67', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 68:
        val1 = (n * 7 + 209) % 29 + 3
        val2 = (n * 5 + 478) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 68) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-68', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 69:
        val1 = (n * 7 + 212) % 29 + 3
        val2 = (n * 5 + 485) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 69) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-69', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 70:
        val1 = (n * 7 + 215) % 29 + 3
        val2 = (n * 5 + 492) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 70) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-70', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 71:
        val1 = (n * 7 + 218) % 29 + 3
        val2 = (n * 5 + 499) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 71) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-71', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 72:
        val1 = (n * 7 + 221) % 29 + 3
        val2 = (n * 5 + 506) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 72) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-72', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 73:
        val1 = (n * 7 + 224) % 29 + 3
        val2 = (n * 5 + 513) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 73) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-73', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 74:
        val1 = (n * 7 + 227) % 29 + 3
        val2 = (n * 5 + 520) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 74) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-74', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 75:
        val1 = (n * 7 + 230) % 29 + 3
        val2 = (n * 5 + 527) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 75) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-75', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 76:
        val1 = (n * 7 + 233) % 29 + 3
        val2 = (n * 5 + 534) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 76) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-76', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 77:
        val1 = (n * 7 + 236) % 29 + 3
        val2 = (n * 5 + 541) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 77) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-77', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 78:
        val1 = (n * 7 + 239) % 29 + 3
        val2 = (n * 5 + 548) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 78) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-78', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 79:
        val1 = (n * 7 + 242) % 29 + 3
        val2 = (n * 5 + 555) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 79) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-79', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 80:
        val1 = (n * 7 + 245) % 29 + 3
        val2 = (n * 5 + 562) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 80) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-80', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 81:
        val1 = (n * 7 + 248) % 29 + 3
        val2 = (n * 5 + 569) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 81) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-81', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 82:
        val1 = (n * 7 + 251) % 29 + 3
        val2 = (n * 5 + 576) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 82) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-82', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 83:
        val1 = (n * 7 + 254) % 29 + 3
        val2 = (n * 5 + 583) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 83) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-83', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 84:
        val1 = (n * 7 + 257) % 29 + 3
        val2 = (n * 5 + 590) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 84) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-84', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 85:
        val1 = (n * 7 + 260) % 29 + 3
        val2 = (n * 5 + 597) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 85) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-85', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 86:
        val1 = (n * 7 + 263) % 29 + 3
        val2 = (n * 5 + 604) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 86) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-86', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 87:
        val1 = (n * 7 + 266) % 29 + 3
        val2 = (n * 5 + 611) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 87) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-87', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 88:
        val1 = (n * 7 + 269) % 29 + 3
        val2 = (n * 5 + 618) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 88) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-88', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 89:
        val1 = (n * 7 + 272) % 29 + 3
        val2 = (n * 5 + 625) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 89) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-89', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 90:
        val1 = (n * 7 + 275) % 29 + 3
        val2 = (n * 5 + 632) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 90) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-90', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 91:
        val1 = (n * 7 + 278) % 29 + 3
        val2 = (n * 5 + 639) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 91) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-91', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 92:
        val1 = (n * 7 + 281) % 29 + 3
        val2 = (n * 5 + 646) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 92) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-92', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 93:
        val1 = (n * 7 + 284) % 29 + 3
        val2 = (n * 5 + 653) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 93) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-93', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 94:
        val1 = (n * 7 + 287) % 29 + 3
        val2 = (n * 5 + 660) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 94) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-94', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 95:
        val1 = (n * 7 + 290) % 29 + 3
        val2 = (n * 5 + 667) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 95) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-95', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 96:
        val1 = (n * 7 + 293) % 29 + 3
        val2 = (n * 5 + 674) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 96) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-96', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 97:
        val1 = (n * 7 + 296) % 29 + 3
        val2 = (n * 5 + 681) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 97) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-97', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 98:
        val1 = (n * 7 + 299) % 29 + 3
        val2 = (n * 5 + 688) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 98) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-98', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 99:
        val1 = (n * 7 + 302) % 29 + 3
        val2 = (n * 5 + 695) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 99) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-99', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 100:
        val1 = (n * 7 + 305) % 29 + 3
        val2 = (n * 5 + 702) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 100) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-100', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 101:
        val1 = (n * 7 + 308) % 29 + 3
        val2 = (n * 5 + 709) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 101) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-101', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 102:
        val1 = (n * 7 + 311) % 29 + 3
        val2 = (n * 5 + 716) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 102) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-102', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 103:
        val1 = (n * 7 + 314) % 29 + 3
        val2 = (n * 5 + 723) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 103) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-103', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 104:
        val1 = (n * 7 + 317) % 29 + 3
        val2 = (n * 5 + 730) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 104) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-104', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 105:
        val1 = (n * 7 + 320) % 29 + 3
        val2 = (n * 5 + 737) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 105) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-105', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 106:
        val1 = (n * 7 + 323) % 29 + 3
        val2 = (n * 5 + 744) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 106) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-106', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 107:
        val1 = (n * 7 + 326) % 29 + 3
        val2 = (n * 5 + 751) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 107) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-107', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 108:
        val1 = (n * 7 + 329) % 29 + 3
        val2 = (n * 5 + 758) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 108) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-108', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 109:
        val1 = (n * 7 + 332) % 29 + 3
        val2 = (n * 5 + 765) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 109) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-109', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 110:
        val1 = (n * 7 + 335) % 29 + 3
        val2 = (n * 5 + 772) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 110) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-110', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 111:
        val1 = (n * 7 + 338) % 29 + 3
        val2 = (n * 5 + 779) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 111) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-111', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 112:
        val1 = (n * 7 + 341) % 29 + 3
        val2 = (n * 5 + 786) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 112) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-112', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 113:
        val1 = (n * 7 + 344) % 29 + 3
        val2 = (n * 5 + 793) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 113) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-113', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 114:
        val1 = (n * 7 + 347) % 29 + 3
        val2 = (n * 5 + 800) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 114) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-114', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 115:
        val1 = (n * 7 + 350) % 29 + 3
        val2 = (n * 5 + 807) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 115) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-115', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 116:
        val1 = (n * 7 + 353) % 29 + 3
        val2 = (n * 5 + 814) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 116) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-116', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 117:
        val1 = (n * 7 + 356) % 29 + 3
        val2 = (n * 5 + 821) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 117) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-117', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 118:
        val1 = (n * 7 + 359) % 29 + 3
        val2 = (n * 5 + 828) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 118) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-118', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 119:
        val1 = (n * 7 + 362) % 29 + 3
        val2 = (n * 5 + 835) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 119) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-119', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 120:
        val1 = (n * 7 + 365) % 29 + 3
        val2 = (n * 5 + 842) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 120) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-120', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 121:
        val1 = (n * 7 + 368) % 29 + 3
        val2 = (n * 5 + 849) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 121) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-121', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 122:
        val1 = (n * 7 + 371) % 29 + 3
        val2 = (n * 5 + 856) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 122) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-122', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 123:
        val1 = (n * 7 + 374) % 29 + 3
        val2 = (n * 5 + 863) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 123) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-123', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 124:
        val1 = (n * 7 + 377) % 29 + 3
        val2 = (n * 5 + 870) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 124) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-124', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 125:
        val1 = (n * 7 + 380) % 29 + 3
        val2 = (n * 5 + 877) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 125) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-125', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 126:
        val1 = (n * 7 + 383) % 29 + 3
        val2 = (n * 5 + 884) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 126) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-126', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 127:
        val1 = (n * 7 + 386) % 29 + 3
        val2 = (n * 5 + 891) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 127) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-127', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 128:
        val1 = (n * 7 + 389) % 29 + 3
        val2 = (n * 5 + 898) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 128) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-128', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 129:
        val1 = (n * 7 + 392) % 29 + 3
        val2 = (n * 5 + 905) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 129) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-129', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 130:
        val1 = (n * 7 + 395) % 29 + 3
        val2 = (n * 5 + 912) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 130) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-130', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 131:
        val1 = (n * 7 + 398) % 29 + 3
        val2 = (n * 5 + 919) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 131) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-131', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 132:
        val1 = (n * 7 + 401) % 29 + 3
        val2 = (n * 5 + 926) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 132) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-132', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 133:
        val1 = (n * 7 + 404) % 29 + 3
        val2 = (n * 5 + 933) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 133) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-133', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 134:
        val1 = (n * 7 + 407) % 29 + 3
        val2 = (n * 5 + 940) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 134) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-134', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 135:
        val1 = (n * 7 + 410) % 29 + 3
        val2 = (n * 5 + 947) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 135) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-135', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 136:
        val1 = (n * 7 + 413) % 29 + 3
        val2 = (n * 5 + 954) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 136) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-136', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 137:
        val1 = (n * 7 + 416) % 29 + 3
        val2 = (n * 5 + 961) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 137) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-137', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 138:
        val1 = (n * 7 + 419) % 29 + 3
        val2 = (n * 5 + 968) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 138) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-138', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 139:
        val1 = (n * 7 + 422) % 29 + 3
        val2 = (n * 5 + 975) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 139) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-139', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 140:
        val1 = (n * 7 + 425) % 29 + 3
        val2 = (n * 5 + 982) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 140) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-140', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 141:
        val1 = (n * 7 + 428) % 29 + 3
        val2 = (n * 5 + 989) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 141) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-141', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 142:
        val1 = (n * 7 + 431) % 29 + 3
        val2 = (n * 5 + 996) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 142) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-142', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 143:
        val1 = (n * 7 + 434) % 29 + 3
        val2 = (n * 5 + 1003) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 143) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-143', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 144:
        val1 = (n * 7 + 437) % 29 + 3
        val2 = (n * 5 + 1010) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 144) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-144', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 145:
        val1 = (n * 7 + 440) % 29 + 3
        val2 = (n * 5 + 1017) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 145) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-145', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 146:
        val1 = (n * 7 + 443) % 29 + 3
        val2 = (n * 5 + 1024) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 146) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-146', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 147:
        val1 = (n * 7 + 446) % 29 + 3
        val2 = (n * 5 + 1031) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 147) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-147', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 148:
        val1 = (n * 7 + 449) % 29 + 3
        val2 = (n * 5 + 1038) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 148) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-148', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 149:
        val1 = (n * 7 + 452) % 29 + 3
        val2 = (n * 5 + 1045) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 149) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-149', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 150:
        val1 = (n * 7 + 455) % 29 + 3
        val2 = (n * 5 + 1052) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 150) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-150', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 151:
        val1 = (n * 7 + 458) % 29 + 3
        val2 = (n * 5 + 1059) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 151) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-151', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 152:
        val1 = (n * 7 + 461) % 29 + 3
        val2 = (n * 5 + 1066) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 152) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-152', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 153:
        val1 = (n * 7 + 464) % 29 + 3
        val2 = (n * 5 + 1073) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 153) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-153', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 154:
        val1 = (n * 7 + 467) % 29 + 3
        val2 = (n * 5 + 1080) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 154) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-154', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 155:
        val1 = (n * 7 + 470) % 29 + 3
        val2 = (n * 5 + 1087) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 155) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-155', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 156:
        val1 = (n * 7 + 473) % 29 + 3
        val2 = (n * 5 + 1094) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 156) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-156', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 157:
        val1 = (n * 7 + 476) % 29 + 3
        val2 = (n * 5 + 1101) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 157) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-157', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 158:
        val1 = (n * 7 + 479) % 29 + 3
        val2 = (n * 5 + 1108) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 158) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-158', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 159:
        val1 = (n * 7 + 482) % 29 + 3
        val2 = (n * 5 + 1115) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 159) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-159', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 160:
        val1 = (n * 7 + 485) % 29 + 3
        val2 = (n * 5 + 1122) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 160) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-160', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 161:
        val1 = (n * 7 + 488) % 29 + 3
        val2 = (n * 5 + 1129) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 161) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-161', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 162:
        val1 = (n * 7 + 491) % 29 + 3
        val2 = (n * 5 + 1136) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 162) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-162', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 163:
        val1 = (n * 7 + 494) % 29 + 3
        val2 = (n * 5 + 1143) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 163) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-163', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 164:
        val1 = (n * 7 + 497) % 29 + 3
        val2 = (n * 5 + 1150) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 164) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-164', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 165:
        val1 = (n * 7 + 500) % 29 + 3
        val2 = (n * 5 + 1157) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 165) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-165', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 166:
        val1 = (n * 7 + 503) % 29 + 3
        val2 = (n * 5 + 1164) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 166) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-166', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 167:
        val1 = (n * 7 + 506) % 29 + 3
        val2 = (n * 5 + 1171) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 167) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-167', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 168:
        val1 = (n * 7 + 509) % 29 + 3
        val2 = (n * 5 + 1178) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 168) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-168', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 169:
        val1 = (n * 7 + 512) % 29 + 3
        val2 = (n * 5 + 1185) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 169) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-169', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 170:
        val1 = (n * 7 + 515) % 29 + 3
        val2 = (n * 5 + 1192) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 170) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-170', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 171:
        val1 = (n * 7 + 518) % 29 + 3
        val2 = (n * 5 + 1199) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 171) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-171', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 172:
        val1 = (n * 7 + 521) % 29 + 3
        val2 = (n * 5 + 1206) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 172) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-172', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 173:
        val1 = (n * 7 + 524) % 29 + 3
        val2 = (n * 5 + 1213) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 173) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-173', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 174:
        val1 = (n * 7 + 527) % 29 + 3
        val2 = (n * 5 + 1220) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 174) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-174', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 175:
        val1 = (n * 7 + 530) % 29 + 3
        val2 = (n * 5 + 1227) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 175) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-175', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 176:
        val1 = (n * 7 + 533) % 29 + 3
        val2 = (n * 5 + 1234) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 176) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-176', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 177:
        val1 = (n * 7 + 536) % 29 + 3
        val2 = (n * 5 + 1241) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 177) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-177', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 178:
        val1 = (n * 7 + 539) % 29 + 3
        val2 = (n * 5 + 1248) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 178) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-178', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 179:
        val1 = (n * 7 + 542) % 29 + 3
        val2 = (n * 5 + 1255) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 179) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-179', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 180:
        val1 = (n * 7 + 545) % 29 + 3
        val2 = (n * 5 + 1262) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 180) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-180', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 181:
        val1 = (n * 7 + 548) % 29 + 3
        val2 = (n * 5 + 1269) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 181) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-181', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 182:
        val1 = (n * 7 + 551) % 29 + 3
        val2 = (n * 5 + 1276) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 182) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-182', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 183:
        val1 = (n * 7 + 554) % 29 + 3
        val2 = (n * 5 + 1283) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 183) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-183', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 184:
        val1 = (n * 7 + 557) % 29 + 3
        val2 = (n * 5 + 1290) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 184) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-184', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 185:
        val1 = (n * 7 + 560) % 29 + 3
        val2 = (n * 5 + 1297) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 185) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-185', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 186:
        val1 = (n * 7 + 563) % 29 + 3
        val2 = (n * 5 + 1304) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 186) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-186', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 187:
        val1 = (n * 7 + 566) % 29 + 3
        val2 = (n * 5 + 1311) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 187) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-187', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 188:
        val1 = (n * 7 + 569) % 29 + 3
        val2 = (n * 5 + 1318) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 188) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-188', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 189:
        val1 = (n * 7 + 572) % 29 + 3
        val2 = (n * 5 + 1325) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 189) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-189', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 190:
        val1 = (n * 7 + 575) % 29 + 3
        val2 = (n * 5 + 1332) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 190) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-190', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 191:
        val1 = (n * 7 + 578) % 29 + 3
        val2 = (n * 5 + 1339) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 191) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-191', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 192:
        val1 = (n * 7 + 581) % 29 + 3
        val2 = (n * 5 + 1346) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 192) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-192', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 193:
        val1 = (n * 7 + 584) % 29 + 3
        val2 = (n * 5 + 1353) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 193) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-193', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 194:
        val1 = (n * 7 + 587) % 29 + 3
        val2 = (n * 5 + 1360) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 194) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-194', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 195:
        val1 = (n * 7 + 590) % 29 + 3
        val2 = (n * 5 + 1367) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 195) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-195', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 196:
        val1 = (n * 7 + 593) % 29 + 3
        val2 = (n * 5 + 1374) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 196) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-196', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 197:
        val1 = (n * 7 + 596) % 29 + 3
        val2 = (n * 5 + 1381) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 197) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-197', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 198:
        val1 = (n * 7 + 599) % 29 + 3
        val2 = (n * 5 + 1388) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 198) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-198', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 199:
        val1 = (n * 7 + 602) % 29 + 3
        val2 = (n * 5 + 1395) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 199) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-199', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 200:
        val1 = (n * 7 + 605) % 29 + 3
        val2 = (n * 5 + 1402) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 200) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-200', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 201:
        val1 = (n * 7 + 608) % 29 + 3
        val2 = (n * 5 + 1409) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 201) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-201', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 202:
        val1 = (n * 7 + 611) % 29 + 3
        val2 = (n * 5 + 1416) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 202) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-202', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 203:
        val1 = (n * 7 + 614) % 29 + 3
        val2 = (n * 5 + 1423) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 203) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-203', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 204:
        val1 = (n * 7 + 617) % 29 + 3
        val2 = (n * 5 + 1430) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 204) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-204', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 205:
        val1 = (n * 7 + 620) % 29 + 3
        val2 = (n * 5 + 1437) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 205) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-205', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 206:
        val1 = (n * 7 + 623) % 29 + 3
        val2 = (n * 5 + 1444) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 206) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-206', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 207:
        val1 = (n * 7 + 626) % 29 + 3
        val2 = (n * 5 + 1451) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 207) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-207', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 208:
        val1 = (n * 7 + 629) % 29 + 3
        val2 = (n * 5 + 1458) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 208) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-208', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 209:
        val1 = (n * 7 + 632) % 29 + 3
        val2 = (n * 5 + 1465) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 209) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-209', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 210:
        val1 = (n * 7 + 635) % 29 + 3
        val2 = (n * 5 + 1472) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 210) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-210', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 211:
        val1 = (n * 7 + 638) % 29 + 3
        val2 = (n * 5 + 1479) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 211) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-211', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 212:
        val1 = (n * 7 + 641) % 29 + 3
        val2 = (n * 5 + 1486) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 212) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-212', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 213:
        val1 = (n * 7 + 644) % 29 + 3
        val2 = (n * 5 + 1493) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 213) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-213', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 214:
        val1 = (n * 7 + 647) % 29 + 3
        val2 = (n * 5 + 1500) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 214) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-214', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 215:
        val1 = (n * 7 + 650) % 29 + 3
        val2 = (n * 5 + 1507) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 215) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-215', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 216:
        val1 = (n * 7 + 653) % 29 + 3
        val2 = (n * 5 + 1514) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 216) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-216', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 217:
        val1 = (n * 7 + 656) % 29 + 3
        val2 = (n * 5 + 1521) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 217) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-217', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 218:
        val1 = (n * 7 + 659) % 29 + 3
        val2 = (n * 5 + 1528) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 218) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-218', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 219:
        val1 = (n * 7 + 662) % 29 + 3
        val2 = (n * 5 + 1535) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 219) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-219', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 220:
        val1 = (n * 7 + 665) % 29 + 3
        val2 = (n * 5 + 1542) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 220) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-220', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 221:
        val1 = (n * 7 + 668) % 29 + 3
        val2 = (n * 5 + 1549) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 221) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-221', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 222:
        val1 = (n * 7 + 671) % 29 + 3
        val2 = (n * 5 + 1556) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 222) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-222', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 223:
        val1 = (n * 7 + 674) % 29 + 3
        val2 = (n * 5 + 1563) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 223) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-223', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 224:
        val1 = (n * 7 + 677) % 29 + 3
        val2 = (n * 5 + 1570) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 224) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-224', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 225:
        val1 = (n * 7 + 680) % 29 + 3
        val2 = (n * 5 + 1577) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 225) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-225', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 226:
        val1 = (n * 7 + 683) % 29 + 3
        val2 = (n * 5 + 1584) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 226) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-226', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 227:
        val1 = (n * 7 + 686) % 29 + 3
        val2 = (n * 5 + 1591) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 227) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-227', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 228:
        val1 = (n * 7 + 689) % 29 + 3
        val2 = (n * 5 + 1598) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 228) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-228', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 229:
        val1 = (n * 7 + 692) % 29 + 3
        val2 = (n * 5 + 1605) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 229) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-229', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 230:
        val1 = (n * 7 + 695) % 29 + 3
        val2 = (n * 5 + 1612) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 230) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-230', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 231:
        val1 = (n * 7 + 698) % 29 + 3
        val2 = (n * 5 + 1619) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 231) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-231', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 232:
        val1 = (n * 7 + 701) % 29 + 3
        val2 = (n * 5 + 1626) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 232) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-232', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 233:
        val1 = (n * 7 + 704) % 29 + 3
        val2 = (n * 5 + 1633) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 233) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-233', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 234:
        val1 = (n * 7 + 707) % 29 + 3
        val2 = (n * 5 + 1640) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 234) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-234', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 235:
        val1 = (n * 7 + 710) % 29 + 3
        val2 = (n * 5 + 1647) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 235) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-235', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 236:
        val1 = (n * 7 + 713) % 29 + 3
        val2 = (n * 5 + 1654) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 236) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-236', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 237:
        val1 = (n * 7 + 716) % 29 + 3
        val2 = (n * 5 + 1661) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 237) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-237', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 238:
        val1 = (n * 7 + 719) % 29 + 3
        val2 = (n * 5 + 1668) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 238) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-238', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 239:
        val1 = (n * 7 + 722) % 29 + 3
        val2 = (n * 5 + 1675) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 239) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-239', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 240:
        val1 = (n * 7 + 725) % 29 + 3
        val2 = (n * 5 + 1682) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 240) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-240', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 241:
        val1 = (n * 7 + 728) % 29 + 3
        val2 = (n * 5 + 1689) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 241) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-241', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 242:
        val1 = (n * 7 + 731) % 29 + 3
        val2 = (n * 5 + 1696) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 242) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-242', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 243:
        val1 = (n * 7 + 734) % 29 + 3
        val2 = (n * 5 + 1703) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 243) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-243', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 244:
        val1 = (n * 7 + 737) % 29 + 3
        val2 = (n * 5 + 1710) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 244) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-244', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 245:
        val1 = (n * 7 + 740) % 29 + 3
        val2 = (n * 5 + 1717) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 245) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-245', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 246:
        val1 = (n * 7 + 743) % 29 + 3
        val2 = (n * 5 + 1724) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 246) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-246', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 247:
        val1 = (n * 7 + 746) % 29 + 3
        val2 = (n * 5 + 1731) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 247) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-247', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 248:
        val1 = (n * 7 + 749) % 29 + 3
        val2 = (n * 5 + 1738) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 248) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-248', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 249:
        val1 = (n * 7 + 752) % 29 + 3
        val2 = (n * 5 + 1745) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 249) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-249', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 250:
        val1 = (n * 7 + 755) % 29 + 3
        val2 = (n * 5 + 1752) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 250) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-250', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    if k == 251:
        val1 = (n * 7 + 758) % 29 + 3
        val2 = (n * 5 + 1759) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 251) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 4 * diff
        return item('arithmetic-sequence-missing-step-251', 'Patterns',
                    f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?',
                    f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟',
                    ans,
                    f'5th term = {val1} + 4 × {diff} = {ans}.',
                    f'الحد الخامس = {ans}.',
                    'Easy')

    if k == 252:
        val1 = (n * 7 + 761) % 29 + 3
        val2 = (n * 5 + 1766) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 252) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val2 * 5
        return item('balanced-scale-puzzle-252', 'Logic',
                    f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?',
                    f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟',
                    ans,
                    f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.',
                    f'وزن التفاحة = {ans} جرام.',
                    'Easy')

    if k == 253:
        val1 = (n * 7 + 764) % 29 + 3
        val2 = (n * 5 + 1773) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 253) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = (val_k * (val_k - 1)) // 2
        return item('counting-handshakes-group-253', 'Combinatorics',
                    f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?',
                    f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟',
                    ans,
                    f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.',
                    f'عدد المباريات = {ans}.',
                    'Easy')

    if k == 254:
        val1 = (n * 7 + 767) % 29 + 3
        val2 = (n * 5 + 1780) % 23 + 2
        diff = (n * 3 + 2) % 11 + 1
        val_k = (n * 2 + 254) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 + 3
        return item('mean-of-set-of-numbers-254', 'Statistics',
                    f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?',
                    f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟',
                    ans,
                    f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.',
                    f'المتوسط الحسابي = {ans}.',
                    'Easy')

    if k == 255:
        val1 = (n * 7 + 770) % 29 + 3
        val2 = (n * 5 + 1787) % 23 + 2
        diff = (n * 3 + 3) % 11 + 1
        val_k = (n * 2 + 255) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = 3 * val1
        return item('equilateral-triangle-perimeter-255', 'Geometry',
                    f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?',
                    f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟',
                    ans,
                    f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.',
                    f'المحيط = 3 × {val1} = {ans} سم.',
                    'Easy')

    if k == 256:
        val1 = (n * 7 + 773) % 29 + 3
        val2 = (n * 5 + 1794) % 23 + 2
        diff = (n * 3 + 4) % 11 + 1
        val_k = (n * 2 + 256) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = diff
        return item('integer-division-remainder-256', 'Numbers and Operations',
                    f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?',
                    f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟',
                    ans,
                    f'\\( {val1 * val2 + diff} = {val1} \\times {val2} + {diff} \\), so remainder is {ans}.',
                    f'باقي القسمة = {ans}.',
                    'Easy')

    if k == 257:
        val1 = (n * 7 + 776) % 29 + 3
        val2 = (n * 5 + 1801) % 23 + 2
        diff = (n * 3 + 5) % 11 + 1
        val_k = (n * 2 + 257) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2 - diff
        return item('two-step-word-problem-257', 'Numbers and Operations',
                    f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?',
                    f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟',
                    ans,
                    f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.',
                    f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.',
                    'Easy')

    if k == 258:
        val1 = (n * 7 + 779) % 29 + 3
        val2 = (n * 5 + 1808) % 23 + 2
        diff = (n * 3 + 6) % 11 + 1
        val_k = (n * 2 + 258) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('parallelogram-area-base-height-258', 'Geometry',
                    f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?',
                    f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟',
                    ans,
                    f'Area = base × height = {val1} × {val2} = {ans} cm².',
                    f'المساحة = القاعدة × الارتفاع = {ans} سم².',
                    'Easy')

    if k == 259:
        val1 = (n * 7 + 782) % 29 + 3
        val2 = (n * 5 + 1815) % 23 + 2
        diff = (n * 3 + 0) % 11 + 1
        val_k = (n * 2 + 259) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1 * val2
        return item('speed-distance-time-hours-259', 'Measurement',
                    f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?',
                    f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟',
                    ans,
                    f'Distance = speed × time = {val1} × {val2} = {ans} km.',
                    f'المسافة = السرعة × الزمن = {ans} كم.',
                    'Easy')

    if k == 260:
        val1 = (n * 7 + 785) % 29 + 3
        val2 = (n * 5 + 1822) % 23 + 2
        diff = (n * 3 + 1) % 11 + 1
        val_k = (n * 2 + 260) % 17 + 5
        if val2 <= diff: val2 = diff + 1
        ans = val1
        return item('fraction-of-a-whole-number-260', 'Fractions and Decimals',
                    f'What is \\( \\frac{{1}}{{{val2}}} \\) of {val1 * val2}?',
                    f'ما قيمة \\( \\frac{{1}}{{{val2}}} \\) من العدد {val1 * val2}؟',
                    ans,
                    f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.',
                    'Easy')

    raise ValueError(f"Unknown junior family k={k}")
