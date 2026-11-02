"""Track 3 (Grades 10-11) — Bank Expansion (300 verified KMC Senior problems across 18 blueprints)."""
import itertools
import math
from fractions import Fraction

from kmc_common import (
    explain_ar,
    explain_en,
    fmt_val,
    m,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams_extra import (
    svg_angle_bisector_tri,
    svg_binary_bulbs,
    svg_coord_diamond,
    svg_factor_tree,
    svg_parabola_roots,
    svg_power_of_point,
    svg_right_tri_incircle,
    svg_round_table,
)

LEVEL = "Track 3: Grades 10-11"


def _vp_factorial(n: int, p: int) -> int:
    """Legendre's formula for prime p in n!, cross-checked against math.factorial(n)."""
    total = 0
    pw = p
    while pw <= n:
        total += n // pw
        pw *= p
    fact = math.factorial(n)
    assert fact % (p ** total) == 0 and fact % (p ** (total + 1)) != 0
    return total


def _prime_factors(n: int) -> dict[int, int]:
    """Return prime factorization {p: exp} of integer n >= 2."""
    out: dict[int, int] = {}
    d = 2
    rem = n
    while d * d <= rem:
        while rem % d == 0:
            out[d] = out.get(d, 0) + 1
            rem //= d
        d += 1
    if rem > 1:
        out[rem] = out.get(rem, 0) + 1
    prod = 1
    for p, e in out.items():
        prod *= p ** e
    assert prod == n
    return out


def _base_b_digits(n: int, b: int) -> list[int]:
    """Convert non-negative integer n to base-b digits (most significant first)."""
    assert b >= 2 and n >= 0
    if n == 0:
        return [0]
    digs: list[int] = []
    rem = n
    while rem > 0:
        digs.append(rem % b)
        rem //= b
    digs.reverse()
    val = 0
    for d in digs:
        assert 0 <= d < b
        val = val * b + d
    assert val == n
    return digs


def _gen_lesson_3_1(push) -> None:
    topic = "Number Theory"

    # ------------------------------------------------------------------
    # 1. kmc_g1011_legendre_prime_factorial (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    leg_cases = [
        # (n, base, diff)
        (15, 2, "Easy"),
        (20, 3, "Easy"),
        (28, 5, "Easy"),
        (30, 3, "Easy"),
        (50, 7, "Easy"),
        (36, 2, "Medium"),
        (65, 5, "Medium"),
        (85, 3, "Medium"),
        (130, 5, "Medium"),
        (25, 6, "Medium"),
        (40, 15, "Medium"),
        (55, 10, "Medium"),
        (30, 12, "Medium"),
        (42, 12, "Hard"),
        (50, 18, "Hard"),
        (60, 24, "Hard"),
        (90, 45, "Hard"),
    ]
    for v_i, (n, base, diff) in enumerate(leg_cases):
        pf = _prime_factors(base)
        fact_n = math.factorial(n)
        if len(pf) == 1 and next(iter(pf.values())) == 1:
            p = base
            ans = _vp_factorial(n, p)
            terms = []
            quotients = []
            pw = p
            while pw <= n:
                terms.append(f"\\lfloor {n}/{pw} \\rfloor")
                quotients.append(str(n // pw))
                pw *= p
            sum_lhs = " + ".join(terms)
            sum_rhs = " + ".join(quotients)
            distractors = [n // p, ans - 1, ans + 1, ans + 2, max(1, ans - 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_leg_{v_i}")
            q_en = (
                f"Let {m(f'{n}! = 1 \\times 2 \\times 3 \\times \\dots \\times {n}')}. "
                f"What is the **greatest integer** {m('k')} such that {m(f'{p}^k')} divides {m(f'{n}!')}?"
            )
            q_ar = (
                f"ليكن {m(f'{n}! = 1 \\times 2 \\times 3 \\times \\dots \\times {n}')}. "
                f"ما **أكبر عدد صحيح** {m('k')} بحيث يقسم {m(f'{p}^k')} العدد {m(f'{n}!')} دون باقٍ؟"
            )
            h_en = (
                f"Count multiples of {p} up to {n}, then add extra factors from multiples of {p*p}"
                + (f", {p**3}, ..." if p ** 3 <= n else "!")
            )
            h_ar = (
                f"احسب عدد مضاعفات {p} حتى {n}، ثم أضف العوامل الإضافية القادمة من مضاعفات {p*p}"
                + (f" و{p**3} وهكذا!" if p ** 3 <= n else "!")
            )
            s_en = explain_en(
                f"By Legendre's formula, the exponent of prime \\( {p} \\) in \\( {n}! \\) sums \\( \\lfloor {n}/{p}^j \\rfloor \\) across powers \\( {p}^j \\le {n} \\).",
                [
                    f"Every multiple of {m(p)} contributes one factor of {m(p)}, every multiple of {m(p*p)} contributes a second factor, and so on.",
                    f"Set up the floor sum: {m(f'v_{{{p}}}({n}!) = {sum_lhs}')}.",
                    f"Evaluate each term and add: {m(f'{sum_rhs} = {ans}')}.",
                ],
                f"Common trap avoided: \\( \\lfloor {n}/{p} \\rfloor = {n // p} \\) misses the extra copies of \\( {p} \\) hidden inside \\( {p*p} \\) and higher powers!",
            )
            s_ar = explain_ar(
                f"بحسب قاعدة ليجاندر، أس العامل الأولي \\( {p} \\) في \\( {n}! \\) يساوي مجموع \\( \\lfloor {n}/{p}^j \\rfloor \\) لكل قوة \\( {p}^j \\le {n} \\).",
                [
                    f"كل مضاعف للعدد {m(p)} يمنح عاملاً واحداً، وكل مضاعف للعدد {m(p*p)} يمنح عاملاً إضافياً ثانياً، وهكذا.",
                    f"نكتب المجموع: {m(f'v_{{{p}}}({n}!) = {sum_lhs}')}.",
                    f"نحسب كل حد ونجمع: {m(f'{sum_rhs} = {ans}')}.",
                ],
                f"تجنّب الفخ الشائع: الاكتفاء بـ \\( \\lfloor {n}/{p} \\rfloor = {n // p} \\) يُهمل العوامل الإضافية داخل مضاعفات \\( {p*p} \\)!",
            )
        else:
            # Composite base = prod p_i^{e_i}
            ans = min(_vp_factorial(n, p) // e for p, e in pf.items())
            assert fact_n % (base ** ans) == 0 and fact_n % (base ** (ans + 1)) != 0
            pf_tex = " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(pf.items()))
            p_details_en = []
            p_details_ar = []
            cand_vals = []
            for p, e in sorted(pf.items()):
                vp = _vp_factorial(n, p)
                q_str = " + ".join(str(n // (p ** j)) for j in range(1, 10) if p ** j <= n)
                cand_vals.append(vp // e)
                if e == 1:
                    p_details_en.append(f"For prime {m(p)}: {m(f'v_{{{p}}}({n}!) = {q_str} = {vp}')} copies.")
                    p_details_ar.append(f"للعامل الأولي {m(p)}: {m(f'v_{{{p}}}({n}!) = {q_str} = {vp}')} مرة.")
                else:
                    p_details_en.append(
                        f"For prime {m(p)}: {m(f'v_{{{p}}}({n}!) = {q_str} = {vp}')}, which forms {m(f'\\lfloor {vp}/{e} \\rfloor = {vp // e}')} groups of {m(f'{p}^{{{e}}}')}."
                    )
                    p_details_ar.append(
                        f"للعامل الأولي {m(p)}: {m(f'v_{{{p}}}({n}!) = {q_str} = {vp}')}، وتكفي لتكوين {m(f'\\lfloor {vp}/{e} \\rfloor = {vp // e}')} مجموعة من {m(f'{p}^{{{e}}}')}."
                    )
            distractors = [max(cand_vals), ans + 1, max(1, ans - 1), sum( _vp_factorial(n, p) for p in pf ), ans + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_leg_{v_i}")
            q_en = (
                f"What is the **largest positive integer** {m('k')} such that the factorial {m(f'{n}!')} is divisible by {m(f'{base}^k')}?"
            )
            q_ar = (
                f"ما **أكبر عدد صحيح موجب** {m('k')} يجعل المضروب {m(f'{n}!')} قابلاً للقسمة على {m(f'{base}^k')}؟"
            )
            h_en = f"Factor the base first ({base} = {pf_tex.replace(' \\times ', '×').replace('{', '').replace('}', '')}) and check how many complete sets of prime factors {n}! can supply!"
            h_ar = f"حلّل الأساس إلى عوامله الأولية أولاً ({m(f'{base} = {pf_tex}')}) ثم احسب كم مجموعة كاملة من هذه العوامل تتوفر في {m(f'{n}!')}!"
            min_tex = ", ".join(str(c) for c in cand_vals)
            s_en = explain_en(
                f"Legendre's formula applies ONLY to **primes**! For a composite base \\( {base} = {pf_tex} \\), count each prime in \\( {n}! \\) and find the bottleneck.",
                [
                    f"Prime-factorize the base: {m(f'{base}^k = ({pf_tex})^k')}.",
                    " ".join(p_details_en),
                    f"The limiting bottleneck is {m(f'k = \\min({min_tex}) = {ans}')}.",
                ],
                f"You cannot divide {n} directly by {base}; always break {base} into prime powers first!",
            )
            s_ar = explain_ar(
                f"قاعدة ليجاندر تُطبَّق على **الأعداد الأولية فقط**! لذا نحلل الأساس \\( {base} = {pf_tex} \\) ونحسب المتاح من كل عامل أولي في \\( {n}! \\).",
                [
                    f"نكتب قوى الأساس بصورة عوامل أولية: {m(f'{base}^k = ({pf_tex})^k')}.",
                    " ".join(p_details_ar),
                    f"العامل الأقل يحدد الحد الأقصى: {m(f'k = \\min({min_tex}) = {ans}')}.",
                ],
                f"انتبه: لا تقسم {n} مباشرةً على {base} لأن {base} عدد غير أولي!",
            )
        push(topic, diff, "kmc_g1011_legendre_prime_factorial", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 2. kmc_g1011_divisors_of_square_cube (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    div_cases = [
        # (N, left_f, right_f, rl_f, rr_f, mode, param, diff)
        (12, 3, 4, 2, 2, "sq", 0, "Easy"),
        (18, 2, 9, 3, 3, "sq", 0, "Easy"),
        (20, 5, 4, 2, 2, "sq", 0, "Easy"),
        (360, 8, 45, 5, 9, "odd", 0, "Easy"),
        (180, 9, 20, 4, 5, "mult", 6, "Easy"),
        (30, 5, 6, 2, 3, "sq", 0, "Medium"),
        (72, 8, 9, 3, 3, "sq", 0, "Medium"),
        (24, 4, 6, 2, 3, "cube", 0, "Medium"),
        (45, 5, 9, 3, 3, "cube", 0, "Medium"),
        (42, 7, 6, 2, 3, "cube", 0, "Medium"),
        (252, 7, 36, 4, 9, "odd", 0, "Medium"),
        (540, 27, 20, 4, 5, "odd", 0, "Medium"),
        (720, 16, 45, 5, 9, "mult", 12, "Medium"),
        (120, 8, 15, 3, 5, "sq", 0, "Hard"),
        (60, 4, 15, 3, 5, "cube", 0, "Hard"),
        (840, 8, 105, 15, 7, "odd_sq", 0, "Hard"),
        (1260, 9, 140, 10, 14, "mult", 14, "Hard"),
    ]
    for v_i, (N, lf, rf, rlf, rrf, mode, d_mult, diff) in enumerate(div_cases):
        assert lf * rf == N and rlf * rrf == rf
        svg = svg_factor_tree(str(N), str(lf), str(rf), str(rlf), str(rrf))
        pf = _prime_factors(N)
        pf_tex = " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(pf.items()))
        tau_N = math.prod(e + 1 for e in pf.values())

        if mode in ("sq", "cube"):
            mult_pow = 2 if mode == "sq" else 3
            target = N ** mult_pow
            ans = sum(1 for d in range(1, target + 1) if target % d == 0)
            formula_ans = math.prod(mult_pow * e + 1 for e in pf.values())
            assert ans == formula_ans
            pow_pf_tex = " \\times ".join(f"{p}^{{{mult_pow * e}}}" for p, e in sorted(pf.items()))
            prod_terms = " \\times ".join(f"({mult_pow * e} + 1)" for _, e in sorted(pf.items()))
            distractors = [tau_N * mult_pow, tau_N ** mult_pow, ans - 2, ans + 2, tau_N]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_div_{v_i}")
            word_en = "square" if mult_pow == 2 else "cube"
            word_ar = "مربع" if mult_pow == 2 else "مكعب"
            q_en = (
                f"Using the factor tree of {m(N)} shown as a starting point, how many **positive divisors** does "
                f"its {word_en} {m(f'{N}^{mult_pow}')} have?"
            )
            q_ar = (
                f"بالاستعانة بشجرة عوامل العدد {m(N)} الموضحة في الشكل، كم **قاسماً موجباً** يمتلك {word_ar}ه {m(f'{N}^{mult_pow}')}؟"
            )
            h_en = f"Find the prime factorization of {N} first, multiply every prime exponent by {mult_pow} for {N}^{mult_pow}, then add 1 to each new exponent and multiply!"
            h_ar = f"أوجد التحليل الأولي للعدد {N} أولاً، ثم اضرب كل أس في {mult_pow} للحصول على تحليل {m(f'{N}^{mult_pow}')}، ثم أضف 1 لكل أس جديد واضرب!"
            s_en = explain_en(
                f"If \\( N = p_1^{{a}} p_2^{{b}} \\cdots \\), then \\( N^{{{mult_pow}}} = p_1^{{{mult_pow}a}} p_2^{{{mult_pow}b}} \\cdots \\), which has \\( ({mult_pow}a + 1)({mult_pow}b + 1)\\cdots \\) positive divisors.",
                [
                    f"Complete the prime factorization of {m(N)}: {m(f'{N} = {pf_tex}')}.",
                    f"Raise to power {m(mult_pow)} by multiplying each exponent by {m(mult_pow)}: {m(f'{N}^{mult_pow} = {pow_pf_tex}')}.",
                    f"Add {m(1)} to each exponent and multiply: {m(f'{prod_terms} = {ans}')}.",
                ],
                f"Trap check: the number of divisors of \\( N^{mult_pow} \\) is **{ans}**, NOT \\( {mult_pow} \\times d(N) = {mult_pow * tau_N} \\) and NOT \\( d(N)^{mult_pow} = {tau_N ** mult_pow} \\)!",
            )
            s_ar = explain_ar(
                f"إذا كان \\( N = p_1^{{a}} p_2^{{b}} \\cdots \\) فإن \\( N^{{{mult_pow}}} = p_1^{{{mult_pow}a}} p_2^{{{mult_pow}b}} \\cdots \\)، وعدد قواسمه الموجبة هو \\( ({mult_pow}a + 1)({mult_pow}b + 1)\\cdots \\).",
                [
                    f"نكمل التحليل الأولي للعدد {m(N)}: {m(f'{N} = {pf_tex}')}.",
                    f"نرفع للقوة {m(mult_pow)} بضرب كل أس في {m(mult_pow)}: {m(f'{N}^{mult_pow} = {pow_pf_tex}')}.",
                    f"نضيف {m(1)} إلى كل أس ثم نضرب: {m(f'{prod_terms} = {ans}')}.",
                ],
                f"انتبه للفخ: عدد قواسم \\( N^{mult_pow} \\) هو **{ans}**، وليس \\( {mult_pow} \\times d(N) \\) ولا \\( d(N)^{mult_pow} \\)!",
            )
        elif mode in ("odd", "odd_sq"):
            mult_pow = 2 if mode == "odd_sq" else 1
            target = N ** mult_pow
            ans = sum(1 for d in range(1, target + 1) if target % d == 0 and d % 2 == 1)
            odd_primes = [(p, mult_pow * e) for p, e in sorted(pf.items()) if p != 2]
            assert ans == math.prod(e + 1 for _, e in odd_primes)
            odd_terms = " \\times ".join(f"({e} + 1)" for _, e in odd_primes)
            tot_divs = math.prod(mult_pow * e + 1 for e in pf.values())
            distractors = [tot_divs, tot_divs - ans, ans + 2, max(1, ans - 2), tot_divs // 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_div_{v_i}")
            num_disp = f"{N}^2" if mult_pow == 2 else str(N)
            q_en = (
                f"A partial factor tree for {m(N)} is shown. How many **odd positive divisors** does {m(num_disp)} have?"
            )
            q_ar = (
                f"تظهر في الشكل شجرة عوامل جزئية للعدد {m(N)}. كم **قاسماً موجباً فردياً** للعدد {m(num_disp)}؟"
            )
            h_en = "An odd divisor cannot contain ANY factor of 2! Set the exponent of 2 to 0 and count combinations of the odd prime powers."
            h_ar = "القاسم الفردي لا يمكن أن يحتوي على أي عامل 2! اجعل أس العدد 2 مساوياً للصفر واحسب خيارات الأسس للعوامل الأولية الفردية فقط."
            s_en = explain_en(
                "A divisor is **odd** if and only if its exponent of \\( 2 \\) is \\( 0 \\), so we drop \\( 2^a \\) completely and apply the divisor formula to the remaining odd primes!",
                [
                    f"Prime-factorize {m(N)}: {m(f'{N} = {pf_tex}')}" + (f", so {m(f'{N}^2')} doubles every exponent." if mult_pow == 2 else "."),
                    f"Ignore the power of {m(2)} (must choose {m('2^0 = 1')}) and keep the odd prime powers: {m(' \\times '.join(f'{p}^{{{e}}}' for p, e in odd_primes))}.",
                    f"Count choices of exponents: {m(f'{odd_terms} = {ans}')}.",
                ],
                f"Sanity check: out of {m(tot_divs)} total divisors of {m(num_disp)}, {m(ans)} are odd and {m(tot_divs - ans)} are even.",
            )
            s_ar = explain_ar(
                "يكون القاسم **فردياً** إذا وفقط إذا كان أس العامل \\( 2 \\) فيه يساوي \\( 0 \\)؛ لذا نستبعد قوى \\( 2 \\) ونطبق قانون عدد القواسم على العوامل الأولية الفردية فقط!",
                [
                    f"نحلل العدد {m(N)} إلى عوامله الأولية: {m(f'{N} = {pf_tex}')}" + (f"، وفي {m(f'{N}^2')} تتضاعف جميع الأسس." if mult_pow == 2 else "."),
                    f"نهمل قوى العدد {m(2)} ونبقي العوامل الأولية الفردية: {m(' \\times '.join(f'{p}^{{{e}}}' for p, e in odd_primes))}.",
                    f"نحسب عدد القواسم الفردية: {m(f'{odd_terms} = {ans}')}.",
                ],
                f"تحقق: من أصل {m(tot_divs)} قاسماً موجباً للعدد {m(num_disp)}، يوجد {m(ans)} قاسماً فردياً و{m(tot_divs - ans)} قاسماً زوجياً.",
            )
        else:
            # multiples of d_mult dividing N
            assert N % d_mult == 0
            q_val = N // d_mult
            ans = sum(1 for d in range(1, N + 1) if N % d == 0 and d % d_mult == 0)
            q_pf = _prime_factors(q_val)
            assert ans == math.prod(e + 1 for e in q_pf.values())
            q_pf_tex = " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(q_pf.items()))
            q_terms = " \\times ".join(f"({e} + 1)" for _, e in sorted(q_pf.items()))
            distractors = [tau_N, tau_N - ans, ans + 4, max(1, ans - 2), ans * 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_div_{v_i}")
            q_en = (
                f"Using the factor tree of {m(N)} shown, how many positive divisors of {m(N)} are **multiples of {m(d_mult)}**?"
            )
            q_ar = (
                f"بالاستعانة بشجرة عوامل العدد {m(N)} الموضحة، كم قاسماً موجباً للعدد {m(N)} يُعدّ **مضاعفاً للعدد {m(d_mult)}**؟"
            )
            h_en = f"Every divisor of {N} that is a multiple of {d_mult} has the form {d_mult} × k, where k can be ANY positive divisor of {N} ÷ {d_mult} = {q_val}!"
            h_ar = f"كل قاسم للعدد {N} يقبل القسمة على {d_mult} يُكتب على الصورة {m(f'{d_mult} \\times k')} حيث {m('k')} أي قاسم موجب لناتج القسمة {m(f'{N} \\div {d_mult} = {q_val}')}!"
            s_en = explain_en(
                f"Factor out the required multiple first! Writing \\( d = {d_mult}k \\), \\( d \\mid {N} \\) is equivalent to \\( k \\mid \\frac{{{N}}}{{{d_mult}}} \\).",
                [
                    f"Divide {m(N)} by {m(d_mult)}: {m(f'\\frac{{{N}}}{{{d_mult}}} = {q_val}')}.",
                    f"Prime-factorize {m(q_val)}: {m(f'{q_val} = {q_pf_tex}')}.",
                    f"Count all positive divisors of {m(q_val)}: {m(f'{q_terms} = {ans}')}.",
                ],
                f"Multiplying each of the {m(ans)} divisors of {m(q_val)} by {m(d_mult)} produces every multiple-of-{m(d_mult)} divisor of {m(N)} exactly once!",
            )
            s_ar = explain_ar(
                f"أخرج المضاعف المطلوب أولاً! بكتابة القاسم على الصورة \\( d = {d_mult}k \\)، فإن شرط \\( d \\mid {N} \\) يكافئ تماماً \\( k \\mid \\frac{{{N}}}{{{d_mult}}} \\).",
                [
                    f"نقسم {m(N)} على {m(d_mult)}: {m(f'\\frac{{{N}}}{{{d_mult}}} = {q_val}')}.",
                    f"نحلل الناتج {m(q_val)} إلى عوامله الأولية: {m(f'{q_val} = {q_pf_tex}')}.",
                    f"نحسب عدد القواسم الموجبة للعدد {m(q_val)}: {m(f'{q_terms} = {ans}')}.",
                ],
                f"ضرب كل قاسم من قواسم {m(q_val)} البالغ عددها {m(ans)} في {m(d_mult)} يعطينا جميع القواسم المطلوبة بلا تكرار!",
            )
        push(topic, diff, "kmc_g1011_divisors_of_square_cube", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 3. kmc_g1011_frobenius_coin_stamp (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # ------------------------------------------------------------------
    frob_cases = [
        # (a, b, mode, ctx_idx, diff)
        (3, 5, "max", 0, "Easy"),
        (3, 7, "max", 1, "Easy"),
        (4, 5, "max", 2, "Easy"),
        (3, 8, "count", 3, "Easy"),
        (4, 7, "count", 4, "Easy"),
        (5, 7, "max", 0, "Medium"),
        (5, 8, "max", 1, "Medium"),
        (6, 7, "max", 2, "Medium"),
        (5, 9, "count", 3, "Medium"),
        (6, 11, "count", 4, "Medium"),
        (7, 9, "max", 0, "Medium"),
        (4, 9, "thresh", 1, "Medium"),
        (7, 11, "max", 2, "Hard"),
        (8, 13, "max", 3, "Hard"),
        (7, 12, "count", 4, "Hard"),
        (9, 11, "thresh", 0, "Hard"),
    ]
    contexts = [
        ("postage stamps of denominations", "SAR", "طوابع بريدية من فئتي", "ريالات"),
        ("arcade tokens worth", "points", "قطع ألعاب بقيمتي", "نقطة"),
        ("gift vouchers of", "riyals", "قسائم شرائية من فئتي", "ريالاً"),
        ("laboratory calibration weights of", "grams (placed on one pan)", "أوزان معايرة مخبرية من فئتي", "جرامات (توضع في كفة واحدة)"),
        ("data bundles of", "GB", "باقات بيانات بسعتي", "جيجابايت"),
    ]
    for v_i, (a, b, mode, c_idx, diff) in enumerate(frob_cases):
        assert math.gcd(a, b) == 1 and 2 <= a < b
        limit = a * b + 40
        dp = [False] * (limit + 1)
        dp[0] = True
        for val in range(1, limit + 1):
            if (val >= a and dp[val - a]) or (val >= b and dp[val - b]):
                dp[val] = True
        unreach = [val for val in range(1, limit + 1) if not dp[val]]
        max_u = a * b - a - b
        cnt_u = (a - 1) * (b - 1) // 2
        assert max(unreach) == max_u and len(unreach) == cnt_u
        assert all(dp[val] for val in range(max_u + 1, limit + 1))

        en_item, en_unit, ar_item, ar_unit = contexts[c_idx]
        if mode == "max":
            ans = max_u
            distractors = [a * b, a * b - 1, a * b - a, a * b - b, cnt_u]
            q_en = (
                f"A post office or shop has an unlimited supply of {en_item} {m(a)} {en_unit} and {m(b)} {en_unit} only. "
                f"What is the **largest** integer total (in {en_unit}) that **cannot** be formed using non-negative numbers of these two items?"
            )
            q_ar = (
                f"يتوفر عدد غير محدود من {ar_item} {m(a)} و{m(b)} {ar_unit} فقط. "
                f"ما **أكبر** مجموع صحيح (بوحدة {ar_unit}) **لا يمكن** تكوينه باستخدام أعداد غير سالبة من هاتين الفئتين؟"
            )
            h_en = f"Since gcd({a}, {b}) = 1, apply the Chicken McNugget / Frobenius theorem: the largest unreachable integer is a·b − a − b!"
            h_ar = f"بما أن القاسم المشترك الأكبر للعددين {a} و{b} هو 1، استخدم قانون فروبينيوس: أكبر عدد لا يمكن تكوينه هو ab − a − b!"
            s_en = explain_en(
                "For two coprime denominations \\( a \\) and \\( b \\) (\\( \\gcd(a, b) = 1 \\)), the Frobenius coin theorem states that the **largest unreachable** integer is \\( ab - a - b \\).",
                [
                    f"Verify that {m(a)} and {m(b)} are coprime: {m(f'\\gcd({a}, {b}) = 1')}.",
                    f"Substitute into {m('ab - a - b')}: {m(f'{a} \\times {b} - {a} - {b} = {a*b} - {a+b} = {ans}')}.",
                    f"Indeed, {m(ans)} cannot be written as {m(f'{a}x + {b}y')} with integers {m('x, y \\ge 0')}, whereas {m(f'{ans+1}, {ans+2}, \\dots, {ans+a}')} form {m(a)} consecutive reachable values!",
                ],
                f"Once {m(a)} consecutive integers ({m(f'{ans+1}')} through {m(f'{ans+a}')}) are reachable, adding {m(a)} repeatedly reaches EVERY larger integer!",
            )
            s_ar = explain_ar(
                "لأي فئتين أوليتين نسبياً \\( a \\) و\\( b \\) (\\( \\gcd(a, b) = 1 \\))، ينص قانون فروبينيوس على أن **أكبر عدد صحيح لا يمكن تكوينه** هو \\( ab - a - b \\).",
                [
                    f"نتحقق أولاً من عدم وجود عامل مشترك: {m(f'\\gcd({a}, {b}) = 1')}.",
                    f"نعوض في الصيغة {m('ab - a - b')}: {m(f'{a} \\times {b} - {a} - {b} = {a*b} - {a+b} = {ans}')}.",
                    f"العدد {m(ans)} لا يمكن كتابته على الصورة {m(f'{a}x + {b}y')} بأعداد صحيحة غير سالبة، بينما الأعداد الـ {m(a)} المتتالية {m(f'{ans+1}, \\dots, {ans+a}')} كلها قابلة للتكوين!",
                ],
                f"بمجرد تكوين {m(a)} أعداد صحيحة متتالية، يمكن إضافة {m(a)} مراراً للوصول إلى جميع الأعداد الأكبر بلا استثناء!",
            )
        elif mode == "count":
            ans = cnt_u
            distractors = [(a - 1) * (b - 1), max_u, ans + a, max(1, ans - 1), a * b // 2]
            q_en = (
                f"Using an unlimited supply of {en_item} {m(a)} {en_unit} and {m(b)} {en_unit}, "
                f"**how many positive integers** in total **cannot** be expressed in the form {m(f'{a}x + {b}y')} for integers {m('x, y \\ge 0')}?"
            )
            q_ar = (
                f"باستخدام عدد غير محدود من {ar_item} {m(a)} و{m(b)} {ar_unit}، "
                f"**كم عدداً صحيحاً موجباً** إجمالاً **لا يمكن** تمثيله على الصورة {m(f'{a}x + {b}y')} حيث {m('x, y \\ge 0')} عددان صحيحان؟"
            )
            h_en = f"Pair each integer n in [0, {max_u}] with ({max_u} − n): in every pair, custom symmetry makes ONE reachable and ONE unreachable! So the count is (a − 1)(b − 1) / 2."
            h_ar = f"زوّج كل عدد n من 0 إلى {max_u} مع ({max_u} − n): في كل زوج يكون أحدهما قابلاً للتكوين والآخر غير قابل! لذا عددها هو (a − 1)(b − 1) / 2."
            s_en = explain_en(
                "For coprime \\( a, b \\), integers from \\( 0 \\) to \\( ab - a - b \\) pair up into \\( (n,\\; ab - a - b - n) \\) where **exactly one** member of every pair is reachable!",
                [
                    f"Check coprimality: {m(f'\\gcd({a}, {b}) = 1')}. There are {m(f'({max_u} + 1) = (a-1)(b-1) = {(a-1)*(b-1)}')} integers in {m(f'[0, {max_u}]')}.",
                    f"Exactly half of them are unreachable: {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a-1} \\times {b-1}}}{{2}} = {ans}')}.",
                    f"Every integer greater than {m(max_u)} is reachable, so there are no others.",
                ],
                f"Notice \\( ({a}-1)({b}-1) = {(a-1)*(b-1)} \\) is always even because at least one of two coprime numbers is odd!",
            )
            s_ar = explain_ar(
                "عندما يكون \\( \\gcd(a, b) = 1 \\)، تتزاوج الأعداد من \\( 0 \\) إلى \\( ab - a - b \\) في أزواج \\( (n,\\; ab - a - b - n) \\) بحيث يكون **واحد فقط** من كل زوج قابلاً للتكوين!",
                [
                    f"بما أن {m(f'\\gcd({a}, {b}) = 1')}، فإن عدد الأعداد في الفترة {m(f'[0, {max_u}]')} يساوي {m(f'(a-1)(b-1) = {(a-1)*(b-1)}')}.",
                    f"نصفها بالضبط غير قابل للتكوين: {m(f'\\frac{{({a} - 1)({b} - 1)}}{{2}} = \\frac{{{a-1} \\times {b-1}}}{{2}} = {ans}')}.",
                    f"وجميع الأعداد الأكبر من {m(max_u)} قابلة للتكوين، فيكون الإجمالي {m(ans)}.",
                ],
                f"لاحظ أن الجداء \\( ({a}-1)({b}-1) \\) زوجي دائماً لأن أحد العددين الأوليين نسبياً على الأقل فردي!",
            )
        else:
            ans = max_u + 1
            distractors = [max_u, a * b, ans + 1, cnt_u, a * b - a]
            q_en = (
                f"A customer pays using only {en_item} {m(a)} {en_unit} and {m(b)} {en_unit} (no change given). "
                f"What is the **smallest positive integer** {m('M')} such that **every** integer amount {m('n \\ge M')} can be paid exactly?"
            )
            q_ar = (
                f"يدفع زبون باستخدام {ar_item} {m(a)} و{m(b)} {ar_unit} فقط (دون إرجاع باقٍ). "
                f"ما **أصغر عدد صحيح موجب** {m('M')} بحيث يمكن دفع **كل** مبلغ صحيح {m('n \\ge M')} بالضبط؟"
            )
            h_en = f"Be careful! First find the largest UNREACHABLE integer ab − a − b = {max_u}, then add 1 to get the threshold M where every integer from M onward works!"
            h_ar = f"انتبه للصياغة! أوجد أولاً أكبر مبلغ **لا يمكن** دفعه وهو ab − a − b = {max_u}، ثم أضف 1 لتحصل على أصغر بداية M تعمل بعدها جميع الأعداد!"
            s_en = explain_en(
                "Read the threshold carefully: if \\( ab - a - b \\) is the **last** integer that fails, then \\( M = (ab - a - b) + 1 = (a - 1)(b - 1) \\) is the **first** integer from which every integer succeeds!",
                [
                    f"Since {m(f'\\gcd({a}, {b}) = 1')}, the largest unreachable integer is {m(f'{a} \\times {b} - {a} - {b} = {max_u}')}.",
                    f"Because {m(max_u)} itself is unreachable, {m('M')} cannot be {m(max_u)} or smaller.",
                    f"Add {m(1)}: {m(f'M = {max_u} + 1 = ({a}-1)({b}-1) = {ans}')}; every integer {m(f'n \\ge {ans}')} is reachable.",
                ],
                f"Classic KMC reading check: 'largest impossible' is {m(max_u)}, whereas 'smallest M with all n ≥ M possible' is {m(ans)}!",
            )
            s_ar = explain_ar(
                "اقرأ المطلوب بدقة: بما أن \\( ab - a - b \\) هو **آخر** عدد يفشل تكوينه، فإن \\( M = (ab - a - b) + 1 = (a - 1)(b - 1) \\) هو **أول** عدد تنجح بدءاً منه جميع الأعداد المتتالية!",
                [
                    f"بما أن {m(f'\\gcd({a}, {b}) = 1')}، فإن أكبر مبلغ مستحيل تكوينه هو {m(f'{a} \\times {b} - {a} - {b} = {max_u}')}.",
                    f"بما أن {m(max_u)} نفسه غير قابل للدفع، فلا يمكن أن تكون {m('M')} مساوية لـ {m(max_u)} أو أصغر.",
                    f"نضيف {m(1)}: {m(f'M = {max_u} + 1 = ({a}-1)({b}-1) = {ans}')}، وكل عدد {m(f'n \\ge {ans}')} قابل للتكوين.",
                ],
                f"انتبه للفرق الدقيق: «أكبر عدد مستحيل» هو {m(max_u)}، بينما «بداية الأعداد الممكنة دائماً» هي {m(ans)}!",
            )
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_frob_{v_i}")
        push(topic, diff, "kmc_g1011_frobenius_coin_stamp", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)


def _gen_lesson_3_2(push) -> None:
    topic = "Number Theory"

    # ------------------------------------------------------------------
    # 4. kmc_g1011_hermite_paired_floor_sum (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    flr_cases = [
        # ("gauss", p, q, diff) -> sum_{k=1}^{q-1} floor(k*p / q) = (p-1)(q-1)//2
        # ("block", m_div, n_hi, diff) -> sum_{k=1}^{n_hi} floor(k / m_div)
        ("gauss", 5, 7, "Easy"),
        ("gauss", 4, 9, "Easy"),
        ("gauss", 7, 8, "Easy"),
        ("block", 4, 15, "Easy"),
        ("block", 5, 24, "Easy"),
        ("gauss", 9, 11, "Medium"),
        ("gauss", 8, 13, "Medium"),
        ("gauss", 11, 14, "Medium"),
        ("gauss", 12, 17, "Medium"),
        ("gauss", 15, 16, "Medium"),
        ("block", 6, 35, "Medium"),
        ("block", 7, 45, "Medium"),
        ("block", 8, 50, "Medium"),
        ("gauss", 17, 21, "Hard"),
        ("gauss", 19, 24, "Hard"),
        ("gauss", 23, 25, "Hard"),
        ("block", 9, 85, "Hard"),
    ]
    for v_i, (kind, p, q, diff) in enumerate(flr_cases):
        if kind == "gauss":
            assert math.gcd(p, q) == 1
            ans = sum((k * p) // q for k in range(1, q))
            assert ans == (p - 1) * (q - 1) // 2
            distractors = [p * q // 2, (p - 1) * q // 2, p * (q - 1) // 2, ans + (p - 1), max(1, ans - (q - 1) // 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_flr_{v_i}")
            sum_tex = f"\\sum_{{k=1}}^{{{q-1}}} \\left\\lfloor \\frac{{{p}k}}{{{q}}} \\right\\rfloor"
            exp_tex = f"\\left\\lfloor \\frac{{{p}}}{{{q}}} \\right\\rfloor + \\left\\lfloor \\frac{{{2*p}}}{{{q}}} \\right\\rfloor + \\dots + \\left\\lfloor \\frac{{{p*(q-1)}}}{{{q}}} \\right\\rfloor"
            q_en = (
                f"What is the exact value of the floor sum {m(f'{sum_tex} = {exp_tex}')}?"
            )
            q_ar = (
                f"ما القيمة الدقيقة لمجموع دالة الجزء الصحيح {m(f'{sum_tex} = {exp_tex}')}؟"
            )
            h_en = f"Since gcd({p}, {q}) = 1, none of the fractions {p}k/{q} is an integer! Pair the k-th term with the ({q} − k)-th term, or count interior lattice points of a {q} × {p} rectangle!"
            h_ar = f"بما أن القاسم المشترك الأكبر للعددين {p} و{q} هو 1، فلا يوجد أي كسر يساوي عدداً صحيحاً! زوّج الحد رقم k مع الحد رقم ({q} − k)، أو احسب النقاط الشبكية داخل مستطيل {q} × {p}!"
            s_en = explain_en(
                f"Because \\( \\gcd({p}, {q}) = 1 \\), the diagonal of the \\( {q} \\times {p} \\) grid rectangle passes through **zero** interior lattice points, splitting the \\( ({q}-1)({p}-1) \\) interior points into two equal triangles!",
                [
                    f"Pairing view: for any non-integer {m('x')}, {m('\\lfloor x \\rfloor + \\lfloor p - x \\rfloor = p - 1')}. Here {m(f'\\frac{{{p}k}}{{{q}}} + \\frac{{{p}({q}-k)}}{{{q}}} = {p}')} is never an integer for {m(f'1 \\le k \\le {q-1}')}.",
                    f"So every symmetric pair sums to {m(f'{p} - 1 = {p-1}')} (and if there is a middle term, it equals {m(f'({p}-1)/2')}).",
                    f"Across {m(f'{q} - 1 = {q-1}')} terms, the sum is {m(f'\\frac{{({p} - 1)({q} - 1)}}{{2}} = \\frac{{{p-1} \\times {q-1}}}{{2}} = {ans}')}.",
                ],
                f"Lattice check: there are \\( {q-1} \\times {p-1} = {(p-1)*(q-1)} \\) interior grid points in \\( (0,{q}) \\times (0,{p}) \\), and exactly half ({m(ans)}) lie below \\( y = \\frac{{{p}}}{{{q}}}x \\)!",
            )
            s_ar = explain_ar(
                f"بما أن \\( \\gcd({p}, {q}) = 1 \\)، فإن قطر المستطيل الشبكي \\( {q} \\times {p} \\) لا يمر بأي نقطة شبكية داخلية، فيقسم النقاط الداخلية البالغ عددها \\( ({q}-1)({p}-1) \\) إلى مثلثين متطابقين تماماً!",
                [
                    f"طريقة التزويج: لأي عدد غير صحيح {m('x')} يتحقق {m(f'\\lfloor x \\rfloor + \\lfloor {p} - x \\rfloor = {p} - 1')}. وهنا {m(f'\\frac{{{p}k}}{{{q}}}')} ليس عدداً صحيحاً أبداً لأن {m(f'\\gcd({p},{q})=1')}.",
                    f"إذن مجموع كل حدّين متناظرين (الأول مع الأخير، وهكذا) يساوي {m(f'{p} - 1 = {p-1}')}.",
                    f"لعدد {m(f'{q} - 1 = {q-1}')} من الحدود، يكون المجموع الكلي {m(f'\\frac{{({p} - 1)({q} - 1)}}{{2}} = \\frac{{{p-1} \\times {q-1}}}{{2}} = {ans}')}.",
                ],
                f"تحقق هندسي: عدد النقاط الصحيحة داخل المستطيل هو \\( {q-1} \\times {p-1} = {(p-1)*(q-1)} \\)، ونصفها تماماً ({m(ans)}) يقع تحت القطر!",
            )
        else:
            m_div, n_hi = p, q
            ans = sum(k // m_div for k in range(1, n_hi + 1))
            num_full_quot = (n_hi + 1) // m_div  # blocks 0..num_full_quot-1 (note k=0 omitted, doesn't affect sum since 0//m=0)
            max_q = n_hi // m_div
            tail_cnt = n_hi - max_q * m_div + 1
            # Formula check: m_div * (1 + 2 + ... + (max_q - 1)) + tail_cnt * max_q
            assert ans == m_div * (max_q - 1) * max_q // 2 + tail_cnt * max_q
            distractors = [ans + max_q, max(1, ans - max_q), ans + m_div, (n_hi * (n_hi + 1) // 2) // m_div]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_flr_{v_i}")
            q_en = (
                f"Find the value of the sum {m(f'\\sum_{{k=1}}^{{{n_hi}}} \\left\\lfloor \\frac{{k}}{{{m_div}}} \\right\\rfloor = \\left\\lfloor \\frac{{1}}{{{m_div}}} \\right\\rfloor + \\left\\lfloor \\frac{{2}}{{{m_div}}} \\right\\rfloor + \\dots + \\left\\lfloor \\frac{{{n_hi}}}{{{m_div}}} \\right\\rfloor')}."
            )
            q_ar = (
                f"أوجد قيمة المجموع {m(f'\\sum_{{k=1}}^{{{n_hi}}} \\left\\lfloor \\frac{{k}}{{{m_div}}} \\right\\rfloor = \\left\\lfloor \\frac{{1}}{{{m_div}}} \\right\\rfloor + \\left\\lfloor \\frac{{2}}{{{m_div}}} \\right\\rfloor + \\dots + \\left\\lfloor \\frac{{{n_hi}}}{{{m_div}}} \\right\\rfloor')}."
            )
            h_en = f"Group consecutive values of k into blocks of size {m_div} where ⌊k/{m_div}⌋ stays constant (0, then {m_div} ones, {m_div} twos, ...)!"
            h_ar = f"جمّع قيم k المتتالية في مجموعات طول كل منها {m_div} حيث تبقى قيمة ⌊k/{m_div}⌋ ثابتة (أصفار، ثم {m_div} واحدات، ثم {m_div} اثنينات، وهكذا)!"
            full_sum = (max_q - 1) * max_q // 2
            s_en = explain_en(
                f"The floor \\( \\lfloor k/{m_div} \\rfloor \\) jumps by \\( 1 \\) only at multiples of \\( {m_div} \\), so each integer quotient \\( j \\ge 1 \\) repeats \\( {m_div} \\) times in a complete block!",
                [
                    f"For {m(f'1 \\le k \\le {m_div - 1}')}, the floor is {m(0)}. Each value {m(f'j = 1, 2, \\dots, {max_q - 1}')} appears in a full block of {m(m_div)} terms ({m(f'k = {m_div}j')} through {m(f'{m_div}j + {m_div - 1}')}).",
                    f"Sum of full blocks: {m(f'{m_div} \\times (1 + 2 + \\dots + {max_q - 1}) = {m_div} \\times {full_sum} = {m_div * full_sum}')}.",
                    f"Remaining tail from {m(f'k = {max_q * m_div}')} to {m(n_hi)} has {m(f'{n_hi} - {max_q * m_div} + 1 = {tail_cnt}')} terms each equal to {m(max_q)}: {m(f'{m_div * full_sum} + {tail_cnt} \\times {max_q} = {ans}')}.",
                ],
                f"Watch the endpoint count: from \\( {max_q * m_div} \\) to \\( {n_hi} \\) inclusive there are \\( {tail_cnt} \\) terms (don't forget \\( +1 \\))!",
            )
            s_ar = explain_ar(
                f"قيمة \\( \\lfloor k/{m_div} \\rfloor \\) تقفز بمقدار \\( 1 \\) عند مضاعفات \\( {m_div} \\) فقط، لذا تتكرر كل قيمة صحيحة \\( j \\ge 1 \\) بالضبط \\( {m_div} \\) مرات في كل مجموعة مكتملة!",
                [
                    f"للقيم {m(f'1 \\le k \\le {m_div - 1}')} يكون الناتج {m(0)}، ثم تتكرر كل قيمة {m(f'j = 1, 2, \\dots, {max_q - 1}')} في مجموعة كاملة من {m(m_div)} حدود.",
                    f"مجموع المجموعات الكاملة: {m(f'{m_div} \\times (1 + 2 + \\dots + {max_q - 1}) = {m_div} \\times {full_sum} = {m_div * full_sum}')}.",
                    f"الحدود المتبقية من {m(f'k = {max_q * m_div}')} إلى {m(n_hi)} عددها {m(f'{n_hi} - {max_q * m_div} + 1 = {tail_cnt}')} وقيمة كل منها {m(max_q)}: {m(f'{m_div * full_sum} + {tail_cnt} \\times {max_q} = {ans}')}.",
                ],
                f"تذكّر حساب الحدود من \\( {max_q * m_div} \\) إلى \\( {n_hi} \\) شاملاً الطرفين بإضافة \\( 1 \\): عددها \\( {tail_cnt} \\)!",
            )
        push(topic, diff, "kmc_g1011_hermite_paired_floor_sum", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 5. kmc_g1011_base_b_representation (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    base_cases = [
        # ("bulbs", base, bits_tuple, diff)
        ("bulbs", 3, (1, 0, 1, 1), "Easy"),
        ("bulbs", 4, (1, 1, 0, 1), "Easy"),
        ("bulbs", 3, (1, 1, 0, 1, 0), "Easy"),
        ("to10", 5, (2, 3, 4), "Easy"),
        ("to10", 6, (1, 4, 5), "Easy"),
        ("bulbs", 5, (1, 0, 1, 1), "Medium"),
        ("bulbs", 6, (1, 1, 0, 1), "Medium"),
        ("bulbs", 3, (1, 0, 1, 1, 1), "Medium"),
        ("to10", 7, (3, 2, 5), "Medium"),
        ("to10", 8, (2, 5, 3), "Medium"),
        ("digsum", 3, 100, "Medium"),
        ("digsum", 5, 194, "Medium"),
        ("digsum", 7, 250, "Medium"),
        ("swap", 5, (4, 2), "Hard"),      # (42)_b = (24)_{b+2}? Wait: check algebra below!
        ("swap_general", 0, (5, 3, 2), "Hard"),
        ("find_b", 6, (2, 3, 5), "Hard"),
        ("digsum", 4, 503, "Hard"),
    ]
    # Let's prepare exact algebraic swap cases cleanly before looping:
    # Equation: (a b)_k = (b a)_{k + d_step} => a*k + b = b*(k + d_step) + a => (a - b)*(k - 1) = b * d_step!
    # Case A: a=5, b=3, d_step=2 => 2*(k - 1) = 6 => k = 4? Wait digit 5 not valid in base 4!
    # Check digit validity: max(a, b) < k!
    # Let's pick valid (a, b, d_step, k):
    # 1) a=5, b=2, d_step=3 => 3*(k - 1) = 6? Wait b*d_step = 2*3 = 6 => 3*(k-1)=6 => k=3 (invalid since a=5>=3).
    # Wait: (a - b)*(k - 1) = b * d_step! For k > a > b: k - 1 >= a, so b * d_step = (a - b)*(k - 1) >= (a - b)*a!
    # Take a=4, b=3, k=7: (4 - 3)*(7 - 1) = 6 = 3 * 2 => d_step = 2!
    # CHECK: (43)_7 = 4*7 + 3 = 31; (34)_9 = 3*9 + 4 = 31! Digits 4,3 < 7 and < 9! PERFECT!
    # 2) Take a=5, b=4, k=9: (5 - 4)*(9 - 1) = 8 = 4 * 2 => d_step = 2!
    # CHECK: (54)_9 = 5*9 + 4 = 49; (45)_11? Keep bases <= 9:
    # Take a=3, b=2, k=5: (3 - 2)*(5 - 1) = 4 = 2 * 2 => d_step = 2!
    # CHECK: (32)_5 = 3*5 + 2 = 17; (23)_7 = 2*7 + 3 = 17! Bases 5 and 7 (both in 3..9)! PERFECT!
    base_cases[13] = ("swap", 5, (3, 2, 2), "Hard")   # (32)_b = (23)_{b+2} -> find b = 5
    base_cases[14] = ("swap", 7, (4, 3, 2), "Hard")   # (43)_b = (34)_{b+2} -> find base-10 value = 31

    for v_i, (kind, b_val, payload, diff) in enumerate(base_cases):
        if kind == "bulbs":
            bits = payload
            n_b = len(bits)
            weights = tuple(b_val ** (n_b - 1 - i) for i in range(n_b))
            svg = svg_binary_bulbs(bits, weights)
            ans = sum(bit * w for bit, w in zip(bits, weights))
            dig_str = "".join(str(x) for x in bits)
            assert int(dig_str, b_val) == ans
            active_w = [str(w) for bit, w in zip(bits, weights) if bit]
            distractors = [sum(weights), int(dig_str, 2), ans + b_val, max(1, ans - b_val), ans + 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_base_{v_i}")
            q_en = (
                f"A base-{m(b_val)} place-value indicator panel displays the numeral {m(f'({dig_str})_{{{b_val}}}')}, "
                f"where **ON** represents digit {m(1)} and **OFF** represents digit {m(0)}, as shown. "
                f"What is the **base-{m(10)}** value of {m(f'({dig_str})_{{{b_val}}}')}?"
            )
            q_ar = (
                f"تعرض لوحة القيم المكانية ذات الأساس {m(b_val)} العدد {m(f'({dig_str})_{{{b_val}}}')}، "
                f"حيث يمثّل المصباح المضاء (**ON**) الرقم {m(1)} والمطفأ (**OFF**) الرقم {m(0)} كما في الشكل. "
                f"ما قيمة العدد {m(f'({dig_str})_{{{b_val}}}')} في **النظام العشري** (الأساس {m(10)})؟"
            )
            h_en = f"In base {b_val}, the place weights from right to left are 1, {b_val}, {b_val**2}, ... — simply add the weights of the ON lamps!"
            h_ar = f"في الأساس {b_val}، تتضاعف القيم المكانية بالضرب في {b_val} من اليمين لليسار — اجمع أوزان المصابيح المضاءة (ON) فقط!"
            s_en = explain_en(
                f"In base \\( {b_val} \\), each position carries a power of \\( {b_val} \\): \\( {', '.join(str(w) for w in weights)} \\) from left to right.",
                [
                    f"Expand {m(f'({dig_str})_{{{b_val}}}')} using powers of {m(b_val)}: {m(' + '.join(f'{bit} \\times {w}' for bit, w in zip(bits, weights)))}.",
                    f"Keep only the active (**ON**) weights: {m(' + '.join(active_w))}.",
                    f"Add them together: {m(f' = {ans}')}.",
                ],
                f"Don't confuse base {m(b_val)} with binary (base 2): here each step left multiplies the weight by {m(b_val)}!",
            )
            s_ar = explain_ar(
                f"في نظام العد ذي الأساس \\( {b_val} \\)، تحمل الخانات قوى العدد \\( {b_val} \\): \\( {', '.join(str(w) for w in weights)} \\) من اليسار إلى اليمين.",
                [
                    f"نفكّك العدد {m(f'({dig_str})_{{{b_val}}}')} بحسب القيم المكانية: {m(' + '.join(f'{bit} \\times {w}' for bit, w in zip(bits, weights)))}.",
                    f"نحتفظ بأوزان الخانات الفعّالة (**ON**) فقط: {m(' + '.join(active_w))}.",
                    f"نجمعها لنحصل على القيمة العشرية: {m(str(ans))}.",
                ],
                f"انتبه: الأساس هنا هو {m(b_val)} وليس النظام الثنائي {m(2)}!",
            )
            push(topic, diff, "kmc_g1011_base_b_representation", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

        elif kind == "to10":
            d2, d1, d0 = payload
            assert max(d2, d1, d0) < b_val
            ans = d2 * (b_val ** 2) + d1 * b_val + d0
            dig_str = f"{d2}{d1}{d0}"
            assert int(dig_str, b_val) == ans
            distractors = [d0 * (b_val ** 2) + d1 * b_val + d2, d2 * b_val + d1 + d0, ans + b_val, max(1, ans - b_val)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_base_{v_i}")
            q_en = (
                f"Convert the base-{m(b_val)} numeral {m(f'({dig_str})_{{{b_val}}}')} into its equivalent **base-{m(10)}** integer."
            )
            q_ar = (
                f"حوّل العدد المكتوب في الأساس {m(b_val)} بالصورة {m(f'({dig_str})_{{{b_val}}}')} إلى قيمته المكافئة في **النظام العشري** (الأساس {m(10)})."
            )
            h_en = f"Expand ({dig_str})_{b_val} = {d2}×{b_val}² + {d1}×{b_val}¹ + {d0}×{b_val}⁰!"
            h_ar = f"فكّك العدد بحسب الخانات: {m(f'({dig_str})_{{{b_val}}} = {d2} \\times {b_val}^2 + {d1} \\times {b_val} + {d0}')}!"
            s_en = explain_en(
                f"A three-digit numeral \\( (abc)_{{{b_val}}} \\) stands for \\( a \\cdot {b_val}^2 + b \\cdot {b_val} + c \\).",
                [
                    f"Identify the place values in base {m(b_val)}: {m(f'{b_val}^2 = {b_val**2}')}, {m(f'{b_val}^1 = {b_val}')}, and {m(f'{b_val}^0 = 1')}.",
                    f"Multiply each digit by its place weight: {m(f'{d2} \\times {b_val**2} + {d1} \\times {b_val} + {d0} \\times 1 = {d2*(b_val**2)} + {d1*b_val} + {d0}')}.",
                    f"Sum the parts: {m(f'{d2*(b_val**2)} + {d1*b_val} + {d0} = {ans}')}.",
                ],
                f"Valid-digit check: every digit ({m(f'{d2}, {d1}, {d0}')}) is strictly less than the base {m(b_val)}.",
            )
            s_ar = explain_ar(
                f"العدد المكوّن من ثلاث خانات \\( (abc)_{{{b_val}}} \\) يساوي \\( a \\cdot {b_val}^2 + b \\cdot {b_val} + c \\).",
                [
                    f"نحدد أوزان الخانات في الأساس {m(b_val)}: {m(f'{b_val}^2 = {b_val**2}')}، و{m(f'{b_val}^1 = {b_val}')}، و{m(f'{b_val}^0 = 1')}.",
                    f"نضرب كل رقم في وزن خانته: {m(f'{d2} \\times {b_val**2} + {d1} \\times {b_val} + {d0} \\times 1 = {d2*(b_val**2)} + {d1*b_val} + {d0}')}.",
                    f"نجمع النواتج: {m(f'{d2*(b_val**2)} + {d1*b_val} + {d0} = {ans}')}.",
                ],
                f"تحقق سريع: جميع الأرقام ({m(f'{d2}, {d1}, {d0}')}) أصغر تماماً من الأساس {m(b_val)}.",
            )
            push(topic, diff, "kmc_g1011_base_b_representation", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

        elif kind == "digsum":
            N_dec = payload
            digs = _base_b_digits(N_dec, b_val)
            ans = sum(digs)
            dig_str = "".join(str(x) for x in digs)
            div_steps = []
            rem_n = N_dec
            while rem_n > 0:
                q_n, r_n = divmod(rem_n, b_val)
                div_steps.append(f"{rem_n} = {b_val} \\times {q_n} + {r_n}")
                rem_n = q_n
            distractors = [len(digs), ans + 2, max(1, ans - 2), sum(int(c) for c in str(N_dec)), ans + 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_base_{v_i}")
            q_en = (
                f"When the base-{m(10)} integer {m(N_dec)} is written in **base {m(b_val)}**, what is the **sum of its digits**?"
            )
            q_ar = (
                f"عند كتابة العدد العشري {m(N_dec)} في **الأساس {m(b_val)}**، ما **مجموع أرقامه** في ذلك الأساس؟"
            )
            h_en = f"Repeatedly divide {N_dec} by {b_val} and record the remainders — those remainders ARE the base-{b_val} digits!"
            h_ar = f"اقسم العدد {N_dec} بشكل متكرر على {b_val} وسجّل البواقي — فهذه البواقي هي أرقام العدد في الأساس {b_val} تماماً!"
            s_en = explain_en(
                f"Repeated division by \\( {b_val} \\) peels off the base-\\( {b_val} \\) digits from right (units) to left!",
                [
                    f"Divide by {m(b_val)} step by step: {m(';\\; '.join(div_steps))}.",
                    f"Reading remainders from last to first gives {m(f'{N_dec} = ({dig_str})_{{{b_val}}}')}.",
                    f"Sum the base-{m(b_val)} digits: {m(' + '.join(str(x) for x in digs) + f' = {ans}')}.",
                ],
                f"Reverse check: {m(' + '.join(f'{d} \\times {b_val}^{{{len(digs)-1-i}}}' for i, d in enumerate(digs)) + f' = {N_dec}')}!",
            )
            s_ar = explain_ar(
                f"القسمة المتكررة على \\( {b_val} \\) تستخرج أرقام العدد في الأساس \\( {b_val} \\) من اليمين إلى اليسار عبر البواقي!",
                [
                    f"نقسم على {m(b_val)} خطوة بخطوة: {m(' ، '.join(div_steps))}.",
                    f"بقراءة البواقي من الأسفل للأعلى نجد {m(f'{N_dec} = ({dig_str})_{{{b_val}}}')}.",
                    f"نجمع الأرقام الناتجة: {m(' + '.join(str(x) for x in digs) + f' = {ans}')}.",
                ],
                f"تحقق عكسي: {m(' + '.join(f'{d} \\times {b_val}^{{{len(digs)-1-i}}}' for i, d in enumerate(digs)) + f' = {N_dec}')}!",
            )
            push(topic, diff, "kmc_g1011_base_b_representation", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

        elif kind == "swap":
            da, db, d_step = payload
            # Verify unique base b > max(da, db) with da*b + db == db*(b + d_step) + da
            sols = [k for k in range(max(da, db) + 1, 50) if da * k + db == db * (k + d_step) + da]
            assert sols == [b_val]
            val_10 = da * b_val + db
            if b_val == 5:
                ans = b_val
                distractors = [b_val + 1, b_val + 2, b_val - 1, val_10]
                q_en = (
                    f"Find the positive integer base {m('b')} such that the two-digit base-{m('b')} numeral {m(f'({da}{db})_b')} "
                    f"equals the two-digit base-{m(f'(b + {d_step})')} numeral {m(f'({db}{da})_{{b+{d_step}}}')}."
                )
                q_ar = (
                    f"أوجد أساس العد الصحيح الموجب {m('b')} الذي يحقق تساوي العدد {m(f'({da}{db})_b')} في الأساس {m('b')} "
                    f"مع العدد {m(f'({db}{da})_{{b+{d_step}}}')} في الأساس {m(f'(b + {d_step})')}."
                )
                last_en = f"Solve for {m('b')}: {m(f'{da - db}b = {da - db + db * d_step} \\implies b = {ans}')} (valid since {m(f'b = {ans} > {da}')})."
                last_ar = f"نحل المعادلة لإيجاد {m('b')}: {m(f'{da - db}b = {da - db + db * d_step} \\implies b = {ans}')} (وهو مقبول لأن {m(f'{ans} > {da}')})."
            else:
                ans = val_10
                distractors = [b_val, b_val + d_step, val_10 + da, val_10 - db]
                q_en = (
                    f"In a certain integer base {m('b')}, the two-digit numeral {m(f'({da}{db})_b')} represents the exact same number as "
                    f"{m(f'({db}{da})_{{b+{d_step}}}')} in base {m(f'b + {d_step}')}. What is this number written in **base {m(10)}**?"
                )
                q_ar = (
                    f"في أساس عد صحيح {m('b')}، يمثّل العدد {m(f'({da}{db})_b')} نفس القيمة التي يمثّلها العدد "
                    f"{m(f'({db}{da})_{{b+{d_step}}}')} في الأساس {m(f'b + {d_step}')}. ما قيمة هذا العدد في **النظام العشري** (الأساس {m(10)})؟"
                )
                last_en = f"Solve {m(f'b = {b_val}')}, then convert to base {m(10)}: {m(f'({da}{db})_{{{b_val}}} = {da}({b_val}) + {db} = {ans}')}."
                last_ar = f"نجد {m(f'b = {b_val}')}، ثم نحوّل للنظام العشري: {m(f'({da}{db})_{{{b_val}}} = {da}({b_val}) + {db} = {ans}')}."
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_base_{v_i}")
            h_en = f"Translate both sides into base 10 using place value: {da}·b + {db} = {db}·(b + {d_step}) + {da}!"
            h_ar = f"ترجم الطرفين إلى معادلة جبرية عبر القيمة المكانية: {m(f'{da}b + {db} = {db}(b + {d_step}) + {da}')}!"
            s_en = explain_en(
                "Turn unknown-base equations into ordinary linear equations by expanding each side in powers of its base!",
                [
                    f"Left side in base {m(10)}: {m(f'({da}{db})_b = {da}b + {db}')}.",
                    f"Right side in base {m(10)}: {m(f'({db}{da})_{{b+{d_step}}} = {db}(b + {d_step}) + {da} = {db}b + {db*d_step + da}')}.",
                    last_en,
                ],
                f"Both sides match: \\( ({da}{db})_{{{b_val}}} = {val_10} \\) and \\( ({db}{da})_{{{b_val+d_step}}} = {db}({b_val+d_step}) + {da} = {val_10} \\)!",
            )
            s_ar = explain_ar(
                "نحوّل معادلات أنظمة العد إلى معادلة جبرية بسيطة بفكّ كل طرف حسب أوزان خاناته!",
                [
                    f"الطرف الأيسر بالقيمة العشرية: {m(f'({da}{db})_b = {da}b + {db}')}.",
                    f"الطرف الأيمن بالقيمة العشرية: {m(f'({db}{da})_{{b+{d_step}}} = {db}(b + {d_step}) + {da} = {db}b + {db*d_step + da}')}.",
                    last_ar,
                ],
                f"تحقق: \\( ({da}{db})_{{{b_val}}} = {val_10} \\) وكذلك \\( ({db}{da})_{{{b_val+d_step}}} = {db}({b_val+d_step}) + {da} = {val_10} \\)!",
            )
            push(topic, diff, "kmc_g1011_base_b_representation", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

        else:
            # kind == "find_b": (d2 d1 d0)_b = N_dec -> solve quadratic d2*b^2 + d1*b + d0 = N_dec for integer b > max(d2,d1,d0)
            d2, d1, d0 = payload
            N_dec = d2 * (b_val ** 2) + d1 * b_val + d0
            sols = [k for k in range(max(d2, d1, d0) + 1, 50) if d2 * k * k + d1 * k + d0 == N_dec]
            assert sols == [b_val]
            ans = b_val
            distractors = [b_val + 1, b_val + 2, b_val - 1, b_val + 3]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_base_{v_i}")
            q_en = (
                f"In what positive integer base {m('b')} does the three-digit numeral {m(f'({d2}{d1}{d0})_b')} equal the base-{m(10)} number {m(N_dec)}?"
            )
            q_ar = (
                f"في أي أساس عد صحيح موجب {m('b')} يساوي العدد ذو الثلاث خانات {m(f'({d2}{d1}{d0})_b')} القيمة العشرية {m(N_dec)}؟"
            )
            h_en = f"Set {d2}b² + {d1}b + {d0} = {N_dec}, note that b must be greater than the largest digit {max(d2,d1,d0)}, and bound {d2}b² ≤ {N_dec}!"
            h_ar = f"اكتب المعادلة {m(f'{d2}b^2 + {d1}b + {d0} = {N_dec}')}، ولاحظ أن الأساس {m('b')} أكبر من أكبر رقم ({m(max(d2,d1,d0))}) مع كون {m(f'{d2}b^2 < {N_dec}')}!"
            s_en = explain_en(
                "Expand in powers of \\( b \\) and use size bounds + digit bounds before doing heavy algebra!",
                [
                    f"Write the place-value equation: {m(f'{d2}b^2 + {d1}b + {d0} = {N_dec} \\implies {d2}b^2 + {d1}b = {N_dec - d0}')}.",
                    f"Since digit {m(max(d2,d1,d0))} appears, {m(f'b > {max(d2,d1,d0)}')}. Also {m(f'{d2}b^2 < {N_dec} \\implies b^2 < {N_dec / d2:.1f}')}, which immediately narrows {m('b')} to {m(b_val)}!",
                    f"Verify {m(f'b = {b_val}')}: {m(f'{d2}({b_val})^2 + {d1}({b_val}) + {d0} = {d2*b_val**2} + {d1*b_val} + {d0} = {N_dec}')}.",
                ],
                f"Bounding \\( b \\) between \\( {max(d2,d1,d0)+1} \\) and \\( \\sqrt{{{N_dec}/{d2}}} \\) finds \\( b = {b_val} \\) in seconds!",
            )
            s_ar = explain_ar(
                "نفكّك العدد بدلالة \\( b \\) ونستخدم حصر القيمة وشرط صحة الأرقام للوصول للحل بسرعة!",
                [
                    f"نكتب معادلة القيمة المكانية: {m(f'{d2}b^2 + {d1}b + {d0} = {N_dec} \\implies {d2}b^2 + {d1}b = {N_dec - d0}')}.",
                    f"وجود الرقم {m(max(d2,d1,d0))} يفرض {m(f'b > {max(d2,d1,d0)}')}. كما أن {m(f'{d2}b^2 < {N_dec}')} يحصر {m('b')} مباشرةً عند {m(b_val)}!",
                    f"نتحقق من {m(f'b = {b_val}')}: {m(f'{d2}({b_val})^2 + {d1}({b_val}) + {d0} = {d2*b_val**2} + {d1*b_val} + {d0} = {N_dec}')}.",
                ],
                f"حصر الأساس \\( b \\) يوفّر عليك حل المعادلة التربيعية كاملةً!",
            )
            push(topic, diff, "kmc_g1011_base_b_representation", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. kmc_g1011_constrained_sum_prod_extremum (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # ------------------------------------------------------------------
    ext_cases = [
        # ("amgm", a, b, diff) -> min of a*x + b/x for x > 0 is 2*sqrt(a*b)
        # ("rect_prod", S, k, diff) -> max of x*(S - k*x) is S^2 / (4*k)
        # ("sum_sq", S, diff) -> min of x^2 + y^2 given x + y = S is S^2 / 2
        ("amgm", 1, 9, "Easy"),
        ("amgm", 1, 25, "Easy"),
        ("rect_prod", 12, 1, "Easy"),
        ("rect_prod", 20, 1, "Easy"),
        ("sum_sq", 10, "Easy"),
        ("amgm", 4, 9, "Medium"),
        ("amgm", 2, 18, "Medium"),
        ("amgm", 3, 27, "Medium"),
        ("rect_prod", 16, 2, "Medium"),
        ("rect_prod", 24, 3, "Medium"),
        ("sum_sq", 14, "Medium"),
        ("sum_sq", 18, "Medium"),
        ("amgm", 5, 45, "Hard"),
        ("amgm_shift", 1, 16, "Hard"),     # min of x + 16/(x - 3) for x > 3 -> (x - 3) + 16/(x - 3) + 3 = 8 + 3 = 11!
        ("rect_prod", 30, 5, "Hard"),
        ("sum_sq_w", 15, "Hard"),          # min of x^2 + 2*y^2 given x + y = 15 -> 2*(x-10)^2? Wait: x=15-y => (15-y)^2+2y^2 = 3y^2-30y+225 = 3(y-5)^2 + 150!
    ]
    for v_i, item in enumerate(ext_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "amgm":
            _, a, b, _ = item
            rt = math.isqrt(a * b)
            assert rt * rt == a * b
            ans = 2 * rt
            x_opt = Fraction(rt, a)
            assert a * x_opt + Fraction(b, 1) / x_opt == ans
            expr_tex = f"x + \\frac{{{b}}}{{x}}" if a == 1 else f"{a}x + \\frac{{{b}}}{{x}}"
            distractors = [rt, a + b, 2 * a * b if 2 * a * b < 200 else ans + 4, ans + 2, max(1, ans - 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_ext_{v_i}")
            q_en = (
                f"Over all positive real numbers {m('x > 0')}, what is the **minimum possible value** of {m(expr_tex)}?"
            )
            q_ar = (
                f"لجميع الأعداد الحقيقية الموجبة {m('x > 0')}، ما **أصغر قيمة ممكنة** للمقدار {m(expr_tex)}؟"
            )
            h_en = f"Notice that ({a}x) × ({b}/x) = {a*b} is constant! Complete the square using (√({a}x) − √({b}/x))² ≥ 0!"
            h_ar = f"لاحظ أن حاصل ضرب الحدين ثابت لا يعتمد على x: {m(f'({a}x) \\times ({b}/x) = {a*b}')}! استخدم إكمال المربع {m('(u - v)^2 \\ge 0')}!"
            s_en = explain_en(
                "For any two positive numbers \\( A, B > 0 \\), \\( (\\sqrt{A} - \\sqrt{B})^2 \\ge 0 \\) expands to \\( A + B \\ge 2\\sqrt{AB} \\) (AM-GM inequality), with equality when \\( A = B \\)!",
                [
                    f"Set {m(f'A = {a}x' if a > 1 else 'A = x')} and {m(f'B = \\frac{{{b}}}{{x}}')}. Since {m('x > 0')}, both are positive and their product is constant: {m(f'AB = {a*b}')}.",
                    f"Apply {m('A + B \\ge 2\\sqrt{AB}')}: {m(f'{expr_tex} \\ge 2\\sqrt{{{a*b}}} = 2 \\times {rt} = {ans}')}.",
                    f"Confirm equality is achieved: {m(f'A = B \\implies x = {fmt_val(x_opt)} > 0')}, giving {m(ans)} exactly.",
                ],
                f"Always verify equality holds at a valid \\( x > 0 \\) (\\( x = {fmt_val(x_opt)} \\))!",
            )
            s_ar = explain_ar(
                "لأي عددين موجبين \\( A, B > 0 \\)، المتباينة البديهية \\( (\\sqrt{A} - \\sqrt{B})^2 \\ge 0 \\) تعطي \\( A + B \\ge 2\\sqrt{AB} \\)، وتتحقق المساواة عندما \\( A = B \\)!",
                [
                    f"نضع {m(f'A = {a}x' if a > 1 else 'A = x')} و{m(f'B = \\frac{{{b}}}{{x}}')}. حاصل ضربهما ثابت: {m(f'AB = {a*b}')}.",
                    f"بتطبيق المتباينة: {m(f'{expr_tex} \\ge 2\\sqrt{{{a*b}}} = 2 \\times {rt} = {ans}')}.",
                    f"نتأكد من تحقق المساواة عند {m('A = B')}: أي عند {m(f'x = {fmt_val(x_opt)} > 0')}، فنحصل على {m(ans)} فعلاً.",
                ],
                f"التحقق من وجود قيمة موجبة \\( x = {fmt_val(x_opt)} \\) يضمن أن {m(ans)} هي القيمة الصغرى الفعلية!",
            )
        elif kind == "amgm_shift":
            _, _, b, _ = item
            # min of x + b/(x - 3) for x > 3
            rt = math.isqrt(b)
            ans = 2 * rt + 3
            # Check at x - 3 = rt => x = 3 + rt: (3+rt) + b/rt = 3 + 2*rt
            assert (3 + rt) + b // rt == ans
            distractors = [2 * rt, 2 * rt - 3, ans + 3, b + 3]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_ext_{v_i}")
            q_en = (
                f"For all real numbers {m('x > 3')}, what is the **minimum value** of {m(f'x + \\frac{{{b}}}{{x - 3}}')}?"
            )
            q_ar = (
                f"لجميع الأعداد الحقيقية {m('x > 3')}، ما **القيمة الصغرى** للمقدار {m(f'x + \\frac{{{b}}}{{x - 3}}')}؟"
            )
            h_en = f"Rewrite x as (x − 3) + 3 so the first term matches the denominator (x − 3) > 0!"
            h_ar = f"أعد كتابة x على الصورة (x − 3) + 3 لكي يختصر القوس (x − 3) > 0 عند الضرب في المقام!"
            s_en = explain_en(
                "Match the denominator by subtracting and adding \\( 3 \\): \\( x + \\frac{16}{x-3} = (x - 3) + \\frac{16}{x - 3} + 3 \\)!",
                [
                    f"Let {m('t = x - 3 > 0')}. Then the expression becomes {m(f't + \\frac{{{b}}}{{t}} + 3')}.",
                    f"Since {m(f'\\left(\\sqrt{{t}} - \\frac{{{rt}}}{{\\sqrt{{t}}}}\\right)^2 \\ge 0')}, we have {m(f't + \\frac{{{b}}}{{t}} \\ge 2\\sqrt{{{b}}} = {2*rt}')}.",
                    f"Add back the constant {m(3)}: minimum value is {m(f'{2*rt} + 3 = {ans}')}, attained when {m(f't = {rt} \\implies x = {3+rt}')}.",
                ],
                f"Plug in \\( x = {3+rt} \\): \\( {3+rt} + \\frac{{{b}}}{{{rt}}} = {3+rt} + {rt} = {ans} \\)!",
            )
            s_ar = explain_ar(
                "نطابق المقام بطرح وإضافة \\( 3 \\): \\( x + \\frac{16}{x-3} = (x - 3) + \\frac{16}{x - 3} + 3 \\)!",
                [
                    f"نضع {m('t = x - 3 > 0')}، فيصبح المقدار {m(f't + \\frac{{{b}}}{{t}} + 3')}.",
                    f"من المتباينة {m(f'\\left(\\sqrt{{t}} - \\frac{{{rt}}}{{\\sqrt{{t}}}}\\right)^2 \\ge 0')} نجد {m(f't + \\frac{{{b}}}{{t}} \\ge 2\\sqrt{{{b}}} = {2*rt}')}.",
                    f"نضيف الثابت {m(3)}: القيمة الصغرى هي {m(f'{2*rt} + 3 = {ans}')} وتتحقق عند {m(f't = {rt} \\implies x = {3+rt}')}.",
                ],
                f"عوّض \\( x = {3+rt} \\) للتأكد: \\( {3+rt} + \\frac{{{b}}}{{{rt}}} = {ans} \\)!",
            )
        elif kind == "rect_prod":
            _, S, k, _ = item
            assert (S * S) % (4 * k) == 0
            ans = (S * S) // (4 * k)
            x_opt = Fraction(S, 2 * k)
            assert x_opt * (S - k * x_opt) == ans
            expr_tex = f"x({S} - x)" if k == 1 else f"x({S} - {k}x)"
            distractors = [ans * 2, (S * S) // (2 * k), ans - k, ans + S // 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_ext_{v_i}")
            q_en = (
                f"As {m('x')} varies over all real numbers, what is the **maximum possible value** of the product {m(expr_tex)}?"
            )
            q_ar = (
                f"عندما يتغير {m('x')} عبر جميع الأعداد الحقيقية، ما **أكبر قيمة ممكنة** لحاصل الضرب {m(expr_tex)}؟"
            )
            k_str = "" if k == 1 else str(k)
            h_en = f"Complete the square! Rewrite -{k_str}x² + {S}x as -{k_str}(x − {fmt_val(x_opt)})² + {ans}; since a square is never negative, the peak is {ans}!"
            h_ar = f"أكمل المربع! أعد كتابة المقدار بصورة {m(f'{ans} - {k_str}(x - {fmt_val(x_opt)})^2')}؛ وبما أن المربع لا يكون سالباً أبداً فإن القيمة العظمى هي {ans}!"
            s_en = explain_en(
                "**Completing the square** writes any downward-opening quadratic in the vertex form \\( M - k(x - h)^2 \\le M \\)!",
                [
                    f"Expand the product: {m(f'{expr_tex} = -{k_str}x^2 + {S}x')}.",
                    f"Complete the square around {m(f'x = {fmt_val(x_opt)}')}: {m(f'-{k_str}x^2 + {S}x = {ans} - {k_str}\\left(x - {fmt_val(x_opt)}\\right)^2')}.",
                    f"Since {m(f'\\left(x - {fmt_val(x_opt)}\\right)^2 \\ge 0')}, the expression is at most {m(ans)}, achieved at {m(f'x = {fmt_val(x_opt)}')}.",
                ],
                f"Test \\( x = {fmt_val(x_opt)} \\): \\( {fmt_val(x_opt)} \\times ({S} - {fmt_val(k * x_opt)}) = {ans} \\)!",
            )
            s_ar = explain_ar(
                "بإكمال المربع مباشرةً نكتب المقدار على الصورة \\( M - k(x - h)^2 \\le M \\) دون الحاجة لأي أدوات متقدمة!",
                [
                    f"نفك الأقواس: {m(f'{expr_tex} = -{k_str}x^2 + {S}x')}.",
                    f"نكمل المربع حول {m(f'x = {fmt_val(x_opt)}')}: {m(f'{ans} - {k_str}\\left(x - {fmt_val(x_opt)}\\right)^2')}.",
                    f"بما أن المربع الكامل {m('\\ge 0')} دائماً، فإن أكبر قيمة ممكنة هي {m(ans)} وتتحقق عند {m(f'x = {fmt_val(x_opt)}')}.",
                ],
                f"عوّض \\( x = {fmt_val(x_opt)} \\): \\( {fmt_val(x_opt)} \\times ({S} - {fmt_val(k * x_opt)}) = {ans} \\)!",
            )
        elif kind == "sum_sq":
            _, S, _ = item
            assert (S * S) % 2 == 0
            ans = (S * S) // 2
            half_s = S // 2
            assert half_s ** 2 + half_s ** 2 == ans
            distractors = [S * S, (S * S) // 4, ans + 2, ans - half_s]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_ext_{v_i}")
            q_en = (
                f"Two real numbers {m('x')} and {m('y')} satisfy {m(f'x + y = {S}')}. "
                f"What is the **minimum possible value** of {m('x^2 + y^2')}?"
            )
            q_ar = (
                f"عددان حقيقيان {m('x')} و{m('y')} يحققان {m(f'x + y = {S}')}. "
                f"ما **أصغر قيمة ممكنة** للمقدار {m('x^2 + y^2')}؟"
            )
            h_en = f"Use the symmetric identity x² + y² = ((x + y)² + (x − y)²) / 2! To minimize it, make (x − y)² equal to 0!"
            h_ar = f"استخدم المتطابقة الجميلة {m('x^2 + y^2 = \\frac{(x+y)^2 + (x-y)^2}{2}')}! لتصغير المقدار اجعل {m('(x-y)^2 = 0')}!"
            s_en = explain_en(
                "Use the identity \\( x^2 + y^2 = \\frac{(x + y)^2 + (x - y)^2}{2} \\): for a fixed sum \\( x + y \\), \\( x^2 + y^2 \\) is minimized when \\( x = y \\)!",
                [
                    f"Substitute {m(f'x + y = {S}')} into the identity: {m(f'x^2 + y^2 = \\frac{{{S}^2 + (x - y)^2}}{{2}} = {ans} + \\frac{{(x - y)^2}}{{2}}')}.",
                    f"Because {m('(x - y)^2 \\ge 0')} for all real numbers, {m(f'x^2 + y^2 \\ge {ans}')}.",
                    f"Equality holds when {m(f'x = y = {half_s}')}, giving {m(f'{half_s}^2 + {half_s}^2 = {ans}')}.",
                ],
                f"Nudge test: at \\( ({half_s+1}, {half_s-1}) \\), \\( x^2 + y^2 = {(half_s+1)**2 + (half_s-1)**2} > {ans} \\)!",
            )
            s_ar = explain_ar(
                "من المتطابقة \\( x^2 + y^2 = \\frac{(x + y)^2 + (x - y)^2}{2} \\)، عند ثبات المجموع \\( x + y \\) يبلغ مجموع المربعين أصغر قيمة له عندما \\( x = y \\)!",
                [
                    f"نعوّض {m(f'x + y = {S}')}: {m(f'x^2 + y^2 = \\frac{{{S}^2 + (x - y)^2}}{{2}} = {ans} + \\frac{{(x - y)^2}}{{2}}')}.",
                    f"بما أن {m('(x - y)^2 \\ge 0')} دائماً، فإن {m(f'x^2 + y^2 \\ge {ans}')}.",
                    f"تتحقق المساواة عندما {m(f'x = y = {half_s}')}، حيث {m(f'{half_s}^2 + {half_s}^2 = {ans}')}.",
                ],
                f"جرّب زوجاً مجاوراً مثل \\( ({half_s+1}, {half_s-1}) \\): المجموع \\( {(half_s+1)**2 + (half_s-1)**2} > {ans} \\)!",
            )
        else:
            # sum_sq_w: x + y = 15, min of x^2 + 2*y^2 = 150 at y = 5, x = 10
            _, S, _ = item
            assert S == 15
            ans = 150
            assert 10 ** 2 + 2 * (5 ** 2) == ans
            distractors = [225, 135, 165, 125]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_ext_{v_i}")
            q_en = (
                f"Real numbers {m('x')} and {m('y')} satisfy {m('x + y = 15')}. "
                f"What is the **minimum possible value** of {m('x^2 + 2y^2')}?"
            )
            q_ar = (
                f"عددان حقيقيان {m('x')} و{m('y')} يحققان {m('x + y = 15')}. "
                f"ما **أصغر قيمة ممكنة** للمقدار {m('x^2 + 2y^2')}؟"
            )
            h_en = "Substitute x = 15 − y into x² + 2y² and complete the square in y!"
            h_ar = "عوّض x = 15 − y في المقدار x² + 2y² ثم أكمل المربع بالنسبة للمتغير y!"
            s_en = explain_en(
                "Eliminate one variable using the linear constraint and complete the square!",
                [
                    f"Substitute {m('x = 15 - y')}: {m('(15 - y)^2 + 2y^2 = 225 - 30y + y^2 + 2y^2 = 3y^2 - 30y + 225')}.",
                    f"Factor out {m(3)} from the {m('y')}-terms and complete the square: {m('3(y^2 - 10y + 25) - 75 + 225 = 3(y - 5)^2 + 150')}.",
                    f"Since {m('3(y - 5)^2 \\ge 0')}, the minimum is {m(150)}, achieved when {m('y = 5')} and {m('x = 10')}.",
                ],
                f"Check at \\( (x, y) = (10, 5) \\): \\( 10 + 5 = 15 \\) and \\( 10^2 + 2(5^2) = 100 + 50 = 150 \\)!",
            )
            s_ar = explain_ar(
                "نعوّض أحد المتغيرين بدلالة الآخر من المعادلة الخطية ثم نكمل المربع!",
                [
                    f"نعوّض {m('x = 15 - y')}: {m('(15 - y)^2 + 2y^2 = 3y^2 - 30y + 225')}.",
                    f"نُخرج {m(3)} عاملاً مشتركاً ونكمل المربع: {m('3(y - 5)^2 + 150')}.",
                    f"بما أن {m('3(y - 5)^2 \\ge 0')}، فإن أصغر قيمة هي {m(150)} وتتحقق عند {m('y = 5')} و{m('x = 10')}.",
                ],
                f"تحقق عند \\( (10, 5) \\): \\( 10^2 + 2(5^2) = 100 + 50 = 150 \\)!",
            )
        push(topic, diff, "kmc_g1011_constrained_sum_prod_extremum", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)


def _gen_lesson_3_3(push) -> None:
    topic = "Algebra"

    # ------------------------------------------------------------------
    # 7. kmc_g1011_parabola_chord_vertex (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    par_cases = [
        # ("vy", r1, r2, a_lead, diff)
        # ("chord", b_lin, c_const, diff)  for y = x^2 - b_lin*x + c_const
        # ("area", r1, r2, a_lead, diff)
        ("vy", 1, 7, 1, "Easy"),
        ("vy", 2, 6, 1, "Easy"),
        ("chord", 8, 12, "Easy"),
        ("chord", 10, 9, "Easy"),
        ("area", 1, 5, 1, "Easy"),
        ("vy", -1, 5, 1, "Medium"),
        ("vy", -3, 7, 1, "Medium"),
        ("vy", 1, 9, 2, "Medium"),
        ("chord", 6, -16, "Medium"),
        ("chord", 12, 20, "Medium"),
        ("area", 2, 8, 1, "Medium"),
        ("area", -1, 7, 1, "Medium"),
        ("area", -2, 8, 1, "Medium"),
        ("chord_surd", 10, 13, "Hard"),   # D = 100 - 52 = 48 -> 4\sqrt{3}
        ("chord_surd", 6, 4, "Hard"),     # D = 36 - 16 = 20 -> 2\sqrt{5}
        ("area", 1, 7, 2, "Hard"),
        ("area", -3, 9, 1, "Hard"),
    ]
    def _poly_tex(a_c: int, b_c: int, c_c: int) -> str:
        s = "x^2" if a_c == 1 else f"{a_c}x^2"
        if b_c > 0:
            s += f" + {b_c}x" if b_c != 1 else " + x"
        elif b_c < 0:
            s += f" - {abs(b_c)}x" if abs(b_c) != 1 else " - x"
        if c_c > 0:
            s += f" + {c_c}"
        elif c_c < 0:
            s += f" - {abs(c_c)}"
        return s

    for v_i, item in enumerate(par_cases):
        kind = item[0]
        diff = item[-1]
        svg = svg_parabola_roots("r₁", "r₂", "V")
        if kind == "vy":
            _, r1, r2, a_l, _ = item
            b_c = -a_l * (r1 + r2)
            c_c = a_l * r1 * r2
            vx = (r1 + r2) // 2
            assert (r1 + r2) % 2 == 0
            vy = a_l * (vx - r1) * (vx - r2)
            assert a_l * vx * vx + b_c * vx + c_c == vy and vy < 0
            ans = vy
            distractors = [-vy, c_c, vx, vy - a_l, vy + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_par_{v_i}")
            ptex = _poly_tex(a_l, b_c, c_c)
            q_en = (
                f"The parabola {m(f'y = {ptex}')} crosses the {m('x')}-axis at two points and reaches its lowest vertex {m('V')}, as illustrated. "
                f"What is the **{m('y')}-coordinate** of the vertex {m('V')}?"
            )
            q_ar = (
                f"يقطع القطع المكافئ {m(f'y = {ptex}')} محور السينات في نقطتين ويبلغ أدنى رأس له عند {m('V')} كما في الشكل التوضيحي. "
                f"ما **الإحداثي الصادي ({m('y')})** للرأس {m('V')}؟"
            )
            h_en = f"Complete the square (or average the roots / use x_V = -b/(2a) = {vx}) and plug x = {vx} back into y!"
            h_ar = f"أكمل المربع (أو استخدم محور التماثل {m(f'x_V = -\\frac{{b}}{{2a}} = {vx}')}) ثم عوّض قيمة {m('x')} لإيجاد {m('y_V')}!"
            sq_tex = f"(x - {vx})^2" if vx >= 0 else f"(x + {abs(vx)})^2"
            if a_l > 1:
                sq_tex = f"{a_l}{sq_tex}"
            s_en = explain_en(
                "Complete the square \\( y = a(x - h)^2 + k \\): because \\( (x - h)^2 \\ge 0 \\), the vertex sits right at \\( V(h, k) \\)!",
                [
                    f"Find the axis of symmetry: {m(f'x_V = -\\frac{{{b_c}}}{{2({a_l})}} = {vx}')}.",
                    f"Complete the square (or substitute {m(f'x = {vx}')}): {m(f'y = {sq_tex} - {abs(vy)}')}.",
                    f"Read off the vertex {m(f'V({vx}, {vy})')}, so its {m('y')}-coordinate is {m(ans)}.",
                ],
                f"Don't confuse the {m('y')}-intercept {m(c_c)} (at {m('x = 0')}) with the vertex {m('y')}-coordinate {m(vy)} (at {m(f'x = {vx}')})!",
            )
            s_ar = explain_ar(
                "بإكمال المربع على الصورة \\( y = a(x - h)^2 + k \\)، وبما أن \\( (x - h)^2 \\ge 0 \\)، يقع رأس القطع عند \\( V(h, k) \\)!",
                [
                    f"نحدد محور التماثل: {m(f'x_V = -\\frac{{{b_c}}}{{2({a_l})}} = {vx}')}.",
                    f"نكمل المربع (أو نعوّض {m(f'x = {vx}')} في المعادلة): {m(f'y = {sq_tex} - {abs(vy)}')}.",
                    f"إذن إحداثيا الرأس هما {m(f'V({vx}, {vy})')}، والإحداثي الصادي هو {m(ans)}.",
                ],
                f"انتبه: المقطع الصادي عند {m('x = 0')} هو {m(c_c)}، أما أدنى قيمة عند الرأس فهي {m(vy)}!",
            )
        elif kind == "chord":
            _, b_lin, c_const, _ = item
            disc = b_lin * b_lin - 4 * c_const
            ans = math.isqrt(disc)
            assert ans * ans == disc
            r1 = (b_lin - ans) // 2
            r2 = (b_lin + ans) // 2
            assert r1 + r2 == b_lin and r1 * r2 == c_const and r2 - r1 == ans
            ptex = _poly_tex(1, -b_lin, c_const)
            distractors = [b_lin, ans // 2, ans + 2, abs(c_const) if abs(c_const) != ans else ans + 4]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_par_{v_i}")
            q_en = (
                f"The graph of the quadratic {m(f'y = {ptex}')} intersects the {m('x')}-axis at {m('r_1')} and {m('r_2')}, as shown. "
                f"What is the **distance** {m('|r_2 - r_1|')} between the two {m('x')}-intercepts?"
            )
            q_ar = (
                f"يقطع منحنى الدالة التربيعية {m(f'y = {ptex}')} محور السينات عند النقطتين {m('r_1')} و{m('r_2')} كما في الشكل. "
                f"ما **المسافة** {m('|r_2 - r_1|')} بين مقطعي محور السينات؟"
            )
            h_en = f"Set y = 0 to find the roots (or use (r₂ − r₁)² = (r₁ + r₂)² − 4r₁r₂ = {b_lin}² − 4({c_const}))!"
            h_ar = f"ضع y = 0 وحلّل لإيجاد الجذرين (أو استخدم المتطابقة {m(f'(r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2')})!"
            s_en = explain_en(
                "The \\( x \\)-intercepts are the roots of \\( y = 0 \\). You can either factor directly or use Vieta's identity \\( (r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \\)!",
                [
                    f"Set {m(f'{ptex} = 0')}. By Vieta's formulas, {m(f'r_1 + r_2 = {b_lin}')} and {m(f'r_1 r_2 = {c_const}')} (specifically, roots {m(r1)} and {m(r2)}).",
                    f"Compute {m(f'(r_2 - r_1)^2 = ({b_lin})^2 - 4({c_const}) = {b_lin*b_lin} - {4*c_const} = {disc}')}.",
                    f"Take the positive square root: {m(f'|r_2 - r_1| = \\sqrt{{{disc}}} = {ans}')}.",
                ],
                f"Direct subtraction check: \\( {r2} - ({r1}) = {ans} \\)!",
            )
            s_ar = explain_ar(
                "مقطعا محور السينات هما جذرا المعادلة \\( y = 0 \\)؛ يمكن إيجادهما بالتحليل المباشر أو بمتطابقة فييت \\( (r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \\)!",
                [
                    f"بوضع {m(f'{ptex} = 0')}، نجد من فييت {m(f'r_1 + r_2 = {b_lin}')} و{m(f'r_1 r_2 = {c_const}')} (أي الجذرين {m(r1)} و{m(r2)}).",
                    f"نحسب مربع الفرق: {m(f'(r_2 - r_1)^2 = ({b_lin})^2 - 4({c_const}) = {disc}')}.",
                    f"بأخذ الجذر التربيعي الموجب نجد الطول: {m(f'|r_2 - r_1| = \\sqrt{{{disc}}} = {ans}')}.",
                ],
                f"تحقق بالطرح المباشر: \\( {r2} - ({r1}) = {ans} \\)!",
            )
        elif kind == "chord_surd":
            _, b_lin, c_const, _ = item
            disc = b_lin * b_lin - 4 * c_const
            # Extract largest square factor
            k_out = 1
            for sq in range(2, 10):
                while disc % (sq * sq) == 0:
                    k_out *= sq
                    disc //= (sq * sq)
            orig_disc = b_lin * b_lin - 4 * c_const
            assert (k_out * k_out) * disc == orig_disc
            ans_tex = f"{k_out}\\sqrt{{{disc}}}"
            d_list = [f"{k_out // 2}\\sqrt{{{disc}}}" if k_out % 2 == 0 else f"{k_out + 1}\\sqrt{{{disc}}}", f"\\sqrt{{{orig_disc // 4}}}", str(b_lin), f"{2 * k_out}\\sqrt{{{disc}}}"]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3x_par_{v_i}")
            ptex = _poly_tex(1, -b_lin, c_const)
            q_en = (
                f"The parabola {m(f'y = {ptex}')} crosses the {m('x')}-axis at two points {m('r_1')} and {m('r_2')}, as shown. "
                f"What is the exact distance {m('|r_2 - r_1|')} between these two {m('x')}-intercepts?"
            )
            q_ar = (
                f"يقطع القطع المكافئ {m(f'y = {ptex}')} محور السينات في النقطتين {m('r_1')} و{m('r_2')} كما في الشكل. "
                f"ما المسافة الدقيقة {m('|r_2 - r_1|')} بين هاتين النقطتين؟"
            )
            h_en = f"Don't compute the two irrational roots separately! Use (r₂ − r₁)² = (r₁ + r₂)² − 4r₁r₂ = {b_lin}² − 4({c_const})!"
            h_ar = f"لا تحسب الجذرين كلّاً على حدة! استخدم المتطابقة المباشرة {m(f'(r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2')}!"
            s_en = explain_en(
                "Even when the roots are irrational, Vieta's identity \\( (r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \\) gives the chord length in one clean step!",
                [
                    f"From {m(f'{ptex} = 0')}, Vieta's formulas give {m(f'r_1 + r_2 = {b_lin}')} and {m(f'r_1 r_2 = {c_const}')}.",
                    f"Substitute into the difference-squared identity: {m(f'(r_2 - r_1)^2 = {b_lin}^2 - 4({c_const}) = {b_lin**2} - {4*c_const} = {orig_disc}')}.",
                    f"Simplify the square root: {m(f'|r_2 - r_1| = \\sqrt{{{orig_disc}}} = \\sqrt{{{k_out**2} \\times {disc}}} = {ans_tex}')}.",
                ],
                f"Notice \\( |r_2 - r_1| = \\frac{{\\sqrt{{\\Delta}}}}{{|a|}} \\) always for \\( ax^2 + bx + c = 0 \\)!",
            )
            s_ar = explain_ar(
                "حتى عندما تكون الجذور غير نسبية، تعطي متطابقة فييت \\( (r_2 - r_1)^2 = (r_1 + r_2)^2 - 4r_1 r_2 \\) مربع المسافة في خطوة واحدة!",
                [
                    f"من المعادلة {m(f'{ptex} = 0')}، نعلم من علاقات فييت أن {m(f'r_1 + r_2 = {b_lin}')} و{m(f'r_1 r_2 = {c_const}')}.",
                    f"نحسب مربع الفرق: {m(f'(r_2 - r_1)^2 = {b_lin}^2 - 4({c_const}) = {orig_disc}')}.",
                    f"نبسّط الجذر التربيعي: {m(f'|r_2 - r_1| = \\sqrt{{{orig_disc}}} = \\sqrt{{{k_out**2} \\times {disc}}} = {ans_tex}')}.",
                ],
                f"ملاحظة سريعة: المسافة بين الجذرين تساوي دائماً \\( \\frac{{\\sqrt{{\\Delta}}}}{{|a|}} \\)!",
            )
        else:
            # kind == "area": area of triangle formed by x-intercepts (r1,0), (r2,0) and vertex V(vx, vy)
            _, r1, r2, a_l, _ = item
            b_c = -a_l * (r1 + r2)
            c_c = a_l * r1 * r2
            vx = (r1 + r2) // 2
            vy = a_l * (vx - r1) * (vx - r2)
            base_len = r2 - r1
            height_len = abs(vy)
            assert (base_len * height_len) % 2 == 0
            ans = (base_len * height_len) // 2
            ptex = _poly_tex(a_l, b_c, c_c)
            distractors = [base_len * height_len, ans // 2 if ans % 2 == 0 else ans + base_len, base_len + height_len, height_len]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_par_{v_i}")
            q_en = (
                f"The parabola {m(f'y = {ptex}')} crosses the {m('x')}-axis at {m('r_1')} and {m('r_2')} and has vertex {m('V')}, as shown. "
                f"What is the **area of the triangle** whose vertices are {m('(r_1, 0)')}, {m('(r_2, 0)')}, and {m('V')}?"
            )
            q_ar = (
                f"يقطع القطع المكافئ {m(f'y = {ptex}')} محور السينات عند {m('r_1')} و{m('r_2')} وله الرأس {m('V')} كما في الشكل. "
                f"ما **مساحة المثلث** الذي رؤوسه النقاط الثلاث {m('(r_1, 0)')} و{m('(r_2, 0)')} و{m('V')}؟"
            )
            h_en = "Find the two x-intercepts for the horizontal base |r₂ − r₁|, then find the vertex's distance |y_V| from the x-axis for the height!"
            h_ar = "أوجد مقطعي محور السينات لحساب طول القاعدة الأفقية |r₂ − r₁|، ثم أوجد بُعد الرأس |y_V| عن محور السينات ليمثّل الارتفاع!"
            s_en = explain_en(
                "The segment between the \\( x \\)-intercepts lies right on the \\( x \\)-axis (base \\( = r_2 - r_1 \\)), and the perpendicular height is \\( |y_V| \\)!",
                [
                    f"Factor {m(f'{ptex} = 0')} to get the roots {m(f'r_1 = {r1}')} and {m(f'r_2 = {r2}')}, so the base is {m(f'{r2} - ({r1}) = {base_len}')}.",
                    f"The vertex lies midway at {m(f'x_V = \\frac{{{r1} + {r2}}}{{2}} = {vx}')}, where {m(f'y_V = {vy}')}, giving height {m(f'|y_V| = {height_len}')}.",
                    f"Compute triangle area: {m(f'\\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {base_len} \\times {height_len} = {ans}')}.",
                ],
                f"Don't forget the factor of \\( \\frac{{1}}{{2}} \\) in the triangle area formula (rectangle area would be {m(base_len * height_len)})!",
            )
            s_ar = explain_ar(
                "تقع قاعدة المثلث على محور السينات بطول \\( r_2 - r_1 \\)، وارتفاعه العمودي هو المسافة الرأسية للرأس \\( |y_V| \\)!",
                [
                    f"بوضع {m('y = 0')} والتحليل نجد الجذرين {m(f'r_1 = {r1}')} و{m(f'r_2 = {r2}')}، فطول القاعدة = {m(f'{r2} - ({r1}) = {base_len}')}.",
                    f"يقع الرأس في المنتصف عند {m(f'x_V = {vx}')}، وبالتعويض نجد {m(f'y_V = {vy}')}، فيكون الارتفاع {m(f'|y_V| = {height_len}')}.",
                    f"مساحة المثلث: {m(f'\\frac{{1}}{{2}} \\times {base_len} \\times {height_len} = {ans}')}.",
                ],
                f"تذكّر الضرب في \\( \\frac{{1}}{{2}} \\) عند حساب مساحة المثلث!",
            )
        push(topic, diff, "kmc_g1011_parabola_chord_vertex", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 8. kmc_g1011_exp_quadratic_substitution (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ZERO forbidden words (never mention log / ln)! Pure exponent laws!
    # ------------------------------------------------------------------
    expq_cases = [
        # ("one_pos", base, r_good, u_neg_abs, diff) -> (b^x - b^r)(b^x + q) = 0 -> unique real x = r
        # ("two_clean", base, r1, r2, ask, diff) -> (b^x - b^r1)(b^x - b^r2) = 0
        # ("vieta_prod", base, M_mid, m_exp, diff) -> b^(2x) - M*b^x + b^m = 0 -> x1 + x2 = m
        ("one_pos", 2, 3, 5, "Easy"),
        ("one_pos", 3, 2, 4, "Easy"),
        ("one_pos", 5, 2, 3, "Easy"),
        ("two_clean", 2, 1, 3, "sum", "Easy"),
        ("two_clean", 3, 0, 2, "sum", "Easy"),
        ("one_pos", 2, 4, 7, "Medium"),
        ("two_clean", 2, 1, 4, "sq_sum", "Medium"),
        ("two_clean", 3, 1, 3, "diff", "Medium"),
        ("two_clean", 5, 0, 3, "sq_sum", "Medium"),
        ("vieta_prod", 2, 7, 3, "Medium"),     # u^2 - 7u + 8 = 0 (D=17>0, u1*u2=8=2^3 => x1+x2=3)
        ("vieta_prod", 2, 10, 4, "Medium"),    # u^2 - 10u + 16 = 0 (u=2,8 => x1+x2=4)
        ("vieta_prod", 3, 13, 3, "Medium"),    # u^2 - 13u + 27 = 0 (D=61>0, u1*u2=27=3^3 => x1+x2=3)
        ("vieta_prod", 5, 12, 2, "Medium"),    # u^2 - 12u + 25 = 0 (D=44>0, u1*u2=25=5^2 => x1+x2=2)
        ("vieta_prod", 2, 13, 5, "Hard"),      # u^2 - 13u + 32 = 0 (D=41>0, u1*u2=32=2^5 => x1+x2=5)
        ("vieta_prod", 3, 20, 4, "Hard"),      # u^2 - 20u + 81 = 0 (D=76>0, u1*u2=81=3^4 => x1+x2=4)
        ("recip_exp", 2, 2, "Hard"),           # 2^x + 16 * 2^(-x) = 10 -> u = 2, 8 -> x1^2 + x2^2 = 10
        ("recip_exp", 3, 3, "Hard"),           # 3^x + 27 * 3^(-x) = 12 -> u = 3, 9 -> x1^2 + x2^2 = 5
    ]
    for v_i, item in enumerate(expq_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "one_pos":
            _, b, r_g, q_neg, _ = item
            u_pos = b ** r_g
            B_coef = u_pos - q_neg
            C_coef = u_pos * q_neg
            # u^2 - B_coef*u - C_coef = 0
            assert u_pos * u_pos - B_coef * u_pos - C_coef == 0
            ans = r_g
            b2 = b * b
            mid_s = f"- {B_coef} \\cdot {b}^x" if B_coef > 0 else (f"+ {abs(B_coef)} \\cdot {b}^x" if B_coef < 0 else "")
            eq_tex = f"{b2}^x {mid_s} - {C_coef} = 0"
            distractors = [u_pos, r_g + 1, max(0, r_g - 1), r_g + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_expq_{v_i}")
            q_en = (
                f"Find the real number {m('x')} that satisfies the exponential equation {m(eq_tex)}."
            )
            q_ar = (
                f"أوجد العدد الحقيقي {m('x')} الذي يحقق المعادلة الأسية {m(eq_tex)}."
            )
            h_en = f"Notice {b2}^x = ({b}²)^x = ({b}^x)²! Substitute u = {b}^x > 0, factor the quadratic in u, and reject any negative u!"
            h_ar = f"لاحظ أن {m(f'{b2}^x = ({b}^x)^2')}! ضع {m(f'u = {b}^x > 0')} وحلّل المعادلة التربيعية، ثم استبعد القيمة السالبة لـ {m('u')}!"
            s_en = explain_en(
                f"Rewrite \\( {b2}^x = ({b}^x)^2 \\) and substitute \\( u = {b}^x \\). Remember that \\( {b}^x > 0 \\) for **every** real number \\( x \\)!",
                [
                    f"Let {m(f'u = {b}^x')}, so {m(f'{b2}^x = u^2')}. The equation becomes {m(f'u^2 - {B_coef}u - {C_coef} = 0' if B_coef >= 0 else f'u^2 + {abs(B_coef)}u - {C_coef} = 0')}.",
                    f"Factor the quadratic: {m(f'(u - {u_pos})(u + {q_neg}) = 0')}, giving {m(f'u = {u_pos}')} or {m(f'u = -{q_neg}')}.",
                    f"Since {m(f'{b}^x > 0')} always, reject {m(f'u = -{q_neg}')}. From {m(f'{b}^x = {u_pos} = {b}^{{{r_g}}}')}, match exponents to get {m(f'x = {ans}')}.",
                ],
                f"Direct check: \\( {b2}^{{{ans}}} - ({B_coef})({b}^{{{ans}}}) - {C_coef} = {b2**ans} - {B_coef * (b**ans)} - {C_coef} = 0 \\)!",
            )
            s_ar = explain_ar(
                f"نكتب \\( {b2}^x = ({b}^x)^2 \\) ونعوض \\( u = {b}^x \\)، مع تذكّر أن القوة الأسية \\( {b}^x > 0 \\) دائماً لأي عدد حقيقي \\( x \\)!",
                [
                    f"بوضع {m(f'u = {b}^x')} تتحول المعادلة إلى {m(f'u^2 - {B_coef}u - {C_coef} = 0' if B_coef >= 0 else f'u^2 + {abs(B_coef)}u - {C_coef} = 0')}.",
                    f"نحلل إلى عاملين: {m(f'(u - {u_pos})(u + {q_neg}) = 0')}، ومنه {m(f'u = {u_pos}')} أو {m(f'u = -{q_neg}')}.",
                    f"نرفض {m(f'u = -{q_neg}')} لأن {m(f'{b}^x > 0')}. ومن {m(f'{b}^x = {u_pos} = {b}^{{{r_g}}}')} تتساوى الأسس فنجد {m(f'x = {ans}')}.",
                ],
                f"تحقق بالتعويض المباشر: \\( {b2}^{{{ans}}} - ({B_coef})({b}^{{{ans}}}) - {C_coef} = 0 \\)!",
            )
        elif kind == "two_clean":
            _, b, r1, r2, ask, _ = item
            u1, u2 = b ** r1, b ** r2
            S_u = u1 + u2
            P_u = u1 * u2
            b2 = b * b
            eq_tex = f"{b2}^x - {S_u} \\cdot {b}^x + {P_u} = 0"
            if ask == "sum":
                ans = r1 + r2
                ask_en = f"What is the **sum** {m('x_1 + x_2')} of its two real solutions?"
                ask_ar = f"ما **مجموع** الحلّين الحقيقيين {m('x_1 + x_2')}؟"
                last_en = f"Add the two solutions: {m(f'x_1 + x_2 = {r1} + {r2} = {ans}')}."
                last_ar = f"نجمع الحلّين: {m(f'x_1 + x_2 = {r1} + {r2} = {ans}')}."
            elif ask == "diff":
                ans = abs(r2 - r1)
                ask_en = f"What is the positive **difference** {m('|x_2 - x_1|')} between its two real solutions?"
                ask_ar = f"ما **الفرق الموجب** {m('|x_2 - x_1|')} بين حلّيها الحقيقيين؟"
                last_en = f"Subtract the solutions: {m(f'|{r2} - {r1}| = {ans}')}."
                last_ar = f"نطرح الحلّين: {m(f'|{r2} - {r1}| = {ans}')}."
            else:
                ans = r1 * r1 + r2 * r2
                ask_en = f"What is the value of {m('x_1^2 + x_2^2')} for its two real solutions {m('x_1, x_2')}?"
                ask_ar = f"ما قيمة {m('x_1^2 + x_2^2')} لحلّيها الحقيقيين {m('x_1, x_2')}؟"
                last_en = f"Square and add: {m(f'x_1^2 + x_2^2 = {r1}^2 + {r2}^2 = {ans}')}."
                last_ar = f"نربّع ونجمع: {m(f'x_1^2 + x_2^2 = {r1}^2 + {r2}^2 = {ans}')}."
            distractors = [S_u, u1 * u1 + u2 * u2 if ask == "sq_sum" else P_u, ans + 1, max(1, ans - 1), ans + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_expq_{v_i}")
            q_en = f"Consider the exponential equation {m(eq_tex)}. {ask_en}"
            q_ar = f"في المعادلة الأسية {m(eq_tex)}، {ask_ar}"
            h_en = f"Substitute u = {b}^x to get u² − {S_u}u + {P_u} = 0, find u₁ and u₂, then convert back using {b}^x = u (remember {b}⁰ = 1)!"
            h_ar = f"ضع {m(f'u = {b}^x')} لتحصل على {m(f'u^2 - {S_u}u + {P_u} = 0')}، ثم أوجد {m('x')} من مقارنة الأسس (وتذكّر أن {m(f'{b}^0 = 1')})!"
            s_en = explain_en(
                f"Turn \\( {b2}^x = ({b}^x)^2 \\) into a quadratic in \\( u = {b}^x \\), solve for \\( u \\), then match powers of \\( {b} \\)!",
                [
                    f"Set {m(f'u = {b}^x')}: {m(f'u^2 - {S_u}u + {P_u} = (u - {u1})(u - {u2}) = 0')}.",
                    f"Recover {m('x')} from {m(f'{b}^{{x_1}} = {u1} = {b}^{{{r1}}}')} and {m(f'{b}^{{x_2}} = {u2} = {b}^{{{r2}}}')}, so {m(f'x_1 = {r1}')} and {m(f'x_2 = {r2}')}.",
                    last_en,
                ],
                f"Trap check: \\( u_1 = {u1} \\) and \\( u_2 = {u2} \\) are values of \\( {b}^x \\), NOT values of \\( x \\) itself!",
            )
            s_ar = explain_ar(
                f"نحوّل \\( {b2}^x = ({b}^x)^2 \\) إلى معادلة تربيعية في \\( u = {b}^x \\)، نوجد قيمتي \\( u \\)، ثم نقارن أسس العدد \\( {b} \\)!",
                [
                    f"بوضع {m(f'u = {b}^x')} نحصل على {m(f'u^2 - {S_u}u + {P_u} = (u - {u1})(u - {u2}) = 0')}.",
                    f"نسترجع قيمتي {m('x')} من {m(f'{b}^{{x_1}} = {u1} = {b}^{{{r1}}}')} و{m(f'{b}^{{x_2}} = {u2} = {b}^{{{r2}}}')}، أي {m(f'x_1 = {r1}')} و{m(f'x_2 = {r2}')}.",
                    last_ar,
                ],
                f"انتبه للفخ الشائع: القيمتان {m(u1)} و{m(u2)} هما قيمتا {m(f'{b}^x')} وليستا قيمتي {m('x')} مباشرةً!",
            )
        elif kind == "vieta_prod":
            _, b, M_mid, m_exp, _ = item
            P_const = b ** m_exp
            assert M_mid * M_mid - 4 * P_const > 0
            ans = m_exp
            b2 = b * b
            eq_tex = f"{b2}^x - {M_mid} \\cdot {b}^x + {P_const} = 0"
            distractors = [M_mid, P_const, m_exp + 1, max(1, m_exp - 1), m_exp * 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_expq_{v_i}")
            q_en = (
                f"Let {m('x_1')} and {m('x_2')} be the two real solutions of {m(eq_tex)}. "
                f"What is the exact value of the sum {m('x_1 + x_2')}?"
            )
            q_ar = (
                f"ليكن {m('x_1')} و{m('x_2')} الحلّين الحقيقيين للمعادلة {m(eq_tex)}. "
                f"ما القيمة الدقيقة للمجموع {m('x_1 + x_2')}؟"
            )
            h_en = f"Set u = {b}^x! You don't need to find x₁ and x₂ separately: multiply u₁ · u₂ = {b}^(x₁) · {b}^(x₂) = {b}^(x₁ + x₂) using Vieta's product formula!"
            h_ar = f"ضع {m(f'u = {b}^x')}! لا تحتاج لإيجاد كل جذر بمفرده: استخدم حاصل ضرب الجذرين في فييت لأن {m(f'u_1 u_2 = {b}^{{x_1}} \\cdot {b}^{{x_2}} = {b}^{{x_1 + x_2}}')}!"
            s_en = explain_en(
                f"To add exponents \\( x_1 + x_2 \\), **multiply** the powers \\( u_1 u_2 = {b}^{{x_1}} \\cdot {b}^{{x_2}} = {b}^{{x_1 + x_2}} \\) via Vieta's product rule!",
                [
                    f"Let {m(f'u = {b}^x')}, turning the equation into {m(f'u^2 - {M_mid}u + {P_const} = 0')}.",
                    f"Check that two positive roots {m('u_1, u_2 > 0')} exist: {m(f'\\Delta = {M_mid}^2 - 4({P_const}) = {M_mid**2 - 4*P_const} > 0')}, sum {m(f'{M_mid} > 0')}, and product {m(f'u_1 u_2 = {P_const} > 0')}.",
                    f"Since {m(f'u_1 u_2 = {b}^{{x_1}} \\cdot {b}^{{x_2}} = {b}^{{x_1 + x_2}} = {P_const} = {b}^{{{m_exp}}}')}, matching exponents gives {m(f'x_1 + x_2 = {ans}')}!",
                ],
                f"Zero messy radicals needed: Vieta's product \\( {P_const} = {b}^{{{m_exp}}} \\) hands us \\( x_1 + x_2 = {ans} \\) immediately!",
            )
            s_ar = explain_ar(
                f"لإيجاد مجموع الأسس \\( x_1 + x_2 \\)، **نضرب** القوتين \\( u_1 u_2 = {b}^{{x_1}} \\cdot {b}^{{x_2}} = {b}^{{x_1 + x_2}} \\) باستخدام قانون ضرب الجذرين في فييت!",
                [
                    f"بوضع {m(f'u = {b}^x')} تصبح المعادلة {m(f'u^2 - {M_mid}u + {P_const} = 0')}.",
                    f"نتأكد من وجود جذرين حقيقيين موجبين لـ {m('u')}: {m(f'\\Delta = {M_mid}^2 - 4({P_const}) = {M_mid**2 - 4*P_const} > 0')}، والمجموع {m(f'{M_mid} > 0')}، والضرب {m(f'{P_const} > 0')}.",
                    f"بما أن {m(f'u_1 u_2 = {b}^{{x_1 + x_2}} = {P_const} = {b}^{{{m_exp}}}')}، فإن مساواة الأسس تعطي {m(f'x_1 + x_2 = {ans}')} فوراً!",
                ],
                f"جمال الجبر: لم نحتج لحساب {m('x_1')} و{m('x_2')} منفردين إطلاقاً!",
            )
        else:
            # kind == "recip_exp":
            # (2, 2) -> 2^x + 16 * 2^(-x) = 10 -> u = 2, 8 -> x = 1, 3 -> x1^2 + x2^2 = 10
            # (3, 3) -> 3^x + 27 * 3^(-x) = 12 -> u = 3, 9 -> x = 1, 2 -> x1^2 + x2^2 = 5
            _, b, tag, _ = item
            if b == 2:
                r1, r2 = 1, 3
            else:
                r1, r2 = 1, 2
            u1, u2 = b ** r1, b ** r2
            P_c = u1 * u2
            S_c = u1 + u2
            ans = r1 * r1 + r2 * r2
            eq_tex = f"{b}^x + {P_c} \\cdot {b}^{{-x}} = {S_c}"
            distractors = [r1 + r2, S_c + 2, u1 * u1 + u2 * u2, ans + 2, max(1, ans - 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_expq_{v_i}")
            q_en = (
                f"If {m('x_1')} and {m('x_2')} are the two real solutions of {m(eq_tex)}, what is the value of {m('x_1^2 + x_2^2')}?"
            )
            q_ar = (
                f"إذا كان {m('x_1')} و{m('x_2')} هما الحلّين الحقيقيين للمعادلة {m(eq_tex)}، فما قيمة {m('x_1^2 + x_2^2')}؟"
            )
            h_en = f"Use {b}⁻ˣ = 1/{b}ˣ! Multiply both sides by u = {b}ˣ to clear the fraction and factor the resulting quadratic!"
            h_ar = f"استخدم {m(f'{b}^{{-x}} = \\frac{{1}}{{{b}^x}}')}! اضرب الطرفين في {m(f'u = {b}^x')} للتخلص من المقام ثم حلّل المعادلة التربيعية!"
            s_en = explain_en(
                f"Replace \\( {b}^{{-x}} \\) with \\( \\frac{{1}}{{{b}^x}} \\) and multiply through by \\( u = {b}^x > 0 \\)!",
                [
                    f"Set {m(f'u = {b}^x')}: {m(f'u + \\frac{{{P_c}}}{{u}} = {S_c} \\implies u^2 - {S_c}u + {P_c} = 0')}.",
                    f"Factor: {m(f'(u - {u1})(u - {u2}) = 0')}, so {m(f'{b}^x = {u1} = {b}^{{{r1}}}')} or {m(f'{b}^x = {u2} = {b}^{{{r2}}}')}, giving {m(f'x_1 = {r1},\\; x_2 = {r2}')}.",
                    f"Compute {m(f'x_1^2 + x_2^2 = {r1}^2 + {r2}^2 = {ans}')}.",
                ],
                f"Verify both roots: \\( {b}^{{{r1}}} + {P_c}\\cdot{b}^{{-{r1}}} = {u1} + {u2} = {S_c} \\) and \\( {b}^{{{r2}}} + {P_c}\\cdot{b}^{{-{r2}}} = {u2} + {u1} = {S_c} \\)!",
            )
            s_ar = explain_ar(
                f"نكتب \\( {b}^{{-x}} = \\frac{{1}}{{{b}^x}} \\) ثم نضرب المعادلة في \\( u = {b}^x > 0 \\)!",
                [
                    f"بوضع {m(f'u = {b}^x')} نجد: {m(f'u + \\frac{{{P_c}}}{{u}} = {S_c} \\implies u^2 - {S_c}u + {P_c} = 0')}.",
                    f"نحلل: {m(f'(u - {u1})(u - {u2}) = 0')}، ومنه {m(f'{b}^x = {b}^{{{r1}}}')} أو {m(f'{b}^x = {b}^{{{r2}}}')}، أي {m(f'x_1 = {r1}')} و{m(f'x_2 = {r2}')}.",
                    f"نحسب المطلوب: {m(f'x_1^2 + x_2^2 = {r1}^2 + {r2}^2 = {ans}')}.",
                ],
                f"تحقق بالتعويض: كلا العددين {m(r1)} و{m(r2)} يحققان المعادلة الأصلية تماماً!",
            )
        push(topic, diff, "kmc_g1011_exp_quadratic_substitution", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 9. kmc_g1011_reciprocal_cube_power (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # ------------------------------------------------------------------
    rec_cases = [
        # (mode, k_val, c_num, diff)
        ("sum3", 2, 1, "Easy"),
        ("sum3", 3, 1, "Easy"),
        ("sum3", 4, 1, "Easy"),
        ("diff3", 1, 1, "Easy"),
        ("diff3", 2, 1, "Easy"),
        ("sum3", 5, 1, "Medium"),
        ("sum3", 6, 1, "Medium"),
        ("diff3", 3, 1, "Medium"),
        ("diff3", 4, 1, "Medium"),
        ("sum4", 3, 1, "Medium"),
        ("diff4", 2, 1, "Medium"),
        ("quad_sum3", 5, 1, "Medium"),
        ("sum4", 4, 1, "Hard"),
        ("diff4", 3, 1, "Hard"),
        ("quad_diff3", 4, 1, "Hard"),
        ("weighted3", 5, 2, "Hard"),      # x + 2/x = 5 -> x^3 + 8/x^3 = 125 - 30 = 95
    ]
    for v_i, (mode, k_v, c_n, diff) in enumerate(rec_cases):
        if mode == "sum3":
            assert k_v >= 2
            ans = k_v ** 3 - 3 * k_v
            x_num = (k_v + math.sqrt(k_v * k_v - 4)) / 2
            assert math.isclose(x_num ** 3 + 1 / (x_num ** 3), ans, rel_tol=1e-9)
            distractors = [k_v ** 3, k_v ** 3 + 3 * k_v, k_v ** 3 - 3, k_v ** 2 - 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rec_{v_i}")
            q_en = f"If {m('x')} is a nonzero real number satisfying {m(f'x + \\frac{{1}}{{x}} = {k_v}')}, what is the value of {m('x^3 + \\frac{1}{x^3}')}?"
            q_ar = f"إذا كان {m('x')} عدداً حقيقياً غير صفري يحقق {m(f'x + \\frac{{1}}{{x}} = {k_v}')}، فما قيمة {m('x^3 + \\frac{1}{x^3}')}؟"
            h_en = f"Cube both sides of x + 1/x = {k_v}: (x + 1/x)³ = x³ + 1/x³ + 3(x + 1/x)!"
            h_ar = f"كعّب طرفي المعادلة: {m('(x + \\frac{1}{x})^3 = x^3 + \\frac{1}{x^3} + 3(x + \\frac{1}{x})')}!"
            s_en = explain_en(
                "Cubing \\( \\left(x + \\frac{1}{x}\\right)^3 = x^3 + 3x^2\\left(\\frac{1}{x}\\right) + 3x\\left(\\frac{1}{x^2}\\right) + \\frac{1}{x^3} \\) collapses the middle terms into \\( 3\\left(x + \\frac{1}{x}\\right) \\)!",
                [
                    f"Use the cube identity: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}.",
                    f"Substitute {m(f'x + \\frac{{1}}{{x}} = {k_v}')}: {m(f'{k_v}^3 = x^3 + \\frac{{1}}{{x^3}} + 3({k_v})')}.",
                    f"Subtract {m(3 * k_v)} from {m(k_v ** 3)}: {m(f'x^3 + \\frac{{1}}{{x^3}} = {k_v**3} - {3*k_v} = {ans}')}.",
                ],
                f"Sign check: \\( + \\) inside \\( (x + 1/x) \\) produces \\( k^3 - 3k \\) when isolating \\( x^3 + 1/x^3 \\)!",
            )
            s_ar = explain_ar(
                "عند فكّ المكعب \\( \\left(x + \\frac{1}{x}\\right)^3 \\)، تجتمع الحدود الوسطى في \\( 3\\left(x + \\frac{1}{x}\\right) \\) لأن \\( x \\cdot \\frac{1}{x} = 1 \\)!",
                [
                    f"نكتب المتطابقة التكعيبية: {m('\\left(x + \\frac{1}{x}\\right)^3 = x^3 + \\frac{1}{x^3} + 3\\left(x + \\frac{1}{x}\\right)')}.",
                    f"نعوّض {m(f'x + \\frac{{1}}{{x}} = {k_v}')}: {m(f'{k_v}^3 = x^3 + \\frac{{1}}{{x^3}} + 3({k_v})')}.",
                    f"نطرح {m(3 * k_v)} من الطرفين: {m(f'x^3 + \\frac{{1}}{{x^3}} = {k_v**3} - {3*k_v} = {ans}')}.",
                ],
                f"تذكّر الإشارة: الجمع يعطي \\( k^3 - 3k = {ans} \\) بعد النقل للطرف الآخر!",
            )
        elif mode == "diff3":
            ans = k_v ** 3 + 3 * k_v
            x_num = (k_v + math.sqrt(k_v * k_v + 4)) / 2
            assert math.isclose(x_num ** 3 - 1 / (x_num ** 3), ans, rel_tol=1e-9)
            distractors = [k_v ** 3 - 3 * k_v, k_v ** 3, k_v ** 3 + 3, ans + k_v]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rec_{v_i}")
            q_en = f"Given a nonzero real number {m('x')} such that {m(f'x - \\frac{{1}}{{x}} = {k_v}')}, what is the exact value of {m('x^3 - \\frac{1}{x^3}')}?"
            q_ar = f"إذا كان {m('x')} عدداً حقيقياً غير صفري يحقق {m(f'x - \\frac{{1}}{{x}} = {k_v}')}، فما القيمة الدقيقة للمقدار {m('x^3 - \\frac{1}{x^3}')}؟"
            h_en = f"Cube (x − 1/x)³ = x³ − 1/x³ − 3(x − 1/x); watch the MINUS sign so you ADD 3({k_v}) to {k_v}³!"
            h_ar = f"كعّب الطرفين: {m('(x - \\frac{1}{x})^3 = x^3 - \\frac{1}{x^3} - 3(x - \\frac{1}{x})')}؛ انتبه للإشارة السالبة، لذا ستجمع {m(f'3({k_v})')}!"
            s_en = explain_en(
                "Expand \\( \\left(x - \\frac{1}{x}\\right)^3 = x^3 - \\frac{1}{x^3} - 3\\left(x - \\frac{1}{x}\\right) \\) carefully — moving \\( -3\\left(x - \\frac{1}{x}\\right) \\) across the equals sign turns it into \\( +3k \\)!",
                [
                    f"Start from {m('\\left(x - \\frac{1}{x}\\right)^3 = x^3 - \\frac{1}{x^3} - 3\\left(x - \\frac{1}{x}\\right)')}.",
                    f"Plug in {m(f'x - \\frac{{1}}{{x}} = {k_v}')}: {m(f'{k_v}^3 = x^3 - \\frac{{1}}{{x^3}} - 3({k_v})')}.",
                    f"Add {m(3 * k_v)} to both sides: {m(f'x^3 - \\frac{{1}}{{x^3}} = {k_v**3} + {3*k_v} = {ans}')}.",
                ],
                f"Sign trap defeated: \\( k^3 + 3k = {ans} \\), NOT \\( k^3 - 3k = {k_v**3 - 3*k_v} \\)!",
            )
            s_ar = explain_ar(
                "عند فكّ مكعب الفرق \\( \\left(x - \\frac{1}{x}\\right)^3 = x^3 - \\frac{1}{x^3} - 3\\left(x - \\frac{1}{x}\\right) \\)، نقل الحد السالب للطرف الآخر يحوّله إلى **جمع** \\( +3k \\)!",
                [
                    f"نكتب المتطابقة: {m('\\left(x - \\frac{1}{x}\\right)^3 = x^3 - \\frac{1}{x^3} - 3\\left(x - \\frac{1}{x}\\right)')}.",
                    f"نعوّض {m(f'x - \\frac{{1}}{{x}} = {k_v}')}: {m(f'{k_v}^3 = x^3 - \\frac{{1}}{{x^3}} - {3*k_v}')}.",
                    f"نضيف {m(3 * k_v)} للطرفين: {m(f'x^3 - \\frac{{1}}{{x^3}} = {k_v**3} + {3*k_v} = {ans}')}.",
                ],
                f"تجنّب فخ الإشارة: الناتج هو {m(ans)} وليس {m(k_v**3 - 3*k_v)}!",
            )
        elif mode in ("sum4", "diff4"):
            is_sum = (mode == "sum4")
            sq2 = k_v * k_v - 2 if is_sum else k_v * k_v + 2
            ans = sq2 * sq2 - 2
            x_num = (k_v + math.sqrt(k_v * k_v - 4 if is_sum else k_v * k_v + 4)) / 2
            assert math.isclose(x_num ** 4 + 1 / (x_num ** 4), ans, rel_tol=1e-9)
            op_s = "+" if is_sum else "-"
            distractors = [sq2 * sq2, sq2 * sq2 + 2, k_v ** 4 - 4, k_v ** 4 - 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rec_{v_i}")
            q_en = f"If {m('x')} is a nonzero real number with {m(f'x {op_s} \\frac{{1}}{{x}} = {k_v}')}, what is the value of {m('x^4 + \\frac{1}{x^4}')}?"
            q_ar = f"إذا كان {m('x')} عدداً حقيقياً غير صفري يحقق {m(f'x {op_s} \\frac{{1}}{{x}} = {k_v}')}، فما قيمة {m('x^4 + \\frac{1}{x^4}')}؟"
            h_en = f"Square TWICE in two calm steps: first find x² + 1/x², then square x² + 1/x² and subtract 2!"
            h_ar = f"ربّع على خطوتين متتاليتين: أوجد أولاً {m('x^2 + \\frac{1}{x^2}')}، ثم ربّع الناتج واطرح 2!"
            step1_sign = f"{k_v}^2 - 2" if is_sum else f"{k_v}^2 + 2"
            s_en = explain_en(
                "Reach the 4th power by **squaring twice**: \\( x \\pm \\frac{1}{x} \\xrightarrow{\\text{square}} x^2 + \\frac{1}{x^2} \\xrightarrow{\\text{square}} x^4 + \\frac{1}{x^4} \\)!",
                [
                    f"First squaring: {m(f'\\left(x {op_s} \\frac{{1}}{{x}}\\right)^2 = x^2 {op_s} 2 + \\frac{{1}}{{x^2}} \\implies x^2 + \\frac{{1}}{{x^2}} = {step1_sign} = {sq2}')}.",
                    f"Second squaring: {m(f'\\left(x^2 + \\frac{{1}}{{x^2}}\\right)^2 = x^4 + 2 + \\frac{{1}}{{x^4}} = {sq2}^2 = {sq2*sq2}')}.",
                    f"Subtract {m(2)} from the second square: {m(f'x^4 + \\frac{{1}}{{x^4}} = {sq2*sq2} - 2 = {ans}')}.",
                ],
                f"Notice the second step ALWAYS subtracts \\( 2 \\) because \\( x^2 + \\frac{{1}}{{x^2}} \\) has a \\( + \\) sign!",
            )
            s_ar = explain_ar(
                "نصل إلى القوة الرابعة عبر **التربيع مرتين**: نحسب \\( x^2 + \\frac{1}{x^2} \\) أولاً، ثم نربعه للحصول على \\( x^4 + \\frac{1}{x^4} \\)!",
                [
                    f"التربيع الأول: {m(f'x^2 + \\frac{{1}}{{x^2}} = {step1_sign} = {sq2}')}.",
                    f"التربيع الثاني: {m(f'\\left(x^2 + \\frac{{1}}{{x^2}}\\right)^2 = x^4 + 2 + \\frac{{1}}{{x^4}} = {sq2}^2 = {sq2*sq2}')}.",
                    f"نطرح {m(2)}: {m(f'x^4 + \\frac{{1}}{{x^4}} = {sq2*sq2} - 2 = {ans}')}.",
                ],
                f"انتبه: في الخطوة الثانية نطرح \\( 2 \\) دائماً لأن الإشارة بين \\( x^2 \\) و\\( \\frac{{1}}{{x^2}} \\) موجبة!",
            )
        elif mode in ("quad_sum3", "quad_diff3"):
            is_sum = (mode == "quad_sum3")
            ans = k_v ** 3 - 3 * k_v if is_sum else k_v ** 3 + 3 * k_v
            c_sign = "+ 1" if is_sum else "- 1"
            t_sign = "+" if is_sum else "-"
            distractors = [k_v ** 3, k_v ** 3 + 3 * k_v if is_sum else k_v ** 3 - 3 * k_v, ans + k_v, ans - 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rec_{v_i}")
            q_en = f"A real number {m('x')} satisfies {m(f'x^2 - {k_v}x {c_sign} = 0')}. What is the value of {m(f'x^3 {t_sign} \\frac{{1}}{{x^3}}')}?"
            q_ar = f"يحقق العدد الحقيقي {m('x')} المعادلة {m(f'x^2 - {k_v}x {c_sign} = 0')}. ما قيمة المقدار {m(f'x^3 {t_sign} \\frac{{1}}{{x^3}}')}؟"
            h_en = f"Since x = 0 does not satisfy the quadratic, divide the entire equation by x to uncover x {t_sign} 1/x = {k_v}!"
            h_ar = f"بما أن x = 0 لا يحقق المعادلة، اقسم جميع حدود المعادلة على x لتحصل فوراً على {m(f'x {t_sign} \\frac{{1}}{{x}} = {k_v}')}!"
            s_en = explain_en(
                f"Never use the quadratic formula here! Dividing \\( x^2 - {k_v}x {c_sign} = 0 \\) by \\( x \\neq 0 \\) immediately reveals \\( x {t_sign} \\frac{{1}}{{x}} = {k_v} \\)!",
                [
                    f"Check {m('x \\neq 0')} (plugging {m('x = 0')} gives {m('1 = 0' if is_sum else '-1 = 0')}, impossible), then divide by {m('x')}: {m(f'x - {k_v} {t_sign} \\frac{{1}}{{x}} = 0 \\implies x {t_sign} \\frac{{1}}{{x}} = {k_v}')}.",
                    f"Cube both sides: {m(f'\\left(x {t_sign} \\frac{{1}}{{x}}\\right)^3 = x^3 {t_sign} \\frac{{1}}{{x^3}} {t_sign} 3\\left(x {t_sign} \\frac{{1}}{{x}}\\right)')}.",
                    f"Solve: {m(f'x^3 {t_sign} \\frac{{1}}{{x^3}} = {k_v}^3 ' + (f'- 3({k_v})' if is_sum else f'+ 3({k_v})') + f' = {ans}')}.",
                ],
                f"Dividing by \\( x \\) turns a disguised quadratic into a standard reciprocal identity!",
            )
            s_ar = explain_ar(
                f"لا تستخدم القانون العام للجذور! قسمة المعادلة على \\( x \\neq 0 \\) تكشف فوراً أن \\( x {t_sign} \\frac{{1}}{{x}} = {k_v} \\)!",
                [
                    f"نتأكد أن {m('x \\neq 0')} ثم نقسم المعادلة على {m('x')}: {m(f'x {t_sign} \\frac{{1}}{{x}} = {k_v}')}.",
                    f"نكعّب الطرفين: {m(f'\\left(x {t_sign} \\frac{{1}}{{x}}\\right)^3 = x^3 {t_sign} \\frac{{1}}{{x^3}} {t_sign} 3\\left(x {t_sign} \\frac{{1}}{{x}}\\right)')}.",
                    f"نحسب الناتج: {m(f'x^3 {t_sign} \\frac{{1}}{{x^3}} = {k_v}^3 ' + (f'- 3({k_v})' if is_sum else f'+ 3({k_v})') + f' = {ans}')}.",
                ],
                f"القسمة على \\( x \\) هي المفتاح الذهبي كلما ظهر \\( x^2 \\) مع الحد الثابت \\( \\pm 1 \\)!",
            )
        else:
            # weighted3: x + 2/x = 5 -> x^3 + 8/x^3 = 5^3 - 3(2)(5) = 95
            ans = k_v ** 3 - 3 * c_n * k_v
            x_num = (k_v + math.sqrt(k_v * k_v - 4 * c_n)) / 2
            assert math.isclose(x_num ** 3 + (c_n ** 3) / (x_num ** 3), ans, rel_tol=1e-9)
            distractors = [k_v ** 3 - 3 * k_v, k_v ** 3 + 3 * c_n * k_v, k_v ** 3, ans - 5]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rec_{v_i}")
            q_en = f"If {m('x')} is a nonzero real number satisfying {m(f'x + \\frac{{{c_n}}}{{x}} = {k_v}')}, what is the value of {m(f'x^3 + \\frac{{{c_n**3}}}{{x^3}}')}?"
            q_ar = f"إذا كان {m('x')} عدداً حقيقياً غير صفري يحقق {m(f'x + \\frac{{{c_n}}}{{x}} = {k_v}')}، فما قيمة {m(f'x^3 + \\frac{{{c_n**3}}}{{x^3}}')}؟"
            h_en = f"Use (a + b)³ = a³ + b³ + 3ab(a + b) with a = x and b = {c_n}/x — notice a·b = {c_n} (not 1)!"
            h_ar = f"استخدم {m('(a+b)^3 = a^3 + b^3 + 3ab(a+b)')} مع {m('a = x')} و{m(f'b = \\frac{{{c_n}}}{{x}}')} — وانتبه أن {m(f'ab = {c_n}')} وليس 1!"
            s_en = explain_en(
                f"Apply \\( (a + b)^3 = a^3 + b^3 + 3ab(a + b) \\) with \\( a = x \\) and \\( b = \\frac{{{c_n}}}{{x}} \\), keeping track of \\( ab = {c_n} \\)!",
                [
                    f"Set {m('a = x')} and {m(f'b = \\frac{{{c_n}}}{{x}}')}; then {m(f'a + b = {k_v}')} and {m(f'ab = x \\cdot \\frac{{{c_n}}}{{x}} = {c_n}')}.",
                    f"Cube the sum: {m(f'{k_v}^3 = x^3 + \\frac{{{c_n**3}}}{{x^3}} + 3({c_n})({k_v})')}.",
                    f"Subtract {m(f'3({c_n})({k_v}) = {3*c_n*k_v}')}: {m(f'x^3 + \\frac{{{c_n**3}}}{{x^3}} = {k_v**3} - {3*c_n*k_v} = {ans}')}.",
                ],
                f"Trap check: forgetting the factor \\( ab = {c_n} \\) would give \\( {k_v**3 - 3*k_v} \\) instead of the true value \\( {ans} \\)!",
            )
            s_ar = explain_ar(
                f"نطبّق المتطابقة \\( (a + b)^3 = a^3 + b^3 + 3ab(a + b) \\) مع \\( a = x \\) و\\( b = \\frac{{{c_n}}}{{x}} \\)، مع الانتباه لأن \\( ab = {c_n} \\)!",
                [
                    f"لدينا {m(f'a + b = {k_v}')} وحاصل الضرب {m(f'ab = x \\cdot \\frac{{{c_n}}}{{x}} = {c_n}')}.",
                    f"بتكعيب المجموع: {m(f'{k_v}^3 = x^3 + \\frac{{{c_n**3}}}{{x^3}} + 3({c_n})({k_v})')}.",
                    f"بطرح {m(3*c_n*k_v)}: {m(f'x^3 + \\frac{{{c_n**3}}}{{x^3}} = {k_v**3} - {3*c_n*k_v} = {ans}')}.",
                ],
                f"تجنّب الفخ: لا تنسَ الضرب في \\( ab = {c_n} \\) (فالناتج {m(ans)} وليس {m(k_v**3 - 3*k_v)})!",
            )
        push(topic, diff, "kmc_g1011_reciprocal_cube_power", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)


def _gen_lesson_3_4(push) -> None:
    topic = "Algebra"

    # ------------------------------------------------------------------
    # 10. kmc_g1011_functional_involution_system (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ZERO forbidden words (never write "matrix", "matrices", "determinant")!
    # ------------------------------------------------------------------
    func_cases = [
        # ("comp", a, b, S, m_sl, c_con, x0, diff) -> a*f(x) + b*f(S - x) = m_sl*x + c_con
        # ("recip", a, b, c_x, d_inv, x0, diff) -> a*f(x) + b*f(1/x) = c_x*x + d_inv/x
        ("comp", 2, 1, 6, 3, 0, 2, "Easy"),
        ("comp", 2, 1, 8, 3, 2, 5, "Easy"),
        ("comp", 3, 1, 10, 4, 0, 7, "Easy"),
        ("recip", 2, 1, 3, 0, 2, "Easy"),
        ("recip", 2, 1, 6, 0, 3, "Easy"),
        ("comp", 3, -1, 7, 2, 4, 5, "Medium"),
        ("comp", 3, 2, 10, 5, -5, 8, "Medium"),
        ("comp", 4, -1, 6, 3, 6, 4, "Medium"),
        ("comp", 2, 3, 9, 5, 0, 6, "Medium"),
        ("recip", 3, 1, 8, 0, 2, "Medium"),
        ("recip", 2, -1, 3, 6, 2, "Medium"),
        ("recip", 3, -1, 8, 4, 2, "Medium"),
        ("recip", 3, 2, 5, 10, 5, "Medium"),
        ("comp", 5, -2, 12, 7, -14, 9, "Hard"),
        ("comp", 4, 3, 11, 7, 14, 8, "Hard"),
        ("recip", 4, -1, 15, 30, 3, "Hard"),
        ("recip", 5, 2, 21, 42, 6, "Hard"),
    ]
    for v_i, item in enumerate(func_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "comp":
            _, a, b, S, m_sl, c_con, x0, _ = item
            assert a * a != b * b and x0 != S - x0
            x1 = S - x0
            rhs0 = m_sl * x0 + c_con
            rhs1 = m_sl * x1 + c_con
            # Exact solution of a*U + b*V = rhs0 and b*U + a*V = rhs1:
            # (a^2 - b^2)*U = a*rhs0 - b*rhs1
            ans = Fraction(a * rhs0 - b * rhs1, a * a - b * b)
            v_val = Fraction(a * rhs1 - b * rhs0, a * a - b * b)
            assert a * ans + b * v_val == rhs0 and b * ans + a * v_val == rhs1
            b_part = f"+ {b}f({S} - x)" if b > 1 else (f"+ f({S} - x)" if b == 1 else (f"- f({S} - x)" if b == -1 else f"- {abs(b)}f({S} - x)"))
            rhs_tex = f"{m_sl}x" + (f" + {c_con}" if c_con > 0 else (f" - {abs(c_con)}" if c_con < 0 else ""))
            eq_tex = f"{a}f(x) {b_part} = {rhs_tex}"
            distractors = [v_val, Fraction(rhs0, a + b), ans + 1, ans - 1, Fraction(rhs0, a)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_fnc_{v_i}")
            q_en = (
                f"A function {m('f')} defined on all real numbers satisfies {m(eq_tex)} for every real {m('x')}. "
                f"What is the exact value of {m(f'f({x0})')}?"
            )
            q_ar = (
                f"تحقق الدالة {m('f')} المعرّفة على جميع الأعداد الحقيقية المعادلة {m(eq_tex)} لكل عدد حقيقي {m('x')}. "
                f"ما القيمة الدقيقة لـ {m(f'f({x0})')}؟"
            )
            h_en = f"Plug in x = {x0} AND its partner x = {S} − {x0} = {x1}! That gives two linear equations in the two unknowns f({x0}) and f({x1})!"
            h_ar = f"عوّض {m(f'x = {x0}')} ثم عوّض قرينها {m(f'x = {S} - {x0} = {x1}')}! ستحصل على معادلتين خطيتين بمجهولين هما {m(f'f({x0})')} و{m(f'f({x1})')}!"
            s_en = explain_en(
                f"Because \\( x \\mapsto {S} - x \\) swaps \\( {x0} \\) and \\( {x1} \\) back and forth, substituting both values creates two linear equations we can solve by elimination!",
                [
                    f"Substitute {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f({x1}) = {rhs0}')}.",
                    f"Substitute {m(f'x = {x1}')}: {m(f'{a}f({x1}) + ({b})f({x0}) = {rhs1}')}.",
                    f"Eliminate {m(f'f({x1})')} (multiply the first equation by {m(a)} and subtract {m(b)} times the second): {m(f'({a*a - b*b})f({x0}) = {a*rhs0 - b*rhs1} \\implies f({x0}) = {fmt_val(ans)}')}.",
                ],
                f"Check both equations with \\( f({x0}) = {fmt_val(ans)} \\) and \\( f({x1}) = {fmt_val(v_val)} \\): \\( {a}({fmt_val(ans)}) + ({b})({fmt_val(v_val)}) = {rhs0} \\)!",
            )
            s_ar = explain_ar(
                f"بما أن التعويض بـ \\( {S} - x \\) يبدّل بين \\( {x0} \\) و\\( {x1} \\)، فإن تعويض القيمتين يعطينا معادلتين خطيتين نحلهما بطريقة الحذف!",
                [
                    f"نعوّض {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f({x1}) = {rhs0}')}.",
                    f"نعوّض {m(f'x = {x1}')}: {m(f'{b}f({x0}) + {a}f({x1}) = {rhs1}')}.",
                    f"نحذف {m(f'f({x1})')} بضرب المعادلة الأولى في {m(a)} وطرح {m(b)} في الثانية: {m(f'({a*a - b*b})f({x0}) = {a*rhs0 - b*rhs1} \\implies f({x0}) = {fmt_val(ans)}')}.",
                ],
                f"تحقق بالتعويض بـ \\( f({x0}) = {fmt_val(ans)} \\) و\\( f({x1}) = {fmt_val(v_val)} \\) في المعادلة الأولى: الناتج \\( {rhs0} \\) تماماً!",
            )
        else:
            _, a, b, c_x, d_inv, x0, _ = item
            assert a * a != b * b and x0 >= 2
            rhs0 = Fraction(c_x * x0, 1) + Fraction(d_inv, x0)
            rhs1 = Fraction(c_x, x0) + Fraction(d_inv * x0, 1)
            ans = (a * rhs0 - b * rhs1) / (a * a - b * b)
            v_val = (a * rhs1 - b * rhs0) / (a * a - b * b)
            assert a * ans + b * v_val == rhs0 and b * ans + a * v_val == rhs1
            b_part = f"+ {b}f(1/x)" if b > 1 else (f"+ f(1/x)" if b == 1 else (f"- f(1/x)" if b == -1 else f"- {abs(b)}f(1/x)"))
            rhs_tex = f"{c_x}x" + (f" + \\frac{{{d_inv}}}{{x}}" if d_inv > 0 else "")
            eq_tex = f"{a}f(x) {b_part} = {rhs_tex}"
            distractors = [v_val, rhs0 / (a + b), ans + 1, ans - 1, rhs0 / a]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_fnc_{v_i}")
            q_en = (
                f"Suppose {m('f')} is a function defined for all nonzero real numbers {m('x \\neq 0')} such that "
                f"{m(eq_tex)}. What is the value of {m(f'f({x0})')}?"
            )
            q_ar = (
                f"لتكن {m('f')} دالة معرّفة لجميع الأعداد الحقيقية غير الصفرية {m('x \\neq 0')} بحيث تحقق "
                f"{m(eq_tex)}. ما قيمة {m(f'f({x0})')}؟"
            )
            h_en = f"Substitute x = {x0} AND its reciprocal x = 1/{x0}, then eliminate f(1/{x0}) between the two equations!"
            h_ar = f"عوّض {m(f'x = {x0}')} ثم عوّض مقلوبها {m(f'x = \\frac{{1}}{{{x0}}}')}، واحذف {m(f'f(1/{x0})')} بين المعادلتين!"
            s_en = explain_en(
                f"Replacing \\( x \\) by \\( 1/x \\) swaps \\( f({x0}) \\) and \\( f(1/{x0}) \\), closing a two-equation loop!",
                [
                    f"Plug in {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f(1/{x0}) = {fmt_val(rhs0)}')}.",
                    f"Plug in {m(f'x = 1/{x0}')}: {m(f'{b}f({x0}) + {a}f(1/{x0}) = {fmt_val(rhs1)}')}.",
                    f"Multiply the first equation by {m(a)} and subtract {m(b)} times the second to eliminate {m(f'f(1/{x0})')}: {m(f'({a*a - b*b})f({x0}) = {fmt_val(a*rhs0 - b*rhs1)} \\implies f({x0}) = {fmt_val(ans)}')}.",
                ],
                f"Verify: \\( {a}({fmt_val(ans)}) + ({b})({fmt_val(v_val)}) = {fmt_val(rhs0)} \\) matches the right-hand side at \\( x = {x0} \\)!",
            )
            s_ar = explain_ar(
                f"التعويض بـ \\( 1/x \\) يبدّل بين \\( f({x0}) \\) و\\( f(1/{x0}) \\)، فنحصل على معادلتين خطيتين مغلقتين نحلهما بالحذف!",
                [
                    f"نعوّض {m(f'x = {x0}')}: {m(f'{a}f({x0}) + ({b})f(1/{x0}) = {fmt_val(rhs0)}')}.",
                    f"نعوّض {m(f'x = 1/{x0}')}: {m(f'{b}f({x0}) + {a}f(1/{x0}) = {fmt_val(rhs1)}')}.",
                    f"نحذف {m(f'f(1/{x0})')} بضرب الأولى في {m(a)} وطرح {m(b)} في الثانية: {m(f'({a*a - b*b})f({x0}) = {fmt_val(a*rhs0 - b*rhs1)} \\implies f({x0}) = {fmt_val(ans)}')}.",
                ],
                f"تحقق: \\( {a}({fmt_val(ans)}) + ({b})({fmt_val(v_val)}) = {fmt_val(rhs0)} \\)!",
            )
        push(topic, diff, "kmc_g1011_functional_involution_system", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 11. kmc_g1011_manhattan_diamond_area (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    dia_cases = [
        # ("std_area", R, diff)
        # ("std_perim", R, diff)
        # ("shift_area", R, h, k, diff)
        # ("scaled_area", a, b, c, diff)
        # ("scaled_perim", a, b, c, diff)
        # ("ring_area", r_in, r_out, diff)
        ("std_area", 3, "Easy"),
        ("std_area", 5, "Easy"),
        ("std_area", 7, "Easy"),
        ("std_perim", 4, "Easy"),
        ("std_perim", 6, "Easy"),
        ("std_area", 9, "Medium"),
        ("std_perim", 10, "Medium"),
        ("shift_area", 4, 3, -2, "Medium"),
        ("shift_area", 6, -5, 4, "Medium"),
        ("shift_area", 8, 7, 1, "Medium"),
        ("scaled_area", 2, 3, 12, "Medium"),
        ("scaled_area", 3, 4, 24, "Medium"),
        ("scaled_area", 2, 5, 20, "Medium"),
        ("scaled_area", 4, 5, 40, "Hard"),
        ("scaled_perim", 4, 3, 12, "Hard"),
        ("scaled_perim", 12, 5, 60, "Hard"),
        ("ring_area", 4, 9, "Hard"),
    ]
    for v_i, item in enumerate(dia_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "std_area":
            _, R, _ = item
            svg = svg_coord_diamond(str(R))
            ans = 2 * R * R
            distractors = [R * R, 4 * R * R, 4 * R, ans + 2 * R]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_dia_{v_i}")
            q_en = (
                f"In the coordinate plane, what is the **area** of the diamond-shaped region defined by the inequality "
                f"{m(f'|x| + |y| \\le {R}')}, shown in the figure?"
            )
            q_ar = (
                f"في المستوى الإحداثي، ما **مساحة** المنطقة المعيّنية المحددة بالمتباينة "
                f"{m(f'|x| + |y| \\le {R}')} والموضحة في الشكل؟"
            )
            h_en = f"The vertices are (±{R}, 0) and (0, ±{R})! Use the rhombus area formula ½ × d₁ × d₂ with both diagonals equal to {2*R}!"
            h_ar = f"رؤوس المنطقة هي {m(f'(\\pm {R}, 0)')} و{m(f'(0, \\pm {R})')}! استخدم قانون مساحة المعين {m('\\frac{1}{2} d_1 d_2')} حيث طول كل قطر {2*R}!"
            s_en = explain_en(
                "The boundary \\( |x| + |y| = R \\) connects the four intercepts \\( (\\pm R, 0) \\) and \\( (0, \\pm R) \\), forming a tilted square (rhombus) with diagonals \\( 2R \\) and \\( 2R \\)!",
                [
                    f"Find the intercepts on both axes: {m(f'(\\pm {R}, 0)')} and {m(f'(0, \\pm {R})')}.",
                    f"Horizontal diagonal {m(f'd_1 = 2({R}) = {2*R}')} and vertical diagonal {m(f'd_2 = 2({R}) = {2*R}')}.",
                    f"Area of the rhombus: {m(f'\\frac{{1}}{{2}} d_1 d_2 = \\frac{{1}}{{2}}({2*R})({2*R}) = 2({R}^2) = {ans}')}.",
                ],
                f"Alternative check: 4 congruent right triangles in the 4 quadrants, each of area \\( \\frac{{1}}{{2}}({R})({R}) \\), total \\( 4 \\times \\frac{{{R*R}}}{{2}} = {ans} \\)!",
            )
            s_ar = explain_ar(
                "الحدود \\( |x| + |y| = R \\) تصل بين المقاطع الأربعة \\( (\\pm R, 0) \\) و\\( (0, \\pm R) \\) مكوّنةً مربعاً مائلاً (معيناً) طول كل من قطريه \\( 2R \\)!",
                [
                    f"نحدد نقاط التقاطع مع المحورين: {m(f'(\\pm {R}, 0)')} و{m(f'(0, \\pm {R})')}.",
                    f"طول القطر الأفقي {m(f'd_1 = {2*R}')} وطول القطر الرأسي {m(f'd_2 = {2*R}')}.",
                    f"مساحة المعين: {m(f'\\frac{{1}}{{2}} d_1 d_2 = \\frac{{1}}{{2}}({2*R})({2*R}) = 2({R}^2) = {ans}')}.",
                ],
                f"تحقق بديل: الشكل يتكون من 4 مثلثات قائمة في الأرباع الأربعة، مجموع مساحاتها \\( 4 \\times \\frac{{1}}{{2}}({R})({R}) = {ans} \\)!",
            )
        elif kind == "std_perim":
            _, R, _ = item
            svg = svg_coord_diamond(str(R))
            ans_tex = f"{4 * R}\\sqrt{{2}}"
            d_list = [f"{2 * R}\\sqrt{{2}}", f"{R}\\sqrt{{2}}", str(4 * R), str(8 * R)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3x_dia_{v_i}")
            q_en = (
                f"What is the **perimeter** (total boundary length) of the coordinate region {m(f'|x| + |y| \\le {R}')} shown in the figure?"
            )
            q_ar = (
                f"ما **محيط** (طول الحدود الخارجية) المنطقة الإحداثية {m(f'|x| + |y| \\le {R}')} الموضحة في الشكل؟"
            )
            h_en = f"In the first quadrant, the boundary connects ({R}, 0) to (0, {R}), which is the hypotenuse of an isosceles right triangle with legs {R} and {R}!"
            h_ar = f"في الربع الأول يصل الضلع بين {m(f'({R}, 0)')} و{m(f'(0, {R})')}، وهو وتر مثلث قائم متطابق الضلعين طول كل من ساقيه {R}!"
            s_en = explain_en(
                "Each of the 4 sides of \\( |x| + |y| = R \\) is the hypotenuse of a right triangle with legs \\( R \\) and \\( R \\)!",
                [
                    f"In Quadrant I ({m('x, y \\ge 0')}), segment {m('x + y = ' + str(R))} connects {m(f'({R}, 0)')} to {m(f'(0, {R})')}.",
                    f"By the Pythagorean theorem, one side has length {m(f'\\sqrt{{{R}^2 + {R}^2}} = {R}\\sqrt{{2}}')}.",
                    f"Multiply by {m(4)} equal sides: perimeter {m(f'= 4 \\times {R}\\sqrt{{2}} = {ans_tex}')}.",
                ],
                f"Approximation check: \\( {4*R}\\sqrt{{2}} \\approx {4*R*1.414:.1f} \\), strictly between \\( 4R = {4*R} \\) and \\( 8R = {8*R} \\).",
            )
            s_ar = explain_ar(
                "كل ضلع من الأضلاع الأربعة للمنحنى \\( |x| + |y| = R \\) هو وتر لمثلث قائم طول ساقيه \\( R \\) و\\( R \\)!",
                [
                    f"في الربع الأول، تصل القطعة {m(f'x + y = {R}')} بين النقطتين {m(f'({R}, 0)')} و{m(f'(0, {R})')}.",
                    f"من نظرية فيثاغورس، طول الضلع الواحد يساوي {m(f'\\sqrt{{{R}^2 + {R}^2}} = {R}\\sqrt{{2}}')}.",
                    f"نضرب في {m(4)} أضلاع متطابقة: المحيط {m(f'= 4 \\times {R}\\sqrt{{2}} = {ans_tex}')}.",
                ],
                f"تحقق منطقي: طول الوتر \\( {R}\\sqrt{{2}} \\) أكبر من الضلع \\( {R} \\) وأصغر من مجموع الساقين \\( {2*R} \\).",
            )
        elif kind == "shift_area":
            _, R, h_c, k_c, _ = item
            svg = svg_coord_diamond(str(R))
            ans = 2 * R * R
            x_term = f"|x - {h_c}|" if h_c > 0 else f"|x + {abs(h_c)}|"
            y_term = f"|y - {k_c}|" if k_c > 0 else f"|y + {abs(k_c)}|"
            distractors = [R * R, 4 * R * R, ans + abs(h_c * k_c), 2 * (R + abs(h_c)) ** 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_dia_{v_i}")
            q_en = (
                f"What is the **area** of the region in the coordinate plane satisfying {m(f'{x_term} + {y_term} \\le {R}')} "
                f"(a translated copy of the centered diamond {m(f'|u| + |v| \\le {R}')} shown)?"
            )
            q_ar = (
                f"ما **مساحة** المنطقة في المستوى الإحداثي التي تحقق المتباينة {m(f'{x_term} + {y_term} \\le {R}')} "
                f"(وهي إزاحة للمنطقة المعيّنية القياسية {m(f'|u| + |v| \\le {R}')} الموضحة في الشكل)؟"
            )
            h_en = f"Set u = x − ({h_c}) and v = y − ({k_c}): shifting a figure's center to ({h_c}, {k_c}) NEVER changes its area! Area = 2R²!"
            h_ar = f"ضع {m(f'u = x - ({h_c})')} و{m(f'v = y - ({k_c})')}: إزاحة الشكل في المستوى لا تغيّر مساحته إطلاقاً! المساحة تظل {m('2R^2')}!"
            s_en = explain_en(
                "Translation invariance: shifting \\( (x, y) \\) by \\( (h, k) \\) moves the diamond's center to \\( (h, k) \\) while leaving its side lengths and **area** completely unchanged!",
                [
                    f"Let {m(f'u = x - ({h_c})')} and {m(f'v = y - ({k_c})')}; the inequality becomes {m(f'|u| + |v| \\le {R}')}.",
                    f"This centered diamond has diagonals {m(f'2({R}) = {2*R}')} and {m(f'2({R}) = {2*R}')}.",
                    f"Its area is {m(f'\\frac{{1}}{{2}}({2*R})({2*R}) = 2({R}^2) = {ans}')}.",
                ],
                f"Notice \\( h = {h_c} \\) and \\( k = {k_c} \\) have **zero** effect on the area!",
            )
            s_ar = explain_ar(
                "ثبات المساحة تحت الانسحاب: إزاحة المركز إلى \\( (h, k) \\) تنقل المعين في المستوى دون أن تغيّر أبعاده أو **مساحته** على الإطلاق!",
                [
                    f"نضع {m(f'u = x - ({h_c})')} و{m(f'v = y - ({k_c})')}، فتتحول المتباينة إلى {m(f'|u| + |v| \\le {R}')}.",
                    f"طولا قطري هذا المعين هما {m(2*R)} و{m(2*R)}.",
                    f"إذن المساحة تساوي {m(f'\\frac{{1}}{{2}}({2*R})({2*R}) = 2({R}^2) = {ans}')}.",
                ],
                f"العددان \\( {h_c} \\) و\\( {k_c} \\) يحددان موقع المركز فقط ولا يدخلان في حساب المساحة!",
            )
        elif kind == "scaled_area":
            _, a, b, c, _ = item
            assert c % a == 0 and c % b == 0
            rx, ry = c // a, c // b
            svg = svg_coord_diamond("r")
            ans = 2 * rx * ry
            assert ans == (2 * c * c) // (a * b)
            distractors = [rx * ry, 4 * rx * ry, c * c // (a * b), ans + rx]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_dia_{v_i}")
            q_en = (
                f"In the coordinate plane, the inequality {m(f'{a}|x| + {b}|y| \\le {c}')} bounds a rhombus symmetric about both axes "
                f"(similar in symmetry to the diamond schematic shown). What is the **area** of this rhombus?"
            )
            q_ar = (
                f"في المستوى الإحداثي، تحدد المتباينة {m(f'{a}|x| + {b}|y| \\le {c}')} معيناً متماثلاً حول المحورين الإحداثيين "
                f"(على غرار الشكل التوضيحي). ما **مساحة** هذا المعين؟"
            )
            h_en = f"Find the x-intercepts (±{rx}, 0) by setting y = 0, and the y-intercepts (0, ±{ry}) by setting x = 0, then use Area = ½ × d₁ × d₂!"
            h_ar = f"أوجد مقطعي محور السينات بوضع y = 0 ({m(f'\\pm {rx}')}) ومقطعي محور الصادات بوضع x = 0 ({m(f'\\pm {ry}')})، ثم طبّق قانون مساحة المعين!"
            s_en = explain_en(
                "For \\( a|x| + b|y| \\le c \\), just find the intercepts on the two axes — the full diagonals are \\( d_1 = 2(c/a) \\) and \\( d_2 = 2(c/b) \\)!",
                [
                    f"Set {m('y = 0')}: {m(f'{a}|x| \\le {c} \\implies |x| \\le {rx}')}, so horizontal diagonal {m(f'd_1 = 2({rx}) = {2*rx}')}.",
                    f"Set {m('x = 0')}: {m(f'{b}|y| \\le {c} \\implies |y| \\le {ry}')}, so vertical diagonal {m(f'd_2 = 2({ry}) = {2*ry}')}.",
                    f"Rhombus area: {m(f'\\frac{{1}}{{2}} d_1 d_2 = \\frac{{1}}{{2}}({2*rx})({2*ry}) = {ans}')}.",
                ],
                f"Formula shortcut: \\( \\text{{Area}} = \\frac{{2c^2}}{{ab}} = \\frac{{2({c}^2)}}{{{a} \\times {b}}} = {ans} \\)!",
            )
            s_ar = explain_ar(
                "لإيجاد مساحة \\( a|x| + b|y| \\le c \\)، نحدد نقاط التقاطع مع المحورين فيكون طولا القطرين \\( d_1 = 2(c/a) \\) و\\( d_2 = 2(c/b) \\)!",
                [
                    f"نضع {m('y = 0')}: {m(f'{a}|x| \\le {c} \\implies |x| \\le {rx}')}، فيكون القطر الأفقي {m(f'd_1 = {2*rx}')}.",
                    f"نضع {m('x = 0')}: {m(f'{b}|y| \\le {c} \\implies |y| \\le {ry}')}، فيكون القطر الرأسي {m(f'd_2 = {2*ry}')}.",
                    f"مساحة المعين: {m(f'\\frac{{1}}{{2}} d_1 d_2 = \\frac{{1}}{{2}}({2*rx})({2*ry}) = {ans}')}.",
                ],
                f"قاعدة سريعة للتأكد: \\( \\frac{{2c^2}}{{ab}} = \\frac{{2({c}^2)}}{{{a} \\times {b}}} = {ans} \\)!",
            )
        elif kind == "scaled_perim":
            _, a, b, c, _ = item
            rx, ry = c // a, c // b
            side = math.isqrt(rx * rx + ry * ry)
            assert side * side == rx * rx + ry * ry
            ans = 4 * side
            svg = svg_coord_diamond("r")
            distractors = [2 * (rx + ry), 4 * (rx + ry), 2 * rx * ry, 2 * side]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_dia_{v_i}")
            q_en = (
                f"What is the **perimeter** of the rhombus in the coordinate plane bounded by {m(f'{a}|x| + {b}|y| = {c}')}?"
            )
            q_ar = (
                f"ما **محيط** المعين المحدد في المستوى الإحداثي بالمعادلة {m(f'{a}|x| + {b}|y| = {c}')}؟"
            )
            h_en = f"Find the Quadrant I intercepts ({rx}, 0) and (0, {ry}), compute one side with the Pythagorean theorem √({rx}² + {ry}²), and multiply by 4!"
            h_ar = f"أوجد نقطتي التقاطع في الربع الأول {m(f'({rx}, 0)')} و{m(f'(0, {ry})')}، واحسب طول الضلع الواحد من فيثاغورس ثم اضرب في 4!"
            s_en = explain_en(
                "The axes cut the rhombus \\( a|x| + b|y| = c \\) into 4 congruent right triangles with legs \\( c/a \\) and \\( c/b \\)!",
                [
                    f"Intercepts in Quadrant I are {m(f'({rx}, 0)')} and {m(f'(0, {ry})')}.",
                    f"By the Pythagorean theorem, each side of the rhombus has length {m(f'\\sqrt{{{rx}^2 + {ry}^2}} = \\sqrt{{{rx*rx + ry*ry}}} = {side}')}.",
                    f"Multiply by {m(4)} congruent sides: perimeter {m(f'= 4 \\times {side} = {ans}')}.",
                ],
                f"Recognize the classic Pythagorean triple \\( ({rx}, {ry}, {side}) \\)!",
            )
            s_ar = explain_ar(
                "يقسم المحوران المعين \\( a|x| + b|y| = c \\) إلى 4 مثلثات قائمة متطابقة ساقا كل منها \\( c/a \\) و\\( c/b \\)!",
                [
                    f"نقطتا التقاطع في الربع الأول هما {m(f'({rx}, 0)')} و{m(f'(0, {ry})')}.",
                    f"من فيثاغورس، طول الضلع الواحد للمعين = {m(f'\\sqrt{{{rx}^2 + {ry}^2}} = {side}')}.",
                    f"نضرب في {m(4)} أضلاع متطابقة: المحيط {m(f'= 4 \\times {side} = {ans}')}.",
                ],
                f"لاحظ الثلاثية الفيثاغورسية الشهيرة \\( ({rx}, {ry}, {side}) \\)!",
            )
        else:
            _, r_in, r_out, _ = item
            svg = svg_coord_diamond(str(r_out))
            ans = 2 * (r_out * r_out - r_in * r_in)
            distractors = [r_out * r_out - r_in * r_in, 2 * (r_out - r_in) ** 2, 2 * r_out * r_out, 4 * (r_out * r_out - r_in * r_in)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_dia_{v_i}")
            q_en = (
                f"What is the **area** of the diamond-shaped frame of points {m('(x, y)')} satisfying the double inequality "
                f"{m(f'{r_in} \\le |x| + |y| \\le {r_out}')}?"
            )
            q_ar = (
                f"ما **مساحة** الإطار المعيّني المكوّن من النقاط {m('(x, y)')} التي تحقق المتباينة المزدوجة "
                f"{m(f'{r_in} \\le |x| + |y| \\le {r_out}')}؟"
            )
            h_en = f"Subtract the inner diamond's area (2 × {r_in}²) from the outer diamond's area (2 × {r_out}²)!"
            h_ar = f"اطرح مساحة المعين الداخلي {m(f'2 \\times {r_in}^2')} من مساحة المعين الخارجي {m(f'2 \\times {r_out}^2')}!"
            s_en = explain_en(
                "The region \\( r_1 \\le |x| + |y| \\le r_2 \\) is an outer diamond of area \\( 2r_2^2 \\) with an inner diamond of area \\( 2r_1^2 \\) removed!",
                [
                    f"Outer diamond {m(f'|x| + |y| \\le {r_out}')} has area {m(f'2({r_out}^2) = {2*r_out*r_out}')}.",
                    f"Inner diamond {m(f'|x| + |y| < {r_in}')} has area {m(f'2({r_in}^2) = {2*r_in*r_in}')}.",
                    f"Subtract to get the frame area: {m(f'{2*r_out*r_out} - {2*r_in*r_in} = {ans}')}.",
                ],
                f"Never do \\( 2({r_out} - {r_in})^2 = {2*(r_out-r_in)**2} \\): subtract the **areas** \\( 2(r_2^2 - r_1^2) \\), not the radii before squaring!",
            )
            s_ar = explain_ar(
                "المنطقة \\( r_1 \\le |x| + |y| \\le r_2 \\) هي المعين الخارجي مطروحاً منه المعين الداخلي!",
                [
                    f"مساحة المعين الخارجي {m(f'|x| + |y| \\le {r_out}')} تساوي {m(f'2({r_out}^2) = {2*r_out*r_out}')}.",
                    f"مساحة المعين الداخلي {m(f'|x| + |y| < {r_in}')} تساوي {m(f'2({r_in}^2) = {2*r_in*r_in}')}.",
                    f"نطرح المساحتين: {m(f'{2*r_out*r_out} - {2*r_in*r_in} = {ans}')}.",
                ],
                f"انتبه: نطرح المربعات \\( 2({r_out}^2 - {r_in}^2) \\) وليس مربع الفرق \\( 2({r_out} - {r_in})^2 \\)!",
            )
        push(topic, diff, "kmc_g1011_manhattan_diamond_area", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 12. kmc_g1011_nested_radical_denest (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # ------------------------------------------------------------------
    rad_cases = [
        # ("diff_cancel", u, m_sq, diff) where v = m_sq^2 < u: sqrt((u+v)+2sqrt(uv)) - sqrt((u+v)-2sqrt(uv)) = 2*m_sq
        # ("sum_cancel", m_sq, v, diff) where u = m_sq^2 > v: sqrt((u+v)+2sqrt(uv)) + sqrt((u+v)-2sqrt(uv)) = 2*m_sq
        # ("one_sub", m_sq, v, diff) where u = m_sq^2: sqrt((u+v)+2sqrt(uv)) - sqrt(v) = m_sq
        # ("hidden_2", m_sq, v, diff) where u = m_sq^2: sqrt((u+v)+sqrt(4uv)) - sqrt(v) = m_sq
        ("one_sub", 2, 3, "Easy"),        # sqrt(7 + 2*sqrt(12)) - sqrt(3) = 2
        ("one_sub", 3, 2, "Easy"),        # sqrt(11 + 2*sqrt(18)) - sqrt(2) = 3
        ("one_sub", 3, 5, "Easy"),        # sqrt(14 + 2*sqrt(45)) - sqrt(5) = 3
        ("diff_cancel", 3, 1, "Easy"),    # sqrt(4 + 2*sqrt(3)) - sqrt(4 - 2*sqrt(3)) = 2
        ("diff_cancel", 5, 1, "Easy"),    # sqrt(6 + 2*sqrt(5)) - sqrt(6 - 2*sqrt(5)) = 2
        ("diff_cancel", 5, 2, "Medium"),  # u=5, v=4: sqrt(9 + 2*sqrt(20)) - sqrt(9 - 2*sqrt(20)) = 4
        ("diff_cancel", 6, 2, "Medium"),  # u=6, v=4: sqrt(10 + 2*sqrt(24)) - sqrt(10 - 2*sqrt(24)) = 4
        ("diff_cancel", 7, 2, "Medium"),  # u=7, v=4: sqrt(11 + 2*sqrt(28)) - sqrt(11 - 2*sqrt(28)) = 4
        ("diff_cancel", 10, 3, "Medium"), # u=10, v=9: sqrt(19 + 2*sqrt(90)) - sqrt(19 - 2*sqrt(90)) = 6
        ("sum_cancel", 2, 3, "Medium"),   # u=4, v=3: sqrt(7 + 2*sqrt(12)) + sqrt(7 - 2*sqrt(12)) = 4
        ("sum_cancel", 3, 5, "Medium"),   # u=9, v=5: sqrt(14 + 2*sqrt(45)) + sqrt(14 - 2*sqrt(45)) = 6
        ("sum_cancel", 3, 7, "Medium"),   # u=9, v=7: sqrt(16 + 2*sqrt(63)) + sqrt(16 - 2*sqrt(63)) = 6
        ("diff_cancel", 11, 3, "Hard"),   # u=11, v=9: sqrt(20 + 2*sqrt(99)) - sqrt(20 - 2*sqrt(99)) = 6
        ("sum_cancel", 4, 11, "Hard"),    # u=16, v=11: sqrt(27 + 2*sqrt(176)) + sqrt(27 - 2*sqrt(176)) = 8
        ("hidden_2", 4, 3, "Hard"),       # u=16, v=3: sqrt(19 + sqrt(192)) - sqrt(3) = 4
        ("hidden_2", 5, 2, "Hard"),       # u=25, v=2: sqrt(27 + sqrt(200)) - sqrt(2) = 5
    ]
    for v_i, (kind, p1, p2, diff) in enumerate(rad_cases):
        if kind == "one_sub":
            m_sq, v = p1, p2
            u = m_sq * m_sq
            A, B = u + v, u * v
            ans = m_sq
            val_num = math.sqrt(A + 2 * math.sqrt(B)) - math.sqrt(v)
            assert math.isclose(val_num, ans, rel_tol=1e-10)
            expr_tex = f"\\sqrt{{{A} + 2\\sqrt{{{B}}}}} - \\sqrt{{{v}}}"
            distractors = [u, ans + 1, A - v, ans * 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rad_{v_i}")
            q_en = f"Simplify the nested radical expression {m(expr_tex)} to an exact integer."
            q_ar = f"بسّط المقدار الجذري المتداخل {m(expr_tex)} إلى عدد صحيح دقيق."
            h_en = f"Look for two numbers u and v whose sum is {A} and whose product is {B}: then √({A} + 2√{B}) = √u + √v!"
            h_ar = f"ابحث عن عددين مجموعهما {A} وحاصل ضربهما {B}: عندها يكون {m(f'\\sqrt{{{A} + 2\\sqrt{{{B}}}}} = \\sqrt{{u}} + \\sqrt{{v}}')}!"
            s_en = explain_en(
                "Denest \\( \\sqrt{(u + v) + 2\\sqrt{uv}} = \\sqrt{(\\sqrt{u} + \\sqrt{v})^2} = \\sqrt{u} + \\sqrt{v} \\) by finding two numbers with sum \\( A \\) and product \\( B \\)!",
                [
                    f"Find {m('u, v > 0')} with {m(f'u + v = {A}')} and {m(f'uv = {B}')}: they are {m(f'u = {u}')} and {m(f'v = {v}')}.",
                    f"Rewrite under the radical: {m(f'\\sqrt{{{A} + 2\\sqrt{{{B}}}}} = \\sqrt{{(\\sqrt{{{u}}} + \\sqrt{{{v}}})^2}} = {m_sq} + \\sqrt{{{v}}}')}.",
                    f"Subtract {m(f'\\sqrt{{{v}}}')}: {m(f'({m_sq} + \\sqrt{{{v}}}) - \\sqrt{{{v}}} = {ans}')}.",
                ],
                f"Square back to verify: \\( ({m_sq} + \\sqrt{{{v}}})^2 = {u} + 2({m_sq})\\sqrt{{{v}}} + {v} = {A} + 2\\sqrt{{{B}}} \\)!",
            )
            s_ar = explain_ar(
                "نفكّ الجذر المتداخل عبر المتطابقة \\( \\sqrt{(u + v) + 2\\sqrt{uv}} = \\sqrt{u} + \\sqrt{v} \\) بالبحث عن عددين مجموعهما \\( A \\) وضربهما \\( B \\)!",
                [
                    f"نبحث عن عددين مجموعهما {m(A)} وضربهما {m(B)}: نجد {m(f'u = {u}')} و{m(f'v = {v}')}.",
                    f"إذن {m(f'\\sqrt{{{A} + 2\\sqrt{{{B}}}}} = \\sqrt{{(\\sqrt{{{u}}} + \\sqrt{{{v}}})^2}} = {m_sq} + \\sqrt{{{v}}}')}.",
                    f"نطرح {m(f'\\sqrt{{{v}}}')}: {m(f'({m_sq} + \\sqrt{{{v}}}) - \\sqrt{{{v}}} = {ans}')}.",
                ],
                f"تحقق بالتربيع العكسي: \\( ({m_sq} + \\sqrt{{{v}}})^2 = {A} + 2\\sqrt{{{B}}} \\)!",
            )
        elif kind == "diff_cancel":
            u, m_sq = p1, p2
            v = m_sq * m_sq
            assert u > v
            A, B = u + v, u * v
            ans = 2 * m_sq
            val_num = math.sqrt(A + 2 * math.sqrt(B)) - math.sqrt(A - 2 * math.sqrt(B))
            assert math.isclose(val_num, ans, rel_tol=1e-10)
            expr_tex = f"\\sqrt{{{A} + 2\\sqrt{{{B}}}}} - \\sqrt{{{A} - 2\\sqrt{{{B}}}}}"
            distractors = [m_sq, 2 * v, u - v, ans + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rad_{v_i}")
            q_en = f"What is the exact value of {m(expr_tex)}?"
            q_ar = f"ما القيمة الدقيقة للمقدار {m(expr_tex)}؟"
            h_en = f"Find u + v = {A} and u·v = {B} with u > v! Remember √((√u − √v)²) = √u − √v (positive!), so the √u terms cancel!"
            h_ar = f"ابحث عن عددين {m('u > v')} مجموعهما {A} وضربهما {B}! تذكّر أن الجذر التربيعي موجب دائماً {m('\\sqrt{(\\sqrt{u}-\\sqrt{v})^2} = \\sqrt{u} - \\sqrt{v}')}!"
            s_en = explain_en(
                "For \\( u > v > 0 \\), \\( \\sqrt{(u+v) + 2\\sqrt{uv}} = \\sqrt{u} + \\sqrt{v} \\) and \\( \\sqrt{(u+v) - 2\\sqrt{uv}} = \\sqrt{u} - \\sqrt{v} \\) (put the LARGER root \\( \\sqrt{u} \\) first so the square root stays positive)!",
                [
                    f"Since {m(f'{u} + {v} = {A}')} and {m(f'{u} \\times {v} = {B}')} with {m(f'{u} > {v}')}, denest both radicals:",
                    f"{m(f'\\sqrt{{{A} + 2\\sqrt{{{B}}}}} = \\sqrt{{{u}}} + \\sqrt{{{v}}} = \\sqrt{{{u}}} + {m_sq}')}, and {m(f'\\sqrt{{{A} - 2\\sqrt{{{B}}}}} = \\sqrt{{{u}}} - {m_sq}')}.",
                    f"Subtract carefully: {m(f'(\\sqrt{{{u}}} + {m_sq}) - (\\sqrt{{{u}}} - {m_sq}) = 2 \\times {m_sq} = {ans}')}.",
                ],
                f"Order trap avoided: had we written \\( {m_sq} - \\sqrt{{{u}}} < 0 \\) for the second root, we would have gotten a negative answer for a positive difference!",
            )
            s_ar = explain_ar(
                "عندما يكون \\( u > v > 0 \\)، فإن \\( \\sqrt{(u+v) - 2\\sqrt{uv}} = \\sqrt{u} - \\sqrt{v} \\) (نضع الجذر الأكبر \\( \\sqrt{u} \\) أولاً لأن ناتج الجذر التربيعي موجب دائماً)!",
                [
                    f"بما أن {m(f'{u} + {v} = {A}')} و{m(f'{u} \\times {v} = {B}')} مع {m(f'{u} > {v}')}، نفكّ الجذرين:",
                    f"الأول يساوي {m(f'\\sqrt{{{u}}} + {m_sq}')}، والثاني يساوي {m(f'\\sqrt{{{u}}} - {m_sq}')}.",
                    f"نطرحهما فتختفي {m(f'\\sqrt{{{u}}}')}: {m(f'(\\sqrt{{{u}}} + {m_sq}) - (\\sqrt{{{u}}} - {m_sq}) = {ans}')}.",
                ],
                f"انتبه للترتيب: كتابة \\( \\sqrt{{{u}}} - {m_sq} > 0 \\) تحميك من الخطأ الشائع في الإشارة!",
            )
        elif kind == "sum_cancel":
            m_sq, v = p1, p2
            u = m_sq * m_sq
            assert u > v
            A, B = u + v, u * v
            ans = 2 * m_sq
            val_num = math.sqrt(A + 2 * math.sqrt(B)) + math.sqrt(A - 2 * math.sqrt(B))
            assert math.isclose(val_num, ans, rel_tol=1e-10)
            expr_tex = f"\\sqrt{{{A} + 2\\sqrt{{{B}}}}} + \\sqrt{{{A} - 2\\sqrt{{{B}}}}}"
            distractors = [m_sq, 2 * u, A, ans + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rad_{v_i}")
            q_en = f"Evaluate the nested radical sum {m(expr_tex)}."
            q_ar = f"احسب قيمة مجموع الجذرين المتداخلين {m(expr_tex)}."
            h_en = f"Here u = {u} > v = {v} satisfies u + v = {A} and u·v = {B}; denesting gives ({m_sq} + √{v}) + ({m_sq} − √{v})!"
            h_ar = f"هنا {m(f'u = {u} > v = {v}')} يحققان المجموع {A} والضرب {B}؛ عند الفك نحصل على {m(f'({m_sq} + \\sqrt{{{v}}}) + ({m_sq} - \\sqrt{{{v}}})')}!"
            s_en = explain_en(
                "Check which of \\( u, v \\) is larger BEFORE taking \\( \\sqrt{(\\sqrt{u} - \\sqrt{v})^2} = |\\sqrt{u} - \\sqrt{v}| \\)!",
                [
                    f"Find {m('u > v > 0')} with {m(f'u + v = {A}')} and {m(f'uv = {B}')}: {m(f'u = {u}')} and {m(f'v = {v}')}.",
                    f"Since {m(f'\\sqrt{{{u}}} = {m_sq} > \\sqrt{{{v}}}')}, the two radicals denest to {m(f'{m_sq} + \\sqrt{{{v}}}')} and {m(f'{m_sq} - \\sqrt{{{v}}}')}.",
                    f"Add them so {m(f'\\pm\\sqrt{{{v}}}')} cancels: {m(f'({m_sq} + \\sqrt{{{v}}}) + ({m_sq} - \\sqrt{{{v}}}) = {ans}')}.",
                ],
                f"Alternative check by squaring the whole sum \\( S \\): \\( S^2 = 2({A}) + 2\\sqrt{{{A}^2 - 4({B})}} = {2*A} + 2({u-v}) = {ans*ans} \\implies S = {ans} \\)!",
            )
            s_ar = explain_ar(
                "نتحقق أولاً أيهما أكبر بين \\( u \\) و\\( v \\) لكي نكتب \\( \\sqrt{(\\sqrt{u} - \\sqrt{v})^2} = \\sqrt{u} - \\sqrt{v} > 0 \\) بشكل صحيح!",
                [
                    f"العددان اللذان مجموعهما {m(A)} وضربهما {m(B)} هما {m(f'u = {u}')} و{m(f'v = {v}')} حيث {m(f'{u} > {v}')}.",
                    f"يُفكّ الجذر الأول إلى {m(f'{m_sq} + \\sqrt{{{v}}}')} والثاني إلى {m(f'{m_sq} - \\sqrt{{{v}}}')}.",
                    f"عند جمعهما يختصر {m(f'\\sqrt{{{v}}}')} ويبقى {m(f'{m_sq} + {m_sq} = {ans}')}.",
                ],
                f"تحقق بتربيع المجموع \\( S \\): \\( S^2 = 2({A}) + 2\\sqrt{{{A}^2 - 4({B})}} = {ans*ans} \\implies S = {ans} \\)!",
            )
        else:
            # hidden_2: sqrt(A + sqrt(4B)) - sqrt(v) = m_sq
            m_sq, v = p1, p2
            u = m_sq * m_sq
            A, B = u + v, u * v
            four_B = 4 * B
            ans = m_sq
            val_num = math.sqrt(A + math.sqrt(four_B)) - math.sqrt(v)
            assert math.isclose(val_num, ans, rel_tol=1e-10)
            expr_tex = f"\\sqrt{{{A} + \\sqrt{{{four_B}}}}} - \\sqrt{{{v}}}"
            distractors = [u, ans + 2, 2 * ans, A - v]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_rad_{v_i}")
            q_en = f"Find the exact integer value of {m(expr_tex)}."
            q_ar = f"أوجد القيمة الصحيحة الدقيقة للمقدار {m(expr_tex)}."
            h_en = f"Pull a factor of 4 out of the inner square root first (√{four_B} = 2√{B}) to create the 2√B pattern needed for denesting!"
            h_ar = f"أخرج العامل 4 من تحت الجذر الداخلي أولاً ({m(f'\\sqrt{{{four_B}}} = 2\\sqrt{{{B}}}')}) لتظهر الصورة القياسية {m('2\\sqrt{uv}')}!"
            s_en = explain_en(
                "To use \\( \\sqrt{(u+v) + 2\\sqrt{uv}} = \\sqrt{u} + \\sqrt{v} \\), there MUST be a coefficient of \\( 2 \\) in front of the inner radical — pull \\( \\sqrt{4} = 2 \\) out first!",
                [
                    f"Rewrite the inner root: {m(f'\\sqrt{{{four_B}}} = \\sqrt{{4 \\times {B}}} = 2\\sqrt{{{B}}}')}.",
                    f"Now find {m('u, v')} with {m(f'u + v = {A}')} and {m(f'uv = {B}')}: {m(f'u = {u}')} and {m(f'v = {v}')}.",
                    f"Denest and subtract: {m(f'\\sqrt{{{A} + 2\\sqrt{{{B}}}}} - \\sqrt{{{v}}} = ({m_sq} + \\sqrt{{{v}}}) - \\sqrt{{{v}}} = {ans}')}.",
                ],
                f"Never search for \\( uv = {four_B} \\) before pulling out the \\( 2 \\)!",
            )
            s_ar = explain_ar(
                "لتطبيق قاعدة فك الجذر المتداخل لا بد من وجود المعامل \\( 2 \\) أمام الجذر الداخلي؛ لذا نُخرج \\( \\sqrt{4} = 2 \\) أولاً!",
                [
                    f"نبسّط الجذر الداخلي: {m(f'\\sqrt{{{four_B}}} = \\sqrt{{4 \\times {B}}} = 2\\sqrt{{{B}}}')}.",
                    f"نبحث عن عددين مجموعهما {m(A)} وضربهما {m(B)}: نجد {m(f'u = {u}')} و{m(f'v = {v}')}.",
                    f"نفك الجذر ونطرح: {m(f'({m_sq} + \\sqrt{{{v}}}) - \\sqrt{{{v}}} = {ans}')}.",
                ],
                f"إخراج العامل \\( 2 \\) أمام الجذر الداخلي هو الخطوة المفتاحية دائماً!",
            )
        push(topic, diff, "kmc_g1011_nested_radical_denest", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)


def _gen_lesson_3_5(push) -> None:
    topic = "Geometry"

    # ------------------------------------------------------------------
    # 13. kmc_g1011_power_of_point_secant_tangent (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    pop_cases = [
        # ("find_pt", pa, ab, diff)
        # ("find_ab", pt, pa, diff)
        # ("find_pa", pt, ab, diff)
        # ("chord", ae, eb, ce, diff) -> ed = (ae*eb)//ce
        # ("combo", pt, pa, ae, ce, diff) -> ab = pt^2//pa - pa, eb = ab - ae, ed = (ae*eb)//ce
        ("find_pt", 4, 5, "Easy"),
        ("find_pt", 3, 9, "Easy"),
        ("find_pt", 2, 6, "Easy"),
        ("chord", 3, 8, 4, "Easy"),
        ("chord", 4, 9, 6, "Easy"),
        ("find_pt", 8, 10, "Medium"),
        ("find_pt", 9, 7, "Medium"),
        ("find_pt", 5, 15, "Medium"),
        ("find_ab", 6, 4, "Medium"),
        ("find_ab", 12, 9, "Medium"),
        ("find_ab", 10, 5, "Medium"),
        ("find_ab", 15, 9, "Medium"),
        ("chord", 6, 10, 5, "Medium"),
        ("find_pa", 6, 5, "Hard"),        # PA(PA + 5) = 36 -> PA = 4
        ("find_pa", 8, 12, "Hard"),       # PA(PA + 12) = 64 -> PA = 4
        ("find_pa", 12, 7, "Hard"),       # PA(PA + 7) = 144 -> PA = 9
        ("combo", 12, 8, 4, 6, "Hard"),   # PB=18 => AB=10 => EB=6 => ED=(4*6)/6=4
    ]
    for v_i, item in enumerate(pop_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "find_pt":
            _, pa, ab, _ = item
            pb = pa + ab
            pt = math.isqrt(pa * pb)
            assert pt * pt == pa * pb
            ans = pt
            svg = svg_power_of_point("PT", str(pa), str(ab))
            distractors = [pa * ab, math.isqrt(pa * ab) if math.isqrt(pa * ab) ** 2 == pa * ab else pt + 2, pb, pt - 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_pop_{v_i}")
            q_en = (
                f"From an exterior point {m('P')}, tangent segment {m('PT')} touches a circle at {m('T')}, and secant {m('PAB')} "
                f"intersects the circle at {m('A')} and {m('B')} with {m(f'PA = {pa}')} and {m(f'AB = {ab}')}, as shown. "
                f"What is the length of the tangent {m('PT')}?"
            )
            q_ar = (
                f"من نقطة خارجية {m('P')}، رُسم المماس {m('PT')} ليمس الدائرة عند {m('T')}، ورُسم القاطع {m('PAB')} "
                f"ليقطع الدائرة في {m('A')} و{m('B')} بحيث {m(f'PA = {pa}')} و{m(f'AB = {ab}')} كما في الشكل. "
                f"ما طول القطعة المماسة {m('PT')}؟"
            )
            h_en = f"Careful with PB! The full secant is PB = PA + AB = {pa} + {ab} = {pb}, and Power of a Point gives PT² = PA × PB!"
            h_ar = f"انتبه لطول القاطع الكامل: {m(f'PB = PA + AB = {pa} + {ab} = {pb}')}، ومن قوة النقطة {m('PT^2 = PA \\times PB')}!"
            s_en = explain_en(
                "By the Tangent-Secant Theorem (Power of a Point), \\( PT^2 = PA \\times PB \\), where \\( PB = PA + AB \\) is the **entire** secant from \\( P \\)!",
                [
                    f"Add the two parts to find the full secant length: {m(f'PB = PA + AB = {pa} + {ab} = {pb}')}.",
                    f"Apply Power of a Point from {m('P')}: {m(f'PT^2 = PA \\times PB = {pa} \\times {pb} = {pa*pb}')}.",
                    f"Take the positive square root: {m(f'PT = \\sqrt{{{pa*pb}}} = {ans}')}.",
                ],
                f"Trap check: NEVER write \\( PT^2 = PA \\times AB = {pa*ab} \\) — always measure both segments from the exterior point \\( P \\)!",
            )
            s_ar = explain_ar(
                "بحسب نظرية المماس والقاطع (قوة النقطة)، فإن \\( PT^2 = PA \\times PB \\)، حيث \\( PB = PA + AB \\) هو طول القاطع **كاملاً** بدءاً من \\( P \\)!",
                [
                    f"نحسب طول القاطع الكامل: {m(f'PB = PA + AB = {pa} + {ab} = {pb}')}.",
                    f"نطبّق نظرية المماس والقاطع: {m(f'PT^2 = PA \\times PB = {pa} \\times {pb} = {pa*pb}')}.",
                    f"بأخذ الجذر التربيعي الموجب نجد: {m(f'PT = \\sqrt{{{pa*pb}}} = {ans}')}.",
                ],
                f"احذر الفخ الأشهر: لا تضرب \\( PA \\times AB \\) أبداً، بل \\( PA \\times PB \\) بدءاً من النقطة \\( P \\)!",
            )
        elif kind == "find_ab":
            _, pt, pa, _ = item
            assert (pt * pt) % pa == 0
            pb = (pt * pt) // pa
            ab = pb - pa
            assert ab > 0
            ans = ab
            svg = svg_power_of_point(str(pt), str(pa), "AB")
            distractors = [pb, pt - pa, ab + pa, max(1, ab - 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_pop_{v_i}")
            q_en = (
                f"From an external point {m('P')}, tangent {m('PT')} has length {m(pt)} and secant {m('PAB')} meets the circle at {m('A')} and {m('B')} "
                f"with exterior segment {m(f'PA = {pa}')}, as shown. What is the length of the chord {m('AB')}?"
            )
            q_ar = (
                f"من نقطة خارجية {m('P')}، رُسم مماس {m('PT')} طوله {m(pt)} وقاطع {m('PAB')} يقطع الدائرة في {m('A')} و{m('B')} "
                f"بحيث طول الجزء الخارجي {m(f'PA = {pa}')} كما في الشكل. ما طول الوتر الداخلي {m('AB')}؟"
            )
            h_en = f"First solve PT² = PA × PB to find the whole secant PB = {pt}²/{pa} = {pb}, then subtract PA = {pa}!"
            h_ar = f"أوجد أولاً طول القاطع الكامل من {m(f'PT^2 = PA \\times PB \\implies PB = {pb}')}، ثم اطرح الجزء الخارجي {m(f'PA = {pa}')}!"
            s_en = explain_en(
                "Use \\( PT^2 = PA \\times PB \\) to find the **whole** secant \\( PB \\) first, then subtract \\( PA \\) to isolate the chord \\( AB \\)!",
                [
                    f"Set up Power of a Point: {m(f'{pt}^2 = {pa} \\times PB \\implies {pt*pt} = {pa} \\cdot PB')}.",
                    f"Divide by {m(pa)} to get the full secant: {m(f'PB = \\frac{{{pt*pt}}}{{{pa}}} = {pb}')}.",
                    f"Subtract the exterior piece: {m(f'AB = PB - PA = {pb} - {pa} = {ans}')}.",
                ],
                f"Trap check: {m(pb)} is the full secant {m('PB')}; the question asks for the chord {m(f'AB = {ans}')}!",
            )
            s_ar = explain_ar(
                "نوجد طول القاطع **الكلي** \\( PB \\) من العلاقة \\( PT^2 = PA \\times PB \\) أولاً، ثم نطرح \\( PA \\) لإيجاد طول الوتر \\( AB \\)!",
                [
                    f"من نظرية المماس والقاطع: {m(f'{pt}^2 = {pa} \\times PB \\implies PB = \\frac{{{pt*pt}}}{{{pa}}} = {pb}')}.",
                    f"بما أن {m('PB = PA + AB')}، نطرح الجزء الخارجي {m(f'PA = {pa}')}.",
                    f"إذن طول الوتر {m(f'AB = {pb} - {pa} = {ans}')}.",
                ],
                f"انتبه: العدد {m(pb)} هو طول {m('PB')} كاملاً، بينما المطلوب هو الوتر {m(f'AB = {ans}')}!",
            )
        elif kind == "find_pa":
            _, pt, ab, _ = item
            sols = [x for x in range(1, pt * pt + 1) if x * (x + ab) == pt * pt]
            assert len(sols) == 1
            ans = sols[0]
            svg = svg_power_of_point(str(pt), "PA", str(ab))
            distractors = [ans + ab, pt - ab if pt > ab else ans + 2, ans + 1, max(1, ans - 1)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_pop_{v_i}")
            q_en = (
                f"Tangent {m('PT')} from exterior point {m('P')} has length {m(pt)}, and secant {m('PAB')} cuts off a chord of length "
                f"{m(f'AB = {ab}')} inside the circle, as shown. What is the length of the exterior segment {m('PA')}?"
            )
            q_ar = (
                f"طول المماس {m('PT')} المرسوم من النقطة الخارجية {m('P')} يساوي {m(pt)}، ويقطع القاطع {m('PAB')} وتراً داخل الدائرة طوله "
                f"{m(f'AB = {ab}')} كما في الشكل. ما طول الجزء الخارجي {m('PA')}؟"
            )
            h_en = f"Let PA = x, so PB = x + {ab}. Solve x(x + {ab}) = {pt}² = {pt*pt} by spotting two positive factors of {pt*pt} that differ by {ab}!"
            h_ar = f"افرض {m('PA = x')} فيكون {m(f'PB = x + {ab}')}. حل المعادلة {m(f'x(x + {ab}) = {pt*pt}')} بالبحث عن عاملين للعدد {pt*pt} فرقهما {ab}!"
            s_en = explain_en(
                "Let \\( x = PA \\); then \\( PB = x + AB \\), turning \\( PT^2 = PA \\cdot PB \\) into a factorable quadratic \\( x(x + AB) = PT^2 \\)!",
                [
                    f"Write {m('PA = x')} and {m(f'PB = x + {ab}')}. Power of a Point gives {m(f'x(x + {ab}) = {pt}^2 = {pt*pt}')}.",
                    f"Expand (or spot factors of {m(pt*pt)} differing by {m(ab)}): {m(f'x^2 + {ab}x - {pt*pt} = (x - {ans})(x + {ans + ab}) = 0')}.",
                    f"Since length {m('x > 0')}, we get {m(f'PA = x = {ans}')}.",
                ],
                f"Check: \\( PA \\times PB = {ans} \\times ({ans} + {ab}) = {ans} \\times {ans+ab} = {pt*pt} = {pt}^2 \\)!",
            )
            s_ar = explain_ar(
                "نفرض \\( x = PA \\) فيكون \\( PB = x + AB \\)، وتتحول علاقة قوة النقطة إلى \\( x(x + AB) = PT^2 \\)!",
                [
                    f"نضع {m('PA = x')} و{m(f'PB = x + {ab}')}، فنجد {m(f'x(x + {ab}) = {pt}^2 = {pt*pt}')}.",
                    f"نبحث عن عاملين موجبين للعدد {m(pt*pt)} فرقهما {m(ab)} فنجد {m(ans)} و{m(ans + ab)} (أو نحلل {m(f'(x - {ans})(x + {ans + ab}) = 0')}).",
                    f"بما أن الطول موجب، فإن {m(f'PA = {ans}')}.",
                ],
                f"تحقق: \\( {ans} \\times {ans + ab} = {pt*pt} = {pt}^2 \\)!",
            )
        elif kind == "chord":
            _, ae, eb, ce, _ = item
            assert (ae * eb) % ce == 0
            ed = (ae * eb) // ce
            ans = ed
            svg = svg_power_of_point("PT", "PA", str(ae + eb))
            distractors = [ae + eb - ce, ce + ed, ans + 2, max(1, ans - 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_pop_{v_i}")
            q_en = (
                f"Inside the circle shown, a second chord {m('CD')} intersects chord {m('AB')} at an interior point {m('E')} "
                f"such that {m(f'AE = {ae}')}, {m(f'EB = {eb}')}, and {m(f'CE = {ce}')}. What is the length of segment {m('ED')}?"
            )
            q_ar = (
                f"داخل الدائرة الموضحة، يقطع وتر ثانٍ {m('CD')} الوتر {m('AB')} في نقطة داخلية {m('E')} "
                f"بحيث {m(f'AE = {ae}')} و{m(f'EB = {eb}')} و{m(f'CE = {ce}')}. ما طول القطعة {m('ED')}؟"
            )
            h_en = f"By the Intersecting Chords Theorem (interior Power of a Point), AE × EB = CE × ED!"
            h_ar = f"بحسب نظرية تقاطع الأوتار داخل دائرة، حاصل ضرب جزأي الوتر الأول يساوي حاصل ضرب جزأي الوتر الثاني: {m('AE \\times EB = CE \\times ED')}!"
            s_en = explain_en(
                "When two chords \\( AB \\) and \\( CD \\) intersect at an interior point \\( E \\), similar triangles give \\( AE \\times EB = CE \\times ED \\)!",
                [
                    f"Write the Intersecting Chords equation: {m('AE \\times EB = CE \\times ED')}.",
                    f"Substitute the known lengths: {m(f'{ae} \\times {eb} = {ce} \\times ED \\implies {ae*eb} = {ce} \\cdot ED')}.",
                    f"Divide by {m(ce)}: {m(f'ED = \\frac{{{ae*eb}}}{{{ce}}} = {ans}')}.",
                ],
                f"Don't add segments (\\( {ae} + {eb} \\neq {ce} + ED \\)): intersecting chords equate **products**, not sums!",
            )
            s_ar = explain_ar(
                "عند تقاطع وترين \\( AB \\) و\\( CD \\) داخل دائرة في النقطة \\( E \\)، ينتج من تشابه المثلثات أن \\( AE \\times EB = CE \\times ED \\)!",
                [
                    f"نطبّق قانون تقاطع الأوتار: {m('AE \\times EB = CE \\times ED')}.",
                    f"نعوّض الأطوال المعطاة: {m(f'{ae} \\times {eb} = {ce} \\times ED \\implies {ae*eb} = {ce} \\cdot ED')}.",
                    f"نقسم على {m(ce)}: {m(f'ED = \\frac{{{ae*eb}}}{{{ce}}} = {ans}')}.",
                ],
                f"تذكّر: العلاقة بين أجزاء الأوتار المتقاطعة علاقة **ضرب** وليست جمعاً!",
            )
        else:
            # combo: exterior PT, PA -> find AB, then interior E on AB -> find ED
            _, pt, pa, ae, ce, _ = item
            pb = (pt * pt) // pa
            ab = pb - pa
            eb = ab - ae
            ed = (ae * eb) // ce
            assert pt * pt == pa * pb and eb > 0 and ae * eb == ce * ed
            ans = ed
            svg = svg_power_of_point(str(pt), str(pa), "AB")
            distractors = [ab, eb, (ae * ab) // ce, ans + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_pop_{v_i}")
            q_en = (
                f"In the figure, tangent {m(f'PT = {pt}')} and exterior segment {m(f'PA = {pa}')}. "
                f"Another chord {m('CD')} intersects chord {m('AB')} inside the circle at {m('E')} with {m(f'AE = {ae}')} and {m(f'CE = {ce}')}. "
                f"What is the length of {m('ED')}?"
            )
            q_ar = (
                f"في الشكل الموضح، طول المماس {m(f'PT = {pt}')} والجزء الخارجي {m(f'PA = {pa}')}. "
                f"يقطع وتر آخر {m('CD')} الوتر {m('AB')} داخل الدائرة في النقطة {m('E')} بحيث {m(f'AE = {ae}')} و{m(f'CE = {ce}')}. "
                f"ما طول القطعة {m('ED')}؟"
            )
            h_en = f"Two-step Power of a Point: first use P outside (PT² = PA·PB) to find chord AB, then use E inside (AE·EB = CE·ED)!"
            h_ar = f"خطوتان متتاليتان لقوة النقطة: استخدم {m('PT^2 = PA \\cdot PB')} لإيجاد طول الوتر {m('AB')} أولاً، ثم {m('AE \\cdot EB = CE \\cdot ED')} داخل الدائرة!"
            s_en = explain_en(
                "Combine **exterior** Power of a Point at \\( P \\) with **interior** Power of a Point at \\( E \\)!",
                [
                    f"From {m('P')}: {m(f'PT^2 = PA \\cdot PB \\implies {pt*pt} = {pa} \\cdot PB \\implies PB = {pb}')}, so chord {m(f'AB = {pb} - {pa} = {ab}')}.",
                    f"Since {m('E')} lies on chord {m('AB')} with {m(f'AE = {ae}')}, we have {m(f'EB = {ab} - {ae} = {eb}')}.",
                    f"At interior point {m('E')}: {m(f'AE \\cdot EB = CE \\cdot ED \\implies {ae} \\times {eb} = {ce} \\cdot ED \\implies ED = {ans}')}.",
                ],
                f"Check both powers: \\( {pa} \\times {pb} = {pt}^2 \\) outside and \\( {ae} \\times {eb} = {ce} \\times {ans} = {ae*eb} \\) inside!",
            )
            s_ar = explain_ar(
                "نجمع بين قوة النقطة **الخارجية** \\( P \\) وقوة النقطة **الداخلية** \\( E \\) في خطوتين واضحتين!",
                [
                    f"من النقطة {m('P')}: {m(f'{pt}^2 = {pa} \\cdot PB \\implies PB = {pb}')}، ومنه طول الوتر {m(f'AB = {pb} - {pa} = {ab}')}.",
                    f"على الوتر {m('AB')}: {m(f'EB = AB - AE = {ab} - {ae} = {eb}')}.",
                    f"عند النقطة الداخلية {m('E')}: {m(f'{ae} \\times {eb} = {ce} \\times ED \\implies ED = {ans}')}.",
                ],
                f"تحقق مزدوج: \\( {pa} \\times {pb} = {pt*pt} \\) خارجياً، و\\( {ae} \\times {eb} = {ce} \\times {ans} \\) داخلياً!",
            )
        push(topic, diff, "kmc_g1011_power_of_point_secant_tangent", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 14. kmc_g1011_angle_bisector_ratio (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    bis_cases = [
        # ("find_bd", ab, ac, bc, diff)
        # ("find_perim", ab, bd, dc, diff)
        # ("area_part", ab, ac, tot_area, diff)
        # ("diff_seg", ab, ac, dc_minus_bd, diff) -> find BC
        # ("right_tri", ab_leg, bc_hyp_or_ac_leg, diff)
        ("find_bd", 6, 9, 10, "Easy"),
        ("find_bd", 8, 12, 15, "Easy"),
        ("find_bd", 10, 15, 20, "Easy"),
        ("find_perim", 12, 4, 6, "Easy"),
        ("area_part", 3, 5, 40, "Easy"),
        ("find_bd", 14, 21, 25, "Medium"),
        ("find_bd", 9, 15, 16, "Medium"),
        ("find_perim", 15, 5, 8, "Medium"),
        ("find_perim", 14, 7, 9, "Medium"),
        ("find_perim", 18, 6, 11, "Medium"),
        ("area_part", 4, 7, 66, "Medium"),
        ("area_part", 5, 8, 91, "Medium"),
        ("area_ratio", 12, 20, 0, "Medium"),
        ("diff_seg", 18, 24, 5, "Hard"),
        ("diff_seg", 15, 25, 6, "Hard"),
        ("right_bis", 6, 10, "Hard"),      # right angle at B: AB=6, AC=10 => BC=8, BD = 8*6/(6+10) = 3!
        ("right_bis", 15, 25, "Hard"),     # right angle at B: AB=15, AC=25 => BC=20, BD = 20*15/40 = 15/2!
    ]
    for v_i, item in enumerate(bis_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "find_bd":
            _, ab, ac, bc, _ = item
            assert ab + ac > bc and ab + bc > ac and ac + bc > ab
            ans = Fraction(bc * ab, ab + ac)
            dc = bc - ans
            assert ans / dc == Fraction(ab, ac)
            svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC")
            distractors = [dc, Fraction(bc, 2), ans + 1, max(Fraction(1, 1), ans - 1)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"In {m('\\triangle ABC')}, the interior angle bisector {m('AD')} of {m('\\angle BAC')} meets side {m('BC')} at {m('D')}, as shown. "
                f"If {m(f'AB = {ab}')}, {m(f'AC = {ac}')}, and {m(f'BC = {bc}')}, what is the length of {m('BD')}?"
            )
            q_ar = (
                f"في المثلث {m('ABC')}، ينصّف {m('AD')} الزاوية الداخلية {m('\\angle BAC')} ويلاقي الضلع {m('BC')} في {m('D')} كما في الشكل. "
                f"إذا كان {m(f'AB = {ab}')} و{m(f'AC = {ac}')} و{m(f'BC = {bc}')}، فما طول القطعة {m('BD')}؟"
            )
            g = math.gcd(ab, ac)
            ra, rc = ab // g, ac // g
            h_en = f"By the Angle Bisector Theorem, BD : DC = AB : AC = {ra} : {rc}, so BD gets {ra}/({ra} + {rc}) of the total base BC = {bc}!"
            h_ar = f"من نظرية منصف الزاوية، {m(f'BD : DC = AB : AC = {ra} : {rc}')}، أي أن {m('BD')} تأخذ الكسر {m(f'\\frac{{{ra}}}{{{ra+rc}}}')} من طول {m(f'BC = {bc}')}!"
            s_en = explain_en(
                "The Interior Angle Bisector Theorem states that \\( AD \\) divides the opposite side \\( BC \\) in the exact ratio of the adjacent sides: \\( \\frac{BD}{DC} = \\frac{AB}{AC} \\)!",
                [
                    f"Simplify the side ratio: {m(f'\\frac{{BD}}{{DC}} = \\frac{{{ab}}}{{{ac}}} = \\frac{{{ra}}}{{{rc}}}')}.",
                    f"Split {m(f'BC = {bc}')} into {m(f'{ra} + {rc} = {ra + rc}')} equal ratio parts.",
                    f"Compute {m('BD')}: {m(f'BD = \\frac{{{ra}}}{{{ra + rc}}} \\times {bc} = {fmt_val(ans)}')}.",
                ],
                f"Check: \\( DC = {bc} - {fmt_val(ans)} = {fmt_val(dc)} \\), and \\( \\frac{{{fmt_val(ans)}}}{{{fmt_val(dc)}}} = \\frac{{{ra}}}{{{rc}}} = \\frac{{{ab}}}{{{ac}}} \\)!",
            )
            s_ar = explain_ar(
                "تنص نظرية منصف الزاوية الداخلية على أن \\( AD \\) يقسم الضلع المقابل \\( BC \\) بنسبة الضلعين المجاورين: \\( \\frac{BD}{DC} = \\frac{AB}{AC} \\)!",
                [
                    f"نبسّط نسبة الضلعين: {m(f'\\frac{{BD}}{{DC}} = \\frac{{{ab}}}{{{ac}}} = \\frac{{{ra}}}{{{rc}}}')}.",
                    f"مجموع أجزاء النسبة على القاعدة {m('BC')} هو {m(f'{ra} + {rc} = {ra + rc}')} أجزاء.",
                    f"نحسب طول {m('BD')}: {m(f'BD = \\frac{{{ra}}}{{{ra + rc}}} \\times {bc} = {fmt_val(ans)}')}.",
                ],
                f"تحقق: \\( DC = {fmt_val(dc)} \\)، والنسبة \\( BD : DC = {ra} : {rc} \\) تطابق \\( AB : AC \\)!",
            )
        elif kind == "find_perim":
            _, ab, bd, dc, _ = item
            assert (ab * dc) % bd == 0
            ac = (ab * dc) // bd
            bc = bd + dc
            assert ab + bc > ac and ab + ac > bc
            ans = ab + ac + bc
            svg = svg_angle_bisector_tri(str(ab), "AC", str(bd), str(dc))
            distractors = [ac, ab + ac, ans - bd, ans + dc]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"In {m('\\triangle ABC')}, angle bisector {m('AD')} divides {m('BC')} into {m(f'BD = {bd}')} and {m(f'DC = {dc}')}, as shown. "
                f"If {m(f'AB = {ab}')}, what is the **perimeter** of {m('\\triangle ABC')}?"
            )
            q_ar = (
                f"في المثلث {m('ABC')}، يقسم منصف الزاوية {m('AD')} الضلع {m('BC')} إلى {m(f'BD = {bd}')} و{m(f'DC = {dc}')} كما في الشكل. "
                f"إذا كان {m(f'AB = {ab}')}، فما **محيط** المثلث {m('ABC')}؟"
            )
            h_en = f"First find AC from AB/AC = BD/DC ({ab}/AC = {bd}/{dc}), then add all three sides AB + AC + (BD + DC)!"
            h_ar = f"أوجد أولاً طول {m('AC')} من التناسب {m(f'\\frac{{{ab}}}{{AC}} = \\frac{{{bd}}}{{{dc}}}')}، ثم اجمع أطوال الأضلاع الثلاثة!"
            s_en = explain_en(
                "Use \\( \\frac{AB}{AC} = \\frac{BD}{DC} \\) to find the missing side \\( AC \\), then sum \\( AB + AC + BC \\)!",
                [
                    f"Apply the Angle Bisector Theorem: {m(f'\\frac{{{ab}}}{{AC}} = \\frac{{{bd}}}{{{dc}}} \\implies AC = \\frac{{{ab} \\times {dc}}}{{{bd}}} = {ac}')}.",
                    f"Find full side {m('BC')}: {m(f'BC = BD + DC = {bd} + {dc} = {bc}')}.",
                    f"Add all three sides for the perimeter: {m(f'{ab} + {ac} + {bc} = {ans}')}.",
                ],
                f"Read the final question carefully: {m(ac)} is side {m('AC')}, whereas the **perimeter** is {m(ans)}!",
            )
            s_ar = explain_ar(
                "نوجد الضلع المجهول \\( AC \\) من تناسب منصف الزاوية \\( \\frac{AB}{AC} = \\frac{BD}{DC} \\) ثم نجمع الأضلاع الثلاثة!",
                [
                    f"من نظرية منصف الزاوية: {m(f'\\frac{{{ab}}}{{AC}} = \\frac{{{bd}}}{{{dc}}} \\implies AC = \\frac{{{ab} \\times {dc}}}{{{bd}}} = {ac}')}.",
                    f"طول القاعدة الكاملة: {m(f'BC = {bd} + {dc} = {bc}')}.",
                    f"محيط المثلث {m('ABC')}: {m(f'{ab} + {ac} + {bc} = {ans}')}.",
                ],
                f"انتبه للمطلوب النهائي: {m(ac)} هو طول {m('AC')} فقط، بينما **المحيط** يساوي {m(ans)}!",
            )
        elif kind == "area_part":
            _, ab, ac, tot_area, _ = item
            assert (tot_area * ab) % (ab + ac) == 0
            ans = (tot_area * ab) // (ab + ac)
            other_a = tot_area - ans
            svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC")
            distractors = [other_a, tot_area // 2, ans + ab, max(1, other_a - ans)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"In {m('\\triangle ABC')} with {m(f'AB = {ab}')} and {m(f'AC = {ac}')}, segment {m('AD')} bisects {m('\\angle BAC')} as shown. "
                f"If the total area of {m('\\triangle ABC')} is {m(tot_area)}, what is the **area of {m('\\triangle ABD')}**?"
            )
            q_ar = (
                f"في المثلث {m('ABC')} حيث {m(f'AB = {ab}')} و{m(f'AC = {ac}')}، تنصّف القطعة {m('AD')} الزاوية {m('\\angle BAC')} كما في الشكل. "
                f"إذا كانت المساحة الكلية للمثلث {m('ABC')} تساوي {m(tot_area)}، فما **مساحة المثلث {m('ABD')}**؟"
            )
            h_en = f"Triangles ABD and ADC share the exact same altitude from A to BC, so Area(ABD) : Area(ADC) = BD : DC = {ab} : {ac}!"
            h_ar = f"المثلثان {m('ABD')} و{m('ADC')} يشتركان في نفس الارتفاع النازل من {m('A')}، لذا نسبة مساحتيهما تساوي {m(f'BD : DC = {ab} : {ac}')}!"
            s_en = explain_en(
                "Triangles sharing a vertex \\( A \\) and collinear bases \\( BD, DC \\) have areas proportional to their bases: \\( \\frac{[ABD]}{[ADC]} = \\frac{BD}{DC} = \\frac{AB}{AC} \\)!",
                [
                    f"By the Angle Bisector Theorem, {m(f'BD : DC = AB : AC = {ab} : {ac}')}.",
                    f"Since {m('\\triangle ABD')} and {m('\\triangle ADC')} share the altitude from {m('A')} to {m('BC')}, their areas also split in the ratio {m(f'{ab} : {ac}')} ({m(ab + ac)} parts total).",
                    f"Area of {m('\\triangle ABD')}: {m(f'\\frac{{{ab}}}{{{ab + ac}}} \\times {tot_area} = {ans}')}.",
                ],
                f"Sum check: \\( [ABD] + [ADC] = {ans} + {other_a} = {tot_area} \\) and \\( {ans} : {other_a} = {ab} : {ac} \\)!",
            )
            s_ar = explain_ar(
                "المثلثان المشتركان في الرأس \\( A \\) والواقعان على استقامة واحدة في القاعدة تتناسب مساحتاهما مع طولي قاعدتيهما: \\( \\frac{[ABD]}{[ADC]} = \\frac{BD}{DC} = \\frac{AB}{AC} \\)!",
                [
                    f"من نظرية منصف الزاوية: {m(f'BD : DC = AB : AC = {ab} : {ac}')}.",
                    f"وبما أن لهما نفس الارتفاع النازل من {m('A')}، تنقسم المساحة الكلية {m(tot_area)} بنسبة {m(f'{ab} : {ac}')} (مجموع الأجزاء {m(ab + ac)}).",
                    f"مساحة المثلث {m('ABD')}: {m(f'\\frac{{{ab}}}{{{ab + ac}}} \\times {tot_area} = {ans}')}.",
                ],
                f"تحقق: \\( {ans} + {other_a} = {tot_area} \\) ونسبتهما \\( {ab} : {ac} \\)!",
            )
        elif kind == "area_ratio":
            _, ab, ac, _, _ = item
            ans = Fraction(ab, ab + ac)
            svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC")
            distractors = [Fraction(ab, ac), Fraction(ac, ab + ac), Fraction(ab * ab, ab * ab + ac * ac), Fraction(1, 2)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"In {m('\\triangle ABC')} with {m(f'AB = {ab}')} and {m(f'AC = {ac}')}, {m('AD')} is the interior bisector of {m('\\angle BAC')}, as shown. "
                f"What is the **ratio of the area** of {m('\\triangle ABD')} to the area of {m('\\triangle ABC')}?"
            )
            q_ar = (
                f"في المثلث {m('ABC')} حيث {m(f'AB = {ab}')} و{m(f'AC = {ac}')}، يمثّل {m('AD')} منصف الزاوية الداخلية {m('\\angle BAC')} كما في الشكل. "
                f"ما **نسبة مساحة** المثلث {m('ABD')} إلى مساحة المثلث الكبير {m('ABC')}؟"
            )
            h_en = "Watch the denominator! Area(ABD) : Area(ADC) = AB : AC, so Area(ABD) : Area(ABC) = AB : (AB + AC) — NOT squared because these triangles are NOT similar!"
            h_ar = "انتبه للمقام! نسبة المساحتين الجزئيتين هي AB : AC، فتكون نسبة [ABD] إلى المثلث الكلي هي AB : (AB + AC) (دون تربيع لأن المثلثات غير متشابهة)!"
            s_en = explain_en(
                "\\( \\triangle ABD \\) and \\( \\triangle ABC \\) share the exact same altitude from \\( A \\) to line \\( BC \\), so \\( \\frac{[ABD]}{[ABC]} = \\frac{BD}{BC} = \\frac{AB}{AB + AC} \\)!",
                [
                    f"By the Angle Bisector Theorem, {m(f'\\frac{{BD}}{{DC}} = \\frac{{{ab}}}{{{ac}}}')}.",
                    f"Therefore {m('BD')} is the fraction {m(f'\\frac{{{ab}}}{{{ab} + {ac}}} = \\frac{{{ab}}}{{{ab+ac}}}')} of the entire base {m('BC')}.",
                    f"Simplify the fraction: {m(f'\\frac{{[ABD]}}{{[ABC]}} = \\frac{{BD}}{{BC}} = {fmt_val(ans)}')}.",
                ],
                f"Trap check: do NOT square the ratio (squaring applies to similar triangles, not equal-height triangles)!",
            )
            s_ar = explain_ar(
                "يشترك المثلثان \\( ABD \\) و\\( ABC \\) في الارتفاع نفسه النازل من \\( A \\) على \\( BC \\)، لذا فإن \\( \\frac{[ABD]}{[ABC]} = \\frac{BD}{BC} = \\frac{AB}{AB + AC} \\)!",
                [
                    f"من نظرية منصف الزاوية: {m(f'BD : DC = {ab} : {ac}')}.",
                    f"إذن تمثّل {m('BD')} الكسر {m(f'\\frac{{{ab}}}{{{ab} + {ac}}} = \\frac{{{ab}}}{{{ab+ac}}}')} من القاعدة الكلية {m('BC')}.",
                    f"بعد التبسيط نجد نسبة المساحة: {m(fmt_val(ans))}.",
                ],
                f"فخ شائع: لا تربّع النسبة، فالمثلثان هنا متساويا الارتفاع وليسا متشابهين!",
            )
        elif kind == "diff_seg":
            _, ab, ac, diff_d, _ = item
            g = math.gcd(ab, ac)
            ra, rc = ab // g, ac // g
            assert diff_d % (rc - ra) == 0
            u = diff_d // (rc - ra)
            ans = (ra + rc) * u
            bd, dc = ra * u, rc * u
            assert dc - bd == diff_d and ab + ac > ans and ab + ans > ac
            svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC")
            distractors = [dc, bd, (ab + ac), ans + u]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"In {m('\\triangle ABC')} with {m(f'AB = {ab}')} and {m(f'AC = {ac}')}, the angle bisector {m('AD')} meets {m('BC')} at {m('D')} "
                f"such that {m(f'DC - BD = {diff_d}')}. What is the total length of side {m('BC')}?"
            )
            q_ar = (
                f"في المثلث {m('ABC')} حيث {m(f'AB = {ab}')} و{m(f'AC = {ac}')}، يلاقي منصف الزاوية {m('AD')} الضلع {m('BC')} في {m('D')} "
                f"بحيث {m(f'DC - BD = {diff_d}')}. ما الطول الكلي للضلع {m('BC')}؟"
            )
            h_en = f"Reduce AB : AC = {ra} : {rc}, set BD = {ra}k and DC = {rc}k, solve ({rc} − {ra})k = {diff_d} for k, then compute BC = ({ra} + {rc})k!"
            h_ar = f"بسّط النسبة {m(f'AB : AC = {ra} : {rc}')}، وافرض {m(f'BD = {ra}k')} و{m(f'DC = {rc}k')}، ثم أوجد {m('k')} من الفرق واحسب {m(f'BC = {ra+rc}k')}!"
            s_en = explain_en(
                "Parametrize \\( BD \\) and \\( DC \\) using the simplified ratio \\( AB : AC \\) so the difference \\( DC - BD \\) gives the scale factor immediately!",
                [
                    f"By the Angle Bisector Theorem, {m(f'BD : DC = {ab} : {ac} = {ra} : {rc}')}. Write {m(f'BD = {ra}k')} and {m(f'DC = {rc}k')}.",
                    f"Use the given difference: {m(f'DC - BD = ({rc} - {ra})k = {rc - ra}k = {diff_d} \\implies k = {u}')}.",
                    f"Total base {m(f'BC = BD + DC = ({ra} + {rc})k = {ra + rc} \\times {u} = {ans}')}.",
                ],
                f"Check: \\( BD = {bd} \\), \\( DC = {dc} \\), \\( {dc} - {bd} = {diff_d} \\), and \\( {bd} + {dc} = {ans} \\)!",
            )
            s_ar = explain_ar(
                "نمثّل \\( BD \\) و\\( DC \\) بدلالة ثابت تناسب \\( k \\) بعد تبسيط النسبة \\( AB : AC \\)!",
                [
                    f"من نظرية منصف الزاوية: {m(f'BD : DC = {ab} : {ac} = {ra} : {rc}')}، فنفرض {m(f'BD = {ra}k')} و{m(f'DC = {rc}k')}.",
                    f"من معطى الفرق: {m(f'({rc} - {ra})k = {diff_d} \\implies k = {u}')}.",
                    f"الطول الكلي: {m(f'BC = ({ra} + {rc})k = {ra + rc} \\times {u} = {ans}')}.",
                ],
                f"تحقق: \\( BD = {bd} \\) و\\( DC = {dc} \\)، وفرقهما \\( {diff_d} \\) ومجموعهما \\( {ans} \\)!",
            )
        else:
            # right_bis: right angle at B, AB = leg, AC = hyp -> BC = sqrt(AC^2 - AB^2), BD = BC * AB / (AB + AC)
            _, ab, ac, _ = item
            bc = math.isqrt(ac * ac - ab * ab)
            assert ab * ab + bc * bc == ac * ac
            ans = Fraction(bc * ab, ab + ac)
            svg = svg_angle_bisector_tri(str(ab), str(ac), "BD", "DC")
            distractors = [bc - ans, Fraction(bc, 2), Fraction(bc * ab, ac), ans + 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_bis_{v_i}")
            q_en = (
                f"Triangle {m('ABC')} has a right angle at {m('B')} ({m('\\angle ABC = 90^\\circ')}), leg {m(f'AB = {ab}')}, and hypotenuse {m(f'AC = {ac}')}. "
                f"If {m('AD')} bisects {m('\\angle BAC')} with {m('D')} on {m('BC')}, what is the length of {m('BD')}?"
            )
            q_ar = (
                f"المثلث {m('ABC')} قائم الزاوية في {m('B')} ({m('\\angle ABC = 90^\\circ')})، فيه الضلع القائم {m(f'AB = {ab}')} والوتر {m(f'AC = {ac}')}. "
                f"إذا كان {m('AD')} منصفاً للزاوية {m('\\angle BAC')} ويلاقي {m('BC')} في {m('D')}، فما طول {m('BD')}؟"
            )
            h_en = f"First find leg BC = √({ac}² − {ab}²) = {bc} via the Pythagorean theorem, then apply BD : DC = AB : AC = {ab} : {ac}!"
            h_ar = f"أوجد أولاً الضلع القائم {m(f'BC = \\sqrt{{{ac}^2 - {ab}^2}} = {bc}')} بنظرية فيثاغورس، ثم طبّق نظرية منصف الزاوية!"
            s_en = explain_en(
                "Combine the **Pythagorean theorem** (to find \\( BC \\)) with the **Angle Bisector Theorem** (to split \\( BC \\) in ratio \\( AB : AC \\))!",
                [
                    f"Since {m('\\angle B = 90^\\circ')}, {m(f'BC = \\sqrt{{AC^2 - AB^2}} = \\sqrt{{{ac}^2 - {ab}^2}} = {bc}')}.",
                    f"By the Angle Bisector Theorem, {m(f'BD : DC = AB : AC = {ab} : {ac}')}.",
                    f"Thus {m(f'BD = \\frac{{{ab}}}{{{ab} + {ac}}} \\times {bc} = \\frac{{{ab * bc}}}{{{ab + ac}}} = {fmt_val(ans)}')}.",
                ],
                f"Trap check: \\( AD \\) bisects the angle, NOT the opposite side (\\( BD = {fmt_val(ans)} < \\frac{{{bc}}}{{2}} \\) because \\( AB < AC \\))!",
            )
            s_ar = explain_ar(
                "نجمع بين **نظرية فيثاغورس** لإيجاد \\( BC \\) و**نظرية منصف الزاوية** لتقسيم \\( BC \\) بنسبة \\( AB : AC \\)!",
                [
                    f"من فيثاغورس في المثلث القائم في {m('B')}: {m(f'BC = \\sqrt{{{ac}^2 - {ab}^2}} = {bc}')}.",
                    f"من نظرية منصف الزاوية: {m(f'BD : DC = AB : AC = {ab} : {ac}')}.",
                    f"إذن {m(f'BD = \\frac{{{ab}}}{{{ab} + {ac}}} \\times {bc} = {fmt_val(ans)}')}.",
                ],
                f"لاحظ منطقياً أن \\( BD < DC \\) لأن الضلع المجاور \\( AB = {ab} \\) أقصر من الوتر \\( AC = {ac} \\)!",
            )
        push(topic, diff, "kmc_g1011_angle_bisector_ratio", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 15. kmc_g1011_right_triangle_inradius (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # ------------------------------------------------------------------
    inc_cases = [
        # ("find_r", a, b, c, given_c, diff)
        # ("sum_Rr", a, b, c, diff) -> R + r = (a + b)/2
        # ("inc_area", a, b, c, diff) -> pi * r^2
        # ("inv_perim", a, b, c, diff) -> given c, r -> perimeter = 2c + 2r
        # ("inv_area", a, b, c, diff) -> given c, r -> area = r(c + r)
        ("find_r", 3, 4, 5, True, "Easy"),
        ("find_r", 6, 8, 10, True, "Easy"),
        ("find_r", 5, 12, 13, True, "Easy"),
        ("find_r", 9, 12, 15, False, "Easy"),
        ("inc_area", 6, 8, 10, "Easy"),
        ("find_r", 8, 15, 17, False, "Medium"),
        ("find_r", 7, 24, 25, False, "Medium"),
        ("sum_Rr", 6, 8, 10, "Medium"),
        ("sum_Rr", 10, 24, 26, "Medium"),
        ("sum_Rr", 12, 16, 20, "Medium"),
        ("inc_area", 8, 15, 17, "Medium"),
        ("inc_area", 12, 16, 20, "Medium"),
        ("inc_area", 9, 40, 41, "Hard"),
        ("inv_perim", 8, 15, 17, "Hard"),
        ("inv_area", 5, 12, 13, "Hard"),
        ("inv_area", 7, 24, 25, "Hard"),
    ]
    for v_i, item in enumerate(inc_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "find_r":
            _, a, b, c, given_c, _ = item
            assert a * a + b * b == c * c
            r = (a + b - c) // 2
            assert 2 * r == a + b - c and (a * b) // 2 == r * ((a + b + c) // 2)
            ans = r
            svg = svg_right_tri_incircle(str(a), str(b), str(c) if given_c else "c", "r")
            distractors = [c // 2 if c % 2 == 0 else r + 2, a + b - c, r + 1, max(1, r - 1)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_inc_{v_i}")
            if given_c:
                q_en = (
                    f"A right triangle has legs {m(a)} and {m(b)} and hypotenuse {m(c)}, with an inscribed circle of radius {m('r')} as shown. "
                    f"What is the **inradius** {m('r')}?"
                )
                q_ar = (
                    f"مثلث قائم الزاوية طولا ضلعيه القائمين {m(a)} و{m(b)} ووتره {m(c)}، رُسمت داخله دائرة محاطة نصف قطرها {m('r')} كما في الشكل. "
                    f"ما قيمة **نصف قطر الدائرة الداخلية** {m('r')}؟"
                )
                step1_en = f"Notice the corner around the right angle with two radii and two tangent segments is a **square** of side {m('r')}!"
                step1_ar = f"الشكل الرباعي عند الزاوية القائمة المكوّن من نصفي قطرين وقطعتي مماس هو **مربع** طول ضلعه {m('r')}!"
            else:
                q_en = (
                    f"A circle of radius {m('r')} is inscribed inside a right triangle whose perpendicular legs have lengths {m(a)} and {m(b)}, as shown. "
                    f"What is the radius {m('r')} of the inscribed circle?"
                )
                q_ar = (
                    f"دائرة نصف قطرها {m('r')} مرسومة داخل مثلث قائم الزاوية طولا ساقيه المتعامدتين {m(a)} و{m(b)} كما في الشكل. "
                    f"ما نصف القطر {m('r')} للدائرة الداخلية؟"
                )
                step1_en = f"First find the hypotenuse by the Pythagorean theorem: {m(f'c = \\sqrt{{{a}^2 + {b}^2}} = {c}')}."
                step1_ar = f"نوجد الوتر أولاً بنظرية فيثاغورس: {m(f'c = \\sqrt{{{a}^2 + {b}^2}} = {c}')}."
            h_en = f"Use the right-triangle inradius formula r = (a + b − c) / 2 (derived from equal tangent segments (a − r) + (b − r) = c)!"
            h_ar = f"استخدم قانون نصف قطر الدائرة الداخلية للمثلث القائم {m('r = \\frac{a + b - c}{2}')}!"
            s_en = explain_en(
                "In ANY right triangle with legs \\( a, b \\) and hypotenuse \\( c \\), equal tangents from the acute vertices give \\( (a - r) + (b - r) = c \\implies r = \\frac{a + b - c}{2} \\)!",
                [
                    step1_en,
                    f"Remaining tangent segments along the legs have lengths {m(f'{a} - r')} and {m(f'{b} - r')}, which fold onto the hypotenuse: {m(f'({a} - r) + ({b} - r) = {c}')}.",
                    f"Solve for {m('r')}: {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = \\frac{{{a + b - c}}}{{2}} = {ans}')}.",
                ],
                f"Area check via \\( \\text{{Area}} = r \\cdot s \\): semiperimeter \\( s = {(a+b+c)//2} \\), and \\( {ans} \\times {(a+b+c)//2} = {(a*b)//2} = \\frac{{1}}{{2}}({a})({b}) \\)!",
            )
            s_ar = explain_ar(
                "في أي مثلث قائم الزاوية ساقاه \\( a, b \\) ووتره \\( c \\)، تساوي قطع المماسات يعطي \\( (a - r) + (b - r) = c \\) ومنه \\( r = \\frac{a + b - c}{2} \\)!",
                [
                    step1_ar,
                    f"بما أن المماسات المرسومة من كل رأس متساوية، فإن {m(f'({a} - r) + ({b} - r) = {c}')}.",
                    f"نحسب {m('r')}: {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = \\frac{{{a + b - c}}}{{2}} = {ans}')}.",
                ],
                f"تحقق عبر المساحة \\( A = r \\cdot s \\): نصف المحيط \\( s = {(a+b+c)//2} \\)، و\\( {ans} \\times {(a+b+c)//2} = {(a*b)//2} \\)!",
            )
        elif kind == "sum_Rr":
            _, a, b, c, _ = item
            assert a * a + b * b == c * c and c % 2 == 0
            r = (a + b - c) // 2
            R = c // 2
            ans = R + r
            assert ans == (a + b) // 2
            svg = svg_right_tri_incircle(str(a), str(b), str(c), "r")
            distractors = [R, r, R - r, a + b]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_inc_{v_i}")
            q_en = (
                f"A right triangle has legs {m(a)} and {m(b)} and hypotenuse {m(c)}. "
                f"If {m('r')} is the radius of its inscribed circle (shown) and {m('R')} is the radius of its circumscribed circle, what is the sum {m('R + r')}?"
            )
            q_ar = (
                f"مثلث قائم الزاوية ساقاه {m(a)} و{m(b)} ووتره {m(c)}. "
                f"إذا كان {m('r')} نصف قطر دائرته الداخلية (الموضحة) و{m('R')} نصف قطر دائرته المحيطة، فما قيمة المجموع {m('R + r')}؟"
            )
            h_en = f"For a right triangle, circumradius R = c/2 = {R} and inradius r = (a + b − c)/2 = {r} — notice how c cancels when you add R + r!"
            h_ar = f"في المثلث القائم، نصف القطر المحيط {m('R = \\frac{c}{2}')} والداخلي {m('r = \\frac{a+b-c}{2}')} — لاحظ اختصار {m('c')} عند جمعهما!"
            s_en = explain_en(
                "Beautiful right-triangle identity: \\( R = \\frac{c}{2} \\) (Thales' theorem) and \\( r = \\frac{a + b - c}{2} \\), so \\( R + r = \\frac{a + b}{2} \\)!",
                [
                    f"Circumradius of a right triangle is half the hypotenuse: {m(f'R = \\frac{{{c}}}{{2}} = {R}')}.",
                    f"Inradius is {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = {r}')}.",
                    f"Add them: {m(f'R + r = {R} + {r} = {ans}')} (which also equals {m(f'\\frac{{{a} + {b}}}{{2}}')} directly!).",
                ],
                f"Remember \\( R + r = \\frac{{a + b}}{{2}} \\) — it saves time whenever KMC gives you the sum of the legs!",
            )
            s_ar = explain_ar(
                "متطابقة رائعة للمثلث القائم: \\( R = \\frac{c}{2} \\) و\\( r = \\frac{a + b - c}{2} \\)، وبجمعهما يختصر الوتر فنجد \\( R + r = \\frac{a + b}{2} \\)!",
                [
                    f"نصف قطر الدائرة المحيطة يساوي نصف الوتر: {m(f'R = \\frac{{{c}}}{{2}} = {R}')}.",
                    f"نصف قطر الدائرة الداخلية: {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = {r}')}.",
                    f"نجمع القيمتين: {m(f'R + r = {R} + {r} = {ans}')}.",
                ],
                f"احفظ القاعدة السريعة: \\( R + r = \\frac{{a + b}}{{2}} = {ans} \\) دائماً في المثلث القائم!",
            )
        elif kind == "inc_area":
            _, a, b, c, _ = item
            assert a * a + b * b == c * c
            r = (a + b - c) // 2
            ans_tex = f"{r * r}\\pi"
            d_list = [f"{2 * r}\\pi", f"{r}\\pi", f"{4 * r * r}\\pi", f"{(c // 2 if c % 2 == 0 else r + 2) ** 2}\\pi"]
            svg = svg_right_tri_incircle(str(a), str(b), "c", "r")
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3x_inc_{v_i}")
            q_en = (
                f"A circle is inscribed inside a right triangle whose perpendicular legs measure {m(a)} cm and {m(b)} cm, as shown. "
                f"What is the **area of the inscribed circle** (in \\( \\text{{cm}}^2 \\))?"
            )
            q_ar = (
                f"رُسمت دائرة محاطة داخل مثلث قائم الزاوية طولا ساقيه المتعامدتين {m(a)} سم و{m(b)} سم كما في الشكل. "
                f"ما **مساحة الدائرة الداخلية** (بـ \\( \\text{{cm}}^2 \\))؟"
            )
            h_en = f"Find hypotenuse c = √({a}² + {b}²) = {c}, then inradius r = ({a} + {b} − {c})/2 = {r}, then circle area πr²!"
            h_ar = f"أوجد الوتر {m(f'c = {c}')} من فيثاغورس، ثم نصف القطر {m(f'r = \\frac{{{a}+{b}-{c}}}{{2}} = {r}')}، ثم مساحة الدائرة {m('\\pi r^2')}!"
            s_en = explain_en(
                "Three calm steps: Pythagorean theorem for \\( c \\), \\( r = \\frac{a + b - c}{2} \\) for the inradius, and \\( \\pi r^2 \\) for the circle's area!",
                [
                    f"Hypotenuse: {m(f'c = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a*a + b*b}}} = {c}')} cm.",
                    f"Inradius: {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = {r}')} cm.",
                    f"Area of the incircle: {m(f'\\pi r^2 = \\pi ({r}^2) = {ans_tex}\\text{{ cm}}^2')}.",
                ],
                f"Sanity check: \\( {r*r}\\pi \\approx {r*r*3.14:.1f} \\) is strictly less than the triangle's area \\( \\frac{{1}}{{2}}({a})({b}) = {(a*b)//2} \\)!",
            )
            s_ar = explain_ar(
                "ثلاث خطوات مرتبة: فيثاغورس لإيجاد الوتر \\( c \\)، ثم \\( r = \\frac{a + b - c}{2} \\)، ثم مساحة الدائرة \\( \\pi r^2 \\)!",
                [
                    f"نحسب الوتر من فيثاغورس: {m(f'c = \\sqrt{{{a}^2 + {b}^2}} = {c}')} سم.",
                    f"نحسب نصف قطر الدائرة الداخلية: {m(f'r = \\frac{{{a} + {b} - {c}}}{{2}} = {r}')} سم.",
                    f"مساحة الدائرة: {m(f'\\pi r^2 = {ans_tex}\\text{{ cm}}^2')}.",
                ],
                f"تحقق منطقي: مساحة الدائرة \\( \\approx {r*r*3.14:.1f} \\) أصغر فعلاً من مساحة المثلث \\( {(a*b)//2} \\)!",
            )
        elif kind == "inv_perim":
            _, a, b, c, _ = item
            r = (a + b - c) // 2
            ans = a + b + c
            assert ans == 2 * c + 2 * r
            svg = svg_right_tri_incircle("a", "b", str(c), str(r))
            distractors = [2 * c + r, c + 2 * r, 2 * c + 4 * r, 2 * c]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_inc_{v_i}")
            q_en = (
                f"A right triangle has hypotenuse {m(f'c = {c}')} and inscribed circle radius {m(f'r = {r}')}, as shown. "
                f"Without needing the individual leg lengths, what is the **perimeter** of the right triangle?"
            )
            q_ar = (
                f"مثلث قائم الزاوية طول وتره {m(f'c = {c}')} ونصف قطر دائرته الداخلية {m(f'r = {r}')} كما في الشكل. "
                f"ما **محيط** هذا المثلث القائم؟"
            )
            h_en = f"Rearrange r = (a + b − c)/2 into a + b = c + 2r, then add c to get the perimeter a + b + c = 2c + 2r!"
            h_ar = f"أعد ترتيب القانون {m('r = \\frac{a+b-c}{2}')} ليصبح {m('a + b = c + 2r')}، ثم أضف {m('c')} للحصول على المحيط {m('2c + 2r')}!"
            s_en = explain_en(
                "You don't need \\( a \\) and \\( b \\) separately! Since \\( r = \\frac{a + b - c}{2} \\), the sum of the legs is \\( a + b = c + 2r \\), so the perimeter is \\( 2c + 2r \\)!",
                [
                    f"Start from {m(f'r = \\frac{{a + b - c}}{{2}} \\implies a + b = c + 2r = {c} + 2({r}) = {c + 2*r}')}.",
                    f"Add the hypotenuse {m(f'c = {c}')} to find the perimeter {m('a + b + c')}:",
                    f"{m(f'\\text{{Perimeter}} = (a + b) + c = {c + 2*r} + {c} = {ans}')}.",
                ],
                f"Hidden triple check: legs {m(a)} and {m(b)} satisfy {m(f'{a}^2 + {b}^2 = {c}^2')}, {m(f'r = {r}')}, and {m(f'{a}+{b}+{c} = {ans}')}!",
            )
            s_ar = explain_ar(
                "لسنا بحاجة لإيجاد \\( a \\) و\\( b \\) كلّاً على حدة! من \\( r = \\frac{a + b - c}{2} \\) نجد \\( a + b = c + 2r \\)، فيكون المحيط \\( 2c + 2r \\)!",
                [
                    f"من قانون نصف القطر الداخلي: {m(f'a + b = c + 2r = {c} + 2({r}) = {c + 2*r}')}.",
                    f"نضيف طول الوتر {m(f'c = {c}')} لحساب المحيط الكلي:",
                    f"{m(f'a + b + c = {c + 2*r} + {c} = {ans}')}.",
                ],
                f"تحقق: المثلث القائم \\( ({a}, {b}, {c}) \\) يحقق \\( r = {r} \\) ومحيطه \\( {ans} \\) بالضبط!",
            )
        else:
            # inv_area: given c and r, Area = r * s = r * (c + r)
            _, a, b, c, _ = item
            r = (a + b - c) // 2
            ans = (a * b) // 2
            assert ans == r * (c + r)
            svg = svg_right_tri_incircle("a", "b", str(c), str(r))
            distractors = [c * r, 2 * r * (c + r), c * r // 2 if (c * r) % 2 == 0 else ans + r, ans + c]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_inc_{v_i}")
            q_en = (
                f"A right triangle has hypotenuse {m(f'c = {c}')} and inradius {m(f'r = {r}')}, as shown. "
                f"What is the **area** of this right triangle?"
            )
            q_ar = (
                f"مثلث قائم الزاوية طول وتره {m(f'c = {c}')} ونصف قطر دائرته الداخلية {m(f'r = {r}')} كما في الشكل. "
                f"ما **مساحة** هذا المثلث القائم؟"
            )
            h_en = f"Find the semiperimeter s = (a + b + c)/2 = c + r = {c + r} first, then use the universal formula Area = r × s!"
            h_ar = f"أوجد أولاً نصف المحيط {m(f's = c + r = {c + r}')}، ثم استخدم القانون العام للمساحة {m('\\text{Area} = r \\times s')}!"
            s_en = explain_en(
                "Combine \\( a + b = c + 2r \\) (so semiperimeter \\( s = \\frac{a+b+c}{2} = c + r \\)) with \\( \\text{Area} = r \\cdot s = r(c + r) \\)!",
                [
                    f"From {m('2r = a + b - c')}, we get {m(f'a + b + c = 2c + 2r')}, so semiperimeter {m(f's = c + r = {c} + {r} = {c + r}')}.",
                    f"Every polygon circumscribed around a circle of radius {m('r')} has area {m('r \\times s')}.",
                    f"Multiply: {m(f'\\text{{Area}} = {r} \\times {c + r} = {ans}')}.",
                ],
                f"Concrete check with the underlying \\( ({a}, {b}, {c}) \\) right triangle: \\( \\frac{{1}}{{2}}({a})({b}) = {ans} \\)!",
            )
            s_ar = explain_ar(
                "نجمع بين \\( a + b = c + 2r \\) (ومنه نصف المحيط \\( s = c + r \\)) وبين قانون المساحة الشهير \\( \\text{Area} = r \\cdot s = r(c + r) \\)!",
                [
                    f"من {m('a + b = c + 2r')} نجد نصف المحيط {m(f's = \\frac{{a + b + c}}{{2}} = c + r = {c} + {r} = {c + r}')}.",
                    f"مساحة أي مثلث بدلالة نصف قطر دائرته الداخلية ونصف محيطه تساوي {m('r \\times s')}.",
                    f"نضرب: {m(f'\\text{{Area}} = {r} \\times {c + r} = {ans}')}.",
                ],
                f"تحقق عبر المثلث \\( ({a}, {b}, {c}) \\): المساحة \\( \\frac{{1}}{{2}}({a})({b}) = {ans} \\) فعلاً!",
            )
        push(topic, diff, "kmc_g1011_right_triangle_inradius", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)


def _count_bounded_sums(lows: tuple[int, ...], total: int) -> int:
    """Exact recursive enumeration of integer tuples (x_1, ..., x_k) with x_i >= lows[i] summing to total."""
    rem = total - sum(lows)
    if rem < 0:
        return 0
    k = len(lows)
    if k == 1:
        return 1
    cnt = 0
    for first in range(rem + 1):
        cnt += _count_bounded_sums((0,) * (k - 1), rem - first)
    return cnt


def _gen_lesson_3_6(push) -> None:
    topic_comb = "Combinatorics & Logic"
    topic_prob = "Data & Probability"

    # ------------------------------------------------------------------
    # 16. kmc_g1011_stars_and_bars_solutions (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    sb_cases = [
        # ("nonneg_eq", N, k, diff)
        # ("nonneg_box", N, k, item_en, box_en, item_ar, box_ar, diff)
        # ("pos_eq", N, k, diff)
        # ("pos_box", N, k, item_en, box_en, item_ar, box_ar, diff)
        # ("lower", N, lows_tuple, diff)
        # ("ineq", N, k, diff) -> x_1 + ... + x_k <= N in nonneg ints
        ("nonneg_eq", 6, 3, "Easy"),
        ("nonneg_box", 7, 3, "identical marbles", "distinct jars", "كرات زجاجية متطابقة", "مرطبانات متمايزة", "Easy"),
        ("pos_eq", 8, 3, "Easy"),
        ("pos_eq", 9, 4, "Easy"),
        ("pos_box", 10, 3, "identical cookies", "distinct children", "قطع بسكويت متطابقة", "أطفال متمايزين", "Easy"),
        ("nonneg_eq", 8, 4, "Medium"),
        ("nonneg_eq", 10, 3, "Medium"),
        ("nonneg_box", 9, 4, "identical notebooks", "distinct shelves", "دفاتر متطابقة", "رفوف متمايزة", "Medium"),
        ("pos_eq", 11, 4, "Medium"),
        ("pos_eq", 12, 5, "Medium"),
        ("pos_box", 11, 3, "identical gold coins", "distinct treasure chests", "عملات ذهبية متطابقة", "صناديق متمايزة", "Medium"),
        ("lower", 14, (2, 3, 1), "Medium"),
        ("lower", 16, (1, 2, 3, 2), "Medium"),
        ("lower", 20, (3, 4, 2, 1), "Hard"),
        ("ineq", 6, 3, "Hard"),
        ("ineq", 7, 4, "Hard"),
        ("even_pos", 16, 3, "Hard"),      # positive EVEN integers x+y+z=16 -> 2a+2b+2c=16 -> a+b+c=8 (a,b,c>=1) -> C(7,2)=21
    ]
    vars_list = ["x", "y", "z", "w", "u"]
    for v_i, item in enumerate(sb_cases):
        kind = item[0]
        diff = item[-1]
        if kind in ("nonneg_eq", "nonneg_box"):
            N, k = item[1], item[2]
            ans = math.comb(N + k - 1, k - 1)
            if N <= 10 and k <= 4:
                assert _count_bounded_sums((0,) * k, N) == ans
            distractors = [math.comb(N - 1, k - 1) if N >= k else ans - 3, math.comb(N + k, k), ans + k, max(1, ans - k)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_sb_{v_i}")
            v_tex = " + ".join(vars_list[:k])
            if kind == "nonneg_eq":
                q_en = (
                    f"How many ordered {m(k)}-tuples of **non-negative integers** {m(f'({', '.join(vars_list[:k])})')} "
                    f"(where {m('0')} is allowed) satisfy the equation {m(f'{v_tex} = {N}')}?"
                )
                q_ar = (
                    f"كم مرتباً من {m(k)} **أعداد صحيحة غير سالبة** {m(f'({', '.join(vars_list[:k])})')} "
                    f"(يُسمح فيها بالصفر {m('0')}) يحقق المعادلة {m(f'{v_tex} = {N}')}؟"
                )
            else:
                _, _, _, i_en, b_en, i_ar, b_ar, _ = item
                q_en = (
                    f"In how many ways can {m(N)} {i_en} be distributed among {m(k)} {b_en} "
                    f"if some of the {b_en} are allowed to remain empty?"
                )
                q_ar = (
                    f"بكم طريقة يمكن توزيع {m(N)} من {i_ar} على {m(k)} {b_ar} "
                    f"إذا سُمح ببقاء بعضها فارغاً؟"
                )
            h_en = f"Stars and Bars: arrange {N} stars and {k} − 1 = {k-1} dividing bars in a row — that is C({N} + {k-1}, {k-1})!"
            h_ar = f"طريقة النجوم والفواصل: رتّب {N} نجوم مع {m(f'{k}-1 = {k-1}')} فواصل في صف واحد، أي {m(f'\\binom{{{N+k-1}}}{{{k-1}}}')}!"
            s_en = explain_en(
                "By **Stars and Bars**, the number of non-negative integer solutions to \\( x_1 + \\dots + x_k = N \\) equals \\( \\binom{N + k - 1}{k - 1} \\)!",
                [
                    f"Line up {m(N)} identical stars and {m(f'{k} - 1 = {k-1}')} bars that split them into {m(k)} groups (empty groups allowed).",
                    f"There are {m(f'{N} + {k-1} = {N + k - 1}')} total positions, and we choose {m(k - 1)} positions for the bars.",
                    f"Compute {m(f'\\binom{{{N + k - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"Don't confuse non-negative solutions \\( \\binom{{N+k-1}}{{k-1}} = {ans} \\) with positive solutions \\( \\binom{{N-1}}{{k-1}} \\)!",
            )
            s_ar = explain_ar(
                "بطريقة **النجوم والفواصل**، عدد الحلول الصحيحة غير السالبة للمعادلة \\( x_1 + \\dots + x_k = N \\) يساوي \\( \\binom{N + k - 1}{k - 1} \\)!",
                [
                    f"نرتّب {m(N)} نجوم متطابقة مع {m(f'{k} - 1 = {k-1}')} فواصل لتقسيمها إلى {m(k)} خانات (قد تكون إحداها صفراً).",
                    f"لدينا إجمالاً {m(f'{N} + {k-1} = {N + k - 1}')} موضعاً نختار منها {m(k - 1)} مواضع للفواصل.",
                    f"نحسب التوافيق: {m(f'\\binom{{{N + k - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"ميّز دائماً بين السماح بالصفر \\( \\binom{{N+k-1}}{{k-1}} = {ans} \\) واشتراط الموجبية \\( \\binom{{N-1}}{{k-1}} \\)!",
            )
        elif kind in ("pos_eq", "pos_box"):
            N, k = item[1], item[2]
            ans = math.comb(N - 1, k - 1)
            if N <= 12 and k <= 4:
                assert _count_bounded_sums((1,) * k, N) == ans
            distractors = [math.comb(N + k - 1, k - 1), math.comb(N, k - 1), ans + (k - 1), max(1, ans - (k - 1))]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_sb_{v_i}")
            v_tex = " + ".join(vars_list[:k])
            if kind == "pos_eq":
                q_en = (
                    f"How many ordered {m(k)}-tuples of **positive integers** {m(f'({', '.join(vars_list[:k])})')} "
                    f"(each {m('\\ge 1')}) satisfy {m(f'{v_tex} = {N}')}?"
                )
                q_ar = (
                    f"كم مرتباً من {m(k)} **أعداد صحيحة موجبة** {m(f'({', '.join(vars_list[:k])})')} "
                    f"(كل منها {m('\\ge 1')}) يحقق المعادلة {m(f'{v_tex} = {N}')}؟"
                )
            else:
                _, _, _, i_en, b_en, i_ar, b_ar, _ = item
                q_en = (
                    f"In how many ways can {m(N)} {i_en} be given to {m(k)} {b_en} so that **every** recipient receives **at least one**?"
                )
                q_ar = (
                    f"بكم طريقة يمكن توزيع {m(N)} من {i_ar} على {m(k)} {b_ar} بحيث يحصل **كل** منهم على **واحد على الأقل**؟"
                )
            h_en = f"Place {N} stars in a row: there are {N} − 1 = {N-1} interior gaps between them, and choosing {k} − 1 = {k-1} distinct gaps for bars gives C({N-1}, {k-1})!"
            h_ar = f"ضع {N} نجوم في صف: يوجد بينها {m(f'{N}-1 = {N-1}')} فراغات داخلية، نختار منها {m(f'{k}-1 = {k-1}')} لوضع الفواصل، أي {m(f'\\binom{{{N-1}}}{{{k-1}}}')}!"
            s_en = explain_en(
                "For **positive** integer solutions (\\( x_i \\ge 1 \\)), place \\( k - 1 \\) dividers into the \\( N - 1 \\) interior gaps between \\( N \\) stars: \\( \\binom{N - 1}{k - 1} \\)!",
                [
                    f"Draw {m(N)} stars in a line, creating {m(f'{N} - 1 = {N-1}')} interior gaps between adjacent stars.",
                    f"To guarantee every group has at least {m(1)} star, place at most one bar in {m(f'{k} - 1 = {k-1}')} of those gaps.",
                    f"Count the choices: {m(f'\\binom{{{N - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"Equivalently, give {m(1)} to each of the {m(k)} variables first ({m(f'{N} - {k} = {N-k}')} left), then apply non-negative Stars and Bars: \\( \\binom{{{N-k}+{k}-1}}{{{k}-1}} = \\binom{{{N-1}}}{{{k-1}}} = {ans} \\)!",
            )
            s_ar = explain_ar(
                "لإيجاد عدد الحلول الصحيحة **الموجبة** (\\( x_i \\ge 1 \\))، نضع \\( k - 1 \\) فواصل في \\( N - 1 \\) فراغات داخلية بين \\( N \\) نجوم: \\( \\binom{N - 1}{k - 1} \\)!",
                [
                    f"نصفّ {m(N)} نجوم، فيتكون بينها {m(f'{N} - 1 = {N-1}')} فراغاً داخلياً.",
                    f"لضمان حصول كل متغير على {m(1)} على الأقل، نختار {m(f'{k} - 1 = {k-1}')} فراغات مختلفة لوضع الفواصل.",
                    f"نحسب التوافيق: {m(f'\\binom{{{N - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"طريقة مكافئة: أعطِ {m(1)} لكل متغير مسبقاً (يتبقى {m(N - k)})، ثم طبّق قانون الأعداد غير السالبة!",
            )
        elif kind == "lower":
            _, N, lows, _ = item
            k = len(lows)
            rem = N - sum(lows)
            ans = math.comb(rem + k - 1, k - 1)
            assert _count_bounded_sums(lows, N) == ans
            v_names = vars_list[:k]
            v_tex = " + ".join(v_names)
            cond_tex = ",\\; ".join(f"{vn} \\ge {lv}" for vn, lv in zip(v_names, lows))
            distractors = [math.comb(N - 1, k - 1), math.comb(rem - 1, k - 1), ans + rem, max(1, ans - k)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_sb_{v_i}")
            q_en = (
                f"How many integer solutions {m(f'({', '.join(v_names)})')} satisfy {m(f'{v_tex} = {N}')} "
                f"subject to the lower bounds {m(cond_tex)}?"
            )
            q_ar = (
                f"كم حلاً صحيحاً للمرتب {m(f'({', '.join(v_names)})')} يحقق المعادلة {m(f'{v_tex} = {N}')} "
                f"تحت الشروط {m(cond_tex)}؟"
            )
            h_en = f"Pre-fill the minimum required amounts ({' + '.join(str(x) for x in lows)} = {sum(lows)}) first, leaving {N} − {sum(lows)} = {rem} unrestricted units for {k} non-negative variables!"
            h_ar = f"وزّع الحدود الدنيا المطلوبة أولاً ({m(' + '.join(str(x) for x in lows) + f' = {sum(lows)}')})، فيتبقى {m(f'{N} - {sum(lows)} = {rem}')} نطبّق عليها قانون الأعداد غير السالبة!"
            s_en = explain_en(
                "Shift each variable to start at zero: setting \\( y_i = x_i - c_i \\ge 0 \\) reduces \\( x_1 + \\dots + x_k = N \\) to standard non-negative Stars and Bars!",
                [
                    f"Define shifted variables {m(', '.join(f'y_{i+1} = {vn} - {lv} \\ge 0' for i, (vn, lv) in enumerate(zip(v_names, lows))))}.",
                    f"Subtract {m(' + '.join(str(x) for x in lows) + f' = {sum(lows)}')} from {m(N)}: {m(' + '.join(f'y_{i+1}' for i in range(k)) + f' = {N} - {sum(lows)} = {rem}')}.",
                    f"Apply non-negative Stars and Bars for {m(k)} variables summing to {m(rem)}: {m(f'\\binom{{{rem} + {k} - 1}}{{{k} - 1}} = \\binom{{{rem + k - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"Once minimums are pre-paid, the shifted variables \\( y_i \\) can be \\( 0 \\), so use \\( \\binom{{R + k - 1}}{{k - 1}} \\)!",
            )
            s_ar = explain_ar(
                "نزيح كل متغير ليبدأ من الصفر بوضع \\( y_i = x_i - c_i \\ge 0 \\)، فتتحول المسألة إلى نجوم وفواصل قياسية لأعداد غير سالبة!",
                [
                    f"ندفع الحدود الدنيا مسبقاً: مجموعها {m(' + '.join(str(x) for x in lows) + f' = {sum(lows)}')}.",
                    f"المتبقي للتوزيع الحر (مع السماح بالصفر) هو {m(f'{N} - {sum(lows)} = {rem}')} على {m(k)} متغيرات.",
                    f"نطبّق قانون النجوم والفواصل: {m(f'\\binom{{{rem} + {k} - 1}}{{{k} - 1}} = \\binom{{{rem + k - 1}}}{{{k - 1}}} = {ans}')}.",
                ],
                f"انتبه: بعد طرح الحدود الدنيا يُسمح بأن تكون المتغيرات الجديدة أصفاراً!",
            )
        elif kind == "ineq":
            _, N, k, _ = item
            ans = math.comb(N + k, k)
            brute = sum(_count_bounded_sums((0,) * k, s_tot) for s_tot in range(N + 1))
            assert brute == ans
            v_names = vars_list[:k]
            v_tex = " + ".join(v_names)
            distractors = [math.comb(N + k - 1, k - 1), math.comb(N + k - 1, k), ans - N, ans + k]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_sb_{v_i}")
            q_en = (
                f"How many ordered {m(k)}-tuples of **non-negative integers** {m(f'({', '.join(v_names)})')} "
                f"satisfy the **inequality** {m(f'{v_tex} \\le {N}')}?"
            )
            q_ar = (
                f"كم مرتباً من {m(k)} **أعداد صحيحة غير سالبة** {m(f'({', '.join(v_names)})')} "
                f"يحقق **المتباينة** {m(f'{v_tex} \\le {N}')}؟"
            )
            h_en = f"Introduce one extra non-negative 'leftover' (slack) variable s = {N} − ({v_tex}) ≥ 0 to turn ≤ {N} into an exact equation with {k+1} variables!"
            h_ar = f"أضف متغيراً إضافياً غير سالب يمثّل «المتبقي» {m(f's = {N} - ({v_tex}) \\ge 0')} لتحويل المتباينة إلى معادلة دقيقة في {m(k + 1)} متغيرات!"
            s_en = explain_en(
                "The **slack-variable trick** turns \\( x_1 + \\dots + x_k \\le N \\) into the exact equation \\( x_1 + \\dots + x_k + s = N \\) with \\( s \\ge 0 \\)!",
                [
                    f"Define {m(f's = {N} - ({v_tex})')}. Because {m(f'{v_tex} \\le {N}')}, {m('s')} is also a non-negative integer.",
                    f"Every valid {m(k)}-tuple corresponds one-to-one with a non-negative solution to {m(f'{v_tex} + s = {N}')} ({m(k + 1)} variables!).",
                    f"Apply Stars and Bars with {m(k + 1)} variables: {m(f'\\binom{{{N} + ({k+1}) - 1}}{{({k+1}) - 1}} = \\binom{{{N + k}}}{{{k}}} = {ans}')}.",
                ],
                f"Way faster than summing \\( \\binom{{s + {k-1}}}{{{k-1}}} \\) separately for \\( s = 0, 1, \\dots, {N} \\)!",
            )
            s_ar = explain_ar(
                "حيلة **متغير الفائض** تحوّل المتباينة \\( x_1 + \\dots + x_k \\le N \\) فوراً إلى المعادلة \\( x_1 + \\dots + x_k + s = N \\) مع \\( s \\ge 0 \\)!",
                [
                    f"نعرّف المتبقي {m(f's = {N} - ({v_tex}) \\ge 0')}، فيصبح لدينا {m(k + 1)} متغيرات غير سالبة مجموعها {m(N)} بالضبط.",
                    f"نطبّق قانون النجوم والفواصل على {m(k + 1)} متغيرات ومجموع {m(N)}:",
                    f"{m(f'\\binom{{{N} + {k+1} - 1}}{{{k+1} - 1}} = \\binom{{{N + k}}}{{{k}}} = {ans}')}.",
                ],
                f"هذه الحيلة تغنيك عن جمع {m(N + 1)} مسائل منفصلة!",
            )
        else:
            # even_pos: positive EVEN integers x + y + z = 16 -> 2a + 2b + 2c = 16 -> a + b + c = 8 (a,b,c >= 1) -> C(7, 2) = 21
            _, N, k, _ = item
            half_N = N // 2
            ans = math.comb(half_N - 1, k - 1)
            brute = sum(
                1 for x in range(2, N, 2) for y in range(2, N, 2) for z in range(2, N, 2) if x + y + z == N
            )
            assert brute == ans
            distractors = [math.comb(N - 1, k - 1), math.comb(half_N + k - 1, k - 1), ans + 7, ans - 6]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_sb_{v_i}")
            q_en = (
                f"How many ordered triples {m('(x, y, z)')} of **positive even integers** satisfy {m(f'x + y + z = {N}')}?"
            )
            q_ar = (
                f"كم ثلاثية مرتبة {m('(x, y, z)')} من **الأعداد الصحيحة الزوجية الموجبة** تحقق المعادلة {m(f'x + y + z = {N}')}؟"
            )
            h_en = f"Write x = 2a, y = 2b, z = 2c with positive integers a, b, c ≥ 1, then divide the equation by 2 to get a + b + c = {half_N}!"
            h_ar = f"اكتب {m('x = 2a,\\; y = 2b,\\; z = 2c')} بأعداد صحيحة موجبة، ثم اقسم المعادلة على 2 لتحصل على {m(f'a + b + c = {half_N}')}!"
            s_en = explain_en(
                "Factor out \\( 2 \\) from every even variable (\\( x_i = 2a_i \\) with \\( a_i \\ge 1 \\)) to turn an even-integer sum into standard positive Stars and Bars!",
                [
                    f"Set {m('x = 2a,\\; y = 2b,\\; z = 2c')} where {m('a, b, c \\ge 1')} are positive integers.",
                    f"Divide {m(f'2a + 2b + 2c = {N}')} by {m(2)}: {m(f'a + b + c = {half_N}')}.",
                    f"Count positive integer triples summing to {m(half_N)}: {m(f'\\binom{{{half_N} - 1}}{{3 - 1}} = \\binom{{{half_N - 1}}}{{2}} = {ans}')}.",
                ],
                f"Check smallest/largest values: e.g. \\( (2, 2, {N-4}) \\) corresponds to \\( (1, 1, {half_N-2}) \\)!",
            )
            s_ar = explain_ar(
                "بتمثيل كل عدد زوجي موجب على الصورة \\( 2a_i \\) حيث \\( a_i \\ge 1 \\)، تتحول المعادلة بعد القسمة على 2 إلى نجوم وفواصل قياسية!",
                [
                    f"نضع {m('x = 2a,\\; y = 2b,\\; z = 2c')} حيث {m('a, b, c \\ge 1')} أعداد صحيحة موجبة.",
                    f"نقسم المعادلة على {m(2)}: {m(f'a + b + c = {half_N}')}.",
                    f"نحسب عدد الحلول الموجبة: {m(f'\\binom{{{half_N} - 1}}{{3 - 1}} = \\binom{{{half_N - 1}}}{{2}} = {ans}')}.",
                ],
                f"تحقق سريع: الثلاثية \\( (2, 2, {N-4}) \\) تقابل \\( (1, 1, {half_N-2}) \\) وهكذا!",
            )
        push(topic_comb, diff, "kmc_g1011_stars_and_bars_solutions", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 17. kmc_g1011_circular_seating_derangement (17 Qs: 5 Easy, 8 Medium, 4 Hard)
    # ------------------------------------------------------------------
    circ_cases = [
        # ("plain", n, diff)
        # ("adj", n, diff)
        # ("non_adj", n, diff)
        # ("alt", k_half, diff)
        # ("derange", n, exact_fixed, diff)
        ("plain", 5, "Easy"),
        ("plain", 6, "Easy"),
        ("adj", 5, "Easy"),
        ("alt", 2, "Easy"),
        ("derange", 3, 0, "Easy"),
        ("plain", 7, "Medium"),
        ("plain", 8, "Medium"),
        ("adj", 6, "Medium"),
        ("adj", 7, "Medium"),
        ("non_adj", 5, "Medium"),
        ("non_adj", 6, "Medium"),
        ("alt", 3, "Medium"),
        ("derange", 4, 0, "Medium"),
        ("adj", 8, "Hard"),
        ("non_adj", 7, "Hard"),
        ("alt", 4, "Hard"),
        ("derange", 5, 0, "Hard"),
    ]
    for v_i, item in enumerate(circ_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "plain":
            _, n, _ = item
            ans = math.factorial(n - 1)
            brute = sum(1 for _ in itertools.permutations(range(1, n)))
            assert brute == ans
            svg = svg_round_table(n, highlight_adj=False)
            distractors = [math.factorial(n), math.factorial(n - 1) // 2, math.factorial(n - 2), n * (n - 1)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_cir_{v_i}")
            q_en = (
                f"In how many distinct ways can {m(n)} students be seated around the circular table shown "
                f"if two seatings are considered identical whenever one can be rotated into the other?"
            )
            q_ar = (
                f"بكم طريقة مختلفة يمكن جلوس {m(n)} طلاب حول الطاولة الدائرية الموضحة "
                f"إذا اعتُبر الترتيبان متطابقين متى أمكن الحصول على أحدهما بتدوير الآخر؟"
            )
            h_en = f"Fix one student's seat as a reference anchor to eliminate rotations, then arrange the remaining {n} − 1 = {n-1} students in ({n-1})! ways!"
            h_ar = f"ثبّت مقعد طالب واحد كنقطة مرجعية لإلغاء التدوير المتكرر، ثم رتّب الـ {m(n - 1)} الباقين بطرق عددها {m(f'({n-1})!')}!"
            s_en = explain_en(
                "Around a circular table, rotating everyone by \\( 1, 2, \\dots, n \\) seats gives the **same** cyclic arrangement, so \\( \\frac{n!}{n} = (n - 1)! \\)!",
                [
                    f"Seat the first student anywhere to serve as the fixed reference point ({m(1)} choice up to rotation).",
                    f"Arrange the remaining {m(f'{n} - 1 = {n-1}')} students in the remaining seats relative to that student.",
                    f"Compute {m(f'({n - 1})! = {ans}')}.",
                ],
                f"Row vs. circle check: in a straight row it would be \\( {n}! = {math.factorial(n)} \\); dividing by \\( {n} \\) rotations gives \\( {ans} \\)!",
            )
            s_ar = explain_ar(
                "حول طاولة دائرية، كل \\( n \\) تدويرت تمثّل نفس الترتيب الدائري، لذا يكون عدد الترتيبات المختلفة \\( \\frac{n!}{n} = (n - 1)! \\)!",
                [
                    f"نُجلس الطالب الأول في أي مقعد ليكون نقطة مرجعية ثابتة.",
                    f"نرتّب الطلاب الـ {m(n - 1)} المتبقين بالنسبة إليه بطرق عددها {m(f'({n - 1})!')}.",
                    f"نحسب المضروب: {m(f'({n - 1})! = {ans}')}.",
                ],
                f"تذكّر الفرق: في صف مستقيم العدد \\( {n}! \\)، أما حول دائرة فهو \\( ({n}-1)! = {ans} \\)!",
            )
        elif kind == "adj":
            _, n, _ = item
            ans = 2 * math.factorial(n - 2)
            # Brute check with person 0 fixed at index 0, checking person 1 adjacent to 0 in circle of length n
            brute = sum(1 for p in itertools.permutations(range(1, n)) if p[0] == 1 or p[-1] == 1)
            assert brute == ans
            svg = svg_round_table(n, highlight_adj=True)
            distractors = [math.factorial(n - 2), math.factorial(n - 1), 2 * math.factorial(n - 1), ans + math.factorial(n - 3)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_cir_{v_i}")
            q_en = (
                f"{m(n)} delegates sit around a round table (rotations considered identical), as shown. "
                f"In how many ways can they be seated if **two specific friends** (say Omar and Rami) **must sit next to each other**?"
            )
            q_ar = (
                f"يجلس {m(n)} مشاركين حول طاولة مستديرة (مع اعتبار الدورانات متماثلة) كما في الشكل. "
                f"بكم طريقة يمكن جلوسهم إذا اشترط **صديقان محددان** (عمر ورامي مثلاً) **الجلوس متجاورين**؟"
            )
            h_en = f"Glue the two friends into ONE combined block so you arrange {n-1} units around the circle in ({n-2})! ways, then multiply by 2! for their internal left/right order!"
            h_ar = f"ادمج الصديقين في «كتلة واحدة» ليصبح لديك {m(n - 1)} عناصر حول الدائرة بـ {m(f'({n-2})!')} طريقة، ثم اضرب في {m('2!')} لتبديل موضعهما الداخلي!"
            s_en = explain_en(
                "Use the **block (glue) method**: fuse Omar and Rami into 1 unit, seat the \\( n - 1 \\) units around the circle in \\( (n - 2)! \\) ways, and multiply by \\( 2! \\)!",
                [
                    f"Treat {m('\\{\\text{Omar, Rami}\\}')} as a single block alongside the other {m(n - 2)} delegates — {m(n - 1)} objects in total.",
                    f"Circular arrangements of {m(n - 1)} objects: {m(f'({n - 1} - 1)! = ({n - 2})! = {math.factorial(n-2)}')}.",
                    f"Within the block, Omar can sit on Rami's left or right ({m(2)} ways): {m(f'2 \\times {math.factorial(n-2)} = {ans}')}.",
                ],
                f"Alternative check: fix Omar first; Rami has {m(2)} adjacent seats, and the other {m(n-2)} people fill the rest in {m(f'({n-2})!')} ways -> {m(ans)}!",
            )
            s_ar = explain_ar(
                "نستخدم **طريقة الكتلة الواحدة**: ندمج الصديقين في عنصر واحد فيصبح لدينا \\( n - 1 \\) عناصر حول الدائرة، ثم نضرب في \\( 2! \\)!",
                [
                    f"بدمج عمر ورامي معاً يصبح عدد الكيانات حول الطاولة {m(f'{n} - 1 = {n - 1}')}.",
                    f"عدد طرق ترتيب {m(n - 1)} عناصر دائرياً هو {m(f'({n - 2})! = {math.factorial(n-2)}')}.",
                    f"نضرب في {m(2)} (عمر يمين رامي أو يساره): {m(f'2 \\times {math.factorial(n-2)} = {ans}')}.",
                ],
                f"تحقق سريع: ثبّت عمر في مكانه؛ أمام رامي مقعدان مجاوران فقط، ويترتب الباقون بـ {m(f'({n-2})!')} طريقة = {m(ans)}!",
            )
        elif kind == "non_adj":
            _, n, _ = item
            tot_c = math.factorial(n - 1)
            adj_c = 2 * math.factorial(n - 2)
            ans = tot_c - adj_c
            brute = sum(1 for p in itertools.permutations(range(1, n)) if p[0] != 1 and p[-1] != 1)
            assert brute == ans
            svg = svg_round_table(n, highlight_adj=True)
            distractors = [tot_c, adj_c, tot_c - math.factorial(n - 2), ans + math.factorial(n - 3)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_cir_{v_i}")
            q_en = (
                f"{m(n)} people sit around the circular table shown (rotations considered identical). "
                f"In how many ways can they sit if **two specific people must NOT sit adjacent** to each other?"
            )
            q_ar = (
                f"يجلس {m(n)} أشخاص حول الطاولة الدائرية الموضحة (مع اعتبار الدورانات متطابقة). "
                f"بكم طريقة يمكنهم الجلوس إذا اشترطنا **ألا يجلس شخصان محددان متجاورين**؟"
            )
            h_en = f"Complementary counting! Subtract the adjacent seatings 2·({n-2})! = {adj_c} from all circular seatings ({n-1})! = {tot_c}!"
            h_ar = f"استخدم العد بالمتمم! اطرح عدد الترتيبات التي يتجاوران فيها {m(f'2({n-2})! = {adj_c}')} من إجمالي الترتيبات الدائرية {m(f'({n-1})! = {tot_c}')}!"
            s_en = explain_en(
                "For 'NOT adjacent', always use **complementary counting**: \\( \\text{Total} - \\text{Adjacent} = (n - 1)! - 2(n - 2)! \\)!",
                [
                    f"Unrestricted circular seatings of {m(n)} people: {m(f'({n - 1})! = {tot_c}')}.",
                    f"Seatings where the two specific people DO sit together (glue method): {m(f'2 \\times ({n - 2})! = {adj_c}')}.",
                    f"Subtract: {m(f'{tot_c} - {adj_c} = {ans}')}.",
                ],
                f"Seat-choice check: fix person A first; person B can pick any of the {m(n - 3)} non-adjacent seats, and the remaining {m(n - 2)} people arrange in {m(f'({n-2})!')} ways: {m(f'{n-3} \\times {math.factorial(n-2)} = {ans}')}!",
            )
            s_ar = explain_ar(
                "لشرط «عدم التجاور» نستخدم **العد بالمتمم**: نطرح حالات التجاور \\( 2(n - 2)! \\) من العدد الكلي \\( (n - 1)! \\)!",
                [
                    f"إجمالي الترتيبات الدائرية لـ {m(n)} أشخاص: {m(f'({n - 1})! = {tot_c}')}.",
                    f"حالات تجاور الشخصين معاً (طريقة الدمج): {m(f'2 \\times ({n - 2})! = {adj_c}')}.",
                    f"نطرح الحالتين: {m(f'{tot_c} - {adj_c} = {ans}')}.",
                ],
                f"تحقق بديل: ثبّت الأول؛ يتبقى للثاني {m(n - 3)} مقاعد غير مجاورة، ويترتب الباقون بـ {m(f'({n-2})!')} طريقة: {m(f'{n-3} \\times {math.factorial(n-2)} = {ans}')}!",
            )
        elif kind == "alt":
            _, k_h, _ = item
            n = 2 * k_h
            ans = math.factorial(k_h - 1) * math.factorial(k_h)
            # Brute verify: 0..k_h-1 are Group A, k_h..2k_h-1 are Group B; fix person 0 at seat 0
            brute = 0
            for p in itertools.permutations(range(1, n)):
                ring = (0,) + p
                if all((ring[i] < k_h) != (ring[(i + 1) % n] < k_h) for i in range(n)):
                    brute += 1
            assert brute == ans
            svg = svg_round_table(n, highlight_adj=False)
            distractors = [2 * ans, math.factorial(k_h) ** 2, math.factorial(k_h - 1) ** 2, math.factorial(n - 1)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_cir_{v_i}")
            q_en = (
                f"{m(k_h)} physicists and {m(k_h)} mathematicians sit around the {m(n)}-seat circular table shown (rotations considered identical) "
                f"so that physicists and mathematicians **alternate** around the table. How many distinct seatings are possible?"
            )
            q_ar = (
                f"يجلس {m(k_h)} فيزيائيين و{m(k_h)} رياضيين حول الطاولة الدائرية ذات الـ {m(n)} مقاعد الموضحة (مع اعتبار الدورانات متطابقة) "
                f"بحيث **يتناوب** الفيزيائيون والرياضيون مقعداً بمقعد. كم ترتيباً مختلفاً ممكناً؟"
            )
            h_en = f"Seat the {k_h} physicists around the circle FIRST in ({k_h} − 1)! ways; once they sit, the {k_h} gaps between them are now DISTINCT, so seat the {k_h} mathematicians in {k_h}! ways (do NOT multiply by 2)!"
            h_ar = f"أجلس الفيزيائيين الـ {m(k_h)} حول الدائرة أولاً بـ {m(f'({k_h}-1)!')} طريقة؛ عندها تصبح الفراغات الـ {m(k_h)} بينهم **محددة ومميزة** فيجلس الرياضيون بـ {m(f'{k_h}!')} طريقة (دون الضرب في 2)!"
            s_en = explain_en(
                "Seat the first group circularly in \\( (k - 1)! \\) ways; their positions break rotational symmetry, so the second group fills the \\( k \\) gaps in \\( k! \\) ways!",
                [
                    f"Seat the {m(k_h)} physicists around the round table leaving one empty seat between neighbors: {m(f'({k_h} - 1)! = {math.factorial(k_h - 1)}')} ways.",
                    f"Because the physicists are already seated, the {m(k_h)} remaining seats are now distinguishable (e.g., 'between Physicist 1 and Physicist 2').",
                    f"Seat the {m(k_h)} mathematicians in those {m(k_h)} seats in {m(f'{k_h}! = {math.factorial(k_h)}')} ways: {m(f'{math.factorial(k_h-1)} \\times {math.factorial(k_h)} = {ans}')}.",
                ],
                f"Trap check: do NOT multiply by \\( 2 \\) (that works on a straight line, but on a circle rotating by 1 seat already swaps even/odd seats)!",
            )
            s_ar = explain_ar(
                "نُجلس المجموعة الأولى دائرياً بـ \\( (k - 1)! \\) طريقة؛ وبمجرد جلوسهم ينكسر التماثل الدوراني فتترتب المجموعة الثانية في الفراغات الـ \\( k \\) بـ \\( k! \\) طريقة!",
                [
                    f"عدد طرق جلوس الفيزيائيين الـ {m(k_h)} حول الدائرة هو {m(f'({k_h} - 1)! = {math.factorial(k_h - 1)}')}.",
                    f"تصبح المقاعد الـ {m(k_h)} الفارغة بينهم مميّزة تماماً بالنسبة إليهم.",
                    f"يجلس الرياضيون الـ {m(k_h)} في تلك المقاعد بـ {m(f'{k_h}! = {math.factorial(k_h)}')} طريقة: {m(f'{math.factorial(k_h-1)} \\times {math.factorial(k_h)} = {ans}')}.",
                ],
                f"احذر الفخ: لا تضرب في \\( 2 \\) كما في الصف المستقيم، لأن الدوران مقعداً واحداً يغطي التبادل حول الدائرة!",
            )
        else:
            # derangement around numbered seats 1..n (seats ARE labeled 1..n in svg_round_table!)
            _, n, exact_f, _ = item
            ans = sum(
                1 for p in itertools.permutations(range(n))
                if sum(1 for i in range(n) if p[i] == i) == exact_f
            )
            svg = svg_round_table(n, highlight_adj=False)
            distractors = [math.factorial(n) - 1, math.factorial(n - 1), ans + n, max(1, ans - 2), ans + 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_cir_{v_i}")
            q_en = (
                f"Around a conference table, {m(n)} chairs are labeled {m(f'1, 2, \\dots, {n}')} for {m(n)} corresponding guests, as shown. "
                f"If the {m(n)} guests sit down in the {m(n)} numbered chairs so that **no guest sits in their own assigned chair**, how many seatings are possible?"
            )
            q_ar = (
                f"حول طاولة اجتماعات وُضعت {m(n)} مقاعد مرقّمة بالأرقام {m(f'1, 2, \\dots, {n}')} لـ {m(n)} ضيوف مناظرة لها كما في الشكل. "
                f"بكم طريقة يمكن للضيوف الجلوس في المقاعد المرقّمة بحيث **لا يجلس أي ضيف في مقعده المخصّص له**؟"
            )
            h_en = f"Because the chairs are NUMBERED 1..{n}, this is a derangement D_{n}! Remember D₁ = 0, D₂ = 1, D₃ = 2, D₄ = 9, D₅ = 44!"
            h_ar = f"بما أن المقاعد **مرقّمة**، فالمسألة تطلب عدد التبديلات الخالية من النقاط الثابتة {m(f'D_{{{n}}}')}! تذكّر القيم: {m('D_1=0, D_2=1, D_3=2, D_4=9, D_5=44')}!"
            s_en = explain_en(
                "Numbered chairs fix every seat's identity, so we count **derangements** \\( D_n \\) (permutations with zero fixed points), satisfying \\( D_n = (n - 1)(D_{n-1} + D_{n-2}) \\)!",
                [
                    f"Start from the base derangement counts: {m('D_1 = 0')} and {m('D_2 = 1')}.",
                    f"Build up step by step using {m('D_k = (k - 1)(D_{k-1} + D_{k-2})')}: {m('D_3 = 2(1 + 0) = 2')}"
                    + (f", {m('D_4 = 3(2 + 1) = 9')}" if n >= 4 else "")
                    + (f", {m('D_5 = 4(9 + 2) = 44')}" if n >= 5 else "") + ".",
                    f"Thus there are {m(f'D_{{{n}}} = {ans}')} valid derangements.",
                ],
                f"Inclusion-Exclusion check: \\( {n}! \\left(1 - 1 + \\frac{{1}}{{2!}} - \\frac{{1}}{{3!}} " + ("+ \\frac{1}{4!}" if n >= 4 else "") + (" - \\frac{1}{5!}" if n >= 5 else "") + f"\\right) = {ans} \\)!",
            )
            s_ar = explain_ar(
                "ترقيم المقاعد يلغي تماثل الدوران ويجعل المطلوب هو **التبديلات التامة الإزاحة** \\( D_n \\) التي تحقق العلاقة \\( D_n = (n - 1)(D_{n-1} + D_{n-2}) \\)!",
                [
                    f"نبدأ بالقيم الأساسية السهلة: {m('D_1 = 0')} و{m('D_2 = 1')}.",
                    f"نحسب بالتدريج: {m('D_3 = 2(1 + 0) = 2')}"
                    + (f"، و{m('D_4 = 3(2 + 1) = 9')}" if n >= 4 else "")
                    + (f"، و{m('D_5 = 4(9 + 2) = 44')}" if n >= 5 else "") + ".",
                    f"إذن عدد الترتيبات المطلوبة يساوي {m(f'D_{{{n}}} = {ans}')}.",
                ],
                f"أكثر من ثلث التبديلات بقليل (\\( \\approx n!/e \\)): \\( {math.factorial(n)} / 2.718 \\approx {math.factorial(n)/math.e:.1f} \\)، والأقرب هو {m(ans)}!",
            )
        push(topic_comb, diff, "kmc_g1011_circular_seating_derangement", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 18. kmc_g1011_geometric_interval_prob (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # Topic: "Data & Probability", diagram_en=svg_coord_diamond(...)
    # ZERO calculus! Pure elementary areas!
    # ------------------------------------------------------------------
    prob_cases = [
        # ("sq_to_dia", R, r, diff) -> point in [-R, R]^2 lands in |x|+|y| <= r: prob = 2*r^2 / (4*R^2) = r^2 / (2*R^2)
        # ("dia_to_dia", R, r, outside, diff) -> point in |x|+|y| <= R lands in |x|+|y| <= r (or >= r)
        # ("meet", T, w, miss, diff) -> two friends in [0, T], wait w: meet = 1 - ((T-w)/T)^2
        # ("quad_sum", T, s, diff) -> x, y in [0, T], prob x + y <= s (for s <= T: s^2 / (2*T^2))
        # ("pi_shape", mode, R, diff) -> inscribed diamond in circle (2/pi) or inscribed circle in diamond (pi/4)
        ("sq_to_dia", 4, 4, "Easy"),
        ("dia_to_dia", 6, 3, False, "Easy"),
        ("meet", 60, 30, False, "Easy"),
        ("meet", 20, 10, True, "Easy"),
        ("quad_sum", 10, 6, "Easy"),
        ("sq_to_dia", 6, 4, "Medium"),
        ("sq_to_dia", 5, 3, "Medium"),
        ("dia_to_dia", 10, 6, True, "Medium"),
        ("meet", 60, 15, False, "Medium"),
        ("meet", 60, 20, False, "Medium"),
        ("meet", 40, 10, False, "Medium"),
        ("meet", 45, 15, False, "Medium"),
        ("meet", 60, 10, False, "Hard"),
        ("quad_sum_hi", 10, 14, "Hard"),   # x, y in [0, 10], prob x + y <= 14 -> 1 - (20-14)^2 / (2*100) = 1 - 36/200 = 41/50!
        ("pi_shape", "dia_in_cir", 6, "Hard"),
        ("pi_shape", "cir_in_dia", 8, "Hard"),
    ]
    for v_i, item in enumerate(prob_cases):
        kind = item[0]
        diff = item[-1]
        if kind == "sq_to_dia":
            _, R, r, _ = item
            svg = svg_coord_diamond(str(r))
            sq_area = 4 * R * R
            dia_area = 2 * r * r
            ans = Fraction(dia_area, sq_area)
            assert ans == Fraction(r * r, 2 * R * R)
            distractors = [Fraction(r * r, R * R) if r < R else Fraction(1, 4), Fraction(r, 2 * R), 1 - ans, Fraction(dia_area, R * R) if dia_area < R * R else Fraction(3, 4)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_prb_{v_i}")
            q_en = (
                f"A point {m('(x, y)')} is chosen uniformly at random inside the square {m(f'-{R} \\le x \\le {R},\\; -{R} \\le y \\le {R}')}. "
                f"What is the probability that it lands inside the diamond region {m(f'|x| + |y| \\le {r}')} (shown)?"
            )
            q_ar = (
                f"اختيرت نقطة {m('(x, y)')} عشوائياً بانتظام داخل المربع {m(f'-{R} \\le x \\le {R},\\; -{R} \\le y \\le {R}')}. "
                f"ما احتمال وقوعها داخل المنطقة المعيّنية {m(f'|x| + |y| \\le {r}')} الموضحة في الشكل؟"
            )
            h_en = f"Divide the target diamond area (2 × {r}² = {dia_area}) by the full square area ((2×{R})² = {sq_area})!"
            h_ar = f"اقسم مساحة المعين المطلوب ({m(f'2 \\times {r}^2 = {dia_area}')}) على المساحة الكلية للمربع ({m(f'(2 \\times {R})^2 = {sq_area}')})!"
            s_en = explain_en(
                "Geometric probability is simply \\( \\frac{\\text{Favorable Area}}{\\text{Total Area}} \\)!",
                [
                    f"The square {m(f'[-{R}, {R}] \\times [-{R}, {R}]')} has side length {m(2 * R)}, so its total area is {m(f'({2*R})^2 = {sq_area}')}.",
                    f"The diamond {m(f'|x| + |y| \\le {r}')} has diagonals {m(2 * r)} and {m(2 * r)}, so its area is {m(f'2({r}^2) = {dia_area}')}.",
                    f"Divide areas and simplify: {m(f'\\frac{{{dia_area}}}{{{sq_area}}} = {fmt_val(ans)}')}.",
                ],
                f"Trap check: the square from \\( -{R} \\) to \\( +{R} \\) has side \\( {2*R} \\) (area \\( {sq_area} \\), NOT \\( {R*R} \\))!",
            )
            s_ar = explain_ar(
                "الاحتمال الهندسي المنتظم يساوي نسبة **المساحة المواتية** إلى **المساحة الكلية**!",
                [
                    f"طول ضلع المربع الممتد من {m(-R)} إلى {m(R)} هو {m(2 * R)}، فمساحته الكلية {m(f'({2*R})^2 = {sq_area}')}.",
                    f"مساحة المعين {m(f'|x| + |y| \\le {r}')} تساوي {m(f'2({r}^2) = {dia_area}')}.",
                    f"نحسب الاحتمال بالتبسيط: {m(f'\\frac{{{dia_area}}}{{{sq_area}}} = {fmt_val(ans)}')}.",
                ],
                f"احذر الفخ: طول ضلع المربع هو {m(2 * R)} وليس {m(R)}!",
            )
        elif kind == "dia_to_dia":
            _, R, r, outside, _ = item
            svg = svg_coord_diamond(str(R))
            inner_frac = Fraction(r * r, R * R)
            ans = 1 - inner_frac if outside else inner_frac
            distractors = [Fraction(r, R), 1 - Fraction(r, R), 1 - ans, Fraction(r * r, 2 * R * R)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_prb_{v_i}")
            cond_tex = f"|x| + |y| \\ge {r}" if outside else f"|x| + |y| \\le {r}"
            q_en = (
                f"A point {m('(x, y)')} is selected uniformly at random inside the diamond {m(f'|x| + |y| \\le {R}')} shown. "
                f"What is the probability that {m('(x, y)')} satisfies {m(cond_tex)}?"
            )
            q_ar = (
                f"اختيرت نقطة {m('(x, y)')} عشوائياً بانتظام داخل المعين {m(f'|x| + |y| \\le {R}')} الموضح في الشكل. "
                f"ما احتمال أن تحقق النقطة المتباينة {m(cond_tex)}؟"
            )
            h_en = f"Concentric similar diamonds have areas proportional to the SQUARE of their radii: ({r}/{R})² = {fmt_val(inner_frac)}" + (" — then subtract from 1!" if outside else "!")
            h_ar = f"المعينان المتحدان في المركز متشابهان، فنسبة مساحتيهما تساوي مربع نسبة البعدين {m(f'({r}/{R})^2 = {fmt_val(inner_frac)}')}" + (" ثم اطرح من 1!" if outside else "!")
            s_en = explain_en(
                "Scaling a shape by \\( r/R \\) scales its area by \\( (r/R)^2 \\)!",
                [
                    f"Outer diamond {m(f'|x| + |y| \\le {R}')} has area {m(f'2({R}^2) = {2*R*R}')}; inner diamond {m(f'|x| + |y| \\le {r}')} has area {m(f'2({r}^2) = {2*r*r}')}.",
                    f"Inner probability is {m(f'\\frac{{2({r}^2)}}{{2({R}^2)}} = \\left(\\frac{{{r}}}{{{R}}}\\right)^2 = {fmt_val(inner_frac)}')}.",
                    f"Desired probability: {m(f'1 - {fmt_val(inner_frac)} = {fmt_val(ans)}' if outside else fmt_val(ans))}.",
                ],
                f"Always square the linear ratio \\( {r}/{R} \\) when comparing 2D areas!",
            )
            s_ar = explain_ar(
                "بما أن المعينين متشابهان بنسبة تشابه \\( r/R \\)، فإن نسبة المساحة تساوي مربع النسبة \\( (r/R)^2 \\)!",
                [
                    f"مساحة المعين الكبير {m(f'2({R}^2) = {2*R*R}')} ومساحة المعين الصغير {m(f'2({r}^2) = {2*r*r}')}.",
                    f"احتمال الوقوع في المعين الداخلي هو {m(f'\\frac{{{2*r*r}}}{{{2*R*R}}} = {fmt_val(inner_frac)}')}.",
                    f"الاحتمال المطلوب: {m(f'1 - {fmt_val(inner_frac)} = {fmt_val(ans)}' if outside else fmt_val(ans))}.",
                ],
                f"تذكّر تربيع النسبة الخطية \\( {r}/{R} \\) عند حساب نسب المساحات!",
            )
        elif kind == "meet":
            _, T, w, ask_miss, _ = item
            svg = svg_coord_diamond(str(w))
            miss_prob = Fraction((T - w) ** 2, T * T)
            ans = miss_prob if ask_miss else 1 - miss_prob
            distractors = [Fraction(w, T), Fraction(2 * w, T) if 2 * w < T else Fraction(w * w, T * T), 1 - ans, Fraction(T - w, T)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_prb_{v_i}")
            outcome_en = "**fail to meet**" if ask_miss else "**meet each other**"
            outcome_ar = "**لا يلتقيا**" if ask_miss else "**يلتقيا**"
            q_en = (
                f"Two friends independently arrive at a café at random times uniformly distributed over a {m(T)}-minute window {m(f'[0, {T}]')}. "
                f"Each person waits {m(w)} minutes for the other before leaving (so they meet if {m(f'|x - y| \\le {w}')}, using {m('L_1')} distance geometry like the reference figure). "
                f"What is the probability that they {outcome_en}?"
            )
            q_ar = (
                f"يصل صديقان بشكل مستقل وعشوائي بانتظام إلى مقهى خلال فترة زمنية طولها {m(T)} دقيقة {m(f'[0, {T}]')}. "
                f"ينتظر كل منهما الآخر لمدة {m(w)} دقيقة قبل المغادرة (أي يلتقيان إذا كان {m(f'|x - y| \\le {w}')}). "
                f"ما احتمال أن {outcome_ar}؟"
            )
            h_en = f"Plot arrival times (x, y) in a {T} × {T} square! Missing each other (|x − y| > {w}) forms TWO corner right triangles of leg {T} − {w} = {T-w}, which fit together into a ({T-w}) × ({T-w}) square!"
            h_ar = f"مثّل وقتي الوصول {m('(x, y)')} في مربع {m(f'{T} \\times {T}')}! حالة عدم اللقاء تكوّن مثلثين قائمين في الركنين طول ساق كل منهما {m(f'{T} - {w} = {T-w}')} مجموع مساحتيهما {m(f'({T-w})^2')}!"
            s_en = explain_en(
                "Plot arrival times \\( (x, y) \\in [0, T] \\times [0, T] \\) (area \\( T^2 \\)). The 'miss' region \\( |x - y| > w \\) consists of two congruent corner right triangles of leg \\( T - w \\), whose combined area is \\( (T - w)^2 \\)!",
                [
                    f"Total sample-space square area: {m(f'{T} \\times {T} = {T*T}')}.",
                    f"They miss each other when {m(f'x - y > {w}')} or {m(f'y - x > {w}')}: two isosceles right triangles of leg {m(f'{T} - {w} = {T - w}')}, combined area {m(f'2 \\times \\frac{{1}}{{2}}({T-w})^2 = {(T-w)**2}')}.",
                    f"Miss probability is {m(f'\\frac{{{(T-w)**2}}}{{{T*T}}} = {fmt_val(miss_prob)}')}"
                    + ("." if ask_miss else f", so meeting probability is {m(f'1 - {fmt_val(miss_prob)} = {fmt_val(ans)}')}.")
                ],
                f"Never guess \\( \\frac{{w}}{{T}} = {fmt_val(Fraction(w, T))} \\) or \\( \\frac{{2w}}{{T}} \\) — always subtract the two corner triangles!",
            )
            s_ar = explain_ar(
                "نمثّل زمني الوصول \\( (x, y) \\) داخل المربع \\( [0, T]^2 \\) الذي مساحته \\( T^2 \\)؛ منطقة عدم اللقاء \\( |x - y| > w \\) هي مثلثان قائمان في الركنين طول ساق كل منهما \\( T - w \\) ومجموع مساحتيهما \\( (T - w)^2 \\)!",
                [
                    f"المساحة الكلية لمربع الفضاء العيني: {m(f'{T}^2 = {T*T}')}.",
                    f"مساحة مثلثي عدم اللقاء معاً: {m(f'2 \\times \\frac{{1}}{{2}}({T} - {w})^2 = ({T-w})^2 = {(T-w)**2}')}.",
                    f"احتمال عدم اللقاء هو {m(f'\\frac{{{(T-w)**2}}}{{{T*T}}} = {fmt_val(miss_prob)}')}"
                    + ("." if ask_miss else f"، ومنه احتمال اللقاء هو {m(f'1 - {fmt_val(miss_prob)} = {fmt_val(ans)}')}.")
                ],
                f"ضمّ المثلثين الركنيين معاً يعطيك مربعاً كاملاً طول ضلعه \\( {T - w} \\) بلمح البصر!",
            )
        elif kind == "quad_sum":
            _, T, s, _ = item
            svg = svg_coord_diamond(str(s))
            ans = Fraction(s * s, 2 * T * T)
            distractors = [Fraction(s, T), Fraction(s * s, T * T), Fraction(s, 2 * T), 1 - ans]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_prb_{v_i}")
            q_en = (
                f"Two real numbers {m('x')} and {m('y')} are chosen independently and uniformly at random from the interval {m(f'[0, {T}]')}. "
                f"What is the probability that {m(f'x + y \\le {s}')} (the first-quadrant corner of {m(f'|x| + |y| \\le {s}')} shown)?"
            )
            q_ar = (
                f"اختير عددان حقيقيان {m('x')} و{m('y')} بشكل مستقل وعشوائي بانتظام من الفترة {m(f'[0, {T}]')}. "
                f"ما احتمال تحقق {m(f'x + y \\le {s}')} (الربع الأول من المعين {m(f'|x| + |y| \\le {s}')} الموضح)؟"
            )
            h_en = f"Inside the {T} × {T} square (area {T*T}), the condition x + y ≤ {s} with x, y ≥ 0 is a right triangle of legs {s} and {s} (area ½ × {s}²)!"
            h_ar = f"داخل المربع {m(f'{T} \\times {T}')}، تمثّل المتباينة {m(f'x + y \\le {s}')} مثلثاً قائماً في الركن الأيسر السفلي ساقاه {s} و{s} ومساحته {m(f'\\frac{{1}}{{2}} \\times {s}^2')}!"
            s_en = explain_en(
                "For \\( 0 \\le s \\le T \\), the region \\( x, y \\ge 0,\\; x + y \\le s \\) is a right triangle of area \\( \\frac{1}{2}s^2 \\) inside the \\( T \\times T \\) square!",
                [
                    f"Total area of the sample space {m(f'[0, {T}] \\times [0, {T}]')}: {m(f'{T}^2 = {T*T}')}.",
                    f"Favorable region {m(f'x + y \\le {s}')} has legs {m(s)} and {m(s)}, so its area is {m(f'\\frac{{1}}{{2}}({s})({s}) = {Fraction(s*s, 2)}')}.",
                    f"Divide areas: {m(f'\\frac{{{s}^2 / 2}}{{{T}^2}} = \\frac{{{s*s}}}{{{2*T*T}}} = {fmt_val(ans)}')}.",
                ],
                f"Check at \\( s = {T} \\): the formula gives \\( \\frac{{{T}^2}}{{2{T}^2}} = \\frac{{1}}{{2}} \\), matching the diagonal half-square!",
            )
            s_ar = explain_ar(
                "عندما يكون \\( 0 \\le s \\le T \\)، تحدد المتباينة \\( x + y \\le s \\) في الربع الأول مثلثاً قائماً مساحته \\( \\frac{1}{2}s^2 \\) داخل مربع مساحته \\( T^2 \\)!",
                [
                    f"مساحة مربع الفضاء العيني {m(f'[0, {T}]^2')}: {m(f'{T}^2 = {T*T}')}.",
                    f"مساحة المثلث القائم المواتي: {m(f'\\frac{{1}}{{2}} \\times {s} \\times {s} = \\frac{{{s*s}}}{{2}}')}.",
                    f"نقسم المساحتين: {m(f'\\frac{{{s*s}}}{{{2*T*T}}} = {fmt_val(ans)}')}.",
                ],
                f"تحقق حدّي: لو كانت \\( s = {T} \\) لأصبح الاحتمال \\( \\frac{{1}}{{2}} \\) تماماً!",
            )
        elif kind == "quad_sum_hi":
            _, T, s, _ = item
            # T < s < 2T: complement x + y > s inside [0, T]^2 is a top-right right triangle of leg (2T - s)!
            leg = 2 * T - s
            svg = svg_coord_diamond(str(T))
            ans = 1 - Fraction(leg * leg, 2 * T * T)
            distractors = [Fraction(s, 2 * T), Fraction(leg * leg, 2 * T * T), Fraction(s * s, 2 * T * T) if s * s < 2 * T * T else Fraction(7, 10), Fraction(4, 5)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3x_prb_{v_i}")
            q_en = (
                f"Two real numbers {m('x')} and {m('y')} are chosen independently and uniformly from {m(f'[0, {T}]')}. "
                f"What is the probability that their sum satisfies {m(f'x + y \\le {s}')}?"
            )
            q_ar = (
                f"اختير عددان حقيقيان {m('x')} و{m('y')} بشكل مستقل وعشوائي بانتظام من الفترة {m(f'[0, {T}]')}. "
                f"ما احتمال أن يحقق مجموعهما المتباينة {m(f'x + y \\le {s}')}؟"
            )
            h_en = f"Careful: since {s} > {T}, the line x + y = {s} clips the TOP-RIGHT corner of [0, {T}]²! Subtract that small corner right triangle of leg 2({T}) − {s} = {leg} from the square!"
            h_ar = f"انتبه: بما أن {m(f'{s} > {T}')}، فإن المستقيم {m(f'x + y = {s}')} يقتطع مثلثاً صغيراً في الركن العلوي الأيمن طول ساقه {m(f'2({T}) - {s} = {leg}')}! استخدم المتمم!"
            s_en = explain_en(
                "When \\( T < s < 2T \\), \\( x + y \\le s \\) covers the entire \\( T \\times T \\) square EXCEPT a small right triangle in the top-right corner of leg \\( 2T - s \\)!",
                [
                    f"The complement {m(f'x + y > {s}')} inside {m(f'[0, {T}]^2')} has vertices {m(f'({s-T}, {T})')}, {m(f'({T}, {s-T})')}, and {m(f'({T}, {T})')}.",
                    f"Its legs each have length {m(f'{T} - ({s - T}) = 2({T}) - {s} = {leg}')}, so its area is {m(f'\\frac{{1}}{{2}}({leg}^2) = {leg*leg // 2}')}.",
                    f"Subtract from total area {m(T*T)}: {m(f'1 - \\frac{{{leg*leg // 2}}}{{{T*T}}} = {fmt_val(ans)}')}.",
                ],
                f"Trap check: \\( \\frac{{s^2}}{{2T^2}} = \\frac{{{s*s}}}{{{2*T*T}}} \\) fails when \\( s > T \\) because the triangle sticks outside the \\( [0, T]^2 \\) square!",
            )
            s_ar = explain_ar(
                "عندما يكون \\( T < s < 2T \\)، تغطي المنطقة \\( x + y \\le s \\) المربع \\( [0, T]^2 \\) بالكامل ما عدا مثلثاً قائماً صغيراً في الركن العلوي الأيمن طول ساقه \\( 2T - s \\)!",
                [
                    f"المنطقة المتممة {m(f'x + y > {s}')} تقع قرب الركن {m(f'({T}, {T})')} برؤوس {m(f'({s-T}, {T})')} و{m(f'({T}, {s-T})')} و{m(f'({T}, {T})')}.",
                    f"طول كل ساق من ساقي هذا المثلث يساوي {m(f'{T} - {s - T} = {leg}')}، ومساحته {m(f'\\frac{{1}}{{2}}({leg}^2) = {leg*leg // 2}')}.",
                    f"نحسب الاحتمال بالمتمم: {m(f'1 - \\frac{{{leg*leg // 2}}}{{{T*T}}} = {fmt_val(ans)}')}.",
                ],
                f"احذر استخدام \\( \\frac{{s^2}}{{2T^2}} \\) عندما \\( s > T \\)، فالمثلث الكبير يتجاوز حدود المربع!",
            )
        else:
            _, sub, R, _ = item
            svg = svg_coord_diamond(str(R))
            if sub == "dia_in_cir":
                ans_tex = "\\frac{2}{\\pi}"
                d_list = ["\\frac{1}{\\pi}", "\\frac{\\pi}{4}", "\\frac{1}{2}", "\\frac{4}{\\pi}"]
                q_en = (
                    f"A point {m('(x, y)')} is chosen uniformly at random inside the disk {m(f'x^2 + y^2 \\le {R*R}')} of radius {m(R)}. "
                    f"What is the probability that it lies inside the inscribed diamond {m(f'|x| + |y| \\le {R}')} shown?"
                )
                q_ar = (
                    f"اختيرت نقطة {m('(x, y)')} عشوائياً بانتظام داخل القرص الدائري {m(f'x^2 + y^2 \\le {R*R}')} ذي نصف القطر {m(R)}. "
                    f"ما احتمال وقوعها داخل المعين المحاط {m(f'|x| + |y| \\le {R}')} الموضح في الشكل؟"
                )
                h_en = f"Divide the diamond's area (2R² = {2*R*R}) by the circle's area (πR² = {R*R}π) — notice R² cancels completely!"
                h_ar = f"اقسم مساحة المعين ({m(f'2R^2 = {2*R*R}')}) على مساحة الدائرة ({m(f'\\pi R^2 = {R*R}\\pi')}) — لاحظ اختصار {m('R^2')} بالكامل!"
                s_en = explain_en(
                    "The vertices \\( (\\pm R, 0), (0, \\pm R) \\) lie right on \\( x^2 + y^2 = R^2 \\), so the diamond is inscribed in the circle and \\( R^2 \\) cancels in the area ratio!",
                    [
                        f"Circle area: {m(f'\\pi R^2 = {R*R}\\pi')}.",
                        f"Inscribed diamond {m(f'|x| + |y| \\le {R}')} area: {m(f'2R^2 = {2*R*R}')}.",
                        f"Probability: {m(f'\\frac{{{2*R*R}}}{{{R*R}\\pi}} = \\frac{{2}}{{\\pi}}')}.",
                    ],
                    f"Numeric sanity check: \\( \\frac{{2}}{{\\pi}} \\approx 0.637 \\), nicely between \\( 0 \\) and \\( 1 \\)!",
                )
                s_ar = explain_ar(
                    "تقع رؤوس المعين \\( (\\pm R, 0) \\) و\\( (0, \\pm R) \\) على محيط الدائرة \\( x^2 + y^2 = R^2 \\) تماماً، وعند قسمة المساحتين تختصر \\( R^2 \\)!",
                    [
                        f"مساحة الدائرة الكلية: {m(f'\\pi R^2 = {R*R}\\pi')}.",
                        f"مساحة المعين المحاط {m(f'|x| + |y| \\le {R}')}: {m(f'2R^2 = {2*R*R}')}.",
                        f"الاحتمال: {m(f'\\frac{{{2*R*R}}}{{{R*R}\\pi}} = \\frac{{2}}{{\\pi}}')}.",
                    ],
                    f"تحقق عددي: \\( \\frac{{2}}{{\\pi}} \\approx 0.637 < 1 \\)!",
                )
            else:
                # circle inscribed in diamond |x| + |y| <= R: side of diamond is R*sqrt(2), inradius of that tilted square is half its side = R/sqrt(2), circle area = pi * R^2 / 2, diamond area = 2*R^2 => ratio = pi / 4!
                r_sq = (R * R) // 2
                ans_tex = "\\frac{\\pi}{4}"
                d_list = ["\\frac{\\pi}{2}", "\\frac{2}{\\pi}", "\\frac{\\pi}{8}", "\\frac{1}{2}"]
                q_en = (
                    f"A point {m('(x, y)')} is chosen uniformly at random inside the diamond {m(f'|x| + |y| \\le {R}')} shown. "
                    f"What is the probability that it lands inside the largest circle centered at the origin that fits inside the diamond ({m(f'x^2 + y^2 \\le {r_sq}')})?"
                )
                q_ar = (
                    f"اختيرت نقطة {m('(x, y)')} عشوائياً بانتظام داخل المعين {m(f'|x| + |y| \\le {R}')} الموضح في الشكل. "
                    f"ما احتمال وقوعها داخل أكبر دائرة مركزها نقطة الأصل تقع بالكامل داخل المعين ({m(f'x^2 + y^2 \\le {r_sq}')})؟"
                )
                h_en = f"The diamond |x| + |y| ≤ {R} IS a tilted square of area 2×{R}² = {2*R*R}, and any circle inscribed in ANY square occupies exactly π/4 of its area!"
                h_ar = f"المعين {m(f'|x| + |y| \\le {R}')} ما هو إلا **مربع مائل** مساحته {m(2*R*R)}، والدائرة المرسومة داخل أي مربع تشغل دائماً الكسر {m('\\frac{\\pi}{4}')} من مساحته!"
                s_en = explain_en(
                    "Because \\( |x| + |y| \\le R \\) is a tilted square of side \\( R\\sqrt{2} \\), its inscribed circle has diameter \\( R\\sqrt{2} \\) (radius \\( r = \\frac{R}{\\sqrt{2}} \\)) and covers \\( \\frac{\\pi}{4} \\) of the square!",
                    [
                        f"Diamond area: {m(f'2({R}^2) = {2*R*R}')}.",
                        f"Inscribed circle {m(f'x^2 + y^2 \\le {r_sq}')} has {m(f'r^2 = {r_sq}')}, so its area is {m(f'{r_sq}\\pi')}.",
                        f"Divide areas: {m(f'\\frac{{{r_sq}\\pi}}{{{2*R*R}}} = \\frac{{\\pi}}{{4}}')}.",
                    ],
                    f"Universal invariant: a circle tangent to all 4 sides of ANY square always covers \\( \\frac{{\\pi r^2}}{{(2r)^2}} = \\frac{{\\pi}}{{4}} \\approx 78.5\\% \\)!",
                )
                s_ar = explain_ar(
                    "المنطقة \\( |x| + |y| \\le R \\) هي مربع مائل طول ضلعه \\( R\\sqrt{2} \\)، لذا فإن قطر دائرته الداخلية يساوي طول ضلعه، أي \\( r^2 = \\frac{R^2}{2} \\)!",
                    [
                        f"مساحة المعين (المربع المائل): {m(f'2({R}^2) = {2*R*R}')}.",
                        f"مساحة الدائرة الداخلية {m(f'x^2 + y^2 \\le {r_sq}')} تساوي {m(f'{r_sq}\\pi')}.",
                        f"بقسمة المساحتين نجد الاحتمال: {m(f'\\frac{{{r_sq}\\pi}}{{{2*R*R}}} = \\frac{{\\pi}}{{4}}')}.",
                    ],
                    f"حقيقة هندسية عامة: الدائرة المحاطة بأي مربع تشغل دائماً \\( \\frac{{\\pi}}{{4}} \\) من مساحته!",
                )
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3x_prb_{v_i}")
        push(topic_prob, diff, "kmc_g1011_geometric_interval_prob", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)


def generate_t3_extra() -> list[dict]:
    """Generate all 300 verified Track 3 (Grades 10-11) expansion questions."""
    out: list[dict] = []
    idx = 1

    def push(topic, diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en=None, svg_ar=None):
        nonlocal idx
        qid = f"KMC-T3-EXT-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg_en, svg_ar,
            )
        )

    _gen_lesson_3_1(push)
    _gen_lesson_3_2(push)
    _gen_lesson_3_3(push)
    _gen_lesson_3_4(push)
    _gen_lesson_3_5(push)
    _gen_lesson_3_6(push)

    assert len(out) == 300, f"Expected 300 Track 3 extra questions, got {len(out)}"
    return out


generate = generate_t3_extra
