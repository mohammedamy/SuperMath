"""Junior Division (Grades 9–10) Question Bank Generator for Kangaroo Math Competition (360 questions)."""
import math
from fractions import Fraction
from kangaroo_common import (
    m,
    make_kang_q,
    svg_area_identity_square,
    svg_bar_chart,
    svg_circle_chords,
    svg_coord_diamond,
    svg_cube_in_cylinder,
    svg_cyclic_quad,
    svg_digit_slots,
    svg_factor_tree,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_inscribed_corner_triangle_in_rect,
    svg_isosceles_trapezoid,
    svg_kang_cube_faces,
    svg_kang_necklace_beads,
    svg_kang_polyomino_board,
    svg_midpoint_square_shaded,
    svg_number_strip,
    svg_parabola_roots,
    svg_parallel_similar_tri,
    svg_pipe_tank,
    svg_power_of_point,
    svg_right_tri_incircle,
    svg_round_table,
    svg_shaded_triangle_in_rect,
    svg_square_eighths_shaded,
    svg_street_grid,
    svg_subdivided_rect_2x2,
    svg_thales_circle,
    svg_two_jars,
    svg_water_tank_3d,
)

LEVEL = "Junior"


def _next_qid(items: list[dict], offset: int = 0) -> str:
    return f"KANG-JUN-{offset + len(items) + 1:03d}"


def _v_p_fact(n: int, p: int) -> int:
    total = 0
    pw = p
    while pw <= n:
        total += n // pw
        pw *= p
    return total


def _divisors(n: int) -> list[int]:
    out = []
    r = math.isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def _unit_4_1_number_theory(offset: int = 0) -> list[dict]:
    items: list[dict] = []
    topic = "Number Theory"

    # 1. kang_jun_rectangle_factoring_diophantine (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_rectangle_factoring_diophantine"
    easy_sfft = [
        (2, 3, 24, "Rayan", "ريان"),
        (1, 4, 32, "Lina", "لينا"),
        (3, 5, 45, "Tariq", "طارق"),
        (2, 5, 62, "Salma", "سلمى"),
        (4, 3, 72, "Omar", "عمر"),
    ]
    for a, b, c, name_en, name_ar in easy_sfft:
        P = c + a * b
        divs = _divisors(P)
        sols = [(d - b, P // d - a) for d in divs if d > b and P // d > a]
        for xv, yv in sols:
            assert xv * yv + a * xv + b * yv == c
        ans = len(sols)
        ax_t = "x" if a == 1 else f"{a}x"
        by_t = "y" if b == 1 else f"{b}y"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On {name_en}'s Junior Kangaroo warm-up sheet, how many ordered pairs {m('(x, y)')} of positive integers satisfy {m(f'xy + {ax_t} + {by_t} = {c}')}?",
            q_ar=f"في ورقة تدريب الكانجارو للناشئين الخاصة بـ{name_ar}، كم زوجاً مرتباً {m('(x, y)')} من الأعداد الصحيحة الموجبة يحقق المعادلة {m(f'xy + {ax_t} + {by_t} = {c}')}؟",
            correct_val=ans,
            distractors=[len(divs), ans + 2, max(1, ans - 1), ans + 1],
            hint_en=f"Add {m(f'{a} \\times {b} = {a*b}')} to both sides so the left side factors as {m(f'(x + {b})(y + {a})')}.",
            hint_ar=f"أضف {m(f'{a} \\times {b} = {a*b}')} إلى الطرفين لتحليل الطرف الأيسر إلى {m(f'(x + {b})(y + {a})')}.",
            idea_en=f"Complete the {m('2 \\times 2')} rectangle by adding {m(str(a*b))} to get {m(f'(x + {b})(y + {a}) = {P}')}.",
            steps_en=[
                f"Add {m(str(a*b))} to both sides: {m(f'(x + {b})(y + {a}) = {c} + {a*b} = {P}')}.",
                f"Since {m('x \\ge 1')} and {m('y \\ge 1')}, we need divisors {m('d \\mid ' + str(P))} with {m(f'd > {b}')} and {m(f'{P}/d > {a}')}.",
                f"Out of all divisors of {m(str(P))}, exact {m(str(ans))} choices give positive integer pairs {m('(x, y)')}.",
            ],
            check_en=f"Valid pairs {m('(x, y)')}: {', '.join(m(f'({u},{v})') for u, v in sols)} — {m(str(ans))} pairs in total.",
            idea_ar=f"نكمل المستطيل بإضافة {m(str(a*b))} للطرفين فنحصل على {m(f'(x + {b})(y + {a}) = {P}')}.",
            steps_ar=[
                f"بإضافة {m(str(a*b))} للطرفين: {m(f'(x + {b})(y + {a}) = {P}')}.",
                f"لضمان {m('x, y \\ge 1')} نختار قواسم {m('d')} للعدد {m(str(P))} التي تحقق {m(f'd > {b}')} و{m(f'{P}/d > {a}')}.",
                f"نجد {m(str(ans))} أزواج مرتبة موجبة بالضبط.",
            ],
            check_ar=f"الأزواج المقبولة هي {', '.join(m(f'({u},{v})') for u, v in sols)} وعددها {m(str(ans))}.",
            diagram_en=svg_subdivided_rect_2x2("xy", by_t, ax_t, str(a * b)),
        ))

    med_sfft = [
        (2, 5, 38, "badge #1"),
        (3, 6, 54, "badge #2"),
        (4, 5, 70, "badge #3"),
        (2, 7, 66, "badge #4"),
        (3, 7, 84, "badge #5"),
    ]
    for idx_m, (a, b, c, tag) in enumerate(med_sfft, 1):
        P = c + a * b
        sols = [(d - b, P // d - a) for d in _divisors(P) if d > b and P // d > a]
        best_x, best_y = max(sols, key=lambda t: t[0] + t[1])
        assert best_x * best_y + a * best_x + b * best_y == c
        ans = best_x + best_y
        min_sum = min(u + v for u, v in sols)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On Junior Kangaroo {tag}, positive integers {m('x')} and {m('y')} satisfy {m(f'xy + {a}x + {b}y = {c}')}. What is the greatest possible value of {m('x + y')}?",
            q_ar=f"في بطاقة الكانجارو للناشئين رقم {idx_m}، يحقق العددان الصحيحان الموجبان {m('x')} و{m('y')} المعادلة {m(f'xy + {a}x + {b}y = {c}')}. ما أكبر قيمة ممكنة للمجموع {m('x + y')}؟",
            correct_val=ans,
            distractors=[min_sum, ans + 2, ans - 2, P - a - b - 1],
            hint_en=f"Factor {m(f'(x + {b})(y + {a}) = {P}')} and test the most extreme valid factor pair of {m(str(P))}.",
            hint_ar=f"حلّل المعادلة إلى {m(f'(x + {b})(y + {a}) = {P}')} وجرّب أبعد زوج قواسم يحقق {m('x, y \\ge 1')}.",
            idea_en=f"For fixed product {m(f'AB = {P}')}, {m('A + B')} is maximized when {m('A')} and {m('B')} are as far apart as the positivity bounds allow.",
            steps_en=[
                f"Add {m(str(a*b))} to both sides: {m(f'(x + {b})(y + {a}) = {P}')}.",
                f"Require {m(f'x + {b} \\ge {b+1}')} and {m(f'y + {a} \\ge {a+1}')}.",
                f"The most extreme valid pair gives {m(f'(x, y) = ({best_x}, {best_y})')}, maximizing {m(f'x + y = {ans}')}.",
            ],
            check_en=f"Check {m(f'({best_x})({best_y}) + {a}({best_x}) + {b}({best_y}) = {best_x*best_y} + {a*best_x} + {b*best_y} = {c}')}.",
            idea_ar=f"عند ثبات الجداء {m(f'AB = {P}')} يكون المجموع أكبر ما يمكن عندما يتباعد القاسمان بأقصى حد يسمح ببقاء {m('x, y \\ge 1')}.",
            steps_ar=[
                f"نضيف {m(str(a*b))} للطرفين: {m(f'(x + {b})(y + {a}) = {P}')}.",
                f"الشرطان هما {m(f'x + {b} \\ge {b+1}')} و{m(f'y + {a} \\ge {a+1}')}.",
                f"أبعد زوج مقبول يعطي {m(f'(x, y) = ({best_x}, {best_y})')} فيكون أكبر مجموع {m(str(ans))}.",
            ],
            check_ar=f"التحقق بالتعويض: {m(f'{best_x*best_y} + {a*best_x} + {b*best_y} = {c}')}، صحيح!",
            diagram_en=svg_subdivided_rect_2x2("xy", f"{b}y", f"{a}x", str(a * b)),
        ))

    hard_sfft = [
        (3, 4, 24, "Round A"),
        (2, 5, 38, "Round B"),
        (4, 6, 40, "Round C"),
        (5, 3, 57, "Round D"),
        (6, 5, 70, "Round E"),
    ]
    for idx_h, (a, b, c, rnd) in enumerate(hard_sfft, 1):
        P = c + a * b
        sols = [(b + d, a + P // d) for d in _divisors(P)]
        bx, by = min(sols, key=lambda t: t[0] + t[1])
        assert bx * by - a * bx - b * by == c and bx > b and by > a
        ans = bx + by
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In Junior Kangaroo {rnd}, integers {m(f'x > {b}')} and {m(f'y > {a}')} satisfy {m(f'xy - {a}x - {b}y = {c}')}. What is the minimum possible value of {m('x + y')}?",
            q_ar=f"في جولة الكانجارو للناشئين ({idx_h})، يحقق العددان الصحيحان {m(f'x > {b}')} و{m(f'y > {a}')} المعادلة {m(f'xy - {a}x - {b}y = {c}')}. ما أصغر قيمة ممكنة للمجموع {m('x + y')}؟",
            correct_val=ans,
            distractors=[ans - 2, ans + 2, ans + 4, a + b + P + 1],
            hint_en=f"Add {m(f'{a} \\times {b} = {a*b}')} to both sides to factor {m(f'(x - {b})(y - {a}) = {P}')}, then pick the closest factor pair.",
            hint_ar=f"أضف {m(str(a*b))} للطرفين لتحصل على {m(f'(x - {b})(y - {a}) = {P}')}، ثم اختر أقرب قاسمين لبعضهما.",
            idea_en=f"Factor as {m(f'(x - {b})(y - {a}) = {P}')}; positive factors with fixed product have minimum sum when closest to {m(f'\\sqrt{{{P}}}')}.",
            steps_en=[
                f"Add {m(str(a*b))} to both sides: {m(f'(x - {b})(y - {a}) = {c} + {a*b} = {P}')}.",
                f"To minimize {m(f'x + y = {a + b} + (x - {b}) + (y - {a})')}, choose the closest factor pair of {m(str(P))}: {m(f'({bx - b}, {by - a})')}.",
                f"Thus {m(f'x = {bx}, y = {by}')}, giving minimum sum {m(f'{bx} + {by} = {ans}')}.",
            ],
            check_en=f"Verify {m(f'({bx})({by}) - {a}({bx}) - {b}({by}) = {bx*by} - {a*bx} - {b*by} = {c}')}.",
            idea_ar=f"بعد التحليل إلى {m(f'(x - {b})(y - {a}) = {P}')}، يتحقق أصغر مجموع باختيار أقرب قاسمين للجذر التربيعي.",
            steps_ar=[
                f"بإضافة {m(str(a*b))} للطرفين: {m(f'(x - {b})(y - {a}) = {P}')}.",
                f"أقرب قاسمين للعدد {m(str(P))} هما {m(f'{bx - b}')} و{m(f'{by - a}')}.",
                f"ومنه {m(f'x = {bx}')} و{m(f'y = {by}')} وأصغر مجموع هو {m(str(ans))}.",
            ],
            check_ar=f"التحقق: {m(f'{bx*by} - {a*bx} - {b*by} = {c}')} مع {m(f'x > {b}, y > {a}')}.",
            diagram_en=svg_subdivided_rect_2x2("xy", f"-{b}y", f"-{a}x", f"+{a * b}"),
        ))

    # 2. kang_jun_divisor_count_puzzle (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_divisor_count_puzzle"
    easy_div = [
        (720, "2⁴·3²·5", "16", "45", "9", "5"),
        (1260, "2²·3²·5·7", "4", "315", "9", "35"),
        (1680, "2⁴·3·5·7", "16", "105", "3", "35"),
        (2160, "2⁴·3³·5", "16", "135", "27", "5"),
        (3600, "2⁴·3²·5²", "16", "225", "9", "25"),
    ]
    for N, pfac_txt, l_lbl, r_lbl, rl_lbl, rr_lbl in easy_div:
        all_d = _divisors(N)
        odd_d = [d for d in all_d if d % 2 == 1]
        ans = len(odd_d)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo number card displaying {m(str(N))}, how many positive **odd** divisors does {m(str(N))} possess?",
            q_ar=f"على بطاقة أعداد في مسابقة الكانجارو للناشئين تحمل العدد {m(str(N))}، كم قاسماً موجباً **فردياً** للعدد {m(str(N))}؟",
            correct_val=ans,
            distractors=[len(all_d), ans + 2, max(2, ans - 2), len(all_d) // 2],
            hint_en=f"Factor {m(str(N))} completely and set the exponent of prime {m('2')} to {m('0')}.",
            hint_ar=f"حلّل العدد {m(str(N))} إلى عوامله الأولية واجعل أس العامل {m('2')} مساوياً لـ {m('0')}.",
            idea_en=f"Odd divisors of {m(str(N))} are exact divisors of its largest odd factor {m(str(N // (N & -N)))}.",
            steps_en=[
                f"Factor out all powers of {m('2')} from {m(str(N))} to leave the odd part {m(str(r_lbl))}.",
                f"Count all positive divisors of {m(str(r_lbl))} from its odd prime exponents to obtain {m(str(ans))}.",
            ],
            check_en=f"The {m(str(ans))} odd divisors of {m(str(N))} are {', '.join(str(x) for x in odd_d)}.",
            idea_ar=f"القواسم الفردية للعدد {m(str(N))} هي جميع قواسم جزئه الفردي {m(str(r_lbl))} بعد إزالة قوى {m('2')}.",
            steps_ar=[
                f"نقسم {m(str(N))} على أعلى قوة للعدد {m('2')} فنحصل على الجزء الفردي {m(str(r_lbl))}.",
                f"نحسب عدد قواسم {m(str(r_lbl))} من أسس عوامله الأولية فنجد {m(str(ans))} قاسماً فردياً.",
            ],
            check_ar=f"القواسم الفردية هي {', '.join(str(x) for x in odd_d)} وعددها {m(str(ans))}.",
            diagram_en=svg_factor_tree(str(N), l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))

    med_div = [
        (1440, "32", "45", "9", "5"),
        (2800, "16", "175", "7", "25"),
        (4320, "32", "135", "27", "5"),
        (7056, "16", "441", "9", "49"),
        (10800, "16", "675", "27", "25"),
    ]
    for N, l_lbl, r_lbl, rl_lbl, rr_lbl in med_div:
        all_d = _divisors(N)
        sq_d = [d for d in all_d if math.isqrt(d) ** 2 == d]
        ans = len(sq_d)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo prime-factor puzzle, how many positive divisors of {m(str(N))} are **perfect squares**?",
            q_ar=f"في لغز العوامل الأولية بمسابقة الكانجارو للناشئين، كم قاسماً موجباً للعدد {m(str(N))} يمثّل **مربعاً كاملاً**؟",
            correct_val=ans,
            distractors=[ans + 3, max(2, ans - 2), ans * 2, len(all_d) // 2],
            hint_en=f"A divisor {m('p^x q^y r^z')} is a perfect square iff every exponent {m('x, y, z')} is even.",
            hint_ar=f"يكون القاسم {m('p^x q^y r^z')} مربعاً كاملاً إذا وفقط إذا كانت جميع أسسه زوجية.",
            idea_en=f"For each prime power {m('p^e \\parallel ' + str(N))}, there are {m('\\lfloor e/2 \\rfloor + 1')} even exponent choices.",
            steps_en=[
                f"Factor {m(str(N))} into prime powers ({m(f'{l_lbl} \\times {rl_lbl} \\times {rr_lbl}')}).",
                f"Multiply {m('(\\lfloor e_i / 2 \\rfloor + 1)')} across each prime factor to obtain {m(str(ans))} square divisors.",
            ],
            check_en=f"Exact square divisors of {m(str(N))}: {', '.join(str(x) for x in sq_d)} ({m(str(ans))} in total).",
            idea_ar=f"لكل عامل أولي أسّه {m('e')} يوجد {m('\\lfloor e/2 \\rfloor + 1')} خياراً زوجياً للأس في القاسم المربع.",
            steps_ar=[
                f"نحلّل {m(str(N))} إلى قوى أولية ({m(f'{l_lbl} \\times {rl_lbl} \\times {rr_lbl}')}).",
                f"نضرب عدد الخيارات الزوجية للأسس فنحصل على {m(str(ans))} قواسم مربعة.",
            ],
            check_ar=f"القواسم المربعة للعدد {m(str(N))} عددها {m(str(ans))} بالضبط.",
            diagram_en=svg_factor_tree(str(N), l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))

    hard_div = [
        (10, "48", "16 = 2⁴", "3¹", "3", "1"),
        (14, "192", "64 = 2⁶", "3¹", "3", "1"),
        (15, "144", "16 = 2⁴", "9 = 3²", "3", "3"),
        (18, "180", "4 = 2²", "45", "9 = 3²", "5¹"),
        (20, "240", "16 = 2⁴", "15", "3¹", "5¹"),
    ]
    for K_cnt, root_s, l_lbl, r_lbl, rl_lbl, rr_lbl in hard_div:
        ans = next(m_v for m_v in range(1, 2500) if len(_divisors(m_v)) == K_cnt)
        assert str(ans) == root_s
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo number puzzle, what is the **smallest** positive integer that has exact {m(str(K_cnt))} positive divisors?",
            q_ar=f"في مسألة من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، ما **أصغر** عدد صحيح موجب له {m(str(K_cnt))} قاسماً موجباً بالضبط؟",
            correct_val=ans,
            distractors=[ans + 12, ans * 2, max(12, ans - 24), ans + 36],
            hint_en=f"Factor {m(str(K_cnt))} into {m('(e_1 + 1)(e_2 + 1)\\cdots')} and assign the largest exponents to the smallest primes {m('2, 3, 5')}.",
            hint_ar=f"حلّل العدد {m(str(K_cnt))} إلى عوامل {m('(e_1 + 1)(e_2 + 1)\\cdots')} وأعطِ الأسس الأكبر لأصغر الأعداد الأولية {m('2, 3, 5')}.",
            idea_en=f"Match {m(f'd(N) = {K_cnt}')} by testing factorizations of {m(str(K_cnt))} and assigning decreasing exponents to {m('2, 3, 5, \\dots')}.",
            steps_en=[
                f"Write {m(str(K_cnt))} as a product of factors {m('(e_i + 1)')} and test candidate prime-power assignments on {m('2, 3, 5')}.",
                f"Comparing candidates confirms {m(f'N = {ans}')} achieves {m(str(K_cnt))} divisors with the minimum possible value.",
            ],
            check_en=f"Direct scan confirms {m(str(ans))} has {m(str(len(_divisors(ans))))} divisors and every integer {m(f'< {ans}')} has a different count.",
            idea_ar=f"نفكك {m(str(K_cnt))} إلى جداء أقواس {m('(e_i + 1)')} ونضع الأس الأكبر على الأساس {m('2')} ثم {m('3')} ثم {m('5')}.",
            steps_ar=[
                f"نقارن جميع طرق كتابة {m(str(K_cnt))} كجداء أعداد أكبر من {m('1')} وتوزيع الأسس تنازلياً على {m('2, 3, 5')}.",
                f"أصغر قيمة ناتجة هي {m(f'N = {ans}')}.",
            ],
            check_ar=f"للعدد {m(str(ans))} بالضبط {m(str(K_cnt))} قاسماً موجباً ولا يسبقه أي عدد يحقق ذلك.",
            diagram_en=svg_factor_tree(root_s, l_lbl, r_lbl, rl_lbl, rr_lbl),
        ))

    # 3. kang_jun_factorial_trailing_zeros (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_factorial_trailing_zeros"
    for n_val in (85, 110, 145, 175, 215):
        ans = _v_p_fact(n_val, 5)
        q5, q25, q125 = n_val // 5, n_val // 25, n_val // 125
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo contest banner, the giant product {m(f'{n_val}!')} is expanded in base 10. With how many consecutive zeros does {m(f'{n_val}!')} end?",
            q_ar=f"على لافتة مسابقة الكانجارو للناشئين كُتب المضروب {m(f'{n_val}!')} بالنظام العشري. بكم صفراً متتالياً ينتهي العدد {m(f'{n_val}!')}؟",
            correct_val=ans,
            distractors=[q5, ans - 1, ans + 1, ans + 2],
            hint_en=f"Sum {m(f'\\lfloor {n_val}/5 \\rfloor + \\lfloor {n_val}/25 \\rfloor + \\lfloor {n_val}/125 \\rfloor')}.",
            hint_ar=f"اجمع {m(f'\\lfloor {n_val}/5 \\rfloor + \\lfloor {n_val}/25 \\rfloor + \\lfloor {n_val}/125 \\rfloor')}.",
            idea_en=f"Trailing zeros equal the exponent of prime {m('5')} in {m(f'{n_val}!')}.",
            steps_en=[
                f"Compute {m(f'\\lfloor {n_val}/5 \\rfloor = {q5}')}, {m(f'\\lfloor {n_val}/25 \\rfloor = {q25}')}, and {m(f'\\lfloor {n_val}/125 \\rfloor = {q125}')}.",
                f"Sum the contributions: {m(f'{q5} + {q25} + {q125} = {ans}')}.",
            ],
            check_en=f"Since {m('5^4 = 625 > ' + str(n_val))}, no higher power of {m('5')} contributes.",
            idea_ar=f"عدد الأصفار الطرفية يساوي أس العامل الأولي {m('5')} في تحليل {m(f'{n_val}!')}.",
            steps_ar=[
                f"نحسب {m(f'\\lfloor {n_val}/5 \\rfloor = {q5}')} و{m(f'\\lfloor {n_val}/25 \\rfloor = {q25}')} و{m(f'\\lfloor {n_val}/125 \\rfloor = {q125}')}.",
                f"المجموع: {m(f'{q5} + {q25} + {q125} = {ans}')} صفراً.",
            ],
            check_ar=f"بما أن {m(f'625 > {n_val}')} تتوقف السلسلة عند {m('125')} ويكون الجواب {m(str(ans))}.",
            diagram_en=svg_function_machine(f"{n_val}!", f"⌊n/5⌋={q5}", f"+{q25}+{q125}", "? zeros"),
        ))

    med_fact = [
        (40, 6, [(2, 1), (3, 1)]),
        (50, 12, [(2, 2), (3, 1)]),
        (65, 15, [(3, 1), (5, 1)]),
        (60, 18, [(2, 1), (3, 2)]),
        (95, 20, [(2, 2), (5, 1)]),
    ]
    for n_val, base_b, p_list in med_fact:
        bounds = [_v_p_fact(n_val, p) // e for p, e in p_list]
        ans = min(bounds)
        p_str = " \\times ".join(f"{p}" if e == 1 else f"{p}^{e}" for p, e in p_list)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo divisibility round, what is the largest integer {m('k')} such that {m(f'{base_b}^k')} divides {m(f'{n_val}!')}?",
            q_ar=f"في جولة قابلية القسمة بمسابقة الكانجارو للناشئين، ما أكبر عدد صحيح {m('k')} بحيث يقسم {m(f'{base_b}^k')} العدد {m(f'{n_val}!')}؟",
            correct_val=ans,
            distractors=[max(bounds) + 1, ans - 1, ans + 2, ans + 1],
            hint_en=f"Factor the composite base {m(f'{base_b} = {p_str}')} and check which prime factor runs out first in {m(f'{n_val}!')}.",
            hint_ar=f"حلّل الأساس {m(f'{base_b} = {p_str}')} وتحقّق من العامل الأولي الذي ينفد أولاً في {m(f'{n_val}!')}.",
            idea_en=f"For {m(f'{base_b}^k \\mid {n_val}!')}, {m('k')} cannot exceed {m('\\lfloor v_p(n!)/e \\rfloor')} for every prime power {m('p^e \\parallel ' + str(base_b))}.",
            steps_en=[
                f"Factor {m(f'{base_b} = {p_str}')}.",
                f"Compute prime valuations in {m(f'{n_val}!')}: bounds on {m('k')} are {', '.join(m(str(b_i)) for b_i in bounds)}.",
                f"Take the bottleneck minimum: {m(f'k = {ans}')}.",
            ],
            check_en=f"At {m(f'k = {ans + 1}')}, the limiting prime power exceeds its total exponent in {m(f'{n_val}!')}.",
            idea_ar=f"لكي يقسم {m(f'{base_b}^k')} المضروب {m(f'{n_val}!')} يجب أن يحقق {m('k \\le \\lfloor v_p(n!)/e \\rfloor')} لكل عامل أولي.",
            steps_ar=[
                f"نحلّل الأساس: {m(f'{base_b} = {p_str}')}.",
                f"نحسب حدود الأس من كل عامل أولي فنجد {', '.join(m(str(b_i)) for b_i in bounds)}.",
                f"نأخذ الحد الأصغر الحاكم فيكون {m(f'k = {ans}')}.",
            ],
            check_ar=f"عند {m(f'k = {ans + 1}')} لا تكفي قوى العامل الأولي المحدِّد داخل {m(f'{n_val}!')}.",
            diagram_en=svg_function_machine(f"{n_val}!", f"base {base_b}", "min v_p/e", "k = ?"),
        ))

    for Z_target in (12, 18, 24, 31, 37):
        ans = next(nv for nv in range(1, 500) if _v_p_fact(nv, 5) >= Z_target)
        prev_z = _v_p_fact(ans - 1, 5)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo factorial puzzle, what is the **smallest** positive integer {m('n')} for which {m('n!')} ends with at least {m(str(Z_target))} trailing zeros?",
            q_ar=f"في لغز مضروب من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، ما **أصغر** عدد صحيح موجب {m('n')} ينتهي مضروبه {m('n!')} بـ {m(str(Z_target))} صفراً طرفياً على الأقل؟",
            correct_val=ans,
            distractors=[5 * Z_target, ans - 5, ans + 5, ans + 10],
            hint_en=f"Watch out for jumps of {m('+2')} or {m('+3')} zeros when {m('n')} hits multiples of {m('25')} or {m('125')}!",
            hint_ar=f"انتبه للقفزات بمقدار صفرين أو ثلاثة عند مرور {m('n')} بمضاعفات {m('25')} أو {m('125')}!",
            idea_en=f"Test multiples of {m('5')} near {m(f'4 \\times {Z_target} = {4 * Z_target}')} using {m('Z(n!) = \\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor')}.",
            steps_en=[
                f"At {m(f'n = {ans - 1}')}, {m(f'({ans - 1})!')} has only {m(str(prev_z))} trailing zeros.",
                f"Stepping up to {m(f'n = {ans}')} supplies extra factors of {m('5')}, bringing {m(f'Z({ans}!)')} to {m(str(_v_p_fact(ans, 5)))}.",
                f"Hence the smallest valid integer is {m(f'n = {ans}')}.",
            ],
            check_en=f"Verify {m(f'Z({ans}!) = {ans//5} + {ans//25} + {ans//125} = {_v_p_fact(ans, 5)} \\ge {Z_target}')}, whereas {m(f'Z({ans-1}!) = {prev_z} < {Z_target}')}.",
            idea_ar=f"نجرّب مضاعفات {m('5')} القريبة من {m(str(4 * Z_target))} مع حساب مساهمة {m('25')} و{m('125')}.",
            steps_ar=[
                f"عند {m(f'n = {ans - 1}')} يكون عدد الأصفار {m(str(prev_z))} فقط.",
                f"وعند الوصول إلى {m(f'n = {ans}')} يرتفع عدد الأصفار إلى {m(str(_v_p_fact(ans, 5)))}.",
                f"إذن أصغر قيمة تحقق الشرط هي {m(f'n = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'{ans//5} + {ans//25} + {ans//125} = {_v_p_fact(ans, 5)}')}.",
            diagram_en=svg_function_machine("n = ?", "⌊n/5⌋+⌊n/25⌋", "+⌊n/125⌋", f"≥ {Z_target}"),
        ))

    # 4. kang_jun_modular_remainder_pattern (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_modular_remainder_pattern"
    easy_mod = [
        (7, 2025, 3, 2026, ["7", "9", "3", "1"]),
        (2, 2026, 8, 2025, ["2", "4", "8", "6"]),
        (3, 2027, 9, 2026, ["3", "9", "7", "1"]),
        (4, 2025, 7, 2026, ["7", "9", "3", "1"]),
        (8, 2027, 2, 2025, ["8", "4", "2", "6"]),
    ]
    for a, e1, b, e2, cyc_lbls in easy_mod:
        ans = (pow(a, e1, 10) + pow(b, e2, 10)) % 10
        u1, u2 = pow(a, e1, 10), pow(b, e2, 10)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Junior Kangaroo quick-fire puzzle, what is the units digit of {m(f'{a}^{{{e1}}} + {b}^{{{e2}}}')}?",
            q_ar=f"في مسألة سريعة بمسابقة الكانجارو للناشئين، ما رقم الآحاد للمقدار {m(f'{a}^{{{e1}}} + {b}^{{{e2}}}')}؟",
            correct_val=ans,
            distractors=[(ans + 2) % 10, (ans + 4) % 10, (ans + 6) % 10, (ans + 8) % 10],
            hint_en=f"Find the repeating cycle (length 2 or 4) of units digits for powers of {m(str(a))} and {m(str(b))}.",
            hint_ar=f"أوجد دورة تكرار رقم الآحاد لقوى كل من {m(str(a))} و{m(str(b))}.",
            idea_en=f"Units digits of integer powers repeat every {m('4')} steps (or fewer), so reduce exponents modulo {m('4')}.",
            steps_en=[
                f"Modulo {m('10')}, {m(f'{a}^{{{e1}}} \\equiv {u1}')} and {m(f'{b}^{{{e2}}} \\equiv {u2}')}.",
                f"Add and take the last digit: {m(f'({u1} + {u2}) \\bmod 10 = {ans}')}.",
            ],
            check_en=f"Since {m(f'{u1} + {u2} = {u1 + u2}')}, its units digit is {m(str(ans))}.",
            idea_ar=f"أرقام آحاد القوى الصحيحة تتكرر كل {m('4')} خطوات على الأكثر.",
            steps_ar=[
                f"بأخذ الباقي على {m('10')}: آحاد {m(f'{a}^{{{e1}}}')} هو {m(str(u1))} وآحاد {m(f'{b}^{{{e2}}}')} هو {m(str(u2))}.",
                f"مجموعهما {m(str(u1 + u2))} ورقم آحاده {m(str(ans))}.",
            ],
            check_ar=f"باقي قسمة {m(str(u1 + u2))} على {m('10')} هو {m(str(ans))}.",
            diagram_en=svg_kang_necklace_beads(cyc_lbls),
        ))

    med_mod = [
        (2, 2026, 7, 3, ["2", "4", "1"]),
        (5, 2025, 13, 4, ["5", "12", "8", "1"]),
        (4, 2026, 11, 5, ["4", "5", "9", "3", "1"]),
        (2, 2027, 9, 6, ["2", "4", "8", "7", "5", "1"]),
        (3, 2026, 13, 3, ["3", "9", "1"]),
    ]
    for a, exp_e, mod_m, cyc_len, cyc_lbls in med_mod:
        assert pow(a, cyc_len, mod_m) == 1
        rem_e = exp_e % cyc_len
        ans = pow(a, exp_e, mod_m)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On a Junior Kangaroo modular wheel, what is the remainder when {m(f'{a}^{{{exp_e}}}')} is divided by {m(str(mod_m))}?",
            q_ar=f"على عجلة البواقي في مسابقة الكانجارو للناشئين، ما باقي قسمة {m(f'{a}^{{{exp_e}}}')} على {m(str(mod_m))}؟",
            correct_val=ans,
            distractors=[(ans + 1) % mod_m, (ans + 2) % mod_m, (ans + 3) % mod_m, (ans + 5) % mod_m],
            hint_en=f"Compute {m(f'{a}^1, {a}^2, \\dots \\pmod{{{mod_m}}}')} until you hit {m('1')} at step {m(str(cyc_len))}.",
            hint_ar=f"احسب أولى قوى العدد {m(str(a))} باقي قسمة على {m(str(mod_m))} حتى تصل إلى الباقي {m('1')} عند الأس {m(str(cyc_len))}.",
            idea_en=f"Since {m(f'{a}^{{{cyc_len}}} \\equiv 1 \\pmod{{{mod_m}}}')}, reduce exponent {m(str(exp_e))} modulo {m(str(cyc_len))}.",
            steps_en=[
                f"Divide {m(str(exp_e))} by cycle length {m(str(cyc_len))}: {m(f'{exp_e} = {cyc_len} \\times {exp_e // cyc_len} + {rem_e}')}.",
                f"Thus {m(f'{a}^{{{exp_e}}} \\equiv {a}^{{{rem_e}}} \\equiv {ans} \\pmod{{{mod_m}}}')}.",
            ],
            check_en=f"Check {m(f'{a}^{{{rem_e}}} = {a**rem_e}')}, which leaves remainder {m(str(ans))} upon division by {m(str(mod_m))}.",
            idea_ar=f"بما أن {m(f'{a}^{{{cyc_len}}} \\equiv 1 \\pmod{{{mod_m}}}')} نختزل الأس {m(str(exp_e))} على {m(str(cyc_len))}.",
            steps_ar=[
                f"باقي قسمة الأس {m(str(exp_e))} على {m(str(cyc_len))} هو {m(str(rem_e))}.",
                f"إذن {m(f'{a}^{{{exp_e}}} \\equiv {a}^{{{rem_e}}} \\equiv {ans} \\pmod{{{mod_m}}}')}.",
            ],
            check_ar=f"المقدار {m(f'{a}^{{{rem_e}}} = {a**rem_e}')} باقي قسمته على {m(str(mod_m))} هو {m(str(ans))}.",
            diagram_en=svg_kang_necklace_beads(cyc_lbls),
        ))

    hard_mod = [
        (100, 10, 5),
        (2026, 12, 4),
        (500, 15, 5),
        (300, 18, 6),
        (400, 20, 5),
    ]
    for N_top, mod_m, cut_k in hard_mod:
        assert math.factorial(cut_k) % mod_m == 0
        partial_sum = sum(math.factorial(i) for i in range(1, cut_k))
        ans = partial_sum % mod_m
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo series problem, what is the remainder when {m(f'1! + 2! + 3! + \\dots + {N_top}!')} is divided by {m(str(mod_m))}?",
            q_ar=f"في مسألة متسلسلات من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، ما باقي قسمة المجموع {m(f'1! + 2! + 3! + \\dots + {N_top}!')} على {m(str(mod_m))}؟",
            correct_val=ans,
            distractors=[0, (ans + 1) % mod_m, (ans + 3) % mod_m, (ans + 6) % mod_m],
            hint_en=f"Every factorial from {m(f'{cut_k}!')} onward is already a multiple of {m(str(mod_m))}!",
            hint_ar=f"لاحظ أن كل مضروب بدءاً من {m(f'{cut_k}!')} فصاعداً يقبل القسمة على {m(str(mod_m))} ويعطي باقياً صفراً!",
            idea_en=f"Since {m(f'{mod_m} \\mid {cut_k}!')}, all terms {m(f'k!')} with {m(f'k \\ge {cut_k}')} vanish modulo {m(str(mod_m))}.",
            steps_en=[
                f"Check {m(f'{cut_k}! = {math.factorial(cut_k)}')}, which is divisible by {m(str(mod_m))}, so {m(f'{cut_k}!, ({cut_k+1})!, \\dots, {N_top}! \\equiv 0 \\pmod{{{mod_m}}}')}.",
                f"Sum only the surviving head terms: {m(' + '.join(f'{i}!' for i in range(1, cut_k)) + f' = {partial_sum}')}.",
                f"Take the remainder modulo {m(str(mod_m))}: {m(f'{partial_sum} \\equiv {ans} \\pmod{{{mod_m}}}')}.",
            ],
            check_en=f"Adding {m(f'{cut_k}! = {math.factorial(cut_k)}')} shifts the sum by a multiple of {m(str(mod_m))}, leaving remainder {m(str(ans))} unchanged.",
            idea_ar=f"بما أن {m(f'{cut_k}! = {math.factorial(cut_k)}')} يقبل القسمة على {m(str(mod_m))}، تختفي جميع الحدود من {m(f'{cut_k}!')} حتى {m(f'{N_top}!')}.",
            steps_ar=[
                f"نحذف الحدود من {m(f'{cut_k}!')} فصاعداً لأن باقي قسمتها على {m(str(mod_m))} يساوي {m('0')}.",
                f"نجمع الحدود الأولى المتبقية فقط فنجد {m(str(partial_sum))}.",
                f"باقي قسمة {m(str(partial_sum))} على {m(str(mod_m))} يساوي {m(str(ans))}.",
            ],
            check_ar=f"{m(f'{partial_sum} = {mod_m} \\times {partial_sum // mod_m} + {ans}')}، إذن الباقي هو {m(str(ans))} تماماً.",
            diagram_en=svg_kang_necklace_beads(["1!", "2!", "3!", f"0 (≥{cut_k}!)"]),
        ))

    return items


def _unit_4_2_algebra(offset: int = 60) -> list[dict]:
    items: list[dict] = []
    topic = "Algebra"

    # 5. kang_jun_square_completion_identity (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_square_completion_identity"
    easy_sq = [
        (1998, 4),
        (2025, 5),
        (1500, 7),
        (3010, 6),
        (4050, 8),
    ]
    for mid_m, diff_d in easy_sq:
        n1, n2, sq_d = mid_m - diff_d, mid_m + diff_d, diff_d * diff_d
        rad = n1 * n2 + sq_d
        ans = math.isqrt(rad)
        assert ans * ans == rad and ans == mid_m
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"Without a calculator on a Junior Kangaroo mental-algebra card, what is the exact integer value of {m(f'\\sqrt{{{n1} \\times {n2} + {sq_d}}}')}?",
            q_ar=f"دون استخدام آلة حاسبة في بطاقة جبر ذهني بمسابقة الكانجارو للناشئين، ما القيمة الصحيحة الدقيقة للمقدار {m(f'\\sqrt{{{n1} \\times {n2} + {sq_d}}}')}؟",
            correct_val=ans,
            distractors=[n1, n2, ans - 2, ans + 2],
            hint_en=f"Write {m(str(n1))} and {m(str(n2))} as {m(f'({mid_m} - {diff_d})')} and {m(f'({mid_m} + {diff_d})')}.",
            hint_ar=f"اكتب {m(str(n1))} و{m(str(n2))} على الصورة {m(f'({mid_m} - {diff_d})')} و{m(f'({mid_m} + {diff_d})')}.",
            idea_en=f"Use {m('(m - d)(m + d) + d^2 = m^2')} around midpoint {m(f'm = {mid_m}')}.",
            steps_en=[
                f"Set {m(f'm = {mid_m}')}, so {m(f'{n1} \\times {n2} = (m - {diff_d})(m + {diff_d}) = m^2 - {sq_d}')}.",
                f"Adding {m(str(sq_d))} gives {m('m^2')}, whose positive square root is {m(str(ans))}.",
            ],
            check_en=f"Check last digit: {m(f'({n1 % 10} \\times {n2 % 10} + {sq_d}) \\bmod 10 = {(rad) % 10}')}, matching {m(f'{ans}^2')}.",
            idea_ar=f"نطبق المتطابقة {m('(m - d)(m + d) + d^2 = m^2')} حول المنتصف {m(f'm = {mid_m}')}.",
            steps_ar=[
                f"نضع {m(f'm = {mid_m}')} فيكون {m(f'{n1} \\times {n2} = m^2 - {sq_d}')}.",
                f"بإضافة {m(str(sq_d))} نحصل على {m('m^2')} وجذره التربيعي الموجب {m(str(ans))}.",
            ],
            check_ar=f"مربع {m(str(ans))} يساوي {m(f'{n1} \\times {n2} + {sq_d}')} بالضبط.",
            diagram_en=svg_area_identity_square(str(mid_m), str(diff_d)),
        ))

    med_sq = [
        (5, 6),
        (7, 8),
        (6, 11),
        (9, 10),
        (8, 15),
    ]
    for D_val, P_val in med_sq:
        ans = D_val * D_val + 4 * P_val
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo algebraic symmetry problem, real numbers {m('a')} and {m('b')} satisfy {m(f'a - b = {D_val}')} and {m(f'ab = {P_val}')}. What is the value of {m('(a + b)^2')}?",
            q_ar=f"في مسألة تماثل جبري بمسابقة الكانجارو للناشئين، يحقق العددان الحقيقيان {m('a')} و{m('b')} العلاقتين {m(f'a - b = {D_val}')} و{m(f'ab = {P_val}')}. ما قيمة {m('(a + b)^2')}؟",
            correct_val=ans,
            distractors=[D_val * D_val + 2 * P_val, abs(D_val * D_val - 4 * P_val), D_val * D_val + P_val, (D_val + P_val) ** 2],
            hint_en=f"Compare the expansions of {m('(a + b)^2')} and {m('(a - b)^2')} — they differ by {m('4ab')}.",
            hint_ar=f"قارن مفكوكي {m('(a + b)^2')} و{m('(a - b)^2')}؛ الفرق بينهما هو {m('4ab')}.",
            idea_en=f"Apply the four-rectangle identity {m('(a + b)^2 = (a - b)^2 + 4ab')}.",
            steps_en=[
                f"Write {m('(a + b)^2 = a^2 + 2ab + b^2 = (a^2 - 2ab + b^2) + 4ab = (a - b)^2 + 4ab')}.",
                f"Substitute {m(f'a - b = {D_val}')} and {m(f'ab = {P_val}')}: {m(f'{D_val}^2 + 4({P_val}) = {D_val*D_val} + {4*P_val} = {ans}')}.",
            ],
            check_en=f"Here {m(f'a^2 + b^2 = {D_val}^2 + 2({P_val}) = {D_val*D_val + 2*P_val}')}, and adding {m(f'2ab = {2*P_val}')} gives {m(str(ans))}.",
            idea_ar=f"نستخدم المتطابقة المباشرة {m('(a + b)^2 = (a - b)^2 + 4ab')}.",
            steps_ar=[
                f"لدينا {m('(a + b)^2 = (a - b)^2 + 4ab')}.",
                f"بالتعويض: {m(f'{D_val}^2 + 4 \\times {P_val} = {D_val*D_val} + {4*P_val} = {ans}')}.",
            ],
            check_ar=f"{m(f'a^2 + b^2 = {D_val*D_val + 2*P_val}')}، وبإضافة {m(f'2ab = {2*P_val}')} نحصل على {m(str(ans))}.",
            diagram_en=svg_area_identity_square("a", "b"),
        ))

    hard_sq = [
        (3, 4, 40),
        (5, 2, 45),
        (4, 5, 52),
        (6, 2, 58),
        (5, 7, 95),
    ]
    for p_v, q_v, C_v in hard_sq:
        ans = C_v - p_v * p_v - q_v * q_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"As {m('x')} and {m('y')} vary over all real numbers in a Junior Kangaroo optimization puzzle, what is the minimum possible value of {m(f'x^2 + y^2 - {2*p_v}x + {2*q_v}y + {C_v}')}?",
            q_ar=f"عند تغيّر العددين الحقيقيين {m('x')} و{m('y')} في مسألة قيم قصوى بمسابقة الكانجارو للناشئين، ما أصغر قيمة ممكنة للمقدار {m(f'x^2 + y^2 - {2*p_v}x + {2*q_v}y + {C_v}')}؟",
            correct_val=ans,
            distractors=[C_v, p_v * p_v + q_v * q_v, ans + p_v, C_v - p_v - q_v],
            hint_en=f"Complete the square separately in {m('x')} and in {m('y')}.",
            hint_ar=f"أكمل المربع بالنسبة للمتغير {m('x')} على حدة وبالنسبة للمتغير {m('y')} على حدة.",
            idea_en=f"Rewrite as {m(f'(x - {p_v})^2 + (y + {q_v})^2 + ({C_v} - {p_v}^2 - {q_v}^2)')}; squares of reals are always {m('\\ge 0')}.",
            steps_en=[
                f"Complete both squares: {m(f'(x^2 - {2*p_v}x + {p_v*p_v}) + (y^2 + {2*q_v}y + {q_v*q_v}) + {C_v} - {p_v*p_v} - {q_v*q_v}')}.",
                f"This equals {m(f'(x - {p_v})^2 + (y + {q_v})^2 + {ans}')}.",
                f"Setting {m(f'x = {p_v}')} and {m(f'y = -{q_v}')} makes both squares {m('0')}, achieving minimum {m(str(ans))}.",
            ],
            check_en=f"Plug in {m(f'({p_v}, -{q_v})')}: {m(f'{p_v*p_v} + {q_v*q_v} - {2*p_v*p_v} - {2*q_v*q_v} + {C_v} = {ans}')}.",
            idea_ar=f"نكمل المربع في {m('x')} وفي {m('y')} معاً، وبما أن المربعات الحقيقية غير سالبة تتحقق الصغرى عند تصفيرهما.",
            steps_ar=[
                f"نعيد كتابة المقدار: {m(f'(x - {p_v})^2 + (y + {q_v})^2 + {C_v} - {p_v*p_v} - {q_v*q_v}')}.",
                f"أي {m(f'(x - {p_v})^2 + (y + {q_v})^2 + {ans} \\ge {ans}')}.",
                f"تتحقق القيمة الصغرى {m(str(ans))} عند {m(f'(x, y) = ({p_v}, -{q_v})')}.",
            ],
            check_ar=f"بالتعويض المباشر بالنقطة {m(f'({p_v}, -{q_v})')} ينتج {m(str(ans))} تماماً.",
            diagram_en=svg_area_identity_square("x", str(p_v)),
        ))

    # 6. kang_jun_vieta_quadratic_symmetry (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_vieta_quadratic_symmetry"
    for B_v, C_v in [(6, 4), (8, 5), (9, 7), (10, 6), (11, 8)]:
        assert B_v * B_v - 4 * C_v > 0
        ans = B_v * B_v - 2 * C_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"If {m('r')} and {m('s')} are the real roots of {m(f'x^2 - {B_v}x + {C_v} = 0')} on a Junior Kangaroo quiz, what is {m('r^2 + s^2')}?",
            q_ar=f"إذا كان {m('r')} و{m('s')} الجذرين الحقيقيين للمعادلة {m(f'x^2 - {B_v}x + {C_v} = 0')} في مسابقة الكانجارو للناشئين، فما قيمة {m('r^2 + s^2')}؟",
            correct_val=ans,
            distractors=[B_v * B_v, B_v * B_v - C_v, B_v * B_v + 2 * C_v, B_v * B_v - 4 * C_v],
            hint_en=f"Read {m(f'r + s = {B_v}')} and {m(f'rs = {C_v}')} via Vieta's formulas, then use {m('r^2 + s^2 = (r + s)^2 - 2rs')}.",
            hint_ar=f"استخرج {m(f'r + s = {B_v}')} و{m(f'rs = {C_v}')} من فييت ثم طبّق {m('r^2 + s^2 = (r + s)^2 - 2rs')}.",
            idea_en=f"By Vieta's formulas, {m(f'r + s = {B_v}')} and {m(f'rs = {C_v}')}.",
            steps_en=[
                f"Identify {m(f'r + s = {B_v}')} and {m(f'rs = {C_v}')}.",
                f"Compute {m(f'r^2 + s^2 = (r + s)^2 - 2rs = {B_v}^2 - 2({C_v}) = {B_v*B_v} - {2*C_v} = {ans}')}.",
            ],
            check_en=f"Discriminant {m(f'{B_v}^2 - 4({C_v}) = {B_v*B_v - 4*C_v} > 0')} confirms both roots are real.",
            idea_ar=f"من علاقات فييت لدينا {m(f'r + s = {B_v}')} و{m(f'rs = {C_v}')}.",
            steps_ar=[
                f"مجموع الجذرين {m(str(B_v))} وحاصل ضربهما {m(str(C_v))}.",
                f"نحسب {m(f'r^2 + s^2 = {B_v}^2 - 2({C_v}) = {ans}')}.",
            ],
            check_ar=f"المميز {m(f'{B_v*B_v - 4*C_v} > 0')} يضمن أن الجذرين حقيقيان.",
            diagram_en=svg_parabola_roots("r", "s", f"S={B_v}"),
        ))

    med_vieta = [
        (2, 7, 3),
        (3, 8, 2),
        (2, 9, 5),
        (3, 10, 4),
        (4, 11, 3),
    ]
    for A_v, B_v, C_v in med_vieta:
        assert B_v * B_v - 4 * A_v * C_v > 0
        ans = Fraction(B_v * B_v - 2 * A_v * C_v, C_v * C_v)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo quadratic challenge, {m('r')} and {m('s')} are the roots of {m(f'{A_v}x^2 - {B_v}x + {C_v} = 0')}. What is the value of {m('\\frac{1}{r^2} + \\frac{1}{s^2}')}?",
            q_ar=f"في مسألة معادلات تربيعية بمسابقة الكانجارو للناشئين، إذا كان {m('r')} و{m('s')} جذري المعادلة {m(f'{A_v}x^2 - {B_v}x + {C_v} = 0')}، فما قيمة {m('\\frac{1}{r^2} + \\frac{1}{s^2}')}؟",
            correct_val=ans,
            distractors=[Fraction(B_v * B_v, C_v * C_v), Fraction(B_v * B_v + 2 * A_v * C_v, C_v * C_v), Fraction(B_v * B_v - 2 * C_v, C_v * C_v), Fraction(B_v, C_v)],
            hint_en=f"Write {m('\\frac{1}{r^2} + \\frac{1}{s^2} = \\frac{(r + s)^2 - 2rs}{(rs)^2}')} using {m(f'r + s = {B_v}/{A_v}')} and {m(f'rs = {C_v}/{A_v}')}.",
            hint_ar=f"وحّد المقامات {m('\\frac{(r + s)^2 - 2rs}{(rs)^2}')} مع استخدام {m(f'r + s = {B_v}/{A_v}')} و{m(f'rs = {C_v}/{A_v}')}.",
            idea_en=f"Notice {m('1/r')} and {m('1/s')} are the roots of the reversed quadratic {m(f'{C_v}u^2 - {B_v}u + {A_v} = 0')}!",
            steps_en=[
                f"By Vieta's formulas, {m(f'r + s = \\frac{{{B_v}}}{{{A_v}}}')} and {m(f'rs = \\frac{{{C_v}}}{{{A_v}}}')}.",
                f"Then {m(f'\\frac{{1}}{{r}} + \\frac{{1}}{{s}} = \\frac{{r + s}}{{rs}} = \\frac{{{B_v}}}{{{C_v}}}')} and {m(f'\\frac{{1}}{{rs}} = \\frac{{{A_v}}}{{{C_v}}}')}.",
                f"Square and subtract: {m(f'\\left(\\frac{{{B_v}}}{{{C_v}}}\\right)^2 - 2\\left(\\frac{{{A_v}}}{{{C_v}}}\\right) = \\frac{{{B_v*B_v - 2*A_v*C_v}}}{{{C_v*C_v}}}')}.",
            ],
            check_en=f"Using {m(f'u_1 = 1/r, u_2 = 1/s')} on {m(f'{C_v}u^2 - {B_v}u + {A_v} = 0')} gives the exact same value!",
            idea_ar=f"المقلوبان {m('1/r')} و{m('1/s')} يحققان {m(f'\\frac{{1}}{{r}} + \\frac{{1}}{{s}} = \\frac{{{B_v}}}{{{C_v}}}')} وحاصل ضربهما {m(f'\\frac{{{A_v}}}{{{C_v}}}')}.",
            steps_ar=[
                f"من علاقات فييت: {m(f'r + s = \\frac{{{B_v}}}{{{A_v}}}')} و{m(f'rs = \\frac{{{C_v}}}{{{A_v}}}')}.",
                f"نحسب {m(f'\\frac{{1}}{{r^2}} + \\frac{{1}}{{s^2}} = \\left(\\frac{{r + s}}{{rs}}\\right)^2 - \\frac{{2}}{{rs}} = \\frac{{{B_v*B_v} - {2*A_v*C_v}}}{{{C_v*C_v}}}')}.",
            ],
            check_ar=f"اختصار الكسر يعطي النتيجة النهائية بدقة.",
            diagram_en=svg_parabola_roots("r", "s", f"a={A_v}"),
        ))

    for B_v, C_v in [(5, 2), (6, 4), (7, 5), (8, 3), (9, 6)]:
        assert B_v * B_v - 4 * C_v > 0
        ans = B_v ** 3 - 3 * B_v * C_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo root-sum problem, {m('r')} and {m('s')} satisfy {m(f'x^2 - {B_v}x + {C_v} = 0')}. What is the exact value of {m('r^3 + s^3')}?",
            q_ar=f"في مسألة مجموع قوى الجذور (٥ نقاط) بمسابقة الكانجارو للناشئين، يحقق الجذران {m('r')} و{m('s')} المعادلة {m(f'x^2 - {B_v}x + {C_v} = 0')}. ما القيمة الدقيقة للمقدار {m('r^3 + s^3')}؟",
            correct_val=ans,
            distractors=[B_v ** 3, B_v ** 3 - B_v * C_v, (B_v * B_v - 2 * C_v) * B_v, B_v ** 3 + 3 * B_v * C_v],
            hint_en=f"Use the symmetric cube identity {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            hint_ar=f"استخدم متطابقة مجموع المكعبين المتماثلة {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            idea_en=f"Factor {m('r^3 + s^3 = (r + s)(r^2 - rs + s^2) = (r + s)^3 - 3rs(r + s)')}.",
            steps_en=[
                f"From Vieta's formulas, {m(f'r + s = {B_v}')} and {m(f'rs = {C_v}')}.",
                f"Evaluate {m(f'r^3 + s^3 = {B_v}^3 - 3({C_v})({B_v}) = {B_v**3} - {3*B_v*C_v} = {ans}')}.",
            ],
            check_en=f"Alternatively, {m(f'r^2 + s^2 = {B_v*B_v - 2*C_v}')}, so {m(f'(r + s)(r^2 - rs + s^2) = {B_v} \\times {B_v*B_v - 3*C_v} = {ans}')}.",
            idea_ar=f"نعوّض {m(f'r + s = {B_v}')} و{m(f'rs = {C_v}')} في متطابقة {m('(r + s)^3 - 3rs(r + s)')}.",
            steps_ar=[
                f"من فييت: {m(f'r + s = {B_v}')} و{m(f'rs = {C_v}')}.",
                f"إذن {m(f'r^3 + s^3 = {B_v**3} - {3*B_v*C_v} = {ans}')}.",
            ],
            check_ar=f"طريقة ثانية: {m(f'(r + s)(r^2 - rs + s^2) = {B_v} \\times {B_v*B_v - 3*C_v} = {ans}')}.",
            diagram_en=svg_parabola_roots("r", "s", "r³+s³"),
        ))

    # 7. kang_jun_reciprocal_sum_squares (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_reciprocal_sum_squares"
    for k_v in (3, 5, 6, 7, 8):
        ans = k_v * k_v - 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo algebra card, a positive real number {m('x')} satisfies {m(f'x + \\frac{{1}}{{x}} = {k_v}')}. What is {m('x^2 + \\frac{1}{x^2}')}?",
            q_ar=f"في بطاقة جبر بمسابقة الكانجارو للناشئين، يحقق العدد الحقيقي الموجب {m('x')} العلاقة {m(f'x + \\frac{{1}}{{x}} = {k_v}')}. ما قيمة {m('x^2 + \\frac{1}{x^2}')}؟",
            correct_val=ans,
            distractors=[k_v * k_v, k_v * k_v + 2, k_v * k_v - 1, k_v * k_v - 4],
            hint_en=f"Square {m(f'x + \\frac{{1}}{{x}} = {k_v}')} and simplify the middle term {m('2 \\cdot x \\cdot \\frac{1}{x}')}.",
            hint_ar=f"ربّع طرفي المعادلة {m(f'x + \\frac{{1}}{{x}} = {k_v}')} وبسّط الحد الأوسط {m('2 \\cdot x \\cdot \\frac{1}{x}')}.",
            idea_en=f"Since {m('\\left(x + \\frac{1}{x}\\right)^2 = x^2 + 2 + \\frac{1}{x^2}')}, subtract {m('2')} from {m(f'{k_v}^2')}.",
            steps_en=[
                f"Square both sides: {m(f'x^2 + 2 + \\frac{{1}}{{x^2}} = {k_v}^2 = {k_v*k_v}')}.",
                f"Subtract {m('2')}: {m(f'x^2 + \\frac{{1}}{{x^2}} = {k_v*k_v} - 2 = {ans}')}.",
            ],
            check_en=f"Since {m(f'{k_v} \\ge 2')}, real solutions exist and {m(f'{ans} + 2 = {k_v*k_v}')}.",
            idea_ar=f"مفكوك {m('\\left(x + \\frac{1}{x}\\right)^2')} يعطي {m('x^2 + \\frac{1}{x^2} + 2')}.",
            steps_ar=[
                f"بتربيع الطرفين: {m(f'x^2 + 2 + \\frac{{1}}{{x^2}} = {k_v*k_v}')}.",
                f"بطرح {m('2')} نحصل على {m(str(ans))}.",
            ],
            check_ar=f"{m(f'{ans} + 2 = {k_v*k_v} = {k_v}^2')}، صحيح.",
            diagram_en=svg_area_identity_square("x", "1/x"),
        ))

    for k_v in (3, 4, 5, 6, 7):
        ans = k_v ** 3 - 3 * k_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo reciprocal puzzle, if {m(f'x + \\frac{{1}}{{x}} = {k_v}')}, what is the exact value of {m('x^3 + \\frac{1}{x^3}')}?",
            q_ar=f"في لغز مقلوبات بمسابقة الكانجارو للناشئين، إذا كان {m(f'x + \\frac{{1}}{{x}} = {k_v}')}، فما القيمة الدقيقة للمقدار {m('x^3 + \\frac{1}{x^3}')}؟",
            correct_val=ans,
            distractors=[k_v ** 3, k_v ** 3 - 3, k_v ** 3 + 3 * k_v, (k_v * k_v - 2) * k_v],
            hint_en=f"Cube {m('x + \\frac{1}{x}')}: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}.",
            hint_ar=f"كعّب المقدار: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}.",
            idea_en=f"Apply {m('x^3 + \\frac{1}{x^3} = k^3 - 3k')} for {m(f'k = {k_v}')}.",
            steps_en=[
                f"Expand {m(f'\\left(x + \\frac{{1}}{{x}}\\right)^3 = x^3 + \\frac{{1}}{{x^3}} + 3\\left(x + \\frac{{1}}{{x}}\\right) = {k_v}^3 = {k_v**3}')}.",
                f"Subtract {m(f'3({k_v}) = {3*k_v}')}: {m(f'x^3 + \\frac{{1}}{{x^3}} = {k_v**3} - {3*k_v} = {ans}')}.",
            ],
            check_en=f"Also {m(f'\\left(x + \\frac{{1}}{{x}}\\right)\\left(x^2 - 1 + \\frac{{1}}{{x^2}}\\right) = {k_v} \\times ({k_v*k_v - 2} - 1) = {ans}')}.",
            idea_ar=f"نطبق المتطابقة التكعيبية {m('x^3 + \\frac{1}{x^3} = k^3 - 3k')}.",
            steps_ar=[
                f"بتكعيب الطرفين: {m(f'x^3 + \\frac{{1}}{{x^3}} + 3({k_v}) = {k_v**3}')}.",
                f"بطرح {m(str(3*k_v))} نجد {m(f'x^3 + \\frac{{1}}{{x^3}} = {ans}')}.",
            ],
            check_ar=f"تحقق بديل: {m(f'{k_v} \\times ({k_v*k_v - 3}) = {ans}')}.",
            diagram_en=svg_area_identity_square("x", "1/x"),
        ))

    for k_v in (2, 3, 5, 6, 7):
        s2 = k_v * k_v + 2
        ans = s2 * s2 - 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo algebra problem, a nonzero real number {m('x')} satisfies {m(f'x^2 - {k_v}x - 1 = 0')}. What is the value of {m('x^4 + \\frac{1}{x^4}')}?",
            q_ar=f"في مسألة جبر من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، يحقق العدد الحقيقي غير الصفري {m('x')} المعادلة {m(f'x^2 - {k_v}x - 1 = 0')}. ما قيمة {m('x^4 + \\frac{1}{x^4}')}؟",
            correct_val=ans,
            distractors=[(k_v * k_v - 2) ** 2 - 2, s2 * s2, s2 * s2 + 2, k_v ** 4],
            hint_en=f"Divide the equation {m(f'x^2 - {k_v}x - 1 = 0')} through by {m('x')} to isolate {m(f'x - \\frac{{1}}{{x}} = {k_v}')}!",
            hint_ar=f"اقسم طرفي المعادلة {m(f'x^2 - {k_v}x - 1 = 0')} على {m('x')} لتحصل فوراً على {m(f'x - \\frac{{1}}{{x}} = {k_v}')}!",
            idea_en=f"Dividing by {m('x')} reveals {m(f'x - \\frac{{1}}{{x}} = {k_v}')}; square twice with careful middle-term signs.",
            steps_en=[
                f"Divide {m(f'x^2 - {k_v}x - 1 = 0')} by {m('x \\neq 0')}: {m(f'x - \\frac{{1}}{{x}} = {k_v}')}.",
                f"Square once: {m(f'x^2 - 2 + \\frac{{1}}{{x^2}} = {k_v*k_v} \\implies x^2 + \\frac{{1}}{{x^2}} = {s2}')}.",
                f"Square again: {m(f'x^4 + 2 + \\frac{{1}}{{x^4}} = {s2}^2 = {s2*s2} \\implies x^4 + \\frac{{1}}{{x^4}} = {ans}')}.",
            ],
            check_en=f"Discriminant {m(f'{k_v}^2 + 4 = {k_v*k_v + 4} > 0')} guarantees nonzero real roots.",
            idea_ar=f"بقسمة المعادلة على {m('x')} نجد {m(f'x - \\frac{{1}}{{x}} = {k_v}')}، ثم نربّع مرتين متتاليتين.",
            steps_ar=[
                f"بالقسمة على {m('x')}: {m(f'x - \\frac{{1}}{{x}} = {k_v}')}.",
                f"التربيع الأول يعطي {m(f'x^2 + \\frac{{1}}{{x^2}} = {k_v*k_v} + 2 = {s2}')}.",
                f"التربيع الثاني يعطي {m(f'x^4 + \\frac{{1}}{{x^4}} = {s2}^2 - 2 = {ans}')}.",
            ],
            check_ar=f"{m(f'{s2*s2} - 2 = {ans}')} مع الانتباه لاختلاف إشارة الحد الأوسط بين الخطوتين.",
            diagram_en=svg_area_identity_square("x²", "1/x²"),
        ))

    # 8. kang_jun_floor_step_equations (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_floor_step_equations"
    easy_fl = [
        (2, 1, 9, 4),
        (3, 4, 11, 5),
        (2, 3, 13, 3),
        (4, 1, 15, 4),
        (3, 2, 14, 5),
    ]
    for a_v, b_v, d_v, m_v in easy_fl:
        sols = [nv for nv in range(1, 300) if (a_v * nv + b_v) // d_v == m_v]
        ans = len(sols)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Junior Kangaroo step-interval puzzle, how many positive integers {m('n')} satisfy {m(f'\\left\\lfloor \\frac{{{a_v}n + {b_v}}}{{{d_v}}} \\right\\rfloor = {m_v}')}?",
            q_ar=f"في لغز دالة الجزء الصحيح بمسابقة الكانجارو للناشئين، كم عدداً صحيحاً موجباً {m('n')} يحقق المعادلة {m(f'\\left\\lfloor \\frac{{{a_v}n + {b_v}}}{{{d_v}}} \\right\\rfloor = {m_v}')}؟",
            correct_val=ans,
            distractors=[ans + 1, max(1, ans - 1), ans + 2, d_v],
            hint_en=f"Rewrite the floor equation as {m(f'{m_v} \\le \\frac{{{a_v}n + {b_v}}}{{{d_v}}} < {m_v + 1}')}.",
            hint_ar=f"اكتب المتباينة المزدوجة المكافئة {m(f'{m_v} \\le \\frac{{{a_v}n + {b_v}}}{{{d_v}}} < {m_v + 1}')}.",
            idea_en=f"Multiply {m(f'{m_v} \\le \\frac{{{a_v}n + {b_v}}}{{{d_v}}} < {m_v + 1}')} by {m(str(d_v))} and count integers.",
            steps_en=[
                f"Unpack bounds: {m(f'{m_v * d_v} \\le {a_v}n + {b_v} < {(m_v + 1) * d_v}')}.",
                f"Subtract {m(str(b_v))}: {m(f'{m_v * d_v - b_v} \\le {a_v}n < {(m_v + 1) * d_v - b_v}')}.",
                f"The integer solutions are {m(', '.join(str(s) for s in sols))}, giving {m(str(ans))} solutions.",
            ],
            check_en=f"Testing endpoints confirms exact {m(str(ans))} integers land inside the interval.",
            idea_ar=f"نضرب المتباينة المزدوجة في {m(str(d_v))} ثم نعزل {m('n')} ونعدّ القيم الصحيحة.",
            steps_ar=[
                f"نفكّ الجزء الصحيح: {m(f'{m_v * d_v} \\le {a_v}n + {b_v} < {(m_v + 1) * d_v}')}.",
                f"بطرح {m(str(b_v))} والقسمة على {m(str(a_v))} نجد الحلول {m(', '.join(str(s) for s in sols))}.",
                f"عدد الحلول الصحيحة الموجبة هو {m(str(ans))}.",
            ],
            check_ar=f"تعويض القيم الحدية يؤكد أن عدد الحلول {m(str(ans))} بالضبط.",
            diagram_en=svg_number_strip([str(s) for s in sols[:4]] if len(sols) <= 4 else [str(sols[0]), "...", str(sols[-1])]),
        ))

    for N_sq in (24, 35, 48, 63, 80):
        ans = sum(math.isqrt(i) for i in range(1, N_sq + 1))
        top_k = math.isqrt(N_sq)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On a Junior Kangaroo sum-of-floors card, what is the exact value of {m(f'\\lfloor\\sqrt{{1}}\\rfloor + \\lfloor\\sqrt{{2}}\\rfloor + \\lfloor\\sqrt{{3}}\\rfloor + \\dots + \\lfloor\\sqrt{{{N_sq}}}\\rfloor')}?",
            q_ar=f"في بطاقة مجاميع بمسابقة الكانجارو للناشئين، ما القيمة الدقيقة للمجموع {m(f'\\lfloor\\sqrt{{1}}\\rfloor + \\lfloor\\sqrt{{2}}\\rfloor + \\lfloor\\sqrt{{3}}\\rfloor + \\dots + \\lfloor\\sqrt{{{N_sq}}}\\rfloor')}؟",
            correct_val=ans,
            distractors=[ans - top_k, ans + top_k + 1, ans - (2 * top_k + 1), N_sq * top_k // 2],
            hint_en=f"Group terms between consecutive perfect squares: for {m('k^2 \\le m < (k+1)^2')}, there are {m('2k + 1')} integers with {m('\\lfloor\\sqrt{m}\\rfloor = k')}.",
            hint_ar=f"جمّع الحدود الواقعة بين المربعات الكاملة المتتالية: يوجد {m('2k + 1')} عدداً يحقق {m('\\lfloor\\sqrt{m}\\rfloor = k')} في الفترة {m('k^2 \\le m < (k+1)^2')}.",
            idea_en=f"Notice {m(f'{N_sq} = {top_k + 1}^2 - 1')}, so every block {m('k = 1, \\dots, ' + str(top_k))} is completely full with {m('2k + 1')} terms!",
            steps_en=[
                f"For each {m(f'k \\in \\{{1, \\dots, {top_k}\\}}')}, the {m('2k + 1')} integers from {m('k^2')} to {m('(k+1)^2 - 1')} all have floor-root {m('k')}.",
                f"Block {m('k')} contributes {m('k(2k + 1)')}; summing {m('k = 1')} to {m(str(top_k))} gives {m(' + '.join(str(k*(2*k+1)) for k in range(1, top_k+1)) + f' = {ans}')}.",
            ],
            check_en=f"Total number of terms counted is {m(' + '.join(str(2*k+1) for k in range(1, top_k+1)) + f' = {N_sq}')}!",
            idea_ar=f"العدد {m(f'{N_sq} = {(top_k+1)**2 - 1}')} يكمل جميع المجموعات من {m('k = 1')} حتى {m(f'k = {top_k}')} بلا نقص.",
            steps_ar=[
                f"لكل قيمة {m('k')} يوجد {m('2k + 1')} حداً قيمتها {m('k')} فتعطي مساهمة قدرها {m('k(2k + 1)')}.",
                f"بجمع المساهمات من {m('1')} إلى {m(str(top_k))} نحصل على {m(str(ans))}.",
            ],
            check_ar=f"مجموع أعداد الحدود في المجموعات يساوي {m(str(N_sq))} حداً بالضبط.",
            diagram_en=svg_function_machine(f"1..{N_sq}", "k²..(k+1)²−1", "k(2k+1)", f"Sum = ?"),
        ))

    hard_fl = [
        (3, 8),
        (4, 15),
        (5, 16),
        (3, 14),
        (4, 21),
    ]
    for p_v, K_v in hard_fl:
        sols = []
        for n_int in range(-10, 50):
            rem = K_v - (p_v - 1) * n_int
            if 0 <= rem < p_v:
                sols.append(Fraction(n_int) + Fraction(rem, p_v))
        for x_s in sols:
            assert p_v * x_s - math.floor(x_s) == K_v
        ans = sum(sols, Fraction(0))
        int_only = Fraction(K_v, p_v - 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo real-floor equation, what is the **sum of all real numbers** {m('x')} that satisfy {m(f'{p_v}x - \\lfloor x \\rfloor = {K_v}')}?",
            q_ar=f"في معادلة جزء صحيح من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، ما **مجموع جميع الأعداد الحقيقية** {m('x')} التي تحقق {m(f'{p_v}x - \\lfloor x \\rfloor = {K_v}')}؟",
            correct_val=ans,
            distractors=[int_only, ans + 1, ans - Fraction(1, p_v), ans + Fraction(1, p_v)],
            hint_en=f"Write {m('x = n + f')} where {m('n = \\lfloor x \\rfloor')} is an integer and {m('0 \\le f < 1')}.",
            hint_ar=f"اكتب {m('x = n + f')} حيث {m('n = \\lfloor x \\rfloor')} عدد صحيح و{m('0 \\le f < 1')}.",
            idea_en=f"Substituting {m('x = n + f')} gives {m(f'{p_v - 1}n + {p_v}f = {K_v}')}, trapping {m(f'{K_v} - {p_v - 1}n')} inside {m(f'[0, {p_v})')}.",
            steps_en=[
                f"Let {m('x = n + f')} with {m('n \\in \\mathbb{Z}')} and {m('0 \\le f < 1')}, so {m(f'{p_v}f = {K_v} - {p_v - 1}n \\in [0, {p_v})')}.",
                f"Testing integers {m('n')} yields the valid real roots {', '.join(m(str(s)) for s in sols)}.",
                f"Their sum equals {m(str(ans))}.",
            ],
            check_en=f"Plug each solution into {m(f'{p_v}x - \\lfloor x \\rfloor')}: both produce {m(str(K_v))}!",
            idea_ar=f"بوضع {m('x = n + f')} نحصل على {m(f'0 \\le {K_v} - {p_v - 1}n < {p_v}')} فنستخرج جميع القيم الممكنة للعدد الصحيح {m('n')}.",
            steps_ar=[
                f"نعوّض {m('x = n + f')} مع {m('0 \\le f < 1')} فنجد {m(f'{p_v}f = {K_v} - {p_v - 1}n')}.",
                f"قيم {m('n')} الصحيحة المقبولة تعطي الجذور الحقيقية {', '.join(m(str(s)) for s in sols)}.",
                f"بجمع الجذور نجد المجموع {m(str(ans))}.",
            ],
            check_ar=f"كل جذر يحقق المعادلة الأصلية {m(f'{p_v}x - \\lfloor x \\rfloor = {K_v}')} بدقة.",
            diagram_en=svg_function_machine("x = n + f", f"{p_v - 1}n + {p_v}f = {K_v}", f"0 ≤ {p_v}f < {p_v}", "Sum x"),
        ))

    return items


def _unit_4_3_geometry_circles_sim(offset: int = 120) -> list[dict]:
    items: list[dict] = []
    topic = "Geometry"

    # 9. kang_jun_cyclic_thales_angles (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_cyclic_thales_angles"
    for alpha in (23, 29, 37, 41, 52):
        ans = 2 * alpha
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo circle diagram, {m('AB')} is a diameter with center {m('O')}, and point {m('C')} lies on the circle such that {m(f'\\angle CAB = {alpha}^\\circ')}. What is the measure of central angle {m('\\angle BOC')}?",
            q_ar=f"في رسم دائرة بمسابقة الكانجارو للناشئين، {m('AB')} قطر مركزه {m('O')} والنقطة {m('C')} تقع على الدائرة بحيث {m(f'\\angle CAB = {alpha}^\\circ')}. ما قياس الزاوية المركزية {m('\\angle BOC')}؟",
            correct_val=ans,
            distractors=[90 - alpha, 180 - 2 * alpha, alpha, 90 + alpha],
            suffix="^\\circ",
            hint_en=f"Radii {m('OA')} and {m('OC')} are equal, making {m('\\triangle OAC')} isosceles with exterior angle {m('\\angle BOC')}.",
            hint_ar=f"نصفا القطرين {m('OA')} و{m('OC')} متساويان، والزاوية {m('\\angle BOC')} خارجية عن المثلث المتطابق الضلعين {m('OAC')}.",
            idea_en=f"Central angle {m('\\angle BOC')} subtends the same arc {m('BC')} as inscribed angle {m('\\angle BAC')}, so {m('\\angle BOC = 2\\angle BAC')}.",
            steps_en=[
                f"Since {m('OA = OC')}, {m(f'\\angle OCA = \\angle OAC = {alpha}^\\circ')}.",
                f"By the Exterior Angle Theorem on {m('\\triangle OAC')}, {m(f'\\angle BOC = {alpha}^\\circ + {alpha}^\\circ = {ans}^\\circ')}.",
            ],
            check_en=f"Also {m('\\angle ACB = 90^\\circ \\implies \\angle OBC = ' + str(90 - alpha) + '^\\circ')}, so isosceles {m('\\triangle OBC')} has apex {m(f'180^\\circ - 2({90 - alpha}^\\circ) = {ans}^\\circ')}.",
            idea_ar=f"الزاوية المركزية {m('\\angle BOC')} تساوي ضعف الزاوية المحيطية {m('\\angle BAC')} المشتركة معها في القوس {m('BC')}.",
            steps_ar=[
                f"بما أن {m('OA = OC')} فإن {m(f'\\angle OCA = {alpha}^\\circ')}.",
                f"الزاوية الخارجية {m(f'\\angle BOC = {alpha}^\\circ + {alpha}^\\circ = {ans}^\\circ')}.",
            ],
            check_ar=f"في المثلث {m('OBC')} زاويتا القاعدة {m(f'{90 - alpha}^\\circ')}، فزاوية الرأس {m(f'180^\\circ - {180 - 2*alpha}^\\circ = {ans}^\\circ')}.",
            diagram_en=svg_thales_circle(f"{alpha}°", "?"),
        ))

    med_cyc = [
        (15, 25),
        (10, 35),
        (20, 15),
        (5, 45),
        (25, 30),
    ]
    for p_v, q_v in med_cyc:
        assert (180 - p_v - q_v) % 5 == 0
        xv = (180 - p_v - q_v) // 5
        ans = 2 * xv + p_v
        ang_c = 3 * xv + q_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"Cyclic quadrilateral {m('ABCD')} is inscribed in a circle on a Junior Kangaroo test with {m(f'\\angle A = (2x + {p_v})^\\circ')} and opposite angle {m(f'\\angle C = (3x + {q_v})^\\circ')}. What is the measure of {m('\\angle A')}?",
            q_ar=f"رباعي دائري {m('ABCD')} مرسوم داخل دائرة في اختبار الكانجارو للناشئين فيه {m(f'\\angle A = (2x + {p_v})^\\circ')} والزاوية المقابلة {m(f'\\angle C = (3x + {q_v})^\\circ')}. ما قياس الزاوية {m('\\angle A')}؟",
            correct_val=ans,
            distractors=[ang_c, xv, ans + 10, abs(90 - xv)],
            suffix="^\\circ",
            hint_en=f"Opposite angles in any cyclic quadrilateral sum to {m('180^\\circ')}.",
            hint_ar=f"مجموع كل زاويتين متقابلتين في الرباعي الدائري يساوي {m('180^\\circ')}.",
            idea_en=f"Solve {m(f'(2x + {p_v}) + (3x + {q_v}) = 180')} for {m('x')}, then evaluate {m(f'2x + {p_v}')}.",
            steps_en=[
                f"Set {m(f'5x + {p_v + q_v} = 180 \\implies 5x = {180 - p_v - q_v} \\implies x = {xv}')}.",
                f"Substitute back into {m('\\angle A')}: {m(f'2({xv}) + {p_v} = {ans}^\\circ')}.",
            ],
            check_en=f"Opposite angle {m(f'\\angle C = 3({xv}) + {q_v} = {ang_c}^\\circ')}, and {m(f'{ans}^\\circ + {ang_c}^\\circ = 180^\\circ')}.",
            idea_ar=f"نجمع الزاويتين المتقابلتين ونساويهما بـ {m('180^\\circ')} لإيجاد {m('x')} ثم نحسب {m('\\angle A')}.",
            steps_ar=[
                f"نحل {m(f'5x + {p_v + q_v} = 180 \\implies x = {xv}')}.",
                f"نعوّض في قياس {m('\\angle A')}: {m(f'2({xv}) + {p_v} = {ans}^\\circ')}.",
            ],
            check_ar=f"الزاوية المقابلة {m(f'{ang_c}^\\circ')}، ومجموعهما {m(f'{ans}^\\circ + {ang_c}^\\circ = 180^\\circ')}.",
            diagram_en=svg_cyclic_quad(f"2x+{p_v}°", f"3x+{q_v}°"),
        ))

    hard_cyc = [
        (40, 60, 80),
        (36, 70, 74),
        (50, 48, 82),
        (44, 56, 80),
        (30, 84, 66),
    ]
    for u_arc, w_arc, v_arc in hard_cyc:
        assert u_arc + w_arc + v_arc == 180
        ang_c = 90 + u_arc // 2
        ang_d = 90 + v_arc // 2
        ans = 540 - 2 * (ang_c + ang_d)
        assert ans == w_arc
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo circle problem, points {m('A, D, C, B')} lie in order along a semicircle with diameter {m('AB')} and center {m('O')}. In convex quadrilateral {m('ABCD')}, {m(f'\\angle BCD = {ang_c}^\\circ')} and {m(f'\\angle ADC = {ang_d}^\\circ')}. What is central angle {m('\\angle COD')}?",
            q_ar=f"في مسألة دوائر من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، تقع النقاط {m('A, D, C, B')} بالترتيب على نصف دائرة قطرها {m('AB')} ومركزها {m('O')}. إذا كان في الرباعي المحدب {m('ABCD')} قياس {m(f'\\angle BCD = {ang_c}^\\circ')} و{m(f'\\angle ADC = {ang_d}^\\circ')}، فما قياس الزاوية المركزية {m('\\angle COD')}؟",
            correct_val=ans,
            distractors=[180 - ans, ans // 2, (ang_d - ang_c) * 2 + 20, ans + 12],
            suffix="^\\circ",
            hint_en=f"Find {m('\\angle BAD')} and {m('\\angle ABC')} from cyclic quadrilateral {m('ABCD')}, then use isosceles triangles {m('OAD')} and {m('OBC')}.",
            hint_ar=f"أوجد {m('\\angle BAD')} و{m('\\angle ABC')} من الرباعي الدائري، ثم استخدم المثلثين المتطابقي الضلعين {m('OAD')} و{m('OBC')}.",
            idea_en=f"Cyclic supplementary angles give base angles of isosceles {m('\\triangle OAD')} and {m('\\triangle OBC')}, isolating {m('\\angle COD')} along straight diameter {m('AOB')}.",
            steps_en=[
                f"In cyclic {m('ABCD')}, {m(f'\\angle BAD = 180^\\circ - {ang_c}^\\circ = {180 - ang_c}^\\circ')} and {m(f'\\angle ABC = 180^\\circ - {ang_d}^\\circ = {180 - ang_d}^\\circ')}.",
                f"In isosceles {m('\\triangle OAD')} ({m('OA = OD')}) and {m('\\triangle OBC')} ({m('OB = OC')}), {m(f'\\angle AOD = 180^\\circ - 2({180 - ang_c}^\\circ) = {u_arc}^\\circ')} and {m(f'\\angle BOC = 180^\\circ - 2({180 - ang_d}^\\circ) = {v_arc}^\\circ')}.",
                f"Along straight line {m('AOB')}, {m(f'\\angle COD = 180^\\circ - {u_arc}^\\circ - {v_arc}^\\circ = {ans}^\\circ')}.",
            ],
            check_en=f"Check {m(f'{u_arc}^\\circ + {ans}^\\circ + {v_arc}^\\circ = 180^\\circ')} along the semicircle.",
            idea_ar=f"نستخرج زاويتي القاعدة {m('\\angle A')} و{m('\\angle B')} من الرباعي الدائري ثم نحسب الزوايا المركزية على القطر المستقيم {m('AB')}.",
            steps_ar=[
                f"من تكامل زوايا الرباعي الدائري: {m(f'\\angle BAD = {180 - ang_c}^\\circ')} و{m(f'\\angle ABC = {180 - ang_d}^\\circ')}.",
                f"في المثلثين المتطابقي الضلعين {m('OAD')} و{m('OBC')}: {m(f'\\angle AOD = {u_arc}^\\circ')} و{m(f'\\angle BOC = {v_arc}^\\circ')}.",
                f"على القطر المستقيم {m('AOB')}: {m(f'\\angle COD = 180^\\circ - {u_arc}^\\circ - {v_arc}^\\circ = {ans}^\\circ')}.",
            ],
            check_ar=f"مجموع الأقواس الثلاثة {m(f'{u_arc}^\\circ + {ans}^\\circ + {v_arc}^\\circ = 180^\\circ')}.",
            diagram_en=svg_cyclic_quad(f"{180 - ang_c}°", f"{ang_c}°"),
        ))

    # 10. kang_jun_similar_area_ratio (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_similar_area_ratio"
    easy_sim = [
        (1, 2, 7),
        (2, 1, 12),
        (3, 2, 18),
        (1, 3, 5),
        (3, 1, 27),
    ]
    for p_v, q_v, top_area in easy_sim:
        assert (top_area * (p_v + q_v) ** 2) % (p_v * p_v) == 0
        ans = (top_area * (p_v + q_v) ** 2) // (p_v * p_v)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In {m('\\triangle ABC')} on a Junior Kangaroo geometry card, {m('D')} on {m('AB')} and {m('E')} on {m('AC')} satisfy {m('DE \\parallel BC')} and {m(f'AD : DB = {p_v} : {q_v}')}. If {m(f'[\\triangle ADE] = {top_area}\\text{{ cm}}^2')}, what is {m('[\\triangle ABC]')} in {m('\\text{cm}^2')}?",
            q_ar=f"في المثلث {m('ABC')} بمسابقة الكانجارو للناشئين، يقع {m('D')} على {m('AB')} و{m('E')} على {m('AC')} بحيث {m('DE \\parallel BC')} والنسبة {m(f'AD : DB = {p_v} : {q_v}')}. إذا كانت مساحة {m(f'\\triangle ADE = {top_area}\\text{{ cm}}^2')}، فما مساحة {m('\\triangle ABC')} بوحدة {m('\\text{cm}^2')}؟",
            correct_val=ans,
            distractors=[ans - top_area, top_area * (p_v + q_v) // p_v, top_area * (q_v * q_v) // max(1, p_v * p_v) + top_area, ans + top_area],
            hint_en=f"First find {m(f'AD : AB = {p_v} : {p_v + q_v}')}, then square the ratio to compare areas.",
            hint_ar=f"احسب النسبة الكلية {m(f'AD : AB = {p_v} : {p_v + q_v}')} ثم ربّعها لإيجاد نسبة المساحتين.",
            idea_en=f"Similar triangles scale in area by {m(f'\\left(\\frac{{AD}}{{AB}}\\right)^2 = \\left(\\frac{{{p_v}}}{{{p_v + q_v}}}\\right)^2')}.",
            steps_en=[
                f"Whole-side ratio: {m(f'AD : AB = {p_v} : ({p_v} + {q_v}) = {p_v} : {p_v + q_v}')}.",
                f"Square the scale factor: {m(f'[\\triangle ABC] = {top_area} \\times \\frac{{({p_v + q_v})^2}}{{{p_v}^2}} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_en=f"Ratio {m(f'{top_area} : {ans} = {p_v*p_v} : {(p_v+q_v)**2}')}.",
            idea_ar=f"نسبة المساحتين تساوي مربع نسبة الضلعين المتناظرين {m(f'\\left(\\frac{{{p_v}}}{{{p_v + q_v}}}\\right)^2')}.",
            steps_ar=[
                f"النسبة إلى الضلع الكامل: {m(f'AD : AB = {p_v} : {p_v + q_v}')}.",
                f"مساحة {m(f'\\triangle ABC = {top_area} \\times \\frac{{{(p_v + q_v)**2}}}{{{p_v*p_v}}} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_ar=f"التحقق من النسبة: {m(f'{top_area} / {ans} = {p_v*p_v} / {(p_v+q_v)**2}')}.",
            diagram_en=svg_parallel_similar_tri(str(p_v), str(q_v), "DE", "BC"),
        ))

    med_sim = [
        (2, 5, 3, 25),
        (3, 5, 2, 30),
        (2, 7, 1, 28),
        (3, 8, 2, 24),
        (4, 7, 1, 35),
    ]
    for p_v, tot_v, k_mul, bc_len in med_sim:
        s1 = k_mul * p_v * p_v
        s2 = k_mul * (tot_v * tot_v - p_v * p_v)
        assert (bc_len * p_v) % tot_v == 0
        ans = (bc_len * p_v) // tot_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"Segment {m('DE \\parallel BC')} cuts {m('\\triangle ABC')} on a Junior Kangaroo blueprint into top triangle {m('ADE')} of area {m(f'{s1}\\text{{ cm}}^2')} and trapezoid {m('DBCE')} of area {m(f'{s2}\\text{{ cm}}^2')}. If {m(f'BC = {bc_len}\\text{{ cm}}')}, what is the length of {m('DE')} in {m('\\text{cm}')}?",
            q_ar=f"يقطع المستقيم {m('DE \\parallel BC')} المثلث {m('ABC')} في مخطط الكانجارو للناشئين إلى مثلث علوي {m('ADE')} مساحته {m(f'{s1}\\text{{ cm}}^2')} وشبه منحرف {m('DBCE')} مساحته {m(f'{s2}\\text{{ cm}}^2')}. إذا كان {m(f'BC = {bc_len}\\text{{ cm}}')}، فما طول {m('DE')} بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[ans + 2, max(2, ans - 2), bc_len * s1 // (s1 + s2), bc_len - ans],
            hint_en=f"Add {m(f'{s1} + {s2} = {s1 + s2}')} for the full area of {m('\\triangle ABC')}, then take the square root of the area ratio!",
            hint_ar=f"اجمع المساحتين {m(f'{s1} + {s2} = {s1 + s2}')} لإيجاد مساحة المثلث الكلي ثم خذ الجذر التربيعي لنسبة المساحتين!",
            idea_en=f"Linear ratio {m('DE / BC')} equals {m('\\sqrt{[\\triangle ADE] / [\\triangle ABC]}')}.",
            steps_en=[
                f"Full triangle area is {m(f'[\\triangle ABC] = {s1} + {s2} = {s1 + s2}\\text{{ cm}}^2')}.",
                f"Area ratio is {m(f'\\frac{{{s1}}}{{{s1 + s2}}} = \\frac{{{p_v*p_v}}}{{{tot_v*tot_v}}}')}, so linear ratio {m(f'\\frac{{DE}}{{BC}} = \\frac{{{p_v}}}{{{tot_v}}}')}.",
                f"Hence {m(f'DE = {bc_len} \\times \\frac{{{p_v}}}{{{tot_v}}} = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Verify {m(f'({ans}/{bc_len})^2 = ({p_v}/{tot_v})^2 = {s1}/{s1 + s2}')}.",
            idea_ar=f"نسبة الطولين {m('DE / BC')} تساوي الجذر التربيعي لنسبة مساحة {m('ADE')} إلى المساحة الكلية.",
            steps_ar=[
                f"المساحة الكلية للمثلث: {m(f'{s1} + {s2} = {s1 + s2}\\text{{ cm}}^2')}.",
                f"معامل التشابه الخطي: {m(f'\\sqrt{{\\frac{{{s1}}}{{{s1 + s2}}}}} = \\frac{{{p_v}}}{{{tot_v}}}')}.",
                f"إذن {m(f'DE = {bc_len} \\times \\frac{{{p_v}}}{{{tot_v}}} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"مربع النسبة {m(f'({ans}/{bc_len})^2 = {s1}/{s1 + s2}')} مطابق للمعطيات.",
            diagram_en=svg_parallel_similar_tri(f"{p_v}k", f"{tot_v - p_v}k", "? cm", f"{bc_len} cm"),
        ))

    hard_sim = [
        (1, 3, 5),
        (2, 2, 3),
        (1, 4, 7),
        (3, 2, 5),
        (2, 3, 4),
    ]
    for k_m, p_v, q_v in hard_sim:
        a_top = k_m * p_v * p_v
        a_bot = k_m * q_v * q_v
        a_wing = k_m * p_v * q_v
        ans = k_m * (p_v + q_v) ** 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo trapezoid {m('ABCD')} with {m('AB \\parallel CD')}, diagonals {m('AC')} and {m('BD')} meet at {m('P')}. If {m(f'[\\triangle ABP] = {a_top}\\text{{ cm}}^2')} and {m(f'[\\triangle CDP] = {a_bot}\\text{{ cm}}^2')}, what is the total area of trapezoid {m('ABCD')} in {m('\\text{cm}^2')}?",
            q_ar=f"في شبه منحرف {m('ABCD')} من فئة ٥ نقاط بمسابقة الكانجارو للناشئين حيث {m('AB \\parallel CD')}، يتقاطع القطران {m('AC')} و{m('BD')} في {m('P')}. إذا كانت مساحة {m(f'\\triangle ABP = {a_top}\\text{{ cm}}^2')} ومساحة {m(f'\\triangle CDP = {a_bot}\\text{{ cm}}^2')}، فما المساحة الكلية لشبه المنحرف {m('ABCD')} بوحدة {m('\\text{cm}^2')}؟",
            correct_val=ans,
            distractors=[a_top + a_bot, a_top + a_bot + a_wing, ans - a_wing, 2 * (a_top + a_bot)],
            hint_en=f"Triangles {m('ABP')} and {m('CDP')} are similar with scale factor {m(f'{p_v} : {q_v}')}; use {m('AP : PC = BP : PD = ' + f'{p_v} : {q_v}')} to find the two side triangles!",
            hint_ar=f"المثلثان {m('ABP')} و{m('CDP')} متشابهان بنسبة خطية {m(f'{p_v} : {q_v}')}؛ استعمل نسبة أجزاء القطر لإيجاد مساحتي المثلثين الجانبيين!",
            idea_en=f"In any trapezoid cut by diagonals, each wing triangle has area {m('\\sqrt{[\\triangle ABP][\\triangle CDP]}')}, so total area is {m('\\left(\\sqrt{S_1} + \\sqrt{S_2}\\right)^2')}.",
            steps_en=[
                f"From {m('\\triangle ABP \\sim \\triangle CDP')}, {m(f'\\frac{{AP}}{{PC}} = \\sqrt{{\\frac{{{a_top}}}{{{a_bot}}}}} = \\frac{{{p_v}}}{{{q_v}}}')}.",
                f"Sharing altitude from {m('B')}, {m(f'[\\triangle BCP] = \\frac{{PC}}{{AP}} [\\triangle ABP] = \\frac{{{q_v}}}{{{p_v}}} \\times {a_top} = {a_wing}\\text{{ cm}}^2')}, and symmetrically {m(f'[\\triangle ADP] = {a_wing}\\text{{ cm}}^2')}.",
                f"Total area {m(f'= {a_top} + {a_bot} + 2({a_wing}) = {ans}\\text{{ cm}}^2')}.",
            ],
            check_en=f"Check {m(f'(\\sqrt{{{a_top}}} + \\sqrt{{{a_bot}}})^2 = {k_m}({p_v} + {q_v})^2 = {ans}')}.",
            idea_ar=f"مساحة كل مثلث جانبي تساوي الوسط الهندسي {m('\\sqrt{S_1 S_2}')}، والمساحة الكلية {m('(\\sqrt{S_1} + \\sqrt{S_2})^2')}.",
            steps_ar=[
                f"نسبة التشابه الخطية بين المثلثين المتقابلين هي {m(f'\\sqrt{{{a_top}/{a_bot}}} = {p_v}/{q_v}')}.",
                f"مساحة كل من المثلثين الجانبيين {m('ADP')} و{m('BCP')} تساوي {m(f'\\sqrt{{{a_top} \\times {a_bot}}} = {a_wing}\\text{{ cm}}^2')}.",
                f"المساحة الكلية {m(f'= {a_top} + {a_bot} + 2({a_wing}) = {ans}\\text{{ cm}}^2')}.",
            ],
            check_ar=f"مجموع الأجزاء الأربعة {m(f'{a_top} + {a_wing} + {a_wing} + {a_bot} = {ans}\\text{{ cm}}^2')}.",
            diagram_en=svg_isosceles_trapezoid(f"S₁={a_top}", f"S₂={a_bot}", "ABCD", "P"),
        ))

    # 11. kang_jun_intersecting_chords_power (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_intersecting_chords_power"
    easy_ch = [
        (4, 15, 6),
        (6, 14, 7),
        (8, 9, 6),
        (5, 18, 9),
        (9, 12, 6),
    ]
    for ae, eb, ce in easy_ch:
        assert (ae * eb) % ce == 0
        ans = (ae * eb) // ce
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"Chords {m('AB')} and {m('CD')} intersect at interior point {m('E')} of a circle on a Junior Kangaroo sheet. If {m(f'AE = {ae}\\text{{ cm}}')}, {m(f'EB = {eb}\\text{{ cm}}')}, and {m(f'CE = {ce}\\text{{ cm}}')}, what is {m('ED')} in {m('\\text{cm}')}?",
            q_ar=f"يتقاطع الوتران {m('AB')} و{m('CD')} في نقطة داخلية {m('E')} من دائرة في ورقة الكانجارو للناشئين. إذا كان {m(f'AE = {ae}\\text{{ cm}}')} و{m(f'EB = {eb}\\text{{ cm}}')} و{m(f'CE = {ce}\\text{{ cm}}')}، فما طول {m('ED')} بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[ae + eb - ce, ans + 2, max(2, ans - 2), ans + 4],
            hint_en=f"Equate the products of chord segments: {m('AE \\cdot EB = CE \\cdot ED')}.",
            hint_ar=f"ساوِ جداءي أجزاء الوترين: {m('AE \\cdot EB = CE \\cdot ED')}.",
            idea_en=f"By the Intersecting Chords Theorem, {m('ED = (AE \\cdot EB) / CE')}.",
            steps_en=[
                f"Write {m(f'{ae} \\times {eb} = {ce} \\times ED')}.",
                f"Divide {m(str(ae * eb))} by {m(str(ce))} to get {m(f'ED = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Both products equal {m(f'{ae} \\times {eb} = {ce} \\times {ans} = {ae * eb}')}.",
            idea_ar=f"نطبق مبرهنة تقاطع الأوتار: {m('ED = (AE \\cdot EB) / CE')}.",
            steps_ar=[
                f"نكتب {m(f'{ae} \\times {eb} = {ce} \\times ED')}.",
                f"بقسمة {m(str(ae * eb))} على {m(str(ce))} نجد {m(f'ED = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"الجداءان متساويان: {m(f'{ce} \\times {ans} = {ae * eb}')}.",
            diagram_en=svg_circle_chords(str(ae), str(eb), str(ce), "?"),
        ))

    med_ch = [
        (4, 5),
        (4, 12),
        (5, 15),
        (9, 7),
        (7, 21),
    ]
    for pa, ab in med_ch:
        pb = pa + ab
        ans = math.isqrt(pa * pb)
        assert ans * ans == pa * pb
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"From an exterior point {m('P')} on a Junior Kangaroo geometry diagram, tangent {m('PT')} touches a circle at {m('T')} and secant {m('PAB')} meets it at {m('A')} then {m('B')}. If {m(f'PA = {pa}\\text{{ cm}}')} and chord {m(f'AB = {ab}\\text{{ cm}}')}, what is {m('PT')} in {m('\\text{cm}')}?",
            q_ar=f"من نقطة خارجية {m('P')} في رسم هندسي بمسابقة الكانجارو للناشئين، يمس المستقيم {m('PT')} الدائرة في {m('T')} ويقطعها القاطع {m('PAB')} في {m('A')} ثم {m('B')}. إذا كان {m(f'PA = {pa}\\text{{ cm}}')} وطول الوتر {m(f'AB = {ab}\\text{{ cm}}')}، فما طول المماس {m('PT')} بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[pb, ans + 2, max(2, ans - 2), pa + ab // 2],
            hint_en=f"Find the whole secant {m(f'PB = PA + AB = {pb}')} first, then apply {m('PT^2 = PA \\cdot PB')}.",
            hint_ar=f"احسب طول القاطع كاملاً {m(f'PB = PA + AB = {pb}')} أولاً ثم طبّق {m('PT^2 = PA \\cdot PB')}.",
            idea_en=f"Tangent-Secant Power of a Point states {m('PT^2 = PA \\cdot (PA + AB)')}.",
            steps_en=[
                f"Compute full secant length: {m(f'PB = {pa} + {ab} = {pb}\\text{{ cm}}')}.",
                f"Apply {m(f'PT^2 = {pa} \\times {pb} = {pa * pb} \\implies PT = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Verify {m(f'{ans}^2 = {ans*ans} = {pa} \\times ({pa} + {ab})')}.",
            idea_ar=f"مبرهنة المماس والقاطع تعطي {m('PT^2 = PA \\cdot (PA + AB)')}.",
            steps_ar=[
                f"طول القاطع الكامل: {m(f'PB = {pa} + {ab} = {pb}\\text{{ cm}}')}.",
                f"ومنه {m(f'PT = \\sqrt{{{pa} \\times {pb}}} = \\sqrt{{{pa * pb}}} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"{m(f'{ans}^2 = {pa * pb}')}، مطابق لقوة النقطة {m('P')}.",
            diagram_en=svg_power_of_point("?", str(pa), str(ab)),
        ))

    hard_ch = [
        (4, 9, 8),
        (6, 12, 7),
        (8, 15, 7),
        (9, 16, 9),
        (9, 25, 8),
    ]
    for u_v, v_v, d_v in hard_ch:
        r_sq = d_v * d_v + u_v * v_v
        ans = math.isqrt(r_sq)
        assert ans * ans == r_sq
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"Inside a circle with center {m('O')} in a 5-point Junior Kangaroo problem, point {m('E')} on chord {m('AB')} divides it into {m(f'AE = {u_v}\\text{{ cm}}')} and {m(f'EB = {v_v}\\text{{ cm}}')}. If {m(f'OE = {d_v}\\text{{ cm}}')}, what is the radius of the circle in {m('\\text{cm}')}?",
            q_ar=f"داخل دائرة مركزها {m('O')} في مسألة من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، تقسم النقطة {m('E')} الوتر {m('AB')} إلى {m(f'AE = {u_v}\\text{{ cm}}')} و{m(f'EB = {v_v}\\text{{ cm}}')}. إذا كان {m(f'OE = {d_v}\\text{{ cm}}')}، فما نصف قطر الدائرة بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[ans - 1, ans + 2, (u_v + v_v) // 2 + 1, ans + 1],
            hint_en=f"Draw the diameter through {m('O')} and {m('E')}! It splits at {m('E')} into segments {m('R - OE')} and {m('R + OE')}.",
            hint_ar=f"ارسم القطر المار بـ {m('O')} و{m('E')}؛ ينقسم عند {m('E')} إلى جزأين طولاهما {m('R - OE')} و{m('R + OE')}.",
            idea_en=f"Intersecting chord {m('AB')} with the diameter through {m('O, E')} gives {m('(R - d)(R + d) = AE \\cdot EB')}, or {m('R^2 = d^2 + AE \\cdot EB')}.",
            steps_en=[
                f"Extend {m('OE')} into a full diameter {m('CD')}, whose segments at {m('E')} have lengths {m(f'R - {d_v}')} and {m(f'R + {d_v}')}.",
                f"By Intersecting Chords, {m(f'(R - {d_v})(R + {d_v}) = {u_v} \\times {v_v} = {u_v * v_v}')}.",
                f"Solve {m(f'R^2 = {d_v}^2 + {u_v * v_v} = {r_sq} \\implies R = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Verify {m(f'({ans} - {d_v})({ans} + {d_v}) = {ans - d_v} \\times {ans + d_v} = {u_v * v_v} = {u_v} \\times {v_v}')}!",
            idea_ar=f"بتمديد {m('OE')} ليصبح قطراً ينقسم إلى {m('R - d')} و{m('R + d')}، نطبّق تقاطع الأوتار فنجد {m('R^2 = d^2 + AE \\cdot EB')}.",
            steps_ar=[
                f"القطر المار بـ {m('O')} و{m('E')} جزآه {m(f'R - {d_v}')} و{m(f'R + {d_v}')}.",
                f"من تقاطع الأوتار: {m(f'R^2 - {d_v}^2 = {u_v} \\times {v_v} = {u_v * v_v}')}.",
                f"إذن {m(f'R^2 = {r_sq} \\implies R = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"التحقق: {m(f'({ans - d_v})({ans + d_v}) = {u_v * v_v}')}.",
            diagram_en=svg_circle_chords(str(u_v), str(v_v), f"R−{d_v}", f"R+{d_v}"),
        ))

    # 12. kang_jun_right_triangle_incircle (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_right_triangle_incircle"
    easy_inc = [
        (6, 8),
        (8, 15),
        (15, 20),
        (20, 21),
        (24, 32),
    ]
    for a_leg, b_leg in easy_inc:
        c_hyp = math.isqrt(a_leg * a_leg + b_leg * b_leg)
        assert c_hyp * c_hyp == a_leg * a_leg + b_leg * b_leg
        ans = (a_leg + b_leg - c_hyp) // 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"A right triangle on a Junior Kangaroo geometry sheet has perpendicular legs of lengths {m(f'{a_leg}\\text{{ cm}}')} and {m(f'{b_leg}\\text{{ cm}}')}. What is the radius of its inscribed circle in {m('\\text{cm}')}?",
            q_ar=f"مثلث قائم الزاوية في ورقة هندسة بمسابقة الكانجارو للناشئين طولا ساقيه المتعامدتين {m(f'{a_leg}\\text{{ cm}}')} و{m(f'{b_leg}\\text{{ cm}}')}. ما نصف قطر دائرته الداخلة بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[ans + 1, max(1, ans - 1), c_hyp // 2, ans + 2],
            hint_en=f"Compute hypotenuse {m('c')} via Pythagoras, then use {m('r = \\frac{a + b - c}{2}')}.",
            hint_ar=f"احسب الوتر {m('c')} بنظرية فيثاغورس ثم استعمل القانون {m('r = \\frac{a + b - c}{2}')}.",
            idea_en=f"In any right triangle, equal tangent segments give {m('r = \\frac{a + b - c}{2}')}.",
            steps_en=[
                f"Hypotenuse {m(f'c = \\sqrt{{{a_leg}^2 + {b_leg}^2}} = {c_hyp}\\text{{ cm}}')}.",
                f"Inradius {m(f'r = \\frac{{{a_leg} + {b_leg} - {c_hyp}}}{{2}} = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Area {m(f'\\frac{{1}}{{2}}({a_leg})({b_leg}) = {a_leg*b_leg//2}')} divided by semiperimeter {m(str((a_leg+b_leg+c_hyp)//2))} equals {m(str(ans))}.",
            idea_ar=f"في أي مثلث قائم الزاوية نصف قطر الدائرة الداخلة هو {m('r = \\frac{a + b - c}{2}')}.",
            steps_ar=[
                f"طول الوتر: {m(f'c = \\sqrt{{{a_leg}^2 + {b_leg}^2}} = {c_hyp}\\text{{ cm}}')}.",
                f"نصف القطر: {m(f'r = \\frac{{{a_leg} + {b_leg} - {c_hyp}}}{{2}} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"المساحة مقسومة على نصف المحيط تعطي {m(str(ans))} أيضاً.",
            diagram_en=svg_right_tri_incircle(str(a_leg), str(b_leg), str(c_hyp), "r = ?"),
        ))

    med_inc = [
        (2, 5),
        (4, 13),
        (6, 17),
        (6, 25),
        (6, 15),
    ]
    for r_in, R_circ in med_inc:
        ans = 2 * r_in + 4 * R_circ
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo right-triangle puzzle, a right triangle has inradius {m(f'r = {r_in}\\text{{ cm}}')} and circumradius {m(f'R = {R_circ}\\text{{ cm}}')}. What is the **perimeter** of the triangle in {m('\\text{cm}')}?",
            q_ar=f"في مسألة مثلث قائم بمسابقة الكانجارو للناشئين، نصف قطر الدائرة الداخلة لمثلث قائم هو {m(f'r = {r_in}\\text{{ cm}}')} ونصف قطر دائرته المحيطة {m(f'R = {R_circ}\\text{{ cm}}')}. ما **محيط** هذا المثلث بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[2 * r_in + 2 * R_circ, r_in + 2 * R_circ, 4 * r_in + 2 * R_circ, ans - 2 * r_in],
            hint_en=f"Use {m('c = 2R')} for the hypotenuse and {m('a + b = 2r + c')} from the inradius formula!",
            hint_ar=f"استعمل {m('c = 2R')} للوتر والعلاقة {m('a + b = 2r + c')} من قانون الدائرة الداخلة!",
            idea_en=f"Since {m('c = 2R')} and {m('a + b - c = 2r')}, perimeter {m('a + b + c = 2r + 2c = 2r + 4R')}!",
            steps_en=[
                f"In a right triangle, hypotenuse {m(f'c = 2R = {2 * R_circ}\\text{{ cm}}')}.",
                f"From {m('r = (a + b - c)/2')}, sum of legs is {m(f'a + b = 2r + c = {2 * r_in} + {2 * R_circ} = {2 * r_in + 2 * R_circ}\\text{{ cm}}')}.",
                f"Perimeter {m(f'= (a + b) + c = {2 * r_in + 2 * R_circ} + {2 * R_circ} = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Compact identity: {m(f'2({r_in}) + 4({R_circ}) = {ans}\\text{{ cm}}')}.",
            idea_ar=f"بما أن {m('c = 2R')} و{m('a + b = 2r + c')} فإن المحيط يساوي {m('2r + 4R')} دائماً.",
            steps_ar=[
                f"طول الوتر يساوي قطر الدائرة المحيطة: {m(f'c = 2R = {2 * R_circ}\\text{{ cm}}')}.",
                f"مجموع الساقين: {m(f'a + b = 2r + c = {2 * r_in + 2 * R_circ}\\text{{ cm}}')}.",
                f"المحيط الكلي {m(f'= {2 * r_in + 2 * R_circ} + {2 * R_circ} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"بتطبيق {m(f'2r + 4R = 2({r_in}) + 4({R_circ}) = {ans}\\text{{ cm}}')}.",
            diagram_en=svg_right_tri_incircle("a", "b", f"{2 * R_circ}", f"r={r_in}"),
        ))

    hard_inc = [
        (3, 10),
        (5, 12),
        (4, 21),
        (6, 20),
        (7, 30),
    ]
    for x_seg, y_seg in hard_inc:
        ans = x_seg * y_seg
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo geometry problem, the inscribed circle of right-angled {m('\\triangle ABC')} ({m('\\angle C = 90^\\circ')}) touches hypotenuse {m('AB')} at {m('T')}, dividing it into {m(f'AT = {x_seg}\\text{{ cm}}')} and {m(f'TB = {y_seg}\\text{{ cm}}')}. What is the **area** of {m('\\triangle ABC')} in {m('\\text{cm}^2')}?",
            q_ar=f"في مسألة هندسة من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، تمس الدائرة الداخلة للمثلث القائم {m('ABC')} (في {m('C')}) الوتر {m('AB')} عند النقطة {m('T')} فتقسمه إلى {m(f'AT = {x_seg}\\text{{ cm}}')} و{m(f'TB = {y_seg}\\text{{ cm}}')}. ما **مساحة** المثلث {m('ABC')} بوحدة {m('\\text{cm}^2')}؟",
            correct_val=ans,
            distractors=[(x_seg * y_seg) // 2 if (x_seg * y_seg) % 2 == 0 else x_seg * y_seg - x_seg, (x_seg + y_seg) * 2, ans + x_seg + y_seg, 2 * ans],
            hint_en=f"Write legs as {m(f'{x_seg} + r')} and {m(f'{y_seg} + r')} and expand Pythagoras {m(f'({x_seg} + r)^2 + ({y_seg} + r)^2 = ({x_seg} + {y_seg})^2')}!",
            hint_ar=f"اكتب الساقين {m(f'{x_seg} + r')} و{m(f'{y_seg} + r')} وطبّق فيثاغورس {m(f'({x_seg} + r)^2 + ({y_seg} + r)^2 = ({x_seg} + {y_seg})^2')}!",
            idea_en=f"In any right triangle, the incircle hypotenuse segments {m('x, y')} satisfy the magical Kangaroo identity {m('[\\triangle ABC] = x \\cdot y')}!",
            steps_en=[
                f"Equal tangents give legs {m(f'b = {x_seg} + r')}, {m(f'a = {y_seg} + r')}, and hypotenuse {m(f'c = {x_seg + y_seg}')}.",
                f"Expanding {m(f'({x_seg} + r)^2 + ({y_seg} + r)^2 = ({x_seg} + {y_seg})^2')} simplifies directly to {m(f'r({x_seg} + {y_seg} + r) = {x_seg} \\times {y_seg}')}.",
                f"Since semiperimeter {m(f's = {x_seg} + {y_seg} + r')}, area {m(f'= r \\cdot s = {x_seg} \\times {y_seg} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_en=f"Notice {m(f'\\frac{{1}}{{2}}({x_seg}+r)({y_seg}+r) = \\frac{{1}}{{2}}({x_seg*y_seg} + r({x_seg}+{y_seg}+r)) = \\frac{{1}}{{2}}({ans} + {ans}) = {ans}')}!",
            idea_ar=f"في أي مثلث قائم الزاوية، مساحته تساوي جداء جزأي الوتر المحددين بنقطة تماس الدائرة الداخلة {m('AT \\times TB')}!",
            steps_ar=[
                f"طولا الساقين من تساوي المماسات هما {m(f'{x_seg} + r')} و{m(f'{y_seg} + r')}، والوتر {m(f'{x_seg} + {y_seg}')}.",
                f"فك فيثاغورس يعطي {m(f'2r({x_seg} + {y_seg} + r) = 2({x_seg})({y_seg})')}.",
                f"وبما أن المساحة تساوي {m(f'r \\cdot s = r({x_seg} + {y_seg} + r)')} فإن المساحة {m(f'= {x_seg} \\times {y_seg} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_ar=f"التحقق الجبري المباشر: {m(f'\\frac{{1}}{{2}}({x_seg}+r)({y_seg}+r) = {ans}\\text{{ cm}}^2')}.",
            diagram_en=svg_right_tri_incircle(f"{x_seg}+r", f"{y_seg}+r", f"{x_seg}+{y_seg}", "r"),
        ))

    return items


def _unit_4_4_geometry_3d_coord(offset: int = 180) -> list[dict]:
    items: list[dict] = []
    topic = "Geometry"

    # 13. kang_jun_isosceles_trapezoid_pythag (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_isosceles_trapezoid_pythag"
    easy_trap = [
        (8, 20, 10),
        (10, 20, 13),
        (14, 30, 17),
        (9, 23, 25),
        (15, 33, 41),
    ]
    for a_top, b_bot, leg_l in easy_trap:
        wing = (b_bot - a_top) // 2
        ans = math.isqrt(leg_l * leg_l - wing * wing)
        assert ans * ans + wing * wing == leg_l * leg_l
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"An isosceles trapezoid on a Junior Kangaroo geometry worksheet has parallel bases of lengths {m(f'{a_top}\\text{{ cm}}')} and {m(f'{b_bot}\\text{{ cm}}')}, and each slanted leg has length {m(f'{leg_l}\\text{{ cm}}')}. What is the height of the trapezoid in {m('\\text{cm}')}?",
            q_ar=f"شبه منحرف متطابق الساقين في ورقة الكانجارو للناشئين طولا قاعدتيه المتوازيتين {m(f'{a_top}\\text{{ cm}}')} و{m(f'{b_bot}\\text{{ cm}}')} وطول كل ساق مائلة {m(f'{leg_l}\\text{{ cm}}')}. ما ارتفاع شبه المنحرف بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[leg_l - wing, ans + 2, max(2, ans - 2), wing * 2],
            hint_en=f"Drop both perpendiculars from the shorter base to split the overhang equally into two segments of length {m(f'({b_bot} - {a_top})/2 = {wing}')}.",
            hint_ar=f"أسقط عمودين من رأسي القاعدة الصغرى لتحصل على مثلثين قائمين قاعدة كل منهما {m(f'({b_bot} - {a_top})/2 = {wing}')}.",
            idea_en=f"Apply Pythagoras to the side right triangle with hypotenuse {m(str(leg_l))} and base {m(str(wing))}.",
            steps_en=[
                f"Horizontal wing length is {m(f'\\frac{{{b_bot} - {a_top}}}{{2}} = {wing}\\text{{ cm}}')}.",
                f"Height {m(f'h = \\sqrt{{{leg_l}^2 - {wing}^2}} = \\sqrt{{{leg_l*leg_l - wing*wing}}} = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Check {m(f'{wing}^2 + {ans}^2 = {wing*wing} + {ans*ans} = {leg_l*leg_l} = {leg_l}^2')}.",
            idea_ar=f"نطبق نظرية فيثاغورس على المثلث الجانبي القائم الذي وتره {m(str(leg_l))} وقاعدته {m(str(wing))}.",
            steps_ar=[
                f"قاعدة المثلث الجانبي: {m(f'\\frac{{{b_bot} - {a_top}}}{{2}} = {wing}\\text{{ cm}}')}.",
                f"الارتفاع: {m(f'h = \\sqrt{{{leg_l}^2 - {wing}^2}} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"{m(f'{wing}^2 + {ans}^2 = {leg_l}^2')}، صحيح.",
            diagram_en=svg_isosceles_trapezoid(str(a_top), str(b_bot), str(leg_l), "h = ?"),
        ))

    med_trap = [
        (5, 11, 6),
        (7, 17, 5),
        (9, 21, 8),
        (12, 28, 21),
        (16, 32, 7),
    ]
    for a_top, b_bot, h_val in med_trap:
        mid = (a_top + b_bot) // 2
        ans = math.isqrt(mid * mid + h_val * h_val)
        assert ans * ans == mid * mid + h_val * h_val
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo design problem, an isosceles trapezoid has parallel bases {m(f'{a_top}\\text{{ cm}}')} and {m(f'{b_bot}\\text{{ cm}}')} and perpendicular height {m(f'{h_val}\\text{{ cm}}')}. What is the length of each **diagonal** in {m('\\text{cm}')}?",
            q_ar=f"في مسألة تصميم بمسابقة الكانجارو للناشئين، شبه منحرف متطابق الساقين قاعدتاه المتوازيتان {m(f'{a_top}\\text{{ cm}}')} و{m(f'{b_bot}\\text{{ cm}}')} وارتفاعه العمودي {m(f'{h_val}\\text{{ cm}}')}. ما طول **قطره** بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[mid + h_val - 2, ans + 2, max(mid, ans - 2), b_bot],
            hint_en=f"The horizontal projection of a diagonal in an isosceles trapezoid equals {m(f'\\frac{{{a_top} + {b_bot}}}{{2}} = {mid}')}!",
            hint_ar=f"المسقط الأفقي للقطر في شبه المنحرف المتطابق الساقين يساوي متوسط القاعدتين {m(f'\\frac{{{a_top} + {b_bot}}}{{2}} = {mid}')}!",
            idea_en=f"Drop an altitude from a top vertex: the diagonal is the hypotenuse of a right triangle with legs {m('h')} and {m('(a + b)/2')}.",
            steps_en=[
                f"Horizontal span from one bottom corner to the opposite top altitude is {m(f'{a_top} + \\frac{{{b_bot} - {a_top}}}{{2}} = \\frac{{{a_top} + {b_bot}}}{{2}} = {mid}\\text{{ cm}}')}.",
                f"By Pythagoras, diagonal {m(f'd = \\sqrt{{{mid}^2 + {h_val}^2}} = \\sqrt{{{mid*mid + h_val*h_val}}} = {ans}\\text{{ cm}}')}.",
            ],
            check_en=f"Verify {m(f'{mid}^2 + {h_val}^2 = {mid*mid} + {h_val*h_val} = {ans*ans} = {ans}^2')}.",
            idea_ar=f"يشكّل القطر وتراً لمثلث قائم ضلعاه الارتفاع {m('h')} ومتوسط القاعدتين {m('(a + b)/2')}.",
            steps_ar=[
                f"المسقط الأفقي للقطر يساوي {m(f'\\frac{{{a_top} + {b_bot}}}{{2}} = {mid}\\text{{ cm}}')}.",
                f"طول القطر من فيثاغورس: {m(f'd = \\sqrt{{{mid}^2 + {h_val}^2}} = {ans}\\text{{ cm}}')}.",
            ],
            check_ar=f"{m(f'{mid}^2 + {h_val}^2 = {ans}^2')}، صحيح تماماً.",
            diagram_en=svg_isosceles_trapezoid(str(a_top), str(b_bot), "ℓ", f"h={h_val}"),
        ))

    hard_trap = [
        (4, 16),
        (9, 25),
        (8, 18),
        (16, 36),
        (18, 32),
    ]
    for a_top, b_bot in hard_trap:
        leg_l = (a_top + b_bot) // 2
        h_val = math.isqrt(a_top * b_bot)
        assert h_val * h_val == a_top * b_bot
        ans = leg_l * h_val
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo geometry problem, an isosceles trapezoid with parallel bases {m(f'{a_top}\\text{{ cm}}')} and {m(f'{b_bot}\\text{{ cm}}')} is circumscribed around a circle (tangent to all four sides). What is the **area** of the trapezoid in {m('\\text{cm}^2')}?",
            q_ar=f"في مسألة هندسة من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، شبه منحرف متطابق الساقين قاعدتاه المتوازيتان {m(f'{a_top}\\text{{ cm}}')} و{m(f'{b_bot}\\text{{ cm}}')} محيط بدائرة تمس أضلاعه الأربعة من الداخل. ما **مساحة** شبه المنحرف بوحدة {m('\\text{cm}^2')}؟",
            correct_val=ans,
            distractors=[leg_l * leg_l, a_top * b_bot, ans - h_val, (b_bot - a_top) * leg_l],
            hint_en=f"In any tangential quadrilateral, opposite sides have equal sums: {m(f'2\\ell = {a_top} + {b_bot}')}!",
            hint_ar=f"في أي رباعي يحيط بدائرة يتساوى مجموعا الضلعين المتقابلين: {m(f'2\\ell = {a_top} + {b_bot}')}!",
            idea_en=f"Tangency forces leg {m(f'\\ell = \\frac{{{a_top} + {b_bot}}}{{2}} = {leg_l}')}, and Pythagoras simplifies height cleanly to {m('h = \\sqrt{ab}')}!",
            steps_en=[
                f"Equal tangent segments give {m(f'\\ell + \\ell = {a_top} + {b_bot} \\implies \\ell = {leg_l}\\text{{ cm}}')}.",
                f"Wing base is {m(f'\\frac{{{b_bot} - {a_top}}}{{2}} = {(b_bot - a_top)//2}')}, so {m(f'h = \\sqrt{{{leg_l}^2 - {(b_bot - a_top)//2}^2}} = \\sqrt{{{a_top} \\times {b_bot}}} = {h_val}\\text{{ cm}}')}.",
                f"Area {m(f'= \\frac{{{a_top} + {b_bot}}}{{2}} \\times {h_val} = {leg_l} \\times {h_val} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_en=f"Algebraic check: {m('\\left(\\frac{a+b}{2}\\right)^2 - \\left(\\frac{b-a}{2}\\right)^2 = ab')}, confirming {m(f'h = {h_val}')}.",
            idea_ar=f"شرط التماس يعطي الساق {m(f'\\ell = {leg_l}')}، وفيثاغورس يعطي الارتفاع {m('h = \\sqrt{ab}')} مباشرة.",
            steps_ar=[
                f"من تساوي مجموع الضلعين المتقابلين: {m(f'2\\ell = {a_top} + {b_bot} \\implies \\ell = {leg_l}\\text{{ cm}}')}.",
                f"الارتفاع {m(f'h = \\sqrt{{{leg_l}^2 - {((b_bot - a_top)//2)}^2}} = \\sqrt{{{a_top * b_bot}}} = {h_val}\\text{{ cm}}')}.",
                f"المساحة {m(f'= {leg_l} \\times {h_val} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_ar=f"نصف قطر الدائرة المماسة هو {m(f'h/2 = {h_val}/2')} والمساحة {m(f'{ans}\\text{{ cm}}^2')}.",
            diagram_en=svg_isosceles_trapezoid(str(a_top), str(b_bot), str(leg_l), f"h={h_val}"),
        ))

    # 14. kang_jun_polyhedron_corner_cuts (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_polyhedron_corner_cuts"
    for k_cuts in (1, 3, 5, 6, 7):
        ans = 12 + 3 * k_cuts
        v_cnt = 8 + 2 * k_cuts
        f_cnt = 6 + k_cuts
        assert v_cnt - ans + f_cnt == 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo 3D sculpture, {m(str(k_cuts))} of the {m('8')} corners of a solid wooden cube are sliced off by small planes that do not meet one another. How many **edges** does the new solid have?",
            q_ar=f"في مجسم ثلاثي الأبعاد بمسابقة الكانجارو للناشئين، قُطعت {m(str(k_cuts))} زوايا من زوايا مكعب خشبي الثماني بمستويات صغيرة متباعدة لا تتقاطع. كم **حرفاً** للمجسم الجديد؟",
            correct_val=ans,
            distractors=[12 + 2 * k_cuts, v_cnt, 12 + 4 * k_cuts, ans - 3],
            hint_en=f"A cube starts with {m('12')} edges, and each small corner slice adds a triangular boundary of {m('3')} new edges without removing any old edge!",
            hint_ar=f"للمكعب الأصلي {m('12')} حرفاً، وكل قطع صغير لزاوية يضيف {m('3')} أحرف جديدة حول الوجه المثلث دون حذف أي حرف قديم!",
            idea_en=f"Each disjoint corner cut on a cube keeps all {m('12')} shortened original edges and adds {m('3')} new edges.",
            steps_en=[
                f"Start with {m('E_0 = 12')} cube edges.",
                f"Add {m('3')} new edges for each of the {m(str(k_cuts))} sliced corners: {m(f'E = 12 + 3({k_cuts}) = {ans}')}.",
            ],
            check_en=f"Euler check: {m(f'V = {v_cnt}, E = {ans}, F = {f_cnt}')} satisfies {m(f'{v_cnt} - {ans} + {f_cnt} = 2')}.",
            idea_ar=f"كل قطع صغير يضيف مثلثاً جديداً بـ {m('3')} أحرف مع بقاء الأحرف الـ {m('12')} الأصلية.",
            steps_ar=[
                f"عدد أحرف المكعب الأصلي {m('12')}.",
                f"بعد بتر {m(str(k_cuts))} زوايا يصبح عدد الأحرف {m(f'12 + 3 \\times {k_cuts} = {ans}')}.",
            ],
            check_ar=f"صيغة أويلر: {m(f'{v_cnt} - {ans} + {f_cnt} = 2')}.",
            diagram_en=svg_kang_cube_faces(f"F={f_cnt}", f"V={v_cnt}", "E = ?"),
        ))

    med_poly = [
        (2, 5, 5, 4, "pentagonal", "خماسية", "square", "مربعة"),
        (4, 3, 4, 6, "triangular", "مثلثة", "hexagonal", "سداسية"),
        (2, 8, 8, 4, "octagonal", "ثمانية", "square", "مربعة"),
        (6, 4, 8, 6, "square", "مربعة", "hexagonal", "سداسية"),
        (12, 5, 20, 6, "pentagonal", "خماسية", "hexagonal", "سداسية"),
    ]
    for f1, s1, f2, s2, n1_en, n1_ar, n2_en, n2_ar in med_poly:
        two_e = f1 * s1 + f2 * s2
        assert two_e % 2 == 0 and two_e % 3 == 0
        e_cnt = two_e // 2
        ans = two_e // 3
        f_cnt = f1 + f2
        assert ans - e_cnt + f_cnt == 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"A convex polyhedron in a Junior Kangaroo 3D puzzle has {m(str(f1))} {n1_en} faces and {m(str(f2))} {n2_en} faces, and exact {m('3')} edges meet at every vertex. How many **vertices** does this polyhedron have?",
            q_ar=f"مجسم محدب في لغز فراغي بمسابقة الكانجارو للناشئين له {m(str(f1))} أوجه {n1_ar} و{m(str(f2))} أوجه {n2_ar}، وتلتقي عند كل رأس {m('3')} أحرف بالضبط. كم **رأساً** لهذا المجسم؟",
            correct_val=ans,
            distractors=[e_cnt, f_cnt + 4, ans + 4, two_e // 4],
            hint_en=f"Sum all polygon sides to find {m('2E')}, or note that every vertex belongs to {m('3')} corners of faces so {m('3V = \\text{total polygon corners}')}!",
            hint_ar=f"مجموع زوايا المضلعات يساوي {m('3V')} لأن كل رأس تلتقي عنده {m('3')} أوجه بالضبط!",
            idea_en=f"Each face corner lands on a degree-3 vertex, so {m(f'3V = {f1}({s1}) + {f2}({s2}) = {two_e}')}.",
            steps_en=[
                f"Total polygon sides/corners across all faces is {m(f'{f1} \\times {s1} + {f2} \\times {s2} = {two_e}')}.",
                f"Thus {m(f'E = {two_e}/2 = {e_cnt}')} edges, and since {m('3')} edges meet per vertex, {m(f'V = {two_e}/3 = {ans}')} vertices.",
            ],
            check_en=f"Euler's formula confirms {m(f'V - E + F = {ans} - {e_cnt} + {f_cnt} = 2')}!",
            idea_ar=f"كل رأس يجمع {m('3')} زوايا من الأوجه، إذن {m(f'3V = {two_e}')}.",
            steps_ar=[
                f"مجموع أضلاع الأوجه: {m(f'{f1} \\times {s1} + {f2} \\times {s2} = {two_e}')}، ومنه {m(f'E = {e_cnt}')}.",
                f"بما أن درجة كل رأس {m('3')} فإن {m(f'V = {two_e} \\div 3 = {ans}')} رأساً.",
            ],
            check_ar=f"صيغة أويلر: {m(f'{ans} - {e_cnt} + {f_cnt} = 2')} متحققة تماماً.",
            diagram_en=svg_kang_cube_faces(f"F={f_cnt}", "V = ?", f"E={e_cnt}"),
        ))

    hard_poly = [
        ("regular tetrahedron", "رباعي أوجه منتظم", 4, 6, 4),
        ("solid cube", "مكعب مصمت", 8, 12, 6),
        ("triangular prism", "منشور ثلاثي", 6, 9, 5),
        ("square-based pyramid", "هرم رباعي القاعدة", 5, 8, 5),
        ("pentagonal prism", "منشور خماسي", 10, 15, 7),
    ]
    for sh_en, sh_ar, v0, e0, f0 in hard_poly:
        v_new, e_new, f_new = e0, 2 * e0, f0 + v0
        assert v_new - e_new + f_new == 2
        ans = v_new + e_new + f_new
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo truncation challenge, every corner of a {sh_en} ({m(f'V={v0}, E={e0}, F={f0}')}) is sliced off by planes passing **exact through the midpoints** of all edges meeting at that corner. What is {m('V + E + F')} for the resulting solid?",
            q_ar=f"في تحدٍّ من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، بُترت جميع رؤوس {sh_ar} ({m(f'V={v0}, E={e0}, F={f0}')}) بمستويات تمرّ **تماماً بنقاط منتصف** جميع الأحرف المتلاقية عند كل رأس. ما قيمة {m('V + E + F')} للمجسم الناتج؟",
            correct_val=ans,
            distractors=[ans + v0, ans - e0, (v0 + 2 * v0) + (e0 + 3 * v0) + (f0 + v0), ans + 4],
            hint_en=f"Unlike tiny corner cuts, cuts meeting at **edge midpoints** merge into single vertices — one new vertex on each of the {m(str(e0))} original edges!",
            hint_ar=f"على عكس القطوع الصغيرة، تلتقي القطوع هنا عند **منتصفات الأحرف** فيصبح منتصف كل حرف أصلي رأساً واحداً فقط للمجسم الجديد!",
            idea_en=f"Midpoint rectification gives {m('V_{\\text{new}} = E_0')}, {m('E_{\\text{new}} = 2E_0')}, and {m('F_{\\text{new}} = F_0 + V_0')}.",
            steps_en=[
                f"The {m(str(e0))} edge midpoints are the only vertices left: {m(f'V = {v_new}')}.",
                f"Original edges vanish, and each old corner's cut polygon contributes edges summing to {m(f'2E_0 = {e_new}')}.",
                f"Faces equal the {m(str(f0))} shrunk original faces plus {m(str(v0))} new corner faces: {m(f'F = {f_new}')}, so {m(f'V + E + F = {v_new} + {e_new} + {f_new} = {ans}')}.",
            ],
            check_en=f"Euler check: {m(f'{v_new} - {e_new} + {f_new} = 2')}!",
            idea_ar=f"عند البتر حتى منتصفات الأحرف: {m('V = E_0')} و{m('E = 2E_0')} و{m('F = F_0 + V_0')}.",
            steps_ar=[
                f"نقاط المنتصف الـ {m(str(e0))} تصبح هي الرؤوس الجديدة: {m(f'V = {v_new}')}.",
                f"عدد الأحرف الجديدة يساوي مجموع درجات الرؤوس الأصلية {m(f'2E_0 = {e_new}')}، والأوجه {m(f'F_0 + V_0 = {f_new}')}.",
                f"المجموع {m(f'V + E + F = {v_new} + {e_new} + {f_new} = {ans}')}.",
            ],
            check_ar=f"التحقق بصيغة أويلر: {m(f'{v_new} - {e_new} + {f_new} = 2')}.",
            diagram_en=svg_kang_cube_faces(f"F={f_new}", f"V={v_new}", f"E={e_new}"),
        ))

    # 15. kang_jun_cube_in_cylinder_prism (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_cube_in_cylinder_prism"
    for s_edge in (4, 8, 10, 12, 14):
        ans = (s_edge ** 3) // 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"A cube of edge length {m(f'{s_edge}\\text{{ cm}}')} fits snugly inside a right circular cylinder of height {m(f'{s_edge}\\text{{ cm}}')} on a Junior Kangaroo exam so all {m('8')} vertices lie on the cylinder's circular rims. If the cylinder's volume is {m('K\\pi\\text{ cm}^3')}, what is {m('K')}?",
            q_ar=f"مكعب طول حرفه {m(f'{s_edge}\\text{{ cm}}')} موضوع داخل أسطوانة دائرية قائمة ارتفاعها {m(f'{s_edge}\\text{{ cm}}')} في اختبار الكانجارو للناشئين بحيث تقع رؤوسه الثمانية على محيطي القاعدتين. إذا كان حجم الأسطوانة {m('K\\pi\\text{ cm}^3')}، فما قيمة {m('K')}؟",
            correct_val=ans,
            distractors=[(s_edge ** 3) // 4, s_edge ** 3, ans + s_edge * s_edge, 2 * ans],
            hint_en=f"The diameter of the cylinder's circular base equals the face diagonal {m(f'{s_edge}\\sqrt{{2}}')} of the cube.",
            hint_ar=f"قطر قاعدة الأسطوانة الدائرية يساوي قطر وجه المكعب {m(f'{s_edge}\\sqrt{{2}}')}.",
            idea_en=f"From {m(f'2r = {s_edge}\\sqrt{{2}}')}, {m(f'r^2 = {s_edge*s_edge // 2}')}, and {m('V = \\pi r^2 h')}.",
            steps_en=[
                f"Cylinder radius satisfies {m(f'r = \\frac{{{s_edge}\\sqrt{{2}}}}{{2}} \\implies r^2 = \\frac{{{s_edge}^2}}{{2}} = {s_edge*s_edge//2}\\text{{ cm}}^2')}.",
                f"Volume {m(f'= \\pi r^2 h = \\pi({s_edge*s_edge//2})({s_edge}) = {ans}\\pi\\text{{ cm}}^3')}, so {m(f'K = {ans}')}.",
            ],
            check_en=f"Inscribed cylinder would give {m(str((s_edge**3)//4))}; circumscribed cylinder is twice that ({m(str(ans))}).",
            idea_ar=f"مربع نصف القطر هو {m(f'r^2 = {s_edge}^2 / 2 = {s_edge*s_edge//2}')} والحجم {m('\\pi r^2 h')}.",
            steps_ar=[
                f"من {m(f'2r = {s_edge}\\sqrt{{2}}')} نجد {m(f'r^2 = {s_edge*s_edge//2}\\text{{ cm}}^2')}.",
                f"الحجم {m(f'= {s_edge*s_edge//2} \\times {s_edge}\\pi = {ans}\\pi\\text{{ cm}}^3')}، إذن {m(f'K = {ans}')}.",
            ],
            check_ar=f"حجم الأسطوانة المحيطة يساوي ضعف حجم الأسطوانة الداخلة.",
            diagram_en=svg_cube_in_cylinder(f"{s_edge} cm"),
        ))

    for R_sph in (3, 4, 5, 6, 7):
        ans = 8 * R_sph * R_sph
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo 3D geometry problem, a cube is inscribed inside a sphere of radius {m(f'{R_sph}\\text{{ cm}}')} so all {m('8')} vertices touch the sphere. What is the **total surface area** of the cube in {m('\\text{cm}^2')}?",
            q_ar=f"في مسألة هندسة فراغية بمسابقة الكانجارو للناشئين، وُضع مكعب داخل كرة نصف قطرها {m(f'{R_sph}\\text{{ cm}}')} بحيث تقع رؤوسه الثمانية على سطح الكرة. ما **المساحة الكلية لسطح** المكعب بوحدة {m('\\text{cm}^2')}؟",
            correct_val=ans,
            distractors=[6 * R_sph * R_sph, 12 * R_sph * R_sph, 4 * R_sph * R_sph, 24 * R_sph * R_sph],
            hint_en=f"The space diagonal of the cube equals the sphere's diameter {m(f'2R = {2 * R_sph}')}, so {m(f'3s^2 = (2R)^2')}!",
            hint_ar=f"القطر الفراغي للمكعب يساوي قطر الكرة {m(f'2R = {2 * R_sph}')}، أي {m('3s^2 = 4R^2')}!",
            idea_en=f"You don't need {m('s')} itself — from {m('3s^2 = 4R^2')}, multiply directly by {m('2')} to get {m('6s^2 = 8R^2')}!",
            steps_en=[
                f"By 3D Pythagoras, space diagonal squared is {m(f'3s^2 = (2 \\times {R_sph})^2 = {4 * R_sph * R_sph}')}.",
                f"Multiply both sides by {m('2')}: surface area {m(f'6s^2 = 2 \\times {4 * R_sph * R_sph} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_en=f"Notice {m(f'{ans} < 4\\pi R^2 \\approx {round(4 * math.pi * R_sph * R_sph, 1)}')}, matching a cube inside the sphere.",
            idea_ar=f"من العلاقة {m('3s^2 = 4R^2')} نضرب الطرفين في {m('2')} فنحصل فوراً على المساحة السطحية {m('6s^2 = 8R^2')}!",
            steps_ar=[
                f"مربع القطر الفراغي للمكعب: {m(f'3s^2 = (2R)^2 = {4 * R_sph * R_sph}')}.",
                f"مساحة الأوجه الستة: {m(f'6s^2 = 2 \\times {4 * R_sph * R_sph} = {ans}\\text{{ cm}}^2')}.",
            ],
            check_ar=f"المساحة السطحية للمكعب المحاط بكرة تساوي {m(f'8({R_sph})^2 = {ans}\\text{{ cm}}^2')}.",
            diagram_en=svg_kang_cube_faces("s²", "s²", f"2R={2 * R_sph}"),
        ))

    hard_tank = [
        (12, 9, 2, 6),
        (10, 10, 3, 5),
        (16, 10, 3, 8),
        (20, 15, 4, 10),
        (25, 16, 6, 10),
    ]
    for L_t, W_t, h0, s_c in hard_tank:
        base_a = L_t * W_t
        vol_w = base_a * h0
        collar = base_a - s_c * s_c
        assert s_c < W_t and vol_w % collar == 0
        ans = vol_w // collar
        assert ans < s_c
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo water-level problem, an open rectangular tank with horizontal base {m(f'{L_t}\\text{{ cm}} \\times {W_t}\\text{{ cm}}')} holds water to a depth of {m(f'{h0}\\text{{ cm}}')}. A heavy solid iron cube of edge {m(f'{s_c}\\text{{ cm}}')} is set flat on the bottom of the tank. What is the new water depth in {m('\\text{cm}')}?",
            q_ar=f"في مسألة منسوب مياه من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، خزان مستطيل مفتوح قاعدته الأفقية {m(f'{L_t}\\text{{ cm}} \\times {W_t}\\text{{ cm}}')} يحتوي ماءً بارتفاع {m(f'{h0}\\text{{ cm}}')}. وُضع مكعب حديدي مصمت طول حرفه {m(f'{s_c}\\text{{ cm}}')} مستوياً على قاع الخزان. ما الارتفاع الجديد للماء بوحدة {m('\\text{cm}')}؟",
            correct_val=ans,
            distractors=[ans + 1, h0 + (s_c ** 3) // base_a if (s_c ** 3) // base_a != ans - h0 else ans + 2, s_c, ans - 1],
            hint_en=f"Test whether the water reaches the top of the {m(f'{s_c}\\text{{ cm}}')} cube! Below height {m(str(s_c))}, water fills only the collar area {m(f'{base_a} - {s_c}^2 = {collar}\\text{{ cm}}^2')}.",
            hint_ar=f"تحقق مما إذا كان الماء يغمر المكعب أم لا! تحت ارتفاع {m(str(s_c))} يتوزع الماء في المساحة الحرة حول المكعب {m(f'{base_a} - {s_c}^2 = {collar}\\text{{ cm}}^2')}.",
            idea_en=f"Water volume {m(f'{vol_w}\\text{{ cm}}^3')} spreads over the unobstructed floor area {m(f'{base_a} - {s_c*s_c} = {collar}\\text{{ cm}}^2')}, rising to {m(f'{ans} < {s_c}\\text{{ cm}}')}.",
            steps_en=[
                f"Water volume is {m(f'V_w = {L_t} \\times {W_t} \\times {h0} = {vol_w}\\text{{ cm}}^3')}.",
                f"With the iron cube standing on the floor, available horizontal cross-section is {m(f'{base_a} - {s_c}^2 = {collar}\\text{{ cm}}^2')}.",
                f"Tentative depth {m(f'h = \\frac{{{vol_w}}}{{{collar}}} = {ans}\\text{{ cm}}')}; since {m(f'{ans} < {s_c}')}, the cube indeed stays partially above water!",
            ],
            check_en=f"Submerged cube volume is {m(f'{s_c}^2 \\times {ans} = {s_c*s_c*ans}')}, and {m(f'{vol_w} + {s_c*s_c*ans} = {base_a} \\times {ans}')}!",
            idea_ar=f"يتوزع حجم الماء {m(f'{vol_w}\\text{{ cm}}^3')} على المساحة المتبقية حول المكعب {m(f'{collar}\\text{{ cm}}^2')} ويبقى المنسوب أقل من ارتفاع المكعب.",
            steps_ar=[
                f"حجم الماء الثابت: {m(f'{L_t} \\times {W_t} \\times {h0} = {vol_w}\\text{{ cm}}^3')}.",
                f"مساحة القاع المتاحة حول المكعب: {m(f'{base_a} - {s_c}^2 = {collar}\\text{{ cm}}^2')}.",
                f"الارتفاع الجديد {m(f'= {vol_w} \\div {collar} = {ans}\\text{{ cm}}')}، وبما أن {m(f'{ans} < {s_c}')} فالمكعب غير مغمور كلياً والحل دقيق.",
            ],
            check_ar=f"مجموع حجم الماء والجزء المغمور من المكعب {m(f'{vol_w} + {s_c*s_c*ans} = {base_a * ans} = {base_a} \\times {ans}')}.",
            diagram_en=svg_water_tank_3d(f"{L_t} cm", f"{W_t} cm", f"h₀={h0}", 0.45),
        ))

    # 16. kang_jun_manhattan_diamond_area (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_manhattan_diamond_area"
    for R_d, h_x, k_y in [(4, 1, -3), (5, -2, 4), (6, 5, -1), (8, -4, 2), (9, 3, 6)]:
        ans = 2 * R_d * R_d
        sx = f"x - {h_x}" if h_x > 0 else f"x + {-h_x}"
        sy = f"y - {k_y}" if k_y > 0 else f"y + {-k_y}"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On the coordinate plane in a Junior Kangaroo question, what is the area of the region defined by {m(f'|{sx}| + |{sy}| \\le {R_d}')}?",
            q_ar=f"في المستوى الإحداثي ضمن سؤال بمسابقة الكانجارو للناشئين، ما مساحة المنطقة المحددة بالمتباينة {m(f'|{sx}| + |{sy}| \\le {R_d}')}؟",
            correct_val=ans,
            distractors=[R_d * R_d, 4 * R_d * R_d, ans - 2 * R_d, ans + 2 * R_d],
            hint_en=f"Shift the center to {m('(0, 0)')}: the tilted square has perpendicular diagonals both of length {m(f'2 \\times {R_d} = {2 * R_d}')}.",
            hint_ar=f"أزح المركز إلى {m('(0, 0)')}؛ المنطقة معين متعامد القطرين طول كل قطر فيه {m(f'2 \\times {R_d} = {2 * R_d}')}.",
            idea_en=f"A Manhattan diamond of radius {m('R')} has area {m('\\frac{1}{2}(2R)(2R) = 2R^2')}.",
            steps_en=[
                f"Shifting center {m(f'({h_x}, {k_y})')} to the origin preserves area.",
                f"Diagonals have lengths {m(str(2 * R_d))} and {m(str(2 * R_d))}, giving area {m(f'\\frac{{1}}{{2}}({2*R_d})({2*R_d}) = {ans}')}.",
            ],
            check_en=f"Each side has length {m(f'{R_d}\\sqrt{{2}}')}, and {m(f'({R_d}\\sqrt{{2}})^2 = {ans}')}.",
            idea_ar=f"مساحة المعين الإحداثي نصف قطره {m('R')} تساوي {m('2R^2')} دائماً.",
            steps_ar=[
                f"الإزاحة لا تغير المساحة، وطول كل قطر يساوي {m(str(2 * R_d))}.",
                f"المساحة {m(f'= \\frac{{1}}{{2}} \\times {2*R_d} \\times {2*R_d} = {ans}')}.",
            ],
            check_ar=f"طول ضلع المربع المائل {m(f'{R_d}\\sqrt{{2}}')} ومربعه {m(str(ans))}.",
            diagram_en=svg_coord_diamond(str(R_d)),
        ))

    med_diam = [
        (2, 3, 12),
        (3, 5, 15),
        (2, 5, 20),
        (3, 4, 24),
        (4, 5, 40),
    ]
    for p_c, q_c, C_lim in med_diam:
        a_int, b_int = C_lim // p_c, C_lim // q_c
        ans = 2 * a_int * b_int
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo coordinate-geometry problem, what is the area enclosed by the graph of {m(f'{p_c}|x| + {q_c}|y| \\le {C_lim}')}?",
            q_ar=f"في مسألة هندسة إحداثية بمسابقة الكانجارو للناشئين، ما مساحة المنطقة المحصورة بالمتباينة {m(f'{p_c}|x| + {q_c}|y| \\le {C_lim}')}؟",
            correct_val=ans,
            distractors=[a_int * b_int, 4 * a_int * b_int, (a_int + b_int) * 2, ans + a_int],
            hint_en=f"Find the four axis intercepts {m(f'(\\pm {a_int}, 0)')} and {m(f'(0, \\pm {b_int})')} to get the rhombus diagonals!",
            hint_ar=f"أوجد نقاط التقاطع الأربع مع المحورين {m(f'(\\pm {a_int}, 0)')} و{m(f'(0, \\pm {b_int})')} لمعرفة طولي قطري المعين!",
            idea_en=f"The boundary is a rhombus with horizontal diagonal {m(str(2 * a_int))} and vertical diagonal {m(str(2 * b_int))}.",
            steps_en=[
                f"Setting {m('y = 0')} gives {m(f'x = \\pm {a_int}')}; setting {m('x = 0')} gives {m(f'y = \\pm {b_int}')}.",
                f"Rhombus area {m(f'= \\frac{{1}}{{2}}({2 * a_int})({2 * b_int}) = 2 \\times {a_int} \\times {b_int} = {ans}')}.",
            ],
            check_en=f"First-quadrant right triangle has area {m(f'\\frac{{1}}{{2}}({a_int})({b_int}) = {Fraction(a_int * b_int, 2)}')}; multiplying by {m('4')} quadrants gives {m(str(ans))}.",
            idea_ar=f"يمثل الشكل معيناً قطراه على المحورين بطولين {m(str(2 * a_int))} و{m(str(2 * b_int))}.",
            steps_ar=[
                f"المقطعان السينيان {m(f'\\pm {a_int}')} والصاديان {m(f'\\pm {b_int}')}.",
                f"مساحة المعين {m(f'= \\frac{{1}}{{2}}({2 * a_int})({2 * b_int}) = {ans}')}.",
            ],
            check_ar=f"أربعة مثلثات قائمة متطابقة مجموع مساحاتها {m(str(ans))}.",
            diagram_en=svg_coord_diamond(f"{a_int},{b_int}"),
        ))

    for R_lat in (3, 4, 5, 6, 7):
        ans = sum(1 for xv in range(-R_lat, R_lat + 1) for yv in range(-R_lat, R_lat + 1) if abs(xv) + abs(yv) <= R_lat)
        assert ans == R_lat * R_lat + (R_lat + 1) ** 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo lattice problem, how many ordered pairs of **integers** {m('(x, y)')} satisfy {m(f'|x - 2| + |y + 5| \\le {R_lat}')}?",
            q_ar=f"في مسألة نقاط شبكية من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، كم زوجاً مرتباً من **الأعداد الصحيحة** {m('(x, y)')} يحقق المتباينة {m(f'|x - 2| + |y + 5| \\le {R_lat}')}؟",
            correct_val=ans,
            distractors=[2 * R_lat * R_lat, (2 * R_lat + 1) ** 2, ans - 4, ans + 4],
            hint_en=f"Shift {m('(2, -5)')} to {m('(0, 0)')} and sum horizontal row counts {m('1 + 3 + \\dots + (2R+1) + \\dots + 3 + 1 = (R+1)^2 + R^2')}!",
            hint_ar=f"أزح المركز إلى نقطة الأصل واجمع عدد النقاط الصحيحة في الصفوف الأفقية لتحصل على {m('(R+1)^2 + R^2')}!",
            idea_en=f"Integer shifts preserve lattice counts; {m('|u| + |v| \\le R')} contains {m('R^2 + (R + 1)^2 = 2R^2 + 2R + 1')} integer points.",
            steps_en=[
                f"Let {m('u = x - 2')} and {m('v = y + 5')}, which remain integers with {m(f'|u| + |v| \\le {R_lat}')}.",
                f"Row {m('v = 0')} has {m(str(2 * R_lat + 1))} points, and pairs of rows {m('v = \\pm k')} add two odd-sum staircases: total {m(f'({R_lat} + 1)^2 + {R_lat}^2 = {(R_lat+1)**2} + {R_lat*R_lat} = {ans}')}.",
            ],
            check_en=f"Pick's Theorem check: area {m(str(2 * R_lat * R_lat))} equals {m('I + B/2 - 1')} with {m(f'B = {4 * R_lat}')}, giving {m(f'I + B = {2 * R_lat * R_lat + 2 * R_lat + 1} = {ans}')}!",
            idea_ar=f"الإزاحة بعدد صحيح لا تغير عدد النقاط الشبكية، وعدد الحلول هو {m('R^2 + (R + 1)^2')}.",
            steps_ar=[
                f"بوضع {m('u = x - 2')} و{m('v = y + 5')} تؤول المتباينة إلى {m(f'|u| + |v| \\le {R_lat}')}.",
                f"عدد النقاط الصحيحة يساوي مجموع مربعين متتاليين: {m(f'{R_lat}^2 + ({R_lat} + 1)^2 = {ans}')}.",
            ],
            check_ar=f"التحقق بمبرهنة بيك يعطي {m(f'2({R_lat})^2 + 2({R_lat}) + 1 = {ans}')} نقطة بالضبط.",
            diagram_en=svg_coord_diamond(str(R_lat)),
        ))

    return items


def _unit_4_5_combinatorics(offset: int = 240) -> list[dict]:
    import itertools
    items: list[dict] = []
    topic = "Combinatorics & Logic"

    # 17. kang_jun_digit_slot_restrictions (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_digit_slot_restrictions"
    easy_dig = [
        (3, 4),
        (3, 5),
        (3, 6),
        (4, 4),
        (4, 5),
    ]
    for k_len, d_max in easy_dig:
        digits = list(range(d_max + 1))
        ans = sum(1 for p in itertools.permutations(digits, k_len) if p[0] != 0 and p[-1] % 2 == 1)
        odd_cnt = sum(1 for d in digits if d % 2 == 1)
        lead_cnt = d_max - 1
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"For a Junior Kangaroo badge number, how many {m(str(k_len))}-digit **odd** positive integers can be formed from {m('\\{0, 1, \\dots, ' + str(d_max) + '\\}')} without repeating any digit?",
            q_ar=f"لتكوين رقم بطاقة في مسابقة الكانجارو للناشئين، كم عدداً صحيحاً موجباً **فردياً** مكوناً من {m(str(k_len))} أرقام يمكن تكوينه من المجموعة {m('\\{0, 1, \\dots, ' + str(d_max) + '\\}')} دون تكرار أي رقم؟",
            correct_val=ans,
            distractors=[odd_cnt * d_max * (d_max - 1), ans + odd_cnt * (d_max - 1), max(6, ans - 12), ans + 12],
            hint_en=f"Fill the units digit first ({m(str(odd_cnt))} odd choices), then the leading digit (cannot be {m('0')} or the units digit: {m(str(lead_cnt))} choices)!",
            hint_ar=f"ابدأ بخانة الآحاد ({m(str(odd_cnt))} خيارات فردية)، ثم الخانة اليسرى (تستبعد {m('0')} ورقم الآحاد: {m(str(lead_cnt))} خيارات)!",
            idea_en=f"Odd units digits never use {m('0')}, so no case split is needed: fill units first, then leading slot, then middle slots.",
            steps_en=[
                f"Units slot has {m(str(odd_cnt))} odd choices; leading slot has {m(f'{d_max + 1} - 2 = {lead_cnt}')} choices (excluding {m('0')} and units).",
                f"Fill the remaining {m(str(k_len - 2))} slot(s) from the unused digits to obtain {m(str(ans))}.",
            ],
            check_en=f"Exact enumeration of all valid {m(str(k_len))}-digit permutations confirms {m(str(ans))}.",
            idea_ar=f"بما أن الآحاد فردي فلا يتقاطع مع الصفر؛ نملأ الآحاد ثم الخانة الكبرى ثم الباقي.",
            steps_ar=[
                f"خانة الآحاد لها {m(str(odd_cnt))} خيارات، والخانة اليسرى لها {m(str(lead_cnt))} خيارات بعد استبعاد الصفر والآحاد.",
                f"بضرب خيارات الخانات المتبقية نحصل على {m(str(ans))} عدداً.",
            ],
            check_ar=f"العدّ المباشر يؤكد وجود {m(str(ans))} عدداً فردياً بلا تكرار.",
            diagram_en=svg_digit_slots([str(lead_cnt)] + ["Free"] * (k_len - 2) + [f"{odd_cnt} odd"], f"{k_len}-digit odd"),
        ))

    med_dig = [
        (3, 4, 2, "even", "زوجياً"),
        (3, 6, 2, "even", "زوجياً"),
        (4, 5, 5, "divisible by 5", "يقبل القسمة على 5"),
        (4, 6, 5, "divisible by 5", "يقبل القسمة على 5"),
        (4, 6, 2, "even", "زوجياً"),
    ]
    for k_len, d_max, div_m, cond_en, cond_ar in med_dig:
        digits = list(range(d_max + 1))
        c0 = sum(1 for p in itertools.permutations(digits, k_len) if p[0] != 0 and p[-1] == 0)
        cnz = sum(1 for p in itertools.permutations(digits, k_len) if p[0] != 0 and p[-1] != 0 and p[-1] % div_m == 0)
        ans = c0 + cnz
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo combinatorics round, how many {m(str(k_len))}-digit positive integers **{cond_en}** can be formed from {m('\\{0, 1, \\dots, ' + str(d_max) + '\\}')} without repeating any digit?",
            q_ar=f"في جولة توافيق بمسابقة الكانجارو للناشئين، كم عدداً صحيحاً موجباً مكوناً من {m(str(k_len))} أرقام **{cond_ar}** يمكن تكوينه من المجموعة {m('\\{0, 1, \\dots, ' + str(d_max) + '\\}')} دون تكرار أي رقم؟",
            correct_val=ans,
            distractors=[ans - c0 // 2, ans + 20, ans - 12, c0 * 2 + 10],
            hint_en=f"Split into **Case 1 (units = 0)** and **Case 2 (nonzero valid units digit)** so the leading-zero rule stays exact!",
            hint_ar=f"افصل العدّ إلى **حالة الآحاد = 0** و**حالة الآحاد غير الصفري** لضبط قيد عدم وقوع الصفر في اليسار!",
            idea_en=f"Add disjoint counts for units digit {m('= 0')} ({m(str(c0))}) and nonzero valid units digits ({m(str(cnz))}).",
            steps_en=[
                f"**Case 1 (units = 0):** {m(str(c0))} valid integers since any remaining digit can lead.",
                f"**Case 2 (units ≠ 0, multiple of {div_m}):** leading slot excludes both {m('0')} and units, giving {m(str(cnz))} integers.",
                f"Total {m(f'= {c0} + {cnz} = {ans}')}.",
            ],
            check_en=f"Disjoint case sum {m(f'{c0} + {cnz} = {ans}')} matches full permutation filtering.",
            idea_ar=f"نجمع حالتي الآحاد الصفري ({m(str(c0))}) والآحاد غير الصفري ({m(str(cnz))}).",
            steps_ar=[
                f"**الحالة ١ (الآحاد = 0):** تعطي {m(str(c0))} عدداً.",
                f"**الحالة ٢ (الآحاد ≠ 0):** بعد استبعاد الصفر والآحاد من اليسار نحصل على {m(str(cnz))} عدداً.",
                f"المجموع الكلي {m(f'= {c0} + {cnz} = {ans}')}.",
            ],
            check_ar=f"مجموع الحالتين المتنافيتين {m(str(ans))} بالضبط.",
            diagram_en=svg_digit_slots(["≠ 0"] + ["Free"] * (k_len - 2) + [f"÷{div_m}"], f"{c0} + {cnz} = {ans}"),
        ))

    hard_dig = [
        (0, 5, 3000),
        (0, 5, 4000),
        (0, 6, 4000),
        (0, 6, 5000),
        (1, 7, 5000),
    ]
    for d_min, d_max, thresh in hard_dig:
        digits = list(range(d_min, d_max + 1))
        ans = sum(
            1 for p in itertools.permutations(digits, 4)
            if p[0] != 0 and p[-1] % 2 == 0 and (1000 * p[0] + 100 * p[1] + 10 * p[2] + p[3]) > thresh
        )
        lead_min = thresh // 1000
        c_odd_lead = sum(1 for p in itertools.permutations(digits, 4) if p[0] >= lead_min and p[0] % 2 == 1 and p[-1] % 2 == 0)
        c_even_lead = sum(1 for p in itertools.permutations(digits, 4) if p[0] >= lead_min and p[0] % 2 == 0 and p[-1] % 2 == 0)
        assert ans == c_odd_lead + c_even_lead
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo code problem, how many {m('4')}-digit **even** integers **greater than {m(str(thresh))}** can be formed using distinct digits from {m('\\{' + ', '.join(str(d) for d in digits) + '\\}')}?",
            q_ar=f"في مسألة شفرات من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، كم عدداً صحيحاً **زوجياً** مكوناً من {m('4')} أرقام مختلفة **وأكبر من {m(str(thresh))}** يمكن تكوينه من المجموعة {m('\\{' + ', '.join(str(d) for d in digits) + '\\}')}؟",
            correct_val=ans,
            distractors=[ans + 24, max(12, ans - 24), ans + 12, ans - 12],
            hint_en=f"Split by the parity of the thousands digit ({m(f'\\ge {lead_min}')}): an **even** thousands digit uses up one even choice needed by the units slot!",
            hint_ar=f"افصل الحالات حسب زوجية خانة الآلاف ({m(f'\\ge {lead_min}')})؛ لأن اختيار رقم زوجي في الآلاف ينقص خيارات الآحاد الزوجية بواحد!",
            idea_en=f"Thousands digit must be {m(f'\\ge {lead_min}')}; split into odd thousands digits ({m(str(c_odd_lead))}) vs even thousands digits ({m(str(c_even_lead))}).",
            steps_en=[
                f"**Case 1 (odd thousands digit {m(f'\\ge {lead_min}')}):** all even digits remain available for units, giving {m(str(c_odd_lead))} numbers.",
                f"**Case 2 (even thousands digit {m(f'\\ge {lead_min}')}):** one fewer even digit remains for units, giving {m(str(c_even_lead))} numbers.",
                f"Add both cases: {m(f'{c_odd_lead} + {c_even_lead} = {ans}')}.",
            ],
            check_en=f"Every valid 4-digit distinct-digit number with thousands {m(f'\\ge {lead_min}')} exceeds {m(str(thresh))}, confirming {m(str(ans))}.",
            idea_ar=f"خانة الآلاف تحقق {m(f'\\ge {lead_min}')}؛ نفصل بين الآلاف الفردية ({m(str(c_odd_lead))}) والآلاف الزوجية ({m(str(c_even_lead))}).",
            steps_ar=[
                f"**الحالة ١ (خانة الآلاف فردية):** تبقى جميع الأرقام الزوجية متاحة للآحاد فتعطي {m(str(c_odd_lead))} عدداً.",
                f"**الحالة ٢ (خانة الآلاف زوجية):** ينقص عدد الخيارات الزوجية للآحاد بواحد فتعطي {m(str(c_even_lead))} عدداً.",
                f"المجموع الكلي {m(f'= {c_odd_lead} + {c_even_lead} = {ans}')}.",
            ],
            check_ar=f"مجموع الحالتين يعطي {m(str(ans))} عدداً زوجياً أكبر من {m(str(thresh))}.",
            diagram_en=svg_digit_slots([f"≥{lead_min}", "Free", "Free", "Even"], f"> {thresh}"),
        ))

    # 18. kang_jun_stars_and_bars_boxes (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_stars_and_bars_boxes"
    for n_stars, k_boxes in [(9, 3), (10, 4), (11, 3), (12, 4), (8, 5)]:
        ans = math.comb(n_stars - 1, k_boxes - 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Junior Kangaroo prize round, {m(str(n_stars))} identical silver coins are distributed among {m(str(k_boxes))} distinct boxes so each box gets **at least 1** coin. How many distributions are possible?",
            q_ar=f"في جولة جوائز بمسابقة الكانجارو للناشئين، تُوزَّع {m(str(n_stars))} عملات فضية متماثلة على {m(str(k_boxes))} صناديق متمايزة بحيث يحصل كل صندوق على **عملة واحدة على الأقل**. كم توزيعاً مختلفاً يمكن إجراؤه؟",
            correct_val=ans,
            distractors=[math.comb(n_stars + k_boxes - 1, k_boxes - 1), math.comb(n_stars, k_boxes), max(6, ans - k_boxes), ans + n_stars],
            hint_en=f"Choose {m(str(k_boxes - 1))} gaps among the {m(str(n_stars - 1))} interior spaces between {m(str(n_stars))} lined-up coins!",
            hint_ar=f"اختر {m(str(k_boxes - 1))} مواضع للفواصل من بين {m(str(n_stars - 1))} فراغات داخلية بين العملات!",
            idea_en=f"Positive integer solutions to {m(f'x_1 + \\dots + x_{{{k_boxes}}} = {n_stars}')} equal {m(f'\\binom{{{n_stars - 1}}}{{{k_boxes - 1}}}')}.",
            steps_en=[
                f"Place {m('1')} coin in each of the {m(str(k_boxes))} boxes (or pick {m(str(k_boxes - 1))} interior gaps).",
                f"Evaluate {m(f'\\binom{{{n_stars - 1}}}{{{k_boxes - 1}}} = {ans}')}.",
            ],
            check_en=f"Equivalently, {m(str(n_stars - k_boxes))} remaining coins into {m(str(k_boxes))} boxes gives {m(f'\\binom{{{(n_stars - k_boxes) + k_boxes - 1}}}{{{k_boxes - 1}}} = {ans}')}.",
            idea_ar=f"عدد الحلول الصحيحة الموجبة هو {m(f'\\binom{{{n_stars - 1}}}{{{k_boxes - 1}}}')}.",
            steps_ar=[
                f"نطبق قانون النجوم والفواصل مع شرط عدم خلو أي صندوق: {m(f'\\binom{{{n_stars} - 1}}{{{k_boxes} - 1}}')}.",
                f"الناتج {m(f'\\binom{{{n_stars - 1}}}{{{k_boxes - 1}}} = {ans}')}.",
            ],
            check_ar=f"بتوزيع عملة لكل صندوق يتبقى {m(str(n_stars - k_boxes))} عملات تعطي نفس الناتج {m(str(ans))}.",
            diagram_en=svg_number_strip(["★"] * min(3, k_boxes) + ["|", "★ ★"]),
        ))

    for n_stars, k_boxes in [(7, 3), (7, 4), (8, 3), (5, 5), (9, 4)]:
        ans = math.comb(n_stars + k_boxes - 1, k_boxes - 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On a Junior Kangaroo combinatorics sheet, how many ordered {m(str(k_boxes))}-tuples of **non-negative** integers {m(f'(x_1, \\dots, x_{{{k_boxes}}})')} satisfy {m(f'x_1 + \\dots + x_{{{k_boxes}}} = {n_stars}')}?",
            q_ar=f"في ورقة توافيق بمسابقة الكانجارو للناشئين، كم {m(str(k_boxes))}-ية مرتبة من الأعداد الصحيحة **غير السالبة** {m(f'(x_1, \\dots, x_{{{k_boxes}}})')} تحقق {m(f'x_1 + \\dots + x_{{{k_boxes}}} = {n_stars}')}؟",
            correct_val=ans,
            distractors=[math.comb(n_stars - 1, min(n_stars - 1, k_boxes - 1)), math.comb(n_stars + k_boxes, k_boxes), ans - n_stars, ans + k_boxes],
            hint_en=f"Arrange {m(str(n_stars))} stars and {m(str(k_boxes - 1))} bars in a row: {m(f'\\binom{{{n_stars} + {k_boxes} - 1}}{{{k_boxes} - 1}}')}.",
            hint_ar=f"رتّب {m(str(n_stars))} نجوم و{m(str(k_boxes - 1))} فواصل في صف واحد: {m(f'\\binom{{{n_stars} + {k_boxes} - 1}}{{{k_boxes} - 1}}')}.",
            idea_en=f"Allowing zeros corresponds directly to choosing {m(str(k_boxes - 1))} bar positions out of {m(str(n_stars + k_boxes - 1))} symbols.",
            steps_en=[
                f"Total symbols (stars + bars) {m(f'= {n_stars} + ({k_boxes} - 1) = {n_stars + k_boxes - 1}')}.",
                f"Count ways to place the bars: {m(f'\\binom{{{n_stars + k_boxes - 1}}}{{{k_boxes - 1}}} = {ans}')}.",
            ],
            check_en=f"Symmetry {m(f'\\binom{{{n_stars + k_boxes - 1}}}{{{n_stars}}} = {ans}')} confirms the count.",
            idea_ar=f"السماح بالصفر يعطي مباشرة {m(f'\\binom{{{n_stars + k_boxes - 1}}}{{{k_boxes - 1}}}')}.",
            steps_ar=[
                f"مجموع الرموز (النجوم + الفواصل) يساوي {m(str(n_stars + k_boxes - 1))}.",
                f"عدد التوزيعات {m(f'= \\binom{{{n_stars + k_boxes - 1}}}{{{k_boxes - 1}}} = {ans}')}.",
            ],
            check_ar=f"من تماثل التوافيق {m(f'\\binom{{{n_stars + k_boxes - 1}}}{{{n_stars}}} = {ans}')}.",
            diagram_en=svg_number_strip(["★ ★", "|", "0", "|", f"n={n_stars}"]),
        ))

    for M_sum in (7, 8, 9, 10, 11):
        ans = math.comb(M_sum, 3)
        brute = sum(1 for a in range(1, M_sum) for b in range(1, M_sum) for c in range(1, M_sum) if a + b + c <= M_sum)
        assert ans == brute
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo inequality-counting problem, how many ordered triples {m('(a, b, c)')} of **positive** integers satisfy {m(f'a + b + c \\le {M_sum}')}?",
            q_ar=f"في مسألة عدّ متباينات من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، كم ثلاثية مرتبة {m('(a, b, c)')} من الأعداد الصحيحة **الموجبة** تحقق المتباينة {m(f'a + b + c \\le {M_sum}')}؟",
            correct_val=ans,
            distractors=[math.comb(M_sum - 1, 2), math.comb(M_sum + 1, 3), ans - M_sum, ans + M_sum],
            hint_en=f"Introduce a fourth positive integer {m(f'd = {M_sum + 1} - (a + b + c) \\ge 1')} to turn the inequality into an exact equation!",
            hint_ar=f"أدخل متغيراً صحيحاً موجباً رابعاً {m(f'd = {M_sum + 1} - (a + b + c) \\ge 1')} لتحويل المتباينة إلى معادلة مساواة دقيقة!",
            idea_en=f"Adding slack variable {m(f'd = {M_sum + 1} - a - b - c \\ge 1')} gives a 1-to-1 bijection with {m(f'a + b + c + d = {M_sum + 1}')} in positive integers!",
            steps_en=[
                f"Define {m(f'd = {M_sum + 1} - (a + b + c)')}; since {m(f'a + b + c \\le {M_sum}')}, {m('d \\ge 1')} is a positive integer.",
                f"Now {m('a, b, c, d \\ge 1')} satisfy {m(f'a + b + c + d = {M_sum + 1}')}.",
                f"By Stars and Bars, there are {m(f'\\binom{{{M_sum + 1} - 1}}{{4 - 1}} = \\binom{{{M_sum}}}{{3}} = {ans}')} triples.",
            ],
            check_en=f"Hockey-stick sum over exact totals {m('s = 3, \\dots, ' + str(M_sum))}: {m(f'\\sum_{{s=3}}^{{{M_sum}}} \\binom{{s-1}}{{2}} = \\binom{{{M_sum}}}{{3}} = {ans}')}!",
            idea_ar=f"بإضافة المتغير المكمل الموجب {m(f'd = {M_sum + 1} - (a + b + c) \\ge 1')} تتحول المتباينة إلى {m(f'a + b + c + d = {M_sum + 1}')}.",
            steps_ar=[
                f"نعرّف {m(f'd = {M_sum + 1} - a - b - c \\ge 1')}.",
                f"تصبح المعادلة {m(f'a + b + c + d = {M_sum + 1}')} في الأعداد الصحيحة الموجبة.",
                f"عدد الحلول بالنجوم والفواصل هو {m(f'\\binom{{{M_sum}}}{{3}} = {ans}')}.",
            ],
            check_ar=f"مجموع الحالات من المجموع {m('3')} حتى {m(str(M_sum))} يعطي {m(f'\\binom{{{M_sum}}}{{3}} = {ans}')}.",
            diagram_en=svg_number_strip(["a", "b", "c", f"d (≤{M_sum})"]),
        ))

    # 19. kang_jun_invariant_parity_game (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_invariant_parity_game"
    for N_st, m_take in [(47, 5), (65, 6), (78, 7), (89, 8), (91, 9)]:
        mod_step = m_take + 1
        ans = N_st % mod_step
        assert 1 <= ans <= m_take
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo game board, a pile holds {m(str(N_st))} tokens. Two players take turns removing from {m('1')} up to {m(str(m_take))} tokens, and the player who takes the **last** token wins. How many tokens must the first player remove on Turn 1 to guarantee a win?",
            q_ar=f"على طاولة ألعاب بمسابقة الكانجارو للناشئين كومة فيها {m(str(N_st))} قرصاً. يتناوب لاعبان على سحب من {m('1')} إلى {m(str(m_take))} أقراص في الدور الواحد، والفائز هو من يسحب القرص **الأخير**. كم قرصاً يجب أن يسحب اللاعب الأول في البداية لضمان الفوز؟",
            correct_val=ans,
            distractors=[(ans % m_take) + 1, ((ans + 1) % m_take) + 1, m_take if ans != m_take else 1, mod_step],
            hint_en=f"Multiples of {m(f'{m_take} + 1 = {mod_step}')} are losing positions — leave a multiple of {m(str(mod_step))} for your opponent!",
            hint_ar=f"مضاعفات العدد {m(f'{m_take} + 1 = {mod_step}')} مواقع خاسرة — اترك لخصمك مضاعفاً للعدد {m(str(mod_step))}!",
            idea_en=f"Reduce {m(str(N_st))} modulo {m(str(mod_step))} and remove the remainder {m(str(ans))}.",
            steps_en=[
                f"Divide {m(str(N_st))} by {m(str(mod_step))}: {m(f'{N_st} = {mod_step} \\times {N_st // mod_step} + {ans}')}.",
                f"Remove {m(str(ans))} token(s) to leave {m(str(N_st - ans))}, then reply {m(f'{mod_step} - k')} whenever the opponent takes {m('k')}.",
            ],
            check_en=f"Since {m(f'{N_st - ans} = {mod_step} \\times {N_st // mod_step}')}, the first player takes the final token of every {m(str(mod_step))}-block.",
            idea_ar=f"نسحب باقي قسمة {m(str(N_st))} على {m(str(mod_step))} لنترك للخصم مضاعفاً للعدد {m(str(mod_step))}.",
            steps_ar=[
                f"{m(f'{N_st} = {mod_step} \\times {N_st // mod_step} + {ans}')}.",
                f"يسحب اللاعب الأول {m(str(ans))} ليترك {m(str(N_st - ans))} ثم يكمل كل دور إلى {m(str(mod_step))}.",
            ],
            check_ar=f"العدد {m(str(N_st - ans))} يقبل القسمة على {m(str(mod_step))} فيضمن الفوز للاعب الأول.",
            diagram_en=svg_kang_necklace_beads([str(i) for i in range(1, min(7, mod_step + 1))]),
        ))

    for N_bb, k_sub in [(20, 1), (25, 2), (30, 3), (40, 2), (50, 5)]:
        init_s = N_bb * (N_bb + 1) // 2
        ans = init_s - k_sub * (N_bb - 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"The integers {m(f'1, 2, 3, \\dots, {N_bb}')} are written on a Junior Kangaroo blackboard. Each step erases any two numbers {m('a')} and {m('b')} and writes {m(f'a + b - {k_sub}')} in their place until a single number remains. What is that final number?",
            q_ar=f"كُتبت الأعداد {m(f'1, 2, 3, \\dots, {N_bb}')} على سبورة مسابقة الكانجارو للناشئين. في كل خطوة يُمسح أي عددين {m('a')} و{m('b')} ويُكتب مكانهما العدد {m(f'a + b - {k_sub}')} حتى يتبقى عدد واحد فقط. ما هذا العدد الأخير؟",
            correct_val=ans,
            distractors=[init_s - k_sub * N_bb, init_s, ans + k_sub, ans - 2 * k_sub],
            hint_en=f"Count how many steps it takes to go from {m(str(N_bb))} numbers down to {m('1')} number ({m(str(N_bb - 1))} steps!), and track the total sum!",
            hint_ar=f"انتبه أن الانتقال من {m(str(N_bb))} أعداد إلى عدد واحد يستغرق {m(str(N_bb - 1))} خطوة بالضبط، وتتبّع المجموع الكلي!",
            idea_en=f"Every move lowers the count of numbers by {m('1')} and lowers the board sum by exact {m(str(k_sub))} — an order-independent invariant!",
            steps_en=[
                f"Initial sum is {m(f'\\frac{{{N_bb}({N_bb}+1)}}{{2}} = {init_s}')}.",
                f"Reducing {m(str(N_bb))} numbers to {m('1')} takes exact {m(f'{N_bb} - 1 = {N_bb - 1}')} moves, subtracting {m(f'{k_sub} \\times {N_bb - 1} = {k_sub * (N_bb - 1)}')}.",
                f"The invariant final number is {m(f'{init_s} - {k_sub * (N_bb - 1)} = {ans}')}.",
            ],
            check_en=f"Notice {m(f'\\sum (x_i - {k_sub})')} is a strict invariant across every single move!",
            idea_ar=f"كل خطوة تنقص عدد الأرقام بواحد وتنقص المجموع الكلي بمقدار ثابت {m(str(k_sub))} مهما كان الترتيب.",
            steps_ar=[
                f"المجموع الابتدائي: {m(f'\\frac{{{N_bb} \\times {N_bb + 1}}}{{2}} = {init_s}')}.",
                f"عدد الخطوات اللازمة هو {m(f'{N_bb} - 1 = {N_bb - 1}')} خطوة تنقص المجموع بمقدار {m(str(k_sub * (N_bb - 1)))}.",
                f"العدد الأخير الثابت هو {m(f'{init_s} - {k_sub * (N_bb - 1)} = {ans}')}.",
            ],
            check_ar=f"المقدار {m(f'\\sum (x_i - {k_sub})')} لامتغير محفوظ في كل خطوة.",
            diagram_en=svg_kang_polyomino_board([[1, 2, 1, 2], [2, 1, 2, 1], [1, 2, 1, 2]]),
        ))

    for N_mis, m_take in [(50, 4), (60, 5), (74, 6), (83, 7), (97, 8)]:
        mod_step = m_take + 1
        ans = (N_mis - 1) % mod_step
        assert 1 <= ans <= m_take
        # DP verify misere winning move
        win = [False] * (N_mis + 1)
        win[1] = False  # 1 stone left is losing in misere!
        for s in range(2, N_mis + 1):
            win[s] = any(not win[s - t] for t in range(1, min(m_take, s - 1) + 1))
        winning_moves = [t for t in range(1, m_take + 1) if not win[N_mis - t]]
        assert winning_moves == [ans]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo **poison-pebble** game, a pile has {m(str(N_mis))} pebbles. Players alternate taking {m('1')} to {m(str(m_take))} pebbles, and the player forced to take the **very last pebble LOSES**. How many pebbles must the first player remove on Turn 1 to guarantee victory?",
            q_ar=f"في لعبة **الحصاة المسمومة** (٥ نقاط) بمسابقة الكانجارو للناشئين، كومة فيها {m(str(N_mis))} حصاة. يتناوب لاعبان على سحب من {m('1')} إلى {m(str(m_take))} حصيات، واللاعب المضطر لسحب **الحصاة الأخيرة يخسر**. كم حصاة يجب على اللاعب الأول سحبها في النقلة الأولى لضمان الفوز؟",
            correct_val=ans,
            distractors=[N_mis % mod_step if N_mis % mod_step != 0 else m_take, (ans % m_take) + 1, ((ans + 1) % m_take) + 1, m_take if ans != m_take else 1],
            hint_en=f"Because the last pebble **loses**, leaving {m('1')} pebble is the target trap — so losing positions are {m(f'1, {1 + mod_step}, {1 + 2*mod_step}, \\dots')} ({m(f'\\equiv 1 \\pmod{{{mod_step}}}')})!",
            hint_ar=f"بما أن سحب الأخيرة **يُخسر** صاحبه، فإن ترك حصاة {m('1')} هو الفخ الرابح — أي المواقع الخاسرة تطابق {m(f'1 \\pmod{{{mod_step}}}')}!",
            idea_en=f"In misère play with max take {m(str(m_take))}, losing positions satisfy {m(f'P \\equiv 1 \\pmod{{{mod_step}}}')}, so remove {m(f'({N_mis} - 1) \\bmod {mod_step} = {ans}')}.",
            steps_en=[
                f"Leaving {m('1')} pebble forces an immediate loss; pairing moves by {m(str(mod_step))} makes every {m(f'{mod_step}k + 1')} a losing state.",
                f"Write {m(f'{N_mis} = {mod_step} \\times {(N_mis - 1) // mod_step} + 1 + {ans}')}.",
                f"Remove {m(str(ans))} pebbles on Turn 1 to leave {m(str(N_mis - ans))}, which is {m(f'\\equiv 1 \\pmod{{{mod_step}}}')}!",
            ],
            check_en=f"From {m(str(N_mis - ans))}, replying {m(f'{mod_step} - k')} after each opponent move {m('k')} eventually leaves exact {m('1')} poison pebble!",
            idea_ar=f"المواقع الخاسرة في اللعب العكسي هي {m(f'{mod_step}k + 1')}، لذا نسحب {m(f'({N_mis} - 1) \\bmod {mod_step} = {ans}')}.",
            steps_ar=[
                f"ترك حصاة واحدة موقع خاسر، وبإكمال كل جولة إلى {m(str(mod_step))} تكون جميع أعداد {m(f'{mod_step}k + 1')} خاسرة.",
                f"أكبر موقع خاسر تحت {m(str(N_mis))} هو {m(str(N_mis - ans))}.",
                f"يسحب اللاعب الأول {m(f'{N_mis} - {N_mis - ans} = {ans}')} حصيات ليحسم الفوز.",
            ],
            check_ar=f"الباقي {m(str(N_mis - ans))} يترك في النهاية حصاة مسمومة واحدة للخصم.",
            diagram_en=svg_kang_necklace_beads(["1 (L)", "+m+1", "...", f"N={N_mis}"]),
        ))

    # 20. kang_jun_extremal_pigeonhole_graph (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_extremal_pigeonhole_graph"
    easy_pig = [
        ([10, 12, 15, 5], 7),
        ([8, 14, 11, 4], 6),
        ([13, 16, 4, 12], 9),
        ([15, 6, 14, 18], 10),
        ([20, 17, 7, 19], 11),
    ]
    for counts, req_r in easy_pig:
        worst = sum(min(c, req_r - 1) for c in counts)
        ans = worst + 1
        c_str = ", ".join(m(str(c)) for c in counts)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"A Junior Kangaroo box holds marbles in four colors with counts {c_str}. Blindfolded, what is the minimum number of marbles you must draw to guarantee at least {m(str(req_r))} marbles of the **same** color?",
            q_ar=f"صندوق في مسابقة الكانجارو للناشئين يحوي كرات بأربعة ألوان أعدادها {c_str}. ما أقل عدد من الكرات يجب سحبه دون نظر لضمان الحصول على {m(str(req_r))} كرات على الأقل من **نفس** اللون؟",
            correct_val=ans,
            distractors=[4 * (req_r - 1) + 1, worst, ans + 2, sum(counts) - req_r],
            hint_en=f"Cap each color at {m(f'\\min(c_i, {req_r - 1})')} in the worst-case miss, then add {m('1')}!",
            hint_ar=f"احسب أسوأ حالة بأخذ {m(f'\\min(c_i, {req_r - 1})')} من كل لون ثم أضف كرة واحدة!",
            idea_en=f"Worst-case draw without {m(str(req_r))} matching marbles is {m(' + '.join(str(min(c, req_r - 1)) for c in counts) + f' = {worst}')}.",
            steps_en=[
                f"Maximum marbles drawn without reaching {m(str(req_r))} of any color is {m(' + '.join(str(min(c, req_r - 1)) for c in counts) + f' = {worst}')}.",
                f"One more marble ({m(f'{worst} + 1 = {ans}')}) forces one color to hit {m(str(req_r))}.",
            ],
            check_en=f"Notice one color has fewer than {m(str(req_r - 1))} marbles, avoiding the naive {m(str(4 * (req_r - 1) + 1))} trap!",
            idea_ar=f"أقصى سحب غير موفق هو {m(str(worst))} كرة، وبإضافة {m('1')} يتحقق الضمان عند {m(str(ans))}.",
            steps_ar=[
                f"نجمع {m(' + '.join(str(min(c, req_r - 1)) for c in counts) + f' = {worst}')} لأسوأ حالة.",
                f"العدد المضمون هو {m(f'{worst} + 1 = {ans}')}.",
            ],
            check_ar=f"عند {m(str(worst))} كرة قد لا يتحقق الشرط، وعند {m(str(ans))} يتحقق يقيناً.",
            diagram_en=svg_round_table(6, highlight_adj=True),
        ))

    med_graph = [
        (10, 4, 2, 3),
        (12, 5, 4, 3),
        (14, 4, 4, 2),
        (15, 6, 5, 4),
        (16, 5, 4, 3),
    ]
    for n_tot, d1, m_sub, d2 in med_graph:
        deg_sum = (n_tot - m_sub) * d1 + m_sub * d2
        assert deg_sum % 2 == 0
        ans = deg_sum // 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"At a Junior Kangaroo math camp of {m(str(n_tot))} students, {m(str(n_tot - m_sub))} veterans each shook hands with {m(str(d1))} students, and the {m(str(m_sub))} newcomers each shook hands with {m(str(d2))} students. How many handshakes occurred in total?",
            q_ar=f"في معسكر الكانجارو للناشئين المكون من {m(str(n_tot))} طالباً، صافح كل واحد من القدامى الـ {m(str(n_tot - m_sub))} بالضبط {m(str(d1))} طلاب، وصافح كل واحد من الجدد الـ {m(str(m_sub))} بالضبط {m(str(d2))} طلاب. كم مصافحة جرت في المجموع؟",
            correct_val=ans,
            distractors=[deg_sum, math.comb(n_tot, 2), ans + m_sub, ans - d1],
            hint_en=f"By the Handshaking Lemma, the sum of all individual handshake counts equals **twice** the number of handshakes!",
            hint_ar=f"حسب مبرهنة المصافحات، مجموع أعداد مصافحات الأفراد يساوي **ضعف** عدد المصافحات الفعلي!",
            idea_en=f"Sum all vertex degrees and divide by {m('2')} since every handshake involves two students.",
            steps_en=[
                f"Sum of degrees: {m(f'{n_tot - m_sub} \\times {d1} + {m_sub} \\times {d2} = {deg_sum}')}.",
                f"Divide by {m('2')}: {m(f'{deg_sum} \\div 2 = {ans}')} handshakes.",
            ],
            check_en=f"Clearly {m(f'{ans} \\le \\binom{{{n_tot}}}{{2}} = {math.comb(n_tot, 2)}')}, and degree sum {m(str(deg_sum))} is even.",
            idea_ar=f"نجمع درجات جميع الرؤوس ونقسم على {m('2')} لعدم عدّ المصافحة مرتين.",
            steps_ar=[
                f"مجموع الدرجات: {m(f'{n_tot - m_sub} \\times {d1} + {m_sub} \\times {d2} = {deg_sum}')}.",
                f"عدد المصافحات {m(f'= {deg_sum} \\div 2 = {ans}')}.",
            ],
            check_ar=f"قسمة المجموع الزوجي {m(str(deg_sum))} على {m('2')} تعطي {m(str(ans))}.",
            diagram_en=svg_graph_cycle_chords(min(8, n_tot), full_kn=False),
        ))

    for n_v in (8, 9, 10, 11, 12):
        ans = (n_v * n_v) // 4
        a_part, b_part = n_v // 2, (n_v + 1) // 2
        assert ans == a_part * b_part
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo graph-logic problem, there are {m(str(n_v))} contestants, and some pairs are mutual friends. If **no three contestants** are all mutual friends with one another, what is the **maximum** possible number of mutual friendships?",
            q_ar=f"في مسألة رسوم بيانية من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، يوجد {m(str(n_v))} متسابقين تربط بعض أزواجهم علاقة صداقة متبادلة. إذا لم يوجد **أي ثلاثة متسابقين** جميعهم أصدقاء فيما بينهم (بلا مثلث صداقة)، فما **أكبر** عدد ممكن من الصداقات؟",
            correct_val=ans,
            distractors=[math.comb(n_v, 2), ans - 1, ans + 2, 2 * n_v - 3],
            hint_en=f"Split the {m(str(n_v))} contestants into two balanced groups of sizes {m(str(a_part))} and {m(str(b_part))} and connect everyone across the two groups!",
            hint_ar=f"قسّم المتسابقين الـ {m(str(n_v))} إلى مجموعتين متوازنتين حجماهما {m(str(a_part))} و{m(str(b_part))} وصِل كل فرد من الأولى بجميع أفراد الثانية!",
            idea_en=f"By Mantel's Theorem, the maximum edges in a triangle-free graph on {m('n')} vertices is {m('\\lfloor n^2 / 4 \\rfloor')}, achieved by complete bipartite {m(f'K_{{{a_part},{b_part}}}')}.",
            steps_en=[
                f"Partition vertices into two disjoint sets of sizes {m(str(a_part))} and {m(str(b_part))} with all cross-edges and zero internal edges (no triangle can form by Pigeonhole!).",
                f"This achieves {m(f'{a_part} \\times {b_part} = \\lfloor {n_v}^2 / 4 \\rfloor = {ans}')} friendships, which is provably maximum.",
            ],
            check_en=f"Adding even {m('1')} more edge ({m(str(ans + 1))}) forces a friendship triangle by Mantel's bound!",
            idea_ar=f"أكبر عدد من الأضلاع في رسم خالٍ من المثلثات على {m('n')} رؤوس هو {m('\\lfloor n^2 / 4 \\rfloor')} عبر الرسم الثنائي المتوازن {m(f'K_{{{a_part},{b_part}}}')}.",
            steps_ar=[
                f"نقسم المتسابقين إلى مجموعتين بحجمين {m(str(a_part))} و{m(str(b_part))} ونصل فقط بين المجموعتين فلا يتكون أي مثلث.",
                f"أكبر عدد صداقات ممكن هو {m(f'{a_part} \\times {b_part} = {ans}')}.",
            ],
            check_ar=f"أي صداقة إضافية ({m(str(ans + 1))}) تنشئ حتماً مثلث صداقة.",
            diagram_en=svg_graph_cycle_chords(min(8, n_v), full_kn=True),
        ))

    return items


def _unit_4_6_data_prob(offset: int = 300) -> list[dict]:
    items: list[dict] = []
    topic = "Data & Probability"

    # 21. kang_jun_conditional_tree_prob (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_conditional_tree_prob"
    for r_c, b_c in [(3, 2), (4, 3), (5, 3), (4, 5), (6, 4)]:
        tot = r_c + b_c
        ans = Fraction(2 * r_c * b_c, tot * (tot - 1))
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"A Junior Kangaroo pouch contains {m(str(r_c))} red and {m(str(b_c))} blue tokens. Two tokens are drawn one after another **without replacement**. What is the probability that the two tokens have **different colors**?",
            q_ar=f"كيس في مسابقة الكانجارو للناشئين يحتوي على {m(str(r_c))} أقراص حمراء و{m(str(b_c))} زرقاء. سُحب قرصان الواحد تلو الآخر **دون إرجاع**. ما احتمال أن يكون القرصان **مختلفي اللون**؟",
            correct_val=ans,
            distractors=[Fraction(2 * r_c * b_c, tot * tot), Fraction(r_c * b_c, tot * (tot - 1)), 1 - ans, Fraction(r_c, tot)],
            hint_en=f"Add both orders — (Red then Blue) plus (Blue then Red) — remembering only {m(str(tot - 1))} tokens remain on Draw 2!",
            hint_ar=f"اجمع الترتيبين (أحمر ثم أزرق) و(أزرق ثم أحمر) مع تذكّر بقاء {m(str(tot - 1))} أقراص فقط في السحبة الثانية!",
            idea_en=f"Without replacement, {m('P(\\text{RB or BR}) = \\frac{2rb}{(r+b)(r+b-1)}')}.",
            steps_en=[
                f"Probability of Red then Blue is {m(f'\\frac{{{r_c}}}{{{tot}}} \\times \\frac{{{b_c}}}{{{tot - 1}}}')}; Blue then Red has the same probability.",
                f"Doubling gives {m(f'\\frac{{2 \\times {r_c} \\times {b_c}}}{{{tot} \\times {tot - 1}}} = {ans}')}.",
            ],
            check_en=f"Alternatively, {m(f'\\frac{{{r_c} \\times {b_c}}}{{\\binom{{{tot}}}{{2}}}} = \\frac{{{r_c * b_c}}}{{{tot * (tot - 1) // 2}}} = {ans}')}.",
            idea_ar=f"في السحب دون إرجاع يكون احتمال اختلاف اللونين {m('\\frac{2rb}{(r+b)(r+b-1)}')}.",
            steps_ar=[
                f"احتمال (أحمر ثم أزرق) يساوي {m(f'\\frac{{{r_c}}}{{{tot}}} \\times \\frac{{{b_c}}}{{{tot - 1}}}')} ومثله (أزرق ثم أحمر).",
                f"المجموع المبسط هو {m(str(ans))}.",
            ],
            check_ar=f"باستخدام التوافيق: {m(f'\\frac{{{r_c} \\times {b_c}}}{{\\binom{{{tot}}}{{2}}}} = {ans}')}.",
            diagram_en=svg_two_jars(f"{r_c}R, {b_c}B", r_c / tot, "Draw 2", 0.5, "no replace"),
        ))

    med_bag = [
        (2, 3, 2, 2),
        (4, 2, 1, 4),
        (3, 4, 3, 2),
        (5, 3, 2, 5),
        (2, 5, 4, 2),
    ]
    for r1, b1, r2, b2 in med_bag:
        t1, t2 = r1 + b1, r2 + b2
        ans = Fraction(r1, t1) * Fraction(r2 + 1, t2 + 1) + Fraction(b1, t1) * Fraction(r2, t2 + 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo transfer experiment, Jar A has {m(str(r1))} red and {m(str(b1))} blue balls, and Jar B has {m(str(r2))} red and {m(str(b2))} blue balls. One ball is moved at random from Jar A to Jar B, then one ball is drawn from Jar B. What is the probability it is **red**?",
            q_ar=f"في تجربة سحب متتابع بمسابقة الكانجارو للناشئين، يحوي الوعاء A {m(str(r1))} كرات حمراء و{m(str(b1))} زرقاء، ويحوي الوعاء B {m(str(r2))} حمراء و{m(str(b2))} زرقاء. نُقلت كرة عشوائياً من A إلى B ثم سُحبت كرة عشوائياً من B. ما احتمال أن تكون **حمراء**؟",
            correct_val=ans,
            distractors=[Fraction(r2, t2), Fraction(r1 + r2, t1 + t2), Fraction(r1, t1) * Fraction(r2 + 1, t2), 1 - ans],
            hint_en=f"Jar B holds {m(str(t2 + 1))} balls after the transfer! Sum the two branches (moved Red vs moved Blue).",
            hint_ar=f"يصبح في الوعاء B {m(str(t2 + 1))} كرات بعد النقل! اجمع فرعي الشجرة (نقل حمراء أو نقل زرقاء).",
            idea_en=f"Apply total probability across the two transfer outcomes into Jar B ({m(str(t2 + 1))} balls).",
            steps_en=[
                f"Move Red ({m(f'{r1}/{t1}')}): Jar B has {m(f'{r2 + 1}/{t2 + 1}')} red.",
                f"Move Blue ({m(f'{b1}/{t1}')}): Jar B has {m(f'{r2}/{t2 + 1}')} red.",
                f"Total {m(f'= \\frac{{{r1}({r2 + 1}) + {b1}({r2})}}{{{t1} \\times {t2 + 1}}} = {ans}')}.",
            ],
            check_en=f"Expected red count in Jar B is {m(f'{r2} + \\frac{{{r1}}}{{{t1}}}')}; dividing by {m(str(t2 + 1))} yields {m(str(ans))}.",
            idea_ar=f"نطبق قانون الاحتمال الكلي مع مقام جديد {m(str(t2 + 1))} للوعاء B.",
            steps_ar=[
                f"فرع نقل حمراء: {m(f'\\frac{{{r1}}}{{{t1}}} \\times \\frac{{{r2 + 1}}}{{{t2 + 1}}}')}؛ وفرع نقل زرقاء: {m(f'\\frac{{{b1}}}{{{t1}}} \\times \\frac{{{r2}}}{{{t2 + 1}}}')}.",
                f"مجموع الفرعين بعد التبسيط يساوي {m(str(ans))}.",
            ],
            check_ar=f"العدد المتوقع للكرات الحمراء مقسوماً على {m(str(t2 + 1))} يعطي {m(str(ans))}.",
            diagram_en=svg_two_jars(f"A:{r1}R,{b1}B", r1 / t1, f"B:{r2}R,{b2}B", r2 / t2, "1 ball →"),
        ))

    hard_bayes = [
        (3, 1, 1, 3),
        (4, 1, 2, 3),
        (5, 1, 1, 2),
        (3, 2, 2, 3),
        (4, 2, 1, 5),
    ]
    for r1, b1, r2, b2 in hard_bayes:
        p1 = Fraction(r1, r1 + b1)
        p2 = Fraction(r2, r2 + b2)
        ans = Fraction(p1, p1 + p2)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo conditional-probability puzzle, Box 1 holds {m(str(r1))} red and {m(str(b1))} white balls, while Box 2 holds {m(str(r2))} red and {m(str(b2))} white balls. A fair coin picks a box at random, and one drawn ball turns out to be **red**. What is the probability that Box 1 was chosen?",
            q_ar=f"في مسألة احتمال شرطي من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، يحوي الصندوق ١ {m(str(r1))} كرات حمراء و{m(str(b1))} بيضاء، ويحوي الصندوق ٢ {m(str(r2))} حمراء و{m(str(b2))} بيضاء. اختير أحد الصندوقين بعملة عادلة وسُحبت كرة فظهرت **حمراء**. ما احتمال أن تكون مسحوبة من الصندوق ١؟",
            correct_val=ans,
            distractors=[p1, Fraction(r1, r1 + r2) if Fraction(r1, r1 + r2) != ans else Fraction(p1 + p2, 2), 1 - ans, Fraction(p1, 2)],
            hint_en=f"Compare the red-draw rates {m(f'P(R \\mid B_1) = {p1}')} and {m(f'P(R \\mid B_2) = {p2}')} — the {m('1/2')} coin weights cancel in Bayes' ratio!",
            hint_ar=f"قارن احتمالي سحب الحمراء من الصندوقين {m(str(p1))} و{m(str(p2))} — عامل {m('1/2')} يختصر في البسط والمقام!",
            idea_en=f"With equal prior {m('1/2')}, {m('P(B_1 \\mid R) = \\frac{P(R \\mid B_1)}{P(R \\mid B_1) + P(R \\mid B_2)}')}.",
            steps_en=[
                f"Compute {m(f'P(R \\mid B_1) = \\frac{{{r1}}}{{{r1 + b1}}} = {p1}')} and {m(f'P(R \\mid B_2) = \\frac{{{r2}}}{{{r2 + b2}}} = {p2}')}.",
                f"Conditional probability {m(f'P(B_1 \\mid R) = \\frac{{{p1}}}{{{p1} + {p2}}} = {ans}')}.",
            ],
            check_en=f"Complementary probability for Box 2 is {m(str(1 - ans))}, and {m(f'{ans} + {1 - ans} = 1')}.",
            idea_ar=f"بما أن اختيار الصندوقين متساوي الاحتمال، فإن {m('P(B_1 \\mid R) = \\frac{p_1}{p_1 + p_2}')}.",
            steps_ar=[
                f"لدينا {m(f'p_1 = \\frac{{{r1}}}{{{r1 + b1}}}')} و{m(f'p_2 = \\frac{{{r2}}}{{{r2 + b2}}}')}.",
                f"الاحتمال الشرطي {m(f'= \\frac{{{p1}}}{{{p1} + {p2}}} = {ans}')}.",
            ],
            check_ar=f"مجموع احتمالي الصندوق ١ والصندوق ٢ بشرط ظهور الحمراء يساوي {m('1')}.",
            diagram_en=svg_two_jars(f"B1:{r1}R,{b1}W", float(p1), f"B2:{r2}R,{b2}W", float(p2), "Given Red"),
        ))

    # 22. kang_jun_geometric_target_prob (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_geometric_target_prob"
    easy_geo = [
        (10, 6, 4, 2),
        (10, 8, 5, 4),
        (12, 8, 3, 4),
        (9, 6, 3, 2),
        (12, 10, 4, 5),
    ]
    for L_r, W_r, ct, cr in easy_geo:
        tot_a = Fraction(L_r * W_r)
        c1 = Fraction(ct * W_r, 2)
        c2 = Fraction((L_r - ct) * (W_r - cr), 2)
        c3 = Fraction(L_r * cr, 2)
        sh_a = tot_a - c1 - c2 - c3
        ans = sh_a / tot_a
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"A {m(f'{L_r}\\text{{ cm}} \\times {W_r}\\text{{ cm}}')} Junior Kangaroo dartboard has an inscribed shaded triangle connecting its bottom-left corner to a top-edge point {m(f'{ct}\\text{{ cm}}')} from the left and a right-edge point {m(f'{cr}\\text{{ cm}}')} from the bottom. What is the probability a random dart hits the shaded triangle?",
            q_ar=f"لوحة سهام مستطيلة أبعادها {m(f'{L_r}\\text{{ cm}} \\times {W_r}\\text{{ cm}}')} في مسابقة الكانجارو للناشئين بداخلها مثلث مظلل يصل الركن الأيسر السفلي بنقطة على الحافة العليا تبعد {m(f'{ct}\\text{{ cm}}')} من اليسار ونقطة على الحافة اليمنى تبعد {m(f'{cr}\\text{{ cm}}')} من الأسفل. ما احتمال إصابة المثلث المظلل عشوائياً؟",
            correct_val=ans,
            distractors=[1 - ans, Fraction(1, 2) if ans != Fraction(1, 2) else Fraction(3, 8), ans + Fraction(1, 16), abs(ans - Fraction(1, 12))],
            hint_en=f"Subtract the three unshaded corner right triangles from {m(f'{L_r} \\times {W_r} = {L_r * W_r}')}!",
            hint_ar=f"اطرح مساحات المثلثات القائمة الثلاثة في الأركان من مساحة المستطيل {m(str(L_r * W_r))}!",
            idea_en=f"Divide shaded area {m(str(sh_a))} by total rectangle area {m(str(L_r * W_r))}.",
            steps_en=[
                f"Corner triangle areas are {m(str(c1))}, {m(str(c2))}, and {m(str(c3))}.",
                f"Shaded area is {m(f'{L_r * W_r} - ({c1} + {c2} + {c3}) = {sh_a}')}, so probability {m(f'= \\frac{{{sh_a}}}{{{L_r * W_r}}} = {ans}')}.",
            ],
            check_en=f"Unshaded probability is {m(str(1 - ans))}, and {m(f'{ans} + {1 - ans} = 1')}.",
            idea_ar=f"نقسم المساحة المظللة {m(str(sh_a))} على المساحة الكلية للمستطيل {m(str(L_r * W_r))}.",
            steps_ar=[
                f"مساحات مثلثات الأركان هي {m(str(c1))} و{m(str(c2))} و{m(str(c3))}.",
                f"المساحة المظللة {m(str(sh_a))} والاحتمال {m(str(ans))}.",
            ],
            check_ar=f"نسبة المساحة المظللة إلى المستطيل بعد الاختصار تساوي {m(str(ans))}.",
            diagram_en=svg_inscribed_corner_triangle_in_rect(L_r, W_r, ct, cr),
        ))

    for A_x, B_y, C_lim in [(6, 4, 4), (8, 5, 4), (10, 6, 6), (8, 6, 4), (12, 5, 5)]:
        assert C_lim <= min(A_x, B_y)
        ans = Fraction(C_lim * C_lim, 2 * A_x * B_y)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo continuous-probability task, real numbers {m('x \\in [0, ' + str(A_x) + ']')} and {m('y \\in [0, ' + str(B_y) + ']')} are chosen independently and uniformly at random. What is the probability that {m(f'x + y \\le {C_lim}')}?",
            q_ar=f"في مسألة احتمال مستمر بمسابقة الكانجارو للناشئين، يُختار العددان الحقيقيان {m('x \\in [0, ' + str(A_x) + ']')} و{m('y \\in [0, ' + str(B_y) + ']')} عشوائياً وبانتظام واستقلال. ما احتمال أن يتحقق {m(f'x + y \\le {C_lim}')}؟",
            correct_val=ans,
            distractors=[Fraction(C_lim * C_lim, A_x * B_y), Fraction(C_lim, A_x + B_y), 1 - ans, Fraction(C_lim, 2 * A_x)],
            hint_en=f"Plot {m(f'[0, {A_x}] \\times [0, {B_y}]')}: since {m(f'{C_lim} \\le {min(A_x, B_y)}')}, {m(f'x + y \\le {C_lim}')} is a right triangle of legs {m(str(C_lim))} and {m(str(C_lim))}!",
            hint_ar=f"في المستطيل {m(f'[0, {A_x}] \\times [0, {B_y}]')} تمثل المتباينة {m(f'x + y \\le {C_lim}')} مثلثاً قائماً في الركن ساقاه {m(str(C_lim))} و{m(str(C_lim))}!",
            idea_en=f"Favorable region is an isosceles right triangle of area {m(f'\\frac{{1}}{{2}}({C_lim})^2')} inside rectangle area {m(f'{A_x} \\times {B_y}')}.",
            steps_en=[
                f"Sample space rectangle has area {m(f'{A_x} \\times {B_y} = {A_x * B_y}')}.",
                f"Region {m(f'x \\ge 0, y \\ge 0, x + y \\le {C_lim}')} fits inside the rectangle with area {m(f'\\frac{{1}}{{2}}({C_lim})^2 = {Fraction(C_lim*C_lim, 2)}')}.",
                f"Probability {m(f'= \\frac{{{C_lim}^2}}{{2 \\times {A_x} \\times {B_y}}} = {ans}')}.",
            ],
            check_en=f"Since {m(f'{C_lim} \\le \\min({A_x}, {B_y})')}, neither leg is clipped by the top or right edge.",
            idea_ar=f"المنطقة المواتية مثلث قائم مساحته {m(f'{C_lim}^2 / 2')} داخل مستطيل مساحته {m(str(A_x * B_y))}.",
            steps_ar=[
                f"مساحة فضاء العينة المستطيل هي {m(str(A_x * B_y))}.",
                f"مساحة مثلث الشرط {m(f'x + y \\le {C_lim}')} تساوي {m(str(Fraction(C_lim * C_lim, 2)))}.",
                f"الاحتمال {m(f'= \\frac{{{C_lim * C_lim}}}{{{2 * A_x * B_y}}} = {ans}')}.",
            ],
            check_ar=f"لأن {m(f'{C_lim} \\le {min(A_x, B_y)}')} لا يقتطع المستطيل أي جزء من المثلث.",
            diagram_en=svg_shaded_triangle_in_rect(A_x, B_y, 0.35, ""),
        ))

    for w_min in (10, 12, 15, 20, 30):
        ans = 1 - Fraction(60 - w_min, 60) ** 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo meeting problem, Sara and Jude each arrive independently and uniformly at random between {m('12{:}00')} and {m('1{:}00')} ({m('60')} minutes) and wait **exact {m(str(w_min))} minutes** before leaving. What is the probability that they meet?",
            q_ar=f"في مسألة التقاء من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، تصل كل من سارة وجود بشكل مستقل وعشوائي منتظم بين الساعة {m('12{:}00')} و{m('1{:}00')} ({m('60')} دقيقة)، وتنتظر كل منهما **{m(str(w_min))} دقيقة بالضبط** قبل المغادرة. ما احتمال التقائهما؟",
            correct_val=ans,
            distractors=[Fraction(w_min, 60), Fraction(2 * w_min, 60), 1 - ans, Fraction(w_min * w_min, 3600)],
            hint_en=f"Graph arrival times {m('(x, y) \\in [0, 60]^2')}: they **miss** each other in two corner right triangles of leg {m(f'60 - {w_min} = {60 - w_min}')}!",
            hint_ar=f"مثّل وقتي الوصول في المربع {m('[0, 60]^2')}؛ يفوت اللقاء في مثلثين قائمين بالركنين طول ساق كل منهما {m(f'60 - {w_min} = {60 - w_min}')}!",
            idea_en=f"They meet iff {m(f'|x - y| \\le {w_min}')}, whose complement in {m('[0, 60]^2')} is two right triangles combining into a {m(f'{60 - w_min} \\times {60 - w_min}')} square!",
            steps_en=[
                f"Total square area is {m('60^2 = 3600')}.",
                f"Two miss triangles ({m(f'x - y > {w_min}')} and {m(f'y - x > {w_min}')}) together have area {m(f'2 \\times \\frac{{1}}{{2}}({60 - w_min})^2 = {(60 - w_min)**2}')}.",
                f"Meeting probability {m(f'= 1 - \\left(\\frac{{{60 - w_min}}}{{60}}\\right)^2 = {ans}')}.",
            ],
            check_en=f"Notice {m(str(ans))} is strictly less than {m(f'2w/60 = {Fraction(2 * w_min, 60)}')} because the strip clips at the corners.",
            idea_ar=f"شرط اللقاء {m(f'|x - y| \\le {w_min}')}، ومتممته مثلثان قائمان يشكلان معاً مربعاً ضلعه {m(str(60 - w_min))}.",
            steps_ar=[
                f"مساحة مربع الأزمان الكلي {m('60^2 = 3600')}.",
                f"مجموع مساحتي مثلثي عدم اللقاء يساوي {m(f'({60 - w_min})^2 = {(60 - w_min)**2}')}.",
                f"احتمال اللقاء {m(f'= 1 - \\left(\\frac{{{60 - w_min}}}{{60}}\\right)^2 = {ans}')}.",
            ],
            check_ar=f"عند {m('w = 60')} يعطي القانون احتمال {m('1')} وعند {m('w = 0')} يعطي {m('0')}، مما يؤكد دقته.",
            diagram_en=svg_square_eighths_shaded([0, 3, 4, 7], draw_horiz=True),
        ))

    # 23. kang_jun_mean_median_extremes (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_mean_median_extremes"
    for n_cnt, m_old, m_new in [(5, 74, 77), (6, 80, 83), (7, 68, 72), (8, 82, 85), (9, 75, 78)]:
        ans = (n_cnt + 1) * m_new - n_cnt * m_old
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Junior Kangaroo club, {m(str(n_cnt))} students had a mean score of {m(str(m_old))}. After one more student's score was recorded, the mean of all {m(str(n_cnt + 1))} students rose to {m(str(m_new))}. What score did the last student earn?",
            q_ar=f"في نادي الكانجارو للناشئين، كان متوسط درجات {m(str(n_cnt))} طلاب يساوي {m(str(m_old))}. وبعد إضافة درجة طالب جديد ارتفع متوسط جميع الطلاب الـ {m(str(n_cnt + 1))} إلى {m(str(m_new))}. ما درجة الطالب الأخير؟",
            correct_val=ans,
            distractors=[m_new + (m_new - m_old), ans - m_new + m_old, ans + (m_new - m_old), (m_old + m_new) // 2],
            hint_en=f"Subtract the old total {m(f'{n_cnt} \\times {m_old}')} from the new total {m(f'{n_cnt + 1} \\times {m_new}')}!",
            hint_ar=f"اطرح المجموع القديم {m(f'{n_cnt} \\times {m_old}')} من المجموع الجديد {m(f'{n_cnt + 1} \\times {m_new}')}!",
            idea_en=f"New score equals {m(f'({n_cnt + 1})({m_new}) - ({n_cnt})({m_old})')}.",
            steps_en=[
                f"Old sum: {m(f'{n_cnt} \\times {m_old} = {n_cnt * m_old}')}; new sum: {m(f'{n_cnt + 1} \\times {m_new} = {(n_cnt + 1) * m_new}')}.",
                f"Difference: {m(f'{(n_cnt + 1) * m_new} - {n_cnt * m_old} = {ans}')}.",
            ],
            check_en=f"Mental shortcut: {m(f'{m_new} + {n_cnt}({m_new} - {m_old}) = {m_new} + {n_cnt * (m_new - m_old)} = {ans}')}!",
            idea_ar=f"درجة الطالب الجديد تساوي الفرق بين المجموع الكلي الجديد والمجموع القديم.",
            steps_ar=[
                f"المجموع القديم {m(str(n_cnt * m_old))} والمجموع الجديد {m(str((n_cnt + 1) * m_new))}.",
                f"درجة الطالب الأخير {m(f'= {(n_cnt + 1) * m_new} - {n_cnt * m_old} = {ans}')}.",
            ],
            check_ar=f"اختصار ذهني: {m(f'{m_new} + {n_cnt} \\times {m_new - m_old} = {ans}')}.",
            diagram_en=svg_bar_chart([("Old", m_old, str(m_old)), ("New μ", m_new, str(m_new)), ("Last", ans, "?")], y_max=ans + 8),
        ))

    for n_cnt, mu_v, med_v in [(5, 14, 10), (5, 18, 13), (7, 16, 11), (7, 20, 14), (9, 15, 10)]:
        k_half = n_cnt // 2
        lows = list(range(1, k_half + 1))
        mids = [med_v + i for i in range(k_half)]
        tot_s = n_cnt * mu_v
        ans = tot_s - sum(lows) - sum(mids)
        assert ans > mids[-1]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"A list of {m(str(n_cnt))} **distinct** positive integers on a Junior Kangaroo leaderboard has mean {m(str(mu_v))} and median {m(str(med_v))}. What is the greatest possible value of the largest integer in the list?",
            q_ar=f"قائمة مكونة من {m(str(n_cnt))} أعداد صحيحة موجبة **مختلفة** في مسابقة الكانجارو للناشئين متوسطها الحسابي {m(str(mu_v))} ووسيطها {m(str(med_v))}. ما أكبر قيمة ممكنة للعدد الأكبر في القائمة؟",
            correct_val=ans,
            distractors=[ans - k_half, ans + k_half, tot_s - (n_cnt - 1), ans - (med_v - k_half)],
            hint_en=f"Minimize the {m(str(k_half))} positive integers below {m(str(med_v))} to {m('1, 2, \\dots')} and the {m(str(k_half - 1))} integers just above {m(str(med_v))} to {m(f'{med_v + 1}, \\dots')}!",
            hint_ar=f"صغّر الأعداد الواقعة قبل الوسيط إلى {m('1, 2, \\dots')} والأعداد الواقعة بعده مباشرة إلى {m(f'{med_v + 1}, \\dots')}!",
            idea_en=f"Fix sum {m(f'{n_cnt} \\times {mu_v} = {tot_s}')} and make the first {m(str(n_cnt - 1))} sorted entries as small as distinctness and median {m(str(med_v))} allow.",
            steps_en=[
                f"Smallest valid choices below median {m(str(med_v))} are {m(', '.join(str(x) for x in lows))}.",
                f"From median upward (excluding the max), smallest choices are {m(', '.join(str(x) for x in mids))}.",
                f"Subtract from {m(str(tot_s))}: {m(f'{tot_s} - {sum(lows) + sum(mids)} = {ans}')}.",
            ],
            check_en=f"Sorted list {m('\\{' + ', '.join(str(x) for x in lows + mids + [ans]) + '\\}')} has median {m(str(med_v))} and mean {m(str(mu_v))}.",
            idea_ar=f"نثبت المجموع {m(str(tot_s))} ونصغّر أول {m(str(n_cnt - 1))} عناصر مرتبة بأقصى قدر ممكن.",
            steps_ar=[
                f"أصغر قيم قبل الوسيط هي {m(', '.join(str(x) for x in lows))}، ومن الوسيط فصاعداً {m(', '.join(str(x) for x in mids))}.",
                f"أكبر قيمة للعنصر الأخير {m(f'= {tot_s} - {sum(lows) + sum(mids)} = {ans}')}.",
            ],
            check_ar=f"المجموع الكلي للقائمة المرتبة يساوي {m(str(tot_s))} والوسيط {m(str(med_v))}.",
            diagram_en=svg_bar_chart([("Min", 1, "1"), ("Med", med_v, str(med_v)), ("Max", ans, "?")], y_max=ans + 6),
        ))

    for mu_5 in (12, 16, 19, 22, 25):
        tot_s = 5 * mu_5
        ans = (tot_s - 6) // 3
        a5 = tot_s - (1 + 2 + ans + (ans + 1))
        assert 1 < 2 < ans < ans + 1 < a5 and 3 * (ans + 1) + 6 > tot_s
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo data-extremes problem, five **distinct** positive integers have a mean of {m(str(mu_5))}. What is the **largest** possible value of their **median**?",
            q_ar=f"في مسألة قيم متطرفة من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، خمسة أعداد صحيحة موجبة **مختلفة** متوسطها الحسابي {m(str(mu_5))}. ما **أكبر** قيمة ممكنة **لوسيطها**؟",
            correct_val=ans,
            distractors=[ans + 1, ans - 1, (tot_s - 3) // 3, mu_5 + 5],
            hint_en=f"With sorted {m('a_1 < a_2 < M < a_4 < a_5')} summing to {m(str(tot_s))}, set {m('a_1 = 1, a_2 = 2')} and {m('a_4 \\ge M + 1, a_5 \\ge M + 2')}!",
            hint_ar=f"في الترتيب {m('a_1 < a_2 < M < a_4 < a_5')} بمجموع {m(str(tot_s))}، اجعل {m('a_1 = 1, a_2 = 2')} واستخدم {m('a_4 \\ge M + 1, a_5 \\ge M + 2')}!",
            idea_en=f"Since {m('a_1 + a_2 \\ge 3')} and {m('a_3 + a_4 + a_5 \\ge M + (M+1) + (M+2) = 3M + 3')}, we must have {m(f'3M + 6 \\le {tot_s}')}.",
            steps_en=[
                f"Total sum is {m(f'5 \\times {mu_5} = {tot_s}')}.",
                f"Minimize all entries relative to median {m('M')}: {m(f'1 + 2 + M + (M + 1) + (M + 2) = 3M + 6 \\le {tot_s}')}.",
                f"Solve {m(f'3M \\le {tot_s - 6} \\implies M \\le {ans}')}, achieved explicitly by {m(f'\\{{1, 2, {ans}, {ans + 1}, {a5}\\}}')}.",
            ],
            check_en=f"Check {m(f'1 + 2 + {ans} + {ans + 1} + {a5} = {tot_s}')}, whereas {m(f'M = {ans + 1}')} requires sum {m(f'\\ge {3*(ans+1) + 6} > {tot_s}')}.",
            idea_ar=f"المجموع الأدنى بدلالة الوسيط {m('M')} هو {m('3M + 6')}، ومنه {m(f'3M + 6 \\le {tot_s}')}.",
            steps_ar=[
                f"المجموع الكلي للأعداد الخمسة يساوي {m(str(tot_s))}.",
                f"من {m(f'1 + 2 + M + (M+1) + (M+2) \\le {tot_s}')} نجد {m(f'3M \\le {tot_s - 6} \\implies M \\le {ans}')}.",
                f"تتحقق القيمة {m(str(ans))} فعلياً بالمجموعة {m(f'\\{{1, 2, {ans}, {ans + 1}, {a5}\\}}')}.",
            ],
            check_ar=f"مجموع المجموعة يساوي {m(str(tot_s))} ولا يمكن أن يصل الوسيط إلى {m(str(ans + 1))}.",
            diagram_en=svg_bar_chart([("1", 1, "1"), ("2", 2, "2"), ("Med", ans, "?"), ("a₄", ans + 1, "M+1"), ("a₅", a5, str(a5))], y_max=a5 + 5),
        ))

    # 24. kang_jun_inlet_outlet_pipes (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    bp = "kang_jun_inlet_outlet_pipes"
    for a_in, b_out in [(4, 12), (6, 15), (5, 20), (8, 12), (9, 18)]:
        ans = Fraction(a_in * b_out, b_out - a_in)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Junior Kangaroo tank puzzle, an inlet pipe fills an empty tank in {m(str(a_in))} hours, while a drain pipe empties a full tank in {m(str(b_out))} hours. If both are opened together when the tank is empty, how many hours will it take to fill?",
            q_ar=f"في لغز خزانات بمسابقة الكانجارو للناشئين، يملأ أنبوب تغذية خزاناً فارغاً في {m(str(a_in))} ساعات، ويفرّغ أنبوب تصريف الخزان الممتلئ في {m(str(b_out))} ساعة. إذا فُتح الأنبوبان معاً والخزان فارغ، فكم ساعة يستغرق امتلاؤه؟",
            correct_val=ans,
            distractors=[Fraction(a_in * b_out, a_in + b_out), b_out - a_in, ans + 2, Fraction(a_in + b_out, 2)],
            hint_en=f"Subtract hourly drain rate {m(f'1/{b_out}')} from hourly fill rate {m(f'1/{a_in}')}, then invert!",
            hint_ar=f"اطرح معدل التفريغ {m(f'1/{b_out}')} من معدل الملء {m(f'1/{a_in}')} ثم اقلب الناتج!",
            idea_en=f"Net rate is {m(f'\\frac{{1}}{{{a_in}}} - \\frac{{1}}{{{b_out}}} = \\frac{{{b_out - a_in}}}{{{a_in * b_out}}}')} tanks per hour.",
            steps_en=[
                f"Compute net hourly fraction: {m(f'\\frac{{1}}{{{a_in}}} - \\frac{{1}}{{{b_out}}} = \\frac{{{b_out} - {a_in}}}{{{a_in * b_out}}} = {Fraction(1, ans)}')}.",
                f"Invert to find fill time: {m(f'{ans}')} hours.",
            ],
            check_en=f"In {m(f'{ans}')} hours, inlet supplies {m(str(ans / a_in))} tanks and drain removes {m(str(ans / b_out))}, net {m('1')} full tank!",
            idea_ar=f"المعدل الصافي في الساعة هو {m(f'\\frac{{1}}{{{a_in}}} - \\frac{{1}}{{{b_out}}}')} وزمن الامتلاء مقلوبه.",
            steps_ar=[
                f"نحسب المعدل الصافي: {m(f'\\frac{{1}}{{{a_in}}} - \\frac{{1}}{{{b_out}}} = {Fraction(1, ans)}')}.",
                f"زمن الامتلاء يساوي {m(str(ans))} ساعة.",
            ],
            check_ar=f"الفرق بين ما يضخه الأول وما يفرغه الثاني خلال هذه المدة يساوي خزاناً كاملاً.",
            diagram_en=svg_pipe_tank(f"+1/{a_in}", f"−1/{b_out}"),
        ))

    for a_in, b_in, c_out in [(4, 6, 12), (3, 6, 4), (6, 10, 15), (8, 12, 24), (4, 8, 16)]:
        net_r = Fraction(1, a_in) + Fraction(1, b_in) - Fraction(1, c_out)
        assert net_r > 0
        ans = Fraction(1, net_r)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Junior Kangaroo fountain system, Inlet A fills the basin in {m(str(a_in))} hours, Inlet B fills it in {m(str(b_in))} hours, and Outlet C drains a full basin in {m(str(c_out))} hours. Starting empty with all three open, how many hours does the basin take to fill?",
            q_ar=f"في نظام نافورة بمسابقة الكانجارو للناشئين، يملأ الأنبوب A الحوض في {m(str(a_in))} ساعات، ويملؤه B في {m(str(b_in))} ساعات، بينما يفرّغه المخرج C في {m(str(c_out))} ساعة. إذا فُتحت الثلاثة معاً والحوض فارغ، فكم ساعة يستغرق امتلاؤه؟",
            correct_val=ans,
            distractors=[Fraction(1, Fraction(1, a_in) + Fraction(1, b_in) + Fraction(1, c_out)), ans + 1, Fraction(a_in + b_in, 2), ans + 2],
            hint_en=f"Combine signed hourly rates {m(f'\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}}')} and take the reciprocal.",
            hint_ar=f"اجمع المعدلات الساعية بإشاراتها {m(f'\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}}')} ثم خذ المقلوب.",
            idea_en=f"Net filling rate equals {m(f'\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}} = {net_r}')} basins per hour.",
            steps_en=[
                f"Sum the signed rates: {m(f'\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}} = {net_r}')}.",
                f"Take the reciprocal: {m(f'T = {ans}')} hours.",
            ],
            check_en=f"Verify {m(f'{ans} \\times \\left(\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}}\\right) = 1')}.",
            idea_ar=f"المعدل الصافي يساوي مجموع معدلي الملء مطروحاً منه معدل التفريغ.",
            steps_ar=[
                f"المعدل الصافي في الساعة: {m(f'\\frac{{1}}{{{a_in}}} + \\frac{{1}}{{{b_in}}} - \\frac{{1}}{{{c_out}}} = {net_r}')}.",
                f"زمن الامتلاء {m(f'= {ans}')} ساعة.",
            ],
            check_ar=f"حاصل ضرب الزمن في المعدل الصافي يعطي {m('1')} حوض كامل.",
            diagram_en=svg_pipe_tank(f"+1/{a_in},+1/{b_in}", f"−1/{c_out}"),
        ))

    for a_pump, t_act in [(6, 8), (4, 6), (8, 10), (10, 15), (12, 16)]:
        leak_r = Fraction(1, a_pump) - Fraction(1, t_act)
        ans = Fraction(1, leak_r)
        assert ans.denominator == 1
        ans_i = int(ans)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Junior Kangaroo leak puzzle, a pump normally fills an empty pool in {m(str(a_pump))} hours, but owing to a bottom leak it took {m(str(t_act))} hours to fill. Once the pool is full and the pump is turned off, how many hours will the leak alone take to empty the pool?",
            q_ar=f"في مسألة تسرب من فئة ٥ نقاط بمسابقة الكانجارو للناشئين، تملأ مضخة مسبحاً فارغاً عادةً في {m(str(a_pump))} ساعات، لكن بسبب تسرب في القاع استغرق امتلاؤه {m(str(t_act))} ساعات. إذا أُغلقت المضخة بعد امتلاء المسبح، فكم ساعة يستغرق التسرب وحده لتفريغ المسبح بالكامل؟",
            correct_val=ans_i,
            distractors=[a_pump + t_act, ans_i // 2, ans_i + a_pump, t_act * 2],
            hint_en=f"The leak's hourly rate equals the slowdown in filling rate: {m(f'\\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{{t_act}}}')}!",
            hint_ar=f"معدل التسرب في الساعة يساوي مقدار النقص في معدل الملء: {m(f'\\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{{t_act}}}')}!",
            idea_en=f"From {m(f'\\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{L}} = \\frac{{1}}{{{t_act}}}')}, isolate {m(f'\\frac{{1}}{{L}} = \\frac{{{t_act} - {a_pump}}}{{{a_pump} \\times {t_act}}}')}.",
            steps_en=[
                f"Pump rate minus leak rate equals observed net rate: {m(f'\\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{L}} = \\frac{{1}}{{{t_act}}}')}.",
                f"Solve for leak rate: {m(f'\\frac{{1}}{{L}} = \\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{{t_act}}} = {leak_r}')}.",
                f"Thus the leak empties a full pool in {m(str(ans_i))} hours.",
            ],
            check_en=f"In {m(str(t_act))} hours, the pump supplies {m(f'{t_act}/{a_pump}')} pools while the leak drains {m(f'{t_act}/{ans_i}')} pools, leaving {m(f'{Fraction(t_act, a_pump)} - {Fraction(t_act, ans_i)} = 1')} full pool!",
            idea_ar=f"نطرح المعدل الفعلي من معدل المضخة لإيجاد معدل التسرب ثم نقلبه.",
            steps_ar=[
                f"المعادلة: {m(f'\\frac{{1}}{{{a_pump}}} - \\frac{{1}}{{L}} = \\frac{{1}}{{{t_act}}}')}.",
                f"ومنه {m(f'\\frac{{1}}{{L}} = {leak_r} \\implies L = {ans_i}')} ساعة.",
            ],
            check_ar=f"خلال {m(str(t_act))} ساعات تضخ المضخة {m(f'{t_act}/{a_pump}')} ويفرغ التسرب {m(f'{t_act}/{ans_i}')} والفرق {m('1')} تماماً.",
            diagram_en=svg_pipe_tank(f"+1/{a_pump}", "−1/L = ?"),
        ))

    return items


def build_junior_bank() -> list[dict]:
    """Build all 360 verified Junior (Grades 9–10) Kangaroo Math Competition questions."""
    bank: list[dict] = []
    bank.extend(_unit_4_1_number_theory(0))
    bank.extend(_unit_4_2_algebra(60))
    bank.extend(_unit_4_3_geometry_circles_sim(120))
    bank.extend(_unit_4_4_geometry_3d_coord(180))
    bank.extend(_unit_4_5_combinatorics(240))
    bank.extend(_unit_4_6_data_prob(300))
    return bank
