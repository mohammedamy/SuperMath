#!/usr/bin/env python3
"""Kangaroo Benjamin (Grades 5-6): Generate 250 questions"""
import json

DATA_FILE = "data/kangaroo.json"

questions = []

topics = ["Fractions & Decimals", "Geometry & Area", "Number Theory", "Combinatorics", "Algebraic Thinking", "Logic & Puzzles"]
difficulties = ["easy", "medium", "hard"]

for i in range(1, 251):
    idx = i
    t = topics[(i - 1) % len(topics)]
    diff = difficulties[(i - 1) % len(difficulties)]
    
    a = (i * 7 + 13) % 90 + 10
    b = (i * 3 + 11) % 40 + 2
    
    if t == "Fractions & Decimals":
        denom = (i % 6) + 2
        num = (i % (denom - 1)) + 1 if denom > 2 else 1
        q_en = f"What is \\( \\dfrac{{{num}}}{{{denom}}} \\) expressed as a percentage rounded to the nearest integer?"
        pct = round((num / denom) * 100)
        q_ar = f"ما هي النسبة المئوية المرافقة للكسر \\( \\dfrac{{{num}}}{{{denom}}} \\) مقربة لأقرب عدد صحيح؟"
        opts = [f"\\( {pct - 5}\\% \\)", f"\\( {pct}\\% \\)", f"\\( {pct + 5}\\% \\)", f"\\( {pct + 10}\\% \\)"]
        corr = "1"
        exp_en = f"\\( \\dfrac{{{num}}}{{{denom}}} \\times 100\\% \\approx {pct}\\% \\)."
        exp_ar = f"\\( \\dfrac{{{num}}}{{{denom}}} \\times 100\\% \\approx {pct}\\% \\)."
        h_en = "Multiply numerator by 100 and divide by denominator."
        h_ar = "اضرب البسط في 100 واقسم على المقام."

    elif t == "Geometry & Area":
        w = (i % 15) + 3
        h = (i % 10) + 4
        area = w * h
        q_en = f"A rectangle has a length of \\( {w} \\) cm and a width of \\( {h} \\) cm. What is its area?"
        q_ar = f"مستطيل طوله \\( {w} \\) سم وعرضه \\( {h} \\) سم. ما مساحته؟"
        opts = [f"\\( {area - 2} \\) cm²", f"\\( {area} \\) cm²", f"\\( {2*(w+h)} \\) cm²", f"\\( {area + 10} \\) cm²"]
        corr = "1"
        exp_en = f"Area = length \\(\\times\\) width = \\( {w} \\times {h} = {area} \\) cm²."
        exp_ar = f"المساحة = الطول \\(\\times\\) العرض = \\( {w} \\times {h} = {area} \\) سم²."
        h_en = "Area of a rectangle is length times width."
        h_ar = "مساحة المستطيل تساوي الطول مضروباً في العرض."

    elif t == "Number Theory":
        val = i * 6 + 12
        rem = val % 7
        q_en = f"What is the remainder when \\( {val} \\) is divided by \\( 7 \\)?"
        q_ar = f"ما باقي قسمة \\( {val} \\) على \\( 7 \\)؟"
        opts = [f"\\( {rem} \\)", f"\\( {(rem+1)%7} \\)", f"\\( {(rem+2)%7} \\)", f"\\( {(rem+3)%7} \\)"]
        corr = "0"
        exp_en = f"\\( {val} = 7 \\times {val // 7} + {rem} \\). Remainder is \\( {rem} \\)."
        exp_ar = f"\\( {val} = 7 \\times {val // 7} + {rem} \\). الباقي هو \\( {rem} \\)."
        h_en = "Find the largest multiple of 7 less than or equal to the number."
        h_ar = "أوجد أكبر مضاعف للعدد 7 أقل من أو يساوي العدد."

    elif t == "Combinatorics":
        n_items = (i % 4) + 3
        fact = 1
        for k in range(1, n_items + 1):
            fact *= k
        q_en = f"In how many different ways can \\( {n_items} \\) distinct toys be arranged in a line?"
        q_ar = f"بكم طريقة مختلفة يمكن ترتيب \\( {n_items} \\) ألعاب مختلفة في صف واحد؟"
        opts = [f"\\( {fact - 2} \\)", f"\\( {fact} \\)", f"\\( {fact + 4} \\)", f"\\( {n_items * 2} \\)"]
        corr = "1"
        exp_en = f"Number of arrangements = \\( {n_items}! = {fact} \\)."
        exp_ar = f"عدد الترتيبات = \\( {n_items}! = {fact} \\)."
        h_en = f"Calculate \\( {n_items}! \\)."
        h_ar = f"احسب مضروب العدد \\( {n_items}! \\)."

    elif t == "Algebraic Thinking":
        x_val = (i % 12) + 2
        mult = (i % 4) + 2
        add_c = (i % 9) + 1
        result = mult * x_val + add_c
        q_en = f"If \\( {mult}x + {add_c} = {result} \\), what is the value of \\( x \\)?"
        q_ar = f"إذا كان \\( {mult}x + {add_c} = {result} \\)، فما قيمة \\( x \\)؟"
        opts = [f"\\( {x_val - 1} \\)", f"\\( {x_val} \\)", f"\\( {x_val + 1} \\)", f"\\( {x_val + 2} \\)"]
        corr = "1"
        exp_en = f"\\( {mult}x = {result - add_c} \\implies x = {x_val} \\)."
        exp_ar = f"\\( {mult}x = {result - add_c} \\implies x = {x_val} \\)."
        h_en = "Subtract constant first, then divide by coefficient."
        h_ar = "اطرح الثابت أولاً، ثم اقسم على معامل س."

    else: # Logic & Puzzles
        age1 = (i % 10) + 8
        age2 = age1 + (i % 5) + 2
        diff_age = age2 - age1
        q_en = f"Nora is \\( {age1} \\) years old and her sister is \\( {age2} \\) years old. What will be the difference in their ages in \\( 10 \\) years?"
        q_ar = f"نورة عمرها \\( {age1} \\) سنوات وأختها عمرها \\( {age2} \\) سنة. ما الفرق بين عمريهما بعد \\( 10 \\) سنوات؟"
        opts = [f"\\( {diff_age} \\)", f"\\( {diff_age + 10} \\)", f"\\( {diff_age * 2} \\)", f"\\( 10 \\)"]
        corr = "0"
        exp_en = f"Age difference remains constant: \\( {age2} - {age1} = {diff_age} \\) years."
        exp_ar = f"الفرق بين العمرين يبقى ثابتاً: \\( {age2} - {age1} = {diff_age} \\) سنوات."
        h_en = "Age difference between two people never changes."
        h_ar = "الفرق بين عمر شخصين لا يتغير أبداً عبر السنين."

    item = {
        "id": f"KANG-BEN-{idx:03d}",
        "track": "kangaroo",
        "level": "Benjamin",
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
print(f"Added {len(to_add)} Benjamin questions. Current counts: {dict(sorted(counts.items()))}")
