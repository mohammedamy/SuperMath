"""KAUST Mathematics Competition (KMC) — Track 1: Grades 6-7
Pillar 3: Geometry, Area, Perimeter, Angles & 3D Spatial Visualization (110 questions).
Every single question includes a parameter-exact KMC past-paper SVG diagram.
"""
from fractions import Fraction
import math
from kmc_common import m, explain_en, explain_ar, make_5_math_options, make_kmc_question
from kmc_diagrams import (
    svg_shaded_triangle_in_rect,
    svg_polyomino,
    svg_painted_cube_3d,
    svg_equilateral_corner_cuts,
    svg_square_eighths_shaded,
    svg_rectilinear_staircase,
    svg_midpoint_square_shaded,
    svg_inscribed_corner_triangle_in_rect,
    svg_water_tank_3d,
    svg_grid_polygon,
    svg_parallel_zigzag,
)

LEVEL = "Track 1: Grades 6-7"


def generate_t1_geometry() -> list[dict]:
    items = []
    idx = 1

    def next_id():
        nonlocal idx
        qid = f"KAUST-G67-G{idx:03d}"
        idx += 1
        return qid

    # 1. Shaded triangle spanning base of L x W rectangle (10 variants) — KMC G6-7 Sample Q4
    rect_tri_cases = [
        (12, 8, 0.65), (14, 6, 0.35), (16, 9, 0.72), (10, 7, 0.42), (18, 8, 0.58),
        (15, 10, 0.30), (20, 9, 0.68), (12, 11, 0.45), (22, 6, 0.75), (16, 12, 0.38),
    ]
    for L, W, af in rect_tri_cases:
        qid = next_id()
        ans = (L * W) // 2
        svg = svg_shaded_triangle_in_rect(L, W, af, "cm")
        q_en = (
            f"In a {m(L)} cm by {m(W)} cm rectangle, the shaded triangle has the entire bottom side of length {m(L)} cm as its base "
            f"and its top vertex on the top side of the rectangle. What is the area of the shaded triangle, in {m('\\text{cm}^2')}?"
        )
        q_ar = (
            f"في مستطيل بُعداه {m(L)} سم و {m(W)} سم، قاعدة المثلث المظلّل هي الضلع السفلي كاملًا ({m(L)} سم) "
            f"ورأسه يقع على الضلع العلوي للمستطيل. ما مساحة المثلث المظلّل بالوحدة {m('\\text{cm}^2')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [L * W, ans // 2, 2 * (L + W), ans + L], qid
        )
        sol_en = explain_en(
            "Area of any triangle = **½ × base × perpendicular height**. No matter where the top vertex slides along the top edge, its perpendicular height straight down to the base is always the width of the rectangle!",
            [
                f"Identify the **base** of the shaded triangle: it is the entire bottom edge, {m(f'b = {L}')} cm.",
                f"Identify the **perpendicular height**: the straight vertical distance from the top side to the bottom side is {m(f'h = {W}')} cm.",
                f"Apply the triangle area formula: {m(f'\\text{{Area}} = \\frac{{1}}{{2}} \\times {L} \\times {W} = \\frac{{{L*W}}}{{2}} = {ans}\\text{{ cm}}^2')} (exactly half of the rectangle!).",
            ],
            f"Rectangle area is {m(f'{L} \\times {W} = {L*W}\\text{{ cm}}^2')}, and half of {m(L*W)} is {m(ans)}!",
        )
        sol_ar = explain_ar(
            "مساحة أي مثلث تساوي **نصف طول القاعدة × الارتفاع العمودي**. مهما تحرّك الرأس العلوي على الضلع العلوي للمستطيل، يظل الارتفاع العمودي مساويًا لعرض المستطيل دائمًا!",
            [
                f"**طول القاعدة:** هو الضلع السفلي كاملًا ويساوي {m(L)} سم.",
                f"**الارتفاع العمودي:** هو المسافة الرأسية بين الضلعين المتقابلين ويساوي {m(W)} سم.",
                f"**حساب المساحة:** {m(f'\\frac{{1}}{{2}} \\times {L} \\times {W} = {ans}\\text{{ cm}}^2')} (أي نصف مساحة المستطيل بالضبط).",
            ],
            f"مساحة المستطيل الكامل {m(L*W)}، ونصفها يساوي {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Easy", "g67-shaded-tri-in-rect",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"What is the straight perpendicular distance (height) from the top vertex down to the {L} cm base?",
            f"ما البُعد العمودي (الارتفاع) من الرأس العلوي إلى القاعدة التي طولها {L} سم؟",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 2. Polyomino outer perimeter <-> area (10 variants) — KMC G6-7 Sample Q11
    CROSS5 = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]       # 5 squares, 12 outer edges
    TSHAPE5 = [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]      # 5 squares, 12 outer edges
    LSHAPE4 = [(0, 0), (0, 1), (0, 2), (1, 2)]              # 4 squares, 10 outer edges
    STAIR6 = [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2)] # 6 squares, 12 outer edges
    USHAPE7 = [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)] # 7 squares, 16 outer edges

    poly_cases = [
        (CROSS5, 5, 12, 3, "perim_to_area"),
        (CROSS5, 5, 12, 4, "perim_to_area"),
        (TSHAPE5, 5, 12, 5, "perim_to_area"),
        (LSHAPE4, 4, 10, 4, "perim_to_area"),
        (STAIR6, 6, 12, 3, "perim_to_area"),
        (USHAPE7, 7, 16, 2, "perim_to_area"),
        (CROSS5, 5, 12, 6, "area_to_perim"),
        (LSHAPE4, 4, 10, 5, "area_to_perim"),
        (STAIR6, 6, 12, 4, "area_to_perim"),
        (USHAPE7, 7, 16, 3, "area_to_perim"),
    ]
    for cells, n_sq, n_edges, side_s, mode in poly_cases:
        qid = next_id()
        perim = n_edges * side_s
        area = n_sq * (side_s ** 2)
        svg = svg_polyomino(cells)
        if mode == "perim_to_area":
            ans = area
            q_en = (
                f"The shaded figure is formed by joining {m(n_sq)} identical squares edge-to-edge, "
                f"and its outer perimeter is {m(perim)} cm. What is the **total area** of the figure, in {m('\\text{cm}^2')}?"
            )
            q_ar = (
                f"تكوّن الشكل المظلّل من ضم {m(n_sq)} مربعات متطابقة جنبًا إلى جنب، "
                f"وكان محيطه الخارجي {m(perim)} سم. ما **المساحة الكلية** للشكل بالوحدة {m('\\text{cm}^2')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [side_s ** 2, n_sq * side_s, ans + side_s ** 2, max(4, ans - side_s ** 2)], qid
            )
            sol_en = explain_en(
                "Count how many **outer unit-square edges** form the boundary of the shape (ignore interior shared lines!), divide the perimeter to find 1 square's side length, then find the area!",
                [
                    f"Walk around the outside boundary of the figure and count the exposed square sides: there are exactly {m(n_edges)} equal outer segments.",
                    f"Divide the perimeter by {m(n_edges)} to get the side length of one small square: {m(f'{perim} \\div {n_edges} = {side_s}')} cm.",
                    f"Area of **one** small square {m(f'= {side_s} \\times {side_s} = {side_s**2}\\text{{ cm}}^2')}. Multiply by {m(n_sq)} squares: {m(f'{n_sq} \\times {side_s**2} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"Watch out: don't divide {m(perim)} by {m(4 * n_sq)}! Interior touching edges are inside the figure, not part of the outer perimeter.",
            )
            sol_ar = explain_ar(
                "نعدّ **الأضلاع الخارجية فقط** على حدود الشكل (دون الخطوط الداخلية المشتركة)، ثم نقسم المحيط عليها لمعرفة طول ضلع المربع الواحد!",
                [
                    f"بتتبع الحدود الخارجية للشكل نجد أنها تتكون من {m(n_edges)} ضلعًا متساويًا.",
                    f"طول ضلع المربع الصغير الواحد يساوي {m(f'{perim} \\div {n_edges} = {side_s}')} سم.",
                    f"مساحة المربع الواحد {m(f'= {side_s}^2 = {side_s**2}\\text{{ cm}}^2')}، إذن المساحة الكلية لـ {m(n_sq)} مربعات تساوي {m(f'{n_sq} \\times {side_s**2} = {ans}\\text{{ cm}}^2')}.",
                ],
                f"تحقق: {m(n_edges)} ضلعًا خارجيًا × {m(side_s)} سم = محيط قدره {m(perim)} سم.",
            )
        else:
            ans = perim
            q_en = (
                f"The shaded figure is made of {m(n_sq)} identical squares joined edge-to-edge, "
                f"and its total area is {m(area)} {m('\\text{cm}^2')}. What is its **outer perimeter**, in cm?"
            )
            q_ar = (
                f"يتكوّن الشكل المظلّل من {m(n_sq)} مربعات متطابقة متلاصقة، ومساحته الكلية {m(area)} {m('\\text{cm}^2')}. "
                f"ما **محيطه الخارجي** بالسنتيمتر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [4 * n_sq * side_s, (n_edges - 2) * side_s, (n_edges + 2) * side_s, n_edges * (side_s + 1)], qid
            )
            sol_en = explain_en(
                "Divide the total area by the number of squares to get the area of **one** square, take its square root for the side length, then multiply by the count of outer boundary edges!",
                [
                    f"Area of **one** small square: {m(f'{area} \\div {n_sq} = {side_s**2}\\text{{ cm}}^2')}.",
                    f"Since {m(f'{side_s} \\times {side_s} = {side_s**2}')}, each small square has side length {m(side_s)} cm.",
                    f"Count the outer boundary edges around the figure: there are {m(n_edges)} outer segments, so Perimeter {m(f'= {n_edges} \\times {side_s} = {ans}')} cm.",
                ],
                f"Notice {m(f'4 \\times {n_sq} \\times {side_s} = {4*n_sq*side_s}')} cm would count buried internal edges too; only the {m(n_edges)} outer edges count!",
            )
            sol_ar = explain_ar(
                "نقسم المساحة الكلية على عدد المربعات لمعرفة مساحة المربع الواحد ومنها طول ضلعه، ثم نضرب في عدد الأضلاع الخارجية!",
                [
                    f"مساحة المربع الواحد تساوي {m(f'{area} \\div {n_sq} = {side_s**2}\\text{{ cm}}^2')}.",
                    f"بما أن {m(f'{side_s} \\times {side_s} = {side_s**2}')}، فإن طول ضلع المربع الصغير هو {m(side_s)} سم.",
                    f"نعدّ الأضلاع الواقعة على المحيط الخارجي فنجدها {m(n_edges)} ضلعًا، فيكون المحيط {m(f'= {n_edges} \\times {side_s} = {ans}')} سم.",
                ],
                f"انتبه لعدم احتساب الأضلاع الداخلية المشتركة؛ المحيط يقتصر على الـ {m(n_edges)} ضلعًا الخارجية فقط.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-polyomino-perim-area",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Carefully trace and count ONLY the outer boundary segments around the figure.",
            "تتبّع وعدّ الأضلاع الواقعة على الحدود الخارجية للشكل فقط دون الخطوط الداخلية.",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 3. Painted n x n x n large cube (10 variants with 3D isometric cube SVG!) — KMC G6-7 Sample Q16
    cube_cases = [
        (3, "two", 12),        # 12*(3-2)=12
        (3, "one", 6),         # 6*(3-2)^2=6
        (3, "zero", 1),        # (3-2)^3=1
        (4, "two", 24),        # 12*(4-2)=24
        (4, "one", 24),        # 6*(4-2)^2=24
        (4, "zero", 8),        # (4-2)^3=8
        (4, "at_least_two", 32), # 24 + 8 = 32
        (5, "two", 36),        # 12*(5-2)=36
        (5, "one", 54),        # 6*(5-2)^2=54
        (5, "zero", 27),       # (5-2)^3=27
    ]
    for n, kind, ans in cube_cases:
        qid = next_id()
        n3 = n ** 3
        svg = svg_painted_cube_3d(min(n, 5))
        desc_map = {
            "two": ("**exactly two** painted faces", "وجهان مطليان **بالضبط**"),
            "one": ("**exactly one** painted face", "وجه واحد مطلي **بالضبط**"),
            "zero": ("**zero** painted faces (completely unpainted)", "**لا يوجد بها أي وجه مطلي** (غير مطلية إطلاقًا)"),
            "at_least_two": ("**at least two** painted faces", "**وجهان مطليان على الأقل**"),
        }
        ask_e, ask_a = desc_map[kind]
        q_en = (
            f"A large {m(f'{n} \\times {n} \\times {n}')} cube is assembled from {m(n3)} identical unit cubes, "
            f"and then all {m(6)} outer faces of the large cube are painted purple. "
            f"How many of the {m(n3)} small unit cubes have {ask_e}?"
        )
        q_ar = (
            f"مكعب كبير أبعاده {m(f'{n} \\times {n} \\times {n}')} مكوّن من {m(n3)} مكعبًا صغيرًا متطابقًا، "
            f"طُليت جميع أوجهه الستة الخارجية باللون البنفسجي. كم مكعبًا صغيرًا {ask_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [8, 12 * (n - 2), 6 * (n - 2) ** 2, (n - 2) ** 3, ans + 6, ans + 4], qid
        )
        if kind == "two":
            rule_e = f"Small cubes with **2 painted faces** sit along the **12 edges** of the big cube, excluding the 2 corners at the ends of each edge! Each edge has {m(f'{n} - 2 = {n-2}')} such middle cubes, giving {m(f'12 \\times {n-2} = {ans}')}."
            rule_a = f"المكعبات ذات **الوجهين المطليين** تقع على **الأحرف الـ 12** للمكعب الكبير بعد استبعاد مكعبَي الزاويتين في طرفَي كل حرف! على كل حرف يوجد {m(f'{n} - 2 = {n-2}')} مكعبات، إذن العدد {m(f'12 \\times {n-2} = {ans}')}."
        elif kind == "one":
            rule_e = f"Small cubes with **1 painted face** sit in the **interior of each of the 6 faces** (away from all edges). Removing the 1-cube border around a {m(f'{n}\\times{n}')} face leaves a {m(f'{n-2}\\times{n-2}')} square of {m((n-2)**2)} cubes per face, so {m(f'6 \\times {(n-2)**2} = {ans}')}."
            rule_a = f"المكعبات ذات **الوجه الواحد المطلي** تقع في **وسط الأوجه الستة** بعيدًا عن الحواف. بعد إزالة الإطار الخارجي من كل وجه {m(f'{n}\\times{n}')} يتبقى مربع {m(f'{n-2}\\times{n-2}')} به {m((n-2)**2)} مكعبًا في الوجه الواحد، إذن المجموع {m(f'6 \\times {(n-2)**2} = {ans}')}."
        elif kind == "zero":
            rule_e = f"Unpainted cubes are hidden completely **inside the core**! Peeling off 1 layer from left/right, front/back, and top/bottom shrinks {m(f'{n}\\times{n}\\times{n}')} to an inner {m(f'{n-2}\\times{n-2}\\times{n-2}')} cube containing {m(f'{n-2}^3 = {ans}')} small cubes."
            rule_a = f"المكعبات غير المطلية تختبئ بالكامل **في قلب المكعب**! عند إزالة طبقة واحدة من كل اتجاه يتبقى مكعب داخلي أبعاده {m(f'{n-2}\\times{n-2}\\times{n-2}')}، وعدد مكعباته {m(f'{n-2}^3 = {ans}')}."
        else:
            rule_e = f"**At least 2 painted faces** means **2 painted faces OR 3 painted faces**. All {m(8)} corners have 3 painted faces, and each of the {m(12)} edges has {m(f'{n}-2 = {n-2}')} cubes with 2 painted faces ({m(12*(n-2))} total). Adding them gives {m(f'8 + {12*(n-2)} = {ans}')}."
            rule_a = f"**وجهان على الأقل** تعني **وجهين مطليين أو 3 أوجه مطلية**. توجد {m(8)} مكعبات في الرؤوس (بـ 3 أوجه مطلية)، وعلى الـ {m(12)} حرفًا يوجد {m(f'12 \\times ({n}-2) = {12*(n-2)}')} مكعبًا بوجهين مطليين؛ إذن المجموع {m(f'8 + {12*(n-2)} = {ans}')}."
        sol_en = explain_en(
            "Every small cube belongs to one of 4 easy locations on the big cube: **8 corners** (3 faces painted), **12 edges** (2 faces), **6 face centers** (1 face), or **1 hidden core** (0 faces)!",
            [
                f"Recall a cube always has {m(8)} corners, {m(12)} edges, and {m(6)} faces.",
                rule_e,
            ],
            f"Full accounting check: {m(f'8 + {12*(n-2)} + {6*(n-2)**2} + {(n-2)**3} = {n3}')} small cubes in total!",
        )
        sol_ar = explain_ar(
            "تتوزع المكعبات الصغيرة حسب موقعها إلى 4 أنواع: **8 رؤوس** (3 أوجه مطلية)، **12 حرفًا** (وجهان)، **مراكز 6 أوجه** (وجه واحد)، و**القلب الداخلي** (0 أوجه)!",
            [
                f"تذكّر أن لأي مكعب {m(8)} رؤوس و {m(12)} حرفًا و {m(6)} أوجه.",
                rule_a,
            ],
            f"التحقق بجمع جميع المكعبات: {m(f'8 + {12*(n-2)} + {6*(n-2)**2} + {(n-2)**3} = {n3}')} مكعبًا صغيرًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-painted-cube-3d",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Classify small cubes by where they sit: 8 corners (3 faces), 12 edges (2 faces), 6 face interiors (1 face), or inner core (0 faces).",
            "صنّف المكعبات الصغيرة حسب موقعها: 8 رؤوس (3 أوجه)، 12 حرفًا (وجهان)، أواسط 6 أوجه (وجه واحد)، أو الداخل (0 أوجه).",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 4. Equilateral triangle corner cuts — perimeter relation (10 variants) — KMC G6-7 Sample Q17
    # Big side S: 3 small equilateral triangles of side x cut off -> sum of 3 small perimeters = 9x, hexagon perimeter = 3x + 3(S - 2x) = 3S - 3x.
    # Variant A (5 items): 9x = 3S - 3x => 12x = 3S => x = S/4!
    # Variant B (5 items): given S and x, find perimeter of shaded hexagon = 3S - 3x!
    eq_cut_cases = [
        (8, None, "find_x"), (12, None, "find_x"), (16, None, "find_x"), (20, None, "find_x"), (6, None, "find_x"),
        (10, 2, "find_hex"), (12, 2, "find_hex"), (15, 3, "find_hex"), (18, 4, "find_hex"), (14, 3, "find_hex"),
    ]
    for S, x_given, mode in eq_cut_cases:
        qid = next_id()
        if mode == "find_x":
            ans_f = Fraction(S, 4)
            ans_val = int(ans_f) if ans_f.denominator == 1 else float(ans_f)
            svg = svg_equilateral_corner_cuts(f"{S} cm", "x")
            q_en = (
                f"Three identical small equilateral triangles of side length {m('x')} cm are cut from the corners of a large equilateral triangle "
                f"of side length {m(S)} cm, leaving a shaded hexagon. If the **sum of the perimeters** of the three small triangles equals "
                f"the **perimeter of the shaded hexagon**, what is {m('x')} (in cm)?"
            )
            q_ar = (
                f"قُطعت ثلاثة مثلثات متطابقة ومتساوية الأضلاع طول ضلع كلٍّ منها {m('x')} سم من رؤوس مثلث كبير متساوي الأضلاع طول ضلعه {m(S)} سم، "
                f"فتبقّى شكل سداسي مظلّل. إذا كان **مجموع محيطات المثلثات الثلاثة الصغيرة** يساوي **محيط السداسي المظلّل**، فما قيمة {m('x')} بالسنتيمتر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans_val, [S / 3 if S % 3 == 0 else ans_val + 1, ans_val + 0.5, ans_val + 1, max(0.5, ans_val - 0.5)], qid
            )
            sol_en = explain_en(
                "Write both perimeters cleanly in terms of the unknown small side `x`!",
                [
                    f"**Three small triangles:** One small equilateral triangle has perimeter {m('3x')}, so all three together have perimeter {m('3 \\times 3x = 9x')}.",
                    f"**Shaded hexagon:** It has {m(3)} newly cut edges (each of length {m('x')}) plus {m(3)} shortened pieces of the big sides (each of length {m(f'{S} - 2x')}). Its perimeter is {m(f'3x + 3({S} - 2x) = {3*S} - 3x')}.",
                    f"**Set them equal:** {m(f'9x = {3*S} - 3x')}. Add {m('3x')} to both sides: {m(f'12x = {3*S}')}, so {m(f'x = \\frac{{{3*S}}}{{12}} = {ans_val:g}')} cm.",
                ],
                f"Check with {m(f'x = {ans_val:g}')}: three small perimeters {m(f'= 9 \\times {ans_val:g} = {9*ans_val:g}')} cm, and hexagon perimeter {m(f'= {3*S} - 3({ans_val:g}) = {3*S - 3*ans_val:g}')} cm!",
            )
            sol_ar = explain_ar(
                "نعبّر عن المحيطين بدلالة طول ضلع المثلث الصغير `x` ثم نساوي بينهما!",
                [
                    f"**مجموع محيطات المثلثات الثلاثة الصغيرة:** محيط الواحد {m('3x')}، ومجموع الثلاثة {m('3 \\times 3x = 9x')}.",
                    f"**محيط السداسي المظلّل:** يتكون من {m(3)} أضلاع ناتجة عن القطع (طول كل منها {m('x')}) و {m(3)} أجزاء متبقية من أضلاع المثلث الكبير (طول كل منها {m(f'{S} - 2x')})، فمحيطه {m(f'3x + 3({S} - 2x) = {3*S} - 3x')}.",
                    f"**بالمساواة:** {m(f'9x = {3*S} - 3x')}، نضيف {m('3x')} للطرفين فنحصل على {m(f'12x = {3*S}')}، أي {m(f'x = {ans_val:g}')} سم.",
                ],
                f"تحقق: {m(f'9 \\times {ans_val:g} = {9*ans_val:g}')} سم، ومحيط السداسي {m(f'{3*S} - 3({ans_val:g}) = {3*S - 3*ans_val:g}')} سم.",
            )
        else:
            ans = 3 * S - 3 * x_given
            svg = svg_equilateral_corner_cuts(f"{S} cm", f"{x_given} cm")
            q_en = (
                f"Three equilateral triangles of side length {m(x_given)} cm are cut from the three corners of a large equilateral triangle "
                f"of side length {m(S)} cm. What is the perimeter of the remaining shaded hexagon, in cm?"
            )
            q_ar = (
                f"قُطعت ثلاثة مثلثات متساوية الأضلاع طول ضلع كلٍّ منها {m(x_given)} سم من رؤوس مثلث كبير متساوي الأضلاع طول ضلعه {m(S)} سم. "
                f"ما محيط الشكل السداسي المظلّل المتبقي بالسنتيمتر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [3 * S, 3 * S - 6 * x_given, 3 * S + 3 * x_given, ans + x_given], qid
            )
            rem_edge = S - 2 * x_given
            sol_en = explain_en(
                "Count all **6 sides** of the shaded hexagon: 3 leftover pieces of the original triangle + 3 new cut edges!",
                [
                    f"Each original side of {m(S)} cm loses {m(x_given)} cm at **both** ends, leaving {m(f'{S} - 2 \\times {x_given} = {rem_edge}')} cm.",
                    f"Each cut corner creates a new hexagon edge of length {m(x_given)} cm (because the cut triangle is equilateral!).",
                    f"Add all 6 sides of the hexagon: {m(f'3 \\times {rem_edge} + 3 \\times {x_given} = {3*rem_edge} + {3*x_given} = {ans}')} cm.",
                ],
                f"Shortcut insight: each cut replaces two corner edges ({m(f'2 \\times {x_given}')}) with one cut edge ({m(x_given)}), losing {m(x_given)} cm per corner: {m(f'{3*S} - 3({x_given}) = {ans}')} cm!",
            )
            sol_ar = explain_ar(
                "نحسب أطوال **الأضلاع الستة** للسداسي المظلّل: 3 أجزاء متبقية من المثلث الكبير + 3 أضلاع جديدة مكان القطع!",
                [
                    f"كل ضلع أصلي طوله {m(S)} سم يُقطع منه {m(x_given)} سم من كل طرف، فيتبقى منه {m(f'{S} - 2 \\times {x_given} = {rem_edge}')} سم.",
                    f"كل زاوية مقطوعة تترك ضلعًا جديدًا طوله {m(x_given)} سم (لأن المثلث المقطوع متساوي الأضلاع).",
                    f"إذن محيط السداسي {m(f'= 3 \\times {rem_edge} + 3 \\times {x_given} = {ans}')} سم.",
                ],
                f"طريقة سريعة: كل ركن مقطوع يُنقص المحيط الأصلي {m(3*S)} بمقدار {m(x_given)} سم، فيصبح المحيط {m(f'{3*S} - {3*x_given} = {ans}')} سم.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-equilateral-corner-cuts",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Each big side loses 2 corner segments of length x, while each corner adds 1 new cut edge of length x.",
            "كل ضلع كبير يفقد قطعتين من طرفيه، بينما يضيف كل ركن مقطوع ضلعًا جديدًا واحدًا للسداسي.",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 5. Square divided into 8 congruent triangles — shaded fraction/percentage (10 variants) — KMC G6-7 Sample Q18
    eighths_cases = [
        ([0, 6, 7], True, "fraction", Fraction(3, 8)),   # 3/8
        ([0, 2, 5, 7], True, "fraction", Fraction(1, 2)),# 4/8 = 1/2
        ([1, 2, 3, 6, 7], True, "fraction", Fraction(5, 8)), # 5/8
        ([0, 4], True, "fraction", Fraction(1, 4)),      # 2/8 = 1/4
        ([0, 1, 2, 4, 6, 7], True, "fraction", Fraction(3, 4)), # 6/8 = 3/4
        ([0, 2, 4, 5, 7], False, "percent", "62.5"),     # 5/8 = 62.5% (note: indices 2,3 and 6,7 pair into quarters if draw_horiz=False; let's keep draw_horiz=True so all 8 triangles are visibly drawn!)
        ([0, 3, 6], True, "percent", "37.5"),            # 3/8 = 37.5%
        ([1, 5], True, "percent", "25"),                 # 2/8 = 25%
        ([0, 1, 3, 5, 6, 7], True, "percent", "75"),     # 6/8 = 75%
        ([0, 2, 4, 6, 7], True, "percent", "62.5"),      # 5/8 = 62.5%
    ]
    eighths_cases[5] = ([0], True, "percent", "12.5")    # 1/8 = 12.5% — distinct!
    for e_i, (sh_idx, d_h, ask_type, ans_v) in enumerate(eighths_cases):
        qid = next_id()
        k = len(sh_idx)
        s_len = 8 + 2 * e_i
        svg = svg_square_eighths_shaded(sh_idx, draw_horiz=True)
        if ask_type == "fraction":
            q_en = (
                f"A square of side length {m(s_len)} cm is divided by its two diagonals and its vertical and horizontal midlines into congruent small right triangles, "
                "as shown. What **fraction** of the entire square is shaded?"
            )
            q_ar = (
                f"قُسِّم مربع طول ضلعه {m(s_len)} سم بواسطة قطريه والقطعتين الواصلتين بين منتصفات أضلاعه المتقابلة إلى مثلثات صغيرة متطابقة كما في الشكل. "
                "ما **الكسر** الذي يمثّل الجزء المظلّل من مساحة المربع الكلي؟"
            )
            dist = [Fraction(x, 8) for x in range(1, 8) if Fraction(x, 8) != ans_v] + [Fraction(1, 3), Fraction(2, 5)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_v, dist, qid)
        else:
            q_en = (
                f"A square of side length {m(s_len)} cm is divided by its two diagonals and its two midlines into identical small right triangles, as shown. "
                "What **percentage** of the square's area is shaded?"
            )
            q_ar = (
                f"قُسِّم مربع طول ضلعه {m(s_len)} سم بواسطة قطريه ومنصّفَي أضلاعه إلى مثلثات قائمة صغيرة متطابقة كما في الشكل. "
                "ما **النسبة المئوية** للجزء المظلّل من مساحة المربع؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans_v, ["25", "37.5", "50", "62.5", "75", "12.5", "87.5"], qid, suffix="\\%"
            )
        sol_en = explain_en(
            "Because the two diagonals and the two midlines all pass symmetrically through the center of the square, they slice the square into **8 identical (congruent) right triangles**!",
            [
                f"Count the total number of equal small triangles inside the square: there are {m(8)} congruent triangles, so each one is {m('\\frac{1}{8}')} ({m('12.5\\%')}) of the square.",
                f"Count how many of those {m(8)} small triangles are shaded: exactly {m(k)} of them are shaded.",
                (
                    f"Write the fraction {m(f'\\frac{{{k}}}{{8}}')} and simplify if possible: {m(cans)}."
                    if ask_type == "fraction" else
                    f"Multiply {m(k)} eighths by {m('12.5\\%')} each: {m(f'{k} \\times 12.5\\% = {ans_v}\\%')}."
                ),
            ],
            f"Shaded count = {m(k)} out of {m(8)} equal pieces!",
        )
        sol_ar = explain_ar(
            "يمر القطران ومنصّفا الأضلاع جميعًا بمركز تناظر المربع، فيقسّمونه إلى **8 مثلثات قائمة صغيرة متطابقة تمامًا**!",
            [
                f"العدد الكلي للمثلثات الصغيرة المتساوية المساحة داخل المربع هو {m(8)} مثلثات، مساحة كل واحد منها {m('\\frac{1}{8}')} (أي {m('12.5\\%')}).",
                f"نعدّ المثلثات المظلّلة في الشكل فنجدها {m(k)} مثلثات.",
                (
                    f"إذن الكسر المطلوب بعد التبسيط هو {m(f'\\frac{{{k}}}{{8}} = {cans}')}."
                    if ask_type == "fraction" else
                    f"نضرب عدد الأثمان {m(k)} في {m('12.5\\%')} فنحصل على {m(f'{ans_v}\\%')}."
                ),
            ],
            f"عدد الأجزاء المظلّلة {m(k)} من أصل {m(8)} أجزاء متطابقة.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Easy", "g67-square-eighths-shaded",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Notice that all 8 small triangles inside the square have the exact same size! Count how many are shaded.",
            "لاحظ أن المثلثات الـ 8 الصغيرة داخل المربع متطابقة تمامًا! عدّ المظلّل منها فقط.",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 6. Rectilinear staircase perimeter (10 variants) — KMC G6-7 Practice Set 1 Q2
    stair_cases = [
        (10, 6, 3), (12, 8, 3), (15, 9, 4), (14, 10, 3), (18, 12, 4),
        (11, 7, 3), (16, 11, 4), (20, 14, 4), (13, 8, 3), (17, 10, 3),
    ]
    for W, H, st in stair_cases:
        qid = next_id()
        ans = 2 * (W + H)
        svg = svg_rectilinear_staircase(f"{W} cm", f"{H} cm", st)
        q_en = (
            f"All corners in the staircase figure shown are right angles ({m('90^\\circ')}). "
            f"The bottom horizontal side has length {m(W)} cm and the left vertical side has height {m(H)} cm. "
            f"What is the **perimeter** of the entire figure, in cm?"
        )
        q_ar = (
            f"جميع الزوايا في الشكل المدرّج الموضّح زوايا قائمة ({m('90^\\circ')}). "
            f"إذا كان طول القاعدة الأفقية السفلية {m(W)} سم، وطول الضلع الرأسي الأيسر {m(H)} سم، "
            f"فما **محيط** الشكل كاملًا بالسنتيمتر؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [W + H, W * H, ans - W, ans + 2 * st], qid
        )
        sol_en = explain_en(
            "**Pushing-Out Trick:** Even though we don't know the individual step lengths, every horizontal step pushes up to match the full width, and every vertical riser pushes right to match the full height!",
            [
                f"Add all the small **horizontal** step tops together: side-by-side without overlaps, they span the exact same width as the bottom base, {m(W)} cm.",
                f"Add all the small **vertical** step risers together: stacked top-to-bottom, they span the exact same height as the left wall, {m(H)} cm.",
                f"So the staircase has the **exact same perimeter as a {m(W)} cm by {m(H)} cm rectangle**: {m(f'2 \\times ({W} + {H}) = 2 \\times {W + H} = {ans}')} cm!",
            ],
            f"Bottom ({m(W)}) + Top steps ({m(W)}) + Left ({m(H)}) + Right risers ({m(H)}) = {m(ans)} cm!",
        )
        sol_ar = explain_ar(
            "**خدعة إزاحة الأضلاع:** حتى بدون معرفة طول كل درجة منفردة، فإن مجموع القطع الأفقية للدرج يساوي طول القاعدة تمامًا، ومجموع القطع الرأسية يساوي الارتفاع الأيسر تمامًا!",
            [
                f"مجموع جميع القطع الأفقية العلوية للدرج يطابق طول الضلع السفلي ويساوي {m(W)} سم.",
                f"ومجموع جميع القطع الرأسية الجانبية للدرج يطابق طول الضلع الأيسر ويساوي {m(H)} سم.",
                f"إذن محيط الشكل يساوي محيط مستطيل أبعاده {m(W)} و {m(H)}: {m(f'2 \\times ({W} + {H}) = {ans}')} سم.",
            ],
            f"الأسفل ({m(W)}) + الدرجات الأفقية ({m(W)}) + اليسار ({m(H)}) + الدرجات الرأسية ({m(H)}) = {m(ans)} سم.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Easy", "g67-staircase-perimeter",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Imagine sliding all horizontal step edges up to the top and all vertical step edges out to the right!",
            "تخيّل دفع جميع القطع الأفقية للدرج إلى الأعلى وجميع القطع الرأسية إلى اليمين لتكوّن مستطيلًا كاملًا!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 7. Midpoint rotated square inside outer square (10 variants) — KMC G6-7 Practice Set 1 Q3
    mid_sq_cases = [
        (10, True), (8, True), (12, True), (14, True), (6, True),
        (16, True), (20, True), (9, False), (11, False), (18, False),
    ]
    # Note: for odd 9 and 11, s^2/2 = 40.5 and 60.5; let's use even numbers for crisp integers or clean .5! Let's use (10..20) & (4,6,8,12,16)
    mid_sq_cases[7] = (4, False)
    mid_sq_cases[8] = (12, False)
    for s, shade_in in mid_sq_cases:
        qid = next_id()
        outer_a = s * s
        ans = outer_a // 2
        svg = svg_midpoint_square_shaded(f"{s} cm", shade_inner=shade_in)
        region_e = "shaded inner square" if shade_in else "four shaded corner triangles altogether"
        region_a = "المربع الداخلي المظلّل" if shade_in else "المثلثات الأربعة المظلّلة في الزوايا معًا"
        q_en = (
            f"The midpoints of the four sides of a square of side length {m(s)} cm are joined in order, as shown. "
            f"What is the area of the {region_e}, in {m('\\text{cm}^2')}?"
        )
        q_ar = (
            f"وُصلت منتصفات الأضلاع الأربعة لمربع طول ضلعه {m(s)} سم بالترتيب كما في الشكل. "
            f"ما مساحة {region_a} بالوحدة {m('\\text{cm}^2')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [outer_a, outer_a // 4, 3 * outer_a // 4, 4 * s], qid
        )
        half_s = s // 2
        corner_a = (half_s * half_s) // 2 if (half_s * half_s) % 2 == 0 else (half_s * half_s) / 2
        sol_en = explain_en(
            "Joining the four midpoints cuts off **4 identical corner right triangles** whose total area is always **exactly half** of the big square!",
            [
                f"Find the area of the outer square first: {m(f'{s} \\times {s} = {outer_a}\\text{{ cm}}^2')}.",
                f"Each midpoint splits the {m(s)} cm side into two halves of {m(half_s)} cm. So each unshaded/corner right triangle has legs {m(half_s)} cm and {m(half_s)} cm, with area {m(f'\\frac{{1}}{{2}} \\times {half_s} \\times {half_s} = {corner_a:g}\\text{{ cm}}^2')}.",
                f"All **4** corner triangles together have area {m(f'4 \\times {corner_a:g} = {ans}\\text{{ cm}}^2')}, and subtracting from {m(outer_a)} leaves {m(f'{outer_a} - {ans} = {ans}\\text{{ cm}}^2')} for the inner tilted square too!",
            ],
            f"Visual folding check: fold the 4 corner triangles inward over the midpoint lines—they cover the inner square with zero overlap, proving both regions equal {m(ans)} {m('\\text{cm}^2')}!",
        )
        sol_ar = explain_ar(
            "عند توصيل منتصفات أضلاع أي مربع تتكوّن في الزوايا **4 مثلثات قائمة متطابقة** مجموع مساحاتها يساوي **نصف مساحة المربع الكبير** دائمًا!",
            [
                f"مساحة المربع الكبير تساوي {m(f'{s} \\times {s} = {outer_a}\\text{{ cm}}^2')}.",
                f"نصف طول الضلع يساوي {m(half_s)} سم، لذا مساحة كل مثلث قائم في الزاوية تساوي {m(f'\\frac{{1}}{{2}} \\times {half_s} \\times {half_s} = {corner_a:g}\\text{{ cm}}^2')}.",
                f"مجموع مساحات المثلثات الأربعة هو {m(f'4 \\times {corner_a:g} = {ans}\\text{{ cm}}^2')}، ويتبقى للمربع الداخلي أيضًا {m(f'{outer_a} - {ans} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"بطيّ مثلثات الزوايا الأربع إلى الداخل تنطبق تمامًا على المربع الداخلي، مما يؤكد أن المساحة المطلوبة تساوي {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Easy", "g67-midpoint-tilted-square",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the area of the big {s} × {s} square, then subtract (or sum) the four right triangles at the corners!",
            f"احسب مساحة المربع الكبير ({s} × {s})، ثم احسب مساحة المثلثات القائمة الأربعة في الزوايا!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 8. Corner-inscribed oblique shaded triangle in rectangle via 3-right-triangle subtraction (10 variants)
    oblique_cases = [
        (10, 8, 4, 2),   # rect 80 - (16 + 6 + 20) = 38
        (12, 8, 6, 4),   # rect 96 - (24 + 12 + 24) = 36
        (10, 6, 4, 2),   # rect 60 - (12 + 6 + 10) = 32
        (12, 10, 4, 4),  # rect 120 - (20 + 24 + 24) = 52
        (8, 6, 2, 2),    # rect 48 - (6 + 12 + 8) = 22
        (14, 8, 6, 2),   # rect 112 - (24 + 24 + 14) = 50
        (12, 6, 4, 2),   # rect 72 - (12 + 16 + 12) = 32
        (10, 10, 6, 4),  # rect 100 - (30 + 12 + 20) = 38
        (16, 8, 6, 4),   # rect 128 - (24 + 20 + 32) = 52
        (14, 10, 4, 6),  # rect 140 - (20 + 20 + 42) = 58
    ]
    for L, W, ct, cr in oblique_cases:
        qid = next_id()
        rect_a = L * W
        # White right triangles:
        # 1) top-left: legs W and ct -> area = W * ct / 2
        # 2) top-right: legs (L - ct) and (W - cr) -> area = (L - ct)*(W - cr)/2
        # 3) bottom-right: legs L and cr -> area = L * cr / 2
        t1 = (W * ct) // 2
        t2 = ((L - ct) * (W - cr)) // 2
        t3 = (L * cr) // 2
        ans = rect_a - (t1 + t2 + t3)
        svg = svg_inscribed_corner_triangle_in_rect(L, W, ct, cr)
        q_en = (
            f"A rectangle of length {m(L)} cm and width {m(W)} cm has a shaded triangle inside it with one vertex at the bottom-left corner, "
            f"one vertex on the top edge ({m(ct)} cm from the left), and one vertex on the right edge ({m(cr)} cm from the bottom), as shown. "
            f"What is the area of the shaded triangle, in {m('\\text{cm}^2')}?"
        )
        q_ar = (
            f"مستطيل طوله {m(L)} سم وعرضه {m(W)} سم، رُسم بداخله مثلث مظلّل يقع أحد رؤوسه عند الزاوية السفلية اليسرى، "
            f"ورأس ثانٍ على الضلع العلوي (على بُعد {m(ct)} سم من اليسار)، ورأس ثالث على الضلع الأيمن (على بُعد {m(cr)} سم من الأسفل) كما في الشكل. "
            f"ما مساحة المثلث المظلّل بالوحدة {m('\\text{cm}^2')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [rect_a // 2 if rect_a // 2 != ans else ans + 4, ans + 4, ans - 4, t1 + t2 + t3], qid
        )
        sol_en = explain_en(
            "Because none of the shaded triangle's sides are horizontal or vertical, **do NOT guess a base and height**! Instead, find the rectangle's area and **subtract the 3 easy white right triangles** around the outside!",
            [
                f"**Full rectangle area:** {m(f'{L} \\times {W} = {rect_a}\\text{{ cm}}^2')}.",
                f"**Three white right triangles** (each has {m('\\text{Area} = \\frac{1}{2} \\times \\text{leg}_1 \\times \\text{leg}_2')}): "
                f"Top-left {m(f'= \\frac{{1}}{{2}} \\times {W} \\times {ct} = {t1}')}; "
                f"Top-right {m(f'= \\frac{{1}}{{2}} \\times {L-ct} \\times {W-cr} = {t2}')}; "
                f"Bottom-right {m(f'= \\frac{{1}}{{2}} \\times {L} \\times {cr} = {t3}')}.",
                f"**Subtract white areas from the rectangle:** {m(f'{rect_a} - ({t1} + {t2} + {t3}) = {rect_a} - {t1+t2+t3} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"Check: {m(f'{ans} + {t1} + {t2} + {t3} = {rect_a}\\text{{ cm}}^2')}, accounting for 100% of the rectangle!",
        )
        sol_ar = explain_ar(
            "أضلاع المثلث المظلّل مائلة، لذا **لا نحاول تخمين قاعدته وارتفاعه مباشرة**! الطريقة الأذكى والأسهل هي حساب مساحة المستطيل الكامل ثم **طرح مساحات المثلثات القائمة الثلاثة البيضاء** المحيطة به!",
            [
                f"**مساحة المستطيل الكامل:** {m(f'{L} \\times {W} = {rect_a}\\text{{ cm}}^2')}.",
                f"**مساحات المثلثات القائمة البيضاء الثلاثة:** "
                f"العلوي الأيسر {m(f'= \\frac{{1}}{{2}} \\times {W} \\times {ct} = {t1}')}؛ "
                f"والعلوي الأيمن {m(f'= \\frac{{1}}{{2}} \\times {L-ct} \\times {W-cr} = {t2}')}؛ "
                f"والسفلي الأيمن {m(f'= \\frac{{1}}{{2}} \\times {L} \\times {cr} = {t3}')}.",
                f"**مساحة المثلث المظلّل:** {m(f'{rect_a} - ({t1} + {t2} + {t3}) = {rect_a} - {t1+t2+t3} = {ans}\\text{{ cm}}^2')}.",
            ],
            f"تحقق بالجمع: {m(f'{ans} + {t1} + {t2} + {t3} = {rect_a}\\text{{ cm}}^2')} وهي مساحة المستطيل كاملة.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Hard", "g67-oblique-triangle-subtraction",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Find the full rectangle's area, then subtract the areas of the 3 unshaded right-angled corner triangles!",
            "احسب مساحة المستطيل الكامل، ثم اطرح منها مساحات المثلثات القائمة البيضاء الثلاثة في الأطراف!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 9. Parallel-line zigzag angle puzzle (10 variants with parallel-zigzag SVG!)
    zig_cases = [
        (35, 45), (42, 38), (28, 54), (47, 43), (33, 52),
        (25, 61), (39, 46), (51, 34), (29, 48), (44, 51),
    ]
    for a1, a2 in zig_cases:
        qid = next_id()
        ans = a1 + a2
        svg = svg_parallel_zigzag(f"{a1}°", "?°", f"{a2}°")
        q_en = (
            f"In the figure shown, horizontal lines {m('L_1')} and {m('L_2')} are parallel. "
            f"A bent path between them makes acute angles of {m(f'{a1}^\\circ')} with {m('L_1')} and {m(f'{a2}^\\circ')} with {m('L_2')}. "
            f"What is the measure of the middle bend angle marked {m('?^\\circ')}?"
        )
        q_ar = (
            f"في الشكل الموضّح، المستقيمان الأفقيان {m('L_1')} و {m('L_2')} متوازيان. "
            f"يصنع المسار المنكسر بينهما زاويتين حادتين قياساهما {m(f'{a1}^\\circ')} مع {m('L_1')} و {m(f'{a2}^\\circ')} مع {m('L_2')}. "
            f"ما قياس الزاوية الوسطى المشار إليها بالعلامة {m('?^\\circ')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [180 - ans, abs(a1 - a2) + 40, ans + 10, ans - 10], qid, suffix="^\\circ"
        )
        sol_en = explain_en(
            "Golden Parallel-Lines Trick: **Draw a helper horizontal line right through the middle bend** parallel to both `L₁` and `L₂`!",
            [
                f"Draw a helper horizontal line through the middle vertex parallel to {m('L_1')} and {m('L_2')}. It splits angle {m('?')} into an **upper part** and a **lower part**.",
                f"By the **Z-angles (alternate interior angles)** rule with {m('L_1')}, the upper part equals {m(f'{a1}^\\circ')}.",
                f"By the **Z-angles** rule with {m('L_2')}, the lower part equals {m(f'{a2}^\\circ')}. Add them together: {m(f'{a1}^\\circ + {a2}^\\circ = {ans}^\\circ')}!",
            ],
            f"Both acute Z-angles tuck into the middle bend, giving {m(f'{ans}^\\circ')}.",
        )
        sol_ar = explain_ar(
            "الحيلة الذهبية في خطوط التوازي المنكسرة: **ارسم خطًا أفقيًا مساعدًا يمر برأس الزاوية الوسطى** موازيًا للمستقيمين `L₁` و `L₂`!",
            [
                f"يقسم هذا الخط المساعد الزاوية المطلوبة {m('?')} إلى جزأين: **جزء علوي** و**جزء سفلي**.",
                f"بالتبادل الداخلي (حرف Z) مع المستقيم العلوي {m('L_1')}، يساوي الجزء العلوي {m(f'{a1}^\\circ')}.",
                f"وبالتبادل الداخلي (حرف Z) مع المستقيم السفلي {m('L_2')}، يساوي الجزء السفلي {m(f'{a2}^\\circ')}. نجمعهما معًا: {m(f'{a1}^\\circ + {a2}^\\circ = {ans}^\\circ')}!",
            ],
            f"مجموع الزاويتين المتبادلتين يعطي الزاوية الوسطى كاملة وهي {m(f'{ans}^\\circ')}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-parallel-zigzag-angle",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Draw a third horizontal line right through the middle bend, parallel to L₁ and L₂, to create two Z-angles!",
            "ارسم مستقيمًا أفقيًا ثالثًا يمر بالرأس الأوسط موازيًا لـ L₁ و L₂ لتحصل على زاويتين متبادلتين (حرف Z)!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 10. 3D Cuboid water tank — water height rise / remaining capacity (10 variants with 3D tank SVG!)
    tank_cases = [
        (20, 15, 12, 8, 600),    # base=300, +600 cm^3 => +2 cm => new height 10 cm
        (25, 10, 14, 7, 750),    # base=250, +750 => +3 cm => 10 cm
        (20, 10, 15, 6, 800),    # base=200, +800 => +4 cm => 10 cm
        (30, 12, 16, 9, 1080),   # base=360, +1080 => +3 cm => 12 cm
        (16, 10, 12, 5, 480),    # base=160, +480 => +3 cm => 8 cm
        (24, 15, 18, 10, 1440),  # base=360, +1440 => +4 cm => 14 cm
        (20, 20, 15, 6, 1200),   # base=400, +1200 => +3 cm => 9 cm
        (18, 10, 14, 8, 540),    # base=180, +540 => +3 cm => 11 cm
        (25, 12, 16, 9, 1200),   # base=300, +1200 => +4 cm => 13 cm
        (30, 15, 20, 11, 1800),  # base=450, +1800 => +4 cm => 15 cm
    ]
    for L, W, H, h0, vol_stone in tank_cases:
        qid = next_id()
        base_a = L * W
        assert vol_stone % base_a == 0
        dh = vol_stone // base_a
        ans = h0 + dh
        assert ans < H
        svg = svg_water_tank_3d(f"{L} cm", f"{W} cm", f"{H} cm", round(h0 / H, 2))
        q_en = (
            f"A rectangular glass tank has base length {m(L)} cm, base width {m(W)} cm, and total height {m(H)} cm. "
            f"It initially contains water to a depth of {m(h0)} cm. When a solid metal block of volume {m(vol_stone)} {m('\\text{cm}^3')} "
            f"is completely submerged at the bottom (with no overflow), what is the **new water depth**, in cm?"
        )
        q_ar = (
            f"حوض زجاجي على شكل متوازي مستطيلات طول قاعدته {m(L)} سم وعرضها {m(W)} سم وارتفاعه الكلي {m(H)} سم، "
            f"يحتوي في البداية على ماء بارتفاع {m(h0)} سم. عند غمر قطعة معدنية مصمتة حجمها {m(vol_stone)} {m('\\text{cm}^3')} "
            f"بالكامل في القاع (دون أن يفيض الماء)، كم يصبح **الارتفاع الجديد للماء** بالسنتيمتر؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [dh, ans + 2, ans - 1, H], qid
        )
        sol_en = explain_en(
            "When a solid object sinks completely underwater, it pushes the water up by an extra volume **equal to the object's volume**! Since Volume = Base Area × Height Change, divide the block's volume by the tank's base area!",
            [
                f"**Base area of the tank:** {m(f'{L} \\times {W} = {base_a}\\text{{ cm}}^2')}.",
                f"**Rise in water level:** Divide the submerged volume by the base area: {m(f'{vol_stone} \\div {base_a} = {dh}')} cm.",
                f"**New water depth:** Add the rise to the starting depth: {m(f'{h0} + {dh} = {ans}')} cm (careful: {m(dh)} cm is only the *increase*, while {m(ans)} cm is the *new depth*!).",
            ],
            f"Check total volume: initial water {m(f'{base_a}\\times{h0} = {base_a*h0}')} + block {m(vol_stone)} = {m(base_a * ans)} {m('\\text{cm}^3')}, which fills {m(f'{base_a} \\times {ans}')}!",
        )
        sol_ar = explain_ar(
            "عند غمر جسم صلب بالكامل في الماء، فإنه يرفع مستوى الماء بحجم مساوٍ لحجم الجسم! وبما أن الحجم = مساحة القاعدة × مقدار الارتفاع، نقسم حجم القطعة على مساحة القاعدة!",
            [
                f"**مساحة قاعدة الحوض:** {m(f'{L} \\times {W} = {base_a}\\text{{ cm}}^2')}.",
                f"**مقدار ارتفاع الماء:** نقسم حجم القطعة على مساحة القاعدة: {m(f'{vol_stone} \\div {base_a} = {dh}')} سم.",
                f"**الارتفاع الجديد للماء:** نضيف الزيادة إلى الارتفاع الابتدائي: {m(f'{h0} + {dh} = {ans}')} سم.",
            ],
            f"احذر من التوقف عند {m(dh)} سم؛ فـ {m(dh)} هو مقدار الزيادة فقط، بينما الارتفاع الجديد للماء هو {m(ans)} سم.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-water-tank-displacement",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Divide the block's volume ({vol_stone}) by the tank's base area ({L} × {W}) to find how many cm the water rises, then add {h0}!",
            f"اقسم حجم القطعة ({vol_stone}) على مساحة القاعدة ({L} × {W}) لمعرفة مقدار ارتفاع الماء، ثم أضفه إلى {h0}!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 11. Shaded triangle/quadrilateral on a 1x1 unit square grid (10 variants with grid SVG!)
    def poly_area2(verts):
        # Shoelace * 2 (exact integer for lattice polygons!)
        n = len(verts)
        s = 0
        for i in range(n):
            x1, y1 = verts[i]
            x2, y2 = verts[(i + 1) % n]
            s += x1 * y2 - x2 * y1
        return abs(s)

    grid_cases = [
        (5, 4, [(0, 0), (5, 1), (2, 4)], ["A", "B", "C"]),          # 2A = |0 + 20 + 0 - 2 - 0 - 0| = 18 => 9
        (6, 4, [(0, 1), (6, 0), (4, 4)], ["A", "B", "C"]),          # 2A = |(6,-1)x(4,3)| = |18 - (-4)| = 22 => 11
        (5, 5, [(0, 1), (5, 0), (4, 5), (1, 4)], ["A", "B", "C", "D"]), # even 2A? Let's check parity!
        (6, 4, [(0, 0), (6, 2), (2, 4)], ["A", "B", "C"]),          # 2A = |24 - 4| = 20 => 10
        (5, 4, [(1, 0), (5, 2), (0, 4)], ["A", "B", "C"]),          # (4,2)x(-1,4)=16+2=18 => 9
        (6, 5, [(0, 0), (6, 1), (3, 5)], ["A", "B", "C"]),          # (6,1)x(3,5)=30-3=27 -> 13.5
        (6, 5, [(0, 1), (6, 1), (4, 5), (1, 5)], ["A", "B", "C", "D"]), # trapezoid base1=6, base2=3, h=4 => 18!
        (5, 5, [(0, 0), (5, 2), (3, 5), (0, 3)], ["A", "B", "C", "D"]),
        (6, 4, [(0, 2), (3, 0), (6, 2), (3, 4)], ["A", "B", "C", "D"]), # rhombus d1=6, d2=4 => 12!
        (6, 6, [(0, 0), (6, 2), (4, 6)], ["A", "B", "C"]),          # (6,2)x(4,6)=36-8=28 => 14!
    ]
    # Make sure all 10 give crisp integer areas!
    grid_cases[2] = (5, 5, [(0, 2), (4, 0), (5, 4), (1, 5)], ["A", "B", "C", "D"])
    grid_cases[5] = (6, 5, [(0, 0), (6, 2), (2, 5)], ["A", "B", "C"])  # (6,2)x(2,5)=30-4=26 => 13!
    grid_cases[7] = (5, 5, [(0, 0), (5, 1), (4, 5), (0, 3)], ["A", "B", "C", "D"])
    for gw, gh, verts, vnames in grid_cases:
        qid = next_id()
        a2 = poly_area2(verts)
        ans = a2 // 2 if a2 % 2 == 0 else a2 / 2
        svg = svg_grid_polygon(gw, gh, verts, vnames)
        shape_e = "triangle" if len(verts) == 3 else "quadrilateral"
        shape_a = "المثلث" if len(verts) == 3 else "الشكل الرباعي"
        v_desc = ", ".join(f"{nm}({vx},{vy})" for nm, (vx, vy) in zip(vnames, verts))
        q_en = (
            f"On the {m(f'{gw} \\times {gh}')} grid of {m('1 \\text{ cm} \\times 1 \\text{ cm}')} unit squares shown, "
            f"the shaded {shape_e} has vertices {m(v_desc)} on grid intersections. "
            f"What is the area of the shaded {shape_e}, in {m('\\text{cm}^2')}?"
        )
        q_ar = (
            f"على شبكة أبعادها {m(f'{gw} \\times {gh}')} مكوّنة من مربعات وحدة صغيرة مساحة كلٍّ منها {m('1\\text{ cm}^2')} كما في الشكل، "
            f"تقع رؤوس {shape_a} المظلّل عند تقاطعات الشبكة {m(v_desc)}. ما مساحة {shape_a} المظلّل بالوحدة {m('\\text{cm}^2')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 1, ans - 1, ans + 2, gw * gh // 2 if gw * gh // 2 != ans else ans + 3], qid
        )
        # Compute bounding box area & unshaded subtraction
        min_x, max_x = min(x for x, _ in verts), max(x for x, _ in verts)
        min_y, max_y = min(y for _, y in verts), max(y for _, y in verts)
        bb_area = (max_x - min_x) * (max_y - min_y)
        outside = bb_area - ans
        sol_en = explain_en(
            "**Bounding-Box Method:** Enclose the slanted grid shape tightly inside its outer grid rectangle, compute that rectangle's area, and subtract the unshaded right triangles/pieces around its edges!",
            [
                f"The tightest grid rectangle surrounding the shaded {shape_e} spans {m(max_x - min_x)} units wide by {m(max_y - min_y)} units tall, giving a box area of {m(f'{max_x - min_x} \\times {max_y - min_y} = {bb_area}\\text{{ cm}}^2')}.",
                f"Compute the unshaded corner right-triangle areas along the grid border (using {m('\\frac{1}{2} \\times \\text{base} \\times \\text{height}')} by counting grid squares): their combined unshaded area inside the box is {m(f'{outside:g}\\text{{ cm}}^2')}.",
                f"Subtract from the bounding box: {m(f'{bb_area} - {outside:g} = {ans:g}\\text{{ cm}}^2')}.",
            ],
            f"Shaded area ({m(f'{ans:g}')}) + unshaded border pieces ({m(f'{outside:g}')}) = full {m(f'{max_x-min_x}\\times{max_y-min_y}')} grid box ({m(bb_area)})!",
        )
        sol_ar = explain_ar(
            "**طريقة المستطيل المحيط:** نحيط الشكل المائل بمستطيل على خطوط الشبكة، نحسب مساحته بسهولة، ثم نطرح منه مساحات المثلثات القائمة البيضاء المحيطة به!",
            [
                f"المستطيل المحيط بالشكل عرضه {m(max_x - min_x)} وحدات وارتفاعه {m(max_y - min_y)} وحدات، فمساحته {m(f'{max_x - min_x} \\times {max_y - min_y} = {bb_area}\\text{{ cm}}^2')}.",
                f"نحسب مساحات الأجزاء القائمة غير المظلّلة حول الشكل داخل هذا المستطيل (باستخدام قانون نصف القاعدة × الارتفاع من مربعات الشبكة) فنجد مجموعها {m(f'{outside:g}\\text{{ cm}}^2')}.",
                f"نطرحها من مساحة المستطيل المحيط: {m(f'{bb_area} - {outside:g} = {ans:g}\\text{{ cm}}^2')}.",
            ],
            f"مجموع المساحة المظلّلة ({m(f'{ans:g}')}) والأجزاء البيضاء ({m(f'{outside:g}')}) يساوي مساحة الإطار ({m(bb_area)}) تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Geometry", "Medium", "g67-grid-polygon-area",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Take the area of the surrounding grid rectangle and subtract the easy right-angled white triangles around the shaded shape!",
            "احسب مساحة المستطيل المحيط بالشكل ثم اطرح مساحات المثلثات القائمة البيضاء في الزوايا!",
            sol_en, sol_ar, diagram_en=svg
        ))

    assert len(items) == 110, f"Expected 110 items, got {len(items)}"
    return items


if __name__ == "__main__":
    qs = generate_t1_geometry()
    print(f"Generated {len(qs)} Track 1 Geometry questions (all with KMC SVGs!) cleanly.")
