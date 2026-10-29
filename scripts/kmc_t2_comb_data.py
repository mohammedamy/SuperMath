"""Track 2 (Grades 8-9) — Combinatorics, Logic & Data/Probability (110 authentic KMC problems)."""
from collections import deque
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
    svg_number_triangle_puzzle,
    svg_travel_map,
    svg_water_cups,
)

LEVEL = "Track 2: Grades 8-9"


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(topic, diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en=None, svg_ar=None):
        nonlocal idx
        qid = f"KMC-T2-CMB-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, topic, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg_en, svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 1. Shortest travel time on weighted map via required stop (KMC Junior Q12!) (10 Qs)
    # ------------------------------------------------------------------
    map_cases = [
        # (stop_en, stop_ar, edges: (S-A, S-M, S-B, A-M, B-M, M-T, A-T, B-T), diff)
        ("Bakery", "المخبز", (6, 12, 7, 4, 6, 9, 11, 10), "Easy"),
        ("Library", "المكتبة", (8, 13, 7, 3, 5, 8, 9, 10), "Easy"),
        ("Bookshop", "متجر الكتب", (5, 11, 8, 4, 2, 10, 8, 7), "Easy"),
        ("Pharmacy", "الصيدلية", (9, 15, 8, 4, 5, 11, 10, 9), "Medium"),
        ("Post Office", "البريد", (7, 14, 6, 5, 5, 12, 9, 8), "Medium"),
        ("Cafe", "المقهى", (10, 16, 9, 4, 5, 13, 12, 11), "Medium"),
        ("Station", "المحطة", (8, 15, 9, 5, 4, 14, 11, 9), "Medium"),
        ("Museum", "المتحف", (11, 18, 9, 5, 6, 15, 13, 11), "Medium"),
        ("Clinic", "العيادة", (9, 17, 10, 6, 4, 16, 12, 11), "Hard"),
        ("Market", "السوق", (12, 19, 10, 5, 6, 17, 14, 12), "Hard"),
    ]
    for v_i, (stop_en, stop_ar, wts, diff) in enumerate(map_cases):
        w_sa, w_sm, w_sb, w_am, w_bm, w_mt, w_at, w_bt = wts
        edges = [
            ("S", "A", w_sa), ("S", "M", w_sm), ("S", "B", w_sb),
            ("A", "M", w_am), ("B", "M", w_bm),
            ("M", "T", w_mt), ("A", "T", w_at), ("B", "T", w_bt),
        ]
        # Exact shortest S -> M and M -> T on undirected graph
        adj = {k: [] for k in ("S", "A", "M", "B", "T")}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dist(src, dst):
            best = {k: 10**9 for k in adj}
            best[src] = 0
            for _ in range(len(adj)):
                for u in adj:
                    for v, w in adj[u]:
                        if best[u] + w < best[v]:
                            best[v] = best[u] + w
            return best[dst]

        d_sm = dist("S", "M")
        d_mt = dist("M", "T")
        ans = d_sm + d_mt
        d_direct_no_stop = dist("S", "T")
        svg_en = svg_travel_map(
            {"S": (170, 200, "Home"), "A": (65, 125, "Park"), "M": (170, 115, stop_en), "B": (275, 125, "Mall"), "T": (170, 28, "School")},
            edges,
        )
        svg_ar = svg_travel_map(
            {"S": (170, 200, "المنزل"), "A": (65, 125, "الحديقة"), "M": (170, 115, stop_ar), "B": (275, 125, "المول"), "T": (170, 28, "المدرسة")},
            edges,
        )
        distractors = [w_sm + w_mt, d_direct_no_stop, ans + 2, ans + 3, max(8, ans - 2)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_map_{v_i}")
        q_en = (
            f"The diagram shows the walking times (in minutes) along roads connecting Tariq's **Home**, **School**, and three landmarks. "
            f"Tariq walks from **Home** to **School**, and he **must visit the {stop_en}** on his way. "
            f"What is the **minimum possible walking time** (in minutes)?"
        )
        q_ar = (
            f"يوضّح المخطط أزمنة المشي (بالدقائق) عبر الطرق التي تربط **المنزل** و**المدرسة** وثلاثة معالم. "
            f"يمشي طارق من **المنزل** إلى **المدرسة**، ويجب عليه **المرور على {stop_ar}** في طريقه. "
            f"ما **أقل زمن مشي ممكن** (بالدقائق)؟"
        )
        h_en = f"Split the journey into two independent shortest-path subproblems: (1) Home → {stop_en}, plus (2) {stop_en} → School! Check indirect detours via Park or Mall!"
        h_ar = f"قسّم الرحلة إلى مسألتين مستقلتين لأقصر طريق: (1) من المنزل إلى {stop_ar}، ثم (2) من {stop_ar} إلى المدرسة! تحقّق من الطرق غير المباشرة!"
        s_en = explain_en(
            f"Because Tariq must visit the **{stop_en}**, we minimize the two legs **separately**: shortest time from Home to {stop_en}, plus shortest time from {stop_en} to School.",
            [
                f"Leg 1 (Home → {stop_en}): compare direct ({m(w_sm)}), via Park ({m(f'{w_sa}+{w_am}={w_sa+w_am}')}), and via Mall ({m(f'{w_sb}+{w_bm}={w_sb+w_bm}')}). Minimum is **{m(d_sm)}** min.",
                f"Leg 2 ({stop_en} → School): compare direct ({m(w_mt)}), via Park ({m(f'{w_am}+{w_at}={w_am+w_at}')}), and via Mall ({m(f'{w_bm}+{w_bt}={w_bm+w_bt}')}). Minimum is **{m(d_mt)}** min.",
                f"Add both optimal legs: {m(f'{d_sm} + {d_mt} = {ans}')} minutes.",
            ],
            f"Notice how a two-road path through Park or Mall can beat a slower 'direct' road!",
        )
        s_ar = explain_ar(
            f"بما أن طارقاً ملزم بزيارة **{stop_ar}**، نبحث عن أقصر زمن لكل مرحلة **على حدة**: من المنزل إلى {stop_ar}، ثم من {stop_ar} إلى المدرسة.",
            [
                f"المرحلة 1 (المنزل ← {stop_ar}): نقارن الطريق المباشر ({m(w_sm)})، وعبر الحديقة ({m(w_sa+w_am)})، وعبر المول ({m(w_sb+w_bm)}). الأصغر هو **{m(d_sm)}** دقائق.",
                f"المرحلة 2 ({stop_ar} ← المدرسة): نقارن الطريق المباشر ({m(w_mt)})، وعبر الحديقة ({m(w_am+w_at)})، وعبر المول ({m(w_bm+w_bt)}). الأصغر هو **{m(d_mt)}** دقائق.",
                f"نجمع المرحلتين المثليين: {m(f'{d_sm} + {d_mt} = {ans}')} دقيقة.",
            ],
            f"لاحظ أن الطريق المارّ بالحديقة أو المول قد يكون أسرع من الطريق المباشر الأبطأ!",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_travel_map_stop", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en, svg_ar)

    # ------------------------------------------------------------------
    # 2. Calculator two-button minimum presses (BFS verified) (10 Qs)
    # ------------------------------------------------------------------
    btn_cases = [
        (1, 19, 2, 3, "Easy"),    # 1 -> 4 -> 8 -> 16 -> 19 (4)
        (1, 23, 2, 3, "Easy"),    # 1 -> 4 -> 5? wait BFS gives exact!
        (2, 29, 2, 3, "Easy"),
        (1, 31, 2, 3, "Medium"),
        (1, 43, 2, 3, "Medium"),
        (1, 29, 2, 1, "Medium"),
        (2, 50, 2, 3, "Medium"),
        (1, 55, 2, 3, "Medium"),
        (2, 67, 2, 3, "Hard"),
        (1, 79, 2, 3, "Hard"),
    ]
    for v_i, (start, target, mul_k, add_c, diff) in enumerate(btn_cases):
        # Exact BFS with parent pointers
        q = deque([start])
        parent = {start: None}
        while q:
            u = q.popleft()
            if u == target:
                break
            for nxt in (u * mul_k, u + add_c):
                if nxt <= target + 20 and nxt not in parent:
                    parent[nxt] = u
                    q.append(nxt)
        path = []
        cur = target
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        ans = len(path) - 1
        chain_str = " \\to ".join(str(x) for x in path)
        distractors = [ans + 1, ans + 2, max(2, ans - 1), ans + 3]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_btn_{v_i}")
        q_en = (
            f"A special toy calculator starts displaying {m(start)} and has only two buttons: "
            f"**Button A** multiplies the current number by {m(mul_k)}, and **Button B** adds {m(add_c)} to the current number. "
            f"What is the **minimum number of button presses** needed to display {m(target)}?"
        )
        q_ar = (
            f"تعرض آلة حاسبة تعليمية العدد {m(start)} في البداية ولها زرّان فقط: "
            f"**الزر A** يضرب العدد الحالي في {m(mul_k)}، و**الزر B** يضيف {m(add_c)} إلى العدد الحالي. "
            f"ما **أقل عدد من الضغطات** للوصول إلى العدد {m(target)}؟"
        )
        h_en = f"Work BACKWARDS from {target} down to {start}! Whenever the number is odd, the last button pressed MUST have been '+{add_c}'!"
        h_ar = f"اعمل **عكسياً** من {target} رجوعاً إلى {start}! كلما كان العدد فردياً، فإن آخر ضغطة لا بد أنها كانت «+{add_c}»!"
        s_en = explain_en(
            f"Working **backwards** from {m(target)} to {m(start)} (using {m(f'\\div {mul_k}')} when even and {m(f'- {add_c}')} when odd) quickly finds the shortest sequence!",
            [
                f"Undo operations from {m(target)} down to {m(start)} to get the shortest forward chain: {m(chain_str)}.",
                f"Count the transitions (arrows) in {m(chain_str)}: there are **{m(ans)}** button presses.",
            ],
            f"No shorter sequence exists because multiplying by {m(mul_k)} grows the number as fast as possible.",
        )
        s_ar = explain_ar(
            f"العمل **بطريقة عكسية** من {m(target)} رجوعاً إلى {m(start)} (بالقسمة على {m(mul_k)} عند الزوجي وطرح {m(add_c)} عند الفردي) يكشف أقصر مسار بسرعة!",
            [
                f"بتتبع العمليات عكسياً نحصل على أقصر سلسلة أمامية: {m(chain_str)}.",
                f"نعدّ الأسهم (الضغطات) في السلسلة فنجدها **{m(ans)}** ضغطات بالضبط.",
            ],
            f"لا يمكن الوصول بعدد أقل من {m(ans)} ضغطات بعد التحقق من جميع التفرعات الممكنة.",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_button_press_bfs", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 3. Adjacent / corner-sharing cell pairs on m x n grid (10 Qs)
    # ------------------------------------------------------------------
    grid_cases = [
        (3, 4, "edge", "Easy"),
        (4, 4, "edge", "Easy"),
        (4, 5, "edge", "Easy"),
        (5, 6, "edge", "Medium"),
        (6, 8, "edge", "Medium"),
        (3, 4, "diag", "Medium"),
        (4, 5, "diag", "Medium"),
        (5, 5, "diag", "Medium"),
        (6, 7, "diag", "Hard"),
        (8, 8, "edge", "Hard"),
    ]
    for v_i, (rows, cols, mode, diff) in enumerate(grid_cases):
        if mode == "edge":
            h_pairs = rows * (cols - 1)
            v_pairs = (rows - 1) * cols
            ans = h_pairs + v_pairs
            distractors = [rows * cols, 2 * rows * cols, ans + rows, max(4, ans - cols)]
            q_en = (
                f"A board is divided into a {m(f'{rows} \\times {cols}')} grid of unit squares ({m(rows)} rows and {m(cols)} columns). "
                f"How many unordered pairs of unit squares **share a common side** (edge)?"
            )
            q_ar = (
                f"قُسِّمت لوحة إلى شبكة أبعادها {m(f'{rows} \\times {cols}')} من المربعات الصغيرة ({m(rows)} صفوف و{m(cols)} أعمدة). "
                f"كم زوجاً (غير مرتب) من المربعات الصغيرة **يشترك في ضلع كامل**؟"
            )
            steps_en = [
                f"Every pair sharing a vertical edge sits left-and-right in the same row: each of the {m(rows)} rows has {m(f'{cols} - 1 = {cols-1}')} such pairs, giving {m(f'{rows} \\times {cols-1} = {h_pairs}')}.",
                f"Every pair sharing a horizontal edge sits top-and-bottom in the same column: each of the {m(cols)} columns has {m(f'{rows} - 1 = {rows-1}')} such pairs, giving {m(f'{cols} \\times {rows-1} = {v_pairs}')}.",
                f"Add horizontal and vertical neighbors: {m(f'{h_pairs} + {v_pairs} = {ans}')}.",
            ]
            steps_ar = [
                f"كل زوج متجاور أفقياً يقع في نفس الصف: في كل صف من الصفوف الـ {m(rows)} يوجد {m(f'{cols} - 1 = {cols-1}')} أزواج، أي {m(f'{rows} \\times {cols-1} = {h_pairs}')}.",
                f"كل زوج متجاور رأسياً يقع في نفس العمود: في كل عمود من الأعمدة الـ {m(cols)} يوجد {m(f'{rows} - 1 = {rows-1}')} أزواج، أي {m(f'{cols} \\times {rows-1} = {v_pairs}')}.",
                f"نجمع الأزواج الأفقية والرأسية: {m(f'{h_pairs} + {v_pairs} = {ans}')}.",
            ]
        else:
            blocks_2x2 = (rows - 1) * (cols - 1)
            ans = 2 * blocks_2x2
            distractors = [blocks_2x2, rows * (cols - 1) + (rows - 1) * cols, ans + 4, max(2, ans - 2)]
            q_en = (
                f"On a {m(f'{rows} \\times {cols}')} grid of unit squares, how many unordered pairs of unit squares "
                f"**touch at a single corner point** (diagonally, without sharing an edge)?"
            )
            q_ar = (
                f"على شبكة أبعادها {m(f'{rows} \\times {cols}')} من المربعات الصغيرة، كم زوجاً (غير مرتب) من المربعات "
                f"**يلتقي في رأس واحد فقط قطرياً** (دون الاشتراك في ضلع)؟"
            )
            steps_en = [
                f"Look at any {m('2 \\times 2')} block inside the grid: it contains **exactly 2** diagonal pairs of unit squares (top-left with bottom-right, and top-right with bottom-left).",
                f"How many {m('2 \\times 2')} blocks fit inside a {m(f'{rows} \\times {cols}')} grid? Exactly {m(f'({rows}-1) \\times ({cols}-1) = {blocks_2x2}')} (one for each interior grid intersection!).",
                f"Multiply by {m(2)}: {m(f'2 \\times {blocks_2x2} = {ans}')} diagonal pairs.",
            ],
            steps_en = steps_en[0]
            steps_ar = [
                f"كل مربع {m('2 \\times 2')} داخل الشبكة يحتوي على **زوجين قطريين بالضبط** (أعلى يسار مع أسفل يمين، وأعلى يمين مع أسفل يسار).",
                f"عدد مربعات {m('2 \\times 2')} داخل شبكة {m(f'{rows} \\times {cols}')} يساوي {m(f'({rows}-1) \\times ({cols}-1) = {blocks_2x2}')} (بعدد نقاط التقاطع الداخلية!).",
                f"نضرب في {m(2)}: {m(f'2 \\times {blocks_2x2} = {ans}')} زوجاً قطرياً.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_grd_{v_i}")
        h_en = "Count the interior grid walls (for edge-sharing pairs) or the interior grid intersection points (each has 2 diagonal pairs)!"
        h_ar = "عُدّ الفواصل الداخلية للشبكة (للأزواج المشتركة في ضلع) أو نقاط التقاطع الداخلية (عند كل نقطة تقاطع داخلية زوجان قطريان)!"
        s_en = explain_en("Counting geometric features (interior borders or interior vertices) avoids double-counting any pair!", steps_en, f"Test on a tiny 2×2 grid: formula gives 4 edge pairs and 2 diagonal pairs — spot on!")
        s_ar = explain_ar("عدّ الفواصل الداخلية أو الرؤوس الداخلية للشبكة يمنع تكرار عدّ أي زوج مرتين!", steps_ar, f"للتحقق على شبكة صغيرة 2×2: تعطي القاعدة 4 أزواج جانبية وزوجين قطريين — صحيح تماماً!")
        push("Combinatorics & Logic", diff, "kmc_g89_grid_adjacent_pairs", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 4. Additive & Multiplicative number triangle puzzles (10 Qs, SVG!)
    # ------------------------------------------------------------------
    tri_cases = [
        # (a_top, b_bl, c_br, op, diff)
        (8, 5, 7, "+", "Easy"),
        (11, 6, 9, "+", "Easy"),
        (14, 9, 13, "+", "Easy"),
        (19, 12, 15, "+", "Medium"),
        (23, 14, 18, "+", "Medium"),
        (4, 3, 5, "*", "Easy"),
        (6, 4, 5, "*", "Medium"),
        (7, 3, 6, "*", "Medium"),
        (8, 5, 6, "*", "Hard"),
        (9, 4, 7, "*", "Hard"),
    ]
    for v_i, (va, vb, vc, op, diff) in enumerate(tri_cases):
        if op == "+":
            el, er, eb = va + vb, va + vc, vb + vc
            ans = va
            tot2 = el + er + eb
            svg = svg_number_triangle_puzzle("?", " ", " ", str(el), str(er), str(eb))
            distractors = [vb, vc, tot2 // 2, ans + 3]
            q_en = (
                f"In the number triangle shown, a positive number is hidden in each of the three corner circles, "
                f"and each rectangle on a side shows the **sum** of the two circles at its ends ({m(el)}, {m(er)}, and {m(eb)}). "
                f"What number belongs in the top circle {m('?')}?"
            )
            q_ar = (
                f"في مثلث الأعداد الموضح، يوضع عدد موجب في كل دائرة عند الرؤوس الثلاثة، "
                f"ويعرض كل مستطيل على ضلع **مجموع** الدائرتين في طرفيه ({m(el)} و{m(er)} و{m(eb)}). "
                f"ما العدد الذي يوضع في الدائرة العلوية {m('?')}؟"
            )
            steps_en = [
                f"Call the top, bottom-left, and bottom-right circles {m('x, y, z')}. Then {m(f'x+y={el}')}, {m(f'x+z={er}')}, and {m(f'y+z={eb}')}.",
                f"Add the two top-connected edges and subtract the bottom edge: {m(f'(x+y) + (x+z) - (y+z) = 2x')}.",
                f"So {m(f'2x = {el} + {er} - {eb} = {2*va} \\implies x = {ans}')}.",
            ]
            steps_ar = [
                f"نرمز للدوائر العلوية والسفلية اليسرى والسفلية اليمنى بالرموز {m('x, y, z')}: إذن {m(f'x+y={el}')} و{m(f'x+z={er}')} و{m(f'y+z={eb}')}.",
                f"نجمع الضلعين العلويين ونطرح الضلع السفلي فتختفي {m('y')} و{m('z')}: {m(f'(x+y) + (x+z) - (y+z) = 2x')}.",
                f"إذن {m(f'2x = {el} + {er} - {eb} = {2*va} \\implies x = {ans}')}.",
            ]
        else:
            el, er, eb = va * vb, va * vc, vb * vc
            ans = va
            svg = svg_number_triangle_puzzle("?", " ", " ", str(el), str(er), str(eb))
            distractors = [vb, vc, ans + 2, max(2, ans - 2)]
            q_en = (
                f"Positive integers are placed in the three corner circles of the triangle shown. "
                f"Each rectangle on an edge shows the **product** of the two corner circles on that edge ({m(el)}, {m(er)}, and {m(eb)}). "
                f"What positive integer goes in the top circle {m('?')}?"
            )
            q_ar = (
                f"وُضعت أعداد صحيحة موجبة في الدوائر الثلاث عند رؤوس المثلث الموضح. "
                f"يعرض كل مستطيل على ضلع **حاصل ضرب** الدائرتين الواقعتين على طرفيه ({m(el)} و{m(er)} و{m(eb)}). "
                f"ما العدد الصحيح الموجب الذي يوضع في الدائرة العلوية {m('?')}؟"
            )
            steps_en = [
                f"Let the circles be {m('x, y, z')} (with {m('x')} on top). Then {m(f'xy = {el}')}, {m(f'xz = {er}')}, and {m(f'yz = {eb}')}.",
                f"Multiply the two top edges and divide by the bottom edge: {m(f'\\frac{{(xy)(xz)}}{{yz}} = x^2')}.",
                f"Compute {m(f'x^2 = \\frac{{{el} \\times {er}}}{{{eb}}} = {va*va}')}, so {m(f'x = {ans}')} (since {m('x > 0')}).",
            ]
            steps_ar = [
                f"نفرض الأعداد في الدوائر {m('x, y, z')} (حيث {m('x')} في الأعلى)، فيكون {m(f'xy = {el}')} و{m(f'xz = {er}')} و{m(f'yz = {eb}')}.",
                f"نضرب الضلعين العلويين ونقسم على الضلع السفلي لاختصار {m('yz')}: {m(f'\\frac{{(xy)(xz)}}{{yz}} = x^2')}.",
                f"نحسب {m(f'x^2 = \\frac{{{el} \\times {er}}}{{{eb}}} = {va*va}')}، ومنه {m(f'x = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_ntri_{v_i}")
        h_en = "Combine the two edges touching '?' and cancel out the opposite bottom edge (by subtracting for sums, or dividing for products)!"
        h_ar = "ادمج الضلعين المتصلين بالدائرة العلوية «?» وتخلّص من الضلع السفلي المقابل (بالطرح في حالة الجمع، أو بالقسمة في حالة الضرب)!"
        s_en = explain_en("Symmetry cancels the two bottom corners immediately without solving three separate equations!", steps_en, f"Check all three corners: ({va}, {vb}, {vc}) reproduce the three edge labels ({el}, {er}, {eb})!")
        s_ar = explain_ar("استغلال التماثل يختصر الدائرتين السفليتين دفعة واحدة دون الحاجة للتخمين!", steps_ar, f"تحقق من الرؤوس الثلاثة ({va}، {vb}، {vc}): تعطي القيم ({el}، {er}، {eb}) على الأضلاع بالضبط!")
        push("Combinatorics & Logic", diff, "kmc_g89_number_triangle_mult", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 5. Coin / banknote exact payment combinations (10 Qs)
    # ------------------------------------------------------------------
    coin_cases = [
        (2, 5, 25, "Easy"),
        (2, 5, 34, "Easy"),
        (3, 5, 30, "Easy"),
        (3, 7, 42, "Medium"),
        (5, 10, 85, "Medium"),
        (4, 5, 48, "Medium"),
        (3, 8, 55, "Medium"),
        (5, 7, 70, "Medium"),
        (4, 9, 80, "Hard"),
        (5, 8, 95, "Hard"),
    ]
    for v_i, (c1, c2, tot, diff) in enumerate(coin_cases):
        ways = [(x, (tot - c1 * x) // c2) for x in range(tot // c1 + 1) if (tot - c1 * x) % c2 == 0]
        ans = len(ways)
        assert ans >= 2
        distractors = [ans + 1, max(1, ans - 1), ans + 2, tot // (c1 + c2) + 3]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_coin_{v_i}")
        ys = [y for _, y in ways]
        y_list_str = ", ".join(str(y) for y in sorted(ys))
        q_en = (
            f"Lina wants to pay **exactly {m(tot)} SAR** using only {m(c1)}-SAR and {m(c2)}-SAR vouchers "
            f"(she may use zero of either type, and she has plenty of each). In how many different ways can she choose the number of each voucher?"
        )
        q_ar = (
            f"تريد لينا دفع مبلغ **{m(tot)} ريالاً بالضبط** باستخدام قسائم من فئتي {m(c1)} ريالات و{m(c2)} ريالات فقط "
            f"(ويمكنها استخدام صفر من أي فئة، ولديها عدد كافٍ من الفئتين). بكم طريقة مختلفة يمكنها اختيار أعداد القسائم؟"
        )
        h_en = f"Test the number y of {c2}-SAR vouchers! Once you find the smallest valid y ≥ 0, valid values of y jump in steps of {c1 // __import__('math').gcd(c1, c2)}!"
        h_ar = f"اختبر عدد قسائم فئة {c2} ريالات (y)! بمجرد إيجاد أصغر قيمة صالحة لـ y ≥ 0، تزداد قيم y الصالحة بقفزات منتظمة!"
        s_en = explain_en(
            f"We are counting non-negative integer solutions \\( (x, y) \\) to \\( {c1}x + {c2}y = {tot} \\), where \\( x, y \\ge 0 \\).",
            [
                f"Here {m('y')} can range from {m('0')} up to {m(f'\\lfloor {tot}/{c2} \\rfloor = {tot // c2}')}, and {m(f'{tot} - {c2}y')} must be divisible by {m(c1)}.",
                f"Checking which values of {m('y')} make {m(f'{tot} - {c2}y')} a multiple of {m(c1)}, the valid counts for {m('y')} are: {m(y_list_str)}.",
                f"Counting that list gives **{m(ans)}** different ways.",
            ],
            f"Notice how the valid values of {m('y')} form an arithmetic progression!",
        )
        s_ar = explain_ar(
            f"نعدّ الأزواج الصحيحة غير السالبة \\( (x, y) \\) التي تحقق \\( {c1}x + {c2}y = {tot} \\) حيث \\( x, y \\ge 0 \\).",
            [
                f"يمكن أن تأخذ {m('y')} قيماً من {m('0')} حتى {m(tot // c2)}، بشرط أن يقبل الباقي {m(f'{tot} - {c2}y')} القسمة على {m(c1)}.",
                f"بفحص القيم نجد أن قيم {m('y')} الصالحة هي: {m(y_list_str)}.",
                f"بعدد هذه القيم نحصل على **{m(ans)}** طرق مختلفة.",
            ],
            f"لاحظ أن قيم {m('y')} الصالحة تكوّن متتابعة حسابية منتظمة!",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_coin_denominations", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 6. Glass water cups multi-step fractional transfers (KMC Junior Q5!) (10 Qs, SVG!)
    # ------------------------------------------------------------------
    cup_cases = [
        # (init1, init2, init3, f12, f23, f31, ask_cup_1based, diff)
        (Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), 1, "Easy"),
        (Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 3), Fraction(1, 2), Fraction(1, 2), 1, "Easy"),
        (Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(2, 3), Fraction(1, 2), Fraction(1, 2), 3, "Easy"),
        (Fraction(1, 1), Fraction(1, 2), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), 2, "Medium"),
        (Fraction(3, 4), Fraction(1, 4), Fraction(0, 1), Fraction(1, 3), Fraction(1, 2), Fraction(1, 2), 1, "Medium"),
        (Fraction(1, 1), Fraction(1, 3), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), 3, "Medium"),
        (Fraction(4, 5), Fraction(0, 1), Fraction(1, 5), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), 1, "Medium"),
        (Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(3, 4), Fraction(2, 3), Fraction(1, 2), 1, "Medium"),
        (Fraction(2, 3), Fraction(1, 3), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2), Fraction(1, 3), 1, "Hard"),
        (Fraction(5, 6), Fraction(1, 6), Fraction(0, 1), Fraction(2, 5), Fraction(1, 2), Fraction(1, 2), 2, "Hard"),
    ]
    for v_i, (i1, i2, i3, f12, f23, f31, ask_c, diff) in enumerate(cup_cases):
        c1, c2, c3 = i1, i2, i3
        # Step 1: pour f12 of cup 1 into cup 2
        p1 = c1 * f12
        c1, c2 = c1 - p1, c2 + p1
        assert c2 <= 1
        s1_state = (c1, c2, c3)
        # Step 2: pour f23 of cup 2 into cup 3
        p2 = c2 * f23
        c2, c3 = c2 - p2, c3 + p2
        assert c3 <= 1
        s2_state = (c1, c2, c3)
        # Step 3: pour f31 of cup 3 into cup 1
        p3 = c3 * f31
        c3, c1 = c3 - p3, c1 + p3
        assert c1 <= 1
        final_state = (c1, c2, c3)
        ans = final_state[ask_c - 1]

        svg = svg_water_cups((float(i1), float(i2), float(i3)), ("Cup 1", "Cup 2", "Cup 3"))
        svg_ar = svg_water_cups((float(i1), float(i2), float(i3)), ("كوب 1", "كوب 2", "كوب 3"))
        distractors = [
            final_state[ask_c % 3],
            final_state[(ask_c + 1) % 3],
            Fraction(ans.numerator + 1, ans.denominator + 1),
            Fraction(max(1, ans.numerator), ans.denominator * 2),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_cup_{v_i}")
        q_en = (
            f"Three identical glasses start filled to fractions {m(fmt_val(i1))}, {m(fmt_val(i2))}, and {m(fmt_val(i3))} of capacity, respectively. "
            f"First, {m(fmt_val(f12))} of the water in Cup 1 is poured into Cup 2. "
            f"Second, {m(fmt_val(f23))} of the water now in Cup 2 is poured into Cup 3. "
            f"Third, {m(fmt_val(f31))} of the water now in Cup 3 is poured back into Cup 1. "
            f"What fraction of Cup {ask_c} is filled at the end?"
        )
        q_ar = (
            f"ثلاثة أكواب متطابقة مملوءة في البداية بالكسور {m(fmt_val(i1))} و{m(fmt_val(i2))} و{m(fmt_val(i3))} من سعتها على الترتيب. "
            f"أولاً، سُكب {m(fmt_val(f12))} الماء الموجود في الكوب 1 إلى الكوب 2. "
            f"ثانياً، سُكب {m(fmt_val(f23))} الماء الموجود الآن في الكوب 2 إلى الكوب 3. "
            f"ثالثاً، سُكب {m(fmt_val(f31))} الماء الموجود الآن في الكوب 3 عائداً إلى الكوب 1. "
            f"ما الكسر المملوء من الكوب {ask_c} في النهاية؟"
        )
        h_en = "Write a 3-number state tuple (Cup 1, Cup 2, Cup 3) after EVERY single pour so you never lose track!"
        h_ar = "اكتب ثلاثية الحالة (كوب 1، كوب 2، كوب 3) بعد **كل عملية سكب** خطوة بخطوة حتى لا تخلط بين الكسور!"
        s_en = explain_en(
            "Track all three cups as a state vector \\( (C_1, C_2, C_3) \\) after each pour, checking that the total water stays constant!",
            [
                f"After Pour 1 ({m(fmt_val(p1))} moved from Cup 1 → Cup 2): {m(f'({fmt_val(s1_state[0])},\\; {fmt_val(s1_state[1])},\\; {fmt_val(s1_state[2])})')}.",
                f"After Pour 2 ({m(fmt_val(p2))} moved from Cup 2 → Cup 3): {m(f'({fmt_val(s2_state[0])},\\; {fmt_val(s2_state[1])},\\; {fmt_val(s2_state[2])})')}.",
                f"After Pour 3 ({m(fmt_val(p3))} moved from Cup 3 → Cup 1): {m(f'({fmt_val(c1)},\\; {fmt_val(c2)},\\; {fmt_val(c3)})')}, so Cup {ask_c} has **{m(fmt_val(ans))}**.",
            ],
            f"Conservation check: \\( {fmt_val(c1)} + {fmt_val(c2)} + {fmt_val(c3)} = {fmt_val(i1+i2+i3)} \\), matching the starting total water!",
        )
        s_ar = explain_ar(
            "نتتبع كمية الماء في الأكواب الثلاثة \\( (C_1, C_2, C_3) \\) بعد كل خطوة، مع التأكد من ثبات مجموع الماء الكلي!",
            [
                f"بعد السكب الأول (انتقل {m(fmt_val(p1))} من كوب 1 إلى كوب 2): {m(f'({fmt_val(s1_state[0])},\\; {fmt_val(s1_state[1])},\\; {fmt_val(s1_state[2])})')}.",
                f"بعد السكب الثاني (انتقل {m(fmt_val(p2))} من كوب 2 إلى كوب 3): {m(f'({fmt_val(s2_state[0])},\\; {fmt_val(s2_state[1])},\\; {fmt_val(s2_state[2])})')}.",
                f"بعد السكب الثالث (انتقل {m(fmt_val(p3))} من كوب 3 إلى كوب 1): {m(f'({fmt_val(c1)},\\; {fmt_val(c2)},\\; {fmt_val(c3)})')}، إذن في الكوب {ask_c} الكسر **{m(fmt_val(ans))}**.",
            ],
            f"تحقق من حفظ الكمية: مجموع الكسور الثلاثة في النهاية يساوي {m(fmt_val(i1+i2+i3))} تماماً كما في البداية!",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_water_cups_transfer", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg, svg_ar)

    # ------------------------------------------------------------------
    # 7. Frequency bar chart: median & mean literacy (10 Qs, SVG!)
    # ------------------------------------------------------------------
    bar_cases = [
        # (counts for scores 1, 2, 3, 4, 5; ask: 'median' or 'mean'; diff)
        ([2, 5, 4, 2, 2], "median", "Easy"),       # N=15, 8th is 3
        ([3, 3, 6, 4, 3], "median", "Easy"),       # N=19, 10th is 3
        ([4, 6, 3, 2, 2], "median", "Easy"),       # N=17, 9th is 2
        ([1, 3, 4, 7, 4], "median", "Medium"),     # N=19, 10th is 4
        ([2, 4, 3, 5, 7], "median", "Medium"),     # N=21, 11th is 4
        ([2, 3, 2, 2, 1], "mean", "Medium"),       # N=10, sum = 2+6+6+8+5 = 27? wait let's pick integer or clean tenth: [1,3,2,3,1]->sum=30, N=10, mean=3!
        ([1, 4, 5, 6, 4], "mean", "Medium"),       # N=20, sum=1+8+15+24+20=68 -> 17/5=3.4
        ([4, 2, 4, 6, 4], "mean", "Medium"),       # N=20, sum=4+4+12+24+20=64 -> 3.2
        ([3, 7, 4, 3, 3], "diff_mm", "Hard"),      # N=20, sum=3+14+12+12+15=56 -> mean 2.8, median (10th=2,11th=3 -> 2.5), mean-med = 0.3
        ([2, 2, 6, 6, 4], "mean", "Hard"),         # N=20, sum=2+4+18+24+20=68 -> 3.4
    ]
    # Replace index 5 with clean integer mean [2, 2, 3, 2, 1] -> sum=2+4+9+8+5=28? [1, 3, 2, 3, 1] -> sum=30, N=10 -> 3!
    bar_cases[5] = ([1, 3, 2, 3, 1], "mean", "Medium")
    for v_i, (cnts, ask, diff) in enumerate(bar_cases):
        bars = [(str(sc), c, str(c)) for sc, c in enumerate(cnts, 1)]
        svg = svg_bar_chart(bars)
        data = []
        for sc, c in enumerate(cnts, 1):
            data.extend([sc] * c)
        N = len(data)
        tot_pts = sum(data)
        mean_v = Fraction(tot_pts, N)
        if N % 2 == 1:
            med_v = Fraction(data[N // 2], 1)
        else:
            med_v = Fraction(data[N // 2 - 1] + data[N // 2], 2)

        cnts_tex = ", ".join(str(c) for c in cnts)
        if ask == "median":
            ans = int(med_v) if med_v.denominator == 1 else float(med_v)
            # Distractor trap: median of the 5 bar heights sorted!
            trap_bar_med = sorted(cnts)[2]
            distractors = [trap_bar_med, ans + 1, max(1, ans - 1), ans + 2]
            q_en = (
                f"The bar chart shows how many books ({m('1')} to {m('5')}) each student in a club read last month, "
                f"with student counts {m(f'({cnts_tex})')} respectively. "
                f"What is the **median** number of books read per student?"
            )
            q_ar = (
                f"يوضّح التمثيل بالأعمدة عدد الكتب (من {m('1')} إلى {m('5')}) التي قرأها كل طالب في نادٍ ثقافي الشهر الماضي، "
                f"حيث أعداد الطلاب على الترتيب هي {m(f'({cnts_tex})')}. "
                f"ما **الوسيط** لعدد الكتب المقروءة لكل طالب؟"
            )
            mid_pos = (N + 1) // 2
            steps_en = [
                f"First find the total number of students by adding the bar heights: {m(' + '.join(str(c) for c in cnts) + f' = {N}')}.",
                f"With {m(N)} students ordered from least to most books, the median is the **{m(f'{mid_pos}\\text{{th}}')}** student's book count.",
                f"Accumulate counts from the left ({m('1')} book: {m(cnts[0])}; up to {m('2')} books: {m(cnts[0]+cnts[1])}; up to {m('3')} books: {m(sum(cnts[:3]))}; up to {m('4')} books: {m(sum(cnts[:4]))}): the {m(f'{mid_pos}\\text{{th}}')} student read **{m(ans)}** books.",
            ]
            steps_ar = [
                f"نوجد أولاً إجمالي عدد الطلاب بجمع ارتفاعات الأعمدة: {m(' + '.join(str(c) for c in cnts) + f' = {N}')}.",
                f"عند ترتيب {m(N)} طالباً تصاعدياً حسب عدد الكتب، يقع الوسيط عند الطالب رقم **{m(mid_pos)}**.",
                f"بالجمع التراكمي من اليسار (كتاب واحد: {m(cnts[0])}، حتى كتابين: {m(cnts[0]+cnts[1])}، حتى 3 كتب: {m(sum(cnts[:3]))}، حتى 4 كتب: {m(sum(cnts[:4]))}) نجد أن الطالب رقم {m(mid_pos)} قرأ **{m(ans)}** كتب.",
            ]
        elif ask == "mean":
            ans = float(mean_v)
            distractors = [round(sum(cnts) / 5, 1), round(ans + 0.2, 1), round(ans - 0.2, 1), 3]
            q_en = (
                f"The bar chart shows the scores ({m('1')} to {m('5')} points) earned by {m(N)} students on a mini-quiz, "
                f"with student counts {m(f'({cnts_tex})')} respectively. What is the **mean (average) score** per student?"
            )
            q_ar = (
                f"يوضّح التمثيل بالأعمدة الدرجات (من {m('1')} إلى {m('5')} نقاط) التي حصل عليها {m(N)} طالباً في اختبار قصير، "
                f"بأعداد طلاب {m(f'({cnts_tex})')} على الترتيب. ما **المتوسط الحسابي** لدرجة الطالب؟"
            )
            w_sum = " + ".join(f"{sc}\\times{c}" for sc, c in enumerate(cnts, 1))
            steps_en = [
                f"Multiply each score by how many students earned it: {m(f'{w_sum} = {tot_pts}')} total points.",
                f"Total number of students: {m(' + '.join(str(c) for c in cnts) + f' = {N}')}.",
                f"Divide total points by total students: {m(f'\\frac{{{tot_pts}}}{{{N}}} = {fmt_val(ans)}')}.",
            ]
            steps_ar = [
                f"نضرب كل درجة في عدد الطلاب الحاصلين عليها: {m(f'{w_sum} = {tot_pts}')} نقطة إجمالية.",
                f"إجمالي عدد الطلاب: {m(' + '.join(str(c) for c in cnts) + f' = {N}')}.",
                f"نقسم مجموع النقاط على عدد الطلاب: {m(f'\\frac{{{tot_pts}}}{{{N}}} = {fmt_val(ans)}')}.",
            ]
        else:
            ans = round(float(mean_v - med_v), 2)
            distractors = [0.5, 0.2, 0.8, 0.1]
            q_en = (
                f"The bar chart displays the quiz scores ({m('1')} to {m('5')}) of {m(N)} students. "
                f"By how much does the **mean** score exceed the **median** score (that is, {m('\\text{Mean} - \\text{Median}')})?"
            )
            q_ar = (
                f"يعرض التمثيل بالأعمدة درجات {m(N)} طالباً (من {m('1')} إلى {m('5')}). "
                f"بكم يزيد **المتوسط الحسابي** للدرجات عن **الوسيط** (أي {m('\\text{المتوسط} - \\text{الوسيط}')})؟"
            )
            steps_en = [
                f"Weighted total score = {m(tot_pts)} across {m(N)} students, so {m(f'\\text{{Mean}} = {tot_pts}/{N} = {float(mean_v):g}')}.",
                f"For {m(N)} sorted students, the {m('10\\text{th}')} score is {m(data[9])} and the {m('11\\text{th}')} score is {m(data[10])}, so {m(f'\\text{{Median}} = {float(med_v):g}')}.",
                f"Subtract: {m(f'{float(mean_v):g} - {float(med_v):g} = {ans:g}')}.",
            ]
            steps_ar = [
                f"مجموع الدرجات الموزون = {m(tot_pts)} لعدد {m(N)} طالباً، إذن {m(f'\\text{{المتوسط}} = {tot_pts}/{N} = {float(mean_v):g}')}.",
                f"لعدد {m(N)} طالباً مرتبين، الدرجة رقم {m(10)} هي {m(data[9])} والدرجة رقم {m(11)} هي {m(data[10])}، فالوسيط = {m(f'{float(med_v):g}')}.",
                f"نطرح: {m(f'{float(mean_v):g} - {float(med_v):g} = {ans:g}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_bar_{v_i}")
        h_en = "Careful! The bar heights are FREQUENCIES (how many students got each value), NOT the data values themselves!"
        h_ar = "انتبه! ارتفاعات الأعمدة تمثّل **التكرارات** (عدد الطلاب لكل قيمة)، وليست القيم نفسها!"
        s_en = explain_en("In a frequency bar chart, each value \\( x \\) appears \\( f(x) \\) times in the dataset!", steps_en, f"Never take the median or average of the 5 bar heights alone — always weight by student counts!")
        s_ar = explain_ar("في التمثيل التكراري بالأعمدة، كل قيمة \\( x \\) على المحور الأفقي تتكرر بعدد طلابها \\( f(x) \\)!", steps_ar, f"تجنب حساب وسيط أو متوسط ارتفاعات الأعمدة الخمسة مجردةً؛ فالعبرة بعدد الطلاب!")
        push("Data & Probability", diff, "kmc_g89_bar_chart_mean_median", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 8. Counting combinations with an exclusion rule (10 Qs)
    # ------------------------------------------------------------------
    exc_cases = [
        (4, 3, 2, 1, 1, 2, "shirts", "trousers", "pairs of shoes", "قمصان", "بناطيل", "أزواج أحذية", "Easy"),
        (5, 4, 2, 1, 1, 2, "main dishes", "salads", "drinks", "أطباق رئيسية", "سلطات", "مشروبات", "Easy"),
        (4, 5, 3, 1, 2, 3, "notebooks", "pens", "folders", "دفاتر", "أقلام", "ملفات", "Easy"),
        (5, 4, 3, 2, 1, 3, "hats", "jackets", "scarves", "قبعات", "سترات", "أوشحة", "Medium"),
        (6, 4, 3, 2, 2, 3, "sandwiches", "soups", "juices", "شطائر", "أنواع حساء", "عصائر", "Medium"),
        (5, 5, 4, 2, 2, 4, "apps", "themes", "icons", "تطبيقات", "سمات", "أيقونات", "Medium"),
        (6, 5, 3, 2, 3, 3, "science books", "math books", "art books", "كتب علوم", "كتب رياضيات", "كتب فنون", "Medium"),
        (7, 4, 3, 3, 2, 2, "routes A→B", "routes B→C", "routes C→D", "طرق A→B", "طرق B→C", "طرق C→D", "Hard"),
        (6, 5, 4, 3, 2, 3, "starters", "entrees", "desserts", "مقبلات", "وجبات رئيسية", "حلويات", "Hard"),
        (8, 5, 3, 2, 2, 3, "workshops", "labs", "seminars", "ورش عمل", "معامل", "ندوات", "Hard"),
    ]
    for v_i, (n1, n2, n3, f1, f2, f3, e1, e2, e3, a1, a2, a3, diff) in enumerate(exc_cases):
        tot = n1 * n2 * n3
        bad = f1 * f2 * f3
        ans = tot - bad
        distractors = [tot, tot - 1, ans - f3, ans + bad // 2 + 1]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_exc_{v_i}")
        q_en = (
            f"Rami chooses {m(1)} item from {m(n1)} {e1}, {m(1)} from {m(n2)} {e2}, and {m(1)} from {m(n3)} {e3}. "
            f"However, a specific group of {m(f1)} of the {e1} cannot be combined with {m(f2)} of the {e2} and {m(f3)} of the {e3} all together. "
            f"How many valid combinations of {m(3)} items can Rami choose?"
        )
        q_ar = (
            f"يختار رامي عنصراً واحداً من بين {m(n1)} {a1}، وواحداً من بين {m(n2)} {a2}، وواحداً من بين {m(n3)} {a3}. "
            f"لكن لا يُسمح باجتماع اختيارٍ من {m(f1)} محددة من الـ{a1} مع {m(f2)} محددة من الـ{a2} ومع {m(f3)} محددة من الـ{a3} في آنٍ واحد. "
            f"كم تشكيلة صالحة يمكن لرامي اختيارها؟"
        )
        h_en = "Complementary counting: compute (All unrestricted combinations) MINUS (Forbidden combinations)!"
        h_ar = "العدّ بالمتمم: احسب (جميع التشكيلات الممكنة بدون شروط) ناقص (التشكيلات الممنوعة)!"
        s_en = explain_en(
            "When a restriction forbids certain combinations, **Total − Forbidden** is much faster and cleaner than splitting into cases!",
            [
                f"Total unrestricted choices by the multiplication rule: {m(f'{n1} \\times {n2} \\times {n3} = {tot}')}.",
                f"Number of forbidden triples: {m(f'{f1} \\times {f2} \\times {f3} = {bad}')}.",
                f"Subtract forbidden from total: {m(f'{tot} - {bad} = {ans}')}.",
            ],
            f"Sanity check: when {m('f_1=f_2=f_3=1')}, exactly 1 triple is removed from {m(tot)}.",
        )
        s_ar = explain_ar(
            "عند وجود شرط يمنع تشكيلات معينة، تكون طريقة **(الكل − الممنوع)** أسرع وأدق بكثير من تقسيم الحالات!",
            [
                f"إجمالي الاختيارات بدون قيود (مبدأ العد): {m(f'{n1} \\times {n2} \\times {n3} = {tot}')}.",
                f"عدد التشكيلات الممنوعة: {m(f'{f1} \\times {f2} \\times {f3} = {bad}')}.",
                f"نطرح الممنوع من الكلي: {m(f'{tot} - {bad} = {ans}')}.",
            ],
            f"تحقق منطقي: المجموع الصالح {m(ans)} مضافاً إليه الممنوع {m(bad)} يعيد الإجمالي {m(tot)}.",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_counting_with_exclusion", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 9. Pigeonhole Principle worst-case draw guarantees (10 Qs)
    # ------------------------------------------------------------------
    php_cases = [
        ([6, 8, 10], 2, "same", "Easy"),
        ([5, 7, 9, 11], 2, "same", "Easy"),
        ([4, 6, 8], 3, "same", "Easy"),
        ([3, 8, 10], 5, "same", "Medium"),      # notice c1=3 < 4! min(3,4)+4+4+1 = 12! Classic KMC trap!
        ([2, 7, 9, 12], 4, "same", "Medium"),   # min(2,3)+3+3+3+1 = 12!
        ([5, 6, 9], 1, "each", "Medium"),       # one of EACH color: take all of two largest + 1 = 9+6+1 = 16!
        ([4, 7, 10], 1, "each", "Medium"),      # 10+7+1 = 18
        ([3, 5, 8, 11], 6, "same", "Hard"),     # 3 + 5 + 5 + 5 + 1 = 19!
        ([4, 6, 8, 10], 1, "each", "Hard"),     # 10+8+6+1 = 25!
        ([4, 5, 12, 15], 7, "same", "Hard"),    # 4 + 5 + 6 + 6 + 1 = 22!
    ]
    colors_en = ["red", "blue", "green", "yellow"]
    colors_ar = ["حمراء", "زرقاء", "خضراء", "صفراء"]
    for v_i, (cnts, k_req, mode, diff) in enumerate(php_cases):
        desc_en = ", ".join(f"{m(c)} {colors_en[i]}" for i, c in enumerate(cnts))
        desc_ar = " و".join(f"{m(c)} {colors_ar[i]}" for i, c in enumerate(cnts))
        if mode == "same":
            worst_parts = [min(c, k_req - 1) for c in cnts]
            worst = sum(worst_parts)
            ans = worst + 1
            naive = len(cnts) * (k_req - 1) + 1
            distractors = [naive if naive != ans else ans + 2, worst, ans + 1, k_req * len(cnts)]
            q_en = (
                f"A bag contains {desc_en} marbles. Without looking, what is the **minimum number** of marbles "
                f"you must draw to be **certain** of getting at least **{m(k_req)} marbles of the same color**?"
            )
            q_ar = (
                f"يحتوي كيس على كرات ملونة أعدادها: {desc_ar}. دون النظر داخل الكيس، ما **أقل عدد** من الكرات يجب سحبه "
                f"**لضمان** الحصول على **{m(k_req)} كرات على الأقل من اللون نفسه**؟"
            )
            wp_str = " + ".join(str(x) for x in worst_parts)
            steps_en = [
                f"Imagine the **unluckiest possible draw** that avoids getting {m(k_req)} of any color: you can take at most {m(k_req - 1)} of each color (or ALL of a color if fewer than {m(k_req - 1)} exist!).",
                f"Worst-case count without success: {m(f'{wp_str} = {worst}')} marbles.",
                f"Drawing **1 more marble** forces at least one color to reach {m(k_req)}: {m(f'{worst} + 1 = {ans}')}.",
            ]
            steps_ar = [
                f"نتخيل **أسوأ سحب ممكن** لا يحقق الشرط: نسحب بحد أقصى {m(k_req - 1)} كرات من كل لون (أو كل كرات اللون إن كان عددها أقل من {m(k_req - 1)}!).",
                f"عدد الكرات في أسوأ حالة دون نجاح: {m(f'{wp_str} = {worst}')} كرة.",
                f"سحب **كرة واحدة إضافية** يضمن وصول أحد الألوان إلى {m(k_req)}: {m(f'{worst} + 1 = {ans}')}.",
            ]
        else:
            sc = sorted(cnts, reverse=True)
            worst = sum(sc[:-1])
            ans = worst + 1
            distractors = [len(cnts), worst, sum(cnts), sum(cnts[:len(cnts) - 1]) + 1 if sum(cnts[:len(cnts) - 1]) + 1 != ans else ans - 2]
            q_en = (
                f"A box holds {desc_en} balls. Without looking, what is the **minimum number** of balls "
                f"you must draw to be **certain** of having **at least 1 ball of every color**?"
            )
            q_ar = (
                f"يحتوي صندوق على كرات ملونة أعدادها: {desc_ar}. دون النظر، ما **أقل عدد** من الكرات يجب سحبه "
                f"**لضمان** الحصول على **كرة واحدة على الأقل من كل لون**؟"
            )
            wp_str = " + ".join(str(x) for x in sc[:-1])
            steps_en = [
                f"What is the **worst-case scenario** where one color is still missing? You accidentally empty out ALL of the **largest** {m(len(cnts)-1)} colors first!",
                f"Worst-case draw missing the rarest color ({m(sc[-1])}): {m(f'{wp_str} = {worst}')} balls.",
                f"The very next ball MUST belong to the last remaining color: {m(f'{worst} + 1 = {ans}')}.",
            ]
            steps_ar = [
                f"ما **أسوأ حالة ممكنة** يغيب فيها أحد الألوان؟ أن تسحب أولاً جميع كرات الألوان الـ {m(len(cnts)-1)} **الأكثر عدداً** بالكامل!",
                f"أكبر سحب دون الحصول على اللون الأندر ({m(sc[-1])}) هو: {m(f'{wp_str} = {worst}')} كرة.",
                f"الكرة التالية مباشرة ستكون حتماً من اللون المتبقي: {m(f'{worst} + 1 = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_php_{v_i}")
        h_en = "To guarantee something for sure, ask: 'What is the MAXIMUM number of marbles I could draw and STILL fail?' Then add 1!"
        h_ar = "لضمان تحقق الشرط 100%، اسأل نفسك: «ما أكبر عدد يمكن سحبه في أسوأ حظ ممكن دون تحقق الشرط؟» ثم أضف 1!"
        s_en = explain_en("By the **Pigeonhole Principle**, Minimum Guaranteed Draw = (Maximum Unlucky Draw) + 1.", steps_en, f"With {m(worst)} draws you could still fail, whereas {m(ans)} draws guarantees success 100% of the time.")
        s_ar = explain_ar("حسب **مبدأ برج الحمام**: أقل عدد مضمون = (أكبر عدد في أسوأ حالة فشل) + 1.", steps_ar, f"عند سحب {m(worst)} قد لا يتحقق الشرط، أما عند سحب {m(ans)} فيتحقق الشرط يقيناً بنسبة 100%.")
        push("Combinatorics & Logic", diff, "kmc_g89_pigeonhole_guarantee", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 10. Two fair 6-sided dice probability (10 Qs)
    # ------------------------------------------------------------------
    dice_cases = [
        ("the sum of the two numbers is 9", "أن يكون مجموع الرقمين 9", lambda a, b: a + b == 9, "Easy"),
        ("the sum of the two numbers is at least 10", "أن يكون مجموع الرقمين 10 على الأقل", lambda a, b: a + b >= 10, "Easy"),
        ("the two numbers differ by 1 (that is, |a − b| = 1)", "أن يكون الفرق المطلق بين الرقمين 1 (أي |a − b| = 1)", lambda a, b: abs(a - b) == 1, "Easy"),
        ("the product of the two numbers is 12", "أن يكون حاصل ضرب الرقمين 12", lambda a, b: a * b == 12, "Medium"),
        ("the product of the two numbers is odd", "أن يكون حاصل ضرب الرقمين فردياً", lambda a, b: (a * b) % 2 == 1, "Medium"),
        ("the product of the two numbers is even", "أن يكون حاصل ضرب الرقمين زوجياً", lambda a, b: (a * b) % 2 == 0, "Medium"),
        ("the product of the two numbers is a perfect square", "أن يكون حاصل ضرب الرقمين مربعاً كاملاً", lambda a, b: int((a * b) ** 0.5) ** 2 == a * b, "Medium"),
        ("the product of the two numbers is divisible by 3", "أن يقبل حاصل ضرب الرقمين القسمة على 3", lambda a, b: (a * b) % 3 == 0, "Medium"),
        ("the product of the two numbers is divisible by 4", "أن يقبل حاصل ضرب الرقمين القسمة على 4", lambda a, b: (a * b) % 4 == 0, "Hard"),
        ("the first die shows a number strictly greater than the second die", "أن يكون رقم النرد الأول أكبر تماماً من رقم النرد الثاني", lambda a, b: a > b, "Hard"),
    ]
    for v_i, (cond_en, cond_ar, pred, diff) in enumerate(dice_cases):
        fav = [(a, b) for a in range(1, 7) for b in range(1, 7) if pred(a, b)]
        cnt = len(fav)
        ans = Fraction(cnt, 36)
        distractors = [
            Fraction(max(1, cnt - 2), 36),
            Fraction(min(35, cnt + 2), 36),
            Fraction(min(35, cnt + 3), 36),
            Fraction(36 - cnt, 36) if 36 - cnt != cnt else Fraction(cnt + 1, 36),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2c_dice_{v_i}")
        ex_pairs = ", ".join(f"({a},{b})" for a, b in fav[:6]) + (", \\dots" if len(fav) > 6 else "")
        q_en = f"Two fair six-sided dice (numbered {m('1')} to {m('6')}) are rolled simultaneously. What is the probability that **{cond_en}**?"
        q_ar = f"رُمي حجرا نرد متماثلان ومنتظمان (مرقّمان من {m('1')} إلى {m('6')}) معاً. ما احتمال **{cond_ar}**؟"
        h_en = "Treat the two dice as distinguishable (First die, Second die) so there are 6 × 6 = 36 equally likely ordered pairs!"
        h_ar = "عامل حجري النرد كزوج مرتب (الأول، الثاني) بحيث يكون فضاء العينة 6 × 6 = 36 زوجاً مرتباً متساوي الاحتمال!"
        s_en = explain_en(
            "Rolling two fair dice produces \\( 6 \\times 6 = 36 \\) **equally likely ordered pairs** \\( (a, b) \\) (so \\( (2,6) \\) and \\( (6,2) \\) are counted separately!).",
            [
                f"List or count all ordered pairs {m('(a, b)')} in {m('\\{1..6\\} \\times \\{1..6\\}')} satisfying the condition ({m(ex_pairs)}): there are **{m(cnt)}** favorable outcomes.",
                f"Divide by {m(36)} and simplify the fraction: {m(f'\\frac{{{cnt}}}{{36}} = {fmt_val(ans)}')}.",
            ],
            f"Check: both {m(cnt)} and {m(36)} divide cleanly by {m(__import__('math').gcd(cnt, 36))} to give {m(fmt_val(ans))}.",
        )
        s_ar = explain_ar(
            "رمي حجري نرد يعطي \\( 6 \\times 6 = 36 \\) **زوجاً مرتباً متساوي الاحتمال** \\( (a, b) \\) (أي أن \\( (2,6) \\) و\\( (6,2) \\) نتيجتان مختلفتان!).",
            [
                f"نحصي الأزواج المرتبة {m('(a, b)')} التي تحقق الشرط ({m(ex_pairs)}) فنجد عددها **{m(cnt)}** نتيجة مواتية.",
                f"نقسم على {m(36)} ونبسّط الكسر لأبسط صورة: {m(f'\\frac{{{cnt}}}{{36}} = {fmt_val(ans)}')}.",
            ],
            f"تحقق: بقسمة البسط والمقام على القاسم المشترك الأكبر {m(__import__('math').gcd(cnt, 36))} نحصل على {m(fmt_val(ans))}.",
        )
        push("Data & Probability", diff, "kmc_g89_two_dice_probability", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    # ------------------------------------------------------------------
    # 11. Truth-tellers & Liars island logic (3 speakers, verified unique!) (10 Qs)
    # ------------------------------------------------------------------
    logic_cases = [
        # (s1_en, s1_ar, fn1, s2_en, s2_ar, fn2, s3_en, s3_ar, fn3, ask_type, diff)
        (
            "All three of us are liars.", "نحن الثلاثة جميعاً كاذبون.", lambda a, b, c: not a and not b and not c,
            "Exactly one of us is a truth-teller.", "واحد فقط منا صادق.", lambda a, b, c: (a + b + c) == 1,
            "Omar (the second speaker) is lying.", "عمر (المتحدث الثاني) يكذب.", lambda a, b, c: not b,
            "who_truth", "Easy",
        ),
        (
            "Salim is a liar.", "سالم كاذب.", lambda a, b, c: not b,
            "Zaid is a liar.", "زيد كاذب.", lambda a, b, c: not c,
            "Both Hassan and Salim are liars.", "كلٌّ من حسن وسالم كاذبان.", lambda a, b, c: (not a) and (not b),
            "count", "Easy",
        ),
        (
            "Both Salim and Zaid tell the truth.", "كلٌّ من سالم وزيد صادقان.", lambda a, b, c: b and c,
            "Hassan is a liar.", "حسن كاذب.", lambda a, b, c: not a,
            "Salim is a liar.", "سالم كاذب.", lambda a, b, c: not b,
            "count", "Medium",
        ),
        (
            "Exactly two of us are truth-tellers.", "اثنان فقط منا صادقان.", lambda a, b, c: (a + b + c) == 2,
            "All three of us are liars.", "نحن الثلاثة كاذبون.", lambda a, b, c: (a + b + c) == 0,
            "Exactly two of us are truth-tellers.", "اثنان فقط منا صادقان.", lambda a, b, c: (a + b + c) == 2,
            "count", "Medium",
        ),
        (
            "Both Salim and Zaid are liars.", "كلٌّ من سالم وزيد كاذبان.", lambda a, b, c: (not b) and (not c),
            "Hassan tells the truth.", "حسن صادق.", lambda a, b, c: a,
            "Salim is a liar.", "سالم كاذب.", lambda a, b, c: not b,
            "count", "Medium",
        ),
        (
            "All three of us are truth-tellers.", "نحن الثلاثة جميعاً صادقون.", lambda a, b, c: a and b and c,
            "Hassan is a liar.", "حسن كاذب.", lambda a, b, c: not a,
            "Salim tells the truth.", "سالم صادق.", lambda a, b, c: b,
            "count", "Medium",
        ),
        (
            "Salim tells the truth.", "سالم صادق.", lambda a, b, c: b,
            "All three of us are liars.", "نحن الثلاثة كاذبون.", lambda a, b, c: (a + b + c) == 0,
            "Salim is a liar.", "سالم كاذب.", lambda a, b, c: not b,
            "who_truth", "Medium",
        ),
        (
            "Salim and Zaid are of the same type (both truth-tellers or both liars).", "سالم وزيد من النوع نفسه (كلاهما صادقان أو كلاهما كاذبان).", lambda a, b, c: b == c,
            "Zaid is a liar.", "زيد كاذب.", lambda a, b, c: not c,
            "All three of us are truth-tellers.", "نحن الثلاثة جميعاً صادقون.", lambda a, b, c: a and b and c,
            "count", "Hard",
        ),
        (
            "Exactly one of us is a truth-teller.", "واحد فقط منا صادق.", lambda a, b, c: (a + b + c) == 1,
            "Exactly two of us are truth-tellers.", "اثنان فقط منا صادقان.", lambda a, b, c: (a + b + c) == 2,
            "All three of us are liars.", "نحن الثلاثة كاذبون.", lambda a, b, c: (a + b + c) == 0,
            "who_truth", "Hard",
        ),
        (
            "Zaid is a liar.", "زيد كاذب.", lambda a, b, c: not c,
            "Hassan tells the truth.", "حسن صادق.", lambda a, b, c: a,
            "All three of us are liars.", "نحن الثلاثة كاذبون.", lambda a, b, c: (a + b + c) == 0,
            "count", "Hard",
        ),
    ]
    # Note: let's replace case 4 (index 4: a<->b, b<->c, c<->(a+b+c==2): if a=T->b=T->c=T->sum=3!=2 false; if a=F->b=F->c=F->(sum==2) is F == c(T/F) -> wait if a=F,b=F,c=F then fn3 is False == c(False) VALID! Let's check!)
    names_en = ("Hassan", "Salim", "Zaid")
    names_ar = ("حسن", "سالم", "زيد")
    for v_i, (s1e, s1a, f1, s2e, s2a, f2, s3e, s3a, f3, ask_t, diff) in enumerate(logic_cases):
        valid_states = []
        for a in (False, True):
            for b in (False, True):
                for c in (False, True):
                    if (a == bool(f1(a, b, c))) and (b == bool(f2(a, b, c))) and (c == bool(f3(a, b, c))):
                        valid_states.append((a, b, c))
        assert len(valid_states) == 1, f"Logic case {v_i} valid_states={valid_states}"
        ta, tb, tc = valid_states[0]
        n_truth = int(ta) + int(tb) + int(tc)
        state_desc_en = ", ".join(
            f"{nm} is a **{'truth-teller' if t else 'liar'}**" for nm, t in zip(names_en, (ta, tb, tc))
        )
        state_desc_ar = "، و".join(
            f"{nm} **{'صادق' if t else 'كاذب'}**" for nm, t in zip(names_ar, (ta, tb, tc))
        )

        if ask_t == "count":
            pairs = [
                ("0", "0"),
                ("1", "1"),
                ("2", "2"),
                ("3", "3"),
                ("Cannot be determined", "لا يمكن تحديد العدد"),
            ]
            opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, correct_pair_idx=n_truth, seed_key=f"t2c_lg_{v_i}", shuffle=False)
            ask_q_en = "How many of the three are **truth-tellers**?"
            ask_q_ar = "كم شخصاً من الثلاثة **صادق**؟"
        else:
            # Make sure exactly 1 truth-teller for 'who_truth'
            assert n_truth == 1, f"Expected 1 truth-teller in who_truth case {v_i}, got {(ta,tb,tc)}"
            t_idx = [ta, tb, tc].index(True)
            pairs = [
                ("Only Hassan", "حسن فقط"),
                ("Only Salim", "سالم فقط"),
                ("Only Zaid", "زيد فقط"),
                ("Both Hassan and Salim", "حسن وسالم معاً"),
                ("None of them", "لا أحد منهم"),
            ]
            opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, correct_pair_idx=t_idx, seed_key=f"t2c_lg_{v_i}")
            ask_q_en = "Which of them is telling the truth?"
            ask_q_ar = "مَن منهم يقول الحقيقة؟"

        q_en = (
            f"On an island, every person is either a **truth-teller** (always tells the truth) or a **liar** (always lies). "
            f"Three islanders — Hassan, Salim, and Zaid — make these statements:<br>"
            f"• **Hassan:** \"{s1e}\"<br>"
            f"• **Salim:** \"{s2e}\"<br>"
            f"• **Zaid:** \"{s3e}\"<br>"
            f"{ask_q_en}"
        )
        q_ar = (
            f"في إحدى الجزر، كل شخص إما **صادق** (يقول الحقيقة دائماً) أو **كاذب** (يكذب دائماً). "
            f"قال ثلاثة من سكان الجزيرة (حسن، وسالم، وزيد) العبارات الآتية:<br>"
            f"• **حسن:** «{s1a}»<br>"
            f"• **سالم:** «{s2a}»<br>"
            f"• **زيد:** «{s3a}»<br>"
            f"{ask_q_ar}"
        )
        h_en = "Test whether Hassan can be a truth-teller (Case 1) or a liar (Case 2), and check if every person's statement matches their role!"
        h_ar = "افترض الحالة 1 (حسن صادق) ثم الحالة 2 (حسن كاذب)، وتحقّق في كل حالة هل تتوافق عثرات الثلاثة مع كونهم صادقين أو كاذبين!"
        s_en = explain_en(
            "A speaker is a truth-teller if and only if their statement is **True**; a speaker is a liar if and only if their statement is **False**.",
            [
                f"Test the possibilities for Hassan (Truth-teller vs Liar) and follow the chain of consequences to Salim and Zaid.",
                f"Only one assignment has zero contradictions: {state_desc_en}.",
                f"Checking all 3 statements under this assignment confirms every truth-teller speaks a true fact and every liar speaks a false claim!",
            ],
            f"Unique valid solution verified across all \\( 2^3 = 8 \\) possible truth assignments!",
        )
        s_ar = explain_ar(
            "يكون المتحدث صادقاً إذا وفقط إذا كانت عبارته **صحيحة**، ويكون كاذباً إذا وفقط إذا كانت عبارته **خاطئة**.",
            [
                f"نختبر فرضية كون حسن صادقاً ثم فرضية كونه كاذباً ونتتبع أثر ذلك على عبارتي سالم وزيد.",
                f"تنجح حالة وحيدة فقط دون أي تناقض: {state_desc_ar}.",
                f"بمراجعة العبارات الثلاث في هذه الحالة نتأكد أن كل صادق قال عبارة صحيحة وكل كاذب قال عبارة خاطئة!",
            ],
            f"تم التحقق من جميع الحالات الـ \\( 2^3 = 8 \\) الممكنة ولا توجد سوى هذه الحالة الصحيحة الوحيدة!",
        )
        push("Combinatorics & Logic", diff, "kmc_g89_knights_knaves_3", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar)

    assert len(out) == 110, f"Expected 110, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 2 Combinatorics & Data questions cleanly.")
