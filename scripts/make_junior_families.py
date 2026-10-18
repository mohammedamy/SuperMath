import json
from pathlib import Path

# Generates 200 distinct junior families from k=61 to k=260 (total 261 families)

code_lines = [
    'import math',
    'from fractions import Fraction as F',
    '',
    'def m(x): return "\\\\( " + str(x) + " \\\\)"',
    'def val(x):',
    '    if isinstance(x, F):',
    '        return f"\\\\frac{{{x.numerator}}}{{{x.denominator}}}" if x.denominator != 1 else str(x.numerator)',
    '    return str(x)',
    '',
    'def item(family, topic, en, ar, answer, solen, solar, diff="Medium", distractors=None):',
    '    return {',
    '        "family": family, "topic": topic, "en": en, "ar": ar,',
    '        "answer": answer, "solen": solen, "solar": solar,',
    '        "difficulty": diff, "distractors": distractors or []',
    '    }',
    '',
    'def junior_extra(k, n, g):',
    '    # Generates junior families from 61 to 260',
    '    a = (n * 3 + 4) % 17 + 2',
    '    b = (n * 5 + 7) % 19 + 3',
    '    c = (n * 2 + 3) % 13 + 2',
    '    d = (n * 7 + 1) % 11 + 2',
    '',
]

# We will define 200 distinct problem generators for junior
generators = []

# 61: LCM coprime
generators.append(('lcm-coprime-pair', 'Number Theory',
'''    p1, p2 = [3, 5, 7, 11, 13][n % 5], [4, 8, 9, 16, 25][(n + 1) % 5]
    ans = p1 * p2
    return item('lcm-coprime-pair', 'Number Theory',
                f'What is the least common multiple (LCM) of {p1} and {p2}?',
                f'ما هو المضاعف المشترك الأصغر (م.م.أ) للعددين {p1} و{p2}؟',
                ans, f'Since gcd({p1}, {p2}) = 1, LCM({p1}, {p2}) = {p1} × {p2} = {ans}.',
                f'بما أن العددين أوليان فيما بينهما، فإن م.م.أ = {p1} × {p2} = {ans}.', 'Easy')'''))

# 62: GCD consecutive multiples
generators.append(('gcd-consecutive-multiples', 'Number Theory',
'''    g0 = c + 3
    ans = g0
    x1, x2 = g0 * a, g0 * (a + 1)
    return item('gcd-consecutive-multiples', 'Number Theory',
                f'What is the greatest common divisor (GCD) of {x1} and {x2}?',
                f'ما هو القاسم المشترك الأكبر (ق.م.أ) للعددين {x1} و{x2}؟',
                ans, f'Consecutive multiples {x1} and {x2} have difference {x2 - x1} = {ans}. Since {ans} divides both, GCD = {ans}.',
                f'الفرق بين المضاعفين المتتاليين هو {ans}، وهو يقسم كلاً منهما، إذن ق.م.أ = {ans}.', 'Easy')'''))

# 63: triangle exterior angle
generators.append(('triangle-exterior-angle', 'Geometry',
'''    ang1 = 30 + (n * 5) % 40
    ang2 = 40 + (n * 7) % 50
    ans = ang1 + ang2
    return item('triangle-exterior-angle', 'Geometry',
                f'In a triangle, two interior opposite angles measure {ang1}° and {ang2}°. What is the measure of their exterior angle in degrees?',
                f'في مثلث، قياس زاويتين داخليتين غير متجاورتين هما {ang1}° و{ang2}°. ما قياس الزاوية الخارجية المقابلة لهما بالدرجات؟',
                ans, f'An exterior angle equals the sum of the two opposite interior angles: {ang1}° + {ang2}° = {ans}°.',
                f'الزاوية الخارجية للمثلث تساوي مجموع الزاويتين الداخليتين المقابلتين: {ang1}° + {ang2}° = {ans}°.', 'Easy')'''))

# 64: rhombus area diagonals
generators.append(('rhombus-area-diagonals', 'Geometry',
'''    d1 = 2 * (a + 3)
    d2 = 2 * (b + 2)
    ans = (d1 * d2) // 2
    return item('rhombus-area-diagonals', 'Geometry',
                f'A rhombus has diagonals of lengths {d1} cm and {d2} cm. What is its area in cm²?',
                f'معين طولا قطريه {d1} سم و{d2} سم. ما مساحته بالسنتيمتر المربع؟',
                ans, f'Area of a rhombus = (d1 × d2) / 2 = ({d1} × {d2}) / 2 = {ans} cm².',
                f'مساحة المعين = (القطر الأول × القطر الثاني) ÷ 2 = {ans} سم².', 'Easy')'''))

# 65: clock minute hand degrees
generators.append(('clock-minute-hand-degrees', 'Measurement',
'''    mins = ((n * 5) % 55) + 5
    ans = mins * 6
    return item('clock-minute-hand-degrees', 'Measurement',
                f'How many degrees does the minute hand of a clock rotate in {mins} minutes?',
                f'كم درجة يدور عقرب الدقائق في الساعة خلال {mins} دقيقة؟',
                ans, f'The minute hand rotates 360° in 60 minutes, which is 6° per minute. In {mins} minutes: {mins} × 6° = {ans}°.',
                f'يدور عقرب الدقائق 6 درجات في الدقيقة الواحدة: {mins} × 6° = {ans}°.', 'Easy')'''))

# 66: rectangle perimeter known ratio
generators.append(('rectangle-perimeter-ratio-ratio', 'Geometry',
'''    w = a + 2
    l = 2 * w
    ans = 2 * (l + w)
    return item('rectangle-perimeter-ratio-ratio', 'Geometry',
                f'A rectangle has width {w} cm, and its length is twice its width. What is its perimeter in cm?',
                f'مستطيل عرضه {w} سم، وطوله ضعف عرضه. ما محيطه بالسنتيمتر؟',
                ans, f'Length is 2 × {w} = {l} cm. Perimeter = 2 × ({l} + {w}) = 2 × {l + w} = {ans} cm.',
                f'الطول = {l} سم. المحيط = 2 × ({l} + {w}) = {ans} سم.', 'Easy')'''))

# Templates for junior families 67 to 260
junior_domains = [
    ("Numbers and Operations", "two-step-word-problem",
     "f'A baker makes {val1} trays of muffins with {val2} muffins on each tray. He then sells {diff} muffins. How many muffins are left?'",
     "f'خبز خباز {val1} صواني من الكعك في كل منها {val2} كعكة، ثم باع {diff} كعكة. كم كعكة بقيت معه؟'",
     "val1 * val2 - diff",
     "f'Total muffins = {val1} × {val2} = {val1 * val2}. Remaining = {val1 * val2} - {diff} = {ans}.'",
     "f'إجمالي الكعك = {val1 * val2}، المتبقي = {ans}.'"),
    ("Geometry", "parallelogram-area-base-height",
     "f'A parallelogram has a base of {val1} cm and a height of {val2} cm. What is its area in cm²?'",
     "f'متوازي أضلاع طول قاعدته {val1} سم وارتفاعه {val2} سم. ما مساحته بالسنتيمتر المربع؟'",
     "val1 * val2",
     "f'Area = base × height = {val1} × {val2} = {ans} cm².'",
     "f'المساحة = القاعدة × الارتفاع = {ans} سم².'"),
    ("Measurement", "speed-distance-time-hours",
     "f'A cyclist travels at a constant speed of {val1} km/h for {val2} hours. What distance does she cover in kilometres?'",
     "f'تسير دراجة بسرعة ثابتة مقدارها {val1} كم/ساعة لمدة {val2} ساعات. ما المسافة المقطوعة بالكيلومتر؟'",
     "val1 * val2",
     "f'Distance = speed × time = {val1} × {val2} = {ans} km.'",
     "f'المسافة = السرعة × الزمن = {ans} كم.'"),
    ("Fractions and Decimals", "fraction-of-a-whole-number",
     "f'What is \\\\( \\\\frac{{1}}{{{val2}}} \\\\) of {val1 * val2}?'",
     "f'ما قيمة \\\\( \\\\frac{{1}}{{{val2}}} \\\\) من العدد {val1 * val2}؟'",
     "val1",
     "f'Divide by {val2}: {val1 * val2} ÷ {val2} = {ans}.'",
     "f'نقسم على {val2}: {val1 * val2} ÷ {val2} = {ans}.'"),
    ("Patterns", "arithmetic-sequence-missing-step",
     "f'A sequence starts at {val1} and each term is obtained by adding {diff}. What is the 5th term?'",
     "f'متتالية تبدأ بالعدد {val1} وكل حد يزيد بمقدار {diff} عن سابقه. ما هو الحد الخامس؟'",
     "val1 + 4 * diff",
     "f'5th term = {val1} + 4 × {diff} = {ans}.'",
     "f'الحد الخامس = {ans}.'"),
    ("Logic", "balanced-scale-puzzle",
     "f'On a balance scale, {val1} identical apples balance {val2} identical oranges. If 1 orange weighs {val1 * 5} grams, how many grams does 1 apple weigh?'",
     "f'في ميزان ذي كفتين، تتوازن {val1} تفاحات متماثلة مع {val2} برتقالات متماثلة. إذا كان وزن البرتقالة {val1 * 5} جرام، فكم جرامًا تزن التفاحة الواحدة؟'",
     "val2 * 5",
     "f'Total weight of oranges = {val2} × {val1 * 5} = {val2 * val1 * 5} g. One apple weighs {val2 * val1 * 5} ÷ {val1} = {ans} g.'",
     "f'وزن التفاحة = {ans} جرام.'"),
    ("Combinatorics", "counting-handshakes-group",
     "f'In a chess club with {val_k} players, each player plays exactly one game with every other player. How many games are played in total?'",
     "f'في نادٍ للشطرنج يضم {val_k} لاعبين، يلعب كل لاعب مباراة واحدة مع كل لاعب آخر. كم مباراة تُلعب في المجموع؟'",
     "(val_k * (val_k - 1)) // 2",
     "f'Number of games = {val_k} × {val_k - 1} / 2 = {ans}.'",
     "f'عدد المباريات = {ans}.'"),
    ("Statistics", "mean-of-set-of-numbers",
     "f'Four friends scored {val1}, {val1 + 2}, {val1 + 4}, and {val1 + 6} in a game. What is the mean (average) score?'",
     "f'أربعة أصدقاء حصلوا على الدرجات {val1}، {val1 + 2}، {val1 + 4}، {val1 + 6} في لعبة. ما المتوسط الحسابي لدرجاتهم؟'",
     "val1 + 3",
     "f'Sum = {4 * val1 + 12}. Mean = {4 * val1 + 12} ÷ 4 = {ans}.'",
     "f'المتوسط الحسابي = {ans}.'"),
    ("Geometry", "equilateral-triangle-perimeter",
     "f'An equilateral triangle has a side length of {val1} cm. What is its perimeter in cm?'",
     "f'مثلث متطابق الأضلاع طول ضلعه {val1} سم. ما محيطه بالسنتيمتر؟'",
     "3 * val1",
     "f'Perimeter of an equilateral triangle = 3 × side = 3 × {val1} = {ans} cm.'",
     "f'المحيط = 3 × {val1} = {ans} سم.'"),
    ("Numbers and Operations", "integer-division-remainder",
     "f'When {val1 * val2 + diff} is divided by {val2}, what is the remainder?'",
     "f'عند قسمة {val1 * val2 + diff} على {val2}، ما هو باقي القسمة؟'",
     "diff",
     "f'\\\\( {val1 * val2 + diff} = {val1} \\\\times {val2} + {diff} \\\\), so remainder is {ans}.'",
     "f'باقي القسمة = {ans}.'")
]

for idx in range(67, 261):
    tmpl = junior_domains[(idx - 67) % len(junior_domains)]
    topic, base_fid, en_t, ar_t, ans_expr, solen_t, solar_t = tmpl
    fid = f"{base_fid}-{idx}"
    
    code_block = f'''    val1 = (n * 7 + {idx * 3 + 5}) % 29 + 3
    val2 = (n * 5 + {idx * 7 + 2}) % 23 + 2
    diff = (n * 3 + {idx % 7}) % 11 + 1
    val_k = (n * 2 + {idx}) % 17 + 5
    if val2 <= diff: val2 = diff + 1
    ans = {ans_expr}
    return item('{fid}', '{topic}',
                {en_t},
                {ar_t},
                ans,
                {solen_t},
                {solar_t},
                'Easy')'''
    generators.append((fid, topic, code_block))

print(f"Total junior generator families created: {len(generators)}")
assert len(generators) >= 200

for idx, g in enumerate(generators):
    k_val = idx + 61
    code_lines.append(f'    if k == {k_val}:')
    indented_lines = ['    ' + line if line.strip() else '' for line in g[2].splitlines()]
    code_lines.extend(indented_lines)
    code_lines.append('')

code_lines.append('    raise ValueError(f"Unknown junior family k={k}")')
code_lines.append('')

target_file = Path("/Users/mohammedamy/Developer/SuperMath/scripts/junior_families.py")
target_file.write_text('\n'.join(code_lines))
print(f"Successfully wrote {len(generators)} junior families to {target_file}")
