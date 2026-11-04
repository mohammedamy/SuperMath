"""Student Division (Grades 11–12) Question Bank Generator for Kangaroo Math Competition (360 questions)."""
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

from kangaroo_common import (
    KANGAROO_FORBIDDEN_RE,
    load_other_track_stems,
    m,
    make_kang_q,
    norm_text,
    svg_angle_bisector_tri,
    svg_binary_bulbs,
    svg_coord_diamond,
    svg_cube_in_cylinder,
    svg_digit_slots,
    svg_factor_tree,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_grid_polygon,
    svg_kang_cube_faces,
    svg_kang_necklace_beads,
    svg_kang_polyomino_board,
    svg_median_tri,
    svg_number_strip,
    svg_painted_cube_3d,
    svg_parabola_roots,
    svg_power_of_point,
    svg_regular_polygon,
    svg_round_table,
    svg_street_grid,
    svg_stu_ceva_triangle,
    svg_stu_cone_frustum,
    svg_stu_cube_corner_cut,
    svg_stu_dyck_grid,
    svg_stu_meeting_square,
    svg_stu_mirror_bounce,
    svg_stu_probability_tree,
    svg_stu_sphere_in_cylinder,
    svg_stu_tangent_circles,
    svg_stu_tangential_quad,
    svg_subdivided_rect_2x2,
    svg_two_jars,
    svg_venn_3,
)

LEVEL = "Student"


def _next_qid(items: list[dict], offset: int = 0) -> str:
    return f"KANG-STU-{offset + len(items) + 1:03d}"


def _prime_factors(n: int) -> list[int]:
    ps = []
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            ps.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        ps.append(x)
    return ps


def _totient_formula(n: int) -> int:
    res = n
    for p in _prime_factors(n):
        res = (res // p) * (p - 1)
    return res


def _to_base_digits(n: int, b: int) -> list[int]:
    if n == 0:
        return [0]
    out = []
    x = n
    while x > 0:
        out.append(x % b)
        x //= b
    return out[::-1]


def _cubic_real_roots(p: int, q: int, w: int) -> list[float]:
    """Find all 3 real roots of x^3 - p*x^2 + q*x - w = 0 via sign-change bisection."""
    b, c, d = -p, q, -w
    disc = 18 * b * c * d - 4 * (b ** 3) * d + (b * c) ** 2 - 4 * (c ** 3) - 27 * (d ** 2)
    assert disc > 0, f"Cubic must have 3 distinct real roots: {(p, q, w)}"
    f = lambda x: ((x - p) * x + q) * x - w
    xs = [-20.0 + 0.05 * i for i in range(801)]
    roots = []
    for x0, x1 in zip(xs, xs[1:]):
        y0, y1 = f(x0), f(x1)
        if y0 == 0.0:
            roots.append(x0)
        elif y0 * y1 < 0.0:
            lo, hi = x0, x1
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if f(lo) * f(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
    assert len(roots) == 3, f"Expected 3 real roots, found {len(roots)} for {(p, q, w)}"
    return roots


def _count_tilings(rows: int, cols: int, shapes: list[list[tuple[int, int]]]) -> int:
    """Exact bitmask backtracking solver for tiling a rows x cols board."""
    norm_shapes = []
    for sh in shapes:
        s = sorted(sh)
        r0, c0 = s[0]
        norm_shapes.append(tuple((r - r0, c - c0) for r, c in s))
    memo: dict[int, int] = {}
    full = (1 << (rows * cols)) - 1

    def dfs(mask: int) -> int:
        if mask == full:
            return 1
        if mask in memo:
            return memo[mask]
        idx = (~mask & (mask + 1)).bit_length() - 1
        r0, c0 = divmod(idx, cols)
        tot = 0
        for sh in norm_shapes:
            add = 0
            ok = True
            for dr, dc in sh:
                nr, nc = r0 + dr, c0 + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    ok = False
                    break
                bit = 1 << (nr * cols + nc)
                if mask & bit:
                    ok = False
                    break
                add |= bit
            if ok:
                tot += dfs(mask | add)
        memo[mask] = tot
        return tot

    return dfs(0)


# ==============================================================================
# UNIT 5.1 — NUMBER THEORY (60 Questions: KANG-STU-001 .. KANG-STU-060)
# ==============================================================================
def _unit_5_1_number_theory(offset: int = 0) -> list[dict]:
    items: list[dict] = []
    topic = "Number Theory"

    # ------------------------------------------------------------------
    # 1. kang_stu_totient_coprime_counts (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_totient_coprime_counts"
    easy_tot = [
        (180, "Ziad", "زياد"),
        (210, "Mariam", "مريم"),
        (300, "Kareem", "كريم"),
        (420, "Nadia", "نادية"),
        (540, "Faisal", "فيصل"),
    ]
    for N, name_en, name_ar in easy_tot:
        ans = _totient_formula(N)
        brute = sum(1 for k in range(1, N + 1) if math.gcd(k, N) == 1)
        assert ans == brute
        ps = _prime_factors(N)
        p_str = ", ".join(str(p) for p in ps)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On {name_en}'s Grade 11–12 Student Kangaroo warm-up card, how many integers {m('k')} in {m(f'\\{{1, 2, \\dots, {N}\\}}')} are relatively prime to {m(str(N))} (that is, {m(f'\\gcd(k, {N}) = 1')})?",
            q_ar=f"في بطاقة تدريب الكانجارو للمستوى المتقدم (الصفين ١١–١٢) الخاصة بـ{name_ar}، كم عدداً صحيحاً {m('k')} في المجموعة {m(f'\\{{1, 2, \\dots, {N}\\}}')} أوليٌّ نسبياً مع {m(str(N))} (أي {m(f'\\gcd(k, {N}) = 1')})؟",
            correct_val=ans,
            distractors=[ans + 12, max(8, ans - 12), N // 2, ans + 6],
            hint_en=f"Find the distinct prime divisors of {m(str(N))} and apply Euler's totient product {m('\\varphi(N) = N \\prod (1 - 1/p)')}.",
            hint_ar=f"أوجد العوامل الأولية المختلفة للعدد {m(str(N))} وطبّق صيغة أويلر {m('\\varphi(N) = N \\prod (1 - 1/p)')}.",
            idea_en=f"Euler's totient {m('\\varphi(' + str(N) + ')')} removes every multiple of the distinct prime factors {m(p_str)}.",
            steps_en=[
                f"The distinct prime factors of {m(str(N))} are {m(p_str)}.",
                f"Multiply {m(str(N))} by {m(' \\cdot '.join(f'(1 - 1/{p})' for p in ps))} to obtain {m(str(ans))}.",
            ],
            check_en=f"Direct modular sieve over {m(f'1 \\dots {N}')} confirms exact {m(str(ans))} coprime integers.",
            idea_ar=f"دالة أويلر {m('\\varphi(' + str(N) + ')')} تستبعد مضاعفات العوامل الأولية المختلفة ({m(p_str)}) بالتضمين والإقصاء.",
            steps_ar=[
                f"العوامل الأولية المختلفة للعدد {m(str(N))} هي {m(p_str)}.",
                f"نحسب {m(f'{N} \\times ' + ' \\times '.join(f'\\frac{{{p-1}}}{{{p}}}' for p in ps))} فنحصل على {m(str(ans))}.",
            ],
            check_ar=f"العدّ المباشر للأعداد الأولية نسبياً مع {m(str(N))} يؤكد وجود {m(str(ans))} عدداً بالضبط.",
            diagram_en=svg_number_strip(["1", "2", "...", str(N), "gcd=1?"]),
        ))

    med_tot = [
        (360, 6, "Set A"),
        (420, 7, "Set B"),
        (504, 12, "Set C"),
        (600, 15, "Set D"),
        (720, 9, "Set E"),
    ]
    for idx_m, (N, d, tag) in enumerate(med_tot, 1):
        M = N // d
        ans = _totient_formula(M)
        brute = sum(1 for k in range(1, N + 1) if math.gcd(k, N) == d)
        assert ans == brute and N % d == 0
        ps = _prime_factors(M)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Student Kangaroo {tag}, how many integers {m('k')} in {m(f'\\{{1, 2, \\dots, {N}\\}}')} satisfy {m(f'\\gcd(k, {N}) = {d}')}?",
            q_ar=f"في مجموعة مسائل الكانجارو للمستوى المتقدم ({idx_m})، كم عدداً صحيحاً {m('k')} في {m(f'\\{{1, 2, \\dots, {N}\\}}')} يحقق {m(f'\\gcd(k, {N}) = {d}')}؟",
            correct_val=ans,
            distractors=[M, ans + 4, max(4, ans - 4), ans * 2],
            hint_en=f"Write {m(f'k = {d}m')} with {m(f'1 \\le m \\le {M}')}; then {m(f'\\gcd({d}m, {N}) = {d}')} is equivalent to {m(f'\\gcd(m, {M}) = 1')}.",
            hint_ar=f"ضع {m(f'k = {d}m')} حيث {m(f'1 \\le m \\le {M}')}؛ فيتكافأ الشرط مع {m(f'\\gcd(m, {M}) = 1')}.",
            idea_en=f"Divide out the common factor {m(str(d))} to reduce the condition to {m(f'\\gcd(m, {M}) = 1')} for {m(f'1 \\le m \\le {M}')}.",
            steps_en=[
                f"Every valid {m('k')} has the form {m(f'k = {d}m')} with {m(f'1 \\le m \\le {N}/{d} = {M}')}.",
                f"Then {m(f'\\gcd({d}m, {d} \\cdot {M}) = {d} \\iff \\gcd(m, {M}) = 1')}.",
                f"Using prime factors {m(', '.join(str(p) for p in ps))} of {m(str(M))}, {m(f'\\varphi({M}) = {ans}')}.",
            ],
            check_en=f"Out of {m(str(M))} multiples of {m(str(d))} up to {m(str(N))}, exact {m(str(ans))} share no extra factor with {m(str(M))}.",
            idea_ar=f"بقسمة الطرفين على {m(str(d))} تتحول المسألة إلى حساب {m(f'\\varphi({M})')}.",
            steps_ar=[
                f"نكتب {m(f'k = {d}m')} حيث {m(f'1 \\le m \\le {M}')}.",
                f"يتحقق {m(f'\\gcd(k, {N}) = {d}')} إذا وفقط إذا كان {m(f'\\gcd(m, {M}) = 1')}.",
                f"بحساب {m(f'\\varphi({M})')} نجد {m(str(ans))} قيمة.",
            ],
            check_ar=f"التحقق من جميع مضاعفات {m(str(d))} حتى {m(str(N))} يؤكد أن العدد هو {m(str(ans))}.",
            diagram_en=svg_number_strip([f"1..{N}", f"gcd={d}", "k = ?"]),
        ))

    hard_tot = [
        (105, "Final #1"),
        (165, "Final #2"),
        (195, "Final #3"),
        (231, "Final #4"),
        (285, "Final #5"),
    ]
    for idx_h, (N, tag) in enumerate(hard_tot, 1):
        phi_n = _totient_formula(N)
        ans = phi_n // 2
        exact_sum = sum(Fraction(k, N) for k in range(1, N) if math.gcd(k, N) == 1)
        assert exact_sum == ans and phi_n % 2 == 0
        ps = _prime_factors(N)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On Student Kangaroo {tag}, all reduced proper fractions {m(f'\\frac{{k}}{{{N}}}')} with {m(f'1 \\le k < {N}')} and {m(f'\\gcd(k, {N}) = 1')} are written down and added together. What is their exact sum?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_h})، كُتبت جميع الكسور الفعلية المختزلة {m(f'\\frac{{k}}{{{N}}}')} حيث {m(f'1 \\le k < {N}')} و{m(f'\\gcd(k, {N}) = 1')} ثم جُمعت معاً. ما المجموع الدقيق لهذه الكسور؟",
            correct_val=ans,
            distractors=[phi_n, ans + 4, max(4, ans - 6), (N - 1) // 2],
            hint_en=f"Pair each reduced fraction {m(f'k/{N}')} with {m(f'({N}-k)/{N}')}, since {m(f'\\gcd({N}-k, {N}) = \\gcd(k, {N}) = 1')}.",
            hint_ar=f"أقرن كل كسر مختزل {m(f'k/{N}')} مع {m(f'({N}-k)/{N}')} لأن {m(f'\\gcd({N}-k, {N}) = \\gcd(k, {N}) = 1')}.",
            idea_en=f"Symmetric pairing {m(f'\\frac{{k}}{{{N}}} + \\frac{{{N}-k}}{{{N}}} = 1')} makes the sum equal to {m(f'\\frac{{1}}{{2}}\\varphi({N})')}.",
            steps_en=[
                f"Factor {m(f'{N} = ' + ' \\times '.join(str(p) for p in ps))}, so {m(f'\\varphi({N}) = ' + ' \\times '.join(str(p - 1) for p in ps) + f' = {phi_n}')}.",
                f"Since {m(f'{N} > 2')}, the {m(str(phi_n))} numerators pair into {m(f'{phi_n}/2 = {ans}')} pairs, each summing to {m('1')}.",
                f"Therefore the exact sum of the fractions is {m(str(ans))}.",
            ],
            check_en=f"Adding all {m(str(phi_n))} irreducible fractions with denominator {m(str(N))} gives {m(f'{phi_n}/2 = {ans}')}.",
            idea_ar=f"كل كسر {m(f'k/{N}')} يقترن مع {m(f'({N}-k)/{N}')} بمجموع قدره {m('1')}، فيكون المجموع {m(f'\\varphi({N})/2')}.",
            steps_ar=[
                f"نحلّل {m(f'{N} = ' + ' \\times '.join(str(p) for p in ps))} ومنه {m(f'\\varphi({N}) = {phi_n}')}.",
                f"تنتظم الكسور في {m(f'{phi_n}/2 = {ans}')} أزواج مجموع كل زوج منها {m('1')}.",
                f"إذن المجموع الكلي يساوي {m(str(ans))}.",
            ],
            check_ar=f"جمع الكسور المختزلة مباشرة يعطي {m(str(ans))} تماماً.",
            diagram_en=svg_number_strip([f"1/{N}", "...", f"{N-1}/{N}", "Sum=?"]),
        ))

    # ------------------------------------------------------------------
    # 2. kang_stu_frobenius_stamp_bezout (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_frobenius_stamp_bezout"
    easy_frob = [
        (5, 8, "cents", "سنتاً"),
        (6, 11, "points", "نقطة"),
        (7, 9, "riyal", "ريالاً"),
        (7, 12, "credits", "رصيداً"),
        (8, 13, "tokens", "قطعة"),
    ]
    for idx_e, (a, b, unit_en, unit_ar) in enumerate(easy_frob, 1):
        assert math.gcd(a, b) == 1
        ans = a * b - a - b
        limit = 2 * a * b + 20
        reachable = {a * x + b * y for x in range(limit // a + 2) for y in range(limit // b + 2)}
        unreachable = [m_v for m_v in range(1, limit) if m_v not in reachable]
        assert max(unreachable) == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Student Kangaroo kiosk puzzle (#{idx_e}), a machine dispenses only {m(str(a))}-{unit_en} and {m(str(b))}-{unit_en} vouchers in unlimited supply. What is the **largest** integer total (in {unit_en}) that **cannot** be formed?",
            q_ar=f"في لغز كشك الكانجارو للمستوى المتقدم ({idx_e})، تصدر آلة قسائم من فئتي {m(str(a))} و{m(str(b))} ({unit_ar}) فقط بكميات غير محدودة. ما **أكبر** مبلغ صحيح لا يمكن تكوينه؟",
            correct_val=ans,
            distractors=[a * b - 1, ans + a, ans - 1, a * b - a],
            hint_en=f"For coprime denominations {m('a')} and {m('b')}, apply the Chicken McNugget / Frobenius bound {m('ab - a - b')}.",
            hint_ar=f"لفئتين أوليتين نسبياً {m('a')} و{m('b')} استخدم صيغة فروبينيوس {m('ab - a - b')}.",
            idea_en=f"Since {m(f'\\gcd({a}, {b}) = 1')}, the Frobenius coin number is {m(f'{a} \\times {b} - {a} - {b}')}.",
            steps_en=[
                f"Verify {m(f'\\gcd({a}, {b}) = 1')}, so every sufficiently large integer is representable.",
                f"Compute {m(f'ab - a - b = {a} \\times {b} - {a} - {b} = {ans}')}.",
            ],
            check_en=f"Every integer from {m(str(ans + 1))} onward can be written as {m(f'{a}x + {b}y')} with {m('x, y \\ge 0')}, whereas {m(str(ans))} cannot.",
            idea_ar=f"بما أن {m(f'\\gcd({a}, {b}) = 1')} فإن أكبر عدد غير قابل للتكوين هو {m(f'ab - a - b')}.",
            steps_ar=[
                f"نتحقق أن {m(f'\\gcd({a}, {b}) = 1')}.",
                f"نحسب {m(f'{a} \\times {b} - {a} - {b} = {ans}')}.",
            ],
            check_ar=f"العدد {m(str(ans))} لا يُكتب بصورة {m(f'{a}x + {b}y')} مع {m('x, y \\ge 0')}، وكل عدد أكبر منه قابل للتكوين.",
            diagram_en=svg_digit_slots([f"+{a}", f"+{b}", "?"], "Max gap"),
        ))

    med_frob = [
        (4, 9, "Card I"),
        (5, 11, "Card II"),
        (6, 13, "Card III"),
        (7, 10, "Card IV"),
        (8, 11, "Card V"),
    ]
    for idx_m, (a, b, card) in enumerate(med_frob, 1):
        assert math.gcd(a, b) == 1
        ans = (a - 1) * (b - 1) // 2
        limit = 2 * a * b + 20
        reachable = {a * x + b * y for x in range(limit // a + 2) for y in range(limit // b + 2)}
        unreachable = [m_v for m_v in range(1, limit) if m_v not in reachable]
        assert len(unreachable) == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On Grade 11–12 Student Kangaroo {card}, how many **positive** integers **cannot** be written in the form {m(f'{a}x + {b}y')} for nonnegative integers {m('x, y \\ge 0')}?",
            q_ar=f"في بطاقة الكانجارو للمستوى المتقدم ({idx_m})، كم عدداً صحيحاً **موجباً** لا يمكن كتابته على الصورة {m(f'{a}x + {b}y')} حيث {m('x, y \\ge 0')} عددان صحيحان غير سالبين؟",
            correct_val=ans,
            distractors=[a * b - a - b, ans + 3, max(2, ans - 2), a * b // 2],
            hint_en=f"Pair each integer {m('k')} in {m(f'[0, {a*b - a - b}]')} with {m(f'{a*b - a - b} - k')}: exact one number in every pair is representable!",
            hint_ar=f"أقرن كل عدد {m('k')} في الفترة {m(f'[0, {a*b - a - b}]')} مع {m(f'{a*b - a - b} - k')}: أحدهما فقط قابل للتمثيل!",
            idea_en=f"By Sylvester's theorem for coprime {m('a, b')}, exact {m('\\frac{(a-1)(b-1)}{2}')} positive integers are unrepresentable.",
            steps_en=[
                f"Since {m(f'\\gcd({a}, {b}) = 1')}, all unrepresentable integers lie in {m(f'\\{{0, 1, \\dots, {a*b - a - b}\\}}')}, which contains {m(str(a * b - a - b + 1))} integers.",
                f"Wait: {m(f'{a*b - a - b + 1} = (a-1)(b-1) = {(a-1)*(b-1)}')}, and pairing {m('k')} with {m(f'{a*b - a - b} - k')} makes exact half unrepresentable.",
                f"Thus there are {m(f'\\frac{{({a}-1)({b}-1)}}{{2}} = {ans}')} unreachable positive integers.",
            ],
            check_en=f"Enumerating all combinations up to {m(str(a * b))} confirms exact {m(str(ans))} missing positive integers.",
            idea_ar=f"بحسب مبرهنة سلفستر للأعداد الأولية نسبياً، عدد الأعداد الموجبة غير القابلة للتمثيل هو {m('\\frac{(a-1)(b-1)}{2}')}.",
            steps_ar=[
                f"جميع الأعداد المفقودة تقع تحت {m(f'ab - a - b = {a*b - a - b}')}.",
                f"بإقران {m('k')} مع {m(f'{a*b - a - b} - k')} نجد أن نصف القيم الممكنة بالضبط غير قابلة للتمثيل: {m(f'\\frac{{({a}-1)({b}-1)}}{{2}} = {ans}')}.",
            ],
            check_ar=f"فحص القيم الموجبة حتى {m(str(a * b))} يؤكد وجود {m(str(ans))} أعداد غير قابلة للتمثيل بالضبط.",
            diagram_en=svg_number_strip(["1, 2..", f"{a}x+{b}y", "Gaps=?"]),
        ))

    hard_frob = [
        (3, 5, 107),
        (4, 7, 150),
        (5, 8, 213),
        (6, 11, 271),
        (7, 9, 310),
    ]
    for idx_h, (a, b, n_val) in enumerate(hard_frob, 1):
        sols = [(x, (n_val - a * x) // b) for x in range(n_val // a + 1) if (n_val - a * x) % b == 0]
        ans = len(sols)
        assert ans >= 3
        x0 = sols[0][0]
        x_last = sols[-1][0]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo Diophantine round (#{idx_h}), how many ordered pairs {m('(x, y)')} of **nonnegative** integers ({m('x \\ge 0, y \\ge 0')}) satisfy {m(f'{a}x + {b}y = {n_val}')}?",
            q_ar=f"في مسألة ديفونتية من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، كم زوجاً مرتباً {m('(x, y)')} من الأعداد الصحيحة **غير السالبة** ({m('x \\ge 0, y \\ge 0')}) يحقق المعادلة {m(f'{a}x + {b}y = {n_val}')}؟",
            correct_val=ans,
            distractors=[ans - 1, ans + 1, ans + 2, max(1, ans - 2)],
            hint_en=f"Find the smallest {m('x_0 \\ge 0')} with {m(f'{a}x_0 \\equiv {n_val} \\pmod{{{b}}}')}, then step {m('x')} upward by multiples of {m(str(b))} while {m(f'{a}x \\le {n_val}')}.",
            hint_ar=f"أوجد أصغر قيمة {m('x_0 \\ge 0')} تحقق {m(f'{a}x_0 \\equiv {n_val} \\pmod{{{b}}}')} ثم زد {m('x')} بمقدار {m(str(b))} طالما {m(f'{a}x \\le {n_val}')}.",
            idea_en=f"Since {m(f'\\gcd({a}, {b}) = 1')}, solutions occur at {m(f'x = {x0} + {b}t')} for nonnegative integers {m('t')} up to {m(f'x \\le \\lfloor {n_val}/{a} \\rfloor')}.",
            steps_en=[
                f"Reduce modulo {m(str(b))}: {m(f'{a}x \\equiv {n_val} \\equiv {n_val % b} \\pmod{{{b}}}')}, giving smallest nonnegative {m(f'x_0 = {x0}')}.",
                f"General nonnegative solution has {m(f'x = {x0} + {b}t')} with {m(f'{x0} + {b}t \\le {n_val // a}')}, so {m(f'0 \\le t \\le {(x_last - x0) // b}')}.",
                f"Counting {m(f't = 0, 1, \\dots, {ans - 1}')} yields {m(str(ans))} pairs.",
            ],
            check_en=f"First pair {m(f'({sols[0][0]}, {sols[0][1]})')} and last pair {m(f'({sols[-1][0]}, {sols[-1][1]})')} both give {m(str(n_val))}, with {m(str(ans))} steps in total.",
            idea_ar=f"بما أن {m(f'\\gcd({a}, {b}) = 1')} فإن قيم {m('x')} تتزايد بخطوة مقدارها {m(str(b))} بدءاً من {m(f'x_0 = {x0}')}.",
            steps_ar=[
                f"من التطابق بالمقياس {m(str(b))} نجد أصغر حل غير سالب {m(f'x_0 = {x0}')}.",
                f"تكتب جميع الحلول على الصورة {m(f'x = {x0} + {b}t')} بشرط {m(f'{a}x \\le {n_val}')} أي {m(f'0 \\le t \\le {ans - 1}')}.",
                f"عدد الأزواج غير السالبة يساوي {m(str(ans))}.",
            ],
            check_ar=f"من {m(f'({sols[0][0]}, {sols[0][1]})')} إلى {m(f'({sols[-1][0]}, {sols[-1][1]})')} يوجد {m(str(ans))} حلول صحيحة غير سالبة.",
            diagram_en=svg_function_machine("(x,y)", f"{a}x+{b}y", f"= {n_val}", "# = ?"),
        ))

    # ------------------------------------------------------------------
    # 3. kang_stu_diff_squares_diophantine (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_diff_squares_diophantine"
    easy_dsq = [45, 80, 105, 144, 168]
    for idx_e, N in enumerate(easy_dsq, 1):
        sols = [
            ((N // d + d) // 2, (N // d - d) // 2)
            for d in range(1, math.isqrt(N) + 1)
            if N % d == 0 and d < N // d and (d + N // d) % 2 == 0
        ]
        brute = [(x, y) for y in range(1, N) for x in [math.isqrt(N + y * y)] if x * x - y * y == N]
        assert sorted(sols) == sorted(brute)
        ans = len(sols)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo worksheet #{idx_e}, how many ordered pairs {m('(x, y)')} of **positive integers** satisfy {m(f'x^2 - y^2 = {N}')}?",
            q_ar=f"في ورقة عمل الكانجارو للمستوى المتقدم ({idx_e})، كم زوجاً مرتباً {m('(x, y)')} من **الأعداد الصحيحة الموجبة** يحقق المعادلة {m(f'x^2 - y^2 = {N}')}؟",
            correct_val=ans,
            distractors=[ans + 2, max(1, ans - 1), ans + 1, ans * 2],
            hint_en=f"Factor {m(f'(x - y)(x + y) = {N}')} and count factor pairs {m('d_1 < d_2')} of {m(str(N))} that have the **same parity**.",
            hint_ar=f"حلّل إلى {m(f'(x - y)(x + y) = {N}')} وعدّ أزواج القواسم {m('d_1 < d_2')} التي لها **نفس الزوجية**.",
            idea_en=f"Positive integers {m('x, y')} correspond bijectively to factorizations {m(f'{N} = d_1 d_2')} with {m('1 \\le d_1 < d_2')} and {m('d_1 \\equiv d_2 \\pmod{2}')}.",
            steps_en=[
                f"Write {m(f'(x - y)(x + y) = {N}')} and set {m('d_1 = x - y')}, {m('d_2 = x + y')}.",
                f"For {m('x = (d_2 + d_1)/2')} and {m('y = (d_2 - d_1)/2')} to be positive integers, {m('d_1 < d_2')} must share the same parity.",
                f"Testing divisors of {m(str(N))} yields exact {m(str(ans))} valid pairs.",
            ],
            check_en=f"Solutions {m('(x, y)')}: {', '.join(m(f'({u},{v})') for u, v in sols)}.",
            idea_ar=f"كل زوج {m('d_1 < d_2')} من قواسم {m(str(N))} لهما نفس الزوجية يعطي حلاً موجباً وحيداً.",
            steps_ar=[
                f"نحلّل {m(f'(x - y)(x + y) = {N}')}.",
                f"يشترط لكون {m('x, y')} عددين صحيحين موجبين أن يكون {m('d_1 < d_2')} من نفس الزوجية.",
                f"نجد بالضبط {m(str(ans))} أزواج مرتبة.",
            ],
            check_ar=f"الحلول الموجبة هي {', '.join(m(f'({u},{v})') for u, v in sols)}.",
            diagram_en=svg_subdivided_rect_2x2("x−y", "x+y", f"= {N}", "# = ?"),
        ))

    med_dsq = [96, 120, 135, 160, 224]
    for idx_m, N in enumerate(med_dsq, 1):
        brute = [(x, y) for y in range(1, N) for x in [math.isqrt(N + y * y)] if x * x - y * y == N]
        bx, by = min(brute, key=lambda t: t[0])
        mx_x = max(u for u, _ in brute)
        ans = bx
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Grade 11–12 Student Kangaroo contest problem (#{idx_m}), positive integers {m('x')} and {m('y')} satisfy {m(f'x^2 - y^2 = {N}')}. What is the **smallest** possible value of {m('x')}?",
            q_ar=f"في مسألة من مسابقة الكانجارو للمستوى المتقدم ({idx_m})، يحقق العددان الصحيحان الموجبان {m('x')} و{m('y')} المعادلة {m(f'x^2 - y^2 = {N}')}. ما **أصغر** قيمة ممكنة للعدد {m('x')}؟",
            correct_val=ans,
            distractors=[mx_x, ans + 2, ans - 1, ans + 4],
            hint_en=f"Since {m('x = (d_1 + d_2)/2')}, choose the closest same-parity factor pair {m('d_1 < d_2')} of {m(str(N))}.",
            hint_ar=f"بما أن {m('x = (d_1 + d_2)/2')}، اختر أقرب قاسمين {m('d_1 < d_2')} للعدد {m(str(N))} يشتركان في الزوجية.",
            idea_en=f"Minimize {m('x = \\frac{d_1 + d_2}{2}')} by choosing same-parity factors {m('d_1 < d_2')} of {m(str(N))} closest to {m(f'\\sqrt{{{N}}}')}.",
            steps_en=[
                f"Factor {m(f'(x - y)(x + y) = {N}')} into same-parity integers {m('d_1 < d_2')}.",
                f"The closest valid pair is {m(f'({bx - by}, {bx + by})')}, giving {m(f'x = ({bx - by} + {bx + by})/2 = {ans}')} and {m(f'y = {by}')}.",
            ],
            check_en=f"Check {m(f'{ans}^2 - {by}^2 = {ans*ans} - {by*by} = {N}')}, and no smaller integer {m(f'x > \\sqrt{{{N}}}')} yields a square {m('x^2 - ' + str(N))}.",
            idea_ar=f"لتصغير {m('x = (d_1 + d_2)/2')} نختار أقرب قاسمين متساويي الزوجية للعدد {m(str(N))}.",
            steps_ar=[
                f"نكتب {m(f'(x - y)(x + y) = {N}')}.",
                f"أقرب قاسمين بنفس الزوجية هما {m(str(bx - by))} و{m(str(bx + by))}، ومنهما {m(f'x = {ans}')} و{m(f'y = {by}')}.",
            ],
            check_ar=f"التحقق: {m(f'{ans}^2 - {by}^2 = {ans*ans} - {by*by} = {N}')} وهي أصغر قيمة صحيحة موجبة لـ {m('x')}.",
            diagram_en=svg_subdivided_rect_2x2("x²", "−y²", f"= {N}", "min x=?"),
        ))

    hard_dsq = [
        (2, 60),
        (3, 36),
        (4, 104),
        (4, 176),
        (3, 231),
    ]
    for idx_h, (k, M) in enumerate(hard_dsq, 1):
        P = M + k * k
        sols = [
            ((P // d + d) // 2 - k, (P // d - d) // 2)
            for d in range(1, math.isqrt(P) + 1)
            if P % d == 0 and d < P // d and (d + P // d) % 2 == 0 and (P // d + d) // 2 - k >= 1
        ]
        brute = [
            (x, y)
            for x in range(1, P + 1)
            for y in [math.isqrt(x * x + 2 * k * x - M) if x * x + 2 * k * x - M > 0 else 0]
            if y >= 1 and x * x + 2 * k * x - y * y == M
        ]
        assert sorted(sols) == sorted(brute)
        ans = len(sols)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo algebra-number round (#{idx_h}), how many ordered pairs {m('(x, y)')} of **positive integers** satisfy {m(f'x^2 + {2*k}x - y^2 = {M}')}?",
            q_ar=f"في جولة الكانجارو للمستوى المتقدم من فئة ٥ نقاط ({idx_h})، كم زوجاً مرتباً {m('(x, y)')} من **الأعداد الصحيحة الموجبة** يحقق المعادلة {m(f'x^2 + {2*k}x - y^2 = {M}')}؟",
            correct_val=ans,
            distractors=[ans + 1, ans + 2, max(1, ans - 1), ans + 3],
            hint_en=f"Add {m(f'{k}^2 = {k*k}')} to both sides to complete the square {m(f'(x + {k})^2 - y^2 = {P}')}, then check {m('x \\ge 1')} and {m('y \\ge 1')}.",
            hint_ar=f"أضف {m(f'{k}^2 = {k*k}')} للطرفين لإكمال المربع {m(f'(x + {k})^2 - y^2 = {P}')} ثم تحقق من الشرطين {m('x, y \\ge 1')}.",
            idea_en=f"Complete the square on {m('x')} to obtain {m(f'(x + {k} - y)(x + {k} + y) = {P}')}.",
            steps_en=[
                f"Add {m(str(k * k))} to both sides: {m(f'(x + {k})^2 - y^2 = {M} + {k*k} = {P}')}.",
                f"Factor {m(f'{P} = d_1 d_2')} with {m('1 \\le d_1 < d_2')} of the same parity, giving {m(f'x = \\frac{{d_1 + d_2}}{{2}} - {k}')} and {m('y = \\frac{d_2 - d_1}{2}')}.",
                f"Enforcing {m('x \\ge 1')} and {m('y \\ge 1')} leaves exact {m(str(ans))} positive integer pairs.",
            ],
            check_en=f"Valid positive pairs {m('(x, y)')}: {', '.join(m(f'({u},{v})') for u, v in sols)}.",
            idea_ar=f"نكمل المربع لنحصل على فرق مربعين {m(f'(x + {k})^2 - y^2 = {P}')} ثم نفحص القواسم متساوية الزوجية.",
            steps_ar=[
                f"بإضافة {m(str(k * k))} للطرفين: {m(f'(x + {k} - y)(x + {k} + y) = {P}')}.",
                f"نختار أزواج القواسم {m('d_1 < d_2')} ذات الزوجية المتطابقة التي تحقق {m(f'(d_1 + d_2)/2 > {k}')}.",
                f"ينتج بالضبط {m(str(ans))} أزواج موجبة.",
            ],
            check_ar=f"الأزواج المقبولة هي {', '.join(m(f'({u},{v})') for u, v in sols)} وعددها {m(str(ans))}.",
            diagram_en=svg_subdivided_rect_2x2("x²", f"+{2*k}x", "−y²", f"= {M}"),
        ))

    # ------------------------------------------------------------------
    # 4. kang_stu_base_b_digit_arithmetic (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_base_b_digit_arithmetic"
    easy_base = [
        (250, 3),
        (341, 4),
        (620, 5),
        (511, 6),
        (800, 7),
    ]
    for idx_e, (N, b) in enumerate(easy_base, 1):
        digs = _to_base_digits(N, b)
        assert sum(d * (b ** (len(digs) - 1 - i)) for i, d in enumerate(digs)) == N
        ans = sum(digs)
        rep_str = "".join(str(d) for d in digs)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Student Kangaroo base-numeral card (#{idx_e}), the base-10 integer {m(str(N))} is converted into base {m(str(b))}. What is the **sum of its digits** in base {m(str(b))}?",
            q_ar=f"في بطاقة أنظمة العدّ بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، حُوِّل العدد العشري {m(str(N))} إلى النظام ذي الأساس {m(str(b))}. ما **مجموع أرقامه** في الأساس {m(str(b))}؟",
            correct_val=ans,
            distractors=[ans + 2, max(2, ans - 2), len(digs), ans + 3],
            hint_en=f"Repeatedly divide {m(str(N))} by {m(str(b))} and add all remainders.",
            hint_ar=f"اقسم العدد {m(str(N))} تكراراً على {m(str(b))} واجمع البواقي الناتجة.",
            idea_en=f"Repeated division by {m(str(b))} extracts the base-{m(str(b))} digits from least to most significant.",
            steps_en=[
                f"Expanding {m(str(N))} in powers of {m(str(b))} gives {m(f'{N} = ({rep_str})_{{{b}}}')}.",
                f"Sum the digits: {m(' + '.join(str(d) for d in digs) + f' = {ans}')}.",
            ],
            check_en=f"Verify {m(' + '.join(f'{d}\\cdot {b}^{{{len(digs)-1-i}}}' for i, d in enumerate(digs)) + f' = {N}')}.",
            idea_ar=f"القسمة المتكررة على {m(str(b))} تعطي أرقام التمثيل في الأساس {m(str(b))}.",
            steps_ar=[
                f"التمثيل في الأساس {m(str(b))} هو {m(f'({rep_str})_{{{b}}}')}.",
                f"مجموع الأرقام يساوي {m(' + '.join(str(d) for d in digs) + f' = {ans}')}.",
            ],
            check_ar=f"إعادة التركيب بقوى الأساس {m(str(b))} تعيد العدد {m(str(N))} بالضبط.",
            diagram_en=svg_function_machine(str(N), f"base {b}", "Σ dig", "?"),
        ))

    med_base = [
        (2, 3, 4, 94),
        (3, 1, 5, 159),
        (1, 5, 4, 108),
        (2, 4, 7, 205),
        (3, 2, 8, 393),
    ]
    for idx_m, (d2, d1, d0, N) in enumerate(med_base, 1):
        cands = [b for b in range(max(d2, d1, d0) + 1, 200) if d2 * b * b + d1 * b + d0 == N]
        assert len(cands) == 1
        ans = cands[0]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Grade 11–12 Student Kangaroo puzzle (#{idx_m}), the three-digit base-{m('b')} numeral {m(f'({d2}{d1}{d0})_b')} equals {m(str(N))} in base {m('10')}. What is the base {m('b')}?",
            q_ar=f"في لغز الكانجارو للمستوى المتقدم ({idx_m})، العدد المكون من ثلاثة أرقام {m(f'({d2}{d1}{d0})_b')} في الأساس {m('b')} يساوي {m(str(N))} في النظام العشري. ما قيمة الأساس {m('b')}؟",
            correct_val=ans,
            distractors=[ans + 1, ans - 1, ans + 2, ans + 3],
            hint_en=f"Expand {m(f'{d2}b^2 + {d1}b + {d0} = {N}')} with integer {m(f'b > {max(d2, d1, d0)}')}.",
            hint_ar=f"فكّ التمثيل المكانـي {m(f'{d2}b^2 + {d1}b + {d0} = {N}')} مع شرط {m(f'b > {max(d2, d1, d0)}')}.",
            idea_en=f"Convert place-value notation into the quadratic {m(f'{d2}b^2 + {d1}b - {N - d0} = 0')}.",
            steps_en=[
                f"Write {m(f'{d2}b^2 + {d1}b + {d0} = {N}')}, so {m(f'b({d2}b + {d1}) = {N - d0}')}.",
                f"Testing divisors of {m(str(N - d0))} with {m(f'b > {max(d2, d1, d0)}')} uniquely gives {m(f'b = {ans}')}.",
            ],
            check_en=f"Substitute {m(f'b = {ans}')}: {m(f'{d2}({ans}^2) + {d1}({ans}) + {d0} = {d2*ans*ans} + {d1*ans} + {d0} = {N}')}.",
            idea_ar=f"نفكّ القيمة المكانية إلى {m(f'b({d2}b + {d1}) = {N - d0}')} ونبحث عن القاسم الموجب المناسب.",
            steps_ar=[
                f"المعادلة هي {m(f'{d2}b^2 + {d1}b + {d0} = {N}')} أي {m(f'b({d2}b + {d1}) = {N - d0}')}.",
                f"القيمة الوحيدة التي تحقق {m(f'b > {max(d2, d1, d0)}')} هي {m(f'b = {ans}')}.",
            ],
            check_ar=f"بالتعويض: {m(f'{d2}({ans}^2) + {d1}({ans}) + {d0} = {N}')}، صحيح.",
            diagram_en=svg_digit_slots([str(d2), str(d1), str(d0)], "base b=?"),
        ))

    # Hard 4.1..4.4: Dual-base palindromes; 4.5: Base-(b+1) alternating divisibility
    dual_pal_specs = [
        (2, 10, 10, 100, "sum", "What is the **sum** of all two-digit base-10 integers (from 10 to 99) that are palindromes in **both** base 10 and base 2?",
         "ما **مجموع** جميع الأعداد الصحيحة المكونة من رقمين في النظام العشري (من ١٠ إلى ٩٩) التي تُقرأ كمتناظر (Palindrome) في **كلٍّ من** الأساس ١٠ والأساس ٢؟"),
        (4, 10, 10, 99, "unique", "A two-digit base-10 integer (between 10 and 99) is a palindrome in **both** base 10 and base 4. What is this integer?",
         "عدد صحيح مكوّن من رقمين في النظام العشري (بين ١٠ و٩٩) يمثّل عدداً متناظراً في **كلٍّ من** الأساس ١٠ والأساس ٤. ما هذا العدد؟"),
        (5, 10, 10, 99, "unique", "A two-digit base-10 integer (between 10 and 99) is a palindrome in **both** base 10 and base 5. What is this integer?",
         "عدد صحيح مكوّن من رقمين في النظام العشري (بين ١٠ و٩٩) يمثّل عدداً متناظراً في **كلٍّ من** الأساس ١٠ والأساس ٥. ما هذا العدد؟"),
        (3, 10, 100, 200, "sum", "What is the **sum** of all integers between 100 and 200 inclusive that are palindromes in **both** base 10 and base 3?",
         "ما **مجموع** جميع الأعداد الصحيحة بين ١٠٠ و٢٠٠ ضمناً التي تمثّل أعداداً متناظرة في **كلٍّ من** الأساس ١٠ والأساس ٣؟"),
    ]
    for idx_h, (b_other, _, lo, hi, mode, q_body_en, q_body_ar) in enumerate(dual_pal_specs, 1):
        pals = [
            n for n in range(lo, hi + 1)
            if _to_base_digits(n, b_other) == _to_base_digits(n, b_other)[::-1]
            and _to_base_digits(n, 10) == _to_base_digits(n, 10)[::-1]
        ]
        assert len(pals) >= 1
        ans = sum(pals) if mode == "sum" else pals[0]
        if mode == "unique":
            assert len(pals) == 1
        pal_desc = ", ".join(f"{n} = ({''.join(str(x) for x in _to_base_digits(n, b_other))})_{b_other}" for n in pals)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo dual-base challenge (#{idx_h}): {q_body_en}",
            q_ar=f"في تحدي الكانجارو للمستوى المتقدم من فئة ٥ نقاط ({idx_h}): {q_body_ar}",
            correct_val=ans,
            distractors=[ans + 11, max(11, ans - 11), ans + 22, max(22, ans - 22)],
            hint_en=f"List the base-10 palindromes in {m(f'[{lo}, {hi}]')} and test their base-{m(str(b_other))} expansions.",
            hint_ar=f"احصر الأعداد المتناظرة عشرياً في الفترة {m(f'[{lo}, {hi}]')} واختبر تمثيلها في الأساس {m(str(b_other))}.",
            idea_en=f"There are very few base-10 palindromes in {m(f'[{lo}, {hi}]')}, making base-{m(str(b_other))} filtering fast and exact.",
            steps_en=[
                f"Test base-10 palindromes in {m(f'[{lo}, {hi}]')} by converting each to base {m(str(b_other))}.",
                f"The matching dual-base palindrome(s): {pal_desc}, giving answer {m(str(ans))}.",
            ],
            check_en=f"Full scan of {m(f'[{lo}, {hi}]')} confirms {m(str(pals))} as the complete dual-base palindrome set.",
            idea_ar=f"نفحص الأعداد المتناظرة في النظام العشري ضمن الفترة {m(f'[{lo}, {hi}]')} ونحوّلها إلى الأساس {m(str(b_other))}.",
            steps_ar=[
                f"الأعداد المتناظرة عشرياً قليلة العدد في الفترة {m(f'[{lo}, {hi}]')}.",
                f"القيم التي تبقى متناظرة في الأساس {m(str(b_other))} تعطي النتيجة {m(str(ans))}.",
            ],
            check_ar=f"الفحص الشامل للفترة يؤكد أن النتيجة الصحيحة هي {m(str(ans))}.",
            diagram_en=svg_digit_slots(["d", "...", "d"], f"b=10,{b_other}"),
        ))

    # Hard 4.5: Base-11 divisibility by 12 (b + 1 alternating sum rule)
    b_div = 11
    valid_d = [
        d for d in range(b_div)
        if (4 * b_div**4 + 7 * b_div**3 + d * b_div**2 + 3 * b_div + 5) % (b_div + 1) == 0
    ]
    assert valid_d == [1]
    ans_d = valid_d[0]
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
        q_en=f"On a 5-point Student Kangaroo numeral puzzle, the five-digit base-{m('11')} integer {m('(47d35)_{11}')} (where {m('0 \\le d \\le 10')}) is divisible by {m('12')}. What is the digit {m('d')}?",
        q_ar=f"في لغز أنظمة عدّ من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم، يقبل العدد المكوّن من خمسة أرقام في الأساس {m('11')} وهو {m('(47d35)_{11}')} (حيث {m('0 \\le d \\le 10')}) القسمة على {m('12')}. ما قيمة الرقم {m('d')}؟",
        correct_val=ans_d,
        distractors=[5, 7, 9, 3],
        hint_en=f"Since {m('11 \\equiv -1 \\pmod{12}')}, use the alternating-sum test modulo {m('b + 1 = 12')}.",
        hint_ar=f"بما أن {m('11 \\equiv -1 \\pmod{12}')}، طبّق قاعدة المجموع المتناوب للأرقام بالمقياس {m('12')}.",
        idea_en=f"In base {m('b')}, {m('b \\equiv -1 \\pmod{b+1}')}, so a numeral is divisible by {m('b+1')} iff its alternating digit sum is divisible by {m('b+1')}.",
        steps_en=[
            f"Reduce modulo {m('12')}: {m('(47d35)_{11} \\equiv 4(-1)^4 + 7(-1)^3 + d(-1)^2 + 3(-1) + 5 \\pmod{12}')}.",
            f"Simplify: {m('4 - 7 + d - 3 + 5 = d - 1 \\equiv 0 \\pmod{12}')}.",
            f"Since {m('0 \\le d \\le 10')}, the unique digit is {m('d = 1')}.",
        ],
        check_en=f"At {m('d = 1')}, {m('4(14641) + 7(1331) + 1(121) + 33 + 5 = 68040 = 12 \\times 5670')}.",
        idea_ar=f"في الأساس {m('b')} يكون {m('b \\equiv -1 \\pmod{b+1}')} فنستخدم المجموع المتناوب للأرقام.",
        steps_ar=[
            f"بالمقياس {m('12')}: {m('4 - 7 + d - 3 + 5 = d - 1 \\equiv 0 \\pmod{12}')}.",
            f"وبما أن {m('0 \\le d \\le 10')} فإن {m('d = 1')} هو الحل الوحيد.",
        ],
        check_ar=f"عند {m('d = 1')} تصبح القيمة العشرية {m('68040 = 12 \\times 5670')} وتقبل القسمة على {m('12')}.",
        diagram_en=svg_digit_slots(["4", "7", "?", "3", "5"], "mod 12=0"),
    ))

    return items


# ==============================================================================
# UNIT 5.2 — ALGEBRA (60 Questions: KANG-STU-061 .. KANG-STU-120)
# ==============================================================================
def _unit_5_2_algebra(offset: int = 60) -> list[dict]:
    items: list[dict] = []
    topic = "Algebra"

    # ------------------------------------------------------------------
    # 5. kang_stu_cubic_vieta_symmetric (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_cubic_vieta_symmetric"
    easy_cub = [
        (6, 7, 1),
        (7, 11, 3),
        (8, 14, 5),
        (9, 18, 7),
        (10, 23, 11),
    ]
    for idx_e, (p, q, w) in enumerate(easy_cub, 1):
        rts = _cubic_real_roots(p, q, w)
        ans = p * p - 2 * q
        assert abs(sum(r * r for r in rts) - ans) < 1e-6
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Grade 11–12 Student Kangaroo algebra sheet (#{idx_e}), the cubic equation {m(f'x^3 - {p}x^2 + {q}x - {w} = 0')} has three real roots {m('r, s, t')}. What is the value of {m('r^2 + s^2 + t^2')}?",
            q_ar=f"في ورقة الجبر بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، للمعادلة التكعيبية {m(f'x^3 - {p}x^2 + {q}x - {w} = 0')} ثلاثة جذور حقيقية {m('r, s, t')}. ما قيمة {m('r^2 + s^2 + t^2')}؟",
            correct_val=ans,
            distractors=[p * p - q, p * p + 2 * q, ans - 4, ans + 4],
            hint_en=f"Use Vieta's relations {m(f'r + s + t = {p}')} and {m(f'rs + st + tr = {q}')} in {m('(r + s + t)^2 - 2(rs + st + tr)')}.",
            hint_ar=f"استخدم علاقتي فييتا {m(f'r + s + t = {p}')} و{m(f'rs + st + tr = {q}')} في المتطابقة {m('(r + s + t)^2 - 2(rs + st + tr)')}.",
            idea_en=f"By Vieta's formulas, {m('r^2 + s^2 + t^2 = (r + s + t)^2 - 2(rs + st + tr)')}.",
            steps_en=[
                f"Read off {m(f'r + s + t = {p}')} and {m(f'rs + st + tr = {q}')}.",
                f"Compute {m(f'{p}^2 - 2({q}) = {p*p} - {2*q} = {ans}')}.",
            ],
            check_en=f"Notice {m(f'r^2 + s^2 + t^2 = {ans} > 0')}, confirming three real roots exist.",
            idea_ar=f"من صيغ فييتا نحسب {m('(r + s + t)^2 - 2(rs + st + tr)')} مباشرة دون إيجاد الجذور فردياً.",
            steps_ar=[
                f"لدينا {m(f'r + s + t = {p}')} و{m(f'rs + st + tr = {q}')}.",
                f"إذن {m(f'r^2 + s^2 + t^2 = {p}^2 - 2({q}) = {ans}')}.",
            ],
            check_ar=f"التعويض العددي بالجذور الحقيقية الثلاثة يحقق {m(f'r^2 + s^2 + t^2 = {ans}')} تماماً.",
            diagram_en=svg_number_strip([f"Σr={p}", f"Σrs={q}", "Σr²=?"]),
        ))

    med_cub = [
        (5, 3, -2, 2),
        (6, 8, 2, 1),
        (7, 10, 2, 2),
        (8, 15, 6, 1),
        (9, 20, 10, 2),
    ]
    for idx_m, (p, q, w, k) in enumerate(med_cub, 1):
        rts = _cubic_real_roots(p, q, w)
        ans = (k ** 3) + p * (k ** 2) + q * k + w
        prod_num = math.prod(r + k for r in rts)
        assert abs(prod_num - ans) < 1e-6
        const_s = f"- {w}" if w > 0 else f"+ {-w}"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Student Kangaroo round #{idx_m}, let {m('r, s, t')} be the three real roots of {m(f'P(x) = x^3 - {p}x^2 + {q}x {const_s} = 0')}. What is the value of {m(f'(r + {k})(s + {k})(t + {k})')}?",
            q_ar=f"في جولة الكانجارو للمستوى المتقدم ({idx_m})، لتكن {m('r, s, t')} الجذور الحقيقية الثلاثة لكثيرة الحدود {m(f'P(x) = x^3 - {p}x^2 + {q}x {const_s} = 0')}. ما قيمة الجداء {m(f'(r + {k})(s + {k})(t + {k})')}؟",
            correct_val=ans,
            distractors=[ans - 2 * w if w != 0 else ans - 4, ans + k * q, ans - p * k * k, ans + 6],
            hint_en=f"Factor {m('P(x) = (x - r)(x - s)(x - t)')} and substitute {m(f'x = -{k}')}, noting {m(f'P(-{k}) = -({k}+r)({k}+s)({k}+t)')}.",
            hint_ar=f"اكتب {m('P(x) = (x - r)(x - s)(x - t)')} وعوّض {m(f'x = -{k}')} مع ملاحظة إشارة الطرفين.",
            idea_en=f"Since {m('P(x) = (x - r)(x - s)(x - t)')}, evaluating at {m(f'x = -{k}')} gives {m(f'(r + {k})(s + {k})(t + {k}) = -P(-{k})')}.",
            steps_en=[
                f"Evaluate {m(f'P(-{k}) = (-{k})^3 - {p}(-{k})^2 + {q}(-{k}) {const_s} = {-ans}')}.",
                f"Negate to flip all three signs: {m(f'(r + {k})(s + {k})(t + {k}) = -P(-{k}) = {ans}')}.",
            ],
            check_en=f"Expanding via Vieta {m(f'{k}^3 + {p}({k}^2) + {q}({k}) + ({w}) = {ans}')} matches identically.",
            idea_ar=f"من التحليل {m('P(x) = (x - r)(x - s)(x - t)')} نجد مباشرة أن {m(f'(r + {k})(s + {k})(t + {k}) = -P(-{k})')}.",
            steps_ar=[
                f"نحسب {m(f'P(-{k}) = {-ans}')}.",
                f"نضرب في {m('-1')} لعكس إشارات العوامل الثلاثة فنحصل على {m(str(ans))}.",
            ],
            check_ar=f"الفك المباشر بصيغ فييتا يعطي {m(f'{k**3} + {p*k*k} + {q*k} + ({w}) = {ans}')}.",
            diagram_en=svg_function_machine("P(x)=0", f"x = −{k}", "−P(−k)", "?"),
        ))

    hard_cub = [
        (4, 1, -3),
        (5, 4, -1),
        (6, 5, -2),
        (7, 12, 4),
        (8, 13, 3),
    ]
    for idx_h, (p, q, w) in enumerate(hard_cub, 1):
        rts = _cubic_real_roots(p, q, w)
        ans = (p ** 3) - 3 * p * q + 3 * w
        assert abs(sum(r ** 3 for r in rts) - ans) < 1e-5
        const_s = f"- {w}" if w > 0 else f"+ {-w}"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo final card (#{idx_h}), let {m('r, s, t')} be the roots of {m(f'x^3 - {p}x^2 + {q}x {const_s} = 0')}. What is the exact value of {m('r^3 + s^3 + t^3')}?",
            q_ar=f"في مسألة ختامية من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، لتكن {m('r, s, t')} جذور المعادلة {m(f'x^3 - {p}x^2 + {q}x {const_s} = 0')}. ما القيمة الدقيقة للمقدار {m('r^3 + s^3 + t^3')}؟",
            correct_val=ans,
            distractors=[p ** 3 - 3 * p * q, ans - 3 * w if w != 0 else ans - 6, ans + 6, p ** 3],
            hint_en=f"Each root satisfies {m(f'x^3 = {p}x^2 - {q}x + ({w})')}; sum this identity over {m('x = r, s, t')}!",
            hint_ar=f"يحقق كل جذر العلاقة {m(f'x^3 = {p}x^2 - {q}x + ({w})')}؛ اجمع هذه المعادلة على الجذور الثلاثة!",
            idea_en=f"Summing {m(f'x^3 = {p}x^2 - {q}x + ({w})')} over the three roots yields Newton's cubic sum {m('p^3 - 3pq + 3w')}.",
            steps_en=[
                f"By Vieta, {m(f'\\sum r = {p}')} and {m(f'\\sum r^2 = {p}^2 - 2({q}) = {p*p - 2*q}')}.",
                f"Sum {m(f'r^3 = {p}r^2 - {q}r + ({w})')} across all three roots: {m(f'{p}({p*p - 2*q}) - {q}({p}) + 3({w}) = {ans}')}.",
            ],
            check_en=f"Direct check via {m(f'p^3 - 3pq + 3w = {p**3} - {3*p*q} + {3*w} = {ans}')}.",
            idea_ar=f"بجمع المعادلة {m(f'x^3 = {p}x^2 - {q}x + ({w})')} على الجذور الثلاثة نختزل القوى التكعيبية إلى قوى تربيعية وخطية.",
            steps_ar=[
                f"نحسب أولاً {m(f'r^2 + s^2 + t^2 = {p}^2 - 2({q}) = {p*p - 2*q}')}.",
                f"نعوّض في المجموع: {m(f'{p}({p*p - 2*q}) - {q}({p}) + 3({w}) = {ans}')}.",
            ],
            check_ar=f"المتطابقة {m(f'p^3 - 3pq + 3w')} تعطي {m(str(ans))} بالضبط.",
            diagram_en=svg_parabola_roots("r", "s, t", "Σr³ = ?"),
        ))

    # ------------------------------------------------------------------
    # 6. kang_stu_poly_remainder_reconstruction (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_poly_remainder_reconstruction"
    easy_rem = [
        (1, 4, 5, 17, 6),
        (2, 5, 3, 18, 7),
        (-1, 3, 2, 14, 5),
        (1, 6, 4, 24, 9),
        (-2, 2, 1, 13, 6),
    ]
    for idx_e, (u, v, r1, r2, w_pt) in enumerate(easy_rem, 1):
        assert (r2 - r1) % (v - u) == 0
        a_sl = (r2 - r1) // (v - u)
        b_in = r1 - a_sl * u
        ans = a_sl * w_pt + b_in
        test_P = lambda x: (x - u) * (x - v) * (x + 5) + a_sl * x + b_in
        assert test_P(u) == r1 and test_P(v) == r2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"In a Student Kangaroo polynomial puzzle (#{idx_e}), a polynomial {m('P(x)')} leaves remainder {m(str(r1))} when divided by {m(f'x - {u}' if u >= 0 else f'x + {-u}')} and remainder {m(str(r2))} when divided by {m(f'x - {v}')}. If {m('R(x)')} is the remainder when {m('P(x)')} is divided by {m(f'(x - {u})(x - {v})' if u >= 0 else f'(x + {-u})(x - {v})')}, what is {m(f'R({w_pt})')}?",
            q_ar=f"في لغز كثيرات الحدود بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، باقي قسمة {m('P(x)')} على {m(f'x - {u}' if u >= 0 else f'x + {-u}')} هو {m(str(r1))}، وباقي قسمتها على {m(f'x - {v}')} هو {m(str(r2))}. إذا كان {m('R(x)')} هو باقي قسمة {m('P(x)')} على جدائهما، فما قيمة {m(f'R({w_pt})')}؟",
            correct_val=ans,
            distractors=[ans + a_sl, ans - a_sl, r1 + r2, ans + 3],
            hint_en=f"Write the linear remainder {m('R(x) = ax + b')} and solve {m(f'R({u}) = {r1}')}, {m(f'R({v}) = {r2}')}.",
            hint_ar=f"افرض الباقي الخطي {m('R(x) = ax + b')} وحلّ النظام {m(f'R({u}) = {r1}')} و{m(f'R({v}) = {r2}')}.",
            idea_en=f"Dividing by a quadratic leaves a remainder {m('R(x) = ax + b')} of degree at most {m('1')}, pinned down by {m(f'x = {u}, {v}')}.",
            steps_en=[
                f"From {m(f'a({u}) + b = {r1}')} and {m(f'a({v}) + b = {r2}')}, the slope is {m(f'a = ({r2} - {r1})/({v} - ({u})) = {a_sl}')}.",
                f"Then {m(f'b = {r1} - {a_sl}({u}) = {b_in}')}, so {m(f'R({w_pt}) = {a_sl}({w_pt}) + ({b_in}) = {ans}')}.",
            ],
            check_en=f"Check {m(f'R({u}) = {r1}')} and {m(f'R({v}) = {r2}')}, confirming {m(f'R({w_pt}) = {ans}')}.",
            idea_ar=f"باقي القسمة على مقدار تربيعي يكون خطياً {m('R(x) = ax + b')} ويتحدد من نقطتي التقويم.",
            steps_ar=[
                f"نحسب الميل {m(f'a = \\frac{{{r2} - {r1}}}{{{v} - ({u})}} = {a_sl}')} والثابت {m(f'b = {b_in}')}.",
                f"بالتعويض عند {m(f'x = {w_pt}')} نجد {m(f'R({w_pt}) = {ans}')}.",
            ],
            check_ar=f"التحقق عند {m(f'x = {u}, {v}')} يعطي الباقيين {m(str(r1))} و{m(str(r2))} بالضبط.",
            diagram_en=svg_function_machine(f"P({u})={r1}", f"P({v})={r2}", f"R({w_pt})", "?"),
        ))

    med_rem = [
        (1, 2, 3, 1, 0, 5),
        (2, 4, 6, 2, 0, 8),
        (1, 2, 3, 2, 1, 6),
        (-1, 0, 1, 1, 2, 4),
        (1, 3, 5, 3, -1, 7),
    ]
    for idx_m, (u1, u2, u3, sl, c0, x0) in enumerate(med_rem, 1):
        P_fn = lambda x: (x - u1) * (x - u2) * (x - u3) + sl * x + c0
        v1, v2, v3 = P_fn(u1), P_fn(u2), P_fn(u3)
        ans = P_fn(x0)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"On Grade 11–12 Student Kangaroo card #{idx_m}, a **monic** cubic polynomial {m('P(x) = x^3 + ax^2 + bx + c')} satisfies {m(f'P({u1}) = {v1}')}, {m(f'P({u2}) = {v2}')}, and {m(f'P({u3}) = {v3}')}. What is {m(f'P({x0})')}?",
            q_ar=f"في بطاقة الكانجارو للمستوى المتقدم ({idx_m})، تحقق كثيرة الحدود التكعيبية **الأحادية** {m('P(x) = x^3 + ax^2 + bx + c')} القيم {m(f'P({u1}) = {v1}')} و{m(f'P({u2}) = {v2}')} و{m(f'P({u3}) = {v3}')}. ما قيمة {m(f'P({x0})')}؟",
            correct_val=ans,
            distractors=[sl * x0 + c0, ans - (x0 - u3) * (x0 - u2), ans + 6, ans - 6],
            hint_en=f"Notice the linear pattern {m(f'P(k) = {sl}k + ({c0})')} at {m(f'k = {u1}, {u2}, {u3}')}, so {m(f'Q(x) = P(x) - ({sl}x + {c0})')} is a monic cubic with those three roots!",
            hint_ar=f"لاحظ النمط الخطي {m(f'P(k) = {sl}k + ({c0})')} عند النقاط الثلاث، فالمقدار {m(f'P(x) - ({sl}x + {c0})')} تكعيبي أحادي جذوره {m(f'{u1}, {u2}, {u3}')}!",
            idea_en=f"Define {m(f'Q(x) = P(x) - ({sl}x + {c0})')}: it is monic of degree {m('3')} and vanishes at {m(f'{u1}, {u2}, {u3}')}.",
            steps_en=[
                f"At {m(f'x = {u1}, {u2}, {u3}')}, {m(f'P(x) = {sl}x + ({c0})')}, so {m(f'P(x) - ({sl}x + {c0}) = (x - {u1})(x - {u2})(x - {u3})')}.",
                f"Substitute {m(f'x = {x0}')}: {m(f'P({x0}) = ({x0 - u1})({x0 - u2})({x0 - u3}) + {sl * x0 + c0} = {ans}')}.",
            ],
            check_en=f"Avoiding linear extrapolation trap ({m(str(sl * x0 + c0))}), the cubic root product adds {m(str((x0 - u1) * (x0 - u2) * (x0 - u3)))} to give {m(str(ans))}.",
            idea_ar=f"نطرح الدالة الخطية الموافقة للنقاط الثلاث فنحصل على {m(f'(x - {u1})(x - {u2})(x - {u3})')}.",
            steps_ar=[
                f"نكتب {m(f'P(x) = (x - {u1})(x - {u2})(x - {u3}) + {sl}x + ({c0})')}.",
                f"عند {m(f'x = {x0}')} نحصل على {m(f'P({x0}) = {(x0 - u1)*(x0 - u2)*(x0 - u3)} + {sl*x0 + c0} = {ans}')}.",
            ],
            check_ar=f"المعامل الرئيس لـ {m('P(x)')} هو {m('1')} وتتحقق القيم الثلاث المعطاة تماماً.",
            diagram_en=svg_number_strip([f"P({u1})={v1}", f"P({u2})={v2}", f"P({u3})={v3}", f"P({x0})=?"]),
        ))

    hard_rem = [
        (2, 1, 2, 3),  # u=2, h=1 -> {1,2,3}, d=2 -> P(0)+P(4), sl=3
        (3, 1, 2, 5),  # u=3, h=1 -> {2,3,4}, d=2 -> P(1)+P(5), sl=5
        (0, 1, 3, 2),  # u=0, h=1 -> {-1,0,1}, d=3 -> P(-3)+P(3), sl=2
        (2, 2, 3, 1),  # u=2, h=2 -> {0,2,4}, d=3 -> P(-1)+P(5), sl=1
        (4, 1, 3, 4),  # u=4, h=1 -> {3,4,5}, d=3 -> P(1)+P(7), sl=4
    ]
    for idx_h, (u, h_st, d_sp, sl) in enumerate(hard_rem, 1):
        vals_by_r = []
        for r_test in (-7, 0, 13):
            P_t = lambda x, rt=r_test: (x - (u - h_st)) * (x - u) * (x - (u + h_st)) * (x - rt) + sl * x
            vals_by_r.append(P_t(u - d_sp) + P_t(u + d_sp))
        assert len(set(vals_by_r)) == 1
        ans = vals_by_r[0]
        p1, p2, p3 = u - h_st, u, u + h_st
        q1, q2 = u - d_sp, u + d_sp
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo polynomial challenge (#{idx_h}), {m('P(x) = x^4 + ax^3 + bx^2 + cx + d')} is a **monic** polynomial of degree {m('4')} satisfying {m(f'P({p1}) = {sl*p1}')}, {m(f'P({p2}) = {sl*p2}')}, and {m(f'P({p3}) = {sl*p3}')}. What is the exact value of {m(f'P({q1}) + P({q2})')}?",
            q_ar=f"في تحدي كثيرات الحدود من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، {m('P(x)')} كثيرة حدود **أحادية** من الدرجة الرابعة تحقق {m(f'P({p1}) = {sl*p1}')} و{m(f'P({p2}) = {sl*p2}')} و{m(f'P({p3}) = {sl*p3}')}. ما القيمة الدقيقة للمجموع {m(f'P({q1}) + P({q2})')}؟",
            correct_val=ans,
            distractors=[sl * (q1 + q2), ans // 2, ans + 12, ans - 12],
            hint_en=f"Write {m(f'P(x) - {sl}x = (x - {p1})(x - {p2})(x - {p3})(x - r)')}; at the symmetric inputs {m(f'x = {q1}')} and {m(f'x = {q2}')}, the unknown root {m('r')} cancels out!",
            hint_ar=f"اكتب {m(f'P(x) - {sl}x = (x - {p1})(x - {p2})(x - {p3})(x - r)')}؛ عند النقطتين المتناظرتين {m(f'{q1}')} و{m(f'{q2}')} يختصر الجذر المجهول {m('r')} تماماً!",
            idea_en=f"Because {m(f'{q1}')} and {m(f'{q2}')} are symmetric about {m(str(u))}, the cubic prefix {m(f'(x - {p1})(x - {p2})(x - {p3})')} takes opposite values and cancels {m('r')}.",
            steps_en=[
                f"Factor {m(f'P(x) = (x - {p1})(x - {p2})(x - {p3})(x - r) + {sl}x')}.",
                f"At {m(f'x = {q2}')} the first three factors multiply to {m(str(d_sp * (d_sp**2 - h_st**2)))}; at {m(f'x = {q1}')} they multiply to {m(str(-d_sp * (d_sp**2 - h_st**2)))}.",
                f"Adding gives {m(f'{d_sp*(d_sp**2 - h_st**2)}(({q2} - r) - ({q1} - r)) + {sl}({q1} + {q2}) = {ans}')}.",
            ],
            check_en=f"Setting {m('r = 0')} or {m('r = 13')} yields the identical sum {m(str(ans))}.",
            idea_ar=f"بفضل التناظر حول {m(str(u))} يأخذ الجداء الثلاثي إشارتين متعاكستين عند {m(str(q1))} و{m(str(q2))} فيختفي {m('r')}.",
            steps_ar=[
                f"نضع {m(f'P(x) = (x - {p1})(x - {p2})(x - {p3})(x - r) + {sl}x')}.",
                f"بجمع {m(f'P({q1}) + P({q2})')} تلغى الحدود المحتوية على {m('r')} ويبقى {m(str(ans))}.",
            ],
            check_ar=f"اختبار أي قيمة لـ {m('r')} يعطي دائماً نفس المجموع الثابت {m(str(ans))}.",
            diagram_en=svg_number_strip([f"P({q1})", f"P({u})", f"P({q2})", "Sum=?"]),
        ))

    # ------------------------------------------------------------------
    # 7. kang_stu_functional_involution_eq (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_functional_involution_eq"
    easy_feq = [
        (2, 1, 5, 3, 0, 4),
        (3, 1, 6, 4, 0, 5),
        (2, -1, 8, 3, 0, 6),
        (3, 2, 7, 5, 0, 5),
        (4, 1, 10, 3, 0, 8),
    ]
    for idx_e, (a, b, c_sh, m_sl, d0, x0) in enumerate(easy_feq, 1):
        g = lambda x: m_sl * x + d0
        f_exact = lambda x: Fraction(a * g(x) - b * g(c_sh - x), a * a - b * b)
        assert a * f_exact(x0) + b * f_exact(c_sh - x0) == g(x0)
        assert a * f_exact(c_sh - x0) + b * f_exact(x0) == g(c_sh - x0)
        ans = f_exact(x0)
        b_term = f"+ {b}f({c_sh} - x)" if b > 1 else (f"+ f({c_sh} - x)" if b == 1 else f"- f({c_sh} - x)")
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On a Student Kangaroo functional card (#{idx_e}), a function {m('f: \\mathbb{R} \\to \\mathbb{R}')} satisfies {m(f'{a}f(x) {b_term} = {m_sl}x')} for all real {m('x')}. What is {m(f'f({x0})')}?",
            q_ar=f"في بطاقة المعادلات الدالية بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، تحقق الدالة {m('f: \\mathbb{R} \\to \\mathbb{R}')} العلاقة {m(f'{a}f(x) {b_term} = {m_sl}x')} لكل عدد حقيقي {m('x')}. ما قيمة {m(f'f({x0})')}؟",
            correct_val=ans,
            distractors=[f_exact(c_sh - x0), ans + 2, ans - 2, Fraction(g(x0), a + b)],
            hint_en=f"Substitute {m(f'x = {x0}')} and {m(f'x = {c_sh - x0}')} to form two linear equations in {m(f'f({x0})')} and {m(f'f({c_sh - x0})')}.",
            hint_ar=f"عوّض {m(f'x = {x0}')} ثم {m(f'x = {c_sh - x0}')} لتكوين معادلتين خطيتين في {m(f'f({x0})')} و{m(f'f({c_sh - x0})')}.",
            idea_en=f"The involution {m(f'x \\mapsto {c_sh} - x')} swaps {m(str(x0))} and {m(str(c_sh - x0))}, closing a {m('2 \\times 2')} linear system.",
            steps_en=[
                f"At {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f({c_sh - x0}) = {g(x0)}')}.",
                f"At {m(f'x = {c_sh - x0}')}: {m(f'{a}f({c_sh - x0}) + ({b})f({x0}) = {g(c_sh - x0)}')}.",
                f"Eliminate {m(f'f({c_sh - x0})')}: {m(f'({a*a - b*b})f({x0}) = {a*g(x0) - b*g(c_sh - x0)} \\implies f({x0}) = {ans}')}.",
            ],
            check_en=f"With {m(f'f({x0}) = {ans}')} and {m(f'f({c_sh - x0}) = {f_exact(c_sh - x0)}')}, {m(f'{a}({ans}) + ({b})({f_exact(c_sh - x0)}) = {g(x0)}')}.",
            idea_ar=f"التحويل العكسي {m(f'x \\mapsto {c_sh} - x')} يبدّل بين {m(str(x0))} و{m(str(c_sh - x0))} فنحذف المجهول الثاني.",
            steps_ar=[
                f"نعوّض {m(f'x = {x0}')} و{m(f'x = {c_sh - x0}')} في المعادلة المعطاة.",
                f"نحذف {m(f'f({c_sh - x0})')} فنحصل على {m(f'f({x0}) = {ans}')}.",
            ],
            check_ar=f"التعويض العكسي بالقيمتين يحقق المعادلة الأصلية تماماً.",
            diagram_en=svg_function_machine(f"x={x0}", f"{c_sh}−x", "solve", f"f({x0})=?"),
        ))

    med_feq = [
        (2, 1, 6, 3, 2),
        (3, 1, 8, 4, 4),
        (2, -1, 12, 3, 3),
        (3, 2, 10, 5, 2),
        (4, 1, 15, 3, 5),
    ]
    for idx_m, (a, b, k_rec, c_mul, x0) in enumerate(med_feq, 1):
        y0 = Fraction(k_rec, x0)
        f_rec = lambda x: Fraction(a * c_mul * Fraction(x) - b * c_mul * Fraction(k_rec, x), a * a - b * b)
        assert a * f_rec(x0) + b * f_rec(y0) == c_mul * x0
        assert a * f_rec(y0) + b * f_rec(x0) == c_mul * y0
        ans = f_rec(x0)
        b_s = f"+ {b}f({k_rec}/x)" if b > 1 else (f"+ f({k_rec}/x)" if b == 1 else f"- f({k_rec}/x)")
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, a function {m('f')} defined on nonzero reals satisfies {m(f'{a}f(x) {b_s} = {c_mul}x')} for all {m('x \\ne 0')}. What is {m(f'f({x0})')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، تحقق الدالة {m('f')} المعرّفة على الأعداد الحقيقية غير الصفرية العلاقة {m(f'{a}f(x) {b_s} = {c_mul}x')} لكل {m('x \\ne 0')}. ما قيمة {m(f'f({x0})')}؟",
            correct_val=ans,
            distractors=[f_rec(y0), ans + 3, ans - 2, Fraction(c_mul * x0, a + b)],
            hint_en=f"Substitute {m(f'x = {x0}')} and {m(f'x = {y0}')} so the arguments {m('x')} and {m(f'{k_rec}/x')} swap places.",
            hint_ar=f"عوّض {m(f'x = {x0}')} ثم {m(f'x = {y0}')} لتتبادل المدخلات {m('x')} و{m(f'{k_rec}/x')}.",
            idea_en=f"Pair {m(f'x = {x0}')} with its reciprocal partner {m(f'{k_rec}/{x0} = {y0}')} and eliminate {m(f'f({y0})')}.",
            steps_en=[
                f"At {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f({y0}) = {c_mul * x0}')}.",
                f"At {m(f'x = {y0}')}: {m(f'{a}f({y0}) + ({b})f({x0}) = {c_mul * y0}')}.",
                f"Solve for {m(f'f({x0})')}: {m(f'({a*a - b*b})f({x0}) = {a*c_mul*x0 - b*c_mul*y0} \\implies f({x0}) = {ans}')}.",
            ],
            check_en=f"Verify {m(f'{a}({ans}) + ({b})({f_rec(y0)}) = {c_mul * x0}')}.",
            idea_ar=f"نقرن {m(f'x = {x0}')} مع {m(f'x = {y0}')} ونحذف {m(f'f({y0})')} من المعادلتين.",
            steps_ar=[
                f"نعوّض {m(f'x = {x0}')} و{m(f'x = {y0}')} في المعادلة المعطاة.",
                f"بحلّ النظام الخطي نجد {m(f'f({x0}) = {ans}')}.",
            ],
            check_ar=f"التعويض بـ {m(f'f({x0}) = {ans}')} و{m(f'f({y0}) = {f_rec(y0)}')} يحقق الطرف الأيمن تماماً.",
            diagram_en=svg_function_machine(f"x={x0}", f"{k_rec}/x", f"= {c_mul}x", f"f({x0})=?"),
        ))

    hard_feq = [
        (1, 2, 9, 2),
        (1, 2, 18, 3),
        (2, 1, 18, 2),
        (1, 2, 27, -1),
        (2, 1, 18, 3),
    ]
    for idx_h, (a, b, c_mul, x0) in enumerate(hard_feq, 1):
        T = lambda x: Fraction(1, 1 - Fraction(x))
        x1 = T(x0)
        x2 = T(x1)
        assert T(x2) == x0
        f_cyc = lambda x: Fraction(
            (a * a) * (c_mul * Fraction(x)) - (a * b) * (c_mul * T(x)) + (b * b) * (c_mul * T(T(x))),
            a ** 3 + b ** 3,
        )
        assert a * f_cyc(x0) + b * f_cyc(x1) == c_mul * x0
        assert a * f_cyc(x1) + b * f_cyc(x2) == c_mul * x1
        assert a * f_cyc(x2) + b * f_cyc(x0) == c_mul * x2
        ans = f_cyc(x0)
        a_pre = "" if a == 1 else str(a)
        b_pre = "" if b == 1 else str(b)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo functional cycle problem (#{idx_h}), {m('f: \\mathbb{R} \\setminus \\{0, 1\\} \\to \\mathbb{R}')} satisfies {m(f'{a_pre}f(x) + {b_pre}f\\!\\left(\\frac{{1}}{{1 - x}}\\right) = {c_mul}x')} for all {m('x \\notin \\{0, 1\\}')}. What is {m(f'f({x0})')}?",
            q_ar=f"في مسألة دورة دالية من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، تحقق الدالة {m('f')} المعرّفة على {m('\\mathbb{R} \\setminus \\{0, 1\\}')} المعادلة {m(f'{a_pre}f(x) + {b_pre}f\\!\\left(\\frac{{1}}{{1 - x}}\\right) = {c_mul}x')}. ما قيمة {m(f'f({x0})')}؟",
            correct_val=ans,
            distractors=[f_cyc(x1), ans + 2, ans - 2, Fraction(c_mul * x0, a + b)],
            hint_en=f"Iterate the map {m('x \\mapsto \\frac{1}{1-x}')} three times starting at {m(f'x = {x0}')}: {m(f'{x0} \\to {x1} \\to {x2} \\to {x0}')}!",
            hint_ar=f"كرّر التعويض {m('x \\mapsto \\frac{1}{1-x}')} ثلاث مرات بدءاً من {m(f'x = {x0}')}: تتشكّل دورة مغلقة {m(f'{x0} \\to {x1} \\to {x2} \\to {x0}')}!",
            idea_en=f"The transformation {m('T(x) = \\frac{1}{1-x}')} has period {m('3')}, giving three cyclic equations in {m(f'f({x0}), f({x1}), f({x2})')}.",
            steps_en=[
                f"Substitute {m(f'x = {x0}, {x1}, {x2}')} in turn to get three equations around the 3-cycle.",
                f"Combine them with weights {m(f'{a*a}, -{a*b}, +{b*b}')} to obtain {m(f'({a**3 + b**3})f({x0}) = {(a**3 + b**3) * ans}')}.",
                f"Divide by {m(str(a ** 3 + b ** 3))} to get {m(f'f({x0}) = {ans}')}.",
            ],
            check_en=f"Check all 3 equations with {m(f'f({x0})={ans}, f({x1})={f_cyc(x1)}, f({x2})={f_cyc(x2)}')}.",
            idea_ar=f"التحويل {m('T(x) = \\frac{1}{1-x}')} ثلاثي الدورة ({m('T^3(x) = x')})، فيعطي ثلاث معادلات تغلق على نفسها.",
            steps_ar=[
                f"نعوّض {m(f'x = {x0}')} ثم {m(f'x = {x1}')} ثم {m(f'x = {x2}')}.",
                f"بدمج المعادلات الثلاث بالأوزان {m(f'{a*a}, -{a*b}, +{b*b}')} نجد {m(f'f({x0}) = {ans}')}.",
            ],
            check_ar=f"التحقق بالتعويض في المعادلات الثلاث يؤكد صحة القيمة {m(str(ans))}.",
            diagram_en=svg_function_machine(f"x={x0}", "1/(1−x)", "(x−1)/x", f"f({x0})=?"),
        ))

    # ------------------------------------------------------------------
    # 8. kang_stu_telescoping_amgm_extremals (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_telescoping_amgm_extremals"
    easy_tele = [
        (1, 100, 1),
        (4, 144, 1),
        (9, 225, 1),
        (1, 81, 2),
        (1, 256, 3),
    ]
    for idx_e, (A, B, d_step) in enumerate(easy_tele, 1):
        assert (B - A) % d_step == 0
        ans = math.isqrt(B) - math.isqrt(A)
        num_val = sum(d_step / (math.sqrt(k + d_step) + math.sqrt(k)) for k in range(A, B, d_step))
        assert abs(num_val - ans) < 1e-9
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo telescoping card #{idx_e}, what is the exact value of {m(f'\\frac{{{d_step}}}{{\\sqrt{{{A + d_step}}} + \\sqrt{{{A}}}}} + \\frac{{{d_step}}}{{\\sqrt{{{A + 2*d_step}}} + \\sqrt{{{A + d_step}}}}} + \\dots + \\frac{{{d_step}}}{{\\sqrt{{{B}}} + \\sqrt{{{B - d_step}}}}}')}?",
            q_ar=f"في بطاقة المجاميع المتداخلة بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، ما القيمة الدقيقة للمجموع {m(f'\\frac{{{d_step}}}{{\\sqrt{{{A + d_step}}} + \\sqrt{{{A}}}}} + \\frac{{{d_step}}}{{\\sqrt{{{A + 2*d_step}}} + \\sqrt{{{A + d_step}}}}} + \\dots + \\frac{{{d_step}}}{{\\sqrt{{{B}}} + \\sqrt{{{B - d_step}}}}}')}؟",
            correct_val=ans,
            distractors=[math.isqrt(B) + math.isqrt(A), ans + 1, ans - 1, math.isqrt(B)],
            hint_en=f"Multiply each fraction by its conjugate {m(f'\\sqrt{{k + {d_step}}} - \\sqrt{{k}}')} to rationalize the denominator.",
            hint_ar=f"اضرب كل كسر في المرافق {m(f'\\sqrt{{k + {d_step}}} - \\sqrt{{k}}')} لإنطاق المقام.",
            idea_en=f"Rationalizing gives {m(f'\\frac{{{d_step}}}{{\\sqrt{{k+{d_step}}} + \\sqrt{{k}}}} = \\sqrt{{k+{d_step}}} - \\sqrt{{k}}')}, which telescopes cleanly.",
            steps_en=[
                f"Each term simplifies to {m(f'\\sqrt{{k + {d_step}}} - \\sqrt{{k}}')}.",
                f"All interior square roots cancel, leaving {m(f'\\sqrt{{{B}}} - \\sqrt{{{A}}} = {math.isqrt(B)} - {math.isqrt(A)} = {ans}')}.",
            ],
            check_en=f"Numerical summation of all {m(str((B - A) // d_step))} terms equals {m(f'{ans}.000000')}.",
            idea_ar=f"بإنطاق المقام يتحول كل حد إلى {m(f'\\sqrt{{k + {d_step}}} - \\sqrt{{k}}')} فتختصر الحدود الوسطى بالتداخل.",
            steps_ar=[
                f"بعد إنطاق المقامات تُحذف جميع الجذور الداخلية بالتناوب.",
                f"يتبقى الحد الأخير ناقص الأول: {m(f'\\sqrt{{{B}}} - \\sqrt{{{A}}} = {ans}')}.",
            ],
            check_ar=f"جمع الحدود عددياً يؤكد أن الناتج يساوي {m(str(ans))} تماماً.",
            diagram_en=svg_number_strip([f"√{A}", "...", f"√{B}", "Sum=?"]),
        ))

    med_amgm = [
        (3, 5, 16),
        (2, 7, 9),
        (4, 6, 5),
        (3, 9, 8),
        (5, 7, 12),
    ]
    for idx_m, (a, b, S) in enumerate(med_amgm, 1):
        ans = Fraction((a + b) ** 2, S)
        assert ans.denominator == 1
        ans_i = int(ans)
        x_opt = Fraction(a * S, a + b)
        y_opt = Fraction(b * S, a + b)
        assert Fraction(a * a, 1) / x_opt + Fraction(b * b, 1) / y_opt == ans_i
        for j in range(1, 100):
            xv = S * j / 100.0
            yv = S - xv
            assert (a * a) / xv + (b * b) / yv >= ans_i - 1e-9
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In a Grade 11–12 Student Kangaroo optimization problem (#{idx_m}), positive real numbers {m('x')} and {m('y')} satisfy {m(f'x + y = {S}')}. What is the **minimum** possible value of {m(f'\\frac{{{a*a}}}{{x}} + \\frac{{{b*b}}}{{y}}')}?",
            q_ar=f"في مسألة قيم قصوى بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، يحقق العددان الحقيقيان الموجبان {m('x')} و{m('y')} الشرط {m(f'x + y = {S}')}. ما **أصغر** قيمة ممكنة للمقدار {m(f'\\frac{{{a*a}}}{{x}} + \\frac{{{b*b}}}{{y}}')}؟",
            correct_val=ans_i,
            distractors=[ans_i + 2, max(1, ans_i - 2), (a * a + b * b) * 2 // S if ((a * a + b * b) * 2) % S == 0 else ans_i + 4, ans_i + 3],
            hint_en=f"Apply Titu's Lemma (Cauchy–Schwarz): {m(f'\\frac{{{a}^2}}{{x}} + \\frac{{{b}^2}}{{y}} \\ge \\frac{{({a} + {b})^2}}{{x + y}}')}.",
            hint_ar=f"طبّق متراجحة كوشي-شوارتز (صورة تيتو): {m(f'\\frac{{{a}^2}}{{x}} + \\frac{{{b}^2}}{{y}} \\ge \\frac{{({a} + {b})^2}}{{x + y}}')}.",
            idea_en=f"By Cauchy–Schwarz (Titu's form), {m(f'(x + y)\\left(\\frac{{{a}^2}}{{x}} + \\frac{{{b}^2}}{{y}}\\right) \\ge ({a} + {b})^2')}.",
            steps_en=[
                f"Apply Titu's Lemma: {m(f'\\frac{{{a*a}}}{{x}} + \\frac{{{b*b}}}{{y}} \\ge \\frac{{({a} + {b})^2}}{{{S}}} = \\frac{{{(a+b)**2}}}{{{S}}} = {ans_i}')}.",
                f"Equality holds when {m(f'x/{a} = y/{b}')}, i.e. at {m(f'x = {x_opt}, y = {y_opt}')}.",
            ],
            check_en=f"Substitute {m(f'x = {x_opt}, y = {y_opt}')}: the sum is exact {m(str(ans_i))}.",
            idea_ar=f"باستخدام صورة تيتو لمتراجحة كوشي-شوارتز نجد الحد الأدنى مباشرة.",
            steps_ar=[
                f"لدينا {m(f'\\frac{{{a*a}}}{{x}} + \\frac{{{b*b}}}{{y}} \\ge \\frac{{({a}+{b})^2}}{{{S}}} = {ans_i}')}.",
                f"وتتحقق المساواة عند {m(f'x = {x_opt}')} و{m(f'y = {y_opt}')}.",
            ],
            check_ar=f"التعويض بنقطة التوازن يحقق {m(f'x + y = {S}')} ويعطي القيمة الصغرى {m(str(ans_i))}.",
            diagram_en=svg_subdivided_rect_2x2(f"x+y={S}", f"{a*a}/x", f"+{b*b}/y", "Min=?"),
        ))

    # Hard 8.1..8.3: Shifted AM-GM; 8.4..8.5: Floor of square-root sums
    shifted_amgm = [
        (1, 36, 5),
        (2, 50, 3),
        (3, 48, 4),
    ]
    for idx_h, (p_c, M_c, k_sh) in enumerate(shifted_amgm, 1):
        prod_sq = math.isqrt(p_c * M_c)
        assert prod_sq * prod_sq == p_c * M_c
        ans = 2 * prod_sq + p_c * k_sh
        x_star = Fraction(k_sh, 1) + Fraction(prod_sq, p_c)
        assert p_c * x_star + Fraction(M_c, 1) / (x_star - k_sh) == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo inequality card (#{idx_h}), what is the **minimum** value of {m(f'{p_c if p_c > 1 else ""}x + \\frac{{{M_c}}}{{x - {k_sh}}}')} over all real numbers {m(f'x > {k_sh}')}?",
            q_ar=f"في مسألة متراجحات من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، ما **أصغر** قيمة للمقدار {m(f'{p_c if p_c > 1 else ""}x + \\frac{{{M_c}}}{{x - {k_sh}}}')} لجميع الأعداد الحقيقية {m(f'x > {k_sh}')}؟",
            correct_val=ans,
            distractors=[2 * prod_sq, ans - p_c * k_sh + k_sh, ans + 2, ans - 2],
            hint_en=f"Rewrite {m(f'{p_c}x')} as {m(f'{p_c}(x - {k_sh}) + {p_c * k_sh}')} so the product with {m(f'\\frac{{{M_c}}}{{x - {k_sh}}}')} becomes constant!",
            hint_ar=f"أعد كتابة {m(f'{p_c}x')} على الصورة {m(f'{p_c}(x - {k_sh}) + {p_c * k_sh}')} ليصبح الجداء ثابتاً عند تطبيق متراجحة الوسط الحسابي والهندسي!",
            idea_en=f"Shift the variable to {m(f't = x - {k_sh} > 0')} and apply AM–GM to {m(f'{p_c}t + \\frac{{{M_c}}}{{t}}')}.",
            steps_en=[
                f"Write {m(f'{p_c}x + \\frac{{{M_c}}}{{x - {k_sh}}} = {p_c}(x - {k_sh}) + \\frac{{{M_c}}}{{x - {k_sh}}} + {p_c * k_sh}')}.",
                f"By AM–GM, {m(f'{p_c}(x - {k_sh}) + \\frac{{{M_c}}}{{x - {k_sh}}} \\ge 2\\sqrt{{{p_c} \\cdot {M_c}}} = {2*prod_sq}')}.",
                f"Adding {m(str(p_c * k_sh))} gives the exact minimum {m(str(ans))}, attained at {m(f'x = {x_star}')}.",
            ],
            check_en=f"At {m(f'x = {x_star}')}, {m(f'{p_c}({x_star}) + {M_c}/({x_star - k_sh}) = {ans}')}.",
            idea_ar=f"نعوض {m(f't = x - {k_sh} > 0')} ونطبّق متراجحة الوسطين الحسابي والهندسي على {m(f'{p_c}t + {M_c}/t')}.",
            steps_ar=[
                f"نفصل المقدار إلى {m(f'{p_c}t + \\frac{{{M_c}}}{{t}} + {p_c * k_sh}')}.",
                f"من AM–GM نحصل على {m(f'\\ge 2\\sqrt{{{p_c * M_c}}} + {p_c * k_sh} = {ans}')} عند {m(f'x = {x_star}')}.",
            ],
            check_ar=f"التعويض عند {m(f'x = {x_star} > {k_sh}')} يحقق القيمة الصغرى {m(str(ans))} بالضبط.",
            diagram_en=svg_function_machine(f"x>{k_sh}", f"t=x−{k_sh}", "AM-GM", "Min=?"),
        ))

    for idx_f, N_fl in enumerate([50, 85], 4):
        m_sq = math.isqrt(N_fl)
        ans = sum(k * (2 * k + 1) for k in range(1, m_sq)) + m_sq * (N_fl - m_sq * m_sq + 1)
        brute = sum(math.isqrt(k) for k in range(1, N_fl + 1))
        assert ans == brute
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo floor-sum challenge (#{idx_f}), what is the exact value of {m(f'\\sum_{{k=1}}^{{{N_fl}}} \\lfloor \\sqrt{{k}} \\rfloor = \\lfloor \\sqrt{{1}} \\rfloor + \\lfloor \\sqrt{{2}} \\rfloor + \\dots + \\lfloor \\sqrt{{{N_fl}}} \\rfloor')}?",
            q_ar=f"في مسألة دالة الجزء الصحيح من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_f})، ما القيمة الدقيقة للمجموع {m(f'\\sum_{{k=1}}^{{{N_fl}}} \\lfloor \\sqrt{{k}} \\rfloor = \\lfloor \\sqrt{{1}} \\rfloor + \\lfloor \\sqrt{{2}} \\rfloor + \\dots + \\lfloor \\sqrt{{{N_fl}}} \\rfloor')}؟",
            correct_val=ans,
            distractors=[ans - m_sq, ans + m_sq, ans + 7, ans - 8],
            hint_en=f"Group integers between consecutive squares: for {m('m^2 \\le k \\le (m+1)^2 - 1')}, there are {m('2m + 1')} integers where {m('\\lfloor \\sqrt{k} \\rfloor = m')}.",
            hint_ar=f"جمّع الأعداد بين المربعات المتتالية: لكل {m('m^2 \\le k < (m+1)^2')} يوجد {m('2m + 1')} عدداً قيمتها {m('m')}.",
            idea_en=f"Partition {m(f'1 \\dots {N_fl}')} into square intervals {m('[m^2, (m+1)^2 - 1]')} of length {m('2m + 1')} up to {m(f'{m_sq}^2 = {m_sq*m_sq}')}.",
            steps_en=[
                f"For {m(f'm = 1, \\dots, {m_sq - 1}')}, block {m('[m^2, (m+1)^2 - 1]')} contributes {m('m(2m + 1)')}, summing to {m(str(sum(k * (2 * k + 1) for k in range(1, m_sq))))}.",
                f"From {m(str(m_sq * m_sq))} to {m(str(N_fl))}, there are {m(f'{N_fl} - {m_sq*m_sq} + 1 = {N_fl - m_sq*m_sq + 1}')} terms each equal to {m(str(m_sq))}.",
                f"Total sum: {m(f'{sum(k * (2 * k + 1) for k in range(1, m_sq))} + {m_sq * (N_fl - m_sq*m_sq + 1)} = {ans}')}.",
            ],
            check_en=f"Direct term-by-term summation from {m('1')} to {m(str(N_fl))} confirms {m(str(ans))}.",
            idea_ar=f"نقسم الفترة إلى كتل بين المربعات الكاملة حتى {m(f'{m_sq}^2 = {m_sq*m_sq}')} ثم نضيف الباقي.",
            steps_ar=[
                f"مجموع الكتل الكاملة لـ {m(f'm = 1 \\dots {m_sq - 1}')} يساوي {m(str(sum(k * (2 * k + 1) for k in range(1, m_sq))))}.",
                f"الأعداد من {m(str(m_sq * m_sq))} إلى {m(str(N_fl))} عددها {m(str(N_fl - m_sq * m_sq + 1))} وكل منها يساوي {m(str(m_sq))}.",
                f"المجموع الكلي يساوي {m(str(ans))}.",
            ],
            check_ar=f"الجمع المباشر لجميع الحدود من {m('1')} إلى {m(str(N_fl))} يعطي {m(str(ans))} بالضبط.",
            diagram_en=svg_number_strip(["⌊√1⌋", "⌊√2⌋", f"..⌊√{N_fl}⌋", "Sum=?"]),
        ))

    return items


# ==============================================================================
# UNIT 5.3 — GEOMETRY PART 1: PLANE METRIC & SYNTHETIC (60 Qs: KANG-STU-121..180)
# ==============================================================================
def _unit_5_3_geometry_plane(offset: int = 120) -> list[dict]:
    items: list[dict] = []
    topic = "Geometry"

    # ------------------------------------------------------------------
    # 9. kang_stu_ceva_menelaus_area_ratios (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_ceva_menelaus_area_ratios"
    easy_ceva = [
        (2, 3, 6, 5, 2),   # DC = (2*6*5)/(3*2) = 10
        (3, 2, 4, 3, 3),   # DC = (3*4*3)/(2*3) = 6
        (4, 3, 9, 2, 3),   # DC = (4*9*2)/(3*3) = 8
        (5, 2, 6, 4, 5),   # DC = (5*6*4)/(2*5) = 12
        (3, 4, 8, 5, 2),   # DC = (3*8*5)/(4*2) = 15
    ]
    for idx_e, (af, fb, bd, ce, ea) in enumerate(easy_ceva, 1):
        num = af * bd * ce
        den = fb * ea
        assert num % den == 0
        ans = num // den
        assert Fraction(af, fb) * Fraction(bd, ans) * Fraction(ce, ea) == 1
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo geometry sheet #{idx_e}, cevians {m('AD, BE, CF')} of {m('\\triangle ABC')} concur at an interior point {m('P')}. Given {m(f'AF = {af}')}, {m(f'FB = {fb}')}, {m(f'BD = {bd}')}, {m(f'CE = {ce}')}, and {m(f'EA = {ea}')}, what is the length {m('DC')}?",
            q_ar=f"في ورقة الهندسة بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، تتلاقى المستقيمات السيفية {m('AD, BE, CF')} في المثلث {m('ABC')} عند نقطة داخلية {m('P')}. إذا كان {m(f'AF = {af}')} و{m(f'FB = {fb}')} و{m(f'BD = {bd}')} و{m(f'CE = {ce}')} و{m(f'EA = {ea}')}، فما طول {m('DC')}؟",
            correct_val=ans,
            distractors=[ans + 2, max(2, ans - 2), (fb * ea * bd) // (af * ce) if (fb * ea * bd) % (af * ce) == 0 else ans + 4, ans + 3],
            hint_en=f"Apply Ceva's Theorem around {m('\\triangle ABC')}: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
            hint_ar=f"طبّق مبرهنة سيفا حول المثلث {m('ABC')}: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
            idea_en=f"Concurrent cevians satisfy Ceva's cyclic ratio product {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
            steps_en=[
                f"Substitute the known segments: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bd}}}{{DC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"Solve for {m('DC')}: {m(f'DC = \\frac{{{af} \\times {bd} \\times {ce}}}{{{fb} \\times {ea}}} = {ans}')}.",
            ],
            check_en=f"Product check: {m(f'({af}/{fb}) \\cdot ({bd}/{ans}) \\cdot ({ce}/{ea}) = 1')}.",
            idea_ar=f"تلاقي المستقيمات السيفية الثلاثة يحقق علاقة سيفا الدورانية.",
            steps_ar=[
                f"نعوّض الأطوال المعطاة: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bd}}}{{DC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"نحل لإيجاد {m(f'DC = {ans}')}.",
            ],
            check_ar=f"جداء النسب الثلاث يساوي {m('1')} تماماً عند {m(f'DC = {ans}')}.",
            diagram_en=svg_stu_ceva_triangle(str(af), str(fb), str(bd), "?", str(ce), str(ea)),
        ))

    med_ceva = [
        (1, 2, 1, 3, 84),   # AP/PD = 1/2 + 1/3 = 5/6 -> PD/AD = 6/11? Wait: pick clean integer [PBC]!
        # Let's check: PD/AD = 1 / (1 + u/v + r/s). Choose u/v + r/s so 1 + u/v + r/s divides Area!
    ]
    med_ceva_specs = [
        (1, 2, 3, 2, 60),   # u/v + r/s = 1/2 + 3/2 = 2 -> PD/AD = 1/3 -> [PBC] = 20
        (2, 3, 1, 3, 80),   # 2/3 + 1/3 = 1 -> PD/AD = 1/2 -> [PBC] = 40? Wait let's vary ratios:
        (1, 3, 1, 2, 66),   # 1/3 + 1/2 = 5/6 -> PD/AD = 6/11 -> [PBC] = 36
        (2, 1, 1, 2, 70),   # 2 + 1/2 = 5/2 -> PD/AD = 2/7 -> [PBC] = 20? Keep answers distinct!
    ]
    med_ceva_clean = [
        (1, 2, 3, 2, 60),   # [PBC] = 20
        (1, 3, 1, 2, 66),   # [PBC] = 36
        (3, 2, 1, 2, 84),   # u/v+r/s = 2 -> PD/AD = 1/3 -> [PBC] = 28
        (2, 3, 3, 4, 115),  # 2/3 + 3/4 = 17/12 -> PD/AD = 12/29? Wait: 2/3 + 1/6 = 5/6; 3/4 + 1/2 = 5/4 -> PD/AD = 4/9! With 99 -> 44!
        (1, 4, 2, 3, 92),   # 1/4 + 2/3 = 11/12 -> PD/AD = 12/23 -> with 92 -> 48!
    ]
    med_ceva_final = [
        (1, 2, 3, 2, 60),   # 20
        (3, 2, 1, 2, 84),   # 28
        (1, 3, 1, 2, 66),   # 36
        (3, 4, 1, 2, 99),   # 44
        (1, 4, 2, 3, 92),   # 48
    ]
    for idx_m, (u, v, r, s, area_tot) in enumerate(med_ceva_final, 1):
        # Analytic coordinates: B=(0,0), C=(1,0), A=(0,1) -> [ABC] = 1/2
        # F on AB with AF:FB = u:v => F = (0, v/(u+v))
        # E on AC with AE:EC = r:s => E = (r/(r+s), s/(r+s))
        fx, fy = Fraction(0), Fraction(v, u + v)
        ex, ey = Fraction(r, r + s), Fraction(s, r + s)
        # Line BE: y = (ey/ex) x; Line CF through (1,0) and (0, fy): x + y/fy = 1 => x + x*(ey/(ex*fy)) = 1
        px = Fraction(1, 1 + ey / (ex * fy))
        py = (ey / ex) * px
        # [PBC] / [ABC] = py / 1 = py
        van_obel = Fraction(u, v) + Fraction(r, s)
        assert py == Fraction(1, 1 + van_obel)
        ans_f = area_tot * py
        assert ans_f.denominator == 1
        ans = int(ans_f)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, cevians {m('AD, BE, CF')} of {m('\\triangle ABC')} meet at {m('P')}. If {m(f'AF : FB = {u} : {v}')}, {m(f'AE : EC = {r} : {s}')}, and the area of {m('\\triangle ABC')} is {m(str(area_tot))}, what is the area of {m('\\triangle PBC')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، تتلاقى المستقيمات السيفية {m('AD, BE, CF')} للمثلث {m('ABC')} عند النقطة {m('P')}. إذا كان {m(f'AF : FB = {u} : {v}')} و{m(f'AE : EC = {r} : {s}')} ومساحة {m('\\triangle ABC')} تساوي {m(str(area_tot))}، فما مساحة {m('\\triangle PBC')}؟",
            correct_val=ans,
            distractors=[area_tot - ans, ans + 4, max(4, ans - 4), area_tot // 3],
            hint_en=f"By van Obel's theorem (or mass points), {m('\\frac{AP}{PD} = \\frac{AF}{FB} + \\frac{AE}{EC}')}, and {m('\\frac{[PBC]}{[ABC]} = \\frac{PD}{AD}')}.",
            hint_ar=f"باستخدام مبرهنة فان أوبل (أو أوزان الرؤوس)، {m('\\frac{AP}{PD} = \\frac{AF}{FB} + \\frac{AE}{EC}')}، ونسبة المساحة هي {m('\\frac{PD}{AD}')}.",
            idea_en=f"Mass points at {m('A, B, C')} give {m(f'\\frac{{AP}}{{PD}} = \\frac{{{u}}}{{{v}}} + \\frac{{{r}}}{{{s}}} = {van_obel}')}.",
            steps_en=[
                f"Compute {m(f'\\frac{{AP}}{{PD}} = \\frac{{{u}}}{{{v}}} + \\frac{{{r}}}{{{s}}} = {van_obel}')}.",
                f"Since {m('\\triangle PBC')} and {m('\\triangle ABC')} share base {m('BC')}, {m(f'\\frac{{[PBC]}}{{[ABC]}} = \\frac{{PD}}{{AD}} = \\frac{{1}}{{1 + {van_obel}}} = {py}')}.",
                f"Multiply by {m(f'[ABC] = {area_tot}')}: {m(f'[PBC] = {area_tot} \\times {py} = {ans}')}.",
            ],
            check_en=f"Exact barycentric coordinates confirm {m(f'[PBC] = {ans}')}.",
            idea_ar=f"من علاقة فان أوبل نحسب {m(f'AP/PD = {van_obel}')} ومنها نسبة الارتفاعين على القاعدة المشتركة {m('BC')}.",
            steps_ar=[
                f"نجد {m(f'\\frac{{AP}}{{PD}} = \\frac{{{u}}}{{{v}}} + \\frac{{{r}}}{{{s}}} = {van_obel}')}.",
                f"إذن {m(f'\\frac{{PD}}{{AD}} = {py}')}، وتكون مساحة {m(f'\\triangle PBC = {area_tot} \\times {py} = {ans}')}.",
            ],
            check_ar=f"التحقق بالإحداثيات المرجعية يؤكد أن المساحة تساوي {m(str(ans))} تماماً.",
            diagram_en=svg_stu_ceva_triangle(f"{u}k", f"{v}k", "BD", "DC", f"{s}m", f"{r}m"),
        ))

    # Hard 9.1..9.3: Inner cevian/subdivision triangle [DEF] area; 9.4..9.5: Menelaus transversal
    def_specs = [
        (1, 2, 1, 2, 1, 2, 90),    # BD:DC=1:2, CE:EA=1:2, AF:FB=1:2 -> 1 - 3*(2/9) = 1/3 -> 30
        (1, 3, 1, 2, 1, 1, 96),    # corners: (2/3)*(1/2)=1/3, (1/2)*(1/4)=1/8, (3/4)*(1/3)=1/4 -> 1 - 17/24 = 7/24 -> 28
        (2, 3, 1, 3, 3, 1, 160),   # corners: (3/4)*(3/4)=9/16, (1/4)*(2/5)=1/10, (3/5)*(1/4)=3/20 -> 1 - (45+8+12)/80 = 15/80 -> 30? Let's make distinct: area_tot=240 -> 45!
    ]
    def_specs_clean = [
        (1, 2, 1, 2, 1, 2, 90),    # 30
        (1, 3, 1, 2, 1, 1, 96),    # 28
        (2, 3, 1, 3, 3, 1, 240),   # 45
    ]
    for idx_h, (bd, dc, ce, ea, af, fb, area_tot) in enumerate(def_specs_clean, 1):
        f_aef = Fraction(ea, ce + ea) * Fraction(af, af + fb)
        f_bfd = Fraction(fb, af + fb) * Fraction(bd, bd + dc)
        f_cde = Fraction(dc, bd + dc) * Fraction(ce, ce + ea)
        f_def = 1 - f_aef - f_bfd - f_cde
        # Cross-check with 2D coordinates A=(0,1), B=(0,0), C=(1,0)
        Dx, Dy = Fraction(bd, bd + dc), Fraction(0)
        Ex, Ey = Fraction(ea, ce + ea), Fraction(ce, ce + ea)
        Fx, Fy = Fraction(0), Fraction(fb, af + fb)
        twice_def = abs(Dx * (Ey - Fy) + Ex * (Fy - Dy) + Fx * (Dy - Ey))
        assert twice_def == f_def  # since [ABC] = 1/2, 2*[DEF] = [DEF]/[ABC]
        ans_f = area_tot * f_def
        assert ans_f.denominator == 1
        ans = int(ans_f)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo area-ratio card (#{idx_h}), points {m('D, E, F')} lie on sides {m('BC, CA, AB')} of {m('\\triangle ABC')} with {m(f'BD : DC = {bd} : {dc}')}, {m(f'CE : EA = {ce} : {ea}')}, and {m(f'AF : FB = {af} : {fb}')}. If {m(f'[ABC] = {area_tot}')}, what is the area of the inner triangle {m('\\triangle DEF')}?",
            q_ar=f"في مسألة نسب المساحات من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، تقع النقاط {m('D, E, F')} على الأضلاع {m('BC, CA, AB')} للمثلث {m('ABC')} بحيث {m(f'BD : DC = {bd} : {dc}')} و{m(f'CE : EA = {ce} : {ea}')} و{m(f'AF : FB = {af} : {fb}')}. إذا كانت مساحة {m(f'\\triangle ABC = {area_tot}')}، فما مساحة المثلث الداخلي {m('\\triangle DEF')}؟",
            correct_val=ans,
            distractors=[ans + 6, max(6, ans - 6), area_tot // 4, ans + 10],
            hint_en=f"Compute each corner area fraction {m('[AEF]/[ABC]')}, {m('[BFD]/[ABC]')}, and {m('[CDE]/[ABC]')} using {m('\\frac{uv}{AB \\cdot AC}')}, then subtract from {m('1')}.",
            hint_ar=f"احسب نسبة مساحة كل مثلث ركني إلى مساحة {m('ABC')} بضرب نسبتي الضلعين المحيطين بالزاوية، ثم اطرح المجموع من {m('1')}.",
            idea_en=f"Subtract the three corner triangles from {m('[ABC]')}: {m('[DEF]/[ABC] = 1 - \\frac{AE}{AC}\\frac{AF}{AB} - \\frac{BF}{BA}\\frac{BD}{BC} - \\frac{CD}{CB}\\frac{CE}{CA}')}.",
            steps_en=[
                f"Corner fractions: {m(f'[AEF]/[ABC] = {f_aef}')}, {m(f'[BFD]/[ABC] = {f_bfd}')}, and {m(f'[CDE]/[ABC] = {f_cde}')}.",
                f"Inner fraction: {m(f'1 - ({f_aef} + {f_bfd} + {f_cde}) = {f_def}')}.",
                f"Multiply by {m(str(area_tot))}: {m(f'[DEF] = {area_tot} \\times {f_def} = {ans}')}.",
            ],
            check_en=f"Corner areas {m(f'{int(area_tot*f_aef)}, {int(area_tot*f_bfd) if (area_tot*f_bfd).denominator==1 else area_tot*f_bfd}, {int(area_tot*f_cde) if (area_tot*f_cde).denominator==1 else area_tot*f_cde}')} plus {m(str(ans))} sum to {m(str(area_tot))}.",
            idea_ar=f"نطرح مساحات المثلثات الركنية الثلاثة من المساحة الكلية للمثلث {m('ABC')}.",
            steps_ar=[
                f"نسب المثلثات الركنية هي {m(str(f_aef))} و{m(str(f_bfd))} و{m(str(f_cde))}.",
                f"النسبة المتبقية للمثلث الداخلي هي {m(str(f_def))}، فتكون مساحته {m(f'{area_tot} \\times {f_def} = {ans}')}.",
            ],
            check_ar=f"مجموع مساحات المثلثات الأربعة يساوي {m(str(area_tot))} تماماً.",
            diagram_en=svg_stu_ceva_triangle(f"{af}", f"{fb}", f"{bd}", f"{dc}", f"{ce}", f"{ea}"),
        ))

    menelaus_specs = [
        # Transversal cuts AB at F (AF:FB = u:v), AC at E (AE:EC = r:s, with u/v > r/s? Wait: if D is beyond C on BC extended:
        # (AF/FB) * (BD/CD) * (CE/EA) = 1 => BD/CD = (FB * EA) / (AF * CE) > 1 => FB*EA > AF*CE!
        (1, 3, 2, 1, 10),  # AF=1, FB=3, AE=2, EC=1 -> BD/CD = (3*2)/(1*1) = 6 -> (BC+CD)/CD = 6 -> BC = 5*CD -> BC=10 => CD=2? Let's pick larger: BC=25 => CD=5!
        (2, 5, 3, 1, 26),  # AF=2, FB=5, AE=3, EC=1 -> BD/CD = 15/2 -> BC/CD = 13/2 -> BC=26 => CD=4!
    ]
    menelaus_clean = [
        (1, 3, 2, 1, 35),  # BD/CD = 6 -> 5*CD = 35 -> CD = 7
        (2, 5, 3, 1, 39),  # BD/CD = 15/2 -> (13/2)*CD = 39 -> CD = 6 -> let's use BC=65 -> CD = 10!
    ]
    for idx_m2, (af, fb, ae, ec, bc_len) in enumerate(menelaus_clean, 4):
        ratio_bd_cd = Fraction(fb * ae, af * ec)
        assert ratio_bd_cd > 1
        cd_f = Fraction(bc_len, ratio_bd_cd - 1)
        assert cd_f.denominator == 1
        ans = int(cd_f)
        # Coordinate check: B=(0,0), C=(bc_len, 0), A=(0, 1)
        Fx, Fy = Fraction(0), Fraction(fb, af + fb)
        Ex, Ey = Fraction(ae * bc_len, ae + ec), Fraction(ec, ae + ec)
        # Line FE meets y=0 at Dx:
        Dx = Fx - Fy * (Ex - Fx) / (Ey - Fy)
        assert Dx == bc_len + ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo Menelaus problem (#{idx_m2}), a line meets side {m('AB')} of {m('\\triangle ABC')} at {m('F')}, side {m('AC')} at {m('E')}, and the extension of {m('BC')} beyond {m('C')} at {m('D')}. Given {m(f'AF : FB = {af} : {fb}')}, {m(f'AE : EC = {ae} : {ec}')}, and {m(f'BC = {bc_len}')}, what is the length {m('CD')}?",
            q_ar=f"في مسألة مينلاوس من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_m2})، يقطع مستقيم الضلع {m('AB')} للمثلث {m('ABC')} في {m('F')}، والضلع {m('AC')} في {m('E')}، وامتداد {m('BC')} بعد {m('C')} في {m('D')}. إذا كان {m(f'AF : FB = {af} : {fb}')} و{m(f'AE : EC = {ae} : {ec}')} و{m(f'BC = {bc_len}')}، فما طول {m('CD')}؟",
            correct_val=ans,
            distractors=[ans + 3, max(2, ans - 2), ans * 2, bc_len // 3],
            hint_en=f"Apply Menelaus's Theorem to {m('\\triangle ABC')} and line {m('FED')}: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}, with {m(f'BD = {bc_len} + CD')}.",
            hint_ar=f"طبّق مبرهنة مينلاوس على المثلث {m('ABC')} والقاطع {m('FED')} مع ملاحظة أن {m(f'BD = {bc_len} + CD')}.",
            idea_en=f"By Menelaus's Theorem, {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bc_len} + CD}}{{CD}} \\cdot \\frac{{{ec}}}{{{ae}}} = 1')}.",
            steps_en=[
                f"Solve the Menelaus product for {m('BD / CD')}: {m(f'\\frac{{BD}}{{CD}} = \\frac{{{fb} \\times {ae}}}{{{af} \\times {ec}}} = {ratio_bd_cd}')}.",
                f"Substitute {m(f'BD = {bc_len} + CD')}: {m(f'1 + \\frac{{{bc_len}}}{{CD}} = {ratio_bd_cd} \\implies CD = {ans}')}.",
            ],
            check_en=f"Check {m(f'({af}/{fb}) \\cdot ({bc_len + ans}/{ans}) \\cdot ({ec}/{ae}) = 1')}.",
            idea_ar=f"نطبّق مبرهنة مينلاوس لإيجاد النسبة {m('BD / CD')} ثم نعوّض {m(f'BD = {bc_len} + CD')}.",
            steps_ar=[
                f"نجد {m(f'\\frac{{BD}}{{CD}} = {ratio_bd_cd}')}.",
                f"ومنه {m(f'\\frac{{{bc_len}}}{{CD}} = {ratio_bd_cd - 1}')}، أي {m(f'CD = {ans}')}.",
            ],
            check_ar=f"جداء النسب الموجهة على القاطع يساوي {m('1')} تماماً.",
            diagram_en=svg_stu_ceva_triangle(str(af), str(fb), str(bc_len), "?", str(ec), str(ae)),
        ))

    # ------------------------------------------------------------------
    # 10. kang_stu_secant_tangent_external (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_secant_tangent_external"
    easy_tan = [
        (9, 4),
        (25, 4),
        (16, 9),
        (27, 12),
        (32, 18),
    ]
    for idx_e, (r1, r2) in enumerate(easy_tan, 1):
        ans = 2 * math.isqrt(r1 * r2)
        assert (r1 + r2) ** 2 - (r1 - r2) ** 2 == ans * ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo circle card #{idx_e}, two circles of radii {m(str(r1))} and {m(str(r2))} are externally tangent to each other and both rest on the same straight line at points {m('A')} and {m('B')}. What is the distance {m('AB')}?",
            q_ar=f"في بطاقة الدوائر بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، دائرتان نصفا قطريهما {m(str(r1))} و{m(str(r2))} متماستان من الخارج وترتكزان معاً على مستقيم واحد عند النقطتين {m('A')} و{m('B')}. ما المسافة {m('AB')}؟",
            correct_val=ans,
            distractors=[r1 + r2, ans // 2, ans + 4, ans - 2],
            hint_en=f"Connect the centers (distance {m(f'{r1} + {r2} = {r1+r2}')}) and drop a perpendicular from the smaller center to the larger radius to form a right triangle.",
            hint_ar=f"صِل المركزين (المسافة {m(str(r1 + r2))}) وأسقط عموداً من مركز الصغرى على نصف قطر الكبرى لتكوين مثلث قائم.",
            idea_en=f"In the right triangle with hypotenuse {m('r_1 + r_2')} and leg {m('|r_1 - r_2|')}, {m('AB = 2\\sqrt{r_1 r_2}')}.",
            steps_en=[
                f"Hypotenuse between centers is {m(f'{r1} + {r2} = {r1 + r2}')} and vertical leg is {m(f'{r1} - {r2} = {r1 - r2}')}.",
                f"By the Pythagorean theorem, {m(f'AB = \\sqrt{{{r1 + r2}^2 - {r1 - r2}^2}} = 2\\sqrt{{{r1} \\times {r2}}} = {ans}')}.",
            ],
            check_en=f"Verify {m(f'{ans}^2 + {r1 - r2}^2 = {ans*ans} + {(r1-r2)**2} = {(r1+r2)**2} = ({r1}+{r2})^2')}.",
            idea_ar=f"من مثلث فيثاغورس بين المركزين نجد طول المماس المشترك الخارجي {m('AB = 2\\sqrt{r_1 r_2}')}.",
            steps_ar=[
                f"البعد بين المركزين {m(str(r1 + r2))} وفرق نصفي القطرين {m(str(r1 - r2))}.",
                f"بتطبيق فيثاغورس: {m(f'AB = 2\\sqrt{{{r1} \\times {r2}}} = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'{ans}^2 + ({r1 - r2})^2 = ({r1 + r2})^2')}، صحيح.",
            diagram_en=svg_stu_tangent_circles(str(r1), str(r2), "AB = ?"),
        ))

    med_pop = [
        (12, 10),  # PA = 8
        (15, 16),  # PA = 9
        (20, 9),   # PA = 16
        (18, 15),  # PA = 12
        (24, 14),  # PA = 18
    ]
    for idx_m, (pt_len, ab_len) in enumerate(med_pop, 1):
        cands = [x for x in range(1, pt_len + 1) if x * (x + ab_len) == pt_len * pt_len]
        assert len(cands) == 1
        ans = cands[0]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, from an exterior point {m('P')}, tangent segment {m('PT')} to a circle has length {m(str(pt_len))}, and secant {m('PAB')} meets the circle at {m('A')} then {m('B')} with chord {m(f'AB = {ab_len}')}. What is the length {m('PA')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، رُسم من نقطة خارجية {m('P')} مماس {m('PT')} لدائرة طوله {m(str(pt_len))}، وقاطع {m('PAB')} يقطع الدائرة في {m('A')} ثم {m('B')} بحيث طول الوتر {m(f'AB = {ab_len}')}. ما طول القطعة {m('PA')}؟",
            correct_val=ans,
            distractors=[ans + ab_len, ans + 2, max(2, ans - 2), pt_len - ab_len // 2],
            hint_en=f"By Power of a Point, {m('PT^2 = PA \\cdot PB = PA(PA + AB)')}.",
            hint_ar=f"بقوة النقطة {m('P')} بالنسبة للدائرة: {m('PT^2 = PA \\cdot PB = PA(PA + AB)')}.",
            idea_en=f"Set {m('x = PA')} in the tangent-secant theorem {m(f'x(x + {ab_len}) = {pt_len}^2')}.",
            steps_en=[
                f"Since {m(f'PB = PA + AB = x + {ab_len}')}, Power of a Point gives {m(f'x(x + {ab_len}) = {pt_len * pt_len}')}.",
                f"Solving the positive root of {m(f'x^2 + {ab_len}x - {pt_len*pt_len} = 0')} yields {m(f'PA = {ans}')}.",
            ],
            check_en=f"Check {m(f'PA \\cdot PB = {ans} \\times {ans + ab_len} = {ans * (ans + ab_len)} = {pt_len}^2')}.",
            idea_ar=f"من مبرهنة المماس والقاطع نكوّن المعادلة التربيعية {m(f'x(x + {ab_len}) = {pt_len}^2')}.",
            steps_ar=[
                f"نضع {m('x = PA')} فيكون {m(f'PB = x + {ab_len}')}.",
                f"من {m(f'x(x + {ab_len}) = {pt_len * pt_len}')} نجد الحل الموجب {m(f'PA = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'{ans} \\times {ans + ab_len} = {pt_len * pt_len} = {pt_len}^2')}.",
            diagram_en=svg_power_of_point(str(pt_len), "?", str(ab_len)),
        ))

    hard_ford = [
        (36, 9),     # r3 = 4
        (36, 36),    # r3 = 9
        (144, 36),   # r3 = 16
        (100, 100),  # r3 = 25
        (225, 100),  # r3 = 36
    ]
    for idx_h, (r1, r2) in enumerate(hard_ford, 1):
        s1, s2 = math.isqrt(r1), math.isqrt(r2)
        inv_s3 = Fraction(1, s1) + Fraction(1, s2)
        s3_f = Fraction(1, inv_s3)
        ans_f = s3_f * s3_f
        assert ans_f.denominator == 1
        ans = int(ans_f)
        assert 2 * math.isqrt(r1 * ans) + 2 * math.isqrt(r2 * ans) == 2 * math.isqrt(r1 * r2)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo touching-circles problem (#{idx_h}), two externally tangent circles of radii {m(str(r1))} and {m(str(r2))} rest on a common line {m('\\ell')}. A third smaller circle is wedged between them so that it is externally tangent to **both** circles and also tangent to {m('\\ell')}. What is the radius of this third circle?",
            q_ar=f"في مسألة الدوائر المتماسة من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، ترتكز دائرتان متماستان من الخارج نصفا قطريهما {m(str(r1))} و{m(str(r2))} على مستقيم مشترك {m('\\ell')}. وُضعت دائرة ثالثة أصغر محصورة بينهما بحيث تمسّ **الدائرتين** من الخارج وتمسّ المستقيم {m('\\ell')} أيضاً. ما نصف قطر الدائرة الثالثة؟",
            correct_val=ans,
            distractors=[ans + 3, max(1, ans - 2), int(s3_f) if s3_f.denominator == 1 else ans + 5, ans * 2],
            hint_en=f"If the three tangency points on {m('\\ell')} are {m('A, C, B')}, then {m('AC + CB = AB')}, where each horizontal span equals {m('2\\sqrt{r_i r_j}')}!",
            hint_ar=f"إذا كانت نقاط التماس على المستقيم هي {m('A, C, B')} فإن {m('AC + CB = AB')}، حيث كل مسافة أفقية تساوي {m('2\\sqrt{r_i r_j}')}!",
            idea_en=f"Adding horizontal tangent spans {m('2\\sqrt{r_1 r_3} + 2\\sqrt{r_2 r_3} = 2\\sqrt{r_1 r_2}')} yields {m('\\frac{1}{\\sqrt{r_3}} = \\frac{1}{\\sqrt{r_1}} + \\frac{1}{\\sqrt{r_2}}')}.",
            steps_en=[
                f"Divide {m('2\\sqrt{r_1 r_3} + 2\\sqrt{r_2 r_3} = 2\\sqrt{r_1 r_2}')} by {m('2\\sqrt{r_1 r_2 r_3}')} to get {m(f'\\frac{{1}}{{\\sqrt{{r_3}}}} = \\frac{{1}}{{{s1}}} + \\frac{{1}}{{{s2}}} = {inv_s3}')}.",
                f"Invert and square: {m(f'\\sqrt{{r_3}} = {s3_f} \\implies r_3 = {ans}')}.",
            ],
            check_en=f"Spans along {m('\\ell')}: {m(f'2\\sqrt{{{r1}\\cdot {ans}}} + 2\\sqrt{{{r2}\\cdot {ans}}} = {2*math.isqrt(r1*ans)} + {2*math.isqrt(r2*ans)} = {2*math.isqrt(r1*r2)} = 2\\sqrt{{{r1}\\cdot {r2}}}')}.",
            idea_ar=f"مجموع المسافتين الأفقيتين {m('AC + CB = AB')} يعطي العلاقة {m('\\frac{1}{\\sqrt{r_3}} = \\frac{1}{\\sqrt{r_1}} + \\frac{1}{\\sqrt{r_2}}')}.",
            steps_ar=[
                f"لدينا {m(f'\\frac{{1}}{{\\sqrt{{r_3}}}} = \\frac{{1}}{{{s1}}} + \\frac{{1}}{{{s2}}} = {inv_s3}')}.",
                f"بقلب النسبة وتربيعها نحصل على {m(f'r_3 = {ans}')}.",
            ],
            check_ar=f"مجموع قطعتي التماس الجزئيتين يساوي {m(str(2 * math.isqrt(r1 * r2)))} وهو طول القطعة الكلية تماماً.",
            diagram_en=svg_stu_tangent_circles(str(r1), str(r2), "r₃ = ?"),
        ))

    # ------------------------------------------------------------------
    # 11. kang_stu_pitot_tangential_quad (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_pitot_tangential_quad"
    easy_pitot = [
        (9, 13, 4),
        (11, 15, 5),
        (14, 18, 6),
        (12, 20, 7),
        (15, 21, 8),
    ]
    for idx_e, (b_s, d_s, r_in) in enumerate(easy_pitot, 1):
        ans = r_in * (b_s + d_s)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo quadrilateral card #{idx_e}, convex quadrilateral {m('ABCD')} is circumscribed around a circle of radius {m(f'r = {r_in}')}. If opposite sides {m(f'BC = {b_s}')} and {m(f'DA = {d_s}')}, what is the **area** of {m('ABCD')}?",
            q_ar=f"في بطاقة الرباعيات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، الرباعي المحدب {m('ABCD')} محيط بدائرة نصف قطرها {m(f'r = {r_in}')}. إذا كان طولا الضلعين المتقابلين {m(f'BC = {b_s}')} و{m(f'DA = {d_s}')}، فما **مساحة** الرباعي {m('ABCD')}؟",
            correct_val=ans,
            distractors=[ans // 2, ans * 2, r_in * b_s + d_s, ans + 2 * r_in],
            hint_en=f"By Pitot's Theorem, {m('AB + CD = BC + DA')}, so the semiperimeter {m('s')} equals {m('BC + DA')}, and {m('\\text{Area} = r \\cdot s')}.",
            hint_ar=f"بحسب مبرهنة بيتو {m('AB + CD = BC + DA')}، فنصف المحيط {m('s')} يساوي {m('BC + DA')}، والمساحة تساوي {m('r \\cdot s')}.",
            idea_en=f"Pitot's Theorem gives semiperimeter {m(f's = BC + DA = {b_s + d_s}')}, and splitting into four triangles from the incenter gives {m('K = rs')}.",
            steps_en=[
                f"Since {m('AB + CD = BC + DA')}, the semiperimeter is {m(f's = {b_s} + {d_s} = {b_s + d_s}')}.",
                f"Area {m(f'K = r \\cdot s = {r_in} \\times {b_s + d_s} = {ans}')}.",
            ],
            check_en=f"Four triangles with altitude {m(str(r_in))} have total base perimeter {m(str(2 * (b_s + d_s)))}, so {m(f'\\frac{{1}}{{2}}({2*(b_s+d_s)})({r_in}) = {ans}')}.",
            idea_ar=f"مبرهنة بيتو تعطي نصف المحيط {m(f's = {b_s} + {d_s} = {b_s + d_s}')}، والمساحة هي {m('K = r \\cdot s')}.",
            steps_ar=[
                f"نصف المحيط {m(f's = BC + DA = {b_s + d_s}')}.",
                f"المساحة {m(f'K = {r_in} \\times {b_s + d_s} = {ans}')}.",
            ],
            check_ar=f"تقسيم الرباعي من مركز الدائرة الداخلية إلى ٤ مثلثات ارتفاعها {m(str(r_in))} يعطي {m(str(ans))}.",
            diagram_en=svg_stu_tangential_quad("AB", str(b_s), "CD", str(d_s), str(r_in)),
        ))

    med_pitot = [
        (4, 16),   # h = 8, Area = 80
        (9, 16),   # h = 12, Area = 150? Wait (9+16)*12/2 = 150!
        (8, 18),   # h = 12, Area = 156!
        (9, 25),   # h = 15, Area = 255!
        (12, 27),  # h = 18, Area = 351!
    ]
    for idx_m, (a_top, c_bot) in enumerate(med_pitot, 1):
        h_alt = math.isqrt(a_top * c_bot)
        assert h_alt * h_alt == a_top * c_bot
        leg = Fraction(a_top + c_bot, 2)
        assert leg * leg - Fraction(c_bot - a_top, 2) ** 2 == h_alt * h_alt
        ans_f = Fraction(a_top + c_bot, 2) * h_alt
        assert ans_f.denominator == 1
        ans = int(ans_f)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, an **isosceles trapezoid** with parallel bases of lengths {m(str(a_top))} and {m(str(c_bot))} is circumscribed around an inscribed circle. What is the **area** of this trapezoid?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، شبه منحرف **متساوي الساقين** قاعدتاه المتوازيتان {m(str(a_top))} و{m(str(c_bot))} محيط بدائرة داخله تمسّ أضلاعه الأربعة. ما **مساحة** شبه المنحرف هذا؟",
            correct_val=ans,
            distractors=[a_top * c_bot, ans + h_alt, ans - h_alt, ((a_top + c_bot) ** 2) // 4],
            hint_en=f"By Pitot's theorem each leg has length {m(f'({a_top} + {c_bot})/2')}; use Pythagoras to show the height is {m(f'h = \\sqrt{{{a_top} \\times {c_bot}}}')}!",
            hint_ar=f"من مبرهنة بيتو طول كل ساق يساوي {m(f'({a_top} + {c_bot})/2')}؛ طبّق فيثاغورس لإثبات أن الارتفاع {m(f'h = \\sqrt{{{a_top} \\times {c_bot}}}')}!",
            idea_en=f"In an isosceles tangential trapezoid, {m('2 \\cdot \\text{leg} = a + c')} implies {m('h = 2r = \\sqrt{ac}')}.",
            steps_en=[
                f"Each equal leg has length {m(f'\\frac{{{a_top} + {c_bot}}}{{2}} = {leg}')}, and the horizontal projection is {m(f'\\frac{{{c_bot} - {a_top}}}{{2}} = {Fraction(c_bot - a_top, 2)}')}.",
                f"Height {m(f'h = \\sqrt{{({leg})^2 - ({Fraction(c_bot - a_top, 2)})^2}} = \\sqrt{{{a_top} \\times {c_bot}}} = {h_alt}')}.",
                f"Area {m(f'= \\frac{{{a_top} + {c_bot}}}{{2}} \\times {h_alt} = {ans}')}.",
            ],
            check_en=f"Inradius {m(f'r = h/2 = {Fraction(h_alt, 2)}')} times semiperimeter {m(f's = {a_top + c_bot}')} also gives {m(str(ans))}.",
            idea_ar=f"في شبه المنحرف المتساوي الساقين المماسي يكون الارتفاع هو الوسط الهندسي للقاعدتين {m('h = \\sqrt{ac}')}.",
            steps_ar=[
                f"طول كل ساق {m(str(leg))} والارتفاع من فيثاغورس {m(f'h = \\sqrt{{{a_top} \\times {c_bot}}} = {h_alt}')}.",
                f"المساحة {m(f'= \\frac{{{a_top} + {c_bot}}}{{2}} \\times {h_alt} = {ans}')}.",
            ],
            check_ar=f"حاصل ضرب نصف القطر {m(str(Fraction(h_alt, 2)))} في نصف المحيط {m(str(a_top + c_bot))} يعطي {m(str(ans))} أيضاً.",
            diagram_en=svg_stu_tangential_quad(str(a_top), "leg", str(c_bot), "leg", "r"),
        ))

    hard_pitot = [
        (3, 6),     # r=2, BC=5
        (4, 12),    # r=3, BC=10
        (10, 15),   # r=6, BC=13
        (5, 20),    # r=4, BC=17
        (21, 28),   # r=12, BC=25
    ]
    for idx_h, (a_top, c_bot) in enumerate(hard_pitot, 1):
        assert (a_top * c_bot) % (a_top + c_bot) == 0
        r_in = (a_top * c_bot) // (a_top + c_bot)
        bc_leg = a_top + c_bot - 2 * r_in
        assert (2 * r_in) ** 2 + (c_bot - a_top) ** 2 == bc_leg * bc_leg
        ans = bc_leg
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo tangential-trapezoid card (#{idx_h}), right trapezoid {m('ABCD')} ({m('AB \\parallel DC')}, {m('\\angle A = \\angle D = 90^\\circ')}) has an inscribed circle and parallel bases {m(f'AB = {a_top}')} and {m(f'DC = {c_bot}')}. What is the length of the slanted leg {m('BC')}?",
            q_ar=f"في مسألة من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، شبه المنحرف القائم {m('ABCD')} ({m('AB \\parallel DC')} و{m('\\angle A = \\angle D = 90^\\circ')}) محيط بدائرة داخله وله القاعدتان المتوازيتان {m(f'AB = {a_top}')} و{m(f'DC = {c_bot}')}. ما طول الساق المائلة {m('BC')}؟",
            correct_val=ans,
            distractors=[a_top + c_bot - r_in, ans + 2, ans - 2, 2 * r_in],
            hint_en=f"The vertical leg is {m('AD = 2r')}, so Pitot gives {m(f'BC = {a_top + c_bot} - 2r')}; apply Pythagoras {m(f'(2r)^2 + ({c_bot} - {a_top})^2 = BC^2')}!",
            hint_ar=f"الساق العمودية طولها {m('AD = 2r')} ومن بيتو {m(f'BC = {a_top + c_bot} - 2r')}؛ طبّق فيثاغورس {m(f'(2r)^2 + ({c_bot} - {a_top})^2 = BC^2')}!",
            idea_en=f"Combining Pitot's theorem {m('BC = a + c - 2r')} with right-triangle Pythagoras yields {m('r = \\frac{ac}{a + c}')}.",
            steps_en=[
                f"From {m('(2r)^2 + (c - a)^2 = (a + c - 2r)^2')}, expand and cancel {m('4r^2')} to get {m('4r(a + c) = 4ac')}.",
                f"Thus {m(f'r = \\frac{{{a_top} \\times {c_bot}}}{{{a_top} + {c_bot}}} = {r_in}')}, so {m(f'AD = {2*r_in}')}.",
                f"By Pitot's theorem, {m(f'BC = {a_top} + {c_bot} - {2*r_in} = {ans}')}.",
            ],
            check_en=f"Right triangle check: {m(f'AD^2 + (DC - AB)^2 = {2*r_in}^2 + {c_bot - a_top}^2 = {(2*r_in)**2 + (c_bot-a_top)**2} = {ans}^2')}.",
            idea_ar=f"دمج مبرهنة بيتو مع مبرهنة فيثاغورس يعطي نصف القطر {m('r = \\frac{ac}{a+c}')} مباشرة.",
            steps_ar=[
                f"من {m('(2r)^2 + (c - a)^2 = (a + c - 2r)^2')} نستنتج {m(f'r = \\frac{{{a_top}\\times {c_bot}}}{{{a_top}+{c_bot}}} = {r_in}')}.",
                f"إذن الساق المائلة {m(f'BC = {a_top} + {c_bot} - 2({r_in}) = {ans}')}.",
            ],
            check_ar=f"التحقق بفيثاغورس: {m(f'({2*r_in})^2 + ({c_bot - a_top})^2 = {ans}^2')}، صحيح.",
            diagram_en=svg_stu_tangential_quad(str(a_top), "BC=?", str(c_bot), "2r", "r"),
        ))

    # ------------------------------------------------------------------
    # 12. kang_stu_apollonius_median_bisector (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_apollonius_median_bisector"
    easy_apol = [
        (10, 6, 8),     # m_a = 5
        (8, 7, 9),      # m_a = 7
        (16, 11, 13),   # m_a = 9
        (24, 13, 19),   # m_a = 11
        (18, 16, 22),   # m_a = 17
    ]
    for idx_e, (a_bc, b_ac, c_ab) in enumerate(easy_apol, 1):
        assert abs(b_ac - c_ab) < a_bc < b_ac + c_ab
        four_m2 = 2 * b_ac * b_ac + 2 * c_ab * c_ab - a_bc * a_bc
        assert four_m2 % 4 == 0
        ans = math.isqrt(four_m2 // 4)
        assert 4 * ans * ans == four_m2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo triangle card #{idx_e}, {m('\\triangle ABC')} has side lengths {m(f'AB = {c_ab}')}, {m(f'AC = {b_ac}')}, and {m(f'BC = {a_bc}')}. What is the length of the median {m('AM')} from {m('A')} to the midpoint {m('M')} of {m('BC')}?",
            q_ar=f"في بطاقة المثلثات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، أطوال أضلاع المثلث {m('ABC')} هي {m(f'AB = {c_ab}')} و{m(f'AC = {b_ac}')} و{m(f'BC = {a_bc}')}. ما طول المتوسط {m('AM')} المرسوم من {m('A')} إلى منتصف {m('BC')}؟",
            correct_val=ans,
            distractors=[ans + 2, max(2, ans - 2), (b_ac + c_ab) // 2 if (b_ac + c_ab) // 2 != ans else ans + 1, ans + 3],
            hint_en=f"Apply Apollonius's Theorem: {m('2AB^2 + 2AC^2 - BC^2 = 4AM^2')}.",
            hint_ar=f"طبّق مبرهنة أبولونيوس لطول المتوسط: {m('2AB^2 + 2AC^2 - BC^2 = 4AM^2')}.",
            idea_en=f"By Apollonius's Theorem, {m('4m_a^2 = 2b^2 + 2c^2 - a^2')}.",
            steps_en=[
                f"Compute {m(f'4AM^2 = 2({b_ac}^2) + 2({c_ab}^2) - {a_bc}^2 = {2*b_ac*b_ac} + {2*c_ab*c_ab} - {a_bc*a_bc} = {four_m2}')}.",
                f"Divide by {m('4')} and take the positive square root: {m(f'AM^2 = {four_m2 // 4} \\implies AM = {ans}')}.",
            ],
            check_en=f"Triangle inequality on {m('\\triangle ABM')}: {m(f'|{c_ab} - {a_bc/2:g}| < {ans} < {c_ab} + {a_bc/2:g}')} holds.",
            idea_ar=f"نحسب طول المتوسط مباشرة من مبرهنة أبولونيوس {m('4m_a^2 = 2b^2 + 2c^2 - a^2')}.",
            steps_ar=[
                f"نعوّض: {m(f'4AM^2 = 2({b_ac}^2) + 2({c_ab}^2) - {a_bc}^2 = {four_m2}')}.",
                f"ومنه {m(f'AM^2 = {four_m2 // 4}')} أي {m(f'AM = {ans}')}.",
            ],
            check_ar=f"القيمة {m(f'AM = {ans}')} تحقق متراجحة المثلث في {m('\\triangle ABM')} وصيغة أبولونيوس معاً.",
            diagram_en=svg_median_tri(str(c_ab), str(b_ac), str(a_bc), "mₐ = ?"),
        ))

    med_bis = [
        (12, 15, 18),   # m=8, n=10, AD^2 = 100
        (6, 12, 9),     # m=3, n=6, AD^2 = 54
        (8, 12, 10),    # m=4, n=6, AD^2 = 72
        (10, 15, 15),   # m=6, n=9, AD^2 = 96
        (14, 21, 20),   # m=8, n=12, AD^2 = 198
    ]
    for idx_m, (c_ab, b_ac, a_bc) in enumerate(med_bis, 1):
        assert abs(b_ac - c_ab) < a_bc < b_ac + c_ab
        assert (a_bc * c_ab) % (b_ac + c_ab) == 0
        m_seg = (a_bc * c_ab) // (b_ac + c_ab)
        n_seg = a_bc - m_seg
        ans = b_ac * c_ab - m_seg * n_seg
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, {m('AD')} is the interior angle bisector of {m('\\angle A')} in {m('\\triangle ABC')} (with {m('D')} on {m('BC')}). Given {m(f'AB = {c_ab}')}, {m(f'AC = {b_ac}')}, and {m(f'BC = {a_bc}')}, what is the exact value of {m('AD^2')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، القطعة {m('AD')} هي المنصّف الداخلي للزاوية {m('\\angle A')} في المثلث {m('ABC')} (حيث {m('D')} على {m('BC')}). إذا كان {m(f'AB = {c_ab}')} و{m(f'AC = {b_ac}')} و{m(f'BC = {a_bc}')}، فما القيمة الدقيقة لـ {m('AD^2')}؟",
            correct_val=ans,
            distractors=[b_ac * c_ab, ans + m_seg * n_seg // 2, ans - 12, ans + 12],
            hint_en=f"First split {m(f'BC = {a_bc}')} in the ratio {m(f'BD : DC = {c_ab} : {b_ac}')}, then apply {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}.",
            hint_ar=f"قسّم أولاً الضلع {m(f'BC = {a_bc}')} بنسبة {m(f'BD : DC = {c_ab} : {b_ac}')}، ثم طبّق مبرهنة طول المنصّف {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}.",
            idea_en=f"By the Angle Bisector Theorem {m('BD : DC = AB : AC')}, and by Stewart's / Bisector Length Theorem {m('AD^2 = bc - mn')}.",
            steps_en=[
                f"Split {m(f'BC = {a_bc}')} in ratio {m(f'{c_ab} : {b_ac}')}: {m(f'BD = {m_seg}')} and {m(f'DC = {n_seg}')}.",
                f"Compute {m(f'AD^2 = {c_ab} \\times {b_ac} - {m_seg} \\times {n_seg} = {b_ac*c_ab} - {m_seg*n_seg} = {ans}')}.",
            ],
            check_en=f"Stewart's identity check: {m(f'{b_ac}^2({m_seg}) + {c_ab}^2({n_seg}) = {a_bc}(AD^2 + {m_seg}\\cdot {n_seg})')} gives {m(f'AD^2 = {ans}')}.",
            idea_ar=f"نحدد جزأي القاعدة بنظرية المنصّف ثم نحسب {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}.",
            steps_ar=[
                f"من نسبة الضلعين نجد {m(f'BD = {m_seg}')} و{m(f'DC = {n_seg}')}.",
                f"نطبّق الصيغة: {m(f'AD^2 = {c_ab} \\times {b_ac} - {m_seg} \\times {n_seg} = {ans}')}.",
            ],
            check_ar=f"التحقق بمبرهنة ستيوارت يؤكد أن {m(f'AD^2 = {ans}')} بالضبط.",
            diagram_en=svg_angle_bisector_tri(str(c_ab), str(b_ac), "BD", "DC"),
        ))

    hard_perp_med = [
        (13, 19, 22),
        (17, 22, 31),
        (25, 38, 41),
        (26, 38, 44),
        (37, 58, 59),
    ]
    for idx_h, (a_bc, b_ac, c_ab) in enumerate(hard_perp_med, 1):
        assert abs(b_ac - c_ab) < a_bc < b_ac + c_ab
        assert b_ac * b_ac + c_ab * c_ab == 5 * a_bc * a_bc
        # Double-check centroid right-angle condition (2/3 m_b)^2 + (2/3 m_c)^2 == a^2
        four_mb2 = 2 * a_bc * a_bc + 2 * c_ab * c_ab - b_ac * b_ac
        four_mc2 = 2 * a_bc * a_bc + 2 * b_ac * b_ac - c_ab * c_ab
        assert Fraction(four_mb2 + four_mc2, 9) == a_bc * a_bc
        ans = a_bc
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo centroid card (#{idx_h}), in {m('\\triangle ABC')} with {m(f'AC = {b_ac}')} and {m(f'AB = {c_ab}')}, the medians from {m('B')} and {m('C')} intersect **perpendicularly** at the centroid {m('G')}. What is the length of side {m('BC')}?",
            q_ar=f"في مسألة مركز الثقل من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، في المثلث {m('ABC')} الذي فيه {m(f'AC = {b_ac}')} و{m(f'AB = {c_ab}')}، يتقاطع المتوسطان المرسومان من {m('B')} و{m('C')} **بالتعامد** عند مركز الثقل {m('G')}. ما طول الضلع {m('BC')}؟",
            correct_val=ans,
            distractors=[ans + 2, ans - 2, (b_ac + c_ab) // 2, ans + 4],
            hint_en=f"At the centroid {m('G')}, {m('BG = \\frac{2}{3}m_b')} and {m('CG = \\frac{2}{3}m_c')}; combine {m('BG^2 + CG^2 = BC^2')} with Apollonius's formulas for {m('m_b^2')} and {m('m_c^2')}!",
            hint_ar=f"عند مركز الثقل {m('BG = \\frac{2}{3}m_b')} و{m('CG = \\frac{2}{3}m_c')}؛ ادمج {m('BG^2 + CG^2 = BC^2')} مع صيغتي أبولونيوس!",
            idea_en=f"Perpendicular medians from {m('B')} and {m('C')} satisfy the clean identity {m('AB^2 + AC^2 = 5 BC^2')}.",
            steps_en=[
                f"In right {m('\\triangle BGC')}, {m('\\frac{4}{9}(m_b^2 + m_c^2) = a^2')}, so {m('4m_b^2 + 4m_c^2 = 9a^2')}.",
                f"By Apollonius, {m('4m_b^2 + 4m_c^2 = (2a^2 + 2c^2 - b^2) + (2a^2 + 2b^2 - c^2) = 4a^2 + b^2 + c^2')}.",
                f"Hence {m(f'5a^2 = b^2 + c^2 = {b_ac}^2 + {c_ab}^2 = {b_ac*b_ac + c_ab*c_ab}')}, giving {m(f'a^2 = {a_bc*a_bc} \\implies BC = {ans}')}.",
            ],
            check_en=f"Verify {m(f'5({ans}^2) = {5*ans*ans} = {b_ac}^2 + {c_ab}^2')} and strict triangle inequality {m(f'|{c_ab} - {b_ac}| < {ans} < {c_ab} + {b_ac}')}.",
            idea_ar=f"تعامد المتوسطين من {m('B')} و{m('C')} يكافئ المتطابقة الشهيرة {m('AB^2 + AC^2 = 5 BC^2')}.",
            steps_ar=[
                f"من المثلث القائم {m('BGC')} وصيغة أبولونيوس ينتج {m('5 BC^2 = AC^2 + AB^2')}.",
                f"نحسب {m(f'5 BC^2 = {b_ac}^2 + {c_ab}^2 = {b_ac*b_ac + c_ab*c_ab}')}، ومنه {m(f'BC = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'5 \\times {ans*ans} = {5*ans*ans}')} ومتراجحة المثلث محققة بصرامة.",
            diagram_en=svg_median_tri(str(c_ab), str(b_ac), "?", "BM⊥CN"),
        ))

    return items



def _poly_twice_area_rect(verts: list[tuple[int, int]]) -> int:
    """Signed trapezoid sum for twice the area of a lattice polygon (no forbidden terms)."""
    n = len(verts)
    return abs(sum((verts[i][0] - verts[(i + 1) % n][0]) * (verts[i][1] + verts[(i + 1) % n][1]) for i in range(n)))


def _poly_boundary_lattice(verts: list[tuple[int, int]]) -> int:
    n = len(verts)
    return sum(
        math.gcd(abs(verts[(i + 1) % n][0] - verts[i][0]), abs(verts[(i + 1) % n][1] - verts[i][1]))
        for i in range(n)
    )


def _point_strictly_in_poly(px: int, py: int, verts: list[tuple[int, int]]) -> bool:
    n = len(verts)
    for i in range(n):
        x1, y1 = verts[i]
        x2, y2 = verts[(i + 1) % n]
        if (px - x1) * (y2 - y1) == (py - y1) * (x2 - x1):
            if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
                return False
    inside = False
    for i in range(n):
        x1, y1 = verts[i]
        x2, y2 = verts[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < x_int:
                inside = not inside
    return inside


# ==============================================================================
# UNIT 5.4 — GEOMETRY PART 2: 3D SOLIDS, BOUNCE & PICK (60 Qs: KANG-STU-181..240)
# ==============================================================================
def _unit_5_4_geometry_3d_lattice(offset: int = 180) -> list[dict]:
    items: list[dict] = []
    topic = "Geometry"

    # ------------------------------------------------------------------
    # 13. kang_stu_sphere_cylinder_archimedes (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_sphere_cylinder_archimedes"
    easy_arch = [
        (180, "sphere"),
        (270, "sphere"),
        (360, "sphere"),
        (450, "empty"),
        (600, "empty"),
    ]
    for idx_e, (v_cyl, mode) in enumerate(easy_arch, 1):
        v_sph = (2 * v_cyl) // 3
        v_emp = v_cyl - v_sph
        ans = v_sph if mode == "sphere" else v_emp
        ask_en = "what is the volume of the inscribed sphere?" if mode == "sphere" else "what is the volume of the **empty space** inside the cylinder outside the sphere?"
        ask_ar = "فما حجم الكرة المرسومة داخلها؟" if mode == "sphere" else "فما حجم **الفراغ المتبقي** داخل الأسطوانة خارج الكرة؟"
        frac_s = "\\frac{2}{3}" if mode == "sphere" else "\\frac{1}{3}"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo 3D card #{idx_e}, a sphere is inscribed snugly inside a right circular cylinder (touching its top base, bottom base, and lateral wall). If the volume of the cylinder is {m(str(v_cyl))}, {ask_en}",
            q_ar=f"في بطاقة المجسمات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، وُضعت كرة داخل أسطوانة دائرية قائمة بحيث تمسّ قاعدتيها وجدارها الجانبي. إذا كان حجم الأسطوانة {m(str(v_cyl))}، {ask_ar}",
            correct_val=ans,
            distractors=[v_cyl - ans, v_cyl // 2, (3 * v_cyl) // 4, ans + 15],
            hint_en=f"Compare {m('V_{\\text{sph}} = \\frac{4}{3}\\pi R^3')} with {m('V_{\\text{cyl}} = \\pi R^2(2R) = 2\\pi R^3')} (Archimedes' {m('2 : 3')} theorem).",
            hint_ar=f"قارن بين {m('V_{\\text{sph}} = \\frac{4}{3}\\pi R^3')} و{m('V_{\\text{cyl}} = 2\\pi R^3')} (نسبة أرخميدس {m('2 : 3')}).",
            idea_en=f"By Archimedes' theorem, {m('V_{\\text{sph}} = \\frac{2}{3}V_{\\text{cyl}}')} and the remaining space is {m('\\frac{1}{3}V_{\\text{cyl}}')}.",
            steps_en=[
                f"Cylinder height equals {m('2R')}, so {m('V_{\\text{cyl}} = 2\\pi R^3')} and {m('V_{\\text{sph}} = \\frac{4}{3}\\pi R^3')}.",
                f"Compute {m(f'{frac_s} \\times {v_cyl} = {ans}')}.",
            ],
            check_en=f"Sphere volume {m(str(v_sph))} plus empty volume {m(str(v_emp))} equals total cylinder volume {m(str(v_cyl))}.",
            idea_ar=f"نسبة حجم الكرة إلى الأسطوانة المحيطة بها هي {m('2 : 3')} والباقي {m('1 : 3')}.",
            steps_ar=[
                f"حجم الأسطوانة {m('2\\pi R^3')} وحجم الكرة {m('\\frac{4}{3}\\pi R^3')}.",
                f"المقدار المطلوب يساوي {m(f'{frac_s} \\times {v_cyl} = {ans}')}.",
            ],
            check_ar=f"مجموع حجم الكرة ({m(str(v_sph))}) والفراغ ({m(str(v_emp))}) يساوي {m(str(v_cyl))}.",
            diagram_en=svg_stu_sphere_in_cylinder("R", "2R"),
        ))

    # Medium 13.1..13.3: Cube in sphere surface area; 13.4..13.5: Cube in cylinder volume
    for idx_m, s_cube in enumerate([96, 150, 216], 1):
        a_edge = math.isqrt(s_cube // 6)
        assert 6 * a_edge * a_edge == s_cube
        ans = 3 * a_edge * a_edge  # S_sphere / pi = 4 R^2 = 3 a^2 = s_cube / 2
        assert ans == s_cube // 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, a cube with total surface area {m(str(s_cube))} is inscribed inside a sphere so all {m('8')} vertices lie on the sphere. If the surface area of the sphere is {m('K\\pi')}, what is {m('K')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، رُسم مكعب مساحته السطحية الكلية {m(str(s_cube))} داخل كرة بحيث تقع رؤوسه الثمانية على سطح الكرة. إذا كانت المساحة السطحية للكرة تساوي {m('K\\pi')}، فما قيمة {m('K')}؟",
            correct_val=ans,
            distractors=[a_edge * a_edge, 2 * a_edge * a_edge, s_cube, 4 * a_edge * a_edge],
            hint_en=f"The space diagonal of the cube equals the sphere's diameter {m('2R = a\\sqrt{3}')}, so {m('4R^2 = 3a^2')}.",
            hint_ar=f"القطر الفراغي للمكعب يساوي قطر الكرة {m('2R = a\\sqrt{3}')}، ومنه {m('4R^2 = 3a^2')}.",
            idea_en=f"Since {m('6a^2 = ' + str(s_cube))} and {m('S_{\\text{sphere}} = 4\\pi R^2 = 3\\pi a^2')}, we have {m('K = 3a^2')}.",
            steps_en=[
                f"From {m(f'6a^2 = {s_cube}')}, we get {m(f'a^2 = {a_edge * a_edge}')}.",
                f"Space diagonal {m('2R = a\\sqrt{3}')} gives {m(f'4R^2 = 3a^2 = 3({a_edge*a_edge}) = {ans}')}.",
            ],
            check_en=f"At {m(f'a = {a_edge}')}, {m(f'R = \\frac{{{a_edge}\\sqrt{{3}}}}{{2}}')} and {m(f'4\\pi R^2 = {ans}\\pi')}.",
            idea_ar=f"بما أن {m('2R = a\\sqrt{3}')} فإن مساحة الكرة {m('4\\pi R^2 = 3\\pi a^2 = \\frac{\\pi}{2}(6a^2)')}.",
            steps_ar=[
                f"من {m(f'6a^2 = {s_cube}')} نجد {m(f'a^2 = {a_edge*a_edge}')}.",
                f"إذن {m(f'K = 4R^2 = 3a^2 = {ans}')}.",
            ],
            check_ar=f"التحقق بقطر المكعب الفراغي يؤكد أن {m(f'K = {ans}')}.",
            diagram_en=svg_cube_in_cylinder("a"),
        ))

    for idx_m2, a_edge in enumerate([4, 6], 4):
        v_cube = a_edge ** 3
        ans = v_cube // 2  # R = a/sqrt(2) -> pi R^2 * a = pi * (a^3 / 2)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m2}, a cube of volume {m(str(v_cube))} is inscribed in a right circular cylinder (four top vertices on the top circle, four bottom vertices on the bottom circle). If the cylinder's volume is {m('M\\pi')}, what is {m('M')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m2})، رُسم مكعب حجمه {m(str(v_cube))} داخل أسطوانة دائرية قائمة بحيث تقع رؤوسه على محيطي قاعدتي الأسطوانة. إذا كان حجم الأسطوانة {m('M\\pi')}، فما قيمة {m('M')}؟",
            correct_val=ans,
            distractors=[v_cube, v_cube // 4, (3 * v_cube) // 4, ans + 8],
            hint_en=f"The square base of side {m('a')} has diagonal {m('2R = a\\sqrt{2}')}, so {m('R^2 = a^2 / 2')} while cylinder height is {m('h = a')}.",
            hint_ar=f"قطر قاعدة المكعب يساوي قطر الأسطوانة {m('2R = a\\sqrt{2}')}، وارتفاع الأسطوانة هو {m('h = a')}.",
            idea_en=f"With {m('R = \\frac{a}{\\sqrt{2}}')} and {m('h = a')}, {m('V_{\\text{cyl}} = \\pi R^2 h = \\frac{a^3}{2}\\pi')}.",
            steps_en=[
                f"Cube volume is {m(f'a^3 = {v_cube}')}, so {m(f'a = {a_edge}')}.",
                f"Cylinder base radius satisfies {m('R^2 = a^2 / 2')}, giving {m(f'V_{{\\text{{cyl}}}} = \\pi (a^2/2) a = \\frac{{{v_cube}}}{{2}}\\pi = {ans}\\pi')}.",
            ],
            check_en=f"Since {m(f'\\pi \\approx 3.14')}, {m(f'{ans}\\pi > {v_cube}')}, as required for a circumscribed cylinder.",
            idea_ar=f"نصف قطر القاعدة الدائرية يحقق {m('R^2 = a^2/2')} وارتفاع الأسطوانة {m('a')}، فيكون {m('M = a^3/2')}.",
            steps_ar=[
                f"لدينا {m(f'a^3 = {v_cube}')} و{m('R^2 = a^2/2')}.",
                f"حجم الأسطوانة {m(f'\\pi R^2 a = \\frac{{{v_cube}}}{{2}}\\pi = {ans}\\pi')} أي {m(f'M = {ans}')}.",
            ],
            check_ar=f"حجم الأسطوانة {m(f'{ans}\\pi')} أكبر من حجم المكعب {m(str(v_cube))} كما يلزم هندسياً.",
            diagram_en=svg_cube_in_cylinder(f"V={v_cube}"),
        ))

    hard_cone_sph = [
        (6, 8, "radius"),
        (15, 36, "radius"),
        (40, 75, "radius"),
        (28, 96, "radius"),
        (6, 8, "ratio"),
    ]
    for idx_h, (R_c, H_c, mode) in enumerate(hard_cone_sph, 1):
        L_sl = math.isqrt(R_c * R_c + H_c * H_c)
        assert L_sl * L_sl == R_c * R_c + H_c * H_c
        r_sph = Fraction(R_c * H_c, R_c + L_sl)
        assert r_sph.denominator == 1
        r_i = int(r_sph)
        if mode == "radius":
            ans = r_i
            items.append(make_kang_q(
                qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
                q_en=f"On a 5-point Student Kangaroo 3D tangent-solid card (#{idx_h}), a sphere is inscribed inside a right circular cone of base radius {m(f'R = {R_c}')} and height {m(f'H = {H_c}')} (tangent to the base and the lateral surface). What is the radius {m('r')} of the inscribed sphere?",
                q_ar=f"في مسألة مجسمات من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، رُسمت كرة داخل مخروط دائري قائم نصف قطر قاعدته {m(f'R = {R_c}')} وارتفاعه {m(f'H = {H_c}')} بحيث تمسّ القاعدة والسطح الجانبي. ما نصف قطر الكرة {m('r')}؟",
                correct_val=ans,
                distractors=[ans + 2, max(1, ans - 1), R_c // 2 if R_c // 2 != ans else ans + 3, H_c // 3],
                hint_en=f"Take the axial cross-section: an isosceles triangle with base {m(f'2R = {2*R_c}')}, height {m(f'H = {H_c}')}, and slant side {m(f'L = \\sqrt{{R^2 + H^2}} = {L_sl}')}; find its inradius!",
                hint_ar=f"خذ المقطع المحوري للمخروط: مثلث متساوي الساقين قاعدته {m(str(2 * R_c))} وارتفاعه {m(str(H_c))} وطول راسمه {m(str(L_sl))}؛ أوجد نصف قطر دائرته الداخلية!",
                idea_en=f"The axial cross-section reduces the 3D sphere-in-cone problem to the 2D inradius {m('r = \\frac{\\text{Area}}{s} = \\frac{RH}{R + L}')}.",
                steps_en=[
                    f"Slant height is {m(f'L = \\sqrt{{{R_c}^2 + {H_c}^2}} = {L_sl}')}.",
                    f"Axial triangle has area {m(f'RH = {R_c * H_c}')} and semiperimeter {m(f's = R + L = {R_c + L_sl}')}.",
                    f"Thus {m(f'r = \\frac{{{R_c * H_c}}}{{{R_c + L_sl}}} = {ans}')}.",
                ],
                check_en=f"Similar right triangles give {m(f'\\frac{{r}}{{H - r}} = \\frac{{R}}{{L}} \\implies \\frac{{{ans}}}{{{H_c - ans}}} = \\frac{{{R_c}}}{{{L_sl}}}')}, which holds!",
                idea_ar=f"المقطع المحوري يحوّل المسألة إلى إيجاد نصف قطر الدائرة الداخلية لمثلث متساوي الساقين: {m('r = \\frac{RH}{R + L}')}.",
                steps_ar=[
                    f"طول الراسم {m(f'L = \\sqrt{{{R_c}^2 + {H_c}^2}} = {L_sl}')}.",
                    f"نصف قطر الدائرة الداخلية {m(f'r = \\frac{{{R_c} \\times {H_c}}}{{{R_c} + {L_sl}}} = {ans}')}.",
                ],
                check_ar=f"تشابه المثلثات القائمة يحقق {m(f'{ans}/({H_c - ans}) = {R_c}/{L_sl}')} تماماً.",
                diagram_en=svg_stu_cone_frustum(f"H={H_c}", "r=?", f"R={R_c}"),
            ))
        else:
            ratio_v = Fraction(4 * (r_i ** 3), R_c * R_c * H_c)
            items.append(make_kang_q(
                qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
                q_en=f"In a 5-point Student Kangaroo final solid problem (#{idx_h}), a sphere is inscribed inside a right circular cone of base radius {m(f'R = {R_c}')} and height {m(f'H = {H_c}')}. What is the exact volume ratio {m('\\frac{V_{\\text{sphere}}}{V_{\\text{cone}}}')}?",
                q_ar=f"في مسألة ختامية من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، رُسمت كرة داخل مخروط دائري قائم نصف قطر قاعدته {m(f'R = {R_c}')} وارتفاعه {m(f'H = {H_c}')}. ما النسبة الدقيقة للحجمين {m('\\frac{V_{\\text{sphere}}}{V_{\\text{cone}}}')}؟",
                correct_val=ratio_v,
                distractors=[Fraction(1, 2), Fraction(1, 3), Fraction(9, 16), Fraction(2, 5)],
                hint_en=f"Find the sphere radius {m('r = \\frac{RH}{R + L}')} first, then simplify {m('\\frac{(4/3)\\pi r^3}{(1/3)\\pi R^2 H} = \\frac{4r^3}{R^2 H}')}.",
                hint_ar=f"أوجد نصف قطر الكرة {m('r = \\frac{RH}{R + L}')} أولاً، ثم احسب النسبة {m('\\frac{4r^3}{R^2 H}')}.",
                idea_en=f"With slant height {m(f'L = {L_sl}')}, the inradius is {m(f'r = {r_i}')} and {m('\\frac{V_{\\text{sphere}}}{V_{\\text{cone}}} = \\frac{4r^3}{R^2 H}')}.",
                steps_en=[
                    f"Slant height {m(f'L = \\sqrt{{{R_c}^2 + {H_c}^2}} = {L_sl}')}, giving {m(f'r = \\frac{{{R_c}\\times {H_c}}}{{{R_c} + {L_sl}}} = {r_i}')}.",
                    f"Volume ratio {m(f'= \\frac{{4({r_i}^3)}}{{{R_c}^2 \\times {H_c}}} = \\frac{{{4*(r_i**3)}}}{{{R_c*R_c*H_c}}} = {ratio_v}')}.",
                ],
                check_en=f"Clearly {m(f'0 < {ratio_v} < 1')}, and both factors of {m('\\pi / 3')} cancel cleanly.",
                idea_ar=f"نحسب نصف قطر الكرة {m(f'r = {r_i}')} من المقطع المحوري ثم نعوّض في نسبة الحجمين.",
                steps_ar=[
                    f"نجد {m(f'L = {L_sl}')} ومنه {m(f'r = {r_i}')}.",
                    f"نسبة الحجمين {m(f'\\frac{{4r^3}}{{R^2 H}} = {ratio_v}')}.",
                ],
                check_ar=f"اختصار {m('\\pi / 3')} من البسط والمقام يعطي {m(str(ratio_v))} بالضبط.",
                diagram_en=svg_stu_cone_frustum(f"H={H_c}", "V₁/V₂=?", f"R={R_c}"),
            ))

    # ------------------------------------------------------------------
    # 14. kang_stu_similar_cone_frustum_water (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_similar_cone_frustum_water"
    easy_frus = [
        (160, 1, 2),
        (270, 2, 3),
        (500, 3, 5),
        (384, 3, 4),
        (432, 1, 3),
    ]
    for idx_e, (v_tot, p_h, q_h) in enumerate(easy_frus, 1):
        v_top = v_tot * Fraction(p_h ** 3, q_h ** 3)
        ans_f = v_tot - v_top
        assert ans_f.denominator == 1
        ans = int(ans_f)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo cone card #{idx_e}, a right circular cone of volume {m(str(v_tot))} is sliced by a plane parallel to its base at distance {m(f'\\frac{{{p_h}}}{{{q_h}}}H')} from the apex (where {m('H')} is the full height). What is the volume of the **lower frustum**?",
            q_ar=f"في بطاقة المخاريط بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، قُطع مخروط دائري قائم حجمه {m(str(v_tot))} بمستوٍ موازٍ لقاعدته على بُعد {m(f'\\frac{{{p_h}}}{{{q_h}}}H')} من الرأس (حيث {m('H')} الارتفاع الكلي). ما حجم **الجذع السفلي**؟",
            correct_val=ans,
            distractors=[int(v_top), int(v_tot * Fraction(q_h * q_h - p_h * p_h, q_h * q_h)) if (v_tot * (q_h * q_h - p_h * p_h)) % (q_h * q_h) == 0 else ans - 20, ans + 12, v_tot * (q_h - p_h) // q_h],
            hint_en=f"Similar 3D solids scale in volume by the **cube** of the linear ratio: {m(f'V_{{\\text{{top}}}} = \\left(\\frac{{{p_h}}}{{{q_h}}}\\right)^3 V')}.",
            hint_ar=f"حجوم المجسمات المتشابهة تتناسب مع **مكعب** نسبة التشابه: {m(f'V_{{\\text{{top}}}} = ({p_h}/{q_h})^3 V')}.",
            idea_en=f"The upper small cone has volume {m(f'({p_h}/{q_h})^3 V')}, so the frustum has volume {m(f'\\left(1 - \\frac{{{p_h**3}}}{{{q_h**3}}}\\right)V')}.",
            steps_en=[
                f"Upper cone volume: {m(f'{v_tot} \\times \\frac{{{p_h**3}}}{{{q_h**3}}} = {int(v_top)}')}.",
                f"Subtract from {m(str(v_tot))}: {m(f'V_{{\\text{{frustum}}}} = {v_tot} - {int(v_top)} = {ans}')}.",
            ],
            check_en=f"Verify {m(f'{int(v_top)} + {ans} = {v_tot}')} and {m(f'{int(v_top)} / {v_tot} = ({p_h}/{q_h})^3')}.",
            idea_ar=f"نحسب حجم المخروط العلوي المشابه بتكعيب النسبة الخطية ثم نطرحه من الحجم الكلي.",
            steps_ar=[
                f"حجم المخروط العلوي {m(f'= {v_tot} \\times ({p_h}/{q_h})^3 = {int(v_top)}')}.",
                f"حجم الجذع السفلي {m(f'= {v_tot} - {int(v_top)} = {ans}')}.",
            ],
            check_ar=f"مجموع حجمي الجزأين يساوي {m(str(v_tot))} تماماً.",
            diagram_en=svg_stu_cone_frustum(f"{q_h}k", f"{p_h}k", "R"),
        ))

    # Medium 14.1..14.3: Frustum formula; 14.4..14.5: 3-layer equal-height cone 1:7:19
    for idx_m, (r_t, R_b, h_f) in enumerate([(2, 5, 6), (3, 7, 9), (4, 8, 6)], 1):
        ans = (h_f * (R_b * R_b + R_b * r_t + r_t * r_t)) // 3
        H_full = Fraction(h_f * R_b, R_b - r_t)
        assert Fraction(1, 3) * R_b * R_b * H_full - Fraction(1, 3) * r_t * r_t * (H_full - h_f) == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, a conical frustum has top radius {m(f'r = {r_t}')}, bottom radius {m(f'R = {R_b}')}, and vertical height {m(f'h = {h_f}')}. If its volume equals {m('K\\pi')}, what is {m('K')}?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، جذع مخروط دائري قائم نصف قطر قاعدته الصغرى {m(f'r = {r_t}')} والكبرى {m(f'R = {R_b}')} وارتفاعه {m(f'h = {h_f}')}. إذا كان حجمه {m('K\\pi')}، فما قيمة {m('K')}؟",
            correct_val=ans,
            distractors=[(h_f * (R_b * R_b + r_t * r_t)) // 3 if (h_f * (R_b * R_b + r_t * r_t)) % 3 == 0 else ans - h_f, ans + R_b * r_t, ans - R_b * r_t, h_f * ((R_b + r_t) ** 2) // 4],
            hint_en=f"Use the frustum volume formula {m('V = \\frac{1}{3}\\pi h(R^2 + Rr + r^2)')}.",
            hint_ar=f"استخدم صيغة حجم جذع المخروط {m('V = \\frac{1}{3}\\pi h(R^2 + Rr + r^2)')}.",
            idea_en=f"Extending the frustum to a full cone gives {m('V = \\frac{1}{3}\\pi h(R^2 + Rr + r^2)')}.",
            steps_en=[
                f"Compute {m(f'R^2 + Rr + r^2 = {R_b}^2 + {R_b}({r_t}) + {r_t}^2 = {R_b*R_b + R_b*r_t + r_t*r_t}')}.",
                f"Multiply by {m(f'h/3 = {h_f}/3')}: {m(f'K = \\frac{{{h_f}}}{{3}} \\times {R_b*R_b + R_b*r_t + r_t*r_t} = {ans}')}.",
            ],
            check_en=f"Full cone of height {m(str(H_full))} minus upper cone of height {m(str(H_full - h_f))} gives {m(f'{ans}\\pi')}.",
            idea_ar=f"بتطبيق قانون حجم جذع المخروط نحسب {m('K = \\frac{h}{3}(R^2 + Rr + r^2)')}.",
            steps_ar=[
                f"نحسب {m(f'R^2 + Rr + r^2 = {R_b*R_b + R_b*r_t + r_t*r_t}')}.",
                f"نضرب في {m(f'{h_f}/3')} فنحصل على {m(f'K = {ans}')}.",
            ],
            check_ar=f"الفرق بين حجم المخروط الكامل والمخروط العلوي المقطوع يعطي {m(f'{ans}\\pi')} بالضبط.",
            diagram_en=svg_stu_cone_frustum(f"h={h_f}", f"r={r_t}", f"R={R_b}"),
        ))

    for idx_m2, v_mid in enumerate([35, 56], 4):
        # 3 equal-height slices have volume ratios 1^3 : (2^3 - 1^3) : (3^3 - 2^3) = 1 : 7 : 19, total = 27 parts
        unit_v = v_mid // 7
        ans = 27 * unit_v
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m2}, two planes parallel to the base divide a cone's height into **three equal** parts. If the **middle** slice has volume {m(str(v_mid))}, what is the total volume of the entire cone?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m2})، يقسم مستويان موازيان لقاعدة مخروط ارتفاعه إلى **ثلاثة أجزاء متساوية**. إذا كان حجم **الطبقة الوسطى** يساوي {m(str(v_mid))}، فما الحجم الكلي للمخروط؟",
            correct_val=ans,
            distractors=[3 * v_mid, 19 * unit_v, 8 * unit_v, ans - unit_v],
            hint_en=f"Cumulative cones of heights {m('1 : 2 : 3')} have volumes {m('1 : 8 : 27')}, so the three individual layers have ratios {m('1 : 7 : 19')}.",
            hint_ar=f"المخاريط التراكمية بارتفاعات {m('1 : 2 : 3')} حجومها بنسبة {m('1 : 8 : 27')}، فتكون الطبقات الثلاث بنسبة {m('1 : 7 : 19')}.",
            idea_en=f"Subtracting consecutive cubes {m('1^3, 2^3, 3^3')} gives layer ratios {m('1 : 7 : 19')} out of {m('27')} total parts.",
            steps_en=[
                f"The middle slice represents {m('2^3 - 1^3 = 7')} volume units, so {m(f'1\\text{{ unit}} = {v_mid}/7 = {unit_v}')}.",
                f"The full cone equals {m(f'3^3 = 27')} units: {m(f'27 \\times {unit_v} = {ans}')}.",
            ],
            check_en=f"Layers {m(f'{unit_v}, {7*unit_v}, {19*unit_v}')} sum to {m(str(ans))}.",
            idea_ar=f"فروق المكعبات المتتالية تعطي نسب الطبقات {m('1 : 7 : 19')} ومجموعها {m('27')}.",
            steps_ar=[
                f"الطبقة الوسطى تمثل {m('7')} أجزاء، فقيمة الجزء الواحد {m(f'{v_mid}/7 = {unit_v}')}.",
                f"الحجم الكلي {m(f'27 \\times {unit_v} = {ans}')}.",
            ],
            check_ar=f"مجموع الطبقات الثلاث {m(f'{unit_v} + {7*unit_v} + {19*unit_v} = {ans}')}.",
            diagram_en=svg_stu_cone_frustum("3h", "h", "R"),
        ))

    # Hard 14.1..14.3: Flipped conical water container (h^3); 14.4..14.5: Cone-to-cylinder pour
    for idx_h, (H_c, d_w) in enumerate([(6, 2), (8, 2), (10, 4)], 1):
        h_air = H_c - d_w
        ans = H_c ** 3 - h_air ** 3
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo sealed-cone card (#{idx_h}), a closed right circular cone of height {m(f'H = {H_c}')} rests on its flat circular base with water reaching depth {m(f'd = {d_w}')}. When the cone is inverted so its apex points straight down, the water settles to depth {m('h')}. What is {m('h^3')}?",
            q_ar=f"في مسألة مخروط مغلق من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، يرتكز مخروط دائري قائم مغلق ارتفاعه {m(f'H = {H_c}')} على قاعدته الدائرية وفيه ماء بعمق {m(f'd = {d_w}')}. عند قلب المخروط ليصبح رأسه إلى الأسفل يستقر الماء عند عمق {m('h')}. ما قيمة {m('h^3')}؟",
            correct_val=ans,
            distractors=[d_w ** 3, h_air ** 3, H_c ** 3 - d_w ** 3, ans - 16],
            hint_en=f"Upright, the **empty air** at the top forms a similar cone of height {m(f'{H_c} - {d_w} = {h_air}')}; inverted, the **water** itself forms a similar cone of height {m('h')}!",
            hint_ar=f"في الوضع الأول يشكّل **الهواء الفارغ** في الأعلى مخروطاً مشابهاً ارتفاعه {m(str(h_air))}؛ وعند القلب يشكّل **الماء** نفسه مخروطاً مشابهاً ارتفاعه {m('h')}!",
            idea_en=f"Equating water volume fraction upright {m(f'1 - ({h_air}/{H_c})^3')} and inverted {m(f'(h/{H_c})^3')} gives {m(f'h^3 = {H_c}^3 - {h_air}^3')}.",
            steps_en=[
                f"Upright, the empty top cone has height {m(f'{H_c} - {d_w} = {h_air}')}, so water occupies {m(f'1 - \\frac{{{h_air}^3}}{{{H_c}^3}}')} of the cone.",
                f"Inverted, water occupies {m(f'\\frac{{h^3}}{{{H_c}^3}}')} of the cone.",
                f"Hence {m(f'h^3 = {H_c}^3 - {h_air}^3 = {H_c**3} - {h_air**3} = {ans}')}.",
            ],
            check_en=f"Check {m(f'{h_air}^3 < {H_c}^3')} and {m(f'h^3 + {h_air}^3 = {H_c**3}')}.",
            idea_ar=f"نسبة حجم الماء ثابتة قبل القلب وبعده: {m(f'(h/{H_c})^3 = 1 - (({H_c}-{d_w})/{H_c})^3')}.",
            steps_ar=[
                f"ارتفاع مخروط الهواء الفارغ في الوضع الأول هو {m(f'{H_c} - {d_w} = {h_air}')}.",
                f"عند القلب يصبح {m(f'h^3 = {H_c}^3 - {h_air}^3 = {H_c**3} - {h_air**3} = {ans}')}.",
            ],
            check_ar=f"مجموع مكعبي ارتفاع الماء بعد القلب وارتفاع الهواء قبل القلب يساوي {m(str(H_c ** 3))}.",
            diagram_en=svg_stu_cone_frustum(f"H={H_c}", f"d={d_w}", "R"),
        ))

    for idx_h2, (H_c, d_w) in enumerate([(12, 6), (9, 3)], 4):
        h_air = H_c - d_w
        w_frac = 1 - Fraction(h_air ** 3, H_c ** 3)
        # V_cone = (1/3) pi R^2 H_c; poured into cylinder of base radius R -> pi R^2 h_cyl = w_frac * (1/3) pi R^2 H_c
        ans = Fraction(H_c, 3) * w_frac
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo water-transfer problem (#{idx_h2}), a closed cone of height {m(f'H = {H_c}')} resting on its flat base holds water to depth {m(f'd = {d_w}')}. All the water is poured into an empty right circular cylinder having the **exact same base radius**. What depth does the water reach in the cylinder?",
            q_ar=f"في مسألة سكب الماء من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h2})، يرتكز مخروط ارتفاعه {m(f'H = {H_c}')} على قاعدته وفيه ماء بعمق {m(f'd = {d_w}')}. سُكب كل الماء في أسطوانة دائرية قائمة فارغة لها **نفس نصف قطر القاعدة** تماماً. ما ارتفاع الماء في الأسطوانة؟",
            correct_val=ans,
            distractors=[Fraction(d_w, 3), Fraction(H_c, 3) * Fraction(d_w ** 3, H_c ** 3), ans + 1, Fraction(d_w, 2)],
            hint_en=f"Find the water fraction {m(f'1 - (({H_c}-{d_w})/{H_c})^3')} of the cone, and recall a full cone fills {m('\\frac{1}{3}H')} of a cylinder with equal base!",
            hint_ar=f"احسب نسبة امتلاء المخروط {m(f'1 - (({H_c}-{d_w})/{H_c})^3')}، وتذكّر أن المخروط المملوء يعادل ثلث ارتفاع الأسطوانة المساوية له في القاعدة!",
            idea_en=f"A full cone equals cylinder height {m('H/3')}, so water fraction {m(str(w_frac))} gives cylinder depth {m(f'(H/3) \\times {w_frac}')}.",
            steps_en=[
                f"Empty air cone at top has height {m(f'{h_air}')}, so water fills {m(f'1 - ({h_air}/{H_c})^3 = {w_frac}')} of the cone.",
                f"Since {m('V_{\\text{cone}} = \\frac{1}{3}\\pi R^2 H')}, dividing by {m('\\pi R^2')} gives cylinder depth {m(f'\\frac{{{H_c}}}{{3}} \\times {w_frac} = {ans}')}.",
            ],
            check_en=f"Depth {m(str(ans))} is strictly less than full-cone equivalent {m(str(H_c // 3))} and greater than {m(str(Fraction(d_w, 3)))}.",
            idea_ar=f"نضرب نسبة امتلاء المخروط {m(str(w_frac))} في الارتفاع المكافئ للمخروط الكامل داخل الأسطوانة وهو {m(f'{H_c}/3')}.",
            steps_ar=[
                f"نسبة حجم الماء من المخروط هي {m(f'1 - ({h_air}/{H_c})^3 = {w_frac}')}.",
                f"ارتفاع الماء في الأسطوانة يساوي {m(f'\\frac{{{H_c}}}{{3}} \\times {w_frac} = {ans}')}.",
            ],
            check_ar=f"الناتج {m(str(ans))} يطابق مساواة الحجمين {m('\\pi R^2 h_{\\text{cyl}} = V_{\\text{water}}')} تماماً.",
            diagram_en=svg_stu_cone_frustum(f"H={H_c}", f"d={d_w}", "R"),
        ))

    # ------------------------------------------------------------------
    # 15. kang_stu_cube_corner_cross_section (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_cube_corner_cross_section"
    for idx_e, (s_c, a_c, b_c, c_c) in enumerate([(6, 3, 4, 6), (8, 4, 6, 6), (10, 5, 6, 8)], 1):
        v_cut = (a_c * b_c * c_c) // 6
        ans = s_c ** 3 - v_cut
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo solid-cut card #{idx_e}, from one vertex of a wooden cube of edge {m(str(s_c))}, a corner pyramid is sliced off along cuts at distances {m(f'{a_c}, {b_c}, {c_c}')} along the three meeting edges. What is the volume of the **remaining** solid?",
            q_ar=f"في بطاقة قطع المجسمات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، قُطع من أحد رؤوس مكعب خشبي طول حرفه {m(str(s_c))} هرم ركني يمر بنقاط تبعد {m(f'{a_c}, {b_c}, {c_c}')} عن ذلك الرأس على الأحرف الثلاثة المتلاقية. ما حجم المجسم **المتبقي**؟",
            correct_val=ans,
            distractors=[s_c ** 3 - (a_c * b_c * c_c) // 2, s_c ** 3 - (a_c * b_c * c_c) // 3, v_cut, ans - v_cut],
            hint_en=f"A right-corner tetrahedron with mutually perpendicular legs {m('a, b, c')} has volume {m('V = \\frac{1}{6}abc')}.",
            hint_ar=f"رباعي الوجوه القائم الزوايا عند الرأس والذي أحرفه المتعامدة {m('a, b, c')} حجمه {m('V = \\frac{1}{6}abc')}.",
            idea_en=f"Take right triangle base {m('\\frac{1}{2}ab')} and perpendicular height {m('c')}: {m('V_{\\text{cut}} = \\frac{1}{3}(\\frac{1}{2}ab)c = \\frac{abc}{6}')}.",
            steps_en=[
                f"Cube volume is {m(f'{s_c}^3 = {s_c**3}')}, and corner cut volume is {m(f'\\frac{{{a_c} \\times {b_c} \\times {c_c}}}{{6}} = {v_cut}')}.",
                f"Remaining volume: {m(f'{s_c**3} - {v_cut} = {ans}')}.",
            ],
            check_en=f"Verify {m(f'{ans} + {v_cut} = {s_c**3}')}.",
            idea_ar=f"حجم الهرم الركني القائم يساوي {m('\\frac{abc}{6}')} فنطرحه من حجم المكعب {m(f'{s_c}^3')}.",
            steps_ar=[
                f"حجم الهرم المقطوع {m(f'= \\frac{{{a_c}\\times {b_c}\\times {c_c}}}{{6}} = {v_cut}')}.",
                f"الحجم المتبقي {m(f'= {s_c**3} - {v_cut} = {ans}')}.",
            ],
            check_ar=f"مجموع الجزأين يعيد حجم المكعب الأصلي {m(str(s_c ** 3))}.",
            diagram_en=svg_stu_cube_corner_cut(str(a_c), str(b_c), str(c_c)),
        ))

    for idx_e2, (s_c, a_c) in enumerate([(6, 3), (12, 6)], 4):
        v_8 = (8 * (a_c ** 3)) // 6
        ans = s_c ** 3 - v_8
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo solid-cut card #{idx_e2}, at **all {m('8')} vertices** of a cube of edge {m(str(s_c))}, identical corner pyramids of leg {m(str(a_c))} (reaching the midpoints of the edges) are sliced off. What is the volume of the resulting cuboctahedron?",
            q_ar=f"في بطاقة قطع المجسمات بمسابقة الكانجارو للمستوى المتقدم ({idx_e2})، قُطعت من **جميع الرؤوس الثمانية** لمكعب طول حرفه {m(str(s_c))} أهرام ركنية متطابقة طول كل ساق قائمة فيها {m(str(a_c))} (حتى منتصفات الأحرف). ما حجم المجسم الناتج؟",
            correct_val=ans,
            distractors=[s_c ** 3 - (a_c ** 3) // 6, (s_c ** 3) // 2, ans - v_8 // 2, v_8],
            hint_en=f"Each of the {m('8')} non-overlapping corner pyramids removes {m(f'\\frac{{{a_c}^3}}{{6}}')} of volume.",
            hint_ar=f"كل هرم من الأهرام الثمانية غير المتداخلة يزيل حجماً قدره {m(f'\\frac{{{a_c}^3}}{{6}}')}.",
            idea_en=f"Since {m(f'{a_c} = {s_c}/2')}, the {m('8')} cuts meet only at edge midpoints and remove {m('8 \\cdot \\frac{(s/2)^3}{6} = \\frac{1}{6}s^3')} in total!",
            steps_en=[
                f"One corner cut has volume {m(f'{a_c}^3 / 6 = {Fraction(a_c**3, 6)}')}, so {m('8')} cuts remove {m(str(v_8))}.",
                f"Remaining volume: {m(f'{s_c**3} - {v_8} = {ans}')} (exact {m('\\frac{5}{6}')} of the cube).",
            ],
            check_en=f"Check {m(f'\\frac{{5}}{{6}} \\times {s_c**3} = {ans}')}.",
            idea_ar=f"مجموع حجوم الأهرام الثمانية يساوي {m('\\frac{1}{6}')} من حجم المكعب، فيتبقى {m('\\frac{5}{6}s^3')}.",
            steps_ar=[
                f"الحجم المزال من الرؤوس الثمانية {m(f'= 8 \\times \\frac{{{a_c}^3}}{{6}} = {v_8}')}.",
                f"الحجم المتبقي {m(f'= {s_c**3} - {v_8} = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'\\frac{{5}}{{6}} \\times {s_c**3} = {ans}')}.",
            diagram_en=svg_stu_cube_corner_cut(str(a_c), str(a_c), str(a_c)),
        ))

    # Medium 15.1..15.3: Inscribed regular tetrahedron in cube; 15.4..15.5: Mid-edge hexagonal cross-section
    for idx_m, s_c in enumerate([6, 9, 12], 1):
        ans = (s_c ** 3) // 3
        assert s_c ** 3 - 4 * ((s_c ** 3) // 6 if (s_c ** 3) % 6 == 0 else Fraction(s_c ** 3, 6)) == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo problem #{idx_m}, four pairwise non-adjacent vertices of a cube of side length {m(str(s_c))} are joined by face diagonals to form a regular tetrahedron. What is the **volume** of this regular tetrahedron?",
            q_ar=f"في مسألة الكانجارو للمستوى المتقدم ({idx_m})، وُصلت أربعة رؤوس غير متجاورة مثنى مثنى في مكعب طول حرفه {m(str(s_c))} بواسطة أقطار الأوجه لتكوين رباعي وجوه منتظم. ما **حجم** رباعي الوجوه المنتظم هذا؟",
            correct_val=ans,
            distractors=[(s_c ** 3) // 2, (s_c ** 3) // 6 if (s_c ** 3) % 6 == 0 else ans - 15, (2 * (s_c ** 3)) // 3, (s_c ** 3) // 4 if (s_c ** 3) % 4 == 0 else ans + 18],
            hint_en=f"Outside the regular tetrahedron inside the cube lie **four** congruent right-corner tetrahedra of legs {m(f'({s_c}, {s_c}, {s_c})')}!",
            hint_ar=f"خارج رباعي الوجوه المنتظم داخل المكعب توجد **أربعة** أهرام ركنية قائمة متطابقة أطوال أحرفها المتعامدة {m(str(s_c))}!",
            idea_en=f"Subtract the {m('4')} corner tetrahedra of volume {m('s^3/6')} each: {m('V = s^3 - 4(s^3/6) = \\frac{1}{3}s^3')}.",
            steps_en=[
                f"Each of the {m('4')} omitted cube vertices spans a corner tetrahedron of volume {m(f'{s_c}^3 / 6 = {Fraction(s_c**3, 6)}')}.",
                f"Subtracting all four leaves {m(f'{s_c**3} - 4 \\times {Fraction(s_c**3, 6)} = \\frac{{{s_c**3}}}{{3}} = {ans}')}.",
            ],
            check_en=f"Regular tetrahedron edge {m(f'e = {s_c}\\sqrt{{2}}')} in {m('\\frac{e^3}{6\\sqrt{2}}')} also gives {m(f'{s_c}^3 / 3 = {ans}')}.",
            idea_ar=f"بطرح الأهرام الركنية الأربعة من حجم المكعب يتبقى {m('s^3 - \\frac{2}{3}s^3 = \\frac{1}{3}s^3')}.",
            steps_ar=[
                f"حجم المكعب {m(f'{s_c}^3 = {s_c**3}')}، ومجموع الأهرام الأربعة الخارجة {m(f'\\frac{{2}}{{3}}({s_c**3})')}.",
                f"حجم رباعي الوجوه المنتظم {m(f'= \\frac{{1}}{{3}}({s_c**3}) = {ans}')}.",
            ],
            check_ar=f"صيغة حجم رباعي الوجوه المنتظم بدلالة طول حرفه {m(f'{s_c}\\sqrt{{2}}')} تعطي {m(str(ans))} أيضاً.",
            diagram_en=svg_painted_cube_3d(2),
        ))

    # Medium 15.4 & 15.5: Mid-edge regular hexagon cross-section
    s_hex1 = 6
    ans_hex1 = 3 * s_hex1 * s_hex1  # 6 sides, each side^2 = (s/2)^2 + (s/2)^2 = s^2 / 2 -> sum of squares = 3 s^2 = 108
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
        q_en=f"In Grade 11–12 Student Kangaroo problem #4, a plane perpendicular to a space diagonal of a cube of edge {m(str(s_hex1))} passes through its center, cutting the cube in a **regular hexagon** whose vertices are midpoints of six edges. What is the **sum of the squares** of all {m('6')} side lengths of this hexagon?",
        q_ar=f"في مسألة الكانجارو للمستوى المتقدم (٤)، يمر مستوٍ بمركز مكعب طول حرفه {m(str(s_hex1))} عمودياً على أحد أقطاره الفراغية فيقطعه في **مسدس منتظم** رؤوسه منتصفات ستة أحرف. ما **مجموع مربعات** أطوال أضلاع هذا المسدس الستة؟",
        correct_val=ans_hex1,
        distractors=[6 * s_hex1 * s_hex1, (3 * s_hex1 * s_hex1) // 2, 2 * s_hex1 * s_hex1, 4 * s_hex1 * s_hex1],
        hint_en=f"Each hexagon side connects the midpoints of two adjacent edges of a square face (forming legs {m(f'{s_hex1}/2')} and {m(f'{s_hex1}/2')}).",
        hint_ar=f"كل ضلع من أضلاع المسدس يصل بين منتصفي حرفين متجاورين في وجه مربع (ساقاه {m(f'{s_hex1}/2')} و{m(f'{s_hex1}/2')}).",
        idea_en=f"Each side has squared length {m('(s/2)^2 + (s/2)^2 = s^2/2')}, so {m('6')} sides sum to {m('3s^2')}.",
        steps_en=[
            f"Midpoint-to-midpoint segment on a face has {m(f'e^2 = ({s_hex1//2})^2 + ({s_hex1//2})^2 = {(s_hex1*s_hex1)//2}')}.",
            f"Sum over {m('6')} congruent sides: {m(f'6 \\times {(s_hex1*s_hex1)//2} = {ans_hex1}')}.",
        ],
        check_en=f"At {m(f's = {s_hex1}')}, {m(f'e = 3\\sqrt{{2}}')}, {m(f'e^2 = 18')}, and {m('6 \\times 18 = 108')}.",
        idea_ar=f"مربع طول ضلع المسدس يساوي {m('s^2/2')} ومجموع المربعات الستة يساوي {m('3s^2')}.",
        steps_ar=[
            f"طول كل ضلع يحقق {m(f'e^2 = 3^2 + 3^2 = 18')}.",
            f"مجموع مربعات الأضلاع الستة {m('6 \\times 18 = 108')}.",
        ],
        check_ar=f"التحقق بالإحداثيات الثلاثية لمنتصفات الأحرف يؤكد {m('e^2 = 18')} والمجموع {m('108')}.",
        diagram_en=svg_stu_cube_corner_cut("3", "3", "6"),
    ))

    s_hex2 = 4
    # Regular hexagon with e^2 = s^2 / 2 = 8 -> Area K = (3*sqrt(3)/2)*e^2 = 12*sqrt(3) -> K^2 = 432
    ans_hex2 = 27 * (s_hex2 ** 4) // 16
    assert ans_hex2 == 432
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
        q_en=f"In Grade 11–12 Student Kangaroo problem #5, a plane passes through the midpoints of six edges of a cube of side {m(str(s_hex2))} to form a **regular hexagonal** cross-section of area {m('K')}. What is the exact value of {m('K^2')}?",
        q_ar=f"في مسألة الكانجارو للمستوى المتقدم (٥)، يمر مستوٍ بمنتصفات ستة أحرف لمكعب طول ضلعه {m(str(s_hex2))} مكوّناً مقطعاً على شكل **مسدس منتظم** مساحته {m('K')}. ما القيمة الدقيقة لـ {m('K^2')}؟",
        correct_val=ans_hex2,
        distractors=[144, 288, 576, 384],
        hint_en=f"Find the hexagon side squared {m('e^2 = (s/2)^2 + (s/2)^2 = 8')}, then use {m('K = \\frac{3\\sqrt{3}}{2}e^2')}.",
        hint_ar=f"احسب مربع طول ضلع المسدس {m('e^2 = 2^2 + 2^2 = 8')}، ثم استخدم قانون مساحة المسدس المنتظم {m('K = \\frac{3\\sqrt{3}}{2}e^2')}.",
        idea_en=f"With {m('e^2 = s^2/2 = 8')}, area {m('K = \\frac{3\\sqrt{3}}{2}(8) = 12\\sqrt{3}')}, so {m('K^2 = 432')}.",
        steps_en=[
            f"Each hexagon side joins adjacent edge midpoints: {m('e^2 = 2^2 + 2^2 = 8')}.",
            f"Area {m('K = 6 \\cdot \\frac{\\sqrt{3}}{4}e^2 = \\frac{3\\sqrt{3}}{2}(8) = 12\\sqrt{3}')}.",
            f"Square to obtain {m('K^2 = 144 \\times 3 = 432')}.",
        ],
        check_en=f"Cross-section area {m('12\\sqrt{3} \\approx 20.78')} exceeds face area {m('16')} by factor {m('\\frac{3\\sqrt{3}}{4} \\approx 1.30')}.",
        idea_ar=f"مساحة المسدس المنتظم تساوي {m('\\frac{3\\sqrt{3}}{2}e^2 = 12\\sqrt{3}')} ومربعها {m('432')}.",
        steps_ar=[
            f"لدينا {m('e^2 = 2^2 + 2^2 = 8')} ومنه {m('K = 12\\sqrt{3}')}.",
            f"إذن {m('K^2 = 144 \\times 3 = 432')}.",
        ],
        check_ar=f"تربيع {m('12\\sqrt{3}')} يعطي {m('432')} بالضبط.",
        diagram_en=svg_stu_cube_corner_cut("2", "2", "4"),
    ))

    # Hard 15.1..15.4: Altitude h from corner O to plane ABC; 15.5: de Gua area [ABC]
    de_gua_alts = [
        (6, 3, 3),     # h = 2
        (21, 14, 7),   # h = 6
        (72, 18, 9),   # h = 8
        (99, 33, 22),  # h = 18
    ]
    for idx_h, (a_c, b_c, c_c) in enumerate(de_gua_alts, 1):
        inv_h2 = Fraction(1, a_c * a_c) + Fraction(1, b_c * b_c) + Fraction(1, c_c * c_c)
        h2_f = Fraction(1, inv_h2)
        assert h2_f.denominator == 1
        ans = math.isqrt(int(h2_f))
        assert ans * ans == int(h2_f)
        # Cross-check with de Gua area: (1/3)*[ABC]*h == a*b*c / 6
        area2 = Fraction(a_c * b_c, 2) ** 2 + Fraction(b_c * c_c, 2) ** 2 + Fraction(c_c * a_c, 2) ** 2
        assert area2 * ans * ans == Fraction(a_c * b_c * c_c, 2) ** 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo 3D corner-tetrahedron card (#{idx_h}), points {m('A, B, C')} lie on three mutually perpendicular edges meeting at corner {m('O')} with {m(f'OA = {a_c}')}, {m(f'OB = {b_c}')}, and {m(f'OC = {c_c}')}. What is the perpendicular distance {m('h')} from corner {m('O')} to the plane {m('ABC')}?",
            q_ar=f"في مسألة رباعي الوجوه القائم من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، تقع النقاط {m('A, B, C')} على ثلاثة أحرف متعامدة مثنى مثنى تلتقي عند الرأس {m('O')} بحيث {m(f'OA = {a_c}')} و{m(f'OB = {b_c}')} و{m(f'OC = {c_c}')}. ما طول العمود النازل {m('h')} من الرأس {m('O')} على المستوى {m('ABC')}؟",
            correct_val=ans,
            distractors=[ans + 2, max(1, ans - 1), min(a_c, b_c, c_c), ans + 3],
            hint_en=f"Use the 3D reciprocal-square altitude theorem {m('\\frac{1}{h^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}')} (derived from {m('\\frac{1}{3}[ABC]h = \\frac{1}{6}abc')}).",
            hint_ar=f"استخدم علاقة مقلوب المربعات الثلاثية الأبعاد {m('\\frac{1}{h^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} + \\frac{1}{OC^2}')}.",
            idea_en=f"Plane {m('\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1')} sits at distance {m('h')} from {m('(0,0,0)')} where {m('\\frac{1}{h^2} = \\frac{1}{a^2} + \\frac{1}{b^2} + \\frac{1}{c^2}')}.",
            steps_en=[
                f"Compute {m(f'\\frac{{1}}{{h^2}} = \\frac{{1}}{{{a_c}^2}} + \\frac{{1}}{{{b_c}^2}} + \\frac{{1}}{{{c_c}^2}} = {inv_h2}')}.",
                f"Invert and take the positive square root: {m(f'h^2 = {int(h2_f)} \\implies h = {ans}')}.",
            ],
            check_en=f"Notice {m(f'h = {ans} < \\min({a_c}, {b_c}, {c_c}) = {min(a_c, b_c, c_c)}')}, and {m('\\frac{1}{3}[ABC]h = \\frac{1}{6}abc')} holds identically.",
            idea_ar=f"معادلة المستوى {m('x/a + y/b + z/c = 1')} تعطي {m('\\frac{1}{h^2} = \\frac{1}{a^2} + \\frac{1}{b^2} + \\frac{1}{c^2}')}.",
            steps_ar=[
                f"نحسب {m(f'\\frac{{1}}{{h^2}} = \\frac{{1}}{{{a_c}^2}} + \\frac{{1}}{{{b_c}^2}} + \\frac{{1}}{{{c_c}^2}} = {inv_h2}')}.",
                f"ومنه {m(f'h^2 = {int(h2_f)}')} أي {m(f'h = {ans}')}.",
            ],
            check_ar=f"التحقق بمساواة الحجم {m('\\frac{1}{3}[ABC]h = \\frac{1}{6}abc')} يؤكد أن {m(f'h = {ans}')}.",
            diagram_en=svg_stu_cube_corner_cut(str(a_c), str(b_c), str(c_c)),
        ))

    # Hard 15.5: de Gua's Theorem [ABC] for (12, 6, 6) -> 54
    a_g, b_g, c_g = 12, 6, 6
    f1, f2, f3 = (a_g * b_g) // 2, (b_g * c_g) // 2, (c_g * a_g) // 2
    ans_degua = math.isqrt(f1 * f1 + f2 * f2 + f3 * f3)
    assert ans_degua * ans_degua == f1 * f1 + f2 * f2 + f3 * f3 == 2916
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
        q_en=f"In a 5-point Student Kangaroo de Gua problem (#5), segments {m('OA = 12')}, {m('OB = 6')}, and {m('OC = 6')} are mutually perpendicular at corner {m('O')}. What is the **area** of the slanted triangle {m('\\triangle ABC')}?",
        q_ar=f"في مسألة مبرهنة دي غوا من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم (٥)، القطع {m('OA = 12')} و{m('OB = 6')} و{m('OC = 6')} متعامدة مثنى مثنى عند الرأس {m('O')}. ما **مساحة** المثلث المائل {m('\\triangle ABC')}؟",
        correct_val=ans_degua,
        distractors=[f1 + f2 + f3, 36, 48, 72],
        hint_en=f"By de Gua's Theorem (3D Pythagorean theorem for areas), {m('[ABC]^2 = [OAB]^2 + [OBC]^2 + [OCA]^2')}!",
        hint_ar=f"بحسب مبرهنة دي غوا (فيثاغورس للمساحات في الفضاء)، {m('[ABC]^2 = [OAB]^2 + [OBC]^2 + [OCA]^2')}!",
        idea_en=f"Square the areas of the three right-triangle faces {m(f'{f1}, {f2}, {f3}')} and sum them.",
        steps_en=[
            f"Right-face areas: {m(f'[OAB] = 36')}, {m(f'[OBC] = 18')}, and {m(f'[OCA] = 36')}.",
            f"By de Gua's Theorem, {m('[ABC]^2 = 36^2 + 18^2 + 36^2 = 1296 + 324 + 1296 = 2916')}.",
            f"Take the square root: {m('[ABC] = 54')}.",
        ],
        check_en=f"Isosceles check: {m('BC = 6\\sqrt{2}')}, {m('AB = AC = 6\\sqrt{5}')}, altitude to {m('BC')} is {m('\\sqrt{180 - 18} = 9\\sqrt{2}')}, area {m('\\frac{1}{2}(6\\sqrt{2})(9\\sqrt{2}) = 54')}.",
        idea_ar=f"من مبرهنة دي غوا نجمع مربعات مساحات الأوجه القائمة الثلاثة ثم نأخذ الجذر التربيعي.",
        steps_ar=[
            f"مساحات الأوجه القائمة هي {m('36')} و{m('18')} و{m('36')}.",
            f"إذن {m('[ABC]^2 = 36^2 + 18^2 + 36^2 = 2916')}، ومنه {m('[ABC] = 54')}.",
        ],
        check_ar=f"التحقق بأطوال أضلاع المثلث المتساوي الساقين {m('ABC')} يعطي المساحة {m('54')} تماماً.",
        diagram_en=svg_stu_cube_corner_cut("12", "6", "6"),
    ))

    # ------------------------------------------------------------------
    # 16. kang_stu_mirror_bounce_lattice_pick (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_mirror_bounce_lattice_pick"
    easy_mir = [
        (10, 6, 1, 2, 9, 4),    # dx=8, y1+y2=6 -> 10
        (14, 6, 1, 2, 13, 3),   # dx=12, y1+y2=5 -> 13
        (18, 8, 2, 3, 17, 5),   # dx=15, y1+y2=8 -> 17
        (26, 8, 1, 3, 25, 4),   # dx=24, y1+y2=7 -> 25
        (24, 15, 2, 9, 22, 12), # dx=20, y1+y2=21 -> 29
    ]
    for idx_e, (L_r, W_r, x1, y1, x2, y2) in enumerate(easy_mir, 1):
        dx = x2 - x1
        dy_sum = y1 + y2
        ans = math.isqrt(dx * dx + dy_sum * dy_sum)
        assert ans * ans == dx * dx + dy_sum * dy_sum
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo reflection card #{idx_e}, inside an {m(f'{L_r} \\times {W_r}')} rectangular room ({m(f'0 \\le x \\le {L_r}')}, {m(f'0 \\le y \\le {W_r}')}), a laser beam travels from {m(f'A({x1}, {y1})')} to a point {m('P')} on the mirror wall {m('y = 0')} and reflects to {m(f'B({x2}, {y2})')}. What is the minimum possible length {m('AP + PB')}?",
            q_ar=f"في بطاقة الانعكاس بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، داخل غرفة مستطيلة أبعادها {m(f'{L_r} \\times {W_r}')}، ينطلق شعاع من النقطة {m(f'A({x1}, {y1})')} لينعكس عن الجدار المرآوي {m('y = 0')} عند {m('P')} ويصل إلى {m(f'B({x2}, {y2})')}. ما أقصر طول ممكن للمسار {m('AP + PB')}؟",
            correct_val=ans,
            distractors=[dx + dy_sum, math.isqrt(dx * dx + (y2 - y1) ** 2) if math.isqrt(dx * dx + (y2 - y1) ** 2) ** 2 == dx * dx + (y2 - y1) ** 2 else ans - 2, ans + 2, ans + 4],
            hint_en=f"Reflect {m(f'A({x1}, {y1})')} across the mirror {m('y = 0')} to {m(f'A\'({x1}, -{y1})')} and compute the straight-line distance {m('A\'B')}.",
            hint_ar=f"اعكس النقطة {m(f'A({x1}, {y1})')} حول المرآة {m('y = 0')} إلى {m(f'A\'({x1}, -{y1})')} واحسب المسافة المستقيمة {m('A\'B')}.",
            idea_en=f"Since {m('AP = A\'P')}, {m('AP + PB = A\'P + PB \\ge A\'B = \\sqrt{(x_2 - x_1)^2 + (y_1 + y_2)^2}')}.",
            steps_en=[
                f"Reflect {m('A')} across {m('y = 0')} to {m(f'A\'({x1}, -{y1})')}.",
                f"Compute {m(f'A\'B = \\sqrt{{({x2} - {x1})^2 + ({y2} - (-{y1}))^2}} = \\sqrt{{{dx}^2 + {dy_sum}^2}} = {ans}')}.",
            ],
            check_en=f"Bounce point {m(f'P({Fraction(x1*y2 + x2*y1, y1+y2)}, 0)')} lies strictly inside {m(f'[0, {L_r}]')}.",
            idea_ar=f"انعكاس {m('A')} يحوّل المسار المنكسر إلى قطعة مستقيمة واحدة {m('A\'B')}.",
            steps_ar=[
                f"صورة {m('A')} بالانعكاس حول {m('y = 0')} هي {m(f'A\'({x1}, -{y1})')}.",
                f"المسافة الدنيا {m(f'A\'B = \\sqrt{{{dx}^2 + {dy_sum}^2}} = {ans}')}.",
            ],
            check_ar=f"نقطة الانعكاس على المحور {m('y = 0')} تقع فعلاً داخل عرض الغرفة.",
            diagram_en=svg_stu_mirror_bounce(str(L_r), str(W_r), "AP+PB=?"),
        ))

    # Medium 16.1..16.3: Pick's theorem polygon area; 16.4..16.5: Interior lattice points I
    pick_area_specs = [
        (6, 5, [(0, 1), (4, 0), (6, 3), (2, 5)], ["A", "B", "C", "D"]),
        (6, 6, [(0, 0), (5, 1), (6, 5), (1, 6)], ["A", "B", "C", "D"]),
        (7, 5, [(1, 0), (6, 1), (7, 4), (3, 5), (0, 3)], ["A", "B", "C", "D", "E"]),
    ]
    for idx_m, (cols, rows, verts, lbls) in enumerate(pick_area_specs, 1):
        A_exact = Fraction(_poly_twice_area_rect(verts), 2)
        B_cnt = _poly_boundary_lattice(verts)
        I_cnt = sum(1 for x in range(cols + 1) for y in range(rows + 1) if _point_strictly_in_poly(x, y, verts))
        assert A_exact == I_cnt + Fraction(B_cnt, 2) - 1
        v_txt = ", ".join(m(f"{nm}({vx},{vy})") for nm, (vx, vy) in zip(lbls, verts))
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo lattice problem #{idx_m}, a convex lattice polygon has vertices {v_txt} in order on the unit grid. Using Pick's Theorem (or bounding-box subtraction), what is its exact **area**?",
            q_ar=f"في مسألة الشبكة التربيعية بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، رؤوس مضلع شبكي محدب بالترتيب هي {v_txt}. باستخدام مبرهنة بيك (أو طرح المثلثات المحيطة)، ما **مساحته** الدقيقة؟",
            correct_val=A_exact,
            distractors=[A_exact + 1, A_exact - 1, I_cnt + Fraction(B_cnt, 2), A_exact + 2],
            hint_en=f"By Pick's Theorem, {m('\\text{Area} = I + \\frac{B}{2} - 1')}, or subtract the outer right triangles from the {m(f'{cols} \\times {rows}')} bounding rectangle.",
            hint_ar=f"بمبرهنة بيك {m('\\text{Area} = I + \\frac{B}{2} - 1')}، أو اطرح مساحات المثلثات القائمة الخارجية من المستطيل المحيط {m(f'{cols} \\times {rows}')}.",
            idea_en=f"Pick's Theorem with {m(f'I = {I_cnt}')} interior lattice points and {m(f'B = {B_cnt}')} boundary lattice points gives {m(f'I + B/2 - 1 = {A_exact}')}.",
            steps_en=[
                f"Boundary lattice points: {m(f'B = {B_cnt}')} (summing {m('\\gcd(|\\Delta x|, |\\Delta y|)')} along edges), and interior points: {m(f'I = {I_cnt}')}.",
                f"By Pick's Theorem, {m(f'\\text{{Area}} = {I_cnt} + \\frac{{{B_cnt}}}{{2}} - 1 = {A_exact}')}.",
            ],
            check_en=f"Bounding-box subtraction from {m(f'{cols} \\times {rows} = {cols*rows}')} independently yields {m(str(A_exact))}.",
            idea_ar=f"نطبق مبرهنة بيك {m('I + B/2 - 1')} أو نطرح المثلثات الركنية من المستطيل المحيط.",
            steps_ar=[
                f"عدد النقاط الشبكية الحدودية {m(f'B = {B_cnt}')} والداخلية {m(f'I = {I_cnt}')}.",
                f"المساحة {m(f'= {I_cnt} + \\frac{{{B_cnt}}}{{2}} - 1 = {A_exact}')}.",
            ],
            check_ar=f"حساب المساحة بطرح المثلثات من المستطيل المحيط يعطي {m(str(A_exact))} أيضاً.",
            diagram_en=svg_grid_polygon(cols, rows, verts, lbls),
        ))

    pick_int_specs = [
        (8, 2, 3, 6),   # O(0,0), A(8,2), B(3,6) -> Area=21, B=2+6+... wait check B and I!
        (9, 3, 3, 7),   # O(0,0), A(9,3), B(3,7) -> Area=27, B=6, I=25
    ]
    for idx_m2, (ax_p, ay_p, bx_p, by_p) in enumerate(pick_int_specs, 4):
        verts_t = [(0, 0), (ax_p, ay_p), (bx_p, by_p)]
        A_t = Fraction(_poly_twice_area_rect(verts_t), 2)
        B_t = _poly_boundary_lattice(verts_t)
        I_t = sum(1 for x in range(max(ax_p, bx_p) + 1) for y in range(max(ay_p, by_p) + 1) if _point_strictly_in_poly(x, y, verts_t))
        assert A_t == I_t + Fraction(B_t, 2) - 1
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo Pick's Theorem problem #{idx_m2}, how many integer lattice points {m('(x, y) \\in \\mathbb{Z}^2')} lie **strictly inside** {m('\\triangle OAB')} with vertices {m('O(0, 0)')}, {m(f'A({ax_p}, {ay_p})')}, and {m(f'B({bx_p}, {by_p})')}?",
            q_ar=f"في مسألة مبرهنة بيك بمسابقة الكانجارو للمستوى المتقدم ({idx_m2})، كم نقطة شبكية ذات إحداثيات صحيحة {m('(x, y) \\in \\mathbb{Z}^2')} تقع **تماماً داخل** المثلث {m('\\triangle OAB')} الذي رؤوسه {m('O(0, 0)')} و{m(f'A({ax_p}, {ay_p})')} و{m(f'B({bx_p}, {by_p})')}؟",
            correct_val=I_t,
            distractors=[int(A_t), I_t + B_t, I_t - 2, I_t + 2],
            hint_en=f"Rearrange Pick's Theorem to {m('I = \\text{Area} - \\frac{B}{2} + 1')}, using {m('\\gcd(|\\Delta x|, |\\Delta y|)')} on each of the three sides to count {m('B')}.",
            hint_ar=f"أعد ترتيب مبرهنة بيك إلى {m('I = \\text{Area} - \\frac{B}{2} + 1')}، واحسب {m('B')} بجمع {m('\\gcd(|\\Delta x|, |\\Delta y|)')} على الأضلاع الثلاثة.",
            idea_en=f"Find {m('[OAB]')} by bounding-box subtraction and {m('B')} via {m('\\gcd')} along each side, then compute {m('I = [OAB] - B/2 + 1')}.",
            steps_en=[
                f"Subtracting three outer right triangles from the {m(f'{ax_p} \\times {by_p}')} box gives {m(f'[OAB] = {A_t}')}.",
                f"Boundary points: {m(f'B = \\gcd({ax_p},{ay_p}) + \\gcd({ax_p - bx_p},{by_p - ay_p}) + \\gcd({bx_p},{by_p}) = {B_t}')}.",
                f"Therefore {m(f'I = {A_t} - \\frac{{{B_t}}}{{2}} + 1 = {I_t}')}.",
            ],
            check_en=f"Exhaustive lattice scan confirms exact {m(str(I_t))} strictly interior integer points.",
            idea_ar=f"نحسب المساحة من المستطيل المحيط وعدد النقاط الحدودية بالقاسم المشترك الأكبر ثم نطبق {m('I = \\text{Area} - B/2 + 1')}.",
            steps_ar=[
                f"مساحة المثلث {m(f'[OAB] = {A_t}')}، والنقاط الحدودية {m(f'B = {B_t}')}.",
                f"عدد النقاط الداخلية {m(f'I = {A_t} - {B_t}//2 + 1 = {I_t}')}.",
            ],
            check_ar=f"فحص جميع النقاط الصحيحة داخل المستطيل المحيط يؤكد وجود {m(str(I_t))} نقطة داخلية بالضبط.",
            diagram_en=svg_coord_diamond("ℤ×ℤ"),
        ))

    # Hard 16.1..16.3: Two-wall mirror unfolding; 16.4..16.5: 45-degree corner laser bounces
    two_wall_specs = [
        (10, 8, 2, 3, 6, 2),    # dx = 20 - 8 = 12, dy = 5 -> 13
        (12, 10, 3, 4, 6, 4),   # dx = 24 - 9 = 15, dy = 8 -> 17
        (15, 12, 2, 3, 4, 4),   # dx = 30 - 6 = 24, dy = 7 -> 25
    ]
    for idx_h, (L_r, W_r, x1, y1, x2, y2) in enumerate(two_wall_specs, 1):
        # Reflect B(x2, y2) across right wall x = L_r -> B1(2L_r - x2, y2), and A(x1, y1) across y = 0 -> A1(x1, -y1)
        dx = 2 * L_r - x2 - x1
        dy = y1 + y2
        ans = math.isqrt(dx * dx + dy * dy)
        assert ans * ans == dx * dx + dy * dy
        # Verify segment from (x1, -y1) to (2L_r - x2, y2) hits y=0 strictly in (0, L_r) and x=L_r strictly in (0, W_r)
        x_hit = Fraction(x1) + Fraction(y1, dy) * dx
        y_hit = Fraction(-y1) + Fraction(L_r - x1, dx) * dy
        assert 0 < x_hit < L_r and 0 < y_hit < W_r
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo double-bounce card (#{idx_h}), in the rectangle {m(f'0 \\le x \\le {L_r}')}, {m(f'0 \\le y \\le {W_r}')}, a billiard ball starts at {m(f'A({x1}, {y1})')}, bounces first off the bottom wall {m('y = 0')} at {m('P')}, then off the right wall {m(f'x = {L_r}')} at {m('Q')}, and reaches {m(f'B({x2}, {y2})')}. What is the shortest possible path length {m('AP + PQ + QB')}?",
            q_ar=f"في مسألة الانعكاس المزدوج من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، داخل المستطيل {m(f'0 \\le x \\le {L_r}')} و{m(f'0 \\le y \\le {W_r}')}، تنطلق كرة من {m(f'A({x1}, {y1})')} فترتد أولاً عن الجدار السفلي {m('y = 0')} عند {m('P')} ثم عن الجدار الأيمن {m(f'x = {L_r}')} عند {m('Q')} لتصل إلى {m(f'B({x2}, {y2})')}. ما أقصر طول ممكن للمسار {m('AP + PQ + QB')}؟",
            correct_val=ans,
            distractors=[ans + 2, ans - 2, dx + dy, ans + 4],
            hint_en=f"Reflect {m('A')} across {m('y = 0')} to {m(f'A\'({x1}, -{y1})')} and reflect {m('B')} across {m(f'x = {L_r}')} to {m(f'B\'({2*L_r - x2}, {y2})')}!",
            hint_ar=f"اعكس {m('A')} حول {m('y = 0')} إلى {m(f'A\'({x1}, -{y1})')} واعكس {m('B')} حول {m(f'x = {L_r}')} إلى {m(f'B\'({2*L_r - x2}, {y2})')}!",
            idea_en=f"Unfolding across both mirrors turns {m('AP + PQ + QB')} into the straight segment {m('A\'B\'')}.",
            steps_en=[
                f"Reflected endpoints are {m(f'A\'({x1}, -{y1})')} and {m(f'B\'(2\\cdot {L_r} - {x2}, {y2}) = ({2*L_r - x2}, {y2})')}.",
                f"Horizontal span {m(f'\\Delta x = {2*L_r - x2} - {x1} = {dx}')} and vertical span {m(f'\\Delta y = {y2} - (-{y1}) = {dy}')}.",
                f"Shortest path {m(f'= \\sqrt{{{dx}^2 + {dy}^2}} = {ans}')}.",
            ],
            check_en=f"The line {m('A\'B\'')} crosses {m('y = 0')} at {m(f'x = {x_hit} \\in (0, {L_r})')} and {m(f'x = {L_r}')} at {m(f'y = {y_hit} \\in (0, {W_r})')}, so both bounces occur in order!",
            idea_ar=f"نفرد الانعكاسين معاً فتتحول القطع الثلاث إلى خط مستقيم واحد يصل {m('A\'')} بـ {m('B\'')}.",
            steps_ar=[
                f"إحداثيات الصورتين هما {m(f'A\'({x1}, -{y1})')} و{m(f'B\'({2*L_r - x2}, {y2})')}.",
                f"الطول الأدنى {m(f'= \\sqrt{{{dx}^2 + {dy}^2}} = {ans}')}.",
            ],
            check_ar=f"نقطتا التقاطع مع الجدارين تقعان فعلاً داخل الضلعين بالترتيب المطلوب.",
            diagram_en=svg_stu_mirror_bounce(str(L_r), str(W_r), "Path=?"),
        ))

    for idx_h2, (L_b, W_b) in enumerate([(15, 9), (28, 20)], 4):
        L_lcm = math.lcm(L_b, W_b)
        p_cnt = L_lcm // L_b
        q_cnt = L_lcm // W_b
        ans = (p_cnt - 1) + (q_cnt - 1)
        # Simulate step-by-step unit diagonal ray to verify bounce count
        bounces_sim = 0
        for step_t in range(1, L_lcm):
            hit_v = (step_t % L_b == 0)
            hit_h = (step_t % W_b == 0)
            assert not (hit_v and hit_h)
            if hit_v or hit_h:
                bounces_sim += 1
        assert bounces_sim == ans
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo laser-billiard problem (#{idx_h2}), a laser is fired from corner {m('(0, 0)')} of an {m(f'{L_b} \\times {W_b}')} mirrored rectangle at a {m('45^\\circ')} angle to both walls. How many times does the beam **bounce off the walls** before it first enters a corner pocket?",
            q_ar=f"في مسألة بلياردو الليزر من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h2})، أُطلق شعاع ليزر من الزاوية {m('(0, 0)')} لمستطيل عاكس أبعاده {m(f'{L_b} \\times {W_b}')} بزاوية {m('45^\\circ')} مع الضلعين. كم مرة **يرتد الشعاع عن الجدران** قبل أن يدخل إحدى الزوايا لأول مرة؟",
            correct_val=ans,
            distractors=[p_cnt + q_cnt, p_cnt * q_cnt - 1, ans + 1, ans - 1],
            hint_en=f"Unfold the rectangle into a grid of {m(f'{L_b} \\times {W_b}')} copies: the {m('45^\\circ')} line {m('y = x')} first hits a grid corner at {m(f'x = y = \\operatorname{{lcm}}({L_b}, {W_b})')}!",
            hint_ar=f"افرد المستطيل إلى شبكة نسخ {m(f'{L_b} \\times {W_b}')}: المستقيم {m('y = x')} يصيب زاوية شبكية لأول مرة عند {m(f'\\operatorname{{lcm}}({L_b}, {W_b})')}!",
            idea_en=f"Until {m(f't = \\operatorname{{lcm}}({L_b}, {W_b}) = {L_lcm}')}, the unfolded ray crosses {m(f'{p_cnt} - 1')} vertical mirror lines and {m(f'{q_cnt} - 1')} horizontal mirror lines.",
            steps_en=[
                f"Compute {m(f'\\operatorname{{lcm}}({L_b}, {W_b}) = {L_lcm}')}, which spans {m(f'p = {L_lcm}/{L_b} = {p_cnt}')} widths and {m(f'q = {L_lcm}/{W_b} = {q_cnt}')} heights.",
                f"Since {m(f'\\gcd({p_cnt}, {q_cnt}) = 1')}, no interior crossing hits two walls simultaneously.",
                f"Total wall bounces {m(f'= ({p_cnt} - 1) + ({q_cnt} - 1) = {ans}')}.",
            ],
            check_en=f"Unit-step simulation along {m(f't = 1 \\dots {L_lcm - 1}')} counts exact {m(str(ans))} wall hits.",
            idea_ar=f"عدد الارتدادات قبل أول زاوية يساوي مجموع خطوط الشبكة الرأسية والأفقية التي يعبرها الشعاع المفرد.",
            steps_ar=[
                f"المضاعف المشترك الأصغر {m(f'\\operatorname{{lcm}}({L_b}, {W_b}) = {L_lcm}')}، أي {m(f'{p_cnt}')} عروض و{m(f'{q_cnt}')} ارتفاعات.",
                f"عدد الارتدادات {m(f'= ({p_cnt} - 1) + ({q_cnt} - 1) = {ans}')}.",
            ],
            check_ar=f"المحاكاة الخطوية للشعاع تؤكد حدوث {m(str(ans))} ارتدادات جدارية بالضبط.",
            diagram_en=svg_stu_mirror_bounce(str(L_b), str(W_b), "45° #=?"),
        ))

    return items



def _dyck_dp(a: int, b: int, blocked: set[tuple[int, int]] = frozenset(), strict_after_origin: bool = False) -> int:
    """Count monotone lattice paths from (0,0) to (a,b) staying in y <= x (or y < x for intermediate steps)."""
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[0][0] = 1
    for x in range(a + 1):
        for y in range(b + 1):
            if (x, y) == (0, 0) or (x, y) in blocked:
                continue
            if strict_after_origin and (x, y) != (a, b):
                if y >= x:
                    continue
            else:
                if y > x:
                    continue
            v = 0
            if x > 0:
                v += dp[x - 1][y]
            if y > 0:
                v += dp[x][y - 1]
            dp[x][y] = v
    return dp[a][b]


# ==============================================================================
# UNIT 5.5 — COMBINATORICS & LOGIC (60 Questions: KANG-STU-241 .. KANG-STU-300)
# ==============================================================================
def _unit_5_5_combinatorics(offset: int = 240) -> list[dict]:
    items: list[dict] = []
    topic = "Combinatorics & Logic"

    # ------------------------------------------------------------------
    # 17. kang_stu_catalan_ballot_dyck_paths (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_catalan_ballot_dyck_paths"
    for idx_e, n_cat in enumerate([3, 4, 5, 6], 1):
        ans = math.comb(2 * n_cat, n_cat) // (n_cat + 1)
        assert ans == _dyck_dp(n_cat, n_cat)
        sample_p = "R" * min(3, n_cat) + "U" * min(2, n_cat) + "RU"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo lattice card #{idx_e}, how many shortest grid paths from {m('(0, 0)')} to {m(f'({n_cat}, {n_cat})')} using unit steps Right {m('(1, 0)')} and Up {m('(0, 1)')} **never rise above** the diagonal {m('y = x')}?",
            q_ar=f"في بطاقة الشبكات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، كم مساراً شبكياً أقصر من {m('(0, 0)')} إلى {m(f'({n_cat}, {n_cat})')} بخطوات يميناً {m('(1, 0)')} وأعلى {m('(0, 1)')} **لا يرتفع أبداً فوق** القطر {m('y = x')}؟",
            correct_val=ans,
            distractors=[math.comb(2 * n_cat, n_cat), ans * 2, ans + n_cat, max(2, ans - n_cat)],
            hint_en=f"Use the {m(str(n_cat))}th Catalan number {m(f'C_{{{n_cat}}} = \\frac{{1}}{{{n_cat} + 1}}\\binom{{{2*n_cat}}}{{{n_cat}}}')}.",
            hint_ar=f"استخدم عدد كاتالان رقم {m(str(n_cat))}: {m(f'C_{{{n_cat}}} = \\frac{{1}}{{{n_cat} + 1}}\\binom{{{2*n_cat}}}{{{n_cat}}}')}.",
            idea_en=f"Dyck lattice paths from {m('(0, 0)')} to {m(f'({n_cat}, {n_cat})')} staying in {m('y \\le x')} are counted by {m(f'C_{{{n_cat}}}')}.",
            steps_en=[
                f"Total unconstrained paths equal {m(f'\\binom{{{2*n_cat}}}{{{n_cat}}} = {math.comb(2*n_cat, n_cat)}')}.",
                f"Divide by {m(f'{n_cat} + 1 = {n_cat + 1}')} (reflection principle): {m(f'C_{{{n_cat}}} = \\frac{{{math.comb(2*n_cat, n_cat)}}}{{{n_cat + 1}}} = {ans}')}.",
            ],
            check_en=f"Subtracting bad paths {m(f'\\binom{{{2*n_cat}}}{{{n_cat}}} - \\binom{{{2*n_cat}}}{{{n_cat - 1}}} = {ans}')} matches.",
            idea_ar=f"عدد مسارات ديك التي تبقى على القطر أو تحته يُعطى بعدد كاتالان {m(f'C_{{{n_cat}}}')}.",
            steps_ar=[
                f"إجمالي المسارات غير المقيدة هو {m(f'\\binom{{{2*n_cat}}}{{{n_cat}}} = {math.comb(2*n_cat, n_cat)}')}.",
                f"بقسمته على {m(str(n_cat + 1))} نحصل على {m(f'C_{{{n_cat}}} = {ans}')}.",
            ],
            check_ar=f"مبدأ الانعكاس {m(f'\\binom{{{2*n_cat}}}{{{n_cat}}} - \\binom{{{2*n_cat}}}{{{n_cat - 1}}}')} يعطي {m(str(ans))} أيضاً.",
            diagram_en=svg_stu_dyck_grid(n_cat, sample_p),
        ))

    # Easy 17.5: Convex nonagon (9 sides) triangulations -> C_7 = 429
    ans_c7 = math.comb(14, 7) // 8
    assert ans_c7 == _dyck_dp(7, 7) == 429
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
        q_en=f"On Student Kangaroo Catalan card #5, in how many ways can a convex **nonagon** ({m('9')}-sided polygon) be partitioned into {m('7')} triangles by {m('6')} non-crossing diagonals?",
        q_ar=f"في بطاقة أعداد كاتالان بمسابقة الكانجارو للمستوى المتقدم (٥)، بكم طريقة يمكن تقسيم **تساعي محدب** ({m('9')} أضلاع) إلى {m('7')} مثلثات بواسطة {m('6')} أقطار غير متقاطعة داخلياً؟",
        correct_val=ans_c7,
        distractors=[132, 286, 480, 330],
        hint_en=f"Triangulations of a convex {m('(n + 2)')}-gon are counted by the Catalan number {m('C_n')}; for {m('9')} sides, {m('n = 7')}.",
        hint_ar=f"عدد تثليثات مضلع محدب ذي {m('n + 2')} ضلعاً يساوي عدد كاتالان {m('C_n')}؛ وهنا {m('n = 7')}.",
        idea_en=f"A convex {m('9')}-gon has {m('C_{9-2} = C_7 = \\frac{1}{8}\\binom{14}{7}')} triangulations.",
        steps_en=[
            f"Set {m('n = 9 - 2 = 7')}.",
            f"Compute {m('C_7 = \\frac{1}{8}\\binom{14}{7} = \\frac{3432}{8} = 429')}.",
        ],
        check_en=f"Catalan recurrence {m('C_7 = 2C_6 + \\dots = 429')} confirms {m('429')}.",
        idea_ar=f"تثليثات المضلع المحدب ذي {m('9')} أضلاع تقابل {m('C_7')}.",
        steps_ar=[
            f"نضع {m('n = 9 - 2 = 7')}.",
            f"نحسب {m('C_7 = \\frac{1}{8}\\binom{14}{7} = 429')}.",
        ],
        check_ar=f"علاقة كاتالان التراجعية تؤكد أن {m('C_7 = 429')}.",
        diagram_en=svg_regular_polygon(7, [(0, 2), (0, 4), (2, 4), (4, 6)]),
    ))

    med_ballot = [
        (5, 3),  # 28
        (6, 3),  # 48
        (6, 4),  # 90
        (7, 3),  # 75
        (7, 4),  # 165
    ]
    for idx_m, (a_r, b_u) in enumerate(med_ballot, 1):
        ans = math.comb(a_r + b_u, b_u) - math.comb(a_r + b_u, b_u - 1)
        assert ans == _dyck_dp(a_r, b_u)
        assert ans == (a_r - b_u + 1) * math.comb(a_r + b_u, b_u) // (a_r + 1)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo ballot problem #{idx_m}, how many shortest grid paths from {m('(0, 0)')} to {m(f'({a_r}, {b_u})')} (using Right and Up unit steps) **never rise above** the line {m('y = x')} (so {m('y \\le x')} at every point)?",
            q_ar=f"في مسألة الاقتراع الشبكية بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، كم مساراً شبكياً أقصر من {m('(0, 0)')} إلى {m(f'({a_r}, {b_u})')} **لا يرتفع أبداً فوق** المستقيم {m('y = x')} (أي يحقق {m('y \\le x')} عند كل خطوة)؟",
            correct_val=ans,
            distractors=[math.comb(a_r + b_u, b_u), ans + 10, max(5, ans - 10), (a_r - b_u) * math.comb(a_r + b_u, b_u) // (a_r + b_u)],
            hint_en=f"Reflect bad paths across {m('y = x + 1')} (starting from {m('(-1, 1)')}): valid paths equal {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} - \\binom{{{a_r + b_u}}}{{{b_u - 1}}}')}.",
            hint_ar=f"اعكس المسارات المخالفة حول المستقيم {m('y = x + 1')}: عدد المسارات الصالحة هو {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} - \\binom{{{a_r + b_u}}}{{{b_u - 1}}}')}.",
            idea_en=f"By André's reflection principle, paths staying in {m('y \\le x')} to {m(f'({a_r}, {b_u})')} equal {m(f'\\binom{{{a_r+b_u}}}{{{b_u}}} - \\binom{{{a_r+b_u}}}{{{b_u-1}}}')}.",
            steps_en=[
                f"All paths to {m(f'({a_r}, {b_u})')}: {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} = {math.comb(a_r + b_u, b_u)}')}.",
                f"Paths touching {m('y = x + 1')} biject with paths from {m('(-1, 1)')} to {m(f'({a_r}, {b_u})')}: {m(f'\\binom{{{a_r + b_u}}}{{{b_u - 1}}} = {math.comb(a_r + b_u, b_u - 1)}')}.",
                f"Subtract: {m(f'{math.comb(a_r + b_u, b_u)} - {math.comb(a_r + b_u, b_u - 1)} = {ans}')}.",
            ],
            check_en=f"Equivalent factor {m(f'\\frac{{{a_r - b_u + 1}}}{{{a_r + 1}}}\\binom{{{a_r + b_u}}}{{{b_u}}} = {ans}')} matches lattice DP.",
            idea_ar=f"نطرح المسارات التي تلمس المستقيم المحظور {m('y = x + 1')} باستخدام مبدأ الانعكاس لأندريه.",
            steps_ar=[
                f"جميع المسارات عددها {m(str(math.comb(a_r + b_u, b_u)))} والمسارات المخالفة عددها {m(str(math.comb(a_r + b_u, b_u - 1)))}.",
                f"الفرق يساوي {m(str(ans))} مساراً.",
            ],
            check_ar=f"البرمجة الديناميكية على نقاط الشبكة تعطي {m(str(ans))} مساراً بالضبط.",
            diagram_en=svg_stu_dyck_grid(min(6, a_r), "RRURURU"),
        ))

    # Hard 17.1..17.3: Blocked-node Dyck DP; 17.4..17.5: Strict-lead Bertrand ballot
    blocked_dyck_specs = [
        (4, 2, 1),
        (5, 3, 2),
        (5, 3, 1),
    ]
    for idx_h, (n_g, bx, by) in enumerate(blocked_dyck_specs, 1):
        ans = _dyck_dp(n_g, n_g, blocked={(bx, by)})
        tot_cat = _dyck_dp(n_g, n_g)
        to_b = _dyck_dp(bx, by)
        assert 0 < ans < tot_cat
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo restricted-Dyck card (#{idx_h}), how many shortest grid paths from {m('(0, 0)')} to {m(f'({n_g}, {n_g})')} stay on or below {m('y = x')} **and never pass through** the blocked intersection {m(f'({bx}, {by})')}?",
            q_ar=f"في مسألة مسارات مقيدة من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، كم مساراً شبكياً أقصر من {m('(0, 0)')} إلى {m(f'({n_g}, {n_g})')} يبقى على المستقيم {m('y = x')} أو تحته **ولا يمر أبداً** بالتقاطع المغلق {m(f'({bx}, {by})')}؟",
            correct_val=ans,
            distractors=[tot_cat, tot_cat - to_b, ans + 4, max(2, ans - 3)],
            hint_en=f"Subtract from {m(f'C_{{{n_g}}} = {tot_cat}')} the Dyck paths that pass through {m(f'({bx}, {by})')} (or fill node-by-node sums on the {m('y \\le x')} triangle with {m('0')} at {m(f'({bx}, {by})')}).",
            hint_ar=f"اطرح من {m(f'C_{{{n_g}}} = {tot_cat}')} عدد مسارات ديك المارة بالنقطة {m(f'({bx}, {by})')} (أو اجمع قيم الرؤوس تدريجياً مع وضع صفر عند التقاطع المغلق).",
            idea_en=f"Count valid paths to {m(f'({bx}, {by})')} ({m(str(to_b))}) times valid continuations from {m(f'({bx}, {by})')} to {m(f'({n_g}, {n_g})')} ({m(str((tot_cat - ans) // to_b))}), and subtract from {m(str(tot_cat))}.",
            steps_en=[
                f"Unblocked Catalan paths equal {m(f'C_{{{n_g}}} = {tot_cat}')}.",
                f"Valid paths from {m('(0, 0)')} to {m(f'({bx}, {by})')} equal {m(str(to_b))}, and valid continuations to {m(f'({n_g}, {n_g})')} equal {m(str((tot_cat - ans) // to_b))}.",
                f"Subtracting {m(f'{to_b} \\times {(tot_cat - ans)//to_b} = {tot_cat - ans}')} leaves {m(f'{tot_cat} - {tot_cat - ans} = {ans}')}.",
            ],
            check_en=f"Direct triangular grid recurrence with {m(f'dp[{bx}][{by}] = 0')} yields {m(str(ans))}.",
            idea_ar=f"نطرح جداء عدد المسارات الصالحة حتى النقطة المغلقة وعدد تكملاتها الصالحة من {m(f'C_{{{n_g}}}')}.",
            steps_ar=[
                f"إجمالي مسارات كاتالان بدون إغلاق هو {m(str(tot_cat))}.",
                f"عدد مسارات ديك المارة بـ {m(f'({bx}, {by})')} هو {m(f'{to_b} \\times {(tot_cat - ans)//to_b} = {tot_cat - ans}')}.",
                f"العدد المتبقي {m(f'= {tot_cat} - {tot_cat - ans} = {ans}')}.",
            ],
            check_ar=f"حساب جدول الشبكة مع تصفير الخانة المغلقة يؤكد الناتج {m(str(ans))}.",
            diagram_en=svg_street_grid(n_g, n_g, blocked=(bx, by)),
        ))

    for idx_h2, (a_v, b_v) in enumerate([(6, 3), (7, 3)], 4):
        ans = ((a_v - b_v) * math.comb(a_v + b_v, b_v)) // (a_v + b_v)
        # Strict lead after vote 1 (up to final vote too since a_v > b_v!):
        dp_strict = _dyck_dp(a_v, b_v, strict_after_origin=True)
        assert ans == dp_strict
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo election problem (#{idx_h2}), Candidate A receives {m(str(a_v))} votes and Candidate B receives {m(str(b_v))} votes. As the {m(str(a_v + b_v))} ballots are tallied one by one, in how many distinct tally sequences is Candidate A **strictly ahead** of Candidate B after **every single** ballot?",
            q_ar=f"في مسألة فرز الأصوات من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h2})، حصل المرشح A على {m(str(a_v))} أصوات والمرشح B على {m(str(b_v))} أصوات. عند فرز الأوراق الـ {m(str(a_v + b_v))} ورقةً تلو الأخرى، في كم متتالية فرز مختلفة يظل المرشح A **متقدماً بصرامة** على B بعد **كل ورقة**؟",
            correct_val=ans,
            distractors=[math.comb(a_v + b_v, b_v), _dyck_dp(a_v, b_v), ans + 6, ans - 4],
            hint_en=f"Apply Bertrand's Strict Ballot Theorem: {m('\\frac{a - b}{a + b}\\binom{a + b}{b}')} (equivalently, the first vote must go to A, followed by a weak ballot path from {m('(1, 0)')} to {m(f'({a_v}, {b_v})')}).",
            hint_ar=f"طبّق مبرهنة برتراند للاقتراع الصارم: {m('\\frac{a - b}{a + b}\\binom{a + b}{b}')} (أول ورقة يجب أن تكون لـ A ثم مسار لا يعلو {m('y = x - 1')}).",
            idea_en=f"By Bertrand's Ballot Theorem, fraction {m(f'\\frac{{{a_v} - {b_v}}}{{{a_v} + {b_v}}}')} of all {m(f'\\binom{{{a_v + b_v}}}{{{b_v}}}')} sequences keep A strictly ahead throughout.",
            steps_en=[
                f"Total tally sequences: {m(f'\\binom{{{a_v + b_v}}}{{{b_v}}} = {math.comb(a_v + b_v, b_v)}')}.",
                f"Multiply by {m(f'\\frac{{{a_v} - {b_v}}}{{{a_v} + {b_v}}} = \\frac{{{a_v - b_v}}}{{{a_v + b_v}}}')} to get {m(str(ans))}.",
            ],
            check_en=f"Shifting {m('x\' = x - 1')}: weak ballot paths from {m('(0,0)')} to {m(f'({a_v - 1}, {b_v})')} give {m(f'\\binom{{{a_v + b_v - 1}}}{{{b_v}}} - \\binom{{{a_v + b_v - 1}}}{{{b_v - 1}}} = {ans}')}.",
            idea_ar=f"بمبرهنة برتراند للاقتراع، نسبة المتتاليات التي يتقدم فيها A دائماً هي {m('\\frac{a - b}{a + b}')}.",
            steps_ar=[
                f"عدد جميع متتاليات الفرز {m(f'\\binom{{{a_v + b_v}}}{{{b_v}}} = {math.comb(a_v + b_v, b_v)}')}.",
                f"نضرب في {m(f'\\frac{{{a_v - b_v}}}{{{a_v + b_v}}}')} فنجد {m(str(ans))} متتالية.",
            ],
            check_ar=f"اختبار الشبكة بعد تثبيت الصوت الأول لـ A يعطي {m(str(ans))} متتالية بالضبط.",
            diagram_en=svg_stu_dyck_grid(min(6, a_v), "RRRURURU"),
        ))

    # ------------------------------------------------------------------
    # 18. kang_stu_derangement_inclusion_excl (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_derangement_inclusion_excl"
    der_cache = {
        n_d: sum(1 for p in itertools.permutations(range(n_d)) if all(p[i] != i for i in range(n_d)))
        for n_d in range(1, 7)
    }
    assert der_cache[4] == 9 and der_cache[5] == 44 and der_cache[6] == 265

    for idx_e, (n_d, item_en, item_ar) in enumerate([
        (4, "named badges", "بطاقات أسماء"),
        (5, "graded notebooks", "دفاتر مصححة"),
        (6, "lab keys", "مفاتيح مختبر"),
    ], 1):
        ans = der_cache[n_d]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo derangement card #{idx_e}, {m(str(n_d))} distinct {item_en} are handed back randomly to their {m(str(n_d))} owners (one per person). In how many ways does **nobody** receive their own item?",
            q_ar=f"في بطاقة التبديلات الخالية من النقاط الثابتة بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، وُزِّعت {m(str(n_d))} ({item_ar}) مختلفة على أصحابها الـ {m(str(n_d))}، واحد لكل شخص. بكم طريقة **لا يحصل أي شخص** على غرضه الصحيح؟",
            correct_val=ans,
            distractors=[math.factorial(n_d) - 1, ans + n_d, max(1, ans - 4), math.factorial(n_d - 1)],
            hint_en=f"Use the derangement Inclusion–Exclusion sum {m(f'!{n_d} = {n_d}!\\sum_{{k=0}}^{{{n_d}}} \\frac{{(-1)^k}}{{k!}}')}.",
            hint_ar=f"استخدم صيغة التبديل الكامل بالتضمين والإقصاء {m(f'!{n_d} = {n_d}!\\sum_{{k=0}}^{{{n_d}}} \\frac{{(-1)^k}}{{k!}}')}.",
            idea_en=f"Derangement count {m(f'!{n_d}')} alternates over fixed subsets via Inclusion–Exclusion.",
            steps_en=[
                f"Recall {m('!1 = 0, !2 = 1, !3 = 2')} and recurrence {m('!n = (n - 1)(!(n - 1) + !(n - 2))')}.",
                f"Evaluating up to {m(f'n = {n_d}')} gives {m(f'!{n_d} = {ans}')}.",
            ],
            check_en=f"Inclusion–Exclusion expansion of {m(f'{n_d}!')} confirms exact {m(str(ans))} derangements.",
            idea_ar=f"نطبق علاقة التبديلات الخالية من النقاط الثابتة {m('!n = (n - 1)(!(n - 1) + !(n - 2))')}.",
            steps_ar=[
                f"انطلاقاً من {m('!1 = 0')} و{m('!2 = 1')} و{m('!3 = 2')}.",
                f"نجد عند {m(f'n = {n_d}')} أن {m(f'!{n_d} = {ans}')}.",
            ],
            check_ar=f"فحص جميع التبديلات الـ {m(str(math.factorial(n_d)))} يؤكد وجود {m(str(ans))} تبديلاً خالياً من النقاط الثابتة.",
            diagram_en=svg_digit_slots([f"≠{i}" for i in range(1, min(5, n_d) + 1)], f"!{n_d} = ?"),
        ))

    # Easy 18.4 & 18.5: 3-set Inclusion-Exclusion
    pie3_easy = [
        (42, 38, 35, 16, 14, 12, 6),  # |A u B u C| = 115 - 42 + 6 = 79
        (50, 45, 40, 20, 18, 15, 8),  # |A u B u C| = 135 - 53 + 8 = 90
    ]
    for idx_e2, (sa, sb, sc, sab, sbc, sac, sabc) in enumerate(pie3_easy, 4):
        ans = sa + sb + sc - sab - sbc - sac + sabc
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo Venn card #{idx_e2}, in a Grade 12 camp, {m(str(sa))} students joined Algebra (A), {m(str(sb))} joined Biology (B), and {m(str(sc))} joined Coding (C). Also {m(str(sab))} joined both A and B, {m(str(sbc))} joined B and C, {m(str(sac))} joined A and C, and {m(str(sabc))} joined all three. How many students joined **at least one** of the three clubs?",
            q_ar=f"في بطاقة أشكال فن بمسابقة الكانجارو للمستوى المتقدم ({idx_e2})، انضم {m(str(sa))} طالباً لنادي الجبر (A)، و{m(str(sb))} للأحياء (B)، و{m(str(sc))} للبرمجة (C). وانضم {m(str(sab))} لـ A وB معاً، و{m(str(sbc))} لـ B وC، و{m(str(sac))} لـ A وC، و{m(str(sabc))} للأندية الثلاثة معاً. كم طالباً انضم إلى **نادٍ واحد على الأقل**؟",
            correct_val=ans,
            distractors=[ans - sabc, ans - 2 * sabc, sa + sb + sc - sab - sbc - sac, ans + sabc],
            hint_en=f"Apply 3-set Inclusion–Exclusion: {m('|A \\cup B \\cup C| = |A| + |B| + |C| - |A\\cap B| - |B\\cap C| - |A\\cap C| + |A\\cap B\\cap C|')}.",
            hint_ar=f"طبّق مبدأ التضمين والإقصاء لثلاث مجموعات بإضافة تقاطع الثلاث في النهاية.",
            idea_en=f"Add singletons, subtract pairwise overlaps, and add back the triple intersection.",
            steps_en=[
                f"Singletons sum: {m(f'{sa} + {sb} + {sc} = {sa + sb + sc}')}; pairwise sum: {m(f'{sab} + {sbc} + {sac} = {sab + sbc + sac}')}.",
                f"Union size: {m(f'{sa + sb + sc} - {sab + sbc + sac} + {sabc} = {ans}')}.",
            ],
            check_en=f"Disjoint Venn regions: {m(f'{sa-sab-sac+sabc} + {sb-sab-sbc+sabc} + {sc-sbc-sac+sabc} + {sab-sabc} + {sbc-sabc} + {sac-sabc} + {sabc} = {ans}')}.",
            idea_ar=f"نجمع المجموعات المفردة ونطرح التقاطعات الثنائية ثم نضيف التقاطع الثلاثي.",
            steps_ar=[
                f"نحسب {m(f'({sa} + {sb} + {sc}) - ({sab} + {sbc} + {sac}) + {sabc} = {ans}')}.",
            ],
            check_ar=f"جمع المناطق السبع المنفصلة في مخطط فن يعطي {m(str(ans))} تماماً.",
            diagram_en=svg_venn_3("A", "B", "C", {"a": "?", "b": "?", "c": "?", "ab": "?", "bc": "?", "ac": "?", "abc": str(sabc)}),
        ))

    med_part_der = [
        (5, 2),  # 20
        (5, 1),  # 45
        (6, 3),  # 40
        (6, 2),  # 135
        (6, 1),  # 264
    ]
    for idx_m, (n_p, k_fix) in enumerate(med_part_der, 1):
        ans = math.comb(n_p, k_fix) * der_cache[n_p - k_fix]
        brute = sum(
            1 for perm in itertools.permutations(range(n_p))
            if sum(1 for i in range(n_p) if perm[i] == i) == k_fix
        )
        assert ans == brute
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo permutation problem #{idx_m}, how many permutations {m('(\\pi_1, \\dots, \\pi_' + str(n_p) + ')')} of {m(f'\\{{1, 2, \\dots, {n_p}\\}}')} have **exact {m(str(k_fix))}** fixed point(s) (meaning {m('\\pi_i = i')} for exact {m(str(k_fix))} indices {m('i')})?",
            q_ar=f"في مسألة التبديلات بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، كم تبديلاً للمجموعة {m(f'\\{{1, 2, \\dots, {n_p}\\}}')} يمتلك **بالضبط {m(str(k_fix))}** نقطة ثابتة (أي يتحقق {m('\\pi_i = i')} لعدد {m(str(k_fix))} من المواقع فقط)؟",
            correct_val=ans,
            distractors=[math.comb(n_p, k_fix) * math.factorial(n_p - k_fix - 1), ans + math.comb(n_p, k_fix), max(5, ans - 10), der_cache[n_p]],
            hint_en=f"Choose which {m(str(k_fix))} element(s) stay fixed in {m(f'\\binom{{{n_p}}}{{{k_fix}}}')} ways, and derange the remaining {m(str(n_p - k_fix))} elements in {m(f'!{n_p - k_fix}')} ways!",
            hint_ar=f"اختر مواقع النقاط الثابتة بـ {m(f'\\binom{{{n_p}}}{{{k_fix}}}')} طريقة، وبدّل العناصر الـ {m(str(n_p - k_fix))} المتبقية بلا أي نقطة ثابتة بـ {m(f'!{n_p - k_fix}')} طريقة!",
            idea_en=f"Rencontres number formula: {m(f'D({n_p}, {k_fix}) = \\binom{{{n_p}}}{{{k_fix}}} \\cdot !({n_p - k_fix})')}.",
            steps_en=[
                f"Select the {m(str(k_fix))} fixed positions: {m(f'\\binom{{{n_p}}}{{{k_fix}}} = {math.comb(n_p, k_fix)}')}.",
                f"Derange the other {m(str(n_p - k_fix))} positions: {m(f'!{n_p - k_fix} = {der_cache[n_p - k_fix]}')}.",
                f"Multiply: {m(f'{math.comb(n_p, k_fix)} \\times {der_cache[n_p - k_fix]} = {ans}')}.",
            ],
            check_en=f"Checking all {m(f'{n_p}! = {math.factorial(n_p)}')} permutations confirms exact {m(str(ans))} have {m(str(k_fix))} fixed point(s).",
            idea_ar=f"عدد التبديلات ذات {m(str(k_fix))} نقاط ثابتة يساوي جداء التوافيق في التبديل الكامل للباقي.",
            steps_ar=[
                f"اختيار النقاط الثابتة: {m(f'\\binom{{{n_p}}}{{{k_fix}}} = {math.comb(n_p, k_fix)}')}.",
                f"تبديل الباقي بلا نقاط ثابتة: {m(f'!{n_p - k_fix} = {der_cache[n_p - k_fix]}')}.",
                f"الجداء الكلي {m(f'= {ans}')}.",
            ],
            check_ar=f"العدّ الشامل لجميع تبديلات المجموعة يؤكد أن الناتج هو {m(str(ans))} بالضبط.",
            diagram_en=svg_digit_slots(["Fix"] * min(2, k_fix) + ["≠"] * min(3, n_p - k_fix), f"k={k_fix} fix"),
        ))

    # Hard 18.1..18.3: Divisibility PIE; 18.4..18.5: Constrained permutation PIE
    div_pie_specs = [
        (300, 2, 3, 5, "any", "divisible by **at least one** of 2, 3, or 5"),
        (180, 2, 3, 5, "a_or_b_not_c", "divisible by **2 or 3, but NOT by 5**"),
        (210, 2, 3, 7, "a_or_b_not_c", "divisible by **2 or 3, but NOT by 7**"),
    ]
    for idx_h, (N_lim, p1, p2, p3, mode, desc_en) in enumerate(div_pie_specs, 1):
        if mode == "any":
            ans = sum(1 for k in range(1, N_lim + 1) if k % p1 == 0 or k % p2 == 0 or k % p3 == 0)
            desc_ar = f"تقبل القسمة على **واحد على الأقل** من الأعداد {m(str(p1))} أو {m(str(p2))} أو {m(str(p3))}"
        else:
            ans = sum(1 for k in range(1, N_lim + 1) if (k % p1 == 0 or k % p2 == 0) and k % p3 != 0)
            desc_ar = f"تقبل القسمة على **{m(str(p1))} أو {m(str(p2))} ولا تقبل القسمة على {m(str(p3))}**"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo Inclusion–Exclusion card (#{idx_h}), how many integers in {m(f'\\{{1, 2, \\dots, {N_lim}\\}}')} are {desc_en}?",
            q_ar=f"في مسألة التضمين والإقصاء من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، كم عدداً صحيحاً في المجموعة {m(f'\\{{1, 2, \\dots, {N_lim}\\}}')} {desc_ar}؟",
            correct_val=ans,
            distractors=[ans + 12, ans - 12, N_lim - ans, ans + 6],
            hint_en=f"Use Inclusion–Exclusion on multiples of {m(f'{p1}, {p2}, {p3}')} inside {m(f'1 \\dots {N_lim}')}.",
            hint_ar=f"طبّق مبدأ التضمين والإقصاء على مضاعفات {m(f'{p1}, {p2}, {p3}')} ضمن الفترة {m(f'1 \\dots {N_lim}')}.",
            idea_en=f"Count multiples of {m(f'{p1}')} or {m(f'{p2}')} via PIE, then adjust for multiples of {m(str(p3))}.",
            steps_en=[
                f"Multiples of {m(str(p1))} or {m(str(p2))} in {m(f'1..{N_lim}')}: {m(f'{N_lim//p1} + {N_lim//p2} - {N_lim//(p1*p2)} = {N_lim//p1 + N_lim//p2 - N_lim//(p1*p2)}')}.",
                f"Applying the condition for prime {m(str(p3))} via Inclusion–Exclusion yields exact {m(str(ans))}.",
            ],
            check_en=f"Direct scan over all {m(str(N_lim))} integers confirms {m(str(ans))}.",
            idea_ar=f"نحسب اتحاد مضاعفات {m(str(p1))} و{m(str(p2))} بالتضمين والإقصاء ثم نطبق شرط المضاعف الثالث {m(str(p3))}.",
            steps_ar=[
                f"عدد مضاعفات {m(str(p1))} أو {m(str(p2))} هو {m(str(N_lim // p1 + N_lim // p2 - N_lim // (p1 * p2)))}.",
                f"بتطبيق شرط العدد {m(str(p3))} بالتضمين والإقصاء نحصل على {m(str(ans))}.",
            ],
            check_ar=f"الفحص المباشر للأعداد من {m('1')} إلى {m(str(N_lim))} يؤكد الناتج {m(str(ans))}.",
            diagram_en=svg_venn_3(f"÷{p1}", f"÷{p2}", f"÷{p3}", {"abc": "?"}),
        ))

    # Hard 18.4: Permutations of {1..6} with p(1)!=1, p(2)!=2, p(3)!=3 -> 426
    ans_p6 = sum(1 for p in itertools.permutations(range(1, 7)) if p[0] != 1 and p[1] != 2 and p[2] != 3)
    assert ans_p6 == 720 - 3 * 120 + 3 * 24 - 6 == 426
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
        q_en=f"In a 5-point Student Kangaroo partial-restriction problem (#4), how many permutations {m('(a_1, a_2, a_3, a_4, a_5, a_6)')} of {m('\\{1, 2, 3, 4, 5, 6\\}')} satisfy {m('a_1 \\ne 1')}, {m('a_2 \\ne 2')}, **and** {m('a_3 \\ne 3')} (with no restrictions on {m('a_4, a_5, a_6')})?",
        q_ar=f"في مسألة قيود جزئية من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم (٤)، كم تبديلاً {m('(a_1, a_2, a_3, a_4, a_5, a_6)')} للمجموعة {m('\\{1, 2, 3, 4, 5, 6\\}')} يحقق {m('a_1 \\ne 1')} و{m('a_2 \\ne 2')} **و**{m('a_3 \\ne 3')} (دون قيود على المواقع الثلاثة الأخيرة)؟",
        correct_val=ans_p6,
        distractors=[265, 360, 432, 420],
        hint_en=f"Apply Inclusion–Exclusion to the three bad events {m('E_1: a_1=1')}, {m('E_2: a_2=2')}, {m('E_3: a_3=3')}: {m('6! - 3\\cdot 5! + 3\\cdot 4! - 3!')}.",
        hint_ar=f"طبّق مبدأ التضمين والإقصاء على الأحداث الثلاثة الممنوعة: {m('6! - 3\\cdot 5! + 3\\cdot 4! - 3!')}.",
        idea_en=f"By Inclusion–Exclusion on the three restricted slots, {m('6! - \\binom{3}{1}5! + \\binom{3}{2}4! - \\binom{3}{3}3!')}.",
        steps_en=[
            f"Start with {m('6! = 720')}, subtract {m('3 \\times 5! = 360')}, add {m('3 \\times 4! = 72')}, and subtract {m('1 \\times 3! = 6')}.",
            f"Compute {m('720 - 360 + 72 - 6 = 426')}.",
        ],
        check_en=f"All {m('720')} permutations verified computationally give exact {m('426')}.",
        idea_ar=f"باستخدام التضمين والإقصاء على الشروط الثلاثة فقط نحسب {m('6! - 3(5!) + 3(4!) - 3!')}.",
        steps_ar=[
            f"نحسب {m('720 - 360 + 72 - 6 = 426')}.",
        ],
        check_ar=f"فحص جميع التبديلات الـ {m('720')} يعطي {m('426')} تبديلاً مقبولاً بالضبط.",
        diagram_en=svg_digit_slots(["≠1", "≠2", "≠3", "any"], "n = 6"),
    ))

    # Hard 18.5: Permutations of {1..5} avoiding consecutive blocks 12, 23, 34 -> 64
    ans_blk = sum(
        1 for p in itertools.permutations("12345")
        if "12" not in "".join(p) and "23" not in "".join(p) and "34" not in "".join(p)
    )
    assert ans_blk == 120 - 3 * 24 + 3 * 6 - 2 == 64
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
        q_en=f"On a 5-point Student Kangaroo adjacent-block card (#5), how many permutations of {m('(1, 2, 3, 4, 5)')} contain **none** of the adjacent ordered pairs {m('12')}, {m('23')}, or {m('34')}?",
        q_ar=f"في مسألة الأزواج المتجاورة من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم (٥)، كم تبديلاً للأعداد {m('(1, 2, 3, 4, 5)')} **لا يحتوي على أيٍّ** من الأزواج المتتالية المرتبة {m('12')} أو {m('23')} أو {m('34')}؟",
        correct_val=ans_blk,
        distractors=[44, 66, 72, 58],
        hint_en=f"Use Inclusion–Exclusion: gluing {m('k')} of the blocks {m('\\{12, 23, 34\\}')} reduces the {m('5')} symbols to {m('5 - k')} objects, leaving {m('(5 - k)!')} arrangements!",
        hint_ar=f"استخدم التضمين والإقصاء: دمج {m('k')} من الكتل {m('\\{12, 23, 34\\}')} يقلل عدد العناصر إلى {m('5 - k')} فيعطي {m('(5 - k)!')} ترتيباً!",
        idea_en=f"Gluing {m('1, 2, 3')} forbidden adjacencies leaves {m('4!, 3!, 2!')} arrangements respectively.",
        steps_en=[
            f"All permutations: {m('5! = 120')}; one block present: {m('\\binom{3}{1}4! = 72')}; two blocks present: {m('\\binom{3}{2}3! = 18')}; all three ({m('1234')} glued): {m('2! = 2')}.",
            f"By Inclusion–Exclusion: {m('120 - 72 + 18 - 2 = 64')}.",
        ],
        check_en=f"Exhaustive check of all {m('120')} permutations of {m('12345')} yields exact {m('64')}.",
        idea_ar=f"دمج الأزواج الممنوعة يحوّلها إلى كتل متماسكة فنطبق التضمين والإقصاء.",
        steps_ar=[
            f"نحسب {m('5! - 3(4!) + 3(3!) - 2! = 120 - 72 + 18 - 2 = 64')}.",
        ],
        check_ar=f"فحص جميع التبديلات الـ {m('120')} يؤكد وجود {m('64')} تبديلاً صالحاً بالضبط.",
        diagram_en=svg_digit_slots(["no12", "no23", "no34"], "5! PIE"),
    ))

    # ------------------------------------------------------------------
    # 19. kang_stu_graph_degrees_chromatic (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_graph_degrees_chromatic"
    easy_deg = [
        (6, 3, 4, 5),   # 6*3 + 4*5 = 38 -> E = 19
        (8, 3, 6, 4),   # 24 + 24 = 48 -> E = 24
        (5, 4, 8, 3),   # 20 + 24 = 44 -> E = 22
        (7, 4, 6, 5),   # 28 + 30 = 58 -> E = 29
        (9, 4, 5, 6),   # 36 + 30 = 66 -> E = 33
    ]
    for idx_e, (n1, d1, n2, d2) in enumerate(easy_deg, 1):
        deg_sum = n1 * d1 + n2 * d2
        assert deg_sum % 2 == 0
        ans = deg_sum // 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo graph card #{idx_e}, a simple network has {m(str(n1))} nodes of degree {m(str(d1))} and {m(str(n2))} nodes of degree {m(str(d2))}, and no other nodes. How many **edges** does the network have?",
            q_ar=f"في بطاقة نظرية البيانات بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، تتكون شبكة بسيطة من {m(str(n1))} رؤوس من الدرجة {m(str(d1))} و{m(str(n2))} رؤوس من الدرجة {m(str(d2))} فقط. كم **ضلعاً (حافة)** في هذه الشبكة؟",
            correct_val=ans,
            distractors=[deg_sum, ans + 3, ans - 3, n1 + n2 + d1 + d2],
            hint_en=f"By the Handshaking Lemma, the sum of all vertex degrees equals {m('2E')}.",
            hint_ar=f"بحسب توطئة المصافحات، مجموع درجات جميع الرؤوس يساوي ضعف عدد الأضلاع {m('2E')}.",
            idea_en=f"Each edge contributes {m('2')} to the total degree sum, so {m('E = \\frac{1}{2}\\sum \\deg(v)')}.",
            steps_en=[
                f"Sum of degrees: {m(f'{n1}({d1}) + {n2}({d2}) = {deg_sum}')}.",
                f"Divide by {m('2')}: {m(f'E = {deg_sum}/2 = {ans}')}.",
            ],
            check_en=f"Degree sum {m(str(deg_sum))} is even and yields {m(str(ans))} edges.",
            idea_ar=f"مجموع درجات الرؤوس يساوي {m('2E')} لأن كل ضلع يربط رأسين.",
            steps_ar=[
                f"مجموع الدرجات {m(f'= {n1}\\times {d1} + {n2}\\times {d2} = {deg_sum}')}.",
                f"عدد الأضلاع {m(f'E = {deg_sum}/2 = {ans}')}.",
            ],
            check_ar=f"المجموع زوجي والقسمة على {m('2')} تعطي {m(str(ans))} ضلعاً.",
            diagram_en=svg_graph_cycle_chords(6, full_kn=True),
        ))

    # Medium 19.1..19.5: Planar Euler V - E + F = 2
    euler_specs = [
        (12, 4, "faces", "A connected planar graph has 12 vertices, each of degree 4. Into how many regions (faces, including the outer infinite region) does it divide the plane?",
         "بيان مستوٍ متصل له ١٢ رأساً، درجة كل رأس منها ٤. إلى كم منطقة (وجهاً، بما في ذلك المنطقة الخارجية) يقسم هذا البيان المستوي؟"),
        (10, 3, "faces", "A connected 3-regular planar graph has 10 vertices (every vertex has degree 3). How many faces (including the exterior face) does its planar drawing have?",
         "بيان مستوٍ متصل منتظم من الدرجة ٣ له ١٠ رؤوس. كم وجهاً (بما فيها الوجه الخارجي) في تمثيله المستوي؟"),
        (16, 3, "faces", "A convex polyhedron has 16 vertices, and exact 3 edges meet at every vertex. How many **faces** does this polyhedron have?",
         "متعدد وجوه محدب له ١٦ رأساً، وتلتقي عند كل رأس ٣ أحرف بالضبط. كم **وجهاً** لهذا المجسم؟"),
        (8, 4, "faces", "A convex polyhedron has 8 vertices, and exact 4 edges meet at every vertex. How many **faces** does this polyhedron have?",
         "متعدد وجوه محدب له ٨ رؤوس، وتلتقي عند كل رأس ٤ أحرف بالضبط. كم **وجهاً** لهذا المجسم؟"),
    ]
    for idx_m, (V_g, deg_g, _, q_body_en, q_body_ar) in enumerate(euler_specs, 1):
        E_g = (V_g * deg_g) // 2
        ans = E_g - V_g + 2
        assert V_g - E_g + ans == 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo Euler problem #{idx_m}: {q_body_en}",
            q_ar=f"في مسألة أويلر بمسابقة الكانجارو للمستوى المتقدم ({idx_m}): {q_body_ar}",
            correct_val=ans,
            distractors=[ans - 1, ans + 2, E_g, ans - 2],
            hint_en=f"First find {m('E = \\frac{1}{2}V \\cdot d')} via the Handshaking Lemma, then apply Euler's formula {m('V - E + F = 2')}.",
            hint_ar=f"احسب أولاً عدد الأحرف {m('E = \\frac{1}{2}V \\cdot d')}، ثم طبّق صيغة أويلر {m('V - E + F = 2')}.",
            idea_en=f"Combine {m(f'2E = {deg_g}V')} with Euler's planar invariant {m('F = E - V + 2')}.",
            steps_en=[
                f"Edges: {m(f'E = ({V_g} \\times {deg_g})/2 = {E_g}')}.",
                f"Faces by Euler's formula: {m(f'F = {E_g} - {V_g} + 2 = {ans}')}.",
            ],
            check_en=f"Check {m(f'V - E + F = {V_g} - {E_g} + {ans} = 2')}.",
            idea_ar=f"ندمج قانون المصافحات مع علاقة أويلر {m('V - E + F = 2')}.",
            steps_ar=[
                f"عدد الأحرف {m(f'E = ({V_g}\\times {deg_g})/2 = {E_g}')}.",
                f"عدد الأوجه {m(f'F = {E_g} - {V_g} + 2 = {ans}')}.",
            ],
            check_ar=f"التحقق: {m(f'{V_g} - {E_g} + {ans} = 2')}.",
            diagram_en=svg_graph_cycle_chords(6, full_kn=False),
        ))

    # Medium 19.5: Soccer-ball fullerene polyhedron (12 pentagons, 20 hexagons, 3 faces per vertex -> V = 60)
    E_soc = (12 * 5 + 20 * 6) // 2
    V_soc = (12 * 5 + 20 * 6) // 3
    assert V_soc - E_soc + 32 == 2 and V_soc == 60
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
        q_en=f"In Grade 11–12 Student Kangaroo polyhedron problem #5, a soccer-ball polyhedron has {m('12')} pentagonal faces and {m('20')} hexagonal faces, and exact {m('3')} faces meet at every vertex. How many **vertices** does it have?",
        q_ar=f"في مسألة المجسمات بمسابقة الكانجارو للمستوى المتقدم (٥)، يتكون مجسم كرة القدم من {m('12')} وجهاً خماسياً و{m('20')} وجهاً سداسياً، وتلتقي عند كل رأس {m('3')} أوجه بالضبط. كم **رأساً** لهذا المجسم؟",
        correct_val=V_soc,
        distractors=[90, 48, 72, 54],
        hint_en=f"Count total polygon corners {m('12 \\times 5 + 20 \\times 6')}; since {m('3')} polygons meet at each vertex, divide by {m('3')}!",
        hint_ar=f"احسب مجموع رؤوس المضلعات {m('12 \\times 5 + 20 \\times 6')}؛ وبما أن كل رأس يجمع {m('3')} أوجه فاقسم على {m('3')}!",
        idea_en=f"Total face-corners {m('12(5) + 20(6) = 180')} counts each degree-3 vertex {m('3')} times, giving {m('V = 60')}.",
        steps_en=[
            f"Sum of face sides: {m('12 \\times 5 + 20 \\times 6 = 60 + 120 = 180')}.",
            f"Hence {m('E = 180/2 = 90')} edges and {m('V = 180/3 = 60')} vertices.",
        ],
        check_en=f"Euler check: {m('V - E + F = 60 - 90 + (12 + 20) = 2')}.",
        idea_ar=f"مجموع زوايا الأوجه {m('180')} وكل رأس تشترك فيه {m('3')} أوجه فيكون {m('V = 60')}.",
        steps_ar=[
            f"مجموع أضلاع الأوجه {m('12\\times 5 + 20\\times 6 = 180')}.",
            f"عدد الرؤوس {m('V = 180 / 3 = 60')}.",
        ],
        check_ar=f"تحقق أويلر: {m('60 - 90 + 32 = 2')}.",
        diagram_en=svg_regular_polygon(6, [(0, 3), (1, 4), (2, 5)]),
    ))

    # Hard 19.1..19.5: Chromatic polynomials of Cycle C_n and Wheel W_n
    chrom_specs = [
        (4, 4, False),  # C_4, 4 colors -> 84
        (5, 3, False),  # C_5, 3 colors -> 30
        (5, 4, False),  # C_5, 4 colors -> 240
        (4, 4, True),   # W_4, 4 colors -> 72
        (5, 4, True),   # W_5, 4 colors -> 120
    ]
    for idx_h, (n_cyc, k_col, is_wheel) in enumerate(chrom_specs, 1):
        if not is_wheel:
            ans = (k_col - 1) ** n_cyc + ((-1) ** n_cyc) * (k_col - 1)
            brute = sum(
                1 for col in itertools.product(range(k_col), repeat=n_cyc)
                if all(col[i] != col[(i + 1) % n_cyc] for i in range(n_cyc))
            )
            assert ans == brute
            g_en = f"a cycle of {m(str(n_cyc))} labeled vertices {m(f'v_1 - v_2 - \\dots - v_{{{n_cyc}}} - v_1')}"
            g_ar = f"دورة مكونة من {m(str(n_cyc))} رؤوس مرقمة {m(f'v_1 - v_2 - \\dots - v_{{{n_cyc}}} - v_1')}"
        else:
            ans = k_col * ((k_col - 2) ** n_cyc + ((-1) ** n_cyc) * (k_col - 2))
            brute = sum(
                1 for col in itertools.product(range(k_col), repeat=n_cyc + 1)
                if all(col[i] != col[n_cyc] and col[i] != col[(i + 1) % n_cyc] for i in range(n_cyc))
            )
            assert ans == brute
            g_en = f"a wheel graph with {m('1')} central hub connected to all {m(str(n_cyc))} labeled rim vertices of a {m(str(n_cyc))}-cycle"
            g_ar = f"بيان عجلة يتكون من رأس مركزي واحد متصل بجميع رؤوس دورة محيطية مرقمة عددها {m(str(n_cyc))}"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo graph-coloring card (#{idx_h}), you have {m(str(k_col))} distinct colors to color {g_en} so that **no two adjacent vertices share the same color**. How many proper colorings exist?",
            q_ar=f"في مسألة تلوين البيانات من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، يتوفر {m(str(k_col))} ألوان مختلفة لتلوين {g_ar} بحيث **لا يشترك رأسان متجاوران في نفس اللون**. كم تلويناً صحيحاً يوجد؟",
            correct_val=ans,
            distractors=[k_col * ((k_col - 1) ** (n_cyc - 1)), (k_col - 1) ** n_cyc, ans + k_col, max(6, ans - k_col * 2)],
            hint_en=f"A labeled {m('n')}-cycle with {m('m')} available colors has {m('(m - 1)^n + (-1)^n(m - 1)')} proper colorings (for a wheel, pick the hub color first and set {m('m = k - 1')} on the rim!).",
            hint_ar=f"الدورة المرقمة بطول {m('n')} مع {m('m')} ألوان لها {m('(m - 1)^n + (-1)^n(m - 1)')} تلويناً صحيحاً (وفي العجلة اختر لون المركز أولاً فيتبقى {m('m = k - 1')} للمحيط!).",
            idea_en=f"Apply the cycle chromatic polynomial {m('P(C_n, m) = (m - 1)^n + (-1)^n(m - 1)')}.",
            steps_en=[
                f"{'Choose the hub color in ' + m(str(k_col)) + ' ways, leaving ' + m(str(k_col - 1)) + ' colors for the rim cycle.' if is_wheel else 'Apply the cycle coloring formula directly with ' + m(f'm = {k_col}') + '.'}",
                f"Evaluate the formula to obtain exact {m(str(ans))} proper colorings.",
            ],
            check_en=f"Brute-force check over all {m(f'{k_col}^{{{n_cyc + (1 if is_wheel else 0)}}}')} color assignments confirms {m(str(ans))}.",
            idea_ar=f"نستخدم كثيرة الحدود اللونية للدورة {m('(m - 1)^n + (-1)^n(m - 1)')}.",
            steps_ar=[
                f"{'نختار لون المركز بـ ' + m(str(k_col)) + ' طرق فيبقى ' + m(str(k_col - 1)) + ' ألوان للدورة المحيطية.' if is_wheel else 'نطبق قانون تلوين الدورة بعدد الألوان ' + m(str(k_col)) + '.'}",
                f"الناتج الدقيق هو {m(str(ans))} تلويناً.",
            ],
            check_ar=f"الفحص الشامل لجميع التلوينات الممكنة يؤكد أن العدد الصحيح هو {m(str(ans))}.",
            diagram_en=svg_kang_necklace_beads(["?"] * n_cyc),
        ))

    # ------------------------------------------------------------------
    # 20. kang_stu_recurrence_tiling_states (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_recurrence_tiling_states"
    dom_shapes = [[(0, 0), (0, 1)], [(0, 0), (1, 0)]]
    for idx_e, n_col in enumerate([6, 7, 8, 9], 1):
        ans = _count_tilings(2, n_col, dom_shapes)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo tiling card #{idx_e}, in how many ways can a {m(f'2 \\times {n_col}')} rectangle be completely tiled with {m('1 \\times 2')} dominoes?",
            q_ar=f"في بطاقة التبليط بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، بكم طريقة يمكن تبليط مستطيل أبعاده {m(f'2 \\times {n_col}')} بالكامل باستخدام قطع دومينو {m('1 \\times 2')}؟",
            correct_val=ans,
            distractors=[ans + 8, max(5, ans - 5), 2 ** (n_col // 2), ans + 3],
            hint_en=f"Condition on the rightmost column (either {m('1')} vertical domino or {m('2')} stacked horizontal dominoes) to get Fibonacci recurrence {m('T_n = T_{n-1} + T_{n-2}')} with {m('T_1 = 1, T_2 = 2')}.",
            hint_ar=f"افحص العمود الأخير (قطعة رأسية واحدة أو قطعتان أفقيتان) لتحصل على متتالية فيبوناتشي {m('T_n = T_{n-1} + T_{n-2}')} مع {m('T_1 = 1, T_2 = 2')}.",
            idea_en=f"{m('2 \\times n')} domino tilings satisfy {m('T_n = T_{n-1} + T_{n-2} = F_{n+1}')}.",
            steps_en=[
                f"Generate the sequence from {m('T_1 = 1, T_2 = 2')}: {m('1, 2, 3, 5, 8, 13, 21, 34, 55')}.",
                f"Read off {m(f'T_{{{n_col}}} = {ans}')}.",
            ],
            check_en=f"Exact backtracking over the {m(f'2 \\times {n_col}')} grid confirms {m(str(ans))} tilings.",
            idea_ar=f"عدد طرق تبليط {m('2 \\times n')} يتبع متتالية فيبوناتشي {m('T_n = T_{n-1} + T_{n-2}')}.",
            steps_ar=[
                f"نولّد الحدود بدءاً من {m('1, 2, 3, 5, 8, 13, 21, 34, 55')}.",
                f"نجد أن {m(f'T_{{{n_col}}} = {ans}')}.",
            ],
            check_ar=f"البحث الشامل على الشبكة يؤكد وجود {m(str(ans))} تبليطاً بالضبط.",
            diagram_en=svg_kang_polyomino_board([[1, 1, 2, 3, 3, 4], [5, 6, 2, 7, 8, 4]]),
        ))

    # Easy 20.5: 1 x 9 strip with 1x1 squares and 1x3 trominoes -> 19
    ans_1x9 = _count_tilings(1, 9, [[(0, 0)], [(0, 0), (0, 1), (0, 2)]])
    assert ans_1x9 == 19
    items.append(make_kang_q(
        qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
        q_en=f"On Student Kangaroo tiling card #5, in how many ways can a {m('1 \\times 9')} strip be tiled using {m('1 \\times 1')} unit squares and {m('1 \\times 3')} horizontal trominoes?",
        q_ar=f"في بطاقة التبليط بمسابقة الكانجارو للمستوى المتقدم (٥)، بكم طريقة يمكن تبليط شريط {m('1 \\times 9')} باستخدام مربعات {m('1 \\times 1')} وقطع ثلاثية أفقية {m('1 \\times 3')}؟",
        correct_val=ans_1x9,
        distractors=[13, 21, 28, 16],
        hint_en=f"Use the recurrence {m('a_n = a_{n-1} + a_{n-3}')} starting from {m('a_0 = 1, a_1 = 1, a_2 = 1')}.",
        hint_ar=f"استخدم العلاقة التراجعية {m('a_n = a_{n-1} + a_{n-3}')} بدءاً من {m('a_0 = 1, a_1 = 1, a_2 = 1')}.",
        idea_en=f"Ending with a {m('1 \\times 1')} tile or a {m('1 \\times 3')} tile gives {m('a_n = a_{n-1} + a_{n-3}')}.",
        steps_en=[
            f"Compute {m('a_0..a_9')}: {m('1, 1, 1, 2, 3, 4, 6, 9, 13, 19')}.",
            f"Thus {m('a_9 = 19')}.",
        ],
        check_en=f"By number of {m('1 \\times 3')} tiles ({m('0, 1, 2, 3')}): {m('\\binom{9}{0} + \\binom{7}{1} + \\binom{5}{2} + \\binom{3}{3} = 1 + 7 + 10 + 1 = 19')}.",
        idea_ar=f"التبليط ينتهي بمربع {m('1\\times 1')} أو بقطعة {m('1\\times 3')} فيحقق {m('a_n = a_{n-1} + a_{n-3}')}.",
        steps_ar=[
            f"ببناء الحدود المتتالية نجد {m('1, 1, 1, 2, 3, 4, 6, 9, 13, 19')}.",
            f"إذن العدد يساوي {m('19')}.",
        ],
        check_ar=f"بالعد حسب عدد القطع الثلاثية: {m('1 + 7 + 10 + 1 = 19')}.",
        diagram_en=svg_kang_polyomino_board([[1, 2, 2, 2, 3, 4, 5, 5, 5]]),
    ))

    # Medium 20.1..20.5: Forbidden-pattern binary/ternary strings
    str_specs = [
        (10, "01", lambda s: "11" not in s,
         "binary strings of length 10 (over {0, 1}) do **not** contain two consecutive 1s (`11`)",
         "سلسلة ثنائية بطول ١٠ (من ٠ و١) **لا تحتوي** على واحدين متجاورين (`11`)",
         "Fibonacci recurrence a_n = a_{n-1} + a_{n-2} with a_1 = 2, a_2 = 3"),
        (6, "01", lambda s: "111" not in s,
         "binary strings of length 6 (over {0, 1}) do **not** contain three consecutive 1s (`111`)",
         "سلسلة ثنائية بطول ٦ (من ٠ و١) **لا تحتوي** على ثلاثة واحدات متتالية (`111`)",
         "Tribonacci recurrence a_n = a_{n-1} + a_{n-2} + a_{n-3} with a_1 = 2, a_2 = 4, a_3 = 7"),
        (7, "01", lambda s: "111" not in s,
         "binary strings of length 7 (over {0, 1}) do **not** contain three consecutive 1s (`111`)",
         "سلسلة ثنائية بطول ٧ (من ٠ و١) **لا تحتوي** على ثلاثة واحدات متتالية (`111`)",
         "Tribonacci recurrence a_n = a_{n-1} + a_{n-2} + a_{n-3} up to n = 7"),
        (4, "ABC", lambda s: "AA" not in s,
         "4-letter words over the alphabet {A, B, C} never contain two adjacent As (`AA`)",
         "كلمة من ٤ أحرف من الأبجدية {A, B, C} لا تحتوي أبداً على حرفي A متجاورين (`AA`)",
         "Recurrence a_n = 2 a_{n-1} + 2 a_{n-2} with a_1 = 3, a_2 = 8"),
        (5, "012", lambda s: all(not (s[i] != "0" and s[i + 1] != "0") for i in range(len(s) - 1)),
         "length-5 strings over {0, 1, 2} never have **two nonzero digits** adjacent to each other",
         "سلسلة بطول ٥ من الأرقام {0, 1, 2} لا يتجاور فيها أبداً **رقمان غير صفريين**",
         "State recurrence a_n = a_{n-1} + 2 a_{n-2} with a_1 = 3, a_2 = 5"),
    ]
    for idx_m, (L_s, alph, pred, desc_en, desc_ar, rule_note) in enumerate(str_specs, 1):
        ans = sum(1 for tup in itertools.product(alph, repeat=L_s) if pred("".join(tup)))
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=f"In Grade 11–12 Student Kangaroo recurrence problem #{idx_m}, how many {desc_en}?",
            q_ar=f"في مسألة العلاقات التراجعية بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، كم {desc_ar}؟",
            correct_val=ans,
            distractors=[(len(alph) ** L_s) - ans if (len(alph) ** L_s) - ans != ans else ans + 7, ans + 6, max(4, ans - 5), ans + 12],
            hint_en=f"Track the valid endings by length using: {rule_note}.",
            hint_ar=f"ابنِ علاقة تراجعية حسب آخر رمز أو رمزين في السلسلة وصولاً إلى الطول {m(str(L_s))}.",
            idea_en=f"Partition valid strings by their suffix state ({rule_note}).",
            steps_en=[
                f"Set up the linear recurrence by conditioning on the first {m('0')} (or non-{m('A')}) symbol from the right.",
                f"Iterating up to length {m(str(L_s))} yields exact {m(str(ans))} valid strings.",
            ],
            check_en=f"Exhaustive check across all {m(f'{len(alph)}^{{{L_s}}} = {len(alph)**L_s}')} strings confirms {m(str(ans))}.",
            idea_ar=f"نقسّم السلاسل المقبولة حسب نهايتها ونبني المتتالية التراجعية خطوة بخطوة.",
            steps_ar=[
                f"بحساب الحدود التراجعية حتى الطول {m(str(L_s))} نحصل على {m(str(ans))} سلسلة صالحة.",
            ],
            check_ar=f"الفحص الشامل لجميع السلاسل الـ {m(str(len(alph) ** L_s))} يؤكد الناتج {m(str(ans))}.",
            diagram_en=svg_binary_bulbs((1, 0, 1, 0, 1), ("s₁", "s₂", "s₃", "s₄", "s₅")),
        ))

    # Hard 20.1..20.5: 2D Domino + 2x2 / L-tromino / 3x6 tilings
    sq2 = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    trom_L = [
        [(0, 0), (0, 1), (1, 0)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 1), (1, 0), (1, 1)],
    ]
    hard_tile_specs = [
        (2, 6, dom_shapes + sq2,
         "a 2 × 6 board be tiled using 1 × 2 dominoes (horizontal or vertical) and 2 × 2 squares",
         "لوحة 2 × 6 باستخدام قطع دومينو 1 × 2 ومربعات 2 × 2",
         "T_n = T_{n-1} + 2 T_{n-2} (1 vertical domino, 2 horizontal dominoes, or one 2×2 square)"),
        (2, 7, dom_shapes + sq2,
         "a 2 × 7 board be tiled using 1 × 2 dominoes (horizontal or vertical) and 2 × 2 squares",
         "لوحة 2 × 7 باستخدام قطع دومينو 1 × 2 ومربعات 2 × 2",
         "T_n = T_{n-1} + 2 T_{n-2} with T_1 = 1, T_2 = 3"),
        (2, 5, dom_shapes + trom_L,
         "a 2 × 5 board be tiled using 1 × 2 dominoes and 3-square L-trominoes (rotations allowed)",
         "لوحة 2 × 5 باستخدام قطع دومينو 1 × 2 وقطع ثلاثية على شكل L (بجميع دوراناتها)",
         "T_n = 2 T_{n-1} + T_{n-3} with T_0 = 1, T_1 = 1, T_2 = 2"),
        (2, 6, dom_shapes + trom_L,
         "a 2 × 6 board be tiled using 1 × 2 dominoes and 3-square L-trominoes (rotations allowed)",
         "لوحة 2 × 6 باستخدام قطع دومينو 1 × 2 وقطع ثلاثية على شكل L (بجميع دوراناتها)",
         "T_n = 2 T_{n-1} + T_{n-3} -> 1, 1, 2, 5, 11, 24, 53"),
        (3, 6, dom_shapes,
         "a 3 × 6 rectangle be completely tiled using 1 × 2 dominoes",
         "مستطيل 3 × 6 بالكامل باستخدام قطع دومينو 1 × 2",
         "T_6 = 4 T_4 - T_2 with T_0 = 1, T_2 = 3, T_4 = 11 -> 41"),
    ]
    for idx_h, (r_b, c_b, sh_list, desc_en, desc_ar, rec_hint) in enumerate(hard_tile_specs, 1):
        ans = _count_tilings(r_b, c_b, sh_list)
        board_vis = [[(r + c) % 4 + 1 for c in range(c_b)] for r in range(r_b)]
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"On a 5-point Student Kangaroo state-tiling card (#{idx_h}), in how many distinct ways can {desc_en}?",
            q_ar=f"في مسألة تبليط متقدمة من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، بكم طريقة مختلفة يمكن تبليط {desc_ar}؟",
            correct_val=ans,
            distractors=[ans + 6, max(5, ans - 6), ans + 12, max(8, ans - 10)],
            hint_en=f"Use column-state dynamic programming: {rec_hint}.",
            hint_ar=f"استخدم حالات العمود لبناء العلاقة التراجعية خطوة بخطوة حتى العمود الأخير.",
            idea_en=f"Column-frontier recurrence ({rec_hint}) counts every valid tiling without overcounting.",
            steps_en=[
                f"Set up the coupled state transitions across columns {m(f'1 \\dots {c_b}')}.",
                f"Evaluating the recurrence gives exact {m(str(ans))} tilings.",
            ],
            check_en=f"Cell-by-cell bitmask backtracking confirms exact {m(str(ans))} complete tilings.",
            idea_ar=f"بتتبع حالات امتلاء الأعمدة المتتالية نحصل على العلاقة التراجعية الدقيقة.",
            steps_ar=[
                f"نحسب الحدود المتتالية للعلاقة التراجعية حتى العمود {m(str(c_b))}.",
                f"عدد التبليطات الممكنة يساوي {m(str(ans))} بالضبط.",
            ],
            check_ar=f"خوارزمية البحث الشامل تؤكد وجود {m(str(ans))} تبليطاً صحيحاً.",
            diagram_en=svg_kang_polyomino_board(board_vis),
        ))

    return items



def _unit_5_6_data_probability(offset: int = 300) -> list[dict]:
    items: list[dict] = []
    topic = "Data & Probability"

    # ------------------------------------------------------------------
    # 21. kang_stu_bayes_conditional_urns (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_bayes_conditional_urns"

    # Easy 21.1..21.5: Fair coin selects Box A (r1 red, b1 blue) or Box B (r2 red, b2 blue); total P(Red)
    easy_urns = [
        (3, 2, 1, 4, "Omar", "عمر"),
        (4, 1, 2, 3, "Lina", "لينا"),
        (3, 3, 5, 1, "Rayan", "ريان"),
        (2, 6, 6, 2, "Salma", "سلمى"),
        (5, 3, 1, 7, "Tariq", "طارق"),
    ]
    for idx_e, (r1, b1, r2, b2, n_en, n_ar) in enumerate(easy_urns, 1):
        pA = Fraction(r1, r1 + b1)
        pB = Fraction(r2, r2 + b2)
        ans = Fraction(1, 2) * pA + Fraction(1, 2) * pB
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=(
                f"In {n_en}'s Student Kangaroo urn game (#{idx_e}), Box A holds {m(str(r1))} red and {m(str(b1))} blue balls, "
                f"while Box B holds {m(str(r2))} red and {m(str(b2))} blue balls. {n_en} flips a fair coin to choose one box "
                f"with probability {m('1/2')} each, then draws one ball at random. What is the probability of drawing a **red** ball?"
            ),
            q_ar=(
                f"في لعبة الصناديق بمسابقة الكانجارو للمستوى المتقدم ({idx_e}) لدى {n_ar}، يحتوي الصندوق A على {m(str(r1))} كرات حمراء و{m(str(b1))} زرقاء، "
                f"ويحتوي الصندوق B على {m(str(r2))} حمراء و{m(str(b2))} زرقاء. يرمي {n_ar} قطعة نقد عادلة لاختيار أحد الصندوقين باحتمال {m('1/2')} لكل منهما ثم يسحب كرة عشوائياً. ما احتمال سحب كرة **حمراء**؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(r1 + r2, r1 + b1 + r2 + b2) if Fraction(r1 + r2, r1 + b1 + r2 + b2) != ans else ans + Fraction(1, 10),
                pA if pA != ans else ans + Fraction(1, 8),
                pB if pB != ans else ans - Fraction(1, 8),
                min(Fraction(19, 20), ans + Fraction(1, 6)),
            ],
            hint_en=f"By the Law of Total Probability, {m('P(\\text{Red}) = \\frac{1}{2} P(\\text{Red}\\mid A) + \\frac{1}{2} P(\\text{Red}\\mid B)')}.",
            hint_ar=f"بقانون الاحتمال الكلي: {m('P(\\text{Red}) = \\frac{1}{2} P(\\text{Red}\\mid A) + \\frac{1}{2} P(\\text{Red}\\mid B)')}.",
            idea_en="Average the two conditional red probabilities since each box is chosen with probability 1/2.",
            steps_en=[
                f"In Box A, {m(f'P(\\text{{Red}}\\mid A) = {r1}/{r1+b1}')}; in Box B, {m(f'P(\\text{{Red}}\\mid B) = {r2}/{r2+b2}')}.",
                f"Compute {m(f'\\frac{{1}}{{2}}\\left(\\frac{{{r1}}}{{{r1+b1}}} + \\frac{{{r2}}}{{{r2+b2}}}\\right) = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Both conditional probabilities lie between {m('0')} and {m('1')}, and their midpoint equals {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar="نحسب متوسط احتمالي سحب كرة حمراء من الصندوقين لأن اختيار كل صندوق متساوي الاحتمال.",
            steps_ar=[
                f"في الصندوق A الاحتمال {m(f'{r1}/{r1+b1}')} وفي الصندوق B الاحتمال {m(f'{r2}/{r2+b2}')}.",
                f"إذن الاحتمال الكلي يساوي {m(f'\\frac{{1}}{{2}}\\left(\\frac{{{r1}}}{{{r1+b1}}} + \\frac{{{r2}}}{{{r2+b2}}}\\right) = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"مجموع احتمالي الحمراء والزرقاء يساوي {m('1')}، وقيمة الاحتمال المختزلة هي {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_stu_probability_tree("1/2", "1/2", f"{r1}/{r1+b1}", f"{r2}/{r2+b2}", "Box A", "Box B"),
        ))

    # Medium 21.1..21.5: Reverse Bayes P(Box A | Red drawn) with weighted prior wA/(wA+wB)
    med_bayes = [
        (1, 1, 4, 1, 2, 3),
        (2, 1, 3, 2, 1, 4),
        (1, 2, 5, 1, 1, 2),
        (3, 2, 2, 2, 3, 1),
        (1, 1, 5, 3, 3, 5),
    ]
    for idx_m, (wA, wB, r1, b1, r2, b2) in enumerate(med_bayes, 1):
        prA = Fraction(wA, wA + wB)
        prB = Fraction(wB, wA + wB)
        num = prA * Fraction(r1, r1 + b1)
        den = num + prB * Fraction(r2, r2 + b2)
        ans = num / den
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=(
                f"On Student Kangaroo Bayes card #{idx_m}, Box A contains {m(str(r1))} gold and {m(str(b1))} silver coins, "
                f"and Box B contains {m(str(r2))} gold and {m(str(b2))} silver coins. Box A is chosen with probability {m(f'{wA}/{wA+wB}')} "
                f"and Box B with probability {m(f'{wB}/{wA+wB}')}. Given that a randomly drawn coin is **gold**, what is the conditional probability it came from **Box A**?"
            ),
            q_ar=(
                f"في بطاقة بايز بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، يضم الصندوق A عدد {m(str(r1))} عملات ذهبية و{m(str(b1))} فضية، "
                f"ويضم الصندوق B عدد {m(str(r2))} ذهبية و{m(str(b2))} فضية. يُختار الصندوق A باحتمال {m(f'{wA}/{wA+wB}')} والصندوق B باحتمال {m(f'{wB}/{wA+wB}')}. "
                f"إذا عُلم أن العملة المسحوبة **ذهبية**، فما الاحتمال الشرطي لأن تكون من **الصندوق A**؟"
            ),
            correct_val=ans,
            distractors=[
                den,
                prA if prA != ans else min(Fraction(15, 16), ans + Fraction(1, 7)),
                Fraction(r1, r1 + r2) if Fraction(r1, r1 + r2) != ans else max(Fraction(1, 12), ans - Fraction(1, 7)),
                Fraction(1, 1) - ans if Fraction(1, 1) - ans != ans else ans + Fraction(1, 9),
            ],
            hint_en=f"Apply Bayes' Rule: divide the Box-A gold branch {m('P(A)P(G\\mid A)')} by the sum of both gold branches.",
            hint_ar=f"طبّق قاعدة بايز: اقسم وزن مسار الذهب من A وهو {m('P(A)P(G\\mid A)')} على مجموع مساري الذهب.",
            idea_en="Compare the probability weight of (Box A and Gold) against total probability of Gold.",
            steps_en=[
                f"Branch A-Gold has probability {m(f'\\frac{{{wA}}}{{{wA+wB}}}\\cdot\\frac{{{r1}}}{{{r1+b1}}} = {num.numerator}/{num.denominator}')}.",
                f"Total Gold probability is {m(f'{den.numerator}/{den.denominator}')}, so {m(f'P(A\\mid G) = \\frac{{{num.numerator}/{num.denominator}}}{{{den.numerator}/{den.denominator}}} = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Notice {m(f'P(A\\mid G) + P(B\\mid G) = {ans.numerator}/{ans.denominator} + {(1-ans).numerator}/{(1-ans).denominator} = 1')}.",
            idea_ar="نقسم احتمال المسار المشترك (اختيار A وسحب عملة ذهبية) على الاحتمال الكلي لسحب عملة ذهبية.",
            steps_ar=[
                f"احتمال مسار A ثم ذهب يساوي {m(f'{num.numerator}/{num.denominator}')}، والاحتمال الكلي للذهب يساوي {m(f'{den.numerator}/{den.denominator}')}.",
                f"بقسمة المقدارين نحصل على {m(f'P(A\\mid G) = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"التحقق: مجموع الاحتمالين اللاحقين للصندوقين يساوي {m('1')} تماماً.",
            diagram_en=svg_stu_probability_tree(f"{wA}/{wA+wB}", f"{wB}/{wA+wB}", f"{r1}/{r1+b1}", f"{r2}/{r2+b2}", "Box A", "Box B"),
        ))

    # Hard 21.1..21.5: Sequential transfer Jar 1 -> Jar 2, then draw from Jar 2 (or reverse Bayes on transferred color!)
    hard_transfers = [
        (3, 2, 2, 3, False),
        (4, 1, 1, 4, False),
        (3, 3, 4, 1, True),
        (4, 2, 2, 3, True),
        (5, 1, 1, 3, True),
    ]
    for idx_h, (r1, b1, r2, b2, ask_posterior) in enumerate(hard_transfers, 1):
        t_red = Fraction(r1, r1 + b1)
        t_blue = Fraction(b1, r1 + b1)
        p_red2_given_tred = Fraction(r2 + 1, r2 + b2 + 1)
        p_red2_given_tblue = Fraction(r2, r2 + b2 + 1)
        total_red2 = t_red * p_red2_given_tred + t_blue * p_red2_given_tblue
        if not ask_posterior:
            ans = total_red2
            q_tail_en = "What is the probability that the ball drawn from Jar B is **red**?"
            q_tail_ar = "ما احتمال أن تكون الكرة المسحوبة من الوعاء B **حمراء**؟"
        else:
            ans = (t_red * p_red2_given_tred) / total_red2
            q_tail_en = "If the ball drawn from Jar B turns out to be **red**, what is the conditional probability that the **transferred** ball from Jar A to Jar B was also **red**?"
            q_tail_ar = "إذا ظهرت الكرة المسحوبة من الوعاء B **حمراء**، فما الاحتمال الشرطي لأن تكون الكرة **المنقولة** من A إلى B **حمراء** أيضاً؟"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=(
                f"In a 5-point Student Kangaroo transfer puzzle (#{idx_h}), Jar A initially holds {m(str(r1))} red and {m(str(b1))} blue marbles, "
                f"while Jar B holds {m(str(r2))} red and {m(str(b2))} blue marbles. One marble is moved unseen at random from Jar A into Jar B, "
                f"and then one marble is drawn at random from Jar B. {q_tail_en}"
            ),
            q_ar=(
                f"في مسألة النقل العشوائي من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، يضم الوعاء A في البداية {m(str(r1))} كرات حمراء و{m(str(b1))} زرقاء، "
                f"ويضم الوعاء B عدد {m(str(r2))} حمراء و{m(str(b2))} زرقاء. نُقلت كرة واحدة عشوائياً دون النظر إليها من A إلى B، ثم سُحبت كرة عشوائياً من B. {q_tail_ar}"
            ),
            correct_val=ans,
            distractors=[
                t_red if t_red != ans else ans + Fraction(1, 11),
                Fraction(r2, r2 + b2) if Fraction(r2, r2 + b2) != ans else ans - Fraction(1, 11),
                p_red2_given_tred if p_red2_given_tred != ans else ans + Fraction(1, 9),
                total_red2 if (ask_posterior and total_red2 != ans) else min(Fraction(29, 30), ans + Fraction(1, 7)),
            ],
            hint_en=f"After moving {m('1')} marble into Jar B, Jar B always contains {m(str(r2 + b2 + 1))} marbles—split into the two transfer cases!",
            hint_ar=f"بعد نقل كرة واحدة إلى B يصبح مجموع كرات B يساوي {m(str(r2 + b2 + 1))} دائماً؛ قسّم المسألة إلى حالتي لون الكرة المنقولة!",
            idea_en="Condition on the color of the transferred marble from Jar A to Jar B.",
            steps_en=[
                f"Transferring red happens with probability {m(f'{r1}/{r1+b1}')} and makes Jar B hold {m(f'{r2+1}')} red out of {m(f'{r2+b2+1}')}.",
                f"Transferring blue happens with probability {m(f'{b1}/{r1+b1}')} and makes Jar B hold {m(f'{r2}')} red out of {m(f'{r2+b2+1}')}.",
                f"Combining the two branches gives {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Exact rational verification over all {m(str((r1 + b1) * (r2 + b2 + 1)))} equally likely two-step outcomes confirms {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar="نفصّل الحالتين الممكنتين للكرة المنقولة (حمراء أو زرقاء) ونحسب وزن كل فرع بدقة.",
            steps_ar=[
                f"احتمال نقل كرة حمراء هو {m(f'{r1}/{r1+b1}')} فيصبح في B عدد {m(f'{r2+1}')} حمراء من أصل {m(f'{r2+b2+1}')}.",
                f"واحتمال نقل زرقاء هو {m(f'{b1}/{r1+b1}')} فيبقى في B عدد {m(f'{r2}')} حمراء من أصل {m(f'{r2+b2+1}')}.",
                f"بحساب النسبة المطلوبة نحصل على {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"العدّ الشامل لجميع الحالات المتساوية وعددها {m(str((r1 + b1) * (r2 + b2 + 1)))} يؤكد الناتج {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_two_jars(f"A ({r1}R,{b1}B)", r1 / (r1 + b1), f"B ({r2}R,{b2}B)", r2 / (r2 + b2), "1 →"),
        ))

    # ------------------------------------------------------------------
    # 22. kang_stu_linearity_expectation_indicators (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_linearity_expectation_indicators"

    # Easy 22.1..22.5: Expected fixed points in random permutation of n + k guaranteed fixed / or expected heads/matches
    easy_lin = [
        (6, 1, "expected number of envelopes that receive their **matching** letter when 6 letters are placed randomly, one per envelope"),
        (8, 2, "expected number of students who receive **both** their own hat and a bonus sticker if every fixed point awards 2 stickers among 8 students"),
        (10, 3, "expected total points when 10 numbered cards are dealt onto spots 1..10 and each card landing on its own number scores 3 points"),
        (12, 5, "expected total prize (in riyals) when 12 keys are assigned randomly to 12 locks and each key opening its matching lock pays 5 riyals"),
        (15, 4, "expected score when 15 name tags are handed out randomly to 15 finalists and each correct match earns 4 points"),
    ]
    easy_lin_ar = [
        "القيمة المتوقعة لعدد المظاريف التي تستلم رسالتها **الصحيحة** عند توزيع ٦ رسائل عشوائياً واحدة في كل مظروف",
        "القيمة المتوقعة لمجموع الملصقات إذا حصل كل طالب يستلم قبعته الصحيحة على ملصقين عند توزيع ٨ قبعات عشوائياً على ٨ طلاب",
        "القيمة المتوقعة لمجموع النقاط عند توزيع ١٠ بطاقات مرقمة عشوائياً على المواقع ١..١٠ إذا كانت كل بطاقة في موقعها الصحيح تمنح ٣ نقاط",
        "القيمة المتوقعة للجائزة بالريال عند توزيع ١٢ مفتاحاً عشوائياً على ١٢ قفلاً إذا كان كل مفتاح يطابق قفله يمنح ٥ ريالات",
        "القيمة المتوقعة لمجموع النقاط عند توزيع ١٥ بطاقة اسم عشوائياً على ١٥ متسابقاً إذا كان كل تطابق صحيح يمنح ٤ نقاط",
    ]
    for idx_e, ((n_it, pts_each, desc_en), desc_ar) in enumerate(zip(easy_lin, easy_lin_ar), 1):
        # E[fixed points] = n * (1/n) = 1, so total expected score = pts_each!
        # Wait: make answers vary cleanly across questions! pts_each = 1, 2, 3, 5, 4 -> distinct answers!
        ans = pts_each
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=f"On Student Kangaroo expectation card #{idx_e}, what is the {desc_en}?",
            q_ar=f"في بطاقة التوقع الرياضي بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، ما {desc_ar}؟",
            correct_val=ans,
            distractors=[n_it, n_it * pts_each, ans + 2, max(0, ans - 1) if max(0, ans - 1) != ans else ans + 4],
            hint_en=f"Define an indicator {m('I_k')} for item {m('k')} landing in spot {m('k')}: {m(f'P(I_k = 1) = 1/{n_it}')}, then sum over all {m(str(n_it))} items!",
            hint_ar=f"عرّف متغير مؤشر {m('I_k')} لكل عنصر {m('k')}: احتمال تطابقه هو {m(f'1/{n_it}')}، ثم اجمع التوقعات للـ {m(str(n_it))} عنصراً!",
            idea_en=f"By Linearity of Expectation, expected fixed points always equal {m(f'{n_it} \\times \\frac{{1}}{{{n_it}}} = 1')}, even though the indicators are dependent!",
            steps_en=[
                f"Each item {m('k \\in \\{1,\\dots,' + str(n_it) + '\\}')} lands in its own spot with probability {m(f'1/{n_it}')}.",
                f"Summing {m(str(n_it))} expectations of {m(f'{pts_each}/{n_it}')} gives {m(f'{n_it} \\times \\frac{{{pts_each}}}{{{n_it}}} = {ans}')}.",
            ],
            check_en=f"Check for {m('n = 2')}: half the time {m('2')} matches ({m(str(2 * pts_each))} pts) and half the time {m('0')} matches ({m('0')} pts), averaging {m(str(ans))}!",
            idea_ar=f"بخطية التوقع الرياضي، التوقع الكلي لعدد النقاط الثابتة يساوي دائماً {m(f'{n_it} \\times \\frac{{1}}{{{n_it}}} = 1')}.",
            steps_ar=[
                f"احتمال وقوع العنصر رقم {m('k')} في مكانه الصحيح يساوي {m(f'1/{n_it}')}.",
                f"بجمع التوقعات لجميع العناصر الـ {m(str(n_it))} وضربها في {m(str(pts_each))} نحصل على {m(str(ans))}.",
            ],
            check_ar=f"لا يشترط الاستقلال لتطبيق خطية التوقع؛ الناتج الدقيق هو {m(str(ans))}.",
            diagram_en=svg_number_strip(["1", "2", "...", str(n_it), "?"]),
        ))

    # Medium 22.1..22.5: Expected adjacent BG/different-color pairs in a row or circle of R red and B blue tokens
    med_lin = [
        (4, 6, False),  # row of 10: 9 * 2*4*6 / (10*9) = 48/10 = 24/5
        (3, 5, True),   # circle of 8: 8 * 2*3*5 / (8*7) = 30/7
        (5, 5, False),  # row of 10: 9 * 50 / 90 = 5
        (4, 5, True),   # circle of 9: 9 * 40 / 72 = 5
        (6, 4, True),   # circle of 10: 10 * 48 / 90 = 16/3
    ]
    for idx_m, (nR, nB, is_circle) in enumerate(med_lin, 1):
        N_tot = nR + nB
        n_pairs = N_tot if is_circle else (N_tot - 1)
        p_diff = Fraction(2 * nR * nB, N_tot * (N_tot - 1))
        ans = n_pairs * p_diff
        # Verify by exact combinatorial enumeration!
        red_subsets = list(itertools.combinations(range(N_tot), nR))
        tot_adj = 0
        for rset in red_subsets:
            rs = set(rset)
            if is_circle:
                tot_adj += sum(1 for i in range(N_tot) if (i in rs) != (((i + 1) % N_tot) in rs))
            else:
                tot_adj += sum(1 for i in range(N_tot - 1) if (i in rs) != ((i + 1) in rs))
        assert ans == Fraction(tot_adj, len(red_subsets))
        arr_en = "around a circular ring" if is_circle else "in a straight row"
        arr_ar = "حول حلقة دائرية" if is_circle else "في صف مستقيم"
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=(
                f"In Student Kangaroo indicator puzzle #{idx_m}, {m(str(nR))} red tokens and {m(str(nB))} blue tokens "
                f"are arranged uniformly at random {arr_en}. What is the **expected number** of adjacent pairs of tokens that have **different colors**?"
            ),
            q_ar=(
                f"في مسألة المؤشرات بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، رُتّب {m(str(nR))} أقراص حمراء و{m(str(nB))} أقراص زرقاء "
                f"عشوائياً بانتظام {arr_ar}. ما **القيمة المتوقعة** لعدد الأزواج المتجاورة ذات **اللونين المختلفين**؟"
            ),
            correct_val=ans,
            distractors=[
                ans + 1,
                max(Fraction(1, 2), ans - 1),
                (N_tot - 1) * p_diff if is_circle else N_tot * p_diff,
                Fraction(nR * nB, N_tot) if Fraction(nR * nB, N_tot) != ans else ans + Fraction(1, 2),
            ],
            hint_en=f"There are {m(str(n_pairs))} adjacent pairs {arr_en}, and any two random slots hold opposite colors with probability {m(f'\\frac{{2 \\cdot {nR} \\cdot {nB}}}{{{N_tot} \\cdot {N_tot - 1}}}')}.",
            hint_ar=f"يوجد {m(str(n_pairs))} أزواج متجاورة {arr_ar}، واحتمال اختلاف اللون في أي زوج معين هو {m(f'\\frac{{2 \\cdot {nR} \\cdot {nB}}}{{{N_tot} \\cdot {N_tot - 1}}}')}.",
            idea_en="Sum indicator probabilities over all adjacent neighbor slots.",
            steps_en=[
                f"Each adjacent pair holds one red and one blue token with probability {m(f'\\frac{{2({nR})({nB})}}{{{N_tot}({N_tot-1})}} = {p_diff.numerator}/{p_diff.denominator}')}.",
                f"Multiply by the {m(str(n_pairs))} adjacent pairs: {m(f'{n_pairs} \\times \\frac{{{p_diff.numerator}}}{{{p_diff.denominator}}} = {ans.numerator}') if ans.denominator == 1 else m(f'{n_pairs} \\times \\frac{{{p_diff.numerator}}}{{{p_diff.denominator}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
            ],
            check_en=f"Averaging over all {m(f'\\binom{{{N_tot}}}{{{nR}}} = {len(red_subsets)}')} equally likely arrangements gives {m(f'{tot_adj}/{len(red_subsets)}')}.",
            idea_ar="نجمع توقعات متغيرات المؤشر لجميع المواضع المتجاورة.",
            steps_ar=[
                f"احتمال اختلاف اللون في أي موضعين متجاورين يساوي {m(f'{p_diff.numerator}/{p_diff.denominator}')}.",
                f"نضرب في عدد الأزواج المتجاورة ({m(str(n_pairs))}) لنحصل على القيمة المتوقعة الدقيقة.",
            ],
            check_ar=f"المتوسط الحسابي عبر جميع التراتيب الممكنة وعددها {m(str(len(red_subsets)))} يطابق الناتج تماماً.",
            diagram_en=svg_round_table(N_tot) if is_circle else svg_number_strip(["R", "B", "?", "...", "R"]),
        ))

    # Hard 22.1..22.5: Expected distinct occupied bins when k balls drop into n bins: n * (1 - ((n-1)/n)^k), or expected local maxima / runs!
    hard_lin = [
        (3, 3, "bins"),   # 3 * (1 - (2/3)^3) = 3 * 19/27 = 19/9
        (4, 2, "boxes"),  # 4 * (1 - 9/16) = 7/4
        (4, 3, "urns"),   # 4 * (1 - 27/64) = 37/16
        (3, 4, "slots"),  # 3 * (1 - 16/81) = 65/27
        (5, 2, "trays"),  # 5 * (1 - 16/25) = 9/5
    ]
    for idx_h, (n_bins, k_balls, word_b) in enumerate(hard_lin, 1):
        ans = n_bins * (Fraction(1, 1) - Fraction(n_bins - 1, n_bins) ** k_balls)
        brute = Fraction(
            sum(len(set(tup)) for tup in itertools.product(range(n_bins), repeat=k_balls)),
            n_bins ** k_balls,
        )
        assert ans == brute
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=(
                f"On a 5-point Student Kangaroo coupon-collector card (#{idx_h}), {m(str(k_balls))} balls are dropped "
                f"independently and uniformly at random into {m(str(n_bins))} labeled {word_b}. What is the **expected number of non-empty {word_b}**?"
            ),
            q_ar=(
                f"في بطاقة التوقع الرياضي من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، أُسقطت {m(str(k_balls))} كرات "
                f"بشكل مستقل وعشوائي منتظم في {m(str(n_bins))} صناديق مرقمة. ما **القيمة المتوقعة لعدد الصناديق غير الفارغة**؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(k_balls, 1) if Fraction(k_balls, 1) != ans else ans + Fraction(1, 3),
                n_bins * Fraction(n_bins - 1, n_bins) ** k_balls,
                ans + Fraction(1, n_bins),
                max(Fraction(1, 2), ans - Fraction(1, n_bins)),
            ],
            hint_en=f"Each single bin stays empty with probability {m(f'(( {n_bins}-1 )/{n_bins})^{{{k_balls}}}')}, so it is non-empty with probability {m(f'1 - ({n_bins-1}/{n_bins})^{{{k_balls}}}')}!",
            hint_ar=f"احتمال بقاء صندوق معين فارغاً هو {m(f'({n_bins-1}/{n_bins})^{{{k_balls}}}')}، فيكون احتمال احتوائه على كرة على الأقل {m(f'1 - ({n_bins-1}/{n_bins})^{{{k_balls}}}')}!",
            idea_en=f"Attach an indicator {m('I_j')} to each of the {m(str(n_bins))} {word_b} being non-empty.",
            steps_en=[
                f"A fixed bin misses all {m(str(k_balls))} balls with probability {m(f'\\left(\\frac{{{n_bins-1}}}{{{n_bins}}}\\right)^{{{k_balls}}}')}.",
                f"Multiply {m(f'1 - \\left(\\frac{{{n_bins-1}}}{{{n_bins}}}\\right)^{{{k_balls}}}')} by {m(str(n_bins))} to get {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Exact enumeration of all {m(f'{n_bins}^{{{k_balls}}} = {n_bins**k_balls}')} placements confirms {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar=f"نضع مؤشراً لكل صندوق يساوي {m('1')} إذا لم يكن فارغاً ونطبق خطية التوقع.",
            steps_ar=[
                f"احتمال خلو صندوق معين من جميع الكرات الـ {m(str(k_balls))} هو {m(f'({n_bins-1}/{n_bins})^{{{k_balls}}}')}.",
                f"نضرب الاحتمال المتمم في {m(str(n_bins))} فنحصل على {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"العدّ الشامل لجميع التوزيعات وعددها {m(str(n_bins ** k_balls))} يؤكد الناتج {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_digit_slots([f"B{i+1}" for i in range(n_bins)]),
        ))

    # ------------------------------------------------------------------
    # 23. kang_stu_geometric_prob_meeting_square (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_geometric_prob_meeting_square"

    # Easy 23.1..23.5: Classic symmetric meeting problem |x - y| <= t on [0, L]^2 -> 1 - ((L-t)/L)^2
    easy_meet = [
        (60, 15),  # 1 - (3/4)^2 = 7/16
        (60, 20),  # 1 - (2/3)^2 = 5/9
        (60, 12),  # 1 - (4/5)^2 = 9/25
        (40, 10),  # 7/16 -> wait, let's keep distinct ratios! (60, 30) -> 3/4
        (50, 10),  # 9/25 -> let's use (60, 10) -> 1 - 25/36 = 11/36!
    ]
    easy_meet = [(60, 15), (60, 20), (60, 12), (60, 30), (60, 10)]
    for idx_e, (L_min, w_min) in enumerate(easy_meet, 1):
        ans = Fraction(1, 1) - Fraction(L_min - w_min, L_min) ** 2
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=(
                f"In Student Kangaroo meeting puzzle #{idx_e}, two friends arrive independently and uniformly at random "
                f"during a {m(str(L_min))}-minute lunch hour between {m('12{:}00')} and {m('1{:}00')}. Each waits {m(str(w_min))} minutes "
                f"before leaving. What is the probability that they **meet**?"
            ),
            q_ar=(
                f"في لغز اللقاء بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، يصل صديقان بشكل مستقل وعشوائي منتظم "
                f"خلال ساعة غداء مدتها {m(str(L_min))} دقيقة بين الساعة {m('12{:}00')} و{m('1{:}00')}، وينتظر كل منهما {m(str(w_min))} دقيقة قبل المغادرة. ما احتمال أن **يلتقيا**؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(w_min, L_min),
                Fraction(2 * w_min, L_min) if 2 * w_min < L_min else Fraction(5, 6),
                Fraction(1, 1) - ans,
                Fraction(w_min * w_min, L_min * L_min),
            ],
            hint_en=f"Plot arrival times {m('(x, y)')} in the {m(f'{L_min} \\times {L_min}')} square: the two unshaded miss corners form a combined square of side {m(f'{L_min} - {w_min} = {L_min - w_min}')}!",
            hint_ar=f"مثّل وقتي الوصول {m('(x, y)')} داخل مربع {m(f'{L_min} \\times {L_min}')}: مثلثا عدم اللقاء يكوّنان معاً مربعاً طول ضلعه {m(str(L_min - w_min))}!",
            idea_en=f"Subtract the two congruent right-triangle miss regions from the {m(f'{L_min} \\times {L_min}')} square.",
            steps_en=[
                f"They miss each other when {m(f'|x - y| > {w_min}')}, forming two corner right triangles of leg {m(str(L_min - w_min))}.",
                f"Combined miss probability is {m(f'\\left(\\frac{{{L_min - w_min}}}{{{L_min}}}\\right)^2')}, so meeting probability is {m(f'1 - \\left(\\frac{{{L_min - w_min}}}{{{L_min}}}\\right)^2 = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Band area = {m(f'{L_min}^2 - {L_min - w_min}^2 = {L_min**2 - (L_min - w_min)**2}')}, giving {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar=f"نطرح مساحة مثلثي عدم اللقاء من المساحة الكلية للمربع {m(f'{L_min} \\times {L_min}')}.",
            steps_ar=[
                f"يتحقق عدم اللقاء عندما {m(f'|x - y| > {w_min}')} وهما مثلثان قائمان ضلع كل منهما {m(str(L_min - w_min))}.",
                f"إذن احتمال اللقاء يساوي {m(f'1 - \\left(\\frac{{{L_min - w_min}}}{{{L_min}}}\\right)^2 = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"نسبة المساحة المظللة إلى مساحة المربع تساوي {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_stu_meeting_square(str(L_min), "?"),
        ))

    # Medium 23.1..23.5: Asymmetric waits (a waits t1, b waits t2) on [0, L]^2 -> 1 - ((L-t1)^2 + (L-t2)^2)/(2 L^2)
    med_meet = [
        (60, 10, 20),
        (60, 15, 30),
        (60, 12, 24),
        (40, 10, 20),
        (50, 10, 25),
    ]
    for idx_m, (Lm, t1, t2) in enumerate(med_meet, 1):
        miss_twice = (Lm - t1) ** 2 + (Lm - t2) ** 2
        ans = Fraction(2 * Lm * Lm - miss_twice, 2 * Lm * Lm)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=(
                f"On Student Kangaroo asymmetric-meeting card #{idx_m}, Ali and Badr arrive independently and uniformly "
                f"during a {m(str(Lm))}-minute window. Ali waits {m(str(t1))} minutes if he arrives first, whereas Badr waits "
                f"{m(str(t2))} minutes if he arrives first. What is the probability that they **meet**?"
            ),
            q_ar=(
                f"في مسألة اللقاء غير المتماثل بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، يصل علي وبدر بشكل مستقل وعشوائي منتظم "
                f"خلال نافذة مدتها {m(str(Lm))} دقيقة. ينتظر علي {m(str(t1))} دقيقة إذا وصل أولاً، بينما ينتظر بدر {m(str(t2))} دقيقة إذا وصل أولاً. ما احتمال أن **يلتقيا**؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(t1 + t2, Lm),
                Fraction(1, 1) - ans,
                Fraction(Lm * Lm - (Lm - t1) * (Lm - t2), Lm * Lm),
                min(Fraction(19, 20), ans + Fraction(1, 12)),
            ],
            hint_en=f"The two miss corners now have different legs: {m(f'{Lm} - {t1} = {Lm - t1}')} and {m(f'{Lm} - {t2} = {Lm - t2}')}!",
            hint_ar=f"مثلثا عدم اللقاء قائمان ومتساويان الساقين بطولي ضلعين مختلفين: {m(str(Lm - t1))} و{m(str(Lm - t2))}!",
            idea_en=f"Subtract the two corner triangle areas {m(f'\\frac{{1}}{{2}}({Lm - t1})^2')} and {m(f'\\frac{{1}}{{2}}({Lm - t2})^2')} from {m(f'{Lm}^2')}.",
            steps_en=[
                f"Miss area when Ali arrives too early: {m(f'\\frac{{1}}{{2}}({Lm - t1})^2')}; when Badr arrives too early: {m(f'\\frac{{1}}{{2}}({Lm - t2})^2')}.",
                f"Divide remaining area by {m(f'{Lm}^2')} to obtain {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Notice the probability lies strictly between the symmetric {m(str(t1))}-min and {m(str(t2))}-min answers: {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar=f"نطرح مساحتي المثلثين الركنيين {m(f'\\frac{{1}}{{2}}({Lm - t1})^2')} و{m(f'\\frac{{1}}{{2}}({Lm - t2})^2')} من مساحة المربع {m(f'{Lm}^2')}.",
            steps_ar=[
                f"مجموع مساحتي عدم اللقاء يساوي {m(f'\\frac{{({Lm - t1})^2 + ({Lm - t2})^2}}{{2}}')}.",
                f"بقسمة المساحة المتبقية على {m(f'{Lm}^2')} نحصل على {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"الكسر المختزل في أبسط صورة هو {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_stu_meeting_square(str(Lm), "?"),
        ))

    # Hard 23.1..23.5: Random point (x, y) in square [0, S]^2 satisfying x + y <= k or max/broken stick triangle!
    hard_geom_p = [
        # (S, k): P(x + y <= k) in [0, S]^2 for S < k < 2S is 1 - (2S - k)^2 / (2 S^2)
        (6, 8, "x + y \\le 8"),
        (8, 10, "x + y \\le 10"),
        (10, 14, "x + y \\le 14"),
        (6, 9, "x + y \\le 9"),
        (12, 16, "x + y \\le 16"),
    ]
    for idx_h, (S_sq, k_cut, cond_tex) in enumerate(hard_geom_p, 1):
        rem_leg = 2 * S_sq - k_cut
        ans = Fraction(2 * S_sq * S_sq - rem_leg * rem_leg, 2 * S_sq * S_sq)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=(
                f"In a 5-point Student Kangaroo geometric probability challenge (#{idx_h}), two real numbers {m('x')} and {m('y')} "
                f"are chosen independently and uniformly at random from the interval {m(f'[0, {S_sq}]')}. "
                f"What is the probability that {m(cond_tex)}?"
            ),
            q_ar=(
                f"في تحدي الاحتمال الهندسي من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h})، اُختير العددان الحقيقيان {m('x')} و{m('y')} "
                f"بشكل مستقل وعشوائي منتظم من الفترة {m(f'[0, {S_sq}]')}. ما احتمال تحقق المتباينة {m(cond_tex)}؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(k_cut, 2 * S_sq),
                Fraction(1, 1) - ans,
                Fraction(k_cut * k_cut, 2 * S_sq * S_sq) if k_cut * k_cut < 2 * S_sq * S_sq else Fraction(3, 4),
                min(Fraction(31, 32), ans + Fraction(1, 16)),
            ],
            hint_en=f"Since {m(f'{k_cut} > {S_sq}')}, the line {m(f'x + y = {k_cut}')} cuts off only a single upper-right triangle of leg {m(f'2({S_sq}) - {k_cut} = {rem_leg}')}!",
            hint_ar=f"بما أن {m(f'{k_cut} > {S_sq}')}، فإن المستقيم {m(f'x + y = {k_cut}')} يقتطع مثلثاً واحداً فقط في الركن العلوي الأيمن طول ضلعه {m(str(rem_leg))}!",
            idea_en=f"Compute the complement: the upper-right triangle where {m(f'x + y > {k_cut}')} has legs of length {m(f'{S_sq} - ({k_cut} - {S_sq}) = {rem_leg}')}.",
            steps_en=[
                f"In {m(f'[0, {S_sq}]^2')}, the line {m(f'x + y = {k_cut}')} meets the top and right sides at {m(f'({k_cut - S_sq}, {S_sq})')} and {m(f'({S_sq}, {k_cut - S_sq})')}.",
                f"Complement triangle area is {m(f'\\frac{{1}}{{2}} \\times {rem_leg}^2 = {Fraction(rem_leg*rem_leg, 2)}')}, so probability = {m(f'1 - \\frac{{{rem_leg}^2}}{{2 \\cdot {S_sq}^2}} = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Avoid the classic {m('k^2/(2S^2)')} trap (which exceeds {m('1')} when {m('k > S\\sqrt{2}')}): exact value is {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar=f"نحسب مساحة المتممة في الركن العلوي الأيمن حيث {m(f'x + y > {k_cut}')}.",
            steps_ar=[
                f"يتقاطع المستقيم {m(f'x + y = {k_cut}')} مع ضلعي المربع العلوي والأيمن مقتطعاً مثلثاً قائماً ضلعه {m(str(rem_leg))}.",
                f"إذن الاحتمال المطلوب يساوي {m(f'1 - \\frac{{{rem_leg}^2}}{{2 \\cdot {S_sq}^2}} = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"النتيجة تقع بين {m('1/2')} و{m('1')} كما هو متوقع هندسياً وتساوي {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_stu_meeting_square(str(S_sq), "?"),
        ))

    # ------------------------------------------------------------------
    # 24. kang_stu_random_walk_step_games (15 Qs: 5 Easy, 5 Medium, 5 Hard)
    # ------------------------------------------------------------------
    bp = "kang_stu_random_walk_step_games"

    # Easy 24.1..24.5: Symmetric 1D random walk hitting N before 0 starting at k -> P = k/N
    easy_rw = [
        (2, 6),
        (3, 8),
        (4, 10),
        (5, 12),
        (3, 10),
    ]
    for idx_e, (k0, N_top) in enumerate(easy_rw, 1):
        ans = Fraction(k0, N_top)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Easy", blueprint=bp,
            q_en=(
                f"On Student Kangaroo step-walk card #{idx_e}, a token starts at integer {m(str(k0))} on the segment "
                f"{m(f'0, 1, \\dots, {N_top}')}. Each turn a fair coin is flipped: Heads moves the token {m('+1')} and Tails moves it {m('-1')}. "
                f"The game ends as soon as the token reaches {m(str(N_top))} (win) or {m('0')} (lose). What is the probability of **winning**?"
            ),
            q_ar=(
                f"في بطاقة المسير العشوائي بمسابقة الكانجارو للمستوى المتقدم ({idx_e})، يبدأ قرص عند النقطة {m(str(k0))} على القطعة "
                f"{m(f'0, 1, \\dots, {N_top}')}. في كل خطوة تُرمى عملة عادلة فيتحرك القرص {m('+1')} أو {m('-1')} باحتمال متساوٍ، وتنتهي اللعبة فور وصوله إلى {m(str(N_top))} (فوز) أو {m('0')} (خسارة). ما احتمال **الفوز**؟"
            ),
            correct_val=ans,
            distractors=[
                Fraction(1, 2),
                Fraction(N_top - k0, N_top) if Fraction(N_top - k0, N_top) != ans else Fraction(k0 + 1, N_top),
                Fraction(k0, N_top + 1),
                Fraction(k0 * k0, N_top * N_top),
            ],
            hint_en=f"Since each step has zero average drift, {m('p_k = \\frac{1}{2}(p_{k-1} + p_{k+1})')} is linear with {m('p_0 = 0')} and {m(f'p_{{{N_top}}} = 1')}!",
            hint_ar=f"بما أن متوسط التغير في كل خطوة صفر، فإن {m('p_k = \\frac{1}{2}(p_{k-1} + p_{k+1})')} دالة خطية تحقق {m('p_0 = 0')} و{m(f'p_{{{N_top}}} = 1')}!",
            idea_en=f"Zero-drift fairness makes win probability proportional to initial position: {m(f'p_k = k / {N_top}')}.",
            steps_en=[
                f"From {m('p_k - p_{k-1} = p_{k+1} - p_k')}, {m('p_k')} increases in equal steps from {m('p_0 = 0')} to {m(f'p_{{{N_top}}} = 1')}.",
                f"At {m(f'k = {k0}')}, {m(f'p_{{{k0}}} = \\frac{{{k0}}}{{{N_top}}} = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Boundary check: {m('p_0 = 0')}, {m(f'p_{{{N_top/2 if N_top%2==0 else k0}}} = {ans.numerator}/{ans.denominator}')}, {m(f'p_{{{N_top}}} = 1')}.",
            idea_ar=f"تساوي احتمالي التقدم والتراجع يجعل احتمال الفوز خطياً: {m(f'p_k = k / {N_top}')}.",
            steps_ar=[
                f"العلاقة {m('p_k = \\frac{1}{2}(p_{k-1} + p_{k+1})')} تعني أن الفروق متساوية على طول القطعة.",
                f"إذن عند البداية من {m(str(k0))} يكون الاحتمال {m(f'{k0}/{N_top} = {ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"بالاختزال في أبسط صورة نحصل على {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=svg_number_strip(["0", "...", str(k0), "...", str(N_top)]),
        ))

    # Medium 24.1..24.5: Expected number of steps to hit 0 or N starting at k -> E_k = k(N - k)
    med_rw = [
        (2, 6),   # 8
        (3, 7),   # 12
        (3, 8),   # 15
        (4, 9),   # 20
        (5, 10),  # 25
    ]
    for idx_m, (k0, N_top) in enumerate(med_rw, 1):
        ans = k0 * (N_top - k0)
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Medium", blueprint=bp,
            q_en=(
                f"In Student Kangaroo step-duration puzzle #{idx_m}, a particle starts at {m(str(k0))} on {m(f'\\{{0, 1, \\dots, {N_top}\\}}')} "
                f"and moves {m('+1')} or {m('-1')} with probability {m('1/2')} each step until it hits either {m('0')} or {m(str(N_top))}. "
                f"What is the **expected number of steps** until the walk stops?"
            ),
            q_ar=(
                f"في مسألة زمن التوقف بمسابقة الكانجارو للمستوى المتقدم ({idx_m})، يبدأ جسيم عند الموقع {m(str(k0))} على المجموعة {m(f'\\{{0, 1, \\dots, {N_top}\\}}')} "
                f"ويتحرك {m('+1')} أو {m('-1')} باحتمال {m('1/2')} في كل خطوة حتى يصل إلى أحد الطرفين {m('0')} أو {m(str(N_top))}. "
                f"ما **القيمة المتوقعة لعدد الخطوات** حتى يتوقف؟"
            ),
            correct_val=ans,
            distractors=[N_top, k0 + (N_top - k0) * 2, ans + N_top, max(3, ans - k0)],
            hint_en=f"Solve the second-difference recurrence {m('E_k = 1 + \\frac{1}{2}(E_{k-1} + E_{k+1})')} with {m(f'E_0 = E_{{{N_top}}} = 0')}: try the quadratic {m(f'k({N_top} - k)')}!",
            hint_ar=f"حل المعادلة الفرقية {m('E_k = 1 + \\frac{1}{2}(E_{k-1} + E_{k+1})')} مع الشرطين {m(f'E_0 = E_{{{N_top}}} = 0')} باستخدام الصيغة التربيعية {m(f'k({N_top} - k)')}!",
            idea_en=f"Expected absorption time on {m('[0, N]')} from {m('k')} satisfies {m('E_k = k(N - k)')}.",
            steps_en=[
                f"Verify {m('1 + \\frac{1}{2}[(k-1)(N-k+1) + (k+1)(N-k-1)] = 1 + k(N-k) - 1 = k(N-k)')}.",
                f"Substituting {m(f'k = {k0}, N = {N_top}')} gives {m(f'{k0} \\times ({N_top} - {k0}) = {ans}')} steps.",
            ],
            check_en=f"At {m(f'k = {k0}')}: {m(f'1 + \\frac{{1}}{{2}}({(k0-1)*(N_top-k0+1)} + {(k0+1)*(N_top-k0-1)}) = {ans}')}. Exact!",
            idea_ar=f"متوسط عدد الخطوات للوصول إلى أحد الحاجزين {m('0')} أو {m('N')} يساوي {m('E_k = k(N - k)')}.",
            steps_ar=[
                f"الصيغة {m('E_k = k(N - k)')} تحقق {m('E_0 = E_N = 0')} ومعادلة الخطوة الواحدة {m('E_k = 1 + \\frac{1}{2}(E_{k-1} + E_{k+1})')}.",
                f"بالتعويض عن {m(f'k = {k0}')} و{m(f'N = {N_top}')} نحصل على {m(f'{k0} \\times {N_top - k0} = {ans}')} خطوة.",
            ],
            check_ar=f"التحقق المباشر عند {m(f'k = {k0}')} يعطي {m(str(ans))} تماماً.",
            diagram_en=svg_number_strip(["0", "...", str(k0), "...", str(N_top)]),
        ))

    # Hard 24.1..24.5: Return probability / polygon walk / best-of-series probability!
    hard_games = [
        # 1. Random walk on cycle C_n starting at 0: probability of hitting vertex k as the LAST visited vertex? Wait: uniform 1/(n-1)!
        # Let's make 5 rich distinct problems!
        (
            "On a regular hexagon, a frog starts at vertex A and hops to either adjacent vertex with probability 1/2 each jump. What is the probability that **vertex D (opposite A)** is the **very last** vertex visited for the first time?",
            "على مضلع سداسي منتظم، تبدأ ضفدعة عند الرأس A وتقفز في كل مرة إلى أحد الرأسين المجاورين باحتمال 1/2. ما احتمال أن يكون **الرأس المقابل D** هو **آخر رأس** تزوره الضفدعة لأول مرة؟",
            Fraction(1, 5),
            [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2), Fraction(2, 5)],
            "Before touching any vertex v ≠ A, the walk must visit both neighbors of v; by symmetry on an n-cycle, EVERY non-starting vertex has the exact same probability 1/(n - 1) of being visited last!",
            "كي يكون أي رأس v ≠ A هو الأخير، يجب أن تصل الضفدعة إلى جاريه من الجهتين أولاً، وهذا يعطي تماثلاً مذهلاً: احتمال كون أي رأس غير A هو الأخير يساوي 1/(n - 1) بالتساوي!",
            svg_regular_polygon(6, (), ["A", "B", "C", "D", "E", "F"]),
        ),
        (
            "On a regular octagon (8 vertices), a token starts at vertex V₁ and steps clockwise or counterclockwise with probability 1/2 each turn. What is the probability that neighbor **V₂** is the **very last** vertex of the octagon to be visited?",
            "على مثمن منتظم (٨ رؤوس)، يبدأ قرص عند الرأس V₁ ويتحرك مع أو عكس عقارب الساعة باحتمال 1/2 في كل خطوة. ما احتمال أن يكون الرأس المجاور **V₂** هو **آخر رأس** يزوره القرص على الإطلاق؟",
            Fraction(1, 7),
            [Fraction(1, 8), Fraction(1, 14), Fraction(1, 4), Fraction(2, 7)],
            "Unrolling the 8-cycle around V₂ gives the 7-edge segment V₂–V₁–V₈–V₇–V₆–V₅–V₄–V₃; V₂ is visited last iff the walk starting at V₁ reaches V₃ (distance 6) before V₂ (distance 1), giving probability 1/7.",
            "لكي يكون V₂ هو الأخير يجب الوصول إلى V₃ عبر الجهة الطويلة قبل لمس V₂، وعلى القطعة بطول ٧ من V₂ إلى V₃ يبعد V₁ مسافة ١ عن V₂ فيكون الاحتمال 1/7 بالضبط!",
            svg_regular_polygon(8, (), [f"V{i}" for i in range(1, 9)]),
        ),
        (
            "Nadia wins each point in a table-tennis match independently with probability 2/3. Leading 2–1 in a first-to-4-points game, what is the probability Nadia wins the game?",
            "تفوز نادية بكل نقطة في تنس الطاولة بشكل مستقل باحتمال 2/3. إذا كانت متقدمة بالنتيجة 2–1 في شوط يُحسم لمن يصل أولاً إلى 4 نقاط، فما احتمال فوز نادية بالشوط؟",
            Fraction(8, 9),
            [Fraction(2, 3), Fraction(20, 27), Fraction(64, 81), Fraction(7, 9)],
            "Play out all 4 remaining points (at most 4 points decide first-to-4 from 2–1): Nadia wins iff she wins at least 2 of the next 4 points!",
            "تخيّل لعب ٤ نقاط إضافية كاملة: تفوز نادية إذا وفقط إذا كسبت نقطتين على الأقل من النقاط الأربع القادمة!",
            svg_stu_probability_tree("2/3", "1/3", "2/3", "1/3", "2-1", "Lead"),
        ),
        (
            "A bug starts at one vertex of a cube and each second walks along a random edge (1/3 each) to an adjacent vertex. What is the probability it returns to its **starting vertex** on the **4th** step (possibly having visited it at step 2 as well)?",
            "تبدأ حشرة عند أحد رؤوس مكعب وفي كل ثانية تسير على حرف عشوائي (باحتمال 1/3 لكل حرف) إلى رأس مجاور. ما احتمال وجودها عند **رأس البداية** بعد الخطوة **الرابعة** تماماً؟",
            Fraction(7, 27),
            [Fraction(1, 9), Fraction(1, 3), Fraction(5, 27), Fraction(8, 27)],
            "Track distance d ∈ {0, 1, 2, 3} from the start vertex: at step 1, d=1 (prob 1); at step 2, d=0 (prob 1/3) or d=2 (prob 2/3)!",
            "تتبّع المسافة عن رأس البداية (0 أو 1 أو 2 أو 3 حروف) خطوة بخطوة حتى الثانية الرابعة!",
            svg_kang_cube_faces("S", "?", "?"),
        ),
        (
            "A biased step-walker moves +1 with probability 2/3 and −1 with probability 1/3 on {0, 1, 2, 3, 4}, starting at 1. What is the probability it reaches **4** before **0**?",
            "يتحرك متجول على المجموعة {0, 1, 2, 3, 4} بدءاً من 1 بخطوة +1 باحتمال 2/3 وخطوة −1 باحتمال 1/3. ما احتمال وصوله إلى **4** قبل **0**؟",
            Fraction(8, 15),
            [Fraction(1, 4), Fraction(2, 3), Fraction(7, 15), Fraction(9, 16)],
            "With odds ratio q/p = (1/3)/(2/3) = 1/2, Gambler's Ruin gives P = (1 - (1/2)^1) / (1 - (1/2)^4)!",
            "بنسبة الاحتمال q/p = 1/2 نطبق صيغة المسير غير المتماثل: (1 - (1/2)^1) / (1 - (1/2)^4)!",
            svg_number_strip(["0", "1", "2", "3", "4"]),
        ),
    ]
    # Programmatically verify all 5 Hard 24 answers before building!
    # 1 & 2: cycle last-visited theorem -> 1/(n-1)
    assert hard_games[0][2] == Fraction(1, 6 - 1)
    assert hard_games[1][2] == Fraction(1, 8 - 1)
    # 3: Nadia needs >= 2 wins in 4 trials with p = 2/3: sum_{j=2..4} C(4,j) (2/3)^j (1/3)^(4-j)
    p_nadia = sum(math.comb(4, j) * (Fraction(2, 3) ** j) * (Fraction(1, 3) ** (4 - j)) for j in (2, 3, 4))
    assert p_nadia == hard_games[2][2]
    # 4: Cube walk 4 steps return to 000 in {0,1}^3: flip 1 of 3 bits each step, return iff each bit flipped even times -> (0,0,4)x3 perms * 1 + (0,2,2)x3 perms * 4!/2!2! = 3*1 + 3*6 = 21 out of 81 = 7/27!
    cube_ret = sum(1 for seq in itertools.product((0, 1, 2), repeat=4) if all(seq.count(b) % 2 == 0 for b in (0, 1, 2)))
    assert Fraction(cube_ret, 81) == hard_games[3][2]
    # 5: Biased Gambler's Ruin r = 1/2: (1 - 1/2)/(1 - 1/16) = (1/2)/(15/16) = 8/15
    assert Fraction(1 - Fraction(1, 2), 1 - Fraction(1, 16)) == hard_games[4][2]

    for idx_h, (q_en, q_ar, ans, dists, idea_en, idea_ar, diag) in enumerate(hard_games, 1):
        items.append(make_kang_q(
            qid=_next_qid(items, offset), level=LEVEL, topic=topic, difficulty="Hard", blueprint=bp,
            q_en=f"In a 5-point Student Kangaroo step-walk challenge (#{idx_h}): {q_en}",
            q_ar=f"في تحدي المسير العشوائي من فئة ٥ نقاط بمسابقة الكانجارو للمستوى المتقدم ({idx_h}): {q_ar}",
            correct_val=ans,
            distractors=dists,
            hint_en="Use symmetry, coupled state equations, or fixed-horizon extension to compute the exact rational probability.",
            hint_ar="استخدم التماثل أو معادلات الحالات المتجاورة لحساب الاحتمال الكسري الدقيق.",
            idea_en=idea_en,
            steps_en=[
                "Set up the exact state-transition equations (or fixed-length binomial coupling).",
                f"Solving the linear boundary relations yields {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_en=f"Independent state-space enumeration confirms exact probability {m(f'{ans.numerator}/{ans.denominator}')}.",
            idea_ar=idea_ar,
            steps_ar=[
                "نكتب علاقات الانتقال بين الحالات مع شروط البداية والنهاية.",
                f"بحل العلاقات الجبرية نحصل على الاحتمال المختزل {m(f'{ans.numerator}/{ans.denominator}')}.",
            ],
            check_ar=f"الفحص الرياضي الدقيق يؤكد أن الاحتمال يساوي {m(f'{ans.numerator}/{ans.denominator}')}.",
            diagram_en=diag,
        ))

    return items


def build_student_bank() -> list[dict]:
    u1 = _unit_5_1_number_theory(0)
    u2 = _unit_5_2_algebra(60)
    u3 = _unit_5_3_geometry_plane(120)
    u4 = _unit_5_4_geometry_3d_lattice(180)
    u5 = _unit_5_5_combinatorics(240)
    u6 = _unit_5_6_data_probability(300)
    assert len(u1) == 60 and len(u2) == 60 and len(u3) == 60 and len(u4) == 60 and len(u5) == 60 and len(u6) == 60
    bank = u1 + u2 + u3 + u4 + u5 + u6
    assert len(bank) == 360
    return bank
