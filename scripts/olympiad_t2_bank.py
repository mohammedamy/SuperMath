"""Tier 2: Intermediate Olympiad (Grades 9-10) — 360 verified 5-option (A–E) questions (OLYM-T2-001..360)."""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

from olympiad_common import (
    OLYMPIAD_LEVELS,
    load_other_olympiad_stems,
    m,
    make_olym_bilingual_q,
    make_olym_q,
    norm_text,
    svg_angle_bisector_tri,
    svg_digit_slots,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_median_tri,
    svg_number_strip,
    svg_olym_bipartite_graph,
    svg_olym_board_coloring,
    svg_olym_cyclic_ptolemy,
    svg_olym_divisibility_lattice,
    svg_olym_func_mapping,
    svg_olym_incircle_excircle,
    svg_olym_inequality_curve,
    svg_olym_nine_point_euler,
    svg_olym_pigeonhole_boxes,
    svg_olym_radical_axis,
    svg_olym_spiral_homothety,
    svg_olym_tetrahedron_3d,
    svg_parabola_roots,
    svg_power_of_point,
    svg_right_tri_incircle,
    svg_stu_ceva_triangle,
    svg_stu_cone_frustum,
    svg_stu_dyck_grid,
    svg_stu_sphere_in_cylinder,
    svg_stu_tangent_circles,
)

LEVEL = OLYMPIAD_LEVELS[1]  # "Tier 2: Intermediate Olympiad (Grades 9-10)"


def _totient(n: int) -> int:
    res = n
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            while x % d == 0:
                x //= d
            res -= res // d
        d += 1
    if x > 1:
        res -= res // x
    return res


def _prime_factors(n: int) -> list[tuple[int, int]]:
    out = []
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            cnt = 0
            while x % d == 0:
                x //= d
                cnt += 1
            out.append((d, cnt))
        d += 1
    if x > 1:
        out.append((x, 1))
    return out


def _vp_fact(n: int, p: int) -> int:
    s = 0
    pw = p
    while pw <= n:
        s += n // pw
        pw *= p
    return s


# ==============================================================================
# UNIT 2.1 — Number Theory (OLYM-T2-001 .. OLYM-T2-060)
# ==============================================================================

def _gen_u21_number_theory() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 1: olym_t2_nt_fermat_euler_totient (OLYM-T2-001..015)
    # ------------------------------------------------------------------
    bp1 = "olym_t2_nt_fermat_euler_totient"

    # Easy (001..005): Euler's totient phi(n) on rich composites
    easy_tot_cases = [
        (360, "in an Intermediate Olympiad code lock"),
        (504, "on a circular Olympiad dial"),
        (720, "in a modular tournament seed table"),
        (900, "among numbered relay batons"),
        (1260, "in a harmonic divisibility screen"),
    ]
    for idx, (n, ctx_en) in enumerate(easy_tot_cases, 1):
        qid = f"OLYM-T2-{idx:03d}"
        ans = _totient(n)
        assert ans == sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)
        pfs = _prime_factors(n)
        pf_tex = " \\cdot ".join(f"{p}^{{{e}}}" if e > 1 else f"{p}" for p, e in pfs)
        prod_tex = "".join(f"\\left(1 - \\frac{{1}}{{{p}}}\\right)" for p, _ in pfs)
        q_en = (
            f"Used {ctx_en}, how many positive integers {m(f'k \\le {n}')} satisfy "
            f"{m(f'\\gcd(k, {n}) = 1')}?"
        )
        q_ar = (
            f"في مسألة أولمبياد المستوى المتوسط، كم عدداً صحيحاً موجباً {m(f'k \\le {n}')} يحقق الشرط "
            f"{m(f'\\gcd(k, {n}) = 1')}؟"
        )
        svg = svg_olym_divisibility_lattice(str(n), f"p={pfs[0][0]}", f"q={pfs[1][0]}", "φ = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Easy", bp1,
            q_en, q_ar, ans,
            [ans + 12, ans - 12, n // 2, ans + 24],
            f"Factor {m(str(n))} into primes and apply Euler's totient formula {m('\\varphi(n) = n \\prod_{p \\mid n}(1 - 1/p)')}.",
            f"حلّل العدد {m(str(n))} إلى عوامله الأولية وطبّق صيغة أويلر {m('\\varphi(n) = n \\prod_{p \\mid n}(1 - 1/p)')}.",
            "Count integers coprime to a composite modulus via Euler's multiplicative totient formula.",
            [
                f"Write the prime factorization: {m(f'{n} = {pf_tex}')}.",
                f"Apply Euler's formula: {m(f'\\varphi({n}) = {n}{prod_tex}')}.",
                f"Evaluating the product directly yields {m(f'\\varphi({n}) = {ans}')}.",
            ],
            f"Every prime factor of {m(str(n))} removes its exact fraction of multiples, leaving {m(str(ans))} coprime residues.",
            "نحسب عدد الأعداد الأولية نسبياً مع العدد المركب باستخدام دالة أويلر التضاعفية.",
            [
                f"نكتب التحليل إلى عوامل أولية: {m(f'{n} = {pf_tex}')}.",
                f"نطبق صيغة أويلر: {m(f'\\varphi({n}) = {n}{prod_tex}')}.",
                f"بحساب الجداء نحصل على {m(f'\\varphi({n}) = {ans}')}.",
            ],
            f"استبعاد مضاعفات العوامل الأولية يترك بالضبط {m(str(ans))} عدداً أولياً نسبياً مع {m(str(n))}.",
            diagram_en=svg,
        ))

    # Medium (006..010): Euler's theorem large-exponent modular remainders
    med_mod_cases = [
        (7, 2026, 25),
        (3, 2027, 40),
        (5, 1003, 49),
        (2, 1505, 63),
        (11, 3007, 72),
    ]
    for offset, (a, exp_e, mod_m) in enumerate(med_mod_cases, 6):
        qid = f"OLYM-T2-{offset:03d}"
        assert math.gcd(a, mod_m) == 1
        phi_m = _totient(mod_m)
        rem_e = exp_e % phi_m
        ans = pow(a, exp_e, mod_m)
        assert ans == pow(a, rem_e, mod_m)
        q_en = (
            f"In an Intermediate Olympiad modular arithmetic round, find the remainder when "
            f"{m(f'{a}^{{{exp_e}}}')} is divided by {m(str(mod_m))}."
        )
        q_ar = (
            f"في جولة الحساب المعياري للأولمبياد المتوسط، أوجد باقي قسمة "
            f"{m(f'{a}^{{{exp_e}}}')} على {m(str(mod_m))}."
        )
        svg = svg_function_machine(f"{a}^{exp_e}", f"φ={phi_m}", f"mod {mod_m}", "r = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Medium", bp1,
            q_en, q_ar, ans,
            [(ans + 2) % mod_m, (ans + 4) % mod_m, (ans * a) % mod_m, mod_m - ans if ans > 0 else 1],
            f"Since {m(f'\\gcd({a}, {mod_m}) = 1')}, reduce the exponent modulo {m(f'\\varphi({mod_m}) = {phi_m}')}.",
            f"بما أن {m(f'\\gcd({a}, {mod_m}) = 1')}، اختزل الأس معيارياً بالنسبة إلى {m(f'\\varphi({mod_m}) = {phi_m}')}.",
            "Euler's theorem states that coprime bases cycle modulo m with period dividing phi(m).",
            [
                f"Compute Euler's totient: {m(f'\\varphi({mod_m}) = {phi_m}')}, so {m(f'{a}^{{{phi_m}}} \\equiv 1 \\pmod{{{mod_m}}}')}.",
                f"Divide the exponent by {m(str(phi_m))}: {m(f'{exp_e} = {exp_e // phi_m} \\cdot {phi_m} + {rem_e}')}.",
                f"Reduce the remaining power: {m(f'{a}^{{{exp_e}}} \\equiv {a}^{{{rem_e}}} \\equiv {ans} \\pmod{{{mod_m}}}')}.",
            ],
            f"Notice {m(f'0 \\le {ans} < {mod_m}')} and {m(f'\\gcd({ans}, {mod_m}) = 1')}, matching a unit residue.",
            "تنص مبرهنة أويلر على أن القوى ذات الأساس الأولي نسبياً تتكرر بدور يقسم قيمة دالة أويلر.",
            [
                f"نحسب دالة أويلر: {m(f'\\varphi({mod_m}) = {phi_m}')}، ومنه {m(f'{a}^{{{phi_m}}} \\equiv 1 \\pmod{{{mod_m}}}')}.",
                f"نقسم الأس على {m(str(phi_m))}: {m(f'{exp_e} = {exp_e // phi_m} \\cdot {phi_m} + {rem_e}')}.",
                f"نحسب القوة المختزلة: {m(f'{a}^{{{exp_e}}} \\equiv {a}^{{{rem_e}}} \\equiv {ans} \\pmod{{{mod_m}}}')}.",
            ],
            f"الباقي {m(str(ans))} يحقق {m(f'0 \\le {ans} < {mod_m}')} وأولي نسبياً مع {m(str(mod_m))}.",
            diagram_en=svg,
        ))

    # Hard (011..015): Fermat's Little Theorem power-tower remainders a^(b^c) mod p
    hard_tower_cases = [
        (5, 3, 22, 13),
        (3, 5, 18, 17),
        (2, 7, 15, 19),
        (6, 5, 24, 23),
        (4, 9, 17, 29),
    ]
    for offset, (a, b, c, p) in enumerate(hard_tower_cases, 11):
        qid = f"OLYM-T2-{offset:03d}"
        exp_mod = pow(b, c, p - 1)
        ans = pow(a, exp_mod, p)
        assert ans == pow(a, b**c, p)
        q_en = (
            f"Determine the remainder when the power tower {m(f'{a}^{{{b}^{{{c}}}}}')} "
            f"is divided by the prime {m(str(p))}."
        )
        q_ar = (
            f"أوجد باقي قسمة البرج الأسي {m(f'{a}^{{{b}^{{{c}}}}}')} "
            f"على العدد الأولي {m(str(p))}."
        )
        svg = svg_digit_slots([f"a={a}", f"{b}^{c}", f"mod {p}", "r=?"], top_note="FLT Tower")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Hard", bp1,
            q_en, q_ar, ans,
            [(ans + 3) % p, (ans + 5) % p, p - ans, (ans * a) % p],
            f"By Fermat's Little Theorem, {m(f'{a}^{{{p - 1}}} \\equiv 1 \\pmod{{{p}}}')}, so first find {m(f'{b}^{{{c}}} \\bmod {p - 1}')}.",
            f"بموجب مبرهنة فيرما الصغرى {m(f'{a}^{{{p - 1}}} \\equiv 1 \\pmod{{{p}}}')}، لذا احسب أولاً {m(f'{b}^{{{c}}} \\bmod {p - 1}')}.",
            "Reduce the top exponent modulo p - 1 using Fermat's Little Theorem before reducing modulo p.",
            [
                f"Since {m(str(p))} is prime and {m(f'{p} \\nmid {a}')}, Fermat's Little Theorem gives {m(f'{a}^{{{p - 1}}} \\equiv 1 \\pmod{{{p}}}')}.",
                f"Compute the upper exponent modulo {m(str(p - 1))}: {m(f'{b}^{{{c}}} \\equiv {exp_mod} \\pmod{{{p - 1}}}')}.",
                f"Substitute back into the base power: {m(f'{a}^{{{b}^{{{c}}}}} \\equiv {a}^{{{exp_mod}}} \\equiv {ans} \\pmod{{{p}}}')}.",
            ],
            f"Exact modular reduction confirms {m(f'{a}^{{{exp_mod}}} \\bmod {p} = {ans}')}.",
            "نختزل الأس العلوي معيارياً بالنسبة إلى p - 1 باستعمال مبرهنة فيرما الصغرى ثم نحسب الباقي معيارياً بالنسبة إلى p.",
            [
                f"بما أن {m(str(p))} أولي ولا يقسم {m(str(a))}، فإن {m(f'{a}^{{{p - 1}}} \\equiv 1 \\pmod{{{p}}}')}.",
                f"نحسب الأس العلوي معيارياً بالنسبة إلى {m(str(p - 1))}: {m(f'{b}^{{{c}}} \\equiv {exp_mod} \\pmod{{{p - 1}}}')}.",
                f"نعوض في الأساس لنجد: {m(f'{a}^{{{b}^{{{c}}}}} \\equiv {a}^{{{exp_mod}}} \\equiv {ans} \\pmod{{{p}}}')}.",
            ],
            f"التحقق المباشر يؤكد أن {m(f'{a}^{{{exp_mod}}} \\bmod {p} = {ans}')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 2: olym_t2_nt_crt_simultaneous_mod (OLYM-T2-016..030)
    # ------------------------------------------------------------------
    bp2 = "olym_t2_nt_crt_simultaneous_mod"

    # Easy (016..020): Two-modulus CRT smallest positive integer
    crt_easy = [
        (7, 3, 11, 8),
        (8, 5, 13, 2),
        (9, 4, 14, 11),
        (11, 7, 15, 4),
        (12, 5, 17, 10),
    ]
    for offset, (m1, r1, m2, r2) in enumerate(crt_easy, 16):
        qid = f"OLYM-T2-{offset:03d}"
        lcm_val = math.lcm(m1, m2)
        cands = [n for n in range(1, lcm_val + 1) if n % m1 == r1 and n % m2 == r2]
        assert len(cands) == 1
        ans = cands[0]
        k_val = (ans - r2) // m2
        q_en = (
            f"Find the smallest positive integer {m('N')} that leaves remainder {m(str(r1))} "
            f"when divided by {m(str(m1))} and remainder {m(str(r2))} when divided by {m(str(m2))}."
        )
        q_ar = (
            f"أوجد أصغر عدد صحيح موجب {m('N')} يترك باقياً قدره {m(str(r1))} عند قسمته على {m(str(m1))} "
            f"وباقياً قدره {m(str(r2))} عند قسمته على {m(str(m2))}."
        )
        svg = svg_olym_pigeonhole_boxes(3, f"mod {m1},{m2}", "N = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Easy", bp2,
            q_en, q_ar, ans,
            [ans + m1, ans + m2, lcm_val - ans if lcm_val - ans != ans else ans + lcm_val, ans - m1 if ans > m1 else ans + 2 * m1],
            f"Write {m(f'N = {m2}k + {r2}')} and test {m(f'{m2}k + {r2} \\equiv {r1} \\pmod{{{m1}}}')}.",
            f"اكتب {m(f'N = {m2}k + {r2}')} وحل التطابق {m(f'{m2}k + {r2} \\equiv {r1} \\pmod{{{m1}}}')}.",
            "Parametrize the larger modulus and solve the resulting linear congruence modulo the smaller modulus.",
            [
                f"Express {m('N')} using modulus {m(str(m2))}: {m(f'N = {m2}k + {r2}')} for an integer {m('k \\ge 0')}.",
                f"Substitute into the first congruence: {m(f'{m2}k + {r2} \\equiv {r1} \\pmod{{{m1}}}')}, which gives smallest {m(f'k = {k_val}')}.",
                f"Compute {m(f'N = {m2} \\cdot {k_val} + {r2} = {ans}')}, unique modulo {m(f'{m1} \\cdot {m2} = {lcm_val}')}.",
            ],
            f"Check: {m(f'{ans} = {ans // m1} \\cdot {m1} + {ans % m1}')} and {m(f'{ans} = {ans // m2} \\cdot {m2} + {ans % m2}')}.",
            "نكتب العدد بدلالة المعيار الأكبر ثم نحل التطابق الخطي بالنسبة إلى المعيار الأصغر.",
            [
                f"نضع {m(f'N = {m2}k + {r2}')} لعدد صحيح {m('k \\ge 0')}.",
                f"بالتعويض في التطابق الأول: {m(f'{m2}k + {r2} \\equiv {r1} \\pmod{{{m1}}}')}، وأصغر حل غير سالب هو {m(f'k = {k_val}')}.",
                f"إذن {m(f'N = {m2} \\cdot {k_val} + {r2} = {ans}')} وهو وحيد معيارياً بالنسبة إلى {m(str(lcm_val))}.",
            ],
            f"التحقق: باقي قسمة {m(str(ans))} على {m(str(m1))} هو {m(str(r1))} وعلى {m(str(m2))} هو {m(str(r2))}.",
            diagram_en=svg,
        ))

    # Medium (021..025): Three-modulus pairwise-coprime CRT
    crt_med = [
        (3, 2, 5, 3, 7, 4),
        (4, 1, 5, 4, 9, 7),
        (3, 1, 7, 5, 11, 2),
        (5, 2, 7, 3, 8, 5),
        (4, 3, 7, 2, 9, 5),
    ]
    for offset, (m1, r1, m2, r2, m3, r3) in enumerate(crt_med, 21):
        qid = f"OLYM-T2-{offset:03d}"
        M = m1 * m2 * m3
        cands = [n for n in range(1, M + 1) if n % m1 == r1 and n % m2 == r2 and n % m3 == r3]
        assert len(cands) == 1
        ans = cands[0]
        m23 = m2 * m3
        r23 = [x for x in range(m23) if x % m2 == r2 and x % m3 == r3][0]
        q_en = (
            f"In an Intermediate Olympiad synchronization puzzle, find the least positive integer {m('N')} "
            f"satisfying {m(f'N \\equiv {r1} \\pmod{{{m1}}}')}, {m(f'N \\equiv {r2} \\pmod{{{m2}}}')}, "
            f"and {m(f'N \\equiv {r3} \\pmod{{{m3}}}')}."
        )
        q_ar = (
            f"في مسألة تزامن للأولمبياد المتوسط، أوجد أصغر عدد صحيح موجب {m('N')} يحقق "
            f"{m(f'N \\equiv {r1} \\pmod{{{m1}}}')} و{m(f'N \\equiv {r2} \\pmod{{{m2}}}')} "
            f"و{m(f'N \\equiv {r3} \\pmod{{{m3}}}')}."
        )
        svg = svg_digit_slots([f"mod {m1}", f"mod {m2}", f"mod {m3}", "N=?"], top_note="CRT-3")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Medium", bp2,
            q_en, q_ar, ans,
            [ans + m23 if ans + m23 < M else abs(ans - m23), ans + m1 * m2, M - ans, r23 if r23 != ans else ans + M],
            f"First combine the last two congruences modulo {m(f'{m2} \\cdot {m3} = {m23}')}, then impose {m(f'\\bmod\\ {m1}')}.",
            f"ادمج أولاً التطابقين الأخيرين معيارياً بالنسبة إلى {m(f'{m2} \\cdot {m3} = {m23}')} ثم طبّق التطابق معيار {m(str(m1))}.",
            "Merge congruences pairwise via the Chinese Remainder Theorem.",
            [
                f"Combine {m(f'N \\equiv {r2} \\pmod{{{m2}}}')} and {m(f'N \\equiv {r3} \\pmod{{{m3}}}')} to get {m(f'N \\equiv {r23} \\pmod{{{m23}}}')}.",
                f"Write {m(f'N = {m23}t + {r23}')} and solve {m(f'{m23}t + {r23} \\equiv {r1} \\pmod{{{m1}}}')}.",
                f"The smallest non-negative integer {m(f't = {(ans - r23) // m23}')} yields {m(f'N = {ans}')} modulo {m(str(M))}.",
            ],
            f"Verify all three remainders: {m(f'{ans} \\bmod {m1} = {r1}')}, {m(f'{ans} \\bmod {m2} = {r2}')}, and {m(f'{ans} \\bmod {m3} = {r3}')}.",
            "ندمج التطابقات مثنى مثنى باستخدام مبرهنة الباقي الصينية.",
            [
                f"بدمج التطابقين معيار {m(str(m2))} ومعيار {m(str(m3))} نجد {m(f'N \\equiv {r23} \\pmod{{{m23}}}')}.",
                f"نضع {m(f'N = {m23}t + {r23}')} ونحل {m(f'{m23}t + {r23} \\equiv {r1} \\pmod{{{m1}}}')}.",
                f"أصغر قيمة غير سالبة هي {m(f't = {(ans - r23) // m23}')} فتعطي {m(f'N = {ans}')}.",
            ],
            f"التحقق من البواقي الثلاثة يؤكد تطابق {m(str(ans))} مع الشروط كافة.",
            diagram_en=svg,
        ))

    # Hard (026..030): Non-coprime simultaneous congruences on bounded intervals
    crt_hard = [
        (6, 5, 10, 9, 14, 13, 1000),
        (8, 3, 12, 7, 15, 7, 999),
        (9, 4, 12, 7, 10, 9, 1000),
        (6, 1, 15, 10, 8, 5, 900),
        (10, 7, 15, 2, 12, 11, 950),
    ]
    for offset, (m1, r1, m2, r2, m3, r3, bound) in enumerate(crt_hard, 26):
        qid = f"OLYM-T2-{offset:03d}"
        L = math.lcm(m1, m2, m3)
        valid = [n for n in range(1, bound + 1) if n % m1 == r1 and n % m2 == r2 and n % m3 == r3]
        assert len(valid) >= 1
        ans = max(valid)
        base_r = valid[0] % L
        q_en = (
            f"Find the greatest positive integer {m(f'N \\le {bound}')} satisfying the non-coprime system "
            f"{m(f'N \\equiv {r1} \\pmod{{{m1}}}')}, {m(f'N \\equiv {r2} \\pmod{{{m2}}}')}, and {m(f'N \\equiv {r3} \\pmod{{{m3}}}')}."
        )
        q_ar = (
            f"أوجد أكبر عدد صحيح موجب {m(f'N \\le {bound}')} يحقق جملة التطابقات غير الأولية نسبياً: "
            f"{m(f'N \\equiv {r1} \\pmod{{{m1}}}')} و{m(f'N \\equiv {r2} \\pmod{{{m2}}}')} و{m(f'N \\equiv {r3} \\pmod{{{m3}}}')}."
        )
        svg = svg_olym_divisibility_lattice(f"L={L}", f"m={m1}", f"n={m2}", "N = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Hard", bp2,
            q_en, q_ar, ans,
            [ans - L if ans > L else ans + 30, base_r if base_r != ans else ans - 60, bound - (bound % L), ans - m3],
            f"Compatibility holds on shared GCDs, so solutions repeat modulo {m(f'\\operatorname{{lcm}}({m1}, {m2}, {m3}) = {L}')}.",
            f"الشروط متوافقة على القواسم المشتركة، لذا تتكرر الحلول كل دور قدره {m(f'\\operatorname{{lcm}}({m1}, {m2}, {m3}) = {L}')}.",
            "Resolve prime-power congruences and step up by the least common multiple up to the bound.",
            [
                f"Compute the combined period {m(f'L = \\operatorname{{lcm}}({m1}, {m2}, {m3}) = {L}')}.",
                f"Splitting into prime-power moduli gives the unique residue class {m(f'N \\equiv {base_r} \\pmod{{{L}}}')}.",
                f"Choosing the largest multiple of {m(str(L))} plus {m(str(base_r))} not exceeding {m(str(bound))} gives {m(f'N = {ans}')}.",
            ],
            f"Adding {m(str(L))} gives {m(str(ans + L))}, which exceeds {m(str(bound))}, while {m(str(ans))} satisfies every congruence.",
            "نحلل التطابقات إلى قوى الأعداد الأولية ثم نتحرك بمضاعفات المضاعف المشترك الأصغر حتى السقف المعطى.",
            [
                f"نحسب الدور المشترك {m(f'L = \\operatorname{{lcm}}({m1}, {m2}, {m3}) = {L}')}.",
                f"بتوحيد التطابقات نحصل على الصنف الوحيد {m(f'N \\equiv {base_r} \\pmod{{{L}}}')}.",
                f"أكبر عدد من هذا الصنف لا يتجاوز {m(str(bound))} هو {m(f'N = {ans}')}.",
            ],
            f"إضافة {m(str(L))} تعطي {m(str(ans + L))} وهو أكبر من {m(str(bound))}، بينما {m(str(ans))} يحقق التطابقات الثلاثة.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 3: olym_t2_nt_legendre_padic_fact (OLYM-T2-031..045)
    # ------------------------------------------------------------------
    bp3 = "olym_t2_nt_legendre_padic_fact"

    # Easy (031..035): Legendre's formula v_p(n!)
    leg_easy = [
        (50, 3),
        (85, 5),
        (128, 3),
        (160, 7),
        (250, 11),
    ]
    for offset, (n, p) in enumerate(leg_easy, 31):
        qid = f"OLYM-T2-{offset:03d}"
        ans = _vp_fact(n, p)
        fn = math.factorial(n)
        assert fn % (p**ans) == 0 and fn % (p ** (ans + 1)) != 0
        terms = []
        pw = p
        while pw <= n:
            terms.append(n // pw)
            pw *= p
        sum_tex = " + ".join(str(t) for t in terms)
        q_en = (
            f"Find the greatest integer {m('k')} such that {m(f'{p}^k')} divides {m(f'{n}!')}"
            f" without remainder."
        )
        q_ar = (
            f"أوجد أكبر عدد صحيح {m('k')} بحيث يقسم {m(f'{p}^k')} المضروب {m(f'{n}!')}"
            f" دون باقٍ."
        )
        svg = svg_number_strip([f"{n}!", f"p={p}", "k = ?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Easy", bp3,
            q_en, q_ar, ans,
            [terms[0], ans - 1, ans + 1, ans + 3],
            f"Apply Legendre's formula {m(f'v_{{{p}}}({n}!) = \\sum_{{j \\ge 1}} \\lfloor {n} / {p}^j \\rfloor')}.",
            f"طبّق صيغة ليجاندر {m(f'v_{{{p}}}({n}!) = \\sum_{{j \\ge 1}} \\lfloor {n} / {p}^j \\rfloor')}.",
            "Sum the floor quotients by successive powers of the prime p.",
            [
                f"By Legendre's formula, {m(f'v_{{{p}}}({n}!) = \\lfloor {n}/{p} \\rfloor + \\lfloor {n}/{p}^2 \\rfloor + \\cdots')}.",
                f"Evaluating the non-zero floor terms gives {m(f'{sum_tex}')}.",
                f"Adding them yields {m(f'k = {ans}')}.",
            ],
            f"Multiples of higher powers of {m(str(p))} exceed {m(str(n))}, contributing {m('0')}.",
            "نجمع خارج القسمة الصحيح على القوى المتتالية للعدد الأولي p.",
            [
                f"بموجب صيغة ليجاندر: {m(f'v_{{{p}}}({n}!) = \\lfloor {n}/{p} \\rfloor + \\lfloor {n}/{p}^2 \\rfloor + \\cdots')}.",
                f"بحساب الحدود غير الصفرية نحصل على: {m(f'{sum_tex}')}.",
                f"المجموع يساوي {m(f'k = {ans}')}.",
            ],
            f"القوى الأعلى للعدد {m(str(p))} تتجاوز {m(str(n))} فتساهم بقيمة {m('0')}.",
            diagram_en=svg,
        ))

    # Medium (036..040): Trailing zeros of n! in composite base B
    leg_med = [
        (100, 12),
        (140, 15),
        (90, 18),
        (125, 24),
        (150, 45),
    ]
    for offset, (n, B) in enumerate(leg_med, 36):
        qid = f"OLYM-T2-{offset:03d}"
        pfs = _prime_factors(B)
        ans = min(_vp_fact(n, p) // e for p, e in pfs)
        fn = math.factorial(n)
        assert fn % (B**ans) == 0 and fn % (B ** (ans + 1)) != 0
        pf_tex = " \\cdot ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in pfs)
        quot_tex = ",\\; ".join(f"\\lfloor v_{{{p}}}({n}!)/{e} \\rfloor = {_vp_fact(n, p) // e}" for p, e in pfs)
        q_en = (
            f"When {m(f'{n}!')} is written in base {m(str(B))}, how many consecutive zeros "
            f"appear at the right end of its representation?"
        )
        q_ar = (
            f"عند كتابة العدد {m(f'{n}!')} في نظام العد ذي الأساس {m(str(B))}، كم صفراً متتالياً "
            f"يظهر في أقصى يمين التمثيل؟"
        )
        svg = svg_function_machine(f"{n}!", f"base {B}", "min v_p", "z = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Medium", bp3,
            q_en, q_ar, ans,
            [max(_vp_fact(n, p) // e for p, e in pfs), ans + 2, ans - 2, _vp_fact(n, pfs[-1][0])],
            f"Factor the base {m(f'{B} = {pf_tex}')} and compute {m('\\min_{p^e \\parallel B} \\lfloor v_p(n!)/e \\rfloor')}.",
            f"حلّل الأساس {m(f'{B} = {pf_tex}')} واحسب {m('\\min_{p^e \\parallel B} \\lfloor v_p(n!)/e \\rfloor')}.",
            "Trailing zeros in base B equal the highest power of B dividing n!, controlled by the bottleneck prime factor.",
            [
                f"Prime-factor the base: {m(f'{B} = {pf_tex}')}.",
                f"Compute Legendre valuations and divide by exponents: {m(quot_tex)}.",
                f"Taking the minimum gives {m(f'z = {ans}')} trailing zeros in base {m(str(B))}.",
            ],
            f"The limiting prime factor restricts complete powers of {m(str(B))} to exactly {m(str(ans))}.",
            "عدد الأصفار الطرفية في الأساس B يساوي أكبر أس للعدد B يقسم n!، ويحدده العامل الأولي الأضيق.",
            [
                f"نحلل الأساس إلى عوامله الأولية: {m(f'{B} = {pf_tex}')}.",
                f"نحسب أسس العوامل الأولية ونقسم على أس كل عامل: {m(quot_tex)}.",
                f"بأخذ القيمة الصغرى نجد أن عدد الأصفار الطرفية هو {m(f'z = {ans}')}.",
            ],
            f"العامل الأولي المحدِّد يمنع تكوّن قوة أعلى للعدد {m(str(B))} فوق الأس {m(str(ans))}.",
            diagram_en=svg,
        ))

    # Hard (041..045): Inverse Legendre threshold & Kummer's theorem on binomials
    # 041..043: Smallest positive integer n with v_p(n!) >= target
    inv_leg_cases = [
        (5, 31, "base 10"),
        (3, 40, "divisibility by 3^40"),
        (7, 19, "divisibility by 7^19"),
    ]
    for idx_sub, (p, target_e, tag_en) in enumerate(inv_leg_cases):
        offset = 41 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = next(n for n in range(1, 2000) if _vp_fact(n, p) >= target_e)
        assert _vp_fact(ans - 1, p) < target_e <= _vp_fact(ans, p)
        q_en = (
            f"In an Intermediate Olympiad factorial threshold problem ({tag_en}), find the smallest "
            f"positive integer {m('n')} such that {m(f'{p}^{{{target_e}}}')} divides {m('n!')}."
        )
        q_ar = (
            f"في مسألة عتبات المضروب للأولمبياد المتوسط، أوجد أصغر عدد صحيح موجب {m('n')} "
            f"بحيث يقسم {m(f'{p}^{{{target_e}}}')} العدد {m('n!') }."
        )
        svg = svg_digit_slots([f"p={p}", f"e={target_e}", "n = ?"], top_note="Inv Leg")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Hard", bp3,
            q_en, q_ar, ans,
            [ans - p, ans + p, target_e * (p - 1), ans - 1],
            f"Use the bound {m('v_p(n!) = (n - s_p(n))/(p - 1)')}, so {m(f'n \\approx {p - 1} \\cdot {target_e}')}, then test nearby multiples of {m(str(p))}.",
            f"استخدم المتطابقة {m('v_p(n!) = (n - s_p(n))/(p - 1)')} فتكون {m(f'n \\approx {p - 1} \\cdot {target_e}')} ثم اختبر مضاعفات {m(str(p))} القريبة.",
            "Estimate n via Legendre's base-p digit-sum identity and verify the exact jump at multiples of p.",
            [
                f"Recall {m('v_p(n!) = \\frac{n - s_p(n)}{p - 1}')}, implying {m(f'n > {p - 1} \\cdot {target_e} = {(p - 1) * target_e}')}.",
                f"Testing multiples of {m(str(p))}: {m(f'v_{{{p}}}({ans - p}!) = {_vp_fact(ans - p, p)} < {target_e}')}, whereas {m(f'v_{{{p}}}({ans}!) = {_vp_fact(ans, p)} \\ge {target_e}')}.",
                f"Since {m('v_p(n!)')} only increases at multiples of {m(str(p))}, the minimal integer is {m(f'n = {ans}')}.",
            ],
            f"Checking {m(f'n = {ans - 1}')} gives {m(f'v_{{{p}}}({ans - 1}!) = {_vp_fact(ans - 1, p)} < {target_e}')}, confirming minimality.",
            "نقدّر قيمة n من متطابقة مجموع الأرقام في الأساس p ثم نتحقق من القفزة الدقيقة عند مضاعفات p.",
            [
                f"من المتطابقة {m('v_p(n!) = \\frac{n - s_p(n)}{p - 1}')} نستنتج أن {m(f'n > {(p - 1) * target_e}')}.",
                f"بفحص مضاعفات {m(str(p))}: نجد {m(f'v_{{{p}}}({ans - p}!) = {_vp_fact(ans - p, p)}')} بينما {m(f'v_{{{p}}}({ans}!) = {_vp_fact(ans, p)} \\ge {target_e}')}.",
                f"بما أن الأس لا يزداد إلا عند مضاعفات {m(str(p))}، فإن أصغر قيمة هي {m(f'n = {ans}')}.",
            ],
            f"عند {m(f'n = {ans - 1}')} يكون الأس {m(str(_vp_fact(ans - 1, p)))} وهو أصغر من {m(str(target_e))}.",
            diagram_en=svg,
        ))

    # 044..045: Kummer's theorem v_p(C(a+b, a))
    kummer_cases = [
        (2, 1000, 512),  # v_2(C(1000, 512)) -> carries when adding 512 + 488 = 1000 in base 2
        (3, 729, 250),   # v_3(C(729, 250)) -> carries when adding 250 + 479 = 729 in base 3
    ]
    for idx_sub, (p, m_top, r_bot) in enumerate(kummer_cases):
        offset = 44 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = _vp_fact(m_top, p) - _vp_fact(r_bot, p) - _vp_fact(m_top - r_bot, p)
        c_val = math.comb(m_top, r_bot)
        assert c_val % (p**ans) == 0 and c_val % (p ** (ans + 1)) != 0
        b_comp = m_top - r_bot
        q_en = (
            f"Find the exponent of the highest power of {m(str(p))} that divides the binomial "
            f"coefficient {m(f'\\binom{{{m_top}}}{{{r_bot}}}')}."
        )
        q_ar = (
            f"أوجد أسّ أكبر قوة للعدد الأولي {m(str(p))} تقسم المعامل الثنائي "
            f"{m(f'\\binom{{{m_top}}}{{{r_bot}}}')}."
        )
        svg = svg_digit_slots([f"C({m_top}", f"{r_bot})", f"p={p}", "v_p=?"], top_note="Kummer")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Hard", bp3,
            q_en, q_ar, ans,
            [ans - 1, ans + 1, ans + 2, max(1, ans - 2)],
            f"By Kummer's theorem, {m(f'v_{{{p}}}\\binom{{{m_top}}}{{{r_bot}}}')} equals the number of carries when adding {m(str(r_bot))} and {m(str(b_comp))} in base {m(str(p))}.",
            f"بموجب مبرهنة كومر، تساوي {m(f'v_{{{p}}}\\binom{{{m_top}}}{{{r_bot}}}')} عدد عمليات الحمل عند جمع {m(str(r_bot))} و{m(str(b_comp))} في الأساس {m(str(p))}.",
            "Apply Kummer's carry theorem or subtract Legendre valuations of the numerator and denominator factorials.",
            [
                f"Write {m(f'v_{{{p}}}\\binom{{{m_top}}}{{{r_bot}}} = v_{{{p}}}({m_top}!) - v_{{{p}}}({r_bot}!) - v_{{{p}}}({b_comp}!)')}.",
                f"Compute each factorial valuation: {m(f'{_vp_fact(m_top, p)} - {_vp_fact(r_bot, p)} - {_vp_fact(b_comp, p)}')}.",
                f"Equivalently, counting base-{m(str(p))} carries when adding {m(f'{r_bot} + {b_comp} = {m_top}')} gives {m(str(ans))}.",
            ],
            f"Both Legendre subtraction and Kummer's base-{m(str(p))} carry count agree on {m(str(ans))}.",
            "نطبق مبرهنة كومر لحساب عدد عمليات الحمل أو نطرح تقييمات ليجاندر للبسط والمقام.",
            [
                f"نكتب {m(f'v_{{{p}}}\\binom{{{m_top}}}{{{r_bot}}} = v_{{{p}}}({m_top}!) - v_{{{p}}}({r_bot}!) - v_{{{p}}}({b_comp}!)')}.",
                f"بحساب التقييمات الثلاثة نجد: {m(f'{_vp_fact(m_top, p)} - {_vp_fact(r_bot, p)} - {_vp_fact(b_comp, p)} = {ans}')}.",
                f"وبالمثل فإن عدد عمليات الحمل في الأساس {m(str(p))} عند جمع {m(f'{r_bot} + {b_comp}')} يساوي {m(str(ans))}.",
            ],
            f"تتطابق نتيجة طرح صيغة ليجاندر مع عدّ عمليات الحمل في مبرهنة كومر وتساوي {m(str(ans))}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 4: olym_t2_nt_pell_pythagorean_dioph (OLYM-T2-046..060)
    # ------------------------------------------------------------------
    bp4 = "olym_t2_nt_pell_pythagorean_dioph"

    # Easy (046..050): Counting positive integer pairs (x, y) with x^2 - y^2 = N
    diff_sq_cases = [105, 144, 180, 225, 315]
    for offset, N in enumerate(diff_sq_cases, 46):
        qid = f"OLYM-T2-{offset:03d}"
        pairs = []
        for u in range(1, int(math.isqrt(N)) + 1):
            if N % u == 0:
                v = N // u
                if u < v and (u + v) % 2 == 0:
                    pairs.append(((v + u) // 2, (v - u) // 2))
        ans = len(pairs)
        assert all(x > 0 and y > 0 and x * x - y * y == N for x, y in pairs)
        q_en = (
            f"How many ordered pairs of positive integers {m('(x, y)')} satisfy the Diophantine "
            f"equation {m(f'x^2 - y^2 = {N}')}?"
        )
        q_ar = (
            f"كم زوجاً مرتباً من الأعداد الصحيحة الموجبة {m('(x, y)')} يحقق المعادلة الديوفانتية "
            f"{m(f'x^2 - y^2 = {N}')}؟"
        )
        svg = svg_olym_divisibility_lattice(str(N), "x − y", "x + y", "# = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Easy", bp4,
            q_en, q_ar, ans,
            [ans + 1, ans + 2, max(1, ans - 1), ans * 2],
            f"Factor {m(f'(x - y)(x + y) = {N}')} into divisor pairs {m('u < v')} of the same parity.",
            f"حلّل المعادلة إلى {m(f'(x - y)(x + y) = {N}')} وابحث عن أزواج القواسم {m('u < v')} المتفقة في الزوجية.",
            "Each same-parity factor pair u < v with uv = N yields a unique positive solution x = (v+u)/2, y = (v-u)/2.",
            [
                f"Factor {m(f'x^2 - y^2 = (x - y)(x + y) = {N}')} with {m('u = x - y < v = x + y')}.",
                f"For {m('x, y')} to be positive integers, {m('u')} and {m('v')} must share the same parity and satisfy {m('u < v')}.",
                f"Counting all valid same-parity divisor pairs of {m(str(N))} gives exactly {m(str(ans))} solutions.",
            ],
            f"Explicit solutions have {m('x - y \\in \\{' + ', '.join(str((x - y)) for x, y in pairs) + '\\}')}, totaling {m(str(ans))} pairs.",
            "كل زوج قواسم u < v لهما نفس الزوجية وحاصل ضربهما N يعطي حلاً موجباً وحيداً.",
            [
                f"نحلل الطرف الأيسر: {m(f'(x - y)(x + y) = {N}')} بوضع {m('u = x - y < v = x + y')}.",
                f"لكي يكون {m('x, y')} عددين صحيحين موجبين يجب أن يتفق {m('u, v')} في الزوجية مع {m('u < v')}.",
                f"بحصر أزواج القواسم المتفقة في الزوجية للعدد {m(str(N))} نجد {m(str(ans))} حلول بالضبط.",
            ],
            f"قيم {m('x - y')} المقبولة عددها {m(str(ans))}، وكل منها يعطي زوجاً موجباً وحيداً.",
            diagram_en=svg,
        ))

    # Medium (051..055): Maximum perimeter of an integer-sided right triangle with given leg a
    pyth_leg_cases = [15, 20, 21, 28, 33]
    for offset, leg_a in enumerate(pyth_leg_cases, 51):
        qid = f"OLYM-T2-{offset:03d}"
        a2 = leg_a * leg_a
        perims = []
        for u in range(1, leg_a):
            if a2 % u == 0:
                v = a2 // u
                if (u + v) % 2 == 0 and v > u:
                    c = (v + u) // 2
                    b = (v - u) // 2
                    perims.append(leg_a + b + c)
        ans = max(perims)
        max_u = 1 if leg_a % 2 == 1 else 2
        max_v = a2 // max_u
        max_b = (max_v - max_u) // 2
        max_c = (max_v + max_u) // 2
        assert leg_a + max_b + max_c == ans and leg_a**2 + max_b**2 == max_c**2
        q_en = (
            f"A right triangle has integer side lengths and one leg of length {m(str(leg_a))}. "
            f"What is the maximum possible perimeter of this triangle?"
        )
        q_ar = (
            f"مثلث قائم الزاوية أطوال أضلاعه أعداد صحيحة وطول أحد ضلعيه القائمين {m(str(leg_a))}. "
            f"ما أكبر محيط ممكن لهذا المثلث؟"
        )
        svg = svg_right_tri_incircle(str(leg_a), "b", "c", "P=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Medium", bp4,
            q_en, q_ar, ans,
            [max_c + max_b, ans - leg_a, ans - 2, max_c * 2],
            f"Write {m(f'c^2 - b^2 = {leg_a}^2 = {a2}')}, so {m('(c - b)(c + b)')} is maximized when {m('c - b')} is as small as parity allows.",
            f"اكتب {m(f'(c - b)(c + b) = {leg_a}^2 = {a2}')}، فيكون {m('c + b')} أكبر ما يمكن عندما نختار أصغر قيمة ممكنة للفرق {m('c - b')}.",
            "Perimeter a + b + c is maximized by choosing the smallest valid divisor u = c - b of a^2 with the same parity as a^2/u.",
            [
                f"By the Pythagorean theorem, {m(f'(c - b)(c + b) = {leg_a}^2 = {a2}')}.",
                f"Since the perimeter equals {m(f'{leg_a} + (b + c)')}, we maximize {m('b + c')} by taking the smallest same-parity divisor {m(f'c - b = {max_u}')}.",
                f"Then {m(f'c + b = {a2} / {max_u} = {max_v}')}, giving maximum perimeter {m(f'{leg_a} + {max_v} = {ans}')}.",
            ],
            f"The optimal triple is {m(f'({leg_a}, {max_b}, {max_c})')}, satisfying {m(f'{leg_a}^2 + {max_b}^2 = {max_c}^2')}.",
            "يتعاظم المحيط a + b + c باختيار أصغر قاسم u = c - b للعدد a^2 يتفق في الزوجية مع مرافقه.",
            [
                f"من مبرهنة فيثاغورس: {m(f'(c - b)(c + b) = {leg_a}^2 = {a2}')}.",
                f"لتعظيم {m(f'{leg_a} + (b + c)')} نأخذ أصغر قاسم يحفظ الزوجية وهو {m(f'c - b = {max_u}')}.",
                f"ومنه {m(f'c + b = {max_v}')}، فيكون أكبر محيط ممكن {m(f'{leg_a} + {max_v} = {ans}')}.",
            ],
            f"الثلاثية المثلى هي {m(f'({leg_a}, {max_b}, {max_c})')} وتحقق {m(f'{leg_a}^2 + {max_b}^2 = {max_c}^2')}.",
            diagram_en=svg,
        ))

    # Hard (056..060): Pell's equation x^2 - d y^2 = 1 higher solutions via Brahmagupta composition
    pell_cases = [
        (2, 3, (3, 2)),   # 3rd positive solution to x^2 - 2y^2 = 1: (3+2sqrt2)^3 = 99 + 70sqrt2 -> x+y = 169
        (3, 3, (2, 1)),   # 3rd positive solution to x^2 - 3y^2 = 1: (2+sqrt3)^3 = 26 + 15sqrt3 -> x+y = 41
        (5, 2, (9, 4)),   # 2nd positive solution to x^2 - 5y^2 = 1: (9+4sqrt5)^2 = 161 + 72sqrt5 -> x+y = 233
        (6, 2, (5, 2)),   # 2nd positive solution to x^2 - 6y^2 = 1: (5+2sqrt6)^2 = 49 + 20sqrt6 -> x+y = 69
        (7, 2, (8, 3)),   # 2nd positive solution to x^2 - 7y^2 = 1: (8+3sqrt7)^2 = 127 + 48sqrt7 -> x+y = 175
    ]
    for offset, (d, rank_k, (x1, y1)) in enumerate(pell_cases, 56):
        qid = f"OLYM-T2-{offset:03d}"
        xk, yk = 1, 0
        for _ in range(rank_k):
            xk, yk = xk * x1 + d * yk * y1, xk * y1 + yk * x1
        assert xk * xk - d * yk * yk == 1
        found = []
        yy = 1
        while len(found) < rank_k:
            xx2 = 1 + d * yy * yy
            xx = math.isqrt(xx2)
            if xx * xx == xx2:
                found.append((xx, yy))
            yy += 1
        assert found[rank_k - 1] == (xk, yk)
        ans = xk + yk
        ord_en = "second" if rank_k == 2 else "third"
        ord_ar = "الثاني" if rank_k == 2 else "الثالث"
        q_en = (
            f"Ordered by increasing {m('x')}, let {m('(x_k, y_k)')} be the {ord_en} positive integer "
            f"solution to Pell's equation {m(f'x^2 - {d}y^2 = 1')}. Compute {m('x_k + y_k')}."
        )
        q_ar = (
            f"عند ترتيب الحلول الصحيحة الموجبة لمعادلة بيل {m(f'x^2 - {d}y^2 = 1')} تصاعدياً حسب {m('x')}، "
            f"ليكن {m('(x_k, y_k)')} الحل الموجب {ord_ar}. احسب {m('x_k + y_k')}."
        )
        svg = svg_number_strip([f"d={d}", f"k={rank_k}", "x+y=?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Number Theory", "Hard", bp4,
            q_en, q_ar, ans,
            [xk, yk, x1 + y1, ans + 12],
            f"Find the fundamental solution {m(f'({x1}, {y1})')} and expand {m(f'({x1} + {y1}\\sqrt{{{d}}})^{{{rank_k}}}')}.",
            f"أوجد الحل الأساسي {m(f'({x1}, {y1})')} ثم انشر القوة {m(f'({x1} + {y1}\\sqrt{{{d}}})^{{{rank_k}}}')}.",
            "All positive solutions to Pell's equation x^2 - d y^2 = 1 are generated by powers of the fundamental unit x_1 + y_1 sqrt(d).",
            [
                f"The smallest positive integer solution to {m(f'x^2 - {d}y^2 = 1')} is {m(f'(x_1, y_1) = ({x1}, {y1})')}.",
                f"Generate the {ord_en} solution via {m(f'x_{{{rank_k}}} + y_{{{rank_k}}}\\sqrt{{{d}}} = ({x1} + {y1}\\sqrt{{{d}}})^{{{rank_k}}} = {xk} + {yk}\\sqrt{{{d}}}')}.",
                f"Therefore {m(f'x_{{{rank_k}}} + y_{{{rank_k}}} = {xk} + {yk} = {ans}')}.",
            ],
            f"Direct check: {m(f'{xk}^2 - {d} \\cdot {yk}^2 = {xk*xk} - {d*yk*yk} = 1')}.",
            "جميع الحلول الموجبة لمعادلة بيل تتولد من قوى الحل الأساسي.",
            [
                f"الحل الموجب الأساسي للمعادلة {m(f'x^2 - {d}y^2 = 1')} هو {m(f'(x_1, y_1) = ({x1}, {y1})')}.",
                f"بنشر القوة {m(f'({x1} + {y1}\\sqrt{{{d}}})^{{{rank_k}}} = {xk} + {yk}\\sqrt{{{d}}}')} نحصل على الحل الموجب {ord_ar}.",
                f"إذن المجموع المطلوب هو {m(f'{xk} + {yk} = {ans}')}.",
            ],
            f"التحقق المباشر: {m(f'{xk}^2 - {d} \\cdot {yk}^2 = {xk*xk} - {d*yk*yk} = 1')}.",
            diagram_en=svg,
        ))

    return qs


# ==============================================================================
# UNIT 2.2 — Algebra (OLYM-T2-061 .. OLYM-T2-120)
# ==============================================================================

def _gen_u22_algebra() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 5: olym_t2_alg_vieta_newton_sums (OLYM-T2-061..075)
    # ------------------------------------------------------------------
    bp5 = "olym_t2_alg_vieta_newton_sums"

    # Easy (061..065): Quadratic Vieta r^3 + s^3
    vieta_easy = [
        (5, 3),
        (6, 4),
        (7, 5),
        (4, -3),
        (8, 9),
    ]
    for offset, (p_sum, q_prod) in enumerate(vieta_easy, 61):
        qid = f"OLYM-T2-{offset:03d}"
        ans = p_sum**3 - 3 * p_sum * q_prod
        p2 = p_sum**2 - 2 * q_prod
        assert p_sum * p2 - q_prod * p_sum == ans
        q_sign = f"+ {q_prod}" if q_prod >= 0 else f"- {abs(q_prod)}"
        q_en = (
            f"Let {m('r')} and {m('s')} be the roots of the quadratic equation "
            f"{m(f'x^2 - {p_sum}x {q_sign} = 0')}. Compute the symmetric power sum {m('r^3 + s^3')}."
        )
        q_ar = (
            f"ليكن {m('r')} و{m('s')} جذري المعادلة التربيعية "
            f"{m(f'x^2 - {p_sum}x {q_sign} = 0')}. احسب قيمة المقدار المتناظر {m('r^3 + s^3')}."
        )
        svg = svg_parabola_roots("r", "s", "P₃=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Easy", bp5,
            q_en, q_ar, ans,
            [p_sum**3, p_sum**3 - q_prod, ans + p_sum * q_prod, p2],
            f"Use Vieta's relations {m(f'r + s = {p_sum}')}, {m(f'rs = {q_prod}')}, and {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            f"استخدم علاقتي فييت {m(f'r + s = {p_sum}')} و{m(f'rs = {q_prod}')} مع المتطابقة {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
            "Express the cubic power sum directly in terms of elementary symmetric polynomials.",
            [
                f"By Vieta's formulas, {m(f'r + s = {p_sum}')} and {m(f'rs = {q_prod}')}.",
                f"Apply the identity {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
                f"Substitute the values: {m(f'{p_sum}^3 - 3({q_prod})({p_sum}) = {p_sum**3} - {3 * p_sum * q_prod} = {ans}')}.",
            ],
            f"Newton's recurrence check: {m(f'P_2 = {p2}')} and {m(f'P_3 = {p_sum} P_2 - ({q_prod}) P_1 = {ans}')}.",
            "نعبّر عن مجموع المكعبين بدلالة المجاميع المتناظرة الأولية لفييت.",
            [
                f"من صيغ فييت نجد {m(f'r + s = {p_sum}')} و{m(f'rs = {q_prod}')}.",
                f"نطبق المتطابقة {m('r^3 + s^3 = (r + s)^3 - 3rs(r + s)')}.",
                f"بالتعويض نحصل على {m(f'{p_sum}^3 - 3({q_prod})({p_sum}) = {ans}')}.",
            ],
            f"باستخدام علاقة نيوتن التكرارية: {m(f'P_2 = {p2}')} ومنه {m(f'P_3 = {ans}')}.",
            diagram_en=svg,
        ))

    # Medium (066..070): Cubic Vieta & Newton sums P_3 = r_1^3 + r_2^3 + r_3^3
    vieta_med = [
        (4, 2, 5),
        (5, 4, 3),
        (3, -2, 4),
        (6, 7, 2),
        (2, -3, 6),
    ]
    for offset, (e1, e2, e3) in enumerate(vieta_med, 66):
        qid = f"OLYM-T2-{offset:03d}"
        p1 = e1
        p2 = e1 * p1 - 2 * e2
        p3 = e1 * p2 - e2 * p1 + 3 * e3
        ans = p3
        e2_term = f"+ {e2}x" if e2 >= 0 else f"- {abs(e2)}x"
        q_en = (
            f"Let {m('a, b, c')} be the complex roots of {m(f'x^3 - {e1}x^2 {e2_term} - {e3} = 0')}. "
            f"Find the value of {m('a^3 + b^3 + c^3')}."
        )
        q_ar = (
            f"لتكن {m('a, b, c')} الجذور المركبة للمعادلة {m(f'x^3 - {e1}x^2 {e2_term} - {e3} = 0')}. "
            f"أوجد قيمة المقدار {m('a^3 + b^3 + c^3')}."
        )
        svg = svg_number_strip([f"e₁={e1}", f"e₂={e2}", "P₃=?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Medium", bp5,
            q_en, q_ar, ans,
            [p3 - 3 * e3, e1**3, p2, p3 + 3 * e3],
            f"Compute {m('P_1 = e_1')}, {m('P_2 = e_1 P_1 - 2e_2')}, and {m('P_3 = e_1 P_2 - e_2 P_1 + 3e_3')}.",
            f"احسب بالتتابع {m('P_1 = e_1')} ثم {m('P_2 = e_1 P_1 - 2e_2')} ثم {m('P_3 = e_1 P_2 - e_2 P_1 + 3e_3')}.",
            "Newton's sums link power sums P_k to Vieta's elementary symmetric sums e_1, e_2, e_3.",
            [
                f"By Vieta's formulas, {m(f'e_1 = {e1}')}, {m(f'e_2 = {e2}')}, and {m(f'e_3 = {e3}')}.",
                f"Compute {m(f'P_1 = {p1}')} and {m(f'P_2 = e_1^2 - 2e_2 = {e1}^2 - 2({e2}) = {p2}')}.",
                f"By Newton's identity, {m(f'P_3 = e_1 P_2 - e_2 P_1 + 3e_3 = {e1}({p2}) - ({e2})({p1}) + 3({e3}) = {ans}')}.",
            ],
            f"Summing {m('x^3 = e_1 x^2 - e_2 x + e_3')} over the three roots directly confirms {m(f'P_3 = {ans}')}.",
            "تربط متطابقات نيوتن مجاميع القوى بمجاميع فييت المتناظرة الأولية.",
            [
                f"من صيغ فييت لدينا {m(f'e_1 = {e1}')} و{m(f'e_2 = {e2}')} و{m(f'e_3 = {e3}')}.",
                f"نحسب {m(f'P_1 = {p1}')} وكذلك {m(f'P_2 = e_1^2 - 2e_2 = {p2}')}.",
                f"بتطبيق متطابقة نيوتن الثالثة نجد {m(f'P_3 = e_1 P_2 - e_2 P_1 + 3e_3 = {ans}')}.",
            ],
            f"بجمع المعادلة {m('x^3 = e_1 x^2 - e_2 x + e_3')} على الجذور الثلاثة نتأكد أن {m(f'P_3 = {ans}')}.",
            diagram_en=svg,
        ))

    # Hard (071..075): Fifth-power Newton sums P_5 on depressed cubics x^3 + p x - q = 0
    # Note: for x^3 + p x - q = 0, P_1 = 0, P_2 = -2p, P_3 = 3q, P_4 = -p P_2 + q P_1 = 2p^2, P_5 = -p P_3 + q P_2 = -5pq!
    vieta_hard = [
        (-3, 4),   # x^3 - 3x - 4 = 0 -> p = -3, q = 4 -> P_5 = -5(-3)(4) = 60
        (-2, 5),   # x^3 - 2x - 5 = 0 -> p = -2, q = 5 -> P_5 = 50
        (-4, 3),   # x^3 - 4x - 3 = 0 -> p = -4, q = 3 -> P_5 = 60? Let's vary so answers differ: (-4, 7) -> 140
        (3, -4),   # x^3 + 3x + 4 = 0 -> p = 3, q = -4 -> P_5 = 60 -> let's pick (-5, 6) -> 150 and (2, -7) -> 70
        (-5, 2),   # p = -5, q = 2 -> P_5 = 50 -> let's pick distinct pairs!
    ]
    vieta_hard = [
        (-3, 4),   # P_5 = 60
        (-2, 7),   # P_5 = 70
        (-4, 5),   # P_5 = 100
        (-5, 6),   # P_5 = 150
        (3, -8),   # P_5 = 120
    ]
    for offset, (p_lin, q_const) in enumerate(vieta_hard, 71):
        qid = f"OLYM-T2-{offset:03d}"
        # Equation: x^3 + p_lin * x - q_const = 0 => x^3 = -p_lin * x + q_const
        P1 = 0
        P2 = -2 * p_lin
        P3 = 3 * q_const
        P4 = -p_lin * P2 + q_const * P1
        P5 = -p_lin * P3 + q_const * P2
        assert P5 == -5 * p_lin * q_const
        ans = P5
        lin_str = f"+ {p_lin}x" if p_lin > 0 else f"- {abs(p_lin)}x"
        c_str = f"- {q_const}" if q_const > 0 else f"+ {abs(q_const)}"
        q_en = (
            f"In an Intermediate Olympiad algebra problem, let {m('r_1, r_2, r_3')} be the roots "
            f"of the depressed cubic {m(f'x^3 {lin_str} {c_str} = 0')}. Find {m('r_1^5 + r_2^5 + r_3^5')}."
        )
        q_ar = (
            f"في مسألة جبر للأولمبياد المتوسط، لتكن {m('r_1, r_2, r_3')} جذور كثيرة الحدود التكعيبية "
            f"{m(f'x^3 {lin_str} {c_str} = 0')}. أوجد قيمة {m('r_1^5 + r_2^5 + r_3^5')}."
        )
        svg = svg_function_machine("P₁=0", "Newton", "x⁵", "P₅ = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Hard", bp5,
            q_en, q_ar, ans,
            [-3 * p_lin * q_const, P4, ans - 10, ans + 20],
            f"Multiply {m(f'x^3 = {-p_lin}x + {q_const}')} by {m('x^2')} to get {m(f'P_5 = {-p_lin} P_3 + {q_const} P_2')}.",
            f"اضرب العلاقة {m(f'x^3 = {-p_lin}x + {q_const}')} في {m('x^2')} واجمع على الجذور لتحصل على {m(f'P_5 = {-p_lin} P_3 + {q_const} P_2')}.",
            "On any depressed cubic x^3 + px - q = 0, vanishing P_1 collapses Newton's fifth sum to P_5 = -5pq.",
            [
                f"Since there is no {m('x^2')} term, {m('P_1 = 0')}, {m(f'P_2 = -2({p_lin}) = {P2}')}, and {m(f'P_3 = 3({q_const}) = {P3}')}.",
                f"Each root satisfies {m(f'r_i^5 = {-p_lin} r_i^3 + ({q_const}) r_i^2')}.",
                f"Summing over {m('i = 1, 2, 3')} gives {m(f'P_5 = ({-p_lin})({P3}) + ({q_const})({P2}) = {ans}')}.",
            ],
            f"This matches the classic depressed-cubic identity {m(f'P_5 = -5pq = -5({p_lin})({q_const}) = {ans}')}.",
            "في المعادلة التكعيبية الخالية من الحد التربيعي تنعدم P_1 فتختزل متطابقة نيوتن الخامسة إلى P_5 = -5pq.",
            [
                f"لعدم وجود حد {m('x^2')} يكون {m('P_1 = 0')} و{m(f'P_2 = {P2}')} و{m(f'P_3 = {P3}')}.",
                f"كل جذر يحقق {m(f'r_i^5 = ({-p_lin}) r_i^3 + ({q_const}) r_i^2')}.",
                f"بالجمع على الجذور الثلاثة نجد {m(f'P_5 = ({-p_lin})({P3}) + ({q_const})({P2}) = {ans}')}.",
            ],
            f"وهذا يطابق المتطابقة الشهيرة {m(f'P_5 = -5pq = {ans}')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 6: olym_t2_alg_polynomial_remainders (OLYM-T2-076..090)
    # ------------------------------------------------------------------
    bp6 = "olym_t2_alg_polynomial_remainders"

    # Easy (076..080): Linear remainder R(x) = Ax + B modulo (x - a)(x - b), evaluate R(c)
    rem_easy = [
        (1, 5, 3, 13, 6),
        (-2, 4, 2, 20, 5),
        (2, 7, 5, 22, 8),
        (-1, 3, 4, 23, 7),
        (1, 9, 4, 27, 10),
    ]
    for offset, (a, ra, b, rb, c_eval) in enumerate(rem_easy, 76):
        qid = f"OLYM-T2-{offset:03d}"
        A = Fraction(rb - ra, b - a)
        B = ra - A * a
        assert A.denominator == 1 and B.denominator == 1
        Ai, Bi = int(A), int(B)
        ans = Ai * c_eval + Bi
        assert Ai * a + Bi == ra and Ai * b + Bi == rb
        xa_str = f"x - {a}" if a > 0 else f"x + {abs(a)}"
        xb_str = f"x - {b}"
        q_en = (
            f"A polynomial {m('P(x)')} leaves remainder {m(str(ra))} when divided by {m(xa_str)} "
            f"and remainder {m(str(rb))} when divided by {m(xb_str)}. Let {m('R(x)')} be the remainder "
            f"when {m('P(x)')} is divided by {m(f'({xa_str})({xb_str})')}. Find {m(f'R({c_eval})')}."
        )
        q_ar = (
            f"كثيرة حدود {m('P(x)')} تترك باقياً قدره {m(str(ra))} عند قسمتها على {m(xa_str)} "
            f"وباقياً قدره {m(str(rb))} عند قسمتها على {m(xb_str)}. إذا كان {m('R(x)')} باقي قسمة "
            f"{m('P(x)')} على {m(f'({xa_str})({xb_str})')}، فأوجد {m(f'R({c_eval})')}."
        )
        svg = svg_function_machine("P(x)", xa_str, xb_str, "R = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Easy", bp6,
            q_en, q_ar, ans,
            [Ai + Bi, ans - Ai, ans + Ai, rb + ra],
            f"Write {m('R(x) = Ax + B')} and solve {m(f'R({a}) = {ra}')} and {m(f'R({b}) = {rb}')}.",
            f"ضع الباقي الخطي {m('R(x) = Ax + B')} وحل المعادلتين {m(f'R({a}) = {ra}')} و{m(f'R({b}) = {rb}')}.",
            "The remainder modulo a quadratic divisor has degree at most 1 and agrees with P(x) at the divisor's roots.",
            [
                f"Write {m(f'P(x) = ({xa_str})({xb_str})Q(x) + Ax + B')}, where {m('R(x) = Ax + B')}.",
                f"By the Remainder Theorem, {m(f'{a}A + B = {ra}')} and {m(f'{b}A + B = {rb}')}, so {m(f'A = {Ai}')} and {m(f'B = {Bi}')}.",
                f"Evaluate at {m(f'x = {c_eval}')}: {m(f'R({c_eval}) = {Ai}({c_eval}) + ({Bi}) = {ans}')}.",
            ],
            f"Check: {m(f'R({a}) = {Ai * a + Bi} = {ra}')} and {m(f'R({b}) = {Ai * b + Bi} = {rb}')}.",
            "باقي القسمة على مقسوم تربيعي يكون خطياً على الأكثر ويتفق مع كثيرة الحدود عند جذري المقسوم.",
            [
                f"نكتب {m(f'P(x) = ({xa_str})({xb_str})Q(x) + Ax + B')} حيث {m('R(x) = Ax + B')}.",
                f"من مبرهنة الباقي: {m(f'{a}A + B = {ra}')} و{m(f'{b}A + B = {rb}')}، ومنه {m(f'A = {Ai}')} و{m(f'B = {Bi}')}.",
                f"نعوض {m(f'x = {c_eval}')}: {m(f'R({c_eval}) = {Ai}({c_eval}) + ({Bi}) = {ans}')}.",
            ],
            f"التحقق: {m(f'R({a}) = {ra}')} وكذلك {m(f'R({b}) = {rb}')}.",
            diagram_en=svg,
        ))

    # Medium (081..085): High-degree remainder modulo x^2 + x + 1 using x^3 ≡ 1
    cyc_med = [
        (2026, 2024, 5, 3),   # x^2026 + 2x^2024 + 5 mod (x^2+x+1), evaluate R(3)
        (100, 50, 7, 4),
        (301, 200, 4, 5),
        (500, 250, 9, 2),
        (998, 499, 6, 6),
    ]
    for offset, (n1, n2, c0, x_ev) in enumerate(cyc_med, 81):
        qid = f"OLYM-T2-{offset:03d}"
        # Modulo x^2 + x + 1: x^0 -> (0, 1), x^1 -> (1, 0), x^2 -> (-1, -1) where (A, B) means Ax + B
        basis = {0: (0, 1), 1: (1, 0), 2: (-1, -1)}
        a1, b1 = basis[n1 % 3]
        a2, b2 = basis[n2 % 3]
        A_rem = a1 + 2 * a2
        B_rem = b1 + 2 * b2 + c0
        ans = A_rem * x_ev + B_rem
        q_en = (
            f"Let {m('R(x)')} be the remainder of degree at most {m('1')} when "
            f"{m(f'P(x) = x^{{{n1}}} + 2x^{{{n2}}} + {c0}')} is divided by {m('x^2 + x + 1')}. "
            f"Compute {m(f'R({x_ev})')}."
        )
        q_ar = (
            f"ليكن {m('R(x)')} الباقي الذي لا تزيد درجته على {m('1')} عند قسمة "
            f"{m(f'P(x) = x^{{{n1}}} + 2x^{{{n2}}} + {c0}')} على {m('x^2 + x + 1')}. "
            f"احسب {m(f'R({x_ev})')}."
        )
        svg = svg_digit_slots(["x³≡1", "x²+x+1", f"x={x_ev}", "R=?"], top_note="Cyclotomic")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Medium", bp6,
            q_en, q_ar, ans,
            [ans + x_ev, ans - x_ev, c0 + 3, abs(A_rem) + abs(B_rem)],
            f"Since {m('(x - 1)(x^2 + x + 1) = x^3 - 1')}, we have {m('x^3 \\equiv 1 \\pmod{x^2 + x + 1}')} and {m('x^2 \\equiv -x - 1')}.",
            f"بما أن {m('(x - 1)(x^2 + x + 1) = x^3 - 1')} فإن {m('x^3 \\equiv 1 \\pmod{x^2 + x + 1}')} وكذلك {m('x^2 \\equiv -x - 1')}.",
            "Reduce exponents modulo 3 using x^3 ≡ 1 (mod x^2 + x + 1) and replace x^2 by -x - 1.",
            [
                f"Modulo {m('x^2 + x + 1')}, {m('x^3 \\equiv 1')}, so {m(f'x^{{{n1}}} \\equiv x^{{{n1 % 3}}}')} and {m(f'x^{{{n2}}} \\equiv x^{{{n2 % 3}}}')}.",
                f"Using {m('x^2 \\equiv -x - 1')}, the linear remainder simplifies to {m(f'R(x) = ({A_rem})x + ({B_rem})')}.",
                f"Evaluating at {m(f'x = {x_ev}')} yields {m(f'R({x_ev}) = ({A_rem})({x_ev}) + ({B_rem}) = {ans}')}.",
            ],
            f"Checking at a cube root of unity {m('\\omega')}: {m('P(\\omega) = R(\\omega)')} holds identically.",
            "نختزل الأسس معيار 3 لأن x^3 ≡ 1 معيار (x^2 + x + 1) ثم نستبدل x^2 بالمقدار -x - 1.",
            [
                f"معيار {m('x^2 + x + 1')} لدينا {m('x^3 \\equiv 1')}، ومنه {m(f'x^{{{n1}}} \\equiv x^{{{n1 % 3}}}')} و{m(f'x^{{{n2}}} \\equiv x^{{{n2 % 3}}}')}.",
                f"باستبدال {m('x^2 \\equiv -x - 1')} يتبسط الباقي الخطي إلى {m(f'R(x) = ({A_rem})x + ({B_rem})')}.",
                f"بالتعويض عند {m(f'x = {x_ev}')} نجد {m(f'R({x_ev}) = {ans}')}.",
            ],
            f"عند التعويض بالجذر التكعيبي للواحد {m('\\omega')} تتطابق قيمتا {m('P(\\omega)')} و{m('R(\\omega)')}.",
            diagram_en=svg,
        ))

    # Hard (086..090): Olympiad difference-polynomial interpolation
    interp_hard = [
        (4, 3, 5),   # monic deg 4, P(k) = 3k for k=1..4 -> find P(5) = 4! + 15 = 39
        (4, 5, 6),   # monic deg 4, P(k) = 5k for k=1..4 -> find P(6) = 5*4*3*2 + 30 = 150
        (3, 4, 6),   # monic deg 3, P(k) = 4k^2 for k=1..3 -> find P(6) via Q(x) = P(x) - 4x^2 = (x-1)(x-2)(x-3) -> 60 + 144 = 204
        (4, 2, 0),   # monic deg 4, P(k) = 2k^2 for k=1..4 -> find P(0) = 24 + 0 = 24
        (5, 2, 6),   # monic deg 5, P(k) = 2k for k=1..5 -> find P(6) = 120 + 12 = 132
    ]
    for offset, (deg_d, mult_c, eval_x) in enumerate(interp_hard, 86):
        qid = f"OLYM-T2-{offset:03d}"
        is_quad_rhs = offset in (88, 89)
        prod_val = math.prod(eval_x - k for k in range(1, deg_d + 1))
        rhs_eval = mult_c * (eval_x**2 if is_quad_rhs else eval_x)
        ans = prod_val + rhs_eval
        rhs_tex = f"{mult_c}k^2" if is_quad_rhs else f"{mult_c}k"
        gx_tex = f"{mult_c}x^2" if is_quad_rhs else f"{mult_c}x"
        fac_tex = "".join(f"(x - {k})" for k in range(1, deg_d + 1))
        ks_str = ", ".join(str(k) for k in range(1, deg_d + 1))
        q_en = (
            f"A monic polynomial {m('P(x)')} of degree {m(str(deg_d))} satisfies {m(f'P(k) = {rhs_tex}')} "
            f"for {m(f'k = {ks_str}')}. Determine {m(f'P({eval_x})')}."
        )
        q_ar = (
            f"كثيرة حدود واحدية المعامل الرئيس {m('P(x)')} من الدرجة {m(str(deg_d))} تحقق {m(f'P(k) = {rhs_tex}')} "
            f"من أجل {m(f'k = {ks_str}')}. أوجد قيمة {m(f'P({eval_x})')}."
        )
        svg = svg_olym_func_mapping(["1,2,..", f"deg {deg_d}", f"x={eval_x}"], ["f(1)", "f(d)", "?"], note="Difference")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Hard", bp6,
            q_en, q_ar, ans,
            [rhs_eval, abs(prod_val), ans - rhs_eval if rhs_eval != 0 else ans + deg_d, ans + 24],
            f"Define the auxiliary monic polynomial {m(f'Q(x) = P(x) - {gx_tex}')}, which has roots {m(ks_str)}.",
            f"عرّف كثيرة الحدود المساعدة الواحدية {m(f'Q(x) = P(x) - {gx_tex}')} التي جذورها {m(ks_str)}.",
            "Subtract the pattern polynomial to form a monic polynomial with all d known roots.",
            [
                f"Consider {m(f'Q(x) = P(x) - {gx_tex}')}. Since {m(f'\\deg({gx_tex}) < {deg_d}')}, {m('Q(x)')} is monic of degree {m(str(deg_d))}.",
                f"Because {m('Q(k) = 0')} for {m(f'k = {ks_str}')}, the Factor Theorem forces {m(f'Q(x) = {fac_tex}')}.",
                f"Evaluate at {m(f'x = {eval_x}')}: {m(f'P({eval_x}) = {prod_val} + {rhs_eval} = {ans}')}.",
            ],
            f"For every {m(f'k \\in \\{{{ks_str}\\}}')}, the product term vanishes and recovers {m(f'P(k) = {rhs_tex}')}.",
            "نطرح دالة النمط لنحصل على كثيرة حدود واحدية معروفة الجذور بالكامل.",
            [
                f"نضع {m(f'Q(x) = P(x) - {gx_tex}')}، وبما أن {m(f'\\deg({gx_tex}) < {deg_d}')} فإن {m('Q(x)')} واحدية من الدرجة {m(str(deg_d))}.",
                f"بما أن {m('Q(k) = 0')} لقيم {m(f'k = {ks_str}')}، فإن مبرهنة العامل تعطي {m(f'Q(x) = {fac_tex}')}.",
                f"بالتعويض عند {m(f'x = {eval_x}')}: {m(f'P({eval_x}) = {prod_val} + {rhs_eval} = {ans}')}.",
            ],
            f"عند تعويض أي قيمة من {m(ks_str)} ينعدم الجداء فنستعيد الشرط المعطى تماماً.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 7: olym_t2_alg_functional_substitutions (OLYM-T2-091..105)
    # ------------------------------------------------------------------
    bp7 = "olym_t2_alg_functional_substitutions"

    # Easy (091..095): Linear involution f(x) + a f(c - x) = b x + d
    func_easy = [
        (2, 5, 3, 1, 4),   # f(x) + 2 f(5-x) = 3x + 1, find f(4)
        (3, 6, 4, -2, 5),  # f(x) + 3 f(6-x) = 4x - 2, find f(5)
        (2, 4, 6, 3, 3),   # f(x) + 2 f(4-x) = 6x + 3, find f(3)
        (4, 7, 5, 2, 6),   # f(x) + 4 f(7-x) = 5x + 2, find f(6)
        (3, 8, 2, 4, 7),   # f(x) + 3 f(8-x) = 2x + 4, find f(7)
    ]
    for offset, (a_coef, c_sum, b_slp, d_int, x0) in enumerate(func_easy, 91):
        qid = f"OLYM-T2-{offset:03d}"
        # Eq1 (at x0): f(x0) + a f(y0) = r1; Eq2 (at y0=c-x0): f(y0) + a f(x0) = r2
        y0 = c_sum - x0
        r1 = Fraction(b_slp * x0 + d_int)
        r2 = Fraction(b_slp * y0 + d_int)
        fx0 = (r1 - a_coef * r2) / (1 - a_coef * a_coef)
        fy0 = (r2 - a_coef * r1) / (1 - a_coef * a_coef)
        assert fx0 + a_coef * fy0 == r1 and fy0 + a_coef * fx0 == r2
        ans = fx0 if fx0.denominator != 1 else int(fx0)
        d_str = f"+ {d_int}" if d_int >= 0 else f"- {abs(d_int)}"
        q_en = (
            f"A function {m('f: \\mathbb{R} \\to \\mathbb{R}')} satisfies "
            f"{m(f'f(x) + {a_coef}f({c_sum} - x) = {b_slp}x {d_str}')} for all real {m('x')}. "
            f"Find {m(f'f({x0})')}."
        )
        q_ar = (
            f"تحقق الدالة {m('f: \\mathbb{R} \\to \\mathbb{R}')} المعادلة الدالية "
            f"{m(f'f(x) + {a_coef}f({c_sum} - x) = {b_slp}x {d_str}')} لكل عدد حقيقي {m('x')}. "
            f"أوجد قيمة {m(f'f({x0})')}."
        )
        svg = svg_olym_func_mapping([str(x0), str(y0)], [f"f({x0})", "?"], note="x ↔ c−x")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Easy", bp7,
            q_en, q_ar, ans,
            [fy0, fx0 + 1, -fx0, Fraction(int(r1), 1 + a_coef)],
            f"Substitute {m(f'x = {x0}')} and {m(f'x = {y0}')} to create two linear equations in {m(f'f({x0})')} and {m(f'f({y0})')}.",
            f"عوّض {m(f'x = {x0}')} ثم {m(f'x = {y0}')} لتكوين معادلتين خطيتين في المجهولين {m(f'f({x0})')} و{m(f'f({y0})')}.",
            "Exploit the involution x <-> c - x to close a 2-by-2 linear system for the unknown function values.",
            [
                f"At {m(f'x = {x0}')}: {m(f'f({x0}) + {a_coef}f({y0}) = {int(r1)}')}.",
                f"At {m(f'x = {y0}')}: {m(f'f({y0}) + {a_coef}f({x0}) = {int(r2)}')}.",
                f"Eliminating {m(f'f({y0})')} gives {m(f'(1 - {a_coef**2})f({x0}) = {int(r1 - a_coef * r2)}')}, hence {m(f'f({x0}) = {fx0}')}.",
            ],
            f"With {m(f'f({y0}) = {fy0}')}, we verify {m(f'({fx0}) + {a_coef}({fy0}) = {int(r1)}')}.",
            "نستغل التحويل الارتدادي x <-> c - x لتكوين جملة خطية مغلقة من معادلتين.",
            [
                f"عند {m(f'x = {x0}')}: {m(f'f({x0}) + {a_coef}f({y0}) = {int(r1)}')}.",
                f"عند {m(f'x = {y0}')}: {m(f'f({y0}) + {a_coef}f({x0}) = {int(r2)}')}.",
                f"بحذف {m(f'f({y0})')} نحصل على {m(f'(1 - {a_coef**2})f({x0}) = {int(r1 - a_coef * r2)}')}.",
            ],
            f"بقسمة الطرفين والتأكد من {m(f'f({y0}) = {fy0}')} تتحقق المعادلتان تماماً.",
            diagram_en=svg,
        ))

    # Medium (096..100): Reciprocal involution a f(x) + b f(1/x) = c x
    func_med = [
        (2, 3, 10, 2),   # 2f(x) + 3f(1/x) = 10x, find f(2)
        (1, 2, 9, 3),    # f(x) + 2f(1/x) = 9x, find f(3)
        (3, 1, 16, 4),   # 3f(x) + f(1/x) = 16x, find f(4)
        (2, 5, 21, 3),   # 2f(x) + 5f(1/x) = 21x, find f(3)
        (3, 2, 15, 5),   # 3f(x) + 2f(1/x) = 15x, find f(5)
    ]
    for offset, (a_c, b_c, c_rhs, k_val) in enumerate(func_med, 96):
        qid = f"OLYM-T2-{offset:03d}"
        # a f(k) + b f(1/k) = c k; b f(k) + a f(1/k) = c / k
        r1 = Fraction(c_rhs * k_val)
        r2 = Fraction(c_rhs, k_val)
        fk = (a_c * r1 - b_c * r2) / (a_c * a_c - b_c * b_c)
        f_inv = (a_c * r2 - b_c * r1) / (a_c * a_c - b_c * b_c)
        assert a_c * fk + b_c * f_inv == r1 and b_c * fk + a_c * f_inv == r2
        ans = fk if fk.denominator != 1 else int(fk)
        a_pref = "" if a_c == 1 else str(a_c)
        b_pref = "" if b_c == 1 else str(b_c)
        q_en = (
            f"For all non-zero real numbers {m('x')}, a function {m('f')} satisfies "
            f"{m(f'{a_pref}f(x) + {b_pref}f(1/x) = {c_rhs}x')}. Determine {m(f'f({k_val})')}."
        )
        q_ar = (
            f"لكل عدد حقيقي غير صفري {m('x')} تحقق الدالة {m('f')} العلاقة "
            f"{m(f'{a_pref}f(x) + {b_pref}f(1/x) = {c_rhs}x')}. أوجد قيمة {m(f'f({k_val})')}."
        )
        svg = svg_olym_func_mapping([str(k_val), f"1/{k_val}"], [f"f({k_val})", "?"], note="x ↔ 1/x")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Medium", bp7,
            q_en, q_ar, ans,
            [f_inv, -fk, fk + 2, Fraction(c_rhs * k_val, a_c + b_c)],
            f"Evaluate the equation at {m(f'x = {k_val}')} and at {m(f'x = 1/{k_val}')}, then eliminate {m(f'f(1/{k_val})')}.",
            f"عوّض {m(f'x = {k_val}')} و{m(f'x = 1/{k_val}')} ثم احذف {m(f'f(1/{k_val})')}.",
            "Replace x by 1/x to pair f(x) and f(1/x) in a solvable linear system.",
            [
                f"Setting {m(f'x = {k_val}')} gives {m(f'{a_pref}f({k_val}) + {b_pref}f(1/{k_val}) = {r1}')}.",
                f"Setting {m(f'x = 1/{k_val}')} gives {m(f'{a_pref}f(1/{k_val}) + {b_pref}f({k_val}) = {r2}')}.",
                f"Eliminating {m(f'f(1/{k_val})')} yields {m(f'({a_c**2} - {b_c**2})f({k_val}) = {a_c * r1 - b_c * r2}')}, so {m(f'f({k_val}) = {fk}')}.",
            ],
            f"Substituting {m(f'f({k_val}) = {fk}')} and {m(f'f(1/{k_val}) = {f_inv}')} satisfies both equations.",
            "نستبدل x بالمقلوب 1/x لربط القيمتين في جملة خطية قابلة للحل.",
            [
                f"بتعويض {m(f'x = {k_val}')} نحصل على {m(f'{a_pref}f({k_val}) + {b_pref}f(1/{k_val}) = {r1}')}.",
                f"بتعويض {m(f'x = 1/{k_val}')} نحصل على {m(f'{a_pref}f(1/{k_val}) + {b_pref}f({k_val}) = {r2}')}.",
                f"بحذف {m(f'f(1/{k_val})')} نجد أن {m(f'f({k_val}) = {fk}')}.",
            ],
            f"بالتعويض العكسي تتحقق المعادلتان معاً بدقة.",
            diagram_en=svg,
        ))

    # Hard (101..105): Order-3 Mobius cycle f(x) + f((x-1)/x) = c * x
    # Orbit: x1 = x0, x2 = (x0-1)/x0, x3 = 1/(1-x0); equations: f1 + f2 = c x1, f2 + f3 = c x2, f3 + f1 = c x3
    # => f1 = c (x1 - x2 + x3) / 2
    func_hard = [
        (4, 2),   # c=4, x0=2 -> x1=2, x2=1/2, x3=-1 -> f(2) = 2*(2 - 1/2 - 1) = 1
        (6, 3),   # c=6, x0=3 -> x1=3, x2=2/3, x3=-1/2 -> f(3) = 3*(3 - 2/3 - 1/2) = 11/2
        (12, 4),  # c=12, x0=4 -> x1=4, x2=3/4, x3=-1/3 -> f(4) = 6*(4 - 3/4 - 1/3) = 35/2
        (4, -1),  # c=4, x0=-1 -> x1=-1, x2=2, x3=1/2 -> f(-1) = 2*(-1 - 2 + 1/2) = -5
        (20, 5),  # c=20, x0=5 -> x1=5, x2=4/5, x3=-1/4 -> f(5) = 10*(5 - 4/5 - 1/4) = 79/2
    ]
    for offset, (c_rhs, x0_int) in enumerate(func_hard, 101):
        qid = f"OLYM-T2-{offset:03d}"
        x1 = Fraction(x0_int)
        x2 = (x1 - 1) / x1
        x3 = Fraction(1, 1) / (1 - x1)
        assert (x3 - 1) / x3 == x1
        f1 = Fraction(c_rhs, 2) * (x1 - x2 + x3)
        f2 = Fraction(c_rhs) * x1 - f1
        f3 = Fraction(c_rhs) * x2 - f2
        assert f3 + f1 == Fraction(c_rhs) * x3
        ans = f1 if f1.denominator != 1 else int(f1)
        q_en = (
            f"In an Intermediate Olympiad functional equation, {m('f: \\mathbb{R} \\setminus \\{0, 1\\} \\to \\mathbb{R}')} "
            f"satisfies {m(f'f(x) + f\\!\\left(\\frac{{x - 1}}{{x}}\\right) = {c_rhs}x')}. Compute {m(f'f({x0_int})')}."
        )
        q_ar = (
            f"في معادلة دالية للأولمبياد المتوسط، تحقق الدالة {m('f: \\mathbb{R} \\setminus \\{0, 1\\} \\to \\mathbb{R}')} "
            f"العلاقة {m(f'f(x) + f\\!\\left(\\frac{{x - 1}}{{x}}\\right) = {c_rhs}x')}. احسب قيمة {m(f'f({x0_int})')}."
        )
        svg = svg_olym_func_mapping([str(x1), str(x2), str(x3)], ["f₁", "f₂", "?"], note="3-Cycle")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Hard", bp7,
            q_en, q_ar, ans,
            [f2, f3, Fraction(c_rhs) * x1 / 2, f1 + 2],
            f"Iterate {m('g(x) = (x - 1)/x')} three times: {m(f'{x1} \\to {x2} \\to {x3} \\to {x1}')}.",
            f"كرّر التعويض بالدالة {m('g(x) = (x - 1)/x')} ثلاث مرات لتحصل على دورة مغلقة: {m(f'{x1} \\to {x2} \\to {x3} \\to {x1}')}.",
            "The Mobius map g(x) = (x - 1)/x has order 3, turning the functional equation into a closed 3-cycle.",
            [
                f"Track the 3-cycle of {m('g(x) = (x - 1)/x')}: {m(f'x_1 = {x1}')}, {m(f'x_2 = {x2}')}, {m(f'x_3 = {x3}')}, and {m('g(x_3) = x_1')}.",
                f"Evaluating at {m('x_1, x_2, x_3')} gives {m(f'f(x_1) + f(x_2) = {c_rhs * x1}')}, {m(f'f(x_2) + f(x_3) = {c_rhs * x2}')}, and {m(f'f(x_3) + f(x_1) = {c_rhs * x3}')}.",
                f"Take (first - second + third)/2: {m(f'f({x0_int}) = \\frac{{{c_rhs}}}{{2}}\\left({x1} - ({x2}) + ({x3})\\right) = {f1}')}.",
            ],
            f"Check cycle closure: {m(f'({f1}) + ({f2}) = {c_rhs * x1}')}, {m(f'({f2}) + ({f3}) = {c_rhs * x2}')}, and {m(f'({f3}) + ({f1}) = {c_rhs * x3}')}.",
            "التحويل الكسري g(x) = (x - 1)/x دورته 3، مما يحوّل المعادلة الدالية إلى جملة مغلقة من ثلاث معادلات.",
            [
                f"نتتبع الدورة الثلاثية: {m(f'x_1 = {x1}')} ثم {m(f'x_2 = {x2}')} ثم {m(f'x_3 = {x3}')} وتعود إلى {m('x_1')}.",
                f"بالتعويض نحصل على ثلاث معادلات خطية في {m('f(x_1), f(x_2), f(x_3)')}.",
                f"بأخذ نصف (الأولى ناقص الثانية زائد الثالثة) نجد {m(f'f({x0_int}) = {f1}')}.",
            ],
            f"التحقق من المجاميع الثلاثة يؤكد إغلاق الدورة بدقة.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 8: olym_t2_alg_floor_hermite_eqs (OLYM-T2-106..120)
    # ------------------------------------------------------------------
    bp8 = "olym_t2_alg_floor_hermite_eqs"

    # Easy (106..110): Hermite's identity sum_{k=0}^{n-1} floor(x + k/n) = floor(n x)
    herm_easy = [
        (Fraction(17, 5), 15),
        (Fraction(23, 7), 21),
        (Fraction(19, 4), 24),
        (Fraction(31, 6), 18),
        (Fraction(29, 8), 32),
    ]
    for offset, (x_frac, n_cnt) in enumerate(herm_easy, 106):
        qid = f"OLYM-T2-{offset:03d}"
        ans = math.floor(n_cnt * x_frac)
        direct_sum = sum(math.floor(x_frac + Fraction(k, n_cnt)) for k in range(n_cnt))
        assert ans == direct_sum
        q_en = (
            f"Using Hermite's floor identity, evaluate the exact finite sum "
            f"{m(f'\\sum_{{k=0}}^{{{n_cnt - 1}}} \\left\\lfloor \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}} + \\frac{{k}}{{{n_cnt}}} \\right\\rfloor')}."
        )
        q_ar = (
            f"باستخدام متطابقة هيرميت لدالة الجزء الصحيح، احسب قيمة المجموع المنتهي "
            f"{m(f'\\sum_{{k=0}}^{{{n_cnt - 1}}} \\left\\lfloor \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}} + \\frac{{k}}{{{n_cnt}}} \\right\\rfloor')}."
        )
        svg = svg_number_strip([f"n={n_cnt}", "Hermite", "Σ = ?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Easy", bp8,
            q_en, q_ar, ans,
            [n_cnt * math.floor(x_frac), ans - n_cnt // x_frac.denominator, ans + 3, ans - 2],
            f"Apply Hermite's identity {m('\\sum_{k=0}^{n-1} \\lfloor x + k/n \\rfloor = \\lfloor nx \\rfloor')}.",
            f"طبّق متطابقة هيرميت {m('\\sum_{k=0}^{n-1} \\lfloor x + k/n \\rfloor = \\lfloor nx \\rfloor')}.",
            "Hermite's identity collapses an n-term shifted floor sum into a single floor floor(nx).",
            [
                f"Identify {m(f'x = \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}}')} and {m(f'n = {n_cnt}')} in Hermite's identity.",
                f"Multiply: {m(f'nx = {n_cnt} \\cdot \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}} = {n_cnt * x_frac}')}.",
                f"Taking the floor gives {m(f'\\lfloor nx \\rfloor = {ans}')}.",
            ],
            f"Comparing with the naive lower bound {m(f'{n_cnt}\\lfloor x \\rfloor = {n_cnt * math.floor(x_frac)}')}, the fractional shifts add {m(str(ans - n_cnt * math.floor(x_frac)))}.",
            "تختزل متطابقة هيرميت مجموع الأجزاء الصحيحة المزاحة إلى جزء صحيح واحد.",
            [
                f"نحدد {m(f'x = \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}}')} و{m(f'n = {n_cnt}')} في متطابقة هيرميت.",
                f"نحسب الجداء: {m(f'nx = {n_cnt} \\cdot \\frac{{{x_frac.numerator}}}{{{x_frac.denominator}}} = {n_cnt * x_frac}')}.",
                f"بأخذ الجزء الصحيح نحصل على {m(f'\\lfloor nx \\rfloor = {ans}')}.",
            ],
            f"الحدود المزاحة تضيف {m(str(ans - n_cnt * math.floor(x_frac)))} فوق الحد الأدنى البسيط {m(str(n_cnt * math.floor(x_frac)))}.",
            diagram_en=svg,
        ))

    # Medium (111..115): Floor-fractional real equations a*floor(x) + b*{x} = c, find sum of all real solutions
    floor_med = [
        (2, 5, 11),  # 2n + 5r = 11, 0<=r<1 => 5r = 11 - 2n in [0, 5) => n in {4, 5}: n=4,r=3/5 -> 23/5; n=5,r=1/5 -> 26/5; sum = 49/5
        (3, 7, 17),  # 7r = 17 - 3n in [0, 7) => n in {4, 5}: n=4,r=5/7 -> 33/7; n=5,r=2/7 -> 37/7; sum = 70/7 = 10
        (2, 7, 15),  # 7r = 15 - 2n in [0, 7) => n in {5, 6, 7}: r=5/7,3/7,1/7 -> x=40/7,45/7,50/7 -> sum = 135/7
        (3, 8, 20),  # 8r = 20 - 3n in [0, 8) => n in {5, 6}: r=5/8, 2/8 -> x=45/8, 25/4=50/8 -> sum = 95/8
        (4, 9, 25),  # 9r = 25 - 4n in [0, 9) => n in {5, 6}: r=5/9, 1/9 -> x=50/9, 55/9 -> sum = 105/9 = 35/3
    ]
    for offset, (a_fl, b_fr, c_val) in enumerate(floor_med, 111):
        qid = f"OLYM-T2-{offset:03d}"
        sols = []
        for n_int in range(-50, 50):
            r_frac = Fraction(c_val - a_fl * n_int, b_fr)
            if 0 <= r_frac < 1:
                x_sol = n_int + r_frac
                assert math.floor(x_sol) == n_int and a_fl * math.floor(x_sol) + b_fr * (x_sol - math.floor(x_sol)) == c_val
                sols.append(x_sol)
        assert len(sols) >= 2
        tot = sum(sols, Fraction(0))
        ans = tot if tot.denominator != 1 else int(tot)
        sols_tex = ", ".join(fmt for fmt in (str(s) for s in sols))
        q_en = (
            f"Let {m('\\lfloor x \\rfloor')} denote the greatest integer {m('\\le x')} and {m('\\{x\\} = x - \\lfloor x \\rfloor')} "
            f"its fractional part. Find the sum of all real solutions {m('x')} to {m(f'{a_fl}\\lfloor x \\rfloor + {b_fr}\\{{x\\}} = {c_val}')}."
        )
        q_ar = (
            f"يرمز {m('\\lfloor x \\rfloor')} إلى أكبر عدد صحيح {m('\\le x')} ويرمز {m('\\{x\\} = x - \\lfloor x \\rfloor')} "
            f"إلى الجزء الكسري. أوجد مجموع جميع الحلول الحقيقية {m('x')} للمعادلة {m(f'{a_fl}\\lfloor x \\rfloor + {b_fr}\\{{x\\}} = {c_val}')}."
        )
        svg = svg_digit_slots(["x=n+r", "0≤r<1", "Σx = ?"], top_note="Floor Eq")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Medium", bp8,
            q_en, q_ar, ans,
            [sols[0], sols[-1], tot + 1, Fraction(c_val, a_fl)],
            f"Write {m('x = n + r')} with integer {m('n')} and {m('0 \\le r < 1')}, so {m(f'0 \\le {c_val} - {a_fl}n < {b_fr}')}.",
            f"ضع {m('x = n + r')} لعدد صحيح {m('n')} وكسر {m('0 \\le r < 1')}، فيكون {m(f'0 \\le {c_val} - {a_fl}n < {b_fr}')}.",
            "Bound the fractional term b{x} in [0, b) to isolate the finitely many valid integer parts n = floor(x).",
            [
                f"Set {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} and {m('r = \\{x\\} \\in [0, 1)')}, giving {m(f'{b_fr}r = {c_val} - {a_fl}n \\in [0, {b_fr})')}.",
                f"Solving {m(f'{c_val - b_fr} < {a_fl}n \\le {c_val}')} gives valid integers {m('n')}, yielding solutions {m(sols_tex)}.",
                f"Summing all valid real solutions gives {m(f'{tot}')}.",
            ],
            f"Each solution satisfies {m('0 \\le \\{x\\} < 1')} and reproduces {m(str(c_val))} upon substitution.",
            "نحصر الحد الكسري b{x} في الفترة [0, b) لتحديد القيم الصحيحة الممكنة للجزء الصحيح.",
            [
                f"نضع {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} و{m('r = \\{x\\} \\in [0, 1)')} فنجد {m(f'{b_fr}r = {c_val} - {a_fl}n \\in [0, {b_fr})')}.",
                f"بحل المتباينة نحصل على قيم {m('n')} الصحيحة ومنها الحلول {m(sols_tex)}.",
                f"بجمع جميع الحلول الحقيقية نحصل على {m(f'{tot}')}.",
            ],
            f"كل حل يحقق {m('0 \\le \\{x\\} < 1')} ويعطي {m(str(c_val))} عند التعويض.",
            diagram_en=svg,
        ))

    # Hard (116..120): Block floor sums & equal-quotient integer counting
    # 116..118: sum_{k=1}^{m^2 - 1} floor(sqrt(k)) = sum_{j=1}^{m-1} j(2j + 1)
    sqrt_sum_cases = [10, 12, 14]  # N = 99, 143, 195
    for idx_sub, m_sq in enumerate(sqrt_sum_cases):
        offset = 116 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        N_top = m_sq * m_sq - 1
        ans = sum(math.isqrt(k) for k in range(1, N_top + 1))
        formula_val = (m_sq - 1) * m_sq * (4 * m_sq + 1) // 6 - (m_sq - 1) * m_sq // 2
        # Wait: sum_{j=1}^{m-1} (2j^2 + j) = 2*(m-1)m(2m-1)/6 + (m-1)m/2 = (m-1)m(4m+1)/6
        exact_closed = (m_sq - 1) * m_sq * (4 * m_sq + 1) // 6
        assert ans == exact_closed
        q_en = (
            f"In an Intermediate Olympiad summation problem, compute the exact value of "
            f"{m(f'\\sum_{{k=1}}^{{{N_top}}} \\lfloor \\sqrt{{k}} \\rfloor')}."
        )
        q_ar = (
            f"في مسألة مجاميع للأولمبياد المتوسط، احسب القيمة الدقيقة للمجموع "
            f"{m(f'\\sum_{{k=1}}^{{{N_top}}} \\lfloor \\sqrt{{k}} \\rfloor')}."
        )
        svg = svg_olym_pigeonhole_boxes(4, f"k≤{N_top}", "Σ = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Hard", bp8,
            q_en, q_ar, ans,
            [ans - (2 * m_sq - 1), ans + m_sq, (m_sq - 1) * N_top // 2, ans - m_sq],
            f"Group {m('k')} into intervals {m('[j^2, (j+1)^2 - 1]')} of length {m('2j + 1')} on which {m('\\lfloor \\sqrt{k} \\rfloor = j')}.",
            f"قسّم قيم {m('k')} إلى الفترات {m('[j^2, (j+1)^2 - 1]')} التي طول كل منها {m('2j + 1')} ويثبت عليها {m('\\lfloor \\sqrt{k} \\rfloor = j')}.",
            "Partition the index range between consecutive perfect squares so floor(sqrt(k)) is constant on each block.",
            [
                f"For each {m(f'1 \\le j \\le {m_sq - 1}')}, {m('\\lfloor \\sqrt{k} \\rfloor = j')} on {m('[j^2, (j+1)^2 - 1]')}, containing {m('2j + 1')} integers.",
                f"Thus the sum equals {m(f'\\sum_{{j=1}}^{{{m_sq - 1}}} j(2j + 1) = 2\\sum_{{j=1}}^{{{m_sq - 1}}} j^2 + \\sum_{{j=1}}^{{{m_sq - 1}}} j')}.",
                f"Using standard power-sum formulas gives {m(f'\\frac{{({m_sq - 1})({m_sq})(4 \\cdot {m_sq} + 1)}}{{6}} = {ans}')}.",
            ],
            f"The top block {m(f'j = {m_sq - 1}')} spans {m(f'[{(m_sq - 1)**2}, {N_top}]')} of size {m(str(2 * m_sq - 1))}, matching {m(str(N_top))} exactly.",
            "نجزئ مدى المجموع بين المربعات الكاملة المتتالية حيث تثبت قيمة الجزء الصحيح للجذر.",
            [
                f"لكل {m(f'1 \\le j \\le {m_sq - 1}')} يكون {m('\\lfloor \\sqrt{k} \\rfloor = j')} على {m('2j + 1')} عدداً صحيحاً في الفترة {m('[j^2, (j+1)^2 - 1]')}.",
                f"يتحول المجموع إلى {m(f'\\sum_{{j=1}}^{{{m_sq - 1}}} (2j^2 + j)')}.",
                f"بتطبيق صيغ مجاميع القوى القياسية نحصل على {m(f'\\frac{{({m_sq - 1})({m_sq})({4 * m_sq + 1})}}{{6}} = {ans}')}.",
            ],
            f"الفترة الأخيرة تنتهي عند {m(str(N_top))} تماماً مما يؤكد شمول جميع الحدود.",
            diagram_en=svg,
        ))

    # 119..120: Count positive integers n satisfying floor(n / a) = floor(n / b)
    eq_quot_cases = [(5, 7), (7, 10)]
    for idx_sub, (a_div, b_div) in enumerate(eq_quot_cases):
        offset = 119 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        valid_ns = [n for n in range(1, 5000) if n // a_div == n // b_div]
        ans = len(valid_ns)
        # Let q = floor(n/a) = floor(n/b): interval [qa, (q+1)a - 1] cap [qb, (q+1)b - 1] (excluding n=0 for q=0)
        q_en = (
            f"How many positive integers {m('n')} satisfy the floor equation "
            f"{m(f'\\left\\lfloor \\frac{{n}}{{{a_div}}} \\right\\rfloor = \\left\\lfloor \\frac{{n}}{{{b_div}}} \\right\\rfloor')}?"
        )
        q_ar = (
            f"كم عدداً صحيحاً موجباً {m('n')} يحقق معادلة الجزء الصحيح "
            f"{m(f'\\left\\lfloor \\frac{{n}}{{{a_div}}} \\right\\rfloor = \\left\\lfloor \\frac{{n}}{{{b_div}}} \\right\\rfloor')}؟"
        )
        svg = svg_digit_slots([f"⌊n/{a_div}⌋", "=", f"⌊n/{b_div}⌋", "#=?"], top_note="Quotients")
        qs.append(make_olym_q(
            qid, LEVEL, "Algebra", "Hard", bp8,
            q_en, q_ar, ans,
            [ans + 1, ans - 1, a_div * b_div, ans + a_div],
            f"Set {m(f'q = \\lfloor n/{a_div} \\rfloor = \\lfloor n/{b_div} \\rfloor \\ge 0')} and intersect {m(f'[{a_div}q, {a_div}q + {a_div - 1}]')} with {m(f'[{b_div}q, {b_div}q + {b_div - 1}]')}.",
            f"ضع {m(f'q = \\lfloor n/{a_div} \\rfloor = \\lfloor n/{b_div} \\rfloor \\ge 0')} وقاطع الفترتين {m(f'[{a_div}q, {a_div}q + {a_div - 1}]')} و{m(f'[{b_div}q, {b_div}q + {b_div - 1}]')}.",
            "Group solutions by their common integer quotient q >= 0 and sum the overlap lengths max(0, a - (b - a)q).",
            [
                f"Let {m('q \\ge 0')} be the common floor value, so {m(f'{b_div}q \\le n \\le {a_div}q + {a_div - 1}')}.",
                f"For {m('q = 0')}, positive integers are {m(f'1 \\le n \\le {a_div - 1}')} ({m(str(a_div - 1))} values); for {m('q \\ge 1')}, each valid {m('q')} contributes {m(f'\\max(0, {a_div} - {b_div - a_div}q)')} integers.",
                f"Summing over all non-empty overlaps gives {m(str(ans))} positive integers.",
            ],
            f"For {m(f'{b_div}q > {a_div}q + {a_div - 1}')}, the intervals become disjoint so no larger {m('n')} can exist.",
            "نجمّع الأعداد حسب خارج القسمة المشترك q ثم نجمع أطوال تقاطعات الفترات غير الخالية.",
            [
                f"نضع {m('q \\ge 0')} القيمة المشتركة للجزء الصحيح فيجب أن يتحقق {m(f'{b_div}q \\le n \\le {a_div}q + {a_div - 1}')}.",
                f"عند {m('q = 0')} لدينا {m(str(a_div - 1))} أعداد موجبة، ولكل {m('q \\ge 1')} يضيف التقاطع {m(f'\\max(0, {a_div} - {b_div - a_div}q)')} أعداد.",
                f"بجمع أطوال التقاطعات غير الخالية نحصل على {m(str(ans))} عدداً صحيحاً موجباً.",
            ],
            f"عندما يصبح {m(f'{b_div}q > {a_div}q + {a_div - 1}')} تنفصل الفترتان فلا توجد حلول أكبر.",
            diagram_en=svg,
        ))

    return qs


# ==============================================================================
# UNIT 2.3 — Inequalities (OLYM-T2-121 .. OLYM-T2-180)
# ==============================================================================

def _gen_u23_inequalities() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 9: olym_t2_ineq_weighted_amgm (OLYM-T2-121..135)
    # ------------------------------------------------------------------
    bp9 = "olym_t2_ineq_weighted_amgm"

    # Easy (121..125): Term-splitting AM-GM minimum of a*x + b/x^2 for x > 0
    amgm_easy = [
        (2, 27, 3),   # x + x + 27/x^2 >= 3*3 = 9 at x=3
        (4, 16, 2),   # 2x + 2x + 16/x^2 >= 3*4 = 12 at x=2
        (10, 5, 1),   # 5x + 5x + 5/x^2 >= 3*5 = 15 at x=1
        (6, 24, 2),   # 3x + 3x + 24/x^2 >= 3*6 = 18 at x=2
        (8, 32, 2),   # 4x + 4x + 32/x^2 >= 3*8 = 24 at x=2
    ]
    for offset, (a_lin, b_inv, x_eq) in enumerate(amgm_easy, 121):
        qid = f"OLYM-T2-{offset:03d}"
        half_a = a_lin // 2
        prod_cube = half_a * half_a * b_inv
        cbrt_val = round(prod_cube ** (1 / 3))
        assert cbrt_val**3 == prod_cube
        ans = 3 * cbrt_val
        assert a_lin * x_eq + b_inv // (x_eq * x_eq) == ans
        for num in range(1, 30):
            xv = Fraction(num, 4)
            assert a_lin * xv + Fraction(b_inv, 1) / (xv * xv) >= ans
        q_en = (
            f"Over all positive real numbers {m('x > 0')}, find the minimum value of "
            f"{m(f'{a_lin}x + \\frac{{{b_inv}}}{{x^2}}')}."
        )
        q_ar = (
            f"على جميع الأعداد الحقيقية الموجبة {m('x > 0')}، أوجد القيمة الصغرى للمقدار "
            f"{m(f'{a_lin}x + \\frac{{{b_inv}}}{{x^2}}')}."
        )
        svg = svg_olym_inequality_curve(f"{half_a}x", f"{b_inv}/x²", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Easy", bp9,
            q_en, q_ar, ans,
            [a_lin + b_inv, 2 * cbrt_val, ans - 3, ans + 3],
            f"Split {m(f'{a_lin}x = {half_a}x + {half_a}x')} so that the product with {m(f'{b_inv}/x^2')} cancels {m('x')}.",
            f"جزّئ الحد الخطي إلى {m(f'{a_lin}x = {half_a}x + {half_a}x')} لكي يختصر المتغير {m('x')} في حاصل الضرب.",
            "Split the linear term into two equal halves and apply the 3-term AM-GM inequality.",
            [
                f"Rewrite the expression as three positive terms: {m(f'{half_a}x + {half_a}x + \\frac{{{b_inv}}}{{x^2}}')}.",
                f"By 3-term AM-GM, the sum is at least {m(f'3\\sqrt[3]{{{half_a}x \\cdot {half_a}x \\cdot \\frac{{{b_inv}}}{{x^2}}}} = 3\\sqrt[3]{{{prod_cube}}} = {ans}')}.",
                f"Equality holds when {m(f'{half_a}x = \\frac{{{b_inv}}}{{x^2}}')}, which occurs at {m(f'x = {x_eq} > 0')}.",
            ],
            f"At {m(f'x = {x_eq}')}, {m(f'{a_lin}({x_eq}) + {b_inv}/{x_eq}^2 = {ans}')}, confirming the minimum is attained.",
            "نجزّئ الحد الخطي إلى حدين متساويين ثم نطبق متباينة الوسط الحسابي والهندسي لثلاثة حدود.",
            [
                f"نعيد كتابة المقدار على صورة ثلاثة حدود موجبة: {m(f'{half_a}x + {half_a}x + \\frac{{{b_inv}}}{{x^2}}')}.",
                f"بتطبيق متباينة AM-GM لثلاثة حدود يكون المجموع أكبر من أو يساوي {m(f'3\\sqrt[3]{{{prod_cube}}} = {ans}')}.",
                f"تتحقق المساواة عندما {m(f'{half_a}x = \\frac{{{b_inv}}}{{x^2}}')} أي عند {m(f'x = {x_eq} > 0')}.",
            ],
            f"بالتعويض عند {m(f'x = {x_eq}')} نجد القيمة {m(str(ans))} تماماً.",
            diagram_en=svg,
        ))

    # Medium (126..130): Constrained weighted AM-GM maximizing x^p * y^q given a*x + b*y = S
    amgm_med = [
        (2, 1, 1, 1, 9),    # x + y = 9 -> max x^2 y at x=6, y=3 -> 108
        (2, 1, 1, 2, 12),   # x + 2y = 12 -> max x^2 y at x=8, y=2 -> 128
        (2, 2, 1, 3, 12),   # x + 3y = 12 -> max x^2 y^2 at x=6, y=2 -> 144
        (1, 3, 1, 1, 8),    # x + y = 8 -> max x y^3 at x=2, y=6 -> 432
        (3, 1, 2, 1, 16),   # 2x + y = 16 -> max x^3 y at x=6, y=4 -> 864
    ]
    for offset, (p_exp, q_exp, a_c, b_c, S_tot) in enumerate(amgm_med, 126):
        qid = f"OLYM-T2-{offset:03d}"
        n_parts = p_exp + q_exp
        part_val = Fraction(S_tot, n_parts)
        x_star = part_val * p_exp / a_c
        y_star = part_val * q_exp / b_c
        assert x_star.denominator == 1 and y_star.denominator == 1
        xi, yi = int(x_star), int(y_star)
        ans = (xi**p_exp) * (yi**q_exp)
        for tx in range(1, S_tot * 4):
            xv = Fraction(tx, 4 * a_c)
            yv = (S_tot - a_c * xv) / b_c
            if yv > 0:
                assert (xv**p_exp) * (yv**q_exp) <= ans
        ax_str = "x" if a_c == 1 else f"{a_c}x"
        by_str = "y" if b_c == 1 else f"{b_c}y"
        xp_str = "x" if p_exp == 1 else f"x^{{{p_exp}}}"
        yq_str = "y" if q_exp == 1 else f"y^{{{q_exp}}}"
        q_en = (
            f"Positive real numbers {m('x')} and {m('y')} satisfy {m(f'{ax_str} + {by_str} = {S_tot}')}. "
            f"Find the maximum possible value of {m(f'{xp_str}{yq_str}')}."
        )
        q_ar = (
            f"عددان حقيقيان موجبان {m('x')} و{m('y')} يحققان {m(f'{ax_str} + {by_str} = {S_tot}')}. "
            f"أوجد أكبر قيمة ممكنة للمقدار {m(f'{xp_str}{yq_str}')}."
        )
        svg = svg_olym_inequality_curve(ax_str, by_str, "max=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Medium", bp9,
            q_en, q_ar, ans,
            [ans // 2, ans - 16, ((S_tot // (2 * a_c)) ** p_exp) * ((S_tot // (2 * b_c)) ** q_exp) if S_tot // (2 * a_c) > 0 and ((S_tot // (2 * a_c)) ** p_exp) * ((S_tot // (2 * b_c)) ** q_exp) != ans else ans + 24, ans + 36],
            f"Split {m(ax_str)} into {m(str(p_exp))} equal parts and {m(by_str)} into {m(str(q_exp))} equal parts, then apply {m(f'{n_parts}')}-term AM-GM.",
            f"جزّئ {m(ax_str)} إلى {m(str(p_exp))} أجزاء متساوية و{m(by_str)} إلى {m(str(q_exp))} أجزاء متساوية ثم طبّق AM-GM لـ {m(str(n_parts))} حدود.",
            "Balance exponents in AM-GM by dividing each linear term into as many equal pieces as its target exponent.",
            [
                f"Write {m(f'{S_tot} = {p_exp} \\cdot \\left(\\frac{{{ax_str}}}{{{p_exp}}}\\right) + {q_exp} \\cdot \\left(\\frac{{{by_str}}}{{{q_exp}}}\\right)')} ({m(str(n_parts))} positive terms).",
                f"By {m(str(n_parts))}-term AM-GM, each piece equals {m(f'{S_tot}/{n_parts} = {int(part_val)}')} at maximum.",
                f"Thus {m(f'x = {xi}')}, {m(f'y = {yi}')}, giving maximum {m(f'{xi}^{{{p_exp}}} \\cdot {yi}^{{{q_exp}}} = {ans}')}.",
            ],
            f"At {m(f'(x, y) = ({xi}, {yi})')}, {m(f'{ax_str} + {by_str} = {a_c * xi + b_c * yi} = {S_tot}')} holds with equality.",
            "نوازن الأسس في متباينة AM-GM بتجزئة كل حد خطي بعدد يساوي أسّه في الجداء المطلوب.",
            [
                f"نكتب {m(f'{S_tot}')} كمجموع {m(str(n_parts))} حدود موجبة: {m(str(p_exp))} نسخ من {m(f'\\frac{{{ax_str}}}{{{p_exp}}}')} و{m(str(q_exp))} نسخ من {m(f'\\frac{{{by_str}}}{{{q_exp}}}')}.",
                f"تتحقق القيمة العظمى عندما تتساوى الأجزاء جميعها وتساوي {m(f'{S_tot}/{n_parts} = {int(part_val)}')}.",
                f"ومنه {m(f'x = {xi}')} و{m(f'y = {yi}')}، فتكون القيمة العظمى {m(str(ans))}.",
            ],
            f"عند النقطة {m(f'({xi}, {yi})')} يتحقق الشرط الخطي {m(f'{a_c * xi + b_c * yi} = {S_tot}')}.",
            diagram_en=svg,
        ))

    # Hard (131..135): Shifted 4-term AM-GM minimum of a*x + b/(x - k)^3 for x > k
    amgm_hard = [
        (3, 1, 2, 3),    # 3(x-2) + 1/(x-2)^3 + 6 >= 4*1 + 6 = 10 at x=3
        (3, 16, 1, 3),   # 3(x-1) + 16/(x-1)^3 + 3 >= 4*2 + 3 = 11 at x=3
        (3, 81, 4, 7),   # 3(x-4) + 81/(x-4)^3 + 12 >= 4*3 + 12 = 24 at x=7
        (6, 2, 3, 4),    # 6(x-3) + 2/(x-3)^3 + 18 = 2t+2t+2t+2/t^3+18 >= 4*2+18 = 26 at x=4
        (9, 3, 2, 3),    # 9(x-2) + 3/(x-2)^3 + 18 = 3t+3t+3t+3/t^3+18 >= 4*3+18 = 30 at x=3
    ]
    for offset, (a_slp, b_num, k_sh, x_opt) in enumerate(amgm_hard, 131):
        qid = f"OLYM-T2-{offset:03d}"
        u_coef = a_slp // 3
        p4 = (u_coef**3) * b_num
        r4 = round(p4 ** 0.25)
        assert r4**4 == p4
        ans = 4 * r4 + a_slp * k_sh
        assert a_slp * x_opt + Fraction(b_num, (x_opt - k_sh) ** 3) == ans
        q_en = (
            f"In an Intermediate Olympiad optimization problem, let {m(f'x > {k_sh}')} be a real number. "
            f"Find the minimum value of {m(f'{a_slp}x + \\frac{{{b_num}}}{{(x - {k_sh})^3}}')}."
        )
        q_ar = (
            f"في مسألة تحسين للأولمبياد المتوسط، ليكن {m(f'x > {k_sh}')} عدداً حقيقياً. "
            f"أوجد القيمة الصغرى للمقدار {m(f'{a_slp}x + \\frac{{{b_num}}}{{(x - {k_sh})^3}}')}."
        )
        svg = svg_olym_inequality_curve(f"x−{k_sh}", "1/t³", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Hard", bp9,
            q_en, q_ar, ans,
            [4 * r4, ans - a_slp, ans + 4, a_slp * (k_sh + 1) + b_num if a_slp * (k_sh + 1) + b_num != ans else ans - 2],
            f"Substitute {m(f't = x - {k_sh} > 0')} to rewrite {m(f'{a_slp}x = {u_coef}t + {u_coef}t + {u_coef}t + {a_slp * k_sh}')}.",
            f"ضع {m(f't = x - {k_sh} > 0')} وأعد كتابة {m(f'{a_slp}x = {u_coef}t + {u_coef}t + {u_coef}t + {a_slp * k_sh}')}.",
            "Shift to t = x - k > 0 and split the linear term into three equal parts to cancel t^3 in 4-term AM-GM.",
            [
                f"Let {m(f't = x - {k_sh} > 0')}, so the expression becomes {m(f'{u_coef}t + {u_coef}t + {u_coef}t + \\frac{{{b_num}}}{{t^3}} + {a_slp * k_sh}')}.",
                f"Apply 4-term AM-GM to the first four terms: {m(f'3({u_coef}t) + \\frac{{{b_num}}}{{t^3}} \\ge 4\\sqrt[4]{{{u_coef}^3 \\cdot {b_num}}} = {4 * r4}')}.",
                f"Adding the constant {m(str(a_slp * k_sh))} gives minimum {m(f'{4 * r4} + {a_slp * k_sh} = {ans}')}, attained at {m(f'x = {x_opt}')}.",
            ],
            f"At {m(f'x = {x_opt}')}, {m(f't = {x_opt - k_sh}')} and {m(f'{u_coef}t = {b_num}/t^3 = {r4}')}, confirming equality.",
            "نزيح المتغير بوضع t = x - k > 0 ثم نجزّئ الحد الخطي إلى ثلاثة أجزاء متساوية لتطبيق AM-GM لأربعة حدود.",
            [
                f"نضع {m(f't = x - {k_sh} > 0')} فيصبح المقدار {m(f'{u_coef}t + {u_coef}t + {u_coef}t + \\frac{{{b_num}}}{{t^3}} + {a_slp * k_sh}')}.",
                f"بتطبيق متباينة AM-GM لأربعة حدود على الحدود الأربعة الأولى نجد أنها أكبر من أو تساوي {m(f'4\\sqrt[4]{{{p4}}} = {4 * r4}')}.",
                f"بإضافة الثابت {m(str(a_slp * k_sh))} نحصل على القيمة الصغرى {m(str(ans))} عند {m(f'x = {x_opt}')}.",
            ],
            f"عند {m(f'x = {x_opt}')} تتساوى الحدود الأربعة وتتحقق المساواة بدقة.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 10: olym_t2_ineq_cauchy_titu_lemma (OLYM-T2-136..150)
    # ------------------------------------------------------------------
    bp10 = "olym_t2_ineq_cauchy_titu_lemma"

    # Easy (136..140): Cauchy-Schwarz minimum of x^2 + y^2 + z^2 given ax + by + cz = S
    cs_easy = [
        (1, 2, 2, 18),   # norm^2 = 9, S=18 -> min = 36
        (2, 3, 6, 21),   # norm^2 = 49, S=21 -> min = 9
        (1, 4, 8, 27),   # norm^2 = 81, S=27 -> min = 9? Pick S=36 -> min = 16
        (2, 6, 9, 33),   # norm^2 = 121, S=33 -> min = 9? Pick S=44 -> min = 16? Pick S=55 -> min = 25
        (3, 4, 12, 52),  # norm^2 = 169, S=52 -> min = 16? Pick S=65 -> min = 25? Let's make all 5 distinct!
    ]
    cs_easy = [
        (1, 2, 2, 15),   # 225 / 9 = 25
        (2, 3, 6, 28),   # 784 / 49 = 16
        (1, 4, 8, 54),   # 2916 / 81 = 36
        (2, 6, 9, 77),   # 5929 / 121 = 49
        (3, 4, 12, 104), # 10816 / 169 = 64
    ]
    for offset, (ca, cb, cc, S_lin) in enumerate(cs_easy, 136):
        qid = f"OLYM-T2-{offset:03d}"
        norm2 = ca * ca + cb * cb + cc * cc
        ans_f = Fraction(S_lin * S_lin, norm2)
        assert ans_f.denominator == 1
        ans = int(ans_f)
        a_s = "x" if ca == 1 else f"{ca}x"
        q_en = (
            f"Real numbers {m('x, y, z')} satisfy {m(f'{a_s} + {cb}y + {cc}z = {S_lin}')}. "
            f"By the Cauchy–Schwarz inequality, what is the minimum possible value of {m('x^2 + y^2 + z^2')}?"
        )
        q_ar = (
            f"تحقق الأعداد الحقيقية {m('x, y, z')} المعادلة {m(f'{a_s} + {cb}y + {cc}z = {S_lin}')}. "
            f"باستخدام متباينة كوشي-شفارتز، ما القيمة الصغرى الممكنة للمقدار {m('x^2 + y^2 + z^2')}؟"
        )
        svg = svg_olym_inequality_curve("u·v", "|u||v|", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Easy", bp10,
            q_en, q_ar, ans,
            [S_lin, ans - 9, ans + 11, norm2],
            f"Apply Cauchy–Schwarz: {m(f'({ca}^2 + {cb}^2 + {cc}^2)(x^2 + y^2 + z^2) \\ge ({a_s} + {cb}y + {cc}z)^2')}.",
            f"طبّق متباينة كوشي-شفارتز: {m(f'({ca}^2 + {cb}^2 + {cc}^2)(x^2 + y^2 + z^2) \\ge ({a_s} + {cb}y + {cc}z)^2')}.",
            "Bound the sum of squares from below using the squared dot product divided by the coefficient norm squared.",
            [
                f"By Cauchy–Schwarz, {m(f'({ca}^2 + {cb}^2 + {cc}^2)(x^2 + y^2 + z^2) \\ge ({S_lin})^2')}.",
                f"Compute the sum of squared coefficients: {m(f'{ca}^2 + {cb}^2 + {cc}^2 = {norm2}')}.",
                f"Divide both sides by {m(str(norm2))}: {m(f'x^2 + y^2 + z^2 \\ge \\frac{{{S_lin}^2}}{{{norm2}}} = {ans}')}.",
            ],
            f"Equality holds when {m(f'(x, y, z) = \\frac{{{S_lin}}}{{{norm2}}}({ca}, {cb}, {cc})')}.",
            "نحدّ مجموع المربعات من الأسفل بقسمة مربع المجموع الخطي على مجموع مربعات المعاملات.",
            [
                f"بموجب متباينة كوشي-شفارتز: {m(f'({ca}^2 + {cb}^2 + {cc}^2)(x^2 + y^2 + z^2) \\ge {S_lin}^2')}.",
                f"نحسب مجموع مربعات المعاملات: {m(f'{ca}^2 + {cb}^2 + {cc}^2 = {norm2}')}.",
                f"بالقسمة على {m(str(norm2))} نجد {m(f'x^2 + y^2 + z^2 \\ge \\frac{{{S_lin}^2}}{{{norm2}}} = {ans}')}.",
            ],
            f"تتحقق المساواة عندما تتناسب {m('(x, y, z)')} طردياً مع {m(f'({ca}, {cb}, {cc})')}.",
            diagram_en=svg,
        ))

    # Medium (141..145): Titu's Lemma p^2/x + q^2/y + r^2/z for x + y + z = S
    titu_med = [
        (2, 3, 5, 20),   # (2+3+5)^2 / 20 = 100 / 20 = 5
        (1, 3, 8, 18),   # 144 / 18 = 8
        (2, 4, 9, 15),   # 225 / 15 = 15
        (3, 5, 7, 9),    # 225 / 9 = 25
        (3, 6, 11, 16),  # 400 / 16 = 25 -> pick S=10: 400 / 10 = 40
    ]
    titu_med[-1] = (3, 6, 11, 10)
    for offset, (p_n, q_n, r_n, S_den) in enumerate(titu_med, 141):
        qid = f"OLYM-T2-{offset:03d}"
        sum_num = p_n + q_n + r_n
        ans_f = Fraction(sum_num * sum_num, S_den)
        ans = int(ans_f) if ans_f.denominator == 1 else ans_f
        x_eq = Fraction(p_n * S_den, sum_num)
        y_eq = Fraction(q_n * S_den, sum_num)
        z_eq = Fraction(r_n * S_den, sum_num)
        assert Fraction(p_n**2, 1) / x_eq + Fraction(q_n**2, 1) / y_eq + Fraction(r_n**2, 1) / z_eq == ans_f
        q_en = (
            f"For positive real numbers {m('x, y, z')} satisfying {m(f'x + y + z = {S_den}')}, "
            f"find the minimum value of {m(f'\\frac{{{p_n**2}}}{{x}} + \\frac{{{q_n**2}}}{{y}} + \\frac{{{r_n**2}}}{{z}}')}."
        )
        q_ar = (
            f"للأعداد الحقيقية الموجبة {m('x, y, z')} التي تحقق {m(f'x + y + z = {S_den}')}، "
            f"أوجد القيمة الصغرى للمقدار {m(f'\\frac{{{p_n**2}}}{{x}} + \\frac{{{q_n**2}}}{{y}} + \\frac{{{r_n**2}}}{{z}}')}."
        )
        svg = svg_olym_inequality_curve("p²/x", "q²/y", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Medium", bp10,
            q_en, q_ar, ans,
            [Fraction(p_n**2 + q_n**2 + r_n**2, S_den) * 3, ans_f + 3, ans_f - 2 if ans_f > 2 else ans_f + 5, sum_num],
            f"Apply Titu's Lemma (Engel's form): {m(f'\\frac{{{p_n}^2}}{{x}} + \\frac{{{q_n}^2}}{{y}} + \\frac{{{r_n}^2}}{{z}} \\ge \\frac{{({p_n} + {q_n} + {r_n})^2}}{{x + y + z}}')}.",
            f"طبّق توطئة تيتو (صورة إنغل): {m(f'\\frac{{{p_n}^2}}{{x}} + \\frac{{{q_n}^2}}{{y}} + \\frac{{{r_n}^2}}{{z}} \\ge \\frac{{({p_n} + {q_n} + {r_n})^2}}{{x + y + z}}')}.",
            "Titu's Lemma bounds a sum of squares over positive denominators by the square of summed numerators over summed denominators.",
            [
                f"Write the numerators as squares: {m(f'{p_n}^2, {q_n}^2, {r_n}^2')}.",
                f"By Titu's Lemma, the sum is at least {m(f'\\frac{{({p_n} + {q_n} + {r_n})^2}}{{x + y + z}} = \\frac{{{sum_num}^2}}{{{S_den}}} = {ans}')}.",
                f"Equality holds at {m(f'(x, y, z) = ({x_eq}, {y_eq}, {z_eq})')}, all strictly positive.",
            ],
            f"Summing the equality coordinates gives {m(f'{x_eq} + {y_eq} + {z_eq} = {S_den}')}.",
            "تعطي توطئة تيتو حداً أدنى لمجموع مربعات على مقامات موجبة بمربع مجموع الجذور على مجموع المقامات.",
            [
                f"نكتب البسوط على صورة مربعات كاملة: {m(f'{p_n}^2, {q_n}^2, {r_n}^2')}.",
                f"بتطبيق توطئة تيتو نجد أن المجموع لا يقل عن {m(f'\\frac{{({p_n} + {q_n} + {r_n})^2}}{{{S_den}}} = {ans}')}.",
                f"تتحقق المساواة عند النقطة الموجبة {m(f'({x_eq}, {y_eq}, {z_eq})')}.",
            ],
            f"مجموع الإحداثيات عند التساوي يساوي {m(str(S_den))} تماماً.",
            diagram_en=svg,
        ))

    # Hard (146..150): Coupled-denominator Titu's Lemma p^2/(2a+b) + q^2/(2b+c) + r^2/(2c+a) with a+b+c = S
    titu_hard = [
        (3, 3, 3, 9),    # sum_num = 9, 3S = 27 -> 81/27 = 3 (a=b=c=3)
        (2, 3, 3, 8),    # 4p-2q+r=5>0, 4q-2r+p=8>0, 4r-2p+q=11>0! sum_num=8, 3S=24 -> 64/24 = 8/3
        (3, 4, 5, 8),    # 4(3)-8+5=9>0, 16-10+3=9>0, 20-6+4=18>0! sum_num=12, 3S=24 -> 144/24 = 6
        (4, 5, 6, 5),    # 16-10+6=12>0, 20-12+4=12>0, 24-8+5=21>0! sum_num=15, 3S=15 -> 225/15 = 15
        (5, 6, 7, 12),   # 20-12+7=15>0, 24-14+5=15>0, 28-10+6=24>0! sum_num=18, 3S=36 -> 324/36 = 9
    ]
    for offset, (p_n, q_n, r_n, S_abc) in enumerate(titu_hard, 146):
        qid = f"OLYM-T2-{offset:03d}"
        sum_num = p_n + q_n + r_n
        denom_sum = 3 * S_abc
        ans_f = Fraction(sum_num * sum_num, denom_sum)
        ans = int(ans_f) if ans_f.denominator == 1 else ans_f
        lam = Fraction(denom_sum, sum_num)
        u, v, w = lam * p_n, lam * q_n, lam * r_n
        a_eq = (4 * u - 2 * v + w) / 9
        b_eq = (4 * v - 2 * w + u) / 9
        c_eq = (4 * w - 2 * u + v) / 9
        assert a_eq > 0 and b_eq > 0 and c_eq > 0 and a_eq + b_eq + c_eq == S_abc
        assert Fraction(p_n**2, 1) / (2 * a_eq + b_eq) + Fraction(q_n**2, 1) / (2 * b_eq + c_eq) + Fraction(r_n**2, 1) / (2 * c_eq + a_eq) == ans_f
        q_en = (
            f"In an Intermediate Olympiad inequality, positive reals {m('a, b, c')} satisfy "
            f"{m(f'a + b + c = {S_abc}')}. Determine the minimum value of "
            f"{m(f'\\frac{{{p_n**2}}}{{2a + b}} + \\frac{{{q_n**2}}}{{2b + c}} + \\frac{{{r_n**2}}}{{2c + a}}')}."
        )
        q_ar = (
            f"في متباينة للأولمبياد المتوسط، تحقق الأعداد الحقيقية الموجبة {m('a, b, c')} الشرط "
            f"{m(f'a + b + c = {S_abc}')}. أوجد القيمة الصغرى للمقدار "
            f"{m(f'\\frac{{{p_n**2}}}{{2a + b}} + \\frac{{{q_n**2}}}{{2b + c}} + \\frac{{{r_n**2}}}{{2c + a}}')}."
        )
        svg = svg_olym_inequality_curve("2a+b", "Σ=3S", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Hard", bp10,
            q_en, q_ar, ans,
            [Fraction(sum_num * sum_num, S_abc), ans_f + 2, ans_f + 1, Fraction(p_n**2 + q_n**2 + r_n**2, S_abc)],
            f"Notice the denominators sum to {m(f'(2a + b) + (2b + c) + (2c + a) = 3(a + b + c) = {denom_sum}')}, then apply Titu's Lemma.",
            f"لاحظ أن مجموع المقامات هو {m(f'(2a + b) + (2b + c) + (2c + a) = 3(a + b + c) = {denom_sum}')} ثم طبّق توطئة تيتو.",
            "Sum the coupled cyclic denominators to 3(a + b + c) and apply Titu's Lemma, verifying interior positivity of the equality point.",
            [
                f"Sum the three denominators: {m(f'(2a + b) + (2b + c) + (2c + a) = 3(a + b + c) = {denom_sum}')}.",
                f"By Titu's Lemma, the expression is at least {m(f'\\frac{{({p_n} + {q_n} + {r_n})^2}}{{{denom_sum}}} = \\frac{{{sum_num}^2}}{{{denom_sum}}} = {ans_f}')}.",
                f"Solving {m(f'\\frac{{2a+b}}{{{p_n}}} = \\frac{{2b+c}}{{{q_n}}} = \\frac{{2c+a}}{{{r_n}}}')} yields strictly positive {m(f'(a, b, c) = ({a_eq}, {b_eq}, {c_eq})')}.",
            ],
            f"Positivity {m('a, b, c > 0')} guarantees the lower bound {m(f'{ans_f}')} is genuinely attained.",
            "نجمع المقامات الدورية المترابطة لنحصل على 3(a + b + c) ثم نطبق توطئة تيتو ونتحقق من موجبية نقطة التساوي.",
            [
                f"مجموع المقامات الثلاثة يساوي {m(f'3(a + b + c) = {denom_sum}')}.",
                f"بتطبيق توطئة تيتو يكون المقدار أكبر من أو يساوي {m(f'\\frac{{{sum_num}^2}}{{{denom_sum}}} = {ans_f}')}.",
                f"بحل شرط التساوي نجد النقطة الموجبة فعلياً {m(f'({a_eq}, {b_eq}, {c_eq})')}.",
            ],
            f"بما أن الإحداثيات الثلاثة موجبة تماماً فإن القيمة الصغرى {m(f'{ans_f}')} متحققة فعلاً.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 11: olym_t2_ineq_nesbitt_cyclic_sums (OLYM-T2-151..165)
    # ------------------------------------------------------------------
    bp11 = "olym_t2_ineq_nesbitt_cyclic_sums"

    # Easy (151..155): Shifted & scaled Nesbitt cyclic sums sum_{cyc} (alpha * a + beta*(b + c)) / (b + c)
    nesb_easy = [
        (2, 1),   # sum (2a + b + c)/(b + c) = 2*(3/2) + 3 = 6
        (4, 1),   # sum (4a + b + c)/(b + c) = 6 + 3 = 9
        (2, 3),   # sum (2a + 3b + 3c)/(b + c) = 3 + 9 = 12
        (6, -1),  # sum (6a - b - c)/(b + c) = 9 - 3 = 6 -> pick (6, 1) -> 9 + 3 = 12? Pick (6, -2) -> 9 - 6 = 3? Pick (1, 1) -> 9/2!
        (4, -1),  # sum (4a - b - c)/(b + c) = 6 - 3 = 3
    ]
    nesb_easy[3] = (1, 1)  # sum (a + b + c)/(b + c) = 3/2 + 3 = 9/2
    for offset, (alp, bet) in enumerate(nesb_easy, 151):
        qid = f"OLYM-T2-{offset:03d}"
        ans_f = Fraction(3 * alp, 2) + 3 * bet
        ans = int(ans_f) if ans_f.denominator == 1 else ans_f
        if alp == 1 and bet == 1:
            num_a = "a + b + c"
            num_b = "a + b + c"
            num_c = "a + b + c"
        else:
            b_sign = f"+ {bet}(b + c)" if bet > 0 else f"- {abs(bet)}(b + c)"
            c_sign = f"+ {bet}(c + a)" if bet > 0 else f"- {abs(bet)}(c + a)"
            a_sign = f"+ {bet}(a + b)" if bet > 0 else f"- {abs(bet)}(a + b)"
            if abs(bet) == 1:
                b_sign = "+ b + c" if bet > 0 else "- b - c"
                c_sign = "+ c + a" if bet > 0 else "- c - a"
                a_sign = "+ a + b" if bet > 0 else "- a - b"
            num_a = f"{alp}a {b_sign}"
            num_b = f"{alp}b {c_sign}"
            num_c = f"{alp}c {a_sign}"
        expr_tex = f"\\frac{{{num_a}}}{{b + c}} + \\frac{{{num_b}}}{{c + a}} + \\frac{{{num_c}}}{{a + b}}"
        q_en = (
            f"Over all positive real numbers {m('a, b, c > 0')}, find the minimum value of the cyclic sum "
            f"{m(expr_tex)}."
        )
        q_ar = (
            f"على جميع الأعداد الحقيقية الموجبة {m('a, b, c > 0')}، أوجد القيمة الصغرى للمجموع الدوري "
            f"{m(expr_tex)}."
        )
        svg = svg_olym_inequality_curve("a", "b+c", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Easy", bp11,
            q_en, q_ar, ans,
            [ans_f + 1, ans_f - 1 if ans_f > 1 else ans_f + 2, Fraction(3 * alp, 2), ans_f + Fraction(1, 2)],
            f"Separate each fraction to isolate Nesbitt's cyclic sum {m('\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b} \\ge \\frac{3}{2}')}.",
            f"افصل كل كسر لعزل مجموع نسبيت الدوري {m('\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b} \\ge \\frac{3}{2}')}.",
            "Decompose each fraction into a multiple of Nesbitt's term plus a constant.",
            [
                f"Split each term by its denominator: the sum equals {m(f'{alp}\\left(\\frac{{a}}{{b+c}} + \\frac{{b}}{{c+a}} + \\frac{{c}}{{a+b}}\\right) + 3({bet})')}.",
                f"By Nesbitt's inequality, {m('\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b} \\ge \\frac{3}{2}')} for all {m('a, b, c > 0')}.",
                f"Therefore the minimum value is {m(f'{alp} \\cdot \\frac{{3}}{{2}} + {3 * bet} = {ans_f}')}, attained when {m('a = b = c')}.",
            ],
            f"Testing {m('a = b = c = 1')} directly gives {m(f'3 \\cdot \\frac{{{alp + 2 * bet}}}{{2}} = {ans_f}')}.",
            "نفكك كل كسر إلى مضاعف لحدّ نسبيت مضافاً إليه ثابت عددي.",
            [
                f"بقسمة حدود البسط على المقام يتحول المجموع إلى {m(f'{alp}\\left(\\frac{{a}}{{b+c}} + \\frac{{b}}{{c+a}} + \\frac{{c}}{{a+b}}\\right) + {3 * bet}')}.",
                f"بموجب متباينة نسبيت يكون المجموع الدوري الأساسي أكبر من أو يساوي {m('\\frac{3}{2}')}.",
                f"إذن القيمة الصغرى هي {m(f'{ans_f}')} وتتحقق عند {m('a = b = c')}.",
            ],
            f"عند تعويض {m('a = b = c = 1')} نحصل على {m(f'{ans_f}')} مباشرة.",
            diagram_en=svg,
        ))

    # Medium (156..160): Cyclic quadratic-over-linear sums sum_{cyc} a^2 / (p b + q c) given a + b + c = S
    nesb_med = [
        (1, 1, 12),   # sum a^2/(b+c) >= 12/2 = 6
        (1, 2, 15),   # sum a^2/(b+2c) >= 15/3 = 5
        (2, 3, 20),   # sum a^2/(2b+3c) >= 20/5 = 4
        (1, 3, 28),   # sum a^2/(b+3c) >= 28/4 = 7
        (3, 2, 35),   # sum a^2/(3b+2c) >= 35/5 = 7 -> pick S=45 -> 9
    ]
    nesb_med[-1] = (3, 2, 45)
    for offset, (p_w, q_w, S_sum) in enumerate(nesb_med, 156):
        qid = f"OLYM-T2-{offset:03d}"
        ans_f = Fraction(S_sum, p_w + q_w)
        ans = int(ans_f) if ans_f.denominator == 1 else ans_f
        for ta, tb, tc in [(1, 2, 3), (5, 1, 9), (1, 1, 1)]:
            scale = Fraction(S_sum, ta + tb + tc)
            va, vb, vc = ta * scale, tb * scale, tc * scale
            val = va**2 / (p_w * vb + q_w * vc) + vb**2 / (p_w * vc + q_w * va) + vc**2 / (p_w * va + q_w * vb)
            assert val >= ans_f
        pb_str = "b" if p_w == 1 else f"{p_w}b"
        qc_str = "c" if q_w == 1 else f"{q_w}c"
        pc_str = "c" if p_w == 1 else f"{p_w}c"
        qa_str = "a" if q_w == 1 else f"{q_w}a"
        pa_str = "a" if p_w == 1 else f"{p_w}a"
        qb_str = "b" if q_w == 1 else f"{q_w}b"
        q_en = (
            f"Positive real numbers {m('a, b, c')} satisfy {m(f'a + b + c = {S_sum}')}. "
            f"Find the minimum value of {m(f'\\frac{{a^2}}{{{pb_str} + {qc_str}}} + \\frac{{b^2}}{{{pc_str} + {qa_str}}} + \\frac{{c^2}}{{{pa_str} + {qb_str}}}')}."
        )
        q_ar = (
            f"أعداد حقيقية موجبة {m('a, b, c')} تحقق {m(f'a + b + c = {S_sum}')}. "
            f"أوجد القيمة الصغرى للمقدار الدوري {m(f'\\frac{{a^2}}{{{pb_str} + {qc_str}}} + \\frac{{b^2}}{{{pc_str} + {qa_str}}} + \\frac{{c^2}}{{{pa_str} + {qb_str}}}')}."
        )
        svg = svg_olym_inequality_curve("a²", f"{pb_str}+{qc_str}", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Medium", bp11,
            q_en, q_ar, ans,
            [ans_f + 2, ans_f - 1, Fraction(S_sum, 3), ans_f + 3],
            f"Apply Titu's Lemma directly: the cyclic denominators sum to {m(f'({p_w} + {q_w})(a + b + c)')}.",
            f"طبّق توطئة تيتو مباشرة؛ إذ إن مجموع المقامات الدورية يساوي {m(f'({p_w} + {q_w})(a + b + c)')}.",
            "Bound the cyclic sum via Titu's Lemma and confirm equality at a = b = c = S/3.",
            [
                f"By Titu's Lemma, the cyclic sum is at least {m(f'\\frac{{(a + b + c)^2}}{{({p_w} + {q_w})(a + b + c)}} = \\frac{{a + b + c}}{{{p_w + q_w}}}')}.",
                f"Substituting {m(f'a + b + c = {S_sum}')} gives {m(f'\\frac{{{S_sum}}}{{{p_w + q_w}}} = {ans}')}.",
                f"Equality holds at {m(f'a = b = c = {Fraction(S_sum, 3)}')}, where all three ratios equal {m(f'1/{p_w + q_w}')}.",
            ],
            f"At {m('a = b = c')}, all three fractions coincide and sum to {m(str(ans))}.",
            "نحدّ المجموع الدوري من الأسفل بتوطئة تيتو ونتحقق من التساوي عند تماثل المتغيرات.",
            [
                f"بتطبيق توطئة تيتو يكون المجموع أكبر من أو يساوي {m(f'\\frac{{(a + b + c)^2}}{{({p_w} + {q_w})(a + b + c)}} = \\frac{{a + b + c}}{{{p_w + q_w}}}')}.",
                f"بتعويض {m(f'a + b + c = {S_sum}')} نحصل على {m(f'{ans}')}.",
                f"تتحقق المساواة عند {m(f'a = b = c = {Fraction(S_sum, 3)}')}.",
            ],
            f"عند تساوي المتغيرات الثلاثة تتطابق النسب ويبلغ المجموع {m(str(ans))}.",
            diagram_en=svg,
        ))

    # Hard (161..165): Olympiad cyclic inequalities (3 cubic sums + 2 harmonic-split maxima)
    cubic_cyc_cases = [18, 24, 30]
    for idx_sub, S_val in enumerate(cubic_cyc_cases):
        offset = 161 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = S_val // 3
        for ta, tb, tc in [(1, 2, 5), (3, 7, 2), (1, 1, 1)]:
            sc = Fraction(S_val, ta + tb + tc)
            va, vb, vc = ta * sc, tb * sc, tc * sc
            lhs = va**3 / (va**2 + va * vb + vb**2) + vb**3 / (vb**2 + vb * vc + vc**2) + vc**3 / (vc**2 + vc * va + va**2)
            assert lhs >= ans
        q_en = (
            f"In an Intermediate Olympiad cyclic inequality, positive reals {m('a, b, c')} satisfy "
            f"{m(f'a + b + c = {S_val}')}. Find the minimum value of "
            f"{m('\\frac{a^3}{a^2 + ab + b^2} + \\frac{b^3}{b^2 + bc + c^2} + \\frac{c^3}{c^2 + ca + a^2}')}."
        )
        q_ar = (
            f"في متباينة دورية للأولمبياد المتوسط، تحقق الأعداد الموجبة {m('a, b, c')} الشرط "
            f"{m(f'a + b + c = {S_val}')}. أوجد القيمة الصغرى للمقدار "
            f"{m('\\frac{a^3}{a^2 + ab + b^2} + \\frac{b^3}{b^2 + bc + c^2} + \\frac{c^3}{c^2 + ca + a^2}')}."
        )
        svg = svg_olym_inequality_curve("a³", "a²+ab+b²", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Hard", bp11,
            q_en, q_ar, ans,
            [S_val // 2, S_val, ans - 2, ans + 3],
            f"Note {m('\\sum_{\\text{cyc}} \\frac{a^3 - b^3}{a^2 + ab + b^2} = \\sum_{\\text{cyc}} (a - b) = 0')} and use {m('\\frac{a^3 + b^3}{a^2 + ab + b^2} \\ge \\frac{a + b}{3}')}.",
            f"لاحظ أن {m('\\sum_{\\text{cyc}} \\frac{a^3 - b^3}{a^2 + ab + b^2} = \\sum_{\\text{cyc}} (a - b) = 0')} واستعمل المتباينة {m('\\frac{a^3 + b^3}{a^2 + ab + b^2} \\ge \\frac{a + b}{3}')}.",
            "Symmetrize using a^3 - b^3 = (a - b)(a^2 + ab + b^2) and bound each symmetric pair from below by (a + b)/3.",
            [
                f"Since {m('\\frac{a^3 - b^3}{a^2 + ab + b^2} = a - b')}, summing cyclically gives {m('\\sum_{\\text{cyc}} \\frac{a^3}{a^2+ab+b^2} = \\sum_{\\text{cyc}} \\frac{b^3}{a^2+ab+b^2}')}.",
                f"Averaging the two equal sums gives {m('\\frac{1}{2}\\sum_{\\text{cyc}} \\frac{a^3 + b^3}{a^2 + ab + b^2} \\ge \\frac{1}{2}\\sum_{\\text{cyc}} \\frac{a + b}{3} = \\frac{a + b + c}{3}')}, since {m('3(a^3+b^3) - (a+b)(a^2+ab+b^2) = 2(a+b)(a-b)^2 \\ge 0')}.",
                f"With {m(f'a + b + c = {S_val}')}, the minimum is {m(f'{S_val}/3 = {ans}')} at {m(f'a = b = c = {ans}')}.",
            ],
            f"At {m(f'a = b = c = {ans}')}, each fraction equals {m(f'{ans}/3')}, summing to {m(str(ans))}.",
            "نُناظر المجموع باستعمال فرق المكعبين ثم نحدّ كل حد متناظر من الأسفل بالمقدار (a + b)/3.",
            [
                f"بما أن {m('\\frac{a^3 - b^3}{a^2 + ab + b^2} = a - b')} فإن المجموع الدوري للبسط {m('a^3')} يساوي نظيره للبسط {m('b^3')}.",
                f"بأخذ المتوسط واستعمال {m('\\frac{a^3 + b^3}{a^2 + ab + b^2} \\ge \\frac{a + b}{3}')} نجد أن المجموع لا يقل عن {m('\\frac{a + b + c}{3}')}.",
                f"بالتعويض نحصل على القيمة الصغرى {m(f'{S_val}/3 = {ans}')} عند {m(f'a = b = c = {ans}')}.",
            ],
            f"عند {m(f'a = b = c = {ans}')} يساوي كل كسر {m(f'{ans}/3')} فيكون المجموع {m(str(ans))}.",
            diagram_en=svg,
        ))

    harm_split_cases = [20, 36]
    for idx_sub, S_val in enumerate(harm_split_cases):
        offset = 164 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = S_val // 4
        for ta, tb, tc in [(1, 2, 5), (4, 1, 3), (1, 1, 1)]:
            sc = Fraction(S_val, ta + tb + tc)
            va, vb, vc = ta * sc, tb * sc, tc * sc
            lhs = va * vb / (va + vb + 2 * vc) + vb * vc / (vb + vc + 2 * va) + vc * va / (vc + va + 2 * vb)
            assert lhs <= ans
        q_en = (
            f"Positive real numbers {m('a, b, c')} satisfy {m(f'a + b + c = {S_val}')}. "
            f"Find the maximum possible value of {m('\\frac{ab}{a + b + 2c} + \\frac{bc}{b + c + 2a} + \\frac{ca}{c + a + 2b}')}."
        )
        q_ar = (
            f"تحقق الأعداد الحقيقية الموجبة {m('a, b, c')} الشرط {m(f'a + b + c = {S_val}')}. "
            f"أوجد القيمة العظمى الممكنة للمقدار {m('\\frac{ab}{a + b + 2c} + \\frac{bc}{b + c + 2a} + \\frac{ca}{c + a + 2b}')}."
        )
        svg = svg_olym_inequality_curve("ab", "a+b+2c", "max=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Hard", bp11,
            q_en, q_ar, ans,
            [S_val // 2, S_val // 3 if S_val % 3 == 0 else ans + 3, ans + 2, ans - 2],
            f"Group {m('a + b + 2c = (a + c) + (b + c)')} and apply {m('\\frac{4}{x + y} \\le \\frac{1}{x} + \\frac{1}{y}')}.",
            f"اجمع المقام في الصورة {m('a + b + 2c = (a + c) + (b + c)')} وطبّق المتباينة {m('\\frac{4}{x + y} \\le \\frac{1}{x} + \\frac{1}{y}')}.",
            "Split each denominator as (a + c) + (b + c) and apply the harmonic-arithmetic inequality so cyclic terms telescope.",
            [
                f"Using {m('\\frac{4}{(a + c) + (b + c)} \\le \\frac{1}{a + c} + \\frac{1}{b + c}')}, we get {m('\\frac{ab}{a + b + 2c} \\le \\frac{1}{4}\\left(\\frac{ab}{a + c} + \\frac{ab}{b + c}\\right)')}.",
                f"Summing cyclically pairs terms with matching denominators: {m('\\frac{1}{4}\\sum_{\\text{cyc}} \\frac{ab + ca}{b + c} = \\frac{a + b + c}{4}')}.",
                f"With {m(f'a + b + c = {S_val}')}, the maximum is {m(f'{S_val}/4 = {ans}')}, attained at {m('a = b = c')}.",
            ],
            f"At {m(f'a = b = c = {Fraction(S_val, 3)}')}, the sum equals {m(f'3 \\cdot \\frac{{(S/3)^2}}{{4S/3}} = \\frac{{S}}{{4}} = {ans}')}.",
            "نقسّم كل مقام إلى مجموع زوجين ثم نطبق متباينة الوسط التوافقي والحسابي فتختصر الكسور دورياً.",
            [
                f"من المتباينة {m('\\frac{4}{(a + c) + (b + c)} \\le \\frac{1}{a + c} + \\frac{1}{b + c}')} نجد {m('\\frac{ab}{a + b + 2c} \\le \\frac{1}{4}\\left(\\frac{ab}{a + c} + \\frac{ab}{b + c}\\right)')}.",
                f"بالجمع الدوري تجتمع الكسور ذات المقام الموحد لتعطي {m('\\frac{1}{4}(a + b + c)')}.",
                f"بتعويض {m(f'a + b + c = {S_val}')} نحصل على القيمة العظمى {m(str(ans))} عند تساوي المتغيرات.",
            ],
            f"بالتعويض المباشر عند التساوي نحصل على {m(str(ans))} بالضبط.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 12: olym_t2_ineq_rearrangement_chebyshev (OLYM-T2-166..180)
    # ------------------------------------------------------------------
    bp12 = "olym_t2_ineq_rearrangement_chebyshev"

    # Easy (166..170): Permutation dot-product minimum via Rearrangement Inequality
    rearr_easy = [
        ([1, 3, 5, 8], [2, 4, 7, 9]),
        ([2, 4, 7, 11], [1, 3, 6, 10]),
        ([1, 5, 6, 9], [3, 4, 8, 12]),
        ([2, 3, 8, 10], [1, 5, 7, 11]),
        ([1, 4, 9, 12], [2, 5, 6, 10]),
    ]
    for offset, (seq_a, seq_b) in enumerate(rearr_easy, 166):
        qid = f"OLYM-T2-{offset:03d}"
        ans = sum(a * b for a, b in zip(sorted(seq_a), sorted(seq_b, reverse=True)))
        max_v = sum(a * b for a, b in zip(sorted(seq_a), sorted(seq_b)))
        all_sums = [sum(a * b for a, b in zip(seq_a, perm)) for perm in itertools.permutations(seq_b)]
        assert ans == min(all_sums) and max_v == max(all_sums)
        a_tex = ", ".join(str(x) for x in seq_a)
        b_tex = ", ".join(str(x) for x in seq_b)
        q_en = (
            f"Let {m(f'(a_1, a_2, a_3, a_4) = ({a_tex})')} and let {m('(b_1, b_2, b_3, b_4)')} be any "
            f"permutation of {m(f'({b_tex})')}. What is the minimum possible value of {m('\\sum_{i=1}^{4} a_i b_i')}?"
        )
        q_ar = (
            f"ليكن {m(f'(a_1, a_2, a_3, a_4) = ({a_tex})')} وليكن {m('(b_1, b_2, b_3, b_4)')} أي تبديل "
            f"للأعداد {m(f'({b_tex})')}. ما أصغر قيمة ممكنة للمجموع {m('\\sum_{i=1}^{4} a_i b_i')}؟"
        )
        svg = svg_number_strip(["a↑", "b↓", "min=?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Easy", bp12,
            q_en, q_ar, ans,
            [max_v, (ans + max_v) // 2, ans + 6, ans - 5],
            f"By the Rearrangement Inequality, {m('\\sum a_i b_i')} is minimized when the sequences are oppositely ordered.",
            f"بموجب متباينة إعادة الترتيب، يبلغ المجموع {m('\\sum a_i b_i')} قيمته الصغرى عندما تُرتَّب المتتاليتان ترتيباً متعاكساً.",
            "Pair the ascending sequence with the descending sequence to minimize the dot product.",
            [
                f"Sort the first tuple ascending: {m(f'({a_tex})')}, and sort the second descending: {m('(' + ', '.join(str(x) for x in sorted(seq_b, reverse=True)) + ')')}.",
                f"By the Rearrangement Inequality, opposite ordering minimizes {m('\\sum_{i=1}^{4} a_i b_i')}.",
                f"Compute {m(' + '.join(f'{a} \\cdot {b}' for a, b in zip(sorted(seq_a), sorted(seq_b, reverse=True))) + f' = {ans}')}.",
            ],
            f"Any adjacent swap of inverted pairs strictly increases the sum toward the maximum {m(str(max_v))}.",
            "نقرن المتتالية التصاعدية بالمتتالية التنازلية لتحقيق أصغر مجموع جداءات ممكن.",
            [
                f"نرتب الأولى تصاعدياً {m(f'({a_tex})')} والثانية تنازلياً {m('(' + ', '.join(str(x) for x in sorted(seq_b, reverse=True)) + ')')}.",
                f"بموجب متباينة إعادة الترتيب يتحقق الحد الأدنى عند الترتيب المتعاكس.",
                f"نحسب المجموع فنجد {m(str(ans))}.",
            ],
            f"أي تبديل يعكس الترتيب المتعاكس يزيد المجموع باتجاه القيمة العظمى {m(str(max_v))}.",
            diagram_en=svg,
        ))

    # Medium (171..175): Algebraic Rearrangement: max of a^2 b + b^2 c + c^2 a given a^3 + b^3 + c^3 = K
    rearr_med = [24, 39, 54, 75, 96]
    for offset, K_cub in enumerate(rearr_med, 171):
        qid = f"OLYM-T2-{offset:03d}"
        ans = K_cub
        q_en = (
            f"Positive real numbers {m('a, b, c')} satisfy {m(f'a^3 + b^3 + c^3 = {K_cub}')}. "
            f"Using the Rearrangement Inequality, find the maximum possible value of {m('a^2 b + b^2 c + c^2 a')}."
        )
        q_ar = (
            f"أعداد حقيقية موجبة {m('a, b, c')} تحقق {m(f'a^3 + b^3 + c^3 = {K_cub}')}. "
            f"باستخدام متباينة إعادة الترتيب، أوجد أكبر قيمة ممكنة للمقدار {m('a^2 b + b^2 c + c^2 a')}."
        )
        svg = svg_olym_inequality_curve("a²b", "a³", "max=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Medium", bp12,
            q_en, q_ar, ans,
            [K_cub // 3, (2 * K_cub) // 3, K_cub - 3, K_cub + 6],
            f"Observe that {m('(a^2, b^2, c^2)')} and {m('(a, b, c)')} are sorted in the exact same order.",
            f"لاحظ أن الثلاثيتين {m('(a^2, b^2, c^2)')} و{m('(a, b, c)')} مرتبتان بنفس الترتيب تماماً.",
            "Apply the Rearrangement Inequality to the similarly ordered triples (a^2, b^2, c^2) and (a, b, c).",
            [
                f"For positive reals, {m('x \\mapsto x^2')} is strictly increasing, so {m('(a^2, b^2, c^2)')} and {m('(a, b, c)')} have identical ordering.",
                f"By the Rearrangement Inequality, any permutation such as {m('(b, c, a)')} satisfies {m('a^2 b + b^2 c + c^2 a \\le a^3 + b^3 + c^3')}.",
                f"Equality holds at {m(f'a = b = c = \\sqrt[3]{{{K_cub}/3}}')}, giving maximum {m(str(ans))}.",
            ],
            f"Equivalently by AM-GM, {m('\\sum_{\\text{cyc}} (2a^3 + b^3)/3 \\ge \\sum_{\\text{cyc}} a^2 b')}, confirming {m(str(ans))}.",
            "نطبق متباينة إعادة الترتيب على الثلاثيتين المتوافقتين في الترتيب (a^2, b^2, c^2) و(a, b, c).",
            [
                f"للأعداد الموجبة تتفق الثلاثيتان {m('(a^2, b^2, c^2)')} و{m('(a, b, c)')} في الترتيب التصاعدي.",
                f"بموجب متباينة إعادة الترتيب يكون {m('a^2 b + b^2 c + c^2 a \\le a^3 + b^3 + c^3')}.",
                f"تتحقق المساواة عند تساوي المتغيرات الثلاثة فتكون القيمة العظمى {m(str(ans))}.",
            ],
            f"وتؤكد متباينة AM-GM النتيجة ذاتها لأن {m('\\sum (2a^3 + b^3)/3 = a^3 + b^3 + c^3')}.",
            diagram_en=svg,
        ))

    # Hard (176..180): Chebyshev's Sum Inequality on symmetric rational sums sum a^3/(b + c) given a + b + c = S
    cheb_hard = [6, 12, 18, 24, 30]
    for offset, S_tot in enumerate(cheb_hard, 176):
        qid = f"OLYM-T2-{offset:03d}"
        ans = (S_tot * S_tot) // 6
        for ta, tb, tc in [(1, 2, 3), (5, 1, 2), (1, 1, 1)]:
            sc = Fraction(S_tot, ta + tb + tc)
            va, vb, vc = ta * sc, tb * sc, tc * sc
            assert va**3 / (vb + vc) + vb**3 / (vc + va) + vc**3 / (va + vb) >= ans
        q_en = (
            f"In an Intermediate Olympiad problem, positive real numbers {m('a, b, c')} satisfy "
            f"{m(f'a + b + c = {S_tot}')}. Using Chebyshev's sum inequality, find the minimum value of "
            f"{m('\\frac{a^3}{b + c} + \\frac{b^3}{c + a} + \\frac{c^3}{a + b}')}."
        )
        q_ar = (
            f"في مسألة للأولمبياد المتوسط، تحقق الأعداد الحقيقية الموجبة {m('a, b, c')} المعادلة "
            f"{m(f'a + b + c = {S_tot}')}. باستخدام متباينة تشيبيشيف للمجاميع، أوجد القيمة الصغرى للمقدار "
            f"{m('\\frac{a^3}{b + c} + \\frac{b^3}{c + a} + \\frac{c^3}{a + b}')}."
        )
        svg = svg_olym_inequality_curve("a³/(b+c)", "Cheb", "min=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Inequalities", "Hard", bp12,
            q_en, q_ar, ans,
            [(S_tot * S_tot) // 3, (S_tot * S_tot) // 9, ans // 2 if ans >= 4 else ans + 4, ans + S_tot],
            f"Without loss of generality assume {m('a \\ge b \\ge c')}; then {m('(a, b, c)')} and {m('\\left(\\frac{a^2}{b+c}, \\frac{b^2}{c+a}, \\frac{c^2}{a+b}\\right)')} are similarly ordered.",
            f"افترض دون إخلال بالعمومية أن {m('a \\ge b \\ge c')}؛ فتكون الثلاثيتان {m('(a, b, c)')} و{m('\\left(\\frac{a^2}{b+c}, \\frac{b^2}{c+a}, \\frac{c^2}{a+b}\\right)')} مرتبتين بنفس الاتجاه.",
            "Combine Chebyshev's sum inequality on similarly sorted triples with Titu's Lemma on sum a^2/(b + c).",
            [
                f"By symmetry assume {m('a \\ge b \\ge c > 0')}; then {m('a^2 \\ge b^2 \\ge c^2')} and {m('\\frac{1}{b+c} \\ge \\frac{1}{c+a} \\ge \\frac{1}{a+b}')}.",
                f"By Chebyshev's inequality, {m('\\sum_{\\text{cyc}} \\frac{a^3}{b+c} \\ge \\frac{a + b + c}{3} \\sum_{\\text{cyc}} \\frac{a^2}{b+c}')}.",
                f"By Titu's Lemma, {m('\\sum_{\\text{cyc}} \\frac{a^2}{b+c} \\ge \\frac{a + b + c}{2}')}, yielding {m(f'\\frac{{{S_tot}}}{{3}} \\cdot \\frac{{{S_tot}}}{{2}} = {ans}')}.",
            ],
            f"At {m(f'a = b = c = {S_tot // 3}')}, the sum equals {m(f'3 \\cdot \\frac{{({S_tot // 3})^3}}{{{2 * (S_tot // 3)}}} = {ans}')}.",
            "ندمج متباينة تشيبيشيف للثلاثيات المتوافقة في الترتيب مع توطئة تيتو.",
            [
                f"بالتماثل نفترض {m('a \\ge b \\ge c > 0')}، فتكون {m('\\frac{a^2}{b+c} \\ge \\frac{b^2}{c+a} \\ge \\frac{c^2}{a+b}')}.",
                f"بموجب متباينة تشيبيشيف: {m('\\sum \\frac{a^3}{b+c} \\ge \\frac{a + b + c}{3}\\sum \\frac{a^2}{b+c}')}.",
                f"ومن توطئة تيتو {m('\\sum \\frac{a^2}{b+c} \\ge \\frac{a + b + c}{2}')}، فنجد القيمة الصغرى {m(f'\\frac{{{S_tot}^2}}{{6}} = {ans}')}.",
            ],
            f"عند {m(f'a = b = c = {S_tot // 3}')} يتحقق الحد الأدنى {m(str(ans))} تماماً.",
            diagram_en=svg,
        ))

    return qs


# ==============================================================================
# UNIT 2.4 — Geometry I: Circles, Cyclic Quads & Cevians (OLYM-T2-181 .. 240)
# ==============================================================================

def _gen_u24_geometry_i() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 13: olym_t2_geo_power_point_radical (OLYM-T2-181..195)
    # ------------------------------------------------------------------
    bp13 = "olym_t2_geo_power_point_radical"

    # Easy (181..185): Tangent-secant Power of a Point PT^2 = PA * (PA + AB), solve for AB
    pop_easy = [
        (12, 8),   # PT=12, PA=8 -> PB=18 -> AB=10
        (15, 9),   # PT=15, PA=9 -> PB=25 -> AB=16
        (20, 16),  # PT=20, PA=16 -> PB=25 -> AB=9
        (18, 12),  # PT=18, PA=12 -> PB=27 -> AB=15
        (24, 18),  # PT=24, PA=18 -> PB=32 -> AB=14
    ]
    for offset, (pt_len, pa_len) in enumerate(pop_easy, 181):
        qid = f"OLYM-T2-{offset:03d}"
        assert (pt_len * pt_len) % pa_len == 0
        pb_len = (pt_len * pt_len) // pa_len
        ans = pb_len - pa_len
        assert ans > 0 and pa_len * (pa_len + ans) == pt_len * pt_len
        q_en = (
            f"From an external point {m('P')}, tangent {m('PT')} of length {m(str(pt_len))} and secant "
            f"{m('PAB')} are drawn to a circle, with {m(f'PA = {pa_len}')}. Find the chord length {m('AB')}."
        )
        q_ar = (
            f"من نقطة خارجية {m('P')} رُسم مماس {m('PT')} طوله {m(str(pt_len))} وقاطع {m('PAB')} لدائرة "
            f"بحيث كان {m(f'PA = {pa_len}')}. أوجد طول الوتر {m('AB')}."
        )
        svg = svg_power_of_point(str(pt_len), str(pa_len), "?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp13,
            q_en, q_ar, ans,
            [pb_len, pt_len - pa_len, ans + 4, abs(ans - 3)],
            f"By Power of a Point, {m('PT^2 = PA \\cdot PB')}, where {m('PB = PA + AB')}.",
            f"بموجب قوة نقطة بالنسبة إلى دائرة: {m('PT^2 = PA \\cdot PB')} حيث {m('PB = PA + AB')}.",
            "Apply the tangent-secant theorem PT^2 = PA * PB and subtract PA from PB.",
            [
                f"By the tangent-secant Power of a Point theorem, {m(f'PA \\cdot PB = PT^2 = {pt_len}^2 = {pt_len**2}')}.",
                f"Solve for {m('PB')}: {m(f'PB = \\frac{{{pt_len**2}}}{{{pa_len}}} = {pb_len}')}.",
                f"Subtract the exterior segment: {m(f'AB = PB - PA = {pb_len} - {pa_len} = {ans}')}.",
            ],
            f"Check: {m(f'PA(PA + AB) = {pa_len} \\cdot {pb_len} = {pa_len * pb_len} = {pt_len}^2')}.",
            "نطبق مبرهنة المماس والقاطع PT^2 = PA · PB ثم نطرح PA من PB.",
            [
                f"من قوة النقطة {m('P')}: {m(f'PA \\cdot PB = PT^2 = {pt_len**2}')}.",
                f"نحسب طول القاطع الكلي: {m(f'PB = {pt_len**2} / {pa_len} = {pb_len}')}.",
                f"إذن طول الوتر هو {m(f'AB = PB - PA = {pb_len} - {pa_len} = {ans}')}.",
            ],
            f"التحقق: {m(f'{pa_len} \\times {pb_len} = {pt_len**2}')}.",
            diagram_en=svg,
        ))

    # Medium (186..190): Interior point power R^2 - OP^2 = PA * PB, find OP
    pop_med = [
        (13, 9, 16, 5),
        (15, 8, 18, 9),
        (17, 9, 25, 8),
        (20, 8, 32, 12),
        (25, 16, 25, 15),
    ]
    for offset, (R_rad, pa_l, pb_l, op_ans) in enumerate(pop_med, 186):
        qid = f"OLYM-T2-{offset:03d}"
        assert R_rad * R_rad - op_ans * op_ans == pa_l * pb_l
        assert pa_l + pb_l <= 2 * R_rad and abs(pa_l - pb_l) <= 2 * op_ans
        ans = op_ans
        q_en = (
            f"Inside a circle with center {m('O')} and radius {m(str(R_rad))}, a chord {m('AB')} passes "
            f"through point {m('P')} such that {m(f'PA = {pa_l}')} and {m(f'PB = {pb_l}')}. Find the distance {m('OP')}."
        )
        q_ar = (
            f"داخل دائرة مركزها {m('O')} ونصف قطرها {m(str(R_rad))}، يمر الوتر {m('AB')} بالنقطة {m('P')} "
            f"بحيث {m(f'PA = {pa_l}')} و{m(f'PB = {pb_l}')}. أوجد المسافة {m('OP')}."
        )
        svg = svg_olym_radical_axis(f"R={R_rad}", f"PA={pa_l}", "OP=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp13,
            q_en, q_ar, ans,
            [abs(pb_l - pa_l) // 2 if abs(pb_l - pa_l) // 2 != ans else ans + 2, R_rad - pa_l if R_rad - pa_l != ans else ans + 4, ans + 3, max(1, ans - 2)],
            f"Use the interior Power of a Point formula {m('R^2 - OP^2 = PA \\cdot PB')}.",
            f"استعمل صيغة قوة النقطة الداخلية {m('R^2 - OP^2 = PA \\cdot PB')}.",
            "Draw the diameter through O and P to equate PA * PB with (R - OP)(R + OP) = R^2 - OP^2.",
            [
                f"The diameter through {m('O')} and {m('P')} divides into segments {m('R - OP')} and {m('R + OP')}.",
                f"By intersecting chords, {m(f'R^2 - OP^2 = PA \\cdot PB = {pa_l} \\cdot {pb_l} = {pa_l * pb_l}')}.",
                f"Thus {m(f'OP^2 = {R_rad}^2 - {pa_l * pb_l} = {ans * ans}')}, so {m(f'OP = {ans}')}.",
            ],
            f"Notice chord length {m(f'{pa_l + pb_l} \\le {2 * R_rad}')} and {m(f'(R - OP)(R + OP) = {R_rad - ans} \\cdot {R_rad + ans} = {pa_l * pb_l}')}.",
            "نمرر القطر المار بـ O وP فتكون قوة النقطة الداخلية PA · PB مساوية للمقدار R^2 - OP^2.",
            [
                f"يقسّم القطر المار بالنقطة {m('P')} إلى الجزأين {m('R - OP')} و{m('R + OP')}.",
                f"من تقاطع الأوتار: {m(f'R^2 - OP^2 = PA \\cdot PB = {pa_l * pb_l}')}.",
                f"إذن {m(f'OP^2 = {R_rad**2} - {pa_l * pb_l} = {ans**2}')} ومنه {m(f'OP = {ans}')}.",
            ],
            f"التحقق: {m(f'({R_rad} - {ans})({R_rad} + {ans}) = {pa_l * pb_l}')}.",
            diagram_en=svg,
        ))

    # Hard (191..195): Radical axis foot H on line of centers O1 O2: O1H^2 - O2H^2 = R1^2 - R2^2
    rad_hard = [
        (13, 9, 22),   # R1=13, R2=9, d=22 -> R1^2-R2^2 = 88 -> d_diff = 4 -> O1H = (22+4)/2 = 13
        (15, 7, 22),   # 225 - 49 = 176 -> 176/22 = 8 -> O1H = (22+8)/2 = 15
        (17, 10, 27),  # 289 - 100 = 189 -> 189/27 = 7 -> O1H = (27+7)/2 = 17
        (20, 12, 16),  # 400 - 144 = 256 -> 256/16 = 16 -> O1H = (16+16)/2 = 16
        (25, 15, 20),  # 625 - 225 = 400 -> 400/20 = 20 -> O1H = (20+20)/2 = 20
    ]
    # Let's vary parameters so O1H isn't accidentally equal to R1!
    rad_hard = [
        (14, 6, 20),   # 196 - 36 = 160 -> 160/20 = 8 -> O1H = (20+8)/2 = 14 -> let's pick d=16: 160/16 = 10 -> O1H = (16+10)/2 = 13!
        (15, 9, 18),   # 225 - 81 = 144 -> 144/18 = 8 -> O1H = (18+8)/2 = 13 -> pick d=24: 144/24 = 6 -> O1H = (24+6)/2 = 15 -> pick d=16: 144/16 = 9 -> non-int; d=12: 144/12=12 -> O1H = 12!
        (17, 7, 20),   # 289 - 49 = 240 -> 240/20 = 12 -> O1H = (20+12)/2 = 16!
        (19, 11, 24),  # 361 - 121 = 240 -> 240/24 = 10 -> O1H = (24+10)/2 = 17!
        (21, 9, 30),   # 441 - 81 = 360 -> 360/30 = 12 -> O1H = (30+12)/2 = 21 -> pick d=20: 360/20 = 18 -> O1H = (20+18)/2 = 19!
    ]
    for offset, (R1, R2, d_cen) in enumerate(rad_hard, 191):
        qid = f"OLYM-T2-{offset:03d}"
        diff_sq = R1 * R1 - R2 * R2
        assert diff_sq % d_cen == 0
        delta = diff_sq // d_cen
        assert (d_cen + delta) % 2 == 0
        ans = (d_cen + delta) // 2
        o2h = d_cen - ans
        assert ans > 0 and o2h >= 0 and (ans * ans - R1 * R1) == (o2h * o2h - R2 * R2)
        q_en = (
            f"Circles {m('\\omega_1')} (center {m('O_1')}, radius {m(str(R1))}) and {m('\\omega_2')} "
            f"(center {m('O_2')}, radius {m(str(R2))}) have {m(f'O_1 O_2 = {d_cen}')}. Their radical axis "
            f"intersects segment {m('O_1 O_2')} at {m('H')}. Find {m('O_1 H')}."
        )
        q_ar = (
            f"دائرتان {m('\\omega_1')} (مركزها {m('O_1')} ونصف قطرها {m(str(R1))}) و{m('\\omega_2')} "
            f"(مركزها {m('O_2')} ونصف قطرها {m(str(R2))}) المسافة بين مركزيهما {m(f'O_1 O_2 = {d_cen}')}. "
            f"يقطع محورهما الأساسي القطعة {m('O_1 O_2')} في {m('H')}. أوجد الطول {m('O_1 H')}."
        )
        svg = svg_olym_radical_axis(f"R={R1}", f"r={R2}", "H=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp13,
            q_en, q_ar, ans,
            [o2h if o2h != ans else ans - 2, R1, d_cen // 2, ans + 2],
            f"Equate powers of {m('H')} with respect to both circles: {m(f'O_1 H^2 - {R1}^2 = O_2 H^2 - {R2}^2')}.",
            f"ساوِ قوة النقطة {m('H')} بالنسبة إلى الدائرتين: {m(f'O_1 H^2 - {R1}^2 = O_2 H^2 - {R2}^2')}.",
            "On the radical axis, O_1 H^2 - O_2 H^2 = R_1^2 - R_2^2 pairs with O_1 H + O_2 H = d.",
            [
                f"Because {m('H')} lies on the radical axis, {m(f'O_1 H^2 - {R1}^2 = O_2 H^2 - {R2}^2')}.",
                f"Factor {m(f'(O_1 H - O_2 H)(O_1 H + O_2 H) = {R1}^2 - {R2}^2 = {diff_sq}')}; since {m(f'O_1 H + O_2 H = {d_cen}')}, we get {m(f'O_1 H - O_2 H = {delta}')}.",
                f"Adding the two equations gives {m(f'O_1 H = \\frac{{{d_cen} + {delta}}}{{2}} = {ans}')}.",
            ],
            f"Powers match: {m(f'{ans}^2 - {R1}^2 = {ans**2 - R1**2}')} and {m(f'{o2h}^2 - {R2}^2 = {o2h**2 - R2**2}')}.",
            "على المحور الأساسي تتساوى قوتا النقطة H بالنسبة للدائرتين، فينتج فرق المربعين مع مجموع القطعتين.",
            [
                f"بما أن {m('H')} تقع على المحور الأساسي فإن {m(f'O_1 H^2 - {R1}^2 = O_2 H^2 - {R2}^2')}.",
                f"بالتحليل مع {m(f'O_1 H + O_2 H = {d_cen}')} نجد {m(f'O_1 H - O_2 H = {diff_sq}/{d_cen} = {delta}')}.",
                f"بجمع المعادلتين نحصل على {m(f'O_1 H = {ans}')}.",
            ],
            f"قوة النقطة متطابقة للدائرتين وتساوي {m(str(ans**2 - R1**2))}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 14: olym_t2_geo_ptolemy_cyclic_quads (OLYM-T2-196..210)
    # ------------------------------------------------------------------
    bp14 = "olym_t2_geo_ptolemy_cyclic_quads"

    # Easy (196..200): Cyclic isosceles trapezoids AC = BD = sqrt(a*c + l^2) via Ptolemy
    ptol_easy = [
        (3, 8, 12, 8, 10),    # AB=3, BC=8, CD=12, DA=8 -> AC^2 = 36 + 64 = 100 -> AC = 10
        (5, 8, 16, 8, 12),    # AB=5, BC=8, CD=16, DA=8 -> AC^2 = 80 + 64 = 144 -> AC = 12
        (9, 10, 21, 10, 17),  # AB=9, BC=10, CD=21, DA=10 -> AC^2 = 189 + 100 = 289 -> AC = 17
        (7, 15, 25, 15, 20),  # AB=7, BC=15, CD=25, DA=15 -> AC^2 = 175 + 225 = 400 -> AC = 20
        (9, 20, 25, 20, 25),  # AB=9, BC=20, CD=25, DA=20 -> AC^2 = 225 + 400 = 625 -> AC = 25
    ]
    for offset, (ab, bc, cd, da, ac_ans) in enumerate(ptol_easy, 196):
        qid = f"OLYM-T2-{offset:03d}"
        assert bc == da and abs(cd - ab) < 2 * bc
        assert ab * cd + bc * da == ac_ans * ac_ans
        ans = ac_ans
        q_en = (
            f"Cyclic isosceles trapezoid {m('ABCD')} with parallel bases {m(f'AB = {ab}')} and "
            f"{m(f'CD = {cd}')} has equal legs {m(f'BC = DA = {bc}')}. Find the diagonal length {m('AC')}."
        )
        q_ar = (
            f"شبه منحرف متساوي الساقين رباعي دائري {m('ABCD')} قاعدتاه المتوازيتان {m(f'AB = {ab}')} "
            f"و{m(f'CD = {cd}')} وساقاه {m(f'BC = DA = {bc}')}. أوجد طول القطر {m('AC')}."
        )
        svg = svg_olym_cyclic_ptolemy(str(ab), str(bc), str(cd), str(da), "AC=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp14,
            q_en, q_ar, ans,
            [(ab + cd) // 2 if (ab + cd) // 2 != ans else ans + 3, bc + ab, ans + 2, ans - 2],
            f"By symmetry {m('AC = BD')}; apply Ptolemy's theorem {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            f"من التماثل {m('AC = BD')}؛ طبّق مبرهنة بطليموس {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            "In a cyclic isosceles trapezoid, equal diagonals reduce Ptolemy's relation to AC^2 = AB*CD + BC^2.",
            [
                f"By symmetry of an isosceles trapezoid inscribed in a circle, the diagonals are equal: {m('AC = BD')}.",
                f"Apply Ptolemy's theorem: {m(f'AC^2 = AB \\cdot CD + BC \\cdot DA = {ab} \\cdot {cd} + {bc}^2 = {ac_ans**2}')}.",
                f"Taking the positive square root yields {m(f'AC = {ans}')}.",
            ],
            f"Leg inequality check: {m(f'|CD - AB|/2 = {abs(cd - ab)/2:g} < {bc}')}, so the trapezoid has positive height.",
            "في شبه المنحرف المتساوي الساقين الدائري يتساوى القطران فتختزل مبرهنة بطليموس إلى مربع القطر.",
            [
                f"بالتماثل يكون القطران متساويين: {m('AC = BD')}.",
                f"من مبرهنة بطليموس: {m(f'AC^2 = {ab} \\cdot {cd} + {bc}^2 = {ac_ans**2}')}.",
                f"بأخذ الجذر التربيعي الموجب نجد {m(f'AC = {ans}')}.",
            ],
            f"يتحقق شرط الارتفاع الموجب لأن {m(f'|CD - AB|/2 < {bc}')}.",
            diagram_en=svg,
        ))

    # Medium (201..205): General cyclic quadrilateral Ptolemy solving for diagonal AC
    # Constructed from two right triangles on common hypotenuse BD so 100% realizable!
    ptol_med = [
        (7, 15, 20, 24, 25),   # BD=25: (7,24,25) & (15,20,25) -> 25*AC = 140 + 360 = 500 -> AC = 20
        (16, 25, 60, 63, 65),  # BD=65: (16,63,65) & (25,60,65) -> 65*AC = 960 + 1575 = 2535 -> AC = 39
        (14, 30, 40, 48, 50),  # BD=50: (14,48,50) & (30,40,50) -> 50*AC = 560 + 1440 = 2000 -> AC = 40
        (13, 36, 77, 84, 85),  # BD=85: (13,84,85) & (36,77,85) -> 85*AC = 1001 + 3024 = 4025? 4025/85 = 805/17; swap C,D: CB=77, CD=36 -> 13*36 + 77*84 = 468 + 6468 = 6936 / 85 = 1387.2? Wait!
        (33, 25, 60, 56, 65),  # BD=65: (33,56,65) & (25,60,65) -> 65*AC = 33*60 + 25*56 = 1980 + 1400 = 3380 -> 3380/65 = 52!
    ]
    # Let's check 4th case cleanly: BD=65 with (39,52,65) and (25,60,65): AB=39, BC=25, CD=60, DA=52 -> 65*AC = 2340 + 1300 = 3640 -> AC = 56!
    ptol_med[3] = (39, 25, 60, 52, 65)
    for offset, (ab, bc, cd, da, bd_diag) in enumerate(ptol_med, 201):
        qid = f"OLYM-T2-{offset:03d}"
        assert ab * ab + da * da == bd_diag * bd_diag and bc * bc + cd * cd == bd_diag * bd_diag
        rhs = ab * cd + bc * da
        assert rhs % bd_diag == 0
        ans = rhs // bd_diag
        # Verify Ptolemy's 2nd theorem too:
        assert Fraction(rhs * (ab * da + bc * cd), ab * bc + cd * da) == ans * ans
        q_en = (
            f"Convex cyclic quadrilateral {m('ABCD')} has side lengths {m(f'AB = {ab}')}, {m(f'BC = {bc}')}, "
            f"{m(f'CD = {cd}')}, {m(f'DA = {da}')}, and diagonal {m(f'BD = {bd_diag}')}. Find diagonal {m('AC')}."
        )
        q_ar = (
            f"الرباعي الدائري المحدب {m('ABCD')} أطوال أضلاعه {m(f'AB = {ab}')} و{m(f'BC = {bc}')} "
            f"و{m(f'CD = {cd}')} و{m(f'DA = {da}')} وطول قطره {m(f'BD = {bd_diag}')}. أوجد طول القطر {m('AC')}."
        )
        svg = svg_olym_cyclic_ptolemy(str(ab), str(bc), str(cd), str(da), "AC=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp14,
            q_en, q_ar, ans,
            [bd_diag, ans + 4, ans - 3, (ab + cd + bc + da) // 4],
            f"Apply Ptolemy's theorem: {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            f"طبّق مبرهنة بطليموس: {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            "Compute the sum of products of opposite sides and divide by the given diagonal BD.",
            [
                f"By Ptolemy's theorem on cyclic quadrilateral {m('ABCD')}, {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
                f"Substitute the given lengths: {m(f'{bd_diag} \\cdot AC = {ab} \\cdot {cd} + {bc} \\cdot {da} = {ab * cd} + {bc * da} = {rhs}')}.",
                f"Divide by {m(str(bd_diag))} to obtain {m(f'AC = {ans}')}.",
            ],
            f"Notice {m('\\angle DAB = \\angle BCD = 90^\\circ')} on diameter {m(f'BD = {bd_diag}')}, confirming {m('ABCD')} is cyclic.",
            "نحسب مجموع جداءي كل ضلعين متقابلين ثم نقسم على طول القطر المعلوم BD.",
            [
                f"بموجب مبرهنة بطليموس في الرباعي الدائري: {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
                f"بالتعويض: {m(f'{bd_diag} \\cdot AC = {ab * cd} + {bc * da} = {rhs}')}.",
                f"بالقسمة على {m(str(bd_diag))} نجد {m(f'AC = {ans}')}.",
            ],
            f"الزاويتان عند {m('A')} و{m('C')} قائمتان على القطر المشترك {m(f'BD = {bd_diag}')} مما يؤكد دائرية الرباعي.",
            diagram_en=svg,
        ))

    # Hard (206..210): Ptolemy's Second Theorem (ratio of diagonals AC/BD) & Brahmagupta cyclic area
    # 206..208: Ratio AC / BD via Ptolemy II: AC / BD = (AB*DA + BC*CD) / (AB*BC + CD*DA)
    ptol_ratio_cases = [
        (2, 3, 6, 7),   # max side 7 < 2+3+6=11! AC/BD = (14 + 18)/(6 + 42) = 32/48 = 2/3
        (3, 5, 6, 10),  # max side 10 < 14! AC/BD = (30 + 30)/(15 + 60) = 60/75 = 4/5
        (4, 5, 8, 11),  # max side 11 < 17! AC/BD = (44 + 40)/(20 + 88) = 84/108 = 7/9
    ]
    for idx_sub, (ab, bc, cd, da) in enumerate(ptol_ratio_cases):
        offset = 206 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        assert 2 * max(ab, bc, cd, da) < ab + bc + cd + da
        ans_f = Fraction(ab * da + bc * cd, ab * bc + cd * da)
        q_en = (
            f"In an Intermediate Olympiad geometry problem, cyclic quadrilateral {m('ABCD')} has side "
            f"lengths {m(f'AB = {ab}')}, {m(f'BC = {bc}')}, {m(f'CD = {cd}')}, and {m(f'DA = {da}')}. "
            f"Find the exact ratio of its diagonals {m('\\frac{AC}{BD}')}."
        )
        q_ar = (
            f"في مسألة هندسة للأولمبياد المتوسط، أطوال أضلاع الرباعي الدائري {m('ABCD')} هي "
            f"{m(f'AB = {ab}')} و{m(f'BC = {bc}')} و{m(f'CD = {cd}')} و{m(f'DA = {da}')}. "
            f"أوجد النسبة الدقيقة بين قطريه {m('\\frac{AC}{BD}')}."
        )
        svg = svg_olym_cyclic_ptolemy(str(ab), str(bc), str(cd), str(da), "AC/BD=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp14,
            q_en, q_ar, ans_f,
            [Fraction(1, 1) / ans_f, Fraction(ab * cd, bc * da), Fraction(ab + cd, bc + da), ans_f + Fraction(1, 5)],
            f"Apply Ptolemy's Second Theorem: {m('\\frac{AC}{BD} = \\frac{AB \\cdot DA + BC \\cdot CD}{AB \\cdot BC + CD \\cdot DA}')}.",
            f"طبّق مبرهنة بطليموس الثانية: {m('\\frac{AC}{BD} = \\frac{AB \\cdot DA + BC \\cdot CD}{AB \\cdot BC + CD \\cdot DA}')}.",
            "Equate circumradius expressions on triangles sharing AC versus BD to obtain Ptolemy's diagonal-ratio formula.",
            [
                f"In any cyclic quadrilateral, {m('AC')} subtends chords split between {m('(AB, DA)')} and {m('(BC, CD)')}, while {m('BD')} splits between {m('(AB, BC)')} and {m('(CD, DA)')}.",
                f"By Ptolemy's Second Theorem, {m(f'\\frac{{AC}}{{BD}} = \\frac{{{ab} \\cdot {da} + {bc} \\cdot {cd}}}{{{ab} \\cdot {bc} + {cd} \\cdot {da}}} = \\frac{{{ab * da + bc * cd}}}{{{ab * bc + cd * da}}}')}.",
                f"Reducing the fraction to lowest terms gives {m(f'\\frac{{AC}}{{BD}} = {ans_f}')}.",
            ],
            f"Since each side is strictly less than the sum of the other three, {m('ABCD')} is a valid non-degenerate cyclic quadrilateral.",
            "نطبق مبرهنة بطليموس الثانية لنسبة القطرين في الرباعي الدائري.",
            [
                f"ترتبط نسبة القطرين بمجموعي جداءات الأضلاع المجاورة لنهايتي كل قطر.",
                f"من مبرهنة بطليموس الثانية: {m(f'\\frac{{AC}}{{BD}} = \\frac{{{ab} \\cdot {da} + {bc} \\cdot {cd}}}{{{ab} \\cdot {bc} + {cd} \\cdot {da}}} = \\frac{{{ab * da + bc * cd}}}{{{ab * bc + cd * da}}}')}.",
                f"بالتبسيط إلى أبسط صورة نحصل على {m(f'{ans_f}')}.",
            ],
            f"متباينة المضلعات متحققة لأن أكبر ضلع أصغر قطعا من مجموع الأضلاع الثلاثة الأخرى.",
            diagram_en=svg,
        ))

    # 209..210: Brahmagupta's formula sqrt((s-a)(s-b)(s-c)(s-d)) on Brahmagupta cyclic quads
    brahm_cases = [
        (13, 14, 15, 12),  # s = 27 -> (14)(13)(12)(15) = 32760? Wait: 14*13*12*15 = 32760 not square! Let's pick exact Brahmagupta quads!
        (7, 15, 20, 24),   # s = 33 -> (26)(18)(13)(9) = 54756 = 234^2! Area = (7*24 + 15*20)/2 = (168+300)/2 = 234!
    ]
    # Second exact Brahmagupta quad: (16, 25, 33, 60)? Wait: s=(16+25+60+63)/2 = 82 -> (66)(57)(22)(19) = 1573704 = 1254^2? Wait: (16*63 + 25*60)/2 = (1008 + 1500)/2 = 1254! Check 1254^2 = 1572516, 66*57*22*19 = 1572516! Or smaller:
    # Take isosceles cyclic trapezoid with integer height! AB=9, CD=21, BC=DA=10: dx = 6, h = 8 -> area = (9+21)/2 * 8 = 120! Check Brahmagupta: s = 25 -> 16 * 4 * 15 * 15 = 14400 = 120^2!
    # Or scalene non-right Brahmagupta quad: (4, 13, 15? -> (5, 12, 13?)) Take (7, 15, 20, 24) -> area 234, and (14, 30, 40, 48) or (8, 15, 15, 22)? Check (4, 11, 15, 12): s=21 -> 17*10*6*9 no; (2, 7, 11, 8): s=14 -> 12*7*3*6 = 1512; (3, 10, 13, 14): s=20 -> 17*10*7*6; (4, 5, 10, 13): s=16 -> 12*11*6*3; (6, 11, 13, 16): s=23 -> 17..; (5, 10, 13, 16): s=22 -> 17..; (8, 9, 15, 16): s=24 -> 16*15*9*8 = 17280; (5, 12, 12, 19): s=24 -> 19..; (7, 15, 20, 24) -> 234 AND (39, 25, 60, 52) -> (39*52 + 25*60)/2 = (2028 + 1500)/2 = 1764! Check s = 88 -> 49 * 63 * 28 * 36 = 3111696 = 1764^2! Even smaller: (3, 11, 14, 12)? s=20 -> 17..; (6, 15, 21, 18): s=30 -> 24*15*9*12 = 38880; (9, 10, 21, 10) -> 120; (7, 15, 25, 15): s=31 -> 24*16*6*16 = 36864 = 192^2 -> area 192! Let's use (7, 15, 20, 24) [scalene, area 234] and (33, 25, 60, 56) [scalene: s=87 -> 54*62*27*31? (33*56+25*60)/2 = (1848+1500)/2 = 1674, check 54*62*27*31 = 2802276 = 1674^2! Or smaller scalene: (14, 30, 40, 48)/2 = (7, 15, 20, 24)! What about (15, 20, 7, 24) vs (12, 16, 5? no hyp=20: (12,16,20) and no other). Hyp=13? No two triples. Hyp=25: (7,24,25) and (15,20,25) — TWO orderings! Ordering 1: (7, 15, 20, 24) -> area 234; Ordering 2: (7, 20, 15, 24) -> s=33 -> same sides, same Brahmagupta area 234! What about cyclic quad from (13, 14, 15) + something? Take (9, 10, 17) and ... wait: (7, 15, 20, 24) -> 234 and (13, 14, 15)? Let's use (7, 15, 20, 24) -> 234 and (7, 15, 25, 15) -> 192? Better: (16, 25, 39, 60)! Let's check s = (16+25+39+60)/2 = 70 -> (70-16)(70-25)(70-39)(70-60) = 54 * 45 * 31 * 10? Wait: 52, not 60: (16, 25, 52, 60) -> s=76.5; what about (25, 39, 52, 60): s = 88 -> (63)(49)(36)(28) = 3111696 = 1764^2! Super clean!).
    brahm_cases = [
        (7, 15, 20, 24),
        (25, 39, 52, 60),
    ]
    for idx_sub, (sa, sb, sc, sd) in enumerate(brahm_cases):
        offset = 209 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        s_semi = (sa + sb + sc + sd) // 2
        prod_b = (s_semi - sa) * (s_semi - sb) * (s_semi - sc) * (s_semi - sd)
        ans = math.isqrt(prod_b)
        assert ans * ans == prod_b
        q_en = (
            f"Cyclic quadrilateral {m('ABCD')} has side lengths {m(f'{sa}, {sb}, {sc}, {sd}')} in cyclic order. "
            f"Using Brahmagupta's formula, find the area of {m('ABCD')}."
        )
        q_ar = (
            f"الرباعي الدائري {m('ABCD')} أطوال أضلاعه بالترتيب الدوري هي {m(f'{sa}, {sb}, {sc}, {sd}')}. "
            f"باستخدام صيغة براهماغوبتا، أوجد مساحة الرباعي {m('ABCD')}."
        )
        svg = svg_olym_cyclic_ptolemy(str(sa), str(sb), str(sc), str(sd), "K = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp14,
            q_en, q_ar, ans,
            [ans + 12, ans - 14, s_semi * 4, ans // 2],
            f"Compute semiperimeter {m(f's = {s_semi}')} and apply Brahmagupta's formula {m('K = \\sqrt{(s - a)(s - b)(s - c)(s - d)}')}.",
            f"احسب نصف المحيط {m(f's = {s_semi}')} وطبّق صيغة براهماغوبتا {m('K = \\sqrt{(s - a)(s - b)(s - c)(s - d)}')}.",
            "Brahmagupta's formula generalizes Heron's formula to any cyclic quadrilateral.",
            [
                f"Compute the semiperimeter: {m(f's = \\frac{{{sa} + {sb} + {sc} + {sd}}}{{2}} = {s_semi}')}.",
                f"Form the four factors: {m(f'(s-a, s-b, s-c, s-d) = ({s_semi-sa}, {s_semi-sb}, {s_semi-sc}, {s_semi-sd})')}.",
                f"Take the square root of their product: {m(f'K = \\sqrt{{{prod_b}}} = {ans}')}.",
            ],
            f"Splitting into right triangles confirms the exact area {m(str(ans))}.",
            "تعمم صيغة براهماغوبتا صيغة هيرون لحساب مساحة أي رباعي دائري بدلالة أضلاعه.",
            [
                f"نحسب نصف المحيط: {m(f's = {s_semi}')}.",
                f"نحسب العوامل الأربعة: {m(f'({s_semi-sa}, {s_semi-sb}, {s_semi-sc}, {s_semi-sd})')}.",
                f"بأخذ الجذر التربيعي لحاصل ضربها نجد المساحة {m(f'K = {ans}')}.",
            ],
            f"بتقسيم الرباعي إلى مثلثين قائمين نتأكد من تطابق المساحة {m(str(ans))}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 15: olym_t2_geo_ceva_menelaus_mass (OLYM-T2-211..225)
    # ------------------------------------------------------------------
    bp15 = "olym_t2_geo_ceva_menelaus_mass"

    # Easy (211..215): Ceva's Theorem solving for DC
    ceva_easy = [
        (2, 3, 6, 5, 2),   # (2/3)*(6/DC)*(5/2) = 1 => 60 / (6*DC) = 1 => DC = 10? Wait: (2*6*5)/(3*2) = 10
        (3, 4, 8, 5, 3),   # (3*8*5)/(4*3) = 10 -> pick BD=12 -> DC = 15
        (4, 5, 10, 3, 2),  # (4*10*3)/(5*2) = 12
        (5, 3, 6, 4, 5),   # (5*6*4)/(3*5) = 8
        (3, 7, 14, 5, 2),  # (3*14*5)/(7*2) = 15 -> pick CE=6 -> (3*14*6)/(7*2) = 18
    ]
    ceva_easy[1] = (3, 4, 12, 5, 3)
    ceva_easy[4] = (3, 7, 14, 6, 2)
    for offset, (af, fb, bd, ce, ea) in enumerate(ceva_easy, 211):
        qid = f"OLYM-T2-{offset:03d}"
        num_dc = af * bd * ce
        den_dc = fb * ea
        assert num_dc % den_dc == 0
        ans = num_dc // den_dc
        assert Fraction(af, fb) * Fraction(bd, ans) * Fraction(ce, ea) == 1
        q_en = (
            f"In {m('\\triangle ABC')}, cevians {m('AD, BE, CF')} concur at an interior point {m('P')}. "
            f"Given {m(f'AF = {af}')}, {m(f'FB = {fb}')}, {m(f'BD = {bd}')}, {m(f'CE = {ce}')}, and {m(f'EA = {ea}')}, "
            f"find {m('DC')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} تتلاقى القطع السيفية {m('AD, BE, CF')} في نقطة داخلية {m('P')}. "
            f"إذا كان {m(f'AF = {af}')} و{m(f'FB = {fb}')} و{m(f'BD = {bd}')} و{m(f'CE = {ce}')} و{m(f'EA = {ea}')}، "
            f"فأوجد طول {m('DC')}."
        )
        svg = svg_stu_ceva_triangle(str(af), str(fb), str(bd), "?", str(ce), str(ea))
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp15,
            q_en, q_ar, ans,
            [bd, ans + 3, max(1, ans - 3), (af * bd) // max(1, fb)],
            f"Apply Ceva's theorem: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
            f"طبّق مبرهنة سيفا: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
            "Set the cyclic product of side-division ratios equal to 1 by Ceva's Theorem.",
            [
                f"By Ceva's theorem for concurrent cevians, {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
                f"Substitute the known segments: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bd}}}{{DC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"Solving for {m('DC')} gives {m(f'DC = \\frac{{{af} \\cdot {bd} \\cdot {ce}}}{{{fb} \\cdot {ea}}} = {ans}')}.",
            ],
            f"Cyclic ratio check: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bd}}}{{{ans}}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
            "نجعل الجداء الدوري لنسب تقسيم الأضلاع مساوياً للواحد بموجب مبرهنة سيفا.",
            [
                f"من مبرهنة سيفا للقطع المتلاقية: {m('\\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1')}.",
                f"بالتعويض بالأطوال المعطاة: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bd}}}{{DC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"ومنه نجد {m(f'DC = {ans}')}.",
            ],
            f"جداء النسب الثلاث يساوي {m('1')} تماماً.",
            diagram_en=svg,
        ))

    # Medium (216..220): Mass points / Van Aubel's theorem AP / PD = AE / EC + AF / FB
    aubel_med = [
        ((2, 3), (3, 4), 46),   # AP/PD = 2/3 + 3/4 = 17/12; given AD = 58 -> AP = 34! Let's set AD = 29 -> AP = 17
        ((3, 5), (1, 2), 31),   # AP/PD = 3/5 + 1/2 = 11/10; AD = 42 -> AP = 22
        ((4, 3), (2, 5), 52),   # AP/PD = 4/3 + 2/5 = 26/15; AD = 41 -> AP = 26
        ((5, 4), (3, 2), 44),   # AP/PD = 5/4 + 3/2 = 11/4; AD = 45 -> AP = 33
        ((3, 2), (4, 5), 66),   # AP/PD = 3/2 + 4/5 = 23/10; AD = 66 -> AP = 46
    ]
    aubel_med[0] = ((2, 3), (3, 4), 29)
    aubel_med[1] = ((3, 5), (1, 2), 42)
    aubel_med[2] = ((4, 3), (2, 5), 41)
    aubel_med[3] = ((5, 4), (3, 2), 45)
    for offset, ((ae_r, ec_r), (af_r, fb_r), ad_tot) in enumerate(aubel_med, 216):
        qid = f"OLYM-T2-{offset:03d}"
        ratio_ap_pd = Fraction(ae_r, ec_r) + Fraction(af_r, fb_r)
        ap_f = ad_tot * ratio_ap_pd / (1 + ratio_ap_pd)
        assert ap_f.denominator == 1
        ans = int(ap_f)
        q_en = (
            f"In {m('\\triangle ABC')}, concurrent cevians {m('AD, BE, CF')} meet at {m('P')}. "
            f"If {m(f'\\frac{{AE}}{{EC}} = \\frac{{{ae_r}}}{{{ec_r}}}')}, {m(f'\\frac{{AF}}{{FB}} = \\frac{{{af_r}}}{{{fb_r}}}')}, "
            f"and {m(f'AD = {ad_tot}')}, find the length {m('AP')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} تتلاقى القطع السيفية {m('AD, BE, CF')} في النقطة {m('P')}. "
            f"إذا كان {m(f'\\frac{{AE}}{{EC}} = \\frac{{{ae_r}}}{{{ec_r}}}')} و{m(f'\\frac{{AF}}{{FB}} = \\frac{{{af_r}}}{{{fb_r}}}')} "
            f"وطول {m(f'AD = {ad_tot}')}، فأوجد طول {m('AP')}."
        )
        svg = svg_stu_ceva_triangle(str(af_r), str(fb_r), "BD", "?", str(ec_r), str(ae_r))
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp15,
            q_en, q_ar, ans,
            [ad_tot - ans, ans + 4, ans - 3, ad_tot // 2],
            f"By mass points (or Van Aubel's theorem), {m('\\frac{AP}{PD} = \\frac{AE}{EC} + \\frac{AF}{FB}')}.",
            f"بطريقة مراكز الكتل (أو مبرهنة فان أوبل): {m('\\frac{AP}{PD} = \\frac{AE}{EC} + \\frac{AF}{FB}')}.",
            "Assign vertex masses balancing E and F, or apply Van Aubel's identity AP/PD = AE/EC + AF/FB.",
            [
                f"By Van Aubel's theorem (mass points at {m('A, B, C')}), {m(f'\\frac{{AP}}{{PD}} = \\frac{{{ae_r}}}{{{ec_r}}} + \\frac{{{af_r}}}{{{fb_r}}} = {ratio_ap_pd}')}.",
                f"Thus {m('AP')} is {m(f'\\frac{{{ratio_ap_pd.numerator}}}{{{ratio_ap_pd.numerator + ratio_ap_pd.denominator}}}')} of {m('AD')}.",
                f"Multiply by {m(f'AD = {ad_tot}')}: {m(f'AP = {ad_tot} \\cdot \\frac{{{ratio_ap_pd.numerator}}}{{{ratio_ap_pd.numerator + ratio_ap_pd.denominator}}} = {ans}')}.",
            ],
            f"Then {m(f'PD = {ad_tot - ans}')} and {m(f'AP/PD = {ans}/{ad_tot - ans} = {ratio_ap_pd}')}.",
            "نوازن الكتل النقطية عند الرؤوس أو نطبق مبرهنة فان أوبل مباشرة لحساب نسبة تقسيم القطعة السيفية.",
            [
                f"بموجب مبرهنة فان أوبل: {m(f'\\frac{{AP}}{{PD}} = \\frac{{{ae_r}}}{{{ec_r}}} + \\frac{{{af_r}}}{{{fb_r}}} = {ratio_ap_pd}')}.",
                f"إذن تمثل {m('AP')} نسبة {m(f'\\frac{{{ratio_ap_pd.numerator}}}{{{ratio_ap_pd.numerator + ratio_ap_pd.denominator}}}')} من طول {m('AD')}.",
                f"بالضرب في {m(f'AD = {ad_tot}')} نجد {m(f'AP = {ans}')}.",
            ],
            f"الجزء المتبقي هو {m(f'PD = {ad_tot - ans}')} ونسبتهما تساوي {m(f'{ratio_ap_pd}')}.",
            diagram_en=svg,
        ))

    # Hard (221..225): Menelaus's Theorem on transversal meeting extension of BC at X beyond C
    menelaus_hard = [
        (3, 2, 1, 3, 10),   # AF/FB = 3/2, AE/EC = 3/1 => CE/EA = 1/3; Menelaus: (3/2)*(BX/XC)*(1/3) = 1 => BX/XC = 2 => (10+CX)/CX = 2 => CX = 10? Pick AF/FB=4/1, CE/EA=1/2 -> BX/XC = 1/2 impossible (BX > XC!). Need (AF/FB)*(CE/EA) < 1!
    ]
    # Note: X is on ray BC beyond C => BX = BC + CX > CX => BX/XC > 1 => need (AF/FB)*(CE/EA) < 1!
    menelaus_hard = [
        (2, 3, 1, 2, 12),   # (2/3)*(BX/XC)*(1/2) = 1 => BX/XC = 3 => (12+CX)/CX = 3 => CX = 6
        (3, 5, 2, 3, 15),   # (3/5)*(BX/XC)*(2/3) = 1 => BX/XC = 5/2 => (15+CX)/CX = 5/2 => CX = 10
        (1, 2, 3, 4, 10),   # (1/2)*(BX/XC)*(3/4) = 1 => BX/XC = 8/3 => (10+CX)/CX = 8/3 => CX = 6 -> pick BC=15 -> CX = 9
        (2, 5, 3, 4, 14),   # (2/5)*(BX/XC)*(3/4) = 1 => BX/XC = 10/3 => (14+CX)/CX = 10/3 => CX = 6 -> pick BC=28 -> CX = 12
        (3, 4, 1, 2, 20),   # (3/4)*(BX/XC)*(1/2) = 1 => BX/XC = 8/3 => pick (3, 7, 1, 2, 18): (3/7)*(1/2)=3/14 => BX/XC = 14/3 => 11 CX = 54; pick BC=22 -> CX = 6? Pick BC=33 -> CX = 9 -> pick (2, 7, 3, 4, 11): (2/7)*(3/4)=3/14 => BX/XC=14/3 => 11 CX = 33 -> pick BC=55 -> CX = 15!
    ]
    menelaus_hard[2] = (1, 2, 3, 4, 15)
    menelaus_hard[3] = (2, 5, 3, 4, 28)
    menelaus_hard[4] = (2, 7, 3, 4, 55)
    for offset, (af, fb, ce, ea, bc_len) in enumerate(menelaus_hard, 221):
        qid = f"OLYM-T2-{offset:03d}"
        prod_other = Fraction(af * ce, fb * ea)
        assert prod_other < 1
        ratio_bx_xc = Fraction(1, 1) / prod_other
        cx_f = Fraction(bc_len, 1) / (ratio_bx_xc - 1)
        assert cx_f.denominator == 1
        ans = int(cx_f)
        assert Fraction(af, fb) * Fraction(bc_len + ans, ans) * Fraction(ce, ea) == 1
        q_en = (
            f"In {m('\\triangle ABC')}, point {m('F')} lies on {m('AB')} with {m(f'AF : FB = {af} : {fb}')}, "
            f"and point {m('E')} lies on {m('AC')} with {m(f'CE : EA = {ce} : {ea}')}. Line {m('FE')} meets "
            f"the extension of {m('BC')} beyond {m('C')} at {m('X')}. Given {m(f'BC = {bc_len}')}, find {m('CX')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} تقع {m('F')} على {m('AB')} بنسبة {m(f'AF : FB = {af} : {fb}')}، "
            f"وتقع {m('E')} على {m('AC')} بنسبة {m(f'CE : EA = {ce} : {ea}')}. يقطع المستقيم {m('FE')} "
            f"امتداد الضلع {m('BC')} بعد {m('C')} في النقطة {m('X')}. إذا كان {m(f'BC = {bc_len}')} فأوجد طول {m('CX')}."
        )
        svg = svg_stu_ceva_triangle(str(af), str(fb), str(bc_len), "CX=?", str(ce), str(ea))
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp15,
            q_en, q_ar, ans,
            [bc_len + ans, ans + 4, max(1, ans - 3), bc_len // 2],
            f"Apply Menelaus's theorem to {m('\\triangle ABC')} and transversal {m('F-E-X')}: {m('\\frac{AF}{FB} \\cdot \\frac{BX}{XC} \\cdot \\frac{CE}{EA} = 1')}.",
            f"طبّق مبرهنة منيلاوس على المثلث {m('ABC')} والقاطع {m('F-E-X')}: {m('\\frac{AF}{FB} \\cdot \\frac{BX}{XC} \\cdot \\frac{CE}{EA} = 1')}.",
            "Use Menelaus's theorem with BX = BC + CX to solve for the external segment CX.",
            [
                f"By Menelaus's theorem on {m('\\triangle ABC')} cut by line {m('FEX')}, {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{BX}}{{XC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"Thus {m(f'\\frac{{BX}}{{XC}} = {ratio_bx_xc}')}. Since {m('X')} lies beyond {m('C')}, {m(f'BX = {bc_len} + CX')}.",
                f"Solving {m(f'\\frac{{{bc_len} + CX}}{{CX}} = {ratio_bx_xc}')} yields {m(f'CX = {ans}')}.",
            ],
            f"Check: {m(f'BX = {bc_len + ans}')}, and {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{{bc_len + ans}}}{{{ans}}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
            "نطبق مبرهنة منيلاوس مع كتابة BX = BC + CX لإيجاد طول القطعة الخارجية CX.",
            [
                f"من مبرهنة منيلاوس على المثلث {m('ABC')} والقاطع {m('FEX')}: {m(f'\\frac{{{af}}}{{{fb}}} \\cdot \\frac{{BX}}{{XC}} \\cdot \\frac{{{ce}}}{{{ea}}} = 1')}.",
                f"ومنه {m(f'\\frac{{BX}}{{XC}} = {ratio_bx_xc}')}، وبما أن {m('X')} بعد {m('C')} فإن {m(f'BX = {bc_len} + CX')}.",
                f"بحل المعادلة الكسرية نجد {m(f'CX = {ans}')}.",
            ],
            f"التحقق: عند {m(f'BX = {bc_len + ans}')} يصبح جداء النسب الثلاث مساوياً {m('1')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 16: olym_t2_geo_stewart_apollonius_bisect (OLYM-T2-226..240)
    # ------------------------------------------------------------------
    bp16 = "olym_t2_geo_stewart_apollonius_bisect"

    # Easy (226..230): Apollonius's median theorem 4 m_a^2 = 2 b^2 + 2 c^2 - a^2
    apol_easy = [
        (10, 7, 9),    # a=10, b=7, c=9 -> 2(49+81) - 100 = 160 -> m_a^2 = 40; or pick exact integer medians!
    ]
    # Let's check exact integer medians!
    # 1. a=16, b=11, c=13: 2(121+169) - 256 = 580 - 256 = 324 -> m_a^2 = 81 -> m_a = 9! (11+13=24>16)
    # 2. a=14, b=13, c=15: 2(169+225) - 196 = 788 - 196 = 592 -> m_b on b=14 (sides 13, 15, base 14): 592/4=148; what about base a=16, b=13, c=15? 788-256=532; base a=24, b=13, c=19? 2(169+361)-576=1060-576=484 -> m_a^2=121 -> m_a=11! (13+19=32>24!)
    # 3. a=10, b=7, c=11: 2(49+121)-100 = 340-100=240; a=8, b=7, c=9: 2(49+81)-64 = 196 -> m_a^2 = 49 -> m_a = 7! (7+8>9!)
    # 4. a=12, b=8, c=10: 2(64+100)-144 = 328-144=184; a=14, b=9, c=13: 2(81+169)-196 = 500-196=304; a=12, b=10, c=14: 2(100+196)-144=448; a=18, b=11, c=17: 2(121+289)-324=820-324=496; a=20, b=14, c=18: 2(196+324)-400=640; a=14, b=11, c=17: 2(410)-196=624; a=22, b=13, c=17: 2(458)-484=432; a=22, b=17, c=19: 2(289+361)-484=1300-484=816; a=26, b=17, c=19: 1300-676=624; a=16, b=14, c=22: 2(196+484)-256=1360-256=1104; double #3? Better: take u=m_a, half-base h=a/2: b^2 + c^2 = 2(u^2 + h^2)!
    #    - u=8, h=6 (a=12): u^2+h^2=100 -> 2*100 = 200 = 6^2 + 14^2 (6+12>14, scalene! b=6? 6+12=18>14, yes! 6, 14, 12: m_a = 8!) or 200 = 2^2 + 14^2 no;
    #    - u=10, h=5 (a=10): 2*125 = 250 = 9^2 + 13^2! Check triangle (10, 9, 13): 9+10=19>13, scalene! 2(81+169)-100 = 400 -> m_a = 10!
    #    - u=12, h=9 (a=18): 2*225 = 450 = 9^2 + 19^2? 81+361=442; 450 = 3^2+21^2 no; u=13, h=4 (a=8): 2*185 = 370 = 9^2 + 17^2 (8+9=17 degenerate) or 370 = 11^2 + 15^2? 121+225=346; u=12, h=5 (a=10): 2*169 = 338 = 7^2 + 17^2 (7+10=17 degenerate); u=15, h=8 (a=16): 2*289 = 578 = 7^2 + 23^2 (7+16=23 degenerate); wait: 17^2+17^2 is isosceles; u=13, h=9 (a=18): 2*250 = 500 = 10^2 + 20^2 (10+18=28>20! Scalene (18, 10, 20): 2(100+400)-324 = 676 = 26^2 -> m_a = 13!)!
    apol_easy = [
        (8, 7, 9, 7),      # m_a = 7
        (10, 9, 13, 10),   # m_a = 10
        (16, 11, 13, 9),   # m_a = 9
        (24, 13, 19, 11),  # m_a = 11
        (18, 10, 20, 13),  # m_a = 13
    ]
    for offset, (a_s, b_s, c_s, m_ans) in enumerate(apol_easy, 226):
        qid = f"OLYM-T2-{offset:03d}"
        assert a_s < b_s + c_s and b_s < a_s + c_s and c_s < a_s + b_s
        assert 2 * (b_s**2 + c_s**2) - a_s**2 == 4 * m_ans**2
        ans = m_ans
        q_en = (
            f"In {m('\\triangle ABC')}, the side lengths are {m(f'BC = {a_s}')}, {m(f'CA = {b_s}')}, "
            f"and {m(f'AB = {c_s}')}. Find the length of the median {m('AM')} drawn from {m('A')} to the midpoint {m('M')} of {m('BC')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} أطوال الأضلاع هي {m(f'BC = {a_s}')} و{m(f'CA = {b_s}')} و{m(f'AB = {c_s}')}. "
            f"أوجد طول المتوسط {m('AM')} المرسوم من {m('A')} إلى منتصف {m('BC')}."
        )
        svg = svg_median_tri(str(c_s), str(b_s), str(a_s), "AM=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp16,
            q_en, q_ar, ans,
            [(b_s + c_s) // 2 if (b_s + c_s) // 2 != ans else ans + 2, ans + 1, ans - 1, a_s // 2 if a_s // 2 != ans else ans + 3],
            f"Apply Apollonius's theorem: {m('AB^2 + AC^2 = 2(AM^2 + BM^2)')}, where {m(f'BM = {a_s // 2}')}.",
            f"طبّق مبرهنة أبولونيوس للمتوسط: {m('AB^2 + AC^2 = 2(AM^2 + BM^2)')} حيث {m(f'BM = {a_s // 2}')}.",
            "Use Apollonius's formula 4*AM^2 = 2*AB^2 + 2*AC^2 - BC^2 to find the median length.",
            [
                f"By Apollonius's median theorem, {m('2(AB^2 + AC^2) - BC^2 = 4 AM^2')}.",
                f"Substitute the side lengths: {m(f'4 AM^2 = 2({c_s}^2 + {b_s}^2) - {a_s}^2 = {2*(b_s**2 + c_s**2)} - {a_s**2} = {4 * m_ans**2}')}.",
                f"Divide by {m('4')} and take the square root: {m(f'AM = \\sqrt{{{m_ans**2}}} = {ans}')}.",
            ],
            f"Check: {m(f'2(AM^2 + BM^2) = 2({ans}^2 + {(a_s//2)}^2) = {2*(ans**2 + (a_s//2)**2)} = {c_s**2 + b_s**2}')}.",
            "نستعمل صيغة أبولونيوس لطول المتوسط بدلالة أضلاع المثلث الثلاثة.",
            [
                f"بموجب مبرهنة أبولونيوس: {m('4 AM^2 = 2(AB^2 + AC^2) - BC^2')}.",
                f"بالتعويض نحصل على {m(f'4 AM^2 = 2({c_s}^2 + {b_s}^2) - {a_s}^2 = {4 * m_ans**2}')}.",
                f"بالقسمة على {m('4')} وأخذ الجذر التربيعي نجد {m(f'AM = {ans}')}.",
            ],
            f"التحقق: {m(f'2({ans}^2 + {(a_s//2)}^2) = {c_s**2 + b_s**2}')}.",
            diagram_en=svg,
        ))

    # Medium (231..235): Internal Angle Bisector Length AD = sqrt(AB*AC - BD*DC)
    bis_med = [
        (5, 20, 20, 4, 16, 6),       # AD = 6
        (9, 18, 21, 7, 14, 8),       # AD = 8
        (13, 52, 60, 12, 48, 10),    # AD = 10
        (13, 117, 120, 12, 108, 15), # AD = 15
        (20, 45, 52, 16, 36, 18),    # AD = 18
    ]
    for offset, (ab, ac, bc, bd, dc, ad_ans) in enumerate(bis_med, 231):
        qid = f"OLYM-T2-{offset:03d}"
        assert ab < ac + bc and ac < ab + bc and bc < ab + ac
        assert bd + dc == bc and bd * ac == dc * ab
        assert ab * ac - bd * dc == ad_ans * ad_ans
        ans = ad_ans
        q_en = (
            f"In {m('\\triangle ABC')}, {m(f'AB = {ab}')}, {m(f'AC = {ac}')}, and {m(f'BC = {bc}')}. "
            f"The internal angle bisector of {m('\\angle BAC')} meets {m('BC')} at {m('D')}. Find the length {m('AD')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} لدينا {m(f'AB = {ab}')} و{m(f'AC = {ac}')} و{m(f'BC = {bc}')}. "
            f"يقطع المنصف الداخلي للزاوية {m('\\angle BAC')} الضلع {m('BC')} في {m('D')}. أوجد الطول {m('AD')}."
        )
        svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "AD=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp16,
            q_en, q_ar, ans,
            [bd if bd != ans else ans + 2, ans + 3, max(1, ans - 2), (ab + ac) // 3 if (ab + ac) // 3 != ans else ans + 4],
            f"First find {m('BD')} and {m('DC')} via {m('BD : DC = AB : AC')}, then apply {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}.",
            f"أوجد أولاً {m('BD')} و{m('DC')} من التناسب {m('BD : DC = AB : AC')} ثم طبّق {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}.",
            "Combine the Angle Bisector Ratio Theorem with Stewart's bisector formula AD^2 = AB*AC - BD*DC.",
            [
                f"By the Angle Bisector Theorem, {m(f'BD : DC = {ab} : {ac}')} with {m(f'BD + DC = {bc}')}, giving {m(f'BD = {bd}')} and {m(f'DC = {dc}')}.",
                f"Apply the angle bisector length identity: {m(f'AD^2 = AB \\cdot AC - BD \\cdot DC = {ab} \\cdot {ac} - {bd} \\cdot {dc} = {ad_ans**2}')}.",
                f"Taking the square root gives {m(f'AD = {ans}')}.",
            ],
            f"Check via full Stewart's theorem: {m(f'{ac}^2({bd}) + {ab}^2({dc}) = {bc}({ans}^2 + {bd}\\cdot{dc})')}.",
            "نجمع بين مبرهنة منصف الزاوية وصيغة طول المنصف الداخلي المستنتجة من مبرهنة ستيوارت.",
            [
                f"من مبرهنة المنصف الداخلي {m(f'BD : DC = {ab} : {ac}')} ومجموعهما {m(str(bc))}، فنجد {m(f'BD = {bd}')} و{m(f'DC = {dc}')}.",
                f"نطبق صيغة طول المنصف: {m(f'AD^2 = {ab} \\cdot {ac} - {bd} \\cdot {dc} = {ad_ans**2}')}.",
                f"بأخذ الجذر التربيعي نحصل على {m(f'AD = {ans}')}.",
            ],
            f"يتطابق الناتج مع التعويض المباشر في مبرهنة ستيوارت.",
            diagram_en=svg,
        ))

    # Hard (236..240): General Stewart's Theorem b^2 m + c^2 n = a(d^2 + m n) computing AD^2
    stew_hard = [
        (13, 15, 14, 6, 8),    # c=13, b=15, a=14, m=6, n=8 -> (225*6 + 169*8)/14 - 48 = (1350+1352)/14 - 48 = 193 - 48 = 145
        (10, 17, 21, 7, 14),   # c=10, b=17, a=21, m=7, n=14 -> (289*7 + 100*14)/21 - 98 = 3423/21 - 98 = 163 - 98 = 65
        (13, 20, 21, 7, 14),   # c=13, b=20, a=21, m=7, n=14 -> (400*7 + 169*14)/21 - 98 = 5166/21 - 98 = 246 - 98 = 148
        (15, 13, 14, 4, 10),   # c=15, b=13, a=14, m=4, n=10 -> (169*4 + 225*10)/14 - 40 = 2926/14 - 40 = 209 - 40 = 169
        (17, 25, 28, 8, 20),   # c=17, b=25, a=28, m=8, n=20 -> (625*8 + 289*20)/28 - 160 = 10780/28 - 160 = 385 - 160 = 225
    ]
    for offset, (c_ab, b_ac, a_bc, m_bd, n_dc) in enumerate(stew_hard, 236):
        qid = f"OLYM-T2-{offset:03d}"
        assert m_bd + n_dc == a_bc
        assert c_ab < b_ac + a_bc and b_ac < c_ab + a_bc and a_bc < c_ab + b_ac
        lhs_num = b_ac * b_ac * m_bd + c_ab * c_ab * n_dc
        assert lhs_num % a_bc == 0
        ans = lhs_num // a_bc - m_bd * n_dc
        assert ans > 0 and a_bc * (ans + m_bd * n_dc) == lhs_num
        q_en = (
            f"In {m('\\triangle ABC')}, {m(f'AB = {c_ab}')}, {m(f'AC = {b_ac}')}, and {m(f'BC = {a_bc}')}. "
            f"Point {m('D')} lies on segment {m('BC')} with {m(f'BD = {m_bd}')} and {m(f'DC = {n_dc}')}. "
            f"Using Stewart's theorem, compute {m('AD^2')}."
        )
        q_ar = (
            f"في المثلث {m('ABC')} لدينا {m(f'AB = {c_ab}')} و{m(f'AC = {b_ac}')} و{m(f'BC = {a_bc}')}. "
            f"تقع النقطة {m('D')} على الضلع {m('BC')} بحيث {m(f'BD = {m_bd}')} و{m(f'DC = {n_dc}')}. "
            f"باستخدام مبرهنة ستيوارت، احسب قيمة {m('AD^2')}."
        )
        svg = svg_median_tri(str(c_ab), str(b_ac), f"{m_bd}+{n_dc}", "AD²=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp16,
            q_en, q_ar, ans,
            [ans + m_bd * n_dc, ans - 12, ans + 15, c_ab * b_ac - m_bd * n_dc],
            f"Apply Stewart's theorem: {m('AC^2 \\cdot BD + AB^2 \\cdot DC = BC(AD^2 + BD \\cdot DC)')}.",
            f"طبّق مبرهنة ستيوارت: {m('AC^2 \\cdot BD + AB^2 \\cdot DC = BC(AD^2 + BD \\cdot DC)')}.",
            "Relate the interior cevian length to the three side lengths and base segments via Stewart's identity.",
            [
                f"Write Stewart's relation on {m('\\triangle ABC')}: {m('b^2 m + c^2 n = a(d^2 + mn)')}.",
                f"Substitute {m(f'{b_ac}^2({m_bd}) + {c_ab}^2({n_dc}) = {lhs_num} = {a_bc}(AD^2 + {m_bd} \\cdot {n_dc})')}.",
                f"Divide by {m(str(a_bc))} and subtract {m(str(m_bd * n_dc))}: {m(f'AD^2 = {lhs_num // a_bc} - {m_bd * n_dc} = {ans}')}.",
            ],
            f"Check: {m(f'{a_bc}({ans} + {m_bd * n_dc}) = {lhs_num}')}, matching {m(f'{b_ac}^2({m_bd}) + {c_ab}^2({n_dc})')}.",
            "نربط مربع طول القطعة السيفية بأضلاع المثلث وجزأي القاعدة عبر متطابقة ستيوارت.",
            [
                f"نكتب علاقة ستيوارت: {m('AC^2 \\cdot BD + AB^2 \\cdot DC = BC(AD^2 + BD \\cdot DC)')}.",
                f"بالتعويض نجد {m(f'{lhs_num} = {a_bc}(AD^2 + {m_bd * n_dc})')}.",
                f"بالقسمة على {m(str(a_bc))} وطرح {m(str(m_bd * n_dc))} نحصل على {m(f'AD^2 = {ans}')}.",
            ],
            f"التحقق العكسي يعطي {m(f'{a_bc}({ans} + {m_bd * n_dc}) = {lhs_num}')} بدقة.",
            diagram_en=svg,
        ))

    return qs



# ==============================================================================
# UNIT 2.5 — Geometry II: Triangle Centers, Homothety & 3D (OLYM-T2-241 .. 300)
# ==============================================================================

def _gen_u25_geometry_ii() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 17: olym_t2_geo_euler_line_nine_point (OLYM-T2-241..255)
    # ------------------------------------------------------------------
    bp17 = "olym_t2_geo_euler_line_nine_point"

    # Easy (241..245): Euler line ratio OH = 3 * OG and GH = 2 * OG
    euler_easy = [4, 7, 9, 11, 15]
    for offset, og_len in enumerate(euler_easy, 241):
        qid = f"OLYM-T2-{offset:03d}"
        ans = 3 * og_len
        gh_len = 2 * og_len
        assert og_len + gh_len == ans
        q_en = (
            f"In non-equilateral {m('\\triangle ABC')}, let {m('O')}, {m('G')}, and {m('H')} denote the "
            f"circumcenter, centroid, and orthocenter, respectively. If {m(f'OG = {og_len}')}, find the "
            f"distance {m('OH')} along the Euler line."
        )
        q_ar = (
            f"في المثلث غير المتطابق الأضلاع {m('ABC')}، ليكن {m('O')} مركز الدائرة المحيطة و{m('G')} مركز الثقل "
            f"و{m('H')} ملتقى الارتفاعات. إذا كان {m(f'OG = {og_len}')}، فأوجد المسافة {m('OH')} على خط أويلر."
        )
        svg = svg_olym_nine_point_euler(f"OG={og_len}", "G", "OH=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp17,
            q_en, q_ar, ans,
            [gh_len, 4 * og_len, og_len + 6, ans - 3],
            f"On the Euler line, the centroid {m('G')} divides segment {m('OH')} in the ratio {m('OG : GH = 1 : 2')}.",
            f"على خط أويلر يقسم مركز الثقل {m('G')} القطعة {m('OH')} بنسبة {m('OG : GH = 1 : 2')}.",
            "Use Euler's collinearity theorem: G lies between O and H with GH = 2*OG, so OH = 3*OG.",
            [
                f"By Euler's theorem, {m('O, G, H')} are collinear in that order with {m('GH = 2 \\cdot OG')}.",
                f"Compute {m(f'GH = 2 \\cdot {og_len} = {gh_len}')}.",
                f"Therefore {m(f'OH = OG + GH = {og_len} + {gh_len} = {ans}')}.",
            ],
            f"The homothety centered at {m('G')} with scale factor {m('-2')} maps {m('O')} to {m('H')}, confirming {m(f'OH = 3 \\cdot {og_len} = {ans}')}.",
            "تقع النقاط O وG وH على استقامة واحدة (خط أويلر) بحيث GH = 2 OG ومنه OH = 3 OG.",
            [
                f"بموجب مبرهنة خط أويلر تقع {m('G')} بين {m('O')} و{m('H')} وتحقق {m('GH = 2 \\cdot OG')}.",
                f"نحسب {m(f'GH = 2 \\cdot {og_len} = {gh_len}')}.",
                f"إذن الطول الكلي هو {m(f'OH = OG + GH = {ans}')}.",
            ],
            f"التحاكي الذي مركزه {m('G')} ونسبته {m('-2')} ينقل {m('O')} إلى {m('H')} فيؤكد أن {m(f'OH = {ans}')}.",
            diagram_en=svg,
        ))

    # Medium (246..250): Nine-point circle radius R_9 = R/2 and center N midpoint of OH
    euler_med = [
        (14, 12),   # R=14, OH=12 -> R_9 = 7, ON = 6 -> R_9 + ON = 13
        (18, 16),   # R=18, OH=16 -> R_9 = 9, ON = 8 -> 17
        (22, 20),   # R=22, OH=20 -> R_9 = 11, ON = 10 -> 21
        (26, 18),   # R=26, OH=18 -> R_9 = 13, ON = 9 -> 22
        (30, 24),   # R=30, OH=24 -> R_9 = 15, ON = 12 -> 27
    ]
    for offset, (R_circ, oh_dist) in enumerate(euler_med, 246):
        qid = f"OLYM-T2-{offset:03d}"
        r9 = R_circ // 2
        on_dist = oh_dist // 2
        ans = r9 + on_dist
        q_en = (
            f"Triangle {m('ABC')} has circumradius {m(f'R = {R_circ}')}, and the distance between its "
            f"circumcenter {m('O')} and orthocenter {m('H')} is {m(f'OH = {oh_dist}')}. Let {m('N')} and {m('R_9')} "
            f"be the center and radius of the nine-point circle of {m('\\triangle ABC')}. Compute {m('R_9 + ON')}."
        )
        q_ar = (
            f"مثلث {m('ABC')} نصف قطر دائرته المحيطة {m(f'R = {R_circ}')} والمسافة بين مركزها {m('O')} "
            f"وملتقى الارتفاعات {m('H')} هي {m(f'OH = {oh_dist}')}. ليكن {m('N')} مركز دائرة النقاط التسع "
            f"و{m('R_9')} نصف قطرها. احسب {m('R_9 + ON')}."
        )
        svg = svg_olym_nine_point_euler(f"R={R_circ}", "N=?", f"OH={oh_dist}")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp17,
            q_en, q_ar, ans,
            [R_circ + on_dist, r9 + oh_dist // 3, ans + 4, ans - 3],
            f"The nine-point circle has radius {m('R_9 = R/2')} and its center {m('N')} is the midpoint of {m('OH')}.",
            f"نصف قطر دائرة النقاط التسع يساوي {m('R_9 = R/2')} ومركزها {m('N')} يقع في منتصف القطعة {m('OH')}.",
            "Use the homothety of ratio 1/2 from H (or -1/2 from G): R_9 = R/2 and ON = OH/2.",
            [
                f"A homothety centered at {m('H')} with scale factor {m('1/2')} maps the circumcircle to the nine-point circle.",
                f"Thus {m(f'R_9 = \\frac{{R}}{{2}} = \\frac{{{R_circ}}}{{2}} = {r9}')}, and {m('N')} is the midpoint of {m('OH')}, so {m(f'ON = \\frac{{{oh_dist}}}{{2}} = {on_dist}')}.",
                f"Adding the two quantities gives {m(f'R_9 + ON = {r9} + {on_dist} = {ans}')}.",
            ],
            f"Notice {m(f'GN = OH/6 = {oh_dist // 6 if oh_dist % 6 == 0 else Fraction(oh_dist, 6)}')}, consistent with Euler line ordering {m('O - G - N - H')}.",
            "التحاكي الذي مركزه H ونسبته 1/2 ينقل الدائرة المحيطة إلى دائرة النقاط التسع.",
            [
                f"نصف قطر دائرة النقاط التسع يساوي نصف شعاع الدائرة المحيطة: {m(f'R_9 = {R_circ}/2 = {r9}')}.",
                f"ومركزها {m('N')} هو منتصف {m('OH')}: {m(f'ON = {oh_dist}/2 = {on_dist}')}.",
                f"بجمع القيمتين نحصل على {m(f'R_9 + ON = {ans}')}.",
            ],
            f"ترتيب النقاط على خط أويلر هو {m('O, G, N, H')} ويحقق جميع النسب القياسية.",
            diagram_en=svg,
        ))

    # Hard (251..255): Distance from vertex A to orthocenter H: AH = 2*OM = sqrt(4R^2 - a^2)
    euler_hard = [
        (10, 16, 12),   # 2R=20, a=16 -> AH = 12
        (13, 10, 24),   # 2R=26, a=10 -> AH = 24
        (17, 16, 30),   # 2R=34, a=16 -> AH = 30
        (20, 24, 32),   # 2R=40, a=24 -> AH = 32
        (25, 14, 48),   # 2R=50, a=14 -> AH = 48
    ]
    for offset, (R_c, a_side, ah_ans) in enumerate(euler_hard, 251):
        qid = f"OLYM-T2-{offset:03d}"
        om_len = ah_ans // 2
        assert 4 * R_c * R_c - a_side * a_side == ah_ans * ah_ans
        assert om_len * om_len + (a_side // 2) ** 2 == R_c * R_c
        ans = ah_ans
        q_en = (
            f"In acute {m('\\triangle ABC')}, the circumradius is {m(f'R = {R_c}')} and side {m(f'BC = {a_side}')}. "
            f"Let {m('H')} be the orthocenter of {m('\\triangle ABC')}. Find the distance {m('AH')}."
        )
        q_ar = (
            f"في المثلث حاد الزوايا {m('ABC')}، نصف قطر الدائرة المحيطة هو {m(f'R = {R_c}')} وطول الضلع "
            f"{m(f'BC = {a_side}')}. ليكن {m('H')} ملتقى ارتفاعات المثلث. أوجد المسافة {m('AH')}."
        )
        svg = svg_olym_nine_point_euler(f"R={R_c}", f"a={a_side}", "AH=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp17,
            q_en, q_ar, ans,
            [om_len, 2 * R_c - a_side, ans - 4, ans + 4],
            f"Use Euler's theorem {m('AH = 2 \\cdot OM')}, where {m('M')} is the midpoint of {m('BC')} and {m('OM = \\sqrt{R^2 - (BC/2)^2}')}.",
            f"استعمل مبرهنة أويلر {m('AH = 2 \\cdot OM')} حيث {m('M')} منتصف {m('BC')} و{m('OM = \\sqrt{R^2 - (BC/2)^2}')}.",
            "By centroid homothety (or extended Law of Sines AH = 2R cos A), AH = 2*OM = sqrt(4R^2 - BC^2).",
            [
                f"Let {m('M')} be the midpoint of {m('BC')}. In right {m('\\triangle OMB')}, {m(f'OM = \\sqrt{{R^2 - (BC/2)^2}} = \\sqrt{{{R_c}^2 - {a_side // 2}^2}} = {om_len}')}.",
                f"Because the centroid {m('G')} divides both {m('AM')} and {m('OH')} in a {m('2 : 1')} ratio, {m('\\triangle AGH \\sim \\triangle MGO')} with ratio {m('2')}.",
                f"Therefore {m(f'AH = 2 \\cdot OM = 2 \\cdot {om_len} = {ans}')}.",
            ],
            f"Equivalently, {m(f'AH^2 + BC^2 = {ans}^2 + {a_side}^2 = {4 * R_c**2} = (2R)^2')}.",
            "من تشابه المثلثين حول مركز الثقل G (أو قانون الجيوب) يكون AH ضعف بُعد مركز الدائرة المحيطة عن الضلع المقابل.",
            [
                f"ليكن {m('M')} منتصف {m('BC')}؛ في المثلث القائم {m('OMB')} نجد {m(f'OM = \\sqrt{{{R_c}^2 - {a_side // 2}^2}} = {om_len}')}.",
                f"بما أن مركز الثقل {m('G')} يقسم كلاً من {m('AM')} و{m('OH')} بنسبة {m('2 : 1')} فإن {m('AH = 2 \\cdot OM')}.",
                f"إذن {m(f'AH = 2 \\times {om_len} = {ans}')}.",
            ],
            f"وبالمثل تتحقق المتطابقة {m(f'AH^2 + BC^2 = 4R^2 = {4 * R_c**2}')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 18: olym_t2_geo_excircles_carnot_inrad (OLYM-T2-256..270)
    # ------------------------------------------------------------------
    bp18 = "olym_t2_geo_excircles_carnot_inrad"

    # Easy (256..260): Incircle tangency segment AE = AF = s - a
    inc_easy = [
        (13, 14, 15),  # s = 21 -> s - a = 8
        (10, 17, 21),  # s = 24 -> s - a = 14
        (15, 22, 25),  # s = 31 -> s - a = 16
        (17, 25, 28),  # s = 35 -> s - a = 18
        (21, 29, 34),  # s = 42 -> s - a = 21
    ]
    for offset, (a_bc, b_ca, c_ab) in enumerate(inc_easy, 256):
        qid = f"OLYM-T2-{offset:03d}"
        s_val = (a_bc + b_ca + c_ab) // 2
        ans = s_val - a_bc
        assert ans + (s_val - b_ca) == c_ab and ans + (s_val - c_ab) == b_ca
        q_en = (
            f"The incircle of {m('\\triangle ABC')} touches sides {m('BC, CA, AB')} at {m('D, E, F')}, "
            f"respectively. If {m(f'BC = {a_bc}')}, {m(f'CA = {b_ca}')}, and {m(f'AB = {c_ab}')}, find the "
            f"tangent segment length {m('AE')}."
        )
        q_ar = (
            f"تمس الدائرة الداخلية للمثلث {m('ABC')} الأضلاع {m('BC, CA, AB')} في النقاط {m('D, E, F')} "
            f"على الترتيب. إذا كان {m(f'BC = {a_bc}')} و{m(f'CA = {b_ca}')} و{m(f'AB = {c_ab}')}، فأوجد طول قطعة المماس {m('AE')}."
        )
        svg = svg_olym_incircle_excircle(str(a_bc), str(b_ca), str(c_ab), "AE=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp18,
            q_en, q_ar, ans,
            [s_val - b_ca, s_val - c_ab, s_val, ans + 3],
            f"Equal tangents from each vertex give {m('AE = AF = s - BC')}, where {m('s = (AB + BC + CA)/2')}.",
            f"تساوي المماسات المرسومة من كل رأس يعطي {m('AE = AF = s - BC')} حيث {m('s')} نصف المحيط.",
            "Compute the semiperimeter s and subtract the opposite side BC to get AE = s - BC.",
            [
                f"Compute the semiperimeter: {m(f's = \\frac{{{a_bc} + {b_ca} + {c_ab}}}{{2}} = {s_val}')}.",
                f"By equal tangents from {m('A, B, C')}, {m('AE = AF = x')}, {m('BD = BF = y')}, {m('CD = CE = z')} with {m('x + y + z = s')}.",
                f"Since {m(f'y + z = BC = {a_bc}')}, we obtain {m(f'AE = s - BC = {s_val} - {a_bc} = {ans}')}.",
            ],
            f"Check: {m(f'BD = {s_val - b_ca}')} and {m(f'CD = {s_val - c_ab}')}, which sum to {m(f'{a_bc} = BC')}.",
            "نحسب نصف المحيط s ثم نطرح طول الضلع المقابل BC للحصول على طول المماس AE = s - BC.",
            [
                f"نحسب نصف المحيط: {m(f's = \\frac{{{a_bc} + {b_ca} + {c_ab}}}{{2}} = {s_val}')}.",
                f"من تساوي قطعتي المماس من كل رأس لدينا {m('AE + BD + CD = s')} مع {m(f'BD + CD = BC = {a_bc}')}.",
                f"إذن {m(f'AE = s - BC = {s_val} - {a_bc} = {ans}')}.",
            ],
            f"التحقق: {m(f'AE + CE = {ans} + {s_val - c_ab} = {b_ca} = CA')}.",
            diagram_en=svg,
        ))

    # Medium (261..265): Exradius r_c = Area / (s - c) on Heronian triangles
    exr_med = [
        (13, 14, 15, 84, 14),   # s=21, s-c=6 -> r_c = 84/6 = 14 -> wait: let's use distinct answers!
        (10, 17, 21, 84, 28),   # s=24, s-c=3 -> r_c = 84/3 = 28
        (13, 20, 21, 126, 21),  # s=27, s-c=6 -> r_c = 126/6 = 21
        (17, 25, 28, 210, 30),  # s=35, s-c=7 -> r_c = 210/7 = 30
        (25, 29, 36, 360, 40),  # s=45, s-c=9 -> r_c = 360/9 = 40
    ]
    for offset, (sa, sb, sc, area_val, rc_ans) in enumerate(exr_med, 261):
        qid = f"OLYM-T2-{offset:03d}"
        s_semi = (sa + sb + sc) // 2
        assert s_semi * (s_semi - sa) * (s_semi - sb) * (s_semi - sc) == area_val * area_val
        assert area_val == rc_ans * (s_semi - sc)
        ans = rc_ans
        q_en = (
            f"Triangle {m('ABC')} has side lengths {m(f'BC = {sa}')}, {m(f'CA = {sb}')}, and {m(f'AB = {sc}')}. "
            f"Find the radius {m('r_C')} of the excircle opposite vertex {m('C')} (tangent to side {m('AB')})."
        )
        q_ar = (
            f"أطوال أضلاع المثلث {m('ABC')} هي {m(f'BC = {sa}')} و{m(f'CA = {sb}')} و{m(f'AB = {sc}')}. "
            f"أوجد نصف قطر الدائرة الماسّة خارجياً {m('r_C')} المقابلة للرأس {m('C')} (الماسة للضلع {m('AB')})."
        )
        svg = svg_olym_incircle_excircle(str(sa), str(sb), str(sc), "r_C=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp18,
            q_en, q_ar, ans,
            [area_val // s_semi, area_val // (s_semi - sa), ans - 4, ans + 5],
            f"Compute the area {m('\\Delta')} by Heron's formula and use {m('r_C = \\frac{\\Delta}{s - AB}')}.",
            f"احسب المساحة {m('\\Delta')} بصيغة هيرون ثم طبّق القانون {m('r_C = \\frac{\\Delta}{s - AB}')}.",
            "Find the semiperimeter s and Heron area Delta, then divide Delta by (s - c).",
            [
                f"Compute the semiperimeter: {m(f's = \\frac{{{sa} + {sb} + {sc}}}{{2}} = {s_semi}')}.",
                f"By Heron's formula, {m(f'\\Delta = \\sqrt{{{s_semi}({s_semi - sa})({s_semi - sb})({s_semi - sc})}} = {area_val}')}.",
                f"The exradius opposite {m('C')} is {m(f'r_C = \\frac{{\\Delta}}{{s - AB}} = \\frac{{{area_val}}}{{{s_semi - sc}}} = {ans}')}.",
            ],
            f"Notice {m(f'r_C = {ans} > r = {area_val // s_semi}')}, as the excircle opposite the longest side is always larger than the incircle.",
            "نحسب نصف المحيط والمساحة بصيغة هيرون ثم نقسم المساحة على (s - AB).",
            [
                f"نصف المحيط هو {m(f's = {s_semi}')}.",
                f"بموجب صيغة هيرون تساوي مساحة المثلث {m(f'\\Delta = {area_val}')}.",
                f"نصف قطر الدائرة الماسّة خارجياً المقابلة للرأس {m('C')} هو {m(f'r_C = \\frac{{{area_val}}}{{{s_semi} - {sc}}} = {ans}')}.",
            ],
            f"نلاحظ أن {m(f'r_C = {ans}')} أكبر من نصف قطر الدائرة الداخلية {m(str(area_val // s_semi))}.",
            diagram_en=svg,
        ))

    # Hard (266..270): Steiner's Exradius Identity r_a + r_b + r_c = 4R + r & Carnot's Theorem
    carnot_hard = [
        (10, 4),   # R=10, r=4 -> r_a + r_b + r_c = 44
        (13, 5),   # R=13, r=5 -> 57
        (15, 6),   # R=15, r=6 -> 66
        (17, 7),   # R=17, r=7 -> 75
        (20, 8),   # R=20, r=8 -> 88
    ]
    for offset, (R_c, r_in) in enumerate(carnot_hard, 266):
        qid = f"OLYM-T2-{offset:03d}"
        assert R_c >= 2 * r_in  # Euler's inequality R >= 2r!
        ans = 4 * R_c + r_in
        carnot_sum = R_c + r_in
        q_en = (
            f"In an Intermediate Olympiad triangle geometry problem, {m('\\triangle ABC')} has circumradius "
            f"{m(f'R = {R_c}')} and inradius {m(f'r = {r_in}')}. Find the sum of its three exradii {m('r_a + r_b + r_c')}."
        )
        q_ar = (
            f"في مسألة هندسة مثلث للأولمبياد المتوسط، نصف قطر الدائرة المحيطة بالمثلث {m('ABC')} هو "
            f"{m(f'R = {R_c}')} ونصف قطر دائرته الداخلية {m(f'r = {r_in}')}. أوجد مجموع أنصاف أقطار الدوائر الماسّة خارجياً الثلاث {m('r_a + r_b + r_c')}."
        )
        svg = svg_olym_incircle_excircle(f"R={R_c}", f"r={r_in}", "Σrᵢ", "4R+r=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp18,
            q_en, q_ar, ans,
            [3 * R_c + r_in, 4 * R_c - r_in, carnot_sum, 2 * R_c + 3 * r_in],
            f"Apply Steiner's identity (linked to Carnot's theorem): {m('r_a + r_b + r_c - r = 4R')}.",
            f"طبّق متطابقة شتاينر (المرتبطة بمبرهنة كارنو): {m('r_a + r_b + r_c - r = 4R')}.",
            "Use Steiner's relation r_a + r_b + r_c = 4R + r.",
            [
                f"By Steiner's exradius theorem (a consequence of Carnot's theorem {m('d_a + d_b + d_c = R + r')}), {m('r_a + r_b + r_c - r = 4R')}.",
                f"Rearrange to isolate the sum of exradii: {m('r_a + r_b + r_c = 4R + r')}.",
                f"Substitute {m(f'R = {R_c}')} and {m(f'r = {r_in}')}: {m(f'4({R_c}) + {r_in} = {ans}')}.",
            ],
            f"Euler's inequality {m(f'R = {R_c} \\ge 2r = {2 * r_in}')} is satisfied, confirming a valid triangle configuration.",
            "نستعمل متطابقة شتاينر لمجموع أنصاف أقطار الدوائر الماسّة خارجياً r_a + r_b + r_c = 4R + r.",
            [
                f"بموجب مبرهنة شتاينر: {m('r_a + r_b + r_c - r = 4R')}.",
                f"بترتيب الحدود نجد {m('r_a + r_b + r_c = 4R + r')}.",
                f"بتعويض {m(f'R = {R_c}')} و{m(f'r = {r_in}')} نحصل على {m(f'4({R_c}) + {r_in} = {ans}')}.",
            ],
            f"متباينة أويلر {m(f'R \\ge 2r')} متحققة مما يؤكد صحة أبعاد المثلث.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 19: olym_t2_geo_homothety_rotation (OLYM-T2-271..285)
    # ------------------------------------------------------------------
    bp19 = "olym_t2_geo_homothety_rotation"

    # Easy (271..275): Area scaling under homothety [A'B'C'] = k^2 [ABC]
    hom_easy = [
        (Fraction(3, 2), 20),   # 9/4 * 20 = 45
        (Fraction(5, 3), 27),   # 25/9 * 27 = 75
        (Fraction(4, 3), 36),   # 16/9 * 36 = 64
        (Fraction(5, 2), 16),   # 25/4 * 16 = 100
        (Fraction(7, 4), 32),   # 49/16 * 32 = 98
    ]
    for offset, (k_rat, area_orig) in enumerate(hom_easy, 271):
        qid = f"OLYM-T2-{offset:03d}"
        ans_f = k_rat * k_rat * area_orig
        assert ans_f.denominator == 1
        ans = int(ans_f)
        k_tex = f"\\frac{{{k_rat.numerator}}}{{{k_rat.denominator}}}"
        q_en = (
            f"A homothety centered at {m('S')} with scale factor {m(f'k = {k_tex}')} maps {m('\\triangle ABC')} "
            f"of area {m(str(area_orig))} to {m('\\triangle A\'B\'C\'')}. Find the area of {m('\\triangle A\'B\'C\'')}."
        )
        q_ar = (
            f"تحاكٍ مركزه {m('S')} ومعامله {m(f'k = {k_tex}')} ينقل المثلث {m('ABC')} الذي مساحته "
            f"{m(str(area_orig))} إلى المثلث {m('A\'B\'C\'')}. أوجد مساحة المثلث {m('A\'B\'C\'')}."
        )
        svg = svg_olym_spiral_homothety(f"{k_rat.numerator}/{k_rat.denominator}", "S=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp19,
            q_en, q_ar, ans,
            [int(k_rat * area_orig) if (k_rat * area_orig).denominator == 1 else ans - 10, ans + 8, ans - 6, area_orig * 2],
            f"Under a homothety of scale factor {m('k')}, areas scale by {m('k^2')}.",
            f"تحت تأثير تحاكٍ معامله {m('k')} تتضاعف المساحات بمعامل {m('k^2')}.",
            "Multiply the original area by the square of the homothety scale factor.",
            [
                f"Every linear dimension of {m('\\triangle ABC')} scales by {m(f'|k| = {k_tex}')}.",
                f"Consequently, the area scales by {m(f'k^2 = \\left({k_tex}\\right)^2 = \\frac{{{k_rat.numerator**2}}}{{{k_rat.denominator**2}}}')}.",
                f"Multiply: {m(f'[A\'B\'C\'] = \\frac{{{k_rat.numerator**2}}}{{{k_rat.denominator**2}}} \\cdot {area_orig} = {ans}')}.",
            ],
            f"Ratio check: {m(f'\\sqrt{{[A\'B\'C\']/[ABC]}} = \\sqrt{{{ans}/{area_orig}}} = {k_tex}')}.",
            "نضرب المساحة الأصلية في مربع معامل التحاكي k^2.",
            [
                f"تتغير الأطوال الخطية بمعامل {m(k_tex)} فتتغير المساحة بمعامل {m(f'k^2 = \\frac{{{k_rat.numerator**2}}}{{{k_rat.denominator**2}}}')}.",
                f"نضرب في المساحة الأصلية: {m(f'[A\'B\'C\'] = \\frac{{{k_rat.numerator**2}}}{{{k_rat.denominator**2}}} \\times {area_orig} = {ans}')}.",
            ],
            f"الجذر التربيعي لنسبة المساحتين يعيد معامل التحاكي {m(k_tex)}.",
            diagram_en=svg,
        ))

    # Medium (276..280): Homothety from apex A inscribing a square in triangle ABC: s = b*h / (b + h)
    hom_med = [
        (12, 6, 4),
        (15, 10, 6),
        (24, 12, 8),
        (30, 15, 10),
        (20, 30, 12),
    ]
    for offset, (base_b, alt_h, s_ans) in enumerate(hom_med, 276):
        qid = f"OLYM-T2-{offset:03d}"
        assert (base_b * alt_h) == s_ans * (base_b + alt_h)
        ans = s_ans
        q_en = (
            f"Acute {m('\\triangle ABC')} has base {m(f'BC = {base_b}')} and altitude {m(f'h = {alt_h}')} from {m('A')} "
            f"to {m('BC')}. A square is inscribed in {m('\\triangle ABC')} with two vertices on {m('BC')} and one "
            f"on each of {m('AB')} and {m('AC')}. Using homothety centered at {m('A')}, find the square's side length."
        )
        q_ar = (
            f"مثلث حاد الزوايا {m('ABC')} طول قاعدته {m(f'BC = {base_b}')} وارتفاعه النازل من {m('A')} "
            f"يساوي {m(f'h = {alt_h}')}. رُسم مربع داخل المثلث يقع رأسان منه على {m('BC')} ورأس على كل من "
            f"{m('AB')} و{m('AC')}. باستخدام التحاكي الذي مركزه {m('A')}، أوجد طول ضلع المربع."
        )
        svg = svg_olym_spiral_homothety("s=?", "A")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp19,
            q_en, q_ar, ans,
            [(base_b + alt_h) // 3 if (base_b + alt_h) // 3 != ans else ans + 3, ans + 2, ans - 2, base_b // 2 if base_b // 2 != ans else ans + 4],
            f"A homothety from {m('A')} relates the top small triangle (height {m('h - s')}, base {m('s')}) to {m('\\triangle ABC')}: {m('\\frac{s}{b} = \\frac{h - s}{h}')}.",
            f"التحاكي من الرأس {m('A')} يربط المثلث العلوي الصغير (ارتفاعه {m('h - s')} وقاعدته {m('s')}) بالمثلث الكلي: {m('\\frac{s}{b} = \\frac{h - s}{h}')}.",
            "Use the homothety ratio s / b = (h - s) / h from apex A, yielding s = b*h / (b + h).",
            [
                f"Let {m('s')} be the side length of the inscribed square. The top sub-triangle above the square is homothetic to {m('\\triangle ABC')} from center {m('A')}.",
                f"Equating base and altitude ratios gives {m(f'\\frac{{s}}{{{base_b}}} = \\frac{{{alt_h} - s}}{{{alt_h}}}')}.",
                f"Solving for {m('s')} yields {m(f's = \\frac{{{base_b} \\cdot {alt_h}}}{{{base_b} + {alt_h}}} = {ans}')}.",
            ],
            f"Check: {m(f's/b = {ans}/{base_b} = {Fraction(ans, base_b)}')} and {m(f'(h - s)/h = {alt_h - ans}/{alt_h} = {Fraction(alt_h - ans, alt_h)}')}.",
            "نستعمل نسبة التحاكي من الرأس A بين المثلث العلوي والمثلث الأصلي فنحصل على s = bh/(b + h).",
            [
                f"ليكن {m('s')} طول ضلع المربع؛ المثلث العلوي فوق المربع يحاكي {m('\\triangle ABC')} من المركز {m('A')}.",
                f"من تساوي نسبة القاعدتين ونسبة الارتفاعين: {m(f'\\frac{{s}}{{{base_b}}} = \\frac{{{alt_h} - s}}{{{alt_h}}}')}.",
                f"بحل المعادلة نجد {m(f's = \\frac{{{base_b} \\times {alt_h}}}{{{base_b} + {alt_h}}} = {ans}')}.",
            ],
            f"التحقق: النسبتان متساويتان وتبلغان {m(f'{Fraction(ans, base_b)}')}.",
            diagram_en=svg,
        ))

    # Hard (281..285): Spiral Similarity switching theorem: S maps AB -> CD => triangle SAC ~ triangle SBD
    spiral_hard = [
        (6, 9, 8, 10, 12),    # SA=6, SB=9, SC=8, AB=10, AC=12 -> CD = AB*(SC/SA) = 10*(8/6)? Let's make SA divide both!
    ]
    spiral_hard = [
        (6, 9, 12, 8, 10),    # SA=6, SB=9, SC=12, AB=8, AC=10 -> CD = 8*(12/6)=16, BD = 10*(9/6)=15 -> CD+BD = 31
        (8, 12, 10, 12, 14),  # SA=8, SB=12, SC=10, AB=12, AC=14 -> CD = 12*(10/8)=15, BD = 14*(12/8)=21 -> CD+BD = 36
        (9, 15, 12, 12, 15),  # SA=9, SB=15, SC=12, AB=12, AC=15 -> CD = 12*(12/9)=16, BD = 15*(15/9)=25 -> CD+BD = 41
        (10, 15, 14, 15, 18), # SA=10, SB=15, SC=14, AB=15, AC=18 -> CD = 15*(14/10)=21, BD = 18*(15/10)=27 -> CD+BD = 48
        (12, 16, 18, 14, 21), # SA=12, SB=16, SC=18, AB=14, AC=21 -> CD = 14*(18/12)=21, BD = 21*(16/12)=28 -> CD+BD = 49
    ]
    for offset, (sa_l, sb_l, sc_l, ab_l, ac_l) in enumerate(spiral_hard, 281):
        qid = f"OLYM-T2-{offset:03d}"
        cd_f = Fraction(ab_l * sc_l, sa_l)
        bd_f = Fraction(ac_l * sb_l, sa_l)
        assert cd_f.denominator == 1 and bd_f.denominator == 1
        cd_i, bd_i = int(cd_f), int(bd_f)
        ans = cd_i + bd_i
        q_en = (
            f"In an Intermediate Olympiad spiral similarity configuration, a spiral similarity centered "
            f"at {m('S')} maps segment {m('AB')} to segment {m('CD')} ({m('A \\mapsto C')}, {m('B \\mapsto D')}). "
            f"Given {m(f'SA = {sa_l}')}, {m(f'SB = {sb_l}')}, {m(f'SC = {sc_l}')}, {m(f'AB = {ab_l}')}, and {m(f'AC = {ac_l}')}, "
            f"compute {m('CD + BD')}."
        )
        q_ar = (
            f"في مسألة تشابه حلزوني للأولمبياد المتوسط، ينقل تشابه حلزوني مركزه {m('S')} القطعة {m('AB')} "
            f"إلى {m('CD')} بحيث ({m('A \\mapsto C')} و{m('B \\mapsto D')}). إذا كان {m(f'SA = {sa_l}')} "
            f"و{m(f'SB = {sb_l}')} و{m(f'SC = {sc_l}')} و{m(f'AB = {ab_l}')} و{m(f'AC = {ac_l}')}، فاحسب {m('CD + BD')}."
        )
        svg = svg_olym_spiral_homothety("CD+BD=?", "S")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp19,
            q_en, q_ar, ans,
            [cd_i + ac_l, bd_i + ab_l, ans + 5, ans - 4],
            f"By the Spiral Similarity Switching Theorem, {m('\\triangle SAB \\sim \\triangle SCD')} implies {m('\\triangle SAC \\sim \\triangle SBD')}.",
            f"بموجب مبرهنة التبديل في التشابه الحلزوني، فإن {m('\\triangle SAB \\sim \\triangle SCD')} يستلزم {m('\\triangle SAC \\sim \\triangle SBD')}.",
            "Use triangle SAB ~ triangle SCD to find CD and the paired similarity triangle SAC ~ triangle SBD to find BD.",
            [
                f"From {m('\\triangle SAB \\sim \\triangle SCD')}, {m(f'CD = AB \\cdot \\frac{{SC}}{{SA}} = {ab_l} \\cdot \\frac{{{sc_l}}}{{{sa_l}}} = {cd_i}')}.",
                f"By the Spiral Similarity Switching Theorem, {m('\\triangle SAC \\sim \\triangle SBD')}, so {m(f'BD = AC \\cdot \\frac{{SB}}{{SA}} = {ac_l} \\cdot \\frac{{{sb_l}}}{{{sa_l}}} = {bd_i}')}.",
                f"Summing the two lengths yields {m(f'CD + BD = {cd_i} + {bd_i} = {ans}')}.",
            ],
            f"Both similarity ratios {m(f'SC/SA = {Fraction(sc_l, sa_l)}')} and {m(f'SB/SA = {Fraction(sb_l, sa_l)}')} are preserved.",
            "نستعمل التشابه المباشر لإيجاد CD والتشابه المرافق بالتبديل لإيجاد BD.",
            [
                f"من التشابه {m('\\triangle SAB \\sim \\triangle SCD')} نجد {m(f'CD = {ab_l} \\cdot \\frac{{{sc_l}}}{{{sa_l}}} = {cd_i}')}.",
                f"وبموجب خاصية التبديل في التشابه الحلزوني {m('\\triangle SAC \\sim \\triangle SBD')}، فيكون {m(f'BD = {ac_l} \\cdot \\frac{{{sb_l}}}{{{sa_l}}} = {bd_i}')}.",
                f"بجمع الطولين نحصل على {m(f'CD + BD = {ans}')}.",
            ],
            f"كلا المثلثين يحافظ على زاوية الدوران ونسبة التمدد حول المركز {m('S')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 20: olym_t2_geo_solid_spheres_cones (OLYM-T2-286..300)
    # ------------------------------------------------------------------
    bp20 = "olym_t2_geo_solid_spheres_cones"

    # Easy (286..290): Archimedes sphere inscribed in a right cylinder (radius R, height 2R): empty volume (V_cyl - V_sph)/pi = 2/3 R^3
    arch_easy = [3, 6, 9, 12, 15]
    for offset, R_val in enumerate(arch_easy, 286):
        qid = f"OLYM-T2-{offset:03d}"
        ans = (2 * (R_val**3)) // 3
        v_cyl = 2 * (R_val**3)
        v_sph = (4 * (R_val**3)) // 3
        assert v_cyl - v_sph == ans
        q_en = (
            f"A sphere of radius {m(f'R = {R_val}')} is tightly inscribed in a right circular cylinder "
            f"of radius {m(str(R_val))} and height {m(str(2 * R_val))}. If the volume of the region inside "
            f"the cylinder but outside the sphere is {m('K\\pi')}, find {m('K')}."
        )
        q_ar = (
            f"كرة نصف قطرها {m(f'R = {R_val}')} محاطة بإحكام داخل أسطوانة دائرية قائمة نصف قطرها {m(str(R_val))} "
            f"وارتفاعها {m(str(2 * R_val))}. إذا كان حجم الفراغ داخل الأسطوانة وخارج الكرة يساوي {m('K\\pi')}، فأوجد قيمة {m('K')}."
        )
        svg = svg_stu_sphere_in_cylinder(f"R={R_val}", "K = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Easy", bp20,
            q_en, q_ar, ans,
            [v_sph, v_cyl, R_val**3, ans + 18],
            f"By Archimedes' theorem, {m('V_{\\text{cyl}} = 2\\pi R^3')} and {m('V_{\\text{sph}} = \\frac{4}{3}\\pi R^3')}, so the difference is {m('\\frac{2}{3}\\pi R^3')}.",
            f"بموجب مبرهنة أرخميدس: {m('V_{\\text{cyl}} = 2\\pi R^3')} و{m('V_{\\text{sph}} = \\frac{4}{3}\\pi R^3')}، فيكون الفرق {m('\\frac{2}{3}\\pi R^3')}.",
            "Subtract the sphere volume (4/3)pi R^3 from the cylinder volume 2 pi R^3 to get (2/3)pi R^3.",
            [
                f"Compute the cylinder volume: {m(f'V_{{\\text{{cyl}}}} = \\pi R^2(2R) = 2\\pi({R_val}^3) = {v_cyl}\\pi')}.",
                f"Compute the sphere volume: {m(f'V_{{\\text{{sph}}}} = \\frac{{4}}{{3}}\\pi R^3 = {v_sph}\\pi')}.",
                f"Subtracting gives {m(f'K = {v_cyl} - {v_sph} = {ans}')}.",
            ],
            f"Archimedes' ratio {m('V_{\\text{sph}} : V_{\\text{cyl}} = 2 : 3')} confirms the remaining volume is {m('1/3')} of {m(f'{v_cyl}\\pi')}.",
            "نطرح حجم الكرة من حجم الأسطوانة المحيطة بها وفق علاقة أرخميدس.",
            [
                f"حجم الأسطوانة هو {m(f'V_{{\\text{{cyl}}}} = 2\\pi R^3 = {v_cyl}\\pi')}.",
                f"وحجم الكرة هو {m(f'V_{{\\text{{sph}}}} = \\frac{{4}}{{3}}\\pi R^3 = {v_sph}\\pi')}.",
                f"بطرح الحجمين نجد {m(f'K = {v_cyl} - {v_sph} = {ans}')}.",
            ],
            f"يمثل الفراغ ثلث حجم الأسطوانة أي {m(f'{v_cyl}/3 = {ans}')}.",
            diagram_en=svg,
        ))

    # Medium (291..295): Right circular cone frustum volume V / pi = (h/3)*(R^2 + R*r + r^2)
    frust_med = [
        (6, 5, 2),    # 2 * (25 + 10 + 4) = 78
        (9, 6, 3),    # 3 * (36 + 18 + 9) = 189
        (6, 7, 3),    # 2 * (49 + 21 + 9) = 158
        (12, 5, 3),   # 4 * (25 + 15 + 9) = 196
        (9, 8, 4),    # 3 * (64 + 32 + 16) = 336
    ]
    for offset, (h_fr, R_bot, r_top) in enumerate(frust_med, 291):
        qid = f"OLYM-T2-{offset:03d}"
        ans = (h_fr * (R_bot**2 + R_bot * r_top + r_top**2)) // 3
        q_en = (
            f"A frustum of a right circular cone has height {m(f'h = {h_fr}')}, bottom base radius "
            f"{m(f'R = {R_bot}')}, and top base radius {m(f'r = {r_top}')}. If its volume is {m('V = K\\pi')}, find {m('K')}."
        )
        q_ar = (
            f"جذع مخروط دائري قائم ارتفاعه {m(f'h = {h_fr}')} ونصف قطر قاعدته الكبرى {m(f'R = {R_bot}')} "
            f"ونصف قطر قاعدته الصغرى {m(f'r = {r_top}')}. إذا كان حجمه {m('V = K\\pi')}، فأوجد قيمة {m('K')}."
        )
        svg = svg_stu_cone_frustum(f"h={h_fr}", f"r={r_top}", "K = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Medium", bp20,
            q_en, q_ar, ans,
            [(h_fr * (R_bot**2 + r_top**2)) // 3, ans - (h_fr * R_bot * r_top) // 3, ans + 12, h_fr * ((R_bot + r_top) // 2) ** 2],
            f"Apply the frustum volume formula {m('V = \\frac{\\pi h}{3}(R^2 + Rr + r^2)')}.",
            f"طبّق صيغة حجم جذع المخروط {m('V = \\frac{\\pi h}{3}(R^2 + Rr + r^2)')}.",
            "Evaluate (h/3)*(R^2 + Rr + r^2) by subtracting the removed apex cone from the full similar cone.",
            [
                f"The volume of a conical frustum is {m('V = \\frac{\\pi h}{3}(R^2 + Rr + r^2)')}.",
                f"Compute the bracket: {m(f'{R_bot}^2 + {R_bot} \\cdot {r_top} + {r_top}^2 = {R_bot**2 + R_bot * r_top + r_top**2}')}.",
                f"Multiply by {m(f'h/3 = {h_fr // 3}')}: {m(f'K = {h_fr // 3} \\cdot {R_bot**2 + R_bot * r_top + r_top**2} = {ans}')}.",
            ],
            f"Completing the cone to height {m(f'H = \\frac{{{R_bot}}}{{{R_bot - r_top}}} \\cdot {h_fr}')} and subtracting volumes yields the exact same result {m(str(ans))}.",
            "نطبق قانون حجم جذع المخروط الدائري القائم مباشرة.",
            [
                f"حجم جذع المخروط يُعطى بالعلاقة {m('V = \\frac{\\pi h}{3}(R^2 + Rr + r^2)')}.",
                f"نحسب القوس: {m(f'{R_bot}^2 + {R_bot}\\cdot{r_top} + {r_top}^2 = {R_bot**2 + R_bot * r_top + r_top**2}')}.",
                f"بالضرب في {m(f'{h_fr}/3 = {h_fr // 3}')} نجد {m(f'K = {ans}')}.",
            ],
            f"إكمال المخروط الكلي وطرح المخروط العلوي يعطي الناتج {m(str(ans))} نفسه.",
            diagram_en=svg,
        ))

    # Hard (296..300): Sphere inscribed in a cone (296..298) & 3D Tetrahedron bimedian (299..300)
    cone_sph_cases = [
        (6, 8, 10, 3),
        (12, 16, 20, 6),
        (15, 36, 39, 10),
    ]
    for idx_sub, (R_c, H_c, L_c, r_ans) in enumerate(cone_sph_cases):
        offset = 296 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        assert R_c * R_c + H_c * H_c == L_c * L_c
        assert (R_c * H_c) == r_ans * (R_c + L_c)
        ans = r_ans
        q_en = (
            f"In an Intermediate Olympiad solid geometry problem, a right circular cone has base radius "
            f"{m(f'R = {R_c}')} and altitude {m(f'H = {H_c}')}. Find the radius {m('r')} of the sphere inscribed "
            f"tangent to the base and the lateral surface of the cone."
        )
        q_ar = (
            f"في مسألة هندسة فراغية للأولمبياد المتوسط، مخروط دائري قائم نصف قطر قاعدته {m(f'R = {R_c}')} "
            f"وارتفاعه {m(f'H = {H_c}')}. أوجد نصف قطر الكرة {m('r')} المرسومة داخله والماسة للقاعدة والسطح الجانبي."
        )
        svg = svg_stu_cone_frustum(f"H={H_c}", f"R={R_c}", "r = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp20,
            q_en, q_ar, ans,
            [R_c // 2 if R_c // 2 != ans else ans + 2, ans + 1, max(1, ans - 1), H_c // 3 if H_c // 3 != ans else ans + 3],
            f"Take the axial cross-section: it is an isosceles triangle of base {m(f'2R = {2 * R_c}')}, height {m(str(H_c))}, and legs {m(f'L = {L_c}')}.",
            f"خذ المقطع المحوري للمخروط؛ فهو مثلث متساوي الساقين قاعدته {m(f'2R = {2 * R_c}')} وارتفاعه {m(str(H_c))} وطول ساقه {m(f'L = {L_c}')}.",
            "Reduce the 3D inscribed sphere to the incircle of the axial cross-section triangle: r = R*H / (R + L).",
            [
                f"Find the slant height of the cone: {m(f'L = \\sqrt{{R^2 + H^2}} = \\sqrt{{{R_c}^2 + {H_c}^2}} = {L_c}')}.",
                f"The axial cross-section is an isosceles triangle of area {m(f'\\Delta = R \\cdot H = {R_c * H_c}')} and semiperimeter {m(f's = R + L = {R_c + L_c}')}.",
                f"The inscribed sphere radius equals the cross-section inradius: {m(f'r = \\frac{{\\Delta}}{{s}} = \\frac{{{R_c * H_c}}}{{{R_c + L_c}}} = {ans}')}.",
            ],
            f"Right-triangle similarity at thecone apex confirms {m(f'\\frac{{r}}{{H - r}} = \\frac{{R}}{{L}} = \\frac{{{R_c}}}{{{L_c}}}')}.",
            "نختزل المسألة الفراغية إلى حساب نصف قطر الدائرة الداخلية للمثلث المتساوي الساقين في المقطع المحوري.",
            [
                f"نحسب طول الراسم: {m(f'L = \\sqrt{{{R_c}^2 + {H_c}^2}} = {L_c}')}.",
                f"المقطع المحوري مثلث متساوي الساقين مساحته {m(f'R \\cdot H = {R_c * H_c}')} ونصف محيطه {m(f'R + L = {R_c + L_c}')}.",
                f"إذن نصف قطر الكرة الداخلية هو {m(f'r = \\frac{{{R_c * H_c}}}{{{R_c + L_c}}} = {ans}')}.",
            ],
            f"تشابه المثلثين القائمين عند رأس المخروط يؤكد أن {m(f'r/(H - r) = {R_c}/{L_c}')}.",
            diagram_en=svg,
        ))

    tetra_cases = [
        (8, 6, 2),    # AB=CD=8, other 4 edges = 6 -> CM^2 = 36 - 16 = 20 -> MN = sqrt(20 - 16) = 2
        (12, 9, 3),   # AB=CD=12, other 4 edges = 9 -> CM^2 = 81 - 36 = 45 -> MN = sqrt(45 - 36) = 3
    ]
    for idx_sub, (a_opp, b_leg, mn_ans) in enumerate(tetra_cases):
        offset = 299 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        cm_sq = b_leg * b_leg - (a_opp // 2) ** 2
        assert cm_sq - (a_opp // 2) ** 2 == mn_ans * mn_ans
        ans = mn_ans
        q_en = (
            f"In tetrahedron {m('ABCD')}, opposite edges {m('AB')} and {m('CD')} both have length {m(str(a_opp))}, "
            f"while the remaining four edges {m('AC, AD, BC, BD')} all have length {m(str(b_leg))}. "
            f"Find the distance {m('MN')} between the midpoints {m('M')} of {m('AB')} and {m('N')} of {m('CD')}."
        )
        q_ar = (
            f"في رباعي الأوجه {m('ABCD')}، طول كل من الحرفين المتقابلين {m('AB')} و{m('CD')} يساوي {m(str(a_opp))}، "
            f"بينما أطوال الأحرف الأربعة الباقية {m('AC, AD, BC, BD')} تساوي {m(str(b_leg))}. "
            f"أوجد المسافة {m('MN')} بين منتصف {m('M')} للحرف {m('AB')} ومنتصف {m('N')} للحرف {m('CD')}."
        )
        svg = svg_olym_tetrahedron_3d(str(a_opp), str(b_leg), "MN=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Geometry", "Hard", bp20,
            q_en, q_ar, ans,
            [b_leg, a_opp // 2, ans + 2, max(1, ans - 2)],
            f"In isosceles {m('\\triangle ABC')} and {m('\\triangle ABD')}, medians {m('CM')} and {m('DM')} are altitudes to {m('AB')}, making {m('\\triangle CMD')} isosceles.",
            f"في المثلثين المتساويي الساقين {m('ABC')} و{m('ABD')} يكون كل من {m('CM')} و{m('DM')} ارتفاعاً على {m('AB')}، فيصبح المثلث {m('CMD')} متساوي الساقين.",
            "Apply the Pythagorean theorem twice: first in triangle ACM to find CM^2, then in triangle CMN to find MN.",
            [
                f"In isosceles {m('\\triangle CAB')} ({m(f'CA = CB = {b_leg}')}), median {m('CM \\perp AB')}, so {m(f'CM^2 = {b_leg}^2 - ({a_opp // 2})^2 = {cm_sq}')}.",
                f"By symmetry {m(f'DM^2 = {cm_sq}')}, so {m('\\triangle CMD')} is isosceles with base {m(f'CD = {a_opp}')} and midpoint {m('N')}.",
                f"Thus {m('MN \\perp CD')} and {m(f'MN = \\sqrt{{CM^2 - CN^2}} = \\sqrt{{{cm_sq} - ({a_opp // 2})^2}} = {ans}')}.",
            ],
            f"Notice {m('MN')} is perpendicular to both skew edges {m('AB')} and {m('CD')}, giving their exact shortest distance {m(str(ans))}.",
            "نطبق مبرهنة فيثاغورس مرتين: الأولى لإيجاد مربع المتوسط CM والثانية في المثلث المتساوي الساقين CMD.",
            [
                f"في المثلث المتساوي الساقين {m('CAB')} يكون {m('CM \\perp AB')} ومنه {m(f'CM^2 = {b_leg}^2 - {a_opp // 2}^2 = {cm_sq}')}.",
                f"وبالتماثل {m(f'DM^2 = {cm_sq}')}، فيكون المثلث {m('CMD')} متساوي الساقين وقاعدته {m(f'CD = {a_opp}')}.",
                f"إذن {m('MN \\perp CD')} وطوله {m(f'MN = \\sqrt{{{cm_sq} - {a_opp // 2}^2}} = {ans}')}.",
            ],
            f"القطعة {m('MN')} عمودية على الحرفين المتخالفين معاً وتمثل أقصر مسافة بينهما.",
            diagram_en=svg,
        ))

    return qs



# ==============================================================================
# UNIT 2.6 — Combinatorics (OLYM-T2-301 .. OLYM-T2-360)
# ==============================================================================

def _catalan(n: int) -> int:
    return math.comb(2 * n, n) // (n + 1)


def _gen_u26_combinatorics() -> list[dict]:
    qs: list[dict] = []

    # ------------------------------------------------------------------
    # Blueprint 21: olym_t2_comb_catalan_dyck_biject (OLYM-T2-301..315)
    # ------------------------------------------------------------------
    bp21 = "olym_t2_comb_catalan_dyck_biject"

    # Easy (301..305): Direct Catalan numbers C_n via Dyck paths & polygon triangulations
    cat_easy = [
        (3, "monotonic lattice paths from (0, 0) to (3, 3) never rising above y = x"),
        (4, "monotonic lattice paths from (0, 0) to (4, 4) staying on or below the main diagonal y = x"),
        (5, "valid sequences of 5 pairs of matched parentheses"),
        (6, "triangulations of a convex octagon (8-gon) into 6 triangles by non-intersecting diagonals"),
        (7, "monotonic Dyck paths from (0, 0) to (7, 7) never crossing above y = x"),
    ]
    for offset, (n_cat, desc_en) in enumerate(cat_easy, 301):
        qid = f"OLYM-T2-{offset:03d}"
        ans = _catalan(n_cat)
        assert ans == math.comb(2 * n_cat, n_cat) - math.comb(2 * n_cat, n_cat - 1)
        q_en = (
            f"In an Intermediate Olympiad combinatorics problem, find the total number of {desc_en}, "
            f"given by the Catalan number {m(f'C_{{{n_cat}}}')}."
        )
        q_ar = (
            f"في مسألة توافقيات للأولمبياد المتوسط، أوجد العدد الكلي للتشكيلات الموصوفة والمكافئة "
            f"لعدد كاتالان {m(f'C_{{{n_cat}}} = \\frac{{1}}{{{n_cat + 1}}}\\binom{{{2 * n_cat}}}{{{n_cat}}}')}."
        )
        svg = svg_stu_dyck_grid(min(6, max(2, n_cat)), "RRUURURU")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Easy", bp21,
            q_en, q_ar, ans,
            [math.comb(2 * n_cat, n_cat) // n_cat, _catalan(n_cat - 1), ans + n_cat, ans * 2],
            f"Evaluate the Catalan formula {m(f'C_{{{n_cat}}} = \\frac{{1}}{{{n_cat + 1}}}\\binom{{{2 * n_cat}}}{{{n_cat}}}')}.",
            f"احسب صيغة عدد كاتالان {m(f'C_{{{n_cat}}} = \\frac{{1}}{{{n_cat + 1}}}\\binom{{{2 * n_cat}}}{{{n_cat}}}')}.",
            "Apply the closed-form Catalan formula C_n = C(2n, n) / (n + 1).",
            [
                f"The configuration is counted by the {m(f'{n_cat}')}-th Catalan number {m(f'C_{{{n_cat}}}')}.",
                f"Compute the central binomial coefficient: {m(f'\\binom{{{2 * n_cat}}}{{{n_cat}}} = {math.comb(2 * n_cat, n_cat)}')}.",
                f"Divide by {m(str(n_cat + 1))}: {m(f'C_{{{n_cat}}} = \\frac{{{math.comb(2 * n_cat, n_cat)}}}{{{n_cat + 1}}} = {ans}')}.",
            ],
            f"By André's reflection principle, {m(f'\\binom{{{2 * n_cat}}}{{{n_cat}}} - \\binom{{{2 * n_cat}}}{{{n_cat - 1}}} = {ans}')}.",
            "نطبق الصيغة المغلقة لأعداد كاتالان C_n = C(2n, n)/(n + 1).",
            [
                f"عدد التشكيلات المطلوبة يساوي عدد كاتالان {m(f'C_{{{n_cat}}}')}.",
                f"نحسب المعامل الثنائي المركزي: {m(f'\\binom{{{2 * n_cat}}}{{{n_cat}}} = {math.comb(2 * n_cat, n_cat)}')}.",
                f"بالقسمة على {m(str(n_cat + 1))} نحصل على {m(f'C_{{{n_cat}}} = {ans}')}.",
            ],
            f"باستعمال مبدأ الانعكاس لأندريه: {m(f'\\binom{{{2 * n_cat}}}{{{n_cat}}} - \\binom{{{2 * n_cat}}}{{{n_cat - 1}}} = {ans}')}.",
            diagram_en=svg,
        ))

    # Medium (306..310): André's reflection principle on rectangular ballot grids (a, b) with a > b staying on/below y = x
    ballot_med = [
        (5, 3),   # C(8,3) - C(8,2) = 56 - 28 = 28
        (6, 3),   # C(9,3) - C(9,2) = 84 - 36 = 48
        (6, 4),   # C(10,4) - C(10,3) = 210 - 120 = 90
        (7, 3),   # C(10,3) - C(10,2) = 120 - 45 = 75
        (7, 4),   # C(11,4) - C(11,3) = 330 - 165 = 165
    ]
    for offset, (a_r, b_u) in enumerate(ballot_med, 306):
        qid = f"OLYM-T2-{offset:03d}"
        tot_p = math.comb(a_r + b_u, b_u)
        bad_p = math.comb(a_r + b_u, b_u - 1)
        ans = tot_p - bad_p
        assert ans == (a_r - b_u + 1) * math.comb(a_r + b_u, b_u) // (a_r + 1)
        q_en = (
            f"How many monotonic lattice paths from {m('(0, 0)')} to {m(f'({a_r}, {b_u})')} using unit steps "
            f"right {m('(1, 0)')} and up {m('(0, 1)')} never rise above the line {m('y = x')}?"
        )
        q_ar = (
            f"كم مساراً شبكياً رتيباً من {m('(0, 0)')} إلى {m(f'({a_r}, {b_u})')} بخطوات وحدة يميناً {m('(1, 0)')} "
            f"وأعلى {m('(0, 1)')} لا يرتفع أبداً فوق المستقيم {m('y = x')}؟"
        )
        svg = svg_stu_dyck_grid(min(6, a_r), "RRURRUUU")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Medium", bp21,
            q_en, q_ar, ans,
            [tot_p, bad_p, ans + 10, (a_r - b_u) * tot_p // (a_r + b_u)],
            f"By André's reflection principle across {m('y = x + 1')}, the number of valid paths is {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} - \\binom{{{a_r + b_u}}}{{{b_u - 1}}}')}.",
            f"بموجب مبدأ الانعكاس لأندريه حول المستقيم {m('y = x + 1')}، يساوي عدد المسارات الصالحة {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} - \\binom{{{a_r + b_u}}}{{{b_u - 1}}}')}.",
            "Subtract the reflected invalid paths C(a + b, b - 1) from total lattice paths C(a + b, b).",
            [
                f"Without restriction, there are {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} = {tot_p}')} lattice paths from {m('(0, 0)')} to {m(f'({a_r}, {b_u})')}.",
                f"Any path rising above {m('y = x')} hits {m('y = x + 1')}; reflecting its prefix across {m('y = x + 1')} gives a bijection with paths from {m('(-1, 1)')} to {m(f'({a_r}, {b_u})')}, of which there are {m(f'\\binom{{{a_r + b_u}}}{{{b_u - 1}}} = {bad_p}')}.",
                f"Subtracting gives {m(f'{tot_p} - {bad_p} = {ans}')} valid paths.",
            ],
            f"Closed-form ballot formula check: {m(f'\\frac{{{a_r - b_u + 1}}}{{{a_r + 1}}}\\binom{{{a_r + b_u}}}{{{b_u}}} = {ans}')}.",
            "نطرح عدد المسارات الخاطئة المنعكسة حول المستقيم y = x + 1 من إجمالي المسارات الشبكية.",
            [
                f"إجمالي المسارات الشبكية دون قيد هو {m(f'\\binom{{{a_r + b_u}}}{{{b_u}}} = {tot_p}')}.",
                f"بمبدأ الانعكاس حول {m('y = x + 1')} يتقابل كل مسار يتجاوز القطر مع مسار من {m('(-1, 1)')} إلى {m(f'({a_r}, {b_u})')} وعددها {m(f'\\binom{{{a_r + b_u}}}{{{b_u - 1}}} = {bad_p}')}.",
                f"بطرح المسارات المرفوضة نجد {m(f'{tot_p} - {bad_p} = {ans}')}.",
            ],
            f"تؤكد صيغة الاقتراع المغلقة أن الناتج يساوي {m(str(ans))}.",
            diagram_en=svg,
        ))

    # Hard (311..315): First-return Catalan convolution C_{k-1} * C_{n-k}
    cat_hard = [
        (5, 2),   # n=5, first return at (2, 2): C_1 * C_3 = 1 * 5 = 5 -> pick (6, 3): C_2 * C_3 = 2 * 5 = 10
        (6, 2),   # C_1 * C_4 = 1 * 14 = 14
        (6, 4),   # C_3 * C_2 = 5 * 2 = 10 -> pick (7, 3): C_2 * C_4 = 2 * 14 = 28
        (7, 4),   # C_3 * C_3 = 5 * 5 = 25
        (7, 2),   # C_1 * C_5 = 1 * 42 = 42
    ]
    cat_hard[0] = (6, 3)
    cat_hard[2] = (7, 3)
    for offset, (n_tot, k_ret) in enumerate(cat_hard, 311):
        qid = f"OLYM-T2-{offset:03d}"
        c_left = _catalan(k_ret - 1)
        c_right = _catalan(n_tot - k_ret)
        ans = c_left * c_right
        q_en = (
            f"A Dyck path from {m('(0, 0)')} to {m(f'({n_tot}, {n_tot})')} stays on or below the diagonal "
            f"{m('y = x')}. How many such paths touch the diagonal {m('y = x')} for the first time after "
            f"{m('(0, 0)')} at the point {m(f'({k_ret}, {k_ret})')}?"
        )
        q_ar = (
            f"مسار دايك من {m('(0, 0)')} إلى {m(f'({n_tot}, {n_tot})')} يبقى على القطر {m('y = x')} أو تحته. "
            f"كم مساراً من هذا النوع يلمس القطر {m('y = x')} لأول مرة بعد نقطة الأصل عند النقطة {m(f'({k_ret}, {k_ret})')}؟"
        )
        svg = svg_stu_dyck_grid(min(6, n_tot), "RRURUURU")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp21,
            q_en, q_ar, ans,
            [_catalan(k_ret) * c_right, ans + c_right, _catalan(n_tot), max(1, ans - c_left)],
            f"The portion from {m('(0, 0)')} to {m(f'({k_ret}, {k_ret})')} starts with {m('R')}, ends with {m('U')}, and stays strictly below {m('y = x')} in between ({m(f'C_{{{k_ret - 1}}}')} ways).",
            f"الجزء الأول من {m('(0, 0)')} إلى {m(f'({k_ret}, {k_ret})')} يبدأ بخطوة يمين وينتهي بخطوة أعلى ويبقى تحت القطر تماماً بينهما وعدد طرقه {m(f'C_{{{k_ret - 1}}}')}.",
            "Decompose the Dyck path at its first diagonal return (k, k) into an elevated C_{k-1} block and a trailing C_{n-k} Dyck path.",
            [
                f"To touch {m('y = x')} first at {m(f'({k_ret}, {k_ret})')}, the path must start with {m('(0,0) \\to (1,0)')}, end that segment with {m(f'({k_ret}, {k_ret - 1}) \\to ({k_ret}, {k_ret})')}, and stay on or below {m('y = x - 1')} in between.",
                f"Thus there are {m(f'C_{{{k_ret - 1}}} = {c_left}')} choices for the first {m(f'2\\cdot {k_ret}')} steps and {m(f'C_{{{n_tot - k_ret}}} = {c_right}')} choices for the remaining Dyck path from {m(f'({k_ret}, {k_ret})')} to {m(f'({n_tot}, {n_tot})')}.",
                f"Multiplying gives {m(f'C_{{{k_ret - 1}}} C_{{{n_tot - k_ret}}} = {c_left} \\cdot {c_right} = {ans}')}.",
            ],
            f"Summing {m('C_{k-1} C_{n-k}')} over {m(f'1 \\le k \\le {n_tot}')} recovers the full Catalan convolution {m(f'C_{{{n_tot}}} = {_catalan(n_tot)}')}.",
            "نفكك المسار عند أول عودة للقطر إلى مسار محصور أولي وعدد طرقه C_{k-1} ومسار دايك لاحق وعدد طرقه C_{n-k}.",
            [
                f"لكي تكون أول عودة للقطر عند {m(f'({k_ret}, {k_ret})')} يجب أن يبدأ المسار بخطوة يمين وينتهي بخطوة أعلى مع البقاء تحت القطر، وعدد طرقه {m(f'C_{{{k_ret - 1}}} = {c_left}')}.",
                f"أما الجزء المتبقي من {m(f'({k_ret}, {k_ret})')} إلى {m(f'({n_tot}, {n_tot})')} فهو مسار دايك مستقل عدد طرقه {m(f'C_{{{n_tot - k_ret}}} = {c_right}')}.",
                f"بحساب الجداء نحصل على {m(f'{c_left} \\times {c_right} = {ans}')}.",
            ],
            f"مجموع هذه الجداءات على جميع قيم {m('k')} يحقق علاقة الالتفاف الكاتالانية الشهيرة.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 22: olym_t2_comb_recurrences_tilings (OLYM-T2-316..330)
    # ------------------------------------------------------------------
    bp22 = "olym_t2_comb_recurrences_tilings"

    # Easy (316..320): 2 x n domino tilings T_n = F_{n+1}
    til_easy = [6, 7, 8, 9, 10]
    for offset, n_col in enumerate(til_easy, 316):
        qid = f"OLYM-T2-{offset:03d}"
        dp = [1, 1]
        for _ in range(2, n_col + 1):
            dp.append(dp[-1] + dp[-2])
        ans = dp[n_col]
        q_en = (
            f"In how many ways can a {m(f'2 \\times {n_col}')} rectangular board be completely tiled "
            f"using indistinguishable {m('1 \\times 2')} dominoes?"
        )
        q_ar = (
            f"بكم طريقة يمكن تبليط لوحة مستطيلة أبعادها {m(f'2 \\times {n_col}')} بالكامل "
            f"باستخدام قطع دومينو متطابقة أبعادها {m('1 \\times 2')}؟"
        )
        svg = svg_olym_board_coloring(2, min(6, n_col), 2, f"2×{n_col}: ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Easy", bp22,
            q_en, q_ar, ans,
            [dp[n_col - 1], dp[n_col - 1] + dp[n_col], ans - 3, 2**n_col],
            f"Condition on the rightmost column: either one vertical domino ({m('T_{n-1}')}) or two horizontal dominoes ({m('T_{n-2}')}).",
            f"صنّف حسب العمود الأيمن: إما قطعة دومينو رأسية واحدة ({m('T_{n-1}')}) أو قطعتان أفقيتان ({m('T_{n-2}')}).",
            "Use the Fibonacci recurrence T_n = T_{n-1} + T_{n-2} with T_1 = 1 and T_2 = 2.",
            [
                f"Let {m('T_k')} be the number of tilings of a {m('2 \\times k')} board. Then {m('T_1 = 1')} and {m('T_2 = 2')}.",
                f"Every tiling of {m('2 \\times k')} ends with either {m('1')} vertical domino or {m('2')} stacked horizontal dominoes, so {m('T_k = T_{k-1} + T_{k-2}')}.",
                f"Iterating up to {m(f'k = {n_col}')} gives the sequence {m(', '.join(str(x) for x in dp[1:]))}, so {m(f'T_{{{n_col}}} = {ans}')}.",
            ],
            f"Check: {m(f'T_{{{n_col - 1}}} + T_{{{n_col - 2}}} = {dp[n_col - 1]} + {dp[n_col - 2]} = {ans}')}.",
            "نستخدم العلاقة التراجعية لفيبوناتشي T_n = T_{n-1} + T_{n-2} مع القيمتين الابتدائيتين T_1 = 1 وT_2 = 2.",
            [
                f"ليكن {m('T_k')} عدد طرق تبليط لوحة {m('2 \\times k')}؛ لدينا {m('T_1 = 1')} و{m('T_2 = 2')}.",
                f"ينتهي التبليط إما بقطعة رأسية أو بقطعتين أفقيتين، فتكون {m('T_k = T_{k-1} + T_{k-2}')}.",
                f"بحساب الحدود متتالية نجد {m(f'T_{{{n_col}}} = {ans}')}.",
            ],
            f"التحقق: {m(f'{dp[n_col - 1]} + {dp[n_col - 2]} = {ans}')}.",
            diagram_en=svg,
        ))

    # Medium (321..325): Colored 1 x n strip tilings a_n = p * a_{n-1} + q * a_{n-2}
    til_med = [
        (5, 1, 2),   # Jacobsthal: a_n = a_{n-1} + 2 a_{n-2}: a_0=1, a_1=1, a_2=3, a_3=5, a_4=11, a_5=21
        (6, 1, 2),   # a_6 = 43
        (4, 2, 1),   # Pell: a_n = 2 a_{n-1} + a_{n-2}: a_0=1, a_1=2, a_2=5, a_3=12, a_4=29
        (5, 2, 1),   # a_5 = 70
        (4, 2, 3),   # a_n = 2 a_{n-1} + 3 a_{n-2}: a_0=1, a_1=2, a_2=7, a_3=20, a_4=61
    ]
    for offset, (n_len, p_col, q_col) in enumerate(til_med, 321):
        qid = f"OLYM-T2-{offset:03d}"
        a_seq = [1, p_col]
        for _ in range(2, n_len + 1):
            a_seq.append(p_col * a_seq[-1] + q_col * a_seq[-2])
        ans = a_seq[n_len]
        q_en = (
            f"A {m(f'1 \\times {n_len}')} strip is tiled using {m('1 \\times 1')} squares available in "
            f"{m(str(p_col))} color(s) and {m('1 \\times 2')} dominoes available in {m(str(q_col))} color(s). "
            f"How many distinct colored tilings are possible?"
        )
        q_ar = (
            f"يُبلَّط شريط أبعاده {m(f'1 \\times {n_len}')} باستخدام مربعات {m('1 \\times 1')} متوفرة في "
            f"{m(str(p_col))} ألوان وقطع دومينو {m('1 \\times 2')} متوفرة في {m(str(q_col))} ألوان. "
            f"كم تبليطاً ملوناً مختلفاً يمكن تكوينه؟"
        )
        svg = svg_number_strip([f"1×{n_len}", f"p={p_col},q={q_col}", "aₙ=?"])
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Medium", bp22,
            q_en, q_ar, ans,
            [a_seq[n_len - 1], ans + p_col * a_seq[n_len - 2], ans - q_col, (p_col + q_col) ** (n_len - 1)],
            f"Set up the linear recurrence {m(f'a_k = {p_col}a_{{k-1}} + {q_col}a_{{k-2}}')} with {m('a_0 = 1')} and {m(f'a_1 = {p_col}')}.",
            f"كوّن العلاقة التراجعية الخطية {m(f'a_k = {p_col}a_{{k-1}} + {q_col}a_{{k-2}}')} مع {m('a_0 = 1')} و{m(f'a_1 = {p_col}')}.",
            "Condition on the last tile placed to build the weighted second-order recurrence a_k = p*a_{k-1} + q*a_{k-2}.",
            [
                f"If the last tile is a {m('1 \\times 1')} square ({m(str(p_col))} choices), there are {m(f'{p_col}a_{{k-1}}')} completions; if it is a {m('1 \\times 2')} domino ({m(str(q_col))} choices), there are {m(f'{q_col}a_{{k-2}}')} completions.",
                f"Starting from {m('a_0 = 1')} and {m(f'a_1 = {p_col}')}, apply {m(f'a_k = {p_col}a_{{k-1}} + {q_col}a_{{k-2}}')}.",
                f"The terms for {m(f'k = 1, \\dots, {n_len}')} are {m(', '.join(str(x) for x in a_seq[1:]))}, giving {m(f'a_{{{n_len}}} = {ans}')}.",
            ],
            f"Final step check: {m(f'{p_col} \\cdot {a_seq[n_len - 1]} + {q_col} \\cdot {a_seq[n_len - 2]} = {ans}')}.",
            "نصنّف حسب القطعة الأخيرة لبناء العلاقة التراجعية الموزونة من الرتبة الثانية.",
            [
                f"إذا انتهى الشريط بمربع {m('1 \\times 1')} فلدينا {m(f'{p_col}a_{{k-1}}')} طريقة، وإذا انتهى بقطعة دومينو فلدينا {m(f'{q_col}a_{{k-2}}')} طريقة.",
                f"نبدأ من {m('a_0 = 1')} و{m(f'a_1 = {p_col}')} ونطبق العلاقة التراجعية.",
                f"نجد الحدود المتتالية: {m(', '.join(str(x) for x in a_seq[1:]))}، ومنه {m(f'a_{{{n_len}}} = {ans}')}.",
            ],
            f"التحقق من الخطوة الأخيرة: {m(f'{p_col} \\times {a_seq[n_len - 1]} + {q_col} \\times {a_seq[n_len - 2]} = {ans}')}.",
            diagram_en=svg,
        ))

    # Hard (326..330): Coupled recurrences (3 x 2k domino tilings & pattern-avoiding binary strings)
    # 326..327: 3 x 2k domino tilings: A_0 = 1, A_2 = 3, A_4 = 11, A_6 = 41, A_8 = 153 (A_{2k} = 4 A_{2k-2} - A_{2k-4})
    for idx_sub, k_half in enumerate([3, 4]):  # 3x6 -> 41, 3x8 -> 153
        offset = 326 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        A = [1, 3]
        while len(A) <= k_half:
            A.append(4 * A[-1] - A[-2])
        ans = A[k_half]
        cols_n = 2 * k_half
        q_en = (
            f"In an Intermediate Olympiad tiling recurrence problem, how many ways can a {m(f'3 \\times {cols_n}')} "
            f"grid be completely tiled with {m('1 \\times 2')} dominoes?"
        )
        q_ar = (
            f"في مسألة علاقات تراجعية للأولمبياد المتوسط، بكم طريقة يمكن تبليط شبكة أبعادها {m(f'3 \\times {cols_n}')} "
            f"بالكامل باستخدام قطع دومينو {m('1 \\times 2')}؟"
        )
        svg = svg_olym_board_coloring(3, min(6, cols_n), 2, f"3×{cols_n}: ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp22,
            q_en, q_ar, ans,
            [3**k_half, 4 * A[k_half - 1], ans - 6, ans + 8],
            f"Let {m('A_{2k}')} be full tilings of {m('3 \\times 2k')}; eliminating corner-missing states yields {m('A_{2k} = 4A_{2k-2} - A_{2k-4}')}.",
            f"ليكن {m('A_{2k}')} عدد تبليطات الشبكة {m('3 \\times 2k')}؛ بحذف الحالات المساعدة تنتج العلاقة {m('A_{2k} = 4A_{2k-2} - A_{2k-4}')}.",
            "Use coupled state recurrences A_{2k} = 3 A_{2k-2} + 2 B_{2k-3}, which reduces to A_{2k} = 4 A_{2k-2} - A_{2k-4}.",
            [
                f"For {m('3 \\times 2k')} boards, base cases are {m('A_0 = 1')} and {m('A_2 = 3')}.",
                f"Coupling full columns {m('A_{2k}')} and protruding-domino states gives the recurrence {m('A_{2k} = 4A_{2k-2} - A_{2k-4}')}.",
                f"Computing sequentially gives {m(', '.join(f'A_{{{2*i}}} = {A[i]}' for i in range(len(A))))}, so {m(f'A_{{{cols_n}}} = {ans}')}.",
            ],
            f"Notice {m(f'A_{{{cols_n}}} = {ans} > 3^{{{k_half}}} = {3**k_half}')} because dominoes can straddle the boundaries between {m('3 \\times 2')} blocks.",
            "نستخدم العلاقات التراجعية المترابطة التي تختزل إلى A_{2k} = 4A_{2k-2} - A_{2k-4}.",
            [
                f"الحالتان الأساسيتان هما {m('A_0 = 1')} و{m('A_2 = 3')}.",
                f"باستعمال التراجع {m('A_{2k} = 4A_{2k-2} - A_{2k-4}')} نحسب الحدود المتتالية.",
                f"نحصل على {m(', '.join(f'A_{{{2*i}}} = {A[i]}' for i in range(len(A))))} ومنه {m(f'A_{{{cols_n}}} = {ans}')}.",
            ],
            f"العدد أكبر من {m(f'3^{{{k_half}}} = {3**k_half}')} لوجود تبليطات تعبر حدود الكتل {m('3 \\times 2')}.",
            diagram_en=svg,
        ))

    # 328..330: Binary strings of length n avoiding "111" (Tribonacci recurrence T_n = T_{n-1} + T_{n-2} + T_{n-3})
    for idx_sub, n_bits in enumerate([6, 7, 8]):
        offset = 328 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = sum(1 for bits in itertools.product((0, 1), repeat=n_bits) if "111" not in "".join(map(str, bits)))
        trib = [1, 2, 4]
        while len(trib) <= n_bits:
            trib.append(trib[-1] + trib[-2] + trib[-3])
        assert ans == trib[n_bits]
        q_en = (
            f"How many binary strings of length {m(str(n_bits))} do not contain three consecutive "
            f"ones ({m('\\text{\"111\"}')})?"
        )
        q_ar = (
            f"كم سلسلة ثنائية طولها {m(str(n_bits))} لا تحتوي على ثلاثة واحدات متتالية "
            f"({m('\\text{\"111\"}')})؟"
        )
        svg = svg_digit_slots([f"n={n_bits}", "no 111", "Tₙ=?"], top_note="Tribonacci")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp22,
            q_en, q_ar, ans,
            [2**n_bits - (n_bits - 2), trib[n_bits - 1], ans + 4, ans - 3],
            f"Partition valid strings by their prefix {m('\\text{\"0\"}')}, {m('\\text{\"10\"}')}, or {m('\\text{\"110\"}')} to get {m('a_n = a_{n-1} + a_{n-2} + a_{n-3}')}.",
            f"صنّف السلاسل الصالحة حسب بدايتها {m('\\text{\"0\"}')} أو {m('\\text{\"10\"}')} أو {m('\\text{\"110\"}')} لتحصل على {m('a_n = a_{n-1} + a_{n-2} + a_{n-3}')}.",
            "Group valid strings by the position of the first zero to obtain the Tribonacci recurrence a_n = a_{n-1} + a_{n-2} + a_{n-3}.",
            [
                f"Base values are {m('a_1 = 2')}, {m('a_2 = 4')}, and {m('a_3 = 7')} (all {m('2^3 = 8')} strings except {m('111')}).",
                f"Any valid string of length {m('k \\ge 4')} starts with {m('0')}, {m('10')}, or {m('110')}, so {m('a_k = a_{k-1} + a_{k-2} + a_{k-3}')}.",
                f"Generating terms up to {m(f'k = {n_bits}')} yields {m(', '.join(str(x) for x in trib[1:]))}, so {m(f'a_{{{n_bits}}} = {ans}')}.",
            ],
            f"Check: {m(f'{trib[n_bits - 1]} + {trib[n_bits - 2]} + {trib[n_bits - 3]} = {ans}')}.",
            "نصنّف السلاسل الصالحة حسب موضع أول صفر فنحصل على علاقة تريبوناتشي التراجعية.",
            [
                f"القيم الابتدائية هي {m('a_1 = 2')} و{m('a_2 = 4')} و{m('a_3 = 7')}.",
                f"كل سلسلة صالحة تبدأ بـ {m('0')} أو {m('10')} أو {m('110')} ومنه {m('a_k = a_{k-1} + a_{k-2} + a_{k-3}')}.",
                f"بحساب الحدود متتالية نجد {m(f'a_{{{n_bits}}} = {ans}')}.",
            ],
            f"التحقق: {m(f'{trib[n_bits - 1]} + {trib[n_bits - 2]} + {trib[n_bits - 3]} = {ans}')}.",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 23: olym_t2_comb_graph_degrees_trees (OLYM-T2-331..345)
    # ------------------------------------------------------------------
    bp23 = "olym_t2_comb_graph_degrees_trees"

    # Easy (331..335): Handshaking Lemma & Forest edge formula E = V - c
    graph_easy = [
        (8, 3, 6, 4),    # 8 vertices of deg 3, 6 vertices of deg 4 -> E = (24 + 24)/2 = 24
        (10, 3, 8, 5),   # (30 + 40)/2 = 35
        (12, 4, 6, 5),   # (48 + 30)/2 = 39
        (9, 4, 8, 3),    # (36 + 24)/2 = 30
        (14, 3, 10, 4),  # (42 + 40)/2 = 41
    ]
    for offset, (n1, d1, n2, d2) in enumerate(graph_easy, 331):
        qid = f"OLYM-T2-{offset:03d}"
        deg_sum = n1 * d1 + n2 * d2
        assert deg_sum % 2 == 0
        ans = deg_sum // 2
        q_en = (
            f"A simple graph {m('G')} has {m(str(n1))} vertices of degree {m(str(d1))} and {m(str(n2))} "
            f"vertices of degree {m(str(d2))}, and no other vertices. How many edges does {m('G')} have?"
        )
        q_ar = (
            f"بيان بسيط {m('G')} يحتوي على {m(str(n1))} رؤوس من الدرجة {m(str(d1))} و{m(str(n2))} رؤوس "
            f"من الدرجة {m(str(d2))} فقط. كم ضلعاً (حافة) في البيان {m('G')}؟"
        )
        svg = svg_graph_cycle_chords(6, True)
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Easy", bp23,
            q_en, q_ar, ans,
            [deg_sum, ans - (n1 + n2) // 2, ans + 4, n1 + n2 - 1],
            f"Apply Euler's Handshaking Lemma: {m('2|E| = \\sum_{v \\in V} \\deg(v)')}.",
            f"طبّق توطئة المصافحة لأويلر: {m('2|E| = \\sum_{v \\in V} \\deg(v)')}.",
            "Sum all vertex degrees and divide by 2 via the Handshaking Lemma.",
            [
                f"Compute the sum of degrees: {m(f'\\sum \\deg(v) = {n1} \\cdot {d1} + {n2} \\cdot {d2} = {deg_sum}')}.",
                f"By the Handshaking Lemma, every edge contributes {m('2')} to the total degree sum.",
                f"Therefore {m(f'|E| = \\frac{{{deg_sum}}}{{2}} = {ans}')}.",
            ],
            f"Double-checking {m(f'2 \\cdot {ans} = {deg_sum}')} confirms the edge count.",
            "نجمع درجات جميع الرؤوس ونقسم المجموع على 2 وفق توطئة المصافحة.",
            [
                f"نحسب مجموع درجات الرؤوس: {m(f'{n1} \\times {d1} + {n2} \\times {d2} = {deg_sum}')}.",
                f"بموجب توطئة المصافحة يساهم كل ضلع بمقدار {m('2')} في مجموع الدرجات.",
                f"إذن عدد الأضلاع هو {m(f'|E| = {deg_sum}/2 = {ans}')}.",
            ],
            f"التحقق: ضعف عدد الأضلاع يساوي {m(str(deg_sum))}.",
            diagram_en=svg,
        ))

    # Medium (336..340): Number of leaves in a tree given internal vertex degrees: L = 2 + sum (d_i - 2)
    tree_med = [
        (4, 3, 3, 4),   # 4 vertices of deg 3, 3 vertices of deg 4 -> L = 2 + 4(1) + 3(2) = 12
        (5, 3, 4, 4),   # L = 2 + 5(1) + 4(2) = 15
        (6, 3, 2, 5),   # L = 2 + 6(1) + 2(3) = 14
        (3, 4, 4, 5),   # L = 2 + 3(2) + 4(3) = 20
        (5, 3, 3, 5),   # L = 2 + 5(1) + 3(3) = 16
    ]
    for offset, (k1, deg1, k2, deg2) in enumerate(tree_med, 336):
        qid = f"OLYM-T2-{offset:03d}"
        ans = 2 + k1 * (deg1 - 2) + k2 * (deg2 - 2)
        v_tot = k1 + k2 + ans
        e_tot = v_tot - 1
        assert k1 * deg1 + k2 * deg2 + ans == 2 * e_tot
        q_en = (
            f"A tree {m('T')} has {m(str(k1))} internal vertices of degree {m(str(deg1))}, {m(str(k2))} "
            f"internal vertices of degree {m(str(deg2))}, and all remaining vertices are leaves (degree {m('1')}). "
            f"How many leaves does {m('T')} have?"
        )
        q_ar = (
            f"شجرة {m('T')} تحتوي على {m(str(k1))} رؤوس داخلية من الدرجة {m(str(deg1))} و{m(str(k2))} رؤوس "
            f"داخلية من الدرجة {m(str(deg2))}، وجميع الرؤوس الباقية أوراق (من الدرجة {m('1')}). "
            f"كم ورقة في الشجرة {m('T')}؟"
        )
        svg = svg_olym_bipartite_graph(3, 4, note="Leaves=?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Medium", bp23,
            q_en, q_ar, ans,
            [ans - 2, ans + 2, k1 * deg1 + k2 * deg2, ans - 1],
            f"In a tree with {m('L')} leaves, {m('|V| = L + ' + str(k1 + k2))} and {m('2(|V| - 1) = L + ' + str(k1 * deg1 + k2 * deg2))}.",
            f"في الشجرة ذات {m('L')} ورقة يكون {m('|V| = L + ' + str(k1 + k2))} ومجموع الدرجات {m('2(|V| - 1)')}.",
            "Use the tree degree identity L = 2 + sum_{internal} (deg(v) - 2).",
            [
                f"Let {m('L')} be the number of leaves. Then {m(f'|V| = L + {k1 + k2}')} and {m(f'|E| = |V| - 1 = L + {k1 + k2 - 1}')}.",
                f"By the Handshaking Lemma, {m(f'L + {k1}\\cdot{deg1} + {k2}\\cdot{deg2} = 2(L + {k1 + k2 - 1})')}.",
                f"Solving for {m('L')} gives {m(f'L = 2 + {k1}({deg1} - 2) + {k2}({deg2} - 2) = {ans}')}.",
            ],
            f"With {m(f'L = {ans}')}, {m(f'|V| = {v_tot}')}, {m(f'|E| = {e_tot}')}, and {m(f'\\sum \\deg = {2 * e_tot}')}.",
            "نستعمل متطابقة درجات الشجرة L = 2 + sum (deg(v) - 2) على الرؤوس الداخلية.",
            [
                f"ليكن {m('L')} عدد الأوراق؛ إذن عدد الرؤوس {m(f'|V| = L + {k1 + k2}')} وعدد الأضلاع {m('|V| - 1')}.",
                f"من توطئة المصافحة: {m(f'L + {k1 * deg1 + k2 * deg2} = 2(L + {k1 + k2 - 1})')}.",
                f"بحل المعادلة نجد {m(f'L = 2 + {k1}({deg1}-2) + {k2}({deg2}-2) = {ans}')}.",
            ],
            f"التحقق: مجموع الدرجات يساوي {m(str(2 * e_tot))} وهو ضعف عدد الأضلاع {m(str(e_tot))}.",
            diagram_en=svg,
        ))

    # Hard (341..345): Mantel's theorem floor(n^2/4) (341..343) & Hamiltonian/Connectivity edge threshold C(n-1, 2) + 1 (344..345)
    for idx_sub, n_v in enumerate([11, 13, 16]):
        offset = 341 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = (n_v * n_v) // 4
        a_part = n_v // 2
        b_part = n_v - a_part
        assert a_part * b_part == ans
        q_en = (
            f"By Mantel's theorem, what is the maximum possible number of edges in a simple graph on "
            f"{m(str(n_v))} vertices that contains no triangle ({m('K_3')})?"
        )
        q_ar = (
            f"بموجب مبرهنة مانتل، ما أكبر عدد ممكن من الأضلاع في بيان بسيط يحتوي على "
            f"{m(str(n_v))} رأساً ولا يحتوي على أي مثلث ({m('K_3')})؟"
        )
        svg = svg_olym_bipartite_graph(4, 4, note=f"n={n_v}: ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp23,
            q_en, q_ar, ans,
            [math.comb(n_v, 2) // 2, ans - a_part, ans + 3, (n_v - 1) * (n_v - 2) // 2],
            f"By Mantel's theorem, the extremal triangle-free graph is the balanced complete bipartite graph {m(f'K_{{{a_part}, {b_part}}}')}.",
            f"بموجب مبرهنة مانتل، يتحقق الحد الأقصى في البيان الثنائي الكامل المتوازن {m(f'K_{{{a_part}, {b_part}}}')}.",
            "Apply Mantel's theorem: maximum edges in a triangle-free n-vertex graph is floor(n^2 / 4).",
            [
                f"By Mantel's theorem (the triangle case of Turán's theorem), a triangle-free graph on {m('n')} vertices has at most {m('\\lfloor n^2 / 4 \\rfloor')} edges.",
                f"This maximum is achieved by partitioning the {m(str(n_v))} vertices into two parts of sizes {m(str(a_part))} and {m(str(b_part))} in {m(f'K_{{{a_part}, {b_part}}}')}.",
                f"Multiplying the part sizes gives {m(f'{a_part} \\cdot {b_part} = \\lfloor {n_v}^2 / 4 \\rfloor = {ans}')}.",
            ],
            f"Every bipartite graph is triangle-free, and adding any edge within a part creates a {m('K_3')}.",
            "نطبق مبرهنة مانتل التي تنص على أن أكبر عدد أضلاع في بيان خالٍ من المثلثات هو floor(n^2 / 4).",
            [
                f"بموجب مبرهنة مانتل لا يتجاوز عدد الأضلاع {m('\\lfloor n^2 / 4 \\rfloor')}.",
                f"يتحقق هذا الحد في البيان الثنائي الكامل المتوازن {m(f'K_{{{a_part}, {b_part}}}')}.",
                f"بحساب الجداء نجد {m(f'{a_part} \\times {b_part} = {ans}')}.",
            ],
            f"البيان الثنائي خالٍ تماماً من الدورات الفردية وبالتالي لا يحوي أي مثلث.",
            diagram_en=svg,
        ))

    for idx_sub, n_v in enumerate([10, 12]):
        offset = 344 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = math.comb(n_v - 1, 2) + 1
        q_en = (
            f"In an Intermediate Olympiad extremal graph problem, what is the minimum number of edges "
            f"that guarantees any simple graph on {m(str(n_v))} vertices is connected?"
        )
        q_ar = (
            f"في مسألة بيانات متطرفة للأولمبياد المتوسط، ما أصغر عدد من الأضلاع يضمن أن يكون أي بيان بسيط "
            f"مكوّن من {m(str(n_v))} رؤوس متصلاً حتماً؟"
        )
        svg = svg_graph_cycle_chords(6, True)
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp23,
            q_en, q_ar, ans,
            [math.comb(n_v - 1, 2), n_v - 1, math.comb(n_v, 2) - n_v, ans + 2],
            f"The most edges a disconnected graph on {m(str(n_v))} vertices can have occurs in {m(f'K_{{{n_v - 1}}} \\sqcup K_1')}, which has {m(f'\\binom{{{n_v - 1}}}{{2}}')} edges.",
            f"أكبر عدد أضلاع في بيان غير متصل على {m(str(n_v))} رؤوس يتحقق في {m(f'K_{{{n_v - 1}}} \\sqcup K_1')} ويساوي {m(f'\\binom{{{n_v - 1}}}{{2}}')}.",
            "Add 1 to the maximum edge count C(n - 1, 2) of a disconnected n-vertex graph.",
            [
                f"A disconnected graph on {m(str(n_v))} vertices with parts of sizes {m('k')} and {m(f'{n_v} - k')} has at most {m(f'\\binom{{k}}{{2}} + \\binom{{{n_v} - k}}{{2}}')} edges.",
                f"By convexity, this is maximized at {m('k = 1')}: {m(f'K_{{{n_v - 1}}} \\sqcup K_1')} has {m(f'\\binom{{{n_v - 1}}}{{2}} = {ans - 1}')} edges and is still disconnected.",
                f"Adding one more edge forces connectivity: {m(f'{ans - 1} + 1 = {ans}')}.",
            ],
            f"While {m(str(n_v - 1))} edges suffice to build one specific tree, {m(str(ans))} edges are required to guarantee connectivity for every simple graph.",
            "نضيف ضلعاً واحداً إلى أكبر عدد أضلاع ممكن في بيان غير متصل وهو C(n - 1, 2).",
            [
                f"أكبر عدد أضلاع في بيان غير متصل على {m(str(n_v))} رؤوس يتحقق عندما ينفصل رأس واحد عن بيان كامل {m(f'K_{{{n_v - 1}}}')}.",
                f"عدد أضلاع هذا البيان غير المتصل هو {m(f'\\binom{{{n_v - 1}}}{{2}} = {ans - 1}')}.",
                f"بإضافة ضلع واحد يصبح الاتصال مضموناً دائماً: {m(f'{ans - 1} + 1 = {ans}')}.",
            ],
            f"نفرق بين أصغر شجرة متصلة ({m(str(n_v - 1))}) وبين الحد الذي يضمن الاتصال لأي توزيع للأضلاع ({m(str(ans))}).",
            diagram_en=svg,
        ))

    # ------------------------------------------------------------------
    # Blueprint 24: olym_t2_comb_monovariants_games (OLYM-T2-346..360)
    # ------------------------------------------------------------------
    bp24 = "olym_t2_comb_monovariants_games"

    # Easy (346..350): Subtraction game winning first move: pile of N stones, take 1..m per turn, last stone wins -> N mod (m + 1)
    game_easy = [
        (100, 6),   # 100 mod 7 = 2
        (149, 7),   # 149 mod 8 = 5
        (200, 8),   # 200 mod 9 = 2 -> pick (202, 8) -> 4
        (250, 10),  # 250 mod 11 = 8 -> pick (248, 10) -> 6
        (300, 12),  # 300 mod 13 = 1 -> pick (302, 12) -> 3
    ]
    game_easy[2] = (202, 8)
    game_easy[3] = (248, 10)
    game_easy[4] = (302, 12)
    for offset, (N_pile, m_max) in enumerate(game_easy, 346):
        qid = f"OLYM-T2-{offset:03d}"
        ans = N_pile % (m_max + 1)
        assert 1 <= ans <= m_max
        q_en = (
            f"A pile contains {m(str(N_pile))} stones. Two players alternate turns removing between "
            f"{m('1')} and {m(str(m_max))} stones inclusive; the player who takes the last stone wins. "
            f"How many stones must the first player remove on the opening turn to guarantee a win?"
        )
        q_ar = (
            f"كومة تحتوي على {m(str(N_pile))} حجراً. يتناوب لاعبان على سحب عدد من الأحجار يتراوح بين "
            f"{m('1')} و{m(str(m_max))} في كل دور، والفائز هو من يسحب الحجر الأخير. "
            f"كم حجراً يجب أن يسحب اللاعب الأول في نقالته الأولى ليضمن الفوز؟"
        )
        svg = svg_olym_pigeonhole_boxes(4, f"N={N_pile}", f"mod {m_max+1}: ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Easy", bp24,
            q_en, q_ar, ans,
            [(m_max + 1) - ans if (m_max + 1) - ans != ans else (ans % m_max) + 1, m_max, 1 if ans != 1 else 2, (ans + 2) % m_max + 1],
            f"Multiples of {m(str(m_max + 1))} are losing positions; reduce {m(str(N_pile))} modulo {m(str(m_max + 1))}.",
            f"مضاعفات العدد {m(str(m_max + 1))} هي مواقع خاسرة؛ احسب باقي قسمة {m(str(N_pile))} على {m(str(m_max + 1))}.",
            "Maintain the modulo (m + 1) invariant by reducing the pile to a multiple of m + 1 after every move.",
            [
                f"Whenever the opponent removes {m('k \\in \\{1, \\dots, ' + str(m_max) + '\\}')} stones, the first player can remove {m(f'{m_max + 1} - k')} stones to preserve multiples of {m(str(m_max + 1))}.",
                f"Divide {m(str(N_pile))} by {m(str(m_max + 1))}: {m(f'{N_pile} = {N_pile // (m_max + 1)} \\cdot {m_max + 1} + {ans}')}.",
                f"Removing {m(str(ans))} stones leaves a multiple of {m(str(m_max + 1))}, securing a winning strategy.",
            ],
            f"Since {m(f'1 \\le {ans} \\le {m_max}')}, removing {m(str(ans))} stones is a legal and unique winning opening move.",
            "نحافظ على اللامتغير معيار (m + 1) بترك مضاعف للعدد (m + 1) بعد كل دور.",
            [
                f"المواقع التي تقبل القسمة على {m(str(m_max + 1))} مواقع خاسرة لمن عليه الدور.",
                f"نقسم {m(str(N_pile))} على {m(str(m_max + 1))}: {m(f'{N_pile} = {N_pile // (m_max + 1)} \\times {m_max + 1} + {ans}')}.",
                f"لذلك يسحب اللاعب الأول {m(str(ans))} أحجار ليترك لمنافسه مضاعفاً للعدد {m(str(m_max + 1))}.",
            ],
            f"النقلة {m(str(ans))} قانونية وتقع ضمن المدى المسموح {m(f'[1, {m_max}]')}.",
            diagram_en=svg,
        ))

    # Medium (351..355): Blackboard shifted-sum invariant: replace (a, b) with a + b - c on {1, ..., n}
    inv_med = [
        (20, 3),   # sum(1..20) - 19*3 = 210 - 57 = 153
        (25, 4),   # 325 - 24*4 = 229
        (30, 5),   # 465 - 29*5 = 320
        (40, 6),   # 820 - 39*6 = 586
        (50, 8),   # 1275 - 49*8 = 883
    ]
    for offset, (n_max, c_shift) in enumerate(inv_med, 351):
        qid = f"OLYM-T2-{offset:03d}"
        s_init = n_max * (n_max + 1) // 2
        ans = s_init - (n_max - 1) * c_shift
        # Verify invariant: sum(x_i - c) is constant
        assert ans - c_shift == sum(k - c_shift for k in range(1, n_max + 1))
        q_en = (
            f"The integers {m(f'1, 2, \\dots, {n_max}')} are written on a blackboard. Each step, two numbers "
            f"{m('a')} and {m('b')} are erased and replaced by {m(f'a + b - {c_shift}')}. After {m(str(n_max - 1))} "
            f"steps, only one number remains. What is this final number?"
        )
        q_ar = (
            f"كُتبت الأعداد الصحيحة {m(f'1, 2, \\dots, {n_max}')} على سبورة. في كل خطوة يُمسح عددان "
            f"{m('a')} و{m('b')} ويُكتب مكانهما العدد {m(f'a + b - {c_shift}')}. بعد {m(str(n_max - 1))} خطوة "
            f"يبقى عدد واحد فقط. ما قيمة هذا العدد النهائي؟"
        )
        svg = svg_function_machine(f"1..{n_max}", f"a+b−{c_shift}", f"{n_max-1}×", "X = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Medium", bp24,
            q_en, q_ar, ans,
            [s_init - n_max * c_shift, s_init, ans + c_shift, ans - 2 * c_shift],
            f"Notice that {m(f'(a + b - {c_shift}) - {c_shift} = (a - {c_shift}) + (b - {c_shift})')}, so {m(f'\\sum (x_i - {c_shift})')} is invariant!",
            f"لاحظ أن {m(f'(a + b - {c_shift}) - {c_shift} = (a - {c_shift}) + (b - {c_shift})')}، أي أن المجموع {m(f'\\sum (x_i - {c_shift})')} لامتغير!",
            "Track the invariant shifted sum sum(x_i - c), or note each of the n - 1 merges subtracts c from the total sum.",
            [
                f"Initial sum of the {m(str(n_max))} numbers is {m(f'\\frac{{{n_max}({n_max} + 1)}}{{2}} = {s_init}')}.",
                f"Each operation decreases the count of numbers by {m('1')} and decreases the total sum by exactly {m(str(c_shift))}.",
                f"After {m(str(n_max - 1))} operations, the single remaining number is {m(f'{s_init} - {n_max - 1} \\cdot {c_shift} = {ans}')}.",
            ],
            f"Shifted invariant check: {m(f'X - {c_shift} = \\sum_{{k=1}}^{{{n_max}}} (k - {c_shift}) = {ans - c_shift}')}, giving {m(f'X = {ans}')}.",
            "نتتبع اللامتغير لمجموع الأعداد المزاحة، حيث تنقص كل خطوة المجموع الكلي بمقدار ثابت c.",
            [
                f"المجموع الابتدائي للأعداد هو {m(f'\\frac{{{n_max}({n_max + 1})}}{{2}} = {s_init}')}.",
                f"في كل خطوة من الخطوات البالغ عددها {m(str(n_max - 1))} ينقص المجموع الكلي بمقدار {m(str(c_shift))} بالضبط.",
                f"إذن العدد الوحيد المتبقي في النهاية هو {m(f'{s_init} - {n_max - 1} \\times {c_shift} = {ans}')}.",
            ],
            f"التحقق باللامتغير المزاح يؤكد أن {m(f'X = {ans}')} بغض النظر عن ترتيب الاختيار.",
            diagram_en=svg,
        ))

    # Hard (356..360): Multiplicative blackboard invariants & Nim XOR / monovariant games
    # 356..358: Replace a, b with (a*b + a + b) on {1/k} or small set, or replace a, b with (a+b)/(1+ab), or Nim XOR!
    # Let's do 3 Nim XOR winning-pile problems (356..358) and 2 multiplicative invariant (x+1)(y+1)-1 problems (359..360)!
    nim_cases = [
        (5, 9, 13),    # 5 ^ 9 = 12; to make 13 -> 12, remove 13 - 12 = 1 stone from pile 3! Wait: let's ask for the new size or number of stones removed from the largest pile!
        (6, 11, 15),   # 6 ^ 11 = 13; remove 15 - 13 = 2 stones from the pile of 15 -> 2? Let's make answers larger/distinct!
        (7, 12, 18),   # 7 ^ 12 = 11; remove 18 - 11 = 7 stones from pile of 18!
    ]
    nim_cases = [
        (6, 10, 15),   # 6 ^ 10 = 12 -> remove 15 - 12 = 3 stones from the pile of 15
        (7, 13, 19),   # 7 ^ 13 = 10 -> remove 19 - 10 = 9 stones from the pile of 19
        (9, 14, 21),   # 9 ^ 14 = 7 -> remove 21 - 7 = 14 stones from the pile of 21
    ]
    for idx_sub, (p1, p2, p3) in enumerate(nim_cases):
        offset = 356 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        target_p3 = p1 ^ p2
        assert target_p3 < p3
        ans = p3 - target_p3
        assert (p1 ^ p2 ^ (p3 - ans)) == 0
        q_en = (
            f"In a three-pile game of Nim with pile sizes {m(f'({p1}, {p2}, {p3})')}, how many stones "
            f"must the first player remove from the pile of size {m(str(p3))} to leave a balanced "
            f"XOR-sum {m('0')} position?"
        )
        q_ar = (
            f"في لعبة نيم المكونة من ثلاث أكوام أحجامها {m(f'({p1}, {p2}, {p3})')}، كم حجراً يجب أن يسحب "
            f"اللاعب الأول من الكومة ذات الحجم {m(str(p3))} ليترك موقعاً متوازناً مجموعه الثنائي الحصري (XOR) يساوي {m('0')}؟"
        )
        svg = svg_olym_pigeonhole_boxes(3, f"{p1},{p2},{p3}", "Δ = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp24,
            q_en, q_ar, ans,
            [target_p3, p3 - (p2 - p1), ans + 2, max(1, ans - 2)],
            f"By Bouton's theorem, reduce the third pile to {m(f'{p1} \\oplus {p2} = {target_p3}')}.",
            f"بموجب مبرهنة بوتون، اختزل الكومة الثالثة إلى القيمة {m(f'{p1} \\oplus {p2} = {target_p3}')}.",
            "Compute the binary XOR sum of the first two piles and subtract it from the third pile.",
            [
                f"By Bouton's theorem for Nim, a position is losing for the next player if and only if its Nim-sum (bitwise XOR) is {m('0')}.",
                f"Compute the XOR of the first two piles in binary: {m(f'{p1} \\oplus {p2} = {target_p3}')}.",
                f"To reduce the third pile from {m(str(p3))} to {m(str(target_p3))}, remove {m(f'{p3} - {target_p3} = {ans}')} stones.",
            ],
            f"After removing {m(str(ans))} stones, the piles are {m(f'({p1}, {p2}, {target_p3})')} with XOR-sum {m(f'{p1} \\oplus {p2} \\oplus {target_p3} = 0')}.",
            "نحسب المجموع الثنائي الحصري (XOR) للكومتين الأوليين ثم نطرحه من حجم الكومة الثالثة.",
            [
                f"بموجب مبرهنة بوتون في لعبة نيم، يكون الموقع متوازناً إذا وفقط إذا كان مجموع XOR للأكوام يساوي {m('0')}.",
                f"نحسب في النظام الثنائي: {m(f'{p1} \\oplus {p2} = {target_p3}')}.",
                f"لتقليص الكومة الثالثة من {m(str(p3))} إلى {m(str(target_p3))} نسحب {m(f'{p3} - {target_p3} = {ans}')} حجراً.",
            ],
            f"بعد السحب تصبح الأحجام {m(f'({p1}, {p2}, {target_p3})')} ومجموعها الحصري {m('0')}.",
            diagram_en=svg,
        ))

    # 359..360: Multiplicative invariant a*b + a + b = (a+1)(b+1) - 1 on {1, 2, ..., n}: final number is (n+1)! - 1
    for idx_sub, n_top in enumerate([5, 6]):
        offset = 359 + idx_sub
        qid = f"OLYM-T2-{offset:03d}"
        ans = math.factorial(n_top + 1) - 1
        val = 1
        for x in range(2, n_top + 1):
            val = val * x + val + x
        assert val == ans
        q_en = (
            f"The integers {m(f'1, 2, \\dots, {n_top}')} are written on a board. Repeatedly, two numbers "
            f"{m('a, b')} are erased and replaced by {m('ab + a + b')} until one number remains. "
            f"What is the final number?"
        )
        q_ar = (
            f"كُتبت الأعداد {m(f'1, 2, \\dots, {n_top}')} على لوح. في كل خطوة يُمسح عددان {m('a, b')} "
            f"ويُكتب مكانهما {m('ab + a + b')} حتى يبقى عدد واحد فقط. ما قيمة هذا العدد النهائي؟"
        )
        svg = svg_function_machine(f"1..{n_top}", "ab+a+b", "∏(x+1)", "X = ?")
        qs.append(make_olym_q(
            qid, LEVEL, "Combinatorics", "Hard", bp24,
            q_en, q_ar, ans,
            [math.factorial(n_top + 1), math.factorial(n_top) - 1, ans - n_top, ans + 2],
            f"Factor {m('(ab + a + b) + 1 = (a + 1)(b + 1)')}, showing that {m('\\prod (x_i + 1)')} is an invariant!",
            f"حلّل المقدار {m('(ab + a + b) + 1 = (a + 1)(b + 1)')} لتستنتج أن الجداء {m('\\prod (x_i + 1)')} لامتغير!",
            "Use the identity (ab + a + b) + 1 = (a + 1)(b + 1) so the product of (x_i + 1) remains invariant.",
            [
                f"Observe the algebraic identity {m('(ab + a + b) + 1 = (a + 1)(b + 1)')}.",
                f"Thus the product {m('\\prod (x_i + 1)')} over all numbers on the board is invariant under every replacement.",
                f"Initially {m(f'\\prod_{{k=1}}^{{{n_top}}} (k + 1) = 2 \\cdot 3 \\cdots {n_top + 1} = {n_top + 1}! = {ans + 1}')}, so the final number {m('X')} satisfies {m(f'X + 1 = {ans + 1}')}, giving {m(f'X = {ans}')}.",
            ],
            f"Regardless of the order in which pairs are merged, {m(f'X = {n_top + 1}! - 1 = {ans}')}.",
            "نستعمل المتطابقة (ab + a + b) + 1 = (a + 1)(b + 1) فيبقى جداء (x_i + 1) ثابتاً لا يتغير.",
            [
                f"نلاحظ المتطابقة الجبرية {m('(ab + a + b) + 1 = (a + 1)(b + 1)')}.",
                f"إذن الجداء {m('\\prod (x_i + 1)')} لامتغير في كل خطوة.",
                f"في البداية يساوي الجداء {m(f'2 \\times 3 \\times \\cdots \\times {n_top + 1} = {n_top + 1}! = {ans + 1}')}، فيكون العدد النهائي {m(f'X = {ans + 1} - 1 = {ans}')}.",
            ],
            f"قيمة العدد النهائي {m(str(ans))} ثابتة ومستقلة تماماً عن ترتيب الدمج.",
            diagram_en=svg,
        ))

    return qs


def build_tier2_bank() -> list[dict]:
    """Build and return all 360 verified Tier 2 Olympiad questions (OLYM-T2-001..360)."""
    bank: list[dict] = []
    bank.extend(_gen_u21_number_theory())
    bank.extend(_gen_u22_algebra())
    bank.extend(_gen_u23_inequalities())
    bank.extend(_gen_u24_geometry_i())
    bank.extend(_gen_u25_geometry_ii())
    bank.extend(_gen_u26_combinatorics())
    assert len(bank) == 360, f"Expected 360 questions, got {len(bank)}"
    return bank
