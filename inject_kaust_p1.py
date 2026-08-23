#!/usr/bin/env python3
"""KAUST SRSI Phase 1: Foundation Research Math - 250 Questions"""
import json

DATA_FILE = "data/kaust.json"

questions = []

topics = ["Graph Theory", "Combinatorics", "Matrix Theory", "Set Theory & Logic", "Polynomials", "Number Theory"]
difficulties = ["medium", "hard"]

for i in range(1, 251):
    idx = i
    t = topics[(i - 1) % len(topics)]
    diff = difficulties[(i - 1) % len(difficulties)]
    
    a = (i * 7 + 3) % 25 + 2
    b = (i * 4 + 5) % 20 + 2
    
    if t == "Graph Theory":
        vertices = (i % 8) + 4
        edges = (vertices * (vertices - 1)) // 2
        q_en = f"What is the number of edges in a complete graph \\( K_{{{vertices}}} \\) with \\( {vertices} \\) vertices?"
        q_ar = f"ما عدد الحواف في الرسم البياني الكامل \\( K_{{{vertices}}} \\) الذي يحتوي على \\( {vertices} \\) رؤوس؟"
        opts = [f"\\( {edges - 2} \\)", f"\\( {edges} \\)", f"\\( {edges + 3} \\)", f"\\( {vertices * 2} \\)"]
        corr = "1"
        exp_en = f"The number of edges in \\( K_n \\) is \\( \\dfrac{{n(n-1)}}{{2}} = \\dfrac{{{vertices} \\times {vertices-1}}}{{2}} = {edges} \\)."
        exp_ar = f"عدد الحواف في الرسم البياني الكامل \\( K_n \\) هو \\( \\dfrac{{n(n-1)}}{{2}} = \\dfrac{{{vertices} \\times {vertices-1}}}{{2}} = {edges} \\)."
        h_en = "Use the complete graph edge formula \\( \\dfrac{n(n-1)}{2} \\)."
        h_ar = "استخدم قانون عدد حواف الرسم البياني الكامل \\( \\dfrac{n(n-1)}{2} \\)."

    elif t == "Combinatorics":
        n_val = (i % 6) + 5
        r_val = 3
        import math
        comb = math.comb(n_val, r_val)
        q_en = f"How many ways can a committee of \\( 3 \\) members be chosen from \\( {n_val} \\) researchers?"
        q_ar = f"بكم طريقة يمكن اختيار لجنة مكونة من \\( 3 \\) أعضاء من بين \\( {n_val} \\) باحثين؟"
        opts = [f"\\( {comb - 5} \\)", f"\\( {comb} \\)", f"\\( {comb + 5} \\)", f"\\( {comb * 2} \\)"]
        corr = "1"
        exp_en = f"\\( \\binom{{{n_val}}}{{3}} = \\dfrac{{{n_val} \\times {n_val-1} \\times {n_val-2}}}{{6}} = {comb} \\)."
        exp_ar = f"\\( \\binom{{{n_val}}}{{3}} = \\dfrac{{{n_val} \\times {n_val-1} \\times {n_val-2}}}{{6}} = {comb} \\)."
        h_en = "Use combination formula \\( \\binom{n}{r} \\)."
        h_ar = "استخدم قانون التوافيق \\( \\binom{n}{r} \\)."

    elif t == "Matrix Theory":
        m_dim = 2
        det_val = a * b - (a + 1) * (b - 1)
        q_en = f"Find the determinant of the \\( 2 \\times 2 \\) matrix \\( \\begin{{pmatrix}} {a} & {a+1} \\\\ {b-1} & {b} \\end{{pmatrix}} \\)."
        q_ar = f"أوجد محدد المصفوفة \\( 2 \\times 2 \\) التالية: \\( \\begin{{pmatrix}} {a} & {a+1} \\\\ {b-1} & {b} \\end{{pmatrix}} \\)."
        opts = [f"\\( {det_val} \\)", f"\\( {det_val + 2} \\)", f"\\( {det_val - 2} \\)", f"\\( 0 \\)"]
        corr = "0"
        exp_en = f"\\( \\det(A) = ({a})({b}) - ({a+1})({b-1}) = {det_val} \\)."
        exp_ar = f"\\( \\det(A) = ({a})({b}) - ({a+1})({b-1}) = {det_val} \\)."
        h_en = "Determinant of 2x2 matrix is \\( ad - bc \\)."
        h_ar = "محدد مصفوفة 2x2 يساوي \\( ad - bc \\)."

    elif t == "Set Theory & Logic":
        set_a = (i % 15) + 10
        set_b = (i % 12) + 8
        inter = (i % 5) + 3
        union = set_a + set_b - inter
        q_en = f"If \\( |A| = {set_a} \\), \\( |B| = {set_b} \\), and \\( |A \\cap B| = {inter} \\), what is \\( |A \\cup B| \\)?"
        q_ar = f"إذا كان \\( |A| = {set_a} \\) و \\( |B| = {set_b} \\) و \\( |A \\cap B| = {inter} \\)، فما قيمة \\( |A \\cup B| \\)؟"
        opts = [f"\\( {union - 2} \\)", f"\\( {union} \\)", f"\\( {union + 2} \\)", f"\\( {set_a + set_b} \\)"]
        corr = "1"
        exp_en = f"By inclusion-exclusion: \\( |A \\cup B| = |A| + |B| - |A \\cap B| = {set_a} + {set_b} - {inter} = {union} \\)."
        exp_ar = f"باستخدام مبدأ الشمول والاسبعاد: \\( |A \\cup B| = {set_a} + {set_b} - {inter} = {union} \\)."
        h_en = "Use inclusion-exclusion principle."
        h_ar = "استخدم مبدأ الإدماج والاستبعاد."

    elif t == "Polynomials":
        c_val = a
        rem = 2**3 - c_val * 2 + 5
        prod_val = c_val * 2
        q_en = f"If \\( P(x) = x^3 - {c_val}x + 5 \\), what is the remainder when \\( P(x) \\) is divided by \\( (x - 2) \\)?"
        q_ar = f"إذا كان \\( P(x) = x^3 - {c_val}x + 5 \\)، فما باقي قسمة \\( P(x) \\) على \\( (x - 2) \\)؟"
        opts = [f"\\( {rem} \\)", f"\\( {rem + 3} \\)", f"\\( {rem - 3} \\)", f"\\( 0 \\)"]
        corr = "0"
        exp_en = f"By polynomial remainder theorem, Remainder = \\( P(2) = 2^3 - {c_val}(2) + 5 = {rem} \\)."
        exp_ar = f"حسب نظرية باقي البواقي: \\( P(2) = 8 - {prod_val} + 5 = {rem} \\)."
        h_en = "Evaluate \\( P(2) \\)."
        h_ar = "عوض بقيمة \\( x = 2 \\) في الكثيرة الحدود."

    else: # Number Theory
        mod_val = 13
        base = a
        ans_mod = (base ** 2) % mod_val
        q_en = f"What is \\( {base}^2 \\pmod{{13}} \\)?"
        q_ar = f"ما قيمة \\( {base}^2 \\pmod{{13}} \\)؟"
        opts = [f"\\( {ans_mod} \\)", f"\\( {(ans_mod + 2) % 13} \\)", f"\\( {(ans_mod + 5) % 13} \\)", f"\\( 0 \\)"]
        corr = "0"
        exp_en = f"\\( {base}^2 = {base**2} \\equiv {ans_mod} \\pmod{{13}} \\)."
        exp_ar = f"\\( {base}^2 = {base**2} \\equiv {ans_mod} \\pmod{{13}} \\)."
        h_en = "Square the number and take remainder modulo 13."
        h_ar = "ربع العدد ثم خذ باقي القسمة على 13."

    item = {
        "id": f"KAUST-P1-{idx:03d}",
        "track": "kaust",
        "level": "Phase 1: Foundation Research",
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
print(f"Added {len(to_add)} KAUST Phase 1 questions. Current counts: {dict(sorted(counts.items()))}")
