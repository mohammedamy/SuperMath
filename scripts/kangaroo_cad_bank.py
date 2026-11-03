"""Kangaroo Math Competition — Cadet Division (Grades 7–8) Question Bank (360 Questions).

Covers all 24 Cadet blueprints (6 units × 4 blueprints × 15 questions = 360 MCQ items):
- 120 Easy (3-point), 120 Medium (4-point), 120 Hard (5-point)
- Every answer is computed programmatically in Python with targeted Kangaroo distractors.
"""
from fractions import Fraction
import math

from kangaroo_common import (
    fmt_val,
    m,
    make_kang_q,
    svg_area_identity_square,
    svg_balance_scales,
    svg_bar_chart,
    svg_binary_bulbs,
    svg_cube_net,
    svg_cube_stack_3d,
    svg_digit_slots,
    svg_factor_tree,
    svg_fraction_grid,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_inscribed_corner_triangle_in_rect,
    svg_kang_cube_faces,
    svg_kang_grid_walk,
    svg_kang_necklace_beads,
    svg_kang_number_pyramid,
    svg_kang_overlapping_rects,
    svg_kang_polyomino_board,
    svg_midpoint_square_shaded,
    svg_motion_timeline,
    svg_number_strip,
    svg_number_triangle_puzzle,
    svg_painted_cube_3d,
    svg_parallel_zigzag,
    svg_pie_chart,
    svg_spinner,
    svg_square_circle_shaded,
    svg_square_eighths_shaded,
    svg_street_grid,
    svg_subdivided_rect_2x2,
    svg_subdivided_rect_3x3,
    svg_trapezoid_semicircle,
    svg_two_jars,
    svg_venn_3,
    wrap_svg,
    _nlabel,
    STROKE,
    SHADE,
    WATER,
    BLUE,
    RED,
    ORANGE,
    DARK,
)

LEVEL = "Cadet"


def _qid(idx: int) -> str:
    return f"KANG-CAD-{idx:03d}"


def _prime_factors(n: int) -> dict[int, int]:
    pf: dict[int, int] = {}
    d = 2
    x = n
    while d * d <= x:
        while x % d == 0:
            pf[d] = pf.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        pf[x] = pf.get(x, 0) + 1
    return pf


def _fmt_pf(pf: dict[int, int]) -> str:
    parts = [f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(pf.items())]
    return " \\times ".join(parts)


def _unit_1() -> list[dict]:
    """Unit 1 (Lesson 3.1 — Number Theory): QIDs 001..060."""
    qs: list[dict] = []
    idx = 1

    # 1. kang_cad_prime_factor_squares (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_sq = [
        (240, "16", "15", "3", "5", "a Kangaroo mosaic badge pack", "حزمة شارات فسيفساء الكانجارو"),
        (360, "8", "45", "9", "5", "an astronomy club tile box", "صندوق بلاط نادي الفلك"),
        (336, "16", "21", "3", "7", "a botanical garden paving lot", "مجموعة رصف الحديقة النباتية"),
        (294, "6", "49", "7", "7", "a science museum floor kit", "مجموعة أرضية متحف العلوم"),
        (880, "16", "55", "5", "11", "a stadium banner grid", "شبكة لافتة الاستاد"),
    ]
    for n_val, l_lbl, r_lbl, rl_lbl, rr_lbl, ctx_en, ctx_ar in easy_sq:
        pf = _prime_factors(n_val)
        ans = math.prod(p for p, e in pf.items() if e % 2 == 1)
        assert math.isqrt(n_val * ans) ** 2 == n_val * ans
        pf_s = _fmt_pf(pf)
        root_v = math.isqrt(n_val * ans)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Easy", "kang_cad_prime_factor_squares",
            f"In {ctx_en}, each carton holds {m(n_val)} identical unit square tiles. What is the smallest positive number of cartons {m('k')} needed so that all {m(f'{n_val}k')} tiles can form one solid **square** without leftover tiles?",
            f"في {ctx_ar}، تحتوي كل علبة على {m(n_val)} بلاطة مربعة متطابقة. ما أصغر عدد موجب من العلب {m('k')} يلزم لترتيب جميع البلاطات البالغ عددها {m(f'{n_val}k')} على شكل **مربع كامل** مصمت دون باقٍ؟",
            ans, [ans * 2, max(2, ans - 3), ans + 4, ans * 3],
            f"Factor {m(n_val)} into primes and multiply one copy of each prime that has an odd exponent.",
            f"حلّل العدد {m(n_val)} إلى عوامله الأولية واضرب في كل عامل أولي أسّه فردي.",
            "A positive integer is a perfect square if and only if every prime factor has an even exponent.",
            [
                f"Factor {m(n_val)} into primes: {m(f'{n_val} = {pf_s}')}.",
                "Identify every prime with an odd exponent—each needs one additional factor to make its exponent even.",
                f"Multiplying those primes gives the minimum carton count {m(f'k = {ans}')}.",
            ],
            f"{m(f'{n_val} \\times {ans} = {n_val * ans} = {root_v}^2')}, a perfect square.",
            "يكون العدد مربعاً كاملاً إذا وفقط إذا كانت جميع أسس عوامله الأولية زوجية.",
            [
                f"نحلّل {m(n_val)} إلى عوامله الأولية: {m(f'{n_val} = {pf_s}')}.",
                "نحدّد العوامل الأولية ذات الأسس الفردية، إذ يحتاج كلٌّ منها إلى عامل إضافي واحد ليصبح أسّه زوجياً.",
                f"بضرب هذه العوامل معاً نحصل على أصغر قيمة {m(f'k = {ans}')}.",
            ],
            f"تحقق: {m(f'{n_val} \\times {ans} = {n_val * ans} = {root_v}^2')} مربع كامل.",
            diagram_en=svg_factor_tree(str(n_val), l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))
        idx += 1

    med_cube = [
        (180, "4", "45", "9", "5", "Tariq"),
        (360, "8", "45", "9", "5", "Lina"),
        (392, "8", "49", "7", "7", "Omar"),
        (432, "16", "27", "9", "3", "Salma"),
        (900, "36", "25", "5", "5", "Ziad"),
    ]
    for n_val, l_lbl, r_lbl, rl_lbl, rr_lbl, person in med_cube:
        pf = _prime_factors(n_val)
        ans = math.prod(p ** ((-e) % 3) for p, e in pf.items())
        cube_prod = n_val * ans
        croot = round(cube_prod ** (1 / 3))
        assert croot ** 3 == cube_prod
        pf_s = _fmt_pf(pf)
        sq_trap = math.prod(p for p, e in pf.items() if e % 2 == 1)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Medium", "kang_cad_prime_factor_squares",
            f"{person} writes the integer {m(n_val)} on a Kangaroo chalkboard and wants to multiply it by the smallest positive integer {m('m')} so that {m(f'{n_val} \\times m')} is a **perfect cube**. What is {m('m')}?",
            f"يكتب ({person}) العدد {m(n_val)} على سبورة الكانجارو ويريد ضربه في أصغر عدد صحيح موجب {m('m')} بحيث يصبح الناتج {m(f'{n_val} \\times m')} **مكعباً كاملاً**. ما قيمة {m('m')}؟",
            ans, [sq_trap, ans * 2, max(2, ans // 2 if ans > 3 else ans + 2), ans + 6],
            "In a perfect cube, every prime exponent must be a multiple of 3 (such as 3 or 6).",
            "في المكعب الكامل يجب أن يكون أسّ كل عامل أولي من مضاعفات 3 (مثل 3 أو 6).",
            "Raise each prime factor's exponent in the factorization up to the next multiple of 3.",
            [
                f"Write the prime factorization: {m(f'{n_val} = {pf_s}')}.",
                "For a perfect cube, each prime exponent must reach a multiple of 3.",
                f"Supplying the missing prime powers gives {m(f'm = {ans}')}.",
            ],
            f"{m(f'{n_val} \\times {ans} = {cube_prod} = {croot}^3')}, an exact cube.",
            "نرفع أسّ كل عامل أولي في التحليل إلى أقرب مضاعف للعدد 3.",
            [
                f"نكتب التحليل الأولي للعدد: {m(f'{n_val} = {pf_s}')}.",
                "لكي يصبح الناتج مكعباً كاملاً يجب أن يصبح كل أسّ من مضاعفات 3.",
                f"بتعويض العوامل الناقصة نجد أصغر مضروب {m(f'm = {ans}')}.",
            ],
            f"تحقق: {m(f'{n_val} \\times {ans} = {cube_prod} = {croot}^3')} مكعب كامل.",
            diagram_en=svg_factor_tree(str(n_val), l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))
        idx += 1

    hard_sq_divs = [
        (1440, "32", "45", "9", "5"),
        (2700, "27", "100", "4", "25"),
        (1296, "16", "81", "9", "9"),
        (3600, "16", "225", "9", "25"),
        (32400, "16", "2025", "81", "25"),
    ]
    for n_val, l_lbl, r_lbl, rl_lbl, rr_lbl in hard_sq_divs:
        pf = _prime_factors(n_val)
        ans = math.prod((e // 2) + 1 for e in pf.values())
        tot_divs = math.prod(e + 1 for e in pf.values())
        pf_s = _fmt_pf(pf)
        choices_s = " \\times ".join(str((e // 2) + 1) for _, e in sorted(pf.items()))
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Hard", "kang_cad_prime_factor_squares",
            f"How many positive divisors of {m(n_val)} are **perfect squares** (including {m(1)})?",
            f"كم قاسماً موجباً للعدد {m(n_val)} يُعدّ **مربعاً كاملاً** (بما في ذلك العدد {m(1)})؟",
            ans, [ans - 1, ans + 2, tot_divs // 2, ans * 2],
            "A divisor is a perfect square iff each of its prime exponents is even (0, 2, 4, ...).",
            "يكون القاسم مربعاً كاملاً إذا وفقط إذا كان أسّ كل عامل أولي فيه زوجياً (0، 2، 4، ...).",
            "Count the allowed even exponents \\( 0, 2, \\dots, 2\\lfloor e_i/2 \\rfloor \\) for each prime factor and multiply.",
            [
                f"Factor {m(n_val)} completely into primes: {m(f'{n_val} = {pf_s}')}.",
                "A square divisor can only choose **even** exponents (including 0) up to each prime's exponent.",
                f"Multiplying the numbers of even-exponent choices gives {m(f'{choices_s} = {ans}')} square divisors.",
            ],
            f"Every combination of even exponents produces a distinct square divisor (from {m(1)} up to the largest square factor).",
            "احسب عدد الأسس الزوجية المتاحة لكل عامل أولي (بما فيها الصفر) ثم اضرب الخيارات معاً.",
            [
                f"نحلّل {m(n_val)} إلى عوامله الأولية: {m(f'{n_val} = {pf_s}')}.",
                "يختار القاسم المربع أسساً **زوجية** فقط (0، 2، 4، ...) لا تتجاوز الأس الأصلي لكل عامل.",
                f"بضرب أعداد الخيارات الزوجية نحصل على {m(f'{choices_s} = {ans}')} قواسم مربعة.",
            ],
            f"تحقق: كل اختيار لأسس زوجية يولّد قاسماً مربعاً وحيداً بدءاً من {m(1)}.",
            diagram_en=svg_factor_tree(str(n_val), l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))
        idx += 1

    # 2. kang_cad_gcd_lcm_product (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_gl = [
        (14, 210, 42, "badge codes"),
        (15, 360, 45, "relay bibs"),
        (18, 252, 36, "vault keys"),
        (16, 336, 48, "beacon intervals"),
        (21, 420, 84, "puzzle cards"),
    ]
    for g, L, a, label_en in easy_gl:
        b = (g * L) // a
        assert math.gcd(a, b) == g and math.lcm(a, b) == L
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Easy", "kang_cad_gcd_lcm_product",
            f"Two Cadet {label_en} carry positive integers {m('a')} and {m('b')} with {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. If {m(f'a = {a}')}, what is {m('b')}?",
            f"يحمل زوج من البطاقات في مسابقة كاديت عددين صحيحين موجبين {m('a')} و{m('b')} يحققان {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. إذا كان {m(f'a = {a}')}، فما قيمة {m('b')}؟",
            b, [L // a * 2, b - g, b + g, L - a],
            "Use the fundamental identity \\( a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b) \\).",
            "استخدم المتطابقة الأساسية \\( a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b) \\).",
            "Divide the product \\( \\gcd(a,b) \\cdot \\operatorname{lcm}(a,b) \\) by \\( a \\).",
            [
                f"Apply {m('a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b)')}.",
                f"Substitute the known values: {m(f'{a} \\times b = {g} \\times {L} = {g * L}')}.",
                f"Divide by {m(a)}: {m(f'b = {g * L} \\div {a} = {b}')}.",
            ],
            f"{m(f'\\gcd({a}, {b}) = {g}')} and {m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}.",
            "اقسم حاصل الضرب \\( \\gcd(a,b) \\cdot \\operatorname{lcm}(a,b) \\) على العدد المعلوم \\( a \\).",
            [
                f"نطبّق العلاقة {m('a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b)')}.",
                f"نعوّض بالقيم المعطاة: {m(f'{a} \\times b = {g} \\times {L} = {g * L}')}.",
                f"بالقسمة على {m(a)} نجد {m(f'b = {b}')}.",
            ],
            f"تحقق: {m(f'\\gcd({a}, {b}) = {g}')} و{m(f'\\operatorname{{lcm}}({a}, {b}) = {L}')}.",
            diagram_en=svg_number_strip([f"gcd={g}", f"a={a}", "b=?", f"lcm={L}"]),
        ))
        idx += 1

    med_gl = [(8, 120), (9, 189), (7, 245), (11, 242), (6, 210)]
    for g, L in med_gl:
        q_prod = L // g
        pairs = [(x, q_prod // x) for x in range(2, q_prod) if q_prod % x == 0 and x < q_prod // x and math.gcd(x, q_prod // x) == 1]
        assert len(pairs) == 1
        x, y = pairs[0]
        a, b = g * x, g * y
        ans = a + b
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Medium", "kang_cad_gcd_lcm_product",
            f"Integers {m('a')} and {m('b')} satisfy {m('1 < a < b')}, {m(f'\\gcd(a, b) = {g}')}, and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. Given that {m('a')} does **not** divide {m('b')}, what is {m('a + b')}?",
            f"عددان صحيحان {m('a')} و{m('b')} يحققان {m('1 < a < b')} و{m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. إذا علمت أن {m('a')} **لا يقسم** {m('b')}، فما قيمة {m('a + b')}؟",
            ans, [g + L, ans - g, ans + g, g * (q_prod - 1)],
            f"Write \\( a = {g}x \\) and \\( b = {g}y \\) with \\( \\gcd(x,y) = 1 \\), so \\( x y = {q_prod} \\) and \\( x > 1 \\).",
            f"اكتب \\( a = {g}x \\) و\\( b = {g}y \\) مع \\( \\gcd(x,y) = 1 \\)، فيكون \\( x y = {q_prod} \\) و\\( x > 1 \\).",
            "Factor \\( \\operatorname{lcm} / \\gcd \\) into two coprime integers greater than 1.",
            [
                f"Set {m(f'a = {g}x')} and {m(f'b = {g}y')} with {m('1 < x < y')} and {m('\\gcd(x, y) = 1')}.",
                f"Then {m(f'{g}xy = {L} \\implies xy = {q_prod}')}.",
                f"Since {m('x > 1')}, the unique coprime pair is {m(f'(x, y) = ({x}, {y})')}, giving {m(f'a = {a},\\; b = {b}')} and {m(f'a + b = {ans}')}.",
            ],
            f"{m(f'\\gcd({a},{b}) = {g}')}, {m(f'\\operatorname{{lcm}}({a},{b}) = {L}')}, and {m(f'{a} \\nmid {b}')}.",
            "حلّل خارج قسمة المضاعف على القاسم إلى عاملين أوليين نسبياً أكبر من 1.",
            [
                f"نضع {m(f'a = {g}x')} و{m(f'b = {g}y')} مع {m('1 < x < y')} و{m('\\gcd(x, y) = 1')}.",
                f"منه {m(f'{g}xy = {L} \\implies xy = {q_prod}')}.",
                f"بما أن {m('x > 1')} فإن الزوج الوحيد هو {m(f'({x}, {y})')}، فيكون {m(f'a = {a}')} و{m(f'b = {b}')} والمجموع {m(ans)}.",
            ],
            f"تحقق: {m(f'{a} + {b} = {ans}')} ولا يقسم أحدهما الآخر.",
            diagram_en=svg_number_strip([f"gcd={g}", f"xy={q_prod}", "a+b=?", f"lcm={L}"]),
        ))
        idx += 1

    hard_gl = [(5, 300), (6, 504), (4, 360), (3, 396), (8, 560)]
    for g, L in hard_gl:
        q_prod = L // g
        coprime_sums = [g * (x + q_prod // x) for x in range(1, int(math.isqrt(q_prod)) + 1) if q_prod % x == 0 and math.gcd(x, q_prod // x) == 1]
        ans = min(coprime_sums)
        non_coprime = [g * (x + q_prod // x) for x in range(1, int(math.isqrt(q_prod)) + 1) if q_prod % x == 0 and math.gcd(x, q_prod // x) > 1]
        trap_nc = min(non_coprime) if non_coprime else ans - g
        best_x = max(x for x in range(1, int(math.isqrt(q_prod)) + 1) if q_prod % x == 0 and math.gcd(x, q_prod // x) == 1)
        best_y = q_prod // best_x
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Hard", "kang_cad_gcd_lcm_product",
            f"Positive integers {m('a')} and {m('b')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. What is the **smallest** possible value of {m('a + b')}?",
            f"عددان صحيحان موجبان {m('a')} و{m('b')} يحققان {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. ما **أصغر** قيمة ممكنة للمجموع {m('a + b')}؟",
            ans, [trap_nc, sorted(coprime_sums)[1], ans + g, g * (1 + q_prod)],
            f"Write \\( xy = {q_prod} \\) with \\( \\gcd(x, y) = 1 \\), and pick \\( x \\) and \\( y \\) as close together as possible!",
            f"اكتب \\( xy = {q_prod} \\) مع الشرط \\( \\gcd(x, y) = 1 \\)، واختر العاملين \\( x, y \\) متقاربين قدر الإمكان!",
            "To minimize \\( g(x + y) \\) for fixed product \\( xy \\), choose the closest **coprime** factor pair.",
            [
                f"Let {m(f'a = {g}x')} and {m(f'b = {g}y')} with {m('\\gcd(x, y) = 1')}, so {m(f'xy = {L} \\div {g} = {q_prod}')}.",
                f"Test factor pairs of {m(q_prod)} near {m(f'\\sqrt{{{q_prod}}}')}, discarding any pair with {m('\\gcd(x,y) > 1')}.",
                f"The closest coprime pair is {m(f'({best_x}, {best_y})')}, giving {m(f'a + b = {g}({best_x} + {best_y}) = {ans}')}.",
            ],
            f"{m(f'\\gcd({g*best_x}, {g*best_y}) = {g}')} and {m(f'\\operatorname{{lcm}}({g*best_x}, {g*best_y}) = {L}')}.",
            "لتصغير المجموع \\( g(x + y) \\) عند ثبات الجداء، نختار أقرب عاملين **أوليين نسبياً**.",
            [
                f"نضع {m(f'a = {g}x')} و{m(f'b = {g}y')} مع {m('\\gcd(x, y) = 1')} فيكون {m(f'xy = {q_prod}')}.",
                f"نفحص أزواج عوامل {m(q_prod)} القريبة من الجذر التربيعي مع استبعاد الأزواج غير الأولية نسبياً.",
                f"أقرب زوج أولي نسبياً هو {m(f'({best_x}, {best_y})')}، ومنه أصغر مجموع {m(f'{g}({best_x}+{best_y}) = {ans}')}.",
            ],
            f"تحقق: العددان {m(g*best_x)} و{m(g*best_y)} قاسمهما {m(g)} ومضاعفهما {m(L)} ومجموعهما {m(ans)}.",
            diagram_en=svg_number_strip([f"gcd={g}", f"xy={q_prod}", "min(a+b)", f"lcm={L}"]),
        ))
        idx += 1

    # 3. kang_cad_digit_sum_reversal (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_rev = [(7, 5), (7, 3), (8, 5), (7, 2), (7, 4)]
    for a_d, b_d in easy_rev:
        n_orig = 10 * a_d + b_d
        n_rev = 10 * b_d + a_d
        s_val = n_orig + n_rev
        diff_d = a_d - b_d
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Easy", "kang_cad_digit_sum_reversal",
            f"A two-digit number {m('\\overline{ab}')} added to its digit-reversal {m('\\overline{ba}')} equals {m(s_val)}. If the tens digit exceeds the units digit by {m(diff_d)} (so {m(f'a - b = {diff_d}')}), what is {m('\\overline{ab}')}?",
            f"عدد مكوّن من رقمين {m('\\overline{ab}')} مجموعُه مع معكوس أرقامه {m('\\overline{ba}')} يساوي {m(s_val)}. إذا كان رقم عشراته يزيد على رقم آحاده بمقدار {m(diff_d)} (أي {m(f'a - b = {diff_d}')})، فما العدد {m('\\overline{ab}')}؟",
            n_orig, [n_rev, n_orig + 9, n_orig - 11, n_orig + 11],
            "Use \\( \\overline{ab} + \\overline{ba} = 11(a + b) \\) to find \\( a + b \\) immediately.",
            "استخدم المتطابقة \\( \\overline{ab} + \\overline{ba} = 11(a + b) \\) لإيجاد \\( a + b \\) مباشرة.",
            "Divide the sum by 11 to obtain \\( a + b \\), then combine with \\( a - b \\).",
            [
                f"Since {m('(10a + b) + (10b + a) = 11(a + b) = ' + str(s_val))}, divide by {m(11)} to get {m(f'a + b = {a_d + b_d}')}.",
                f"Combine {m(f'a + b = {a_d + b_d}')} with {m(f'a - b = {diff_d}')}: adding gives {m(f'2a = {2 * a_d} \\implies a = {a_d}')}.",
                f"Then {m(f'b = {b_d}')}, so the original number is {m(n_orig)}.",
            ],
            f"{m(f'{n_orig} + {n_rev} = {s_val}')} and {m(f'{a_d} - {b_d} = {diff_d}')}.",
            "اقسم المجموع على 11 لإيجاد \\( a + b \\) ثم اجمع المعادلتين.",
            [
                f"بما أن {m(f'11(a + b) = {s_val}')} فإن {m(f'a + b = {a_d + b_d}')}.",
                f"بجمعها مع {m(f'a - b = {diff_d}')} نجد {m(f'2a = {2 * a_d} \\implies a = {a_d}')} ومنها {m(f'b = {b_d}')}.",
                f"إذن العدد الأصلي هو {m(n_orig)}.",
            ],
            f"تحقق: {m(f'{n_orig} + {n_rev} = {s_val}')}.",
            diagram_en=svg_digit_slots(["a", "b"], f"ab + ba = {s_val}"),
        ))
        idx += 1

    med_rev = [(8, 5, 3), (7, 2, 4), (9, 6, 2), (8, 1, 4), (9, 3, 5)]
    for a_d, b_d, c_d in med_rev:
        n_orig = 100 * a_d + 10 * b_d + c_d
        n_rev = 100 * c_d + 10 * b_d + a_d
        diff_v = n_orig - n_rev
        d_sum = a_d + b_d + c_d
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Medium", "kang_cad_digit_sum_reversal",
            f"A 3-digit Kangaroo code {m('\\overline{abc}')} satisfies {m(f'\\overline{{abc}} - \\overline{{cba}} = {diff_v}')}, its middle digit is {m(f'b = {b_d}')}, and the sum of its three digits is {m(d_sum)}. What is {m('\\overline{abc}')}?",
            f"شفرة ثلاثية الخانات {m('\\overline{abc}')} تحقق {m(f'\\overline{{abc}} - \\overline{{cba}} = {diff_v}')}، ورقمها الأوسط {m(f'b = {b_d}')}، ومجموع أرقامها الثلاثة {m(d_sum)}. ما العدد {m('\\overline{abc}')}؟",
            n_orig, [n_rev, n_orig - 99, n_orig - 9, 100 * (a_d - 1) + 10 * b_d + (c_d + 1)],
            "Apply \\( \\overline{abc} - \\overline{cba} = 99(a - c) \\) to get \\( a - c \\).",
            "طبّق القاعدة \\( \\overline{abc} - \\overline{cba} = 99(a - c) \\) لإيجاد الفرق \\( a - c \\).",
            "Divide the reversal difference by 99 to find \\( a - c \\), and use the digit sum to find \\( a + c \\).",
            [
                f"From {m(f'99(a - c) = {diff_v}')}, divide by {m(99)} to obtain {m(f'a - c = {a_d - c_d}')}.",
                f"Since {m(f'b = {b_d}')} and {m(f'a + b + c = {d_sum}')}, we have {m(f'a + c = {a_d + c_d}')}.",
                f"Solving gives {m(f'a = {a_d}')} and {m(f'c = {c_d}')}, so {m(f'\\overline{{abc}} = {n_orig}')}.",
            ],
            f"{m(f'{n_orig} - {n_rev} = {diff_v}')} and {m(f'{a_d} + {b_d} + {c_d} = {d_sum}')}.",
            "اقسم فرق العدد ومعكوسه على 99 لإيجاد \\( a - c \\) واستنتج \\( a + c \\) من مجموع الأرقام.",
            [
                f"من {m(f'99(a - c) = {diff_v}')} نجد {m(f'a - c = {a_d - c_d}')}.",
                f"وبما أن {m(f'b = {b_d}')} فإن {m(f'a + c = {d_sum} - {b_d} = {a_d + c_d}')}.",
                f"بحل المعادلتين نجد {m(f'a = {a_d},\\; c = {c_d}')} والعدد هو {m(n_orig)}.",
            ],
            f"تحقق: {m(f'{n_orig} - {n_rev} = {diff_v}')}.",
            diagram_en=svg_digit_slots(["a", str(b_d), "c"], f"abc − cba = {diff_v}"),
        ))
        idx += 1

    hard_nsn = [247, 356, 463, 538, 645]
    for n_target in hard_nsn:
        sn = sum(int(ch) for ch in str(n_target))
        tot_t = n_target + sn
        sols = [x for x in range(1, 1000) if x + sum(int(c) for c in str(x)) == tot_t]
        assert sols == [n_target], f"Expected unique solution for {tot_t}, got {sols}"
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Hard", "kang_cad_digit_sum_reversal",
            f"When a 3-digit positive integer {m('N')} is added to the sum of its own digits {m('S(N)')}, the result is {m(tot_t)}. What is {m('N')}?",
            f"عند إضافة عدد صحيح موجب مكوّن من 3 أرقام {m('N')} إلى مجموع أرقامه {m('S(N)')} يكون الناتج {m(tot_t)}. ما قيمة {m('N')}؟",
            n_target, [n_target - 9, n_target + 9, tot_t - 18, n_target + 2],
            f"For any 3-digit number, \\( 1 \\le S(N) \\le 27 \\), so \\( N \\) lies between \\( {tot_t - 27} \\) and \\( {tot_t - 1} \\), and \\( 2N \\equiv {tot_t} \\pmod 9 \\)!",
            f"لأي عدد من 3 أرقام يكون \\( 1 \\le S(N) \\le 27 \\)، أي أن \\( N \\) محصور بين \\( {tot_t - 27} \\) و\\( {tot_t - 1} \\)، كما أن \\( 2N \\equiv {tot_t} \\pmod 9 \\)!",
            "Bound \\( N \\) within \\( [T - 27, T - 1] \\) and use modulo-9 remainder \\( N \\equiv S(N) \\pmod 9 \\) to pinpoint \\( N \\).",
            [
                f"Since {m('N')} has 3 digits, {m('1 \\le S(N) \\le 27')}, forcing {m(f'{tot_t - 27} \\le N \\le {tot_t - 1}')}.",
                f"Because {m('N \\equiv S(N) \\pmod 9')}, we have {m(f'2N \\equiv N + S(N) = {tot_t} \\equiv {tot_t % 9} \\pmod 9')}, so {m(f'N \\equiv {(tot_t * 5) % 9} \\pmod 9')}.",
                f"Testing the multiples in {m(f'[{tot_t - 27}, {tot_t - 1}]')} gives the unique solution {m(f'N = {n_target}')} (with {m(f'S(N) = {sn}')}).",
            ],
            f"{m(f'{n_target} + ({str(n_target)[0]} + {str(n_target)[1]} + {str(n_target)[2]}) = {n_target} + {sn} = {tot_t}')}.",
            "احصر \\( N \\) في الفترة \\( [T - 27, T - 1] \\) واستخدم التطابق \\( 2N \\equiv T \\pmod 9 \\).",
            [
                f"بما أن {m('1 \\le S(N) \\le 27')} فإن {m(f'{tot_t - 27} \\le N \\le {tot_t - 1}')}.",
                f"وبما أن {m('N \\equiv S(N) \\pmod 9')} فإن {m(f'2N \\equiv {tot_t} \\pmod 9')} أي {m(f'N \\equiv {(tot_t * 5) % 9} \\pmod 9')}.",
                f"بفحص القيم المحصورة نجد الحل الوحيد {m(f'N = {n_target}')} حيث {m(f'S(N) = {sn}')}.",
            ],
            f"تحقق: {m(f'{n_target} + {sn} = {tot_t}')}.",
            diagram_en=svg_function_machine("N", "+ S(N)", "mod 9", str(tot_t)),
        ))
        idx += 1

    # 4. kang_cad_power_units_cycle (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_pow = [(2023, 74), (2022, 95), (2027, 81), (2028, 64), (2024, 53)]
    for base, exp in easy_pow:
        u = base % 10
        ans = pow(u, exp, 10)
        rem = exp % 4
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Easy", "kang_cad_power_units_cycle",
            f"What is the units digit of {m(f'{base}^{{{exp}}}')}?",
            f"ما رقم الآحاد للعدد {m(f'{base}^{{{exp}}}')}؟",
            ans, [(ans + 2) % 10, (ans + 4) % 10, (ans + 6) % 10, 1 if ans != 1 else 3],
            f"Keep only the base's last digit {m(u)} and reduce the exponent {m(exp)} modulo 4.",
            f"احتفظ بآحاد الأساس {m(u)} فقط واحسب باقي قسمة الأس {m(exp)} على 4.",
            "The units digits of integer powers repeat every 4 steps (or 2 steps for 4 and 9).",
            [
                f"Only the units digit {m(u)} matters: {m(f'{base}^{{{exp}}}')} ends in the same digit as {m(f'{u}^{{{exp}}}')}.",
                f"Divide {m(exp)} by {m(4)}: remainder is {m(rem)} (where remainder 0 means the 4th term in the cycle).",
                f"Evaluating the cycle position gives units digit {m(ans)}.",
            ],
            f"Cycle of {m(u)} is {m(f'({u}, {u**2%10}, {u**3%10}, {u**4%10})')}, landing on {m(ans)}.",
            "تتكرر أرقام الآحاد للقوى الصحيحة كل 4 خطوات.",
            [
                f"نأخذ رقم آحاد الأساس فقط، أي نحسب آحاد {m(f'{u}^{{{exp}}}')}.",
                f"باقي قسمة الأس {m(exp)} على {m(4)} هو {m(rem)} (والباقي 0 يعني الحد الرابع في الدورة).",
                f"نجد أن رقم الآحاد يساوي {m(ans)}.",
            ],
            f"تحقق: دورة آحاد {m(u)} هي {m(f'({u}, {u**2%10}, {u**3%10}, {u**4%10})')} وتعطي {m(ans)}.",
            diagram_en=svg_function_machine(f"{u}^{exp}", f"rem {rem}", "cycle", str(ans)),
        ))
        idx += 1

    med_pow = [
        (13, 47, "*", 17, 38),
        (22, 61, "+", 19, 35),
        (18, 51, "*", 14, 26),
        (27, 62, "+", 23, 44),
        (32, 75, "+", 37, 53),
    ]
    for b1, e1, op, b2, e2 in med_pow:
        d1, d2 = pow(b1, e1, 10), pow(b2, e2, 10)
        ans = (d1 * d2) % 10 if op == "*" else (d1 + d2) % 10
        op_tex = "\\times" if op == "*" else "+"
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Number Theory", "Medium", "kang_cad_power_units_cycle",
            f"What is the units digit of {m(f'{b1}^{{{e1}}} {op_tex} {b2}^{{{e2}}}')}?",
            f"ما رقم الآحاد للمقدار {m(f'{b1}^{{{e1}}} {op_tex} {b2}^{{{e2}}}')}؟",
            ans, [(ans + 2) % 10, (ans + 4) % 10, (ans + 5) % 10, (ans + 8) % 10],
            "Find the units digit of each power separately using its 4-step cycle, then combine modulo 10.",
            "أوجد رقم آحاد كل قوة على حدة باستخدام دورتها الرباعية ثم احسب الناتج بآحاد العشرات.",
            "Reduce each base modulo 10 and each exponent modulo 4.",
            [
                f"For {m(f'{b1}^{{{e1}}}')}, base {m(b1 % 10)} at exponent {m(e1)} gives units digit {m(d1)}.",
                f"For {m(f'{b2}^{{{e2}}}')}, base {m(b2 % 10)} at exponent {m(e2)} gives units digit {m(d2)}.",
                f"Combine modulo 10: {m(f'{d1} {op_tex} {d2}')} has units digit {m(ans)}.",
            ],
            f"{m(f'{d1} {op_tex} {d2} \\equiv {ans} \\pmod{{10}}')}.",
            "نبسّط كل أساس إلى رقم آحاده وكل أسّ بباقي قسمته على 4.",
            [
                f"للقوة الأولى {m(f'{b1}^{{{e1}}}')} نجد رقم الآحاد {m(d1)}.",
                f"وللقوة الثانية {m(f'{b2}^{{{e2}}}')} نجد رقم الآحاد {m(d2)}.",
                f"نطبّق العملية على رقمَي الآحاد فنحصل على الآحاد النهائي {m(ans)}.",
            ],
            f"تحقق: {m(f'{d1} {op_tex} {d2} \\equiv {ans} \\pmod{{10}}')}.",
            diagram_en=svg_function_machine(f"{b1%10}^{e1}{op}{b2%10}^{e2}", f"{d1} {op} {d2}", "mod 10", str(ans)),
        ))
        idx += 1

    hard_pow = [
        ("diff", 17, 60, 13, 29),
        ("diff", 23, 52, 12, 35),
        ("diff", 28, 46, 17, 21),
        ("sum_series", 3, 42, 0, 0),
        ("sum_series", 7, 55, 0, 0),
    ]
    for kind, b1, e1, b2, e2 in hard_pow:
        if kind == "diff":
            d1, d2 = pow(b1, e1, 10), pow(b2, e2, 10)
            ans = (d1 - d2) % 10
            trap_abs = abs(d1 - d2)
            qs.append(make_kang_q(
                _qid(idx), LEVEL, "Number Theory", "Hard", "kang_cad_power_units_cycle",
                f"What is the units digit of the positive integer {m(f'{b1}^{{{e1}}} - {b2}^{{{e2}}}')}?",
                f"ما رقم الآحاد للعدد الصحيح الموجب {m(f'{b1}^{{{e1}}} - {b2}^{{{e2}}}')}؟",
                ans, [trap_abs, (ans + 2) % 10, (ans + 4) % 10, (d1 + d2) % 10],
                "Watch out for borrowing! If a giant number ends in a smaller digit than the number subtracted, add 10 before subtracting.",
                "انتبه للاستلاف! إذا كان رقم آحاد المطروح منه أصغر من آحاد المطروح، أضف 10 قبل الطرح.",
                "Compute each units digit modulo 10; when \\( d_1 < d_2 \\), borrow 10 so the last digit is \\( (10 + d_1) - d_2 \\).",
                [
                    f"{m(f'{b1}^{{{e1}}}')} ends in {m(d1)}, while {m(f'{b2}^{{{e2}}}')} ends in {m(d2)} (and {m(f'{b1}^{{{e1}}} > {b2}^{{{e2}}}')}).",
                    f"Since {m(f'{d1} < {d2}')}, subtracting borrows from the tens place: {m(f'(10 + {d1}) - {d2} = {ans}')}.",
                ],
                f"{m(f'({d1} - {d2}) \\bmod 10 = {ans}')} (avoiding the sign trap {m(trap_abs)}!).",
                "عندما يكون آحاد العدد الأكبر أصغر من آحاد العدد الأصغر نستلف 10 من العشرات.",
                [
                    f"آحاد {m(f'{b1}^{{{e1}}}')} هو {m(d1)}، وآحاد {m(f'{b2}^{{{e2}}}')} هو {m(d2)}.",
                    f"بما أن {m(f'{d1} < {d2}')} مع كون العدد الأول أكبر، نستلف {m(10)} فيصبح الآحاد {m(f'10 + {d1} - {d2} = {ans}')}.",
                ],
                f"تحقق: {m(f'({d1} - {d2}) \\bmod 10 = {ans}')}.",
                diagram_en=svg_function_machine(f"{b1}^{e1}−{b2}^{e2}", f"…{d1} − …{d2}", "borrow 10", str(ans)),
            ))
        else:
            ans = sum(pow(b1, k, 10) for k in range(1, e1 + 1)) % 10
            cyc_sum = sum(pow(b1, k, 10) for k in range(1, 5))
            rem = e1 % 4
            qs.append(make_kang_q(
                _qid(idx), LEVEL, "Number Theory", "Hard", "kang_cad_power_units_cycle",
                f"What is the units digit of the sum {m(f'{b1}^1 + {b1}^2 + {b1}^3 + \\cdots + {b1}^{{{e1}}}')}?",
                f"ما رقم الآحاد للمجموع {m(f'{b1}^1 + {b1}^2 + {b1}^3 + \\cdots + {b1}^{{{e1}}}')}؟",
                ans, [(ans + 1) % 10, pow(b1, e1, 10), (ans + 4) % 10, (ans + 7) % 10],
                "Group consecutive powers into blocks of 4 and check the sum of one full 4-term cycle!",
                "جمّع القوى المتتالية في مجموعات من 4 حدود واحسب مجموع الدورة الواحدة!",
                f"Every 4 consecutive powers of {m(b1)} have units digits summing to {m(cyc_sum)} (ending in 0!).",
                [
                    f"One full 4-cycle of units digits of {m(f'{b1}^k')} sums to {m(f'{b1} + {b1**2%10} + {b1**3%10} + {b1**4%10} = {cyc_sum} \\equiv 0 \\pmod{{10}}')}.",
                    f"Dividing {m(e1)} terms into blocks of {m(4)} leaves {m(rem)} leftover terms at the end.",
                    f"Adding the first {m(rem)} cycle digits gives a sum ending in {m(ans)}.",
                ],
                f"All {m(e1 // 4)} full blocks contribute {m(0)} to the units place, leaving {m(ans)}.",
                f"مجموع أرقام الآحاد لكل 4 قوى متتالية للعدد {m(b1)} يساوي {m(cyc_sum)} أي آحاده 0!",
                [
                    f"مجموع آحاد كل دورة رباعية كاملة يساوي {m(f'{cyc_sum} \\equiv 0 \\pmod{{10}}')}.",
                    f"بقسمة عدد الحدود {m(e1)} على {m(4)} يتبقى {m(rem)} حدود في النهاية.",
                    f"بجمع آحاد الحدود الـ {m(rem)} المتبقية نجد رقم الآحاد {m(ans)}.",
                ],
                f"تحقق: المجموعات الـ {m(e1 // 4)} الكاملة آحادها صفر، والباقي يعطي {m(ans)}.",
                diagram_en=svg_number_strip([f"{b1}¹", f"+{b1}²", "+ … +", f"{b1}^{e1}", "u=?"]),
            ))
        idx += 1

    assert len(qs) == 60
    return qs


def _unit_2() -> list[dict]:
    """Unit 2 (Lesson 3.2 — Algebra): QIDs 061..120."""
    qs: list[dict] = []
    idx = 61

    # 1. kang_cad_ratio_jar_transfer (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_jar = [
        (7, 3, 24, "lemonade"),
        (9, 5, 28, "pomegranate juice"),
        (5, 1, 30, "maple syrup"),
        (11, 5, 36, "iced tea"),
        (7, 1, 42, "orange nectar"),
    ]
    for p1, q1, pour_v, liq_en in easy_jar:
        tot_parts = p1 + q1
        half_p = tot_parts // 2
        moved_parts = p1 - half_p
        unit_v = pour_v // moved_parts
        ans = tot_parts * unit_v
        assert (p1 * unit_v - pour_v) == (q1 * unit_v + pour_v)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Easy", "kang_cad_ratio_jar_transfer",
            f"Carafe A and Carafe B contain {liq_en} in the volume ratio {m(f'{p1} : {q1}')}. When {m(f'{pour_v}\\text{{ mL}}')} is poured from Carafe A into Carafe B, both carafes hold the **exact same** volume. What is the total volume of {liq_en} in both carafes combined (in {m('\\text{mL}')})?",
            f"يحتوي الدورق (أ) والدورق (ب) على عصير بنسبة حجمية قدرها {m(f'{p1} : {q1}')}. عند صبّ {m(f'{pour_v}\\text{{ مل}}')} من الدورق (أ) إلى الدورق (ب) يتساوى الحجم في الدورقين تماماً. ما الحجم الكلي للعصير في الدورقين معاً بوحدة {m('\\text{مل}')}؟",
            ans, [ans // 2, (p1 + q1) * (pour_v // (p1 - q1)) if pour_v % (p1 - q1) == 0 else ans - 20, ans + 2 * pour_v, p1 * unit_v],
            f"Total parts = {m(tot_parts)}, so equal volumes correspond to {m(f'{half_p} : {half_p}')} parts!",
            f"مجموع الأجزاء = {m(tot_parts)}، لذا التساوي يعني أن النسبة أصبحت {m(f'{half_p} : {half_p}')}!",
            "Keep total parts constant; the transfer equals the drop from \\( p_1 \\) parts to \\( \\frac{p_1+q_1}{2} \\) parts.",
            [
                f"Initially the carafes have {m(p1)} parts and {m(q1)} parts, for a constant total of {m(tot_parts)} parts.",
                f"When equal, each carafe holds {m(f'{tot_parts} \\div 2 = {half_p}')} parts, so Carafe A loses {m(f'{p1} - {half_p} = {moved_parts}')} parts.",
                f"Thus {m(f'{moved_parts}\\text{{ parts}} = {pour_v}\\text{{ mL}} \\implies 1\\text{{ part}} = {unit_v}\\text{{ mL}}')}, giving total {m(f'{tot_parts} \\times {unit_v} = {ans}\\text{{ mL}}')}.",
            ],
            f"Before: {m(p1*unit_v)} and {m(q1*unit_v)}; after pouring {m(pour_v)}: {m(half_p*unit_v)} and {m(half_p*unit_v)}.",
            "بما أن الحجم الكلي ثابت، فإن الكمية المنقولة تساوي نقصان الدورق الأول من نصيبه الابتدائي إلى نصف المجموع.",
            [
                f"مجموع الأجزاء ثابت ويساوي {m(f'{p1} + {q1} = {tot_parts}')} أجزاء، وعند التساوي يحوي كل دورق {m(half_p)} أجزاء.",
                f"نقص الدورق (أ) بمقدار {m(f'{p1} - {half_p} = {moved_parts}')} أجزاء، وهو ما يعادل {m(f'{pour_v}\\text{{ مل}}')}.",
                f"قيمة الجزء الواحد {m(f'{unit_v}\\text{{ مل}}')}، والحجم الكلي {m(f'{tot_parts} \\times {unit_v} = {ans}\\text{{ مل}}')}.",
            ],
            f"تحقق: البداية {m(p1*unit_v)} و{m(q1*unit_v)}، وبعد نقل {m(pour_v)} يصبح كل منهما {m(half_p*unit_v)}.",
            diagram_en=svg_two_jars(f"A ({p1})", 0.72, f"B ({q1})", 0.34, f"{pour_v} mL"),
        ))
        idx += 1

    med_jar = [
        (2, 1, 5, 7, 21),
        (3, 1, 5, 7, 32),
        (4, 1, 7, 8, 25),
        (5, 2, 11, 10, 20),
        (7, 3, 9, 11, 35),
    ]
    for p1, q1, p2, q2, pour_v in med_jar:
        s1, s2 = p1 + q1, p2 + q2
        common_s = math.lcm(s1, s2)
        a_before = p1 * (common_s // s1)
        a_after = p2 * (common_s // s2)
        diff_parts = a_before - a_after
        unit_v = pour_v // diff_parts
        ans = a_before * unit_v
        b_init = (common_s - a_before) * unit_v
        assert (ans - pour_v) * q2 == (b_init + pour_v) * p2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Medium", "kang_cad_ratio_jar_transfer",
            f"Tank A and Tank B hold olive oil in the ratio {m(f'{p1} : {q1}')}. After {m(f'{pour_v}\\text{{ L}}')} of oil is pumped from Tank A into Tank B, the new ratio is {m(f'{p2} : {q2}')}. How many liters of olive oil were in **Tank A initially**?",
            f"يحتوي الخزان (أ) والخزان (ب) على زيت زيتون بنسبة {m(f'{p1} : {q1}')}. بعد ضخّ {m(f'{pour_v}\\text{{ لتراً}}')} من الخزان (أ) إلى الخزان (ب) أصبحت النسبة الجديدة {m(f'{p2} : {q2}')}. كم لتراً من الزيت كان في **الخزان (أ) في البداية**؟",
            ans, [common_s * unit_v, a_after * unit_v, ans - unit_v * 2, ans + pour_v],
            f"Scale both ratios to the same total number of parts: \\( \\operatorname{{lcm}}({s1}, {s2}) = {common_s} \\).",
            f"وحّد مجموع أجزاء النسبتين على المضاعف المشترك الأصغر: \\( \\operatorname{{lcm}}({s1}, {s2}) = {common_s} \\).",
            "Scale the initial ratio so its part-sum matches the final ratio's part-sum.",
            [
                f"Initial sum of parts is {m(s1)} and final sum is {m(s2)}; scale to {m(common_s)} total parts.",
                f"Tank A changes from {m(a_before)} parts to {m(a_after)} parts, losing {m(diff_parts)} parts = {m(f'{pour_v}\\text{{ L}}')}.",
                f"Each part is {m(f'{unit_v}\\text{{ L}}')}, so Tank A initially held {m(f'{a_before} \\times {unit_v} = {ans}\\text{{ L}}')}.",
            ],
            f"After pumping {m(pour_v)} L: {m(ans - pour_v)} L and {m(b_init + pour_v)} L, which simplifies to {m(f'{p2} : {q2}')}.",
            "نوحّد مجموع أجزاء النسبتين لأن كمية الزيت الكلية لم تتغير.",
            [
                f"نوحد مجموع الأجزاء على {m(common_s)} جزءاً، فينتقل نصيب الخزان (أ) من {m(a_before)} إلى {m(a_after)} جزءاً.",
                f"مقدار النقص {m(diff_parts)} أجزاء يعادل {m(f'{pour_v}\\text{{ لتراً}}')}، أي أن الجزء الواحد = {m(f'{unit_v}\\text{{ لتر}}')}.",
                f"إذن كمية الخزان (أ) الابتدائية = {m(f'{a_before} \\times {unit_v} = {ans}\\text{{ لتراً}}')}.",
            ],
            f"تحقق: بعد الضخ يصبح الرصيدان {m(ans - pour_v)} و{m(b_init + pour_v)} ونسبتهما {m(f'{p2}:{q2}')}.",
            diagram_en=svg_two_jars(f"A ({p1}:{q1})", 0.75, f"B→({p2}:{q2})", 0.32, f"{pour_v} L"),
        ))
        idx += 1

    hard_evap = [
        (80, 95, 90, "fresh desert figs", "التين الطازج"),
        (60, 96, 92, "sliced watermelons", "شرائح البطيخ"),
        (90, 98, 95, "harvested sea sponges", "إسفنج البحر"),
        (125, 92, 80, "wild forest mushrooms", "فطر الغابة"),
        (140, 97, 93, "aloe vera leaves", "أوراق الصبار"),
    ]
    for w_init, p_w1, p_w2, item_en, item_ar in hard_evap:
        dry_p1, dry_p2 = 100 - p_w1, 100 - p_w2
        ans = (w_init * dry_p1) // dry_p2
        assert w_init * dry_p1 == ans * dry_p2
        naive_trap = w_init - (p_w1 - p_w2)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Hard", "kang_cad_ratio_jar_transfer",
            f"A crate of {item_en} weighs {m(f'{w_init}\\text{{ kg}}')} and consists of {m(f'{p_w1}\\%')} water by mass. After drying in the sun, the water content drops to {m(f'{p_w2}\\%')} by mass. What is the new total mass of the crate's contents in {m('\\text{kg}')}?",
            f"تزن شحنة من {item_ar} {m(f'{w_init}\\text{{ كجم}}')} وتتكوّن من {m(f'{p_w1}\\%')} ماءً بالكتلة. بعد تجفيفها في الشمس انخفضت نسبة الماء إلى {m(f'{p_w2}\\%')} بالكتلة. ما الكتلة الإجمالية الجديدة للشحنة بوحدة {m('\\text{كجم}')}؟",
            ans, [naive_trap, (w_init * p_w2) // p_w1, ans + 10, max(10, ans // 2)],
            f"Focus on the **non-water (dry) mass**: it starts as {m(f'{dry_p1}\\%')} of {m(w_init)} kg and becomes {m(f'{dry_p2}\\%')} of the new mass!",
            f"ركّز على **كتلة المادة الجافة** الثابتة: كانت {m(f'{dry_p1}\\%')} من {m(w_init)} كجم وأصبحت {m(f'{dry_p2}\\%')} من الكتلة الجديدة!",
            "Equate the unchanged dry mass before and after evaporation.",
            [
                f"Initially, dry matter accounts for {m(f'100\\% - {p_w1}\\% = {dry_p1}\\%')} of {m(f'{w_init}\\text{{ kg}}')}, which is {m(f'{fmt_val(Fraction(w_init * dry_p1, 100))}\\text{{ kg}}')}.",
                f"After drying, that exact same dry mass represents {m(f'100\\% - {p_w2}\\% = {dry_p2}\\%')} of the new total mass {m('M')}.",
                f"Solve {m(f'{dry_p2}\\% \\cdot M = {dry_p1}\\% \\cdot {w_init}')}: {m(f'M = \\frac{{{w_init} \\times {dry_p1}}}{{{dry_p2}}} = {ans}\\text{{ kg}}')}.",
            ],
            f"{m(f'{dry_p2}\\%')} of {m(ans)} kg equals {m(f'{dry_p1}\\%')} of {m(w_init)} kg.",
            "ساوي كتلة المادة الجافة قبل التجفيف وبعده لأن الماء وحده هو الذي يتبخر.",
            [
                f"نسبة المادة الجافة في البداية {m(f'{dry_p1}\\%')} من {m(w_init)} كجم.",
                f"بعد التجفيف تصبح المادة الجافة نفسها ممثِّلةً لنسبة {m(f'{dry_p2}\\%')} من الكتلة الجديدة {m('M')}.",
                f"إذن {m(f'M = \\frac{{{w_init} \\times {dry_p1}}}{{{dry_p2}}} = {ans}\\text{{ كجم}}')}.",
            ],
            f"تحقق: {m(f'{dry_p2}\\% \\times {ans} = {dry_p1}\\% \\times {w_init}')}.",
            diagram_en=svg_two_jars(f"{w_init}kg ({p_w1}%)", 0.85, f"? kg ({p_w2}%)", 0.48, "evaporate"),
        ))
        idx += 1

    # 2. kang_cad_harmonic_roundtrip (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_rt = [
        (10, 15, "kayaker", "تجدف قارب كاياك"),
        (20, 30, "scooter rider", "يقود دراجة كهربائية"),
        (15, 30, "camel courier", "يسير رسول"),
        (30, 60, "desertrover", "تنطلق مركبة"),
        (24, 40, "ferry boat", "تبحر عبّارة"),
    ]
    for v1, v2, who_en, who_ar in easy_rt:
        ans = (2 * v1 * v2) // (v1 + v2)
        assert (2 * v1 * v2) % (v1 + v2) == 0
        arith_trap = Fraction(v1 + v2, 2)
        d_pick = math.lcm(v1, v2)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Easy", "kang_cad_harmonic_roundtrip",
            f"A {who_en} travels from Camp X to Camp Y at {m(f'{v1}\\text{{ km/h}}')} and immediately returns from Camp Y to Camp X along the same route at {m(f'{v2}\\text{{ km/h}}')}. What is the average speed for the entire round trip in {m('\\text{km/h}')}?",
            f"{who_ar} من المخيم X إلى المخيم Y بسرعة {m(f'{v1}\\text{{ كم/س}}')} ثم يعود فوراً على الطريق نفسه بسرعة {m(f'{v2}\\text{{ كم/س}}')}. ما السرعة المتوسطة لرحلة الذهاب والإياب كاملةً بوحدة {m('\\text{كم/س}')}؟",
            ans, [arith_trap, ans - 2, ans + 2, v2 - v1],
            "Use \\( v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2} \\) or pick distance \\( D = \\operatorname{lcm}(v_1, v_2) \\).",
            "طبّق قانون المتوسط التوافقي \\( \\frac{2 v_1 v_2}{v_1 + v_2} \\) أو افرض مسافة تساوي المضاعف المشترك الأصغر.",
            "Average speed equals total round-trip distance \\( 2D \\) divided by total time \\( D/v_1 + D/v_2 \\).",
            [
                f"Pick one-way distance {m(f'D = \\operatorname{{lcm}}({v1}, {v2}) = {d_pick}\\text{{ km}}')}.",
                f"Outbound time is {m(f'{d_pick} \\div {v1} = {d_pick // v1}\\text{{ h}}')} and return time is {m(f'{d_pick} \\div {v2} = {d_pick // v2}\\text{{ h}}')}.",
                f"Average speed = {m(f'\\frac{{2 \\times {d_pick}}}{{{d_pick // v1} + {d_pick // v2}}} = {ans}\\text{{ km/h}}')}.",
            ],
            f"Harmonic mean: {m(f'\\frac{{2 \\times {v1} \\times {v2}}}{{{v1 + v2}}} = {ans} < {fmt_val(arith_trap)}')}.",
            "السرعة المتوسطة تساوي المسافة الكلية ذهاباً وإياباً مقسومةً على الزمن الكلي.",
            [
                f"نفرض المسافة ذهاباً {m(f'D = {d_pick}\\text{{ كم}}')}.",
                f"زمن الذهاب {m(f'{d_pick // v1}')} ساعات وزمن الإياب {m(f'{d_pick // v2}')} ساعات.",
                f"السرعة المتوسطة = {m(f'\\frac{{{2 * d_pick}}}{{{d_pick // v1 + d_pick // v2}}} = {ans}\\text{{ كم/س}}')}.",
            ],
            f"تحقق: {m(f'\\frac{{2 \\times {v1} \\times {v2}}}{{{v1 + v2}}} = {ans}')}.",
            diagram_en=svg_motion_timeline("Camp X", "Camp Y", "D", f"{v1} km/h", f"{v2} km/h", meet=True),
        ))
        idx += 1

    med_rt = [(20, 24), (30, 40), (15, 20), (40, 48), (12, 16)]
    for v1, v_avg in med_rt:
        ans = (v1 * v_avg) // (2 * v1 - v_avg)
        assert (2 * v1 * ans) == v_avg * (v1 + ans)
        lin_trap = 2 * v_avg - v1
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Medium", "kang_cad_harmonic_roundtrip",
            f"A Kangaroo shuttle drives from Town A to Town B at {m(f'{v1}\\text{{ km/h}}')}. At what constant speed (in {m('\\text{km/h}')}) must it drive back from Town B to Town A so that its average speed for the entire round trip is {m(f'{v_avg}\\text{{ km/h}}')}?",
            f"تنطلق حافلة من المدينة (أ) إلى المدينة (ب) بسرعة {m(f'{v1}\\text{{ كم/س}}')}. بأي سرعة ثابتة (بوحدة {m('\\text{كم/س}')}) يجب أن تعود من (ب) إلى (أ) لتصبح سرعتها المتوسطة لرحلة الذهاب والإياب كاملةً {m(f'{v_avg}\\text{{ كم/س}}')}؟",
            ans, [lin_trap, ans - 4, ans + 6, v1 + v_avg],
            f"Set \\( \\frac{{2 \\cdot {v1} \\cdot v_2}}{{{v1} + v_2}} = {v_avg} \\) and solve for \\( v_2 \\)—don't assume \\( v_2 = {lin_trap} \\)!",
            f"ضع المعادلة \\( \\frac{{2 \\cdot {v1} \\cdot v_2}}{{{v1} + v_2}} = {v_avg} \\) وحلّها لإيجاد \\( v_2 \\)!",
            "Solve the harmonic mean equation \\( 2 v_1 v_2 = v_{\\text{avg}}(v_1 + v_2) \\) for \\( v_2 \\).",
            [
                f"Write the round-trip average speed condition: {m(f'\\frac{{2 \\times {v1} \\times v_2}}{{{v1} + v_2}} = {v_avg}')}.",
                f"Multiply by {m(f'({v1} + v_2)')}: {m(f'{2 * v1} v_2 = {v_avg * v1} + {v_avg} v_2')}.",
                f"Collect {m('v_2')}: {m(f'{2 * v1 - v_avg} v_2 = {v_avg * v1} \\implies v_2 = {ans}\\text{{ km/h}}')}.",
            ],
            f"Check: {m(f'\\frac{{2 \\times {v1} \\times {ans}}}{{{v1} + {ans}}} = \\frac{{{2*v1*ans}}}{{{v1+ans}}} = {v_avg}\\text{{ km/h}}')}.",
            "نحلّ معادلة المتوسط التوافقي \\( 2 v_1 v_2 = v_{\\text{avg}}(v_1 + v_2) \\) لإيجاد سرعة العودة.",
            [
                f"نكتب معادلة السرعة المتوسطة: {m(f'\\frac{{2 \\times {v1} \\times v_2}}{{{v1} + v_2}} = {v_avg}')}.",
                f"بالضرب التبادلي: {m(f'{2 * v1} v_2 = {v_avg * v1} + {v_avg} v_2')}.",
                f"بطرح {m(f'{v_avg} v_2')} نحصل على {m(f'{2 * v1 - v_avg} v_2 = {v_avg * v1} \\implies v_2 = {ans}\\text{{ كم/س}}')}.",
            ],
            f"تحقق: {m(f'\\frac{{2 \\times {v1} \\times {ans}}}{{{v1 + ans}}} = {v_avg}')}.",
            diagram_en=svg_motion_timeline("A", "B", "avg=" + str(v_avg), f"{v1} km/h", "v₂=?", meet=True),
        ))
        idx += 1

    hard_3seg = [
        (10, 15, 30, "mountain triathlon course"),
        (12, 20, 60, "desert endurance rally"),
        (12, 15, 20, "coastal cycling loop"),
        (24, 30, 40, "solar car test track"),
        (8, 12, 24, "cross-country ski trail"),
    ]
    for v1, v2, v3, track_en in hard_3seg:
        d_seg = math.lcm(v1, v2, v3)
        tot_t = d_seg // v1 + d_seg // v2 + d_seg // v3
        ans = (3 * d_seg) // tot_t
        assert (3 * d_seg) % tot_t == 0
        arith_3 = Fraction(v1 + v2 + v3, 3)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Hard", "kang_cad_harmonic_roundtrip",
            f"A {track_en} is divided into **three equal-length** sections. An athlete covers the first third at {m(f'{v1}\\text{{ km/h}}')}, the middle third at {m(f'{v2}\\text{{ km/h}}')}, and the final third at {m(f'{v3}\\text{{ km/h}}')}. What is the athlete's average speed over the whole course in {m('\\text{km/h}')}?",
            f"ينقسم مضمار سباق إلى **ثلاثة أجزاء متساوية الطول**. يقطع متسابق الثلث الأول بسرعة {m(f'{v1}\\text{{ كم/س}}')}، والثلث الأوسط بسرعة {m(f'{v2}\\text{{ كم/س}}')}، والثلث الأخير بسرعة {m(f'{v3}\\text{{ كم/س}}')}. ما سرعته المتوسطة على كامل المضمار بوحدة {m('\\text{كم/س}')}؟",
            ans, [arith_3, ans + 3, ans - 2, (v1 + v2) // 2],
            f"Let each third have length \\( d = \\operatorname{{lcm}}({v1}, {v2}, {v3}) = {d_seg}\\text{{ km}} \\), then divide \\( 3d \\) by total time!",
            f"افرض طول كل ثلث \\( d = \\operatorname{{lcm}}({v1}, {v2}, {v3}) = {d_seg}\\text{{ كم}} \\) ثم اقسم المسافة الكلية \\( 3d \\) على الزمن الكلي!",
            "Use the 3-part harmonic mean: \\( v_{\\text{avg}} = \\frac{3d}{d/v_1 + d/v_2 + d/v_3} \\).",
            [
                f"Set each section's length to {m(f'd = {d_seg}\\text{{ km}}')}, so total course length is {m(f'3d = {3 * d_seg}\\text{{ km}}')}.",
                f"Section times are {m(f'{d_seg // v1}\\text{{ h}}')}, {m(f'{d_seg // v2}\\text{{ h}}')}, and {m(f'{d_seg // v3}\\text{{ h}}')}, totaling {m(f'{tot_t}\\text{{ h}}')}.",
                f"Average speed = {m(f'{3 * d_seg} \\div {tot_t} = {ans}\\text{{ km/h}}')}.",
            ],
            f"{m(f'\\frac{{3}}{{1/{v1} + 1/{v2} + 1/{v3}}} = {ans}\\text{{ km/h}}')}.",
            "نحسب الزمن في كل ثلث على حدة ثم نقسم المسافة الكلية \\( 3d \\) على مجموع الأزمنة.",
            [
                f"نفرض طول كل ثلث {m(f'd = {d_seg}\\text{{ كم}}')} فتكون المسافة الكلية {m(f'{3 * d_seg}\\text{{ كم}}')}.",
                f"مجموع الأزمنة يساوي {m(f'{d_seg // v1} + {d_seg // v2} + {d_seg // v3} = {tot_t}')} ساعات.",
                f"السرعة المتوسطة = {m(f'{3 * d_seg} \\div {tot_t} = {ans}\\text{{ كم/س}}')}.",
            ],
            f"تحقق: {m(f'3 \\div (\\frac{{1}}{{{v1}}} + \\frac{{1}}{{{v2}}} + \\frac{{1}}{{{v3}}}) = {ans}')}.",
            diagram_en=svg_number_strip([f"d@{v1}", f"d@{v2}", f"d@{v3}", "avg=?"]),
        ))
        idx += 1

    # 3. kang_cad_linear_system_weights (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_wt = [(4, 3, 12, 7), (5, 2, 15, 9), (3, 5, 14, 11), (4, 1, 18, 8), (5, 3, 13, 6)]
    for a_c, b_c, x_w, y_w in easy_wt:
        w1 = a_c * x_w + b_c * y_w
        w2 = b_c * x_w + a_c * y_w
        ans = x_w + y_w
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Easy", "kang_cad_linear_system_weights",
            f"On a balance, {m(a_c)} red marbles and {m(b_c)} green cubes weigh {m(f'{w1}\\text{{ g}}')}, while {m(b_c)} red marbles and {m(a_c)} green cubes weigh {m(f'{w2}\\text{{ g}}')}. What is the combined mass of **1 red marble and 1 green cube** in grams?",
            f"على ميزان دقيق، تزن {m(a_c)} كرات حمراء و{m(b_c)} مكعبات خضراء {m(f'{w1}\\text{{ جم}}')}، بينما تزن {m(b_c)} كرات حمراء و{m(a_c)} مكعبات خضراء {m(f'{w2}\\text{{ جم}}')}. ما الكتلة المشتركة **لكرة حمراء واحدة ومكعب أخضر واحد** بالجرام؟",
            ans, [abs(w1 - w2), ans + 4, x_w * 2, y_w * 2],
            f"Add both weighings together: you get {m(a_c + b_c)} red marbles + {m(a_c + b_c)} green cubes right away!",
            f"اجمع الوزنين معاً مباشرة لتحصل على {m(a_c + b_c)} كرات حمراء و{m(a_c + b_c)} مكعبات خضراء!",
            "Sum the two symmetric equations and divide by \\( a + b \\).",
            [
                f"Add {m(f'{a_c}R + {b_c}G = {w1}')} and {m(f'{b_c}R + {a_c}G = {w2}')} to obtain {m(f'{a_c + b_c}(R + G) = {w1 + w2}')}.",
                f"Divide both sides by {m(a_c + b_c)}: {m(f'R + G = {w1 + w2} \\div {a_c + b_c} = {ans}\\text{{ g}}')}.",
            ],
            f"With {m(f'R={x_w}, G={y_w}')}, {m(f'R+G={ans}')} and both weighings match ({m(w1)} and {m(w2)}).",
            "بجمع المعادلتين المتماثلتين والقسمة على مجموع المعاملين نحصل على المجموع المطلوب فوراً.",
            [
                f"بجمع المعادلتين نجد {m(f'{a_c + b_c}(R + G) = {w1 + w2}')}.",
                f"بالقسمة على {m(a_c + b_c)} ينتج {m(f'R + G = {ans}\\text{{ جم}}')}.",
            ],
            f"تحقق: {m(f'{a_c + b_c} \\times {ans} = {w1 + w2}')}.",
            diagram_en=svg_balance_scales(a_c, b_c, b_c, a_c),
        ))
        idx += 1

    med_age = [
        (7, 5, 7, "coach", "المدرب"),
        (6, 6, 4, "uncle", "العم"),
        (8, 4, 4, "mother", "الأم"),
        (10, 4, 5, "father", "الأب"),
        (5, 7, 5, "aunt", "العمة"),
    ]
    for c_now, k1, t_yr, rel_en, rel_ar in med_age:
        p_now = k1 * c_now
        assert (p_now + t_yr) % (c_now + t_yr) == 0
        k2 = (p_now + t_yr) // (c_now + t_yr)
        ans = p_now
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Medium", "kang_cad_linear_system_weights",
            f"Today, a Cadet's {rel_en} is {m(k1)} times as old as the Cadet. In {m(t_yr)} years, the {rel_en} will be {m(k2)} times as old as the Cadet. How old is the **{rel_en} today** (in years)?",
            f"اليوم عُمر {rel_ar} يساوي {m(k1)} أضعاف عمر الطالب. وبعد {m(t_yr)} سنوات سيصبح عمر {rel_ar} مساوياً لـ {m(k2)} أضعاف عمر الطالب. كم عمر **{rel_ar} اليوم** بالسنوات؟",
            ans, [ans + t_yr, c_now, ans - k1, (k1 + 1) * c_now],
            f"Let the Cadet's age today be \\( x \\), so the {rel_en} is \\( {k1}x \\); in {t_yr} years, \\( {k1}x + {t_yr} = {k2}(x + {t_yr}) \\).",
            f"افرض عمر الطالب اليوم \\( x \\) وعمر {rel_ar} \\( {k1}x \\)؛ بعد {t_yr} سنوات يكون \\( {k1}x + {t_yr} = {k2}(x + {t_yr}) \\).",
            "Add \\( t \\) years to **both** ages before applying the future ratio.",
            [
                f"Let the Cadet be {m('x')} years old today and the {rel_en} be {m(f'{k1}x')} years old.",
                f"In {m(t_yr)} years: {m(f'{k1}x + {t_yr} = {k2}(x + {t_yr}) = {k2}x + {k2 * t_yr}')}.",
                f"Thus {m(f'{k1 - k2}x = {(k2 - 1) * t_yr} \\implies x = {c_now}')}, so the {rel_en} is {m(f'{k1} \\times {c_now} = {ans}')} today.",
            ],
            f"Today: {m(ans)} and {m(c_now)} ({m(f'{k1}\\times')}); in {m(t_yr)} yrs: {m(ans + t_yr)} and {m(c_now + t_yr)} ({m(f'{k2}\\times')}).",
            "نضيف عدد السنوات \\( t \\) إلى العمرين معاً ثم نطبق النسبة المستقبلية.",
            [
                f"نفرض عمر الطالب اليوم {m('x')} فيكون عمر {rel_ar} {m(f'{k1}x')}.",
                f"بعد {m(t_yr)} سنوات: {m(f'{k1}x + {t_yr} = {k2}(x + {t_yr})')} ومنه {m(f'{k1 - k2}x = {(k2 - 1) * t_yr} \\implies x = {c_now}')}.",
                f"إذن عمر {rel_ar} اليوم هو {m(f'{k1} \\times {c_now} = {ans}')} سنة.",
            ],
            f"تحقق: اليوم {m(ans)} و{m(c_now)}، وبعد {m(t_yr)} سنوات {m(ans+t_yr)} و{m(c_now+t_yr)}.",
            diagram_en=svg_function_machine(f"x & {k1}x", f"+{t_yr} yrs", f"×{k2}", f"{k1}x={ans}"),
        ))
        idx += 1

    hard_3wt = [(28, 13, 19), (34, 15, 23), (41, 18, 27), (37, 14, 25), (46, 19, 31)]
    for x_k, y_c, z_w in hard_3wt:
        ab, bc, ca = x_k + y_c, y_c + z_w, z_w + x_k
        tot_xyz = (ab + bc + ca) // 2
        ans = tot_xyz - bc
        assert ans == x_k
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Hard", "kang_cad_linear_system_weights",
            f"At a wildlife sanctuary, a Kangaroo and a Koala together weigh {m(f'{ab}\\text{{ kg}}')}, the Koala and a Wombat together weigh {m(f'{bc}\\text{{ kg}}')}, and the Wombat and the Kangaroo together weigh {m(f'{ca}\\text{{ kg}}')}. How many kilograms does the **Kangaroo** weigh alone?",
            f"في محمية طبيعية، يزن الكانجارو والكوالا معاً {m(f'{ab}\\text{{ كجم}}')}، ويزن الكوالا والومبت معاً {m(f'{bc}\\text{{ كجم}}')}، ويزن الومبت والكانجارو معاً {m(f'{ca}\\text{{ كجم}}')}. كم كيلوجراماً يزن **الكانجارو** بمفرده؟",
            ans, [tot_xyz, z_w, y_c, ab - bc + z_w // 2],
            "Add all three pairwise weights: every animal is counted **twice**, giving \\( 2(K + C + W) \\)!",
            "اجمع الأوزان الثلاثة الثنائية معاً؛ كل حيوان يُحسب **مرتين** فنحصل على \\( 2(K + C + W) \\)!",
            "Divide the sum of all three equations by 2 to get \\( K + C + W \\), then subtract \\( C + W \\).",
            [
                f"Adding all three weighings gives {m(f'2(K + C + W) = {ab} + {bc} + {ca} = {2 * tot_xyz}')}.",
                f"Divide by 2: all three animals together weigh {m(f'K + C + W = {tot_xyz}\\text{{ kg}}')}.",
                f"Subtract the Koala + Wombat pair ({m(f'{bc}\\text{{ kg}}')}): {m(f'K = {tot_xyz} - {bc} = {ans}\\text{{ kg}}')}.",
            ],
            f"{m(f'K={x_k}, C={y_c}, W={z_w}')} gives {m(f'{ab}, {bc}, {ca}')}.",
            "اقسم مجموع المعادلات الثلاث على 2 لإيجاد مجموع الثلاثة معاً ثم اطرح وزن (الكوالا + الومبت).",
            [
                f"بجمع المعادلات الثلاث نحصل على {m(f'2(K + C + W) = {2 * tot_xyz}')} ومنها {m(f'K + C + W = {tot_xyz}\\text{{ كجم}}')}.",
                f"بطرح وزن الكوالا والومبت ({m(bc)} كجم) نجد وزن الكانجارو {m(f'K = {tot_xyz} - {bc} = {ans}\\text{{ كجم}}')}.",
            ],
            f"تحقق: {m(f'{x_k} + {y_c} = {ab}')} و{m(f'{x_k} + {z_w} = {ca}')}.",
            diagram_en=svg_number_triangle_puzzle("?", str(y_c) if False else "C", "W", str(ab), str(ca), str(bc)),
        ))
        idx += 1

    # 4. kang_cad_telescoping_fractions (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_tele = [(2, 17), (4, 27), (5, 39), (3, 35), (6, 65)]
    for a_k, b_k in easy_tele:
        ans = (b_k + 1) // a_k
        assert (b_k + 1) % a_k == 0
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Easy", "kang_cad_telescoping_fractions",
            f"Evaluate the product {m(f'\\left(1 + \\frac{{1}}{{{a_k}}}\\right)\\left(1 + \\frac{{1}}{{{a_k+1}}}\\right)\\left(1 + \\frac{{1}}{{{a_k+2}}}\\right)\\cdots\\left(1 + \\frac{{1}}{{{b_k}}}\\right)')}.",
            f"احسب قيمة الجداء {m(f'\\left(1 + \\frac{{1}}{{{a_k}}}\\right)\\left(1 + \\frac{{1}}{{{a_k+1}}}\\right)\\left(1 + \\frac{{1}}{{{a_k+2}}}\\right)\\cdots\\left(1 + \\frac{{1}}{{{b_k}}}\\right)')}.",
            ans, [Fraction(b_k, a_k), ans - 1, ans + 1, Fraction(b_k + 1, a_k + 1)],
            f"Rewrite each factor as \\( \\frac{{k+1}}{{k}} \\) starting with \\( \\frac{{{a_k+1}}}{{{a_k}}} \\) and ending with \\( \\frac{{{b_k+1}}}{{{b_k}}} \\).",
            f"اكتب كل قوس على صورة كسر واحد \\( \\frac{{k+1}}{{k}} \\) بدءاً من \\( \\frac{{{a_k+1}}}{{{a_k}}} \\) وحتى \\( \\frac{{{b_k+1}}}{{{b_k}}} \\).",
            "Adjacent numerators and denominators telescope, leaving \\( \\frac{b+1}{a} \\).",
            [
                f"Convert each term: {m(f'\\frac{{{a_k+1}}}{{{a_k}}} \\times \\frac{{{a_k+2}}}{{{a_k+1}}} \\times \\cdots \\times \\frac{{{b_k+1}}}{{{b_k}}}')}.",
                f"All intermediate integers from {m(a_k + 1)} through {m(b_k)} cancel in pairs.",
                f"Only {m(f'\\frac{{{b_k + 1}}}{{{a_k}}} = {ans}')} remains.",
            ],
            f"{m(f'({b_k}+1)/{a_k} = {ans}')}.",
            "تختصر البسوط والمقامات المتجاورة تباعاً ولا يبقى سوى آخر بسط على أول مقام.",
            [
                f"نكتب الجداء بصورة كسور: {m(f'\\frac{{{a_k+1}}}{{{a_k}}} \\times \\frac{{{a_k+2}}}{{{a_k+1}}} \\times \\cdots \\times \\frac{{{b_k+1}}}{{{b_k}}}')}.",
                f"تُختصر الأعداد من {m(a_k + 1)} حتى {m(b_k)} فيتبقى {m(f'\\frac{{{b_k + 1}}}{{{a_k}}} = {ans}')}.",
            ],
            f"تحقق: {m(f'{b_k + 1} \\div {a_k} = {ans}')}.",
            diagram_en=svg_number_strip([f"{a_k+1}/{a_k}", f"×{a_k+2}/{a_k+1}", "× … ×", f"{b_k+1}/{b_k}"]),
        ))
        idx += 1

    med_tele = [(1, 9), (2, 11), (3, 14), (4, 19), (2, 19)]
    for a_k, b_k in med_tele:
        ans = Fraction(1, a_k) - Fraction(1, b_k + 1)
        assert ans == sum(Fraction(1, k * (k + 1)) for k in range(a_k, b_k + 1))
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Medium", "kang_cad_telescoping_fractions",
            f"What is the exact value of the sum {m(f'\\frac{{1}}{{{a_k}\\times {a_k+1}}} + \\frac{{1}}{{{a_k+1}\\times {a_k+2}}} + \\cdots + \\frac{{1}}{{{b_k}\\times {b_k+1}}}')}?",
            f"ما القيمة الدقيقة للمجموع {m(f'\\frac{{1}}{{{a_k}\\times {a_k+1}}} + \\frac{{1}}{{{a_k+1}\\times {a_k+2}}} + \\cdots + \\frac{{1}}{{{b_k}\\times {b_k+1}}}')}؟",
            ans, [Fraction(1, a_k) - Fraction(1, b_k), Fraction(b_k, b_k + 1) if a_k > 1 else Fraction(b_k - 1, b_k + 1), ans + Fraction(1, b_k + 1), Fraction(1, a_k + 1)],
            "Split every fraction using \\( \\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1} \\).",
            "فكّك كل كسر باستخدام المتطابقة \\( \\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1} \\).",
            "Telescope the partial fractions so only \\( \\frac{1}{a} - \\frac{1}{b+1} \\) survives.",
            [
                f"Rewrite each term as {m('\\frac{1}{k} - \\frac{1}{k+1}')}: {m(f'\\left(\\frac{{1}}{{{a_k}}} - \\frac{{1}}{{{a_k+1}}}\\right) + \\left(\\frac{{1}}{{{a_k+1}}} - \\frac{{1}}{{{a_k+2}}}\\right) + \\cdots + \\left(\\frac{{1}}{{{b_k}}} - \\frac{{1}}{{{b_k+1}}}\\right)')}.",
                f"Every interior term cancels, leaving {m(f'\\frac{{1}}{{{a_k}}} - \\frac{{1}}{{{b_k+1}}} = {fmt_val(ans)}')}.",
            ],
            f"Exact fraction check matches term-by-term addition: {m(fmt_val(ans))}.",
            "بتفكيك كل كسر تتلاشى جميع الحدود الوسطى ويبقى الحد الأول مطروحاً منه الحد الأخير.",
            [
                f"نكتب المجموع على الصورة {m(f'\\left(\\frac{{1}}{{{a_k}}} - \\frac{{1}}{{{a_k+1}}}\\right) + \\cdots + \\left(\\frac{{1}}{{{b_k}}} - \\frac{{1}}{{{b_k+1}}}\\right)')}.",
                f"تختفي الحدود الداخلية ويبقى {m(f'\\frac{{1}}{{{a_k}}} - \\frac{{1}}{{{b_k+1}}} = {fmt_val(ans)}')}.",
            ],
            f"تحقق: القيمة المبسطة هي {m(fmt_val(ans))}.",
            diagram_en=svg_number_strip([f"1/{a_k}", f"−1/{a_k+1}+1/{a_k+1}", "− … −", f"1/{b_k+1}"]),
        ))
        idx += 1

    hard_tele = [10, 12, 15, 20, 25]
    for n_max in hard_tele:
        ans = Fraction(n_max + 1, 2 * n_max)
        prod_check = Fraction(1, 1)
        for k in range(2, n_max + 1):
            prod_check *= Fraction(k * k - 1, k * k)
        assert prod_check == ans
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Algebra", "Hard", "kang_cad_telescoping_fractions",
            f"Compute the exact value of {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{n_max}^2}}\\right)')}.",
            f"احسب القيمة الدقيقة للجداء {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{n_max}^2}}\\right)')}.",
            ans, [Fraction(1, n_max), Fraction(n_max - 1, 2 * n_max), Fraction(n_max + 1, n_max), Fraction(1, 2)],
            "Factor \\( 1 - \\frac{1}{k^2} = \\left(1 - \\frac{1}{k}\\right)\\left(1 + \\frac{1}{k}\\right) = \\frac{k-1}{k} \\cdot \\frac{k+1}{k} \\)!",
            "حلّل فرق المربعين \\( 1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k} \\) إلى جداءين متداخلين!",
            "Separate into \\( \\prod \\frac{k-1}{k} \\) and \\( \\prod \\frac{k+1}{k} \\), each telescoping cleanly.",
            [
                f"Use difference of squares: {m('1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}.",
                f"The first chain {m(f'\\frac{{1}}{{2}}\\cdot\\frac{{2}}{{3}}\\cdots\\frac{{{n_max-1}}}{{{n_max}}}')} collapses to {m(f'\\frac{{1}}{{{n_max}}}')}.",
                f"The second chain {m(f'\\frac{{3}}{{2}}\\cdot\\frac{{4}}{{3}}\\cdots\\frac{{{n_max+1}}}{{{n_max}}}')} collapses to {m(f'\\frac{{{n_max+1}}}{{2}}')}.",
                f"Multiplying the two results gives {m(f'\\frac{{1}}{{{n_max}}} \\times \\frac{{{n_max+1}}}{{2}} = {fmt_val(ans)}')}.",
            ],
            f"Formula {m('\\frac{n+1}{2n}')} at {m(f'n={n_max}')} gives {m(fmt_val(ans))}.",
            "نفصل الجداء إلى سلسلتين متداخلتين بعد تحليل فرق المربعين.",
            [
                f"نكتب كل حد بالصورة {m('\\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}.",
                f"جداء الكسور الأولى يعطي {m(f'\\frac{{1}}{{{n_max}}}')}، وجداء الكسور الثانية يعطي {m(f'\\frac{{{n_max+1}}}{{2}}')}.",
                f"بحاصل ضربهما نجد القيمة الدقيقة {m(fmt_val(ans))}.",
            ],
            f"تحقق: {m(f'\\frac{{{n_max}+1}}{{2\\times {n_max}}} = {fmt_val(ans)}')}.",
            diagram_en=svg_area_identity_square("1", f"1/{n_max}"),
        ))
        idx += 1

    assert len(qs) == 60
    return qs


def _svg_zigzag_3bends(a_lbl: str, r1_lbl: str, l1_lbl: str, r2_lbl: str, b_lbl: str) -> str:
    parts = [
        f'<line x1="30" y1="26" x2="290" y2="26" stroke="{STROKE}" stroke-width="2"/>',
        f'<line x1="30" y1="162" x2="290" y2="162" stroke="{STROKE}" stroke-width="2"/>',
        f'<polyline points="78,26 196,60 96,98 206,130 104,162" fill="none" stroke="{BLUE}" stroke-width="2.2" stroke-linejoin="round"/>',
        _nlabel(118, 39, a_lbl, size=11, color=DARK),
        _nlabel(162, 64, r1_lbl, size=11, color=ORANGE),
        _nlabel(132, 102, l1_lbl, size=11, color=RED),
        _nlabel(170, 133, r2_lbl, size=11, color=ORANGE),
        _nlabel(142, 157, b_lbl, size=11, color=DARK),
    ]
    return wrap_svg("".join(parts), w=320, h=184, disp_w=380, title="Three-bend parallel zigzag")


def _unit_3() -> list[dict]:
    """Unit 3 (Lesson 3.3 — Flat Geometry): QIDs 121..180."""
    qs: list[dict] = []
    idx = 121

    # 1. kang_cad_parallel_zigzag_angle (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_zz = [(35, 48), (44, 59), (37, 62), (51, 38), (46, 67)]
    for ang_a, ang_b in easy_zz:
        ans = ang_a + ang_b
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_parallel_zigzag_angle",
            f"Two straight rails {m('L_1')} and {m('L_2')} are parallel. A bent laser beam leaves {m('L_1')} at an acute angle of {m(f'{ang_a}^\\circ')} and hits {m('L_2')} at an acute angle of {m(f'{ang_b}^\\circ')}. What is the measure of the interior bend angle {m('x^\\circ')}?",
            f"سكتان مستقيمتان {m('L_1')} و{m('L_2')} متوازيتان. ينطلق شعاع ليزر منكسر من {m('L_1')} بزاوية حادة {m(f'{ang_a}^\\circ')} ويسقط على {m('L_2')} بزاوية حادة {m(f'{ang_b}^\\circ')}. ما قياس زاوية الانكسار الوسطى {m('x^\\circ')}؟",
            ans, [180 - ans, abs(ang_a - ang_b) + 60, ans + 10, ans - 10],
            "Draw a helper line through the bend vertex parallel to both rails.",
            "ارسم مستقيماً مساعداً يمر برأس الانكسار ويوازي السكتين.",
            "Split the bend angle with an auxiliary parallel line and add the two alternate interior angles.",
            [
                f"Draw an auxiliary line through the vertex of angle {m('x')} parallel to {m('L_1')} and {m('L_2')}.",
                f"Alternate interior angles split {m('x')} into {m(f'{ang_a}^\\circ')} above the helper line and {m(f'{ang_b}^\\circ')} below it.",
                f"Add them together: {m(f'x = {ang_a}^\\circ + {ang_b}^\\circ = {ans}^\\circ')}.",
            ],
            f"{m(f'{ang_a} + {ang_b} = {ans}')}.",
            "يقسّم المستقيم الموازي المساعد الزاوية الوسطى إلى زاويتين متبادلتين داخلياً مع الزاويتين المعطاتين.",
            [
                f"نرسم مستقيماً موازياً لـ {m('L_1')} و{m('L_2')} يمر برأس الزاوية {m('x')}.",
                f"بالتبادل الداخلي ينقسم قياس {m('x')} إلى {m(f'{ang_a}^\\circ')} و{m(f'{ang_b}^\\circ')}.",
                f"إذن {m(f'x = {ang_a} + {ang_b} = {ans}^\\circ')}.",
            ],
            f"تحقق: {m(f'{ang_a} + {ang_b} = {ans}')}.",
            diagram_en=svg_parallel_zigzag(f"{ang_a}°", "x°", f"{ang_b}°"),
        ))
        idx += 1

    med_zz = [(132, 105), (141, 94), (126, 112), (137, 96), (119, 110)]
    for obt_top, mid_m in med_zz:
        ac_top = 180 - obt_top
        ans = mid_m - ac_top
        assert 15 < ans < 85
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_parallel_zigzag_angle",
            f"Between parallel lines {m('L_1 \\parallel L_2')}, a two-segment path makes an **obtuse** angle of {m(f'{obt_top}^\\circ')} with {m('L_1')} on the left side, bends through an interior angle of {m(f'{mid_m}^\\circ')}, and meets {m('L_2')} at acute angle {m('y^\\circ')}. What is {m('y')}?",
            f"بين مستقيمين متوازيين {m('L_1 \\parallel L_2')}، يصنع مسار من قطعتين زاوية **منفرجة** قياسها {m(f'{obt_top}^\\circ')} مع {m('L_1')}، ثم ينعطف بزاوية وسطى {m(f'{mid_m}^\\circ')}، ويلتقي بـ {m('L_2')} بزاوية حادة {m('y^\\circ')}. ما قيمة {m('y')}؟",
            ans, [obt_top - mid_m, 180 - mid_m, ans + 10, ac_top],
            f"First find the supplementary acute angle on {m('L_1')}: \\( 180^\\circ - {obt_top}^\\circ = {ac_top}^\\circ \\)!",
            f"أوجد أولاً الزاوية الحادة المكملة على المستقيم الأول: \\( 180^\\circ - {obt_top}^\\circ = {ac_top}^\\circ \\)!",
            "Convert the obtuse angle to its acute supplement \\( 180^\\circ - \\theta \\), then subtract from the middle bend.",
            [
                f"On straight line {m('L_1')}, the acute angle opening toward the bend is {m(f'180^\\circ - {obt_top}^\\circ = {ac_top}^\\circ')}.",
                f"By the parallel-zigzag rule, {m(f'{ac_top}^\\circ + y^\\circ = {mid_m}^\\circ')}.",
                f"Subtract {m(ac_top)}: {m(f'y = {mid_m} - {ac_top} = {ans}')}.",
            ],
            f"{m(f'{ac_top} + {ans} = {mid_m}')} and {m(f'{ac_top} + {obt_top} = 180')}.",
            "نحوّل الزاوية المنفرجة إلى مكملتها الحادة ثم نطرحها من الزاوية الوسطى.",
            [
                f"الزاوية الحادة المكملة على {m('L_1')} تساوي {m(f'180 - {obt_top} = {ac_top}^\\circ')}.",
                f"من قاعدة التوازي: {m(f'{ac_top} + y = {mid_m}')}، ومنه {m(f'y = {ans}')}.",
            ],
            f"تحقق: {m(f'{ac_top} + {ans} = {mid_m}')}.",
            diagram_en=svg_parallel_zigzag(f"180°−{obt_top}°", f"{mid_m}°", "y°"),
        ))
        idx += 1

    hard_zz = [
        (25, 58, 67, 32),
        (31, 64, 73, 28),
        (22, 55, 79, 41),
        (29, 68, 74, 35),
        (34, 71, 65, 27),
    ]
    for ang_a, r1, r2, ang_b in hard_zz:
        ans = r1 + r2 - ang_a - ang_b
        assert 25 < ans < 120
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_parallel_zigzag_angle",
            f"In the 3-bend zigzag between parallel lines, the acute start and end angles are {m(f'{ang_a}^\\circ')} and {m(f'{ang_b}^\\circ')}, and the two right-pointing bends measure {m(f'{r1}^\\circ')} and {m(f'{r2}^\\circ')}. What is the measure of the middle left-pointing angle {m('x^\\circ')}?",
            f"في المسار المتعرج ذي الانكسارات الثلاثة بين مستقيمين متوازيين، قياسا الزاويتين الحادتين عند الطرفين {m(f'{ang_a}^\\circ')} و{m(f'{ang_b}^\\circ')}، وقياسا الرأسين المتجهين يميناً {m(f'{r1}^\\circ')} و{m(f'{r2}^\\circ')}. ما قياس الزاوية الوسطى المتجهة يساراً {m('x^\\circ')}؟",
            ans, [r1 + r2 - ang_a, ang_a + ang_b, (r1 + r2) // 2, ans + 12],
            "Balance alternating turns: (angles opening right) = (angles opening left)!",
            "وازن الزوايا المتناوبة: مجموع الزوايا المتجهة لجهة واحدة يساوي مجموع الزوايا المتجهة للجهة المقابلة!",
            "Apply \\( \\alpha + x + \\beta = r_1 + r_2 \\) across the three auxiliary parallel lines.",
            [
                "Drawing auxiliary parallel lines at all three bends splits every bend into alternate interior pairs.",
                f"Summing left-opening vs. right-opening angles gives {m(f'{ang_a} + x + {ang_b} = {r1} + {r2}')}.",
                f"Solve for {m('x')}: {m(f'x = {r1 + r2} - {ang_a + ang_b} = {ans}')}.",
            ],
            f"Left sum {m(f'{ang_a} + {ans} + {ang_b} = {r1 + r2}')} matches right sum {m(f'{r1} + {r2} = {r1 + r2}')}.",
            "برسم مستقيمات موازية عند الرؤوس الثلاثة نجد أن مجموع الزوايا المتناوبة متساوٍ في الاتجاهين.",
            [
                f"من توازن الزوايا المتناوبة بين المتوازيين: {m(f'{ang_a} + x + {ang_b} = {r1} + {r2}')}.",
                f"إذن {m(f'x = {r1 + r2} - {ang_a + ang_b} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ang_a} + {ans} + {ang_b} = {r1 + r2}')}.",
            diagram_en=_svg_zigzag_3bends(f"{ang_a}°", f"{r1}°", "x°", f"{r2}°", f"{ang_b}°"),
        ))
        idx += 1

    # 2. kang_cad_four_rect_areas (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_4r = [(3, 5, 4, 7), (4, 6, 5, 8), (3, 7, 6, 5), (5, 8, 3, 6), (6, 9, 4, 10)]
    for w1, w2, h1, h2 in easy_4r:
        tl, tr, bl, ans = w1 * h1, w2 * h1, w1 * h2, w2 * h2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_four_rect_areas",
            f"A rectangle is partitioned by one horizontal segment and one vertical segment into four smaller rectangles. Three of the areas are {m(tl)}, {m(tr)}, and {m(bl)} as shown. What is the area of the fourth rectangle {m('?')}?",
            f"قُسّم مستطيل بقطعة أفقية وقطعة رأسية إلى أربعة مستطيلات أصغر. ثلاث من المساحات هي {m(tl)} و{m(tr)} و{m(bl)} كما في الشكل. ما مساحة المستطيل الرابع {m('?')}؟",
            ans, [tr + bl - tl, ans - w2, ans + h2, tl + tr],
            "Opposite sub-rectangle areas have equal products: \\( A_{\\text{TL}} \\times A_{\\text{BR}} = A_{\\text{TR}} \\times A_{\\text{BL}} \\).",
            "حاصل ضرب مساحتَي كل مستطيلين متقابلين قطرياً متساوٍ: \\( A_{\\text{TL}} \\times A_{\\text{BR}} = A_{\\text{TR}} \\times A_{\\text{BL}} \\).",
            "Multiply the two known off-diagonal areas and divide by the opposite corner's area.",
            [
                f"Use {m(f'{tl} \\times A = {tr} \\times {bl} = {tr * bl}')}.",
                f"Divide by {m(tl)}: {m(f'A = {tr * bl} \\div {tl} = {ans}')}.",
            ],
            f"{m(f'{tl}/{tr} = {bl}/{ans} = {fmt_val(Fraction(w1, w2))}')}.",
            "نضرب مساحتَي المستطيلين المتقابلين ونقسم على المساحة الثالثة.",
            [
                f"من تناسب الأضلاع: {m(f'{tl} \\times A = {tr} \\times {bl} = {tr * bl}')}.",
                f"بالقسمة على {m(tl)} نجد {m(f'A = {ans}')}.",
            ],
            f"تحقق: {m(f'{tl} \\times {ans} = {tr} \\times {bl} = {tr * bl}')}.",
            diagram_en=svg_subdivided_rect_2x2(str(tl), str(tr), str(bl), "?"),
        ))
        idx += 1

    med_4p = [(4, 7, 3, 6), (5, 9, 4, 8), (6, 10, 5, 7), (3, 8, 5, 9), (7, 11, 4, 9)]
    for w1, w2, h1, h2 in med_4p:
        ptl, ptr, pbl, ans = 2 * (w1 + h1), 2 * (w2 + h1), 2 * (w1 + h2), 2 * (w2 + h2)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_four_rect_areas",
            f"A large rectangle is divided into four smaller rectangles by two lines parallel to its sides. The **perimeters** of the top-left, top-right, and bottom-left rectangles are {m(f'{ptl}\\text{{ cm}}')}, {m(f'{ptr}\\text{{ cm}}')}, and {m(f'{pbl}\\text{{ cm}}')}. What is the **perimeter** of the bottom-right rectangle in {m('\\text{cm}')}?",
            f"قُسّم مستطيل كبير بمستقيمين موازيين لأضلاعه إلى أربعة مستطيلات صغيرة. إذا كانت **محيطات** المستطيلات (أعلى اليسار، أعلى اليمين، أسفل اليسار) هي {m(f'{ptl}\\text{{ سم}}')} و{m(f'{ptr}\\text{{ سم}}')} و{m(f'{pbl}\\text{{ سم}}')}، فما **محيط** المستطيل أسفل اليمين بوحدة {m('\\text{سم}')}؟",
            ans, [(ptr * pbl) // ptl, ans - 4, ans + 4, ptr + pbl],
            "For **perimeters**, opposite corners have the same **sum**: \\( P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}} \\)!",
            "في **المحيطات** يتساوى **مجموع** كل مستطيلين متقابلين قطرياً: \\( P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}} \\)!",
            "Both diagonal pairs sum to \\( 2(w_1 + w_2 + h_1 + h_2) \\).",
            [
                f"Notice {m('P_{\\text{TL}} + P_{\\text{BR}} = 2(w_1+h_1) + 2(w_2+h_2) = P_{\\text{TR}} + P_{\\text{BL}}')}.",
                f"Therefore {m(f'P_{{\\text{{BR}}}} = {ptr} + {pbl} - {ptl} = {ans}\\text{{ cm}}')}.",
            ],
            f"{m(f'{ptl} + {ans} = {ptr} + {pbl} = {ptl + ans}')}.",
            "مجموع محيطَي المستطيلين المتقابلين قطرياً يساوي مجموع محيطَي الآخرين.",
            [
                f"نطبّق قاعدة مجموع المحيطات: {m(f'P_{{\\text{{TL}}}} + P_{{\\text{{BR}}}} = P_{{\\text{{TR}}}} + P_{{\\text{{BL}}}}')}.",
                f"إذن {m(f'P_{{\\text{{BR}}}} = {ptr} + {pbl} - {ptl} = {ans}\\text{{ سم}}')}.",
            ],
            f"تحقق: {m(f'{ptl} + {ans} = {ptr} + {pbl}')}.",
            diagram_en=svg_subdivided_rect_2x2(f"P={ptl}", f"P={ptr}", f"P={pbl}", "P=?"),
        ))
        idx += 1

    hard_9r = [
        (2, 3, 5, 3, 4, 6),
        (3, 4, 6, 2, 5, 4),
        (2, 5, 4, 3, 2, 5),
        (4, 3, 6, 3, 4, 5),
        (3, 6, 5, 2, 3, 4),
    ]
    for w1, w2, w3, h1, h2, h3 in hard_9r:
        a00, a01, a11, a12, a20 = w1 * h1, w2 * h1, w2 * h2, w3 * h2, w1 * h3
        ans = w3 * h3
        assert a20 * a01 * a12 == ans * a00 * a11
        grid_lbls = [
            [str(a00), str(a01), ""],
            ["", str(a11), str(a12)],
            [str(a20), "", "?"],
        ]
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_four_rect_areas",
            f"A rectangle is divided into {m(9)} smaller rectangles by two horizontal and two vertical lines. Five of the areas are shown in the diagram ({m(a00)}, {m(a01)}, {m(a11)}, {m(a12)}, and {m(a20)}). What is the area of the bottom-right rectangle marked {m('?')}?",
            f"قُسّم مستطيل بمستقيمين أفقيين ومستقيمين رأسيين إلى {m(9)} مستطيلات أصغر. حُدّدت مساحات خمسة منها في الشكل ({m(a00)}، {m(a01)}، {m(a11)}، {m(a12)}، و{m(a20)}). ما مساحة المستطيل الموجود أسفل اليمين والمشار إليه بالعلامة {m('?')}؟",
            ans, [ans - h3, ans + w3, a20 + a12 - a00, (a01 * a20) // a00],
            "Chain column ratios: find \\( w_2/w_1 \\) from Row 1 and \\( w_3/w_2 \\) from Row 2, then multiply by \\( A_{3,1} \\)!",
            "اربط نسب الأعمدة: أوجد \\( w_2/w_1 \\) من الصف الأول و\\( w_3/w_2 \\) من الصف الثاني ثم اضرب في \\( A_{3,1} \\)!",
            "Multiply column-width ratios across rows: \\( A_{3,3} = A_{3,1} \\cdot \\frac{A_{1,2}}{A_{1,1}} \\cdot \\frac{A_{2,3}}{A_{2,2}} \\).",
            [
                f"In Row 1, the column-width ratio is {m(f'w_2 / w_1 = {a01} / {a00} = {fmt_val(Fraction(w2, w1))}')}.",
                f"In Row 2, {m(f'w_3 / w_2 = {a12} / {a11} = {fmt_val(Fraction(w3, w2))}')}, so {m(f'w_3 / w_1 = {fmt_val(Fraction(w3, w1))}')}.",
                f"In Row 3, {m(f'A_{{3,3}} = A_{{3,1}} \\times (w_3 / w_1) = {a20} \\times {fmt_val(Fraction(w3, w1))} = {ans}')}.",
            ],
            f"All 9 cells match widths {m(f'({w1},{w2},{w3})')} and heights {m(f'({h1},{h2},{h3})')}, giving {m(f'{w3}\\times{h3}={ans}')}.",
            "نربط نسبة العرض الثالث إلى الأول عبر ضرب نسب الصفين الأول والثاني.",
            [
                f"من الصف الأول {m(f'w_2/w_1 = {a01}/{a00}')}، ومن الصف الثاني {m(f'w_3/w_2 = {a12}/{a11}')}.",
                f"بضرب النسبتين في مساحة أسفل اليسار {m(a20)} نحصل على {m(f'{a20} \\times \\frac{{{a01}}}{{{a00}}} \\times \\frac{{{a12}}}{{{a11}}} = {ans}')}.",
            ],
            f"تحقق: المساحة المطلوبة تساوي {m(f'{w3} \\times {h3} = {ans}')}.",
            diagram_en=svg_subdivided_rect_3x3(grid_lbls),
        ))
        idx += 1

    # 3. kang_cad_midpoint_shaded_square (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_mp = [24, 32, 40, 48, 56]
    for perim in easy_mp:
        s = perim // 4
        ans = (s * s) // 2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_midpoint_shaded_square",
            f"A square frame has **perimeter** {m(f'{perim}\\text{{ cm}}')}. Joining the midpoints of its four sides forms the shaded inner square. What is the area of the shaded inner square in {m('\\text{cm}^2')}?",
            f"إطار مربع الشكل **محيطه** {m(f'{perim}\\text{{ سم}}')}. بتوصيل منتصفات أضلاعه الأربعة يتكون المربع الداخلي المظلل. ما مساحة المربع الداخلي المظلل بوحدة {m('\\text{سم}^2')}؟",
            ans, [s * s, ans // 2, perim * 2, (perim * perim) // 8],
            f"First divide the perimeter by 4 to get the outer side \\( s = {s}\\text{{ cm}} \\), then take half of \\( s^2 \\).",
            f"اقسم المحيط على 4 أولاً لإيجاد طول الضلع \\( s = {s}\\text{{ سم}} \\)، ثم خذ نصف المساحة \\( s^2 \\).",
            "Outer side is \\( P/4 \\), and the midpoint square has area \\( \\frac{1}{2}s^2 \\).",
            [
                f"Outer side length is {m(f's = {perim} \\div 4 = {s}\\text{{ cm}}')}, so outer area is {m(f'{s}^2 = {s * s}\\text{{ cm}}^2')}.",
                f"The midpoint square covers exactly half the outer square: {m(f'{s * s} \\div 2 = {ans}\\text{{ cm}}^2')}.",
            ],
            f"4 outer corner right triangles have area {m(f'4 \\times \\frac{{1}}{{2}}({fmt_val(Fraction(s,2))})^2 = {ans}')}, leaving {m(ans)} inside.",
            "طول ضلع المربع الخارجي هو ربع المحيط، ومساحة مربع المنتصفات تساوي نصف مساحة المربع الخارجي.",
            [
                f"طول الضلع الخارجي {m(f's = {perim} \\div 4 = {s}\\text{{ سم}}')} ومساحته {m(f'{s*s}\\text{{ سم}}^2')}.",
                f"مساحة المربع المظلل تساوي النصف أي {m(f'{s*s} \\div 2 = {ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: {m(f'{s}^2 \\div 2 = {ans}')}.",
            diagram_en=svg_midpoint_square_shaded(f"P = {perim} cm", shade_inner=True),
        ))
        idx += 1

    med_eighths = [
        (6, [0, 3, 5]),
        (8, [1, 2, 5]),
        (10, [0, 4, 7]),
        (12, [1, 3, 6]),
        (14, [0, 2, 5]),
    ]
    for s_half, sh_idxs in med_eighths:
        s = 2 * s_half
        k_cnt = len(sh_idxs)
        assert (s * s * k_cnt) % 8 == 0
        sh_area = (s * s * k_cnt) // 8
        ans = 4 * s
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_midpoint_shaded_square",
            f"A square is divided into {m(8)} congruent right triangles by its two diagonals and two midlines, with {m(k_cnt)} of those triangles shaded. If the total shaded area is {m(f'{sh_area}\\text{{ cm}}^2')}, what is the **perimeter** of the square in {m('\\text{cm}')}?",
            f"قُسّم مربع بقطريه ومنصّفَي أضلاعه إلى {m(8)} مثلثات قائمة متطابقة، وظُلّلت {m(k_cnt)} مثلثات منها. إذا كانت المساحة المظللة الكلية {m(f'{sh_area}\\text{{ سم}}^2')}، فما **محيط** المربع بوحدة {m('\\text{سم}')}؟",
            ans, [s, s * s, ans // 2, ans + 8],
            f"Find the area of 1 small triangle ({m(sh_area // k_cnt)} cm²), multiply by 8 for \\( s^2 \\), take \\( \\sqrt{{s^2}} \\), and multiply by 4!",
            f"احسب مساحة المثلث الصغير الواحد ({m(sh_area // k_cnt)} سم²)، ثم اضرب في 8 لإيجاد \\( s^2 \\)، واستخرج الضلع ثم المحيط!",
            "Scale from \\( k/8 \\) of the square to the full area \\( s^2 \\), then compute \\( 4s \\).",
            [
                f"Each of the {m(8)} congruent triangles has area {m(f'{sh_area} \\div {k_cnt} = {sh_area // k_cnt}\\text{{ cm}}^2')}.",
                f"Full square area is {m(f'8 \\times {sh_area // k_cnt} = {s * s}\\text{{ cm}}^2')}, so side length {m(f's = {s}\\text{{ cm}}')}.",
                f"Perimeter of the square = {m(f'4 \\times {s} = {ans}\\text{{ cm}}')}.",
            ],
            f"{m(f'\\frac{{{k_cnt}}}{{8}} \\times {s}^2 = {sh_area}')}, and {m(f'4 \\times {s} = {ans}')}.",
            "نستنتج مساحة المربع الكلي من نسبة الجزء المظلل ثم نأخذ الجذر التربيعي ونضرب في 4.",
            [
                f"مساحة المثلث الواحد {m(f'{sh_area // k_cnt}\\text{{ سم}}^2')}، ومساحة المربع الكلي {m(f'8 \\times {sh_area // k_cnt} = {s*s}\\text{{ سم}}^2')}.",
                f"إذن طول الضلع {m(f's = {s}\\text{{ سم}}')} والمحيط {m(f'4 \\times {s} = {ans}\\text{{ سم}}')}.",
            ],
            f"تحقق: {m(f'4 \\times {s} = {ans}')}.",
            diagram_en=svg_square_eighths_shaded(sh_idxs, draw_horiz=True),
        ))
        idx += 1

    hard_inscr = [
        (10, 8, 4, 4),
        (12, 8, 6, 4),
        (12, 10, 4, 6),
        (14, 10, 6, 4),
        (16, 12, 6, 8),
    ]
    for L_r, W_r, c_top, c_right in hard_inscr:
        t1 = (W_r * c_top) // 2
        t2 = ((L_r - c_top) * (W_r - c_right)) // 2
        t3 = (L_r * c_right) // 2
        ans = L_r * W_r - (t1 + t2 + t3)
        assert 2 * ans == 2 * L_r * W_r - W_r * c_top - (L_r - c_top) * (W_r - c_right) - L_r * c_right
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_midpoint_shaded_square",
            f"Inside a {m(f'{L_r}\\text{{ cm}} \\times {W_r}\\text{{ cm}}')} rectangle, a shaded triangle connects the bottom-left corner to points on the top and right edges that split those edges into {m(f'{c_top}, {L_r - c_top}')} and {m(f'{W_r - c_right}, {c_right}')} as shown. What is the area of the shaded triangle in {m('\\text{cm}^2')}?",
            f"داخل مستطيل أبعاده {m(f'{L_r}\\text{{ سم}} \\times {W_r}\\text{{ سم}}')}، رُسم مثلث مظلل يصل الركن السفلي الأيسر بنقطتين على الضلعين العلوي والأيمن تقسمانهما إلى {m(f'{c_top}, {L_r - c_top}')} و{m(f'{W_r - c_right}, {c_right}')} كما في الشكل. ما مساحة المثلث المظلل بوحدة {m('\\text{سم}^2')}؟",
            ans, [(L_r * W_r) // 2, ans - 4, ans + 6, t1 + t2 + t3],
            "Subtract the areas of the **three unshaded right triangles** around the border from the full rectangle!",
            "اطرح مساحات **المثلثات القائمة الثلاثة غير المظللة** عند الزوايا من مساحة المستطيل الكلي!",
            "Use the bounding-box subtraction technique: \\( A_{\\text{rect}} - (T_1 + T_2 + T_3) \\).",
            [
                f"Full rectangle area = {m(f'{L_r} \\times {W_r} = {L_r * W_r}\\text{{ cm}}^2')}.",
                f"Top-left right triangle = {m(f'\\frac{{1}}{{2}}({W_r})({c_top}) = {t1}')}; top-right = {m(f'\\frac{{1}}{{2}}({L_r - c_top})({W_r - c_right}) = {t2}')}; bottom-right = {m(f'\\frac{{1}}{{2}}({L_r})({c_right}) = {t3}')}.",
                f"Shaded area = {m(f'{L_r * W_r} - ({t1} + {t2} + {t3}) = {ans}\\text{{ cm}}^2')}.",
            ],
            f"{m(f'{ans} + {t1} + {t2} + {t3} = {L_r * W_r}')}.",
            "نطرح مساحات المثلثات القائمة الثلاثة البيضاء المحيطة من مساحة المستطيل الكلي.",
            [
                f"مساحة المستطيل الكلي = {m(f'{L_r} \\times {W_r} = {L_r * W_r}\\text{{ سم}}^2')}.",
                f"مساحات المثلثات البيضاء الثلاثة هي {m(t1)} و{m(t2)} و{m(t3)} ومجموعها {m(t1 + t2 + t3)}.",
                f"إذن مساحة المثلث المظلل = {m(f'{L_r * W_r} - {t1 + t2 + t3} = {ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: {m(f'{ans} + {t1 + t2 + t3} = {L_r * W_r}')}.",
            diagram_en=svg_inscribed_corner_triangle_in_rect(L_r, W_r, c_top, c_right),
        ))
        idx += 1

    # 4. kang_cad_circle_in_square_area (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_cs = [28, 42, 56, 70, 84]
    for s in easy_cs:
        r = s // 2
        c_area = (22 * r * r) // 7
        ans = s * s - c_area
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_circle_in_square_area",
            f"A circle is inscribed inside a square of side length {m(f'{s}\\text{{ cm}}')}. Using {m('\\pi = \\frac{22}{7}')}, what is the total area of the four shaded corner regions outside the circle in {m('\\text{cm}^2')}?",
            f"رُسمت دائرة تمس أضلاع مربع طول ضلعه {m(f'{s}\\text{{ سم}}')} من الداخل. باعتبار {m('\\pi = \\frac{22}{7}')}، ما المساحة الكلية للمناطق الأربع المظللة خارج الدائرة بوحدة {m('\\text{سم}^2')}؟",
            ans, [ans // 4, c_area, s * s - (22 * s) // 7, ans + r * 2],
            f"Radius \\( r = {s}/2 = {r}\\text{{ cm}} \\); subtract \\( \\pi r^2 \\) from \\( {s}^2 \\).",
            f"نصف القطر \\( r = {r}\\text{{ سم}} \\)؛ اطرح مساحة الدائرة \\( \\pi r^2 \\) من مساحة المربع \\( {s}^2 \\).",
            "Shaded area equals \\( s^2 - \\pi (s/2)^2 \\).",
            [
                f"Square area = {m(f'{s}^2 = {s * s}\\text{{ cm}}^2')}, and inscribed radius {m(f'r = {r}\\text{{ cm}}')}.",
                f"Circle area = {m(f'\\frac{{22}}{{7}} \\times {r}^2 = {c_area}\\text{{ cm}}^2')}.",
                f"Shaded corners = {m(f'{s * s} - {c_area} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"{m(f'{c_area} + {ans} = {s * s}')}.",
            "نطرح مساحة الدائرة المرسومة بالداخل من مساحة المربع.",
            [
                f"مساحة المربع {m(f'{s*s}\\text{{ سم}}^2')}، ونصف قطر الدائرة {m(f'r = {r}\\text{{ سم}}')}.",
                f"مساحة الدائرة {m(f'\\frac{{22}}{{7}} \\times {r}^2 = {c_area}\\text{{ سم}}^2')}، والباقي المظلل {m(f'{s*s} - {c_area} = {ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: {m(f'{c_area} + {ans} = {s * s}')}.",
            diagram_en=svg_square_circle_shaded(f"{s} cm", "inscribed_outside"),
        ))
        idx += 1

    med_stad = [(30, 14), (45, 21), (50, 28), (60, 35), (80, 42)]
    for L_st, D_st in med_stad:
        circ_p = (22 * D_st) // 7
        ans = circ_p + 2 * L_st
        trap_inner = ans + 2 * D_st
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_circle_in_square_area",
            f"A Kangaroo stadium track consists of a central {m(f'{L_st}\\text{{ m}} \\times {D_st}\\text{{ m}}')} rectangle capped on its left and right ends by two outward semicircles of diameter {m(f'{D_st}\\text{{ m}}')}. Using {m('\\pi = \\frac{22}{7}')}, what is the **outer perimeter** of the stadium track in meters?",
            f"يتكوّن مضمار ملعب من مستطيل أوسط أبعاده {m(f'{L_st}\\text{{ م}} \\times {D_st}\\text{{ م}}')} ينتهي من طرفيه الأيمن والأيسر بنصفَي دائرتين خارجيتين قطر كلٍّ منهما {m(f'{D_st}\\text{{ م}}')}. باعتبار {m('\\pi = \\frac{22}{7}')}، ما **المحيط الخارجي** للمضمار بالأمتار؟",
            ans, [trap_inner, circ_p + L_st, ans - L_st, circ_p // 2 + 2 * L_st],
            "Do NOT include the two dashed interior segments! The outer boundary is 2 straight sides + 1 full circle circumference.",
            "لا تحتسب الضلعين المتقطعين بالداخل! المحيط الخارجي يتكون من ضلعين مستقيمين فقط + محيط دائرة كاملة.",
            "Combine the two semicircular arcs into one full circumference \\( \\pi D \\) and add \\( 2L \\).",
            [
                f"The two semicircular ends together form one complete circle of diameter {m(f'{D_st}\\text{{ m}}')}, giving arc length {m(f'\\frac{{22}}{{7}} \\times {D_st} = {circ_p}\\text{{ m}}')}.",
                f"Add the top and bottom straight segments ({m(f'2 \\times {L_st} = {2 * L_st}\\text{{ m}}')}) while ignoring the interior dashed lines.",
                f"Total outer perimeter = {m(f'{circ_p} + {2 * L_st} = {ans}\\text{{ m}}')}.",
            ],
            f"{m(f'{circ_p} + {2 * L_st} = {ans}\\text{{ m}}')} (avoiding the interior-diameter trap {m(trap_inner)}).",
            "مجموع القوسين الجانبيين يعادل محيط دائرة كاملة، ونضيف إليه الضلعين الأفقيين فقط.",
            [
                f"طول القوسين معاً = {m(f'\\frac{{22}}{{7}} \\times {D_st} = {circ_p}\\text{{ م}}')}.",
                f"نضيف الضلعين العلوي والسفلي {m(f'2 \\times {L_st} = {2 * L_st}\\text{{ م}}')} فنحصل على {m(f'{ans}\\text{{ م}}')}.",
            ],
            f"تحقق: {m(f'{circ_p} + {2 * L_st} = {ans}')}.",
            diagram_en=svg_square_circle_shaded(f"{L_st} m", "stadium"),
        ))
        idx += 1

    hard_qs = [14, 28, 42, 56, 70]
    for s in hard_qs:
        q_area = (22 * s * s) // (7 * 4)
        semi_area = (22 * (s // 2) ** 2) // (7 * 2)
        ans = q_area - semi_area
        assert ans == semi_area
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_circle_in_square_area",
            f"Inside a square of side length {m(f'{s}\\text{{ cm}}')}, a quarter-circle of radius {m(f'{s}\\text{{ cm}}')} is centered at the bottom-left corner, and a white semicircle of **diameter** {m(f'{s}\\text{{ cm}}')} is cut out along the bottom edge as shown. Using {m('\\pi = \\frac{22}{7}')}, what is the area of the shaded region in {m('\\text{cm}^2')}?",
            f"داخل مربع طول ضلعه {m(f'{s}\\text{{ سم}}')}، رُسم ربع دائرة نصف قطرها {m(f'{s}\\text{{ سم}}')} مركزها الركن السفلي الأيسر، واقتُطع منها نصف دائرة بيضاء **قطرها** {m(f'{s}\\text{{ سم}}')} على الضلع السفلي كما في الشكل. باعتبار {m('\\pi = \\frac{22}{7}')}، ما مساحة المنطقة المظللة بوحدة {m('\\text{سم}^2')}؟",
            ans, [q_area, s * s - q_area, ans * 3 // 2, s * s - ans],
            "Compare \\( \\frac{1}{4}\\pi s^2 \\) with \\( \\frac{1}{2}\\pi (s/2)^2 = \\frac{1}{8}\\pi s^2 \\)—the semicircle is **half** the quarter-circle!",
            "قارن مساحة ربع الدائرة \\( \\frac{1}{4}\\pi s^2 \\) بمساحة نصف الدائرة \\( \\frac{1}{2}\\pi (s/2)^2 = \\frac{1}{8}\\pi s^2 \\)!",
            "Subtract \\( \\frac{1}{8}\\pi s^2 \\) from \\( \\frac{1}{4}\\pi s^2 \\) to get \\( \\frac{1}{8}\\pi s^2 \\).",
            [
                f"Quarter-circle of radius {m(s)} has area {m(f'\\frac{{1}}{{4}} \\times \\frac{{22}}{{7}} \\times {s}^2 = {q_area}\\text{{ cm}}^2')}.",
                f"White semicircle has radius {m(s // 2)}, so its area is {m(f'\\frac{{1}}{{2}} \\times \\frac{{22}}{{7}} \\times {s // 2}^2 = {semi_area}\\text{{ cm}}^2')}.",
                f"Shaded area = {m(f'{q_area} - {semi_area} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"{m(f'\\frac{{1}}{{8}} \\times \\frac{{22}}{{7}} \\times {s}^2 = {ans}\\text{{ cm}}^2')}.",
            "مساحة نصف الدائرة الصغرى تساوي نصف مساحة ربع الدائرة الكبرى بالضبط.",
            [
                f"مساحة ربع الدائرة الكبرى = {m(f'{q_area}\\text{{ سم}}^2')}.",
                f"مساحة نصف الدائرة البيضاء (نصف قطرها {m(s // 2)}) = {m(f'{semi_area}\\text{{ سم}}^2')}.",
                f"المساحة المظللة = {m(f'{q_area} - {semi_area} = {ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: {m(f'{q_area} - {semi_area} = {ans}')}.",
            diagram_en=svg_square_circle_shaded(f"{s} cm", "quarter_minus_semi"),
        ))
        idx += 1

    assert len(qs) == 60
    return qs


def _roll_die(state: tuple[int, int, int, int, int, int], moves: str) -> tuple[int, int, int, int, int, int]:
    t, bo, s, n, e, w = state
    for mv in moves:
        if mv == "E":
            t, bo, s, n, e, w = w, e, s, n, t, bo
        elif mv == "W":
            t, bo, s, n, e, w = e, w, s, n, bo, t
        elif mv == "S":
            t, bo, s, n, e, w = n, s, t, bo, e, w
        elif mv == "N":
            t, bo, s, n, e, w = s, n, bo, t, e, w
    return t, bo, s, n, e, w


def _voxel_surface_area(voxels: set[tuple[int, int, int]]) -> int:
    dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return sum(1 for (x, y, z) in voxels for (dx, dy, dz) in dirs if (x + dx, y + dy, z + dz) not in voxels)


def _unit_4() -> list[dict]:
    """Unit 4 (Lesson 3.4 — 3D Spatial Geometry): QIDs 181..240."""
    qs: list[dict] = []
    idx = 181

    # 1. kang_cad_painted_prism_cubes (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_p0 = [(4, 4, 5), (5, 5, 6), (4, 5, 6), (3, 5, 7), (4, 6, 7)]
    for a, b, c in easy_p0:
        ans = (a - 2) * (b - 2) * (c - 2)
        tot = a * b * c
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_painted_prism_cubes",
            f"A solid {m(f'{a} \\times {b} \\times {c}')} wooden block is dipped in purple paint so all six outer faces are coated, then cut into {m(tot)} unit cubes. How many unit cubes have **no paint at all**?",
            f"غُمست كتلة خشبية مصمتة أبعادها {m(f'{a} \\times {b} \\times {c}')} في طلاء بنفسجي فغطّى أوجهها الستة جميعاً، ثم قُطّعت إلى {m(tot)} مكعباً وحدوياً. كم مكعباً صغيراً **لم يصله أي طلاء إطلاقاً**؟",
            ans, [(a - 1) * (b - 1) * (c - 1), tot - ans, ans + 8, max(2, ans - 4)],
            "Peel off 1 layer from both ends of each dimension: the unpainted core has size \\( (a-2)(b-2)(c-2) \\).",
            "قشّر طبقة واحدة من كل طرف في الأبعاد الثلاثة؛ القلب غير المطلي أبعاده \\( (a-2)(b-2)(c-2) \\).",
            "Compute the volume of the inner unpainted box \\( (a-2) \\times (b-2) \\times (c-2) \\).",
            [
                "Removing the outer painted layer reduces each dimension by 2.",
                f"The unpainted interior core is a {m(f'({a}-2) \\times ({b}-2) \\times ({c}-2) = {a-2} \\times {b-2} \\times {c-2}')} block.",
                f"Number of unpainted unit cubes = {m(f'{a-2} \\times {b-2} \\times {c-2} = {ans}')}.",
            ],
            f"{m(f'{a-2} \\times {b-2} \\times {c-2} = {ans}')} inner cubes out of {m(tot)}.",
            "إزالة الطبقة الخارجية المطلية ينقص كل بُعد بمقدار 2.",
            [
                f"أبعاد القلب الداخلي غير المطلي هي {m(f'{a-2} \\times {b-2} \\times {c-2}')}.",
                f"عدد المكعبات الخالية من الطلاء = {m(f'{a-2} \\times {b-2} \\times {c-2} = {ans}')}.",
            ],
            f"تحقق: {m(f'{a-2} \\times {b-2} \\times {c-2} = {ans}')}.",
            diagram_en=svg_painted_cube_3d(min(a, 5)),
        ))
        idx += 1

    med_p1 = [(3, 4, 6), (4, 4, 6), (3, 5, 6), (4, 5, 6), (5, 5, 7)]
    for a, b, c in med_p1:
        ans = 2 * ((a - 2) * (b - 2) + (b - 2) * (c - 2) + (c - 2) * (a - 2))
        n2_trap = 4 * ((a - 2) + (b - 2) + (c - 2))
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_painted_prism_cubes",
            f"All six faces of a {m(f'{a} \\times {b} \\times {c}')} block are painted green, and the block is sawed into {m(a * b * c)} unit cubes. How many unit cubes have **exactly 1** green face?",
            f"طُليت جميع الأوجه الستة لمتوازي مستطيلات أبعاده {m(f'{a} \\times {b} \\times {c}')} باللون الأخضر ثم قُطّع إلى {m(a * b * c)} مكعباً صغيراً. كم مكعباً صغيراً له **وجه أخضر واحد بالضبط**؟",
            ans, [n2_trap, ans // 2, ans + 8, (a - 2) * (b - 2) * (c - 2)],
            "One-face cubes form the inner \\( (x-2) \\times (y-2) \\) rectangle on each of the 6 faces!",
            "مكعبات الوجه الواحد تشكّل المستطيل الداخلي \\( (x-2) \\times (y-2) \\) في وسط كل وجه من الأوجه الستة!",
            "Sum the interior rectangles across the three pairs of opposite faces: \\( 2[(a-2)(b-2)+(b-2)(c-2)+(c-2)(a-2)] \\).",
            [
                f"Opposite {m(f'{a}\\times{b}')} faces contribute {m(f'2 \\times ({a-2})({b-2}) = {2*(a-2)*(b-2)}')}.",
                f"Opposite {m(f'{b}\\times{c}')} faces contribute {m(f'2 \\times ({b-2})({c-2}) = {2*(b-2)*(c-2)}')}.",
                f"Opposite {m(f'{c}\\times{a}')} faces contribute {m(f'2 \\times ({c-2})({a-2}) = {2*(c-2)*(a-2)}')}, giving total {m(ans)}.",
            ],
            f"Total 1-face cubes = {m(ans)} (distinct from the {m(n2_trap)} two-face edge cubes).",
            "نجمع المستطيلات الداخلية بعيداً عن الحواف على أزواج الأوجه الثلاثة.",
            [
                f"المساهمات من أزواج الأوجه الثلاثة هي {m(2*(a-2)*(b-2))} و{m(2*(b-2)*(c-2))} و{m(2*(c-2)*(a-2))}.",
                f"بجمعها نحصل على {m(ans)} مكعباً بوجه واحد مطلي.",
            ],
            f"تحقق: المجموع يساوي {m(ans)}.",
            diagram_en=svg_painted_cube_3d(min(b, 5)),
        ))
        idx += 1

    hard_2col = [(4, 5, 4), (5, 6, 4), (4, 6, 5), (5, 5, 5), (6, 7, 4)]
    for a, b, c in hard_2col:
        ans = sum(
            1 for i in range(a) for j in range(b) for k in range(c)
            if (k == 0 or k == c - 1) and (0 < i < a - 1 and 0 < j < b - 1)
        )
        assert ans == 2 * (a - 2) * (b - 2)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_painted_prism_cubes",
            f"A {m(f'{a} \\times {b} \\times {c}')} block ({m(a)} wide, {m(b)} deep, {m(c)} tall) has its **top and bottom** {m(f'{a} \\times {b}')} faces painted **red** and its **four vertical side** faces painted **blue**, then is cut into {m(a * b * c)} unit cubes. How many unit cubes have **red paint and NO blue paint**?",
            f"متوازي مستطيلات أبعاده {m(f'{a} \\times {b} \\times {c}')} طُلي وجهاه **العلوي والسفلي** ({m(f'{a} \\times {b}')}) باللون **الأحمر**، وطُليت أوجهه **الجانبية الأربعة** باللون **الأزرق**، ثم قُطّع إلى {m(a * b * c)} مكعباً صغيراً. كم مكعباً صغيراً يحمل **طلاءً أحمر ولا يحمل أي طلاء أزرق**؟",
            ans, [2 * a * b, (a - 2) * (b - 2), ans + 4 * (a + b - 4), (a - 2) * (b - 2) * (c - 2)],
            "Any cube on the outer rim of the top or bottom face touches a vertical blue wall! Count only interior cells of the top and bottom faces.",
            "أي مكعب على حافة الوجه العلوي أو السفلي يلامس جداراً أزرق! احسب فقط المربعات الداخلية للوجهين العلوي والسفلي.",
            "Avoid all 4 vertical blue walls by restricting to the \\( (a-2) \\times (b-2) \\) interior of the top and bottom layers.",
            [
                f"To have **no blue paint**, a unit cube cannot lie on the front, back, left, or right outer layers—leaving {m(f'({a}-2)\\times({b}-2) = {(a-2)*(b-2)}')} vertical columns.",
                f"Since height {m(f'{c} \\ge 3')}, the top cube and bottom cube of each such column are distinct and each receives red paint.",
                f"Total red-only cubes = {m(f'2 \\times {(a - 2) * (b - 2)} = {ans}')}.",
            ],
            f"{m(f'2 \\times ({a}-2) \\times ({b}-2) = {ans}')} cubes.",
            "الابتعاد عن الجدران الزرقاء الأربعة يحصرنا في المستطيل الداخلي للطبقتين العليا والسفلى.",
            [
                f"عدد الأعمدة الداخلية البعيدة عن الأوجه الزرقاء يساوي {m(f'({a}-2)({b}-2) = {(a-2)*(b-2)}')}.",
                f"المكعب العلوي والمكعب السفلي في كل عمود منها يحملان اللون الأحمر فقط، فيكون العدد {m(f'2 \\times {(a-2)*(b-2)} = {ans}')}.",
            ],
            f"تحقق: {m(f'2 \\times {(a-2)*(b-2)} = {ans}')}.",
            diagram_en=svg_painted_cube_3d(min(a, 5)),
        ))
        idx += 1

    # 2. kang_cad_rolling_die_top (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_rolls = [
        ((1, 6, 2, 5, 3, 4), "ES", "1 step East, then 1 step South", "خطوة شرقاً ثم خطوة جنوباً"),
        ((1, 6, 2, 5, 3, 4), "SE", "1 step South, then 1 step East", "خطوة جنوباً ثم خطوة شرقاً"),
        ((2, 5, 3, 4, 1, 6), "EEN", "2 steps East, then 1 step North", "خطوتين شرقاً ثم خطوة شمالاً"),
        ((3, 4, 1, 6, 2, 5), "SSW", "2 steps South, then 1 step West", "خطوتين جنوباً ثم خطوة غرباً"),
        ((4, 3, 2, 5, 6, 1), "ENE", "1 step East, 1 step North, then 1 step East", "خطوة شرقاً ثم خطوة شمالاً ثم خطوة شرقاً"),
    ]
    for init_st, mv_str, desc_en, desc_ar in easy_rolls:
        fin_st = _roll_die(init_st, mv_str)
        ans = fin_st[0]
        other_opts = [v for v in range(1, 7) if v != ans][:4]
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_rolling_die_top",
            f"A standard die (opposite faces sum to {m(7)}) starts with **{init_st[0]} on top**, **{init_st[2]} facing South**, and **{init_st[4]} facing East**. It rolls **{desc_en}**. Which number is on **top** at the end?",
            f"يبدأ حجر نرد قياسي (مجموع كل وجهين متقابلين {m(7)}) والرقم **{init_st[0]} في الأعلى** و**{init_st[2]} جنوباً** و**{init_st[4]} شرقاً**. يتدحرج النرد **{desc_ar}**. ما الرقم الذي يستقر في **الأعلى** في النهاية؟",
            ans, other_opts,
            "Track (Top, Bottom, South, North, East, West) one roll at a time using opposite pairs summing to 7.",
            "تتبّع الأوجه الستة خطوة بخطوة مع تذكّر أن مجموع كل وجهين متقابلين يساوي 7.",
            "Update the four rotating faces on each step while keeping the two axis faces fixed.",
            [
                f"Initial faces (Top, Bottom, South, North, East, West) = {m(str(init_st))}.",
                f"Applying the roll sequence `{mv_str}` step by step transforms the orientation to {m(str(fin_st))}.",
                f"Thus the face on **top** at the end is {m(ans)}.",
            ],
            f"Opposite check at end: Top {m(fin_st[0])} + Bottom {m(fin_st[1])} = {m(7)}.",
            "نحدّث الأوجه الأربعة المتحركة في كل خطوة مع ثبات الوجهين الجانبيين لمحور الدحرجة.",
            [
                f"الوضع الابتدائي للأوجه (أعلى، أسفل، جنوب، شمال، شرق، غرب) هو {m(str(init_st))}.",
                f"بتطبيق خطوات الدحرجة بالترتيب يصبح الوضع النهائي {m(str(fin_st))}، أي أن الوجه العلوي هو {m(ans)}.",
            ],
            f"تحقق: الأعلى {m(fin_st[0])} + الأسفل {m(fin_st[1])} = {m(7)}.",
            diagram_en=svg_kang_cube_faces(str(init_st[0]), str(init_st[2]), str(init_st[4])),
        ))
        idx += 1

    med_walks = [
        ((1, 6, 2, 5, 3, 4), "ENNE", [(0, 3), (1, 3), (1, 2), (1, 1), (2, 1)]),
        ((1, 6, 3, 4, 5, 2), "EESS", [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        ((2, 5, 1, 6, 3, 4), "NEEES", [(0, 2), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]),
        ((6, 1, 2, 5, 4, 3), "SENES", [(0, 1), (0, 2), (1, 2), (1, 1), (2, 1), (2, 2)]),
        ((3, 4, 5, 2, 1, 6), "EENNW", [(1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]),
    ]
    for init_st, mv_str, path_cells in med_walks:
        fin_st = _roll_die(init_st, mv_str)
        ans = fin_st[1]  # bottom face touching the star!
        other_opts = [v for v in range(1, 7) if v != ans][:4]
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_rolling_die_top",
            f"A standard die sits on start cell **S** with **{init_st[0]} on top**, **{init_st[2]} facing South (down the grid)**, and **{init_st[4]} facing East (right)**. It rolls along the red path `{mv_str}` to the starred cell **★**. Which number touches the **board (bottom face)** on cell ★?",
            f"يقف حجر نرد قياسي على الخلية **S** والرقم **{init_st[0]} في الأعلى** و**{init_st[2]} باتجاه الجنوب (لأسفل الشبكة)** و**{init_st[4]} باتجاه الشرق (يميناً)**. يتدحرج على المسار الأحمر `{mv_str}` حتى يصل إلى الخلية **★**. ما الرقم الملامس **لأرضية اللوحة (الوجه السفلي)** فوق الخلية ★؟",
            ans, other_opts,
            "Be careful: the question asks for the **bottom** face touching ★, which equals \\( 7 - \\text{Top} \\)!",
            "انتبه: المطلوب هو **الوجه السفلي** الملامس للخلية ★، ويساوي \\( 7 - \\text{العلوي} \\)!",
            "Simulate the roll sequence along the grid path and read the **bottom** face.",
            [
                f"Starting from {m(str(init_st))}, trace the rolls `{mv_str}` along the grid cells.",
                f"At cell ★, the top face is {m(fin_st[0])} and the **bottom** face touching ★ is {m(f'7 - {fin_st[0]} = {ans}')}.",
            ],
            f"Top {m(fin_st[0])} + Bottom {m(ans)} = {m(7)}.",
            "نتتبع الدحرجة على الشبكة ثم نأخذ الوجه السفلي المكمل للسبعة.",
            [
                f"بتتبع الحركات `{mv_str}` من الوضع الابتدائي يصل النرد إلى الخلية ★ والرقم {m(fin_st[0])} في الأعلى.",
                f"إذن الوجه السفلي الملامس للخلية ★ هو {m(f'7 - {fin_st[0]} = {ans}')}.",
            ],
            f"تحقق: {m(f'{fin_st[0]} + {ans} = 7')}.",
            diagram_en=svg_kang_grid_walk(5, 4, path_cells),
        ))
        idx += 1

    hard_towers = [
        (3, 6, "3 standard dice", 3),
        (4, 5, "4 standard dice", 4),
        (5, 2, "5 standard dice", 5),
        (4, 1, "4 standard dice", 4),
        (6, 4, "6 standard dice", 6),
    ]
    for k_dice, top_v, lbl_en, stack_h in hard_towers:
        ans = 14 * k_dice + top_v
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_rolling_die_top",
            f"A vertical tower of **{lbl_en}** (opposite faces on each die sum to {m(7)}) stands flat on a wooden table. If the very top face of the tower shows **{m(top_v)}**, what is the sum of the numbers on **all visible faces** as you walk completely around the table?",
            f"برج رأسي مكوّن من **{m(k_dice)} أحجار نرد قياسية** (مجموع كل وجهين متقابلين {m(7)}) موضوع على طاولة خشبية. إذا كان الوجه العلوي لقمة البرج يُظهر الرقم **{m(top_v)}**، فما مجموع الأرقام على **جميع الأوجه المرئية** عند الدوران حول الطاولة؟",
            ans, [ans + (7 - top_v), 14 * k_dice, ans - 7, 21 * k_dice - top_v],
            "Every die in the tower shows 4 side faces consisting of **two opposite pairs**—what do those 4 side faces always sum to?",
            "كل حجر نرد في البرج يُظهر 4 أوجه جانبية تمثّل **زوجين متقابلين**—كم يبلغ مجموع هذه الأوجه الأربعة دائماً؟",
            "Each die's 4 vertical faces form two opposite pairs summing to \\( 7 + 7 = 14 \\), plus the single top face!",
            [
                f"On every standard die, the 4 vertical side faces consist of two opposite pairs, so they **always** sum to {m('7 + 7 = 14')} regardless of horizontal rotation.",
                f"Across {m(k_dice)} stacked dice, the side faces contribute {m(f'{k_dice} \\times 14 = {14 * k_dice}')}.",
                f"Adding the single visible top face ({m(top_v)}) gives {m(f'{14 * k_dice} + {top_v} = {ans}')}.",
            ],
            f"{m(f'4 \\times {k_dice} + 1 = {4*k_dice+1}')} visible faces summing to {m(ans)}.",
            "الأوجه الجانبية الأربعة لكل نرد تشكل زوجين متقابلين مجموعهما دائماً 14.",
            [
                f"يساهم كل نرد من الأحجار الـ {m(k_dice)} بمقدار {m('7 + 7 = 14')} على الجوانب الأربعة مهما دار أفقياً.",
                f"مجموع الجوانب {m(f'{k_dice} \\times 14 = {14 * k_dice}')}، وبإضافة قمة البرج ({m(top_v)}) نحصل على {m(ans)}.",
            ],
            f"تحقق: {m(f'{14 * k_dice} + {top_v} = {ans}')}.",
            diagram_en=svg_cube_stack_3d((min(stack_h, 4),)),
        ))
        idx += 1

    # 3. kang_cad_ant_on_box_net (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_nets = [
        ([(1, 0, "2"), (0, 1, "5"), (1, 1, "1"), (2, 1, "4"), (3, 1, "?"), (1, 2, "7")], 9, "1"),
        ([(0, 0, "3"), (0, 1, "6"), (1, 1, "8"), (2, 1, "?"), (2, 2, "4"), (1, 2, "2")], 10, "6"),
        ([(1, 0, "?"), (0, 1, "4"), (1, 1, "5"), (2, 1, "7"), (1, 2, "9"), (1, 3, "6")], 11, "9"),
        ([(0, 1, "3"), (1, 1, "8"), (2, 1, "9"), (3, 1, "?"), (2, 0, "5"), (2, 2, "7")], 12, "8"),
        ([(1, 0, "6"), (1, 1, "4"), (1, 2, "9"), (0, 2, "5"), (2, 2, "?"), (1, 3, "11")], 15, "5"),
    ]
    for cells_net, opp_sum, opp_partner in easy_nets:
        ans = opp_sum - int(opp_partner)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_ant_on_box_net",
            f"The six-square net shown folds into a cube in which **every pair of opposite faces adds up to {m(opp_sum)}**. What number must replace {m('?')}?",
            f"تُطوى الشبكة السداسية الموضحة لتكوّن مكعباً يكون فيه **مجموع كل وجهين متقابلين مساوياً لـ {m(opp_sum)}**. ما العدد الذي يجب وضعه مكان العلامة {m('?')}؟",
            ans, [ans + 2, max(1, ans - 2), opp_sum - ans, ans + 3],
            "Faces separated by one intervening square along a straight strip fold to become **opposite** faces!",
            "كل مربعين يفصل بينهما مربع واحد على استقامة واحدة يصبحان **وجهين متقابلين** عند الطي!",
            f"Identify the square two steps away from `?` ({m(opp_partner)}) and subtract from {m(opp_sum)}.",
            [
                f"When folded into a cube, the square marked `?` lands directly opposite the square labeled {m(opp_partner)}.",
                f"Since opposite faces sum to {m(opp_sum)}, `?` must equal {m(f'{opp_sum} - {opp_partner} = {ans}')}.",
            ],
            f"{m(f'{opp_partner} + {ans} = {opp_sum}')}.",
            "نحدد المربع المقابل للمربع المجهول عند طي الشبكة ثم نطرح قيمته من المجموع المعطى.",
            [
                f"عند طي الشبكة يقابل المربع `?` المربع الذي يحمل العدد {m(opp_partner)}.",
                f"بما أن مجموع المتقابلين {m(opp_sum)}، فإن القيمة المجهولة تساوي {m(f'{opp_sum} - {opp_partner} = {ans}')}.",
            ],
            f"تحقق: {m(f'{opp_partner} + {ans} = {opp_sum}')}.",
            diagram_en=svg_cube_net(cells_net),
        ))
        idx += 1

    med_ant = [(2, 4, 8), (4, 5, 12), (5, 7, 16), (3, 4, 24), (8, 10, 24)]
    for a, b, c in med_ant:
        ans = math.isqrt((a + b) ** 2 + c ** 2)
        assert ans * ans == (a + b) ** 2 + c ** 2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_ant_on_box_net",
            f"An ant sits at corner {m('A')} of a closed {m(f'{a}\\text{{ cm}} \\times {b}\\text{{ cm}} \\times {c}\\text{{ cm}}')} gift box and crawls along its outer surface to the diagonally opposite corner {m('B')} in 3D space. What is the **shortest** possible crawl distance in {m('\\text{cm}')}?",
            f"تقف نملة عند الركن {m('A')} لصندوق هدايا مغلق أبعاده {m(f'{a}\\text{{ سم}} \\times {b}\\text{{ سم}} \\times {c}\\text{{ سم}}')} وتزحف على سطحه الخارجي إلى الركن المقابل له قطرياً في الفراغ {m('B')}. ما **أقصر** مسافة ممكنة بوحدة {m('\\text{سم}')}؟",
            ans, [a + b + c, ans + 2, ans - 1, a + c],
            f"Unfold two adjacent faces pairing the **two smallest** dimensions ({m(f'{a}+{b}={a+b}')}) against {m(c)}!",
            f"افرد وجهين متجاورين بجمع **أصغر بُعدين** ({m(f'{a}+{b}={a+b}')}) مع البُعد الثالث {m(c)}!",
            "Minimize \\( \\sqrt{(x+y)^2 + z^2} \\) by setting \\( x, y \\) to the two shortest box edges.",
            [
                f"Pair the two shortest edges {m(a)} and {m(b)} to form a flat unfolded leg of length {m(f'{a} + {b} = {a + b}\\text{{ cm}}')}.",
                f"The perpendicular leg has length {m(f'{c}\\text{{ cm}}')}.",
                f"By the Pythagorean theorem, {m(f'd_{{\\min}} = \\sqrt{{{a+b}^2 + {c}^2}} = \\sqrt{{{(a+b)**2 + c**2}}} = {ans}\\text{{ cm}}')}.",
            ],
            f"{m(f'{a+b}^2 + {c}^2 = {(a+b)**2} + {c**2} = {ans}^2')}.",
            "نجمع أصغر بُعدين على الشبكة المفرودة ثم نطبق نظرية فيثاغورس.",
            [
                f"نجمع البُعدين الأصغرين: {m(f'{a} + {b} = {a + b}\\text{{ سم}}')} مع تعامد البُعد {m(f'{c}\\text{{ سم}}')}.",
                f"أقصر مسافة = {m(f'\\sqrt{{{a+b}^2 + {c}^2}} = {ans}\\text{{ سم}}')}.",
            ],
            f"تحقق: {m(f'{(a+b)**2} + {c**2} = {ans**2}')}.",
            diagram_en=svg_cube_net([(1, 0, "Top"), (0, 1, str(a)), (1, 1, str(b)), (2, 1, str(c)), (1, 2, "Base"), (3, 1, "Back")]),
        ))
        idx += 1

    hard_wrap = [(3, 5), (2, 15), (3, 16), (5, 21), (6, 7)]
    for s_col, h_col in hard_wrap:
        ans = math.isqrt((4 * s_col) ** 2 + h_col ** 2)
        assert ans * ans == (4 * s_col) ** 2 + h_col ** 2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_ant_on_box_net",
            f"A decorative ribbon starts at a bottom corner of a square pillar with base {m(f'{s_col}\\text{{ cm}} \\times {s_col}\\text{{ cm}}')} and height {m(f'{h_col}\\text{{ cm}}')}, wraps **once completely around all four vertical faces**, and ends at the top corner directly above its starting point. What is the **minimum** ribbon length in {m('\\text{cm}')}?",
            f"يبدأ شريط زينة من أحد أركان قاعدة عمود رباعي مربع القاعدة ({m(f'{s_col}\\text{{ سم}} \\times {s_col}\\text{{ سم}}')}) ارتفاعه {m(f'{h_col}\\text{{ سم}}')}، ويلتف **دورة كاملة واحدة حول الأوجه الجانبية الأربعة** لينتهي عند الركن العلوي الواقع فوق نقطة البداية مباشرة. ما **أقصر** طول ممكن للشريط بوحدة {m('\\text{سم}')}؟",
            ans, [4 * s_col + h_col, math.isqrt((2 * s_col) ** 2 + h_col ** 2) if math.isqrt((2 * s_col) ** 2 + h_col ** 2) ** 2 == (2 * s_col) ** 2 + h_col ** 2 else ans - 3, ans + 2, 4 * s_col],
            f"Unfold all 4 vertical side faces side by side into one wide {m(f'{4 * s_col}\\text{{ cm}} \\times {h_col}\\text{{ cm}}')} rectangle!",
            f"افرد الأوجه الجانبية الأربعة بجانب بعضها في مستطيل واحد عرضه {m(f'{4 * s_col}\\text{{ سم}}')} وارتفاعه {m(f'{h_col}\\text{{ سم}}')}!",
            "Unrolling the 4 lateral faces forms a rectangle of width \\( 4s \\) and height \\( H \\); take its diagonal!",
            [
                f"Unfolding the four vertical faces side-by-side creates a flat rectangle of width {m(f'4 \\times {s_col} = {4 * s_col}\\text{{ cm}}')} and height {m(f'{h_col}\\text{{ cm}}')}.",
                f"The shortest wrap is the straight diagonal of this rectangle: {m(f'\\sqrt{{{4 * s_col}^2 + {h_col}^2}} = \\sqrt{{{(4*s_col)**2 + h_col**2}}} = {ans}\\text{{ cm}}')}.",
            ],
            f"{m(f'({4 * s_col})^2 + {h_col}^2 = {ans}^2')}.",
            "عند فرد الأوجه الجانبية الأربعة نحصل على مستطيل عرضه \\( 4s \\) وارتفاعه \\( H \\) وقطره هو أقصر شريط.",
            [
                f"عرض المستطيل المفرود = {m(f'4 \\times {s_col} = {4 * s_col}\\text{{ سم}}')} وارتفاعه {m(f'{h_col}\\text{{ سم}}')}.",
                f"أقصر طول للشريط هو القطر: {m(f'\\sqrt{{{4*s_col}^2 + {h_col}^2}} = {ans}\\text{{ سم}}')}.",
            ],
            f"تحقق: {m(f'{(4*s_col)**2} + {h_col**2} = {ans**2}')}.",
            diagram_en=svg_cube_net([(0, 1, str(s_col)), (1, 1, str(s_col)), (2, 1, str(s_col)), (3, 1, str(s_col)), (1, 0, f"H={h_col}"), (1, 2, "Base")]),
        ))
        idx += 1

    # 4. kang_cad_hidden_stack_surface (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_stacks = [(4, 2, 1), (3, 3, 1), (4, 3, 2), (2, 4, 1), (3, 1, 2)]
    for cols in easy_stacks:
        vox = {(i, 0, z) for i, h in enumerate(cols) for z in range(h)}
        ans = _voxel_surface_area(vox) - len(cols)  # exclude floor touches
        proj_check = len(cols) + 2 * sum(cols) + cols[0] + cols[-1] + sum(abs(cols[i] - cols[i + 1]) for i in range(len(cols) - 1))
        assert ans == proj_check
        col_s = ", ".join(str(x) for x in cols)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Easy", "kang_cad_hidden_stack_surface",
            f"Unit cubes ({m('1\\text{ cm}^3')}) are glued into three adjacent columns of heights {m(col_s)} standing flat on a table. All exposed faces **not touching the table** are painted silver. What is the painted area in {m('\\text{cm}^2')}?",
            f"أُلصقت مكعبات وحدوية ({m('1\\text{ سم}^3')}) لتكوين ثلاثة أعمدة متجاورة ارتفاعاتها {m(col_s)} موضوعة على طاولة. طُليت جميع الأوجه الظاهرة **غير الملامسة للطاولة** باللون الفضي. ما المساحة المطلية بوحدة {m('\\text{سم}^2')}؟",
            ans, [ans + len(cols), 6 * sum(cols) - ans, ans - 2, ans + 5],
            "Add Top + Front + Back + Left/Right/step vertical faces, leaving out the bottom squares on the table!",
            "اجمع الأوجه المرئية من الأعلى والأمام والخلف والجوانب دون احتساب المربعات السفلية الملامسة للطاولة!",
            "Sum visible faces across all five non-floor directions (watching any inner valley walls!).",
            [
                f"Top view contributes {m(len(cols))} unit squares; Front and Back contribute {m(f'2 \\times {sum(cols)} = {2 * sum(cols)}')} squares.",
                f"Left, Right, and vertical step walls contribute {m(ans - len(cols) - 2 * sum(cols))} squares.",
                f"Total silver area = {m(f'{ans}\\text{{ cm}}^2')}.",
            ],
            f"Full surface is {m(ans + len(cols))}, minus {m(len(cols))} bottom faces on the table = {m(ans)}.",
            "نحسب مجموع الأوجه المكشوفة باستثناء القاعدة الملامسة للطاولة.",
            [
                f"من الأعلى {m(len(cols))} مربعات، ومن الأمام والخلف {m(2 * sum(cols))} مربعاً.",
                f"وبإضافة الجدران الجانبية الرأسية يصبح إجمالي المساحة المطلية {m(f'{ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: المساحة الكلية {m(ans + len(cols))} مطروحاً منها {m(len(cols))} على الطاولة = {m(ans)}.",
            diagram_en=svg_cube_stack_3d(cols),
        ))
        idx += 1

    med_cuts = [
        (4, 5, 6, 1, 1, 1),
        (3, 4, 5, 2, 1, 1),
        (5, 5, 5, 1, 2, 1),
        (4, 6, 8, 1, 1, 2),
        (6, 6, 6, 2, 2, 2),
    ]
    for a, b, c, kx, ky, kz in med_cuts:
        orig_sa = 2 * (a * b + b * c + c * a)
        added_sa = 2 * (kx * b * c + ky * a * c + kz * a * b)
        ans = orig_sa + added_sa
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Medium", "kang_cad_hidden_stack_surface",
            f"A solid {m(f'{a}\\text{{ cm}} \\times {b}\\text{{ cm}} \\times {c}\\text{{ cm}}')} cheese block is sliced completely through by {m(kx)} cut(s) parallel to the {m(f'{b}\\times{c}')} face, {m(ky)} cut(s) parallel to the {m(f'{a}\\times{c}')} face, and {m(kz)} cut(s) parallel to the {m(f'{a}\\times{b}')} face. What is the **total surface area** of all resulting pieces combined (in {m('\\text{cm}^2')})?",
            f"قُطعت كتلة جبن مصمتة أبعادها {m(f'{a}\\text{{ سم}} \\times {b}\\text{{ سم}} \\times {c}\\text{{ سم}}')} بعدد {m(kx)} قطع موازٍ للوجه {m(f'{b}\\times{c}')}، و{m(ky)} قطع موازٍ للوجه {m(f'{a}\\times{c}')}، و{m(kz)} قطع موازٍ للوجه {m(f'{a}\\times{b}')}. ما **مجموع المساحات السطحية** لجميع القطع الناتجة معاً بوحدة {m('\\text{سم}^2')}؟",
            ans, [orig_sa + added_sa // 2, orig_sa, ans + 2 * a * b, ans - 2 * b * c],
            "Every flat slice parallel to a face of area \\( F \\) exposes **two** new faces of area \\( F \\)!",
            "كل عملية قطع مستوٍ موازية لوجه مساحته \\( F \\) تضيف **وجهين جديدين** مساحة كلٍّ منهما \\( F \\)!",
            "Add \\( 2 \\times (\\text{cross-section area}) \\) for each cut to the original surface area.",
            [
                f"Original surface area = {m(f'2({a}\\cdot{b} + {b}\\cdot{c} + {c}\\cdot{a}) = {orig_sa}\\text{{ cm}}^2')}.",
                f"The cuts add {m(f'2({kx}\\cdot{b*c} + {ky}\\cdot{a*c} + {kz}\\cdot{a*b}) = {added_sa}\\text{{ cm}}^2')} of fresh surface.",
                f"Combined surface area = {m(f'{orig_sa} + {added_sa} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"{m(f'{orig_sa} + {added_sa} = {ans}\\text{{ cm}}^2')}.",
            "نضيف ضعف مساحة المقطع لكل عملية قطع إلى المساحة السطحية الأصلية.",
            [
                f"المساحة السطحية الأصلية = {m(f'{orig_sa}\\text{{ سم}}^2')}.",
                f"القطوع تضيف مساحة جديدة قدرها {m(f'{added_sa}\\text{{ سم}}^2')}، فيصبح الإجمالي {m(f'{ans}\\text{{ سم}}^2')}.",
            ],
            f"تحقق: {m(f'{orig_sa} + {added_sa} = {ans}')}.",
            diagram_en=svg_painted_cube_3d(min(a, 5)),
        ))
        idx += 1

    hard_carve = [
        (4, 8, 0),   # 4x4x4 minus all 8 corners -> +0!
        (4, 0, 6),   # 4x4x4 minus 6 face-center cubes (at (1,1,0) etc.) -> +24!
        (5, 8, 6),   # 5x5x5 minus all 8 corners and all 6 face centers -> 150 + 24 = 174!
        (5, 4, 3),   # 5x5x5 minus 4 corners and 3 face centers -> 150 + 12 = 162!
        (6, 8, 6),   # 6x6x6 minus 8 corners and 6 face centers -> 216 + 24 = 240!
    ]
    for n_c, n_corners, n_fcenters in hard_carve:
        vox = {(x, y, z) for x in range(n_c) for y in range(n_c) for z in range(n_c)}
        all_corners = [(x, y, z) for x in (0, n_c - 1) for y in (0, n_c - 1) for z in (0, n_c - 1)]
        for pt in all_corners[:n_corners]:
            vox.remove(pt)
        m_c = n_c // 2 if n_c % 2 == 1 else 1
        face_centers = [
            (m_c, m_c, 0), (m_c, m_c, n_c - 1),
            (m_c, 0, m_c), (m_c, n_c - 1, m_c),
            (0, m_c, m_c), (n_c - 1, m_c, m_c),
        ]
        for pt in face_centers[:n_fcenters]:
            vox.remove(pt)
        ans = _voxel_surface_area(vox)
        assert ans == 6 * n_c * n_c + 4 * n_fcenters
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Geometry", "Hard", "kang_cad_hidden_stack_surface",
            f"From a solid {m(f'{n_c} \\times {n_c} \\times {n_c}')} cube made of unit cubes, **{m(n_corners)} corner unit cube(s)** and **{m(n_fcenters)} non-adjacent interior face unit cube(s)** (one from the interior of {m(n_fcenters)} outer face(s)) are plucked out. What is the total surface area of the remaining solid?",
            f"من مكعب مصمت أبعاده {m(f'{n_c} \\times {n_c} \\times {n_c}')} مكوّن من مكعبات وحدوية، نُزع **{m(n_corners)} من مكعبات الرؤوس** و**{m(n_fcenters)} من مكعبات قلب الأوجه غير المتجاورة**. ما المساحة السطحية الكلية للمجسم المتبقي؟",
            ans, [6 * n_c * n_c - 3 * n_corners - n_fcenters, 6 * n_c * n_c + 2 * n_corners + 4 * n_fcenters, 6 * n_c * n_c - n_fcenters, ans + 6],
            "Removing a **corner** cube swaps 3 outer faces for 3 inner faces (+0 change), while removing a **face-interior** cube swaps 1 outer face for 5 inner faces (+4 change)!",
            "نزع مكعب **زاوية** يستبدل 3 أوجه خارجية بـ 3 داخلية (تغيّر 0)، بينما نزع مكعب **وسط وجه** يستبدل وجهاً واحداً بـ 5 أوجه داخلية (+4)!",
            "Start with \\( 6n^2 \\), add \\( 0 \\) per removed corner cube, and add \\( +4 \\) per isolated face-interior pocket.",
            [
                f"Original {m(f'{n_c} \\times {n_c} \\times {n_c}')} cube has surface area {m(f'6 \\times {n_c}^2 = {6 * n_c * n_c}')}.",
                f"Each of the {m(n_corners)} removed corner cubes removes {m(3)} faces and reveals {m(3)} faces (net change {m(0)}).",
                f"Each of the {m(n_fcenters)} isolated face-interior pockets removes {m(1)} face and reveals {m(5)} faces (net change {m('+4')}), giving {m(f'{6 * n_c * n_c} + 4 \\times {n_fcenters} = {ans}')}.",
            ],
            f"Exact 3D face count = {m(ans)}.",
            "نبدأ بمساحة المكعب الكلي \\( 6n^2 \\)، ومكعبات الزوايا لا تغيّر المساحة بينما تضيف كل فجوة في وسط وجه \\( +4 \\).",
            [
                f"المساحة الأصلية للمكعب تساوي {m(f'6 \\times {n_c}^2 = {6 * n_c * n_c}')}.",
                f"نزع مكعبات الزوايا لا يغيّر المساحة ({m('+0')})، بينما تضيف كل فجوة من الـ {m(n_fcenters)} في وسط الأوجه {m('+4')} أوجه صافية.",
                f"المساحة النهائية = {m(f'{6 * n_c * n_c} + {4 * n_fcenters} = {ans}')}.",
            ],
            f"تحقق: {m(f'{6 * n_c * n_c} + {4 * n_fcenters} = {ans}')}.",
            diagram_en=svg_painted_cube_3d(min(n_c, 5)),
        ))
        idx += 1

    assert len(qs) == 60
    return qs


def _max_dominoes(cells: set[tuple[int, int]]) -> int:
    lefts = [c for c in sorted(cells) if (c[0] + c[1]) % 2 == 0]
    match_r: dict[tuple[int, int], tuple[int, int]] = {}

    def dfs(u: tuple[int, int], seen: set[tuple[int, int]]) -> bool:
        r, c = u
        for v in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if v in cells and v not in seen:
                seen.add(v)
                if v not in match_r or dfs(match_r[v], seen):
                    match_r[v] = u
                    return True
        return False

    ans = 0
    for u in lefts:
        if dfs(u, set()):
            ans += 1
    return ans


def _dp_grid_paths(cols: int, rows: int, blocked: set[tuple[int, int]]) -> int:
    dp = [[0] * (rows + 1) for _ in range(cols + 1)]
    if (0, 0) not in blocked:
        dp[0][0] = 1
    for x in range(cols + 1):
        for y in range(rows + 1):
            if (x, y) in blocked or (x == 0 and y == 0):
                continue
            dp[x][y] = (dp[x - 1][y] if x > 0 else 0) + (dp[x][y - 1] if y > 0 else 0)
    return dp[cols][rows]


def _unit_5() -> list[dict]:
    """Unit 5 (Lesson 3.5 — Combinatorics & Logic): QIDs 241..300."""
    qs: list[dict] = []
    idx = 241

    # 1. kang_cad_knights_liars_circle (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    for n_circ in (6, 8, 10, 12, 14):
        valid_ks = [
            sum(mask)
            for bits in range(1 << n_circ)
            for mask in [[(bits >> i) & 1 for i in range(n_circ)]]
            if all((mask[i] == 1 and mask[(i + 1) % n_circ] == 0) or (mask[i] == 0 and mask[(i + 1) % n_circ] == 1) for i in range(n_circ))
        ]
        assert set(valid_ks) == {n_circ // 2}
        ans = n_circ // 2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Easy", "kang_cad_knights_liars_circle",
            f"Around a circular table sit {m(n_circ)} islanders—each either a truth-telling **Knight** or an always-lying **Liar**. Every person points to their immediate right-hand neighbor and says: *\"That neighbor is a Liar.\"* How many Knights sit at the table?",
            f"يجلس حول طاولة دائرية {m(n_circ)} من سكان الجزيرة—كلٌّ منهم إما **فارس صادق** دائماً أو **كاذب** دائماً. أشار كل شخص إلى جاره المباشر على يمينه وقال: *«هذا الجار كاذب»*. كم فارساً صادقاً يجلس حول الطاولة؟",
            ans, [ans - 1, ans + 1, n_circ // 3, n_circ - 2],
            "If X is a Knight, X's right neighbor is a Liar; if X is a Liar, X's right neighbor must be a Knight!",
            "إذا كان المتحدث صادقاً فجاره الأيمن كاذب، وإذا كان كاذباً فجاره الأيمن صادق حتماً!",
            "Truth values must strictly alternate \\( K, L, K, L, \\dots \\) around the circle.",
            [
                "A Knight's right-hand neighbor must be a Liar, and a Liar's right-hand neighbor cannot be a Liar, so must be a Knight.",
                f"Thus Knights and Liars strictly alternate around all {m(n_circ)} seats.",
                f"Exactly half are Knights: {m(f'{n_circ} \\div 2 = {ans}')}.",
            ],
            f"Alternating {m('K, L')} repeated {m(ans)} times satisfies all {m(n_circ)} statements.",
            "يتناوب الصادقون والكاذبون بانتظام حول الطاولة الدائرية.",
            [
                "جار الصادق على يمينه كاذب، وجار الكاذب على يمينه صادق بالضرورة.",
                f"إذن يتناوبون مقعداً بمقعد، وعدد الصادقين يساوي النصف تماماً: {m(f'{n_circ} \\div 2 = {ans}')}.",
            ],
            f"تحقق: {m(ans)} صادقين و{m(ans)} كاذبين بالتناوب.",
            diagram_en=svg_kang_necklace_beads([str(i + 1) for i in range(min(n_circ, 12))]),
        ))
        idx += 1

    for n_circ in (6, 7, 9, 11, 13):
        valid_ks = [
            sum(mask)
            for bits in range(1 << n_circ)
            for mask in [[(bits >> i) & 1 for i in range(n_circ)]]
            if all(
                (mask[i] == 1 and mask[(i - 1) % n_circ] == 0 and mask[(i + 1) % n_circ] == 0)
                or (mask[i] == 0 and (mask[(i - 1) % n_circ] == 1 or mask[(i + 1) % n_circ] == 1))
                for i in range(n_circ)
            )
        ]
        ans = min(valid_ks)
        max_k = max(valid_ks)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Medium", "kang_cad_knights_liars_circle",
            f"Around a circular fountain stand {m(n_circ)} islanders (Knights and Liars). Every single islander announces: *\"Both of my immediate neighbors are Liars.\"* What is the **smallest** possible number of Knights standing around the fountain?",
            f"يقف حول نافورة دائرية {m(n_circ)} من الفرسان الصادقين والكاذبين. قال كل شخص منهم: *«جاراي المجاوران لي كلاهما كاذبان»*. ما **أصغر** عدد ممكن للفرسان الصادقين حول النافورة؟",
            ans, [ans - 1 if ans > 1 else ans + 3, max_k, ans + 1, ans + 2],
            "Three Liars in a row (L–L–L) is impossible because the middle Liar would be telling the truth! Pack as many K–L–L triples as possible.",
            "لا يمكن وجود ثلاثة كاذبين متتاليين (L–L–L) لأن الأوسط سيكون صادقاً! استخدم أكبر عدد ممكن من الثلاثيات K–L–L.",
            "Partition the circle into blocks of `K-L-L` (size 3) and `K-L` (size 2), maximizing size-3 blocks to minimize Knights.",
            [
                "No two Knights can be adjacent, and no three Liars can be consecutive (otherwise the middle Liar's neighbors would both be Liars!).",
                f"Every Knight can be followed clockwise by at most 2 Liars, so {m(f'3K \\ge {n_circ} \\implies K \\ge \\lceil {n_circ}/3 \\rceil = {ans}')}.",
                f"Tiling {m(n_circ)} seats with blocks of `KLL` and `KL` achieves {m(ans)} Knights.",
            ],
            f"Minimum valid Knight count on {m(n_circ)} seats is {m(ans)} (while maximum is {m(max_k)}).",
            "لا يجتمع ثلاثة كاذبين متجاورين أبداً، لذا يتبع كل صادق كاذبٌ أو كاذبان على الأكثر.",
            [
                f"بما أن كل صادق يغطي نفسه وكاذبَين على الأكثر، فإن {m(f'K \\ge \\lceil {n_circ}/3 \\rceil = {ans}')}.",
                f"يمكن تحقيق {m(ans)} صادقين بتقسيم الدائرة إلى مقاطع `KLL` و`KL`.",
            ],
            f"تحقق: أصغر عدد يحقق جميع العبارات هو {m(ans)}.",
            diagram_en=svg_kang_necklace_beads([str(i + 1) for i in range(min(n_circ, 12))]),
        ))
        idx += 1

    hard_kl = [
        (6, "diff"),
        (9, "diff"),
        (12, "diff"),
        (8, "at_least_one_L"),
        (10, "at_least_one_L"),
    ]
    for n_circ, rule in hard_kl:
        if rule == "diff":
            valid_ks = [
                sum(mask)
                for bits in range(1, 1 << n_circ)
                for mask in [[(bits >> i) & 1 for i in range(n_circ)]]
                if all(
                    (mask[i] == 1 and (mask[(i - 1) % n_circ] != mask[(i + 1) % n_circ]))
                    or (mask[i] == 0 and (mask[(i - 1) % n_circ] == mask[(i + 1) % n_circ]))
                    for i in range(n_circ)
                )
            ]
            ans = max(valid_ks)
            qs.append(make_kang_q(
                _qid(idx), LEVEL, "Combinatorics & Logic", "Hard", "kang_cad_knights_liars_circle",
                f"{m(n_circ)} islanders (Knights and Liars, with **at least one Knight** present) sit around a round table. Every person declares: *\"Exactly one of my two immediate neighbors is a Liar.\"* How many Knights sit at the table?",
                f"يجلس {m(n_circ)} من الفرسان الصادقين والكاذبين (مع وجود **فارس صادق واحد على الأقل**) حول طاولة مستديرة. يقول كل شخص: *«واحد فقط بالضبط من جاريّ المجاورين لي كاذب»*. كم فارساً صادقاً يجلس حول الطاولة؟",
                ans, [n_circ // 2, n_circ // 3, ans - 1, ans + 1],
                "Test the 3-person block `K–K–L`: check both Knights' neighbors and the Liar's neighbors!",
                "اختبر النمط الثلاثي المتكرر `K–K–L`: افحص جارَي كل صادق وجارَي الكاذب!",
                "With at least one Knight, the circle must repeat `K–K–L`, making exactly \\( \\frac{2}{3} \\) of the table Knights!",
                [
                    "Each Knight sits between one Knight and one Liar; each Liar must sit between two identical types.",
                    "Starting from any `K–L` pair forces `K–K–L–K–K–L...` in cycles of 3 around the table.",
                    f"Hence Knights occupy {m(f'\\frac{{2}}{{3}} \\times {n_circ} = {ans}')} seats.",
                ],
                f"Repeating `K, K, L` {m(n_circ // 3)} times gives {m(ans)} Knights and {m(n_circ // 3)} Liars.",
                "وجود صادق واحد يفرض تكرار الثلاثية `K–K–L` حول الطاولة بالكامل.",
                [
                    "كل صادق يجلس بين صادق وكاذب، وكل كاذب يجلس بين صادقين (`K–L–K`).",
                    f"يتكرر المقطع `K–K–L` عدد {m(n_circ // 3)} مرات، فيكون عدد الصادقين {m(ans)}.",
                ],
                f"تحقق: ثلثا المقاعد ({m(ans)}) للفرسان الصادقين.",
                diagram_en=svg_kang_necklace_beads([str(i + 1) for i in range(n_circ)]),
            ))
        else:
            valid_ks = [
                sum(mask)
                for bits in range(1 << n_circ)
                for mask in [[(bits >> i) & 1 for i in range(n_circ)]]
                if all(
                    (mask[i] == 1 and (mask[(i - 1) % n_circ] == 0 or mask[(i + 1) % n_circ] == 0))
                    or (mask[i] == 0 and (mask[(i - 1) % n_circ] == 1 and mask[(i + 1) % n_circ] == 1))
                    for i in range(n_circ)
                )
            ]
            ans = max(valid_ks)
            qs.append(make_kang_q(
                _qid(idx), LEVEL, "Combinatorics & Logic", "Hard", "kang_cad_knights_liars_circle",
                f"Around a circle of {m(n_circ)} chairs sit Knights and Liars. Every person states: *\"At least one of my two immediate neighbors is a Liar.\"* What is the **largest** possible number of Knights in the circle?",
                f"يجلس فرسان صادقون وكاذبون على {m(n_circ)} مقاعد مرتبة في دائرة. يقول كل شخص: *«واحد على الأقل من جاريّ المجاورين لي كاذب»*. ما **أكبر** عدد ممكن للفرسان الصادقين في الدائرة؟",
                ans, [n_circ // 2, ans - 1, ans + 1, n_circ - 2],
                "A Liar's false statement forces **both** neighbors to be Knights (`K–L–K`), while no three Knights can sit together (`K–K–K` is forbidden)!",
                "كذب الكاذب يفرض أن يكون **كلا جاريه صادقين** (`K–L–K`)، كما يمنع صدق الصادق جلوس 3 صادقين متتاليين (`K–K–K`)!",
                "Tile the circle with blocks `K–K–L` (size 3, 2 Knights) and `K–L` (size 2, 1 Knight) to maximize Knights.",
                [
                    "Every Liar must have two Knight neighbors (no `L–L`), and no Knight can sit between two Knights (no `K–K–K`).",
                    f"Partitioning {m(n_circ)} into as many `K–K–L` triples as possible plus `K–L` pairs yields a maximum of {m(ans)} Knights.",
                ],
                f"Maximum achievable Knights on {m(n_circ)} seats is {m(ans)}.",
                "نقسّم الدائرة إلى مقاطع `K–K–L` و`K–L` مع الإكثار من المقاطع الثلاثية لتعظيم عدد الصادقين.",
                [
                    "يُمنع تجاور كاذبين (`L–L`) ويُمنع توالي ثلاثة صادقين (`K–K–K`).",
                    f"بتقسيم الـ {m(n_circ)} مقاعد إلى مقاطع ثلاثية وثنائية نحصل على أكبر عدد للصادقين وهو {m(ans)}.",
                ],
                f"تحقق: التوزيع يحقق جميع العبارات بعدد {m(ans)} من الصادقين.",
                diagram_en=svg_kang_necklace_beads([str(i + 1) for i in range(n_circ)]),
            ))
        idx += 1

    # 2. kang_cad_domino_parity_hole (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_dom = [(4, 4), (4, 6), (6, 8), (8, 8), (4, 8)]
    for rows, cols in easy_dom:
        cells = {(r, c) for r in range(rows) for c in range(cols)} - {(0, 0), (rows - 1, cols - 1)}
        ans = _max_dominoes(cells)
        assert ans == (rows * cols) // 2 - 2
        board_vis = [[-1 if (r, c) in {(0, 0), (rows - 1, cols - 1)} else (r + c) % 2 for c in range(min(cols, 6))] for r in range(min(rows, 6))]
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Easy", "kang_cad_domino_parity_hole",
            f"Two **diagonally opposite corner squares** are removed from a {m(f'{rows} \\times {cols}')} checkerboard, leaving {m(rows * cols - 2)} unit squares. What is the **maximum** number of non-overlapping {m('1 \\times 2')} dominoes that can be placed on the remaining board?",
            f"أُزيل **مربعان من ركنين متقابلين قطرياً** في رقعة أبعادها {m(f'{rows} \\times {cols}')} فبقي {m(rows * cols - 2)} مربعاً صغيراً. ما **أكبر** عدد من قطع الدومينو {m('1 \\times 2')} غير المتداخلة التي يمكن وضعها على الرقعة المتبقية؟",
            ans, [ans + 1, ans + 2, ans - 1, ans - 2],
            f"Check the checkerboard colors of `(1,1)` and `({rows},{cols})`—both coordinate sums are even, so both removed corners have the **same color**!",
            f"افحص لونَي الركنين `(1,1)` و`({rows},{cols})`—كلاهما له مجموع إحداثيات زوجي أي من **نفس اللون**!",
            "Opposite corners on an even-by-even grid share the same color, reducing one color count by 2.",
            [
                f"Full {m(f'{rows} \\times {cols}')} board has {m(rows * cols // 2)} black and {m(rows * cols // 2)} white squares.",
                f"Removing two same-color corners leaves {m(ans)} squares of that color and {m(ans + 2)} of the other.",
                f"Each domino covers 1 black and 1 white square, capping the count at {m(ans)} (which is achievable!).",
            ],
            f"Max dominoes = {m(ans)} (not {m(ans + 1)}, the half-area trap!).",
            "الركنان المتقابلان في الرقعة الزوجية من نفس اللون، مما يُنقص أحد اللونين بمقدار 2.",
            [
                f"يتبقى {m(ans)} مربعاً من لون واحد و{m(ans + 2)} من اللون الآخر.",
                f"كل قطعة دومينو تغطي لونين مختلفين، لذا أقصى عدد ممكن ومتحقق هو {m(ans)}.",
            ],
            f"تحقق: {m(ans)} قطعة تغطي {m(2 * ans)} مربعاً.",
            diagram_en=svg_kang_polyomino_board(board_vis),
        ))
        idx += 1

    med_dom = [
        (5, 5, [(0, 1), (1, 0), (4, 3)]),   # 3 white cells removed from 5x5 (13B, 12W -> 13B, 9W -> 9 dominoes!)
        (5, 5, [(0, 0), (0, 2), (2, 0), (4, 4)]),  # 4 black cells removed (13B, 12W -> 9B, 12W -> 9 dominoes!)
        (4, 5, [(0, 0), (1, 1), (3, 3)]),   # 3 black cells removed from 4x5 (10B, 10W -> 7B, 10W -> 7 dominoes!)
        (6, 5, [(0, 0), (0, 4), (5, 1)]),   # 3 black cells removed from 6x5 (15B, 15W -> 12B, 15W -> 12 dominoes!)
        (5, 7, [(0, 1), (2, 1), (4, 5)]),   # 3 white cells removed from 5x7 (18B, 17W -> 18B, 14W -> 14 dominoes!)
    ]
    for rows, cols, holes in med_dom:
        hset = set(holes)
        cells = {(r, c) for r in range(rows) for c in range(cols)} - hset
        ans = _max_dominoes(cells)
        b_cnt = sum(1 for (r, c) in cells if (r + c) % 2 == 0)
        w_cnt = sum(1 for (r, c) in cells if (r + c) % 2 == 1)
        assert ans == min(b_cnt, w_cnt)
        board_vis = [[-1 if (r, c) in hset else (r + c) % 2 for c in range(cols)] for r in range(rows)]
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Medium", "kang_cad_domino_parity_hole",
            f"On the {m(f'{rows} \\times {cols}')} grid shown, the {m(len(holes))} dark blocked cells are unusable. What is the **maximum** number of non-overlapping {m('1 \\times 2')} dominoes that can be placed on the remaining {m(len(cells))} open cells?",
            f"على الشبكة {m(f'{rows} \\times {cols}')} الموضحة، الخلايا الداكنة البالغ عددها {m(len(holes))} محجوزة ولا يمكن استخدامها. ما **أكبر** عدد من قطع الدومينو {m('1 \\times 2')} غير المتداخلة التي يمكن وضعها على الخلايا المفتوحة الـ {m(len(cells))} المتبقية؟",
            ans, [len(cells) // 2, ans + 1, ans - 1, max(b_cnt, w_cnt)],
            "Color the grid like a chessboard and count how many Black cells and how many White cells remain!",
            "لوّن الشبكة كرقعة شطرنج واحسب عدد المربعات السوداء وعدد المربعات البيضاء المتبقية!",
            "Count remaining cells of each checkerboard color; \\( \\min(B, W) \\) bounds and equals the maximum tiling.",
            [
                f"Checkerboard coloring leaves {m(b_cnt)} cells of one color and {m(w_cnt)} cells of the opposite color.",
                f"Since each domino covers one cell of each color, at most {m(f'\\min({b_cnt}, {w_cnt}) = {ans}')} dominoes can fit, and an explicit placement achieves {m(ans)}.",
            ],
            f"Remaining open cells = {m(f'{b_cnt} + {w_cnt} = {len(cells)}')}, max dominoes = {m(ans)}.",
            "بالتلوين المتناوب نجد عدد خلايا كل لون، ويكون الحد الأقصى مساوياً للأقل عدداً بين اللونين.",
            [
                f"يتبقى في اللوحة {m(b_cnt)} خلية من اللون الأول و{m(w_cnt)} خلية من اللون الثاني.",
                f"أقصى عدد لقطع الدومينو هو {m(f'\\min({b_cnt}, {w_cnt}) = {ans}')} وهو متحقق فعلياً.",
            ],
            f"تحقق: {m(ans)} قطع تغطي جميع خلايا اللون الأقل.",
            diagram_en=svg_kang_polyomino_board(board_vis),
        ))
        idx += 1

    hard_walk = [(3, 5), (5, 5), (3, 7), (5, 7), (7, 7)]
    for rows, cols in hard_walk:
        tot = rows * cols
        w_cnt = tot // 2
        ans = 2 * w_cnt  # tot - 1!
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Hard", "kang_cad_domino_parity_hole",
            f"A {m(f'{rows} \\times {cols}')} board is colored like a chessboard with **black** corners ({m(tot - w_cnt)} black and {m(w_cnt)} white squares). A token starts on a **white** square and moves orthogonally (up, down, left, right) to adjacent squares without ever visiting any square twice. At most how many squares (including the start square) can the token visit?",
            f"لوحة أبعادها {m(f'{rows} \\times {cols}')} ملونة كرقعة شطرنج بحيث تكون زواياها الأربع **سوداء** ({m(tot - w_cnt)} مربعاً أسود و{m(w_cnt)} مربعاً أبيض). تبدأ قطعة من مربع **أبيض** وتنتقل أفقياً أو رأسياً بين المربعات المتجاورة دون زيارة أي مربع مرتين. ما **أكبر** عدد من المربعات (بما فيها مربع البداية) يمكن للقطعة زيارته؟",
            ans, [tot, ans - 1, ans - 2, w_cnt * 2 - 3],
            f"Starting on White forces the path colors to alternate `W, B, W, B, ...`—and there are only {m(w_cnt)} White squares on the whole board!",
            f"البدء بمربع أبيض يفرض تناوب الألوان `أبيض، أسود، أبيض، أسود...` ولا يوجد في اللوحة سوى {m(w_cnt)} مربعاً أبيض!",
            "A path starting on White has \\( \\lceil L/2 \\rceil \\) White squares, so \\( L \\) cannot exceed \\( 2W = RC - 1 \\).",
            [
                f"Every orthogonal step switches color: starting at White produces `W, B, W, B, ...`.",
                f"Visiting all {m(tot)} squares would require {m(tot - w_cnt)} White squares, impossible because only {m(w_cnt)} White squares exist!",
                f"With {m(w_cnt)} White squares, the longest alternating sequence is `W, B, ..., W, B` of length {m(f'2 \\times {w_cnt} = {ans}')}, achievable by snaking around one black corner.",
            ],
            f"{m(w_cnt)} White + {m(w_cnt)} Black = {m(ans)} visited squares (leaving 1 black corner unvisited).",
            "تناوب الألوان عند البدء بالأبيض يمنع تجاوز ضعف عدد المربعات البيضاء.",
            [
                f"بما أن المسار يبدأ بمربع أبيض ويتناوب لونياً، ولا يوجد سوى {m(w_cnt)} مربعاً أبيض، فأقصى طول هو `W, B, ..., W, B` بطول {m(f'2 \\times {w_cnt} = {ans}')}.",
                f"يمكن تحقيق {m(ans)} مربعاً فعلياً بمسار ثعباني يتخطى ركناً أسود واحداً.",
            ],
            f"تحقق: {m(f'2 \\times {w_cnt} = {ans}')} مربعاً.",
            diagram_en=svg_kang_grid_walk(min(cols, 5), min(rows, 5), [(1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)]),
        ))
        idx += 1

    # 3. kang_cad_blocked_grid_paths (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_gp = [
        (3, 3, (1, 2)),
        (4, 2, (2, 1)),
        (5, 2, (3, 1)),
        (3, 4, (1, 2)),
        (4, 4, (2, 2)),
    ]
    for cols, rows, blk in easy_gp:
        ans = _dp_grid_paths(cols, rows, {blk})
        tot = math.comb(cols + rows, rows)
        thru = math.comb(blk[0] + blk[1], blk[1]) * math.comb((cols - blk[0]) + (rows - blk[1]), rows - blk[1])
        assert ans == tot - thru
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Easy", "kang_cad_blocked_grid_paths",
            f"On a {m(f'{cols} \\times {rows}')} street grid, a walker travels from {m('A(0,0)')} to {m(f'B({cols},{rows})')} moving only East or North. Intersection {m(f'P({blk[0]},{blk[1]})')} is closed. How many shortest paths from {m('A')} to {m('B')} avoid {m('P')}?",
            f"على شبكة شوارع أبعادها {m(f'{cols} \\times {rows}')}، ينتقل شخص من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')} شرقاً أو شمالاً فقط. التقاطع {m(f'P({blk[0]},{blk[1]})')} مغلق. كم مساراً قصيراً من {m('A')} إلى {m('B')} يتجنب {m('P')}؟",
            ans, [tot, thru, ans + 3, max(1, ans - 3)],
            f"Subtract paths through {m(f'P({blk[0]},{blk[1]})')} from all {m(f'\\binom{{{cols+rows}}}{{{rows}}} = {tot}')} unrestricted paths.",
            f"اطرح عدد المسارات المارة بـ {m(f'P({blk[0]},{blk[1]})')} من إجمالي المسارات {m(tot)}.",
            "Use \\( \\binom{m+n}{n} - \\binom{x+y}{y}\\binom{m-x+n-y}{n-y} \\).",
            [
                f"Total shortest paths without closures = {m(f'\\binom{{{cols+rows}}}{{{rows}}} = {tot}')}.",
                f"Paths passing through {m(f'P({blk[0]},{blk[1]})')} = {m(f'\\binom{{{blk[0]+blk[1]}}}{{{blk[1]}}} \\times \\binom{{{cols-blk[0]+rows-blk[1]}}}{{{rows-blk[1]}}} = {thru}')}.",
                f"Valid paths = {m(f'{tot} - {thru} = {ans}')}.",
            ],
            f"{m(f'{ans} + {thru} = {tot}')}.",
            "نطرح المسارات المارة بالتقاطع المغلق من العدد الكلي للمسارات القصيرة.",
            [
                f"إجمالي المسارات دون إغلاق = {m(tot)}، والمسارات المارة بـ {m('P')} = {m(thru)}.",
                f"عدد المسارات المتاحة = {m(f'{tot} - {thru} = {ans}')}.",
            ],
            f"تحقق: {m(f'{tot} - {thru} = {ans}')}.",
            diagram_en=svg_street_grid(cols, rows, blocked=blk),
        ))
        idx += 1

    med_gp = [
        (4, 4, (2, 1), (3, 3)),
        (5, 3, (2, 1), (4, 2)),
        (4, 3, (1, 1), (3, 2)),
        (5, 4, (2, 2), (4, 3)),
        (6, 3, (3, 1), (5, 2)),
    ]
    for cols, rows, cp, blk in med_gp:
        # Must pass through `cp` AND avoid `blk` (where cp precedes blk!)
        leg1 = math.comb(cp[0] + cp[1], cp[1])
        leg2_tot = math.comb((cols - cp[0]) + (rows - cp[1]), rows - cp[1])
        leg2_blk = math.comb((blk[0] - cp[0]) + (blk[1] - cp[1]), blk[1] - cp[1]) * math.comb((cols - blk[0]) + (rows - blk[1]), rows - blk[1])
        ans = leg1 * (leg2_tot - leg2_blk)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Medium", "kang_cad_blocked_grid_paths",
            f"On a {m(f'{cols} \\times {rows}')} street grid from {m('A(0,0)')} to {m(f'B({cols},{rows})')} (moving only East or North), a runner **must stop at checkpoint** {m(f'C({cp[0]},{cp[1]})')} and **must avoid** closed intersection {m(f'P({blk[0]},{blk[1]})')}. How many shortest paths satisfy both rules?",
            f"على شبكة شوارع {m(f'{cols} \\times {rows}')} من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')} (شرقاً أو شمالاً فقط)، يجب على عدّاء **المرور بنقطة التفتيش** {m(f'C({cp[0]},{cp[1]})')} و**تجنب** التقاطع المغلق {m(f'P({blk[0]},{blk[1]})')}. كم مساراً قصيراً يحقق الشرطين معاً؟",
            ans, [leg1 * leg2_tot, ans + leg2_blk, ans - leg1, _dp_grid_paths(cols, rows, {blk})],
            f"Multiply ways from \\( A \\to C \\) ({m(leg1)}) by valid ways from \\( C \\to B \\) avoiding \\( P \\)!",
            f"اضرب عدد طرق الانتقال \\( A \\to C \\) ({m(leg1)}) في عدد طرق الانتقال من \\( C \\to B \\) مع تجنب \\( P \\)!",
            "Split the journey at checkpoint \\( C \\): count \\( A \\to C \\) times \\( (C \\to B \\text{ avoiding } P) \\).",
            [
                f"From {m('A(0,0)')} to {m(f'C({cp[0]},{cp[1]})')} there are {m(f'\\binom{{{cp[0]+cp[1]}}}{{{cp[1]}}} = {leg1}')} paths.",
                f"From {m(f'C({cp[0]},{cp[1]})')} to {m(f'B({cols},{rows})')} there are {m(leg2_tot)} total paths, of which {m(leg2_blk)} hit {m('P')}, leaving {m(leg2_tot - leg2_blk)} clear paths.",
                f"Multiply both stages: {m(f'{leg1} \\times {leg2_tot - leg2_blk} = {ans}')} paths.",
            ],
            f"{m(f'{leg1} \\times ({leg2_tot} - {leg2_blk}) = {ans}')}.",
            "نقسم الرحلة عند نقطة التفتيش C ونضرب خيارات المرحلتين.",
            [
                f"عدد المسارات من {m('A')} إلى {m('C')} يساوي {m(leg1)}.",
                f"ومن {m('C')} إلى {m('B')} دون المرور بـ {m('P')} يوجد {m(f'{leg2_tot} - {leg2_blk} = {leg2_tot - leg2_blk}')} مساراً.",
                f"حاصل الضرب = {m(f'{leg1} \\times {leg2_tot - leg2_blk} = {ans}')}.",
            ],
            f"تحقق: {m(f'{leg1} \\times {leg2_tot - leg2_blk} = {ans}')}.",
            diagram_en=svg_street_grid(cols, rows, blocked=blk),
        ))
        idx += 1

    hard_gp2 = [
        (4, 3, (1, 1), (3, 2)),
        (4, 4, (1, 1), (3, 3)),
        (5, 3, (2, 1), (4, 2)),
        (5, 4, (1, 2), (4, 3)),
        (6, 3, (2, 1), (4, 2)),
    ]
    for cols, rows, p1, p2 in hard_gp2:
        ans = _dp_grid_paths(cols, rows, {p1, p2})
        tot = math.comb(cols + rows, rows)
        n_p1 = math.comb(p1[0] + p1[1], p1[1]) * math.comb(cols - p1[0] + rows - p1[1], rows - p1[1])
        n_p2 = math.comb(p2[0] + p2[1], p2[1]) * math.comb(cols - p2[0] + rows - p2[1], rows - p2[1])
        n_both = (
            math.comb(p1[0] + p1[1], p1[1])
            * math.comb((p2[0] - p1[0]) + (p2[1] - p1[1]), p2[1] - p1[1])
            * math.comb((cols - p2[0]) + (rows - p2[1]), rows - p2[1])
        )
        assert ans == tot - n_p1 - n_p2 + n_both and n_both > 0
        trap_no_ie = tot - n_p1 - n_p2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Hard", "kang_cad_blocked_grid_paths",
            f"On a {m(f'{cols} \\times {rows}')} street grid, **both** intersections {m(f'P_1({p1[0]},{p1[1]})')} and {m(f'P_2({p2[0]},{p2[1]})')} are closed. Moving only East or North, how many shortest paths lead from {m('A(0,0)')} to {m(f'B({cols},{rows})')}?",
            f"على شبكة شوارع أبعادها {m(f'{cols} \\times {rows}')}، أُغلق التقاطعان {m(f'P_1({p1[0]},{p1[1]})')} و{m(f'P_2({p2[0]},{p2[1]})')} معاً. بالتحرك شرقاً أو شمالاً فقط، كم مساراً قصيراً يصل {m('A(0,0)')} بـ {m(f'B({cols},{rows})')}؟",
            ans, [trap_no_ie, ans + n_both, tot - n_p1, max(1, ans - 4)],
            "Remember Inclusion–Exclusion: paths passing through **both** \\( P_1 \\) and \\( P_2 \\) get subtracted twice, so add them back once!",
            "تذكّر مبدأ التضمين والإقصاء: المسارات المارة بـ \\( P_1 \\) و\\( P_2 \\) معاً طُرحت مرتين، لذا أعد جمعها مرة واحدة!",
            "Apply \\( \\text{Total} - N(P_1) - N(P_2) + N(P_1 \\text{ and } P_2) \\) (or fill intersection counts by DP).",
            [
                f"Unrestricted paths = {m(tot)}; paths through {m('P_1')} = {m(n_p1)}; paths through {m('P_2')} = {m(n_p2)}.",
                f"Paths hitting **both** {m('P_1')} and then {m('P_2')} equal {m(n_both)}.",
                f"By Inclusion–Exclusion: {m(f'{tot} - {n_p1} - {n_p2} + {n_both} = {ans}')}.",
            ],
            f"Grid DP confirms {m(ans)} paths (avoiding the double-subtraction trap {m(trap_no_ie)}!).",
            "نطبق التضمين والإقصاء بإعادة جمع المسارات المارة بالتقاطعين المغلقين معاً.",
            [
                f"الكل {m(tot)}، والمار بـ {m('P_1')} يساوي {m(n_p1)}، والمار بـ {m('P_2')} يساوي {m(n_p2)}، والمار بهما معاً {m(n_both)}.",
                f"عدد المسارات السليمة = {m(f'{tot} - {n_p1} - {n_p2} + {n_both} = {ans}')}.",
            ],
            f"تحقق بالبرمجة الديناميكية: {m(ans)} مساراً.",
            diagram_en=svg_street_grid(cols, rows, blocked=p1),
        ))
        idx += 1

    # 4. kang_cad_round_robin_points (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_rr = [
        (5, [7, 5, 4, 2]),
        (6, [9, 7, 6, 5, 1]),
        (7, [10, 9, 8, 6, 4, 3]),
        (8, [12, 11, 9, 8, 6, 5, 2]),
        (5, [6, 6, 4, 1]),
    ]
    for n_t, other_pts in easy_rr:
        tot_pts = n_t * (n_t - 1)  # 2 pts per match in chess (2, 1, 0)
        ans = tot_pts - sum(other_pts)
        pts_s = ", ".join(str(x) for x in other_pts)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Easy", "kang_cad_round_robin_points",
            f"In a {m(n_t)}-player Kangaroo chess tournament, each pair of players plays once (**2 points** for a win, **1 point each** for a draw, **0** for a loss). If {m(n_t - 1)} of the players finish with scores {m(pts_s)}, how many points did the remaining player score?",
            f"في بطولة شطرنج تضم {m(n_t)} لاعبين، يلعب كل لاعبين معاً مباراة واحدة (**نقطتان** للفوز، **نقطة لكل لاعب** عند التعادل، **0** للخسارة). إذا أنهى {m(n_t - 1)} لاعبين البطولة بالنقاط {m(pts_s)}، فكم نقطة جمع اللاعب المتبقي؟",
            ans, [ans + 2, max(0, ans - 1), ans + 1, tot_pts // 2 - ans if tot_pts // 2 > ans else ans + 3],
            f"In 2-1-0 chess scoring, **every game awards 2 total points**, so total points = \\( 2 \\times \\binom{{{n_t}}}{{2}} = {tot_pts} \\)!",
            f"في نظام الشطرنج (2-1-0) **تمنح كل مباراة نقطتين في المجموع** مهما كانت نتيجتها، فالمجموع الكلي = {m(tot_pts)}!",
            "Total points across all players is \\( 2\\binom{n}{2} = n(n-1) \\); subtract the known players' scores.",
            [
                f"There are {m(f'\\binom{{{n_t}}}{{2}} = {n_t * (n_t - 1) // 2}')} games, and every game adds {m(2)} points to the sum (either {m('2+0')} or {m('1+1')}).",
                f"Total points awarded = {m(tot_pts)}; subtracting {m(sum(other_pts))} leaves {m(f'{tot_pts} - {sum(other_pts)} = {ans}')}.",
            ],
            f"{m(f'{sum(other_pts)} + {ans} = {tot_pts}')}.",
            "كل مباراة شطرنج تضيف نقطتين للمجموع الكلي بغض النظر عن الفوز أو التعادل.",
            [
                f"إجمالي النقاط الموزعة في البطولة = {m(f'2 \\times \\binom{{{n_t}}}{{2}} = {tot_pts}')} نقطة.",
                f"نقاط اللاعب المتبقي = {m(f'{tot_pts} - {sum(other_pts)} = {ans}')}.",
            ],
            f"تحقق: {m(f'{sum(other_pts)} + {ans} = {tot_pts}')}.",
            diagram_en=svg_graph_cycle_chords(min(n_t, 8), full_kn=True),
        ))
        idx += 1

    med_rr = [(5, 4), (7, 8), (8, 9), (9, 11), (10, 14)]
    for n_t, draws_d in med_rr:
        m_cnt = n_t * (n_t - 1) // 2
        s_tot = 3 * m_cnt - draws_d
        ans = draws_d
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Medium", "kang_cad_round_robin_points",
            f"{m(n_t)} teams contest a single round-robin football league (each pair plays once; **3 points** for a win, **1 point each** for a draw, **0** for a loss). At season's end, the sum of all {m(n_t)} teams' points is {m(s_tot)}. How many matches ended in a **draw**?",
            f"تتنافس {m(n_t)} فرق في دوري كرة قدم من دور واحد (**3 نقاط** للفائز، **نقطة لكل فريق** عند التعادل، **0** للخاسر). في نهاية الموسم بلغ مجموع نقاط جميع الفرق {m(s_tot)} نقطة. كم مباراة انتهت **بالتعادل**؟",
            ans, [m_cnt - ans, ans + 3, max(1, ans - 2), (3 * m_cnt - s_tot) // 2 if ans >= 4 else ans + 5],
            f"Total matches = \\( \\binom{{{n_t}}}{{2}} = {m_cnt} \\); every draw lowers the league sum from \\( 3 \\times {m_cnt} = {3*m_cnt} \\) by 1 point.",
            f"عدد المباريات = {m(m_cnt)}؛ كل تعادل يُنقص المجموع الأقصى {m(3 * m_cnt)} بمقدار نقطة واحدة.",
            "Compute \\( D = 3\\binom{n}{2} - S \\).",
            [
                f"Total matches played = {m(f'\\binom{{{n_t}}}{{2}} = {m_cnt}')}; maximum possible points (0 draws) = {m(f'3 \\times {m_cnt} = {3 * m_cnt}')}.",
                f"Each draw awards {m('1+1=2')} points instead of {m(3)}, reducing the sum by {m(1)}.",
                f"Number of draws = {m(f'{3 * m_cnt} - {s_tot} = {ans}')}.",
            ],
            f"{m(m_cnt - ans)} wins ({m(3*(m_cnt-ans))} pts) + {m(ans)} draws ({m(2*ans)} pts) = {m(s_tot)} pts.",
            "نطرح مجموع النقاط الفعلي من حاصل ضرب 3 في إجمالي عدد المباريات.",
            [
                f"عدد المباريات الكلي {m(m_cnt)}، وأقصى مجموع ممكن بلا تعادلات هو {m(3 * m_cnt)}.",
                f"عدد التعادلات = {m(f'{3 * m_cnt} - {s_tot} = {ans}')} مباراة.",
            ],
            f"تحقق: {m(f'3({m_cnt - ans}) + 2({ans}) = {s_tot}')}.",
            diagram_en=svg_graph_cycle_chords(min(n_t, 8), full_kn=True),
        ))
        idx += 1

    hard_rr = [
        # Explicit realizable match tables: n teams, k draws, sum of first (n-1) teams -> find nth team's score!
        (5, 3, 24, 3),   # M=10, 3 draws -> tot = 27; top 4 sum = 24 -> 5th has 3 pts (e.g. 3 draws + 1 loss!)
        (6, 5, 36, 4),   # M=15, 5 draws -> tot = 40; top 5 sum = 36 -> 6th has 4 pts (1W, 1D, 3L)
        (7, 6, 52, 5),   # M=21, 6 draws -> tot = 57; top 6 sum = 52 -> 7th has 5 pts (1W, 2D, 3L)
        (8, 7, 71, 6),   # M=28, 7 draws -> tot = 77; top 7 sum = 71 -> 8th has 6 pts (2W, 0D, 5L)
        (6, 4, 39, 2),   # M=15, 4 draws -> tot = 41; top 5 sum = 39 -> 6th has 2 pts (0W, 2D, 3L)
    ]
    for n_t, k_dr, sum_others, ans in hard_rr:
        m_cnt = n_t * (n_t - 1) // 2
        tot_pts = 3 * m_cnt - k_dr
        assert tot_pts - sum_others == ans
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Combinatorics & Logic", "Hard", "kang_cad_round_robin_points",
            f"In an {m(n_t)}-club single round-robin football league (**3 points** win, **1 point each** draw, **0** loss), exactly **{m(k_dr)} matches** ended in a draw. If the first {m(n_t - 1)} clubs scored a combined total of **{m(sum_others)} points**, how many points did the {m(n_t)}th club score?",
            f"في دوري كرة قدم من دور واحد يضم {m(n_t)} أندية (**3 نقاط** للفوز، **نقطة لكل نادٍ** عند التعادل، **0** للخسارة)، انتهت **{m(k_dr)} مباريات بالضبط** بالتعادل. إذا جمع أول {m(n_t - 1)} أندية معاً **{m(sum_others)} نقطة**، فكم نقطة أحرز النادي الأخير؟",
            ans, [3 * m_cnt - sum_others, ans + k_dr, max(0, ans - 1), ans + 2],
            f"First compute total league points \\( 3\\binom{{{n_t}}}{{2}} - {k_dr} \\), then subtract {m(sum_others)}!",
            f"احسب أولاً إجمالي نقاط الدوري \\( 3\\binom{{{n_t}}}{{2}} - {k_dr} \\) ثم اطرح منه {m(sum_others)}!",
            "Combine \\( M = \\binom{n}{2} \\) and \\( S_{\\text{all}} = 3M - D \\) to isolate the final club's score.",
            [
                f"Total league matches = {m(f'\\binom{{{n_t}}}{{2}} = {m_cnt}')}.",
                f"With {m(k_dr)} draws and {m(m_cnt - k_dr)} decisive games, total points across all {m(n_t)} clubs is {m(f'3({m_cnt}) - {k_dr} = {tot_pts}')}.",
                f"Subtracting the first {m(n_t - 1)} clubs' sum gives {m(f'{tot_pts} - {sum_others} = {ans}')} points.",
            ],
            f"{m(f'{sum_others} + {ans} = {tot_pts} = 3({m_cnt - k_dr}) + 2({k_dr})')}.",
            "نستنتج مجموع النقاط الكلي للبطولة من عدد المباريات وعدد التعادلات ثم نطرح مجموع بقية الأندية.",
            [
                f"إجمالي المباريات {m(m_cnt)}، ومجموع النقاط الكلي للبطولة = {m(f'3 \\times {m_cnt} - {k_dr} = {tot_pts}')}.",
                f"رصيد النادي الأخير = {m(f'{tot_pts} - {sum_others} = {ans}')} نقاط.",
            ],
            f"تحقق: {m(f'{sum_others} + {ans} = {tot_pts}')}.",
            diagram_en=svg_graph_cycle_chords(n_t, full_kn=True),
        ))
        idx += 1

    assert len(qs) == 60
    return qs


def _unit_6() -> list[dict]:
    """Unit 6 (Lesson 3.6 — Data & Probability): QIDs 301..360."""
    qs: list[dict] = []
    idx = 301

    # 1. kang_cad_weighted_group_mean (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_wm = [
        (15, 76, 10, 86),
        (18, 70, 12, 85),
        (14, 90, 6, 70),
        (21, 68, 9, 88),
        (16, 92, 24, 77),
    ]
    for n1, m1, n2, m2 in easy_wm:
        tot_s = n1 * m1 + n2 * m2
        assert tot_s % (n1 + n2) == 0
        ans = tot_s // (n1 + n2)
        unw_trap = Fraction(m1 + m2, 2)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Easy", "kang_cad_weighted_group_mean",
            f"In a Cadet math contest, {m(n1)} students in Room A averaged {m(m1)} points and {m(n2)} students in Room B averaged {m(m2)} points. What is the mean score of all {m(n1 + n2)} students combined?",
            f"في اختبار رياضيات لمستوى كاديت، بلغ متوسط درجات {m(n1)} طالباً في القاعة (أ) {m(m1)} نقطة، ومتوسط درجات {m(n2)} طالباً في القاعة (ب) {m(m2)} نقطة. ما المتوسط الحسابي لجميع الـ {m(n1 + n2)} طالباً معاً؟",
            ans, [unw_trap, ans - 2, ans + 2, (n2 * m1 + n1 * m2) // (n1 + n2)],
            f"Compute total points \\( {n1}\\times{m1} + {n2}\\times{m2} \\), then divide by \\( {n1 + n2} \\).",
            f"احسب مجموع النقاط الكلي \\( {n1}\\times{m1} + {n2}\\times{m2} \\) ثم اقسم على \\( {n1 + n2} \\).",
            "Add the two rooms' point totals and divide by the combined student count.",
            [
                f"Room A total = {m(f'{n1} \\times {m1} = {n1 * m1}')}; Room B total = {m(f'{n2} \\times {m2} = {n2 * m2}')}.",
                f"Combined sum across {m(n1 + n2)} students = {m(tot_s)}.",
                f"Combined mean = {m(f'{tot_s} \\div {n1 + n2} = {ans}')}.",
            ],
            f"{m(f'({n1 * m1} + {n2 * m2}) / {n1 + n2} = {ans}')}.",
            "نجمع مجموعَي درجات القاعتين ونقسم على إجمالي عدد الطلاب.",
            [
                f"مجموع القاعة (أ) = {m(n1 * m1)} ومجموع القاعة (ب) = {m(n2 * m2)}.",
                f"المتوسط المشترك = {m(f'{tot_s} \\div {n1 + n2} = {ans}')}.",
            ],
            f"تحقق: {m(f'{tot_s} \\div {n1 + n2} = {ans}')}.",
            diagram_en=svg_bar_chart([(f"A ({n1})", m1, str(m1)), (f"B ({n2})", m2, str(m2)), ("All", ans, "?")], y_max=100),
        ))
        idx += 1

    med_wm = [
        (12, 78, 8, 82),
        (15, 84, 10, 80),
        (18, 75, 6, 78),
        (20, 88, 5, 86),
        (14, 72, 7, 76),
    ]
    for n1, m1, n2, m_all in med_wm:
        tot_all = (n1 + n2) * m_all
        rem_s = tot_all - n1 * m1
        assert rem_s % n2 == 0
        ans = rem_s // n2
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Medium", "kang_cad_weighted_group_mean",
            f"A group of {m(n1 + n2)} Cadets achieved an overall mean score of {m(m_all)}. If the first {m(n1)} Cadets had a mean score of {m(m1)}, what was the mean score of the remaining {m(n2)} Cadets?",
            f"حصلت مجموعة من {m(n1 + n2)} طالباً على متوسط كلي قدره {m(m_all)} نقطة. إذا كان متوسط أول {m(n1)} طالباً يساوي {m(m1)} نقطة، فما متوسط درجات الطلاب الـ {m(n2)} المتبقين؟",
            ans, [2 * m_all - m1, ans - 3, ans + 3, m_all],
            f"Subtract the first group's sum ({m(f'{n1}\\times{m1}')}) from the overall sum ({m(f'{n1+n2}\\times{m_all}')}), then divide by {m(n2)}.",
            f"اطرح مجموع المجموعة الأولى ({m(f'{n1}\\times{m1}')}) من المجموع الكلي ({m(f'{n1+n2}\\times{m_all}')}) ثم اقسم على {m(n2)}.",
            "Isolate the second subgroup's total sum from \\( S_{\\text{all}} - S_1 \\) and divide by \\( n_2 \\).",
            [
                f"Overall sum for {m(n1 + n2)} Cadets = {m(f'{n1 + n2} \\times {m_all} = {tot_all}')}.",
                f"First {m(n1)} Cadets' sum = {m(f'{n1} \\times {m1} = {n1 * m1}')}, leaving {m(f'{tot_all} - {n1 * m1} = {rem_s}')}.",
                f"Mean of the remaining {m(n2)} Cadets = {m(f'{rem_s} \\div {n2} = {ans}')}.",
            ],
            f"{m(f'{n1}\\times{m1} + {n2}\\times{ans} = {tot_all} = {n1+n2}\\times{m_all}')}.",
            "نطرح مجموع الفئة الأولى من المجموع الكلي ثم نقسم على عدد الفئة المتبقية.",
            [
                f"المجموع الكلي = {m(tot_all)}، ومجموع الفئة الأولى = {m(n1 * m1)}.",
                f"متوسط الفئة المتبقية = {m(f'({tot_all} - {n1 * m1}) \\div {n2} = {ans}')}.",
            ],
            f"تحقق: {m(f'{rem_s} \\div {n2} = {ans}')}.",
            diagram_en=svg_bar_chart([(f"G1 ({n1})", m1, str(m1)), (f"G2 ({n2})", ans, "?"), ("All", m_all, str(m_all))], y_max=100),
        ))
        idx += 1

    hard_range = [
        (9, 80, 78, 83),   # S=720; H = 720 - 8*78 = 96; L = 720 - 8*83 = 56 -> H-L = 40!
        (11, 75, 73, 78),  # S=825; H = 825 - 730 = 95; L = 825 - 780 = 45 -> H-L = 50!
        (8, 82, 80, 85),   # S=656; H = 656 - 560 = 96; L = 656 - 595 = 61 -> H-L = 35!
        (10, 79, 77, 82),  # S=790; H = 790 - 693 = 97; L = 790 - 738 = 52 -> H-L = 45!
        (7, 84, 82, 87),   # S=588; H = 588 - 492 = 96; L = 588 - 522 = 66 -> H-L = 30!
    ]
    for n_st, mu_orig, mu_no_hi, mu_no_lo in hard_range:
        s_orig = n_st * mu_orig
        hi_v = s_orig - (n_st - 1) * mu_no_hi
        lo_v = s_orig - (n_st - 1) * mu_no_lo
        assert 0 <= lo_v < mu_orig < hi_v <= 100
        ans = hi_v - lo_v
        assert ans == (n_st - 1) * (mu_no_lo - mu_no_hi)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Hard", "kang_cad_weighted_group_mean",
            f"A team of {m(n_st)} Cadets has a mean score of {m(mu_orig)}. Removing the **single highest** score lowers the remaining {m(n_st - 1)} Cadets' mean to {m(mu_no_hi)}, whereas removing the **single lowest** score instead raises the remaining {m(n_st - 1)} Cadets' mean to {m(mu_no_lo)}. What is the difference (**range**) between the highest and lowest scores?",
            f"فريق يضم {m(n_st)} طلاب متوسط درجاتهم {m(mu_orig)}. إذا استُبعدت **أعلى درجة** انخفض متوسط الـ {m(n_st - 1)} الباقين إلى {m(mu_no_hi)}، وإذا استُبعدت **أدنى درجة** بدلاً منها ارتفع متوسط الـ {m(n_st - 1)} الباقين إلى {m(mu_no_lo)}. ما الفرق (**المدى**) بين أعلى درجة وأدنى درجة؟",
            ans, [n_st * (mu_no_lo - mu_no_hi), hi_v, lo_v, ans - (mu_no_lo - mu_no_hi)],
            f"Notice \\( (S - L) - (S - H) = H - L = ({n_st - 1}) \\times ({mu_no_lo} - {mu_no_hi}) \\)!",
            f"لاحظ أن \\( (S - L) - (S - H) = H - L = ({n_st - 1}) \\times ({mu_no_lo} - {mu_no_hi}) \\)!",
            "Compare the two (n−1)-student sums directly: \\( H - L = (n-1)(\\mu_{\\text{no }L} - \\mu_{\\text{no }H}) \\).",
            [
                f"Without the highest score {m('H')}, the other {m(n_st - 1)} scores sum to {m(f'{n_st - 1} \\times {mu_no_hi} = {(n_st-1)*mu_no_hi}')} (so {m(f'H = {hi_v}')}).",
                f"Without the lowest score {m('L')}, the other {m(n_st - 1)} scores sum to {m(f'{n_st - 1} \\times {mu_no_lo} = {(n_st-1)*mu_no_lo}')} (so {m(f'L = {lo_v}')}).",
                f"Difference = {m(f'{hi_v} - {lo_v} = ({n_st - 1})({mu_no_lo} - {mu_no_hi}) = {ans}')}.",
            ],
            f"Highest = {m(hi_v)}, Lowest = {m(lo_v)}, Range = {m(ans)}.",
            "الفرق بين مجموعَي الـ (n−1) طالباً في الحالتين يساوي الفرق بين أعلى وأدنى درجة مباشرة.",
            [
                f"أعلى درجة {m(f'H = {s_orig} - {(n_st-1)*mu_no_hi} = {hi_v}')}، وأدنى درجة {m(f'L = {s_orig} - {(n_st-1)*mu_no_lo} = {lo_v}')}.",
                f"المدى المطلوب = {m(f'{hi_v} - {lo_v} = {ans}')}.",
            ],
            f"تحقق: {m(f'({n_st - 1})({mu_no_lo} - {mu_no_hi}) = {ans}')}.",
            diagram_en=svg_bar_chart([("All", mu_orig, str(mu_orig)), ("−High", mu_no_hi, str(mu_no_hi)), ("−Low", mu_no_lo, str(mu_no_lo))], y_max=100),
        ))
        idx += 1

    # 2. kang_cad_without_replacement_prob (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    easy_pr = [(4, 5), (6, 4), (5, 7), (3, 6), (6, 9)]
    for a_c, b_c in easy_pr:
        tot_n = a_c + b_c
        ans = Fraction(a_c * (a_c - 1), tot_n * (tot_n - 1))
        repl_trap = Fraction(a_c * a_c, tot_n * tot_n)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Easy", "kang_cad_without_replacement_prob",
            f"A box contains {m(a_c)} gold medals and {m(b_c)} silver medals. Two medals are drawn at random **without replacement**. What is the probability that **both** medals are **gold**?",
            f"يحتوي صندوق على {m(a_c)} ميداليات ذهبية و{m(b_c)} ميداليات فضية. سُحبت ميداليتان عشوائياً **دون إرجاع**. ما احتمال أن تكون الميداليتان **ذهبيتين معاً**؟",
            ans, [repl_trap, Fraction(a_c, tot_n), Fraction(a_c - 1, tot_n - 1), Fraction(2 * a_c, tot_n * (tot_n - 1))],
            f"Multiply \\( P(\\text{{1st gold}}) = \\frac{{{a_c}}}{{{tot_n}}} \\) by \\( P(\\text{{2nd gold}}) = \\frac{{{a_c - 1}}}{{{tot_n - 1}}} \\).",
            f"اضرب احتمال الأولى \\( \\frac{{{a_c}}}{{{tot_n}}} \\) في احتمال الثانية بعد النقصان \\( \\frac{{{a_c - 1}}}{{{tot_n - 1}}} \\).",
            "Reduce both the gold count and total count by 1 on the second draw.",
            [
                f"First draw is gold with probability {m(f'\\frac{{{a_c}}}{{{tot_n}}}')}.",
                f"Given the first was gold, {m(a_c - 1)} gold medals remain out of {m(tot_n - 1)} total medals.",
                f"Product = {m(f'\\frac{{{a_c}}}{{{tot_n}}} \\times \\frac{{{a_c - 1}}}{{{tot_n - 1}}} = {fmt_val(ans)}')}.",
            ],
            f"{m(f'\\binom{{{a_c}}}{{2}} / \\binom{{{tot_n}}}{{2}} = {fmt_val(ans)}')}.",
            "نضرب احتمال السحبة الأولى في احتمال السحبة الثانية مع إنقاص البسط والمقام بمقدار 1.",
            [
                f"احتمال الأولى ذهبية {m(f'\\frac{{{a_c}}}{{{tot_n}}}')}، واحتمال الثانية ذهبية {m(f'\\frac{{{a_c - 1}}}{{{tot_n - 1}}}')}.",
                f"حاصل الضرب المبسط = {m(fmt_val(ans))}.",
            ],
            f"تحقق بالتوافيق: {m(f'\\binom{{{a_c}}}{{2}} / \\binom{{{tot_n}}}{{2}} = {fmt_val(ans)}')}.",
            diagram_en=svg_pie_chart([(a_c / tot_n, f"{a_c} G"), (b_c / tot_n, f"{b_c} S")]),
        ))
        idx += 1

    med_pr = [(4, 3), (5, 4), (6, 3), (7, 3), (5, 6)]
    for a_c, b_c in med_pr:
        tot_n = a_c + b_c
        ans = Fraction(2 * a_c * b_c, tot_n * (tot_n - 1))
        half_trap = Fraction(a_c * b_c, tot_n * (tot_n - 1))
        repl_trap = Fraction(2 * a_c * b_c, tot_n * tot_n)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Medium", "kang_cad_without_replacement_prob",
            f"A jar holds {m(a_c)} blue marbles and {m(b_c)} yellow marbles. Two marbles are drawn one after another **without replacement**. What is the probability that the two marbles have **different colors**?",
            f"تحتوي جرة على {m(a_c)} كرات زرقاء و{m(b_c)} كرات صفراء. سُحبت كرتان الواحدة تلو الأخرى **دون إرجاع**. ما احتمال أن تكون الكرتان من **لونين مختلفين**؟",
            ans, [half_trap, repl_trap, 1 - ans, Fraction(a_c + b_c - 2, tot_n * (tot_n - 1))],
            "Count **both** orders: (Blue then Yellow) + (Yellow then Blue)!",
            "احسب **الترتيبين معاً**: (زرقاء ثم صفراء) + (صفراء ثم زرقاء)!",
            "Add \\( \\frac{a}{N}\\cdot\\frac{b}{N-1} + \\frac{b}{N}\\cdot\\frac{a}{N-1} = \\frac{2ab}{N(N-1)} \\).",
            [
                f"Blue then Yellow has probability {m(f'\\frac{{{a_c}}}{{{tot_n}}} \\times \\frac{{{b_c}}}{{{tot_n - 1}}}')}.",
                f"Yellow then Blue also has probability {m(f'\\frac{{{b_c}}}{{{tot_n}}} \\times \\frac{{{a_c}}}{{{tot_n - 1}}}')}.",
                f"Adding both orders gives {m(f'\\frac{{{2 * a_c * b_c}}}{{{tot_n * (tot_n - 1)}}} = {fmt_val(ans)}')}.",
            ],
            f"{m(f'({a_c} \\times {b_c}) / \\binom{{{tot_n}}}{{2}} = {fmt_val(ans)}')}.",
            "نجمع احتمالَي الترتيبين الممكنين لاختلاف اللونين.",
            [
                f"احتمال (زرقاء ثم صفراء) يساوي احتمال (صفراء ثم زرقاء) ويساوي {m(f'\\frac{{{a_c * b_c}}}{{{tot_n * (tot_n - 1)}}}')}.",
                f"بجمعهما نحصل على {m(fmt_val(ans))}.",
            ],
            f"تحقق: {m(f'\\frac{{2 \\times {a_c} \\times {b_c}}}{{{tot_n} \\times {tot_n - 1}}} = {fmt_val(ans)}')}.",
            diagram_en=svg_spinner([(a_c / tot_n, f"{a_c} B"), (b_c / tot_n, f"{b_c} Y")]),
        ))
        idx += 1

    hard_pr3 = [(2, 3, 4), (3, 3, 4), (2, 4, 4), (3, 4, 5), (2, 3, 5)]
    for r_c, g_c, b_c in hard_pr3:
        tot_n = r_c + g_c + b_c
        ans = Fraction(2 * (r_c * g_c + g_c * b_c + b_c * r_c), tot_n * (tot_n - 1))
        same_p = Fraction(r_c * (r_c - 1) + g_c * (g_c - 1) + b_c * (b_c - 1), tot_n * (tot_n - 1))
        assert ans + same_p == 1
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Hard", "kang_cad_without_replacement_prob",
            f"A pouch holds {m(r_c)} red, {m(g_c)} green, and {m(b_c)} blue counters. Two counters are drawn simultaneously at random. What is the probability that the two counters have **different colors**?",
            f"يحتوي كيس على {m(r_c)} أقراص حمراء و{m(g_c)} خضراء و{m(b_c)} زرقاء. سُحب قرصان معاً عشوائياً. ما احتمال أن يكون القرصان من **لونين مختلفين**؟",
            ans, [same_p, ans / 2, Fraction(r_c * g_c + g_c * b_c + b_c * r_c, tot_n * tot_n), 1 - same_p / 2 if same_p / 2 < 1 else Fraction(1, 2)],
            f"Count mixed pairs \\( rg + gb + br \\) divided by \\( \\binom{{{tot_n}}}{{2}} \\) (or use \\( 1 - P(\\text{{same color}}) \\))!",
            f"اقسم عدد الأزواج المختلطة \\( rg + gb + br \\) على \\( \\binom{{{tot_n}}}{{2}} \\) (أو احسب \\( 1 - P(\\text{{نفس اللون}}) \\))!",
            "Divide heterogeneous pairs \\( rg + gb + br \\) by \\( \\binom{N}{2} \\).",
            [
                f"Total unordered pairs of counters = {m(f'\\binom{{{tot_n}}}{{2}} = {tot_n * (tot_n - 1) // 2}')}.",
                f"Mixed-color pairs = {m(f'{r_c}\\cdot{g_c} + {g_c}\\cdot{b_c} + {b_c}\\cdot{r_c} = {r_c*g_c + g_c*b_c + b_c*r_c}')}.",
                f"Probability = {m(f'\\frac{{{r_c*g_c + g_c*b_c + b_c*r_c}}}{{{tot_n*(tot_n-1)//2}}} = {fmt_val(ans)}')}.",
            ],
            f"Complement check: same-color pairs = {m(fmt_val(same_p))}, and {m(f'1 - {fmt_val(same_p)} = {fmt_val(ans)}')}.",
            "نقسم عدد الأزواج ذات الألوان المختلفة على إجمالي الأزواج الممكنة.",
            [
                f"إجمالي الأزواج = {m(tot_n * (tot_n - 1) // 2)}، والأزواج المختلطة = {m(r_c*g_c + g_c*b_c + b_c*r_c)}.",
                f"الاحتمال المطلوب بعد التبسيط = {m(fmt_val(ans))}.",
            ],
            f"تحقق بالمتمم: {m(f'1 - {fmt_val(same_p)} = {fmt_val(ans)}')}.",
            diagram_en=svg_pie_chart([(r_c / tot_n, f"{r_c} R"), (g_c / tot_n, f"{g_c} G"), (b_c / tot_n, f"{b_c} B")]),
        ))
        idx += 1

    # 3. kang_cad_three_set_venn (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    venn_regions_easy = [
        (10, 9, 8, 5, 4, 3, 4),
        (12, 11, 7, 6, 5, 4, 3),
        (8, 10, 9, 4, 6, 5, 5),
        (14, 9, 11, 5, 3, 6, 2),
        (9, 13, 8, 7, 4, 5, 6),
    ]
    for a_o, b_o, c_o, ab_o, bc_o, ac_o, x_3 in venn_regions_easy:
        A = a_o + ab_o + ac_o + x_3
        B = b_o + ab_o + bc_o + x_3
        C = c_o + ac_o + bc_o + x_3
        AB, BC, AC = ab_o + x_3, bc_o + x_3, ac_o + x_3
        ans = a_o + b_o + c_o + ab_o + bc_o + ac_o + x_3
        assert ans == A + B + C - AB - BC - AC + x_3
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Easy", "kang_cad_three_set_venn",
            f"In a survey, {m(A)} students speak Arabic, {m(B)} speak English, and {m(C)} speak French. Exactly {m(AB)} speak Arabic and English, {m(BC)} speak English and French, {m(AC)} speak Arabic and French, and {m(x_3)} speak **all three** languages. How many students speak **at least one** of the three languages?",
            f"في استبيان مدرسي، يتحدث {m(A)} طالباً العربية و{m(B)} الإنجليزية و{m(C)} الفرنسية. يتحدث {m(AB)} العربية والإنجليزية معاً، و{m(BC)} الإنجليزية والفرنسية معاً، و{m(AC)} العربية والفرنسية معاً، ويتحدث {m(x_3)} **اللغات الثلاث جميعاً**. كم طالباً يتحدث **واحدة على الأقل** من هذه اللغات الثلاث؟",
            ans, [ans - x_3, ans - 2 * x_3, ans + x_3, A + B + C - AB - BC],
            "Use Inclusion–Exclusion: \\( |A| + |B| + |C| - |AB| - |BC| - |AC| + |ABC| \\).",
            "استخدم التضمين والإقصاء: اجمع المجموعات الفردية واطرح التقاطعات الثنائية ثم أضف التقاطع الثلاثي.",
            "Sum the three totals, subtract the three pairwise overlaps, and add back the center overlap.",
            [
                f"Single totals sum to {m(f'{A} + {B} + {C} = {A + B + C}')}; pairwise overlaps sum to {m(f'{AB} + {BC} + {AC} = {AB + BC + AC}')}.",
                f"By Inclusion–Exclusion: {m(f'{A + B + C} - {AB + BC + AC} + {x_3} = {ans}')}.",
            ],
            f"7 disjoint regions sum: {m(f'{a_o}+{b_o}+{c_o}+{ab_o}+{bc_o}+{ac_o}+{x_3} = {ans}')}.",
            "نجمع الأعداد الثلاثة ونطرح التقاطعات الثنائية ثم نعيد إضافة التقاطع الثلاثي الأوسط.",
            [
                f"مجموع المجموعات {m(A + B + C)} ومجموع التقاطعات الثنائية {m(AB + BC + AC)}.",
                f"إجمالي الاتحاد = {m(f'{A + B + C} - {AB + BC + AC} + {x_3} = {ans}')}.",
            ],
            f"تحقق بالمناطق السبع: المجموع يساوي {m(ans)}.",
            diagram_en=svg_venn_3(f"A({A})", f"E({B})", f"F({C})", {"a": "?", "b": "?", "c": "?", "ab": str(ab_o), "bc": str(bc_o), "ac": str(ac_o), "abc": str(x_3)}),
        ))
        idx += 1

    venn_med = [
        (7, 8, 6, 4, 3, 5, 4, 5),
        (9, 7, 8, 5, 4, 3, 6, 4),
        (10, 9, 7, 3, 5, 4, 7, 3),
        (8, 11, 6, 4, 6, 2, 5, 6),
        (11, 8, 9, 5, 3, 4, 8, 2),
    ]
    for a_o, b_o, c_o, ab_o, bc_o, ac_o, x_3, none_n in venn_med:
        A = a_o + ab_o + ac_o + x_3
        B = b_o + ab_o + bc_o + x_3
        C = c_o + ac_o + bc_o + x_3
        AB, BC, AC = ab_o + x_3, bc_o + x_3, ac_o + x_3
        union_n = a_o + b_o + c_o + ab_o + bc_o + ac_o + x_3
        U_tot = union_n + none_n
        ans = x_3
        assert ans == union_n - (A + B + C) + (AB + BC + AC)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Medium", "kang_cad_three_set_venn",
            f"Out of {m(U_tot)} Cadets, {m(none_n)} joined **none** of the three science labs (Physics, Coding, Astronomy). Overall, {m(A)} joined Physics, {m(B)} joined Coding, {m(C)} joined Astronomy, {m(AB)} joined Physics & Coding, {m(BC)} joined Coding & Astronomy, and {m(AC)} joined Physics & Astronomy. How many Cadets joined **all three** labs?",
            f"من أصل {m(U_tot)} طالباً، لم يلتحق {m(none_n)} طلاب **بأي** من المختبرات العلمية الثلاثة (الفيزياء، البرمجة، الفلك). التحق {m(A)} بالفيزياء، و{m(B)} بالبرمجة، و{m(C)} بالفلك، و{m(AB)} بالفيزياء والبرمجة معاً، و{m(BC)} بالبرمجة والفلك معاً، و{m(AC)} بالفيزياء والفلك معاً. كم طالباً التحق **بالمختبرات الثلاثة جميعاً**؟",
            ans, [ans + none_n, max(1, ans - 2), ans + 3, AB - 1],
            f"First find \\( |P \\cup C \\cup A| = {U_tot} - {none_n} = {union_n} \\), then solve Inclusion–Exclusion for \\( x \\)!",
            f"أوجد أولاً اتحاد المجموعات الثلاث \\( {U_tot} - {none_n} = {union_n} \\) ثم حلّ معادلة التضمين والإقصاء لإيجاد \\( x \\)!",
            "Set \\( U - \\text{none} = (|P|+|C|+|A|) - (|PC|+|CA|+|PA|) + x \\) and solve for \\( x \\).",
            [
                f"Students in at least one lab = {m(f'{U_tot} - {none_n} = {union_n}')}.",
                f"Apply Inclusion–Exclusion: {m(f'{union_n} = ({A}+{B}+{C}) - ({AB}+{BC}+{AC}) + x = {A+B+C - (AB+BC+AC)} + x')}.",
                f"Solve for {m('x')}: {m(f'x = {union_n} - {A+B+C - (AB+BC+AC)} = {ans}')}.",
            ],
            f"Center overlap {m(ans)} makes all 7 Venn regions non-negative and sum to {m(union_n)}.",
            "نحسب عدد المنضمين لمختبر واحد على الأقل ثم نعوض في قانون التضمين والإقصاء لإيجاد المركز.",
            [
                f"عدد الملتحقين بمختبر واحد على الأقل = {m(f'{U_tot} - {none_n} = {union_n}')}.",
                f"من قانون التضمين والإقصاء: {m(f'{union_n} = {A+B+C} - {AB+BC+AC} + x')}، ومنه {m(f'x = {ans}')}.",
            ],
            f"تحقق: {m(f'{A+B+C - (AB+BC+AC)} + {ans} = {union_n}')}.",
            diagram_en=svg_venn_3(f"P({A})", f"C({B})", f"A({C})", {"a": "", "b": "", "c": "", "ab": "", "bc": "", "ac": "", "abc": "x"}),
        ))
        idx += 1

    venn_hard = [
        (11, 9, 10, 4, 5, 3, 4),
        (13, 8, 12, 5, 4, 6, 3),
        (9, 14, 11, 6, 3, 5, 5),
        (15, 10, 8, 4, 6, 3, 2),
        (12, 11, 13, 5, 5, 4, 6),
    ]
    for a_o, b_o, c_o, ab_o, bc_o, ac_o, x_3 in venn_hard:
        A = a_o + ab_o + ac_o + x_3
        B = b_o + ab_o + bc_o + x_3
        C = c_o + ac_o + bc_o + x_3
        AB, BC, AC = ab_o + x_3, bc_o + x_3, ac_o + x_3
        ans = a_o + b_o + c_o
        assert ans == (A + B + C) - 2 * (AB + BC + AC) + 3 * x_3
        union_trap = a_o + b_o + c_o + ab_o + bc_o + ac_o + x_3
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Hard", "kang_cad_three_set_venn",
            f"At a Kangaroo summer camp, {m(A)} students take Art, {m(B)} take Music, and {m(C)} take Drama. Exactly {m(AB)} take Art & Music, {m(BC)} take Music & Drama, {m(AC)} take Art & Drama, and {m(x_3)} take **all three**. How many students take **exactly ONE** of these three classes?",
            f"في معسكر صيفي، يدرس {m(A)} طالباً الفنون و{m(B)} الموسيقى و{m(C)} المسرح. يدرس {m(AB)} الفنون والموسيقى معاً، و{m(BC)} الموسيقى والمسرح معاً، و{m(AC)} الفنون والمسرح معاً، ويدرس {m(x_3)} **المواد الثلاث جميعاً**. كم طالباً يدرس **مادة واحدة فقط بالضبط** من هذه المواد الثلاث؟",
            ans, [union_trap, ans - 2 * x_3, ab_o + bc_o + ac_o, ans + x_3],
            "Peel from the center outward: find the 3 'two-only' petals first, then each 'one-only' outer region!",
            "قشّر المخطط من المركز للخارج: أوجد مناطق المادتين فقط أولاً، ثم مناطق المادة الواحدة فقط!",
            "Peel center \\( x \\) from each pair to get two-only counts, then find \\( a_{\\text{only}} + b_{\\text{only}} + c_{\\text{only}} \\).",
            [
                f"Two-class-only regions: Art & Music only = {m(f'{AB}-{x_3}={ab_o}')}, Music & Drama only = {m(f'{BC}-{x_3}={bc_o}')}, Art & Drama only = {m(f'{AC}-{x_3}={ac_o}')}.",
                f"Single-class-only regions: Art only = {m(f'{A}-({ab_o}+{ac_o}+{x_3})={a_o}')}, Music only = {m(b_o)}, Drama only = {m(c_o)}.",
                f"Students taking **exactly one** class = {m(f'{a_o} + {b_o} + {c_o} = {ans}')}.",
            ],
            f"Formula check: {m(f'({A}+{B}+{C}) - 2({AB}+{BC}+{AC}) + 3({x_3}) = {ans}')}.",
            "نبدأ بالتقاطع الثلاثي فنطرحه من التقاطعات الثنائية ثم نستخرج مناطق المادة الواحدة فقط.",
            [
                f"مناطق المادتين فقط هي {m(ab_o)} و{m(bc_o)} و{m(ac_o)}.",
                f"مناطق المادة الواحدة فقط هي {m(a_o)} و{m(b_o)} و{m(c_o)}، ومجموعها = {m(ans)} طالباً.",
            ],
            f"تحقق: {m(f'{a_o} + {b_o} + {c_o} = {ans}')}.",
            diagram_en=svg_venn_3(f"Art({A})", f"Mus({B})", f"Dra({C})", {"a": "?", "b": "?", "c": "?", "ab": str(ab_o), "bc": str(bc_o), "ac": str(ac_o), "abc": str(x_3)}),
        ))
        idx += 1

    # 4. kang_cad_binary_bulb_switches (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    weights = (16, 8, 4, 2, 1)
    easy_bin = [
        ((1, 0, 1, 0, 0), 27),  # 20=(1,0,1,0,0) -> 27=(1,1,0,1,1) -> diff at 8,4,2,1 = 4 flips
        ((0, 1, 1, 0, 1), 22),  # 13=(0,1,1,0,1) -> 22=(1,0,1,1,0) -> diff at 16,8,2,1 = 4 -> let's vary answers!
        ((1, 1, 0, 0, 1), 29),  # 25=(1,1,0,0,1) -> 29=(1,1,1,0,1) -> 1 flip!
        ((0, 1, 0, 1, 1), 26),  # 11=(0,1,0,1,1) -> 26=(1,1,0,1,0) -> 2 flips!
        ((1, 0, 0, 1, 0), 13),  # 18=(1,0,0,1,0) -> 13=(0,1,1,0,1) -> 5 flips!
    ]
    # Replace 2nd tuple so all 5 answers are {4, 3, 1, 2, 5}!
    easy_bin[1] = ((0, 1, 1, 0, 1), 19)  # 13=(0,1,1,0,1) -> 19=(1,0,0,1,1): diff at 16,8,4,2? 4 flips; try 21=(1,0,1,0,1): diff at 16,8 = 2; try 28=(1,1,1,0,0): diff at 16,1 = 2; try 18=(1,0,0,1,0): 5; try 15=(0,1,1,1,1): 1; try 23=(1,0,1,1,1): diff at 16,8,2 = 3 flips!
    easy_bin[1] = ((0, 1, 1, 0, 1), 23)
    for init_b, target_v in easy_bin:
        targ_b = tuple((target_v >> (4 - i)) & 1 for i in range(5))
        ans = sum(1 for x, y in zip(init_b, targ_b) if x != y)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Easy", "kang_cad_binary_bulb_switches",
            f"A binary display has 5 bulbs with weights {m('16, 8, 4, 2, 1')} currently set as shown. What is the **exact number of bulbs** whose state (ON/OFF) must be flipped so that the lit bulbs sum to **{m(target_v)}**?",
            f"لوحة ثنائية تضم 5 مصابيح أوزانها {m('16, 8, 4, 2, 1')} وتظهر بحالتها الحالية في الشكل. كم مصباحاً بالضبط يجب **عكس حالته** (مضاء/مطفأ) ليصبح مجموع أوزان المصابيح المضاءة **{m(target_v)}**؟",
            ans, [sum(targ_b), (ans % 5) + 1, max(0, ans - 2), min(5, ans + 2)],
            f"Write {m(target_v)} as a sum of powers of 2 from {{16, 8, 4, 2, 1}} and count where the bits differ!",
            f"اكتب العدد {m(target_v)} كمجموع لقوى العدد 2 من {{16, 8, 4, 2, 1}} واحسب عدد المواضع المختلفة!",
            "Find the unique binary pattern for the target sum and count mismatched positions (Hamming distance).",
            [
                f"Target {m(target_v)} has unique binary representation {m(str(targ_b))} on weights {m('(16, 8, 4, 2, 1)')}.",
                f"Comparing {m(str(init_b))} with {m(str(targ_b))} shows {m(ans)} bulb(s) must change state.",
            ],
            f"Target bits {m(str(targ_b))} sum to {m(sum(w * b for w, b in zip(weights, targ_b)))}.",
            "نحدد التمثيل الثنائي الوحيد للعدد المطلوب ونحسب عدد المصابيح المختلفة عن الحالة الابتدائية.",
            [
                f"تمثيل العدد {m(target_v)} على الأوزان {m('(16, 8, 4, 2, 1)')} هو {m(str(targ_b))}.",
                f"بمقارنته بالحالة الحالية {m(str(init_b))} نجد أننا نحتاج لعكس {m(ans)} مصابيح.",
            ],
            f"تحقق: التمثيل الجديد مجموعه {m(target_v)}.",
            diagram_en=svg_binary_bulbs(init_b, weights),
        ))
        idx += 1

    med_bin = [
        ((1, 1, 0, 1, 0), [(0, 1, 2), (2, 3, 4)], "Button L (leftmost 3) then Button R (rightmost 3)", "الزر الأيسر (أول 3 يساراً) ثم الزر الأيمن (آخر 3 يميناً)"),
        ((0, 1, 1, 0, 1), [(0, 1, 2), (1, 2, 3)], "Button L (leftmost 3) then Button M (middle 3)", "الزر الأيسر (أول 3 يساراً) ثم الزر الأوسط (الـ 3 الوسطى)"),
        ((1, 0, 0, 1, 1), [(1, 2, 3), (2, 3, 4)], "Button M (middle 3) then Button R (rightmost 3)", "الزر الأوسط (الـ 3 الوسطى) ثم الزر الأيمن (آخر 3 يميناً)"),
        ((1, 1, 1, 0, 0), [(0, 1, 2), (1, 2, 3), (2, 3, 4)], "all three buttons L, M, and R once each", "الأزرار الثلاثة L وM وR مرة واحدة لكلٍّ منها"),
        ((0, 0, 1, 1, 1), [(0, 1, 2), (1, 2, 3), (2, 3, 4)], "all three buttons L, M, and R once each", "الأزرار الثلاثة L وM وR مرة واحدة لكلٍّ منها"),
    ]
    for init_b, btn_masks, desc_en, desc_ar in med_bin:
        cur = list(init_b)
        for msk in btn_masks:
            for pos in msk:
                cur[pos] ^= 1
        ans = sum(w * b for w, b in zip(weights, cur))
        init_sum = sum(w * b for w, b in zip(weights, init_b))
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Medium", "kang_cad_binary_bulb_switches",
            f"The 5-bulb panel ({m('16, 8, 4, 2, 1')}) starts in state {m(str(init_b))} as shown ({m('1=\\text{ON},\\;0=\\text{OFF}')}). Button L flips the leftmost 3 bulbs, Button M flips the middle 3 bulbs, and Button R flips the rightmost 3 bulbs. After pressing **{desc_en}**, what is the sum of the weights of all **ON** bulbs?",
            f"تبدأ لوحة المصابيح الخمسة ({m('16, 8, 4, 2, 1')}) بالحالة {m(str(init_b))} كما في الشكل. يعكس الزر L أول 3 مصابيح يساراً، ويعكس الزر M المصابيح الـ 3 الوسطى، ويعكس الزر R آخر 3 مصابيح يميناً. بعد الضغط على **{desc_ar}**، ما مجموع أوزان المصابيح **المضاءة**؟",
            ans, [31 - ans, init_sum, (ans + 8) % 32, max(1, ans - 4)],
            "Count how many times each of the 5 positions gets toggled—even toggles leave a bulb unchanged, odd toggles flip it!",
            "احسب عدد مرات تبديل كل مصباح؛ العدد الزوجي يبقيه كما كان والفردي يعكس حالته!",
            "Use toggle parity at each position, then sum the weights of the final ON bulbs.",
            [
                f"Initial state is {m(str(init_b))} (initial sum {m(init_sum)}).",
                f"Applying the button toggles by parity produces final state {m(str(tuple(cur)))}.",
                f"Summing the lit weights gives {m(ans)}.",
            ],
            f"Final bits {m(str(tuple(cur)))} evaluate to {m(ans)}.",
            "نحدد تكافؤ عدد التبديلات لكل مصباح ثم نجمع أوزان المصابيح المضاءة في النهاية.",
            [
                f"الحالة الابتدائية {m(str(init_b))} تتحول بعد التبديلات إلى {m(str(tuple(cur)))}.",
                f"مجموع أوزان المصابيح المضاءة يصبح {m(ans)}.",
            ],
            f"تحقق: {m(str(tuple(cur)))} تعطي {m(ans)}.",
            diagram_en=svg_binary_bulbs(init_b, weights),
        ))
        idx += 1

    for n_lockers in (50, 85, 130):
        bulbs = [0] * (n_lockers + 1)
        for pass_k in range(1, n_lockers + 1):
            for mult in range(pass_k, n_lockers + 1, pass_k):
                bulbs[mult] ^= 1
        ans = sum(bulbs[1:])
        assert ans == math.isqrt(n_lockers)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Hard", "kang_cad_binary_bulb_switches",
            f"In a Kangaroo corridor, {m(n_lockers)} bulbs numbered {m(f'1, 2, \\dots, {n_lockers}')} are all initially **OFF**. On Pass 1, every bulb is flipped; on Pass 2, every multiple of 2 is flipped; on Pass 3, every multiple of 3 is flipped; and so on up to Pass {m(n_lockers)}. How many bulbs remain **ON** after all {m(n_lockers)} passes?",
            f"في ممر مسابقة الكانجارو يوجد {m(n_lockers)} مصباحاً مرقمة من {m(1)} إلى {m(n_lockers)} وجميعها **مطفأة** في البداية. في الجولة 1 عُكست حالة كل مصباح، وفي الجولة 2 عُكست مضاعفات 2، وفي الجولة 3 مضاعفات 3، وهكذا حتى الجولة {m(n_lockers)}. كم مصباحاً يبقى **مضاءً** في النهاية؟",
            ans, [ans - 1, ans + 1, n_lockers // 2, n_lockers - ans],
            "Bulb \\( k \\) is flipped once for each positive divisor of \\( k \\)—which numbers have an **odd** number of divisors?",
            "يُعكس المصباح رقم \\( k \\) بعدد قواسمه الموجبة—ما الأعداد التي تمتلك عدداً **فردياً** من القواسم؟",
            "Only **perfect squares** have an odd number of divisors, so exactly \\( \\lfloor \\sqrt{N} \\rfloor \\) bulbs stay ON!",
            [
                "Bulb \\( k \\) is toggled on Pass \\( d \\) if and only if \\( d \\) divides \\( k \\).",
                "Divisors pair up as \\( (d, k/d) \\) unless \\( k = m^2 \\) is a **perfect square**, giving it an odd number of toggles.",
                f"Perfect squares in {m(f'1..{n_lockers}')} are {m(f'1^2, 2^2, \\dots, {ans}^2 = {ans*ans}')}, so {m(ans)} bulbs remain ON.",
            ],
            f"{m(f'{ans}^2 = {ans*ans} \\le {n_lockers} < {(ans+1)**2} = {ans+1}^2')}.",
            "المربعات الكاملة وحدها لها عدد فردي من القواسم فتبقى مضاءة.",
            [
                "يُبدَّل المصباح رقم \\( k \\) مرة واحدة لكل قاسم موجب من قواسمه.",
                f"الأعداد ذات العدد الفردي من القواسم هي المربعات الكاملة من {m('1^2')} حتى {m(f'{ans}^2 = {ans*ans}')}، وعددها {m(ans)}.",
            ],
            f"تحقق: {m(f'\\lfloor \\sqrt{{{n_lockers}}} \\rfloor = {ans}')}.",
            diagram_en=svg_binary_bulbs((1, 0, 0, 1, 0), (1, 2, 3, 4, 5)),
        ))
        idx += 1

    adj_puzzles = [
        (0, 0, 1, 0, 0),  # S1(0,1) + S5(3,4) -> 2 presses
        (0, 1, 0, 1, 0),  # S1(0,1) + S3(1,2,3) + S5(3,4) -> 3 presses
    ]
    sw_masks = [(0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4)]
    for init_b in adj_puzzles:
        valid_presses = []
        for mask_p in range(32):
            cur = list(init_b)
            cnt_p = 0
            for s_i in range(5):
                if (mask_p >> s_i) & 1:
                    cnt_p += 1
                    for pos in sw_masks[s_i]:
                        cur[pos] ^= 1
            if cur == [1, 1, 1, 1, 1]:
                valid_presses.append(cnt_p)
        assert valid_presses, f"Unreachable all-ON from {init_b}"
        ans = min(valid_presses)
        qs.append(make_kang_q(
            _qid(idx), LEVEL, "Data & Probability", "Hard", "kang_cad_binary_bulb_switches",
            f"Five bulbs sit in a row in initial state {m(str(init_b))} as shown ({m('1=\\text{ON},\\;0=\\text{OFF}')}). Pressing switch {m('i')} ({m('1 \\le i \\le 5')}) flips bulb {m('i')} **and** its immediate neighbor(s) (so switch 1 flips bulbs 1 & 2, switch 3 flips 2, 3 & 4, and switch 5 flips 4 & 5). What is the **minimum** number of switch presses needed to turn **all 5 bulbs ON**?",
            f"خمسة مصابيح في صف واحد تبدأ بالحالة {m(str(init_b))} كما في الشكل. الضغط على المفتاح رقم {m('i')} يعكس حالة المصباح {m('i')} **وجيرانه المباشرين** (المفتاح 1 يعكس 1 و2، والمفتاح 3 يعكس 2 و3 و4، والمفتاح 5 يعكس 4 و5). ما **أقل** عدد من الضغطات يلزم لإضاءة **المصابيح الخمسة جميعاً**؟",
            ans, [ans + 1, ans + 2, max(1, ans - 1), 5],
            "Decide whether Switch 1 is pressed (only 2 choices!)—that immediately locks in Switch 2, then Switch 3, 4, and 5 from left to right!",
            "ابدأ بتحديد ما إذا كان المفتاح 1 سيُضغط أم لا (خياران فقط!)، فهذا يحدد تلقائياً بقية المفاتيح من اليسار إلى اليمين!",
            "Sweep from left to right: once Switch 1 is chosen, each subsequent switch is uniquely forced to make the bulb to its left ON.",
            [
                f"Starting from {m(str(init_b))}, Bulb 1 is affected **only** by Switch 1 and Switch 2.",
                "Testing the two possibilities for Switch 1 (pressed vs. unpressed) uniquely determines Switches 2, 3, 4, and 5 from left to right.",
                f"Checking the valid solution(s) gives a minimum of {m(ans)} switch presses.",
            ],
            f"Verified across all {m('2^5 = 32')} switch subsets: minimum presses = {m(ans)}.",
            "نمسح اللوحة من اليسار إلى اليمين؛ اختيار حالة المفتاح الأول يحدد بقية المفاتيح تباعاً.",
            [
                f"انطلاقاً من الحالة {m(str(init_b))}، نختبر خيارَي المفتاح الأول فنحصل بشكل وحيد على بقية المفاتيح.",
                f"أقل عدد من الضغطات يجعل جميع المصابيح الخمسة مضاءة هو {m(ans)}.",
            ],
            f"تحقق شامل لجميع التشكيلات الـ 32: الحد الأدنى هو {m(ans)}.",
            diagram_en=svg_binary_bulbs(init_b, (1, 2, 3, 4, 5)),
        ))
        idx += 1

    assert len(qs) == 60
    return qs


def build_cadet_bank() -> list[dict]:
    """Build and return all 360 Kangaroo Cadet (Grades 7–8) MCQ questions."""
    bank = _unit_1() + _unit_2() + _unit_3() + _unit_4() + _unit_5() + _unit_6()
    assert len(bank) == 360, f"Expected 360 Cadet questions, got {len(bank)}"
    return bank
