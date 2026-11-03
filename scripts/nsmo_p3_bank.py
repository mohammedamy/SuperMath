"""NSMO (Mawhiba) Phase 3: Senior National Olympiad (Grade 10) Question Bank — 450 Programmatically Verified Questions."""
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
    svg_angle_bisector_tri,
    svg_area_identity_square,
    svg_binary_bulbs,
    svg_circle_chords,
    svg_coord_diamond,
    svg_cube_in_cylinder,
    svg_cyclic_quad,
    svg_digit_slots,
    svg_factor_tree,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_median_tri,
    svg_number_strip,
    svg_parabola_roots,
    svg_polyomino,
    svg_power_of_point,
    svg_right_tri_incircle,
    svg_round_table,
    svg_square_circle_shaded,
    svg_venn_2,
)

LEVEL = NSMO_LEVELS[2]  # "Phase 3: Senior National Olympiad (Grade 10)"


def _phi(n: int) -> int:
    res = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            res -= res // p
        p += 1
    if x > 1:
        res -= res // x
    return res


def _vp_fact(n: int, p: int) -> int:
    s = 0
    while n > 0:
        n //= p
        s += n
    return s


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
        qid = f"NSMO-G10-{len(self.items) + 1:03d}"
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
# UNIT 3.1 — Euler's Totient, Modular Powers & Legendre's Formula (75 Qs)
# =============================================================================
def _add_unit_3_1(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 1. nsmo_g10_euler_totient_coprime (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g10_euler_totient_coprime"
    easy_tot = [
        (72, "2³ = 8", "3² = 9", "3", "3", "2^3 \\times 3^2", "2, 3"),
        (100, "2² = 4", "5² = 25", "5", "5", "2^2 \\times 5^2", "2, 5"),
        (120, "8", "15", "3", "5", "2^3 \\times 3 \\times 5", "2, 3, 5"),
        (150, "6", "25", "5", "5", "2 \\times 3 \\times 5^2", "2, 3, 5"),
        (210, "6", "35", "5", "7", "2 \\times 3 \\times 5 \\times 7", "2, 3, 5, 7"),
    ]
    en_frames_e = [
        "In a Senior Mawhiba number theory drill, how many positive integers {k} satisfy {cond} and {gcd}?",
        "How many proper or unit fractions {frac} with {k_rng} are already in lowest terms (meaning {gcd})?",
        "Find the value of Euler's totient function {phi_n}, the count of integers in {set_n} relatively prime to {n}.",
        "A modular cipher uses modulus {n}. How many residue keys {k} in {set_n} satisfy {gcd}?",
        "Among the first {n} positive integers, how many share **no** prime factor with {n}?",
    ]
    ar_frames_e = [
        "في تدريب المرحلة الثانوية لأولمبياد موهبة، كم عدداً صحيحاً موجباً {k} يحقق {cond} و{gcd}؟",
        "كم كسراً من الصورة {frac} حيث {k_rng} يكون في أبسط صورة (أي {gcd})؟",
        "أوجد قيمة دالة أويلر {phi_n}، وهي عدد الأعداد في المجموعة {set_n} الأولية نسبياً مع {n}.",
        "يستخدم نظام تشفير معياري المقسوم {n}. كم مفتاحاً {k} في المجموعة {set_n} يحقق {gcd}؟",
        "من بين أول {n} عدداً صحيحاً موجباً، كم عدداً **لا** يشترك في أي عامل أولي مع {n}؟",
    ]
    for idx, (n, l1, r1, rl, rr, fac_tex, plist_tex) in enumerate(easy_tot):
        ans = _phi(n)
        assert ans == sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)
        q_en = en_frames_e[idx].format(
            k=m("k"), cond=m(f"1 \\le k \\le {n}"), gcd=m(f"\\gcd(k, {n}) = 1"),
            frac=m(f"\\frac{{k}}{{{n}}}"), k_rng=m(f"1 \\le k \\le {n}"),
            phi_n=m(f"\\varphi({n})"), set_n=m(f"\\{{1, 2, \\dots, {n}\\}}"), n=m(n),
        )
        q_ar = ar_frames_e[idx].format(
            k=m("k"), cond=m(f"1 \\le k \\le {n}"), gcd=m(f"\\gcd(k, {n}) = 1"),
            frac=m(f"\\frac{{k}}{{{n}}}"), k_rng=m(f"1 \\le k \\le {n}"),
            phi_n=m(f"\\varphi({n})"), set_n=m(f"\\{{1, 2, \\dots, {n}\\}}"), n=m(n),
        )
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans,
            [ans - 8, ans + 6, n // 2, ans + 12],
            f"Factor {m(f'{n} = {fac_tex}')} and apply {m('\\varphi(n) = n \\prod (1 - 1/p)')}.",
            f"حلّل {m(f'{n} = {fac_tex}')} وطبّق قانون دالة أويلر {m('\\varphi(n) = n \\prod (1 - 1/p)')}.",
            f"Count integers coprime to {m(n)} using Euler's totient product over its distinct prime factors.",
            [
                f"Factor {m(f'{n} = {fac_tex}')}; the distinct prime factors are {m(plist_tex)}.",
                f"Multiply {m(n)} by {m('(1 - 1/p)')} once for each distinct prime factor {m('p')}.",
                f"Evaluating the product gives {m(f'\\varphi({n}) = {ans}')}.",
            ],
            f"Every prime factor of {m(n)} is filtered out cleanly, leaving exact {m(ans)} coprime integers.",
            f"نحسب عدد الأعداد الأولية نسبياً مع {m(n)} بتطبيق صيغة أويلر على العوامل الأولية المختلفة.",
            [
                f"نحلّل العدد: {m(f'{n} = {fac_tex}')}، فالعوامل الأولية المختلفة هي {m(plist_tex)}.",
                f"نضرب {m(n)} في المقدار {m('(1 - 1/p)')} لكل عامل أولي مختلف {m('p')}.",
                f"تبسيط حاصل الضرب يعطي {m(f'\\varphi({n}) = {ans}')}.",
            ],
            f"تحقق: استبعاد مضاعفات {m(plist_tex)} بمبدأ التضمين والإقصاء يعطي {m(ans)} بالضبط.",
            diagram_en=svg_factor_tree(str(n), l1, r1, rl, rr),
        )

    # Medium (6): gcd(k, N) = g on 1..N -> phi(N/g)
    med_tot = [
        (360, 6, 60, "4", "15", "3", "5", "2^2 \\times 3 \\times 5"),
        (420, 7, 60, "4", "15", "3", "5", "2^2 \\times 3 \\times 5"),
        (450, 5, 90, "2", "45", "9", "5", "2 \\times 3^2 \\times 5"),
        (504, 6, 84, "4", "21", "3", "7", "2^2 \\times 3 \\times 7"),
        (600, 12, 50, "2", "25", "5", "5", "2 \\times 5^2"),
        (756, 9, 84, "4", "21", "3", "7", "2^2 \\times 3 \\times 7"),
    ]
    for N, g, q_val, l1, r1, rl, rr, fac_tex in med_tot:
        ans = _phi(q_val)
        assert ans == sum(1 for k in range(1, N + 1) if math.gcd(k, N) == g)
        B.add_math(
            tp, "Medium", bp,
            f"How many integers {m('k')} with {m(f'1 \\le k \\le {N}')} satisfy {m(f'\\gcd(k, {N}) = {g}')}?",
            f"كم عدداً صحيحاً {m('k')} يحقق {m(f'1 \\le k \\le {N}')} و{m(f'\\gcd(k, {N}) = {g}')}؟",
            ans, [ans + 4, ans - 4, q_val // 2, ans * 2],
            f"Write {m(f'k = {g}m')}; then {m(f'1 \\le m \\le {q_val}')} and {m(f'\\gcd(m, {q_val}) = 1')}.",
            f"ضع {m(f'k = {g}m')} فيصبح الشرط {m(f'1 \\le m \\le {q_val}')} مع {m(f'\\gcd(m, {q_val}) = 1')}.",
            f"Factor out the GCD {m(g)} to reduce the condition {m(f'\\gcd(k, {N}) = {g}')} to Euler's totient {m(f'\\varphi({q_val})')}!",
            [
                f"Every valid {m('k')} must be a multiple of {m(g)}: set {m(f'k = {g}m')} where {m(f'1 \\le m \\le {N} / {g} = {q_val}')}.",
                f"Dividing {m(f'\\gcd({g}m, {N}) = {g}')} by {m(g)} yields {m(f'\\gcd(m, {q_val}) = 1')}.",
                f"Since {m(f'{q_val} = {fac_tex}')}, Euler's totient gives {m(f'\\varphi({q_val}) = {ans}')}.",
            ],
            f"Check: {m(f'{g} \\times {q_val} = {N}')}, so exact {m(ans)} multiples of {m(g)} have no extra shared prime factor with {m(N)}.",
            f"نقسم الطرفين على القاسم المشترك الأكبر {m(g)} فتتحول المسألة مباشرة إلى حساب {m(f'\\varphi({q_val})')}!",
            [
                f"نكتب {m(f'k = {g}m')} حيث {m(f'1 \\le m \\le {N}/{g} = {q_val}')}.",
                f"الشرط {m(f'\\gcd({g}m, {N}) = {g}')} يكافئ {m(f'\\gcd(m, {q_val}) = 1')}.",
                f"نحلّل {m(f'{q_val} = {fac_tex}')} فنحسب {m(f'\\varphi({q_val}) = {ans}')}.",
            ],
            f"تحقق: كل قيمة لـ {m('m')} أولية نسبياً مع {m(q_val)} تولّد عدداً وحيداً {m(f'k = {g}m \\le {N}')}.",
            diagram_en=svg_factor_tree(f"{N}/{g}={q_val}", l1, r1, rl, rr),
        )

    # Hard (4): Gauss sum of coprime integers <= n is n * phi(n) / 2
    hard_tot = [
        (30, "2", "15", "3", "5", "2 \\times 3 \\times 5"),
        (42, "2", "21", "3", "7", "2 \\times 3 \\times 7"),
        (45, "5", "9", "3", "3", "3^2 \\times 5"),
        (60, "4", "15", "3", "5", "2^2 \\times 3 \\times 5"),
    ]
    for n, l1, r1, rl, rr, fac_tex in hard_tot:
        ph = _phi(n)
        ans = (n * ph) // 2
        assert ans == sum(k for k in range(1, n + 1) if math.gcd(k, n) == 1)
        B.add_math(
            tp, "Hard", bp,
            f"What is the **sum** of all positive integers less than or equal to {m(n)} that are relatively prime to {m(n)}?",
            f"ما **مجموع** جميع الأعداد الصحيحة الموجبة الأصغر من أو المساوية للعدد {m(n)} والأولية نسبياً معه؟",
            ans, [n * ph, ans - n, ans + ph, (n * (ph + 2)) // 2],
            f"Pair each coprime integer {m('k')} with {m(f'{n} - k')}: since {m(f'\\gcd(k, {n}) = \\gcd({n} - k, {n})')}, every pair sums to {m(n)}!",
            f"زاوج كل عدد أولي نسبياً {m('k')} مع مكمّله {m(f'{n} - k')}؛ مجموع كل زوج يساوي {m(n)}!",
            f"Combine Euler's totient {m(f'\\varphi({n})')} with symmetric pairing {m(f'k \\leftrightarrow {n} - k')}: the coprime sum for {m('n > 2')} is always {m('\\frac{1}{2} n \\varphi(n)')}!",
            [
                f"Factor {m(f'{n} = {fac_tex}')} to find the count of coprime integers: {m(f'\\varphi({n}) = {ph}')}.",
                f"Because {m(f'\\gcd(k, {n}) = \\gcd({n} - k, {n}) = 1')} and {m('k \\neq n - k')} (for {m('n > 2')}), the {m(ph)} coprime integers form {m(ph // 2)} pairs each summing to {m(n)}.",
                f"Multiply: {m(f'\\frac{{{n} \\times {ph}}}{{2}} = {ans}')}.",
            ],
            f"Average check: the {m(ph)} coprime integers are symmetrically distributed around {m(f'{n}/2')}, giving sum {m(f'{ph} \\times ({n}/2) = {ans}')}!",
            f"نجمع بين دالة أويلر {m(f'\\varphi({n})')} والتناظر {m(f'k \\leftrightarrow {n} - k')} فنطبّق الصيغة {m('\\frac{1}{2} n \\varphi(n)')}!",
            [
                f"من التحليل {m(f'{n} = {fac_tex}')} نجد عدد الأعداد الأولية نسبياً: {m(f'\\varphi({n}) = {ph}')}.",
                f"كل عدد {m('k')} أولي نسبياً مع {m(n)} يقابله {m(f'{n} - k')} ومجموعهما {m(n)}، فيتكوّن {m(ph // 2)} زوجاً.",
                f"إذن المجموع الكلي يساوي {m(f'{ph // 2} \\times {n} = {ans}')}.",
            ],
            f"تحقق بالمتوسط الحسابي: متوسط الأعداد المتناظرة هو {m(f'{n}/2')} وعددها {m(ph)} وحاصل ضربهما {m(ans)}.",
            diagram_en=svg_factor_tree(str(n), l1, r1, rl, rr),
        )

    # 2. nsmo_g10_fermat_euler_mod_power (5E, 6M, 4H) — SVG: svg_function_machine
    bp = "nsmo_g10_fermat_euler_mod_power"
    easy_mod = [
        (3, 102, 11, 10),
        (5, 146, 13, 12),
        (2, 203, 17, 16),
        (4, 183, 19, 18),
        (3, 223, 23, 22),
    ]
    for base, exp, modp, cyc in easy_mod:
        rem_e = exp % cyc
        ans = pow(base, exp, modp)
        assert ans == pow(base, rem_e, modp)
        B.add_math(
            tp, "Easy", bp,
            f"Using Fermat's Little Theorem, find the remainder when {m(f'{base}^{{{exp}}}')} is divided by the prime {m(modp)}.",
            f"باستخدام مبرهنة فيرما الصغرى، ما باقي قسمة {m(f'{base}^{{{exp}}}')} على العدد الأولي {m(modp)}؟",
            ans, [1, base, modp - ans, (ans + 2) % modp],
            f"Since {m(modp)} is prime and {m(f'\\gcd({base}, {modp}) = 1')}, {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modp}}}')}.",
            f"بما أن {m(modp)} أولي ولا يقسم {m(base)}، فإن {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modp}}}')}.",
            f"Apply Fermat's Little Theorem {m(f'a^{{p-1}} \\equiv 1 \\pmod{{p}}')} to reduce the exponent modulo {m(cyc)}.",
            [
                f"Because {m(modp)} is prime and {m(f'\\gcd({base}, {modp}) = 1')}, we have {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modp}}}')}.",
                f"Divide the exponent {m(exp)} by {m(cyc)}: {m(f'{exp} = {cyc} \\times {exp // cyc} + {rem_e}')}.",
                f"Thus {m(f'{base}^{{{exp}}} \\equiv {base}^{{{rem_e}}} = {base ** rem_e} \\equiv {ans} \\pmod{{{modp}}}')}.",
            ],
            f"Check: {m(f'{base ** rem_e} = {(base ** rem_e) // modp} \\times {modp} + {ans}')}, leaving remainder {m(ans)}.",
            f"نطبّق مبرهنة فيرما الصغرى لتخفيض الأس بقسمته على {m(f'p - 1 = {cyc}')}.",
            [
                f"بما أن {m(modp)} أولي و{m(f'\\gcd({base}, {modp}) = 1')}، فإن {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modp}}}')}.",
                f"باقي قسمة الأس {m(exp)} على {m(cyc)} هو {m(rem_e)} لأن {m(f'{exp} = {cyc} \\times {exp // cyc} + {rem_e}')}.",
                f"إذن {m(f'{base}^{{{exp}}} \\equiv {base}^{{{rem_e}}} = {base ** rem_e} \\equiv {ans} \\pmod{{{modp}}}')}.",
            ],
            f"تحقق: الباقي محصور بين {m('0')} و{m(modp - 1)} ويساوي {m(ans)} بالضبط.",
            diagram_en=svg_function_machine(f"{base}^{exp}", f"exp mod {cyc}", f"{base}^{rem_e} mod {modp}", "?"),
        )

    med_mod = [
        (3, 251, 16),
        (5, 302, 21),
        (2, 365, 27),
        (3, 483, 35),
        (7, 523, 40),
        (3, 603, 100),
    ]
    for base, exp, modm in med_mod:
        cyc = _phi(modm)
        rem_e = exp % cyc
        ans = pow(base, exp, modm)
        assert math.gcd(base, modm) == 1 and ans == pow(base, rem_e, modm)
        B.add_math(
            tp, "Medium", bp,
            f"What is the remainder when {m(f'{base}^{{{exp}}}')} is divided by {m(modm)}?",
            f"ما باقي قسمة العدد {m(f'{base}^{{{exp}}}')} على {m(modm)}؟",
            ans, [1, (ans + base) % modm, modm - ans, pow(base, (rem_e + 1) % cyc, modm)],
            f"Compute Euler's totient {m(f'\\varphi({modm}) = {cyc}')} and reduce the exponent {m(exp)} modulo {m(cyc)}.",
            f"احسب دالة أويلر {m(f'\\varphi({modm}) = {cyc}')} ثم خذ باقي قسمة الأس {m(exp)} على {m(cyc)}.",
            f"Since {m(f'\\gcd({base}, {modm}) = 1')}, Euler's Theorem gives {m(f'{base}^{{\\varphi({modm})}} = {base}^{{{cyc}}} \\equiv 1 \\pmod{{{modm}}}')}!",
            [
                f"Compute {m(f'\\varphi({modm}) = {cyc}')}; because {m(f'\\gcd({base}, {modm}) = 1')}, {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modm}}}')}.",
                f"Reduce the exponent: {m(f'{exp} = {cyc} \\times {exp // cyc} + {rem_e}')}, so {m(f'{base}^{{{exp}}} \\equiv {base}^{{{rem_e}}} \\pmod{{{modm}}}')}.",
                f"Evaluate {m(f'{base}^{{{rem_e}}} = {base ** rem_e} \\equiv {ans} \\pmod{{{modm}}}')}.",
            ],
            f"Check: {m(f'{base ** rem_e} - {ans} = {base ** rem_e - ans}')}, which is an exact multiple of {m(modm)}!",
            f"بما أن {m(f'\\gcd({base}, {modm}) = 1')} نختزل الأس عبر مبرهنة أويلر {m(f'\\varphi({modm}) = {cyc}')}!",
            [
                f"نحسب {m(f'\\varphi({modm}) = {cyc}')}، فتكون {m(f'{base}^{{{cyc}}} \\equiv 1 \\pmod{{{modm}}}')}.",
                f"باقي قسمة {m(exp)} على {m(cyc)} هو {m(rem_e)}، لذا {m(f'{base}^{{{exp}}} \\equiv {base}^{{{rem_e}}} \\pmod{{{modm}}}')}.",
                f"نحسب {m(f'{base}^{{{rem_e}}} = {base ** rem_e}')} وباقي قسمته على {m(modm)} يساوي {m(ans)}.",
            ],
            f"تحقق: الفرق {m(f'{base ** rem_e} - {ans} = {base ** rem_e - ans}')} يقبل القسمة على {m(modm)} تماماً!",
            diagram_en=svg_function_machine(f"{base}^{exp}", f"φ({modm})={cyc}", f"{base}^{rem_e} mod {modm}", "?"),
        )

    # Hard (4): Combined modular sums & exponent towers a^(b^c) mod p
    hard_mod = [
        # (a, b, c, p): compute a^(b^c) mod p
        (2, 3, 40, 13),
        (5, 2, 50, 17),
        (3, 5, 37, 19),
        (2, 7, 45, 29),
    ]
    for a, b, c, modp in hard_mod:
        pm1 = modp - 1
        top_mod = pow(b, c, pm1)
        ans = pow(a, top_mod, modp)
        B.add_math(
            tp, "Hard", bp,
            f"In a Senior National Olympiad round, evaluate the remainder when the power tower {m(f'{a}^{{({b}^{{{c}}})}}')} is divided by the prime {m(modp)}.",
            f"في جولة الأولمبياد الوطني للمرحلة الثانوية، أوجد باقي قسمة القوة المركبة {m(f'{a}^{{({b}^{{{c}}})}}')} على العدد الأولي {m(modp)}.",
            ans, [1, a, modp - ans, pow(a, (top_mod + 1) % pm1, modp)],
            f"By Fermat's Little Theorem, reduce the upper exponent {m(f'{b}^{{{c}}}')} modulo {m(f'{modp} - 1 = {pm1}')} **not** modulo {m(modp)}!",
            f"بمبرهنة فيرما الصغرى، اخفض الأس العلوي {m(f'{b}^{{{c}}}')} بالنسبة للمقسوم {m(f'{modp} - 1 = {pm1}')} **وليس** {m(modp)}!",
            f"To compute {m(f'{a}^E \\pmod{{{modp}}}')} for prime {m(modp)}, reduce the exponent {m(f'E = {b}^{{{c}}}')} modulo {m(f'p - 1 = {pm1}')} first!",
            [
                f"Since {m(modp)} is prime and {m(f'\\gcd({a}, {modp}) = 1')}, {m(f'{a}^{{{pm1}}} \\equiv 1 \\pmod{{{modp}}}')}.",
                f"Find {m(f'E = {b}^{{{c}}} \\pmod{{{pm1}}}')}: evaluating powers of {m(b)} modulo {m(pm1)} gives {m(f'{b}^{{{c}}} \\equiv {top_mod} \\pmod{{{pm1}}}')}.",
                f"Substitute back into the base: {m(f'{a}^{{({b}^{{{c}}})}} \\equiv {a}^{{{top_mod}}} \\equiv {ans} \\pmod{{{modp}}}')}.",
            ],
            f"Key check: we reduced the exponent mod {m(pm1)} (giving {m(top_mod)}) and the final power mod {m(modp)} (giving {m(ans)}).",
            f"لحساب {m(f'{a}^E \\pmod{{{modp}}}')} نوجد أولاً باقي الأس {m(f'E = {b}^{{{c}}}')} عند القسمة على {m(f'p - 1 = {pm1}')}!",
            [
                f"بمبرهنة فيرما الصغرى: {m(f'{a}^{{{pm1}}} \\equiv 1 \\pmod{{{modp}}}')}.",
                f"نحسب باقي الأس العلوي على {m(pm1)} فنجد {m(f'{b}^{{{c}}} \\equiv {top_mod} \\pmod{{{pm1}}}')}.",
                f"نعوّض بالأس المختزل في الأساس: {m(f'{a}^{{{top_mod}}} \\equiv {ans} \\pmod{{{modp}}}')}.",
            ],
            f"تحقق: انتبه دائماً أن الأس يُختزل معيار {m(pm1)} بينما الناتج النهائي يُحسب معيار {m(modp)}.",
            diagram_en=svg_function_machine(f"{b}^{c}", f"mod {pm1} → {top_mod}", f"{a}^{top_mod} mod {modp}", "?"),
        )

    # 3. nsmo_g10_legendre_prime_valuation (5E, 6M, 4H) — SVG: svg_factor_tree
    bp = "nsmo_g10_legendre_prime_valuation"
    easy_leg = [65, 95, 130, 175, 255]
    for n in easy_leg:
        ans = _vp_fact(n, 5)
        t1, t2, t3 = n // 5, n // 25, n // 125
        assert ans == t1 + t2 + t3
        B.add_math(
            tp, "Easy", bp,
            f"How many trailing zeros appear at the right end of {m(f'{n}!')} when written in base {m('10')}?",
            f"كم صفراً طرفياً يظهر في يمين العدد {m(f'{n}!')} عند كتابته في النظام العشري؟",
            ans, [t1, t1 + t2 - 1, ans + 2, ans - 1],
            f"Trailing zeros come from pairs {m('2 \\times 5')}; count factors of {m('5')} via Legendre's formula {m(f'v_5({n}!)')}.",
            f"الأصفار الطرفية تنتج عن العوامل {m('2 \\times 5')}؛ احسب أس العدد {m('5')} بصيغة ليجاندر {m(f'v_5({n}!)')}.",
            f"Because {m(f'{n}!')} has far more factors of {m('2')} than {m('5')}, the number of trailing zeros equals {m(f'v_5({n}!)')}!",
            [
                f"Apply Legendre's formula for {m('p = 5')}: {m(f'\\lfloor {n}/5 \\rfloor = {t1}')} and {m(f'\\lfloor {n}/25 \\rfloor = {t2}')}.",
                f"Check {m('5^3 = 125')}: {m(f'\\lfloor {n}/125 \\rfloor = {t3}')} (higher powers of {m('5')} exceed {m(n)}).",
                f"Sum the terms: {m(f'{t1} + {t2} + {t3} = {ans}')} trailing zeros.",
            ],
            f"Check: quotient chain {m(f'{n} \\to {t1} \\to {t2} \\to {t3}')} sums to {m(ans)}.",
            f"عدد الأصفار الطرفية في {m(f'{n}!')} يساوي تماماً أعلى أس للعدد {m('5')} يقسم {m(f'{n}!')} أي {m(f'v_5({n}!)')}!",
            [
                f"نطبّق صيغة ليجاندر عند {m('p = 5')}: {m(f'\\lfloor {n}/5 \\rfloor = {t1}')} و{m(f'\\lfloor {n}/25 \\rfloor = {t2}')}.",
                f"وعند {m('125')}: {m(f'\\lfloor {n}/125 \\rfloor = {t3}')} (وقوى {m('5')} الأكبر تتجاوز {m(n)}).",
                f"المجموع: {m(f'{t1} + {t2} + {t3} = {ans}')} صفراً طرفياً.",
            ],
            f"تحقق بسلسلة القسمة الصحيحة على {m('5')}: {m(f'{t1} + {t2} + {t3} = {ans}')}.",
            diagram_en=svg_factor_tree(f"{n}!", "10 = 2×5", f"⌊{n}/5⌋={t1}", f"⌊{n}/25⌋={t2}", f"+{t3}"),
        )

    med_leg = [
        (50, 2), (76, 3), (108, 3), (140, 7), (160, 3), (200, 7),
    ]
    for n, p in med_leg:
        ans = _vp_fact(n, p)
        terms = []
        pw = p
        while pw <= n:
            terms.append(n // pw)
            pw *= p
        assert sum(terms) == ans
        t_sum_str = " + ".join(str(x) for x in terms)
        B.add_math(
            tp, "Medium", bp,
            f"What is the greatest integer {m('k')} such that {m(f'{p}^k')} is a divisor of {m(f'{n}!')}?",
            f"ما أكبر عدد صحيح {m('k')} يجعل {m(f'{p}^k')} قاسماً للعدد {m(f'{n}!')}؟",
            ans, [terms[0], ans - 1, ans + 1, ans + 3],
            f"Sum {m(f'\\lfloor {n} / {p}^m \\rfloor')} for {m('m = 1, 2, \\dots')} until {m(f'{p}^m > {n}')}.",
            f"اجمع الحدود {m(f'\\lfloor {n} / {p}^m \\rfloor')} لقيم {m('m = 1, 2, \\dots')} حتى يصبح {m(f'{p}^m > {n}')}.",
            f"Apply Legendre's prime valuation formula {m(f'v_{{{p}}}({n}!) = \\sum_{{m \\ge 1}} \\lfloor {n}/{p}^m \\rfloor')}.",
            [
                f"Divide {m(n)} repeatedly by powers of the prime {m(p)}: terms are {m(', '.join(str(x) for x in terms))}.",
                f"Higher powers of {m(p)} exceed {m(n)} and contribute {m('0')}.",
                f"Add all floor quotients: {m(f'k = {t_sum_str} = {ans}')}.",
            ],
            f"Repeated integer division of {m(n)} by {m(p)} produces {m(t_sum_str)}, confirming {m(f'k = {ans}')}.",
            f"نطبّق صيغة ليجاندر لحساب أس العامل الأولي {m(p)} في تحليل {m(f'{n}!')}.",
            [
                f"نحسب خوارج القسمة الصحيحة للعدد {m(n)} على قوى {m(p)} المتتالية فنجد: {m(', '.join(str(x) for x in terms))}.",
                f"القوى الأعلى للعدد {m(p)} أكبر من {m(n)} فمساهمتها {m('0')}.",
                f"نجمع القيم: {m(f'k = {t_sum_str} = {ans}')}.",
            ],
            f"تحقق: القسمة الصحيحة المتكررة للعدد {m(n)} على {m(p)} تعطي {m(f'{t_sum_str} = {ans}')}.",
            diagram_en=svg_factor_tree(f"v_{p}({n}!)", f"÷{p}→{terms[0]}", f"÷{p*p}→{terms[1]}", "higher", f"+{sum(terms[2:])}"),
        )

    # Hard (4): Composite base power m^k | n! (12^k, 18^k, 24^k, 45^k)
    hard_leg = [
        (60, 12, 2, 2, 3, 1),   # 12 = 2^2 * 3^1
        (90, 18, 2, 1, 3, 2),   # 18 = 2^1 * 3^2
        (100, 24, 2, 3, 3, 1),  # 24 = 2^3 * 3^1
        (125, 45, 3, 2, 5, 1),  # 45 = 3^2 * 5^1
    ]
    for n, comp, p1, a1, p2, a2 in hard_leg:
        v1 = _vp_fact(n, p1)
        v2 = _vp_fact(n, p2)
        ans = min(v1 // a1, v2 // a2)
        B.add_math(
            tp, "Hard", bp,
            f"Find the largest positive integer {m('k')} such that the composite power {m(f'{comp}^k')} divides {m(f'{n}!')}.",
            f"أوجد أكبر عدد صحيح موجب {m('k')} يجعل القوة المركبة {m(f'{comp}^k')} تقسم المضروب {m(f'{n}!')}.",
            ans, [max(v1 // a1, v2 // a2), v2, ans + 2, ans - 2],
            f"Factor {m(f'{comp} = {p1}^{{{a1}}} \\times {p2}^{{{a2}}}')} and compute {m(f'\\min(\\lfloor v_{{{p1}}}({n}!)/{a1} \\rfloor,\\; \\lfloor v_{{{p2}}}({n}!)/{a2} \\rfloor)')}!",
            f"حلّل {m(f'{comp} = {p1}^{{{a1}}} \\times {p2}^{{{a2}}}')} واحسب القيمة الصغرى بين {m(f'\\lfloor v_{{{p1}}}/{a1} \\rfloor')} و{m(f'\\lfloor v_{{{p2}}}/{a2} \\rfloor')}!",
            f"Legendre's formula applies **only to primes**! Factor {m(f'{comp} = {p1}^{{{a1}}} \\cdot {p2}^{{{a2}}}')} and check which prime supply runs out first.",
            [
                f"Compute {m(f'v_{{{p1}}}({n}!) = {v1}')}, which supports at most {m(f'\\lfloor {v1}/{a1} \\rfloor = {v1 // a1}')} copies of {m(f'{p1}^{{{a1}}}')}.",
                f"Compute {m(f'v_{{{p2}}}({n}!) = {v2}')}, which supports at most {m(f'\\lfloor {v2}/{a2} \\rfloor = {v2 // a2}')} copies of {m(f'{p2}^{{{a2}}}')}.",
                f"The bottleneck is {m(f'k = \\min({v1 // a1}, {v2 // a2}) = {ans}')}.",
            ],
            f"Check: for {m(f'k = {ans + 1}')}, we would ran short of the limiting prime factor, so {m(ans)} is exact!",
            f"صيغة ليجاندر تُطبَّق على **الأعداد الأولية فقط**؛ نحلّل {m(f'{comp} = {p1}^{{{a1}}} \\cdot {p2}^{{{a2}}}')} ونأخذ العامل المحدِّد الأصغر!",
            [
                f"نحسب بصيغة ليجاندر: {m(f'v_{{{p1}}}({n}!) = {v1}')}، ويكفي لتكوين {m(f'\\lfloor {v1}/{a1} \\rfloor = {v1 // a1}')} نسخة من {m(f'{p1}^{{{a1}}}')}.",
                f"ونحسب {m(f'v_{{{p2}}}({n}!) = {v2}')}، ويكفي لتكوين {m(f'\\lfloor {v2}/{a2} \\rfloor = {v2 // a2}')} نسخة من {m(f'{p2}^{{{a2}}}')}.",
                f"القيمة الكبرى الممكنة هي الأصغر بينهما: {m(f'k = \\min({v1 // a1}, {v2 // a2}) = {ans}')}.",
            ],
            f"تحقق: العامل الأولي الأندر يحدّ أعلى أس ممكن للقوة المركبة عند {m(ans)}.",
            diagram_en=svg_factor_tree(str(comp), f"{p1}^{a1}", f"{p2}^{a2}", f"v={v1}", f"v={v2}"),
        )

    # 4. nsmo_g10_frobenius_chicken_mcnugget (5E, 6M, 4H) — 5 with svg_number_strip
    bp = "nsmo_g10_frobenius_chicken_mcnugget"
    easy_frob = [(4, 9), (5, 8), (6, 11), (8, 13), (9, 14)]
    for a, b in easy_frob:
        assert math.gcd(a, b) == 1
        ans = a * b - a - b
        B.add_math(
            tp, "Easy", bp,
            f"A Mawhiba robotics lab packs batteries only in boxes of {m(a)} and boxes of {m(b)}. What is the largest positive integer number of batteries that **cannot** be purchased exactly?",
            f"يوفّر مختبر الروبوتات في موهبة البطاريات في علب سعتها {m(a)} وعلب سعتها {m(b)} فقط. ما أكبر عدد صحيح موجب من البطاريات **لا يمكن** شراؤه بالضبط؟",
            ans, [a * b - a, a * b, (a - 1) * (b - 1) // 2, ans + 1],
            f"Since {m(f'\\gcd({a}, {b}) = 1')}, use the Chicken McNugget formula {m('ab - a - b')}.",
            f"بما أن {m(f'\\gcd({a}, {b}) = 1')}، استخدم صيغة فروبينيوس {m('ab - a - b')}.",
            f"For two coprime box sizes {m(a)} and {m(b)}, the Frobenius number (largest unattainable sum {m('ax + by')} with {m('x, y \\ge 0')}) is {m('ab - a - b')}.",
            [
                f"Check coprimality: {m(f'\\gcd({a}, {b}) = 1')}.",
                f"Compute {m(f'{a} \\times {b} - {a} - {b} = {a * b} - {a + b} = {ans}')}.",
            ],
            f"Check {m(ans + 1)}: every integer from {m(ans + 1)} onward can be formed as {m(f'{a}x + {b}y')} with {m('x, y \\ge 0')}.",
            f"لفئتين أوليتين نسبياً {m(a)} و{m(b)}، أكبر مجموع غير قابل للتكوين بتركيب {m('ax + by')} ({m('x, y \\ge 0')}) هو {m('ab - a - b')}.",
            [
                f"نتحقق من التباين الأولي: {m(f'\\gcd({a}, {b}) = 1')}.",
                f"نعوّض في القانون: {m(f'{a} \\times {b} - {a} - {b} = {a * b} - {a + b} = {ans}')}.",
            ],
            f"تحقق: العدد {m(ans)} مستحيل التكوين، بينما جميع الأعداد الأكبر من {m(ans)} قابلة للتكوين.",
            diagram_en=svg_number_strip([f"{ans} ✗", f"{ans+1} ✓", f"{ans+2} ✓", "···"]),
        )

    med_frob = [(5, 9), (6, 13), (7, 10), (7, 12), (8, 11), (9, 13)]
    for a, b in med_frob:
        assert math.gcd(a, b) == 1
        ans = (a - 1) * (b - 1) // 2
        B.add_math(
            tp, "Medium", bp,
            f"How many **positive integers** cannot be written in the form {m(f'{a}x + {b}y')} for **non-negative** integers {m('x, y \\ge 0')}?",
            f"كم **عدداً صحيحاً موجباً** لا يمكن كتابته على الصورة {m(f'{a}x + {b}y')} حيث {m('x, y \\ge 0')} عددان صحيحان غير سالبين؟",
            ans, [a * b - a - b, (a - 1) * (b - 1), ans + a, ans - 1],
            f"For coprime {m('a, b')}, exact half of the {m('(a - 1)(b - 1)')} grid residues fail: count {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"لعددين أوليين نسبياً {m('a, b')}، عدد الأعداد الموجبة المستحيلة يساوي دائماً {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"Pair {m('k')} with {m('ab - a - b - k')}: exact one member of each complementary pair is attainable, leaving {m('\\frac{(a-1)(b-1)}{2}')} unattainable positive integers!",
            [
                f"Confirm {m(f'\\gcd({a}, {b}) = 1')}.",
                f"Apply Sylvester's count formula: {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a - 1} \\times {b - 1}}}{{2}} = {ans}')}.",
            ],
            f"Sanity check: the largest unattainable integer is {m(a * b - a - b)}, and {m(ans)} is close to half of {m(a * b - a - b + 1)}.",
            f"باستخدام تناظر الأزواج المتكاملة حول {m('ab - a - b')} نجد أن عدد الأعداد الموجبة غير الممكنة هو {m('\\frac{(a-1)(b-1)}{2}')}!",
            [
                f"نتأكد أن {m(f'\\gcd({a}, {b}) = 1')}.",
                f"نطبّق قانون عدد المجاميع المستحيلة: {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a - 1} \\times {b - 1}}}{{2}} = {ans}')}.",
            ],
            f"تحقق: لا تخلط بين أكبر عدد مستحيل ({m(a * b - a - b)}) وبين **عدد** الأعداد المستحيلة ({m(ans)})!",
        )

    # Hard (4): Strictly positive integers x >= 1, y >= 1 -> largest unattainable is a*b! Plus inverse parameter!
    hard_frob_pos = [(5, 12), (7, 9)]
    for a, b in hard_frob_pos:
        ans = a * b
        B.add_math(
            tp, "Hard", bp,
            f"What is the largest positive integer {m('N')} that **cannot** be expressed as {m(f'{a}x + {b}y')} where {m('x')} and {m('y')} are **positive** integers ({m('x \\ge 1,\\; y \\ge 1')})?",
            f"ما أكبر عدد صحيح موجب {m('N')} **لا يمكن** تمثيله بالصورة {m(f'{a}x + {b}y')} حيث {m('x, y')} عددان صحيحان **موجبان تماماً** ({m('x \\ge 1,\\; y \\ge 1')})؟",
            ans, [a * b - a - b, a * b + a + b, a * b - 1, (a + 1) * (b + 1)],
            f"Set {m('x = x\' + 1')} and {m('y = y\' + 1')} with {m('x\', y\' \\ge 0')}: every sum shifts upward by {m(f'{a} + {b}')}!",
            f"ضع {m('x = x\' + 1')} و{m('y = y\' + 1')} مع {m('x\', y\' \\ge 0')} فترتفع جميع المجاميع بمقدار {m(f'{a} + {b}')}!",
            f"Shift variables to reduce {m('x, y \\ge 1')} back to the standard {m('x\', y\' \\ge 0')} Frobenius theorem!",
            [
                f"Write {m('x = x\' + 1')} and {m('y = y\' + 1')} with {m('x\', y\' \\ge 0')}; then {m(f'{a}x + {b}y = ({a} + {b}) + {a}x\' + {b}y\'')}.",
                f"Since {m(f'\\gcd({a}, {b}) = 1')}, the largest unattainable value of {m(f'{a}x\' + {b}y\'')} is {m(f'{a}\\cdot{b} - {a} - {b}')}.",
                f"Adding back the shift {m(f'{a} + {b}')} cancels {m(f'-{a} - {b}')}, leaving {m(f'N = {a} \\times {b} = {ans}')}!",
            ],
            f"Direct check: if {m(f'{a}x + {b}y = {a*b}')} with {m('x, y \\ge 1')}, then {m(f'{a} \\mid y \\implies y \\ge {a} \\implies {b}y \\ge {a*b}')}, leaving {m('x \\le 0')}, impossible!",
            f"نجري الإزاحة {m('x = x\' + 1')} و{m('y = y\' + 1')} لتحويل الشرط {m('x, y \\ge 1')} إلى صورة فروبينيوس القياسية!",
            [
                f"بالتعويض نجد {m(f'{a}x + {b}y = ({a} + {b}) + ({a}x\' + {b}y\')')} مع {m('x\', y\' \\ge 0')}.",
                f"أكبر قيمة مستحيلة للمقدار {m(f'{a}x\' + {b}y\'')} هي {m(f'{a*b} - {a} - {b}')}.",
                f"بإضافة الإزاحة {m(f'{a} + {b}')} تختصر الحدود ليتبقى {m(f'N = {a} \\times {b} = {ans}')} بالضبط!",
            ],
            f"تحقق جبري: لو كان {m(f'{a}x + {b}y = {ans}')} مع {m('x, y \\ge 1')} لوجب أن يقسم {m(a)} العدد {m('y')} أي {m(f'y \\ge {a}')} فيصبح {m('x \\le 0')} تناقض!",
        )

    hard_frob_inv = [(8, 95, 13), (11, 139, 15)]  # a, largest_unattainable = ab-a-b -> (a-1)b - a = L -> b = (L+a)/(a-1)
    # Check: (8-1)*15 - 8 = 97! Let's compute exact L = a*b - a - b!
    for a, b in [(8, 15), (11, 16)]:
        assert math.gcd(a, b) == 1
        L_unatt = a * b - a - b
        cnt_unatt = (a - 1) * (b - 1) // 2
        B.add_math(
            tp, "Hard", bp,
            f"Two coprime token values are {m(a)} and {m('b')}. If the largest positive integer score unattainable from non-negative combinations {m(f'{a}x + by')} is {m(L_unatt)}, how many positive integer scores in total are unattainable?",
            f"فئتان أوليتان نسبياً من النقاط هما {m(a)} و{m('b')}. إذا كان أكبر مجموع صحيح موجب لا يمكن تكوينه بالصورة {m(f'{a}x + by')} ({m('x, y \\ge 0')}) هو {m(L_unatt)}، فكم مجموعاً صحيحاً موجباً إجمالاً لا يمكن تكوينه؟",
            cnt_unatt, [b, cnt_unatt + a - 1, (L_unatt + 1) // 2 + 3, cnt_unatt - 3],
            f"Solve {m(f'{a}b - {a} - b = {L_unatt}')} for {m('b')} first, then compute {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"حل المعادلة {m(f'{a}b - {a} - b = {L_unatt}')} لإيجاد {m('b')} أولاً، ثم احسب {m('\\frac{(a-1)(b-1)}{2}')}!",
            f"Recover the unknown denomination {m('b')} from {m('ab - a - b = (a-1)b - a')}, then apply the count formula!",
            [
                f"From {m(f'{a}b - {a} - b = {L_unatt}')}, we get {m(f'{a - 1}b = {L_unatt + a} \\implies b = {b}')} (and indeed {m(f'\\gcd({a}, {b}) = 1')}).",
                f"Now count unattainable positive integers: {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a - 1} \\times {b - 1}}}{{2}} = {cnt_unatt}')}.",
            ],
            f"Check: {m(f'{a} \\times {b} - {a} - {b} = {L_unatt}')}, and {m(f'({a - 1})({b - 1})/2 = {cnt_unatt}')}.",
            f"نستخرج قيمة {m('b')} من قانون أكبر مجموع مستحيل ثم نعوّض في قانون عدد المجاميع المستحيلة!",
            [
                f"لدينا {m(f'({a} - 1)b - {a} = {L_unatt} \\implies {a - 1}b = {L_unatt + a} \\implies b = {b}')}.",
                f"نتأكد أن {m(f'\\gcd({a}, {b}) = 1')}، ثم نحسب العدد: {m(f'\\frac{{({a}-1)({b}-1)}}{{2}} = {cnt_unatt}')}.",
            ],
            f"تحقق: {m(f'{a} \\times {b} - {a} - {b} = {L_unatt}')} فعلاً!",
        )

    # 5. nsmo_g10_divisors_of_powers_squares (5E, 6M, 4H) — SVG: svg_binary_bulbs
    bp = "nsmo_g10_divisors_of_powers_squares"
    easy_sqdiv = [
        (4, 2, 3, (1, 1, 1, 0, 0)),
        (6, 5, 2, (1, 0, 1, 0, 1)),
        (5, 4, 4, (0, 1, 1, 0, 1)),
        (7, 3, 2, (1, 1, 0, 1, 0)),
        (8, 5, 3, (1, 0, 1, 1, 0)),
    ]
    for e2, e3, e5, bits in easy_sqdiv:
        ans = (e2 // 2 + 1) * (e3 // 2 + 1) * (e5 // 2 + 1)
        tot_d = (e2 + 1) * (e3 + 1) * (e5 + 1)
        B.add_math(
            tp, "Easy", bp,
            f"Let {m(f'N = 2^{{{e2}}} \\times 3^{{{e3}}} \\times 5^{{{e5}}}')}. How many positive divisors of {m('N')} are **perfect squares**?",
            f"ليكن {m(f'N = 2^{{{e2}}} \\times 3^{{{e3}}} \\times 5^{{{e5}}}')}. كم قاسماً موجباً للعدد {m('N')} يمثّل **مربعاً كاملاً**؟",
            ans, [(e2 // 2) * (e3 // 2) * (e5 // 2), ans + 6, tot_d // 2, ans - 3],
            f"A divisor {m('2^x 3^y 5^z')} is a square iff {m('x, y, z')} are **even** (don't forget exponent {m('0')}!).",
            f"يكون القاسم {m('2^x 3^y 5^z')} مربعاً كاملاً إذا وفقط إذا كانت الأسس {m('x, y, z')} **زوجية** (شاملة الأس {m('0')}!).",
            f"Count even exponent choices {m('\\lfloor a / 2 \\rfloor + 1')} independently for each prime factor!",
            [
                f"Even choices for {m('x \\in [0, ' + str(e2) + ']')}: {m(e2 // 2 + 1)} choices ({m('0, 2, \\dots, ' + str(2 * (e2 // 2)))}).",
                f"Even choices for {m('y \\in [0, ' + str(e3) + ']')}: {m(e3 // 2 + 1)} choices; for {m('z \\in [0, ' + str(e5) + ']')}: {m(e5 // 2 + 1)} choices.",
                f"Multiply independent choices: {m(f'{e2 // 2 + 1} \\times {e3 // 2 + 1} \\times {e5 // 2 + 1} = {ans}')}.",
            ],
            f"Check: {m('1 = 2^0 3^0 5^0')} is included because exponent {m('0')} is even!",
            f"نعدّ الخيارات الزوجية للأس في كل عامل أولي بقاعدة {m('\\lfloor a/2 \\rfloor + 1')} ثم نضرب الخيارات!",
            [
                f"عدد الأسس الزوجية لـ {m('2')}: {m(e2 // 2 + 1)} خيارات، ولـ {m('3')}: {m(e3 // 2 + 1)} خيارات، ولـ {m('5')}: {m(e5 // 2 + 1)} خيارات.",
                f"نضرب عدد الخيارات المستقلة: {m(f'{e2 // 2 + 1} \\times {e3 // 2 + 1} \\times {e5 // 2 + 1} = {ans}')}.",
            ],
            f"تحقق: تضمين الأس {m('0')} يضمن احتساب القاسم المربع {m('1')} وجميع المربعات الأخرى.",
            diagram_en=svg_binary_bulbs(bits, (e2, e3, e5, 2, 0)),
        )

    # Medium (6): Perfect-cube divisors of composite powers M^k
    med_div = [
        (60, 3, 6, 3, 3, "2^2 \\times 3 \\times 5"),     # 60^3 = 2^6 3^3 5^3 -> cubes: (3)(2)(2)=12
        (72, 3, 9, 6, 0, "2^3 \\times 3^2"),             # 72^3 = 2^9 3^6 -> cubes: (4)(3)=12? Wait vary answers!
        (36, 4, 8, 8, 0, "2^2 \\times 3^2"),             # 36^4 = 2^8 3^8 -> cubes: (3)(3)=9
        (90, 4, 4, 8, 4, "2 \\times 3^2 \\times 5"),     # 90^4 = 2^4 3^8 5^4 -> cubes: (2)(3)(2)=12 -> let's do 90^5: 2^5 3^10 5^5 -> (2)(4)(2)=16!
        (120, 4, 12, 4, 4, "2^3 \\times 3 \\times 5"),   # 120^4 = 2^12 3^4 5^4 -> cubes: (5)(2)(2)=20
        (180, 5, 10, 10, 5, "2^2 \\times 3^2 \\times 5"),# 180^5 = 2^10 3^10 5^5 -> cubes: (4)(4)(2)=32
    ]
    med_div[3] = (90, 5, 5, 10, 5, "2 \\times 3^2 \\times 5")
    med_div[1] = (48, 3, 12, 3, 0, "2^4 \\times 3")      # 48^3 = 2^12 3^3 -> cubes: (5)(2)=10
    for base_m, pw_k, a2, a3, a5, fac_s in med_div:
        c2, c3, c5 = a2 // 3 + 1, a3 // 3 + 1, (a5 // 3 + 1 if a5 > 0 else 1)
        ans = c2 * c3 * c5
        B.add_math(
            tp, "Medium", bp,
            f"How many positive divisors of {m(f'{base_m}^{{{pw_k}}}')} are **perfect cubes**?",
            f"كم قاسماً موجباً للعدد {m(f'{base_m}^{{{pw_k}}}')} يمثّل **مكعباً كاملاً**؟",
            ans, [ans - 2, ans + 4, (c2 - 1) * max(1, c3 - 1) * max(1, c5 - 1), ans + 6],
            f"Factor {m(f'{base_m} = {fac_s}')}, raise exponents by {m(pw_k)}, and count multiples of {m('3')} from {m('0')} up to each exponent!",
            f"حلّل {m(f'{base_m} = {fac_s}')}، واضرب الأسس في {m(pw_k)}، ثم عدّ مضاعفات {m('3')} لكل أس بدءاً من {m('0')}!",
            f"Expand {m(f'{base_m}^{{{pw_k}}}')} into primes; a divisor is a perfect cube iff every prime exponent is a multiple of {m('3')} ({m('\\lfloor e/3 \\rfloor + 1')} choices).",
            [
                f"Since {m(f'{base_m} = {fac_s}')}, raising to the {m(pw_k)}-th power gives prime exponents {m(f'({a2}, {a3}' + (f', {a5})' if a5 else ')'))}.",
                f"Count multiples of {m('3')} in each range: {m(f'{c2} \\times {c3}' + (f' \\times {c5}' if a5 else '') + f' = {ans}')}.",
            ],
            f"Check: each prime exponent choice {m('0, 3, 6, \\dots')} combines independently into {m(ans)} cube divisors.",
            f"نفكّ {m(f'{base_m}^{{{pw_k}}}')} لعوامله الأولية، ويكون القاسم مكعباً كاملاً إذا كان كل أس من مضاعفات {m('3')}.",
            [
                f"بما أن {m(f'{base_m} = {fac_s}')}، فإن رفع الأساس للأس {m(pw_k)} يعطي الأسس الأولية {m(f'({a2}, {a3}' + (f', {a5})' if a5 else ')'))}.",
                f"نطبّق {m('\\lfloor e/3 \\rfloor + 1')} لكل عامل أولي ونضرب: {m(ans)}.",
            ],
            f"تحقق: احتساب الأس الصفري يضمن وجود المكعب الكامل {m('1^3 = 1')}.",
            diagram_en=svg_binary_bulbs((1, 0, 0, 1, 1), (a2, a3, a5, 3, pw_k)),
        )

    # Hard (4): Inclusion-Exclusion — divisors of N that are a perfect square OR a perfect cube!
    hard_div = [
        (6, 6, 4),   # 2^6 3^6 5^4: sq=(4)(4)(3)=48, cb=(3)(3)(2)=18, 6th=(2)(2)(1)=4 -> 48+18-4 = 62
        (8, 6, 3),   # 2^8 3^6 5^3: sq=(5)(4)(2)=40, cb=(3)(3)(2)=18, 6th=(2)(2)(1)=4 -> 40+18-4 = 54
        (9, 7, 6),   # 2^9 3^7 5^6: sq=(5)(4)(4)=80, cb=(4)(3)(3)=36, 6th=(2)(2)(2)=8 -> 80+36-8 = 108
        (12, 6, 2),  # 2^12 3^6 5^2: sq=(7)(4)(2)=56, cb=(5)(3)(1)=15, 6th=(3)(2)(1)=6 -> 56+15-6 = 65
    ]
    for e2, e3, e5 in hard_div:
        n_sq = (e2 // 2 + 1) * (e3 // 2 + 1) * (e5 // 2 + 1)
        n_cb = (e2 // 3 + 1) * (e3 // 3 + 1) * (e5 // 3 + 1)
        n_6 = (e2 // 6 + 1) * (e3 // 6 + 1) * (e5 // 6 + 1)
        ans = n_sq + n_cb - n_6
        B.add_math(
            tp, "Hard", bp,
            f"Let {m(f'N = 2^{{{e2}}} \\times 3^{{{e3}}} \\times 5^{{{e5}}}')}. How many positive divisors of {m('N')} are a **perfect square** or a **perfect cube** (or both)?",
            f"ليكن {m(f'N = 2^{{{e2}}} \\times 3^{{{e3}}} \\times 5^{{{e5}}}')}. كم قاسماً موجباً للعدد {m('N')} يمثّل **مربعاً كاملاً** أو **مكعباً كاملاً** (أو كليهما)؟",
            ans, [n_sq + n_cb, ans - n_6, n_sq + n_cb - 1, ans + 4],
            f"Use Inclusion-Exclusion! A number is both a square and a cube iff it is a **6th power** (exponents divisible by {m('6')}).",
            f"استخدم التضمين والإقصاء! العدد الذي هو مربع ومكعب معاً يكون **قوة سادسة** (أسسه تقبل القسمة على {m('6')}).",
            f"Count squares + cubes and subtract **6th powers** ({m('\\operatorname{lcm}(2, 3) = 6')}) so numbers like {m('1')} and {m('64')} aren't counted twice!",
            [
                f"Perfect-square divisors: {m(f'({e2//2+1})({e3//2+1})({e5//2+1}) = {n_sq}')}.",
                f"Perfect-cube divisors: {m(f'({e2//3+1})({e3//3+1})({e5//3+1}) = {n_cb}')}.",
                f"Sixth-power divisors (both): {m(f'({e2//6+1})({e3//6+1})({e5//6+1}) = {n_6}')}; by Inclusion-Exclusion, {m(f'{n_sq} + {n_cb} - {n_6} = {ans}')}.",
            ],
            f"Overlap check: forgetting to subtract {m(n_6)} would overcount every 6th-power divisor!",
            f"نطبّق مبدأ التضمين والإقصاء بطرح القوى السادسة لأن {m('\\operatorname{lcm}(2, 3) = 6')}!",
            [
                f"عدد القواسم المربعة: {m(f'({e2//2+1})({e3//2+1})({e5//2+1}) = {n_sq}')}.",
                f"عدد القواسم المكعبة: {m(f'({e2//3+1})({e3//3+1})({e5//3+1}) = {n_cb}')}.",
                f"عدد القوى السادسة المشتركة: {m(f'({e2//6+1})({e3//6+1})({e5//6+1}) = {n_6}')}؛ والمطلوب {m(f'{n_sq} + {n_cb} - {n_6} = {ans}')}.",
            ],
            f"تحقق: طرح {m(n_6)} يمنع تكرار عدّ القواسم التي هي مربعات ومكعبات في آنٍ واحد.",
            diagram_en=svg_binary_bulbs((1, 1, 0, 1, 0), (e2, e3, e5, 2, 3)),
        )



# =============================================================================
# UNIT 3.2 — Olympiad Diophantine Equations, Floor Sums & Prime Bounding (75 Qs)
# =============================================================================
def _add_unit_3_2(B: BankBuilder) -> None:
    tp = "Number Theory"

    # 6. nsmo_g10_nonlinear_diophantine_squares (5E, 6M, 4H) — SVG: svg_area_identity_square
    bp = "nsmo_g10_nonlinear_diophantine_squares"
    easy_dio = [45, 64, 80, 105, 144]
    for N in easy_dio:
        sols = [
            ((u + N // u) // 2, (N // u - u) // 2)
            for u in range(1, math.isqrt(N) + 1)
            if N % u == 0 and u < N // u and (u + N // u) % 2 == 0
        ]
        ans = len(sols)
        assert all(x > 0 and y > 0 and x * x - y * y == N for x, y in sols)
        B.add_math(
            tp, "Easy", bp,
            f"How many ordered pairs of **positive integers** {m('(x, y)')} satisfy {m(f'x^2 - y^2 = {N}')}?",
            f"كم زوجاً مرتباً من **الأعداد الصحيحة الموجبة** {m('(x, y)')} يحقق المعادلة {m(f'x^2 - y^2 = {N}')}؟",
            ans, [ans + 1, ans + 2, max(1, ans - 1), ans * 2],
            f"Factor as {m(f'(x - y)(x + y) = {N}')} with {m('0 < x - y < x + y')} and **same parity**!",
            f"حلّل الطرف الأيسر إلى {m(f'(x - y)(x + y) = {N}')} مع اشتراط {m('0 < x - y < x + y')} وتماثل الزوجية!",
            f"Set {m('u = x - y')} and {m('v = x + y')}: every factor pair {m('uv = ' + str(N))} with {m('1 \\le u < v')} and {m('u \\equiv v \\pmod{2}')} gives a unique positive pair {m('(x, y)')}.",
            [
                f"Factor {m(f'(x - y)(x + y) = {N}')}; we need {m('1 \\le u < v')}, {m(f'uv = {N}')}, and {m('u + v')} even.",
                f"Testing divisor pairs {m('u < \\sqrt{' + str(N) + '}')} of matching parity yields {m(ans)} valid pairs, giving {m('(x, y) \\in \\{' + ', '.join(f'({x},{y})' for x, y in sols) + '\\}')}.",
            ],
            f"Check: for instance, {m(f'{sols[0][0]}^2 - {sols[0][1]}^2 = {sols[0][0]**2} - {sols[0][1]**2} = {N}')}!",
            f"نكتب {m(f'(x - y)(x + y) = {N}')} ونحصي أزواج قواسم {m(N)} المختلفة المتماثلة في الزوجية!",
            [
                f"نضع {m('u = x - y')} و{m('v = x + y')} بحيث {m('1 \\le u < v')} و{m('u \\equiv v \\pmod 2')}.",
                f"بفحص قواسم {m(N)} نجد {m(ans)} أزواج صالحة تعطي الحلول {m('\\{' + ', '.join(f'({x},{y})' for x, y in sols) + '\\}')}.",
            ],
            f"تحقق: {m(f'{sols[0][0]}^2 - {sols[0][1]}^2 = {N}')} وكلا العددين صحيح موجب.",
            diagram_en=svg_area_identity_square("x", "y"),
        )

    # Medium (6): Max x + y or Min x in x^2 - y^2 = N, plus shifted (x + c)^2 - y^2 = N
    med_dio = [
        (96, "min_x"),
        (160, "min_x"),
        (180, "count"),
        (225, "count"),
        (240, "min_x"),
        (315, "count"),
    ]
    for N, mode in med_dio:
        sols = [
            ((u + N // u) // 2, (N // u - u) // 2)
            for u in range(1, math.isqrt(N) + 1)
            if N % u == 0 and u < N // u and (u + N // u) % 2 == 0
        ]
        if mode == "min_x":
            ans = min(x for x, _ in sols)
            best_y = next(y for x, y in sols if x == ans)
            B.add_math(
                tp, "Medium", bp,
                f"Among all pairs of positive integers {m('(x, y)')} satisfying {m(f'x^2 - y^2 = {N}')}, what is the **smallest** possible value of {m('x')}?",
                f"من بين جميع أزواج الأعداد الصحيحة الموجبة {m('(x, y)')} التي تحقق {m(f'x^2 - y^2 = {N}')}، ما **أصغر** قيمة ممكنة للعدد {m('x')}؟",
                ans, [ans - 2, ans + 2, sols[0][0], ans + 4],
                f"Since {m('x = (u + v)/2')} where {m(f'uv = {N}')}, minimize {m('u + v')} by choosing same-parity factors {m('u < v')} as **close together** as possible!",
                f"بما أن {m('x = (u + v)/2')} حيث {m(f'uv = {N}')}، لتصغير {m('x')} اختر أقرب عاملين زوجيين مختلفين لبعضهما!",
                f"Minimize {m('x = (u + v)/2')} by picking the closest valid same-parity factor pair {m('u < v')} of {m(N)}!",
                [
                    f"Write {m(f'(x - y)(x + y) = uv = {N}')} with {m('u < v')} both even (since {m(N)} is divisible by {m('4')}).",
                    f"The closest even factor pair {m('(u, v)')} with {m('u < v')} is {m(f'({ans - best_y}, {ans + best_y})')}.",
                    f"Thus the minimum value of {m('x')} is {m(f'({ans - best_y} + {ans + best_y})/2 = {ans}')} (with {m(f'y = {best_y}')}).",
                ],
                f"Check: {m(f'{ans}^2 - {best_y}^2 = {ans**2} - {best_y**2} = {N}')}, and any closer pair would violate parity or {m('u < v')}.",
                f"لتصغير {m('x = (u+v)/2')} نختار أقرب قاسمين متماثلي الزوجية للعدد {m(N)}!",
                [
                    f"بما أن {m(N)} زوجي، يجب أن يكون العاملان {m('u < v')} زوجيين معاً.",
                    f"أقرب زوج عوامل زوجيين هو {m(f'({ans - best_y}, {ans + best_y})')}، ومنه {m(f'x = {ans}')} و{m(f'y = {best_y}')}.",
                ],
                f"تحقق: {m(f'{ans}^2 - {best_y}^2 = {N}')} فعلاً!",
                diagram_en=svg_area_identity_square("x", "y"),
            )
        else:
            ans = len(sols)
            B.add_math(
                tp, "Medium", bp,
                f"In a Mawhiba senior selection test, find the number of positive integer pairs {m('(x, y)')} such that {m(f'x^2 - y^2 = {N}')}.",
                f"في اختبار ترشيح المرحلة الثانوية لموهبة، أوجد عدد أزواج الأعداد الصحيحة الموجبة {m('(x, y)')} التي تحقق {m(f'x^2 - y^2 = {N}')}.",
                ans, [ans + 2, ans - 2, ans * 2, ans + 4],
                f"Count divisor pairs {m('1 \\le u < v')} of {m(N)} with {m('u \\equiv v \\pmod{2}')} (use prime factorization of {m(N)}!).",
                f"عدّ أزواج قواسم {m(N)} التي تحقق {m('1 \\le u < v')} وتتفق في الزوجية بالاستعانة بالتحليل الأولي!",
                f"Use the divisor-count shortcut! For odd {m('N')}, every factor pair has both factors odd; for {m('4 \\mid N')}, divide by {m('4')} and pair factors of {m('N/4')}.",
                [
                    f"Write {m(f'uv = {N}')} with {m('1 \\le u < v')} and {m('u \\equiv v \\pmod{2}')}.",
                    f"Counting valid factor pairs directly from the prime factorization of {m(N)} gives exact {m(ans)} pairs.",
                ],
                f"Explicit check confirms {m(ans)} positive integer pairs {m('(x, y)')}.",
                f"نستخدم اختصار التحليل الأولي لحساب أزواج القواسم المتماثلة في الزوجية مع {m('u < v')}!",
                [
                    f"إذا كان {m(N)} فردياً فجميع قواسمه فردية، وإذا كان يقبل القسمة على {m('4')} نقسم على {m('4')} ونعدّ أزواج عوامل {m('N/4')}.",
                    f"نستبعد حالة تساوي العاملين إن كان مربعاً كاملاً فنحصل على {m(ans)} أزواج.",
                ],
                f"تحقق: جميع الأزواج الـ {m(ans)} تعطي قيماً صحيحة موجبة لـ {m('x, y')}.",
                diagram_en=svg_area_identity_square("x", "y"),
            )

    # Hard (4): All integer pairs (x, y) in Z^2 (including 0 and negatives!) & completed-square x^2 + 2kx - y^2 = M
    hard_dio_allz = [24, 36, 40, 56]
    for N in hard_dio_allz:
        # Count ALL (x, y) in Z^2 with x^2 - y^2 = N
        z_sols = [
            (x, y)
            for x in range(-N, N + 1)
            for y in range(-N, N + 1)
            if x * x - y * y == N
        ]
        ans = len(z_sols)
        pos_q = N // 4
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered pairs of **integers** {m('(x, y) \\in \\mathbb{Z}^2')} (positive, negative, or zero) satisfy {m(f'x^2 - y^2 = {N}')}?",
            f"كم زوجاً مرتباً من **الأعداد الصحيحة** {m('(x, y) \\in \\mathbb{Z}^2')} (موجبة أو سالبة أو صفراً) يحقق المعادلة {m(f'x^2 - y^2 = {N}')}؟",
            ans, [ans // 4, ans // 2, ans + 2, ans - 2],
            f"Substitute {m('x - y = 2a')} and {m('x + y = 2b')}: every **signed** integer divisor {m('a')} of {m(pos_q)} gives a distinct pair {m('(x, y)')}!",
            f"ضع {m('x - y = 2a')} و{m('x + y = 2b')}؛ كل قاسم صحيح **بإشارته** (موجباً أو سالباً) للعدد {m(pos_q)} يعطي حلاً مستقلاً!",
            f"Because {m('x')} and {m('y')} can be zero or negative, **every** signed even factor pair {m('(2a, 2b)')} with {m(f'ab = {pos_q}')} is valid — no {m('a < b')} restriction!",
            [
                f"Since {m(f'x^2 - y^2 = {N}')} is even, {m('x - y = 2a')} and {m('x + y = 2b')} must both be even integers, giving {m(f'ab = {pos_q}')}.",
                f"Each integer divisor {m('a')} of {m(pos_q)} (positive OR negative!) uniquely determines {m(f'b = {pos_q}/a')}, {m('x = a + b')}, and {m('y = b - a')}.",
                f"The number of positive divisors of {m(pos_q)} is {m(ans // 2)}, so including negative divisors gives {m(f'2 \\times {ans // 2} = {ans}')} integer pairs!",
            ],
            f"Zero-trap check: if {m(pos_q)} is a perfect square ({m('a = b')}), {m('y = 0')} gives {m('(\\pm\\sqrt{' + str(N) + '}, 0)')}, which has {m('2')} pairs (not {m('4')}) — and counting divisors of {m(pos_q)} handles that automatically!",
            f"عند السماح بالأعداد السالبة والصفر، كل قاسم صحيح (موجب أو سالب) للعدد {m(pos_q)} يولّد زوجاً وحيداً {m('(x, y)')}!",
            [
                f"نضع {m('x - y = 2a')} و{m('x + y = 2b')} فنجد {m(f'ab = {pos_q}')}.",
                f"عدد القواسم الموجبة للعدد {m(pos_q)} هو {m(ans // 2)}، ومع القواسم السالبة يصبح العدد الكلي {m(ans)} قاسماً.",
                f"بما أن العلاقة {m('(x, y) = (a+b, b-a)')} تقابل تقابلاً تاماً كل قاسم {m('a')}، فإن عدد الأزواج هو {m(ans)}.",
            ],
            f"تحقق: طريقة عدّ قواسم {m(pos_q)} تعالج تلقائياً حالة {m('y = 0')} عندما يكون {m(N)} مربعاً كاملاً!",
            diagram_en=svg_area_identity_square("x", "y"),
        )

    # 7. nsmo_g10_polynomial_divisibility_n (5E, 6M, 4H)
    bp = "nsmo_g10_polynomial_divisibility_n"
    easy_pdiv = [
        # (c_add, k_den): positive integers n >= 1 for which (n + c_add)/(n + k_den) is an integer -> (n+k) | (c_add - k), n >= 1 -> d > k
        (33, 3),   # R = 30, divisors of 30 > 3: 5, 6, 10, 15, 30 -> 5
        (40, 4),   # R = 36, divisors of 36 > 4: 6, 9, 12, 18, 36 -> 5? Vary answers!
        (50, 2),   # R = 48, divisors of 48 > 2: 3,4,6,8,12,16,24,48 -> 8
        (45, 5),   # R = 40, divisors of 40 > 5: 8,10,20,40 -> 4
        (66, 6),   # R = 60, divisors of 60 > 6: 10,12,15,20,30,60 -> 6
    ]
    easy_pdiv[1] = (30, 2)  # R = 28, divisors of 28 > 2: 4, 7, 14, 28 -> 4; let's use (44, 2): R=42, >2: 3,6,7,14,21,42 -> 6; (65, 2): R=63, >2: 3,7,9,21,63 -> 5; let's pick (74, 2): R=72, >2: 12-2=10!
    easy_pdiv[1] = (74, 2)
    for c_num, k_den in easy_pdiv:
        R = c_num - k_den
        valid_n = [n for n in range(1, R + 1) if (n + c_num) % (n + k_den) == 0]
        ans = len(valid_n)
        B.add_math(
            tp, "Easy", bp,
            f"For how many **positive** integers {m('n \\ge 1')} is the fraction {m(f'\\frac{{n + {c_num}}}{{n + {k_den}}}')} an integer?",
            f"كم عدداً صحيحاً **موجباً** {m('n \\ge 1')} يجعل الكسر {m(f'\\frac{{n + {c_num}}}{{n + {k_den}}}')} عدداً صحيحاً؟",
            ans, [ans + 2, ans + 1, ans - 1, ans * 2],
            f"Rewrite {m(f'\\frac{{n + {c_num}}}{{n + {k_den}}} = 1 + \\frac{{{R}}}{{n + {k_den}}}')} and remember {m(f'n \\ge 1 \\implies n + {k_den} > {k_den}')}!",
            f"اكتب الكسر بصورة {m(f'1 + \\frac{{{R}}}{{n + {k_den}}}')} وتذكّر أن {m(f'n \\ge 1')} يعني {m(f'n + {k_den} > {k_den}')}!",
            f"Isolate the constant remainder {m(R)}, then count divisors of {m(R)} strictly greater than {m(k_den)}!",
            [
                f"Split the numerator: {m(f'\\frac{{(n + {k_den}) + {R}}}{{n + {k_den}}} = 1 + \\frac{{{R}}}{{n + {k_den}}}')}.",
                f"Thus {m(f'n + {k_den}')} must be a positive divisor of {m(R)} satisfying {m(f'n + {k_den} \\ge {k_den + 1}')}.",
                f"Counting divisors of {m(R)} greater than {m(k_den)} gives exact {m(ans)} positive integers {m('n')}.",
            ],
            f"Boundary check: small divisors {m(f'\\le {k_den}')} would make {m('n \\le 0')}, so excluding them leaves {m(ans)}.",
            f"نعزل الباقي الثابت {m(R)} ثم نعدّ قواسم {m(R)} الأكبر تماماً من {m(k_den)}!",
            [
                f"نكتب الكسر على الصورة {m(f'1 + \\frac{{{R}}}{{n + {k_den}}}')}.",
                f"بما أن {m('n \\ge 1')}، يجب أن يكون {m(f'n + {k_den}')} قاسماً للعدد {m(R)} وأكبر من {m(k_den)}.",
                f"بإحصاء القواسم الأكبر من {m(k_den)} للعدد {m(R)} نجد {m(ans)} قيم موجبة للعدد {m('n')}.",
            ],
            f"تحقق: استبعاد القواسم الصغيرة {m(f'\\le {k_den}')} ضروري لأنها تعطي {m('n \\le 0')}.",
        )

    # Medium (6): All integers n in Z for quadratic (n^2 + b n + c) / (n + k)
    med_pdiv = [
        (3, 22, 1),   # R = 1 - 3 + 22 = 20 -> 6*2 = 12 -> vary R!
        (7, 30, 3),   # R = 9 - 21 + 30 = 18 -> 6*2 = 12 -> let's pick distinct divisor counts!
        (4, 29, 2),   # R = 4 - 8 + 29 = 25 -> 3*2 = 6
        (6, 33, 3),   # R = 9 - 18 + 33 = 24 -> 8*2 = 16
        (5, 34, 2),   # R = 4 - 10 + 34 = 28 -> 6*2 = 12
        (8, 46, 3),   # R = 9 - 24 + 46 = 31? Wait: 9 - 24 + 51 = 36 -> 9*2 = 18!
    ]
    med_pdiv = [
        (3, 18, 2),   # R = 4 - 6 + 18 = 16 -> 5*2 = 10
        (4, 29, 2),   # R = 4 - 8 + 29 = 25 -> 3*2 = 6
        (6, 33, 3),   # R = 9 - 18 + 33 = 24 -> 8*2 = 16
        (5, 36, 3),   # R = 9 - 15 + 36 = 30 -> 8*2 = 16 -> let's make R = 20 -> 12: (5, 26, 2) -> 4-10+26=20 -> 12? Avoid 12 (worked ex)! Use (5, 38, 2) -> 4-10+38 = 32 -> 6*2=12? 32 has 6 pos -> 12. Use R=40 -> 8*2=16; R=36 -> 9*2=18: (8, 51, 3) -> 9-24+51 = 36 -> 18!
        (8, 51, 3),   # R = 36 -> 18
        (7, 40, 4),   # R = 16 - 28 + 40 = 28 -> 12 -> use (7, 52, 4) -> 16-28+52 = 40 -> 16 -> use (7, 57, 4) -> 16-28+57 = 45 -> 6*2=12 -> use (7, 60, 4) -> 48 -> 10*2 = 20!
        (9, 76, 4),   # R = 16 - 36 + 76 = 56 -> 8*2 = 16 -> use (9, 80, 4) -> 60 -> 12*2 = 24!
    ]
    med_pdiv = [
        (3, 18, 2),   # R = 16 -> 10
        (4, 29, 2),   # R = 25 -> 6
        (6, 33, 3),   # R = 24 -> 16
        (8, 51, 3),   # R = 36 -> 18
        (7, 60, 4),   # R = 48 -> 20
        (9, 80, 4),   # R = 60 -> 24
    ]
    for b_c, c_c, k_d in med_pdiv:
        R = k_d * k_d - b_c * k_d + c_c
        valid_z = [
            n for n in range(-abs(R) - 20, abs(R) + 20)
            if n != -k_d and (n * n + b_c * n + c_c) % (n + k_d) == 0
        ]
        ans = len(valid_z)
        B.add_math(
            tp, "Medium", bp,
            f"For how many **integers** {m('n \\in \\mathbb{Z}')} is {m(f'\\frac{{n^2 + {b_c}n + {c_c}}}{{n + {k_d}}}')} an integer?",
            f"كم **عدداً صحيحاً** {m('n \\in \\mathbb{Z}')} يجعل المقدار الكسري {m(f'\\frac{{n^2 + {b_c}n + {c_c}}}{{n + {k_d}}}')} عدداً صحيحاً؟",
            ans, [ans // 2, ans - 2, ans + 2, ans + 4],
            f"Plug {m(f'n = -{k_d}')} into the numerator to find the constant remainder {m(f'R = {R}')}, and count **both positive and negative** divisors!",
            f"عوّض بـ {m(f'n = -{k_d}')} في البسط لإيجاد الباقي الثابت {m(f'R = {R}')}، وعدّ القواسم **الموجبة والسالبة معاً**!",
            f"Use the Polynomial Remainder Theorem: {m(f'(n + {k_d})')} divides {m(f'n^2 + {b_c}n + {c_c}')} iff {m(f'(n + {k_d})')} divides {m(f'P(-{k_d}) = {R}')}.",
            [
                f"Evaluate the remainder at {m(f'n = -{k_d}')}: {m(f'R = (-{k_d})^2 + {b_c}(-{k_d}) + {c_c} = {R}')}.",
                f"Thus {m(f'n + {k_d}')} can equal any non-zero integer divisor (positive or negative) of {m(R)}.",
                f"Since {m(R)} has {m(ans // 2)} positive divisors, it has {m(f'2 \\times {ans // 2} = {ans}')} total integer divisors, giving {m(ans)} integers {m('n')}.",
            ],
            f"Symmetry check: every positive divisor {m('d')} pairs with {m('-d')}, doubling {m(ans // 2)} to {m(ans)}.",
            f"بتطبيق مبرهنة الباقي، يقبل البسط القسمة على {m(f'(n + {k_d})')} إذا وفقط إذا قسم {m(f'(n + {k_d})')} الباقي الثابت {m(f'R = {R}')}.",
            [
                f"نحسب الباقي عند {m(f'n = -{k_d}')}: {m(f'R = (-{k_d})^2 + {b_c}(-{k_d}) + {c_c} = {R}')}.",
                f"عدد القواسم الموجبة للعدد {m(R)} هو {m(ans // 2)} قاسماً.",
                f"باحتساب القواسم الموجبة والسالبة معاً نحصل على {m(f'2 \\times {ans // 2} = {ans}')} قيمة صحيحة لـ {m('n')}.",
            ],
            f"تحقق: لا تنسَ القواسم السالبة لأن السؤال طلب جميع الأعداد الصحيحة {m('n \\in \\mathbb{Z}')}!",
        )

    # Hard (4): Largest integer n OR sum of all valid integers n for cubic divisibility
    hard_pdiv = [
        # (b, c, d, k, ask_mode): (n^3 + b n^2 + c n + d) / (n + k)
        (2, 5, 36, 2, "max"),   # R = -8 + 8 - 10 + 36 = 26 -> max n = 26 - 2 = 24
        (4, 3, 45, 3, "max"),   # R = -27 + 36 - 9 + 45 = 45 -> max n = 45 - 3 = 42
        (3, 4, 28, 2, "sum_pos_d"), # sum of ALL integers n: each pair (+d, -d) gives (-2k), R = -8+12-8+28 = 24 (16 divs -> sum = -32 -> ask |sum| or shift n - k! Wait: for (n - k) in denominator, pair (+d, -d) gives +2k > 0! Let's use denominator (n - k)!)
        (2, 1, 50, 3, "sum_minus"),
    ]
    for b_c, c_c, d_c, k_d, mode in hard_pdiv:
        if mode == "max":
            R = (-k_d) ** 3 + b_c * (k_d ** 2) - c_c * k_d + d_c
            valid_z = [
                n for n in range(-abs(R) - 20, abs(R) + 20)
                if n != -k_d and (n ** 3 + b_c * n * n + c_c * n + d_c) % (n + k_d) == 0
            ]
            ans = max(valid_z)
            assert ans == R - k_d
            B.add_math(
                tp, "Hard", bp,
                f"What is the **greatest** integer {m('n')} for which {m(f'\\frac{{n^3 + {b_c}n^2 + {c_c}n + {d_c}}}{{n + {k_d}}}')} is an integer?",
                f"ما **أكبر** عدد صحيح {m('n')} يجعل المقدار {m(f'\\frac{{n^3 + {b_c}n^2 + {c_c}n + {d_c}}}{{n + {k_d}}}')} عدداً صحيحاً؟",
                ans, [R, R + k_d, ans - k_d, R // 2 - k_d],
                f"Find the constant remainder {m(f'R = P(-{k_d})')}; the largest possible divisor of {m('|R|')} is {m('|R|')} itself!",
                f"احسب الباقي الثابت {m(f'R = P(-{k_d})')}؛ أكبر قاسم ممكن للعدد {m('|R|')} هو {m('|R|')} نفسه!",
                f"Isolate the cubic remainder {m(f'R = P(-{k_d})')} and set {m(f'n + {k_d} = |R|')} to maximize {m('n')}.",
                [
                    f"Substitute {m(f'n = -{k_d}')} into the cubic numerator: {m(f'R = (-{k_d})^3 + {b_c}(-{k_d})^2 + {c_c}(-{k_d}) + {d_c} = {R}')}.",
                    f"For the fraction to be an integer, {m(f'n + {k_d}')} must divide {m(R)}.",
                    f"The maximum divisor of {m(R)} is {m(R)}, giving {m(f'n + {k_d} = {R} \\implies n = {ans}')}.",
                ],
                f"Check: for any {m(f'n > {ans}')}, {m(f'0 < \\frac{{{R}}}{{n + {k_d}}} < 1')}, which can never be an integer!",
                f"نعوّض بـ {m(f'n = -{k_d}')} لإيجاد الباقي {m('R')}، ثم نساوي المقام بأكبر قاسم لـ {m('R')}!",
                [
                    f"قيمة الباقي هي {m(f'R = (-{k_d})^3 + {b_c}(-{k_d})^2 + {c_c}(-{k_d}) + {d_c} = {R}')}.",
                    f"أكبر قاسم للعدد {m(R)} هو {m(R)} نفسه.",
                    f"نضع {m(f'n + {k_d} = {R}')} فنحصل على أكبر قيمة صحيحة {m(f'n = {ans}')}.",
                ],
                f"تحقق: لأي عدد {m(f'n > {ans}')} يصبح الكسر المتبقي محصوراً بين {m('0')} و{m('1')} فيستحيل أن يكون صحيحاً!",
            )
        else:
            # Denominator (n - k_d), numerator n^2 - b_c*n + d_c so R = k_d^2 - b_c*k_d + d_c > 0
            R = k_d * k_d - b_c * k_d + d_c
            valid_z = [
                n for n in range(-abs(R) - 20, abs(R) + 20)
                if n != k_d and (n * n - b_c * n + d_c) % (n - k_d) == 0
            ]
            ans = sum(valid_z)
            cnt_d = len(valid_z)
            assert ans == k_d * cnt_d
            B.add_math(
                tp, "Hard", bp,
                f"Find the **sum** of all integers {m('n \\in \\mathbb{Z}')} (positive, negative, or zero) for which {m(f'\\frac{{n^2 - {b_c}n + {d_c}}}{{n - {k_d}}}')} is an integer.",
                f"أوجد **مجموع** جميع الأعداد الصحيحة {m('n \\in \\mathbb{Z}')} التي تجعل الكسر {m(f'\\frac{{n^2 - {b_c}n + {d_c}}}{{n - {k_d}}}')} عدداً صحيحاً.",
                ans, [ans // 2, k_d * (cnt_d // 2), ans + 2 * k_d, R],
                f"Pair opposite divisors {m('n - ' + str(k_d) + ' = +d')} and {m('-d')}: each pair adds to {m(f'({k_d} + d) + ({k_d} - d) = {2 * k_d}')}!",
                f"زاوج كل قاسمين متعاكسين {m('+d')} و{m('-d')} للمقام {m(f'n - {k_d}')}؛ مجموع الزوج يساوي {m(2 * k_d)} دائماً!",
                f"Never list all divisors by hand! Pair {m(f'n - {k_d} = d')} with {m(f'n - {k_d} = -d')} so the {m('d')}'s cancel completely!",
                [
                    f"Evaluate remainder at {m(f'n = {k_d}')}: {m(f'R = {k_d}^2 - {b_c}({k_d}) + {d_c} = {R}')}.",
                    f"The positive integer {m(R)} has {m(cnt_d // 2)} positive divisors {m('d')}, each paired with {m('-d')}.",
                    f"Each pair contributes {m(f'({k_d} + d) + ({k_d} - d) = {2 * k_d}')}, so the total sum is {m(f'{cnt_d // 2} \\times {2 * k_d} = {ans}')}!",
                ],
                f"Average check: the {m(cnt_d)} solutions are symmetric around {m(k_d)}, giving sum {m(f'{cnt_d} \\times {k_d} = {ans}')}!",
                f"نزاوج الحلول المتناظرة {m(f'n = {k_d} + d')} و{m(f'n = {k_d} - d')} فتختفي قيم القواسم ويبقى عددها فقط!",
                [
                    f"الباقي عند {m(f'n = {k_d}')} هو {m(f'R = {k_d}^2 - {b_c}({k_d}) + {d_c} = {R}')}.",
                    f"للعدد {m(R)} بالضبط {m(cnt_d // 2)} قاسماً موجباً، وكل زوج {m('(d, -d)')} يعطي مجموعاً يساوي {m(2 * k_d)}.",
                    f"إذن مجموع جميع قيم {m('n')} هو {m(f'{cnt_d // 2} \\times {2 * k_d} = {ans}')}.",
                ],
                f"تحقق بالتناظر: تتوزع الحلول الـ {m(cnt_d)} بتناظر تام حول المركز {m(k_d)} فمجموعها {m(f'{cnt_d} \\times {k_d} = {ans}')}!",
            )

    # 8. nsmo_g10_floor_sqrt_sum (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g10_floor_sqrt_sum"
    easy_fl = [24, 35, 48, 63, 80]  # M^2 - 1 for M = 5, 6, 7, 8, 9
    for N in easy_fl:
        M = math.isqrt(N + 1)
        ans = sum(math.isqrt(k) for k in range(1, N + 1))
        assert ans == sum(j * (2 * j + 1) for j in range(1, M))
        B.add_math(
            tp, "Easy", bp,
            f"Evaluate the floor sum {m(f'\\sum_{{k=1}}^{{{N}}} \\lfloor \\sqrt{{k}} \\rfloor')}.",
            f"احسب قيمة المجموع {m(f'\\sum_{{k=1}}^{{{N}}} \\lfloor \\sqrt{{k}} \\rfloor')}.",
            ans, [ans - M, ans + M + 1, ans - (2 * M - 1), ans + 10],
            f"Notice {m(f'{N} = {M}^2 - 1')}, so every block {m('[j^2, (j+1)^2 - 1]')} for {m(f'j = 1, \\dots, {M - 1}')} is **complete** with {m('2j + 1')} terms!",
            f"لاحظ أن {m(f'{N} = {M}^2 - 1')}، لذا كل فترة {m('[j^2, (j+1)^2 - 1]')} لقيم {m(f'j = 1, \\dots, {M - 1}')} مكتملة وطولها {m('2j + 1')}!",
            f"Group by perfect-square intervals: for {m('j = 1, \\dots, ' + str(M - 1))}, exact {m('2j + 1')} integers have {m('\\lfloor \\sqrt{k} \\rfloor = j')}.",
            [
                f"Recognize {m(f'{N} = {M}^2 - 1')}, giving {m(M - 1)} complete square blocks.",
                f"Sum {m('j(2j + 1)')} for {m(f'j = 1, \\dots, {M - 1}')}: "
                + m(" + ".join(str(j * (2 * j + 1)) for j in range(1, M)) + f" = {ans}") + ".",
            ],
            f"Closed-form check: {m('\\sum_{j=1}^{m} j(2j+1) = \\frac{m(m+1)(4m+5)}{6}')} gives {m(ans)} for {m(f'm = {M - 1}')}!",
            f"نجمّع الأعداد حسب الفترات بين المربعات الكاملة حيث يظهر كل عدد {m('j')} بعدد {m('2j + 1')} مرة!",
            [
                f"بما أن {m(f'{N} = {M}^2 - 1')} فلدينا {m(M - 1)} فترات مكتملة تماماً.",
                f"نجمع مساهمات الفترات {m('j(2j + 1)')}: " + m(" + ".join(str(j * (2 * j + 1)) for j in range(1, M)) + f" = {ans}") + ".",
            ],
            f"تحقق من عدد الحدود: {m('3 + 5 + \\cdots + ' + str(2 * M - 1) + f' = {N}')} حداً بالضبط.",
            diagram_en=svg_number_strip(["1..3 → 1", "4..8 → 2", "···", f"..{N} → {M-1}"]),
        )

    med_fl = [30, 52, 70, 90, 105, 115]
    for N in med_fl:
        M = math.isqrt(N)
        ans = sum(math.isqrt(k) for k in range(1, N + 1))
        full_part = sum(j * (2 * j + 1) for j in range(1, M))
        tail_cnt = N - M * M + 1
        tail_part = tail_cnt * M
        assert full_part + tail_part == ans
        B.add_math(
            tp, "Medium", bp,
            f"Compute the exact value of {m(f'\\lfloor \\sqrt{{1}} \\rfloor + \\lfloor \\sqrt{{2}} \\rfloor + \\cdots + \\lfloor \\sqrt{{{N}}} \\rfloor')}.",
            f"احسب القيمة الدقيقة للمجموع {m(f'\\lfloor \\sqrt{{1}} \\rfloor + \\lfloor \\sqrt{{2}} \\rfloor + \\cdots + \\lfloor \\sqrt{{{N}}} \\rfloor')}.",
            ans, [ans - M, ans + M, full_part + (tail_cnt - 1) * M, ans + 8],
            f"Sum full blocks up to {m(f'{M}^2 - 1 = {M*M - 1}')}, then add {m(f'{N} - {M*M} + 1 = {tail_cnt}')} copies of {m(M)}!",
            f"اجمع الفترات المكتملة حتى {m(M*M - 1)}، ثم أضف {m(f'{N} - {M*M} + 1 = {tail_cnt}')} حدود قيمة كل منها {m(M)}!",
            f"Split at the largest square {m(f'{M}^2 = {M*M} \\le {N}')}; don't forget the **+1** fencepost count on the final partial block!",
            [
                f"Complete blocks for {m(f'j = 1, \\dots, {M - 1}')} (covering {m(f'1 \\dots {M*M - 1}')}) sum to {m(full_part)}.",
                f"From {m(M * M)} to {m(N)} inclusive, there are {m(f'{N} - {M*M} + 1 = {tail_cnt}')} integers each with {m(f'\\lfloor \\sqrt{{k}} \\rfloor = {M}')}, contributing {m(f'{tail_cnt} \\times {M} = {tail_part}')}.",
                f"Total sum: {m(f'{full_part} + {tail_part} = {ans}')}.",
            ],
            f"Fencepost check: {m(f'({M*M - 1}) + {tail_cnt} = {N}')} total terms summed cleanly!",
            f"نفصل عند أكبر مربع كامل {m(f'{M}^2 = {M*M}')} مع الانتباه لقاعدة العدّ {m(f'{N} - {M*M} + 1')} في الفترة الأخيرة!",
            [
                f"مجموع الفترات المكتملة من {m('1')} حتى {m(M*M - 1)} يساوي {m(full_part)}.",
                f"الفترة المتبقية من {m(M*M)} إلى {m(N)} تضم {m(f'{N} - {M*M} + 1 = {tail_cnt}')} أعداد قيمة كل منها {m(M)}، ومجموعها {m(tail_part)}.",
                f"المجموع النهائي: {m(f'{full_part} + {tail_part} = {ans}')}.",
            ],
            f"تحقق: إغفال {m('+1')} في عدّ الفترة الأخيرة ينقص الناتج بمقدار {m(M)}؛ الناتج الدقيق هو {m(ans)}.",
            diagram_en=svg_number_strip(["1..3 → 1", "···", f"..{M*M-1} → {M-1}", f"{M*M}..{N} → {M}"]),
        )

    # Hard (4): 2 cube-root floor sums + 2 inverse floor-sqrt target equations
    for N_cb in (35, 75):
        # floor(cbrt(k)): 1..7 -> 1 (7 terms), 8..26 -> 2 (19 terms), 27..63 -> 3 (37 terms), 64..124 -> 4
        def _icbrt(x: int) -> int:
            r = int(round(x ** (1 / 3)))
            while (r + 1) ** 3 <= x:
                r += 1
            while r ** 3 > x:
                r -= 1
            return r
        ans = sum(_icbrt(k) for k in range(1, N_cb + 1))
        B.add_math(
            tp, "Hard", bp,
            f"Evaluate the cube-root floor sum {m(f'\\sum_{{k=1}}^{{{N_cb}}} \\lfloor \\sqrt[3]{{k}} \\rfloor')}.",
            f"احسب قيمة مجموع الجذور التكعيبية الصحيحة {m(f'\\sum_{{k=1}}^{{{N_cb}}} \\lfloor \\sqrt[3]{{k}} \\rfloor')}.",
            ans, [ans - 3, ans + 4, ans - 7, ans + 8],
            f"Split at perfect cubes {m('1^3 = 1,\\; 2^3 = 8,\\; 3^3 = 27,\\; 4^3 = 64')}!",
            f"قسّم المجموع عند المكعبات الكاملة {m('1, 8, 27, 64')}!",
            f"Group integers between consecutive perfect cubes {m('m^3')} and {m('(m+1)^3 - 1')}!",
            [
                f"For {m('k \\in [1, 7]')}: {m('7 \\times 1 = 7')}. For {m('k \\in [8, 26]')}: {m('19 \\times 2 = 38')}.",
                (
                    f"For {m('k \\in [27, 35]')}: {m('9 \\times 3 = 27')}, giving {m(f'7 + 38 + 27 = {ans}')}."
                    if N_cb == 35
                    else f"For {m('k \\in [27, 63]')}: {m('37 \\times 3 = 111')}; for {m('k \\in [64, 75]')}: {m('12 \\times 4 = 48')}; sum {m(f'7 + 38 + 111 + 48 = {ans}')}."
                ),
            ],
            f"Term-count check: block lengths sum to exact {m(N_cb)}!",
            f"نجمّع الحدود بين المكعبات الكاملة المتتالية {m('1, 8, 27, 64')}!",
            [
                f"الفترة {m('[1, 7]')} تعطي {m('7 \\times 1 = 7')}، والفترة {m('[8, 26]')} تعطي {m('19 \\times 2 = 38')}.",
                (
                    f"والفترة الأخيرة {m('[27, 35]')} تضم {m('9')} حدود بقيمة {m('3')} أي {m('27')}، فالمجموع {m(ans)}."
                    if N_cb == 35
                    else f"والفترة {m('[27, 63]')} تعطي {m('37 \\times 3 = 111')}، والفترة {m('[64, 75]')} تعطي {m('12 \\times 4 = 48')}، فالمجموع {m(ans)}."
                ),
            ],
            f"تحقق: مجموع أطوال جميع الفترات يساوي {m(N_cb)} حداً تماماً!",
            diagram_en=svg_number_strip(["1..7 → 1", "8..26 → 2", "27.. → 3", f"..{N_cb}"]),
        )

    for N_inv in (44, 60):
        target_s = sum(math.isqrt(k) for k in range(1, N_inv + 1))
        M = math.isqrt(N_inv)
        base_s = sum(math.isqrt(k) for k in range(1, M * M))
        B.add_math(
            tp, "Hard", bp,
            f"Find the positive integer {m('N')} such that {m(f'\\sum_{{k=1}}^{{N}} \\lfloor \\sqrt{{k}} \\rfloor = {target_s}')}.",
            f"أوجد العدد الصحيح الموجب {m('N')} الذي يحقق {m(f'\\sum_{{k=1}}^{{N}} \\lfloor \\sqrt{{k}} \\rfloor = {target_s}')}.",
            N_inv, [N_inv - 1, N_inv + 1, N_inv - 2, N_inv + 2],
            f"Accumulate full square-block sums {m('3, 13, 34, 70, 125, 203, \\dots')} until just below {m(target_s)}, then divide the remainder by {m(M)}!",
            f"اجمع الفترات المربعة المكتملة تباعاً حتى تقترب من {m(target_s)}، ثم اقسم الفرق المتبقي على {m(M)}!",
            f"Since {m('\\lfloor \\sqrt{k} \\rfloor \\ge 1')}, the cumulative sum is strictly increasing — locate which square block contains {m(target_s)}!",
            [
                f"Sum full blocks up to {m(f'{M}^2 - 1 = {M*M - 1}')}: {m(f'\\sum_{{k=1}}^{{{M*M - 1}}} \\lfloor \\sqrt{{k}} \\rfloor = {base_s}')}.",
                f"The remaining sum needed is {m(f'{target_s} - {base_s} = {target_s - base_s}')}, and every term from {m(M*M)} onward contributes {m(M)}.",
                f"We need {m(f'({target_s - base_s}) / {M} = {(target_s - base_s) // M}')} extra terms starting at {m(M*M)}, giving {m(f'N = {M*M - 1} + {(target_s - base_s) // M} = {N_inv}')}.",
            ],
            f"Check: adding {m(N_inv + 1)} would push the sum to {m(target_s + M)}, so {m(f'N = {N_inv}')} is unique!",
            f"بما أن المجموع متزايد قطعاً، نحدد الفترة المربعة التي يقع فيها العدد {m(target_s)}!",
            [
                f"مجموع الفترات المكتملة حتى {m(M*M - 1)} يساوي {m(base_s)}.",
                f"المقدار المتبقي {m(f'{target_s} - {base_s} = {target_s - base_s}')} نقسمه على قيمة الفترة الجديدة {m(M)} فنجد {m((target_s - base_s) // M)} حدود إضافية.",
                f"إذن {m(f'N = {M*M - 1} + {(target_s - base_s) // M} = {N_inv}')}.",
            ],
            f"تحقق: المجموع حتى {m(N_inv)} يساوي {m(target_s)} بالضبط!",
            diagram_en=svg_number_strip([f"1..{M*M-1}", f"sum={base_s}", f"+{target_s-base_s}", "N = ?"]),
        )

    # 9. nsmo_g10_floor_fractional_equation (5E, 6M, 4H)
    bp = "nsmo_g10_floor_fractional_equation"
    # Easy (5): Unique solution to a * floor(x) + b * {x} = Fraction(P, Q) where a != 0, 0 <= {x} < 1 -> wait: if we write a*floor(x) + b*{x} = M (integer!) with b > M_rem? Look: 3*floor(x) + 5*{x} = 14 -> floor(x) = n, 5r = 14 - 3n in [0, 5) -> 14 - 3n in {0,1,2,3,4}: n=4 gives 5r=2 -> r=2/5 -> x = 22/5! Unique!! Let's verify programmatically!
    easy_ff = [
        (3, 5, 14),   # 5r = 14 - 3n in [0, 5) -> n=4, r=2/5 -> x = 22/5
        (4, 7, 25),   # 7r = 25 - 4n in [0, 7) -> n=5 (r=5/7) AND n=6 (r=1/7)! Wait: if we want UNIQUE solution, we need b <= a! When 1 < b <= a, 0 <= C - a*n < b has AT MOST ONE integer n! Let's check: a=5, b=4, C=23 -> 4r = 23 - 5n in [0, 4) -> n=4 gives 3, r=3/4 -> x = 19/4! UNIQUE!
    ]
    easy_ff = [
        (5, 4, 23),   # n=4, 4r=3 -> x = 19/4
        (6, 5, 32),   # n=5, 5r=2 -> x = 27/5
        (7, 4, 30),   # n=4, 4r=2 -> r=1/2 -> x = 9/2
        (8, 5, 43),   # n=5, 5r=3 -> x = 28/5
        (9, 7, 50),   # n=5, 7r=5 -> x = 40/7
    ]
    for a_f, b_f, C_f in easy_ff:
        ns = [n for n in range(-50, 50) if 0 <= C_f - a_f * n < b_f]
        assert len(ns) == 1
        n0 = ns[0]
        r0 = Fraction(C_f - a_f * n0, b_f)
        ans = n0 + r0
        B.add_math(
            tp, "Easy", bp,
            f"Let {m('\\lfloor x \\rfloor')} denote the greatest integer {m('\\le x')} and {m('\\{x\\} = x - \\lfloor x \\rfloor')}. Find the real number {m('x')} satisfying {m(f'{a_f}\\lfloor x \\rfloor + {b_f}\\{{x\\}} = {C_f}')}.",
            f"ليكن {m('\\lfloor x \\rfloor')} الجزء الصحيح للعدد {m('x')} و{m('\\{x\\} = x - \\lfloor x \\rfloor')} جزءه الكسري. أوجد العدد الحقيقي {m('x')} الذي يحقق {m(f'{a_f}\\lfloor x \\rfloor + {b_f}\\{{x\\}} = {C_f}')}.",
            ans, [ans + 1, ans - Fraction(1, b_f), Fraction(C_f, a_f + b_f), n0 + Fraction(1, b_f)],
            f"Write {m('x = n + r')} with {m('n \\in \\mathbb{Z}')} and {m('0 \\le r < 1')}, so {m(f'0 \\le {C_f} - {a_f}n < {b_f}')}!",
            f"ضع {m('x = n + r')} حيث {m('n \\in \\mathbb{Z}')} و{m('0 \\le r < 1')}، فيكون {m(f'0 \\le {C_f} - {a_f}n < {b_f}')}!",
            f"Isolate {m(f'{b_f}\\{{x\\}} = {C_f} - {a_f}n')} and trap it inside {m(f'[0, {b_f})')} to pin down the unique integer {m('n')}!",
            [
                f"Set {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} and {m('r = \\{x\\} \\in [0, 1)')}; then {m(f'{b_f}r = {C_f} - {a_f}n')}.",
                f"Since {m(f'0 \\le {b_f}r < {b_f}')}, we require {m(f'0 \\le {C_f} - {a_f}n < {b_f}')}, which uniquely forces {m(f'n = {n0}')}.",
                f"Then {m(f'r = \\frac{{{C_f - a_f * n0}}}{{{b_f}}} = {r0}')}, giving {m(f'x = {n0} + {r0}')}.",
            ],
            f"Substitute back: {m(f'\\lfloor x \\rfloor = {n0}')}, {m(f'\\{{x\\}} = {r0}')}, and {m(f'{a_f}({n0}) + {b_f}({r0}) = {C_f}')}!",
            f"نعزل الحد الكسري {m(f'{b_f}r = {C_f} - {a_f}n')} ونحصره في الفترة {m(f'[0, {b_f})')} لتحديد قيمة {m('n')} الصحيحة الوحيدة!",
            [
                f"نضع {m('n = \\lfloor x \\rfloor')} و{m('r = \\{x\\}')} حيث {m('0 \\le r < 1')}.",
                f"من المتباينة {m(f'0 \\le {C_f} - {a_f}n < {b_f}')} نجد القيمة الصحيحة الوحيدة {m(f'n = {n0}')}.",
                f"ومنه {m(f'r = {r0}')}، فيكون الحل {m(f'x = {n0} + {r0}')}.",
            ],
            f"تحقق بالتعويض المباشر: {m(f'{a_f}({n0}) + {b_f}({r0}) = {C_f}')}!",
        )

    # Medium (6): Count of real solutions to floor(x) = a * {x} + b -> r = (n - b)/a in [0, 1) -> n in {b, b+1, ..., b+a-1} -> a solutions, OR a * floor(x) + b * {x} = C when b > a!
    med_ff = [
        (3, 14, 41),  # 14r = 41 - 3n in [0, 14) -> 27 < 3n <= 41 -> n in {10,11,12,13} -> 4 solutions? Let's count exact!
        (4, 21, 50),
        (3, 19, 40),
        (5, 28, 73),
        (4, 27, 65),
        (6, 35, 92),
    ]
    for a_f, b_f, C_f in med_ff:
        ns = [n for n in range(-100, 100) if 0 <= C_f - a_f * n < b_f]
        ans = len(ns)
        B.add_math(
            tp, "Medium", bp,
            f"How many real numbers {m('x')} satisfy the equation {m(f'{a_f}\\lfloor x \\rfloor + {b_f}\\{{x\\}} = {C_f}')}?",
            f"كم عدداً حقيقياً {m('x')} يحقق المعادلة {m(f'{a_f}\\lfloor x \\rfloor + {b_f}\\{{x\\}} = {C_f}')}؟",
            ans, [ans - 1, ans + 1, ans + 2, max(1, ans - 2)],
            f"Set {m('x = n + r')} ({m('n \\in \\mathbb{Z},\\; 0 \\le r < 1')}): each integer {m('n')} satisfying {m(f'0 \\le {C_f} - {a_f}n < {b_f}')} gives exact **one** real solution!",
            f"ضع {m('x = n + r')}: كل عدد صحيح {m('n')} يحقق {m(f'0 \\le {C_f} - {a_f}n < {b_f}')} يعطي **حلاً حقيقياً وحيداً**!",
            f"Solve the strict-upper-bound inequality {m(f'{C_f - b_f} < {a_f}n \\le {C_f}')} for integers {m('n')}!",
            [
                f"Write {m(f'{b_f}r = {C_f} - {a_f}n')}. Since {m('0 \\le r < 1')}, we need {m(f'0 \\le {C_f} - {a_f}n < {b_f}')}.",
                f"Rearranging gives {m(f'{C_f - b_f} < {a_f}n \\le {C_f}')} (strict inequality on the left because {m('r < 1')}!).",
                f"The valid integers are {m('n \\in \\{' + ', '.join(str(x) for x in ns) + '\\}')}, giving exact **{m(ans)}** real solutions.",
            ],
            f"Boundary check: {m(f'{a_f}n = {C_f - b_f}')} would give {m('r = 1')}, which is invalid since {m('\\{x\\} < 1')}.",
            f"نحوّل الشرط {m('0 \\le r < 1')} إلى متباينة حاصرة للعدد الصحيح {m('n')}: {m(f'{C_f - b_f} < {a_f}n \\le {C_f}')}!",
            [
                f"من {m(f'{b_f}r = {C_f} - {a_f}n')} مع {m('0 \\le r < 1')} نحصل على {m(f'{C_f - b_f} < {a_f}n \\le {C_f}')}.",
                f"القيم الصحيحة التي تحقق المتباينة هي {m('\\{' + ', '.join(str(x) for x in ns) + '\\}')}.",
                f"كل قيمة صحيحة لـ {m('n')} تحدد كسراً وحيداً {m('r \\in [0, 1)')}، فيكون عدد الحلول **{m(ans)}**.",
            ],
            f"تحقق: المتباينة اليسرى قطعية لأن {m('r')} لا يمكن أن يساوي {m('1')} أبداً!",
        )

    # Hard (4): Nonlinear floor*fractional: floor(x) * {x} + floor(x) = k*x or floor(x)^2 - m*{x} = c -> sum of solutions!
    # Look at: floor(x)^2 = m * {x} + c -> m * r = n^2 - c in [0, m) -> c <= n^2 < c + m!
    hard_ff = [
        (12, 15),  # 15 <= n^2 < 27 -> n^2 in {16, 25} -> n in {-5, -4, 4, 5}! Ask number of real solutions = 4, or sum of positive real solutions! Let's ask sum of positive real solutions or count of all real solutions!
        (20, 8),   # 8 <= n^2 < 28 -> n^2 in {9, 16, 25} -> n in {+-3, +-4, +-5} -> 6 real solutions!
        (30, 20),  # 20 <= n^2 < 50 -> n^2 in {25, 36, 49} -> 6 real solutions -> let's pick distinct counts! (40, 15): 15 <= n^2 < 55 -> {16,25,36,49} -> 8 real solutions!
        (50, 30),  # 30 <= n^2 < 80 -> {36, 49, 64} -> 6 -> use (60, 24): 24 <= n^2 < 84 -> {25,36,49,64,81} -> 10 real solutions!
    ]
    hard_ff = [(12, 15), (20, 8), (40, 15), (60, 24)]
    for m_f, c_f in hard_ff:
        ns = [n for n in range(-100, 100) if c_f <= n * n < c_f + m_f]
        ans = len(ns)
        pos_ns = [n for n in ns if n > 0]
        B.add_math(
            tp, "Hard", bp,
            f"How many real numbers {m('x')} (positive or negative) satisfy {m(f'\\lfloor x \\rfloor^2 - {m_f}\\{{x\\}} = {c_f}')}?",
            f"كم عدداً حقيقياً {m('x')} (موجباً أو سالباً) يحقق المعادلة {m(f'\\lfloor x \\rfloor^2 - {m_f}\\{{x\\}} = {c_f}')}؟",
            ans, [ans // 2, ans + 2, ans - 2, ans + 1],
            f"Isolate {m(f'{m_f}\\{{x\\}} = n^2 - {c_f}')} where {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')}, and don't forget **negative** integers {m('n')}!",
            f"اعزل {m(f'{m_f}\\{{x\\}} = n^2 - {c_f}')} حيث {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')}، ولا تنسَ القيم **السالبة** للعدد {m('n')}!",
            f"Trap {m('n^2')} inside {m(f'[{c_f}, {c_f + m_f})')} and count **both** {m('+n')} and {m('-n')} for each valid square!",
            [
                f"Let {m('n = \\lfloor x \\rfloor \\in \\mathbb{Z}')} and {m('r = \\{x\\} \\in [0, 1)')}. Then {m(f'{m_f}r = n^2 - {c_f}')}.",
                f"Enforcing {m(f'0 \\le n^2 - {c_f} < {m_f}')} gives {m(f'{c_f} \\le n^2 < {c_f + m_f}')}.",
                f"The valid positive integers are {m('n \\in \\{' + ', '.join(str(x) for x in pos_ns) + '\\}')}, and their negatives {m('-n')} also satisfy the exact same inequality on {m('n^2')}, giving {m(f'2 \\times {len(pos_ns)} = {ans}')} real solutions!",
            ],
            f"Negative-root check: for {m(f'n = -{pos_ns[0]}')}, {m(f'r = ({pos_ns[0]**2 - c_f})/{m_f} \\in [0, 1)')}, so {m(f'x = -{pos_ns[0]} + r')} has {m(f'\\lfloor x \\rfloor = -{pos_ns[0]}')} cleanly!",
            f"نحصر {m('n^2')} في الفترة نصف المفتوحة {m(f'[{c_f}, {c_f + m_f})')} ونحتسب الجذرين الموجب والسالب لكل مربع كامل!",
            [
                f"نضع {m('n = \\lfloor x \\rfloor')} و{m('r = \\{x\\}')} فنجد {m(f'{m_f}r = n^2 - {c_f}')}.",
                f"الشرط {m('0 \\le r < 1')} يكافئ {m(f'{c_f} \\le n^2 < {c_f + m_f}')}.",
                f"القيم الموجبة لـ {m('n')} هي {m('\\{' + ', '.join(str(x) for x in pos_ns) + '\\}')}، ومع نظائرها السالبة يكون عدد الحلول الحقيقية {m(f'2 \\times {len(pos_ns)} = {ans}')}!",
            ],
            f"تحقق: الجزء الكسري {m('\\{x\\}')} موجب دائماً حتى للأعداد السالبة، لذا كل قيمة سالبة لـ {m('n')} تعطي حلاً حقيقياً صحيحاً!",
        )

    # 10. nsmo_g10_prime_parity_bounding (5E, 6M, 4H)
    bp = "nsmo_g10_prime_parity_bounding"
    def _is_p(v: int) -> bool:
        return v >= 2 and all(v % d != 0 for d in range(2, math.isqrt(v) + 1))

    # Easy (5): Primes p, q with p^2 + q = N (even N -> one of p, q is 2!)
    easy_pr = [
        (33, 2, 29),   # p^2 + q = 33: if p=2 -> q=29 (prime); if q=2 -> p^2=31 (no). Unique! Ask p + q = 31
        (45, 2, 41),   # p=2 -> q=41; q=2 -> p^2=43 (no). Ask p * q = 82
        (63, 2, 59),   # p=2 -> q=59; q=2 -> p^2=61 (no). Ask q - p = 57
        (77, 2, 73),   # p=2 -> q=73; q=2 -> p^2=75 (no). Ask p + q = 75
        (93, 2, 89),   # p=2 -> q=89; q=2 -> p^2=91 (no). Ask p * q = 178
    ]
    for idx, (N, p_v, q_v) in enumerate(easy_pr):
        assert _is_p(p_v) and _is_p(q_v) and p_v * p_v + q_v == N and not _is_p(math.isqrt(N - 2) if math.isqrt(N - 2)**2 == N - 2 else 0)
        if idx % 2 == 0:
            ans = p_v + q_v
            ask_en, ask_ar = f"What is {m('p + q')}?", f"ما قيمة {m('p + q')}؟"
        else:
            ans = p_v * q_v
            ask_en, ask_ar = f"What is the product {m('pq')}?", f"ما قيمة حاصل الضرب {m('pq')}؟"
        B.add_math(
            tp, "Easy", bp,
            f"Prime numbers {m('p')} and {m('q')} satisfy {m(f'p^2 + q = {N}')}. {ask_en}",
            f"عددان أوليان {m('p')} و{m('q')} يحققان {m(f'p^2 + q = {N}')}. {ask_ar}",
            ans, [ans - 2, ans + 2, N - 2, q_v],
            f"Since {m(N)} is **odd**, one of {m('p^2')} and {m('q')} must be **even** — test {m('p = 2')} and {m('q = 2')}!",
            f"بما أن {m(N)} **فردي**، يجب أن يكون أحد الحدين {m('p^2')} أو {m('q')} **زوجياً** — اختبر {m('p = 2')} و{m('q = 2')}!",
            f"An odd sum {m(f'p^2 + q = {N}')} forces opposite parities, so one of the primes {m('p, q')} must be {m('2')}!",
            [
                f"Test {m('q = 2')}: {m(f'p^2 = {N - 2}')}, which is not a perfect square.",
                f"Test {m('p = 2')}: {m(f'q = {N} - 4 = {q_v}')}, which is prime!",
                f"Therefore {m(f'(p, q) = (2, {q_v})')}, giving {m(ans)}.",
            ],
            f"Check: {m(f'2^2 + {q_v} = 4 + {q_v} = {N}')} and both {m('2')} and {m(q_v)} are prime.",
            f"المجموع الفردي {m(N)} يستلزم اختلاف الزوجية، فيجب أن يكون أحد الأوليين مساوياً للعدد {m('2')}!",
            [
                f"نجرّب {m('q = 2')} فنجد {m(f'p^2 = {N - 2}')} وليس مربعاً كاملاً.",
                f"نجرّب {m('p = 2')} فنجد {m(f'q = {N} - 4 = {q_v}')} وهو عدد أولي!",
                f"إذن الحل الوحيد هو {m(f'(p, q) = (2, {q_v})')} والقيمة المطلوبة تساوي {m(ans)}.",
            ],
            f"تحقق: {m(f'4 + {q_v} = {N}')} وكلا العددين أولي!",
        )

    # Medium (6): Primes p < q with p*q + r = even or p^2 + q^2 = r? Wait: p^2 + q^2 can NEVER be prime > 5 if p=2: 4 + 9 = 13 (prime!), 4 + 25 = 29, 4 + 49 = 53, 4 + 121 = 125 (no), 4 + 169 = 173 (prime!)... Wait: if p^2 + q^2 = r is unspecified which prime r is, there are multiple! Instead, fix pq + r = N with p <= q <= r or p < q and 2p + 3q? No, look: p*q + r = N where N is EVEN? Wait if N is odd, e.g. p^2 + 2q = N? No: p^2 + q*r = N? Better: p < q < r primes with p*q + r = N? Even cleaner: 2-prime equation p^3 + q^2 = N, OR 3-prime equation p + q^2 + r^2 = M (or p*q + q*r = N -> q(p+r) = N!!).
    # WHOA! Look at q(p + r) = N or p(q + r) = N! Factor N cleanly AND parity! Or look at: primes p, q, r satisfy p^2 + q^2 + r^2 = M (distinct from 182!):
    # Let's check M values where p < q < r primes satisfy p^2 + q^2 + r^2 = M UNIQUELY!
    med_pr_m = []
    for r_cand in (7, 11, 17, 19, 23, 29):
        M_val = 4 + 9 + r_cand * r_cand
        # Verify uniqueness across all primes p < q < r!
        triples = [
            (p, q, r)
            for p in range(2, M_val) if _is_p(p) and p * p < M_val
            for q in range(p + 1, M_val) if _is_p(q) and p * p + q * q < M_val
            for r in [math.isqrt(M_val - p * p - q * q)]
            if r > q and _is_p(r) and p * p + q * q + r * r == M_val
        ]
        assert triples == [(2, 3, r_cand)], (r_cand, triples)
        med_pr_m.append((M_val, r_cand))

    for idx, (M_val, r_v) in enumerate(med_pr_m):
        ans = 2 * 3 * r_v if idx % 2 == 1 else (2 + 3 + r_v)
        ask_en = f"What is the product {m('pqr')}?" if idx % 2 == 1 else f"What is the sum {m('p + q + r')}?"
        ask_ar = f"ما قيمة حاصل الضرب {m('pqr')}؟" if idx % 2 == 1 else f"ما قيمة المجموع {m('p + q + r')}؟"
        B.add_math(
            tp, "Medium", bp,
            f"Three distinct prime numbers {m('p < q < r')} satisfy {m(f'p^2 + q^2 + r^2 = {M_val}')}. {ask_en}",
            f"ثلاثة أعداد أولية مختلفة {m('p < q < r')} تحقق {m(f'p^2 + q^2 + r^2 = {M_val}')}. {ask_ar}",
            ans, [ans - 6, ans + 6, r_v + 5, ans + 12],
            f"Use parity (since {m(M_val)} is even) to get {m('p = 2')}, then inspect remainders modulo {m('3')} to get {m('q = 3')}!",
            f"استفد من كون {m(M_val)} زوجياً لإثبات {m('p = 2')}، ثم افحص الباقي على {m('3')} لإثبات {m('q = 3')}!",
            f"Combine Mod {m('2')} and Mod {m('3')} bounding: an even sum of three distinct prime squares forces {m('p = 2')}, and {m(f'{M_val - 4} \\equiv 1 \\pmod{{3}}')} forces {m('q = 3')}!",
            [
                f"Because {m(M_val)} is even and {m('p < q < r')} cannot all be even, exact one prime is even: {m('p = 2')}.",
                f"Then {m(f'q^2 + r^2 = {M_val - 4}')}. Since {m(f'{M_val - 4} \\equiv 1 \\pmod{{3}}')} and any prime {m('> 3')} squares to {m('1 \\pmod{3}')}, one of {m('q, r')} must be {m('3')}, so {m('q = 3')}.",
                f"Thus {m(f'r^2 = {M_val - 13} \\implies r = {r_v}')} (prime), giving {m(ans)}.",
            ],
            f"Check: {m(f'2^2 + 3^2 + {r_v}^2 = 4 + 9 + {r_v*r_v} = {M_val}')}!",
            f"نستخدم الزوجية لتثبيت {m('p = 2')} ثم باقي القسمة على {m('3')} لتثبيت {m('q = 3')} فوراً!",
            [
                f"بما أن {m(M_val)} زوجي والأعداد الأولية مختلفة، فإن أصغرها هو {m('p = 2')}.",
                f"يبقى {m(f'q^2 + r^2 = {M_val - 4} \\equiv 1 \\pmod{{3}}')}، ولو كان {m('q, r > 3')} لكان مجموع مربعيهما {m('2 \\pmod{3}')}؛ إذن {m('q = 3')}.",
                f"ومنه {m(f'r^2 = {M_val - 13} \\implies r = {r_v}')}، والقيمة المطلوبة تساوي {m(ans)}.",
            ],
            f"تحقق: {m(f'4 + 9 + {r_v*r_v} = {M_val}')} والأعداد الثلاثة أولية!",
        )

    # Hard (4): Olympiad prime power / polynomial prime traps!
    # 1) Primes p, q with p^q + q^p = r (prime!) -> one of p, q is 2 -> 2^3 + 3^2 = 17 (unique! For q > 3, 2^q + q^2 mod 3: q odd not 3 -> 2^q = -1 mod 3 and q^2 = 1 mod 3 -> sum = 0 mod 3, divisible by 3 and > 3 so composite!! WHAT A CLASSIC OLYMPIAD PROBLEM!)
    B.add_math(
        tp, "Hard", bp,
        f"Prime numbers {m('p \\le q')} and {m('r')} satisfy {m('p^q + q^p = r')}. What is the value of {m('p + q + r')}?",
        f"أعداد أولية {m('p \\le q')} و{m('r')} تحقق المعادلة {m('p^q + q^p = r')}. ما قيمة {m('p + q + r')}؟",
        22, [17, 20, 24, 31],
        f"Parity forces {m('p = 2')} (since {m('r > 2')} is odd), and then inspect {m('2^q + q^2 \\pmod{3}')} for odd primes {m('q')}!",
        f"الزوجية تفرض {m('p = 2')}، ثم افحص باقي {m('2^q + q^2')} عند القسمة على {m('3')} لأي عدد أولي فردي {m('q')}!",
        f"A classic Olympiad gem! Parity forces {m('p = 2')}, and modulo {m('3')}, {m('2^q + q^2 \\equiv (-1)^q + 1 \\equiv 0 \\pmod{3}')} for every odd prime {m('q \\neq 3')}!",
        [
            f"Since {m('p^q + q^p = r > 2')}, {m('r')} is odd, so one term is even and the other is odd; with {m('p \\le q')}, we must have {m('p = 2')} and {m('q')} odd.",
            f"If {m('q > 3')}, then {m('q')} is odd and {m('3 \\nmid q')}, so {m('2^q \\equiv (-1)^q = -1 \\pmod{3}')} and {m('q^2 \\equiv 1 \\pmod{3}')}, making {m('2^q + q^2')} a multiple of {m('3')} greater than {m('3')} — never prime!",
            f"Hence {m('q = 3')} is the **only** possibility, giving {m('r = 2^3 + 3^2 = 8 + 9 = 17')} (prime) and {m('p + q + r = 2 + 3 + 17 = 22')}.",
        ],
        f"Test {m('q = 5')}: {m('2^5 + 5^2 = 32 + 25 = 57 = 3 \\times 19')} (composite, divisible by {m('3')} as proved!).",
        f"مسألة أولمبية كلاسيكية! الزوجية تحتم {m('p = 2')}، والتطابق معيار {m('3')} يستبعد كل أولي {m('q > 3')}!",
        [
            f"بما أن {m('r > 2')} فردي، يجب أن يكون أحد الحدين زوجياً والآخر فردياً، ومع {m('p \\le q')} نجد {m('p = 2')} و{m('q')} فردي.",
            f"إذا كان {m('q > 3')} فإن {m('2^q \\equiv (-1)^q = -1 \\pmod{3}')} و{m('q^2 \\equiv 1 \\pmod{3}')}، فيقبل المجموع القسمة على {m('3')} ولا يكون أولياً!",
            f"إذن يتعيّن {m('q = 3')} ومنه {m('r = 2^3 + 3^2 = 17')} (أولي)، ويكون {m('p + q + r = 2 + 3 + 17 = 22')}.",
        ],
        f"تحقق عند {m('q = 5')}: {m('32 + 25 = 57 = 3 \\times 19')} مركب كما أثبت البرهان!",
    )

    # 2) Primes p such that p, p^2 + 2, and p^3 + 2 are prime -> p = 3 -> find p^3 + p^2 + 4 = 40 (or sum of the three primes 3 + 11 + 29 = 43!)
    B.add_math(
        tp, "Hard", bp,
        f"A prime {m('p')} has the property that both {m('p^2 + 2')} and {m('p^3 + 2')} are also prime numbers. What is the sum {m('p + (p^2 + 2) + (p^3 + 2)')}?",
        f"عدد أولي {m('p')} يحقق أن كلاً من {m('p^2 + 2')} و{m('p^3 + 2')} عدد أولي أيضاً. ما قيمة المجموع {m('p + (p^2 + 2) + (p^3 + 2)')}؟",
        43, [17, 39, 41, 47],
        f"Check {m('p^2 + 2 \\pmod{3}')} for every prime {m('p \\neq 3')}!",
        f"افحص باقي {m('p^2 + 2')} عند القسمة على {m('3')} لأي عدد أولي {m('p \\neq 3')}!",
        f"For any prime {m('p \\neq 3')}, {m('p^2 \\equiv 1 \\pmod{3}')}, so {m('p^2 + 2 \\equiv 0 \\pmod{3}')} and {m('p^2 + 2 > 3')}, which is composite!",
        [
            f"If {m('p \\neq 3')}, then {m('3 \\nmid p \\implies p^2 \\equiv 1 \\pmod{3} \\implies p^2 + 2 \\equiv 0 \\pmod{3}')}. Since {m('p \\ge 2')}, {m('p^2 + 2 \\ge 6 > 3')}, so it cannot be prime!",
            f"Thus {m('p = 3')} is the unique candidate: check {m('3^2 + 2 = 11')} (prime) and {m('3^3 + 2 = 29')} (prime).",
            f"Sum the three primes: {m('3 + 11 + 29 = 43')}.",
        ],
        f"Check {m('p = 2')}: {m('2^2 + 2 = 6')} (divisible by {m('3')}); {m('p = 5')}: {m('5^2 + 2 = 27')} (divisible by {m('3')})!",
        f"لأي عدد أولي {m('p \\neq 3')} يكون {m('p^2 \\equiv 1 \\pmod{3}')} فيصبح {m('p^2 + 2')} مضاعفاً للعدد {m('3')} وأكبر منه!",
        [
            f"إذا كان {m('p \\neq 3')} فإن {m('p^2 + 2 \\equiv 1 + 2 \\equiv 0 \\pmod{3}')} ومع {m('p^2 + 2 \\ge 6')} يستحيل أن يكون أولياً.",
            f"إذن الخيار الوحيد هو {m('p = 3')}: نتحقق فنجد {m('3^2 + 2 = 11')} (أولي) و{m('3^3 + 2 = 29')} (أولي).",
            f"مجموع الأعداد الأولية الثلاثة: {m('3 + 11 + 29 = 43')}.",
        ],
        f"تحقق: عند {m('p = 3')} القيم {m('3, 11, 29')} كلها أولية ومجموعها {m('43')}.",
    )

    # 3) Primes p, q with p^2 - 2q^2 = 1 -> mod 3: if q != 3, 2q^2 = 2 mod 3 -> p^2 = 3 = 0 mod 3 -> p = 3 -> 9 - 2q^2 = 1 -> q = 2! Unique! Ask p^3 + q^3 = 35
    B.add_math(
        tp, "Hard", bp,
        f"Prime numbers {m('p')} and {m('q')} satisfy Pell's prime equation {m('p^2 - 2q^2 = 1')}. What is the value of {m('p^3 + q^3')}?",
        f"عددان أوليان {m('p')} و{m('q')} يحققان المعادلة {m('p^2 - 2q^2 = 1')}. ما قيمة {m('p^3 + q^3')}؟",
        35, [17, 29, 37, 133],
        f"Reduce {m('p^2 = 2q^2 + 1')} modulo {m('3')}!",
        f"ادرس المعادلة {m('p^2 = 2q^2 + 1')} بأخذ باقي القسمة على {m('3')}!",
        f"Inspect {m('p^2 = 2q^2 + 1 \\pmod{3}')}: if {m('q \\neq 3')}, then {m('2q^2 + 1 \\equiv 2(1) + 1 \\equiv 0 \\pmod{3}')}, forcing {m('p = 3')}!",
        [
            f"Test {m('q = 3')}: {m('p^2 = 2(9) + 1 = 19')}, not a square.",
            f"For any prime {m('q \\neq 3')}, {m('q^2 \\equiv 1 \\pmod{3}')}, so {m('p^2 = 2q^2 + 1 \\equiv 0 \\pmod{3}')}, forcing the prime {m('p')} to equal {m('3')}!",
            f"Substitute {m('p = 3')}: {m('9 - 2q^2 = 1 \\implies q^2 = 4 \\implies q = 2')}, giving {m('p^3 + q^3 = 27 + 8 = 35')}.",
        ],
        f"Check: {m('3^2 - 2(2^2) = 9 - 8 = 1')}, and no larger primes can ever satisfy {m('p^2 - 2q^2 = 1')}!",
        f"بدراسة المعادلة {m('p^2 = 2q^2 + 1')} معيار {m('3')} نثبت أن الحل الأولي الوحيد هو {m('(p, q) = (3, 2)')}!",
        [
            f"إذا كان {m('q = 3')} فإن {m('p^2 = 19')} وهو مستحيل.",
            f"إذا كان {m('q \\neq 3')} فإن {m('q^2 \\equiv 1 \\pmod{3}')} ومنه {m('p^2 \\equiv 2 + 1 \\equiv 0 \\pmod{3}')}، فيتعيّن {m('p = 3')}.",
            f"بالتعويض: {m('9 - 2q^2 = 1 \\implies q = 2')}، وعليه {m('p^3 + q^3 = 27 + 8 = 35')}.",
        ],
        f"تحقق: {m('9 - 8 = 1')} فعلاً وكلا العددين {m('3, 2')} أولي!",
    )

    # 4) Primes p, q, r with p(q + r) = 38 or p^2 + q*r: let's do p^2 + 8^q? Better: primes p, q with p^4 + 4*q^4 prime? No: primes p, q, r with p^2 + q^3 = r and r <= 50? Wait: p=2, q=3 -> 4 + 27 = 31 (prime!); q=2, p=3 -> 9 + 8 = 17 (prime!). What about p^3 + q^3 + 1 = r^2? Look at p, q primes with p^2 + pq + q^2 = r^2 -> impossible for positive integers since (p+q)^2 > p^2+pq+q^2 > p^2! What about primes p, q with p^2 + 3pq + q^2 = square? Look at clean: primes p, q, r satisfy p^2 + 2q^2 = r and p + q + r = 20 -> wait: mod 3! If p != 3 and q != 3, p^2 + 2q^2 = 1 + 2 = 0 mod 3 -> r = 3 impossible since p^2 + 2q^2 >= 12! Let's check p=3 or q=3!!
    # Check p^2 + 2q^2 = r AND 2p^2 + q^2 = s are BOTH prime!!
    # If p != 3 and q != 3: p^2 + 2q^2 = 1 + 2 = 0 mod 3 (>3, composite!).
    # If p = 3 and q != 3: 2p^2 + q^2 = 18 + q^2: wait 18 + 1 = 19! Wait: if p=3, q=2: p^2+2q^2 = 9+8=17 (prime!), 2p^2+q^2 = 18+4=22 (even, composite!). Why? Parity!! r = p^2 + 2q^2 is prime -> p MUST be odd (if p=2, 4+2q^2 is even > 2!). s = 2p^2 + q^2 is prime -> q MUST be odd! And one of p, q is 3! WLOG p = 3, q odd prime: r = 9 + 2q^2, s = 18 + q^2. Wait for q=5: 59 & 43 BOTH prime! So instead fix r + s or fix ONE clean condition: primes p, q satisfy p^2 + 2q^2 = 59? No, even cleaner: primes p, q, r satisfy p^2 + 2q^2 = r and q^2 + 2r^2 is... wait: p + 2q = ? Let's check `p^2 + 6pq + q^2`? No, look at `p(p + 2) + q(q + 2) = 59`? Let's test in mental math:
    # Look at: primes p, q, r satisfy r = p^2 + 2q^2 and p + q = 8 -> (3, 5): 9 + 50 = 59 (prime!); (5, 3): 25 + 18 = 43 (prime!). What if p < q and p + q = 8? Only (3, 5) -> r = 59! Even better without p+q=8:
    # Primes p, q, r satisfy p^3 - q^3 = 19 (or 61 or 91? 5^3 - 2^3 = 117=9*13; 3^3 - 2^3 = 19!). Wait: p^3 - q^3 = 3r for primes p, q, r!!
    # CHECK p^3 - q^3 = 3r for primes p, q, r!!
    # (p - q)(p^2 + pq + q^2) = 3r!
    # Since p^2 + pq + q^2 > 7 > 3 and r is prime, we MUST have p - q = 1 OR p - q = 3!
    # Case 1: p - q = 1 -> p = 3, q = 2 -> 27 - 8 = 19 != 3r!
    # Case 2: p - q = 3 -> since 3 is odd, one of p, q is even -> q = 2, p = 5!!
    # Check q = 2, p = 5: 5^3 - 2^3 = 125 - 8 = 117 = 3 * 39 (39 = 3*13, not prime!).
    # What about p^3 - q^3 = 7r?!
    # (p - q)(p^2 + pq + q^2) = 7r! Since p^2 + pq + q^2 >= 4 + 6 + 9 = 19 > 7:
    # Case 1: p - q = 1 -> p = 3, q = 2 -> 27 - 8 = 19 != 7r.
    # Case 2: p - q = 7 (odd!) -> q = 2, p = 9 (not prime!).
    # What about p^3 + q^3 = 5r?! (p+q)(p^2 - pq + q^2) = 5r: p+q = 5 -> {p,q}={2,3} -> 8+27 = 35 = 5*7 -> r = 7 PRIME!! Check if p^2 - pq + q^2 = 5 is possible: (p-q)^2 + pq = 5 -> pq <= 5 -> {p,q} = {2,2} (4, no) or {2,3} (1 + 6 = 7 != 5)!
    # SO {p, q} = {2, 3}, r = 7 IS THE UNIQUE SOLUTION IN ALL PRIMES TO p^3 + q^3 = 5r!!
    # Let's double check! (p+q)(p^2 - pq + q^2) = 5r. Both factors are positive integers. Since p, q >= 2: p + q >= 4, and p^2 - pq + q^2 >= 4 - 4 + 4 = 4 (for p=q=2: sum is 16 != 5r; for distinct primes >= 2, p^2 - pq + q^2 >= 9 - 6 + 4 = 7 > 5!). Since 5 and r are BOTH PRIME, the two factors > 1 MUST be {5, r}! Since p^2 - pq + q^2 >= 7 (for distinct primes) and = 4 (for p=q=2), the ONLY way one factor equals 5 is p + q = 5 -> {p, q} = {2, 3}, giving r = 7!
    # WHAT A MASTERPIECE OLYMPIAD PROBLEM!
    B.add_math(
        tp, "Hard", bp,
        f"Prime numbers {m('p, q, r')} with {m('p < q')} satisfy {m('p^3 + q^3 = 5r')}. What is the value of {m('p + q + r')}?",
        f"أعداد أولية {m('p, q, r')} حيث {m('p < q')} تحقق المعادلة {m('p^3 + q^3 = 5r')}. ما قيمة {m('p + q + r')}؟",
        12, [10, 14, 15, 17],
        f"Factor {m('p^3 + q^3 = (p + q)(p^2 - pq + q^2) = 5r')} — since {m('5')} and {m('r')} are primes and both factors exceed {m('1')}, match the factors to {m('5')} and {m('r')}!",
        f"حلّل مجموع المكعبين {m('(p + q)(p^2 - pq + q^2) = 5r')}؛ بما أن {m('5')} و{m('r')} أوليان وكلا القوسين أكبر من {m('1')}، طابق العاملين مع {m('5')} و{m('r')}!",
        f"Factor the sum of cubes: because {m('5r')} is a product of two primes, the two factors {m('(p + q)')} and {m('(p^2 - pq + q^2)')} must be {m('5')} and {m('r')}!",
        [
            f"Factor: {m('(p + q)(p^2 - pq + q^2) = 5r')}. Since {m('2 \\le p < q')}, we have {m('p + q \\ge 5')} and {m('p^2 - pq + q^2 = (q - p)^2 + pq \\ge 1 + 6 = 7')}.",
            f"Because {m('5')} and {m('r')} are primes and {m('p^2 - pq + q^2 \\ge 7 > 5')}, the only possibility is {m('p + q = 5')} and {m('p^2 - pq + q^2 = r')}.",
            f"From {m('p < q')} primes with {m('p + q = 5')}, we get {m('p = 2,\\; q = 3')}, so {m('r = 4 - 6 + 9 = 7')} (prime) and {m('p + q + r = 2 + 3 + 7 = 12')}.",
        ],
        f"Check: {m('2^3 + 3^3 = 8 + 27 = 35 = 5 \\times 7')}, and {m('2, 3, 7')} are all prime!",
        f"نحلّل مجموع المكعبين ونستفيد من كون الطرف الأيمن {m('5r')} حاصل ضرب عددين أوليين!",
        [
            f"لدينا {m('(p + q)(p^2 - pq + q^2) = 5r')}. وبما أن {m('2 \\le p < q')} فإن {m('p + q \\ge 5')} و{m('p^2 - pq + q^2 = (q-p)^2 + pq \\ge 7')}.",
            f"بما أن العاملين أكبر من {m('1')} وضربهما يساوي حاصل ضرب الأوليين {m('5')} و{m('r')}، يتعيّن أن يكون {m('p + q = 5')} و{m('p^2 - pq + q^2 = r')}.",
            f"إذن {m('p = 2,\\; q = 3')} ومنه {m('r = 7')} (أولي)، ويكون {m('p + q + r = 2 + 3 + 7 = 12')}.",
        ],
        f"تحقق: {m('8 + 27 = 35 = 5 \\times 7')} فعلاً!",
    )



# =============================================================================
# UNIT 3.3 — Polynomial Remainder Theorem, Cubic Identities & Nested Radicals (75 Qs)
# =============================================================================
def _add_unit_3_3(B: BankBuilder) -> None:
    tp = "Algebra"

    # 11. nsmo_g10_polynomial_linear_remainder (5E, 6M, 4H) — SVG: svg_parabola_roots
    bp = "nsmo_g10_polynomial_linear_remainder"
    easy_rem = [
        # (r1, v1, r2, v2, x_eval) -> R(x) = a*x + b
        (1, 7, 4, 16, 6),    # a = 3, b = 4 -> R(6) = 22
        (-1, 2, 2, 14, 5),   # a = 4, b = 6 -> R(5) = 26
        (2, 5, 5, 20, 0),    # a = 5, b = -5 -> R(0) = -5? Keep positive or clean: (2, 11, 5, 20, 0) -> a=3, b=5 -> R(0)=5
        (-2, 1, 3, 16, 4),   # a = 3, b = 7 -> R(4) = 19
        (1, 9, 5, 25, 7),    # a = 4, b = 5 -> R(7) = 33
    ]
    easy_rem[2] = (2, 11, 5, 20, 0)
    for r1, v1, r2, v2, x0 in easy_rem:
        a = (v2 - v1) // (r2 - r1)
        b = v1 - a * r1
        assert a * r1 + b == v1 and a * r2 + b == v2
        ans = a * x0 + b
        B.add_math(
            tp, "Easy", bp,
            f"A polynomial {m('P(x)')} satisfies {m(f'P({r1}) = {v1}')} and {m(f'P({r2}) = {v2}')}. If {m('R(x)')} is the remainder when {m('P(x)')} is divided by {m(f'(x - ({r1}))(x - {r2})' if r1 < 0 else f'(x - {r1})(x - {r2})')}, what is {m(f'R({x0})')}?",
            f"كثيرة حدود {m('P(x)')} تحقق {m(f'P({r1}) = {v1}')} و{m(f'P({r2}) = {v2}')}. إذا كان {m('R(x)')} هو باقي قسمة {m('P(x)')} على {m(f'(x + {-r1})(x - {r2})' if r1 < 0 else f'(x - {r1})(x - {r2})')}، فما قيمة {m(f'R({x0})')}؟",
            ans, [ans - a, ans + a, a + b, v1 + v2],
            f"Write the remainder as {m('R(x) = ax + b')} and solve {m(f'R({r1}) = {v1}')}, {m(f'R({r2}) = {v2}')}.",
            f"اكتب الباقي بصورة خطية {m('R(x) = ax + b')} وحل المعادلتين {m(f'R({r1}) = {v1}')} و{m(f'R({r2}) = {v2}')}.",
            f"Dividing by a quadratic leaves a linear remainder {m('R(x) = ax + b')} matching {m('P(x)')} at both roots!",
            [
                f"Set {m('R(x) = ax + b')}; then {m(f'{r1}a + b = {v1}')} and {m(f'{r2}a + b = {v2}')}.",
                f"Slope {m(f'a = \\frac{{{v2} - {v1}}}{{{r2} - ({r1})}} = {a}')}, and intercept {m(f'b = {v1} - {a}({r1}) = {b}')}.",
                f"Evaluate {m(f'R({x0}) = {a}({x0}) + {b} = {ans}')}.",
            ],
            f"Check: {m(f'R({r1}) = {a*r1 + b} = {v1}')} and {m(f'R({r2}) = {a*r2 + b} = {v2}')}.",
            f"القسمة على مقسوم تربيعي تعطي باقياً خطياً {m('R(x) = ax + b')} يتفق مع {m('P(x)')} عند الجذرين!",
            [
                f"نفرض {m('R(x) = ax + b')} فنجد {m(f'a = \\frac{{{v2} - {v1}}}{{{r2} - ({r1})}} = {a}')}.",
                f"نعوّض لإيجاد الثابت: {m(f'b = {v1} - {a}({r1}) = {b}')}.",
                f"نحسب القيمة المطلوبة: {m(f'R({x0}) = {a}({x0}) + {b} = {ans}')}.",
            ],
            f"تحقق: الباقي {m(f'R(x) = {a}x + {b}')} يحقق القيمتين المعطاتين بدقة.",
            diagram_en=svg_parabola_roots(str(r1), str(r2), f"R({x0})=?"),
        )

    # Medium (6): High-degree explicit P(x) = x^n + c*x + d divided by x^2 - r^2: find R(2) or a + b = R(1)
    med_rem = [
        # P(x) = x^n + c*x + d divided by (x^2 - r^2): for odd n, x^n mod (x^2 - r^2) is r^(n-1)*x!
        (5, 3, 7, 2, 1),     # P(x) = x^5 + 3x + 7 mod (x^2 - 4): P(2)=45, P(-2)=-31 -> a=19, b=7 -> R(1) = 26
        (7, 2, 5, 2, 1),     # P(x) = x^7 + 2x + 5 mod (x^2 - 4): a = 64+2=66, b = 5 -> R(1) = 71
        (6, 4, 3, 2, 2),     # P(x) = x^6 + 4x + 3 mod (x^2 - 4): P(2)=75, P(-2)=59 -> a=4, b=67 -> R(2)=75? Ask R(1)=71? Vary! Ask R(3) = 79!
        (5, 5, 4, 3, 1),     # P(x) = x^5 + 5x + 4 mod (x^2 - 9): a = 81+5=86, b = 4 -> R(1) = 90
        (8, 3, 2, 2, 1),     # P(x) = x^8 + 3x + 2 mod (x^2 - 4): a = 3, b = 258 -> R(1) = 261
        (9, 7, 11, 1, 3),    # P(x) = x^9 + 7x + 11 mod (x^2 - 1): a = 1+7=8, b = 11 -> R(3) = 35
    ]
    for deg_n, c_lin, d_con, r_val, x_ask in med_rem:
        p_pos = (r_val ** deg_n) + c_lin * r_val + d_con
        p_neg = ((-r_val) ** deg_n) - c_lin * r_val + d_con
        a = (p_pos - p_neg) // (2 * r_val)
        b = (p_pos + p_neg) // 2
        ans = a * x_ask + b
        B.add_math(
            tp, "Medium", bp,
            f"Let {m('R(x)')} be the remainder when {m(f'P(x) = x^{{{deg_n}}} + {c_lin}x + {d_con}')} is divided by {m(f'x^2 - {r_val*r_val}')}. What is the value of {m(f'R({x_ask})')}?",
            f"ليكن {m('R(x)')} باقي قسمة كثيرة الحدود {m(f'P(x) = x^{{{deg_n}}} + {c_lin}x + {d_con}')} على {m(f'x^2 - {r_val*r_val}')}. ما قيمة {m(f'R({x_ask})')}؟",
            ans, [ans - b, ans + r_val, a + d_con, ans - 2 * a],
            f"Factor {m(f'x^2 - {r_val*r_val} = (x - {r_val})(x + {r_val})')} and plug {m(f'x = \\pm {r_val}')} into {m('P(x) = Q(x)(x^2 - ' + str(r_val*r_val) + ') + ax + b')}!",
            f"حلّل المقسوم إلى {m(f'(x - {r_val})(x + {r_val})')} وعوّض بـ {m(f'x = \\pm {r_val}')} لإيجاد {m('a')} و{m('b')}!",
            f"Never do long division of degree {m(deg_n)}! Evaluate {m(f'P({r_val})')} and {m(f'P(-{r_val})')} to solve for {m('R(x) = ax + b')} in two lines.",
            [
                f"Evaluate at the divisor's roots: {m(f'P({r_val}) = {p_pos}')} and {m(f'P(-{r_val}) = {p_neg}')}.",
                f"From {m(f'{r_val}a + b = {p_pos}')} and {m(f'-{r_val}a + b = {p_neg}')}, adding and subtracting give {m(f'b = {b}')} and {m(f'a = {a}')}.",
                f"Thus {m(f'R(x) = {a}x + {b}')}, so {m(f'R({x_ask}) = {a}({x_ask}) + {b} = {ans}')}.",
            ],
            f"Parity shortcut check: under {m(f'x^2 \\equiv {r_val*r_val}')}, even powers become constants and odd powers become multiples of {m('x')}, giving {m(f'R(x) = {a}x + {b}')}!",
            f"بدل القسمة المطولة من الدرجة {m(deg_n)}، نعوّض بجذرَي المقسوم {m(f'x = \\pm {r_val}')} مباشرة!",
            [
                f"نحسب {m(f'P({r_val}) = {p_pos}')} و{m(f'P(-{r_val}) = {p_neg}')}.",
                f"من النظام {m(f'\\pm {r_val}a + b')} نجد بالجمع والطرح أن {m(f'b = {b}')} و{m(f'a = {a}')}.",
                f"إذن {m(f'R({x_ask}) = {a}({x_ask}) + {b} = {ans}')}.",
            ],
            f"تحقق: استبدال كل {m('x^2')} بالعدد {m(r_val*r_val)} يعطي نفس الباقي الخطي {m(f'{a}x + {b}')} فوراً!",
            diagram_en=svg_parabola_roots(f"−{r_val}", f"+{r_val}", f"R({x_ask})=?"),
        )

    # Hard (4): Quadratic remainder R(x) modulo (x - 1)(x - 2)(x - 3) given P(1), P(2), P(3) -> evaluate R(4) or R(5)!
    # Notice finite-difference magic: for quadratic R(x), R(4) = P(1) - 3 P(2) + 3 P(3)! Let's verify via exact quadratic interpolation!
    hard_rem = [
        (2, 5, 12, 4),    # P(1)=2, P(2)=5, P(3)=12 -> R(x) = 2x^2 - 3x + 3 -> R(4) = 32 - 12 + 3 = 23 (check 2 - 15 + 36 = 23!)
        (3, 4, 9, 5),     # P(1)=3, P(2)=4, P(3)=9 -> R(x) = 2x^2 - 5x + 6 -> R(5) = 50 - 25 + 6 = 31
        (1, 6, 17, 4),    # P(1)=1, P(2)=6, P(3)=17 -> R(x) = 3x^2 - 4x + 2 -> R(4) = 48 - 16 + 2 = 34
        (5, 8, 17, 5),    # P(1)=5, P(2)=8, P(3)=17 -> R(x) = 3x^2 - 6x + 8 -> R(5) = 75 - 30 + 8 = 53
    ]
    for p1, p2, p3, x_ask in hard_rem:
        # R(x) = A x^2 + B x + C through (1,p1), (2,p2), (3,p3): 2A = p3 - 2*p2 + p1
        A_q = (p3 - 2 * p2 + p1) // 2
        B_q = (p2 - p1) - 3 * A_q
        C_q = p1 - A_q - B_q
        assert A_q + B_q + C_q == p1 and 4 * A_q + 2 * B_q + C_q == p2 and 9 * A_q + 3 * B_q + C_q == p3
        ans = A_q * x_ask * x_ask + B_q * x_ask + C_q
        B.add_math(
            tp, "Hard", bp,
            f"A polynomial {m('P(x)')} leaves remainders {m(p1)}, {m(p2)}, and {m(p3)} when divided by {m('x - 1')}, {m('x - 2')}, and {m('x - 3')}, respectively. If {m('R(x)')} is the remainder when {m('P(x)')} is divided by {m('(x - 1)(x - 2)(x - 3)')}, find {m(f'R({x_ask})')}.",
            f"تترك كثيرة الحدود {m('P(x)')} البواقي {m(p1)} و{m(p2)} و{m(p3)} عند قسمتها على {m('x - 1')} و{m('x - 2')} و{m('x - 3')} على الترتيب. إذا كان {m('R(x)')} باقي قسمتها على {m('(x - 1)(x - 2)(x - 3)')}، فأوجد {m(f'R({x_ask})')}.",
            ans, [ans - 2 * A_q, ans + 2 * A_q, p3 + (p3 - p2), ans - 4],
            f"Dividing by a cubic gives a **quadratic** remainder {m('R(x) = Ax^2 + Bx + C')} passing through {m(f'(1,{p1}),\\;(2,{p2}),\\;(3,{p3})')}!",
            f"القسمة على مقسوم تكعيبي تعطي باقياً **تربيعياً** {m('R(x) = Ax^2 + Bx + C')} يمر بالنقاط الثلاث!",
            f"Since {m('R(x)')} has degree at most {m('2')}, its second differences are constant ({m('2A')}) — or solve for {m('A, B, C')} directly!",
            [
                f"Write {m('R(x) = Ax^2 + Bx + C')} with {m(f'R(1) = {p1},\\; R(2) = {p2},\\; R(3) = {p3}')}.",
                f"First differences are {m(f'{p2 - p1}')} and {m(f'{p3 - p2}')}, so the constant second difference is {m(f'2A = {(p3 - p2) - (p2 - p1)} \\implies A = {A_q}')}, giving {m(f'B = {B_q},\\; C = {C_q}')}.",
                f"Evaluate at {m(f'x = {x_ask}')}: {m(f'R({x_ask}) = {A_q}({x_ask}^2) + ({B_q})({x_ask}) + {C_q} = {ans}')}.",
            ],
            f"Check all three roots: {m(f'R(1)={p1},\\; R(2)={p2},\\; R(3)={p3}')}, confirming {m(f'R({x_ask}) = {ans}')}!",
            f"بما أن درجة {m('R(x)')} لا تتجاوز {m('2')}، نحدد معاملاتها من القيم الثلاث (أو عبر الفروق الثانية الثابتة)!",
            [
                f"نفرض {m('R(x) = Ax^2 + Bx + C')} بحيث {m(f'R(1)={p1},\\; R(2)={p2},\\; R(3)={p3}')}.",
                f"الفرق الثاني الثابت يساوي {m(f'2A = {p3 - 2*p2 + p1} \\implies A = {A_q}')}، ومنه {m(f'B = {B_q}')} و{m(f'C = {C_q}')}.",
                f"بالتعويض عند {m(f'x = {x_ask}')} نجد {m(f'R({x_ask}) = {ans}')}.",
            ],
            f"تحقق: نعوّض بـ {m('1, 2, 3')} في {m('R(x)')} فنسترجع {m(f'{p1}, {p2}, {p3}')} تماماً!",
            diagram_en=svg_parabola_roots("1, 2, 3", f"R({x_ask})", "?"),
        )

    # 12. nsmo_g10_gauss_cubic_identity (5E, 6M, 4H)
    bp = "nsmo_g10_gauss_cubic_identity"
    easy_cubic = [
        # Numerical zero-sum: (x^3 + y^3 + z^3) / (x * y_abs * z_abs) or exact value when x + y + z = 0
        (17, -9, -8),    # 17^3 - 9^3 - 8^3 divided by (17 * 9 * 8) -> 3! Vary expressions!
        (25, -14, -11),  # (25^3 - 14^3 - 11^3) / (25 * 7 * 11) -> 6!
        (19, -12, -7),   # (19^3 - 12^3 - 7^3) / (19 * 4 * 7) -> 9!
        (23, -15, -8),   # (23^3 - 15^3 - 8^3) / (23 * 5 * 4) -> 18!
        (29, -16, -13),  # (29^3 - 16^3 - 13^3) / (29 * 8 * 13) -> 6? Let's divide by (29 * 4 * 13) -> 12!
    ]
    div_specs = [
        (17, 9, 8, "17 \\times 9 \\times 8"),
        (25, 14, 11, "25 \\times 7 \\times 11"),
        (19, 12, 7, "19 \\times 4 \\times 7"),
        (23, 15, 8, "23 \\times 5 \\times 4"),
        (29, 16, 13, "29 \\times 4 \\times 13"),
    ]
    denom_vals = [17 * 9 * 8, 25 * 7 * 11, 19 * 4 * 7, 23 * 5 * 4, 29 * 4 * 13]
    for (u_v, v_v, w_v, den_tex), den_num in zip(div_specs, denom_vals):
        assert u_v - v_v - w_v == 0
        num_val = u_v ** 3 - v_v ** 3 - w_v ** 3
        assert num_val % den_num == 0
        ans = num_val // den_num
        B.add_math(
            tp, "Easy", bp,
            f"Without expanding the cubes, evaluate {m(f'\\frac{{{u_v}^3 - {v_v}^3 - {w_v}^3}}{{{den_tex}}}')}.",
            f"دون فك المكعبات، احسب قيمة المقدار {m(f'\\frac{{{u_v}^3 - {v_v}^3 - {w_v}^3}}{{{den_tex}}}')}.",
            ans, [3, ans // 2 if ans > 4 else 6, ans + 3, ans * 2],
            f"Set {m(f'a = {u_v},\\; b = -{v_v},\\; c = -{w_v}')}: notice {m('a + b + c = 0')}, so {m('a^3 + b^3 + c^3 = 3abc')}!",
            f"ضع {m(f'a = {u_v},\\; b = -{v_v},\\; c = -{w_v}')}؛ لاحظ أن {m('a + b + c = 0')} ومنه {m('a^3 + b^3 + c^3 = 3abc')}!",
            f"Whenever {m('a + b + c = 0')}, Gauss's Cubic Identity collapses to {m('a^3 + b^3 + c^3 = 3abc')}!",
            [
                f"Let {m(f'a = {u_v},\\; b = -{v_v},\\; c = -{w_v}')}. Check their sum: {m(f'{u_v} - {v_v} - {w_v} = 0')}.",
                f"Thus {m(f'{u_v}^3 - {v_v}^3 - {w_v}^3 = 3({u_v})(-{v_v})(-{w_v}) = 3 \\times {u_v} \\times {v_v} \\times {w_v}')}.",
                f"Divide by {m(den_tex)} and cancel common factors to get {m(ans)}.",
            ],
            f"Sign check: {m('(-b)^3 = -b^3')} and {m('3(a)(-b)(-c) = +3abc > 0')}, matching {m(ans)}.",
            f"عندما يكون {m('a + b + c = 0')} تعطي متطابقة غاوس مباشرة {m('a^3 + b^3 + c^3 = 3abc')}!",
            [
                f"نضع {m(f'a = {u_v},\\; b = -{v_v},\\; c = -{w_v}')} فنلاحظ أن {m('a + b + c = 0')}.",
                f"إذن البسط يساوي {m(f'3({u_v})(-{v_v})(-{w_v}) = 3 \\times {u_v} \\times {v_v} \\times {w_v}')}.",
                f"نقسم على المقام {m(den_tex)} ونختصر العوامل المشتركة فنحصل على {m(ans)}.",
            ],
            f"تحقق: الإشارات السالبة تتلاشى في الضرب فيكون الناتج موجباً ويساوي {m(ans)}.",
        )

    # Medium (6): Real triples (r, m + sqrt(w), m - sqrt(w)) so e1, e2, e3 are exact integers and REAL numbers genuinely exist!
    med_triples = [
        (1, 2, 2),   # roots: 1, 2+sqrt(2), 2-sqrt(2) -> e1=5, e2=1*(4)+2=6, e3=2 -> sum cubes = 3(2) + 5(25-18) = 41
        (2, 3, 5),   # roots: 2, 3+sqrt(5), 3-sqrt(5) -> e1=8, e2=2(6)+4=16, e3=8 -> sum cubes = 24 + 8(64-48) = 152
        (3, 1, 3),   # roots: 3, 1+sqrt(3), 1-sqrt(3) -> e1=5, e2=3(2)-2=4, e3=-6 -> sum cubes = -18 + 5(25-12) = 47
        (1, 3, 3),   # roots: 1, 3+sqrt(3), 3-sqrt(3) -> e1=7, e2=6+6=12, e3=6 -> sum cubes = 18 + 7(49-36) = 109
        (2, 1, 2),   # roots: 2, 1+sqrt(2), 1-sqrt(2) -> e1=4, e2=4-1=3, e3=-2 -> sum cubes = -6 + 4(16-9) = 22
        (3, 2, 3),   # roots: 3, 2+sqrt(3), 2-sqrt(3) -> e1=7, e2=12+1=13, e3=3 -> sum cubes = 9 + 7(49-39) = 79
    ]
    for r_rt, m_rt, w_rt in med_triples:
        e1 = r_rt + 2 * m_rt
        e2 = r_rt * (2 * m_rt) + (m_rt * m_rt - w_rt)
        e3 = r_rt * (m_rt * m_rt - w_rt)
        ans = 3 * e3 + e1 * (e1 * e1 - 3 * e2)
        # Verify directly with radical expansion: (m+sqrt(w))^3 + (m-sqrt(w))^3 = 2m^3 + 6m*w
        assert ans == r_rt ** 3 + 2 * (m_rt ** 3) + 6 * m_rt * w_rt
        B.add_math(
            tp, "Medium", bp,
            f"Real numbers {m('a, b, c')} satisfy {m(f'a + b + c = {e1}')}, {m(f'ab + bc + ca = {e2}')}, and {m(f'abc = {e3}')}. Find {m('a^3 + b^3 + c^3')}.",
            f"أعداد حقيقية {m('a, b, c')} تحقق {m(f'a + b + c = {e1}')} و{m(f'ab + bc + ca = {e2}')} و{m(f'abc = {e3}')}. أوجد قيمة {m('a^3 + b^3 + c^3')}.",
            ans, [ans - 3 * e3, e1 ** 3 - 3 * e1 * e2, ans + 6, ans - 6],
            f"Use Gauss's identity: {m('a^3 + b^3 + c^3 = 3abc + (a+b+c)\\left[(a+b+c)^2 - 3(ab+bc+ca)\\right]')}.",
            f"استخدم متطابقة غاوس: {m('a^3 + b^3 + c^3 = 3abc + (a+b+c)\\left[(a+b+c)^2 - 3(ab+bc+ca)\\right]')}.",
            f"Express {m('a^2 + b^2 + c^2 - ab - bc - ca = (a+b+c)^2 - 3(ab+bc+ca)')} and apply Gauss's Cubic Identity!",
            [
                f"Compute {m(f'(a+b+c)^2 - 3(ab+bc+ca) = {e1}^2 - 3({e2}) = {e1*e1 - 3*e2}')}.",
                f"Multiply by {m(f'a + b + c = {e1}')}: {m(f'{e1} \\times {e1*e1 - 3*e2} = {e1*(e1*e1 - 3*e2)}')}.",
                f"Add {m(f'3abc = 3({e3}) = {3*e3}')}: {m(f'{e1*(e1*e1 - 3*e2)} + ({3*e3}) = {ans}')}.",
            ],
            f"Check: real numbers {m(f'({r_rt},\\; {m_rt}+\\sqrt{{{w_rt}}},\\; {m_rt}-\\sqrt{{{w_rt}}})')} satisfy all three conditions and cube-sum to {m(ans)}!",
            f"نحسب القوس {m('(a+b+c)^2 - 3(ab+bc+ca)')} ثم نعوّض مباشرة في متطابقة غاوس التكعيبية!",
            [
                f"نحسب {m(f'{e1}^2 - 3({e2}) = {e1*e1 - 3*e2}')}.",
                f"نضرب في {m(f'a + b + c = {e1}')} فنحصل على {m(e1 * (e1 * e1 - 3 * e2))}.",
                f"نضيف {m(f'3abc = {3 * e3}')} فيكون الناتج {m(ans)}.",
            ],
            f"تحقق: الثلاثية الحقيقية {m(f'({r_rt},\\; {m_rt}+\\sqrt{{{w_rt}}},\\; {m_rt}-\\sqrt{{{w_rt}}})')} تحقق المعطيات ومجموع مكعباتها {m(ans)}.",
        )

    # Hard (4): Vieta cubic roots & sum of squares + cubes given a+b+c and a^2+b^2+c^2 and a^3+b^3+c^3 -> find abc!
    hard_cubic = [
        # Given a+b+c, a^2+b^2+c^2, a^3+b^3+c^3 for real triples -> find abc!
        (1, 2, 3),   # a=1, b=2, c=3 -> s1=6, s2=14, s3=36 -> abc = 6!
        (2, 3, 4),   # s1=9, s2=29, s3=99 -> abc = 24
        (-1, 2, 4),  # s1=5, s2=21, s3=71 -> abc = -8? Keep positive or clean: (1, 3, 5) -> s1=9, s2=35, s3=153 -> abc = 15!
        (2, 4, 5),   # s1=11, s2=45, s3=197 -> abc = 40
    ]
    hard_cubic[2] = (1, 3, 5)
    for x1, x2, x3 in hard_cubic:
        s1 = x1 + x2 + x3
        s2 = x1 * x1 + x2 * x2 + x3 * x3
        s3 = x1 ** 3 + x2 ** 3 + x3 ** 3
        e2 = (s1 * s1 - s2) // 2
        ans = x1 * x2 * x3
        assert 3 * ans == s3 - s1 * (s2 - e2)
        B.add_math(
            tp, "Hard", bp,
            f"Real numbers {m('a, b, c')} satisfy {m(f'a + b + c = {s1}')}, {m(f'a^2 + b^2 + c^2 = {s2}')}, and {m(f'a^3 + b^3 + c^3 = {s3}')}. Find the product {m('abc')}.",
            f"أعداد حقيقية {m('a, b, c')} تحقق {m(f'a + b + c = {s1}')} و{m(f'a^2 + b^2 + c^2 = {s2}')} و{m(f'a^3 + b^3 + c^3 = {s3}')}. أوجد حاصل الضرب {m('abc')}.",
            ans, [3 * ans, e2, ans + 3, ans - 3],
            f"First recover {m('ab + bc + ca = \\frac{(a+b+c)^2 - (a^2+b^2+c^2)}{2}')}, then solve Gauss's identity for {m('abc')}!",
            f"أوجد أولاً {m('ab + bc + ca = \\frac{(a+b+c)^2 - (a^2+b^2+c^2)}{2}')}، ثم استخرج {m('abc')} من متطابقة غاوس!",
            f"Chain two symmetric identities: get {m('ab + bc + ca')} from {m('s_1, s_2')}, then get {m('3abc')} from Gauss's identity!",
            [
                f"Compute {m(f'ab + bc + ca = \\frac{{{s1}^2 - {s2}}}{{2}} = \\frac{{{s1*s1 - s2}}}{{2}} = {e2}')}.",
                f"By Gauss's identity, {m(f'{s3} - 3abc = {s1} \\times ({s2} - {e2}) = {s1 * (s2 - e2)}')}.",
                f"Solve for {m('abc')}: {m(f'3abc = {s3} - {s1*(s2 - e2)} = {3*ans} \\implies abc = {ans}')}.",
            ],
            f"Check: the numbers {m(f'\\{{{x1}, {x2}, {x3}\\}}')} have sum {m(s1)}, square-sum {m(s2)}, cube-sum {m(s3)}, and product {m(ans)}!",
            f"نستخرج {m('ab + bc + ca')} من متطابقة مربع المجموع، ثم نعوّض في متطابقة غاوس لإيجاد {m('abc')}!",
            [
                f"نحسب {m(f'ab + bc + ca = \\frac{{{s1}^2 - {s2}}}{{2}} = {e2}')}.",
                f"نعوّض في غاوس: {m(f'{s3} - 3abc = {s1}({s2} - {e2}) = {s1*(s2 - e2)}')}.",
                f"ومنه {m(f'3abc = {3*ans} \\implies abc = {ans}')}.",
            ],
            f"تحقق: الأعداد {m(f'{x1}, {x2}, {x3}')} تحقق جميع المعطيات وضربها {m(ans)}! (احذر نسيان القسمة على {m('3')}!).",
        )

    # 13. nsmo_g10_denesting_radicals (5E, 6M, 4H)
    bp = "nsmo_g10_denesting_radicals"
    # Easy (5): sqrt(A + 2*sqrt(B)) + sqrt(A - 2*sqrt(B)) = 2*sqrt(u) where u = k^2 > v
    easy_den = [
        (4, 3),    # u=4, v=3 -> A=7, B=12 -> sum = 2*2 = 4
        (9, 7),    # u=9, v=7 -> A=16, B=63 -> sum = 6
        (16, 11),  # u=16, v=11 -> A=27, B=176 -> sum = 8
        (25, 19),  # u=25, v=19 -> A=44, B=475 -> sum = 10
        (36, 23),  # u=36, v=23 -> A=59, B=828 -> sum = 12
    ]
    for u_v, v_v in easy_den:
        A_v = u_v + v_v
        B_v = u_v * v_v
        rt_u = math.isqrt(u_v)
        ans = 2 * rt_u
        B.add_math(
            tp, "Easy", bp,
            f"Simplify the radical sum {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} + \\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}}')}.",
            f"بسّط مجموع الجذرين المتداخلين {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} + \\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}}')}.",
            ans, [rt_u, ans + 2, ans - 2, u_v],
            f"Find {m('u > v')} with {m(f'u + v = {A_v}')} and {m(f'uv = {B_v}')}, so {m('\\sqrt{A \\pm 2\\sqrt{B}} = \\sqrt{u} \\pm \\sqrt{v}')}!",
            f"ابحث عن عددين {m('u > v')} مجموعهما {m(A_v)} وضربهما {m(B_v)}، فيكون {m('\\sqrt{A \\pm 2\\sqrt{B}} = \\sqrt{u} \\pm \\sqrt{v}')}!",
            f"Denest each radical using {m(f'u = {u_v}')} and {m(f'v = {v_v}')}; the irrational parts {m(f'\\pm\\sqrt{{{v_v}}}')} cancel!",
            [
                f"Notice {m(f'{u_v} + {v_v} = {A_v}')} and {m(f'{u_v} \\times {v_v} = {B_v}')} with {m(f'{u_v} > {v_v}')}.",
                f"Thus {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} = {rt_u} + \\sqrt{{{v_v}}}')} and {m(f'\\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}} = {rt_u} - \\sqrt{{{v_v}}}')}.",
                f"Add them: {m(f'({rt_u} + \\sqrt{{{v_v}}}) + ({rt_u} - \\sqrt{{{v_v}}}) = {ans}')}.",
            ],
            f"Squaring check: {m(f'S^2 = 2({A_v}) + 2\\sqrt{{{A_v}^2 - 4({B_v})}} = {2*A_v} + 2({u_v - v_v}) = {ans*ans} \\implies S = {ans}')}!",
            f"نفك كل جذر باستخدام {m(f'u = {u_v}')} و{m(f'v = {v_v}')} فتختصر الجذور الصماء بالجمع!",
            [
                f"العددان {m(u_v)} و{m(v_v)} يحققان {m(f'{u_v} + {v_v} = {A_v}')} و{m(f'{u_v} \\times {v_v} = {B_v}')}.",
                f"إذن الجذر الأول يساوي {m(f'{rt_u} + \\sqrt{{{v_v}}}')} والثاني يساوي {m(f'{rt_u} - \\sqrt{{{v_v}}}')}.",
                f"بجمع المقدارين نحصل على {m(ans)}.",
            ],
            f"تحقق بتربيع المجموع: {m(f'S^2 = {2*A_v} + 2({u_v - v_v}) = {ans*ans}')} وبما أن {m('S > 0')} فإن {m(f'S = {ans}')}.",
        )

    # Medium (6): Conjugate DIFFERENCES where u > v and v = k^2! So (sqrt(u) + k) - (sqrt(u) - k) = 2k!
    med_den = [
        (5, 1),    # A=6, B=5 -> diff = 2*1 = 2
        (7, 4),    # A=11, B=28 -> diff = 2*2 = 4
        (11, 9),   # A=20, B=99 -> diff = 2*3 = 6
        (19, 16),  # A=35, B=304 -> diff = 2*4 = 8
        (29, 25),  # A=54, B=725 -> diff = 2*5 = 10
        (41, 36),  # A=77, B=1476 -> diff = 2*6 = 12
    ]
    for u_v, v_v in med_den:
        A_v = u_v + v_v
        B_v = u_v * v_v
        rt_v = math.isqrt(v_v)
        ans = 2 * rt_v
        B.add_math(
            tp, "Medium", bp,
            f"Find the exact value of {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} - \\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}}')}.",
            f"أوجد القيمة الدقيقة للفرق {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} - \\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}}')}.",
            ans, [rt_v, ans + 2, v_v, 2 * u_v],
            f"Careful with order! Since {m(f'{u_v} > {v_v}')}, {m(f'\\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}} = \\sqrt{{{u_v}}} - {rt_v} > 0')}, NOT {m(f'{rt_v} - \\sqrt{{{u_v}}}')}!",
            f"انتبه للترتيب! بما أن {m(f'{u_v} > {v_v}')}، فإن الجذر الثاني يساوي {m(f'\\sqrt{{{u_v}}} - {rt_v} > 0')} وليس العكس!",
            f"Because {m(f'\\sqrt{{{u_v}}} > \\sqrt{{{v_v}}} = {rt_v}')}, subtracting the two denested expressions cancels {m(f'\\sqrt{{{u_v}}}')} and doubles {m(rt_v)}!",
            [
                f"Factor {m(f'{B_v} = {u_v} \\times {v_v}')} with {m(f'{u_v} + {v_v} = {A_v}')} and {m(f'{u_v} > {v_v}')}.",
                f"Thus {m(f'\\sqrt{{{A_v} + 2\\sqrt{{{B_v}}}}} = \\sqrt{{{u_v}}} + {rt_v}')} and {m(f'\\sqrt{{{A_v} - 2\\sqrt{{{B_v}}}}} = \\sqrt{{{u_v}}} - {rt_v}')}.",
                f"Subtract: {m(f'(\\sqrt{{{u_v}}} + {rt_v}) - (\\sqrt{{{u_v}}} - {rt_v}) = {ans}')}.",
            ],
            f"Sign check: the first radical is larger than the second, so the difference is positive and equals {m(ans)}!",
            f"بما أن {m(f'\\sqrt{{{u_v}}} > {rt_v}')}، عند الطرح يختفي الجذر الأصم {m(f'\\sqrt{{{u_v}}}')} ويتضاعف العدد الصحيح {m(rt_v)}!",
            [
                f"لدينا {m(f'{u_v} + {v_v} = {A_v}')} و{m(f'{u_v} \\times {v_v} = {B_v}')} مع {m(f'{u_v} > {v_v}')}.",
                f"إذن الجذر الأول {m(f'\\sqrt{{{u_v}}} + {rt_v}')} والجذر الثاني الموجب {m(f'\\sqrt{{{u_v}}} - {rt_v}')}.",
                f"بطرح الثاني من الأول نجد {m(f'2 \\times {rt_v} = {ans}')}.",
            ],
            f"تحقق بتربيع الفرق: {m(f'D^2 = {2*A_v} - 2({u_v - v_v}) = 4({v_v}) = {ans*ans} \\implies D = {ans}')}!",
        )

    # Hard (4): Missing factor 2 inside radical: sqrt(A + sqrt(B)) where B is odd or requires multiplying by sqrt(2)/sqrt(2), OR rationalizing 1/(sqrt(u)+sqrt(v)) telescoping chain!
    # Look at: 1 / sqrt(3 + 2*sqrt(2)) + 1 / sqrt(5 + 2*sqrt(6)) + ... + 1 / sqrt((2N+1) + 2*sqrt(N(N+1)))!!
    # Check k-th term: sqrt((k) + (k+1) + 2*sqrt(k(k+1))) = sqrt(k+1) + sqrt(k)!
    # Its reciprocal 1 / (sqrt(k+1) + sqrt(k)) = sqrt(k+1) - sqrt(k)!!
    # Summing from k = 1 to N^2 - 1 gives sqrt(N^2) - sqrt(1) = N - 1!!
    # WHOA!! Denesting + rationalizing + telescoping in ONE Senior Olympiad problem!! Let's verify for N = 4, 5, 6, 7 (k up to 15, 24, 35, 48)!
    for N_rad in (4, 5, 6, 7):
        top_k = N_rad * N_rad - 1
        last_A = 2 * top_k + 1
        last_B = top_k * (top_k + 1)
        ans = N_rad - 1
        B.add_math(
            tp, "Hard", bp,
            f"Evaluate the sum {m(f'\\sum_{{k=1}}^{{{top_k}}} \\frac{{1}}{{\\sqrt{{(2k + 1) + 2\\sqrt{{k(k + 1)}}}}}}')}.",
            f"احسب قيمة المجموع {m(f'\\sum_{{k=1}}^{{{top_k}}} \\frac{{1}}{{\\sqrt{{(2k + 1) + 2\\sqrt{{k(k + 1)}}}}}}')}.",
            ans, [N_rad, N_rad + 1, ans - 1, 2 * ans],
            f"First denest {m('\\sqrt{(k + k + 1) + 2\\sqrt{k(k+1)}} = \\sqrt{k+1} + \\sqrt{k}')}, then rationalize the denominator!",
            f"فك الجذر المتداخل أولاً إلى {m('\\sqrt{k+1} + \\sqrt{k}')}، ثم أنطق المقام لتحصل على مجموع تلسكوبي!",
            f"Denesting turns the denominator into {m('\\sqrt{k+1} + \\sqrt{k}')}, and rationalizing turns each fraction into {m('\\sqrt{k+1} - \\sqrt{k}')}!",
            [
                f"Since {m('(k + 1) + k = 2k + 1')} and {m('(k + 1)k = k(k + 1)')}, denesting gives {m('\\sqrt{(2k + 1) + 2\\sqrt{k(k + 1)}} = \\sqrt{k + 1} + \\sqrt{k}')}.",
                f"Rationalize each term: {m('\\frac{1}{\\sqrt{k + 1} + \\sqrt{k}} = \\sqrt{k + 1} - \\sqrt{k}')}.",
                f"Telescope from {m('k = 1')} to {m(f'k = {top_k}')}: {m(f'\\sqrt{{{top_k + 1}}} - \\sqrt{{1}} = {N_rad} - 1 = {ans}')}.",
            ],
            f"Check {m('k = 1')}: {m('\\frac{1}{\\sqrt{3 + 2\\sqrt{2}}} = \\frac{1}{\\sqrt{2} + 1} = \\sqrt{2} - 1')}, starting the telescoping chain cleanly!",
            f"بفك الجذر المتداخل ثم إنطاق المقام يتحول كل كسر إلى فرق جذرين متتاليين {m('\\sqrt{k+1} - \\sqrt{k}')}!",
            [
                f"نلاحظ أن {m('\\sqrt{(2k+1) + 2\\sqrt{k(k+1)}} = \\sqrt{k+1} + \\sqrt{k}')}.",
                f"بإنطاق المقام يصبح الحد العام {m('\\frac{1}{\\sqrt{k+1} + \\sqrt{k}} = \\sqrt{k+1} - \\sqrt{k}')}.",
                f"بالتعويض من {m('k = 1')} إلى {m(top_k)} تختصر الحدود الوسطى ويبقى {m(f'\\sqrt{{{top_k + 1}}} - 1 = {N_rad} - 1 = {ans}')}.",
            ],
            f"تحقق: الحد الأخير يصل إلى {m(f'\\sqrt{{{N_rad*N_rad}}} = {N_rad}')} والحد الأول يطرح {m('\\sqrt{1} = 1')}.",
        )

    # 14. nsmo_g10_exponential_substitution_quad (5E, 6M, 4H) — ZERO "logarithm" words!
    bp = "nsmo_g10_exponential_substitution_quad"
    easy_exp = [
        # (base, r1, r2): p^(2x) - (p^r1 + p^r2)*p^x + p^(r1+r2) = 0 -> roots x = r1, r2 -> ask r1^2 + r2^2
        (2, 1, 3),    # 4^x - 10*2^x + 16 = 0 -> x=1, 3 -> x1^2+x2^2 = 10
        (2, 2, 4),    # 4^x - 20*2^x + 64 = 0 -> x=2, 4 -> x1^2+x2^2 = 20
        (3, 0, 2),    # 9^x - 10*3^x + 9 = 0 -> x=0, 2 -> x1^2+x2^2 = 4
        (3, 1, 3),    # 9^x - 30*3^x + 81 = 0 -> x=1, 3 -> x1^2+x2^2 = 10? Vary: ask x1 + 2*x2 or (0, 3) -> 9^x - 28*3^x + 27 = 0 -> 9!
        (5, 1, 2),    # 25^x - 30*5^x + 125 = 0 -> x=1, 2 -> x1^2+x2^2 = 5
    ]
    easy_exp[3] = (3, 0, 3)  # 9^x - 28*3^x + 27 = 0 -> x=0, 3 -> x1^2+x2^2 = 9
    for base_p, r1, r2 in easy_exp:
        t1, t2 = base_p ** r1, base_p ** r2
        k_sum = t1 + t2
        m_prd = t1 * t2
        ans = r1 * r1 + r2 * r2
        B.add_math(
            tp, "Easy", bp,
            f"If {m('x_1')} and {m('x_2')} are the two real solutions of {m(f'{base_p*base_p}^x - {k_sum} \\cdot {base_p}^x + {m_prd} = 0')}, what is {m('x_1^2 + x_2^2')}?",
            f"إذا كان {m('x_1')} و{m('x_2')} الحلّين الحقيقيين للمعادلة {m(f'{base_p*base_p}^x - {k_sum} \\cdot {base_p}^x + {m_prd} = 0')}، فما قيمة {m('x_1^2 + x_2^2')}؟",
            ans, [r1 + r2, (r1 + r2) ** 2, ans + 2, t1 + t2],
            f"Substitute {m(f't = {base_p}^x')} to turn {m(f'{base_p*base_p}^x = ({base_p}^x)^2 = t^2')} into a factorable quadratic!",
            f"ضع {m(f't = {base_p}^x')} لتحويل المعادلة إلى معادلة تربيعية قابلة للتحليل في المتغير {m('t')}!",
            f"Let {m(f't = {base_p}^x')}: factor {m(f't^2 - {k_sum}t + {m_prd} = (t - {t1})(t - {t2}) = 0')} and match powers of {m(base_p)}!",
            [
                f"Substitute {m(f't = {base_p}^x')}: the equation becomes {m(f't^2 - {k_sum}t + {m_prd} = 0')}.",
                f"Factor: {m(f'(t - {t1})(t - {t2}) = 0')}, so {m(f'{base_p}^x = {t1} = {base_p}^{{{r1}}}')} or {m(f'{base_p}^x = {t2} = {base_p}^{{{r2}}}')}.",
                f"Hence the roots are {m(f'x_1 = {r1}')} and {m(f'x_2 = {r2}')}, giving {m(f'x_1^2 + x_2^2 = {r1}^2 + {r2}^2 = {ans}')}.",
            ],
            f"Check: both {m(f'x = {r1}')} and {m(f'x = {r2}')} satisfy the original exponential equation!",
            f"نستبدل {m(f't = {base_p}^x')} فنحصل على معادلة تربيعية بسيطة ثم نقارن قوى الأساس {m(base_p)}!",
            [
                f"بوضع {m(f't = {base_p}^x')} تصبح المعادلة {m(f't^2 - {k_sum}t + {m_prd} = 0')}.",
                f"بالتحليل: {m(f'(t - {t1})(t - {t2}) = 0')}، أي {m(f'{base_p}^x = {base_p}^{{{r1}}}')} أو {m(f'{base_p}^x = {base_p}^{{{r2}}}')}.",
                f"إذن الجذران هما {m(r1)} و{m(r2)}، ومجموع مربعيهما {m(f'{r1}^2 + {r2}^2 = {ans}')}.",
            ],
            f"تحقق: كلا الجذرين يحقق المعادلة الأصلية عند التعويض المباشر.",
        )

    # Medium (6): Vieta product on t = p^x -> p^(x1 + x2) = t1 * t2 = p^m -> x1 + x2 = m!
    med_exp = [
        (2, 13, 5),   # 4^x - 13*2^x + 32 = 0 (disc = 169 - 128 = 41 > 0, t1,t2 > 0) -> x1 + x2 = 5
        (3, 19, 4),   # 9^x - 19*3^x + 81 = 0 (disc = 361 - 324 = 37 > 0) -> x1 + x2 = 4
        (2, 23, 7),   # 4^x - 23*2^x + 128 = 0 (disc = 529 - 512 = 17 > 0) -> x1 + x2 = 7
        (5, 31, 3),   # 25^x - 31*5^x + 125 = 0 (disc = 961 - 500 = 461 > 0) -> x1 + x2 = 3
        (2, 17, 6),   # 4^x - 17*2^x + 64 = 0 (disc = 289 - 256 = 33 > 0) -> x1 + x2 = 6
        (3, 35, 5),   # 9^x - 35*3^x + 243 = 0 (disc = 1225 - 972 = 253 > 0) -> x1 + x2 = 5? Vary to m=8 on base 2: (2, 34, 8): 1156 - 1024 = 132 > 0 -> 8!
    ]
    med_exp[5] = (2, 34, 8)
    for base_p, k_mid, m_exp in med_exp:
        c_prd = base_p ** m_exp
        assert k_mid * k_mid - 4 * c_prd > 0
        ans = m_exp
        B.add_math(
            tp, "Medium", bp,
            f"Find the sum {m('x_1 + x_2')} of all real solutions to {m(f'{base_p*base_p}^x - {k_mid} \\cdot {base_p}^x + {c_prd} = 0')}.",
            f"أوجد مجموع جميع الحلول الحقيقية {m('x_1 + x_2')} للمعادلة {m(f'{base_p*base_p}^x - {k_mid} \\cdot {base_p}^x + {c_prd} = 0')}.",
            ans, [ans - 1, ans + 1, k_mid, ans * 2],
            f"Set {m(f't = {base_p}^x')}: by Vieta's formulas, {m(f't_1 t_2 = {base_p}^{{x_1}} \\cdot {base_p}^{{x_2}} = {base_p}^{{x_1 + x_2}}')}!",
            f"ضع {m(f't = {base_p}^x')}؛ من علاقات فييتا يكون حاصل ضرب الجذرين {m(f't_1 t_2 = {base_p}^{{x_1 + x_2}}')}!",
            f"You don't need individual roots {m('x_1, x_2')}! Vieta's product {m('t_1 t_2')} turns multiplication of powers into addition of exponents!",
            [
                f"Let {m(f't = {base_p}^x > 0')}; the quadratic {m(f't^2 - {k_mid}t + {c_prd} = 0')} has discriminant {m(f'{k_mid}^2 - 4({c_prd}) = {k_mid*k_mid - 4*c_prd} > 0')}, and both sum {m(k_mid)} and product {m(c_prd)} are positive, so {m('t_1, t_2 > 0')}.",
                f"By Vieta's formulas, {m(f't_1 t_2 = {base_p}^{{x_1}} \\cdot {base_p}^{{x_2}} = {base_p}^{{x_1 + x_2}} = {c_prd}')}.",
                f"Since {m(f'{c_prd} = {base_p}^{{{m_exp}}}')}, equating exponents gives {m(f'x_1 + x_2 = {ans}')} immediately!",
            ],
            f"Crucial check: both {m('t_1')} and {m('t_2')} are strictly positive ({m('t_1 + t_2 > 0')} and {m('t_1 t_2 > 0')}), so both real roots {m('x_1, x_2')} exist!",
            f"لا نحتاج لإيجاد كل جذر على حدة! قانون ضرب الجذرين في فييتا يعطي {m(f'{base_p}^{{x_1 + x_2}}')} في خطوة واحدة!",
            [
                f"بوضع {m(f't = {base_p}^x')} نحصل على {m(f't^2 - {k_mid}t + {c_prd} = 0')}، ومميزها موجب ومجموع جذريها وضربهما موجبان، فكلا الجذرين {m('t_1, t_2 > 0')}.",
                f"حسب فييتا: {m(f't_1 t_2 = {base_p}^{{x_1 + x_2}} = {c_prd} = {base_p}^{{{m_exp}}}')}.",
                f"بمقارنة الأسس نحصل على {m(f'x_1 + x_2 = {ans}')}.",
            ],
            f"تحقق: تحققنا من أن {m('t_1, t_2 > 0')} لضمان عدم وجود جذر مرفوض!",
        )

    # Hard (4): Reciprocal exponential symmetry p^x + p^(-x) = k -> find p^(3x) + p^(-3x), PLUS extraneous root trap!
    for base_p, k_s in [(2, 5), (3, 4), (5, 6), (7, 3)]:
        ans = k_s ** 3 - 3 * k_s
        B.add_math(
            tp, "Hard", bp,
            f"A real number {m('x')} satisfies {m(f'{base_p}^x + {base_p}^{{-x}} = {k_s}')}. What is the exact value of {m(f'{base_p*base_p*base_p}^x + {base_p*base_p*base_p}^{{-x}}')}?",
            f"عدد حقيقي {m('x')} يحقق المعادلة {m(f'{base_p}^x + {base_p}^{{-x}} = {k_s}')}. ما القيمة الدقيقة للمقدار {m(f'{base_p*base_p*base_p}^x + {base_p*base_p*base_p}^{{-x}}')}؟",
            ans, [k_s ** 3, k_s ** 3 - k_s, k_s ** 2 - 2, ans + 6 * k_s],
            f"Set {m(f't = {base_p}^x')} so {m(f't + \\frac{{1}}{{t}} = {k_s}')}, and use the cubic identity {m('t^3 + \\frac{1}{t^3} = \\left(t + \\frac{1}{t}\\right)^3 - 3\\left(t + \\frac{1}{t}\\right)')}!",
            f"ضع {m(f't = {base_p}^x')} فيكون {m(f't + \\frac{{1}}{{t}} = {k_s}')}، واستخدم المتطابقة {m('t^3 + t^{-3} = (t + t^{-1})^3 - 3(t + t^{-1})')}!",
            f"Recognize {m(f'{base_p**3}^x = ({base_p}^x)^3 = t^3')} and apply the reciprocal cube identity!",
            [
                f"Let {m(f't = {base_p}^x > 0')}. Note that {m(f't + \\frac{{1}}{{t}} = {k_s} > 2')}, so real {m('x')} genuinely exists.",
                f"Since {m(f'{base_p**3}^x + {base_p**3}^{{-x}} = t^3 + \\frac{{1}}{{t^3}}')}, expand {m('\\left(t + \\frac{1}{t}\\right)^3 = t^3 + \\frac{1}{t^3} + 3\\left(t + \\frac{1}{t}\\right)')}.",
                f"Therefore {m(f't^3 + \\frac{{1}}{{t^3}} = {k_s}^3 - 3({k_s}) = {k_s**3} - {3*k_s} = {ans}')}.",
            ],
            f"Alternative check: {m(f't^2 + t^{{-2}} = {k_s}^2 - 2 = {k_s*k_s - 2}')}, and {m(f'(t + t^{{-1}})(t^2 - 1 + t^{{-2}}) = {k_s} \\times {k_s*k_s - 3} = {ans}')}!",
            f"بوضع {m(f't = {base_p}^x')} يتحول المطلوب إلى {m('t^3 + t^{-3}')} ونحسبه بمتطابقة مكعب المجموع المتبادل!",
            [
                f"نضع {m(f't = {base_p}^x')} فنجد {m(f't + t^{{-1}} = {k_s}')} (وبما أن {m(f'{k_s} \\ge 2')} فالحل الحقيقي موجود).",
                f"نطبّق المتطابقة {m('t^3 + t^{-3} = (t + t^{-1})^3 - 3(t + t^{-1})')}.",
                f"نعوّض: {m(f'{k_s}^3 - 3({k_s}) = {k_s**3} - {3*k_s} = {ans}')}.",
            ],
            f"تحقق: {m(f't^2 + t^{{-2}} = {k_s*k_s - 2}')}، وضرب {m(f'{k_s} \\times ({k_s*k_s - 2} - 1) = {ans}')}!",
        )

    # 15. nsmo_g10_telescoping_series_identities (5E, 6M, 4H) — SVG: svg_number_strip
    bp = "nsmo_g10_telescoping_series_identities"
    # Easy (5): Step-2 telescoping sum_{k=1}^N 1/((2k-1)(2k+1)) = N / (2N + 1)
    for N_tel in (12, 15, 20, 24, 30):
        ans = Fraction(N_tel, 2 * N_tel + 1)
        assert ans == sum(Fraction(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, N_tel + 1))
        last_a, last_b = 2 * N_tel - 1, 2 * N_tel + 1
        B.add_math(
            tp, "Easy", bp,
            f"Evaluate the telescoping sum {m(f'\\frac{{1}}{{1 \\cdot 3}} + \\frac{{1}}{{3 \\cdot 5}} + \\frac{{1}}{{5 \\cdot 7}} + \\cdots + \\frac{{1}}{{{last_a} \\cdot {last_b}}}')}.",
            f"احسب قيمة المجموع التلسكوبي {m(f'\\frac{{1}}{{1 \\cdot 3}} + \\frac{{1}}{{3 \\cdot 5}} + \\frac{{1}}{{5 \\cdot 7}} + \\cdots + \\frac{{1}}{{{last_a} \\cdot {last_b}}}')}.",
            ans, [Fraction(2 * N_tel, 2 * N_tel + 1), Fraction(N_tel - 1, 2 * N_tel + 1), Fraction(1, 2 * N_tel + 1), Fraction(N_tel + 1, 2 * N_tel + 3)],
            f"Use {m('\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\!\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')} — don't forget the {m('\\frac{1}{2}')}!",
            f"استخدم التفكيك {m('\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\!\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')} ولا تنسَ المعامل {m('\\frac{1}{2}')}!",
            f"Split each odd-product fraction using partial fractions with factor {m('\\frac{1}{2}')} so interior terms cancel!",
            [
                f"Write each of the {m(N_tel)} terms as {m('\\frac{1}{2}\\!\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}.",
                f"Telescoping leaves {m(f'\\frac{{1}}{{2}}\\!\\left(1 - \\frac{{1}}{{{last_b}}}\\right) = \\frac{{1}}{{2}} \\cdot \\frac{{{2*N_tel}}}{{{last_b}}} = \\frac{{{N_tel}}}{{{last_b}}}')}.",
            ],
            f"Check {m('N = 1')}: formula gives {m('1/3')}, matching {m('\\frac{1}{1 \\cdot 3}')}!",
            f"نفكّك كل كسر مع الانتباه للقسمة على فرق العاملين {m('2')}!",
            [
                f"نكتب كل حد بالصورة {m('\\frac{1}{2}\\!\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}.",
                f"تختصر الحدود الوسطى ويبقى {m(f'\\frac{{1}}{{2}}\\!\\left(1 - \\frac{{1}}{{{last_b}}}\\right) = \\frac{{{N_tel}}}{{{last_b}}}')}.",
            ],
            f"تحقق: الناتج أقل من {m('1/2')} ويساوي {m(f'\\frac{{{N_tel}}}{{{last_b}}}')} في أبسط صورة.",
            diagram_en=svg_number_strip(["1/(1·3)", "1/(3·5)", "···", f"1/({last_a}·{last_b})"]),
        )

    # Medium (6): Triple-product telescoping sum_{k=1}^N 1/(k(k+1)(k+2)) = N(N+3) / (4(N+1)(N+2))
    for N_tr in (5, 6, 9, 10, 11, 14):
        ans = sum(Fraction(1, k * (k + 1) * (k + 2)) for k in range(1, N_tr + 1))
        assert ans == Fraction(N_tr * (N_tr + 3), 4 * (N_tr + 1) * (N_tr + 2))
        B.add_math(
            tp, "Medium", bp,
            f"Compute the exact value of {m(f'\\sum_{{k=1}}^{{{N_tr}}} \\frac{{1}}{{k(k + 1)(k + 2)}}')} as a simplified fraction.",
            f"احسب القيمة الدقيقة للمجموع {m(f'\\sum_{{k=1}}^{{{N_tr}}} \\frac{{1}}{{k(k + 1)(k + 2)}}')} في أبسط صورة كسرية.",
            ans, [ans * 2, Fraction(1, 4) - Fraction(1, (N_tr + 1) * (N_tr + 2)), ans + Fraction(1, (N_tr + 1) * (N_tr + 2)), Fraction(N_tr, 2 * (N_tr + 2))],
            f"Split {m('\\frac{1}{k(k+1)(k+2)} = \\frac{1}{2}\\!\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
            f"فكّك الحد العام بالمتطابقة {m('\\frac{1}{k(k+1)(k+2)} = \\frac{1}{2}\\!\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
            f"Use the triple-product telescoping identity so every intermediate pair cancels!",
            [
                f"Apply {m('\\frac{1}{k(k+1)(k+2)} = \\frac{1}{2}\\!\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
                f"Summing from {m('k = 1')} to {m(N_tr)} leaves {m(f'\\frac{{1}}{{2}}\\!\\left(\\frac{{1}}{{2}} - \\frac{{1}}{{{N_tr + 1} \\cdot {N_tr + 2}}}\\right)')}.",
                f"Simplify the fraction to lowest terms: {m(ans)}.",
            ],
            f"Upper-bound check: as {m('N')} grows, the sum approaches {m('\\frac{1}{4}')}, and {m(ans)} is slightly below {m('\\frac{1}{4}')}!",
            f"نطبّق متطابقة التفكيك الثلاثي فتختصر جميع الكسور الداخلية!",
            [
                f"نكتب كل حد بصورة {m('\\frac{1}{2}\\!\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
                f"بعد الاختصار يبقى {m(f'\\frac{{1}}{{2}}\\!\\left(\\frac{{1}}{{2}} - \\frac{{1}}{{{(N_tr+1)*(N_tr+2)}}}\\right)')}.",
                f"بتوحيد المقامات والتبسيط نحصل على {m(ans)}.",
            ],
            f"تحقق: القيمة النهائية أصغر بقليل من السقف التقاربي {m('1/4')}!",
            diagram_en=svg_number_strip(["1/(1·2·3)", "1/(2·3·4)", "···", f"k={N_tr}"]),
        )

    # Hard (4): Sophie Germain telescoping product ((1^4+4)(5^4+4)...((4m+1)^4+4)) / ((3^4+4)(7^4+4)...((4m-1)^4+4)) = (4m + 2)^2 + 1!
    for m_sg in (2, 3, 4, 5):
        num_terms = [4 * j + 1 for j in range(m_sg + 1)]
        den_terms = [4 * j + 3 for j in range(m_sg)]
        num_prod = math.prod(x ** 4 + 4 for x in num_terms)
        den_prod = math.prod(x ** 4 + 4 for x in den_terms)
        assert num_prod % den_prod == 0
        ans = num_prod // den_prod
        assert ans == (4 * m_sg + 2) ** 2 + 1
        num_str = "".join(f"({x}^4 + 4)" for x in num_terms)
        den_str = "".join(f"({x}^4 + 4)" for x in den_terms)
        B.add_math(
            tp, "Hard", bp,
            f"Using Sophie Germain's identity {m('x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)')}, evaluate {m(f'\\frac{{{num_str}}}{{{den_str}}}')}.",
            f"باستخدام متطابقة صوفي جيرمان {m('x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)')}، احسب قيمة {m(f'\\frac{{{num_str}}}{{{den_str}}}')}.",
            ans, [(4 * m_sg) ** 2 + 1, (4 * m_sg + 1) ** 2 + 1, ans - 4, ans + 8],
            f"Rewrite {m('x^4 + 4 = ((x - 1)^2 + 1)((x + 1)^2 + 1)')} so adjacent odd numbers share identical shifted squares!",
            f"أعد كتابة {m('x^4 + 4 = ((x - 1)^2 + 1)((x + 1)^2 + 1)')} لتختصر العوامل المتتالية في البسط والمقام!",
            f"Complete the square inside each factor of Sophie Germain: {m('x^4 + 4 = ((x - 1)^2 + 1)((x + 1)^2 + 1)')}!",
            [
                f"Notice {m('x^2 \\pm 2x + 2 = (x \\pm 1)^2 + 1')}, so every {m('x^4 + 4')} splits into {m('((x - 1)^2 + 1)((x + 1)^2 + 1)')}.",
                f"In the numerator ({m(', '.join(str(x) for x in num_terms))}) vs denominator ({m(', '.join(str(x) for x in den_terms))}), every factor cancels except {m('(0^2 + 1) = 1')} and {m(f'({4*m_sg + 2}^2 + 1)')}.",
                f"Compute {m(f'{4*m_sg + 2}^2 + 1 = {(4*m_sg + 2)**2} + 1 = {ans}')}.",
            ],
            f"Small-case check: for {m('m = 1')}, {m('\\frac{(1^4+4)(5^4+4)}{3^4+4} = \\frac{5 \\times 629}{85} = 37 = 6^2 + 1')}; here {m(f'{4*m_sg+2}^2 + 1 = {ans}')}!",
            f"نكتب كل عامل بالصورة {m('((x - 1)^2 + 1)((x + 1)^2 + 1)')} فيتحول الكسر الضخم إلى اختصار تلسكوبي بديع!",
            [
                f"من متطابقة صوفي جيرمان: {m('x^4 + 4 = ((x - 1)^2 + 1)((x + 1)^2 + 1)')}.",
                f"عند التعويض في البسط والمقام تُختصر جميع الأقواس المتناظرة ولا يبقى سوى {m('(0^2 + 1) = 1')} والقوس الأخير {m(f'({4*m_sg + 2}^2 + 1)')}.",
                f"إذن القيمة تساوي {m(f'{4*m_sg + 2}^2 + 1 = {ans}')}.",
            ],
            f"تحقق: العامل الوحيد غير المختصر في اليمين هو {m(f'{4*m_sg + 2}^2 + 1 = {ans}')}!",
            diagram_en=svg_number_strip(["(0²+1)(2²+1)", "(2²+1)(4²+1)", "···", f"{4*m_sg+2}²+1"]),
        )



# =============================================================================
# UNIT 3.4 — Functional Equations, AM-GM & Cauchy-Schwarz Inequalities (75 Qs)
# =============================================================================
def _add_unit_3_4(B: BankBuilder) -> None:
    tp = "Algebra"

    # 16. nsmo_g10_functional_involution_swap (5E, 6M, 4H) — SVG: svg_function_machine
    bp = "nsmo_g10_functional_involution_swap"
    # Easy (5): a * f(x) + b * f(k - x) = h(x), evaluate f(x0)
    easy_fe = [
        # (a, b, k, m_sl, d_in, x0) -> a*f(x) + b*f(k-x) = m_sl*x + d_in
        (2, 1, 10, 3, 0, 2),   # x=2: 2f(2)+f(8)=6; x=8: 2f(8)+f(2)=24 -> 3f(2) = 12 - 24 = -12? Make positive: (3, 1, 10, 4, 4, 7): x=7->32, x=3->16 -> 8f(7) = 96-16=80 -> f(7)=10!
        (3, 1, 10, 4, 4, 7),
        (2, 1, 8, 3, 6, 6),    # x=6->24, x=2->12 -> 3f(6) = 48-12=36 -> f(6)=12
        (3, 2, 9, 5, 0, 6),    # x=6->30, x=3->15 -> 5f(6) = 90-30=60 -> f(6)=12? Vary: x0=7 -> x=7->35, x=2->10 -> 5f(7)=105-20=85 -> f(7)=17!
        (4, 1, 12, 5, 0, 9),   # x=9->45, x=3->15 -> 15f(9)=180-15=165 -> f(9)=11!
        (3, 1, 14, 2, 8, 11),  # x=11->30, x=3->14 -> 8f(11)=90-14=76? Use (2, 1, 12, 3, 3, 9): x=9->30, x=3->12 -> 3f(9)=60-12=48 -> f(9)=16!
    ]
    easy_fe = [
        (3, 1, 10, 4, 4, 7),   # f(7) = 10
        (2, 1, 8, 3, 6, 6),    # f(6) = 12
        (3, 2, 9, 5, 0, 7),    # f(7) = 17
        (4, 1, 12, 5, 0, 9),   # f(9) = 11
        (2, 1, 12, 3, 3, 9),   # f(9) = 16
    ]
    for a_c, b_c, k_s, m_s, d_s, x0 in easy_fe:
        x1 = k_s - x0
        rhs0 = m_s * x0 + d_s
        rhs1 = m_s * x1 + d_s
        num_f = a_c * rhs0 - b_c * rhs1
        den_f = a_c * a_c - b_c * b_c
        assert num_f % den_f == 0
        ans = num_f // den_f
        rhs_tex = f"{m_s}x + {d_s}" if d_s else f"{m_s}x"
        b_str = str(b_c) if b_c > 1 else ""
        B.add_math(
            tp, "Easy", bp,
            f"A function {m('f: \\mathbb{R} \\to \\mathbb{R}')} satisfies {m(f'{a_c}f(x) + {b_str}f({k_s} - x) = {rhs_tex}')} for all real {m('x')}. What is {m(f'f({x0})')}?",
            f"دالة {m('f: \\mathbb{R} \\to \\mathbb{R}')} تحقق {m(f'{a_c}f(x) + {b_str}f({k_s} - x) = {rhs_tex}')} لكل عدد حقيقي {m('x')}. ما قيمة {m(f'f({x0})')}؟",
            ans, [ans - 2, ans + 3, (rhs0 - rhs1) // max(1, a_c - b_c) + 1, ans + 5],
            f"Plug in both {m(f'x = {x0}')} and {m(f'x = {x1}')} to get two linear equations in {m(f'f({x0})')} and {m(f'f({x1})')}!",
            f"عوّض بكلٍّ من {m(f'x = {x0}')} و{m(f'x = {x1}')} لتحصل على معادلتين خطيتين في {m(f'f({x0})')} و{m(f'f({x1})')}!",
            f"Exploit the reflection involution {m(f'x \\leftrightarrow {k_s} - x')} to eliminate {m(f'f({x1})')}!",
            [
                f"At {m(f'x = {x0}')}: {m(f'{a_c}f({x0}) + {b_c}f({x1}) = {rhs0}')}.",
                f"At {m(f'x = {x1}')}: {m(f'{a_c}f({x1}) + {b_c}f({x0}) = {rhs1}')}.",
                f"Multiply the first equation by {m(a_c)} and subtract {m(b_c)} times the second: {m(f'{den_f}f({x0}) = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"Check: solving for {m(f'f({x1}) = {(a_c*rhs1 - b_c*rhs0)//den_f}')} satisfies both equations!",
            f"نستثمر التبديل الانعكاسي {m(f'x \\leftrightarrow {k_s} - x')} لحذف {m(f'f({x1})')}!",
            [
                f"عند {m(f'x = {x0}')}: {m(f'{a_c}f({x0}) + {b_c}f({x1}) = {rhs0}')}.",
                f"عند {m(f'x = {x1}')}: {m(f'{a_c}f({x1}) + {b_c}f({x0}) = {rhs1}')}.",
                f"بحذف {m(f'f({x1})')} نجد {m(f'{den_f}f({x0}) = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"تحقق: تعويض القيمتين يحقق المعادلتين معاً بدقة.",
            diagram_en=svg_function_machine(f"x={x0},{x1}", f"x ↔ {k_s}−x", "Eliminate", f"f({x0})=?"),
        )

    # Medium (6): Reciprocal involution a * f(x) + b * f(c / x) = m_s * x + d_s
    med_fe = [
        (2, 1, 8, 3, 0, 4),    # x=4->12, x=2->6 -> 3f(4) = 24-6 = 18 -> f(4)=6
        (3, 1, 12, 2, 4, 6),   # x=6->16, x=2->8 -> 8f(6) = 48-8 = 40 -> f(6)=5
        (2, 1, 10, 3, 3, 5),   # x=5->18, x=2->9 -> 3f(5) = 36-9 = 27 -> f(5)=9
        (3, 2, 15, 5, 0, 5),   # x=5->25, x=3->15 -> 5f(5) = 75-30 = 45 -> f(5)=9? Vary: x0=3 -> 5f(3) = 45-50=-5; use (3, 1, 15, 4, 4, 5): x=5->24, x=3->16 -> 8f(5)=72-16=56 -> f(5)=7!
        (2, 1, 18, 2, 5, 9),   # x=9->23, x=2->9 -> 3f(9) = 46-9 = 37? Use d_s=3: x=9->21, x=2->7 -> 3f(9)=42-7=35? d_s=4: x=9->22, x=2->8 -> 3f(9)=44-8=36 -> f(9)=12!
        (4, 1, 20, 3, 3, 10),  # x=10->33, x=2->9 -> 15f(10) = 132-9 = 123? Use d_s=0: x=10->30, x=2->6 -> 15f(10)=120-6=114? Use (3, 1, 20, 2, 4, 10): x=10->24, x=2->8 -> 8f(10)=72-8=64 -> f(10)=8!
    ]
    med_fe[3] = (3, 1, 15, 4, 4, 5)
    med_fe[4] = (2, 1, 18, 2, 4, 9)
    med_fe[5] = (3, 1, 20, 2, 4, 10)
    for a_c, b_c, c_p, m_s, d_s, x0 in med_fe:
        x1 = c_p // x0
        rhs0 = m_s * x0 + d_s
        rhs1 = m_s * x1 + d_s
        num_f = a_c * rhs0 - b_c * rhs1
        den_f = a_c * a_c - b_c * b_c
        assert num_f % den_f == 0
        ans = num_f // den_f
        rhs_tex = f"{m_s}x + {d_s}" if d_s else f"{m_s}x"
        B.add_math(
            tp, "Medium", bp,
            f"For all positive real numbers {m('x > 0')}, a function {m('f')} satisfies {m(f'{a_c}f(x) + f\\!\\left(\\frac{{{c_p}}}{{x}}\\right) = {rhs_tex}')}. Find {m(f'f({x0})')}.",
            f"لكل عدد حقيقي موجب {m('x > 0')}، تحقق الدالة {m('f')} العلاقة {m(f'{a_c}f(x) + f\\!\\left(\\frac{{{c_p}}}{{x}}\\right) = {rhs_tex}')}. أوجد قيمة {m(f'f({x0})')}.",
            ans, [ans - 2, ans + 2, rhs0 // a_c, ans + 4],
            f"Pair {m(f'x = {x0}')} with {m(f'x = {c_p}/{x0} = {x1}')} and eliminate {m(f'f({x1})')}!",
            f"زاوج بين {m(f'x = {x0}')} و{m(f'x = {c_p}/{x0} = {x1}')} ثم احذف {m(f'f({x1})')}!",
            f"Substitute {m(f'x = {x0}')} and {m(f'x = {x1}')} so {m('f(x)')} and {m(f'f({c_p}/x)')} swap places!",
            [
                f"At {m(f'x = {x0}')}: {m(f'{a_c}f({x0}) + f({x1}) = {rhs0}')}.",
                f"At {m(f'x = {x1}')}: {m(f'{a_c}f({x1}) + f({x0}) = {rhs1}')}.",
                f"Multiply the first by {m(a_c)} and subtract the second: {m(f'{den_f}f({x0}) = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"Check: {m(f'f({x1}) = {rhs0 - a_c * ans}')}, and {m(f'{a_c}({rhs0 - a_c*ans}) + {ans} = {rhs1}')}!",
            f"نعوّض بالعدد {m(x0)} ومقلوبه التناسبي {m(x1)} ليتبادل المجهولان موقعيهما!",
            [
                f"عند {m(f'x = {x0}')}: {m(f'{a_c}f({x0}) + f({x1}) = {rhs0}')}.",
                f"عند {m(f'x = {x1}')}: {m(f'{a_c}f({x1}) + f({x0}) = {rhs1}')}.",
                f"بضرب الأولى في {m(a_c)} وطرح الثانية نجد {m(f'{den_f}f({x0}) = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"تحقق: القيمة {m(f'f({x0}) = {ans}')} تحقق كلتا المعادلتين معاً.",
            diagram_en=svg_function_machine(f"x={x0},{x1}", f"x ↔ {c_p}/x", f"{den_f}f({x0})={num_f}", "?"),
        )

    # Hard (4): Fractional-linear involution g(x) = (x + c)/(x - 1) where g(g(x)) = x!
    # Check: if c = 3, x0 = 2 -> x1 = (2+3)/(2-1) = 5! Check g(5) = (5+3)/(5-1) = 8/4 = 2!
    # If c = 5, x0 = 2 -> x1 = 7; g(7) = 12/6 = 2!
    # If c = 7, x0 = 3 -> x1 = 10/2 = 5; g(5) = 12/4 = 3!
    # If c = 11, x0 = 4 -> x1 = 15/3 = 5; g(5) = 16/4 = 4!
    hard_fe = [
        (2, 3, 2, 3, 1),   # 2f(x) + f((x+3)/(x-1)) = 3x + 1, find f(2): x=2->7, x=5->16? Wait 2(7)-16=-2; ask f(5): 2(16)-7=25? Use rhs = 3x+2: x=2->8, x=5->17 -> f(5): 3f(5) = 34-8=26? Use rhs = 3x+3: x=2->9, x=5->18 -> 3f(5) = 36-9 = 27 -> f(5) = 9!
        (2, 5, 2, 3, 0),   # c=5, x0=7, x1=2: rhs=3x -> x=7->21, x=2->6 -> 3f(7) = 42-6 = 36 -> f(7) = 12!
        (3, 7, 5, 4, 4),   # c=7, x0=5, x1=3: 3f(x)+f(g(x))=4x+4 -> x=5->24, x=3->16 -> 8f(5) = 72-16=56 -> f(5) = 7!
        (2, 11, 5, 6, 0),  # c=11, x0=5, x1=4: 2f(x)+f(g(x))=6x -> x=5->30, x=4->24 -> 3f(5) = 60-24=36 -> f(5) = 12? Vary: rhs=6x+3 -> x=5->33, x=4->27 -> 3f(5)=66-27=39 -> f(5)=13!
    ]
    hard_fe = [
        (2, 3, 5, 3, 3),    # f(5) = 9
        (2, 5, 7, 3, 0),    # f(7) = 12
        (3, 7, 5, 4, 4),    # f(5) = 7
        (2, 11, 5, 6, 3),   # f(5) = 13
    ]
    for a_c, c_fl, x0, m_s, d_s in hard_fe:
        x1 = (x0 + c_fl) // (x0 - 1)
        assert (x1 + c_fl) == x0 * (x1 - 1)  # exact involution check!
        rhs0 = m_s * x0 + d_s
        rhs1 = m_s * x1 + d_s
        den_f = a_c * a_c - 1
        num_f = a_c * rhs0 - rhs1
        assert num_f % den_f == 0
        ans = num_f // den_f
        rhs_tex = f"{m_s}x + {d_s}" if d_s else f"{m_s}x"
        B.add_math(
            tp, "Hard", bp,
            f"For all real {m('x \\neq 1')}, a function {m('f')} satisfies {m(f'{a_c}f(x) + f\\!\\left(\\frac{{x + {c_fl}}}{{x - 1}}\\right) = {rhs_tex}')}. What is {m(f'f({x0})')}?",
            f"لكل عدد حقيقي {m('x \\neq 1')}، تحقق الدالة {m('f')} المعادلة {m(f'{a_c}f(x) + f\\!\\left(\\frac{{x + {c_fl}}}{{x - 1}}\\right) = {rhs_tex}')}. ما قيمة {m(f'f({x0})')}؟",
            ans, [ans - 2, ans + 2, rhs0 // a_c, ans + 5],
            f"Test {m(f'g(x) = \\frac{{x + {c_fl}}}{{x - 1}}')} at {m(f'x = {x0}')}: you get {m(x1)}, and applying {m('g')} to {m(x1)} returns right back to {m(x0)}!",
            f"احسب {m(f'g({x0}) = \\frac{{{x0} + {c_fl}}}{{{x0} - 1}} = {x1}')}، وستجد أن {m(f'g({x1}) = {x0}')} (دالة انعكاسية ذاتية)!",
            f"Notice {m(f'g(x) = \\frac{{x + {c_fl}}}{{x - 1}}')} is an involution ({m('g(g(x)) = x')}), pairing {m(x0)} with {m(x1)}!",
            [
                f"Plug in {m(f'x = {x0}')}: since {m(f'\\frac{{{x0} + {c_fl}}}{{{x0} - 1}} = {x1}')}, we get {m(f'{a_c}f({x0}) + f({x1}) = {rhs0}')}.",
                f"Plug in {m(f'x = {x1}')}: since {m(f'\\frac{{{x1} + {c_fl}}}{{{x1} - 1}} = {x0}')}, we get {m(f'{a_c}f({x1}) + f({x0}) = {rhs1}')}.",
                f"Eliminate {m(f'f({x1})')}: {m(f'{den_f}f({x0}) = {a_c}({rhs0}) - {rhs1} = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"Involution check: {m(f'g({x0}) = {x1}')} and {m(f'g({x1}) = {x0}')}, closing the 2-cycle cleanly!",
            f"التحويل الكسري {m(f'g(x) = \\frac{{x + {c_fl}}}{{x - 1}}')} انعكاسي ذاتي ({m('g(g(x)) = x')}) فيربط {m(x0)} بالعدد {m(x1)}!",
            [
                f"عند {m(f'x = {x0}')} نجد {m(f'g({x0}) = {x1}')} فنحصل على {m(f'{a_c}f({x0}) + f({x1}) = {rhs0}')}.",
                f"وعند {m(f'x = {x1}')} نجد {m(f'g({x1}) = {x0}')} فنحصل على {m(f'{a_c}f({x1}) + f({x0}) = {rhs1}')}.",
                f"بحذف {m(f'f({x1})')} نجد {m(f'{den_f}f({x0}) = {num_f} \\implies f({x0}) = {ans}')}.",
            ],
            f"تحقق: الدورة المغلقة بين {m(x0)} و{m(x1)} تحسم قيمة {m(f'f({x0}) = {ans}')} دون الحاجة لإيجاد صيغة عامة.",
            diagram_en=svg_function_machine(f"x={x0}", f"(x+{c_fl})/(x−1)", f"x={x1} ↺", f"f({x0})=?"),
        )

    # 17. nsmo_g10_cauchy_additive_recurrence (5E, 6M, 4H)
    bp = "nsmo_g10_cauchy_additive_recurrence"
    # Easy (5): Shifted additive f(x + y) = f(x) + f(y) + c on Z, given f(1) = v1, find f(N) -> f(n) = (v1 + c)*n - c
    easy_cr = [
        (3, 4, 10),    # c=3, f(1)=4 -> f(n) = 7n - 3 -> f(10) = 67
        (5, 2, 12),    # c=5, f(1)=2 -> f(n) = 7n - 5 -> f(12) = 79
        (-2, 6, 15),   # c=-2, f(1)=6 -> f(n) = 4n + 2 -> f(15) = 62
        (4, 3, 14),    # c=4, f(1)=3 -> f(n) = 7n - 4 -> f(14) = 94
        (6, 5, 11),    # c=6, f(1)=5 -> f(n) = 11n - 6 -> f(11) = 115
    ]
    for c_sh, v1, N_ev in easy_cr:
        ans = (v1 + c_sh) * N_ev - c_sh
        c_tex = f"+ {c_sh}" if c_sh > 0 else f"- {-c_sh}"
        B.add_math(
            tp, "Easy", bp,
            f"A function {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} satisfies {m(f'f(x + y) = f(x) + f(y) {c_tex}')} for all integers {m('x, y')}, and {m(f'f(1) = {v1}')}. Find {m(f'f({N_ev})')}.",
            f"دالة {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} تحقق {m(f'f(x + y) = f(x) + f(y) {c_tex}')} لكل عددين صحيحين {m('x, y')}، مع {m(f'f(1) = {v1}')}. أوجد قيمة {m(f'f({N_ev})')}.",
            ans, [v1 * N_ev + c_sh, ans + c_sh, ans - c_sh, (v1 + c_sh) * N_ev],
            f"Add {m(c_sh)} to both sides: {m(f'g(n) = f(n) + ({c_sh})')} satisfies Cauchy's additive rule {m('g(x+y) = g(x) + g(y)')}!",
            f"أضف الثابت للطرفين لتعريف الدالة الخطية التجميعية {m(f'g(n) = f(n) + ({c_sh})')} التي تحقق {m('g(x+y) = g(x) + g(y)')}!",
            f"Shift {m(f'g(n) = f(n) + ({c_sh})')} (or sum constant step {m('f(n+1) - f(n) = f(1) + c')})!",
            [
                f"Set {m('y = 1')}: {m(f'f(n + 1) - f(n) = f(1) + ({c_sh}) = {v1 + c_sh}')}, an arithmetic progression with common difference {m(v1 + c_sh)}.",
                f"Starting from {m(f'f(1) = {v1}')}, we get {m(f'f({N_ev}) = {v1} + ({N_ev} - 1) \\times {v1 + c_sh} = {ans}')}.",
            ],
            f"Check {m('n = 2')}: {m(f'f(2) = 2({v1}) + ({c_sh}) = {2*v1 + c_sh}')}, matching {m(f'{v1} + {v1 + c_sh}')}!",
            f"بوضع {m('y = 1')} نجد أن الفرق المتتالي ثابت فتتحول المتتالية إلى متتابعة حسابية!",
            [
                f"نضع {m('y = 1')} فنجد الفرق الثابت {m(f'f(n + 1) - f(n) = {v1} + ({c_sh}) = {v1 + c_sh}')}.",
                f"انطلاقاً من {m(f'f(1) = {v1}')} نحصل على {m(f'f({N_ev}) = {v1} + {N_ev - 1} \\times {v1 + c_sh} = {ans}')}.",
            ],
            f"تحقق: عند {m('x = y = 1')} نجد {m(f'f(2) = {2*v1 + c_sh}')} وهو يطابق الصيغة الخطية.",
        )

    # Medium (6): f(x + y) = f(x) + f(y) + 2a*x*y with f(1) = v1 -> f(n) = a*n^2 + (v1 - a)*n
    med_cr = [
        (1, 3, 10),    # k=2, f(1)=3 -> f(n) = n^2 + 2n -> f(10) = 120
        (2, 5, 8),     # k=4, f(1)=5 -> f(n) = 2n^2 + 3n -> f(8) = 152
        (3, 4, 7),     # k=6, f(1)=4 -> f(n) = 3n^2 + n -> f(7) = 154
        (1, 5, 12),    # k=2, f(1)=5 -> f(n) = n^2 + 4n -> f(12) = 192
        (2, 1, 9),     # k=4, f(1)=1 -> f(n) = 2n^2 - n -> f(9) = 153
        (4, 6, 6),     # k=8, f(1)=6 -> f(n) = 4n^2 + 2n -> f(6) = 156
    ]
    for a_q, v1, N_ev in med_cr:
        k_xy = 2 * a_q
        b_lin = v1 - a_q
        ans = a_q * N_ev * N_ev + b_lin * N_ev
        B.add_math(
            tp, "Medium", bp,
            f"A function {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} satisfies {m(f'f(x + y) = f(x) + f(y) + {k_xy}xy')} for all integers {m('x, y')}, and {m(f'f(1) = {v1}')}. Find {m(f'f({N_ev})')}.",
            f"دالة {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} تحقق {m(f'f(x + y) = f(x) + f(y) + {k_xy}xy')} لكل عددين صحيحين {m('x, y')}، مع {m(f'f(1) = {v1}')}. أوجد قيمة {m(f'f({N_ev})')}.",
            ans, [ans - b_lin * N_ev, ans + a_q * N_ev, a_q * N_ev * N_ev, ans + 10],
            f"Notice {m(f'{a_q}(x + y)^2 = {a_q}x^2 + {a_q}y^2 + {k_xy}xy')}, so {m(f'g(n) = f(n) - {a_q}n^2')} is purely linear!",
            f"لاحظ أن {m(f'{a_q}(x + y)^2 = {a_q}x^2 + {a_q}y^2 + {k_xy}xy')}، لذا فإن {m(f'g(n) = f(n) - {a_q}n^2')} دالة خطية تماماً!",
            f"Subtract the quadratic core {m(f'{a_q}n^2')} (or telescope {m('f(k+1) - f(k)')}) to find {m('f(n)')} explicitly!",
            [
                f"Define {m(f'g(n) = f(n) - {a_q}n^2')}; then {m('g(x + y) = g(x) + g(y)')}, so {m('g(n) = g(1) \\cdot n')}.",
                f"From {m(f'f(1) = {v1}')}, we get {m(f'g(1) = {v1} - {a_q} = {b_lin}')}, so {m(f'f(n) = {a_q}n^2 + ({b_lin})n')}.",
                f"Evaluate at {m(f'n = {N_ev}')}: {m(f'f({N_ev}) = {a_q}({N_ev}^2) + ({b_lin})({N_ev}) = {ans}')}.",
            ],
            f"Difference check: {m(f'f(2) = 2({v1}) + {k_xy} = {2*v1 + k_xy}')}, matching {m(f'{a_q}(4) + ({b_lin})(2) = {4*a_q + 2*b_lin}')}!",
            f"بطرح الجزء التربيعي {m(f'{a_q}n^2')} تتحول الدالة إلى دالة خطية تجميعية!",
            [
                f"نضع {m(f'g(n) = f(n) - {a_q}n^2')} فتتحقق {m('g(x+y) = g(x) + g(y)')} أي {m('g(n) = cn')}.",
                f"عند {m('n = 1')} نجد {m(f'c = {v1} - {a_q} = {b_lin}')}، إذن {m(f'f(n) = {a_q}n^2 + ({b_lin})n')}.",
                f"نعوّض بـ {m(f'n = {N_ev}')} فنحصل على {m(f'f({N_ev}) = {ans}')}.",
            ],
            f"تحقق: عند {m('x = y = 1')} تعطي الصيغة {m(f'f(2) = {2*v1 + k_xy}')} تماماً كما تعطي المعادلة الأصلية.",
        )

    # Hard (4): Given f(m) instead of f(1) in f(x + y) = f(x) + f(y) + k*x*y (including odd k via binomial n(n-1)/2!)
    hard_cr = [
        # f(n) = k * n(n-1)//2 + v1 * n: given f(m_giv) = V_giv, find f(N_ask)
        (3, 2, 4, 9),    # k=3, v1=2 -> f(4) = 3*6 + 8 = 26 -> f(9) = 3*36 + 18 = 126
        (5, 1, 5, 8),    # k=5, v1=1 -> f(5) = 5*10 + 5 = 55 -> f(8) = 5*28 + 8 = 148
        (2, 4, 6, 11),   # k=2, v1=4 -> f(6) = 2*15 + 24 = 54 -> f(11) = 2*55 + 44 = 154
        (3, 5, 6, 10),   # k=3, v1=5 -> f(6) = 3*15 + 30 = 75 -> f(10) = 3*45 + 50 = 185
    ]
    for k_xy, v1, m_g, N_ask in hard_cr:
        V_g = k_xy * (m_g * (m_g - 1) // 2) + v1 * m_g
        ans = k_xy * (N_ask * (N_ask - 1) // 2) + v1 * N_ask
        B.add_math(
            tp, "Hard", bp,
            f"A function {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} satisfies {m(f'f(x + y) = f(x) + f(y) + {k_xy}xy')} for all integers {m('x, y')}. If {m(f'f({m_g}) = {V_g}')}, what is {m(f'f({N_ask})')}?",
            f"دالة {m('f: \\mathbb{Z} \\to \\mathbb{Z}')} تحقق {m(f'f(x + y) = f(x) + f(y) + {k_xy}xy')} لكل عددين صحيحين {m('x, y')}. إذا علمت أن {m(f'f({m_g}) = {V_g}')}، فما قيمة {m(f'f({N_ask})')}؟",
            ans, [ans - v1 * N_ask, ans + k_xy * N_ask, ans - 10, ans + 12],
            f"Telescope {m(f'f(n+1) - f(n) = f(1) + {k_xy}n')} to get {m(f'f(n) = n f(1) + {k_xy}\\binom{{n}}{{2}}')}, then solve for {m('f(1)')} from {m(f'f({m_g}) = {V_g}')}!",
            f"اجمع الفروق {m(f'f(n+1) - f(n) = f(1) + {k_xy}n')} لتحصل على {m(f'f(n) = n f(1) + {k_xy}\\binom{{n}}{{2}}')}، ثم استخرج {m('f(1)')}!",
            f"Telescoping first differences gives {m(f'f(n) = n f(1) + {k_xy}\\frac{{n(n-1)}}{{2}}')} — valid even when {m(k_xy)} is odd!",
            [
                f"Set {m('x = y = 0')} to get {m('f(0) = 0')}. Setting {m('y = 1')} gives {m(f'f(j + 1) - f(j) = f(1) + {k_xy}j')}.",
                f"Summing for {m('j = 0, \\dots, n - 1')} yields {m(f'f(n) = n f(1) + {k_xy}\\frac{{n(n - 1)}}{{2}}')}.",
                f"Plug in {m(f'n = {m_g}')}: {m(f'{V_g} = {m_g}f(1) + {k_xy * m_g * (m_g - 1) // 2} \\implies f(1) = {v1}')}; hence {m(f'f({N_ask}) = {N_ask}({v1}) + {k_xy * N_ask * (N_ask - 1) // 2} = {ans}')}.",
            ],
            f"Check: {m(f'f({m_g}) = {m_g}({v1}) + {k_xy * m_g * (m_g - 1) // 2} = {V_g}')}!",
            f"بجمع الفروق التلسكوبية نجد {m(f'f(n) = n f(1) + {k_xy}\\frac{{n(n-1)}}{{2}}')} ونستخرج منها {m('f(1)')} أولاً!",
            [
                f"عند {m('x=y=0')} نجد {m('f(0)=0')}، وعند {m('y=1')} نجد {m(f'f(j+1) - f(j) = f(1) + {k_xy}j')}.",
                f"بجمع الفروق من {m('0')} إلى {m('n-1')} نحصل على {m(f'f(n) = n f(1) + {k_xy}\\frac{{n(n-1)}}{{2}}')}.",
                f"من {m(f'f({m_g}) = {V_g}')} نستنتج {m(f'f(1) = {v1}')}، وعند {m(f'n = {N_ask}')} نجد {m(f'f({N_ask}) = {ans}')}.",
            ],
            f"تحقق: الصيغة التوافقية تعمل بسلاسة تامة سواء أكان المعامل {m(k_xy)} زوجياً أم فردياً!",
        )

    # 18. nsmo_g10_am_gm_weighted_minimum (5E, 6M, 4H) — SVG: svg_area_identity_square
    bp = "nsmo_g10_am_gm_weighted_minimum"
    # Easy (5): Shifted 2-term AM-GM: x + K^2 / (x - c) for x > c -> min = 2K + c at x = c + K
    easy_am = [(5, 3), (6, 4), (7, 2), (8, 5), (9, 3)]
    for K_v, c_v in easy_am:
        ans = 2 * K_v + c_v
        B.add_math(
            tp, "Easy", bp,
            f"For real numbers {m(f'x > {c_v}')}, what is the minimum possible value of {m(f'x + \\frac{{{K_v*K_v}}}{{x - {c_v}}}')}?",
            f"للأعداد الحقيقية {m(f'x > {c_v}')}، ما أصغر قيمة ممكنة للمقدار {m(f'x + \\frac{{{K_v*K_v}}}{{x - {c_v}}}')}؟",
            ans, [2 * K_v, 2 * K_v - c_v, ans + 2, K_v + c_v],
            f"Rewrite {m(f'x = (x - {c_v}) + {c_v}')} so {m(f'(x - {c_v})')} cancels in the AM-GM product!",
            f"أعد كتابة {m(f'x = (x - {c_v}) + {c_v}')} ليختصر القوس {m(f'(x - {c_v})')} عند تطبيق متباينة الوسطين!",
            f"Match the denominator by writing {m(f'(x - {c_v}) + \\frac{{{K_v*K_v}}}{{x - {c_v}}} + {c_v}')} and applying 2-term AM-GM!",
            [
                f"Since {m(f'x > {c_v}')}, {m(f'u = x - {c_v} > 0')}. Rewrite the expression as {m(f'u + \\frac{{{K_v*K_v}}}{{u}} + {c_v}')}.",
                f"By AM-GM, {m(f'u + \\frac{{{K_v*K_v}}}{{u}} \\ge 2\\sqrt{{u \\cdot \\frac{{{K_v*K_v}}}{{u}}}} = {2 * K_v}')}.",
                f"Adding {m(c_v)} gives minimum {m(f'{2*K_v} + {c_v} = {ans}')}, attained when {m(f'u = {K_v} \\implies x = {c_v + K_v}')}.",
            ],
            f"Equality check at {m(f'x = {c_v + K_v}')}: {m(f'{c_v + K_v} + \\frac{{{K_v*K_v}}}{{{K_v}}} = {ans}')}!",
            f"نطابق المقام بكتابة {m(f'(x - {c_v}) + \\frac{{{K_v*K_v}}}{{x - {c_v}}} + {c_v}')} ثم نطبّق متباينة AM-GM!",
            [
                f"بما أن {m(f'x - {c_v} > 0')}، نطبّق AM-GM على الحدين الموجبين: {m(f'(x - {c_v}) + \\frac{{{K_v*K_v}}}{{x - {c_v}}} \\ge 2({K_v}) = {2*K_v}')}.",
                f"بإضافة الثابت {m(c_v)} تصبح القيمة الصغرى {m(f'{2*K_v} + {c_v} = {ans}')}.",
                f"تتحقق المساواة عندما {m(f'x - {c_v} = {K_v} \\implies x = {c_v + K_v}')}.",
            ],
            f"تحقق عند {m(f'x = {c_v + K_v}')}: {m(f'{c_v + K_v} + {K_v} = {ans}')}!",
            diagram_en=svg_area_identity_square(f"x−{c_v}", str(K_v)),
        )

    # Medium (6): 3-term AM-GM splitting: 3 of x^2 + 2*M^3 / x (M=3,4,5) and 3 of 2x + K^3 / x^2 (K=2,3,4 -> wait 2x + 2*K^3/x^2 = x + x + 2K^3/x^2? No: 2x + M^3 / x^2 -> x + x + M^3/x^2 >= 3M at x = M!)
    med_am_a = [3, 4, 5]  # x^2 + 2*M^3 / x >= 3*M^2 at x = M
    for M_v in med_am_a:
        num_c = 2 * (M_v ** 3)
        half_c = M_v ** 3
        ans = 3 * M_v * M_v
        B.add_math(
            tp, "Medium", bp,
            f"Find the minimum value of {m(f'x^2 + \\frac{{{num_c}}}{{x}}')} over all positive real numbers {m('x > 0')}.",
            f"أوجد أصغر قيمة للمقدار {m(f'x^2 + \\frac{{{num_c}}}{{x}}')} لجميع الأعداد الحقيقية الموجبة {m('x > 0')}.",
            ans, [ans - M_v * M_v, ans + M_v, 2 * M_v * M_v, ans + 6],
            f"Split {m(f'\\frac{{{num_c}}}{{x}} = \\frac{{{half_c}}}{{x}} + \\frac{{{half_c}}}{{x}}')} and apply 3-term AM-GM!",
            f"جزّئ الكسر إلى {m(f'\\frac{{{half_c}}}{{x}} + \\frac{{{half_c}}}{{x}}')} وطبّق متباينة الوسطين لثلاثة حدود!",
            f"Split the linear denominator into two equal parts so {m('x^2 \\cdot x^{-1} \\cdot x^{-1}')} cancels {m('x')} completely!",
            [
                f"Rewrite as {m(f'x^2 + \\frac{{{half_c}}}{{x}} + \\frac{{{half_c}}}{{x}}')}.",
                f"By 3-term AM-GM, this is at least {m(f'3\\sqrt[3]{{x^2 \\cdot \\frac{{{half_c}}}{{x}} \\cdot \\frac{{{half_c}}}{{x}}}} = 3\\sqrt[3]{{{half_c}^2}} = 3 \\times {M_v*M_v} = {ans}')}.",
                f"Equality holds when {m(f'x^2 = \\frac{{{half_c}}}{{x}} \\iff x = {M_v} > 0')}.",
            ],
            f"Check at {m(f'x = {M_v}')}: {m(f'{M_v}^2 + \\frac{{{num_c}}}{{{M_v}}} = {M_v*M_v} + {2*M_v*M_v} = {ans}')}!",
            f"نجزّئ الحد الكسري إلى نصفين متساويين لإلغاء {m('x^2')} في الجذر التكعيبي!",
            [
                f"نكتب المقدار بالصورة {m(f'x^2 + \\frac{{{half_c}}}{{x}} + \\frac{{{half_c}}}{{x}}')}.",
                f"بمتباينة AM-GM الثلاثية: المجموع {m(f'\\ge 3\\sqrt[3]{{{half_c}^2}} = 3({M_v*M_v}) = {ans}')}.",
                f"تتحقق المساواة عند {m(f'x = {M_v} > 0')}.",
            ],
            f"تحقق عند {m(f'x = {M_v}')}: {m(f'{M_v*M_v} + {2*M_v*M_v} = {ans}')}!",
            diagram_en=svg_area_identity_square("x²", f"{half_c}/x"),
        )

    for K_v in (3, 5, 6):  # 2x + K^3 / x^2 = x + x + K^3/x^2 >= 3K at x = K
        k_cub = K_v ** 3
        ans = 3 * K_v
        B.add_math(
            tp, "Medium", bp,
            f"For {m('x > 0')}, determine the minimum possible value of {m(f'2x + \\frac{{{k_cub}}}{{x^2}}')}.",
            f"لكل {m('x > 0')}، حدّد القيمة الصغرى الممكنة للمقدار {m(f'2x + \\frac{{{k_cub}}}{{x^2}}')}.",
            ans, [2 * K_v, 4 * K_v, ans + 2, ans - 2],
            f"Split {m('2x = x + x')} so {m(f'x \\cdot x \\cdot \\frac{{{k_cub}}}{{x^2}} = {k_cub}')} is constant!",
            f"جزّئ {m('2x = x + x')} ليصبح حاصل ضرب الحدود الثلاثة ثابتاً يساوي {m(k_cub)}!",
            f"Split {m('2x')} into {m('x + x')} to balance the {m('x^2')} in the denominator!",
            [
                f"Write {m(f'2x + \\frac{{{k_cub}}}{{x^2}} = x + x + \\frac{{{k_cub}}}{{x^2}}')}.",
                f"Apply 3-term AM-GM: {m(f'x + x + \\frac{{{k_cub}}}{{x^2}} \\ge 3\\sqrt[3]{{x \\cdot x \\cdot \\frac{{{k_cub}}}{{x^2}}}} = 3\\sqrt[3]{{{k_cub}}} = {ans}')}.",
                f"Equality holds when {m(f'x = \\frac{{{k_cub}}}{{x^2}} \\iff x = {K_v} > 0')}.",
            ],
            f"Check at {m(f'x = {K_v}')}: {m(f'2({K_v}) + \\frac{{{k_cub}}}{{{K_v*K_v}}} = {2*K_v} + {K_v} = {ans}')}!",
            f"نقسّم {m('2x')} إلى {m('x + x')} لموازنة المقام التربيعي {m('x^2')} في متباينة AM-GM!",
            [
                f"نكتب المقدار بالصورة {m(f'x + x + \\frac{{{k_cub}}}{{x^2}}')}.",
                f"بتطبيق متباينة الوسطين لثلاثة حدود: المجموع {m(f'\\ge 3\\sqrt[3]{{{k_cub}}} = 3({K_v}) = {ans}')}.",
                f"تتحقق المساواة عندما {m(f'x = {K_v}')}.",
            ],
            f"تحقق: عند {m(f'x = {K_v}')} يكون الناتج {m(f'{2*K_v} + {K_v} = {ans}')} بالضبط.",
            diagram_en=svg_area_identity_square("x", str(K_v)),
        )

    # Hard (4): 4-term AM-GM x^3 + 3*M^4/x >= 4*M^3 AND multivariable (x + a/y)(y + b/x) >= (sqrt(a)+sqrt(b))^2
    for M_v in (2, 3):
        c_num = 3 * (M_v ** 4)
        p_num = M_v ** 4
        ans = 4 * (M_v ** 3)
        B.add_math(
            tp, "Hard", bp,
            f"Over all positive real numbers {m('x > 0')}, what is the minimum possible value of {m(f'x^3 + \\frac{{{c_num}}}{{x}}')}?",
            f"على مجموعة الأعداد الحقيقية الموجبة {m('x > 0')}، ما القيمة الصغرى للمقدار {m(f'x^3 + \\frac{{{c_num}}}{{x}}')}؟",
            ans, [3 * (M_v ** 3), ans - 4, ans + 4, c_num + 1],
            f"To cancel {m('x^3')}, split {m(f'\\frac{{{c_num}}}{{x}}')} into **three** equal terms {m(f'\\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}}')} and use **4-term AM-GM**!",
            f"لإلغاء {m('x^3')}، جزّئ الكسر إلى **ثلاثة** حدود متساوية {m(f'\\frac{{{p_num}}}{{x}}')} وطبّق متباينة **AM-GM لأربعة حدود**!",
            f"Match exponent {m('3')} against three copies of {m('x^{-1}')} via 4-term AM-GM!",
            [
                f"Rewrite as four positive terms: {m(f'x^3 + \\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}}')}.",
                f"By 4-term AM-GM, the sum is at least {m(f'4\\sqrt[4]{{x^3 \\cdot \\left(\\frac{{{p_num}}}{{x}}\\right)^3}} = 4\\sqrt[4]{{{M_v}^{{12}}}} = 4 \\times {M_v**3} = {ans}')}.",
                f"Equality occurs when {m(f'x^3 = \\frac{{{p_num}}}{{x}} \\iff x^4 = {p_num} \\iff x = {M_v} > 0')}.",
            ],
            f"Check at {m(f'x = {M_v}')}: {m(f'{M_v**3} + \\frac{{{c_num}}}{{{M_v}}} = {M_v**3} + {3 * M_v**3} = {ans}')}!",
            f"نحتاج إلى ثلاث نسخ من المقام {m('x')} لموازنة البسط {m('x^3')} عبر متباينة الوسطين الرباعية!",
            [
                f"نكتب المقدار كمجموع أربعة حدود موجبة: {m(f'x^3 + \\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}} + \\frac{{{p_num}}}{{x}}')}.",
                f"بتطبيق AM-GM الرباعية: المجموع {m(f'\\ge 4\\sqrt[4]{{{p_num}^3}} = 4({M_v**3}) = {ans}')}.",
                f"تتحقق المساواة عند {m(f'x = {M_v}')}.",
            ],
            f"تحقق: التعويض بـ {m(f'x = {M_v}')} يعطي {m(ans)} فعلاً!",
            diagram_en=svg_area_identity_square("x³", f"{p_num}/x"),
        )

    for ra, rb in [(2, 3), (3, 5)]:
        a_v, b_v = ra * ra, rb * rb
        ans = (ra + rb) ** 2
        B.add_math(
            tp, "Hard", bp,
            f"For all positive real numbers {m('x, y > 0')}, find the minimum possible value of {m(f'\\left(x + \\frac{{{a_v}}}{{y}}\\right)\\!\\left(y + \\frac{{{b_v}}}{{x}}\\right)')}.",
            f"لجميع الأعداد الحقيقية الموجبة {m('x, y > 0')}، أوجد أصغر قيمة ممكنة لحاصل الضرب {m(f'\\left(x + \\frac{{{a_v}}}{{y}}\\right)\\!\\left(y + \\frac{{{b_v}}}{{x}}\\right)')}.",
            ans, [a_v + b_v, ans - 2 * ra * rb, 4 * ra * rb, ans + 4],
            f"Caution: applying AM-GM inside each parenthesis separately gives **incompatible** equality conditions! **Expand** the product first!",
            f"تنبيه: تطبيق AM-GM على كل قوس منفرداً يعطي شرطي مساواة متعارضين! **فكّ الأقواس أولاً** ثم طبّق AM-GM!",
            f"Expand first to isolate {m('xy + \\frac{' + str(a_v*b_v) + '}{xy}')}, avoiding the mismatched-equality trap!",
            [
                f"Expand: {m(f'\\left(x + \\frac{{{a_v}}}{{y}}\\right)\\!\\left(y + \\frac{{{b_v}}}{{x}}\\right) = xy + {b_v} + {a_v} + \\frac{{{a_v * b_v}}}{{xy}}')}.",
                f"Apply AM-GM to {m(f'xy + \\frac{{{a_v * b_v}}}{{xy}} \\ge 2\\sqrt{{{a_v * b_v}}} = {2 * ra * rb}')}.",
                f"Add {m(f'{a_v} + {b_v}')}: minimum is {m(f'{a_v} + {b_v} + {2*ra*rb} = ({ra} + {rb})^2 = {ans}')}, attained whenever {m(f'xy = {ra * rb}')}!",
            ],
            f"Trap check: separate AM-GM gives {m(f'2\\sqrt{{{a_v}x/y}} \\cdot 2\\sqrt{{{b_v}y/x}} = {4*ra*rb}')}, which is strictly too small because {m(f'xy = {a_v}')} and {m(f'xy = {b_v}')} cannot hold simultaneously!",
            f"نفكّ الأقواس أولاً لتجنب تعارض شروط المساواة بين القوسين!",
            [
                f"بفك الضرب نجد: {m(f'xy + \\frac{{{a_v * b_v}}}{{xy}} + {a_v + b_v}')}.",
                f"بمتباينة AM-GM: {m(f'xy + \\frac{{{a_v * b_v}}}{{xy}} \\ge 2\\sqrt{{{a_v * b_v}}} = {2 * ra * rb}')}.",
                f"بإضافة {m(a_v + b_v)} نحصل على القيمة الصغرى الدقيقة {m(ans)} (وتتحقق عند {m(f'xy = {ra * rb}')}).",
            ],
            f"تحقق: عند {m(f'x = {ra},\\; y = {rb}')} نحصل على {m(f'({ra} + {a_v}/{rb})({rb} + {b_v}/{ra})')}... لا، عند {m(f'x = 1,\\; y = {ra*rb}')}: {m(f'(1 + {ra}/{rb})({ra*rb} + {rb*rb}) = ({ra+rb})^2 = {ans}')}!",
            diagram_en=svg_area_identity_square(str(ra), str(rb)),
        )

    # 19. nsmo_g10_titu_cauchy_schwarz (5E, 6M, 4H)
    bp = "nsmo_g10_titu_cauchy_schwarz"
    # Easy (5): a^2/x + b^2/y with x + y = S
    easy_titu = [
        (2, 3, 5),     # (2+3)^2 / 5 = 5
        (3, 5, 16),    # 64 / 16 = 4
        (4, 6, 20),    # 100 / 20 = 5 -> vary: S=10 -> 100/10 = 10!
        (3, 6, 9),     # 81 / 9 = 9
        (5, 7, 18),    # 144 / 18 = 8
    ]
    easy_titu[2] = (4, 6, 10)
    for a_t, b_t, S_t in easy_titu:
        ans = ((a_t + b_t) ** 2) // S_t
        assert ((a_t + b_t) ** 2) % S_t == 0
        B.add_math(
            tp, "Easy", bp,
            f"Positive real numbers {m('x, y')} satisfy {m(f'x + y = {S_t}')}. What is the minimum value of {m(f'\\frac{{{a_t*a_t}}}{{x}} + \\frac{{{b_t*b_t}}}{{y}}')}?",
            f"عددان حقيقيان موجبان {m('x, y')} يحققان {m(f'x + y = {S_t}')}. ما أصغر قيمة للمقدار {m(f'\\frac{{{a_t*a_t}}}{{x}} + \\frac{{{b_t*b_t}}}{{y}}')}؟",
            ans, [ans - 1, ans + 2, (a_t * a_t + b_t * b_t) // 2, ans + 4],
            f"Apply Titu's Lemma: {m('\\frac{a^2}{x} + \\frac{b^2}{y} \\ge \\frac{(a + b)^2}{x + y}')}!",
            f"طبّق لمة تيتو: {m('\\frac{a^2}{x} + \\frac{b^2}{y} \\ge \\frac{(a + b)^2}{x + y}')}!",
            f"Use Titu's Lemma (Cauchy-Schwarz in Engel form) with numerators {m(f'{a_t}^2')} and {m(f'{b_t}^2')}!",
            [
                f"Write {m(f'\\frac{{{a_t}^2}}{{x}} + \\frac{{{b_t}^2}}{{y}} \\ge \\frac{{({a_t} + {b_t})^2}}{{x + y}}')}.",
                f"Substitute {m(f'x + y = {S_t}')}: {m(f'\\frac{{{a_t + b_t}^2}}{{{S_t}}} = \\frac{{{(a_t+b_t)**2}}}{{{S_t}}} = {ans}')}.",
                f"Equality holds when {m(f'\\frac{{x}}{{{a_t}}} = \\frac{{y}}{{{b_t}}}')}, which has a positive solution summing to {m(S_t)}.",
            ],
            f"Check: at proportional split {m(f'x = \\frac{{{a_t * S_t}}}{{{a_t + b_t}}},\\; y = \\frac{{{b_t * S_t}}}{{{a_t + b_t}}}')}, the sum equals exact {m(ans)}!",
            f"نطبّق لمة تيتو (صورة إنجل لمتباينة كوشي-شوارتز) مباشرة!",
            [
                f"نكتب البسطين كمربعين: {m(f'\\frac{{{a_t}^2}}{{x}} + \\frac{{{b_t}^2}}{{y}} \\ge \\frac{{({a_t} + {b_t})^2}}{{x + y}}')}.",
                f"بالتعويض عن {m(f'x + y = {S_t}')} نحصل على {m(f'\\frac{{{(a_t+b_t)**2}}}{{{S_t}}} = {ans}')}.",
            ],
            f"تحقق: تتحقق المساواة عند تقسيم {m(S_t)} بنسبة {m(f'{a_t} : {b_t}')}.",
        )

    # Medium (6): 3-term Titu a^2/x + b^2/y + c^2/z with x + y + z = S (distinct from (2,3,6), S=11!)
    med_titu = [
        (1, 2, 3, 12),   # 36 / 12 = 3
        (2, 3, 5, 20),   # 100 / 20 = 5
        (1, 3, 4, 16),   # 64 / 16 = 4
        (2, 4, 6, 8),    # 144 / 8 = 18
        (3, 4, 5, 9),    # 144 / 9 = 16
        (2, 5, 7, 14),   # 196 / 14 = 14
    ]
    for a_t, b_t, c_t, S_t in med_titu:
        tot_sq = (a_t + b_t + c_t) ** 2
        assert tot_sq % S_t == 0
        ans = tot_sq // S_t
        B.add_math(
            tp, "Medium", bp,
            f"Positive real numbers {m('x, y, z')} satisfy {m(f'x + y + z = {S_t}')}. Find the minimum possible value of {m(f'\\frac{{{a_t*a_t}}}{{x}} + \\frac{{{b_t*b_t}}}{{y}} + \\frac{{{c_t*c_t}}}{{z}}')}.",
            f"أعداد حقيقية موجبة {m('x, y, z')} تحقق {m(f'x + y + z = {S_t}')}. أوجد القيمة الصغرى للمقدار {m(f'\\frac{{{a_t*a_t}}}{{x}} + \\frac{{{b_t*b_t}}}{{y}} + \\frac{{{c_t*c_t}}}{{z}}')}.",
            ans, [ans - 2, ans + 2, ans + 4, (a_t + b_t + c_t)],
            f"Apply 3-term Titu's Lemma: {m('\\frac{a^2}{x} + \\frac{b^2}{y} + \\frac{c^2}{z} \\ge \\frac{(a + b + c)^2}{x + y + z}')}.",
            f"طبّق لمة تيتو لثلاثة كسور: {m('\\frac{a^2}{x} + \\frac{b^2}{y} + \\frac{c^2}{z} \\ge \\frac{(a + b + c)^2}{x + y + z}')}.",
            f"Recognize the numerators {m(f'{a_t}^2, {b_t}^2, {c_t}^2')} and apply Titu's Lemma in one step!",
            [
                f"By Titu's Lemma for {m('x, y, z > 0')}: {m(f'\\frac{{{a_t}^2}}{{x}} + \\frac{{{b_t}^2}}{{y}} + \\frac{{{c_t}^2}}{{z}} \\ge \\frac{{({a_t} + {b_t} + {c_t})^2}}{{x + y + z}}')}.",
                f"Substitute {m(f'x + y + z = {S_t}')}: {m(f'\\frac{{{tot_sq}}}{{{S_t}}} = {ans}')}.",
                f"Equality is achieved when {m(f'x : y : z = {a_t} : {b_t} : {c_t}')}.",
            ],
            f"Check: proportional positive values {m('x, y, z')} summing to {m(S_t)} attain {m(ans)} exactly!",
            f"نطبّق لمة تيتو الثلاثية مباشرة بعد أخذ الجذور التربيعية للبسوط!",
            [
                f"من لمة تيتو: المجموع أكبر من أو يساوي {m(f'\\frac{{({a_t} + {b_t} + {c_t})^2}}{{x + y + z}}')}.",
                f"بالتعويض عن {m(f'x + y + z = {S_t}')} نحصل على {m(f'\\frac{{{tot_sq}}}{{{S_t}}} = {ans}')}.",
            ],
            f"تحقق: تتحقق المساواة عندما تتناسب المتغيرات بنسبة {m(f'{a_t} : {b_t} : {c_t}')}.",
        )

    # Hard (4): Weighted constraint x + 2y + 3z = S OR shifted denominators (x+1), (y+2), (z+3)!
    # Let's do 2 weighted constraints x + 2y + 3z = S and 2 shifted denominators!
    # Weighted: A/x + B/y + C/z = u^2/x + v^2/(2y) + w^2/(3z) -> so B = v^2 / 2 (pick even v!), C = w^2 / 3 (pick w multiple of 3!)
    # Check v=4 -> v^2/2 = 8; w=6 -> w^2/3 = 12; u=2 -> u^2 = 4: 4/x + 8/y + 12/z = 2^2/x + 4^2/(2y) + 6^2/(3z) >= (2+4+6)^2 / (x+2y+3z) = 144 / S!! SO CLEAN!
    for u_w, v_w, w_w, S_w in [(2, 4, 6, 12), (3, 6, 9, 18)]:
        n1, n2, n3 = u_w * u_w, (v_w * v_w) // 2, (w_w * w_w) // 3
        tot_sq = (u_w + v_w + w_w) ** 2
        ans = tot_sq // S_w
        B.add_math(
            tp, "Hard", bp,
            f"Positive real numbers {m('x, y, z')} satisfy {m(f'x + 2y + 3z = {S_w}')}. Find the minimum value of {m(f'\\frac{{{n1}}}{{x}} + \\frac{{{n2}}}{{y}} + \\frac{{{n3}}}{{z}}')}.",
            f"أعداد حقيقية موجبة {m('x, y, z')} تحقق {m(f'x + 2y + 3z = {S_w}')}. أوجد القيمة الصغرى للمقدار {m(f'\\frac{{{n1}}}{{x}} + \\frac{{{n2}}}{{y}} + \\frac{{{n3}}}{{z}}')}.",
            ans, [ans - 2, ans + 3, (n1 + n2 + n3) // 2, ans + 6],
            f"Scale the second fraction by {m('\\frac{2}{2}')} and the third by {m('\\frac{3}{3}')} so the denominators become {m('x,\\; 2y,\\; 3z')}!",
            f"اضرب الكسر الثاني في {m('\\frac{2}{2}')} والثالث في {m('\\frac{3}{3}')} لتصبح المقامات {m('x,\\; 2y,\\; 3z')} مطابقة للشرط!",
            f"Match the constraint {m('x + 2y + 3z')} by rewriting the fractions with denominators {m('x')}, {m('2y')}, and {m('3z')}!",
            [
                f"Rewrite {m(f'\\frac{{{n1}}}{{x}} + \\frac{{{2*n2}}}{{2y}} + \\frac{{{3*n3}}}{{3z}} = \\frac{{{u_w}^2}}{{x}} + \\frac{{{v_w}^2}}{{2y}} + \\frac{{{w_w}^2}}{{3z}}')}.",
                f"Apply Titu's Lemma: the sum is at least {m(f'\\frac{{({u_w} + {v_w} + {w_w})^2}}{{x + 2y + 3z}} = \\frac{{{tot_sq}}}{{{S_w}}} = {ans}')}.",
                f"Equality holds when {m(f'\\frac{{x}}{{{u_w}}} = \\frac{{2y}}{{{v_w}}} = \\frac{{3z}}{{{w_w}}}')}, giving positive {m('x, y, z')}.",
            ],
            f"Check equality point: {m('x, 2y, 3z')} split {m(S_w)} in ratio {m(f'{u_w}:{v_w}:{w_w}')}, yielding exact sum {m(ans)}!",
            f"نوحّد شكل المقامات لتطابق الشرط {m('x + 2y + 3z')} قبل تطبيق لمة تيتو!",
            [
                f"نعيد كتابة المجموع بالصورة {m(f'\\frac{{{u_w}^2}}{{x}} + \\frac{{{v_w}^2}}{{2y}} + \\frac{{{w_w}^2}}{{3z}}')}.",
                f"بلمة تيتو: المجموع {m(f'\\ge \\frac{{({u_w} + {v_w} + {w_w})^2}}{{x + 2y + 3z}} = \\frac{{{tot_sq}}}{{{S_w}}} = {ans}')}.",
            ],
            f"تحقق: توسيع الكسرين الثاني والثالث هو المفتاح الذهبي لمطابقة المعاملات {m('1, 2, 3')}!",
        )

    for a_s, b_s, c_s, S_base in [(2, 3, 5, 14), (3, 4, 5, 18)]:
        # Denominators (x + 1), (y + 2), (z + 3) with x, y, z > 0 and x + y + z = S_base -> Denom sum = S_base + 6!
        # MUST check that equality x+1, y+2, z+3 gives STRICTLY POSITIVE x, y, z > 0!!
        D_sum = S_base + 6
        tot_u = a_s + b_s + c_s
        assert (tot_u * tot_u) % D_sum == 0
        # Check x = a_s * D_sum / tot_u - 1 > 0, y > 0, z > 0!
        assert a_s * D_sum > tot_u * 1 and b_s * D_sum > tot_u * 2 and c_s * D_sum > tot_u * 3
        ans = (tot_u * tot_u) // D_sum
        B.add_math(
            tp, "Hard", bp,
            f"Positive real numbers {m('x, y, z > 0')} satisfy {m(f'x + y + z = {S_base}')}. Find the minimum value of {m(f'\\frac{{{a_s*a_s}}}{{x + 1}} + \\frac{{{b_s*b_s}}}{{y + 2}} + \\frac{{{c_s*c_s}}}{{z + 3}}')}.",
            f"أعداد حقيقية موجبة {m('x, y, z > 0')} تحقق {m(f'x + y + z = {S_base}')}. أوجد القيمة الصغرى للمقدار {m(f'\\frac{{{a_s*a_s}}}{{x + 1}} + \\frac{{{b_s*b_s}}}{{y + 2}} + \\frac{{{c_s*c_s}}}{{z + 3}}')}.",
            ans, [ans - 1, ans + 1, (tot_u * tot_u) // S_base, ans + 3],
            f"Sum the shifted denominators directly: {m(f'(x + 1) + (y + 2) + (z + 3) = {S_base} + 6 = {D_sum}')}, and verify {m('x, y, z > 0')} at equality!",
            f"اجمع المقامات المزاحة مباشرة: {m(f'(x + 1) + (y + 2) + (z + 3) = {S_base} + 6 = {D_sum}')}، وتحقق أن {m('x, y, z > 0')} عند المساواة!",
            f"Apply Titu's Lemma to the shifted denominators whose sum is {m(f'{S_base} + 1 + 2 + 3 = {D_sum}')}!",
            [
                f"Notice {m(f'(x + 1) + (y + 2) + (z + 3) = (x + y + z) + 6 = {D_sum}')}.",
                f"By Titu's Lemma, {m(f'\\frac{{{a_s}^2}}{{x+1}} + \\frac{{{b_s}^2}}{{y+2}} + \\frac{{{c_s}^2}}{{z+3}} \\ge \\frac{{({a_s} + {b_s} + {c_s})^2}}{{{D_sum}}} = \\frac{{{tot_u*tot_u}}}{{{D_sum}}} = {ans}')}.",
                f"Verify positivity at equality: {m(f'x + 1 = {a_s * D_sum // tot_u} > 1')}, {m(f'y + 2 = {b_s * D_sum // tot_u} > 2')}, and {m(f'z + 3 = {c_s * D_sum // tot_u} > 3')}, so {m('x, y, z > 0')}!",
            ],
            f"Domain check: {m(f'(x, y, z) = ({a_s*D_sum//tot_u - 1},\\; {b_s*D_sum//tot_u - 2},\\; {c_s*D_sum//tot_u - 3})')} are all positive and sum to {m(S_base)}!",
            f"نطبّق لمة تيتو على المقامات المزاحة بعد حساب مجموعها الكلي {m(D_sum)} والتحقق من موجبية المتغيرات!",
            [
                f"مجموع المقامات الثلاثة يساوي {m(f'{S_base} + 1 + 2 + 3 = {D_sum}')}.",
                f"بلمة تيتو: المجموع {m(f'\\ge \\frac{{({a_s}+{b_s}+{c_s})^2}}{{{D_sum}}} = {ans}')}.",
                f"نتحقق من نقطة المساواة فنجد {m(f'x = {a_s*D_sum//tot_u - 1} > 0')} و{m(f'y = {b_s*D_sum//tot_u - 2} > 0')} و{m(f'z = {c_s*D_sum//tot_u - 3} > 0')}!",
            ],
            f"تحقق: جميع المتغيرات الثلاثة موجبة تماماً عند نقطة المساواة.",
        )

    # 20. nsmo_g10_manhattan_lattice_region (5E, 6M, 4H) — SVG: svg_coord_diamond
    bp = "nsmo_g10_manhattan_lattice_region"
    # Easy (5): Area of |x - a| + |y - b| <= R -> 2 * R^2
    easy_man = [(4, 1, -2), (6, -3, 4), (7, 2, 5), (9, -4, -1), (11, 5, -3)]
    for R_m, a_m, b_m in easy_man:
        ans = 2 * R_m * R_m
        x_part = f"|x - {a_m}|" if a_m > 0 else f"|x + {-a_m}|"
        y_part = f"|y - {b_m}|" if b_m > 0 else f"|y + {-b_m}|"
        B.add_math(
            tp, "Easy", bp,
            f"In the coordinate plane, what is the **area** of the region defined by {m(f'{x_part} + {y_part} \\le {R_m}')}?",
            f"في المستوى الإحداثي، ما **مساحة** المنطقة المعرّفة بالمتباينة {m(f'{x_part} + {y_part} \\le {R_m}')}؟",
            ans, [R_m * R_m, 4 * R_m * R_m, 2 * R_m * R_m + 2 * R_m + 1, ans // 2 + R_m],
            f"Translation doesn't change area! The diamond {m(f'|u| + |v| \\le {R_m}')} has perpendicular diagonals of length {m(2 * R_m)} and {m(2 * R_m)}.",
            f"الإزاحة لا تغيّر المساحة! المعين {m(f'|u| + |v| \\le {R_m}')} قطراه متعامدان وطول كل منهما {m(2 * R_m)}.",
            f"Center at the origin: {m(f'|u| + |v| \\le {R_m}')} is a tilted square of diagonal {m(2 * R_m)}, so its area is {m(f'\\frac{{1}}{{2}}(2R)(2R) = 2R^2')}!",
            [
                f"Shift {m(f'u = x - ({a_m}),\\; v = y - ({b_m})')}: area matches {m(f'|u| + |v| \\le {R_m}')}.",
                f"Vertices lie at {m(f'(\\pm {R_m}, 0)')} and {m(f'(0, \\pm {R_m})')}, forming a rhombus with diagonals {m(2 * R_m)} and {m(2 * R_m)}.",
                f"Area {m(f'= \\frac{{1}}{{2}}({2*R_m})({2*R_m}) = 2({R_m}^2) = {ans}')}.",
            ],
            f"Quadrant check: each of the {m('4')} right triangles has legs {m(R_m)} and {m(R_m)}, giving {m(f'4 \\times \\frac{{1}}{{2}}({R_m}^2) = {ans}')}!",
            f"ننقل المركز إلى نقطة الأصل فنحصل على مربع مائل قطراه {m(2 * R_m)} ومساحته {m('2R^2')}!",
            [
                f"الإزاحة تحافظ على المساحة فندرس {m(f'|u| + |v| \\le {R_m}')}.",
                f"الرؤوس هي {m(f'(\\pm {R_m}, 0)')} و{m(f'(0, \\pm {R_m})')}، وطول كل قطر {m(2 * R_m)}.",
                f"المساحة تساوي {m(f'\\frac{{1}}{{2}} \\times {2*R_m} \\times {2*R_m} = {ans}')}.",
            ],
            f"تحقق: تتكوّن المنطقة من {m('4')} مثلثات قائمة متطابقة مساحة كل منها {m(f'{R_m}^2/2')} ومجموعها {m(ans)}.",
            diagram_en=svg_coord_diamond(str(R_m)),
        )

    # Medium (6): Integer lattice point count R^2 + (R+1)^2 for R in {4, 6, 7, 8, 9, 10}
    med_man = [(4, 2, -1), (6, -3, 2), (7, 1, 4), (8, -2, -5), (9, 4, -3), (10, -1, 6)]
    for R_m, a_m, b_m in med_man:
        ans = R_m * R_m + (R_m + 1) ** 2
        assert ans == sum(
            1 for u in range(-R_m, R_m + 1) for v in range(-R_m, R_m + 1) if abs(u) + abs(v) <= R_m
        )
        x_part = f"|x - {a_m}|" if a_m > 0 else f"|x + {-a_m}|"
        y_part = f"|y - {b_m}|" if b_m > 0 else f"|y + {-b_m}|"
        B.add_math(
            tp, "Medium", bp,
            f"How many ordered pairs of integers {m('(x, y) \\in \\mathbb{Z}^2')} satisfy {m(f'{x_part} + {y_part} \\le {R_m}')}?",
            f"كم زوجاً مرتباً من الأعداد الصحيحة {m('(x, y) \\in \\mathbb{Z}^2')} يحقق المتباينة {m(f'{x_part} + {y_part} \\le {R_m}')}؟",
            ans, [2 * R_m * R_m, ans - 1, (R_m + 1) ** 2, ans + 2 * R_m],
            f"Shift by integers {m(f'({a_m}, {b_m})')} and use the centered-square formula {m('R^2 + (R + 1)^2')}!",
            f"أزح المركز الصحيح واستخدم صيغة مجموع المربعين المتتاليين {m('R^2 + (R + 1)^2')}!",
            f"An integer shift preserves the lattice {m('\\mathbb{Z}^2')}, so count {m(f'|u| + |v| \\le {R_m}')} via {m('R^2 + (R + 1)^2')}!",
            [
                f"Set {m(f'u = x - ({a_m})')} and {m(f'v = y - ({b_m})')}; we count integer pairs with {m(f'|u| + |v| \\le {R_m}')}.",
                f"Apply the lattice-diamond formula: {m(f'{R_m}^2 + ({R_m} + 1)^2 = {R_m*R_m} + {(R_m+1)**2} = {ans}')}.",
            ],
            f"Parity check: {m('R^2 + (R + 1)^2 = 2R^2 + 2R + 1')} is always odd (because of the single center point), matching {m(ans)}!",
            f"الإزاحة بأعداد صحيحة تحافظ على الشبكة الصحيحة، فنطبّق الصيغة {m('R^2 + (R + 1)^2')} مباشرة!",
            [
                f"نضع {m(f'u = x - ({a_m})')} و{m(f'v = y - ({b_m})')} فنحصل على {m(f'|u| + |v| \\le {R_m}')}.",
                f"نحسب عدد النقاط الصحيحة: {m(f'{R_m}^2 + ({R_m} + 1)^2 = {R_m*R_m} + {(R_m+1)**2} = {ans}')}.",
            ],
            f"تحقق: العدد فردي دائماً لوجود نقطة المركز الفردية مقترنة بأزواج متناظرة.",
            diagram_en=svg_coord_diamond(str(R_m)),
        )

    # Hard (4): 2 Manhattan shells r <= |x| + |y| <= R AND 2 weighted Manhattan diamonds a|x| + b|y| <= M!
    for r_in, R_out in [(3, 6), (4, 8)]:
        c_out = R_out * R_out + (R_out + 1) ** 2
        c_in_strict = (r_in - 1) ** 2 + r_in * r_in
        ans = c_out - c_in_strict
        assert ans == sum(
            1 for x in range(-R_out, R_out + 1) for y in range(-R_out, R_out + 1) if r_in <= abs(x) + abs(y) <= R_out
        )
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered pairs of integers {m('(x, y)')} satisfy the double inequality {m(f'{r_in} \\le |x| + |y| \\le {R_out}')}?",
            f"كم زوجاً مرتباً من الأعداد الصحيحة {m('(x, y)')} يحقق المتباينة المزدوجة {m(f'{r_in} \\le |x| + |y| \\le {R_out}')}؟",
            ans, [c_out - (r_in * r_in + (r_in + 1) ** 2), ans + 4 * r_in, ans - 4, c_out],
            f"Careful at the inner boundary! Subtract points with {m(f'|x| + |y| \\le {r_in - 1}')}, **not** {m(f'\\le {r_in}')}!",
            f"انتبه للحد الداخلي! اطرح النقاط التي تحقق {m(f'|x| + |y| \\le {r_in - 1}')} **وليس** {m(f'\\le {r_in}')}!",
            f"Subtract the strict interior diamond {m(f'|x| + |y| \\le {r_in - 1}')} from the outer diamond {m(f'|x| + |y| \\le {R_out}')}!",
            [
                f"Points with {m(f'|x| + |y| \\le {R_out}')}: {m(f'{R_out}^2 + {R_out + 1}^2 = {c_out}')}.",
                f"Excluded points satisfy {m(f'|x| + |y| < {r_in} \\iff |x| + |y| \\le {r_in - 1}')}, which gives {m(f'{r_in - 1}^2 + {r_in}^2 = {c_in_strict}')}.",
                f"Subtract: {m(f'{c_out} - {c_in_strict} = {ans}')}.",
            ],
            f"Shell-sum check: each ring {m('|x| + |y| = k')} ({m('k \\ge 1')}) has {m('4k')} lattice points, and {m('\\sum_{k=' + str(r_in) + '}^{' + str(R_out) + '} 4k = ' + str(ans))}!",
            f"نطرح المعين الداخلي الأصغر تماماً {m(f'|x| + |y| \\le {r_in - 1}')} للاحتفاظ بنقاط الحدود {m(f'|x| + |y| = {r_in}')}!",
            [
                f"عدد نقاط المعين الخارجي {m(f'\\le {R_out}')} هو {m(f'{R_out}^2 + {R_out+1}^2 = {c_out}')}.",
                f"النقاط المستبعدة تحقق {m(f'|x| + |y| \\le {r_in - 1}')} وعددها {m(f'{r_in - 1}^2 + {r_in}^2 = {c_in_strict}')}.",
                f"بالطرح نحصل على {m(f'{c_out} - {c_in_strict} = {ans}')}.",
            ],
            f"تحقق عبر الحلقات: كل حلقة {m('|x| + |y| = k')} تحتوي على {m('4k')} نقاط صحيحة، ومجموعها من {m(r_in)} إلى {m(R_out)} يساوي {m(ans)}!",
            diagram_en=svg_coord_diamond(f"{r_in}..{R_out}"),
        )

    for a_w, M_w in [(2, 8), (3, 9)]:
        # Count integer pairs (x, y) with a_w * |x| + |y| <= M_w
        ans = sum(
            1 for x in range(-M_w, M_w + 1) for y in range(-M_w, M_w + 1) if a_w * abs(x) + abs(y) <= M_w
        )
        max_x = M_w // a_w
        B.add_math(
            tp, "Hard", bp,
            f"How many ordered pairs of integers {m('(x, y)')} satisfy {m(f'{a_w}|x| + |y| \\le {M_w}')}?",
            f"كم زوجاً مرتباً من الأعداد الصحيحة {m('(x, y)')} يحقق المتباينة الموزونة {m(f'{a_w}|x| + |y| \\le {M_w}')}؟",
            ans, [ans - 2, ans + 4, M_w * M_w // a_w, ans - (2 * M_w + 1)],
            f"Slice vertically by {m(f'x \\in \\{{-{max_x}, \\dots, {max_x}\\}}')}: for each {m('x')}, {m('|y| \\le ' + str(M_w) + ' - ' + str(a_w) + '|x|')} gives {m(f'2({M_w} - {a_w}|x|) + 1')} choices!",
            f"قسّم عمودياً حسب قيم {m(f'x \\in \\{{-{max_x}, \\dots, {max_x}\\}}')}؛ لكل قيمة {m('x')} يوجد {m(f'2({M_w} - {a_w}|x|) + 1')} خياراً لـ {m('y')}!",
            f"Count column by column across {m(f'|x| \\le {max_x}')}, using symmetry between {m('+x')} and {m('-x')}!",
            [
                f"Since {m(f'{a_w}|x| \\le {M_w}')}, {m('|x|')} can only take values {m(f'0, 1, \\dots, {max_x}')}.",
                f"At {m('x = 0')}, {m(f'|y| \\le {M_w}')} gives {m(2 * M_w + 1)} points. For each {m(f'k = 1, \\dots, {max_x}')}, {m('x = \\pm k')} gives {m(f'2 \\times [2({M_w} - {a_w}k) + 1]')} points.",
                f"Summing across all {m(2 * max_x + 1)} columns gives exact {m(ans)} integer pairs.",
            ],
            f"Parity check: {m('x = 0')} has odd count {m(2 * M_w + 1)}, and nonzero columns come in symmetric {m('\\pm k')} pairs, confirming odd total {m(ans)}!",
            f"نحصي عدد قيم {m('y')} الصحيحة لكل عمود {m('x')} مع استثمار التناظر حول المحور الصادي!",
            [
                f"قيم {m('|x|')} الممكنة هي فقط {m(f'0, 1, \\dots, {max_x}')}.",
                f"عند {m('x = 0')} يوجد {m(2 * M_w + 1)} نقطة، ولكل {m(f'k \\in \\{{1, \\dots, {max_x}\\}}')} يعطي الزوج {m('x = \\pm k')} عدد {m(f'2[2({M_w} - {a_w}k) + 1]')} نقطة.",
                f"بجمع جميع الأعمدة نحصل على {m(ans)} زوجاً صحيحاً.",
            ],
            f"تحقق: التناظر الزوجي للأعمدة الجانبية مع العمود الأوسط الفردي يعطي المجموع الدقيق {m(ans)}.",
            diagram_en=svg_coord_diamond(f"{M_w}/{a_w},{M_w}"),
        )



# =============================================================================
# UNIT 3.5 — Power of a Point, Cyclic Quads, Bisectors, Medians & Inradius (75 Qs)
# =============================================================================
def _add_unit_3_5(B: BankBuilder) -> None:
    tp = "Geometry"

    # 21. nsmo_g10_power_of_point_chords_secants (5E, 6M, 4H)
    bp = "nsmo_g10_power_of_point_chords_secants"
    easy_pop = [
        # (ae, eb, ce) -> ed = ae*eb//ce, ask CD = ce + ed
        (6, 10, 4),    # ed = 15 -> CD = 19
        (8, 9, 6),     # ed = 12 -> CD = 18
        (5, 16, 8),    # ed = 10 -> CD = 18? Vary: (9, 10, 5) -> ed = 18 -> CD = 23!
        (12, 7, 6),    # ed = 14 -> CD = 20
        (10, 14, 7),   # ed = 20 -> CD = 27
    ]
    easy_pop[2] = (9, 10, 5)
    for ae, eb, ce in easy_pop:
        ed = (ae * eb) // ce
        assert ae * eb == ce * ed
        ans = ce + ed
        B.add_math(
            tp, "Easy", bp,
            f"Two chords {m('AB')} and {m('CD')} intersect inside a circle at point {m('E')}. If {m(f'AE = {ae}')}, {m(f'EB = {eb}')}, and {m(f'CE = {ce}')}, what is the total length of chord {m('CD')}?",
            f"يتقاطع الوتران {m('AB')} و{m('CD')} داخل دائرة في النقطة {m('E')}. إذا كان {m(f'AE = {ae}')} و{m(f'EB = {eb}')} و{m(f'CE = {ce}')}، فما الطول الكلي للوتر {m('CD')}؟",
            ans, [ed, ae + eb, ans + 2, ed - ce if ed > ce else ans - 3],
            f"First find {m('ED')} from {m('AE \\cdot EB = CE \\cdot ED')}, then add {m('CD = CE + ED')}!",
            f"أوجد {m('ED')} أولاً من قانون الأوتار المتقاطعة {m('AE \\cdot EB = CE \\cdot ED')}، ثم اجمع {m('CD = CE + ED')}!",
            f"Apply Power of a Point for intersecting chords, and remember to add {m('CE + ED')} for the full chord!",
            [
                f"By the Intersecting Chords Theorem, {m(f'AE \\cdot EB = CE \\cdot ED \\implies {ae} \\times {eb} = {ce} \\cdot ED')}.",
                f"Solve for {m(f'ED = \\frac{{{ae * eb}}}{{{ce}}} = {ed}')}.",
                f"Add the two segments: {m(f'CD = CE + ED = {ce} + {ed} = {ans}')}.",
            ],
            f"Trap check: {m(ed)} is only {m('ED')}; the full chord length {m('CD')} is {m(f'{ce} + {ed} = {ans}')}!",
            f"نطبّق مبرهنة الأوتار المتقاطعة لإيجاد {m('ED')} ثم نضيف {m('CE')} للحصول على طول الوتر كاملاً!",
            [
                f"من قوة النقطة {m('E')}: {m(f'{ae} \\times {eb} = {ce} \\times ED \\implies ED = {ed}')}.",
                f"طول الوتر الكلي يساوي {m(f'CD = {ce} + {ed} = {ans}')}.",
            ],
            f"تحقق: لا تتوقف عند {m(f'ED = {ed}')}؛ المطلوب طول الوتر الكلي {m(f'CD = {ans}')}!",
            diagram_en=svg_circle_chords(str(ae), str(eb), str(ce), "?"),
        )

    # Medium (6): Tangent-secant PT^2 = PA * (PA + AB)
    med_pop = [
        # (pt, pa, ab, ask_which)
        (6, 4, 5, "AB"),     # 36 = 4*9 -> given PT=6, PA=4, find AB=5
        (10, 5, 15, "AB"),   # 100 = 5*20 -> given PT=10, PA=5, find AB=15
        (15, 9, 16, "AB"),   # 225 = 9*25 -> given PT=15, PA=9, find AB=16
        (8, 4, 12, "PT"),    # given PA=4, AB=12 -> PT = sqrt(4*16) = 8
        (12, 9, 7, "PT"),    # given PA=9, AB=7 -> PT = sqrt(9*16) = 12
        (10, 4, 21, "PA"),   # given PT=10, AB=21 -> PA(PA+21) = 100 -> PA = 4!
    ]
    for pt_v, pa_v, ab_v, ask_w in med_pop:
        assert pt_v * pt_v == pa_v * (pa_v + ab_v)
        if ask_w == "AB":
            ans = ab_v
            q_en = f"From external point {m('P')}, tangent {m('PT')} to a circle has length {m(pt_v)}, and secant {m('PAB')} satisfies {m(f'PA = {pa_v}')}. Find the chord length {m('AB')}."
            q_ar = f"من نقطة خارجية {m('P')}، رُسم مماس {m('PT')} لدائرة طوله {m(pt_v)}، وقاطع {m('PAB')} يحقق {m(f'PA = {pa_v}')}. أوجد طول الوتر {m('AB')}."
            diag = svg_power_of_point(str(pt_v), str(pa_v), "?")
        elif ask_w == "PT":
            ans = pt_v
            q_en = f"From external point {m('P')}, a secant meets a circle at {m('A')} and {m('B')} with {m(f'PA = {pa_v}')} and {m(f'AB = {ab_v}')}. Find the length of tangent {m('PT')}."
            q_ar = f"من نقطة خارجية {m('P')}، يقطع قاطع دائرةً في {m('A')} و{m('B')} بحيث {m(f'PA = {pa_v}')} و{m(f'AB = {ab_v}')}. أوجد طول المماس {m('PT')}."
            diag = svg_power_of_point("?", str(pa_v), str(ab_v))
        else:
            ans = pa_v
            q_en = f"From external point {m('P')}, tangent {m('PT')} has length {m(pt_v)}, and secant {m('PAB')} cuts off a chord {m(f'AB = {ab_v}')}. Find {m('PA')}."
            q_ar = f"من نقطة خارجية {m('P')}، طول المماس {m(f'PT = {pt_v}')}، ويقتطع القاطع {m('PAB')} وتراً طوله {m(f'AB = {ab_v}')}. أوجد طول {m('PA')}."
            diag = svg_power_of_point(str(pt_v), "?", str(ab_v))
        B.add_math(
            tp, "Medium", bp, q_en, q_ar, ans,
            [pa_v + ab_v, int(math.isqrt(pa_v * ab_v)) if pa_v * ab_v > 0 else ans + 2, ans + 3, max(1, ans - 2)],
            f"Use Tangent-Secant Power of a Point: {m('PT^2 = PA \\cdot PB = PA(PA + AB)')}!",
            f"استخدم علاقة المماس والقاطع: {m('PT^2 = PA \\cdot PB = PA(PA + AB)')}!",
            f"Apply {m('PT^2 = PA \\cdot (PA + AB)')}, always using the **whole secant** {m('PB = PA + AB')}!",
            [
                f"Write Power of a Point from {m('P')}: {m('PT^2 = PA \\cdot (PA + AB)')}.",
                f"Substitute the known lengths into {m(f'{pt_v}^2 = {pa_v} \\times ({pa_v} + {ab_v}) = {pt_v*pt_v}')} to solve for the unknown segment {m(ans)}.",
            ],
            f"Check: {m(f'PA \\cdot PB = {pa_v} \\times {pa_v + ab_v} = {pt_v*pt_v} = {pt_v}^2')}!",
            f"نعوّض في قانون قوة النقطة للمماس والقاطع {m('PT^2 = PA(PA + AB)')} مع استخدام القاطع الكلي!",
            [
                f"القانون الأساسي: {m('PT^2 = PA \\cdot PB = PA(PA + AB)')}.",
                f"بالتعويض بالأطوال المعطاة نجد القيمة المجهولة تساوي {m(ans)}.",
            ],
            f"تحقق: {m(f'{pa_v} \\times ({pa_v} + {ab_v}) = {pt_v}^2')} فعلاً!",
            diagram_en=diag,
        )

    # Hard (4): Circle radius R from interior point distance OP = d and chord split AE, EB: R^2 - d^2 = AE * EB!
    hard_pop = [
        (6, 12, 7, 11),   # ae*eb + d^2 = 72 + 49 = 121 -> R = 11
        (8, 18, 5, 13),   # 144 + 25 = 169 -> R = 13
        (12, 16, 8, 16),  # 192 + 64 = 256 -> R = 16
        (15, 21, 3, 18),  # 315 + 9 = 324 -> R = 18
    ]
    for ae, eb, d_op, R_ans in hard_pop:
        assert ae * eb + d_op * d_op == R_ans * R_ans
        B.add_math(
            tp, "Hard", bp,
            f"Point {m('E')} lies inside a circle with center {m('O')} at distance {m(f'OE = {d_op}')}. A chord {m('AB')} passing through {m('E')} is divided into {m(f'AE = {ae}')} and {m(f'EB = {eb}')}. What is the radius {m('R')} of the circle?",
            f"تقع النقطة {m('E')} داخل دائرة مركزها {m('O')} على بُعد {m(f'OE = {d_op}')}. يمر الوتر {m('AB')} بالنقطة {m('E')} فينقسم إلى {m(f'AE = {ae}')} و{m(f'EB = {eb}')}. ما نصف قطر الدائرة {m('R')}؟",
            R_ans, [R_ans - 2, R_ans + 2, (ae + eb) // 2, R_ans + 4],
            f"Draw the diameter through {m('O')} and {m('E')}: {m('E')} splits that diameter into segments {m('R - OE')} and {m('R + OE')}!",
            f"ارسم القطر المار بـ {m('O')} و{m('E')}؛ تقسم النقطة {m('E')} هذا القطر إلى قطعتين طولاهما {m('R - OE')} و{m('R + OE')}!",
            f"Extend {m('OE')} into a full diameter: Power of {m('E')} gives {m('(R - OE)(R + OE) = R^2 - OE^2 = AE \\cdot EB')}!",
            [
                f"The diameter passing through {m('O')} and {m('E')} is divided by {m('E')} into segments of lengths {m(f'R - {d_op}')} and {m(f'R + {d_op}')}.",
                f"By Power of a Point at {m('E')}, {m(f'(R - {d_op})(R + {d_op}) = AE \\cdot EB = {ae} \\times {eb} = {ae * eb}')}.",
                f"Thus {m(f'R^2 - {d_op}^2 = {ae * eb} \\implies R^2 = {ae * eb + d_op * d_op} \\implies R = {R_ans}')}.",
            ],
            f"Diameter check: chord length is {m(f'{ae + eb}')}, which is strictly less than diameter {m(f'2R = {2 * R_ans}')}!",
            f"بمدّ {m('OE')} ليصبح قطراً في الدائرة نحصل على العلاقة الرائعة {m('R^2 - OE^2 = AE \\cdot EB')}!",
            [
                f"القطر المار بـ {m('E')} ينقسم إلى قطعتين طولاهما {m(f'R - {d_op}')} و{m(f'R + {d_op}')}.",
                f"بتطبيق قوة النقطة {m('E')}: {m(f'R^2 - {d_op}^2 = {ae} \\times {eb} = {ae * eb}')}.",
                f"ومنه {m(f'R^2 = {ae * eb + d_op * d_op} \\implies R = {R_ans}')}.",
            ],
            f"تحقق: طول القطر {m(2 * R_ans)} أكبر من طول الوتر {m(ae + eb)} كما يجب هندسياً!",
            diagram_en=svg_circle_chords(str(ae), str(eb), f"R−{d_op}", f"R+{d_op}"),
        )

    # 22. nsmo_g10_cyclic_quad_ptolemy_angles (5E, 6M, 4H) — SVG: svg_cyclic_quad
    bp = "nsmo_g10_cyclic_quad_ptolemy_angles"
    # Easy (5): Cyclic quad angle chasing
    easy_cy = [
        # (a_mul, a_add, c_mul, c_add) -> (a_mul*x + a_add) + (c_mul*x + c_add) = 180 -> find angle C
        (2, 10, 3, -5),   # 5x + 5 = 180 -> x = 35 -> A = 80, C = 100
        (3, -15, 2, 20),  # 5x + 5 = 180 -> x = 35 -> A = 90, C = 90? Vary: (3, -12, 2, 12) -> x=36 -> A=96, C=84!
        (4, -20, 1, 25),  # 5x + 5 = 180 -> x = 35 -> A = 120, C = 60
        (2, 18, 2, -6),   # 4x + 12 = 180 -> x = 42 -> A = 102, C = 78
        (3, 6, 1, 14),    # 4x + 20 = 180 -> x = 40 -> A = 126, C = 54
    ]
    easy_cy[1] = (3, -12, 2, 12)
    for am, aa, cm, ca in easy_cy:
        x_val = (180 - aa - ca) // (am + cm)
        ang_a = am * x_val + aa
        ang_c = cm * x_val + ca
        assert ang_a + ang_c == 180
        a_tex = f"{am}x + {aa}^\\circ" if aa >= 0 else f"{am}x - {-aa}^\\circ"
        c_tex = f"{cm}x + {ca}^\\circ" if (cm > 1 and ca >= 0) else (f"x + {ca}^\\circ" if cm == 1 else f"{cm}x - {-ca}^\\circ")
        B.add_math(
            tp, "Easy", bp,
            f"Quadrilateral {m('ABCD')} is inscribed in a circle. If {m(f'\\angle A = {a_tex}')} and {m(f'\\angle C = {c_tex}')}, what is the measure (in degrees) of {m('\\angle C')}?",
            f"الرباعي {m('ABCD')} مرسوم داخل دائرة (رباعي دائري). إذا كان {m(f'\\angle A = {a_tex}')} و{m(f'\\angle C = {c_tex}')}، فما قياس الزاوية {m('\\angle C')} بالدرجات؟",
            ang_c, [ang_a, x_val, 180 - ang_c + 10, ang_c + 12],
            f"Opposite angles of a cyclic quadrilateral sum to {m('180^\\circ')}: solve {m('\\angle A + \\angle C = 180^\\circ')} for {m('x')} first!",
            f"كل زاويتين متقابلتين في الرباعي الدائري متكاملتان مجموعهما {m('180^\\circ')}: أوجد {m('x')} أولاً ثم احسب {m('\\angle C')}!",
            f"Use {m('\\angle A + \\angle C = 180^\\circ')}, solve for {m('x')}, and substitute into {m('\\angle C')}!",
            [
                f"In cyclic quadrilateral {m('ABCD')}, {m(f'({a_tex}) + ({c_tex}) = 180^\\circ')}.",
                f"Combine like terms: {m(f'{am + cm}x + ({aa + ca})^\\circ = 180^\\circ \\implies x = {x_val}^\\circ')}.",
                f"Substitute {m(f'x = {x_val}^\\circ')} into {m('\\angle C')}: {m(f'\\angle C = {ang_c}^\\circ')}.",
            ],
            f"Check: {m(f'\\angle A = {ang_a}^\\circ')} and {m(f'{ang_a}^\\circ + {ang_c}^\\circ = 180^\\circ')}!",
            f"نجمع الزاويتين المتقابلتين ونسويهما بـ {m('180^\\circ')} لإيجاد {m('x')} ثم نعوّض في {m('\\angle C')}!",
            [
                f"في الرباعي الدائري: {m('\\angle A + \\angle C = 180^\\circ')}.",
                f"بحل المعادلة الخطية نجد {m(f'x = {x_val}^\\circ')}.",
                f"نعوّض لإيجاد الزاوية المطلوبة: {m(f'\\angle C = {ang_c}^\\circ')}.",
            ],
            f"تحقق: لا تتوقف عند قيمة {m(f'x = {x_val}')}؛ قياس {m('\\angle C')} هو {m(ang_c)} درجة!",
            diagram_en=svg_cyclic_quad("∠A", "∠C = ?"),
        )

    # Medium (6): 100% geometrically realizable Ptolemy cyclic quads!
    med_ptol = [
        # (AB, BC, CD, DA, BD, AC) — all verified realizable Euclidean cyclic quads!
        (16, 25, 60, 63, 65, 39),  # 16*60 + 63*25 = 960 + 1575 = 2535 = 65 * 39
        (25, 39, 52, 60, 65, 56),  # 25*52 + 60*39 = 1300 + 2340 = 3640 = 65 * 56
        (33, 25, 60, 56, 65, 52),  # 33*60 + 56*25 = 1980 + 1400 = 3380 = 65 * 52
        (9, 10, 21, 10, 17, 17),   # isosceles trapezoid: 9*21 + 100 = 289 = 17 * 17
        (4, 13, 14, 13, 15, 15),   # isosceles trapezoid: 4*14 + 169 = 225 = 15 * 15
        (11, 25, 25, 25, 30, 30),  # isosceles trapezoid: 11*25 + 625 = 900 = 30 * 30
    ]
    for ab, bc, cd, da, bd, ac in med_ptol:
        assert ab * cd + ad * bc if False else (ab * cd + da * bc == ac * bd)
        B.add_math(
            tp, "Medium", bp,
            f"Cyclic quadrilateral {m('ABCD')} has side lengths {m(f'AB = {ab}')}, {m(f'BC = {bc}')}, {m(f'CD = {cd}')}, {m(f'DA = {da}')}, and diagonal {m(f'BD = {bd}')}. Find the length of diagonal {m('AC')}.",
            f"رباعي دائري {m('ABCD')} أطوال أضلاعه {m(f'AB = {ab}')} و{m(f'BC = {bc}')} و{m(f'CD = {cd}')} و{m(f'DA = {da}')}، وطول قطره {m(f'BD = {bd}')}. أوجد طول القطر {m('AC')}.",
            ac, [ac - 3, ac + 4, bd + 2 if ac != bd else ac + 3, ac - 5],
            f"Use Ptolemy's Theorem: {m('AC \\cdot BD = AB \\cdot CD + AD \\cdot BC')}!",
            f"استخدم مبرهنة بطليموس: {m('AC \\cdot BD = AB \\cdot CD + AD \\cdot BC')}!",
            f"Apply Ptolemy's Theorem directly to link the product of diagonals to opposite side pairs!",
            [
                f"Compute opposite side products: {m(f'AB \\cdot CD = {ab} \\times {cd} = {ab * cd}')} and {m(f'AD \\cdot BC = {da} \\times {bc} = {da * bc}')}.",
                f"By Ptolemy's Theorem, {m(f'AC \\cdot {bd} = {ab * cd} + {da * bc} = {ac * bd}')}.",
                f"Divide by {m(bd)}: {m(f'AC = \\frac{{{ac * bd}}}{{{bd}}} = {ac}')}.",
            ],
            f"Check: {m(f'{ac} \\times {bd} = {ac * bd} = {ab * cd} + {da * bc}')}!",
            f"نعوّض مباشرة في مبرهنة بطليموس للرباعي الدائري!",
            [
                f"حاصل ضرب الضلعين المتقابلين الأولين {m(f'{ab} \\times {cd} = {ab * cd}')}، والآخرين {m(f'{da} \\times {bc} = {da * bc}')}.",
                f"من مبرهنة بطليموس: {m(f'AC \\times {bd} = {ab * cd + da * bc}')}.",
                f"بالقسمة على {m(bd)} نجد {m(f'AC = {ac}')}.",
            ],
            f"تحقق: مجموع حاصلي ضرب الأضلاع المتقابلة يساوي حاصل ضرب القطرين تماماً.",
            diagram_en=svg_cyclic_quad(f"BD={bd}", "AC=?"),
        )

    # Hard (4): Inscribed equilateral triangle Ptolemy corollary PA = PB + PC (2 Qs) & solving for missing side in Ptolemy (2 Qs)!
    for pb_v, pc_v in [(7, 11), (9, 16)]:
        ans = pb_v + pc_v
        B.add_math(
            tp, "Hard", bp,
            f"Equilateral triangle {m('ABC')} is inscribed in a circle, and point {m('P')} lies on the minor arc {m('BC')}. If {m(f'PB = {pb_v}')} and {m(f'PC = {pc_v}')}, what is the length of chord {m('PA')}?",
            f"مثلث متطابق الأضلاع {m('ABC')} مرسوم داخل دائرة، وتقع النقطة {m('P')} على القوس الأصغر {m('BC')}. إذا كان {m(f'PB = {pb_v}')} و{m(f'PC = {pc_v}')}، فما طول الوتر {m('PA')}؟",
            ans, [ans - 2, ans + 3, pc_v - pb_v, int(math.isqrt(pb_v * pb_v + pc_v * pc_v)) + 1],
            f"Apply Ptolemy's Theorem to cyclic quadrilateral {m('ABPC')} and cancel the equilateral side length {m('s')}!",
            f"طبّق مبرهنة بطليموس على الرباعي الدائري {m('ABPC')} واختصر طول ضلع المثلث المتطابق الأضلاع {m('s')}!",
            f"Let {m('s = AB = BC = CA')}: Ptolemy's Theorem on cyclic quadrilateral {m('ABPC')} cancels {m('s')} completely, leaving {m('PA = PB + PC')}!",
            [
                f"Since {m('P')} lies on minor arc {m('BC')}, the vertices in cyclic order form quadrilateral {m('ABPC')} with diagonals {m('PA')} and {m('BC = s')}.",
                f"By Ptolemy's Theorem, {m('PA \\cdot BC = AB \\cdot PC + AC \\cdot PB \\implies s \\cdot PA = s \\cdot PC + s \\cdot PB')}.",
                f"Dividing by {m('s > 0')} gives Van Schooten's Theorem: {m(f'PA = PB + PC = {pb_v} + {pc_v} = {ans}')}!",
            ],
            f"Remarkable check: the answer {m(ans)} does not even depend on the side length {m('s')} of {m('\\triangle ABC')}!",
            f"بتطبيق بطليموس على الرباعي الدائري {m('ABPC')} يختصر طول الضلع {m('s')} ويبقى {m('PA = PB + PC')}!",
            [
                f"نرمز لطول ضلع المثلث المتطابق الأضلاع بالرمز {m('s')}. في الرباعي الدائري {m('ABPC')} القطران هما {m('PA')} و{m('BC = s')}.",
                f"من بطليموس: {m('s \\cdot PA = s \\cdot PB + s \\cdot PC')}.",
                f"بالقسمة على {m('s')} نجد {m(f'PA = PB + PC = {pb_v} + {pc_v} = {ans}')}!",
            ],
            f"تحقق (مبرهنة فان شوتن): النتيجة مستقلة تماماً عن طول ضلع المثلث المتطابق الأضلاع!",
            diagram_en=svg_cyclic_quad(f"PB={pb_v}", f"PC={pc_v}"),
        )

    for ab, bc, da, bd, ac, cd_ans in [(15, 7, 20, 25, 20, 24), (16, 25, 63, 65, 39, 60)]:
        # Wait: (15,7,24,20,25,20) had AC asked in worked ex, here ask missing side CD!
        assert ab * cd_ans + da * bc == ac * bd
        B.add_math(
            tp, "Hard", bp,
            f"In cyclic quadrilateral {m('ABCD')}, {m(f'AB = {ab}')}, {m(f'BC = {bc}')}, {m(f'DA = {da}')}, and the diagonals have lengths {m(f'AC = {ac}')} and {m(f'BD = {bd}')}. What is the length of side {m('CD')}?",
            f"في الرباعي الدائري {m('ABCD')} لدينا {m(f'AB = {ab}')} و{m(f'BC = {bc}')} و{m(f'DA = {da}')}، وطولا القطرين {m(f'AC = {ac}')} و{m(f'BD = {bd}')}. ما طول الضلع {m('CD')}؟",
            cd_ans, [cd_ans - 4, cd_ans + 3, cd_ans - 2, bd - 2],
            f"Rearrange Ptolemy's Theorem to isolate {m('AB \\cdot CD = AC \\cdot BD - AD \\cdot BC')}!",
            f"أعد ترتيب مبرهنة بطليموس لعزل {m('AB \\cdot CD = AC \\cdot BD - AD \\cdot BC')}!",
            f"Use Ptolemy's Theorem {m('AC \\cdot BD = AB \\cdot CD + AD \\cdot BC')} in reverse to solve for the unknown side {m('CD')}!",
            [
                f"Compute diagonal product: {m(f'AC \\cdot BD = {ac} \\times {bd} = {ac * bd}')}.",
                f"Subtract the known opposite-side product {m(f'AD \\cdot BC = {da} \\times {bc} = {da * bc}')}: {m(f'{ab} \\cdot CD = {ac*bd - da*bc}')}.",
                f"Divide by {m(ab)}: {m(f'CD = \\frac{{{ac*bd - da*bc}}}{{{ab}}} = {cd_ans}')}.",
            ],
            f"Check: {m(f'{ab} \\times {cd_ans} + {da} \\times {bc} = {ac * bd} = {ac} \\times {bd}')}!",
            f"نطبّق مبرهنة بطليموس عكسياً لإيجاد الضلع المجهول {m('CD')}!",
            [
                f"نحسب حاصل ضرب القطرين: {m(f'{ac} \\times {bd} = {ac * bd}')}.",
                f"نطرح {m(f'AD \\cdot BC = {da * bc}')} فنحصل على {m(f'{ab} \\cdot CD = {ac*bd - da*bc}')}.",
                f"بالقسمة على {m(ab)} نجد {m(f'CD = {cd_ans}')}.",
            ],
            f"تحقق: جميع الأضلاع والقطرين تحقق بطليموس ومتباينة المثلث بدقة.",
            diagram_en=svg_cyclic_quad(f"AC={ac}, BD={bd}", "CD=?"),
        )

    # 23. nsmo_g10_angle_bisector_theorem (5E, 6M, 4H) — SVG: svg_angle_bisector_tri
    bp = "nsmo_g10_angle_bisector_theorem"
    easy_ab = [
        (10, 15, 20),  # BD = 20 * 10 / 25 = 8
        (12, 16, 21),  # BD = 21 * 12 / 28 = 9
        (9, 12, 14),   # BD = 14 * 9 / 21 = 6
        (14, 21, 25),  # BD = 25 * 14 / 35 = 10
        (15, 25, 32),  # BD = 32 * 15 / 40 = 12
    ]
    for ab, ac, bc in easy_ab:
        assert ab + ac > bc and ab + bc > ac and ac + bc > ab
        bd = (bc * ab) // (ab + ac)
        dc = bc - bd
        assert bd * ac == dc * ab
        B.add_math(
            tp, "Easy", bp,
            f"In {m('\\triangle ABC')}, the interior angle bisector of {m('\\angle A')} meets side {m('BC')} at {m('D')}. If {m(f'AB = {ab}')}, {m(f'AC = {ac}')}, and {m(f'BC = {bc}')}, find the length of {m('BD')}.",
            f"في المثلث {m('ABC')}، يلاقي المنصف الداخلي للزاوية {m('\\angle A')} الضلع {m('BC')} في النقطة {m('D')}. إذا كان {m(f'AB = {ab}')} و{m(f'AC = {ac}')} و{m(f'BC = {bc}')}، فأوجد طول {m('BD')}.",
            bd, [dc, bc // 2, bd + 2, bd - 2],
            f"By the Angle Bisector Theorem, {m('D')} divides {m('BC')} in the ratio {m(f'BD : DC = AB : AC = {ab} : {ac}')}!",
            f"حسب مبرهنة منصف الزاوية، تقسم {m('D')} الضلع {m('BC')} بنسبة {m(f'BD : DC = AB : AC = {ab} : {ac}')}!",
            f"Take the fraction {m('\\frac{AB}{AB + AC}')} of the total base {m('BC')}!",
            [
                f"By the Angle Bisector Theorem, {m(f'\\frac{{BD}}{{DC}} = \\frac{{AB}}{{AC}} = \\frac{{{ab}}}{{{ac}}}')}.",
                f"Thus {m('BD')} is {m(f'\\frac{{{ab}}}{{{ab} + {ac}}}')} of {m(f'BC = {bc}')}: {m(f'BD = {bc} \\times \\frac{{{ab}}}{{{ab + ac}}} = {bd}')}.",
            ],
            f"Check: {m(f'DC = {dc}')}, and {m(f'{bd} : {dc} = {ab} : {ac}')}!",
            f"نأخذ حصة {m('BD')} من الضلع الكلي {m('BC')} بنسبة الضلعين المجاورين!",
            [
                f"من مبرهنة منصف الزاوية: {m(f'\\frac{{BD}}{{DC}} = \\frac{{{ab}}}{{{ac}}}')}.",
                f"إذن {m(f'BD = {bc} \\times \\frac{{{ab}}}{{{ab + ac}}} = {bd}')}.",
            ],
            f"تحقق: {m(f'DC = {dc}')} والنسبة {m(f'{bd}/{dc} = {ab}/{ac}')} متحققة.",
            diagram_en=svg_angle_bisector_tri(str(ab), str(ac), "?", "DC"),
        )

    # Medium (6): 3 perimeter + bisector segments -> find AB, and 3 incenter ratio AI / ID = (AB + AC) / BC!
    for bd, dc, perim in [(6, 9, 60), (8, 12, 70), (10, 14, 84)]:
        bc = bd + dc
        ab_plus_ac = perim - bc
        ab = (ab_plus_ac * bd) // bc
        ac = ab_plus_ac - ab
        assert ab + ac + bc == perim and ab * dc == ac * bd and ab + bc > ac
        B.add_math(
            tp, "Medium", bp,
            f"In {m('\\triangle ABC')}, angle bisector {m('AD')} divides {m('BC')} into {m(f'BD = {bd}')} and {m(f'DC = {dc}')}. If the perimeter of {m('\\triangle ABC')} is {m(perim)}, what is the length of side {m('AB')}?",
            f"في المثلث {m('ABC')}، يقسم منصف الزاوية {m('AD')} الضلع {m('BC')} إلى {m(f'BD = {bd}')} و{m(f'DC = {dc}')}. إذا كان محيط المثلث {m('ABC')} يساوي {m(perim)}، فما طول الضلع {m('AB')}؟",
            ab, [ac, ab + 3, ab - 3, perim // 3],
            f"Subtract {m(f'BC = {bd} + {dc} = {bc}')} from the perimeter to get {m('AB + AC')}, then split in ratio {m(f'{bd} : {dc}')}!",
            f"اطرح {m(f'BC = {bc}')} من المحيط لإيجاد {m('AB + AC')}، ثم قسّمه بنسبة {m(f'{bd} : {dc}')}!",
            f"Find {m('AB + AC')} from the perimeter, then apply {m('AB : AC = BD : DC')}!",
            [
                f"Compute {m(f'BC = {bd} + {dc} = {bc}')}, so {m(f'AB + AC = {perim} - {bc} = {ab_plus_ac}')}.",
                f"By the Angle Bisector Theorem, {m(f'AB : AC = {bd} : {dc}')}.",
                f"Therefore {m(f'AB = {ab_plus_ac} \\times \\frac{{{bd}}}{{{bc}}} = {ab}')}.",
            ],
            f"Check: {m(f'AC = {ac}')}, perimeter {m(f'{ab} + {ac} + {bc} = {perim}')}, and {m(f'{ab}/{ac} = {bd}/{dc}')}!",
            f"نحسب {m('AB + AC')} من المحيط أولاً ثم نوزّعه بنسبة {m('BD : DC')}!",
            [
                f"طول القاعدة {m(f'BC = {bd} + {dc} = {bc}')}، فيكون {m(f'AB + AC = {perim} - {bc} = {ab_plus_ac}')}.",
                f"بما أن {m(f'AB : AC = {bd} : {dc}')} فإن {m(f'AB = {ab_plus_ac} \\times \\frac{{{bd}}}{{{bc}}} = {ab}')}.",
            ],
            f"تحقق: الضلعان {m(ab)} و{m(ac)} والقاعدة {m(bc)} مجموعها {m(perim)} وتحقق متباينة المثلث.",
            diagram_en=svg_angle_bisector_tri("?", "AC", str(bd), str(dc)),
        )

    for ab, ac, bc in [(10, 14, 12), (15, 21, 12), (14, 16, 12)]:
        # Incenter I on bisector AD: BI bisects angle ABD -> AI / ID = AB / BD = (AB + AC) / BC!
        ans = Fraction(ab + ac, bc)
        B.add_math(
            tp, "Medium", bp,
            f"In {m('\\triangle ABC')}, {m(f'AB = {ab}')}, {m(f'AC = {ac}')}, and {m(f'BC = {bc}')}. Angle bisector {m('AD')} meets {m('BC')} at {m('D')}, and {m('I')} is the incenter of {m('\\triangle ABC')}. Find the ratio {m('\\frac{AI}{ID}')}.",
            f"في المثلث {m('ABC')} لدينا {m(f'AB = {ab}')} و{m(f'AC = {ac}')} و{m(f'BC = {bc}')}. يقطع منصف الزاوية {m('AD')} الضلع {m('BC')} في {m('D')}، والنقطة {m('I')} هي مركز الدائرة الداخلية. أوجد النسبة {m('\\frac{AI}{ID}')}.",
            ans, [Fraction(ab, ac), Fraction(bc, ab + ac), ans + 1, Fraction(ab + ac, 2 * bc)],
            f"Apply the Angle Bisector Theorem a **second time** inside {m('\\triangle ABD')} using bisector {m('BI')}!",
            f"طبّق مبرهنة منصف الزاوية **مرة ثانية** داخل المثلث الجزئي {m('ABD')} باستخدام المنصف {m('BI')}!",
            f"Since {m('BI')} bisects {m('\\angle ABD')}, {m('\\frac{AI}{ID} = \\frac{AB}{BD}')}, which simplifies cleanly to {m('\\frac{AB + AC}{BC}')}!",
            [
                f"In {m('\\triangle ABC')}, {m(f'BD = BC \\cdot \\frac{{AB}}{{AB + AC}} = {bc} \\cdot \\frac{{{ab}}}{{{ab + ac}}}')}.",
                f"Since {m('I')} is the incenter, {m('BI')} bisects {m('\\angle ABD')} in {m('\\triangle ABD')}, giving {m('\\frac{AI}{ID} = \\frac{AB}{BD}')}.",
                f"Substitute {m('BD')}: {m(f'\\frac{{AI}}{{ID}} = \\frac{{AB + AC}}{{BC}} = \\frac{{{ab + ac}}}{{{bc}}} = {ans}')}.",
            ],
            f"Memorizable Olympiad gem: {m('AI : ID = (b + c) : a')} holds in every triangle!",
            f"بتطبيق مبرهنة منصف الزاوية في المثلث {m('ABD')} نحصل على القاعدة الذهبية {m('\\frac{AI}{ID} = \\frac{AB + AC}{BC}')}!",
            [
                f"في المثلث {m('ABC')}: {m('BD = \\frac{AB \\cdot BC}{AB + AC}')}.",
                f"بما أن {m('I')} مركز الدائرة الداخلية فإن {m('BI')} ينصّف {m('\\angle ABD')}، وعليه {m('\\frac{AI}{ID} = \\frac{AB}{BD}')}.",
                f"بالتعويض والاختصار نجد {m(f'\\frac{{AI}}{{ID}} = \\frac{{{ab} + {ac}}}{{{bc}}} = {ans}')}.",
            ],
            f"تحقق: القاعدة العامة {m('AI : ID = (b + c) : a')} تختصر الحل في ثوانٍ!",
            diagram_en=svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC"),
        )

    # Hard (4): Exact integer angle-bisector length AD^2 = AB*AC - BD*DC!
    hard_ab = [
        (6, 8, 7, 3, 4, 6),       # AD^2 = 48 - 12 = 36 -> AD = 6
        (12, 16, 14, 6, 8, 12),   # AD^2 = 192 - 48 = 144 -> AD = 12
        (24, 27, 17, 8, 9, 24),   # AD^2 = 648 - 72 = 576 -> AD = 24
        (24, 50, 37, 12, 25, 30), # AD^2 = 1200 - 300 = 900 -> AD = 30
    ]
    for ab, ac, bc, bd, dc, ad_ans in hard_ab:
        assert ab + bc > ac and ab + ac > bc and ac + bc > ab
        assert bd + dc == bc and bd * ac == dc * ab
        assert ab * ac - bd * dc == ad_ans * ad_ans
        B.add_math(
            tp, "Hard", bp,
            f"In {m('\\triangle ABC')}, {m(f'AB = {ab}')}, {m(f'AC = {ac}')}, and {m(f'BC = {bc}')}. If {m('AD')} is the interior angle bisector of {m('\\angle A')} meeting {m('BC')} at {m('D')}, find the exact length of {m('AD')}.",
            f"في المثلث {m('ABC')} لدينا {m(f'AB = {ab}')} و{m(f'AC = {ac}')} و{m(f'BC = {bc}')}. إذا كان {m('AD')} المنصف الداخلي للزاوية {m('\\angle A')} ويقطع {m('BC')} في {m('D')}، فأوجد الطول الدقيق للمنصف {m('AD')}.",
            ad_ans, [ad_ans - 2, ad_ans + 3, bd + dc, int(math.isqrt(ab * ac))],
            f"First find {m('BD')} and {m('DC')}, then apply the Angle Bisector Length Theorem {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}!",
            f"أوجد {m('BD')} و{m('DC')} أولاً، ثم طبّق قانون طول المنصف {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}!",
            f"Combine {m('BD : DC = AB : AC')} with Stewart's bisector formula {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}!",
            [
                f"Split {m(f'BC = {bc}')} in ratio {m(f'{ab} : {ac}')}: {m(f'BD = {bd}')} and {m(f'DC = {dc}')}.",
                f"Apply the Angle Bisector Length formula: {m(f'AD^2 = AB \\cdot AC - BD \\cdot DC = {ab} \\times {ac} - {bd} \\times {dc} = {ab*ac - bd*dc}')}.",
                f"Take the square root: {m(f'AD = \\sqrt{{{ad_ans*ad_ans}}} = {ad_ans}')}.",
            ],
            f"Triangle check in {m('\\triangle ABD')}: sides {m(f'{ab}, {bd}, {ad_ans}')} satisfy {m(f'{bd} + {ad_ans} > {ab}')}!",
            f"نحسب جزأَي القاعدة {m('BD, DC')} أولاً ثم نعوّض في صيغة طول المنصف الداخلي {m('AD^2 = AB \\cdot AC - BD \\cdot DC')}!",
            [
                f"نقسم {m(f'BC = {bc}')} بنسبة {m(f'{ab} : {ac}')} فنجد {m(f'BD = {bd}')} و{m(f'DC = {dc}')}.",
                f"نعوّض في قانون طول المنصف: {m(f'AD^2 = {ab} \\times {ac} - {bd} \\times {dc} = {ad_ans*ad_ans}')}.",
                f"بأخذ الجذر التربيعي نحصل على {m(f'AD = {ad_ans}')}.",
            ],
            f"تحقق: في المثلث {m('ABD')} الأطوال {m(f'{ab}, {bd}, {ad_ans}')} تحقق متباينة المثلث!",
            diagram_en=svg_angle_bisector_tri(str(ab), str(ac), str(bd), str(dc)),
        )

    # 24. nsmo_g10_apollonius_median_centroid (5E, 6M, 4H) — SVG: svg_median_tri
    bp = "nsmo_g10_apollonius_median_centroid"
    # Easy (5): Centroid 2:1 ratio & 1/6 area split
    easy_med = [
        ("len_ag", 18, 12),   # AM = 18 -> AG = 12
        ("len_am", 14, 21),   # AG = 14 -> AM = 21
        ("area_bgm", 72, 12), # Area(ABC) = 72 -> Area(BGM) = 72 / 6 = 12
        ("area_abg", 90, 30), # Area(ABC) = 90 -> Area(ABG) = 90 / 3 = 30
        ("len_gm", 27, 9),    # AM = 27 -> GM = 9
    ]
    for kind, giv, ans in easy_med:
        if kind == "len_ag":
            q_en = f"In {m('\\triangle ABC')}, {m('G')} is the centroid and {m('AM')} is the median to side {m('BC')}. If {m(f'AM = {giv}')}, what is the length of {m('AG')}?"
            q_ar = f"في المثلث {m('ABC')}، {m('G')} هو مركز الثقل و{m('AM')} هو المتوسط إلى الضلع {m('BC')}. إذا كان {m(f'AM = {giv}')}، فما طول {m('AG')}؟"
        elif kind == "len_am":
            q_en = f"In {m('\\triangle ABC')}, centroid {m('G')} lies on median {m('AM')}. If {m(f'AG = {giv}')}, what is the full length of median {m('AM')}?"
            q_ar = f"في المثلث {m('ABC')}، يقع مركز الثقل {m('G')} على المتوسط {m('AM')}. إذا كان {m(f'AG = {giv}')}، فما الطول الكلي للمتوسط {m('AM')}؟"
        elif kind == "len_gm":
            q_en = f"In {m('\\triangle ABC')}, median {m('AM')} has length {m(giv)} and {m('G')} is the centroid. Find the length of segment {m('GM')}."
            q_ar = f"في المثلث {m('ABC')}، طول المتوسط {m(f'AM = {giv}')} والنقطة {m('G')} هي مركز الثقل. أوجد طول القطعة {m('GM')}."
        elif kind == "area_bgm":
            q_en = f"The three medians of {m('\\triangle ABC')} meet at centroid {m('G')}, with {m('M')} the midpoint of {m('BC')}. If the area of {m('\\triangle ABC')} is {m(giv)}, what is the area of {m('\\triangle BGM')}?"
            q_ar = f"تتلاقى متوسطات المثلث {m('ABC')} في مركز الثقل {m('G')}، وكانت {m('M')} منتصف {m('BC')}. إذا كانت مساحة المثلث {m('ABC')} تساوي {m(giv)}، فما مساحة المثلث {m('BGM')}؟"
        else:
            q_en = f"In {m('\\triangle ABC')} of area {m(giv)}, {m('G')} is the centroid. What is the area of {m('\\triangle ABG')}?"
            q_ar = f"في المثلث {m('ABC')} الذي مساحته {m(giv)}، النقطة {m('G')} هي مركز الثقل. ما مساحة المثلث {m('ABG')}؟"
        B.add_math(
            tp, "Easy", bp, q_en, q_ar, ans,
            [giv // 2, ans + 6, max(2, ans - 4), ans * 2],
            f"The centroid {m('G')} divides every median in ratio {m('AG : GM = 2 : 1')} and splits {m('\\triangle ABC')} into {m('6')} equal-area sub-triangles!",
            f"مركز الثقل {m('G')} يقسم كل متوسط بنسبة {m('AG : GM = 2 : 1')} ويقسم المثلث إلى {m('6')} مثلثات متساوية المساحة!",
            f"Use the {m('2 : 1')} centroid division property (and {m('6')}-way equal-area partition by the three medians)!",
            [
                f"Recall that the three medians concur at centroid {m('G')} with {m('AG : GM = 2 : 1')}, partitioning {m('\\triangle ABC')} into {m('6')} triangles of equal area.",
                f"Applying this ratio directly to {m(giv)} yields {m(ans)}.",
            ],
            f"Check: the {m('2 : 1')} vertex-to-midpoint split holds universally in every triangle!",
            f"نطبّق خاصية مركز الثقل الذي يقسم المتوسط بنسبة {m('2 : 1')} من جهة الرأس ويقسم المساحة إلى {m('6')} أجزاء متساوية!",
            [
                f"مركز الثقل {m('G')} يحقق {m('AG : GM = 2 : 1')} وتقسم المتوسطات الثلاثة المساحة الكلية إلى {m('6')} مثلثات متكافئة.",
                f"بتطبيق النسبة المناسبة على القيمة {m(giv)} نحصل على {m(ans)}.",
            ],
            f"تحقق: النسبة {m('2 : 1')} والمساحات المتكافئة الـ {m('6')} متحققة دائماً.",
            diagram_en=svg_median_tri("c", "b", "a", "AM"),
        )

    # Medium (6): Apollonius median lengths (exact integer medians!)
    # Find clean triangles with integer a, b, c, m_a (distinct from 11, 13, 16 -> 9):
    med_ap = [
        (7, 9, 8, 7),      # 2(49+81) - 64 = 260 - 64 = 196 -> m_a = 7!
        (8, 12, 10, 9),    # 2(64+144) - 100 = 416 - 100 = 316 no! Let's check: (7, 11, 12): 2(49+121)-144 = 340-144 = 196 -> m_a = 7!
        (9, 13, 10, 10),   # 2(81+169) - 100 = 500 - 100 = 400 -> m_a = 10!
        (10, 14, 16, 9),   # 2(100+196) - 256 = 592 - 256 = 336 no; (10, 14, 12): 592 - 144 = 448 no; (6, 10, 8): right tri -> m_a = 7? 2(36+100)-64 = 208 no; (13, 15, 14): 2(169+225)-196 = 788-196=592; (12, 16, 20): hyp 20 -> m_a = 10!
        (14, 18, 16, 14),  # scaled (7,9,8): 2(196+324)-256 = 1040-256 = 784 = 28^2 -> m_a = 14!
        (11, 17, 18, 12),  # 2(121+289) - 324 = 820 - 324 = 496 no; (13, 17, 16): 2(169+289)-256 = 916-256=660; (8, 14, 18): 2(64+196)-324 = 196 -> m_a = 7!
    ]
    med_ap = [
        (7, 9, 8, 7),
        (7, 11, 12, 7),
        (9, 13, 10, 10),
        (8, 14, 18, 7),
        (14, 18, 16, 14),
        (17, 23, 20, 18),  # check: 2(289 + 529) - 400 = 1636 - 400 = 1236 no! Let's check (13, 19, 14): 2(169+361)-196 = 1060-196 = 864; (15, 19, 22): 2(225+361)-484 = 1172-484=688; (11, 15, 12): 2(121+225)-144 = 692-144=548; (9, 17, 14): 2(81+289)-196 = 740-196=544; (13, 15, 24): 2(169+225)-576 = 788-576 = 212; (10, 22, 24): 2(100+484)-576 = 592; (12, 20, 16): 2(144+400)-256 = 832; (11, 21, 26): 2(121+441)-676 = 448; (17, 19, 12): 2(289+361)-144 = 1300-144 = 1156 = 34^2 -> m_a = 17!!
    ]
    med_ap[5] = (17, 19, 12, 17)
    for c_s, b_s, a_s, ma_ans in med_ap:
        assert c_s + b_s > a_s and c_s + a_s > b_s and b_s + a_s > c_s
        assert 2 * (b_s * b_s + c_s * c_s) - a_s * a_s == 4 * ma_ans * ma_ans
        B.add_math(
            tp, "Medium", bp,
            f"In {m('\\triangle ABC')}, {m(f'AB = {c_s}')}, {m(f'AC = {b_s}')}, and {m(f'BC = {a_s}')}. What is the length of median {m('AM')} drawn from {m('A')} to the midpoint {m('M')} of {m('BC')}?",
            f"في المثلث {m('ABC')} لدينا {m(f'AB = {c_s}')} و{m(f'AC = {b_s}')} و{m(f'BC = {a_s}')}. ما طول المتوسط {m('AM')} المرسوم من الرأس {m('A')} إلى منتصف {m('BC')}؟",
            ma_ans, [ma_ans - 1, ma_ans + 2, (b_s + c_s) // 2, ma_ans + 3],
            f"Apply Apollonius's Theorem: {m('4 \\cdot AM^2 = 2(AB^2 + AC^2) - BC^2')}!",
            f"طبّق مبرهنة أبولونيوس: {m('4 \\cdot AM^2 = 2(AB^2 + AC^2) - BC^2')}!",
            f"Use Apollonius's Median Theorem, remembering to subtract the square of the bisected side {m(f'BC = {a_s}')}!",
            [
                f"Substitute {m(f'AB = {c_s},\\; AC = {b_s},\\; BC = {a_s}')}: {m(f'4 \\cdot AM^2 = 2({c_s}^2 + {b_s}^2) - {a_s}^2')}.",
                f"Compute {m(f'4 \\cdot AM^2 = 2({c_s*c_s + b_s*b_s}) - {a_s*a_s} = {4 * ma_ans * ma_ans}')}.",
                f"Divide by {m('4')} and take the square root: {m(f'AM^2 = {ma_ans*ma_ans} \\implies AM = {ma_ans}')}.",
            ],
            f"Check: {m(f'4({ma_ans}^2) + {a_s}^2 = {4*ma_ans*ma_ans + a_s*a_s} = 2({c_s}^2 + {b_s}^2)')}!",
            f"نعوّض في قانون أبولونيوس للمتوسط مع طرح مربع الضلع المنصَّف {m('BC')}!",
            [
                f"لدينا {m(f'4 \\cdot AM^2 = 2({c_s}^2 + {b_s}^2) - {a_s}^2 = 2({c_s*c_s + b_s*b_s}) - {a_s*a_s} = {4*ma_ans*ma_ans}')}.",
                f"بالقسمة على {m('4')} وأخذ الجذر التربيعي نحصل على {m(f'AM = {ma_ans}')}.",
            ],
            f"تحقق: {m(f'AM = {ma_ans}')} يحقق متباينة المثلث في نصفي المثلث.",
            diagram_en=svg_median_tri(str(c_s), str(b_s), str(a_s), "AM=?"),
        )

    # Hard (4): 2 sum-of-median-squares m_a^2 + m_b^2 + m_c^2 = 3/4 (a^2 + b^2 + c^2), and 2 perpendicular medians b^2 + c^2 = 5a^2!
    for a_s, b_s, c_s in [(6, 8, 12), (10, 12, 16)]:
        assert a_s + b_s > c_s
        s_sq = a_s * a_s + b_s * b_s + c_s * c_s
        assert (3 * s_sq) % 4 == 0
        ans = (3 * s_sq) // 4
        B.add_math(
            tp, "Hard", bp,
            f"Triangle {m('ABC')} has side lengths {m(f'a = {a_s}')}, {m(f'b = {b_s}')}, and {m(f'c = {c_s}')}, with medians {m('m_a, m_b, m_c')}. Find the value of {m('m_a^2 + m_b^2 + m_c^2')}.",
            f"مثلث {m('ABC')} أطوال أضلاعه {m(f'a = {a_s}')} و{m(f'b = {b_s}')} و{m(f'c = {c_s}')}، ومتوسطاته {m('m_a, m_b, m_c')}. أوجد قيمة {m('m_a^2 + m_b^2 + m_c^2')}.",
            ans, [s_sq, ans - 12, ans + 15, (2 * s_sq) // 3],
            f"Add Apollonius's formula across all three medians: {m('4(m_a^2 + m_b^2 + m_c^2) = 3(a^2 + b^2 + c^2)')}!",
            f"اجمع معادلة أبولونيوس للمتوسطات الثلاثة لتحصل على المتطابقة {m('4(m_a^2 + m_b^2 + m_c^2) = 3(a^2 + b^2 + c^2)')}!",
            f"Summing Apollonius's Theorem over all three sides yields the universal invariant {m('m_a^2 + m_b^2 + m_c^2 = \\frac{3}{4}(a^2 + b^2 + c^2)')}!",
            [
                f"Write {m('4m_a^2 = 2b^2 + 2c^2 - a^2')}, {m('4m_b^2 = 2a^2 + 2c^2 - b^2')}, and {m('4m_c^2 = 2a^2 + 2b^2 - c^2')}.",
                f"Adding all three gives {m('4(m_a^2 + m_b^2 + m_c^2) = 3(a^2 + b^2 + c^2)')}.",
                f"Substitute {m(f'a^2 + b^2 + c^2 = {a_s}^2 + {b_s}^2 + {c_s}^2 = {s_sq}')}: {m(f'\\frac{{3}}{{4}} \\times {s_sq} = {ans}')}.",
            ],
            f"Equilateral check: if {m('a = b = c = 2')}, each median has {m('m^2 = 3')}, sum {m('9 = \\frac{3}{4}(12)')}!",
            f"بجمع قانون أبولونيوس للأضلاع الثلاثة نستنتج أن مجموع مربعات المتوسطات يساوي {m('\\frac{3}{4}')} مجموع مربعات الأضلاع!",
            [
                f"بجمع المعادلات الثلاث نجد {m('m_a^2 + m_b^2 + m_c^2 = \\frac{3}{4}(a^2 + b^2 + c^2)')}.",
                f"نحسب {m(f'a^2 + b^2 + c^2 = {s_sq}')}، ثم نضرب في {m('\\frac{3}{4}')} فنحصل على {m(ans)}.",
            ],
            f"تحقق: لا حاجة لحساب كل متوسط منفرداً بفضل التناظر الجبري!",
            diagram_en=svg_median_tri(str(c_s), str(b_s), str(a_s), "mₐ,mᵦ,m𝒸"),
        )

    for b_s, c_s, a_ans in [(7, 11, 6), (9, 13, 7)]:
        # Wait: check 7^2 + 11^2 = 49 + 121 = 170 (not 5*a^2!); let's pick exact b^2 + c^2 = 5 * a^2 with triangle inequality b + a > c!
        # Check a = 5 -> 5a^2 = 125 = 2^2 + 11^2 (2+5 < 11 no!) OR 5^2 + 10^2 (5+5=10 boundary)!
        # Check a = 6 -> 5a^2 = 180 = 6^2 + 12^2 (boundary); a = 10 -> 500 = 10^2 + 20^2 or 4^2 + 22^2;
        # Check a = 13 -> 5*169 = 845 = 13^2 + 26^2 or 2^2 + 29^2 or 19^2 + 22^2!! CHECK 19^2 + 22^2 = 361 + 484 = 845 = 5 * 13^2!! AND 13 + 19 = 32 > 22!!
        # Check a = 17 -> 5*289 = 1445 = 17^2 + 34^2 or 23^2 + 30^2? 529 + 900 = 1429 no; 19^2 + 33^2 = 361 + 1089 = 1450; 26^2 + 27^2? No, 29^2 + 24^2 = 841 + 576 = 1417; 31^2 + 22^2 = 961 + 484 = 1445 = 5 * 17^2!! AND 17 + 22 = 39 > 31!!
        pass
    for b_s, c_s, a_ans in [(19, 22, 13), (22, 31, 17)]:
        assert b_s * b_s + c_s * c_s == 5 * a_ans * a_ans and a_ans + b_s > c_s
        B.add_math(
            tp, "Hard", bp,
            f"In {m('\\triangle ABC')}, the medians drawn from vertices {m('B')} and {m('C')} are **perpendicular** to each other! If {m(f'AC = {b_s}')} and {m(f'AB = {c_s}')}, what is the length of side {m('BC')}?",
            f"في المثلث {m('ABC')}، المتوسطان المرسومان من الرأسين {m('B')} و{m('C')} **متعامدان**! إذا كان {m(f'AC = {b_s}')} و{m(f'AB = {c_s}')}، فما طول الضلع {m('BC')}؟",
            a_ans, [a_ans - 2, a_ans + 2, (b_s + c_s) // 3, a_ans + 4],
            f"At centroid {m('G')}, {m('\\triangle BGC')} is right-angled at {m('G')}, so {m('BG^2 + CG^2 = BC^2')}, where {m('BG = \\frac{2}{3}m_b')} and {m('CG = \\frac{2}{3}m_c')}!",
            f"عند مركز الثقل {m('G')} يكون المثلث {m('BGC')} قائم الزاوية في {m('G')}، أي {m('BG^2 + CG^2 = BC^2')} مع {m('BG = \\frac{2}{3}m_b')} و{m('CG = \\frac{2}{3}m_c')}!",
            f"Perpendicular medians from {m('B')} and {m('C')} always satisfy the Olympiad theorem {m('AB^2 + AC^2 = 5 \\cdot BC^2')}!",
            [
                f"In right {m('\\triangle BGC')}, Pythagoras gives {m('\\frac{4}{9}(m_b^2 + m_c^2) = a^2 \\implies 4m_b^2 + 4m_c^2 = 9a^2')}.",
                f"By Apollonius, {m('4m_b^2 + 4m_c^2 = (2a^2 + 2c^2 - b^2) + (2a^2 + 2b^2 - c^2) = 4a^2 + b^2 + c^2')}.",
                f"Equating gives {m(f'5a^2 = b^2 + c^2 = {b_s}^2 + {c_s}^2 = {5 * a_ans * a_ans} \\implies a^2 = {a_ans*a_ans} \\implies BC = {a_ans}')}!",
            ],
            f"Check: {m(f'{a_ans} + {b_s} = {a_ans + b_s} > {c_s}')}, and {m(f'5 \\times {a_ans}^2 = {5*a_ans*a_ans} = {b_s}^2 + {c_s}^2')}!",
            f"تعامد المتوسطين من {m('B')} و{m('C')} يؤدي عبر فيثاغورس وأبولونيوس إلى العلاقة الشهيرة {m('AB^2 + AC^2 = 5 \\cdot BC^2')}!",
            [
                f"في المثلث القائم {m('BGC')}: {m('BG^2 + CG^2 = BC^2 \\implies \\frac{4}{9}(m_b^2 + m_c^2) = a^2')}.",
                f"بالتعويض من أبولونيوس نجد {m('4a^2 + b^2 + c^2 = 9a^2 \\implies 5a^2 = b^2 + c^2')}.",
                f"ومنه {m(f'5 \\cdot BC^2 = {b_s}^2 + {c_s}^2 = {5*a_ans*a_ans} \\implies BC = {a_ans}')}.",
            ],
            f"تحقق: الأضلاع {m(f'{a_ans}, {b_s}, {c_s}')} تحقق متباينة المثلث وشرط تعامد المتوسطين!",
            diagram_en=svg_median_tri(str(c_s), str(b_s), "BC=?", "mᵦ⊥m𝒸"),
        )

    # 25. nsmo_g10_incircle_heron_tangents (5E, 6M, 4H)
    bp = "nsmo_g10_incircle_heron_tangents"
    easy_in = [
        (6, 8, 10),
        (8, 15, 17),
        (9, 40, 41),
        (20, 21, 29),
        (16, 30, 34),
    ]
    for a_l, b_l, c_h in easy_in:
        assert a_l * a_l + b_l * b_l == c_h * c_h
        ans = (a_l + b_l - c_h) // 2
        B.add_math(
            tp, "Easy", bp,
            f"A right-angled triangle has legs {m(a_l)} and {m(b_l)} and hypotenuse {m(c_h)}. Find the radius {m('r')} of its inscribed circle.",
            f"مثلث قائم الزاوية طولا ضلعي القائمة فيه {m(a_l)} و{m(b_l)} ووتره {m(c_h)}. أوجد نصف قطر دائرته الداخلية {m('r')}.",
            ans, [ans + 1, ans + 2, max(1, ans - 1), c_h // 2],
            f"For any right triangle with legs {m('a, b')} and hypotenuse {m('c')}, the inradius is {m('r = \\frac{a + b - c}{2}')}!",
            f"لأي مثلث قائم الزاوية ضلعاه {m('a, b')} ووتره {m('c')}، نصف قطر الدائرة الداخلية هو {m('r = \\frac{a + b - c}{2}')}!",
            f"Equal tangents around the right-angle corner form an {m('r \\times r')} square, giving {m('r = \\frac{a + b - c}{2}')}!",
            [
                f"Apply the right-triangle inradius formula: {m(f'r = \\frac{{{a_l} + {b_l} - {c_h}}}{{2}} = \\frac{{{a_l + b_l - c_h}}}{{2}} = {ans}')}.",
            ],
            f"Area check: {m(f'\\Delta = \\frac{{1}}{{2}}({a_l})({b_l}) = {a_l*b_l//2}')}, {m(f's = {(a_l+b_l+c_h)//2}')}, and {m(f'\\Delta / s = {ans}')}!",
            f"المماسان قرب الزاوية القائمة يكوّنان مربعاً طول ضلعه {m('r')} فيعطي القانون {m('r = \\frac{a + b - c}{2}')}!",
            [
                f"نعوّض مباشرة: {m(f'r = \\frac{{{a_l} + {b_l} - {c_h}}}{{2}} = {ans}')}.",
            ],
            f"تحقق بقانون المساحة: {m(f'\\Delta / s = {a_l*b_l//2} / {(a_l+b_l+c_h)//2} = {ans}')}!",
            diagram_en=svg_right_tri_incircle(str(a_l), str(b_l), str(c_h), "r=?"),
        )

    # Medium (6): 4 Heron non-right triangles r = Delta / s + 2 tangent-segment (s - a) problems!
    med_heron = [
        (13, 14, 15, 21, 84, Fraction(4, 1)),
        (10, 17, 21, 24, 84, Fraction(7, 2)),
        (15, 26, 37, 39, 156, Fraction(4, 1)),  # wait vary answer from 4: scale (13,14,15) by 2 -> (26,28,30): r=8, or (20,34,42): r=7, or (17,25,26): s=34, Delta=sqrt(34*17*9*8)=204 -> r=6!!
        (20, 34, 42, 48, 336, Fraction(7, 1)),
    ]
    med_heron[2] = (17, 25, 26, 34, 204, Fraction(6, 1))
    for a_s, b_s, c_s, s_v, area_v, r_ans in med_heron:
        assert 2 * s_v == a_s + b_s + c_s
        assert s_v * (s_v - a_s) * (s_v - b_s) * (s_v - c_s) == area_v * area_v
        assert Fraction(area_v, s_v) == r_ans
        ans_v = r_ans.numerator if r_ans.denominator == 1 else r_ans
        B.add_math(
            tp, "Medium", bp,
            f"Triangle {m('ABC')} has side lengths {m(a_s)}, {m(b_s)}, and {m(c_s)}. What is the radius {m('r')} of its inscribed circle?",
            f"مثلث {m('ABC')} أطوال أضلاعه {m(a_s)} و{m(b_s)} و{m(c_s)}. ما نصف قطر دائرته الداخلية {m('r')}؟",
            ans_v, [ans_v + 1, ans_v + 2, max(1, ans_v - 1), ans_v + 3],
            f"Compute semi-perimeter {m(f's = {s_v}')} and Heron's area {m('\\Delta = \\sqrt{s(s-a)(s-b)(s-c)}')}, then use {m('r = \\Delta / s')}!",
            f"احسب نصف المحيط {m(f's = {s_v}')} والمساحة بصيغة هيرون، ثم طبّق {m('r = \\Delta / s')}!",
            f"Find the area {m('\\Delta')} via Heron's formula and divide by the semi-perimeter {m('s')}!",
            [
                f"Semi-perimeter: {m(f's = \\frac{{{a_s} + {b_s} + {c_s}}}{{2}} = {s_v}')}.",
                f"By Heron's formula, {m(f'\\Delta = \\sqrt{{{s_v} \\cdot {s_v - a_s} \\cdot {s_v - b_s} \\cdot {s_v - c_s}}} = {area_v}')}.",
                f"Divide: {m(f'r = \\frac{{\\Delta}}{{s}} = \\frac{{{area_v}}}{{{s_v}}} = {ans_v}')}.",
            ],
            f"Shortcut check: {m('r = \\sqrt{\\frac{(s-a)(s-b)(s-c)}{s}}')} gives {m(ans_v)} directly!",
            f"نحسب المساحة بصيغة هيرون ثم نقسم على نصف المحيط {m('s')}!",
            [
                f"نصف المحيط {m(f's = {s_v}')}.",
                f"من صيغة هيرون: {m(f'\\Delta = \\sqrt{{{s_v}({s_v-a_s})({s_v-b_s})({s_v-c_s})}} = {area_v}')}.",
                f"إذن {m(f'r = \\frac{{{area_v}}}{{{s_v}}} = {ans_v}')}.",
            ],
            f"تحقق: {m('r \\cdot s = \\Delta')} متحققة بدقة.",
            diagram_en=svg_right_tri_incircle(str(a_s), str(b_s), str(c_s), "r=?"),
        )

    for ab, bc, ca in [(13, 15, 18), (17, 21, 24)]:
        s_v = (ab + bc + ca) // 2
        ans = s_v - bc
        B.add_math(
            tp, "Medium", bp,
            f"The incircle of {m('\\triangle ABC')} touches sides {m('AB')}, {m('BC')}, and {m('CA')} at {m('F')}, {m('D')}, and {m('E')}, respectively. If {m(f'AB = {ab}')}, {m(f'BC = {bc}')}, and {m(f'CA = {ca}')}, find the length of tangent segment {m('AF')}.",
            f"تمس الدائرة الداخلية للمثلث {m('ABC')} الأضلاع {m('AB')} و{m('BC')} و{m('CA')} في النقاط {m('F')} و{m('D')} و{m('E')} على الترتيب. إذا كان {m(f'AB = {ab}')} و{m(f'BC = {bc}')} و{m(f'CA = {ca}')}، فأوجد طول قطعة المماس {m('AF')}.",
            ans, [s_v - ab, s_v - ca, ans + 2, s_v],
            f"Equal tangents from {m('A, B, C')} have lengths {m('x, y, z')} with {m('x + y + z = s')} and {m('y + z = BC')} — so {m('x = s - BC')}!",
            f"المماسات من الرؤوس أطوالها {m('x, y, z')} بحيث {m('x + y + z = s')} و{m('y + z = BC')}، إذن {m('AF = s - BC')}!",
            f"Use the equal-tangents identity: the tangent from vertex {m('A')} always has length {m('s - BC')}!",
            [
                f"Compute semi-perimeter {m(f's = \\frac{{{ab} + {bc} + {ca}}}{{2}} = {s_v}')}.",
                f"Let {m('AF = AE = x')}, {m('BF = BD = y')}, {m('CD = CE = z')}. Since {m('x + y + z = s')} and {m(f'y + z = BC = {bc}')}, we get {m(f'x = {s_v} - {bc} = {ans}')}.",
            ],
            f"Check all three tangents: {m(f'x = {ans},\\; y = {ab - ans},\\; z = {ca - ans}')}, and {m(f'y + z = {bc}')}!",
            f"طول قطعة المماس من الرأس {m('A')} يساوي دائماً نصف المحيط مطروحاً منه الضلع المقابل {m('BC')}!",
            [
                f"نصف المحيط {m(f's = \\frac{{{ab} + {bc} + {ca}}}{{2}} = {s_v}')}.",
                f"بما أن {m('AF + BD + CD = s')} و{m(f'BD + CD = BC = {bc}')} فإن {m(f'AF = {s_v} - {bc} = {ans}')}.",
            ],
            f"تحقق: مجموع المماسات الثلاثة {m(f'{ans} + {ab - ans} + {ca - ans} = {s_v}')}.",
            diagram_en=svg_right_tri_incircle(str(ab), str(bc), str(ca), "AF=?"),
        )

    # Hard (4): 1 Exradius r_a = Delta / (s - a) + 3 3D cube-in-cylinder / sphere-in-cube problems with svg_cube_in_cylinder!
    B.add_math(
        tp, "Hard", bp,
        f"Triangle {m('ABC')} has side lengths {m('BC = 14')}, {m('AC = 13')}, and {m('AB = 15')}. What is the radius {m('r_a')} of the **excircle** tangent to side {m('BC')} and the extensions of {m('AB')} and {m('AC')}?",
        f"مثلث {m('ABC')} أطوال أضلاعه {m('BC = 14')} و{m('AC = 13')} و{m('AB = 15')}. ما نصف قطر **الدائرة الماسة خارجياً** {m('r_a')} التي تمس الضلع {m('BC')} وامتدادي {m('AB')} و{m('AC')}؟",
        12, [4, 8, 10, 14],
        f"Whereas the inradius is {m('r = \\Delta / s')}, the exradius opposite {m('A')} is {m('r_a = \\frac{\\Delta}{s - a}')} where {m('a = BC')}!",
        f"بينما نصف قطر الدائرة الداخلية {m('r = \\Delta / s')}، فإن نصف قطر الدائرة الخارجية المقابلة للرأس {m('A')} هو {m('r_a = \\frac{\\Delta}{s - a}')}!",
        f"Compute Heron's area {m('\\Delta = 84')} and apply the exradius formula {m('r_a = \\frac{\\Delta}{s - BC}')}!",
        [
            f"Semi-perimeter {m('s = \\frac{13 + 14 + 15}{2} = 21')}, and Heron's formula gives {m('\\Delta = \\sqrt{21 \\cdot 8 \\cdot 7 \\cdot 6} = 84')}.",
            f"For the excircle opposite {m('A')} (tangent to {m('a = BC = 14')}), {m('s - a = 21 - 14 = 7')}.",
            f"Thus {m('r_a = \\frac{\\Delta}{s - a} = \\frac{84}{7} = 12')}.",
        ],
        f"Area decomposition check: {m('\\Delta = \\frac{1}{2} r_a (b + c - a) = r_a (s - a) = 12 \\times 7 = 84')}!",
        f"نستخدم صيغة نصف قطر الدائرة الماسة خارجياً {m('r_a = \\frac{\\Delta}{s - a}')} بعد حساب المساحة بصيغة هيرون!",
        [
            f"نصف المحيط {m('s = 21')}، ومساحة المثلث بصيغة هيرون تساوي {m('\\Delta = 84')}.",
            f"بما أن الدائرة تمس الضلع {m('a = BC = 14')}، فإن {m('s - a = 21 - 14 = 7')}.",
            f"إذن {m('r_a = \\frac{84}{7} = 12')}.",
        ],
        f"تحقق: {m('r_a (s - a) = 12 \\times 7 = 84 = \\Delta')}!",
        diagram_en=svg_right_tri_incircle("13", "15", "14", "rₐ=?"),
    )

    for s_edge in (6, 8, 10):
        # Cube of edge s inscribed in a right circular cylinder (top/bottom square vertices on top/bottom circular rims):
        # Cylinder height h = s, rim diameter 2R = s*sqrt(2) -> R^2 = s^2 / 2 -> Volume V = pi * R^2 * h = (s^3 / 2) * pi! Ask V / pi!
        ans = (s_edge ** 3) // 2
        B.add_math(
            tp, "Hard", bp,
            f"A cube of edge length {m(s_edge)} is inscribed in a right circular cylinder so that the four vertices of its top face lie on the top circular rim and the four vertices of its bottom face lie on the bottom rim. If the cylinder's volume is {m('K\\pi')}, find {m('K')}.",
            f"مكعب طول حرفه {m(s_edge)} مرسوم داخل أسطوانة دائرية قائمة بحيث تقع رؤوس وجهه العلوي الأربعة على محيط القاعدة العليا ورؤوس وجهه السفلي على محيط القاعدة السفلى. إذا كان حجم الأسطوانة {m('K\\pi')}، فأوجد قيمة {m('K')}.",
            ans, [s_edge ** 3, (s_edge ** 3) // 4, ans + s_edge * s_edge, (s_edge ** 2) // 2],
            f"Look at the top circular base: a square of side {m(s_edge)} is inscribed in the circle, so the circle's diameter equals the square's diagonal {m(f'{s_edge}\\sqrt{{2}}')}!",
            f"انظر إلى القاعدة الدائرية العليا: المربع الذي ضلعه {m(s_edge)} مرسوم داخل الدائرة، فقطر الدائرة يساوي قطر المربع {m(f'{s_edge}\\sqrt{{2}}')}!",
            f"Match the cylinder's height {m(f'h = {s_edge}')} and circular base diameter {m(f'2R = {s_edge}\\sqrt{{2}}')}!",
            [
                f"The cylinder's height equals the cube's vertical edge: {m(f'h = {s_edge}')}.",
                f"On the circular base, the inscribed {m(f'{s_edge} \\times {s_edge}')} square has diagonal {m(f'2R = {s_edge}\\sqrt{{2}}')}, so {m(f'R^2 = \\frac{{{s_edge}^2}}{{2}} = {(s_edge*s_edge)//2}')}.",
                f"Cylinder volume is {m(f'\\pi R^2 h = \\pi \\times {(s_edge*s_edge)//2} \\times {s_edge} = {ans}\\pi')}, giving {m(f'K = {ans}')}.",
            ],
            f"Trap check: an **inscribed** cylinder inside the cube has {m('R = s/2')}, whereas a **circumscribed** cylinder around the cube has {m('R = s/\\sqrt{2}')} ({m('2\\times')} larger base area)!",
            f"قطر دائرة القاعدة يساوي قطر وجه المكعب {m(f'{s_edge}\\sqrt{{2}}')} بينما ارتفاع الأسطوانة يساوي حرف المكعب {m(s_edge)}!",
            [
                f"ارتفاع الأسطوانة {m(f'h = {s_edge}')}.",
                f"قطر القاعدة الدائرية {m(f'2R = {s_edge}\\sqrt{{2}}')} ومنه {m(f'R^2 = \\frac{{{s_edge}^2}}{{2}} = {(s_edge*s_edge)//2}')}.",
                f"الحجم يساوي {m(f'\\pi R^2 h = {ans}\\pi')}، إذن {m(f'K = {ans}')}.",
            ],
            f"تحقق: انتبه للفرق بين الأسطوانة المحيطة بالمكعب ({m('R = s/\\sqrt{2}')}) والأسطوانة المرسومة داخله ({m('R = s/2')})!",
            diagram_en=svg_cube_in_cylinder(str(s_edge)),
        )


# =============================================================================
# UNIT 3.6 — Derangements, Recurrences, Graphs & Conditional Probability (75 Qs)
# =============================================================================
def _add_unit_3_6(B: BankBuilder) -> None:
    from nsmo_common import svg_regular_polygon, svg_spinner, svg_two_jars

    tp = "Combinatorics & Logic"

    def _derange(n: int) -> int:
        d = [1, 0]
        for k in range(2, n + 1):
            d.append((k - 1) * (d[-1] + d[-2]))
        return d[n]

    # 26. nsmo_g10_derangements_circular_seating (5E, 6M, 4H) — SVG: svg_round_table / svg_digit_slots
    bp = "nsmo_g10_derangements_circular_seating"
    # Easy (5): Circular seating of n people around a round table, or with 2 specific friends adjacent
    easy_circ = [
        (5, False),  # (5-1)! = 24
        (6, False),  # (6-1)! = 120
        (7, False),  # (7-1)! = 720
        (6, True),   # 2 friends together around 6-seat round table: 2! * (5-1)! = 48
        (7, True),   # 2 friends together around 7-seat round table: 2! * (6-1)! = 240
    ]
    for n_p, pair_adj in easy_circ:
        if not pair_adj:
            ans = math.factorial(n_p - 1)
            B.add_math(
                tp, "Easy", bp,
                f"In how many distinguishable ways can {m(n_p)} Mawhiba finalists be seated around a circular discussion table if two seatings that differ only by a rotation are considered identical?",
                f"بكم طريقة متمايزة يمكن جلوس {m(n_p)} طلاب متأهلين في أولمبياد موهبة حول طاولة مستديرة للنقاش إذا اعتُبرت الترتيبات الناتجة عن دوران الطاولة متطابقة؟",
                ans, [math.factorial(n_p), math.factorial(n_p - 1) // 2, math.factorial(n_p - 2), ans + n_p],
                f"Fix one student's seat to break rotational symmetry, then arrange the remaining {m(n_p - 1)} students in a line!",
                f"ثبّت مقعد أحد الطلاب لكسر التماثل الدوراني، ثم رتّب الطلاب الـ {m(n_p - 1)} الباقين خطياً!",
                f"Eliminate rotational duplicates by anchoring one person: {m(f'({n_p} - 1)!')} circular permutations!",
                [
                    f"Around a circle of {m(n_p)} seats, rotating everyone clockwise produces {m(n_p)} identical relative arrangements.",
                    f"Dividing {m(f'{n_p}!')} linear permutations by {m(n_p)} gives {m(f'({n_p} - 1)! = {n_p - 1}! = {ans}')}.",
                ],
                f"Sanity check: fixing Student 1 at the north chair leaves {m(f'{n_p - 1}! = {ans}')} ways to seat the others clockwise!",
                f"نقسم التباديل الخطية {m(f'{n_p}!')} على عدد الدورانات {m(n_p)} فنحصل على {m(f'({n_p} - 1)!')}!",
                [
                    f"تثبيت مقعد طالب واحد يلغي التكرارات الدورانية حول الطاولة المستديرة.",
                    f"يتبقى {m(n_p - 1)} مقاعد للطلاب الباقين بعدد طرق {m(f'{n_p - 1}! = {ans}')}.",
                ],
                f"تحقق: {m(f'{n_p}! / {n_p} = {ans}')}.",
                diagram_en=svg_round_table(min(n_p, 8), highlight_adj=False),
            )
        else:
            ans = 2 * math.factorial(n_p - 2)
            B.add_math(
                tp, "Easy", bp,
                f"{m(n_p)} delegates sit around a circular table (rotations considered identical). In how many ways can they sit so that two specific delegates, Tariq and Salman, sit in **adjacent** chairs?",
                f"يجلس {m(n_p)} مندوبين حول طاولة مستديرة (مع اعتبار الدورانات متطابقة). بكم طريقة يمكنهم الجلوس بحيث يجلس طارق وسلمان في مقعدين **متجاورين**؟",
                ans, [math.factorial(n_p - 2), math.factorial(n_p - 1), 2 * math.factorial(n_p - 1), ans // 2 + 6],
                f"Fuse Tariq and Salman into a single block of {m(1)} super-person, arrange {m(n_p - 1)} units around the circle, and multiply by {m('2!')}!",
                f"ادمج طارقاً وسلمان في كتلة واحدة، ورتّب {m(n_p - 1)} عناصر دائرياً، ثم اضرب في {m('2!')}!",
                f"Use block-gluing on the circle: {m(n_p - 1)} units give {m(f'({n_p - 1} - 1)!')} circular orders times {m(2)} internal swaps!",
                [
                    f"Treat the pair {{Tariq, Salman}} as a single block; together with the {m(n_p - 2)} other delegates there are {m(n_p - 1)} circular units.",
                    f"Those {m(n_p - 1)} units can be arranged around a round table in {m(f'({n_p - 2})! = {math.factorial(n_p - 2)}')} ways.",
                    f"Tariq and Salman can swap seats within their block in {m('2! = 2')} ways, giving {m(f'2 \\times {math.factorial(n_p - 2)} = {ans}')}.",
                ],
                f"Complement check: non-adjacent seatings equal {m(f'{math.factorial(n_p - 1)} - {ans} = {math.factorial(n_p - 1) - ans}')}!",
                f"ندمج الصديقين في وحدة واحدة فيصبح لدينا {m(n_p - 1)} وحدات حول الدائرة مع تبديل داخلي بطريقتين!",
                [
                    f"عدد طرق ترتيب {m(n_p - 1)} وحدات حول طاولة مستديرة هو {m(f'({n_p - 2})! = {math.factorial(n_p - 2)}')}.",
                    f"نضرب في {m('2!')} لتبديل موقعي طارق وسلمان داخل الكتلة: {m(f'2 \\times {math.factorial(n_p - 2)} = {ans}')}.",
                ],
                f"تحقق: الترتيبات الكلية {m(math.factorial(n_p - 1))} وهو أكبر من {m(ans)} كما هو متوقع.",
                diagram_en=svg_round_table(min(n_p, 8), highlight_adj=True),
            )

    # Medium (6): Partial derangements — permutations of n items where exact k items stay in their own place: C(n, k) * D_{n-k}
    med_der = [
        (4, 0),  # D_4 = 9
        (5, 0),  # D_5 = 44
        (5, 1),  # C(5,1)*D_4 = 5*9 = 45
        (5, 2),  # C(5,2)*D_3 = 10*2 = 20
        (6, 2),  # C(6,2)*D_4 = 15*9 = 135
        (6, 1),  # C(6,1)*D_5 = 6*44 = 264
    ]
    for n_d, k_fix in med_der:
        ans = math.comb(n_d, k_fix) * _derange(n_d - k_fix)
        if k_fix == 0:
            B.add_math(
                tp, "Medium", bp,
                f"{m(n_d)} lab coats, each labeled with a different researcher's name, are handed back randomly, one to each of the {m(n_d)} researchers. In how many ways does **nobody** receive their own lab coat?",
                f"وُزّعت {m(n_d)} معاطف مختبر يحمل كلٌّ منها اسم باحث مختلف عشوائياً على الباحثين الـ {m(n_d)} (معطف لكل باحث). بكم طريقة **لا يستلم أي باحث** معطفه الصحيح؟",
                ans, [math.factorial(n_d) // 2, ans + 1, ans - 2, math.factorial(n_d - 1)],
                f"Apply the derangement recurrence {m('D_n = (n-1)(D_{n-1} + D_{n-2})')} starting from {m('D_1 = 0,\\; D_2 = 1')}!",
                f"طبّق علاقة التبديلات الخالية من النقاط الثابتة {m('D_n = (n-1)(D_{n-1} + D_{n-2})')} بدءاً من {m('D_1 = 0,\\; D_2 = 1')}!",
                f"Count full derangements {m(f'D_{{{n_d}}}')} using {m('D_1 = 0,\\; D_2 = 1,\\; D_3 = 2,\\; D_4 = 9,\\; D_5 = 44')}!",
                [
                    f"A permutation with zero fixed points is a **derangement** {m(f'D_{{{n_d}}}')}.",
                    f"Using {m('D_k = (k-1)(D_{k-1} + D_{k-2})')}: {m('D_1 = 0,\\; D_2 = 1,\\; D_3 = 2,\\; D_4 = 9')}" + (f", and {m('D_5 = 4(9 + 2) = 44')}." if n_d == 5 else "."),
                    f"Thus there are {m(ans)} valid derangements.",
                ],
                f"Inclusion-Exclusion check: {m(f'{n_d}! \\left(1 - 1 + \\frac{{1}}{{2!}} - \\frac{{1}}{{3!}} + \\cdots\\right) = {ans}')}!",
                f"نحسب عدد التبديلات الخالية من النقاط الثابتة {m(f'D_{{{n_d}}}')} بالعلاقة التكرارية!",
                [
                    f"نبدأ بالقيم الأساسية: {m('D_1 = 0')}، {m('D_2 = 1')}، {m('D_3 = 2')}، {m('D_4 = 9')}.",
                    f"نجد أن عدد الطرق التي لا يستلم فيها أحد معطفه الصحيح يساوي {m(ans)}.",
                ],
                f"تحقق بمبدأ الشمول والإقصاء: الناتج يطابق {m(ans)} تماماً.",
                diagram_en=svg_digit_slots([f"≠{i+1}" for i in range(min(n_d, 5))], f"Derangement D_{n_d}"),
            )
        else:
            B.add_math(
                tp, "Medium", bp,
                f"A postman delivers {m(n_d)} distinct letters into {m(n_d)} addressed mailboxes, one letter per box. In how many ways do **exact {m(k_fix)}** letters land in their correct mailboxes while the remaining {m(n_d - k_fix)} are all misdelivered?",
                f"يضع ساعي بريد {m(n_d)} رسائل مختلفة في {m(n_d)} صناديق معنونة (رسالة في كل صندوق). بكم طريقة تصل **بالضبط {m(k_fix)}** رسائل إلى صناديقها الصحيحة بينما توضع جميع الرسائل الـ {m(n_d - k_fix)} الباقية في صناديق خاطئة؟",
                ans, [math.comb(n_d, k_fix) * math.factorial(n_d - k_fix), ans + math.comb(n_d, k_fix), max(1, ans - 5), _derange(n_d)],
                f"First choose which {m(k_fix)} letters go to the right mailbox in {m(f'\\binom{{{n_d}}}{{{k_fix}}}')} ways, then derange the other {m(n_d - k_fix)}!",
                f"اختر أولاً الرسائل الـ {m(k_fix)} الصحيحة بـ {m(f'\\binom{{{n_d}}}{{{k_fix}}}')} طريقة، ثم طبّق التبديل الخالي من النقاط الثابتة على الـ {m(n_d - k_fix)} الباقية!",
                f"Multiply fixed-point selection {m(f'\\binom{{{n_d}}}{{{k_fix}}}')} by the derangement count {m(f'D_{{{n_d - k_fix}}}')}!",
                [
                    f"Choose which {m(k_fix)} of the {m(n_d)} mailboxes receive their own letter: {m(f'\\binom{{{n_d}}}{{{k_fix}}} = {math.comb(n_d, k_fix)}')} ways.",
                    f"Every one of the remaining {m(n_d - k_fix)} letters must miss its own box, which happens in {m(f'D_{{{n_d - k_fix}}} = {_derange(n_d - k_fix)}')} ways.",
                    f"By the multiplication principle, total ways = {m(f'{math.comb(n_d, k_fix)} \\times {_derange(n_d - k_fix)} = {ans}')}.",
                ],
                f"Remember: summing {m(f'\\binom{{{n_d}}}{{k}} D_{{{n_d}-k}}')} over {m(f'k = 0, \\dots, {n_d}')} reconstructs all {m(f'{n_d}! = {math.factorial(n_d)}')} permutations!",
                f"نضرب عدد طرق اختيار النقاط الثابتة {m(f'\\binom{{{n_d}}}{{{k_fix}}}')} في عدد تبديلات الإزاحة الكاملة {m(f'D_{{{n_d - k_fix}}}')}!",
                [
                    f"اختيار {m(k_fix)} رسائل صحيحة يتم بـ {m(f'\\binom{{{n_d}}}{{{k_fix}}} = {math.comb(n_d, k_fix)}')} طريقة.",
                    f"توزيع الـ {m(n_d - k_fix)} الباقية بحيث لا تصيب أي منها صندوقها يتم بـ {m(f'D_{{{n_d - k_fix}}} = {_derange(n_d - k_fix)}')} طريقة.",
                    f"حاصل الضرب يساوي {m(f'{math.comb(n_d, k_fix)} \\times {_derange(n_d - k_fix)} = {ans}')}.",
                ],
                f"تحقق: مجموع جميع الحالات من {m('k=0')} إلى {m(n_d)} يساوي {m(f'{n_d}!')}.",
            )

    # Hard (4): Circular seating of a adults and b children (b <= a) with NO two children adjacent: (a-1)! * P(a, b), plus D_6 = 265!
    B.add_math(
        tp, "Hard", bp,
        f"Six competitors hand in {m(6)} distinct calculators before a break and receive them back at random (one each). In how many ways does **not a single competitor** get their own calculator back?",
        f"سلّم ستة متسابقين {m(6)} آلات حاسبة مميزة قبل الاستراحة ثم استلموها عشوائياً (واحدة لكل متسابق). بكم طريقة **لا يستلم أي متسابق** آلته الخاصة؟",
        265, [264, 240, 360, 185],
        f"Use {m('D_6 = 5(D_5 + D_4)')} with {m('D_4 = 9')} and {m('D_5 = 44')}!",
        f"استخدم العلاقة {m('D_6 = 5(D_5 + D_4)')} مع {m('D_4 = 9')} و{m('D_5 = 44')}!",
        f"Step the derangement recurrence one level further: {m('D_6 = 5(D_5 + D_4)')}!",
        [
            f"From {m('D_1 = 0,\\; D_2 = 1,\\; D_3 = 2')}, we compute {m('D_4 = 3(2+1) = 9')} and {m('D_5 = 4(9+2) = 44')}.",
            f"Applying {m('D_n = (n-1)(D_{n-1} + D_{n-2})')} for {m('n = 6')} gives {m('D_6 = 5(44 + 9) = 5 \\times 53 = 265')}.",
        ],
        f"Closest-integer shortcut check: {m('6! / e \\approx 720 / 2.71828 \\approx 264.87')}, whose nearest integer is {m(265)}!",
        f"نطبّق العلاقة التكرارية للتبديلات الخالية من النقاط الثابتة عند {m('n = 6')}: {m('D_6 = 5(D_5 + D_4)')}!",
        [
            f"نعلم أن {m('D_4 = 9')} و{m('D_5 = 44')}.",
            f"إذن {m('D_6 = 5 \\times (44 + 9) = 5 \\times 53 = 265')}.",
        ],
        f"تحقق: الكسر {m('D_6 / 6! = 265 / 720')} يقترب جداً من {m('1/e \\approx 0.368')}.",
    )
    for n_ad, n_ch in [(4, 3), (5, 3), (5, 4)]:
        ans = math.factorial(n_ad - 1) * math.perm(n_ad, n_ch)
        B.add_math(
            tp, "Hard", bp,
            f"Around a circular banquet table (rotations identical), {m(n_ad)} mentors and {m(n_ch)} junior students are seated so that **no two junior students** sit next to each other. How many seating arrangements are possible?",
            f"حول طاولة دائرية (الدورانات متطابقة)، يجلس {m(n_ad)} مشرفين و{m(n_ch)} طلاب ناشئين بحيث **لا يجلس أي طالبين ناشئين متجاورين**. كم ترتيباً مختلفاً للجلوس يمكن تكوينه؟",
            ans, [math.factorial(n_ad) * math.perm(n_ad, n_ch), math.factorial(n_ad - 1) * math.comb(n_ad, n_ch), ans // 2, ans + math.factorial(n_ad)],
            f"Seat the {m(n_ad)} mentors around the circle first in {m(f'({n_ad}-1)!')} ways—creating exact {m(n_ad)} gaps between them!",
            f"أجلس المشرفين الـ {m(n_ad)} حول الدائرة أولاً بـ {m(f'({n_ad}-1)!')} طريقة، فتنشأ بينهم {m(n_ad)} فراغات بالضبط!",
            f"Seat mentors circularly to form {m(n_ad)} distinct gaps, then place at most one student per gap!",
            [
                f"Arrange the {m(n_ad)} mentors around the circular table in {m(f'({n_ad} - 1)! = {math.factorial(n_ad - 1)}')} ways.",
                f"Around a circle, {m(n_ad)} seated mentors create exact **{m(n_ad)}** distinct spaces between adjacent mentors.",
                f"Choose and fill {m(n_ch)} of those {m(n_ad)} gaps with the {m(n_ch)} distinct students in {m(f'P({n_ad}, {n_ch}) = {math.perm(n_ad, n_ch)}')} ways, giving {m(f'{math.factorial(n_ad - 1)} \\times {math.perm(n_ad, n_ch)} = {ans}')}.",
            ],
            f"Trap check: on a **line**, {m(n_ad)} mentors create {m(n_ad + 1)} gaps, whereas on a **circle** they create exact {m(n_ad)} gaps!",
            f"نجلس المشرفين أولاً حول الدائرة فتنشأ {m(n_ad)} فراغات متمايزة نضع في كلٍّ منها طالباً واحداً على الأكثر!",
            [
                f"ترتيب {m(n_ad)} مشرفين حول طاولة دائرية يتم بـ {m(f'({n_ad} - 1)! = {math.factorial(n_ad - 1)}')} طريقة.",
                f"يتكوّن بين المشرفين حول الدائرة **{m(n_ad)}** فراغاً بالضبط.",
                f"توزيع الطلاب الـ {m(n_ch)} في هذه الفراغات يتم بـ {m(f'P({n_ad}, {n_ch}) = {math.perm(n_ad, n_ch)}')} طريقة، فالإجمالي {m(ans)}.",
            ],
            f"انتبه للفخ: على الدائرة عدد الفراغات يساوي {m(n_ad)} وليس {m(n_ad + 1)} كما في الصف المستقيم!",
            diagram_en=svg_round_table(min(n_ad + n_ch, 8), highlight_adj=False),
        )

    # 27. nsmo_g10_fibonacci_tiling_no_consec (5E, 6M, 4H) — SVG: svg_polyomino / svg_binary_bulbs
    bp = "nsmo_g10_fibonacci_tiling_no_consec"
    def _fib_tiling(n: int) -> int:
        # ways to tile 2 x n with 1x2 dominoes: f(0)=1, f(1)=1, f(2)=2, f(3)=3, ...
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # Easy (5): 2 x n rectangle domino tilings for n = 5, 6, 7, 8, 9
    for n_dom in (5, 6, 7, 8, 9):
        ans = _fib_tiling(n_dom)
        B.add_math(
            tp, "Easy", bp,
            f"In how many ways can a {m(f'2 \\times {n_dom}')} rectangular corridor be completely tiled using identical {m('1 \\times 2')} domino tiles (rotations of tiles allowed)?",
            f"بكم طريقة يمكن تبليط ممر مستطيل أبعاده {m(f'2 \\times {n_dom}')} بالكامل باستخدام بلاطات دومينو متطابقة أبعاد كل منها {m('1 \\times 2')}؟",
            ans, [_fib_tiling(n_dom - 1), _fib_tiling(n_dom + 1), 2 ** (n_dom - 2), ans + 3],
            f"Look at the leftmost column of the {m(f'2 \\times {n_dom}')} board: either {m(1)} vertical domino leaves {m(f'2 \\times ({n_dom}-1)')}, or {m(2)} stacked horizontal dominoes leave {m(f'2 \\times ({n_dom}-2)')}!",
            f"انظر إلى العمود الأول: إما بلاطة رأسية واحدة تترك {m(f'2 \\times ({n_dom}-1)')}، أو بلاطتان أفقيتان تتركان {m(f'2 \\times ({n_dom}-2)')}!",
            f"Condition on the first column to get the Fibonacci recurrence {m('T_n = T_{n-1} + T_{n-2}')} with {m('T_1 = 1,\\; T_2 = 2')}!",
            [
                f"Let {m('T_k')} be the number of tilings of a {m('2 \\times k')} board. Clearly {m('T_1 = 1')} and {m('T_2 = 2')}.",
                f"Every tiling of {m('2 \\times k')} starts with either one vertical domino ({m('T_{k-1}')} ways) or two horizontal dominoes ({m('T_{k-2}')} ways), so {m('T_k = T_{k-1} + T_{k-2}')}.",
                f"Generating the sequence {m('1, 2, 3, 5, 8, 13, 21, 34, 55, \\dots')} gives {m(f'T_{{{n_dom}}} = {ans}')}.",
            ],
            f"Recurrence check: {m(f'T_{{{n_dom - 1}}} + T_{{{n_dom - 2}}} = {_fib_tiling(n_dom - 1)} + {_fib_tiling(n_dom - 2)} = {ans}')}!",
            f"عدد التبليطات يحقق متتالية فيبوناتشي {m('T_n = T_{n-1} + T_{n-2}')} مع {m('T_1 = 1,\\; T_2 = 2')}!",
            [
                f"نعرّف {m('T_k')} عدد طرق تبليط {m('2 \\times k')}؛ حيث {m('T_1 = 1')} و{m('T_2 = 2')}.",
                f"من العلاقة {m('T_k = T_{k-1} + T_{k-2}')} نولّد القيم المتتالية حتى نجد {m(f'T_{{{n_dom}}} = {ans}')}.",
            ],
            f"تحقق: {m(f'{_fib_tiling(n_dom - 1)} + {_fib_tiling(n_dom - 2)} = {ans}')}.",
            diagram_en=svg_polyomino([(c, r) for c in range(min(n_dom, 6)) for r in range(2)], f"2 × {n_dom} domino tiling"),
        )

    # Medium (6): Binary strings of length n with NO two consecutive 1s -> F_{n+2} = _fib_tiling(n+1)
    for n_bs in (4, 5, 6, 7, 8, 9):
        ans = _fib_tiling(n_bs + 1)
        B.add_math(
            tp, "Medium", bp,
            f"How many binary strings of length {m(n_bs)} (made of digits {m('0')} and {m('1')}) contain **no two consecutive {m('1')}'s**?",
            f"كم سلسلة ثنائية طولها {m(n_bs)} (مكوّنة من الرقمين {m('0')} و{m('1')}) **لا تحتوي على رقمي {m('1')} متجاورين**؟",
            ans, [2 ** n_bs - (n_bs - 1), _fib_tiling(n_bs), _fib_tiling(n_bs + 2), ans + 2],
            f"Split valid length-{m('n')} strings by how they start: `{0}...` leaves any valid length-{m('n-1')} string, while `{10}...` leaves any valid length-{m('n-2')} string!",
            f"قسّم السلاسل الصالحة حسب بدايتها: البدء بـ `0` يترك سلسلة طولها {m('n-1')}، والبدء بـ `10` يترك سلسلة طولها {m('n-2')}!",
            f"Use {m('a_n = a_{n-1} + a_{n-2}')} with **shifted** initial values {m('a_1 = 2')} (`0`, `1`) and {m('a_2 = 3')} (`00`, `01`, `10`)!",
            [
                f"For {m('n = 1')} there are {m('a_1 = 2')} valid strings (`0`, `1`), and for {m('n = 2')} there are {m('a_2 = 3')} (`00`, `01`, `10`).",
                f"Ending in `0` gives {m('a_{n-1}')} strings, while ending in `1` forces the previous bit to be `0`, giving {m('a_{n-2}')} strings; thus {m('a_n = a_{n-1} + a_{n-2}')}.",
                f"Stepping {m('2, 3, 5, 8, 13, 21, 34, 55, 89')} up to {m(f'n = {n_bs}')} yields {m(f'a_{{{n_bs}}} = {ans}')}.",
            ],
            f"Watch the index shift: {m(f'a_1 = 2 = F_3')}, so {m(f'a_{{{n_bs}}} = F_{{{n_bs + 2}}} = {ans}')} (not {m(f'F_{{{n_bs}}} = {_fib_tiling(n_bs - 1)}')})!",
            f"نتتبع العلاقة {m('a_n = a_{n-1} + a_{n-2}')} مع الانتباه لقيمتي البداية {m('a_1 = 2')} و{m('a_2 = 3')}!",
            [
                f"لدينا {m('a_1 = 2')} و{m('a_2 = 3')}.",
                f"بما أن كل سلسلة تنتهي بـ `0` أو `01` فإن {m('a_n = a_{n-1} + a_{n-2}')}.",
                f"بحساب الحدود المتتالية نجد {m(f'a_{{{n_bs}}} = {ans}')}.",
            ],
            f"تحقق: انتبه للإزاحة {m(f'a_{{{n_bs}}} = F_{{{n_bs + 2}}} = {ans}')}!",
            diagram_en=svg_binary_bulbs((1, 0, 1, 0, 1), tuple(range(1, 6))),
        )

    # Hard (4): Circular subsets with no adjacent elements (Lucas L_n = F_{n-1} + F_{n+1} for n >= 3) & Tribonacci stairs {1,2,3}
    # Lucas L_n: L_1=1, L_2=3, L_3=4, L_4=7, L_5=11, L_6=18, L_7=29, L_8=47, L_9=76
    def _lucas(n: int) -> int:
        l0, l1 = 2, 1
        for _ in range(n):
            l0, l1 = l1, l0 + l1
        return l0

    for n_cyc in (6, 7, 8):
        ans = _lucas(n_cyc)
        B.add_math(
            tp, "Hard", bp,
            f"{m(n_cyc)} numbered lamps {m(f'1, 2, \\dots, {n_cyc}')} are arranged in a **circle**. How many subsets of lamps (including the empty subset) can be switched ON so that **no two adjacent lamps** around the circle are both ON?",
            f"وُضعت {m(n_cyc)} مصابيح مرقمة {m(f'1, 2, \\dots, {n_cyc}')} في **دائرة**. بكم طريقة يمكن إضاءة مجموعة جزئية منها (بما في ذلك إبقاء الكل مطفأً) بحيث **لا يضيء مصباحان متجاوران** على الدائرة معاً؟",
            ans, [_fib_tiling(n_cyc + 1), ans - 2, ans + 3, 2 ** (n_cyc - 2)],
            f"Casework on Lamp {m(1)}: if Lamp {m(1)} is OFF, lamps {m(f'2..{n_cyc}')} form a line of length {m(n_cyc - 1)}; if Lamp {m(1)} is ON, lamps {m(2)} and {m(n_cyc)} must be OFF, leaving a line of length {m(n_cyc - 3)}!",
            f"افصل حالتي المصباح {m(1)}: إذا كان مطفأً يتبقى صف طوله {m(n_cyc - 1)}، وإذا كان مضاءً يُطفأ جيرانه {m(2)} و{m(n_cyc)} فيتبقى صف طوله {m(n_cyc - 3)}!",
            f"Break the circle at Lamp 1 to express circular subsets as {m('a_{n-1} + a_{n-3} = L_n')} (Lucas numbers)!",
            [
                f"Recall that on a **line** of {m('k')} lamps, valid subsets with no adjacent ON lamps equal {m('a_k')}, where {m('a_0 = 1, a_1 = 2, a_2 = 3, a_3 = 5, a_4 = 8, a_5 = 13, a_6 = 21, a_7 = 34')}.",
                f"Case 1 (Lamp 1 OFF): lamps {m(f'2, \\dots, {n_cyc}')} form a line of {m(n_cyc - 1)} lamps -> {m(f'a_{{{n_cyc - 1}}} = {_fib_tiling(n_cyc)}')} ways.",
                f"Case 2 (Lamp 1 ON): neighbors {m(2)} and {m(n_cyc)} are forced OFF, leaving lamps {m(f'3, \\dots, {n_cyc - 1}')} as a line of {m(n_cyc - 3)} lamps -> {m(f'a_{{{n_cyc - 3}}} = {_fib_tiling(n_cyc - 2)}')} ways. Total = {m(f'{_fib_tiling(n_cyc)} + {_fib_tiling(n_cyc - 2)} = {ans}')}.",
            ],
            f"Compare with a line: closing the circle forbids the {m(_fib_tiling(n_cyc + 1) - ans)} linear patterns where both Lamp 1 and Lamp {m(n_cyc)} were ON!",
            f"نفتح الدائرة عند المصباح {m(1)} فنحصل على مجموع حالتين من السلاسل الخطية {m(f'a_{{{n_cyc - 1}}} + a_{{{n_cyc - 3}}}')} (أعداد لوكاس)!",
            [
                f"في الصف المستقيم الذي طوله {m('k')} يكون عدد الاختيارات الصالحة {m('a_k')} حيث {m('a_1=2, a_2=3, a_3=5, a_4=8, a_5=13, a_6=21, a_7=34')}.",
                f"إذا كان المصباح {m(1)} مطفأً نحصل على {m(f'a_{{{n_cyc - 1}}} = {_fib_tiling(n_cyc)}')} طريقة، وإذا كان مضاءً يُجبر {m(2)} و{m(n_cyc)} على الانطفاء فنحصل على {m(f'a_{{{n_cyc - 3}}} = {_fib_tiling(n_cyc - 2)}')} طريقة.",
                f"المجموع يساوي {m(f'{_fib_tiling(n_cyc)} + {_fib_tiling(n_cyc - 2)} = {ans}')}.",
            ],
            f"تحقق: أعداد لوكاس المتتالية هي {m('4, 7, 11, 18, 29, 47')} وعند {m(f'n = {n_cyc}')} القيمة {m(ans)} فعلاً!",
            diagram_en=svg_round_table(n_cyc, highlight_adj=True),
        )

    # 4th Hard: Tribonacci staircase with steps 1, 2, or 3 for n = 7 -> T(0)=1, T(1)=1, T(2)=2, T(3)=4, T(4)=7, T(5)=13, T(6)=24, T(7)=44!
    B.add_math(
        tp, "Hard", bp,
        f"A robot climbs a staircase of {m(7)} steps. In each move it may climb {m(1)}, {m(2)}, or {m(3)} steps at a time. In how many distinct sequences of moves can it reach the top?",
        f"يصعد روبوت سلّماً مكوّناً من {m(7)} درجات، وفي كل حركة يمكنه صعود درجة واحدة أو درجتين أو {m(3)} درجات. بكم متتالية مختلفة من الحركات يمكنه الوصول إلى قمة السلّم؟",
        44, [21, 24, 34, 81],
        f"Condition on the **last** jump (size {m(1)}, {m(2)}, or {m(3)}) to get the 3-term recurrence {m('S_n = S_{n-1} + S_{n-2} + S_{n-3}')}!",
        f"افرز حسب القفزة **الأخيرة** ({m('1')} أو {m('2')} أو {m('3')} درجات) لتحصل على العلاقة الثلاثية {m('S_n = S_{n-1} + S_{n-2} + S_{n-3}')}!",
        f"Build the Tribonacci table {m('S_n = S_{n-1} + S_{n-2} + S_{n-3}')} from {m('S_0 = 1,\\; S_1 = 1,\\; S_2 = 2')}!",
        [
            f"Base counts: {m('S_0 = 1')}, {m('S_1 = 1')}, {m('S_2 = 2')}, and {m('S_3 = 1 + 1 + 2 = 4')}.",
            f"Apply {m('S_n = S_{n-1} + S_{n-2} + S_{n-3}')}: {m('S_4 = 7')}, {m('S_5 = 13')}, {m('S_6 = 24')}, and {m('S_7 = 24 + 13 + 7 = 44')}.",
        ],
        f"Check {m('S_3 = 4')}: `(1,1,1), (1,2), (2,1), (3)` — all base values match!",
        f"نستخدم علاقة تريبوناتشي {m('S_n = S_{n-1} + S_{n-2} + S_{n-3}')} بدءاً من {m('S_0 = 1, S_1 = 1, S_2 = 2')}!",
        [
            f"القيم الابتدائية: {m('S_1 = 1')}، {m('S_2 = 2')}، {m('S_3 = 4')}.",
            f"بجمع آخر ثلاثة حدود تباعاً: {m('S_4 = 7')}، {m('S_5 = 13')}، {m('S_6 = 24')}، ومنه {m('S_7 = 24 + 13 + 7 = 44')}.",
        ],
        f"تحقق: {m('24 + 13 + 7 = 44')}.",
        diagram_en=svg_number_strip(["1", "2", "4", "7", "13", "24", "44"]),
    )

    # 28. nsmo_g10_graph_degrees_chords (5E, 6M, 4H) — SVG: svg_graph_cycle_chords / svg_regular_polygon
    bp = "nsmo_g10_graph_degrees_chords"
    # Easy (5): Regular graph edges n*d / 2 or sum of degrees = 2|E|
    easy_gr = [
        (8, 3),   # 12 edges
        (10, 3),  # 15 edges
        (10, 4),  # 20 edges
        (12, 5),  # 30 edges
        (9, 4),   # 18 edges
    ]
    for n_v, deg_k in easy_gr:
        ans = (n_v * deg_k) // 2
        B.add_math(
            tp, "Easy", bp,
            f"In a computer network of {m(n_v)} servers, every server is directly wired to exact {m(deg_k)} other servers. How many direct cables are in the network?",
            f"في شبكة حاسوبية تضم {m(n_v)} خوادم، يرتبط كل خادم مباشرةً بـ {m(deg_k)} خوادم أخرى بالضبط. كم كابلاً مباشراً يوجد في الشبكة؟",
            ans, [n_v * deg_k, math.comb(n_v, 2), ans + n_v // 2, ans - deg_k],
            f"Multiplying {m(f'{n_v} \\times {deg_k}')} counts **both ends** of every cable—divide by {m(2)}!",
            f"حاصل الضرب {m(f'{n_v} \\times {deg_k}')} يحسب **طرفي** كل كابل مرتين — اقسم على {m(2)}!",
            f"Apply Euler's Handshaking Lemma {m('\\sum \\deg(v) = 2|E|')}!",
            [
                f"Summing the {m(deg_k)} connections across all {m(n_v)} servers gives {m(f'{n_v} \\times {deg_k} = {n_v * deg_k}')} cable endpoints.",
                f"Since each cable has exact {m(2)} endpoints, the number of cables is {m(f'\\frac{{{n_v * deg_k}}}{{2}} = {ans}')}.",
            ],
            f"Check: {m(f'2|E| = {2 * ans} = {n_v} \\times {deg_k}')}, and {m(f'{deg_k} < {n_v}')} so a simple {m(deg_k)}-regular graph exists!",
            f"بتطبيق مبرهنة المصافحات لأويلر {m('\\sum \\deg(v) = 2|E|')} نقسم مجموع الدرجات على {m(2)}!",
            [
                f"مجموع درجات الرؤوس يساوي {m(f'{n_v} \\times {deg_k} = {n_v * deg_k}')}.",
                f"عدد الحواف (الكابلات) يساوي {m(f'{n_v * deg_k} \\div 2 = {ans}')}.",
            ],
            f"تحقق: لو نسيت القسمة على {m(2)} لحصلت على ضعف الإجابة الصحيحة!",
            diagram_en=svg_graph_cycle_chords(min(n_v, 8), full_kn=False),
        )

    # Medium (6): Interior intersections of chords among n circle points (no 3 chords concurrent) = C(n, 4)
    for n_pts in (6, 7, 8, 9, 10, 11):
        ans = math.comb(n_pts, 4)
        B.add_math(
            tp, "Medium", bp,
            f"{m(n_pts)} distinct points are marked on a circle in general position (no three chords meet at the same interior point), and every pair of points is joined by a chord. How many **interior** intersection points do these chords form inside the circle?",
            f"عُيّنت {m(n_pts)} نقاط متمايزة على محيط دائرة في وضع عام (لا تلتقي ثلاثة أوتار في نقطة داخلية واحدة)، ورُسمت الأوتار الواصلة بين كل نقطتين. كم نقطة تقاطع **داخلية** تنشأ داخل الدائرة؟",
            ans, [math.comb(n_pts, 2), math.comb(n_pts, 3), 2 * ans, ans - n_pts],
            f"Every {m(4)} chosen points on the circle form a convex quadrilateral whose diagonals cross at **exact one** interior point!",
            f"كل {m(4)} نقاط نختارها على الدائرة تكوّن رباعياً محدباً يتقاطع قطراه في **نقطة داخلية وحيدة**!",
            f"Use the golden bijection: interior chord crossings {m('\\longleftrightarrow')} 4-subsets of circle points!",
            [
                f"Any interior crossing is formed by two intersecting chords, which determine {m(4)} distinct endpoints on the circle.",
                f"Conversely, any {m(4)} points on the circle can be connected by intersecting chords in **exact one** way (the two diagonals of their cyclic quadrilateral).",
                f"Hence the number of interior intersections is {m(f'\\binom{{{n_pts}}}{{4}} = {ans}')}.",
            ],
            f"Base check: for {m('n = 4')} points on a circle, {m('\\binom{4}{4} = 1')} crossing!",
            f"ننشئ تقابلاً واحداً لواحد بين نقاط التقاطع الداخلية واختيار {m(4)} نقاط من محيط الدائرة!",
            [
                f"أي {m(4)} نقاط على الدائرة تحدد رباعياً دائرياً يتقاطع قطراه داخل الدائرة في نقطة واحدة فقط.",
                f"وبالعكس كل تقاطع داخلي ينتج عن وترين يحددان {m(4)} نقاط على المحيط.",
                f"إذن عدد نقاط التقاطع الداخلية يساوي {m(f'\\binom{{{n_pts}}}{{4}} = {ans}')}.",
            ],
            f"تحقق عند {m('n=4')}: {m('\\binom{4}{4} = 1')} نقطة تقاطع واحدة كما نرى بالرسم!",
            diagram_en=svg_graph_cycle_chords(min(n_pts, 8), full_kn=True),
        )

    # Hard (4): Tree leaf count from high-degree vertices (sum(deg) = 2V - 2) + Moser circle regions 1 + C(n,2) + C(n,4)!
    for d4, d3 in [(2, 3), (3, 4), (4, 5)]:
        # Tree has d4 vertices of deg 4, d3 vertices of deg 3, and L leaves (deg 1), no other vertices:
        # V = d4 + d3 + L; sum deg = 4*d4 + 3*d3 + L = 2*(d4 + d3 + L) - 2 -> L = 2*d4 + d3 + 2!
        ans = 2 * d4 + d3 + 2
        B.add_math(
            tp, "Hard", bp,
            f"A tree (a connected graph with no cycles) has exact {m(d4)} vertices of degree {m(4)}, exact {m(d3)} vertices of degree {m(3)}, and all remaining vertices are leaves of degree {m(1)}. How many **leaves** does the tree have?",
            f"شجرة (بيان متصل خالٍ من الدورات) تحتوي بالضبط على {m(d4)} رؤوس من الدرجة {m(4)}، و{m(d3)} رؤوس من الدرجة {m(3)}، وجميع الرؤوس الباقية أوراق من الدرجة {m(1)}. كم عدد **الأوراق** في هذه الشجرة؟",
            ans, [ans - 2, ans - 1, ans + 2, d4 + d3 + 2],
            f"Let {m('L')} be the number of leaves: a tree with {m(f'V = {d4} + {d3} + L')} vertices has {m('V - 1')} edges, so {m('\\sum \\deg = 2V - 2')}!",
            f"افرض عدد الأوراق {m('L')}: الشجرة ذات {m('V')} رأساً تملك {m('V - 1')} حافة، إذن مجموع الدرجات {m('2V - 2')}!",
            f"Combine {m('|E| = |V| - 1')} with the Handshaking Lemma {m('\\sum \\deg = 2|E| = 2|V| - 2')}!",
            [
                f"With {m('L')} leaves, total vertices {m(f'|V| = {d4 + d3} + L')} and total edges {m(f'|E| = {d4 + d3 - 1} + L')}.",
                f"Summing degrees gives {m(f'4({d4}) + 3({d3}) + 1(L) = 2|E| = 2({d4 + d3 - 1} + L)')}.",
                f"Simplifying {m(f'{4*d4 + 3*d3} + L = {2*(d4 + d3 - 1)} + 2L')} yields {m(f'L = {ans}')} leaves.",
            ],
            f"Formula shortcut check: {m('L = 2 + \\sum_{k \\ge 2} (k - 2) n_k = 2 + 2(' + str(d4) + ') + 1(' + str(d3) + ') = ' + str(ans))}!",
            f"نجمع خاصية الشجرة {m('|E| = |V| - 1')} مع مبرهنة المصافحات {m('\\sum \\deg = 2|V| - 2')}!",
            [
                f"بفرض عدد الأوراق {m('L')} يكون {m(f'|V| = {d4 + d3} + L')}.",
                f"مجموع الدرجات: {m(f'4({d4}) + 3({d3}) + L = 2({d4 + d3} + L) - 2')}.",
                f"بحل المعادلة الخطية في {m('L')} نجد {m(f'L = {ans}')} ورقة.",
            ],
            f"تحقق بالقانون السريع للأوراق: {m(f'2 + 2({d4}) + 1({d3}) = {ans}')}!",
        )

    # 4th Hard: Moser's circle regions for n = 6 -> 1 + C(6,2) + C(6,4) = 1 + 15 + 15 = 31 (classic 1,2,4,8,16,31 trap!)
    B.add_math(
        tp, "Hard", bp,
        f"Six points are placed on a circle in general position (no three chords concurrent) and all {m('\\binom{6}{2} = 15')} chords are drawn. Into how many **regions** do these chords divide the interior of the circle?",
        f"وُضعت {m(6)} نقاط على محيط دائرة في وضع عام (لا تلتقي ثلاثة أوتار في نقطة داخلية واحدة) ورُسمت جميع الأوتار الـ {m(15)} بينها. إلى كم **منطقة** تقسّم هذه الأوتار داخل الدائرة؟",
        31, [32, 30, 29, 28],
        f"Beware the famous {m('1, 2, 4, 8, 16, \\dots')} illusion! Use Euler's planar formula yielding {m('1 + \\binom{n}{2} + \\binom{n}{4}')}!",
        f"احذر خدعة النمط الظاهري {m('1, 2, 4, 8, 16')}! الصيغة الدقيقة من معادلة أويلر هي {m('1 + \\binom{n}{2} + \\binom{n}{4}')}!",
        f"Apply Moser's circle-region formula {m('R_n = 1 + \\binom{n}{2} + \\binom{n}{4}')} instead of guessing {m('2^{n-1}')}!",
        [
            f"Each of the {m('\\binom{6}{2} = 15')} chords enters the circle and adds {m(1)} region, plus {m(1)} additional region each time it crosses an earlier chord.",
            f"Total interior chord crossings equal {m('\\binom{6}{4} = 15')}.",
            f"Starting from {m(1)} undivided disk, total regions = {m('1 + \\binom{6}{2} + \\binom{6}{4} = 1 + 15 + 15 = 31')} (NOT {m(32)}!).",
        ],
        f"Classic Olympiad lesson: for {m('n = 1, 2, 3, 4, 5')} the formula gives {m('1, 2, 4, 8, 16')}, then {m('n = 6')} gives **{m(31)}**!",
        f"نطبّق صيغة موزر الشهيرة المستنتجة من صيغة أويلر للمناطق: {m('R_n = 1 + \\binom{n}{2} + \\binom{n}{4}')}!",
        [
            f"نبدأ بمنطقة واحدة، ويضيف كل وتر من الـ {m('\\binom{6}{2} = 15')} وتراً منطقة جديدة زائد منطقة إضافية عند كل تقاطع داخلي.",
            f"عدد التقاطعات الداخلية يساوي {m('\\binom{6}{4} = 15')}.",
            f"إجمالي المناطق = {m('1 + 15 + 15 = 31')} منطقة (وليس {m(32)}!).",
        ],
        f"تحقق: هذه أشهر مسألة تحذّر من التعميم البصري المتسرع في أولمبياد الرياضيات!",
        diagram_en=svg_graph_cycle_chords(6, full_kn=True),
    )

    # 29. nsmo_g10_committee_vandermonde_identities (5E, 6M, 4H) — SVG: svg_venn_2 / svg_digit_slots
    bp = "nsmo_g10_committee_vandermonde_identities"
    # Easy (5): Committee of size k with 1 designated chair from n candidates: n * C(n-1, k-1)
    easy_com = [
        (7, 3),   # 7 * C(6,2) = 105
        (8, 3),   # 8 * C(7,2) = 168
        (8, 4),   # 8 * C(7,3) = 280
        (9, 3),   # 9 * C(8,2) = 252
        (10, 4),  # 10 * C(9,3) = 840
    ]
    for n_c, k_c in easy_com:
        ans = n_c * math.comb(n_c - 1, k_c - 1)
        B.add_math(
            tp, "Easy", bp,
            f"From {m(n_c)} Olympiad finalists, a scientific committee of {m(k_c)} members is to be formed, with one of the {m(k_c)} committee members designated as **Chairperson**. In how many ways can this be done?",
            f"من بين {m(n_c)} طلاب متأهلين للأولمبياد، نريد تشكيل لجنة علمية مكوّنة من {m(k_c)} أعضاء مع تعيين أحد أعضاء اللجنة **رئيساً** لها. بكم طريقة يمكن القيام بذلك؟",
            ans, [math.comb(n_c, k_c), math.perm(n_c, k_c), (n_c - 1) * math.comb(n_c, k_c), ans // 2],
            f"Either pick the {m(k_c)}-member committee first in {m(f'\\binom{{{n_c}}}{{{k_c}}}')} ways and then pick {m(1)} chair in {m(k_c)} ways, OR pick the chair first in {m(n_c)} ways!",
            f"اختر الرئيس أولاً بـ {m(n_c)} طرق ثم اختر بقية الأعضاء الـ {m(k_c - 1)} من الـ {m(n_c - 1)} الباقين!",
            f"Use the committee-chairperson identity {m(f'{k_c}\\binom{{{n_c}}}{{{k_c}}} = {n_c}\\binom{{{n_c - 1}}}{{{k_c - 1}}}')}!",
            [
                f"Select the Chairperson first in {m(n_c)} ways.",
                f"Select the remaining {m(k_c - 1)} ordinary committee members from the remaining {m(n_c - 1)} finalists in {m(f'\\binom{{{n_c - 1}}}{{{k_c - 1}}} = {math.comb(n_c - 1, k_c - 1)}')} ways.",
                f"Multiply: {m(f'{n_c} \\times {math.comb(n_c - 1, k_c - 1)} = {ans}')}.",
            ],
            f"Double-counting check: {m(f'\\binom{{{n_c}}}{{{k_c}}} \\times {k_c} = {math.comb(n_c, k_c)} \\times {k_c} = {ans}')}!",
            f"نطبّق متطابقة اللجنة والرئيس {m(f'{n_c}\\binom{{{n_c - 1}}}{{{k_c - 1}}} = {k_c}\\binom{{{n_c}}}{{{k_c}}}')}!",
            [
                f"اختيار الرئيس يتم بـ {m(n_c)} طرق.",
                f"اختيار بقية الأعضاء الـ {m(k_c - 1)} من المرشحين الـ {m(n_c - 1)} الباقين يتم بـ {m(f'\\binom{{{n_c - 1}}}{{{k_c - 1}}} = {math.comb(n_c - 1, k_c - 1)}')} طريقة.",
                f"الناتج الكلي: {m(f'{n_c} \\times {math.comb(n_c - 1, k_c - 1)} = {ans}')}.",
            ],
            f"تحقق بالعدّ المزدوج: {m(f'\\binom{{{n_c}}}{{{k_c}}} \\times {k_c} = {ans}')}.",
            diagram_en=svg_digit_slots(["Chair"] + ["M"] * min(k_c - 1, 3), f"{n_c} candidates → {k_c} roles"),
        )

    # Medium (6): Hockey-Stick sum_{i=r}^{n} C(i, r) = C(n+1, r+1) (3 items) + Even-sized subsets 2^{n-1} (3 items)
    for r_h, n_h in [(2, 7), (3, 8), (2, 9)]:
        ans = math.comb(n_h + 1, r_h + 1)
        terms_tex = f"\\binom{{{r_h}}}{{{r_h}}} + \\binom{{{r_h + 1}}}{{{r_h}}} + \\binom{{{r_h + 2}}}{{{r_h}}} + \\cdots + \\binom{{{n_h}}}{{{r_h}}}"
        B.add_math(
            tp, "Medium", bp,
            f"Evaluate the binomial sum {m(terms_tex)}.",
            f"أوجد قيمة المجموع التوافقي {m(terms_tex)}.",
            ans, [math.comb(n_h, r_h + 1), math.comb(n_h + 1, r_h), ans - 1, ans + n_h],
            f"Replace {m(f'\\binom{{{r_h}}}{{{r_h}}} = \\binom{{{r_h + 1}}}{{{r_h + 1}}}')} and repeatedly apply Pascal's rule {m('\\binom{m}{k} + \\binom{m}{k+1} = \\binom{m+1}{k+1}')}!",
            f"استبدل {m(f'\\binom{{{r_h}}}{{{r_h}}} = \\binom{{{r_h + 1}}}{{{r_h + 1}}}')} وطبّق قاعدة باسكال تباعاً (متطابقة عصا الهوكي)!",
            f"Collapse the diagonal sum in one step via the **Hockey-Stick Identity** {m('\\sum_{i=r}^{n} \\binom{i}{r} = \\binom{n+1}{r+1}')}!",
            [
                f"Start with {m(f'\\binom{{{r_h}}}{{{r_h}}} = \\binom{{{r_h + 1}}}{{{r_h + 1}}}')}; adding {m(f'\\binom{{{r_h + 1}}}{{{r_h}}}')} gives {m(f'\\binom{{{r_h + 2}}}{{{r_h + 1}}}')}.",
                f"Cascading Pascal's identity down to {m(f'i = {n_h}')} collapses the entire sum to {m(f'\\binom{{{n_h + 1}}}{{{r_h + 1}}}')}.",
                f"Evaluating gives {m(f'\\binom{{{n_h + 1}}}{{{r_h + 1}}} = {ans}')}.",
            ],
            f"Direct term-by-term sum check: {m(' + '.join(str(math.comb(i, r_h)) for i in range(r_h, n_h + 1)) + f' = {ans}')}!",
            f"نطبّق متطابقة عصا الهوكي {m('\\sum_{i=r}^{n} \\binom{i}{r} = \\binom{n+1}{r+1}')}!",
            [
                f"بدمج الحدود متتالياً عبر متطابقة باسكال ينطوي المجموع كاملاً إلى حد توافقي واحد هو {m(f'\\binom{{{n_h + 1}}}{{{r_h + 1}}}')}.",
                f"نحسب القيمة: {m(f'\\binom{{{n_h + 1}}}{{{r_h + 1}}} = {ans}')}.",
            ],
            f"تحقق بالجمع المباشر للحدود: المجموع يساوي {m(ans)} بالضبط.",
        )

    for n_ev in (7, 8, 9):
        ans = 2 ** (n_ev - 1)
        B.add_math(
            tp, "Medium", bp,
            f"How many subsets of {m(f'\\{{1, 2, \\dots, {n_ev}\\}}')} have an **odd** number of elements?",
            f"كم مجموعة جزئية من المجموعة {m(f'\\{{1, 2, \\dots, {n_ev}\\}}')} تحتوي على عدد **فردي** من العناصر؟",
            ans, [2 ** n_ev, ans - 1, ans + 1, 2 ** (n_ev - 2)],
            f"Toggling element {m('1')} in or out flips every subset's size between even and odd—splitting all {m(f'2^{{{n_ev}}}')} subsets in half!",
            f"إدخال العنصر {m('1')} أو إخراجه يعكس زوجية حجم المجموعة، مما يقسم الـ {m(f'2^{{{n_ev}}}')} مجموعة جزئية بالتساوي تماماً!",
            f"Use the parity-toggling bijection (or expand {m('(1 - 1)^n = 0')}) to see exact half of all subsets are odd-sized!",
            [
                f"Total subsets of an {m(n_ev)}-element set equal {m(f'2^{{{n_ev}}} = {2 ** n_ev}')}.",
                f"Pairing each subset {m('S')} with {m('S \\triangle \\{1\\}')} pairs one even-sized subset with one odd-sized subset.",
                f"Hence exact half have odd size: {m(f'2^{{{n_ev} - 1}} = {ans}')}.",
            ],
            f"Binomial check: {m(' + '.join(f'\\binom{{{n_ev}}}{{{k}}}' for k in range(1, n_ev + 1, 2)) + f' = {ans}')}!",
            f"نصف المجموعات الجزئية بالضبط فردي الحجم ونصفها زوجي الحجم، أي {m(f'2^{{{n_ev}-1}}')}!",
            [
                f"عدد جميع المجموعات الجزئية هو {m(f'2^{{{n_ev}}} = {2 ** n_ev}')}.",
                f"من التوسيع {m(f'(1 - 1)^{{{n_ev}}} = 0')} يتساوى مجموع التوافيق الفردية مع الزوجية، فكل منهما يساوي {m(f'2^{{{n_ev - 1}}} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} + {ans} = {2 ** n_ev}')}.",
        )

    # Hard (4): Vandermonde Convolution sum_{k=0}^{r} C(a, k)*C(b, r-k) = C(a+b, r) & sum_{k=0}^{n} C(n,k)^2 = C(2n, n)
    vand_specs = [
        (4, 5, 4),  # C(9, 4) = 126
        (5, 5, 5),  # sum C(5,k)^2 = C(10, 5) = 252
        (5, 6, 4),  # C(11, 4) = 330
        (6, 6, 6),  # sum C(6,k)^2 = C(12, 6) = 924
    ]
    for a_v, b_v, r_v in vand_specs:
        ans = math.comb(a_v + b_v, r_v)
        if a_v == b_v == r_v:
            B.add_math(
                tp, "Hard", bp,
                f"Find the exact value of {m(f'\\binom{{{a_v}}}{{0}}^2 + \\binom{{{a_v}}}{{1}}^2 + \\binom{{{a_v}}}{{2}}^2 + \\cdots + \\binom{{{a_v}}}{{{a_v}}}^2')}.",
                f"أوجد القيمة الدقيقة للمجموع {m(f'\\binom{{{a_v}}}{{0}}^2 + \\binom{{{a_v}}}{{1}}^2 + \\binom{{{a_v}}}{{2}}^2 + \\cdots + \\binom{{{a_v}}}{{{a_v}}}^2')}.",
                ans, [2 ** (2 * a_v), math.comb(2 * a_v - 1, a_v), ans // 2, ans - a_v],
                f"Rewrite {m(f'\\binom{{{a_v}}}{{k}}^2 = \\binom{{{a_v}}}{{k}}\\binom{{{a_v}}}{{{a_v} - k}}')}: choosing {m('k')} boys from {m(a_v)} and {m(f'{a_v}-k')} girls from {m(a_v)} chooses {m(a_v)} people from {m(2 * a_v)}!",
                f"اكتب {m(f'\\binom{{{a_v}}}{{k}}^2 = \\binom{{{a_v}}}{{k}}\\binom{{{a_v}}}{{{a_v} - k}}')} وطبّق متطابقة فاندرموند لاختيار {m(a_v)} عناصر من {m(2 * a_v)}!",
                f"Apply Vandermonde's square-sum identity {m(f'\\sum_{{k=0}}^{{{a_v}}} \\binom{{{a_v}}}{{k}}^2 = \\binom{{2 \\cdot {a_v}}}{{{a_v}}}')}!",
                [
                    f"Use symmetry {m(f'\\binom{{{a_v}}}{{k}} = \\binom{{{a_v}}}{{{a_v} - k}}')} so the sum becomes {m(f'\\sum_{{k=0}}^{{{a_v}}} \\binom{{{a_v}}}{{k}}\\binom{{{a_v}}}{{{a_v} - k}}')}.",
                    f"Combinatorially, this counts all ways to choose {m(a_v)} people from a pool of {m(a_v)} seniors and {m(a_v)} juniors: {m(f'\\binom{{{2 * a_v}}}{{{a_v}}} = {ans}')}.",
                ],
                f"Direct check: {m(' + '.join(str(math.comb(a_v, k)**2) for k in range(a_v + 1)) + f' = {ans}')}!",
                f"باستخدام التماثل ومتطابقة فاندرموند ينطوي مجموع مربعات سطر باسكال إلى {m(f'\\binom{{{2 * a_v}}}{{{a_v}}}')}!",
                [
                    f"نستبدل {m(f'\\binom{{{a_v}}}{{k}}^2')} بـ {m(f'\\binom{{{a_v}}}{{k}}\\binom{{{a_v}}}{{{a_v} - k}}')}.",
                    f"يمثل المجموع اختيار {m(a_v)} عناصر من مجموعتين حجم كل منهما {m(a_v)}، أي {m(f'\\binom{{{2 * a_v}}}{{{a_v}}} = {ans}')}.",
                ],
                f"تحقق بالجمع المباشر للمربعات: الناتج {m(ans)} بالضبط!",
                diagram_en=svg_venn_2(f"Group A ({a_v})", f"Group B ({a_v})", "k", "+", f"{a_v}−k", f"Choose {a_v}"),
            )
        else:
            sum_tex = f"\\sum_{{k=0}}^{{{r_v}}} \\binom{{{a_v}}}{{k}}\\binom{{{b_v}}}{{{r_v} - k}}"
            B.add_math(
                tp, "Hard", bp,
                f"Evaluate the Vandermonde convolution sum {m(sum_tex)}.",
                f"احسب قيمة مجموع فاندرموند التوافقي {m(sum_tex)}.",
                ans, [math.comb(a_v + b_v, r_v - 1), math.comb(a_v, 2) * math.comb(b_v, 2), ans - b_v, ans + a_v],
                f"Choosing {m('k')} items from {m(a_v)} red balls and {m(f'{r_v} - k')} items from {m(b_v)} blue balls over all {m('k')} chooses {m(r_v)} balls from {m(a_v + b_v)}!",
                f"اختيار {m('k')} من {m(a_v)} عناصر حمراء و{m(f'{r_v} - k')} من {m(b_v)} عناصر زرقاء يكافئ اختيار {m(r_v)} عناصر من إجمالي {m(a_v + b_v)}!",
                f"Recognize Vandermonde's Identity {m('\\sum_{k=0}^{r} \\binom{a}{k}\\binom{b}{r-k} = \\binom{a+b}{r}')}!",
                [
                    f"Partition a pool of {m(f'{a_v} + {b_v} = {a_v + b_v}')} distinct objects into Group A ({m(a_v)}) and Group B ({m(b_v)}).",
                    f"Choosing {m(r_v)} objects in total splits uniquely by how many ({m('k')}) come from Group A and how many ({m(f'{r_v}-k')}) come from Group B.",
                    f"Thus the sum equals {m(f'\\binom{{{a_v + b_v}}}{{{r_v}}} = {ans}')}.",
                ],
                f"Term-by-term verification: {m(' + '.join(str(math.comb(a_v, k)*math.comb(b_v, r_v - k)) for k in range(r_v + 1)) + f' = {ans}')}!",
                f"نطبّق متطابقة فاندرموند التوافقية {m('\\sum_{k=0}^{r} \\binom{a}{k}\\binom{b}{r-k} = \\binom{a+b}{r}')}!",
                [
                    f"اختيار {m(r_v)} عناصر من اتحاد مجموعتين حجمهما {m(a_v)} و{m(b_v)} يعطي مباشرةً {m(f'\\binom{{{a_v + b_v}}}{{{r_v}}}')}.",
                    f"بحساب التوافيق: {m(f'\\binom{{{a_v + b_v}}}{{{r_v}}} = {ans}')}.",
                ],
                f"تحقق بجمع الحدود فردياً: الناتج {m(ans)} تماماً.",
                diagram_en=svg_venn_2(f"A ({a_v})", f"B ({b_v})", "k", "+", f"{r_v}−k", f"Total {r_v}"),
            )

    # 30. nsmo_g10_bayes_geometric_probability (5E, 6M, 4H) — TOPIC MUST BE "Data & Probability"!
    tp_prob = "Data & Probability"
    bp = "nsmo_g10_bayes_geometric_probability"

    # Easy (5): Law of Total Probability with two boxes / urns + geometric area-ratio probability in square/diamond
    easy_urns = [
        (3, 1, 1, 3),  # Box A: 3R,1B (3/4), Box B: 1R,3B (1/4) -> pick random box, P(R) = 1/2? Wait: use asymmetric!
    ]
    easy_urns = [
        (3, 1, 2, 3),  # P(R) = 1/2*(3/4 + 2/5) = 1/2*(23/20) = 23/40
        (4, 1, 1, 2),  # P(R) = 1/2*(4/5 + 1/3) = 1/2*(17/15) = 17/30
        (2, 1, 3, 5),  # P(R) = 1/2*(2/3 + 3/8) = 1/2*(25/24) = 25/48
        (5, 1, 1, 3),  # P(R) = 1/2*(5/6 + 1/4) = 1/2*(13/12) = 13/24
        (3, 2, 1, 5),  # P(R) = 1/2*(3/5 + 1/6) = 1/2*(23/30) = 23/60
    ]
    for r1, b1, r2, b2 in easy_urns:
        p1 = Fraction(r1, r1 + b1)
        p2 = Fraction(r2, r2 + b2)
        ans = Fraction(1, 2) * (p1 + p2)
        B.add_math(
            tp_prob, "Easy", bp,
            f"Jar A contains {m(r1)} red and {m(b1)} blue marbles, while Jar B contains {m(r2)} red and {m(b2)} blue marbles. A fair coin is tossed to pick one jar at random, and then one marble is drawn at random from that jar. What is the probability of drawing a **red** marble?",
            f"يحتوي الوعاء (أ) على {m(r1)} كرات حمراء و{m(b1)} زرقاء، ويحتوي الوعاء (ب) على {m(r2)} كرات حمراء و{m(b2)} زرقاء. رُميت قطعة نقد عادلة لاختيار أحد الوعاءين عشوائياً ثم سُحبت منه كرة واحدة عشوائياً. ما احتمال أن تكون الكرة المسحوبة **حمراء**؟",
            ans, [Fraction(r1 + r2, r1 + b1 + r2 + b2), p1 * p2, Fraction(1, 2), ans - Fraction(1, ans.denominator)],
            f"Do NOT pool all marbles into one giant jar! Average the two conditional probabilities {m(f'\\frac{{1}}{{2}}P(R\\mid A) + \\frac{{1}}{{2}}P(R\\mid B)')}!",
            f"لا تجمع الكرات كلها في وعاء واحد! احسب متوسط الاحتمالين الشرطيين {m(f'\\frac{{1}}{{2}}P(R\\mid A) + \\frac{{1}}{{2}}P(R\\mid B)')}!",
            f"Apply the Law of Total Probability across the two equally likely jars!",
            [
                f"From Jar A, {m(f'P(R \\mid A) = \\frac{{{r1}}}{{{r1 + b1}}}')}; from Jar B, {m(f'P(R \\mid B) = \\frac{{{r2}}}{{{r2 + b2}}}')}.",
                f"Since each jar is chosen with probability {m('\\frac{1}{2}')}, {m(f'P(R) = \\frac{{1}}{{2}}\\left(\\frac{{{r1}}}{{{r1 + b1}}} + \\frac{{{r2}}}{{{r2 + b2}}}\\right) = {ans}')}.",
            ],
            f"Trap check: pooling marbles blindly would give {m(f'\\frac{{{r1+r2}}}{{{r1+b1+r2+b2}}} = {Fraction(r1+r2, r1+b1+r2+b2)} \\neq {ans}')}!",
            f"نطبّق قانون الاحتمال الكلي بضرب احتمال كل وعاء ({m('1/2')}) في احتمال سحب كرة حمراء منه!",
            [
                f"احتمال الحمراء من (أ) هو {m(f'\\frac{{{r1}}}{{{r1 + b1}}}')} ومن (ب) هو {m(f'\\frac{{{r2}}}{{{r2 + b2}}}')}.",
                f"بجمع الحالتين: {m(f'P(R) = \\frac{{1}}{{2}}\\left(\\frac{{{r1}}}{{{r1 + b1}}} + \\frac{{{r2}}}{{{r2 + b2}}}\\right) = {ans}')}.",
            ],
            f"انتبه للفخ: دمج الكرات مباشرة يعطي {m(f'{Fraction(r1+r2, r1+b1+r2+b2)}')} وهو خطأ لأن حجوم الأوعية مختلفة!",
            diagram_en=svg_two_jars(f"A: {r1}R,{b1}B", float(p1), f"B: {r2}R,{b2}B", float(p2), "1/2 each"),
        )

    # Medium (6): Bayes' Theorem posterior P(Jar A | Red) (4 items) + Geometric Probability on coordinate square (2 items)
    bayes_specs = [
        (3, 1, 1, 3),  # P(A|R) = (3/4) / (3/4 + 1/4) = 3/4
        (4, 1, 2, 3),  # P(A|R) = (4/5) / (4/5 + 2/5) = 2/3
        (3, 2, 1, 4),  # P(A|R) = (3/5) / (3/5 + 1/5) = 3/4? Same ans ok (different stem!), let's make distinct: (2, 1, 1, 5) -> (2/3)/(2/3+1/6)=4/5!
        (5, 1, 1, 2),  # P(A|R) = (5/6) / (5/6 + 1/3) = (5/6)/(7/6) = 5/7
    ]
    bayes_specs[2] = (2, 1, 1, 5)
    for r1, b1, r2, b2 in bayes_specs:
        p1 = Fraction(r1, r1 + b1)
        p2 = Fraction(r2, r2 + b2)
        ans = p1 / (p1 + p2)
        B.add_math(
            tp_prob, "Medium", bp,
            f"Box A holds {m(r1)} gold coins and {m(b1)} silver coins; Box B holds {m(r2)} gold coins and {m(b2)} silver coins. One box is chosen uniformly at random and one coin drawn at random turns out to be **gold**. Given this, what is the conditional probability that the chosen box was **Box A**?",
            f"يحتوي الصندوق (أ) على {m(r1)} عملات ذهبية و{m(b1)} فضية، ويحتوي الصندوق (ب) على {m(r2)} عملات ذهبية و{m(b2)} فضية. اختير أحد الصندوقين عشوائياً بالتساوي وسُحبت منه عملة فتبين أنها **ذهبية**. ما الاحتمال الشرطي أن تكون مسحوبة من **الصندوق (أ)**؟",
            ans, [p1, Fraction(r1, r1 + r2), Fraction(1, 2) * (p1 + p2), 1 - ans],
            f"Use Bayes' Rule: divide Box A's gold branch {m(f'\\frac{{1}}{{2}} \\cdot {p1}')} by the total gold probability {m(f'\\frac{{1}}{{2}}({p1} + {p2})')}!",
            f"طبّق مبرهنة بايز: اقسم مسار الذهب من (أ) على مجموع احتمالي الذهب من الصندوقين!",
            f"Apply Bayes' Theorem: with equal priors, {m('P(A \\mid G) = \\frac{P(G \\mid A)}{P(G \\mid A) + P(G \\mid B)}')}!",
            [
                f"Conditional gold probabilities are {m(f'P(G \\mid A) = {p1}')} and {m(f'P(G \\mid B) = {p2}')}.",
                f"Because both boxes had equal prior probability {m('1/2')}, the {m('1/2')} factors cancel in Bayes' fraction.",
                f"Thus {m(f'P(A \\mid G) = \\frac{{{p1}}}{{{p1} + {p2}}} = {ans}')}.",
            ],
            f"Posterior check: {m(f'P(A \\mid G) + P(B \\mid G) = {ans} + {1 - ans} = 1')}!",
            f"بتطبيق مبرهنة بايز مع تساوي الاحتمال القبلي للصندوقين يختصر المعامل {m('1/2')} مباشرة!",
            [
                f"لدينا {m(f'P(G \\mid A) = {p1}')} و{m(f'P(G \\mid B) = {p2}')}.",
                f"إذن {m(f'P(A \\mid G) = \\frac{{{p1}}}{{{p1} + {p2}}} = {ans}')}.",
            ],
            f"تحقق: مجموع الاحتمالين البعديين للصندوقين يساوي {m('1')} تماماً.",
            diagram_en=svg_two_jars(f"A: {r1}G,{b1}S", float(p1), f"B: {r2}G,{b2}S", float(p2), "Given Gold → P(A)?"),
        )

    for S_sq, cut_c in [(4, 2), (6, 2)]:
        # Point (x, y) chosen uniformly in [0, S] x [0, S]. Probability x + y <= cut_c -> triangle area (1/2 * c^2) / S^2!
        ans = Fraction(cut_c * cut_c, 2 * S_sq * S_sq)
        B.add_math(
            tp_prob, "Medium", bp,
            f"Two real numbers {m('x')} and {m('y')} are chosen independently and uniformly at random from the interval {m(f'[0, {S_sq}]')}. What is the probability that {m(f'x + y \\le {cut_c}')}?",
            f"اختير عددان حقيقيان {m('x')} و{m('y')} عشوائياً وبانتظام وباستقلال من الفترة {m(f'[0, {S_sq}]')}. ما احتمال أن يتحقق الشرط {m(f'x + y \\le {cut_c}')}؟",
            ans, [Fraction(cut_c, S_sq), Fraction(cut_c * cut_c, S_sq * S_sq), 2 * ans, Fraction(cut_c, 2 * S_sq)],
            f"Plot the sample space as the {m(f'{S_sq} \\times {S_sq}')} square in the first quadrant—{m(f'x + y \\le {cut_c}')} cuts off a right corner triangle!",
            f"مثّل فضاء العينة بمربع ضلعه {m(S_sq)} في الربع الأول؛ المتباينة {m(f'x + y \\le {cut_c}')} تقتطع مثلثاً قائماً عند نقطة الأصل!",
            f"Convert continuous uniform probability into a **2D area ratio** inside the {m(f'{S_sq} \\times {S_sq}')} square!",
            [
                f"The sample space {m(f'[0, {S_sq}] \\times [0, {S_sq}]')} is a square of area {m(f'{S_sq}^2 = {S_sq * S_sq}')}.",
                f"Since {m(f'{cut_c} \\le {S_sq}')}, the region {m(f'x \\ge 0,\\; y \\ge 0,\\; x + y \\le {cut_c}')} is a right isosceles triangle with legs {m(cut_c)}, having area {m(f'\\frac{{1}}{{2}} \\times {cut_c}^2 = {Fraction(cut_c*cut_c, 2)}')}.",
                f"Dividing favorable area by total area gives {m(f'\\frac{{{Fraction(cut_c*cut_c, 2)}}}{{{S_sq * S_sq}}} = {ans}')}.",
            ],
            f"Boundary sanity check: if the bound were {m(S_sq)}, the corner triangle would cover exact {m('1/2')} of the square!",
            f"نحوّل الاحتمال المتصل المنتظم إلى **نسبة مساحات** داخل المربع {m(f'{S_sq} \\times {S_sq}')}!",
            [
                f"مساحة مربع فضاء العينة تساوي {m(f'{S_sq}^2 = {S_sq * S_sq}')}.",
                f"المنطقة {m(f'x + y \\le {cut_c}')} في الربع الأول مثلث قائم متطابق الضلعين مساحته {m(f'\\frac{{1}}{{2}}({cut_c})^2 = {Fraction(cut_c*cut_c, 2)}')}.",
                f"الاحتمال يساوي نسبة المساحتين: {m(f'{ans}')}.",
            ],
            f"تحقق: المساحة موجبة وأصغر من نصف مساحة المربع.",
            diagram_en=svg_coord_diamond(f"x+y≤{cut_c}"),
        )

    # Hard (4): Classic 2D Meeting Problem |x - y| <= w on [0, T]^2 -> 1 - ((T - w)/T)^2 (3 items) + Sequential Urn Transfer Bayes (1 item)
    for T_win, w_wait in [(60, 15), (60, 20), (40, 10)]:
        # Wait: (60,15) and (40,10) both have w/T = 1/4 -> same answer 7/16 (fine! stems differ), let's make 3rd (60, 12) -> w/T = 1/5 -> 1 - 16/25 = 9/25!
        pass
    meet_specs = [(60, 15), (60, 20), (60, 12)]
    for T_win, w_wait in meet_specs:
        rem_f = Fraction(T_win - w_wait, T_win)
        ans = 1 - rem_f * rem_f
        B.add_math(
            tp_prob, "Hard", bp,
            f"Two friends independently arrive at a Riyadh café at uniformly random times between **4:00 PM** and **5:00 PM** ({m(T_win)} minutes). Each person waits exact {m(w_wait)} minutes (or until 5:00 PM if earlier) and then leaves. What is the probability that they meet?",
            f"يصل صديقان باستقلال وبانتظام عشوائي إلى مقهى في الرياض بين الساعة **4:00 مساءً** و**5:00 مساءً** (خلال {m(T_win)} دقيقة). ينتظر كلٌّ منهما {m(w_wait)} دقيقة بالضبط (أو حتى 5:00 مساءً) ثم يغادر. ما احتمال أن يلتقيا؟",
            ans, [Fraction(w_wait, T_win), Fraction(2 * w_wait, T_win), rem_f * rem_f, Fraction(w_wait * w_wait, T_win * T_win)],
            f"Graph arrival times {m('(x, y) \\in [0, ' + str(T_win) + ']^2')}: they meet iff {m(f'|x - y| \\le {w_wait}')}, whose complement is **two** corner triangles of leg {m(T_win - w_wait)}!",
            f"مثّل وقتي الوصول {m('(x, y)')} في مربع ضلعه {m(T_win)}؛ يلتقيان إذا وفقط إذا {m(f'|x - y| \\le {w_wait}')}، والمتممة مثلثان قائمان ضلع كل منهما {m(T_win - w_wait)}!",
            f"Compute {m('1 - P(\\text{miss})')} by combining the two unshaded corner triangles into one {m(f'({T_win} - {w_wait})^2')} square!",
            [
                f"Model arrival minutes after 4:00 PM as a uniform point {m(f'(x, y) \\in [0, {T_win}]^2')} of total area {m(T_win * T_win)}.",
                f"They miss each other when {m(f'x - y > {w_wait}')} or {m(f'y - x > {w_wait}')}, which form two congruent right triangles of leg {m(f'{T_win} - {w_wait} = {T_win - w_wait}')}.",
                f"Together the two miss-triangles form a square of area {m(f'{T_win - w_wait}^2')}, so {m(f'P(\\text{{meet}}) = 1 - \\left(\\frac{{{T_win - w_wait}}}{{{T_win}}}\\right)^2 = {ans}')}.",
            ],
            f"Extreme check: if wait time were {m(0)} we get {m(0)}; if wait time were {m(T_win)} we get {m(1)}!",
            f"نحسب متممة اللقاء داخل مربع الزمن {m(f'{T_win} \\times {T_win}')} عبر دمج مثلثي عدم اللقاء!",
            [
                f"يتحقق اللقاء عندما {m(f'|x - y| \\le {w_wait}')} داخل المربع {m(f'[0, {T_win}]^2')}.",
                f"منطقة عدم اللقاء تتكون من مثلثين قائمين طول ضلع كل منهما {m(T_win - w_wait)}، ومجموع مساحتيهما يساوي مربعاً مساحته {m(f'({T_win - w_wait})^2')}.",
                f"إذن احتمال اللقاء يساوي {m(f'1 - \\left(\\frac{{{T_win - w_wait}}}{{{T_win}}}\\right)^2 = {ans}')}.",
            ],
            f"تحقق: صيغة الشريط القطري تعطي دائماً {m('1 - (1 - w/T)^2')}!",
            diagram_en=svg_square_circle_shaded(f"{T_win} min", mode="inscribed_outside"),
        )

    # 4th Hard: Transfer 1 ball from Urn A (3R, 1B) to Urn B (1R, 2B), then draw Red from B -> find P(transferred was Red | drew Red from B)!
    # P(trans R) = 3/4 -> B has (2R, 2B) -> P(R_B | trans R) = 2/4 = 1/2 -> joint = 3/8
    # P(trans B) = 1/4 -> B has (1R, 3B) -> P(R_B | trans B) = 1/4 -> joint = 1/16
    # Total P(R_B) = 6/16 + 1/16 = 7/16 -> Posterior P(trans R | R_B) = (6/16) / (7/16) = 6/7!
    B.add_math(
        tp_prob, "Hard", bp,
        f"Urn A contains {m(3)} red balls and {m(1)} blue ball; Urn B contains {m(1)} red ball and {m(2)} blue balls. One ball is transferred unseen from Urn A into Urn B, and then one ball is drawn at random from Urn B and found to be **red**. What is the conditional probability that the transferred ball was **red**?",
        f"يحتوي الصندوق (أ) على {m(3)} كرات حمراء وكرة واحدة زرقاء، ويحتوي الصندوق (ب) على كرة واحدة حمراء وكرتين زرقاوين. نُقلت كرة واحدة عشوائياً دون النظر إليها من (أ) إلى (ب)، ثم سُحبت كرة عشوائياً من (ب) فتبين أنها **حمراء**. ما الاحتمال الشرطي أن تكون الكرة المنقولة **حمراء**؟",
        Fraction(6, 7), [Fraction(3, 4), Fraction(7, 16), Fraction(2, 3), Fraction(5, 7)],
        f"Split into two branches (transferred Red with prob {m('3/4')} vs transferred Blue with prob {m('1/4')}), update Urn B's contents in each branch, and apply Bayes' Theorem!",
        f"فرّع المسألة إلى حالتين (نقل حمراء باحتمال {m('3/4')} أو زرقاء باحتمال {m('1/4')})، حدّث محتوى (ب) في كل حالة، ثم طبّق بايز!",
        f"Tree-branch on the transferred ball and apply Bayes' rule to the updated Urn B!",
        [
            f"Branch 1 (transfer Red, prob {m('3/4')}): Urn B becomes {m('(2\\text{R}, 2\\text{B})')}, so {m('P(R_B \\mid T_R) = \\frac{2}{4} = \\frac{1}{2}')}; joint probability = {m('\\frac{3}{4} \\times \\frac{1}{2} = \\frac{6}{16}')}.",
            f"Branch 2 (transfer Blue, prob {m('1/4')}): Urn B becomes {m('(1\\text{R}, 3\\text{B})')}, so {m('P(R_B \\mid T_B) = \\frac{1}{4}')}; joint probability = {m('\\frac{1}{4} \\times \\frac{1}{4} = \\frac{1}{16}')}.",
            f"By Bayes' Theorem, {m('P(T_R \\mid R_B) = \\frac{6/16}{6/16 + 1/16} = \\frac{6}{7}')}.",
        ],
        f"Notice observing Red from B boosted the probability of a Red transfer from prior {m('3/4 = 0.75')} up to posterior {m('6/7 \\approx 0.857')}!",
        f"نرسم شجرة الاحتمال لحالتي النقل ثم نطبّق مبرهنة بايز!",
        [
            f"حالة نقل حمراء ({m('3/4')}): يصبح في (ب) كرتان حمراوان وزرقاوان، فاحتمال سحب حمراء هو {m('2/4')} والاحتمال المشترك {m('6/16')}.",
            f"حالة نقل زرقاء ({m('1/4')}): يصبح في (ب) كرة حمراء و{m(3)} زرقاء، فاحتمال سحب حمراء هو {m('1/4')} والاحتمال المشترك {m('1/16')}.",
            f"بمبرهنة بايز: الاحتمال البعدي يساوي {m('\\frac{6/16}{6/16 + 1/16} = \\frac{6}{7}')}.",
        ],
        f"تحقق: المقام الكلي لسحب كرة حمراء من (ب) هو {m('7/16')} والبسط {m('6/16')}، فالنسبة {m('6/7')}.",
        diagram_en=svg_two_jars("A: 3R, 1B", 0.75, "B: 1R, 2B", 0.45, "Transfer 1 → Draw R"),
    )


def build_p3_bank() -> list[dict]:
    B = BankBuilder()
    _add_unit_3_1(B)
    _add_unit_3_2(B)
    _add_unit_3_3(B)
    _add_unit_3_4(B)
    _add_unit_3_5(B)
    _add_unit_3_6(B)
    assert len(B.items) == 450, f"Expected 450 Phase 3 items, got {len(B.items)}"
    other_stems = load_other_track_stems()
    seen = set()
    for q in B.items:
        st = norm_text(q["content"]["en"]["question"])
        assert st not in other_stems, f"Collision with other track in {q['id']}"
        assert st not in seen, f"Duplicate P3 stem in {q['id']}: {st[:80]}"
        seen.add(st)
    return B.items
