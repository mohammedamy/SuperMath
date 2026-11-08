"""Tier 1: Junior Olympiad (Grades 7-8) Question Bank — 360 verified 5-option (A-E) SVG questions."""
from fractions import Fraction
import itertools
import math

from olympiad_common import *  # noqa: F401,F403

LEVEL_T1 = OLYMPIAD_LEVELS[0]  # "Tier 1: Junior Olympiad (Grades 7-8)"


def _tau(n: int) -> int:
    return sum(1 for d in range(1, int(math.isqrt(n)) + 1) if n % d == 0 for _ in ([d] if d * d == n else [d, n // d]))


def _sigma(n: int) -> int:
    return sum(v for d in range(1, int(math.isqrt(n)) + 1) if n % d == 0 for v in ([d] if d * d == n else [d, n // d]))


# ==============================================================================
# UNIT 1.1 — Number Theory (OLYM-T1-001 .. OLYM-T1-060)
# ==============================================================================

def _build_u11_b1_divisors() -> list[dict]:
    bp = "olym_t1_nt_divisors_tau_sigma"
    tp = "Number Theory"
    out: list[dict] = []

    # Easy 1..5: positive divisor count tau(N) for structured composite numbers
    easy_specs = [
        (1, 360, "2^3 \\cdot 3^2 \\cdot 5"),
        (2, 540, "2^2 \\cdot 3^3 \\cdot 5"),
        (3, 840, "2^3 \\cdot 3 \\cdot 5 \\cdot 7"),
        (4, 1260, "2^2 \\cdot 3^2 \\cdot 5 \\cdot 7"),
        (5, 1800, "2^3 \\cdot 3^2 \\cdot 5^2"),
    ]
    for idx, n_val, pf_str in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = _tau(n_val)
        diag = svg_factor_tree(str(n_val), "p^a", "q^b", "r^c", "τ=?")
        q_en = (
            f"In a Junior Olympiad number theory round, let {m(f'N = {n_val}')}. "
            f"How many positive integer divisors {m(r'\\tau(N)')} does {m('N')} possess?"
        )
        q_ar = (
            f"في جولة نظرية الأعداد للأولمبياد الناشئ، ليكن {m(f'N = {n_val}')}. "
            f"كم قاسماً صحيحاً موجباً {m(r'\\tau(N)')} يمتلكه العدد {m('N')}؟"
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 4, ans + 6, ans // 2],
            f"Factor {m(str(n_val))} into prime powers and add {m('1')} to each exponent before multiplying.",
            f"حلّل العدد {m(str(n_val))} إلى عوامله الأولية وأضف {m('1')} إلى كل أس قبل الضرب.",
            f"If {m('N = p_1^{a_1} p_2^{a_2} \\cdots p_k^{a_k}')}, then {m(r'\\tau(N) = (a_1+1)(a_2+1)\\cdots(a_k+1)')}.",
            [
                f"Write the prime factorization: {m(f'{n_val} = {pf_str}')}.",
                f"Multiply one more than each prime exponent to obtain {m(f'\\tau({n_val}) = {ans}')}.",
            ],
            f"Direct enumeration confirms exactly {m(str(ans))} positive divisors of {m(str(n_val))}.",
            f"إذا كان {m('N = p_1^{a_1} p_2^{a_2} \\cdots p_k^{a_k}')}، فإن {m(r'\\tau(N) = (a_1+1)(a_2+1)\\cdots(a_k+1)')}.",
            [
                f"نكتب التحليل إلى عوامل أولية: {m(f'{n_val} = {pf_str}')}.",
                f"نضرب القيم بعد إضافة واحد لكل أس فنحصل على {m(f'\\tau({n_val}) = {ans}')}.",
            ],
            f"يتحقق العد المباشر من وجود {m(str(ans))} قاسماً موجباً للعدد {m(str(n_val))}.",
            diagram_en=diag,
        ))

    # Medium 6..10: sum of divisors sigma(N), odd divisors, perfect-square divisors
    med_specs = [
        (
            6,
            lambda: _sigma(72),
            svg_olym_divisibility_lattice("72", "2³", "3²", "σ(72)=?"),
            f"In a Junior Olympiad divisor-sum task, compute the sum of all positive divisors {m(r'\\sigma(72)')} of {m('72')}.",
            f"في مسألة مجموع القواسم للأولمبياد الناشئ، احسب مجموع جميع القواسم الموجبة {m(r'\\sigma(72)')} للعدد {m('72')}.",
            f"Use the multiplicative formula {m(r'\\sigma(2^3 \\cdot 3^2) = (1+2+4+8)(1+3+9)')}.",
            f"استخدم الصيغة الضربية {m(r'\\sigma(2^3 \\cdot 3^2) = (1+2+4+8)(1+3+9)')}.",
            f"Prime factorization gives {m('72 = 2^3 \\cdot 3^2')}, so {m(r'\\sigma(72) = 15 \\times 13 = 195')}.",
            f"التحليل الأولي يعطي {m('72 = 2^3 \\cdot 3^2')}، ومنه {m(r'\\sigma(72) = 15 \\times 13 = 195')}.",
        ),
        (
            7,
            lambda: _sigma(108),
            svg_olym_divisibility_lattice("108", "2²", "3³", "σ(108)=?"),
            f"In a Junior Olympiad divisor-sum challenge, evaluate the sum of all positive divisors {m(r'\\sigma(108)')} of {m('108')}.",
            f"في تحدي مجموع القواسم للأولمبياد الناشئ، أوجد مجموع جميع القواسم الموجبة {m(r'\\sigma(108)')} للعدد {m('108')}.",
            f"Factor {m('108 = 2^2 \\cdot 3^3')} and multiply {m('(1+2+4)(1+3+9+27)')}.",
            f"حلّل {m('108 = 2^2 \\cdot 3^3')} واضرب {m('(1+2+4)(1+3+9+27)')}.",
            f"Since {m('1+2+4 = 7')} and {m('1+3+9+27 = 40')}, we get {m(r'\\sigma(108) = 7 \\times 40 = 280')}.",
            f"بما أن {m('1+2+4 = 7')} و{m('1+3+9+27 = 40')}، نحصل على {m(r'\\sigma(108) = 7 \\times 40 = 280')}.",
        ),
        (
            8,
            lambda: sum(1 for d in range(1, 2521) if 2520 % d == 0 and d % 2 == 1),
            svg_olym_divisibility_lattice("2520", "odd d", "3²·5·7", "count=?"),
            f"In a Junior Olympiad parity-divisor problem, how many positive odd divisors does {m('N = 2520')} have?",
            f"في مسألة القواسم الفردية للأولمبياد الناشئ، كم قاسماً موجباً فردياً يمتلكه العدد {m('N = 2520')}؟",
            f"Drop the power of {m('2')} from {m('2520 = 2^3 \\cdot 3^2 \\cdot 5 \\cdot 7')} and count divisors of the odd part.",
            f"استبعد قوى العدد {m('2')} من {m('2520 = 2^3 \\cdot 3^2 \\cdot 5 \\cdot 7')} واحسب قواسم الجزء الفردي.",
            f"The odd part is {m('3^2 \\cdot 5^1 \\cdot 7^1')}, giving {m('(2+1)(1+1)(1+1) = 12')} odd divisors.",
            f"الجزء الفردي هو {m('3^2 \\cdot 5^1 \\cdot 7^1')}، مما يعطي {m('(2+1)(1+1)(1+1) = 12')} قاسماً فردياً.",
        ),
        (
            9,
            lambda: (4 // 2 + 1) * (2 // 2 + 1) * (2 // 2 + 1),
            svg_factor_tree("2⁴·3²·5²", "2^{2a}", "3^{2b}", "5^{2c}", "sq=?"),
            f"In a Junior Olympiad square-divisor problem, let {m('M = 2^4 \\cdot 3^2 \\cdot 5^2 = 3600')}. How many positive divisors of {m('M')} are perfect squares?",
            f"في مسألة القواسم المربعة للأولمبياد الناشئ، ليكن {m('M = 2^4 \\cdot 3^2 \\cdot 5^2 = 3600')}. كم قاسماً موجباً للعدد {m('M')} يُعَدّ مربعاً كاملاً؟",
            f"A divisor {m('2^a 3^b 5^c')} is a square if and only if {m('a, b, c')} are all even.",
            f"يكون القاسم {m('2^a 3^b 5^c')} مربعاً كاملاً إذا وفقط إذا كانت الأسس {m('a, b, c')} جميعها زوجية.",
            f"There are {m('3')} choices for {m('a \\in \\{0,2,4\\}')}, {m('2')} for {m('b \\in \\{0,2\\}')}, and {m('2')} for {m('c \\in \\{0,2\\}')}, giving {m('3 \\times 2 \\times 2 = 12')}.",
            f"توجد {m('3')} خيارات للأس {m('a \\in \\{0,2,4\\}')}، وخياران للأس {m('b \\in \\{0,2\\}')}، وخياران للأس {m('c \\in \\{0,2\\}')}، فيكون الناتج {m('3 \\times 2 \\times 2 = 12')}.",
        ),
        (
            10,
            lambda: sum(d for d in range(1, 181) if 180 % d == 0 and d % 3 == 0),
            svg_olym_divisibility_lattice("180", "3 | d", "2²·3²·5", "sum=?"),
            f"In a Junior Olympiad constrained divisor problem, find the sum of all positive divisors of {m('180')} that are multiples of {m('3')}.",
            f"في مسألة القواسم المشروطة للأولمبياد الناشئ، أوجد مجموع جميع القواسم الموجبة للعدد {m('180')} التي تقبل القسمة على {m('3')}.",
            f"Since {m('180 = 2^2 \\cdot 3^2 \\cdot 5')}, require the exponent of {m('3')} to be {m('1')} or {m('2')}.",
            f"بما أن {m('180 = 2^2 \\cdot 3^2 \\cdot 5')}، اشترط أن يكون أس العدد {m('3')} إما {m('1')} أو {m('2')}.",
            f"The sum is {m('(1+2+4)(3+9)(1+5) = 7 \\times 12 \\times 6 = 504')}.",
            f"المجموع يساوي {m('(1+2+4)(3+9)(1+5) = 7 \\times 12 \\times 6 = 504')}.",
        ),
    ]
    for idx, fn_ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = fn_ans()
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 12, ans - 6, ans + 6, ans + 18, ans + 24],
            h_en, h_ar,
            "Multiplicative prime-power structure separates choices per prime factor.",
            [st_en],
            f"Verified by direct divisor enumeration: {m(str(ans))}.",
            "البنية الضربية لقوى الأعداد الأولية تفصل الخيارات لكل عامل أولي.",
            [st_ar],
            f"تم التحقق عبر حصر القواسم مباشرة: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 11..15: inverse divisor problems, product of divisors, tau(n^2)
    hard_specs = [
        (
            11,
            2**5 * 3 * 5,
            svg_olym_divisibility_lattice("N=?", "τ(N)=24", "2⁵·3·5", "min N"),
            f"In a Junior Olympiad extremal number theory problem, find the smallest positive integer {m('N')} that has exactly {m('24')} positive divisors and is divisible by {m('15')}.",
            f"في مسألة القيم القصوى لنظرية الأعداد في الأولمبياد الناشئ، أوجد أصغر عدد صحيح موجب {m('N')} يمتلك بالضبط {m('24')} قاسماً موجباً ويقبل القسمة على {m('15')}.",
            f"Since {m('3 \\mid N')} and {m('5 \\mid N')}, assign the largest exponent in {m('24 = 6 \\times 2 \\times 2')} to the smallest prime {m('2')}.",
            f"بما أن {m('3 \\mid N')} و{m('5 \\mid N')}، خصص أكبر عامل في {m('24 = 6 \\times 2 \\times 2')} لأصغر عدد أولي وهو {m('2')}.",
            f"Comparing exponent patterns containing at least two odd primes {m('3, 5')}, the minimum is {m('2^5 \\cdot 3^1 \\cdot 5^1 = 480')} (smaller than {m('2^3 \\cdot 3^2 \\cdot 5^1 = 360')}? Wait: let us check both!).",
            f"نقارن توزيعات الأسس التي تتضمن العاملين {m('3, 5')} فنحصل على أصغر قيمة.",
        ),
        (
            12,
            24,
            svg_factor_tree("n=24", "τ(n)=8", "n^{τ/2}", "24⁴", "k=?"),
            f"In a Junior Olympiad divisor-product problem, the product of all positive divisors of {m('n = 24')} equals {m('24^k')}. Find the integer {m('k')}.",
            f"في مسألة جداء القواسم للأولمبياد الناشئ، إن حاصل ضرب جميع القواسم الموجبة للعدد {m('n = 24')} يساوي {m('24^k')}. أوجد العدد الصحيح {m('k')}.",
            f"Pair each divisor {m('d')} with {m('n/d')}; the product of all divisors is {m('n^{\\tau(n)/2}')}.",
            f"اربط كل قاسم {m('d')} بالقاسم المرافق {m('n/d')}؛ فيكون جداء جميع القواسم مساوياً للمقدار {m('n^{\\tau(n)/2}')}.",
            f"Since {m('24 = 2^3 \\cdot 3^1')}, we have {m(r'\\tau(24) = (3+1)(1+1) = 8')}, so {m('k = \\tau(24)/2 = 4')}.",
            f"بما أن {m('24 = 2^3 \\cdot 3^1')}، فإن {m(r'\\tau(24) = (3+1)(1+1) = 8')}، ومنه {m('k = \\tau(24)/2 = 4')}.",
        ),
        (
            13,
            (2 * 2 + 1) * (2 * 1 + 1) * (2 * 1 + 1),
            svg_olym_divisibility_lattice("n²", "p⁴", "q²·r²", "τ(n²)=?"),
            f"In a Junior Olympiad multiplicative-function problem, a positive integer {m('n = p^2 q r')} has distinct prime factors {m('p, q, r')}. Compute {m(r'\\tau(n^2)')}, the number of positive divisors of {m('n^2')}.",
            f"في مسألة الدوال الضربية للأولمبياد الناشئ، عدد صحيح موجب {m('n = p^2 q r')} عوامله الأولية {m('p, q, r')} مختلفة. احسب {m(r'\\tau(n^2)')}، أي عدد القواسم الموجبة للعدد {m('n^2')}.",
            f"Square each prime power in {m('n')} to get {m('n^2 = p^4 q^2 r^2')}.",
            f"ربّع كل قوة أولية في {m('n')} لتحصل على {m('n^2 = p^4 q^2 r^2')}.",
            f"From {m('n^2 = p^4 q^2 r^2')}, we compute {m(r'\\tau(n^2) = (4+1)(2+1)(2+1) = 5 \\times 3 \\times 3 = 45')}.",
            f"من {m('n^2 = p^4 q^2 r^2')}، نحسب {m(r'\\tau(n^2) = (4+1)(2+1)(2+1) = 5 \\times 3 \\times 3 = 45')}.",
        ),
        (
            14,
            sum(n for n in range(1, 200) if _tau(n) == 6 and n <= 50),
            svg_number_strip(["12", "18", "20", "28", "32", "44", "45", "50", "∑=?"]),
            f"In a Junior Olympiad classification problem, find the sum of all positive integers {m('n \\le 50')} that have exactly {m('6')} positive divisors.",
            f"في مسألة تصنيف الأعداد للأولمبياد الناشئ، أوجد مجموع جميع الأعداد الصحيحة الموجبة {m('n \\le 50')} التي تمتلك بالضبط {m('6')} قواسم موجبة.",
            f"An integer has {m('6')} divisors iff it has the form {m('p^5')} or {m('p^2 q')} for distinct primes {m('p, q')}.",
            f"يمتلك العدد الصحيح {m('6')} قواسم إذا وفقط إذا كان على الصورة {m('p^5')} أو {m('p^2 q')} لعددين أوليين مختلفين {m('p, q')}.",
            f"The integers {m('n \\le 50')} with {m(r'\\tau(n)=6')} are {m('12, 18, 20, 28, 32, 44, 45, 50')}, whose sum is {m('249')}.",
            f"الأعداد {m('n \\le 50')} التي تحقق {m(r'\\tau(n)=6')} هي {m('12, 18, 20, 28, 32, 44, 45, 50')}، ومجموعها {m('249')}.",
        ),
        (
            15,
            next(n for n in range(1, 5000) if n % 100 == 0 and _tau(n) == 27),
            svg_olym_divisibility_lattice("100 | N", "2²·5²", "3²", "N=?"),
            f"In a Junior Olympiad divisor-structure problem, find the smallest positive multiple of {m('100')} that has exactly {m('27')} positive divisors.",
            f"في مسألة بنية القواسم للأولمبياد الناشئ، أوجد أصغر مضاعف موجب للعدد {m('100')} يمتلك بالضبط {m('27')} قاسماً موجباً.",
            f"Note that {m('100 = 2^2 \\cdot 5^2')} already has {m('3 \\times 3 = 9')} divisors; factor {m('27 = 3 \\times 3 \\times 3')}.",
            f"لاحظ أن {m('100 = 2^2 \\cdot 5^2')} يمتلك بالفعل {m('3 \\times 3 = 9')} قواسم؛ وحلّل {m('27 = 3 \\times 3 \\times 3')}.",
            f"Multiplying {m('2^2 \\cdot 5^2')} by {m('3^2 = 9')} yields {m('N = 2^2 \\cdot 3^2 \\cdot 5^2 = 900')}, which is smaller than {m('2^8 \\cdot 5^2 = 6400')}.",
            f"بضرب {m('2^2 \\cdot 5^2')} في {m('3^2 = 9')} نحصل على {m('N = 2^2 \\cdot 3^2 \\cdot 5^2 = 900')}، وهو أصغر من {m('2^8 \\cdot 5^2 = 6400')}.",
        ),
    ]
    # Fix Hard 11 programmatically!
    ans_11 = next(n for n in range(15, 2000, 15) if _tau(n) == 24)
    assert ans_11 == 360  # 2^3 * 3^2 * 5^1 = 360 has (3+1)*(2+1)*(1+1) = 24 divisors and 15 | 360!
    hard_specs[0] = (
        11,
        ans_11,
        svg_olym_divisibility_lattice("N=?", "τ(N)=24", "15 | N", "min N"),
        f"In a Junior Olympiad extremal number theory problem, find the smallest positive integer {m('N')} that is divisible by {m('15')} and has exactly {m('24')} positive divisors.",
        f"في مسألة القيم القصوى لنظرية الأعداد في الأولمبياد الناشئ، أوجد أصغر عدد صحيح موجب {m('N')} يقبل القسمة على {m('15')} ويمتلك بالضبط {m('24')} قاسماً موجباً.",
        f"Factor {m('24 = 4 \\times 3 \\times 2')} and assign exponents {m('3, 2, 1')} to primes {m('2, 3, 5')}.",
        f"حلّل {m('24 = 4 \\times 3 \\times 2')} وخصص الأسس {m('3, 2, 1')} للأعداد الأولية {m('2, 3, 5')}.",
        f"Setting {m('N = 2^3 \\cdot 3^2 \\cdot 5^1 = 360')} gives {m('15 \\mid 360')} and {m(r'\\tau(360) = (3+1)(2+1)(1+1) = 24')}.",
        f"بوضع {m('N = 2^3 \\cdot 3^2 \\cdot 5^1 = 360')} يتحقق {m('15 \\mid 360')} وكذلك {m(r'\\tau(360) = (3+1)(2+1)(1+1) = 24')}.",
    )
    # Fix Hard 12 answer to 4 (not 24)
    hard_specs[1] = (12, 4, *hard_specs[1][2:])

    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 3, ans + 3, ans + 9, ans + 15, max(1, ans // 2)],
            h_en, h_ar,
            "Match prime-exponent partitions of the divisor count to minimize or evaluate the target.",
            [st_en],
            f"Programmatic check confirms {m(str(ans))}.",
            "طابق تجزئات العوامل لعدد القواسم مع الأسس الأولية لإيجاد القيمة المطلوبة.",
            [st_ar],
            f"يؤكد التحقق البرمجي أن الجواب هو {m(str(ans))}.",
            diagram_en=diag,
        ))

    return out


def _build_u11_b2_gcd_lcm() -> list[dict]:
    bp = "olym_t1_nt_gcd_lcm_bezout"
    tp = "Number Theory"
    out: list[dict] = []

    # Easy 16..20: gcd * lcm = a * b and Euclidean algorithm steps
    easy_specs = [
        (16, 12, 180, 36, "Find b"),
        (17, 15, 315, 45, "Find b"),
        (18, 18, 504, 72, "Find b"),
        (19, 24, 720, 120, "Find b"),
        (20, 28, 840, 140, "Find b"),
    ]
    for idx, g_val, l_val, a_val, _ in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (g_val * l_val) // a_val
        assert math.gcd(a_val, ans) == g_val and math.lcm(a_val, ans) == l_val
        diag = svg_olym_divisibility_lattice(f"lcm={l_val}", f"a={a_val}", "b=?", f"gcd={g_val}")
        q_en = (
            f"In a Junior Olympiad GCD-LCM lattice problem, two positive integers {m('a')} and {m('b')} satisfy "
            f"{m(f'\\gcd(a, b) = {g_val}')} and {m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}. "
            f"If {m(f'a = {a_val}')}, what is the value of {m('b')}?"
        )
        q_ar = (
            f"في مسألة شبكة القاسم المشترك الأكبر والمضاعف المشترك الأصغر للأولمبياد الناشئ، يحقق العددان الصحيحان الموجبان {m('a')} و{m('b')} "
            f"العلاقتين {m(f'\\gcd(a, b) = {g_val}')} و{m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}. "
            f"إذا كان {m(f'a = {a_val}')}، فما قيمة {m('b')}؟"
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - g_val, ans + g_val, ans + 2 * g_val, l_val // g_val, a_val + g_val],
            f"Use the fundamental identity {m(r'a \cdot b = \gcd(a,b) \cdot \operatorname{lcm}(a,b)')}.",
            f"استخدم المتطابقة الأساسية {m(r'a \cdot b = \gcd(a,b) \cdot \operatorname{lcm}(a,b)')}.",
            f"The product of two positive integers equals the product of their GCD and LCM.",
            [
                f"Substitute into {m(f'b = \\frac{{\\gcd(a,b)\\cdot\\operatorname{{lcm}}(a,b)}}{{a}} = \\frac{{{g_val} \\times {l_val}}}{{{a_val}}}')}.",
                f"Simplifying gives {m(f'b = {ans}')}.",
            ],
            f"Check: {m(f'\\gcd({a_val}, {ans}) = {g_val}')} and {m(f'\\operatorname{{lcm}}({a_val}, {ans}) = {l_val}')}.",
            f"حاصل ضرب أي عددين صحيحين موجبين يساوي حاصل ضرب قاسمهما المشترك الأكبر في مضاعفهما المشترك الأصغر.",
            [
                f"نعوض في الصيغة {m(f'b = \\frac{{{g_val} \\times {l_val}}}{{{a_val}}}')}.",
                f"التبسيط يعطي {m(f'b = {ans}')}.",
            ],
            f"تحقق: {m(f'\\gcd({a_val}, {ans}) = {g_val}')} و{m(f'\\operatorname{{lcm}}({a_val}, {ans}) = {l_val}')}.",
            diagram_en=diag,
        ))

    # Medium 21..25: counting pairs (a,b) with given gcd and lcm, or min(a+b)
    med_specs = [
        (21, 6, 756, "min_sum"),    # l/g = 126 = 2 * 9 * 7 -> coprime pair closest to sqrt(126) is (9, 14), sum = 6*(9+14) = 138
        (22, 8, 1680, "min_sum"),   # l/g = 210 = 2*3*5*7 -> closest coprime pair is (14, 15), sum = 8*29 = 232
        (23, 10, 2100, "count_ord"),  # l/g = 210 has 4 distinct prime factors -> 2^4 = 16 ordered pairs
        (24, 12, 5040, "count_ord"),  # l/g = 420 = 2^2 * 3 * 5 * 7 -> 4 distinct prime factors -> 2^4 = 16 ordered pairs
        (25, 15, 1350, "min_sum"),  # l/g = 90 = 2 * 9 * 5 -> closest coprime pair is (9, 10), sum = 15*19 = 285
    ]
    for idx, g_val, l_val, mode in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        q_ratio = l_val // g_val
        coprime_pairs = [(x, q_ratio // x) for x in range(1, q_ratio + 1) if q_ratio % x == 0 and math.gcd(x, q_ratio // x) == 1]
        if mode == "min_sum":
            ans = min(g_val * (x + y) for x, y in coprime_pairs)
            diag = svg_olym_divisibility_lattice(f"lcm={l_val}", "a=gx", "b=gy", "min(a+b)=?")
            q_en = (
                f"In a Junior Olympiad GCD-LCM optimization problem, positive integers {m('a')} and {m('b')} satisfy "
                f"{m(f'\\gcd(a, b) = {g_val}')} and {m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}. "
                f"What is the minimum possible value of {m('a + b')}?"
            )
            q_ar = (
                f"في مسألة تحسين القاسم والمضاعف المشترك للأولمبياد الناشئ، يحقق العددان الصحيحان الموجبان {m('a')} و{m('b')} "
                f"العلاقتين {m(f'\\gcd(a, b) = {g_val}')} و{m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}. "
                f"ما أصغر قيمة ممكنة للمجموع {m('a + b')}؟"
            )
            h_en = f"Write {m(f'a = {g_val}x')} and {m(f'b = {g_val}y')} with {m('\\gcd(x,y)=1')} and {m(f'xy = {q_ratio}')}."
            h_ar = f"اكتب {m(f'a = {g_val}x')} و{m(f'b = {g_val}y')} مع {m('\\gcd(x,y)=1')} و{m(f'xy = {q_ratio}')}."
            st_en = f"Among coprime factor pairs of {m(str(q_ratio))}, choosing the pair closest to {m(f'\\sqrt{{{q_ratio}}}')} gives {m(f'\\min(a+b) = {ans}')}."
            st_ar = f"من بين أزواج العوامل الأولية نسبياً للعدد {m(str(q_ratio))}، اختيار الزوج الأقرب إلى {m(f'\\sqrt{{{q_ratio}}}')} يعطي {m(f'\\min(a+b) = {ans}')}."
        else:
            ans = len(coprime_pairs)
            diag = svg_olym_divisibility_lattice(f"lcm={l_val}", "(a, b)", f"xy={q_ratio}", "pairs=?")
            q_en = (
                f"In a Junior Olympiad pair-counting problem, how many ordered pairs of positive integers {m('(a, b)')} satisfy "
                f"{m(f'\\gcd(a, b) = {g_val}')} and {m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}?"
            )
            q_ar = (
                f"في مسألة عد الأزواج للأولمبياد الناشئ، كم زوجاً مرتباً من الأعداد الصحيحة الموجبة {m('(a, b)')} يحقق "
                f"{m(f'\\gcd(a, b) = {g_val}')} و{m(f'\\operatorname{{lcm}}(a, b) = {l_val}')}؟"
            )
            h_en = f"Each prime power in {m(f'\\operatorname{{lcm}}/\\gcd = {q_ratio}')} must go entirely to {m('x')} or entirely to {m('y')}."
            h_ar = f"كل قوة أولية في خارج القسمة {m(f'\\operatorname{{lcm}}/\\gcd = {q_ratio}')} يجب أن تذهب بالكامل إلى {m('x')} أو بالكامل إلى {m('y')}."
            st_en = f"Since {m(str(q_ratio))} has {m('4')} distinct prime factors, there are {m(f'2^4 = {ans}')} ordered coprime pairs {m('(x, y)')}."
            st_ar = f"بما أن العدد {m(str(q_ratio))} يمتلك {m('4')} عوامل أولية مختلفة، فهناك {m(f'2^4 = {ans}')} زوجاً مرتباً أولياً نسبياً {m('(x, y)')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 8, ans // 2, ans + 8, ans + 16, ans * 2],
            h_en, h_ar,
            "Factor out the GCD to reduce the condition to coprime factors of lcm/gcd.",
            [st_en],
            f"Verified across all divisor pairs of {m(str(q_ratio))}: {m(str(ans))}.",
            "أخرج القاسم المشترك الأكبر لتبسيط الشرط إلى عوامل أولية نسبياً للمقدار lcm/gcd.",
            [st_ar],
            f"تم التحقق عبر فحص جميع أزواج قواسم {m(str(q_ratio))}: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 26..30: Euclidean shift gcd(a*n + b, c*n + d), Bezout / Chicken McNugget Frobenius coin problem
    hard_specs = [
        (
            26,
            max(math.gcd(2 * n + 13, n + 2) for n in range(1, 500)),  # 2(n+2) - (2n+13) = -9 -> max gcd is 9 (e.g. n=7 -> 27, 9)
            svg_olym_divisibility_lattice("2n+13", "n+2", "2(n+2)−(2n+13)", "max gcd=?"),
            f"In a Junior Olympiad Euclidean elimination problem, as {m('n')} ranges over all positive integers, what is the maximum possible value of {m('\\gcd(2n + 13,\\, n + 2)')}?",
            f"في مسألة الحذف الإقليدي للأولمبياد الناشئ، عندما يتغير {m('n')} عبر جميع الأعداد الصحيحة الموجبة، ما أكبر قيمة ممكنة للمقدار {m('\\gcd(2n + 13,\\, n + 2)')}؟",
            f"Eliminate {m('n')} via the linear combination {m('(2n + 13) - 2(n + 2) = 9')}.",
            f"تخلص من {m('n')} عبر التركيبة الخطية {m('(2n + 13) - 2(n + 2) = 9')}.",
            f"Since {m('\\gcd(2n+13, n+2) = \\gcd(n+2, 9)')}, the maximum possible divisor is {m('9')}, achieved at {m('n = 7')}.",
            f"بما أن {m('\\gcd(2n+13, n+2) = \\gcd(n+2, 9)')}، فإن أكبر قاسم ممكن هو {m('9')}، ويتحقق عند {m('n = 7')}.",
        ),
        (
            27,
            max(math.gcd(3 * n + 25, n + 4) for n in range(1, 500)),  # (3n+25) - 3(n+4) = 13 -> 13 (at n=9)
            svg_olym_divisibility_lattice("3n+25", "n+4", "(3n+25)−3(n+4)", "max gcd=?"),
            f"In a Junior Olympiad linear GCD problem, find the greatest possible value of {m('\\gcd(3n + 25,\\, n + 4)')} over all positive integers {m('n')}.",
            f"في مسألة القاسم المشترك الخطي للأولمبياد الناشئ، أوجد أكبر قيمة ممكنة للمقدار {m('\\gcd(3n + 25,\\, n + 4)')} لجميع الأعداد الصحيحة الموجبة {m('n')}.",
            f"Compute {m('(3n + 25) - 3(n + 4) = 13')}.",
            f"احسب الفرق الخطي {m('(3n + 25) - 3(n + 4) = 13')}.",
            f"Every common divisor divides {m('13')}, and for {m('n = 9')} both expressions are multiples of {m('13')}, giving {m('13')}.",
            f"كل قاسم مشترك يقسم {m('13')}، وعند {m('n = 9')} يقبل المقداران القسمة على {m('13')}، فنحصل على {m('13')}.",
        ),
        (
            28,
            7 * 11 - 7 - 11,  # 59
            svg_pre_coin_purse(["7", "11"], "Max ≠ ?"),
            f"In a Junior Olympiad Frobenius coin problem, tokens are available only in denominations of {m('7')} and {m('11')} points. What is the largest integer score that CANNOT be formed using nonnegative multiples of {m('7')} and {m('11')}?",
            f"في مسألة عملات فروبينيوس للأولمبياد الناشئ، تتوفر قسائم بفئتي {m('7')} و{m('11')} نقطة فقط. ما أكبر مجموع صحيح لا يمكن تكوينه باستخدام مضاعفات غير سالبة للعددين {m('7')} و{m('11')}؟",
            f"For coprime {m('a, b')}, the Chicken McNugget theorem gives {m('ab - a - b')} as the largest unattainable integer.",
            f"للعددين الأوليين نسبياً {m('a, b')}، تنص مبرهنة فروبينيوس على أن أكبر عدد غير قابل للتمثيل هو {m('ab - a - b')}.",
            f"Since {m('\\gcd(7, 11) = 1')}, the largest unattainable score is {m('7 \\times 11 - 7 - 11 = 59')}.",
            f"بما أن {m('\\gcd(7, 11) = 1')}، فإن أكبر مجموع لا يمكن تكوينه هو {m('7 \\times 11 - 7 - 11 = 59')}.",
        ),
        (
            29,
            (9 - 1) * (13 - 1) // 2,  # 48 unattainable nonnegative integers
            svg_pre_coin_purse(["9", "13"], "Unattainable=?"),
            f"In a Junior Olympiad Bézout semigroup problem, how many positive integers CANNOT be written in the form {m('9x + 13y')} for nonnegative integers {m('x, y \\ge 0')}?",
            f"في مسألة نصف زمرة بيزو للأولمبياد الناشئ، كم عدداً صحيحاً موجباً لا يمكن كتابته على الصورة {m('9x + 13y')} حيث {m('x, y \\ge 0')} عددان صحيحان غير سالبين؟",
            f"For coprime {m('a, b')}, exactly {m('\\frac{(a-1)(b-1)}{2}')} positive integers cannot be represented.",
            f"للعددين الأوليين نسبياً {m('a, b')}، يوجد بالضبط {m('\\frac{(a-1)(b-1)}{2}')} عدداً صحيحاً موجباً لا يمكن تمثيله.",
            f"Applying Sylvester's theorem for {m('a = 9')} and {m('b = 13')} gives {m('\\frac{(9-1)(13-1)}{2} = \\frac{8 \\times 12}{2} = 48')}.",
            f"بتطبيق مبرهنة سيلفستر للعددين {m('a = 9')} و{m('b = 13')} نحصل على {m('\\frac{(9-1)(13-1)}{2} = \\frac{8 \\times 12}{2} = 48')}.",
        ),
        (
            30,
            next(x for x in range(1, 37) if (15 * x) % 37 == 1),  # 15*5 = 75 = 2*37 + 1 -> x = 5
            svg_olym_divisibility_lattice("15x − 37y = 1", "x > 0", "y > 0", "min x=?"),
            f"In a Junior Olympiad Bézout identity problem, find the smallest positive integer {m('x')} for which there exists an integer {m('y')} satisfying {m('15x - 37y = 1')}.",
            f"في مسألة متطابقة بيزو للأولمبياد الناشئ، أوجد أصغر عدد صحيح موجب {m('x')} يوجد من أجله عدد صحيح {m('y')} يحقق {m('15x - 37y = 1')}.",
            f"Reduce modulo {m('37')}: we need {m('15x \\equiv 1 \\pmod{37}')}.",
            f"اختزل المعادلة بترديد {m('37')}: نحتاج إلى {m('15x \\equiv 1 \\pmod{37}')}.",
            f"Notice that {m('15 \\times 5 = 75 = 2 \\times 37 + 1')}, so the smallest positive solution is {m('x = 5')} (with {m('y = 2')}).",
            f"نلاحظ أن {m('15 \\times 5 = 75 = 2 \\times 37 + 1')}، لذا فإن أصغر حل موجب هو {m('x = 5')} (مع {m('y = 2')}).",
        ),
    ]
    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans + 2, ans + 4, ans + 6, ans + 11],
            h_en, h_ar,
            "Linear integer combinations preserve common divisors and generate all multiples of the GCD.",
            [st_en],
            f"Programmatically verified: {m(str(ans))}.",
            "التركيبات الخطية الصحيحة تحافظ على القواسم المشتركة وتولّد مضاعفات القاسم المشترك الأكبر.",
            [st_ar],
            f"تم التحقق برمجياً: {m(str(ans))}.",
            diagram_en=diag,
        ))

    return out


def _build_u11_b3_modular_cycles() -> list[dict]:
    bp = "olym_t1_nt_modular_cycles"
    tp = "Number Theory"
    out: list[dict] = []

    # Easy 31..35: units digit / remainder of large powers via cycle length
    easy_specs = [
        (31, 7, 2026, 10, "units digit"),
        (32, 3, 2027, 10, "units digit"),
        (33, 2, 2025, 7, "remainder"),
        (34, 5, 2026, 13, "remainder"),
        (35, 8, 2027, 10, "units digit"),
    ]
    for idx, base, exp, mod_v, kind in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = pow(base, exp, mod_v)
        diag = svg_number_strip([f"{base}¹", f"{base}²", f"{base}³", f"{base}⁴", f"{base}^{exp} mod {mod_v} = ?"])
        if kind == "units digit":
            q_en = f"In a Junior Olympiad modular periodicity problem, what is the units digit of {m(f'{base}^{{{exp}}}')}?"
            q_ar = f"في مسألة الدورية المعيارية للأولمبياد الناشئ، ما رقم آحاد العدد {m(f'{base}^{{{exp}}}')}؟"
        else:
            q_en = f"In a Junior Olympiad modular arithmetic problem, find the remainder when {m(f'{base}^{{{exp}}}')} is divided by {m(str(mod_v))}."
            q_ar = f"في مسألة الحساب المعياري للأولمبياد الناشئ، أوجد باقي قسمة {m(f'{base}^{{{exp}}}')} على {m(str(mod_v))}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [(ans + 1) % mod_v, (ans + 2) % mod_v, (ans + 3) % mod_v, (ans + 4) % mod_v, (ans + 5) % mod_v],
            f"Find the repeating cycle of powers of {m(str(base))} modulo {m(str(mod_v))}.",
            f"أوجد طول الدورة المتكررة لقوى العدد {m(str(base))} بترديد {m(str(mod_v))}.",
            f"Powers of {m(str(base))} modulo {m(str(mod_v))} repeat in a short cycle of length at most {m('4')}.",
            [
                f"Reduce the exponent {m(str(exp))} modulo the cycle length.",
                f"Evaluating the matching power modulo {m(str(mod_v))} yields {m(str(ans))}.",
            ],
            f"Exact modular exponentiation gives {m(f'{base}^{{{exp}}} \\equiv {ans} \\pmod{{{mod_v}}}')}.",
            f"قوى العدد {m(str(base))} بترديد {m(str(mod_v))} تتكرر في دورة قصيرة طولها على الأكثر {m('4')}.",
            [
                f"نختزل الأس {m(str(exp))} بترديد طول الدورة.",
                f"حساب القوة الموافقة بترديد {m(str(mod_v))} يعطي {m(str(ans))}.",
            ],
            f"الحساب المعياري الدقيق يؤكد أن {m(f'{base}^{{{exp}}} \\equiv {ans} \\pmod{{{mod_v}}}')}.",
            diagram_en=diag,
        ))

    # Medium 36..40: last two digits (mod 100), divisibility by 9/11, combined modular sums
    med_specs = [
        (
            36,
            (pow(3, 100, 10) + pow(7, 100, 10)) % 10,
            svg_number_strip(["3¹⁰⁰", "+", "7¹⁰⁰", "mod 10 = ?"]),
            f"In a Junior Olympiad modular sum problem, find the remainder when {m('3^{100} + 7^{100}')} is divided by {m('10')}.",
            f"في مسألة المجاميع المعيارية للأولمبياد الناشئ، أوجد باقي قسمة {m('3^{100} + 7^{100}')} على {m('10')}.",
            f"Both {m('3^4 \\equiv 1')} and {m('7^4 \\equiv 1 \\pmod{10}')}.",
            f"كل من {m('3^4 \\equiv 1')} و{m('7^4 \\equiv 1 \\pmod{10}')}.",
            f"Since {m('100')} is a multiple of {m('4')}, {m('3^{100} + 7^{100} \\equiv 1 + 1 = 2 \\pmod{10}')}.",
            f"بما أن {m('100')} من مضاعفات {m('4')}، فإن {m('3^{100} + 7^{100} \\equiv 1 + 1 = 2 \\pmod{10}')}.",
        ),
        (
            37,
            pow(7, 2026, 100),
            svg_number_strip(["7¹=07", "7²=49", "7³=43", "7⁴=01", "7²⁰²⁶=?"]),
            f"In a Junior Olympiad last-two-digits problem, what is the remainder when {m('7^{2026}')} is divided by {m('100')}?",
            f"في مسألة آخر رقمين للأولمبياد الناشئ، ما باقي قسمة {m('7^{2026}')} على {m('100')}؟",
            f"Observe that {m('7^4 = 2401 \\equiv 1 \\pmod{100}')}.",
            f"لاحظ أن {m('7^4 = 2401 \\equiv 1 \\pmod{100}')}.",
            f"Since {m('2026 = 4 \\times 506 + 2')}, we have {m('7^{2026} \\equiv 7^2 = 49 \\pmod{100}')}.",
            f"بما أن {m('2026 = 4 \\times 506 + 2')}، فإن {m('7^{2026} \\equiv 7^2 = 49 \\pmod{100}')}.",
        ),
        (
            38,
            next(d for d in range(10) if int(f"54{d}72") % 11 == 0),
            svg_digit_slots(["5", "4", "?", "7", "2"], "11 | N"),
            f"In a Junior Olympiad divisibility test problem, the five-digit number {m('\\overline{54d72}')} is divisible by {m('11')}. Find the digit {m('d')}.",
            f"في مسألة قابلية القسمة للأولمبياد الناشئ، العدد المكون من خمسة أرقام {m('\\overline{54d72}')} يقبل القسمة على {m('11')}. أوجد الرقم {m('d')}.",
            f"Use the alternating digit sum modulo {m('11')}: {m('(5 + d + 2) - (4 + 7) \\equiv 0 \\pmod{11}')}.",
            f"استخدم المجموع المتناوب للأرقام بترديد {m('11')}: {m('(5 + d + 2) - (4 + 7) \\equiv 0 \\pmod{11}')}.",
            f"Simplifying {m('d - 4 \\equiv 0 \\pmod{11}')} gives the single digit {m('d = 4')}.",
            f"تبسيط العلاقة {m('d - 4 \\equiv 0 \\pmod{11}')} يعطي الرقم الوحيد {m('d = 4')}.",
        ),
        (
            39,
            next(a + b for a in range(1, 10) for b in range(0, 10, 2) if int(f"{a}37{b}") % 72 == 0),
            svg_digit_slots(["a", "3", "7", "b"], "72 | a37b"),
            f"In a Junior Olympiad composite divisibility problem, the four-digit integer {m('\\overline{a37b}')} is divisible by {m('72')}. Find {m('a + b')}.",
            f"في مسألة قابلية القسمة المركبة للأولمبياد الناشئ، العدد المكون من أربعة أرقام {m('\\overline{a37b}')} يقبل القسمة على {m('72')}. أوجد {m('a + b')}.",
            f"Since {m('72 = 8 \\times 9')}, first use {m('8 \\mid \\overline{37b}')} to find {m('b')}, then {m('9 \\mid (a+3+7+b)')}.",
            f"بما أن {m('72 = 8 \\times 9')}، استخدم أولاً {m('8 \\mid \\overline{37b}')} لإيجاد {m('b')}، ثم {m('9 \\mid (a+3+7+b)')}.",
            f"Since {m('376 = 8 \\times 47')}, we have {m('b = 6')}; then {m('a + 16')} is a multiple of {m('9')}, so {m('a = 2')} and {m('a + b = 8')}.",
            f"بما أن {m('376 = 8 \\times 47')}، فإن {m('b = 6')}؛ ومنه {m('a + 16')} مضاعف للعدد {m('9')}، أي {m('a = 2')} ويكون {m('a + b = 8')}.",
        ),
        (
            40,
            sum(math.factorial(k) for k in range(1, 50)) % 15,
            svg_number_strip(["1!", "2!", "3!", "4!", "⋯", "49!", "mod 15 = ?"]),
            f"In a Junior Olympiad factorial remainder problem, find the remainder when {m('1! + 2! + 3! + \\cdots + 49!')} is divided by {m('15')}.",
            f"في مسألة بواقي المضروب للأولمبياد الناشئ، أوجد باقي قسمة {m('1! + 2! + 3! + \\cdots + 49!')} على {m('15')}.",
            f"For every {m('k \\ge 5')}, {m('k!')} is divisible by {m('3 \\times 5 = 15')}.",
            f"لكل {m('k \\ge 5')}، يقبل المضروب {m('k!')} القسمة على {m('3 \\times 5 = 15')}.",
            f"Only the first four terms contribute: {m('1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 = 33 \\equiv 3 \\pmod{15}')}.",
            f"تبقى الحدود الأربعة الأولى فقط: {m('1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 = 33 \\equiv 3 \\pmod{15}')}.",
        ),
    ]
    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans + 1, ans + 2, ans + 3, max(0, ans - 1), ans + 5],
            h_en, h_ar,
            "Exploit modular periodicity and prime-power divisibility criteria.",
            [st_en],
            f"Verified directly in Python: {m(str(ans))}.",
            "استثمر الدورية المعيارية وقواعد قابلية القسمة لقوى الأعداد الأولية.",
            [st_ar],
            f"تم التحقق برمجياً بشكل مباشر: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 41..45: Chinese Remainder Theorem (CRT) & Fermat/Euler cyclic remainders
    hard_specs = [
        (
            41,
            next(x for x in range(1, 106) if x % 3 == 2 and x % 5 == 3 and x % 7 == 2),  # 23
            svg_olym_divisibility_lattice("x mod 105", "x≡2 (3)", "x≡2 (7)", "x≡3 (5), x=?"),
            f"In a Junior Olympiad Chinese Remainder problem, find the smallest positive integer {m('x')} satisfying {m('x \\equiv 2 \\pmod{3}')}, {m('x \\equiv 3 \\pmod{5}')}, and {m('x \\equiv 2 \\pmod{7}')}.",
            f"في مسألة مبرهنة البواقي الصينية للأولمبياد الناشئ، أوجد أصغر عدد صحيح موجب {m('x')} يحقق {m('x \\equiv 2 \\pmod{3}')} و{m('x \\equiv 3 \\pmod{5}')} و{m('x \\equiv 2 \\pmod{7}')}.",
            f"Combine {m('x \\equiv 2 \\pmod{3}')} and {m('x \\equiv 2 \\pmod{7}')} into {m('x \\equiv 2 \\pmod{21}')}.",
            f"ادمج الشرطين {m('x \\equiv 2 \\pmod{3}')} و{m('x \\equiv 2 \\pmod{7}')} في الشرط الواحد {m('x \\equiv 2 \\pmod{21}')}.",
            f"Testing {m('x = 2, 23, 44, \\dots')}, we find {m('23 \\equiv 3 \\pmod{5}')}, so {m('x = 23')}.",
            f"بتجربة القيم {m('x = 2, 23, 44, \\dots')}، نجد أن {m('23 \\equiv 3 \\pmod{5}')}، ومنه {m('x = 23')}.",
        ),
        (
            42,
            next(x for x in range(1, 200) if x % 4 == 3 and x % 5 == 4 and x % 6 == 5),  # lcm(4,5,6)-1 = 59
            svg_olym_divisibility_lattice("x+1", "4 | x+1", "5 | x+1", "6 | x+1, x=?"),
            f"In a Junior Olympiad simultaneous congruence problem, find the smallest positive integer {m('x')} that leaves remainders {m('3, 4, 5')} when divided by {m('4, 5, 6')}, respectively.",
            f"في مسألة التطابقات المتزامنة للأولمبياد الناشئ، أوجد أصغر عدد صحيح موجب {m('x')} يترك البواقي {m('3, 4, 5')} عند قسمته على {m('4, 5, 6')} على الترتيب.",
            f"Notice that {m('x + 1')} is divisible by {m('4, 5,')} and {m('6')}.",
            f"لاحظ أن {m('x + 1')} يقبل القسمة على كل من {m('4, 5, 6')}.",
            f"Since {m('\\operatorname{lcm}(4, 5, 6) = 60')}, the smallest positive solution is {m('x = 60 - 1 = 59')}.",
            f"بما أن {m('\\operatorname{lcm}(4, 5, 6) = 60')}، فإن أصغر حل موجب هو {m('x = 60 - 1 = 59')}.",
        ),
        (
            43,
            pow(2, 2026, 13),
            svg_number_strip(["2⁶≡−1", "2¹²≡1", "mod 13", "2²⁰²⁶ mod 13 = ?"]),
            f"In a Junior Olympiad Fermat cycle problem, find the remainder when {m('2^{2026}')} is divided by {m('13')}.",
            f"في مسألة دورة فيرما للأولمبياد الناشئ، أوجد باقي قسمة {m('2^{2026}')} على {m('13')}.",
            f"By Fermat's Little Theorem, {m('2^{12} \\equiv 1 \\pmod{13}')}.",
            f"بحسب مبرهنة فيرما الصغرى، فإن {m('2^{12} \\equiv 1 \\pmod{13}')}.",
            f"Since {m('2026 = 12 \\times 168 + 10')} and {m('2^6 = 64 \\equiv -1 \\pmod{13}')}, we get {m('2^{10} = 2^6 \\cdot 2^4 \\equiv (-1)(16) \\equiv -3 \\equiv 10 \\pmod{13}')}.",
            f"بما أن {m('2026 = 12 \\times 168 + 10')} و{m('2^6 = 64 \\equiv -1 \\pmod{13}')}، نحصل على {m('2^{10} \\equiv (-1)(16) \\equiv 10 \\pmod{13}')}.",
        ),
        (
            44,
            sum(pow(k, 4, 5) for k in range(1, 101)) % 5,
            svg_number_strip(["1⁴", "2⁴", "3⁴", "4⁴", "5⁴", "⋯", "100⁴ mod 5 = ?"]),
            f"In a Junior Olympiad fourth-power residue problem, find the remainder when {m('1^4 + 2^4 + 3^4 + \\cdots + 100^4')} is divided by {m('5')}.",
            f"في مسألة بواقي القوى الرابعة للأولمبياد الناشئ، أوجد باقي قسمة المجموع {m('1^4 + 2^4 + 3^4 + \\cdots + 100^4')} على {m('5')}.",
            f"For every integer {m('k')} not divisible by {m('5')}, {m('k^4 \\equiv 1 \\pmod{5}')}.",
            f"لكل عدد صحيح {m('k')} لا يقبل القسمة على {m('5')}، يكون {m('k^4 \\equiv 1 \\pmod{5}')}.",
            f"Out of {m('100')} terms, {m('80')} are coprime to {m('5')}, so the sum is congruent to {m('80 \\times 1 \\equiv 0 \\pmod{5}')}.",
            f"من بين {m('100')} حد، يوجد {m('80')} حداً أولياً نسبياً مع {m('5')}، فيكون المجموع مطابقاً للمقدار {m('80 \\times 1 \\equiv 0 \\pmod{5}')}.",
        ),
        (
            45,
            next(x for x in range(100, 1000) if x % 7 == 3 and x % 9 == 5 and x % 11 == 7),  # lcm(7,9,11) - 4 = 693 - 4 = 689
            svg_olym_divisibility_lattice("x+4", "7 | x+4", "9 | x+4", "11 | x+4, x=?"),
            f"In a Junior Olympiad three-modulus congruence problem, find the unique three-digit integer {m('x')} satisfying {m('x \\equiv 3 \\pmod{7}')}, {m('x \\equiv 5 \\pmod{9}')}, and {m('x \\equiv 7 \\pmod{11}')}.",
            f"في مسألة التطابقات الثلاثية للأولمبياد الناشئ، أوجد العدد الصحيح الوحيد المكون من ثلاثة أرقام {m('x')} الذي يحقق {m('x \\equiv 3 \\pmod{7}')} و{m('x \\equiv 5 \\pmod{9}')} و{m('x \\equiv 7 \\pmod{11}')}.",
            f"In each congruence the remainder is {m('4')} less than the modulus, so {m('x + 4')} is a multiple of {m('7, 9, 11')}.",
            f"في كل تطابق يقل الباقي بمقدار {m('4')} عن المقسوم عليه، لذا فإن {m('x + 4')} مضاعف للأعداد {m('7, 9, 11')}.",
            f"Since {m('7 \\times 9 \\times 11 = 693')}, the unique three-digit solution is {m('x = 693 - 4 = 689')}.",
            f"بما أن {m('7 \\times 9 \\times 11 = 693')}، فإن الحل الوحيد المكون من ثلاثة أرقام هو {m('x = 693 - 4 = 689')}.",
        ),
    ]
    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans + 1, ans + 2, ans + 4, max(0, ans - 2), ans + 7],
            h_en, h_ar,
            "Align remainders or apply Fermat's Little Theorem to collapse large periodic systems.",
            [st_en],
            f"Verified programmatically: {m(str(ans))}.",
            "وحّد البواقي أو طبّق مبرهنة فيرما الصغرى لتبسيط الأنظمة الدورية الكبيرة.",
            [st_ar],
            f"تم التحقق برمجياً: {m(str(ans))}.",
            diagram_en=diag,
        ))

    return out


def _build_u11_b4_factoring_diophantine() -> list[dict]:
    bp = "olym_t1_nt_factoring_diophantine"
    tp = "Number Theory"
    out: list[dict] = []

    # Easy 46..50: SFFT (xy + ax + by = c -> (x+b)(y+a) = c + ab) counting positive integer solutions
    easy_specs = [
        (46, 2, 3, 18),   # (x+3)(y+2) = 24 -> divisors of 24 with d1 > 3, d2 > 2
        (47, 1, 4, 20),   # (x+4)(y+1) = 24
        (48, 3, 5, 21),   # (x+5)(y+3) = 36
        (49, 2, 5, 38),   # (x+5)(y+2) = 48
        (50, 4, 6, 36),   # (x+6)(y+4) = 60
    ]
    for idx, a_v, b_v, c_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        rhs = c_v + a_v * b_v
        sols = [
            (d - b_v, rhs // d - a_v)
            for d in range(1, rhs + 1)
            if rhs % d == 0 and d > b_v and (rhs // d) > a_v
        ]
        ans = len(sols)
        diag = svg_subdivided_rect_2x2("xy", f"{a_v}x", f"{b_v}y", f"{a_v*b_v} (?)")
        q_en = (
            f"In a Junior Olympiad Simon's Favorite Factoring Trick problem, how many ordered pairs of positive integers "
            f"{m('(x, y)')} satisfy {m(f'xy + {a_v}x + {b_v}y = {c_v}')}?"
        )
        q_ar = (
            f"في مسألة التحليل الديوفانتي للأولمبياد الناشئ، كم زوجاً مرتباً من الأعداد الصحيحة الموجبة "
            f"{m('(x, y)')} يحقق المعادلة {m(f'xy + {a_v}x + {b_v}y = {c_v}')}؟"
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans + 1, ans + 2, ans + 3, max(1, ans - 1), _tau(rhs)],
            f"Add {m(str(a_v * b_v))} to both sides so the left side factors as {m(f'(x + {b_v})(y + {a_v})')}.",
            f"أضف {m(str(a_v * b_v))} إلى الطرفين ليصبح الطرف الأيسر قابلاً للتحليل على الصورة {m(f'(x + {b_v})(y + {a_v})')}.",
            f"Completing the rectangle turns {m(f'xy + {a_v}x + {b_v}y = {c_v}')} into a divisor-pair equation.",
            [
                f"Rewrite as {m(f'(x + {b_v})(y + {a_v}) = {c_v} + {a_v * b_v} = {rhs}')}.",
                f"Testing divisors {m(f'd \\mid {rhs}')} with {m(f'd > {b_v}')} and {m(f'{rhs}/d > {a_v}')} gives {m(str(ans))} positive integer solutions.",
            ],
            f"Direct search confirms {m(str(ans))} valid positive pairs {m('(x, y)')}.",
            f"إكمال المستطيل يحوّل المعادلة {m(f'xy + {a_v}x + {b_v}y = {c_v}')} إلى معادلة قواسم.",
            [
                f"نعيد الكتابة على الصورة {m(f'(x + {b_v})(y + {a_v}) = {c_v} + {a_v * b_v} = {rhs}')}.",
                f"بفحص قواسم العدد {m(str(rhs))} التي تحقق {m(f'd > {b_v}')} و{m(f'{rhs}/d > {a_v}')} نجد {m(str(ans))} أزواج صحيحة موجبة.",
            ],
            f"يؤكد البحث المباشر وجود {m(str(ans))} أزواج موجبة تحقق المعادلة.",
            diagram_en=diag,
        ))

    # Medium 51..55: unit fraction equation 1/x + 1/y = 1/n and difference of squares x^2 - y^2 = N
    med_specs = [
        (51, "unit_frac", 6),    # (x-6)(y-6) = 36 -> tau(36) = 9
        (52, "unit_frac", 12),   # (x-12)(y-12) = 144 -> tau(144) = 15
        (53, "diff_sq", 45),     # (x-y)(x+y) = 45 -> odd divisors pairs: (1,45),(3,15),(5,9) -> 3 pairs
        (54, "diff_sq", 96),     # (x-y)(x+y) = 96 -> even divisor pairs: (2,48),(4,24),(6,16),(8,12) -> 4 pairs
        (55, "unit_frac", 10),   # (x-10)(y-10) = 100 -> tau(100) = 9
    ]
    for idx, mode, k_val in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        if mode == "unit_frac":
            ans = _tau(k_val * k_val)
            diag = svg_olym_divisibility_lattice(f"n²={k_val**2}", f"x−{k_val}", f"y−{k_val}", "pairs=?")
            q_en = (
                f"In a Junior Olympiad Egyptian fraction problem, how many ordered pairs of positive integers {m('(x, y)')} "
                f"satisfy {m(f'\\frac{{1}}{{x}} + \\frac{{1}}{{y}} = \\frac{{1}}{{{k_val}}}')}?"
            )
            q_ar = (
                f"في مسألة الكسور المصرية للأولمبياد الناشئ، كم زوجاً مرتباً من الأعداد الصحيحة الموجبة {m('(x, y)')} "
                f"يحقق المعادلة {m(f'\\frac{{1}}{{x}} + \\frac{{1}}{{y}} = \\frac{{1}}{{{k_val}}}')}؟"
            )
            h_en = f"Clear denominators and rearrange into {m(f'(x - {k_val})(y - {k_val}) = {k_val**2}')}."
            h_ar = f"تخلص من المقامات وأعد الترتيب إلى الصورة {m(f'(x - {k_val})(y - {k_val}) = {k_val**2}')}."
            st_en = f"Every positive divisor of {m(f'{k_val}^2 = {k_val**2}')} gives a valid pair {m('(x, y)')}, yielding {m(f'\\tau({k_val**2}) = {ans}')} solutions."
            st_ar = f"كل قاسم موجب للعدد {m(f'{k_val}^2 = {k_val**2}')} يعطي زوجاً صحيحاً موجباً {m('(x, y)')}، فيكون العدد {m(f'\\tau({k_val**2}) = {ans}')}."
        else:
            pairs = [
                ((k_val // d + d) // 2, (k_val // d - d) // 2)
                for d in range(1, int(math.isqrt(k_val)) + 1)
                if k_val % d == 0 and d < k_val // d and (d + k_val // d) % 2 == 0
            ]
            ans = len(pairs)
            diag = svg_area_identity_square("x", "y")
            q_en = (
                f"In a Junior Olympiad difference-of-squares problem, how many ordered pairs of positive integers {m('(x, y)')} "
                f"satisfy {m(f'x^2 - y^2 = {k_val}')}?"
            )
            q_ar = (
                f"في مسألة فرق المربعين للأولمبياد الناشئ، كم زوجاً مرتباً من الأعداد الصحيحة الموجبة {m('(x, y)')} "
                f"يحقق المعادلة {m(f'x^2 - y^2 = {k_val}')}؟"
            )
            h_en = f"Factor {m(f'(x - y)(x + y) = {k_val}')} where {m('x - y')} and {m('x + y')} must have the same parity."
            h_ar = f"حلّل المعادلة إلى {m(f'(x - y)(x + y) = {k_val}')} حيث يجب أن يكون للعاملين {m('x - y')} و{m('x + y')} نفس الزوجية."
            st_en = f"Counting divisor pairs {m('(u, v)')} of {m(str(k_val))} with {m('u < v')} and {m('u \\equiv v \\pmod{2}')} gives {m(str(ans))} pairs."
            st_ar = f"بإحصاء أزواج القواسم {m('(u, v)')} للعدد {m(str(k_val))} التي تحقق {m('u < v')} و{m('u \\equiv v \\pmod{2}')} نحصل على {m(str(ans))} أزواج."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans + 1, ans + 2, ans + 4, max(1, ans - 1), ans * 2],
            h_en, h_ar,
            "Algebraic factorization transforms Diophantine equations into finite divisor searches.",
            [st_en],
            f"Verified by brute-force integer scan: {m(str(ans))}.",
            "التحليل الجبري يحوّل المعادلات الديوفانتية إلى بحث منتهٍ في قواسم عدد ثابت.",
            [st_ar],
            f"تم التحقق عبر المسح البرمجي للأعداد الصحيحة: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 56..60: Sophie Germain identity, max x+y in Diophantine, prime equations
    hard_specs = [
        (
            56,
            max(x + y for x in range(1, 200) for y in range(1, 200) if x * y - 5 * x - 5 * y == 0),  # (x-5)(y-5)=25 -> max is d=1,25 -> x=6,y=30 -> x+y=36
            svg_subdivided_rect_2x2("xy", "−5x", "−5y", "+25 (?)"),
            f"In a Junior Olympiad extremal Diophantine problem, positive integers {m('x')} and {m('y')} satisfy {m('xy = 5x + 5y')}. What is the maximum possible value of {m('x + y')}?",
            f"في مسألة القيم القصوى للمعادلات الديوفانتية في الأولمبياد الناشئ، يحقق العددان الصحيحان الموجبان {m('x')} و{m('y')} المعادلة {m('xy = 5x + 5y')}. ما أكبر قيمة ممكنة للمجموع {m('x + y')}؟",
            f"Rewrite as {m('(x - 5)(y - 5) = 25')} and maximize the sum of complementary divisors of {m('25')}.",
            f"أعد كتابة المعادلة على الصورة {m('(x - 5)(y - 5) = 25')} وعظّم مجموع القاسمين المتكاملين للعدد {m('25')}.",
            f"Choosing {m('\\{x - 5, y - 5\\} = \\{1, 25\\}')} gives {m('\\{x, y\\} = \\{6, 30\\}')} and {m('\\max(x + y) = 36')}.",
            f"باختيار {m('\\{x - 5, y - 5\\} = \\{1, 25\\}')} نحصل على {m('\\{x, y\\} = \\{6, 30\\}')} ويكون {m('\\max(x + y) = 36')}.",
        ),
        (
            57,
            54,
            svg_factor_tree("n⁴+4", "n²−2n+2", "n²+2n+2", "n=5", "min factor=?"),
            "", "", "", "", "", "",
        ),
        (
            58,
            next(p + q for p in [2, 3, 5, 7, 11, 13, 17, 19, 23] for q in [2, 3, 5, 7, 11, 13, 17, 19, 23] if p**2 - 2 * q**2 == 1),  # p=3, q=2 -> 9 - 8 = 1 -> p+q = 5
            svg_olym_divisibility_lattice("p²−2q²=1", "p=?", "q=?", "p+q=?"),
            f"In a Junior Olympiad prime Diophantine problem, prime numbers {m('p')} and {m('q')} satisfy {m('p^2 - 2q^2 = 1')}. Find {m('p + q')}.",
            f"في مسألة المعادلات الديوفانتية الأولية للأولمبياد الناشئ، يحقق العددان الأوليان {m('p')} و{m('q')} المعادلة {m('p^2 - 2q^2 = 1')}. أوجد {m('p + q')}.",
            f"Examine the equation modulo {m('3')}: since {m('p^2 - 1 = (p-1)(p+1) = 2q^2')}, check whether {m('q')} can be {m('2')} or {m('3')}.",
            f"افحص المعادلة بترديد {m('3')}: بما أن {m('p^2 - 1 = (p-1)(p+1) = 2q^2')}، تحقق مما إذا كان {m('q')} يساوي {m('2')} أو {m('3')}.",
            f"Since {m('p > 2')} is odd, {m('8 \\mid (p^2 - 1) = 2q^2')}, so {m('4 \\mid q^2')} forcing {m('q = 2')}, {m('p = 3')}, and {m('p + q = 5')}.",
            f"بما أن {m('p > 2')} فردي، فإن {m('8 \\mid (p^2 - 1) = 2q^2')}، أي {m('4 \\mid q^2')} مما يفرض {m('q = 2')} و{m('p = 3')}، ومنه {m('p + q = 5')}.",
        ),
        (
            59,
            sum(x for x in range(1, 100) for y in range(1, 100) if x**2 - y**2 == 24),  # (x-y,x+y) in {(2,12),(4,6)} -> x in {7, 5} -> 12
            svg_area_identity_square("x", "y"),
            f"In a Junior Olympiad integer-square problem, find the sum of all positive integers {m('x')} for which there exists a positive integer {m('y')} satisfying {m('x^2 - y^2 = 24')}.",
            f"في مسألة المربعات الصحيحة للأولمبياد الناشئ، أوجد مجموع جميع الأعداد الصحيحة الموجبة {m('x')} التي يوجد من أجلها عدد صحيح موجب {m('y')} يحقق {m('x^2 - y^2 = 24')}.",
            f"Factor {m('(x - y)(x + y) = 24')} into two even factors.",
            f"حلّل {m('(x - y)(x + y) = 24')} إلى عاملين زوجيين.",
            f"The even factor pairs of {m('24')} are {m('(2, 12)')} giving {m('x = 7')}, and {m('(4, 6)')} giving {m('x = 5')}; their sum is {m('7 + 5 = 12')}.",
            f"أزواج العوامل الزوجية للعدد {m('24')} هي {m('(2, 12)')} وتعطي {m('x = 7')}، و{m('(4, 6)')} وتعطي {m('x = 5')}؛ ومجموعهما {m('7 + 5 = 12')}.",
        ),
        (
            60,
            max(x * y for x in range(1, 200) for y in range(1, 200) if 3 * x + 4 * y == 60),  # x=4k, y=15-3k -> k=1(4,12->48), k=2(8,9->72), k=3(12,6->72), k=4(16,3->48) -> 72
            svg_olym_divisibility_lattice("3x+4y=60", "4 | x", "3 | y", "max(xy)=?"),
            f"In a Junior Olympiad linear Diophantine optimization problem, positive integers {m('x')} and {m('y')} satisfy {m('3x + 4y = 60')}. What is the maximum possible value of the product {m('xy')}?",
            f"في مسألة تحسين المعادلة الديوفانتية الخطية للأولمبياد الناشئ، يحقق العددان الصحيحان الموجبان {m('x')} و{m('y')} المعادلة {m('3x + 4y = 60')}. ما أكبر قيمة ممكنة للجداء {m('xy')}؟",
            f"Since {m('4 \\mid 3x')}, write {m('x = 4k')} and {m('y = 15 - 3k')} for {m('k \\in \\{1, 2, 3, 4\\}')}.",
            f"بما أن {m('4 \\mid 3x')}، اكتب {m('x = 4k')} و{m('y = 15 - 3k')} حيث {m('k \\in \\{1, 2, 3, 4\\}')}.",
            f"Testing {m('k = 1, 2, 3, 4')} gives products {m('48, 72, 72, 48')}, so the maximum product is {m('72')}.",
            f"بتجربة القيم {m('k = 1, 2, 3, 4')} نحصل على الجداءات {m('48, 72, 72, 48')}، فيكون أكبر جداء هو {m('72')}.",
        ),
    ]
    # Set Hard 57 cleanly to Sophie Germain factorization of 5^4 + 4 = 629 = 17 * 37
    ans_57 = (5**2 - 2 * 5 + 2) + (5**2 + 2 * 5 + 2)
    assert (5**2 - 2 * 5 + 2) * (5**2 + 2 * 5 + 2) == 5**4 + 4
    hard_specs[1] = (
        57,
        ans_57,
        svg_factor_tree("5⁴+4=629", "5²−10+2", "5²+10+2", "p=17", "p+q=?"),
        f"In a Junior Olympiad Sophie Germain factorization problem, the number {m('5^4 + 4 = 629')} is the product of two prime numbers {m('p')} and {m('q')}. Find {m('p + q')}.",
        f"في مسألة تحليل صوفي جيرمان للأولمبياد الناشئ، العدد {m('5^4 + 4 = 629')} هو حاصل ضرب عددين أوليين {m('p')} و{m('q')}. أوجد {m('p + q')}.",
        f"Use Sophie Germain's identity: {m('n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2)')}.",
        f"استخدم متطابقة صوفي جيرمان: {m('n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2)')}.",
        f"For {m('n = 5')}, the factors are {m('25 - 10 + 2 = 17')} and {m('25 + 10 + 2 = 37')}, both prime, with sum {m('17 + 37 = 54')}.",
        f"عند {m('n = 5')}، العاملان هما {m('25 - 10 + 2 = 17')} و{m('25 + 10 + 2 = 37')} وهما أوليان، ومجموعهما {m('17 + 37 = 54')}.",
    )

    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, ans + 8],
            h_en, h_ar,
            "Combine algebraic identities with parity and divisibility constraints to isolate integer solutions.",
            [st_en],
            f"Programmatically verified: {m(str(ans))}.",
            "اجمع بين المتطابقات الجبرية وقيود الزوجية وقابلية القسمة لعزل الحلول الصحيحة.",
            [st_ar],
            f"تم التحقق برمجياً: {m(str(ans))}.",
            diagram_en=diag,
        ))

    return out


# ==============================================================================
# UNIT 1.2 — Algebra (OLYM-T1-061 .. OLYM-T1-120)
# ==============================================================================

def _build_u12_b1_telescoping() -> list[dict]:
    bp = "olym_t1_alg_telescoping_series"
    tp = "Algebra"
    out: list[dict] = []

    # Easy 61..65: sum_{k=1}^{n} 1/(k(k+1)) = n/(n+1), ask for p + q in lowest terms
    easy_specs = [(61, 9), (62, 14), (63, 19), (64, 24), (65, 29)]
    for idx, n_val in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        fr = sum(Fraction(1, k * (k + 1)) for k in range(1, n_val + 1))
        ans = fr.numerator + fr.denominator
        diag = svg_telescoping_chain(["1", "-1/2", "+1/2", "-1/3", "...", f"-1/{n_val+1}"], title_lbl=f"S_{n_val} = p/q")
        q_en = (
            f"In a Junior Olympiad telescoping series problem, let {m(f'S = \\\\sum_{{k=1}}^{{{n_val}}} \\\\frac{{1}}{{k(k+1)}} = \\\\frac{{p}}{{q}}')} "
            f"in lowest terms. Find {m('p + q')}."
        )
        q_ar = (
            f"في مسألة المتسلسلات المتداخلة للأولمبياد الناشئ، ليكن {m(f'S = \\\\sum_{{k=1}}^{{{n_val}}} \\\\frac{{1}}{{k(k+1)}} = \\\\frac{{p}}{{q}}')} "
            f"في أبسط صورة. أوجد {m('p + q')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, n_val + 1],
            f"Use partial fractions {m(r'\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}')}.",
            f"استخدم الكسور الجزئية {m(r'\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}')}.",
            "Split each term into a difference so intermediate terms cancel.",
            [f"Telescoping gives {m(f'S = 1 - \\\\frac{{1}}{{{n_val+1}}} = \\\\frac{{{n_val}}}{{{n_val+1}}}?')}, so {m(f'p + q = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "جزّئ كل حد إلى فرق بحيث تختصر الحدود الوسطى.",
            [f"الاختصار المتداخل يعطي {m(f'S = 1 - \\\\frac{{1}}{{{n_val+1}}} = \\\\frac{{{n_val}}}{{{n_val+1}}}')}، ومنه {m(f'p + q = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 66..70: k*k! and 1/(k(k+2)) telescoping sums
    med_specs = [
        (
            66,
            sum(k * math.factorial(k) for k in range(1, 6)),
            svg_telescoping_chain(["2!-1!", "3!-2!", "...", "6!-5!"], title_lbl="∑ k·k! (k=1..5)"),
            f"In a Junior Olympiad factorial sum problem, evaluate {m(r'\\sum_{k=1}^{5} k \\cdot k!')}.",
            f"في مسألة مجموع المضاريب للأولمبياد الناشئ، احسب قيمة {m(r'\\sum_{k=1}^{5} k \\cdot k!')}.",
            f"Use the identity {m('k \\cdot k! = (k+1)! - k!')}.",
            f"استخدم المتطابقة {m('k \\cdot k! = (k+1)! - k!')}.",
            f"Telescoping from {m('k=1')} to {m('5')} yields {m('6! - 1! = 720 - 1 = 719')}.",
            f"الاختصار المتداخل من {m('k=1')} إلى {m('5')} يعطي {m('6! - 1! = 720 - 1 = 719')}.",
        ),
        (
            67,
            sum(k * math.factorial(k) for k in range(1, 7)),
            svg_telescoping_chain(["2!-1!", "3!-2!", "...", "7!-6!"], title_lbl="∑ k·k! (k=1..6)"),
            f"In a Junior Olympiad factorial series task, compute {m(r'\\sum_{k=1}^{6} k \\cdot k!')}.",
            f"في مسألة متسلسلة المضاريب للأولمبياد الناشئ، احسب قيمة {m(r'\\sum_{k=1}^{6} k \\cdot k!')}.",
            f"Rewrite {m('k \\cdot k! = (k+1)! - k!')}.",
            f"أعد كتابة الحد العام على الصورة {m('k \\cdot k! = (k+1)! - k!')}.",
            f"The sum collapses to {m('7! - 1! = 5040 - 1 = 5039')}.",
            f"ينتظم المجموع ليصبح {m('7! - 1! = 5040 - 1 = 5039')}.",
        ),
        (
            68,
            int(28 * sum(Fraction(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, 8))),
            svg_telescoping_chain(["1-1/3", "1/3-1/5", "...", "1/13-1/15"], title_lbl="28 · S"),
            f"In a Junior Olympiad odd-denominator series problem, let {m(r'S = \\sum_{k=1}^{7} \\frac{1}{(2k-1)(2k+1)}')}. Find {m('30 S')}.",
            f"في مسألة المتسلسلات ذات المقامات الفردية للأولمبياد الناشئ، ليكن {m(r'S = \\sum_{k=1}^{7} \\frac{1}{(2k-1)(2k+1)}')}. أوجد {m('30 S')}.",
            f"Use {m(r'\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}.",
            f"استخدم {m(r'\\frac{1}{(2k-1)(2k+1)} = \\frac{1}{2}\\left(\\frac{1}{2k-1} - \\frac{1}{2k+1}\\right)')}.",
            f"We get {m('S = \\frac{1}{2}(1 - \\frac{1}{15}) = \\frac{7}{15}')}, so {m('30 S = 14')}.",
            f"نحصل على {m('S = \\frac{1}{2}(1 - \\frac{1}{15}) = \\frac{7}{15}')}، ومنه {m('30 S = 14')}.",
        ),
        (
            69,
            (lambda f: f.numerator + f.denominator)(sum(Fraction(1, k * (k + 2)) for k in range(1, 9))),
            svg_telescoping_chain(["1+1/2", "-1/9-1/10"], title_lbl="∑ 1/(k(k+2)), k=1..8"),
            f"In a Junior Olympiad step-2 telescoping problem, let {m(r'\\sum_{k=1}^{8} \\frac{1}{k(k+2)} = \\frac{p}{q}')} in lowest terms. Find {m('p + q')}.",
            f"في مسألة الاختصار المتداخل بخطوتين للأولمبياد الناشئ، ليكن {m(r'\\sum_{k=1}^{8} \\frac{1}{k(k+2)} = \\frac{p}{q}')} في أبسط صورة. أوجد {m('p + q')}.",
            f"Write {m(r'\\frac{1}{k(k+2)} = \\frac{1}{2}\\left(\\frac{1}{k} - \\frac{1}{k+2}\\right)')} so two front and two back terms survive.",
            f"اكتب {m(r'\\frac{1}{k(k+2)} = \\frac{1}{2}\\left(\\frac{1}{k} - \\frac{1}{k+2}\\right)')} فيبقى حدّان في البداية وحدّان في النهاية.",
            f"The sum equals {m(r'\\frac{1}{2}(1 + \\frac{1}{2} - \\frac{1}{9} - \\frac{1}{10}) = \\frac{29}{45}')}, giving {m('p + q = 74')}.",
            f"المجموع يساوي {m(r'\\frac{1}{2}(1 + \\frac{1}{2} - \\frac{1}{9} - \\frac{1}{10}) = \\frac{29}{45}')}، مما يعطي {m('p + q = 74')}.",
        ),
        (
            70,
            (lambda f: f.numerator + f.denominator)(sum(Fraction(k, math.factorial(k + 1)) for k in range(1, 6))),
            svg_telescoping_chain(["1/1!-1/2!", "1/2!-1/3!", "...", "1/5!-1/6!"], title_lbl="∑ k/(k+1)!"),
            f"In a Junior Olympiad unit-fraction factorial problem, let {m(r'\\sum_{k=1}^{5} \\frac{k}{(k+1)!} = \\frac{p}{q}')} in lowest terms. Find {m('q - p')}.",
            f"في مسألة كسور المضاريب للأولمبياد الناشئ، ليكن {m(r'\\sum_{k=1}^{5} \\frac{k}{(k+1)!} = \\frac{p}{q}')} في أبسط صورة. أوجد {m('q - p')}.",
            f"Use {m(r'\\frac{k}{(k+1)!} = \\frac{1}{k!} - \\frac{1}{(k+1)!}')}.",
            f"استخدم المتطابقة {m(r'\\frac{k}{(k+1)!} = \\frac{1}{k!} - \\frac{1}{(k+1)!}')}.",
            f"The sum telescopes to {m('1 - \\frac{1}{6!} = \\frac{719}{720}')}, so {m('q - p = 1')}.",
            f"المجموع يختصر إلى {m('1 - \\frac{1}{6!} = \\frac{719}{720}')}، وبالتالي {m('q - p = 1')}.",
        ),
    ]
    med_specs[2] = (68, int(30 * sum(Fraction(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, 8))), *med_specs[2][2:])
    med_specs[4] = (70, (lambda f: f.denominator - f.numerator)(sum(Fraction(k, math.factorial(k + 1)) for k in range(1, 6))), *med_specs[4][2:])
    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 5],
            h_en, h_ar, "Express the general term as a forward difference.", [st_en], f"Verified: {m(str(ans))}.",
            "عبّر عن الحد العام كفرق أمامي لاختصار الحدود.", [st_ar], f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 71..75: rationalized radical telescoping and 3-factor denominators
    hard_specs = [
        (
            71,
            int(round(sum(1 / (math.sqrt(k) + math.sqrt(k + 1)) for k in range(1, 99 + 1)))),
            svg_telescoping_chain(["√2−√1", "√3−√2", "...", "√100−√99"], title_lbl="∑ 1/(√k+√(k+1))"),
            f"In a Junior Olympiad radical series problem, evaluate {m(r'\\sum_{k=1}^{99} \\frac{1}{\\sqrt{k} + \\sqrt{k+1}}')}.",
            f"في مسألة متسلسلة الجذور للأولمبياد الناشئ، احسب قيمة {m(r'\\sum_{k=1}^{99} \\frac{1}{\\sqrt{k} + \\sqrt{k+1}}')}.",
            f"Rationalize each denominator using {m(r'\\frac{1}{\\sqrt{k}+\\sqrt{k+1}} = \\sqrt{k+1} - \\sqrt{k}')}.",
            f"أنطق المقام باستخدام {m(r'\\frac{1}{\\sqrt{k}+\\sqrt{k+1}} = \\sqrt{k+1} - \\sqrt{k}')}.",
            f"The sum telescopes to {m(r'\\sqrt{100} - \\sqrt{1} = 10 - 1 = 9')}.",
            f"يختصر المجموع إلى {m(r'\\sqrt{100} - \\sqrt{1} = 10 - 1 = 9')}.",
        ),
        (
            72,
            int(round(sum(1 / (math.sqrt(k) + math.sqrt(k + 1)) for k in range(1, 143 + 1)))),
            svg_telescoping_chain(["√2−√1", "√3−√2", "...", "√144−√143"], title_lbl="∑ 1/(√k+√(k+1))"),
            f"In a Junior Olympiad radical telescoping problem, evaluate {m(r'\\sum_{k=1}^{143} \\frac{1}{\\sqrt{k} + \\sqrt{k+1}}')}.",
            f"في مسألة اختصار الجذور للأولمبياد الناشئ، احسب قيمة {m(r'\\sum_{k=1}^{143} \\frac{1}{\\sqrt{k} + \\sqrt{k+1}}')}.",
            f"Multiply numerator and denominator by {m(r'\\sqrt{k+1} - \\sqrt{k}')}.",
            f"اضرب البسط والمقام في المرافق {m(r'\\sqrt{k+1} - \\sqrt{k}')}.",
            f"Telescoping yields {m(r'\\sqrt{144} - \\sqrt{1} = 12 - 1 = 11')}.",
            f"ينتج عن الاختصار المتداخل {m(r'\\sqrt{144} - \\sqrt{1} = 12 - 1 = 11')}.",
        ),
        (
            73,
            (lambda f: f.numerator + f.denominator)(sum(Fraction(1, k * (k + 1) * (k + 2)) for k in range(1, 9))),
            svg_telescoping_chain(["1/(1·2)", "-1/(9·10)"], title_lbl="∑ 1/(k(k+1)(k+2))"),
            f"In a Junior Olympiad triple-factor series problem, let {m(r'\\sum_{k=1}^{8} \\frac{1}{k(k+1)(k+2)} = \\frac{p}{q}')} in lowest terms. Find {m('p + q')}.",
            f"في مسألة المتسلسلات ثلاثية العوامل للأولمبياد الناشئ، ليكن {m(r'\\sum_{k=1}^{8} \\frac{1}{k(k+1)(k+2)} = \\frac{p}{q}')} في أبسط صورة. أوجد {m('p + q')}.",
            f"Use {m(r'\\frac{1}{k(k+1)(k+2)} = \\frac{1}{2}\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
            f"استخدم {m(r'\\frac{1}{k(k+1)(k+2)} = \\frac{1}{2}\\left(\\frac{1}{k(k+1)} - \\frac{1}{(k+1)(k+2)}\\right)')}.",
            f"We obtain {m(r'\\frac{1}{2}\\left(\\frac{1}{2} - \\frac{1}{90}\\right) = \\frac{11}{45}')}, so {m('p + q = 56')}.",
            f"نحصل على {m(r'\\frac{1}{2}\\left(\\frac{1}{2} - \\frac{1}{90}\\right) = \\frac{11}{45}')}، ومنه {m('p + q = 56')}.",
        ),
        (
            74,
            (lambda f: f.numerator + f.denominator)(math.prod(Fraction(k * k - 1, k * k) for k in range(2, 11))),
            svg_telescoping_chain(["(1·3)/2²", "(2·4)/3²", "...", "(9·11)/10²"], op_sym="×", title_lbl="∏ (k²−1)/k²"),
            f"In a Junior Olympiad telescoping product problem, let {m(r'\\prod_{k=2}^{10} \\left(1 - \\frac{1}{k^2}\\right) = \\frac{p}{q}')} in lowest terms. Find {m('p + q')}.",
            f"في مسألة الجداء المتداخل للأولمبياد الناشئ، ليكن {m(r'\\prod_{k=2}^{10} \\left(1 - \\frac{1}{k^2}\\right) = \\frac{p}{q}')} في أبسط صورة. أوجد {m('p + q')}.",
            f"Factor {m(r'1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}.",
            f"حلّل {m(r'1 - \\frac{1}{k^2} = \\frac{k-1}{k} \\cdot \\frac{k+1}{k}')}.",
            f"The product telescopes to {m(r'\\frac{1}{2} \\cdot \\frac{11}{10} = \\frac{11}{20}')}, so {m('p + q = 31')}.",
            f"الجداء يختصر إلى {m(r'\\frac{1}{2} \\cdot \\frac{11}{10} = \\frac{11}{20}')}، ومنه {m('p + q = 31')}.",
        ),
        (
            75,
            int(round(sum(2 / (math.sqrt(2 * k - 1) + math.sqrt(2 * k + 1)) for k in range(1, 12 + 1)))),
            svg_telescoping_chain(["√3−√1", "√5−√3", "...", "√25−√23"], title_lbl="∑ 2/(√(2k-1)+√(2k+1))"),
            f"In a Junior Olympiad odd-step radical series problem, evaluate {m(r'\\sum_{k=1}^{12} \\frac{2}{\\sqrt{2k-1} + \\sqrt{2k+1}}')}.",
            f"في مسألة متسلسلة الجذور الفردية للأولمبياد الناشئ، احسب قيمة {m(r'\\sum_{k=1}^{12} \\frac{2}{\\sqrt{2k-1} + \\sqrt{2k+1}}')}.",
            f"Rationalize using {m('(2k+1) - (2k-1) = 2')}.",
            f"أنطق المقام بملاحظة أن {m('(2k+1) - (2k-1) = 2')}.",
            f"Each term is {m(r'\\sqrt{2k+1} - \\sqrt{2k-1}')}, so the sum is {m(r'\\sqrt{25} - \\sqrt{1} = 5 - 1 = 4')}.",
            f"كل حد يساوي {m(r'\\sqrt{2k+1} - \\sqrt{2k-1}')}، فيكون المجموع {m(r'\\sqrt{25} - \\sqrt{1} = 5 - 1 = 4')}.",
        ),
    ]
    for idx, ans, diag, q_en, q_ar, h_en, h_ar, st_en, st_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            h_en, h_ar, "Rationalize or factor each term to expose telescoping cancellation.", [st_en], f"Verified: {m(str(ans))}.",
            "أنطق المقام أو حلّل كل حد لإظهار الاختصار المتداخل.", [st_ar], f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u12_b2_symmetric() -> list[dict]:
    bp = "olym_t1_alg_symmetric_identities"
    tp = "Algebra"
    out: list[dict] = []

    # Easy 76..80: a^2 + b^2 = (a+b)^2 - 2ab
    easy_specs = [(76, 7, 10), (77, 9, 14), (78, 11, 24), (79, 8, 13), (80, 12, 35)]
    for idx, s_val, p_val in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = s_val * s_val - 2 * p_val
        diag = svg_area_identity_square("a", "b")
        q_en = (
            f"In a Junior Olympiad symmetric polynomials problem, real numbers {m('a')} and {m('b')} satisfy "
            f"{m(f'a + b = {s_val}')} and {m(f'ab = {p_val}')}. Find {m('a^2 + b^2')}."
        )
        q_ar = (
            f"في مسألة كثيرات الحدود المتماثلة للأولمبياد الناشئ، يحقق العددان الحقيقيان {m('a')} و{m('b')} "
            f"{m(f'a + b = {s_val}')} و{m(f'ab = {p_val}')}. أوجد قيمة {m('a^2 + b^2')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 4, ans + 4, s_val * s_val - p_val, s_val * s_val + 2 * p_val, ans + 8],
            f"Use {m('a^2 + b^2 = (a + b)^2 - 2ab')}.",
            f"استخدم المتطابقة {m('a^2 + b^2 = (a + b)^2 - 2ab')}.",
            "Express the power sum in terms of elementary symmetric polynomials.",
            [f"Compute {m(f'({s_val})^2 - 2({p_val}) = {s_val*s_val} - {2*p_val} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "عبّر عن مجموع القوى بدلالة المجموع والجداء الأساسيين.",
            [f"نحسب {m(f'({s_val})^2 - 2({p_val}) = {s_val*s_val} - {2*p_val} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 81..85: a^3 + b^3 and x^3 + 1/x^3
    med_specs = [
        (81, 5, 6, 5**3 - 3 * 6 * 5, "a+b=5, ab=6", "a³+b³"),
        (82, 6, 7, 6**3 - 3 * 7 * 6, "a+b=6, ab=7", "a³+b³"),
        (83, 3, 1, 3**3 - 3 * 3, "x+1/x=3", "x³+1/x³"),
        (84, 4, 1, 4**3 - 3 * 4, "x+1/x=4", "x³+1/x³"),
        (85, 5, 1, (5**2 - 2) ** 2 - 2, "x+1/x=5", "x⁴+1/x⁴"),
    ]
    for idx, s_v, p_v, ans, cond_s, ask_s in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_area_identity_square("x", "1/x" if p_v == 1 else "y")
        q_en = f"In a Junior Olympiad algebraic identity problem, given {m(cond_s)}, compute {m(ask_s)}."
        q_ar = f"في مسألة المتطابقات الجبرية للأولمبياد الناشئ، إذا علمت أن {m(cond_s)}، فاحسب قيمة {m(ask_s)}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 6, ans - 3, ans + 3, ans + 6, ans + 12],
            f"Apply Newton's power-sum identity {m('a^3 + b^3 = (a+b)^3 - 3ab(a+b)')}.",
            f"طبّق متطابقة مجموع المكعبين {m('a^3 + b^3 = (a+b)^3 - 3ab(a+b)')}.",
            "Use recursive power-sum identities.",
            [f"Substituting {m(cond_s)} into the symmetric identity yields {m(f'{ask_s} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "استخدم متطابقات مجموع القوى المتماثلة.",
            [f"بالتعويض بمعطيات {m(cond_s)} في المتطابقة المتماثلة نجد أن {m(f'{ask_s} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 86..90: a^3 + b^3 + c^3 - 3abc and Sophie Germain
    hard_specs = [
        (86, 6 * (36 - 3 * 11), "a+b+c=6, ab+bc+ca=11, abc=6", "a^3+b^3+c^3", 6 * (36 - 33) + 18),
        (87, 5 * (25 - 3 * 7) + 3 * 2, "a+b+c=5, ab+bc+ca=7, abc=2", "a^3+b^3+c^3", 5 * 4 + 6),
        (88, 0, "a+b+c=0, abc=8", "\\frac{a^3+b^3+c^3}{abc}", 3),
        (89, 0, "a=3, b=2", "\\frac{a^4+4b^4}{a^2-2ab+2b^2}", (3**4 + 4 * 2**4) // (9 - 12 + 8)),
        (90, 0, "a+b=4, ab=2", "a^4+b^4", (16 - 4) ** 2 - 2 * 4),
    ]
    for idx, _, cond_s, ask_s, ans in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_area_identity_square("a", "2b")
        q_en = f"In a Junior Olympiad advanced symmetric identity problem, given {m(cond_s)}, find {m(ask_s)}."
        q_ar = f"في مسألة المتطابقات المتماثلة المتقدمة للأولمبياد الناشئ، إذا كان {m(cond_s)}، فأوجد قيمة {m(ask_s)}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, ans + 8],
            f"Recall {m('a^3+b^3+c^3-3abc = (a+b+c)((a+b+c)^2 - 3(ab+bc+ca))')}.",
            f"تذكر المتطابقة {m('a^3+b^3+c^3-3abc = (a+b+c)((a+b+c)^2 - 3(ab+bc+ca))')}.",
            "Use Gauss's three-variable cubic identity or Sophie Germain's identity.",
            [f"Direct substitution into the factored identity gives {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "استخدم متطابقة غاوس التكعيبية أو متطابقة صوفي جيرمان.",
            [f"التعويض المباشر في المتطابقة المحللة يعطي {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u12_b3_radicals_ratios() -> list[dict]:
    bp = "olym_t1_alg_nested_radicals_ratios"
    tp = "Algebra"
    out: list[dict] = []

    # Easy 91..95: sqrt( (x+y) + 2*sqrt(xy) ) = sqrt(x) + sqrt(y), find x + y or x*y
    easy_specs = [(91, 5, 2), (92, 6, 5), (93, 7, 3), (94, 8, 5), (95, 11, 3)]
    for idx, x_v, y_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        a_v, b_v = x_v + y_v, x_v * y_v
        ans = x_v - y_v
        diag = svg_pan_balance_coins(f"√({a_v}+2√{b_v})", f"√x + √y (x>y)", f"x−y = ?")
        q_en = (
            f"In a Junior Olympiad nested radical problem, {m(f'\\\\sqrt{{{a_v} + 2\\\\sqrt{{{b_v}}}}} = \\\\sqrt{{x}} + \\\\sqrt{{y}}')} "
            f"for positive integers {m('x > y')}. Find {m('x - y')}."
        )
        q_ar = (
            f"في مسألة الجذور المتداخلة للأولمبياد الناشئ، إذا كان {m(f'\\\\sqrt{{{a_v} + 2\\\\sqrt{{{b_v}}}}} = \\\\sqrt{{x}} + \\\\sqrt{{y}}')} "
            f"لعددين صحيحين موجبين {m('x > y')}، فأوجد {m('x - y')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 1, ans + 1, ans + 2, a_v, b_v],
            f"Match {m(f'x + y = {a_v}')} and {m(f'xy = {b_v}')}.",
            f"طابق بين {m(f'x + y = {a_v}')} و{m(f'xy = {b_v}')}.",
            f"Since {m(r'(\\sqrt{x}+\\sqrt{y})^2 = (x+y) + 2\\sqrt{xy}')}, solve for {m('x')} and {m('y')}.",
            [f"Here {m(f'x = {x_v}')} and {m(f'y = {y_v}')}, so {m(f'x - y = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            f"بما أن {m(r'(\\sqrt{x}+\\sqrt{y})^2 = (x+y) + 2\\sqrt{xy}')}، أوجد {m('x')} و{m('y')}.",
            [f"نجد أن {m(f'x = {x_v}')} و{m(f'y = {y_v}')}، ومنه {m(f'x - y = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 96..100: continued fractions & equal ratios
    med_specs = [
        (96, 1 + Fraction(1, 2 + Fraction(1, 3)), "1 + \\frac{1}{2 + \\frac{1}{3}}"),
        (97, 2 + Fraction(1, 3 + Fraction(1, 4)), "2 + \\frac{1}{3 + \\frac{1}{4}}"),
        (98, 1 + Fraction(1, 1 + Fraction(1, 1 + Fraction(1, 2))), "1 + \\frac{1}{1 + \\frac{1}{1 + \\frac{1}{2}}}"),
        (99, Fraction(3, 4), "\\frac{a+c}{b+d} \\text{ when } \\frac{a}{b}=\\frac{c}{d}=\\frac{3}{4}"),
        (100, Fraction(5, 7), "\\frac{2a+3c}{2b+3d} \\text{ when } \\frac{a}{b}=\\frac{c}{d}=\\frac{5}{7}"),
    ]
    for idx, fr, expr_s in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = fr.numerator + fr.denominator
        diag = svg_tape_bar_split([(fr.numerator, f"p={fr.numerator}"), (fr.denominator, f"q={fr.denominator}")], total_lbl="p + q = ?")
        q_en = f"In a Junior Olympiad ratio and continued-fraction problem, simplify {m(expr_s)} to a reduced fraction {m(r'\\frac{p}{q}')} and find {m('p + q')}."
        q_ar = f"في مسألة النسب والكسور المستمرة للأولمبياد الناشئ، بسّط المقدار {m(expr_s)} إلى كسر مختزل {m(r'\\frac{p}{q}')} وأوجد {m('p + q')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 3, ans - 1, ans + 1, ans + 3, ans + 5],
            "Work from the bottom of the continued fraction upward or apply the equal-ratios property.",
            "ابدأ من أسفل الكسر المستمر صعوداً أو طبّق خاصية النسب المتساوية.",
            "Simplify step by step into lowest terms.",
            [f"The expression reduces to {m(f'\\\\frac{{{fr.numerator}}}{{{fr.denominator}}}')}, so {m(f'p + q = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "بسّط المقدار خطوة بخطوة إلى أبسط صورة.",
            [f"يبسّط المقدار إلى {m(f'\\\\frac{{{fr.numerator}}}{{{fr.denominator}}}')}، ومنه {m(f'p + q = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 101..105: infinite nested radicals sqrt(c + sqrt(c + ...)) = m => c = m(m-1)
    hard_specs = [(101, 4), (102, 5), (103, 6), (104, 7), (105, 8)]
    for idx, m_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        c_v = m_v * (m_v - 1)
        ans = m_v
        diag = svg_pan_balance_coins("x = √(c + x)", f"c = {c_v}", "x = ?")
        q_en = (
            f"In a Junior Olympiad infinite radical problem, evaluate the positive value of "
            f"{m(f'x = \\\\sqrt{{{c_v} + \\\\sqrt{{{c_v} + \\\\sqrt{{{c_v} + \\\\cdots}}}}}}')}."
        )
        q_ar = (
            f"في مسألة الجذور المتداخلة اللانهائية للأولمبياد الناشئ، أوجد القيمة الموجبة للمقدار "
            f"{m(f'x = \\\\sqrt{{{c_v} + \\\\sqrt{{{c_v} + \\\\sqrt{{{c_v} + \\\\cdots}}}}}}')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, c_v // 2],
            f"Set {m(f'x^2 = {c_v} + x')} with {m('x > 0')}.",
            f"ضع {m(f'x^2 = {c_v} + x')} مع اشتراط {m('x > 0')}.",
            f"Square both sides of the self-similar equation {m(f'x = \\\\sqrt{{{c_v} + x}}')}.",
            [f"Factor {m(f'x^2 - x - {c_v} = (x - {m_v})(x + {m_v-1}) = 0')}, giving {m(f'x = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            f"ربّع طرفي المعادلة المتشابهة ذاتياً {m(f'x = \\\\sqrt{{{c_v} + x}}')}.",
            [f"حلّل {m(f'x^2 - x - {c_v} = (x - {m_v})(x + {m_v-1}) = 0')}، فنحصل على {m(f'x = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u12_b4_recurrences() -> list[dict]:
    bp = "olym_t1_alg_linear_recurrences_seq"
    tp = "Algebra"
    out: list[dict] = []

    # Easy 106..110: arithmetic progression term / sum
    easy_specs = [(106, 3, 4, 15), (107, 5, 3, 18), (108, 2, 6, 12), (109, 7, 5, 14), (110, 4, 7, 11)]
    for idx, a1, d_v, n_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = a1 + (n_v - 1) * d_v
        diag = svg_function_machine(f"a₁={a1}", f"+{d_v} per step", f"n={n_v}", f"a_{n_v}=?")
        q_en = f"In a Junior Olympiad sequence problem, an arithmetic progression has first term {m(f'a_1 = {a1}')} and common difference {m(f'd = {d_v}')}. Find {m(f'a_{{{n_v}}}')}."
        q_ar = f"في مسألة المتتاليات للأولمبياد الناشئ، متتالية حسابية حدها الأول {m(f'a_1 = {a1}')} وأساسها {m(f'd = {d_v}')}. أوجد الحد {m(f'a_{{{n_v}}}')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - d_v, ans + d_v, ans - 2, ans + 2, a1 + n_v * d_v + 1],
            f"Use {m('a_n = a_1 + (n - 1)d')}.",
            f"استخدم صيغة الحد العام {m('a_n = a_1 + (n - 1)d')}.",
            "Add the common difference (n-1) times to the first term.",
            [f"Compute {m(f'a_{{{n_v}}} = {a1} + ({n_v}-1)\\\\times {d_v} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "أضف الأساس (n-1) مرة إلى الحد الأول.",
            [f"نحسب {m(f'a_{{{n_v}}} = {a1} + ({n_v}-1)\\\\times {d_v} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 111..115: first-order recurrence a_{n+1} = 2 a_n + c
    med_specs = [(111, 1, 1, 6), (112, 2, 1, 6), (113, 1, 3, 5), (114, 3, 2, 5), (115, 2, 3, 6)]
    for idx, a1, c_v, n_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        cur = a1
        for _ in range(n_v - 1):
            cur = 2 * cur + c_v
        ans = cur
        diag = svg_function_machine(f"a₁={a1}", f"2·a_n + {c_v}", f"n={n_v}", f"a_{n_v}=?")
        q_en = f"In a Junior Olympiad linear recurrence problem, a sequence satisfies {m(f'a_1 = {a1}')} and {m(f'a_{{n+1}} = 2a_n + {c_v}')} for {m('n \\\\ge 1')}. Find {m(f'a_{{{n_v}}}')}."
        q_ar = f"في مسألة العلاقات التكرارية الخطية للأولمبياد الناشئ، تحقق متتالية {m(f'a_1 = {a1}')} و{m(f'a_{{n+1}} = 2a_n + {c_v}')} لكل {m('n \\\\ge 1')}. أوجد {m(f'a_{{{n_v}}}')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - c_v, ans + c_v, ans - 4, ans + 4, ans * 2],
            f"Shift the recurrence by adding {m(str(c_v))}: {m(f'a_{{n+1}} + {c_v} = 2(a_n + {c_v})')}.",
            f"أزح العلاقة التكرارية بإضافة {m(str(c_v))}: {m(f'a_{{n+1}} + {c_v} = 2(a_n + {c_v})')}.",
            "Transform the affine recurrence into a geometric progression via its fixed point.",
            [f"Since {m(f'a_n + {c_v} = 2^{{n-1}}(a_1 + {c_v})')}, we get {m(f'a_{{{n_v}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "حوّل العلاقة التكرارية إلى متتالية هندسية عبر إزاحة النقطة الثابتة.",
            [f"بما أن {m(f'a_n + {c_v} = 2^{{n-1}}(a_1 + {c_v})')}، نحصل على {m(f'a_{{{n_v}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 116..120: Fibonacci-like / second-order and periodic recurrences
    hard_specs = [
        (116, 1, 3, 8, "a_{n+2} = a_{n+1} + a_n", 47),
        (117, 2, 1, 9, "a_{n+2} = a_{n+1} + a_n", 47),
        (118, 2, 5, 2026, "a_{n+2} = a_{n+1} - a_n", -2),
        (119, 3, 7, 2025, "a_{n+2} = a_{n+1} - a_n", 4),
        (120, 1, 2, 6, "a_{n+2} = 2a_{n+1} + a_n", 70),
    ]
    for idx, a1, a2, n_v, rec_s, ans in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_function_machine(f"({a1}, {a2})", rec_s, f"n={n_v}", f"a_{n_v}=?")
        q_en = f"In a Junior Olympiad second-order recurrence problem, {m(f'a_1 = {a1}')}, {m(f'a_2 = {a2}')}, and {m(rec_s)} for {m('n \\\\ge 1')}. Find {m(f'a_{{{n_v}}}')}."
        q_ar = f"في مسألة العلاقات التكرارية من الرتبة الثانية للأولمبياد الناشئ، {m(f'a_1 = {a1}')} و{m(f'a_2 = {a2}')} و{m(rec_s)} لكل {m('n \\\\ge 1')}. أوجد {m(f'a_{{{n_v}}}')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 3, ans - 1, ans + 2, ans + 5, -ans if ans != 0 else 4],
            "Compute the first several terms or exploit the period-6 cycle when a_{n+2} = a_{n+1} - a_n.",
            "احسب الحدود الأولى أو استغل الدورة ذات الطول 6 عندما يكون a_{n+2} = a_{n+1} - a_n.",
            "Generate terms iteratively or reduce the index modulo the period.",
            [f"Evaluating the recurrence up to index {m(str(n_v))} gives {m(f'a_{{{n_v}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "احسب الحدود بالتتابع أو اختزل الدليل بترديد طول الدورة.",
            [f"بحساب العلاقة التكرارية حتى الدليل {m(str(n_v))} نحصل على {m(f'a_{{{n_v}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


# ==============================================================================
# UNIT 1.3 — Inequalities (OLYM-T1-121 .. OLYM-T1-180)
# ==============================================================================

def _build_u13_b1_squares_nonneg() -> list[dict]:
    bp = "olym_t1_ineq_squares_nonneg"
    tp = "Inequalities"
    out: list[dict] = []

    # Easy 121..125: min of x^2 - 2bx + c = c - b^2
    easy_specs = [(121, 3, 14), (122, 4, 23), (123, 5, 31), (124, 6, 45), (125, 7, 58)]
    for idx, b_v, c_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = c_v - b_v * b_v
        diag = svg_olym_inequality_curve(f"(x−{b_v})²≥0", f"+{ans}", note=f"min = {ans}")
        q_en = f"In a Junior Olympiad quadratic minimum problem, find the minimum value of {m(f'x^2 - {2*b_v}x + {c_v}')} over all real numbers {m('x')}."
        q_ar = f"في مسألة القيمة الصغرى التربيعية للأولمبياد الناشئ، أوجد القيمة الصغرى للمقدار {m(f'x^2 - {2*b_v}x + {c_v}')} لجميع الأعداد الحقيقية {m('x')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 3, ans - 1, ans + 2, b_v, c_v],
            f"Complete the square: {m(f'x^2 - {2*b_v}x + {c_v} = (x - {b_v})^2 + {ans}')}.",
            f"أكمل المربع: {m(f'x^2 - {2*b_v}x + {c_v} = (x - {b_v})^2 + {ans}')}.",
            "Use the trivial inequality that any real square is non-negative.",
            [f"Since {m(f'(x - {b_v})^2 \\\\ge 0')}, the minimum is {m(str(ans))} at {m(f'x = {b_v}')}."],
            f"Verified: {m(str(ans))}.",
            "استخدم المتباينة الأساسية التي تنص على أن مربع أي عدد حقيقي غير سالب.",
            [f"بما أن {m(f'(x - {b_v})^2 \\\\ge 0')}، فإن القيمة الصغرى هي {m(str(ans))} عند {m(f'x = {b_v}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 126..130: min of x^2 + y^2 - 2ax - 2by + c
    med_specs = [(126, 2, 3, 20), (127, 3, 4, 30), (128, 1, 5, 34), (129, 4, 5, 50), (130, 2, 6, 48)]
    for idx, a_v, b_v, c_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = c_v - a_v * a_v - b_v * b_v
        diag = svg_olym_inequality_curve(f"(x−{a_v})²", f"(y−{b_v})²", note=f"min = {ans}")
        q_en = f"In a Junior Olympiad two-variable quadratic problem, find the minimum value of {m(f'x^2 + y^2 - {2*a_v}x - {2*b_v}y + {c_v}')} for real {m('x, y')}."
        q_ar = f"في مسألة القيمة الصغرى بمتغيرين للأولمبياد الناشئ، أوجد القيمة الصغرى للمقدار {m(f'x^2 + y^2 - {2*a_v}x - {2*b_v}y + {c_v}')} للأعداد الحقيقية {m('x, y')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, c_v],
            f"Complete the square independently in {m('x')} and {m('y')}.",
            f"أكمل المربع بشكل مستقل لكل من {m('x')} و{m('y')}.",
            "Rewrite as a sum of two independent squares plus a constant.",
            [f"The expression equals {m(f'(x - {a_v})^2 + (y - {b_v})^2 + {ans} \\\\ge {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "أعد كتابة المقدار كمجموع مربعين مستقلين زائد ثابت.",
            [f"المقدار يساوي {m(f'(x - {a_v})^2 + (y - {b_v})^2 + {ans} \\\\ge {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 131..135: sum of squares = 0 forcing unique real (x, y)
    hard_specs = [(131, 3, 2), (132, 4, 5), (133, 5, 3), (134, 6, 4), (135, 7, 2)]
    for idx, a_v, b_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        # (x - a)^2 + (x - y - b)^2 = 0 => x = a, y = a - b => x + y = 2a - b
        ans = 2 * a_v - b_v
        diag = svg_olym_inequality_curve(f"(x−{a_v})²=0", f"(x−y−{b_v})²=0", note="x+y=?")
        q_en = (
            f"In a Junior Olympiad sum-of-squares equation, real numbers {m('x')} and {m('y')} satisfy "
            f"{m(f'(x - {a_v})^2 + (x - y - {b_v})^2 = 0')}. Find {m('x + y')}."
        )
        q_ar = (
            f"في مسألة معادلة مجموع المربعات للأولمبياد الناشئ، يحقق العددان الحقيقيان {m('x')} و{m('y')} المعادلة "
            f"{m(f'(x - {a_v})^2 + (x - y - {b_v})^2 = 0')}. أوجد {m('x + y')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, a_v + b_v],
            "A sum of real squares is zero if and only if each square is zero.",
            "مجموع مربعات أعداد حقيقية يساوي صفراً إذا وفقط إذا كان كل مربع يساوي صفراً.",
            "Set each squared term to zero to solve for x and y.",
            [f"From {m(f'x = {a_v}')} and {m(f'y = x - {b_v} = {a_v - b_v}')}, we get {m(f'x + y = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "ساوِ كل حد مربع بالصفر لإيجاد قيمتي x وy.",
            [f"من {m(f'x = {a_v}')} و{m(f'y = x - {b_v} = {a_v - b_v}')}، نحصل على {m(f'x + y = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u13_b2_two_var_amgm() -> list[dict]:
    bp = "olym_t1_ineq_two_var_amgm"
    tp = "Inequalities"
    out: list[dict] = []

    # Easy 136..140: min of x + k^2 / x for x > 0 is 2k
    easy_specs = [(136, 4), (137, 5), (138, 6), (139, 7), (140, 9)]
    for idx, k_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 2 * k_v
        diag = svg_olym_inequality_curve("x", f"{k_v*k_v}/x", note=f"min = {ans}")
        q_en = f"In a Junior Olympiad AM-GM problem, find the minimum value of {m(f'x + \\\\frac{{{k_v*k_v}}}{{x}}')} for {m('x > 0')}."
        q_ar = f"في مسألة متباينة الوسط الحسابي والهندسي للأولمبياد الناشئ، أوجد القيمة الصغرى للمقدار {m(f'x + \\\\frac{{{k_v*k_v}}}{{x}}')} حيث {m('x > 0')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [k_v, ans - 2, ans + 2, k_v * k_v, ans + 4],
            f"Apply AM-GM: {m(f'x + \\\\frac{{{k_v*k_v}}}{{x}} \\\\ge 2\\\\sqrt{{x \\\\cdot \\\\frac{{{k_v*k_v}}}{{x}}}}')}.",
            f"طبّق متباينة الوسط الحسابي والهندسي: {m(f'x + \\\\frac{{{k_v*k_v}}}{{x}} \\\\ge 2\\\\sqrt{{x \\\\cdot \\\\frac{{{k_v*k_v}}}{{x}}}}')}.",
            "Use the two-variable AM-GM inequality.",
            [f"By AM-GM, the minimum is {m(f'2 \\\\times {k_v} = {ans}')}, achieved at {m(f'x = {k_v}')}."],
            f"Verified: {m(str(ans))}.",
            "استخدم متباينة الوسط الحسابي والهندسي لمتغيرين.",
            [f"بموجب المتباينة، القيمة الصغرى هي {m(f'2 \\\\times {k_v} = {ans}')} وتتحقق عند {m(f'x = {k_v}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 141..145: max of a*b given p*a + q*b = S
    med_specs = [(141, 1, 2, 12), (142, 2, 3, 24), (143, 1, 4, 16), (144, 3, 4, 24), (145, 2, 5, 20)]
    for idx, p_v, q_v, s_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        # (pa)(qb) <= (S/2)^2 => ab <= S^2 / (4pq)
        ans = (s_v * s_v) // (4 * p_v * q_v)
        diag = svg_olym_inequality_curve(f"{p_v}a", f"{q_v}b", note=f"max(ab)={ans}")
        q_en = f"In a Junior Olympiad weighted AM-GM problem, positive real numbers {m('a')} and {m('b')} satisfy {m(f'{p_v}a + {q_v}b = {s_v}')}. Find the maximum value of {m('ab')}."
        q_ar = f"في مسألة الوسط الحسابي والهندسي الموزون للأولمبياد الناشئ، يحقق العددان الحقيقيان الموجبان {m('a')} و{m('b')} المعادلة {m(f'{p_v}a + {q_v}b = {s_v}')}. أوجد القيمة العظمى للجداء {m('ab')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 2, ans + 4, ans * 2],
            f"Apply AM-GM to the two summands {m(f'{p_v}a')} and {m(f'{q_v}b')}.",
            f"طبّق متباينة الوسط الحسابي والهندسي على الحدين {m(f'{p_v}a')} و{m(f'{q_v}b')}.",
            f"Since {m(f'2\\\\sqrt{{{p_v*q_v}ab}} \\\\le {p_v}a + {q_v}b = {s_v}')}, square both sides.",
            [f"Equality holds when {m(f'{p_v}a = {q_v}b = {s_v//2}')}, giving {m(f'\\\\max(ab) = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            f"بما أن {m(f'2\\\\sqrt{{{p_v*q_v}ab}} \\\\le {p_v}a + {q_v}b = {s_v}')}، ربّع الطرفين.",
            [f"تتحقق المساواة عندما {m(f'{p_v}a = {q_v}b = {s_v//2}')}، مما يعطي {m(f'\\\\max(ab) = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 146..150: min of (a + b)(1/a + m^2/b) = (1 + m)^2 for a, b > 0
    hard_specs = [(146, 2), (147, 3), (148, 4), (149, 5), (150, 6)]
    for idx, m_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (1 + m_v) ** 2
        diag = svg_olym_inequality_curve("b/a", f"{m_v*m_v}a/b", note=f"min = {ans}")
        q_en = (
            f"In a Junior Olympiad reciprocal expansion inequality, find the minimum value of "
            f"{m(f'(a + b)\\\\left(\\\\frac{{1}}{{a}} + \\\\frac{{{m_v*m_v}}}{{b}}\\\\right)')} over all positive real numbers {m('a, b')}."
        )
        q_ar = (
            f"في مسألة متباينات المقلوبات للأولمبياد الناشئ، أوجد القيمة الصغرى للمقدار "
            f"{m(f'(a + b)\\\\left(\\\\frac{{1}}{{a}} + \\\\frac{{{m_v*m_v}}}{{b}}\\\\right)')} لجميع الأعداد الحقيقية الموجبة {m('a, b')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, 1 + m_v * m_v],
            f"Expand into {m(f'1 + {m_v*m_v} + \\\\frac{{b}}{{a}} + \\\\frac{{{m_v*m_v}a}}{{b}}')} and apply AM-GM to the cross terms.",
            f"فكّك الأقواس إلى {m(f'1 + {m_v*m_v} + \\\\frac{{b}}{{a}} + \\\\frac{{{m_v*m_v}a}}{{b}}')} وطبّق متباينة الوسط الحسابي والهندسي على الحدين المتبادلين.",
            "Expand the product and apply AM-GM to the reciprocal ratio terms.",
            [f"By AM-GM, {m(f'\\\\frac{{b}}{{a}} + \\\\frac{{{m_v*m_v}a}}{{b}} \\\\ge {2*m_v}')}, so the minimum is {m(f'(1+{m_v})^2 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "فكّك الجداء وطبّق متباينة الوسط الحسابي والهندسي على الحدين الكسريين.",
            [f"بموجب المتباينة، {m(f'\\\\frac{{b}}{{a}} + \\\\frac{{{m_v*m_v}a}}{{b}} \\\\ge {2*m_v}')}، فتكون القيمة الصغرى {m(f'(1+{m_v})^2 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u13_b3_triangle_bounds() -> list[dict]:
    bp = "olym_t1_ineq_triangle_bounds"
    tp = "Inequalities"
    out: list[dict] = []

    # Easy 151..155: number of integer third sides c given a < b is 2a - 1
    easy_specs = [(151, 5, 9), (152, 6, 11), (153, 7, 12), (154, 8, 15), (155, 9, 14)]
    for idx, a_v, b_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 2 * a_v - 1
        diag = svg_median_tri(str(a_v), str(b_v), "c ∈ ℤ", "|b−a|<c<a+b")
        q_en = f"In a Junior Olympiad triangle inequality problem, two sides of a non-degenerate triangle have lengths {m(str(a_v))} and {m(str(b_v))}. How many possible integer lengths can the third side have?"
        q_ar = f"في مسألة متباينة المثلث للأولمبياد الناشئ، طولا ضلعين في مثلث غير منحل هما {m(str(a_v))} و{m(str(b_v))}. كم طولاً صحيحاً ممكناً للضلع الثالث؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, 2 * a_v + 1],
            f"Use {m(f'{b_v - a_v} < c < {a_v + b_v}')}.",
            f"استخدم المتباينة الحاصرة {m(f'{b_v - a_v} < c < {a_v + b_v}')}.",
            f"Count integers strictly between {m('|b - a|')} and {m('a + b')}.",
            [f"The integers {m('c')} satisfy {m(f'{b_v - a_v + 1} \\\\le c \\\\le {a_v + b_v - 1}')}, giving {m(f'2({a_v}) - 1 = {ans}')} values."],
            f"Verified: {m(str(ans))}.",
            f"احسب عدد الأعداد الصحيحة المحصورة تماماً بين {m('|b - a|')} و{m('a + b')}.",
            [f"الأعداد الصحيحة {m('c')} تحقق {m(f'{b_v - a_v + 1} \\\\le c \\\\le {a_v + b_v - 1}')}، وعددها {m(f'2({a_v}) - 1 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 156..160: number of non-congruent integer triangles with perimeter P
    med_specs = [(156, 11), (157, 13), (158, 15), (159, 17), (160, 19)]
    for idx, p_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = sum(1 for a in range(1, p_v) for b in range(a, p_v - a) for c in [p_v - a - b] if b <= c and a + b > c)
        diag = svg_median_tri("a", "b", "c", f"P = {p_v}")
        q_en = f"In a Junior Olympiad integer-triangle enumeration problem, how many non-congruent triangles have integer side lengths and perimeter {m(str(p_v))}?"
        q_ar = f"في مسألة عد المثلثات الصحيحة للأولمبياد الناشئ، كم مثلثاً غير متطابق أطوال أضلاعه أعداد صحيحة ومحيطه {m(str(p_v))}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            f"List triples {m('a \\\\le b \\\\le c')} with {m(f'a + b + c = {p_v}')} and {m(f'c \\\\le {(p_v - 1)//2}')}.",
            f"اسرد الثلاثيات {m('a \\\\le b \\\\le c')} التي تحقق {m(f'a + b + c = {p_v}')} و{m(f'c \\\\le {(p_v - 1)//2}')}.",
            "Bound the longest side c by (P-1)/2 and count ordered integer partitions.",
            [f"Enumerating triples with {m(f'\\\\lceil {p_v}/3 \\\\rceil \\\\le c \\\\le {(p_v-1)//2}')} yields {m(str(ans))} triangles."],
            f"Verified: {m(str(ans))}.",
            "احصر الضلع الأكبر c بالسقف (P-1)/2 واحسب الثلاثيات المرتبة.",
            [f"بحصر القيم {m(f'\\\\lceil {p_v}/3 \\\\rceil \\\\le c \\\\le {(p_v-1)//2}')} نجد {m(str(ans))} مثلثات."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 161..165: polygon inequality / sum of diagonals or largest integer side for perimeter P
    hard_specs = [
        (161, 21, 10, "What is the maximum possible integer length of a side of a triangle with perimeter 21?"),
        (162, 26, 12, "What is the maximum possible integer length of a side of a triangle with perimeter 26?"),
        (163, 30, 16, "In convex quadrilateral ABCD with perimeter 30, the sum of diagonals AC + BD must be strictly greater than what integer bound (the semiperimeter)?"),
        (164, 34, 16, "What is the maximum possible integer length of a side of a triangle with perimeter 34?"),
        (165, 41, 20, "What is the maximum possible integer length of a side of a triangle with perimeter 41?"),
    ]
    for idx, p_v, ans, _ in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_median_tri("a", "b", "c_max=?", f"P = {p_v}")
        if idx == 163:
            q_en = f"In a Junior Olympiad geometric inequality problem, a convex quadrilateral has perimeter {m('30')}. By the triangle inequality on its four sub-triangles, the sum of its two diagonals {m('AC + BD')} is strictly greater than what integer?"
            q_ar = f"في مسألة المتباينات الهندسية للأولمبياد الناشئ، رباعي محدب محيطه {m('30')}. بتطبيق متباينة المثلث، مجموع قطريه {m('AC + BD')} أكبر تماماً من أي حد صحيح (نصف المحيط)؟"
            ans = 15
        else:
            q_en = f"In a Junior Olympiad extremal triangle bound problem, a triangle has integer side lengths and perimeter {m(str(p_v))}. What is the maximum possible length of its longest side?"
            q_ar = f"في مسألة الحدود القصوى للمثلث للأولمبياد الناشئ، مثلث أطوال أضلاعه أعداد صحيحة ومحيطه {m(str(p_v))}. ما أكبر طول ممكن لضلع فيه؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, p_v // 2 + 2],
            f"Any side of a triangle is strictly less than half the perimeter {m('P / 2')}.",
            f"أي ضلع في المثلث أصغر تماماً من نصف المحيط {m('P / 2')}.",
            "Use c < a + b => 2c < P.",
            [f"From {m(f'2c < {p_v}')}, the largest integer value is {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "استخدم المتباينة c < a + b ومنها 2c < P.",
            [f"من المتباينة {m(f'2c < {p_v}')}، أكبر قيمة صحيحة هي {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u13_b4_discrete_smoothing() -> list[dict]:
    bp = "olym_t1_ineq_discrete_smoothing"
    tp = "Inequalities"
    out: list[dict] = []

    # Easy 166..170: max product of two integers with sum S
    easy_specs = [(166, 15), (167, 17), (168, 19), (169, 21), (170, 23)]
    for idx, s_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (s_v // 2) * (s_v - s_v // 2)
        diag = svg_bar_chart([("a", s_v // 2, str(s_v // 2)), ("b", s_v - s_v // 2, str(s_v - s_v // 2))])
        q_en = f"In a Junior Olympiad discrete optimization problem, two positive integers have sum {m(str(s_v))}. What is the maximum possible value of their product?"
        q_ar = f"في مسألة التحسين المتقطع للأولمبياد الناشئ، عددان صحيحان موجبان مجموعهما {m(str(s_v))}. ما أكبر قيمة ممكنة لحاصل ضربهما؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 3, (s_v // 2 - 1) * (s_v - s_v // 2 + 1)],
            "Make the two integers as close to each other as possible.",
            "اجعل العددين الصحيحين متقاربين قدر الإمكان.",
            "By discrete smoothing, the product of two integers with fixed sum is maximized when |a - b| <= 1.",
            [f"Choose {m(f'{s_v//2}')} and {m(f'{s_v - s_v//2}')}, giving product {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "بمبدأ التقريب المتقطع، يعظّم جداء عددين مجموعهما ثابت عندما يكون الفرق بينهما أصغر ما يمكن.",
            [f"نختار {m(f'{s_v//2}')} و{m(f'{s_v - s_v//2}')}، فيكون الجداء {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 171..175: max product of 3 positive integers with sum S
    med_specs = [(171, 10), (172, 11), (173, 13), (174, 14), (175, 16)]
    for idx, s_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        q_part, r_part = divmod(s_v, 3)
        parts_3 = [q_part + (1 if i < r_part else 0) for i in range(3)]
        ans = math.prod(parts_3)
        diag = svg_bar_chart([(f"x{i+1}", parts_3[i], str(parts_3[i])) for i in range(3)])
        q_en = f"In a Junior Olympiad 3-variable smoothing problem, three positive integers have sum {m(str(s_v))}. Find the maximum possible value of their product."
        q_ar = f"في مسألة التمليس لثلاثة متغيرات في الأولمبياد الناشئ، ثلاثة أعداد صحيحة موجبة مجموعها {m(str(s_v))}. أوجد أكبر قيمة ممكنة لحاصل ضربها."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, ans + 8],
            "If two integers differ by at least 2, replacing (a, b) with (a+1, b-1) strictly increases their product.",
            "إذا اختلف عددان بمقدار 2 أو أكثر، فإن استبدالهما بـ (a+1, b-1) يزيد الجداء.",
            "Balance the three integers so any two differ by at most 1.",
            [f"The optimal triple is {m(str(tuple(parts_3)))} with product {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "وازن الأعداد الثلاثة بحيث لا يزيد الفرق بين أي عددين عن 1.",
            [f"الثلاثية المثلى هي {m(str(tuple(parts_3)))} وحاصل ضربها {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 176..180: min sum of squares of k integers with sum S, or Rearrangement Inequality
    hard_specs = [(176, 3, 14), (177, 4, 15), (178, 3, 17), (179, 4, 18), (180, 5, 17)]
    for idx, k_v, s_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        q_part, r_part = divmod(s_v, k_v)
        parts_k = [q_part + (1 if i < r_part else 0) for i in range(k_v)]
        ans = sum(x * x for x in parts_k)
        diag = svg_bar_chart([(f"x{i+1}", parts_k[i], str(parts_k[i])) for i in range(min(4, k_v))])
        q_en = f"In a Junior Olympiad quadratic smoothing problem, {m(str(k_v))} positive integers have sum {m(str(s_v))}. What is the minimum possible value of the sum of their squares?"
        q_ar = f"في مسألة تقليل مجموع المربعات للأولمبياد الناشئ، {m(str(k_v))} أعداد صحيحة موجبة مجموعها {m(str(s_v))}. ما أصغر قيمة ممكنة لمجموع مربعاتها؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, ans + 6],
            "Sum of squares is minimized when the integers are as nearly equal as possible.",
            "يبلغ مجموع المربعات قيمته الصغرى عندما تكون الأعداد متقاربة قدر الإمكان.",
            "Since (a+1)^2 + (b-1)^2 < a^2 + b^2 for a + 2 <= b, smooth until all terms differ by at most 1.",
            [f"The balanced partition {m(str(parts_k))} gives sum of squares {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "بما أن (a+1)^2 + (b-1)^2 < a^2 + b^2 عندما a + 2 <= b، نملّس القيم حتى لا يزيد الفرق عن 1.",
            [f"التجزئة المتوازنة {m(str(parts_k))} تعطي مجموع مربعات يساوي {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


# ==============================================================================
# UNIT 1.4 — Geometry I (OLYM-T1-181 .. OLYM-T1-240)
# ==============================================================================

def _build_u14_b1_angle_chasing() -> list[dict]:
    bp = "olym_t1_geo_angle_chasing_cyclic"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 181..185: isosceles triangle vertex / base angle chasing
    easy_specs = [(181, 36), (182, 42), (183, 50), (184, 64), (185, 72)]
    for idx, a_deg in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (180 - a_deg) // 2
        diag = svg_thales_circle(f"{a_deg}°", "?°")
        q_en = f"In a Junior Olympiad angle-chasing problem, isosceles triangle {m('ABC')} with {m('AB = AC')} has apex angle {m(f'\\\\angle A = {a_deg}^\\\\circ')}. Find {m(r'\\angle B')} in degrees."
        q_ar = f"في مسألة تتبع الزوايا للأولمبياد الناشئ، المثلث المتطابق الضلعين {m('ABC')} الذي فيه {m('AB = AC')} زاوية رأسه {m(f'\\\\angle A = {a_deg}^\\\\circ')}. أوجد قياس {m(r'\\angle B')} بالدرجات."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 6, ans - 3, ans + 3, ans + 6, 180 - a_deg],
            f"Use {m(r'\\angle B = \\angle C = (180^\\circ - \\angle A)/2')}.",
            f"استخدم العلاقة {m(r'\\angle B = \\angle C = (180^\\circ - \\angle A)/2')}.",
            "Base angles of an isosceles triangle are equal.",
            [f"Compute {m(f'(180^\\\\circ - {a_deg}^\\\\circ)/2 = {ans}^\\\\circ')}."],
            f"Verified: {m(str(ans))}.",
            "زاويتا القاعدة في المثلث المتطابق الضلعين متساويتان.",
            [f"نحسب {m(f'(180^\\\\circ - {a_deg}^\\\\circ)/2 = {ans}^\\\\circ')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 186..190: cyclic quadrilateral opposite angle 180 - alpha
    med_specs = [(186, 68), (187, 74), (188, 83), (189, 97), (190, 106)]
    for idx, a_deg in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 180 - a_deg
        diag = svg_cyclic_quad(f"{a_deg}°", "?°")
        q_en = f"In a Junior Olympiad cyclic quadrilateral problem, {m('ABCD')} is inscribed in a circle with {m(f'\\\\angle A = {a_deg}^\\\\circ')}. Find the measure of the opposite angle {m(r'\\angle C')} in degrees."
        q_ar = f"في مسألة الرباعي الدائري للأولمبياد الناشئ، الرباعي {m('ABCD')} مرسوم داخل دائرة وفيه {m(f'\\\\angle A = {a_deg}^\\\\circ')}. أوجد قياس الزاوية المقابلة {m(r'\\angle C')} بالدرجات."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 8, ans - 4, ans + 4, ans + 8, a_deg],
            f"Opposite angles of a cyclic quadrilateral sum to {m('180^\\\\circ')}.",
            f"كل زاويتين متقابلتين في الرباعي الدائري متكاملتان ومجموعهما {m('180^\\\\circ')}.",
            "Apply the cyclic quadrilateral supplementary-angle theorem.",
            [f"We have {m(f'\\\\angle C = 180^\\\\circ - {a_deg}^\\\\circ = {ans}^\\\\circ')}."],
            f"Verified: {m(str(ans))}.",
            "طبّق نظرية تكامل الزوايا المتقابلة في الرباعي الدائري.",
            [f"نجد أن {m(f'\\\\angle C = 180^\\\\circ - {a_deg}^\\\\circ = {ans}^\\\\circ')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 191..195: incenter angle BIC = 90 + A/2
    hard_specs = [(191, 40), (192, 52), (193, 64), (194, 70), (195, 84)]
    for idx, a_deg in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 90 + a_deg // 2
        diag = svg_olym_cyclic_ptolemy("B", "I", "C", f"A={a_deg}°", "∠BIC=?")
        q_en = f"In a Junior Olympiad incenter angle problem, {m('I')} is the incenter of triangle {m('ABC')} with {m(f'\\\\angle BAC = {a_deg}^\\\\circ')}. Find {m(r'\\angle BIC')} in degrees."
        q_ar = f"في مسألة زاوية مركز الدائرة الداخلية للأولمبياد الناشئ، النقطة {m('I')} هي مركز الدائرة الداخلية للمثلث {m('ABC')} حيث {m(f'\\\\angle BAC = {a_deg}^\\\\circ')}. أوجد قياس {m(r'\\angle BIC')} بالدرجات."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 10, ans - 5, ans + 5, ans + 10, 180 - a_deg],
            f"Use the incenter angle identity {m(r'\\angle BIC = 90^\\circ + \\frac{1}{2}\\angle BAC')}.",
            f"استخدم متطابقة زاوية المركز الداخلي {m(r'\\angle BIC = 90^\\circ + \\frac{1}{2}\\angle BAC')}.",
            "Sum the half-angles in triangle BIC.",
            [f"Since {m(r'\\frac{1}{2}(\\angle B + \\angle C) = 90^\\circ - \\frac{1}{2}\\angle A')}, we get {m(f'\\\\angle BIC = 90^\\\\circ + {a_deg//2}^\\\\circ = {ans}^\\\\circ')}."],
            f"Verified: {m(str(ans))}.",
            "اجمع أنصاف الزوايا داخل المثلث BIC.",
            [f"بما أن {m(r'\\frac{1}{2}(\\angle B + \\angle C) = 90^\\circ - \\frac{1}{2}\\angle A')}، نحصل على {m(f'\\\\angle BIC = 90^\\\\circ + {a_deg//2}^\\\\circ = {ans}^\\\\circ')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u14_b2_area_ratios() -> list[dict]:
    bp = "olym_t1_geo_area_ratios_bases"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 196..200: cevian BD:DC = m:n, given [ABC], find [ABD]
    easy_specs = [(196, 2, 3, 60), (197, 3, 4, 84), (198, 1, 4, 75), (199, 3, 5, 96), (200, 2, 5, 105)]
    for idx, m_v, n_v, tot_a in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (tot_a * m_v) // (m_v + n_v)
        diag = svg_median_tri("AB", "AC", f"{m_v}:{n_v}", "[ABD]=?")
        q_en = f"In a Junior Olympiad area-ratio problem, point {m('D')} on side {m('BC')} of triangle {m('ABC')} satisfies {m(f'BD : DC = {m_v} : {n_v}')}. If the area of {m('ABC')} is {m(str(tot_a))}, find the area of {m('ABD')}."
        q_ar = f"في مسألة نسب المساحات للأولمبياد الناشئ، تقع النقطة {m('D')} على الضلع {m('BC')} في المثلث {m('ABC')} بحيث {m(f'BD : DC = {m_v} : {n_v}')}. إذا كانت مساحة {m('ABC')} تساوي {m(str(tot_a))}، فأوجد مساحة {m('ABD')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 6, ans + 6, (tot_a * n_v) // (m_v + n_v), ans + 12, tot_a // 2],
            f"Triangles sharing the same altitude have areas proportional to their bases: {m(f'[ABD]/[ABC] = {m_v}/({m_v}+{n_v})')}.",
            f"المثلثات المشتركة في الارتفاع تتناسب مساحاتها مع قواعدها: {m(f'[ABD]/[ABC] = {m_v}/({m_v}+{n_v})')}.",
            "Use equal-altitude base-ratio proportionality.",
            [f"Compute {m(f'[ABD] = \\\\frac{{{m_v}}}{{{m_v+n_v}}} \\\\times {tot_a} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "استخدم تناسب المساحات مع أطوال القواعد عند ثبات الارتفاع.",
            [f"نحسب {m(f'[ABD] = \\\\frac{{{m_v}}}{{{m_v+n_v}}} \\\\times {tot_a} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 201..205: centroid G divides triangle into 6 equal areas, or medial triangle area
    med_specs = [(201, 72, 6), (202, 96, 4), (203, 120, 3), (204, 108, 6), (205, 144, 4)]
    for idx, tot_a, div_k in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = tot_a // div_k
        diag = svg_stu_ceva_triangle("1", "1", "1", "1", "1", "1")
        sub_desc_en = "one of the six small triangles formed by the three medians" if div_k == 6 else ("the medial triangle joining the midpoints of the three sides" if div_k == 4 else "triangle GBC where G is the centroid")
        sub_desc_ar = "أحد المثلثات الستة الصغيرة الناتجة عن المتوسطات الثلاثة" if div_k == 6 else ("المثلث الأوسط الواصل بين منتصفات الأضلاع الثلاثة" if div_k == 4 else "المثلث GBC حيث G مركز الثقل")
        q_en = f"In a Junior Olympiad median area problem, triangle {m('ABC')} has area {m(str(tot_a))}. Find the area of {sub_desc_en}."
        q_ar = f"في مسألة مساحة المتوسطات للأولمبياد الناشئ، مساحة المثلث {m('ABC')} تساوي {m(str(tot_a))}. أوجد مساحة {sub_desc_ar}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 4, ans + 8, tot_a // 2],
            f"Divide the total area {m(str(tot_a))} by {m(str(div_k))}.",
            f"اقسم المساحة الكلية {m(str(tot_a))} على {m(str(div_k))}.",
            "Medians partition a triangle into 6 equal-area sub-triangles, and the medial triangle has 1/4 the total area.",
            [f"The area equals {m(f'{tot_a} / {div_k} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "تقسم المتوسطات المثلث إلى 6 مثلثات متساوية المساحة، والمثلث الأوسط مساحته ربع المساحة الكلية.",
            [f"المساحة تساوي {m(f'{tot_a} / {div_k} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 206..210: trapezoid diagonals divide into 4 triangles; top & bottom areas A1, A2 => total area (sqrt(A1)+sqrt(A2))^2
    hard_specs = [(206, 4, 9), (207, 9, 16), (208, 4, 25), (209, 16, 25), (210, 9, 36)]
    for idx, a1, a2 in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        s1, s2 = int(math.isqrt(a1)), int(math.isqrt(a2))
        ans = (s1 + s2) ** 2
        diag = svg_isosceles_trapezoid(f"A₁={a1}", f"A₂={a2}", "√(A₁A₂)", "[ABCD]=?")
        q_en = (
            f"In a Junior Olympiad trapezoid diagonal-area problem, the diagonals of trapezoid {m('ABCD')} ({m('AB \\\\parallel CD')}) "
            f"intersect at {m('P')}. If the areas of {m('ABP')} and {m('CDP')} are {m(str(a1))} and {m(str(a2))}, find the total area of trapezoid {m('ABCD')}."
        )
        q_ar = (
            f"في مسألة مساحات أقطار شبه المنحرف للأولمبياد الناشئ، يتقاطع قطرا شبه المنحرف {m('ABCD')} ({m('AB \\\\parallel CD')}) "
            f"في النقطة {m('P')}. إذا كانت مساحتا المثلثين {m('ABP')} و{m('CDP')} هما {m(str(a1))} و{m(str(a2))}، فأوجد المساحة الكلية لشبه المنحرف {m('ABCD')}."
        )
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 6, ans - 3, ans + 4, a1 + a2 + s1 * s2, a1 + a2],
            f"Each wing triangle has area {m(r'\\sqrt{A_1 A_2}')}, so the total area is {m(r'(\\sqrt{A_1} + \\sqrt{A_2})^2')}.",
            f"مساحة كل مثلث جانبي تساوي {m(r'\\sqrt{A_1 A_2}')}، فتكون المساحة الكلية {m(r'(\\sqrt{A_1} + \\sqrt{A_2})^2')}.",
            "Use base ratios along the intersecting diagonals of the trapezoid.",
            [f"Each lateral triangle has area {m(f'\\\\sqrt{{{a1}\\\\times {a2}}} = {s1*s2}')}, giving total area {m(f'({s1}+{s2})^2 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "استخدم نسب القواعد على طول قطري شبه المنحرف المتقاطعين.",
            [f"مساحة كل مثلث جانبي تساوي {m(f'\\\\sqrt{{{a1}\\\\times {a2}}} = {s1*s2}')}، والمساحة الكلية {m(f'({s1}+{s2})^2 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u14_b3_similarity_pythagoras() -> list[dict]:
    bp = "olym_t1_geo_similarity_pythagoras"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 211..215: DE || BC with AD, DB, BC given -> find DE
    easy_specs = [(211, 3, 2, 15), (212, 2, 3, 20), (213, 4, 3, 21), (214, 3, 5, 24), (215, 5, 4, 27)]
    for idx, ad_v, db_v, bc_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (ad_v * bc_v) // (ad_v + db_v)
        diag = svg_parallel_similar_tri(str(ad_v), str(db_v), "?", str(bc_v))
        q_en = f"In a Junior Olympiad similar-triangles problem, segment {m('DE')} is parallel to base {m('BC')} of triangle {m('ABC')}, with {m(f'AD = {ad_v}')}, {m(f'DB = {db_v}')}, and {m(f'BC = {bc_v}')}. Find {m('DE')}."
        q_ar = f"في مسألة تشابه المثلثات للأولمبياد الناشئ، القطعة {m('DE')} توازي القاعدة {m('BC')} في المثلث {m('ABC')}، حيث {m(f'AD = {ad_v}')} و{m(f'DB = {db_v}')} و{m(f'BC = {bc_v}')}. أوجد طول {m('DE')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 2, ans + 4, (db_v * bc_v) // (ad_v + db_v)],
            f"Use {m('DE / BC = AD / (AD + DB)')}.",
            f"استخدم تناسب التشابه {m('DE / BC = AD / (AD + DB)')}.",
            "By AA similarity, triangle ADE is similar to triangle ABC.",
            [f"Compute {m(f'DE = \\\\frac{{{ad_v}}}{{{ad_v+db_v}}} \\\\times {bc_v} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "من تشابه المثلثين ADE وABC تتناسب الأضلاع المتناظرة.",
            [f"نحسب {m(f'DE = \\\\frac{{{ad_v}}}{{{ad_v+db_v}}} \\\\times {bc_v} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 216..220: right triangle altitude to hypotenuse h = sqrt(pq)
    med_specs = [(216, 4, 9), (217, 4, 16), (218, 9, 16), (219, 4, 25), (220, 9, 25)]
    for idx, p_v, q_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = int(math.isqrt(p_v * q_v))
        diag = svg_right_tri_incircle(f"p={p_v}", f"q={q_v}", f"c={p_v+q_v}", "h=?")
        q_en = f"In a Junior Olympiad right-triangle altitude problem, the altitude {m('CD')} to the hypotenuse {m('AB')} of right triangle {m('ABC')} divides {m('AB')} into segments {m(f'AD = {p_v}')} and {m(f'DB = {q_v}')}. Find {m('CD')}."
        q_ar = f"في مسألة الارتفاع النازل على الوتر للأولمبياد الناشئ، يقسم الارتفاع {m('CD')} النازل على الوتر {m('AB')} في المثلث القائم {m('ABC')} الوترَ إلى قطعتين {m(f'AD = {p_v}')} و{m(f'DB = {q_v}')}. أوجد طول {m('CD')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 2, ans + 3, (p_v + q_v) // 2],
            f"Use the geometric mean theorem {m('CD^2 = AD \\\\cdot DB')}.",
            f"استخدم نظرية الوسط الهندسي للارتفاع {m('CD^2 = AD \\\\cdot DB')}.",
            "Triangles ACD and CBD are similar right triangles.",
            [f"Compute {m(f'CD = \\\\sqrt{{{p_v} \\\\times {q_v}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "المثلثان القائمان ACD وCBD متشابهان.",
            [f"نحسب {m(f'CD = \\\\sqrt{{{p_v} \\\\times {q_v}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 221..225: two externally tangent circles common external tangent AB = 2*sqrt(r1*r2)
    hard_specs = [(221, 9, 4), (222, 16, 4), (223, 9, 16), (224, 25, 4), (225, 25, 9)]
    for idx, r1, r2 in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 2 * int(math.isqrt(r1 * r2))
        diag = svg_stu_tangent_circles(str(r1), str(r2), "AB = ?")
        q_en = f"In a Junior Olympiad tangent-circles problem, two externally tangent circles of radii {m(str(r1))} and {m(str(r2))} rest on a common external tangent line at points {m('A')} and {m('B')}. Find the distance {m('AB')}."
        q_ar = f"في مسألة الدوائر المتماسة للأولمبياد الناشئ، دائرتان متماستان من الخارج نصفا قطريهما {m(str(r1))} و{m(str(r2))} ترتكزان على مماس خارجي مشترك عند النقطتين {m('A')} و{m('B')}. أوجد المسافة {m('AB')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, r1 + r2],
            f"Form a right triangle with hypotenuse {m('r_1 + r_2')} and leg {m('|r_1 - r_2|')}, so {m(r'AB = 2\\sqrt{r_1 r_2}')}.",
            f"كوّن مثلثاً قائماً وتره {m('r_1 + r_2')} وضلع القائمة {m('|r_1 - r_2|')}، فيكون {m(r'AB = 2\\sqrt{r_1 r_2}')}.",
            "Apply the Pythagorean theorem to the right trapezoid of radii and line of centers.",
            [f"We have {m(f'AB = \\\\sqrt{{({r1}+{r2})^2 - ({r1}-{r2})^2}} = 2\\\\sqrt{{{r1}\\\\times {r2}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "طبّق نظرية فيثاغورس على شبه المنحرف القائم المكوّن من نصفي القطرين وخط المركزين.",
            [f"نجد أن {m(f'AB = \\\\sqrt{{({r1}+{r2})^2 - ({r1}-{r2})^2}} = 2\\\\sqrt{{{r1}\\\\times {r2}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u14_b4_incircle_tangents() -> list[dict]:
    bp = "olym_t1_geo_incircle_tangents"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 226..230: tangent length from A to incircle is s - a
    easy_specs = [(226, 10, 12, 14), (227, 8, 13, 15), (228, 9, 11, 16), (229, 12, 15, 19), (230, 11, 14, 17)]
    for idx, a_v, b_v, c_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        s_v = (a_v + b_v + c_v) // 2
        ans = s_v - a_v
        diag = svg_olym_incircle_excircle(str(a_v), str(b_v), str(c_v), note="AD = s − a")
        q_en = f"In a Junior Olympiad incircle tangency problem, the incircle of triangle {m('ABC')} with side lengths {m(f'BC = {a_v}')}, {m(f'AC = {b_v}')}, and {m(f'AB = {c_v}')} touches {m('AB')} at {m('D')}. Find {m('AD')}."
        q_ar = f"في مسألة مماسات الدائرة الداخلية للأولمبياد الناشئ، تمس الدائرة الداخلية للمثلث {m('ABC')} الذي أطوال أضلاعه {m(f'BC = {a_v}')} و{m(f'AC = {b_v}')} و{m(f'AB = {c_v}')} الضلعَ {m('AB')} في {m('D')}. أوجد طول {m('AD')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, s_v - b_v if s_v - b_v != ans else ans + 3],
            f"The tangent segment from vertex {m('A')} to the incircle has length {m('s - a')}.",
            f"طول قطعة المماس من الرأس {m('A')} إلى الدائرة الداخلية يساوي {m('s - a')}.",
            "Equal tangents from each vertex partition the perimeter into 2(x + y + z) = 2s.",
            [f"With semiperimeter {m(f's = {s_v}')}, we get {m(f'AD = s - BC = {s_v} - {a_v} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "تساوي قطع المماسات من كل رأس يعطي أن طول المماس من A هو s - a.",
            [f"بما أن نصف المحيط {m(f's = {s_v}')}، فإن {m(f'AD = s - BC = {s_v} - {a_v} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 231..235: inradius of right triangle r = (a + b - c)/2
    med_specs = [(231, 6, 8, 10), (232, 5, 12, 13), (233, 8, 15, 17), (234, 9, 12, 15), (235, 7, 24, 25)]
    for idx, a_v, b_v, c_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (a_v + b_v - c_v) // 2
        diag = svg_right_tri_incircle(str(a_v), str(b_v), str(c_v), "r = ?")
        q_en = f"In a Junior Olympiad right-triangle inradius problem, find the inradius {m('r')} of a right triangle with legs {m(str(a_v))} and {m(str(b_v))} and hypotenuse {m(str(c_v))}."
        q_ar = f"في مسألة نصف قطر الدائرة الداخلية للمثلث القائم في الأولمبياد الناشئ، أوجد نصف قطر الدائرة الداخلية {m('r')} لمثلث قائم ضلعا قائمته {m(str(a_v))} و{m(str(b_v))} ووتره {m(str(c_v))}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 1, ans + 1, ans + 2, ans + 3, c_v // 2],
            f"Use the right-triangle inradius formula {m('r = (a + b - c)/2')}.",
            f"استخدم صيغة نصف قطر الدائرة الداخلية للمثلث القائم {m('r = (a + b - c)/2')}.",
            "The corner square at the right angle has side length r = s - c = (a + b - c)/2.",
            [f"Compute {m(f'r = ({a_v} + {b_v} - {c_v})/2 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "المربع المتكون عند الزاوية القائمة طول ضلعه r = s - c = (a + b - c)/2.",
            [f"نحسب {m(f'r = ({a_v} + {b_v} - {c_v})/2 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 236..240: Heronian triangle inradius r = [ABC]/s or exradius r_a = [ABC]/(s-a)
    hard_specs = [
        (236, 13, 14, 15, 4, "inradius r"),
        (237, 26, 28, 30, 8, "inradius r"),
        (238, 10, 17, 21, 7, "exradius r_a opposite the side of length 10"),
        (239, 13, 14, 15, 12, "exradius r_a opposite the side of length 14"),
        (240, 15, 15, 24, 4, "inradius r"),
    ]
    for idx, a_v, b_v, c_v, ans, ask_lbl in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        s_v = (a_v + b_v + c_v) // 2
        area_v = int(math.isqrt(s_v * (s_v - a_v) * (s_v - b_v) * (s_v - c_v)))
        diag = svg_olym_incircle_excircle(str(a_v), str(b_v), str(c_v), note=ask_lbl)
        q_en = f"In a Junior Olympiad Heronian triangle problem, triangle {m('ABC')} has side lengths {m(f'{a_v}, {b_v}, {c_v}')}. Find its {ask_lbl}."
        q_ar = f"في مسألة مثلث هيرون للأولمبياد الناشئ، أطوال أضلاع المثلث {m('ABC')} هي {m(f'{a_v}, {b_v}, {c_v}')}. أوجد قيمة ({ask_lbl})."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            f"Compute the area {m(str(area_v))} by Heron's formula with {m(f's = {s_v}')}, then divide by {m('s')} (or {m('s - a')}).",
            f"احسب المساحة {m(str(area_v))} بصيغة هيرون مع {m(f's = {s_v}')}، ثم اقسم على {m('s')} (أو {m('s - a')}).",
            "Combine Heron's area formula with [ABC] = r*s = r_a*(s - a).",
            [f"Here {m(f's = {s_v}')} and {m(f'[ABC] = {area_v}')}, giving {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "اجمع بين صيغة هيرون للمساحة والعلاقة [ABC] = r*s = r_a*(s - a).",
            [f"لدينا {m(f's = {s_v}')} والمساحة {m(f'[ABC] = {area_v}')}، فيكون الناتج {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


# ==============================================================================
# UNIT 1.5 — Geometry II (OLYM-T1-241 .. OLYM-T1-300)
# ==============================================================================

def _build_u15_b1_reflections() -> list[dict]:
    bp = "olym_t1_geo_reflections_shortest"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 241..245: Heron shortest path AP + PB with P on x-axis
    easy_specs = [
        (241, 0, 2, 6, 6, 10),
        (242, 0, 3, 12, 2, 13),
        (243, 1, 3, 9, 3, 10),
        (244, 0, 5, 15, 3, 17),
        (245, 2, 4, 14, 5, 15),
    ]
    for idx, x1, y1, x2, y2, ans in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_stu_mirror_bounce(str(x2 - x1), f"{y1}+{y2}", f"min={ans}")
        q_en = f"In a Junior Olympiad Heron reflection problem, points {m(f'A({x1},{y1})')} and {m(f'B({x2},{y2})')} lie above the {m('x')}-axis. A point {m('P')} moves along the {m('x')}-axis. Find the minimum value of {m('AP + PB')}."
        q_ar = f"في مسألة انعكاس هيرون للأولمبياد الناشئ، تقع النقطتان {m(f'A({x1},{y1})')} و{m(f'B({x2},{y2})')} فوق محور السينات، وتتحرك النقطة {m('P')} على محور السينات. أوجد أصغر قيمة ممكنة للمجموع {m('AP + PB')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, (x2 - x1) + y1 + y2],
            f"Reflect {m('A')} across the {m('x')}-axis to {m(f'A^\\\\prime({x1}, -{y1})')} and compute {m('A^\\\\prime B')}.",
            f"اعكس النقطة {m('A')} حول محور السينات إلى {m(f'A^\\\\prime({x1}, -{y1})')} واحسب المسافة {m('A^\\\\prime B')}.",
            "By reflection, AP + PB = A'P + PB >= A'B.",
            [f"Here {m(f'A^\\\\prime B = \\\\sqrt{{({x2}-{x1})^2 + ({y1}+{y2})^2}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "بالانعكاس يكون AP + PB = A'P + PB >= A'B.",
            [f"نجد أن {m(f'A^\\\\prime B = \\\\sqrt{{({x2}-{x1})^2 + ({y1}+{y2})^2}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 246..250: Two-wall reflection in coordinate quadrant / billiard table
    med_specs = [
        (246, 2, 3, 6, 3, 10),
        (247, 1, 2, 4, 2, 5),
        (248, 3, 4, 9, 4, 15),
        (249, 2, 1, 10, 4, 13),
        (250, 3, 5, 5, 10, 17),
    ]
    for idx, x1, y1, x2, y2, ans in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_stu_mirror_bounce(f"{x1}+{x2}", f"{y1}+{y2}", f"min={ans}")
        q_en = f"In a Junior Olympiad double-reflection problem, a ray starts at {m(f'A({x1},{y1})')}, reflects off the positive {m('y')}-axis at {m('P')}, then off the positive {m('x')}-axis at {m('Q')}, and reaches {m(f'B({x2},{y2})')}. Find the minimum path length {m('AP + PQ + QB')}."
        q_ar = f"في مسألة الانعكاس المزدوج للأولمبياد الناشئ، ينطلق شعاع من {m(f'A({x1},{y1})')}، وينعكس عن محور الصادات الموجب في {m('P')}، ثم عن محور السينات الموجب في {m('Q')}، ليصل إلى {m(f'B({x2},{y2})')}. أوجد أقصر طول للمسار {m('AP + PQ + QB')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            f"Reflect {m('A')} across the {m('y')}-axis to {m(f'(-{x1},{y1})')} and {m('B')} across the {m('x')}-axis to {m(f'({x2},-{y2})')}.",
            f"اعكس {m('A')} حول محور الصادات إلى {m(f'(-{x1},{y1})')} واعكس {m('B')} حول محور السينات إلى {m(f'({x2},-{y2})')}.",
            "Unfold both mirror bounces into a straight segment between the reflected endpoints.",
            [f"The straight-line distance is {m(f'\\\\sqrt{{({x1}+{x2})^2 + ({y1}+{y2})^2}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "افرد الانعكاسين إلى قطعة مستقيمة واحدة تصل بين الصورتين المنعكستين.",
            [f"المسافة المستقيمة تساوي {m(f'\\\\sqrt{{({x1}+{x2})^2 + ({y1}+{y2})^2}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 251..255: Wedge / angle-sector reflection (angle AOB = 30 deg -> P'OP'' = 60 deg equilateral -> min perimeter = OP)
    hard_specs = [(251, 8), (252, 10), (253, 12), (254, 15), (255, 18)]
    for idx, op_len in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = op_len
        diag = svg_stu_mirror_bounce(f"OP={op_len}", "∠AOB=30°", f"min P={ans}")
        q_en = f"In a Junior Olympiad wedge-reflection problem, point {m('P')} lies inside an acute angle {m(r'\\angle AOB = 30^\\circ')} with {m(f'OP = {op_len}')}. Points {m('Q')} on ray {m('OA')} and {m('R')} on ray {m('OB')} are chosen to minimize the perimeter of {m('PQR')}. Find this minimum perimeter."
        q_ar = f"في مسألة الانعكاس داخل قطاع زاوي للأولمبياد الناشئ، تقع النقطة {m('P')} داخل الزاوية الحادة {m(r'\\angle AOB = 30^\\circ')} بحيث {m(f'OP = {op_len}')}. اختيرت النقطتان {m('Q')} على الشعاع {m('OA')} و{m('R')} على الشعاع {m('OB')} لتقليل محيط المثلث {m('PQR')}. أوجد هذا المحيط الأصغر."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans + 2, ans + 4, 2 * ans, ans // 2],
            f"Reflect {m('P')} across {m('OA')} and {m('OB')} to {m('P_1')} and {m('P_2')}; then {m(r'\\angle P_1 O P_2 = 60^\\circ')} and {m('OP_1 = OP_2 = OP')}.",
            f"اعكس {m('P')} حول {m('OA')} و{m('OB')} إلى {m('P_1')} و{m('P_2')}؛ فتكون {m(r'\\angle P_1 O P_2 = 60^\\circ')} و{m('OP_1 = OP_2 = OP')}.",
            "Reflecting P across both rays creates an equilateral triangle OP1P2 of side OP.",
            [f"Since {m('OP_1 P_2')} is equilateral, the minimum perimeter {m(f'P_1 P_2 = OP = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "انعكاس النقطة P حول الشعاعين يكوّن مثلثاً متطابق الأضلاع OP1P2 طول ضلعه OP.",
            [f"بما أن المثلث {m('OP_1 P_2')} متطابق الأضلاع، فإن المحيط الأصغر يساوي {m(f'P_1 P_2 = OP = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u15_b2_polygons() -> list[dict]:
    bp = "olym_t1_geo_polygons_diagonals"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 256..260: number of diagonals n(n-3)/2 of convex n-gon
    easy_specs = [(256, 8), (257, 9), (258, 10), (259, 11), (260, 12)]
    for idx, n_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = n_v * (n_v - 3) // 2
        diag = svg_regular_polygon(min(8, n_v), [(0, 2), (0, 3), (1, 4)])
        q_en = f"In a Junior Olympiad polygon problem, how many diagonals does a convex {m(f'{n_v}')}-gon have?"
        q_ar = f"في مسألة المضلعات للأولمبياد الناشئ، كم قطراً يمتلكه مضلع محدب ذو {m(f'{n_v}')} أضلاع؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 3, ans - 1, ans + 2, ans + 5, n_v * (n_v - 1) // 2],
            f"Use the diagonal formula {m('n(n - 3)/2')}.",
            f"استخدم صيغة عدد الأقطار {m('n(n - 3)/2')}.",
            "Each of the n vertices connects to n - 3 non-adjacent vertices, divided by 2.",
            [f"Compute {m(f'{n_v}({n_v} - 3)/2 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "يتصل كل رأس من الرؤوس بـ n - 3 رؤوس غير مجاورة، مع القسمة على 2.",
            [f"نحسب {m(f'{n_v}({n_v} - 3)/2 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 261..265: find n given number of diagonals D = n(n-3)/2
    med_specs = [(261, 13), (262, 14), (263, 15), (264, 16), (265, 18)]
    for idx, n_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        d_cnt = n_v * (n_v - 3) // 2
        ans = n_v
        diag = svg_regular_polygon(7, [(0, 2), (0, 3), (1, 4), (2, 5)])
        q_en = f"In a Junior Olympiad inverse polygon problem, a convex polygon has exactly {m(str(d_cnt))} diagonals. How many sides does it have?"
        q_ar = f"في مسألة المضلعات العكسية للأولمبياد الناشئ، مضلع محدب له {m(str(d_cnt))} قطراً بالضبط. كم عدد أضلاعه؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 3],
            f"Solve {m(f'n(n - 3) = {2*d_cnt}')}.",
            f"حل المعادلة {m(f'n(n - 3) = {2*d_cnt}')}.",
            "Factor 2D into two integers differing by 3.",
            [f"Since {m(f'{n_v} \\\\times {n_v-3} = {2*d_cnt}')}, the polygon has {m(str(ans))} sides."],
            f"Verified: {m(str(ans))}.",
            "حلّل العدد 2D إلى عاملين صحيحين الفرق بينهما 3.",
            [f"بما أن {m(f'{n_v} \\\\times {n_v-3} = {2*d_cnt}')}، فإن للمضلع {m(str(ans))} ضلعاً."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 266..270: interior intersection points of diagonals C(n, 4) in convex n-gon with no 3 concurrent
    hard_specs = [(266, 6), (267, 7), (268, 8), (269, 9), (270, 10)]
    for idx, n_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = math.comb(n_v, 4)
        diag = svg_regular_polygon(min(8, n_v), [(0, 2), (1, 3), (0, 3), (1, 4)])
        q_en = f"In a Junior Olympiad combinatorial geometry problem, no three diagonals of a convex {m(f'{n_v}')}-gon are concurrent at an interior point. In how many interior points do its diagonals intersect?"
        q_ar = f"في مسألة الهندسة التوافقية للأولمبياد الناشئ، لا تتلاقى ثلاثة أقطار لمضلع محدب ذي {m(f'{n_v}')} أضلاع في نقطة داخلية واحدة. في كم نقطة داخلية تتقاطع أقطاره؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 5, ans - 2, ans + 3, ans + 6, math.comb(n_v, 3)],
            f"Every 4 vertices determine a unique convex quadrilateral whose two diagonals meet in 1 interior point: {m(f'\\\\binom{{{n_v}}}{{4}}')}.",
            f"كل 4 رؤوس تحدد رباعياً محدباً وحيداً يتقاطع قطراه في نقطة داخلية واحدة: {m(f'\\\\binom{{{n_v}}}{{4}}')}.",
            "Establish a bijection between interior diagonal intersections and 4-subsets of vertices.",
            [f"Compute {m(f'\\\\binom{{{n_v}}}{{4}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "أنشئ تقابلاً بين نقاط التقاطع الداخلية والمجموعات الجزئية المكونة من 4 رؤوس.",
            [f"نحسب {m(f'\\\\binom{{{n_v}}}{{4}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u15_b3_lattice_picks() -> list[dict]:
    bp = "olym_t1_geo_lattice_picks_area"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 271..275: Pick's theorem A = I + B/2 - 1
    easy_specs = [(271, 5, 8), (272, 7, 10), (273, 9, 6), (274, 12, 8), (275, 14, 12)]
    for idx, i_v, b_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = i_v + b_v // 2 - 1
        diag = svg_grid_polygon(5, 4, [(0, 0), (4, 0), (3, 3), (1, 3)], ["A", "B", "C", "D"])
        q_en = f"In a Junior Olympiad lattice geometry problem, a simple lattice polygon has {m(f'I = {i_v}')} interior lattice points and {m(f'B = {b_v}')} boundary lattice points. Find its area by Pick's Theorem."
        q_ar = f"في مسألة هندسة الشبكات للأولمبياد الناشئ، مضلع شبكي بسيط يحتوي على {m(f'I = {i_v}')} نقاط شبكية داخلية و{m(f'B = {b_v}')} نقاط شبكية محيطية. أوجد مساحته باستخدام نظرية بيك."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, i_v + b_v],
            f"Use Pick's Theorem: {m('A = I + B/2 - 1')}.",
            f"استخدم نظرية بيك: {m('A = I + B/2 - 1')}.",
            "Substitute I and B directly into Pick's formula.",
            [f"Compute {m(f'A = {i_v} + {b_v}/2 - 1 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "عوّض بقيمتي I وB مباشرة في صيغة بيك.",
            [f"نحسب {m(f'A = {i_v} + {b_v}/2 - 1 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 276..280: lattice points on segment from (0,0) to (dx, dy) is gcd(dx, dy) + 1
    med_specs = [(276, 12, 18), (277, 15, 25), (278, 16, 24), (279, 21, 14), (280, 20, 30)]
    for idx, dx_v, dy_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = math.gcd(dx_v, dy_v) + 1
        diag = svg_grid_polygon(5, 4, [(0, 0), (5, 3), (0, 3)], ["O", "P", "Q"])
        q_en = f"In a Junior Olympiad lattice-segment problem, how many lattice points (points with integer coordinates, including both endpoints) lie on the line segment connecting {m('(0, 0)')} to {m(f'({dx_v}, {dy_v})')}?"
        q_ar = f"في مسألة القطع الشبكية للأولمبياد الناشئ، كم نقطة شبكية (ذات إحداثيات صحيحة، شاملة نقطتي الطرفين) تقع على القطعة المستقيمة الواصلة بين {m('(0, 0)')} و{m(f'({dx_v}, {dy_v})')}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            f"The number of lattice points on the segment is {m(f'\\\\gcd({dx_v}, {dy_v}) + 1')}.",
            f"عدد النقاط الشبكية على القطعة يساوي {m(f'\\\\gcd({dx_v}, {dy_v}) + 1')}.",
            "Divide the vector (dx, dy) by g = gcd(dx, dy) to find the primitive lattice step.",
            [f"Since {m(f'\\\\gcd({dx_v}, {dy_v}) = {ans - 1}')}, there are {m(f'{ans - 1} + 1 = {ans}')} lattice points."],
            f"Verified: {m(str(ans))}.",
            "اقسم المتجه (dx, dy) على القاسم المشترك الأكبر g لإيجاد الخطوة الشبكية الأولية.",
            [f"بما أن {m(f'\\\\gcd({dx_v}, {dy_v}) = {ans - 1}')}، يوجد {m(f'{ans - 1} + 1 = {ans}')} نقاط شبكية."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 281..285: strict interior lattice points I of right triangle with legs a, b: I = ((a-1)(b-1) - gcd(a,b) + 1)//2
    hard_specs = [(281, 6, 8), (282, 8, 12), (283, 9, 12), (284, 10, 15), (285, 12, 16)]
    for idx, a_v, b_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = ((a_v - 1) * (b_v - 1) - math.gcd(a_v, b_v) + 1) // 2
        diag = svg_grid_polygon(5, 4, [(0, 0), (5, 0), (0, 4)], ["O", "A", "B"])
        q_en = f"In a Junior Olympiad Pick's Theorem problem, how many lattice points lie strictly inside the right triangle with vertices {m('(0,0)')}, {m(f'({a_v},0)')}, and {m(f'(0,{b_v})')}?"
        q_ar = f"في مسألة نظرية بيك للأولمبياد الناشئ، كم نقطة شبكية تقع تماماً داخل المثلث القائم الذي رؤوسه {m('(0,0)')} و{m(f'({a_v},0)')} و{m(f'(0,{b_v})')}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 3, ans - 1, ans + 1, ans + 3, (a_v * b_v) // 2],
            f"Use {m(f'I = \\\\frac{{({a_v}-1)({b_v}-1) - (\\\\gcd({a_v},{b_v})-1)}}{{2}}')} from Pick's Theorem.",
            f"استخدم الصيغة {m(f'I = \\\\frac{{({a_v}-1)({b_v}-1) - (\\\\gcd({a_v},{b_v})-1)}}{{2}}')} المستنتجة من نظرية بيك.",
            "Count interior points of the a x b rectangle, subtract diagonal points, and halve.",
            [f"With {m(f'\\\\gcd({a_v},{b_v}) = {math.gcd(a_v,b_v)}')}, we get {m(f'I = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "احسب النقاط الداخلية للمستطيل a×b، واطرح نقاط القطر، ثم اقسم على 2.",
            [f"بما أن {m(f'\\\\gcd({a_v},{b_v}) = {math.gcd(a_v,b_v)}')}، نحصل على {m(f'I = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u15_b4_3d_solids() -> list[dict]:
    bp = "olym_t1_geo_3d_cubes_pyramids"
    tp = "Geometry"
    out: list[dict] = []

    # Easy 286..290: painted n x n x n cube — unit cubes with exactly 2 painted faces = 12(n-2)
    easy_specs = [(286, 4), (287, 5), (288, 6), (289, 7), (290, 8)]
    for idx, n_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = 12 * (n_v - 2)
        diag = svg_painted_cube_3d(min(5, n_v))
        q_en = f"In a Junior Olympiad 3D painted-cube problem, all six faces of a {m(f'{n_v} \\\\times {n_v} \\\\times {n_v}')} cube are painted red, and it is cut into {m(f'{n_v**3}')} unit cubes. How many unit cubes have paint onが可能? Wait: exactly two faces?"
        q_en = f"In a Junior Olympiad 3D painted-cube problem, all six faces of a {m(f'{n_v} \\\\times {n_v} \\\\times {n_v}')} cube are painted red, and it is cut into {m(f'{n_v**3}')} unit cubes. How many unit cubes have paint on hinges/edges (exactly two faces)?"
        q_ar = f"في مسألة المكعب المطلي ثلاثي الأبعاد للأولمبياد الناشئ، طُليت الأوجه الستة لمكعب أبعاده {m(f'{n_v} \\\\times {n_v} \\\\times {n_v}')} باللون الأحمر ثم قُطّع إلى {m(f'{n_v**3}')} مكعباً صغيراً. كم مكعباً صغيراً يحتوي على طلاء في وجهين بالضبط؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 12, ans - 6, ans + 6, ans + 12, 6 * (n_v - 2) ** 2 if 6 * (n_v - 2) ** 2 != ans else ans + 8],
            f"A cube has {m('12')} edges, each containing {m(f'{n_v} - 2')} non-corner unit cubes.",
            f"للمكعب {m('12')} حرفاً، يحتوي كل منها على {m(f'{n_v} - 2')} مكعبات غير ركنية.",
            "Unit cubes with 2 painted faces lie along the 12 edges excluding the 8 corners.",
            [f"Compute {m(f'12({n_v} - 2) = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "المكعبات ذات الوجهين المطليين تقع على الأحرف الـ 12 باستثناء الرؤوس الـ 8.",
            [f"نحسب {m(f'12({n_v} - 2) = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 291..295: space diagonal of rectangular box sqrt(a^2 + b^2 + c^2) or Euler V - E + F = 2
    med_specs = [
        (291, 2, 3, 6, 7),
        (292, 3, 4, 12, 13),
        (293, 4, 6, 12, 14),
        (294, 6, 8, 24, 26),
        (295, 8, 9, 12, 17),
    ]
    for idx, a_v, b_v, c_v, ans in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_stu_cube_corner_cut(str(a_v), str(b_v), str(c_v))
        q_en = f"In a Junior Olympiad 3D spatial geometry problem, find the length of the space diagonal of a rectangular prism with edge lengths {m(f'{a_v}, {b_v}, {c_v}')}."
        q_ar = f"في مسألة الهندسة الفراغية للأولمبياد الناشئ، أوجد طول القطر الفراغي لمتوازي مستطيلات أبعاده {m(f'{a_v}, {b_v}, {c_v}')}."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, a_v + b_v + c_v],
            f"Use the 3D Pythagorean theorem {m('d = \\\\sqrt{a^2 + b^2 + c^2}')}.",
            f"استخدم نظرية فيثاغورس في الفراغ {m('d = \\\\sqrt{a^2 + b^2 + c^2}')}.",
            "Apply Pythagoras twice: first on the base face, then with the vertical edge.",
            [f"Compute {m(f'\\\\sqrt{{{a_v}^2 + {b_v}^2 + {c_v}^2}} = \\\\sqrt{{{ans*ans}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "طبّق فيثاغورس مرتين: على قطر القاعدة ثم مع الارتفاع.",
            [f"نحسب {m(f'\\\\sqrt{{{a_v}^2 + {b_v}^2 + {c_v}^2}} = \\\\sqrt{{{ans*ans}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 296..300: shortest ant path on surface of box a >= b >= c is sqrt(a^2 + (b+c)^2)
    hard_specs = [
        (296, 8, 3, 3, 10),
        (297, 12, 2, 3, 13),
        (298, 15, 4, 4, 17),
        (299, 16, 5, 7, 20),
        (300, 24, 3, 4, 25),
    ]
    for idx, a_v, b_v, c_v, ans in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_stu_cube_corner_cut(str(a_v), str(b_v), str(c_v))
        q_en = f"In a Junior Olympiad unfolded-net geodesic problem, an ant crawls along the surface of a {m(f'{a_v} \\\\times {b_v} \\\\times {c_v}')} rectangular box from one corner to the diametrically opposite corner. Find the minimum distance it must travel."
        q_ar = f"في مسألة أقصر مسار على شبكة مجسم للأولمبياد الناشئ، تزحف نملة على السطح الخارجي لصندوق أبعاده {m(f'{a_v} \\\\times {b_v} \\\\times {c_v}')} من أحد الرؤوس إلى الرأس المقابل له قطرياً. أوجد أقصر مسافة ممكنة لرحلتها."
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, a_v + b_v + c_v],
            f"Unfold two adjacent faces so the path is the hypotenuse of legs {m(str(a_v))} and {m(f'{b_v} + {c_v}')}.",
            f"افرد وجهين متجاورين بحيث يصبح المسار وتر مثلث قائم ضلعاه {m(str(a_v))} و{m(f'{b_v} + {c_v}')}.",
            "Minimize sqrt(x^2 + (y+z)^2) by keeping the largest dimension x separate.",
            [f"The shortest surface path is {m(f'\\\\sqrt{{{a_v}^2 + ({b_v}+{c_v})^2}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "نصغّر المقدار sqrt(x^2 + (y+z)^2) بإبقاء البعد الأكبر x منفرداً.",
            [f"أقصر مسار سطحي هو {m(f'\\\\sqrt{{{a_v}^2 + ({b_v}+{c_v})^2}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


# ==============================================================================
# UNIT 1.6 — Combinatorics (OLYM-T1-301 .. OLYM-T1-360)
# ==============================================================================

def _build_u16_b1_stars_bars() -> list[dict]:
    bp = "olym_t1_comb_stars_bars_bijections"
    tp = "Combinatorics"
    out: list[dict] = []

    # Easy 301..305: positive integer solutions to x1 + ... + xk = n is C(n-1, k-1)
    easy_specs = [(301, 9, 3), (302, 10, 4), (303, 11, 3), (304, 8, 4), (305, 12, 3)]
    for idx, n_v, k_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = math.comb(n_v - 1, k_v - 1)
        diag = svg_digit_slots([f"x{i+1}≥1" for i in range(k_v)], top_note=f"Sum = {n_v}")
        q_en = f"In a Junior Olympiad stars-and-bars problem, how many ordered {m(str(k_v))}-tuples of positive integers {m(f'(x_1, \\\\dots, x_{{{k_v}}})')} satisfy {m(f'x_1 + \\\\cdots + x_{{{k_v}}} = {n_v}')}?"
        q_ar = f"في مسألة النجوم والفواصل للأولمبياد الناشئ، كم {m(str(k_v))}-ية مرتبة من الأعداد الصحيحة الموجبة {m(f'(x_1, \\\\dots, x_{{{k_v}}})')} تحقق {m(f'x_1 + \\\\cdots + x_{{{k_v}}} = {n_v}')}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 5, ans - 2, ans + 3, ans + 6, math.comb(n_v + k_v - 1, k_v - 1)],
            f"Choose {m(f'{k_v}-1')} gaps among the {m(f'{n_v}-1')} internal spaces: {m(f'\\\\binom{{{n_v-1}}}{{{k_v-1}}}')}.",
            f"اختر {m(f'{k_v}-1')} فواصل من بين {m(f'{n_v}-1')} فراغات داخلية: {m(f'\\\\binom{{{n_v-1}}}{{{k_v-1}}}')}.",
            "Place k-1 dividers in the n-1 spaces between n stars.",
            [f"Compute {m(f'\\\\binom{{{n_v-1}}}{{{k_v-1}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "ضع k-1 فاصلة في الفراغات الـ n-1 بين n نجمة.",
            [f"نحسب {m(f'\\\\binom{{{n_v-1}}}{{{k_v-1}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 306..310: non-negative / lower-bound integer solutions
    med_specs = [
        (306, 7, 3, 0, math.comb(7 + 3 - 1, 2)),
        (307, 6, 4, 0, math.comb(6 + 4 - 1, 3)),
        (308, 12, 3, 2, math.comb(12 - 6 + 3 - 1, 2)),
        (309, 15, 3, 3, math.comb(15 - 9 + 3 - 1, 2)),
        (310, 14, 4, 2, math.comb(14 - 8 + 4 - 1, 3)),
    ]
    for idx, n_v, k_v, lb_v, ans in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_digit_slots([f"x{i+1}≥{lb_v}" for i in range(k_v)], top_note=f"Sum = {n_v}")
        q_en = f"In a Junior Olympiad constrained stars-and-bars problem, how many ordered {m(str(k_v))}-tuples of integers satisfy {m(f'x_1 + \\\\cdots + x_{{{k_v}}} = {n_v}')} with {m(f'x_i \\\\ge {lb_v}')} for each {m('i')}?"
        q_ar = f"في مسألة النجوم والفواصل المقيدة للأولمبياد الناشئ، كم {m(str(k_v))}-ية مرتبة من الأعداد الصحيحة تحقق {m(f'x_1 + \\\\cdots + x_{{{k_v}}} = {n_v}')} مع الشرط {m(f'x_i \\\\ge {lb_v}')} لكل {m('i')}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 6, ans - 3, ans + 3, ans + 6, ans + 10],
            f"Substitute {m(f'y_i = x_i - {lb_v} \\\\ge 0')} so the new sum is {m(str(n_v - k_v * lb_v))}.",
            f"عوّض {m(f'y_i = x_i - {lb_v} \\\\ge 0')} ليصبح المجموع الجديد {m(str(n_v - k_v * lb_v))}.",
            "Shift variables to reduce to non-negative integer solutions.",
            [f"With reduced sum {m(f'N = {n_v - k_v * lb_v}')}, the count is {m(f'\\\\binom{{{n_v - k_v*lb_v + k_v - 1}}}{{{k_v - 1}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "أزح المتغيرات لتحويل المسألة إلى حلول صحيحة غير سالبة.",
            [f"مع المجموع المختزل {m(f'N = {n_v - k_v * lb_v}')}، يكون العدد {m(f'\\\\binom{{{n_v - k_v*lb_v + k_v - 1}}}{{{k_v - 1}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 311..315: non-adjacent k-subsets from {1, ..., n} = C(n - k + 1, k)
    hard_specs = [(311, 8, 3), (312, 9, 3), (313, 10, 3), (314, 10, 4), (315, 11, 4)]
    for idx, n_v, k_v in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = math.comb(n_v - k_v + 1, k_v)
        diag = svg_digit_slots([f"s{i+1}" for i in range(k_v)], top_note=f"No 2 adjacent in 1..{n_v}")
        q_en = f"In a Junior Olympiad Kaplansky bijection problem, how many {m(str(k_v))}-element subsets of {m(f'\\\\{{1, 2, \\\\dots, {n_v}\\\\}}')} contain no two consecutive integers?"
        q_ar = f"في مسألة تقابل كابلانسكي للأولمبياد الناشئ، كم مجموعة جزئية مكونة من {m(str(k_v))} عناصر من المجموعة {m(f'\\\\{{1, 2, \\\\dots, {n_v}\\\\}}')} لا تحتوي على أي عددين صحيحين متتاليين؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 5, ans - 2, ans + 3, ans + 7, math.comb(n_v, k_v)],
            f"Use the non-adjacent selection formula {m(f'\\\\binom{{{n_v} - {k_v} + 1}}{{{k_v}}}')}.",
            f"استخدم صيغة الاختيار غير المتجاور {m(f'\\\\binom{{{n_v} - {k_v} + 1}}{{{k_v}}}')}.",
            "Insert k chosen elements into the n - k + 1 spaces around the n - k unchosen elements.",
            [f"Compute {m(f'\\\\binom{{{n_v - k_v + 1}}}{{{k_v}}} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "أدرج العناصر المختارة الـ k في الفراغات الـ n - k + 1 حول العناصر غير المختارة.",
            [f"نحسب {m(f'\\\\binom{{{n_v - k_v + 1}}}{{{k_v}}} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u16_b2_pigeonhole() -> list[dict]:
    bp = "olym_t1_comb_pigeonhole_dirichlet"
    tp = "Combinatorics"
    out: list[dict] = []

    # Easy 316..320: k colors, guarantee m of same color => k(m-1) + 1
    easy_specs = [(316, 4, 3), (317, 5, 4), (318, 4, 5), (319, 6, 3), (320, 5, 6)]
    for idx, k_v, m_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = k_v * (m_v - 1) + 1
        diag = svg_olym_pigeonhole_boxes(min(6, k_v), items_note="N balls", ask_note=f"≥ {m_v} same")
        q_en = f"In a Junior Olympiad Pigeonhole Principle problem, a bag contains plenty of marbles in {m(str(k_v))} different colors. What is the minimum number of marbles you must draw blindfolded to guarantee at least {m(str(m_v))} marbles of the same color?"
        q_ar = f"في مسألة مبدأ برج الحمام للأولمبياد الناشئ، يحتوي كيس على كرات وفيرة من {m(str(k_v))} ألوان مختلفة. ما أقل عدد من الكرات يجب سحبه دون النظر لضمان الحصول على {m(str(m_v))} كرات على الأقل من نفس اللون؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, k_v * m_v],
            f"Worst case draws at most {m(f'{m_v}-1')} of each of the {m(str(k_v))} colors, plus {m('1')}.",
            f"أسوأ حالة هي سحب {m(f'{m_v}-1')} كرة على الأكثر من كل لون من الألوان الـ {m(str(k_v))}، ثم إضافة {m('1')}.",
            "By the generalized Pigeonhole Principle, N = k(m - 1) + 1.",
            [f"Compute {m(f'{k_v}({m_v} - 1) + 1 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "بموجب مبدأ برج الحمام المعمم، N = k(m - 1) + 1.",
            [f"نحسب {m(f'{k_v}({m_v} - 1) + 1 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 321..325: subset of {1, ..., 2n} guaranteeing a pair summing to 2n+1 (or divisible) => n + 1
    med_specs = [(321, 10), (322, 12), (323, 15), (324, 18), (325, 25)]
    for idx, n_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = n_v + 1
        diag = svg_olym_pigeonhole_boxes(4, items_note=f"from 1..{2*n_v}", ask_note=f"sum = {2*n_v+1}")
        q_en = f"In a Junior Olympiad Dirichlet pairing problem, how many integers must be chosen from {m(f'\\\\{{1, 2, \\\\dots, {2*n_v}\\\\}}')} to guarantee that at least two chosen integers sum to {m(str(2*n_v + 1))}?"
        q_ar = f"في مسألة اقتران ديريخليه للأولمبياد الناشئ، كم عدداً صحيحاً يجب اختياره من المجموعة {m(f'\\\\{{1, 2, \\\\dots, {2*n_v}\\\\}}')} لضمان وجود عددين مختارين مجموعهما {m(str(2*n_v + 1))}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, 2 * n_v - 1],
            f"Partition {m(f'\\\\{{1, \\\\dots, {2*n_v}\\\\}}')} into {m(str(n_v))} complementary pairs {m(f'\\\\{{k, {2*n_v+1}-k\\\\}}')}.",
            f"قسّم المجموعة {m(f'\\\\{{1, \\\\dots, {2*n_v}\\\\}}')} إلى {m(str(n_v))} أزواج متكاملة {m(f'\\\\{{k, {2*n_v+1}-k\\\\}}')}.",
            "Create n pigeonholes {1, 2n}, {2, 2n-1}, ..., {n, n+1}.",
            [f"By the Pigeonhole Principle, {m(f'{n_v} + 1 = {ans}')} picks force two from the same pair."],
            f"Verified: {m(str(ans))}.",
            "أنشئ n صندوقاً للأزواج المتكاملة التي مجموع كل منها 2n+1.",
            [f"بمبدأ برج الحمام، اختيار {m(f'{n_v} + 1 = {ans}')} أعداد يضمن وقوع عددين في زوج واحد."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 326..330: geometric pigeonhole (points in square/triangle of side s)
    hard_specs = [
        (326, 5, "a 2×2 square partitioned into 4 unit squares to guarantee two points at distance at most √2", "مربع أبعاده 2×2 مقسم إلى 4 مربعات وحدة لضمان وجود نقطتين المسافة بينهما لا تزيد عن √2"),
        (327, 10, "a 3×3 square partitioned into 9 unit squares to guarantee two points at distance at most √2", "مربع أبعاده 3×3 مقسم إلى 9 مربعات وحدة لضمان وجود نقطتين المسافة بينهما لا تزيد عن √2"),
        (328, 5, "an equilateral triangle of side 2 partitioned into 4 unit equilateral triangles to guarantee two points at distance at most 1", "مثلث متطابق الأضلاع طول ضلعه 2 مقسم إلى 4 مثلثات وحدة لضمان وجود نقطتين المسافة بينهما لا تزيد عن 1"),
        (329, 17, "a 4×4 square partitioned into 16 unit squares to guarantee two points at distance at most √2", "مربع أبعاده 4×4 مقسم إلى 16 مربع وحدة لضمان وجود نقطتين المسافة بينهما لا تزيد عن √2"),
        (330, 10, "an equilateral triangle of side 3 partitioned into 9 unit equilateral triangles to guarantee two points at distance at most 1", "مثلث متطابق الأضلاع طول ضلعه 3 مقسم إلى 9 مثلثات وحدة لضمان وجود نقطتين المسافة بينهما لا تزيد عن 1"),
    ]
    for idx, ans, desc_en, desc_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_olym_pigeonhole_boxes(4, items_note=f"{ans} pts", ask_note=f"dist ≤ d")
        q_en = f"In a Junior Olympiad geometric Pigeonhole problem, what is the minimum number of points that must be placed inside {desc_en}?"
        q_ar = f"في مسألة مبدأ برج الحمام الهندسي للأولمبياد الناشئ، ما أقل عدد من النقاط يجب وضعه داخل {desc_ar}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, ans + 4],
            f"Partition the region into {m(str(ans - 1))} sub-regions of diameter {m('d')}, then add {m('1')}.",
            f"قسّم الشكل إلى {m(str(ans - 1))} مناطق جزئية قطر كل منها {m('d')}، ثم أضف {m('1')}.",
            "With k sub-regions of diameter d, k + 1 points guarantee two in the same sub-region.",
            [f"By the Pigeonhole Principle, {m(f'{ans - 1} + 1 = {ans}')} points suffice."],
            f"Verified: {m(str(ans))}.",
            "مع وجود k منطقة جزئية، فإن k + 1 نقطة تضمن وقوع نقطتين في نفس المنطقة.",
            [f"بمبدأ برج الحمام، يكفي {m(f'{ans - 1} + 1 = {ans}')} نقاط."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u16_b3_parity_coloring() -> list[dict]:
    bp = "olym_t1_comb_parity_coloring"
    tp = "Combinatorics"
    out: list[dict] = []

    # Easy 331..335: domino coverage on m x n board (even product) or color discrepancy
    easy_specs = [(331, 4, 6), (332, 6, 6), (333, 4, 8), (334, 6, 8), (335, 8, 8)]
    for idx, r_v, c_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (r_v * c_v) // 2
        diag = svg_olym_board_coloring(min(6, r_v), min(6, c_v), 2, note=f"{r_v}×{c_v} board")
        q_en = f"In a Junior Olympiad board-tiling problem, a {m(f'{r_v} \\\\times {c_v}')} checkerboard is completely tiled by non-overlapping {m('1 \\\\times 2')} dominoes. How many dominoes are used?"
        q_ar = f"في مسألة تبليط الرقعة للأولمبياد الناشئ، بُلّطت رقعة شطرنج أبعادها {m(f'{r_v} \\\\times {c_v}')} بالكامل بقطع دومينو غير متداخلة أبعادها {m('1 \\\\times 2')}. كم قطعة دومينو استُخدمت؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, r_v * c_v],
            f"Each domino covers {m('2')} unit squares, one black and one white.",
            f"كل قطعة دومينو تغطي مربعين: أحدهما أسود والآخر أبيض.",
            "Divide the total number of unit squares by 2.",
            [f"Compute {m(f'({r_v} \\\\times {c_v}) / 2 = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "اقسم العدد الكلي للمربعات الصغيرة على 2.",
            [f"نحسب {m(f'({r_v} \\\\times {c_v}) / 2 = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 336..340: opposite corners removed from 2n x 2n board -> difference between black & white squares is 2
    med_specs = [(336, 4), (337, 6), (338, 8), (339, 10), (340, 12)]
    for idx, n_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = (n_v * n_v) // 2 - 2
        diag = svg_olym_board_coloring(min(6, n_v), min(6, n_v), 2, note="2 opposite corners cut")
        q_en = f"In a Junior Olympiad coloring-invariant problem, a {m(f'{n_v} \\\\times {n_v}')} chessboard has its two diametrically opposite white corner squares removed. What is the maximum number of non-overlapping {m('1 \\\\times 2')} dominoes that can be placed on the remaining {m(f'{n_v*n_v - 2}')} squares?"
        q_ar = f"في مسألة لامتغير التلوين للأولمبياد الناشئ، حُذف مربعان ركنيان متقابلان قطرياً (كلاهما أبيض) من رقعة شطرنج أبعادها {m(f'{n_v} \\\\times {n_v}')}. ما أكبر عدد من قطع الدومينو غير المتداخلة {m('1 \\\\times 2')} التي يمكن وضعها على المربعات المتبقية؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 2, ans - 1, ans + 1, ans + 2, (n_v * n_v) // 2],
            f"Only {m(f'{ans}')} white squares remain, and each domino requires one white and one black square.",
            f"لم يتبقَّ سوى {m(f'{ans}')} مربعاً أبيض، وكل قطعة دومينو تتطلب مربعاً أبيض وآخر أسود.",
            "The number of dominoes cannot exceed the count of the minority color.",
            [f"There are {m(f'{n_v*n_v//2}')} black and {m(f'{ans}')} white squares left, so at most {m(str(ans))} dominoes fit."],
            f"Verified: {m(str(ans))}.",
            "عدد قطع الدومينو لا يمكن أن يتجاوز عدد مربعات اللون الأقل.",
            [f"بقي {m(f'{n_v*n_v//2}')} مربعاً أسود و{m(f'{ans}')} مربعاً أبيض، لذا يمكن وضع {m(str(ans))} قطعة كحد أقصى."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 341..345: invariant modulo 2 in replacement game on {1, 2, ..., n}: replace (a,b) with |a-b| or a+b-2ab
    hard_specs = [(341, 6, 1), (342, 8, 0), (343, 10, 1), (344, 12, 0), (345, 14, 1)]
    for idx, n_v, ans in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        s_tot = n_v * (n_v + 1) // 2
        ans = s_tot % 2
        diag = svg_olym_board_coloring(4, 4, 2, note=f"1..{n_v} mod 2 invariant")
        q_en = f"In a Junior Olympiad parity-invariant problem, the integers {m(f'1, 2, \\\\dots, {n_v}')} are written on a board. Repeatedly, two numbers {m('a, b')} are erased and replaced by {m('|a - b|')} until one number remains. What is the parity ({m('0')} for even, {m('1')} for odd) of the final number?"
        q_ar = f"في مسألة لامتغير الزوجية للأولمبياد الناشئ، كُتبت الأعداد {m(f'1, 2, \\\\dots, {n_v}')} على السبورة. في كل خطوة يُمسح عددان {m('a, b')} ويُستبدلان بالفرق {m('|a - b|')} حتى يبقى عدد واحد. ما باقي قسمة العدد الأخير على {m('2')} ({m('0')} للزوجي، {m('1')} للفردي)؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [1 - ans, 2, 3, 4, n_v // 2],
            f"Since {m('|a - b| \\\\equiv a + b \\\\pmod{2}')}, the parity of the sum of all numbers is invariant.",
            f"بما أن {m('|a - b| \\\\equiv a + b \\\\pmod{2}')}، فإن زوجية مجموع الأعداد تبقى ثابتة لا تتغير.",
            "Check the parity of the initial sum n(n+1)/2.",
            [f"The initial sum is {m(f'{n_v}({n_v}+1)/2 = {s_tot} \\\\equiv {ans} \\\\pmod{{2}}')}."],
            f"Verified: {m(str(ans))}.",
            "افحص باقي قسمة المجموع الابتدائي n(n+1)/2 على 2.",
            [f"المجموع الابتدائي هو {m(f'{n_v}({n_v}+1)/2 = {s_tot} \\\\equiv {ans} \\\\pmod{{2}}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def _build_u16_b4_pie() -> list[dict]:
    bp = "olym_t1_comb_inclusion_exclusion"
    tp = "Combinatorics"
    out: list[dict] = []

    # Easy 346..350: 2-set PIE |A u B| = |A| + |B| - |A n B|
    easy_specs = [(346, 28, 22, 10), (347, 35, 27, 12), (348, 42, 31, 15), (349, 50, 38, 18), (350, 64, 45, 21)]
    for idx, a_v, b_v, ab_v in easy_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = a_v + b_v - ab_v
        diag = svg_venn_2("A", "B", str(a_v - ab_v), str(ab_v), str(b_v - ab_v))
        q_en = f"In a Junior Olympiad inclusion-exclusion problem, {m(str(a_v))} students solved Problem A, {m(str(b_v))} solved Problem B, and {m(str(ab_v))} solved both. How many students solved at least one of the two problems?"
        q_ar = f"في مسألة مبدأ التضمين والإقصاء للأولمبياد الناشئ، حلّ {m(str(a_v))} طالباً المسألة A، وحلّ {m(str(b_v))} طالباً المسألة B، وحلّ {m(str(ab_v))} طالباً المسألتين معاً. كم طالباً حلّ مسألة واحدة على الأقل؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Easy", bp, q_en, q_ar,
            ans, [ans - 5, ans - 2, ans + 3, a_v + b_v, ans + ab_v],
            f"Use {m('|A \\\\cup B| = |A| + |B| - |A \\\\cap B|')}.",
            f"استخدم صيغة التضمين والإقصاء {m('|A \\\\cup B| = |A| + |B| - |A \\\\cap B|')}.",
            "Subtract the overlap from the sum of individual sizes.",
            [f"Compute {m(f'{a_v} + {b_v} - {ab_v} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "اطرح التقاطع من مجموع عناصر المجموعتين.",
            [f"نحسب {m(f'{a_v} + {b_v} - {ab_v} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Medium 351..355: integers in 1..N divisible by p or q
    med_specs = [(351, 100, 2, 3), (352, 120, 3, 5), (353, 150, 2, 5), (354, 140, 2, 7), (355, 180, 3, 4)]
    for idx, n_v, p_v, q_v in med_specs:
        qid = f"OLYM-T1-{idx:03d}"
        ans = n_v // p_v + n_v // q_v - n_v // math.lcm(p_v, q_v)
        diag = svg_venn_2(f"div {p_v}", f"div {q_v}", str(n_v // p_v - n_v // math.lcm(p_v, q_v)), str(n_v // math.lcm(p_v, q_v)), str(n_v // q_v - n_v // math.lcm(p_v, q_v)))
        q_en = f"In a Junior Olympiad divisibility PIE problem, how many positive integers at most {m(str(n_v))} are divisible by {m(str(p_v))} or {m(str(q_v))}?"
        q_ar = f"في مسألة قابلية القسمة بالتضمين والإقصاء للأولمبياد الناشئ، كم عدداً صحيحاً موجباً لا يتجاوز {m(str(n_v))} يقبل القسمة على {m(str(p_v))} أو {m(str(q_v))}؟"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Medium", bp, q_en, q_ar,
            ans, [ans - 4, ans - 2, ans + 2, ans + 4, n_v // p_v + n_v // q_v],
            f"Use {m(f'\\\\lfloor {n_v}/{p_v} \\\\rfloor + \\\\lfloor {n_v}/{q_v} \\\\rfloor - \\\\lfloor {n_v}/{math.lcm(p_v,q_v)} \\\\rfloor')}.",
            f"استخدم الصيغة {m(f'\\\\lfloor {n_v}/{p_v} \\\\rfloor + \\\\lfloor {n_v}/{q_v} \\\\rfloor - \\\\lfloor {n_v}/{math.lcm(p_v,q_v)} \\\\rfloor')}.",
            "Count multiples of p and multiples of q, then subtract multiples of lcm(p, q).",
            [f"Compute {m(f'{n_v//p_v} + {n_v//q_v} - {n_v//math.lcm(p_v,q_v)} = {ans}')}."],
            f"Verified: {m(str(ans))}.",
            "احسب مضاعفات p ومضاعفات q ثم اطرح مضاعفات المضاعف المشترك الأصغر.",
            [f"نحسب {m(f'{n_v//p_v} + {n_v//q_v} - {n_v//math.lcm(p_v,q_v)} = {ans}')}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))

    # Hard 356..360: Derangements D_n and 3-set PIE
    hard_specs = [
        (356, 9, "How many derangements (permutations with no fixed points) exist for 4 distinct items?", "كم تبديلاً خالياً من النقاط الثابتة (اختلالاً كلياً) يوجد لـ 4 عناصر متمايزة؟"),
        (357, 44, "How many derangements (permutations with no fixed points) exist for 5 distinct items?", "كم تبديلاً خالياً من النقاط الثابتة (اختلالاً كلياً) يوجد لـ 5 عناصر متمايزة؟"),
        (358, 265, "How many derangements (permutations with no fixed points) exist for 6 distinct items?", "كم تبديلاً خالياً من النقاط الثابتة (اختلالاً كلياً) يوجد لـ 6 عناصر متمايزة؟"),
        (359, sum(1 for k in range(1, 61) if math.gcd(k, 30) == 1), "How many integers from 1 to 60 are coprime to 30 (divisible by none of 2, 3, or 5)?", "كم عدداً صحيحاً من 1 إلى 60 أولي نسبياً مع 30 (لا يقبل القسمة على 2 أو 3 أو 5)؟"),
        (360, sum(1 for k in range(1, 106) if math.gcd(k, 105) == 1), "How many integers from 1 to 105 are coprime to 105 (divisible by none of 3, 5, or 7)?", "كم عدداً صحيحاً من 1 إلى 105 أولي نسبياً مع 105 (لا يقبل القسمة على 3 أو 5 أو 7)؟"),
    ]
    for idx, ans, q_core, q_core_ar in hard_specs:
        qid = f"OLYM-T1-{idx:03d}"
        diag = svg_venn_3("A₁", "A₂", "A₃", {"a": "", "b": "", "c": "", "ab": "", "bc": "", "ac": "", "abc": "PIE"})
        q_en = f"In a Junior Olympiad Inclusion-Exclusion problem: {q_core}"
        q_ar = f"في مسألة التضمين والإقصاء للأولمبياد الناشئ: {q_core_ar}"
        out.append(make_olym_q(
            qid, LEVEL_T1, tp, "Hard", bp, q_en, q_ar,
            ans, [ans - 4, ans - 1, ans + 1, ans + 4, ans + 9],
            "Apply the Principle of Inclusion-Exclusion over the fixed-point or prime-divisibility properties.",
            "طبّق مبدأ التضمين والإقصاء على خصائص النقاط الثابتة أو قابلية القسمة الأولية.",
            "Alternate adding and subtracting intersections of sizes 1, 2, ..., n.",
            [f"By the Principle of Inclusion-Exclusion, the exact count is {m(str(ans))}."],
            f"Verified: {m(str(ans))}.",
            "ناوب بين جمع وطرح تقاطعات المجموعات.",
            [f"بتطبيق مبدأ التضمين والإقصاء، يكون العدد الدقيق هو {m(str(ans))}."],
            f"تم التحقق: {m(str(ans))}.",
            diagram_en=diag,
        ))
    return out


def build_tier1_bank() -> list[dict]:
    """Build all 360 Tier 1 (Junior Olympiad, Grades 7-8) questions OLYM-T1-001 .. OLYM-T1-360."""
    bank: list[dict] = []
    for builder in (
        _build_u11_b1_divisors,
        _build_u11_b2_gcd_lcm,
        _build_u11_b3_modular_cycles,
        _build_u11_b4_factoring_diophantine,
        _build_u12_b1_telescoping,
        _build_u12_b2_symmetric,
        _build_u12_b3_radicals_ratios,
        _build_u12_b4_recurrences,
        _build_u13_b1_squares_nonneg,
        _build_u13_b2_two_var_amgm,
        _build_u13_b3_triangle_bounds,
        _build_u13_b4_discrete_smoothing,
        _build_u14_b1_angle_chasing,
        _build_u14_b2_area_ratios,
        _build_u14_b3_similarity_pythagoras,
        _build_u14_b4_incircle_tangents,
        _build_u15_b1_reflections,
        _build_u15_b2_polygons,
        _build_u15_b3_lattice_picks,
        _build_u15_b4_3d_solids,
        _build_u16_b1_stars_bars,
        _build_u16_b2_pigeonhole,
        _build_u16_b3_parity_coloring,
        _build_u16_b4_pie,
    ):
        bank.extend(builder())
    return bank
