"""Track 2 (Grades 8-9) — Number Theory (110 authentic KMC problems)."""
import math

from kmc_common import (
    explain_ar,
    explain_en,
    m,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams import svg_number_strip

LEVEL = "Track 2: Grades 8-9"
TOPIC = "Number Theory"


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg=None):
        nonlocal idx
        qid = f"KMC-T2-NT-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, TOPIC, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg,
            )
        )

    # ------------------------------------------------------------------
    # 1. Coprime sequence: not divisible by p or q (KMC Junior Q6!) (10 Qs)
    # ------------------------------------------------------------------
    cop_cases = [
        (2, 3, 20, "Easy"),
        (2, 3, 35, "Easy"),
        (2, 3, 50, "Medium"),
        (2, 3, 100, "Medium"),
        (2, 5, 25, "Easy"),
        (2, 5, 42, "Medium"),
        (2, 5, 83, "Medium"),
        (3, 5, 30, "Medium"),
        (3, 5, 65, "Hard"),
        (2, 7, 61, "Hard"),
    ]
    for v_i, (p, q, k_term, diff) in enumerate(cop_cases):
        L = math.lcm(p, q)
        rem_block = [x for x in range(1, L + 1) if x % p != 0 and x % q != 0]
        b_sz = len(rem_block)
        # Brute-force verify
        seq = [x for x in range(1, k_term * L + 20) if x % p != 0 and x % q != 0]
        ans = seq[k_term - 1]
        q_blk, r_idx = divmod(k_term - 1, b_sz)
        assert ans == q_blk * L + rem_block[r_idx]
        svg = svg_number_strip([str(seq[0]), str(seq[1]), str(seq[2]), str(seq[3]), str(seq[4]), "..."])
        distractors = [seq[k_term], seq[max(0, k_term - 2)], ans + 2, max(1, ans - 2), q_blk * L + 1]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_cop_{v_i}")
        first5 = ", ".join(str(x) for x in seq[:5])
        blk_str = ", ".join(str(x) for x in rem_block)
        q_en = (
            f"All positive integers that are **neither divisible by {m(p)} nor divisible by {m(q)}** are written in increasing order: "
            f"{m(first5 + ', \\dots')}. What is the {m(f'{k_term}\\text{{th}}')} number in this sequence?"
        )
        q_ar = (
            f"كُتبت جميع الأعداد الصحيحة الموجبة التي **لا تقبل القسمة على {m(p)} ولا تقبل القسمة على {m(q)}** بترتيب تصاعدي: "
            f"{m(first5 + ', \\dots')}. ما العدد رقم {m(k_term)} في هذه المتتالية؟"
        )
        h_en = f"Group the integers into repeating blocks of length lcm({p}, {q}) = {L}! Every block contains the exact same count of surviving numbers."
        h_ar = f"قسّم الأعداد إلى مجموعات دورية طول كل منها المضاعف المشترك الأصغر lcm({p}, {q}) = {L}! كل مجموعة تحتوي على نفس العدد من الحدود."
        s_en = explain_en(
            f"Divisibility by {m(p)} and {m(q)} repeats every {m(f'\\operatorname{{lcm}}({p},{q}) = {L}')} integers.",
            [
                f"In the first block {m(f'1..{L}')}, the surviving numbers are {m(blk_str)} — that is **{m(b_sz)} numbers** per block of {m(L)}.",
                f"Write {m(k_term)} using blocks of {m(b_sz)}: {m(f'{q_blk} \\times {b_sz} = {q_blk * b_sz}')} numbers cover the first {m(q_blk)} full blocks (up to {m(q_blk * L)}).",
                f"We need the {m(f'{r_idx + 1}\\text{{th}}')} surviving number in the next block, which adds {m(rem_block[r_idx])}: {m(f'{q_blk * L} + {rem_block[r_idx]} = {ans}')}.",
            ],
            f"Check: {m(ans)} is neither divisible by {m(p)} nor by {m(q)}!",
        )
        s_ar = explain_ar(
            f"قابلية القسمة على {m(p)} و{m(q)} تتكرر دورياً كل {m(f'\\operatorname{{lcm}}({p},{q}) = {L}')} أعداد.",
            [
                f"في المجموعة الأولى من {m('1')} إلى {m(L)}، الأعداد المتبقية هي {m(blk_str)}، أي **{m(b_sz)} أعداد** في كل دورة طولها {m(L)}.",
                f"عدد الدورات الكاملة قبل الحد المطلوب: {m(f'{q_blk} \\times {b_sz} = {q_blk * b_sz}')} حداً تصل بنا إلى {m(q_blk * L)}.",
                f"نحتاج إلى الحد رقم {m(r_idx + 1)} في الدورة التالية، فنضيف {m(rem_block[r_idx])}: {m(f'{q_blk * L} + {rem_block[r_idx]} = {ans}')}.",
            ],
            f"تحقق: العدد {m(ans)} لا يقبل القسمة على {m(p)} ولا على {m(q)}!",
        )
        push(diff, "kmc_g89_coprime_sequence", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 2. Distinct positive integers with near-minimal sum -> product (KMC Junior Cat A Q4!) (10 Qs)
    # ------------------------------------------------------------------
    # For n distinct positive integers summing to T_n + 1, the unique set is {1, 2, ..., n-1, n+1}!
    # For T_n + 2, ask for MAXIMUM product ({1, ..., n-2, n, n+1}) or MINIMUM product ({1, ..., n-1, n+2})!
    dsp_cases = [
        (4, 1, "unique", "Easy"),     # sum = 11 -> {1,2,3,5}, prod = 30
        (5, 1, "unique", "Easy"),     # sum = 16 -> {1,2,3,4,6}, prod = 144
        (6, 1, "unique", "Medium"),   # sum = 22 -> {1,2,3,4,5,7}, prod = 840 (KMC Junior Cat A Q4!)
        (7, 1, "unique", "Medium"),   # sum = 29 -> {1,2,3,4,5,6,8}, prod = 5760
        (4, 2, "max", "Medium"),      # sum = 12 -> {1,2,4,5}=40 vs {1,2,3,6}=36 -> max 40
        (4, 2, "min", "Medium"),      # sum = 12 -> min 36
        (5, 2, "max", "Medium"),      # sum = 17 -> {1,2,3,5,6}=180 vs {1,2,3,4,7}=168 -> max 180
        (5, 2, "min", "Medium"),      # sum = 17 -> min 168
        (6, 2, "max", "Hard"),        # sum = 23 -> {1,2,3,4,6,7}=1008 vs {1,2,3,4,5,8}=960 -> max 1008
        (6, 2, "min", "Hard"),        # sum = 23 -> min 960
    ]
    for v_i, (n, extra, mode, diff) in enumerate(dsp_cases):
        min_s = n * (n + 1) // 2
        S = min_s + extra
        if extra == 1:
            nums = list(range(1, n)) + [n + 1]
            ans = math.prod(nums)
            fact_n = math.factorial(n)
            distractors = [fact_n, math.prod(range(1, n)) * (n + 2), ans + fact_n // n, max(6, ans - 12)]
            ask_en = "What is the **product** of these integers?"
            ask_ar = "ما **حاصل ضرب** هذه الأعداد؟"
            nums_str = ", ".join(str(x) for x in nums)
            steps_en = [
                f"The smallest possible sum of {m(n)} **distinct** positive integers is {m(f'1 + 2 + \\dots + {n} = {min_s}')}.",
                f"Since the actual sum is {m(f'{S} = {min_s} + 1')}, we must add just {m('1')} to one number without creating duplicates — only the largest number {m(n)} can increase to {m(n+1)}!",
                f"So the numbers must be {m(nums_str)}, and their product is {m(f'{nums_str.replace(', ', ' \\times ')} = {ans}')}.",
            ]
            steps_ar = [
                f"أصغر مجموع ممكن لـ {m(n)} أعداد صحيحة موجبة **مختلفة** هو {m(f'1 + 2 + \\dots + {n} = {min_s}')}.",
                f"بما أن المجموع المعطى هو {m(f'{S} = {min_s} + 1')}، يجب زيادة عدد واحد بمقدار {m('1')} دون تكرار أي عدد، فلا يمكن إلا زيادة أكبر عدد {m(n)} ليصبح {m(n+1)}!",
                f"إذن الأعداد هي حتماً {m(nums_str)}، وحاصل ضربها هو {m(ans)}.",
            ]
        else:
            set_a = list(range(1, n)) + [n + 2]            # min product
            set_b = list(range(1, n - 1)) + [n, n + 1]     # max product
            pa, pb = math.prod(set_a), math.prod(set_b)
            assert pb > pa
            ans = pb if mode == "max" else pa
            other = pa if mode == "max" else pb
            distractors = [other, math.factorial(n), ans + 24, max(12, ans - 24)]
            word_en = "**largest** possible product" if mode == "max" else "**smallest** possible product"
            word_ar = "**أكبر** حاصل ضرب ممكن" if mode == "max" else "**أصغر** حاصل ضرب ممكن"
            ask_en = f"What is the {word_en} of these {m(n)} integers?"
            ask_ar = f"ما {word_ar} لهذه الأعداد الـ {m(n)}؟"
            sa_s = ", ".join(str(x) for x in set_a)
            sb_s = ", ".join(str(x) for x in set_b)
            steps_en = [
                f"The minimum sum of {m(n)} distinct positive integers is {m(f'1 + 2 + \\dots + {n} = {min_s}')}, which is {m('2')} less than {m(S)}.",
                f"Without creating duplicates, we can distribute the extra {m('+2')} in only two ways: {m(f'\\{{{sa_s}\\}}')} (product {m(pa)}) or {m(f'\\{{{sb_s}\\}}')} (product {m(pb)}).",
                f"Therefore, the required answer is {m(ans)}.",
            ]
            steps_ar = [
                f"أصغر مجموع لـ {m(n)} أعداد موجبة مختلفة هو {m(f'1 + 2 + \\dots + {n} = {min_s}')}، أي أقل بـ {m('2')} من {m(S)}.",
                f"لتجنب تساوي أي عددين، لا يمكن توزيع الزيادة {m('+2')} إلا بطريقتين فقط: {m(f'\\{{{sa_s}\\}}')} (حاصل ضربها {m(pa)}) أو {m(f'\\{{{sb_s}\\}}')} (حاصل ضربها {m(pb)}).",
                f"إذن القيمة المطلوبة هي {m(ans)}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_dsp_{v_i}")
        q_en = f"Suppose {m(n)} **distinct** positive integers have a sum equal to {m(S)}. {ask_en}"
        q_ar = f"مجموع {m(n)} أعداد صحيحة موجبة **مختلفة** يساوي {m(S)}. {ask_ar}"
        h_en = f"Compare the given sum {S} with the smallest possible sum 1 + 2 + ... + {n} = {min_s}!"
        h_ar = f"قارن المجموع المعطى {S} بأصغر مجموع ممكن لأعداد موجبة مختلفة وهو 1 + 2 + ... + {n} = {min_s}!"
        s_en = explain_en("Whenever distinct positive integers have a sum very close to \\( 1 + 2 + \\dots + n \\), almost all the numbers are forced!", steps_en, f"Check that all {m(n)} numbers are positive, distinct, and sum to {m(S)}.")
        s_ar = explain_ar("عندما يكون مجموع أعداد صحيحة موجبة مختلفة قريباً جداً من \\( 1 + 2 + \\dots + n \\)، فإن الأعداد تتحدد فوراً!", steps_ar, f"تحقق أن جميع الأعداد الـ {m(n)} موجبة ومختلفة ومجموعها {m(S)} بالضبط.")
        push(diff, "kmc_g89_distinct_sum_product", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 3. Modular number machine cycle (KMC Junior Cat A Q5!) (10 Qs)
    # ------------------------------------------------------------------
    mach_cases = [
        # (a, b, M, x0, steps_or_mode)
        (2, 0, 7, 1, 50, "Easy"),        # 1 -> 2 -> 4 -> 1 (cycle 3)
        (2, 1, 7, 0, 40, "Easy"),        # 0 -> 1 -> 3 -> 0 (cycle 3)
        (2, 0, 9, 1, 100, "Medium"),     # 1 -> 2 -> 4 -> 8 -> 7 -> 5 -> 1 (cycle 6)
        (3, 1, 10, 2, 75, "Medium"),     # 2 -> 7 -> 2 -> 7 (cycle 2)
        (2, 3, 11, 1, 65, "Medium"),     # 1->5->2->7->6->4->0->3->9->10->1 (cycle 10)
        (3, 0, 13, 1, "return", "Easy"),   # 1 -> 3 -> 9 -> 1 (3 steps)
        (2, 0, 15, 1, "return", "Easy"),   # 1 -> 2 -> 4 -> 8 -> 1 (4 steps)
        (2, 1, 13, 1, 2026, "Hard"),
        (3, 2, 11, 1, 2025, "Hard"),
        (4, 1, 9, 2, 2026, "Hard"),
    ]
    for v_i, (a, b, M, x0, mode, diff) in enumerate(mach_cases):
        # Trace orbit from x0
        orbit = [x0]
        cur = (a * x0 + b) % M
        while cur not in orbit:
            orbit.append(cur)
            cur = (a * cur + b) % M
        assert cur == x0, f"Orbit did not return directly to x0: {orbit} -> {cur}"
        cyc_len = len(orbit)
        rule_tex = f"{a}n" + (f" + {b}" if b > 0 else "")
        cyc_str = " \\to ".join(str(v) for v in orbit + [x0])
        if mode == "return":
            ans = cyc_len
            distractors = [cyc_len + 1, cyc_len + 2, max(2, cyc_len - 1), M - 1, cyc_len * 2]
            q_en = (
                f"A digital machine takes a number {m('n')}, computes {m(rule_tex)}, and displays the **remainder when divided by {m(M)}**. "
                f"Starting with {m(f'n = {x0}')} and feeding each output back into the machine, what is the **smallest positive number of steps** until {m(x0)} appears again?"
            )
            q_ar = (
                f"تأخذ آلة رقمية العدد {m('n')}، فتحسب {m(rule_tex)} وتعرض **باقي قسمته على {m(M)}**. "
                f"إذا بدأنا بالعدد {m(f'n = {x0}')} وأدخلنا كل مخرج مجدداً في الآلة، فما **أصغر عدد موجب من الخطوات** حتى يظهر العدد {m(x0)} مرة أخرى؟"
            )
            steps_en = [
                f"Compute step by step (taking remainders mod {m(M)}): {m(cyc_str)}.",
                f"Counting the arrows, the machine returns to {m(x0)} after exactly {m(ans)} steps.",
            ]
            steps_ar = [
                f"نحسب خطوة بخطوة (مع أخذ باقي القسمة على {m(M)}): {m(cyc_str)}.",
                f"بعدّ الأسهم نجد أن الآلة تعود إلى {m(x0)} بعد {m(ans)} خطوات بالضبط.",
            ]
        else:
            N_steps = int(mode)
            r = N_steps % cyc_len
            ans = orbit[r]
            distractors = [o for o in orbit if o != ans] + [(ans + 1) % M, (ans + 2) % M, M - 1]
            q_en = (
                f"A number machine replaces {m('n')} with the remainder when {m(rule_tex)} is divided by {m(M)}. "
                f"If the machine starts with {m(x0)}, what number is displayed after **{m(N_steps)} steps**?"
            )
            q_ar = (
                f"تستبدل آلة عددية العدد {m('n')} بباقي قسمة {m(rule_tex)} على {m(M)}. "
                f"إذا بدأت الآلة بالعدد {m(x0)}، فما العدد الذي سيظهر بعد **{m(N_steps)} خطوة**؟"
            )
            steps_en = [
                f"Trace the first few steps to find the repeating cycle: {m(cyc_str)}. The cycle repeats every **{m(cyc_len)} steps**!",
                f"Divide {m(N_steps)} by the cycle length {m(cyc_len)}: {m(f'{N_steps} = {N_steps // cyc_len} \\times {cyc_len} + {r}')}.",
                f"So step {m(N_steps)} matches step {m(r)} in the cycle, which is {m(ans)}.",
            ]
            steps_ar = [
                f"نتتبع الخطوات الأولى لاكتشاف الدورة المتكررة: {m(cyc_str)}. الدورة تتكرر كل **{m(cyc_len)} خطوات**!",
                f"نقسم {m(N_steps)} على طول الدورة {m(cyc_len)}: {m(f'{N_steps} = {N_steps // cyc_len} \\times {cyc_len} + {r}')}.",
                f"إذن الخطوة {m(N_steps)} تطابق الخطوة رقم {m(r)} في الدورة، وهي {m(ans)}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_mach_{v_i}")
        h_en = "Never compute hundreds of steps! Write out the first few outputs until the starting number repeats, then use the cycle length."
        h_ar = "لا تحسب مئات الخطوات يدوياً! اكتب المخرجات الأولى فقط حتى يتكرر عدد البداية، ثم استخدم طول الدورة."
        s_en = explain_en("Because there are only finitely many remainders modulo \\( M \\), the machine's outputs quickly lock into a short repeating loop.", steps_en, f"Check step 1: \\( {a}({x0}) + {b} = {a*x0+b} \\), which leaves remainder \\( {orbit[1]} \\) upon division by \\( {M} \\).")
        s_ar = explain_ar("لأن بواقي القسمة على \\( M \\) محدودة العدد، فإن مخرجات الآلة تدخل سريعاً في دورة قصيرة متكررة.", steps_ar, f"تحقق من الخطوة 1: باقي قسمة \\( {a}({x0}) + {b} = {a*x0+b} \\) على \\( {M} \\) هو \\( {orbit[1]} \\).")
        push(diff, "kmc_g89_mod_machine_cycle", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 4. Divisor rainbow pairing d_i * d_{k+1-i} = N (10 Qs)
    # ------------------------------------------------------------------
    div_cases = [
        (36, 2, "Easy"),
        (48, 3, "Easy"),
        (60, 3, "Easy"),
        (72, 4, "Medium"),
        (84, 3, "Medium"),
        (90, 4, "Medium"),
        (108, 3, "Medium"),
        (120, 5, "Medium"),
        (144, 4, "Hard"),
        (180, 5, "Hard"),
    ]
    for v_i, (N, idx_pair, diff) in enumerate(div_cases):
        divs = [d for d in range(1, N + 1) if N % d == 0]
        k = len(divs)
        d_left = divs[idx_pair - 1]
        d_right = divs[k - idx_pair]
        assert d_left * d_right == N and d_left < d_right
        # Alternate asking for N (given d_left and d_right) vs asking for d_2 + d_{k-1}
        if v_i % 2 == 0:
            ans = N
            distractors = [d_left * d_right // 2, (d_left + 1) * d_right, N + d_right, N - d_left]
            q_en = (
                f"All {m(k)} positive divisors of a positive integer {m('N')} are written in increasing order: "
                f"{m(f'1 = d_1 < d_2 < \\dots < d_{{{k}}} = N')}. If {m(f'd_{{{idx_pair}}} = {d_left}')} and {m(f'd_{{{k + 1 - idx_pair}}} = {d_right}')}, what is {m('N')}?"
            )
            q_ar = (
                f"كُتبت جميع القواسم الموجبة وعددها {m(k)} لعدد صحيح موجب {m('N')} بترتيب تصاعدي: "
                f"{m(f'1 = d_1 < d_2 < \\dots < d_{{{k}}} = N')}. إذا كان {m(f'd_{{{idx_pair}}} = {d_left}')} و{m(f'd_{{{k + 1 - idx_pair}}} = {d_right}')}، فما قيمة {m('N')}؟"
            )
            steps_en = [
                f"Divisors pair up symmetrically from the ends: {m(f'd_1 d_{{{k}}} = d_2 d_{{{k-1}}} = \\dots = d_{{{idx_pair}}} d_{{{k+1-idx_pair}}} = N')}.",
                f"Notice the indices {m(idx_pair)} and {m(k + 1 - idx_pair)} are symmetric from the two ends ({m(f'{idx_pair} + {k+1-idx_pair} = {k+1}')}).",
                f"Multiply the symmetric pair: {m(f'N = {d_left} \\times {d_right} = {N}')}.",
            ]
            steps_ar = [
                f"تقترن قواسم أي عدد بشكل متماثل من الطرفين: {m(f'd_1 d_{{{k}}} = d_2 d_{{{k-1}}} = \\dots = d_{{{idx_pair}}} d_{{{k+1-idx_pair}}} = N')}.",
                f"نلاحظ أن الرتبتين {m(idx_pair)} و{m(k + 1 - idx_pair)} متماثلتان من البداية والنهاية ({m(f'{idx_pair} + {k+1-idx_pair} = {k+1}')}).",
                f"نضرب القاسمين المتناظرين: {m(f'N = {d_left} \\times {d_right} = {N}')}.",
            ]
        else:
            ans = d_right
            distractors = [N // (d_left + 1) if N % (d_left + 1) == 0 else d_right + 4, d_right - d_left, N // 2, d_right + 6]
            q_en = (
                f"The {m(k)} positive divisors of {m(N)} are listed in increasing order: "
                f"{m(f'd_1 < d_2 < \\dots < d_{{{k}}}')}. Given that {m(f'd_{{{idx_pair}}} = {d_left}')}, what is the value of {m(f'd_{{{k + 1 - idx_pair}}}')}?"
            )
            q_ar = (
                f"رُتِّبت القواسم الموجبة للعدد {m(N)} وعددها {m(k)} ترتيباً تصاعدياً: "
                f"{m(f'd_1 < d_2 < \\dots < d_{{{k}}}')}. إذا علمت أن {m(f'd_{{{idx_pair}}} = {d_left}')}، فما قيمة {m(f'd_{{{k + 1 - idx_pair}}}')}؟"
            )
            steps_en = [
                f"In an ordered list of {m(k)} divisors, the {m(f'{idx_pair}\\text{{th}}')} from the start and the {m(f'{idx_pair}\\text{{th}}')} from the end ({m(f'd_{{{k+1-idx_pair}}}')}) multiply to {m(N)}.",
                f"Divide {m(N)} by {m(d_left)}: {m(f'd_{{{k+1-idx_pair}}} = \\frac{{{N}}}{{{d_left}}} = {ans}')}.",
            ]
            steps_ar = [
                f"في قائمة القواسم المرتبة وعددها {m(k)}، حاصل ضرب القاسم رقم {m(idx_pair)} من البداية والقاسم المناظر له من النهاية ({m(f'd_{{{k+1-idx_pair}}}')}) يساوي {m(N)}.",
                f"نقسم {m(N)} على {m(d_left)}: {m(f'd_{{{k+1-idx_pair}}} = \\frac{{{N}}}{{{d_left}}} = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_div_{v_i}")
        h_en = "Rainbow divisor rule: the 1st and last divisors multiply to N, the 2nd and second-to-last multiply to N, and in general d_i × d_{k+1−i} = N!"
        h_ar = "قاعدة أقواس القواسم: حاصل ضرب القاسم الأول والأخير يساوي N، والثاني وما قبل الأخير يساوي N، وعموماً d_i × d_{k+1−i} = N!"
        s_en = explain_en("Every divisor \\( d \\) of \\( N \\) pairs up with \\( N/d \\) at the opposite position in the sorted divisor list.", steps_en, f"Full sorted divisors of {m(N)}: {m(', '.join(str(x) for x in divs))}.")
        s_ar = explain_ar("كل قاسم \\( d \\) للعدد \\( N \\) يقترن بالقاسم \\( N/d \\) في الموقع المناظر له من الطرف الآخر لقائمة القواسم.", steps_ar, f"قائمة قواسم {m(N)} كاملة للتحقق: {m(', '.join(str(x) for x in divs))}.")
        push(diff, "kmc_g89_divisor_pairing", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 5. Euclidean division remainder -> count valid divisors d (10 Qs)
    # ------------------------------------------------------------------
    rem_cases = [
        (40, 4, "Easy"),      # d | 36, d > 4 -> 6,9,12,18,36 -> 5
        (53, 5, "Easy"),      # d | 48, d > 5 -> 6,8,12,16,24,48 -> 6
        (67, 7, "Easy"),      # d | 60, d > 7 -> 10,12,15,20,30,60 -> 6
        (80, 8, "Medium"),    # d | 72, d > 8 -> 9,12,18,24,36,72 -> 6
        (95, 5, "Medium"),    # d | 90, d > 5 -> 6,9,10,15,18,30,45,90 -> 8
        (106, 6, "Medium"),   # d | 100, d > 6 -> 10,20,25,50,100 -> 5
        (115, 7, "Medium"),   # d | 108, d > 7 -> 9,12,18,27,36,54,108 -> 7
        (130, 10, "Medium"),  # d | 120, d > 10 -> 12,15,20,24,30,40,60,120 -> 8
        (155, 11, "Hard"),    # d | 144, d > 11 -> 12,16,18,24,36,48,72,144 -> 8
        (192, 12, "Hard"),    # d | 180, d > 12 -> 15,18,20,30,36,45,60,90,180 -> 9
    ]
    for v_i, (A, r, diff) in enumerate(rem_cases):
        M = A - r
        all_divs = [d for d in range(1, M + 1) if M % d == 0]
        valid = [d for d in all_divs if d > r]
        # Verify directly by A % d == r
        assert valid == [d for d in range(1, A + 5) if A % d == r]
        ans = len(valid)
        distractors = [len(all_divs), ans + 1, max(1, ans - 1), ans + 2, len([d for d in all_divs if d >= r]) + 2]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_rem_{v_i}")
        all_str = ", ".join(str(x) for x in all_divs)
        val_str = ", ".join(str(x) for x in valid)
        q_en = (
            f"When {m(A)} is divided by a positive integer {m('d')}, the remainder is {m(r)}. "
            f"How many different positive integers {m('d')} have this property?"
        )
        q_ar = (
            f"عند قسمة العدد {m(A)} على عدد صحيح موجب {m('d')}، يكون الباقي {m(r)}. "
            f"كم عدداً صحيحاً موجباً مختلفاً {m('d')} يحقق هذه الخاصية؟"
        )
        h_en = f"Two conditions must hold: (1) d divides ({A} − {r}) = {M}, AND (2) the divisor d must be strictly greater than the remainder {r}!"
        h_ar = f"يجب تحقق شرطين معاً: (1) أن يقسم d الفرق ({A} − {r}) = {M}، و(2) أن يكون المقسوم عليه d أكبر تماماً من الباقي {r}!"
        s_en = explain_en(
            f"Saying '{m(A)} leaves remainder {m(r)} when divided by {m('d')}' means {m(f'{A} = q \\cdot d + {r}')} **with {m(f'd > {r}')}**!",
            [
                f"Subtract {m(r)}: {m(f'q \\cdot d = {A} - {r} = {M}')}, so {m('d')} must be a positive divisor of {m(M)}.",
                f"List all divisors of {m(M)}: {m(all_str)} ({m(len(all_divs))} divisors in total).",
                f"Keep ONLY those strictly greater than the remainder {m(r)}: {m(val_str)}, which gives **{m(ans)}** valid values.",
            ],
            f"Trap check: any divisor {m(f'd \\le {r}')} would leave a remainder smaller than {m(r)}, not {m(r)}!",
        )
        s_ar = explain_ar(
            f"كون باقي قسمة {m(A)} على {m('d')} يساوي {m(r)} يعني أن {m(f'{A} = q \\cdot d + {r}')} **بشرط أساسي أن يكون المقسوم عليه أكبر من الباقي ({m(f'd > {r}')})**!",
            [
                f"نطرح الباقي {m(r)}: {m(f'q \\cdot d = {A} - {r} = {M}')}، إذن {m('d')} قاسم موجب للعدد {m(M)}.",
                f"جميع قواسم {m(M)} هي: {m(all_str)}.",
                f"نختار فقط القواسم الأكبر تماماً من {m(r)}: {m(val_str)}، وعددها **{m(ans)}**.",
            ],
            f"تنبيه مهم: أي قاسم {m(f'd \\le {r}')} يعطي باقياً أصغر من {m(r)} ولا يحقق الشرط!",
        )
        push(diff, "kmc_g89_euclidean_remainder_divisors", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. Concatenated number stream k-th digit (10 Qs)
    # ------------------------------------------------------------------
    cat_cases = [
        ("all", 35, "Easy"),
        ("all", 60, "Easy"),
        ("all", 100, "Medium"),
        ("all", 195, "Hard"),
        ("even", 30, "Easy"),
        ("even", 55, "Medium"),
        ("even", 95, "Medium"),
        ("odd", 32, "Medium"),
        ("odd", 70, "Medium"),
        ("odd", 120, "Hard"),
    ]
    for v_i, (kind, k_pos, diff) in enumerate(cat_cases):
        if kind == "all":
            nums = list(range(1, 300))
            desc_en = "all positive integers are written side by side without spaces: \\( 123456789101112\\dots \\)"
            desc_ar = "كُتبت جميع الأعداد الصحيحة الموجبة متلاصقة دون مسافات: \\( 123456789101112\\dots \\)"
            c1 = 9
            b2_start = 10
            step_n = 1
        elif kind == "even":
            nums = list(range(2, 600, 2))
            desc_en = "all positive **even** integers are written side by side: \\( 246810121416\\dots \\)"
            desc_ar = "كُتبت جميع الأعداد الصحيحة الموجبة **الزوجية** متلاصقة: \\( 246810121416\\dots \\)"
            c1 = 4
            b2_start = 10
            step_n = 2
        else:
            nums = list(range(1, 600, 2))
            desc_en = "all positive **odd** integers are written side by side: \\( 13579111315\\dots \\)"
            desc_ar = "كُتبت جميع الأعداد الصحيحة الموجبة **الفردية** متلاصقة: \\( 13579111315\\dots \\)"
            c1 = 5
            b2_start = 11
            step_n = 2

        stream = "".join(str(x) for x in nums)
        ans = int(stream[k_pos - 1])
        # Find exact number containing k_pos
        pos = 0
        hit_num, hit_d_idx = 0, 0
        for x in nums:
            sx = str(x)
            if pos + len(sx) >= k_pos:
                hit_num = x
                hit_d_idx = k_pos - pos - 1
                break
            pos += len(sx)

        distractors = [(ans + 1) % 10, (ans + 9) % 10, int(stream[k_pos]), int(stream[max(0, k_pos - 2)]), (ans + 2) % 10]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_cat_{v_i}")
        q_en = f"Suppose {desc_en}. What is the {m(f'{k_pos}\\text{{th}}')} digit from the left?"
        q_ar = f"افترض أنه {desc_ar}. ما الرقم الذي يقع في الخانة رقم {m(k_pos)} من جهة اليسار (بداية السلسلة)؟"
        h_en = "Count how many digits are used by 1-digit numbers first, subtract that from the position, then divide the remaining positions by 2 (for 2-digit numbers)!"
        h_ar = "احسب أولاً عدد الخانات التي تشغلها الأعداد المكونة من رقم واحد، واطرحها من الرتبة المطلوبة، ثم اقسم الباقي على 2 (للأعداد المكونة من رقمين)!"
        rem_after_1 = k_pos - c1
        s_en = explain_en(
            "Group the stream by **number of digits**: 1-digit numbers contribute 1 digit each, 2-digit numbers contribute 2 digits each, and 3-digit numbers contribute 3 digits each.",
            [
                f"1-digit numbers in this list use **{m(c1)}** digits, leaving {m(f'{k_pos} - {c1} = {rem_after_1}')} digit positions still to go.",
                f"Counting through the 2-digit numbers (and 3-digit if needed) starting at {m(b2_start)} in steps of {m(step_n)}, position {m(k_pos)} lands on digit #{m(hit_d_idx + 1)} of the number **{m(hit_num)}**.",
                f"Reading digit #{m(hit_d_idx + 1)} of {m(hit_num)} gives **{m(ans)}**.",
            ],
            f"Neighboring slice around position {m(k_pos)}: `...{stream[max(0, k_pos-4):k_pos+3]}...` where position {m(k_pos)} is `{ans}`.",
        )
        s_ar = explain_ar(
            "نقسّم السلسلة حسب **عدد خانات كل عدد**: الأعداد ذات الرقم الواحد تشغل خانة واحدة، وذات الرقمين تشغل خانتين، وذات الثلاثة أرقام تشغل 3 خانات.",
            [
                f"الأعداد المكونة من رقم واحد في هذه السلسلة تشغل **{m(c1)}** خانات، فيتبقى لدينا {m(f'{k_pos} - {c1} = {rem_after_1}')} خانة.",
                f"بالمتابعة عبر الأعداد المكونة من رقمين (فأكثر) بدءاً من {m(b2_start)} بزيادة {m(step_n)} في كل مرة، نجد أن الخانة رقم {m(k_pos)} تقع في الرقم رقم {m(hit_d_idx + 1)} من العدد **{m(hit_num)}**.",
                f"الرقم المطلوب داخل العدد {m(hit_num)} هو **{m(ans)}**.",
            ],
            f"تحقق من المقطع المحيط بالخانة {m(k_pos)} للتأكد أن الرقم هو {m(ans)} بالضبط.",
        )
        push(diff, "kmc_g89_concat_digit_stream", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 7. Units digit (last digit) of powers a^m + b^n (10 Qs)
    # ------------------------------------------------------------------
    ud_cases = [
        (2, 50, 3, 25, "+", "Easy"),
        (7, 41, 4, 20, "+", "Easy"),
        (3, 102, 8, 53, "+", "Medium"),
        (2, 2025, 7, 2026, "+", "Medium"),
        (3, 2026, 9, 2025, "+", "Medium"),
        (7, 103, 3, 101, "*", "Medium"),
        (8, 2026, 7, 2025, "*", "Medium"),
        (2, 2026, 3, 2026, "+", "Hard"),
        (7, 2027, 8, 2027, "+", "Hard"),
        (3, 999, 7, 999, "*", "Hard"),
    ]
    cycles_map = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }
    for v_i, (a, e1, b, e2, op, diff) in enumerate(ud_cases):
        u1 = pow(a, e1, 10)
        u2 = pow(b, e2, 10)
        ans = (u1 + u2) % 10 if op == "+" else (u1 * u2) % 10
        expr_tex = f"{a}^{{{e1}}} + {b}^{{{e2}}}" if op == "+" else f"{a}^{{{e1}}} \\times {b}^{{{e2}}}"
        c1_str = ", ".join(str(x) for x in cycles_map[a])
        c2_str = ", ".join(str(x) for x in cycles_map[b])
        distractors = [(ans + 2) % 10, (ans + 4) % 10, (ans + 6) % 10, (ans + 8) % 10, (ans + 1) % 10]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_ud_{v_i}")
        q_en = f"What is the **units digit** (ones digit) of {m(expr_tex)}?"
        q_ar = f"ما **رقم الآحاد** للعدد {m(expr_tex)}؟"
        h_en = "Only the units digits matter! Find the repeating cycle of units digits for powers of each base (length 2 or 4)."
        h_ar = "رقم الآحاد يعتمد فقط على دورة آحاد القوى لكل أساس (طول الدورة 2 أو 4)!"
        comb_eq = f"{u1} + {u2} = {u1+u2}" if op == "+" else f"{u1} \\times {u2} = {u1*u2}"
        s_en = explain_en(
            "Powers of any integer have units digits that repeat in a short cycle of length 1, 2, or 4.",
            [
                f"Units digits of powers of {m(a)} repeat in the cycle {m(f'[{c1_str}]')} (length {m(len(cycles_map[a]))}), so {m(f'{a}^{{{e1}}}')} ends in **{m(u1)}**.",
                f"Units digits of powers of {m(b)} repeat in the cycle {m(f'[{c2_str}]')} (length {m(len(cycles_map[b]))}), so {m(f'{b}^{{{e2}}}')} ends in **{m(u2)}**.",
                f"Combine the units digits: {m(comb_eq)}, whose units digit is **{m(ans)}**.",
            ],
            f"Quick check: divide each exponent by its cycle length and look up the remainder position!",
        )
        s_ar = explain_ar(
            "أرقام آحاد قوى أي عدد صحيح تتكرر في دورة قصيرة طولها 1 أو 2 أو 4.",
            [
                f"دورة آحاد قوى العدد {m(a)} هي {m(f'[{c1_str}]')} (طولها {m(len(cycles_map[a]))})، لذا ينتهي {m(f'{a}^{{{e1}}}')} بالرقم **{m(u1)}**.",
                f"دورة آحاد قوى العدد {m(b)} هي {m(f'[{c2_str}]')} (طولها {m(len(cycles_map[b]))})، لذا ينتهي {m(f'{b}^{{{e2}}}')} بالرقم **{m(u2)}**.",
                f"نحسب للآحاد: {m(comb_eq)}، فيكون رقم الآحاد الناتج هو **{m(ans)}**.",
            ],
            f"تحقق سريع: نقسم كل أس على طول دورته ونأخذ العنصر الموافق للباقي!",
        )
        push(diff, "kmc_g89_units_digit_powers", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 8. Combined divisibility by 72, 88, or 99 (two missing digits) (10 Qs)
    # ------------------------------------------------------------------
    # Patterns where x is first digit (1..9) or middle digit (0..9) and y is last digit (0..9)
    div2_cases = [
        (["A", "5", "1", "B"], 72, "Easy"),
        (["A", "3", "7", "B"], 72, "Easy"),
        (["A", "1", "3", "B"], 72, "Medium"),
        (["A", "2", "5", "B"], 72, "Medium"),
        (["A", "4", "7", "B"], 72, "Medium"),
        (["4", "A", "5", "B"], 88, "Medium"),
        (["7", "A", "1", "B"], 88, "Medium"),
        (["A", "6", "2", "B"], 99, "Medium"),
        (["A", "4", "3", "B"], 99, "Hard"),
        (["A", "6", "7", "9", "B"], 72, "Hard"),
    ]
    for v_i, (tpl, div_by, diff) in enumerate(div2_cases):
        sols = []
        a_start = 1 if tpl[0] == "A" else 0
        for da in range(a_start, 10):
            for db in range(0, 10):
                s_num = "".join(str(da) if c == "A" else (str(db) if c == "B" else c) for c in tpl)
                if int(s_num) % div_by == 0:
                    sols.append((da, db, int(s_num)))
        assert len(sols) == 1, f"Expected unique solution for {tpl} mod {div_by}, got {sols}"
        da, db, full_n = sols[0]
        ans = da + db
        svg = svg_number_strip(tpl)
        distractors = [ans + 1, max(1, ans - 1), ans + 2, abs(da - db), ans + 3]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_d72_{v_i}")
        n_dig = len(tpl)
        str_pat = "".join(tpl)
        if div_by == 72:
            f1, f2 = 8, 9
            r1_en = f"Divisibility by {m(8)} depends ONLY on the last three digits, forcing {m(f'B = {db}')}."
            r2_en = f"Divisibility by {m(9)} requires the sum of all digits to be a multiple of {m(9)}, forcing {m(f'A = {da}')}."
            r1_ar = f"قابلية القسمة على {m(8)} تعتمد فقط على آخر ثلاثة أرقام من اليمين، مما يحدد فوراً أن {m(f'B = {db}')}."
            r2_ar = f"قابلية القسمة على {m(9)} تشترط أن يقبل مجموع جميع الأرقام القسمة على {m(9)}، مما يحدد {m(f'A = {da}')}."
        elif div_by == 88:
            f1, f2 = 8, 11
            r1_en = f"Divisibility by {m(8)} on the last three digits determines {m(f'B = {db}')}."
            r2_en = f"Divisibility by {m(11)} (alternating sum of digits divisible by {m(11)}) gives {m(f'A = {da}')}."
            r1_ar = f"قابلية القسمة على {m(8)} لآخر ثلاثة أرقام تحدد {m(f'B = {db}')}."
            r2_ar = f"قابلية القسمة على {m(11)} (المجموع المتناوب للأرقام يقبل القسمة على {m(11)}) تعطي {m(f'A = {da}')}."
        else:
            f1, f2 = 9, 11
            r1_en = f"Using divisibility by {m(9)} (sum of digits is a multiple of {m(9)}) and {m(11)} (alternating sum of digits is a multiple of {m(11)})."
            r2_en = f"Solving both conditions for digits {m('0..9')} uniquely yields {m(f'A = {da}')} and {m(f'B = {db}')}."
            r1_ar = f"نطبق شرط القسمة على {m(9)} (مجموع الأرقام مضاعف لـ {m(9)}) وشرط القسمة على {m(11)} (المجموع المتناوب مضاعف لـ {m(11)})."
            r2_ar = f"بحل الشرطين معاً للأرقام من {m('0')} إلى {m('9')} نجد أن {m(f'A = {da}')} و{m(f'B = {db}')}."

        q_en = (
            f"The {m(n_dig)}-digit number {m(f'\\overline{{{str_pat}}}')} shown on the digit cards is divisible by {m(div_by)}. "
            f"What is the sum of the two missing digits {m('A + B')}?"
        )
        q_ar = (
            f"العدد المكون من {m(n_dig)} خانات {m(f'\\overline{{{str_pat}}}')} الموضح في البطاقات يقبل القسمة على {m(div_by)}. "
            f"ما مجموع الرقمين المفقودين {m('A + B')}؟"
        )
        h_en = f"Split {div_by} into two coprime factors: {f1} × {f2} = {div_by}! Check divisibility by {f1} and by {f2} separately."
        h_ar = f"حلّل {div_by} إلى عاملين أوليين نسبياً: {f1} × {f2} = {div_by}! ثم طبّق قاعدة القسمة على {f1} وقاعدة القسمة على {f2}."
        s_en = explain_en(
            f"Since {m(f'\\gcd({f1}, {f2}) = 1')} and {m(f'{f1} \\times {f2} = {div_by}')}, a number is divisible by {m(div_by)} if and only if it is divisible by **both {m(f1)} and {m(f2)}**.",
            [
                r1_en,
                r2_en,
                f"Add the two digits: {m(f'A + B = {da} + {db} = {ans}')}.",
            ],
            f"Check: {m(f'{full_n} \\div {div_by} = {full_n // div_by}')} with remainder {m(0)}!",
        )
        s_ar = explain_ar(
            f"بما أن {m(f'\\gcd({f1}, {f2}) = 1')} و{m(f'{f1} \\times {f2} = {div_by}')}، فإن العدد يقبل القسمة على {m(div_by)} إذا وفقط إذا قبل القسمة على **{m(f1)} و{m(f2)} معاً**.",
            [
                r1_ar,
                r2_ar,
                f"نجمع الرقمين: {m(f'A + B = {da} + {db} = {ans}')}.",
            ],
            f"تحقق: {m(f'{full_n} \\div {div_by} = {full_n // div_by}')} بدون أي باقٍ!",
        )
        push(diff, "kmc_g89_divisibility_8_9_11", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 9. GCD & LCM product and minimum-sum puzzles (10 Qs)
    # ------------------------------------------------------------------
    gl_cases = [
        (6, 72, "other", 18, "Easy"),      # b = 6*72/18 = 24
        (8, 120, "other", 24, "Easy"),     # b = 40
        (12, 180, "other", 36, "Easy"),    # b = 60
        (5, 60, "min_sum", 0, "Medium"),   # L/g = 12 -> coprime (3,4) -> 5*(3+4)=35
        (6, 120, "min_sum", 0, "Medium"),  # L/g = 20 -> coprime (4,5) -> 6*9 = 54
        (4, 140, "min_sum", 0, "Medium"),  # L/g = 35 -> coprime (5,7) -> 4*12 = 48
        (7, 210, "min_sum", 0, "Medium"),  # L/g = 30 -> coprime (5,6) -> 7*11 = 77
        (3, 180, "count_ord", 0, "Hard"),  # L/g = 60 = 2^2*3*5 (3 distinct primes -> 2^3 = 8 ordered pairs)
        (5, 210, "count_ord", 0, "Hard"),  # L/g = 42 = 2*3*7 (3 primes -> 8 ordered pairs)
        (9, 540, "min_sum", 0, "Hard"),    # L/g = 60 -> coprime (4, 15)? wait: 3 and 20 (23), 4 and 15 (19), 5 and 12 (17)! 9*17 = 153!
    ]
    for v_i, (g, L, mode, given_a, diff) in enumerate(gl_cases):
        assert L % g == 0
        K = L // g
        if mode == "other":
            ans = (g * L) // given_a
            assert math.gcd(given_a, ans) == g and math.lcm(given_a, ans) == L
            distractors = [L // given_a, ans + g, max(g, ans - g), given_a + g]
            q_en = f"Two positive integers have greatest common divisor {m(g)} and least common multiple {m(L)}. If one of the integers is {m(given_a)}, what is the other integer?"
            q_ar = f"عددان صحيحان موجبان قاسمهما المشترك الأكبر {m(g)} ومضاعفهما المشترك الأصغر {m(L)}. إذا كان أحد العددين هو {m(given_a)}، فما العدد الآخر؟"
            steps_en = [
                f"Use the golden identity: {m('\\gcd(a, b) \\times \\operatorname{lcm}(a, b) = a \\times b')}.",
                f"Substitute the known values: {m(f'{g} \\times {L} = {given_a} \\times b \\implies {g*L} = {given_a}b')}.",
                f"Divide by {m(given_a)}: {m(f'b = \\frac{{{g*L}}}{{{given_a}}} = {ans}')}.",
            ]
            steps_ar = [
                f"نستخدم المتطابقة الذهبية: {m('\\gcd(a, b) \\times \\operatorname{lcm}(a, b) = a \\times b')}.",
                f"نعوض بالقيم المعطاة: {m(f'{g} \\times {L} = {given_a} \\times b \\implies {g*L} = {given_a}b')}.",
                f"نقسم على {m(given_a)}: {m(f'b = \\frac{{{g*L}}}{{{given_a}}} = {ans}')}.",
            ]
        elif mode == "min_sum":
            cop_pairs = [(u, K // u) for u in range(1, int(math.isqrt(K)) + 1) if K % u == 0 and math.gcd(u, K // u) == 1]
            best_u, best_v = min(cop_pairs, key=lambda p: p[0] + p[1])
            ans = g * (best_u + best_v)
            distractors = [g + L, g * (1 + K), ans + 2 * g, max(2 * g, ans - g)]
            q_en = f"Two positive integers {m('a')} and {m('b')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}. What is the **smallest possible value** of {m('a + b')}?"
            q_ar = f"عددان صحيحان موجبان {m('a')} و{m('b')} يحققان {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}. ما **أصغر قيمة ممكنة** للمجموع {m('a + b')}؟"
            steps_en = [
                f"Write {m(f'a = {g}u')} and {m(f'b = {g}v')} where {m('\\gcd(u, v) = 1')}. Then {m(f'\\operatorname{{lcm}}(a,b) = {g}uv = {L} \\implies uv = {K}')}.",
                f"To minimize {m(f'a + b = {g}(u + v)')}, choose coprime factors {m('u, v')} of {m(K)} as close together as possible: {m(f'u = {best_u}, v = {best_v}')}.",
                f"Compute the sum: {m(f'{g} \\times ({best_u} + {best_v}) = {ans}')}.",
            ]
            steps_ar = [
                f"نضع {m(f'a = {g}u')} و{m(f'b = {g}v')} حيث {m('\\gcd(u, v) = 1')}، فيكون {m(f'{g}uv = {L} \\implies uv = {K}')}.",
                f"لتصغير المجموع {m(f'a + b = {g}(u + v)')} نختار عاملين أوليين نسبياً للعدد {m(K)} أقرب ما يمكن لبعضهما: {m(f'u = {best_u}, v = {best_v}')}.",
                f"نحسب المجموع الأصغر: {m(f'{g} \\times ({best_u} + {best_v}) = {ans}')}.",
            ]
        else:
            ord_pairs = [(u, K // u) for u in range(1, K + 1) if K % u == 0 and math.gcd(u, K // u) == 1]
            ans = len(ord_pairs)
            all_div_cnt = sum(1 for u in range(1, K + 1) if K % u == 0)
            distractors = [ans // 2, all_div_cnt, ans + 2, ans - 2]
            q_en = f"How many **ordered pairs** of positive integers {m('(a, b)')} satisfy {m(f'\\gcd(a, b) = {g}')} and {m(f'\\operatorname{{lcm}}(a, b) = {L}')}?"
            q_ar = f"كم **زوجاً مرتباً** من الأعداد الصحيحة الموجبة {m('(a, b)')} يحقق {m(f'\\gcd(a, b) = {g}')} و{m(f'\\operatorname{{lcm}}(a, b) = {L}')}؟"
            steps_en = [
                f"Write {m(f'a = {g}u, b = {g}v')} with {m('\\gcd(u, v) = 1')}; then {m(f'uv = {L} \\div {g} = {K}')}.",
                f"In {m('u \\times v = ' + str(K))} with {m('\\gcd(u,v)=1')}, each prime power factor of {m(K)} must go entirely into {m('u')} OR entirely into {m('v')}.",
                f"Since {m(K)} has {m('3')} distinct prime factors, there are {m(f'2^3 = {ans}')} ordered coprime pairs {m('(u, v)')}.",
            ]
            steps_ar = [
                f"نضع {m(f'a = {g}u, b = {g}v')} مع {m('\\gcd(u, v) = 1')}، فيكون {m(f'uv = {L} \\div {g} = {K}')}.",
                f"لتحقيق {m('\\gcd(u,v)=1')}، يجب أن تذهب كل قوة أولية في تحليل {m(K)} كاملةً إما إلى {m('u')} أو إلى {m('v')}.",
                f"بما أن للعدد {m(K)} ثلاثة عوامل أولية مختلفة، يوجد {m(f'2^3 = {ans}')} أزواج مرتبة {m('(a, b)')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_gl_{v_i}")
        h_en = "Factor out g = gcd(a, b) by setting a = g·u and b = g·v with gcd(u, v) = 1; then lcm(a, b) = g·u·v!"
        h_ar = "أخرج القاسم المشترك بوضع a = g·u وb = g·v حيث gcd(u, v) = 1، وعندئذٍ يكون lcm(a, b) = g·u·v!"
        s_en = explain_en("Writing \\( a = g u \\) and \\( b = g v \\) with \\( \\gcd(u, v) = 1 \\) turns every GCD-LCM problem into a simple factor puzzle on \\( u v = L/g \\).", steps_en, f"Verify with \\( g = {g}, L = {L} \\): both GCD and LCM conditions hold!")
        s_ar = explain_ar("كتابة \\( a = g u \\) و\\( b = g v \\) مع \\( \\gcd(u, v) = 1 \\) تحوّل مسائل القاسم والمضاعف إلى مسألة عوامل بسيطة على \\( u v = L/g \\).", steps_ar, f"بالتحقق عند \\( g = {g}, L = {L} \\) يتطابق القاسم المشترك والمضاعف المشترك تماماً.")
        push(diff, "kmc_g89_gcd_lcm_product", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 10. Trailing zeros at the end of N! (10 Qs)
    # ------------------------------------------------------------------
    tz_cases = [
        (20, "Easy"),
        (25, "Easy"),
        (30, "Easy"),
        (45, "Medium"),
        (50, "Medium"),
        (60, "Medium"),
        (75, "Medium"),
        (100, "Medium"),
        (125, "Hard"),
        (150, "Hard"),
    ]
    for v_i, (N, diff) in enumerate(tz_cases):
        c5 = N // 5
        c25 = N // 25
        c125 = N // 125
        ans = c5 + c25 + c125
        distractors = [c5, ans - 1 if ans > 1 else ans + 3, ans + 1, ans + 2, c5 + 1 if c25 > 1 else ans + 4]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_tz_{v_i}")
        sum_parts = f"{c5} + {c25}" + (f" + {c125}" if c125 > 0 else "")
        q_en = (
            f"The product of all integers from {m(1)} to {m(N)} is written as {m(f'{N}! = 1 \\times 2 \\times 3 \\times \\dots \\times {N}')}. "
            f"How many **zeros** are at the right end of {m(f'{N}!')} when written out in full?"
        )
        q_ar = (
            f"يُكتب حاصل ضرب جميع الأعداد الصحيحة من {m(1)} إلى {m(N)} على الصورة {m(f'{N}! = 1 \\times 2 \\times 3 \\times \\dots \\times {N}')}. "
            f"بكم **صفراً** ينتهي العدد {m(f'{N}!')} من جهة اليمين عند كتابته كاملاً؟"
        )
        h_en = "Every trailing zero comes from 10 = 2 × 5. Since factors of 2 are plentiful, count how many factors of 5 appear — and don't forget 25 = 5×5 gives an EXTRA 5!"
        h_ar = "كل صفر في نهاية العدد ينتج عن 10 = 2 × 5. وبما أن عوامل الـ 2 كثيرة جداً، يكفي عدّ عوامل الـ 5 — ولا تنسَ أن مضاعفات 25 تعطي خمسة إضافية!"
        s_en = explain_en(
            "Each trailing zero is produced by one pair \\( 2 \\times 5 = 10 \\). Because even numbers supply plenty of \\( 2 \\)s, the number of trailing zeros equals the **total number of prime factors of \\( 5 \\)** in \\( 1, 2, \\dots, N \\).",
            [
                f"Multiples of {m(5)} up to {m(N)} contribute one {m(5)} each: {m(f'\\lfloor {N}/5 \\rfloor = {c5}')}.",
                f"Multiples of {m(25)} ({m('5^2')}) contribute an **extra** {m(5)} each: {m(f'\\lfloor {N}/25 \\rfloor = {c25}')}"
                + (f", and multiples of {m(125)} ({m('5^3')}) contribute one more: {m(c125)}." if c125 > 0 else "."),
                f"Total trailing zeros: {m(f'{sum_parts} = {ans}')}.",
            ],
            f"Classic trap avoided: {m(c5)} alone forgets the extra factor(s) of {m(5)} inside {m('25, 50, 75, \\dots')}!",
        )
        s_ar = explain_ar(
            "كل صفر في يمين العدد ينتج من زوج \\( 2 \\times 5 = 10 \\). ولأن عوامل الـ \\( 2 \\) متوفرة بكثرة في الأعداد الزوجية، فإن عدد الأصفار يساوي **إجمالي عدد مرات ظهور العامل الأولي \\( 5 \\)**.",
            [
                f"مضاعفات {m(5)} حتى {m(N)} تعطي عامل {m(5)} واحداً لكل منها: {m(f'\\lfloor {N}/5 \\rfloor = {c5}')}.",
                f"مضاعفات {m(25)} ({m('5^2')}) تعطي عامل {m(5)} **إضافياً**: {m(f'\\lfloor {N}/25 \\rfloor = {c25}')}"
                + (f"، ومضاعفات {m(125)} ({m('5^3')}) تعطي عاملاً إضافياً آخر: {m(c125)}." if c125 > 0 else "."),
                f"إجمالي عدد الأصفار في نهاية العدد: {m(f'{sum_parts} = {ans}')}.",
            ],
            f"تجنبنا الفخ الشهير: الاكتفاء بـ {m(c5)} ينسى عوامل الـ {m(5)} الإضافية الموجودة في {m('25, 50, \\dots')}!",
        )
        push(diff, "kmc_g89_trailing_zeros_product", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 11. Sum of digits of 10^n - k (10 Qs)
    # ------------------------------------------------------------------
    p10_cases = [
        (12, 7, "Easy"),
        (15, 4, "Easy"),
        (20, 28, "Easy"),
        (25, 37, "Medium"),
        (30, 64, "Medium"),
        (40, 85, "Medium"),
        (50, 92, "Medium"),
        (60, 125, "Hard"),
        (80, 202, "Hard"),
        (100, 2026, "Hard"),
    ]
    for v_i, (n, k, diff) in enumerate(p10_cases):
        tail_len = len(str(k))
        # Verify on exact Python big integer!
        big_val = 10 ** n - k
        ans = sum(int(ch) for ch in str(big_val))
        n_nines = n - tail_len
        tail_str = str(10 ** tail_len - k).zfill(tail_len)
        tail_sum = sum(int(ch) for ch in tail_str)
        assert ans == 9 * n_nines + tail_sum
        distractors = [9 * n - sum(int(c) for c in str(k)), 9 * (n_nines + 1) + tail_sum, 9 * (n_nines - 1) + tail_sum, ans + 9]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2n_p10_{v_i}")
        small_ex_n = tail_len + 2
        small_ex_val = 10 ** small_ex_n - k
        q_en = f"When the number {m(f'10^{{{n}}} - {k}')} is written out as an ordinary decimal integer, what is the **sum of its digits**?"
        q_ar = f"عند كتابة العدد {m(f'10^{{{n}}} - {k}')} بالصورة العشرية الاعتيادية، ما **مجموع أرقامه**؟"
        h_en = f"Test a tiny exponent first! For example, 10^{small_ex_n} − {k} = {small_ex_val}. Count how many 9s appear at the front!"
        h_ar = f"جرّب أُساً صغيراً أولاً لاكتشاف النمط! مثلاً 10^{small_ex_n} − {k} = {small_ex_val}. لاحظ كم تسعة تظهر في البداية!"
        s_en = explain_en(
            f"\\( 10^{{{n}}} \\) is \\( 1 \\) followed by \\( {n} \\) zeros. Subtracting a {m(tail_len)}-digit number {m(k)} turns the last {m(tail_len)} zeros into `{tail_str}` and turns all the remaining zeros in front into `9`s!",
            [
                f"Test on a small case: {m(f'10^{{{small_ex_n}}} - {k} = {small_ex_val}')} (two `9`s followed by `{tail_str}`).",
                f"For {m(f'10^{{{n}}} - {k}')}, there are {m(f'{n} - {tail_len} = {n_nines}')} digits equal to `9`, followed by the {m(tail_len)} digits `{tail_str}`.",
                f"Sum the digits: {m(f'{n_nines} \\times 9 + ({' + '.join(tail_str)}) = {9*n_nines} + {tail_sum} = {ans}')}.",
            ],
            f"Notice the total number of digits is {m(f'{n_nines} + {tail_len} = {n}')}, matching a number just below {m(f'10^{{{n}}}')}!",
        )
        s_ar = explain_ar(
            f"العدد \\( 10^{{{n}}} \\) هو \\( 1 \\) وأمامه \\( {n} \\) من الأصفار. عند طرح العدد {m(k)} المكون من {m(tail_len)} خانات، تتحول آخر {m(tail_len)} أصفار إلى `{tail_str}` وتتحول جميع الأصفار السابقة لها إلى تسعات `9`!",
            [
                f"نجرب مثالاً صغيراً للتأكد: {m(f'10^{{{small_ex_n}}} - {k} = {small_ex_val}')} (تسعتان يتبعهما `{tail_str}`).",
                f"إذن في العدد {m(f'10^{{{n}}} - {k}')} يوجد {m(f'{n} - {tail_len} = {n_nines}')} تسعة، تتبعها الأرقام `{tail_str}`.",
                f"نجمع الأرقام: {m(f'{n_nines} \\times 9 + ({' + '.join(tail_str)}) = {9*n_nines} + {tail_sum} = {ans}')}.",
            ],
            f"تحقق: إجمالي عدد الخانات هو {m(f'{n_nines} + {tail_len} = {n}')} خانة، وهو الصحيح لعدد أصغر قليلاً من {m(f'10^{{{n}}}')}!",
        )
        push(diff, "kmc_g89_digit_sum_power10_minus_k", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    assert len(out) == 110, f"Expected 110, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 2 Number Theory questions cleanly.")
