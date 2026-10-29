"""Track 3 (Grades 10-11) — Combinatorics & Probability (110 authentic KMC Senior problems)."""
import itertools
import math
from fractions import Fraction

from kmc_common import (
    explain_ar,
    explain_en,
    fmt_val,
    m,
    make_5_bilingual_options,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams import (
    svg_bar_chart,
    svg_cube_net,
    svg_grid_polygon,
    svg_matchstick_squares,
    svg_spinner,
    svg_spiral_walk,
    svg_travel_map,
)

LEVEL = "Track 3: Grades 10-11"


def spiral_pos(steps: int) -> tuple[int, int]:
    """Exact coordinates after `steps` unit steps along (1E, 1N, 2W, 2S, 3E, 3N, 4W, 4S, ...)."""
    x, y = 0, 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d_idx = 0
    seg_len = 1
    rem = steps
    while rem > 0:
        for _ in range(2):
            if rem <= 0:
                break
            take = min(rem, seg_len)
            dx, dy = dirs[d_idx % 4]
            x += dx * take
            y += dy * take
            rem -= take
            d_idx += 1
        seg_len += 1
    return x, y


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(topic, diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en=None, svg_ar=None):
        nonlocal idx
        qid = f"KMC-T3-CMB-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg_en, svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 1. Coordinate rectangular spiral walk (KMC Senior!) (10 Qs, SVG!)
    # ------------------------------------------------------------------
    sp_cases = [
        (25, "coord", "Easy"),
        (40, "coord", "Easy"),
        (60, "sum", "Easy"),
        (85, "coord", "Medium"),
        (100, "coord", "Medium"),
        (130, "sum", "Medium"),
        (200, "coord", "Medium"),
        (400, "sum", "Medium"),
        (1000, "coord", "Hard"),
        (2026, "sum", "Hard"),
    ]
    svg_sp = svg_spiral_walk()
    for v_i, (n_st, ask, diff) in enumerate(sp_cases):
        x, y = spiral_pos(n_st)
        # Find largest k with 2k(2k+1) <= n_st or 2k(2k-1) <= n_st for explanation landmark
        k_land = int((math.isqrt(4 * n_st + 1) - 1) // 4)
        st_land = 2 * k_land * (2 * k_land + 1)
        xl, yl = spiral_pos(st_land)
        assert (xl, yl) == (-k_land, -k_land)

        if ask == "coord":
            pairs = [
                (m(f"({x}, {y})"), m(f"({x}, {y})")),
                (m(f"({y}, {x})") if x != y else m(f"({x+1}, {y})"), m(f"({y}, {x})") if x != y else m(f"({x+1}, {y})")),
                (m(f"({-x}, {y})") if x != 0 else m(f"(1, {y})"), m(f"({-x}, {y})") if x != 0 else m(f"(1, {y})")),
                (m(f"({x}, {-y})") if y != 0 else m(f"({x}, 1)"), m(f"({x}, {-y})") if y != 0 else m(f"({x}, 1)")),
                (m(f"({x - 1}, {y + 1})"), m(f"({x - 1}, {y + 1})")),
            ]
            opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, 0, f"t3c_sp_{v_i}")
            ask_en = f"At which point {m('(x, y)')} is the particle located after **{m(n_st)} unit steps**?"
            ask_ar = f"عند أي نقطة {m('(x, y)')} سيقع الجسيم بعد **{m(n_st)} خطوة وحدة**؟"
            end_en = f"Following the remaining {m(n_st - st_land)} steps along the next spiral edges reaches **{m(f'({x}, {y})')}**."
            end_ar = f"بتتبع الخطوات المتبقية وعددها {m(n_st - st_land)} على أضلاع الحلزون التالية نصل إلى **{m(f'({x}, {y})')}**."
        else:
            ans = x + y
            distractors = [x - y, -ans if ans != 0 else 4, ans + 2, ans - 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_sp_{v_i}")
            ask_en = f"If the particle lands at {m('(x, y)')} after **{m(n_st)} unit steps**, what is the value of {m('x + y')}?"
            ask_ar = f"إذا وصل الجسيم إلى النقطة {m('(x, y)')} بعد **{m(n_st)} خطوة وحدة**، فما قيمة {m('x + y')}؟"
            end_en = f"Tracing the remaining {m(n_st - st_land)} steps lands at {m(f'({x}, {y})')}, so {m(f'x + y = {x} + ({y}) = {ans}')}."
            end_ar = f"بتتبع الـ {m(n_st - st_land)} خطوة المتبقية نصل إلى {m(f'({x}, {y})')}، ومنه {m(f'x + y = {x} + ({y}) = {ans}')}."

        q_en = (
            f"A particle starts at the origin {m('(0, 0)')} and moves along the rectangular spiral shown: "
            f"{m(1)} unit East, {m(1)} unit North, {m(2)} units West, {m(2)} units South, {m(3)} units East, {m(3)} units North, and so on. "
            f"{ask_en}"
        )
        q_ar = (
            f"يبدأ جسيم من نقطة الأصل {m('(0, 0)')} ويتحرك على المسار الحلزوني الموضح: "
            f"وحدة واحدة شرقاً، ثم وحدة شمالاً، ثم وحدتين غرباً، ثم وحدتين جنوباً، ثم 3 شرقاً، ثم 3 شمالاً، وهكذا. "
            f"{ask_ar}"
        )
        h_en = "Spot the corner pattern! After 1+1+2+2+...+2k+2k = 2k(2k+1) steps, the particle always sits at bottom-left corner (−k, −k)!"
        h_ar = "اكتشف نمط الزوايا! بعد 1+1+2+2+...+2k+2k = 2k(2k+1) خطوة، يقف الجسيم دائماً عند الركن السفلي الأيسر (−k, −k)!"
        s_en = explain_en(
            "Group segment lengths in pairs: \\( (1+1) + (2+2) + \\dots + (m+m) = m(m+1) \\). After \\( m = 2k \\) pairs (\\( 2k(2k+1) \\) steps), the particle is always at \\( (-k, -k) \\) facing East!",
            [
                f"Pick \\( k = {k_land} \\): after {m(f'2({k_land})(2\\cdot{k_land}+1) = {st_land}')} steps, the particle is at {m(f'(-{k_land}, -{k_land})')} ready to move {m(2*k_land + 1)} units East, then {m(2*k_land + 1)} units North, etc.",
                end_en,
            ],
            f"Test the formula at \\( k=1 \\): after \\( 2(3)=6 \\) steps (\\( 1\\text{{E}}, 1\\text{{N}}, 2\\text{{W}}, 2\\text{{S}} \\)), it is indeed at \\( (-1, -1) \\)!",
        )
        s_ar = explain_ar(
            "نجمع أطوال القطع المثناة: \\( (1+1) + (2+2) + \\dots + (m+m) = m(m+1) \\). بعد \\( m = 2k \\) أزواج (أي \\( 2k(2k+1) \\) خطوة)، يقف الجسيم دائماً عند الزاوية \\( (-k, -k) \\) متجهاً شرقاً!",
            [
                f"نختار \\( k = {k_land} \\): بعد {m(st_land)} خطوة يقف الجسيم عند {m(f'(-{k_land}, -{k_land})')} ثم يتحرك {m(2*k_land + 1)} شرقاً ثم {m(2*k_land + 1)} شمالاً...",
                end_ar,
            ],
            f"تحقق عند \\( k=1 \\) (بعد 6 خطوات): يصل فعلاً إلى \\( (-1, -1) \\)!",
        )
        push("Combinatorics & Logic", diff, "kmc_g1011_spiral_walk_coords", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_sp)

    # ------------------------------------------------------------------
    # 2. Lattice points inside |x| + |y| <= R (10 Qs, SVG!)
    # ------------------------------------------------------------------
    lat_cases = [
        (3, "<=", "Easy"),
        (4, "<=", "Easy"),
        (5, "<=", "Easy"),
        (6, "<=", "Medium"),
        (7, "=", "Medium"),
        (8, "<=", "Medium"),
        (10, "=", "Medium"),
        (10, "<=", "Medium"),
        (12, "<=", "Hard"),
        (15, "<=", "Hard"),
    ]
    svg_diam = svg_grid_polygon(6, 6, [(3, 0), (6, 3), (3, 6), (0, 3)], ["S", "E", "N", "W"])
    for v_i, (R, rel, diff) in enumerate(lat_cases):
        if rel == "<=":
            ans = 2 * R * R + 2 * R + 1
            bf = sum(1 for x in range(-R, R + 1) for y in range(-R, R + 1) if abs(x) + abs(y) <= R)
            assert ans == bf
            distractors = [(2 * R + 1) ** 2, 2 * R * R + 1, ans - 4 * R, ans + 2 * R]
            q_en = (
                f"How many points {m('(x, y)')} with **integer coordinates** satisfy {m(f'|x| + |y| \\le {R}')} "
                f"(forming a diamond region like the one illustrated)?"
            )
            q_ar = (
                f"كم نقطة {m('(x, y)')} ذات **إحداثيات صحيحة** تحقق المتباينة {m(f'|x| + |y| \\le {R}')} "
                f"(والتي تكوّن منطقة معينية كالموضحة في الشكل التوضيحي)؟"
            )
            steps_en = [
                f"Slice horizontally by the value of {m('y')}: when {m('y = 0')}, {m(f'|x| \\le {R}')} gives {m(2*R + 1)} points.",
                f"Moving up or down from {m('y = 0')} to {m(f'y = \\pm {R}')}, the counts are {m(f'1 + 3 + 5 + \\dots + {2*R-1}')} above AND the same below.",
                f"Recall {m(f'1 + 3 + \\dots + (2R-1) = R^2 = {R*R}')}, so total points = {m(f'{R*R} + {2*R+1} + {R*R} = {ans}')} (equivalently {m(f'R^2 + (R+1)^2 = {R*R} + {(R+1)**2} = {ans}')}!).",
            ]
            steps_ar = [
                f"نقسّم النقاط أفقياً حسب قيمة {m('y')}: عند {m('y = 0')} لدينا {m(f'|x| \\le {R}')} أي {m(2*R + 1)} نقطة.",
                f"فوق المحور الأفقي (من {m('y=1')} إلى {m(f'y={R}')}) أعداد النقاط هي {m(f'1 + 3 + \\dots + {2*R-1} = {R*R}')}، ومثلها تماماً تحت المحور!",
                f"المجموع الكلي: {m(f'{R*R} + {2*R+1} + {R*R} = {ans}')} نقطة (أو بالصيغة الأنيقة {m(f'R^2 + (R+1)^2 = {ans}')}!).",
            ]
        else:
            ans = 4 * R
            bf = sum(1 for x in range(-R, R + 1) for y in range(-R, R + 1) if abs(x) + abs(y) == R)
            assert ans == bf
            distractors = [4 * R + 4, 4 * R - 4, 2 * R * R + 2 * R + 1, 2 * R]
            q_en = f"How many points {m('(x, y)')} with **integer coordinates** lie **on the boundary** {m(f'|x| + |y| = {R}')}?"
            q_ar = f"كم نقطة {m('(x, y)')} ذات **إحداثيات صحيحة** تقع **على المحيط** {m(f'|x| + |y| = {R}')}؟"
            steps_en = [
                f"Consider the values of {m('x')} from {m(-R)} to {m(R)}:",
                f"At {m(f'x = -{R}')} and {m(f'x = {R}')}, {m('|y| = 0')} gives **1** point each ({m(2)} points total).",
                f"For each of the {m(2*R - 1)} values {m(f'-{R-1} \\le x \\le {R-1}')}, {m(f'|y| = {R} - |x| > 0')} gives **2** points ({m('\\pm y')}): {m(f'2 + 2({2*R-1}) = {ans}')}.",
            ]
            steps_ar = [
                f"ندرس قيم {m('x')} الصحيحة من {m(-R)} إلى {m(R)}:",
                f"عند الطرفين {m(f'x = \\pm {R}')} يكون {m('y = 0')} فنحصل على نقطتين فقط.",
                f"ولكل قيمة من القيم الـ {m(2*R - 1)} الوسطى يكون {m('|y| > 0')} فنحصل على نقطتين ({m('\\pm y')}): الإجمالي {m(f'2 + 2({2*R-1}) = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_lat_{v_i}")
        h_en = "Count row by row for y = −R, ..., 0, ..., +R — notice the row counts are consecutive odd numbers!"
        h_ar = "عُدّ النقاط صفاً بصف لقيم y من −R إلى +R — ستلاحظ أن أعداد النقاط في الصفوف أعداد فردية متتالية!"
        s_en = explain_en("Slicing a Manhattan-distance diamond \\( |x| + |y| \\le R \\) row by row turns a 2D problem into a sum of odd integers!", steps_en, f"Test \\( R = 1 \\): \\( (0,0), (\\pm 1, 0), (0, \\pm 1) \\) gives \\( 5 \\) total and \\( 4 \\) boundary points — both formulas match!")
        s_ar = explain_ar("تقسيم معين مسافة مانهاتن \\( |x| + |y| \\le R \\) إلى صفوف أفقية يحوّل المسألة إلى مجموع أعداد فردية متتالية!", steps_ar, f"للتحقق عند \\( R = 1 \\): توجد 5 نقاط كلية و4 نقاط على المحيط — مطابق تماماً!")
        push("Combinatorics & Logic", diff, "kmc_g1011_diamond_lattice_points", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_diam)

    # ------------------------------------------------------------------
    # 3. Sequential 2-day outfit probability without replacement (KMC Senior Q3!) (10 Qs)
    # ------------------------------------------------------------------
    out_cases = [
        # (red_shirts, blue_shirts, red_shorts, blue_shorts, diff)
        (2, 1, 1, 2, "Easy"),      # exact KMC Senior page_d-018.png Q3!
        (2, 2, 2, 2, "Easy"),
        (3, 1, 1, 3, "Easy"),
        (3, 2, 2, 3, "Medium"),
        (3, 1, 2, 2, "Medium"),
        (4, 1, 1, 4, "Medium"),
        (4, 2, 2, 4, "Medium"),
        (3, 3, 2, 4, "Medium"),
        (4, 2, 3, 3, "Hard"),
        (5, 2, 2, 5, "Hard"),
    ]
    for v_i, (rs, bs, rsh, bsh, diff) in enumerate(out_cases):
        S_tot = rs + bs
        H_tot = rsh + bsh
        # Day 1 & Day 2 both matching color (RR+RR, RR+BB, BB+RR, BB+BB) without replacement!
        # Let's compute exact probability over ordered 2-day picks:
        denom = S_tot * (S_tot - 1) * H_tot * (H_tot - 1)
        rr_rr = rs * (rs - 1) * rsh * (rsh - 1)
        bb_bb = bs * (bs - 1) * bsh * (bsh - 1)
        rr_bb = rs * bs * rsh * bsh
        bb_rr = bs * rs * bsh * rsh
        numer = rr_rr + bb_bb + rr_bb + bb_rr
        ans = Fraction(numer, denom)
        # Trap: WITH replacement ((rs*rsh + bs*bsh)/(S_tot*H_tot))^2
        p_day1 = Fraction(rs * rsh + bs * bsh, S_tot * H_tot)
        trap_rep = p_day1 * p_day1
        distractors = [
            trap_rep if trap_rep != ans else Fraction(ans.numerator + 1, ans.denominator + 2),
            p_day1,
            Fraction(rr_bb + bb_rr, denom),
            Fraction(min(denom - 1, numer + S_tot), denom),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_out_{v_i}")
        q_en = (
            f"Faisal has {m(rs)} red shirts and {m(bs)} blue shirt{'s' if bs>1 else ''}, as well as {m(rsh)} red pair{'s' if rsh>1 else ''} of shorts and {m(bsh)} blue pairs of shorts. "
            f"On Monday he randomly picks one shirt and one pair of shorts, and on Tuesday he randomly picks one shirt and one pair of shorts from the **remaining** unworn items. "
            f"What is the probability that on **both days** his shirt and shorts have the **same color**?"
        )
        q_ar = (
            f"لدى فيصل {m(rs)} قمصان حمراء و{m(bs)} قمصان زرقاء، وكذلك {m(rsh)} سراويل رياضية حمراء و{m(bsh)} سراويل زرقاء. "
            f"يوم الإثنين اختار عشوائياً قميصاً وسروالاً، ويوم الثلاثاء اختار عشوائياً قميصاً وسروالاً من القطع **المتبقية** دون إرجاع ما لبسه يوم الإثنين. "
            f"ما احتمال أن يكون القميص والسروال **من اللون نفسه في كلا اليومين معاً**؟"
        )
        h_en = "Split into mutually exclusive 2-day color sequences: (Red-Red then Red-Red), (Blue-Blue then Blue-Blue), (Red-Red then Blue-Blue), and (Blue-Blue then Red-Red)!"
        h_ar = "قسّم الحدث إلى 4 حالات متنافية لليومين: (أحمر ثم أحمر)، (أزرق ثم أزرق)، (أحمر ثم أزرق)، و(أزرق ثم أحمر) بدون إرجاع!"
        s_en = explain_en(
            f"There are {m(f'{S_tot}\\times{S_tot-1} = {S_tot*(S_tot-1)}')} ordered 2-day shirt choices and {m(f'{H_tot}\\times{H_tot-1} = {H_tot*(H_tot-1)}')} ordered 2-day shorts choices ({m(denom)} equally likely 2-day sequences).",
            [
                f"Both days Red: {m(f'({rs}\\times{rs-1}) \\times ({rsh}\\times{rsh-1}) = {rr_rr}')} ways; Both days Blue: {m(f'({bs}\\times{bs-1}) \\times ({bsh}\\times{bsh-1}) = {bb_bb}')} ways.",
                f"Red Monday & Blue Tuesday: {m(f'({rs}\\times{bs}) \\times ({rsh}\\times{bsh}) = {rr_bb}')} ways; Blue Monday & Red Tuesday: {m(bb_rr)} ways.",
                f"Add all 4 cases and divide by {m(denom)}: {m(f'\\frac{{{rr_rr} + {bb_bb} + {rr_bb} + {bb_rr}}}{{{denom}}} = \\frac{{{numer}}}{{{denom}}} = {fmt_val(ans)}')}.",
            ],
            "Notice that when a count is 1 (e.g. only 1 red short), repeating that color twice has 1 × 0 = 0 ways automatically!",
        )
        s_ar = explain_ar(
            f"يوجد {m(S_tot*(S_tot-1))} اختياراً مرتباً للقمصان خلال اليومين و{m(H_tot*(H_tot-1))} اختياراً مرتباً للسراويل، أي {m(denom)} تسلسلاً متساوي الاحتمال.",
            [
                f"أحمر في اليومين: {m(rr_rr)} طريقة؛ أزرق في اليومين: {m(bb_bb)} طريقة.",
                f"أحمر الإثنين وأزرق الثلاثاء: {m(rr_bb)} طريقة؛ أزرق الإثنين وأحمر الثلاثاء: {m(bb_rr)} طريقة.",
                f"نجمع الحالات الأربع ونقسم على {m(denom)}: {m(f'\\frac{{{numer}}}{{{denom}}} = {fmt_val(ans)}')}.",
            ],
            "لاحظ أنه بدون إرجاع، إذا كان هناك قطعة واحدة فقط من لون معين فلا يمكن تكرار ذلك اللون في اليومين (0 طرق)!",
        )
        push("Data & Probability", diff, "kmc_g1011_sequential_prob_no_replace", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 4. Matchstick m x n rectangular grid total sticks (10 Qs, SVG!)
    # ------------------------------------------------------------------
    ms_cases = [
        (3, 4, "sticks", "Easy"),
        (4, 5, "sticks", "Easy"),
        (5, 5, "sticks", "Easy"),
        (5, 8, "sticks", "Medium"),
        (6, 7, "sticks", "Medium"),
        (8, 10, "sticks", "Medium"),
        (4, 9, "cols", "Medium"),       # given m=4 rows and total sticks, find n=9 cols!
        (5, 11, "cols", "Medium"),
        (10, 12, "sticks", "Hard"),
        (6, 14, "cols", "Hard"),
    ]
    svg_ms = svg_matchstick_squares((1, 2, 3))
    for v_i, (rows, cols, ask, diff) in enumerate(ms_cases):
        h_st = (rows + 1) * cols
        v_st = rows * (cols + 1)
        tot_st = h_st + v_st
        assert tot_st == 2 * rows * cols + rows + cols
        if ask == "sticks":
            ans = tot_st
            distractors = [4 * rows * cols, 2 * rows * cols, tot_st - (rows + cols), tot_st + rows]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_ms_{v_i}")
            q_en = (
                f"Unit matchsticks are arranged to build a complete {m(f'{rows} \\times {cols}')} rectangular grid of unit squares "
                f"(sharing interior edges, like extending the matchstick row shown to {m(rows)} rows and {m(cols)} columns). "
                f"How many matchsticks are needed in total?"
            )
            q_ar = (
                f"رُتِّبت أعواد ثقاب متطابقة لبناء شبكة مستطيلة كاملة أبعادها {m(f'{rows} \\times {cols}')} من المربعات الصغيرة "
                f"(بحيث تشترك المربعات المتجاورة في الأعواد الداخلية). كم عود ثقاب يلزم إجمالاً؟"
            )
            steps_en = [
                f"Count **horizontal** matchsticks: there are {m(f'{rows} + 1 = {rows+1}')} horizontal grid lines, each {m(cols)} sticks long → {m(f'{rows+1} \\times {cols} = {h_st}')} sticks.",
                f"Count **vertical** matchsticks: there are {m(f'{cols} + 1 = {cols+1}')} vertical grid lines, each {m(rows)} sticks tall → {m(f'{cols+1} \\times {rows} = {v_st}')} sticks.",
                f"Add horizontal and vertical sticks: {m(f'{h_st} + {v_st} = {ans}')}.",
            ]
            steps_ar = [
                f"نعدّ الأعواد **الأفقية**: يوجد {m(rows + 1)} خطوط أفقية في كلٍّ منها {m(cols)} أعواد ← {m(f'{rows+1} \\times {cols} = {h_st}')} عوداً.",
                f"نعدّ الأعواد **الرأسية**: يوجد {m(cols + 1)} خطوط رأسية في كلٍّ منها {m(rows)} أعواد ← {m(f'{cols+1} \\times {rows} = {v_st}')} عوداً.",
                f"نجمع الأفقي والرأسي: {m(f'{h_st} + {v_st} = {ans}')} عوداً.",
            ]
        else:
            ans = cols
            per_col = 2 * rows + 1
            distractors = [cols - 1, cols + 1, tot_st // (3 * rows + 1), cols + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_ms_{v_i}")
            q_en = (
                f"Using exactly {m(tot_st)} unit matchsticks (with adjacent squares sharing interior matchsticks), "
                f"Yousef builds a complete rectangular grid having **{m(rows)} rows** and {m('n')} columns of unit squares. What is {m('n')}?"
            )
            q_ar = (
                f"باستخدام {m(tot_st)} عود ثقاب بالضبط (مع اشتراك المربعات المتجاورة في الأعواد الداخلية)، "
                f"بنى يوسف شبكة مستطيلة مكتملة مكونة من **{m(rows)} صفوف** و{m('n')} من الأعمدة. ما قيمة {m('n')}؟"
            )
            steps_en = [
                f"Total sticks for {m(rows)} rows and {m('n')} columns is {m(f'({rows}+1)n + {rows}(n+1) = {per_col}n + {rows}')}.",
                f"Set equal to {m(tot_st)}: {m(f'{per_col}n + {rows} = {tot_st} \\implies {per_col}n = {tot_st - rows}')}.",
                f"Divide by {m(per_col)}: {m(f'n = \\frac{{{tot_st - rows}}}{{{per_col}}} = {ans}')} columns.",
            ]
            steps_ar = [
                f"عدد الأعواد لشبكة فيها {m(rows)} صفوف و{m('n')} عموداً هو {m(f'({rows}+1)n + {rows}(n+1) = {per_col}n + {rows}')}.",
                f"نساوي المجموع بـ {m(tot_st)}: {m(f'{per_col}n + {rows} = {tot_st} \\implies {per_col}n = {tot_st - rows}')}.",
                f"نقسم على {m(per_col)}: {m(f'n = {ans}')} أعمدة.",
            ]

        h_en = "Count ALL horizontal matchsticks first ((rows + 1) × cols), then ALL vertical matchsticks (rows × (cols + 1))!"
        h_ar = "عُدّ جميع الأعواد الأفقية أولاً ((الصفوف + 1) × الأعمدة)، ثم جميع الأعواد الرأسية (الصفوف × (الأعمدة + 1))!"
        s_en = explain_en("Separating horizontal grid segments from vertical grid segments counts every matchstick cleanly without double-counting shared interior edges!", steps_en, f"Check on a 1×1 square: \\( 2(1)(1)+1+1 = 4 \\) matchsticks!")
        s_ar = explain_ar("فصل الأعواد الأفقية عن الأعواد الرأسية يمنع تكرار عدّ الأضلاع المشتركة الداخلية!", steps_ar, f"للتحقق عند مربع واحد 1×1 تعطي القاعدة 4 أعواد بالضبط!")
        push("Combinatorics & Logic", diff, "kmc_g1011_matchstick_grid_total", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_ms)

    # ------------------------------------------------------------------
    # 5. Football 3-1-0 tournament point invariant (3G - D = Total Points) (10 Qs)
    # ------------------------------------------------------------------
    trn_cases = [
        (5, 3, "Easy"),      # G=10, 3G=30, D=3 -> P=27
        (6, 4, "Easy"),      # G=15, 3G=45, D=4 -> P=41
        (6, 7, "Easy"),      # G=15, D=7 -> P=38
        (7, 5, "Medium"),    # G=21, 3G=63, D=5 -> P=58
        (8, 6, "Medium"),    # G=28, 3G=84, D=6 -> P=78
        (8, 10, "Medium"),   # G=28, D=10 -> P=74
        (9, 8, "Medium"),    # G=36, 3G=108, D=8 -> P=100
        (10, 11, "Medium"),  # G=45, 3G=135, D=11 -> P=124
        (10, 15, "Hard"),    # G=45, D=15 -> P=120
        (12, 14, "Hard"),    # G=66, 3G=198, D=14 -> P=184
    ]
    for v_i, (n_teams, draws, diff) in enumerate(trn_cases):
        G = n_teams * (n_teams - 1) // 2
        tot_pts = 3 * G - draws
        ans = draws
        distractors = [(tot_pts - 2 * G), draws + 2, max(1, draws - 2), G - draws]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_trn_{v_i}")
        q_en = (
            f"In a football league of {m(n_teams)} teams, every pair of teams plays **exactly once**. "
            f"In each match, a win awards {m(3)} points to the winner and {m(0)} to the loser, while a **draw** awards {m(1)} point to **each** of the two teams. "
            f"At the end of the tournament, the sum of all {m(n_teams)} teams' points is {m(tot_pts)}. How many matches ended in a **draw**?"
        )
        q_ar = (
            f"في بطولة كرة قدم تضم {m(n_teams)} فِرق، يلعب كل فريقين معاً **مباراة واحدة فقط**. "
            f"في كل مباراة يحصل الفائز على {m(3)} نقاط والخاسر على {m(0)}، وفي حالة **التعادل** يحصل **كل فريق** من الفريقين على نقطة واحدة ({m(1)}). "
            f"في نهاية البطولة كان مجموع نقاط جميع الفِرق الـ {m(n_teams)} يساوي {m(tot_pts)} نقطة. كم مباراة انتهت **بالتعادل**؟"
        )
        h_en = f"Look at the TOTAL points awarded in a single match: a decisive match adds 3 + 0 = 3 points to the league total, while a draw adds only 1 + 1 = 2 points!"
        h_ar = f"انظر إلى مجموع النقاط الموزعة في المباراة الواحدة: الفوز يضيف 3 + 0 = 3 نقاط للمجموع الكلي، بينما التعادل يضيف 1 + 1 = 2 نقطتين فقط!"
        s_en = explain_en(
            "Every decisive match contributes \\( 3 + 0 = 3 \\) points to the sum of all teams' points, whereas every **draw** contributes \\( 1 + 1 = 2 \\) points — **\\( 1 \\) point less** than 3!",
            [
                f"Total number of matches played among {m(n_teams)} teams: {m(f'\\frac{{{n_teams} \\times {n_teams - 1}}}{{2}} = {G}')}.",
                f"If all {m(G)} matches had a winner, the league total would be {m(f'3 \\times {G} = {3*G}')} points.",
                f"Each draw reduces that maximum total by {m('3 - 2 = 1')} point, so the number of draws is {m(f'{3*G} - {tot_pts} = {ans}')}!",
            ],
            f"Check: {m(G - draws)} decisive matches ({m(3*(G-draws))} pts) + {m(draws)} draws ({m(2*draws)} pts) = {m(tot_pts)} total points!",
        )
        s_ar = explain_ar(
            "كل مباراة تنتهي بفوز تضيف \\( 3 + 0 = 3 \\) نقاط للمجموع الكلي، بينما كل **تعادل** يضيف \\( 1 + 1 = 2 \\) نقطتين فقط — أي **أقل بنقطة واحدة** من 3!",
            [
                f"إجمالي عدد المباريات بين {m(n_teams)} فِرق: {m(f'\\frac{{{n_teams} \\times {n_teams - 1}}}{{2}} = {G}')} مباراة.",
                f"لو انتهت جميع المباريات الـ {m(G)} بفوز لكان مجموع النقاط {m(f'3 \\times {G} = {3*G}')} نقطة.",
                f"بما أن كل تعادل يُنقص المجموع الكلي بمقدار {m('1')} نقطة، فإن عدد مباريات التعادل يساوي {m(f'{3*G} - {tot_pts} = {ans}')}!",
            ],
            f"تحقق: {m(G - draws)} فوز ({m(3*(G-draws))} نقطة) + {m(draws)} تعادل ({m(2*draws)} نقطة) = {m(tot_pts)} نقطة!",
        )
        push("Combinatorics & Logic", diff, "kmc_g1011_tournament_handshakes", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. Cube net maximum corner-vertex product of 3 meeting faces (10 Qs, SVG!)
    # ------------------------------------------------------------------
    # Cross net: (1,0)=Top, (0,1)=Left, (1,1)=Base, (2,1)=Right, (3,1)=OppositeBase, (1,2)=Bottom
    # Opposite pairs are: ((1,0), (1,2)), ((0,1), (2,1)), ((1,1), (3,1))!
    # Three faces meet at a vertex iff we pick ONE face from each of the 3 opposite pairs!
    cnet_cases = [
        ((2, 5), (3, 4), (1, 6), "Easy"),
        ((3, 6), (2, 5), (4, 1), "Easy"),
        ((7, 2), (3, 5), (4, 6), "Easy"),
        ((4, 8), (5, 3), (2, 7), "Medium"),
        ((9, 3), (4, 6), (5, 2), "Medium"),
        ((5, 7), (8, 3), (4, 6), "Medium"),
        ((6, 9), (7, 4), (3, 8), "Medium"),
        ((8, 5), (9, 2), (6, 7), "Medium"),
        ((11, 4), (6, 9), (8, 5), "Hard"),
        ((12, 7), (5, 10), (9, 4), "Hard"),
    ]
    for v_i, ((p1a, p1b), (p2a, p2b), (p3a, p3b), diff) in enumerate(cnet_cases):
        cells = [
            (1, 0, str(p1a)),
            (0, 1, str(p2a)),
            (1, 1, str(p3a)),
            (2, 1, str(p2b)),
            (3, 1, str(p3b)),
            (1, 2, str(p1b)),
        ]
        svg = svg_cube_net(cells)
        m1, m2, m3 = max(p1a, p1b), max(p2a, p2b), max(p3a, p3b)
        ans = m1 * m2 * m3
        # Trap: multiplying the 3 largest numbers overall even if two are opposite!
        all6 = sorted([p1a, p1b, p2a, p2b, p3a, p3b], reverse=True)
        trap_top3 = all6[0] * all6[1] * all6[2]
        distractors = [
            trap_top3 if trap_top3 != ans else ans + m1,
            min(p1a, p1b) * m2 * m3,
            m1 * min(p2a, p2b) * m3,
            m1 * m2 * min(p3a, p3b),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_cnet_{v_i}")
        q_en = (
            f"The six-square net shown (top {m(p1a)}, middle row {m(f'{p2a}, {p3a}, {p2b}, {p3b}')}, bottom {m(p1b)}) is folded along its edges to form a cube. "
            f"At each of the {m(8)} corners (vertices) of the cube, **three faces meet**, and we compute the **product** of the three numbers on those faces. "
            f"What is the **largest** of these {m(8)} corner products?"
        )
        q_ar = (
            f"طُويت الشبكة المكونة من ستة مربعات الموضحة في الشكل (العلوي {m(p1a)}، الصف الأوسط {m(f'{p2a}, {p3a}, {p2b}, {p3b}')}، السفلي {m(p1b)}) لتكوين مكعب. "
            f"عند كل رأس من الرؤوس الـ {m(8)} للمكعب **تلتقي ثلاثة أوجه**، ونحسب **حاصل ضرب** الأعداد الثلاثة المكتوبة عليها. "
            f"ما **أكبر** حاصل ضرب من بين نواتج الرؤوس الـ {m(8)}؟"
        )
        h_en = "Two opposite faces NEVER touch the same corner! Identify the 3 pairs of opposite faces, pick the LARGER number from each pair, and multiply!"
        h_ar = "الوجهان المتقابلان لا يلتقيان أبداً عند رأس واحد! حدّد الأزواج الثلاثة للأوجه المتقابلة، واختر العدد الأكبر من كل زوج ثم اضربها!"
        s_en = explain_en(
            "Every corner of a cube is formed by choosing **one face from each of the 3 opposite-face pairs**! So the maximum corner product simply picks the larger number from each opposite pair.",
            [
                f"Fold the net to identify the 3 opposite pairs: {m(f'\\{{{p1a}, {p1b}\\}}')}, {m(f'\\{{{p2a}, {p2b}\\}}')}, and {m(f'\\{{{p3a}, {p3b}\\}}')}.",
                f"Choose the larger value from each opposite pair: {m(m1)}, {m(m2)}, and {m(m3)}.",
                f"Multiply them together: {m(f'{m1} \\times {m2} \\times {m3} = {ans}')}.",
            ],
            "Beware the trap of multiplying the 3 largest numbers on the net without checking if two of them sit on opposite faces!",
        )
        s_ar = explain_ar(
            "يتكوّن كل رأس في المكعب من التقاء **وجه واحد من كل زوج من الأزواج الثلاثة المتقابلة**! لذا نختار العدد الأكبر من كل زوج متقابل ونضربها معاً.",
            [
                f"عند طي الشبكة نحدّد أزواج الأوجه المتقابلة الثلاثة: {m(f'\\{{{p1a}, {p1b}\\}}')} و{m(f'\\{{{p2a}, {p2b}\\}}')} و{m(f'\\{{{p3a}, {p3b}\\}}')}.",
                f"نختار الأكبر من كل زوج متقابل: {m(m1)} و{m(m2)} و{m(m3)}.",
                f"نضرب القيم الثلاث: {m(f'{m1} \\times {m2} \\times {m3} = {ans}')}.",
            ],
            "تجنب فخ ضرب أكبر ثلاثة أعداد في الشبكة دون التأكد من عدم تقابل أي اثنين منها!",
        )
        push("Combinatorics & Logic", diff, "kmc_g1011_cube_net_opposite_sum", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 7. Weighted map network: shortest path avoiding a closed node or edge (10 Qs, SVG!)
    # ------------------------------------------------------------------
    net_cases = [
        ((7, 15, 8, 4, 5, 9, 13, 12), "M", "Easy"),
        ((6, 14, 9, 3, 4, 8, 12, 10), "M", "Easy"),
        ((8, 16, 7, 5, 4, 7, 14, 13), "A", "Easy"),
        ((9, 18, 8, 4, 5, 8, 15, 14), "B", "Medium"),
        ((7, 17, 6, 4, 4, 9, 13, 12), "M", "Medium"),
        ((10, 19, 8, 5, 4, 8, 16, 14), "B", "Medium"),
        ((8, 20, 9, 4, 5, 9, 15, 13), "M", "Medium"),
        ((11, 22, 9, 5, 5, 10, 17, 15), "B", "Medium"),
        ((9, 21, 10, 4, 6, 8, 16, 15), "A", "Hard"),
        ((12, 24, 11, 5, 5, 9, 19, 17), "M", "Hard"),
    ]
    node_names_en = {"A": "West Gate", "M": "Central Plaza", "B": "East Gate"}
    node_names_ar = {"A": "البوابة الغربية", "M": "الساحة الوسطى", "B": "البوابة الشرقية"}
    for v_i, (wts, closed_k, diff) in enumerate(net_cases):
        w_sa, w_sm, w_sb, w_am, w_bm, w_mt, w_at, w_bt = wts
        edges = [
            ("S", "A", w_sa), ("S", "M", w_sm), ("S", "B", w_sb),
            ("A", "M", w_am), ("B", "M", w_bm),
            ("M", "T", w_mt), ("A", "T", w_at), ("B", "T", w_bt),
        ]
        svg_en = svg_travel_map(
            {"S": (170, 200, "Lab"), "A": (62, 125, "West Gate"), "M": (170, 115, "Central Plaza"), "B": (278, 125, "East Gate"), "T": (170, 28, "Auditorium")},
            edges,
        )
        svg_ar = svg_travel_map(
            {"S": (170, 200, "المختبر"), "A": (62, 125, "البوابة الغربية"), "M": (170, 115, "الساحة الوسطى"), "B": (278, 125, "البوابة الشرقية"), "T": (170, 28, "القاعة")},
            edges,
        )

        def shortest_avoiding(ban_set):
            allowed = [k for k in ("S", "A", "M", "B", "T") if k not in ban_set]
            best = {k: 10**9 for k in allowed}
            best["S"] = 0
            for _ in range(len(allowed)):
                for u, v, w in edges:
                    if u in best and v in best:
                        if best[u] + w < best[v]:
                            best[v] = best[u] + w
                        if best[v] + w < best[u]:
                            best[u] = best[v] + w
            return best["T"]

        ans = shortest_avoiding({closed_k})
        unrestricted = shortest_avoiding(set())
        distractors = [unrestricted if unrestricted != ans else ans - 2, ans + 2, ans + 3, max(8, ans - 1)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_net_{v_i}")
        q_en = (
            f"The campus map shows travel times (in minutes) between the **Lab** and the **Auditorium** "
            f"(direct Lab–West Gate {m(w_sa)}, Lab–Plaza {m(w_sm)}, Lab–East Gate {m(w_sb)}). "
            f"Today **{node_names_en[closed_k]}** is closed for maintenance, so no path may pass through it. "
            f"What is the **minimum travel time** from the **Lab** to the **Auditorium**?"
        )
        q_ar = (
            f"توضّح خريطة الحرم الجامعي أزمنة التنقل (بالدقائق) بين **المختبر** و**القاعة** "
            f"(من المختبر إلى البوابة الغربية {m(w_sa)}، وإلى الساحة الوسطى {m(w_sm)}، وإلى البوابة الشرقية {m(w_sb)}). "
            f"أُغلقت **{node_names_ar[closed_k]}** اليوم للصيانة، فلا يمكن المرور عبرها. "
            f"ما **أقل زمن تنقل ممكن** من **المختبر** إلى **القاعة**؟"
        )
        h_en = f"Cross out '{node_names_en[closed_k]}' and EVERY road connected to it, then compare the remaining routes from Lab to Auditorium!"
        h_ar = f"اشطب «{node_names_ar[closed_k]}» وجميع الطرق المتصلة بها، ثم قارن المسارات المتبقية من المختبر إلى القاعة!"
        s_en = explain_en(
            f"Deleting the closed hub (**{node_names_en[closed_k]}**) and all edges touching it simplifies the map to just the open hubs!",
            [
                f"Remove {node_names_en[closed_k]} and every road incident to it.",
                f"Evaluate the travel time along each remaining valid route from Lab to Auditorium.",
                f"The shortest available open route takes **{m(ans)}** minutes.",
            ],
            f"Note that without the closure, the unrestricted shortest route would take {m(unrestricted)} minutes.",
        )
        s_ar = explain_ar(
            f"عند حذف النقطة المغلقة (**{node_names_ar[closed_k]}**) وجميع الطرق المتصلة بها تتبسط الخريطة إلى المسارات المفتوحة فقط!",
            [
                f"نستبعد جميع الطرق المارّة بـ{node_names_ar[closed_k]}.",
                f"نحسب زمن كل مسار مفتوح متبقٍّ من المختبر إلى القاعة.",
                f"أقصر مسار مفتوح يستغرق **{m(ans)}** دقيقة.",
            ],
            f"ملاحظة: بدون الإغلاق كان أقصر زمن ممكن {m(unrestricted)} دقيقة.",
        )
        push("Combinatorics & Logic", diff, "kmc_g1011_network_path_counting", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en, svg_ar)

    # ------------------------------------------------------------------
    # 8. Subset sums: even sum & divisible-by-3 sum (10 Qs)
    # ------------------------------------------------------------------
    sub_cases = [
        (5, "even_nonempty", "Easy"),
        (6, "even_nonempty", "Easy"),
        (7, "even_nonempty", "Medium"),
        (8, "even_nonempty", "Medium"),
        (9, "even_nonempty", "Medium"),
        (6, "3elem_mod3", "Medium"),      # {1..6}: 3 residues of size 2 -> 0+0+0(0) + 2^3 = 8!
        (9, "3elem_mod3", "Medium"),      # {1..9}: 3*C(3,3) + 3^3 = 3 + 27 = 30!
        (12, "3elem_mod3", "Hard"),       # {1..12}: 3*C(4,3) + 4^3 = 12 + 64 = 76!
        (10, "even_nonempty", "Hard"),
        (15, "3elem_mod3", "Hard"),       # {1..15}: 3*C(5,3) + 5^3 = 30 + 125 = 155!
    ]
    for v_i, (n_max, mode, diff) in enumerate(sub_cases):
        S_set = list(range(1, n_max + 1))
        if mode == "even_nonempty":
            ans = (2 ** (n_max - 1)) - 1
            bf = sum(1 for r in range(1, n_max + 1) for comb in itertools.combinations(S_set, r) if sum(comb) % 2 == 0)
            assert ans == bf
            distractors = [2 ** (n_max - 1), 2 ** n_max - 1, ans - 1, 2 ** (n_max // 2) - 1]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_sub_{v_i}")
            q_en = f"How many **non-empty subsets** of {m(f'\\{{1, 2, 3, \\dots, {n_max}\\}}')} have an **even** sum of elements?"
            q_ar = f"كم **مجموعة جزئية غير خالية** من المجموعة {m(f'\\{{1, 2, 3, \\dots, {n_max}\\}}')} يكون مجموع عناصرها **زوجياً**؟"
            h_en = "Set aside the number 1 as a 'parity switch'! For ANY choice of the remaining elements {2..n}, toggling '1' in or out makes the sum even in EXACTLY one way!"
            h_ar = "اجعل العدد 1 «مفتاحاً للزوجية»! لأي اختيار من العناصر المتبقية {2..n}، إما إدخال 1 أو عدم إدخاله يجعل المجموع زوجياً بطريقة وحيدة!"
            s_en = explain_en(
                f"Because {m(f'\\{{1, \\dots, {n_max}\\}}')} contains at least one odd number ({m(1)}), **exactly half** of all {m(f'2^{{{n_max}}}')} subsets have an even sum!",
                [
                    f"Freely choose whether each of {m(f'2, 3, \\dots, {n_max}')} is included ({m(f'2^{{{n_max - 1}}} = {2**(n_max-1)}')} ways). Then {m(1)} is **forced** (include {m(1)} if the partial sum is odd; omit {m(1)} if even!).",
                    f"That gives {m(2**(n_max-1))} subsets with even sum (including the empty set, whose sum is {m(0)}).",
                    f"Subtract the {m(1)} empty subset: {m(f'{2**(n_max-1)} - 1 = {ans}')}.",
                ],
                f"Trap check: don't forget to subtract {m(1)} for the **non-empty** requirement!",
            )
            s_ar = explain_ar(
                f"بما أن المجموعة تحتوي على عدد فردي واحد على الأقل ({m(1)})، فإن **نصف** جميع المجموعات الجزئية بالضبط مجموعها زوجي!",
                [
                    f"نختار بحرية من العناصر {m(f'2, 3, \\dots, {n_max}')} بـ {m(f'2^{{{n_max-1}}} = {2**(n_max-1)}')} طريقة، ثم يتحدد مصير العنصر {m(1)} تلقائياً ليضبط زوجية المجموع!",
                    f"ينتج {m(2**(n_max-1))} مجموعة جزئية مجموعها زوجي (بما فيها المجموعة الخالية التي مجموعها 0).",
                    f"نطرح المجموعة الخالية ({m(1)}): {m(f'{2**(n_max-1)} - 1 = {ans}')}.",
                ],
                f"انتبه لشرط «غير خالية»: طرح 1 ضروري لاستبعاد المجموعة الخالية!",
            )
        else:
            k_grp = n_max // 3
            same_res = 3 * math.comb(k_grp, 3)
            diff_res = k_grp ** 3
            ans = same_res + diff_res
            bf = sum(1 for comb in itertools.combinations(S_set, 3) if sum(comb) % 3 == 0)
            assert ans == bf
            distractors = [diff_res, math.comb(n_max, 3) // 3 if math.comb(n_max, 3) // 3 != ans else ans + 3, ans - same_res // 3 if same_res > 0 else ans + 4, ans + k_grp]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_sub_{v_i}")
            q_en = f"How many **{m(3)}-element subsets** of {m(f'\\{{1, 2, 3, \\dots, {n_max}\\}}')} have a sum **divisible by {m(3)}**?"
            q_ar = f"كم **مجموعة جزئية ثلاثية** (مكوّنة من {m(3)} عناصر) من المجموعة {m(f'\\{{1, 2, 3, \\dots, {n_max}\\}}')} يقبل مجموع عناصرها **القسمة على {m(3)}**؟"
            h_en = f"Group {{1..{n_max}}} by remainder mod 3 into 3 buckets of size {k_grp} each! Three remainders sum to 0 (mod 3) iff they are ALL THE SAME or ALL DIFFERENT!"
            h_ar = f"صنّف الأعداد حسب باقي قسمتها على 3 إلى 3 سلال حجم كل منها {k_grp}! مجموع 3 بواقٍ يقبل القسمة على 3 إذا كانت البواقي **كلها متماثلة** أو **كلها مختلفة**!"
            s_en = explain_en(
                f"Split \\( \\{{1..{n_max}\\}} \\) by remainder mod 3 into 3 equal buckets (remainders \\( 0, 1, 2 \\)), each holding **{m(k_grp)}** numbers.",
                [
                    f"Case 1 (all 3 from the **same** bucket: {m('0+0+0')}, {m('1+1+1')}, or {m('2+2+2')}): {m(f'3 \\times \\binom{{{k_grp}}}{{3}} = {same_res}')} ways.",
                    f"Case 2 (one from **each** bucket: {m('0 + 1 + 2 = 3')}): {m(f'{k_grp} \\times {k_grp} \\times {k_grp} = {diff_res}')} ways.",
                    f"Add both disjoint cases: {m(f'{same_res} + {diff_res} = {ans}')}.",
                ],
                f"Exact check across all {m(math.comb(n_max, 3))} triples confirms {m(ans)} valid subsets!",
            )
            s_ar = explain_ar(
                f"نقسّم الأعداد من 1 إلى {m(n_max)} حسب باقي قسمتها على 3 إلى 3 مجموعات متساوية (البواقي 0، 1، 2)، في كلٍّ منها **{m(k_grp)}** أعداد.",
                [
                    f"الحالة 1 (الأعداد الثلاثة من **نفس المجموعة**): {m(f'3 \\times \\binom{{{k_grp}}}{{3}} = {same_res}')} طريقة.",
                    f"الحالة 2 (عدد واحد من **كل مجموعة** لأن {m('0+1+2=3')}): {m(f'{k_grp}^3 = {diff_res}')} طريقة.",
                    f"نجمع الحالتين: {m(f'{same_res} + {diff_res} = {ans}')}.",
                ],
                f"بالتحقق من جميع الثلاثيات البالغ عددها {m(math.comb(n_max, 3))} نجد {m(ans)} ثلاثية بالضبط!",
            )
        push("Combinatorics & Logic", diff, "kmc_g1011_subset_sum_parity_div", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 9. Committee selection with incompatible or inseparable pair (10 Qs)
    # ------------------------------------------------------------------
    com_cases = [
        (7, 3, "apart", "Easy"),
        (8, 3, "apart", "Easy"),
        (8, 4, "apart", "Medium"),
        (9, 4, "apart", "Medium"),
        (10, 3, "apart", "Medium"),
        (7, 3, "together", "Easy"),
        (8, 4, "together", "Medium"),
        (9, 3, "together", "Medium"),
        (10, 4, "apart", "Hard"),
        (10, 4, "together", "Hard"),
    ]
    for v_i, (n_p, k_sel, rule, diff) in enumerate(com_cases):
        tot_c = math.comb(n_p, k_sel)
        both_c = math.comb(n_p - 2, k_sel - 2)
        neither_c = math.comb(n_p - 2, k_sel)
        if rule == "apart":
            ans = tot_c - both_c
            distractors = [tot_c, neither_c, ans - both_c, tot_c - 2]
            q_en = (
                f"A KAUST math team of {m(k_sel)} students is to be chosen from {m(n_p)} finalists. "
                f"Two twins, Sarah and Nora, **cannot both be on the team together** (at most one of them can be chosen). "
                f"How many valid teams of {m(k_sel)} can be formed?"
            )
            q_ar = (
                f"يُراد اختيار فريق رياضيات مكوّن من {m(k_sel)} طلاب من بين {m(n_p)} مرشحين. "
                f"إذا لم يكن مسموحاً باختيار سارة ونورة **معاً في الفريق نفسه** (يمكن اختيار إحداهما على الأكثر أو عدم اختيار أي منهما)، "
                f"فكم فريقاً صالحاً يمكن تكوينه؟"
            )
            steps_en = [
                f"Total unrestricted teams of {m(k_sel)} from {m(n_p)}: {m(f'\\binom{{{n_p}}}{{{k_sel}}} = {tot_c}')}.",
                f"Forbidden teams (containing **both** Sarah and Nora, plus {m(k_sel - 2)} of the remaining {m(n_p - 2)} finalists): {m(f'\\binom{{{n_p - 2}}}{{{k_sel - 2}}} = {both_c}')}.",
                f"Subtract forbidden from total: {m(f'{tot_c} - {both_c} = {ans}')}.",
            ]
            steps_ar = [
                f"إجمالي الفِرق بدون شروط: {m(f'\\binom{{{n_p}}}{{{k_sel}}} = {tot_c}')}.",
                f"الفِرق الممنوعة (التي تضم سارة ونورة **معاً** بالإضافة إلى {m(k_sel - 2)} من الـ {m(n_p - 2)} الباقين): {m(f'\\binom{{{n_p - 2}}}{{{k_sel - 2}}} = {both_c}')}.",
                f"نطرح الممنوع من الكلي: {m(f'{tot_c} - {both_c} = {ans}')}.",
            ]
        else:
            ans = both_c + neither_c
            distractors = [both_c, neither_c, tot_c - both_c, tot_c]
            q_en = (
                f"A committee of {m(k_sel)} students is chosen from {m(n_p)} candidates. "
                f"Best friends Omar and Ali insist on **either serving together or neither of them serving**. "
                f"How many valid committees of {m(k_sel)} can be formed?"
            )
            q_ar = (
                f"تُختار لجنة من {m(k_sel)} طلاب من بين {m(n_p)} مرشحين. "
                f"يشترط الصديقان عمر وعلي **إما أن يُختارا معاً في اللجنة أو ألا يُختار أيٌّ منهما**. "
                f"كم لجنة صالحة يمكن تكوينها؟"
            )
            steps_en = [
                f"Case 1 (**Both** Omar and Ali are chosen): pick the remaining {m(k_sel - 2)} members from the other {m(n_p - 2)} candidates → {m(f'\\binom{{{n_p - 2}}}{{{k_sel - 2}}} = {both_c}')} ways.",
                f"Case 2 (**Neither** Omar nor Ali is chosen): pick all {m(k_sel)} members from the other {m(n_p - 2)} candidates → {m(f'\\binom{{{n_p - 2}}}{{{k_sel}}} = {neither_c}')} ways.",
                f"Add both disjoint cases: {m(f'{both_c} + {neither_c} = {ans}')}.",
            ]
            steps_ar = [
                f"الحالة 1 (اختيار عمر وعلي **معاً**): نختار {m(k_sel - 2)} أعضاء من الـ {m(n_p - 2)} الباقين ← {m(f'\\binom{{{n_p - 2}}}{{{k_sel - 2}}} = {both_c}')} طريقة.",
                f"الحالة 2 (**عدم** اختيار أيٍّ منهما): نختار الأعضاء الـ {m(k_sel)} جميعاً من الـ {m(n_p - 2)} الباقين ← {m(f'\\binom{{{n_p - 2}}}{{{k_sel}}} = {neither_c}')} طريقة.",
                f"نجمع الحالتين المنفصلتين: {m(f'{both_c} + {neither_c} = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_com_{v_i}")
        h_en = "Freeze the two special people first: count committees containing BOTH of them (choose k−2 from n−2) and/or NEITHER (choose k from n−2)!"
        h_ar = "ثبّت وضع الشخصين الخاصين أولاً: احسب اللجان التي تضمهما معاً (اختيار k−2 من n−2) أو تخلو منهما (اختيار k من n−2)!"
        s_en = explain_en("Conditioning on the special pair breaks any restricted combination problem into clean, smaller binomial coefficients!", steps_en, f"Recall \\( \\binom{{n}}{{r}} = \\frac{{n!}}{{r!(n-r)!}} \\).")
        s_ar = explain_ar("تفصيل الحالات وفق وضع الشخصين المشروطين يحوّل المسألة إلى توافيق بسيطة ومباشرة!", steps_ar, f"تذكّر قانون التوافيق \\( \\binom{{n}}{{r}} = \\frac{{n!}}{{r!(n-r)!}} \\).")
        push("Combinatorics & Logic", diff, "kmc_g1011_committee_incompatible", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 10. Unequal-sector spinner spun twice independently (10 Qs, SVG!)
    # ------------------------------------------------------------------
    spin_cases = [
        # (sectors=[(frac, num_val), ...], cond_en, cond_ar, pred_fn, diff)
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 4), 3)], "the two spins land on the **same number**", "أن يقف المؤشر على **الرقم نفسه** في المرتين", lambda a, b: a == b, "Easy"),
        ([(Fraction(1, 2), 1), (Fraction(1, 3), 2), (Fraction(1, 6), 3)], "the two spins land on the **same number**", "أن يقف المؤشر على **الرقم نفسه** في المرتين", lambda a, b: a == b, "Easy"),
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 4), 3)], "the **sum** of the two numbers is 4", "أن يكون **مجموع** الرقمين 4", lambda a, b: a + b == 4, "Easy"),
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 8), 3), (Fraction(1, 8), 4)], "the **sum** of the two numbers is 5", "أن يكون **مجموع** الرقمين 5", lambda a, b: a + b == 5, "Medium"),
        ([(Fraction(1, 2), 2), (Fraction(1, 3), 3), (Fraction(1, 6), 5)], "the **sum** of the two numbers is even", "أن يكون **مجموع** الرقمين زوجياً", lambda a, b: (a + b) % 2 == 0, "Medium"),
        ([(Fraction(1, 2), 1), (Fraction(1, 3), 2), (Fraction(1, 6), 4)], "the **product** of the two numbers is 4", "أن يكون **حاصل ضرب** الرقمين 4", lambda a, b: a * b == 4, "Medium"),
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 4), 3)], "the **second** number is strictly greater than the **first**", "أن يكون الرقم **الثاني** أكبر تماماً من الرقم **الأول**", lambda a, b: b > a, "Medium"),
        ([(Fraction(1, 2), 1), (Fraction(1, 3), 2), (Fraction(1, 6), 3)], "the **second** number is strictly greater than the **first**", "أن يكون الرقم **الثاني** أكبر تماماً من الرقم **الأول**", lambda a, b: b > a, "Hard"),
        ([(Fraction(1, 2), 1), (Fraction(1, 4), 2), (Fraction(1, 8), 3), (Fraction(1, 8), 4)], "the two spins land on the **same number**", "أن يقف المؤشر على **الرقم نفسه** في المرتين", lambda a, b: a == b, "Hard"),
        ([(Fraction(1, 2), 2), (Fraction(1, 4), 3), (Fraction(1, 4), 6)], "the **product** of the two numbers is divisible by 6", "أن يقبل **حاصل ضرب** الرقمين القسمة على 6", lambda a, b: (a * b) % 6 == 0, "Hard"),
    ]
    for v_i, (secs, cond_en, cond_ar, pred, diff) in enumerate(spin_cases):
        svg = svg_spinner([(float(f), str(v)) for f, v in secs])
        ans = Fraction(0, 1)
        hit_terms = []
        for f1, v1 in secs:
            for f2, v2 in secs:
                if pred(v1, v2):
                    ans += f1 * f2
                    hit_terms.append(f"({v1},{v2}): {fmt_val(f1)}\\cdot{fmt_val(f2)}={fmt_val(f1*f2)}")
        # Trap: treating sectors as equally likely!
        n_s = len(secs)
        eq_fav = sum(1 for _, v1 in secs for _, v2 in secs if pred(v1, v2))
        trap_eq = Fraction(eq_fav, n_s * n_s)
        distractors = [
            trap_eq if trap_eq != ans else Fraction(ans.numerator + 1, ans.denominator),
            Fraction(1, 2) if ans != Fraction(1, 2) else Fraction(3, 8),
            Fraction(max(1, ans.numerator - 1), ans.denominator),
            Fraction(min(ans.denominator - 1, ans.numerator + 1), ans.denominator),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_spn_{v_i}")
        sec_desc_en = ", ".join(f"sector {m(v)} covers {m(fmt_val(f))} of the circle" for f, v in secs)
        sec_desc_ar = "، و".join(f"القطاع {m(v)} يمثّل {m(fmt_val(f))} الدائرة" for f, v in secs)
        q_en = (
            f"On the circular spinner shown, {sec_desc_en}. "
            f"The pointer is spun **twice** independently. What is the probability that {cond_en}?"
        )
        q_ar = (
            f"في القرص الدوّار الموضح، {sec_desc_ar}. "
            f"أُدير المؤشر **مرتين** مستقلتين. ما احتمال {cond_ar}؟"
        )
        h_en = "Sectors have UNEQUAL sizes! Multiply P(first = a) × P(second = b) for every favorable ordered pair (a, b), then add!"
        h_ar = "القطاعات **غير متساوية** المساحة! اضرب احتمال الأول × احتمال الثاني لكل زوج مرتب يحقق الشرط، ثم اجمع الاحتمالات!"
        s_en = explain_en(
            "Because the two spins are independent, \\( P(\\text{first}=a \\text{ and } \\text{second}=b) = P(a) \\times P(b) \\), weighted by each sector's fraction of the circle!",
            [
                f"List all favorable ordered pairs {m('(a, b)')} and multiply their sector probabilities: {m(';\\; '.join(hit_terms[:5]))}{'...' if len(hit_terms)>5 else ''}.",
                f"Sum those probabilities and simplify to get **{m(fmt_val(ans))}**.",
            ],
            "Trap avoided: never divide favorable pair count by n² when the spinner sectors have different areas!",
        )
        s_ar = explain_ar(
            "بما أن الدورتين مستقلتان، فإن احتمال الزوج المرتب \\( (a, b) \\) يساوي \\( P(a) \\times P(b) \\) بحسب كسر مساحة كل قطاع!",
            [
                f"نحدد جميع الأزواج المرتبة التي تحقق الشرط ونضرب احتمالاتها: {m(';\\; '.join(hit_terms[:5]))}{'...' if len(hit_terms)>5 else ''}.",
                f"بجمع هذه الاحتمالات وتبسيط الكسر نحصل على **{m(fmt_val(ans))}**.",
            ],
            "تجنبنا الفخ الشائع: لا نقسم على مربع عدد القطاعات لأن مساحات القطاعات غير متساوية!",
        )
        push("Data & Probability", diff, "kmc_g1011_spinner_two_spins", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 11. Bar chart: 5th bar raises/changes the 4-bar average by d (10 Qs, SVG!)
    # ------------------------------------------------------------------
    b5_cases = [
        ([12, 16, 14, 18], 2, "Easy"),     # avg4 = 15, avg5 = 17 -> sum5 = 85 -> ? = 25
        ([10, 14, 18, 14], 3, "Easy"),     # avg4 = 14, avg5 = 17 -> ? = 29
        ([20, 24, 18, 22], 2, "Easy"),     # avg4 = 21, avg5 = 23 -> ? = 31
        ([15, 21, 18, 26], 3, "Medium"),   # avg4 = 20, avg5 = 23 -> ? = 35
        ([25, 30, 22, 27], 4, "Medium"),   # avg4 = 26, avg5 = 30 -> ? = 46
        ([32, 28, 36, 24], -2, "Medium"),  # avg4 = 30, avg5 = 28 -> ? = 20
        ([40, 35, 45, 32], 3, "Medium"),   # avg4 = 38, avg5 = 41 -> ? = 53
        ([18, 27, 24, 31], 4, "Medium"),   # avg4 = 25, avg5 = 29 -> ? = 45
        ([50, 42, 48, 44], -3, "Hard"),    # avg4 = 46, avg5 = 43 -> ? = 31
        ([36, 44, 38, 50], 5, "Hard"),     # avg4 = 42, avg5 = 47 -> ? = 67
    ]
    days_lbl = ["Sun", "Mon", "Tue", "Wed", "Thu"]
    for v_i, (v4, d_chg, diff) in enumerate(b5_cases):
        s4 = sum(v4)
        assert s4 % 4 == 0
        avg4 = s4 // 4
        avg5 = avg4 + d_chg
        s5 = 5 * avg5
        ans = s5 - s4
        assert ans == avg4 + 5 * d_chg
        bars = [(days_lbl[i], v4[i], str(v4[i])) for i in range(4)] + [("Thu", ans, "?")]
        svg = svg_bar_chart(bars)
        distractors = [avg4 + d_chg, avg4 + 4 * d_chg, ans + d_chg, ans - 2 * d_chg]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3c_b5_{v_i}")
        chg_en = f"**increases** the daily average by {m(d_chg)}" if d_chg > 0 else f"**decreases** the daily average by {m(abs(d_chg))}"
        chg_ar = f"**يرفع** المتوسط اليومي بمقدار {m(d_chg)}" if d_chg > 0 else f"**يُخفض** المتوسط اليومي بمقدار {m(abs(d_chg))}"
        q_en = (
            f"The bar chart records the number of problems solved by a club from Sunday to Wednesday ({m(v4[0])}, {m(v4[1])}, {m(v4[2])}, and {m(v4[3])}), "
            f"while Thursday's bar is marked {m('?')}. Including Thursday's count {chg_en} (compared to the 4-day Sunday–Wednesday average). "
            f"What is Thursday's count {m('?')}?"
        )
        q_ar = (
            f"يسجّل التمثيل بالأعمدة عدد المسائل التي حلّها نادٍ رياضي من الأحد إلى الأربعاء ({m(v4[0])} و{m(v4[1])} و{m(v4[2])} و{m(v4[3])})، "
            f"بينما عمود الخميس مجهول {m('?')}. إذا كان إدراج عدد يوم الخميس {chg_ar} (مقارنةً بمتوسط الأيام الأربعة الأولى)، "
            f"فما عدد مسائل يوم الخميس {m('?')}؟"
        )
        h_en = f"Find the 4-day sum ({s4}) and 4-day average ({avg4}) first, then compute the new 5-day sum = 5 × {avg5}!"
        h_ar = f"احسب مجموع الأيام الأربعة ({s4}) ومتوسطها ({avg4}) أولاً، ثم احسب مجموع الأيام الخمسة = 5 × {avg5}!"
        s_en = explain_en(
            "Always translate average changes into **total sums**: \\( \\text{Thursday} = (\\text{5-day sum}) - (\\text{4-day sum}) \\)!",
            [
                f"4-day sum: {m(' + '.join(str(x) for x in v4) + f' = {s4}')}, so 4-day average = {m(f'{s4} \\div 4 = {avg4}')}.",
                f"New 5-day average = {m(f'{avg4} {("+" if d_chg>0 else "-")} {abs(d_chg)} = {avg5}')}, giving 5-day sum = {m(f'5 \\times {avg5} = {s5}')}.",
                f"Subtract: {m(f'? = {s5} - {s4} = {ans}')}.",
            ],
            f"Mental-math shortcut: to shift all 5 days' average by {m(d_chg)}, Thursday must equal {m(f'{avg4} + 5({d_chg}) = {ans}')}!",
        )
        s_ar = explain_ar(
            "نحوّل تغير المتوسط دائماً إلى **مجموع كلي**: قيمة الخميس = (مجموع 5 أيام) − (مجموع 4 أيام)!",
            [
                f"مجموع 4 أيام: {m(s4)}، ومتوسطها = {m(f'{s4} \\div 4 = {avg4}')}.",
                f"متوسط 5 أيام الجديد = {m(avg5)}، ومجموع 5 أيام = {m(f'5 \\times {avg5} = {s5}')}.",
                f"نطرح: {m(f'? = {s5} - {s4} = {ans}')}.",
            ],
            f"اختصار ذهني سريع: لتغيير متوسط 5 أيام بمقدار {m(d_chg)} يجب أن تساوي القيمة الخامسة {m(f'{avg4} + 5({d_chg}) = {ans}')}!",
        )
        push("Data & Probability", diff, "kmc_g1011_bar_chart_two_missing", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    assert len(out) == 110, f"Expected 110, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 3 Combinatorics & Probability questions cleanly.")
