"""Track 3 (Grades 10-11) — Number Theory (110 authentic KMC Senior problems)."""
import itertools
import math

from kmc_common import (
    explain_ar,
    explain_en,
    m,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams import (
    svg_column_cryptarithm,
    svg_number_triangle_puzzle,
)

LEVEL = "Track 3: Grades 10-11"
TOPIC = "Number Theory"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg=None):
        nonlocal idx
        qid = f"KMC-T3-NT-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, TOPIC, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg,
            )
        )

    # ------------------------------------------------------------------
    # 1. Block sequence 1, 2, 2, 3, 3, 3, ... via triangular numbers (KMC Senior Cat B Q2!) (10 Qs)
    # ------------------------------------------------------------------
    blk_cases = [
        (40, "Easy"),
        (60, "Easy"),
        (100, "Easy"),
        (150, "Medium"),
        (200, "Medium"),
        (300, "Medium"),
        (500, "Medium"),
        (800, "Medium"),
        (1000, "Hard"),
        (2026, "Hard"),
    ]
    for v_i, (N_pos, diff) in enumerate(blk_cases):
        # Build sequence directly to verify
        seq = []
        k = 1
        while len(seq) < N_pos + 5:
            seq.extend([k] * k)
            k += 1
        ans = seq[N_pos - 1]
        t_prev = (ans - 1) * ans // 2
        t_cur = ans * (ans + 1) // 2
        assert t_prev < N_pos <= t_cur
        distractors = [ans - 1, ans + 1, ans + 2, max(2, ans - 2)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_blk_{v_i}")
        q_en = (
            f"In the sequence {m('1, 2, 2, 3, 3, 3, 4, 4, 4, 4, \\dots')}, each positive integer {m('k')} appears {m('k')} consecutive times. "
            f"What is the {m(f'{N_pos}\\text{{th}}')} term of this sequence?"
        )
        q_ar = (
            f"في المتتالية {m('1, 2, 2, 3, 3, 3, 4, 4, 4, 4, \\dots')}، يتكرر كل عدد صحيح موجب {m('k')} بالضبط {m('k')} من المرات المتتالية. "
            f"ما الحد رقم {m(N_pos)} في هذه المتتالية؟"
        )
        h_en = "By the end of the block of k's, how many terms have appeared in total? Exactly 1 + 2 + ... + k = k(k+1)/2!"
        h_ar = "مع نهاية مجموعة العدد k، كم حداً يكون قد ظهر في المتتالية؟ المجموع المثلثي 1 + 2 + ... + k = k(k+1)/2 بالضبط!"
        s_en = explain_en(
            "The block of \\( k \\)'s ends at position \\( T_k = 1 + 2 + \\dots + k = \\frac{k(k+1)}{2} \\). So we just find the triangular numbers straddling \\( " + str(N_pos) + " \\)!",
            [
                f"Test \\( k = {ans - 1} \\): block \\( {ans - 1} \\) ends at position {m(f'\\frac{{{ans-1} \\times {ans}}}{{2}} = {t_prev}')}.",
                f"Test \\( k = {ans} \\): block \\( {ans} \\) runs from position {m(t_prev + 1)} up to {m(f'\\frac{{{ans} \\times {ans+1}}}{{2}} = {t_cur}')}.",
                f"Since {m(f'{t_prev} < {N_pos} \\le {t_cur}')}, the {m(f'{N_pos}\\text{{th}}')} term equals **{m(ans)}**.",
            ],
            f"Quick estimate trick: \\( \\frac{{k^2}}{{2}} \\approx {N_pos} \\implies k^2 \\approx {2*N_pos} \\implies k \\approx {int((2*N_pos)**0.5)} \\) gets you right next to \\( {ans} \\) immediately!",
        )
        s_ar = explain_ar(
            "تنتهي مجموعة العدد \\( k \\) عند الرتبة \\( T_k = 1 + 2 + \\dots + k = \\frac{k(k+1)}{2} \\). لذا نبحث عن العددين المثلثيين اللذين يحصران الرتبة \\( " + str(N_pos) + " \\)!",
            [
                f"عند \\( k = {ans - 1} \\): تنتهي مجموعته عند الرتبة {m(f'\\frac{{{ans-1} \\times {ans}}}{{2}} = {t_prev}')}.",
                f"عند \\( k = {ans} \\): تمتد مجموعته من الرتبة {m(t_prev + 1)} إلى {m(f'\\frac{{{ans} \\times {ans+1}}}{{2}} = {t_cur}')}.",
                f"بما أن {m(f'{t_prev} < {N_pos} \\le {t_cur}')}، فإن الحد رقم {m(N_pos)} هو **{m(ans)}**.",
            ],
            f"حيلة تقدير سريعة: \\( k^2 \\approx 2 \\times {N_pos} = {2*N_pos} \\) تقودك مباشرة إلى جوار العدد \\( {ans} \\)!",
        )
        push(diff, "kmc_g1011_block_sequence_triangular", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 2. Floor function sum \sum_{n=1}^M floor(((kn + 1)^2) / n^2) (KMC Senior Q4!) (10 Qs)
    # ------------------------------------------------------------------
    flr_cases = [
        (1, 10, "Easy"),
        (1, 20, "Easy"),
        (2, 10, "Easy"),
        (2, 25, "Medium"),
        (3, 15, "Medium"),
        (3, 30, "Medium"),
        (4, 20, "Medium"),
        (4, 50, "Hard"),
        (5, 30, "Hard"),
        (2, 100, "Hard"),
    ]
    for v_i, (k, M, diff) in enumerate(flr_cases):
        terms = [((k * n + 1) ** 2) // (n * n) for n in range(1, M + 1)]
        ans = sum(terms)
        base_val = k * k
        cutoff = 2 * k  # for n >= 2k + 1, 2k/n + 1/n^2 < 1 so floor is k^2!
        assert all(t == base_val for t in terms[cutoff:])
        early_str = ", ".join(f"n={n}: {terms[n-1]}" for n in range(1, cutoff + 1))
        rem_cnt = M - cutoff
        distractors = [M * base_val, ans - 1, ans + base_val, ans + 2]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_flr_{v_i}")
        num_tex = f"({k}n + 1)^2" if k > 1 else "(n + 1)^2"
        q_en = (
            f"Recall that {m('\\lfloor x \\rfloor')} denotes the greatest integer less than or equal to {m('x')}. "
            f"What is the exact value of {m(f'\\sum_{{n=1}}^{{{M}}} \\left\\lfloor \\frac{{{num_tex}}}{{n^2}} \\right\\rfloor')}?"
        )
        q_ar = (
            f"إذا كان الرمز {m('\\lfloor x \\rfloor')} يرمُز لأكبر عدد صحيح أقل من أو يساوي {m('x')} (دالة الصحيح)، "
            f"فما القيمة الدقيقة للمجموع {m(f'\\sum_{{n=1}}^{{{M}}} \\left\\lfloor \\frac{{{num_tex}}}{{n^2}} \\right\\rfloor')}؟"
        )
        h_en = f"Expand {num_tex}/n² = {base_val} + {2*k}/n + 1/n²! Once n ≥ {cutoff + 1}, the fractional tail is strictly less than 1, so EVERY remaining term equals {base_val}!"
        h_ar = f"فكّ البسط واقسم على n²: المقدار يساوي {base_val} + {2*k}/n + 1/n²! عندما يكون n ≥ {cutoff + 1} يصبح الكسر أصغر من 1 فتثبت جميع الحدود المتبقية عند {base_val}!"
        s_en = explain_en(
            f"Expand the fraction: \\( \\frac{{{num_tex}}}{{n^2}} = {base_val} + \\frac{{{2*k}}}{{n}} + \\frac{{1}}{{n^2}} \\). As \\( n \\) grows, the fraction part drops below \\( 1 \\) and stays below \\( 1 \\) forever!",
            [
                f"Compute the first {m(cutoff)} terms directly ({early_str}), whose sum is {m(sum(terms[:cutoff]))}.",
                f"For every {m(f'n \\ge {cutoff + 1}')}, {m(f'\\frac{{{2*k}}}{{n}} + \\frac{{1}}{{n^2}} < 1')}, so the floor equals **{m(base_val)}** for all remaining {m(f'{M} - {cutoff} = {rem_cnt}')} terms!",
                f"Add them: {m(f'{sum(terms[:cutoff])} + {rem_cnt} \\times {base_val} = {ans}')}.",
            ],
            f"Check at boundary {m(f'n = {cutoff}')} vs {m(f'n = {cutoff+1}')}: at {m(f'n={cutoff}')} the tail is {m(f'1 + \\frac{{1}}{{{cutoff**2}}} > 1')}, whereas at {m(f'n={cutoff+1}')} it drops below {m(1)}!",
        )
        s_ar = explain_ar(
            f"نفكّ البسط ونقسم على \\( n^2 \\): \\( \\frac{{{num_tex}}}{{n^2}} = {base_val} + \\frac{{{2*k}}}{{n}} + \\frac{{1}}{{n^2}} \\). بعد حدٍّ صغير يصبح الجزء الكسري أصغر من \\( 1 \\) دائماً!",
            [
                f"نحسب أول {m(cutoff)} حدود مباشرة ({early_str}) ومجموعها {m(sum(terms[:cutoff]))}.",
                f"لكل {m(f'n \\ge {cutoff + 1}')} يكون {m(f'\\frac{{{2*k}}}{{n}} + \\frac{{1}}{{n^2}} < 1')}، فتثبت قيمة دالة الصحيح عند **{m(base_val)}** للحدود الـ {m(rem_cnt)} المتبقية!",
                f"المجموع الكلي: {m(f'{sum(terms[:cutoff])} + {rem_cnt} \\times {base_val} = {ans}')}.",
            ],
            f"تحقق عند الحد الفاصل {m(f'n = {cutoff}')}: الجزء الكسري أكبر من 1، بينما من {m(cutoff+1)} فصاعداً يصبح أصغر من 1!",
        )
        push(diff, "kmc_g1011_floor_sum_jump", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 3. Linear Diophantine GCD threshold ax + by >= M (KMC Senior 27x+36y >= 555!) (10 Qs)
    # ------------------------------------------------------------------
    dio_cases = [
        (12, 18, 100, "Easy"),     # gcd=6 -> 102
        (14, 21, 150, "Easy"),     # gcd=7 -> 154
        (15, 25, 212, "Easy"),     # gcd=5 -> 215
        (27, 36, 555, "Medium"),   # gcd=9 -> 558 (exact KMC Senior!)
        (24, 40, 300, "Medium"),   # gcd=8 -> 304
        (22, 33, 400, "Medium"),   # gcd=11 -> 407
        (26, 39, 500, "Medium"),   # gcd=13 -> 507
        (28, 42, 600, "Medium"),   # gcd=14 -> 602
        (34, 51, 700, "Hard"),     # gcd=17 -> 714
        (38, 57, 1000, "Hard"),    # gcd=19 -> 1007
    ]
    for v_i, (a, b, M_min, diff) in enumerate(dio_cases):
        g = math.gcd(a, b)
        assert M_min % g != 0
        ans = ((M_min + g - 1) // g) * g
        # Find concrete integers (x0, y0) with a*x0 + b*y0 == ans
        x0, y0 = None, None
        for xx in range(-200, 201):
            if (ans - a * xx) % b == 0:
                x0, y0 = xx, (ans - a * xx) // b
                break
        assert x0 is not None and a * x0 + b * y0 == ans
        distractors = [M_min, M_min + 1, ans + g, ans - g]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_dio_{v_i}")
        q_en = (
            f"Integers {m('x')} and {m('y')} (which may be positive, negative, or zero) satisfy {m(f'{a}x + {b}y \\ge {M_min}')}. "
            f"What is the **smallest possible value** of {m(f'{a}x + {b}y')}?"
        )
        q_ar = (
            f"عددان صحيحان {m('x')} و{m('y')} (قد يكونان موجبين أو سالبين أو صفراً) يحققان {m(f'{a}x + {b}y \\ge {M_min}')}. "
            f"ما **أصغر قيمة ممكنة** للمقدار {m(f'{a}x + {b}y')}؟"
        )
        h_en = f"Notice both {a} and {b} are multiples of g = gcd({a}, {b}) = {g}! So {a}x + {b}y MUST be a multiple of {g}!"
        h_ar = f"لاحظ أن كلاً من {a} و{b} يقبل القسمة على القاسم المشترك الأكبر g = gcd({a}, {b}) = {g}! إذن {a}x + {b}y لا بد أن يكون من مضاعفات {g}!"
        s_en = explain_en(
            f"For any integers \\( x, y \\), the possible values of \\( ax + by \\) are **every exact multiple** of \\( g = \\gcd(a, b) \\)!",
            [
                f"Factor out {m(f'g = \\gcd({a}, {b}) = {g}')}: {m(f'{a}x + {b}y = {g}({a//g}x + {b//g}y)')}, which is always a multiple of **{m(g)}**.",
                f"Because {m(f'\\gcd({a//g}, {b//g}) = 1')}, {m(f'{a//g}x + {b//g}y')} can equal ANY integer, so we just need the smallest multiple of {m(g)} that is {m(f'\\ge {M_min}')}.",
                f"Divide {m(M_min)} by {m(g)}: {m(f'{M_min} = {M_min // g} \\times {g} + {M_min % g}')}, so the next multiple of {m(g)} is {m(f'{(M_min // g) + 1} \\times {g} = {ans}')}.",
            ],
            f"Concrete witness check: taking {m(f'x = {x0}, y = {y0}')} gives {m(f'{a}({x0}) + {b}({y0}) = {ans}')}!",
        )
        s_ar = explain_ar(
            f"لأي عددين صحيحين \\( x, y \\)، القيم التي يمكن أن يأخذها المقدار \\( ax + by \\) هي **جميع مضاعفات** القاسم المشترك الأكبر \\( g = \\gcd(a, b) \\)!",
            [
                f"نخرج العامل المشترك الأكبر {m(f'g = \\gcd({a}, {b}) = {g}')}: {m(f'{a}x + {b}y = {g}({a//g}x + {b//g}y)')}، فهو دائماً مضاعف للعدد **{m(g)}**.",
                f"بما أن {m(f'\\gcd({a//g}, {b//g}) = 1')} يمكن تكوين أي مضاعف لـ {m(g)}، فنبحث عن أصغر مضاعف للعدد {m(g)} أكبر من أو يساوي {m(M_min)}.",
                f"بما أن {m(f'{M_min} = {M_min // g} \\times {g} + {M_min % g}')}، فإن أصغر مضاعف تالٍ هو {m(f'{(M_min // g) + 1} \\times {g} = {ans}')}.",
            ],
            f"مثال تحققي بالأعداد: عند {m(f'x = {x0}, y = {y0}')} نحصل على {m(f'{a}({x0}) + {b}({y0}) = {ans}')} بالضبط!",
        )
        push(diff, "kmc_g1011_gcd_threshold_min", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 4. Prime parity trap: A - n and B - n both prime with A - B odd (KMC Senior!) (10 Qs)
    # ------------------------------------------------------------------
    # Need A - B odd AND 2 + (A - B) prime!
    # Odd differences d where 2 + d is prime: d in {3->5, 5->7, 9->11, 11->13, 15->17, 17->19, 21->23, 27->29, 29->31, 39->41}!
    prm_cases = [
        (30, 27, "Easy"),    # d=3, primes 5 and 2, n = 25
        (42, 37, "Easy"),    # d=5, primes 7 and 2, n = 35
        (50, 41, "Easy"),    # d=9, primes 11 and 2, n = 39
        (65, 54, "Medium"),  # d=11, primes 13 and 2, n = 52
        (80, 65, "Medium"),  # d=15, primes 17 and 2, n = 63
        (93, 76, "Medium"),  # d=17, primes 19 and 2, n = 74
        (100, 79, "Medium"), # d=21, primes 23 and 2, n = 77
        (120, 93, "Medium"), # d=27, primes 29 and 2, n = 91
        (150, 121, "Hard"),  # d=29, primes 31 and 2, n = 119
        (200, 161, "Hard"),  # d=39, primes 41 and 2, n = 159
    ]
    for v_i, (A, B, diff) in enumerate(prm_cases):
        d = A - B
        assert d % 2 == 1 and is_prime(2 + d)
        ans = B - 2
        # Verify uniqueness across all integers n <= B
        all_n = [n for n in range(-500, B + 1) if is_prime(A - n) and is_prime(B - n)]
        assert all_n == [ans]
        distractors = [B - 3, B - 1, A - 2, ans - 2]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_prm_{v_i}")
        q_en = (
            f"For a certain integer {m('n')}, both {m(f'{A} - n')} and {m(f'{B} - n')} are **prime numbers**. "
            f"What is the value of {m('n')}?"
        )
        q_ar = (
            f"يوجد عدد صحيح {m('n')} يجعل كلاً من {m(f'{A} - n')} و{m(f'{B} - n')} **عددين أوليين**. "
            f"ما قيمة {m('n')}؟"
        )
        h_en = f"Subtract the two primes: ({A} − n) − ({B} − n) = {d}, which is ODD! How can the difference of two primes be odd?"
        h_ar = f"اطرح العددين الأوليين: ({A} − n) − ({B} − n) = {d}، وهو عدد **فردي**! متى يكون الفرق بين عددين أوليين فردياً؟"
        s_en = explain_en(
            "Almost all primes are odd, and `(odd) − (odd) = (even)`. The ONLY way two primes have an **odd** difference is when one of them is even — and **\\( 2 \\) is the only even prime**!",
            [
                f"Subtract the two expressions ({m('n')} cancels!): {m(f'({A} - n) - ({B} - n) = {d}')}, which is **odd**.",
                f"Therefore the smaller prime {m(f'{B} - n')} MUST equal **{m(2)}**!",
                f"Solve {m(f'{B} - n = 2 \\implies n = {B} - 2 = {ans}')}, and check that {m(f'{A} - {ans} = {2 + d}')} is indeed prime!",
            ],
            f"Both {m(2)} and {m(2 + d)} are prime, so {m(f'n = {ans}')} is the unique integer solution!",
        )
        s_ar = explain_ar(
            "جميع الأعداد الأولية فردية ما عدا \\( 2 \\)، والفرق بين عددين فرديين زوجي دائماً! لذا إذا كان الفرق بين عددين أوليين **فردياً** فلا بد أن يكون أصغرهما هو **\\( 2 \\)**!",
            [
                f"نطرح المقدارين فتختفي {m('n')}: {m(f'({A} - n) - ({B} - n) = {d}')}، وهو عدد **فردي**.",
                f"إذن العدد الأولي الأصغر {m(f'{B} - n')} يجب أن يساوي **{m(2)}** حتماً!",
                f"نحل المعادلة {m(f'{B} - n = 2 \\implies n = {ans}')}، ونتأكد أن {m(f'{A} - {ans} = {2 + d}')} عدد أولي فعلاً!",
            ],
            f"كلا العددين {m(2)} و{m(2 + d)} أوليان، مما يؤكد أن {m(f'n = {ans}')} هو الحل الوحيد!",
        )
        push(diff, "kmc_g1011_prime_parity_trap", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 5. Factorial product perfect square: n * a! * (a+1)! or n * a! * (a+2)! (KMC Senior!) (10 Qs)
    # ------------------------------------------------------------------
    fac_cases = [
        (7, 8, "Easy"),       # 7! * 8! = (7!)^2 * 8 -> square-free of 8 is 2!
        (11, 12, "Easy"),     # (11!)^2 * 12 -> square-free of 12 is 3!
        (17, 18, "Easy"),     # (17!)^2 * 18 -> 2!
        (19, 20, "Medium"),   # (19!)^2 * 20 -> 5!
        (23, 24, "Medium"),   # (23!)^2 * 24 -> 6!
        (26, 27, "Medium"),   # (26!)^2 * 27 -> 3!
        (7, 9, "Medium"),     # 7! * 9! = (7!)^2 * (8 * 9) = (7!)^2 * 72 -> 2!
        (8, 10, "Medium"),    # (8!)^2 * (9 * 10) = (8!)^2 * 90 -> 10!
        (9, 11, "Hard"),      # (9!)^2 * 110 -> 110? Wait let's pick (11, 13): 12*13=156 -> 39; or (14, 16): 15*16=240 = 16*15 -> 15!
        (17, 19, "Hard"),     # (17!)^2 * (18 * 19) = (17!)^2 * 9 * 38 -> 38!
    ]
    fac_cases[8] = (14, 16, "Hard")
    for v_i, (a, b, diff) in enumerate(fac_cases):
        prod_rem = 1
        for x in range(a + 1, b + 1):
            prod_rem *= x
        # Square-free part of prod_rem: divide out largest square k^2 dividing prod_rem
        ans = prod_rem
        for sq in range(int(math.isqrt(prod_rem)), 1, -1):
            if ans % (sq * sq) == 0:
                ans //= (sq * sq)
                break
        # Verify directly with full factorial big integer!
        full_val = ans * math.factorial(a) * math.factorial(b)
        rt = math.isqrt(full_val)
        assert rt * rt == full_val
        for cand in range(1, ans):
            cv = cand * math.factorial(a) * math.factorial(b)
            assert math.isqrt(cv) ** 2 != cv

        distractors = [prod_rem if prod_rem != ans else ans * 2, a, b, ans * 2, max(2, ans + 3)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_fac_{v_i}")
        rem_factors = " \\times ".join(str(x) for x in range(a + 1, b + 1))
        sq_part = prod_rem // ans
        q_en = (
            f"What is the **smallest positive integer** {m('n')} such that the product "
            f"{m(f'n \\times {a}! \\times {b}!')} is a **perfect square**?"
        )
        q_ar = (
            f"ما **أصغر عدد صحيح موجب** {m('n')} يجعل حاصل الضرب "
            f"{m(f'n \\times {a}! \\times {b}!')} **مربعاً كاملاً**؟"
        )
        h_en = f"Rewrite {b}! as {a}! × ({rem_factors}) so ({a}!)² pulls right out as a giant perfect square!"
        h_ar = f"أعد كتابة {b}! على الصورة {a}! × ({rem_factors}) ليظهر المربع الكامل ({a}!)² مباشرة!"
        s_en = explain_en(
            f"Never expand factorials! Pair them up using \\( {b}! = {a}! \\times {rem_factors} \\) so \\( {a}! \\times {b}! = ({a}!)^2 \\times ({prod_rem}) \\)!",
            [
                f"Pull out the square {m(f'({a}!)^2')}: we only need {m(f'n \\times {prod_rem}')} to be a perfect square.",
                f"Factor out the largest perfect square inside {m(prod_rem)}: {m(f'{prod_rem} = {sq_part} \\times {ans} = ({math.isqrt(sq_part)})^2 \\times {ans}')}.",
                f"To complete the remaining square-free factor {m(ans)}, the smallest positive integer is **{m(f'n = {ans}')}**.",
            ],
            f"With {m(f'n = {ans}')}, {m(f'n \\cdot {a}! \\cdot {b}! = ({a}! \\times {math.isqrt(sq_part)} \\times {ans})^2')} — an exact square!",
        )
        s_ar = explain_ar(
            f"لا تفكّ المضروب كاملاً! استخدم العلاقة \\( {b}! = {a}! \\times {rem_factors} \\) فيصبح الجداء \\( ({a}!)^2 \\times {prod_rem} \\)!",
            [
                f"بما أن {m(f'({a}!)^2')} مربع كامل جاهز، يكفي أن نجعل {m(f'n \\times {prod_rem}')} مربعاً كاملاً.",
                f"نخرج أكبر مربع كامل من {m(prod_rem)}: {m(f'{prod_rem} = {sq_part} \\times {ans} = ({math.isqrt(sq_part)})^2 \\times {ans}')}.",
                f"لموازنة العامل المتبقي {m(ans)} لكي يصبح مربعاً، فإن أصغر قيمة موجبة هي **{m(f'n = {ans}')}**.",
            ],
            f"عند {m(f'n = {ans}')} يصبح الجداء الكلي مربعاً كاملاً بالضبط!",
        )
        push(diff, "kmc_g1011_factorial_square", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. Highest power of prime p dividing A^k ± B^k (KMC Senior 300^9 style!) (10 Qs)
    # ------------------------------------------------------------------
    vp_cases = [
        # (A, B, k, sign, p, diff) — exact v_p computed on Python big int!
        (60, 3, 8, "+", 3, "Easy"),       # 3^8 * (20^8 + 1); 20 == -1 mod 3 -> 20^8 + 1 == 1 + 1 = 2 != 0 mod 3 -> ans = 8!
        (300, 3, 9, "+", 3, "Easy"),      # 3^9 * (100^9 + 1); 100 == 1 mod 3 -> 1 + 1 = 2 -> ans = 9!
        (50, 5, 7, "-", 5, "Easy"),       # 5^7 * (10^7 - 1); 10 == 0 mod 5 -> -1 != 0 mod 5 -> ans = 7!
        (70, 7, 10, "-", 7, "Medium"),    # 7^10 * (10^10 - 1); 10 == 3 mod 7, 3^6=1, 3^4=4 != 1 -> ans = 10!
        (45, 9, 6, "+", 3, "Medium"),     # 9^6 * (5^6 + 1) = 3^12 * (5^6 + 1); 5^2=1 mod 3 -> 1+1=2 -> ans = 12!
        (80, 16, 5, "-", 2, "Medium"),    # 16^5 * (5^5 - 1) = 2^20 * (5^5 - 1); 5^5 - 1: 5 = 1 mod 4, 5^5-1 = (5-1)(odd)=4*(odd)! v_2 = 22!
        (250, 25, 6, "-", 5, "Medium"),   # 25^6 * (10^6 - 1) = 5^12 * (multiple of 5 - 1) -> ans = 12!
        (180, 9, 8, "+", 3, "Medium"),    # 9^8 * (20^8 + 1) = 3^16 * (2 mod 3) -> ans = 16!
        (270, 27, 7, "+", 3, "Hard"),     # 27^7 * (10^7 + 1) = 3^21 * (1 + 1 mod 3) -> ans = 21!
        (300, 3, 6, "-", 3, "Hard"),      # 3^6 * (100^6 - 1): let's check exact v_3!
    ]
    # Replace index 5 & 9 with crystal-clear cases where remaining factor is coprime to p so students follow in 3 lines!
    vp_cases[5] = (150, 25, 5, "+", 5, "Medium")
    vp_cases[9] = (490, 49, 6, "+", 7, "Hard")
    for v_i, (A, B, k, sign, p, diff) in enumerate(vp_cases):
        assert A % B == 0
        q_ratio = A // B
        big = (A ** k + B ** k) if sign == "+" else (A ** k - B ** k)
        ans = 0
        tmp = big
        while tmp % p == 0:
            ans += 1
            tmp //= p
        # Check B = p^r * u where p does not divide (q_ratio^k ± 1)
        b_vp = 0
        tb = B
        while tb % p == 0:
            b_vp += 1
            tb //= p
        assert ans == b_vp * k, f"Expected clean factor {b_vp * k}, got {ans} for {(A,B,k,sign,p)}"
        distractors = [k, ans + 1, ans - 1 if ans > 1 else ans + 3, ans + k]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_vp_{v_i}")
        expr_tex = f"{A}^{{{k}}} {sign} {B}^{{{k}}}"
        inner_tex = f"{q_ratio}^{{{k}}} {sign} 1"
        rem_mod = (pow(q_ratio, k, p) + (1 if sign == "+" else -1)) % p
        q_en = f"What is the **largest integer** {m('m')} such that {m(f'{p}^m')} divides {m(expr_tex)}?"
        q_ar = f"ما **أكبر عدد صحيح** {m('m')} بحيث يقسم {m(f'{p}^m')} المقدار {m(expr_tex)}؟"
        h_en = f"Factor out {B}^{k} first: {A}^{k} {sign} {B}^{k} = {B}^{k}({q_ratio}^{k} {sign} 1), then check whether ({q_ratio}^{k} {sign} 1) is divisible by {p}!"
        h_ar = f"أخرج العامل المشترك {B}^{k} أولاً: {A}^{k} {sign} {B}^{k} = {B}^{k}({q_ratio}^{k} {sign} 1)، ثم اختبر باقي قسمة ({q_ratio}^{k} {sign} 1) على {p}!"
        s_en = explain_en(
            f"Pull out the common base power \\( {B}^{{{k}}} \\) first, then check the remaining parenthesis modulo \\( {p} \\)!",
            [
                f"Since {m(f'{A} = {B} \\times {q_ratio}')}, factor: {m(f'{expr_tex} = {B}^{{{k}}}({inner_tex})')}.",
                f"Count factors of {m(p)} in {m(f'{B}^{{{k}}}')}: since {m(B)} contains {m(f'{p}^{{{b_vp}}}')}, {m(f'{B}^{{{k}}}')} contributes {m(f'{b_vp} \\times {k} = {ans}')} factors of {m(p)}.",
                f"Check {m(inner_tex)} modulo {m(p)}: it leaves remainder **{m(rem_mod)}** {m(f'\\ne 0 \\pmod{{{p}}}')}, contributing **{m(0)}** extra factors of {m(p)} — so {m(f'm = {ans}')}!",
            ],
            f"Verified on the exact integer {m(expr_tex)}: divisible by {m(f'{p}^{{{ans}}}')} and NOT by {m(f'{p}^{{{ans+1}}}')}!",
        )
        s_ar = explain_ar(
            f"نخرج القوة المشتركة \\( {B}^{{{k}}} \\) خارج قوس، ثم نفحص قابلية القوس المتبقي للقسمة على \\( {p} \\)!",
            [
                f"بما أن {m(f'{A} = {B} \\times {q_ratio}')} نحلّل المقدار: {m(f'{expr_tex} = {B}^{{{k}}}({inner_tex})')}.",
                f"قوة العامل {m(p)} في {m(f'{B}^{{{k}}}')}: يحوي {m(B)} القوة {m(f'{p}^{{{b_vp}}}')}، فتعطي {m(f'{B}^{{{k}}}')} الأس {m(f'{b_vp} \\times {k} = {ans}')}.",
                f"نفحص باقي قسمة {m(inner_tex)} على {m(p)} فنجده **{m(rem_mod)}** {m('\\ne 0')}، فلا يضيف أي عامل إضافي من {m(p)} — إذن {m(f'm = {ans}')}!",
            ],
            f"تم التحقق حسابياً: المقدار يقبل القسمة على {m(f'{p}^{{{ans}}}')} ولا يقبل القسمة على {m(f'{p}^{{{ans+1}}}')}!",
        )
        push(diff, "kmc_g1011_prime_power_diff", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 7. Verified unique alphametic column cryptarithms (10 Qs, SVG!)
    # ------------------------------------------------------------------
    alpha_cases = [
        (["AB", "B"], "BA", "A + B", "Easy"),
        (["AA", "B"], "BCC", "A + B + C", "Easy"),
        (["AB", "BA"], "AAC", "A + B + C", "Easy"),
        (["AA", "BB"], "CBC", "A + B + C", "Medium"),
        (["AB", "BC"], "BCB", "A + B + C", "Medium"),
        (["AB", "AB"], "BCC", "A + B + C", "Medium"),
        (["AA", "BB", "CC"], "BAC", "A + B + C", "Medium"),
        (["AB", "AB", "AB", "AB"], "CA", "A + B + C", "Medium"),
        (["ABC", "BC"], "BAA", "A + B + C", "Hard"),
        (["SEND", "MORE"], "MONEY", "M + O + N + E + Y", "Hard"),
    ]
    for v_i, (words, tot_w, ask_expr, diff) in enumerate(alpha_cases):
        letters = sorted(set("".join(words) + tot_w))
        leads = {w[0] for w in words + [tot_w]}
        sols = []
        for perm in itertools.permutations(range(10), len(letters)):
            mp = dict(zip(letters, perm))
            if any(mp[ch] == 0 for ch in leads):
                continue
            if sum(int("".join(str(mp[c]) for c in w)) for w in words) == int("".join(str(mp[c]) for c in tot_w)):
                sols.append(mp)
        assert len(sols) == 1, f"Cryptarithm {words}={tot_w} solutions: {sols}"
        mp = sols[0]
        ask_vars = [v.strip() for v in ask_expr.split("+")]
        ans = sum(mp[v] for v in ask_vars)
        svg = svg_column_cryptarithm(words, tot_w)
        distractors = [ans + 1, max(1, ans - 1), ans + 2, max(2, ans - 2)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_alp_{v_i}")
        assign_str = ", ".join(f"{k} = {mp[k]}" for k in letters)
        nums_sum = " + ".join("".join(str(mp[c]) for c in w) for w in words) + " = " + "".join(str(mp[c]) for c in tot_w)
        eq_tex = " + ".join(f"\\overline{{{w}}}" for w in words) + f" = \\overline{{{tot_w}}}"
        q_en = (
            f"In the column addition {m(eq_tex)} shown, different letters stand for **different digits** from {m('0')} to {m('9')}, "
            f"and no leading letter of a multi-digit number is {m('0')}. What is the value of {m(ask_expr)}?"
        )
        q_ar = (
            f"في عملية الجمع العمودية {m(eq_tex)} الموضحة، يمثّل كل حرف مختلف **رقماً مختلفاً** من {m('0')} إلى {m('9')}، "
            f"ولا يساوي الحرف الأول في اليسار لأي عدد الصفر {m('0')}. ما قيمة {m(ask_expr)}؟"
        )
        h_en = "Start with the leftmost carry digit (often forced to be 1!) and the ones-column parity/carry!"
        h_ar = "ابدأ من الرقم المحمول في أقصى اليسار (غالباً ما يُجبر على أن يكون 1!) ثم حلّل عمود الآحاد والحمل!"
        s_en = explain_en(
            "In alphametics, combine **place-value algebra** (e.g. \\( \\overline{AB} = 10A + B \\)) with **carry bounds** (adding two digits gives carry at most \\( 1 \\)).",
            [
                f"Write the place-value equation and bound the leftmost carry digit first.",
                f"Checking the ones and tens columns pins down the unique distinct digits: {m(assign_str)}.",
                f"Evaluate the requested sum: {m(f'{ask_expr} = {ans}')}.",
            ],
            f"Direct arithmetic verification: {m(nums_sum)}!",
        )
        s_ar = explain_ar(
            "في ألغاز الحروف الحسابية نجمع بين **القيمة المكانية** (مثل \\( \\overline{AB} = 10A + B \\)) و**حدود الحمل**.",
            [
                f"نكتب معادلة القيم المكانية ونحدّد قيمة الرقم المحمول في أقصى اليسار أولاً.",
                f"من توازن خانات الآحاد والعشرات تتحدد الأرقام الوحيدة المختلفة: {m(assign_str)}.",
                f"نحسب المجموع المطلوب: {m(f'{ask_expr} = {ans}')}.",
            ],
            f"تحقق حسابي مباشر: {m(nums_sum)}!",
        )
        push(diff, "kmc_g1011_cryptarithm_senior", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 8. Consecutive integers with one interior number erased (KMC Senior Q8!) (10 Qs)
    # ------------------------------------------------------------------
    era_cases = [
        # (count_written = k+1, start_a, erased_offset_j in 1..k-1, diff)
        (5, 10, 2, "Easy"),      # 5 consecutive -> 4 remain (k=4), j in 1..3 -> unique!
        (6, 14, 3, "Easy"),      # k=5
        (7, 20, 2, "Easy"),      # k=6
        (8, 25, 5, "Medium"),    # k=7
        (9, 30, 4, "Medium"),    # k=8
        (10, 42, 6, "Medium"),   # k=9
        (11, 50, 3, "Medium"),   # k=10
        (11, 80, 7, "Medium"),   # k=10
        (12, 100, 8, "Hard"),    # k=11
        (15, 140, 9, "Hard"),    # k=14
    ]
    for v_i, (n_tot, a_st, j_off, diff) in enumerate(era_cases):
        k_rem = n_tot - 1
        assert 1 <= j_off <= k_rem - 1
        erased = a_st + j_off
        full_sum = sum(range(a_st, a_st + n_tot))
        S_rem = full_sum - erased
        # Verify uniqueness across all positive starts a >= 1 and interior offsets 1..k_rem-1!
        matches = []
        for aa in range(1, S_rem + 5):
            fs = n_tot * aa + n_tot * (n_tot - 1) // 2
            cand_e = fs - S_rem
            if aa < cand_e < aa + n_tot - 1:
                matches.append((aa, cand_e))
        assert matches == [(a_st, erased)], f"Expected unique erased match, got {matches}"

        distractors = [erased - 1, erased + 1, erased + 2, a_st]
        opts_en, opts_ar, cidx, cans = make_5_math_options(erased, distractors, f"t3n_era_{v_i}")
        tri_k = n_tot * (n_tot - 1) // 2
        q_en = (
            f"{m(n_tot)} consecutive positive integers are written on a whiteboard. "
            f"One integer (**neither the smallest nor the largest**) is erased, and the sum of the remaining {m(k_rem)} integers is {m(S_rem)}. "
            f"Which integer was erased?"
        )
        q_ar = (
            f"كُتب {m(n_tot)} عدداً صحيحاً موجباً متتالياً على السبورة، ثم مُسِح عدد واحد منها (**ليس الأصغر وليس الأكبر**)، "
            f"فكان مجموع الأعداد الـ {m(k_rem)} المتبقية يساوي {m(S_rem)}. ما العدد الذي مُسِح؟"
        )
        h_en = f"Let the consecutive integers be a, a+1, ..., a+{n_tot-1}, and let the erased interior number be a+j (with 1 ≤ j ≤ {k_rem-1}). Look at the sum modulo {k_rem}!"
        h_ar = f"افرض الأعداد a، a+1، ...، a+{n_tot-1} والعدد الممسوح a+j (حيث 1 ≤ j ≤ {k_rem-1})، ثم ادرس المجموع المتبقي بالنسبة للقسمة على {k_rem}!"
        s_en = explain_en(
            f"Let the {m(n_tot)} consecutive integers start at \\( a \\), and let the erased interior number be \\( a + j \\) with \\( 1 \\le j \\le {k_rem - 1} \\).",
            [
                f"Full sum of {m(n_tot)} consecutive integers starting at {m('a')}: {m(f'{n_tot}a + {tri_k}')}. Subtracting {m('a + j')} leaves {m(f'{k_rem}a + {tri_k} - j = {S_rem}')}.",
                f"Rearrange: {m(f'{k_rem}a = {S_rem - tri_k} + j')}. Since {m(f'1 \\le j \\le {k_rem - 1}')}, there is **only one** value of {m('j')} making the right side divisible by {m(k_rem)}: {m(f'j = {j_off}')}!",
                f"Thus {m(f'a = \\frac{{{S_rem - tri_k + j_off}}}{{{k_rem}}} = {a_st}')}, and the erased integer is {m(f'a + j = {a_st} + {j_off} = {erased}')}.",
            ],
            f"Average check: {m(f'{S_rem} / {k_rem} \\approx {S_rem / k_rem:.2f}')}, putting the middle of the list right around {m(a_st + n_tot // 2)}!",
        )
        s_ar = explain_ar(
            f"نفرض أن الأعداد المتتالية تبدأ بـ \\( a \\)، وأن العدد الداخلي الممسوح هو \\( a + j \\) حيث \\( 1 \\le j \\le {k_rem - 1} \\).",
            [
                f"مجموع الأعداد الـ {m(n_tot)} الكاملة هو {m(f'{n_tot}a + {tri_k}')}، وبعد طرح {m('a + j')} يتبقى: {m(f'{k_rem}a + {tri_k} - j = {S_rem}')}.",
                f"نرتّب المعادلة: {m(f'{k_rem}a = {S_rem - tri_k} + j')}. وبما أن {m(f'1 \\le j \\le {k_rem - 1}')} توجد قيمة **وحيدة** لـ {m('j')} تجعل الطرف الأيمن مضاعفاً لـ {m(k_rem)} وهي {m(f'j = {j_off}')}!",
                f"إذن {m(f'a = {a_st}')}، والعدد الممسوح هو {m(f'{a_st} + {j_off} = {erased}')}.",
            ],
            f"تحقق سريع بالمتوسط: {m(f'{S_rem} \\div {k_rem} \\approx {S_rem / k_rem:.1f}')} مما يحدد موقع الأعداد فوراً!",
        )
        push(diff, "kmc_g1011_consecutive_subset_sum", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 9. Multiplicative number triangle -> sum of all three vertices (10 Qs, SVG!)
    # ------------------------------------------------------------------
    mtri_cases = [
        (4, 5, 6, "Easy"),
        (3, 7, 8, "Easy"),
        (5, 6, 9, "Easy"),
        (6, 7, 10, "Medium"),
        (5, 8, 11, "Medium"),
        (7, 9, 12, "Medium"),
        (8, 9, 15, "Medium"),
        (6, 11, 14, "Medium"),
        (9, 12, 16, "Hard"),
        (10, 14, 15, "Hard"),
    ]
    for v_i, (va, vb, vc, diff) in enumerate(mtri_cases):
        p1, p2, p3 = va * vb, va * vc, vb * vc
        xyz = va * vb * vc
        ans = va + vb + vc
        svg = svg_number_triangle_puzzle("?", "?", "?", str(p1), str(p2), str(p3))
        distractors = [ans + 2, ans - 2, va + vb + vc + 4, (p1 + p2 + p3) // 6]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_mtri_{v_i}")
        q_en = (
            f"Three positive integers are hidden inside the three corner circles of the triangle shown. "
            f"Each rectangle on an edge displays the **product** of the two corner integers on that edge ({m(p1)}, {m(p2)}, and {m(p3)}). "
            f"What is the **sum** of the three hidden corner integers?"
        )
        q_ar = (
            f"توجد ثلاثة أعداد صحيحة موجبة مخفية داخل الدوائر الثلاث عند رؤوس المثلث الموضح. "
            f"يعرض كل مستطيل على ضلع **حاصل ضرب** العددين في طرفيه ({m(p1)} و{m(p2)} و{m(p3)}). "
            f"ما **مجموع** الأعداد الثلاثة المخفية في الرؤوس؟"
        )
        h_en = "Multiply all three edge products together: (xy)(xz)(yz) = (xyz)²! Take the square root to get xyz, then divide by each edge!"
        h_ar = "اضرب نواتج الأضلاع الثلاثة معاً: (xy)(xz)(yz) = (xyz)²! خذ الجذر التربيعي لإيجاد xyz ثم اقسم على كل ضلع!"
        s_en = explain_en(
            "Multiplying all three pairwise products \\( xy, xz, yz \\) gives \\( (xy)(xz)(yz) = x^2 y^2 z^2 = (xyz)^2 \\)!",
            [
                f"Multiply and take the positive square root: {m(f'(xyz)^2 = {p1} \\times {p2} \\times {p3} = {xyz**2} \\implies xyz = {xyz}')}.",
                f"Divide {m(f'xyz = {xyz}')} by each opposite edge product: {m(f'z = {xyz}/{p1} = {vc}')}, {m(f'y = {xyz}/{p2} = {vb}')}, and {m(f'x = {xyz}/{p3} = {va}')}.",
                f"Sum the three corner numbers: {m(f'{va} + {vb} + {vc} = {ans}')}.",
            ],
            f"Keep numbers small when taking the square root by factoring ({m(f'{va}^2 \\times {vb}^2 \\times {vc}^2')}) instead of multiplying out {m(xyz**2)}!",
        )
        s_ar = explain_ar(
            "عند ضرب نواتج الأضلاع الثلاثة \\( xy, xz, yz \\) نحصل على \\( (xy)(xz)(yz) = (xyz)^2 \\)!",
            [
                f"بتحليل العوامل وأخذ الجذر التربيعي الموجب نجد حاصل الضرب الثلاثي: {m(f'xyz = {xyz}')}.",
                f"بقسمة {m(xyz)} على كل ضلع نوجد الرؤوس الثلاثة: {m(f'{vc}, {vb}, {va}')}.",
                f"نجمع الرؤوس الثلاثة: {m(f'{va} + {vb} + {vc} = {ans}')}.",
            ],
            f"نصيحة ذهبية بدون آلة حاسبة: حلّل الأعداد إلى عوامل صغيرة قبل أخذ الجذر التربيعي بدلاً من ضرب الأعداد الكبيرة!",
        )
        push(diff, "kmc_g1011_mult_triangle_gcd", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 10. Simultaneous remainder / Chinese Remainder puzzles (10 Qs)
    # ------------------------------------------------------------------
    crt_cases = [
        # (m1, r1, m2, r2, m3, r3, diff) -> smallest positive integer n
        (3, 2, 4, 3, 5, 4, "Easy"),       # n + 1 = lcm(3,4,5) = 60 -> 59!
        (4, 1, 5, 1, 6, 1, "Easy"),       # n - 1 = lcm(4,5,6) = 60 -> 61!
        (3, 1, 5, 3, 7, 5, "Easy"),       # n + 2 = 105 -> 103!
        (4, 2, 5, 3, 6, 4, "Medium"),     # n + 2 = 60 -> 58!
        (5, 2, 6, 3, 7, 4, "Medium"),     # n + 3 = 210 -> 207!
        (3, 2, 5, 3, 7, 2, "Medium"),     # classic Sunzi: 23!
        (4, 3, 5, 2, 7, 5, "Medium"),     # let's compute exact smallest >= 2!
        (5, 4, 7, 6, 8, 7, "Medium"),     # n + 1 = 280 -> 279!
        (6, 5, 7, 4, 8, 7, "Hard"),
        (5, 3, 7, 2, 9, 4, "Hard"),
    ]
    for v_i, (m1, r1, m2, r2, m3, r3, diff) in enumerate(crt_cases):
        L = math.lcm(m1, m2, m3)
        ans = next(n for n in range(2, L + 10) if n % m1 == r1 and n % m2 == r2 and n % m3 == r3)
        distractors = [L - 1 if L - 1 != ans else L + 1, ans + m1 * m2, max(2, ans - m3), L + r1]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_crt_{v_i}")
        q_en = (
            f"What is the **smallest integer greater than {m(1)}** that leaves remainder {m(r1)} when divided by {m(m1)}, "
            f"remainder {m(r2)} when divided by {m(m2)}, and remainder {m(r3)} when divided by {m(m3)}?"
        )
        q_ar = (
            f"ما **أصغر عدد صحيح أكبر من {m(1)}** يترك باقياً قدره {m(r1)} عند قسمته على {m(m1)}، "
            f"وباقياً قدره {m(r2)} عند قسمته على {m(m2)}، وباقياً قدره {m(r3)} عند قسمته على {m(m3)}؟"
        )
        h_en = f"Check if (divisor − remainder) is constant across the clues — or step through numbers of the form {m3}k + {r3}!"
        h_ar = f"تحقق أولاً هل الفرق (المقسوم عليه − الباقي) ثابت، أو اختبر مضاعفات المقسوم الأكبر على الصورة {m3}k + {r3}!"
        if (m1 - r1) == (m2 - r2) == (m3 - r3):
            gap = m1 - r1
            steps_en = [
                f"Spot the constant-deficit pattern: {m(f'{m1}-{r1} = {m2}-{r2} = {m3}-{r3} = {gap}')}!",
                f"That means {m(f'n + {gap}')} is divisible by {m(m1)}, {m(m2)}, AND {m(m3)}, so it must be a multiple of {m(f'\\operatorname{{lcm}}({m1},{m2},{m3}) = {L}')}.",
                f"Smallest positive solution: {m(f'n = {L} - {gap} = {ans}')}.",
            ]
            steps_ar = [
                f"نلاحظ نمط النقص الثابت: {m(f'{m1}-{r1} = {m2}-{r2} = {m3}-{r3} = {gap}')}!",
                f"هذا يعني أن {m(f'n + {gap}')} يقبل القسمة على {m(m1)} و{m(m2)} و{m(m3)} معاً، أي من مضاعفات {m(f'\\operatorname{{lcm}}({m1},{m2},{m3}) = {L}')}.",
                f"إذن أصغر عدد يحقق الشروط هو {m(f'n = {L} - {gap} = {ans}')}.",
            ]
        elif r1 == r2 == r3:
            steps_en = [
                f"All three divisions leave the **exact same remainder {m(r1)}**!",
                f"So {m(f'n - {r1}')} is a positive multiple of {m(f'\\operatorname{{lcm}}({m1},{m2},{m3}) = {L}')}.",
                f"Smallest solution {m('> 1')}: {m(f'n = {L} + {r1} = {ans}')}.",
            ]
            steps_ar = [
                f"القسمات الثلاث تترك **الباقي نفسه {m(r1)}**!",
                f"إذن {m(f'n - {r1}')} مضاعف موجب للمضاعف المشترك الأصغر {m(f'\\operatorname{{lcm}}({m1},{m2},{m3}) = {L}')}.",
                f"أصغر حل أكبر من {m(1)} هو {m(f'n = {L} + {r1} = {ans}')}.",
            ]
        else:
            L23 = math.lcm(m2, m3)
            base23 = next(x for x in range(1, L23 + 1) if x % m2 == r2 and x % m3 == r3)
            steps_en = [
                f"Combine the last two clues ({m(f'\\bmod\\,{m2}')} and {m(f'\\bmod\\,{m3}')}) by stepping by {m(m3)}: the first match is {m(base23)}, repeating every {m(f'\\operatorname{{lcm}}({m2},{m3}) = {L23}')}.",
                f"Test numbers of the form {m(f'{base23} + {L23}k')} until remainder mod {m(m1)} equals {m(r1)}.",
                f"The first match is **{m(ans)}**.",
            ]
            steps_ar = [
                f"ندمج الشرطين الأخيرين بالقفز بمقدار {m(m3)}: أول عدد يحققهما هو {m(base23)} ويتكرر كل {m(f'\\operatorname{{lcm}}({m2},{m3}) = {L23}')}.",
                f"نختبر الأعداد على الصورة {m(f'{base23} + {L23}k')} حتى يكون باقي القسمة على {m(m1)} مساوياً لـ {m(r1)}.",
                f"أول عدد يحقق الشروط الثلاثة هو **{m(ans)}**.",
            ]

        s_en = explain_en("Simultaneous remainder problems yield quickly to either a constant offset from the LCM or stepping by the largest modulus!", steps_en, f"Verify: \\( {ans} \\bmod {m1} = {ans%m1} \\), \\( {ans} \\bmod {m2} = {ans%m2} \\), \\( {ans} \\bmod {m3} = {ans%m3} \\)!")
        s_ar = explain_ar("مسائل البواقي المتزامنة تُحل بسهولة بملاحظة الفرق الثابت عن المضاعف المشترك الأصغر أو بالقفز وفق المقسوم الأكبر!", steps_ar, f"تحقق: باقي قسمة {m(ans)} على {m(m1)} و{m(m2)} و{m(m3)} هو {m(r1)} و{m(r2)} و{m(r3)} بالترتيب!")
        push(diff, "kmc_g1011_multi_constraint_integer", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 11. Sum of two squares divisible by p in {3, 7, 11} (10 Qs)
    # ------------------------------------------------------------------
    sqmod_cases = [
        (3, 15, "Easy"),
        (3, 25, "Easy"),
        (3, 30, "Easy"),
        (7, 25, "Medium"),
        (7, 40, "Medium"),
        (7, 50, "Medium"),
        (7, 70, "Medium"),
        (11, 50, "Medium"),
        (7, 100, "Hard"),
        (11, 100, "Hard"),
    ]
    res_map = {
        3: "0, 1",
        7: "0, 1, 2, 4",
        11: "0, 1, 3, 4, 5, 9",
    }
    for v_i, (p, N_max, diff) in enumerate(sqmod_cases):
        m_cnt = N_max // p
        ans = m_cnt * m_cnt
        # Brute-force verify on all N_max^2 ordered pairs!
        bf = sum(1 for a in range(1, N_max + 1) for b in range(1, N_max + 1) if (a * a + b * b) % p == 0)
        assert bf == ans
        distractors = [m_cnt, 2 * m_cnt, (N_max * N_max) // p, ans + m_cnt]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3n_sqm_{v_i}")
        q_en = (
            f"How many **ordered pairs** of integers {m('(a, b)')} with {m(f'1 \\le a \\le {N_max}')} and {m(f'1 \\le b \\le {N_max}')} "
            f"have the property that {m('a^2 + b^2')} is divisible by {m(p)}?"
        )
        q_ar = (
            f"كم **زوجاً مرتباً** من الأعداد الصحيحة {m('(a, b)')} حيث {m(f'1 \\le a \\le {N_max}')} و{m(f'1 \\le b \\le {N_max}')} "
            f"يحقق أن {m('a^2 + b^2')} يقبل القسمة على {m(p)}؟"
        )
        h_en = f"List all possible remainders of a² when divided by {p}: {{{res_map[p]}}}! Which two remainders from this list can add up to a multiple of {p}?"
        h_ar = f"اكتب جميع بواقي المربعات الممكنة عند القسمة على {p}: {{{res_map[p]}}}! أي باقيين منها فقط يمكن أن يكون مجموعهما مضاعفاً لـ {p}؟"
        s_en = explain_en(
            f"Modulo {m(p)}, the only possible remainders of a square \\( x^2 \\) are \\( \\{{{res_map[p]}\\}} \\). Notice that **NO two non-zero remainders** in that set add up to {m(p)}!",
            [
                f"Test all pairs from {m(f'\\{{{res_map[p]}\\}}')}: the **only** way {m(f'a^2 + b^2 \\equiv 0 \\pmod{{{p}}}')} is {m('0 + 0 \\equiv 0')}, meaning **both {m('a')} and {m('b')} must be multiples of {m(p)}**!",
                f"Between {m(1)} and {m(N_max)}, there are {m(f'\\lfloor {N_max}/{p} \\rfloor = {m_cnt}')} multiples of {m(p)}.",
                f"Choose {m('a')} in {m(m_cnt)} ways and {m('b')} independently in {m(m_cnt)} ways: {m(f'{m_cnt} \\times {m_cnt} = {ans}')} ordered pairs.",
            ],
            f"Checked across all {m(N_max**2)} pairs in {m(f'\\{{1..{N_max}\\}}^2')}: {m(ans)} pairs work!",
        )
        s_ar = explain_ar(
            f"عند القسمة على {m(p)}، البواقي الممكنة لأي مربع كامل \\( x^2 \\) هي فقط \\( \\{{{res_map[p]}\\}} \\)، ولا يوجد أي باقيين غير صفريين منها مجموعهما يساوي {m(p)}!",
            [
                f"بفحص الأزواج من {m(f'\\{{{res_map[p]}\\}}')} نجد أن الحالة الوحيدة لقسمة {m('a^2 + b^2')} على {m(p)} هي {m('0 + 0')}، أي يجب أن يكون **كلٌّ من {m('a')} و{m('b')} من مضاعفات {m(p)}**!",
                f"في المدى من {m(1)} إلى {m(N_max)} يوجد {m(f'\\lfloor {N_max}/{p} \\rfloor = {m_cnt}')} مضاعفاً للعدد {m(p)}.",
                f"عدد الأزواج المرتبة {m('(a, b)')} هو: {m(f'{m_cnt} \\times {m_cnt} = {ans}')}.",
            ],
            f"قاعدة ذهبية في نظرية الأعداد: لقسمة مجموع مربعين على عدد أولي يترك باقي 3 عند قسمته على 4 (مثل 3 و7 و11)، يجب أن يقسم العدد الأولي كلا العددين معاً!",
        )
        push(diff, "kmc_g1011_sum_squares_mod", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    assert len(out) == 110, f"Expected 110, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 3 Number Theory questions cleanly.")
