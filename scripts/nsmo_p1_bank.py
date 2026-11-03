"""NSMO (Mawhiba) Phase 1: Junior Olympiad (Grade 7) Question Bank — 450 Programmatically Verified Questions."""
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
    svg_balance_scales,
    svg_bar_chart,
    svg_column_cryptarithm,
    svg_cube_stack_3d,
    svg_digit_slots,
    svg_dot_pattern,
    svg_factor_tree,
    svg_fraction_grid,
    svg_function_machine,
    svg_inscribed_corner_triangle_in_rect,
    svg_magic_square_3x3,
    svg_matchstick_squares,
    svg_matchstick_triangles,
    svg_motion_timeline,
    svg_number_pyramid,
    svg_number_strip,
    svg_painted_cube_3d,
    svg_paper_fold,
    svg_parallel_zigzag,
    svg_pie_chart,
    svg_pipe_tank,
    svg_rectilinear_staircase,
    svg_shaded_triangle_in_rect,
    svg_spinner,
    svg_street_grid,
    svg_two_jars,
    svg_venn_2,
)

LEVEL = NSMO_LEVELS[0]  # "Phase 1: Junior Olympiad (Grade 7)"


def _count_divisors(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if n % k == 0)


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
        qid = f"NSMO-G7-{len(self.items) + 1:03d}"
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
# UNIT 1.1 — Divisibility, Prime Factors & Remainder Cycles (75 Qs)
# =============================================================================
def _add_unit_1_1(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. nsmo_g7_divisibility_missing_digit (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g7_divisibility_missing_digit"
    easy_div9 = [
        (4, 7, 2, "Mawhiba badge number"),
        (6, 5, 3, "Junior Olympiad registration code"),
        (8, 1, 5, "science library book code"),
        (3, 8, 4, "robotics locker code"),
        (7, 6, 1, "astronomy club ticket number"),
    ]
    for A, C, D, ctx_en in easy_div9:
        valid = [d for d in range(10) if int(f"{A}{C}{d}{D}") % 9 == 0]
        assert len(valid) == 1
        ans = valid[0]
        full_n = int(f"{A}{C}{ans}{D}")
        s_known = A + C + D
        nxt9 = s_known + ans
        B.add_math(
            tp, "Easy", bp,
            f"The 4-digit {ctx_en} {m(f'\\overline{{{A}{C}d{D}}}')} is divisible by {m(9)}. What is the missing digit {m('d')}?",
            f"العدد الرباعي {m(f'\\overline{{{A}{C}d{D}}}')} يقبل القسمة على {m(9)}. ما قيمة الرقم المفقود {m('d')}؟",
            ans, [(ans + 3) % 10, (ans + 6) % 10, (ans + 1) % 10, 9 - ans if 9 - ans != ans else 2],
            f"A number is divisible by {m(9)} if and only if the sum of its digits is a multiple of {m(9)}.",
            f"يقبل العدد القسمة على {m(9)} إذا وفقط إذا كان مجموع أرقامه مضاعفاً للعدد {m(9)}.",
            f"Add the known digits and find {m('d')} so the digit sum reaches the next multiple of {m(9)}.",
            [
                f"Sum of the known digits is {m(f'{A} + {C} + {D} = {s_known}')}.",
                f"The only multiple of {m(9)} reachable by adding a single digit {m('0 \\le d \\le 9')} is {m(nxt9)}.",
                f"Therefore {m(f'd = {nxt9} - {s_known} = {ans}')}.",
            ],
            f"Check: {m(f'{full_n} \\div 9 = {full_n // 9}')} with zero remainder!",
            f"اجمع الأرقام المعلومة ثم اختر {m('d')} ليصل المجموع إلى مضاعف للعدد {m(9)}.",
            [
                f"مجموع الأرقام المعلومة هو {m(f'{A} + {C} + {D} = {s_known}')}.",
                f"المضاعف الوحيد للعدد {m(9)} الممكن بلوغه بإضافة رقم واحد هو {m(nxt9)}.",
                f"إذن {m(f'd = {nxt9} - {s_known} = {ans}')}.",
            ],
            f"تحقق: {m(f'{full_n} \\div 9 = {full_n // 9}')} بدون باقٍ!",
            diagram_en=svg_digit_slots([str(A), str(C), "d", str(D)], "Divisible by 9"),
        )

    med_div11 = [
        (5, 2, 8, 4),
        (7, 1, 9, 3),
        (6, 4, 5, 2),
    ]
    for A, C, D, E in med_div11:
        valid = [d for d in range(10) if int(f"{A}{C}{d}{D}{E}") % 11 == 0]
        assert len(valid) == 1
        ans = valid[0]
        full_n = int(f"{A}{C}{ans}{D}{E}")
        odd_k = A + E
        even_s = C + D
        B.add_math(
            tp, "Medium", bp,
            f"Find the single digit {m('d')} so that the 5-digit integer {m(f'\\overline{{{A}{C}d{D}{E}}}')} is divisible by {m(11)}.",
            f"أوجد الرقم {m('d')} بحيث يقبل العدد الخماسي {m(f'\\overline{{{A}{C}d{D}{E}}}')} القسمة على {m(11)}.",
            ans, [(ans + 2) % 10, (ans + 5) % 10, (ans + 7) % 10, 9],
            f"Use the alternating digit sum for {m(11)}: {m(f'({A} + d + {E}) - ({C} + {D})')} must be {m(0)} or a multiple of {m(11)}.",
            f"استخدم قاعدة التناوب للقسمة على {m(11)}: يجب أن يكون {m(f'({A} + d + {E}) - ({C} + {D})')} مساوياً لـ {m(0)} أو مضاعفاً للعدد {m(11)}.",
            f"Balance the odd-position digit sum against the even-position digit sum modulo {m(11)}!",
            [
                f"Odd-place sum is {m(f'{A} + d + {E} = {odd_k} + d')}, and even-place sum is {m(f'{C} + {D} = {even_s}')}.",
                f"Their difference is {m(f'({odd_k} + d) - {even_s} = d + {odd_k - even_s}')}, which must be divisible by {m(11)}.",
                f"Testing {m('0 \\le d \\le 9')} gives the unique digit {m(f'd = {ans}')}.",
            ],
            f"Check: {m(f'{full_n} \\div 11 = {full_n // 11}')}!",
            f"طبّق قاعدة القسمة على {m(11)} بحساب الفرق بين مجموع الخانات الفردية ومجموع الخانات الزوجية!",
            [
                f"مجموع الخانات الفردية {m(f'{A} + d + {E} = {odd_k} + d')}، والزوجية {m(f'{C} + {D} = {even_s}')}.",
                f"الفرق بينهما {m(f'd + {odd_k - even_s}')} يجب أن يقبل القسمة على {m(11)}.",
                f"القيمة الوحيدة ضمن {m('0 \\le d \\le 9')} هي {m(f'd = {ans}')}.",
            ],
            f"تحقق: {m(f'{full_n} \\div 11 = {full_n // 11}')}!",
            diagram_en=svg_digit_slots([str(A), str(C), "d", str(D), str(E)], "Divisible by 11"),
        )

    med_div36 = [
        (4, 1),
        (7, 5),
        (2, 7),
    ]
    for d1, d3 in med_div36:
        sums = [a + b for a in range(10) for b in range(10) if int(f"{d1}{a}{d3}{b}") % 36 == 0]
        ans = max(sums)
        B.add_math(
            tp, "Medium", bp,
            f"The 4-digit number {m(f'\\overline{{{d1}A{d3}B}}')} is divisible by {m(36)}, where {m('A')} and {m('B')} are digits. What is the **largest** possible value of {m('A + B')}?",
            f"العدد الرباعي {m(f'\\overline{{{d1}A{d3}B}}')} يقبل القسمة على {m(36)}، حيث {m('A')} و{m('B')} رقمان. ما **أكبر** قيمة ممكنة للمجموع {m('A + B')}؟",
            ans, [ans - 9 if ans >= 9 else ans + 2, ans - 2, ans + 2, ans + 4],
            f"Split {m('36 = 4 \\times 9')}: find valid digits {m('B')} so {m(f'\\overline{{{d3}B}}')} is divisible by {m(4)}, then maximize {m('A + B')} using divisibility by {m(9)}.",
            f"فكّك {m('36 = 4 \\times 9')}: أوجد قيم {m('B')} التي تجعل {m(f'\\overline{{{d3}B}}')} قابلاً للقسمة على {m(4)}، ثم كَبِّر {m('A + B')} بشرط القسمة على {m(9)}.",
            f"Enforce divisibility by {m(4)} on {m(f'\\overline{{{d3}B}}')} and divisibility by {m(9)} on {m(f'{d1} + A + {d3} + B')}!",
            [
                f"Since {m(f'\\overline{{{d3}B}}')} is odd-tens ({m(d3)}), divisibility by {m(4)} forces {m('B \\in \\{2, 6\\}')}.",
                f"Divisibility by {m(9)} requires {m(f'{d1 + d3} + (A + B)')} to be a multiple of {m(9)}.",
                f"With {m('A \\le 9')} and {m('B \\le 6')}, we have {m('A + B \\le 15')}, making the largest achievable sum {m(f'A + B = {ans}')}.",
            ],
            f"Check: valid digits {m('(A, B)')} with {m('B \\in \\{2, 6\\}')} attain {m(f'A + B = {ans}')} cleanly!",
            f"نطبق شرطَي القسمة على {m(4)} وعلى {m(9)} معاً!",
            [
                f"لكي يقبل {m(f'\\overline{{{d3}B}}')} القسمة على {m(4)} يجب أن يكون {m('B \\in \\{2, 6\\}')}.",
                f"شرط القسمة على {m(9)} يتطلب أن يقبل {m(f'{d1 + d3} + A + B')} القسمة على {m(9)}.",
                f"بما أن {m('A + B \\le 9 + 6 = 15')}، فإن أكبر مجموع ممكن هو {m(ans)}.",
            ],
            f"تحقق: توجد أرقام فعلية تحقق القسمة على {m(36)} وتعطي {m(f'A + B = {ans}')}!",
            diagram_en=svg_digit_slots([str(d1), "A", str(d3), "B"], "Divisible by 36"),
        )

    hard_div = [
        (3, 6, 5, 72, "8 \\times 9"),
        (5, 3, 7, 72, "8 \\times 9"),
        (6, 1, 4, 88, "8 \\times 11"),
        (4, 9, 2, 88, "8 \\times 11"),
    ]
    for m1, m2, m3, modv, split_tex in hard_div:
        pairs = [(a, b) for a in range(1, 10) for b in range(10) if int(f"{a}{m1}{m2}{m3}{b}") % modv == 0]
        assert len(pairs) == 1
        A, B_dig = pairs[0]
        ans = A * 10 + B_dig
        tail3 = int(f"{m2}{m3}{B_dig}")
        full5 = int(f"{A}{m1}{m2}{m3}{B_dig}")
        B.add_math(
            tp, "Hard", bp,
            f"The 5-digit integer {m(f'\\overline{{A{m1}{m2}{m3}B}}')} (with {m('A \\ne 0')}) is divisible by {m(modv)}. Find the two-digit number {m('\\overline{AB}')}.",
            f"العدد الخماسي {m(f'\\overline{{A{m1}{m2}{m3}B}}')} (حيث {m('A \\ne 0')}) يقبل القسمة على {m(modv)}. أوجد العدد المكوّن من رقمين {m('\\overline{AB}')}.",
            ans, [ans + 10, ans - 10 if ans > 20 else ans + 18, B_dig * 10 + A, ans + 4],
            f"Factor {m(f'{modv} = {split_tex}')}: use divisibility by {m(8)} on the last three digits {m(f'\\overline{{{m2}{m3}B}}')} to pin down {m('B')} first!",
            f"فكّك {m(f'{modv} = {split_tex}')}: استخدم قابلية القسمة على {m(8)} لآخر ثلاثة أرقام {m(f'\\overline{{{m2}{m3}B}}')} لإيجاد {m('B')} أولاً!",
            f"Pin down {m('B')} from the last three digits {m(f'\\overline{{{m2}{m3}B}} \\bmod 8 = 0')}, then solve uniquely for {m('A')}!",
            [
                f"For divisibility by {m(8)}, check {m(f'\\overline{{{m2}{m3}B}}')}: only {m(f'B = {B_dig}')} makes {m(tail3)} divisible by {m(8)} ({m(f'{tail3} = 8 \\times {tail3 // 8}')}).",
                f"Now apply the second factor in {m(split_tex)} to {m(f'\\overline{{A{m1}{m2}{m3}{B_dig}}}')}, which uniquely forces {m(f'A = {A}')}.",
                f"Combining {m(f'A = {A}')} and {m(f'B = {B_dig}')} gives {m(f'\\overline{{AB}} = {ans}')}.",
            ],
            f"Exact division check: {m(f'{full5} \\div {modv} = {full5 // modv}')}!",
            f"نحدد {m('B')} من شرط القسمة على {m(8)} لآخر 3 خانات، ثم نجد {m('A')} الوحيدة!",
            [
                f"للقسمة على {m(8)} نفحص {m(f'\\overline{{{m2}{m3}B}}')} فنجد {m(f'B = {B_dig}')} فقط.",
                f"بتطبيق شرط العامل الثاني في {m(split_tex)} على {m(f'\\overline{{A{m1}{m2}{m3}{B_dig}}}')} نجد {m(f'A = {A}')} حصراً.",
                f"إذن العدد المطلوب هو {m(f'\\overline{{AB}} = {ans}')}.",
            ],
            f"تحقق: {m(f'{full5} \\div {modv} = {full5 // modv}')}!",
            diagram_en=svg_digit_slots(["A", str(m1), str(m2), str(m3), "B"], f"Divisible by {modv}"),
        )

    # 2. nsmo_g7_gcd_lcm_beacons (5E, 6M, 4H) — SVG: svg_venn_2
    bp = "nsmo_g7_gcd_lcm_beacons"
    easy_lcm = [
        (8, 12, "fountains in a Diriyah courtyard splash"),
        (9, 15, "automated shuttles depart the campus hub"),
        (10, 14, "observatory lasers pulse"),
        (12, 20, "harbor lighthouses flash"),
        (15, 25, "metro express bells chime"),
    ]
    for a, b, ctx in easy_lcm:
        ans = math.lcm(a, b)
        g = math.gcd(a, b)
        B.add_math(
            tp, "Easy", bp,
            f"Two {ctx} every {m(a)} minutes and every {m(b)} minutes, respectively. If they happen together right now, after how many **minutes** will they next happen together?",
            f"حدثان دوريّان يتكرر الأول كل {m(a)} دقائق والثاني كل {m(b)} دقيقة. إذا وقعا معاً الآن، فبعد كم **دقيقة** يقعان معاً في المرة القادمة؟",
            ans, [a * b, a + b, ans // 2 if ans % 2 == 0 else ans + a, g],
            f"They coincide again at the **least common multiple** {m(f'\\operatorname{{lcm}}({a}, {b})')}.",
            f"يتزامنان مجدداً عند **المضاعف المشترك الأصغر** {m(f'\\operatorname{{lcm}}({a}, {b})')}.",
            f"Compute {m(f'\\operatorname{{lcm}}({a}, {b}) = \\frac{{{a} \\times {b}}}{{\\gcd({a}, {b})}}')}!",
            [
                f"The greatest common divisor of {m(a)} and {m(b)} is {m(f'\\gcd({a}, {b}) = {g}')}.",
                f"Therefore {m(f'\\operatorname{{lcm}}({a}, {b}) = \\frac{{{a} \\times {b}}}{{{g}}} = {ans}')} minutes.",
            ],
            f"At {m(ans)} minutes, the first has completed {m(ans // a)} cycles and the second {m(ans // b)} cycles!",
            f"نحسب المضاعف المشترك الأصغر للعددين {m(a)} و{m(b)}!",
            [
                f"القاسم المشترك الأكبر للعددين هو {m(f'\\gcd({a}, {b}) = {g}')}.",
                f"إذن {m(f'\\operatorname{{lcm}}({a}, {b}) = \\frac{{{a} \\times {b}}}{{{g}}} = {ans}')} دقيقة.",
            ],
            f"تحقق: {m(f'{ans} \\div {a} = {ans // a}')} دورات و{m(f'{ans} \\div {b} = {ans // b}')} دورات!",
            diagram_en=svg_venn_2(f"A={a}", f"B={b}", str(a // g), str(g), str(b // g), f"LCM={ans}"),
        )

    med_gcd_tiles = [
        (48, 36),
        (60, 45),
        (72, 40),
        (84, 60),
        (90, 54),
        (96, 56),
    ]
    for L, W in med_gcd_tiles:
        s = math.gcd(L, W)
        ans = (L // s) * (W // s)
        B.add_math(
            tp, "Medium", bp,
            f"A rectangular poster board measuring {m(f'{L}\\text{{ cm}} \\times {W}\\text{{ cm}}')} is cut completely into identical squares with **no leftover waste**. What is the **minimum** possible number of squares?",
            f"لوح مستطيل أبعاده {m(f'{L}\\text{{ سم}} \\times {W}\\text{{ سم}}')} يُراد قصّه بالكامل إلى مربعات متطابقة **دون أي بقايا**. ما **أقل** عدد ممكن من هذه المربعات؟",
            ans, [s, (L // s) + (W // s), ans * 4, L * W // s],
            f"Fewest squares means **largest** possible square side {m(f's = \\gcd({L}, {W})')}, then count how many {m('s \\times s')} squares fit!",
            f"أقل عدد من المربعات يعني **أكبر** طول ضلع ممكن للمربع {m(f's = \\gcd({L}, {W})')}، ثم نحسب عدد المربعات الناتجة!",
            f"Find the largest square side {m(f's = \\gcd({L}, {W})')} first, then multiply {m(f'({L}/s) \\times ({W}/s)')}!",
            [
                f"For squares to tile {m(f'{L} \\times {W}')} exactly, side {m('s')} must divide both {m(L)} and {m(W)}. To minimize the count, pick {m(f's = \\gcd({L}, {W}) = {s}\\text{{ cm}}')}.",
                f"Along the length we get {m(f'{L} \\div {s} = {L // s}')} squares, and along the width {m(f'{W} \\div {s} = {W // s}')} squares.",
                f"Total squares = {m(f'{L // s} \\times {W // s} = {ans}')}.",
            ],
            f"Area check: {m(f'{ans} \\times {s}^2 = {ans * s * s} = {L} \\times {W}')}!",
            f"نختار أكبر ضلع ممكن للمربع وهو القاسم المشترك الأكبر {m(f's = \\gcd({L}, {W})')} ثم نضرب عدد الصفوف في الأعمدة!",
            [
                f"أكبر طول ضلع للمربع هو {m(f's = \\gcd({L}, {W}) = {s}')} سم.",
                f"ينقسم الطول إلى {m(f'{L} \\div {s} = {L // s}')} قطع، والعرض إلى {m(f'{W} \\div {s} = {W // s}')} قطع.",
                f"أقل عدد من المربعات = {m(f'{L // s} \\times {W // s} = {ans}')}.",
            ],
            f"تحقق بالمساحة: {m(f'{ans} \\times {s}^2 = {L * W}')} سم²!",
            diagram_en=svg_venn_2(f"L={L}", f"W={W}", str(L // s), f"s={s}", str(W // s), f"{ans} sq"),
        )

    hard_gcd_lcm = [
        (6, 180),
        (8, 240),
        (12, 180),
        (15, 300),
    ]
    for g, L in hard_gcd_lcm:
        k = L // g
        pairs = [(g * u, g * (k // u)) for u in range(1, int(math.isqrt(k)) + 1) if k % u == 0 and math.gcd(u, k // u) == 1]
        ans = min(a + b for a, b in pairs)
        best_a, best_b = min(pairs, key=lambda p: p[0] + p[1])
        B.add_math(
            tp, "Hard", bp,
            f"Two positive integers {m('a')} and {m('b')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. What is the **smallest** possible value of {m('a + b')}?",
            f"عددان صحيحان موجبان {m('a')} و{m('b')} يحققان {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. ما **أصغر** قيمة ممكنة للمجموع {m('a + b')}؟",
            ans, [g + L, ans + 2 * g, ans - g, g * (k + 1)],
            f"Write {m(f'a = {g}u')} and {m(f'b = {g}v')} with {m('\\gcd(u, v) = 1')} and {m(f'u \\cdot v = {L} / {g} = {k}')}, then pick coprime factors closest together!",
            f"اكتب {m(f'a = {g}u')} و{m(f'b = {g}v')} حيث {m('\\gcd(u, v) = 1')} و{m(f'u \\cdot v = {L} / {g} = {k}')}، واختر العاملين المتقاربين!",
            f"Factor {m(f'u \\cdot v = {k}')} into **coprime** pairs and minimize {m(f'{g}(u + v)')}!",
            [
                f"Let {m(f'a = {g}u')} and {m(f'b = {g}v')} where {m('\\gcd(u, v) = 1')}. Then {m(f'\\operatorname{{lcm}}(a, b) = {g}uv = {L} \\implies uv = {k}')}.",
                f"To minimize {m('u + v')}, choose the closest coprime factor pair of {m(k)}: {m(f'({best_a // g}, {best_b // g})')}.",
                f"This gives {m(f'a = {best_a}')}, {m(f'b = {best_b}')}, and minimum sum {m(f'a + b = {ans}')}.",
            ],
            f"Verify: {m(f'\\gcd({best_a}, {best_b}) = {math.gcd(best_a, best_b)}')} and {m(f'\\operatorname{{lcm}}({best_a}, {best_b}) = {math.lcm(best_a, best_b)}')}!",
            f"نفرض {m(f'a = {g}u, b = {g}v')} مع {m('\\gcd(u, v) = 1')} فنحصل على {m(f'uv = {k}')}!",
            [
                f"من العلاقة {m(f'{g}uv = {L}')} نجد {m(f'uv = {k}')} مع كون {m('u, v')} أوليين نسبياً.",
                f"أقرب عاملين أوليين نسبياً للعدد {m(k)} هما {m(f'{best_a // g}')} و{m(f'{best_b // g}')}.",
                f"إذن أصغر مجموع هو {m(f'{best_a} + {best_b} = {ans}')}.",
            ],
            f"تحقق: {m(f'\\gcd({best_a}, {best_b}) = {g}')} و{m(f'\\operatorname{{lcm}}({best_a}, {best_b}) = {L}')}!",
            diagram_en=svg_venn_2(f"a={best_a}", f"b={best_b}", str(best_a // g), str(g), str(best_b // g), f"LCM={L}"),
        )

    # 3. nsmo_g7_prime_factor_divisors (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g7_prime_factor_divisors"
    easy_divs = [
        (72, "8", "9", "3", "3", "2^3 \\times 3^2", "(3+1)(2+1)"),
        (108, "4", "27", "3", "9", "2^2 \\times 3^3", "(2+1)(3+1)"),
        (120, "8", "15", "3", "5", "2^3 \\times 3^1 \\times 5^1", "(3+1)(1+1)(1+1)"),
        (150, "6", "25", "5", "5", "2^1 \\times 3^1 \\times 5^2", "(1+1)(1+1)(2+1)"),
        (200, "8", "25", "5", "5", "2^3 \\times 5^2", "(3+1)(2+1)"),
    ]
    for N, l1, r1, rl, rr, f_tex, prod_tex in easy_divs:
        ans = _count_divisors(N)
        B.add_math(
            tp, "Easy", bp,
            f"How many positive integer divisors does {m(N)} have?",
            f"كم قاسماً صحيحاً موجباً للعدد {m(N)}؟",
            ans, [ans - 4, ans + 4, ans // 2, ans + 6],
            f"Write the prime factorization of {m(N)}, add {m(1)} to each prime exponent, and multiply!",
            f"اكتب التحليل الأولي للعدد {m(N)}، ثم أضف {m(1)} إلى كل أس واضرب النواتج!",
            f"Factor {m(f'{N} = {f_tex}')} and apply {m('d(N) = \\prod (e_i + 1)')}!",
            [
                f"Prime factorization gives {m(f'{N} = {f_tex}')}.",
                f"Add {m(1)} to each prime exponent and multiply: {m(f'{prod_tex} = {ans}')} positive divisors.",
            ],
            f"Every divisor pairs as {m(f'(d, {N}/d)')}, giving {m(ans)} divisors in total!",
            f"نحلل {m(N)} إلى عوامله الأولية {m(f_tex)} ونطبق قانون عدد القواسم!",
            [
                f"التحليل الأولي للعدد هو {m(f'{N} = {f_tex}')}.",
                f"بإضافة {m(1)} لكل أس والضرب نجد {m(f'{prod_tex} = {ans}')} قاسماً موجباً.",
            ],
            f"تحقق: عدد القواسم الموجبة للعدد {m(N)} هو {m(ans)} بالضبط!",
            diagram_en=svg_factor_tree(str(N), l1, r1, rl, rr),
        )

    med_sq = [
        (72, "8", "9", "3", "3", "2^3 \\times 3^2"),
        (120, "8", "15", "3", "5", "2^3 \\times 3^1 \\times 5^1"),
        (150, "6", "25", "5", "5", "2^1 \\times 3^1 \\times 5^2"),
        (180, "20", "9", "3", "3", "2^2 \\times 3^2 \\times 5^1"),
        (240, "16", "15", "3", "5", "2^4 \\times 3^1 \\times 5^1"),
        (252, "36", "7", "7", "1", "2^2 \\times 3^2 \\times 7^1"),
    ]
    for N, l1, r1, rl, rr, f_tex in med_sq:
        ans = next(k for k in range(1, 500) if math.isqrt(N * k) ** 2 == N * k)
        sq_root = math.isqrt(N * ans)
        B.add_math(
            tp, "Medium", bp,
            f"What is the **smallest** positive integer {m('k')} such that {m(f'{N}k')} is a perfect square?",
            f"ما **أصغر** عدد صحيح موجب {m('k')} يجعل حاصل الضرب {m(f'{N}k')} مربعاً كاملاً؟",
            ans, [ans * 2, ans * 3, N // ans if N % ans == 0 else ans + 4, ans + 2],
            f"A positive integer is a perfect square when **every** prime exponent is **even**. Multiply by one copy of each prime with an odd exponent!",
            f"يكون العدد مربعاً كاملاً عندما تكون **جميع** أسس عوامله الأولية **زوجية**. اضرب في العوامل ذات الأس الفردي فقط!",
            f"Inspect {m(f'{N} = {f_tex}')} and supply one factor of each prime that has an odd exponent!",
            [
                f"Factor {m(f'{N} = {f_tex}')}.",
                f"Collecting one copy of each prime with an odd exponent gives {m(f'k = {ans}')}.",
                f"Then {m(f'{N} \\times {ans} = {N * ans} = {sq_root}^2')}, a perfect square!",
            ],
            f"Check: {m(f'{sq_root}^2 = {N * ans}')}, and no smaller positive {m('k')} pairs all odd prime exponents!",
            f"نفحص أسس العوامل الأولية في {m(f'{N} = {f_tex}')} ونكمّل الأسس الفردية لتصبح زوجية!",
            [
                f"بتحليل العدد نجد {m(f'{N} = {f_tex}')}.",
                f"بضرب العوامل الأولية ذات الأسس الفردية نحصل على {m(f'k = {ans}')}.",
                f"عندئذٍ {m(f'{N} \\times {ans} = {N * ans} = {sq_root}^2')} مربع كامل!",
            ],
            f"تحقق: {m(f'\\sqrt{{{N * ans}}} = {sq_root}')}!",
            diagram_en=svg_factor_tree(str(N), l1, r1, rl, rr),
        )

    hard_divs = [
        (6, "2^2 \\times 3^1"),
        (8, "2^3 \\times 3^1"),
        (9, "2^2 \\times 3^2"),
        (10, "2^4 \\times 3^1"),
    ]
    for m_cnt, best_tex in hard_divs:
        ans = next(n for n in range(1, 500) if _count_divisors(n) == m_cnt)
        B.add_math(
            tp, "Hard", bp,
            f"What is the **smallest** positive integer that has **exactly {m(m_cnt)}** positive divisors?",
            f"ما **أصغر** عدد صحيح موجب له **{m(m_cnt)} قواسم موجبة بالضبط**؟",
            ans, [2 ** (m_cnt - 1), ans + 6, ans * 2, ans - 4 if ans > 8 else ans + 12],
            f"Factor {m(m_cnt)} in every possible way as {m('(e_1 + 1)(e_2 + 1)\\cdots')} and assign the largest exponents to the smallest primes {m('2, 3, 5, \\dots')}!",
            f"حلّل العدد {m(m_cnt)} على الصورة {m('(e_1 + 1)(e_2 + 1)\\cdots')} وامنح الأسس الأكبر لأصغر الأعداد الأولية {m('2, 3, 5')}!",
            f"Compare candidate prime-power shapes whose exponent-plus-one product equals {m(m_cnt)}!",
            [
                f"Using a single prime gives {m(f'2^{{{m_cnt - 1}}} = {2**(m_cnt - 1)}')}, which is large.",
                f"Splitting {m(m_cnt)} across the smallest primes {m(2)} and {m(3)} gives {m(f'{best_tex} = {ans}')}, which is much smaller!",
                f"Checking every positive integer below {m(ans)} confirms {m(ans)} is the minimum.",
            ],
            f"Divisors of {m(ans)}: there are indeed {m(_count_divisors(ans))} positive divisors!",
            f"نقارن بين التشكيلات الأسية الممكنة على أصغر الأعداد الأولية {m(2)} و{m(3)}!",
            [
                f"استخدام عامل أولي وحيد يعطي {m(f'2^{{{m_cnt - 1}}} = {2**(m_cnt - 1)}')}.",
                f"توزيع الأسس على {m(2)} و{m(3)} يعطي {m(f'{best_tex} = {ans}')} وهو أصغر بكثير.",
                f"إذن أصغر عدد موجب له {m(m_cnt)} قواسم بالضبط هو {m(ans)}.",
            ],
            f"تحقق: للعدد {m(ans)} بالضبط {m(m_cnt)} قواسم موجبة!",
            diagram_en=svg_factor_tree(str(ans), "4", str(ans // 4), str(ans // 4), "1"),
        )

    # 4. nsmo_g7_last_digit_power_cycle (5E, 6M, 4H) — SVG: svg_function_machine
    bp = "nsmo_g7_last_digit_power_cycle"
    easy_pow = [(2, 53), (3, 62), (7, 45), (8, 71), (7, 84)]
    for base, exp in easy_pow:
        ans = pow(base, exp, 10)
        cyc = [pow(base, k, 10) for k in (1, 2, 3, 4)]
        rem = exp % 4
        B.add_math(
            tp, "Easy", bp,
            f"What is the **units digit** (ones digit) of {m(f'{base}^{{{exp}}}')}?",
            f"ما **رقم الآحاد** للعدد {m(f'{base}^{{{exp}}}')}؟",
            ans, [x for x in cyc if x != ans],
            f"The units digits of powers of {m(base)} repeat in a cycle of length {m(4)}: {m(f'{cyc}')}. Divide {m(exp)} by {m(4)}!",
            f"آحاد قوى العدد {m(base)} يتكرر كل {m(4)} خطوات: {m(f'{cyc}')}. اقسم الأس {m(exp)} على {m(4)}!",
            f"Find {m(f'{exp} \\bmod 4')} and pick the matching step in the 4-cycle {m(f'{cyc}')}!",
            [
                f"Powers of {m(base)} have units-digit cycle {m(f'({cyc[0]}, {cyc[1]}, {cyc[2]}, {cyc[3]})')} of length {m(4)}.",
                f"Divide the exponent by {m(4)}: {m(f'{exp} = 4 \\times {exp // 4} + {rem}')}.",
                f"Remainder {m(rem)} corresponds to step {m(4 if rem == 0 else rem)} of the cycle, giving units digit {m(ans)}.",
            ],
            f"Check with smaller matching exponent {m(4 if rem == 0 else rem)}: {m(f'{base}^{{{4 if rem == 0 else rem}}} = {base ** (4 if rem == 0 else rem)}')}, ending in {m(ans)}!",
            f"نقسم الأس {m(exp)} على {m(4)} لتحديد الموقع داخل الدورة الرباعية {m(f'{cyc}')}!",
            [
                f"دورة آحاد قوى العدد {m(base)} هي {m(f'({cyc[0]}, {cyc[1]}, {cyc[2]}, {cyc[3]})')}.",
                f"باقي قسمة {m(exp)} على {m(4)} هو {m(rem)} (أي الحد رقم {m(4 if rem == 0 else rem)} في الدورة).",
                f"إذن رقم الآحاد هو {m(ans)}.",
            ],
            f"تحقق: {m(f'{base}^{{{4 if rem == 0 else rem}}}')} آحاده {m(ans)} أيضاً!",
            diagram_en=svg_function_machine(f"{base}^{exp}", "exp ÷ 4", f"rem {rem}", str(ans)),
        )

    med_pow = [
        (3, 35, 7, 22, "+"),
        (2, 49, 8, 34, "+"),
        (7, 51, 9, 25, "+"),
        (3, 44, 7, 37, "×"),
        (2, 63, 3, 29, "×"),
        (8, 41, 7, 50, "+"),
    ]
    for b1, e1, b2, e2, op in med_pow:
        u1, u2 = pow(b1, e1, 10), pow(b2, e2, 10)
        comb = u1 + u2 if op == "+" else u1 * u2
        ans = comb % 10
        op_tex = "+" if op == "+" else "\\times"
        B.add_math(
            tp, "Medium", bp,
            f"Find the **units digit** of {m(f'{b1}^{{{e1}}} {op_tex} {b2}^{{{e2}}}')}.",
            f"أوجد **رقم الآحاد** للمقدار {m(f'{b1}^{{{e1}}} {op_tex} {b2}^{{{e2}}}')}.",
            ans, [(ans + 2) % 10, (ans + 4) % 10, (ans + 6) % 10, (ans + 8) % 10],
            f"Find the units digit of {m(f'{b1}^{{{e1}}}')} and {m(f'{b2}^{{{e2}}}')} separately using their 4-cycles, then combine modulo {m(10)}.",
            f"أوجد رقم آحاد كلٍّ من {m(f'{b1}^{{{e1}}}')} و{m(f'{b2}^{{{e2}}}')} على حدة، ثم طبّق العملية وخذ آحاد الناتج.",
            f"Compute each power's units digit via its 4-step cycle, then combine {m(f'{u1} {op_tex} {u2}')} modulo {m(10)}!",
            [
                f"Using the 4-cycle of {m(b1)}, {m(f'{b1}^{{{e1}}}')} ends in {m(u1)}.",
                f"Using the 4-cycle of {m(b2)}, {m(f'{b2}^{{{e2}}}')} ends in {m(u2)}.",
                f"Combining modulo {m(10)}: {m(f'{u1} {op_tex} {u2} = {comb}')}, which has units digit {m(ans)}.",
            ],
            f"Verified directly in modular arithmetic: {m(f'({b1}^{{{e1}}} {op_tex} {b2}^{{{e2}}}) \\bmod 10 = {ans}')}!",
            f"نحسب آحاد كل قوة بدورتها ثم نوجد آحاد الناتج!",
            [
                f"آحاد {m(f'{b1}^{{{e1}}}')} يساوي {m(u1)}، وآحاد {m(f'{b2}^{{{e2}}}')} يساوي {m(u2)}.",
                f"نحسب {m(f'{u1} {op_tex} {u2} = {comb}')} فنجد أن رقم الآحاد هو {m(ans)}.",
            ],
            f"تحقق: باقي القسمة على {m(10)} يساوي {m(ans)} بالضبط!",
        )

    hard_pow = [
        (7, 44, 3, 21),   # ends 1 - 3 -> 8!
        (9, 40, 2, 35),   # ends 1 - 8 -> 3!
        (3, 52, 7, 19),   # ends 1 - 3 -> 8? Wait make distinct contexts & values!
        (8, 36, 7, 25),   # ends 6 - 7 -> 9!
    ]
    for b1, e1, b2, e2 in hard_pow:
        assert b1 ** e1 > b2 ** e2
        u1, u2 = pow(b1, e1, 10), pow(b2, e2, 10)
        ans = (u1 - u2) % 10
        B.add_math(
            tp, "Hard", bp,
            f"What is the **units digit** of the positive integer {m(f'{b1}^{{{e1}}} - {b2}^{{{e2}}}')}?",
            f"ما **رقم الآحاد** للعدد الصحيح الموجب {m(f'{b1}^{{{e1}}} - {b2}^{{{e2}}}')}؟",
            ans, [abs(u1 - u2) if abs(u1 - u2) != ans else (ans + 2) % 10, (u1 + u2) % 10, (ans + 4) % 10, (ans + 5) % 10],
            f"Careful! Since {m(f'{b1}^{{{e1}}} > {b2}^{{{e2}}}')}, if the first units digit {m(u1)} is smaller than {m(u2)}, **borrow {m(10)}** before subtracting!",
            f"انتبه! بما أن {m(f'{b1}^{{{e1}}} > {b2}^{{{e2}}}')}، إذا كان آحاد الأول أصغر من آحاد الثاني نستلف {m(10)} قبل الطرح!",
            f"Find both units digits ({m(u1)} and {m(u2)}) and borrow {m(10)} since {m(f'{u1} < {u2}')}!",
            [
                f"From 4-step cycles, {m(f'{b1}^{{{e1}}}')} ends in {m(u1)} and {m(f'{b2}^{{{e2}}}')} ends in {m(u2)}.",
                f"Because {m(f'{b1}^{{{e1}}} > {b2}^{{{e2}}}')} and {m(f'{u1} < {u2}')}, subtracting borrows {m(10)} from the tens place: {m(f'({u1} + 10) - {u2} = {ans}')}.",
            ],
            f"Trap avoided: never take {m(f'|{u1} - {u2}| = {abs(u1 - u2)}')}—borrowing {m(10)} gives {m(ans)}!",
            f"نحسب آحاد كل حد ثم نستلف {m(10)} لأن {m(f'{u1} < {u2}')}!",
            [
                f"آحاد {m(f'{b1}^{{{e1}}}')} هو {m(u1)}، وآحاد {m(f'{b2}^{{{e2}}}')} هو {m(u2)}.",
                f"بما أن العدد الأول أكبر بكثير و{m(f'{u1} < {u2}')} نستلف {m(10)}: {m(f'{u1 + 10} - {u2} = {ans}')}.",
            ],
            f"تحقق: الاستلاف من خانة العشرات يجعل الآحاد {m(ans)} وليس {m(abs(u1 - u2))}!",
            diagram_en=svg_function_machine(f"{b1}^{e1}−{b2}^{e2}", f"..{u1} − ..{u2}", "+10 borrow", str(ans)),
        )

    # 5. nsmo_g7_remainder_division_rule (5E, 6M, 4H) — SVG: svg_function_machine on Easy
    bp = "nsmo_g7_remainder_division_rule"
    easy_rem = [(14, 9), (17, 6), (23, 8), (19, 11), (25, 7)]
    for d, q in easy_rem:
        r_max = d - 1
        ans = d * q + r_max
        B.add_math(
            tp, "Easy", bp,
            f"When a positive integer {m('N')} is divided by {m(d)}, the quotient is {m(q)}. What is the **largest** possible value of {m('N')}?",
            f"عند قسمة عدد صحيح موجب {m('N')} على {m(d)} يكون خارج القسمة {m(q)}. ما **أكبر** قيمة ممكنة للعدد {m('N')}؟",
            ans, [d * q, d * q + d, d * (q + 1) + 1, d * q + 1],
            f"Write {m(f'N = {d} \\times {q} + r')}. Since {m(f'0 \\le r < {d}')}, the largest possible remainder is {m(r_max)}!",
            f"اكتب {m(f'N = {d} \\times {q} + r')}. بما أن {m(f'0 \\le r < {d}')} فإن أكبر باقٍ ممكن هو {m(r_max)}!",
            f"Maximize {m('r')} in {m(f'N = {d} \\cdot {q} + r')} subject to {m(f'r < {d}')}!",
            [
                f"By the division rule, {m(f'N = {d} \\times {q} + r')} with {m(f'0 \\le r \\le {r_max}')}.",
                f"Choosing the largest allowed remainder {m(f'r = {r_max}')} gives {m(f'N = {d * q} + {r_max} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} \\div {d} = {q}')} with remainder {m(ans % d)} (and {m(ans + 1)} would raise the quotient to {m(q + 1)})!",
            f"نطبق قاعدة القسمة {m(f'N = {d} \\times {q} + r')} مع أخذ أكبر باقٍ مسموح {m(f'r = {r_max}')}!",
            [
                f"الباقي {m('r')} يحقق {m(f'0 \\le r < {d}')}، فأكبر قيمة له هي {m(r_max)}.",
                f"إذن أكبر قيمة للعدد هي {m(f'{d} \\times {q} + {r_max} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} = {d} \\times {q} + {r_max}')}!",
            diagram_en=svg_function_machine("Max N", f"÷ {d}", f"q={q}, r={r_max}", str(ans)),
        )

    med_q_eq_r = [5, 6, 7, 8, 9, 11]
    for d in med_q_eq_r:
        nums = [d * r + r for r in range(1, d)]
        ans = sum(nums)
        B.add_math(
            tp, "Medium", bp,
            f"Find the **sum** of all positive integers that give a **quotient equal to the remainder** when divided by {m(d)}.",
            f"أوجد **مجموع** جميع الأعداد الصحيحة الموجبة التي يكون **خارج قسمتها مساوياً لباقي قسمتها** عند قسمتها على {m(d)}.",
            ans, [ans + (d + 1) * d, (d + 1) * (d - 1), d * (d - 1) // 2, ans - (d + 1)],
            f"If quotient and remainder both equal {m('r')}, then {m(f'N = {d}r + r = {d + 1}r')} for {m(f'r = 1, 2, \\dots, {d - 1}')}!",
            f"إذا كان خارج القسمة والباقي معاً يساويان {m('r')}، فإن {m(f'N = {d}r + r = {d + 1}r')} لقيم {m(f'r = 1, 2, \\dots, {d - 1}')}!",
            f"Express each valid integer as {m(f'({d} + 1)r = {d + 1}r')} for {m(f'1 \\le r \\le {d - 1}')} and sum!",
            [
                f"Since {m('N > 0')} and {m(f'0 \\le r < {d}')}, equal quotient and remainder {m('q = r')} forces {m(f'r \\in \\{{1, 2, \\dots, {d - 1}\\}}')}.",
                f"Each such integer has the form {m(f'N = {d}r + r = {d + 1}r')}.",
                f"Sum them all: {m(f'{d + 1} \\times (1 + 2 + \\dots + {d - 1}) = {d + 1} \\times {(d - 1) * d // 2} = {ans}')}.",
            ],
            f"There are {m(d - 1)} such integers ({m(f'{nums[0]}')} up to {m(f'{nums[-1]}')}), summing to {m(ans)}!",
            f"نكتب كل عدد يحقق الشرط على الصورة {m(f'N = {d}r + r = {d + 1}r')} حيث {m(f'1 \\le r \\le {d - 1}')}!",
            [
                f"بما أن العدد موجب والباقي أصغر من {m(d)}، فإن {m('r')} يأخذ القيم من {m(1)} إلى {m(d - 1)}.",
                f"المجموع يساوي {m(f'{d + 1} \\times \\frac{{({d - 1}) \\times {d}}}{{2}} = {ans}')}.",
            ],
            f"تحقق: الأعداد من {m(nums[0])} إلى {m(nums[-1])} مجموعها {m(ans)}!",
        )

    hard_crt = [
        (5, 3, 7, 2),
        (6, 5, 11, 4),
        (7, 4, 9, 6),
        (8, 5, 9, 2),
    ]
    for a, r1, b, r2 in hard_crt:
        ans = next(x for x in range(1, 1000) if x % a == r1 and x % b == r2)
        cands = [b * k + r2 for k in range(a) if b * k + r2 <= ans]
        B.add_math(
            tp, "Hard", bp,
            f"What is the **smallest** positive integer that leaves remainder {m(r1)} when divided by {m(a)} and remainder {m(r2)} when divided by {m(b)}?",
            f"ما **أصغر** عدد صحيح موجب يترك باقياً قدره {m(r1)} عند قسمته على {m(a)} ويترك باقياً قدره {m(r2)} عند قسمته على {m(b)}؟",
            ans, [ans + a * b, a * b - r1, ans - a if ans > a else ans + a, ans + b],
            f"List numbers that leave remainder {m(r2)} when divided by the larger divisor {m(b)}: {m(f'{r2}, {b + r2}, {2*b + r2}, \\dots')} and pick the first one that leaves remainder {m(r1)} mod {m(a)}!",
            f"اكتب الأعداد التي تترك الباقي {m(r2)} على المقسوم الأكبر {m(b)}: {m(f'{r2}, {b + r2}, {2*b + r2}, \\dots')} واختر أول عدد يحقق الشرط الأول!",
            f"Step through the arithmetic progression {m(f'{b}k + {r2}')} until {m(f'({b}k + {r2}) \\bmod {a} = {r1}')}!",
            [
                f"Numbers with remainder {m(r2)} upon division by {m(b)} are {m(', '.join(str(c) for c in cands))}.",
                f"Test each modulo {m(a)}: {m(ans)} is the very first one giving {m(f'{ans} = {a} \\times {ans // a} + {r1}')}.",
            ],
            f"Check both: {m(f'{ans} \\bmod {a} = {ans % a}')} and {m(f'{ans} \\bmod {b} = {ans % b}')}!",
            f"نسرد الأعداد التي تحقق شرط القسمة على {m(b)} أولاً لأن خطوتها أكبر!",
            [
                f"الأعداد من الصورة {m(f'{b}k + {r2}')} هي: {m(', '.join(str(c) for c in cands))}.",
                f"بفحص باقي قسمتها على {m(a)} نجد أن {m(ans)} هو أول عدد يعطي الباقي {m(r1)}.",
            ],
            f"تحقق: {m(f'{ans} = {a} \\times {ans // a} + {r1} = {b} \\times {ans // b} + {r2}')}!",
        )


# =============================================================================
# UNIT 1.2 — Fractions, Ratios & Cryptarithms (75 Qs)
# =============================================================================
def _add_unit_1_2(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 6. nsmo_g7_telescoping_unit_fractions (5E, 6M, 4H) — SVG: svg_number_strip on Easy & Hard
    bp = "nsmo_g7_telescoping_unit_fractions"
    easy_tele = [(1, 8), (1, 11), (2, 9), (3, 11), (4, 15)]
    for a, b in easy_tele:
        ans = sum(Fraction(1, k * (k + 1)) for k in range(a, b + 1))
        assert ans == Fraction(1, a) - Fraction(1, b + 1)
        B.add_math(
            tp, "Easy", bp,
            f"Evaluate the exact sum {m(f'\\frac{{1}}{{{a}\\times {a+1}}} + \\frac{{1}}{{{a+1}\\times {a+2}}} + \\dots + \\frac{{1}}{{{b}\\times {b+1}}}')}.",
            f"أوجد القيمة الدقيقة للمجموع {m(f'\\frac{{1}}{{{a}\\times {a+1}}} + \\frac{{1}}{{{a+1}\\times {a+2}}} + \\dots + \\frac{{1}}{{{b}\\times {b+1}}}')}.",
            ans, [Fraction(1, b + 1), Fraction(b, b + 1) if ans != Fraction(b, b + 1) else Fraction(b - 1, b + 1), ans + Fraction(1, b + 1), Fraction(1, a * (b + 1))],
            f"Rewrite each term using {m('\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}')} so middle terms cancel!",
            f"اكتب كل حد على الصورة {m('\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}')} لتختصر الحدود الوسطى!",
            f"Telescope the series using {m('\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}')}!",
            [
                f"Split every term: {m(f'\\left(\\frac{{1}}{{{a}}} - \\frac{{1}}{{{a+1}}}\\right) + \\left(\\frac{{1}}{{{a+1}}} - \\frac{{1}}{{{a+2}}}\\right) + \\dots + \\left(\\frac{{1}}{{{b}}} - \\frac{{1}}{{{b+1}}}\\right)')}.",
                f"All interior fractions cancel in pairs, leaving {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b+1}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Direct sum of all {m(b - a + 1)} fractions confirms {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            f"نفكك كل كسر إلى فرق كسرين فيبقى الحد الأول ناقص الأخير فقط!",
            [
                f"نكتب المجموع بصورة فروق متتالية من {m(f'\\frac{{1}}{{{a}}}')} حتى {m(f'\\frac{{1}}{{{b+1}}}')}.",
                f"تختفي الحدود الوسطى ويبقى {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b+1}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: المجموع الدقيق في أبسط صورة هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            diagram_en=svg_number_strip([f"1/{a}", f"−1/{a+1}", "+...", f"−1/{b+1}"]),
        )

    med_prod = [(2, 19), (3, 23), (4, 27)]
    for a, b in med_prod:
        ans = 1
        for k in range(a, b + 1):
            ans = ans * Fraction(k + 1, k)
        ans_int = int(ans) if ans.denominator == 1 else ans
        B.add_math(
            tp, "Medium", bp,
            f"Compute the exact value of the product {m(f'\\left(1 + \\frac{{1}}{{{a}}}\\right)\\left(1 + \\frac{{1}}{{{a+1}}}\\right)\\left(1 + \\frac{{1}}{{{a+2}}}\\right)\\cdots\\left(1 + \\frac{{1}}{{{b}}}\\right)')}.",
            f"احسب القيمة الدقيقة لحاصل الضرب {m(f'\\left(1 + \\frac{{1}}{{{a}}}\\right)\\left(1 + \\frac{{1}}{{{a+1}}}\\right)\\left(1 + \\frac{{1}}{{{a+2}}}\\right)\\cdots\\left(1 + \\frac{{1}}{{{b}}}\\right)')}.",
            ans_int, [b // a, (b + 1) * a, ans_int + 1 if isinstance(ans_int, int) else Fraction(b, a), ans_int - 1 if isinstance(ans_int, int) else Fraction(b + 2, a)],
            f"Turn each bracket into an improper fraction {m('\\frac{k+1}{k}')} and cancel diagonally!",
            f"حوّل كل قوس إلى كسر غير فعلي {m('\\frac{k+1}{k}')} ثم اختصر البسوط مع المقامات قطرياً!",
            f"Write {m('1 + \\frac{1}{k} = \\frac{k+1}{k}')} and cancel matching numerators and denominators!",
            [
                f"Rewrite the product as {m(f'\\frac{{{a+1}}}{{{a}}} \\times \\frac{{{a+2}}}{{{a+1}}} \\times \\dots \\times \\frac{{{b+1}}}{{{b}}}')}.",
                f"Every numerator from {m(a + 1)} to {m(b)} cancels the next denominator, leaving {m(f'\\frac{{{b+1}}}{{{a}}} = {ans_int}')}.",
            ],
            f"Check: {m(f'({b} + 1) / {a} = {ans_int}')}!",
            f"نكتب كل قوس بصورة {m('\\frac{k+1}{k}')} فتختصر العوامل المتتالية!",
            [
                f"يتحول الجداء إلى {m(f'\\frac{{{a+1}}}{{{a}}} \\times \\frac{{{a+2}}}{{{a+1}}} \\times \\dots \\times \\frac{{{b+1}}}{{{b}}}')}.",
                f"يبقى آخر بسط على أول مقام: {m(f'\\frac{{{b+1}}}{{{a}}} = {ans_int}')}.",
            ],
            f"تحقق: الناتج يساوي {m(ans_int)} بالضبط!",
        )

    med_odd_tele = [6, 8, 10]
    for n in med_odd_tele:
        last_a, last_b = 2 * n - 1, 2 * n + 1
        ans = sum(Fraction(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, n + 1))
        assert ans == Fraction(n, 2 * n + 1)
        B.add_math(
            tp, "Medium", bp,
            f"Find the exact value of {m(f'\\frac{{1}}{{1\\times 3}} + \\frac{{1}}{{3\\times 5}} + \\frac{{1}}{{5\\times 7}} + \\dots + \\frac{{1}}{{{last_a}\\times {last_b}}}')}.",
            f"أوجد القيمة الدقيقة للمجموع {m(f'\\frac{{1}}{{1\\times 3}} + \\frac{{1}}{{3\\times 5}} + \\frac{{1}}{{5\\times 7}} + \\dots + \\frac{{1}}{{{last_a}\\times {last_b}}}')}.",
            ans, [Fraction(2 * n, 2 * n + 1), Fraction(1, 2 * n + 1), Fraction(n, 2 * n - 1), Fraction(n + 1, 2 * n + 1)],
            f"Watch the gap of {m(2)} in the denominator: {m('\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}!",
            f"انتبه لفرق الـ {m(2)} في المقام: {m('\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}!",
            f"Factor out {m('\\frac{1}{2}')} before telescoping!",
            [
                f"Use {m('\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')} on all {m(n)} terms.",
                f"After inner cancellation, we get {m(f'\\frac{{1}}{{2}}\\left(1 - \\frac{{1}}{{{last_b}}}\\right) = \\frac{{1}}{{2}} \\times \\frac{{{2*n}}}{{{last_b}}} = \\frac{{{n}}}{{{last_b}}}')}.",
            ],
            f"Trap avoided: forgetting the {m('\\frac{1}{2}')} factor would double the answer to {m(f'\\frac{{{2*n}}}{{{last_b}}}')}!",
            f"نخرج العامل {m('\\frac{1}{2}')} خارج القوس ثم نختصر الحدود المتداخلة!",
            [
                f"كل حد يساوي {m('\\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}.",
                f"بعد الاختصار نحصل على {m(f'\\frac{{1}}{{2}}\\left(1 - \\frac{{1}}{{{last_b}}}\\right) = \\frac{{{n}}}{{{last_b}}}')}.",
            ],
            f"تحقق: ضرب الناتج في {m('\\frac{1}{2}')} يعطي {m(f'\\frac{{{n}}}{{{last_b}}}')}!",
        )

    hard_sq_prod = [9, 11, 15, 19]
    for n in hard_sq_prod:
        ans = Fraction(1, 1)
        for k in range(2, n + 1):
            ans *= Fraction(k * k - 1, k * k)
        assert ans == Fraction(n + 1, 2 * n)
        B.add_math(
            tp, "Hard", bp,
            f"Evaluate the product {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{n}^2}}\\right)')}.",
            f"احسب قيمة الجداء {m(f'\\left(1 - \\frac{{1}}{{2^2}}\\right)\\left(1 - \\frac{{1}}{{3^2}}\\right)\\left(1 - \\frac{{1}}{{4^2}}\\right)\\cdots\\left(1 - \\frac{{1}}{{{n}^2}}\\right)')}.",
            ans, [Fraction(n - 1, 2 * n), Fraction(n + 1, n), Fraction(1, n), Fraction(n, 2 * n + 1)],
            f"Factor each bracket using difference of squares: {m('1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}!",
            f"حلّل كل قوس بفرق المربعين: {m('1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}!",
            f"Split into two telescoping products: {m('\\prod \\frac{k-1}{k}')} and {m('\\prod \\frac{k+1}{k}')}!",
            [
                f"Write {m('1 - \\frac{1}{k^2} = \\frac{(k-1)(k+1)}{k^2} = \\frac{k-1}{k} \\times \\frac{k+1}{k}')}.",
                f"The first chain {m(f'\\frac{{1}}{{2}} \\times \\frac{{2}}{{3}} \\times \\dots \\times \\frac{{{n-1}}}{{{n}}}')} collapses to {m(f'\\frac{{1}}{{{n}}}')}.",
                f"The second chain {m(f'\\frac{{3}}{{2}} \\times \\frac{{4}}{{3}} \\times \\dots \\times \\frac{{{n+1}}}{{{n}}}')} collapses to {m(f'\\frac{{{n+1}}}{{2}}')}. Multiplying gives {m(f'\\frac{{{n+1}}}{{{2*n}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Small check for {m('n=2')}: {m('\\frac{2+1}{4} = \\frac{3}{4} = 1 - \\frac{1}{4}')}; here we get {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            f"نفكك كل قوس إلى {m('\\frac{k-1}{k} \\times \\frac{k+1}{k}')} فنحصل على جداءين متداخلين!",
            [
                f"الجداء الأول يختصر إلى {m(f'\\frac{{1}}{{{n}}}')} والجداء الثاني يختصر إلى {m(f'\\frac{{{n+1}}}{{2}}')}.",
                f"بضربهما معاً نحصل على {m(f'\\frac{{{n+1}}}{{{2*n}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: الكسر في أبسط صورة هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            diagram_en=svg_number_strip(["(k−1)/k", "×", "(k+1)/k", "=", f"{ans.numerator}/{ans.denominator}"]),
        )

    # 7. nsmo_g7_remainder_fraction_chain (5E, 6M, 4H) — SVG: svg_fraction_grid
    bp = "nsmo_g7_remainder_fraction_chain"
    easy_rem_f = [
        (1, 4, 1, 3, 24, "pages of a novel", "صفحة من رواية"),
        (1, 3, 2, 5, 18, "dates from a basket", "تمرة من سلة"),
        (2, 5, 1, 2, 21, "riyals of his allowance", "ريالاً من مصروفه"),
        (1, 5, 3, 8, 30, "liters of water in a tank", "لتراً من الماء في خزان"),
        (3, 7, 1, 4, 27, "kilometers of a desert trail", "كيلومتراً من مسار بري"),
    ]
    for n1, d1, n2, d2, left_v, item_en, item_ar in easy_rem_f:
        f_left = (1 - Fraction(n1, d1)) * (1 - Fraction(n2, d2))
        tot = left_v / f_left
        assert tot.denominator == 1
        ans = int(tot)
        B.add_math(
            tp, "Easy", bp,
            f"Lina completed {m(f'\\frac{{{n1}}}{{{d1}}}')} of the {item_en} on Friday, and {m(f'\\frac{{{n2}}}{{{d2}}}')} of the **remaining** amount on Saturday. If {m(left_v)} {item_en} still remain, what was the original total?",
            f"أنهت لينا {m(f'\\frac{{{n1}}}{{{d1}}}')} من المجموع الكلي يوم الجمعة، ثم أنهت {m(f'\\frac{{{n2}}}{{{d2}}}')} من **المتبقي** يوم السبت. إذا بقي {m(left_v)} {item_ar}، فكم كان العدد الكلي أصلاً؟",
            ans, [ans - left_v, ans + d1 * d2, int(left_v * d1), ans // 2],
            f"Multiply the fractions that **stay** untouched: {m(f'\\left(1 - \\frac{{{n1}}}{{{d1}}}\\right)\\left(1 - \\frac{{{n2}}}{{{d2}}}\\right)')}!",
            f"اضرب الكسور **المتبقية** بعد كل خطوة: {m(f'\\left(1 - \\frac{{{n1}}}{{{d1}}}\\right)\\left(1 - \\frac{{{n2}}}{{{d2}}}\\right)')}!",
            f"Compute the surviving fraction {m(f'(1 - \\frac{{{n1}}}{{{d1}}})(1 - \\frac{{{n2}}}{{{d2}}})')} and equate it to {m(left_v)}!",
            [
                f"After Friday, {m(f'1 - \\frac{{{n1}}}{{{d1}}} = \\frac{{{d1 - n1}}}{{{d1}}}')} of the total remains.",
                f"After Saturday, {m(f'\\frac{{{d1 - n1}}}{{{d1}}} \\times \\frac{{{d2 - n2}}}{{{d2}}} = \\frac{{{f_left.numerator}}}{{{f_left.denominator}}}')} of the total remains.",
                f"Setting {m(f'\\frac{{{f_left.numerator}}}{{{f_left.denominator}}} T = {left_v}')} gives {m(f'T = {ans}')}.",
            ],
            f"Forward check: {m(ans)} minus {m(ans * n1 // d1)} leaves {m(ans * (d1 - n1) // d1)}, then keeping {m(f'\\frac{{{d2 - n2}}}{{{d2}}}')} leaves {m(left_v)}!",
            f"نضرب الكسرين المتبقيين بعد يومي الجمعة والسبت ونساوي الناتج بالمتبقي {m(left_v)}!",
            [
                f"يتبقى بعد الجمعة {m(f'\\frac{{{d1 - n1}}}{{{d1}}}')}، ويتبقى منه بعد السبت {m(f'\\frac{{{d2 - n2}}}{{{d2}}}')}.",
                f"الكسر المتبقي النهائي هو {m(f'\\frac{{{f_left.numerator}}}{{{f_left.denominator}}}')} ويقابل {m(left_v)}.",
                f"إذن المجموع الأصلي = {m(ans)}.",
            ],
            f"تحقق أمامي: بدءاً من {m(ans)} يتبقى في النهاية {m(left_v)} بالضبط!",
            diagram_en=svg_fraction_grid(d1, d2 if d2 <= 6 else 4, n1 * 2, n2),
        )

    med_rem3 = [
        (1, 4, 1, 3, 1, 2, 15),
        (1, 5, 1, 4, 1, 3, 24),
        (1, 3, 1, 4, 2, 5, 18),
        (2, 5, 1, 3, 1, 4, 27),
        (1, 6, 1, 5, 1, 4, 30),
        (1, 4, 2, 5, 1, 3, 21),
    ]
    for n1, d1, n2, d2, n3, d3, rem_v in med_rem3:
        fl = (1 - Fraction(n1, d1)) * (1 - Fraction(n2, d2)) * (1 - Fraction(n3, d3))
        tot = rem_v / fl
        assert tot.denominator == 1
        ans = int(tot)
        B.add_math(
            tp, "Medium", bp,
            f"A courier delivers {m(f'\\frac{{{n1}}}{{{d1}}}')} of a crate of parcels in District 1, then {m(f'\\frac{{{n2}}}{{{d2}}}')} of the remainder in District 2, and then {m(f'\\frac{{{n3}}}{{{d3}}}')} of the new remainder in District 3. If {m(rem_v)} parcels are left, how many parcels started in the crate?",
            f"وزّع مندوب {m(f'\\frac{{{n1}}}{{{d1}}}')} من صندوق طرود في الحي الأول، ثم {m(f'\\frac{{{n2}}}{{{d2}}}')} من المتبقي في الحي الثاني، ثم {m(f'\\frac{{{n3}}}{{{d3}}}')} من المتبقي الجديد في الحي الثالث. إذا بقي {m(rem_v)} طرداً، فكم طرداً كان في الصندوق في البداية؟",
            ans, [ans - rem_v, ans + 20, ans // 2, ans + 15],
            f"Chain all three surviving fractions: {m(f'\\left(1-\\frac{{{n1}}}{{{d1}}}\\right)\\left(1-\\frac{{{n2}}}{{{d2}}}\\right)\\left(1-\\frac{{{n3}}}{{{d3}}}\\right)')}!",
            f"اضرب الكسور الثلاثة المتبقية متتاليةً واختصر البسوط مع المقامات!",
            f"Multiply the three remaining fractions—notice how cleanly they telescope—and solve for the initial total!",
            [
                f"Remaining fractions are {m(f'\\frac{{{d1-n1}}}{{{d1}}}')}, {m(f'\\frac{{{d2-n2}}}{{{d2}}}')}, and {m(f'\\frac{{{d3-n3}}}{{{d3}}}')}.",
                f"Their product simplifies to {m(f'\\frac{{{fl.numerator}}}{{{fl.denominator}}}')} of the initial crate.",
                f"Since {m(f'\\frac{{{fl.numerator}}}{{{fl.denominator}}} T = {rem_v}')}, we get {m(f'T = {ans}')} parcels.",
            ],
            f"Check: {m(f'\\frac{{{fl.numerator}}}{{{fl.denominator}}} \\times {ans} = {rem_v}')} parcels left!",
            f"نضرب الكسور المتبقية بعد الأحياء الثلاثة ونختصر!",
            [
                f"حاصل ضرب الكسور المتبقية {m(f'\\frac{{{d1-n1}}}{{{d1}}} \\times \\frac{{{d2-n2}}}{{{d2}}} \\times \\frac{{{d3-n3}}}{{{d3}}} = \\frac{{{fl.numerator}}}{{{fl.denominator}}}')}.",
                f"بمساواته بالمتبقي {m(rem_v)} نجد أن العدد الأصلي = {m(ans)} طرداً.",
            ],
            f"تحقق: {m(f'{ans} \\times \\frac{{{fl.numerator}}}{{{fl.denominator}}} = {rem_v}')}!",
            diagram_en=svg_fraction_grid(5, 4, 8, 4),
        )

    hard_back = [
        (2, 3, 5),   # ((T/2 - 2)/2 - 3) = 5 -> T/2 - 2 = 16 -> T = 36
        (4, 2, 7),   # (7+2)*2 = 18 -> (18+4)*2 = 44
        (3, 5, 4),   # (4+5)*2 = 18 -> (18+3)*2 = 42
        (1, 4, 6),   # (6+4)*2 = 20 -> (20+1)*2 = 42? Wait make distinct ans: (6, 4, 6) -> (10)*2=20 -> (26)*2=52!
    ]
    hard_back = [(2, 3, 5), (4, 2, 7), (3, 5, 4), (6, 4, 6)]
    for e1, e2, final_v in hard_back:
        after1 = (final_v + e2) * 2
        ans = (after1 + e1) * 2
        assert ((ans // 2 - e1) // 2 - e2) == final_v
        B.add_math(
            tp, "Hard", bp,
            f"Tariq gave away **half** of his stickers **plus {m(e1)} more** to his brother, and then gave **half** of what remained **plus {m(e2)} more** to his cousin, leaving himself with {m(final_v)} stickers. How many stickers did Tariq have at first?",
            f"أعطى طارق أخاه **نصف** ما معه من الملصقات **وزيادة {m(e1)}**، ثم أعطى ابن عمه **نصف** ما تبقى معه **وزيادة {m(e2)}**، فبقي معه {m(final_v)} ملصقات. كم ملصقاً كان مع طارق في البداية؟",
            ans, [ans - 2 * e1, final_v * 4 + e1 + e2, after1 * 2, ans + 8],
            f"Work **backward** from the {m(final_v)} stickers at the end: add {m(e2)} before doubling, then add {m(e1)} before doubling again!",
            f"اعمل **عكسياً** من النهاية ({m(final_v)} ملصقات): أضف {m(e2)} قبل المضاعفة الأولى، ثم أضف {m(e1)} قبل المضاعفة الثانية!",
            f"Reverse each operation in opposite order from the final {m(final_v)} stickers!",
            [
                f"Before giving the extra {m(e2)} stickers to his cousin, half of the first remainder equaled {m(f'{final_v} + {e2} = {final_v + e2}')}, so the first remainder was {m(f'2 \\times {final_v + e2} = {after1}')}.",
                f"Before giving the extra {m(e1)} stickers to his brother, half of the starting total equaled {m(f'{after1} + {e1} = {after1 + e1}')}.",
                f"Doubling gives {m(f'2 \\times {after1 + e1} = {ans}')} stickers originally.",
            ],
            f"Forward check: {m(f'{ans}/2 - {e1} = {after1}')}, then {m(f'{after1}/2 - {e2} = {final_v}')}!",
            f"نرجع خطوة بخطوة من النهاية بعكس العمليات الحسابية!",
            [
                f"قبل إعطاء الـ {m(e2)} الإضافية كان نصف المتبقي يساوي {m(final_v + e2)}، أي المتبقي الأول = {m(after1)}.",
                f"قبل إعطاء الـ {m(e1)} الإضافية كان نصف العدد الأصلي يساوي {m(after1 + e1)}، أي العدد الأصلي = {m(ans)}.",
            ],
            f"تحقق للأمام: {m(f'{ans} \\to {after1} \\to {final_v}')} ملصقات!",
            diagram_en=svg_fraction_grid(4, 4, 4, 2),
        )

    # 8. nsmo_g7_invariant_ratio_mixture (5E, 6M, 4H) — SVG: svg_two_jars
    bp = "nsmo_g7_invariant_ratio_mixture"
    easy_mix = [
        (2, 3, 12, 1, 3),  # 2:3 -> 2:6 (+3u = 12 -> u=4 -> first=8)
        (3, 5, 14, 1, 4),  # 3:5 -> 3:12 (+7u = 14 -> u=2 -> first=6)
        (4, 3, 20, 4, 7),  # 4:3 -> 4:7 (+4u = 20 -> u=5 -> first=20)
        (5, 2, 18, 5, 8),  # 5:2 -> 5:8 (+6u = 18 -> u=3 -> first=15)
        (3, 2, 15, 2, 3),  # 6:4 -> 6:9 (+5u = 15 -> u=3 -> first=18)
    ]
    for a, b, add_w, c, d in easy_mix:
        g_anc = math.lcm(a, c)
        s1, s2 = g_anc // a, g_anc // c
        b_old, b_new = b * s1, d * s2
        unit_v = add_w // (b_new - b_old)
        ans = g_anc * unit_v
        assert Fraction(ans, b_old * unit_v + add_w) == Fraction(c, d)
        B.add_math(
            tp, "Easy", bp,
            f"A pitcher contains lemon juice and water in the ratio {m(f'{a} : {b}')}. After {m(add_w)} cups of **water** (and no lemon juice) are added, the ratio becomes {m(f'{c} : {d}')}. How many cups of **lemon juice** are in the pitcher?",
            f"يحتوي إبريق على عصير ليمون وماء بنسبة {m(f'{a} : {b}')}. بعد إضافة {m(add_w)} كوباً من **الماء فقط** أصبحت النسبة {m(f'{c} : {d}')}. كم كوباً من **عصير الليمون** في الإبريق؟",
            ans, [b_old * unit_v, ans + unit_v * 2, b_new * unit_v, ans // 2 if ans % 2 == 0 else ans + 3],
            f"Lemon juice **never changed**! Scale both ratios so the lemon-juice part equals {m(g_anc)} units.",
            f"كمية عصير الليمون **لم تتغير**! وحِّد حصة الليمون في النسبتين عند {m(g_anc)} وحدات.",
            f"Anchor the unchanged lemon juice at {m(g_anc)} ratio units!",
            [
                f"Write {m(f'{a}:{b} = {g_anc}:{b_old}')} and {m(f'{c}:{d} = {g_anc}:{b_new}')} so lemon juice stays at {m(g_anc)} units.",
                f"Water rose by {m(f'{b_new} - {b_old} = {b_new - b_old}')} units, which equals {m(add_w)} cups, so {m(f'1\\text{{ unit}} = {unit_v}')} cups.",
                f"Lemon juice = {m(f'{g_anc} \\times {unit_v} = {ans}')} cups.",
            ],
            f"Check: {m(ans)} lemon and {m(b_old * unit_v)} water ({m(f'{a}:{b}')}) plus {m(add_w)} water gives {m(ans)} to {m(b_new * unit_v)} ({m(f'{c}:{d}')})!",
            f"نثبّت حصة عصير الليمون عند {m(g_anc)} وحدات في النسبتين!",
            [
                f"النسبة الأولى تصبح {m(f'{g_anc}:{b_old}')} والثانية تصبح {m(f'{g_anc}:{b_new}')}.",
                f"زيادة الماء = {m(b_new - b_old)} وحدات تقابل {m(add_w)} كوباً، فالوحدة = {m(unit_v)}.",
                f"كمية عصير الليمون = {m(f'{g_anc} \\times {unit_v} = {ans}')} كوباً.",
            ],
            f"تحقق: {m(f'{ans} : {b_new * unit_v} = {c} : {d}')}!",
            diagram_en=svg_two_jars(f"{a}:{b}", 0.5, f"{c}:{d}", 0.78, f"+{add_w}"),
        )

    med_conc = [
        (300, 20, 12),   # salt=60 -> new total = 500 -> +200 mL water
        (240, 25, 15),   # salt=60 -> new total = 400 -> +160 mL water
        (400, 15, 10),   # salt=60 -> new total = 600 -> +200? Wait distinct stems/values: 200 ok, let's check
        (350, 30, 21),   # salt=105 -> new total = 500 -> +150 mL water
        (180, 40, 24),   # salt=72 -> new total = 300 -> +120 mL water
        (450, 16, 12),   # salt=72 -> new total = 600 -> +150 mL water
    ]
    for V, p1, p2 in med_conc:
        salt = V * p1 // 100
        V_new = salt * 100 // p2
        ans = V_new - V
        assert salt * 100 == V_new * p2
        B.add_math(
            tp, "Medium", bp,
            f"A beaker holds {m(V)} mL of a {m(f'{p1}\\%')} saline solution. How many milliliters of **pure water** must be added to dilute it into a {m(f'{p2}\\%')} saline solution?",
            f"يحتوي دورق على {m(V)} مل من محلول ملحي تركيزه {m(f'{p1}\\%')}. كم ملليلتراً من **الماء النقي** يجب إضافته لتخفيف المحلول إلى تركيز {m(f'{p2}\\%')}؟",
            ans, [V_new, salt, ans + 50, abs(V - ans) if abs(V - ans) != ans else ans + 30],
            f"Pure water adds **zero salt**! Compute the grams of salt ({m(f'{p1}\\%')} of {m(V)}), which must equal {m(f'{p2}\\%')} of the new total volume.",
            f"الماء النقي لا يضيف أي ملح! احسب كمية الملح الثابتة ({m(f'{p1}\\%')} من {m(V)}) واجعلها تساوي {m(f'{p2}\\%')} من الحجم الجديد.",
            f"Anchor the unchanged amount of pure salt at {m(salt)} units!",
            [
                f"Amount of salt in the beaker is {m(f'\\frac{{{p1}}}{{100}} \\times {V} = {salt}')} mL-equivalents, and this stays constant.",
                f"In the diluted {m(f'{p2}\\%')} solution, {m(f'\\frac{{{p2}}}{{100}} \\times V_{{\\text{{new}}}} = {salt} \\implies V_{{\\text{{new}}}} = {V_new}')} mL.",
                f"Pure water added = {m(f'{V_new} - {V} = {ans}')} mL.",
            ],
            f"Check: {m(f'{salt} / ({V} + {ans}) = {salt} / {V_new} = {p2}\\%')}!",
            f"نحسب كمية الملح الثابتة أولاً ثم نقسمها على النسبة الجديدة لإيجاد الحجم الجديد!",
            [
                f"كمية الملح الثابتة تساوي {m(f'\\frac{{{p1}}}{{100}} \\times {V} = {salt}')}.",
                f"الحجم الكلي الجديد بعد التخفيف = {m(f'{salt} \\times \\frac{{100}}{{{p2}}} = {V_new}')} مل.",
                f"كمية الماء المضاف = {m(f'{V_new} - {V} = {ans}')} مل.",
            ],
            f"تحقق: {m(f'\\frac{{{salt}}}{{{V_new}}} = {p2}\\%')}!",
            diagram_en=svg_two_jars(f"{p1}%", 0.52, f"{p2}%", 0.80, "+Water"),
        )

    hard_eq_jars = [
        (1, 2, 3, 2),   # lcm(3,5)=15 -> (5:10) + (9:6) = 14:16 = 7:8 -> frac gold = 7/15
        (1, 3, 2, 3),   # lcm(4,5)=20 -> (5:15) + (8:12) = 13:27 -> frac = 13/40
        (2, 3, 5, 3),   # lcm(5,8)=40 -> (16:24) + (25:15) = 41:39 -> frac = 41/80
        (1, 4, 1, 2),   # lcm(5,3)=15 -> (3:12) + (5:10) = 8:22 = 4:11 -> frac = 4/15
    ]
    for a1, b1, a2, b2 in hard_eq_jars:
        s1, s2 = a1 + b1, a2 + b2
        V = math.lcm(s1, s2)
        g1, g2 = a1 * (V // s1), a2 * (V // s2)
        ans = Fraction(g1 + g2, 2 * V)
        B.add_math(
            tp, "Hard", bp,
            f"Two **identical-volume** bottles are completely full of syrup-and-water mixtures: Bottle 1 has syrup to water in ratio {m(f'{a1}:{b1}')}, and Bottle 2 has syrup to water in ratio {m(f'{a2}:{b2}')}. When both bottles are poured into one large jug, what **fraction** of the combined mixture is syrup?",
            f"قارورتان **متساويتان تماماً في السعة** مملوءتان بمزيج من الشراب المركز والماء: النسبة في الأولى {m(f'{a1}:{b1}')} وفي الثانية {m(f'{a2}:{b2}')}. عند إفراغ القارورتين معاً في وعاء كبير، ما **الكسر** الذي يمثله الشراب المركز من المزيج الكلي؟",
            ans, [Fraction(a1 + a2, s1 + s2), Fraction(1, 2), Fraction(ans.denominator - ans.numerator, ans.denominator), Fraction(a1 + a2, 2 * max(s1, s2))],
            f"Do **not** add {m(f'{a1}+{a2}')} over {m(f'{s1}+{s2}')}! Give both bottles the same common volume {m(f'\\operatorname{{lcm}}({s1}, {s2}) = {V}')} units first!",
            f"لا تجمع البسوط والمقامات مباشرة! اجعل سعة كل قارورة {m(f'\\operatorname{{lcm}}({s1}, {s2}) = {V}')} وحدة أولاً!",
            f"Equalize both bottle capacities to {m(V)} units before combining!",
            [
                f"Bottle 1 has {m(s1)} parts and Bottle 2 has {m(s2)} parts; choose each bottle's volume to be {m(f'\\operatorname{{lcm}}({s1}, {s2}) = {V}')} units.",
                f"Syrup in Bottle 1 is {m(f'\\frac{{{a1}}}{{{s1}}} \\times {V} = {g1}')} units, and in Bottle 2 is {m(f'\\frac{{{a2}}}{{{s2}}} \\times {V} = {g2}')} units.",
                f"Combined jug has {m(f'{g1} + {g2} = {g1 + g2}')} syrup units out of {m(2 * V)} total units, giving {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Average of fractions check: {m(f'\\frac{{1}}{{2}}\\left(\\frac{{{a1}}}{{{s1}}} + \\frac{{{a2}}}{{{s2}}}\\right) = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            f"نوحّد سعة القارورتين عند {m(V)} وحدة ثم نجمع حصص الشراب المركز!",
            [
                f"في القارورة الأولى {m(g1)} وحدات شراب من {m(V)}، وفي الثانية {m(g2)} وحدات شراب من {m(V)}.",
                f"المزيج الكلي يحوي {m(g1 + g2)} وحدة شراب من أصل {m(2 * V)}، أي {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: متوسط الكسرين يساوي {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')} بالضبط!",
            diagram_en=svg_two_jars(f"{a1}:{b1}", 0.85, f"{a2}:{b2}", 0.85, "Mix"),
        )

    # 9. nsmo_g7_column_cryptarithm (5E, 6M, 4H) — SVG: svg_column_cryptarithm
    bp = "nsmo_g7_column_cryptarithm"
    easy_crypt = [99, 121, 132, 154, 176]
    for S in easy_crypt:
        ans = S // 11
        B.add_math(
            tp, "Easy", bp,
            f"In the column addition {m(f'\\overline{{AB}} + \\overline{{BA}} = {S}')}, {m('A')} and {m('B')} are non-zero digits. What is the value of {m('A + B')}?",
            f"في عملية الجمع العمودي {m(f'\\overline{{AB}} + \\overline{{BA}} = {S}')}، حيث {m('A')} و{m('B')} رقمان غير صفريين، ما قيمة {m('A + B')}؟",
            ans, [ans - 2, ans + 1, ans + 3, S % 10 + (S // 10) % 10],
            f"Expand by place value: {m('(10A + B) + (10B + A) = 11(A + B)')}!",
            f"فكّك بالقيمة المكانية: {m('(10A + B) + (10B + A) = 11(A + B)')}!",
            f"Factor {m('\\overline{AB} + \\overline{BA} = 11(A + B)')} and divide {m(S)} by {m(11)}!",
            [
                f"Using place value, {m('\\overline{AB} + \\overline{BA} = 10A + B + 10B + A = 11(A + B)')}.",
                f"Divide {m(S)} by {m(11)}: {m(f'A + B = {S} \\div 11 = {ans}')}.",
            ],
            f"Check: {m(f'11 \\times {ans} = {S}')}!",
            f"نستخدم المتطابقة المكانية {m('\\overline{AB} + \\overline{BA} = 11(A + B)')}!",
            [
                f"بفك القيمة المكانية نحصل على {m(f'11(A + B) = {S}')}.",
                f"بقسمة الطرفين على {m(11)} نجد {m(f'A + B = {ans}')}.",
            ],
            f"تحقق: {m(f'11 \\times {ans} = {S}')}!",
            diagram_en=svg_column_cryptarithm(["AB", "BA"], str(S)),
        )

    med_crypt = [
        # AB + AB + AB = 1B4 -> 3*(10A+B) = 104 + 10B -> 30A - 7B = 104 -> A=4, B=16/7 no; let's generate exact verified tuples!
        ("AB", "AB", 156, 78),   # 2*AB = 156 -> AB=78 -> A+B=15
        ("AB", "BC", 149, 13),   # wait: make 100% unique-solution cryptarithms!
    ]
    # Programmatically verified unique-solution 2-addend / 3-addend cryptarithms:
    med_specs = [
        # (addends_display, total_str, question_en, question_ar, ans, explain_line_en, explain_line_ar)
        (["AB", "B7"], "93", f"In the column addition {m('\\overline{AB} + \\overline{B7} = 93')}, {m('A')} and {m('B')} are digits. Find the two-digit number {m('\\overline{AB}')}.",
         f"في عملية الجمع العمودي {m('\\overline{AB} + \\overline{B7} = 93')}، حيث {m('A')} و{m('B')} رقمان، أوجد العدد {m('\\overline{AB}')}.",
         36, f"Units column {m('B + 7')} ends in {m(3)}, forcing {m('B = 6')} (carry {m(1)}), then tens column {m('A + 6 + 1 = 9 \\implies A = 2')}? Wait check!", ""),
    ]
    # Let's compute exact verified medium cryptarithms via Python assertions!
    med_verified = [
        (7, 93),   # AB + B7 = 93 -> 10A + B + 10B + 7 = 93 -> 10A + 11B = 86 -> B=6, A=2 -> AB=26!
        (8, 82),   # AB + B8 = 82 -> 10A + 11B = 74 -> B=4, A=3 -> AB=34!
        (6, 94),   # AB + B6 = 94 -> 10A + 11B = 88 -> B=8, A=0 disallowed (A>=1)! Try (6, 103): 10A+11B=97 -> B=7, A=2 -> AB=27!
        (9, 114),  # AB + B9 = 114 -> 10A + 11B = 105 -> B=5, A=5; try (9, 122): 10A+11B=113 -> B=3, A=8 -> AB=83!
        (4, 133),  # AB + B4 = 133 -> 10A + 11B = 129 -> B=9, A=3 -> AB=39!
        (5, 117),  # AB + B5 = 117 -> 10A + 11B = 112 -> B=2, A=9 -> AB=92!
    ]
    med_verified = [(7, 93), (8, 82), (6, 103), (9, 122), (4, 133), (5, 117)]
    for u_fixed, tot_s in med_verified:
        sols = [(a, b) for a in range(1, 10) for b in range(1, 10) if (10 * a + b) + (10 * b + u_fixed) == tot_s]
        assert len(sols) == 1, (u_fixed, tot_s, sols)
        A, B_d = sols[0]
        ans = 10 * A + B_d
        B.add_math(
            tp, "Medium", bp,
            f"In the column addition {m(f'\\overline{{AB}} + \\overline{{B{u_fixed}}} = {tot_s}')}, {m('A')} and {m('B')} are non-zero digits. Find the two-digit number {m('\\overline{AB}')}.",
            f"في عملية الجمع العمودي {m(f'\\overline{{AB}} + \\overline{{B{u_fixed}}} = {tot_s}')}، حيث {m('A')} و{m('B')} رقمان غير صفريين، أوجد العدد المكوّن من رقمين {m('\\overline{AB}')}.",
            ans, [10 * B_d + A, ans + 10, ans - 9, ans + 11],
            f"Look at the **units column** first: {m(f'B + {u_fixed}')} must have units digit {m(tot_s % 10)}, which pins down {m('B')} and the carry!",
            f"ابدأ بـ **عمود الآحاد** أولاً: {m(f'B + {u_fixed}')} آحاده {m(tot_s % 10)}، مما يحدد قيمة {m('B')} واليد المحمولة فوراً!",
            f"Solve the units column {m(f'B + {u_fixed} \\equiv {tot_s % 10} \\pmod{{10}}')} first, then track the carry to find {m('A')}!",
            [
                f"In the ones column, {m(f'B + {u_fixed}')} ends in {m(tot_s % 10)}, forcing {m(f'B = {B_d}')} (since {m(f'{B_d} + {u_fixed} = {B_d + u_fixed}')}).",
                f"Now substitute {m(f'B = {B_d}')} into {m(f'\\overline{{A{B_d}}} + {10 * B_d + u_fixed} = {tot_s}')}: {m(f'\\overline{{A{B_d}}} = {tot_s} - {10 * B_d + u_fixed} = {ans}')}, so {m(f'A = {A}')}.",
            ],
            f"Check: {m(f'{ans} + {10 * B_d + u_fixed} = {tot_s}')}!",
            f"نحل خانة الآحاد أولاً لتحديد {m('B')} ثم نعوّض لإيجاد {m('A')}!",
            [
                f"من خانة الآحاد: {m(f'B + {u_fixed}')} يعطي آحاداً قدره {m(tot_s % 10)}، إذن {m(f'B = {B_d}')}.",
                f"بالتعويض: {m(f'\\overline{{AB}} = {tot_s} - {10 * B_d + u_fixed} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} + {10 * B_d + u_fixed} = {tot_s}')}!",
            diagram_en=svg_column_cryptarithm(["AB", f"B{u_fixed}"], str(tot_s)),
        )

    # Hard (4): 3-digit distinct-digit cryptarithms verified by brute force!
    # 1) ABC + ABC + ABC = BBB -> 148 + 148 + 148 = 444 (ans = 148)
    assert [(a, b, c) for a in range(1, 10) for b in range(1, 10) for c in range(10)
            if len({a, b, c}) == 3 and 3 * (100 * a + 10 * b + c) == 111 * b] == [(1, 4, 8)]
    B.add_math(
        tp, "Hard", bp,
        f"In the column addition {m('\\overline{ABC} + \\overline{ABC} + \\overline{ABC} = \\overline{BBB}')}, distinct letters represent distinct digits with {m('A, B \\ne 0')}. Find the 3-digit number {m('\\overline{ABC}')}.",
        f"في عملية الجمع العمودي {m('\\overline{ABC} + \\overline{ABC} + \\overline{ABC} = \\overline{BBB}')}، تمثل الحروف المختلفة أرقاماً مختلفة مع {m('A, B \\ne 0')}. أوجد العدد الثلاثي {m('\\overline{ABC}')}.",
        148, [185, 259, 137, 296],
        f"Notice {m('\\overline{BBB} = 111B = 3 \\times 37B')}, so {m('\\overline{ABC} = 37B')}!",
        f"لاحظ أن {m('\\overline{BBB} = 111B = 3 \\times 37B')}، أي أن {m('\\overline{ABC} = 37B')}!",
        f"Divide both sides by {m(3)} using {m('111 = 3 \\times 37')}!",
        [
            f"Rewrite the equation as {m('3 \\times \\overline{ABC} = 111B')}, and divide by {m(3)} to get {m('\\overline{ABC} = 37B')}.",
            f"We need the tens digit of {m('37B')} to equal {m('B')} itself with distinct digits {m('A, B, C')}.",
            f"Testing {m('B = 4')} gives {m('37 \\times 4 = 148')}, whose middle digit is indeed {m(4)}!",
        ],
        f"Check: {m('148 + 148 + 148 = 444')}, with distinct digits {m('A=1, B=4, C=8')}!",
        f"نقسم الطرفين على {m(3)} مستفيدين من أن {m('111 = 3 \\times 37')}!",
        [
            f"من المعادلة {m('3 \\times \\overline{ABC} = 111B')} نستنتج أن {m('\\overline{ABC} = 37B')}.",
            f"بتجربة قيم {m('B')} نجد عند {m('B = 4')} أن {m('37 \\times 4 = 148')} ورقم عشراته {m(4)} فعلاً!",
        ],
        f"تحقق: {m('148 + 148 + 148 = 444')}!",
        diagram_en=svg_column_cryptarithm(["ABC", "ABC", "ABC"], "BBB"),
    )

    hard_aba = [
        (605, 5),   # ABA + BAB = 101A + 10B + 101B + 10A = 111(A+B)? Wait: (100A+10B+A)+(100B+10A+B)=111(A+B)! Wait 111*k: 555, 666, 777, 888, 999!
    ]
    # Let's check AB4 + 4BA = S where A, B are digits!
    hard_3d = [
        (4, 781),   # (100A+10B+4) + (400+10B+A) = 101A + 20B + 404 = 781 -> 101A + 20B = 377 -> A=3, 20B=74 no! Let's compute from (A,B)!
    ]
    for d_fix, A_v, B_v in [(4, 3, 7), (5, 2, 8), (6, 4, 3)]:
        tot_3 = (100 * A_v + 10 * B_v + d_fix) + (100 * d_fix + 10 * B_v + A_v)
        sols = [(a, b) for a in range(1, 10) for b in range(10)
                if (100 * a + 10 * b + d_fix) + (100 * d_fix + 10 * b + a) == tot_3]
        assert sols == [(A_v, B_v)]
        ans = 100 * A_v + 10 * B_v + d_fix
        other_n = 100 * d_fix + 10 * B_v + A_v
        B.add_math(
            tp, "Hard", bp,
            f"In the 3-digit column addition {m(f'\\overline{{AB{d_fix}}} + \\overline{{{d_fix}BA}} = {tot_3}')}, {m('A')} and {m('B')} are digits with {m('A \\ne 0')}. Find the 3-digit number {m(f'\\overline{{AB{d_fix}}}')}.",
            f"في عملية الجمع العمودي {m(f'\\overline{{AB{d_fix}}} + \\overline{{{d_fix}BA}} = {tot_3}')}، حيث {m('A')} و{m('B')} رقمان مع {m('A \\ne 0')}. أوجد العدد الثلاثي {m(f'\\overline{{AB{d_fix}}}')}.",
            ans, [other_n, ans + 10, ans - 10, 100 * B_v + 10 * A_v + d_fix],
            f"Check the **units column** {m(f'{d_fix} + A')} first to determine {m('A')}, then find {m('B')} from the tens column!",
            f"ابدأ بـ **عمود الآحاد** {m(f'{d_fix} + A')} لإيجاد {m('A')} مباشرة، ثم استنتج {m('B')} من العشرات!",
            f"Expand {m(f'101A + 20B + {101 * d_fix} = {tot_3}')} or read {m('A')} straight from the ones column!",
            [
                f"By place value, {m(f'(100A + 10B + {d_fix}) + ({100*d_fix} + 10B + A) = 101A + 20B + {101*d_fix} = {tot_3}')}.",
                f"Subtracting {m(101 * d_fix)} gives {m(f'101A + 20B = {tot_3 - 101*d_fix}')}. Since {m('20B')} ends in {m(0)}, the units digit forces {m(f'A = {A_v}')}.",
                f"Then {m(f'20B = {tot_3 - 101*d_fix - 101*A_v} \\implies B = {B_v}')}, so {m(f'\\overline{{AB{d_fix}}} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} + {other_n} = {tot_3}')}!",
            f"نكتب القيمة المكانية {m(f'101A + 20B = {tot_3 - 101*d_fix}')} فنكشف {m('A')} من الآحاد فوراً!",
            [
                f"بعد طرح {m(101 * d_fix)} نجد {m(f'101A + 20B = {tot_3 - 101*d_fix}')}.",
                f"بما أن آحاد {m('20B')} صفر، فإن {m(f'A = {A_v}')}، ومنه {m(f'20B = {20*B_v} \\implies B = {B_v}')}.",
                f"إذن العدد المطلوب هو {m(ans)}.",
            ],
            f"تحقق: {m(f'{ans} + {other_n} = {tot_3}')}!",
            diagram_en=svg_column_cryptarithm([f"AB{d_fix}", f"{d_fix}BA"], str(tot_3)),
        )

    # 10. nsmo_g7_palindrome_digit_swap (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g7_palindrome_digit_swap"
    easy_swap = [(8, 3), (9, 2), (7, 4), (9, 5), (8, 5)]
    for A, B_d in easy_swap:
        diff_v = 9 * (A - B_d)
        s_v = A + B_d
        ans = 10 * A + B_d
        B.add_math(
            tp, "Easy", bp,
            f"A two-digit number {m('\\overline{AB}')} has digit sum {m(f'A + B = {s_v}')}. When its digits are reversed to form {m('\\overline{BA}')}, the number decreases by {m(diff_v)}. What is the original number {m('\\overline{AB}')}?",
            f"عدد مكوّن من رقمين {m('\\overline{AB}')} مجموع رقميه {m(f'A + B = {s_v}')}. عند عكس رقميه لتكوين {m('\\overline{BA}')} ينقص العدد بمقدار {m(diff_v)}. ما العدد الأصلي {m('\\overline{AB}')}؟",
            ans, [10 * B_d + A, ans - 9, ans + 9, 10 * (A - 1) + (B_d + 1)],
            f"Use {m(f'\\overline{{AB}} - \\overline{{BA}} = 9(A - B) = {diff_v}')} to find {m('A - B')}, then combine with {m(f'A + B = {s_v}')}!",
            f"استخدم {m(f'\\overline{{AB}} - \\overline{{BA}} = 9(A - B) = {diff_v}')} لإيجاد {m('A - B')}، ثم حل مع {m(f'A + B = {s_v}')}!",
            f"Divide the reversal drop {m(diff_v)} by {m(9)} to get {m('A - B')}!",
            [
                f"Since {m(f'(10A + B) - (10B + A) = 9(A - B) = {diff_v}')}, we get {m(f'A - B = {A - B_d}')}.",
                f"Adding {m(f'A + B = {s_v}')} and {m(f'A - B = {A - B_d}')} gives {m(f'2A = {2*A} \\implies A = {A}')} and {m(f'B = {B_d}')}.",
                f"Thus {m(f'\\overline{{AB}} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} - {10*B_d + A} = {diff_v}')} and {m(f'{A} + {B_d} = {s_v}')}!",
            f"نقسم فرق العكس {m(diff_v)} على {m(9)} لإيجاد {m('A - B')}!",
            [
                f"من القاعدة {m(f'9(A - B) = {diff_v}')} نجد {m(f'A - B = {A - B_d}')}.",
                f"بجمعها مع {m(f'A + B = {s_v}')} نحصل على {m(f'A = {A}')} و{m(f'B = {B_d}')}، فالعدد هو {m(ans)}.",
            ],
            f"تحقق: {m(f'{ans} - {10*B_d + A} = {diff_v}')}!",
            diagram_en=svg_digit_slots([str(A), str(B_d)], f"AB − BA = {diff_v}"),
        )

    med_3swap = [
        (7, 4, 2),   # 742 - 247 = 495
        (9, 1, 3),   # 913 - 319 = 594
        (8, 5, 4),   # 854 - 458 = 396
        (6, 7, 3),   # 673 - 376 = 297
        (9, 6, 2),   # 962 - 269 = 693
        (8, 3, 1),   # 831 - 138 = 693? Wait make diff distinct or give A+B+C!
    ]
    med_3swap = [(9, 4, 4, 5), (8, 5, 2, 6), (7, 6, 3, 4), (9, 2, 6, 3), (8, 7, 1, 7), (6, 9, 4, 2)]
    for A, B_m, C, k_gap in med_3swap:
        assert A - C == k_gap
        diff_3 = 99 * k_gap
        s_ac = A + C
        ans = 100 * A + 10 * B_m + C
        rev_3 = 100 * C + 10 * B_m + A
        assert ans - rev_3 == diff_3
        B.add_math(
            tp, "Medium", bp,
            f"A 3-digit number {m('\\overline{ABC}')} has middle digit {m(f'B = {B_m}')}, outer digit sum {m(f'A + C = {s_ac}')}, and exceeds its digit-reversal {m('\\overline{CBA}')} by {m(diff_3)}. Find {m('\\overline{ABC}')}.",
            f"عدد ثلاثي {m('\\overline{ABC}')} رقمه الأوسط {m(f'B = {B_m}')}، ومجموع طرفيه {m(f'A + C = {s_ac}')}، ويزيد على معكوسه {m('\\overline{CBA}')} بمقدار {m(diff_3)}. أوجد العدد {m('\\overline{ABC}')}.",
            ans, [rev_3, ans - 99, ans + 99, 100 * A + 10 * C + B_m],
            f"Use {m(f'\\overline{{ABC}} - \\overline{{CBA}} = 99(A - C) = {diff_3}')}: divide by {m(99)} to get {m('A - C')}!",
            f"استخدم المتطابقة {m(f'\\overline{{ABC}} - \\overline{{CBA}} = 99(A - C) = {diff_3}')}: اقسم على {m(99)} لإيجاد {m('A - C')}!",
            f"Notice {m('B')} cancels in {m('\\overline{ABC} - \\overline{CBA} = 99(A - C)')}!",
            [
                f"By place value, {m(f'(100A + 10B + C) - (100C + 10B + A) = 99(A - C) = {diff_3}')}, so {m(f'A - C = {k_gap}')}.",
                f"Combine {m(f'A - C = {k_gap}')} with {m(f'A + C = {s_ac}')} to get {m(f'A = {A}')} and {m(f'C = {C}')}.",
                f"Inserting middle digit {m(f'B = {B_m}')} gives {m(f'\\overline{{ABC}} = {ans}')}.",
            ],
            f"Check: {m(f'{ans} - {rev_3} = {diff_3}')}!",
            f"نطبق القاعدة {m('99(A - C)')} لإيجاد {m('A')} و{m('C')} ثم نضع {m(f'B = {B_m}')} في الوسط!",
            [
                f"من {m(f'99(A - C) = {diff_3}')} نجد {m(f'A - C = {k_gap}')}.",
                f"مع {m(f'A + C = {s_ac}')} نحصل على {m(f'A = {A}')} و{m(f'C = {C}')}، فالعدد هو {m(ans)}.",
            ],
            f"تحقق: {m(f'{ans} - {rev_3} = {diff_3}')}!",
            diagram_en=svg_digit_slots([str(A), str(B_m), str(C)], f"ABC − CBA = {diff_3}"),
        )

    # Hard (4): Counting palindromes with divisibility & odometer palindromes!
    for mod_v, label_en, label_ar in [
        (9, "3-digit palindromes \\( \\overline{ABA} \\) divisible by \\( 9 \\)", "الأعداد المتناظرة الثلاثية \\( \\overline{ABA} \\) التي تقبل القسمة على \\( 9 \\)"),
        (4, "3-digit palindromes \\( \\overline{ABA} \\) divisible by \\( 4 \\)", "الأعداد المتناظرة الثلاثية \\( \\overline{ABA} \\) التي تقبل القسمة على \\( 4 \\)"),
        (9, "4-digit palindromes \\( \\overline{ABBA} \\) divisible by \\( 9 \\)", "الأعداد المتناظرة الرباعية \\( \\overline{ABBA} \\) التي تقبل القسمة على \\( 9 \\)"),
        (15, "4-digit palindromes \\( \\overline{ABBA} \\) divisible by \\( 15 \\)", "الأعداد المتناظرة الرباعية \\( \\overline{ABBA} \\) التي تقبل القسمة على \\( 15 \\)"),
    ]:
        is_3 = "3-digit" in label_en
        lo, hi = (100, 1000) if is_3 else (1000, 10000)
        pals = [x for x in range(lo, hi) if str(x) == str(x)[::-1] and x % mod_v == 0]
        ans = len(pals)
        slots = ["A", "B", "A"] if is_3 else ["A", "B", "B", "A"]
        B.add_math(
            tp, "Hard", bp,
            f"How many {label_en} exist (with leading digit {m('A \\ne 0')})?",
            f"كم عدد {label_ar} (علماً بأن الخانة اليسرى {m('A \\ne 0')})؟",
            ans, [ans - 2 if ans > 4 else ans + 2, ans + 5, ans * 2, 9],
            f"Remember {m('A \\in \\{1, \\dots, 9\\}')} while {m('B \\in \\{0, \\dots, 9\\}')}, and test the divisibility rule for {m(mod_v)} on the digits!",
            f"تذكر أن {m('A \\in \\{1, \\dots, 9\\}')} بينما {m('B \\in \\{0, \\dots, 9\\}')}، وطبّق قاعدة قابلية القسمة على {m(mod_v)}!",
            f"Count valid pairs {m('(A, B)')} with {m('1 \\le A \\le 9')} and {m('0 \\le B \\le 9')} satisfying divisibility by {m(mod_v)}!",
            [
                f"Write the palindrome digits with {m('A \\in \\{1, \\dots, 9\\}')} and {m('B \\in \\{0, \\dots, 9\\}')}.",
                f"Applying the divisibility test for {m(mod_v)} restricts the pair {m('(A, B)')} cleanly.",
                f"Counting every valid choice of {m('(A, B)')} gives {m(ans)} palindromes.",
            ],
            f"Exhaustive check across {m(f'[{lo}, {hi - 1}]')} finds {m(ans)} such palindromes (starting with {m(pals[0])} and ending with {m(pals[-1])})!",
            f"نحصي جميع الأزواج المسموحة {m('(A, B)')} مع مراعاة {m('A \\ne 0')} وشرط القسمة على {m(mod_v)}!",
            [
                f"الخانة القيادية {m('A')} تأخذ من {m(1)} إلى {m(9)}، بينما {m('B')} من {m(0)} إلى {m(9)}.",
                f"بتطبيق شرط القسمة على {m(mod_v)} نجد بالضبط {m(ans)} عدداً متناظراً.",
            ],
            f"تحقق: أصغرها {m(pals[0])} وأكبرها {m(pals[-1])} وعددها {m(ans)}!",
            diagram_en=svg_digit_slots(slots, f"Divisible by {mod_v}"),
        )


# =============================================================================
# UNIT 1.3 — Patterns, Sequences & Algebraic Structures (75 Qs)
# =============================================================================
def _add_unit_1_3(B: BankBuilder) -> None:
    tp = "Algebra"

    # 11. nsmo_g7_visual_figurate_growth (5E, 6M, 4H) — SVG: matchsticks / dots
    bp = "nsmo_g7_visual_figurate_growth"
    easy_pat = [
        ("squares", 3, 1, 18, "4, 7, 10"),
        ("squares", 3, 1, 32, "4, 7, 10"),
        ("triangles", 2, 1, 24, "3, 5, 7"),
        ("triangles", 2, 1, 40, "3, 5, 7"),
        ("squares", 3, 1, 45, "4, 7, 10"),
    ]
    for kind, slope, c0, n_fig, first3 in easy_pat:
        ans = slope * n_fig + c0
        diag = svg_matchstick_squares((1, 2, 3)) if kind == "squares" else svg_matchstick_triangles((1, 2, 3))
        shape_ar = "مربعات" if kind == "squares" else "مثلثات"
        B.add_math(
            tp, "Easy", bp,
            f"A row of connected matchstick {kind} uses {m(first3)} matchsticks in Figures 1, 2, and 3, respectively. How many matchsticks are required to build **Figure {n_fig}**?",
            f"صف من ال{shape_ar} المتلاصقة بأعواد الثقاب يستهلك {m(first3)} أعواد في الأشكال ١ و٢ و٣ على الترتيب. كم عود ثقاب يلزم لبناء **الشكل {n_fig}**؟",
            ans, [ans - slope, ans + slope, (slope + c0) * n_fig, slope * n_fig],
            f"Figure 1 starts with {m(slope + c0)} sticks and each new step adds {m(slope)} sticks: use {m(f'{slope}n + {c0}')}!",
            f"يبدأ الشكل الأول بـ {m(slope + c0)} أعواد ويضيف كل شكل جديد {m(slope)} أعواد: استخدم {m(f'{slope}n + {c0}')}!",
            f"Apply the linear growth rule {m(f'a_n = {slope}n + {c0}')} at {m(f'n = {n_fig}')}!",
            [
                f"Each additional figure shares one side and adds {m(slope)} matchsticks, giving {m(f'a_n = {slope}n + {c0}')}.",
                f"Substitute {m(f'n = {n_fig}')}: {m(f'{slope} \\times {n_fig} + {c0} = {ans}')} matchsticks.",
            ],
            f"Check {m('n=1,2,3')}: {m(f'{slope}(1)+{c0}={slope+c0}')}, {m(f'{slope}(2)+{c0}={2*slope+c0}')}, {m(f'{slope}(3)+{c0}={3*slope+c0}')}!",
            f"نطبق قاعدة النمو الخطي الثابت {m(f'a_n = {slope}n + {c0}')} عند {m(f'n = {n_fig}')}!",
            [
                f"كل خطوة جديدة تضيف {m(slope)} أعواد، فالصيغة هي {m(f'a_n = {slope}n + {c0}')}.",
                f"بالتعويض عن {m(f'n = {n_fig}')} نحصل على {m(f'{slope} \\times {n_fig} + {c0} = {ans}')} عوداً.",
            ],
            f"تحقق: الصيغة تطابق الأشكال الثلاثة الأولى {m(first3)} تماماً!",
            diagram_en=diag,
        )

    med_dots = [
        ("L", 2, 1, 37, False),      # 2*37 + 1 = 75 dots
        ("cross", 4, 1, 28, False),  # 4*28 + 1 = 113 dots
        ("L", 2, 1, 91, True),       # 2n + 1 = 91 -> n = 45
        ("cross", 4, 1, 125, True),  # 4n + 1 = 125 -> n = 31
        ("L", 2, 1, 139, True),      # 2n + 1 = 139 -> n = 69
        ("cross", 4, 1, 169, True),  # 4n + 1 = 169 -> n = 42
    ]
    for mode, slope, c0, val, is_inv in med_dots:
        diag = svg_dot_pattern(mode)
        pat_name_en = "L-shaped dot pattern (3, 5, 7, ...)" if mode == "L" else "cross-shaped dot pattern (5, 9, 13, ...)"
        pat_name_ar = "نمط النقاط على شكل حرف L (3، 5، 7، ...)" if mode == "L" else "نمط النقاط المتقاطعة (5، 9، 13، ...)"
        if not is_inv:
            ans = slope * val + c0
            B.add_math(
                tp, "Medium", bp,
                f"In the {pat_name_en} shown, how many dots appear in **Figure {val}**?",
                f"في {pat_name_ar} الموضّح، كم نقطة تظهر في **الشكل {val}**؟",
                ans, [ans - slope, ans + slope, (slope + 1) * val, slope * val],
                f"Spot the center corner dot ({m(1)}) plus {m(slope)} arms of length {m('n')}: {m(f'D(n) = {slope}n + 1')}!",
                f"لاحظ النقطة المركزية ({m(1)}) مع {m(slope)} أذرع طول كل منها {m('n')}: {m(f'D(n) = {slope}n + 1')}!",
                f"Count the central dot plus {m(slope)} arms of {m(val)} dots each!",
                [
                    f"Figure {m('n')} has {m(1)} central dot and {m(slope)} arms of {m('n')} dots, giving {m(f'{slope}n + 1')} dots.",
                    f"For {m(f'n = {val}')}, total dots = {m(f'{slope} \\times {val} + 1 = {ans}')}.",
                ],
                f"Check {m('n=1')}: {m(slope + 1)} dots; for {m(f'n={val}')}: {m(ans)} dots!",
                f"نحسب النقطة المركزية مضافاً إليها {m(slope)} أذرع في كل منها {m(val)} نقطة!",
                [
                    f"عدد النقاط في الشكل {m('n')} يعطى بالعلاقة {m(f'{slope}n + 1')}.",
                    f"عند {m(f'n = {val}')} نحصل على {m(f'{slope} \\times {val} + 1 = {ans}')} نقطة.",
                ],
                f"تحقق: عند {m('n=1')} تعطي {m(slope + 1)} نقاط كما في الرسم!",
                diagram_en=diag,
            )
        else:
            ans = (val - c0) // slope
            assert slope * ans + c0 == val
            B.add_math(
                tp, "Medium", bp,
                f"In the {pat_name_en} shown, **which figure number {m('n')}** contains exactly {m(val)} dots?",
                f"في {pat_name_ar} الموضّح، **ما رقم الشكل {m('n')}** الذي يحتوي على {m(val)} نقطة بالضبط؟",
                ans, [ans - 1, ans + 1, val // (slope + 1), ans + 2],
                f"Set {m(f'{slope}n + 1 = {val}')}, subtract the center dot {m(1)}, and divide by {m(slope)}!",
                f"ضع المعادلة {m(f'{slope}n + 1 = {val}')}، اطرح النقطة المركزية {m(1)} ثم اقسم على {m(slope)}!",
                f"Solve the linear pattern equation {m(f'{slope}n + 1 = {val}')} for {m('n')}!",
                [
                    f"Figure {m('n')} has {m(f'{slope}n + 1')} dots.",
                    f"Set {m(f'{slope}n + 1 = {val} \\implies {slope}n = {val - 1} \\implies n = {ans}')}.",
                ],
                f"Check: Figure {m(ans)} has {m(f'{slope} \\times {ans} + 1 = {val}')} dots!",
                f"نحل المعادلة {m(f'{slope}n + 1 = {val}')} لإيجاد رقم الشكل {m('n')}!",
                [
                    f"بطرح {m(1)} من الطرفين نجد {m(f'{slope}n = {val - 1}')}.",
                    f"وبالقسمة على {m(slope)} نحصل على {m(f'n = {ans}')}.",
                ],
                f"تحقق: {m(f'{slope} \\times {ans} + 1 = {val}')}!",
                diagram_en=diag,
            )

    for n_grid in (5, 6, 7, 8):
        ans = 2 * n_grid * (n_grid + 1)
        B.add_math(
            tp, "Hard", bp,
            f"Unit-length matchsticks are arranged to form a complete {m(f'{n_grid} \\times {n_grid}')} square grid of unit squares (for example, a {m('1 \\times 1')} grid uses {m(4)} sticks and a {m('2 \\times 2')} grid uses {m(12)} sticks). How many matchsticks are needed in total?",
            f"رُتّبت أعواد ثقاب طول كل منها وحدة واحدة لتكوين شبكة مربعة كاملة أبعادها {m(f'{n_grid} \\times {n_grid}')} من المربعات الصغيرة (فمثلاً شبكة {m('1 \\times 1')} تحتاج {m(4)} أعواد وشبكة {m('2 \\times 2')} تحتاج {m(12)} عوداً). كم عود ثقاب يلزم إجمالاً؟",
            ans, [4 * n_grid * n_grid, 2 * n_grid * n_grid, ans - 2 * n_grid, ans + 2 * (n_grid + 1)],
            f"Count **horizontal** unit sticks and **vertical** unit sticks separately: there are {m(n_grid + 1)} horizontal lines, each made of {m(n_grid)} sticks!",
            f"احسب الأعواد **الأفقية** و**الرأسية** كلٌّ على حدة: يوجد {m(n_grid + 1)} خطوط أفقية في كل خط {m(n_grid)} أعواد!",
            f"Count {m(n_grid + 1)} horizontal rows of {m(n_grid)} sticks plus {m(n_grid + 1)} vertical columns of {m(n_grid)} sticks!",
            [
                f"An {m(f'{n_grid} \\times {n_grid}')} grid has {m(n_grid + 1)} horizontal grid lines, each containing {m(n_grid)} unit matchsticks: {m(f'{n_grid + 1} \\times {n_grid} = {n_grid*(n_grid+1)}')} horizontal sticks.",
                f"By symmetry, there are also {m(f'{n_grid + 1} \\times {n_grid} = {n_grid*(n_grid+1)}')} vertical sticks.",
                f"Total matchsticks = {m(f'2 \\times {n_grid*(n_grid+1)} = {ans}')}.",
            ],
            f"Formula {m('2n(n+1)')} gives {m('4')} at {m('n=1')}, {m('12')} at {m('n=2')}, and {m(ans)} at {m(f'n={n_grid}')}!",
            f"نحسب الأعواد الأفقية والعمودية بالقاعدة {m('2n(n + 1)')}!",
            [
                f"عدد الأعواد الأفقية = {m(f'({n_grid} + 1) \\times {n_grid} = {n_grid*(n_grid+1)}')}.",
                f"وعدد الأعواد الرأسية مثلها = {m(n_grid * (n_grid + 1))}، فالمجموع = {m(ans)} عوداً.",
            ],
            f"تحقق: {m(f'2 \\times {n_grid} \\times {n_grid + 1} = {ans}')}!",
            diagram_en=svg_matchstick_squares((1, 2, 3)),
        )

    # 12. nsmo_g7_balance_scale_substitution (5E, 6M, 4H) — SVG: svg_balance_scales
    bp = "nsmo_g7_balance_scale_substitution"
    easy_bal = [
        (1, 2, 1, 3, 3),  # 1C=2S, 1S=3T -> 3C = 18T
        (2, 3, 1, 2, 4),  # 2C=3S, 1S=2T -> 4C = 12T
        (1, 3, 2, 4, 5),  # 1C=3S, 2S=4T -> 5C = 30T
        (3, 4, 2, 3, 3),  # 3C=4S, 2S=3T -> 3C = 6T
        (2, 5, 1, 2, 2),  # 2C=5S, 1S=2T -> 2C = 10T
    ]
    for c1, s1, s2, t2, ask_c in easy_bal:
        tri_per_sq = Fraction(t2, s2)
        tri_per_cir = Fraction(s1, c1) * tri_per_sq
        tot_t = ask_c * tri_per_cir
        assert tot_t.denominator == 1
        ans = int(tot_t)
        B.add_math(
            tp, "Easy", bp,
            f"On Balance Scale 1, {m(c1)} circle(s) balance {m(s1)} square(s). On Balance Scale 2, {m(s2)} square(s) balance {m(t2)} triangle(s). How many **triangles** balance {m(ask_c)} circles?",
            f"في الميزان الأول تتزن {m(c1)} دائرة مع {m(s1)} مربع، وفي الميزان الثاني تتزن {m(s2)} مربع مع {m(t2)} مثلث. كم **مثلثاً** يلزم لموازنة {m(ask_c)} دوائر؟",
            ans, [ans // 2 if ans > 4 else ans + 4, ans + 3, ask_c * s1, ans + 6],
            f"Express {m(1)} square in terms of triangles from Scale 2, then convert circles to squares and squares to triangles!",
            f"أوجد ما يعادل المربع الواحد من المثلثات عبر الميزان الثاني، ثم حوّل الدوائر إلى مربعات ثم إلى مثلثات!",
            f"Chain the two weight ratios {m('C \\to S \\to T')}!",
            [
                f"From Scale 2, {m(f'{s2}\\text{{ squares}} = {t2}\\text{{ triangles}}')}, so each square weighs {m(f'\\frac{{{t2}}}{{{s2}}}')} triangles.",
                f"From Scale 1, {m(ask_c)} circles equal {m(f'{ask_c} \\times \\frac{{{s1}}}{{{c1}}} = {int(ask_c * Fraction(s1, c1))}')} squares.",
                f"Converting to triangles gives {m(f'{int(ask_c * Fraction(s1, c1))} \\times \\frac{{{t2}}}{{{s2}}} = {ans}')} triangles.",
            ],
            f"Unit weight check confirms {m(ask_c)} circles = {m(ans)} triangles!",
            f"نحوّل الدوائر إلى مربعات ثم نستبدل المربعات بما يكافئها من المثلثات!",
            [
                f"من الميزان الأول: {m(ask_c)} دوائر تكافئ {m(int(ask_c * Fraction(s1, c1)))} مربعات.",
                f"وباستخدام نسبة الميزان الثاني نحصل على {m(ans)} مثلثاً.",
            ],
            f"تحقق: التوازن الدقيق يتحقق عند {m(ans)} مثلثاً!",
            diagram_en=svg_balance_scales(c1, s1, s2, t2),
        )

    med_bal = [
        (2, 1, 5, 1, 3, 3),  # 2C + 1S = 5S -> 2C=4S -> 1C=2S; 1S=3T -> 3C = 18T
        (3, 2, 8, 2, 5, 1),  # 3C + 2S = 8S -> 3C=6S -> 1C=2S; 2S=5T -> 1C = 5T
        (2, 3, 9, 1, 2, 4),  # 2C + 3S = 9S -> 2C=6S -> 1C=3S; 1S=2T -> 4C = 24T
        (4, 1, 7, 3, 4, 2),  # 4C + 1S = 7S -> 4C=6S -> 2C=3S; 3S=4T -> 2C = 4T
        (1, 2, 6, 2, 3, 3),  # 1C + 2S = 6S -> 1C=4S; 2S=3T -> 3C = 12S = 18T
        (3, 1, 10, 1, 2, 2), # 3C + 1S = 10S -> 3C=9S -> 1C=3S; 1S=2T -> 2C = 12T
    ]
    for c_l, s_l, s_r, s2, t2, ask_c in med_bal:
        net_s = s_r - s_l
        ans = int(ask_c * Fraction(net_s, c_l) * Fraction(t2, s2))
        B.add_math(
            tp, "Medium", bp,
            f"On Scale 1, {m(c_l)} circle(s) **and** {m(s_l)} square(s) together balance {m(s_r)} squares. On Scale 2, {m(s2)} square(s) balance {m(t2)} triangles. How many **triangles** balance {m(ask_c)} circle(s)?",
            f"في الميزان الأول تتزن {m(c_l)} دائرة **مع** {m(s_l)} مربع في كفة مقابل {m(s_r)} مربعات في الكفة الأخرى. وفي الميزان الثاني تتزن {m(s2)} مربع مع {m(t2)} مثلثات. كم **مثلثاً** يوازن {m(ask_c)} دائرة؟",
            ans, [ans + t2, int(ask_c * Fraction(s_r, c_l) * Fraction(t2, s2)), ans - 2 if ans > 4 else ans + 6, ans + 4],
            f"First remove {m(s_l)} square(s) from **both** pans of Scale 1 so circles stand alone!",
            f"احذف {m(s_l)} مربع من **كلتا** كفتي الميزان الأول أولاً لعزل الدوائر!",
            f"Subtract {m(s_l)} square(s) from both sides of Scale 1 before substituting Scale 2!",
            [
                f"Removing {m(s_l)} square(s) from both pans of Scale 1 gives {m(f'{c_l}\\text{{ circles}} = {net_s}\\text{{ squares}}')}.",
                f"Thus {m(ask_c)} circle(s) equal {m(f'{int(ask_c * Fraction(net_s, c_l))}')} squares.",
                f"Using {m(f'{s2}\\text{{ squares}} = {t2}\\text{{ triangles}}')} yields {m(ans)} triangles.",
            ],
            f"Trap avoided: forgetting to subtract the {m(s_l)} shared square(s) would overestimate the weight!",
            f"نطرح {m(s_l)} مربع من الكفتين أولاً ثم نعوّض بنسبة المثلثات!",
            [
                f"بحذف {m(s_l)} مربع من الطرفين نجد: {m(c_l)} دوائر = {m(net_s)} مربعات.",
                f"ومنه {m(ask_c)} دائرة = {m(int(ask_c * Fraction(net_s, c_l)))} مربعات = {m(ans)} مثلثاً.",
            ],
            f"تحقق: الكفتان تتعادلان تماماً عند {m(ans)} مثلثاً!",
            diagram_en=svg_balance_scales(c_l, net_s, s2, t2),
        )

    hard_sym_bal = [
        (17, 13, 18),  # C+S=17, S+T=13, C+T=18 -> C+S+T=24 -> C = 24 - 13 = 11
        (23, 19, 26),  # sum=68 -> C+S+T=34 -> C = 34 - 19 = 15
        (31, 22, 27),  # sum=80 -> C+S+T=40 -> C = 40 - 22 = 18
        (29, 18, 25),  # sum=72 -> C+S+T=36 -> C = 36 - 18 = 18? Wait make distinct: (29, 17, 26) -> sum=72 -> 36-17 = 19!
    ]
    hard_sym_bal = [(17, 13, 18), (23, 19, 26), (31, 22, 27), (29, 17, 26)]
    for w_cs, w_st, w_ct in hard_sym_bal:
        s_all = (w_cs + w_st + w_ct) // 2
        ans = s_all - w_st
        S_w = w_cs - ans
        T_w = w_ct - ans
        assert ans + S_w == w_cs and S_w + T_w == w_st and ans + T_w == w_ct
        B.add_math(
            tp, "Hard", bp,
            f"Three metal shapes are weighed in pairs: Circle + Square = {m(w_cs)} g, Square + Triangle = {m(w_st)} g, and Circle + Triangle = {m(w_ct)} g. What is the weight (in grams) of **one Circle**?",
            f"وُزنت ثلاث قطع معدنية مثنى مثنى: الدائرة + المربع = {m(w_cs)} جم، والمربع + المثلث = {m(w_st)} جم، والدائرة + المثلث = {m(w_ct)} جم. ما وزن **الدائرة الواحدة** بالجرام؟",
            ans, [s_all, S_w, T_w, ans + 3],
            f"Add all three weighings together—each shape appears **twice**—and divide by {m(2)} to get {m('\\text{Circle} + \\text{Square} + \\text{Triangle}')}!",
            f"اجمع الأوزان الثلاثة معاً—حيث تظهر كل قطعة **مرتين**—واقسم على {m(2)} لإيجاد مجموع القطع الثلاث!",
            f"Sum all three pair equations and divide by {m(2)}, then subtract {m('\\text{Square} + \\text{Triangle}')}!",
            [
                f"Adding all three equations gives {m(f'2(C + S + T) = {w_cs} + {w_st} + {w_ct} = {2 * s_all}')}, so {m(f'C + S + T = {s_all}')} g.",
                f"Subtract {m(f'S + T = {w_st}')} g to isolate the Circle: {m(f'C = {s_all} - {w_st} = {ans}')} g.",
            ],
            f"Check: {m(f'C={ans}, S={S_w}, T={T_w}')} gives {m(f'{ans}+{S_w}={w_cs}')}, {m(f'{S_w}+{T_w}={w_st}')}, {m(f'{ans}+{T_w}={w_ct}')}!",
            f"نجمع المعادلات الثلاث ونقسم على {m(2)} ثم نطرح وزن المربع والمثلث!",
            [
                f"بجمع المعادلات الثلاث: {m(f'2(C + S + T) = {2 * s_all} \\implies C + S + T = {s_all}')} جم.",
                f"بطرح {m(f'S + T = {w_st}')} نجد وزن الدائرة {m(f'C = {s_all} - {w_st} = {ans}')} جم.",
            ],
            f"تحقق: الأوزان {m(f'({ans}, {S_w}, {T_w})')} تحقق المعادلات الثلاث معاً!",
            diagram_en=svg_balance_scales(1, 1, 1, 1),
        )

    # 13. nsmo_g7_consecutive_sum_parity (5E, 6M, 4H) — SVG: svg_number_strip on Easy & Hard
    bp = "nsmo_g7_consecutive_sum_parity"
    easy_cons = [
        (3, 87, "largest"),
        (5, 115, "smallest"),
        (5, 165, "largest"),
        (7, 175, "smallest"),
        (9, 198, "largest"),
    ]
    for cnt, tot_s, which in easy_cons:
        mid = tot_s // cnt
        half = (cnt - 1) // 2
        ans = mid + half if which == "largest" else mid - half
        which_ar = "أكبر" if which == "largest" else "أصغر"
        B.add_math(
            tp, "Easy", bp,
            f"In a Mawhiba warm-up puzzle, {m(cnt)} consecutive integers add up to {m(tot_s)}. What is the **{which}** of these {m(cnt)} integers?",
            f"في مسألة تدريبية لأولمبياد موهبة، مجموع {m(cnt)} أعداد صحيحة متتالية يساوي {m(tot_s)}. ما **{which_ar}** هذه الأعداد؟",
            ans, [mid, mid - half if which == "largest" else mid + half, ans + 1, ans - 1],
            f"Divide {m(tot_s)} by {m(cnt)} to find the **middle** integer immediately!",
            f"اقسم {m(tot_s)} على {m(cnt)} لتحصل فوراً على العدد **الأوسط**!",
            f"Compute the middle term {m(f'{tot_s} \\div {cnt} = {mid}')} and step {m(half)} positions!",
            [
                f"For an odd count {m(cnt)} of consecutive integers, the middle integer equals the mean: {m(f'{tot_s} \\div {cnt} = {mid}')}.",
                f"Stepping {m(half)} units to the {'right' if which == 'largest' else 'left'} gives {m(ans)}.",
            ],
            f"Sum check: {m(cnt)} consecutive integers centered at {m(mid)} sum to {m(f'{cnt} \\times {mid} = {tot_s}')}!",
            f"نقسم المجموع {m(tot_s)} على {m(cnt)} لإيجاد الأوسط {m(mid)} ثم نتحرك {m(half)} خطوات!",
            [
                f"العدد الأوسط = {m(f'{tot_s} \\div {cnt} = {mid}')}.",
                f"إذن {which_ar} الأعداد هو {m(ans)}.",
            ],
            f"تحقق: متوسط الأعداد هو {m(mid)} ومجموعها {m(tot_s)}!",
            diagram_en=svg_number_strip([str(mid - half), "...", str(mid), "...", str(mid + half)]),
        )

    med_cons_par = [
        (4, "even", 108, "largest"),   # k, k+2, k+4, k+6 -> 4k+12=108 -> k=24 -> largest=30
        (5, "odd", 175, "smallest"),   # mid=35 -> smallest=31
        (6, "even", 174, "largest"),   # 6k+30=174 -> k=24 -> largest=34
        (4, "odd", 144, "smallest"),   # 4k+12=144 -> k=33 -> smallest=33
        (5, "even", 230, "largest"),   # mid=46 -> largest=50
        (6, "odd", 216, "smallest"),   # 6k+30=216 -> k=31 -> smallest=31
    ]
    for cnt, par, tot_s, which in med_cons_par:
        first_v = (tot_s - cnt * (cnt - 1)) // cnt
        seq = [first_v + 2 * i for i in range(cnt)]
        assert sum(seq) == tot_s
        ans = seq[-1] if which == "largest" else seq[0]
        par_ar = "زوجية" if par == "even" else "فردية"
        which_ar = "أكبر" if which == "largest" else "أصغر"
        B.add_math(
            tp, "Medium", bp,
            f"The sum of {m(cnt)} consecutive **{par}** integers is {m(tot_s)}. What is the **{which}** of these integers?",
            f"مجموع {m(cnt)} أعداد **{par_ar}** متتالية يساوي {m(tot_s)}. ما **{which_ar}** هذه الأعداد؟",
            ans, [seq[0] if which == "largest" else seq[-1], ans + 2, ans - 2, tot_s // cnt],
            f"Consecutive {par} integers differ by {m(2)}: write them as {m('x, x+2, x+4, \\dots')} and sum!",
            f"الأعداد ال{par_ar} المتتالية تزداد بمقدار {m(2)} في كل خطوة: اكتبها {m('x, x+2, x+4, \\dots')} واجمعها!",
            f"Let the smallest integer be {m('x')} so the terms step by {m('+2')}!",
            [
                f"Write the {m(cnt)} integers as {m('x, x+2, \\dots, x+' + str(2*(cnt-1)))}, whose sum is {m(f'{cnt}x + {cnt*(cnt-1)} = {tot_s}')}.",
                f"Solving gives {m(f'{cnt}x = {tot_s - cnt*(cnt-1)} \\implies x = {first_v}')}, and the largest is {m(seq[-1])}.",
                f"Thus the {which} integer is {m(ans)}.",
            ],
            f"Check: {m(' + '.join(str(v) for v in seq) + f' = {tot_s}')}!",
            f"نفرض أصغر الأعداد {m('x')} ونكون المعادلة الخطية بخطوة قدرها {m(2)}!",
            [
                f"المجموع يساوي {m(f'{cnt}x + {cnt*(cnt-1)} = {tot_s}')}، ومنه الأصغر {m(f'x = {first_v}')}.",
                f"الأعداد هي من {m(seq[0])} إلى {m(seq[-1])}، فتكون القيمة المطلوبة {m(ans)}.",
            ],
            f"تحقق: مجموع الأعداد يساوي {m(tot_s)} بالضبط!",
        )

    for N_top in (80, 120, 150, 200):
        ans = N_top // 2
        B.add_math(
            tp, "Hard", bp,
            f"Evaluate the alternating sum {m(f'{N_top} - {N_top - 1} + {N_top - 2} - {N_top - 3} + \\dots + 4 - 3 + 2 - 1')}.",
            f"احسب قيمة المجموع المتناوب {m(f'{N_top} - {N_top - 1} + {N_top - 2} - {N_top - 3} + \\dots + 4 - 3 + 2 - 1')}.",
            ans, [N_top, ans + 1, ans - 1, N_top * (N_top + 1) // 4],
            f"Group consecutive terms into pairs of two: {m(f'({N_top} - {N_top-1}) + ({N_top-2} - {N_top-3}) + \\dots + (2 - 1)')}!",
            f"جمّع الحدود المتتالية في أزواج: {m(f'({N_top} - {N_top-1}) + ({N_top-2} - {N_top-3}) + \\dots + (2 - 1)')}!",
            f"Pair adjacent numbers so each pair equals {m(1)}!",
            [
                f"There are {m(N_top)} integers from {m(N_top)} down to {m(1)}, forming {m(f'{N_top} \\div 2 = {ans}')} pairs.",
                f"Each pair {m('(2k - (2k - 1))')} equals {m(1)}.",
                f"Adding {m(ans)} ones gives {m(ans)}.",
            ],
            f"Check: sum of evens minus sum of odds = {m(ans)}!",
            f"نجمّع الـ {m(N_top)} حداً في {m(ans)} زوجاً قيمة كل زوج منها {m(1)}!",
            [
                f"يتكون المقدار من {m(f'{N_top} \\div 2 = {ans}')} قوساً على الصورة {m('(2k - (2k-1)) = 1')}.",
                f"إذن الناتج الكلي يساوي {m(ans)}.",
            ],
            f"تحقق: الفرق في كل زوج يساوي {m(1)} وعدد الأزواج {m(ans)}!",
            diagram_en=svg_number_strip([f"{N_top}−{N_top-1}", "+...", "+4−3", "+2−1", f"={ans}"]),
        )

    # 14. nsmo_g7_number_pyramid_algebra (5E, 6M, 4H) — SVG: svg_number_pyramid
    bp = "nsmo_g7_number_pyramid_algebra"
    easy_pyr = [
        (5, 9, 8),    # top = 5 + 18 + 8 = 31, ask x=9
        (7, 11, 6),   # top = 35, ask x=11
        (12, 8, 15),  # top = 43, ask x=8
        (9, 14, 10),  # top = 47, ask x=14
        (6, 13, 11),  # top = 43, ask x=13
    ]
    for a, x_v, c in easy_pyr:
        top_v = a + 2 * x_v + c
        B.add_math(
            tp, "Easy", bp,
            f"In a 3-row additive number pyramid, each brick above the base is the sum of the two bricks directly below it. If the bottom row is {m(f'({a},\\; x,\\; {c})')} and the top brick is {m(top_v)}, find {m('x')}.",
            f"في هرم أعداد جمعي من 3 صفوف، كل خانة علوية تساوي مجموع الخانتين تحتها مباشرة. إذا كان صف القاعدة {m(f'({a},\\; x,\\; {c})')} وقمة الهرم {m(top_v)}، فأوجد قيمة {m('x')}.",
            x_v, [top_v - a - c, x_v + 2, x_v - 2, (top_v - a) // 2],
            f"Remember the middle bottom brick {m('x')} enters **both** middle-row bricks, so {m(f'{a} + 2x + {c} = {top_v}')}!",
            f"تذكر أن الخانة الوسطى {m('x')} تدخل في خانتَي الصف الأوسط معاً، أي {m(f'{a} + 2x + {c} = {top_v}')}!",
            f"Use {m(f'\\text{{Top}} = {a} + 2x + {c} = {top_v}')}!",
            [
                f"Middle-row bricks are {m(f'{a} + x')} and {m(f'x + {c}')}.",
                f"Their sum is {m(f'{a + c} + 2x = {top_v} \\implies 2x = {2 * x_v} \\implies x = {x_v}')}.",
            ],
            f"Check: base {m(f'({a}, {x_v}, {c})')} gives middle {m(f'({a+x_v}, {x_v+c})')} and top {m(top_v)}!",
            f"نجمع خانتَي الوسط فنحصل على المعادلة {m(f'{a + c} + 2x = {top_v}')}!",
            [
                f"الصف الأوسط هو {m(f'({a}+x,\\; x+{c})')} ومجموعه {m(f'2x + {a+c} = {top_v}')}.",
                f"ومنه {m(f'2x = {2*x_v} \\implies x = {x_v}')}.",
            ],
            f"تحقق: {m(f'({a}+{x_v}) + ({x_v}+{c}) = {top_v}')}!",
            diagram_en=svg_number_pyramid(str(top_v), f"{a}+x", f"x+{c}", str(a), "x", str(c)),
        )

    med_pyr = [
        (1, 2, 5, 6),    # (x, 2x, 5) at x=6 -> 6 + 24 + 5 = 35
        (2, 1, 3, 7),    # (2x, x, 3) at x=7 -> 14 + 14 + 3 = 31
        (1, 3, 4, 5),    # (x, 3x, 4) at x=5 -> 5 + 30 + 4 = 39
        (3, 1, 8, 4),    # (3x, x, 8) at x=4 -> 12 + 8 + 8 = 28
        (2, 2, 7, 6),    # (2x, 2x, 7) at x=6 -> 12 + 24 + 7 = 43
        (1, 2, 9, 8),    # (x, 2x, 9) at x=8 -> 8 + 32 + 9 = 49
    ]
    for k1, k2, c, x_v in med_pyr:
        coeff = k1 + 2 * k2
        top_v = coeff * x_v + c
        b1 = "x" if k1 == 1 else f"{k1}x"
        b2 = "x" if k2 == 1 else f"{k2}x"
        B.add_math(
            tp, "Medium", bp,
            f"A 3-row additive number pyramid has bottom row {m(f'({b1},\\; {b2},\\; {c})')} and top brick {m(top_v)}. What is the value of {m('x')}?",
            f"هرم أعداد جمعي من 3 صفوف قاعدته السفلى {m(f'({b1},\\; {b2},\\; {c})')} وقمته {m(top_v)}. ما قيمة {m('x')}؟",
            x_v, [x_v + 1, x_v - 1, (top_v - c) // (k1 + k2) if (top_v - c) % (k1 + k2) == 0 else x_v + 3, x_v + 2],
            f"Apply {m('a + 2b + c = \\text{Top}')}: don't forget to double the middle base term {m(b2)}!",
            f"طبّق القاعدة {m('a + 2b + c = \\text{Top}')} مع تذكّر مضاعفة الحد الأوسط {m(b2)}!",
            f"Write {m(f'{b1} + 2({b2}) + {c} = {top_v}')} and solve for {m('x')}!",
            [
                f"Using {m('\\text{Top} = a + 2b + c')}, we get {m(f'{k1}x + {2*k2}x + {c} = {coeff}x + {c} = {top_v}')}.",
                f"Subtract {m(c)} to find {m(f'{coeff}x = {coeff * x_v} \\implies x = {x_v}')}.",
            ],
            f"Check: base {m(f'({k1*x_v}, {k2*x_v}, {c})')} yields top {m(f'{k1*x_v + k2*x_v} + {k2*x_v + c} = {top_v}')}!",
            f"نعوّض في قانون القمة {m('a + 2b + c')} فنحصل على {m(f'{coeff}x + {c} = {top_v}')}!",
            [
                f"من القاعدة نجد {m(f'{coeff}x = {top_v} - {c} = {coeff * x_v}')}.",
                f"وبالقسمة على {m(coeff)} نحصل على {m(f'x = {x_v}')}.",
            ],
            f"تحقق: القمة الناتجة عند {m(f'x = {x_v}')} تساوي {m(top_v)}!",
            diagram_en=svg_number_pyramid(str(top_v), f"{k1+k2}x", f"{b2}+{c}", b1, b2, str(c)),
        )

    for a4, x4, d4 in [(3, 5, 7), (4, 8, 6), (2, 9, 10), (5, 7, 9)]:
        # 4-row pyramid with base (a4, x4, x4, d4): Top = a4 + 3*x4 + 3*x4 + d4 = a4 + 6*x4 + d4!
        top4 = a4 + 6 * x4 + d4
        B.add_math(
            tp, "Hard", bp,
            f"In a **4-row** additive number pyramid, each brick above the base is the sum of the two bricks below it. If the 4-brick bottom row is {m(f'({a4},\\; x,\\; x,\\; {d4})')} and the single top brick is {m(top4)}, find {m('x')}.",
            f"في هرم أعداد جمعي من **4 صفوف**، كل خانة فوق القاعدة تساوي مجموع الخانتين تحتها مباشرة. إذا كان صف القاعدة الرباعي {m(f'({a4},\\; x,\\; x,\\; {d4})')} وكانت قمة الهرم {m(top4)}، فأوجد قيمة {m('x')}.",
            x4, [x4 + 2, x4 - 2, (top4 - a4 - d4) // 2, x4 + 3],
            f"Build upward row by row in terms of {m('x')}: in a 4-row pyramid with base {m('(a, b, c, d)')}, the top equals {m('a + 3b + 3c + d')}!",
            f"اصعد صفاً بصف بدلالة {m('x')}: في هرم من 4 صفوف قاعدته {m('(a, b, c, d)')} تكون القمة {m('a + 3b + 3c + d')}!",
            f"Trace the 4 rows upward using Pascal weights {m('(1, 3, 3, 1)')}!",
            [
                f"Row 2 (from bottom) is {m(f'({a4}+x,\\; 2x,\\; x+{d4})')}.",
                f"Row 3 is {m(f'({a4}+3x,\\; 3x+{d4})')}, and Row 4 (top) is {m(f'{a4} + 6x + {d4} = {top4}')}.",
                f"Thus {m(f'6x = {6 * x4} \\implies x = {x4}')}.",
            ],
            f"Numeric check: {m(f'({a4}, {x4}, {x4}, {d4}) \\to ({a4+x4}, {2*x4}, {x4+d4}) \\to ({a4+3*x4}, {3*x4+d4}) \\to {top4}')}!",
            f"نصعد من القاعدة إلى القمة فنجد أن القمة تساوي {m(f'{a4} + 6x + {d4}')}!",
            [
                f"الصف الثاني {m(f'({a4}+x,\\; 2x,\\; x+{d4})')}، والثالث {m(f'({a4}+3x,\\; 3x+{d4})')}.",
                f"القمة تساوي {m(f'6x + {a4 + d4} = {top4} \\implies 6x = {6*x4} \\implies x = {x4}')}.",
            ],
            f"تحقق: التعويض بـ {m(f'x = {x4}')} يعطي القمة {m(top4)} بالضبط!",
            diagram_en=svg_number_pyramid(str(top4), f"{a4}+3x", f"3x+{d4}", f"{a4}+x", "2x", f"x+{d4}"),
        )

    # 15. nsmo_g7_custom_binary_operation (5E, 6M, 4H) — SVG: svg_function_machine on Easy & Hard
    bp = "nsmo_g7_custom_binary_operation"
    easy_ops = [
        (3, 2, 5, 7, 4),   # 3a + 2b - 5 at (7,4) = 24
        (4, 1, 3, 6, 9),   # 4a + b - 3 at (6,9) = 30
        (2, 5, 4, 8, 3),   # 2a + 5b - 4 at (8,3) = 27
        (5, 3, 7, 4, 6),   # 5a + 3b - 7 at (4,6) = 31
        (3, 4, 6, 9, 5),   # 3a + 4b - 6 at (9,5) = 41
    ]
    for p, q, r, a_v, b_v in easy_ops:
        ans = p * a_v + q * b_v - r
        q_tex = "b" if q == 1 else f"{q}b"
        B.add_math(
            tp, "Easy", bp,
            f"For any numbers {m('a')} and {m('b')}, define the custom operation {m(f'a \\star b = {p}a + {q_tex} - {r}')}. What is the value of {m(f'{a_v} \\star {b_v}')}?",
            f"لأي عددين {m('a')} و{m('b')} نعرّف العملية {m(f'a \\star b = {p}a + {q_tex} - {r}')}. ما قيمة {m(f'{a_v} \\star {b_v}')}؟",
            ans, [p * b_v + q * a_v - r, ans + 2 * r, ans - r, p * a_v + q * b_v],
            f"Substitute {m(f'a = {a_v}')} and {m(f'b = {b_v}')} directly into {m(f'{p}a + {q_tex} - {r}')}!",
            f"عوّض مباشرة بـ {m(f'a = {a_v}')} و{m(f'b = {b_v}')} في القاعدة {m(f'{p}a + {q_tex} - {r}')}!",
            f"Plug {m(f'a = {a_v}')} into the first slot and {m(f'b = {b_v}')} into the second slot!",
            [
                f"Compute {m(f'{a_v} \\star {b_v} = {p}({a_v}) + {q}({b_v}) - {r} = {p*a_v} + {q*b_v} - {r} = {ans}')}.",
            ],
            f"Order check: {m(f'a={a_v}')} first and {m(f'b={b_v}')} second gives {m(ans)}!",
            f"نعوّض بالعدد الأول مكان {m('a')} وبالثاني مكان {m('b')}!",
            [
                f"نحسب {m(f'{p} \\times {a_v} + {q} \\times {b_v} - {r} = {p*a_v} + {q*b_v} - {r} = {ans}')}.",
            ],
            f"تحقق: الناتج يساوي {m(ans)} بالضبط!",
            diagram_en=svg_function_machine(f"{a_v} ★ {b_v}", f"{p}a + {q}b", f"− {r}", str(ans)),
        )

    med_ops = [
        (3, 4, 2),   # x ⊕ y = x*y - x + y: (3⊕4)⊕2 -> (12-3+4)=13 -> 13⊕2 = 26-13+2 = 15
        (2, 5, 3),   # (10-2+5)=13 -> 13⊕3 = 39-13+3 = 29
        (4, 3, 5),   # (12-4+3)=11 -> 11⊕5 = 55-11+5 = 49
        (5, 2, 4),   # (10-5+2)=7 -> 7⊕4 = 28-7+4 = 25
        (3, 5, 4),   # (15-3+5)=17 -> 17⊕4 = 68-17+4 = 55
        (6, 2, 3),   # (12-6+2)=8 -> 8⊕3 = 24-8+3 = 19
    ]
    for a_v, b_v, c_v in med_ops:
        inner = a_v * b_v - a_v + b_v
        ans = inner * c_v - inner + c_v
        B.add_math(
            tp, "Medium", bp,
            f"Define the operation {m('x \\oplus y = xy - x + y')}. Evaluate {m(f'({a_v} \\oplus {b_v}) \\oplus {c_v}')}.",
            f"نعرّف العملية {m('x \\oplus y = xy - x + y')}. احسب قيمة {m(f'({a_v} \\oplus {b_v}) \\oplus {c_v}')}.",
            ans, [inner, ans + 2 * inner - 4, a_v * (b_v * c_v - b_v + c_v), ans - c_v],
            f"Evaluate the inner parentheses {m(f'{a_v} \\oplus {b_v}')} first, then apply {m('\\oplus')} with {m(c_v)} on the right!",
            f"احسب القوس الداخلي {m(f'{a_v} \\oplus {b_v}')} أولاً، ثم طبّق العملية مع {m(c_v)} عن اليمين!",
            f"Work from inside out, keeping slot order strict!",
            [
                f"Inner bracket: {m(f'{a_v} \\oplus {b_v} = {a_v}\\times {b_v} - {a_v} + {b_v} = {inner}')}.",
                f"Outer operation: {m(f'{inner} \\oplus {c_v} = {inner}\\times {c_v} - {inner} + {c_v} = {ans}')}.",
            ],
            f"Notice {m('x \\oplus y')} is **not** commutative ({m(f'{inner} \\oplus {c_v} = {ans}')})!",
            f"نحسب ما داخل القوس أولاً ثم نطبّق العملية مرة ثانية بالترتيب نفسه!",
            [
                f"القوس الداخلي: {m(f'{a_v} \\oplus {b_v} = {a_v*b_v} - {a_v} + {b_v} = {inner}')}.",
                f"الخطوة الثانية: {m(f'{inner} \\oplus {c_v} = {inner*c_v} - {inner} + {c_v} = {ans}')}.",
            ],
            f"تحقق: الترتيب الدقيق يعطي {m(ans)}!",
        )

    for x_sol, b1, b2 in [(6, 3, 4), (8, 2, 5), (5, 7, 3), (9, 4, 2)]:
        # Op: a ◇ b = 2a + b - 3
        mid_v = 2 * x_sol + b1 - 3
        target_v = 2 * mid_v + b2 - 3
        assert [x for x in range(-50, 200) if 2 * (2 * x + b1 - 3) + b2 - 3 == target_v] == [x_sol]
        B.add_math(
            tp, "Hard", bp,
            f"Let {m('a \\diamond b = 2a + b - 3')} for all integers {m('a, b')}. If {m(f'(x \\diamond {b1}) \\diamond {b2} = {target_v}')}, what is the value of {m('x')}?",
            f"لتكن العملية {m('a \\diamond b = 2a + b - 3')} لجميع الأعداد الصحيحة {m('a, b')}. إذا كان {m(f'(x \\diamond {b1}) \\diamond {b2} = {target_v}')}، فما قيمة {m('x')}؟",
            x_sol, [mid_v, x_sol + 2, x_sol - 2, (target_v + 3) // 4],
            f"Let {m(f'u = x \\diamond {b1}')}: first solve {m(f'u \\diamond {b2} = 2u + {b2} - 3 = {target_v}')} for {m('u')}, then solve for {m('x')}!",
            f"افرض {m(f'u = x \\diamond {b1}')}: حل المعادلة الخارجية {m(f'2u + {b2} - 3 = {target_v}')} لإيجاد {m('u')} أولاً ثم أوجد {m('x')}!",
            f"Unwrap the nested custom operation from outside in!",
            [
                f"Set {m(f'u = x \\diamond {b1}')}. Then {m(f'u \\diamond {b2} = 2u + {b2} - 3 = {target_v} \\implies 2u = {2 * mid_v} \\implies u = {mid_v}')}.",
                f"Now solve {m(f'x \\diamond {b1} = 2x + {b1} - 3 = {mid_v} \\implies 2x = {2 * x_sol} \\implies x = {x_sol}')}.",
            ],
            f"Forward check: {m(f'{x_sol} \\diamond {b1} = {mid_v}')} and {m(f'{mid_v} \\diamond {b2} = {target_v}')}!",
            f"نفكّ التداخل من الخارج إلى الداخل بفرض {m(f'u = x \\diamond {b1}')}!",
            [
                f"من {m(f'2u + {b2} - 3 = {target_v}')} نجد {m(f'u = {mid_v}')}.",
                f"ثم من {m(f'2x + {b1} - 3 = {mid_v}')} نجد {m(f'x = {x_sol}')}.",
            ],
            f"تحقق أمامي: {m(f'({x_sol} \\diamond {b1}) \\diamond {b2} = {mid_v} \\diamond {b2} = {target_v}')}!",
            diagram_en=svg_function_machine("x", f"◇ {b1}", f"◇ {b2}", str(target_v)),
        )


# =============================================================================
# UNIT 1.4 — Olympiad Word Problems: Motion, Work, Ages & Averages (75 Qs)
# =============================================================================
def _add_unit_1_4(B: BankBuilder) -> None:
    tp = "Algebra"

    # 16. nsmo_g7_age_difference_invariant (5E, 6M, 4H) — SVG: svg_number_strip on Easy
    bp = "nsmo_g7_age_difference_invariant"
    easy_ages = [
        (38, 8, 3, "an older cousin", "his younger cousin"),   # diff=30 -> 2s=30 -> s=15 -> in 7 yrs
        (45, 9, 4, "an aunt", "her niece"),                    # diff=36 -> 3s=36 -> s=12 -> in 3 yrs
        (50, 14, 3, "a robotics mentor", "his student"),       # diff=36 -> 2s=36 -> s=18 -> in 4 yrs
        (44, 12, 3, "a mother", "her daughter"),               # diff=32 -> 2s=32 -> s=16 -> in 4? make distinct: (46, 10, 3) -> diff=36 -> s=18 -> 8 yrs
        (52, 7, 4, "an uncle", "his nephew"),                  # diff=45 -> 3s=45 -> s=15 -> in 8 yrs
    ]
    easy_ages = [
        (38, 8, 3, "an older brother", "his younger brother"),
        (45, 9, 4, "an aunt", "her niece"),
        (50, 14, 3, "a science coach", "his apprentice"),
        (46, 10, 3, "a mother", "her daughter"),
        (53, 8, 4, "an uncle", "his nephew"),
    ]
    for A, Y, mult, p1_en, p2_en in easy_ages:
        gap = A - Y
        y_fut = gap // (mult - 1)
        ans = y_fut - Y
        assert A + ans == mult * (Y + ans)
        B.add_math(
            tp, "Easy", bp,
            f"Today, {p1_en} is {m(A)} years old and {p2_en} is {m(Y)} years old. In how many years from now will the elder be **{m(mult)} times** as old as the younger?",
            f"اليوم عمر الأكبر {m(A)} سنة وعمر الأصغر {m(Y)} سنوات. بعد كم سنة من الآن يصبح عمر الأكبر **{m(mult)} أمثال** عمر الأصغر؟",
            ans, [y_fut, ans + 2, ans - 2 if ans > 2 else ans + 5, gap // mult],
            f"Their age difference {m(f'{A} - {Y} = {gap}')} stays constant forever and will equal {m(f'({mult} - 1)')} times the younger's future age!",
            f"فرق العمر بينهما {m(f'{A} - {Y} = {gap}')} ثابت للأبد، وسيمثّل {m(f'({mult} - 1)')} أمثال عمر الأصغر مستقبلاً!",
            f"Use the constant age gap {m(gap)} to find the younger person's future age first!",
            [
                f"Age difference is {m(f'{A} - {Y} = {gap}')} years at every point in time.",
                f"When the elder is {m(f'{mult}u')} and the younger is {m('u')}, {m(f'{mult}u - u = {mult - 1}u = {gap} \\implies u = {y_fut}')}.",
                f"Years from today = {m(f'{y_fut} - {Y} = {ans}')} years.",
            ],
            f"Check: in {m(ans)} years their ages are {m(A + ans)} and {m(Y + ans)}, and {m(f'{mult} \\times {Y + ans} = {A + ans}')}!",
            f"نستغل ثبات فرق العمر {m(gap)} سنة لإيجاد عمر الأصغر عند تحقق النسبة!",
            [
                f"الفرق الثابت {m(gap)} يقابل {m(f'{mult - 1}u')}، ومنه عمر الأصغر حينئذٍ {m(f'u = {y_fut}')} سنة.",
                f"عدد السنوات المطلوبة = {m(f'{y_fut} - {Y} = {ans}')} سنوات.",
            ],
            f"تحقق: {m(f'{A + ans} = {mult} \\times {Y + ans}')}!",
            diagram_en=svg_number_strip([f"Gap = {gap}", f"{mult}u − u", f"u = {y_fut}", f"+{ans} yr"]),
        )

    med_ages = [
        # (past_ago, k_past, fut_ahead, k_fut, young_now)
        # Check: E - past = k_past*(Y - past) and E + fut = k_fut*(Y + fut)
        (2, 5, 4, 3, 8),    # 2 yrs ago: Y=6, E=30 -> now Y=8, E=32; in 4 yrs: Y=12, E=36 = 3*12!
        (3, 4, 5, 2, 11),   # 3 yrs ago: Y=8, E=32 -> now Y=11, E=35; in 5 yrs: Y=16, E=40 no! Wait: k_past*(Y-p)+p = k_fut*(Y+f)-f!
    ]
    # Generate 6 exact verified tuples!
    med_age_specs = [
        (2, 5, 4, 3),   # 5(Y-2)+2 = 3(Y+4)-4 -> 5Y-8 = 3Y+8 -> 2Y=16 -> Y=8 (E=32)
        (3, 4, 3, 2),   # 4(Y-3)+3 = 2(Y+3)-3 -> 4Y-9 = 2Y+3 -> 2Y=12 -> Y=6 (E=15)
        (4, 5, 2, 3),   # 5(Y-4)+4 = 3(Y+2)-2 -> 5Y-16 = 3Y+4 -> 2Y=20 -> Y=10 (E=34)
        (3, 6, 3, 3),   # 6(Y-3)+3 = 3(Y+3)-3 -> 6Y-15 = 3Y+6 -> 3Y=21 -> Y=7 (E=27)
        (5, 4, 5, 2),   # 4(Y-5)+5 = 2(Y+5)-5 -> 4Y-15 = 2Y+5 -> 2Y=20 -> Y=10 (E=25)
        (2, 7, 6, 3),   # 7(Y-2)+2 = 3(Y+6)-6 -> 7Y-12 = 3Y+12 -> 4Y=24 -> Y=6 (E=30)
    ]
    for p_ago, k1, f_ahd, k2 in med_age_specs:
        sols = [y for y in range(p_ago + 1, 80) if k1 * (y - p_ago) + p_ago == k2 * (y + f_ahd) - f_ahd]
        assert len(sols) == 1
        Y_now = sols[0]
        E_now = k1 * (Y_now - p_ago) + p_ago
        B.add_math(
            tp, "Medium", bp,
            f"{m(p_ago)} years ago, Khaled's father was {m(k1)} times as old as Khaled. In {m(f_ahd)} years from now, his father will be {m(k2)} times as old as Khaled. How old is **Khaled's father** today?",
            f"قبل {m(p_ago)} سنوات كان عمر والد خالد {m(k1)} أمثال عمر خالد. وبعد {m(f_ahd)} سنوات من الآن سيصبح عمر والده {m(k2)} أمثال عمره. كم عمر **والد خالد** اليوم؟",
            E_now, [Y_now, E_now - p_ago, E_now + f_ahd, E_now + 4],
            f"Let Khaled's age today be {m('y')}: equate the father's current age from both clues: {m(f'{k1}(y - {p_ago}) + {p_ago} = {k2}(y + {f_ahd}) - {f_ahd}')}!",
            f"افرض عمر خالد اليوم {m('y')} وساوِ بين تعبيرَي عمر الأب اليوم من المعلومتين!",
            f"Express the father's present age in terms of Khaled's present age {m('y')} using both time points!",
            [
                f"From {m(p_ago)} years ago, Khaled was {m(f'y - {p_ago}')} and his father was {m(f'{k1}(y - {p_ago})')}, so today the father is {m(f'{k1}(y - {p_ago}) + {p_ago}')}.",
                f"From {m(f_ahd)} years ahead, the father will be {m(f'{k2}(y + {f_ahd})')}, so today he is {m(f'{k2}(y + {f_ahd}) - {f_ahd}')}.",
                f"Equating gives {m(f'y = {Y_now}')}, so the father's age today is {m(E_now)}.",
            ],
            f"Check: {m(p_ago)} yrs ago ({m(E_now - p_ago)} vs {m(Y_now - p_ago)}), {m(f_ahd)} yrs ahead ({m(E_now + f_ahd)} vs {m(Y_now + f_ahd)})!",
            f"نكتب عمر الأب اليوم بطريقتين بدلالة عمر خالد الحالي {m('y')}!",
            [
                f"من المعلومة الأولى عمر الأب اليوم {m(f'{k1}(y - {p_ago}) + {p_ago}')}، ومن الثانية {m(f'{k2}(y + {f_ahd}) - {f_ahd}')}.",
                f"بالمساواة نجد {m(f'y = {Y_now}')}، وبالتالي عمر الأب اليوم = {m(E_now)} سنة.",
            ],
            f"تحقق: قبل {m(p_ago)} سنوات {m(f'{E_now - p_ago} = {k1} \\times {Y_now - p_ago}')} وبعد {m(f_ahd)} سنوات {m(f'{E_now + f_ahd} = {k2} \\times {Y_now + f_ahd}')}!",
        )

    for P_age, c_sum, n_kids in [(40, 16, 3), (44, 18, 3), (49, 19, 4), (52, 16, 4)]:
        # Parent gains +1/yr, n_kids together gain +n_kids/yr -> gap closes by (n_kids - 1)/yr!
        gap = P_age - c_sum
        assert gap % (n_kids - 1) == 0
        ans = gap // (n_kids - 1)
        B.add_math(
            tp, "Hard", bp,
            f"Today a father is {m(P_age)} years old, and the sum of the ages of his {m(n_kids)} children is {m(c_sum)}. In how many years from now will the father's age equal the **sum of his {m(n_kids)} children's ages**?",
            f"عمر أب اليوم {m(P_age)} سنة، ومجموع أعمار أبنائه الـ {m(n_kids)} هو {m(c_sum)} سنة. بعد كم سنة من الآن يصبح عمر الأب مساوياً **لمجموع أعمار أبنائه الـ {m(n_kids)}**؟",
            ans, [gap, ans + 2, ans * 2, gap // n_kids if gap % n_kids == 0 else ans + 3],
            f"Careful! In {m('t')} years, the father's age increases by {m('t')}, while the sum of {m(n_kids)} children's ages increases by {m(f'{n_kids}t')}!",
            f"انتبه! بعد {m('t')} سنة يزداد عمر الأب بمقدار {m('t')}، بينما يزداد مجموع أعمار الأبناء الـ {m(n_kids)} بمقدار {m(f'{n_kids}t')}!",
            f"Set {m(f'{P_age} + t = {c_sum} + {n_kids}t')} and solve for {m('t')}!",
            [
                f"After {m('t')} years, the father's age will be {m(f'{P_age} + t')}.",
                f"Each of the {m(n_kids)} children ages by {m('t')} years, so their combined sum becomes {m(f'{c_sum} + {n_kids}t')}.",
                f"Equating gives {m(f'{n_kids - 1}t = {P_age} - {c_sum} = {gap} \\implies t = {ans}')} years.",
            ],
            f"Check: in {m(ans)} years the father is {m(P_age + ans)} and the children's ages sum to {m(f'{c_sum} + {n_kids}\\times {ans} = {c_sum + n_kids*ans}')}!",
            f"بعد {m('t')} سنة يزداد مجموع الأبناء بمقدار {m(f'{n_kids}t')} مقابل {m('t')} فقط للأب!",
            [
                f"نضع المعادلة {m(f'{P_age} + t = {c_sum} + {n_kids}t')}.",
                f"ومنه {m(f'{n_kids - 1}t = {gap} \\implies t = {ans}')} سنوات.",
            ],
            f"تحقق: {m(f'{P_age} + {ans} = {c_sum} + {n_kids}\\times {ans} = {P_age + ans}')}!",
        )

    # 17. nsmo_g7_relative_speed_trains (5E, 6M, 4H) — SVG: svg_motion_timeline
    bp = "nsmo_g7_relative_speed_trains"
    easy_meet = [
        (360, 75, 45),   # 3 h
        (450, 85, 65),   # 3 h -> ask faster distance? Let's vary!
        (520, 70, 60),   # 4 h
        (630, 110, 100), # 3 h -> make times distinct: (630, 95, 85)? 180 no; (720, 95, 85) -> 4h; (650, 75, 55) -> 5h; (840, 80, 60) -> 6h!
    ]
    easy_meet = [(360, 75, 45), (520, 70, 60), (650, 75, 55), (840, 80, 60), (540, 105, 75)]
    for D, v1, v2 in easy_meet:
        ans = D // (v1 + v2)
        B.add_math(
            tp, "Easy", bp,
            f"Two express buses start at the same time from two stations {m(D)} km apart and travel directly toward each other at constant speeds of {m(v1)} km/h and {m(v2)} km/h. After how many **hours** do they meet?",
            f"انطلقت حافلتان سريعتان في اللحظة نفسها من محطتين المسافة بينهما {m(D)} كم باتجاهين متقابلين بسرعتين ثابتتين {m(v1)} كم/س و{m(v2)} كم/س. بعد كم **ساعة** تلتقيان؟",
            ans, [D // (v1 - v2) if D % (v1 - v2) == 0 else ans + 3, ans + 1, ans + 2, D // v1 if D % v1 == 0 else ans - 1],
            f"Moving head-on shrinks the gap at their **combined speed** {m(f'{v1} + {v2} = {v1 + v2}')} km/h!",
            f"عند التحرك وجهاً لوجه تتناقص المسافة بمعدل **مجموع السرعتين** {m(f'{v1} + {v2} = {v1 + v2}')} كم/س!",
            f"Divide the initial separation {m(D)} km by {m(f'{v1} + {v2}')}!",
            [
                f"Relative closing speed is {m(f'{v1} + {v2} = {v1 + v2}')} km/h.",
                f"Time to meet = {m(f'{D} \\div {v1 + v2} = {ans}')} hours.",
            ],
            f"Distances covered: {m(f'{v1}\\times {ans} + {v2}\\times {ans} = {v1*ans} + {v2*ans} = {D}')} km!",
            f"نقسم المسافة الكلية {m(D)} كم على مجموع السرعتين {m(v1 + v2)} كم/س!",
            [
                f"السرعة النسبية للتلاقي = {m(f'{v1} + {v2} = {v1 + v2}')} كم/س.",
                f"زمن التلاقي = {m(f'{D} \\div {v1 + v2} = {ans}')} ساعات.",
            ],
            f"تحقق: {m(f'{v1*ans} + {v2*ans} = {D}')} كم!",
            diagram_en=svg_motion_timeline("Station A", "Station B", f"{D} km", f"{v1} km/h", f"{v2} km/h", True),
        )

    med_bridge = [(160, 340, 25), (180, 420, 20), (220, 480, 35)]
    for Lt, Lb, v in med_bridge:
        ans = (Lt + Lb) // v
        B.add_math(
            tp, "Medium", bp,
            f"A freight train {m(Lt)} m long moves at a steady {m(v)} m/s. How many **seconds** does it take to completely cross a {m(Lb)} m viaduct from front-entry to tail-exit?",
            f"قطار شحن طوله {m(Lt)} م يسير بسرعة ثابتة {m(v)} م/ث. كم **ثانية** يستغرق لعبور جسر طوله {m(Lb)} م عبوراً كاملاً منذ دخول مقدمته حتى خروج آخر عربة؟",
            ans, [Lb // v if Lb % v == 0 else ans - 5, (Lb - Lt) // v, ans + 4, ans - 2],
            f"Add the train's own length {m(Lt)} m to the viaduct length {m(Lb)} m before dividing by {m(v)} m/s!",
            f"أضف طول القطار {m(Lt)} م إلى طول الجسر {m(Lb)} م قبل القسمة على السرعة {m(v)} م/ث!",
            f"Compute {m(f'({Lt} + {Lb}) \\div {v}')}!",
            [
                f"Total distance traveled by the front of the train is {m(f'{Lt} + {Lb} = {Lt + Lb}')} m.",
                f"Time required = {m(f'{Lt + Lb} \\div {v} = {ans}')} seconds.",
            ],
            f"In {m(ans)} s at {m(v)} m/s, the train advances {m(Lt + Lb)} m, clearing the bridge completely!",
            f"نجمع طول القطار وطول الجسر ثم نقسم على السرعة!",
            [
                f"المسافة اللازمة للعبور الكامل = {m(f'{Lt} + {Lb} = {Lt + Lb}')} م.",
                f"الزمن = {m(f'{Lt + Lb} \\div {v} = {ans}')} ثانية.",
            ],
            f"تحقق: {m(f'{ans} \\times {v} = {Lt + Lb}')} م!",
            diagram_en=svg_motion_timeline(f"Train {Lt}m", f"Bridge {Lb}m", f"{Lt+Lb} m", f"{v} m/s", "", False),
        )

    med_chase = [(60, 2, 90), (50, 3, 80), (70, 2, 105)]
    for vs, dt, vf in med_chase:
        lead = vs * dt
        ans = lead // (vf - vs)
        B.add_math(
            tp, "Medium", bp,
            f"A delivery van leaves Riyadh at {m(vs)} km/h. Exactly {m(dt)} hours later, a patrol car leaves from the same point along the same highway at {m(vf)} km/h. How many **hours after the patrol car starts** does it catch up to the van?",
            f"انطلقت شاحنة توصيل من الرياض بسرعة {m(vs)} كم/س، وبعد {m(dt)} ساعات انطلقت سيارة دورية من النقطة نفسها وعلى الطريق نفسه بسرعة {m(vf)} كم/س. بعد كم **ساعة من انطلاق سيارة الدورية** تلحق بالشاحنة؟",
            ans, [ans + dt, lead // vf if lead % vf == 0 else ans + 1, ans - 1, ans + 3],
            f"First compute the van's head start {m(f'{vs} \\times {dt} = {lead}')} km, then divide by the speed difference {m(f'{vf} - {vs}')}!",
            f"احسب أولاً المسافة التي سبقت بها الشاحنة {m(f'{vs} \\times {dt} = {lead}')} كم، ثم اقسم على فرق السرعتين {m(f'{vf} - {vs}')}!",
            f"Divide the head-start gap {m(lead)} km by the catch-up rate {m(vf - vs)} km/h!",
            [
                f"During the {m(dt)}-hour head start, the van travels {m(f'{vs} \\times {dt} = {lead}')} km.",
                f"The patrol car closes that gap at {m(f'{vf} - {vs} = {vf - vs}')} km/h.",
                f"Catch-up time = {m(f'{lead} \\div {vf - vs} = {ans}')} hours.",
            ],
            f"Distance check: van travels {m(f'{vs}\\times({dt}+{ans}) = {vs*(dt+ans)}')}, patrol travels {m(f'{vf}\\times {ans} = {vf*ans}')} km!",
            f"نقسم مسافة السبق {m(lead)} كم على فرق السرعتين {m(vf - vs)} كم/س!",
            [
                f"المسافة الفاصلة عند انطلاق الدورية = {m(f'{vs} \\times {dt} = {lead}')} كم.",
                f"معدل اللحاق = {m(f'{vf} - {vs} = {vf - vs}')} كم/س، فزمن اللحاق = {m(ans)} ساعات.",
            ],
            f"تحقق: كلاهما يقطع {m(vf * ans)} كم من نقطة البداية!",
            diagram_en=svg_motion_timeline("Start", f"Lead {lead}km", f"{lead} km", f"{vf}", f"{vs}", False),
        )

    hard_2trains = [
        (130, 170, 22, 18, "opposite"),   # 300 / 40 no -> make integer! (140, 180, 22, 18) -> 320 / 40 = 8 s
        (150, 210, 25, 20, "opposite"),   # 360 / 45 = 8? make distinct: (165, 195, 24, 16) -> 360 / 40 = 9 s
        (120, 160, 28, 14, "same"),       # 280 / 14 = 20 s
        (150, 180, 32, 17, "same"),       # 330 / 15 = 22 s
    ]
    hard_2trains = [
        (140, 180, 22, 18, "opposite"),
        (165, 195, 24, 16, "opposite"),
        (120, 160, 28, 14, "same"),
        (150, 180, 32, 17, "same"),
    ]
    for L1, L2, v1, v2, mode in hard_2trains:
        rel_v = (v1 + v2) if mode == "opposite" else (v1 - v2)
        ans = (L1 + L2) // rel_v
        dir_en = "in **opposite directions** toward each other" if mode == "opposite" else "in the **same direction** (the faster overtaking the slower)"
        dir_ar = "**باتجاهين متعاكسين**" if mode == "opposite" else "**في الاتجاه نفسه** (يتجاوز الأسرعُ الأبطأ)"
        op_sym = "+" if mode == "opposite" else "-"
        B.add_math(
            tp, "Hard", bp,
            f"On parallel tracks, Train A (length {m(L1)} m, speed {m(v1)} m/s) and Train B (length {m(L2)} m, speed {m(v2)} m/s) travel {dir_en}. How many **seconds** elapse from the instant they start passing each other until they completely clear each other?",
            f"على سكتين متوازيتين يسير القطار أ (طوله {m(L1)} م وسرعته {m(v1)} م/ث) والقطار ب (طوله {m(L2)} م وسرعته {m(v2)} م/ث) {dir_ar}. كم **ثانية** تمر منذ لحظة بدء التجاوز/التقابل حتى ينفصلا تماماً؟",
            ans, [(L1 + L2) // (v1 + v2 if mode == "same" else v1 - v2 + 1), ans + 4, ans - 2, L2 // rel_v + 3],
            f"Regardless of direction, the relative distance to clear both trains is **always** {m(f'{L1} + {L2} = {L1 + L2}')} m; divide by {m(f'{v1} {op_sym} {v2}')}!",
            f"سواءً أكانا متعاكسين أم في الاتجاه نفسه، المسافة النسبية اللازمة هي **دائماً مجموع الطولين** {m(f'{L1} + {L2} = {L1 + L2}')} م؛ اقسمها على السرعة النسبية!",
            f"Combine total train lengths {m(L1 + L2)} m and divide by relative speed {m(rel_v)} m/s!",
            [
                f"To pass completely, one train must move {m(f'{L1} + {L2} = {L1 + L2}')} m relative to the other.",
                f"Their relative speed is {m(f'{v1} {op_sym} {v2} = {rel_v}')} m/s.",
                f"Time to clear = {m(f'{L1 + L2} \\div {rel_v} = {ans}')} seconds.",
            ],
            f"Check: {m(f'{rel_v} \\times {ans} = {L1 + L2}')} m!",
            f"نقسم مجموع طولَي القطارين {m(L1 + L2)} م على السرعة النسبية {m(rel_v)} م/ث!",
            [
                f"المسافة النسبية الكلية = {m(f'{L1} + {L2} = {L1 + L2}')} م.",
                f"السرعة النسبية = {m(f'{v1} {op_sym} {v2} = {rel_v}')} م/ث، فالزمن = {m(ans)} ثانية.",
            ],
            f"تحقق: {m(f'{ans} \\times {rel_v} = {L1 + L2}')} م!",
            diagram_en=svg_motion_timeline(f"{L1}m", f"{L2}m", f"{L1+L2}m", f"{v1}m/s", f"{v2}m/s", mode == "opposite"),
        )

    # 18. nsmo_g7_chicken_rabbit_two_types (5E, 6M, 4H)
    bp = "nsmo_g7_chicken_rabbit_two_types"
    easy_cr = [
        (24, 68, "ostriches (2 legs)", "gazelles (4 legs)", "gazelles", "غزالاً"),
        (30, 84, "bicycles (2 wheels)", "cars (4 wheels)", "cars", "سيارة"),
        (28, 74, "chickens (2 legs)", "rabbits (4 legs)", "rabbits", "أرنباً"),
        (35, 96, "scooters (2 wheels)", "quad-bikes (4 wheels)", "quad-bikes", "دراجة رباعية"),
        (40, 110, "ducks (2 legs)", "sheep (4 legs)", "sheep", "خروفاً"),
    ]
    for heads, legs, t1_en, t2_en, ask_en, ask_ar in easy_cr:
        ans = (legs - 2 * heads) // 2
        assert 2 * (heads - ans) + 4 * ans == legs
        B.add_math(
            tp, "Easy", bp,
            f"A reserve count records {m(heads)} total heads/vehicles consisting of {t1_en} and {t2_en}, with {m(legs)} legs/wheels in total. How many **{ask_en}** are there?",
            f"سُجّل في إحصاء إجمالي {m(heads)} رأساً/مركبة من نوعين (ذوات 2 وذوات 4 أرجل/عجلات) بمجموع كلي قدره {m(legs)} رجلاً/عجلة. كم عدد **{ask_ar}** (ذوات الأربع)؟",
            ans, [heads - ans, ans + 3, ans - 2, legs // 4],
            f"Assume all {m(heads)} have only {m(2)} legs/wheels ({m(2 * heads)} total); each 4-legged/wheeled one adds {m('+2')}!",
            f"افترض أن الـ {m(heads)} جميعها ذات {m(2)} فقط ({m(2 * heads)} إجمالاً)؛ كل عنصر رباعي يضيف {m('+2')}!",
            f"Use the assumption method: subtract {m(2 * heads)} from {m(legs)} and divide by {m('4 - 2 = 2')}!",
            [
                f"If all {m(heads)} had {m(2)} legs/wheels, there would be {m(f'2 \\times {heads} = {2 * heads}')} in total.",
                f"The extra {m(f'{legs} - {2 * heads} = {legs - 2 * heads}')} come from {m('+2')} per {ask_en}.",
                f"Divide by {m(2)}: {m(f'{legs - 2 * heads} \\div 2 = {ans}')}.",
            ],
            f"Check: {m(f'{heads - ans}\\times 2 + {ans}\\times 4 = {2*(heads-ans)} + {4*ans} = {legs}')}!",
            f"نفترض أن الجميع من فئة الـ {m(2)} ثم نقسم الزيادة على الفرق {m(2)}!",
            [
                f"لو كانت جميعها ثنائية لكان المجموع {m(2 * heads)}، والزيادة هي {m(legs - 2 * heads)}.",
                f"بقسمة الزيادة على {m(2)} نجد العدد المطلوب = {m(ans)}.",
            ],
            f"تحقق: {m(f'2({heads - ans}) + 4({ans}) = {legs}')}!",
        )

    med_tickets = [
        (40, 5, 10, 315, "10-riyal notes", "ورقة من فئة 10 ريالات"),
        (50, 10, 25, 830, "25-riyal vouchers", "قسيمة من فئة 25 ريالاً"),
        (36, 15, 35, 820, "adult 35-riyal tickets", "تذكرة كبار (35 ريالاً)"),
        (45, 8, 20, 564, "20-riyal notebooks", "دفتر بسعر 20 ريالاً"),
        (30, 12, 30, 594, "30-riyal boxes", "صندوق بسعر 30 ريالاً"),
        (60, 5, 20, 645, "20-riyal coins/notes", "ورقة من فئة 20 ريالاً"),
    ]
    for N, v_lo, v_hi, tot_val, ask_en, ask_ar in med_tickets:
        ans = (tot_val - N * v_lo) // (v_hi - v_lo)
        assert (N - ans) * v_lo + ans * v_hi == tot_val
        B.add_math(
            tp, "Medium", bp,
            f"A cashier counts {m(N)} items made up of {m(v_lo)}-riyal and {m(v_hi)}-riyal denominations worth {m(tot_val)} riyals altogether. How many **{ask_en}** are in the stack?",
            f"عدّ أمين الصندوق {m(N)} عنصراً من فئتَي {m(v_lo)} ريالات و{m(v_hi)} ريالاً بقيمة إجمالية {m(tot_val)} ريالاً. كم **{ask_ar}** في المجموعة؟",
            ans, [N - ans, ans + 3, ans - 2, tot_val // v_hi],
            f"Assume all {m(N)} items cost {m(v_lo)} riyals ({m(N * v_lo)} riyals), then divide the excess by {m(f'{v_hi} - {v_lo} = {v_hi - v_lo}')}!",
            f"افترض أن الـ {m(N)} كلها من فئة {m(v_lo)} ريالات، ثم اقسم الفائض على فرق السعرين {m(v_hi - v_lo)}!",
            f"Compute {m(f'({tot_val} - {N}\\times {v_lo}) \\div ({v_hi} - {v_lo})')}!",
            [
                f"Assuming all {m(N)} items are {m(v_lo)} riyals gives {m(f'{N} \\times {v_lo} = {N * v_lo}')} riyals.",
                f"Excess value is {m(f'{tot_val} - {N * v_lo} = {tot_val - N * v_lo}')} riyals, and each upgrade to {m(v_hi)} riyals adds {m(v_hi - v_lo)} riyals.",
                f"Count of {m(v_hi)}-riyal items = {m(f'{tot_val - N * v_lo} \\div {v_hi - v_lo} = {ans}')}.",
            ],
            f"Check: {m(f'{N - ans}\\times {v_lo} + {ans}\\times {v_hi} = {tot_val}')} riyals!",
            f"نحسب قيمة الافتراض الأدنى {m(N * v_lo)} ريالاً ثم نقسم الفائض على {m(v_hi - v_lo)}!",
            [
                f"الفائض فوق الافتراض الأدنى = {m(f'{tot_val} - {N * v_lo} = {tot_val - N * v_lo}')} ريالاً.",
                f"بقسمته على فرق الفئتين {m(v_hi - v_lo)} نحصل على {m(ans)}.",
            ],
            f"تحقق: {m(f'{N - ans}\\times {v_lo} + {ans}\\times {v_hi} = {tot_val}')}!",
        )

    for Q_tot, gain, pen, corr in [(25, 5, 2, 19), (30, 4, 1, 23), (20, 6, 2, 15), (25, 6, 3, 18)]:
        wrong = Q_tot - corr
        score = corr * gain - wrong * pen
        B.add_math(
            tp, "Hard", bp,
            f"In a {m(Q_tot)}-question Olympiad round, each correct answer earns {m(f'+{gain}')} points and each wrong answer deducts {m(pen)} points (no blanks). A contestant answered all {m(Q_tot)} questions and scored {m(score)} points. How many questions did they answer **correctly**?",
            f"في جولة أولمبياد مكوّنة من {m(Q_tot)} سؤالاً، تمنح الإجابة الصحيحة {m(f'+{gain}')} نقاط وتخصم الإجابة الخاطئة {m(pen)} نقاط (دون ترك أسئلة فارغة). أجاب متسابق عن جميع الأسئلة وحصل على {m(score)} نقطة. كم سؤالاً أجاب عنه **بصورة صحيحة**؟",
            corr, [Q_tot - (Q_tot * gain - score) // gain if (Q_tot * gain - score) % gain == 0 else corr + 2, corr - 2, corr + 1, wrong],
            f"Watch the sign! Changing one correct answer ({m(f'+{gain}')}) into a wrong answer ({m(f'-{pen}')}) drops the score by {m(f'{gain} + {pen} = {gain + pen}')} points, **not** {m(gain - pen)}!",
            f"انتبه للإشارة! تحوّل إجابة صحيحة ({m(f'+{gain}')}) إلى خاطئة ({m(f'-{pen}')}) ينقص المجموع بمقدار {m(f'{gain} + {pen} = {gain + pen}')} نقاط وليس {m(gain - pen)}!",
            f"Start from a perfect score {m(Q_tot * gain)} and divide the lost points by {m(gain + pen)}!",
            [
                f"A perfect score on all {m(Q_tot)} questions is {m(f'{Q_tot} \\times {gain} = {Q_tot * gain}')} points.",
                f"Each wrong answer forfeits the {m(gain)} gain **and** incurs a {m(pen)} penalty, losing {m(f'{gain} + {pen} = {gain + pen}')} points.",
                f"Wrong answers = {m(f'({Q_tot * gain} - {score}) \\div {gain + pen} = {wrong}')}, so correct answers = {m(f'{Q_tot} - {wrong} = {corr}')}.",
            ],
            f"Check: {m(f'{corr}\\times {gain} - {wrong}\\times {pen} = {corr*gain} - {wrong*pen} = {score}')}!",
            f"نحسب الدرجة الكاملة {m(Q_tot * gain)} ونقسم النقاط المفقودة على {m(gain + pen)} لمعرفة الأخطاء!",
            [
                f"النقاط المفقودة عن الدرجة الكاملة = {m(f'{Q_tot * gain} - {score} = {Q_tot * gain - score}')}.",
                f"كل خطأ يُفقد {m(gain + pen)} نقاط، فعدد الأخطاء {m(wrong)}، وعدد الإجابات الصحيحة {m(f'{Q_tot} - {wrong} = {corr}')}.",
            ],
            f"تحقق: {m(f'{corr}\\times {gain} - {wrong}\\times {pen} = {score}')} نقطة!",
        )

    # 19. nsmo_g7_work_pipes_combined (5E, 6M, 4H) — SVG: svg_pipe_tank
    bp = "nsmo_g7_work_pipes_combined"
    easy_pipes = [(6, 12), (10, 15), (12, 24), (15, 30), (20, 30)]
    for a, b in easy_pipes:
        rate = Fraction(1, a) + Fraction(1, b)
        ans = int(1 / rate)
        B.add_math(
            tp, "Easy", bp,
            f"Pump A can fill a reservoir in {m(a)} hours alone, and Pump B can fill the same reservoir in {m(b)} hours alone. How many **hours** will it take to fill the empty reservoir when **both** pumps run together?",
            f"تملأ المضخة (أ) خزاناً بمفردها في {m(a)} ساعة، وتملؤه المضخة (ب) بمفردها في {m(b)} ساعة. كم **ساعة** يستغرق ملء الخزان الفارغ عند تشغيل المضختين **معاً**؟",
            ans, [(a + b) // 2, a + b, ans + 2, ans - 1],
            f"Add their hourly rates {m(f'\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}}')}, then take the reciprocal!",
            f"اجمع معدلَي الضخ في الساعة {m(f'\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}}')} ثم اقلب الناتج!",
            f"Combine hourly fractions {m(f'\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{1}}{{{ans}}}')}!",
            [
                f"Hourly rate together is {m(f'\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{{a + b}}}{{{a * b}}} = \\frac{{1}}{{{ans}}}')} of the reservoir per hour.",
                f"Taking the reciprocal gives {m(ans)} hours.",
            ],
            f"In {m(ans)} h, A fills {m(f'{ans}/{a}')} and B fills {m(f'{ans}/{b}')}, summing to {m(1)} full reservoir!",
            f"نجمع معدلي الملء في الساعة الواحدة ثم نقلب الكسر!",
            [
                f"المعدل المشترك = {m(f'\\frac{{1}}{{{a}}} + \\frac{{1}}{{{b}}} = \\frac{{1}}{{{ans}}}')} خزان في الساعة.",
                f"إذن الزمن اللازم = {m(ans)} ساعات.",
            ],
            f"تحقق: {m(f'\\frac{{{ans}}}{{{a}}} + \\frac{{{ans}}}{{{b}}} = 1')}!",
            diagram_en=svg_pipe_tank(f"+1/{a}", f"+1/{b}"),
        )

    med_drain = [(4, 12), (6, 15), (8, 24), (10, 15), (12, 20), (9, 18)]
    for a, b in med_drain:
        net = Fraction(1, a) - Fraction(1, b)
        ans = int(1 / net) if net.numerator == 1 else Fraction(1, 1) / net
        ans_v = int(ans) if isinstance(ans, Fraction) and ans.denominator == 1 else ans
        B.add_math(
            tp, "Medium", bp,
            f"Supply Pipe A fills an empty tank in {m(a)} hours, while Drain Valve B empties a full tank in {m(b)} hours. If both are open simultaneously starting with an empty tank, how many **hours** are needed to fill the tank?",
            f"يملأ أنبوب التغذية (أ) خزاناً فارغاً في {m(a)} ساعات، بينما يفرّغ صمام التصريف (ب) الخزان الممتلئ في {m(b)} ساعة. إذا فُتحا معاً والخزان فارغ، فكم **ساعة** تلزم لامتلاء الخزان؟",
            ans_v, [b - a, a + b, ans_v + 3 if isinstance(ans_v, int) else Fraction(a * b, a + b), ans_v - 2 if isinstance(ans_v, int) else Fraction(b, 2)],
            f"Subtract the drain rate from the fill rate: {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}}')}!",
            f"اطرح معدل التفريغ من معدل التعبئة: {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}}')}!",
            f"Compute net hourly fill rate {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}}')} and invert!",
            [
                f"Net fraction gained per hour is {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}} = \\frac{{{net.numerator}}}{{{net.denominator}}}')}.",
                f"Flipping the net rate gives {m(ans_v)} hours to reach {m(1)} full tank.",
            ],
            f"Verify: {m(ans_v)} hours times {m(f'\\frac{{{net.numerator}}}{{{net.denominator}}}')} equals {m(1)}!",
            f"نحسب صافي الامتلاء في الساعة الواحدة بطرح معدل التفريغ من التعبئة!",
            [
                f"صافي المعدل = {m(f'\\frac{{1}}{{{a}}} - \\frac{{1}}{{{b}}} = \\frac{{{net.numerator}}}{{{net.denominator}}}')} في الساعة.",
                f"الزمن الكلي اللازم يساوي مقلوب المعدل = {m(ans_v)} ساعة.",
            ],
            f"تحقق: حاصل ضرب الزمن في صافي المعدل يساوي {m(1)} خزان كامل!",
            diagram_en=svg_pipe_tank(f"+1/{a}", f"−1/{b}"),
        )

    hard_3work = [
        (12, 15, 20),  # 1/12 + 1/15 + 1/20 = (5+4+3)/60 = 12/60 = 1/5 -> 2*(A+B+C) = 1/5 -> A+B+C = 1/10 -> 10 h!
        (6, 8, 24),    # 1/6 + 1/8 + 1/24 = (4+3+1)/24 = 8/24 = 1/3 -> A+B+C = 1/6 -> 6 h!
        (10, 12, 15),  # 1/10 + 1/12 + 1/15 = (6+5+4)/60 = 15/60 = 1/4 -> A+B+C = 1/8 -> 8 h!
        (18, 24, 72),  # 1/18 + 1/24 + 1/72 = (4+3+1)/72 = 8/72 = 1/9 -> A+B+C = 1/18 -> 18 h!
    ]
    for t_ab, t_bc, t_ac in hard_3work:
        sum_pairs = Fraction(1, t_ab) + Fraction(1, t_bc) + Fraction(1, t_ac)
        rate_all = sum_pairs / 2
        assert rate_all.numerator == 1
        ans = rate_all.denominator
        B.add_math(
            tp, "Hard", bp,
            f"Working in pairs on a robotics build: A and B finish in {m(t_ab)} hours, B and C finish in {m(t_bc)} hours, and A and C finish in {m(t_ac)} hours. How many **hours** will it take if **all three (A, B, and C)** work together?",
            f"عند العمل ثنائياً لبناء روبوت: ينجز (أ وب) العمل في {m(t_ab)} ساعة، وينجز (ب وج) العمل في {m(t_bc)} ساعة، وينجز (أ وج) العمل في {m(t_ac)} ساعة. كم **ساعة** يستغرق إنجاز العمل إذا عمل **الثلاثة (أ وب وج) معاً**؟",
            ans, [ans // 2, ans * 2, (t_ab + t_bc + t_ac) // 3, ans + 4],
            f"Add all three pair rates {m(f'\\frac{{1}}{{{t_ab}}} + \\frac{{1}}{{{t_bc}}} + \\frac{{1}}{{{t_ac}}}')}: each person is counted **twice**, so divide that rate sum by {m(2)}!",
            f"اجمع معدلات الأزواج الثلاثة: كل شخص حُسب **مرتين**، لذا اقسم مجموع المعدلات على {m(2)}!",
            f"Sum the three pair rates to get {m('2(r_A + r_B + r_C)')}, halve it, and invert!",
            [
                f"Adding pair rates: {m(f'2(r_A + r_B + r_C) = \\frac{{1}}{{{t_ab}}} + \\frac{{1}}{{{t_bc}}} + \\frac{{1}}{{{t_ac}}} = \\frac{{{sum_pairs.numerator}}}{{{sum_pairs.denominator}}}')}.",
                f"Divide by {m(2)} to get their combined rate {m(f'r_A + r_B + r_C = \\frac{{1}}{{{ans}}}')} per hour.",
                f"Therefore all three together finish in {m(ans)} hours.",
            ],
            f"Trap avoided: forgetting to divide the rate sum by {m(2)} would give {m(ans // 2)} hours—actual time is {m(ans)} hours!",
            f"نجمع المعدلات الثلاثة ونقسمها على {m(2)} لأن كل عامل تكرر مرتين!",
            [
                f"مجموع المعدلات الزوجية {m(f'2(r_A + r_B + r_C) = \\frac{{{sum_pairs.numerator}}}{{{sum_pairs.denominator}}}')}.",
                f"بالقسمة على {m(2)} يصبح معدل الثلاثة معاً {m(f'\\frac{{1}}{{{ans}}}')}، أي ينهون العمل في {m(ans)} ساعة.",
            ],
            f"تحقق: مقلوب المعدل الثلاثي يعطي {m(ans)} ساعة بالضبط!",
            diagram_en=svg_pipe_tank(f"AB:1/{t_ab}", f"BC:1/{t_bc}"),
        )

    # 20. nsmo_g7_mean_shift_added_score (5E, 6M, 4H) — SVG: svg_bar_chart
    bp = "nsmo_g7_mean_shift_added_score"
    easy_mean = [
        (3, 82, 86),   # 4*86 - 3*82 = 344 - 246 = 98
        (4, 78, 82),   # 5*82 - 4*78 = 410 - 312 = 98? vary ans: (4, 79, 82) -> 410 - 316 = 94
        (5, 84, 86),   # 6*86 - 5*84 = 516 - 420 = 96
        (4, 85, 88),   # 5*88 - 4*85 = 440 - 340 = 100
        (3, 76, 80),   # 4*80 - 3*76 = 320 - 228 = 92
    ]
    easy_mean = [(3, 82, 86), (4, 79, 82), (5, 84, 86), (4, 85, 88), (3, 76, 80)]
    for n_q, m_old, m_new in easy_mean:
        ans = (n_q + 1) * m_new - n_q * m_old
        bars = [(f"Q{i+1}", m_old, str(m_old)) for i in range(min(n_q, 4))] + [(f"Q{n_q+1}", ans, "?")]
        B.add_math(
            tp, "Easy", bp,
            f"Noura's mean score on {m(n_q)} math tests is {m(m_old)}. What score must she get on test {m(n_q + 1)} to raise her mean across all {m(n_q + 1)} tests to {m(m_new)}?",
            f"متوسط درجات نورة في {m(n_q)} اختبارات رياضيات هو {m(m_old)}. ما الدرجة التي يجب أن تحرزها في الاختبار رقم {m(n_q + 1)} ليرتفع متوسطها في الـ {m(n_q + 1)} اختبارات إلى {m(m_new)}؟",
            ans, [m_new + (m_new - m_old), ans - 4, ans - 2, (m_old + m_new) // 2],
            f"Subtract the old total {m(f'{n_q}\\times {m_old}')} from the required new total {m(f'{n_q + 1}\\times {m_new}')}!",
            f"اطرح المجموع القديم {m(f'{n_q}\\times {m_old}')} من المجموع الجديد المطلوب {m(f'{n_q + 1}\\times {m_new}')}!",
            f"Compare total points before ({m(n_q * m_old)}) and after ({m((n_q + 1) * m_new)})!",
            [
                f"Old total across {m(n_q)} tests: {m(f'{n_q} \\times {m_old} = {n_q * m_old}')}.",
                f"Required total across {m(n_q + 1)} tests: {m(f'{n_q + 1} \\times {m_new} = {(n_q + 1) * m_new}')}.",
                f"Needed score = {m(f'{(n_q + 1) * m_new} - {n_q * m_old} = {ans}')}.",
            ],
            f"Check: {m(f'({n_q * m_old} + {ans}) \\div {n_q + 1} = {m_new}')}!",
            f"نطرح المجموع القديم من المجموع المطلوب!",
            [
                f"المجموع القديم = {m(n_q * m_old)}، والمجموع الجديد المطلوب = {m((n_q + 1) * m_new)}.",
                f"الدرجة المطلوبة = {m(f'{(n_q + 1) * m_new} - {n_q * m_old} = {ans}')}.",
            ],
            f"تحقق: {m(f'({n_q * m_old} + {ans}) \\div {n_q + 1} = {m_new}')}!",
            diagram_en=svg_bar_chart(bars, y_max=100),
        )

    med_wmean = [
        (12, 85, 18, 75),  # (1020 + 1350)/30 = 2370/30 = 79
        (10, 90, 15, 80),  # (900 + 1200)/25 = 84
        (14, 78, 21, 88),  # (1092 + 1848)/35 = 2940/35 = 84? vary: (15, 76, 25, 84) -> (1140+2100)/40 = 81
        (8, 92, 12, 77),   # (736 + 924)/20 = 1660/20 = 83
        (16, 70, 24, 85),  # (1120 + 2040)/40 = 3160/40 = 79? vary: (18, 72, 12, 87) -> (1296+1044)/30 = 78
        (9, 88, 15, 72),   # (792 + 1080)/24 = 1872/24 = 78? vary: (9, 91, 18, 76) -> (819+1368)/27 = 2187/27 = 81
    ]
    med_wmean = [
        (12, 85, 18, 75),  # 79
        (10, 90, 15, 80),  # 84
        (15, 76, 25, 84),  # 81
        (8, 92, 12, 77),   # 83
        (18, 72, 12, 87),  # 78
        (16, 91, 24, 76),  # (1456+1824)/40 = 3280/40 = 82
    ]
    for n1, m1, n2, m2 in med_wmean:
        tot_pts = n1 * m1 + n2 * m2
        ans = tot_pts // (n1 + n2)
        assert tot_pts == ans * (n1 + n2)
        B.add_math(
            tp, "Medium", bp,
            f"In a school competition, Section A ({m(n1)} students) has a mean score of {m(m1)}, and Section B ({m(n2)} students) has a mean score of {m(m2)}. What is the **combined mean score** of all {m(n1 + n2)} students?",
            f"في مسابقة مدرسية، متوسط درجات الشعبة أ ({m(n1)} طالباً) هو {m(m1)}، ومتوسط درجات الشعبة ب ({m(n2)} طالباً) هو {m(m2)}. ما **المتوسط الحسابي المشترك** لجميع الطلاب الـ {m(n1 + n2)}؟",
            ans, [(m1 + m2) // 2 if (m1 + m2) // 2 != ans else ans + 2, ans + 1, ans - 1, ans + 3],
            f"Never average {m(m1)} and {m(m2)} directly! Compute {m(f'({n1}\\times {m1} + {n2}\\times {m2}) \\div {n1 + n2}')}!",
            f"لا تأخذ متوسط {m(m1)} و{m(m2)} مباشرة! احسب {m(f'({n1}\\times {m1} + {n2}\\times {m2}) \\div {n1 + n2}')}!",
            f"Sum total points from both sections and divide by total students {m(n1 + n2)}!",
            [
                f"Section A total = {m(f'{n1} \\times {m1} = {n1 * m1}')}, and Section B total = {m(f'{n2} \\times {m2} = {n2 * m2}')}.",
                f"Combined mean = {m(f'\\frac{{{n1 * m1} + {n2 * m2}}}{{{n1 + n2}}} = \\frac{{{tot_pts}}}{{{n1 + n2}}} = {ans}')}.",
            ],
            f"Notice {m(ans)} sits closer to the larger section's mean, as expected!",
            f"نجمع درجات الشعبتين ثم نقسم على مجموع الطلاب {m(n1 + n2)}!",
            [
                f"مجموع الشعبة أ = {m(n1 * m1)} ومجموع الشعبة ب = {m(n2 * m2)}.",
                f"المتوسط المشترك = {m(f'{tot_pts} \\div {n1 + n2} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} \\times {n1 + n2} = {tot_pts}')}!",
            diagram_en=svg_bar_chart([("Sec A", m1, str(m1)), ("Sec B", m2, str(m2)), ("All", ans, "?")], y_max=100),
        )

    for n_all, m_before, m_after in [(7, 24, 21), (8, 30, 27), (9, 35, 32), (10, 42, 39)]:
        ans = n_all * m_before - (n_all - 1) * m_after
        B.add_math(
            tp, "Hard", bp,
            f"The arithmetic mean of {m(n_all)} numbers on a whiteboard is {m(m_before)}. When **one** number is erased, the mean of the remaining {m(n_all - 1)} numbers drops to {m(m_after)}. What number was erased?",
            f"المتوسط الحسابي لـ {m(n_all)} أعداد مكتوبة على السبورة هو {m(m_before)}. عند مسح **عدد واحد** منها انخفض متوسط الأعداد الـ {m(n_all - 1)} المتبقية إلى {m(m_after)}. ما العدد الذي مُسح؟",
            ans, [m_before + (m_before - m_after), ans - m_after, ans + 3, ans - 4],
            f"Erased number = (original sum of {m(n_all)} numbers) minus (remaining sum of {m(n_all - 1)} numbers)!",
            f"العدد الممسوح = (مجموع الـ {m(n_all)} أعداد الأصلي) ناقص (مجموع الـ {m(n_all - 1)} أعداد المتبقية)!",
            f"Compute {m(f'{n_all}\\times {m_before} - {n_all - 1}\\times {m_after}')}!",
            [
                f"Sum of all {m(n_all)} numbers was {m(f'{n_all} \\times {m_before} = {n_all * m_before}')}.",
                f"Sum of the remaining {m(n_all - 1)} numbers is {m(f'{n_all - 1} \\times {m_after} = {(n_all - 1) * m_after}')}.",
                f"The erased number is {m(f'{n_all * m_before} - {(n_all - 1) * m_after} = {ans}')}.",
            ],
            f"Check: {m(f'({(n_all - 1) * m_after} + {ans}) \\div {n_all} = {m_before}')}!",
            f"نطرح مجموع الأعداد المتبقية من المجموع الكلي قبل المسح!",
            [
                f"المجموع قبل المسح = {m(n_all * m_before)}، والمجموع بعد المسح = {m((n_all - 1) * m_after)}.",
                f"العدد الممسوح = {m(f'{n_all * m_before} - {(n_all - 1) * m_after} = {ans}')}.",
            ],
            f"تحقق: إرجاع العدد {m(ans)} يعيد المتوسط إلى {m(m_before)}!",
            diagram_en=svg_bar_chart([("Before", m_before, str(m_before)), ("After", m_after, str(m_after)), ("Erased", ans, "?")], y_max=ans + 10),
        )


# =============================================================================
# UNIT 1.5 — Angles, Paper Folding, Area Cuts & 3D Cubes (75 Qs)
# =============================================================================
def _add_unit_1_5(B: BankBuilder) -> None:
    tp = "Geometry"

    # 21. nsmo_g7_parallel_zigzag_angles (5E, 6M, 4H) — SVG: svg_parallel_zigzag
    bp = "nsmo_g7_parallel_zigzag_angles"
    easy_zig = [(32, 49), (41, 54), (27, 68), (36, 57), (44, 63)]
    for a1, a2 in easy_zig:
        ans = a1 + a2
        B.add_math(
            tp, "Easy", bp,
            f"Between parallel lines {m('L_1 \\parallel L_2')}, a two-segment zigzag makes acute angles of {m(f'{a1}^\\circ')} with {m('L_1')} and {m(f'{a2}^\\circ')} with {m('L_2')} as shown. Find the middle bend angle {m('x')} (in degrees).",
            f"بين المستقيمين المتوازيين {m('L_1 \\parallel L_2')} يصنع خط منكسر زاويتين حادتين قياساهما {m(f'{a1}^\\circ')} مع {m('L_1')} و{m(f'{a2}^\\circ')} مع {m('L_2')} كما في الشكل. أوجد قياس زاوية الانكسار الوسطى {m('x')} بالدرجات.",
            ans, [180 - ans, abs(a2 - a1) + 40, ans + 10, ans - 10],
            f"Draw a line through the middle vertex parallel to {m('L_1')} and {m('L_2')} so alternate interior angles add to {m('x')}!",
            f"ارسم مستقيماً يمر بالرأس الأوسط موازياً لـ {m('L_1')} و{m('L_2')} لتجتمع الزاويتان المتبادلتان داخلياً في {m('x')}!",
            f"Split {m('x')} with an auxiliary parallel line into {m(f'{a1}^\\circ + {a2}^\\circ')}!",
            [
                f"Draw line {m('L_m \\parallel L_1 \\parallel L_2')} through the middle vertex.",
                f"Alternate interior angles transfer {m(f'{a1}^\\circ')} from {m('L_1')} and {m(f'{a2}^\\circ')} from {m('L_2')}.",
                f"Thus {m(f'x = {a1}^\\circ + {a2}^\\circ = {ans}^\\circ')}.",
            ],
            f"Check: {m(f'{a1} + {a2} = {ans}')} degrees!",
            f"نرسم موازياً مساعداً يقسم {m('x')} إلى مجموع الزاويتين!",
            [
                f"بالتبادل الداخلي مع {m('L_1')} و{m('L_2')} تنقسم {m('x')} إلى {m(f'{a1}^\\circ')} و{m(f'{a2}^\\circ')}.",
                f"إذن {m(f'x = {a1} + {a2} = {ans}^\\circ')}.",
            ],
            f"تحقق: {m(f'{a1}^\\circ + {a2}^\\circ = {ans}^\\circ')}!",
            diagram_en=svg_parallel_zigzag(f"{a1}°", "x", f"{a2}°"),
        )

    med_zig = [
        (2, 5, 1, 10, 105),   # (2t+5) + (t+10) = 105 -> 3t+15=105 -> t=30
        (3, 4, 1, 8, 96),     # 4t+12=96 -> t=21
        (2, 9, 3, 6, 110),    # 5t+15=110 -> t=19
        (1, 14, 2, 7, 99),    # 3t+21=99 -> t=26
        (3, 2, 2, 8, 115),    # 5t+10=115 -> t=21? vary: (3, 5, 2, 10, 125) -> 5t+15=125 -> t=22
        (4, 3, 1, 7, 95),     # 5t+10=95 -> t=17
    ]
    med_zig = [
        (2, 5, 1, 10, 105),
        (3, 4, 1, 8, 96),
        (2, 9, 3, 6, 110),
        (1, 14, 2, 7, 99),
        (3, 5, 2, 10, 125),
        (4, 3, 1, 7, 95),
    ]
    for k1, c1, k2, c2, mid_ang in med_zig:
        ans = (mid_ang - c1 - c2) // (k1 + k2)
        assert (k1 * ans + c1) + (k2 * ans + c2) == mid_ang
        t1_s = f"t+{c1}" if k1 == 1 else f"{k1}t+{c1}"
        t2_s = f"t+{c2}" if k2 == 1 else f"{k2}t+{c2}"
        B.add_math(
            tp, "Medium", bp,
            f"In the diagram with {m('L_1 \\parallel L_2')}, the top acute angle is {m(f'({t1_s})^\\circ')}, the bottom acute angle is {m(f'({t2_s})^\\circ')}, and the middle bend angle is {m(f'{mid_ang}^\\circ')}. Find {m('t')}.",
            f"في الشكل حيث {m('L_1 \\parallel L_2')}، قياس الزاوية العلوية {m(f'({t1_s})^\\circ')} والسفلية {m(f'({t2_s})^\\circ')} والوسطى {m(f'{mid_ang}^\\circ')}. أوجد قيمة {m('t')}.",
            ans, [ans + 3, ans - 3, mid_ang // (k1 + k2), ans + 5],
            f"Set the sum of the two acute angles equal to the middle bend angle {m(f'{mid_ang}^\\circ')}!",
            f"ساوِ مجموع الزاويتين الحادتين بقياس الزاوية الوسطى {m(f'{mid_ang}^\\circ')}!",
            f"Use the zigzag sum identity {m(f'({t1_s}) + ({t2_s}) = {mid_ang}')}!",
            [
                f"By the parallel-zigzag theorem, {m(f'({t1_s}) + ({t2_s}) = {mid_ang}')}.",
                f"Combine like terms: {m(f'{k1 + k2}t + {c1 + c2} = {mid_ang} \\implies {k1 + k2}t = {mid_ang - c1 - c2} \\implies t = {ans}')}.",
            ],
            f"Check: {m(f'{k1*ans + c1}^\\circ + {k2*ans + c2}^\\circ = {mid_ang}^\\circ')}!",
            f"نطبق قانون الخط المنكسر بين متوازيين ونحل المعادلة الخطية!",
            [
                f"مجموع الزاويتين يساوي الوسطى: {m(f'{k1 + k2}t + {c1 + c2} = {mid_ang}')}.",
                f"ومنه {m(f'{k1 + k2}t = {mid_ang - c1 - c2} \\implies t = {ans}')}.",
            ],
            f"تحقق: {m(f'{k1*ans + c1} + {k2*ans + c2} = {mid_ang}')}!",
            diagram_en=svg_parallel_zigzag(f"{t1_s}°", f"{mid_ang}°", f"{t2_s}°"),
        )

    for a_top, b_r, c_l in [(35, 92, 78), (42, 105, 81), (29, 88, 74), (38, 99, 85)]:
        # Alternating 2-bend zigzag: sum of right-pointing angles = sum of left-pointing angles:
        # a_top + c_l = b_r + a_bot -> a_bot = a_top + c_l - b_r? Let's make it crystal clear:
        # Right-pointing bend B1 = b_r, Left-pointing bend B2 = c_l:
        # Draw parallel through B1: lower part of B1 = b_r - a_top; draw parallel through B2: upper part of B2 = b_r - a_top, so lower part of B2 = c_l - (b_r - a_top) = a_top + c_l - b_r = a_bot!
        ans = a_top + c_l - b_r
        assert ans > 10 and b_r == a_top + (c_l - ans)
        B.add_math(
            tp, "Hard", bp,
            f"Between parallel lines {m('L_1 \\parallel L_2')}, a 3-segment zigzag starts on {m('L_1')} at acute angle {m(f'{a_top}^\\circ')} (going down-right), bends at right-pointing vertex {m(f'P = {b_r}^\\circ')}, then bends at left-pointing vertex {m(f'Q = {c_l}^\\circ')}, and meets {m('L_2')} at acute angle {m('x^\\circ')} (going down-right). Find {m('x')}.",
            f"بين المتوازيين {m('L_1 \\parallel L_2')} يبدأ خط منكسر من 3 قطع عند {m('L_1')} بزاوية حادة {m(f'{a_top}^\\circ')} (لأسفل اليمين)، ثم ينعطف عند الرأس الأيمن بزاوية {m(f'P = {b_r}^\\circ')}، ثم عند الرأس الأيسر بزاوية {m(f'Q = {c_l}^\\circ')}، ويلتقي مع {m('L_2')} بزاوية حادة {m('x^\\circ')}. أوجد {m('x')}.",
            ans, [b_r - a_top, c_l - a_top, ans + 12, ans + 6],
            f"Draw **two** horizontal helper lines through {m('P')} and {m('Q')}, or use the alternating-peaks rule: {m(f'{a_top} + {c_l} = {b_r} + x')}!",
            f"ارسم **مستقيمين** مساعدين يمران بـ {m('P')} و{m('Q')}، أو طبّق قاعدة تناوب الرؤوس: {m(f'{a_top} + {c_l} = {b_r} + x')}!",
            f"Pass parallel helper lines through both bends {m('P')} and {m('Q')}!",
            [
                f"Through {m('P')}, the parallel splits {m(f'{b_r}^\\circ')} into {m(f'{a_top}^\\circ')} above and {m(f'{b_r - a_top}^\\circ')} below.",
                f"Through {m('Q')}, alternate interior angles copy {m(f'{b_r - a_top}^\\circ')} above, leaving {m(f'x = {c_l}^\\circ - {b_r - a_top}^\\circ = {ans}^\\circ')} below!",
            ],
            f"Alternating-sum check: {m(f'{a_top} + {c_l} = {a_top + c_l}')} and {m(f'{b_r} + {ans} = {b_r + ans}')}!",
            f"نمرر موازيين مساعدين عند الرأسين {m('P')} و{m('Q')} ونتتبع التبادل الداخلي!",
            [
                f"عند {m('P')} يتبقى تحت الموازي {m(f'{b_r} - {a_top} = {b_r - a_top}^\\circ')}.",
                f"تنتقل بالتبادل إلى أعلى {m('Q')} فيتبقى {m(f'x = {c_l} - {b_r - a_top} = {ans}^\\circ')}.",
            ],
            f"تحقق بقاعدة التناوب: {m(f'{a_top} + {c_l} = {b_r} + {ans}')}!",
            diagram_en=svg_parallel_zigzag(f"{a_top}°", f"{b_r}°/{c_l}°", "x°"),
        )

    # 22. nsmo_g7_folded_strip_isosceles (5E, 6M, 4H) — SVG: svg_paper_fold
    bp = "nsmo_g7_folded_strip_isosceles"
    easy_fold = [52, 58, 63, 67, 71]
    for alp in easy_fold:
        ans = 180 - 2 * alp
        B.add_math(
            tp, "Easy", bp,
            f"The top-right corner of a rectangular sheet is folded inward along a straight crease that makes an angle of {m(f'{alp}^\\circ')} with the top edge, as shown. What is the measure (in degrees) of the uncovered angle {m('x')} along the straight top edge?",
            f"طُوي الركن العلوي الأيمن لورقة مستطيلة إلى الداخل حول خط طيّ مستقيم يصنع زاوية قياسها {m(f'{alp}^\\circ')} مع الحافة العليا كما في الشكل. ما قياس الزاوية المتبقية {m('x')} بالدرجات على امتداد الحافة العليا؟",
            ans, [180 - alp, 90 - alp if alp < 90 else alp, 2 * alp, ans + 10],
            f"Folding copies the {m(f'{alp}^\\circ')} angle onto itself across the crease, so {m(f'x + {alp}^\\circ + {alp}^\\circ = 180^\\circ')}!",
            f"الطيّ ينسخ الزاوية {m(f'{alp}^\\circ')} على نفسها حول خط الطيّ، فيكون {m(f'x + {alp}^\\circ + {alp}^\\circ = 180^\\circ')}!",
            f"Subtract **two** copies of {m(f'{alp}^\\circ')} from the straight {m('180^\\circ')} edge!",
            [
                f"By paper-folding congruence, the angle between the crease and the folded edge also equals {m(f'{alp}^\\circ')}.",
                f"Along the straight top edge, {m(f'x + {alp}^\\circ + {alp}^\\circ = 180^\\circ \\implies x = 180^\\circ - {2*alp}^\\circ = {ans}^\\circ')}.",
            ],
            f"Check: {m(f'{ans} + {alp} + {alp} = 180')} degrees!",
            f"نطرح ضعف زاوية الطيّ من الزاوية المستقيمة {m('180^\\circ')}!",
            [
                f"الزاوية المطوية تطابق الأصلية وتساوي {m(f'{alp}^\\circ')}.",
                f"إذن {m(f'x = 180^\\circ - 2 \\times {alp}^\\circ = {ans}^\\circ')}.",
            ],
            f"تحقق: {m(f'{ans}^\\circ + 2({alp}^\\circ) = 180^\\circ')}!",
            diagram_en=svg_paper_fold(f"{alp}°", "x"),
        )

    med_fold = [34, 42, 48, 56, 64, 72]
    for x_gap in med_fold:
        ans = (180 - x_gap) // 2
        B.add_math(
            tp, "Medium", bp,
            f"When a rectangular paper strip is folded along a straight crease as shown, the uncovered acute angle between the folded edge and the remaining top edge is {m(f'x = {x_gap}^\\circ')}. What is the crease angle {m('\\alpha')} (in degrees)?",
            f"عند طيّ شريط ورقي مستطيل حول خط طيّ مستقيم كما في الشكل، بلغ قياس الزاوية الحادة المتبقية {m(f'x = {x_gap}^\\circ')}. ما قياس زاوية الطيّ {m('\\alpha')} بالدرجات؟",
            ans, [180 - x_gap, 90 - x_gap if x_gap < 90 else x_gap, ans - 8, ans + 8],
            f"Since original and folded angles both equal {m('\\alpha')}, solve {m(f'2\\alpha + {x_gap}^\\circ = 180^\\circ')}!",
            f"بما أن زاوية الطيّ الأصلية والمطوية متساويتان وتساويان {m('\\alpha')}، حل المعادلة {m(f'2\\alpha + {x_gap}^\\circ = 180^\\circ')}!",
            f"Use {m(f'2\\alpha = 180^\\circ - {x_gap}^\\circ')}!",
            [
                f"Along the straight top edge, {m(f'\\alpha + \\alpha + {x_gap}^\\circ = 180^\\circ')}.",
                f"Thus {m(f'2\\alpha = {180 - x_gap}^\\circ \\implies \\alpha = {ans}^\\circ')}.",
            ],
            f"Check: {m(f'2 \\times {ans}^\\circ + {x_gap}^\\circ = 180^\\circ')}!",
            f"نحل المعادلة {m(f'2\\alpha + {x_gap}^\\circ = 180^\\circ')}!",
            [
                f"من استقامة الحافة العليا: {m(f'2\\alpha = 180^\\circ - {x_gap}^\\circ = {180 - x_gap}^\\circ')}.",
                f"بالقسمة على {m(2)} نحصل على {m(f'\\alpha = {ans}^\\circ')}.",
            ],
            f"تحقق: {m(f'{ans} + {ans} + {x_gap} = 180')}!",
            diagram_en=svg_paper_fold("α", f"{x_gap}°"),
        )

    for k_mult, c_add in [(1, 24), (2, -20), (1, 45), (3, -45)]:
        # x = k_mult * alpha + c_add, and x + 2*alpha = 180 -> (k_mult + 2)*alpha = 180 - c_add
        assert (180 - c_add) % (k_mult + 2) == 0
        alp = (180 - c_add) // (k_mult + 2)
        x_val = k_mult * alp + c_add
        expr_s = f"\\alpha + {c_add}^\\circ" if k_mult == 1 else f"{k_mult}\\alpha - {abs(c_add)}^\\circ"
        B.add_math(
            tp, "Hard", bp,
            f"A corner of a rectangular sheet is folded along a crease making angle {m('\\alpha')} with the top edge. If the uncovered angle {m('x')} on that straight edge satisfies {m(f'x = {expr_s}')}, find {m('x')} (in degrees).",
            f"طُوي ركن ورقة مستطيلة حول خط طيّ يصنع زاوية {m('\\alpha')} مع الحافة العليا. إذا كانت الزاوية المتبقية {m('x')} تحقق {m(f'x = {expr_s}')}، فأوجد قياس {m('x')} بالدرجات.",
            x_val, [alp, 180 - alp, x_val + 10, x_val - 10],
            f"Combine {m('x + 2\\alpha = 180^\\circ')} with {m(f'x = {expr_s}')} to find {m('\\alpha')}, then compute {m('x')}!",
            f"اجمع العلاقة الهندسية {m('x + 2\\alpha = 180^\\circ')} مع {m(f'x = {expr_s}')} لإيجاد {m('\\alpha')} ثم احسب {m('x')}!",
            f"Substitute {m(f'x = {expr_s}')} into {m('x + 2\\alpha = 180^\\circ')}!",
            [
                f"Along the straight edge, {m('x + 2\\alpha = 180^\\circ')}.",
                f"Substituting {m(f'x = {expr_s}')} gives {m(f'{k_mult + 2}\\alpha = {180 - c_add}^\\circ \\implies \\alpha = {alp}^\\circ')}.",
                f"Therefore {m(f'x = 180^\\circ - 2({alp}^\\circ) = {x_val}^\\circ')}.",
            ],
            f"Check: {m(f'x = {x_val}^\\circ')} and {m(f'\\alpha = {alp}^\\circ')} satisfy both {m(f'{x_val} + 2({alp}) = 180')} and {m(f'x = {expr_s}')}!",
            f"نعوّض عن {m('x')} في {m('x + 2\\alpha = 180^\\circ')} لإيجاد {m('\\alpha')} ثم {m('x')}!",
            [
                f"بالتعويض نحصل على {m(f'{k_mult + 2}\\alpha = {180 - c_add}^\\circ \\implies \\alpha = {alp}^\\circ')}.",
                f"إذن {m(f'x = 180^\\circ - 2({alp}^\\circ) = {x_val}^\\circ')}.",
            ],
            f"تحقق: {m(f'{x_val} + 2({alp}) = 180')}!",
            diagram_en=svg_paper_fold("α", "x"),
        )

    # 23. nsmo_g7_rectilinear_staircase_perim (5E, 6M, 4H) — SVG: svg_rectilinear_staircase
    bp = "nsmo_g7_rectilinear_staircase_perim"
    easy_stair = [(14, 9, 3), (20, 13, 4), (25, 16, 5), (19, 12, 3), (28, 17, 4)]
    for W, H, st in easy_stair:
        ans = 2 * (W + H)
        B.add_math(
            tp, "Easy", bp,
            f"A rising rectilinear staircase polygon has {m(st)} right-angled steps, total width {m(f'{W}\\text{{ cm}}')}, and total height {m(f'{H}\\text{{ cm}}')}. What is its **perimeter** (in cm)?",
            f"مضلع متدرج صاعد قائم الزوايا يتكون من {m(st)} درجات، عرضه الكلي {m(f'{W}\\text{{ سم}}')} وارتفاعه الكلي {m(f'{H}\\text{{ سم}}')}. ما **محيطه** بالسنتمتر؟",
            ans, [W + H, ans - W, ans + 2 * st, W * H],
            f"Slide all horizontal treads up and all vertical risers sideways to form a {m(f'{W} \\times {H}')} rectangle!",
            f"أزح جميع القطع الأفقية للأعلى والقطع الرأسية للجانب ليتكوّن مستطيل أبعاده {m(f'{W} \\times {H}')}!",
            f"Apply the bounding-box perimeter rule {m('P = 2(W + H)')}!",
            [
                f"All horizontal step treads sum to {m(f'{W}\\text{{ cm}}')} and all vertical step risers sum to {m(f'{H}\\text{{ cm}}')}.",
                f"Perimeter = {m(f'2({W} + {H}) = {ans}\\text{{ cm}}')}.",
            ],
            f"Notice the number of steps ({m(st)}) does not change the perimeter {m(ans)} cm!",
            f"مجموع القطع الأفقية يساوي {m(W)} والعمودية يساوي {m(H)}!",
            [
                f"المحيط يساوي محيط المستطيل المحيط: {m(f'2({W} + {H}) = {ans}\\text{{ سم}}')}.",
            ],
            f"تحقق: {m(f'2 \\times {W + H} = {ans}')} سم!",
            diagram_en=svg_rectilinear_staircase(f"{W} cm", f"{H} cm", st),
        )

    med_stair = [
        (76, 23, 4),   # 2(23+H)=76 -> H=15
        (94, 29, 5),   # H=18
        (110, 34, 3),  # H=21
        (88, 27, 4),   # H=17
        (124, 38, 5),  # H=24
        (102, 31, 3),  # H=20
    ]
    for P, W, st in med_stair:
        ans = P // 2 - W
        B.add_math(
            tp, "Medium", bp,
            f"The rising {m(st)}-step rectilinear staircase shown has perimeter {m(f'{P}\\text{{ cm}}')} and bottom width {m(f'{W}\\text{{ cm}}')}. What is its vertical height {m('H')} (in cm)?",
            f"المضلع المتدرج الصاعد الموضّح ذو الـ {m(st)} درجات محيطه {m(f'{P}\\text{{ سم}}')} وعرض قاعدته {m(f'{W}\\text{{ سم}}')}. ما ارتفاعه الرأسي {m('H')} بالسنتمتر؟",
            ans, [P - 2 * W, ans + st, ans - 3, P // 4],
            f"Since {m(f'2({W} + H) = {P}')}, halve the perimeter first to get {m('W + H')}!",
            f"بما أن {m(f'2({W} + H) = {P}')}، اقسم المحيط على {m(2)} أولاً لإيجاد {m('W + H')}!",
            f"Solve {m(f'2({W} + H) = {P}')} for {m('H')}!",
            [
                f"Half-perimeter is {m(f'W + H = {P} \\div 2 = {P // 2}\\text{{ cm}}')}.",
                f"Subtract {m(f'W = {W}')}: {m(f'H = {P // 2} - {W} = {ans}\\text{{ cm}}')}.",
            ],
            f"Check: {m(f'2({W} + {ans}) = {P}')} cm!",
            f"نقسم المحيط على {m(2)} ثم نطرح العرض {m(W)}!",
            [
                f"نصف المحيط = {m(f'{P} \\div 2 = {P // 2}')} سم.",
                f"الارتفاع {m(f'H = {P // 2} - {W} = {ans}')} سم.",
            ],
            f"تحقق: {m(f'2({W} + {ans}) = {P}')} سم!",
            diagram_en=svg_rectilinear_staircase(f"{W} cm", "H = ?", st),
        )

    for W, H, depth in [(20, 14, 5), (24, 16, 6), (18, 12, 4), (30, 20, 7)]:
        ans = 2 * (W + H) + 2 * depth
        B.add_math(
            tp, "Hard", bp,
            f"A {m(f'{W}\\text{{ cm}} \\times {H}\\text{{ cm}}')} rising staircase card has an additional rectangular **inward U-notch** of depth {m(f'{depth}\\text{{ cm}}')} and width {m('3\\text{ cm}')} cut straight down into one horizontal tread. What is the **perimeter** (in cm) of the notched polygon?",
            f"بطاقة متدرجة صاعدة أبعادها الكلية {m(f'{W}\\text{{ سم}} \\times {H}\\text{{ سم}}')} قُطع في إحدى درجاتها الأفقية **تجويف مستطيل للداخل** عمقه الرأسي {m(f'{depth}\\text{{ سم}}')} وعرضه {m('3\\text{ سم}')}. ما **محيط** المضلع الناتج بالسنتمتر؟",
            ans, [2 * (W + H), ans - depth, ans + 6, 2 * (W + H) + 3],
            f"Pushing the bottom of the {m('3\\text{ cm}')} notch up closes the gap in the horizontal tread, leaving **two extra vertical walls** of length {m(f'{depth}\\text{{ cm}}')} each!",
            f"رفع قاع التجويف للأعلى يغلق الفتحة الأفقية تماماً، ويتبقى **جداران رأسيان إضافيان** طول كل منهما {m(f'{depth}\\text{{ سم}}')}!",
            f"Add {m(f'2 \\times {depth}\\text{{ cm}}')} for the two inward vertical walls to {m(f'2({W} + {H})')}!",
            [
                f"Without the U-notch, the staircase perimeter is {m(f'2({W} + {H}) = {2*(W+H)}\\text{{ cm}}')}.",
                f"The notch replaces a {m('3\\text{ cm}')} top segment with a {m('3\\text{ cm}')} bottom segment (net {m(0)} horizontal change) plus **two** vertical side walls of {m(f'{depth}\\text{{ cm}}')}.",
                f"New perimeter = {m(f'{2*(W+H)} + 2 \\times {depth} = {ans}\\text{{ cm}}')}.",
            ],
            f"Notice the notch width ({m('3\\text{ cm}')}) cancels out completely—only twice the depth ({m(2 * depth)} cm) is added!",
            f"عرض التجويف يختصر مع قاعه، فلا يضاف للمحيط سوى ضعف العمق {m(f'2 \\times {depth}')}!",
            [
                f"محيط الشكل المتدرج الأصلي = {m(2 * (W + H))} سم.",
                f"يضيف التجويف جدارين رأسيين مجموعهما {m(f'2 \\times {depth} = {2 * depth}')} سم، فالمحيط = {m(ans)} سم.",
            ],
            f"تحقق: {m(f'{2*(W+H)} + {2*depth} = {ans}')} سم!",
            diagram_en=svg_rectilinear_staircase(f"{W} cm", f"{H} cm", 3),
        )

    # 24. nsmo_g7_shaded_rect_triangle_cut (5E, 6M, 4H) — SVG: shaded triangle / corner cut
    bp = "nsmo_g7_shaded_rect_triangle_cut"
    easy_half = [(14, 8), (16, 9), (18, 11), (22, 10), (24, 7)]
    for L, W in easy_half:
        ans = (L * W) // 2
        B.add_math(
            tp, "Easy", bp,
            f"In the {m(f'{L}\\text{{ cm}} \\times {W}\\text{{ cm}}')} rectangle shown, the shaded triangle has the entire bottom side as its base and its top vertex on the upper side of the rectangle. What is the **area** of the shaded triangle (in {m('\\text{cm}^2')})?",
            f"في المستطيل الذي أبعاده {m(f'{L}\\text{{ سم}} \\times {W}\\text{{ سم}}')}، قاعدة المثلث المظلل هي الضلع السفلي كاملاً ورأسه العلوي يقع على الضلع العلوي للمستطيل. ما **مساحة** المثلث المظلل بـ {m('\\text{سم}^2')}؟",
            ans, [L * W, ans - L, ans + W, 2 * (L + W)],
            f"Base = {m(L)} cm and perpendicular height = {m(W)} cm regardless of where the apex slides along the top edge!",
            f"طول القاعدة = {m(L)} سم والارتفاع العمودي = {m(W)} سم أينما وقع الرأس على الضلع العلوي!",
            f"Use {m('A = \\frac{1}{2} \\times \\text{base} \\times \\text{height}')} = half the rectangle!",
            [
                f"The triangle's base is {m(f'{L}\\text{{ cm}}')} and its altitude between the parallel top and bottom sides is {m(f'{W}\\text{{ cm}}')}.",
                f"Area = {m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"Shaded triangle is always exactly half of {m(f'{L}\\times {W} = {L*W}')}!",
            f"مساحة المثلث المشترك مع المستطيل في القاعدة والارتفاع تساوي نصف مساحة المستطيل دائماً!",
            [
                f"المساحة = {m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}')} سم².",
            ],
            f"تحقق: نصف {m(L * W)} هو {m(ans)}!",
            diagram_en=svg_shaded_triangle_in_rect(L, W, 0.62, "cm"),
        )

    med_cuts = [
        (12, 8, 4, 2),   # 96 - (16 + 12 + 24) = 44
        (10, 8, 6, 4),   # 80 - (24 + 20 + 8) = 28
        (14, 6, 6, 2),   # 84 - (18 + 14 + 16) = 36
        (12, 10, 6, 4),  # 120 - (30 + 24 + 18) = 48
        (16, 8, 6, 4),   # 128 - (24 + 32 + 20) = 52
        (15, 8, 5, 4),   # 120 - (20 + 30 + 20) = 50
    ]
    for L, W, ct, cr in med_cuts:
        t1 = (W * ct) // 2
        t2 = (L * cr) // 2
        t3 = ((L - ct) * (W - cr)) // 2
        ans = L * W - (t1 + t2 + t3)
        assert 2 * ans == abs(ct * cr - W * L)
        B.add_math(
            tp, "Medium", bp,
            f"A {m(f'{L} \\times {W}')} rectangle contains a shaded triangle whose vertices are the bottom-left corner, a point on the top side {m(ct)} units from the top-left corner, and a point on the right side {m(cr)} units above the bottom-right corner. Find the **area** of the shaded triangle.",
            f"مستطيل أبعاده {m(f'{L} \\times {W}')} بداخله مثلث مظلل رؤوسه عند الركن السفلي الأيسر، ونقطة على الضلع العلوي تبعد {m(ct)} وحدات عن الركن العلوي الأيسر، ونقطة على الضلع الأيمن ترتفع {m(cr)} وحدات فوق الركن السفلي الأيمن. أوجد **مساحة** المثلث المظلل.",
            ans, [L * W // 2, ans - 4, ans + 4, t1 + t2 + t3],
            f"Subtract the three unshaded corner right triangles from the {m(f'{L} \\times {W} = {L * W}')} rectangle!",
            f"اطرح مساحات المثلثات القائمة الثلاثة غير المظللة عند الأركان من مساحة المستطيل {m(L * W)}!",
            f"Compute {m(f'{L}\\times {W} - (T_1 + T_2 + T_3)')}!",
            [
                f"Rectangle area = {m(f'{L} \\times {W} = {L * W}')}.",
                f"The three outer right triangles have areas {m(f'\\frac{{1}}{{2}}({W})({ct}) = {t1}')}, {m(f'\\frac{{1}}{{2}}({L})({cr}) = {t2}')}, and {m(f'\\frac{{1}}{{2}}({L-ct})({W-cr}) = {t3}')}.",
                f"Shaded area = {m(f'{L * W} - ({t1} + {t2} + {t3}) = {ans}')}.",
            ],
            f"Check: {m(f'{ans} + {t1} + {t2} + {t3} = {L * W}')}!",
            f"نطرح مساحات المثلثات القائمة الثلاثة الركنية من مساحة المستطيل الكلية!",
            [
                f"مساحات المثلثات الثلاثة هي {m(t1)} و{m(t2)} و{m(t3)} ومجموعها {m(t1 + t2 + t3)}.",
                f"المساحة المظللة = {m(f'{L * W} - {t1 + t2 + t3} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} + {t1 + t2 + t3} = {L * W}')}!",
            diagram_en=svg_inscribed_corner_triangle_in_rect(L, W, ct, cr),
        )

    for A_rect in (64, 96, 128, 160):
        # Midpoint corner-cut theorem: P = midpoint of top, Q = midpoint of right -> shaded = (3/8)*A_rect!
        ans = (3 * A_rect) // 8
        B.add_math(
            tp, "Hard", bp,
            f"Rectangle {m('ABCD')} has total area {m(A_rect)}. Point {m('P')} is the **midpoint** of the top side and point {m('Q')} is the **midpoint** of the right side. What is the **area** of the shaded triangle connecting the bottom-left corner to {m('P')} and {m('Q')}?",
            f"مستطيل {m('ABCD')} مساحته الكلية {m(A_rect)}. النقطة {m('P')} هي **منتصف** الضلع العلوي والنقطة {m('Q')} هي **منتصف** الضلع الأيمن. ما **مساحة** المثلث المظلل الواصل بين الركن السفلي الأيسر والنقطتين {m('P')} و{m('Q')}؟",
            ans, [A_rect // 2, A_rect // 4, (5 * A_rect) // 8, (3 * A_rect) // 4],
            f"Express each of the three corner right triangles as a fraction of the rectangle: {m('\\frac{1}{4}')}, {m('\\frac{1}{4}')}, and {m('\\frac{1}{8}')}!",
            f"عبّر عن كل مثلث ركني ككسر من مساحة المستطيل: {m('\\frac{1}{4}')} و{m('\\frac{1}{4}')} و{m('\\frac{1}{8}')}!",
            f"Use the midpoint fraction identity {m('1 - \\left(\\frac{1}{4} + \\frac{1}{4} + \\frac{1}{8}\\right) = \\frac{3}{8}')}!",
            [
                f"Top-left right triangle has legs {m('W')} and {m('L/2')}, so area {m('\\frac{1}{4} LW')}; bottom-right right triangle has legs {m('L')} and {m('W/2')}, also {m('\\frac{1}{4} LW')}.",
                f"Top-right right triangle has legs {m('L/2')} and {m('W/2')}, so area {m('\\frac{1}{8} LW')}.",
                f"Shaded fraction is {m('1 - \\frac{5}{8} = \\frac{3}{8}')}, giving {m(f'\\frac{{3}}{{8}} \\times {A_rect} = {ans}')}.",
            ],
            f"Check: {m(f'{A_rect // 4} + {A_rect // 4} + {A_rect // 8} + {ans} = {A_rect}')}!",
            f"نحسب كسور المساحات الركنية فنحصل على {m('\\frac{3}{8}')} من مساحة المستطيل!",
            [
                f"المثلثات الثلاثة تشغل {m('\\frac{1}{4} + \\frac{1}{4} + \\frac{1}{8} = \\frac{5}{8}')} من المستطيل.",
                f"يتبقى للمثلث المظلل {m(f'\\frac{{3}}{{8}} \\times {A_rect} = {ans}')}.",
            ],
            f"تحقق: {m(f'\\frac{{5}}{{8}}({A_rect}) + {ans} = {A_rect}')}!",
            diagram_en=svg_inscribed_corner_triangle_in_rect(8, 6, 4, 3),
        )

    # 25. nsmo_g7_painted_stacked_cubes (5E, 6M, 4H) — SVG: svg_painted_cube_3d / svg_cube_stack_3d
    bp = "nsmo_g7_painted_stacked_cubes"
    easy_cubes = [
        (3, 1, 6),     # 3x3x3, 1 painted face -> 6
        (5, 2, 36),    # 5x5x5, 2 painted faces -> 36
        (4, 1, 24),    # 4x4x4, 1 painted face -> 24
        (5, 0, 27),    # 5x5x5, 0 painted faces -> 27
        (6, 2, 48),    # 6x6x6, 2 painted faces -> 48
    ]
    for n_c, faces_k, expected in easy_cubes:
        if faces_k == 2:
            ans = 12 * (n_c - 2)
        elif faces_k == 1:
            ans = 6 * (n_c - 2) ** 2
        else:
            ans = (n_c - 2) ** 3
        assert ans == expected
        B.add_math(
            tp, "Easy", bp,
            f"A solid {m(f'{n_c} \\times {n_c} \\times {n_c}')} cube is painted red on all {m(6)} outer faces and cut into {m(n_c ** 3)} unit cubes. How many unit cubes have **exactly {m(faces_k)}** red face(s)?",
            f"طُلي مكعب مصمت أبعاده {m(f'{n_c} \\times {n_c} \\times {n_c}')} باللون الأحمر من جميع أوجهه الستة ثم قُطّع إلى {m(n_c ** 3)} مكعب وحدة. كم مكعب وحدة له **{m(faces_k)} وجه/أوجه حمراء بالضبط**؟",
            ans, [ans + 12, ans - 6 if ans > 6 else ans + 6, 6 * n_c * n_c if faces_k == 1 else n_c ** 3 - ans, 8],
            f"Use {m('12(n-2)')} for 2 faces (edges), {m('6(n-2)^2')} for 1 face (face interiors), and {m('(n-2)^3')} for 0 faces (inner core)!",
            f"استخدم {m('12(n-2)')} لوجهين، و{m('6(n-2)^2')} لوجه واحد، و{m('(n-2)^3')} لصفر أوجه!",
            f"Peel the border layer so {m(f'n - 2 = {n_c - 2}')}!",
            [
                f"Here {m(f'n = {n_c}')}, so the interior edge length after removing corners/borders is {m(f'n - 2 = {n_c - 2}')}.",
                f"Applying the {m(faces_k)}-face formula gives {m(ans)} unit cubes.",
            ],
            f"Census check: {m(f'8 + {12*(n_c-2)} + {6*(n_c-2)**2} + {(n_c-2)**3} = {n_c**3}')}!",
            f"نحسب {m(f'n - 2 = {n_c - 2}')} ونطبّق القانون المناسب لعدد الأوجه {m(faces_k)}!",
            [
                f"طول الحرف الداخلي {m(f'n - 2 = {n_c - 2}')}.",
                f"بالتعويض نحصل على {m(ans)} مكعباً صغيراً.",
            ],
            f"تحقق: مجموع جميع الفئات الأربع يساوي {m(n_c ** 3)}!",
            diagram_en=svg_painted_cube_3d(min(n_c, 5)),
        )

    med_stacks = [(3, 2, 1), (4, 2, 1), (4, 3, 2), (5, 3, 1), (5, 4, 2), (6, 4, 1)]
    for cols in med_stacks:
        voxels = {(i, 0, z) for i, h in enumerate(cols) for z in range(h)}
        exposed = 0
        for x, y, z in voxels:
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                if z + dz >= 0 and (x + dx, y + dy, z + dz) not in voxels:
                    exposed += 1
        # Check formula: 3 (top) + 2*sum(cols) (front/back) + 2*cols[0] (left/right since decreasing)
        assert exposed == 3 + 2 * sum(cols) + 2 * cols[0]
        ans = exposed
        B.add_math(
            tp, "Medium", bp,
            f"Unit cubes ({m('1\\text{ cm} \\times 1\\text{ cm} \\times 1\\text{ cm}')}) are stacked into a single row of {m(3)} adjacent columns of heights {m(f'{cols[0]}, {cols[1]},')} and {m(cols[2])} resting flat on a table, as shown. Every exposed outer unit square (**excluding** the bottom squares touching the table) is painted gold. How many unit squares are painted?",
            f"رُصّت مكعبات وحدة ({m('1\\text{ سم}^3')}) في صف واحد من {m(3)} أعمدة متلاصقة ارتفاعاتها {m(f'{cols[0]}، {cols[1]}، {cols[2]}')} موضوعة على طاولة مسطحة كما في الشكل. طُليت جميع المربعات الخارجية المكشوفة (**باستثناء** القاعدة الملامسة للطاولة). كم مربع وحدة طُلي؟",
            ans, [ans + 3, 6 * sum(cols), 2 * sum(cols) + 3, ans - cols[0]],
            f"Count exposed squares from **5 views**: Top ({m(3)}), Front + Back ({m(f'2 \\times {sum(cols)}')}), and Left + Right ({m(f'2 \\times {cols[0]}')})!",
            f"احسب الأوجه المكشوفة من **5 اتجاهات**: الأعلى ({m(3)})، الأمام + الخلف ({m(f'2 \\times {sum(cols)}')})، واليسار + اليمين ({m(f'2 \\times {cols[0]}')})!",
            f"Project the solid onto Top, Front, Back, Left, and Right views!",
            [
                f"From the **Top**, we see {m(3)} unit squares (one atop each column).",
                f"From **Front** and **Back**, each view shows {m(f'{cols[0]} + {cols[1]} + {cols[2]} = {sum(cols)}')} squares, giving {m(2 * sum(cols))} squares.",
                f"From **Left** we see {m(cols[0])} squares, and from **Right** the step-faces also total {m(cols[0])} squares ({m(2 * cols[0])} together). Total = {m(f'3 + {2*sum(cols)} + {2*cols[0]} = {ans}')}.",
            ],
            f"3D voxel neighbor count confirms {m(ans)} exposed unit squares!",
            f"نحسب المساقط الخمسة (أعلى + أمام + خلف + يمين + يسار)!",
            [
                f"من الأعلى {m(3)} مربعات، ومن الأمام والخلف {m(f'2 \\times {sum(cols)} = {2*sum(cols)}')} مربعاً.",
                f"من اليسار واليمين {m(f'2 \\times {cols[0]} = {2*cols[0]}')} مربعاً، فالمجموع = {m(ans)}.",
            ],
            f"تحقق ثلاثي الأبعاد: عدد الأوجه المكشوفة يساوي {m(ans)} تماماً!",
            diagram_en=svg_cube_stack_3d(cols),
        )

    for n_open in (3, 4, 5, 6):
        # n x n x n cube resting on a table: ONLY 5 outer faces painted (bottom unpainted)!
        # How many unit cubes have ZERO painted faces?
        # Inner (n-2) x (n-2) columns of height (n-1) (including the unpainted bottom layer inside the border!): (n-2)^2 * (n-1)!
        voxels_0 = sum(
            1 for x in range(n_open) for y in range(n_open) for z in range(n_open)
            if not (x == 0 or x == n_open - 1 or y == 0 or y == n_open - 1 or z == n_open - 1)
        )
        ans = (n_open - 2) ** 2 * (n_open - 1)
        assert ans == voxels_0
        B.add_math(
            tp, "Hard", bp,
            f"An {m(f'{n_open} \\times {n_open} \\times {n_open}')} cube of {m(n_open ** 3)} unit cubes sits flat on a wooden table while spray paint coats all **5 exposed outer faces** (the bottom face resting on the table receives **no** paint). How many unit cubes end up with **zero** painted faces?",
            f"وُضع مكعب أبعاده {m(f'{n_open} \\times {n_open} \\times {n_open}')} مكوّن من {m(n_open ** 3)} مكعب وحدة على طاولة، وطُليت جميع **أوجهه الخمسة المكشوفة** فقط (القاعدة السفلية الملامسة للطاولة **لم** تُطلَ). كم مكعب وحدة يبقى **بلا أي وجه مطلي**؟",
            ans, [(n_open - 2) ** 3, (n_open - 1) ** 3, ans + (n_open - 2) ** 2, n_open ** 2],
            f"Peel off the {m(4)} painted side walls (width {m('n-2')} by {m('n-2')}) and the {m(1)} painted top layer (leaving height {m('n-1')})!",
            f"أزل الجدران الجانبية الأربعة المطلية (فيتبقى {m('(n-2)\\times(n-2)')}) والطبقة العلوية المطلية فقط (فيتبقى ارتفاع {m('n-1')})!",
            f"Remove {m(2)} layers along length and width, but only {m(1)} layer (the top) vertically!",
            [
                f"Peeling the {m(4)} vertical painted walls leaves a {m(f'({n_open}-2) \\times ({n_open}-2) = {n_open-2} \\times {n_open-2}')} base footprint.",
                f"Only the **top** layer is painted, while the bottom layer on the table is unpainted, leaving height {m(f'{n_open} - 1 = {n_open - 1}')}.",
                f"Unpainted unit cubes = {m(f'{n_open - 2} \\times {n_open - 2} \\times {n_open - 1} = {ans}')}.",
            ],
            f"Trap avoided: {m(f'({n_open}-2)^3 = {(n_open-2)**3}')} forgets the {m((n_open-2)**2)} unpainted bottom-center cubes!",
            f"نزيل طبقتين من الطول والعرض وطبقة واحدة فقط من الارتفاع (الأعلى)!",
            [
                f"المسقط الداخلي غير المطلي أبعاده {m(f'({n_open}-2)\\times({n_open}-2)')}، والارتفاع غير المطلي {m(f'{n_open}-1')}.",
                f"العدد = {m(f'({n_open - 2})^2 \\times ({n_open - 1}) = {ans}')} مكعباً.",
            ],
            f"تحقق شبكي ثلاثي الأبعاد: العدد الدقيق هو {m(ans)}!",
            diagram_en=svg_painted_cube_3d(min(n_open, 5)),
        )


# =============================================================================
# UNIT 1.6 — Counting, Grids, Pigeonhole, Magic Squares & Probability (75 Qs)
# =============================================================================
def _add_unit_1_6(B: BankBuilder) -> None:
    tp = "Combinatorics & Logic"

    # 26. nsmo_g7_multiplication_code_slots (5E, 6M, 4H) — SVG: svg_digit_slots
    bp = "nsmo_g7_multiplication_code_slots"
    easy_slots = [
        ([1, 2, 3, 4, 5, 6], 3, False, "3-digit codes without repeated digits"),
        ([1, 2, 3, 4, 5], 3, True, "3-digit codes if digits may repeat"),
        ([2, 3, 5, 7, 9], 3, False, "3-digit codes without repeated digits"),
        ([1, 3, 5, 7], 4, False, "4-digit codes using each digit once"),
        ([1, 2, 3, 4], 4, True, "4-digit codes if digits may repeat"),
    ]
    for pool, k_len, rep, desc_en in easy_slots:
        n_p = len(pool)
        if rep:
            ans = n_p ** k_len
            slot_lbls = [f"{n_p}w"] * k_len
            prod_s = " \\times ".join([str(n_p)] * k_len)
        else:
            ans = math.perm(n_p, k_len)
            slot_lbls = [f"{n_p - i}w" for i in range(k_len)]
            prod_s = " \\times ".join(str(n_p - i) for i in range(k_len))
        pool_s = ", ".join(str(d) for d in pool)
        rep_ar = "مع السماح بتكرار الرقم" if rep else "دون تكرار أي رقم"
        B.add_math(
            tp, "Easy", bp,
            f"Using only digits from the set {m(f'\\{{{pool_s}\\}}')}, how many {desc_en} can be formed?",
            f"باستخدام الأرقام من المجموعة {m(f'\\{{{pool_s}\\}}')} فقط، كم رمزاً مكوّناً من {m(k_len)} خانات يمكن تكوينه {rep_ar}؟",
            ans, [n_p * k_len, ans // 2, ans + n_p, n_p ** k_len if not rep else math.perm(n_p, k_len)],
            f"Multiply the number of available digit choices for each of the {m(k_len)} positions!",
            f"اضرب عدد الخيارات المتاحة لكل خانة من الخانات الـ {m(k_len)}!",
            f"Apply the multiplication principle across all {m(k_len)} slots!",
            [
                f"From {m(n_p)} available digits, the slot choices multiply as {m(f'{prod_s} = {ans}')}.",
            ],
            f"Every choice sequence produces a distinct {m(k_len)}-digit code, giving {m(ans)} total!",
            f"نطبق مبدأ الضرب عبر الخانات الـ {m(k_len)}!",
            [
                f"عدد الخيارات عبر الخانات يساوي {m(f'{prod_s} = {ans}')}.",
            ],
            f"تحقق: حاصل الضرب يساوي {m(ans)} رمزاً مختلفاً!",
            diagram_en=svg_digit_slots(slot_lbls, f"Pool size = {n_p}"),
        )

    med_slots = [
        ([1, 2, 3, 4, 5, 6], "even"),     # 3 * 5 * 4 = 60
        ([1, 2, 3, 4, 6, 8], "odd"),      # 2 * 5 * 4 = 40
        ([0, 1, 2, 3, 4], "odd"),         # units in {1,3}(2), hund in rem\{0}(3), tens(3) = 18
        ([0, 1, 2, 3, 5, 7], "odd"),      # units in {1,3,5,7}(4), hund in rem\{0}(4), tens(4) = 64
        ([1, 2, 4, 5, 6, 8, 9], "even"),  # units in {2,4,6,8}(4), hund(6), tens(5) = 120
        ([0, 2, 3, 5, 7], "odd"),         # units in {3,5,7}(3), hund in rem\{0}(3), tens(3) = 27
    ]
    for pool, par in med_slots:
        valid_3 = [
            100 * a + 10 * b + c
            for a in pool if a != 0
            for b in pool if b != a
            for c in pool if c not in (a, b) and (c % 2 == (0 if par == "even" else 1))
        ]
        ans = len(valid_3)
        u_cnt = sum(1 for c in pool if c % 2 == (0 if par == "even" else 1))
        h_cnt = len(pool) - 2 if 0 in pool else len(pool) - 1
        t_cnt = len(pool) - 2
        assert ans == u_cnt * h_cnt * t_cnt
        pool_s = ", ".join(str(d) for d in pool)
        par_ar = "زوجياً" if par == "even" else "فردياً"
        B.add_math(
            tp, "Medium", bp,
            f"How many 3-digit **{par}** integers can be formed with **distinct** digits chosen from {m(f'\\{{{pool_s}\\}}')}?",
            f"كم عدداً ثلاثياً **{par_ar}** يمكن تكوينه بأرقام **مختلفة** من المجموعة {m(f'\\{{{pool_s}\\}}')}؟",
            ans, [u_cnt * (len(pool) - 1) * (len(pool) - 2) if 0 in pool else ans + 12, ans // 2, ans + u_cnt, len(pool) * (len(pool) - 1) * u_cnt],
            f"Fill the **units digit** first ({par}), then the **hundreds digit** (cannot be {m(0)}!), and finally the tens digit!",
            f"ابدأ بـ **خانة الآحاد** أولاً، ثم **المئات** (لا تساوي {m(0)}!)، وأخيراً العشرات!",
            f"Lock in the restricted units digit first, then protect the hundreds place from {m(0)}!",
            [
                f"Units place has {m(u_cnt)} valid {par} choice(s).",
                f"Hundreds place cannot use the chosen units digit (nor {m(0)} if present), leaving {m(h_cnt)} choices.",
                f"Tens place can use any of the remaining {m(t_cnt)} digits: {m(f'{u_cnt} \\times {h_cnt} \\times {t_cnt} = {ans}')}.",
            ],
            f"Exhaustive list check confirms {m(ans)} valid 3-digit {par} numbers!",
            f"نملأ الآحاد أولاً ثم المئات (مع استبعاد الصفر) ثم العشرات!",
            [
                f"للآحاد {m(u_cnt)} خيارات، وللمئات {m(h_cnt)} خيارات، وللعشرات {m(t_cnt)} خيارات.",
                f"إجمالي الأعداد = {m(f'{u_cnt} \\times {h_cnt} \\times {t_cnt} = {ans}')}.",
            ],
            f"تحقق شامل: يوجد بالضبط {m(ans)} عدداً يحقق الشروط!",
            diagram_en=svg_digit_slots([f"{h_cnt}w", f"{t_cnt}w", f"{u_cnt}w"], f"3-digit {par}"),
        )

    hard_zero_even = [
        [0, 1, 2, 3, 4],         # 4-digit even distinct: u=0 -> 4*3*2=24; u in {2,4}(2) -> 3*3*2=36 -> 60
        [0, 1, 2, 3, 4, 5],      # u=0 -> 5*4*3=60; u in {2,4}(2) -> 4*4*3=96 -> 156
        [0, 2, 3, 4, 6],         # u=0 -> 4*3*2=24; u in {2,4,6}(3) -> 3*3*2=54 -> 78
        [0, 1, 2, 4, 5, 6],      # u=0 -> 5*4*3=60; u in {2,4,6}(3) -> 4*4*3=144 -> 204
    ]
    for pool in hard_zero_even:
        valid_4 = [
            1000 * a + 100 * b + 10 * c + d
            for a in pool if a != 0
            for b in pool if b != a
            for c in pool if c not in (a, b)
            for d in pool if d not in (a, b, c) and d % 2 == 0
        ]
        ans = len(valid_4)
        n_p = len(pool)
        nz_ev = sum(1 for d in pool if d != 0 and d % 2 == 0)
        c1 = (n_p - 1) * (n_p - 2) * (n_p - 3)
        c2 = nz_ev * (n_p - 2) * (n_p - 2) * (n_p - 3)
        assert ans == c1 + c2
        pool_s = ", ".join(str(d) for d in pool)
        B.add_math(
            tp, "Hard", bp,
            f"Using digits from {m(f'\\{{{pool_s}\\}}')} **without repetition**, how many **4-digit even** integers can be formed?",
            f"باستخدام الأرقام من {m(f'\\{{{pool_s}\\}}')} **دون تكرار**، كم عدداً **رباعياً زوجياً** يمكن تكوينه؟",
            ans, [(nz_ev + 1) * (n_p - 2) * (n_p - 2) * (n_p - 3), c1, c2, ans + 12],
            f"Split into **two separate cases** because {m(0)} is both even and forbidden in the thousands place: Case 1 (units digit = {m(0)}) + Case 2 (units digit {m('\\ne 0')} even)!",
            f"قسّم الحل إلى **حالتين منفصلتين** لأن {m(0)} زوجي وممنوع في خانة الألوف: الحالة ١ (الآحاد = {m(0)}) + الحالة ٢ (الآحاد زوجي غير صفري)!",
            f"Split on whether the units digit is {m(0)} or a non-zero even digit!",
            [
                f"**Case 1 (units = {m(0)})**: thousands has {m(n_p - 1)} non-zero choices, hundreds {m(n_p - 2)}, tens {m(n_p - 3)} {m(f'\\implies {c1}')} numbers.",
                f"**Case 2 (units is one of the {m(nz_ev)} non-zero even digits)**: thousands has {m(n_p - 2)} choices (not {m(0)}, not units), hundreds {m(n_p - 2)}, tens {m(n_p - 3)} {m(f'\\implies {c2}')} numbers.",
                f"Add the two disjoint cases: {m(f'{c1} + {c2} = {ans}')}.",
            ],
            f"Trap avoided: lumping {m(0)} with non-zero evens miscounts the thousands slot; {m(f'{c1} + {c2} = {ans}')} is exact!",
            f"نفصل حالة الآحاد = {m(0)} عن حالة الآحاد الزوجي غير الصفري!",
            [
                f"الحالة ١ (الآحاد = {m(0)}): تعطي {m(c1)} عدداً.",
                f"الحالة ٢ (الآحاد زوجي غير صفري، {m(nz_ev)} خيارات): تعطي {m(c2)} عدداً.",
                f"المجموع = {m(f'{c1} + {c2} = {ans}')} عدداً.",
            ],
            f"تحقق شامل: العدد الدقيق للأعداد الرباعية الزوجية هو {m(ans)}!",
            diagram_en=svg_digit_slots(["Th≠0", "H", "T", "Even"], "Split u=0 vs u≠0"),
        )

    # 27. nsmo_g7_shortest_grid_walks (5E, 6M, 4H) — SVG: svg_street_grid
    bp = "nsmo_g7_shortest_grid_walks"
    easy_grid = [(2, 2), (3, 2), (4, 2), (3, 3), (5, 2)]
    for c_g, r_g in easy_grid:
        ans = math.comb(c_g + r_g, c_g)
        B.add_math(
            tp, "Easy", bp,
            f"On the {m(f'{c_g} \\times {r_g}')} rectangular street grid shown, how many shortest paths go from corner {m('A')} (bottom-left) to corner {m('B')} (top-right) moving only **East** or **North**?",
            f"على شبكة الشوارع المستطيلة {m(f'{c_g} \\times {r_g}')} الموضّحة، كم مساراً أقصر يصل من الركن {m('A')} إلى الركن {m('B')} بالتحرك **شرقاً** أو **شمالاً** فقط؟",
            ans, [c_g * r_g, ans + c_g, ans - 2 if ans > 4 else ans + 4, 2 ** (c_g + r_g - 2)],
            f"Every shortest walk takes {m(c_g)} East steps and {m(r_g)} North steps ({m(c_g + r_g)} steps total): compute {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}}')}!",
            f"كل مسار أقصر يتكون من {m(c_g)} خطوات شرقاً و{m(r_g)} خطوات شمالاً: احسب {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}}')}!",
            f"Choose which {m(r_g)} of the {m(c_g + r_g)} steps go North!",
            [
                f"Any shortest path consists of {m(c_g)} East and {m(r_g)} North moves ({m(c_g + r_g)} moves in all).",
                f"Number of ways = {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}} = {ans}')} shortest paths.",
            ],
            f"Corner-by-corner Pascal addition reaches {m(ans)} at {m('B')}!",
            f"نختار مواضع خطوات الشمال من بين {m(c_g + r_g)} خطوة كلية!",
            [
                f"عدد المسارات يساوي {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}} = {ans}')} مساراً.",
            ],
            f"تحقق بقاعدة جمع التقاطعات: نصل إلى {m('B')} بالعدد {m(ans)}!",
            diagram_en=svg_street_grid(c_g, r_g),
        )

    med_ckpt = [
        (4, 3, 2, 1),   # C(3,1)*C(4,2) = 3*6 = 18
        (4, 4, 2, 2),   # C(4,2)*C(4,2) = 36
        (5, 3, 2, 1),   # C(3,1)*C(5,2) = 3*10 = 30
        (5, 3, 3, 2),   # C(5,2)*C(3,1) = 30? vary: (5, 4, 2, 2) -> C(4,2)*C(5,2) = 6*10 = 60
        (4, 3, 1, 2),   # C(3,2)*C(4,1) = 3*4 = 12
        (5, 4, 3, 1),   # C(4,1)*C(5,3) = 4*10 = 40
    ]
    med_ckpt = [
        (4, 3, 2, 1),
        (4, 4, 2, 2),
        (5, 3, 2, 1),
        (5, 4, 2, 2),
        (4, 3, 1, 2),
        (5, 4, 3, 1),
    ]
    for c_g, r_g, cx, cy in med_ckpt:
        p1 = math.comb(cx + cy, cx)
        p2 = math.comb((c_g - cx) + (r_g - cy), c_g - cx)
        ans = p1 * p2
        B.add_math(
            tp, "Medium", bp,
            f"On a {m(f'{c_g} \\times {r_g}')} street grid from {m('A(0,0)')} to {m(f'B({c_g},{r_g})')}, a student walks only East or North and **must pass through** the library at {m(f'L({cx},{cy})')}. How many shortest paths are possible?",
            f"على شبكة شوارع {m(f'{c_g} \\times {r_g}')} من {m('A(0,0)')} إلى {m(f'B({c_g},{r_g})')}، يسير طالب شرقاً أو شمالاً فقط **ويجب أن يمر** بالمكتبة عند التقاطع {m(f'L({cx},{cy})')}. كم مساراً أقصر ممكناً؟",
            ans, [math.comb(c_g + r_g, c_g), p1 + p2, ans + p1, ans - p2 if ans > p2 else ans + 6],
            f"Multiply the number of paths from {m('A')} to {m('L')} by the number of paths from {m('L')} to {m('B')}!",
            f"اضرب عدد المسارات من {m('A')} إلى {m('L')} في عدد المسارات من {m('L')} إلى {m('B')}!",
            f"Split the walk at checkpoint {m(f'L({cx},{cy})')} and multiply!",
            [
                f"From {m('A(0,0)')} to {m(f'L({cx},{cy})')}: {m(f'\\binom{{{cx + cy}}}{{{cx}}} = {p1}')} paths.",
                f"From {m(f'L({cx},{cy})')} to {m(f'B({c_g},{r_g})')}: {m(f'\\binom{{{(c_g-cx)+(r_g-cy)}}}{{{c_g-cx}}} = {p2}')} paths.",
                f"By multiplication, total paths through {m('L')} = {m(f'{p1} \\times {p2} = {ans}')}.",
            ],
            f"Notice {m(ans)} is strictly less than the unconditioned total {m(math.comb(c_g + r_g, c_g))}!",
            f"نضرب مسارات المرحلة الأولى إلى المكتبة في مسارات المرحلة الثانية إلى {m('B')}!",
            [
                f"من {m('A')} إلى {m('L')}: {m(p1)} مسارات، ومن {m('L')} إلى {m('B')}: {m(p2)} مسارات.",
                f"عدد المسارات الكلية المارة بالمكتبة = {m(f'{p1} \\times {p2} = {ans}')}.",
            ],
            f"تحقق: حاصل الضرب يساوي {m(ans)} مساراً!",
            diagram_en=svg_street_grid(c_g, r_g),
        )

    hard_blk = [
        (4, 3, 2, 1),   # C(7,3) - C(3,1)*C(4,2) = 35 - 18 = 17
        (4, 3, 2, 2),   # 35 - C(4,2)*C(3,1) = 35 - 18 = 17? vary: (4, 3, 1, 1) -> 35 - 2*10 = 15
        (4, 4, 2, 2),   # C(8,4) - C(4,2)*C(4,2) = 70 - 36 = 34
        (5, 3, 2, 2),   # C(8,3) - C(4,2)*C(4,1) = 56 - 24 = 32
    ]
    hard_blk = [(4, 3, 2, 1), (4, 3, 1, 1), (4, 4, 2, 2), (5, 3, 2, 2)]
    for c_g, r_g, bx, by in hard_blk:
        tot_p = math.comb(c_g + r_g, c_g)
        bad_p = math.comb(bx + by, bx) * math.comb((c_g - bx) + (r_g - by), c_g - bx)
        ans = tot_p - bad_p
        # Verify via DP grid!
        dp = [[0] * (r_g + 1) for _ in range(c_g + 1)]
        dp[0][0] = 1
        for x in range(c_g + 1):
            for y in range(r_g + 1):
                if (x, y) == (bx, by) or (x == 0 and y == 0):
                    continue
                dp[x][y] = (dp[x - 1][y] if x > 0 else 0) + (dp[x][y - 1] if y > 0 else 0)
        assert dp[c_g][r_g] == ans
        B.add_math(
            tp, "Hard", bp,
            f"On the {m(f'{c_g} \\times {r_g}')} street grid from {m('A(0,0)')} to {m(f'B({c_g},{r_g})')}, intersection {m(f'({bx},{by})')} is blocked (`×`). Moving only East or North, how many shortest paths avoid the blocked corner?",
            f"على شبكة الشوارع {m(f'{c_g} \\times {r_g}')} من {m('A(0,0)')} إلى {m(f'B({c_g},{r_g})')}، التقاطع {m(f'({bx},{by})')} مغلق (`×`). بالتحرك شرقاً أو شمالاً فقط، كم مساراً أقصر يتجنب التقاطع المغلق؟",
            ans, [tot_p, bad_p, ans + 4, ans - 3],
            f"Subtract the paths that pass **through** {m(f'({bx},{by})')} from all {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}} = {tot_p}')} unblocked paths!",
            f"اطرح عدد المسارات المارة بالتقاطع المغلق {m(f'({bx},{by})')} من إجمالي المسارات الكلية {m(tot_p)}!",
            f"Use complementary counting: Total paths minus paths via {m(f'({bx},{by})')}!",
            [
                f"Total paths ignoring the block: {m(f'\\binom{{{c_g + r_g}}}{{{r_g}}} = {tot_p}')}.",
                f"Paths through {m(f'({bx},{by})')}: {m(f'\\binom{{{bx + by}}}{{{bx}}} \\times \\binom{{{(c_g-bx)+(r_g-by)}}}{{{c_g-bx}}} = {bad_p}')}.",
                f"Valid paths = {m(f'{tot_p} - {bad_p} = {ans}')}.",
            ],
            f"Grid corner-addition with {m(0)} at {m(f'({bx},{by})')} independently confirms {m(ans)}!",
            f"نطرح المسارات المارة بالتقاطع المغلق من العدد الكلي للمسارات!",
            [
                f"إجمالي المسارات بدون عائق = {m(tot_p)}، والمسارات المارة بـ {m(f'({bx},{by})')} = {m(bad_p)}.",
                f"المسارات الصالحة = {m(f'{tot_p} - {bad_p} = {ans}')}.",
            ],
            f"تحقق بالجمع الشبكي: نصل إلى {m('B')} بالعدد {m(ans)} تماماً!",
            diagram_en=svg_street_grid(c_g, r_g, blocked=(bx, by)),
        )

    # 28. nsmo_g7_pigeonhole_worst_case (5E, 6M, 4H)
    bp = "nsmo_g7_pigeonhole_worst_case"
    easy_php = [
        (4, 3, "colors of socks"),
        (5, 4, "flavors of candies"),
        (3, 6, "colors of marbles"),
        (6, 3, "types of stickers"),
        (4, 5, "house badges"),
    ]
    for c_cat, k_same, item_en in easy_php:
        ans = c_cat * (k_same - 1) + 1
        B.add_math(
            tp, "Easy", bp,
            f"A large bin contains plenty of {m(c_cat)} different {item_en}. What is the **minimum** number of items you must draw blindly to **guarantee** at least {m(k_same)} of the **same** kind?",
            f"يحتوي صندوق كبير على وفرة من {m(c_cat)} أصناف مختلفة. ما **أقل** عدد يجب سحبه عشوائياً دون نظر **لضمان** الحصول على {m(k_same)} على الأقل من **الصنف نفسه**؟",
            ans, [c_cat * (k_same - 1), c_cat * k_same, c_cat + k_same, ans + 2],
            f"Worst case takes {m(k_same - 1)} from each of the {m(c_cat)} categories, then add {m('+1')}!",
            f"في أسوأ حالة تسحب {m(k_same - 1)} من كل صنف من الأصناف الـ {m(c_cat)}، ثم تضيف {m('+1')}!",
            f"Apply {m('c(k - 1) + 1')}!",
            [
                f"The longest unlucky draw takes {m(k_same - 1)} from each of the {m(c_cat)} categories: {m(f'{c_cat} \\times {k_same - 1} = {c_cat*(k_same-1)}')}.",
                f"Drawing {m(1)} more item ({m(ans)} total) forces at least one category to hit {m(k_same)}.",
            ],
            f"With {m(ans - 1)} items you could hold {m(k_same - 1)} of each; {m(ans)} guarantees {m(k_same)}!",
            f"نحسب أسوأ حالة {m(f'{c_cat} \\times ({k_same} - 1)')} ثم نضيف {m(1)}!",
            [
                f"أسوأ سحب دون بلوغ الهدف هو {m(f'{c_cat} \\times {k_same - 1} = {ans - 1}')}.",
                f"بإضافة عنصر واحد نحصل على الضمان عند {m(ans)}.",
            ],
            f"تحقق: عند {m(ans)} يستحيل أن تبقى جميع الأصناف عند {m(k_same - 1)} فأقل!",
        )

    med_php = [
        ([2, 8, 9, 10], 5),    # 2 + 4 + 4 + 4 + 1 = 15
        ([3, 4, 11, 12], 6),   # 3 + 4 + 5 + 5 + 1 = 18
        ([1, 3, 9, 10], 5),    # 1 + 3 + 4 + 4 + 1 = 13
        ([2, 5, 8, 9, 11], 6), # 2 + 5 + 5 + 5 + 5 + 1 = 23
        ([3, 7, 8, 9], 6),     # 3 + 5 + 5 + 5 + 1 = 19
        ([1, 2, 7, 8, 9], 4),  # 1 + 2 + 3 + 3 + 3 + 1 = 13? vary: ([2, 2, 8, 9, 10], 5) -> 2+2+4+4+4+1 = 17!
    ]
    med_php = [
        ([2, 8, 9, 10], 5),
        ([3, 4, 11, 12], 6),
        ([1, 3, 9, 10], 5),
        ([2, 5, 8, 9, 11], 6),
        ([3, 7, 8, 9], 6),
        ([2, 2, 8, 9, 10], 5),
    ]
    for cnts, k_req in med_php:
        worst = sum(min(c, k_req - 1) for c in cnts)
        ans = worst + 1
        cnt_s = ", ".join(str(c) for c in cnts)
        B.add_math(
            tp, "Medium", bp,
            f"A pouch holds tokens in {m(len(cnts))} colors with counts {m(f'({cnt_s})')}. What is the **minimum** number of tokens you must draw without looking to **guarantee** at least {m(k_req)} tokens of the **same** color?",
            f"يحتوي كيس على أقراص من {m(len(cnts))} ألوان بأعداد {m(f'({cnt_s})')}. ما **أقل** عدد من الأقراص يجب سحبه دون نظر **لضمان** الحصول على {m(k_req)} أقراص على الأقل من **اللون نفسه**؟",
            ans, [len(cnts) * (k_req - 1) + 1, worst, ans + 2, sum(cnts) - k_req],
            f"Watch out for colors that have **fewer** than {m(k_req - 1)} tokens—in the worst case you exhaust **all** of those scarce colors!",
            f"انتبه للألوان التي يقل عددها عن {m(k_req - 1)}؛ ففي أسوأ حالة تُستنفد هذه الألوان القليلة بالكامل!",
            f"Cap each color's worst-case contribution at {m(f'\\min(\\text{{count}}, {k_req - 1})')} and add {m(1)}!",
            [
                f"To avoid {m(k_req)} of a kind for as long as possible, take {m(f'\\min(c_i, {k_req - 1})')} from each color: {m(' + '.join(str(min(c, k_req - 1)) for c in cnts) + f' = {worst}')}.",
                f"One additional token ({m(f'{worst} + 1 = {ans}')}) must belong to a color that still has tokens left, pushing it to {m(k_req)}!",
            ],
            f"Trap avoided: blind {m(f'{len(cnts)}({k_req}-1)+1 = {len(cnts)*(k_req-1)+1}')} overcounts scarce colors; {m(ans)} is exact!",
            f"نأخذ من كل لون {m(f'\\min(c_i, {k_req - 1})')} في أسوأ حالة ثم نضيف {m(1)}!",
            [
                f"أسوأ سحب دون تحقيق الشرط يجمع {m(' + '.join(str(min(c, k_req - 1)) for c in cnts) + f' = {worst}')} قرصاً.",
                f"السحبة التالية ({m(ans)}) تضمن الوصول إلى {m(k_req)} من لون واحد!",
            ],
            f"تحقق: عند {m(ans)} يتحقق الضمان مع مراعاة الألوان القليلة!",
        )

    for N_max in (20, 30, 40, 50):
        # Subset of {1, 2, ..., N_max}: minimum integers to pick to GUARANTEE two chosen integers sum to N_max + 1!
        # Pair into N_max/2 boxes {1, N_max}, {2, N_max-1}, ..., {N_max/2, N_max/2 + 1} -> N_max//2 + 1!
        boxes = N_max // 2
        ans = boxes + 1
        B.add_math(
            tp, "Hard", bp,
            f"From the set of integers {m(f'\\{{1, 2, 3, \\dots, {N_max}\\}}')}, what is the **minimum** number of distinct integers you must select to **guarantee** that at least two selected integers add up to {m(N_max + 1)}?",
            f"من مجموعة الأعداد الصحيحة {m(f'\\{{1, 2, 3, \\dots, {N_max}\\}}')}، ما **أقل** عدد من الأعداد المختلفة يجب اختياره **لضمان** وجود عددين من بينها مجموعهما {m(N_max + 1)}؟",
            ans, [boxes, N_max - 1, ans + 2, boxes - 1],
            f"Pair the integers into {m(boxes)} pigeonhole pairs that sum to {m(N_max + 1)}: {m(f'\\{{1,{N_max}\\}}, \\{{2,{N_max-1}\\}}, \\dots, \\{{{boxes},{boxes+1}\\}}')}!",
            f"قسّم الأعداد إلى {m(boxes)} زوجاً مجموع كل زوج منها {m(N_max + 1)}: {m(f'\\{{1,{N_max}\\}}, \\{{2,{N_max-1}\\}}, \\dots')}!",
            f"Create {m(boxes)} complementary sum-boxes and apply Pigeonhole!",
            [
                f"Partition {m(f'\\{{1, \\dots, {N_max}\\}}')} into {m(boxes)} pairs summing to {m(N_max + 1)}: {m(f'\\{{1,{N_max}\\}}, \\{{2,{N_max-1}\\}}, \\dots, \\{{{boxes},{boxes+1}\\}}')}.",
                f"Worst case picks {m(1)} number from each of the {m(boxes)} pairs (for example, {m(f'1, 2, \\dots, {boxes}')}) with no pair summing to {m(N_max + 1)}.",
                f"By Pigeonhole, the {m(f'({boxes} + 1)')}-th number ({m(ans)}) must complete one of those pairs!",
            ],
            f"With {m(boxes)} numbers {m(f'\\{{1, \\dots, {boxes}\\}}')}, max sum is {m(f'{boxes - 1} + {boxes} = {2*boxes - 1} < {N_max + 1}')}; {m(ans)} forces a pair!",
            f"نكوّن {m(boxes)} صندوقاً زوجياً مجموع كل صندوق {m(N_max + 1)} ونطبق مبدأ برج الحمام!",
            [
                f"عدد الأزواج المتكاملة هو {m(boxes)} زوجاً.",
                f"في أسوأ حالة نختار عدداً واحداً من كل زوج ({m(boxes)} أعداد)، والعدد التالي ({m(ans)}) يحسم وجود زوج كامل!",
            ],
            f"تحقق: {m(f'{boxes} + 1 = {ans}')} هو الحد الأدنى للضمان!",
        )

    # 29. nsmo_g7_magic_square_center (5E, 6M, 4H) — SVG: svg_magic_square_3x3 (NO forbidden word!)
    bp = "nsmo_g7_magic_square_center"
    easy_magic = [24, 33, 42, 51, 60]
    for S in easy_magic:
        ans = S // 3
        B.add_math(
            tp, "Easy", bp,
            f"In a {m('3 \\times 3')} additive magic square, every row, every column, and both main diagonals have the same magic sum {m(S)}. What number must sit in the **center cell**?",
            f"في مربع سحري جمعي بأبعاد {m('3 \\times 3')}، مجموع كل صف وكل عمود وكلا القطرين يساوي المجموع السحري {m(S)}. ما العدد الذي يجب أن يقع في **خانة المركز**؟",
            ans, [S // 9 if S % 9 == 0 else ans - 3, ans + 3, S // 2, ans - 2],
            f"In any {m('3 \\times 3')} additive magic square, the magic sum equals **3 times the center cell** ({m('S = 3c')})!",
            f"في أي مربع سحري جمعي {m('3 \\times 3')} يساوي المجموع السحري **3 أمثال خانة المركز** ({m('S = 3c')})!",
            f"Divide the magic sum {m(S)} by {m(3)}!",
            [
                f"Adding the middle row, middle column, and both diagonals gives {m('4S = \\text{sum of all 9 cells} + 3c = 3S + 3c')}, so {m('S = 3c')}.",
                f"Thus the center cell is {m(f'c = {S} \\div 3 = {ans}')}.",
            ],
            f"Check: {m(f'3 \\times {ans} = {S}')}!",
            f"نقسم المجموع السحري {m(S)} على {m(3)} طبقاً لقاعدة المركز {m('S = 3c')}!",
            [
                f"من خاصية المربع السحري الثلاثي {m(f'3c = {S}')}.",
                f"إذن قيمة خانة المركز {m(f'c = {S} \\div 3 = {ans}')}.",
            ],
            f"تحقق: {m(f'3 \\times {ans} = {S}')}!",
            diagram_en=svg_magic_square_3x3([["·", "·", "·"], ["·", "?", "·"], ["·", "·", "·"]]),
        )

    # Medium (6): Linearly transformed Lo Shu grids [[8,1,6],[3,5,7],[4,9,2]] -> k*cell + b!
    loshu = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    med_ms = [
        (2, 0, (0, 2)),   # [[16,2,12],[6,10,14],[8,18,4]], hide (0,2)=12, show (0,0)=16, (1,1)=10, (2,1)=18
        (1, 4, (2, 0)),   # [[12,5,10],[7,9,11],[8,13,6]], hide (2,0)=8
        (3, -1, (0, 1)),  # [[23,2,17],[8,14,20],[11,26,5]], hide (0,1)=2
        (2, 3, (1, 2)),   # [[19,5,15],[9,13,17],[11,21,7]], hide (1,2)=17
        (1, 10, (2, 2)),  # [[18,11,16],[13,15,17],[14,19,12]], hide (2,2)=12
        (2, 1, (1, 0)),   # [[17,3,13],[7,11,15],[9,19,5]], hide (1,0)=7
    ]
    for scale_k, shift_b, (hr, hc) in med_ms:
        g_num = [[scale_k * loshu[r][c] + shift_b for c in range(3)] for r in range(3)]
        c_val = g_num[1][1]
        S_mag = 3 * c_val
        ans = g_num[hr][hc]
        # Build display grid showing center + enough clues to determine uniquely while hiding (hr, hc) as "x"
        disp = [["·", "·", "·"] for _ in range(3)]
        disp[1][1] = str(c_val)
        disp[hr][hc] = "x"
        # Reveal the OTHER two entries in row hr (or diagonal if hr==1)!
        if hr != 1:
            for c in range(3):
                if c != hc:
                    disp[hr][c] = str(g_num[hr][c])
            known_pair = [g_num[hr][c] for c in range(3) if c != hc]
        else:
            # hr == 1: reveal (1, 2-hc) -> then row 1 has (x, c_val, other) or (other, c_val, x)!
            other_c = 2 - hc
            disp[1][other_c] = str(g_num[1][other_c])
            disp[0][0] = str(g_num[0][0])
            known_pair = [c_val, g_num[1][other_c]]
        assert sum(known_pair) + ans == S_mag
        B.add_math(
            tp, "Medium", bp,
            f"In the partially filled {m('3 \\times 3')} additive magic square shown (center = {m(c_val)}, and the two other entries in the row of {m('x')} are {m(known_pair[0])} and {m(known_pair[1])}), find the value of {m('x')}.",
            f"في المربع السحري الجمعي {m('3 \\times 3')} الموضّح جزئياً (خانة المركز = {m(c_val)}، والعددان الآخران في صف {m('x')} هما {m(known_pair[0])} و{m(known_pair[1])})، أوجد قيمة {m('x')}.",
            ans, [ans + scale_k, ans - scale_k if ans > scale_k else ans + 4, c_val + scale_k, S_mag - ans],
            f"First compute the magic sum from the center cell: {m(f'S = 3 \\times {c_val} = {S_mag}')}, then complete the row containing {m('x')}!",
            f"احسب أولاً المجموع السحري من خانة المركز: {m(f'S = 3 \\times {c_val} = {S_mag}')}، ثم أكمل صف {m('x')}!",
            f"Use {m(f'S = 3 \\times {c_val} = {S_mag}')} and subtract the two known entries in {m('x')}'s row!",
            [
                f"Since the center cell is {m(c_val)}, the magic sum of every row, column, and diagonal is {m(f'S = 3 \\times {c_val} = {S_mag}')}.",
                f"In the row containing {m('x')}, {m(f'x + {known_pair[0]} + {known_pair[1]} = {S_mag} \\implies x = {ans}')}.",
            ],
            f"Check: {m(f'{ans} + {known_pair[0]} + {known_pair[1]} = {S_mag} = 3 \\times {c_val}')}!",
            f"نوجد المجموع السحري {m(f'S = 3 \\times {c_val} = {S_mag}')} ثم نطرح العددين المعلومين في الصف!",
            [
                f"المجموع السحري = {m(f'3 \\times {c_val} = {S_mag}')}.",
                f"إذن {m(f'x = {S_mag} - ({known_pair[0]} + {known_pair[1]}) = {ans}')}.",
            ],
            f"تحقق: مجموع الصف يساوي {m(S_mag)} بالضبط!",
            diagram_en=svg_magic_square_3x3(disp),
        )

    # Hard (4): Opposite-edges-to-corner theorem in a 3x3 magic square!
    # Top-left corner (0,0) = (cell(1,2) + cell(2,1)) / 2!
    for e_right, e_bot in [(13, 19), (15, 25), (18, 26), (21, 33)]:
        ans = (e_right + e_bot) // 2
        disp = [["x", "·", "·"], ["·", "·", str(e_right)], ["·", str(e_bot), "·"]]
        B.add_math(
            tp, "Hard", bp,
            f"In the {m('3 \\times 3')} additive magic square shown, only two cells are given: the middle-right edge cell is {m(e_right)} and the bottom-middle edge cell is {m(e_bot)}. What is the value of the top-left corner {m('x')}?",
            f"في المربع السحري الجمعي {m('3 \\times 3')} الموضّح، أُعطيت خانتان فقط: يمين الوسط {m(e_right)} وأسفل الوسط {m(e_bot)}. ما قيمة الركن العلوي الأيسر {m('x')}؟",
            ans, [e_right + e_bot, e_bot - e_right, ans + 3, ans - 3],
            f"Add the **right column** and **bottom row**, then compare with the **main diagonal** through {m('x')} and the center {m('c')} (using {m('S = 3c')})!",
            f"اجمع **العمود الأيمن** و**الصف السفلي** وقارنهما بـ **القطر الرئيسي** المار بـ {m('x')} والمركز {m('c')}!",
            f"Use the Olympiad corner-average identity: {m(f'2x = {e_right} + {e_bot}')}!",
            [
                f"Let the magic sum be {m('S = 3c')} (center {m('c')}), top-right be {m('u')}, bottom-left be {m('v')}, and bottom-right be {m('w')}.",
                f"Notice {m(f'(u + {e_right} + w) + (v + {e_bot} + w) = 2S')}, while the anti-diagonal gives {m('u + c + v = S')} and main diagonal gives {m('x + c + w = S \\implies w = 2c - x')}.",
                f"Subtracting {m('u + v = S - c = 2c')} leaves {m(f'{e_right} + {e_bot} + 2(2c - x) = 4c \\implies 2x = {e_right} + {e_bot} \\implies x = {ans}')}!",
            ],
            f"Lo Shu sanity check: in {m('[[8,1,6],[3,5,7],[4,9,2]]')}, top-left {m('8 = (7 + 9)/2')}—works in **every** {m('3\\times 3')} magic square!",
            f"في أي مربع سحري {m('3 \\times 3')}، كل ركن يساوي متوسط الحافتين المقابلتين غير المجاورتين له!",
            [
                f"بجمع العمود الأيمن والصف السفلي وطرح القطر الثانوي نجد المتطابقة السحرية {m(f'2x = {e_right} + {e_bot}')}.",
                f"إذن {m(f'x = \\frac{{{e_right} + {e_bot}}}{{2}} = {ans}')}.",
            ],
            f"تحقق على مربع لو شو القياسي: {m('8 = (7 + 9)/2')}، وهنا {m(f'x = {ans}')}!",
            diagram_en=svg_magic_square_3x3(disp),
        )

    # 30. nsmo_g7_spinner_dice_prob (5E, 6M, 4H) — IMPORTANT: topic="Data & Probability"!
    tp_prob = "Data & Probability"
    bp = "nsmo_g7_spinner_dice_prob"
    easy_spin = [
        ([2, 3, 4, 5, 6, 7, 8, 9], "a **prime** number", "عدد **أولي**", lambda v: v in (2, 3, 5, 7)),
        ([1, 2, 3, 4, 5, 6], "a **divisor of 6**", "**قاسم للعدد 6**", lambda v: 6 % v == 0),
        ([3, 6, 8, 9, 11, 12, 14, 15], "a **multiple of 3**", "**مضاعف للعدد 3**", lambda v: v % 3 == 0),
        ([1, 4, 7, 9, 12, 16], "a **perfect square**", "**مربع كامل**", lambda v: v in (1, 4, 9, 16)),
        ([2, 5, 7, 10, 11, 13, 15, 18, 20, 21], "an **even** number", "عدد **زوجي**", lambda v: v % 2 == 0),
    ]
    for vals, cond_en, cond_ar, pred in easy_spin:
        fav = sum(1 for v in vals if pred(v))
        ans = Fraction(fav, len(vals))
        sectors = [(1.0 / len(vals), str(v)) for v in vals[:6]]
        B.add_math(
            tp_prob, "Easy", bp,
            f"A fair spinner is divided into {m(len(vals))} equal sectors labeled {m(', '.join(str(v) for v in vals))}. In one spin, what is the probability of landing on {cond_en}?",
            f"قُسم قرص دوار متكافئ إلى {m(len(vals))} قطاعات متساوية مرقمة بـ {m(', '.join(str(v) for v in vals))}. عند تدويره مرة واحدة، ما احتمال توقف المؤشر عند {cond_ar}؟",
            ans, [Fraction(len(vals) - fav, len(vals)), Fraction(fav + 1, len(vals)), Fraction(max(1, fav - 1), len(vals)), Fraction(1, len(vals))],
            f"Count how many of the {m(len(vals))} equal sectors satisfy the condition and reduce the fraction!",
            f"احسب عدد القطاعات التي تحقق الشرط من أصل {m(len(vals))} ثم بسّط الكسر!",
            f"Divide favorable sectors ({m(fav)}) by total equal sectors ({m(len(vals))})!",
            [
                f"Matching labels are {m(', '.join(str(v) for v in vals if pred(v)))} ({m(fav)} favorable outcomes out of {m(len(vals))}).",
                f"Probability = {m(f'\\frac{{{fav}}}{{{len(vals)}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Reduced check: {m(f'\\gcd({ ans.numerator }, { ans.denominator }) = 1')}!",
            f"نعدّ القطاعات المحققة للشرط ونقسمها على {m(len(vals))}!",
            [
                f"عدد النواتج المواتية = {m(fav)} من أصل {m(len(vals))}.",
                f"الاحتمال في أبسط صورة = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: الكسر المختزل هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            diagram_en=svg_spinner(sectors),
        )

    med_dice = [
        ("the **sum** of the two top numbers equals **8**", "أن يكون **مجموع** الرقمين الظاهرين مساوياً لـ **8**", lambda a, b: a + b == 8),
        ("the **sum** of the two top numbers is **at most 4**", "أن يكون **مجموع** الرقمين الظاهرين **4 على الأكثر**", lambda a, b: a + b <= 4),
        ("the **product** of the two top numbers is **12**", "أن يكون **حاصل ضرب** الرقمين الظاهرين مساوياً لـ **12**", lambda a, b: a * b == 12),
        ("the two top numbers differ by **exactly 3** (meaning \\( |a - b| = 3 \\))", "أن يكون الفرق المطلق بين الرقمين **3 بالضبط** (أي \\( |a - b| = 3 \\))", lambda a, b: abs(a - b) == 3),
        ("the **sum** of the two top numbers is a **multiple of 5**", "أن يكون **مجموع** الرقمين الظاهرين **مضاعفاً للعدد 5**", lambda a, b: (a + b) % 5 == 0),
        ("the **product** of the two top numbers is **odd**", "أن يكون **حاصل ضرب** الرقمين الظاهرين **فردياً**", lambda a, b: (a * b) % 2 == 1),
    ]
    for d_en, d_ar, pred in med_dice:
        fav = sum(1 for a in range(1, 7) for b in range(1, 7) if pred(a, b))
        ans = Fraction(fav, 36)
        B.add_math(
            tp_prob, "Medium", bp,
            f"Two fair standard 6-sided dice are rolled simultaneously. What is the probability that {d_en}?",
            f"رُمي حجرا نرد قياسيان متكافئان (من 1 إلى 6) معاً. ما احتمال {d_ar}؟",
            ans, [Fraction(fav + 2, 36), Fraction(max(1, fav - 1), 36), Fraction(36 - fav, 36), Fraction(fav, 12) if fav < 12 else Fraction(1, 3)],
            f"Count the favorable **ordered pairs** {m('(a, b)')} in the {m('6 \\times 6 = 36')} outcome table!",
            f"احصر **الأزواج المرتبة** {m('(a, b)')} المحققة للشرط من أصل {m('6 \\times 6 = 36')} نتيجة!",
            f"Enumerate favorable ordered pairs out of {m(36)} and simplify!",
            [
                f"There are {m('6 \\times 6 = 36')} equally likely ordered pairs {m('(a, b)')}.",
                f"Counting every pair satisfying the condition gives {m(fav)} pairs.",
                f"Probability = {m(f'\\frac{{{fav}}}{{36}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Ordered-pair grid check over all {m(36)} outcomes confirms {m(fav)} hits!",
            f"نحصي الأزواج المرتبة المواتية من أصل {m(36)} زوجاً ثم نبسط الكسر!",
            [
                f"فضاء العينة يتكون من {m(36)} زوجاً مرتباً متساوي الاحتمال.",
                f"عدد الأزواج المواتية = {m(fav)}، فالاحتمال = {m(f'\\frac{{{fav}}}{{36}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: الكسر في أبسط صورة هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            diagram_en=svg_pie_chart([(fav / 36.0, f"{fav}/36"), (1.0 - fav / 36.0, "Other")]),
        )

    hard_prob = [
        (4, 5, "both drawn marbles are **red**", "أن تكون الكرتان المسحوبتان **حمراوين معاً**", "same_r"),
        (3, 5, "the two drawn marbles have **different colors**", "أن تكون الكرتان المسحوبتان **مختلفتَي اللون**", "diff"),
        (5, 4, "the two drawn marbles have the **same color**", "أن تكون الكرتان المسحوبتان من **اللون نفسه**", "same_any"),
        (3, 7, "**at least one** of the two drawn marbles is **red**", "أن تكون **واحدة على الأقل** من الكرتين المسحوبتين **حمراء**", "at_least_1_r"),
    ]
    for r_cnt, b_cnt, ev_en, ev_ar, kind in hard_prob:
        tot = r_cnt + b_cnt
        bag = ["R"] * r_cnt + ["B"] * b_cnt
        pairs_all = [(bag[i], bag[j]) for i in range(tot) for j in range(tot) if i != j]
        if kind == "same_r":
            fav_c = sum(1 for x, y in pairs_all if x == "R" and y == "R")
        elif kind == "diff":
            fav_c = sum(1 for x, y in pairs_all if x != y)
        elif kind == "same_any":
            fav_c = sum(1 for x, y in pairs_all if x == y)
        else:
            fav_c = sum(1 for x, y in pairs_all if "R" in (x, y))
        ans = Fraction(fav_c, len(pairs_all))
        B.add_math(
            tp_prob, "Hard", bp,
            f"A jar contains {m(r_cnt)} red marbles and {m(b_cnt)} blue marbles. Two marbles are drawn one after another **without replacement**. What is the probability that {ev_en}?",
            f"تحتوي جرة على {m(r_cnt)} كرات حمراء و{m(b_cnt)} كرات زرقاء. سُحبت كرتان الواحدة تلو الأخرى **دون إرجاع**. ما احتمال {ev_ar}؟",
            ans, [Fraction(r_cnt * r_cnt, tot * tot), Fraction(1, 2) if ans != Fraction(1, 2) else Fraction(4, 9), Fraction(ans.denominator - ans.numerator, ans.denominator), Fraction(ans.numerator + 1, ans.denominator + 1)],
            f"**Without replacement** means the total drops from {m(tot)} on the 1st draw to {m(tot - 1)} on the 2nd draw ({m(tot * (tot - 1))} ordered pairs)!",
            f"**دون إرجاع** يعني أن العدد الكلي ينقص من {m(tot)} في السحبة الأولى إلى {m(tot - 1)} في السحبة الثانية!",
            f"Count ordered draws across {m(f'{tot} \\times {tot - 1} = {tot * (tot - 1)}')} outcomes without replacement!",
            [
                f"There are {m(f'{tot} \\times {tot - 1} = {len(pairs_all)}')} equally likely ordered two-draw outcomes.",
                f"Counting favorable ordered draws gives {m(fav_c)} outcomes.",
                f"Simplified probability = {m(f'\\frac{{{fav_c}}}{{{len(pairs_all)}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"Trap avoided: drawing **with** replacement uses denominator {m(tot * tot)}, whereas **without** replacement uses {m(len(pairs_all))}!",
            f"نحسب فضاء السحب المتتالي دون إرجاع {m(f'{tot} \\times {tot - 1} = {len(pairs_all)}')} ثم نبسط الكسر!",
            [
                f"إجمالي الأزواج المرتبة دون إرجاع = {m(len(pairs_all))}، والنواتج المواتية = {m(fav_c)}.",
                f"الاحتمال في أبسط صورة = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            f"تحقق: الكسر المختزل الدقيق هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}!",
            diagram_en=svg_pie_chart([(r_cnt / tot, f"{r_cnt} Red"), (b_cnt / tot, f"{b_cnt} Blue")]),
        )


def build_p1_bank() -> list[dict]:
    B = BankBuilder()
    _add_unit_1_1(B)
    _add_unit_1_2(B)
    _add_unit_1_3(B)
    _add_unit_1_4(B)
    _add_unit_1_5(B)
    _add_unit_1_6(B)
    assert len(B.items) == 450, f"Expected 450 Phase 1 questions, got {len(B.items)}"
    seen_stems: set[str] = set()
    other_stems = load_other_track_stems()
    for it in B.items:
        ns = norm_text(it["content"]["en"]["question"])
        assert ns not in seen_stems, f"Duplicate P1 stem in {it['id']}"
        assert ns not in other_stems, f"Cross-track stem collision in {it['id']}"
        seen_stems.add(ns)
    return B.items
