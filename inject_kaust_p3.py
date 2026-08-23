#!/usr/bin/env python3
"""KAUST SRSI Phase 3: Elite Research & Modeling - 250 Questions"""
import json

DATA_FILE = "data/kaust.json"

questions = []

topics = ["Differential Equations", "Optimization & Modeling", "Cryptography & Modular Math", "Complex Analysis", "Markov Chains & Probability", "Fourier Analysis"]
difficulties = ["hard"]

for i in range(1, 251):
    idx = i
    t = topics[(i - 1) % len(topics)]
    diff = "hard"
    
    a = (i * 3 + 2) % 15 + 1
    b = (i * 2 + 5) % 10 + 2
    
    if t == "Differential Equations":
        q_en = f"What is the general solution to the first-order linear differential equation \\( \\dfrac{{dy}}{{dx}} = {a}y \\)?"
        q_ar = f"ما هو الحل العام للمعادلة التفاضلية الخطية من الدرجة الأولى \\( \\dfrac{{dy}}{{dx}} = {a}y \\)؟"
        opts = [f"\\( y(x) = C e^{{{a}x}} \\)", f"\\( y(x) = C e^{{-{a}x}} \\)", f"\\( y(x) = {a}x + C \\)", f"\\( y(x) = C x^{{{a}}} \\)"]
        corr = "0"
        exp_en = f"Separation of variables gives \\( \\int \\dfrac{{dy}}{{y}} = \\int {a} dx \\implies \\ln|y| = {a}x + K \\implies y(x) = C e^{{{a}x}} \\)."
        exp_ar = f"بفصل المتغيرات: \\( \\int \\dfrac{{dy}}{{y}} = \\int {a} dx \\implies \\ln|y| = {a}x + K \\implies y(x) = C e^{{{a}x}} \\)."
        h_en = "Separate variables dy/y = a dx and integrate."
        h_ar = "افصل المتغيرات واجرِ التكامل."

    elif t == "Optimization & Modeling":
        max_val = a**2
        double_a = 2 * a
        q_en = f"Find the maximum value of the function \\( f(x) = -x^2 + {double_a}x \\) for \\( x \\in \\mathbb{{R}} \\)."
        q_ar = f"أوجد القيمة العظمى للدالة \\( f(x) = -x^2 + {double_a}x \\) عندما \\( x \\in \\mathbb{{R}} \\)."
        opts = [f"\\( {max_val - 2} \\)", f"\\( {max_val} \\)", f"\\( {max_val + 4} \\)", f"\\( {a} \\)"]
        corr = "1"
        exp_en = f"Taking derivative \\( f'(x) = -2x + {double_a} = 0 \\implies x = {a} \\). Max value \\( f({a}) = -{a}^2 + 2({a})^2 = {max_val} \\)."
        exp_ar = f"بأخذ المشتقة \\( f'(x) = -2x + {double_a} = 0 \\implies x = {a} \\). القيمة العظمى \\( f({a}) = {max_val} \\)."
        h_en = "Set derivative f'(x) equal to zero."
        h_ar = "ساوِ المشتقة الأولى بالصفر."

    elif t == "Cryptography & Modular Math":
        p = 5
        q = 7
        pq_prod = p * q
        phi_val = (p - 1) * (q - 1)
        q_en = f"In RSA cryptography, what is Euler's totient function \\( \\phi(n) \\) for \\( n = {pq_prod} = {p} \\times {q} \\)?"
        q_ar = f"في التشفير باستخدام RSA، ما قيمة دالة أيلر \\( \\phi(n) \\) للعدد \\( n = {pq_prod} = {p} \\times {q} \\)؟"
        opts = [f"\\( {phi_val - 4} \\)", f"\\( {phi_val} \\)", f"\\( {phi_val + 6} \\)", f"\\( {pq_prod - 1} \\)"]
        corr = "1"
        exp_en = f"Since \\( {p} \\) and \\( {q} \\) are primes, \\( \\phi({pq_prod}) = ({p}-1)({q}-1) = 4 \\times 6 = {phi_val} \\)."
        exp_ar = f"بما أن \\( {p} \\) و \\( {q} \\) عددان أوليان، فإن \\( \\phi({pq_prod}) = ({p}-1)({q}-1) = 4 \\times 6 = {phi_val} \\)."
        h_en = "Formula: phi(p*q) = (p-1)(q-1) for distinct primes."
        h_ar = "القانون: phi(p*q) = (p-1)(q-1) للأعداد الأولية."

    elif t == "Complex Analysis":
        mod_z_sq = a**2 + b**2
        sum_ab = a + b
        q_en = f"What is the modulus \\( |z| \\) of the complex number \\( z = {a} + {b}i \\)?"
        q_ar = f"ما هو المقياس \\( |z| \\) للعدد المركب \\( z = {a} + {b}i \\)؟"
        opts = [f"\\( \\sqrt{{{mod_z_sq}}} \\)", f"\\( {mod_z_sq} \\)", f"\\( {sum_ab} \\)", f"\\( \\sqrt{{{sum_ab}}} \\)"]
        corr = "0"
        exp_en = f"\\( |z| = \\sqrt{{Re(z)^2 + Im(z)^2}} = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{mod_z_sq}}} \\)."
        exp_ar = f"\\( |z| = \\sqrt{{Re(z)^2 + Im(z)^2}} = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{mod_z_sq}}} \\)."
        h_en = "Use definition |a + bi| = sqrt(a^2 + b^2)."
        h_ar = "استخدم تعريف المقياس |a + bi| = sqrt(a^2 + b^2)."

    elif t == "Markov Chains & Probability":
        q_en = f"Consider a 2-state Markov chain with transition matrix \\( P = \\begin{{pmatrix}} 0.7 & 0.3 \\\\ 0.4 & 0.6 \\end{{pmatrix}} \\). What is the sum of entries in any valid probability vector?"
        q_ar = f"سلسلة ماركوف بحالتين مع مصفوفة الانتقال \\( P = \\begin{{pmatrix}} 0.7 & 0.3 \\\\ 0.4 & 0.6 \\end{{pmatrix}} \\). ما مجموع عناصر أي متجه احتمالي صحيح؟"
        opts = [f"\\( 0.5 \\)", f"\\( 1.0 \\)", f"\\( 1.3 \\)", f"\\( 2.0 \\)"]
        corr = "1"
        exp_en = f"The sum of probabilities in any valid probability state vector must equal \\( 1.0 \\)."
        exp_ar = f"مجموع الاحتمالات في أي متجه حالة احتمالي يجب أن يساوي دائماً \\( 1.0 \\)."
        h_en = "Total probability of all mutually exclusive events sums to 1."
        h_ar = "مجموع الاحتمالات الكلية لجميع الأحداث المستقلة هو 1."

    else: # Fourier Analysis
        q_en = f"In Fourier Series, a function \\( f(x) \\) defined on \\( [-\\pi, \\pi] \\) is even if \\( f(-x) = f(x) \\). Which terms appear in its Fourier expansion?"
        q_ar = f"في متسلسلة فورير، الدالة الزوجية \\( f(x) \\) المعرفة على \\( [-\\pi, \\pi] \\) تحقق \\( f(-x) = f(x) \\). أي الحدود تظهر في مفكوكها؟"
        opts = [f"Sine terms only", f"Cosine terms and constant term", f"Exponential terms only", f"No terms"]
        corr = "1"
        exp_en = f"An even function has \\( b_n = 0 \\) for all \\( n \\), so its Fourier series contains only cosine terms and the constant term \\( a_0/2 \\)."
        exp_ar = f"الدالة الزوجية تحتوي فقط على حدود جيب التمام (Cosine) والحد الثابت لأن معامل الساين \\( b_n = 0 \\)."
        h_en = "Even functions multiplied by odd sine integrated over symmetric intervals yield 0."
        h_ar = "تكامل الدالة الزوجية في دالة فردية على مجال متناظر يساوي صفر."

    item = {
        "id": f"KAUST-P3-{idx:03d}",
        "track": "kaust",
        "level": "Phase 3: Elite Research",
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
print(f"Added {len(to_add)} KAUST Phase 3 questions. Current counts: {dict(sorted(counts.items()))}")
