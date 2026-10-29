"""KAUST Mathematics Competition (KMC) — Track 2: Grades 8-9
Pillar 1: Algebra, Radicals, Exponents, Work-Rate, Factoring Tricks & Sequences (115 questions).
Strictly aligned with official KMC Grades 8-9 Junior syllabus (no calculators).
"""
from fractions import Fraction
import math
from kmc_common import m, explain_en, explain_ar, make_5_math_options, make_kmc_question

LEVEL = "Track 2: Grades 8-9"


def generate_t2_algebra() -> list[dict]:
    items = []
    idx = 1

    def next_id():
        nonlocal idx
        qid = f"KAUST-G89-A{idx:03d}"
        idx += 1
        return qid

    # 1. Nested radicals & sqrt((a - sqrt(b))^2) = |a - sqrt(b)| (10 variants) — KMC Junior Cat A Q1!
    # Keep surd > whole (or whole > surd) cleanly!
    rad_cases = [
        # sqrt( (k - sqrt(p))^2 ) + sqrt(p) where sqrt(p) > k => (sqrt(p) - k) + sqrt(p) = 2*sqrt(p) - k, OR -sqrt(p) cancels surd!
        # Even cleaner: |k - sqrt(p)| + |m - sqrt(p)| where k < sqrt(p) < m => (sqrt(p) - k) + (m - sqrt(p)) = m - k (pure integer!)
        (1, 3, 2),    # |1 - sqrt(3)| + |2 - sqrt(3)| = (sqrt(3)-1) + (2-sqrt(3)) = 1
        (2, 5, 3),    # |2 - sqrt(5)| + |3 - sqrt(5)| = 1 -> let's vary m - k!
        (1, 5, 3),    # sqrt(5)≈2.23 -> (sqrt5 - 1) + (3 - sqrt5) = 2
        (2, 7, 5),    # sqrt(7)≈2.64 -> (sqrt7 - 2) + (5 - sqrt7) = 3
        (1, 6, 5),    # sqrt(6)≈2.45 -> 4
        (3, 11, 6),   # sqrt(11)≈3.31 -> 3
        (2, 10, 7),   # sqrt(10)≈3.16 -> 5
        (3, 13, 8),   # sqrt(13)≈3.60 -> 5
        (4, 19, 10),  # sqrt(19)≈4.35 -> 6
        (2, 8, 9),    # sqrt(8)≈2.82 -> 7
        (5, 29, 12),  # sqrt(29)≈5.38 -> 7
    ]
    rad_cases = rad_cases[:10]
    rad_cases[1] = (2, 6, 8)  # 8 - 2 = 6
    for k, p, hi in rad_cases:
        qid = next_id()
        assert k * k < p < hi * hi
        ans = hi - k
        q_en = (
            f"Without using a calculator, find the exact value of the expression: "
            f"{m(f'\\sqrt{{({k} - \\sqrt{{{p}}})^2}} + \\sqrt{{({hi} - \\sqrt{{{p}}})^2}}')}."
        )
        q_ar = (
            f"دون استخدام الآلة الحاسبة، أوجد القيمة الدقيقة للمقدار: "
            f"{m(f'\\sqrt{{({k} - \\sqrt{{{p}}})^2}} + \\sqrt{{({hi} - \\sqrt{{{p}}})^2}}')}."
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [hi + k, f"2\\sqrt{{{p}}} - {k + hi}", f"{k + hi} - 2\\sqrt{{{p}}}", ans + 2, max(1, ans - 2)], qid
        )
        sol_en = explain_en(
            "Crucial Radical Rule: **The square root of a square is NEVER negative!** That means "
            f"{m('\\sqrt{A^2} = |A|')} (if {m('A')} is negative, flip its subtraction order so the result is positive!).",
            [
                f"**Compare {m(f'\\sqrt{{{p}}}')} with {m(k)} and {m(hi)}:** Since {m(f'{k}^2 = {k*k}')} and {m(f'{hi}^2 = {hi*hi}')}, and {m(f'{k*k} < {p} < {hi*hi}')}, we know {m(f'{k} < \\sqrt{{{p}}} < {hi}')}.",
                f"**First square root:** Because {m(f'{k} < \\sqrt{{{p}}}')}, {m(f'{k} - \\sqrt{{{p}}}')} is negative! Flipping it positive gives {m(f'\\sqrt{{({k} - \\sqrt{{{p}}})^2}} = \\sqrt{{{p}}} - {k}')}.",
                f"**Second square root:** Because {m(f'{hi} > \\sqrt{{{p}}}')}, {m(f'{hi} - \\sqrt{{{p}}}')} is already positive, so {m(f'\\sqrt{{({hi} - \\sqrt{{{p}}})^2}} = {hi} - \\sqrt{{{p}}}')}.",
                f"**Add them together:** {m(f'(\\sqrt{{{p}}} - {k}) + ({hi} - \\sqrt{{{p}}}) = {hi} - {k} = {ans}')} (the {m(f'\\sqrt{{{p}}}')} terms cancel completely!).",
            ],
            f"Common trap: writing {m(f'({k} - \\sqrt{{{p}}})')} directly without checking its sign would give the wrong sign!",
        )
        sol_ar = explain_ar(
            f"قاعدة جوهرية في الجذور التربيعية: **الجذر التربيعي لا يعطي قيمة سالبة أبدًا!** أي أن {m('\\sqrt{A^2} = |A|')}؛ فإذا كان ما داخل التربيع سالبًا نعكس ترتيب الطرح ليصبح موجبًا!",
            [
                f"**نحدد موقع {m(f'\\sqrt{{{p}}}')}:** بما أن {m(f'{k}^2 = {k*k}')} و {m(f'{hi}^2 = {hi*hi}')}، وأن {m(f'{k*k} < {p} < {hi*hi}')}، فإن {m(f'{k} < \\sqrt{{{p}}} < {hi}')}.",
                f"**الجذر الأول:** المقدار {m(f'{k} - \\sqrt{{{p}}}')} سالب لأن {m(k)} أصغر من {m(f'\\sqrt{{{p}}}')}، لذا تكون قيمته الموجبة {m(f'\\sqrt{{{p}}} - {k}')}.",
                f"**الجذر الثاني:** المقدار {m(f'{hi} - \\sqrt{{{p}}}')} موجب لأن {m(hi)} أكبر من {m(f'\\sqrt{{{p}}}')}، فيخرج كما هو {m(f'{hi} - \\sqrt{{{p}}}')}.",
                f"**نجمع الناتجين:** {m(f'(\\sqrt{{{p}}} - {k}) + ({hi} - \\sqrt{{{p}}}) = {hi} - {k} = {ans}')} حيث يختصر {m(f'\\sqrt{{{p}}}')} مع {m(f'-\\sqrt{{{p}}}')}!",
            ],
            f"احذر من الخطأ الشائع بإخراج {m(f'{k} - \\sqrt{{{p}}}')} كما هو دون القيمة المطلقة؛ الناتج الصحيح هو {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-nested-radical-abs",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Remember √(X²) = |X| ≥ 0! Check whether {k} - √{p} and {hi} - √{p} are positive or negative by squaring {k} and {hi}.",
            f"تذكّر أن √(X²) = |X| ≥ 0 دائمًا! قارن مربعَي {k} و {hi} بالعدد {p} لتعرف إشارة كل قوس.",
            sol_en, sol_ar
        ))

    # 2. Combined work-rate in minutes (10 variants) — KMC Junior Cat A Q2!
    work_cases = [
        (4, 6, "Ahmad", "Khalid", "plant a field", "أحمد", "خالد", "زراعة حقل"),        # 144 min
        (3, 6, "Noura", "Salma", "paint a mural", "نورة", "سلمى", "طلاء جدارية"),       # 120 min
        (2, 3, "Faisal", "Omar", "catalog library books", "فيصل", "عمر", "فهرسة الكتب"), # 72 min
        (5, 20, "Pump A", "Pump B", "fill a water reservoir", "المضخة A", "المضخة B", "ملء خزان مياه"), # 240 min
        (3, 5, "Printer A", "Printer B", "print contest booklets", "الطابعة A", "الطابعة B", "طباعة كتيبات المسابقة"), # 112.5? Wait 60*15/8 not int! Let's ensure integer minutes!
        (4, 12, "Tariq", "Rayan", "wash the school courtyard", "طارق", "ريان", "تنظيف ساحة المدرسة"), # 180 min
        (6, 12, "Lina", "Huda", "prepare science kits", "لينا", "هدى", "تجهيز حقائب المختبر"), # 240 min
        (3, 12, "Sami", "Ziad", "mow a sports field", "سامي", "زياد", "قص عشب الملعب"), # 144 min
        (5, 10, "Machine 1", "Machine 2", "pack date boxes", "الآلة 1", "الآلة 2", "تعبئة علب التمر"), # 200 min
        (6, 10, "Maha", "Reem", "decorate the auditorium", "مها", "ريم", "تزيين المسرح"), # 225 min
        (2, 6, "Pipe 1", "Pipe 2", "fill a swimming pool", "الأنبوب 1", "الأنبوب 2", "ملء مسبح"), # 90 min
    ]
    work_cases = [c for c in work_cases if (60 * c[0] * c[1]) % (c[0] + c[1]) == 0][:10]
    assert len(work_cases) == 10
    for h1, h2, p1_e, p2_e, task_e, p1_a, p2_a, task_a in work_cases:
        qid = next_id()
        ans = (60 * h1 * h2) // (h1 + h2)
        L_hr = math.lcm(h1, h2)
        r1, r2 = L_hr // h1, L_hr // h2
        comb_num, comb_den = r1 + r2, L_hr
        q_en = (
            f"{p1_e} needs {m(h1)} hours working alone to {task_e}, while {p2_e} needs {m(h2)} hours working alone to complete the exact same job. "
            f"How many **minutes** will they need if they work together at their constant rates?"
        )
        q_ar = (
            f"يحتاج {p1_a} إلى {m(h1)} ساعات بمفرده لإنجاز ({task_a})، بينما يحتاج {p2_a} إلى {m(h2)} ساعات بمفرده لإنجاز العمل نفسه. "
            f"كم **دقيقة** يحتاجان إذا عملا معًا في الوقت نفسه؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [(h1 + h2) * 30, ans + 15, ans - 12, 60 * abs(h2 - h1)], qid
        )
        sol_en = explain_en(
            "Never add the hours (`h₁ + h₂`) — working together makes the job **faster**, not slower! Add **what fraction of the job each finishes in 1 hour**!",
            [
                f"**Hourly rates:** In {m(1)} hour, {p1_e} finishes {m(f'\\frac{{1}}{{{h1}}}')} of the job, and {p2_e} finishes {m(f'\\frac{{1}}{{{h2}}}')} of the job.",
                f"**Combined fraction in 1 hour:** Use common denominator {m(L_hr)}: {m(f'\\frac{{1}}{{{h1}}} + \\frac{{1}}{{{h2}}} = \\frac{{{r1}}}{{{L_hr}}} + \\frac{{{r2}}}{{{L_hr}}} = \\frac{{{comb_num}}}{{{comb_den}}}')} of the job per hour.",
                f"**Flip to get total hours, then convert to minutes:** Total hours {m(f'= \\frac{{{comb_den}}}{{{comb_num}}}')}. Multiply by {m(60)} minutes/hour: {m(f'60 \\times \\frac{{{comb_den}}}{{{comb_num}}} = {ans}')} minutes!",
            ],
            f"Sanity check: working together ({m(ans)} min) is faster than {p1_e} alone ({m(h1 * 60)} min)!",
        )
        sol_ar = explain_ar(
            "لا تجمع الساعات أبدًا! فالعمل الجماعي يقلّل الزمن ولا يزيده. بدلًا من ذلك، نجمع **الجزء الذي ينجزه كلٌّ منهما في الساعة الواحدة**!",
            [
                f"**معدل الإنجاز في الساعة:** ينجز الأول {m(f'\\frac{{1}}{{{h1}}}')} من العمل في الساعة، وينجز الثاني {m(f'\\frac{{1}}{{{h2}}}')} في الساعة.",
                f"**ما ينجزانه معًا في ساعة واحدة:** بتوحيد المقامات على {m(L_hr)}: {m(f'\\frac{{1}}{{{h1}}} + \\frac{{1}}{{{h2}}} = \\frac{{{r1} + {r2}}}{{{L_hr}}} = \\frac{{{comb_num}}}{{{comb_den}}}')}.",
                f"**الزمن الكلي بالدقائق:** نقلب الكسر لإيجاد عدد الساعات ({m(f'\\frac{{{comb_den}}}{{{comb_num}}}')} ساعة)، ثم نضرب في {m(60)}: {m(f'60 \\times \\frac{{{comb_den}}}{{{comb_num}}} = {ans}')} دقيقة.",
            ],
            f"تحقق منطقي: الزمن المشترك ({m(ans)} دقيقة) أقل من زمن الأسرع بمفرده ({m(min(h1,h2)*60)} دقيقة).",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-work-rate-minutes",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the fraction of the job done in 1 hour together (1/{h1} + 1/{h2}), invert it for hours, and multiply by 60 for minutes!",
            f"اجمع ما ينجزانه في ساعة واحدة (1/{h1} + 1/{h2})، ثم اقلب الكسر واضربه في 60 لتحويله إلى دقائق!",
            sol_en, sol_ar
        ))

    # 3. Powers of 2 factoring & algebraic expression = 2^m (10 variants) — KMC Junior Cat A Q3!
    # a = 2^(k+1), b = 2^k => a^2 + 2ab + 4b^2 + 2^(2k+2) = 4*2^(2k) + 4*2^(2k) + 4*2^(2k) + 4*2^(2k) = 16*2^(2k) = 2^(2k+4)!
    pow2_cases = [
        (4, "base4"),   # a=2^5, b=2^4, extra=2^10 => m = 12 (exact KMC Junior Cat A Q3!)
        (3, "base4"),   # a=2^4, b=2^3, extra=2^8 => m = 10
        (5, "base4"),   # a=2^6, b=2^5, extra=2^12 => m = 14
        (6, "base4"),   # a=2^7, b=2^6, extra=2^14 => m = 16
        (2, "base4"),   # a=2^3, b=2^2, extra=2^6 => m = 8
        (7, "base4"),   # a=2^8, b=2^7, extra=2^16 => m = 18
        (4, "sum8"),    # 2^k + 2^k + 2^(k+1) + 2^(k+2) = 2^(k+3)
        (8, "sum8"),
        (10, "sum8"),
        (12, "sum8"),
    ]
    for k, mode in pow2_cases:
        qid = next_id()
        if mode == "base4":
            ea, eb, ec = k + 1, k, 2 * k + 2
            ans = 2 * k + 4
            assert (2**ea)**2 + 2*(2**ea)*(2**eb) + 4*(2**eb)**2 + 2**ec == 2**ans
            q_en = (
                f"If the algebraic expression {m(f'a^2 + 2ab + 4b^2 + 2^{{{ec}}}')} equals {m('2^m')} "
                f"when {m(f'a = 2^{{{ea}}}')} and {m(f'b = 2^{{{eb}}}')}, what is the value of {m('m')}?"
            )
            q_ar = (
                f"إذا كانت قيمة المقدار الجبري {m(f'a^2 + 2ab + 4b^2 + 2^{{{ec}}}')} تساوي {m('2^m')} "
                f"عندما {m(f'a = 2^{{{ea}}}')} و {m(f'b = 2^{{{eb}}}')}، فما قيمة {m('m')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans - 2, ans - 1, ans + 1, ans + 2], qid
            )
            sol_en = explain_en(
                "Exponent Rules Refresher: "
                f"{m('(2^x)^2 = 2^{2x}')} and {m('2^x \\times 2^y = 2^{x+y}')}. Rewrite **every single term** as a power of 2, then combine identical powers!",
                [
                    f"**Term 1 ({m('a^2')}):** {m(f'(2^{{{ea}}})^2 = 2^{{{2*ea}}}')}.",
                    f"**Term 2 ({m('2ab')}):** {m(f'2^1 \\times 2^{{{ea}}} \\times 2^{{{eb}}} = 2^{{1 + {ea} + {eb}}} = 2^{{{ec}}}')}.",
                    f"**Term 3 ({m('4b^2')}):** Since {m('4 = 2^2')}, we get {m(f'2^2 \\times (2^{{{eb}}})^2 = 2^{{2 + {2*eb}}} = 2^{{{ec}}}')}.",
                    f"**Combine all 4 terms:** Every one of the four terms equals {m(f'2^{{{ec}}}')}! Adding four copies of {m(f'2^{{{ec}}}')} gives {m(f'4 \\times 2^{{{ec}}} = 2^2 \\times 2^{{{ec}}} = 2^{{{ans}}}')}, so {m(f'm = {ans}')}!",
                ],
                f"Key insight: {m('2^N + 2^N + 2^N + 2^N = 4 \\cdot 2^N = 2^{N+2}')} — we add exponents only when multiplying, so factor out the count {m('4 = 2^2')}!",
            )
            sol_ar = explain_ar(
                f"تذكير بقوانين الأسس: {m('(2^x)^2 = 2^{2x}')} و {m('2^x \\times 2^y = 2^{x+y}')}. نكتب **كل حد على صورة قوة للعدد 2** ثم نجمع الحدود المتشابهة!",
                [
                    f"**الحد الأول ({m('a^2')}):** {m(f'(2^{{{ea}}})^2 = 2^{{{2*ea}}}')}.",
                    f"**الحد الثاني ({m('2ab')}):** {m(f'2^1 \\times 2^{{{ea}}} \\times 2^{{{eb}}} = 2^{{{ec}}}')}.",
                    f"**الحد الثالث ({m('4b^2')}):** بما أن {m('4 = 2^2')} فإن {m(f'2^2 \\times 2^{{{2*eb}}} = 2^{{{ec}}}')}.",
                    f"**نجمع الحدود الأربعة:** جميع الحدود الأربعة متساوية وتساوي {m(f'2^{{{ec}}}')}! إذن مجموعها {m(f'4 \\times 2^{{{ec}}} = 2^2 \\times 2^{{{ec}}} = 2^{{{ans}}}')}، ومنه {m(f'm = {ans}')}.",
                ],
                f"انتبه: عند جمع أربع نسخ من {m(f'2^{{{ec}}}')} نضرب في {m('4 = 2^2')} فيزيد الأس بمقدار {m(2)} ليصبح {m(ans)}.",
            )
        else:
            ans = k + 3
            assert 2**k + 2**k + 2**(k+1) + 2**(k+2) == 2**ans
            q_en = (
                f"If {m(f'2^{{{k}}} + 2^{{{k}}} + 2^{{{k+1}}} + 2^{{{k+2}}} = 2^m')}, what is the value of {m('m')}?"
            )
            q_ar = (
                f"إذا كان {m(f'2^{{{k}}} + 2^{{{k}}} + 2^{{{k+1}}} + 2^{{{k+2}}} = 2^m')}، فما قيمة الأس {m('m')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [4 * k + 3, k + 2, k + 4, k + 1], qid
            )
            sol_en = explain_en(
                "Golden Rule for Adding Powers of 2: **Two identical powers of 2 combine into the NEXT power of 2**, because `2ⁿ + 2ⁿ = 2 × 2ⁿ = 2ⁿ⁺¹`!",
                [
                    f"Combine the first two identical terms: {m(f'2^{{{k}}} + 2^{{{k}}} = 2 \\times 2^{{{k}}} = 2^{{{k+1}}}')}.",
                    f"Now add that to the third term {m(f'2^{{{k+1}}}')}: {m(f'2^{{{k+1}}} + 2^{{{k+1}}} = 2 \\times 2^{{{k+1}}} = 2^{{{k+2}}}')}.",
                    f"Finally, add that to the fourth term {m(f'2^{{{k+2}}}')}: {m(f'2^{{{k+2}}} + 2^{{{k+2}}} = 2 \\times 2^{{{k+2}}} = 2^{{{k+3}}}')}. Thus {m(f'm = {ans}')}!",
                ],
                f"Domino chain check: you can also factor out {m(f'2^{{{k}}}')} to get {m(f'2^{{{k}}}(1 + 1 + 2 + 4) = 2^{{{k}}} \\times 8 = 2^{{{k}}} \\times 2^3 = 2^{{{ans}}}')}!",
            )
            sol_ar = explain_ar(
                "القاعدة الذهبية لجمع قوى العدد 2: **مجموع قوتين متماثلتين للعدد 2 يعطي القوة التالية مباشرة** لأن `2ⁿ + 2ⁿ = 2 × 2ⁿ = 2ⁿ⁺¹`!",
                [
                    f"نجمع أول حدين متساويين: {m(f'2^{{{k}}} + 2^{{{k}}} = 2^{{{k+1}}}')}.",
                    f"نضيف الناتج إلى الحد الثالث: {m(f'2^{{{k+1}}} + 2^{{{k+1}}} = 2^{{{k+2}}}')}.",
                    f"نضيف الناتج إلى الحد الرابع: {m(f'2^{{{k+2}}} + 2^{{{k+2}}} = 2^{{{k+3}}}')}، وبذلك تكون قيمة {m(f'm = {ans}')}.",
                ],
                f"تحقق بإخراج عامل مشترك: {m(f'2^{{{k}}}(1 + 1 + 2 + 4) = 2^{{{k}}} \\times 8 = 2^{{{k}}} \\times 2^3 = 2^{{{ans}}}')}.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-powers-of-two-sum",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Never add exponents across a '+' sign! Instead, use 2^n + 2^n = 2^(n+1) or factor out the smallest power of 2.",
            "لا تجمع الأسس في عملية الجمع! استخدم العلاقة 2^n + 2^n = 2^(n+1) أو أخرج أصغر قوة لـ 2 عاملًا مشتركًا.",
            sol_en, sol_ar
        ))

    # 4. Contest scoring (+P correct, -D wrong, U unanswered) (10 variants) — KMC Junior Q9!
    score_cases = [
        (30, 4, 1, 1, 6, "Salma", "سلمى"),   # 29 answered: 23*4 - 6*1 = 86 -> wrong = 6!
        (25, 4, 1, 2, 5, "Hamza", "حمزة"),   # 23 answered: 18*4 - 5*1 = 67 -> wrong = 5
        (30, 5, 2, 2, 4, "Noura", "نورة"),   # 28 answered: 24*5 - 4*2 = 112 -> wrong = 4
        (24, 5, 1, 1, 5, "Tariq", "طارق"),   # 23 answered: 18*5 - 5*1 = 85 -> wrong = 5
        (20, 4, 1, 0, 3, "Lina", "لينا"),    # 20 answered: 17*4 - 3*1 = 65 -> wrong = 3
        (30, 4, 1, 3, 7, "Omar", "عمر"),     # 27 answered: 20*4 - 7*1 = 73 -> wrong = 7
        (25, 5, 2, 1, 6, "Rayan", "ريان"),   # 24 answered: 18*5 - 6*2 = 78 -> wrong = 6
        (40, 3, 1, 4, 8, "Maha", "مها"),     # 36 answered: 28*3 - 8*1 = 76 -> wrong = 8
        (24, 4, 2, 2, 3, "Faisal", "فيصل"),  # 22 answered: 19*4 - 3*2 = 70 -> wrong = 3
        (30, 5, 1, 0, 9, "Huda", "هدى"),     # 30 answered: 21*5 - 9*1 = 96 -> wrong = 9
    ]
    for n_q, pt_c, pt_w, n_un, n_wr, nm_e, nm_a in score_cases:
        qid = next_id()
        n_ans = n_q - n_un
        n_cor = n_ans - n_wr
        score = n_cor * pt_c - n_wr * pt_w
        ans = n_wr
        q_en = (
            f"A math competition has {m(n_q)} problems. Each correct answer earns {m(pt_c)} points, "
            f"{m(pt_w)} point(s) are deducted for each wrong answer, and {m(0)} points are given for unanswered problems. "
            f"{nm_e} scored {m(score)} points and left **exactly {m(n_un)}** problem(s) unanswered. "
            f"How many problems did {nm_e} answer **incorrectly**?"
        )
        q_ar = (
            f"تتكوّن مسابقة رياضيات من {m(n_q)} سؤالًا؛ تُمنح {m(pt_c)} نقاط لكل إجابة صحيحة، "
            f"ويُخصم {m(pt_w)} نقطة لكل إجابة خاطئة، و {m(0)} للأسئلة المتروكة دون إجابة. "
            f"حصل/حصلت {nm_a} على {m(score)} نقطة وترك **{m(n_un)}** من الأسئلة دون إجابة. "
            f"كم سؤالًا أجاب عنه **بشكل خاطئ**؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans - 1, ans + 1, ans + 2, n_cor, max(1, ans - 2)], qid
        )
        all_right_pts = n_ans * pt_c
        loss_per_wr = pt_c + pt_w
        sol_en = explain_en(
            f"Super-Easy 'Perfect Score Drop' Method: Imagine all answered questions were right first, and notice that changing 1 right answer into 1 wrong answer drops the score by **{m(f'{pt_c} + {pt_w} = {loss_per_wr}')} points** (you lose the `+{pt_c}` AND get `- {pt_w}`)!",
            [
                f"**Count answered problems:** Out of {m(n_q)}, {m(n_un)} were left blank, so {nm_e} answered {m(f'{n_q} - {n_un} = {n_ans}')} problems.",
                f"**If all {m(n_ans)} answered problems were correct:** Score would be {m(f'{n_ans} \\times {pt_c} = {all_right_pts}')} points. Actual score is {m(score)}, which is lower by {m(f'{all_right_pts} - {score} = {all_right_pts - score}')} points.",
                f"**Divide by the drop per wrong answer ({m(f'{pt_c} + {pt_w} = {loss_per_wr}')}):** {m(f'{all_right_pts - score} \\div {loss_per_wr} = {ans}')} wrong answers!",
            ],
            f"Check: {m(n_cor)} correct ({m(f'+{n_cor*pt_c}')}) and {m(ans)} wrong ({m(f'-{ans*pt_w}')}) gives {m(f'{n_cor*pt_c} - {ans*pt_w} = {score}')} points!",
        )
        sol_ar = explain_ar(
            f"طريقة (الفرق عن العلامة الكاملة) السهلة: لو كانت جميع الأسئلة المجاب عنها صحيحة لحصل على أعلى مجموع، وتبديل إجابة واحدة من صحيحة إلى خاطئة يُنقص الدرجة بمقدار **{m(f'{pt_c} + {pt_w} = {loss_per_wr}')} نقاط** (خسارة الـ {m(pt_c)} نقاط + خصم {m(pt_w)})!",
            [
                f"**عدد الأسئلة المجاب عنها:** {m(f'{n_q} - {n_un} = {n_ans}')} سؤالًا.",
                f"**لو كانت الـ {m(n_ans)} كلها صحيحة:** لكانت الدرجة {m(f'{n_ans} \\times {pt_c} = {all_right_pts}')}، أي أعلى من الدرجة الفعلية بـ {m(f'{all_right_pts} - {score} = {all_right_pts - score}')} نقطة.",
                f"**عدد الإجابات الخاطئة:** نقسم فرق النقاط على خسارة الخطأ الواحد ({m(loss_per_wr)}): {m(f'{all_right_pts - score} \\div {loss_per_wr} = {ans}')} إجابات خاطئة!",
            ],
            f"تحقق: {m(n_cor)} صحيحة ({m(n_cor*pt_c)}) ناقص خصم {m(ans)} خاطئة ({m(ans*pt_w)}) = {m(score)} نقطة.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-contest-scoring",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"First find how many questions were answered ({n_q} - {n_un}). Remember each wrong answer costs ({pt_c} + {pt_w}) points compared to a correct answer!",
            f"احسب أولًا عدد الأسئلة المجاب عنها ({n_q} - {n_un})، وتذكّر أن كل إجابة خاطئة تُفقد ({pt_c} + {pt_w}) نقاط مقارنة بالإجابة الصحيحة!",
            sol_en, sol_ar
        ))

    # 5. Factoring trick: ab + a + b = C for positive integers a, b (find a + b) (10 variants)
    # (a + 1)(b + 1) = C + 1, choose C + 1 = p * q (two distinct primes > 2!) so {a+1, b+1} = {p, q} is UNIQUE!
    simon_cases = [
        (3, 5), (3, 7), (5, 7), (3, 11), (5, 11),
        (7, 11), (3, 13), (5, 13), (7, 13), (11, 13),
    ]
    for p, q in simon_cases:
        qid = next_id()
        C = p * q - 1
        a_v, b_v = p - 1, q - 1
        ans = a_v + b_v
        q_en = (
            f"Positive integers {m('a')} and {m('b')} satisfy the equation {m(f'ab + a + b = {C}')}. "
            f"What is the value of {m('a + b')}?"
        )
        q_ar = (
            f"عددان صحيحان موجبان {m('a')} و {m('b')} يحققان المعادلة {m(f'ab + a + b = {C}')}. "
            f"ما قيمة المجموع {m('a + b')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [p + q, a_v * b_v, ans + 2, ans - 2], qid
        )
        sol_en = explain_en(
            "Classic KMC Factoring Trick: **Add `1` to both sides** of `ab + a + b = C`! Why? Because `ab + a + b + 1` factors cleanly into `(a + 1)(b + 1)`!",
            [
                f"Add {m(1)} to both sides of the equation: {m(f'ab + a + b + 1 = {C} + 1 = {p*q}')}.",
                f"Factor the left side by grouping: {m('a(b + 1) + 1(b + 1) = (a + 1)(b + 1)')}, so {m(f'(a + 1)(b + 1) = {p*q}')}.",
                f"Since {m('a, b \\ge 1')}, both {m('a + 1 \\ge 2')} and {m('b + 1 \\ge 2')}. Because {m(f'{p*q} = {p} \\times {q}')} is a product of two primes, the two factors must be {m(p)} and {m(q)}!",
                f"Subtract {m(1)} from each factor: {m(f'\\{{a, b\\}} = \\{{{a_v}, {b_v}\\}}')}, so {m(f'a + b = {a_v} + {b_v} = {ans}')}.",
            ],
            f"Plug {m(a_v)} and {m(b_v)} back in: {m(f'{a_v}\\times{b_v} + {a_v} + {b_v} = {a_v*b_v} + {ans} = {C}')}!",
        )
        sol_ar = explain_ar(
            "حيلة التحليل الشهيرة في مسابقات كاوست: **أضف `1` إلى طرفَي المعادلة** `ab + a + b = C`! لأن المقدار `ab + a + b + 1` يتحلل مباشرة إلى القوسين `(a + 1)(b + 1)`!",
            [
                f"نضيف {m(1)} إلى الطرفين: {m(f'ab + a + b + 1 = {C} + 1 = {p*q}')}.",
                f"نحلّل الطرف الأيسر: {m(f'(a + 1)(b + 1) = {p*q}')}.",
                f"بما أن {m('a, b \\ge 1')} فإن القوسين أكبر من أو يساويان {m(2)}، والعدد {m(p*q)} يتحلل بشكل وحيد إلى العاملين الأوليين {m(f'{p} \\times {q}')}.",
                f"إذن العددان هما {m(f'{p}-1 = {a_v}')} و {m(f'{q}-1 = {b_v}')}، ومجموعهما {m(f'a + b = {a_v} + {b_v} = {ans}')}.",
            ],
            f"تحقق بالتعويض: {m(f'{a_v}\\times{b_v} + {a_v} + {b_v} = {a_v*b_v} + {ans} = {C}')} بالضبط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Hard", "g89-add-one-factoring",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Add 1 to both sides so the left-hand side becomes ab + a + b + 1 = (a + 1)(b + 1)!",
            "أضف 1 إلى الطرفين ليصبح الطرف الأيسر قابلاً للتحليل على الصورة (a + 1)(b + 1)!",
            sol_en, sol_ar
        ))

    # 6. Mental difference of squares (A^2 - B^2) / D without calculator (10 variants)
    dos_cases = [
        (2026, 2024, 1, 8100),   # (4050 * 2) = 8100
        (503, 497, 6, 1000),     # (1000 * 6) / 6 = 1000
        (1005, 995, 10, 2000),   # (2000 * 10) / 10 = 2000
        (304, 296, 8, 600),      # (600 * 8) / 8 = 600
        (752, 748, 4, 1500),     # (1500 * 4) / 4 = 1500
        (153, 147, 1, 1800),     # 300 * 6 = 1800
        (254, 246, 1, 4000),     # 500 * 8 = 4000
        (605, 595, 5, 2400),     # (1200 * 10) / 5 = 2400
        (403, 397, 3, 1600),     # (800 * 6) / 3 = 1600
        (852, 848, 2, 3400),     # (1700 * 4) / 2 = 3400
    ]
    for A, B, D, ans in dos_cases:
        qid = next_id()
        assert (A * A - B * B) // D == ans and (A * A - B * B) % D == 0
        expr_tex = f"{A}^2 - {B}^2" if D == 1 else f"\\frac{{{A}^2 - {B}^2}}{{{D}}}"
        q_en = f"Without using a calculator, compute the exact value of {m(expr_tex)}."
        q_ar = f"دون استخدام الآلة الحاسبة، احسب القيمة الدقيقة للمقدار {m(expr_tex)}."
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [(A - B) ** 2 // D if (A - B) ** 2 >= D else ans // 2, ans // 2, ans + (A - B) * 10, ans * 2], qid
        )
        sol_en = explain_en(
            "Never multiply huge numbers like " + m(f"{A}\\times{A}") + " by hand! Use the **Difference of Squares** shortcut: "
            f"{m('A^2 - B^2 = (A - B)(A + B)')}!",
            [
                f"**Subtract the two numbers:** {m(f'{A} - {B} = {A - B}')}.",
                f"**Add the two numbers:** {m(f'{A} + {B} = {A + B}')} (a clean round number!).",
                (
                    f"**Multiply them:** {m(f'{A - B} \\times {A + B} = {ans}')}."
                    if D == 1 else
                    f"**Substitute and simplify:** {m(f'\\frac{{({A - B}) \\times ({A + B})}}{{{D}}} = {ans}')}."
                ),
            ],
            f"Difference of squares turns two hard squarings into one mental addition ({m(A+B)}) and one tiny subtraction ({m(A-B)})!",
        )
        sol_ar = explain_ar(
            f"لا تضرب الأعداد الكبيرة مثل {m(f'{A}\\times{A}')} يدويًا! استخدم متطابقة **الفرق بين مربعين**: {m('A^2 - B^2 = (A - B)(A + B)')}!",
            [
                f"**نحسب الفرق أولًا:** {m(f'{A} - {B} = {A - B}')}.",
                f"**نحسب المجموع ثانيًا:** {m(f'{A} + {B} = {A + B}')} (لاحظ أنه عدد دائري سهل!).",
                (
                    f"**نضرب الناتجين ذهنيًا:** {m(f'{A - B} \\times {A + B} = {ans}')}."
                    if D == 1 else
                    f"**نعوّض ونختصر مع المقام:** {m(f'\\frac{{({A - B}) \\times ({A + B})}}{{{D}}} = {ans}')}."
                ),
            ],
            f"متطابقة الفرق بين مربعين حوّلت العملية الطويلة إلى حساب ذهني سريع نتيجته {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g89-difference-of-squares",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Use the identity A² - B² = (A - B)(A + B) instead of squaring each number!",
            "استخدم المتطابقة A² - B² = (A - B)(A + B) بدلًا من تربيع كل عدد على حدة!",
            sol_en, sol_ar
        ))

    # 7. Alternating grouped series (1 - 2 + 3 - 4 + ... or 1 + 2 - 3 - 4 + ...) (10 variants)
    alt_cases = [
        (100, "pair_1_minus_2"),   # (1-2)+(3-4)+...+(99-100) = -50
        (99, "pair_1_minus_2"),    # -49 + 99 = 50
        (200, "pair_1_minus_2"),   # -100
        (201, "pair_1_minus_2"),   # -100 + 201 = 101
        (120, "pair_1_minus_2"),   # -60
        (80, "quad_ppmm"),         # (1+2-3-4) + ... = 20 * (-4) = -80
        (100, "quad_ppmm"),        # 25 * (-4) = -100
        (60, "quad_ppmm"),         # 15 * (-4) = -60
        (40, "quad_ppmm"),         # 10 * (-4) = -40
        (140, "quad_ppmm"),        # 35 * (-4) = -140
    ]
    for N, mode in alt_cases:
        qid = next_id()
        if mode == "pair_1_minus_2":
            ans = -(N // 2) if N % 2 == 0 else -(N // 2) + N
            check_v = sum(k if k % 2 == 1 else -k for k in range(1, N + 1))
            assert ans == check_v
            last_sign = "-" if N % 2 == 0 else "+"
            expr = f"1 - 2 + 3 - 4 + 5 - 6 + \\dots {last_sign} {N}"
            q_en = f"Find the exact value of the alternating sum: {m(expr)}."
            q_ar = f"أوجد القيمة الدقيقة للمجموع المتناوب: {m(expr)}."
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [-ans, ans + 1, ans - 1, N // 2 + 1], qid
            )
            n_pairs = N // 2
            sol_en = explain_en(
                "Group neighbors into **pairs of two**! Notice that `(1 - 2) = -1`, `(3 - 4) = -1`, `(5 - 6) = -1` — every pair has the exact same value `-1`!",
                [
                    f"Group consecutive terms two at a time: {m('(1 - 2) + (3 - 4) + (5 - 6) + \\dots')}.",
                    f"Out of {m(N)} numbers, there are {m(n_pairs)} full pairs, contributing {m(f'{n_pairs} \\times (-1) = -{n_pairs}')}.",
                    (
                        f"Since {m(N)} is even, no number is left over, so the sum is {m(ans)}."
                        if N % 2 == 0 else
                        f"Since {m(N)} is odd, the final term {m(f'+{N}')} sits after the {m(n_pairs)} pairs: {m(f'-{n_pairs} + {N} = {ans}')}!"
                    ),
                ],
                f"Pattern check on small examples: {m('1-2 = -1')}, {m('1-2+3 = 2')}, matching our pair rule!",
            )
            sol_ar = explain_ar(
                "نجمّع الحدود المتجاورة في **أزواج ثنائية**! لاحظ أن `(1 - 2) = -1`، و `(3 - 4) = -1`، و `(5 - 6) = -1` — أي أن كل زوج يعطي `-1` دائمًا!",
                [
                    f"نكتب المجموع على صورة أزواج: {m('(1 - 2) + (3 - 4) + (5 - 6) + \\dots')}.",
                    f"يوجد لدينا {m(n_pairs)} زوجًا كاملًا، مجموعها {m(f'{n_pairs} \\times (-1) = -{n_pairs}')}.",
                    (
                        f"بما أن {m(N)} زوجي فلا يبقى أي حد منفرد، ويكون الناتج النهائي {m(ans)}."
                        if N % 2 == 0 else
                        f"بما أن {m(N)} فردي يتبقى الحد الأخير {m(f'+{N}')}، فيكون المجموع {m(f'-{n_pairs} + {N} = {ans}')}."
                    ),
                ],
                f"تجميع الحدود في أزواج يختصر {m(N)} عملية إلى خطوة ذهنية واحدة نتيجتها {m(ans)}.",
            )
        else:
            # 1 + 2 - 3 - 4 + 5 + 6 - 7 - 8 + ... up to N (multiple of 4)
            n_blocks = N // 4
            ans = -4 * n_blocks
            check_v = sum(k if (k - 1) % 4 in (0, 1) else -k for k in range(1, N + 1))
            assert ans == check_v
            expr = f"1 + 2 - 3 - 4 + 5 + 6 - 7 - 8 + \\dots - {N - 1} - {N}"
            q_en = f"Evaluate the pattern sum of {m(N)} terms (where signs repeat `+ + - -`): {m(expr)}."
            q_ar = f"احسب قيمة المجموع المكون من {m(N)} حدًا (حيث تتكرر الإشارات بالنمط `+ + - -`): {m(expr)}."
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [-ans, -2 * n_blocks, 0, ans - 4], qid
            )
            sol_en = explain_en(
                "Because the sign pattern `+ + - -` repeats every **4 numbers**, group the sum into **blocks of 4**!",
                [
                    f"**Check the first block of 4:** {m('1 + 2 - 3 - 4 = -4')}.",
                    f"**Check the second block of 4:** {m('5 + 6 - 7 - 8 = -4')}. Every block `(k) + (k+1) - (k+2) - (k+3)` always equals {m('-4')}!",
                    f"**Count how many blocks of 4 fit in {m(N)} numbers:** {m(f'{N} \\div 4 = {n_blocks}')} blocks. Multiply: {m(f'{n_blocks} \\times (-4) = {ans}')}.",
                ],
                f"Every 4 terms contribute {m(-4)}, so {m(n_blocks)} blocks give {m(ans)}!",
            )
            sol_ar = explain_ar(
                "بما أن نمط الإشارات `+ + - -` يتكرر كل **4 أعداد**، نقسم السلسلة إلى **مجموعات رباعية**!",
                [
                    f"**المجموعة الأولى:** {m('1 + 2 - 3 - 4 = -4')}.",
                    f"**المجموعة الثانية:** {m('5 + 6 - 7 - 8 = -4')}. وهكذا تعطي كل مجموعة رباعية الناتج الثابت {m('-4')} دائمًا!",
                    f"**عدد المجموعات في {m(N)} حدًا:** {m(f'{N} \\div 4 = {n_blocks}')} مجموعة، إذن المجموع الكلي {m(f'{n_blocks} \\times (-4) = {ans}')}.",
                ],
                f"كل 4 حدود تساهم بـ {m(-4)}، فيكون ناتج الـ {m(n_blocks)} مجموعة هو {m(ans)}.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-alternating-grouped-sum",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Group adjacent terms according to the repeating sign cycle and compute the value of one block!",
            "جمّع الحدود المتتالية بحسب طول دورة الإشارات واحسب قيمة المجموعة الواحدة!",
            sol_en, sol_ar
        ))

    # 8. Reciprocal squaring trick: x + 1/x = k => x^2 + 1/x^2 = k^2 - 2 (or x - 1/x = k => x^2 + 1/x^2 = k^2 + 2) (10 variants)
    recip_cases = [
        (3, "+"), (4, "+"), (5, "+"), (6, "+"), (7, "+"),
        (2, "-"), (3, "-"), (4, "-"), (5, "-"), (6, "-"),
    ]
    for k, sign in recip_cases:
        qid = next_id()
        ans = k * k - 2 if sign == "+" else k * k + 2
        q_en = (
            f"If a non-zero real number {m('x')} satisfies {m(f'x {sign} \\frac{{1}}{{x}} = {k}')}, "
            f"what is the exact value of {m('x^2 + \\frac{1}{x^2}')}?"
        )
        q_ar = (
            f"إذا كان العدد الحقيقي غير الصفري {m('x')} يحقق المعادلة {m(f'x {sign} \\frac{{1}}{{x}} = {k}')}، "
            f"فما القيمة الدقيقة للمقدار {m('x^2 + \\frac{1}{x^2}')}؟"
        )
        wrong_sign = k * k + 2 if sign == "+" else k * k - 2
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [k * k, wrong_sign, k * k - 1, k * k + 1], qid
        )
        mid_term = "+ 2" if sign == "+" else "- 2"
        op_undo = f"subtract {m(2)}" if sign == "+" else f"add {m(2)}"
        op_undo_ar = f"نطرح {m(2)}" if sign == "+" else f"نضيف {m(2)}"
        sol_en = explain_en(
            "Don't try to solve for `x`! Instead, **square both sides** of the given equation—because `x × (1/x) = 1`, the middle term simplifies to a plain number (`±2`)!",
            [
                f"Square both sides of {m(f'x {sign} \\frac{{1}}{{x}} = {k}')}: {m(f'\\left(x {sign} \\frac{{1}}{{x}}\\right)^2 = {k}^2 = {k*k}')}.",
                f"Expand the left side using {m('(A \\pm B)^2 = A^2 \\pm 2AB + B^2')}: {m(f'x^2 {sign} 2(x)\\left(\\frac{{1}}{{x}}\\right) + \\frac{{1}}{{x^2}} = x^2 + \\frac{{1}}{{x^2}} {mid_term}')}.",
                f"So {m(f'x^2 + \\frac{{1}}{{x^2}} {mid_term} = {k*k}')}. Now {op_undo} on both sides: {m(f'x^2 + \\frac{{1}}{{x^2}} = {ans}')}!",
            ],
            f"Common trap: thinking {m('(A+B)^2 = A^2 + B^2')} gives {m(k*k)}, forgetting the middle term {m('2AB = 2')}!",
        )
        sol_ar = explain_ar(
            "لا تحاول إيجاد قيمة `x` نفسها! الفكرة الأذكى هي **تربيع طرفَي المعادلة المعطاة**، لأن حاصل ضرب `x` في مقلوبه `1/x` يساوي `1` فيختفي المجهول من الحد الأوسط!",
            [
                f"نربّع الطرفين: {m(f'\\left(x {sign} \\frac{{1}}{{x}}\\right)^2 = {k}^2 = {k*k}')}.",
                f"نفك التربيع باستخدام المتطابقة {m('(A \\pm B)^2 = A^2 \\pm 2AB + B^2')}: {m(f'x^2 {mid_term} + \\frac{{1}}{{x^2}} = {k*k}')}.",
                f"لعزل المقدار المطلوب {op_undo_ar} في الطرفين، فنحصل على {m(f'x^2 + \\frac{{1}}{{x^2}} = {ans}')}.",
            ],
            f"انتبه من الخطأ الشائع باختيار {m(k*k)} ونسيان الحد الأوسط {m(mid_term)} في فك التربيع!",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g89-reciprocal-square",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Square both sides of x {sign} 1/x = {k} using (A {sign} B)² = A² {sign} 2AB + B²!",
            f"ربّع طرفَي المعادلة مستخدمًا متطابقة مربع المجموع أو الفرق وتذكّر أن x × (1/x) = 1!",
            sol_en, sol_ar
        ))

    # 9. Arithmetic progression: finding a target term from two non-adjacent terms (10 variants)
    ap_cases = [
        (3, 14, 8, 34, 15),   # d=4, a1=6 -> a15 = 62
        (4, 19, 10, 49, 16),  # d=5, a1=4 -> a16 = 79
        (2, 11, 7, 26, 20),   # d=3, a1=8 -> a20 = 65
        (5, 25, 11, 61, 18),  # d=6, a1=1 -> a18 = 103
        (3, 20, 9, 44, 14),   # d=4, a1=8 -> a14 = 60
        (6, 32, 13, 67, 21),  # d=5, a1=7 -> a21 = 107
        (4, 15, 12, 39, 19),  # d=3, a1=6 -> a19 = 60
        (5, 38, 10, 23, 14),  # decreasing! d=-3 -> a14 = 11
        (2, 50, 8, 38, 16),   # d=-2 -> a16 = 22
        (3, 17, 10, 66, 13),  # d=7 -> a13 = 87
    ]
    for i1, v1, i2, v2, i_ask in ap_cases:
        qid = next_id()
        d = (v2 - v1) // (i2 - i1)
        ans = v2 + (i_ask - i2) * d
        q_en = (
            f"In an arithmetic sequence (where consecutive terms change by a constant step), "
            f"the {m(i1)}th term is {m(v1)} and the {m(i2)}th term is {m(v2)}. "
            f"What is the {m(i_ask)}th term of this sequence?"
        )
        q_ar = (
            f"في متتالية حسابية (تتغير حدودها المتتالية بمقدار ثابت)، الحد ذو الترتيب {m(i1)} يساوي {m(v1)}، "
            f"والحد ذو الترتيب {m(i2)} يساوي {m(v2)}. ما قيمة الحد ذي الترتيب {m(i_ask)} في هذه المتتالية؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + d, ans - d, ans + 2 * d, v1 + v2], qid
        )
        sol_en = explain_en(
            "You don't even need the 1st term! Moving from term `#i₁` to term `#i₂` takes `(i₂ - i₁)` equal steps, so divide the change in value by the number of steps to find 1 step!",
            [
                f"**Count the steps between term #{i1} and term #{i2}:** {m(f'{i2} - {i1} = {i2 - i1}')} steps.",
                f"**Find the constant step {m('d')}:** {m(f'd = \\frac{{{v2} - {v1}}}{{{i2 - i1}}} = \\frac{{{v2 - v1}}}{{{i2 - i1}}} = {d}')}.",
                f"**Jump from term #{i2} to term #{i_ask}** ({m(f'{i_ask} - {i2} = {i_ask - i2}')} more steps): {m(f'{v2} + ({i_ask - i2}) \\times ({d}) = {ans}')}!",
            ],
            f"Check: starting at {m(v1)} and taking {m(i_ask - i1)} steps of {m(d)} also gives {m(f'{v1} + {i_ask - i1}\\times({d}) = {ans}')}!",
        )
        sol_ar = explain_ar(
            "لا نحتاج حتى للرجوع إلى الحد الأول! الانتقال من الحد رقم `i₁` إلى الحد رقم `i₂` يستغرق `(i₂ - i₁)` خطوة متساوية!",
            [
                f"**عدد الخطوات بين الحدين المعطيين:** {m(f'{i2} - {i1} = {i2 - i1}')} خطوات.",
                f"**مقدار الخطوة الثابتة {m('d')}:** {m(f'd = \\frac{{{v2} - {v1}}}{{{i2 - i1}}} = {d}')}.",
                f"**الانتقال من الحد رقم {m(i2)} إلى الحد رقم {m(i_ask)}** (أي {m(i_ask - i2)} خطوة إضافية): {m(f'{v2} + ({i_ask - i2}) \\times ({d}) = {ans}')}.",
            ],
            f"تحقق من الحد رقم {m(i1)}: {m(f'{v1} + ({i_ask - i1}) \\times ({d}) = {ans}')} أيضًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g89-arithmetic-sequence-jump",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"From the {i1}th term to the {i2}th term is ({i2} - {i1}) equal steps. Divide ({v2} - {v1}) by ({i2} - {i1}) to find one step!",
            f"من الحد {i1} إلى الحد {i2} توجد ({i2} - {i1}) خطوة متساوية؛ اقسم فرق القيمتين على عدد الخطوات لإيجاد مقدار الخطوة!",
            sol_en, sol_ar
        ))

    # 10. Percentage interval smallest whole-number club size (9 variants) — KMC Senior/Junior percentage squeeze!
    pct_squeeze = [
        (40, 50, 5, "boys in a math circle", "الأولاد في حلقة الرياضيات"),     # 2/5=40%, 1/2=50%; strictly between: 3/7 -> n=7! Wait let's verify by brute force!
        (20, 25, 9, "left-handed players on a team", "اللاعبين العُسر في فريق"), # 2/9 = 22.2%!
        (25, 30, 7, "gold-medal winners in a group", "الفائزين بميدالية ذهبية"),  # 2/7 = 28.57%!
        (30, 33, 13, "girls in a robotics club", "الطالبات في نادي الروبوت"),     # 4/13 = 30.77%!
        (60, 65, 8, "seniors in a study group", "طلاب المرحلة العليا في مجموعة"), # 5/8 = 62.5%!
        (70, 75, 7, "members who passed Round 1", "الأعضاء المجتازين للجولة الأولى"), # 5/7 = 71.4%!
        (15, 20, 6, "red marbles in a bag", "الكرات الحمراء في كيس"),            # 1/6 = 16.67%!
        (35, 40, 8, "fiction books on a shelf", "القصص الأدبية على رف"),          # 3/8 = 37.5%!
        (80, 85, 6, "correct answers on a quiz", "الإجابات الصحيحة في اختبار"),   # 5/6 = 83.33%!
    ]
    for p_lo, p_hi, _, grp_e, grp_a in pct_squeeze:
        qid = next_id()
        # Brute force exact smallest positive integer N having an integer A with p_lo/100 < A/N < p_hi/100!
        ans = None
        witness_a = None
        for n_cand in range(1, 200):
            found = [a for a in range(1, n_cand) if p_lo * n_cand < 100 * a < p_hi * n_cand]
            if found:
                ans = n_cand
                witness_a = found[0]
                break
        assert ans is not None
        q_en = (
            f"Strictly **more than {m(f'{p_lo}\\%')}** and strictly **less than {m(f'{p_hi}\\%')}** of the {grp_e} meet a special condition. "
            f"Since the number of items/people must be a whole number, what is the **smallest possible** total number in the group?"
        )
        q_ar = (
            f"نسبة {grp_a} هي **أكبر تمامًا من {m(f'{p_lo}\\%')}** و**أقل تمامًا من {m(f'{p_hi}\\%')}**. "
            f"بما أن الأعداد يجب أن تكون صحيحة، فما **أصغر عدد كلي ممكن** للمجموعة كلها؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [max(2, ans - 1), ans + 1, ans + 2, ans + 3], qid
        )
        pct_actual = round(100 * witness_a / ans, 2)
        sol_en = explain_en(
            f"Convert percentages to fractions or test small group sizes `n = 2, 3, 4, ...` until you find the **first `n`** where some whole number `k` satisfies `{p_lo}% < (k/n) × 100% < {p_hi}%`!",
            [
                f"Write the inequality without fractions by multiplying by {m('100n')}: we need a whole number {m('k')} such that {m(f'{p_lo}n < 100k < {p_hi}n')}.",
                f"Test small values {m(f'n = 1, 2, \\dots, {ans - 1}')}: for every smaller {m('n')}, no multiple of {m(100)} falls **strictly** between {m(f'{p_lo}n')} and {m(f'{p_hi}n')}.",
                f"At {m(f'n = {ans}')}, we get {m(f'{p_lo}\\times{ans} = {p_lo*ans}')} and {m(f'{p_hi}\\times{ans} = {p_hi*ans}')}, which traps {m(f'100 \\times {witness_a} = {100*witness_a}')} strictly in between! So {m(f'n = {ans}')} (with {m(witness_a)} out of {m(ans)} {m(f'\\approx {pct_actual}\\%')}).",
            ],
            f"Notice 'strictly between' excludes exact {m(f'{p_lo}\\%')} and {m(f'{p_hi}\\%')}! At {m(f'n = {ans}')}, {m(f'\\frac{{{witness_a}}}{{{ans}}}')} lands cleanly inside the interval.",
        )
        sol_ar = explain_ar(
            f"نبحث عن أصغر عدد صحيح `n` يوجد له عدد صحيح `k` يجعل النسبة `(k / n) × 100%` واقعة **بين {p_lo}% و {p_hi}% تمامًا** (دون مساواة الطرفين)!",
            [
                f"نكتب الشرط بدون كسور بضرب المتباينة في {m('100n')}: نريد عددًا صحيحًا {m('k')} يحقق {m(f'{p_lo}n < 100k < {p_hi}n')}.",
                f"نجرّب القيم الصغيرة {m(f'n = 1, 2, \\dots, {ans - 1}')}: نلاحظ أنه لا يوجد أي مضاعف للعدد {m(100)} يقع بين {m(f'{p_lo}n')} و {m(f'{p_hi}n')} لأيٍّ منها.",
                f"عند {m(f'n = {ans}')} تصبح الفترة من {m(p_lo * ans)} إلى {m(p_hi * ans)}، ويقع بداخلها العدد {m(100 * witness_a)} (أي {m(f'k = {witness_a}')})؛ إذن أصغر عدد كلي ممكن هو {m(ans)}.",
            ],
            f"تحقق: الكسر {m(f'\\frac{{{witness_a}}}{{{ans}}}')} يعادل تقريبًا {m(f'{pct_actual}\\%')} وهو يقع فعلًا بين {m(f'{p_lo}\\%')} و {m(f'{p_hi}\\%')}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Hard", "g89-percentage-squeeze",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Rewrite the condition as {p_lo}n < 100k < {p_hi}n and test n = 2, 3, 4, ... until a multiple of 100 fits strictly inside!",
            f"اكتب المتباينة بالصورة {p_lo}n < 100k < {p_hi}n وجرّب قيم n الصغيرة تصاعديًا حتى تجد أول فترة تحوي مضاعفًا للعدد 100!",
            sol_en, sol_ar
        ))

    # 11. Linear fractional equations (x - a)/(x - b) = c/d (8 variants)
    frac_eq_cases = [
        (2, 8, 2, 5, 12),   # Let's compute exact ans from cross-multiplication!
        (1, 7, 1, 3, 10),
        (3, 11, 3, 5, 15),
        (-2, 6, 3, 1, 10),
        (4, 10, 1, 4, 2),
        (-1, 5, 2, 5, 3),
        (5, 13, 1, 3, 9),
        (-3, 9, 5, 2, 17),
    ]
    # Re-parameterize cleanly by choosing ans, a, b, and reduced fraction (ans-a)/(ans-b) = c/d!
    clean_frac_eq = [
        (12, 4, 2, "x - 4", "x - 2"),     # 8/10 = 4/5
        (10, 2, 6, "x - 2", "x - 6"),     # 8/4 = 2/1 -> let's use non-integer c/d: (10-1)/(10-4) = 9/6 = 3/2!
        (9, 1, 5, "x - 1", "x - 5"),      # 8/4 -> (9-3)/(9+1)=6/10=3/5!
        (7, 1, 10, "x - 1", "x - 10"),
        (14, 2, 8, "x - 2", "x - 8"),
        (11, 3, -1, "x - 3", "x + 1"),
        (15, 5, 0, "x - 5", "x + 5"),
        (8, -2, 3, "x + 2", "x - 3"),
    ]
    # Let's pick 8 where c/d is a clean non-integer reduced fraction with c != d!
    exact_feq = [
        (12, -4, -2),   # (x-4)/(x-2) at x=12: 8/10 = 4/5
        (10, -1, -4),   # (x-1)/(x-4) at x=10: 9/6 = 3/2
        (9, -3, 1),     # (x-3)/(x+1) at x=9: 6/10 = 3/5
        (13, -1, -5),   # (x-1)/(x-5) at x=13: 12/8 = 3/2
        (8, 2, 7),      # (x+2)/(x+7) at x=8: 10/15 = 2/3
        (14, -2, 4),    # (x-2)/(x+4) at x=14: 12/18 = 2/3
        (11, 4, -1),    # (x+4)/(x-1) at x=11: 15/10 = 3/2
        (16, -4, 2),    # (x-4)/(x+2) at x=16: 12/18 -> wait same 2/3; let's use (15, -3, 5) -> 12/20 = 3/5!
    ]
    exact_feq[7] = (15, -3, 1)  # (x-3)/(x+1) at 15 -> 12/16 = 3/4!
    for ans, s1, s2 in exact_feq:
        qid = next_id()
        fr = Fraction(ans + s1, ans + s2)
        c_n, d_n = fr.numerator, fr.denominator
        assert c_n != d_n and d_n > 1
        t1 = f"x - {abs(s1)}" if s1 < 0 else f"x + {s1}"
        t2 = f"x - {abs(s2)}" if s2 < 0 else f"x + {s2}"
        q_en = f"Solve for {m('x')}: {m(f'\\frac{{{t1}}}{{{t2}}} = \\frac{{{c_n}}}{{{d_n}}}')}."
        q_ar = f"أوجد قيمة {m('x')} التي تحقق المعادلة الكسرية: {m(f'\\frac{{{t1}}}{{{t2}}} = \\frac{{{c_n}}}{{{d_n}}}')}."
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 2, ans - 2, ans + 4, abs(s1) + abs(s2) + 1], qid
        )
        sol_en = explain_en(
            "When two fractions are equal (`A/B = C/D`), **cross-multiply** (`D × A = C × B`) to clear all denominators in one step!",
            [
                f"**Cross-multiply:** {m(f'{d_n}({t1}) = {c_n}({t2})')}.",
                f"**Expand the brackets carefully** (multiply BOTH terms inside each bracket!): {m(f'{d_n}x + ({d_n*s1}) = {c_n}x + ({c_n*s2})')}.",
                f"**Collect `x` on one side and numbers on the other:** {m(f'{abs(d_n - c_n)}x = {abs(c_n*s2 - d_n*s1)}')}, which gives {m(f'x = {ans}')}!",
            ],
            f"Substitute {m(f'x = {ans}')} back in: {m(f'\\frac{{{ans + s1}}}{{{ans + s2}}} = \\frac{{{c_n}}}{{{d_n}}}')} (and denominator {m(f'{ans + s2} \\ne 0')})!",
        )
        sol_ar = explain_ar(
            "عند تساوي كسرين (`A/B = C/D`) نستخدم **الضرب التبادلي (المقص)** (`D × A = C × B`) للتخلص من المقامات فورًا!",
            [
                f"**نضرب تبادليًا:** {m(f'{d_n}({t1}) = {c_n}({t2})')}.",
                f"**نفك الأقواس بدقة** (بضرب العدد الخارجي في كلا الحدّين داخل القوس): {m(f'{d_n}x + ({d_n*s1}) = {c_n}x + ({c_n*s2})')}.",
                f"**نجمع حدود `x` في طرف والأعداد في الطرف الآخر:** {m(f'{abs(d_n - c_n)}x = {abs(c_n*s2 - d_n*s1)}')}، ومنها {m(f'x = {ans}')}.",
            ],
            f"تحقق بالتعويض عن {m(f'x = {ans}')}: نحصل على {m(f'\\frac{{{ans + s1}}}{{{ans + s2}}} = \\frac{{{c_n}}}{{{d_n}}}')} تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g89-fractional-linear-eq",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Cross-multiply to get {d_n}({t1}) = {c_n}({t2}), expand both brackets, and solve for x!",
            f"اضرب ضربًا تبادليًا لتحصل على {d_n}({t1}) = {c_n}({t2})، ثم فك القوسين وأوجد x!",
            sol_en, sol_ar
        ))

    # 12. Consecutive odd/even/integer sums — finding largest or smallest (8 variants)
    consec_cases = [
        (5, 1, 135, "largest", "أكبر"),     # middle = 27 -> 25,26,27,28,29 -> 29
        (7, 1, 140, "smallest", "أصغر"),    # middle = 20 -> 17..23 -> 17
        (5, 2, 120, "largest", "أكبر"),     # 5 consecutive even: mid=24 -> 20,22,24,26,28 -> 28
        (5, 2, 95, "smallest", "أصغر"),     # 5 consecutive odd: mid=19 -> 15,17,19,21,23 -> 15
        (9, 1, 180, "largest", "أكبر"),     # mid=20 -> 16..24 -> 24
        (7, 2, 154, "largest", "أكبر"),     # 7 consecutive even: mid=22 -> 16..28 -> 28
        (6, 1, 123, "largest", "أكبر"),     # 6 consecutive integers: avg=20.5 -> 18,19,20,21,22,23 -> 23
        (4, 2, 100, "smallest", "أصغر"),    # 4 consecutive odd: avg=25 -> 22,24,26,28 even! Let's specify even!
    ]
    for k_cnt, step, tot_s, extr_e, extr_a in consec_cases:
        qid = next_id()
        # Generate sequence centered around tot_s / k_cnt
        # first + last = 2 * tot_s / k_cnt, last - first = (k_cnt - 1) * step
        assert (2 * tot_s) % k_cnt == 0
        sum_ends = (2 * tot_s) // k_cnt
        span = (k_cnt - 1) * step
        first = (sum_ends - span) // 2
        seq = [first + i * step for i in range(k_cnt)]
        assert sum(seq) == tot_s
        ans = seq[-1] if extr_e == "largest" else seq[0]
        if step == 1:
            kind_e, kind_a = "consecutive integers", "أعداد صحيحة متتالية"
        elif first % 2 == 0:
            kind_e, kind_a = "consecutive **even** integers", "أعداد صحيحة **زوجية** متتالية"
        else:
            kind_e, kind_a = "consecutive **odd** integers", "أعداد صحيحة **فردية** متتالية"
        q_en = f"The sum of {m(k_cnt)} {kind_e} is {m(tot_s)}. What is the **{extr_e}** of these {m(k_cnt)} integers?"
        q_ar = f"مجموع {m(k_cnt)} {kind_a} يساوي {m(tot_s)}. ما **{extr_a}** هذه الأعداد الـ {m(k_cnt)}؟"
        mid_approx = tot_s // k_cnt
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [mid_approx if mid_approx != ans else ans + step, seq[0] if extr_e == "largest" else seq[-1], ans + step, ans - step], qid
        )
        seq_str = ", ".join(map(str, seq))
        sol_en = explain_en(
            "Middle-Number Shortcut: In any evenly-spaced list of numbers, the **average (`Sum ÷ Count`) sits right in the exact center** of the list!",
            [
                f"**Divide the sum by {m(k_cnt)} to find the center:** {m(f'{tot_s} \\div {k_cnt} = {tot_s / k_cnt:g}')}.",
                f"**Build the {m(k_cnt)} numbers symmetrically around {m(f'{tot_s / k_cnt:g}')}** (stepping by {m(step)}): {m(seq_str)}.",
                f"Pick the **{extr_e}** number in the list: {m(ans)}!",
            ],
            f"Check the sum: {m(' + '.join(map(str, seq)) + f' = {tot_s}')}!",
        )
        sol_ar = explain_ar(
            "حيلة العدد الأوسط السريعة: في أي أعداد متتالية منتظمة، **المتوسط الحسابي (`المجموع ÷ العدد`) يقع في المنتصف تمامًا**!",
            [
                f"**نقسم المجموع على {m(k_cnt)} لمعرفة المركز:** {m(f'{tot_s} \\div {k_cnt} = {tot_s / k_cnt:g}')}.",
                f"**نرتب الـ {m(k_cnt)} أعداد بتماثل حول {m(f'{tot_s / k_cnt:g}')}** (بفارق {m(step)} بين كل عدد والذي يليه): {m(seq_str)}.",
                f"نختار **{extr_a}** عدد في القائمة وهو {m(ans)}!",
            ],
            f"تحقق بالجمع: {m(' + '.join(map(str, seq)) + f' = {tot_s}')} تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g89-consecutive-sum-center",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Divide {tot_s} by {k_cnt} first — that gives you the exact middle of the {k_cnt} numbers!",
            f"اقسم {tot_s} على {k_cnt} أولًا؛ سيعطيك ذلك منتصف الأعداد مباشرة!",
            sol_en, sol_ar
        ))

    assert len(items) == 115, f"Expected 115 items, got {len(items)}"
    return items


if __name__ == "__main__":
    qs = generate_t2_algebra()
    print(f"Generated {len(qs)} Track 2 Algebra questions cleanly.")

