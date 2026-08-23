#!/usr/bin/env python3
"""Kangaroo Junior (Grades 9-10): Generate 250 questions"""
import json

DATA_FILE = "data/kangaroo.json"

questions = []

topics = ["Advanced Algebra", "Trigonometry & Geometry", "Polynomials & Quadratics", "Probability & Statistics", "Sequences & Series", "Coordinate Geometry"]
difficulties = ["easy", "medium", "hard"]

for i in range(1, 251):
    idx = i
    t = topics[(i - 1) % len(topics)]
    diff = difficulties[(i - 1) % len(difficulties)]
    
    a = (i * 5 + 7) % 20 + 2
    b = (i * 3 + 4) % 15 + 1
    
    if t == "Advanced Algebra":
        # System of linear equations or exponent rules
        exp_sum = a + b
        q_en = f"Simplify the expression \\( \\dfrac{{x^{{{a + 5}}} \\cdot x^{{{b}}}}}{{x^{{5}}}} \\)."
        q_ar = f"بسط التعبير الرياضي \\( \\dfrac{{x^{{{a + 5}}} \\cdot x^{{{b}}}}}{{x^{{5}}}} \\)."
        ans_exp = exp_sum
        opts = [f"\\( x^{{{ans_exp - 1}}} \\)", f"\\( x^{{{ans_exp}}} \\)", f"\\( x^{{{ans_exp + 1}}} \\)", f"\\( x^{{{ans_exp + 5}}} \\)"]
        corr = "1"
        exp_en = f"Apply exponent rules: \\( x^{{({a}+5)+{b}-5}} = x^{{{ans_exp}}} \\)."
        exp_ar = f"تطبيق قوانين الأسس: \\( x^{{({a}+5)+{b}-5}} = x^{{{ans_exp}}} \\)."
        h_en = "Add exponents in the numerator and subtract the denominator exponent."
        h_ar = "اجمع الأسس في البسط واطرح أس المقام."

    elif t == "Trigonometry & Geometry":
        # Pythagorean theorem / basic trig
        # Right triangle with leg a, b, hyp c
        leg1 = 3 * ((i % 5) + 1)
        leg2 = 4 * ((i % 5) + 1)
        hyp = 5 * ((i % 5) + 1)
        q_en = f"In a right-angled triangle, the two legs measure \\( {leg1} \\) cm and \\( {leg2} \\) cm. What is the length of the hypotenuse?"
        q_ar = f"في مثلث قائم الزاوية، طول الساقين \\( {leg1} \\) سم و \\( {leg2} \\) سم. ما طول الوتر؟"
        opts = [f"\\( {hyp - 2} \\) cm", f"\\( {hyp} \\) cm", f"\\( {hyp + 2} \\) cm", f"\\( {leg1 + leg2} \\) cm"]
        corr = "1"
        exp_en = f"By Pythagorean theorem: \\( c = \\sqrt{{{leg1}^2 + {leg2}^2}} = {hyp} \\) cm."
        exp_ar = f"حسب نظرية فيثاغورس: \\( c = \\sqrt{{{leg1}^2 + {leg2}^2}} = {hyp} \\) سم."
        h_en = "Use Pythagorean theorem \\( a^2 + b^2 = c^2 \\)."
        h_ar = "استخدم نظرية فيثاغورس \\( a^2 + b^2 = c^2 \\)."

    elif t == "Polynomials & Quadratics":
        # Quadratic roots (x - r1)(x - r2) = x^2 - (r1+r2)x + r1*r2
        r1 = (i % 6) + 1
        r2 = (i % 5) + 2
        sum_r = r1 + r2
        prod_r = r1 * r2
        q_en = f"What is the sum of the roots of the quadratic equation \\( x^2 - {sum_r}x + {prod_r} = 0 \\)?"
        q_ar = f"ما مجموع جذري المعادلة التربيعية \\( x^2 - {sum_r}x + {prod_r} = 0 \\)؟"
        opts = [f"\\( {-sum_r} \\)", f"\\( {sum_r} \\)", f"\\( {prod_r} \\)", f"\\( {-prod_r} \\)"]
        corr = "1"
        exp_en = f"By Vieta's formulas, sum of roots = \\( -(-{sum_r}) = {sum_r} \\)."
        exp_ar = f"حسب صيغ فييتا، مجموع الجذور = \\( -(-{sum_r}) = {sum_r} \\)."
        h_en = "Sum of roots of \\( x^2 + bx + c = 0 \\) is \\( -b \\)."
        h_ar = "مجموع جذري المعادلة \\( x^2 + bx + c = 0 \\) هو \\( -b \\)."

    elif t == "Probability & Statistics":
        red = (i % 5) + 3
        blue = (i % 4) + 4
        total_marbles = red + blue
        q_en = f"A bag contains \\( {red} \\) red balls and \\( {blue} \\) blue balls. If one ball is drawn at random, what is the probability that it is red?"
        q_ar = f"يحتوي كيس على \\( {red} \\) كرات حمراء و \\( {blue} \\) كرات زرقاء. إذا سُحبت كرة واحدة عشوائياً، فما احتمال أن تكون حمراء؟"
        opts = [f"\\( \\dfrac{{{red}}}{{{total_marbles}}} \\)", f"\\( \\dfrac{{{blue}}}{{{total_marbles}}} \\)", f"\\( \\dfrac{{1}}{{{red}}} \\)", f"\\( \\dfrac{{1}}{{{blue}}} \\)"]
        corr = "0"
        exp_en = f"Probability = \\( \\dfrac{{\\text{{favorable}}}}{{\\text{{total}}}} = \\dfrac{{{red}}}{{{total_marbles}}} \\)."
        exp_ar = f"الاحتمال = \\( \\dfrac{{\\text{{عدد الحالات المواتية}}}}{{\\text{{الإجمالي}}}} = \\dfrac{{{red}}}{{{total_marbles}}} \\)."
        h_en = "Divide number of red balls by total number of balls."
        h_ar = "اقسم عدد الكرات الحمراء على إجمالي عدد الكرات."

    elif t == "Sequences & Series":
        a1 = (i % 10) + 1
        d_val = (i % 6) + 2
        term_num = 10
        a10 = a1 + (term_num - 1) * d_val
        q_en = f"Find the \\( 10 \\)th term of the arithmetic sequence with first term \\( {a1} \\) and common difference \\( {d_val} \\)."
        q_ar = f"أوجد الحد العاشر من المتتابعة الحسابية التي حدها الأول \\( {a1} \\) وأساسها \\( {d_val} \\)."
        opts = [f"\\( {a10 - d_val} \\)", f"\\( {a10} \\)", f"\\( {a10 + d_val} \\)", f"\\( {a10 + 2*d_val} \\)"]
        corr = "1"
        exp_en = f"\\( a_{{10}} = a_1 + 9d = {a1} + 9({d_val}) = {a10} \\)."
        exp_ar = f"\\( a_{{10}} = a_1 + 9d = {a1} + 9({d_val}) = {a10} \\)."
        h_en = "Use the formula \\( a_n = a_1 + (n-1)d \\)."
        h_ar = "استخدم الصيغة العامة للمتتابعة الحسابية \\( a_n = a_1 + (n-1)d \\)."

    else: # Coordinate Geometry
        x1, y1 = 0, 0
        x2 = 3 * ((i % 4) + 1)
        y2 = 4 * ((i % 4) + 1)
        dist = 5 * ((i % 4) + 1)
        q_en = f"What is the distance between the points \\( (0, 0) \\) and \\( ({x2}, {y2}) \\) in the Cartesian plane?"
        q_ar = f"ما المسافة بين النقطتين \\( (0, 0) \\) و \\( ({x2}, {y2}) \\) في المستوى الإحداثي؟"
        opts = [f"\\( {dist - 1} \\)", f"\\( {dist} \\)", f"\\( {dist + 1} \\)", f"\\( {x2 + y2} \\)"]
        corr = "1"
        exp_en = f"Distance = \\( \\sqrt{{{x2}^2 + {y2}^2}} = {dist} \\)."
        exp_ar = f"المسافة = \\( \\sqrt{{{x2}^2 + {y2}^2}} = {dist} \\)."
        h_en = "Use the distance formula \\( d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} \\)."
        h_ar = "استخدم قانون المسافة بين نقطتين \\( d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} \\)."

    item = {
        "id": f"KANG-JUN-{idx:03d}",
        "track": "kangaroo",
        "level": "Junior",
        "topic": t,
        "type": "MCQ",
        "difficulty": diff,
        "content": {
            "en": {
                "question": q_en,
                "options": opts,
                "hint": h_en,
                "explanation": exp_en
            },
            "ar": {
                "question": q_ar,
                "options": opts,
                "hint": h_ar,
                "explanation": exp_ar
            }
        },
        "correct_index": corr
    }
    questions.append(item)

with open(DATA_FILE, "r", encoding="utf-8") as f:
    all_questions = json.load(f)

existing_ids = {q["id"] for q in all_questions}
to_add = [q for q in questions if q["id"] not in existing_ids]
all_questions.extend(to_add)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

from collections import Counter
counts = Counter(q.get("level") for q in all_questions)
print(f"Added {len(to_add)} Junior questions. Current counts: {dict(sorted(counts.items()))}")
