"""NSMO (Mawhiba) Phase 2: Intermediate Olympiad (Grades 8-9) Question Bank — 450 Programmatically Verified Questions."""
import math
from fractions import Fraction
from nsmo_common import (
    NSMO_LEVELS,
    explain_ar,
    explain_en,
    load_other_track_stems,
    m,
    make_4_bilingual_options,
    make_4_math_options,
    make_nsmo_question,
    norm_text,
    svg_area_identity_square,
    svg_binary_bulbs,
    svg_coord_diamond,
    svg_digit_slots,
    svg_digital_clock,
    svg_equilateral_corner_cuts,
    svg_factor_tree,
    svg_graph_cycle_chords,
    svg_isosceles_trapezoid,
    svg_midpoint_square_shaded,
    svg_motion_timeline,
    svg_number_strip,
    svg_parabola_roots,
    svg_parallel_similar_tri,
    svg_regular_polygon,
    svg_round_table,
    svg_street_grid,
    svg_subdivided_apex_triangle,
    svg_subdivided_rect_2x2,
    svg_thales_circle,
    svg_trapezoid_semicircle,
    svg_two_jars,
    svg_venn_2,
    svg_venn_3,
)

LEVEL = NSMO_LEVELS[1]  # "Phase 2: Intermediate Olympiad (Grades 8-9)"


def _vp_fact(n: int, p: int) -> int:
    s = 0
    while n > 0:
        n //= p
        s += n
    return s


def _divisors(n: int) -> list[int]:
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


class BankBuilder:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add_math(
        self,
        topic: str,
        difficulty: str,
        blueprint: str,
        q_en: str,
        q_ar: str,
        correct_val,
        distractors: list,
        hint_en: str,
        hint_ar: str,
        idea_en: str,
        steps_en: list[str],
        check_en: str,
        idea_ar: str,
        steps_ar: list[str],
        check_ar: str,
        suffix: str = "",
        diagram_en: str = None,
        diagram_ar: str = None,
    ) -> None:
        qid = f"NSMO-G89-{len(self.items) + 1:03d}"
        opts_en, opts_ar, cidx, cans = make_4_math_options(correct_val, distractors, qid, suffix=suffix)
        self.items.append(
            make_nsmo_question(
                qid,
                LEVEL,
                topic,
                difficulty,
                blueprint,
                q_en,
                q_ar,
                opts_en,
                opts_ar,
                cidx,
                cans,
                hint_en,
                hint_ar,
                explain_en(idea_en, steps_en, check_en),
                explain_ar(idea_ar, steps_ar, check_ar),
                diagram_en=diagram_en,
                diagram_ar=diagram_ar,
            )
        )


# =============================================================================
# UNIT 2.1 — Modular Arithmetic, CRT & Factorial Zeros (75 Qs)
# =============================================================================
def _add_unit_2_1(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. nsmo_g89_crt_simultaneous_mod (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g89_crt_simultaneous_mod"
    easy_crt = [
        (4, 3, 7, 5, "robotics kits"),
        (5, 4, 8, 3, "astronomy booklets"),
        (6, 5, 7, 2, "chess medals"),
        (5, 2, 9, 7, "laboratory vials"),
        (7, 4, 9, 5, "camp badges"),
    ]
    for m1, r1, m2, r2, item_en in easy_crt:
        ans = next(x for x in range(1, m1 * m2 + 1) if x % m1 == r1 and x % m2 == r2)
        seq = [r2 + k * m2 for k in range(4)]
        B.add_math(
            tp, "Easy", bp,
            f"A crate of {item_en} contains the smallest positive number {m('N')} of items that leaves remainder {m(r1)} when packed into boxes of {m(m1)} and remainder {m(r2)} when packed into boxes of {m(m2)}. Find {m('N')}.",
            f"يحتوي صندوق على أصغر عدد موجب {m('N')} من القطع بحيث يترك باقياً قدره {m(r1)} عند توزيعه في علب تسع {m(m1)} قطع، وباقياً قدره {m(r2)} عند توزيعه في علب تسع {m(m2)} قطع. أوجد {m('N')}.",
            ans, [ans + m1, ans + m2, m1 * m2 - ans, ans - m1 if ans > m1 else ans + m1 * m2],
            f"List numbers of the form {m(f'{r2} + {m2}k')} and test which one leaves remainder {m(r1)} modulo {m(m1)}.",
            f"اسرد الأعداد من الصورة {m(f'{r2} + {m2}k')} واختبر أول عدد يعطي الباقي {m(r1)} عند قسمته على {m(m1)}.",
            f"Step through candidates congruent to {m(r2)} modulo the larger divisor {m(m2)}!",
            [
                f"Positive integers leaving remainder {m(r2)} modulo {m(m2)} are {m(', '.join(str(v) for v in seq))}, ...",
                f"Test each modulo {m(m1)} until remainder {m(r1)} appears: {m(f'{ans} = {ans // m1} \\times {m1} + {r1}')}.",
                f"Since {m(f'\\gcd({m1}, {m2}) = 1')}, {m(f'N = {ans}')} is the unique solution in {m(f'1 \\le N \\le {m1*m2}')}.",
            ],
            f"Check: {m(f'{ans} \\bmod {m1} = {r1}')} and {m(f'{ans} \\bmod {m2} = {r2}')}.",
            f"نقفز بمقدار المقسوم الأكبر {m(m2)} بدءاً من {m(r2)} حتى يتحقق شرط القسمة على {m(m1)}!",
            [
                f"الأعداد التي تترك الباقي {m(r2)} على {m(m2)} هي: {m(', '.join(str(v) for v in seq))}، ...",
                f"نفحص بواقيها على {m(m1)} فنجد {m(f'{ans} = {ans // m1} \\times {m1} + {r1}')}.",
                f"إذن أصغر عدد موجب يحقق الشرطين معاً هو {m(ans)}.",
            ],
            f"تحقق: باقي قسمة {m(ans)} على {m(m1)} هو {m(r1)}، وعلى {m(m2)} هو {m(r2)}.",
            diagram_en=svg_number_strip([f"÷{m1}→{r1}", f"÷{m2}→{r2}", f"+{m1*m2}k", "N = ?"]),
        )

    med_crt = [
        (5, 3, 9, 4, "min3"),
        (6, 1, 11, 8, "min3"),
        (7, 5, 8, 3, "min3"),
        (5, 2, 11, 7, "max3"),
        (7, 3, 9, 6, "max3"),
        (8, 5, 9, 2, "max3"),
    ]
    for m1, r1, m2, r2, mode in med_crt:
        L = math.lcm(m1, m2)
        n0 = next(x for x in range(1, L + 1) if x % m1 == r1 and x % m2 == r2)
        cands = [x for x in range(100, 1000) if x % m1 == r1 and x % m2 == r2]
        ans = cands[0] if mode == "min3" else cands[-1]
        adj_en = "**smallest** three-digit" if mode == "min3" else "**largest** three-digit"
        adj_ar = "**أصغر** عدد من ثلاث خانات" if mode == "min3" else "**أكبر** عدد من ثلاث خانات"
        B.add_math(
            tp, "Medium", bp,
            f"Find the {adj_en} positive integer {m('N')} such that {m(f'N \\equiv {r1} \\pmod{{{m1}}}')} and {m(f'N \\equiv {r2} \\pmod{{{m2}}}')}.",
            f"أوجد {adj_ar} {m('N')} يحقق {m(f'N \\equiv {r1} \\pmod{{{m1}}}')} و{m(f'N \\equiv {r2} \\pmod{{{m2}}}')}.",
            ans, [ans - L if ans - L >= 100 else ans + L, ans + L if ans + L <= 999 else ans - 2 * L, n0 + 100, ans + m2],
            f"First find the base solution {m(f'N_0 = {n0}')}, then add multiples of {m(f'\\operatorname{{lcm}}({m1}, {m2}) = {L}')}.",
            f"أوجد أولاً الحل الأساسي {m(f'N_0 = {n0}')} ثم أضف مضاعفات {m(f'\\operatorname{{lcm}}({m1}, {m2}) = {L}')}.",
            f"Combine both congruences into a single progression {m(f'N = {n0} + {L}k')}!",
            [
                f"Stepping by {m(m2)} from {m(r2)} gives the smallest positive solution {m(f'N_0 = {n0}')}.",
                f"Since {m(f'\\operatorname{{lcm}}({m1}, {m2}) = {L}')}, all solutions have the form {m(f'N = {n0} + {L}k')}.",
                f"Choosing {m(f'k = {(ans - n0)//L}')} yields the required three-digit value {m(f'N = {ans}')}.",
            ],
            f"Verify: {m(f'100 \\le {ans} \\le 999')}, {m(f'{ans} \\bmod {m1} = {r1}')}, and {m(f'{ans} \\bmod {m2} = {r2}')}.",
            f"ندمج الشرطين في متتالية حسابية خطوتها {m(f'\\operatorname{{lcm}}({m1}, {m2}) = {L}')}!",
            [
                f"أصغر حل موجب للنظام هو {m(f'N_0 = {n0}')}.",
                f"جميع الحلول تُكتب بالصورة {m(f'N = {n0} + {L}k')}.",
                f"عند {m(f'k = {(ans - n0)//L}')} نحصل على العدد الثلاثي المطلوب {m(f'N = {ans}')}.",
            ],
            f"تحقق: {m(ans)} مكون من ثلاث خانات ويحقق الباقيين {m(r1)} و{m(r2)} معاً.",
            diagram_en=svg_number_strip([str(n0), f"+{L}k", "100..999", "N = ?"]),
        )

    hard_crt = [
        (3, 2, 5, 3, 7, 4),
        (3, 1, 4, 3, 7, 5),
        (4, 1, 5, 4, 7, 2),
        (3, 2, 5, 1, 8, 5),
    ]
    for m1, r1, m2, r2, m3, r3 in hard_crt:
        L12 = m1 * m2
        n12 = next(x for x in range(1, L12 + 1) if x % m1 == r1 and x % m2 == r2)
        L123 = L12 * m3
        ans = next(x for x in range(1, L123 + 1) if x % m1 == r1 and x % m2 == r2 and x % m3 == r3)
        B.add_math(
            tp, "Hard", bp,
            f"What is the smallest positive integer {m('N')} satisfying the three simultaneous congruences {m(f'N \\equiv {r1} \\pmod{{{m1}}}')}, {m(f'N \\equiv {r2} \\pmod{{{m2}}}')}, and {m(f'N \\equiv {r3} \\pmod{{{m3}}}')}?",
            f"ما أصغر عدد صحيح موجب {m('N')} يحقق التطابقات الثلاثة المتزامنة {m(f'N \\equiv {r1} \\pmod{{{m1}}}')} و{m(f'N \\equiv {r2} \\pmod{{{m2}}}')} و{m(f'N \\equiv {r3} \\pmod{{{m3}}}')}؟",
            ans, [ans + L12, n12 + m3, L123 - ans, ans + m2 * m3],
            f"Merge the first two moduli into {m(f'N \\equiv {n12} \\pmod{{{L12}}}')}, then step by {m(L12)} to match modulo {m(m3)}.",
            f"ادمج التطابقين الأولين في {m(f'N \\equiv {n12} \\pmod{{{L12}}}')} ثم اقفز بمقدار {m(L12)} لتحقيق التطابق الثالث.",
            f"Solve two moduli first, then step by {m(f'{m1} \\times {m2} = {L12}')} against {m(m3)}!",
            [
                f"From {m(f'N \\equiv {r1} \\pmod{{{m1}}}')} and {m(f'N \\equiv {r2} \\pmod{{{m2}}}')}, we get {m(f'N \\equiv {n12} \\pmod{{{L12}}}')}.",
                f"Test terms {m(f'{n12}, {n12 + L12}, {n12 + 2*L12}, \\dots')} modulo {m(m3)}.",
                f"The first term leaving remainder {m(r3)} modulo {m(m3)} is {m(f'N = {ans}')}.",
            ],
            f"Triple check: {m(f'{ans} \\bmod {m1} = {r1}')}, {m(f'{ans} \\bmod {m2} = {r2}')}, and {m(f'{ans} \\bmod {m3} = {r3}')}.",
            f"نحل أول تطابقين معاً فنحصل على باقٍ وحيد للمقاس {m(L12)} ثم نختبر مضاعفاته مع {m(m3)}!",
            [
                f"دمج الشرطين الأولين يعطي {m(f'N \\equiv {n12} \\pmod{{{L12}}}')}.",
                f"نختبر حدود المتتالية {m(f'{n12} + {L12}t')} عند القسمة على {m(m3)}.",
                f"أول حد يعطي الباقي {m(r3)} على {m(m3)} هو {m(f'N = {ans}')}.",
            ],
            f"تحقق ثلاثي: {m(ans)} يحقق البواقي {m(r1)} و{m(r2)} و{m(r3)} جميعاً.",
            diagram_en=svg_number_strip([f"mod {m1}={r1}", f"mod {m2}={r2}", f"mod {m3}={r3}", "N = ?"]),
        )

    # 2. nsmo_g89_trailing_zeros_factorial (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g89_trailing_zeros_factorial"
    for n in (45, 65, 85, 110, 140):
        ans = _vp_fact(n, 5)
        q5, q25, q125 = n // 5, n // 25, n // 125
        B.add_math(
            tp, "Easy", bp,
            f"How many consecutive zeros appear at the right end of {m(f'{n}!')} when written in standard base-{m(10)} notation?",
            f"كم صفراً متتالياً يظهر في أقصى يمين العدد {m(f'{n}!')} عند كتابته بالنظام العشري؟",
            ans, [q5, ans - 1, ans + 1, ans + 2],
            f"Apply Legendre's formula {m('\\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor')}.",
            f"طبّق صيغة ليجاندر لقوى الخمسة: {m('\\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor')}.",
            f"Count the total exponent of prime {m(5)} in {m(f'{n}!')}!",
            [
                f"Multiples of {m(5)} contribute {m(f'\\lfloor {n}/5 \\rfloor = {q5}')} factors of {m(5)}.",
                f"Multiples of {m(25)} add {m(f'\\lfloor {n}/25 \\rfloor = {q25}')}, and multiples of {m(125)} add {m(f'\\lfloor {n}/125 \\rfloor = {q125}')}.",
                f"Total trailing zeros: {m(f'{q5} + {q25} + {q125} = {ans}')}.",
            ],
            f"Notice {m(q5)} alone misses the {m(ans - q5)} extra factors of {m(5)} from higher powers!",
            f"نحسب الأس الكلي للعامل الأولي {m(5)} في تحليل {m(f'{n}!')}!",
            [
                f"مضاعفات {m(5)} تعطي {m(f'\\lfloor {n}/5 \\rfloor = {q5}')}.",
                f"مضاعفات {m(25)} تضيف {m(q25)}، ومضاعفات {m(125)} تضيف {m(q125)}.",
                f"مجموع الأصفار الطرفية هو {m(f'{q5} + {q25} + {q125} = {ans}')}.",
            ],
            f"تحقق: عوامل العدد {m(2)} أكثر بكثير من عوامل {m(5)}، لذا يحدد أس الـ {m(5)} عدد الأصفار.",
            diagram_en=svg_factor_tree(f"{n}!", f"÷5→{q5}", f"÷25→{q25}", f"÷125→{q125}", "Z=?"),
        )

    for z_target in (12, 16, 20, 22, 28, 32):
        ans = next(x for x in range(1, 300) if _vp_fact(x, 5) == z_target)
        assert _vp_fact(ans - 1, 5) < z_target
        B.add_math(
            tp, "Medium", bp,
            f"What is the **smallest** positive integer {m('n')} such that {m('n!')} ends in at least {m(z_target)} trailing zeros?",
            f"ما **أصغر** عدد صحيح موجب {m('n')} يجعل العدد {m('n!')} ينتهي بـ {m(z_target)} صفراً على الأقل في يمينه؟",
            ans, [5 * z_target, ans - 5, ans + 5, ans + 1],
            f"Remember {m('n!')} gains new zeros only at multiples of {m(5)}, and {m('n')} is slightly smaller than {m(f'5 \\times {z_target} = {5*z_target}')}.",
            f"تذكّر أن عدد الأصفار يقفز فقط عند مضاعفات {m(5)}، وأن {m('n')} أصغر قليلاً من {m(5*z_target)} بسبب مضاعفات {m(25)}.",
            f"Estimate {m('n \\approx 4z')}, then test multiples of {m(5)} with Legendre's sum!",
            [
                f"Since {m('n/5 + n/25 \\approx 6n/25')}, estimate {m(f'n \\approx \\frac{{25 \\times {z_target}}}{{6}} \\approx {round(25*z_target/6)}')}.",
                f"At {m(f'n = {ans}')}, {m(f'Z({ans}!) = {ans//5} + {ans//25} + {ans//125} = {z_target}')}.",
                f"For {m(f'n = {ans - 1}')}, {m(f'Z({ans - 1}!) = {_vp_fact(ans - 1, 5)} < {z_target}')}, so {m(ans)} is minimal.",
            ],
            f"Naive multiplication {m(f'5 \\times {z_target} = {5*z_target}')} overshoots because multiples of {m(25)} supply bonus {m(5)}'s!",
            f"نقدّر قيمة {m('n')} بقرب {m('\\frac{25}{6} z')} ثم نفحص مضاعفات {m(5)} بصيغة ليجاندر!",
            [
                f"عند {m(f'n = {ans}')} نجد {m(f'Z({ans}!) = {ans//5} + {ans//25} + {ans//125} = {z_target}')}.",
                f"بينما عند {m(f'n = {ans - 1}')} يكون عدد الأصفار {m(_vp_fact(ans - 1, 5))} فقط.",
                f"إذن أصغر قيمة تحقق المطلوب هي {m(f'n = {ans}')}.",
            ],
            f"انتبه: الضرب المباشر {m(f'5 \\times {z_target} = {5*z_target}')} يتجاهل العوامل الإضافية في مضاعفات {m(25)}!",
            diagram_en=svg_factor_tree("n!", f"Z={z_target}", "÷5", "÷25", "min n"),
        )

    hard_base_fact = [
        (50, 12, "2^2 \\times 3", 2, 2, 3, 1),
        (60, 15, "3 \\times 5", 3, 1, 5, 1),
        (72, 18, "2 \\times 3^2", 2, 1, 3, 2),
        (80, 24, "2^3 \\times 3", 2, 3, 3, 1),
    ]
    for n, base_b, b_fac, p1, e1, p2, e2 in hard_base_fact:
        v1, v2 = _vp_fact(n, p1), _vp_fact(n, p2)
        ans = min(v1 // e1, v2 // e2)
        B.add_math(
            tp, "Hard", bp,
            f"When {m(f'{n}!')} is written in **base {m(base_b)}**, in how many consecutive trailing zeros does it end?",
            f"عند كتابة العدد {m(f'{n}!')} في **نظام العدّ ذي الأساس {m(base_b)}**، بكم صفراً متتالياً ينتهي في أقصى يمينه؟",
            ans, [max(v1 // e1, v2 // e2), v2, ans + 1, ans - 1],
            f"Factor the base {m(f'{base_b} = {b_fac}')}; each trailing zero requires a full copy of {m(b_fac)}.",
            f"حلّل الأساس {m(f'{base_b} = {b_fac}')}؛ كل صفر طرفي يحتاج نسخة كاملة من عوامل {m(base_b)}.",
            f"Count prime exponents of {m(p1)} and {m(p2)} in {m(f'{n}!')}, then take {m(f'\\min(\\lfloor v_{{{p1}}}/{e1} \\rfloor, \\lfloor v_{{{p2}}}/{e2} \\rfloor)')}!",
            [
                f"Factor the base: {m(f'{base_b} = {b_fac}')}.",
                f"By Legendre's formula, {m(f'v_{{{p1}}}({n}!) = {v1}')} (giving {m(f'\\lfloor {v1}/{e1} \\rfloor = {v1 // e1}')} blocks) and {m(f'v_{{{p2}}}({n}!) = {v2}')} (giving {m(f'\\lfloor {v2}/{e2} \\rfloor = {v2 // e2}')} blocks).",
                f"The limiting prime-power block count is {m(f'\\min({v1 // e1}, {v2 // e2}) = {ans}')}.",
            ],
            f"Always check **both** prime powers when a prime has exponent {m('>1')} in the base!",
            f"نحسب أسس العوامل الأولية للأساس {m(base_b)} داخل {m(f'{n}!')} ونأخذ الأصغر بعد القسمة على أسسها!",
            [
                f"تحليل الأساس هو {m(f'{base_b} = {b_fac}')}.",
                f"نجد {m(f'v_{{{p1}}}({n}!) = {v1}')} (أي {m(v1 // e1)} حزمة) و{m(f'v_{{{p2}}}({n}!) = {v2}')} (أي {m(v2 // e2)} حزمة).",
                f"العدد المحدد للأصفار هو الأصغر: {m(f'\\min({v1 // e1}, {v2 // e2}) = {ans}')}.",
            ],
            f"تحقق: لا تكتفِ بالعامل الأولي الأكبر وحده عندما يحوي الأساس قوة أولية مثل {m('2^2')} أو {m('2^3')}!",
            diagram_en=svg_factor_tree(f"{n}! (base {base_b})", f"v_{p1}={v1}", f"v_{p2}={v2}", f"÷{e1}", f"÷{e2}"),
        )

    # 3. nsmo_g89_divisor_sum_product (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g89_divisor_sum_product"
    easy_div = [
        (180, "count", "2^2 \\times 3^2 \\times 5", "4×9", "5"),
        (240, "count", "2^4 \\times 3 \\times 5", "16", "15"),
        (420, "count", "2^2 \\times 3 \\times 5 \\times 7", "12", "35"),
        (72, "sum", "2^3 \\times 3^2", "8", "9"),
        (120, "sum", "2^3 \\times 3 \\times 5", "8", "15"),
    ]
    for N, kind, fac_tex, l1, r1 in easy_div:
        divs = _divisors(N)
        ans = len(divs) if kind == "count" else sum(divs)
        ask_en = "how many positive divisors" if kind == "count" else "what is the **sum** of all positive divisors"
        ask_ar = "كم قاسماً موجباً" if kind == "count" else "ما **مجموع** جميع القواسم الموجبة"
        B.add_math(
            tp, "Easy", bp,
            f"For the integer {m(N)}, {ask_en} does {m(N)} have?",
            f"للعدد الصحيح {m(N)}، {ask_ar} له؟",
            ans, [ans - 4, ans + 6, ans // 2, ans + 12],
            f"Prime-factorize {m(f'{N} = {fac_tex}')} first.",
            f"حلّل العدد إلى عوامله الأولية أولاً: {m(f'{N} = {fac_tex}')}.",
            f"Use the prime factorization {m(f'{N} = {fac_tex}')}!",
            [
                f"Write {m(f'{N} = {fac_tex}')}.",
                f"Apply the {'exponent+1 product rule' if kind == 'count' else 'multiplicative geometric-sum formula'} across each prime power.",
                f"Evaluating the product yields {m(ans)}.",
            ],
            f"Direct divisor check confirms {m(ans)} for {m(N)}.",
            f"ننطلق من التحليل الأولي {m(f'{N} = {fac_tex}')}!",
            [
                f"نحلل العدد: {m(f'{N} = {fac_tex}')}.",
                f"نطبّق {'قاعدة ضرب (الأس + 1)' if kind == 'count' else 'صيغة ضرب مجموع قوى كل عامل أولي'}.",
                f"الناتج النهائي يساوي {m(ans)}.",
            ],
            f"تحقق مباشر من قواسم {m(N)} يؤكد أن الجواب {m(ans)}.",
            diagram_en=svg_factor_tree(str(N), l1, r1, "pᵃ", "qᵇ"),
        )

    for M in (300, 500, 900):
        ans = math.isqrt(M)
        assert ans == sum(1 for x in range(1, M + 1) if len(_divisors(x)) % 2 == 1)
        B.add_math(
            tp, "Medium", bp,
            f"How many positive integers {m('n')} with {m(f'1 \\le n \\le {M}')} have an **odd** number of positive divisors?",
            f"كم عدداً صحيحاً موجباً {m('n')} يحقق {m(f'1 \\le n \\le {M}')} وله عدد **فردي** من القواسم الموجبة؟",
            ans, [ans - 1, ans + 1, M // 2, ans * 2],
            f"Pair each divisor {m('d')} with {m('n/d')}: when is {m('d = n/d')}?",
            f"زاوج كل قاسم {m('d')} مع {m('n/d')}؛ متى يندمج الزوج في عدد واحد {m('d = n/d')}؟",
            f"An integer has an odd number of positive divisors if and only if it is a **perfect square**!",
            [
                f"Divisors of {m('n')} pair up as {m('(d, n/d)')}, leaving an unpaired divisor iff {m('n = k^2')}.",
                f"Count perfect squares {m(f'1^2, 2^2, \\dots, k^2 \\le {M}')}.",
                f"Since {m(f'{ans}^2 = {ans*ans} \\le {M}')} (and {m(f'{ans+1}^2 = {(ans+1)**2} > {M}')}), there are {m(ans)} such integers.",
            ],
            f"Square boundary check: {m(f'{ans}^2 = {ans*ans}')} fits inside {m(M)}, while {m((ans+1)**2)} exceeds {m(M)}.",
            f"يكون لعدد موجب عدد فردي من القواسم إذا وفقط إذا كان **مربعاً كاملاً**!",
            [
                f"تتزاوج القواسم على صورة {m('(d, n/d)')} ولا يبقى قاسم منفرد إلا عندما {m('n = k^2')}.",
                f"نحصي المربعات الكاملة من {m('1^2')} حتى {m(M)}.",
                f"بما أن {m(f'\\lfloor \\sqrt{{{M}}} \\rfloor = {ans}')}، يوجد {m(ans)} عدداً.",
            ],
            f"تحقق: {m(f'{ans}^2 = {ans*ans} \\le {M} < {(ans+1)**2}')}.",
            diagram_en=svg_number_strip(["1²", "2²", "…", f"≤ {M}"]),
        )

    for N, k_div, fac_q in [(360, 2, "2^2 \\times 3^2 \\times 5"), (720, 6, "2^3 \\times 3 \\times 5"), (1080, 12, "2 \\times 3^2 \\times 5")]:
        ans = sum(1 for d in _divisors(N) if d % k_div == 0)
        q_val = N // k_div
        assert ans == len(_divisors(q_val))
        B.add_math(
            tp, "Medium", bp,
            f"How many positive divisors of {m(N)} are multiples of {m(k_div)}?",
            f"كم قاسماً موجباً للعدد {m(N)} يُعدّ مضاعفاً للعدد {m(k_div)}؟",
            ans, [len(_divisors(N)), ans - 2, ans + 4, ans // 2],
            f"Write every such divisor as {m(f'd = {k_div}m')}; then {m('m')} can be any positive divisor of {m(f'{N}/{k_div} = {q_val}')}!",
            f"اكتب كل قاسم مطلوب على الصورة {m(f'd = {k_div}m')}؛ عندئذٍ {m('m')} هو أي قاسم موجب للعدد {m(f'{N}/{k_div} = {q_val}')}!",
            f"Factor out {m(k_div)} first: counting multiples of {m(k_div)} dividing {m(N)} equals counting all divisors of {m(q_val)}!",
            [
                f"Set {m(f'd = {k_div}m')}. Then {m(f'd \\mid {N} \\iff m \\mid \\frac{{{N}}}{{{k_div}}} = {q_val}')}.",
                f"Prime-factorize {m(f'{q_val} = {fac_q}')}.",
                f"Adding {m(1)} to each prime exponent and multiplying gives {m(ans)} divisors.",
            ],
            f"Check: {m(ans)} is strictly less than the total divisor count {m(len(_divisors(N)))} of {m(N)}.",
            f"بقسمة {m(N)} على {m(k_div)} تتحول المسألة إلى حساب جميع القواسم الموجبة للعدد {m(q_val)}!",
            [
                f"نضع {m(f'd = {k_div}m')} فيكون {m(f'd \\mid {N} \\iff m \\mid {q_val}')}.",
                f"نحلل {m(f'{q_val} = {fac_q}')}.",
                f"نضرب (الأس + 1) لكل عامل أولي فنحصل على {m(ans)} قاسماً.",
            ],
            f"تحقق: العدد الكلي لقواسم {m(N)} هو {m(len(_divisors(N)))}، ومنها {m(ans)} تقبل القسمة على {m(k_div)}.",
            diagram_en=svg_factor_tree(f"{N}÷{k_div}={q_val}", "pᵃ", "qᵇ", "rᶜ", "τ=?"),
        )

    for t_cnt, fac_ans in [(12, "2^2 \\times 3 \\times 5"), (15, "2^4 \\times 3^2"), (16, "2^3 \\times 3 \\times 5"), (18, "2^2 \\times 3^2 \\times 5")]:
        ans = next(x for x in range(1, 2000) if len(_divisors(x)) == t_cnt)
        B.add_math(
            tp, "Hard", bp,
            f"What is the **smallest** positive integer that has exact {m(t_cnt)} positive divisors?",
            f"ما **أصغر** عدد صحيح موجب له بالضبط {m(t_cnt)} قاسماً موجباً؟",
            ans, [2 ** (t_cnt - 1) if t_cnt <= 12 else ans + 36, ans + 24, ans + 60, ans * 2],
            f"Factor {m(t_cnt)} into ways of writing {m('(a+1)(b+1)\\cdots = ' + str(t_cnt))} and assign larger exponents to the smallest primes {m('2, 3, 5')}.",
            f"حلّل {m(t_cnt)} إلى جداء عوامل {m('(a+1)(b+1)\\cdots')} وامنح الأسس الأكبر لأصغر الأعداد الأولية {m('2, 3, 5')}.",
            f"Test exponent shapes multiplying to {m(t_cnt)} on the smallest primes {m('2, 3, 5, \\dots')}!",
            [
                f"Write {m(t_cnt)} as a product of factors {m('\\ge 2')} and assign non-increasing exponents {m('e_1 \\ge e_2 \\ge \\cdots')} to primes {m('2, 3, 5, \\dots')}.",
                f"Comparing candidate prime-power products shows {m(f'{fac_ans} = {ans}')} beats single-prime or fewer-prime shapes.",
                f"Thus the minimal positive integer with {m(t_cnt)} divisors is {m(ans)}.",
            ],
            f"Verify: {m(f'\\tau({ans}) = {len(_divisors(ans))}')}, and no smaller integer achieves {m(t_cnt)} divisors.",
            f"نقارن جميع طرق تحليل {m(t_cnt)} ونضع الأسس الأكبر على أصغر الأعداد الأولية {m('2, 3, 5')}!",
            [
                f"نكتب {m(t_cnt)} كحاصل ضرب عوامل {m('(e_i + 1)')} ونرتب الأسس تنازلياً على {m('2, 3, 5')}.",
                f"بمقارنة المرشحين نجد أن أصغر قيمة هي {m(f'{fac_ans} = {ans}')}.",
                f"إذن أصغر عدد موجب له {m(t_cnt)} قاسماً هو {m(ans)}.",
            ],
            f"تحقق: عدد قواسم {m(ans)} يساوي {m(t_cnt)} تماماً.",
        )

    # 4. nsmo_g89_gcd_lcm_pair_count (5E, 6M, 4H) — SVG: svg_venn_2
    bp = "nsmo_g89_gcd_lcm_pair_count"
    for g, L, a0 in [(6, 180, 30), (8, 240, 48), (12, 360, 72), (15, 450, 90), (9, 315, 45)]:
        ans = (g * L) // a0
        assert math.gcd(a0, ans) == g and math.lcm(a0, ans) == L
        B.add_math(
            tp, "Easy", bp,
            f"Two positive integers {m('a')} and {m('b')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. If {m(f'a = {a0}')}, what is {m('b')}?",
            f"عددان صحيحان موجبان {m('a')} و{m('b')} يحققان {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. إذا كان {m(f'a = {a0}')}، فما قيمة {m('b')}؟",
            ans, [L // a0, ans + g, ans - g, (L // g)],
            f"Use the fundamental identity {m('a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b)')}.",
            f"استخدم المتطابقة الأساسية {m('a \\times b = \\gcd(a, b) \\times \\operatorname{lcm}(a, b)')}.",
            f"Apply {m('ab = gL')} directly!",
            [
                f"For any two positive integers, {m('a \\cdot b = \\gcd(a,b) \\cdot \\operatorname{lcm}(a,b)')}.",
                f"Substitute {m(f'{a0} \\cdot b = {g} \\times {L} = {g*L}')}.",
                f"Divide by {m(a0)}: {m(f'b = {g*L} / {a0} = {ans}')}.",
            ],
            f"Check: {m(f'\\gcd({a0}, {ans}) = {g}')} and {m(f'\\operatorname{{lcm}}({a0}, {ans}) = {L}')}.",
            f"نطبّق العلاقة {m('a \\times b = \\gcd(a,b) \\times \\operatorname{lcm}(a,b)')} مباشرة!",
            [
                f"حاصل ضرب العددين يساوي حاصل ضرب قاسمهما المشترك الأكبر في مضاعفهما المشترك الأصغر.",
                f"نعوّض: {m(f'{a0} \\times b = {g} \\times {L} = {g*L}')}.",
                f"بالقسمة على {m(a0)} نجد {m(f'b = {ans}')}.",
            ],
            f"تحقق: {m(f'\\gcd({a0}, {ans}) = {g}')} و{m(f'\\operatorname{{lcm}}({a0}, {ans}) = {L}')}.",
            diagram_en=svg_venn_2(f"a={a0}", "b=?", str(a0 // g), str(g), "y", f"lcm={L}"),
        )

    med_gl = [
        (4, 120, "2 \\times 3 \\times 5", 3),
        (5, 300, "2^2 \\times 3 \\times 5", 3),
        (6, 252, "2 \\times 3 \\times 7", 3),
        (3, 630, "2 \\times 3 \\times 5 \\times 7", 4),
        (7, 294, "2 \\times 3 \\times 7", 3),
        (2, 420, "2 \\times 3 \\times 5 \\times 7", 4),
    ]
    for g, L, q_fac, k_primes in med_gl:
        q_val = L // g
        ans = 2 ** k_primes
        assert ans == sum(1 for d in _divisors(q_val) if math.gcd(d, q_val // d) == 1)
        B.add_math(
            tp, "Medium", bp,
            f"How many **ordered pairs** {m('(a, b)')} of positive integers satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}?",
            f"كم **زوجاً مرتباً** {m('(a, b)')} من الأعداد الصحيحة الموجبة يحقق {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}؟",
            ans, [ans // 2, len(_divisors(q_val)), ans + 2, ans * 2],
            f"Write {m(f'a = {g}x, b = {g}y')} with {m('\\gcd(x, y) = 1')} so {m(f'xy = {L}/{g} = {q_val}')}.",
            f"ضع {m(f'a = {g}x')} و{m(f'b = {g}y')} مع {m('\\gcd(x,y) = 1')} فيكون {m(f'xy = {L}/{g} = {q_val}')}.",
            f"Count distinct prime factors {m('k')} of {m(f'L/g = {q_val}')}; the ordered pair count is {m('2^k')}!",
            [
                f"Let {m(f'a = {g}x')} and {m(f'b = {g}y')} with {m('\\gcd(x, y) = 1')}; then {m(f'xy = {L}/{g} = {q_val}')}.",
                f"Factor {m(f'{q_val} = {q_fac}')}, which has {m(f'k = {k_primes}')} distinct prime-power blocks.",
                f"Each block goes wholly to {m('x')} or wholly to {m('y')}, yielding {m(f'2^{{{k_primes}}} = {ans}')} ordered pairs.",
            ],
            f"Unordered pairs would be {m(ans // 2)}, whereas ordered pairs count both {m('(a,b)')} and {m('(b,a)')} to give {m(ans)}.",
            f"نحسب عدد العوامل الأولية المختلفة {m('k')} للخارج {m(f'L/g = {q_val}')} فيكون الجواب {m('2^k')}!",
            [
                f"نضع {m(f'a = {g}x, b = {g}y')} بشرط {m('\\gcd(x,y) = 1')} فنجد {m(f'xy = {q_val}')}.",
                f"تحليل {m(f'{q_val} = {q_fac}')} يضم {m(k_primes)} قوى أولية مستقلة.",
                f"تتوزع كل قوة كاملة على {m('x')} أو {m('y')} بطريقتين، فيكون العدد {m(f'2^{{{k_primes}}} = {ans}')}.",
            ],
            f"انتبه: المطلوب الأزواج **المرتبة** ولذلك الجواب {m(ans)} وليس نصفه {m(ans // 2)}.",
            diagram_en=svg_venn_2(f"a={g}x", f"b={g}y", "x", str(g), "y", f"xy={q_val}"),
        )

    for g, L in [(6, 360), (8, 560), (5, 420), (12, 504)]:
        q_val = L // g
        ans = min(g * (d + q_val // d) for d in _divisors(q_val) if math.gcd(d, q_val // d) == 1)
        B.add_math(
            tp, "Hard", bp,
            f"Positive integers {m('a')} and {m('b')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. What is the **minimum** possible value of {m('a + b')}?",
            f"يحقق العددان الصحيحان الموجبان {m('a')} و{m('b')} الشرطين {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. ما **أصغر** قيمة ممكنة للمجموع {m('a + b')}؟",
            ans, [g * (1 + q_val), ans + 2 * g, ans - g, g * int(sum(divmod(q_val, 2)))],
            f"Write {m(f'a + b = {g}(x + y)')} where {m(f'xy = {q_val}')} and {m('\\gcd(x, y) = 1')}; choose {m('x, y')} as close together as possible!",
            f"اكتب {m(f'a + b = {g}(x + y)')} حيث {m(f'xy = {q_val}')} و{m('\\gcd(x, y) = 1')}، واختر {m('x, y')} متقاربين قدر الإمكان!",
            f"Minimize {m('x + y')} over **coprime** factor pairs of {m(f'L/g = {q_val}')}!",
            [
                f"Set {m(f'a = {g}x')} and {m(f'b = {g}y')} with {m('\\gcd(x, y) = 1')} and {m(f'xy = {L}/{g} = {q_val}')}.",
                f"To minimize {m('x + y')}, pick coprime factors of {m(q_val)} closest to {m(f'\\sqrt{{{q_val}}}')}.",
                f"Multiplying that minimal sum {m(ans // g)} by {m(g)} gives {m(f'a + b = {ans}')}.",
            ],
            f"Trap check: non-coprime factorizations of {m(q_val)} are invalid because they increase {m('\\gcd(a, b)')} above {m(g)}!",
            f"نبحث عن عاملين **أوليين نسبياً** للعدد {m(q_val)} متقاربين قدر الإمكان لتصغير {m('x + y')}!",
            [
                f"بوضع {m(f'a = {g}x, b = {g}y')} يكون {m(f'xy = {q_val}')} مع شرط {m('\\gcd(x,y) = 1')}.",
                f"أقرب عاملين أوليين نسبياً لجذر {m(q_val)} يعطيان أصغر مجموع {m(f'x + y = {ans // g}')}.",
                f"نضرب في {m(g)} فنحصل على {m(f'a + b = {ans}')}.",
            ],
            f"تحقق: أي تحليل غير أولي نسبياً للعدد {m(q_val)} يرفع القاسم المشترك الأكبر فوق {m(g)} فهو مرفوض!",
            diagram_en=svg_venn_2(f"{g}x", f"{g}y", "x", str(g), "y", f"min(a+b)"),
        )

    # 5. nsmo_g89_base_b_conversion (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g89_base_b_conversion"
    easy_base = [
        ("231", 4),
        ("142", 5),
        ("325", 6),
        ("246", 7),
        ("175", 8),
    ]
    for digits_s, b in easy_base:
        ans = int(digits_s, b)
        d2, d1, d0 = [int(c) for c in digits_s]
        B.add_math(
            tp, "Easy", bp,
            f"Convert the base-{m(b)} numeral {m(f'({digits_s})_{{{b}}}')} into standard base-{m(10)} notation.",
            f"حوّل العدد المكتوب في الأساس {m(b)} وهو {m(f'({digits_s})_{{{b}}}')} إلى النظام العشري.",
            ans, [ans + b, ans - b, d2 * 100 + d1 * 10 + d0, ans + b * b],
            f"Expand {m(f'{d2} \\cdot {b}^2 + {d1} \\cdot {b} + {d0}')}.",
            f"افكك القيم المكانية للخانات: {m(f'{d2} \\cdot {b}^2 + {d1} \\cdot {b} + {d0}')}.",
            f"Multiply each digit by its positional power of {m(b)}!",
            [
                f"Write place values: {m(f'({digits_s})_{{{b}}} = {d2} \\times {b}^2 + {d1} \\times {b} + {d0}')}.",
                f"Evaluate powers: {m(f'{d2 * b * b} + {d1 * b} + {d0}')}.",
                f"Add to obtain {m(ans)} in base {m(10)}.",
            ],
            f"Check: every digit in {m(digits_s)} is strictly less than {m(b)}, and {m(f'{ans} = ({digits_s})_{{{b}}}')}.",
            f"نضرب كل خانة في القوة المقابلة للأساس {m(b)} ثم نجمع!",
            [
                f"نفك العدد: {m(f'{d2} \\times {b}^2 + {d1} \\times {b} + {d0}')}.",
                f"نحسب الحدود: {m(f'{d2 * b * b} + {d1 * b} + {d0}')}.",
                f"المجموع في النظام العشري يساوي {m(ans)}.",
            ],
            f"تحقق: القسمة المتكررة للعدد {m(ans)} على {m(b)} تعيد الخانات {m(digits_s)} بالترتيب.",
            diagram_en=svg_digit_slots(list(digits_s), f"Base {b}: {b}², {b}¹, 1"),
        )

    med_base = [
        ("24", "33", "101", 6),
        ("45", "36", "103", 8),
        ("54", "47", "112", 9),
        ("23", "34", "112", 5),
        ("46", "25", "104", 7),
        ("67", "56", "112", 11),
    ]
    for s1, s2, s3, b_ans in med_base:
        assert int(s1, b_ans) + int(s2, b_ans) == int(s3, b_ans)
        max_d = max(int(c) for c in s1 + s2 + s3)
        B.add_math(
            tp, "Medium", bp,
            f"In what positive integer base {m(f'b > {max_d}')} is the addition {m(f'({s1})_b + ({s2})_b = ({s3})_b')} valid?",
            f"في أي أساس عددي صحيح موجب {m(f'b > {max_d}')} تتحقق عملية الجمع {m(f'({s1})_b + ({s2})_b = ({s3})_b')}؟",
            b_ans, [b_ans - 1, b_ans + 1, b_ans + 2, 10 if b_ans != 10 else 12],
            f"Look at the units column {m(f'{s1[1]} + {s2[1]} = b + {s3[2]}')} (or expand all three numerals in powers of {m('b')}).",
            f"انظر إلى عمود الآحاد {m(f'{s1[1]} + {s2[1]} = b + {s3[2]}')} أو حوّل الحدود الثلاثة إلى قوى {m('b')}.",
            f"Expand both sides in powers of {m('b')} (or read the carry from the units column)!",
            [
                f"In the units place, {m(f'{int(s1[1])} + {int(s2[1])} = {int(s1[1]) + int(s2[1])}')}, which leaves digit {m(s3[2])} with carry {m(1)}, so {m(f'b = {int(s1[1]) + int(s2[1])} - {int(s3[2])} = {b_ans}')}.",
                f"Check the full quadratic: {m(f'({s1[0]}b + {s1[1]}) + ({s2[0]}b + {s2[1]}) = b^2 + {s3[1]}b + {s3[2]}')}.",
                f"Substituting {m(f'b = {b_ans}')} gives {m(f'{int(s1, b_ans)} + {int(s2, b_ans)} = {int(s3, b_ans)}')}, confirming {m(f'b = {b_ans}')}.",
            ],
            f"All digits are {m(f'\\le {max_d} < {b_ans}')}, so {m(f'b = {b_ans}')} is completely valid!",
            f"نفك الأعداد الثلاثة بدلالة قوى {m('b')} أو نستنتج قيمة {m('b')} مباشرة من حمل خانة الآحاد!",
            [
                f"مجموع خانتي الآحاد {m(f'{int(s1[1])} + {int(s2[1])} = {int(s1[1]) + int(s2[1])}')} ويكتب {m(s3[2])} مع حمل {m(1)}، إذن {m(f'b = {b_ans}')}.",
                f"نتحقق في عمود العشرات: {m(f'{int(s1[0])} + {int(s2[0])} + 1 = {int(s1[0]) + int(s2[0]) + 1} = 1 \\cdot {b_ans} + {int(s3[1])}')}.",
                f"إذن الأساس الصحيح الوحيد هو {m(f'b = {b_ans}')}.",
            ],
            f"تحقق عشري: {m(f'{int(s1, b_ans)} + {int(s2, b_ans)} = {int(s3, b_ans)} = ({s3})_{{{b_ans}}}')}.",
            diagram_en=svg_digit_slots([f"{s1}_b", "+", f"{s2}_b", f"{s3}_b"], f"b > {max_d}"),
        )

    hard_rev = [
        (7, 9, 4, 3),   # (43)_7 = 31 = (34)_9
        (5, 8, 3, 2),   # wait: 5*3+2=17 vs 8*2+3=19 -> let's compute exact pairs below!
    ]
    # Exact two-base / three-digit reversal gems verified programmatically:
    # 1) (ab)_7 = (ba)_9 -> 7a+b = 9b+a -> 3a = 4b -> (4,3) -> base-10 value 31
    # 2) (ab)_8 = (ba)_11 -> 8a+b = 11b+a -> 7a = 10b -> no; (ab)_6 = (ba)_9 -> 5a = 8b -> no; (ab)_5 = (ba)_7 -> 4a=6b -> 2a=3b -> (3,2) -> 17 = 14+3=17! YES!
    # 3) (abc)_7 = (cba)_9 with b=0 -> 49a+c = 81c+a -> 48a = 80c -> 3a = 5c -> (5,0,3): 49*5+3 = 248 = 81*3+5! YES!
    # 4) (abc)_6 = (cba)_8 with b=2 -> 36a+12+c = 64c+16+a -> 35a - 4 = 63c -> wait (abc)_5 = (cba)_7 with b=0 -> 25a+c = 49c+a -> 24a = 48c -> a=2c -> a=4,c=2 -> (402)_5 = 102 = (204)_7! Or unique: (ab)_9 = (ba)_13 -> 8a = 12b -> 2a=3b -> if gcd(a,b)=1 or unique in base: let's check (ab)_7 = (ba)_11 -> 6a = 10b -> 3a = 5b -> unique (5,3) since a<7! 35+3 = 38 = 33+5!
    # And (ab)_8 = (ba)_13 -> 7a = 12b -> no; (ab)_9 = (ba)_14 -> 8a = 13b -> no; (ab)_6 = (ba)_10 -> 5a = 9b -> (9 invalid); (ab)_8 = (ba)_11? no; (ab)_9 = (ba)_11 -> 8a = 10b -> 4a = 5b -> unique (5,4) since a<9! 45+4 = 49 = 44+5!
    hard_base_gems = [
        (5, 7, 3, 2),    # 2a = 3b, 1<=a<=4 -> unique (3,2) -> 17
        (7, 9, 4, 3),    # 3a = 4b, 1<=a<=6 -> unique (4,3) -> 31
        (7, 11, 5, 3),   # 3a = 5b, 1<=a<=6 -> unique (5,3) -> 38
        (9, 11, 5, 4),   # 4a = 5b, 1<=a<=8 -> unique (5,4) -> 49
    ]
    for b1, b2, da, db in hard_base_gems:
        sols = [(a, b) for a in range(1, b1) for b in range(1, b1) if b1 * a + b == b2 * b + a]
        assert sols == [(da, db)], f"Expected unique solution, got {sols}"
        ans = b1 * da + db
        B.add_math(
            tp, "Hard", bp,
            f"Nonzero digits {m('a')} and {m('b')} (both valid in base {m(b1)}) satisfy {m(f'(\\overline{{ab}})_{{{b1}}} = (\\overline{{ba}})_{{{b2}}}')}. Express the common value of this number in **base {m(10)}**.",
            f"الرقمان غير الصفريين {m('a')} و{m('b')} (وكلاهما مسموح في الأساس {m(b1)}) يحققان {m(f'(\\overline{{ab}})_{{{b1}}} = (\\overline{{ba}})_{{{b2}}}')}. أوجد القيمة المشتركة لهذا العدد في **النظام العشري**.",
            ans, [da * 10 + db, db * 10 + da, ans + b1, ans - b1],
            f"Expand {m(f'{b1}a + b = {b2}b + a')} and use {m(f'1 \\le a, b < {b1}')} to pin down {m('(a, b)')} uniquely!",
            f"فكّ المعادلة إلى {m(f'{b1}a + b = {b2}b + a')} واستخدم قيد الخانات {m(f'1 \\le a, b < {b1}')} لتحديد الزوج الوحيد!",
            f"Equate the base-{m(10)} expansions and apply the base-{m(b1)} digit bound {m(f'a < {b1}')}!",
            [
                f"Expand both sides: {m(f'{b1}a + b = {b2}b + a \\implies {b1 - 1}a = {b2 - 1}b')}.",
                f"Divide by {m(math.gcd(b1 - 1, b2 - 1))}: {m(f'{(b1-1)//math.gcd(b1-1,b2-1)}a = {(b2-1)//math.gcd(b1-1,b2-1)}b')}. Since {m(f'1 \\le a, b < {b1}')}, the unique digit pair is {m(f'(a, b) = ({da}, {db})')}.",
                f"Evaluate in base {m(10)}: {m(f'{b1}({da}) + {db} = {ans}')} (which also equals {m(f'{b2}({db}) + {da} = {ans}')}).",
            ],
            f"Check: {m(f'({da}{db})_{{{b1}}} = {ans} = ({db}{da})_{{{b2}}}')}!",
            f"نساوي القيمتين المكانيتين في النظام العشري ثم نستخدم شرط {m(f'1 \\le a, b < {b1}')}!",
            [
                f"بفك الطرفين: {m(f'{b1}a + b = {b2}b + a \\implies {b1 - 1}a = {b2 - 1}b')}.",
                f"بالتبسيط ومراعاة أن الخانات أصغر من {m(b1)}، الحل الوحيد هو {m(f'(a, b) = ({da}, {db})')}.",
                f"القيمة العشرية تساوي {m(f'{b1} \\times {da} + {db} = {ans}')}.",
            ],
            f"تحقق: {m(f'{b2} \\times {db} + {da} = {ans}')} أيضاً!",
            diagram_en=svg_digit_slots([f"a<{b1}", f"b<{b1}"], f"(ab)_{b1} = (ba)_{b2}"),
        )


# =============================================================================
# UNIT 2.2 — Digit Constraints, Palindromes, Stamps & Unit Fractions (75 Qs)
# =============================================================================
def _add_unit_2_2(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. nsmo_g89_semi_increasing_digits (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g89_semi_increasing_digits"
    for k in (2, 3, 4, 5):
        ans = math.comb(9, k)
        B.add_math(
            tp, "Easy", bp,
            f"How many {m(k)}-digit positive integers have **strictly increasing** digits from left to right (for example, {m(''.join(str(i) for i in range(1, k+1)))})?",
            f"كم عدداً صحيحاً موجباً مكوناً من {m(k)} خانات تكون أرقامه **متزايدة قطعيّاً** من اليسار إلى اليمين (مثل {m(''.join(str(i) for i in range(1, k+1)))})؟",
            ans, [math.comb(10, k), ans - 9, ans + 12, math.comb(8, k)],
            f"Can {m(0)} ever appear if the leftmost digit is at least {m(1)} and digits strictly increase?",
            f"هل يمكن أن يظهر الصفر إذا كانت الخانة اليسرى {m('\\ge 1')} والأرقام تتزايد قطعيّاً؟",
            f"Every subset of {m(k)} distinct digits from {m('\\{1, 2, \\dots, 9\\}')} sorts into exact one strictly increasing {m(k)}-digit integer!",
            [
                f"Since {m('d_1 \\ge 1')} and {m('d_1 < d_2 < \\cdots < d_k')}, the digit {m(0)} can never occur.",
                f"Choose any {m(k)} distinct digits from {m('\\{1, 2, \\dots, 9\\}')}; there is only {m(1)} increasing order for them.",
                f"Compute {m(f'\\binom{{9}}{{{k}}} = {ans}')}.",
            ],
            f"Using {m(f'\\binom{{10}}{{{k}}} = {math.comb(10, k)}')} is the classic trap of accidentally allowing a leading {m(0)}!",
            f"كل مجموعة جزئية من {m(k)} أرقام مختارة من {m('\\{1,\\dots,9\\}')} ترتّب تصاعدياً بطريقة وحيدة!",
            [
                f"يستحيل ظهور الرقم {m(0)} لأن أصغر خانة تقع في أقصى اليسار ويجب أن تكون {m('\\ge 1')}.",
                f"نختار {m(k)} أرقام مختلفة من أصل {m(9)} أرقام متاحة.",
                f"الناتج هو {m(f'\\binom{{9}}{{{k}}} = {ans}')}.",
            ],
            f"انتبه: اختيار {m(f'\\binom{{10}}{{{k}}}')} يقع في فخ السماح بصفر في الخانة اليسرى!",
            diagram_en=svg_digit_slots([f"d_{i+1}" for i in range(k)], f"1 ≤ d₁ < … < d_{k} ≤ 9"),
        )

    # 5th Easy: strictly decreasing 3-digit positive integers 9 >= a > b > c >= 0 -> C(10, 3) = 120
    assert sum(1 for n in range(100, 1000) if int(str(n)[0]) > int(str(n)[1]) > int(str(n)[2])) == 120
    B.add_math(
        tp, "Easy", bp,
        f"How many three-digit positive integers {m('\\overline{abc}')} have **strictly decreasing** digits {m('a > b > c')}?",
        f"كم عدداً صحيحاً موجباً من ثلاث خانات {m('\\overline{abc}')} يحقق الترتيب **التنازلي القطعي** {m('a > b > c')}؟",
        120, [84, 90, 165, 210],
        f"Here {m(0)} **is** allowed as the units digit {m('c')}, and any {m(3)} distinct digits from {m('\\{0,1,\\dots,9\\}')} automatically have largest digit {m('a \\ge 2')}!",
        f"هنا **يُسمح** بظهور الصفر في خانة الآحاد {m('c')}، وأي {m(3)} أرقام مختلفة من {m('\\{0,\\dots,9\\}')} يكون أكبرها {m('a \\ge 2')} تلقائياً!",
        f"Choose any {m(3)} distinct digits from all {m(10)} digits {m('\\{0, 1, \\dots, 9\\}')} and place them in decreasing order!",
        [
            f"Unlike increasing numbers, {m('c = 0')} is valid (e.g. {m(210)}), and {m('a > b > c \\ge 0')} forces {m('a \\ge 2 \\neq 0')}.",
            f"Every {m(3)}-element subset of {m('\\{0, 1, \\dots, 9\\}')} yields a unique decreasing number {m('\\overline{abc}')}.",
            f"Compute {m('\\binom{10}{3} = \\frac{10 \\times 9 \\times 8}{6} = 120')}.",
        ],
        f"Compare carefully: strictly increasing {m('3')}-digit numbers equal {m('\\binom{9}{3} = 84')}, while strictly decreasing equal {m('\\binom{10}{3} = 120')}!",
        f"نختار أي {m(3)} أرقام مختلفة من المجموعة الكاملة {m('\\{0,1,\\dots,9\\}')} ونرتبها تنازلياً!",
        [
            f"يُسمح هنا بأن يكون {m('c = 0')}، وشرط {m('a > b > c')} يضمن تلقائياً أن {m('a \\ge 2')}.",
            f"كل اختيار لـ {m(3)} أرقام من {m(10)} يحدد عدداً وحيداً تنازلياً.",
            f"العدد هو {m('\\binom{10}{3} = 120')}.",
        ],
        f"مقارنة مهمة: المتزايدة قطعيّاً عددها {m(84)}، أما المتناقصة قطعيّاً فعددها {m(120)} لدخول الصفر!",
        diagram_en=svg_digit_slots(["a", "> b", "> c"], "Choose 3 from {0..9}"),
    )

    for k, max_d in [(2, 9), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8)]:
        ans = math.comb(max_d + k - 1, k)
        B.add_math(
            tp, "Medium", bp,
            f"How many {m(k)}-digit positive integers are formed using only digits from {m(f'\\{{1, 2, \\dots, {max_d}\\}}')} arranged in **non-decreasing** order ({m(f'1 \\le d_1 \\le \\cdots \\le d_{k} \\le {max_d}')})?",
            f"كم عدداً صحيحاً موجباً من {m(k)} خانات يتكون من أرقام المجموعة {m(f'\\{{1, 2, \\dots, {max_d}\\}}')} مرتبةً ترتيباً **غير متناقص** ({m(f'1 \\le d_1 \\le \\cdots \\le d_{k} \\le {max_d}')})؟",
            ans, [math.comb(max_d, k), math.comb(max_d + k, k), ans - max_d, ans + max_d],
            f"Use combinations with repetition {m(f'\\binom{{{max_d} + {k} - 1}}{{{k}}}')}.",
            f"استخدم قانون التوافيق مع التكرار {m(f'\\binom{{{max_d} + {k} - 1}}{{{k}}}')}.",
            f"Select {m(k)} digits with repetition from {m(max_d)} available nonzero digits via Stars and Bars!",
            [
                f"A non-decreasing sequence of length {m(k)} from {m(f'\\{{1,\\dots,{max_d}\\}}')} is uniquely determined by how many times each digit is chosen.",
                f"By Stars and Bars, there are {m(f'\\binom{{{max_d} + {k} - 1}}{{{k}}} = \\binom{{{max_d + k - 1}}}{{{k}}}')} choices.",
                f"Evaluating the binomial coefficient gives {m(ans)}.",
            ],
            f"Check: strictly increasing choices {m(f'\\binom{{{max_d}}}{{{k}}} = {math.comb(max_d, k)}')} are a proper subset of all {m(ans)} non-decreasing numbers.",
            f"نختار {m(k)} أرقام مع السماح بالتكرار من بين {m(max_d)} أرقام متاحة!",
            [
                f"بمجرد تحديد مجموعة الأرقام المختارة (مع تكراراتها)، يوجد ترتيب غير متناقص وحيد لها.",
                f"نطبق صيغة النجوم والفواصل: {m(f'\\binom{{{max_d} + {k} - 1}}{{{k}}} = \\binom{{{max_d + k - 1}}}{{{k}}}')}.",
                f"بحساب التوافيق نحصل على {m(ans)}.",
            ],
            f"تحقق: هذا العدد أكبر من حالة التزايد القطعي {m(math.comb(max_d, k))} لأنه يشمل تساوي الخانات.",
            diagram_en=svg_digit_slots([f"d_{i+1}" for i in range(k)], f"C({max_d+k-1}, {k})"),
        )

    for k in (2, 3, 4):
        ans = math.comb(10 + k - 1, k) - 1
        assert ans == sum(1 for n in range(10 ** (k - 1), 10 ** k) if list(str(n)) == sorted(str(n), reverse=True))
        B.add_math(
            tp, "Hard", bp,
            f"How many {m(k)}-digit positive integers have **non-increasing** digits from left to right ({m(f'9 \\ge d_1 \\ge \\cdots \\ge d_{k} \\ge 0')} with {m('d_1 \\ge 1')})?",
            f"كم عدداً صحيحاً موجباً من {m(k)} خانات تكون أرقامه **غير متزايدة** من اليسار إلى اليمين ({m(f'9 \\ge d_1 \\ge \\cdots \\ge d_{k} \\ge 0')} مع {m('d_1 \\ge 1')})؟",
            ans, [math.comb(10 + k - 1, k), math.comb(9 + k - 1, k), ans - 9, ans + 10],
            f"Choose {m(k)} digits with repetition from all {m(10)} digits {m('\\{0,\\dots,9\\}')}, then subtract the single all-zero string!",
            f"اختر {m(k)} أرقام مع التكرار من الأرقام العشرة {m('\\{0,\\dots,9\\}')}، ثم اطرح حالة الأصفار الكاملة الوحيدة!",
            f"Count multisets of size {m(k)} from {m('\\{0,\\dots,9\\}')} and exclude {m('00\\dots 0')}!",
            [
                f"Choosing {m(k)} digits with repetition from {m('\\{0,1,\\dots,9\\}')} and sorting descending gives {m(f'\\binom{{10 + {k} - 1}}{{{k}}} = \\binom{{{9 + k}}}{{{k}}} = {math.comb(9+k, k)}')} strings.",
                f"Every string has {m('d_1 \\ge 1')} **except** the single all-zero string {m('0' * k)}.",
                f"Subtract {m(1)}: {m(f'{math.comb(9+k, k)} - 1 = {ans}')}.",
            ],
            f"Trap check: forgetting to exclude {m('0' * k)} gives {m(ans + 1)}!",
            f"نحسب التوافيق مع التكرار من الأرقام العشرة {m('\\{0,\\dots,9\\}')} ثم نستبعد سلسلة الأصفار الوحيدة!",
            [
                f"عدد الاختيارات مع التكرار من {m(10)} أرقام هو {m(f'\\binom{{{9 + k}}}{{{k}}} = {math.comb(9+k, k)}')}.",
                f"الحالة الوحيدة التي تجعل {m('d_1 = 0')} هي اختيار الصفر {m(k)} مرات ({m('0' * k)}).",
                f"نطرح {m(1)} فنحصل على {m(ans)}.",
            ],
            f"انتبه: نسيان طرح حالة الأصفار يعطي الخيار الخاطئ {m(ans + 1)}!",
            diagram_en=svg_digit_slots([f"d_{i+1}" for i in range(k)], f"C({9+k},{k}) − 1"),
        )

    # 4th Hard: 3-digit mountain numbers a < b and b > c
    ans_mtn = sum(1 for n in range(100, 1000) if int(str(n)[0]) < int(str(n)[1]) and int(str(n)[1]) > int(str(n)[2]))
    assert ans_mtn == 240
    B.add_math(
        tp, "Hard", bp,
        f"A three-digit integer {m('\\overline{abc}')} is called a **peak number** if its middle digit is strictly larger than both neighbors ({m('a < b')} and {m('b > c')}). How many three-digit peak numbers exist?",
        f"يُسمى العدد الثلاثي {m('\\overline{abc}')} **عدداً قِمّياً** إذا كان رقمه الأوسط أكبر قطعيّاً من جاريه ({m('a < b')} و{m('b > c')}). كم عدداً ثلاثياً قِمّياً يوجد؟",
        240, [204, 210, 252, 285],
        f"Casework on the middle peak digit {m('b \\in \\{2, 3, \\dots, 9\\}')}: note {m('1 \\le a \\le b - 1')} while {m('0 \\le c \\le b - 1')}!",
        f"قسّم الحل بحسب قيمة الرقم الأوسط {m('b \\in \\{2,\\dots,9\\}')}؛ لاحظ أن {m('1 \\le a \\le b-1')} بينما {m('0 \\le c \\le b-1')}!",
        f"Fix the peak digit {m('b')} and multiply the {m('b - 1')} choices for {m('a')} by the {m('b')} choices for {m('c')}!",
        [
            f"For a given middle digit {m('b')} ({m('2 \\le b \\le 9')}), {m('a \\in \\{1,\\dots,b-1\\}')} has {m('b - 1')} choices and {m('c \\in \\{0,\\dots,b-1\\}')} has {m('b')} choices.",
            f"Sum {m('(b - 1)b')} for {m('b = 2, \\dots, 9')}: {m('2 + 6 + 12 + 20 + 30 + 42 + 56 + 72')}.",
            f"Adding (or using {m('2\\binom{10}{3} = 2 \\times 120')}) gives {m(240)}.",
        ],
        f"Elegant identity: {m('\\sum_{b=2}^9 2\\binom{b}{2} = 2\\binom{10}{3} = 240')}!",
        f"نثبّت رقم القمة {m('b')} فنضرب {m('b - 1')} خياراً للخانة {m('a')} في {m('b')} خياراً للخانة {m('c')}!",
        [
            f"لكل قيمة {m('2 \\le b \\le 9')}، توجد {m('b - 1')} قيم لـ {m('a')} (من {m(1)} إلى {m('b-1')}) و{m('b')} قيم لـ {m('c')} (من {m(0)} إلى {m('b-1')}).",
            f"نجمع {m('1\\cdot 2 + 2\\cdot 3 + \\cdots + 8\\cdot 9 = 2 + 6 + 12 + 20 + 30 + 42 + 56 + 72')}.",
            f"المجموع الكلي يساوي {m(240)} عدداً قِمّياً.",
        ],
        f"تحقق جميل بمتطابقة عصا الهوكي: {m('2\\sum_{b=2}^9 \\binom{b}{2} = 2\\binom{10}{3} = 240')}!",
        diagram_en=svg_digit_slots(["a ≥ 1", "b (peak)", "c ≥ 0"], "a < b > c"),
    )

    # 2. nsmo_g89_palindrome_divisibility_11 (5E, 6M, 4H) — SVG: svg_digital_clock / svg_digit_slots
    bp = "nsmo_g89_palindrome_divisibility_11"
    easy_11_exact = [
        ("72d83", 11),  # d=0 -> 72083 = 11 * 6553
        ("59d47", 11),  # d=1 -> 59147 = 11 * 5377
        ("68d43", 11),  # d=3 -> 68343 = 11 * 6213
        ("475d", 99),   # d=2 -> 4752 = 99 * 48
        ("732d", 99),   # d=6 -> 7326 = 99 * 74
    ]
    for pat, mod_m in easy_11_exact:
        sols = [d for d in range(10) if int(pat.replace("d", str(d))) % mod_m == 0]
        assert len(sols) == 1, f"{pat} mod {mod_m} -> {sols}"
        ans = sols[0]
        val_full = int(pat.replace("d", str(ans)))
        disp = pat
        B.add_math(
            tp, "Easy", bp,
            f"Find the single digit {m('d \\in \\{0,1,\\dots,9\\}')} such that the integer {m(f'\\overline{{{disp}}}')} is divisible by {m(mod_m)}.",
            f"أوجد الرقم الوحيد {m('d \\in \\{0,1,\\dots,9\\}')} الذي يجعل العدد {m(f'\\overline{{{disp}}}')} قابلاً للقسمة على {m(mod_m)}.",
            ans, [(ans + 2) % 10, (ans + 5) % 10, (ans + 7) % 10, (ans + 9) % 10],
            f"Use the alternating digit-sum test for {m(11)} ({'and digit-sum test for 9' if mod_m == 99 else 'odd positions minus even positions'}).",
            f"طبّق قاعدة المجموع المتناوب للعدد {m(11)}{' مع مجموع الخانات للعدد 9' if mod_m == 99 else ''}.",
            f"Set the alternating sum of digits congruent to {m('0 \\pmod{11}')}!",
            [
                f"Compute the alternating sum of the digits of {m(f'\\overline{{{disp}}}')}.",
                f"Require the alternating sum to be a multiple of {m(11)}{' and the digit sum to be a multiple of 9' if mod_m == 99 else ''}.",
                f"Since {m('0 \\le d \\le 9')}, the unique valid digit is {m(f'd = {ans}')}.",
            ],
            f"Division check: {m(f'{val_full} = {mod_m} \\times {val_full // mod_m}')}!",
            f"نجعل المجموع المتناوب للخانات مضاعفاً للعدد {m(11)} ضمن النطاق {m('0 \\le d \\le 9')}!",
            [
                f"نكتب المجموع المتناوب لخانات العدد {m(f'\\overline{{{disp}}}')} بدلالة {m('d')}.",
                f"نساويه بمضاعف للعدد {m(11)}{' ونتحقق من القسمة على 9' if mod_m == 99 else ''}.",
                f"القيمة الوحيدة الممكنة للرقم هي {m(f'd = {ans}')}.",
            ],
            f"تحقق بالقسمة المباشرة: {m(f'{val_full} \\div {mod_m} = {val_full // mod_m}')}.",
            diagram_en=svg_digit_slots(list(pat), f"Divisible by {mod_m}"),
        )

    for div_m in (3, 4, 6, 7, 8, 9):
        ans = sum(1 for n in range(100, 1000) if str(n) == str(n)[::-1] and n % div_m == 0)
        B.add_math(
            tp, "Medium", bp,
            f"How many three-digit palindromes {m('\\overline{aba}')} (where {m('a \\ge 1')}) are divisible by {m(div_m)}?",
            f"كم عدداً متناظراً من ثلاث خانات {m('\\overline{aba}')} (حيث {m('a \\ge 1')}) يقبل القسمة على {m(div_m)}؟",
            ans, [ans + 3, max(1, ans - 2), 90 // div_m + 4, ans + 6],
            f"Write {m('\\overline{aba} = 101a + 10b')} and test which pairs {m('(a, b)')} with {m('1 \\le a \\le 9,\\; 0 \\le b \\le 9')} satisfy {m(f'101a + 10b \\equiv 0 \\pmod{{{div_m}}}')}.",
            f"اكتب {m('\\overline{aba} = 101a + 10b')} وافحص الأزواج {m('(a, b)')} التي تحقق {m(f'101a + 10b \\equiv 0 \\pmod{{{div_m}}}')}.",
            f"Reduce {m('101a + 10b')} modulo {m(div_m)} and count valid choices of {m('b \\in \\{0,\\dots,9\\}')} for each leading digit {m('a')}!",
            [
                f"Every three-digit palindrome has the form {m('\\overline{aba} = 101a + 10b')} with {m('a \\in \\{1,\\dots,9\\}')} and {m('b \\in \\{0,\\dots,9\\}')}.",
                f"Reduce modulo {m(div_m)}: {m(f'{101 % div_m}a + {10 % div_m}b \\equiv 0 \\pmod{{{div_m}}}')}.",
                f"Summing the valid {m('b')}-values across all allowed digits {m('a')} yields exact {m(ans)} palindromes.",
            ],
            f"There are {m('9 \\times 10 = 90')} three-digit palindromes in total, of which {m(ans)} are multiples of {m(div_m)}.",
            f"نختزل المقدار {m('101a + 10b')} بالمقاس {m(div_m)} ونعدّ قيم {m('b')} المسموحة لكل قيمة من {m('a')}!",
            [
                f"يكتب المتناظر الثلاثي بالصورة {m('101a + 10b')} حيث {m('1 \\le a \\le 9')} و{m('0 \\le b \\le 9')}.",
                f"بأخذ الباقي على {m(div_m)}: {m(f'{101 % div_m}a + {10 % div_m}b \\equiv 0 \\pmod{{{div_m}}}')}.",
                f"بجمع الحالات الممكنة نحصل على {m(ans)} عدداً متناظراً.",
            ],
            f"تحقق: من أصل {m(90)} متناظراً ثلاثياً، يوجد بالضبط {m(ans)} تقبل القسمة على {m(div_m)}.",
            diagram_en=svg_digital_clock("a:b:a", f"aba ÷ {div_m}"),
        )

    for div_m in (11, 9, 99, 45):
        ans = sum(1 for a in range(1, 10) for b in range(10) for c in range(10) if (10001 * a + 1010 * b + 100 * c) % div_m == 0)
        B.add_math(
            tp, "Hard", bp,
            f"How many five-digit palindromes {m('\\overline{abcba}')} (with {m('a \\ge 1')}) are divisible by {m(div_m)}?",
            f"كم عدداً متناظراً من خمس خانات {m('\\overline{abcba}')} (حيث {m('a \\ge 1')}) يقبل القسمة على {m(div_m)}؟",
            ans, [ans + 9, max(1, ans - 9), 900 // div_m + 5, ans * 2],
            f"Check how {m('a, b, c')} behave under the divisibility rule(s) for {m(div_m)}!",
            f"افحص القيود التي تفرضها قابلية القسمة على {m(div_m)} على الأرقام {m('a, b, c')}!",
            f"Fix {m('(a, b)')} (or {m('a')}) and count how many middle digits {m('c \\in \\{0,\\dots,9\\}')} satisfy the congruence modulo {m(div_m)}!",
            [
                f"Write {m('\\overline{abcba}')} with {m('a \\in \\{1,\\dots,9\\}')} and {m('b, c \\in \\{0,\\dots,9\\}')} ({m(900)} five-digit palindromes total).",
                f"Apply the modular condition for {m(div_m)} (digit sum {m('2a + 2b + c')} for {m(9)}, alternating sum {m('2a - 2b + c')} for {m(11)}, and {m('a \\in \\{5\\}')} for {m(45)}).",
                f"Counting all valid triples {m('(a, b, c)')} gives {m(ans)}.",
            ],
            f"Out of {m(900)} five-digit palindromes, exact {m(ans)} are multiples of {m(div_m)}.",
            f"نطبّق شروط القسمة على {m(div_m)} على الخانات الثلاث المستقلة {m('(a, b, c)')}!",
            [
                f"يتحدد المتناظر الخماسي بالثلاثية {m('(a, b, c)')} وعددها الكلي {m('9 \\times 10 \\times 10 = 900')}.",
                f"نطبق شرط القسمة على {m(div_m)} لتحديد قيم {m('c')} الموافقة لكل زوج {m('(a, b)')}.",
                f"ينتج بالضبط {m(ans)} متناظراً خماسياً.",
            ],
            f"تحقق شامل: عدّ الثلاثيات {m('(a,b,c)')} برمجياً وجبرياً يؤكد القيمة {m(ans)}.",
            diagram_en=svg_digit_slots(["a", "b", "c", "b", "a"], f"÷ {div_m}"),
        )

    # 3. nsmo_g89_linear_diophantine_stamps (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g89_linear_diophantine_stamps"
    for a, b, ctx in [(3, 7, "arcade tokens"), (4, 9, "postage stamps"), (5, 7, "gift vouchers"), (6, 11, "gold coins"), (7, 10, "cargo weights")]:
        ans = a * b - a - b
        B.add_math(
            tp, "Easy", bp,
            f"Using only {ctx} worth {m(a)} units and {m(b)} units, what is the **largest** positive integer total that **cannot** be formed?",
            f"باستخدام فئتين فقط قيمتاهما {m(a)} و{m(b)} وحدات، ما **أكبر** مجموع صحيح موجب **لا يمكن** تكوينه؟",
            ans, [a * b, ans + 1, ans - a, a * b - a],
            f"Since {m(f'\\gcd({a}, {b}) = 1')}, apply Frobenius's formula {m('ab - a - b')}.",
            f"بما أن {m(f'\\gcd({a}, {b}) = 1')}، طبّق صيغة فروبينيوس {m('ab - a - b')}.",
            f"For two coprime denominations {m('a')} and {m('b')}, the largest unattainable integer is {m('ab - a - b')}!",
            [
                f"Verify {m(f'\\gcd({a}, {b}) = 1')}.",
                f"Compute {m(f'{a} \\times {b} - {a} - {b} = {a*b} - {a+b} = {ans}')}.",
                f"Every integer {m(f'\\ge {ans + 1}')} can be expressed as {m(f'{a}x + {b}y')} with {m('x, y \\ge 0')}.",
            ],
            f"Quick check: {m(ans + 1)} through {m(ans + a)} are {m(a)} consecutive attainable totals!",
            f"لفئتين أوليتين نسبياً {m('a')} و{m('b')} يكون أكبر مجموع مستحيل هو {m('ab - a - b')}!",
            [
                f"بما أن {m(f'\\gcd({a}, {b}) = 1')} نطبق القانون مباشرة.",
                f"نحسب: {m(f'{a} \\times {b} - {a} - {b} = {ans}')}.",
                f"جميع الأعداد الصحيحة الأكبر من {m(ans)} قابلة للتكوين.",
            ],
            f"تحقق: العدد {m(ans)} لا يكتب بالصورة {m(f'{a}x + {b}y')} مع {m('x, y \\ge 0')}.",
            diagram_en=svg_number_strip([f"{a}x+{b}y", f"{ans} ✗", f"{ans+1} ✓", "… ✓"]),
        )

    for a, b, N in [(3, 5, 60), (4, 7, 84), (5, 8, 120), (3, 7, 75), (5, 9, 135), (4, 9, 108)]:
        ans = sum(1 for x in range(N // a + 1) if (N - a * x) % b == 0)
        B.add_math(
            tp, "Medium", bp,
            f"How many ordered pairs {m('(x, y)')} of **non-negative** integers ({m('x \\ge 0,\\; y \\ge 0')}) satisfy {m(f'{a}x + {b}y = {N}')}?",
            f"كم زوجاً مرتباً {m('(x, y)')} من الأعداد الصحيحة **غير السالبة** ({m('x \\ge 0,\\; y \\ge 0')}) يحقق المعادلة {m(f'{a}x + {b}y = {N}')}؟",
            ans, [ans - 1, ans - 2 if ans > 2 else ans + 2, ans + 1, N // (a * b)],
            f"Find one solution (such as {m('y = 0')} or smallest {m('y \\ge 0')}), then step {m('y')} by {m(a)} and {m('x')} by {m(f'-{b}')}!",
            f"أوجد حلاً واحداً أولاً ثم غيّر {m('y')} بمقدار {m(a)} و{m('x')} بمقدار {m(f'-{b}')}!",
            f"Step through solutions using {m(f'(x - {b}t,\\; y + {a}t)')} while keeping both coordinates {m('\\ge 0')}!",
            [
                f"In {m(f'{a}x + {b}y = {N}')}, {m(f'{b}y \\equiv {N} \\pmod{{{a}}}')} fixes {m('y')} modulo {m(a)}.",
                f"Valid values of {m('y')} increase in steps of {m(a)} inside {m(f'0 \\le y \\le \\lfloor {N}/{b} \\rfloor = {N // b}')}.",
                f"Counting those steps yields exact {m(ans)} non-negative pairs {m('(x, y)')}.",
            ],
            f"Watch the boundary: **positive** solutions ({m('x,y \\ge 1')}) may exclude {m('x=0')} or {m('y=0')}, whereas **non-negative** includes them!",
            f"ننتقل بين الحلول بالخطوة {m(f'(x - {b}t,\\; y + {a}t)')} مع الحفاظ على {m('x, y \\ge 0')}!",
            [
                f"من المعادلة {m(f'{a}x + {b}y = {N}')} تتغير قيم {m('y')} الصحيحة بقفزات مقدارها {m(a)}.",
                f"تقع قيم {m('y')} المسموحة في الفترة {m(f'0 \\le y \\le {N // b}')}.",
                f"عدد القيم الصحيحة الناتجة يساوي {m(ans)} زوجاً مرتباً.",
            ],
            f"انتبه للحدود: الحلول **غير السالبة** تقبل {m('x=0')} أو {m('y=0')} إن تحققت القسمة!",
            diagram_en=svg_number_strip([f"{a}x+{b}y={N}", f"Δx=−{b}", f"Δy=+{a}", "# = ?"]),
        )

    for a, b in [(5, 9), (7, 11), (6, 13), (8, 11)]:
        ans = (a - 1) * (b - 1) // 2
        reach = {a * x + b * y for x in range(b + 1) for y in range(a + 1)}
        assert ans == sum(1 for v in range(1, a * b) if v not in reach)
        B.add_math(
            tp, "Hard", bp,
            f"How many **positive integers** in total **cannot** be written in the form {m(f'{a}x + {b}y')} for non-negative integers {m('x, y \\ge 0')}?",
            f"كم **عدداً صحيحاً موجباً** في المجموع **لا يمكن** كتابته على الصورة {m(f'{a}x + {b}y')} لعددين صحيحين غير سالبين {m('x, y \\ge 0')}؟",
            ans, [(a - 1) * (b - 1), a * b - a - b, ans + 2, ans - 2],
            f"For coprime {m('a, b')}, exact half of the integers in {m('[0, ab - a - b]')} are unattainable: {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"لأي عددين أوليين نسبياً {m('a, b')}، عدد الأعداد الموجبة المستحيلة يساوي {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"Apply Sylvester's coin-problem count {m('\\frac{(a - 1)(b - 1)}{2}')}!",
            [
                f"Since {m(f'\\gcd({a}, {b}) = 1')}, pairing {m('k')} with {m(f'{a*b - a - b} - k')} matches each attainable integer in {m(f'[0, {a*b - a - b}]')} with an unattainable one.",
                f"Thus the count of unattainable positive integers is {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a-1} \\times {b-1}}}{{2}}')}.",
                f"Evaluating gives {m(ans)} unattainable positive integers.",
            ],
            f"Don't confuse the **count** of impossible integers ({m(ans)}) with the **largest** impossible integer ({m(a*b - a - b)})!",
            f"نطبّق مبرهنة سلفستر لعدد الأعداد الموجبة غير القابلة للتكوين {m('\\frac{(a-1)(b-1)}{2}')}!",
            [
                f"بما أن {m(f'\\gcd({a}, {b}) = 1')}، تتزاوج الأعداد في الفترة {m(f'[0, {a*b-a-b}]')} إلى أزواج مجموعها {m(a*b-a-b)} أحدها ممكن والآخر مستحيل.",
                f"إذن عدد الأعداد الموجبة المستحيلة يساوي {m(f'\\frac{{({a}-1)({b}-1)}}{{2}}')}.",
                f"بحساب المقدار نجد {m(ans)}.",
            ],
            f"انتبه لعدم الخلط بين **عدد** القيم المستحيلة ({m(ans)}) و**أكبر** قيمة مستحيلة ({m(a*b - a - b)})!",
            diagram_en=svg_number_strip([f"a={a}, b={b}", "(a−1)(b−1)/2", f"max={a*b-a-b}", "# = ?"]),
        )

    # 4. nsmo_g89_unit_fraction_split (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g89_unit_fraction_split"
    for n, x0 in [(6, 9), (8, 12), (10, 15)]:
        ans = (n * x0) // (x0 - n)
        assert Fraction(1, n) == Fraction(1, x0) + Fraction(1, ans)
        B.add_math(
            tp, "Easy", bp,
            f"Find the positive integer {m('y')} that satisfies the unit-fraction equation {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{{x0}}} + \\frac{{1}}{{y}}')}.",
            f"أوجد العدد الصحيح الموجب {m('y')} الذي يحقق معادلة الكسور الوحدية {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{{x0}}} + \\frac{{1}}{{y}}')}.",
            ans, [x0 + n, x0 * n, ans + n, ans - 2],
            f"Subtract {m(f'\\frac{{1}}{{y}} = \\frac{{1}}{{{n}}} - \\frac{{1}}{{{x0}}}')} using a common denominator.",
            f"اطرح الكسرين: {m(f'\\frac{{1}}{{y}} = \\frac{{1}}{{{n}}} - \\frac{{1}}{{{x0}}}')} بتوحيد المقامات.",
            f"Isolate {m('\\frac{1}{y}')} and take the reciprocal!",
            [
                f"Write {m(f'\\frac{{1}}{{y}} = \\frac{{1}}{{{n}}} - \\frac{{1}}{{{x0}}} = \\frac{{{x0} - {n}}}{{{n} \\times {x0}}} = \\frac{{{x0 - n}}}{{{n*x0}}}')}.",
                f"Simplify the fraction to {m(f'\\frac{{1}}{{{ans}}}')}.",
                f"Therefore {m(f'y = {ans}')}.",
            ],
            f"Check: {m(f'({x0} - {n})({ans} - {n}) = {x0 - n} \\times {ans - n} = {n*n} = {n}^2')}!",
            f"نعزل {m('\\frac{1}{y}')} بتوحيد المقامات ثم نقلب الكسر الناتج!",
            [
                f"نحسب {m(f'\\frac{{1}}{{y}} = \\frac{{{x0} - {n}}}{{{n} \\times {x0}}} = \\frac{{{x0 - n}}}{{{n*x0}}}')}.",
                f"باختصار الكسر نحصل على {m(f'\\frac{{1}}{{{ans}}}')}.",
                f"إذن {m(f'y = {ans}')}.",
            ],
            f"تحقق: {m(f'\\frac{{1}}{{{x0}}} + \\frac{{1}}{{{ans}}} = \\frac{{1}}{{{n}}}')}.",
        )

    for n in (8, 10):
        ans = (n + 1) ** 2
        B.add_math(
            tp, "Easy", bp,
            f"Positive integers {m('x')} and {m('y')} satisfy {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}. What is the **maximum** possible value of {m('x + y')}?",
            f"عددان صحيحان موجبان {m('x')} و{m('y')} يحققان {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}. ما **أكبر** قيمة ممكنة للمجموع {m('x + y')}؟",
            ans, [n * n + n, 4 * n, ans - 1, n * n + 2 * n],
            f"Factor {m(f'(x - {n})(y - {n}) = {n*n}')}; to maximize the sum of two positive factors of {m(n*n)}, choose {m(f'1 \\times {n*n}')}!",
            f"حلّل المعادلة إلى {m(f'(x - {n})(y - {n}) = {n*n}')}؛ لتكبير مجموع عاملين موجبين اختر الطرفين {m(f'1 \\times {n*n}')}!",
            f"Use {m(f'(x - {n})(y - {n}) = {n}^2')} and pick the most extreme divisor pair {m(f'(1, {n*n})')}!",
            [
                f"Rewrite as {m(f'(x - {n})(y - {n}) = {n*n}')}, so {m(f'x + y = 2({n}) + d + \\frac{{{n*n}}}{{d}}')}.",
                f"The sum {m(f'd + {n*n}/d')} is maximized at {m('d = 1')}, giving {m(f'x = {n+1}')} and {m(f'y = {n + n*n}')}.",
                f"Add them: {m(f'{n+1} + {n + n*n} = {ans} = ({n}+1)^2')}.",
            ],
            f"Check: {m(f'\\frac{{1}}{{{n+1}}} + \\frac{{1}}{{{n*(n+1)}}} = \\frac{{{n} + 1}}{{{n}({n}+1)}} = \\frac{{1}}{{{n}}}')}!",
            f"نحوّل المعادلة إلى {m(f'(x - {n})(y - {n}) = {n*n}')} ونختار أبعد قاسمين {m(1)} و{m(n*n)}!",
            [
                f"بوضع {m(f'd = x - {n}')} نجد {m(f'x + y = {2*n} + d + {n*n}/d')}.",
                f"أكبر مجموع لقاسمين موجبين للعدد {m(n*n)} يتحقق عند {m(f'1 + {n*n}')}.",
                f"إذن أكبر قيمة لـ {m('x + y')} هي {m(f'{2*n} + 1 + {n*n} = {ans}')}.",
            ],
            f"تحقق: عند {m(f'x = {n+1}, y = {n*(n+1)}')} يتحقق الكسر تماماً ومجموعهما {m(ans)}.",
        )

    for n, sq_fac in [(6, "2^2 \\times 3^2"), (8, "2^6"), (10, "2^2 \\times 5^2"), (14, "2^2 \\times 7^2"), (15, "3^2 \\times 5^2"), (18, "2^2 \\times 3^4")]:
        ans = len(_divisors(n * n))
        B.add_math(
            tp, "Medium", bp,
            f"How many **ordered pairs** {m('(x, y)')} of positive integers satisfy {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}?",
            f"كم **زوجاً مرتباً** {m('(x, y)')} من الأعداد الصحيحة الموجبة يحقق {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}؟",
            ans, [len(_divisors(n)), (ans + 1) // 2, ans - 1, ans + 3],
            f"Rewrite as {m(f'(x - {n})(y - {n}) = {n}^2 = {n*n}')} and count positive divisors of {m(n*n)}.",
            f"أعد كتابة المعادلة على الصورة {m(f'(x - {n})(y - {n}) = {n*n}')} واحسب عدد قواسم {m(n*n)} الموجبة.",
            f"Count positive divisors {m(f'\\tau({n}^2)')} via {m(f'(x - {n})(y - {n}) = {n*n}')}!",
            [
                f"Clearing denominators and adding {m(f'{n}^2')} gives {m(f'(x - {n})(y - {n}) = {n*n}')}.",
                f"Prime-factorize {m(f'{n}^2 = {n*n} = {sq_fac}')}.",
                f"The number of positive divisors (and hence ordered pairs) is {m(ans)}.",
            ],
            f"Every divisor {m(f'd \\mid {n*n}')} gives {m(f'x = {n} + d > {n}')} and {m(f'y = {n} + {n*n}/d > {n}')}.",
            f"نحلّل المعادلة إلى {m(f'(x - {n})(y - {n}) = {n*n}')} فيكون الجواب {m(f'\\tau({n*n})')}!",
            [
                f"بضرب الطرفين في {m(f'{n}xy')} وإكمال المستطيل نجد {m(f'(x - {n})(y - {n}) = {n*n}')}.",
                f"نحلّل {m(f'{n*n} = {sq_fac}')}.",
                f"عدد القواسم الموجبة للعدد {m(n*n)} هو {m(ans)} زوجاً مرتباً.",
            ],
            f"تحقق: العدد فردي دائماً لأن {m(n*n)} مربع كامل!",
            diagram_en=svg_factor_tree(f"n²={n*n}", "x−n = d", f"y−n = {n*n}/d", "τ(n²)", f"={ans}"),
        )

    for n, sq_fac in [(12, "2^4 \\times 3^2"), (20, "2^4 \\times 5^2"), (24, "2^6 \\times 3^2"), (30, "2^2 \\times 3^2 \\times 5^2")]:
        t_sq = len(_divisors(n * n))
        ans = (t_sq + 1) // 2
        B.add_math(
            tp, "Hard", bp,
            f"How many pairs {m('(x, y)')} of positive integers with {m('x \\le y')} satisfy {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}?",
            f"كم زوجاً {m('(x, y)')} من الأعداد الصحيحة الموجبة يحقق {m('x \\le y')} والمعادلة {m(f'\\frac{{1}}{{{n}}} = \\frac{{1}}{{x}} + \\frac{{1}}{{y}}')}؟",
            ans, [t_sq, (t_sq - 1) // 2, ans + 2, len(_divisors(n))],
            f"First compute {m(f'\\tau({n}^2) = {t_sq}')}; don't forget the symmetric solution {m(f'x = y = {2*n}')} before halving!",
            f"احسب أولاً {m(f'\\tau({n}^2) = {t_sq}')}؛ وتذكّر أن الزوج المتماثل {m(f'x = y = {2*n}')} يُحسب مرة واحدة قبل القسمة على {m(2)}!",
            f"Count ordered solutions {m(f'\\tau({n}^2)')} and apply {m('\\frac{\\tau(n^2) + 1}{2}')} for {m('x \\le y')}!",
            [
                f"From {m(f'(x - {n})(y - {n}) = {n}^2 = {sq_fac}')}, there are {m(f'\\tau({n}^2) = {t_sq}')} ordered pairs.",
                f"One pair has {m(f'x = y = {2*n}')}, while the other {m(t_sq - 1)} pairs split equally between {m('x < y')} and {m('x > y')}.",
                f"Thus {m('x \\le y')} holds for {m(f'1 + \\frac{{{t_sq} - 1}}{{2}} = \\frac{{{t_sq} + 1}}{{2}} = {ans}')} pairs.",
            ],
            f"Notice {m((t_sq - 1) // 2)} counts strictly {m('x < y')}, missing {m(f'({2*n}, {2*n})')}!",
            f"نحسب {m(f'\\tau({n}^2) = {t_sq}')} ثم نستخدم الصيغة {m('\\frac{\\tau(n^2) + 1}{2}')} لأن {m('x = y')} مشمول!",
            [
                f"من التحليل {m(f'{n}^2 = {sq_fac}')} نجد عدد الأزواج المرتبة {m(t_sq)}.",
                f"الزوج المتماثل {m(f'({2*n}, {2*n})')} يحقق {m('x \\le y')}، وبقية الـ {m(t_sq - 1)} زوجاً يُؤخذ نصفها.",
                f"إذن العدد يساوي {m(f'\\frac{{{t_sq} + 1}}{{2}} = {ans}')}.",
            ],
            f"انتبه: الإجابة {m((t_sq - 1) // 2)} تغفل الحل المتماثل {m(f'x = y = {2*n}')}!",
            diagram_en=svg_factor_tree(f"n²={n*n}", f"τ={t_sq}", "x ≤ y", "(τ+1)/2", str(ans)),
        )

    # 5. nsmo_g89_concatenated_digit_stream (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g89_concatenated_digit_stream"
    for N in (50, 85, 120, 250, 400):
        ans = len("".join(str(i) for i in range(1, N + 1)))
        B.add_math(
            tp, "Easy", bp,
            f"If all positive integers from {m(1)} through {m(N)} inclusive are written side by side with no spaces ({m(f'1234567891011\\dots{N}')}), how many digits are written in total?",
            f"إذا كُتبت جميع الأعداد الصحيحة الموجبة من {m(1)} إلى {m(N)} متجاورةً بلا فراغات ({m(f'1234567891011\\dots{N}')})، فكم خانة (رقماً) كُتبت في المجموع؟",
            ans, [ans - 1, ans + 2, N * len(str(N)), ans - 9],
            f"Group by digit length: {m('1\\text{–}9')} ({m(9)} numbers), {m('10\\text{–}99')} ({m(90)} numbers), and {m('100\\text{–}' + str(N))} if {m('N \\ge 100')}.",
            f"قسّم الأعداد حسب عدد خاناتها: من {m(1)} إلى {m(9)}، ثم من {m(10)} إلى {m(99)}، ثم من {m(100)} فصاعداً.",
            f"Sum digit counts block by block (watch the inclusive fencepost {m('b - a + 1')})!",
            [
                f"One-digit numbers {m('1\\text{–}9')} contribute {m('9 \\times 1 = 9')} digits.",
                f"Two-digit numbers contribute {m(f'{min(N, 99) - 9} \\times 2 = {(min(N, 99) - 9) * 2}')} digits" + (f", and three-digit numbers {m(f'100\\text{{–}}{N}')} contribute {m(f'({N} - 99) \\times 3 = {(N - 99)*3}')} digits." if N >= 100 else "."),
                f"Adding the blocks gives {m(ans)} digits in total.",
            ],
            f"Fencepost check: from {m(10)} to {m(min(N, 99))} inclusive is {m(min(N, 99) - 10 + 1)}, not {m(min(N, 99) - 10)}!",
            f"نجمع عدد الخانات لكل فئة مع الانتباه لقاعدة العد الشامل {m('b - a + 1')}!",
            [
                f"الأعداد الأحادية {m('1\\text{–}9')} تعطي {m(9)} خانات.",
                f"الأعداد الثنائية تعطي {m((min(N, 99) - 9) * 2)} خانة" + (f"، والثلاثية من {m(100)} إلى {m(N)} تعطي {m((N - 99)*3)} خانة." if N >= 100 else "."),
                f"المجموع الكلي للخانات هو {m(ans)}.",
            ],
            f"تحقق: تذكّر دائماً إضافة {m(1)} عند حساب عدد الأعداد من {m('a')} إلى {m('b')}!",
            diagram_en=svg_number_strip(["1..9 (9)", "10..99", f"..{N}", "Digits=?"]),
        )

    stream_full = "".join(str(i) for i in range(1, 400))
    for K in (125, 168, 210, 270, 351, 500):
        ans = int(stream_full[K - 1])
        if K <= 189:
            rem = K - 9
            num = 10 + (rem - 1) // 2
            pos_idx = (rem - 1) % 2
        else:
            rem = K - 189
            num = 100 + (rem - 1) // 3
            pos_idx = (rem - 1) % 3
        assert int(str(num)[pos_idx]) == ans
        dists = [int(c) for c in str(num) if int(c) != ans] + [(ans + 1) % 10, (ans + 3) % 10, (ans + 7) % 10]
        B.add_math(
            tp, "Medium", bp,
            f"The positive integers are concatenated in order to form the infinite digit string {m('12345678910111213\\dots')}. What is the {m(K)}-th digit from the left?",
            f"كُتبت الأعداد الصحيحة الموجبة متتاليةً لتشكّل السلسلة غير المنتهية {m('12345678910111213\\dots')}. ما الرقم الواقع في المرتبة {m(K)} من اليسار؟",
            ans, dists,
            f"Subtract {m(9)} digits for {m('1\\text{–}9')} (and {m(180)} digits for {m('10\\text{–}99')} if {m('K > 189')}) to locate the exact integer!",
            f"اطرح {m(9)} خانات للأعداد الأحادية (و{m(180)} خانة للأعداد الثنائية إذا كان {m('K > 189')}) لتحديد العدد بدقة!",
            f"Peel off completed digit-length blocks, then divide by the digit width!",
            [
                f"Subtracting earlier digit blocks leaves position {m(rem)} inside the {'two-digit block starting at 10' if K <= 189 else 'three-digit block starting at 100'}.",
                f"Dividing {m(f'{rem} - 1 = {rem - 1}')} by {m(2 if K <= 189 else 3)} lands on the integer {m(num)} at digit index {m(pos_idx + 1)} (from left).",
                f"The {m(pos_idx + 1)}-th digit of {m(num)} is {m(ans)}.",
            ],
            f"Off-by-one check: the digits of {m(num)} sit right around index {m(K)}, and index {m(K)} is {m(ans)}!",
            f"نطرح كتل الخانات المكتملة ثم نقسم الفائض على طول الخانة لتحديد العدد المستهدف!",
            [
                f"بعد طرح الكتل السابقة يتبقى الموضع {m(rem)} داخل {'الأعداد الثنائية بدءاً من 10' if K <= 189 else 'الأعداد الثلاثية بدءاً من 100'}.",
                f"القسمة تحدد أن الخانة تقع داخل العدد {m(num)} في موضعه رقم {m(pos_idx + 1)} من اليسار.",
                f"إذن الرقم المطلوب هو {m(ans)}.",
            ],
            f"تحقق: فحص الخانات المجاورة للعدد {m(num)} يؤكد أن الخانة رقم {m(K)} هي {m(ans)}.",
            diagram_en=svg_number_strip(["1..9: 9", "10..99: 180", f"#{K}", f"in {num}"]),
        )

    for D, pages in [(642, 250), (1089, 399)]:
        assert len("".join(str(i) for i in range(1, pages + 1))) == D
        B.add_math(
            tp, "Hard", bp,
            f"A printer uses exact {m(D)} individual digits to number every page of a manual consecutively starting from page {m(1)}. How many pages does the manual have?",
            f"استخدمت مطبعة بالضبط {m(D)} رقماً مفرداً لترقيم جميع صفحات كتيب بالتسلسل بدءاً من الصفحة {m(1)}. كم صفحة في هذا الكتيب؟",
            pages, [pages - 1, pages + 1, D // 3, pages + 30],
            f"Pages {m('1\\text{–}99')} use {m('9 + 180 = 189')} digits; each page from {m(100)} onward uses {m(3)} digits!",
            f"تستهلك الصفحات {m('1\\text{–}99')} ما مجموعه {m('9 + 180 = 189')} رقماً، وكل صفحة من {m(100)} فصاعداً تستهلك {m(3)} أرقام!",
            f"Subtract {m(189)} digits for pages {m('1\\text{–}99')}, divide the remaining digits by {m(3)}, and add {m(99)}!",
            [
                f"Pages {m('1\\text{–}9')} use {m(9)} digits and pages {m('10\\text{–}99')} use {m(180)} digits ({m(189)} total).",
                f"Remaining digits for three-digit pages: {m(f'{D} - 189 = {D - 189}')}, giving {m(f'({D - 189}) / 3 = {(D - 189)//3}')} three-digit pages.",
                f"Add the first {m(99)} pages: {m(f'99 + {(D - 189)//3} = {pages}')} pages.",
            ],
            f"Check: {m(f'9 + 180 + 3 \\times ({pages} - 99) = 189 + {3*(pages - 99)} = {D}')}!",
            f"نطرح {m(189)} رقماً لأول {m(99)} صفحة، ثم نقسم الباقي على {m(3)} ونضيف {m(99)}!",
            [
                f"أول {m(99)} صفحة تستهلك {m('9 + 180 = 189')} رقماً.",
                f"يتبقى {m(f'{D} - 189 = {D - 189}')} رقماً، وبقسمتها على {m(3)} نجد {m((D - 189)//3)} صفحة ثلاثية الخانات.",
                f"إجمالي عدد الصفحات {m(f'99 + {(D - 189)//3} = {pages}')} صفحة.",
            ],
            f"تحقق: لا تنسَ الجمع مع {m(99)} بدلاً من {m(100)} (لأن الصفحة {m(100)} هي أول صفحة ثلاثية)!",
        )

    even_stream = "".join(str(2 * i) for i in range(1, 200))
    ans_ev = int(even_stream[149])
    B.add_math(
        tp, "Hard", bp,
        f"All positive **even** integers are written consecutively to form {m('246810121416\\dots')}. What is the {m(150)}-th digit from the left?",
        f"كُتبت جميع الأعداد الصحيحة الموجبة **الزوجية** متتاليةً لتشكّل السلسلة {m('246810121416\\dots')}. ما الرقم الواقع في المرتبة {m(150)} من اليسار؟",
        ans_ev, [(ans_ev + 2) % 10, (ans_ev + 4) % 10, (ans_ev + 6) % 10, (ans_ev + 1) % 10],
        f"Count how many one-digit evens ({m('2,4,6,8')}) and two-digit evens ({m('10,12,\\dots,98')}) appear before {m(100)}!",
        f"احسب عدد الأعداد الزوجية الأحادية ({m('2,4,6,8')}) والثنائية ({m('10,12,\\dots,98')}) قبل الوصول إلى {m(100)}!",
        f"Subtract {m(4)} digits for {m('2..8')} and {m('45 \\times 2 = 90')} digits for {m('10..98')}, then index into three-digit evens!",
        [
            f"One-digit evens {m('2,4,6,8')} give {m(4)} digits; the {m(45)} two-digit evens {m('10,12,\\dots,98')} give {m('45 \\times 2 = 90')} digits ({m(94)} total).",
            f"Remaining offset is {m('150 - 94 = 56')} into {m('100, 102, 104, \\dots')}; since {m('56 = 18 \\times 3 + 2')}, we take the {m(2)}nd digit of the {m(19)}th three-digit even {m('100 + 18 \\times 2 = 136')}.",
            f"The middle digit of {m(136)} is {m(ans_ev)}.",
        ],
        f"Check: {m(18)} numbers {m('100\\text{–}134')} use {m(54)} digits (reaching {m('94 + 54 = 148')}), so positions {m('149, 150, 151')} are {m('1, 3, 6')}!",
        f"نطرح {m(4)} خانات للأحادية و{m(90)} خانة للثنائية، ثم نحدد موقع الخانة داخل الأعداد الزوجية الثلاثية!",
        [
            f"الأعداد {m('2,4,6,8')} تعطي {m(4)} خانات، والـ {m(45)} عدداً زوجياً من {m(10)} إلى {m(98)} تعطي {m(90)} خانة (المجموع {m(94)}).",
            f"يتبقى {m('150 - 94 = 56')} خانة؛ وبما أن {m('56 = 18 \\times 3 + 2')} نأخذ الخانة الثانية في العدد الزوجي التاسع عشر بعد المئة وهو {m('100 + 36 = 136')}.",
            f"الرقم الأوسط في {m(136)} هو {m(ans_ev)}.",
        ],
        f"تحقق: المواضع {m('149, 150, 151')} توافق أرقام العدد {m(136)} على الترتيب، فالموضع {m(150)} هو {m(ans_ev)}!",
        diagram_en=svg_number_strip(["2..8: 4", "10..98: 90", "#150", "in 136"]),
    )

    sq_stream = "".join(str(i * i) for i in range(1, 50))
    ans_sq = int(sq_stream[39])
    B.add_math(
        tp, "Hard", bp,
        f"The positive **perfect squares** are concatenated in increasing order: {m('149162536496481100\\dots')}. What is the {m(40)}-th digit from the left?",
        f"كُتبت **المربعات الكاملة** الموجبة متتاليةً تصاعدياً: {m('149162536496481100\\dots')}. ما الرقم الواقع في المرتبة {m(40)} من اليسار؟",
        ans_sq, [(ans_sq + 1) % 10, (ans_sq + 3) % 10, (ans_sq + 5) % 10, (ans_sq + 7) % 10],
        f"Group squares by digit count: {m('1^2\\text{–}3^2')} ({m(1)} digit each), {m('4^2\\text{–}9^2')} ({m(2)} digits each), and {m('10^2\\text{–}31^2')} ({m(3)} digits each)!",
        f"قسّم المربعات حسب عدد خاناتها: {m('1^2\\text{–}3^2')} (خانة واحدة)، و{m('4^2\\text{–}9^2')} (خانتان)، و{m('10^2')} فصاعداً (ثلاث خانات)!",
        f"Count digits of {m('1^2..3^2')} ({m(3)}) and {m('4^2..9^2')} ({m(12)}), then step by {m(3)} digits per square from {m('10^2 = 100')}!",
        [
            f"Squares {m('1, 4, 9')} use {m(3)} digits, and the {m(6)} squares {m('16, 25, 36, 49, 64, 81')} use {m('6 \\times 2 = 12')} digits ({m(15)} total).",
            f"Remaining offset is {m('40 - 15 = 25')}; since {m('25 = 8 \\times 3 + 1')}, {m('10^2\\text{–}17^2')} use {m(24)} digits and index {m(40)} is the **first** digit of {m('18^2 = 324')}.",
            f"The first digit of {m(324)} is {m(ans_sq)}.",
        ],
        f"Verify: {m('3 + 12 + 24 = 39')} digits end {m('17^2 = 289')}, so the {m(40)}-th digit starts {m('18^2 = 324')}, giving {m(ans_sq)}!",
        f"نجمع خانات المربعات الأحادية ({m(3)}) والثنائية ({m(12)})، ثم نقسم الباقي على {m(3)} بدءاً من {m('10^2 = 100')}!",
        [
            f"المربعات {m('1, 4, 9')} تستهلك {m(3)} خانات، والمربعات الستة {m('16..81')} تستهلك {m(12)} خانة (المجموع {m(15)}).",
            f"يتبقى {m('40 - 15 = 25 = 8 \\times 3 + 1')}؛ إذن المربعات الثمانية {m('10^2..17^2')} تستهلك {m(24)} خانة، وتكون الخانة {m(40)} هي أول خانة في {m('18^2 = 324')}.",
            f"أول رقم في {m(324)} هو {m(ans_sq)}.",
        ],
        f"تحقق: الخانات {m('40, 41, 42')} هي {m('3, 2, 4')} على الترتيب!",
        diagram_en=svg_number_strip(["1²..3²: 3", "4²..9²: 12", "#40", "18²=324"]),
    )


# =============================================================================
# UNIT 2.3 — Factoring Tricks, Telescoping Surds & Symmetric Identities (75 Qs)
# =============================================================================
def _add_unit_2_3(B: BankBuilder) -> None:
    tp = "Algebra"

    # 1. nsmo_g89_simons_favorite_factoring (5E, 6M, 4H) — SVG: svg_subdivided_rect_2x2
    bp = "nsmo_g89_simons_favorite_factoring"
    for a, b, p in [(2, 3, 7), (3, 4, 11), (2, 5, 11), (4, 5, 13), (3, 6, 13)]:
        c_rhs = p * p - a * b
        sols = [(x, y) for x in range(1, p * p) for y in range(1, p * p) if x * y + a * x + b * y == c_rhs]
        assert sols == [(p - b, p - a)], sols
        ans = (p - b) + (p - a)
        B.add_math(
            tp, "Easy", bp,
            f"Positive integers {m('x')} and {m('y')} satisfy {m(f'xy + {a}x + {b}y = {c_rhs}')}. Find the value of {m('x + y')}.",
            f"يحقق العددان الصحيحان الموجبان {m('x')} و{m('y')} المعادلة {m(f'xy + {a}x + {b}y = {c_rhs}')}. أوجد قيمة {m('x + y')}.",
            ans, [ans + 2, ans - 2, 2 * p, p + a + b],
            f"Add {m(f'{a} \\times {b} = {a*b}')} to both sides so the left side factors as {m(f'(x + {b})(y + {a})')}.",
            f"أضف {m(f'{a} \\times {b} = {a*b}')} إلى الطرفين ليتحلل الطرف الأيسر إلى {m(f'(x + {b})(y + {a})')}.",
            f"Complete the rectangle via Simon's Favorite Factoring Trick: {m(f'(x + {b})(y + {a}) = {p}^2')}!",
            [
                f"Add {m(a * b)} to both sides: {m(f'(x + {b})(y + {a}) = {c_rhs} + {a*b} = {p*p} = {p}^2')}.",
                f"Since {m('x, y \\ge 1')}, we have {m(f'x + {b} \\ge {b + 1}')} and {m(f'y + {a} \\ge {a + 1}')}, forcing both factors to equal the prime {m(p)}.",
                f"Thus {m(f'x = {p - b}')} and {m(f'y = {p - a}')}, giving {m(f'x + y = {ans}')}.",
            ],
            f"Substitute {m(f'(x, y) = ({p - b}, {p - a})')}: {m(f'{(p-b)*(p-a)} + {a*(p-b)} + {b*(p-a)} = {c_rhs}')}!",
            f"نطبق حيلة سايمون بإضافة {m(a*b)} للطرفين فنحصل على {m(f'(x + {b})(y + {a}) = {p}^2')}!",
            [
                f"بعد إضافة {m(a*b)} للطرفين تصبح المعادلة {m(f'(x + {b})(y + {a}) = {p*p}')}.",
                f"بما أن {m('x, y \\ge 1')} والعدد {m(p)} أولي، يجب أن يساوي كل قوس {m(p)} بالضبط.",
                f"ينتج {m(f'x = {p - b}')} و{m(f'y = {p - a}')}، ومنه {m(f'x + y = {ans}')}.",
            ],
            f"تحقق بالتعويض المباشر للزوج {m(f'({p - b}, {p - a})')} يعطي {m(c_rhs)} تماماً.",
            diagram_en=svg_subdivided_rect_2x2("xy", f"{a}x", f"{b}y", str(a * b)),
        )

    for a, b, rhs_prod in [(2, 4, 48), (3, 5, 72), (4, 6, 90)]:
        c_rhs = rhs_prod - a * b
        ans = sum(1 for d in _divisors(rhs_prod) if d > b and (rhs_prod // d) > a)
        B.add_math(
            tp, "Medium", bp,
            f"How many ordered pairs {m('(x, y)')} of **positive integers** satisfy {m(f'xy + {a}x + {b}y = {c_rhs}')}?",
            f"كم زوجاً مرتباً {m('(x, y)')} من **الأعداد الصحيحة الموجبة** يحقق المعادلة {m(f'xy + {a}x + {b}y = {c_rhs}')}؟",
            ans, [len(_divisors(rhs_prod)), ans + 2, max(1, ans - 2), ans + 4],
            f"Factor {m(f'(x + {b})(y + {a}) = {rhs_prod}')} and filter divisors {m('d = x + b')} satisfying {m(f'd > {b}')} and {m(f'{rhs_prod}/d > {a}')}!",
            f"حلّل إلى {m(f'(x + {b})(y + {a}) = {rhs_prod}')} ثم اختر القواسم التي تحقق {m(f'd > {b}')} و{m(f'{rhs_prod}/d > {a}')}!",
            f"Add {m(a * b)} to get {m(f'(x + {b})(y + {a}) = {rhs_prod}')}, then discard divisor pairs making {m('x \\le 0')} or {m('y \\le 0')}!",
            [
                f"Adding {m(a * b)} to both sides yields {m(f'(x + {b})(y + {a}) = {c_rhs} + {a*b} = {rhs_prod}')}.",
                f"For {m('x \\ge 1')} and {m('y \\ge 1')}, divisor {m(f'd = x + {b}')} of {m(rhs_prod)} must satisfy {m(f'{b + 1} \\le d \\le {rhs_prod // (a + 1)}')}.",
                f"Counting divisors of {m(rhs_prod)} in that interval gives {m(ans)} ordered pairs.",
            ],
            f"Trap check: {m(rhs_prod)} has {m(len(_divisors(rhs_prod)))} positive divisors in total, not all of which give {m('x, y \\ge 1')}!",
            f"بإضافة {m(a*b)} نحصل على {m(f'(x + {b})(y + {a}) = {rhs_prod}')} ثم نصفي القواسم التي تجعل {m('x, y \\ge 1')}!",
            [
                f"المعادلة تكافئ {m(f'(x + {b})(y + {a}) = {rhs_prod}')}.",
                f"الشرط {m('x, y \\ge 1')} يحصر القاسم {m(f'd = x + {b}')} في المجال {m(f'{b + 1} \\le d \\le {rhs_prod // (a + 1)}')}.",
                f"عدد قواسم {m(rhs_prod)} ضمن هذا المجال هو {m(ans)}.",
            ],
            f"انتبه: أخذ جميع قواسم {m(rhs_prod)} البالغ عددها {m(len(_divisors(rhs_prod)))} يُدخل قيماً صفرية أو سالبة!",
            diagram_en=svg_subdivided_rect_2x2("xy", f"{a}x", f"{b}y", str(a * b)),
        )

    for a, b, rhs_prod in [(3, 4, 36), (2, 7, 50), (5, 6, 80)]:
        c_rhs = rhs_prod - a * b
        ans = len(_divisors(rhs_prod))
        assert ans == sum(1 for d in _divisors(rhs_prod) if b + d >= 1 and a + rhs_prod // d >= 1)
        B.add_math(
            tp, "Medium", bp,
            f"How many ordered pairs {m('(x, y)')} of positive integers satisfy {m(f'xy - {a}x - {b}y = {c_rhs}')}?",
            f"كم زوجاً مرتباً {m('(x, y)')} من الأعداد الصحيحة الموجبة يحقق المعادلة {m(f'xy - {a}x - {b}y = {c_rhs}')}؟",
            ans, [ans - 2, ans + 3, ans // 2, ans + 6],
            f"Add {m(f'{a} \\times {b} = {a*b}')} to both sides to factor {m(f'(x - {b})(y - {a}) = {rhs_prod}')}; check whether negative divisors can work!",
            f"أضف {m(a*b)} للطرفين لتحصل على {m(f'(x - {b})(y - {a}) = {rhs_prod}')}، وتحقق هل توجد قواسم سالبة مقبولة!",
            f"Factor {m(f'(x - {b})(y - {a}) = {rhs_prod}')} and check both positive and negative divisor pairs!",
            [
                f"Adding {m(a * b)} gives {m(f'(x - {b})(y - {a}) = {rhs_prod}')}.",
                f"Every positive divisor {m(f'd \\mid {rhs_prod}')} gives {m(f'x = {b} + d \\ge 1')} and {m(f'y = {a} + {rhs_prod}/d \\ge 1')}.",
                f"Can both factors be negative? We would need {m(f'1 - {b} \\le x - {b} \\le -1')} and {m(f'1 - {a} \\le y - {a} \\le -1')}, whose product is at most {m((b - 1) * (a - 1))} {m(f'< {rhs_prod}')} — impossible! So exact {m(ans)} pairs exist.",
            ],
            f"Great Olympiad check: always verify {m(f'({b}-1)({a}-1) = {(b-1)*(a-1)} < {rhs_prod}')} to rule out negative factor pairs!",
            f"نحلل إلى {m(f'(x - {b})(y - {a}) = {rhs_prod}')} ونتأكد من استحالة العوامل السالبة!",
            [
                f"إضافة {m(a*b)} تعطي {m(f'(x - {b})(y - {a}) = {rhs_prod}')}.",
                f"كل قاسم موجب للعدد {m(rhs_prod)} يعطي حلاً موجباً {m('(x, y)')}، وعدد القواسم الموجبة {m(ans)}.",
                f"العوامل السالبة مستحيلة لأن أقصى جداء لها لـ {m('x, y \\ge 1')} هو {m((b-1)*(a-1))} وهو أصغر من {m(rhs_prod)}.",
            ],
            f"تحقق مهم: استبعاد القواسم السالبة لأن {m(f'{(b-1)*(a-1)} < {rhs_prod}')} يثبت أن الجواب {m(ans)} بالضبط.",
            diagram_en=svg_subdivided_rect_2x2("xy", f"−{a}x", f"−{b}y", f"+{a*b}"),
        )

    for a, b, c_rhs in [(3, 5, 25), (1, 3, 21), (3, 7, 36), (5, 3, 39)]:
        # 2xy + ax + by = c_rhs -> (2x + b)(2y + a) = 2*c_rhs + a*b (odd * odd since a,b odd!)
        M = 2 * c_rhs + a * b
        sols = [(x, y) for x in range(1, M) for y in range(1, M) if 2 * x * y + a * x + b * y == c_rhs]
        ans = len(sols)
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered pairs {m('(x, y)')} of **positive integers** satisfy {m(f'2xy + {a}x + {b}y = {c_rhs}')}?",
            f"كم زوجاً مرتباً {m('(x, y)')} من **الأعداد الصحيحة الموجبة** يحقق المعادلة {m(f'2xy + {a}x + {b}y = {c_rhs}')}؟",
            ans, [len(_divisors(M)), ans + 2, ans + 4, max(0, ans - 1) if ans > 0 else 3],
            f"Multiply the entire equation by {m(2)} first so {m('4xy')} becomes {m('(2x)(\\cdot)(2y)')}, then add {m(f'{a} \\times {b} = {a*b}')}!",
            f"اضرب المعادلة كاملةً في {m(2)} أولاً ليصبح الحد الأول {m('4xy')} ثم أضف {m(f'{a} \\times {b} = {a*b}')}!",
            f"Double the equation to factor {m(f'(2x + {b})(2y + {a}) = {M}')}!",
            [
                f"Multiply by {m(2)} and add {m(a * b)}: {m(f'4xy + {2*a}x + {2*b}y + {a*b} = {2*c_rhs} + {a*b} = {M}')}.",
                f"Factor as {m(f'(2x + {b})(2y + {a}) = {M}')}. Since {m(a)} and {m(b)} are odd and {m(M)} is odd, every divisor {m('d')} of {m(M)} is odd!",
                f"Enforcing {m(f'2x + {b} \\ge {b + 2}')} and {m(f'2y + {a} \\ge {a + 2}')} leaves exact {m(ans)} valid positive integer pairs.",
            ],
            f"Explicit solutions: {m(', '.join(str(p) for p in sols) if sols else '\\text{none}')} ({m(ans)} total).",
            f"نضرب المعادلة في {m(2)} ثم نضيف {m(a*b)} لنحصل على {m(f'(2x + {b})(2y + {a}) = {M}')}!",
            [
                f"بالضرب في {m(2)} وإضافة {m(a*b)}: {m(f'(2x + {b})(2y + {a}) = {M}')}.",
                f"نختبر قواسم العدد الفردي {m(M)} التي تحقق {m(f'2x + {b} \\ge {b + 2}')} و{m(f'2y + {a} \\ge {a + 2}')}.",
                f"نجد بالضبط {m(ans)} زوجاً مرتباً يحقق المعادلة.",
            ],
            f"تحقق: الأزواج الناتجة هي {m(', '.join(str(p) for p in sols))} وعددها {m(ans)}.",
            diagram_en=svg_subdivided_rect_2x2("4xy", f"{2*a}x", f"{2*b}y", str(a * b)),
        )

    # 2. nsmo_g89_difference_of_squares_chain (5E, 6M, 4H) — SVG: svg_area_identity_square
    bp = "nsmo_g89_difference_of_squares_chain"
    for A, Bv in [(503, 497), (1005, 995), (256, 244), (752, 748), (1252, 1248)]:
        ans = A * A - Bv * Bv
        B.add_math(
            tp, "Easy", bp,
            f"Without direct squaring, compute the exact value of {m(f'{A}^2 - {Bv}^2')}.",
            f"دون التربيع المباشر، احسب القيمة الدقيقة للمقدار {m(f'{A}^2 - {Bv}^2')}.",
            ans, [ans // 2, (A - Bv) ** 2, ans + 1000, ans - 1000],
            f"Factor {m(f'({A} - {Bv})({A} + {Bv})')}.",
            f"حلّل المقدار إلى {m(f'({A} - {Bv})({A} + {Bv})')}.",
            f"Apply difference of squares {m('A^2 - B^2 = (A - B)(A + B)')}!",
            [
                f"Compute the difference: {m(f'{A} - {Bv} = {A - Bv}')}.",
                f"Compute the sum: {m(f'{A} + {Bv} = {A + Bv}')}.",
                f"Multiply: {m(f'{A - Bv} \\times {A + Bv} = {ans}')}.",
            ],
            f"Mental check: round sum {m(A + Bv)} times small gap {m(A - Bv)} gives {m(ans)} instantly!",
            f"نطبق متطابقة فرق المربعين {m('(A - B)(A + B)')}!",
            [
                f"نحسب الفرق: {m(f'{A} - {Bv} = {A - Bv}')}.",
                f"نحسب المجموع: {m(f'{A} + {Bv} = {A + Bv}')}.",
                f"نضرب الناتجين: {m(f'{A - Bv} \\times {A + Bv} = {ans}')}.",
            ],
            f"تحقق ذهني سريع: {m(f'{A - Bv} \\times {A + Bv} = {ans}')}.",
            diagram_en=svg_area_identity_square(str(Bv), str(A - Bv)),
        )

    for n_ev in (20, 30, 40):
        ans = n_ev * (n_ev + 1) // 2
        assert ans == sum(((-1) ** (n_ev - k)) * k * k for k in range(1, n_ev + 1))
        B.add_math(
            tp, "Medium", bp,
            f"Evaluate the alternating sum of squares {m(f'{n_ev}^2 - {n_ev-1}^2 + {n_ev-2}^2 - {n_ev-3}^2 + \\cdots + 2^2 - 1^2')}.",
            f"احسب قيمة مجموع المربعات المتناوب {m(f'{n_ev}^2 - {n_ev-1}^2 + {n_ev-2}^2 - {n_ev-3}^2 + \\cdots + 2^2 - 1^2')}.",
            ans, [n_ev * n_ev // 2, ans - n_ev, ans + n_ev, n_ev * (n_ev - 1) // 2],
            f"Group consecutive pairs {m('(2k)^2 - (2k - 1)^2 = (2k - (2k-1))(2k + (2k-1)) = 4k - 1 = 2k + (2k - 1)')}!",
            f"جمّع كل حدين متتاليين {m('(2k)^2 - (2k - 1)^2 = 1 \\times (2k + 2k - 1)')}!",
            f"Pair adjacent squares so every difference {m('a^2 - (a-1)^2')} turns into {m('a + (a - 1)')}!",
            [
                f"Group into {m(n_ev // 2)} pairs: {m(f'({n_ev}^2 - {n_ev-1}^2) + \\cdots + (2^2 - 1^2)')}.",
                f"Since {m('k^2 - (k-1)^2 = 1 \\cdot (k + k - 1)')}, the sum becomes {m(f'{n_ev} + {n_ev-1} + \\cdots + 2 + 1')}.",
                f"By Gauss's triangular sum formula, {m(f'\\frac{{{n_ev} \\times {n_ev + 1}}}{{2}} = {ans}')}.",
            ],
            f"Small-case check for {m('n=4')}: {m('16 - 9 + 4 - 1 = 10 = 4 \\times 5 / 2')}!",
            f"نجمّع كل حدين متتاليين فتتحول المتسلسلة كاملةً إلى مجموع الأعداد من {m(1)} إلى {m(n_ev)}!",
            [
                f"كل زوج {m('k^2 - (k-1)^2')} يتحلل إلى {m('1 \\times (k + k - 1)')}.",
                f"يؤول المجموع إلى {m(f'1 + 2 + \\cdots + {n_ev}')}.",
                f"بتطبيق قانون غاوس نجد {m(f'\\frac{{{n_ev}({n_ev + 1})}}{{2}} = {ans}')}.",
            ],
            f"تحقق مصغّر عند {m('n=2')}: {m('4 - 1 = 3 = 2 \\times 3 / 2')}!",
        )

    for m_end in (10, 15, 24):
        ans = Fraction(m_end + 1, 2 * m_end)
        prod_check = Fraction(1, 1)
        for k in range(2, m_end + 1):
            prod_check *= Fraction(k * k - 1, k * k)
        assert prod_check == ans
        B.add_math(
            tp, "Medium", bp,
            f"Simplify the product {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{m_end}^2}}\\right)')}.",
            f"بسّط حاصل الضرب {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{m_end}^2}}\\right)')}.",
            ans, [Fraction(m_end - 1, 2 * m_end), Fraction(m_end + 1, m_end), Fraction(1, m_end), Fraction(m_end, 2 * m_end - 1)],
            f"Rewrite each factor as {m('\\frac{k^2 - 1}{k^2} = \\frac{k - 1}{k} \\cdot \\frac{k + 1}{k}')} so adjacent fractions telescope!",
            f"أعد كتابة كل قوس على الصورة {m('\\frac{k - 1}{k} \\cdot \\frac{k + 1}{k}')} لتختصر العوامل المتجاورة!",
            f"Factor {m('1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')} into two telescoping chains!",
            [
                f"Split the product into {m(f'\\left(\\frac{{1}}{{2}} \\cdot \\frac{{2}}{{3}} \\cdots \\frac{{{m_end - 1}}}{{{m_end}}}\\right)')} times {m(f'\\left(\\frac{{3}}{{2}} \\cdot \\frac{{4}}{{3}} \\cdots \\frac{{{m_end + 1}}}{{{m_end}}}\\right)')}.",
                f"The first chain telescopes to {m(f'\\frac{{1}}{{{m_end}}}')}, and the second telescopes to {m(f'\\frac{{{m_end + 1}}}{{2}}')}.",
                f"Multiplying gives {m(f'\\frac{{{m_end + 1}}}{{2 \\times {m_end}}}')} = {m(ans)}.",
            ],
            f"Check at {m('m=3')}: {m('\\frac{3}{4} \\cdot \\frac{8}{9} = \\frac{2}{3} = \\frac{3+1}{2 \\cdot 3}')}!",
            f"نفك كل عامل إلى {m('\\frac{k-1}{k} \\cdot \\frac{k+1}{k}')} فينفصل الجداء إلى سلسلتين متداخلتين!",
            [
                f"السلسلة الأولى {m(f'\\frac{{1}}{{2}} \\cdot \\frac{{2}}{{3}} \\cdots \\frac{{{m_end-1}}}{{{m_end}}}')} تختصر إلى {m(f'\\frac{{1}}{{{m_end}}}')}.",
                f"السلسلة الثانية {m(f'\\frac{{3}}{{2}} \\cdot \\frac{{4}}{{3}} \\cdots \\frac{{{m_end+1}}}{{{m_end}}}')} تختصر إلى {m(f'\\frac{{{m_end+1}}}{{2}}')}.",
                f"حاصل ضربهما بعد التبسيط يساوي {m(ans)}.",
            ],
            f"تحقق سريع عند {m('m=2')}: الناتج {m('3/4 = (2+1)/(2 \\cdot 2)')}!",
        )

    # 4 Hard domino difference-of-squares questions
    assert (2 + 1) * (4 + 1) * (16 + 1) * (256 + 1) * (65536 + 1) + 1 == 2 ** 32
    B.add_math(
        tp, "Hard", bp,
        f"Find the positive integer {m('k')} such that {m('(2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)(2^{16} + 1) + 1 = 2^k')}.",
        f"أوجد العدد الصحيح الموجب {m('k')} الذي يحقق {m('(2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)(2^{16} + 1) + 1 = 2^k')}.",
        32, [16, 30, 31, 64],
        f"Multiply the product by {m('(2 - 1) = 1')} on the left to start a chain reaction of {m('(a - b)(a + b) = a^2 - b^2')}!",
        f"اضرب الجداء من اليسار في {m('(2 - 1) = 1')} لتنطلق سلسلة فرق المربعين!",
        f"Insert the invisible factor {m('(2 - 1) = 1')} to collapse all five factors in sequence!",
        [
            f"Multiply the product {m('P')} by {m('(2 - 1) = 1')}: {m('(2 - 1)(2 + 1) = 2^2 - 1')}.",
            f"Each step doubles the exponent: {m('(2^2 - 1)(2^2 + 1) = 2^4 - 1 \\to 2^8 - 1 \\to 2^{16} - 1 \\to 2^{32} - 1')}.",
            f"Thus {m('P + 1 = (2^{32} - 1) + 1 = 2^{32}')}, so {m('k = 32')}.",
        ],
        f"Adding the exponents {m('1+2+4+8+16 = 31')} misses the extra {m('+1')} from {m('(2 - 1)')}, which makes the final power {m(32)}!",
        f"نضرب الجداء في {m('(2 - 1) = 1')} فيندمج كل قوسين متتاليين بمتطابقة فرق المربعين!",
        [
            f"الضرب في {m('(2 - 1)')} لا يغيّر القيمة ويعطي {m('(2 - 1)(2 + 1) = 2^2 - 1')}.",
            f"يتضاعف الأس في كل خطوة حتى نصل إلى {m('(2^{16} - 1)(2^{16} + 1) = 2^{32} - 1')}.",
            f"بإضافة {m(1)} نحصل على {m('2^{32}')}، إذن {m('k = 32')}.",
        ],
        f"انتبه: جمع الأسس {m('1+2+4+8+16 = 31')} فخ شهير؛ الأس الصحيح هو {m(32)}!",
    )

    assert (3 + 1) * (9 + 1) * (81 + 1) == 3280
    B.add_math(
        tp, "Hard", bp,
        f"Compute the exact integer value of the product {m('(3 + 1)(3^2 + 1)(3^4 + 1)')}.",
        f"احسب القيمة الصحيحة الدقيقة لحاصل الضرب {m('(3 + 1)(3^2 + 1)(3^4 + 1)')}.",
        3280, [6560, 6561, 2187, 3281],
        f"Multiply and **divide** by {m('(3 - 1) = 2')} so you don't double the answer!",
        f"اضرب **واقسم** على {m('(3 - 1) = 2')} حتى لا تتضاعف القيمة النهائية!",
        f"Multiply by {m('\\frac{3 - 1}{2}')} to collapse the product into {m('\\frac{3^8 - 1}{2}')}!",
        [
            f"Write {m('P = \\frac{(3 - 1)(3 + 1)(3^2 + 1)(3^4 + 1)}{3 - 1}')}.",
            f"The numerator collapses via difference of squares to {m('3^8 - 1 = 6561 - 1 = 6560')}.",
            f"Divide by {m('3 - 1 = 2')}: {m('P = 6560 / 2 = 3280')}.",
        ],
        f"Crucial check: unlike {m('2 - 1 = 1')}, here {m('3 - 1 = 2')}, so forgetting to divide by {m(2)} gives the trap {m(6560)}!",
        f"نضرب البسط والمقام في {m('(3 - 1) = 2')} فينهار البسط إلى {m('3^8 - 1')}!",
        [
            f"نكتب الجداء بالصورة {m('\\frac{(3 - 1)(3 + 1)(3^2 + 1)(3^4 + 1)}{2}')}.",
            f"البسط يساوي {m('3^8 - 1 = 6561 - 1 = 6560')}.",
            f"بقسمة الناتج على {m(2)} نجد {m('3280')}.",
        ],
        f"انتبه: نسيان القسمة على {m('3 - 1 = 2')} يوقعك في الفخ {m(6560)}!",
    )

    assert (4 + 1) * (16 + 1) * (256 + 1) == 21845
    B.add_math(
        tp, "Hard", bp,
        f"Evaluate the product {m('(4 + 1)(4^2 + 1)(4^4 + 1)')}.",
        f"أوجد قيمة حاصل الضرب {m('(4 + 1)(4^2 + 1)(4^4 + 1)')}.",
        21845, [65535, 21846, 16384, 32768],
        f"Multiply and divide by {m('4 - 1 = 3')}, using {m('4^8 = 2^{16} = 65536')}.",
        f"اضرب واقسم على {m('4 - 1 = 3')} مع استخدام {m('4^8 = 2^{16} = 65536')}.",
        f"Use {m('4 - 1 = 3')} to telescope the numerator to {m('4^8 - 1')}!",
        [
            f"Multiply and divide by {m('4 - 1 = 3')}: {m('\\frac{(4 - 1)(4 + 1)(4^2 + 1)(4^4 + 1)}{3} = \\frac{4^8 - 1}{3}')}.",
            f"Compute {m('4^8 = (2^2)^8 = 2^{16} = 65536')}, so {m('4^8 - 1 = 65535')}.",
            f"Divide by {m(3)}: {m('65535 / 3 = 21845')}.",
        ],
        f"Units-digit check: {m('5 \\times 17 \\times 257')} ends in {m(5)}, matching {m(21845)}!",
        f"بالضرب والقسمة على {m('4 - 1 = 3')} نحصل على {m('\\frac{4^8 - 1}{3}')}!",
        [
            f"البسط يختصر بفرق المربعين إلى {m('4^8 - 1 = 2^{16} - 1 = 65535')}.",
            f"نقسم على {m('4 - 1 = 3')}.",
            f"الناتج يساوي {m('65535 \\div 3 = 21845')}.",
        ],
        f"تحقق من الآحاد: ضرب أعداد فردية أولها {m(5)} ينتهي حتماً بالرقم {m(5)}!",
    )

    assert sum(int(c) for c in str((2 + 1) * (4 + 1) * (16 + 1) * (256 + 1) + 1)) == 25
    B.add_math(
        tp, "Hard", bp,
        f"Let {m('N = (2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)')}. What is the **sum of the decimal digits** of {m('N + 1')}?",
        f"ليكن {m('N = (2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1)')}. ما **مجموع خانات** العدد {m('N + 1')} في النظام العشري؟",
        25, [24, 16, 28, 31],
        f"Collapse {m('N')} to {m('2^{16} - 1')}, write {m('2^{16} = 65536')}, and add its digits!",
        f"اختصر {m('N')} إلى {m('2^{16} - 1')} ثم احسب {m('2^{16} = 65536')} واجمع خاناته!",
        f"Simplify {m('N + 1 = 2^{16} = 65536')} via difference of squares!",
        [
            f"Multiplying {m('N')} by {m('(2 - 1) = 1')} collapses the four factors to {m('N = 2^{16} - 1')}.",
            f"Hence {m('N + 1 = 2^{16} = 1024 \\times 64 = 65536')}.",
            f"Sum the digits: {m('6 + 5 + 5 + 3 + 6 = 25')}.",
        ],
        f"Mod-9 check: {m('2^{16} = (2^6)^2 \\cdot 2^4 \\equiv 1^2 \\cdot 16 \\equiv 7 \\pmod{9}')}, and {m('25 \\equiv 7 \\pmod{9}')}!",
        f"نبسّط {m('N')} إلى {m('2^{16} - 1')} فيكون {m('N + 1 = 65536')}!",
        [
            f"باستخدام {m('(2 - 1) = 1')} نجد {m('N = 2^{16} - 1')}.",
            f"إذن {m('N + 1 = 2^{16} = 65536')}.",
            f"مجموع خاناته: {m('6 + 5 + 5 + 3 + 6 = 25')}.",
        ],
        f"تحقق بالمقاس {m(9)}: باقي {m('2^{16}')} على {m(9)} هو {m(7)}، ومجموع خانات {m(25)} هو {m(7)} أيضاً!",
    )

    # 3. nsmo_g89_reciprocal_power_sum (5E, 6M, 4H) — SVG: svg_area_identity_square
    bp = "nsmo_g89_reciprocal_power_sum"
    for k in (3, 5, 6, 7, 8):
        ans = k * k - 2
        B.add_math(
            tp, "Easy", bp,
            f"If a real number {m('x')} satisfies {m(f'x + \\frac{{1}}{{x}} = {k}')}, what is the value of {m('x^2 + \\frac{1}{x^2}')}?",
            f"إذا كان العدد الحقيقي {m('x')} يحقق {m(f'x + \\frac{{1}}{{x}} = {k}')}، فما قيمة {m('x^2 + \\frac{1}{x^2}')}؟",
            ans, [k * k, k * k + 2, ans - 2, 2 * k],
            f"Square {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^2 = x^2 + 2 + \\frac{{1}}{{x^2}}')}.",
            f"ربّع الطرفين: {m('\\left(x + \\frac{1}{x}\\right)^2 = x^2 + 2 + \\frac{1}{x^2}')}.",
            f"Square both sides and subtract the constant middle term {m(2)}!",
            [
                f"Expand {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^2 = x^2 + 2 \\cdot x \\cdot \\frac{{1}}{{x}} + \\frac{{1}}{{x^2}} = x^2 + 2 + \\frac{{1}}{{x^2}}')}.",
                f"Substitute {m(f'x + \\frac{{1}}{{x}} = {k}')}: {m(f'{k}^2 = x^2 + \\frac{{1}}{{x^2}} + 2')}.",
                f"Subtract {m(2)}: {m(f'x^2 + \\frac{{1}}{{x^2}} = {k*k} - 2 = {ans}')}.",
            ],
            f"Don't forget the middle {m('+2')}, which separates {m(ans)} from {m(k*k)}!",
            f"نربّع الطرفين ونطرح الحد الأوسط الثابت {m(2)}!",
            [
                f"بفك المربع: {m('\\left(x + \\frac{1}{x}\\right)^2 = x^2 + 2 + \\frac{1}{x^2}')}.",
                f"نعوّض بـ {m(k)}: {m(f'{k*k} = x^2 + \\frac{{1}}{{x^2}} + 2')}.",
                f"إذن {m(f'x^2 + \\frac{{1}}{{x^2}} = {ans}')}.",
            ],
            f"انتبه لعدم نسيان طرح {m(2)} من {m(k*k)}!",
            diagram_en=svg_area_identity_square("x", "1/x"),
        )

    for k in (2, 3, 4):
        ans = k * k + 2
        B.add_math(
            tp, "Medium", bp,
            f"If a nonzero real number {m('x')} satisfies {m(f'x - \\frac{{1}}{{x}} = {k}')}, what is the value of {m('x^2 + \\frac{1}{x^2}')}?",
            f"إذا كان العدد الحقيقي غير الصفري {m('x')} يحقق {m(f'x - \\frac{{1}}{{x}} = {k}')}، فما قيمة {m('x^2 + \\frac{1}{x^2}')}؟",
            ans, [k * k - 2, k * k, ans + 2, (k + 1) ** 2],
            f"Watch the minus sign: {m('\\left(x - \\frac{1}{x}\\right)^2 = x^2 - 2 + \\frac{1}{x^2}')}, so you **add** {m(2)}!",
            f"انتبه لإشارة الطرح: {m('\\left(x - \\frac{1}{x}\\right)^2 = x^2 - 2 + \\frac{1}{x^2}')}، لذا **نجمع** {m(2)}!",
            f"Square {m(f'x - \\frac{{1}}{{x}} = {k}')} and **add** {m(2)}!",
            [
                f"Expand {m('\\left(x - \\frac{1}{x}\\right)^2 = x^2 - 2 + \\frac{1}{x^2}')}.",
                f"Substitute {m(f'x - \\frac{{1}}{{x}} = {k}')}: {m(f'{k*k} = x^2 - 2 + \\frac{{1}}{{x^2}}')}.",
                f"Add {m(2)}: {m(f'x^2 + \\frac{{1}}{{x^2}} = {k*k} + 2 = {ans}')}.",
            ],
            f"Sign trap beaten: {m(k*k - 2)} comes from {m('x + 1/x')}, whereas {m('x - 1/x')} gives {m(ans)}!",
            f"نربّع المعادلة ثم **نضيف** {m(2)} لأن الحد الأوسط سالب!",
            [
                f"لدينا {m('\\left(x - \\frac{1}{x}\\right)^2 = x^2 - 2 + \\frac{1}{x^2}')}.",
                f"بالتعويض نحصل على {m(f'{k*k} = x^2 + \\frac{{1}}{{x^2}} - 2')}.",
                f"بإضافة {m(2)} للطرفين نجد {m(ans)}.",
            ],
            f"تحقق من الإشارة: هنا نجمع {m(2)} ولا نطرحها!",
        )

    for k in (3, 4, 5):
        ans = k ** 3 - 3 * k
        B.add_math(
            tp, "Medium", bp,
            f"If {m(f'x + \\frac{{1}}{{x}} = {k}')}, find the exact value of {m('x^3 + \\frac{1}{x^3}')}.",
            f"إذا كان {m(f'x + \\frac{{1}}{{x}} = {k}')}، فأوجد القيمة الدقيقة للمقدار {m('x^3 + \\frac{1}{x^3}')}.",
            ans, [k ** 3, k ** 3 - 3, k ** 3 + 3 * k, k * (k * k - 2)],
            f"Expand {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}!",
            f"فك المكعب: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}!",
            f"Use the cubic reciprocal identity {m('x^3 + x^{-3} = k^3 - 3k')}!",
            [
                f"Cube both sides: {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^3 = x^3 + 3x + \\frac{{3}}{{x}} + \\frac{{1}}{{x^3}} = x^3 + \\frac{{1}}{{x^3}} + 3\\left(x + \\frac{{1}}{{x}}\\right)')}.",
                f"Substitute {m(f'x + \\frac{{1}}{{x}} = {k}')}: {m(f'{k**3} = \\left(x^3 + \\frac{{1}}{{x^3}}\\right) + 3({k})')}.",
                f"Subtract {m(3 * k)}: {m(f'{k**3} - {3*k} = {ans}')}.",
            ],
            f"Alternative check: {m(f'(x + 1/x)(x^2 - 1 + 1/x^2) = {k} \\times ({k*k - 2} - 1) = {ans}')}!",
            f"نطبق متطابقة مجموع المكعبين التبادلية {m('k^3 - 3k')}!",
            [
                f"بتكعيب الطرفين: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}.",
                f"نعوّض بالقيمة {m(k)}: {m(f'{k**3} = \\left(x^3 + \\frac{{1}}{{x^3}}\\right) + {3*k}')}.",
                f"بطرح {m(3 * k)} نجد {m(ans)}.",
            ],
            f"تحقق آخر: {m(f'{k} \\times ({k*k - 2} - 1) = {ans}')}!",
        )

    for M, k in [(23, 5), (47, 7)]:
        ans = k ** 3 - 3 * k
        B.add_math(
            tp, "Hard", bp,
            f"A **positive** real number {m('x > 0')} satisfies {m(f'x^2 + \\frac{{1}}{{x^2}} = {M}')}. Find the value of {m('x^3 + \\frac{1}{x^3}')}.",
            f"يحقق العدد الحقيقي **الموجب** {m('x > 0')} المعادلة {m(f'x^2 + \\frac{{1}}{{x^2}} = {M}')}. أوجد قيمة {m('x^3 + \\frac{1}{x^3}')}.",
            ans, [k ** 3, k * M, ans + 3 * k, (k - 1) ** 3 - 3 * (k - 1)],
            f"First recover {m('x + \\frac{1}{x}')} by adding {m(2)} to {m(M)} and taking the positive square root!",
            f"أوجد أولاً {m('x + \\frac{1}{x}')} بإضافة {m(2)} إلى {m(M)} وأخذ الجذر التربيعي الموجب!",
            f"Add {m(2)} to find {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^2 = {M + 2} = {k}^2')}, then compute {m('k^3 - 3k')}!",
            [
                f"Notice {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^2 = x^2 + \\frac{{1}}{{x^2}} + 2 = {M} + 2 = {M + 2}')}.",
                f"Since {m('x > 0')}, {m(f'x + \\frac{{1}}{{x}} = \\sqrt{{{M + 2}}} = {k}')}.",
                f"Now {m(f'x^3 + \\frac{{1}}{{x^3}} = {k}^3 - 3({k}) = {k**3} - {3*k} = {ans}')}.",
            ],
            f"Check: {m(f'(x + 1/x)(x^2 + 1/x^2) = {k} \\times {M} = {k*M} = (x^3 + 1/x^3) + (x + 1/x) = {ans} + {k}')}!",
            f"نستنتج {m(f'x + \\frac{{1}}{{x}} = {k}')} أولاً بإضافة {m(2)} وأخذ الجذر الموجب، ثم نحسب {m('k^3 - 3k')}!",
            [
                f"لدينا {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^2 = {M} + 2 = {M + 2}')}، وبما أن {m('x > 0')} فإن {m(f'x + \\frac{{1}}{{x}} = {k}')}.",
                f"نطبق قانون التكعيب: {m(f'x^3 + \\frac{{1}}{{x^3}} = {k}^3 - 3({k})')}.",
                f"الناتج يساوي {m(f'{k**3} - {3*k} = {ans}')}.",
            ],
            f"تحقق: {m(f'{k} \\times {M} - {k} = {ans}')}!",
        )

    for k in (3, 5):
        s2 = k * k - 2
        ans = s2 * s2 - 2
        B.add_math(
            tp, "Hard", bp,
            f"A real number {m('x')} satisfies the quadratic equation {m(f'x^2 - {k}x + 1 = 0')}. What is the value of {m('x^4 + \\frac{1}{x^4}')}?",
            f"يحقق العدد الحقيقي {m('x')} المعادلة التربيعية {m(f'x^2 - {k}x + 1 = 0')}. ما قيمة {m('x^4 + \\frac{1}{x^4}')}؟",
            ans, [s2 * s2, ans + 4, k ** 4 - 2, s2 * s2 + 2],
            f"Since {m('x \\neq 0')}, divide the entire quadratic by {m('x')} to uncover {m(f'x + \\frac{{1}}{{x}} = {k}')}!",
            f"بما أن {m('x \\neq 0')}، اقسم المعادلة التربيعية على {m('x')} لتحصل فوراً على {m(f'x + \\frac{{1}}{{x}} = {k}')}!",
            f"Divide {m(f'x^2 - {k}x + 1 = 0')} by {m('x')}, then square twice!",
            [
                f"Testing {m('x = 0')} gives {m('1 = 0')}, so {m('x \\neq 0')}; dividing by {m('x')} yields {m(f'x + \\frac{{1}}{{x}} = {k}')}.",
                f"First squaring step: {m(f'x^2 + \\frac{{1}}{{x^2}} = {k}^2 - 2 = {s2}')}.",
                f"Second squaring step: {m(f'x^4 + \\frac{{1}}{{x^4}} = {s2}^2 - 2 = {s2*s2} - 2 = {ans}')}.",
            ],
            f"Dividing {m(f'x^2 - {k}x + 1 = 0')} by {m('x')} is the classic Olympiad bridge from quadratics to reciprocal powers!",
            f"نقسم المعادلة على {m('x')} لكشف {m(f'x + \\frac{{1}}{{x}} = {k}')} ثم نربّع مرتين!",
            [
                f"بقسمة {m(f'x^2 - {k}x + 1 = 0')} على {m('x \\neq 0')} نجد {m(f'x + \\frac{{1}}{{x}} = {k}')}.",
                f"التربيع الأول يعطي {m(f'x^2 + \\frac{{1}}{{x^2}} = {s2}')}.",
                f"التربيع الثاني يعطي {m(f'x^4 + \\frac{{1}}{{x^4}} = {s2}^2 - 2 = {ans}')}.",
            ],
            f"تحقق: لا تنسَ طرح {m(2)} في كلتا خطوتي التربيع!",
            diagram_en=svg_area_identity_square("x²", "1/x²"),
        )

    # 4. nsmo_g89_rationalizing_surd_sum (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g89_rationalizing_surd_sum"
    for m_int, b_rad in [(3, 5), (4, 11), (5, 19), (6, 29), (7, 38)]:
        k_num = m_int * m_int - b_rad
        ans = 2 * m_int
        assert math.isclose(k_num / (m_int - math.sqrt(b_rad)) + k_num / (m_int + math.sqrt(b_rad)), ans)
        B.add_math(
            tp, "Easy", bp,
            f"Simplify the radical sum {m(f'\\frac{{{k_num}}}{{{m_int} - \\sqrt{{{b_rad}}}}} + \\frac{{{k_num}}}{{{m_int} + \\sqrt{{{b_rad}}}}}')}.",
            f"بسّط المجموع الجذري {m(f'\\frac{{{k_num}}}{{{m_int} - \\sqrt{{{b_rad}}}}} + \\frac{{{k_num}}}{{{m_int} + \\sqrt{{{b_rad}}}}}')}.",
            ans, [m_int, 2 * k_num, ans + 2, m_int * m_int],
            f"Notice {m(f'{m_int}^2 - (\\sqrt{{{b_rad}}})^2 = {m_int*m_int} - {b_rad} = {k_num}')}, which matches the numerator!",
            f"لاحظ أن {m(f'{m_int}^2 - {b_rad} = {k_num}')} يساوي البسط تماماً عند الضرب في المرافق!",
            f"Rationalize each fraction using {m(f'({m_int} - \\sqrt{{{b_rad}}})({m_int} + \\sqrt{{{b_rad}}}) = {k_num}')}!",
            [
                f"Multiply the first fraction by {m(f'{m_int} + \\sqrt{{{b_rad}}}')} and the second by {m(f'{m_int} - \\sqrt{{{b_rad}}}')}.",
                f"Both denominators become {m(f'{m_int}^2 - {b_rad} = {k_num}')}, canceling the numerators {m(k_num)} cleanly.",
                f"Add what remains: {m(f'({m_int} + \\sqrt{{{b_rad}}}) + ({m_int} - \\sqrt{{{b_rad}}}) = {ans}')}.",
            ],
            f"Both radicals {m(f'+\\sqrt{{{b_rad}}}')} and {m(f'-\\sqrt{{{b_rad}}}')} cancel to {m(0)}, leaving {m(ans)}!",
            f"نضرب كل كسر في مرافقه فيختصر المقام {m(k_num)} مع البسط وتلغي الجذور بعضها!",
            [
                f"جداء المترافقين في المقام يساوي {m(f'{m_int}^2 - {b_rad} = {k_num}')}.",
                f"يصبح الكسر الأول {m(f'{m_int} + \\sqrt{{{b_rad}}}')} والكسر الثاني {m(f'{m_int} - \\sqrt{{{b_rad}}}')}.",
                f"بجمعهما تختفي الجذور ويبقى {m(f'2 \\times {m_int} = {ans}')}.",
            ],
            f"تحقق: حاصل الجمع عدد صحيح خالص قيمته {m(ans)}.",
        )

    for a_sq, b_sq in [(1, 25), (1, 49), (4, 64), (9, 81), (16, 121), (25, 144)]:
        ra, rb = math.isqrt(a_sq), math.isqrt(b_sq)
        ans = rb - ra
        B.add_math(
            tp, "Medium", bp,
            f"Evaluate the telescoping radical sum {m(f'\\frac{{1}}{{\\sqrt{{{a_sq}}} + \\sqrt{{{a_sq+1}}}}} + \\frac{{1}}{{\\sqrt{{{a_sq+1}}} + \\sqrt{{{a_sq+2}}}}} + \\cdots + \\frac{{1}}{{\\sqrt{{{b_sq-1}}} + \\sqrt{{{b_sq}}}}}')}.",
            f"أوجد قيمة المجموع الجذري المتداخل {m(f'\\frac{{1}}{{\\sqrt{{{a_sq}}} + \\sqrt{{{a_sq+1}}}}} + \\frac{{1}}{{\\sqrt{{{a_sq+1}}} + \\sqrt{{{a_sq+2}}}}} + \\cdots + \\frac{{1}}{{\\sqrt{{{b_sq-1}}} + \\sqrt{{{b_sq}}}}}')}.",
            ans, [rb + ra, rb, ans - 1, ans + 1],
            f"Rationalize each term as {m('\\sqrt{k+1} - \\sqrt{k}')} so all interior square roots cancel!",
            f"أنطق مقام كل حد على الصورة {m('\\sqrt{k+1} - \\sqrt{k}')} فتختصر جميع الجذور الداخلية!",
            f"Turn every term into {m('\\sqrt{k+1} - \\sqrt{k}')} and keep only the outer endpoints!",
            [
                f"Rationalizing gives {m(f'(\\sqrt{{{a_sq+1}}} - \\sqrt{{{a_sq}}}) + (\\sqrt{{{a_sq+2}}} - \\sqrt{{{a_sq+1}}}) + \\cdots + (\\sqrt{{{b_sq}}} - \\sqrt{{{b_sq-1}}})')}.",
                f"Every interior root appears once with {m('+')} and once with {m('-')}.",
                f"Only {m(f'\\sqrt{{{b_sq}}} - \\sqrt{{{a_sq}}} = {rb} - {ra} = {ans}')} survives.",
            ],
            f"Check: {m(f'\\sqrt{{{b_sq}}} = {rb}')} minus {m(f'\\sqrt{{{a_sq}}} = {ra}')} equals {m(ans)}!",
            f"نحوّل كل كسر بضربه في المرافق إلى {m('\\sqrt{k+1} - \\sqrt{k}')}!",
            [
                f"يصبح المجموع سلسلة فروق متتالية من {m(f'\\sqrt{{{a_sq}}}')} حتى {m(f'\\sqrt{{{b_sq}}}')}.",
                f"تختصر جميع الجذور الوسطى ويبقى الجذر الأكبر ناقص الجذر الأصغر.",
                f"نحسب: {m(f'\\sqrt{{{b_sq}}} - \\sqrt{{{a_sq}}} = {rb} - {ra} = {ans}')}.",
            ],
            f"تحقق: انتبه لطرح {m(ra)} بدلاً من نسيانه!",
            diagram_en=svg_number_strip([f"√{a_sq+1}−√{a_sq}", "…", f"√{b_sq}−√{b_sq-1}", f"={ans}"]),
        )

    for step_d, a_sq, b_sq in [(2, 1, 81), (3, 1, 100), (4, 9, 121), (3, 1, 256)]:
        ra, rb = math.isqrt(a_sq), math.isqrt(b_sq)
        ans = (rb - ra) // step_d
        n_terms = (b_sq - a_sq) // step_d
        assert math.isclose(
            sum(1.0 / (math.sqrt(a_sq + j * step_d) + math.sqrt(a_sq + (j + 1) * step_d)) for j in range(n_terms)),
            ans,
        )
        B.add_math(
            tp, "Hard", bp,
            f"Compute the exact value of {m(f'\\frac{{1}}{{\\sqrt{{{a_sq}}} + \\sqrt{{{a_sq+step_d}}}}} + \\frac{{1}}{{\\sqrt{{{a_sq+step_d}}} + \\sqrt{{{a_sq+2*step_d}}}}} + \\cdots + \\frac{{1}}{{\\sqrt{{{b_sq-step_d}}} + \\sqrt{{{b_sq}}}}}')}.",
            f"احسب القيمة الدقيقة للمجموع {m(f'\\frac{{1}}{{\\sqrt{{{a_sq}}} + \\sqrt{{{a_sq+step_d}}}}} + \\frac{{1}}{{\\sqrt{{{a_sq+step_d}}} + \\sqrt{{{a_sq+2*step_d}}}}} + \\cdots + \\frac{{1}}{{\\sqrt{{{b_sq-step_d}}} + \\sqrt{{{b_sq}}}}}')}.",
            ans, [rb - ra, ans + 1, (rb + ra) // step_d if (rb + ra) % step_d == 0 else ans + 2, rb // step_d],
            f"Watch the denominator gap! Here {m(f'(k + {step_d}) - k = {step_d}')}, so rationalizing introduces a factor of {m(f'\\frac{{1}}{{{step_d}}}')}!",
            f"انتبه لفرق المربعين في المقام! هنا {m(f'(k + {step_d}) - k = {step_d}')}، لذا يظهر العامل {m(f'\\frac{{1}}{{{step_d}}}')} خارج المجموع!",
            f"Rationalize each term as {m(f'\\frac{{\\sqrt{{k+{step_d}}} - \\sqrt{{k}}}}{{{step_d}}}')}, telescope, and divide by {m(step_d)}!",
            [
                f"Multiply top and bottom by {m(f'\\sqrt{{k + {step_d}}} - \\sqrt{{k}}')}: the denominator becomes {m(f'(k + {step_d}) - k = {step_d}')}.",
                f"Factor out {m(f'\\frac{{1}}{{{step_d}}}')}; the telescoping sum leaves {m(f'\\frac{{\\sqrt{{{b_sq}}} - \\sqrt{{{a_sq}}}}}{{{step_d}}}')}.",
                f"Evaluate {m(f'\\frac{{{rb} - {ra}}}{{{step_d}}} = \\frac{{{rb - ra}}}{{{step_d}}} = {ans}')}.",
            ],
            f"Forgetting to divide by the step size {m(step_d)} gives the trap {m(rb - ra)}!",
            f"عند إنطاق المقام يصبح المقام مساوياً للخطوة {m(step_d)} فنخرجه عاملاً مشتركاً قبل الاختصار!",
            [
                f"كل حد يساوي {m(f'\\frac{{1}}{{{step_d}}}(\\sqrt{{k+{step_d}}} - \\sqrt{{k}})')}.",
                f"تختصر الجذور الداخلية ويبقى {m(f'\\frac{{\\sqrt{{{b_sq}}} - \\sqrt{{{a_sq}}}}}{{{step_d}}}')}.",
                f"نحسب: {m(f'\\frac{{{rb} - {ra}}}{{{step_d}}} = {ans}')}.",
            ],
            f"انتبه: نسيان القسمة على خطوة التزايد {m(step_d)} يعطي الفخ الشائع {m(rb - ra)}!",
            diagram_en=svg_number_strip([f"÷{step_d}", f"√{b_sq}−√{a_sq}", f"({rb}−{ra})/{step_d}", f"={ans}"]),
        )

    # 5. nsmo_g89_symmetric_system_three (5E, 6M, 4H) — SVG: svg_area_identity_square
    bp = "nsmo_g89_symmetric_system_three"
    for x0, y0, z0 in [(4, 7, 11), (6, 9, 15), (5, 12, 17), (8, 13, 19), (10, 14, 22)]:
        s_xy, s_yz, s_zx = x0 + y0, y0 + z0, z0 + x0
        ans = x0 + y0 + z0
        B.add_math(
            tp, "Easy", bp,
            f"Real numbers {m('x, y, z')} satisfy {m(f'x + y = {s_xy}')}, {m(f'y + z = {s_yz}')}, and {m(f'z + x = {s_zx}')}. Find the value of {m('x + y + z')}.",
            f"تحقق الأعداد الحقيقية {m('x, y, z')} المعادلات {m(f'x + y = {s_xy}')} و{m(f'y + z = {s_yz}')} و{m(f'z + x = {s_zx}')}. أوجد قيمة {m('x + y + z')}.",
            ans, [2 * ans, z0, ans - x0, ans + 4],
            f"Add all three equations together: each variable appears exact **twice**!",
            f"اجمع المعادلات الثلاث معاً؛ يظهر كل متغير **مرتين** بالضبط!",
            f"Sum the symmetric equations to get {m('2(x + y + z)')} and divide by {m(2)}!",
            [
                f"Adding all three equations gives {m(f'2(x + y + z) = {s_xy} + {s_yz} + {s_zx} = {2 * ans}')}.",
                f"Divide both sides by {m(2)}: {m(f'x + y + z = {ans}')}.",
                f"(Individual values {m(f'x={x0}, y={y0}, z={z0}')} aren't even needed unless asked!)",
            ],
            f"Trap check: don't forget to divide {m(2 * ans)} by {m(2)}!",
            f"بجمع المعادلات الثلاث المتماثلة نحصل على {m('2(x + y + z)')} ثم نقسم على {m(2)}!",
            [
                f"بجمع الأطراف: {m(f'2(x + y + z) = {s_xy} + {s_yz} + {s_zx} = {2 * ans}')}.",
                f"بالقسمة على {m(2)} نجد {m(f'x + y + z = {ans}')}.",
                f"لا حاجة لإيجاد كل متغير منفرداً للوصول إلى المجموع.",
            ],
            f"انتبه لقسمة المجموع الكلي {m(2 * ans)} على {m(2)}!",
        )

    for x0, y0, z0 in [(2, 3, 6), (1, 4, 7), (2, 5, 8)]:
        S = x0 + y0 + z0
        P = x0 * y0 + y0 * z0 + z0 * x0
        ans = x0 * x0 + y0 * y0 + z0 * z0
        assert ans == S * S - 2 * P
        B.add_math(
            tp, "Medium", bp,
            f"Real numbers {m('x, y, z')} satisfy {m(f'x + y + z = {S}')} and {m(f'xy + yz + zx = {P}')}. Find {m('x^2 + y^2 + z^2')}.",
            f"تحقق الأعداد الحقيقية {m('x, y, z')} الشرطين {m(f'x + y + z = {S}')} و{m(f'xy + yz + zx = {P}')}. أوجد قيمة {m('x^2 + y^2 + z^2')}.",
            ans, [S * S - P, S * S, ans + 4, ans - 4],
            f"Use {m('(x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx)')}.",
            f"طبّق المتطابقة {m('(x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx)')}.",
            f"Subtract {m('2(xy + yz + zx)')} from {m('(x + y + z)^2')}!",
            [
                f"Start from {m('x^2 + y^2 + z^2 = (x + y + z)^2 - 2(xy + yz + zx)')}.",
                f"Substitute {m(f'S = {S}')} and {m(f'P = {P}')}: {m(f'{S}^2 - 2({P}) = {S*S} - {2*P}')}.",
                f"Simplify to get {m(ans)}.",
            ],
            f"Real-root verification: {m(f'({x0}, {y0}, {z0})')} has sum {m(S)}, pairwise sum {m(P)}, and square sum {m(ans)}!",
            f"نطرح {m('2(xy + yz + zx)')} من مربع المجموع {m('(x + y + z)^2')}!",
            [
                f"من المتطابقة التربيعية الثلاثية: {m('x^2 + y^2 + z^2 = (x+y+z)^2 - 2(xy+yz+zx)')}.",
                f"نعوّض: {m(f'{S}^2 - 2 \\times {P} = {S*S} - {2*P}')}.",
                f"الناتج يساوي {m(ans)}.",
            ],
            f"تحقق بالثلاثية الحقيقية {m(f'({x0}, {y0}, {z0})')} يؤكد أن مجموع المربعات {m(ans)}.",
            diagram_en=svg_area_identity_square("x+y", "z"),
        )

    for x0, y0, z0 in [(2, 3, 5), (3, 4, 6), (2, 5, 7)]:
        ab, bc, ca = x0 * y0, y0 * z0, z0 * x0
        prod_xyz = x0 * y0 * z0
        ans = x0 + y0 + z0
        B.add_math(
            tp, "Medium", bp,
            f"Positive real numbers {m('x, y, z')} satisfy {m(f'xy = {ab}')}, {m(f'yz = {bc}')}, and {m(f'zx = {ca}')}. Find {m('x + y + z')}.",
            f"تحقق الأعداد الحقيقية الموجبة {m('x, y, z')} المعادلات {m(f'xy = {ab}')} و{m(f'yz = {bc}')} و{m(f'zx = {ca}')}. أوجد قيمة {m('x + y + z')}.",
            ans, [prod_xyz, ans + 2, ans - 2, (ab + bc + ca) // 3],
            f"Multiply all three equations together to get {m('(xyz)^2')}!",
            f"اضرب المعادلات الثلاث معاً لتحصل على {m('(xyz)^2')}!",
            f"Take the positive square root of {m('(xyz)^2 = (xy)(yz)(zx)')}, then divide by each pairwise product!",
            [
                f"Multiply all three: {m(f'(xyz)^2 = {ab} \\times {bc} \\times {ca} = {prod_xyz ** 2}')}, so {m(f'xyz = {prod_xyz}')} (since {m('x,y,z > 0')}).",
                f"Divide {m('xyz')} by each pair: {m(f'z = {prod_xyz}/{ab} = {z0}')}, {m(f'x = {prod_xyz}/{bc} = {x0}')}, {m(f'y = {prod_xyz}/{ca} = {y0}')}.",
                f"Add: {m(f'{x0} + {y0} + {z0} = {ans}')}.",
            ],
            f"Check: {m(f'{x0}\\cdot{y0}={ab}')}, {m(f'{y0}\\cdot{z0}={bc}')}, and {m(f'{z0}\\cdot{x0}={ca}')}!",
            f"نضرب المعادلات الثلاث لإيجاد {m('xyz')} ثم نقسمه على كل معادلة لإيجاد المتغيرات!",
            [
                f"بضرب المعادلات: {m(f'(xyz)^2 = {prod_xyz ** 2}')}، وبما أنها موجبة فإن {m(f'xyz = {prod_xyz}')}.",
                f"بالقسمة نجد {m(f'x = {x0}')} و{m(f'y = {y0}')} و{m(f'z = {z0}')}.",
                f"المجموع {m(f'x + y + z = {ans}')}.",
            ],
            f"تحقق مباشر من الجداءات الثلاثة يؤكد القيم {m(f'({x0}, {y0}, {z0})')}.",
        )

    for x0, y0, z0 in [(1, 2, 4), (2, 3, 6)]:
        S = x0 + y0 + z0
        Q = x0 * x0 + y0 * y0 + z0 * z0
        R = x0 * y0 * z0
        P = x0 * y0 + y0 * z0 + z0 * x0
        ans = Fraction(P, R)
        assert ans == Fraction(1, x0) + Fraction(1, y0) + Fraction(1, z0)
        B.add_math(
            tp, "Hard", bp,
            f"Nonzero real numbers {m('x, y, z')} satisfy {m(f'x + y + z = {S}')}, {m(f'x^2 + y^2 + z^2 = {Q}')}, and {m(f'xyz = {R}')}. Find the value of {m('\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z}')}.",
            f"تحقق الأعداد الحقيقية غير الصفرية {m('x, y, z')} المعادلات {m(f'x + y + z = {S}')} و{m(f'x^2 + y^2 + z^2 = {Q}')} و{m(f'xyz = {R}')}. أوجد قيمة {m('\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z}')}.",
            ans, [Fraction(S, R), Fraction(2 * P, R), Fraction(P - 2, R), Fraction(Q, R)],
            f"Combine {m('\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z} = \\frac{xy + yz + zx}{xyz}')} and find {m('xy + yz + zx')} from {m('(x+y+z)^2 - (x^2+y^2+z^2)')}!",
            f"وحّد المقامات في {m('\\frac{xy + yz + zx}{xyz}')} وأوجد البسط من {m('\\frac{(x+y+z)^2 - (x^2+y^2+z^2)}{2}')}!",
            f"Put the reciprocals over common denominator {m('xyz')} and extract {m('xy + yz + zx')}!",
            [
                f"Write {m('\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z} = \\frac{xy + yz + zx}{xyz}')}.",
                f"Compute {m(f'xy + yz + zx = \\frac{{(x+y+z)^2 - (x^2+y^2+z^2)}}{{2}} = \\frac{{{S}^2 - {Q}}}{{2}} = {P}')}.",
                f"Divide by {m(f'xyz = {R}')}: {m(f'\\frac{{{P}}}{{{R}}}')} = {m(ans)}.",
            ],
            f"Concrete check with {m(f'({x0}, {y0}, {z0})')}: {m(f'1/{x0} + 1/{y0} + 1/{z0}')} = {m(ans)}!",
            f"نوحّد مقامات المقلوبات إلى {m('xyz')} ونحسب البسط {m('xy + yz + zx')} من مربع المجموع!",
            [
                f"لدينا {m('\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z} = \\frac{xy + yz + zx}{xyz}')}.",
                f"نحسب {m(f'xy + yz + zx = \\frac{{{S*S} - {Q}}}{{2}} = {P}')}.",
                f"بالقسمة على {m(R)} والتبسيط نحصل على {m(ans)}.",
            ],
            f"تحقق بالثلاثية {m(f'({x0}, {y0}, {z0})')} يعطي نفس القيمة تماماً!",
        )

    for x0, y0, z0 in [(1, 2, 3), (1, 3, 4)]:
        S = x0 + y0 + z0
        P = x0 * y0 + y0 * z0 + z0 * x0
        R = x0 * y0 * z0
        Q = S * S - 2 * P
        ans = x0 ** 3 + y0 ** 3 + z0 ** 3
        assert ans == S * (Q - P) + 3 * R
        B.add_math(
            tp, "Hard", bp,
            f"Real numbers {m('x, y, z')} satisfy {m(f'x + y + z = {S}')}, {m(f'xy + yz + zx = {P}')}, and {m(f'xyz = {R}')}. Find {m('x^3 + y^3 + z^3')}.",
            f"تحقق الأعداد الحقيقية {m('x, y, z')} المعادلات {m(f'x + y + z = {S}')} و{m(f'xy + yz + zx = {P}')} و{m(f'xyz = {R}')}. أوجد قيمة {m('x^3 + y^3 + z^3')}.",
            ans, [ans - 3 * R, S ** 3 - 3 * S * P, ans + 3 * R, S * Q],
            f"Use Gauss's identity {m('x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)')}!",
            f"استخدم متطابقة غاوس: {m('x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)')}!",
            f"Apply the three-variable cubic identity {m('x^3 + y^3 + z^3 = (x+y+z)((x+y+z)^2 - 3(xy+yz+zx)) + 3xyz')}!",
            [
                f"Recall {m('x^3 + y^3 + z^3 - 3xyz = (x+y+z)\\big((x+y+z)^2 - 3(xy+yz+zx)\\big)')}.",
                f"Substitute {m(f'S = {S},\\; P = {P},\\; R = {R}')}: {m(f'x^3 + y^3 + z^3 - 3({R}) = {S}({S*S} - 3 \\times {P}) = {S * (S*S - 3*P)}')}.",
                f"Add {m(3 * R)}: {m(f'{S * (S*S - 3*P)} + {3*R} = {ans}')}.",
            ],
            f"Direct check with {m(f'({x0}, {y0}, {z0})')}: {m(f'{x0}^3 + {y0}^3 + {z0}^3 = {ans}')}!",
            f"نطبق متطابقة غاوس التكعيبية {m('x^3+y^3+z^3 = S(S^2 - 3P) + 3R')}!",
            [
                f"من المتطابقة القياسية: {m('x^3 + y^3 + z^3 - 3xyz = (x+y+z)((x+y+z)^2 - 3(xy+yz+zx))')}.",
                f"نعوّض: {m(f'x^3 + y^3 + z^3 - {3*R} = {S}({S*S} - {3*P}) = {S*(S*S - 3*P)}')}.",
                f"بإضافة {m(3 * R)} نجد {m(ans)}.",
            ],
            f"تحقق مباشر بالثلاثية {m(f'({x0}, {y0}, {z0})')}: مجموع مكعباتها {m(ans)}!",
            diagram_en=svg_area_identity_square("x+y", "z"),
        )


# =============================================================================
# UNIT 2.4 — Vieta's Formulas, Quadratic Extrema, Absolute Value & Sequences (75 Qs)
# =============================================================================
def _add_unit_2_4(B: BankBuilder) -> None:
    tp = "Algebra"

    # 1. nsmo_g89_vieta_quadratic_roots (5E, 6M, 4H) — SVG: svg_parabola_roots
    bp = "nsmo_g89_vieta_quadratic_roots"
    for s_sum, p_prod, k_shift in [(8, 11, 1), (9, 14, 2), (10, 17, 3)]:
        assert s_sum * s_sum - 4 * p_prod > 0
        ans = p_prod + k_shift * s_sum + k_shift * k_shift
        B.add_math(
            tp, "Easy", bp,
            f"If {m('r')} and {m('s')} are the roots of {m(f'x^2 - {s_sum}x + {p_prod} = 0')}, what is the value of {m(f'(r + {k_shift})(s + {k_shift})')}?",
            f"إذا كان {m('r')} و{m('s')} جذري المعادلة {m(f'x^2 - {s_sum}x + {p_prod} = 0')}، فما قيمة {m(f'(r + {k_shift})(s + {k_shift})')}؟",
            ans, [p_prod - k_shift * s_sum + k_shift * k_shift, p_prod + k_shift * s_sum, ans + s_sum, p_prod * k_shift],
            f"Expand {m(f'(r + {k_shift})(s + {k_shift}) = rs + {k_shift}(r + s) + {k_shift*k_shift}')} and apply Vieta's formulas.",
            f"فك القوسين إلى {m(f'rs + {k_shift}(r + s) + {k_shift*k_shift}')} وطبّق علاقتي فييتا.",
            f"Expand the product and substitute {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}!",
            [
                f"By Vieta's formulas on {m(f'x^2 - {s_sum}x + {p_prod} = 0')}, {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}.",
                f"Expand {m(f'(r + {k_shift})(s + {k_shift}) = rs + {k_shift}(r + s) + {k_shift}^2')}.",
                f"Compute {m(f'{p_prod} + {k_shift}({s_sum}) + {k_shift*k_shift} = {ans}')}.",
            ],
            f"Shortcut check: for {m('f(x) = (x - r)(x - s)')}, {m(f'({-k_shift} - r)({-k_shift} - s) = f(-{k_shift}) = {ans}')}!",
            f"نفك الجداء ونعوّض بـ {m(f'r + s = {s_sum}')} و{m(f'rs = {p_prod}')}!",
            [
                f"من علاقات فييتا: {m(f'r + s = {s_sum}')} و{m(f'rs = {p_prod}')}.",
                f"نفك القوسين: {m(f'rs + {k_shift}(r + s) + {k_shift*k_shift}')}.",
                f"نحسب: {m(f'{p_prod} + {k_shift * s_sum} + {k_shift*k_shift} = {ans}')}.",
            ],
            f"تحقق جميل: القيمة تساوي {m(f'f(-{k_shift}) = (-{k_shift})^2 - {s_sum}(-{k_shift}) + {p_prod} = {ans}')}!",
            diagram_en=svg_parabola_roots("r", "s", f"r+s={s_sum}"),
        )

    for s_sum, p_prod in [(7, 5), (11, 8)]:
        assert s_sum * s_sum - 4 * p_prod > 0
        ans = Fraction(s_sum, p_prod)
        B.add_math(
            tp, "Easy", bp,
            f"Let {m('r')} and {m('s')} be the roots of {m(f'x^2 - {s_sum}x + {p_prod} = 0')}. Find the value of {m('\\frac{1}{r} + \\frac{1}{s}')}.",
            f"ليكن {m('r')} و{m('s')} جذري المعادلة {m(f'x^2 - {s_sum}x + {p_prod} = 0')}. أوجد قيمة {m('\\frac{1}{r} + \\frac{1}{s}')}.",
            ans, [Fraction(-s_sum, p_prod) if s_sum < 0 else Fraction(p_prod, s_sum), Fraction(s_sum - 1, p_prod), Fraction(s_sum, p_prod + 1), Fraction(2 * s_sum, p_prod)],
            f"Combine over a common denominator: {m('\\frac{1}{r} + \\frac{1}{s} = \\frac{r + s}{rs}')}.",
            f"وحّد المقامات: {m('\\frac{1}{r} + \\frac{1}{s} = \\frac{r + s}{rs}')}.",
            f"Rewrite {m('\\frac{1}{r} + \\frac{1}{s} = \\frac{r + s}{rs}')} and plug in Vieta's sum and product!",
            [
                f"Combine fractions: {m('\\frac{1}{r} + \\frac{1}{s} = \\frac{r + s}{rs}')}.",
                f"By Vieta's formulas, {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}.",
                f"Hence {m('\\frac{1}{r} + \\frac{1}{s} = ')} {m(ans)}.",
            ],
            f"Check: reversing coefficients gives {m(f'{p_prod}y^2 - {s_sum}y + 1 = 0')} for {m('y = 1/x')}, whose root sum is {m(ans)}!",
            f"نوحّد المقامات إلى {m('\\frac{r + s}{rs}')} ونعوّض من فييتا!",
            [
                f"لدينا {m('\\frac{1}{r} + \\frac{1}{s} = \\frac{r + s}{rs}')}.",
                f"من فييتا {m(f'r + s = {s_sum}')} و{m(f'rs = {p_prod}')}.",
                f"إذن الناتج يساوي {m(ans)}.",
            ],
            f"تحقق: معادلة المقلوبات هي {m(f'{p_prod}y^2 - {s_sum}y + 1 = 0')} ومجموع جذريها {m(ans)}.",
            diagram_en=svg_parabola_roots("r", "s", f"rs={p_prod}"),
        )

    for a_c, b_c, c_c in [(2, 10, 7), (2, 12, 11), (2, 14, 15)]:
        assert b_c * b_c - 4 * a_c * c_c > 0
        r_sum = b_c // a_c
        ans = r_sum * r_sum - c_c
        B.add_math(
            tp, "Medium", bp,
            f"If {m('r')} and {m('s')} are the roots of {m(f'{a_c}x^2 - {b_c}x + {c_c} = 0')}, find the value of {m('r^2 + s^2')}.",
            f"إذا كان {m('r')} و{m('s')} جذري المعادلة {m(f'{a_c}x^2 - {b_c}x + {c_c} = 0')}، فأوجد قيمة {m('r^2 + s^2')}.",
            ans, [b_c * b_c - 2 * c_c, r_sum * r_sum - 2 * c_c, ans + c_c, r_sum * r_sum + c_c],
            f"Remember to divide by the leading coefficient {m(a_c)}: {m(f'r + s = {b_c}/{a_c} = {r_sum}')} and {m(f'rs = {c_c}/{a_c}')}!",
            f"لا تنسَ القسمة على معامل {m('x^2')} وهو {m(a_c)}: {m(f'r + s = {r_sum}')} و{m(f'rs = {c_c}/{a_c}')}!",
            f"Divide by {m(a_c)} first when reading Vieta's sum and product!",
            [
                f"Divide by {m(a_c)}: {m(f'r + s = \\frac{{{b_c}}}{{{a_c}}} = {r_sum}')} and {m(f'rs = \\frac{{{c_c}}}{{{a_c}}}')}.",
                f"Use {m('r^2 + s^2 = (r + s)^2 - 2rs')}.",
                f"Compute {m(f'{r_sum}^2 - 2 \\cdot \\frac{{{c_c}}}{{{a_c}}} = {r_sum*r_sum} - {c_c} = {ans}')}.",
            ],
            f"Forgetting to divide by {m(a_c)} gives the classic trap {m(b_c*b_c - 2*c_c)}!",
            f"نقسم على المعامل الرئيسي {m(a_c)} أولاً عند تطبيق علاقتي فييتا!",
            [
                f"نجد {m(f'r + s = {b_c}/{a_c} = {r_sum}')} و{m(f'rs = {c_c}/{a_c}')}.",
                f"نعوّض في {m('r^2 + s^2 = (r + s)^2 - 2rs')}.",
                f"نحسب: {m(f'{r_sum*r_sum} - 2 \\times \\frac{{{c_c}}}{{2}} = {ans}')}.",
            ],
            f"انتبه: إغفال القسمة على المعامل الرئيسي {m(a_c)} فخ شائع جداً!",
            diagram_en=svg_parabola_roots("r", "s", f"a={a_c}"),
        )

    for s_sum, p_prod in [(9, 13), (11, 19), (13, 25)]:
        ans = s_sum * s_sum - 4 * p_prod
        assert ans > 0
        B.add_math(
            tp, "Medium", bp,
            f"The quadratic {m(f'x^2 - {s_sum}x + {p_prod} = 0')} has roots {m('r')} and {m('s')}. What is the value of {m('(r - s)^2')}?",
            f"للمعادلة التربيعية {m(f'x^2 - {s_sum}x + {p_prod} = 0')} جذران {m('r')} و{m('s')}. ما قيمة {m('(r - s)^2')}؟",
            ans, [s_sum * s_sum - 2 * p_prod, s_sum * s_sum + 4 * p_prod, ans + 2 * p_prod, s_sum * s_sum],
            f"Relate {m('(r - s)^2')} to {m('(r + s)^2')} by subtracting {m('4rs')}!",
            f"اربط {m('(r - s)^2')} بالمقدار {m('(r + s)^2')} بطرح {m('4rs')}!",
            f"Use the bridge identity {m('(r - s)^2 = (r + s)^2 - 4rs')}!",
            [
                f"From Vieta's formulas, {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}.",
                f"Apply {m('(r - s)^2 = (r + s)^2 - 4rs')}.",
                f"Evaluate {m(f'{s_sum}^2 - 4({p_prod}) = {s_sum*s_sum} - {4*p_prod} = {ans}')}.",
            ],
            f"Notice {m('(r - s)^2')} for a monic quadratic equals its discriminant {m('\\Delta = b^2 - 4c')}!",
            f"نستخدم المتطابقة الجسرية {m('(r - s)^2 = (r + s)^2 - 4rs')}!",
            [
                f"من فييتا {m(f'r + s = {s_sum}')} و{m(f'rs = {p_prod}')}.",
                f"نطبق {m('(r - s)^2 = (r + s)^2 - 4rs')}.",
                f"نحسب: {m(f'{s_sum*s_sum} - {4*p_prod} = {ans}')}.",
            ],
            f"ملاحظة مفيدة: لمعادلة معاملها الرئيسي {m(1)}، يساوي {m('(r - s)^2')} المميز {m('\\Delta')} دائماً!",
        )

    for s_sum, p_prod in [(5, 3), (7, 8)]:
        assert s_sum * s_sum - 4 * p_prod > 0
        B_new = -(s_sum * s_sum - 2 * p_prod)
        C_new = p_prod * p_prod
        ans = B_new + C_new
        B.add_math(
            tp, "Hard", bp,
            f"Let {m('r')} and {m('s')} be the roots of {m(f'x^2 - {s_sum}x + {p_prod} = 0')}. If the monic quadratic whose roots are {m('r^2')} and {m('s^2')} is {m('x^2 + Bx + C = 0')}, find {m('B + C')}.",
            f"ليكن {m('r')} و{m('s')} جذري المعادلة {m(f'x^2 - {s_sum}x + {p_prod} = 0')}. إذا كانت المعادلة التربيعية التي جذراها {m('r^2')} و{m('s^2')} هي {m('x^2 + Bx + C = 0')}، فأوجد {m('B + C')}.",
            ans, [-B_new + C_new, B_new + p_prod, C_new - s_sum * s_sum, ans - 2 * p_prod],
            f"Notice {m('B = -(r^2 + s^2)')} (watch the minus sign!) and {m('C = r^2 s^2 = (rs)^2')}.",
            f"لاحظ أن {m('B = -(r^2 + s^2)')} (انتبه للإشارة السالبة!) وأن {m('C = (rs)^2')}.",
            f"Compute the new root sum {m('r^2 + s^2')} and new root product {m('(rs)^2')} via Vieta!",
            [
                f"From {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}, {m(f'r^2 + s^2 = {s_sum}^2 - 2({p_prod}) = {s_sum*s_sum - 2*p_prod}')}.",
                f"Thus {m(f'B = -(r^2 + s^2) = {B_new}')} and {m(f'C = (rs)^2 = {p_prod}^2 = {C_new}')}.",
                f"Add: {m(f'B + C = {B_new} + {C_new} = {ans}')}.",
            ],
            f"Sign check: in {m('x^2 + Bx + C = (x - r^2)(x - s^2)')}, {m('B')} is **negative** when {m('r^2 + s^2 > 0')}!",
            f"نحسب مجموع وجداء الجذرين الجديدين {m('r^2')} و{m('s^2')} مع مراعاة إشارة {m('B')}!",
            [
                f"نجد {m(f'r^2 + s^2 = {s_sum}^2 - 2({p_prod}) = {-B_new}')}، ومنه {m(f'B = {B_new}')}.",
                f"وجداء الجذرين الجديدين {m(f'C = r^2 s^2 = {p_prod}^2 = {C_new}')}.",
                f"إذن {m(f'B + C = {B_new} + {C_new} = {ans}')}.",
            ],
            f"انتبه لإشارة {m('B')}: نسيان الإشارة السالبة يعطي الفخ {m(-B_new + C_new)}!",
            diagram_en=svg_parabola_roots("r²", "s²", f"C={C_new}"),
        )

    for s_sum, p_prod in [(5, 3), (6, 4)]:
        assert s_sum * s_sum - 4 * p_prod > 0
        ans = s_sum ** 3 - 3 * p_prod * s_sum
        B.add_math(
            tp, "Hard", bp,
            f"If {m('r')} and {m('s')} are the roots of {m(f'x^2 - {s_sum}x + {p_prod} = 0')}, compute {m('r^3 + s^3')}.",
            f"إذا كان {m('r')} و{m('s')} جذري المعادلة {m(f'x^2 - {s_sum}x + {p_prod} = 0')}، فاحسب قيمة {m('r^3 + s^3')}.",
            ans, [s_sum ** 3, s_sum ** 3 - 3 * p_prod, s_sum ** 3 + 3 * p_prod * s_sum, ans - p_prod * s_sum],
            f"Factor {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            f"استخدم المتطابقة {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            f"Substitute {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')} into {m('(r + s)^3 - 3rs(r + s)')}!",
            [
                f"By Vieta's formulas, {m(f'r + s = {s_sum}')} and {m(f'rs = {p_prod}')}.",
                f"Apply {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
                f"Compute {m(f'{s_sum}^3 - 3({p_prod})({s_sum}) = {s_sum**3} - {3*p_prod*s_sum} = {ans}')}.",
            ],
            f"Alternative check via {m(f'r^2 = {s_sum}r - {p_prod}')}: {m(f'r^3 + s^3 = {s_sum}(r^2+s^2) - {p_prod}(r+s) = {s_sum}({s_sum*s_sum - 2*p_prod}) - {p_prod*s_sum} = {ans}')}!",
            f"نعوّض من فييتا في المتطابقة التكعيبية {m('(r + s)^3 - 3rs(r + s)')}!",
            [
                f"لدينا {m(f'r + s = {s_sum}')} و{m(f'rs = {p_prod}')}.",
                f"نحسب {m(f'{s_sum}^3 - 3 \\times {p_prod} \\times {s_sum}')}.",
                f"الناتج يساوي {m(f'{s_sum**3} - {3*p_prod*s_sum} = {ans}')}.",
            ],
            f"تحقق آخر: {m(f'(r+s)(r^2 - rs + s^2) = {s_sum} \\times ({s_sum*s_sum - 3*p_prod}) = {ans}')}!",
        )

    # 2. nsmo_g89_completing_square_extremum (5E, 6M, 4H) — SVG: svg_parabola_roots
    bp = "nsmo_g89_completing_square_extremum"
    for h, c_val, sign in [(4, 25, 1), (5, 31, 1), (7, 60, 1), (3, 10, -1), (6, 5, -1)]:
        if sign == 1:
            ans = c_val - h * h
            expr = f"x^2 - {2*h}x + {c_val}"
            word_en, word_ar = "**minimum**", "**أصغر**"
        else:
            ans = c_val + h * h
            expr = f"-x^2 + {2*h}x + {c_val}"
            word_en, word_ar = "**maximum**", "**أكبر**"
        B.add_math(
            tp, "Easy", bp,
            f"Over all real numbers {m('x')}, what is the {word_en} possible value of {m(expr)}?",
            f"لجميع الأعداد الحقيقية {m('x')}، ما {word_ar} قيمة ممكنة للمقدار {m(expr)}؟",
            ans, [c_val, h, ans + h, abs(c_val - 2 * h)],
            f"Complete the square centered at {m(f'x = {h}')}.",
            f"أكمل المربع حول {m(f'x = {h}')}.",
            f"Complete the square to isolate {m(f'(x - {h})^2 \\ge 0')}!",
            [
                f"Rewrite as {m(f'(x - {h})^2 + {ans}') if sign == 1 else m(f'-(x - {h})^2 + {ans}')}.",
                f"Since {m(f'(x - {h})^2 \\ge 0')} for every real {m('x')}, equality {m(f'(x - {h})^2 = 0')} occurs at {m(f'x = {h}')}.",
                f"Thus the extreme value is {m(ans)} (not the {m('x')}-coordinate {m(h)}!).",
            ],
            f"Always distinguish **where** the extremum occurs ({m(f'x = {h}')}) from **what** the extremum equals ({m(ans)})!",
            f"نكمل المربع لعزل المقدار غير السالب {m(f'(x - {h})^2')}!",
            [
                f"نكتب كثير الحدود بالصورة الرأسية عند {m(f'x = {h}')}.",
                f"ينعدم القوس المربّع عند {m(f'x = {h}')}.",
                f"إذن القيمة القصوى المطلوبة هي {m(ans)}.",
            ],
            f"انتبه لعدم الخلط بين إحداثي الرأس {m(f'x = {h}')} والقيمة القصوى نفسها وهي {m(ans)}!",
            diagram_en=svg_parabola_roots("", "", f"V({h}, {ans})"),
        )

    for a_c, h, k_min in [(2, 3, 7), (3, 2, 11), (4, 3, 5)]:
        c_val = a_c * h * h + k_min
        B.add_math(
            tp, "Medium", bp,
            f"Find the minimum possible value of {m(f'{a_c}x^2 - {2*a_c*h}x + {c_val}')} over all real numbers {m('x')}.",
            f"أوجد أصغر قيمة ممكنة للمقدار {m(f'{a_c}x^2 - {2*a_c*h}x + {c_val}')} لجميع الأعداد الحقيقية {m('x')}.",
            k_min, [c_val - h * h, c_val, h, k_min + a_c * h],
            f"Factor {m(a_c)} out of the first two terms: {m(f'{a_c}(x^2 - {2*h}x) + {c_val}')} — remember subtracting {m(f'{h}^2')} inside the bracket subtracts {m(f'{a_c} \\times {h}^2')} outside!",
            f"أخرج {m(a_c)} عاملاً مشتركاً من أول حدين، وانتبه أن طرح {m(f'{h}^2')} داخل القوس يعني طرح {m(f'{a_c} \\times {h}^2')} خارجه!",
            f"Factor out {m(a_c)} carefully so you subtract {m(f'{a_c} \\cdot {h}^2 = {a_c*h*h}')}, not just {m(h*h)}!",
            [
                f"Write {m(f'{a_c}(x^2 - {2*h}x) + {c_val} = {a_c}\\big((x - {h})^2 - {h*h}\\big) + {c_val}')}.",
                f"Distribute {m(a_c)}: {m(f'{a_c}(x - {h})^2 + ({c_val} - {a_c*h*h}) = {a_c}(x - {h})^2 + {k_min}')}.",
                f"Since {m(f'{a_c}(x - {h})^2 \\ge 0')}, the minimum value is {m(k_min)} (at {m(f'x = {h}')}).",
            ],
            f"Subtracting {m(h*h)} instead of {m(a_c*h*h)} gives the classic trap {m(c_val - h*h)}!",
            f"نخرج {m(a_c)} عاملاً مشتركاً ونطرح {m(f'{a_c} \\times {h}^2 = {a_c*h*h}')} من الحد الثابت!",
            [
                f"نكتب المقدار: {m(f'{a_c}((x - {h})^2 - {h*h}) + {c_val}')}.",
                f"نبسّط الثوابت: {m(f'{a_c}(x - {h})^2 + ({c_val} - {a_c*h*h}) = {a_c}(x - {h})^2 + {k_min}')}.",
                f"أصغر قيمة هي {m(k_min)} وتتحقق عند {m(f'x = {h}')}.",
            ],
            f"انتبه: طرح {m(h*h)} فقط دون ضربه في {m(a_c)} يوقع في الفخ {m(c_val - h*h)}!",
            diagram_en=svg_parabola_roots("", "", f"Min={k_min}"),
        )

    for p, q, k_min in [(2, 5, 9), (4, 3, 12), (5, 6, 8)]:
        C = p * p + q * q + k_min
        B.add_math(
            tp, "Medium", bp,
            f"For real numbers {m('x')} and {m('y')}, find the minimum value of {m(f'x^2 + {2*p}x + y^2 - {2*q}y + {C}')}.",
            f"للأعداد الحقيقية {m('x')} و{m('y')}، أوجد أصغر قيمة للمقدار {m(f'x^2 + {2*p}x + y^2 - {2*q}y + {C}')}.",
            k_min, [C, C - p * p, C - q * q, k_min + p + q],
            f"Complete the square in {m('x')} and in {m('y')} separately.",
            f"أكمل المربع لحدود {m('x')} ولحدود {m('y')} كلاً على حدة.",
            f"Rewrite as {m(f'(x + {p})^2 + (y - {q})^2 + {k_min}')}!",
            [
                f"Group {m(f'x^2 + {2*p}x = (x + {p})^2 - {p*p}')} and {m(f'y^2 - {2*q}y = (y - {q})^2 - {q*q}')}.",
                f"Combine constants: {m(f'{C} - {p*p} - {q*q} = {k_min}')}.",
                f"Both squares vanish simultaneously at {m(f'(x, y) = (-{p}, {q})')}, giving minimum {m(k_min)}.",
            ],
            f"Check at {m(f'(-{p}, {q})')}: {m(f'{p*p} - {2*p*p} + {q*q} - {2*q*q} + {C} = {k_min}')}!",
            f"نكمل المربع في المتغيرين معاً لنحصل على مجموع مربعين زائد ثابت!",
            [
                f"نكتب المقدار: {m(f'(x + {p})^2 + (y - {q})^2 + ({C} - {p*p} - {q*q})')}.",
                f"الثابت المتبقي يساوي {m(k_min)}.",
                f"بما أن المربعين {m('\\ge 0')} وينعدمان عند {m(f'(-{p}, {q})')}، فأصغر قيمة هي {m(k_min)}.",
            ],
            f"تحقق بالتعويض المباشر عند {m(f'(-{p}, {q})')} يعطي {m(k_min)}.",
        )

    for k_y, m_min in [(3, 6), (4, 11)]:
        C = k_y * k_y + m_min
        B.add_math(
            tp, "Hard", bp,
            f"Over all real numbers {m('x')} and {m('y')}, what is the minimum value of {m(f'x^2 + 2xy + 2y^2 - {2*k_y}y + {C}')}?",
            f"لجميع الأعداد الحقيقية {m('x')} و{m('y')}، ما أصغر قيمة للمقدار {m(f'x^2 + 2xy + 2y^2 - {2*k_y}y + {C}')}؟",
            m_min, [C, C - k_y * k_y // 2, m_min - k_y, m_min + k_y],
            f"Split {m('2y^2')} into {m('y^2 + y^2')}: use the first {m('y^2')} to form {m('(x + y)^2')} and the second {m('y^2')} to complete the square with {m(f'-{2*k_y}y')}!",
            f"جزّئ {m('2y^2')} إلى {m('y^2 + y^2')}؛ الأول يكوّن {m('(x + y)^2')} والثاني يكمل المربع مع {m(f'-{2*k_y}y')}!",
            f"Split {m('2y^2 = y^2 + y^2')} to decouple {m('(x + y)^2')} and {m(f'(y - {k_y})^2')}!",
            [
                f"Rewrite {m(f'x^2 + 2xy + 2y^2 - {2*k_y}y + {C} = (x^2 + 2xy + y^2) + (y^2 - {2*k_y}y + {k_y*k_y}) + {m_min}')}.",
                f"This equals {m(f'(x + y)^2 + (y - {k_y})^2 + {m_min} \\ge {m_min}')}.",
                f"Setting {m(f'y = {k_y}')} and {m(f'x = -{k_y}')} makes **both** squares {m(0)}, achieving {m(m_min)}!",
            ],
            f"Check at {m(f'(x, y) = (-{k_y}, {k_y})')}: {m(f'{k_y*k_y} - {2*k_y*k_y} + {2*k_y*k_y} - {2*k_y*k_y} + {C} = {m_min}')}!",
            f"نفصل {m('2y^2')} إلى {m('y^2 + y^2')} ليتكون لدينا مجموع مربعين كاملين مستقلين!",
            [
                f"نعيد الترتيب: {m(f'(x + y)^2 + (y - {k_y})^2 + ({C} - {k_y*k_y})')}.",
                f"ينعدم القوسان معاً عند {m(f'y = {k_y}')} و{m(f'x = -{k_y}')}.",
                f"إذن القيمة الصغرى هي {m(m_min)}.",
            ],
            f"تحقق عند {m(f'(-{k_y}, {k_y})')}: القيمة الناتجة تساوي {m(m_min)} بالضبط.",
        )

    for M_num, h, d_den in [(72, 3, 6), (90, 4, 5)]:
        c_den = h * h + d_den
        ans = M_num // d_den
        B.add_math(
            tp, "Hard", bp,
            f"What is the **maximum** possible value of the rational expression {m(f'\\frac{{{M_num}}}{{x^2 - {2*h}x + {c_den}}}')} over all real numbers {m('x')}?",
            f"ما **أكبر** قيمة ممكنة للمقدار الكسري {m(f'\\frac{{{M_num}}}{{x^2 - {2*h}x + {c_den}}}')} لجميع الأعداد الحقيقية {m('x')}؟",
            ans, [d_den, M_num // c_den if M_num % c_den == 0 else ans - 3, ans + 3, h * d_den],
            f"Since the numerator {m(M_num)} is positive and fixed, **maximizing** the fraction is equivalent to **minimizing** its positive denominator!",
            f"بما أن البسط {m(M_num)} موجب وثابت، فإن **تكبير** الكسر يكافئ **تصغير** مقامه الموجب!",
            f"Minimize the denominator {m(f'(x - {h})^2 + {d_den}')} to maximize the fraction!",
            [
                f"Complete the square in the denominator: {m(f'x^2 - {2*h}x + {c_den} = (x - {h})^2 + {d_den} \\ge {d_den} > 0')}.",
                f"The denominator reaches its minimum {m(d_den)} at {m(f'x = {h}')}.",
                f"Hence the fraction reaches its maximum {m(f'{M_num} / {d_den} = {ans}')}.",
            ],
            f"At {m(f'x = {h}')}, the expression equals {m(ans)}, and for every other {m('x')} the denominator exceeds {m(d_den)}.",
            f"نكمل المربع لتصغير المقام الموجب، فيبلغ الكسر أكبر قيمة له!",
            [
                f"المقام يساوي {m(f'(x - {h})^2 + {d_den}')} وأصغر قيمة له هي {m(d_den)} عند {m(f'x = {h}')}.",
                f"نقسم البسط {m(M_num)} على أصغر مقام {m(d_den)}.",
                f"أكبر قيمة للكسر هي {m(f'{M_num} \\div {d_den} = {ans}')}.",
            ],
            f"انتبه: القيمة الصغرى للمقام هي {m(d_den)}، أما القيمة العظمى للكسر فهي {m(ans)}!",
            diagram_en=svg_parabola_roots("", "", f"Max={ans}"),
        )

    # 3. nsmo_g89_absolute_value_equation (5E, 6M, 4H) — SVG: svg_coord_diamond / svg_number_strip
    bp = "nsmo_g89_absolute_value_equation"
    for a0, b0, c0 in [(5, 7, 3), (6, 9, 4), (8, 10, 3)]:
        sols = [a0 + b0 + c0, a0 + b0 - c0, a0 - b0 + c0, a0 - b0 - c0]
        assert all(abs(abs(x - a0) - b0) == c0 for x in sols)
        ans = sum(sols)
        B.add_math(
            tp, "Easy", bp,
            f"Find the **sum** of all real solutions {m('x')} to the nested absolute-value equation {m(f'||x - {a0}| - {b0}| = {c0}')}.",
            f"أوجد **مجموع** جميع الحلول الحقيقية {m('x')} لمعادلة القيمة المطلقة المتداخلة {m(f'||x - {a0}| - {b0}| = {c0}')}.",
            ans, [2 * a0, a0, 4 * b0, ans - a0],
            f"Peel the outer bars: {m(f'|x - {a0}| = {b0} \\pm {c0}')} gives {m(4)} solutions symmetric around {m(f'x = {a0}')}!",
            f"فك القيمة المطلقة الخارجية إلى {m(f'|x - {a0}| = {b0} \\pm {c0}')} فتحصل على {m(4)} حلول متناظرة حول {m(f'x = {a0}')}!",
            f"Exploit symmetry around {m(f'x = {a0}')} after verifying both {m(f'{b0} \\pm {c0} > 0')}!",
            [
                f"Removing the outer bars gives {m(f'|x - {a0}| = {b0 + c0}')} or {m(f'|x - {a0}| = {b0 - c0}')}.",
                f"Since both {m(b0 + c0)} and {m(b0 - c0)} are positive, we get {m(4)} distinct solutions {m(f'{a0} \\pm {b0 + c0}')} and {m(f'{a0} \\pm {b0 - c0}')}.",
                f"Both {m('\\pm')} pairs average to {m(a0)}, so the sum of all {m(4)} solutions is {m(f'4 \\times {a0} = {ans}')}.",
            ],
            f"Explicit roots: {m(', '.join(str(v) for v in sorted(sols)))} — their sum is {m(ans)}!",
            f"نفك القيمتين المطلقتين ونستثمر تناظر الحلول الأربعة حول {m(a0)}!",
            [
                f"ينتج {m(f'|x - {a0}| = {b0 + c0}')} أو {m(f'|x - {a0}| = {b0 - c0}')} وكلاهما موجب.",
                f"للمعادلة {m(4)} حلول هي {m(f'{a0} \\pm {b0+c0}')} و{m(f'{a0} \\pm {b0-c0}')}.",
                f"مجموع الحلول الأربعة يساوي {m(f'4 \\times {a0} = {ans}')}.",
            ],
            f"انتبه: لو كان {m('b - c < 0')} لكان لدينا حلان فقط مجموعهما {m(2*a0)}!",
            diagram_en=svg_number_strip([str(v) for v in sorted(sols)]),
        )

    for a_c, b_c, c_c in [(3, 7, 15), (4, 9, 22)]:
        # |a_c * x - b_c| = c_c -> distance between the two roots is 2 * c_c / a_c -> pick divisible: (3, 7, 15) -> 10; (4, 9, 22) -> 11
        ans = (2 * c_c) // a_c
        B.add_math(
            tp, "Easy", bp,
            f"If {m('x_1')} and {m('x_2')} are the two solutions to {m(f'|{a_c}x - {b_c}| = {c_c}')}, what is the distance {m('|x_1 - x_2|')} between them?",
            f"إذا كان {m('x_1')} و{m('x_2')} هما حلا المعادلة {m(f'|{a_c}x - {b_c}| = {c_c}')}، فما المسافة {m('|x_1 - x_2|')} بينهما؟",
            ans, [2 * c_c, c_c // a_c if c_c % a_c == 0 else ans + 2, ans - 2, ans + 4],
            f"Solve {m(f'{a_c}x = {b_c} \\pm {c_c}')}; the constant {m(b_c)} cancels when subtracting the two roots!",
            f"من {m(f'{a_c}x = {b_c} \\pm {c_c}')} يختفي الثابت {m(b_c)} عند طرح الجذرين!",
            f"Subtract {m(f'x_1 = ({b_c} + {c_c})/{a_c}')} and {m(f'x_2 = ({b_c} - {c_c})/{a_c}')}!",
            [
                f"The two roots are {m(f'x_1 = \\frac{{{b_c} + {c_c}}}{{{a_c}}}')} and {m(f'x_2 = \\frac{{{b_c} - {c_c}}}{{{a_c}}}')}.",
                f"Subtract them: {m(f'x_1 - x_2 = \\frac{{2 \\times {c_c}}}{{{a_c}}} = \\frac{{{2*c_c}}}{{{a_c}}}')}.",
                f"Simplify to obtain {m(ans)}.",
            ],
            f"Dividing {m(f'|{a_c}x - {b_c}| = {c_c}')} by {m(a_c)} gives {m(f'|x - {b_c}/{a_c}| = {c_c}/{a_c}')}, radius {m(f'{c_c}/{a_c}')} and diameter {m(ans)}!",
            f"نطرح الجذرين فتختفي الإزاحة {m(b_c)} وتبقى المسافة {m(f'\\frac{{2 \\times {c_c}}}{{{a_c}}}')}!",
            [
                f"الجذران هما {m(f'\\frac{{{b_c} \\pm {c_c}}}{{{a_c}}}')}.",
                f"الفرق بينهما يساوي {m(f'\\frac{{2 \\times {c_c}}}{{{a_c}}} = \\frac{{{2*c_c}}}{{{a_c}}}')}.",
                f"الناتج يساوي {m(ans)}.",
            ],
            f"تحقق هندسي: نصف قطر الفترة هو {m(f'{c_c}/{a_c}')} وطولها الكلي (المسافة) هو {m(ans)}.",
        )

    for a0, b0, c0 in [(2, 7, 15), (-3, 4, 12), (1, 9, 20)]:
        ans = c0 - a0
        assert ans == min(abs(x - a0) + abs(x - b0) + abs(x - c0) for x in range(-20, 40))
        B.add_math(
            tp, "Medium", bp,
            f"Over all real numbers {m('x')}, what is the **minimum** value of {m(f'|x - ({a0})|' if a0 < 0 else f'|x - {a0}|')} {m(f'+ |x - {b0}| + |x - {c0}|')}?",
            f"لجميع الأعداد الحقيقية {m('x')}، ما **أصغر** قيمة للمجموع {m(f'|x + {-a0}|' if a0 < 0 else f'|x - {a0}|')} {m(f'+ |x - {b0}| + |x - {c0}|')}؟",
            ans, [ans + abs(b0 - a0), b0, c0 - b0, ans - 2],
            f"Place {m('x')} at the **median** of the three anchor points {m(f'{a0}, {b0}, {c0}')}!",
            f"ضع {m('x')} عند **الوسيط** بين النقاط الثلاث {m(f'{a0}, {b0}, {c0}')}!",
            f"By the median principle, {m('|x - a| + |x - b| + |x - c|')} is minimized at the middle point {m(f'x = {b0}')}!",
            [
                f"For any {m('x')}, the outer pair satisfies {m(f'|x - ({a0})| + |x - {c0}| \\ge {c0} - ({a0}) = {ans}')}, with equality for all {m(f'x \\in [{a0}, {c0}]')}.",
                f"Meanwhile {m(f'|x - {b0}| \\ge 0')}, with equality at {m(f'x = {b0} \\in [{a0}, {c0}]')}.",
                f"At {m(f'x = {b0}')}, both minimums occur simultaneously, giving {m(f'{ans} + 0 = {ans}')}!",
            ],
            f"Notice the middle anchor {m(b0)} vanishes at {m(f'x = {b0}')}, leaving just the span {m(f'{c0} - ({a0}) = {ans}')}!",
            f"وفق مبدأ الوسيط يتحقق أصغر مجموع للمسافات عند النقطة الوسطى {m(f'x = {b0}')}!",
            [
                f"مجموع المسافتين الطرفيتين يحقق دائماً {m(f'\\ge {c0} - ({a0}) = {ans}')} لكل نقطة بينهما.",
                f"وعند اختيار {m(f'x = {b0}')} تنعدم المسافة الوسطى {m(f'|x - {b0}| = 0')}.",
                f"إذن القيمة الصغرى للمجموع هي {m(ans)}.",
            ],
            f"تحقق عند {m(f'x = {b0}')}: {m(f'{b0 - a0} + 0 + {c0 - b0} = {ans}')}!",
            diagram_en=svg_number_strip([str(a0), f"x={b0}", str(c0), f"Min={ans}"]),
        )

    for R, x0, y0 in [(5, 1, -2), (7, -3, 4), (8, 0, 5)]:
        ans = 2 * R * R
        B.add_math(
            tp, "Medium", bp,
            f"Find the area of the closed region in the coordinate plane defined by {m(f'|x - {x0}| + |y - ({y0})| \\le {R}' if y0 < 0 else f'|x + {-x0}| + |y - {y0}| \\le {R}' if x0 < 0 else f'|x| + |y - {y0}| \\le {R}')}.",
            f"أوجد مساحة المنطقة المغلقة في المستوى الإحداثي المعرّفة بالمتباينة {m(f'|x - {x0}| + |y + {-y0}| \\le {R}' if y0 < 0 else f'|x + {-x0}| + |y - {y0}| \\le {R}' if x0 < 0 else f'|x| + |y - {y0}| \\le {R}')}.",
            ans, [R * R, 4 * R * R, 4 * R, ans - R],
            f"Shifting the center does not change area; {m(f'|u| + |v| \\le {R}')} is a rhombus with both diagonals equal to {m(2 * R)}!",
            f"إزاحة المركز لا تغيّر المساحة؛ المنطقة {m(f'|u| + |v| \\le {R}')} معين طول كل من قطريه المتعامدين {m(2 * R)}!",
            f"Translate to the origin and apply the coordinate-diamond area formula {m('2R^2')}!",
            [
                f"Translation to {m('(0, 0)')} gives {m(f'|u| + |v| \\le {R}')} without changing area.",
                f"The vertices {m(f'(\\pm {R}, 0)')} and {m(f'(0, \\pm {R})')} span perpendicular diagonals of length {m(2 * R)} each.",
                f"Area {m(f'= \\frac{{1}}{{2}}({2*R})({2*R}) = 2 \\times {R}^2 = {ans}')}.",
            ],
            f"Trap check: {m(4*R*R)} is the bounding axis-aligned square, and the diamond fills exact half of it ({m(ans)})!",
            f"ننقل المركز إلى نقطة الأصل ونحسب مساحة المعين الذي قطراه {m(2 * R)} و{m(2 * R)}!",
            [
                f"الإزاحة تحافظ على المساحة وتردّ المنطقة إلى {m(f'|u| + |v| \\le {R}')}.",
                f"طولا القطرين المتعامدين هما {m(2 * R)} و{m(2 * R)}.",
                f"المساحة {m(f'= \\frac{{1}}{{2}} \\times {2*R} \\times {2*R} = {ans}')}.",
            ],
            f"تحقق: المعين يشغل نصف مساحة المربع المحيط به ({m(4*R*R)}) أي {m(ans)}!",
            diagram_en=svg_coord_diamond(str(R)),
        )

    # 4 Hard absolute-value / lattice diamond questions
    ans_seg = sum(1 for x in range(-50, 50) if abs(x + 4) + abs(x - 9) == 13)
    assert ans_seg == 14
    B.add_math(
        tp, "Hard", bp,
        f"How many **integers** {m('x')} satisfy the equation {m('|x + 4| + |x - 9| = 13')}?",
        f"كم **عدداً صحيحاً** {m('x')} يحقق المعادلة {m('|x + 4| + |x - 9| = 13')}؟",
        14, [2, 12, 13, 15],
        f"Notice the distance between {m('-4')} and {m('9')} on the number line is {m('9 - (-4) = 13')}!",
        f"لاحظ أن المسافة بين {m('-4')} و{m('9')} على خط الأعداد تساوي {m('9 - (-4) = 13')} بالضبط!",
        f"Since {m('9 - (-4) = 13')}, **every** point in the entire closed interval {m('[-4, 9]')} is a solution!",
        [
            f"Interpret {m('|x - (-4)| + |x - 9|')} as the sum of distances from {m('x')} to {m('-4')} and {m('9')}.",
            f"Because {m('9 - (-4) = 13')}, equality holds iff {m('x')} lies between {m('-4')} and {m('9')} inclusive ({m('-4 \\le x \\le 9')}).",
            f"Count integers in {m('[-4, 9]')}: {m('9 - (-4) + 1 = 14')}.",
        ],
        f"Double-trap alert: algebraic autopilot often guesses '{m(2)} roots', and fencepost haste guesses {m(13)} instead of {m(14)}!",
        f"بما أن البعد بين {m('-4')} و{m('9')} هو {m(13)}، فإن **كل** نقطة في الفترة المغلقة {m('[-4, 9]')} تحقق المعادلة!",
        [
            f"المقدار يمثل مجموع بعدي {m('x')} عن النقطتين {m('-4')} و{m('9')}.",
            f"يتساوى مجموع البعدين مع {m(13)} إذا وفقط إذا كان {m('-4 \\le x \\le 9')}.",
            f"عدد الأعداد الصحيحة في الفترة الشاملة هو {m('9 - (-4) + 1 = 14')}.",
        ],
        f"انتبه من الفخين الشهيرين: الجواب ليس {m(2)} وليس {m(13)} بل {m(14)} عدداً صحيحاً!",
        diagram_en=svg_number_strip(["−4", "…", "9", "14 ints"]),
    )

    ans_ineq = sum(1 for x in range(-50, 50) if abs(x - 2) + abs(x - 10) <= 14)
    assert ans_ineq == 15
    B.add_math(
        tp, "Hard", bp,
        f"How many **integers** {m('x')} satisfy the inequality {m('|x - 2| + |x - 10| \\le 14')}?",
        f"كم **عدداً صحيحاً** {m('x')} يحقق المتباينة {m('|x - 2| + |x - 10| \\le 14')}؟",
        15, [9, 13, 14, 17],
        f"On {m('[2, 10]')} the sum is {m(8)}; outside {m('[2, 10]')}, moving {m('t')} units past either endpoint adds {m('2t')} to the sum!",
        f"على الفترة {m('[2, 10]')} يساوي المجموع {m(8)}؛ والابتعاد خارجها بمقدار {m('t')} يزيد المجموع بمقدار {m('2t')}!",
        f"Start from the flat plateau {m('[2, 10]')} of height {m(8)}, and extend {m('(14 - 8)/2 = 3')} units past each end!",
        [
            f"For {m('2 \\le x \\le 10')}, {m('|x - 2| + |x - 10| = 8')}.",
            f"Moving {m('t > 0')} units below {m(2)} or above {m(10)} makes the sum {m('8 + 2t \\le 14 \\implies t \\le 3')}.",
            f"Thus the solution interval is {m('[2 - 3,\\; 10 + 3] = [-1, 13]')}, containing {m('13 - (-1) + 1 = 15')} integers.",
        ],
        f"Endpoint check: at {m('x = -1')}, {m('3 + 11 = 14')}; at {m('x = 13')}, {m('11 + 3 = 14')}!",
        f"المجموع على الفترة {m('[2, 10]')} يساوي {m(8)}، والفائض {m('14 - 8 = 6')} يسمح بالتمدد {m(3)} وحدات من كل طرف!",
        [
            f"لكل {m('x \\in [2, 10]')} يكون المجموع ثابتاً ويساوي {m(8)}.",
            f"خارج الفترة يزداد المجموع بمعدل {m('2t')}، لذا {m('8 + 2t \\le 14 \\implies t \\le 3')}.",
            f"الفترة الكاملة هي {m('[-1, 13]')} وتضم {m('13 - (-1) + 1 = 15')} عدداً صحيحاً.",
        ],
        f"تحقق طرفي: عند {m('x = -1')} وعند {m('x = 13')} يساوي المجموع {m(14)} تماماً.",
    )

    for R in (5, 7):
        ans = 2 * R * R + 2 * R + 1
        assert ans == sum(1 for x in range(-R, R + 1) for y in range(-R, R + 1) if abs(x) + abs(y) <= R)
        B.add_math(
            tp, "Hard", bp,
            f"How many integer **lattice points** {m('(x, y) \\in \\mathbb{Z}^2')} satisfy {m(f'|x| + |y| \\le {R}')}?",
            f"كم نقطة ذات **إحداثيات صحيحة** {m('(x, y) \\in \\mathbb{Z}^2')} تحقق المتباينة {m(f'|x| + |y| \\le {R}')}؟",
            ans, [2 * R * R, (2 * R + 1) ** 2, ans - 1, 2 * R * R + 1],
            f"Count points column by column (for {m(f'x = 0')}, {m(f'|y| \\le {R}')} gives {m(2*R + 1)} points; for {m('|x| = k')}, {m('2(R - k) + 1')} points) or sum shells {m('1 + 4(1 + 2 + \\cdots + R)')}!",
            f"احسب النقاط على الطبقات المتتالية {m('|x| + |y| = k')}: نقطة الأصل {m(1)} زائد {m('4k')} لكل {m('k = 1, \\dots, R')}!",
            f"Sum concentric diamond shells: {m('1 + \\sum_{k=1}^{R} 4k = 2R^2 + 2R + 1')}!",
            [
                f"For {m('k = 0')}, {m('|x| + |y| = 0')} has {m(1)} point {m('(0,0)')}; for each {m('k \\ge 1')}, {m('|x| + |y| = k')} has exact {m('4k')} lattice points.",
                f"Sum for {m(f'k = 0, 1, \\dots, {R}')}: {m(f'1 + 4(1 + 2 + \\cdots + {R}) = 1 + 4 \\cdot \\frac{{{R}({R+1})}}{{2}}')}.",
                f"Evaluate {m(f'1 + 2({R})({R+1}) = {ans}')} (equivalently {m(f'{R}^2 + {R+1}^2 = {ans}')}).",
            ],
            f"Area vs lattice check: continuous area is {m(2*R*R)}, while discrete lattice count is {m(f'R^2 + (R+1)^2 = {ans}')}!",
            f"نجمع نقاط الطبقات المعينية المتمركزة: {m('1 + 4(1 + 2 + \\cdots + R) = R^2 + (R+1)^2')}!",
            [
                f"عند {m('k=0')} توجد نقطة واحدة، ولكل {m('1 \\le k \\le R')} تحوي القشرة {m('|x|+|y|=k')} أربع مضاعفات {m('4k')} من النقاط.",
                f"المجموع الكلي: {m(f'1 + 4 \\times \\frac{{{R} \\times {R+1}}}{{2}} = 1 + {2*R*(R+1)}')}.",
                f"الناتج يساوي {m(ans)} نقطة صحيحة.",
            ],
            f"انتبه: المساحة الهندسية {m(2*R*R)} أما عدد النقاط الشبكية الصحيحة فهو {m(ans)}!",
            diagram_en=svg_coord_diamond(str(R)),
        )

    # 4. nsmo_g89_harmonic_average_speed (5E, 6M, 4H) — SVG: svg_motion_timeline
    bp = "nsmo_g89_harmonic_average_speed"
    for v1, v2, c1, c2 in [
        (30, 70, "Abha", "Khamis"),
        (40, 60, "Riyadh", "Kharj"),
        (36, 45, "Jeddah", "Makkah"),
        (50, 75, "Yanbu", "Madinah"),
        (80, 120, "Tabuk", "Duba"),
    ]:
        ans = (2 * v1 * v2) // (v1 + v2)
        B.add_math(
            tp, "Easy", bp,
            f"A courier drives from {c1} to {c2} at {m(f'{v1}\\text{{ km/h}}')} and returns along the exact same road at {m(f'{v2}\\text{{ km/h}}')}. What is the average speed for the entire round trip, in {m('\\text{km/h}')}?",
            f"سافر سائق من المدينة أ إلى المدينة ب بسرعة {m(f'{v1}\\text{{ km/h}}')} ثم عاد على الطريق نفسه بسرعة {m(f'{v2}\\text{{ km/h}}')}. ما سرعته المتوسطة لرحلة الذهاب والإياب كاملةً بوحدة {m('\\text{km/h}')}؟",
            ans, [(v1 + v2) // 2 if (v1 + v2) % 2 == 0 else (v1 + v2 + 1) // 2, ans + 4, ans - 4, math.isqrt(v1 * v2)],
            f"Use the harmonic mean {m('\\frac{2 v_1 v_2}{v_1 + v_2}')}, never the arithmetic mean!",
            f"استخدم الوسط التوافقي {m('\\frac{2 v_1 v_2}{v_1 + v_2}')} ولا تستخدم الوسط الحسابي!",
            f"Apply the round-trip harmonic speed formula {m('\\frac{2 v_1 v_2}{v_1 + v_2}')}!",
            [
                f"Total distance is {m('2d')} and total time is {m(f'\\frac{{d}}{{{v1}}} + \\frac{{d}}{{{v2}}}')}.",
                f"Divide total distance by total time: {m(f'\\frac{{2 \\times {v1} \\times {v2}}}{{{v1} + {v2}}} = \\frac{{{2*v1*v2}}}{{{v1+v2}}}')}.",
                f"Simplifying gives {m(f'{ans}\\text{{ km/h}}')}.",
            ],
            f"Sanity check: {m(ans)} is strictly less than the arithmetic midpoint {m(f'({v1}+{v2})/2')}!",
            f"نطبق قانون السرعة المتوسطة التوافقية {m('\\frac{2 v_1 v_2}{v_1 + v_2}')}!",
            [
                f"بما أن المسافتين متساويتان، فالسرعة المتوسطة تساوي الوسط التوافقي للسرعتين.",
                f"نحسب: {m(f'\\frac{{2 \\times {v1} \\times {v2}}}{{{v1} + {v2}}} = \\frac{{{2*v1*v2}}}{{{v1+v2}}}')}.",
                f"الناتج يساوي {m(f'{ans}\\text{{ km/h}}')}.",
            ],
            f"تحقق: القيمة {m(ans)} أصغر دائماً من الوسط الحسابي للسرعتين!",
            diagram_en=svg_motion_timeline(c1, c2, "d", f"{v1} km/h", f"{v2} km/h", meet=False),
        )

    for v1, v_avg in [(40, 48), (60, 80), (30, 45)]:
        ans = (v1 * v_avg) // (2 * v1 - v_avg)
        assert (2 * v1 * ans) == v_avg * (v1 + ans)
        B.add_math(
            tp, "Medium", bp,
            f"A cyclist rides uphill from camp to a ridge at {m(f'{v1}\\text{{ km/h}}')} and coasts back down the same trail at a constant speed {m('v')}. If her average speed for the entire round trip is {m(f'{v_avg}\\text{{ km/h}}')}, find {m('v')} in {m('\\text{km/h}')}.",
            f"صعد دراج تلّاً بسرعة ثابتة {m(f'{v1}\\text{{ km/h}}')} ثم هبط على المسار نفسه بسرعة ثابتة {m('v')}. إذا كانت سرعته المتوسطة لرحلة الذهاب والإياب كاملةً {m(f'{v_avg}\\text{{ km/h}}')}، فأوجد {m('v')} بوحدة {m('\\text{km/h}')}.",
            ans, [2 * v_avg - v1, v_avg + (v_avg - v1) // 2, ans + 10, ans - 8],
            f"Solve {m(f'\\frac{{2 \\cdot {v1} \\cdot v}}{{{v1} + v}} = {v_avg}')} — note {m('v')} must be larger than {m(2*v_avg - v1)}!",
            f"حل المعادلة {m(f'\\frac{{2 \\cdot {v1} \\cdot v}}{{{v1} + v}} = {v_avg}')}؛ انتبه أن {m('v')} أكبر من {m(2*v_avg - v1)}!",
            f"Set {m(f'\\frac{{2 \\cdot {v1} v}}{{{v1} + v}} = {v_avg}')} and solve for {m('v')}!",
            [
                f"From {m(f'\\frac{{2({v1})v}}{{{v1} + v}} = {v_avg}')}, clear the denominator: {m(f'{2*v1}v = {v_avg}({v1} + v)')}.",
                f"Collect {m('v')}-terms: {m(f'({2*v1} - {v_avg})v = {v_avg * v1} \\implies {2*v1 - v_avg}v = {v_avg * v1}')}.",
                f"Divide: {m(f'v = {v_avg * v1} / {2*v1 - v_avg} = {ans}\\text{{ km/h}}')}.",
            ],
            f"Arithmetic-mean trap {m(f'2({v_avg}) - {v1} = {2*v_avg - v1}')} is too slow to pull the round-trip average up to {m(v_avg)}!",
            f"نعوّض في قانون الوسط التوافقي ثم نحل المعادلة الخطية في {m('v')}!",
            [
                f"نكتب {m(f'\\frac{{2 \\times {v1} \\times v}}{{{v1} + v}} = {v_avg}')} ونضرب الطرفين في {m(f'({v1} + v)')}.",
                f"نبسّط: {m(f'{2*v1 - v_avg}v = {v_avg * v1}')}.",
                f"بالقسمة نحصل على {m(f'v = {ans}\\text{{ km/h}}')}.",
            ],
            f"انتبه: الفخ الشائع {m(2*v_avg - v1)} يفترض الوسط الحسابي بدلاً من التوافقي!",
            diagram_en=svg_motion_timeline("Base", "Ridge", "d", f"{v1} km/h", "v = ?", meet=False),
        )

    for v1, v2, v3 in [(20, 30, 60), (30, 40, 120), (40, 60, 120)]:
        L = math.lcm(v1, v2, v3)
        ans = (3 * L) // (L // v1 + L // v2 + L // v3)
        B.add_math(
            tp, "Medium", bp,
            f"A rally car covers three equal-length stages at constant speeds of {m(f'{v1}\\text{{ km/h}}')}, {m(f'{v2}\\text{{ km/h}}')}, and {m(f'{v3}\\text{{ km/h}}')}. What is its average speed across all three stages combined, in {m('\\text{km/h}')}?",
            f"قطعت سيارة سباق ثلاث مراحل متساوية الطول بسرعات ثابتة هي {m(f'{v1}\\text{{ km/h}}')} و{m(f'{v2}\\text{{ km/h}}')} و{m(f'{v3}\\text{{ km/h}}')}. ما سرعتها المتوسطة للمراحل الثلاث مجتمعةً بوحدة {m('\\text{km/h}')}؟",
            ans, [(v1 + v2 + v3) // 3, ans + 5, ans - 5, v2],
            f"Choose each stage length to be {m(f'd = {L}\\text{{ km}}')} so every stage time is a tiny integer!",
            f"افرض طول كل مرحلة {m(f'd = {L}\\text{{ km}}')} لتصبح أزمنة المراحل الثلاث أعداداً صحيحة صغيرة!",
            f"Pick stage distance {m(f'd = \\operatorname{{lcm}}({v1}, {v2}, {v3}) = {L}\\text{{ km}}')} and divide {m('3d')} by total time!",
            [
                f"Let each stage be {m(f'{L}\\text{{ km}}')}, so total distance is {m(f'3 \\times {L} = {3*L}\\text{{ km}}')}.",
                f"Stage times are {m(f'{L}/{v1} = {L//v1}\\text{{ h}}')}, {m(f'{L}/{v2} = {L//v2}\\text{{ h}}')}, and {m(f'{L}/{v3} = {L//v3}\\text{{ h}}')} (sum {m(f'{L//v1 + L//v2 + L//v3}\\text{{ h}}')}).",
                f"Average speed {m(f'= \\frac{{{3*L}}}{{{L//v1 + L//v2 + L//v3}}} = {ans}\\text{{ km/h}}')}.",
            ],
            f"Three-term harmonic mean {m('\\frac{3}{1/v_1 + 1/v_2 + 1/v_3}')} beats the arithmetic-mean trap!",
            f"نفرض طول كل مرحلة {m(f'{L}\\text{{ km}}')} ونقسم المسافة الكلية {m(3*L)} على مجموع الأزمنة!",
            [
                f"المسافة الكلية للمراحل الثلاث هي {m(f'3 \\times {L} = {3*L}\\text{{ km}}')}.",
                f"الأزمنة هي {m(L//v1)} و{m(L//v2)} و{m(L//v3)} ساعات، ومجموعها {m(L//v1 + L//v2 + L//v3)} ساعات.",
                f"السرعة المتوسطة {m(f'= {3*L} \\div {L//v1 + L//v2 + L//v3} = {ans}\\text{{ km/h}}')}.",
            ],
            f"تحقق: الوسط التوافقي لثلاث سرعات يساوي {m(ans)} وليس متوسطها الحسابي!",
        )

    for v1, v2 in [(30, 60), (40, 80)]:
        # First 1/3 of distance at v1, remaining 2/3 of distance at v2 -> 3*v1*v2 / (v2 + 2*v1) -> (30,60)->45, (40,80)->60
        ans = (3 * v1 * v2) // (v2 + 2 * v1)
        B.add_math(
            tp, "Hard", bp,
            f"A train travels the first {m('\\frac{1}{3}')} of the distance between two stations at {m(f'{v1}\\text{{ km/h}}')} and the remaining {m('\\frac{2}{3}')} of the distance at {m(f'{v2}\\text{{ km/h}}')}. What is its average speed for the whole trip, in {m('\\text{km/h}')}?",
            f"قطع قطار الثلث الأول {m('\\frac{1}{3}')} من المسافة بين محطتين بسرعة {m(f'{v1}\\text{{ km/h}}')}، والثلثين المتبقيين {m('\\frac{2}{3}')} بسرعة {m(f'{v2}\\text{{ km/h}}')}. ما سرعته المتوسطة للرحلة كاملةً بوحدة {m('\\text{km/h}')}؟",
            ans, [(v1 + 2 * v2) // 3, (v1 + v2) // 2, ans - 5, ans + 5],
            f"Pick a convenient total distance divisible by {m(3)} and both speeds, such as {m(f'{3 * v2}\\text{{ km}}')}!",
            f"اختر مسافة كلية تقبل القسمة على {m(3)} وعلى السرعتين معاً، مثل {m(f'{3 * v2}\\text{{ km}}')}!",
            f"Set total distance {m(f'D = {3*v2}\\text{{ km}}')} and compute {m('D / (t_1 + t_2)')}!",
            [
                f"Choose {m(f'D = {3*v2}\\text{{ km}}')}: the first leg is {m(f'{v2}\\text{{ km}}')} at {m(v1)} (taking {m(f'{v2}/{v1} = {v2//v1}\\text{{ h}}')}).",
                f"The second leg is {m(f'{2*v2}\\text{{ km}}')} at {m(v2)} (taking {m(f'{2*v2}/{v2} = 2\\text{{ h}}')}).",
                f"Total time is {m(f'{v2//v1 + 2}\\text{{ h}}')}, so average speed is {m(f'{3*v2} / {v2//v1 + 2} = {ans}\\text{{ km/h}}')}.",
            ],
            f"Weighted-arithmetic trap {m(f'\\frac{{1}}{{3}}({v1}) + \\frac{{2}}{{3}}({v2})')} applies to **time** fractions, not **distance** fractions!",
            f"نفرض المسافة الكلية {m(f'{3*v2}\\text{{ km}}')} ونحسب زمن كل جزء على حدة!",
            [
                f"الثلث الأول طوله {m(v2)} كم ويستغرق {m(f'{v2} \\div {v1} = {v2//v1}')} ساعات.",
                f"الثلثان المتبقيان طولهما {m(2*v2)} كم ويستغرقان {m(2)} ساعتين، فالزمن الكلي {m(v2//v1 + 2)} ساعات.",
                f"السرعة المتوسطة {m(f'= {3*v2} \\div {v2//v1 + 2} = {ans}\\text{{ km/h}}')}.",
            ],
            f"انتبه: المتوسط المرجح {m('\\frac{1}{3}v_1 + \\frac{2}{3}v_2')} يصح عندما تكون النسب من **الزمن** لا من **المسافة**!",
            diagram_en=svg_motion_timeline("Station A", "Station B", "1/3 D + 2/3 D", f"{v1} km/h", f"{v2} km/h", meet=False),
        )

    for gap_km, v_slow, v_fast in [(45, 75, 90), (60, 80, 100)]:
        # Head start: freight leaves at v_slow, express leaves later (when freight is gap_km ahead) at v_fast -> catch-up time = gap / (v_fast - v_slow) hours -> distance from start = v_fast * t!
        t_hr = gap_km // (v_fast - v_slow)
        ans = v_fast * t_hr
        B.add_math(
            tp, "Hard", bp,
            f"A cargo van leaves Riyadh traveling at {m(f'{v_slow}\\text{{ km/h}}')}. When it is {m(f'{gap_km}\\text{{ km}}')} ahead, a patrol car departs from the same point along the same highway at {m(f'{v_fast}\\text{{ km/h}}')}. How many kilometers from Riyadh does the patrol car catch up to the van?",
            f"انطلقت شاحنة من الرياض بسرعة {m(f'{v_slow}\\text{{ km/h}}')}. وعندما أصبحت على بعد {m(f'{gap_km}\\text{{ km}}')}، انطلقت سيارة دورية من النقطة نفسها وعلى الطريق نفسه بسرعة {m(f'{v_fast}\\text{{ km/h}}')}. على بُعد كم كيلومتراً من الرياض تلحق الدورية بالشاحنة؟",
            ans, [v_slow * t_hr, gap_km * t_hr, ans - gap_km // 2, ans + v_fast],
            f"Use relative closing speed {m(f'{v_fast} - {v_slow} = {v_fast - v_slow}\\text{{ km/h}}')} to find catch-up time first!",
            f"استخدم سرعة الاقتراب النسبية {m(f'{v_fast} - {v_slow} = {v_fast - v_slow}\\text{{ km/h}}')} لإيجاد زمن اللحاق أولاً!",
            f"Divide the {m(f'{gap_km}\\text{{ km}}')} gap by relative speed {m(f'{v_fast - v_slow}\\text{{ km/h}}')}, then multiply by {m(v_fast)}!",
            [
                f"The patrol car closes the gap at {m(f'{v_fast} - {v_slow} = {v_fast - v_slow}\\text{{ km/h}}')}.",
                f"Catch-up time is {m(f'{gap_km} / {v_fast - v_slow} = {t_hr}\\text{{ hours}}')}.",
                f"Distance from Riyadh equals {m(f'{v_fast} \\times {t_hr} = {ans}\\text{{ km}}')} (matching {m(f'{gap_km} + {v_slow} \\times {t_hr} = {ans}\\text{{ km}}')}).",
            ],
            f"Watch the trap {m(v_slow * t_hr)}, which forgets to add the van's initial {m(f'{gap_km}\\text{{ km}}')} head start!",
            f"نقسم الفارق المبدئي {m(gap_km)} كم على فرق السرعتين {m(v_fast - v_slow)} كم/س ثم نضرب في {m(v_fast)}!",
            [
                f"سرعة اللحاق النسبية هي {m(f'{v_fast} - {v_slow} = {v_fast - v_slow}\\text{{ km/h}}')}.",
                f"زمن اللحاق يساوي {m(f'{gap_km} \\div {v_fast - v_slow} = {t_hr}')} ساعات.",
                f"المسافة من الرياض تساوي {m(f'{v_fast} \\times {t_hr} = {ans}\\text{{ km}}')}.",
            ],
            f"تحقق للشاحنة: {m(f'{gap_km} + {v_slow} \\times {t_hr} = {ans}\\text{{ km}}')} أيضاً!",
            diagram_en=svg_motion_timeline("Riyadh", "Catch-up", f"Gap {gap_km} km", f"{v_fast} km/h", f"{v_slow} km/h", meet=False),
        )

    # 5. nsmo_g89_arithmetic_geometric_seq (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g89_arithmetic_geometric_seq"
    for a1, d, p, q, r in [(5, 4, 3, 8, 15), (7, 6, 4, 9, 14), (10, 3, 5, 11, 20)]:
        ap = a1 + (p - 1) * d
        aq = a1 + (q - 1) * d
        ans = a1 + (r - 1) * d
        B.add_math(
            tp, "Easy", bp,
            f"In an arithmetic sequence {m('(a_n)')}, {m(f'a_{{{p}}} = {ap}')} and {m(f'a_{{{q}}} = {aq}')}. What is the value of {m(f'a_{{{r}}}')}?",
            f"في متتالية حسابية {m('(a_n)')}، إذا كان {m(f'a_{{{p}}} = {ap}')} و{m(f'a_{{{q}}} = {aq}')}، فما قيمة الحد {m(f'a_{{{r}}}')}؟",
            ans, [ans - d, ans + d, ap + aq, a1 + r * d],
            f"Find the common difference {m(f'd = \\frac{{a_{{{q}}} - a_{{{p}}}}}{{{q} - {p}}}')} first.",
            f"أوجد أساس المتتالية أولاً: {m(f'd = \\frac{{a_{{{q}}} - a_{{{p}}}}}{{{q} - {p}}}')}.",
            f"Compute step {m('d')} from the index gap {m(f'{q} - {p}')}, then jump {m(f'{r} - {q}')} more steps!",
            [
                f"Common difference {m(f'd = \\frac{{{aq} - {ap}}}{{{q} - {p}}} = {d}')}.",
                f"Step directly from {m(f'a_{{{q}}}')}: {m(f'a_{{{r}}} = a_{{{q}}} + ({r} - {q})d')}.",
                f"Evaluate {m(f'{aq} + {r - q} \\times {d} = {ans}')}.",
            ],
            f"No need to backtrack to {m('a_1')} when you can step straight from {m(f'a_{{{q}}}')} to {m(f'a_{{{r}}}')}!",
            f"نحسب الأساس {m('d')} من فرق الحدين على فرق رتبتيهما ثم نقفز مباشرة إلى {m(f'a_{{{r}}}')}!",
            [
                f"أساس المتتالية {m(f'd = \\frac{{{aq} - {ap}}}{{{q} - {p}}} = {d}')}.",
                f"ننتقل من {m(f'a_{{{q}}}')} بمقدار {m(r - q)} خطوة: {m(f'{aq} + {r - q} \\times {d}')}.",
                f"إذن {m(f'a_{{{r}}} = {ans}')}.",
            ],
            f"تحقق: الحد الأول {m(f'a_1 = {a1}')} والحد العام {m(f'{a1} + ({r}-1)\\times {d} = {ans}')}.",
            diagram_en=svg_number_strip([f"a_{p}={ap}", f"a_{q}={aq}", f"d={d}", f"a_{r}=?"]),
        )

    for g2, r_gp, n_ask in [(6, 2, 7), (6, 3, 5)]:
        g5 = g2 * (r_gp ** 3)
        ans = g2 * (r_gp ** (n_ask - 2))
        B.add_math(
            tp, "Easy", bp,
            f"In a geometric sequence of positive numbers, {m(f'g_2 = {g2}')} and {m(f'g_5 = {g5}')}. Find {m(f'g_{{{n_ask}}}')}.",
            f"في متتالية هندسية حدودها موجبة، {m(f'g_2 = {g2}')} و{m(f'g_5 = {g5}')}. أوجد قيمة {m(f'g_{{{n_ask}}}')}.",
            ans, [ans // r_gp, ans * r_gp, g5 + (n_ask - 5) * (g5 - g2) // 3, g2 * (r_gp ** (n_ask - 1))],
            f"Divide {m(f'g_5 / g_2 = r^3 = {g5 // g2}')} to find the common ratio {m('r')}.",
            f"اقسم {m(f'g_5 / g_2 = r^3 = {g5 // g2}')} لإيجاد أساس المتتالية الهندسية {m('r')}.",
            f"Take the cube root of {m(f'g_5 / g_2 = {r_gp**3}')} to find {m(f'r = {r_gp}')}!",
            [
                f"Since {m('g_5 = g_2 \\cdot r^3')}, we have {m(f'r^3 = {g5} / {g2} = {r_gp**3} \\implies r = {r_gp}')}.",
                f"Multiply from {m('g_2')}: {m(f'g_{{{n_ask}}} = g_2 \\cdot r^{{{n_ask - 2}}}')}.",
                f"Compute {m(f'{g2} \\times {r_gp}^{{{n_ask - 2}}} = {ans}')}.",
            ],
            f"Check: {m(f'g_5 \\cdot r^{{{n_ask - 5}}} = {g5} \\times {r_gp**(n_ask - 5)} = {ans}')}!",
            f"نستخرج الأساس {m('r')} من قسمة {m('g_5 / g_2 = r^3')} ثم نضرب للوصول إلى {m(f'g_{{{n_ask}}}')}!",
            [
                f"من {m(f'r^3 = {g5} \\div {g2} = {r_gp**3}')} نجد {m(f'r = {r_gp}')}.",
                f"نحسب {m(f'g_{{{n_ask}}} = g_2 \\times r^{{{n_ask - 2}}}')}.",
                f"الناتج يساوي {m(f'{g2} \\times {r_gp**(n_ask - 2)} = {ans}')}.",
            ],
            f"انتبه: الأس هو {m(f'{n_ask} - 2 = {n_ask - 2}')} عند الانطلاق من {m('g_2')}!",
        )

    for n_cnt, k_idx, pair_sum in [(15, 3, 48), (18, 4, 35), (21, 5, 40)]:
        j_idx = n_cnt + 1 - k_idx
        ans = (n_cnt * pair_sum) // 2
        B.add_math(
            tp, "Medium", bp,
            f"In an arithmetic sequence {m('(a_n)')}, {m(f'a_{{{k_idx}}} + a_{{{j_idx}}} = {pair_sum}')}. What is the sum {m(f'S_{{{n_cnt}}} = a_1 + a_2 + \\cdots + a_{{{n_cnt}}}')} of the first {m(n_cnt)} terms?",
            f"في متتالية حسابية {m('(a_n)')}، يُعلم أن {m(f'a_{{{k_idx}}} + a_{{{j_idx}}} = {pair_sum}')}. ما مجموع أول {m(n_cnt)} حداً {m(f'S_{{{n_cnt}}} = a_1 + a_2 + \\cdots + a_{{{n_cnt}}}')}؟",
            ans, [n_cnt * pair_sum, ans - pair_sum, ans + pair_sum // 2, (n_cnt - 1) * pair_sum // 2],
            f"Check the index sum: {m(f'{k_idx} + {j_idx} = {n_cnt + 1} = 1 + {n_cnt}')}, so {m(f'a_{{{k_idx}}} + a_{{{j_idx}}} = a_1 + a_{{{n_cnt}}}')}!",
            f"لاحظ مجموع الرتبتين: {m(f'{k_idx} + {j_idx} = {n_cnt + 1} = 1 + {n_cnt}')}، إذن {m(f'a_{{{k_idx}}} + a_{{{j_idx}}} = a_1 + a_{{{n_cnt}}}')}!",
            f"Use symmetric AP pairing: {m(f'a_{{{k_idx}}} + a_{{{j_idx}}} = a_1 + a_{{{n_cnt}}}')}!",
            [
                f"In any AP, whenever {m('i + j = p + q')}, {m('a_i + a_j = a_p + a_q')}.",
                f"Since {m(f'{k_idx} + {j_idx} = 1 + {n_cnt}')}, we immediately have {m(f'a_1 + a_{{{n_cnt}}} = {pair_sum}')}.",
                f"Therefore {m(f'S_{{{n_cnt}}} = \\frac{{{n_cnt}(a_1 + a_{{{n_cnt}}})}}{{2}} = \\frac{{{n_cnt} \\times {pair_sum}}}{{2}} = {ans}')}.",
            ],
            f"Even though {m('a_1')} and {m('d')} cannot be determined individually, {m(f'S_{{{n_cnt}}}')} is uniquely fixed at {m(ans)}!",
            f"نستثمر تماثل الرتب في المتتالية الحسابية: {m(f'a_1 + a_{{{n_cnt}}} = a_{{{k_idx}}} + a_{{{j_idx}}} = {pair_sum}')}!",
            [
                f"بما أن {m(f'{k_idx} + {j_idx} = {n_cnt + 1} = 1 + {n_cnt}')} فإن {m(f'a_1 + a_{{{n_cnt}}} = {pair_sum}')}.",
                f"نعوّض في قانون المجموع {m(f'S_{{{n_cnt}}} = \\frac{{{n_cnt}}}{{2}}(a_1 + a_{{{n_cnt}}})')}.",
                f"نحسب: {m(f'\\frac{{{n_cnt} \\times {pair_sum}}}{{2}} = {ans}')}.",
            ],
            f"روعة الفكرة: لا نحتاج معرفة {m('a_1')} أو {m('d')} منفردين لأن مجموع الطرفين معلوم!",
            diagram_en=svg_number_strip(["a₁", f"a_{k_idx}+a_{j_idx}={pair_sum}", f"a_{n_cnt}", f"S_{n_cnt}=?"]),
        )

    for a_sub, b_add in [(3, 6), (4, 12), (6, 15)]:
        ans = (a_sub * b_add) // (b_add - a_sub)
        assert ans * ans == (ans - a_sub) * (ans + b_add)
        B.add_math(
            tp, "Medium", bp,
            f"For what real number {m('x')} do the three terms {m(f'x - {a_sub}')}, {m('x')}, and {m(f'x + {b_add}')} form three consecutive terms of a **geometric** sequence?",
            f"لأي عدد حقيقي {m('x')} تشكّل الحدود الثلاثة {m(f'x - {a_sub}')} و{m('x')} و{m(f'x + {b_add}')} ثلاثة حدود متتالية في متتالية **هندسية**؟",
            ans, [ans + 2, (b_add + a_sub) // 2, b_add - a_sub, ans * 2],
            f"Set the square of the middle term equal to the product of its neighbors: {m(f'x^2 = (x - {a_sub})(x + {b_add})')}.",
            f"اجعل مربع الحد الأوسط مساوياً لحاصل ضرب جاريه: {m(f'x^2 = (x - {a_sub})(x + {b_add})')}.",
            f"Apply the geometric-mean condition {m(f'x^2 = (x - {a_sub})(x + {b_add})')}; {m('x^2')} cancels cleanly!",
            [
                f"In a geometric sequence, {m(f'x^2 = (x - {a_sub})(x + {b_add}) = x^2 + {b_add - a_sub}x - {a_sub * b_add}')}.",
                f"Subtract {m('x^2')} from both sides: {m(f'{b_add - a_sub}x = {a_sub * b_add}')}.",
                f"Divide by {m(b_add - a_sub)}: {m(f'x = {ans}')} (giving the GP {m(f'{ans - a_sub},\\; {ans},\\; {ans + b_add}')}).",
            ],
            f"Ratio check: {m(f'{ans} / {ans - a_sub} = {ans + b_add} / {ans}')}!",
            f"نطبق شرط الوسط الهندسي {m(f'x^2 = (x - {a_sub})(x + {b_add})')} فتختصر {m('x^2')} فوراً!",
            [
                f"بفك الطرف الأيمن: {m(f'x^2 = x^2 + {b_add - a_sub}x - {a_sub * b_add}')}.",
                f"نحذف {m('x^2')} من الطرفين فنجد {m(f'{b_add - a_sub}x = {a_sub * b_add}')}.",
                f"إذن {m(f'x = {ans}')}.",
            ],
            f"تحقق: الحدود الثلاثة هي {m(f'{ans - a_sub}, {ans}, {ans + b_add}')} وهي متتالية هندسية فعلاً!",
        )

    for b_mid, d_ap, c1, c2, c3 in [(6, 3, 1, 2, 7), (9, 5, 2, 3, 10)]:
        S_ap = 3 * b_mid
        ans = b_mid + d_ap
        assert (b_mid - d_ap + c1) * (b_mid + d_ap + c3) == (b_mid + c2) ** 2
        B.add_math(
            tp, "Hard", bp,
            f"Three increasing numbers form an arithmetic progression with sum {m(S_ap)}. If {m(c1)}, {m(c2)}, and {m(c3)} are added to the first, second, and third terms respectively, the resulting three numbers form a geometric progression. What is the **largest** of the original three AP terms?",
            f"ثلاثة أعداد متزايدة تشكّل متتالية حسابية مجموعها {m(S_ap)}. إذا أُضيف {m(c1)} و{m(c2)} و{m(c3)} إلى الحد الأول والثاني والثالث على الترتيب، شكّلت الأعداد الناتجة متتالية هندسية. ما **أكبر** حد في المتتالية الحسابية الأصلية؟",
            ans, [b_mid, ans + c3, b_mid + 2 * d_ap, ans - 2],
            f"Parameterize the AP symmetrically around its middle term as {m(f'{b_mid} - d,\\; {b_mid},\\; {b_mid} + d')} with {m('d > 0')}!",
            f"اكتب المتتالية الحسابية بتناظر حول حدها الأوسط {m(f'{b_mid} - d,\\; {b_mid},\\; {b_mid} + d')} مع {m('d > 0')}!",
            f"Set the AP to {m(f'({b_mid} - d, {b_mid}, {b_mid} + d)')} and apply {m('G_2^2 = G_1 G_3')}!",
            [
                f"Since the three AP terms sum to {m(S_ap)}, the middle term is {m(f'{S_ap}/3 = {b_mid}')}; write them as {m(f'{b_mid} - d,\\; {b_mid},\\; {b_mid} + d')} ({m('d > 0')}).",
                f"Adding {m(f'({c1}, {c2}, {c3})')} gives the GP {m(f'({b_mid + c1} - d,\\; {b_mid + c2},\\; {b_mid + c3} + d)')}, so {m(f'({b_mid + c1} - d)({b_mid + c3} + d) = {b_mid + c2}^2 = {(b_mid + c2)**2}')}.",
                f"Solving the quadratic for {m('d > 0')} gives {m(f'd = {d_ap}')}, so the largest original AP term is {m(f'{b_mid} + {d_ap} = {ans}')}.",
            ],
            f"Check: AP {m(f'({b_mid - d_ap}, {b_mid}, {ans})')} plus {m(f'({c1}, {c2}, {c3})')} becomes GP {m(f'({b_mid - d_ap + c1}, {b_mid + c2}, {ans + c3})')}!",
            f"نمثّل المتتالية الحسابية حول حدها الأوسط {m(b_mid)} ثم نطبق شرط التناسب الهندسي!",
            [
                f"الحد الأوسط هو {m(f'{S_ap} \\div 3 = {b_mid}')}، فنفرض الحدود {m(f'{b_mid} - d,\\; {b_mid},\\; {b_mid} + d')} مع {m('d > 0')}.",
                f"بعد الإضافة نحصل على {m(f'({b_mid + c1} - d)({b_mid + c3} + d) = {(b_mid + c2)**2}')}.",
                f"الموجب الوحيد لـ {m('d')} هو {m(d_ap)}، فيكون أكبر حد أصلي {m(f'{b_mid} + {d_ap} = {ans}')}.",
            ],
            f"تحقق: المتتالية الهندسية الناتجة هي {m(f'{b_mid - d_ap + c1}, {b_mid + c2}, {ans + c3}')}!",
        )

    for a1, d1, b1, d2, cap in [(3, 4, 5, 6, 500), (2, 5, 4, 7, 700)]:
        s1 = set(range(a1, cap + 1, d1))
        s2 = set(range(b1, cap + 1, d2))
        common = sorted(s1 & s2)
        ans = len(common)
        L = math.lcm(d1, d2)
        c0 = common[0]
        B.add_math(
            tp, "Hard", bp,
            f"Consider two arithmetic progressions, {m(f'{a1}, {a1+d1}, {a1+2*d1}, \\dots')} (step {m(d1)}) and {m(f'{b1}, {b1+d2}, {b1+2*d2}, \\dots')} (step {m(d2)}). How many integers less than or equal to {m(cap)} appear in **both** progressions?",
            f"لدينا متتاليتان حسابيتان: الأولى {m(f'{a1}, {a1+d1}, {a1+2*d1}, \\dots')} (أساسها {m(d1)}) والثانية {m(f'{b1}, {b1+d2}, {b1+2*d2}, \\dots')} (أساسها {m(d2)}). كم عدداً صحيحاً أصغر من أو يساوي {m(cap)} يظهر في **كلتا** المتتاليتين معاً؟",
            ans, [cap // L, ans - 1, ans + 1, cap // (d1 * d2)],
            f"The intersection of two APs is a new AP with step {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')} starting at their first shared term {m(c0)}!",
            f"تقاطع متتاليتين حسابيتين يشكّل متتالية حسابية جديدة أساسها {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')} وتبدأ عند أول حد مشترك {m(c0)}!",
            f"Find the first shared term {m(c0)} and step by {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')} up to {m(cap)}!",
            [
                f"Inspecting the first few terms reveals the first common term {m(c0)}.",
                f"Common terms repeat every {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')}: {m(f'{c0} + {L}k \\le {cap}')}.",
                f"Solve {m(f'0 \\le k \\le \\lfloor ({cap} - {c0}) / {L} \\rfloor = {(cap - c0)//L}')}, giving {m(f'{(cap - c0)//L} + 1 = {ans}')} common terms.",
            ],
            f"Don't forget {m('+1')} for {m('k = 0')} (the initial shared term {m(c0)})!",
            f"نحدد أول حد مشترك {m(c0)} ثم نقفز بمقدار {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')} حتى سقف {m(cap)}!",
            [
                f"أول عدد مشترك بين المتتاليتين هو {m(c0)}.",
                f"تتكرر الحدود المشتركة بخطوة {m(f'\\operatorname{{lcm}}({d1}, {d2}) = {L}')} وفق {m(f'{c0} + {L}k \\le {cap}')}.",
                f"تتراوح {m('k')} من {m(0)} إلى {m((cap - c0)//L)}، وعددها {m(ans)} حداً مشتركاً.",
            ],
            f"انتبه لإضافة {m(1)} المقابلة لقيمة {m('k = 0')}!",
            diagram_en=svg_number_strip([str(c0), str(c0 + L), "…", f"≤ {cap}"]),
        )


# =============================================================================
# UNIT 2.5 — Similar Triangles, Thales Circles, Trapezoids & Polygons (75 Qs)
# =============================================================================
def _add_unit_2_5(B: BankBuilder) -> None:
    tp = "Geometry"

    # 1. nsmo_g89_parallel_similar_triangles (5E, 6M, 4H) — SVG: svg_parallel_similar_tri
    bp = "nsmo_g89_parallel_similar_triangles"
    for ad, db, bc in [(3, 2, 20), (4, 5, 36), (2, 5, 35), (5, 3, 40), (3, 7, 50)]:
        ans = (ad * bc) // (ad + db)
        B.add_math(
            tp, "Easy", bp,
            f"In {m('\\triangle ABC')}, point {m('D')} lies on {m('AB')} and point {m('E')} lies on {m('AC')} with {m('DE \\parallel BC')}. Given {m(f'AD = {ad}')}, {m(f'DB = {db}')}, and {m(f'BC = {bc}')}, find the length of {m('DE')}.",
            f"في المثلث {m('ABC')}، تقع {m('D')} على {m('AB')} و{m('E')} على {m('AC')} بحيث {m('DE \\parallel BC')}. إذا كان {m(f'AD = {ad}')} و{m(f'DB = {db}')} و{m(f'BC = {bc}')}، فأوجد طول {m('DE')}.",
            ans, [(db * bc) // (ad + db), (ad * bc) // db if (ad * bc) % db == 0 else ans + 4, ans + 3, ans - 2],
            f"Use the full side {m(f'AB = AD + DB = {ad + db}')}: {m('DE / BC = AD / AB')}!",
            f"استخدم الضلع الكامل {m(f'AB = AD + DB = {ad + db}')}: {m('DE / BC = AD / AB')}!",
            f"Since {m('\\triangle ADE \\sim \\triangle ABC')}, scale {m('BC')} by {m(f'\\frac{{AD}}{{AD + DB}} = \\frac{{{ad}}}{{{ad + db}}}')}!",
            [
                f"Compute full side {m(f'AB = {ad} + {db} = {ad + db}')}.",
                f"By AA similarity ({m('DE \\parallel BC')}), {m(f'\\frac{{DE}}{{{bc}}} = \\frac{{{ad}}}{{{ad + db}}}')}.",
                f"Solve: {m(f'DE = {bc} \\times \\frac{{{ad}}}{{{ad + db}}} = {ans}')}.",
            ],
            f"Trap check: never divide by {m(f'DB = {db}')} alone — always divide by {m(f'AB = {ad + db}')}!",
            f"بالتشابه نضرب {m('BC')} في نسبة الضلع الكامل {m(f'\\frac{{{ad}}}{{{ad + db}}}')}!",
            [
                f"طول الضلع الكامل {m(f'AB = {ad} + {db} = {ad + db}')}.",
                f"من تشابه المثلثين {m('\\triangle ADE \\sim \\triangle ABC')}: {m(f'\\frac{{DE}}{{{bc}}} = \\frac{{{ad}}}{{{ad + db}}}')}.",
                f"إذن {m(f'DE = {ans}')}.",
            ],
            f"انتبه: المقام في نسبة التشابه هو {m(ad + db)} وليس {m(db)}!",
            diagram_en=svg_parallel_similar_tri(str(ad), str(db), "DE=?", str(bc)),
        )

    for p, q, area_top in [(1, 2, 9), (3, 2, 27), (2, 1, 20)]:
        area_full = area_top * ((p + q) ** 2) // (p * p)
        ans = area_full - area_top
        B.add_math(
            tp, "Medium", bp,
            f"In {m('\\triangle ABC')}, segment {m('DE \\parallel BC')} connects {m('D')} on {m('AB')} to {m('E')} on {m('AC')} with {m(f'AD : DB = {p} : {q}')}. If {m(f'[\\triangle ADE] = {area_top}')}, what is the area of trapezoid {m('DBCE')}?",
            f"في المثلث {m('ABC')}، توازي القطعة {m('DE')} القاعدة {m('BC')} حيث {m(f'AD : DB = {p} : {q}')}. إذا كانت مساحة {m(f'\\triangle ADE = {area_top}')}، فما مساحة شبه المنحرف {m('DBCE')}؟",
            ans, [area_full, area_top * q // p if (area_top * q) % p == 0 else ans - 5, ans + area_top // 2, (area_top * q * q) // (p * p) if (area_top * q * q) % (p * p) == 0 else ans - 4],
            f"Area scales as the **square** of {m(f'AD / AB = {p} / {p + q}')}; find {m('[\\triangle ABC]')} first, then subtract {m(area_top)}!",
            f"تتناسب المساحات مع **مربع** النسبة {m(f'AD / AB = {p} / {p + q}')}؛ أوجد مساحة {m('\\triangle ABC')} ثم اطرح {m(area_top)}!",
            f"Square the full-side scale factor {m(f'\\left(\\frac{{{p}}}{{{p+q}}}\\right)^2')} and subtract the top triangle!",
            [
                f"Since {m(f'AD : AB = {p} : {p + q}')}, we have {m(f'\\frac{{[\\triangle ADE]}}{{[\\triangle ABC]}} = \\frac{{{p*p}}}{{{(p+q)**2}}}')}.",
                f"Thus {m(f'[\\triangle ABC] = {area_top} \\times \\frac{{{(p+q)**2}}}{{{p*p}}} = {area_full}')}.",
                f"Subtract {m('[\\triangle ADE]')}: {m(f'[DBCE] = {area_full} - {area_top} = {ans}')}.",
            ],
            f"Check: {m(area_full)} is the whole triangle; subtracting {m(area_top)} leaves {m(ans)} for trapezoid {m('DBCE')}!",
            f"نربّع نسبة التشابه {m(f'\\frac{{{p}}}{{{p+q}}}')} لحساب المساحة الكلية ثم نطرح {m(area_top)}!",
            [
                f"نسبة التشابه الخطية هي {m(f'{p} : {p + q}')}، فنسبة المساحتين {m(f'{p*p} : {(p+q)**2}')}.",
                f"المساحة الكلية للمثلث {m(f'ABC = {area_full}')}.",
                f"مساحة شبه المنحرف {m(f'DBCE = {area_full} - {area_top} = {ans}')}.",
            ],
            f"انتبه لطرح مساحة المثلث العلوي {m(area_top)} من {m(area_full)}!",
            diagram_en=svg_parallel_similar_tri(f"{p}k", f"{q}k", "DE", "BC"),
        )

    for a_pole, b_pole in [(6, 12), (10, 15), (12, 24)]:
        ans = (a_pole * b_pole) // (a_pole + b_pole)
        B.add_math(
            tp, "Medium", bp,
            f"Two vertical poles of heights {m(f'{a_pole}\\text{{ m}}')} and {m(f'{b_pole}\\text{{ m}}')} stand perpendicular to flat ground. Straight taut wires join the top of each pole to the foot of the other pole. At what height above the ground (in {m('\\text{m}')}) do the two wires cross?",
            f"عمودان رأسيان طولا هما {m(f'{a_pole}\\text{{ m}}')} و{m(f'{b_pole}\\text{{ m}}')} قائمان على أرض أفقية. وُصل سلك مشدود من قمة كل عمود إلى قاعدة العمود الآخر. على أي ارتفاع عن سطح الأرض (بالمتر) يتقاطع السلكان؟",
            ans, [(a_pole + b_pole) // 2, ans + 2, a_pole - 1, b_pole // 2],
            f"Remarkably, the horizontal distance between the poles cancels out: {m('\\frac{1}{h} = \\frac{1}{a} + \\frac{1}{b}')}!",
            f"المفاجأة الجميلة أن المسافة الأفقية بين العمودين تختصر تماماً، ويتحقق القانون {m('\\frac{1}{h} = \\frac{1}{a} + \\frac{1}{b}')}!",
            f"Drop altitude {m('h')} from the crossing point and add the two similar-triangle base ratios {m('\\frac{h}{a} + \\frac{h}{b} = 1')}!",
            [
                f"Let the horizontal ground span be {m('D = d_1 + d_2')} split directly under the crossing point of height {m('h')}.",
                f"By similar right triangles, {m(f'\\frac{{h}}{{{a_pole}}} = \\frac{{d_2}}{{D}}')} and {m(f'\\frac{{h}}{{{b_pole}}} = \\frac{{d_1}}{{D}}')}.",
                f"Adding gives {m(f'h\\left(\\frac{{1}}{{{a_pole}}} + \\frac{{1}}{{{b_pole}}}\\right) = 1 \\implies h = \\frac{{{a_pole} \\times {b_pole}}}{{{a_pole} + {b_pole}}} = {ans}\\text{{ m}}')}.",
            ],
            f"Notice {m(f'h = \\frac{{ab}}{{a + b}}')} is independent of how far apart the poles stand!",
            f"نسقط ارتفاع نقطة التقاطع {m('h')} ونجمع نسبتي التشابه {m('\\frac{h}{a} + \\frac{h}{b} = 1')}!",
            [
                f"من تشابه المثلثات القائمة على جانبي نقطة التقاطع: {m(f'\\frac{{h}}{{{a_pole}}} + \\frac{{h}}{{{b_pole}}} = \\frac{{d_2 + d_1}}{{D}} = 1')}.",
                f"إذن {m(f'h = \\frac{{{a_pole} \\times {b_pole}}}{{{a_pole} + {b_pole}}}')}.",
                f"بحساب الكسر نجد {m(f'h = {ans}\\text{{ m}}')}.",
            ],
            f"تحقق رائع: الارتفاع مستقل تماماً عن المسافة الأفقية بين العمودين!",
        )

    for b_base, h_alt in [(15, 10), (20, 30)]:
        ans = (b_base * h_alt) // (b_base + h_alt)
        B.add_math(
            tp, "Hard", bp,
            f"Triangle {m('ABC')} has base {m(f'BC = {b_base}')} and corresponding altitude {m(f'h = {h_alt}')}. A square is inscribed in {m('\\triangle ABC')} with two vertices on side {m('BC')}, one vertex on {m('AB')}, and one vertex on {m('AC')}. Find the side length of the square.",
            f"مثلث {m('ABC')} طول قاعدته {m(f'BC = {b_base}')} والارتفاع النازل عليها {m(f'h = {h_alt}')}. رُسم مربع داخل المثلث بحيث يقع رأسان منه على {m('BC')} ورأس على {m('AB')} ورأس على {m('AC')}. أوجد طول ضلع المربع.",
            ans, [(b_base + h_alt) // 4, ans + 2, min(b_base, h_alt) // 2, ans - 1],
            f"If the square has side {m('s')}, the top triangle above the square has base {m('s')} and altitude {m(f'{h_alt} - s')}!",
            f"إذا كان ضلع المربع {m('s')}، فإن المثلث العلوي فوق المربع قاعدته {m('s')} وارتفاعه {m(f'{h_alt} - s')}!",
            f"Equate base-to-height ratios of the similar top triangle and {m('\\triangle ABC')}: {m(f'\\frac{{s}}{{{b_base}}} = \\frac{{{h_alt} - s}}{{{h_alt}}}')}!",
            [
                f"The top edge of the {m('s \\times s')} square is parallel to {m('BC')}, creating a similar top triangle of base {m('s')} and altitude {m(f'{h_alt} - s')}.",
                f"Similarity gives {m(f'\\frac{{s}}{{{b_base}}} = \\frac{{{h_alt} - s}}{{{h_alt}}} \\implies {h_alt}s = {b_base}({h_alt} - s)')}.",
                f"Solve {m(f'({b_base} + {h_alt})s = {b_base * h_alt} \\implies s = \\frac{{{b_base * h_alt}}}{{{b_base + h_alt}}} = {ans}')}.",
            ],
            f"Notice the exact same harmonic product {m('\\frac{bh}{b + h}')} governs inscribed squares in any triangle!",
            f"من توازي الضلع العلوي للمربع مع {m('BC')} نطبق تناسب القاعدة والارتفاع {m(f'\\frac{{s}}{{{b_base}}} = \\frac{{{h_alt} - s}}{{{h_alt}}}')}!",
            [
                f"المثلث العلوي يشابه {m('\\triangle ABC')}، وقاعدته {m('s')} وارتفاعه {m(f'{h_alt} - s')}.",
                f"من التناسب: {m(f'{h_alt}s = {b_base}({h_alt} - s) \\implies ({b_base} + {h_alt})s = {b_base * h_alt}')}.",
                f"إذن طول ضلع المربع {m(f's = {ans}')}.",
            ],
            f"تحقق: مساحة المربع زائد المثلثات الثلاثة المحيطة به تساوي مساحة {m('\\triangle ABC')} تماماً!",
            diagram_en=svg_parallel_similar_tri("", "", "s", str(b_base)),
        )

    for a_top_sq, b_bot_sq in [(9, 25), (16, 36)]:
        ra, rb = math.isqrt(a_top_sq), math.isqrt(b_bot_sq)
        ans = (ra + rb) ** 2
        B.add_math(
            tp, "Hard", bp,
            f"In trapezoid {m('ABCD')} with {m('AB \\parallel CD')}, diagonals {m('AC')} and {m('BD')} intersect at {m('P')}. If {m(f'[\\triangle APB] = {a_top_sq}')} and {m(f'[\\triangle CPD] = {b_bot_sq}')}, what is the total area of trapezoid {m('ABCD')}?",
            f"في شبه المنحرف {m('ABCD')} حيث {m('AB \\parallel CD')}، يتقاطع القطران {m('AC')} و{m('BD')} في {m('P')}. إذا كانت مساحة {m(f'\\triangle APB = {a_top_sq}')} ومساحة {m(f'\\triangle CPD = {b_bot_sq}')}، فما المساحة الكلية لشبه المنحرف {m('ABCD')}؟",
            ans, [2 * (a_top_sq + b_bot_sq), a_top_sq + b_bot_sq + ra * rb, ans - ra * rb, (rb - ra) ** 2 + a_top_sq + b_bot_sq],
            f"Since {m('\\triangle APB \\sim \\triangle CPD')}, find {m('AP : PC = \\sqrt{[APB]} : \\sqrt{[CPD]}')}, then find the two wing areas {m('[\\triangle APD]')} and {m('[\\triangle BPC]')}!",
            f"من تشابه {m('\\triangle APB \\sim \\triangle CPD')} أوجد نسبة {m('AP : PC')} بجذر المساحتين ثم احسب مساحتي المثلثين الجانبيين!",
            f"Use trapezoid diagonal-area identity {m('\\big(\\sqrt{[APB]} + \\sqrt{[CPD]}\\big)^2')}!",
            [
                f"Hourglass similarity {m('\\triangle APB \\sim \\triangle CPD')} gives {m(f'AP : PC = \\sqrt{{{a_top_sq}}} : \\sqrt{{{b_bot_sq}}} = {ra} : {rb}')}.",
                f"Equal-height ratio along {m('AC')} gives {m(f'[\\triangle BPC] = \\frac{{PC}}{{AP}}[\\triangle APB] = \\frac{{{rb}}}{{{ra}}} \\times {a_top_sq} = {ra * rb}')}, and symmetrically {m(f'[\\triangle APD] = {ra * rb}')}.",
                f"Add all four triangles: {m(f'{a_top_sq} + {ra * rb} + {ra * rb} + {b_bot_sq} = ({ra} + {rb})^2 = {ans}')}.",
            ],
            f"Beautiful Olympiad gem: each wing has geometric-mean area {m(f'\\sqrt{{{a_top_sq} \\cdot {b_bot_sq}}} = {ra * rb}')}!",
            f"نحسب نسبة القطرين {m(f'{ra} : {rb}')} فنجد مساحة كل مثلث جانبي تساوي الوسط الهندسي {m(ra * rb)}!",
            [
                f"من التشابه {m('\\triangle APB \\sim \\triangle CPD')} تكون نسبة التشابه {m(f'\\sqrt{{{a_top_sq}}} : \\sqrt{{{b_bot_sq}}} = {ra} : {rb}')}.",
                f"مساحة كل من المثلثين الجانبيين {m('\\triangle APD')} و{m('\\triangle BPC')} تساوي {m(f'{ra} \\times {rb} = {ra * rb}')}.",
                f"مجموع المثلثات الأربعة هو {m(f'({ra} + {rb})^2 = {ans}')}.",
            ],
            f"تحقق: {m(f'{a_top_sq} + {b_bot_sq} + 2({ra*rb}) = {ans}')}!",
        )

    # 2. nsmo_g89_thales_inscribed_angles (5E, 6M, 4H) — SVG: svg_thales_circle
    bp = "nsmo_g89_thales_inscribed_angles"
    for ang_a in (28, 37, 53):
        ans = 90 - ang_a
        B.add_math(
            tp, "Easy", bp,
            f"Segment {m('AB')} is a diameter of circle {m('O')}, and {m('C')} is a point on the circle. If {m(f'\\angle CAB = {ang_a}^\\circ')}, what is the measure of {m('\\angle CBA')}, in degrees?",
            f"القطعة {m('AB')} قطر في الدائرة {m('O')}، والنقطة {m('C')} تقع على محيطها. إذا كان {m(f'\\angle CAB = {ang_a}^\\circ')}، فما قياس {m('\\angle CBA')} بالدرجات؟",
            ans, [180 - ang_a, 90 - ang_a // 2, 2 * ang_a, ans + 10],
            f"By Thales' theorem, {m('\\angle ACB = 90^\\circ')}.",
            f"بحسب مبرهنة طاليس فإن {m('\\angle ACB = 90^\\circ')}.",
            f"Apply Thales' theorem ({m('\\angle ACB = 90^\\circ')}) so the acute angles are complementary!",
            [
                f"Since {m('AB')} is a diameter, {m('\\angle ACB = 90^\\circ')}.",
                f"Angles in {m('\\triangle ABC')} sum to {m('180^\\circ')}, so {m('\\angle CAB + \\angle CBA = 90^\\circ')}.",
                f"Compute {m(f'90^\\circ - {ang_a}^\\circ = {ans}^\\circ')}.",
            ],
            f"Check: {m(f'{ang_a}^\\circ + 90^\\circ + {ans}^\\circ = 180^\\circ')}.",
            f"نطبق مبرهنة طاليس ({m('\\angle ACB = 90^\\circ')}) فتكون الزاويتان الحادتان متتامتين!",
            [
                f"الزاوية المحيطية المقابلة للقطر قائمة: {m('\\angle ACB = 90^\\circ')}.",
                f"إذن {m(f'\\angle CBA = 90^\\circ - {ang_a}^\\circ = {ans}^\\circ')}.",
                f"قياس الزاوية المطلوبة هو {m(ans)} درجة.",
            ],
            f"تحقق: مجموع زوايا المثلث {m(f'{ang_a} + 90 + {ans} = 180')}.",
            diagram_en=svg_thales_circle(f"{ang_a}°", "x°"),
        )

    for c_ang in (116, 148):
        ans = c_ang // 2
        B.add_math(
            tp, "Easy", bp,
            f"Points {m('A, B, C')} lie on a circle with center {m('O')} such that {m('C')} is on the major arc {m('AB')}. If the central angle {m(f'\\angle AOB = {c_ang}^\\circ')}, find {m('\\angle ACB')} in degrees.",
            f"تقع النقاط {m('A, B, C')} على دائرة مركزها {m('O')} بحيث تقع {m('C')} على القوس الأكبر {m('AB')}. إذا كان قياس الزاوية المركزية {m(f'\\angle AOB = {c_ang}^\\circ')}، فأوجد {m('\\angle ACB')} بالدرجات.",
            ans, [c_ang, 180 - ans, 90 - ans // 2, 180 - c_ang],
            f"An inscribed angle is half the central angle subtending the same minor arc {m('AB')}.",
            f"قياس الزاوية المحيطية يساوي نصف قياس الزاوية المركزية المشتركة معها في القوس.",
            f"Halve the central angle {m('\\angle AOB')}!",
            [
                f"Inscribed angle {m('\\angle ACB')} subtends minor arc {m('AB')}, the same arc as central angle {m('\\angle AOB')}.",
                f"By the Inscribed Angle Theorem, {m('\\angle ACB = \\frac{1}{2} \\angle AOB')}.",
                f"Compute {m(f'{c_ang}^\\circ / 2 = {ans}^\\circ')}.",
            ],
            f"Had {m('C')} been on the **minor** arc {m('AB')}, the opposite angle would be {m(f'180^\\circ - {ans}^\\circ = {180 - ans}^\\circ')}!",
            f"نقسم قياس الزاوية المركزية على {m(2)} مباشرة!",
            [
                f"الزاوية المحيطية {m('\\angle ACB')} تشترك مع المركزية {m('\\angle AOB')} في القوس الأصغر {m('AB')}.",
                f"إذن {m(f'\\angle ACB = \\frac{{1}}{{2}} \\times {c_ang}^\\circ = {ans}^\\circ')}.",
                f"القيمة هي {m(ans)} درجة.",
            ],
            f"انتبه: لو وقعت {m('C')} على القوس الأصغر لكانت الزاوية مكملة لـ {m(ans)} أي {m(180 - ans)}!",
        )

    for ac, bc in [(6, 8), (10, 24), (16, 30)]:
        diam = math.isqrt(ac * ac + bc * bc)
        ans = diam // 2
        B.add_math(
            tp, "Medium", bp,
            f"Segment {m('AB')} is a diameter of circle {m('O')}, and point {m('C')} on the circle satisfies {m(f'AC = {ac}')} and {m(f'BC = {bc}')}. Find the **radius** of circle {m('O')}.",
            f"القطعة {m('AB')} قطر في الدائرة {m('O')}، والنقطة {m('C')} على محيطها تحقق {m(f'AC = {ac}')} و{m(f'BC = {bc}')}. أوجد **نصف قطر** الدائرة {m('O')}.",
            ans, [diam, (ac + bc) // 2, ans + 2, ans - 1],
            f"Find hypotenuse {m('AB')} via Pythagoras ({m('\\angle ACB = 90^\\circ')}), then divide by {m(2)} for the radius!",
            f"أوجد القطر {m('AB')} بفيثاغورس لأن {m('\\angle ACB = 90^\\circ')}، ثم اقسمه على {m(2)} لإيجاد نصف القطر!",
            f"Compute {m('AB = \\sqrt{AC^2 + BC^2}')} by Thales' theorem and halve it!",
            [
                f"By Thales' theorem, {m('\\angle ACB = 90^\\circ')}.",
                f"Thus diameter {m(f'AB = \\sqrt{{{ac}^2 + {bc}^2}} = \\sqrt{{{ac*ac + bc*bc}}} = {diam}')}.",
                f"Radius {m(f'R = AB / 2 = {diam} / 2 = {ans}')}.",
            ],
            f"Diameter {m(diam)} is the #1 distractor — always halve to report the radius {m(ans)}!",
            f"نحسب طول القطر {m('AB')} بمبرهنة فيثاغورس ثم نقسمه على {m(2)}!",
            [
                f"بما أن {m('AB')} قطر فإن {m('\\angle ACB = 90^\\circ')}.",
                f"طول القطر {m(f'AB = \\sqrt{{{ac}^2 + {bc}^2}} = {diam}')}.",
                f"نصف القطر يساوي {m(f'{diam} \\div 2 = {ans}')}.",
            ],
            f"انتبه: الإجابة {m(diam)} تمثل القطر الكامل بينما المطلوب نصف القطر {m(ans)}!",
            diagram_en=svg_thales_circle(f"AC={ac}", f"BC={bc}"),
        )

    for p_seg, q_seg in [(4, 9), (4, 16), (9, 16)]:
        ans = math.isqrt(p_seg * q_seg)
        B.add_math(
            tp, "Medium", bp,
            f"Point {m('C')} lies on a semicircle with diameter {m('AB')}, and the perpendicular from {m('C')} to {m('AB')} meets {m('AB')} at {m('H')}. If {m(f'AH = {p_seg}')} and {m(f'HB = {q_seg}')}, find the length of {m('CH')}.",
            f"تقع النقطة {m('C')} على نصف دائرة قطرها {m('AB')}، ويسقط العمود من {m('C')} على {m('AB')} في النقطة {m('H')}. إذا كان {m(f'AH = {p_seg}')} و{m(f'HB = {q_seg}')}، فأوجد طول {m('CH')}.",
            ans, [(p_seg + q_seg) // 2, p_seg * q_seg // 2, ans + 2, q_seg - p_seg],
            f"In right triangle {m('ACB')}, altitude {m('CH')} satisfies {m('CH^2 = AH \\cdot HB')}!",
            f"في المثلث القائم {m('ACB')}، مربع الارتفاع النازل على الوتر يحقق {m('CH^2 = AH \\cdot HB')}!",
            f"Combine Thales' right angle {m('\\angle ACB = 90^\\circ')} with the geometric-mean altitude theorem {m('CH = \\sqrt{AH \\cdot HB}')}!",
            [
                f"By Thales' theorem, {m('\\triangle ACB')} is right-angled at {m('C')}, making {m('\\triangle AHC \\sim \\triangle CHB')}.",
                f"Hence {m('CH / AH = HB / CH \\implies CH^2 = AH \\cdot HB')}.",
                f"Compute {m(f'CH = \\sqrt{{{p_seg} \\times {q_seg}}} = \\sqrt{{{p_seg * q_seg}}} = {ans}')}.",
            ],
            f"Notice {m(f'CH = {ans} \\le R = {(p_seg + q_seg)/2:g}')}, visualizing the AM–GM inequality right inside a semicircle!",
            f"بما أن {m('\\angle ACB = 90^\\circ')} فإن الارتفاع {m('CH')} هو الوسط الهندسي لجزأي القطر!",
            [
                f"من تشابه {m('\\triangle AHC \\sim \\triangle CHB')} نحصل على {m('CH^2 = AH \\times HB')}.",
                f"نعوّض: {m(f'CH^2 = {p_seg} \\times {q_seg} = {p_seg * q_seg}')}.",
                f"بأخذ الجذر التربيعي الموجب نجد {m(f'CH = {ans}')}.",
            ],
            f"تحقق: طول العمود {m(ans)} أصغر من أو يساوي نصف القطر {m(f'{(p_seg+q_seg)/2:g}')}.",
            diagram_en=svg_thales_circle(f"AH={p_seg}", f"HB={q_seg}"),
        )

    for a_top, b_bot in [(4, 16), (9, 16)]:
        ans = math.isqrt(a_top * b_bot) // 2
        leg = (a_top + b_bot) // 2
        B.add_math(
            tp, "Hard", bp,
            f"An isosceles trapezoid with parallel bases of lengths {m(a_top)} and {m(b_bot)} has an inscribed circle tangent to all four of its sides. What is the **radius** of this circle?",
            f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a_top)} و{m(b_bot)} مرسومة داخله دائرة تمس أضلاعه الأربعة جميعاً. ما **نصف قطر** هذه الدائرة؟",
            ans, [2 * ans, (a_top + b_bot) // 4, ans + 2, (b_bot - a_top) // 2],
            f"By Pitot's tangential-quadrilateral theorem, the sum of legs equals {m(f'{a_top} + {b_bot}')}, so each leg is {m(leg)}; then find height {m('2r')}!",
            f"من مبرهنة بيتو للرباعي المماسي، مجموع الساقين يساوي مجموع القاعدتين {m(a_top + b_bot)} فيكون طول كل ساق {m(leg)}، ومنه نحسب الارتفاع {m('2r')}!",
            f"Find each leg {m(f'c = ({a_top} + {b_bot})/2 = {leg}')} via equal tangents, then apply Pythagoras for {m('h = 2r')}!",
            [
                f"Equal tangent segments give {m(f'2c = {a_top} + {b_bot} \\implies c = {leg}')}.",
                f"Dropping altitudes gives overhang {m(f'({b_bot} - {a_top})/2 = {(b_bot - a_top)//2}')}, so {m(f'(2r)^2 = {leg}^2 - {(b_bot - a_top)//2}^2 = {a_top * b_bot}')}.",
                f"Thus {m(f'2r = {2*ans}')}, giving radius {m(f'r = {ans}')}.",
            ],
            f"Remember the altitude of the trapezoid equals the **diameter** {m(f'2r = {2*ans}')}, so halve it to get {m(f'r = {ans}')}!",
            f"مجموع الساقين يساوي مجموع القاعدتين، فنحسب الساق {m(leg)} ثم الارتفاع {m('2r = \\sqrt{ab}')}!",
            [
                f"من تساوي القطع المماسية نجد طول كل ساق {m(f'c = ({a_top} + {b_bot})/2 = {leg}')}.",
                f"بتطبيق فيثاغورس نجد مربع الارتفاع {m(f'(2r)^2 = {leg}^2 - {(b_bot - a_top)//2}^2 = {a_top * b_bot}')} ومنه {m(f'2r = {2*ans}')}.",
                f"إذن نصف القطر {m(f'r = {ans}')}.",
            ],
            f"انتبه: الارتفاع {m(2*ans)} يساوي قطر الدائرة لا نصف قطرها!",
            diagram_en=svg_trapezoid_semicircle(str(a_top), str(b_bot)),
        )

    for R_rad, cd_len in [(10, 12), (13, 10)]:
        h_dist = math.isqrt(R_rad * R_rad - (cd_len // 2) ** 2)
        ans = (2 * R_rad + cd_len) * h_dist // 2
        B.add_math(
            tp, "Hard", bp,
            f"In a circle of radius {m(R_rad)}, {m('AB')} is a diameter and chord {m('CD')} of length {m(cd_len)} is parallel to {m('AB')}. What is the area of trapezoid {m('ABDC')}?",
            f"في دائرة نصف قطرها {m(R_rad)}، القطعة {m('AB')} قطر والوتر {m('CD')} الذي طوله {m(cd_len)} يوازي {m('AB')}. ما مساحة شبه المنحرف {m('ABDC')}؟",
            ans, [(R_rad + cd_len) * h_dist // 2, (2 * R_rad + cd_len) * R_rad // 2, ans - h_dist * 2, ans + 20],
            f"Drop the perpendicular from center {m('O')} to chord {m('CD')}: it bisects {m('CD')} into {m(cd_len // 2)} and {m(cd_len // 2)}, giving the trapezoid's height!",
            f"أسقط عموداً من المركز {m('O')} على الوتر {m('CD')} فينصّفه إلى {m(cd_len // 2)} و{m(cd_len // 2)} ويعطيك ارتفاع شبه المنحرف!",
            f"Find the perpendicular distance from center {m('O')} to chord {m('CD')} via right triangle {m(f'({cd_len//2}, h, {R_rad})')}!",
            [
                f"The perpendicular from {m('O')} to {m('CD')} bisects {m('CD')}, forming a right triangle with hypotenuse {m(f'OC = {R_rad}')} and leg {m(cd_len // 2)}.",
                f"Trapezoid height {m(f'h = \\sqrt{{{R_rad}^2 - {cd_len//2}^2}} = {h_dist}')}.",
                f"With bases {m(f'AB = {2*R_rad}')} and {m(f'CD = {cd_len}')}, area {m(f'= \\frac{{{2*R_rad} + {cd_len}}}{{2}} \\times {h_dist} = {ans}')}.",
            ],
            f"Check: base {m('AB')} is the diameter {m(2*R_rad)}, not the radius {m(R_rad)}!",
            f"نحسب بعد الوتر {m('CD')} عن المركز بفيثاغورس ليكون هو ارتفاع شبه المنحرف!",
            [
                f"العمود من المركز ينصّف الوتر {m('CD')} إلى {m(cd_len // 2)}، فنحسب الارتفاع {m(f'h = \\sqrt{{{R_rad}^2 - {cd_len//2}^2}} = {h_dist}')}.",
                f"طولا القاعدتين هما القطر {m(2 * R_rad)} والوتر {m(cd_len)}.",
                f"المساحة {m(f'= \\frac{{{2*R_rad} + {cd_len}}}{{2}} \\times {h_dist} = {ans}')}.",
            ],
            f"تحقق: لا تنسَ استخدام القطر الكامل {m(2*R_rad)} كقاعدة كبرى!",
            diagram_en=svg_isosceles_trapezoid(str(cd_len), str(2 * R_rad), "", f"h={h_dist}"),
        )

    # 3. nsmo_g89_isosceles_trapezoid_pythag (5E, 6M, 4H) — SVG: svg_isosceles_trapezoid
    bp = "nsmo_g89_isosceles_trapezoid_pythag"
    for a_b, b_b, leg, ask_mode in [
        (8, 20, 10, "area"),
        (12, 22, 13, "area"),
        (6, 22, 10, "area"),
        (14, 30, 17, "h"),
        (10, 34, 13, "h"),
    ]:
        ov = (b_b - a_b) // 2
        h_v = math.isqrt(leg * leg - ov * ov)
        ans = ((a_b + b_b) * h_v) // 2 if ask_mode == "area" else h_v
        q_en = (
            f"An isosceles trapezoid has parallel bases {m(a_b)} and {m(b_b)}, and each non-parallel leg has length {m(leg)}. Find its {'area' if ask_mode == 'area' else 'altitude (height)'}."
        )
        q_ar = (
            f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a_b)} و{m(b_b)} وطول كل ساق من ساقيه {m(leg)}. أوجد {'مساحته' if ask_mode == 'area' else 'ارتفاعه'}."
        )
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans,
            [((a_b + b_b) * leg) // 2 if ask_mode == "area" else leg, ans + 12, max(1, ans - 8), ov * h_v if ask_mode == "area" else ov],
            f"Each right-triangle base at the ends is {m(f'({b_b} - {a_b})/2 = {ov}')}.",
            f"قاعدة كل مثلث قائم عند الطرفين تساوي {m(f'({b_b} - {a_b})/2 = {ov}')}.",
            f"Split the base difference equally ({m(ov)} on each side) and apply Pythagoras!",
            [
                f"Overhang on each side is {m(f'\\frac{{{b_b} - {a_b}}}{{2}} = {ov}')}.",
                f"Altitude {m(f'h = \\sqrt{{{leg}^2 - {ov}^2}} = {h_v}')}.",
                f"{'Area = ' + m(f'\\frac{{{a_b} + {b_b}}}{{2}} \\times {h_v} = {ans}') if ask_mode == 'area' else 'Thus the altitude is ' + m(str(ans))}.",
            ],
            f"Pythagorean triple {m(f'({ov}, {h_v}, {leg})')} makes calculation instant!",
            f"نقسم فرق القاعدتين على {m(2)} ثم نحسب الارتفاع بمبرهنة فيثاغورس!",
            [
                f"طول الجزء الجانبي {m(f'\\frac{{{b_b} - {a_b}}}{{2}} = {ov}')}.",
                f"الارتفاع {m(f'h = \\sqrt{{{leg}^2 - {ov}^2}} = {h_v}')}.",
                f"{'المساحة تساوي ' + m(str(ans)) if ask_mode == 'area' else 'إذن الارتفاع يساوي ' + m(str(ans))}.",
            ],
            f"تحقق من ثلاثية فيثاغورس {m(f'({ov}, {h_v}, {leg})')}!",
            diagram_en=svg_isosceles_trapezoid(str(a_b), str(b_b), str(leg), "h"),
        )

    for a_b, b_b, leg in [(9, 21, 10), (11, 21, 13), (26, 44, 15)]:
        ov = (b_b - a_b) // 2
        h_v = math.isqrt(leg * leg - ov * ov)
        mid = (a_b + b_b) // 2
        ans = math.isqrt(h_v * h_v + mid * mid)
        assert ans * ans == leg * leg + a_b * b_b
        B.add_math(
            tp, "Medium", bp,
            f"An isosceles trapezoid has parallel bases of lengths {m(a_b)} and {m(b_b)}, and legs of length {m(leg)} each. Find the length of a **diagonal** of the trapezoid.",
            f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a_b)} و{m(b_b)} وطول كل من ساقيه {m(leg)}. أوجد طول **قطر** شبه المنحرف.",
            ans, [h_v + ov, b_b - ov, ans + 3, ans - 2],
            f"First find height {m(f'h = {h_v}')}; the horizontal leg for the diagonal is {m(f'{b_b} - {ov} = {mid}')}!",
            f"احسب أولاً الارتفاع {m(f'h = {h_v}')}؛ ثم لاحظ أن المسقط الأفقي للقطر يساوي {m(f'{b_b} - {ov} = {mid}')}!",
            f"Find altitude {m(f'h = {h_v}')}, then apply Pythagoras to the diagonal right triangle of legs {m(h_v)} and {m(f'({a_b}+{b_b})/2 = {mid}')}!",
            [
                f"Side overhang is {m(f'({b_b} - {a_b})/2 = {ov}')}, giving altitude {m(f'h = \\sqrt{{{leg}^2 - {ov}^2}} = {h_v}')}.",
                f"From the foot of that altitude to the far bottom corner has length {m(f'{b_b} - {ov} = {mid}')}.",
                f"Diagonal {m(f'd = \\sqrt{{{h_v}^2 + {mid}^2}} = \\sqrt{{{h_v*h_v + mid*mid}}} = {ans}')}.",
            ],
            f"Ptolemy shortcut check (every isosceles trapezoid is cyclic!): {m(f'd^2 = c^2 + ab = {leg}^2 + {a_b}\\cdot{b_b} = {ans*ans}')}!",
            f"نحسب الارتفاع {m(h_v)} أولاً ثم نطبّق فيثاغورس على مثلث القطر ذي القاعدة {m(mid)}!",
            [
                f"البروز الجانبي {m(ov)} ومنه الارتفاع {m(f'h = {h_v}')}.",
                f"القاعدة الأفقية لمثلث القطر تساوي {m(f'{b_b} - {ov} = {mid}')}.",
                f"طول القطر {m(f'd = \\sqrt{{{h_v}^2 + {mid}^2}} = {ans}')}.",
            ],
            f"تحقق رائع بمبرهنة بطليموس: {m(f'd^2 = c^2 + ab = {leg*leg + a_b*b_b} = {ans}^2')}!",
            diagram_en=svg_isosceles_trapezoid(str(a_b), str(b_b), str(leg), f"h={h_v}"),
        )

    for a_b, b_b, h_v in [(7, 13, 8), (10, 22, 5), (9, 24, 8)]:
        slant = math.isqrt(h_v * h_v + (b_b - a_b) ** 2)
        ans = a_b + b_b + h_v + slant
        B.add_math(
            tp, "Medium", bp,
            f"In a **right trapezoid** {m('ABCD')}, parallel bases {m('AB')} and {m('CD')} have lengths {m(a_b)} and {m(b_b)}, and leg {m('AD')} of length {m(h_v)} is perpendicular to both bases. What is the **perimeter** of {m('ABCD')}?",
            f"في **شبه منحرف قائم** {m('ABCD')}، طولا القاعدتين المتوازيتين {m('AB')} و{m('CD')} هما {m(a_b)} و{m(b_b)}، والساق {m('AD')} العمودية على القاعدتين طولها {m(h_v)}. ما **محيط** {m('ABCD')}؟",
            ans, [a_b + b_b + 2 * h_v, ans - h_v, ans + (b_b - a_b) // 2, a_b + b_b + 2 * slant],
            f"In a **right** trapezoid, all of {m(f'{b_b} - {a_b} = {b_b - a_b}')} sits on **one** side (do NOT divide by {m(2)}!) to form a {m(f'({h_v}, {b_b - a_b}, BC)')} right triangle!",
            f"في شبه المنحرف **القائم** يتركز الفرق {m(f'{b_b} - {a_b} = {b_b - a_b}')} كاملاً في جهة واحدة (لا تقسم على {m(2)}!)!",
            f"Drop one perpendicular from {m('B')} to {m('CD')} to find the slanted leg {m('BC')}!",
            [
                f"Dropping the altitude from {m('B')} splits {m('CD')} into {m(a_b)} and {m(f'{b_b} - {a_b} = {b_b - a_b}')}.",
                f"Slanted leg {m(f'BC = \\sqrt{{{h_v}^2 + {b_b - a_b}^2}} = {slant}')}.",
                f"Perimeter {m(f'= {a_b} + {b_b} + {h_v} + {slant} = {ans}')}.",
            ],
            f"Contrast carefully: isosceles trapezoids split {m('b - a')} in half, whereas right trapezoids keep {m('b - a')} whole!",
            f"نسقط عموداً من {m('B')} على {m('CD')} لحساب الساق المائلة {m('BC')} ثم نجمع الأضلاع الأربعة!",
            [
                f"القاعدة الأفقية للمثلث القائم تساوي الفرق الكامل {m(f'{b_b} - {a_b} = {b_b - a_b}')}.",
                f"طول الساق المائلة {m(f'BC = \\sqrt{{{h_v}^2 + {b_b - a_b}^2}} = {slant}')}.",
                f"المحيط {m(f'= {a_b} + {b_b} + {h_v} + {slant} = {ans}')}.",
            ],
            f"انتبه للفرق الجوهري بين شبه المنحرف القائم والمتطابق الساقين عند حساب القاعدة الجانبية!",
        )

    for a_b, b_b in [(10, 18), (12, 20)]:
        h_v = (a_b + b_b) // 2
        ans = h_v * h_v
        B.add_math(
            tp, "Hard", bp,
            f"An isosceles trapezoid has parallel bases of lengths {m(a_b)} and {m(b_b)}, and its two diagonals are **perpendicular** to each other. Find the area of the trapezoid.",
            f"شبه منحرف متطابق الساقين طولا قاعدتيه المتوازيتين {m(a_b)} و{m(b_b)}، وقطراه **متعامدان**. أوجد مساحته.",
            ans, [a_b * b_b, ((b_b - a_b) // 2) * (a_b + b_b), ans // 2, ans + a_b],
            f"By symmetry and {m('AC \\perp BD')}, the top and bottom triangles are **45-45-90 right isosceles triangles** with altitudes {m(a_b // 2)} and {m(b_b // 2)}!",
            f"من التناظر وتعامد القطرين، يكون المثلثان العلوي والسفلي **قائمين متطابقي الساقين** بارتفاعين {m(a_b // 2)} و{m(b_b // 2)}!",
            f"Sum the altitudes {m(f'{a_b}/2 + {b_b}/2')} of the two {m('45^\\circ\\text{-}45^\\circ\\text{-}90^\\circ')} triangles to find {m(f'h = {h_v}')}!",
            [
                f"In an isosceles trapezoid with {m('AC \\perp BD')}, {m('\\triangle APB')} and {m('\\triangle CPD')} are right isosceles triangles on bases {m(a_b)} and {m(b_b)}.",
                f"Their altitudes from {m('P')} are {m(f'{a_b}/2 = {a_b//2}')} and {m(f'{b_b}/2 = {b_b//2}')}, so total height is {m(f'h = {a_b//2} + {b_b//2} = {h_v}')}.",
                f"Area {m(f'= \\frac{{{a_b} + {b_b}}}{{2}} \\times {h_v} = {h_v}^2 = {ans}')}.",
            ],
            f"Alternative shift proof: translating {m('BD')} to pass through {m('C')} forms a right isosceles triangle of base {m(f'{a_b} + {b_b} = {2*h_v}')} and height {m(h_v)}!",
            f"ارتفاع شبه المنحرف المتعامد القطرين والمتطابق الساقين يساوي دائماً متوسط قاعدتيه {m(h_v)}!",
            [
                f"المثلثان القائمان المتطابقا الساقين عند القاعدتين ارتفاعاهما {m(a_b // 2)} و{m(b_b // 2)}.",
                f"الارتفاع الكلي لشبه المنحرف هو {m(f'h = {a_b//2} + {b_b//2} = {h_v}')}.",
                f"المساحة تساوي {m(f'\\frac{{{a_b} + {b_b}}}{{2}} \\times {h_v} = {ans}')}.",
            ],
            f"تحقق: إزاحة أحد القطرين تكوّن مثلثاً قائماً متطابق الساقين مساحته {m(ans)}!",
            diagram_en=svg_isosceles_trapezoid(str(a_b), str(b_b), "", f"h={h_v}"),
        )

    for d_len in (14, 18):
        ans = (d_len * d_len) // 2
        B.add_math(
            tp, "Hard", bp,
            f"In an isosceles trapezoid, each diagonal has length {m(d_len)} and the two diagonals intersect at right angles ({m('90^\\circ')}). What is the area of the trapezoid?",
            f"في شبه منحرف متطابق الساقين، طول كل قطر {m(d_len)} والقطران متعامدان ({m('90^\\circ')}). ما مساحة شبه المنحرف؟",
            ans, [d_len * d_len, ans // 2, ans + d_len, d_len * (d_len - 2) // 2],
            f"Any quadrilateral with perpendicular diagonals {m('d_1 \\perp d_2')} has area {m('\\frac{1}{2} d_1 d_2')}!",
            f"مساحة أي مضلع رباعي قطراه متعامدان {m('d_1 \\perp d_2')} تساوي {m('\\frac{1}{2} d_1 d_2')}!",
            f"Use equal diagonals ({m(f'd_1 = d_2 = {d_len}')}) in the perpendicular-diagonal area formula {m('\\frac{1}{2} d_1 d_2')}!",
            [
                f"In any isosceles trapezoid, both diagonals have equal length {m(f'd_1 = d_2 = {d_len}')}.",
                f"Because {m('d_1 \\perp d_2')}, the area equals {m('\\frac{1}{2} d_1 d_2')}.",
                f"Compute {m(f'\\frac{{1}}{{2}} \\times {d_len} \\times {d_len} = {ans}')}.",
            ],
            f"Even without knowing the individual base lengths, {m('\\frac{1}{2} d^2')} fixes the area uniquely!",
            f"بما أن قطري شبه المنحرف المتطابق الساقين متساويان ومتعامدان، فالمساحة {m('\\frac{1}{2} d^2')}!",
            [
                f"طولا القطرين متساويان: {m(f'd_1 = d_2 = {d_len}')}.",
                f"لتعامد القطرين نطبق القانون {m('\\text{Area} = \\frac{1}{2} d_1 d_2')}.",
                f"نحسب: {m(f'\\frac{{1}}{{2}} \\times {d_len}^2 = {ans}')}.",
            ],
            f"تحقق: لا نحتاج معرفة طولَي القاعدتين منفردتين لحساب المساحة!",
        )

    # 4. nsmo_g89_equal_height_area_ratios (5E, 6M, 4H) — SVG: svg_subdivided_apex_triangle / svg_midpoint_square_shaded
    bp = "nsmo_g89_equal_height_area_ratios"
    for p, q, S_tot in [(2, 3, 75), (3, 4, 84), (5, 3, 96)]:
        ans = (p * S_tot) // (p + q)
        B.add_math(
            tp, "Easy", bp,
            f"In {m('\\triangle ABC')} of area {m(S_tot)}, point {m('D')} lies on base {m('BC')} such that {m(f'BD : DC = {p} : {q}')}. What is the area of {m('\\triangle ABD')}?",
            f"في المثلث {m('ABC')} الذي مساحته {m(S_tot)}، تقع النقطة {m('D')} على القاعدة {m('BC')} بحيث {m(f'BD : DC = {p} : {q}')}. ما مساحة المثلث {m('\\triangle ABD')}؟",
            ans, [(q * S_tot) // (p + q), (p * p * S_tot) // ((p + q) ** 2) if (p * p * S_tot) % ((p + q) ** 2) == 0 else ans - 6, S_tot // 2, ans + p],
            f"Triangles {m('ABD')} and {m('ABC')} share the exact same altitude from {m('A')}, so area scales **linearly** with the base (do NOT square {m(f'{p}/{p+q}')}!)!",
            f"يشترك المثلثان {m('ABD')} و{m('ABC')} في نفس الارتفاع من {m('A')}، فتتناسب المساحة **طردياً** مع القاعدة دون تربيع!",
            f"Take the base fraction {m(f'\\frac{{BD}}{{BC}} = \\frac{{{p}}}{{{p + q}}}')} of {m(S_tot)}!",
            [
                f"Since {m('D')} divides {m('BC')} in ratio {m(f'{p} : {q}')}, {m(f'BD = \\frac{{{p}}}{{{p + q}}} BC')}.",
                f"Sharing apex {m('A')} means equal altitude, so {m(f'[\\triangle ABD] = \\frac{{{p}}}{{{p + q}}} [\\triangle ABC]')}.",
                f"Compute {m(f'\\frac{{{p}}}{{{p + q}}} \\times {S_tot} = {ans}')}.",
            ],
            f"Trap alert: equal-height triangles use {m('p/(p+q)')}, NOT {m('(p/(p+q))^2')} (which is for similar triangles)!",
            f"تتناسب المساحتان خطياً مع القاعدتين لاشتراكهما في الارتفاع النازل من {m('A')}!",
            [
                f"نسبة القاعدة {m('BD')} إلى القاعدة الكلية {m('BC')} هي {m(f'\\frac{{{p}}}{{{p + q}}}')}.",
                f"بما أن الارتفاع مشترك نضرب النسبة في المساحة الكلية مباشرة.",
                f"إذن مساحة {m(f'\\triangle ABD = \\frac{{{p}}}{{{p + q}}} \\times {S_tot} = {ans}')}.",
            ],
            f"انتبه: هنا لا نربّع النسبة لأن المثلثين مشتركان في الارتفاع وليسا متشابهين!",
            diagram_en=svg_subdivided_apex_triangle(min(p + q, 5), 1),
        )

    for L_sq in (10, 14):
        ans = (L_sq * L_sq) // 2
        B.add_math(
            tp, "Easy", bp,
            f"The midpoints of the four sides of a square of side length {m(L_sq)} are connected in order to form an inner shaded square. What is the area of the inner shaded square?",
            f"وُصلت منتصفات أضلاع مربع طول ضلعه {m(L_sq)} بالترتيب لتكوين مربع داخلي مظلل. ما مساحة المربع الداخلي المظلل؟",
            ans, [L_sq * L_sq // 4, L_sq * L_sq * 3 // 4, ans + L_sq, 4 * L_sq],
            f"Subtract the four corner right triangles (each with legs {m(L_sq // 2)} and {m(L_sq // 2)}) from {m(f'{L_sq}^2')}!",
            f"اطرح المثلثات القائمة الأربعة عند الأركان (ضلع كل منها {m(L_sq // 2)}) من مساحة المربع {m(f'{L_sq}^2')}!",
            f"Joining the midpoints of any quadrilateral encloses exact **half** its area!",
            [
                f"Outer square area is {m(f'{L_sq}^2 = {L_sq*L_sq}')}.",
                f"Each of the {m(4)} corner right triangles has area {m(f'\\frac{{1}}{{2}}({L_sq//2})({L_sq//2}) = {(L_sq//2)**2 / 2:g}')}, totaling {m(ans)}.",
                f"Inner area {m(f'= {L_sq*L_sq} - {ans} = {ans}')}.",
            ],
            f"Or by Pythagoras: inner side squared equals {m(f'({L_sq//2})^2 + ({L_sq//2})^2 = {ans}')}!",
            f"المربع الواصل بين منتصفات الأضلاع يساوي دائماً **نصف** مساحة المربع الأصلي!",
            [
                f"مساحة المربع الخارجي {m(L_sq * L_sq)}.",
                f"مجموع مساحات المثلثات الأربعة الركنية يساوي {m(ans)}.",
                f"إذن مساحة المربع الداخلي {m(ans)}.",
            ],
            f"تحقق بفيثاغورس: مربع ضلع المربع الداخلي يساوي {m(f'({L_sq//2})^2 + ({L_sq//2})^2 = {ans}')}!",
            diagram_en=svg_midpoint_square_shaded(str(L_sq)),
        )

    for p1, q1, p2, q2, S_tot in [
        (2, 1, 3, 1, 60),
        (3, 2, 1, 2, 90),
        (1, 3, 2, 3, 100),
        (2, 3, 3, 2, 125),
        (3, 1, 2, 1, 72),
        (4, 1, 1, 3, 80),
    ]:
        abd = (p1 * S_tot) // (p1 + q1)
        ans = (p2 * abd) // (p2 + q2)
        B.add_math(
            tp, "Medium", bp,
            f"In {m('\\triangle ABC')} of area {m(S_tot)}, {m('D')} lies on {m('BC')} with {m(f'BD : DC = {p1} : {q1}')}, and {m('E')} lies on segment {m('AD')} with {m(f'AE : ED = {p2} : {q2}')}. Find the area of {m('\\triangle ABE')}.",
            f"في المثلث {m('ABC')} الذي مساحته {m(S_tot)}، تقع {m('D')} على {m('BC')} بحيث {m(f'BD : DC = {p1} : {q1}')}، وتقع {m('E')} على {m('AD')} بحيث {m(f'AE : ED = {p2} : {q2}')}. أوجد مساحة {m('\\triangle ABE')}.",
            ans, [abd, abd - ans, S_tot - abd, ans + p1 * p2],
            f"Step in two stages: first find {m('[\\triangle ABD]')} along base {m('BC')}, then slice {m('\\triangle ABD')} along base {m('AD')}!",
            f"اعمل على مرحلتين: احسب أولاً مساحة {m('\\triangle ABD')} على القاعدة {m('BC')}، ثم قسّمه على القاعدة {m('AD')}!",
            f"Chain two equal-height ratios: {m(f'\\frac{{{p1}}}{{{p1+q1}}} \\times \\frac{{{p2}}}{{{p2+q2}}} \\times {S_tot}')}!",
            [
                f"Along base {m('BC')}, {m(f'[\\triangle ABD] = \\frac{{{p1}}}{{{p1 + q1}}} \\times {S_tot} = {abd}')}.",
                f"Inside {m('\\triangle ABD')}, {m('\\triangle ABE')} and {m('\\triangle EBD')} share apex {m('B')} along base {m('AD')}.",
                f"Thus {m(f'[\\triangle ABE] = \\frac{{{p2}}}{{{p2 + q2}}} \\times {abd} = {ans}')}.",
            ],
            f"Check: {m(f'[\\triangle ABE] + [\\triangle EBD] = {ans} + {abd - ans} = {abd} = [\\triangle ABD]')}!",
            f"نضرب نسبتي القاعدتين المتتاليتين في المساحة الكلية على خطوتين!",
            [
                f"على القاعدة {m('BC')} نجد مساحة {m(f'\\triangle ABD = \\frac{{{p1}}}{{{p1+q1}}} \\times {S_tot} = {abd}')}.",
                f"داخل {m('\\triangle ABD')} يشترك {m('\\triangle ABE')} في الرأس {m('B')} على القاعدة {m('AD')}.",
                f"إذن مساحة {m(f'\\triangle ABE = \\frac{{{p2}}}{{{p2+q2}}} \\times {abd} = {ans}')}.",
            ],
            f"تحقق: مجموع {m('\\triangle ABE')} و{m('\\triangle EBD')} يساوي {m(abd)} تماماً.",
            diagram_en=svg_subdivided_apex_triangle(3, 2),
        )

    for S_tot in (72, 108):
        # Points D on BC (BD = 1/3 BC), E on CA (CE = 1/3 CA), F on AB (AF = 1/3 AB):
        # Each corner triangle [AFD] = (1/3)(2/3) S = 2/9 S! Three corners = 6/9 S = 2/3 S, so [DEF] = 1/3 S!
        ans = S_tot // 3
        B.add_math(
            tp, "Hard", bp,
            f"In {m('\\triangle ABC')} of area {m(S_tot)}, points {m('D, E, F')} lie on sides {m('BC, CA, AB')} respectively such that {m('BD = \\frac{1}{3}BC')}, {m('CE = \\frac{1}{3}CA')}, and {m('AF = \\frac{1}{3}AB')}. What is the area of the inner triangle {m('\\triangle DEF')}?",
            f"في المثلث {m('ABC')} الذي مساحته {m(S_tot)}، تقع النقاط {m('D, E, F')} على الأضلاع {m('BC, CA, AB')} على الترتيب بحيث {m('BD = \\frac{1}{3}BC')} و{m('CE = \\frac{1}{3}CA')} و{m('AF = \\frac{1}{3}AB')}. ما مساحة المثلث الداخلي {m('\\triangle DEF')}؟",
            ans, [S_tot // 9, (2 * S_tot) // 9, (4 * S_tot) // 9, S_tot // 4],
            f"Find the area of each outer corner triangle first: e.g. {m('[\\triangle BDF] = \\frac{BD}{BC} \\cdot \\frac{BF}{BA} [\\triangle ABC] = \\frac{1}{3} \\cdot \\frac{2}{3} S')}!",
            f"احسب مساحة كل مثلث ركني خارجي أولاً: {m('[\\triangle BDF] = \\frac{1}{3} \\times \\frac{2}{3} S = \\frac{2}{9} S')}!",
            f"Subtract the three congruent-fraction corner triangles (each {m('\\frac{2}{9} S')}) from {m('S')}!",
            [
                f"Since {m('AF = \\frac{1}{3}AB')}, we have {m('BF = \\frac{2}{3}AB')}; chaining base ratios gives {m('[\\triangle BDF] = \\frac{1}{3} \\cdot \\frac{2}{3} [\\triangle ABC] = \\frac{2}{9} S')}.",
                f"By cyclic symmetry, {m('[\\triangle CED] = [\\triangle AFE] = \\frac{2}{9} S')} as well.",
                f"Subtract all three corners: {m(f'[\\triangle DEF] = \\left(1 - 3 \\cdot \\frac{{2}}{{9}}\\right) \\times {S_tot} = \\frac{{1}}{{3}} \\times {S_tot} = {ans}')}.",
            ],
            f"Don't confuse **vertex-cevian** Routh's theorem ({m('1/7')}) with **perimeter-point** triangle {m('DEF')} ({m('1/3')})!",
            f"نحسب مساحة كل مثلث من المثلثات الركنية الثلاثة ({m('\\frac{2}{9} S')}) ونطرحها من {m(S_tot)}!",
            [
                f"لكل ركن، حاصل ضرب نسبتي الضلعين المحيطين به هو {m('\\frac{1}{3} \\times \\frac{2}{3} = \\frac{2}{9}')}.",
                f"مجموع مساحات الأركان الثلاثة يساوي {m('3 \\times \\frac{2}{9} S = \\frac{2}{3} S')}.",
                f"يتبقى للمثلث الداخلي {m(f'\\frac{{1}}{{3}} \\times {S_tot} = {ans}')}.",
            ],
            f"تحقق: عند التنصيف ({m('1/2')}) تعطي الطريقة نفسها {m('1 - 3(1/4) = 1/4')}!",
        )

    for S_tot in (90, 126):
        # Medians AD, BE, CF meet at centroid G: 6 equal triangles of area S/6; quad AEGF has 2 of them -> S/3! Let's ask [AEGF] + [BGD] = 3 * S/6? Wait S/2 is too easy to guess! Ask for [AEGF] = S/3? Already used S/3 above! Ask: given [AEGF] = K, find [ABC] = 3K, OR ask for [BDGF] + [CEG] = 3*k, OR if G is centroid and M is midpoint of BG, find [AMD] when [ABC] = S_tot!
        # Let's check: [ABD] = S/2; G divides AD in 2:1 (AG:GD = 2:1), so [BGD] = 1/3 [ABD] = S/6; M is midpoint of BG -> [MGD] = S/12, [ABG] = S/3 -> [AMG] = S/6 -> [AMD] = [AMG] + [MGD] = S/6 + S/12 = S/4? Wait M, G, D are NOT collinear; [AMD] = [ABD] - [ABM] - [MBD]? Wait B, M, G are collinear! So in triangle ABD (area S/2), line BG passes through B, M, G! Wait: [MBD] = 1/2 [GBD] = 1/2 (S/6) = S/12, and [ABM] = 1/2 [ABG] = 1/2 (2/3 * S/2) = S/6! Since M is inside triangle ABD: [ABD] = [ABM] + [MBD] + [AMD] -> [AMD] = S/2 - S/6 - S/12 = S/4!
        # Even cleaner & classic: Medians AD and BE of ABC intersect at centroid G. If [四边形 CDGE] = K (which is 2/6 S = S/3), what is [ABG]? Equal to K! What if we ask: if [△BDG] = k, what is [ABC] - [CDGE]? 4k! Let's do: Medians AD, BE, CF meet at G; point P is the midpoint of AG. Given [ABC] = S_tot (divisible by 12, e.g. 96 and 144), find [△BDP]!
        pass
    for S_tot in (96, 144):
        # [ABD] = S/2. On AD, AG = 2/3 AD, GD = 1/3 AD; P is midpoint of AG, so AP = PG = GD = 1/3 AD -> PD = PG + GD = 2/3 AD!
        # Thus [BDP] = (PD / AD) * [ABD] = (2/3) * (S/2) = S/3? Wait let's ask [BGP] = (1/3)*(S/2) = S/6 or if P is on BG with BP:PG = 1:2 and D is midpoint of BC, [PGD] = (2/3)[BGD] = (2/3)(S/6) = S/9! Let's use S_tot in (90, 126) -> S_tot // 9 = 10 and 14!
        pass
    for S_tot in (90, 126):
        ans = S_tot // 9
        B.add_math(
            tp, "Hard", bp,
            f"In {m('\\triangle ABC')} of area {m(S_tot)}, medians {m('AD')} and {m('BE')} intersect at the centroid {m('G')}, and point {m('P')} lies on segment {m('BG')} with {m('BP : PG = 1 : 2')}. What is the area of {m('\\triangle PGD')}?",
            f"في المثلث {m('ABC')} الذي مساحته {m(S_tot)}، يتقاطع المتوسطان {m('AD')} و{m('BE')} في مركز الثقل {m('G')}، وتقع النقطة {m('P')} على القطعة {m('BG')} بحيث {m('BP : PG = 1 : 2')}. ما مساحة المثلث {m('\\triangle PGD')}؟",
            ans, [S_tot // 6, S_tot // 12 if S_tot % 12 == 0 else ans + 3, (2 * S_tot) // 9, S_tot // 18],
            f"The three medians split {m('\\triangle ABC')} into {m(6)} triangles of equal area, so {m('[\\triangle BGD] = \\frac{1}{6}[\\triangle ABC]')}; then slice along {m('BG')}!",
            f"تقسم المتوسطات المثلث إلى {m(6)} مثلثات متساوية المساحة، فتكون مساحة {m('\\triangle BGD = \\frac{1}{6} S')}، ثم قسّم على القاعدة {m('BG')}!",
            f"Use centroid {m('1/6')}-partition for {m('[\\triangle BGD]')}, then take {m('\\frac{PG}{BG} = \\frac{2}{3}')}!",
            [
                f"Centroid {m('G')} divides each median in a {m('2 : 1')} ratio, making {m(f'[\\triangle BGD] = \\frac{{1}}{{6}} \\times {S_tot} = {S_tot // 6}')}.",
                f"Point {m('P')} splits {m('BG')} into {m('BP : PG = 1 : 2')}, so {m('PG = \\frac{2}{3} BG')}.",
                f"Hence {m(f'[\\triangle PGD] = \\frac{{2}}{{3}} [\\triangle BGD] = \\frac{{2}}{{3}} \\times {S_tot // 6} = {ans}')}.",
            ],
            f"Check: {m(f'[\\triangle BPD] = {S_tot // 18}')} and {m(f'[\\triangle PGD] = {ans}')}, summing to {m(f'[\\triangle BGD] = {S_tot // 6}')}!",
            f"مساحة {m('\\triangle BGD')} تساوي سدس المثلث الكلي، ثم نأخذ ثلثيها وفق نسبة {m('PG : BG')}!",
            [
                f"بخصائص مركز الثقل: مساحة {m(f'\\triangle BGD = \\frac{{1}}{{6}} \\times {S_tot} = {S_tot // 6}')}.",
                f"بما أن {m('BP : PG = 1 : 2')} فإن {m('PG = \\frac{2}{3} BG')}.",
                f"إذن مساحة {m(f'\\triangle PGD = \\frac{{2}}{{3}} \\times {S_tot // 6} = {ans}')}.",
            ],
            f"تحقق: {m(f'{S_tot // 18} + {ans} = {S_tot // 6}')}.",
        )

    # 5. nsmo_g89_regular_polygon_diagonals_angles (5E, 6M, 4H) — SVG: svg_regular_polygon / svg_equilateral_corner_cuts
    bp = "nsmo_g89_regular_polygon_diagonals_angles"
    for n_gon in (9, 10, 12):
        ans = n_gon * (n_gon - 3) // 2
        B.add_math(
            tp, "Easy", bp,
            f"How many diagonals does a convex {m(n_gon)}-sided polygon have?",
            f"كم قطراً للمضلع المحدب ذي الـ {m(n_gon)} أضلاع؟",
            ans, [n_gon * (n_gon - 3), n_gon * (n_gon - 1) // 2, n_gon * (n_gon - 2) // 2, ans - n_gon],
            f"Apply {m('\\frac{n(n - 3)}{2}')}.",
            f"طبّق القانون {m('\\frac{n(n - 3)}{2}')}.",
            f"Subtract the vertex itself and its {m(2)} neighbors ({m('n - 3')} choices per vertex) and divide by {m(2)}!",
            [
                f"Each of the {m(n_gon)} vertices connects to {m(f'{n_gon} - 3 = {n_gon - 3}')} non-adjacent vertices.",
                f"Divide {m(f'{n_gon} \\times {n_gon - 3}')} by {m(2)} so each diagonal is counted once.",
                f"Compute {m(f'\\frac{{{n_gon} \\times {n_gon - 3}}}{{2}} = {ans}')}.",
            ],
            f"Alternative: {m(f'\\binom{{{n_gon}}}{{2}} - {n_gon} = {n_gon*(n_gon-1)//2} - {n_gon} = {ans}')}!",
            f"نطبق صيغة عدد الأقطار {m('\\frac{n(n - 3)}{2}')}!",
            [
                f"يخرج من كل رأس {m(f'{n_gon} - 3 = {n_gon - 3}')} أقطار.",
                f"نقسم حاصل الضرب على {m(2)} لمنع التكرار.",
                f"الناتج: {m(f'\\frac{{{n_gon} \\times {n_gon - 3}}}{{2}} = {ans}')} قطراً.",
            ],
            f"تحقق بالتوافيق: جميع القطع الواصلة {m(f'\\binom{{{n_gon}}}{{2}}')} مطروحاً منها الأضلاع {m(n_gon)} تعطي {m(ans)}.",
            diagram_en=svg_regular_polygon(min(n_gon, 8), chords=((0, 2), (0, 3), (0, 4))),
        )

    for n_gon in (10, 12):
        ans = 180 - 360 // n_gon
        B.add_math(
            tp, "Easy", bp,
            f"What is the measure (in degrees) of one interior angle of a regular {m(n_gon)}-gon?",
            f"ما قياس الزاوية الداخلية الواحدة (بالدرجات) في مضلع منتظم ذي {m(n_gon)} أضلاع؟",
            ans, [360 // n_gon, 180 - 180 // n_gon, ans - 12, ans + 6],
            f"Subtract one exterior angle {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')} from {m('180^\\circ')}.",
            f"اطرح الزاوية الخارجية {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')} من {m('180^\\circ')}.",
            f"Compute the exterior angle {m(f'360^\\circ / {n_gon}')} first, then subtract from {m('180^\\circ')}!",
            [
                f"Each exterior angle of a regular {m(n_gon)}-gon is {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')}.",
                f"Interior and exterior angles at any vertex are supplementary.",
                f"Thus {m(f'180^\\circ - {360 // n_gon}^\\circ = {ans}^\\circ')}.",
            ],
            f"Check: {m(f'({n_gon} - 2) \\times 180^\\circ / {n_gon} = {ans}^\\circ')}.",
            f"نحسب الزاوية الخارجية {m(f'360^\\circ / {n_gon}')} ثم نطرحها من {m('180^\\circ')}!",
            [
                f"الزاوية الخارجية تساوي {m(f'{360 // n_gon}^\\circ')}.",
                f"الزاوية الداخلية تكملها إلى {m('180^\\circ')}.",
                f"إذن القياس هو {m(f'180^\\circ - {360 // n_gon}^\\circ = {ans}^\\circ')}.",
            ],
            f"تحقق: {m(f'{n_gon} \\times {ans}^\\circ = {(n_gon - 2) * 180}^\\circ')}.",
            diagram_en=svg_regular_polygon(min(n_gon, 8)),
        )

    for D_cnt, n_ans in [(35, 10), (54, 12), (77, 14)]:
        assert n_ans * (n_ans - 3) // 2 == D_cnt
        ans = (n_ans - 2) * 180
        B.add_math(
            tp, "Medium", bp,
            f"A convex polygon has exact {m(D_cnt)} diagonals. What is the **sum of its interior angles**, in degrees?",
            f"مضلع محدب له بالضبط {m(D_cnt)} قطراً. ما **مجموع قياسات زواياه الداخلية** بالدرجات؟",
            ans, [n_ans * 180, (n_ans - 3) * 180, (n_ans - 1) * 180, ans + 360],
            f"Solve {m(f'n(n - 3) = {2 * D_cnt}')} for {m('n')}, then compute {m('(n - 2) \\times 180^\\circ')}!",
            f"حل المعادلة {m(f'n(n - 3) = {2 * D_cnt}')} لإيجاد {m('n')} ثم احسب {m('(n - 2) \\times 180^\\circ')}!",
            f"Recover {m('n')} by factoring {m(2 * D_cnt)} into two integers differing by {m(3)}!",
            [
                f"From {m(f'\\frac{{n(n - 3)}}{{2}} = {D_cnt}')}, we get {m(f'n(n - 3) = {2 * D_cnt} = {n_ans} \\times {n_ans - 3}')}, so {m(f'n = {n_ans}')}.",
                f"Apply the interior-angle sum formula {m('(n - 2) \\times 180^\\circ')}.",
                f"Compute {m(f'({n_ans} - 2) \\times 180^\\circ = {ans}^\\circ')}.",
            ],
            f"Factoring {m(2 * D_cnt)} as {m(f'{n_ans} \\times {n_ans - 3}')} avoids the quadratic formula completely!",
            f"نحلّل {m(2 * D_cnt)} إلى عاملين فرقهما {m(3)} لإيجاد {m('n')} ثم نحسب {m('(n - 2) \\times 180^\\circ')}!",
            [
                f"من {m(f'n(n - 3) = {2 * D_cnt}')} نجد {m(f'n = {n_ans}')}.",
                f"مجموع الزوايا الداخلية يساوي {m(f'({n_ans} - 2) \\times 180^\\circ')}.",
                f"الناتج يساوي {m(ans)} درجة.",
            ],
            f"تحقق: لا تخلط بين {m('(n - 2)\\cdot 180^\\circ')} و{m('n \\cdot 180^\\circ')}!",
        )

    for big_s, area_tri in [(9, 81), (12, 108), (15, 135)]:
        # Equilateral triangle of side 3a and given area area_tri: cutting corners of side a leaves regular hexagon of 6 small triangles out of 9 -> 2/3 * area_tri!
        ans = (2 * area_tri) // 3
        B.add_math(
            tp, "Medium", bp,
            f"An equilateral triangle of side length {m(big_s)} has area {m(area_tri)} (in playful grid units). Small equilateral triangles of side length {m(big_s // 3)} are cut off from all three corners to form a regular hexagon. What is the area of this regular hexagon (in the same units)?",
            f"مثلث متطابق الأضلاع طول ضلعه {m(big_s)} ومساحته {m(area_tri)} وحدة مربعة افتراضية. قُطع من كل ركن من أركانه الثلاثة مثلث صغير متطابق الأضلاع طول ضلعه {m(big_s // 3)} فتكوّن سداسي منتظم. ما مساحة هذا السداسي المنتظم (بنفس الوحدات)؟",
            ans, [area_tri // 2, (3 * area_tri) // 4 if (3 * area_tri) % 4 == 0 else ans + 9, (8 * area_tri) // 9, area_tri - area_tri // 9],
            f"Tile the big equilateral triangle of side {m('3a')} into {m('3^2 = 9')} congruent small equilateral triangles of side {m('a')}!",
            f"قسّم المثلث الكبير الذي ضلعه {m('3a')} إلى {m('3^2 = 9')} مثلثات صغيرة متطابقة ضلع كل منها {m('a')}!",
            f"Each corner cut has {m('(1/3)^2 = 1/9')} of the big triangle's area, so removing {m(3)} corners leaves {m('6/9 = 2/3')}!",
            [
                f"Scaling side length by {m('1/3')} scales area by {m('(1/3)^2 = 1/9')}, so each removed corner has area {m(f'{area_tri}/9 = {area_tri // 9}')}.",
                f"Removing {m(3)} corners subtracts {m(f'3 \\times {area_tri // 9} = {area_tri // 3}')}.",
                f"Hexagon area {m(f'= {area_tri} - {area_tri // 3} = {ans}')} ({m(6)} of the {m(9)} unit triangles).",
            ],
            f"Visualizing {m(6)} small triangles in the hexagon plus {m(3)} at the tips = {m(9)} makes this unforgettable!",
            f"ينقسم المثلث الكبير إلى {m(9)} مثلثات صغيرة متطابقة، يأخذ السداسي المنتظم {m(6)} منها!",
            [
                f"مساحة كل ركن مقطوع تساوي {m(f'(1/3)^2 = 1/9')} من المساحة الكلية أي {m(area_tri // 9)}.",
                f"مجموع الأركان الثلاثة يساوي {m(area_tri // 3)}.",
                f"مساحة السداسي المتبقية هي {m(f'{area_tri} - {area_tri // 3} = {ans}')}.",
            ],
            f"تحقق بصري: السداسي المنتظم يتألف من {m(6)} مثلثات متطابقة الأضلاع من أصل {m(9)}!",
            diagram_en=svg_equilateral_corner_cuts(str(big_s), str(big_s // 3)),
        )

    for n_gon, k1, k2 in [(12, 3, 8), (10, 3, 7)]:
        # Regular n-gon A_1 ... A_n, angle A_1 A_{k1} A_{k2}: chord chords from A_1 -> A_{k1} (k1-1 sides) and A_{k1} -> A_{k2} (k2-k1 sides), remaining arc A_{k2} -> A_1 has n - (k2 - 1) sides!
        rem_sides = n_gon - (k2 - 1)
        arc_deg = rem_sides * (360 // n_gon)
        ans = arc_deg // 2
        B.add_math(
            tp, "Hard", bp,
            f"The vertices of a regular {m(n_gon)}-gon are labeled {m(f'A_1, A_2, \\dots, A_{{{n_gon}}}')} in clockwise order. What is the measure of {m(f'\\angle A_1 A_{{{k1}}} A_{{{k2}}}')}, in degrees?",
            f"رُقمت رؤوس مضلع منتظم ذي {m(n_gon)} أضلاع بالترتيب مع عقارب الساعة {m(f'A_1, A_2, \\dots, A_{{{n_gon}}}')}. ما قياس الزاوية {m(f'\\angle A_1 A_{{{k1}}} A_{{{k2}}}')} بالدرجات؟",
            ans, [arc_deg, ans - (180 // n_gon), ans + (180 // n_gon), 180 - ans],
            f"Inscribe the regular {m(n_gon)}-gon in its circumcircle! Each side subtends an arc of {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')}.",
            f"احط المضلع المنتظم بدائرته المارة برؤوسه! كل ضلع يقابل قوساً قياسه {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')}.",
            f"Count how many polygon edges lie on the intercepted arc from {m(f'A_{{{k2}}}')} clockwise back to {m('A_1')}, then halve that arc!",
            [
                f"Every regular polygon is cyclic, and each edge subtends {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')} on the circumcircle.",
                f"Going clockwise, {m(f'A_1 \\to A_{{{k1}}}')} spans {m(k1 - 1)} edges and {m(f'A_{{{k1}}} \\to A_{{{k2}}}')} spans {m(k2 - k1)} edges, so the intercepted arc {m(f'A_{{{k2}}} \\to A_1')} spans {m(f'{n_gon} - {k2 - 1} = {rem_sides}')} edges ({m(f'{arc_deg}^\\circ')}).",
                f"By the Inscribed Angle Theorem, {m(f'\\angle A_1 A_{{{k1}}} A_{{{k2}}} = {arc_deg}^\\circ / 2 = {ans}^\\circ')}.",
            ],
            f"Circumcircle arc-counting solves **any** regular-polygon diagonal angle in seconds!",
            f"نرسم الدائرة المحيطة بالمضلع ونعدّ أضلاع القوس المقابل للزاوية المحيطية {m(f'\\angle A_1 A_{{{k1}}} A_{{{k2}}}')}!",
            [
                f"قياس قوس الضلع الواحد هو {m(f'360^\\circ / {n_gon} = {360 // n_gon}^\\circ')}.",
                f"القوس المقابل للزاوية يمتد من {m(f'A_{{{k2}}}')} حتى {m('A_1')} ويضم {m(rem_sides)} أضلاع قياسها {m(f'{arc_deg}^\\circ')}.",
                f"الزاوية المحيطية تساوي نصف القوس: {m(f'{arc_deg}^\\circ \\div 2 = {ans}^\\circ')}.",
            ],
            f"تحقق: مجموع القوسين حول الرأس {m(f'A_{{{k1}}}')} مع القوس المقابل يساوي {m(n_gon)} أضلاع كاملة!",
            diagram_en=svg_regular_polygon(8, chords=((0, 2), (2, 6))),
        )

    # 2 Hard shared-edge regular polygon isosceles-triangle angle chasers:
    # 1) Regular pentagon ABCDE + square ABFG inside -> angle EAG = 108 - 90 = 18 -> angle AEG = (180 - 18)/2 = 81
    B.add_math(
        tp, "Hard", bp,
        f"Regular pentagon {m('ABCDE')} and square {m('ABFG')} share side {m('AB')}, with vertices {m('F')} and {m('G')} lying **inside** the pentagon. What is the measure of {m('\\angle AEG')}, in degrees?",
        f"يشترك الخماسي المنتظم {m('ABCDE')} والمربع {m('ABFG')} في الضلع {m('AB')} بحيث تقع الرأسان {m('F')} و{m('G')} **داخل** الخماسي. ما قياس الزاوية {m('\\angle AEG')} بالدرجات؟",
        81, [18, 72, 84, 99],
        f"Spot the hidden isosceles triangle! Both {m('AE')} and {m('AG')} equal {m('AB')}, so {m('AE = AG')}!",
        f"اكتشف المثلث المتطابق الضلعين المخفي! كل من {m('AE')} و{m('AG')} يساوي الضلع المشترك {m('AB')}، إذن {m('AE = AG')}!",
        f"Use {m('AE = AB = AG')} so {m('\\triangle EAG')} is isosceles with apex angle {m('108^\\circ - 90^\\circ = 18^\\circ')}!",
        [
            f"In regular pentagon {m('ABCDE')}, {m('\\angle BAE = 108^\\circ')}, and in square {m('ABFG')}, {m('\\angle BAG = 90^\\circ')}, so {m('\\angle EAG = 108^\\circ - 90^\\circ = 18^\\circ')}.",
            f"Because {m('AE = AB')} and {m('AG = AB')}, triangle {m('EAG')} is **isosceles** with {m('AE = AG')}.",
            f"Therefore {m('\\angle AEG = \\frac{180^\\circ - 18^\\circ}{2} = 81^\\circ')}.",
        ],
        f"Hidden equal-edge transfer ({m('AE = AB = AG')}) is the #1 key to Olympiad shared-polygon puzzles!",
        f"بما أن {m('AE = AB = AG')} فإن المثلث {m('EAG')} متطابق الضلعين وزاوية رأسه {m('108^\\circ - 90^\\circ = 18^\\circ')}!",
        [
            f"زاوية الخماسي {m('108^\\circ')} وزاوية المربع {m('90^\\circ')}، إذن {m('\\angle EAG = 18^\\circ')}.",
            f"المثلث {m('EAG')} متطابق الضلعين لأن {m('AE = AB = AG')}.",
            f"قياس زاوية القاعدة {m('\\angle AEG = (180^\\circ - 18^\\circ) \\div 2 = 81^\\circ')}.",
        ],
        f"تحقق: {m('18^\\circ + 81^\\circ + 81^\\circ = 180^\\circ')}!",
        diagram_en=svg_regular_polygon(5),
    )

    # 2) Regular hexagon ABCDEF + square ABGH inside -> angle FAH = 120 - 90 = 30 -> angle AFH = (180 - 30)/2 = 75
    B.add_math(
        tp, "Hard", bp,
        f"Regular hexagon {m('ABCDEF')} and square {m('ABGH')} share side {m('AB')}, with {m('G')} and {m('H')} lying **inside** the hexagon. What is the measure of {m('\\angle AFH')}, in degrees?",
        f"يشترك السداسي المنتظم {m('ABCDEF')} والمربع {m('ABGH')} في الضلع {m('AB')} بحيث تقع {m('G')} و{m('H')} **داخل** السداسي. ما قياس الزاوية {m('\\angle AFH')} بالدرجات؟",
        75, [30, 60, 70, 80],
        f"Compare {m('AF')} and {m('AH')}: both equal {m('AB')}, making {m('\\triangle FAH')} isosceles!",
        f"قارن بين {m('AF')} و{m('AH')}؛ كلاهما يساوي {m('AB')} فيكون المثلث {m('FAH')} متطابق الضلعين!",
        f"Use {m('AF = AB = AH')} in isosceles {m('\\triangle FAH')} with apex angle {m('120^\\circ - 90^\\circ = 30^\\circ')}!",
        [
            f"Interior angle {m('\\angle BAF = 120^\\circ')} in the hexagon and {m('\\angle BAH = 90^\\circ')} in the square give {m('\\angle FAH = 120^\\circ - 90^\\circ = 30^\\circ')}.",
            f"Since {m('AF = AB = AH')}, {m('\\triangle FAH')} is isosceles with base {m('FH')}.",
            f"Compute {m('\\angle AFH = \\frac{180^\\circ - 30^\\circ}{2} = 75^\\circ')}.",
        ],
        f"Had the square been built **outside** the hexagon, {m('\\angle FAH')} would be {m('120^\\circ + 90^\\circ \\to 150^\\circ')} reflex ({m('15^\\circ')} base angles)!",
        f"المثلث {m('FAH')} متطابق الضلعين لأن {m('AF = AB = AH')} وزاوية رأسه {m('120^\\circ - 90^\\circ = 30^\\circ')}!",
        [
            f"زاوية السداسي {m('120^\\circ')} وزاوية المربع {m('90^\\circ')}، فزاوية الرأس {m('\\angle FAH = 30^\\circ')}.",
            f"من تساوي الضلعين {m('AF = AH')} تتساوى زاويتا القاعدة.",
            f"إذن {m('\\angle AFH = (180^\\circ - 30^\\circ) \\div 2 = 75^\\circ')}.",
        ],
        f"انتبه لكلمة **داخل** السداسي ({m('30^\\circ')}) مقابل خارجه ({m('150^\\circ')})!",
        diagram_en=svg_regular_polygon(6),
    )



def _dp_grid_paths(cols: int, rows: int, blocked_nodes: set = None, blocked_edges: set = None) -> int:
    blocked_nodes = blocked_nodes or set()
    blocked_edges = blocked_edges or set()
    dp = [[0] * (rows + 1) for _ in range(cols + 1)]
    dp[0][0] = 0 if (0, 0) in blocked_nodes else 1
    for x in range(cols + 1):
        for y in range(rows + 1):
            if (x, y) == (0, 0) or (x, y) in blocked_nodes:
                continue
            v = 0
            if x > 0 and ((x - 1, y), (x, y)) not in blocked_edges:
                v += dp[x - 1][y]
            if y > 0 and ((x, y - 1), (x, y)) not in blocked_edges:
                v += dp[x][y - 1]
            dp[x][y] = v
    return dp[cols][rows]


# =============================================================================
# UNIT 2.6 — Lattice Paths, Stars & Bars, PIE, Graphs & Conditional Urns (75 Qs)
# =============================================================================
def _add_unit_2_6(B: BankBuilder) -> None:
    tp = "Combinatorics & Logic"

    # 1. nsmo_g89_blocked_lattice_paths (5E, 6M, 4H) — SVG: svg_street_grid
    bp = "nsmo_g89_blocked_lattice_paths"
    for cols, rows in [(3, 3), (4, 2), (5, 2), (4, 3), (5, 3)]:
        ans = math.comb(cols + rows, rows)
        assert ans == _dp_grid_paths(cols, rows)
        B.add_math(
            tp, "Easy", bp,
            f"Starting at corner {m('A(0,0)')} of a {m(f'{cols} \\times {rows}')} rectangular street grid, how many shortest paths reach {m(f'B({cols},{rows})')} moving only East ({m('+x')}) and North ({m('+y')})?",
            f"انطلاقاً من الركن {m('A(0,0)')} على شبكة طرق مستطيلة أبعادها {m(f'{cols} \\times {rows}')}، كم مساراً أقصر يصل إلى {m(f'B({cols},{rows})')} بالتحرك شرقاً وشمالاً فقط؟",
            ans, [cols * rows, math.comb(cols + rows - 1, rows), ans + cols, 2 ** rows * cols],
            f"Choose which {m(rows)} of the {m(cols + rows)} total steps go North: {m(f'\\binom{{{cols + rows}}}{{{rows}}}')}.",
            f"اختر مواقع الـ {m(rows)} خطوات المتجهة شمالاً من أصل {m(cols + rows)} خطوة كلية: {m(f'\\binom{{{cols + rows}}}{{{rows}}}')}.",
            f"Count sequences of {m(cols)} East steps and {m(rows)} North steps via {m(f'\\binom{{{cols}+{rows}}}{{{rows}}}')}!",
            [
                f"Every shortest path consists of exact {m(cols)} East steps and {m(rows)} North steps ({m(cols + rows)} steps total).",
                f"Choosing which {m(rows)} steps go North fixes the path uniquely.",
                f"Compute {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {ans}')}.",
            ],
            f"Symmetry check: {m(f'\\binom{{{cols + rows}}}{{{cols}}} = \\binom{{{cols + rows}}}{{{rows}}} = {ans}')}.",
            f"كل مسار أقصر يتحدد باختيار {m(rows)} خطوات شمالاً من أصل {m(cols + rows)} خطوة!",
            [
                f"طول أي مسار أقصر هو {m(f'{cols} + {rows} = {cols + rows}')} خطوة.",
                f"عدد طرق ترتيب {m(cols)} خطوات شرقاً و{m(rows)} شمالاً هو {m(f'\\binom{{{cols + rows}}}{{{rows}}}')}.",
                f"بحساب التوافيق نحصل على {m(ans)} مساراً.",
            ],
            f"تحقق بالتناظر: {m(f'\\binom{{{cols + rows}}}{{{cols}}} = {ans}')}.",
            diagram_en=svg_street_grid(cols, rows),
        )

    for cols, rows, px, py in [(4, 4, 2, 2), (5, 3, 2, 2), (5, 4, 3, 2)]:
        ans = math.comb(px + py, px) * math.comb((cols - px) + (rows - py), cols - px)
        B.add_math(
            tp, "Medium", bp,
            f"On a {m(f'{cols} \\times {rows}')} street grid from {m('A(0,0)')} to {m(f'B({cols},{rows})')}, how many shortest (East/North) paths **must pass through** checkpoint {m(f'P({px},{py})')}?",
            f"على شبكة طرق {m(f'{cols} \\times {rows}')} من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')}، كم مساراً أقصر (شرقاً/شمالاً) **يمر وجوباً** بنقطة التفتيش {m(f'P({px},{py})')}؟",
            ans, [math.comb(cols + rows, rows) - ans, math.comb(px + py, px) + math.comb((cols - px) + (rows - py), cols - px), ans + 6, math.comb(cols + rows, rows)],
            f"Multiply the path count from {m('A')} to {m('P')} by the path count from {m('P')} to {m('B')}!",
            f"اضرب عدد المسارات من {m('A')} إلى {m('P')} في عدد المسارات من {m('P')} إلى {m('B')}!",
            f"Split the journey at {m('P')} and multiply independent leg counts!",
            [
                f"Paths from {m('(0,0)')} to {m(f'({px},{py})')} equal {m(f'\\binom{{{px + py}}}{{{px}}} = {math.comb(px + py, px)}')}.",
                f"Paths from {m(f'({px},{py})')} to {m(f'({cols},{rows})')} equal {m(f'\\binom{{{(cols-px)+(rows-py)}}}{{{cols-px}}} = {math.comb((cols-px)+(rows-py), cols-px)}')}.",
                f"By the multiplication rule, {m(f'{math.comb(px + py, px)} \\times {math.comb((cols-px)+(rows-py), cols-px)} = {ans}')}.",
            ],
            f"Remember independent sequential stages **multiply**, never add!",
            f"نقسم المسار عند {m('P')} إلى مرحلتين مستقلتين ونضرب عددي مساراتهما!",
            [
                f"من {m('A')} إلى {m('P')} يوجد {m(f'\\binom{{{px+py}}}{{{px}}} = {math.comb(px+py, px)}')} مساراً.",
                f"ومن {m('P')} إلى {m('B')} يوجد {m(f'\\binom{{{(cols-px)+(rows-py)}}}{{{cols-px}}} = {math.comb((cols-px)+(rows-py), cols-px)}')} مساراً.",
                f"بمبدأ الضرب: {m(f'{math.comb(px+py, px)} \\times {math.comb((cols-px)+(rows-py), cols-px)} = {ans}')}.",
            ],
            f"انتبه: المرحلتان المتتاليتان تُضربان ولا تُجمعان!",
            diagram_en=svg_street_grid(cols, rows),
        )

    for cols, rows, bx, by in [(4, 4, 2, 2), (5, 3, 3, 1), (5, 4, 2, 2)]:
        tot = math.comb(cols + rows, rows)
        bad = math.comb(bx + by, bx) * math.comb((cols - bx) + (rows - by), cols - bx)
        ans = tot - bad
        assert ans == _dp_grid_paths(cols, rows, blocked_nodes={(bx, by)})
        B.add_math(
            tp, "Medium", bp,
            f"On a {m(f'{cols} \\times {rows}')} street grid from {m('A(0,0)')} to {m(f'B({cols},{rows})')}, intersection {m(f'P({bx},{by})')} is blocked. How many shortest (East/North) paths from {m('A')} to {m('B')} avoid {m('P')}?",
            f"على شبكة طرق {m(f'{cols} \\times {rows}')} من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')}، أُغلق التقاطع {m(f'P({bx},{by})')}. كم مساراً أقصر من {m('A')} إلى {m('B')} يتجنب {m('P')}؟",
            ans, [bad, tot, ans + 4, ans - 4],
            f"Subtract the {m('A \\to P \\to B')} paths from all {m(f'\\binom{{{cols+rows}}}{{{rows}}} = {tot}')} paths!",
            f"اطرح المسارات المارة عبر {m('P')} من إجمالي المسارات الكلية {m(tot)}!",
            f"Use complementary counting: Total paths minus paths hitting {m('P')}!",
            [
                f"Unrestricted paths: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {tot}')}.",
                f"Paths through {m(f'P({bx},{by})')}: {m(f'\\binom{{{bx + by}}}{{{bx}}} \\times \\binom{{{(cols-bx)+(rows-by)}}}{{{cols-bx}}} = {bad}')}.",
                f"Valid paths avoiding {m('P')}: {m(f'{tot} - {bad} = {ans}')}.",
            ],
            f"Don't stop at {m(bad)} — subtract it from {m(tot)} to get {m(ans)}!",
            f"نطبق العدّ التكميلي بطرح المسارات المارة بـ {m('P')} من العدد الكلي!",
            [
                f"إجمالي المسارات بدون عوائق هو {m(tot)}.",
                f"المسارات المارة بالتقاطع المغلق {m('P')} عددها {m(bad)}.",
                f"إذن المسارات المسموحة تساوي {m(f'{tot} - {bad} = {ans}')}.",
            ],
            f"تحقق: مجموع المسارات المسموحة ({m(ans)}) والممنوعة ({m(bad)}) يعيد {m(tot)}.",
            diagram_en=svg_street_grid(cols, rows, blocked=(bx, by)),
        )

    for cols, rows, p1, p2 in [(4, 4, (1, 1), (3, 3)), (5, 4, (2, 1), (3, 3))]:
        ans = _dp_grid_paths(cols, rows, blocked_nodes={p1, p2})
        tot = math.comb(cols + rows, rows)
        n1 = math.comb(p1[0] + p1[1], p1[0]) * math.comb((cols - p1[0]) + (rows - p1[1]), cols - p1[0])
        n2 = math.comb(p2[0] + p2[1], p2[0]) * math.comb((cols - p2[0]) + (rows - p2[1]), cols - p2[0])
        n12 = math.comb(p1[0] + p1[1], p1[0]) * math.comb((p2[0] - p1[0]) + (p2[1] - p1[1]), p2[0] - p1[0]) * math.comb((cols - p2[0]) + (rows - p2[1]), cols - p2[0])
        assert ans == tot - n1 - n2 + n12
        B.add_math(
            tp, "Hard", bp,
            f"On a {m(f'{cols} \\times {rows}')} grid from {m('A(0,0)')} to {m(f'B({cols},{rows})')}, **both** intersections {m(f'P_1{p1}')} and {m(f'P_2{p2}')} are blocked. How many shortest (East/North) paths reach {m('B')}?",
            f"على شبكة {m(f'{cols} \\times {rows}')} من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')}، أُغلق التقاطعان {m(f'P_1{p1}')} و{m(f'P_2{p2}')} معاً. كم مساراً أقصر يصل إلى {m('B')}؟",
            ans, [tot - n1 - n2, tot - n1, ans + n12, ans - 4],
            f"Use Inclusion–Exclusion! Paths hitting **both** {m('P_1')} and {m('P_2')} were subtracted twice, so add {m('|A \\to P_1 \\to P_2 \\to B|')} back!",
            f"طبّق التضمين والإقصاء! المسارات المارة بـ {m('P_1')} ثم {m('P_2')} معاً طُرحت مرتين فيجب إعادة جمعها!",
            f"Apply Inclusion–Exclusion: {m('\\text{Total} - |P_1| - |P_2| + |P_1 \\cap P_2|')}!",
            [
                f"Total unrestricted paths: {m(tot)}. Paths through {m('P_1')}: {m(n1)}; paths through {m('P_2')}: {m(n2)}.",
                f"Since {m('P_2')} is northeast of {m('P_1')}, paths through **both** ({m('A \\to P_1 \\to P_2 \\to B')}) equal {m(n12)}.",
                f"By Inclusion–Exclusion: {m(f'{tot} - {n1} - {n2} + {n12} = {ans}')}.",
            ],
            f"Forgetting {m(f'+{n12}')} undercounts by {m(n12)} and gives the #1 trap {m(tot - n1 - n2)}!",
            f"نطرح مسارات {m('P_1')} ومسارات {m('P_2')} ثم نعيد جمع المسارات المارة بهما معاً!",
            [
                f"العدد الكلي {m(tot)}، ومسارات {m('P_1')} هي {m(n1)}، ومسارات {m('P_2')} هي {m(n2)}.",
                f"المسارات المارة بالاثنين معاً {m('A \\to P_1 \\to P_2 \\to B')} تساوي {m(n12)}.",
                f"بالتضمين والإقصاء: {m(f'{tot} - {n1} - {n2} + {n12} = {ans}')}.",
            ],
            f"انتبه: إغفال إعادة جمع التقاطع {m(n12)} يوقع في الفخ {m(tot - n1 - n2)}!",
            diagram_en=svg_street_grid(cols, rows, blocked=p1),
        )

    for cols, rows, u_pt, v_pt in [(4, 3, (1, 1), (2, 1)), (5, 3, (2, 1), (3, 1))]:
        ans = _dp_grid_paths(cols, rows, blocked_edges={(u_pt, v_pt)})
        tot = math.comb(cols + rows, rows)
        bad = math.comb(u_pt[0] + u_pt[1], u_pt[0]) * math.comb((cols - v_pt[0]) + (rows - v_pt[1]), cols - v_pt[0])
        assert ans == tot - bad
        B.add_math(
            tp, "Hard", bp,
            f"On a {m(f'{cols} \\times {rows}')} street grid from {m('A(0,0)')} to {m(f'B({cols},{rows})')}, only the **single road segment** joining {m(f'{u_pt}')} to {m(f'{v_pt}')} is closed (both endpoints remain open for Northbound turns!). How many shortest paths reach {m('B')}?",
            f"على شبكة طرق {m(f'{cols} \\times {rows}')} من {m('A(0,0)')} إلى {m(f'B({cols},{rows})')}، أُغلقت **قطعة الطريق الواحدة** الواصلة بين {m(f'{u_pt}')} و{m(f'{v_pt}')} فقط (بينما يبقى التقاطعان مفتوحين للانعطاف شمالاً). كم مساراً أقصر يصل إلى {m('B')}؟",
            ans, [_dp_grid_paths(cols, rows, blocked_nodes={u_pt}), tot, bad, ans - 3],
            f"A path uses the closed segment iff it goes {m(f'A \\to {u_pt}')}, steps directly along the closed edge to {m(f'{v_pt}')}, and continues {m(f'{v_pt} \\to B')}!",
            f"يستخدم المسار القطعة المغلقة إذا وفقط إذا وصل إلى {m(f'{u_pt}')} ثم عبر القطعة إلى {m(f'{v_pt}')} ثم أكمل إلى {m('B')}!",
            f"Subtract paths traversing the directed edge {m(f'{u_pt} \\to {v_pt}')}: {m(f'|A \\to {u_pt}| \\times 1 \\times |{v_pt} \\to B|')}!",
            [
                f"Total shortest paths: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {tot}')}.",
                f"Paths crossing edge {m(f'{u_pt} \\to {v_pt}')} equal {m(f'\\binom{{{u_pt[0]+u_pt[1]}}}{{{u_pt[0]}}} \\times 1 \\times \\binom{{{(cols-v_pt[0])+(rows-v_pt[1])}}}{{{cols-v_pt[0]}}} = {bad}')}.",
                f"Subtracting gives {m(f'{tot} - {bad} = {ans}')} valid paths.",
            ],
            f"Contrast: blocking **node** {m(f'{u_pt}')} removes more paths than blocking just **edge** {m(f'{u_pt} \\to {v_pt}')}!",
            f"نطرح فقط المسارات التي تعبر القطعة المغلقة من {m(f'{u_pt}')} إلى {m(f'{v_pt}')}!",
            [
                f"إجمالي المسارات الكلية يساوي {m(tot)}.",
                f"عدد المسارات العابرة للقطعة المغلقة هو {m(f'\\binom{{{u_pt[0]+u_pt[1]}}}{{{u_pt[0]}}} \\times \\binom{{{(cols-v_pt[0])+(rows-v_pt[1])}}}{{{cols-v_pt[0]}}} = {bad}')}.",
                f"عدد المسارات المسموحة هو {m(f'{tot} - {bad} = {ans}')}.",
            ],
            f"مقارنة ذكية: إغلاق قطعة واحدة يحذف مسارات أقل من إغلاق التقاطع كاملاً!",
            diagram_en=svg_street_grid(cols, rows),
        )

    # 2. nsmo_g89_stars_and_bars_distributions (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g89_stars_and_bars_distributions"
    for n_sum, k_vars in [(9, 3), (10, 4), (12, 3), (8, 4), (11, 4)]:
        ans = math.comb(n_sum - 1, k_vars - 1)
        B.add_math(
            tp, "Easy", bp,
            f"How many ordered {m(k_vars)}-tuples of **positive integers** {m(f'(x_1, \\dots, x_{{{k_vars}}})')} satisfy {m(f'x_1 + \\cdots + x_{{{k_vars}}} = {n_sum}')}?",
            f"كم {m(k_vars)}-ية مرتبة من **الأعداد الصحيحة الموجبة** {m(f'(x_1, \\dots, x_{{{k_vars}}})')} تحقق المعادلة {m(f'x_1 + \\cdots + x_{{{k_vars}}} = {n_sum}')}؟",
            ans, [math.comb(n_sum + k_vars - 1, k_vars - 1), math.comb(n_sum, k_vars - 1), ans - 5, ans + 8],
            f"Place {m(k_vars - 1)} divider bars among the {m(n_sum - 1)} interior gaps: {m(f'\\binom{{{n_sum - 1}}}{{{k_vars - 1}}}')}.",
            f"ضع {m(k_vars - 1)} فواصل في الفراغات الداخلية البالغ عددها {m(n_sum - 1)}: {m(f'\\binom{{{n_sum - 1}}}{{{k_vars - 1}}}')}.",
            f"Apply positive-integer Stars and Bars {m('\\binom{n - 1}{k - 1}')}!",
            [
                f"With {m(n_sum)} stars in a row, there are {m(n_sum - 1)} interior gaps.",
                f"Choose {m(k_vars - 1)} gaps to split into {m(k_vars)} positive parts.",
                f"Compute {m(f'\\binom{{{n_sum - 1}}}{{{k_vars - 1}}} = {ans}')}.",
            ],
            f"Watch out: {m(f'\\binom{{{n_sum + k_vars - 1}}}{{{k_vars - 1}}}')} is for **non-negative** ({m('\\ge 0')}), whereas positive ({m('\\ge 1')}) gives {m(ans)}!",
            f"نطبق قانون النجوم والفواصل للأعداد الموجبة {m('\\binom{n - 1}{k - 1}')}!",
            [
                f"يوجد {m(n_sum - 1)} فراغاً داخلياً بين {m(n_sum)} وحدة.",
                f"نختار {m(k_vars - 1)} فواصل لتقسيمها إلى {m(k_vars)} أجزاء موجبة.",
                f"الناتج: {m(f'\\binom{{{n_sum - 1}}}{{{k_vars - 1}}} = {ans}')}.",
            ],
            f"تحقق: لا تخلط بين قانون الموجبة {m('\\binom{n-1}{k-1}')} وغير السالبة {m('\\binom{n+k-1}{k-1}')}!",
            diagram_en=svg_digit_slots([f"x_{i+1}≥1" for i in range(k_vars)], f"Sum = {n_sum}"),
        )

    for n_items, k_bins, item_lbl in [(7, 3, "identical gold coins"), (8, 4, "identical marbles"), (10, 3, "identical notebooks")]:
        ans = math.comb(n_items + k_bins - 1, k_bins - 1)
        B.add_math(
            tp, "Medium", bp,
            f"In how many ways can {m(n_items)} {item_lbl} be distributed into {m(k_bins)} **distinct** boxes if empty boxes are allowed?",
            f"بكم طريقة يمكن توزيع {m(n_items)} عناصر متماثلة على {m(k_bins)} صناديق **متمايزة** إذا سُمح ببقاء بعض الصناديق فارغة؟",
            ans, [math.comb(n_items - 1, k_bins - 1), k_bins ** n_items if k_bins ** n_items < 5000 else ans + 20, ans - k_bins, math.comb(n_items + k_bins, k_bins)],
            f"Empty boxes mean {m('x_i \\ge 0')}; arrange {m(n_items)} stars and {m(k_bins - 1)} bars!",
            f"السماح بصناديق فارغة يعني {m('x_i \\ge 0')}؛ رتّب {m(n_items)} نجوم و{m(k_bins - 1)} فواصل!",
            f"Use non-negative Stars and Bars {m(f'\\binom{{{n_items} + {k_bins} - 1}}{{{k_bins} - 1}}')}!",
            [
                f"Let {m(f'x_1 + \\cdots + x_{{{k_bins}}} = {n_items}')} with {m('x_i \\ge 0')}.",
                f"Arrange {m(n_items)} stars and {m(k_bins - 1)} bars in {m(f'\\binom{{{n_items + k_bins - 1}}}{{{k_bins - 1}}}')} ways.",
                f"Evaluating gives {m(ans)}.",
            ],
            f"Remember: {m('k^n')} is for **distinct** items, while Stars and Bars is for **identical** items!",
            f"نطبق قانون النجوم والفواصل للحلول غير السالبة {m('\\binom{n + k - 1}{k - 1}')}!",
            [
                f"المسألة تكافئ عدّ حلول {m(f'x_1 + \\cdots + x_{{{k_bins}}} = {n_items}')} مع {m('x_i \\ge 0')}.",
                f"نرتب {m(n_items)} نجوم مع {m(k_bins - 1)} فواصل.",
                f"العدد يساوي {m(f'\\binom{{{n_items + k_bins - 1}}}{{{k_bins - 1}}} = {ans}')}.",
            ],
            f"انتبه: العناصر هنا **متماثلة** وليست متمايزة!",
            diagram_en=svg_digit_slots([f"Box {i+1}" for i in range(k_bins)], f"n={n_items} (empty OK)"),
        )

    for a_lb, b_lb, c_lb, N_tot in [(2, 3, 1, 14), (1, 2, 4, 16), (3, 2, 2, 17)]:
        rem = N_tot - (a_lb + b_lb + c_lb)
        ans = math.comb(rem + 2, 2)
        assert ans == sum(1 for x in range(a_lb, N_tot + 1) for y in range(b_lb, N_tot + 1) if N_tot - x - y >= c_lb)
        B.add_math(
            tp, "Medium", bp,
            f"How many ordered triples {m('(x, y, z)')} of integers satisfy {m(f'x + y + z = {N_tot}')} subject to {m(f'x \\ge {a_lb}')}, {m(f'y \\ge {b_lb}')}, and {m(f'z \\ge {c_lb}')}?",
            f"كم ثلاثية مرتبة {m('(x, y, z)')} من الأعداد الصحيحة تحقق {m(f'x + y + z = {N_tot}')} بشرط {m(f'x \\ge {a_lb}')} و{m(f'y \\ge {b_lb}')} و{m(f'z \\ge {c_lb}')}؟",
            ans, [math.comb(rem - 1, 2), math.comb(N_tot - 1, 2), ans - rem, ans + rem],
            f"Pre-allocate {m(a_lb)}, {m(b_lb)}, and {m(c_lb)} first so the remaining {m(f'{N_tot} - {a_lb+b_lb+c_lb} = {rem}')} units satisfy non-negative Stars and Bars!",
            f"امنح الحدود الدنيا {m(f'{a_lb}, {b_lb}, {c_lb}')} مسبقاً، فيتبقى {m(rem)} وحدة تتوزع بدون قيد ({m('\\ge 0')})!",
            f"Shift variables {m(f'x\' = x - {a_lb},\\; y\' = y - {b_lb},\\; z\' = z - {c_lb} \\ge 0')}!",
            [
                f"Subtract the required minimums: {m(f'x\' + y\' + z\' = {N_tot} - ({a_lb} + {b_lb} + {c_lb}) = {rem}')} with {m('x\', y\', z\' \\ge 0')}.",
                f"Apply non-negative Stars and Bars with {m('k = 3')} variables: {m(f'\\binom{{{rem} + 2}}{{2}}')}.",
                f"Compute {m(f'\\frac{{{rem + 2} \\times {rem + 1}}}{{2}} = {ans}')}.",
            ],
            f"After shifting to {m('\\ge 0')}, be sure to use {m(f'\\binom{{{rem}+2}}{{2}}')}, NOT {m(f'\\binom{{{rem}-1}}{{2}}')}!",
            f"نطرح الحدود الدنيا مسبقاً لتتحول المسألة إلى توزيع {m(rem)} وحدات غير سالبة!",
            [
                f"نضع {m(f'x\' = x - {a_lb},\\; y\' = y - {b_lb},\\; z\' = z - {c_lb} \\ge 0')} فيكون مجموعها {m(rem)}.",
                f"نطبق قانون النجوم والفواصل غير السالب: {m(f'\\binom{{{rem} + 2}}{{2}}')}.",
                f"الناتج: {m(ans)} ثلاثية مرتبة.",
            ],
            f"انتبه: بعد طرح الحدود الدنيا تصبح المتغيرات الجديدة {m('\\ge 0')} لا {m('\\ge 1')}!",
        )

    for N_cap in (8, 10):
        # Positive integers x + y + z <= N_cap -> introduce w = N_cap - (x+y+z) >= 0 -> (x) + (y) + (z) + (w+1) = N_cap + 1 in positive ints -> C(N_cap, 3)!
        ans = math.comb(N_cap, 3)
        assert ans == sum(1 for x in range(1, N_cap) for y in range(1, N_cap) for z in range(1, N_cap) if x + y + z <= N_cap)
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered triples {m('(x, y, z)')} of **positive integers** satisfy the **inequality** {m(f'x + y + z \\le {N_cap}')}?",
            f"كم ثلاثية مرتبة {m('(x, y, z)')} من **الأعداد الصحيحة الموجبة** تحقق **المتباينة** {m(f'x + y + z \\le {N_cap}')}؟",
            ans, [math.comb(N_cap - 1, 2), math.comb(N_cap + 3, 3), math.comb(N_cap - 1, 3), ans + N_cap],
            f"Introduce a fourth slack variable {m(f'w = {N_cap} - (x + y + z) + 1 \\ge 1')} so {m(f'x + y + z + w = {N_cap + 1}')} in positive integers!",
            f"أضف متغيراً رابعاً مكمّلاً {m(f'w = {N_cap + 1} - (x + y + z) \\ge 1')} لتتحول المتباينة إلى معادلة {m(f'x + y + z + w = {N_cap + 1}')}!",
            f"Turn the inequality into an equality using a slack variable!",
            [
                f"Let {m(f's = {N_cap} - (x + y + z) \\ge 0')}, and set {m('w = s + 1 \\ge 1')}.",
                f"Then {m('(x, y, z, w)')} is a {m(4)}-tuple of **positive** integers summing to {m(N_cap + 1)}.",
                f"By Stars and Bars, there are {m(f'\\binom{{({N_cap + 1}) - 1}}{{4 - 1}} = \\binom{{{N_cap}}}{{3}} = {ans}')} triples.",
            ],
            f"Hockey-stick check: {m(f'\\sum_{{k=3}}^{{{N_cap}}} \\binom{{k-1}}{{2}} = \\binom{{{N_cap}}}{{3}} = {ans}')}!",
            f"نحوّل المتباينة إلى معادلة بإدخال متغير فائض رابع!",
            [
                f"نضع {m(f'w = {N_cap + 1} - (x + y + z) \\ge 1')} فتصبح المعادلة {m(f'x + y + z + w = {N_cap + 1}')} في الأعداد الموجبة.",
                f"عدد الحلول الموجبة لأربعة متغيرات مجموعها {m(N_cap + 1)} هو {m(f'\\binom{{{N_cap}}}{{3}}')}.",
                f"بحساب التوافيق نحصل على {m(ans)}.",
            ],
            f"تحقق بمتطابقة عصا الهوكي: مجموع {m('\\binom{k-1}{2}')} من {m('k=3')} إلى {m(N_cap)} يساوي {m(ans)}!",
        )

    for N_tot, U_cap in [(10, 5), (12, 6)]:
        tot = math.comb(N_tot + 2, 2)
        over = 3 * math.comb(N_tot - (U_cap + 1) + 2, 2)
        ans = tot - over
        assert ans == sum(1 for x in range(U_cap + 1) for y in range(U_cap + 1) for z in range(U_cap + 1) if x + y + z == N_tot)
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered triples {m('(x, y, z)')} of integers satisfy {m(f'x + y + z = {N_tot}')} with {m(f'0 \\le x, y, z \\le {U_cap}')}?",
            f"كم ثلاثية مرتبة {m('(x, y, z)')} من الأعداد الصحيحة تحقق {m(f'x + y + z = {N_tot}')} بشرط {m(f'0 \\le x, y, z \\le {U_cap}')}؟",
            ans, [tot, tot - math.comb(N_tot - (U_cap + 1) + 2, 2), ans + 3, ans - 3],
            f"Start with all {m(f'\\binom{{{N_tot}+2}}{{2}} = {tot}')} non-negative triples and subtract those where a variable is {m(f'\\ge {U_cap + 1}')}!",
            f"ابدأ بجميع الثلاثيات غير السالبة ({m(tot)}) واطرح الحالات التي يتجاوز فيها أحد المتغيرات السقف ({m(f'\\ge {U_cap + 1}')})!",
            f"Combine Stars and Bars with Inclusion–Exclusion on the upper bound {m(f'x_i \\ge {U_cap + 1}')}!",
            [
                f"Without the upper cap, non-negative triples total {m(f'\\binom{{{N_tot} + 2}}{{2}} = {tot}')}.",
                f"If {m(f'x \\ge {U_cap + 1}')}, shifting {m(f'x\' = x - {U_cap + 1}')} leaves sum {m(N_tot - U_cap - 1)}, giving {m(f'\\binom{{{N_tot - U_cap + 1}}}{{2}} = {over // 3}')} bad triples (and similarly for {m('y')} and {m('z')}).",
                f"Since {m(f'2({U_cap + 1}) = {2*(U_cap+1)} > {N_tot}')}, two variables cannot exceed {m(U_cap)} at once, so {m(f'{tot} - 3 \\times {over // 3} = {ans}')}.",
            ],
            f"Multiplying by {m(3)} (for {m('x')}, {m('y')}, or {m('z')} violating the cap) is essential!",
            f"ندمج النجوم والفواصل مع التضمين والإقصاء لاستبعاد الحالات التي تتجاوز {m(U_cap)}!",
            [
                f"إجمالي الحلول غير السالبة هو {m(f'\\binom{{{N_tot + 2}}}{{2}} = {tot}')}.",
                f"تجاوز متغير واحد (أي {m(f'\\ge {U_cap + 1}')}) يعطي {m(over // 3)} حلاً مرفوضاً لكل من المتغيرات الثلاثة، ويستحيل تجاوز متغيرين معاً لأن {m(f'{2*(U_cap+1)} > {N_tot}')}.",
                f"إذن العدد الصافي هو {m(f'{tot} - 3 \\times {over // 3} = {ans}')}.",
            ],
            f"انتبه لضرب الحالات المرفوضة في {m(3)} لأن التجاوز قد يقع في {m('x')} أو {m('y')} أو {m('z')}!",
            diagram_en=svg_digit_slots([f"0..{U_cap}"] * 3, f"Sum = {N_tot}"),
        )

    # 3. nsmo_g89_three_set_inclusion_exclusion (5E, 6M, 4H) — SVG: svg_venn_3
    bp = "nsmo_g89_three_set_inclusion_exclusion"
    easy_venn = [
        (18, 15, 12, 8, 6, 5, 4, 80, "union"),
        (20, 16, 14, 9, 7, 6, 5, 90, "union"),
        (24, 19, 17, 10, 8, 7, 6, 100, "union"),
        (15, 14, 11, 7, 5, 4, 3, 75, "none"),
        (22, 18, 15, 9, 6, 5, 4, 95, "none"),
    ]
    for ra, rb, rc, rab, rbc, rac, rabc, n_all, mode in easy_venn:
        A = ra + rab + rac + rabc
        Bc = rb + rab + rbc + rabc
        C = rc + rac + rbc + rabc
        AB, BC, AC = rab + rabc, rbc + rabc, rac + rabc
        union_v = ra + rb + rc + rab + rbc + rac + rabc
        ans = union_v if mode == "union" else (n_all - union_v)
        ask_en = "participate in **at least one** of the three clubs" if mode == "union" else "participate in **none** of the three clubs"
        ask_ar = "يشاركون في **نادٍ واحد على الأقل**" if mode == "union" else "لا يشاركون في **أيٍّ** من الأندية الثلاثة"
        B.add_math(
            tp, "Easy", bp,
            f"Among {m(n_all)} students, {m(A)} join Math, {m(Bc)} join Coding, {m(C)} join Robotics, {m(AB)} join both Math and Coding, {m(BC)} join both Coding and Robotics, {m(AC)} join both Math and Robotics, and {m(rabc)} join all three. How many students {ask_en}?",
            f"من بين {m(n_all)} طالباً، انضم {m(A)} لنادي الرياضيات، و{m(Bc)} للبرمجة، و{m(C)} للروبوت، وانضم {m(AB)} للرياضيات والبرمجة معاً، و{m(BC)} للبرمجة والروبوت معاً، و{m(AC)} للرياضيات والروبوت معاً، و{m(rabc)} للأندية الثلاثة جميعاً. كم طالباً {ask_ar}؟",
            ans, [union_v - rabc if mode == "union" else union_v, union_v + rabc if mode == "union" else ans + rabc, ans + 4, max(1, ans - 4)],
            f"Compute {m('|M \\cup C \\cup R| = (|M|+|C|+|R|) - (|M\\cap C|+|C\\cap R|+|M\\cap R|) + |M\\cap C\\cap R|')}.",
            f"احسب اتحاد المجموعات الثلاث بقانون التضمين والإقصاء الثلاثي.",
            f"Apply three-set Inclusion–Exclusion{' and subtract from ' + str(n_all) if mode == 'none' else ''}!",
            [
                f"Singles sum: {m(f'{A} + {Bc} + {C} = {A+Bc+C}')}; pairwise sum: {m(f'{AB} + {BC} + {AC} = {AB+BC+AC}')}.",
                f"Union {m(f'= {A+Bc+C} - {AB+BC+AC} + {rabc} = {union_v}')}.",
                f"{'Thus ' + m(str(ans)) + ' join at least one club.' if mode == 'union' else 'Subtract from ' + m(str(n_all)) + ': ' + m(f'{n_all} - {union_v} = {ans}') + '.'}",
            ],
            f"All {m(7)} disjoint Venn regions are positive and sum to {m(union_v)}!",
            f"نطبق قانون التضمين والإقصاء الثلاثي{' ثم نطرح الناتج من ' + str(n_all) if mode == 'none' else ''}!",
            [
                f"مجموع الفرديات {m(A+Bc+C)} ومجموع التقاطعات الثنائية {m(AB+BC+AC)}.",
                f"الاتحاد يساوي {m(f'{A+Bc+C} - {AB+BC+AC} + {rabc} = {union_v}')}.",
                f"{'إذن الجواب هو ' + m(str(ans)) if mode == 'union' else 'الباقون خارج الأندية: ' + m(f'{n_all} - {union_v} = {ans}')}.",
            ],
            f"تحقق: مجموع المناطق السبع المنفصلة في مخطط فن يساوي {m(union_v)}.",
            diagram_en=svg_venn_3("M", "C", "R", {"a": str(ra), "b": str(rb), "c": str(rc), "ab": str(rab), "bc": str(rbc), "ac": str(rac), "abc": str(rabc)}),
        )

    for ra, rb, rc, rab, rbc, rac, rabc in [(16, 14, 12, 7, 6, 5, 5), (20, 18, 15, 9, 8, 6, 7), (19, 15, 13, 8, 7, 6, 9)]:
        A = ra + rab + rac + rabc
        Bc = rb + rab + rbc + rabc
        C = rc + rac + rbc + rabc
        AB, BC, AC = rab + rabc, rbc + rabc, rac + rabc
        union_v = ra + rb + rc + rab + rbc + rac + rabc
        B.add_math(
            tp, "Medium", bp,
            f"Every one of {m(union_v)} delegates speaks Arabic, English, or French: {m(A)} speak Arabic, {m(Bc)} speak English, {m(C)} speak French, {m(AB)} speak both Arabic and English, {m(BC)} speak both English and French, and {m(AC)} speak both Arabic and French. How many delegates speak **all three** languages?",
            f"يتحدث كل فرد من بين {m(union_v)} مندوباً لغةً واحدة على الأقل من العربية أو الإنجليزية أو الفرنسية: {m(A)} يتحدثون العربية، و{m(Bc)} الإنجليزية، و{m(C)} الفرنسية، و{m(AB)} العربية والإنجليزية معاً، و{m(BC)} الإنجليزية والفرنسية معاً، و{m(AC)} العربية والفرنسية معاً. كم مندوباً يتحدث اللغات **الثلاث جميعاً**؟",
            rabc, [rabc + 3, max(1, rabc - 2), rabc * 2, rab + rbc],
            f"Plug {m('x = |A \\cap E \\cap F|')} into {m(f'{union_v} = ({A}+{Bc}+{C}) - ({AB}+{BC}+{AC}) + x')}!",
            f"عوّض عن التقاطع الثلاثي {m('x')} في معادلة الاتحاد {m(f'{union_v} = ({A}+{Bc}+{C}) - ({AB}+{BC}+{AC}) + x')}!",
            f"Solve the three-set Inclusion–Exclusion equation backwards for {m('|A \\cap E \\cap F|')}!",
            [
                f"Write {m(f'{union_v} = ({A} + {Bc} + {C}) - ({AB} + {BC} + {AC}) + |A \\cap E \\cap F|')}.",
                f"Simplify: {m(f'{union_v} = {A+Bc+C} - {AB+BC+AC} + |A \\cap E \\cap F| = {union_v - rabc} + |A \\cap E \\cap F|')}.",
                f"Solve: {m(f'|A \\cap E \\cap F| = {union_v} - {union_v - rabc} = {rabc}')}.",
            ],
            f"Check: {m(f'{A+Bc+C} - {AB+BC+AC} + {rabc} = {union_v}')}!",
            f"نعوّض بالقيم المعلومة في قانون الاتحاد ونعزل التقاطع الثلاثي!",
            [
                f"لدينا {m(f'{union_v} = {A+Bc+C} - {AB+BC+AC} + x')}.",
                f"نبسّط الطرف الأيمن: {m(f'{union_v} = {union_v - rabc} + x')}.",
                f"إذن عدد المتحدثين باللغات الثلاث هو {m(f'x = {rabc}')}.",
            ],
            f"تحقق: جميع المناطق الفرعية موجبة ومجموعها {m(union_v)}.",
            diagram_en=svg_venn_3("Ar", "En", "Fr", {"a": str(ra), "b": str(rb), "c": str(rc), "ab": str(rab), "bc": str(rbc), "ac": str(rac), "abc": "?"}),
        )

    for ra, rb, rc, rab, rbc, rac, rabc in [(14, 12, 10, 9, 7, 5, 4), (18, 15, 13, 11, 8, 6, 5), (21, 17, 14, 10, 9, 8, 6)]:
        AB, BC, AC = rab + rabc, rbc + rabc, rac + rabc
        ans = rab + rbc + rac
        assert ans == (AB + BC + AC) - 3 * rabc
        B.add_math(
            tp, "Medium", bp,
            f"In a survey on three apps {m('A, B, C')}, {m(AB)} users have both {m('A')} and {m('B')}, {m(BC)} have both {m('B')} and {m('C')}, {m(AC)} have both {m('A')} and {m('C')}, and {m(rabc)} have all three apps. How many users have **exact two** of the three apps?",
            f"في استبيان حول ثلاثة تطبيقات {m('A, B, C')}، يستخدم {m(AB)} شخصاً {m('A')} و{m('B')} معاً، و{m(BC)} يستخدمون {m('B')} و{m('C')} معاً، و{m(AC)} يستخدمون {m('A')} و{m('C')} معاً، بينما يستخدم {m(rabc)} التطبيقات الثلاثة جميعاً. كم شخصاً يستخدم **تطبيقين فقط بالضبط**؟",
            ans, [(AB + BC + AC) - rabc, (AB + BC + AC) - 2 * rabc, AB + BC + AC, ans + rabc],
            f"Each of {m('|A \\cap B|')}, {m('|B \\cap C|')}, and {m('|A \\cap C|')} includes {m('|A \\cap B \\cap C|')} once — so subtract {m(f'3 \\times {rabc}')}!",
            f"كل تقاطع ثنائي يشمل التقاطع الثلاثي داخله، لذا يجب طرح {m(f'3 \\times {rabc}')} وليس {m(rabc)} واحدة!",
            f"Peel the center region from each of the three petals: subtract {m('3 |A \\cap B \\cap C|')}!",
            [
                f"Users with {m('A')} and {m('B')} **only**: {m(f'{AB} - {rabc} = {rab}')}.",
                f"Users with {m('B')} and {m('C')} **only**: {m(f'{BC} - {rabc} = {rbc}')}; {m('A')} and {m('C')} **only**: {m(f'{AC} - {rabc} = {rac}')}.",
                f"Total with exact two apps: {m(f'{rab} + {rbc} + {rac} = {ans}')} (equivalently {m(f'({AB}+{BC}+{AC}) - 3({rabc}) = {ans}')}).",
            ],
            f"Subtracting {m(rabc)} once ({m(AB+BC+AC - rabc)}) or twice ({m(AB+BC+AC - 2*rabc)}) are classic Olympiad traps — 'exact two' subtracts {m('3\\times')}!",
            f"نطرح التقاطع الثلاثي من كل تقاطع ثنائي على حدة (أي نطرح {m(f'3 \\times {rabc}')})!",
            [
                f"منطقة {m('A, B')} فقط تساوي {m(rab)}، ومنطقة {m('B, C')} فقط تساوي {m(rbc)}، ومنطقة {m('A, C')} فقط تساوي {m(rac)}.",
                f"بجمع المناطق الثلاث نحصل على {m(f'{rab} + {rbc} + {rac} = {ans}')}.",
                f"ويكافئ ذلك {m(f'({AB} + {BC} + {AC}) - 3 \\times {rabc} = {ans}')}.",
            ],
            f"انتبه: عبارة «تطبيقين على الأقل» تطرح {m('2\\times')}، أما «تطبيقين بالضبط» فتطرح {m('3\\times')}!",
            diagram_en=svg_venn_3("A", "B", "C", {"a": "", "b": "", "c": "", "ab": str(rab), "bc": str(rbc), "ac": str(rac), "abc": str(rabc)}),
        )

    for N_cap, p1, p2, p3 in [(210, 3, 5, 7), (280, 2, 5, 7)]:
        ans = sum(1 for k in range(1, N_cap + 1) if k % p1 == 0 or k % p2 == 0 or k % p3 == 0)
        s1 = N_cap // p1 + N_cap // p2 + N_cap // p3
        s2 = N_cap // (p1 * p2) + N_cap // (p2 * p3) + N_cap // (p1 * p3)
        s3 = N_cap // (p1 * p2 * p3)
        assert ans == s1 - s2 + s3
        B.add_math(
            tp, "Hard", bp,
            f"How many integers in {m(f'\\{{1, 2, \\dots, {N_cap}\\}}')} are divisible by **at least one** of {m(p1)}, {m(p2)}, or {m(p3)}?",
            f"كم عدداً صحيحاً في المجموعة {m(f'\\{{1, 2, \\dots, {N_cap}\\}}')} يقبل القسمة على **واحد على الأقل** من الأعداد {m(p1)} أو {m(p2)} أو {m(p3)}؟",
            ans, [N_cap - ans, s1 - s2, ans - s3, s1],
            f"Apply 3-set Inclusion–Exclusion using floor quotients for singles, pairwise products, and {m(p1 * p2 * p3)}.",
            f"طبّق التضمين والإقصاء الثلاثي بقسمة {m(N_cap)} على الأعداد المفردة ثم المثناة ثم جدائها الثلاثي {m(p1*p2*p3)}.",
            f"Use {m('|A \\cup B \\cup C| = S_1 - S_2 + S_3')} on multiples up to {m(N_cap)}!",
            [
                f"Singles: {m(f'{N_cap}//{p1} + {N_cap}//{p2} + {N_cap}//{p3} = {s1}')}.",
                f"Pairs: {m(f'{N_cap}//{p1*p2} + {N_cap}//{p2*p3} + {N_cap}//{p1*p3} = {s2}')}; triple: {m(f'{N_cap}//{p1*p2*p3} = {s3}')}.",
                f"By Inclusion–Exclusion, {m(f'{s1} - {s2} + {s3} = {ans}')}.",
            ],
            f"Complement check: integers divisible by **none** equal {m(f'{N_cap} - {ans} = {N_cap - ans}')}!",
            f"نطبق قانون التضمين والإقصاء على مضاعفات {m(f'{p1}, {p2}, {p3}')} حتى {m(N_cap)}!",
            [
                f"مجموع المضاعفات المفردة {m(s1)}، ومجموع المثناة {m(s2)}، والمضاعفات الثلاثية المشتركة {m(s3)}.",
                f"نحسب الاتحاد: {m(f'{s1} - {s2} + {s3} = {ans}')}.",
                f"إذن يوجد {m(ans)} عدداً يقبل القسمة على أحدها على الأقل.",
            ],
            f"انتبه: العدد المكمل {m(N_cap - ans)} يمثل الأعداد التي لا تقبل القسمة على أيٍّ منها!",
        )

    for N_cap, a_d, b_d, c_no in [(300, 3, 4, 5), (210, 2, 3, 7)]:
        ans = sum(1 for k in range(1, N_cap + 1) if (k % a_d == 0 or k % b_d == 0) and k % c_no != 0)
        ab_union = N_cap // a_d + N_cap // b_d - N_cap // math.lcm(a_d, b_d)
        in_c = N_cap // (a_d * c_no) + N_cap // (b_d * c_no) - N_cap // (math.lcm(a_d, b_d) * c_no)
        assert ans == ab_union - in_c
        B.add_math(
            tp, "Hard", bp,
            f"How many integers in {m(f'\\{{1, 2, \\dots, {N_cap}\\}}')} are divisible by {m(a_d)} or {m(b_d)}, **but NOT** divisible by {m(c_no)}?",
            f"كم عدداً صحيحاً في المجموعة {m(f'\\{{1, 2, \\dots, {N_cap}\\}}')} يقبل القسمة على {m(a_d)} أو {m(b_d)}، **ولا يقبل** القسمة على {m(c_no)}؟",
            ans, [ab_union - N_cap // c_no, ab_union, ans + N_cap // (math.lcm(a_d, b_d) * c_no), ans - 5],
            f"First count {m('|A \\cup B|')}, then remove the fraction {m(f'1/{c_no}')} of those multiples that are also divisible by {m(c_no)}!",
            f"احسب أولاً اتحاد مضاعفات {m(a_d)} و{m(b_d)}، ثم استبعد منها الأعداد التي تقبل القسمة على {m(c_no)}!",
            f"Compute {m(f'|M_{{{a_d}}} \\cup M_{{{b_d}}}| = {ab_union}')}, and multiply by {m(f'\\left(1 - \\frac{{1}}{{{c_no}}}\\right)')} since {m(c_no)} is coprime to {m(a_d)} and {m(b_d)}!",
            [
                f"Multiples of {m(a_d)} or {m(b_d)}: {m(f'{N_cap}//{a_d} + {N_cap}//{b_d} - {N_cap}//{math.lcm(a_d, b_d)} = {ab_union}')}.",
                f"Among those, multiples also divisible by {m(c_no)} total {m(f'{N_cap}//{a_d*c_no} + {N_cap}//{b_d*c_no} - {N_cap}//{math.lcm(a_d,b_d)*c_no} = {in_c}')}.",
                f"Subtracting gives {m(f'{ab_union} - {in_c} = {ans}')}.",
            ],
            f"Never subtract all {m(N_cap // c_no)} multiples of {m(c_no)} — subtract only those **inside** {m('A \\cup B')} ({m(in_c)})!",
            f"نحسب اتحاد مضاعفات {m(a_d)} و{m(b_d)} ثم نطرح منه ما يقبل القسمة على {m(c_no)} فقط!",
            [
                f"عدد مضاعفات {m(a_d)} أو {m(b_d)} هو {m(ab_union)}.",
                f"عدد ما يقبل القسمة على {m(c_no)} من داخل هذا الاتحاد هو {m(in_c)}.",
                f"الباقي الصافي يساوي {m(f'{ab_union} - {in_c} = {ans}')}.",
            ],
            f"انتبه من فخ طرح جميع مضاعفات {m(c_no)} ({m(N_cap // c_no)}) بدلاً من تقاطعها مع الاتحاد ({m(in_c)})!",
        )

    # 4. nsmo_g89_handshake_tournament_graphs (5E, 6M, 4H) — SVG: svg_graph_cycle_chords / svg_round_table
    bp = "nsmo_g89_handshake_tournament_graphs"
    for n_p in (9, 11, 14):
        ans = n_p * (n_p - 1) // 2
        B.add_math(
            tp, "Easy", bp,
            f"In a chess championship, each of the {m(n_p)} finalists plays exact one game against every other finalist. How many games are played in total?",
            f"في بطولة شطرنج، يلعب كل متأهل من الـ {m(n_p)} متأهلين مباراة واحدة بالضبط مع كل متأهل آخر. كم مباراة تُلعب في المجموع؟",
            ans, [n_p * (n_p - 1), n_p * (n_p - 2) // 2, ans - n_p, ans + n_p],
            f"Divide {m(f'{n_p} \\times {n_p - 1}')} by {m(2)} because each game involves two players.",
            f"اقسم {m(f'{n_p} \\times {n_p - 1}')} على {m(2)} لأن كل مباراة تجمع لاعبين اثنين.",
            f"Count unordered pairs {m(f'\\binom{{{n_p}}}{{2}} = \\frac{{{n_p}({n_p - 1})}}{{2}}')}!",
            [
                f"Each of the {m(n_p)} players plays {m(n_p - 1)} opponents.",
                f"Dividing {m(f'{n_p} \\times {n_p - 1}')} by {m(2)} removes double-counting.",
                f"Total games: {m(ans)}.",
            ],
            f"Forgetting to divide by {m(2)} gives the classic trap {m(n_p * (n_p - 1))}!",
            f"نحسب عدد الأزواج غير المرتبة {m(f'\\binom{{{n_p}}}{{2}}')}!",
            [
                f"يلعب كل لاعب {m(n_p - 1)} مباراة.",
                f"نقسم {m(f'{n_p} \\times {n_p - 1}')} على {m(2)} لمنع عدّ كل مباراة مرتين.",
                f"الناتج: {m(ans)} مباراة.",
            ],
            f"انتبه لقسمة حاصل الضرب على {m(2)} دائماً!",
            diagram_en=svg_graph_cycle_chords(min(n_p, 7), full_kn=True),
        )

    for games, n_ans in [(66, 12), (105, 15)]:
        assert n_ans * (n_ans - 1) // 2 == games
        B.add_math(
            tp, "Easy", bp,
            f"At a Mawhiba alumni banquet, every guest shook hands exact once with every other guest, resulting in {m(games)} handshakes altogether. How many guests attended?",
            f"في لقاء خريجي موهبة، صافح كل حاضر جميع الحاضرين الآخرين مرة واحدة بالضبط، فبلغ مجموع المصافحات {m(games)} مصافحة. كم شخصاً حضر اللقاء؟",
            n_ans, [n_ans - 1, n_ans + 1, games // 2, n_ans + 2],
            f"Solve {m(f'n(n - 1) = {2 * games}')} by finding two consecutive integers multiplying to {m(2 * games)}!",
            f"حل المعادلة {m(f'n(n - 1) = {2 * games}')} بالبحث عن عددين متتاليين حاصل ضربهما {m(2 * games)}!",
            f"Double {m(games)} to {m(2 * games)} and spot consecutive factors {m(f'{n_ans} \\times {n_ans - 1}')}!",
            [
                f"From {m(f'\\frac{{n(n - 1)}}{{2}} = {games}')}, we get {m(f'n(n - 1) = {2 * games}')}.",
                f"Since {m(f'{n_ans} \\times {n_ans - 1} = {2 * games}')}, the larger factor is {m(f'n = {n_ans}')}.",
                f"Thus {m(n_ans)} guests attended.",
            ],
            f"Be careful to pick {m(n_ans)} (which is {m('n')}), not {m(n_ans - 1)} (which is {m('n - 1')})!",
            f"نضاعف عدد المصافحات إلى {m(2 * games)} ونبحث عن عددين متتاليين حاصل ضربهما {m(2 * games)}!",
            [
                f"من {m(f'n(n - 1) = {2 * games}')} نبحث عن عاملين متتاليين.",
                f"نجد {m(f'{n_ans} \\times {n_ans - 1} = {2 * games}')}.",
                f"إذن عدد الحضور هو العامل الأكبر {m(f'n = {n_ans}')}.",
            ],
            f"انتبه لاختيار {m('n = ' + str(n_ans))} وليس {m('n - 1 = ' + str(n_ans - 1))}!",
            diagram_en=svg_round_table(6),
        )

    for n_v, deg_k in [(10, 4), (12, 5), (14, 3)]:
        ans = (n_v * deg_k) // 2
        B.add_math(
            tp, "Medium", bp,
            f"A communication network has {m(n_v)} servers, and every server is directly wired to exact {m(deg_k)} other servers. How many direct cables are in the network?",
            f"تضم شبكة اتصالات {m(n_v)} خادماً، وكل خادم متصل مباشرة بـ {m(deg_k)} خوادم أخرى بالضبط. كم كابلاً مباشراً يوجد في الشبكة؟",
            ans, [n_v * deg_k, ans + n_v, ans - deg_k, n_v * (n_v - 1) // 2],
            f"By the Handshake Lemma, the sum of degrees {m(f'{n_v} \\times {deg_k}')} equals **twice** the number of edges!",
            f"بحسب مبرهنة المصافحات، مجموع الدرجات {m(f'{n_v} \\times {deg_k}')} يساوي **ضعفي** عدد الكابلات!",
            f"Apply the Handshake Lemma {m('|E| = \\frac{1}{2} \\sum d_i')}!",
            [
                f"Summing connections across all {m(n_v)} servers gives {m(f'{n_v} \\times {deg_k} = {n_v * deg_k}')} cable-ends.",
                f"Every cable has {m(2)} ends, so divide by {m(2)}.",
                f"Total cables: {m(f'{n_v * deg_k} / 2 = {ans}')}.",
            ],
            f"Degree-sum parity note: {m(n_v * deg_k)} is even, as required by the Handshake Lemma!",
            f"نطبق مبرهنة المصافحات بقسمة مجموع الدرجات على {m(2)}!",
            [
                f"مجموع أطراف التوصيل يساوي {m(f'{n_v} \\times {deg_k} = {n_v * deg_k}')}.",
                f"بما أن لكل كابل طرفين، نقسم على {m(2)}.",
                f"عدد الكابلات يساوي {m(ans)}.",
            ],
            f"تحقق: ضرب {m(n_v)} في {m(deg_k)} دون قسمة يحسب كل كابل مرتين!",
            diagram_en=svg_graph_cycle_chords(6, full_kn=False),
        )

    for m_couples in (6, 8, 10):
        n_tot = 2 * m_couples
        ans = n_tot * (n_tot - 1) // 2 - m_couples
        assert ans == 2 * m_couples * (m_couples - 1)
        B.add_math(
            tp, "Medium", bp,
            f"{m(m_couples)} two-person debate teams ({m(n_tot)} students in total) meet before a round. Every student shakes hands once with every student from **other** teams, but teammates do not shake hands with each other. How many handshakes occur?",
            f"التقى {m(m_couples)} فرق مناظرة ثنائية (إجمالي {m(n_tot)} طالباً). صافح كل طالب جميع طلاب الفرق **الأخرى** مرة واحدة، ولم يتصافح زميلا الفريق الواحد. كم مصافحة جرت؟",
            ans, [n_tot * (n_tot - 1) // 2, m_couples * (m_couples - 1) // 2, ans - m_couples, 2 * ans],
            f"Subtract the {m(m_couples)} forbidden teammate pairs from all {m(f'\\binom{{{n_tot}}}{{2}}')} pairs (or note each of the {m(n_tot)} students shakes {m(n_tot - 2)} hands)!",
            f"اطرح الـ {m(m_couples)} أزواج الزملاء من إجمالي الأزواج {m(f'\\binom{{{n_tot}}}{{2}}')}، أو اضرب {m(n_tot)} في {m(n_tot - 2)} واقسم على {m(2)}!",
            f"Compute {m(f'\\binom{{{n_tot}}}{{2}} - {m_couples}')} (equivalently {m(f'\\frac{{{n_tot} \\times {n_tot - 2}}}{{2}}')})!",
            [
                f"Each of the {m(n_tot)} students shakes hands with everyone except themselves and their {m(1)} teammate: {m(n_tot - 2)} handshakes each.",
                f"Divide {m(f'{n_tot} \\times {n_tot - 2}')} by {m(2)}: {m(f'\\frac{{{n_tot} \\times {n_tot - 2}}}{{2}} = {ans}')}.",
                f"Same answer via complement: {m(f'\\binom{{{n_tot}}}{{2}} - {m_couples} = {n_tot*(n_tot-1)//2} - {m_couples} = {ans}')}.",
            ],
            f"Two independent derivations both give {m(ans)}!",
            f"نحسب {m(f'\\binom{{{n_tot}}}{{2}} - {m_couples}')} بطرح أزواج الزملاء من جميع المصافحات الممكنة!",
            [
                f"إجمالي المصافحات لو تصافح الجميع هو {m(f'\\binom{{{n_tot}}}{{2}} = {n_tot*(n_tot-1)//2}')}.",
                f"نطرح {m(m_couples)} زوجاً يمثلون زملاء الفرق الثنائية.",
                f"الناتج: {m(ans)} مصافحة.",
            ],
            f"تحقق آخر: يصافح كل طالب {m(n_tot - 2)} شخصاً، فنجد {m(f'{n_tot} \\times {n_tot - 2} \\div 2 = {ans}')}.",
            diagram_en=svg_graph_cycle_chords(6, full_kn=True),
        )

    for m_other in (4, 6):
        # Mr. & Mrs. Salman + m_other couples -> 2*m_other + 2 people total; Mr. Salman gets 2*m_other + 1 distinct answers 0..2*m_other -> Mrs. Salman shook m_other hands!
        tot_couples = m_other + 1
        B.add_math(
            tp, "Hard", bp,
            f"Mr. and Mrs. Salman attend a dinner with {m(m_other)} other married couples ({m(2 * tot_couples)} people in total). Some handshakes take place; nobody shakes hands with themselves or with their own spouse. Afterward, Mr. Salman asks all other {m(2 * m_other + 1)} people (including his wife) how many hands they shook, and receives {m(2 * m_other + 1)} **all different** answers! How many hands did **Mrs. Salman** shake?",
            f"حضر السيد والسيدة سلمان مأدبة عشاء مع {m(m_other)} أزواج آخرين (إجمالي {m(2 * tot_couples)} شخصاً). جرت بعض المصافحات بحيث لم يصافح أحد نفسه ولا زوجه. سأل السيد سلمان الـ {m(2 * m_other + 1)} أشخاص الآخرين (بمن فيهم زوجته) عن عدد من صافحوهم، فحصل على {m(2 * m_other + 1)} إجابات **مختلفة جميعاً**! كم شخصاً صافحت **السيدة سلمان**؟",
            m_other, [m_other - 1, m_other + 1, 2 * m_other, 0],
            f"The {m(2 * m_other + 1)} distinct answers must be {m(f'0, 1, 2, \\dots, {2 * m_other}')}! Pair the person with {m(2 * m_other)} handshakes against the person with {m(0)} — they MUST be spouses!",
            f"الإجابات المختلفة لا بد أن تكون {m(f'0, 1, \\dots, {2 * m_other}')}! الشخص الذي صافح {m(2 * m_other)} أشخاص لا بد أن يكون زوج الشخص الذي صافح {m(0)}!",
            f"Peel extreme degree pairs {m(f'({2*m_other}, 0), ({2*m_other - 1}, 1), \\dots')} as married couples until only the middle number {m(m_other)} remains!",
            [
                f"Maximum possible handshakes for anyone is {m(2 * m_other)}, so the {m(2 * m_other + 1)} distinct answers are {m(f'0, 1, \\dots, {2 * m_other}')}.",
                f"The person {m('P_{' + str(2*m_other) + '}')} shook hands with everyone except their spouse, so **only** their spouse can have degree {m(0)}! Neither is Mrs. Salman because {m('P_{' + str(2*m_other) + '}')} shook Mr. Salman's hand.",
                f"Removing that couple and repeating on {m(f'({2*m_other - 1}, 1), \\dots, ({m_other + 1}, {m_other - 1})')} leaves the unpaired middle value {m(m_other)} for Mrs. Salman!",
            ],
            f"Halmos's handshake invariant: in {m('C')} total couples, the host's spouse always shakes {m('C - 1')} hands!",
            f"الإجابات هي {m(f'0, 1, \\dots, {2*m_other}')}؛ وبمزاوجة الطرفين كأزواج متتالية يتبقى العدد الأوسط {m(m_other)} للسيدة سلمان!",
            [
                f"أقصى عدد مصافحات ممكن لأي شخص هو {m(2 * m_other)}، لذا الإجابات هي {m(f'0, 1, \\dots, {2 * m_other}')}.",
                f"صاحب الدرجة {m(2 * m_other)} صافح الجميع عدا زوجه، فيكون زوجه حتماً هو صاحب الدرجة {m(0)}، وهكذا تتزاوج {m(f'({2*m_other - 1}, 1)')} تباعاً.",
                f"القيمة الوحيدة غير المتزاوجة في المنتصف هي {m(m_other)} وهي عدد مصافحات السيدة سلمان.",
            ],
            f"نتيجة أولمبية شهيرة: في وجود {m(tot_couples)} أزواج، تصافح زوجة السائل دائماً {m(m_other)} أشخاص!",
        )

    for k_drop, G_tot, m_rem in [(3, 48, 10), (4, 82, 13)]:
        assert m_rem * (m_rem - 1) // 2 + k_drop == G_tot
        ans = m_rem + 1
        B.add_math(
            tp, "Hard", bp,
            f"In a round-robin tournament where every pair of entrants was scheduled to play once, one player fell ill after playing exact {m(k_drop)} games and withdrew. All remaining players completed every scheduled game among themselves, and {m(G_tot)} games were played in total. How many players **originally** entered the tournament?",
            f"في بطولة دورية يلعب فيها كل متسابقين مباراة واحدة، انسحب أحد اللاعبين بعد أن لعب {m(k_drop)} مباريات فقط، بينما أكمل بقية اللاعبين جميع مبارياتهم البينية، فبلغ إجمالي المباريات الملعوبة {m(G_tot)} مباراة. كم لاعباً **بدأ** البطولة في الأصل؟",
            ans, [m_rem, ans + 1, ans - 2, m_rem + 2],
            f"Let {m('m')} be the number of **remaining** players: {m(f'\\binom{{m}}{{2}} + {k_drop} = {G_tot}')}, then remember to add {m(1)} for the withdrawn player!",
            f"افرض عدد اللاعبين **المكملين** {m('m')} فتحصل على {m(f'\\binom{{m}}{{2}} + {k_drop} = {G_tot}')}، ولا تنسَ إضافة {m(1)} للاعب المنسحب!",
            f"Solve {m(f'\\binom{{m}}{{2}} = {G_tot} - {k_drop} = {G_tot - k_drop}')} and return {m('m + 1')}!",
            [
                f"Let {m('m')} players finish the tournament; they played {m('\\binom{m}{2}')} games among themselves.",
                f"Adding the withdrawn player's {m(k_drop)} games gives {m(f'\\binom{{m}}{{2}} = {G_tot} - {k_drop} = {G_tot - k_drop} \\implies m(m - 1) = {2*(G_tot - k_drop)}')}, so {m(f'm = {m_rem}')}.",
                f"Including the player who withdrew, {m(f'm + 1 = {m_rem} + 1 = {ans}')} players originally entered.",
            ],
            f"Classic final-step trap: {m(m_rem)} is {m('m')} (finishers), whereas the question asks for original entrants ({m(ans)})!",
            f"نحل {m(f'\\binom{{m}}{{2}} = {G_tot - k_drop}')} لإيجاد اللاعبين المكملين ثم نضيف {m(1)} للاعب المنسحب!",
            [
                f"عدد المباريات بين الـ {m('m')} لاعبين المكملين يساوي {m(f'{G_tot} - {k_drop} = {G_tot - k_drop}')}.",
                f"من {m(f'm(m - 1) = {2*(G_tot - k_drop)}')} نجد {m(f'm = {m_rem}')}.",
                f"إجمالي المشاركين الأصليين هو {m(f'{m_rem} + 1 = {ans}')} لاعباً.",
            ],
            f"انتبه: الإجابة {m(m_rem)} تمثل من أكملوا البطولة، والمطلوب العدد الأصلي وهو {m(ans)}!",
        )

    # 5. nsmo_g89_conditional_urn_transfer (5E, 6M, 4H) — TOPIC = "Data & Probability", SVG: svg_two_jars
    tp_prob = "Data & Probability"
    bp = "nsmo_g89_conditional_urn_transfer"
    for r_cnt, b_cnt, mode in [(5, 3, "same_r"), (6, 4, "same_r"), (4, 5, "same_r"), (4, 6, "diff"), (5, 4, "diff")]:
        tot = r_cnt + b_cnt
        ans = Fraction(r_cnt * (r_cnt - 1), tot * (tot - 1)) if mode == "same_r" else Fraction(2 * r_cnt * b_cnt, tot * (tot - 1))
        B.add_math(
            tp_prob, "Easy", bp,
            f"A jar contains {m(r_cnt)} red marbles and {m(b_cnt)} blue marbles. Two marbles are drawn one after another **without replacement**. What is the probability that {'both marbles are red' if mode == 'same_r' else 'the two marbles have **different** colors'}?",
            f"تحتوي جرة على {m(r_cnt)} كرات حمراء و{m(b_cnt)} كرات زرقاء. سُحبت كرتان الواحدة تلو الأخرى **دون إرجاع**. ما احتمال أن تكون {'الكرتان حمراوين معاً' if mode == 'same_r' else 'الكرتان **مختلفتي** اللون'}؟",
            ans,
            [
                Fraction(r_cnt * r_cnt, tot * tot) if mode == "same_r" else Fraction(r_cnt * b_cnt, tot * (tot - 1)),
                Fraction(2 * r_cnt * b_cnt, tot * tot),
                Fraction(r_cnt - 1, tot - 1),
                Fraction(b_cnt, tot),
            ],
            f"Without replacement, the second draw has {m(tot - 1)} marbles left{' (and remember RB + BR doubles the order!)' if mode == 'diff' else ''}!",
            f"بما أن السحب دون إرجاع، يتبقى في السحبة الثانية {m(tot - 1)} كرات{' (وتذكّر جمع حالتي أحمر-أزرق وأزرق-أحمر!)' if mode == 'diff' else ''}!",
            f"Use conditional multiplication without replacement{' across both color orders (RB and BR)' if mode == 'diff' else ''}!",
            [
                f"Total marbles initially: {m(f'{r_cnt} + {b_cnt} = {tot}')}.",
                f"{'Compute ' + m(f'\\frac{{{r_cnt}}}{{{tot}}} \\times \\frac{{{r_cnt - 1}}}{{{tot - 1}}}') if mode == 'same_r' else 'Sum RB and BR: ' + m(f'2 \\times \\frac{{{r_cnt}}}{{{tot}}} \\times \\frac{{{b_cnt}}}{{{tot - 1}}}')}.",
                f"Simplify the fraction to {m(ans)}.",
            ],
            f"{'With replacement gives ' + m(str(Fraction(r_cnt*r_cnt, tot*tot))) + ', whereas without replacement gives ' + m(ans) if mode == 'same_r' else 'Forgetting both orders (RB and BR) halves the true answer to ' + m(str(ans / 2))}!",
            f"نضرب الاحتمال الأول في الاحتمال الشرطي الثاني مع إنقاص المقام بمقدار {m(1)}!",
            [
                f"مجموع الكرات في البداية {m(tot)} كرة.",
                f"{'الاحتمال يساوي ' + m(f'\\frac{{{r_cnt}}}{{{tot}}} \\times \\frac{{{r_cnt - 1}}}{{{tot - 1}}}') if mode == 'same_r' else 'نجمع الترتيبين (حمراء ثم زرقاء، أو زرقاء ثم حمراء): ' + m(f'2 \\times \\frac{{{r_cnt}}}{{{tot}}} \\times \\frac{{{b_cnt}}}{{{tot - 1}}}')}.",
                f"بعد الاختصار نحصل على {m(ans)}.",
            ],
            f"تحقق: انتبه لإنقاص المقام إلى {m(tot - 1)} في السحبة الثانية!",
            diagram_en=svg_two_jars(f"{r_cnt}R, {b_cnt}B", 0.65, "Draw 2", 0.35, "no repl."),
        )

    med_urn = [
        (4, 1, 2, 3),
        (2, 3, 4, 1),
        (3, 1, 1, 4),
        (1, 3, 3, 2),
        (5, 1, 2, 2),
        (3, 3, 4, 3),
    ]
    for r1, b1, r2, b2 in med_urn:
        t1, t2 = r1 + b1, r2 + b2
        ans = Fraction(r1, t1) * Fraction(r2 + 1, t2 + 1) + Fraction(b1, t1) * Fraction(r2, t2 + 1)
        B.add_math(
            tp_prob, "Medium", bp,
            f"Urn A contains {m(r1)} red and {m(b1)} blue balls, and Urn B contains {m(r2)} red and {m(b2)} blue balls. One ball is drawn at random from Urn A and placed into Urn B; then one ball is drawn at random from Urn B. What is the probability that the ball drawn from Urn B is **red**?",
            f"تحتوي الجرة A على {m(r1)} حمراء و{m(b1)} زرقاء، وتحتوي الجرة B على {m(r2)} حمراء و{m(b2)} زرقاء. نُقلت كرة عشوائياً من A إلى B، ثم سُحبت كرة عشوائياً من B. ما احتمال أن تكون الكرة المسحوبة من B **حمراء**؟",
            ans,
            [
                Fraction(r2, t2),
                Fraction(r1 + r2, t1 + t2),
                Fraction(r1 * (r2 + 1) + b1 * r2, t1 * t2),
                ans + Fraction(1, t1 * (t2 + 1)),
            ],
            f"After moving {m(1)} ball into Urn B, Urn B holds {m(t2 + 1)} balls — split into Case R transferred ({m(f'{r1}/{t1}')}) and Case B transferred ({m(f'{b1}/{t1}')})!",
            f"بعد نقل الكرة يصبح في الجرة B ما مجموعه {m(t2 + 1)} كرات؛ قسّم الحل إلى حالتي نقل حمراء ({m(f'{r1}/{t1}')}) ونقل زرقاء ({m(f'{b1}/{t1}')})!",
            f"Apply the Law of Total Probability across the two transfer colors!",
            [
                f"If Red moves ({m(f'P = {r1}/{t1}')}), Urn B has {m(r2 + 1)} red out of {m(t2 + 1)} balls.",
                f"If Blue moves ({m(f'P = {b1}/{t1}')}), Urn B has {m(r2)} red out of {m(t2 + 1)} balls.",
                f"Total probability: {m(f'\\frac{{{r1}}}{{{t1}}} \\cdot \\frac{{{r2 + 1}}}{{{t2 + 1}}} + \\frac{{{b1}}}{{{t1}}} \\cdot \\frac{{{r2}}}{{{t2 + 1}}}')} = {m(ans)}.",
            ],
            f"Forgetting to update Urn B's total from {m(t2)} to {m(t2 + 1)} is the #1 distractor!",
            f"نطبق قانون الاحتمال الكلي على فرعي نقل كرة حمراء أو نقل كرة زرقاء!",
            [
                f"حالة نقل حمراء ({m(f'{r1}/{t1}')}): يصبح في B عدد {m(r2 + 1)} حمراء من أصل {m(t2 + 1)}.",
                f"حالة نقل زرقاء ({m(f'{b1}/{t1}')}): يبقى في B عدد {m(r2)} حمراء من أصل {m(t2 + 1)}.",
                f"نجمع الفرعين: {m(f'\\frac{{{r1}({r2+1}) + {b1}({r2})}}{{{t1} \\times {t2+1}}}')} = {m(ans)}.",
            ],
            f"انتبه لزيادة العدد الكلي في الجرة B إلى {m(t2 + 1)} بعد النقل!",
            diagram_en=svg_two_jars(f"A: {r1}R,{b1}B", 0.65, f"B: {r2}R,{b2}B", 0.55, "1 ball →"),
        )

    for r1, b1, r2, b2 in [(3, 2, 1, 4), (4, 1, 2, 3)]:
        t1, t2 = r1 + b1, r2 + b2
        p_both_r = Fraction(r1, t1) * Fraction(r2 + 1, t2 + 1)
        p_r2 = p_both_r + Fraction(b1, t1) * Fraction(r2, t2 + 1)
        ans = p_both_r / p_r2
        B.add_math(
            tp_prob, "Hard", bp,
            f"Urn A holds {m(r1)} red and {m(b1)} blue balls, and Urn B holds {m(r2)} red and {m(b2)} blue balls. One ball is moved at random from Urn A to Urn B, and then a ball is drawn at random from Urn B and observed to be **red**. Given this observation, what is the conditional probability that the transferred ball was **also red**?",
            f"تحوي الجرة A عدد {m(r1)} حمراء و{m(b1)} زرقاء، وتحوي الجرة B عدد {m(r2)} حمراء و{m(b2)} زرقاء. نُقلت كرة عشوائياً من A إلى B، ثم سُحبت كرة عشوائياً من B فتبين أنها **حمراء**. بمعلومية ذلك، ما الاحتمال الشرطي لأن تكون الكرة المنقولة من A **حمراء أيضاً**؟",
            ans, [Fraction(r1, t1), p_r2, p_both_r, Fraction(r1 * r2, r1 * r2 + b1 * r2)],
            f"By Bayes' rule, divide the red-transfer branch weight {m(f'{r1} \\times {r2 + 1}')} by the sum of both branch weights {m(f'{r1}({r2 + 1}) + {b1}({r2})')}!",
            f"بقانون بايز، اقسم وزن فرع نقل الحمراء {m(f'{r1} \\times {r2 + 1}')} على مجموع وزني الفرعين {m(f'{r1}({r2 + 1}) + {b1}({r2})')}!",
            f"Apply Bayes' theorem — notice the common denominator {m(f'{t1}({t2 + 1})')} cancels immediately!",
            [
                f"Weight of (Red moved AND Red drawn): {m(f'\\frac{{{r1}}}{{{t1}}} \\cdot \\frac{{{r2 + 1}}}{{{t2 + 1}}} = \\frac{{{r1*(r2+1)}}}{{{t1*(t2+1)}}}')}.",
                f"Weight of (Blue moved AND Red drawn): {m(f'\\frac{{{b1}}}{{{t1}}} \\cdot \\frac{{{r2}}}{{{t2 + 1}}} = \\frac{{{b1*r2}}}{{{t1*(t2+1)}}}')}.",
                f"Bayes' ratio: {m(f'\\frac{{{r1*(r2+1)}}}{{{r1*(r2+1)} + {b1*r2}}} = \\frac{{{r1*(r2+1)}}}{{{r1*(r2+1) + b1*r2}}}')} = {m(ans)}.",
            ],
            f"Observing a red draw boosts the probability of a red transfer above the prior {m(f'{r1}/{t1}')} to {m(ans)}!",
            f"نطبق قاعدة بايز بقسمة احتمال الفرع الأول على مجموع الفرعين بعد اختصار المقام المشترك!",
            [
                f"وزن فرع (نقل حمراء وسحب حمراء) هو {m(f'{r1} \\times {r2 + 1} = {r1*(r2+1)}')}.",
                f"وزن فرع (نقل زرقاء وسحب حمراء) هو {m(f'{b1} \\times {r2} = {b1*r2}')}.",
                f"الاحتمال الشرطي يساوي {m(f'\\frac{{{r1*(r2+1)}}}{{{r1*(r2+1) + b1*r2}}}')} = {m(ans)}.",
            ],
            f"تحقق منطقي: رؤية كرة حمراء ترفع احتمال نقل الحمراء من {m(f'{r1}/{t1}')} إلى {m(ans)}!",
            diagram_en=svg_two_jars(f"A: {r1}R,{b1}B", 0.65, f"B: {r2}R,{b2}B", 0.55, "Bayes P(R₁|R₂)"),
        )

    for r1, b1, r2, b2 in [(3, 1, 1, 3), (2, 3, 3, 2)]:
        t1, t2 = r1 + b1, r2 + b2
        ans = Fraction(r1, t1) * Fraction(r2 + 1, t2 + 1) + Fraction(b1, t1) * Fraction(b2 + 1, t2 + 1)
        B.add_math(
            tp_prob, "Hard", bp,
            f"Urn A contains {m(r1)} red and {m(b1)} blue balls, and Urn B contains {m(r2)} red and {m(b2)} blue balls. One ball is moved at random from Urn A into Urn B, and after mixing, one ball is moved at random from Urn B **back** into Urn A. What is the probability that Urn A ends up with its **exact original** numbers of red and blue balls?",
            f"تحوي الجرة A عدد {m(r1)} حمراء و{m(b1)} زرقاء، وتحوي الجرة B عدد {m(r2)} حمراء و{m(b2)} زرقاء. نُقلت كرة عشوائياً من A إلى B، وبعد الخلط أُعيدت كرة عشوائياً من B إلى A. ما احتمال أن تعود الجرة A إلى **نفس أعداد الألوان الأصلية** بالضبط؟",
            ans,
            [
                Fraction(1, 2) if ans != Fraction(1, 2) else Fraction(3, 5),
                Fraction(r1 * r2 + b1 * b2, t1 * t2),
                ans - Fraction(1, t1 * (t2 + 1)),
                ans + Fraction(1, t1 * (t2 + 1)),
            ],
            f"Urn A regains its exact original counts iff the ball returned from B has the **exact same color** as the ball sent from A!",
            f"تستعيد الجرة A تركيبها الأصلي إذا وفقط إذا كانت الكرة العائدة من B **من نفس لون** الكرة المنقولة من A!",
            f"Sum the probabilities of (Red out, Red back) and (Blue out, Blue back)!",
            [
                f"Urn A's composition is unchanged iff both transfers move the same color.",
                f"Red-out then Red-back: {m(f'\\frac{{{r1}}}{{{t1}}} \\cdot \\frac{{{r2 + 1}}}{{{t2 + 1}}}')}; Blue-out then Blue-back: {m(f'\\frac{{{b1}}}{{{t1}}} \\cdot \\frac{{{b2 + 1}}}{{{t2 + 1}}}')}.",
                f"Add both branches: {m(f'\\frac{{{r1*(r2+1)} + {b1*(b2+1)}}}{{{t1 * (t2 + 1)}}}')} = {m(ans)}.",
            ],
            f"Notice it does NOT need to be the exact same physical ball — only the same **color**!",
            f"يعود التركيب الأصلي إذا وفقط إذا تطابق لون الكرة الذاهبة مع لون الكرة العائدة!",
            [
                f"حالة ذهاب وعودة حمراء: {m(f'\\frac{{{r1}}}{{{t1}}} \\times \\frac{{{r2 + 1}}}{{{t2 + 1}}}')}.",
                f"حالة ذهاب وعودة زرقاء: {m(f'\\frac{{{b1}}}{{{t1}}} \\times \\frac{{{b2 + 1}}}{{{t2 + 1}}}')}.",
                f"مجموع الحالتين بعد الاختصار يساوي {m(ans)}.",
            ],
            f"ملاحظة ذكية: لا يشترط عودة نفس الكرة بذاتها، بل يكفي عودة كرة من **نفس اللون**!",
            diagram_en=svg_two_jars(f"A: {r1}R,{b1}B", 0.6, f"B: {r2}R,{b2}B", 0.6, "A ⇄ B"),
        )


def build_p2_bank() -> list[dict]:
    B = BankBuilder()
    _add_unit_2_1(B)
    _add_unit_2_2(B)
    _add_unit_2_3(B)
    _add_unit_2_4(B)
    _add_unit_2_5(B)
    _add_unit_2_6(B)
    assert len(B.items) == 450, f"Expected 450 Phase 2 items, got {len(B.items)}"
    other_stems = load_other_track_stems()
    seen_en: set[str] = set()
    for q in B.items:
        st = norm_text(q["content"]["en"]["question"])
        assert st not in seen_en, f"Duplicate EN stem inside P2: {q['id']}"
        assert st not in other_stems, f"EN stem collides with another track: {q['id']}"
        seen_en.add(st)
    return B.items
