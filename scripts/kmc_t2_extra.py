"""KAUST Mathematics Competition (KMC) — Track 2: Grades 8-9
Extra Bank Expansion: 300 programmatically verified, beginner-friendly bilingual questions
across 18 blueprints (50 questions per lesson group, Lessons 2.1 through 2.6).
"""
from fractions import Fraction
import itertools
import math
import re

from kmc_common import (
    explain_ar,
    explain_en,
    fmt_val,
    m,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams_extra import (
    svg_algebra_flow,
    svg_area_identity_square,
    svg_binary_bulbs,
    svg_digit_cards,
    svg_factor_tree,
    svg_isosceles_trapezoid,
    svg_motion_timeline,
    svg_number_line_sign_chart,
    svg_pan_balance_coins,
    svg_pie_chart,
    svg_pipe_tank,
    svg_score_table,
    svg_statement_cards,
    svg_street_grid,
    svg_telescoping_chain,
    svg_thales_circle,
    svg_two_jars,
    svg_venn_3,
)

LEVEL = "Track 2: Grades 8-9"

_SUP_MAP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")


def _sup(v) -> str:
    return str(v).translate(_SUP_MAP)


def _prime_factors(n: int) -> list[tuple[int, int]]:
    out = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            c = 0
            while x % d == 0:
                x //= d
                c += 1
            out.append((d, c))
        d += 1
    if x > 1:
        out.append((x, 1))
    return out


def _fmt_pf(pf: list[tuple[int, int]]) -> str:
    return " \\times ".join(f"{p}^{{{e}}}" if e >= 1 else str(p) for p, e in pf)


def _digital_root_exact(val: int) -> int:
    assert val > 0
    x = val
    while x >= 10:
        x = sum(int(ch) for ch in str(x))
    return x


def _gen_lesson_2_1() -> list[dict]:
    out: list[dict] = []
    topic = "Number Theory"

    # ------------------------------------------------------------------
    # 1. kmc_g89_factor_tree_square_cube (17 Qs, svg_factor_tree)
    # ------------------------------------------------------------------
    ft_cases = [
        (72, 8, 9, 3, 3, "mul_sq", "Easy"),
        (108, 4, 27, 3, 9, "mul_sq", "Easy"),
        (150, 6, 25, 5, 5, "mul_sq", "Easy"),
        (200, 8, 25, 5, 5, "div_sq", "Easy"),
        (300, 3, 100, 10, 10, "div_sq", "Easy"),
        (240, 16, 15, 3, 5, "mul_sq", "Medium"),
        (252, 7, 36, 6, 6, "mul_sq", "Medium"),
        (360, 10, 36, 6, 6, "mul_sq", "Medium"),
        (504, 8, 63, 7, 9, "mul_sq", "Medium"),
        (245, 5, 49, 7, 7, "div_sq", "Medium"),
        (540, 15, 36, 6, 6, "div_sq", "Medium"),
        (700, 7, 100, 10, 10, "div_sq", "Medium"),
        (36, 4, 9, 3, 3, "mul_cube", "Medium"),
        (100, 4, 25, 5, 5, "mul_cube", "Hard"),
        (75, 3, 25, 5, 5, "mul_cube", "Hard"),
        (144, 16, 9, 3, 3, "mul_cube", "Hard"),
        (196, 4, 49, 7, 7, "mul_cube", "Hard"),
    ]
    for i, (N, lv, rv, rlv, rrv, mode, diff) in enumerate(ft_cases, 1):
        assert lv * rv == N and rlv * rrv == rv
        pf = _prime_factors(N)
        pf_str = _fmt_pf(pf)
        svg = svg_factor_tree(str(N), str(lv), str(rv), str(rlv), str(rrv))

        if mode == "mul_sq":
            ans = math.prod(p for p, e in pf if e % 2 == 1)
            brute = next(k for k in range(1, N + 1) if math.isqrt(N * k) ** 2 == N * k)
            assert ans == brute
            root_sq = math.isqrt(N * ans)
            odd_primes = [str(p) for p, e in pf if e % 2 == 1]
            odd_str = " \\times ".join(odd_primes)
            q_en = (
                f"Using the factor tree of {m(N)} started in the diagram, find the **smallest positive integer** "
                f"{m('k')} such that the product {m(f'{N} \\times k')} is a **perfect square**."
            )
            q_ar = (
                f"بالاستعانة بشجرة عوامل العدد {m(N)} الموضّحة في الشكل، أوجد **أصغر عدد صحيح موجب** "
                f"{m('k')} يجعل حاصل الضرب {m(f'{N} \\times k')} **مربعاً كاملاً**."
            )
            h_en = f"Write the full prime factorization of {N}. In a perfect square, every prime exponent must be EVEN!"
            h_ar = f"اكتب التحليل الأولي الكامل للعدد {N}. في المربع الكامل يجب أن يكون أسّ كل عامل أولي عدداً زوجياً!"
            s_en = explain_en(
                "A positive integer is a **perfect square** if and only if every prime in its prime factorization has an **even** exponent.",
                [
                    f"Complete the prime factorization from the tree: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"Check the parity of each exponent: the prime(s) with **odd** exponents need one extra copy to become even: {m(f'k = {odd_str} = {ans}')}.",
                    f"Multiply to verify: {m(f'{N} \\times {ans} = {N * ans} = {root_sq}^2')}.",
                ],
                f"Direct check: {m(f'{root_sq}^2 = {N * ans}')}, and no smaller positive integer fixes all odd prime exponents!",
            )
            s_ar = explain_ar(
                "يكون العدد الصحيح الموجب **مربعاً كاملاً** إذا وفقط إذا كان أسّ كل عامل أولي في تحليله **عدداً زوجياً**.",
                [
                    f"نكمل التحليل إلى العوامل الأولية انطلاقاً من الشجرة: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"نبحث عن العوامل الأولية ذات الأسس **الفردية** ونضرب في نسخة واحدة من كلٍّ منها ليصبح الأس زوجياً: {m(f'k = {odd_str} = {ans}')}.",
                    f"نتحقق بالضرب: {m(f'{N} \\times {ans} = {N * ans} = {root_sq}^2')}.",
                ],
                f"تحقق سريع: {m(f'{root_sq}^2 = {N * ans}')}، ولا يوجد عدد أصغر يجعل جميع الأسس زوجية!",
            )
            distractors = [ans * 2, ans * 3, max(1, ans - 1), lv, rlv * rrv]
        elif mode == "div_sq":
            ans = math.prod(p for p, e in pf if e % 2 == 1)
            brute = next(k for k in range(1, N + 1) if N % k == 0 and math.isqrt(N // k) ** 2 == N // k)
            assert ans == brute
            root_sq = math.isqrt(N // ans)
            odd_primes = [str(p) for p, e in pf if e % 2 == 1]
            odd_str = " \\times ".join(odd_primes)
            q_en = (
                f"A factor tree for {m(N)} is partially shown. What is the **smallest positive integer** {m('k')} "
                f"by which we can divide {m(N)} so that the quotient {m(f'{N} \\div k')} is an integer **perfect square**?"
            )
            q_ar = (
                f"يوضّح الشكل بداية شجرة عوامل العدد {m(N)}. ما **أصغر عدد صحيح موجب** {m('k')} "
                f"إذا قسمنا {m(N)} عليه كان ناتج القسمة {m(f'{N} \\div k')} عدداً صحيحاً **مربعاً كاملاً**؟"
            )
            h_en = f"Prime-factorize {N} completely. Dividing out one copy of each prime that has an odd exponent leaves all even exponents!"
            h_ar = f"حلّل {N} إلى عوامله الأولية كاملةً. قسمة العدد على كل عامل أولي ذي أس فردي تجعل جميع الأسس المتبقية زوجية!"
            s_en = explain_en(
                "For the quotient \\( N \\div k \\) to be a **perfect square** with \\( k \\) as small as possible, we divide out only the primes that have **odd** exponents.",
                [
                    f"Complete the prime factorization: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"To make every remaining exponent even with minimal division, divide by one copy of each odd-exponent prime: {m(f'k = {odd_str} = {ans}')}.",
                    f"Check the quotient: {m(f'{N} \\div {ans} = {N // ans} = {root_sq}^2')}.",
                ],
                f"Check: {m(f'{N} \\div {ans} = {N // ans} = {root_sq}^2')} is the largest square divisor of {m(N)}!",
            )
            s_ar = explain_ar(
                "لكي يصبح خارج القسمة \\( N \\div k \\) **مربعاً كاملاً** بأصغر قيمة ممكنة لـ \\( k \\)، نقسم فقط على العوامل الأولية ذات الأسس **الفردية**.",
                [
                    f"نكتب التحليل الأولي الكامل: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"لتصبح الأسس المتبقية زوجية بأقل قسمة ممكنة، نأخذ {m(f'k = {odd_str} = {ans}')}.",
                    f"نحسب ناتج القسمة: {m(f'{N} \\div {ans} = {N // ans} = {root_sq}^2')}.",
                ],
                f"تحقق: {m(f'{N} \\div {ans} = {N // ans} = {root_sq}^2')} مربع كامل ولا توجد قيمة موجبة أصغر لـ {m('k')}!",
            )
            distractors = [ans * 2, ans * 4, root_sq, max(1, ans - 1), lv]
        else:
            ans = math.prod(p ** ((3 - (e % 3)) % 3) for p, e in pf)
            brute = next(k for k in range(1, N * N + 1) if round((N * k) ** (1 / 3)) ** 3 == N * k)
            assert ans == brute
            root_cb = round((N * ans) ** (1 / 3))
            assert root_cb ** 3 == N * ans
            need_terms = [f"{p}^{{{(3 - (e % 3)) % 3}}}" for p, e in pf if e % 3 != 0]
            need_str = " \\times ".join(need_terms)
            q_en = (
                f"Look at the factor tree started for {m(N)}. What is the **smallest positive integer** {m('k')} "
                f"such that {m(f'{N} \\times k')} is a **perfect cube**?"
            )
            q_ar = (
                f"تأمّل شجرة العوامل المبدوءة للعدد {m(N)}. ما **أصغر عدد صحيح موجب** {m('k')} "
                f"يجعل حاصل الضرب {m(f'{N} \\times k')} **مكعباً كاملاً**؟"
            )
            h_en = f"In a perfect cube, every prime exponent must be a MULTIPLE OF 3 (such as 3 or 6)!"
            h_ar = f"في المكعب الكامل، يجب أن يكون أسّ كل عامل أولي من مضاعفات العدد 3 (مثل 3 أو 6)!"
            s_en = explain_en(
                "A positive integer is a **perfect cube** if and only if every prime exponent in its prime factorization is a **multiple of 3** (3, 6, 9, ...).",
                [
                    f"Write the prime factorization of {m(N)}: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"Raise each exponent up to the next multiple of {m(3)}: we must multiply by {m(f'k = {need_str} = {ans}')}.",
                    f"Verify the cube: {m(f'{N} \\times {ans} = {N * ans} = {root_cb}^3')}.",
                ],
                f"Check: {m(f'{root_cb} \\times {root_cb} \\times {root_cb} = {N * ans}')}!",
            )
            s_ar = explain_ar(
                "يكون العدد الصحيح الموجب **مكعباً كاملاً** إذا وفقط إذا كان أسّ كل عامل أولي في تحليله **من مضاعفات 3** (مثل 3 أو 6).",
                [
                    f"نكتب التحليل الأولي للعدد {m(N)}: {m(f'{N} = {lv} \\times {rv} = {pf_str}')}.",
                    f"نكمّل أسّ كل عامل أولي إلى أقرب مضاعف للعدد {m(3)}، فنضرب في {m(f'k = {need_str} = {ans}')}.",
                    f"نتحقق من المكعب الناتج: {m(f'{N} \\times {ans} = {N * ans} = {root_cb}^3')}.",
                ],
                f"تحقق: {m(f'{root_cb}^3 = {N * ans}')} مكعب كامل صحيح!",
            )
            sqft_trap = math.prod(p for p, e in pf if e % 2 == 1)
            distractors = [sqft_trap, ans // 2 if ans % 2 == 0 else ans + 3, ans * 2, root_cb, lv * rlv]

        qid = f"KMC-T2-EX-21A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_factor_tree_square_cube",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 2. kmc_g89_venn_three_sets (17 Qs, svg_venn_3)
    # ------------------------------------------------------------------
    # (oa, ob, oc, oab, obc, oac, abc, c1_en, c2_en, c3_en, c1_ar, c2_ar, c3_ar, mode, diff)
    venn_cases = [
        (8, 7, 6, 3, 2, 4, 2, "Math", "Coding", "Robotics", "الرياضيات", "البرمجة", "الروبوتات", "union", "Easy"),
        (10, 9, 8, 4, 3, 2, 3, "Chess", "Science", "Debate", "الشطرنج", "العلوم", "المناظرة", "union", "Easy"),
        (12, 10, 9, 5, 4, 3, 4, "Physics", "Astronomy", "Math", "الفيزياء", "الفلك", "الرياضيات", "union", "Easy"),
        (9, 8, 7, 3, 4, 2, 3, "Art", "Music", "Drama", "الفنون", "الموسيقى", "المسرح", "only_one", "Easy"),
        (11, 9, 10, 4, 2, 3, 2, "Swimming", "Running", "Cycling", "السباحة", "الجري", "الدراجات", "only_one", "Easy"),
        (14, 11, 13, 6, 5, 4, 5, "Robotics", "AI", "Electronics", "الروبوتات", "الذكاء الاصطناعي", "الإلكترونيات", "union", "Medium"),
        (15, 13, 12, 5, 6, 4, 3, "Biology", "Chemistry", "Geology", "الأحياء", "الكيمياء", "الجيولوجيا", "union", "Medium"),
        (16, 14, 15, 7, 5, 6, 4, "Arabic", "English", "French", "العربية", "الإنجليزية", "الفرنسية", "union", "Medium"),
        (13, 12, 10, 5, 3, 4, 4, "Math", "Chess", "Puzzle", "الرياضيات", "الشطرنج", "الألغاز", "only_one", "Medium"),
        (15, 11, 14, 6, 4, 5, 3, "Coding", "Design", "Media", "البرمجة", "التصميم", "الإعلام", "only_one", "Medium"),
        (17, 14, 12, 5, 6, 3, 5, "Tennis", "Football", "Volleyball", "التنس", "كرة القدم", "الكرة الطائرة", "only_one", "Medium"),
        (10, 12, 9, 4, 5, 3, 4, "Math", "Physics", "Coding", "الرياضيات", "الفيزياء", "البرمجة", "find_triple", "Medium"),
        (14, 11, 13, 5, 4, 6, 6, "Science", "Robotics", "Chess", "العلوم", "الروبوتات", "الشطرنج", "find_triple", "Medium"),
        (18, 16, 15, 7, 6, 5, 6, "Logic", "Algebra", "Geometry", "المنطق", "الجبر", "الهندسة", "only_one", "Hard"),
        (16, 15, 14, 6, 7, 5, 5, "Astronomy", "Robotics", "Debate", "الفلك", "الروبوتات", "المناظرة", "find_triple", "Hard"),
        (19, 17, 13, 8, 5, 6, 7, "Chemistry", "Physics", "Biology", "الكيمياء", "الفيزياء", "الأحياء", "find_triple", "Hard"),
        (20, 18, 16, 9, 7, 8, 8, "Coding", "Math", "Astronomy", "البرمجة", "الرياضيات", "الفلك", "find_triple", "Hard"),
    ]
    for i, (oa, ob, oc, oab, obc, oac, abc, c1e, c2e, c3e, c1a, c2a, c3a, mode, diff) in enumerate(venn_cases, 1):
        assert min(oa, ob, oc, oab, obc, oac, abc) >= 1
        nA = oa + oab + oac + abc
        nB = ob + oab + obc + abc
        nC = oc + oac + obc + abc
        pAB = oab + abc
        pBC = obc + abc
        pAC = oac + abc
        union_val = oa + ob + oc + oab + obc + oac + abc
        assert union_val == nA + nB + nC - (pAB + pBC + pAC) + abc
        only_one_val = oa + ob + oc

        if mode == "union":
            ans = union_val
            svg_en = svg_venn_3(f"{c1e} ({nA})", f"{c2e} ({nB})", f"{c3e} ({nC})", {"abc": str(abc)})
            svg_ar = svg_venn_3(f"{c1a} ({nA})", f"{c2a} ({nB})", f"{c3a} ({nC})", {"abc": str(abc)})
            q_en = (
                f"In a KAUST Olympiad camp, students join three clubs: **{c1e}** ({m(nA)} students), **{c2e}** ({m(nB)} students), "
                f"and **{c3e}** ({m(nC)} students). Exactly {m(pAB)} are in both {c1e} and {c2e}, {m(pBC)} are in both {c2e} and {c3e}, "
                f"{m(pAC)} are in both {c1e} and {c3e}, and {m(abc)} are in **all three** clubs. "
                f"How many students belong to **at least one** of the three clubs?"
            )
            q_ar = (
                f"في معسكر أولمبياد كاوست، التحق الطلاب بثلاثة أندية: **{c1a}** ({m(nA)} طالباً)، و**{c2a}** ({m(nB)} طالباً)، "
                f"و**{c3a}** ({m(nC)} طالباً). يشترك {m(pAB)} في {c1a} و{c2a} معاً، و{m(pBC)} في {c2a} و{c3a} معاً، "
                f"و{m(pAC)} في {c1a} و{c3a} معاً، بينما يشترك {m(abc)} في **الأندية الثلاثة جميعها**. "
                f"كم طالباً ينتمي إلى **نادٍ واحد على الأقل** من هذه الأندية الثلاثة؟"
            )
            h_en = "Use 3-set Inclusion–Exclusion: add the 3 single-club totals, subtract the 3 pairwise overlaps, then ADD back the triple overlap!"
            h_ar = "استخدم مبدأ التضمين والإقصاء لثلاث مجموعات: اجمع أعداد الأندية الثلاثة، واطرح التقاطعات الثنائية الثلاثة، ثم أضف تقاطع الثلاثة معاً!"
            sum1 = nA + nB + nC
            sum2 = pAB + pBC + pAC
            s_en = explain_en(
                "By the **3-Set Inclusion–Exclusion Principle**, subtracting the three pairwise overlaps removes the center region three times, so we add the triple overlap back once: "
                f"{m('|A \\cup B \\cup C| = (|A|+|B|+|C|) - (|A\\cap B|+|B\\cap C|+|A\\cap C|) + |A\\cap B\\cap C|')}.",
                [
                    f"Add the three club sizes: {m(f'{nA} + {nB} + {nC} = {sum1}')}.",
                    f"Add the three pairwise overlaps: {m(f'{pAB} + {pBC} + {pAC} = {sum2}')}.",
                    f"Apply the formula: {m(f'{sum1} - {sum2} + {abc} = {ans}')}.",
                ],
                f"Trap check: forgetting {m(f'+{abc}')} gives {m(sum1 - sum2)}, and subtracting {m(abc)} instead gives {m(sum1 - sum2 - abc)}!",
            )
            s_ar = explain_ar(
                "حسب **مبدأ التضمين والإقصاء لثلاث مجموعات**، عند طرح التقاطعات الثنائية الثلاثة نكون قد حذفنا منطقة الوسط ثلاث مرات، لذا نعيد إضافة تقاطع الثلاثة مرة واحدة.",
                [
                    f"مجموع أعداد الأندية الثلاثة: {m(f'{nA} + {nB} + {nC} = {sum1}')}.",
                    f"مجموع التقاطعات الثنائية الثلاثة: {m(f'{pAB} + {pBC} + {pAC} = {sum2}')}.",
                    f"نطبّق القانون: {m(f'{sum1} - {sum2} + {abc} = {ans}')} طالباً.",
                ],
                f"انتبه للفخ الشائع: نسيان إضافة {m(abc)} يعطي {m(sum1 - sum2)} بدلاً من الإجابة الصحيحة {m(ans)}!",
            )
            distractors = [sum1 - sum2, sum1 - sum2 - abc, ans + abc, only_one_val]
        elif mode == "only_one":
            ans = only_one_val
            svg_en = svg_venn_3(f"{c1e} ({nA})", f"{c2e} ({nB})", f"{c3e} ({nC})", {"a": "?", "b": "?", "c": "?", "abc": str(abc)})
            svg_ar = svg_venn_3(f"{c1a} ({nA})", f"{c2a} ({nB})", f"{c3a} ({nC})", {"a": "؟", "b": "؟", "c": "؟", "abc": str(abc)})
            q_en = (
                f"Three Olympiad clubs have **{c1e}** = {m(nA)}, **{c2e}** = {m(nB)}, and **{c3e}** = {m(nC)} members. "
                f"There are {m(pAB)} students in both {c1e} and {c2e}, {m(pBC)} in both {c2e} and {c3e}, {m(pAC)} in both {c1e} and {c3e}, "
                f"and {m(abc)} in **all three** clubs. How many students belong to **exactly one** club?"
            )
            q_ar = (
                f"ثلاثة أندية أولمبية عدد أعضائها: **{c1a}** = {m(nA)}، و**{c2a}** = {m(nB)}، و**{c3a}** = {m(nC)}. "
                f"يشترك {m(pAB)} في {c1a} و{c2a} معاً، و{m(pBC)} في {c2a} و{c3a} معاً، و{m(pAC)} في {c1a} و{c3a} معاً، "
                f"و{m(abc)} في **الأندية الثلاثة جميعها**. كم طالباً ينتمي إلى **نادٍ واحد فقط**؟"
            )
            h_en = "Work from the center outward! First subtract the triple overlap from each pairwise overlap to get the 'exactly two clubs' petals."
            h_ar = "ابدأ من مركز الشكل واتجه للخارج! اطرح تقاطع الثلاثة أولاً من كل تقاطع ثنائي لإيجاد مناطق «ناديين فقط»."
            s_en = explain_en(
                "Always fill a 3-set Venn diagram **from the innermost region outward**!",
                [
                    f"Subtract the center ({m(abc)}) from each pairwise overlap to find the 'exactly two' regions: "
                    f"{m(f'{pAB}-{abc}={oab}')}, {m(f'{pBC}-{abc}={obc}')}, and {m(f'{pAC}-{abc}={oac}')}.",
                    f"Find each 'only one' region: only {c1e} = {m(f'{nA} - ({oab}+{oac}+{abc}) = {oa}')}; "
                    f"only {c2e} = {m(f'{nB} - ({oab}+{obc}+{abc}) = {ob}')}; only {c3e} = {m(f'{nC} - ({oac}+{obc}+{abc}) = {oc}')}.",
                    f"Sum the three outer regions: {m(f'{oa} + {ob} + {oc} = {ans}')}.",
                ],
                f"Check: adding all 7 disjoint regions gives {m(f'{ans} + ({oab}+{obc}+{oac}) + {abc} = {union_val}')}, matching the union!",
            )
            s_ar = explain_ar(
                "أفضل طريقة لحل مخطط فن الثلاثي هي البدء **من المنطقة الوسطى ثم الاتجاه نحو الخارج**!",
                [
                    f"نطرح المركز ({m(abc)}) من كل تقاطع ثنائي لنحصل على مناطق «ناديين فقط»: "
                    f"{m(f'{pAB}-{abc}={oab}')}، و{m(f'{pBC}-{abc}={obc}')}، و{m(f'{pAC}-{abc}={oac}')}.",
                    f"نحسب المنتمين لنادٍ واحد فقط: {c1a} فقط = {m(oa)}، و{c2a} فقط = {m(ob)}، و{c3a} فقط = {m(oc)}.",
                    f"نجمع المناطق الثلاث الخارجية: {m(f'{oa} + {ob} + {oc} = {ans}')} طالباً.",
                ],
                f"تحقق: مجموع المناطق السبع المنفصلة يساوي {m(f'{ans} + {oab+obc+oac} + {abc} = {union_val}')}!",
            )
            distractors = [union_val, ans + abc, max(1, ans - abc), ans + oab]
        else:
            ans = abc
            svg_en = svg_venn_3(f"{c1e} ({nA})", f"{c2e} ({nB})", f"{c3e} ({nC})", {"abc": "x"})
            svg_ar = svg_venn_3(f"{c1a} ({nA})", f"{c2a} ({nB})", f"{c3a} ({nC})", {"abc": "x"})
            sum1 = nA + nB + nC
            sum2 = pAB + pBC + pAC
            base_diff = sum1 - sum2
            q_en = (
                f"A total of {m(union_val)} students participate in at least one of three clubs: **{c1e}** ({m(nA)}), "
                f"**{c2e}** ({m(nB)}), and **{c3e}** ({m(nC)}). Given that {m(pAB)} are in both {c1e} and {c2e}, "
                f"{m(pBC)} are in both {c2e} and {c3e}, and {m(pAC)} are in both {c1e} and {c3e}, find the number of students "
                f"{m('x')} who belong to **all three** clubs."
            )
            q_ar = (
                f"يشارك {m(union_val)} طالباً في نادٍ واحد على الأقل من ثلاثة أندية: **{c1a}** ({m(nA)})، و**{c2a}** ({m(nB)})، "
                f"و**{c3a}** ({m(nC)}). إذا كان {m(pAB)} في {c1a} و{c2a} معاً، و{m(pBC)} في {c2a} و{c3a} معاً، "
                f"و{m(pAC)} في {c1a} و{c3a} معاً، فما عدد الطلاب {m('x')} المشتركين في **الأندية الثلاثة جميعها**؟"
            )
            h_en = "Plug all known totals into |A ∪ B ∪ C| = (|A|+|B|+|C|) − (|A∩B|+|B∩C|+|A∩C|) + x and solve for x!"
            h_ar = "عوّض القيم المعلومة في قانون التضمين والإقصاء: الاتحاد = مجموع المجموعات − مجموع التقاطعات الثنائية + x، ثم أوجد x!"
            s_en = explain_en(
                "Let \\( x \\) be the number of students in all three clubs and set up the 3-set Inclusion–Exclusion equation.",
                [
                    f"Sum of single-club counts: {m(f'{nA} + {nB} + {nC} = {sum1}')}.",
                    f"Sum of pairwise overlaps: {m(f'{pAB} + {pBC} + {pAC} = {sum2}')}.",
                    f"Solve {m(f'{union_val} = {sum1} - {sum2} + x = {base_diff} + x \\implies x = {union_val} - {base_diff} = {ans}')}.",
                ],
                f"Check: every region stays positive — for instance, {c1e}&{c2e} only has {m(f'{pAB} - {ans} = {oab}')} students!",
            )
            s_ar = explain_ar(
                "نفرض أن \\( x \\) هو عدد الطلاب في الأندية الثلاثة معاً ونطبّق معادلة التضمين والإقصاء.",
                [
                    f"مجموع أعداد الأندية الثلاثة: {m(f'{nA} + {nB} + {nC} = {sum1}')}.",
                    f"مجموع التقاطعات الثنائية: {m(f'{pAB} + {pBC} + {pAC} = {sum2}')}.",
                    f"نحل المعادلة: {m(f'{union_val} = {sum1} - {sum2} + x = {base_diff} + x \\implies x = {union_val} - {base_diff} = {ans}')}.",
                ],
                f"تحقق: جميع المناطق موجبة؛ فمثلاً المشتركون في {c1a} و{c2a} فقط عددهم {m(f'{pAB} - {ans} = {oab}')}!",
            )
            distractors = [ans + 2, max(1, ans - 2), ans + 1, pAC]

        qid = f"KMC-T2-EX-21B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_venn_three_sets",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 3. kmc_g89_simultaneous_remainders (16 Qs)
    # ------------------------------------------------------------------
    # (a, b, mode, param, target_kind, diff)
    rem_cases = [
        (4, 6, "same_rem", 1, "min_2d", "Easy"),
        (6, 8, "same_rem", 3, "min_2d", "Easy"),
        (5, 7, "same_rem", 2, "max_2d", "Easy"),
        (6, 9, "same_rem", 4, "max_2d", "Easy"),
        (4, 6, "deficit", 1, "min_2d", "Easy"),
        (8, 12, "same_rem", 5, "min_3d", "Medium"),
        (9, 15, "same_rem", 7, "min_3d", "Medium"),
        (12, 18, "same_rem", 5, "max_3d", "Medium"),
        (14, 21, "same_rem", 9, "min_3d", "Medium"),
        (6, 8, "deficit", 1, "max_2d", "Medium"),
        (5, 9, "deficit", 2, "max_2d", "Medium"),
        (8, 10, "deficit", 3, "min_3d", "Medium"),
        (12, 15, "deficit", 4, "min_3d", "Medium"),
        (15, 20, "same_rem", 11, "max_3d", "Hard"),
        (12, 18, "deficit", 5, "max_3d", "Hard"),
        (16, 24, "deficit", 7, "max_3d", "Hard"),
    ]
    for i, (a, b, mode, param, tkind, diff) in enumerate(rem_cases, 1):
        L = math.lcm(a, b)
        lo, hi = (10, 99) if "2d" in tkind else (100, 999)
        dig_en = "two-digit" if "2d" in tkind else "three-digit"
        dig_ar = "مكوّن من رقمين" if "2d" in tkind else "مكوّن من ثلاثة أرقام"
        ext_en = "smallest" if "min" in tkind else "largest"
        ext_ar = "أصغر" if "min" in tkind else "أكبر"

        if mode == "same_rem":
            r = param
            ra, rb = r, r
            valid = [n for n in range(lo, hi + 1) if n % a == ra and n % b == rb]
            ans = valid[0] if "min" in tkind else valid[-1]
            k_used = (ans - r) // L
            assert ans == L * k_used + r
            q_en = (
                f"What is the **{ext_en} {dig_en}** positive integer that leaves a remainder of {m(r)} "
                f"both when divided by {m(a)} and when divided by {m(b)}?"
            )
            q_ar = (
                f"ما **{ext_ar}** عدد صحيح موجب **{dig_ar}** يعطي الباقي {m(r)} "
                f"عند قسمته على {m(a)} وكذلك عند قسمته على {m(b)}؟"
            )
            h_en = f"Subtract {r} first! Since N − {r} is divisible by both {a} and {b}, N − {r} must be a multiple of lcm({a}, {b}) = {L}."
            h_ar = f"اطرح {r} أولاً! بما أن N − {r} يقبل القسمة على {a} و{b} معاً، فإن N − {r} مضاعف للمضاعف المشترك الأصغر lcm({a}, {b}) = {L}."
            k_adj = k_used - 1 if "min" in tkind else k_used + 1
            n_adj = ans - L if "min" in tkind else ans + L
            s_en = explain_en(
                f"If dividing {m('N')} by {m(a)} and by {m(b)} leaves the **same remainder** {m(r)}, then {m(f'N - {r}')} is a multiple of {m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}.",
                [
                    f"Write the general form: {m(f'N = {L}k + {r}')} for integer {m('k \\ge 0')}.",
                    f"Find the {ext_en} choice inside {m(f'[{lo}, {hi}]')}: taking {m(f'k = {k_used}')} gives {m(f'N = {L} \\times {k_used} + {r} = {ans}')}.",
                    f"Check the next step to confirm the boundary: {m(f'{L} \\times {k_adj} + {r} = {n_adj}')}, which lies outside {m(f'[{lo}, {hi}]')}.",
                ],
                f"Check: {m(f'{ans} = {a} \\times {ans // a} + {ans % a}')} and {m(f'{ans} = {b} \\times {ans // b} + {ans % b}')}!",
            )
            s_ar = explain_ar(
                f"إذا ترك العدد {m('N')} **نفس الباقي** {m(r)} عند القسمة على {m(a)} وعلى {m(b)}، فإن {m(f'N - {r}')} مضاعف لـ {m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}.",
                [
                    f"الصورة العامة للعدد هي: {m(f'N = {L}k + {r}')}.",
                    f"نختار قيمة {m('k')} التي تعطي {ext_ar} عدد في الفترة {m(f'[{lo}, {hi}]')}: عند {m(f'k = {k_used}')} نحصل على {m(f'N = {L} \\times {k_used} + {r} = {ans}')}.",
                    f"نتأكد من حدود الفترة: القيمة المجاورة هي {m(ans - L if 'min' in tkind else ans + L)} وهي خارج نطاق الأعداد المطلوبة.",
                ],
                f"تحقق مباشر: باقي قسمة {m(ans)} على {m(a)} هو {m(ans % a)}، وعلى {m(b)} هو {m(ans % b)}!",
            )
            distractors = [L * k_used - r, ans + L if ans + L < 2000 else ans - L, L * k_used, (a * b) + r]
        else:
            d = param
            ra, rb = a - d, b - d
            valid = [n for n in range(lo, hi + 1) if n % a == ra and n % b == rb]
            ans = valid[0] if "min" in tkind else valid[-1]
            k_used = (ans + d) // L
            assert ans == L * k_used - d
            q_en = (
                f"Find the **{ext_en} {dig_en}** positive integer that leaves remainder {m(ra)} when divided by {m(a)} "
                f"and remainder {m(rb)} when divided by {m(b)}."
            )
            q_ar = (
                f"أوجد **{ext_ar}** عدد صحيح موجب **{dig_ar}** يعطي الباقي {m(ra)} عند قسمته على {m(a)}، "
                f"ويعطي الباقي {m(rb)} عند قسمته على {m(b)}."
            )
            h_en = f"Notice both remainders are {d} short of a full multiple ({a} − {ra} = {d} and {b} − {rb} = {d})! So N + {d} is divisible by both {a} and {b}!"
            h_ar = f"لاحظ أن كلا الباقيين ينقص بمقدار {d} عن المضاعف الكامل ({a} − {ra} = {d} و {b} − {rb} = {d})! إذن N + {d} يقبل القسمة على {a} و{b} معاً!"
            s_en = explain_en(
                f"Both remainders have the **same shortfall** {m(d)}: {m(f'{a} - {ra} = {d}')} and {m(f'{b} - {rb} = {d}')}. "
                f"Therefore, adding {m(d)} makes {m(f'N + {d}')} divisible by both {m(a)} and {m(b)}!",
                [
                    f"Compute {m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}, so {m(f'N + {d} = {L}k \\implies N = {L}k - {d}')}.",
                    f"Pick {m(f'k = {k_used}')} so {m('N')} is the {ext_en} value in {m(f'[{lo}, {hi}]')}: {m(f'N = {L} \\times {k_used} - {d} = {ans}')}.",
                    f"Stepping one block further gives {m(ans - L if 'min' in tkind else ans + L)}, which is outside {m(f'[{lo}, {hi}]')}.",
                ],
                f"Check: {m(f'{ans} = {a} \\times {ans // a} + {ans % a}')} and {m(f'{ans} = {b} \\times {ans // b} + {ans % b}')}!",
            )
            s_ar = explain_ar(
                f"كلا الباقيين يشتركان في **نفس النقص** {m(d)} لأن {m(f'{a} - {ra} = {d}')} و{m(f'{b} - {rb} = {d}')}؛ "
                f"وبالتالي فإن {m(f'N + {d}')} يقبل القسمة على {m(a)} و{m(b)} معاً!",
                [
                    f"نحسب {m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}، ومنه {m(f'N = {L}k - {d}')}.",
                    f"باختيار {m(f'k = {k_used}')} نحصل على {ext_ar} قيمة ضمن {m(f'[{lo}, {hi}]')}: {m(f'N = {L} \\times {k_used} - {d} = {ans}')}.",
                    f"القيمة المجاورة {m(ans - L if 'min' in tkind else ans + L)} تقع خارج النطاق المطلوب.",
                ],
                f"تحقق: قسمة {m(ans)} على {m(a)} تعطي الباقي {m(ans % a)}، وقسمته على {m(b)} تعطي الباقي {m(ans % b)}!",
            )
            distractors = [L * k_used + d, L * k_used, ans - L if "max" in tkind else ans + L, a * b - d]

        qid = f"KMC-T2-EX-21C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        svg_en = svg_statement_cards(
            [(f"÷ {a}", f"Remainder = {ra}"), (f"÷ {b}", f"Remainder = {rb}"), ("Range", f"{lo} ≤ N ≤ {hi}")],
            header_lbl=f"{ext_en.capitalize()} N = ?",
        )
        svg_ar = svg_statement_cards(
            [(f"÷ {a}", f"الباقي = {ra}"), (f"÷ {b}", f"الباقي = {rb}"), ("النطاق", f"{lo} ≤ N ≤ {hi}")],
            header_lbl=f"{ext_ar} عدد N = ؟",
        )
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_simultaneous_remainders",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(out) == 50
    return out


def _gen_lesson_2_2() -> list[dict]:
    out: list[dict] = []
    topic = "Number Theory"

    # ------------------------------------------------------------------
    # 4. kmc_g89_binary_switch_panel (17 Qs, svg_binary_bulbs)
    # ------------------------------------------------------------------
    # Subtype A: read decimal value / toggle switches (6 Qs)
    bin_read_cases = [
        ((1, 0, 1, 1, 0), (16, 8, 4, 2, 1), None, "Easy"),          # 22
        ((1, 1, 0, 0, 1), (16, 8, 4, 2, 1), None, "Easy"),          # 25
        ((0, 1, 1, 1, 0), (16, 8, 4, 2, 1), None, "Easy"),          # 14
        ((1, 0, 1, 1, 0, 1), (32, 16, 8, 4, 2, 1), None, "Medium"), # 45
        ((1, 1, 0, 1, 1, 0), (32, 16, 8, 4, 2, 1), (16, 1), "Medium"),  # shown 54, flip 16 & 1 -> 54 - 16 + 1 = 39
        ((0, 1, 1, 0, 1, 1), (32, 16, 8, 4, 2, 1), (32, 8), "Medium"),  # shown 27, flip 32 & 8 -> 27 + 32 - 8 = 51
    ]
    for i, (bits, weights, flips, diff) in enumerate(bin_read_cases, 1):
        svg = svg_binary_bulbs(bits, weights, lang="en")
        svg_ar = svg_binary_bulbs(bits, weights, lang="ar")
        shown_val = sum(b * w for b, w in zip(bits, weights))
        w_str = ", ".join(str(w) for w in weights)
        state_str = ", ".join(f"{w}:{'ON' if b else 'OFF'}" for b, w in zip(bits, weights))
        state_ar = "، ".join(f"{w}:{'مضيء' if b else 'منطفئ'}" for b, w in zip(bits, weights))
        on_weights = [w for b, w in zip(bits, weights) if b == 1]
        on_sum_str = " + ".join(str(w) for w in on_weights)

        if flips is None:
            ans = shown_val
            q_en = (
                f"A binary light-bulb panel has place-value weights {m(f'({w_str})')}. Each **ON** bulb adds its weight, "
                f"and each **OFF** bulb adds {m(0)}. For the displayed pattern ({state_str}), what base-10 integer is shown?"
            )
            q_ar = (
                f"تحتوي لوحة مصابيح ثنائية على الأوزان المكانية {m(f'({w_str})')}. كل مصباح **مضيء (ON)** يضيف وزنه، "
                f"وكل مصباح **منطفئ (OFF)** يضيف {m(0)}. في النمط المعروض ({state_ar})، ما العدد العشري الممثَّل؟"
            )
            h_en = "List only the weights directly underneath the yellow ON bulbs and add them up!"
            h_ar = "اجمع فقط الأوزان المكتوبة أسفل المصابيح المضيئة (ON)!"
            s_en = explain_en(
                "In binary place value, the represented number is simply the **sum of weights of all ON bulbs**.",
                [
                    f"Identify the **ON** bulbs from left to right: weights {m(', '.join(str(w) for w in on_weights))}.",
                    f"Ignore the **OFF** bulbs (they contribute {m(0)}).",
                    f"Add the active weights: {m(f'{on_sum_str} = {ans}')}.",
                ],
                f"Complement check: total of all bulbs is {m(sum(weights))}, minus OFF bulbs ({m(sum(weights) - ans)}) = {m(ans)}!",
            )
            s_ar = explain_ar(
                "في نظام القيم المكانية الثنائي، العدد الممثَّل هو **مجموع أوزان المصابيح المضيئة (ON) فقط**.",
                [
                    f"نحدد أوزان المصابيح **المضيئة**: {m(', '.join(str(w) for w in on_weights))}.",
                    f"نتجاهل المصابيح المنطفئة لأن مساهمتها تساوي {m(0)}.",
                    f"نجمع الأوزان الفعّالة: {m(f'{on_sum_str} = {ans}')}.",
                ],
                f"تحقق بالمتمم: مجموع كل الأوزان {m(sum(weights))} ناقص أوزان المنطفئة ({m(sum(weights) - ans)}) يساوي {m(ans)}!",
            )
            distractors = [sum(weights) - ans, ans + 2, ans - 2, ans + 4]
        else:
            f1, f2 = flips
            new_bits = [1 - b if w in flips else b for b, w in zip(bits, weights)]
            ans = sum(b * w for b, w in zip(new_bits, weights))
            new_on = [w for b, w in zip(new_bits, weights) if b == 1]
            q_en = (
                f"The {m(len(weights))}-bulb binary panel {m(f'({w_str})')} currently displays ({state_str}). "
                f"If we **flip** (toggle ON↔OFF) the two switches labeled {m(f1)} and {m(f2)}, what new base-10 number is displayed?"
            )
            q_ar = (
                f"تعرض لوحة المصابيح الثنائية ذات الأوزان {m(f'({w_str})')} حالياً الحالة ({state_ar}). "
                f"إذا **عكسنا حالة** المفتاحين ذوي الوزنين {m(f1)} و{m(f2)} (من مضيء إلى منطفئ والعكس)، فما العدد العشري الجديد المعروض؟"
            )
            h_en = f"Find the current value ({shown_val}) first, then add a flipped weight if it turns ON or subtract it if it turns OFF!"
            h_ar = f"احسب القيمة الحالية ({shown_val}) أولاً، ثم أضف وزن المصباح الذي أضاء واطرح وزن المصباح الذي انطفأ!"
            s_en = explain_en(
                "Flipping an **OFF** bulb to **ON** adds its weight; flipping an **ON** bulb to **OFF** subtracts its weight.",
                [
                    f"Current displayed value: {m(f'{on_sum_str} = {shown_val}')}.",
                    f"After toggling weights {m(f1)} and {m(f2)}, the **ON** bulbs become {m(', '.join(str(w) for w in new_on))}.",
                    f"Add the new active weights: {m(' + '.join(str(w) for w in new_on) + f' = {ans}')}.",
                ],
                f"Check: the net change from {m(shown_val)} to {m(ans)} is {m(ans - shown_val)}!",
            )
            s_ar = explain_ar(
                "تحويل مصباح من منطفئ إلى مضيء يضيف وزنه، وتحويله من مضيء إلى منطفئ يطرح وزنه.",
                [
                    f"القيمة المعروضة قبل التغيير: {m(f'{on_sum_str} = {shown_val}')}.",
                    f"بعد عكس حالتي المفتاحين {m(f1)} و{m(f2)} تصبح المصابيح المضيئة هي ذات الأوزان: {m(', '.join(str(w) for w in new_on))}.",
                    f"نجمع الأوزان المضيئة الجديدة: {m(' + '.join(str(w) for w in new_on) + f' = {ans}')}.",
                ],
                f"تحقق: التغير الصافي من {m(shown_val)} إلى {m(ans)} يساوي {m(ans - shown_val)} تماماً!",
            )
            distractors = [shown_val, shown_val + f1 + f2, abs(shown_val - f1 - f2), ans + 4]

        qid = f"KMC-T2-EX-22A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_binary_switch_panel",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg, diagram_ar=svg_ar,
            )
        )

    # Subtype B: how many bulbs are ON for a target integer N (6 Qs)
    bin_count_cases = [
        (19, (16, 8, 4, 2, 1), "Easy"),         # 16+2+1 -> 3 bulbs
        (28, (16, 8, 4, 2, 1), "Easy"),         # 16+8+4 -> 3 bulbs
        (29, (16, 8, 4, 2, 1), "Medium"),       # 16+8+4+1 -> 4 bulbs
        (37, (32, 16, 8, 4, 2, 1), "Medium"),   # 32+4+1 -> 3 bulbs
        (58, (32, 16, 8, 4, 2, 1), "Medium"),   # 32+16+8+2 -> 4 bulbs
        (62, (32, 16, 8, 4, 2, 1), "Medium"),   # 32+16+8+4+2 -> 5 bulbs
    ]
    for j, (target_n, weights, diff) in enumerate(bin_count_cases, 7):
        bits_zero = tuple(0 for _ in weights)
        svg = svg_binary_bulbs(bits_zero, weights, lang="en")
        svg_ar = svg_binary_bulbs(bits_zero, weights, lang="ar")
        rem = target_n
        chosen = []
        for w in weights:
            if rem >= w:
                chosen.append(w)
                rem -= w
        assert rem == 0
        ans = len(chosen)
        assert ans == bin(target_n).count("1")
        w_str = ", ".join(str(w) for w in weights)
        ch_str = " + ".join(str(w) for w in chosen)

        q_en = (
            f"All bulbs on the {m(len(weights))}-switch binary panel {m(f'({w_str})')} start **OFF**, as shown. "
            f"To display the base-10 integer {m(target_n)}, how many bulbs must be switched **ON**?"
        )
        q_ar = (
            f"تبدأ جميع المصابيح في اللوحة الثنائية ذات الأوزان {m(f'({w_str})')} في وضع **الإطفاء (OFF)** كما في الشكل. "
            f"لتمثيل العدد العشري {m(target_n)}، كم مصباحاً يجب تشغيله ليكون **مضيئاً (ON)**؟"
        )
        h_en = f"Use the greedy largest-power rule: subtract the largest weight ≤ {target_n}, then repeat with what remains!"
        h_ar = f"استخدم طريقة الطرح المتدرج من أكبر وزن: اطرح أكبر وزن أصغر من أو يساوي {target_n} ثم كرر العملية مع الباقي!"
        s_en = explain_en(
            "Every integer has a **unique** representation as a sum of distinct powers of 2, found greedily from left (largest weight) to right.",
            [
                f"Pick the largest available weights that fit into {m(target_n)}: {m(f'{target_n} = {ch_str}')}.",
                f"Turn **ON** the switches for {m(', '.join(str(w) for w in chosen))} and leave the remaining switches **OFF**.",
                f"Count the active switches: there are **{m(ans)}** bulbs ON.",
            ],
            f"Quick check: {m(f'{ch_str} = {target_n}')}, using {m(ans)} distinct powers of {m(2)}!",
        )
        s_ar = explain_ar(
            "لكل عدد صحيح تمثيل **وحيد** كمجموع قوى مختلفة للعدد 2، ونجده باختيار أكبر وزن ممكن من اليسار إلى اليمين.",
            [
                f"نفكّك العدد {m(target_n)} إلى مجموع أوزان من اللوحة: {m(f'{target_n} = {ch_str}')}.",
                f"نضيء المفاتيح المقابلة للأوزان {m(', '.join(str(w) for w in chosen))} ونترك البقية منطفئة.",
                f"نعدّ المصابيح المضيئة فنجدها **{m(ans)}** مصابيح.",
            ],
            f"تحقق سريع: {m(f'{ch_str} = {target_n}')}، وعدد المصابيح المضيئة هو {m(ans)}!",
        )
        distractors = [x for x in (1, 2, 3, 4, 5, 6) if x != ans][:4]
        qid = f"KMC-T2-EX-22A-{j:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_binary_switch_panel",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg, diagram_ar=svg_ar,
            )
        )

    # Subtype C: sum of numbers matching a bulb pattern (5 Qs)
    # 13: 5-bulb, exactly 1 bulb ON -> 31 (Medium)
    # 14: 5-bulb, exactly 4 bulbs ON -> 4 * 31 = 124 (Hard)
    # 15: 5-bulb, 16-bulb and 1-bulb both ON (middle 3 arbitrary) -> 8*17 + 4*14 = 192 (Hard)
    # 16: 6-bulb, exactly 5 bulbs ON -> 5 * 63 = 315 (Hard)
    # 17: 6-bulb, left-right symmetric ON/OFF pattern with at least 1 ON -> 4 * 63 = 252 (Hard)
    pat_cases = [
        (
            (1, 0, 0, 0, 0), (16, 8, 4, 2, 1), "Medium",
            lambda b: sum(b) == 1,
            "have **exactly 1 bulb ON** (like the example shown)",
            "يكون فيها **مصباح واحد فقط مضيئاً** (كما في المثال الموضّح)",
            "List all 5 single-bulb configurations and add their weights!",
            "اسرد الحالات الخمس التي يضيء فيها مصباح واحد فقط واجمع أوزانها!",
            "Each of the 5 weights appears ON in **1** configuration.",
            [
                f"There are {m(5)} such patterns, corresponding to the individual weights {m('16, 8, 4, 2, 1')}.",
                f"Add them together (a geometric powers-of-2 sum): {m('16 + 8 + 4 + 2 + 1 = 31')}.",
            ],
            "كل وزن من الأوزان الخمسة يظهر مضيئاً في **حالة واحدة** فقط.",
            [
                f"توجد {m(5)} أعداد تحقق الشرط هي الأوزان المفردة نفسها: {m('16, 8, 4, 2, 1')}.",
                f"نجمعها معاً: {m('16 + 8 + 4 + 2 + 1 = 31')}.",
            ],
            [32, 16, 30, 62],
        ),
        (
            (1, 1, 1, 1, 0), (16, 8, 4, 2, 1), "Hard",
            lambda b: sum(b) == 4,
            "have **exactly 4 bulbs ON** and **1 bulb OFF** (one example is shown)",
            "يكون فيها **4 مصابيح مضيئة بالضبط** ومصباح واحد منطفئ (كما في المثال الموضّح)",
            "Symmetry trick: choosing 4 bulbs ON is the same as choosing which 1 bulb is OFF (31 − w)!",
            "خدعة التماثل: إضاءة 4 مصابيح تعني إطفاء مصباح واحد فقط، فيكون كل عدد على الصورة (31 − وزن المنطفئ)!",
            "By symmetry, there are 5 such patterns (one for each choice of the single OFF bulb), and each weight is ON in **4** of the 5 patterns!",
            [
                f"Total of all 5 weights is {m('16 + 8 + 4 + 2 + 1 = 31')}.",
                f"Across the {m(5)} patterns, each bulb is OFF once and **ON exactly {m(4)} times**.",
                f"Therefore the sum of all 5 numbers is {m('4 \\times 31 = 124')} (equivalently {m('30 + 29 + 27 + 23 + 15 = 124')}).",
            ],
            "بالتماثل توجد 5 حالات (بحسب اختيار المصباح الوحيد المنطفئ)، ويظهر كل وزن مضيئاً في **4 حالات** من أصل 5!",
            [
                f"مجموع الأوزان الخمسة كاملةً يساوي {m('16 + 8 + 4 + 2 + 1 = 31')}.",
                f"في الحالات الخمس، ينطفئ كل مصباح مرة واحدة ويضيء **4 مرات بالضبط**.",
                f"إذن مجموع الأعداد الخمسة يساوي {m('4 \\times 31 = 124')} (وهي {m('30 + 29 + 27 + 23 + 15 = 124')}).",
            ],
            [155, 93, 120, 128],
        ),
        (
            (1, 0, 1, 0, 1), (16, 8, 4, 2, 1), "Hard",
            lambda b: b[0] == 1 and b[4] == 1,
            "have **both outer bulbs (16 and 1) ON**, while the middle three bulbs (8, 4, 2) can be ON or OFF in any combination",
            "يكون فيها **المصباحان الطرفيان (16 و1) مضيئين معاً**، بينما المصابيح الثلاثة الوسطى (8، 4، 2) تأخذ أي حالة إضاءة أو إطفاء",
            "There are 2³ = 8 such patterns! Count how many times each weight is ON across all 8 patterns.",
            "يوجد 2³ = 8 أنماط ممكنة! احسب كم مرة يكون كل مصباح مضيئاً عبر الأنماط الثمانية جميعها.",
            "Count each bulb's contribution separately across all \\( 2^3 = 8 \\) combinations of the three middle switches!",
            [
                f"The 3 middle switches each have 2 choices, giving {m('2^3 = 8')} valid numbers.",
                f"Outer weights {m('16')} and {m('1')} are ON in **all {m(8)}** numbers, contributing {m('8 \\times (16 + 1) = 136')}.",
                f"Each middle weight ({m('8, 4, 2')}) is ON in **half ({m(4)})** of the numbers, contributing {m('4 \\times (8 + 4 + 2) = 56')}; total = {m('136 + 56 = 192')}.",
            ],
            "نحسب مساهمة كل مصباح على حدة عبر التشكيلات الـ \\( 2^3 = 8 \\) للمفاتيح الثلاثة الوسطى!",
            [
                f"للمفاتيح الثلاثة الوسطى {m('2^3 = 8')} تشكيلات ممكنة.",
                f"المصباحان الطرفيان ({m('16')} و{m('1')}) مضيئان في **جميع الأعداد الـ {m(8)}** فيساهمان بـ {m('8 \\times 17 = 136')}.",
                f"كل مصباح أوسط ({m('8, 4, 2')}) يضيء في **نصف الحالات ({m(4)})** فيساهم بـ {m('4 \\times 14 = 56')}؛ والمجموع الكلي = {m('136 + 56 = 192')}.",
            ],
            [136, 248, 176, 196],
        ),
        (
            (1, 1, 1, 1, 1, 0), (32, 16, 8, 4, 2, 1), "Hard",
            lambda b: sum(b) == 5,
            "have **exactly 5 bulbs ON** and **1 bulb OFF** on the 6-bulb panel",
            "يكون فيها **5 مصابيح مضيئة بالضبط** ومصباح واحد منطفئ على اللوحة السداسية",
            "All 6 weights add to 63. Across the 6 patterns with 5 bulbs ON, each bulb is ON in 5 of them!",
            "مجموع الأوزان الستة هو 63. في الأنماط الستة التي يضيء فيها 5 مصابيح، يضيء كل مصباح 5 مرات!",
            "Across the 6 patterns with 1 OFF bulb, every weight is ON exactly **5 times**!",
            [
                f"Sum of all 6 weights: {m('32 + 16 + 8 + 4 + 2 + 1 = 63')}.",
                f"There are {m(6)} valid patterns (one for each choice of the OFF bulb), and each bulb is ON in {m(5)} of them.",
                f"Total sum = {m('5 \\times 63 = 315')}.",
            ],
            "عبر الأنماط الستة ذات المصباح الوحيد المنطفئ، يضيء كل وزن **5 مرات بالضبط**!",
            [
                f"مجموع الأوزان الستة جميعها: {m('32 + 16 + 8 + 4 + 2 + 1 = 63')}.",
                f"توجد {m(6)} حالات صالحة، ويظهر كل مصباح مضيئاً في {m(5)} حالات منها.",
                f"المجموع الكلي = {m('5 \\times 63 = 315')}.",
            ],
            [378, 252, 310, 320],
        ),
        (
            (1, 0, 1, 1, 0, 1), (32, 16, 8, 4, 2, 1), "Hard",
            lambda b: b == b[::-1] and sum(b) >= 1,
            "form a **left-to-right symmetric (mirror) ON/OFF pattern** with at least one bulb ON (one example is shown)",
            "تشكّل **نمطاً متماثلاً مرآتياً بين اليمين واليسار** مع وجود مصباح واحد مضيء على الأقل (كما في المثال الموضّح)",
            "Pair the mirror switches: (32, 1), (16, 2), and (8, 4). Each pair acts together as a single combined switch!",
            "زاوج المفاتيح المتناظرة: (32 مع 1)، و(16 مع 2)، و(8 مع 4)؛ كل زوج يضيء أو ينطفئ معاً!",
            "Symmetry links the 6 bulbs into **3 mirror pairs**: \\( (32,1) \\), \\( (16,2) \\), and \\( (8,4) \\)!",
            [
                f"The 3 mirror pairs have combined weights {m('32+1=33')}, {m('16+2=18')}, and {m('8+4=12')} (total {m('33+18+12 = 63')}).",
                f"Across all {m('2^3 = 8')} symmetric patterns (including all-OFF = {m(0)}), each mirror pair is ON in **half ({m(4)})** of them.",
                f"Since all-OFF contributes {m(0)}, the sum of the {m(7)} positive symmetric numbers is {m('4 \\times 63 = 252')}.",
            ],
            "التماثل المرآتي يربط المصابيح الستة في **3 أزواج متناظرة**: \\( (32,1) \\) و\\( (16,2) \\) و\\( (8,4) \\)!",
            [
                f"أوزان الأزواج الثلاثة هي {m('33')} و{m('18')} و{m('12')}، ومجموعها {m('63')}.",
                f"من بين التشكيلات المتماثلة الـ {m('2^3 = 8')} (بما فيها الصفر)، يضيء كل زوج في **نصفها ({m(4)} مرات)**.",
                f"بما أن حالة الإطفاء الكامل تضيف {m(0)}، فإن مجموع الأعداد السبعة الموجبة يساوي {m('4 \\times 63 = 252')}.",
            ],
            [189, 315, 248, 256],
        ),
    ]
    for off, (ex_bits, weights, diff, pred, cond_en, cond_ar, h_en, h_ar, idea_en, st_en, idea_ar, st_ar, dists) in enumerate(pat_cases, 13):
        svg = svg_binary_bulbs(ex_bits, weights, lang="en")
        svg_ar = svg_binary_bulbs(ex_bits, weights, lang="ar")
        ans = sum(
            sum(b * w for b, w in zip(bits, weights))
            for bits in itertools.product((0, 1), repeat=len(weights))
            if pred(bits)
        )
        w_str = ", ".join(str(w) for w in weights)
        q_en = (
            f"On the binary light-bulb panel with weights {m(f'({w_str})')}, what is the **sum of all base-10 numbers** "
            f"whose bulb configurations {cond_en}?"
        )
        q_ar = (
            f"على لوحة المصابيح الثنائية ذات الأوزان {m(f'({w_str})')}، ما **مجموع جميع الأعداد العشرية** "
            f"التي تحقق تشكيلاتها الشرط التالي: {cond_ar}؟"
        )
        s_en = explain_en(idea_en, st_en, f"Verified across all valid binary states: the exact sum is {m(ans)}!")
        s_ar = explain_ar(idea_ar, st_ar, f"بالتحقق عبر جميع التشكيلات الثنائية الصالحة نجد المجموع يساوي {m(ans)} بالضبط!")
        qid = f"KMC-T2-EX-22A-{off:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, dists, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_binary_switch_panel",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 5. kmc_g89_palindrome_divisibility (17 Qs)
    # ------------------------------------------------------------------
    # (digits, div_k, ask_mode, diff, rule_en, rule_ar)
    pal_cases = [
        (3, 3, "smallest", "Easy"),
        (3, 4, "largest", "Easy"),
        (3, 6, "smallest", "Easy"),
        (3, 9, "smallest", "Easy"),
        (4, 11, "count", "Easy"),
        (3, 8, "smallest", "Medium"),
        (3, 8, "largest", "Medium"),
        (3, 4, "count", "Medium"),
        (3, 9, "count", "Medium"),
        (4, 3, "smallest", "Medium"),
        (4, 4, "smallest", "Medium"),
        (4, 6, "largest", "Medium"),
        (4, 9, "count", "Medium"),
        (3, 6, "count", "Hard"),
        (3, 11, "count", "Hard"),
        (4, 8, "smallest", "Hard"),
        (4, 8, "count", "Hard"),
    ]
    div_hints_en = {
        3: "A number is divisible by 3 iff the sum of its digits is a multiple of 3.",
        4: "A palindrome's first digit equals its last digit (cannot be 0!), so for divisibility by 4 the outer digit must be EVEN (2, 4, 6, or 8) and the last two digits must be a multiple of 4!",
        6: "Divisible by 6 means BOTH even (outer digit in {2, 4, 6, 8}) AND digit sum divisible by 3!",
        8: "An even palindrome has outer digit in {2, 4, 6, 8}; check when the last 3 digits are divisible by 8!",
        9: "A number is divisible by 9 iff the sum of its digits is a multiple of 9 (watch both B = 0 and B = 9 when A = 9!).",
        11: "Use the alternating digit sum test for 11: for ABA test (A − B + A), and for ABBA test (A − B + B − A)!",
    }
    div_hints_ar = {
        3: "يقبل العدد القسمة على 3 إذا وفقط إذا كان مجموع أرقامه من مضاعفات 3.",
        4: "الرقم الأول يساوي الرقم الأخير (ولا يساوي 0!)، لذا للقسمة على 4 يجب أن يكون الرقم الطرفي زوجياً (2 أو 4 أو 6 أو 8) وأن يقبل آخر رقمان القسمة على 4!",
        6: "القسمة على 6 تعني تحقق شرطين معاً: الرقم الطرفي زوجي {2, 4, 6, 8} ومجموع الأرقام يقبل القسمة على 3!",
        8: "يجب أن يكون الرقم الطرفي زوجياً {2, 4, 6, 8} وأن تقبل آخر 3 خانات القسمة على 8!",
        9: "يقبل العدد القسمة على 9 إذا كان مجموع أرقامه من مضاعفات 9 (انتبه لحالتي B = 0 و B = 9 عندما A = 9!).",
        11: "استخدم قاعدة المجموع المتناوب للقسمة على 11: في ABA اختبر (A − B + A)، وفي ABBA اختبر (A − B + B − A)!",
    }
    for i, (digs, dk, ask_m, diff) in enumerate(pal_cases, 1):
        lo, hi = (100, 999) if digs == 3 else (1000, 9999)
        pals = [n for n in range(lo, hi + 1) if str(n) == str(n)[::-1] and n % dk == 0]
        assert len(pals) >= 1
        form_tex = "\\overline{ABA}" if digs == 3 else "\\overline{ABBA}"
        dig_en = "three-digit" if digs == 3 else "four-digit"
        dig_ar = "مكوّن من ثلاثة أرقام" if digs == 3 else "مكوّن من أربعة أرقام"

        if ask_m == "smallest":
            ans = pals[0]
            q_en = (
                f"A palindrome reads the same forwards and backwards (form {m(form_tex)} with {m('A \\neq 0')}). "
                f"What is the **smallest {dig_en} palindrome** that is divisible by {m(dk)}?"
            )
            q_ar = (
                f"العدد المتناظر يُقرأ بنفس الترتيب من اليمين ومن اليسار (على الصورة {m(form_tex)} حيث {m('A \\neq 0')}). "
                f"ما **أصغر عدد متناظر {dig_ar}** يقبل القسمة على {m(dk)}؟"
            )
            distractors = [pals[1] if len(pals) > 1 else ans + dk, ans - dk, ans + 11, lo + 1]
            a_d, b_d = int(str(ans)[0]), int(str(ans)[1])
            s_en = explain_en(
                f"To minimize {m(form_tex)}, make the leading digit {m('A')} as **small as possible** first, then minimize the inner digit {m('B')}.",
                [
                    f"Remember {m('A \\in \\{1, \\dots, 9\\}')} (even {m('A \\in \\{2,4,6,8\\}')} whenever the divisor {m(dk)} is even).",
                    f"Testing the smallest valid outer digit {m(f'A = {a_d}')} and then the smallest valid {m(f'B = {b_d}')} gives {m(ans)}.",
                    f"Verify division: {m(f'{ans} \\div {dk} = {ans // dk}')} with remainder {m(0)}.",
                ],
                f"Every smaller {dig_en} palindrome fails divisibility by {m(dk)}; {m(ans)} is the minimum!",
            )
            s_ar = explain_ar(
                f"لتصغير العدد المتناظر {m(form_tex)}، نبدأ بأصغر قيمة ممكنة للخانة الكبرى {m('A')} ثم أصغر قيمة ممكنة للخانة الوسطى {m('B')}.",
                [
                    f"بما أن {m('A \\in \\{1, \\dots, 9\\}')} (ويجب أن يكون {m('A')} زوجياً إذا كان المقسوم عليه {m(dk)} زوجياً).",
                    f"باختبار أصغر قيمة صالحة {m(f'A = {a_d}')} ثم أصغر قيمة {m(f'B = {b_d}')} نحصل على العدد {m(ans)}.",
                    f"نتحقق بالقسمة: {m(f'{ans} \\div {dk} = {ans // dk}')} والباقي {m(0)}.",
                ],
                f"تحقق: جميع الأعداد المتناظرة الأصغر لا تقبل القسمة على {m(dk)}، فالإجابة الصحيحة هي {m(ans)}!",
            )
        elif ask_m == "largest":
            ans = pals[-1]
            q_en = (
                f"A palindrome reads the same left-to-right and right-to-left (form {m(form_tex)}). "
                f"What is the **largest {dig_en} palindrome** that is divisible by {m(dk)}?"
            )
            q_ar = (
                f"العدد المتناظر يُقرأ من الجهتين بنفس الصورة ({m(form_tex)}). "
                f"ما **أكبر عدد متناظر {dig_ar}** يقبل القسمة على {m(dk)}؟"
            )
            distractors = [pals[-2] if len(pals) > 1 else ans - dk, 999 if digs == 3 else 9999, ans - 11, ans - 22]
            a_d, b_d = int(str(ans)[0]), int(str(ans)[1])
            s_en = explain_en(
                f"To maximize {m(form_tex)}, choose the **largest valid outer digit** {m('A')} first, then the largest valid middle digit {m('B')}.",
                [
                    f"Since {m(dk)} is {'even, the ones digit A must be even, so try A = 8' if dk % 2 == 0 else 'odd, start from A = 9'}.",
                    f"With {m(f'A = {a_d}')}, testing from {m('B = 9')} downward gives {m(f'B = {b_d}')}, producing {m(ans)}.",
                    f"Confirm exact divisibility: {m(f'{ans} = {dk} \\times {ans // dk}')}.",
                ],
                f"Direct check: {m(ans)} is a palindrome and {m(f'{ans} \\div {dk} = {ans // dk}')}!",
            )
            s_ar = explain_ar(
                f"لتكبير العدد المتناظر {m(form_tex)}، نختار **أكبر قيمة صالحة للخانة الطرفية** {m('A')} أولاً ثم أكبر قيمة لـ {m('B')}.",
                [
                    f"بما أن المقسوم عليه {m(dk)} {'زوجي، يجب أن يكون آحاد العدد زوجياً فنبدأ بـ A = 8' if dk % 2 == 0 else 'فردي، نختبر بدءاً من A = 9'}.",
                    f"عند {m(f'A = {a_d}')} وأكبر قيمة صالحة {m(f'B = {b_d}')} نحصل على العدد المتناظر {m(ans)}.",
                    f"نتأكد من القسمة التامة: {m(f'{ans} = {dk} \\times {ans // dk}')}.",
                ],
                f"تحقق: العدد {m(ans)} متناظر ويقبل القسمة على {m(dk)} دون باقٍ!",
            )
        else:
            ans = len(pals)
            q_en = (
                f"How many **{dig_en} palindromes** (integers of the form {m(form_tex)} with {m('1 \\le A \\le 9')} "
                f"and {m('0 \\le B \\le 9')}) are divisible by {m(dk)}?"
            )
            q_ar = (
                f"كم **عدداً متناظراً {dig_ar}** (على الصورة {m(form_tex)} حيث {m('1 \\le A \\le 9')} "
                f"و{m('0 \\le B \\le 9')}) يقبل القسمة على {m(dk)}؟"
            )
            sample_str = ", ".join(str(x) for x in pals[:3]) + (f", \\dots, {pals[-1]}" if len(pals) > 3 else "")
            if digs == 4 and dk == 11:
                why_en = f"Compute the alternating digit sum of {m('\\overline{ABBA}')}: {m('A - B + B - A = 0')}, which is **always** a multiple of {m(11)} for every choice of {m('A')} and {m('B')}!"
                why_ar = f"المجموع المتناوب لأرقام {m('\\overline{ABBA}')} هو {m('A - B + B - A = 0')}، وهو يقبل القسمة على {m(11)} **دائماً** مهما كانت قيمتا {m('A')} و{m('B')}!"
            else:
                by_a = {a_v: [x for x in pals if str(x)[0] == str(a_v)] for a_v in range(1, 10)}
                active_a = [f"A={k} ({len(v)})" for k, v in by_a.items() if v]
                why_en = f"Counting valid middle digits {m('B \\in \\{0..9\\}')} for each outer digit {m('A')} gives: {', '.join(active_a)}."
                why_ar = f"بعدّ قيم {m('B \\in \\{0..9\\}')} الصالحة لكل قيمة من {m('A')} نجد التوزيع: {', '.join(active_a)}."
            s_en = explain_en(
                f"There are {m('9 \\times 10 = 90')} total {dig_en} palindromes; apply the divisibility rule for {m(dk)} to {m(form_tex)}.",
                [
                    why_en,
                    f"Summing the valid choices across all {m('A \\in \\{1, \\dots, 9\\}')} gives exactly **{m(ans)}** palindromes ({m(sample_str)}).",
                ],
                f"Check: smallest is {m(pals[0])}, largest is {m(pals[-1])}, and total count is {m(ans)}!",
            )
            s_ar = explain_ar(
                f"يوجد إجمالاً {m('9 \\times 10 = 90')} عدداً متناظراً {dig_ar}؛ نطبّق قاعدة القسمة على {m(dk)} على الصيغة {m(form_tex)}.",
                [
                    why_ar,
                    f"بجمع جميع الخيارات الصالحة لـ {m('A')} و{m('B')} نحصل على **{m(ans)}** أعداد متناظرة ({m(sample_str)}).",
                ],
                f"تحقق: أصغرها {m(pals[0])} وأكبرها {m(pals[-1])} ومجموع عددها {m(ans)} بالضبط!",
            )
            distractors = [90 // dk, ans + 1, max(1, ans - 1), ans + 2, 90 if ans != 90 else 81]

        qid = f"KMC-T2-EX-22B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        pal_slots = ["A", "B", "A"] if digs == 3 else ["A", "B", "B", "A"]
        pal_note_en = {"smallest": "Smallest = ?", "largest": "Largest = ?", "count": "Count = ?"}[ask_m]
        pal_note_ar = {"smallest": "أصغر متناظر = ؟", "largest": "أكبر متناظر = ؟", "count": "العدد = ؟"}[ask_m]
        svg_en = svg_digit_cards(pal_slots, badge_lbl=f"Divisible by {dk}", note_lbl=pal_note_en)
        svg_ar = svg_digit_cards(pal_slots, badge_lbl=f"يقبل القسمة على {dk}", note_lbl=pal_note_ar)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_palindrome_divisibility",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                div_hints_en[dk], div_hints_ar[dk], s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 6. kmc_g89_digital_root_invariant (16 Qs)
    # ------------------------------------------------------------------
    # (expr_tex, exact_val, diff, hint_e, hint_a, step_e, step_a)
    dr_cases = [
        (
            "9 \\times 2026 + 7", 9 * 2026 + 7, "Easy",
            "Any multiple of 9 contributes 0 mod 9 to the digital root!",
            "أي مضاعف للعدد 9 يكافئ 0 عند القسمة على 9 في الجذر الرقمي!",
            f"{m('9 \\times 2026')} is a multiple of {m(9)}, so {m('9 \\times 2026 + 7 \\equiv 0 + 7 = 7 \\pmod{9}')}.",
            f"الحد {m('9 \\times 2026')} مضاعف للعدد {m(9)}، لذا {m('9 \\times 2026 + 7 \\equiv 0 + 7 = 7 \\pmod{9}')}.",
        ),
        (
            "18 \\times 543 + 5", 18 * 543 + 5, "Easy",
            "Since 18 = 2 × 9, 18 × 543 is automatically divisible by 9!",
            "بما أن 18 = 2 × 9، فإن 18 × 543 يقبل القسمة على 9 تلقائياً!",
            f"Since {m('9 \\mid 18')}, {m('18 \\times 543 + 5 \\equiv 0 + 5 = 5 \\pmod{9}')}.",
            f"بما أن {m('18')} مضاعف لـ {m(9)}، فإن {m('18 \\times 543 + 5 \\equiv 0 + 5 = 5 \\pmod{9}')}.",
        ),
        (
            "27 \\times 819 + 9", 27 * 819 + 9, "Easy",
            "Both terms are multiples of 9! What is the single-digit digital root of a positive multiple of 9?",
            "كلا الحدين من مضاعفات 9! ما الجذر الرقمي الموجب لأي مضاعف موجب للعدد 9؟",
            f"Both {m('27 \\times 819')} and {m('9')} are divisible by {m(9)}, so the positive sum is a multiple of {m(9)}, giving digital root **{m(9)}** (never {m(0)}!).",
            f"كلا الحدين يقبل القسمة على {m(9)}، وبما أن الناتج عدد موجب يقبل القسمة على {m(9)} فإن جذره الرقمي يساوي **{m(9)}** (وليس صفراً!).",
        ),
        (
            "10^{50} + 26", 10**50 + 26, "Easy",
            "Write out the digits of 10⁵⁰ + 26: it starts with 1, has lots of 0s, and ends with 26!",
            "تخيّل أرقام العدد 10⁵⁰ + 26: يبدأ بالرقم 1، يليه أصفار، وينتهي بالعدد 26!",
            f"Since {m('10 \\equiv 1 \\pmod{9}')}, {m('10^{50} + 26 \\equiv 1^{50} + 26 = 27 \\equiv 0 \\pmod{9}')}, so its single-digit digital root is **{m(9)}** (first digit sum is {m('1 + 2 + 6 = 9')}).",
            f"مجموع أرقام العدد {m('10^{50} + 26')} مباشرةً هو {m('1 + 0 + \\dots + 0 + 2 + 6 = 9')}، فالجذر الرقمي يساوي **{m(9)}**.",
        ),
        (
            "10^{100} + 10^{40} + 15", 10**100 + 10**40 + 15, "Easy",
            "Every power 10ⁿ has remainder 1 when divided by 9!",
            "كل قوة على الصورة 10ⁿ تعطي الباقي 1 عند القسمة على 9!",
            f"Using {m('10^k \\equiv 1 \\pmod{9}')}: {m('1 + 1 + 15 = 17')}, and {m('1 + 7 = 8')}.",
            f"بما أن {m('10^k \\equiv 1 \\pmod{9}')} فإن المجموع يكافئ {m('1 + 1 + 15 = 17')}، ثم {m('1 + 7 = 8')}.",
        ),
        (
            "999 \\times 74 + 4", 999 * 74 + 4, "Medium",
            "Notice 999 = 9 × 111 is a multiple of 9!",
            "لاحظ أن 999 = 9 × 111 مضاعف للعدد 9!",
            f"Because {m('9 \\mid 999')}, {m('999 \\times 74 + 4 \\equiv 0 + 4 = 4 \\pmod{9}')}.",
            f"بما أن {m('999')} يقبل القسمة على {m(9)}، فإن {m('999 \\times 74 + 4 \\equiv 0 + 4 = 4 \\pmod{9}')}.",
        ),
        (
            "4 \\times 10^{60} + 38", 4 * 10**60 + 38, "Medium",
            "Replace 10⁶⁰ with 1 (mod 9), or sum the non-zero digits 4, 3, and 8!",
            "عوّض عن 10⁶⁰ بـ 1 (باقي القسمة على 9)، أو اجمع الأرقام غير الصفرية 4 و3 و8!",
            f"First digit sum is {m('4 + 3 + 8 = 15')}, and summing digits once more gives {m('1 + 5 = 6')}.",
            f"مجموع الأرقام الأول هو {m('4 + 3 + 8 = 15')}، وبجمع رقمي {m(15)} نحصل على {m('1 + 5 = 6')}.",
        ),
        (
            "10^{80} - 4", 10**80 - 4, "Medium",
            "Use mod 9 directly: 10⁸⁰ ≡ 1 (mod 9), so 1 − 4 ≡ −3 ≡ 6 (mod 9)!",
            "استخدم باقي القسمة على 9 مباشرة: 10⁸⁰ ≡ 1، ومنه 1 − 4 ≡ −3 ≡ 6 (mod 9)!",
            f"Modulo {m(9)}: {m('10^{80} - 4 \\equiv 1 - 4 = -3 \\equiv 6 \\pmod{9}')} (in digits, it is seventy-nine {m(9)}s followed by {m(6)}!).",
            f"بحساب باقي القسمة على {m(9)}: {m('10^{80} - 4 \\equiv 1 - 4 = -3 \\equiv 6 \\pmod{9}')} (فهو يتكون من 79 تسعة ثم الرقم {m(6)}!).",
        ),
        (
            "2^{12}", 2**12, "Medium",
            "Notice 2³ = 8 ≡ −1 (mod 9), so 2⁶ = 64 ≡ 1 (mod 9)!",
            "لاحظ أن 2³ = 8 ≡ −1 (mod 9)، وبالتالي 2⁶ = 64 ≡ 1 (mod 9)!",
            f"Since {m('2^3 = 8 \\equiv -1 \\pmod{9}')}, we get {m('2^{12} = (2^3)^4 \\equiv (-1)^4 = 1 \\pmod{9}')}.",
            f"بما أن {m('2^3 = 8 \\equiv -1 \\pmod{9}')}، فإن {m('2^{12} = (2^3)^4 \\equiv (-1)^4 = 1 \\pmod{9}')}.",
        ),
        (
            "2^{19}", 2**19, "Medium",
            "Use 2⁶ ≡ 1 (mod 9) to reduce the exponent 19 = 3 × 6 + 1!",
            "استخدم الحقيقة 2⁶ ≡ 1 (mod 9) لتبسيط الأس 19 = 3 × 6 + 1!",
            f"Since {m('2^6 = 64 \\equiv 1 \\pmod{9}')} and {m('19 = 6 \\times 3 + 1')}, {m('2^{19} = (2^6)^3 \\times 2^1 \\equiv 1^3 \\times 2 = 2 \\pmod{9}')}.",
            f"بما أن {m('2^6 = 64 \\equiv 1 \\pmod{9}')} وأن {m('19 = 6 \\times 3 + 1')}، فإن {m('2^{19} \\equiv 1^3 \\times 2^1 = 2 \\pmod{9}')}.",
        ),
        (
            "2^{32}", 2**32, "Medium",
            "Divide the exponent 32 by the cycle length 6 (since 2⁶ ≡ 1 mod 9)!",
            "اقسم الأس 32 على طول الدورة 6 (لأن 2⁶ ≡ 1 عند القسمة على 9)!",
            f"Write {m('32 = 6 \\times 5 + 2')}; since {m('2^6 \\equiv 1 \\pmod{9}')}, {m('2^{32} \\equiv 2^2 = 4 \\pmod{9}')}.",
            f"نكتب {m('32 = 6 \\times 5 + 2')}؛ وبما أن {m('2^6 \\equiv 1 \\pmod{9}')} فإن {m('2^{32} \\equiv 2^2 = 4 \\pmod{9}')}.",
        ),
        (
            "1234 \\times 5678", 1234 * 5678, "Medium",
            "Find the digit sum mod 9 of each factor BEFORE multiplying!",
            "احسب باقي مجموع أرقام كل عامل على 9 قبل إجراء الضرب!",
            f"Digit sums: {m('1+2+3+4 = 10 \\equiv 1 \\pmod{9}')} and {m('5+6+7+8 = 26 \\equiv 8 \\pmod{9}')}; product {m('\\equiv 1 \\times 8 = 8 \\pmod{9}')}.",
            f"مجموع أرقام الأول {m('10 \\equiv 1 \\pmod{9}')}، ومجموع أرقام الثاني {m('26 \\equiv 8 \\pmod{9}')}؛ فحاصل الضرب يكافئ {m('1 \\times 8 = 8 \\pmod{9}')}.",
        ),
        (
            "47 \\times 65 + 1", 47 * 65 + 1, "Medium",
            "Reduce 47 and 65 modulo 9 using their digit sums (4+7=11≡2 and 6+5=11≡2)!",
            "بسّط 47 و65 بجمع أرقامهما على 9: كلٌّ منهما يعطي 11 ≡ 2 (mod 9)!",
            f"Modulo {m(9)}: {m('47 \\equiv 4+7 = 11 \\equiv 2')} and {m('65 \\equiv 6+5 = 11 \\equiv 2')}, so {m('47 \\times 65 + 1 \\equiv 2 \\times 2 + 1 = 5 \\pmod{9}')}.",
            f"باقي القسمة على {m(9)}: {m('47 \\equiv 2')} و{m('65 \\equiv 2')}، ومنه {m('47 \\times 65 + 1 \\equiv 2 \\times 2 + 1 = 5 \\pmod{9}')}.",
        ),
        (
            "2^{53}", 2**53, "Hard",
            "Powers of 2 mod 9 repeat every 6 steps: 2, 4, 8, 7, 5, 1. Check 53 mod 6!",
            "بواقي قوى العدد 2 على 9 تتكرر كل 6 خطوات: 2، 4، 8، 7، 5، 1. احسب باقي قسمة 53 على 6!",
            f"Since {m('2^6 \\equiv 1 \\pmod{9}')} and {m('53 = 6 \\times 8 + 5')}, {m('2^{53} \\equiv 2^5 = 32 \\equiv 3 + 2 = 5 \\pmod{9}')}.",
            f"بما أن {m('2^6 \\equiv 1 \\pmod{9}')} وأن {m('53 = 6 \\times 8 + 5')}، فإن {m('2^{53} \\equiv 2^5 = 32 \\equiv 5 \\pmod{9}')}.",
        ),
        (
            "987654321 \\times 37 + 3", 987654321 * 37 + 3, "Hard",
            "Check the digit sum of 987654321 first: 1 + 2 + ... + 9 = 45!",
            "احسب أولاً مجموع أرقام 987654321: المجموع 1 + 2 + ... + 9 = 45!",
            f"The digit sum of {m('987654321')} is {m('45 = 9 \\times 5')}, so {m('987654321 \\equiv 0 \\pmod{9}')}; thus the whole expression is {m('\\equiv 0 \\times 1 + 3 = 3 \\pmod{9}')}.",
            f"مجموع أرقام {m('987654321')} هو {m('45')} (من مضاعفات {m(9)})، فيصبح المقدار كاملاً {m('\\equiv 0 + 3 = 3 \\pmod{9}')}.",
        ),
        (
            "(10^{75} + 8)^2", (10**75 + 8) ** 2, "Hard",
            "Find (10⁷⁵ + 8) mod 9 BEFORE squaring!",
            "احسب باقي (10⁷⁵ + 8) على 9 قبل التربيع!",
            f"Inside the parentheses: {m('10^{75} + 8 \\equiv 1 + 8 = 9 \\equiv 0 \\pmod{9}')}. Squaring {m('0 \\pmod{9}')} stays {m('0 \\pmod{9}')}, so the positive integer's digital root is **{m(9)}**!",
            f"ما داخل القوس يكافئ {m('1 + 8 = 9 \\equiv 0 \\pmod{9}')}، وتربيع مضاعف للعدد {m(9)} يبقى مضاعفاً موجباً للعدد {m(9)}، فجذره الرقمي هو **{m(9)}**!",
        ),
    ]
    for i, (expr_tex, exact_v, diff, h_en, h_ar, st_en, st_ar) in enumerate(dr_cases, 1):
        ans = _digital_root_exact(exact_v)
        mod_check = 9 if exact_v % 9 == 0 else (exact_v % 9)
        assert ans == mod_check

        q_en = (
            f"We repeatedly replace a positive integer with the **sum of its digits** until a single digit ({m('1')} to {m('9')}) remains "
            f"(its *digital root*). What single digit is obtained at the end if we start with {m(expr_tex)}?"
        )
        q_ar = (
            f"نستبدل العدد الصحيح الموجب مراراً بـ **مجموع أرقامه** حتى يتبقى رقم واحد فقط من {m('1')} إلى {m('9')} "
            f"(ويُسمّى *الجذر الرقمي*). ما الرقم الواحد المتبقي في النهاية عند البدء بالمقدار {m(expr_tex)}؟"
        )
        s_en = explain_en(
            "Summing digits preserves the remainder **modulo 9** because \\( 10^k \\equiv 1 \\pmod{9} \\)! "
            "For any positive integer, the final single digit equals \\( N \\bmod 9 \\) (written as \\( 9 \\) whenever \\( 9 \\mid N \\)).",
            [
                "Reduce each part of the expression modulo 9 using digit sums or powers.",
                st_en,
                f"Therefore, the repeated digit sum settles at **{m(ans)}**.",
            ],
            f"Remember: a positive integer never has digital root {m(0)}; multiples of {m(9)} end at {m(9)}, and here the answer is {m(ans)}!",
        )
        s_ar = explain_ar(
            "عملية جمع الأرقام تحافظ دائماً على باقي القسمة على **9** لأن \\( 10^k \\equiv 1 \\pmod{9} \\)! "
            "لأي عدد موجب، الرقم النهائي يساوي باقي قسمته على 9 (ويساوي \\( 9 \\) إذا كان من مضاعفات 9).",
            [
                "نبسّط أجزاء المقدار بحساب بواقيها عند القسمة على 9.",
                st_ar,
                f"بالتالي يستقر مجموع الأرقام المتكرر عند الرقم **{m(ans)}**.",
            ],
            f"تذكّر: الجذر الرقمي لأي عدد موجب ينتمي إلى {m('\\{1,\\dots,9\\}')}، وهنا الإجابة المؤكدة هي {m(ans)}!",
        )
        distractors = [x for x in (9, 1, 2, 3, 4, 5, 6, 7, 8, 0) if x != ans][:4]
        qid = f"KMC-T2-EX-22C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        expr_u = re.sub(
            r"\^\{(\d+)\}",
            lambda mo: _sup(mo.group(1)),
            expr_tex.replace(" \\times ", "×").replace(" - ", " − ").replace(" + ", "+").replace("^2", "²"),
        )
        svg_en = svg_algebra_flow(
            [("Start", expr_u), ("Step", "∑ digits"), ("Digital Root", "?")],
            arrows=["→", "→"],
            title_lbl="Repeated Digit Sum",
        )
        svg_ar = svg_algebra_flow(
            [("البداية", expr_u), ("الخطوة", "مجموع الأرقام"), ("الجذر الرقمي", "؟")],
            arrows=["→", "→"],
            title_lbl="تكرار جمع الأرقام",
        )
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_digital_root_invariant",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(out) == 50
    return out


def _gen_lesson_2_3() -> list[dict]:
    out: list[dict] = []
    topic = "Algebra"

    # ------------------------------------------------------------------
    # 7. kmc_g89_geometric_square_identity (17 Qs, svg_area_identity_square)
    # ------------------------------------------------------------------
    sq_cases = [
        # (va, vb, mode, p1, p2, diff)
        ("a", "b", "find_ab", 10, 58, "Easy"),
        ("x", "y", "find_ab", 12, 80, "Easy"),
        ("m", "n", "find_ab", 9, 45, "Easy"),
        ("p", "q", "find_ab", 11, 65, "Easy"),
        ("a", "b", "find_sum_sq", 8, 15, "Easy"),
        ("x", "y", "find_sum_sq", 13, 30, "Medium"),
        ("m", "n", "find_sum_sq", 14, 41, "Medium"),
        ("p", "q", "find_sum_sq", 15, 47, "Medium"),
        ("a", "b", "find_sum_sq", 16, 55, "Medium"),
        ("a", "b", "find_diff_sq", 10, 21, "Medium"),
        ("x", "y", "find_diff_sq", 11, 24, "Medium"),
        ("m", "n", "sum_sq_from_diff", 5, 14, "Medium"),
        ("p", "q", "sum_sq_from_diff", 6, 16, "Medium"),
        ("m", "n", "find_diff_sq", 13, 35, "Hard"),
        ("p", "q", "find_diff_sq", 15, 48, "Hard"),
        ("a", "b", "ab_from_squares", 196, 36, "Hard"),
        ("x", "y", "ab_from_squares", 225, 49, "Hard"),
    ]
    for i, (va, vb, mode, p1, p2, diff) in enumerate(sq_cases, 1):
        svg = svg_area_identity_square(va, vb)

        if mode == "find_ab":
            S, Q = p1, p2
            assert (S * S - Q) % 2 == 0 and S * S > Q
            ans = (S * S - Q) // 2
            assert S * S >= 4 * ans
            q_en = (
                f"A square of side {m(f'{va} + {vb} = {S}')} is partitioned into two squares of areas "
                f"{m(f'{va}^2')} and {m(f'{vb}^2')} and two congruent rectangles of area {m(f'{va}{vb}')}, as shown. "
                f"If {m(f'{va}^2 + {vb}^2 = {Q}')}, what is the area {m(f'{va}{vb}')} of **one** of the two rectangles?"
            )
            q_ar = (
                f"قُسِّم مربع طول ضلعه {m(f'{va} + {vb} = {S}')} إلى مربعين مساحتاهما {m(f'{va}^2')} و{m(f'{vb}^2')} "
                f"ومستطيلين متطابقين مساحة كلٍّ منهما {m(f'{va}{vb}')} كما في الشكل. إذا كان {m(f'{va}^2 + {vb}^2 = {Q}')}، "
                f"فما مساحة **أحد** المستطيلين {m(f'{va}{vb}')}؟"
            )
            h_en = f"Total square area is ({va}+{vb})² = {S*S}, which equals ({va}² + {vb}²) + 2{va}{vb}. Don't forget to divide 2{va}{vb} by 2!"
            h_ar = f"مساحة المربع الكبير هي ({va}+{vb})² = {S*S}، وتساوي ({va}² + {vb}²) + 2{va}{vb}. لا تنسَ القسمة على 2 لإيجاد مستطيل واحد!"
            s_en = explain_en(
                f"The partitioned square shows geometrically that {m(f'({va} + {vb})^2 = {va}^2 + 2{va}{vb} + {vb}^2')}.",
                [
                    f"Compute the total area of the large square: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"Subtract the two corner squares {m(f'{va}^2 + {vb}^2 = {Q}')} to get both rectangles together: {m(f'2{va}{vb} = {S*S} - {Q} = {S*S - Q}')}.",
                    f"Divide by {m(2)} for **one** rectangle: {m(f'{va}{vb} = {S*S - Q} \\div 2 = {ans}')}.",
                ],
                f"Trap avoided: {m(S*S - Q)} is the area of **both** rectangles ({m(f'2{va}{vb}')}), whereas **one** rectangle is {m(ans)}!",
            )
            s_ar = explain_ar(
                f"يوضّح تقسيم المربع هندسياً المتطابقة الشهيرة: {m(f'({va} + {vb})^2 = {va}^2 + 2{va}{vb} + {vb}^2')}.",
                [
                    f"مساحة المربع الكلي: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"نطرح مجموع مساحتي المربعين {m(f'{va}^2 + {vb}^2 = {Q}')} فنجد مجموع المستطيلين: {m(f'2{va}{vb} = {S*S} - {Q} = {S*S - Q}')}.",
                    f"نقسم على {m(2)} لإيجاد مساحة مستطيل **واحد**: {m(f'{va}{vb} = {S*S - Q} \\div 2 = {ans}')}.",
                ],
                f"انتبه للفخ: العدد {m(S*S - Q)} يمثّل المستطيلين معاً، أما المستطيل الواحد فمساحته {m(ans)}!",
            )
            distractors = [S * S - Q, ans + 4, max(1, ans - 3), Q - S]
        elif mode == "find_sum_sq":
            S, P = p1, p2
            assert S * S >= 4 * P
            ans = S * S - 2 * P
            q_en = (
                f"In the partitioned square of side {m(f'{va} + {vb}')} shown, suppose {m(f'{va} + {vb} = {S}')} "
                f"and each rectangle has area {m(f'{va}{vb} = {P}')}. What is the combined area {m(f'{va}^2 + {vb}^2')} of the two inner squares?"
            )
            q_ar = (
                f"في المربع المقسَّم الذي طول ضلعه {m(f'{va} + {vb}')} كما في الشكل، إذا علمت أن {m(f'{va} + {vb} = {S}')} "
                f"وأن مساحة كل مستطيل تساوي {m(f'{va}{vb} = {P}')}، فما مجموع مساحتي المربعين الداخليين {m(f'{va}^2 + {vb}^2')}؟"
            )
            h_en = f"You don't need to find {va} and {vb} separately! Subtract the TWO rectangles (2 × {P}) from the outer square ({S}²)."
            h_ar = f"لا تحتاج إلى إيجاد {va} و{vb} منفردين! اطرح مساحتي المستطيلين (2 × {P}) من مساحة المربع الكبير ({S}²)."
            s_en = explain_en(
                f"Rearrange {m(f'({va} + {vb})^2 = {va}^2 + 2{va}{vb} + {vb}^2')} to isolate {m(f'{va}^2 + {vb}^2 = ({va} + {vb})^2 - 2{va}{vb}')}!",
                [
                    f"Outer square area: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"Combined area of the **two** rectangles: {m(f'2{va}{vb} = 2 \\times {P} = {2*P}')}.",
                    f"Subtract: {m(f'{va}^2 + {vb}^2 = {S*S} - {2*P} = {ans}')}.",
                ],
                f"Trap check: subtracting only one {m(f'{va}{vb}')} gives {m(S*S - P)}; subtracting **both** rectangles gives {m(ans)}!",
            )
            s_ar = explain_ar(
                f"من المتطابقة الهندسية نرتب الحدود لنحصل على: {m(f'{va}^2 + {vb}^2 = ({va} + {vb})^2 - 2{va}{vb}')}!",
                [
                    f"مساحة المربع الخارجي: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"مجموع مساحتي **المستطيلين معاً**: {m(f'2{va}{vb} = 2 \\times {P} = {2*P}')}.",
                    f"نطرح فنجد: {m(f'{va}^2 + {vb}^2 = {S*S} - {2*P} = {ans}')}.",
                ],
                f"احذر من طرح مستطيل واحد فقط ({m(S*S - P)})؛ بطرح المستطيلين معاً نجد {m(ans)}!",
            )
            distractors = [S * S - P, S * S + 2 * P, S * S - 4 * P, ans + 6]
        elif mode == "find_diff_sq":
            S, P = p1, p2
            assert S * S > 4 * P
            ans = S * S - 4 * P
            q_en = (
                f"Using the square-identity diagram as inspiration, if positive numbers {m(va)} and {m(vb)} satisfy "
                f"{m(f'{va} + {vb} = {S}')} and {m(f'{va}{vb} = {P}')}, what is the exact value of {m(f'({va} - {vb})^2')}?"
            )
            q_ar = (
                f"بالاستفادة من متطابقات المربع المقسَّم، إذا كان العددان الموجبان {m(va)} و{m(vb)} يحققان "
                f"{m(f'{va} + {vb} = {S}')} و{m(f'{va}{vb} = {P}')}، فما القيمة الدقيقة للمقدار {m(f'({va} - {vb})^2')}؟"
            )
            h_en = f"Compare ({va}+{vb})² = {va}² + 2{va}{vb} + {vb}² with ({va}−{vb})² = {va}² − 2{va}{vb} + {vb}²: their difference is 4{va}{vb}!"
            h_ar = f"قارن بين ({va}+{vb})² = {va}² + 2{va}{vb} + {vb}² و ({va}−{vb})² = {va}² − 2{va}{vb} + {vb}²: الفرق بينهما يساوي 4{va}{vb}!"
            s_en = explain_en(
                f"The golden bridge between sum and difference of two variables is {m(f'({va} - {vb})^2 = ({va} + {vb})^2 - 4{va}{vb}')}!",
                [
                    f"Square the sum: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"Compute four times the product: {m(f'4{va}{vb} = 4 \\times {P} = {4*P}')}.",
                    f"Subtract: {m(f'({va} - {vb})^2 = {S*S} - {4*P} = {ans}')}.",
                ],
                f"Notice why it is {m(f'-4{va}{vb}')}: {m(f'+2{va}{vb}')} drops to {m(0)} after {m(f'-2{va}{vb}')}, and needs another {m(f'-2{va}{vb}')} to reach {m(f'-2{va}{vb}')}!",
            )
            s_ar = explain_ar(
                f"الجسر الذهبي الذي يربط مربع المجموع بمربع الفرق هو: {m(f'({va} - {vb})^2 = ({va} + {vb})^2 - 4{va}{vb}')}!",
                [
                    f"نربّع المجموع: {m(f'({va} + {vb})^2 = {S}^2 = {S*S}')}.",
                    f"نحسب أربعة أضعاف حاصل الضرب: {m(f'4{va}{vb} = 4 \\times {P} = {4*P}')}.",
                    f"نطرح: {m(f'({va} - {vb})^2 = {S*S} - {4*P} = {ans}')}.",
                ],
                f"انتبه: نطرح {m(f'4{va}{vb}')} وليس {m(f'2{va}{vb}')} لأننا ننتقل من {m(f'+2{va}{vb}')} إلى {m(f'-2{va}{vb}')}!",
            )
            distractors = [S * S - 2 * P, S * S - 3 * P, ans + 4, max(1, ans - 4)]
        elif mode == "sum_sq_from_diff":
            D, P = p1, p2
            ans = D * D + 4 * P
            q_en = (
                f"Two positive numbers {m(va)} and {m(vb)} (representing the segments in the square diagram) satisfy "
                f"{m(f'{va} - {vb} = {D}')} and {m(f'{va}{vb} = {P}')}. What is the total area {m(f'({va} + {vb})^2')} of the outer square?"
            )
            q_ar = (
                f"عددان موجبان {m(va)} و{m(vb)} (يمثلان جزأي ضلع المربع الموضّح) يحققان "
                f"{m(f'{va} - {vb} = {D}')} و{m(f'{va}{vb} = {P}')}. ما المساحة الكلية للمربع الخارجي {m(f'({va} + {vb})^2')}؟"
            )
            h_en = f"Use ({va} + {vb})² = ({va} − {vb})² + 4{va}{vb}!"
            h_ar = f"استخدم المتطابقة ({va} + {vb})² = ({va} − {vb})² + 4{va}{vb}!"
            s_en = explain_en(
                f"Since {m(f'({va} + {vb})^2')} has {m(f'+2{va}{vb}')} while {m(f'({va} - {vb})^2')} has {m(f'-2{va}{vb}')}, we add {m(f'4{va}{vb}')}: "
                f"{m(f'({va} + {vb})^2 = ({va} - {vb})^2 + 4{va}{vb}')}.",
                [
                    f"Square the given difference: {m(f'({va} - {vb})^2 = {D}^2 = {D*D}')}.",
                    f"Add four rectangles of area {m(P)}: {m(f'4 \\times {P} = {4*P}')}.",
                    f"Combine: {m(f'({va} + {vb})^2 = {D*D} + {4*P} = {ans}')}.",
                ],
                f"Check: {m(f'{D*D} + {4*P} = {ans}')}!",
            )
            s_ar = explain_ar(
                f"بما أن الفرق بين {m(f'({va} + {vb})^2')} و{m(f'({va} - {vb})^2')} هو {m(f'4{va}{vb}')}، فإن {m(f'({va} + {vb})^2 = ({va} - {vb})^2 + 4{va}{vb}')}.",
                [
                    f"نربّع الفرق المعطى: {m(f'({va} - {vb})^2 = {D}^2 = {D*D}')}.",
                    f"نضيف أربعة أمثال الضرب: {m(f'4 \\times {P} = {4*P}')}.",
                    f"المجموع = {m(f'{D*D} + {4*P} = {ans}')}.",
                ],
                f"تحقق سريع: {m(f'{D*D} + {4*P} = {ans}')}!",
            )
            distractors = [D * D + 2 * P, D * D + P, ans + 8, ans - 10]
        else:
            U, V = p1, p2
            assert (U - V) % 4 == 0
            ans = (U - V) // 4
            q_en = (
                f"In the partitioned square model for {m(va)} and {m(vb)}, suppose {m(f'({va} + {vb})^2 = {U}')} "
                f"and {m(f'({va} - {vb})^2 = {V}')}. What is the area {m(f'{va}{vb}')} of one rectangle?"
            )
            q_ar = (
                f"في نموذج المربع المقسَّم للمتغيرين {m(va)} و{m(vb)}، إذا كان {m(f'({va} + {vb})^2 = {U}')} "
                f"و{m(f'({va} - {vb})^2 = {V}')}، فما مساحة المستطيل الواحد {m(f'{va}{vb}')}؟"
            )
            h_en = f"Subtract the two equations! ({va} + {vb})² − ({va} − {vb})² = 4{va}{vb}."
            h_ar = f"اطرح المعادلتين! ({va} + {vb})² − ({va} − {vb})² = 4{va}{vb}."
            s_en = explain_en(
                f"Subtracting {m(f'({va} - {vb})^2 = {va}^2 - 2{va}{vb} + {vb}^2')} from {m(f'({va} + {vb})^2 = {va}^2 + 2{va}{vb} + {vb}^2')} cancels both squares and leaves {m(f'4{va}{vb}')}!",
                [
                    f"Compute the difference: {m(f'4{va}{vb} = {U} - {V} = {U - V}')}.",
                    f"Divide by {m(4)}: {m(f'{va}{vb} = {U - V} \\div 4 = {ans}')}.",
                ],
                f"Check: {m(f'4 \\times {ans} + {V} = {U}')}!",
            )
            s_ar = explain_ar(
                f"بطرح {m(f'({va} - {vb})^2')} من {m(f'({va} + {vb})^2')} تختفي المربعات ويتبقى {m(f'4{va}{vb}')} مباشرةً!",
                [
                    f"نطرح القيمتين: {m(f'4{va}{vb} = {U} - {V} = {U - V}')}.",
                    f"نقسم على {m(4)}: {m(f'{va}{vb} = {U - V} \\div 4 = {ans}')}.",
                ],
                f"تحقق: {m(f'4 \\times {ans} + {V} = {U}')}!",
            )
            distractors = [(U - V) // 2, U - V, ans + 5, max(1, ans - 4)]

        qid = f"KMC-T2-EX-23A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_geometric_square_identity",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 8. kmc_g89_telescoping_fraction_prod (17 Qs)
    # ------------------------------------------------------------------
    tele_cases = [
        ("minus", 2, 10, "Easy"),
        ("minus", 2, 25, "Easy"),
        ("minus", 3, 18, "Easy"),
        ("plus", 2, 19, "Easy"),
        ("plus", 3, 23, "Easy"),
        ("minus", 4, 27, "Medium"),
        ("minus", 5, 35, "Medium"),
        ("minus", 7, 42, "Medium"),
        ("plus", 4, 47, "Medium"),
        ("plus", 5, 31, "Medium"),
        ("plus", 6, 49, "Medium"),
        ("sq", 2, 10, "Medium"),
        ("sq", 2, 15, "Medium"),
        ("sq", 2, 20, "Hard"),
        ("sq", 2, 50, "Hard"),
        ("sq", 3, 12, "Hard"),
        ("sq", 4, 16, "Hard"),
    ]
    for i, (kind, a, b, diff) in enumerate(tele_cases, 1):
        if kind == "minus":
            ans = math.prod(Fraction(k - 1, k) for k in range(a, b + 1))
            assert ans == Fraction(a - 1, b)
            expr_tex = f"\\left(1 - \\frac{{1}}{{{a}}}\\right)\\left(1 - \\frac{{1}}{{{a+1}}}\\right)\\left(1 - \\frac{{1}}{{{a+2}}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{b}}}\\right)"
            chain_tex = f"\\frac{{{a-1}}}{{{a}}} \\times \\frac{{{a}}}{{{a+1}}} \\times \\frac{{{a+1}}}{{{a+2}}} \\times \\cdots \\times \\frac{{{b-1}}}{{{b}}}"
            h_en = f"Rewrite each parenthesis as a single fraction (k − 1)/k and watch neighboring numerators and denominators cancel!"
            h_ar = f"اكتب كل قوس على صورة كسر واحد (k − 1)/k ولاحظ اختصار المقامات مع البسوط المجاورة!"
            s_en = explain_en(
                "Turn each subtraction into a single fraction \\( 1 - \\frac{1}{k} = \\frac{k-1}{k} \\) to trigger a **telescoping cancellation**!",
                [
                    f"Rewrite every factor: {m(chain_tex)}.",
                    f"Every intermediate number ({m(f'{a}, {a+1}, \\dots, {b-1}')}) appears once in a denominator and once in the next numerator, so they all cancel!",
                    f"Only the very first numerator {m(a-1)} and the very last denominator {m(b)} survive: {m(f'\\frac{{{a-1}}}{{{b}}} = {fmt_val(ans)}')}.",
                ],
                f"Check on the first two terms alone: {m(f'\\frac{{{a-1}}}{{{a}}} \\times \\frac{{{a}}}{{{a+1}}} = \\frac{{{a-1}}}{{{a+1}}}')} — the pattern holds all the way to {m(b)}!",
            )
            s_ar = explain_ar(
                "نحوّل كل قوس إلى كسر واحد \\( 1 - \\frac{1}{k} = \\frac{k-1}{k} \\) فيحدث **اختصار متسلسل (تلسكوبي)**!",
                [
                    f"نكتب العوامل على صورة كسور: {m(chain_tex)}.",
                    f"تختصر جميع الأعداد الوسطى ({m(f'{a}, {a+1}, \\dots, {b-1}')}) بين المقامات والبسوط المتتالية!",
                    f"لا يتبقى سوى البسط الأول {m(a-1)} والمقام الأخير {m(b)}: {m(f'\\frac{{{a-1}}}{{{b}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق بأول حدين: {m(f'\\frac{{{a-1}}}{{{a}}} \\times \\frac{{{a}}}{{{a+1}}} = \\frac{{{a-1}}}{{{a+1}}}')}، ويستمر النمط حتى {m(b)}!",
            )
            distractors = [Fraction(1, b), Fraction(a, b), Fraction(a - 1, b - 1), Fraction(a - 1, b + 1)]
        elif kind == "plus":
            ans = math.prod(Fraction(k + 1, k) for k in range(a, b + 1))
            assert ans == Fraction(b + 1, a)
            ans_final = int(ans) if ans.denominator == 1 else ans
            expr_tex = f"\\left(1 + \\frac{{1}}{{{a}}}\\right)\\left(1 + \\frac{{1}}{{{a+1}}}\\right)\\left(1 + \\frac{{1}}{{{a+2}}}\\right)\\cdots\\left(1 + \\frac{{1}}{{{b}}}\\right)"
            chain_tex = f"\\frac{{{a+1}}}{{{a}}} \\times \\frac{{{a+2}}}{{{a+1}}} \\times \\frac{{{a+3}}}{{{a+2}}} \\times \\cdots \\times \\frac{{{b+1}}}{{{b}}}"
            h_en = f"Write 1 + 1/k = (k + 1)/k! Notice each numerator cancels the NEXT fraction's denominator."
            h_ar = f"اكتب 1 + 1/k على الصورة (k + 1)/k! لاحظ أن كل بسط يختصر مع مقام الكسر الذي يليه."
            s_en = explain_en(
                "Writing \\( 1 + \\frac{1}{k} = \\frac{k+1}{k} \\) makes every numerator cancel the next denominator!",
                [
                    f"Convert each parenthesis into one fraction: {m(chain_tex)}.",
                    f"Cancel {m(f'{a+1}, {a+2}, \\dots, {b}')} diagonally between numerators and denominators.",
                    f"Only the last numerator {m(b+1)} and the first denominator {m(a)} remain: {m(f'\\frac{{{b+1}}}{{{a}}} = {fmt_val(ans_final)}')}.",
                ],
                f"Common trap avoided: the final numerator is {m(f'{b} + 1 = {b+1}')}, NOT {m(b)}!",
            )
            s_ar = explain_ar(
                "بكتابة كل قوس على الصورة \\( 1 + \\frac{1}{k} = \\frac{k+1}{k} \\) يختصر كل بسط مع مقام الكسر التالي!",
                [
                    f"نكتب الجداء على هيئة كسور: {m(chain_tex)}.",
                    f"تختصر الأعداد {m(f'{a+1}, {a+2}, \\dots, {b}')} قطرياً بين البسوط والمقامات.",
                    f"يتبقى البسط الأخير {m(b+1)} مقسوماً على المقام الأول {m(a)}: {m(f'\\frac{{{b+1}}}{{{a}}} = {fmt_val(ans_final)}')}.",
                ],
                f"انتبه للفخ الشائع: البسط الأخير هو {m(f'{b} + 1 = {b+1}')} وليس {m(b)}!",
            )
            ans = ans_final
            distractors = [
                Fraction(b, a) if Fraction(b, a).denominator != 1 else b // a,
                Fraction(b + 1, a + 1) if Fraction(b + 1, a + 1).denominator != 1 else (b + 1) // (a + 1),
                ans + 1 if isinstance(ans, int) else Fraction(ans.numerator + 1, ans.denominator),
                max(1, ans - 1) if isinstance(ans, int) else Fraction(max(1, ans.numerator - 1), ans.denominator),
            ]
        else:
            ans = math.prod(Fraction(k * k - 1, k * k) for k in range(a, b + 1))
            assert ans == Fraction(a - 1, a) * Fraction(b + 1, b)
            expr_tex = f"\\left(1 - \\frac{{1}}{{{a}^2}}\\right)\\left(1 - \\frac{{1}}{{{a+1}^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{b}^2}}\\right)"
            h_en = "Use Difference of Squares on EVERY factor: 1 − 1/k² = (1 − 1/k)(1 + 1/k) = ((k−1)/k) × ((k+1)/k)!"
            h_ar = "طبّق فرق المربعين على كل قوس: 1 − 1/k² = (1 − 1/k)(1 + 1/k) = ((k−1)/k) × ((k+1)/k)!"
            s_en = explain_en(
                "Factor each term by **Difference of Squares**: \\( 1 - \\frac{1}{k^2} = \\left(1 - \\frac{1}{k}\\right)\\left(1 + \\frac{1}{k}\\right) = \\frac{k-1}{k} \\cdot \\frac{k+1}{k} \\)!",
                [
                    f"Split into two telescoping products: {m(f'\\left(\\frac{{{a-1}}}{{{a}}}\\cdots\\frac{{{b-1}}}{{{b}}}\\right) \\times \\left(\\frac{{{a+1}}}{{{a}}}\\cdots\\frac{{{b+1}}}{{{b}}}\\right)')}.",
                    f"The first chain telescopes to {m(f'\\frac{{{a-1}}}{{{b}}}')}, and the second chain telescopes to {m(f'\\frac{{{b+1}}}{{{a}}}')}.",
                    f"Multiply the two survivors and simplify: {m(f'\\frac{{{a-1}}}{{{b}}} \\times \\frac{{{b+1}}}{{{a}}} = {fmt_val(ans)}')}.",
                ],
                f"Double check with exact fractions: the product reduces cleanly to {m(fmt_val(ans))}!",
            )
            s_ar = explain_ar(
                "نحلّل كل قوس بـ **فرق المربعين**: \\( 1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k} \\) فنحصل على جداءين تلسكوبيين معاً!",
                [
                    f"نفصل السلسلتين: {m(f'\\left(\\frac{{{a-1}}}{{{a}}}\\cdots\\frac{{{b-1}}}{{{b}}}\\right) \\times \\left(\\frac{{{a+1}}}{{{a}}}\\cdots\\frac{{{b+1}}}{{{b}}}\\right)')}.",
                    f"تختصر السلسلة الأولى إلى {m(f'\\frac{{{a-1}}}{{{b}}}')}، وتختصر السلسلة الثانية إلى {m(f'\\frac{{{b+1}}}{{{a}}}')}.",
                    f"نضرب الناتجين ونبسّط الكسر: {m(f'\\frac{{{a-1}}}{{{b}}} \\times \\frac{{{b+1}}}{{{a}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق: الكسر المبسّط في أبسط صورة هو {m(fmt_val(ans))}!",
            )
            distractors = [
                Fraction(b - 1, a * b),
                Fraction(b, 2 * b) if a == 2 else Fraction(a - 1, b),
                Fraction(ans.numerator + 1, ans.denominator),
                Fraction(max(1, ans.numerator - 1), ans.denominator),
            ]

        q_en = f"Without a calculator, evaluate the exact product in simplest form: {m(expr_tex)}."
        q_ar = f"دون استخدام الآلة الحاسبة، أوجد القيمة الدقيقة لحاصل الضرب في أبسط صورة: {m(expr_tex)}."
        qid = f"KMC-T2-EX-23B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        if kind == "minus":
            t_terms = [f"1 − 1/{a}", f"1 − 1/{a+1}", "···", f"1 − 1/{b}"]
            t_hdr = f"({a-1}/{a}) × ({a}/{a+1}) × ···"
        elif kind == "plus":
            t_terms = [f"1 + 1/{a}", f"1 + 1/{a+1}", "···", f"1 + 1/{b}"]
            t_hdr = f"({a+1}/{a}) × ({a+2}/{a+1}) × ···"
        else:
            t_terms = [f"1 − 1/{a}²", f"1 − 1/{a+1}²", "···", f"1 − 1/{b}²"]
            t_hdr = "1−1/k² = (k−1)(k+1)/k²"
        svg_en = svg_telescoping_chain(t_terms, op_sym="×", title_lbl=t_hdr, footer_lbl="Product = ?", slash_middle=True)
        svg_ar = svg_telescoping_chain(t_terms, op_sym="×", title_lbl=t_hdr, footer_lbl="حاصل الضرب = ؟", slash_middle=True)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_telescoping_fraction_prod",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 9. kmc_g89_linear_floor_equation (16 Qs)
    # ------------------------------------------------------------------
    floor_cases = [
        ("count_pos", 6, 4, "Easy"),
        ("count_pos", 8, 0, "Easy"),
        ("count_pos", 9, 5, "Easy"),
        ("sum_int", 4, 3, "Easy"),
        ("sum_int", 5, 2, "Easy"),
        ("sqrt_sum", 15, 0, "Medium"),
        ("sqrt_sum", 20, 0, "Medium"),
        ("sqrt_sum", 24, 0, "Medium"),
        ("sqrt_sum", 30, 0, "Medium"),
        ("sqrt_sum", 35, 0, "Medium"),
        ("sqrt_sum", 48, 0, "Medium"),
        ("eq_solve", 3, 14, "Medium"),
        ("eq_solve", 4, 22, "Medium"),
        ("eq_solve", 5, 33, "Hard"),
        ("eq_solve", 6, 45, "Hard"),
        ("eq_solve", 7, 61, "Hard"),
    ]
    for i, (fmode, p1, p2, diff) in enumerate(floor_cases, 1):
        if fmode in ("count_pos", "sum_int"):
            k, m_val = p1, p2
            sols = [n for n in range(1, 500) if n // k == m_val]
            ans = len(sols) if fmode == "count_pos" else sum(sols)
            lo_s, hi_s = sols[0], sols[-1]
            ask_en = "How many **positive integers** \\( n \\) satisfy" if fmode == "count_pos" else "What is the **sum** of all positive integers \\( n \\) that satisfy"
            ask_ar = "كم **عدداً صحيحاً موجباً** \\( n \\) يحقق" if fmode == "count_pos" else "ما **مجموع** جميع الأعداد الصحيحة الموجبة \\( n \\) التي تحقق"
            q_en = (
                f"Let {m('\\lfloor x \\rfloor')} denote the greatest integer less than or equal to {m('x')}. "
                f"{ask_en} {m(f'\\left\\lfloor \\frac{{n}}{{{k}}} \\right\\rfloor = {m_val}')}?"
            )
            q_ar = (
                f"يرمز {m('\\lfloor x \\rfloor')} إلى أكبر عدد صحيح أصغر من أو يساوي {m('x')}. "
                f"{ask_ar} المعادلة {m(f'\\left\\lfloor \\frac{{n}}{{{k}}} \\right\\rfloor = {m_val}')}؟"
            )
            h_en = f"Rewrite ⌊n/{k}⌋ = {m_val} as the double inequality {m_val} ≤ n/{k} < {m_val + 1}, then multiply by {k}!"
            h_ar = f"حوّل المعادلة ⌊n/{k}⌋ = {m_val} إلى المتباينة المزدوجة {m_val} ≤ n/{k} < {m_val + 1}، ثم اضرب في {k}!"
            s_en = explain_en(
                f"By definition of the floor function, {m(f'\\lfloor n/{k} \\rfloor = {m_val}')} means {m(f'{m_val} \\le \\frac{{n}}{{{k}}} < {m_val + 1}')}.",
                [
                    f"Multiply through by {m(k)}: {m(f'{m_val * k} \\le n < {(m_val + 1) * k}')}.",
                    f"Keeping **positive** integers {m('n \\ge 1')}, the valid integers are {m(f'{lo_s}, {lo_s + 1}, \\dots, {hi_s}')}.",
                    f"{'Count them' if fmode == 'count_pos' else 'Add them up'}: "
                    + (f"{m(f'{hi_s} - {lo_s} + 1 = {ans}')}." if fmode == "count_pos" else f"{m(' + '.join(str(x) for x in sols) + f' = {ans}')}."),
                ],
                f"{'Trap avoided: n = 0 is NOT a positive integer!' if m_val == 0 else f'Every integer from {lo_s} to {hi_s} has quotient {m_val} when divided by {k}!'}",
            )
            s_ar = explain_ar(
                f"من تعريف دالة الصحيح (الأرضية)، فإن {m(f'\\lfloor n/{k} \\rfloor = {m_val}')} تعني {m(f'{m_val} \\le \\frac{{n}}{{{k}}} < {m_val + 1}')}.",
                [
                    f"نضرب أطراف المتباينة في {m(k)}: {m(f'{m_val * k} \\le n < {(m_val + 1) * k}')}.",
                    f"بمراعاة شرط الأعداد الصحيحة **الموجبة** ({m('n \\ge 1')})، القيم الصالحة هي {m(f'{lo_s}, {lo_s + 1}, \\dots, {hi_s}')}.",
                    (f"عدد هذه القيم هو: {m(f'{hi_s} - {lo_s} + 1 = {ans}')}." if fmode == "count_pos" else f"مجموع هذه القيم هو: {m(' + '.join(str(x) for x in sols) + f' = {ans}')}."),
                ],
                f"{'انتبه للفخ: الصفر ليس عدداً موجباً لذا استبعدناه!' if m_val == 0 else f'تحقق: قسمة أي عدد من {lo_s} إلى {hi_s} على {k} تعطي خارج قسمة صحيحاً يساوي {m_val}!'}",
            )
            distractors = [k + 1, k - 1 if ans != k - 1 else k, ans + k, max(1, ans - 2)]
        elif fmode == "sqrt_sum":
            N = p1
            ans = sum(math.isqrt(x) for x in range(1, N + 1))
            max_m = math.isqrt(N)
            blocks = []
            for mv in range(1, max_m + 1):
                lo_b = mv * mv
                hi_b = min(N, (mv + 1) ** 2 - 1)
                cnt = hi_b - lo_b + 1
                blocks.append(f"{cnt} \\times {mv}")
            blk_sum_tex = " + ".join(blocks)
            q_en = (
                f"Where {m('\\lfloor x \\rfloor')} denotes the greatest integer less than or equal to {m('x')}, "
                f"find the exact value of the sum: "
                f"{m(f'\\lfloor\\sqrt{{1}}\\rfloor + \\lfloor\\sqrt{{2}}\\rfloor + \\lfloor\\sqrt{{3}}\\rfloor + \\cdots + \\lfloor\\sqrt{{{N}}}\\rfloor')}."
            )
            q_ar = (
                f"إذا كان {m('\\lfloor x \\rfloor')} يرمز إلى أكبر عدد صحيح أصغر من أو يساوي {m('x')}، "
                f"فأوجد القيمة الدقيقة للمجموع: "
                f"{m(f'\\lfloor\\sqrt{{1}}\\rfloor + \\lfloor\\sqrt{{2}}\\rfloor + \\lfloor\\sqrt{{3}}\\rfloor + \\cdots + \\lfloor\\sqrt{{{N}}}\\rfloor')}."
            )
            h_en = f"Group the terms between consecutive perfect squares: 1..3 give 1, 4..8 give 2, 9..15 give 3, 16..24 give 4, ...!"
            h_ar = f"جمّع الحدود الواقعة بين المربعات الكاملة المتتالية: من 1 إلى 3 تعطي 1، ومن 4 إلى 8 تعطي 2، ومن 9 إلى 15 تعطي 3، وهكذا!"
            s_en = explain_en(
                "Between two consecutive perfect squares \\( m^2 \\) and \\( (m+1)^2 - 1 \\), every integer has the **exact same** floor square root \\( m \\)!",
                [
                    f"Split {m(f'1..{N}')} at perfect squares {m(', '.join(str(v*v) for v in range(1, max_m + 1)))}.",
                    f"Count terms in each block and multiply by {m('m')}: {m(blk_sum_tex)}.",
                    f"Add the block totals: {m(f'{blk_sum_tex} = {ans}')}.",
                ],
                f"Total number of terms checked: {m(' + '.join(str(min(N, (mv+1)**2 - 1) - mv*mv + 1) for mv in range(1, max_m + 1)) + f' = {N}')} terms!",
            )
            s_ar = explain_ar(
                "بين كل مربعين كاملين متتاليين من \\( m^2 \\) إلى \\( (m+1)^2 - 1 \\)، جميع الأعداد تشترك في **نفس القيمة** \\( \\lfloor\\sqrt{k}\\rfloor = m \\)!",
                [
                    f"نقسّم الأعداد من {m(1)} إلى {m(N)} عند المربعات الكاملة {m(', '.join(str(v*v) for v in range(1, max_m + 1)))}.",
                    f"نضرب عدد حدود كل فترة في قيمتها الثابتة: {m(blk_sum_tex)}.",
                    f"نجمع النواتج: {m(f'{blk_sum_tex} = {ans}')}.",
                ],
                f"تحقق من عدد الحدود: مجموع أطوال الفترات يساوي {m(N)} حداً بالضبط، والمجموع {m(ans)}!",
            )
            distractors = [ans + max_m, ans - max_m, ans + 3, ans - 4]
        else:
            k, n_true = p1, p2
            T = n_true + n_true // k
            brute_sols = [x for x in range(1, T + 5) if x + x // k == T]
            assert brute_sols == [n_true]
            ans = n_true
            q_val, r_val = divmod(n_true, k)
            q_en = (
                f"Let {m('\\lfloor x \\rfloor')} be the greatest integer less than or equal to {m('x')}. "
                f"Find the positive integer {m('n')} that satisfies the equation {m(f'n + \\left\\lfloor \\frac{{n}}{{{k}}} \\right\\rfloor = {T}')}."
            )
            q_ar = (
                f"ليكن {m('\\lfloor x \\rfloor')} أكبر عدد صحيح أصغر من أو يساوي {m('x')}. "
                f"أوجد العدد الصحيح الموجب {m('n')} الذي يحقق المعادلة {m(f'n + \\left\\lfloor \\frac{{n}}{{{k}}} \\right\\rfloor = {T}')}."
            )
            h_en = f"Write n = {k}q + r with remainder 0 ≤ r < {k}! Then ⌊n/{k}⌋ = q, so the equation becomes ({k + 1})q + r = {T}!"
            h_ar = f"اكتب n = {k}q + r حيث الباقي 0 ≤ r < {k}! عندئذٍ ⌊n/{k}⌋ = q، فتتحول المعادلة إلى ({k + 1})q + r = {T}!"
            s_en = explain_en(
                f"Divide {m('n')} by {m(k)} with remainder: write {m(f'n = {k}q + r')} where {m(f'0 \\le r < {k}')}. Then {m(f'\\lfloor n/{k} \\rfloor = q')}!",
                [
                    f"Substitute into the equation: {m(f'({k}q + r) + q = ({k + 1})q + r = {T}')}.",
                    f"Since {m(f'0 \\le r < {k} < {k + 1}')}, {m('q')} and {m('r')} are simply the quotient and remainder when {m(T)} is divided by {m(k + 1)}: {m(f'{T} = {k + 1} \\times {q_val} + {r_val}')}.",
                    f"Recover {m('n')}: {m(f'n = {k} \\times {q_val} + {r_val} = {ans}')}.",
                ],
                f"Plug {m(f'n = {ans}')} back in: {m(f'{ans} + \\lfloor {ans}/{k} \\rfloor = {ans} + {q_val} = {T}')}!",
            )
            s_ar = explain_ar(
                f"باستخدام القسمة الإقليدية نكتب {m(f'n = {k}q + r')} حيث {m(f'0 \\le r < {k}')}، فيكون {m(f'\\lfloor n/{k} \\rfloor = q')} مباشرةً!",
                [
                    f"نعوّض في المعادلة: {m(f'({k}q + r) + q = ({k + 1})q + r = {T}')}.",
                    f"بما أن {m(f'0 \\le r < {k + 1}')}، نقسم {m(T)} على {m(k + 1)} فنحصل على {m(f'{T} = {k + 1} \\times {q_val} + {r_val}')}، أي {m(f'q = {q_val}')} و{m(f'r = {r_val}')}.",
                    f"نستخرج قيمة {m('n')}: {m(f'n = {k} \\times {q_val} + {r_val} = {ans}')}.",
                ],
                f"تحقق بالتعويض: {m(f'{ans} + \\lfloor {ans}/{k} \\rfloor = {ans} + {q_val} = {T}')}!",
            )
            distractors = [ans + 1, ans - 1, (T * k) // (k + 1) + 2, ans + 2]

        qid = f"KMC-T2-EX-23C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        if fmode in ("count_pos", "sum_int"):
            fl_ticks = [(str(m_val), True), (f"n/{k}", True), (str(m_val + 1), False)]
            fl_hdr = f"⌊n / {k}⌋ = {m_val}"
            fl_ftr_en = "Count of n > 0 = ?" if fmode == "count_pos" else "Sum of n > 0 = ?"
            fl_ftr_ar = "عدد قيم n الموجبة = ؟" if fmode == "count_pos" else "مجموع قيم n = ؟"
            fl_ints = ["", "≤", "<", ""]
        elif fmode == "sqrt_sum":
            fl_ticks = [("1²", True), ("2²", True), ("3²", True), (f"≤{N}", True)]
            fl_hdr = f"⌊√1⌋ + ··· + ⌊√{N}⌋"
            fl_ftr_en, fl_ftr_ar = "Sum = ?", "المجموع = ؟"
            fl_ints = ["", "⌊√k⌋=1", "⌊√k⌋=2", "···", ""]
        else:
            fl_ticks = [("q", True), (f"n/{k}", True), ("q + 1", False)]
            fl_hdr = f"n + ⌊n / {k}⌋ = {T}"
            fl_ftr_en, fl_ftr_ar = "Solve n = ?", "أوجد n = ؟"
            fl_ints = ["", "≤", "<", ""]
        svg_en = svg_number_line_sign_chart(fl_ticks, intervals=fl_ints, header_lbl=fl_hdr, footer_lbl=fl_ftr_en)
        svg_ar = svg_number_line_sign_chart(fl_ticks, intervals=fl_ints, header_lbl=fl_hdr, footer_lbl=fl_ftr_ar)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_linear_floor_equation",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(out) == 50
    return out


def _gen_lesson_2_4() -> list[dict]:
    out: list[dict] = []
    topic = "Algebra"

    # ------------------------------------------------------------------
    # 10. kmc_g89_harmonic_round_trip_speed (17 Qs, svg_motion_timeline)
    # ------------------------------------------------------------------
    harm_cases = [
        (30, 60, "round", "Car", "السيارة", "Easy"),
        (40, 60, "round", "Bus", "الحافلة", "Easy"),
        (20, 30, "round", "Cyclist", "الدراج", "Easy"),
        (12, 24, "half", "Runner", "العدّاء", "Easy"),
        (60, 120, "round", "Train", "القطار", "Easy"),
        (15, 30, "round", "Boat", "القارب", "Medium"),
        (24, 8, "round", "Hiker", "المتسلّق", "Medium"),
        (36, 12, "half", "Skater", "المتزلّج", "Medium"),
        (60, 90, "round", "Courier", "مندوب التوصيل", "Medium"),
        (80, 120, "half", "Express van", "مركبة النقل", "Medium"),
        (10, 40, "round", "Drone", "الطائرة المسيّرة", "Medium"),
        (15, 60, "round", "Mountain biker", "راكب الدراجة الجبلية", "Medium"),
        (21, 28, "half", "Rowing team", "فريق التجديف", "Medium"),
        (20, 50, "round", "Shuttle", "الحافلة الترددية", "Hard"),      # 2000/70 = 200/7 km/h (Fraction!)
        (60, 40, "rev", "Driver", "السائق", "Hard"),                   # given v1=60, avg=48 -> find v2=40
        (15, 60, "rev", "Climber", "المتسلّق الجبلي", "Hard"),         # given v1=15, avg=24 -> find v2=60
        (30, 60, "rev_half", "Triathlete", "متسابق التحمّل", "Hard"),  # given v1=30, avg=40 -> find v2=60
    ]
    for i, (v1, v2, hmode, who_en, who_ar, diff) in enumerate(harm_cases, 1):
        harm_f = Fraction(2 * v1 * v2, v1 + v2)
        harm_val = int(harm_f) if harm_f.denominator == 1 else harm_f
        arith_f = Fraction(v1 + v2, 2)
        arith_val = int(arith_f) if arith_f.denominator == 1 else arith_f

        if hmode in ("round", "half"):
            ans = harm_val
            is_round = hmode == "round"
            svg = svg_motion_timeline(
                "A", "B", "d" if is_round else "2d",
                f"v₁ = {v1}", f"v₂ = {v2}", meet=is_round,
            )
            if is_round:
                q_en = (
                    f"{who_en} travels from point **A** to point **B** at a constant speed of {m(v1)} km/h "
                    f"and immediately returns along the exact same route from **B** to **A** at {m(v2)} km/h. "
                    f"What is the **average speed** (in km/h) for the entire round trip?"
                )
                q_ar = (
                    f"ينتقل ({who_ar}) من النقطة **A** إلى النقطة **B** بسرعة ثابتة مقدارها {m(v1)} كم/س، "
                    f"ثم يعود فوراً عبر الطريق نفسه من **B** إلى **A** بسرعة {m(v2)} كم/س. "
                    f"ما **السرعة المتوسطة** (بوحدة كم/س) لرحلة الذهاب والإياب كاملةً؟"
                )
            else:
                q_en = (
                    f"{who_en} covers the **first half of the distance** from **A** to **B** at {m(v1)} km/h "
                    f"and the **second half of the distance** at {m(v2)} km/h. "
                    f"What is the **average speed** (in km/h) over the whole journey?"
                )
                q_ar = (
                    f"يقطع ({who_ar}) **نصف المسافة الأول** من **A** إلى **B** بسرعة {m(v1)} كم/س، "
                    f"ويقطع **نصف المسافة الثاني** بسرعة {m(v2)} كم/س. "
                    f"ما **السرعة المتوسطة** (بوحدة كم/س) للرحلة كاملةً؟"
                )
            h_en = f"Careful: ({v1} + {v2})/2 is a famous trap! Pick a smart half-distance d = lcm({v1}, {v2}) = {math.lcm(v1, v2)} km, or use 2·v₁·v₂ / (v₁ + v₂)!"
            h_ar = f"احذر من الفخ الشهير ({v1} + {v2})/2! افرض طول كل شوط d = lcm({v1}, {v2}) = {math.lcm(v1, v2)} كم، أو طبّق قانون الوسط التوافقي 2·v₁·v₂ / (v₁ + v₂)!"
            d_smart = math.lcm(v1, v2)
            t1_s, t2_s = d_smart // v1, d_smart // v2
            s_en = explain_en(
                f"Average speed is ALWAYS **Total Distance ÷ Total Time**! Because more time is spent at the slower speed, "
                f"the true average is the **harmonic mean** {m('\\frac{2 v_1 v_2}{v_1 + v_2}')}, NOT {m('\\frac{v_1 + v_2}{2}')}!",
                [
                    f"Pick a convenient one-way (half) distance {m(f'd = \\operatorname{{lcm}}({v1}, {v2}) = {d_smart}')} km so Total Distance = {m(2 * d_smart)} km.",
                    f"Time for part 1: {m(f'{d_smart} \\div {v1} = {t1_s}')} h; time for part 2: {m(f'{d_smart} \\div {v2} = {t2_s}')} h; Total Time = {m(t1_s + t2_s)} h.",
                    f"Average speed = {m(f'\\frac{{{2 * d_smart}}}{{{t1_s + t2_s}}} = {fmt_val(ans)}')} km/h.",
                ],
                f"Trap warning: the simple average {m(fmt_val(arith_val))} km/h only works for equal *times*, never equal *distances*!",
            )
            s_ar = explain_ar(
                f"السرعة المتوسطة تساوي دائماً **المسافة الكلية ÷ الزمن الكلي**! ولأن الجسم يقضي زمناً أطول في السرعة الأبطأ، "
                f"تكون الإجابة هي **الوسط التوافقي** {m('\\frac{2 v_1 v_2}{v_1 + v_2}')} وليست الوسط الحسابي {m('\\frac{v_1 + v_2}{2}')}!",
                [
                    f"نفرض طول الشوط الواحد {m(f'd = \\operatorname{{lcm}}({v1}, {v2}) = {d_smart}')} كم، فتكون المسافة الكلية {m(2 * d_smart)} كم.",
                    f"زمن الشوط الأول {m(f'{d_smart} \\div {v1} = {t1_s}')} س، وزمن الثاني {m(f'{d_smart} \\div {v2} = {t2_s}')} س، والزمن الكلي {m(t1_s + t2_s)} س.",
                    f"السرعة المتوسطة = {m(f'\\frac{{{2 * d_smart}}}{{{t1_s + t2_s}}} = {fmt_val(ans)}')} كم/س.",
                ],
                f"تنبيه مهم: الوسط الحسابي {m(fmt_val(arith_val))} كم/س فخ شهير لا يصح إلا عند تساوي الزمنين لا المسافتين!",
            )
            distractors = [
                arith_val,
                ans + 2 if isinstance(ans, int) else Fraction(ans.numerator + 10, ans.denominator),
                max(1, ans - 2) if isinstance(ans, int) else Fraction(max(1, ans.numerator - 10), ans.denominator),
                abs(v2 - v1),
            ]
        else:
            ans = v2
            v_avg = int(harm_f)
            is_round = hmode == "rev"
            svg = svg_motion_timeline("A", "B", "d" if is_round else "2d", f"v₁ = {v1}", "v₂ = ?", meet=is_round)
            q_en = (
                f"{who_en} covers {'the outgoing leg from **A** to **B**' if is_round else 'the first half of the distance from **A** to **B**'} "
                f"at {m(v1)} km/h, and {'returns from **B** to **A**' if is_round else 'completes the second half'} at a constant speed {m('v_2')} km/h. "
                f"If the **average speed** for the entire journey is {m(v_avg)} km/h, what is {m('v_2')}?"
            )
            q_ar = (
                f"يقطع ({who_ar}) {'رحلة الذهاب من **A** إلى **B**' if is_round else 'نصف المسافة الأول من **A** إلى **B**'} "
                f"بسرعة {m(v1)} كم/س، ثم {'يعود من **B** إلى **A**' if is_round else 'يكمل النصف الثاني'} بسرعة ثابتة {m('v_2')} كم/س. "
                f"إذا كانت **السرعة المتوسطة** للرحلة كاملةً هي {m(v_avg)} كم/س، فما قيمة {m('v_2')}؟"
            )
            h_en = f"Set up 2·{v1}·v₂ / ({v1} + v₂) = {v_avg}, or pick half-distance d = lcm({v1}, {v_avg}) = {math.lcm(v1, v_avg)} km!"
            h_ar = f"اكتب معادلة الوسط التوافقي 2·{v1}·v₂ / ({v1} + v₂) = {v_avg}، أو افرض مسافة الشوط d = {math.lcm(v1, v_avg)} كم!"
            trap_lin = 2 * v_avg - v1
            s_en = explain_en(
                f"Use the equal-distance average speed formula {m(f'\\frac{{2 \\times {v1} \\times v_2}}{{{v1} + v_2}} = {v_avg}')}!",
                [
                    f"Clear the denominator: {m(f'{2 * v1} v_2 = {v_avg}({v1} + v_2) = {v_avg * v1} + {v_avg} v_2')}.",
                    f"Collect {m('v_2')} terms: {m(f'({2 * v1} - {v_avg}) v_2 = {2 * v1 - v_avg} v_2 = {v_avg * v1}')}.",
                    f"Divide: {m(f'v_2 = {v_avg * v1} \\div {2 * v1 - v_avg} = {ans}')} km/h.",
                ],
                f"Trap warning: solving {m(f'({v1} + v_2)/2 = {v_avg}')} gives the wrong answer {m(trap_lin)} km/h!",
            )
            s_ar = explain_ar(
                f"نطبّق قانون السرعة المتوسطة للمسافات المتساوية: {m(f'\\frac{{2 \\times {v1} \\times v_2}}{{{v1} + v_2}} = {v_avg}')}!",
                [
                    f"نضرب طرفين في وسطين: {m(f'{2 * v1} v_2 = {v_avg}({v1} + v_2) = {v_avg * v1} + {v_avg} v_2')}.",
                    f"نجمع حدود {m('v_2')}: {m(f'{2 * v1 - v_avg} v_2 = {v_avg * v1}')}.",
                    f"نقسم فنحصل على: {m(f'v_2 = {v_avg * v1} \\div {2 * v1 - v_avg} = {ans}')} كم/س.",
                ],
                f"احذر من الفخ الحسابي {m(f'2 \\times {v_avg} - {v1} = {trap_lin}')} الناتج عن استخدام الوسط الحسابي خطأً!",
            )
            distractors = [trap_lin if trap_lin > 0 else ans + 10, ans + 5, max(5, ans - 5), v1 + v_avg]

        qid = f"KMC-T2-EX-24A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_harmonic_round_trip_speed",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 11. kmc_g89_inlet_outlet_pipe_tank (17 Qs, svg_pipe_tank)
    # ------------------------------------------------------------------
    pipe_cases = [
        ("one_in_one_out", 4, 12, 0, "hours", "ساعات", "Easy"),       # 6
        ("one_in_one_out", 6, 18, 0, "hours", "ساعات", "Easy"),       # 9
        ("one_in_one_out", 3, 6, 0, "hours", "ساعات", "Easy"),        # 6
        ("one_in_one_out", 20, 30, 0, "minutes", "دقيقة", "Easy"),    # 60
        ("one_in_one_out", 12, 15, 0, "minutes", "دقيقة", "Easy"),    # 60
        ("one_in_one_out", 10, 15, 0, "hours", "ساعات", "Medium"),    # 30
        ("one_in_one_out", 8, 12, 0, "hours", "ساعات", "Medium"),     # 24
        ("one_in_one_out", 6, 10, 0, "hours", "ساعات", "Medium"),     # 15
        ("find_leak", 4, 5, 0, "hours", "ساعات", "Medium"),           # 20
        ("find_leak", 6, 8, 0, "hours", "ساعات", "Medium"),           # 24
        ("find_leak", 3, 4, 0, "hours", "ساعات", "Medium"),           # 12
        ("two_in_one_out", 3, 6, 4, "hours", "ساعات", "Medium"),      # 4
        ("two_in_one_out", 4, 6, 12, "hours", "ساعات", "Medium"),     # 3
        ("find_leak", 5, 6, 0, "hours", "ساعات", "Hard"),             # 30
        ("two_in_one_out", 6, 12, 8, "hours", "ساعات", "Hard"),       # 8
        ("two_in_one_out", 10, 15, 12, "hours", "ساعات", "Hard"),     # 12
        ("two_in_one_out", 5, 20, 10, "hours", "ساعات", "Hard"),      # 20/3 hours (Fraction!)
    ]
    for i, (pmode, t1, t2, t3, u_en, u_ar, diff) in enumerate(pipe_cases, 1):
        if pmode == "one_in_one_out":
            net_rate = Fraction(1, t1) - Fraction(1, t2)
            assert net_rate > 0
            ans_f = Fraction(1, 1) / net_rate
            ans = int(ans_f) if ans_f.denominator == 1 else ans_f
            svg = svg_pipe_tank(f"+A ({t1})", f"−B ({t2})")
            svg_ar = svg_pipe_tank(f"+A ({t1})", f"−B ({t2})")
            L_v = math.lcm(t1, t2)
            q_en = (
                f"Inlet **Pipe A** can fill an empty water tank in {m(t1)} {u_en}, while outlet **Pipe B** at the bottom "
                f"can completely drain a full tank in {m(t2)} {u_en}. Starting with an **empty** tank, if both pipes are opened "
                f"at the same time, how many {u_en} will it take to fill the tank?"
            )
            q_ar = (
                f"يستطيع أنبوب التعبئة **A** ملء خزان فارغ خلال {m(t1)} {u_ar}، بينما يُفرغ أنبوب التصريف **B** في القاع "
                f"الخزان الممتلئ خلال {m(t2)} {u_ar}. إذا فُتح الأنبوبان معاً والخزان **فارغ**، فكم عدد الـ ({u_ar}) اللازمة لملء الخزان بالكامل؟"
            )
            h_en = f"Inlet adds +1/{t1} of the tank per unit time, while outlet subtracts −1/{t2}! Subtract the rates!"
            h_ar = f"أنبوب التعبئة يضيف 1/{t1} من الخزان في وحدة الزمن، وأنبوب التصريف ينقص 1/{t2}! اطرح المعدلين!"
            s_en = explain_en(
                "An inlet **adds** to the tank's rate while an outlet **subtracts**: "
                f"{m('\\text{Net Rate} = \\frac{1}{t_1} - \\frac{1}{t_2}')}.",
                [
                    f"Imagine the tank holds {m(f'\\operatorname{{lcm}}({t1}, {t2}) = {L_v}')} liters: Pipe A adds {m(L_v // t1)} L/{u_en[:-1]}, and Pipe B drains {m(L_v // t2)} L/{u_en[:-1]}.",
                    f"Net gain per unit time: {m(f'{L_v // t1} - {L_v // t2} = {L_v // t1 - L_v // t2}')} liters (fraction {m(fmt_val(net_rate))} of the tank).",
                    f"Total time to reach {m(L_v)} liters: {m(f'{L_v} \\div {L_v // t1 - L_v // t2} = {fmt_val(ans)}')} {u_en}.",
                ],
                f"Check: adding rates by mistake would give {m(fmt_val(Fraction(t1 * t2, t1 + t2)))}, which is faster than Pipe A alone — impossible with a leak!",
            )
            s_ar = explain_ar(
                "أنبوب التعبئة **يُضاف** معدله وأنبوب التصريف **يُطرح** معدله: "
                f"{m('\\text{المعدل الصافي} = \\frac{1}{t_1} - \\frac{1}{t_2}')}.",
                [
                    f"نفرض سعة الخزان {m(f'\\operatorname{{lcm}}({t1}, {t2}) = {L_v}')} لتراً: الأنبوب A يضيف {m(L_v // t1)} لتر، والأنبوب B يفرغ {m(L_v // t2)} لتر في كل وحدة زمن.",
                    f"الزيادة الصافية في كل وحدة زمن = {m(f'{L_v // t1} - {L_v // t2} = {L_v // t1 - L_v // t2}')} لتر.",
                    f"الزمن اللازم لملء {m(L_v)} لتراً هو {m(f'{L_v} \\div {L_v // t1 - L_v // t2} = {fmt_val(ans)}')}.",
                ],
                f"تحقق منطقي: وجود التصريف يجعل الزمن أكبر من {m(t1)}، فالإجابة {m(fmt_val(ans))} منطقية وصحيحة!",
            )
            add_trap = Fraction(t1 * t2, t1 + t2)
            distractors = [
                int(add_trap) if add_trap.denominator == 1 else add_trap,
                t2 - t1,
                t1 + t2,
                ans + 3 if isinstance(ans, int) else Fraction(ans.numerator + 3, ans.denominator),
            ]
        elif pmode == "find_leak":
            T_actual = t2
            leak_rate = Fraction(1, t1) - Fraction(1, T_actual)
            ans = int(Fraction(1, 1) / leak_rate)
            svg = svg_pipe_tank(f"+A ({t1})", "−Leak (?)")
            svg_ar = svg_pipe_tank(f"+A ({t1})", "−تسرب (؟)")
            L_v = math.lcm(t1, T_actual)
            q_en = (
                f"Inlet **Pipe A** normally fills an empty tank in {m(t1)} {u_en}. Because of a bottom leak, "
                f"filling the empty tank actually takes {m(T_actual)} {u_en}. If the tank is **full** and Pipe A is turned off, "
                f"how many {u_en} will the leak alone take to completely empty the tank?"
            )
            q_ar = (
                f"يملأ أنبوب التعبئة **A** خزاناً فارغاً في المعتاد خلال {m(t1)} {u_ar}، لكن بسبب تسرّب في القاع استغرق ملء الخزان "
                f"{m(T_actual)} {u_ar}. إذا كان الخزان **ممتلئاً** وأُغلق الأنبوب A، فكم عدد الـ ({u_ar}) التي يستغرقها التسرّب وحده لإفراغ الخزان؟"
            )
            h_en = f"Net rate = 1/{T_actual} equals (Pipe A rate 1/{t1}) − (Leak rate 1/x). Solve for 1/x = 1/{t1} − 1/{T_actual}!"
            h_ar = f"المعدل الصافي 1/{T_actual} يساوي (معدل التعبئة 1/{t1}) − (معدل التسرب 1/x). احسب 1/x = 1/{t1} − 1/{T_actual}!"
            s_en = explain_en(
                f"The difference between Pipe A's solo rate {m(f'1/{t1}')} and the slowed net rate {m(f'1/{T_actual}')} is the exact leak rate!",
                [
                    f"Set up the rate equation: {m(f'\\frac{{1}}{{{t1}}} - \\frac{{1}}{{x}} = \\frac{{1}}{{{T_actual}}} \\implies \\frac{{1}}{{x}} = \\frac{{1}}{{{t1}}} - \\frac{{1}}{{{T_actual}}}')}.",
                    f"Use common denominator {m(L_v)}: {m(f'\\frac{{1}}{{x}} = \\frac{{{L_v // t1} - {L_v // T_actual}}}{{{L_v}}} = {fmt_val(leak_rate)}')}.",
                    f"Take the reciprocal: {m(f'x = {ans}')} {u_en}.",
                ],
                f"Check: {m(f'\\frac{{1}}{{{t1}}} - \\frac{{1}}{{{ans}}} = \\frac{{1}}{{{T_actual}}}')}!",
            )
            s_ar = explain_ar(
                f"الفرق بين معدل الأنبوب A بمفرده ({m(f'1/{t1}')}) والمعدل الفعلي البطيء ({m(f'1/{T_actual}')}) يساوي معدل التسرّب!",
                [
                    f"نكتب معادلة المعدلات: {m(f'\\frac{{1}}{{x}} = \\frac{{1}}{{{t1}}} - \\frac{{1}}{{{T_actual}}}')}.",
                    f"بتوحيد المقامات على {m(L_v)}: {m(f'\\frac{{1}}{{x}} = \\frac{{{L_v // t1} - {L_v // T_actual}}}{{{L_v}}} = {fmt_val(leak_rate)}')}.",
                    f"نقلب الكسر فنجد زمن التفريغ الكامل: {m(f'x = {ans}')}.",
                ],
                f"تحقق: {m(f'\\frac{{1}}{{{t1}}} - \\frac{{1}}{{{ans}}} = \\frac{{1}}{{{T_actual}}}')}!",
            )
            distractors = [t1 * T_actual, t1 + T_actual, ans // 2, ans + 4]
        else:
            net_rate = Fraction(1, t1) + Fraction(1, t2) - Fraction(1, t3)
            assert net_rate > 0
            ans_f = Fraction(1, 1) / net_rate
            ans = int(ans_f) if ans_f.denominator == 1 else ans_f
            svg = svg_pipe_tank(f"+A({t1}), +B({t2})", f"−C ({t3})")
            svg_ar = svg_pipe_tank(f"+A({t1})، +B({t2})", f"−C ({t3})")
            L_v = math.lcm(t1, t2, t3)
            q_en = (
                f"Two inlet pipes **A** and **B** can fill an empty tank in {m(t1)} {u_en} and {m(t2)} {u_en} respectively, "
                f"while an outlet pipe **C** can empty the full tank in {m(t3)} {u_en}. If all three pipes are opened simultaneously "
                f"when the tank is empty, how many {u_en} are needed to fill it completely?"
            )
            q_ar = (
                f"يملأ أنبوبا التعبئة **A** و**B** خزاناً فارغاً في {m(t1)} {u_ar} و{m(t2)} {u_ar} على الترتيب، "
                f"بينما يفرغ أنبوب التصريف **C** الخزان الممتلئ في {m(t3)} {u_ar}. إذا فُتحت الأنابيب الثلاثة معاً "
                f"والخزان فارغ، فكم عدد الـ ({u_ar}) اللازمة لملئه تماماً؟"
            )
            h_en = f"Combine all three rates with signs: +1/{t1} + 1/{t2} − 1/{t3}, using common denominator {L_v}!"
            h_ar = f"اجمع معدلي التعبئة واطرح معدل التصريف: 1/{t1} + 1/{t2} − 1/{t3} بتوحيد المقامات على {L_v}!"
            r1_v, r2_v, r3_v = L_v // t1, L_v // t2, L_v // t3
            s_en = explain_en(
                f"Combine both inlets (+) and the outlet (−): {m('\\text{Net Rate} = \\frac{1}{t_1} + \\frac{1}{t_2} - \\frac{1}{t_3}')}.",
                [
                    f"Let the tank capacity be {m(f'\\operatorname{{lcm}}({t1},{t2},{t3}) = {L_v}')} units.",
                    f"Per {u_en[:-1]}, A adds {m(r1_v)}, B adds {m(r2_v)}, and C drains {m(r3_v)}, giving net gain {m(f'{r1_v} + {r2_v} - {r3_v} = {r1_v + r2_v - r3_v}')} units.",
                    f"Time to fill {m(L_v)} units: {m(f'\\frac{{{L_v}}}{{{r1_v + r2_v - r3_v}}} = {fmt_val(ans)}')} {u_en}.",
                ],
                f"Trap check: adding C instead of subtracting would give {m(fmt_val(Fraction(L_v, r1_v + r2_v + r3_v)))}!",
            )
            s_ar = explain_ar(
                f"نجمع معدلي أنبوبي التعبئة ونطرح معدل التصريف: {m('\\text{المعدل الصافي} = \\frac{1}{t_1} + \\frac{1}{t_2} - \\frac{1}{t_3}')}.",
                [
                    f"نفرض سعة الخزان {m(f'\\operatorname{{lcm}}({t1},{t2},{t3}) = {L_v}')} وحدة.",
                    f"في كل وحدة زمن يضيف A مقدار {m(r1_v)} ويضيف B مقدار {m(r2_v)} ويفرغ C مقدار {m(r3_v)}؛ الصافي = {m(f'{r1_v} + {r2_v} - {r3_v} = {r1_v + r2_v - r3_v}')}.",
                    f"زمن امتلاء الخزان = {m(f'\\frac{{{L_v}}}{{{r1_v + r2_v - r3_v}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق: المعدل الصافي يساوي {m(fmt_val(net_rate))} من الخزان لكل وحدة زمن، ومقلوبه {m(fmt_val(ans))}!",
            )
            add_all = Fraction(L_v, r1_v + r2_v + r3_v)
            distractors = [
                int(add_all) if add_all.denominator == 1 else add_all,
                ans + 2 if isinstance(ans, int) else Fraction(ans.numerator + 2, ans.denominator),
                max(1, ans - 1) if isinstance(ans, int) else Fraction(max(1, ans.numerator - 2), ans.denominator),
                t1 + t2 - t3 if t1 + t2 - t3 > 0 else t3,
            ]

        qid = f"KMC-T2-EX-24B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_inlet_outlet_pipe_tank",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 12. kmc_g89_league_table_points (16 Qs)
    # ------------------------------------------------------------------
    league_cases = [
        ("total_pts", 4, 2, None, "Easy"),
        ("total_pts", 5, 3, None, "Easy"),
        ("total_pts", 6, 4, None, "Easy"),
        ("total_pts", 7, 5, None, "Easy"),
        ("total_pts", 8, 6, None, "Easy"),
        ("total_pts", 10, 9, None, "Medium"),
        ("find_draws", 5, 4, None, "Medium"),
        ("find_draws", 6, 5, None, "Medium"),
        ("find_draws", 7, 6, None, "Medium"),
        ("find_draws", 8, 7, None, "Medium"),
        ("find_draws", 9, 8, None, "Medium"),
        ("last_team", 4, 2, [7, 4, 3], "Medium"),       # M=6, P=18-2=16 -> last = 2
        ("last_team", 5, 3, [10, 7, 5, 3], "Medium"),   # M=10, P=30-3=27 -> last = 2
        ("find_draws", 10, 11, None, "Hard"),
        ("last_team", 6, 4, [13, 10, 8, 6, 2], "Hard"), # M=15, P=45-4=41 -> last = 2
        ("ratio_draws", 8, 7, 3, "Hard"),               # M=28, decisive = 3 * draws -> 4D = 28 -> D=7, ask Total Points = 84-7=77!
    ]
    for i, (lmode, n, draws, extra, diff) in enumerate(league_cases, 1):
        M = n * (n - 1) // 2
        P = 3 * M - draws
        assert 0 <= draws <= M

        if lmode == "total_pts":
            ans = P
            q_en = (
                f"In a single round-robin football tournament with {m(n)} teams, every pair of teams plays **exactly once**. "
                f"A win awards {m(3)} points to the winner and {m(0)} to the loser, while a draw awards {m(1)} point to **each** of the two teams. "
                f"If exactly {m(draws)} games ended in a draw, what is the **sum of points of all {m(n)} teams** at the end?"
            )
            q_ar = (
                f"في بطولة كرة قدم بنظام الدوري من دور واحد بين {m(n)} فرق، يلعب كل فريقين معاً **مباراة واحدة فقط**. "
                f"يُمنح الفائز {m(3)} نقاط والخاسر {m(0)}، وفي حالة التعادل يحصل **كل فريق** على نقطة واحدة ({m(1)}). "
                f"إذا انتهت {m(draws)} مباريات بالتعادل، فما **مجموع نقاط الفرق الـ {m(n)} جميعها** في نهاية البطولة؟"
            )
            h_en = f"First count total matches C({n}, 2) = {M}. Each decisive match adds 3 total points, while each draw adds 1 + 1 = 2 total points!"
            h_ar = f"احسب أولاً عدد المباريات الكلي C({n}, 2) = {M}. كل مباراة حاسمة تضيف 3 نقاط للمجموع، وكل تعادل يضيف 1 + 1 = 2 نقطة!"
            s_en = explain_en(
                "Invariant trick: every decisive game adds \\( 3 + 0 = 3 \\) points to the league table, whereas every draw adds \\( 1 + 1 = 2 \\) points (1 point less) — so \\( \\text{Total Points} = 3M - \\text{Draws} \\)!",
                [
                    f"Total matches played: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}.",
                    f"If all {m(M)} matches had a winner, the table would have {m(f'3 \\times {M} = {3 * M}')} points.",
                    f"Each of the {m(draws)} draws reduces the total by {m(1)} point: {m(f'{3 * M} - {draws} = {ans}')} points.",
                ],
                f"Direct check: {m(M - draws)} decisive games ({m(3 * (M - draws))} pts) + {m(draws)} draws ({m(2 * draws)} pts) = {m(ans)} pts!",
            )
            s_ar = explain_ar(
                "ثابت جدول الدوري: كل مباراة تنتهي بفوز تضيف \\( 3 + 0 = 3 \\) نقاط للمجموع، وكل تعادل يضيف \\( 1 + 1 = 2 \\) نقطة (أقل بنقطة واحدة) — إذن \\( \\text{مجموع النقاط} = 3M - \\text{عدد التعادلات} \\)!",
                [
                    f"إجمالي عدد المباريات: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')} مباراة.",
                    f"لو انتهت جميع المباريات بفوز لكان المجموع {m(f'3 \\times {M} = {3 * M}')} نقطة.",
                    f"نطرح نقطة واحدة عن كل تعادل من التعادلات الـ {m(draws)}: {m(f'{3 * M} - {draws} = {ans}')} نقطة.",
                ],
                f"تحقق مباشر: {m(M - draws)} مباريات حاسمة ({m(3 * (M - draws))} نقطة) + {m(draws)} تعادلات ({m(2 * draws)} نقطة) = {m(ans)} نقطة!",
            )
            distractors = [3 * M, 3 * M - 2 * draws, 2 * M + draws, ans + 2]
        elif lmode == "find_draws":
            ans = draws
            q_en = (
                f"In a tournament of {m(n)} teams where every pair plays **once** ({m(3)} points for a win, {m(1)} point to each team for a draw, "
                f"{m(0)} for a loss), the final league table shows that the sum of all teams' points is {m(P)}. "
                f"How many games in the tournament ended in a **draw**?"
            )
            q_ar = (
                f"في بطولة تضم {m(n)} فرق يلعب فيها كل فريقين معاً **مرة واحدة** ({m(3)} نقاط للفوز، ونقطة واحدة لكل فريق عند التعادل، "
                f"وصفر للخسارة)، بلغ مجموع نقاط جميع الفرق في الجدول النهائي {m(P)} نقطة. "
                f"كم مباراة في البطولة انتهت **بالتعادل**؟"
            )
            h_en = f"Compare the maximum possible total points 3 × C({n}, 2) = {3 * M} with the actual total {P}! Every missing point is 1 draw!"
            h_ar = f"قارن أقصى مجموع نقاط ممكن 3 × C({n}, 2) = {3 * M} بالمجموع الفعلي {P}! كل نقطة ناقصة تمثّل مباراة تعادل واحدة!"
            s_en = explain_en(
                "Since each draw gives \\( 2 \\) total points instead of \\( 3 \\), every single point missing from \\( 3 \\times \\binom{n}{2} \\) corresponds to **exactly one draw**!",
                [
                    f"Count total games: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}.",
                    f"Maximum possible point sum (zero draws): {m(f'3 \\times {M} = {3 * M}')}.",
                    f"Number of draws = {m(f'{3 * M} - {P} = {ans}')}.",
                ],
                f"Check: {m(M - ans)} wins ({m(3 * (M - ans))} pts) + {m(ans)} draws ({m(2 * ans)} pts) = {m(P)} pts!",
            )
            s_ar = explain_ar(
                "لأن كل تعادل يمنح نقطتين بدلاً من 3 نقاط، فإن كل نقطة ينقصها المجموع الفعلي عن \\( 3 \\times \\binom{n}{2} \\) تقابل **تعادلاً واحداً بالضبط**!",
                [
                    f"عدد المباريات الكلي: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}.",
                    f"أقصى مجموع نقاط ممكن (بدون تعادلات): {m(f'3 \\times {M} = {3 * M}')}.",
                    f"عدد مباريات التعادل = {m(f'{3 * M} - {P} = {ans}')}.",
                ],
                f"تحقق: {m(M - ans)} انتصارات ({m(3 * (M - ans))} نقطة) + {m(ans)} تعادلات ({m(2 * ans)} نقطة) = {m(P)} نقطة!",
            )
            distractors = [(3 * M - P) // 2 if ans > 2 else ans + 3, M - draws, ans + 2, max(1, ans - 2)]
        elif lmode == "last_team":
            known_scores = extra
            assert len(known_scores) == n - 1
            ans = P - sum(known_scores)
            assert ans >= 0
            sc_str = ", ".join(str(x) for x in known_scores)
            q_en = (
                f"In a single round-robin league of {m(n)} teams ({m(3)} pts for a win, {m(1)} pt each for a draw, {m(0)} for a loss), "
                f"exactly {m(draws)} matches ended in a draw. The final point totals of {m(n - 1)} of the teams are {m(sc_str)}. "
                f"How many points did the **{m(f'{n}\\text{{th}}')} team** score?"
            )
            q_ar = (
                f"في دوري من دور واحد يضم {m(n)} فرق ({m(3)} نقاط للفوز، ونقطة واحدة لكل فريق عند التعادل، وصفر للخسارة)، "
                f"انتهت {m(draws)} مباريات بالتعادل. إذا كانت حصيلة نقاط {m(n - 1)} من الفرق هي {m(sc_str)}، "
                f"فكم نقطة أحرز **الفريق رقم {m(n)}**؟"
            )
            h_en = f"First find the total points across all {n} teams using 3 × C({n}, 2) − {draws}, then subtract the {n - 1} known scores!"
            h_ar = f"أوجد أولاً مجموع نقاط الفرق الـ {n} بالقانون 3 × C({n}, 2) − {draws}، ثم اطرح نقاط الفرق المعلومة!"
            s_en = explain_en(
                "Use the league-table point invariant \\( P = 3\\binom{n}{2} - \\text{Draws} \\) to find the sum of all teams' scores first!",
                [
                    f"Total games {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}, so total points across all teams = {m(f'3 \\times {M} - {draws} = {P}')}.",
                    f"Sum of the {m(n - 1)} given teams' scores: {m(' + '.join(str(x) for x in known_scores) + f' = {sum(known_scores)}')}.",
                    f"Remaining team's score: {m(f'{P} - {sum(known_scores)} = {ans}')}.",
                ],
                f"Check: {m(f'{sum(known_scores)} + {ans} = {P} = 3({M}) - {draws}')}!",
            )
            s_ar = explain_ar(
                "نحسب أولاً المجموع الكلي لنقاط الجدول بالقانون \\( P = 3\\binom{n}{2} - \\text{التعادلات} \\) ثم نطرح النقاط المعلومة!",
                [
                    f"عدد المباريات {m(f'M = {M}')}، فيكون مجموع نقاط جميع الفرق = {m(f'3 \\times {M} - {draws} = {P}')}.",
                    f"مجموع نقاط الفرق الـ {m(n - 1)} المعلومة: {m(sum(known_scores))}.",
                    f"نقاط الفريق الأخير = {m(f'{P} - {sum(known_scores)} = {ans}')}.",
                ],
                f"تحقق: {m(f'{sum(known_scores)} + {ans} = {P}')}!",
            )
            distractors = [ans + draws, ans + 1, ans + 3, max(0, ans - 1)]
        else:
            mult = extra
            assert M == (mult + 1) * draws
            ans = P
            q_en = (
                f"In a single round-robin tournament of {m(n)} teams ({m(3)} pts win, {m(1)} pt each draw, {m(0)} loss), "
                f"the number of decisive games (games with a winner) was **{m(mult)} times** the number of draws. "
                f"What was the **total sum of points** across all {m(n)} teams?"
            )
            q_ar = (
                f"في بطولة دوري من دور واحد تضم {m(n)} فرق ({m(3)} نقاط للفوز، ونقطة لكل فريق عند التعادل، وصفر للخسارة)، "
                f"كان عدد المباريات الحاسمة (التي انتهت بفوز أحد الفريقين) يساوي **{m(mult)} أمثال** عدد مباريات التعادل. "
                f"ما **المجموع الكلي لنقاط** الفرق الـ {m(n)} جميعها؟"
            )
            h_en = f"Total matches M = C({n}, 2) = {M}. If draws = D, then {mult}D + D = {M}. Find D, then compute 3M − D!"
            h_ar = f"عدد المباريات الكلي M = C({n}, 2) = {M}. بفرض عدد التعادلات D يكون {mult}D + D = {M}. أوجد D ثم احسب 3M − D!"
            s_en = explain_en(
                "Find total matches \\( M = \\binom{n}{2} \\), split \\( M \\) in the given ratio to find draws \\( D \\), then apply \\( P = 3M - D \\)!",
                [
                    f"Total matches: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}.",
                    f"Let {m('D')} be the number of draws; then {m(f'{mult}D + D = {mult + 1}D = {M} \\implies D = {draws}')}.",
                    f"Total points = {m(f'3 \\times {M} - {draws} = {3 * M} - {draws} = {ans}')}.",
                ],
                f"Check: {m(mult * draws)} decisive games ({m(3 * mult * draws)} pts) + {m(draws)} draws ({m(2 * draws)} pts) = {m(ans)} pts!",
            )
            s_ar = explain_ar(
                "نوجد إجمالي المباريات \\( M = \\binom{n}{2} \\)، ثم نقسّمها لإيجاد عدد التعادلات \\( D \\)، ثم نطبّق \\( P = 3M - D \\)!",
                [
                    f"عدد المباريات الكلي: {m(f'M = \\frac{{{n} \\times {n - 1}}}{{2}} = {M}')}.",
                    f"بفرض عدد التعادلات {m('D')} يكون {m(f'{mult}D + D = {mult + 1}D = {M} \\implies D = {draws}')}.",
                    f"مجموع النقاط الكلي = {m(f'3 \\times {M} - {draws} = {3 * M} - {draws} = {ans}')}.",
                ],
                f"تحقق: {m(mult * draws)} فوزاً ({m(3 * mult * draws)} نقطة) + {m(draws)} تعادلات ({m(2 * draws)} نقطة) = {m(ans)} نقطة!",
            )
            distractors = [3 * M, 3 * M - 2 * draws, ans - 3, ans + 3]

        qid = f"KMC-T2-EX-24C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        if lmode == "total_pts":
            lg_rows_en = [["Win / Draw", "3 / 2", f"D = {draws}"], ["All Teams", f"n = {n}", "Total = ?"]]
            lg_rows_ar = [["فوز / تعادل", "3 / 2", f"تعادل = {draws}"], ["جميع الفرق", f"n = {n}", "المجموع = ؟"]]
        elif lmode == "find_draws":
            lg_rows_en = [["Win / Draw", "3 / 2", "D = ?"], ["All Teams", f"n = {n}", f"Total = {P}"]]
            lg_rows_ar = [["فوز / تعادل", "3 / 2", "تعادل = ؟"], ["جميع الفرق", f"n = {n}", f"المجموع = {P}"]]
        elif lmode == "last_team":
            sc_short = ",".join(str(x) for x in known_scores)
            lg_rows_en = [[f"{n-1} Teams", sc_short, f"D = {draws}"], [f"Team #{n}", "?", "Pts = ?"]]
            lg_rows_ar = [[f"{n-1} فرق", sc_short, f"تعادل = {draws}"], [f"الفريق {n}", "؟", "النقاط = ؟"]]
        else:
            lg_rows_en = [["Wins : Draws", f"{mult} : 1", f"n = {n}"], ["All Teams", "3 / 2", "Total = ?"]]
            lg_rows_ar = [["فوز : تعادل", f"{mult} : 1", f"n = {n}"], ["جميع الفرق", "3 / 2", "المجموع = ؟"]]
        svg_en = svg_score_table(["Item", "Pts", "Stat"], lg_rows_en, title_lbl=f"League of {n} teams")
        svg_ar = svg_score_table(["البند", "النقاط", "الإحصائية"], lg_rows_ar, title_lbl=f"دوري من {n} فرق")
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_league_table_points",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(out) == 50
    return out


def _gen_lesson_2_5() -> list[dict]:
    out: list[dict] = []
    topic = "Geometry"

    # ------------------------------------------------------------------
    # 13. kmc_g89_thales_semicircle_angles (17 Qs, svg_thales_circle)
    # ------------------------------------------------------------------
    thales_cases = [
        ("ang_b", 34, 0, "Easy"),
        ("ang_b", 27, 0, "Easy"),
        ("ang_b", 41, 0, "Easy"),
        ("find_radius", 6, 8, "Easy"),
        ("find_radius", 10, 24, "Easy"),
        ("central_cob", 32, 0, "Medium"),
        ("central_cob", 38, 0, "Medium"),
        ("from_aoc", 116, 0, "Medium"),
        ("from_aoc", 104, 0, "Medium"),
        ("find_chord", 5, 8, "Medium"),
        ("find_chord", 13, 10, "Medium"),
        ("find_area", 5, 6, "Medium"),
        ("find_area", 17, 16, "Medium"),
        ("find_area", 25, 14, "Hard"),
        ("find_alt", 15, 20, "Hard"),
        ("find_alt", 30, 40, "Hard"),
        ("find_alt", 9, 12, "Hard"),
    ]
    for i, (tmode, p1, p2, diff) in enumerate(thales_cases, 1):
        if tmode == "ang_b":
            alpha = p1
            ans = 90 - alpha
            svg = svg_thales_circle(f"{alpha}°", "x°")
            q_en = (
                f"In the circle with center {m('O')} shown, segment {m('AB')} is a **diameter** and point {m('C')} lies on the circle. "
                f"If {m(f'\\angle CAB = {alpha}^\\circ')}, what is the measure of {m('\\angle CBA')} (in degrees)?"
            )
            q_ar = (
                f"في الدائرة التي مركزها {m('O')} الموضّحة، القطعة {m('AB')} هي **قطر** للدائرة والنقطة {m('C')} تقع على محيطها. "
                f"إذا كان {m(f'\\angle CAB = {alpha}^\\circ')}، فما قياس الزاوية {m('\\angle CBA')} (بالدرجات)؟"
            )
            h_en = "By Thales' Theorem, any angle inscribed in a semicircle is a right angle: ∠ACB = 90°!"
            h_ar = "حسب مبرهنة طاليس، الزاوية المحيطية المرسومة في نصف دائرة قائمة دائماً: ∠ACB = 90°!"
            s_en = explain_en(
                "By **Thales' Theorem**, since \\( AB \\) is a diameter and \\( C \\) lies on the circle, \\( \\angle ACB = 90^\\circ \\)!",
                [
                    f"In right triangle {m('\\triangle ABC')}, the two acute angles at {m('A')} and {m('B')} sum to {m('90^\\circ')}.",
                    f"Subtract: {m(f'\\angle CBA = 90^\\circ - {alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"Angle-sum check: {m(f'{alpha}^\\circ + 90^\\circ + {ans}^\\circ = 180^\\circ')}!",
            )
            s_ar = explain_ar(
                "حسب **مبرهنة طاليس**، بما أن \\( AB \\) قطر والنقطة \\( C \\) على محيط الدائرة، فإن \\( \\angle ACB = 90^\\circ \\)!",
                [
                    f"في المثلث القائم {m('\\triangle ABC')}، مجموع الزاويتين الحادتين عند {m('A')} و{m('B')} يساوي {m('90^\\circ')}.",
                    f"إذن {m(f'\\angle CBA = 90^\\circ - {alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"تحقق من مجموع زوايا المثلث: {m(f'{alpha}^\\circ + 90^\\circ + {ans}^\\circ = 180^\\circ')}!",
            )
            distractors = [180 - alpha, 2 * alpha, 90 - 2 * alpha if 90 - 2 * alpha > 0 else alpha + 10, ans + 10]
        elif tmode == "central_cob":
            alpha = p1
            ans = 2 * alpha
            svg = svg_thales_circle(f"{alpha}°", "∠COB")
            q_en = (
                f"In the circle with center {m('O')} and diameter {m('AB')}, point {m('C')} lies on the circle such that "
                f"{m(f'\\angle CAB = {alpha}^\\circ')}. What is the measure of the **central angle** {m('\\angle COB')} (in degrees)?"
            )
            q_ar = (
                f"في الدائرة ذات المركز {m('O')} والقطر {m('AB')}، تقع النقطة {m('C')} على الدائرة بحيث يكون "
                f"{m(f'\\angle CAB = {alpha}^\\circ')}. ما قياس **الزاوية المركزية** {m('\\angle COB')} (بالدرجات)؟"
            )
            h_en = "Draw radius OC! Since OA = OC = radius, triangle OAC is isosceles with ∠OCA = ∠OAC!"
            h_ar = "ارسم نصف القطر OC! بما أن OA = OC (أنصاف أقطار)، فالمثلث OAC متطابق الضلعين وفيه ∠OCA = ∠OAC!"
            s_en = explain_en(
                "Radii \\( OA \\) and \\( OC \\) are equal, making \\( \\triangle OAC \\) **isosceles**!",
                [
                    f"Since {m('OA = OC')}, base angles are equal: {m(f'\\angle OCA = \\angle OAC = {alpha}^\\circ')}.",
                    f"Angle {m('\\angle COB')} is the exterior angle to {m('\\triangle OAC')} at {m('O')}, so {m(f'\\angle COB = {alpha}^\\circ + {alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"This also confirms the Inscribed Angle Theorem on arc {m('CB')}: {m(f'\\angle COB = 2 \\angle CAB = {ans}^\\circ')}!",
            )
            s_ar = explain_ar(
                "بما أن \\( OA = OC \\) أنصاف أقطار متساوية، فإن المثلث \\( \\triangle OAC \\) **متطابق الضلعين**!",
                [
                    f"زاويتا القاعدة متساويتان: {m(f'\\angle OCA = \\angle OAC = {alpha}^\\circ')}.",
                    f"الزاوية {m('\\angle COB')} زاوية خارجية للمثلث {m('\\triangle OAC')} عند {m('O')}، فتساوي {m(f'{alpha}^\\circ + {alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"وهذا يطابق أيضاً نظرية الزاوية المركزية والمحيطية المشتركتين في القوس {m('CB')}: {m(f'2 \\times {alpha}^\\circ = {ans}^\\circ')}!",
            )
            distractors = [90 - alpha, 180 - 2 * alpha, alpha, ans + 8]
        elif tmode == "from_aoc":
            aoc = p1
            cab = (180 - aoc) // 2
            ans = 90 - cab
            svg = svg_thales_circle(f"∠AOC={aoc}°", "x°")
            q_en = (
                f"Segment {m('AB')} is a diameter of a circle with center {m('O')}, and point {m('C')} lies on the circle. "
                f"If the central angle {m(f'\\angle AOC = {aoc}^\\circ')}, what is the measure of {m('\\angle CBA')} (in degrees)?"
            )
            q_ar = (
                f"القطعة {m('AB')} قطر في دائرة مركزها {m('O')}، والنقطة {m('C')} تقع على محيطها. "
                f"إذا كان قياس الزاوية المركزية {m(f'\\angle AOC = {aoc}^\\circ')}، فما قياس الزاوية {m('\\angle CBA')} (بالدرجات)؟"
            )
            h_en = f"First find ∠COB = 180° − {aoc}° on the straight diameter AB, then use isosceles triangle OBC (OB = OC)!"
            h_ar = f"استخدم أولاً زاوية الخط المستقيم AB لإيجاد ∠COB = 180° − {aoc}°، أو المثلث متطابق الضلعين OAC!"
            s_en = explain_en(
                "In isosceles \\( \\triangle OAC \\) (\\( OA = OC \\)), we find \\( \\angle CAB \\), then use Thales' right angle \\( \\angle ACB = 90^\\circ \\)!",
                [
                    f"In isosceles {m('\\triangle OAC')}: {m(f'\\angle CAB = \\frac{{180^\\circ - {aoc}^\\circ}}{{2}} = {cab}^\\circ')}.",
                    f"By Thales' Theorem {m('\\angle ACB = 90^\\circ')}, so {m(f'\\angle CBA = 90^\\circ - {cab}^\\circ = {ans}^\\circ')}.",
                ],
                f"Shortcut check: inscribed {m('\\angle CBA')} subtends arc {m('AC')}, so {m(f'\\angle CBA = \\frac{{1}}{{2}} \\angle AOC = {aoc}^\\circ \\div 2 = {ans}^\\circ')}!",
            )
            s_ar = explain_ar(
                "نوجد \\( \\angle CAB \\) من المثلث متطابق الضلعين \\( \\triangle OAC \\)، ثم نطرح من \\( 90^\\circ \\) حسب مبرهنة طاليس!",
                [
                    f"في المثلث متطابق الضلعين {m('\\triangle OAC')}: {m(f'\\angle CAB = \\frac{{180^\\circ - {aoc}^\\circ}}{{2}} = {cab}^\\circ')}.",
                    f"وبما أن {m('\\angle ACB = 90^\\circ')}، فإن {m(f'\\angle CBA = 90^\\circ - {cab}^\\circ = {ans}^\\circ')}.",
                ],
                f"طريقة سريعة للتحقق: المحيطية {m('\\angle CBA')} تقابل القوس {m('AC')} فتساوي نصف المركزية: {m(f'{aoc}^\\circ \\div 2 = {ans}^\\circ')}!",
            )
            distractors = [cab, 180 - aoc, 90 - (180 - aoc), ans + 6]
        elif tmode == "find_radius":
            ac, bc = p1, p2
            ab = math.isqrt(ac * ac + bc * bc)
            assert ab * ab == ac * ac + bc * bc and ab % 2 == 0
            ans = ab // 2
            svg = svg_thales_circle(f"AC={ac}", f"BC={bc}")
            q_en = (
                f"Point {m('C')} lies on a circle with diameter {m('AB')} and center {m('O')}, as shown. "
                f"If chords {m(f'AC = {ac}')} cm and {m(f'BC = {bc}')} cm, what is the **radius** {m('OA')} of the circle (in cm)?"
            )
            q_ar = (
                f"تقع النقطة {m('C')} على دائرة قطرها {m('AB')} ومركزها {m('O')} كما في الشكل. "
                f"إذا كان طول الوتر {m(f'AC = {ac}')} سم وطول الوتر {m(f'BC = {bc}')} سم، فما **نصف قطر** الدائرة {m('OA')} (بالسم)؟"
            )
            h_en = "By Thales' Theorem ∠ACB = 90°! Find the hypotenuse AB by Pythagoras, then DIVIDE BY 2 for the radius!"
            h_ar = "حسب مبرهنة طاليس ∠ACB = 90°! أوجد طول القطر AB بنظرية فيثاغورس، ثم اقسم على 2 لإيجاد نصف القطر!"
            s_en = explain_en(
                "Since \\( AB \\) is a diameter, \\( \\angle ACB = 90^\\circ \\), making \\( AB \\) the hypotenuse of right triangle \\( \\triangle ABC \\).",
                [
                    f"Apply the Pythagorean Theorem: {m(f'AB^2 = {ac}^2 + {bc}^2 = {ac*ac} + {bc*bc} = {ab*ab} \\implies AB = {ab}')} cm.",
                    f"Divide the diameter by {m(2)} to get the radius: {m(f'R = {ab} \\div 2 = {ans}')} cm.",
                ],
                f"Famous KMC trap avoided: {m(ab)} cm is the **diameter**, while {m(ans)} cm is the **radius**!",
            )
            s_ar = explain_ar(
                "بما أن \\( AB \\) قطر، فإن \\( \\angle ACB = 90^\\circ \\)، ويكون \\( AB \\) وتر المثلث القائم \\( \\triangle ABC \\).",
                [
                    f"نطبّق نظرية فيثاغورس: {m(f'AB^2 = {ac}^2 + {bc}^2 = {ac*ac} + {bc*bc} = {ab*ab} \\implies AB = {ab}')} سم.",
                    f"نقسم القطر على {m(2)} للحصول على نصف القطر: {m(f'R = {ab} \\div 2 = {ans}')} سم.",
                ],
                f"احذر من الفخ الشهير: العدد {m(ab)} هو القطر كاملاً، أما نصف القطر المطلوب فهو {m(ans)} سم!",
            )
            distractors = [ab, (ac + bc) // 2, ans + 2, max(1, ans - 1)]
        elif tmode == "find_chord":
            R, ac = p1, p2
            ab = 2 * R
            bc = math.isqrt(ab * ab - ac * ac)
            assert bc * bc == ab * ab - ac * ac
            ans = bc
            svg = svg_thales_circle(f"AC={ac}", "BC=?")
            q_en = (
                f"A circle with center {m('O')} has **radius** {m(R)} cm, and {m('AB')} is a diameter. "
                f"Point {m('C')} lies on the circle with chord {m(f'AC = {ac}')} cm. What is the length of chord {m('BC')} (in cm)?"
            )
            q_ar = (
                f"دائرة مركزها {m('O')} **نصف قطرها** {m(R)} سم، و{m('AB')} قطر فيها. "
                f"تقع النقطة {m('C')} على الدائرة بحيث طول الوتر {m(f'AC = {ac}')} سم. ما طول الوتر {m('BC')} (بالسم)؟"
            )
            h_en = f"First double the radius to get diameter AB = {ab} cm, then use ∠ACB = 90° and Pythagoras!"
            h_ar = f"ضاعف نصف القطر أولاً لإيجاد القطر AB = {ab} سم، ثم استخدم الزاوية القائمة ∠ACB = 90° ونظرية فيثاغورس!"
            s_en = explain_en(
                "Double the radius to get hypotenuse \\( AB = 2R \\), then apply Pythagoras in right \\( \\triangle ABC \\) (\\( \\angle ACB = 90^\\circ \\)).",
                [
                    f"Diameter {m(f'AB = 2 \\times {R} = {ab}')} cm.",
                    f"In right {m('\\triangle ABC')}: {m(f'BC^2 = AB^2 - AC^2 = {ab}^2 - {ac}^2 = {ab*ab} - {ac*ac} = {bc*bc}')}.",
                    f"Take the square root: {m(f'BC = {ans}')} cm.",
                ],
                f"Check: {m(f'{ac}^2 + {ans}^2 = {ac*ac + ans*ans} = {ab}^2')}!",
            )
            s_ar = explain_ar(
                "نضاعف نصف القطر لإيجاد القطر \\( AB = 2R \\)، ثم نطبّق فيثاغورس في المثلث القائم \\( \\triangle ABC \\).",
                [
                    f"طول القطر: {m(f'AB = 2 \\times {R} = {ab}')} سم.",
                    f"في المثلث القائم {m('\\triangle ABC')}: {m(f'BC^2 = {ab}^2 - {ac}^2 = {ab*ab} - {ac*ac} = {bc*bc}')}.",
                    f"بأخذ الجذر التربيعي: {m(f'BC = {ans}')} سم.",
                ],
                f"تحقق: {m(f'{ac}^2 + {ans}^2 = {ab}^2')}!",
            )
            distractors = [ab - ac, ans + 2, max(1, ans - 2), R + ac // 2]
        elif tmode == "find_area":
            R, ac = p1, p2
            ab = 2 * R
            bc = math.isqrt(ab * ab - ac * ac)
            assert bc * bc == ab * ab - ac * ac
            ans = (ac * bc) // 2
            svg = svg_thales_circle(f"AC={ac}", f"R={R}")
            q_en = (
                f"Point {m('C')} lies on a circle of **radius** {m(R)} cm with diameter {m('AB')}. "
                f"If chord {m(f'AC = {ac}')} cm, what is the **area** of triangle {m('ABC')} (in {m('\\text{cm}^2')})?"
            )
            q_ar = (
                f"تقع النقطة {m('C')} على دائرة **نصف قطرها** {m(R)} سم وقطرها {m('AB')}. "
                f"إذا كان طول الوتر {m(f'AC = {ac}')} سم، فما **مساحة** المثلث {m('ABC')} (بوحدة {m('\\text{cm}^2')})؟"
            )
            h_en = f"Since ∠ACB = 90°, legs AC and BC are perpendicular! Find AB = 2R = {ab}, then BC by Pythagoras, then Area = ½·AC·BC."
            h_ar = f"بما أن ∠ACB = 90° فإن الضلعين AC و BC متعامدان! احسب القطر AB = {ab}، ثم BC بفيثاغورس، ثم المساحة = ½·AC·BC."
            s_en = explain_en(
                "By Thales' Theorem \\( \\angle ACB = 90^\\circ \\), so the area of \\( \\triangle ABC \\) is simply \\( \\frac{1}{2} \\times AC \\times BC \\)!",
                [
                    f"Diameter {m(f'AB = 2 \\times {R} = {ab}')} cm.",
                    f"Find the second leg by Pythagoras: {m(f'BC = \\sqrt{{{ab}^2 - {ac}^2}} = \\sqrt{{{ab*ab - ac*ac}}} = {bc}')} cm.",
                    f"Compute area: {m(f'\\frac{{1}}{{2}} \\times {ac} \\times {bc} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"Trap avoided: forgetting the {m('\\frac{1}{2}')} factor gives {m(ac * bc)}, and using {m('AB')} instead of {m('BC')} gives {m((ac * ab) // 2)}!",
            )
            s_ar = explain_ar(
                "بما أن \\( \\angle ACB = 90^\\circ \\) حسب مبرهنة طاليس، فإن مساحة المثلث تساوي \\( \\frac{1}{2} \\times AC \\times BC \\)!",
                [
                    f"طول القطر {m(f'AB = 2 \\times {R} = {ab}')} سم.",
                    f"نحسب الضلع القائم الثاني بفيثاغورس: {m(f'BC = \\sqrt{{{ab}^2 - {ac}^2}} = {bc}')} سم.",
                    f"مساحة المثلث = {m(f'\\frac{{1}}{{2}} \\times {ac} \\times {bc} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"احذر من نسيان الضرب في {m('\\frac{1}{2}')} ({m(ac * bc)}) أو استخدام الوتر بدلاً من الضلع القائم!",
            )
            distractors = [ac * bc, (ac * ab) // 2, ans + ac, max(1, ans - bc)]
        else:
            ac, bc = p1, p2
            ab = math.isqrt(ac * ac + bc * bc)
            assert ab * ab == ac * ac + bc * bc
            ans_f = Fraction(ac * bc, ab)
            ans = int(ans_f) if ans_f.denominator == 1 else ans_f
            svg = svg_thales_circle(f"AC={ac}", f"BC={bc}")
            q_en = (
                f"Point {m('C')} lies on a semicircle with diameter {m('AB')}. Given that chords {m(f'AC = {ac}')} cm "
                f"and {m(f'BC = {bc}')} cm, what is the **perpendicular distance** from {m('C')} to the diameter {m('AB')} (in cm)?"
            )
            q_ar = (
                f"تقع النقطة {m('C')} على نصف دائرة قطرها {m('AB')}. إذا كان {m(f'AC = {ac}')} سم "
                f"و{m(f'BC = {bc}')} سم، فما **البعد العمودي** من النقطة {m('C')} إلى القطر {m('AB')} (بالسم)؟"
            )
            h_en = "Express the area of right triangle ABC in TWO ways: ½·AC·BC = ½·AB·h!"
            h_ar = "عبّر عن مساحة المثلث القائم ABC بطريقتين مختلفتين: ½·AC·BC = ½·AB·h!"
            s_en = explain_en(
                "Two-way area trick in right \\( \\triangle ABC \\): \\( \\frac{1}{2} AC \\cdot BC = \\frac{1}{2} AB \\cdot h \\implies h = \\frac{AC \\cdot BC}{AB} \\)!",
                [
                    f"By Thales' Theorem {m('\\angle ACB = 90^\\circ')}, so {m(f'AB = \\sqrt{{{ac}^2 + {bc}^2}} = {ab}')} cm.",
                    f"Equate double-areas: {m(f'{ab} \\times h = {ac} \\times {bc} = {ac * bc}')}.",
                    f"Solve for altitude {m('h')}: {m(f'h = \\frac{{{ac * bc}}}{{{ab}}} = {fmt_val(ans)}')} cm.",
                ],
                f"Sanity check: the altitude {m(fmt_val(ans))} is strictly shorter than the shorter leg {m(min(ac, bc))}!",
            )
            s_ar = explain_ar(
                "حيلة المساحة بطريقتين في المثلث القائم \\( \\triangle ABC \\): \\( \\frac{1}{2} AC \\cdot BC = \\frac{1}{2} AB \\cdot h \\implies h = \\frac{AC \\cdot BC}{AB} \\)!",
                [
                    f"بمبرهنة طاليس {m('\\angle ACB = 90^\\circ')}، ومن فيثاغورس {m(f'AB = \\sqrt{{{ac}^2 + {bc}^2}} = {ab}')} سم.",
                    f"بمساواة ضعفي المساحة: {m(f'{ab} \\times h = {ac} \\times {bc} = {ac * bc}')}.",
                    f"الارتفاع العمودي {m(f'h = \\frac{{{ac * bc}}}{{{ab}}} = {fmt_val(ans)}')} سم.",
                ],
                f"تحقق منطقي: الارتفاع {m(fmt_val(ans))} أصغر من أصغر ضلع قائم ({m(min(ac, bc))})!",
            )
            distractors = [
                ab // 2 if ab % 2 == 0 else Fraction(ab, 2),
                ans + 2 if isinstance(ans, int) else Fraction(ans.numerator + 4, ans.denominator),
                max(1, ans - 2) if isinstance(ans, int) else Fraction(max(1, ans.numerator - 4), ans.denominator),
                min(ac, bc),
            ]

        qid = f"KMC-T2-EX-25A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_thales_semicircle_angles",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 14. kmc_g89_isosceles_trapezoid_pythag (17 Qs, svg_isosceles_trapezoid)
    # ------------------------------------------------------------------
    trap_cases = [
        ("height", 10, 22, 10, "Easy"),
        ("height", 7, 17, 13, "Easy"),
        ("height", 8, 24, 17, "Easy"),
        ("height", 11, 29, 15, "Easy"),
        ("perim", 8, 14, 4, "Easy"),
        ("perim", 10, 20, 12, "Medium"),
        ("perim", 12, 28, 15, "Medium"),
        ("perim", 7, 25, 12, "Medium"),
        ("area", 6, 18, 10, "Medium"),
        ("area", 9, 19, 13, "Medium"),
        ("area", 10, 26, 10, "Medium"),
        ("area", 12, 30, 15, "Medium"),
        ("area", 14, 28, 25, "Medium"),
        ("diag", 11, 21, 13, "Hard"),
        ("diag", 4, 14, 13, "Hard"),
        ("diag", 9, 21, 10, "Hard"),
        ("diag", 3, 17, 25, "Hard"),
    ]
    for i, (zmode, a, b, p3, diff) in enumerate(trap_cases, 1):
        assert b > a and (b - a) % 2 == 0
        d_wing = (b - a) // 2

        if zmode == "height":
            c = p3
            h = math.isqrt(c * c - d_wing * d_wing)
            assert h * h + d_wing * d_wing == c * c
            ans = h
            svg = svg_isosceles_trapezoid(str(a), str(b), str(c), "h")
            q_en = (
                f"An isosceles trapezoid has parallel bases of lengths {m(a)} cm and {m(b)} cm, and two equal slant legs "
                f"of length {m(c)} cm, as shown. What is the **perpendicular height** {m('h')} of the trapezoid (in cm)?"
            )
            q_ar = (
                f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a)} سم و{m(b)} سم، وطول كل ساق من ساقيه المتساويتين "
                f"{m(c)} سم كما في الشكل. ما **الارتفاع العمودي** {m('h')} لشبه المنحرف (بالسم)؟"
            )
            h_en = f"Drop both dashed altitudes! They split {b} into {d_wing} + {a} + {d_wing}, so each outer right triangle has base ({b}−{a})/2 = {d_wing}!"
            h_ar = f"أنزل الارتفاعين المتقطعين! يقسمان القاعدة الكبرى {b} إلى {d_wing} + {a} + {d_wing}، فيكون طول قاعدة كل مثلث قائم طرفي {d_wing}!"
            s_en = explain_en(
                "Dropping both altitudes splits the bottom base \\( b \\) into a central rectangle of width \\( a \\) and **two congruent right triangles**, each of base \\( \\frac{b - a}{2} \\)!",
                [
                    f"Base of each outer right triangle: {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} cm.",
                    f"Apply Pythagoras with hypotenuse {m(c)}: {m(f'h^2 = {c}^2 - {d_wing}^2 = {c*c} - {d_wing*d_wing} = {h*h}')}.",
                    f"Take the square root: {m(f'h = {ans}')} cm.",
                ],
                f"Trap check: forgetting to divide {m(f'{b} - {a} = {b - a}')} by {m(2)} is the #1 trapezoid mistake!",
            )
            s_ar = explain_ar(
                "بإنزال الارتفاعين تنقسم القاعدة السفلى \\( b \\) إلى مستطيل أوسط عرضه \\( a \\) و**مثلثين قائمين متطابقين** طول قاعدة كلٍّ منهما \\( \\frac{b - a}{2} \\)!",
                [
                    f"قاعدة المثلث القائم الطرفي: {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} سم.",
                    f"بتطبيق فيثاغورس مع الوتر {m(c)}: {m(f'h^2 = {c}^2 - {d_wing}^2 = {c*c} - {d_wing*d_wing} = {h*h}')}.",
                    f"الارتفاع العمودي {m(f'h = {ans}')} سم.",
                ],
                f"احذر من الفخ الأشهر: نسيان قسمة الفرق {m(b - a)} على {m(2)}!",
            )
            distractors = [d_wing, c - d_wing, ans + 2, max(1, ans - 2)]
        elif zmode == "perim":
            h = p3
            c = math.isqrt(h * h + d_wing * d_wing)
            assert c * c == h * h + d_wing * d_wing
            ans = a + b + 2 * c
            svg = svg_isosceles_trapezoid(str(a), str(b), "c", str(h))
            q_en = (
                f"An isosceles trapezoid has parallel bases {m(a)} cm and {m(b)} cm and perpendicular height {m(f'h = {h}')} cm, "
                f"as shown. What is the **perimeter** of the trapezoid (in cm)?"
            )
            q_ar = (
                f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a)} سم و{m(b)} سم، وارتفاعه العمودي {m(f'h = {h}')} سم "
                f"كما في الشكل. ما **محيط** شبه المنحرف (بالسم)؟"
            )
            h_en = f"Find each slant leg c using the outer right triangle of legs ({b}−{a})/2 = {d_wing} and h = {h}, then add a + b + 2c!"
            h_ar = f"احسب طول كل ساق مائلة c من المثلث القائم الطرفي ذي الضلعين {d_wing} و {h}، ثم اجمع a + b + 2c!"
            s_en = explain_en(
                "Use the outer right triangle of base \\( \\frac{b - a}{2} \\) and height \\( h \\) to find slant leg \\( c \\), then add all four sides.",
                [
                    f"Outer right-triangle base: {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} cm.",
                    f"Slant leg by Pythagoras: {m(f'c = \\sqrt{{{d_wing}^2 + {h}^2}} = \\sqrt{{{d_wing*d_wing + h*h}}} = {c}')} cm.",
                    f"Perimeter = {m(f'{a} + {b} + 2 \\times {c} = {ans}')} cm.",
                ],
                f"Trap check: do NOT add the interior altitude {m(h)} into the outer perimeter ({m(a + b + 2 * h)})!",
            )
            s_ar = explain_ar(
                "نوجد طول الساق المائلة \\( c \\) من المثلث القائم الطرفي، ثم نجمع أطوال الأضلاع الأربعة الخارجية.",
                [
                    f"قاعدة المثلث الطرفي: {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} سم.",
                    f"طول الساق المائلة بفيثاغورس: {m(f'c = \\sqrt{{{d_wing}^2 + {h}^2}} = {c}')} سم.",
                    f"المحيط = {m(f'{a} + {b} + 2 \\times {c} = {ans}')} سم.",
                ],
                f"انتبه: لا نجمع الارتفاع الداخلي {m(h)} بدلاً من الساق المائلة {m(c)}!",
            )
            distractors = [a + b + 2 * h, a + b + c, ans + 4, ans - 2]
        elif zmode == "area":
            c = p3
            h = math.isqrt(c * c - d_wing * d_wing)
            assert h * h + d_wing * d_wing == c * c
            ans = ((a + b) * h) // 2
            svg = svg_isosceles_trapezoid(str(a), str(b), str(c), "h")
            q_en = (
                f"An isosceles trapezoid has parallel bases {m(a)} cm and {m(b)} cm and equal slant legs of length {m(c)} cm, "
                f"as shown. What is the **area** of the trapezoid (in {m('\\text{cm}^2')})?"
            )
            q_ar = (
                f"شبه منحرف متطابق الساقين قاعدتاه المتوازيتان {m(a)} سم و{m(b)} سم، وطول كلٍّ من ساقيه {m(c)} سم كما في الشكل. "
                f"ما **مساحة** شبه المنحرف (بوحدة {m('\\text{cm}^2')})؟"
            )
            h_en = f"Never multiply by the slant leg {c}! First find perpendicular height h from the outer right triangle of base ({b}−{a})/2 = {d_wing}."
            h_ar = f"لا تضرب في الساق المائلة {c}! أوجد أولاً الارتفاع العمودي h من المثلث القائم الطرفي الذي قاعدته ({b}−{a})/2 = {d_wing}."
            s_en = explain_en(
                "Trapezoid area uses the **perpendicular height** \\( h \\), never the slant leg \\( c \\): \\( \\text{Area} = \\frac{a + b}{2} \\times h \\)!",
                [
                    f"Each outer right triangle has base {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} cm and hypotenuse {m(c)} cm.",
                    f"Find height by Pythagoras: {m(f'h = \\sqrt{{{c}^2 - {d_wing}^2}} = \\sqrt{{{c*c - d_wing*d_wing}}} = {h}')} cm.",
                    f"Compute area: {m(f'\\frac{{{a} + {b}}}{{2}} \\times {h} = {(a + b) // 2} \\times {h} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"Trap avoided: using the slant leg {m(c)} instead of {m(h)} would give {m(((a + b) * c) // 2)}!",
            )
            s_ar = explain_ar(
                "قانون مساحة شبه المنحرف يعتمد على **الارتفاع العمودي** \\( h \\) وليس الساق المائلة \\( c \\): \\( \\text{المساحة} = \\frac{a + b}{2} \\times h \\)!",
                [
                    f"قاعدة كل مثلث قائم طرفي = {m(f'\\frac{{{b} - {a}}}{{2}} = {d_wing}')} سم ووتره {m(c)} سم.",
                    f"الارتفاع من فيثاغورس: {m(f'h = \\sqrt{{{c}^2 - {d_wing}^2}} = {h}')} سم.",
                    f"المساحة = {m(f'\\frac{{{a} + {b}}}{{2}} \\times {h} = {(a + b) // 2} \\times {h} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"احذر من الفخ الشائع بضرب متوسط القاعدتين في الساق المائلة {m(c)} ({m(((a + b) * c) // 2)})!",
            )
            distractors = [((a + b) * c) // 2, (a + b) * h, ans + h, max(1, ans - h)]
        else:
            c = p3
            h = math.isqrt(c * c - d_wing * d_wing)
            assert h * h + d_wing * d_wing == c * c
            mid_seg = b - d_wing
            assert mid_seg == (a + b) // 2
            diag = math.isqrt(h * h + mid_seg * mid_seg)
            assert diag * diag == h * h + mid_seg * mid_seg
            ans = diag
            svg = svg_isosceles_trapezoid(str(a), str(b), str(c), "h")
            q_en = (
                f"An isosceles trapezoid has parallel bases {m(a)} cm and {m(b)} cm and equal legs of length {m(c)} cm, "
                f"as shown. What is the length of each **diagonal** of the trapezoid (in cm)?"
            )
            q_ar = (
                f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a)} سم و{m(b)} سم، وطول كل ساق من ساقيه {m(c)} سم كما في الشكل. "
                f"ما طول **قطر** شبه المنحرف (بالسم)؟"
            )
            h_en = f"Two steps of Pythagoras! Step 1: find h from ({d_wing}, h, {c}). Step 2: the diagonal is the hypotenuse of legs h and (b − {d_wing}) = {mid_seg}!"
            h_ar = f"تطبيقان متتاليان لفيثاغورس! أولاً أوجد الارتفاع h من ({d_wing}, h, {c})، وثانياً القطر هو وتر المثلث القائم الذي ضلعاه h و (b − {d_wing}) = {mid_seg}!"
            s_en = explain_en(
                "Use **two right triangles** sharing the dashed altitude \\( h \\): first the narrow outer triangle of base \\( \\frac{b-a}{2} \\), then the wide triangle of base \\( b - \\frac{b-a}{2} = \\frac{a+b}{2} \\)!",
                [
                    f"Outer right triangle has base {m(f'\\frac{{{b}-{a}}}{{2}} = {d_wing}')}, so {m(f'h = \\sqrt{{{c}^2 - {d_wing}^2}} = {h}')} cm.",
                    f"From the foot of that altitude to the opposite bottom corner is {m(f'{b} - {d_wing} = {mid_seg}')} cm.",
                    f"Diagonal by Pythagoras: {m(f'd = \\sqrt{{{h}^2 + {mid_seg}^2}} = \\sqrt{{{h*h + mid_seg*mid_seg}}} = {ans}')} cm.",
                ],
                f"Check: both {m(f'({d_wing}, {h}, {c})')} and {m(f'({h}, {mid_seg}, {ans})')} are exact Pythagorean triples!",
            )
            s_ar = explain_ar(
                "نستخدم **مثلثين قائمين** يشتركان في الارتفاع \\( h \\): المثلث الطرفي لإيجاد \\( h \\)، ثم المثلث العريض الذي قاعدته \\( b - \\frac{b-a}{2} = \\frac{a+b}{2} \\) لإيجاد القطر!",
                [
                    f"من المثلث الطرفي ذي القاعدة {m(d_wing)}: {m(f'h = \\sqrt{{{c}^2 - {d_wing}^2}} = {h}')} سم.",
                    f"المسافة الأفقية من مسقط الارتفاع إلى الركن السفلي البعيد تساوي {m(f'{b} - {d_wing} = {mid_seg}')} سم.",
                    f"طول القطر بفيثاغورس: {m(f'd = \\sqrt{{{h}^2 + {mid_seg}^2}} = \\sqrt{{{h*h + mid_seg*mid_seg}}} = {ans}')} سم.",
                ],
                f"تحقق: الثلاثيتان {m(f'({d_wing}, {h}, {c})')} و{m(f'({h}, {mid_seg}, {ans})')} ثلاثيتا فيثاغورس صحيحتان تماماً!",
            )
            distractors = [mid_seg + d_wing, ans + 2, ans - 2, h + d_wing]

        qid = f"KMC-T2-EX-25B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_isosceles_trapezoid_pythag",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 15. kmc_g89_sector_arc_annulus (16 Qs, svg_pie_chart)
    # ------------------------------------------------------------------
    sec_cases = [
        ("sec_area", 90, 8, 0, "Easy"),
        ("sec_area", 60, 6, 0, "Easy"),
        ("sec_area", 120, 9, 0, "Easy"),
        ("sec_area", 45, 8, 0, "Easy"),
        ("sec_arc", 90, 10, 0, "Easy"),
        ("sec_area", 72, 10, 0, "Medium"),
        ("sec_area", 135, 8, 0, "Medium"),
        ("sec_arc", 120, 12, 0, "Medium"),
        ("sec_arc", 150, 12, 0, "Medium"),
        ("sec_perim", 90, 6, 0, "Medium"),
        ("sec_perim", 60, 12, 0, "Medium"),
        ("annulus", 360, 10, 6, "Medium"),
        ("annulus", 360, 13, 12, "Medium"),
        ("annulus", 360, 17, 8, "Hard"),
        ("annulus_sec", 90, 10, 6, "Hard"),
        ("annulus_sec", 120, 9, 6, "Hard"),
    ]
    for i, (smode, theta, r_big, r_in, diff) in enumerate(sec_cases, 1):
        fr_theta = Fraction(theta, 360)

        if smode == "sec_area":
            coeff = fr_theta * r_big * r_big
            assert coeff.denominator == 1
            c_int = int(coeff)
            ans_tex = f"{c_int}\\pi"
            svg = svg_pie_chart([(float(fr_theta), f"{theta}°"), (float(1 - fr_theta), "")])
            q_en = (
                f"In a circle of radius {m(r_big)} cm, a sector has central angle {m(f'{theta}^\\circ')}, as shaded in the diagram. "
                f"What is the **area** of this sector in terms of {m('\\pi')} (in {m('\\text{cm}^2')})?"
            )
            q_ar = (
                f"في دائرة نصف قطرها {m(r_big)} سم، قُطع قطاع دائري زاويته المركزية {m(f'{theta}^\\circ')} كما هو مظلّل في الشكل. "
                f"ما **مساحة** هذا القطاع بدلالة {m('\\pi')} (بوحدة {m('\\text{cm}^2')})؟"
            )
            h_en = f"A {theta}° sector is {fmt_val(fr_theta)} of the full circle's area πr² = {r_big*r_big}π!"
            h_ar = f"القطاع ذو الزاوية {theta}° يمثّل الكسر {fmt_val(fr_theta)} من مساحة الدائرة الكاملة πr² = {r_big*r_big}π!"
            s_en = explain_en(
                "Sector area is the fraction \\( \\frac{\\theta}{360^\\circ} \\) of the full circle area \\( \\pi r^2 \\)!",
                [
                    f"Fraction of the full circle: {m(f'\\frac{{{theta}^\\circ}}{{360^\\circ}} = {fmt_val(fr_theta)}')}.",
                    f"Full circle area: {m(f'\\pi \\times {r_big}^2 = {r_big * r_big}\\pi')}.",
                    f"Multiply: {m(f'{fmt_val(fr_theta)} \\times {r_big * r_big}\\pi = {ans_tex}')}.",
                ],
                f"Check: {m(c_int)} is strictly smaller than the full circle coefficient {m(r_big * r_big)}!",
            )
            s_ar = explain_ar(
                "مساحة القطاع الدائري تساوي الكسر \\( \\frac{\\theta}{360^\\circ} \\) مضروباً في مساحة الدائرة الكاملة \\( \\pi r^2 \\)!",
                [
                    f"نسبة القطاع من الدائرة: {m(f'\\frac{{{theta}^\\circ}}{{360^\\circ}} = {fmt_val(fr_theta)}')}.",
                    f"مساحة الدائرة الكاملة: {m(f'\\pi \\times {r_big}^2 = {r_big * r_big}\\pi')}.",
                    f"مساحة القطاع = {m(f'{fmt_val(fr_theta)} \\times {r_big * r_big}\\pi = {ans_tex}')}.",
                ],
                f"تحقق: المعامل {m(c_int)} يساوي {m(fmt_val(fr_theta))} من {m(r_big * r_big)} بالضبط!",
            )
            distractors = [f"{c_int * 2}\\pi", f"{r_big * r_big}\\pi", f"{max(1, c_int // 2) if c_int > 2 else c_int + 3}\\pi", f"{c_int + 4}\\pi"]
        elif smode == "sec_arc":
            coeff = fr_theta * 2 * r_big
            assert coeff.denominator == 1
            c_int = int(coeff)
            ans_tex = f"{c_int}\\pi"
            svg = svg_pie_chart([(float(fr_theta), f"{theta}°"), (float(1 - fr_theta), "")])
            q_en = (
                f"A sector of a circle of radius {m(r_big)} cm has central angle {m(f'{theta}^\\circ')}, as shown. "
                f"What is the **length of its curved arc** in terms of {m('\\pi')} (in cm)?"
            )
            q_ar = (
                f"قطاع دائري في دائرة نصف قطرها {m(r_big)} سم زاويته المركزية {m(f'{theta}^\\circ')} كما في الشكل. "
                f"ما **طول قوسه المنحني** بدلالة {m('\\pi')} (بالسم)؟"
            )
            h_en = f"Arc length uses circumference 2πr = {2 * r_big}π (NOT πr²!), multiplied by {theta}/360 = {fmt_val(fr_theta)}!"
            h_ar = f"طول القوس يعتمد على المحيط 2πr = {2 * r_big}π (وليس المساحة πr²!) مضروباً في {fmt_val(fr_theta)}!"
            s_en = explain_en(
                "Arc length is the fraction \\( \\frac{\\theta}{360^\\circ} \\) of the full **circumference** \\( 2\\pi r \\)!",
                [
                    f"Sector fraction: {m(f'\\frac{{{theta}^\\circ}}{{360^\\circ}} = {fmt_val(fr_theta)}')}.",
                    f"Full circumference: {m(f'2\\pi \\times {r_big} = {2 * r_big}\\pi')} cm.",
                    f"Arc length: {m(f'{fmt_val(fr_theta)} \\times {2 * r_big}\\pi = {ans_tex}')} cm.",
                ],
                f"Trap check: using area {m('\\pi r^2')} by mistake would give {m(f'{int(fr_theta * r_big * r_big)}\\pi')} instead of {m(ans_tex)}!",
            )
            s_ar = explain_ar(
                "طول القوس يساوي الكسر \\( \\frac{\\theta}{360^\\circ} \\) من **محيط الدائرة الكامل** \\( 2\\pi r \\)!",
                [
                    f"نسبة القوس: {m(f'\\frac{{{theta}^\\circ}}{{360^\\circ}} = {fmt_val(fr_theta)}')}.",
                    f"محيط الدائرة الكامل: {m(f'2\\pi \\times {r_big} = {2 * r_big}\\pi')} سم.",
                    f"طول القوس = {m(f'{fmt_val(fr_theta)} \\times {2 * r_big}\\pi = {ans_tex}')} سم.",
                ],
                f"انتبه لعدم الخلط بين قانون المحيط {m('2\\pi r')} وقانون المساحة {m('\\pi r^2')}!",
            )
            area_trap = int(fr_theta * r_big * r_big)
            distractors = [f"{area_trap}\\pi", f"{2 * r_big}\\pi", f"{max(1, c_int - 2)}\\pi", f"{c_int + 2}\\pi"]
        elif smode == "sec_perim":
            coeff = int(fr_theta * 2 * r_big)
            ans_tex = f"{2 * r_big} + {coeff}\\pi"
            svg = svg_pie_chart([(float(fr_theta), f"{theta}°"), (float(1 - fr_theta), "")])
            q_en = (
                f"A slice (sector) of central angle {m(f'{theta}^\\circ')} is cut out from a circular disc of radius {m(r_big)} cm. "
                f"What is the **total perimeter** of this cut-out sector in terms of {m('\\pi')} (in cm)?"
            )
            q_ar = (
                f"قُطعت شريحة (قطاع دائري) زاويتها المركزية {m(f'{theta}^\\circ')} من قرص دائري نصف قطره {m(r_big)} سم. "
                f"ما **المحيط الكلي** لهذا القطاع المقطوع بدلالة {m('\\pi')} (بالسم)؟"
            )
            h_en = f"A cut-out sector's boundary has THREE pieces: its curved arc PLUS TWO straight radii ({r_big} + {r_big} = {2 * r_big})!"
            h_ar = f"حدود القطاع المقطوع تتكون من ثلاثة أجزاء: القوس المنحني + نصفي القطرين المستقيمين ({r_big} + {r_big} = {2 * r_big})!"
            s_en = explain_en(
                "Perimeter of a sector = **2 straight radii + curved arc length** = \\( 2r + \\frac{\\theta}{360^\\circ}(2\\pi r) \\)!",
                [
                    f"Curved arc length: {m(f'\\frac{{{theta}}}{{360}} \\times 2\\pi({r_big}) = {coeff}\\pi')} cm.",
                    f"Two straight radii bounding the slice: {m(f'2 \\times {r_big} = {2 * r_big}')} cm.",
                    f"Total perimeter: {m(ans_tex)} cm.",
                ],
                f"Famous KMC trap avoided: {m(f'{coeff}\\pi')} alone is only the curved arc, forgetting the two straight sides!",
            )
            s_ar = explain_ar(
                "محيط القطاع الدائري = **نصفا القطرين المستقيمين + طول القوس المنحني** = \\( 2r + \\frac{\\theta}{360^\\circ}(2\\pi r) \\)!",
                [
                    f"طول القوس المنحني: {m(f'\\frac{{{theta}}}{{360}} \\times 2\\pi({r_big}) = {coeff}\\pi')} سم.",
                    f"مجموع الضلعين المستقيمين (نصفي القطرين): {m(f'2 \\times {r_big} = {2 * r_big}')} سم.",
                    f"المحيط الكلي للقطاع: {m(ans_tex)} سم.",
                ],
                f"احذر من الفخ الشهير باختيار {m(f'{coeff}\\pi')} فقط ونسيان الضلعين المستقيمين!",
            )
            distractors = [f"{coeff}\\pi", f"{r_big} + {coeff}\\pi", f"{2 * r_big} + {2 * coeff}\\pi", f"{2 * r_big} + {int(fr_theta * r_big * r_big)}\\pi"]
        elif smode == "annulus":
            c_int = r_big * r_big - r_in * r_in
            ans_tex = f"{c_int}\\pi"
            svg = svg_pie_chart([(0.25, f"r={r_in}"), (0.75, f"R={r_big}")])
            q_en = (
                f"Two concentric circles share the same center and have outer radius {m(f'R = {r_big}')} cm and inner radius "
                f"{m(f'r = {r_in}')} cm (forming a flat circular ring / annulus). What is the **area of the ring** between "
                f"the two circles in terms of {m('\\pi')} (in {m('\\text{cm}^2')})?"
            )
            q_ar = (
                f"دائرتان متحدتان في المركز نصف قطرهما الخارجي {m(f'R = {r_big}')} سم والداخلي {m(f'r = {r_in}')} سم "
                f"(تشكلان حلقة دائرية مسطحة). ما **مساحة الحلقة** المحصورة بين الدائرتين بدلالة {m('\\pi')} (بوحدة {m('\\text{cm}^2')})؟"
            )
            h_en = f"Ring area = πR² − πr² = π(R − r)(R + r)! Use difference of squares ({r_big}−{r_in})({r_big}+{r_in}) for instant mental math!"
            h_ar = f"مساحة الحلقة = πR² − πr² = π(R − r)(R + r)! استخدم فرق المربعين ({r_big}−{r_in})({r_big}+{r_in}) للحساب الذهني السريع!"
            s_en = explain_en(
                "The area of a concentric ring (annulus) is \\( \\pi R^2 - \\pi r^2 = \\pi(R - r)(R + r) \\) — NEVER \\( \\pi(R - r)^2 \\)!",
                [
                    f"Use Difference of Squares: {m(f'R^2 - r^2 = ({r_big} - {r_in})({r_big} + {r_in}) = {r_big - r_in} \\times {r_big + r_in} = {c_int}')}.",
                    f"Multiply by {m('\\pi')}: ring area = {m(ans_tex)} {m('\\text{cm}^2')}.",
                ],
                f"Trap check: {m(f'\\pi({r_big} - {r_in})^2 = {(r_big - r_in)**2}\\pi')} is a classic trap — always subtract areas {m('R^2 - r^2')}, not radii!",
            )
            s_ar = explain_ar(
                "مساحة الحلقة الدائرية تساوي \\( \\pi R^2 - \\pi r^2 = \\pi(R - r)(R + r) \\)، وليست \\( \\pi(R - r)^2 \\) أبداً!",
                [
                    f"نطبّق فرق المربعين ذهنياً: {m(f'R^2 - r^2 = ({r_big} - {r_in})({r_big} + {r_in}) = {r_big - r_in} \\times {r_big + r_in} = {c_int}')}.",
                    f"نضرب في {m('\\pi')}: مساحة الحلقة = {m(ans_tex)} {m('\\text{cm}^2')}.",
                ],
                f"احذر من الفخ الشهير {m(f'\\pi(R - r)^2 = {(r_big - r_in)**2}\\pi')}!",
            )
            trap_sq = (r_big - r_in) ** 2
            distractors = [
                f"{trap_sq}\\pi" if trap_sq != c_int else f"{c_int + 8}\\pi",
                f"{r_big * r_big + r_in * r_in}\\pi",
                f"{2 * (r_big - r_in)}\\pi",
                f"{c_int + 10}\\pi",
            ]
        else:
            ring_full = r_big * r_big - r_in * r_in
            coeff = fr_theta * ring_full
            assert coeff.denominator == 1
            c_int = int(coeff)
            ans_tex = f"{c_int}\\pi"
            svg = svg_pie_chart([(float(fr_theta), f"{theta}°"), (float(1 - fr_theta), "")])
            q_en = (
                f"A curved garden path is shaped as a {m(f'{theta}^\\circ')} sector of a concentric ring with outer radius "
                f"{m(f'R = {r_big}')} m and inner radius {m(f'r = {r_in}')} m. What is the **area** of this curved path "
                f"in terms of {m('\\pi')} (in {m('\\text{m}^2')})?"
            )
            q_ar = (
                f"ممر حديقة منحني على شكل قطاع بزاوية {m(f'{theta}^\\circ')} من حلقة دائرية نصف قطرها الخارجي "
                f"{m(f'R = {r_big}')} م والداخلي {m(f'r = {r_in}')} م. ما **مساحة** هذا الممر بدلالة {m('\\pi')} (بوحدة {m('\\text{m}^2')})؟"
            )
            h_en = f"Take the sector fraction {theta}/360 = {fmt_val(fr_theta)} of the full ring area π(R² − r²)!"
            h_ar = f"اضرب نسبة القطاع {fmt_val(fr_theta)} في مساحة الحلقة الكاملة π(R² − r²)!"
            s_en = explain_en(
                "A sector of a ring has area \\( \\frac{\\theta}{360^\\circ} \\pi (R^2 - r^2) \\)!",
                [
                    f"Full ring area: {m(f'\\pi({r_big}^2 - {r_in}^2) = \\pi({r_big*r_big} - {r_in*r_in}) = {ring_full}\\pi')}.",
                    f"Multiply by sector fraction {m(f'\\frac{{{theta}}}{{360}} = {fmt_val(fr_theta)}')}: {m(f'{fmt_val(fr_theta)} \\times {ring_full}\\pi = {ans_tex}')}.",
                ],
                f"Check: outer sector ({m(f'{fmt_val(fr_theta * r_big * r_big)}\\pi')}) minus inner sector ({m(f'{fmt_val(fr_theta * r_in * r_in)}\\pi')}) = {m(ans_tex)}!",
            )
            s_ar = explain_ar(
                "مساحة قطاع من حلقة دائرية تساوي \\( \\frac{\\theta}{360^\\circ} \\pi (R^2 - r^2) \\)!",
                [
                    f"مساحة الحلقة الكاملة: {m(f'\\pi({r_big}^2 - {r_in}^2) = {ring_full}\\pi')}.",
                    f"نضرب في كسر القطاع {m(fmt_val(fr_theta))}: {m(f'{fmt_val(fr_theta)} \\times {ring_full}\\pi = {ans_tex}')}.",
                ],
                f"تحقق: مساحة القطاع الخارجي ناقص القطاع الداخلي تعطي {m(ans_tex)} بالضبط!",
            )
            distractors = [f"{ring_full}\\pi", f"{c_int * 2}\\pi", f"{max(1, c_int - 4)}\\pi", f"{c_int + 5}\\pi"]

        qid = f"KMC-T2-EX-25C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, "kmc_g89_sector_arc_annulus",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    assert len(out) == 50
    return out


def _gen_lesson_2_6() -> list[dict]:
    out: list[dict] = []

    # ------------------------------------------------------------------
    # 16. kmc_g89_blocked_grid_paths (17 Qs, svg_street_grid)
    # ------------------------------------------------------------------
    grid_cases = [
        (3, 2, (1, 1), "Easy"),
        (3, 2, (1, 2), "Easy"),
        (2, 3, (1, 1), "Easy"),
        (3, 3, (1, 1), "Easy"),
        (3, 3, (2, 1), "Easy"),
        (4, 2, (2, 1), "Medium"),
        (4, 2, (1, 1), "Medium"),
        (4, 2, (2, 2), "Medium"),
        (4, 3, (2, 1), "Medium"),
        (4, 3, (1, 1), "Medium"),
        (4, 3, (1, 2), "Medium"),
        (5, 2, (2, 1), "Medium"),
        (6, 2, (3, 1), "Medium"),
        (4, 4, (2, 2), "Hard"),
        (4, 4, (2, 1), "Hard"),
        (5, 3, (2, 1), "Hard"),
        (5, 3, (2, 2), "Hard"),
    ]
    for i, (cols, rows, blocked, diff) in enumerate(grid_cases, 1):
        bc, br = blocked
        total_p = math.comb(cols + rows, cols)
        bad_p = math.comb(bc + br, bc) * math.comb((cols - bc) + (rows - br), cols - bc)
        ans = total_p - bad_p

        # Cross-check by 2D dynamic programming
        dp = [[0] * (rows + 1) for _ in range(cols + 1)]
        dp[0][0] = 1
        for c_i in range(cols + 1):
            for r_i in range(rows + 1):
                if (c_i, r_i) == (0, 0) or (c_i, r_i) == blocked:
                    if (c_i, r_i) == blocked:
                        dp[c_i][r_i] = 0
                    continue
                if c_i > 0:
                    dp[c_i][r_i] += dp[c_i - 1][r_i]
                if r_i > 0:
                    dp[c_i][r_i] += dp[c_i][r_i - 1]
        assert ans == dp[cols][rows] and ans > 0

        svg = svg_street_grid(cols, rows, blocked)
        q_en = (
            f"On the {m(f'{cols} \\times {rows}')} street grid shown, a robot starts at corner **A** {m('(0, 0)')} "
            f"and moves only **Right** or **Up** along grid lines to reach **B** {m(f'({cols}, {rows})')}. "
            f"Intersection {m(f'X({bc}, {br})')} is closed for construction (marked {m('\\times')}). "
            f"How many shortest paths from **A** to **B** avoid {m('X')}?"
        )
        q_ar = (
            f"على شبكة الشوارع ذات الأبعاد {m(f'{cols} \\times {rows}')} الموضّحة، ينطلق روبوت من الركن **A** {m('(0, 0)')} "
            f"ويتحرك فقط **يميناً** أو **لأعلى** على خطوط الشبكة للوصول إلى **B** {m(f'({cols}, {rows})')}. "
            f"التقاطع {m(f'X({bc}, {br})')} مغلق للصيانة (المعلَّم بـ {m('\\times')}). "
            f"كم مساراً من أقصر المسارات من **A** إلى **B** يتجنّب المرور بالتقاطع {m('X')}؟"
        )
        h_en = f"Complementary counting! Subtract the paths that DO pass through X({bc},{br}) from all C({cols + rows}, {cols}) = {total_p} paths!"
        h_ar = f"استخدم العدّ بالمتمم! اطرح عدد المسارات التي تمرّ بـ X({bc},{br}) من إجمالي المسارات C({cols + rows}, {cols}) = {total_p}!"
        p_ax = math.comb(bc + br, bc)
        p_xb = math.comb((cols - bc) + (rows - br), cols - bc)
        s_en = explain_en(
            "Count **all** shortest paths from \\( A \\) to \\( B \\), then subtract the forbidden paths that pass through \\( X \\) "
            "(which equal \\( (\\text{paths } A \\to X) \\times (\\text{paths } X \\to B) \\))!",
            [
                f"Total unrestricted paths ({m(cols)} Right, {m(rows)} Up): {m(f'\\binom{{{cols + rows}}}{{{cols}}} = {total_p}')}.",
                f"Paths from {m('A(0,0)')} to {m(f'X({bc},{br})')}: {m(f'\\binom{{{bc + br}}}{{{bc}}} = {p_ax}')}; "
                f"paths from {m(f'X({bc},{br})')} to {m(f'B({cols},{rows})')}: {m(f'\\binom{{{(cols - bc) + (rows - br)}}}{{{cols - bc}}} = {p_xb}')}.",
                f"Subtract forbidden paths: {m(f'{total_p} - ({p_ax} \\times {p_xb}) = {total_p} - {bad_p} = {ans}')}.",
            ],
            f"Corner-by-corner addition (Pascal grid rule with {m('0')} at {m('X')}) also confirms **{m(ans)}** paths!",
        )
        s_ar = explain_ar(
            "نحسب **جميع** المسارات القصيرة من \\( A \\) إلى \\( B \\)، ثم نطرح المسارات الممنوعة التي تمر عبر \\( X \\) "
            "وهي تساوي \\( (\\text{مسارات } A \\to X) \\times (\\text{مسارات } X \\to B) \\)!",
            [
                f"إجمالي المسارات بدون عوائق ({m(cols)} يميناً و{m(rows)} لأعلى): {m(f'\\binom{{{cols + rows}}}{{{cols}}} = {total_p}')}.",
                f"المسارات من {m('A')} إلى {m('X')}: {m(f'\\binom{{{bc + br}}}{{{bc}}} = {p_ax}')}؛ "
                f"والمسارات من {m('X')} إلى {m('B')}: {m(f'\\binom{{{(cols - bc) + (rows - br)}}}{{{cols - bc}}} = {p_xb}')}.",
                f"نطرح المسارات المارة بـ {m('X')}: {m(f'{total_p} - ({p_ax} \\times {p_xb}) = {total_p} - {bad_p} = {ans}')} مساراً.",
            ],
            f"تحقق بجمع الأعداد عند تقاطعات الشبكة (مع وضع {m(0)} عند {m('X')}): نحصل على **{m(ans)}** مساراً بالضبط!",
        )
        distractors = [total_p, total_p - (p_ax + p_xb), bad_p, ans + 2]
        qid = f"KMC-T2-EX-26A-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, "Combinatorics & Logic", diff, "kmc_g89_blocked_grid_paths",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg,
            )
        )

    # ------------------------------------------------------------------
    # 17. kmc_g89_counterfeit_coin_weighings (17 Qs, NO forbidden words!)
    # ------------------------------------------------------------------
    coin_cases = [
        ("min_w", 8, "gold coins", "عملات ذهبية", "Easy"),
        ("min_w", 9, "silver coins", "عملات فضية", "Easy"),
        ("min_w", 27, "bronze medals", "ميداليات برونزية", "Easy"),
        ("max_c", 2, "", "", "Easy"),
        ("max_c", 3, "", "", "Easy"),
        ("min_w", 10, "copper coins", "عملات نحاسية", "Medium"),
        ("min_w", 24, "pearl beads", "حبات لؤلؤ", "Medium"),
        ("min_w", 28, "steel balls", "كرات فولاذية", "Medium"),
        ("min_w", 75, "brass weights", "أثقال نحاسية", "Medium"),
        ("max_c", 4, "", "", "Medium"),
        ("max_c", 5, "", "", "Medium"),
        ("key_match", 5, "", "", "Medium"),
        ("key_match", 6, "", "", "Medium"),
        ("min_w", 100, "platinum tokens", "أقراص بلاتينية", "Hard"),
        ("key_match", 8, "", "", "Hard"),
        ("key_match", 10, "", "", "Hard"),
        ("key_open", 7, "", "", "Hard"),
    ]
    for i, (cmode, param, item_en, item_ar, diff) in enumerate(coin_cases, 1):
        if cmode == "min_w":
            N = param
            k = 1
            while 3 ** k < N:
                k += 1
            ans = k
            prev_p = 3 ** (k - 1)
            curr_p = 3 ** k
            split_top = (N + 2) // 3
            q_en = (
                f"You have {m(N)} identical-looking {item_en}, exactly **one** of which is counterfeit and **slightly lighter** "
                f"than all the genuine ones. Using a two-pan balance scale (with no standard weights), what is the **minimum number "
                f"of weighings** needed to **guarantee** finding the lighter counterfeit item in the worst case?"
            )
            q_ar = (
                f"لديك {m(N)} من الـ ({item_ar}) متطابقة المظهر، إحداها فقط مزيّفة وهي **أخف قليلاً** من البقية الأصلية. "
                f"باستخدام ميزان ذي كفتين (دون أوزان خارجية)، ما **أقل عدد من الوزنات** يكفي **لضمان** تحديد القطعة الأخف في أسوأ الحالات؟"
            )
            h_en = "Divide into THREE groups (Left pan, Right pan, Table)! Compare N against powers of 3: 3¹ = 3, 3² = 9, 3³ = 27, 3⁴ = 81, 3⁵ = 243!"
            h_ar = "قسّم القطع إلى ثلاث مجموعات (الكفة اليسرى، الكفة اليمنى، خارج الميزان)! قارن العدد بقوى الثلاثة: 3¹ = 3، 3² = 9، 3³ = 27، 3⁴ = 81، 3⁵ = 243!"
            s_en = explain_en(
                "One weighing on a two-pan balance has **3 outcomes** (left lighter, right lighter, or balanced = on the table), "
                "so \\( k \\) weighings can guarantee finding 1 lighter coin among at most \\( 3^k \\) coins!",
                [
                    f"List powers of {m(3)}: {m('3^1 = 3,\\; 3^2 = 9,\\; 3^3 = 27,\\; 3^4 = 81,\\; 3^5 = 243')}.",
                    f"Since {m(f'{prev_p} < {N} \\le {curr_p}')}, {m(k - 1)} weighings can handle at most {m(prev_p)} items (not enough!), while {m(k)} weighings handle up to {m(curr_p)}.",
                    f"On Weighing 1, put {m(split_top)} on each pan and leave {m(N - 2 * split_top)} aside — every branch leaves at most {m(prev_p)} candidates, solved in {m(k - 1)} more weighings (total **{m(ans)}**).",
                ],
                f"Trap check: splitting into 2 piles instead of 3 wastes the 'balanced' outcome and takes more weighings!",
            )
            s_ar = explain_ar(
                "كل وزنة في الميزان ذي الكفتين تعطي **3 نتائج ممكنة** (الكفة اليسرى أخف، اليمنى أخف، أو تعادل أي أن المزيّفة خارج الميزان)، "
                "لذلك فإن \\( k \\) وزنات تحسم البحث في مجموعة حجمها الأقصى \\( 3^k \\)!",
                [
                    f"قوى العدد {m(3)} هي: {m('3^1 = 3،\\; 3^2 = 9،\\; 3^3 = 27،\\; 3^4 = 81،\\; 3^5 = 243')}.",
                    f"بما أن {m(f'{prev_p} < {N} \\le {curr_p}')}، فإن {m(k - 1)} وزنات تكفي لـ {m(prev_p)} كحد أقصى فقط، بينما {m(k)} وزنات تكفي حتى {m(curr_p)}.",
                    f"في الوزنة الأولى نضع {m(split_top)} في كل كفة ونترك {m(N - 2 * split_top)} جانباً، فيتبقى على الأكثر {m(prev_p)} مرشحات تُحسم في {m(k - 1)} وزنات (المجموع **{m(ans)}**).",
                ],
                f"انتبه: التقسيم إلى 3 مجموعات بدلاً من مجموعتين هو السر وراء القوة {m(f'3^{{{ans}}} = {curr_p}')}!",
            )
            distractors = [x for x in (ans - 1, ans + 1, ans + 2, (N + 1) // 2, 1) if x > 0 and x != ans][:4]
        elif cmode == "max_c":
            k = param
            ans = 3 ** k
            q_en = (
                f"Suppose you have a pile of identical-looking coins containing **exactly one lighter counterfeit coin**, "
                f"and you are allowed **at most {m(k)} weighings** on a two-pan balance scale. "
                f"What is the **maximum number of coins** for which you can **guarantee** finding the counterfeit coin?"
            )
            q_ar = (
                f"لديك مجموعة من العملات المتطابقة شكلاً بينها **عملة واحدة مزيّفة أخف وزناً**، ويُسمح لك بإجراء "
                f"**{m(k)} وزنات على الأكثر** بميزان ذي كفتين. ما **أكبر عدد من العملات** يمكنك أن **تضمن** اكتشاف العملة المزيّفة من بينها؟"
            )
            h_en = f"Each weighing triples the maximum testable pool because a balance scale has 3 outcomes (left, right, balanced)!"
            h_ar = f"كل وزنة تضاعف العدد الأقصى القابل للفحص 3 مرات لأن للميزان 3 نتائج (يمين، يسار، تعادل)!"
            pow_chain = ",\\; ".join(f"3^{{{j}}} = {3**j}" for j in range(1, k + 1))
            s_en = explain_en(
                "Each balance weighing narrows the suspect pool by a factor of **3** (Left pan, Right pan, Off-scale), so \\( k \\) weighings test up to \\( 3^k \\) coins!",
                [
                    f"1 weighing tests up to {m(3)} coins (1 left, 1 right, 1 off).",
                    f"Multiply by {m(3)} for each extra weighing: {m(pow_chain)}.",
                    f"With {m(k)} weighings, the maximum guaranteed number of coins is **{m(ans)}**.",
                ],
                f"Trap check: {m(f'2^{{{k}}} = {2**k}')} comes from splitting into 2 groups instead of 3!",
            )
            s_ar = explain_ar(
                "كل وزنة تقسّم المرشحين إلى **3 مجموعات متساوية** (الكفة اليسرى، اليمنى، خارج الميزان)، لذا تفحص \\( k \\) وزنات حتى \\( 3^k \\) عملة!",
                [
                    f"وزنة واحدة تفحص حتى {m(3)} عملات.",
                    f"نضرب في {m(3)} مع كل وزنة إضافية: {m(pow_chain)}.",
                    f"إذن أقصى عدد مضمون في {m(k)} وزنات هو **{m(ans)}** عملة.",
                ],
                f"احذر من الفخ الشهير {m(f'2^{{{k}}} = {2**k}')} الناتج عن إهمال المجموعة الثالثة خارج الكفتين!",
            )
            distractors = [2 ** k, ans - 1, 3 ** (k - 1), 2 * (3 ** (k - 1))]
        elif cmode == "key_match":
            n = param
            ans = n * (n - 1) // 2
            sum_chain = " + ".join(str(x) for x in range(n - 1, 0, -1))
            q_en = (
                f"There are {m(n)} different padlocks and {m(n)} matching keys mixed up in a pile. "
                f"If a key fails to open {m(n - 1)} padlocks, you immediately know it belongs to the remaining padlock without testing it. "
                f"In the **worst case**, how many key-in-lock trials are needed to **match every key to its padlock** with certainty?"
            )
            q_ar = (
                f"يوجد {m(n)} أقفال مختلفة و{m(n)} مفاتيح مطابقة لها اختلطت معاً. "
                f"إذا جُرِّب مفتاح وفشل في فتح {m(n - 1)} قفلاً، نعلم فوراً أنه يخص القفل المتبقي دون حاجة لتجربته فيه. "
                f"في **أسوأ الحالات**، ما أقل عدد من التجارب يكفي **لتحديد القفل المطابق لكل مفتاح** بيقين تام؟"
            )
            h_en = f"Worst case: Key 1 fails {n - 1} times (now matched!), Key 2 fails {n - 2} times among the remaining locks, ..., down to 1!"
            h_ar = f"في أسوأ حالة: المفتاح الأول يفشل {n - 1} مرات (فيتحدد قفله!)، والثاني يفشل {n - 2} مرات في الأقفال المتبقية، وهكذا حتى 1!"
            s_en = explain_en(
                "In the worst case, every test fails until only 1 lock remains for the current key!",
                [
                    f"Key 1 requires at most {m(n - 1)} failed tries to pinpoint its lock; set that matched pair aside.",
                    f"Key 2 requires at most {m(n - 2)} tries among the remaining {m(n - 1)} locks, Key 3 needs {m(n - 3)}, ..., and Key {m(n - 1)} needs {m(1)} try (leaving Key {m(n)} automatically matched!).",
                    f"Add the triangular sum: {m(f'{sum_chain} = \\frac{{{n} \\times {n - 1}}}{{2}} = {ans}')} trials.",
                ],
                f"Trap check: {m(n * (n + 1) // 2)} counts physically turning the already-known final key in each lock; for **matching**, {m(ans)} suffices!",
            )
            s_ar = explain_ar(
                "في أسوأ الحالات تفشل كل محاولة حتى يتبقى قفل واحد فقط فيتعيّن تلقائياً للمفتاح الحالي!",
                [
                    f"المفتاح الأول يحتاج على الأكثر {m(n - 1)} محاولات فاشلة لمعرفة قفله، ثم نضع هذا الزوج جانباً.",
                    f"المفتاح الثاني يحتاج على الأكثر {m(n - 2)} محاولات، والثالث {m(n - 3)}، ...، والمفتاح قبل الأخير يحتاج محاولة واحدة ({m(1)}) ويتحدد الأخير تلقائياً.",
                    f"نجمع المتسلسلة الحسابية: {m(f'{sum_chain} = \\frac{{{n} \\times {n - 1}}}{{2}} = {ans}')} تجربة.",
                ],
                f"انتبه للفرق: {m(ans)} تكفي لمعرفة التطابق، بينما {m(n * (n + 1) // 2)} تشمل إدخال المفتاح الأخير لفتح القفل فعلياً!",
            )
            distractors = [n * (n + 1) // 2, n * n, n * (n - 1), ans - 1]
        else:
            n = param
            ans = n * (n + 1) // 2
            sum_chain = " + ".join(str(x) for x in range(n, 0, -1))
            q_en = (
                f"A treasure hunter has {m(n)} locked chests and {m(n)} unlabeled keys (one per chest). "
                f"Each chest opens **only when its matching key is actually inserted and turned** inside its lock. "
                f"In the **worst case**, how many key insertions might be required to **physically unlock all {m(n)} chests**?"
            )
            q_ar = (
                f"لدى باحث عن الكنوز {m(n)} صناديق مقفلة و{m(n)} مفاتيح غير مرقّمة (مفتاح لكل صندوق). "
                f"لا يُفتح أي صندوق **إلا بإدخال مفتاحه الصحيح وتدويره فعلياً** داخل قفله. "
                f"في **أسوأ الحالات**، كم عملية إدخال مفتاح قد يلزم إجراؤها **لفتح الصناديق الـ {m(n)} جميعها فعلياً**؟"
            )
            h_en = f"Even after {n - 1} failures tell you which chest Key 1 fits, you still need +1 insertion to actually OPEN that chest!"
            h_ar = f"حتى بعد فشل المفتاح في {n - 1} صناديق، لا بد من إدخاله مرة إضافية (+1) لفتح صندوقه فعلياً!"
            s_en = explain_en(
                "To **physically open** each chest, the final successful insertion must also be counted!",
                [
                    f"Key 1 can fail on {m(n - 1)} chests and then takes {m(1)} successful insertion to open the {m(f'{n}\\text{{th}}')} chest = **{m(n)}** insertions.",
                    f"Key 2 takes at most {m(n - 1)} insertions among the remaining chests, ..., down to **{m(1)}** insertion to open the last chest.",
                    f"Total worst-case insertions: {m(f'{sum_chain} = \\frac{{{n} \\times {n + 1}}}{{2}} = {ans}')}.",
                ],
                f"Notice: {m(f'{n * (n - 1) // 2} \\text{{ (failed tests)}} + {n} \\text{{ (successful openings)}} = {ans}')}!",
            )
            s_ar = explain_ar(
                "لأن المطلوب **فتح الصناديق فعلياً**، يجب احتساب المحاولة الناجحة الأخيرة لكل مفتاح أيضاً!",
                [
                    f"المفتاح الأول قد يفشل في {m(n - 1)} صناديق ثم يحتاج محاولة ناجحة ({m(1)}) لفتح صندوقه = **{m(n)}** محاولات.",
                    f"المفتاح الثاني يحتاج على الأكثر {m(n - 1)} محاولات، ...، والمفتاح الأخير يحتاج محاولة واحدة (**{m(1)}**) لفتح الصندوق الأخير.",
                    f"إجمالي المحاولات في أسوأ حالة: {m(f'{sum_chain} = \\frac{{{n} \\times {n + 1}}}{{2}} = {ans}')}.",
                ],
                f"تحقق جميل: {m(n * (n - 1) // 2)} محاولة فاشلة + {m(n)} محاولات فتح ناجحة = {m(ans)}!",
            )
            distractors = [n * (n - 1) // 2, n * n, ans + n, ans - 2]

        qid = f"KMC-T2-EX-26B-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        if cmode == "min_w":
            svg_en = svg_pan_balance_coins(f"N = {N} (1 lighter)", "Pan L", "Pan R", sub_lbl="Min weighings = ?")
            svg_ar = svg_pan_balance_coins(f"العدد = {N} (1 أخف)", "الكفة 1", "الكفة 2", sub_lbl="أقل عدد وزنات = ؟")
        elif cmode == "max_c":
            svg_en = svg_pan_balance_coins(f"At most {k} weighings", "Pan L", "Pan R", sub_lbl="Max coins = ?")
            svg_ar = svg_pan_balance_coins(f"{k} وزنات على الأكثر", "الكفة 1", "الكفة 2", sub_lbl="أكبر عدد عملات = ؟")
        elif cmode == "key_match":
            svg_en = svg_pan_balance_coins(f"{n} locks & {n} keys", f"{n} keys", f"{n} locks", sub_lbl="Match all: trials = ?")
            svg_ar = svg_pan_balance_coins(f"{n} أقفال و{n} مفاتيح", f"{n} مفاتيح", f"{n} أقفال", sub_lbl="عدد التجارب = ؟")
        else:
            svg_en = svg_pan_balance_coins(f"Unlock {n} chests", f"{n} keys", f"{n} chests", sub_lbl="Open all: trials = ?")
            svg_ar = svg_pan_balance_coins(f"فتح {n} صناديق مقفلة", f"{n} مفاتيح", f"{n} صناديق", sub_lbl="عدد المحاولات = ؟")
        out.append(
            make_kmc_question(
                qid, LEVEL, "Combinatorics & Logic", diff, "kmc_g89_counterfeit_coin_weighings",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 18. kmc_g89_two_box_transfer_prob (16 Qs, svg_two_jars)
    # ------------------------------------------------------------------
    box_cases = [
        ("same_color", 2, 3, 3, 2, "Easy"),
        ("same_color", 1, 3, 3, 1, "Easy"),
        ("same_color", 3, 1, 2, 2, "Easy"),
        ("at_least_one_red", 1, 2, 1, 3, "Easy"),
        ("at_least_one_red", 2, 3, 1, 4, "Easy"),
        ("same_color", 4, 3, 2, 5, "Medium"),
        ("same_color", 5, 3, 3, 6, "Medium"),
        ("at_least_one_red", 3, 4, 2, 3, "Medium"),
        ("at_least_one_red", 2, 5, 3, 4, "Medium"),
        ("at_least_one_red", 4, 5, 2, 6, "Medium"),
        ("transfer_red", 2, 2, 1, 2, "Medium"),
        ("transfer_red", 3, 1, 2, 3, "Medium"),
        ("transfer_red", 1, 4, 3, 1, "Medium"),
        ("transfer_red", 4, 2, 2, 5, "Hard"),
        ("transfer_red", 3, 5, 4, 3, "Hard"),
        ("transfer_red", 5, 2, 3, 6, "Hard"),
    ]
    for i, (bmode, rA, bA, rB, bB, diff) in enumerate(box_cases, 1):
        nA, nB = rA + bA, rB + bB
        balls_A = ["R"] * rA + ["B"] * bA
        balls_B = ["R"] * rB + ["B"] * bB

        if bmode == "same_color":
            ans = Fraction(rA * rB + bA * bB, nA * nB)
            brute = Fraction(sum(1 for x in balls_A for y in balls_B if x == y), nA * nB)
            assert ans == brute
            svg_en = svg_two_jars(f"A ({rA}R, {bA}B)", rA / nA, f"B ({rB}R, {bB}B)", rB / nB)
            svg_ar = svg_two_jars(f"صندوق A ({rA}ح، {bA}ز)", rA / nA, f"صندوق B ({rB}ح، {bB}ز)", rB / nB)
            q_en = (
                f"**Box A** contains {m(rA)} red and {m(bA)} blue balls, while **Box B** contains {m(rB)} red and {m(bB)} blue balls. "
                f"One ball is drawn at random from **Box A** and one ball is drawn at random from **Box B**. "
                f"What is the probability that the two drawn balls have the **same color**?"
            )
            q_ar = (
                f"يحتوي **الصندوق A** على {m(rA)} كرات حمراء و{m(bA)} كرات زرقاء، ويحتوي **الصندوق B** على {m(rB)} كرات حمراء و{m(bB)} كرات زرقاء. "
                f"سُحبت كرة عشوائياً من **A** وكرة عشوائياً من **B**. ما احتمال أن تكون الكرتان المسحوبتان من **نفس اللون**؟"
            )
            h_en = "Add the two mutually exclusive cases: P(both Red) + P(both Blue)!"
            h_ar = "اجمع الحالتين المتنافيتين: احتمال (الكرتان حمراوان) + احتمال (الكرتان زرقاوان)!"
            s_en = explain_en(
                "'Same color' splits into two disjoint cases: **Both Red** OR **Both Blue**!",
                [
                    f"Probability both are red: {m(f'\\frac{{{rA}}}{{{nA}}} \\times \\frac{{{rB}}}{{{nB}}} = \\frac{{{rA * rB}}}{{{nA * nB}}}')}.",
                    f"Probability both are blue: {m(f'\\frac{{{bA}}}{{{nA}}} \\times \\frac{{{bB}}}{{{nB}}} = \\frac{{{bA * bB}}}{{{nA * nB}}}')}.",
                    f"Add and simplify: {m(f'\\frac{{{rA * rB} + {bA * bB}}}{{{nA * nB}}} = \\frac{{{rA * rB + bA * bB}}}{{{nA * nB}}} = {fmt_val(ans)}')}.",
                ],
                f"Check: P(different colors) = {m(fmt_val(1 - ans))}, and {m(f'{fmt_val(ans)} + {fmt_val(1 - ans)} = 1')}!",
            )
            s_ar = explain_ar(
                "حدث «نفس اللون» ينقسم إلى حالتين منفصلتين: **حمراوان معاً** أو **زرقاوان معاً**!",
                [
                    f"احتمال أن تكونا حمراوين: {m(f'\\frac{{{rA}}}{{{nA}}} \\times \\frac{{{rB}}}{{{nB}}} = \\frac{{{rA * rB}}}{{{nA * nB}}}')}.",
                    f"احتمال أن تكونا زرقاوين: {m(f'\\frac{{{bA}}}{{{nA}}} \\times \\frac{{{bB}}}{{{nB}}} = \\frac{{{bA * bB}}}{{{nA * nB}}}')}.",
                    f"نجمع ونبسّط الكسر: {m(f'\\frac{{{rA * rB + bA * bB}}}{{{nA * nB}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق بالمتمم: احتمال اختلاف اللونين هو {m(fmt_val(1 - ans))} ومجموعهما {m(1)}!",
            )
            distractors = [
                1 - ans if 1 - ans != ans else Fraction(ans.numerator + 1, ans.denominator + 2),
                Fraction(rA * rB, nA * nB),
                Fraction(rA + rB, nA + nB),
                Fraction(min(ans.denominator - 1, ans.numerator + 1), ans.denominator),
            ]
        elif bmode == "at_least_one_red":
            ans = 1 - Fraction(bA * bB, nA * nB)
            brute = Fraction(sum(1 for x in balls_A for y in balls_B if x == "R" or y == "R"), nA * nB)
            assert ans == brute
            svg_en = svg_two_jars(f"A ({rA}R, {bA}B)", rA / nA, f"B ({rB}R, {bB}B)", rB / nB)
            svg_ar = svg_two_jars(f"صندوق A ({rA}ح، {bA}ز)", rA / nA, f"صندوق B ({rB}ح، {bB}ز)", rB / nB)
            q_en = (
                f"**Box A** has {m(rA)} red and {m(bA)} blue balls, and **Box B** has {m(rB)} red and {m(bB)} blue balls. "
                f"If one ball is drawn at random from each box, what is the probability of getting **at least one red ball**?"
            )
            q_ar = (
                f"في **الصندوق A** توجد {m(rA)} كرات حمراء و{m(bA)} كرات زرقاء، وفي **الصندوق B** توجد {m(rB)} كرات حمراء و{m(bB)} كرات زرقاء. "
                f"إذا سُحبت كرة واحدة عشوائياً من كل صندوق، فما احتمال ظهور **كرة حمراء واحدة على الأقل**؟"
            )
            h_en = "Use the Complement Shortcut! 1 − P(NO red balls) = 1 − P(both balls are blue)!"
            h_ar = "استخدم حيلة الحدث المتمم! 1 − احتمال (عدم ظهور أي كرة حمراء) = 1 − احتمال (الكرتان زرقاوان)!"
            s_en = explain_en(
                "Complement rule: \\( P(\\text{at least one red}) = 1 - P(\\text{both blue}) \\)!",
                [
                    f"Probability of blue from Box A is {m(f'\\frac{{{bA}}}{{{nA}}}')}, and blue from Box B is {m(f'\\frac{{{bB}}}{{{nB}}}')}.",
                    f"Probability both are blue: {m(f'\\frac{{{bA}}}{{{nA}}} \\times \\frac{{{bB}}}{{{nB}}} = \\frac{{{bA * bB}}}{{{nA * nB}}}')}.",
                    f"Subtract from {m(1)}: {m(f'1 - \\frac{{{bA * bB}}}{{{nA * nB}}} = {fmt_val(ans)}')}.",
                ],
                f"Trap check: simply adding {m(f'\\frac{{{rA}}}{{{nA}}} + \\frac{{{rB}}}{{{nB}}}')} double-counts the case where **both** balls are red!",
            )
            s_ar = explain_ar(
                "قاعدة الحدث المتمم: \\( P(\\text{واحدة حمراء على الأقل}) = 1 - P(\\text{الكرتان زرقاوان}) \\)!",
                [
                    f"احتمال سحب كرة زرقاء من A هو {m(f'\\frac{{{bA}}}{{{nA}}}')} ومن B هو {m(f'\\frac{{{bB}}}{{{nB}}}')}.",
                    f"احتمال أن تكونا زرقاوين معاً: {m(f'\\frac{{{bA * bB}}}{{{nA * nB}}}')}.",
                    f"نطرح من {m(1)}: {m(f'1 - \\frac{{{bA * bB}}}{{{nA * nB}}} = {fmt_val(ans)}')}.",
                ],
                f"انتبه: جمع الاحتمالين مباشرةً يحسب حالة (حمراوين معاً) مرتين، فطرح المتمم أسرع وأدق!",
            )
            distractors = [
                Fraction(bA * bB, nA * nB),
                Fraction(rA * bB + bA * rB, nA * nB),
                Fraction(rA + rB, nA + nB),
                Fraction(max(1, ans.numerator - 1), ans.denominator),
            ]
        else:
            ans = Fraction(rA * (rB + 1) + bA * rB, nA * (nB + 1))
            hits = 0
            tot_paths = 0
            for ball_moved in balls_A:
                new_B = balls_B + [ball_moved]
                for drawn in new_B:
                    tot_paths += 1
                    if drawn == "R":
                        hits += 1
            assert ans == Fraction(hits, tot_paths)
            svg_en = svg_two_jars(f"A ({rA}R, {bA}B)", rA / nA, f"B ({rB}R, {bB}B)", rB / nB, arrow_txt="1 ball")
            svg_ar = svg_two_jars(f"صندوق A ({rA}ح، {bA}ز)", rA / nA, f"صندوق B ({rB}ح، {bB}ز)", rB / nB, arrow_txt="كرة واحدة")
            q_en = (
                f"**Box A** contains {m(rA)} red and {m(bA)} blue balls; **Box B** contains {m(rB)} red and {m(bB)} blue balls. "
                f"One ball is chosen at random from **Box A** and transferred unseen into **Box B**. Then one ball is drawn at random "
                f"from **Box B**. What is the probability that the ball drawn from **Box B** is **red**?"
            )
            q_ar = (
                f"يحتوي **الصندوق A** على {m(rA)} كرات حمراء و{m(bA)} كرات زرقاء، ويحتوي **الصندوق B** على {m(rB)} كرات حمراء و{m(bB)} كرات زرقاء. "
                f"نُقلت كرة واحدة عشوائياً دون النظر إليها من **A** إلى **B**، ثم سُحبت كرة عشوائياً من **B**. "
                f"ما احتمال أن تكون الكرة المسحوبة من **الصندوق B** **حمراء**؟"
            )
            h_en = f"Split into two cases by what moved from A to B (Box B now has {nB + 1} balls!): Case 1 (Red moved) + Case 2 (Blue moved)!"
            h_ar = f"قسّم الحل إلى حالتين بحسب لون الكرة المنقولة من A إلى B (أصبح في B الآن {nB + 1} كرات!): الحالة 1 (انتقلت حمراء) + الحالة 2 (انتقلت زرقاء)!"
            s_en = explain_en(
                f"After moving 1 ball, Box B holds **{m(nB + 1)} balls**. Split into **Case 1 (Red transferred)** and **Case 2 (Blue transferred)**!",
                [
                    f"**Case 1 (Red moved):** probability {m(f'\\frac{{{rA}}}{{{nA}}}')}, leaving {m(rB + 1)} red out of {m(nB + 1)} in B {m(f'\\implies \\frac{{{rA}}}{{{nA}}} \\times \\frac{{{rB + 1}}}{{{nB + 1}}} = \\frac{{{rA * (rB + 1)}}}{{{nA * (nB + 1)}}}')}.",
                    f"**Case 2 (Blue moved):** probability {m(f'\\frac{{{bA}}}{{{nA}}}')}, leaving {m(rB)} red out of {m(nB + 1)} in B {m(f'\\implies \\frac{{{bA}}}{{{nA}}} \\times \\frac{{{rB}}}{{{nB + 1}}} = \\frac{{{bA * rB}}}{{{nA * (nB + 1)}}}')}.",
                    f"Add both cases and simplify: {m(f'\\frac{{{rA * (rB + 1)} + {bA * rB}}}{{{nA * (nB + 1)}}} = \\frac{{{rA * (rB + 1) + bA * rB}}}{{{nA * (nB + 1)}}} = {fmt_val(ans)}')}.",
                ],
                f"Check: P(Blue from B) = {m(fmt_val(1 - ans))}, and {m(f'{fmt_val(ans)} + {fmt_val(1 - ans)} = 1')}!",
            )
            s_ar = explain_ar(
                f"بعد نقل كرة واحدة يصبح في الصندوق B **{m(nB + 1)} كرات**. نقسّم المسألة إلى **الحالة 1 (نُقلت حمراء)** و**الحالة 2 (نُقلت زرقاء)**!",
                [
                    f"**الحالة 1 (نُقلت حمراء):** احتمالها {m(f'\\frac{{{rA}}}{{{nA}}}')} ويصبح في B عدد {m(rB + 1)} حمراء من {m(nB + 1)} {m(f'\\implies \\frac{{{rA * (rB + 1)}}}{{{nA * (nB + 1)}}}')}.",
                    f"**الحالة 2 (نُقلت زرقاء):** احتمالها {m(f'\\frac{{{bA}}}{{{nA}}}')} ويبقى في B عدد {m(rB)} حمراء من {m(nB + 1)} {m(f'\\implies \\frac{{{bA * rB}}}{{{nA * (nB + 1)}}}')}.",
                    f"نجمع الحالتين ونبسّط: {m(f'\\frac{{{rA * (rB + 1) + bA * rB}}}{{{nA * (nB + 1)}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق: احتمال سحب زرقاء من B في النهاية يساوي {m(fmt_val(1 - ans))} ومجموعهما يساوي {m(1)}!",
            )
            distractors = [
                Fraction(rB, nB),
                Fraction(rB + 1, nB + 1),
                Fraction(rA + rB, nA + nB),
                1 - ans if 1 - ans != ans else Fraction(ans.numerator + 1, ans.denominator + 2),
            ]

        qid = f"KMC-T2-EX-26C-{i:02d}"
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        out.append(
            make_kmc_question(
                qid, LEVEL, "Data & Probability", diff, "kmc_g89_two_box_transfer_prob",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(out) == 50
    return out


def generate_t2_extra() -> list[dict]:
    """Generate all 300 verified Track 2 (Grades 8-9) extra KMC questions across 18 blueprints."""
    items = (
        _gen_lesson_2_1()
        + _gen_lesson_2_2()
        + _gen_lesson_2_3()
        + _gen_lesson_2_4()
        + _gen_lesson_2_5()
        + _gen_lesson_2_6()
    )
    assert len(items) == 300, f"Expected 300 Track 2 extra items, got {len(items)}"
    for idx, q in enumerate(items, 1):
        q["id"] = f"KAUST-G89-EX-{idx:03d}"
    return items
