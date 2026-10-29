"""Track 3 (Grades 10-11) — Geometry (115 authentic KMC Senior problems, 100% with SVGs)."""
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
from kmc_diagrams import (
    svg_congruent_inner_triangles,
    svg_cube_in_cylinder,
    svg_grid_polygon,
    svg_midpoint_square_shaded,
    svg_overlapping_rects,
    svg_regular_polygon,
    svg_square_circle_shaded,
    svg_subdivided_apex_triangle,
    svg_subdivided_rect_3x3,
    svg_subdivided_triangle_grid,
    svg_trapezoid_semicircle,
    svg_water_tank_3d,
)

LEVEL = "Track 3: Grades 10-11"
TOPIC = "Geometry"


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en, svg_ar=None):
        nonlocal idx
        qid = f"KMC-T3-GEO-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, TOPIC, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg_en, svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 1. Cube inscribed in circular cylinder (KMC Senior Cat B Q5!) (10 Qs)
    # ------------------------------------------------------------------
    cyl_cases = [
        (2, "cyl_vol", "Easy"),
        (4, "cyl_vol", "Easy"),
        (6, "cyl_vol", "Medium"),
        (2, "diff_vol", "Medium"),
        (4, "diff_vol", "Medium"),
        (6, "diff_vol", "Medium"),
        (8, "diff_vol", "Hard"),
        (10, "cyl_vol", "Medium"),
        (8, "cyl_vol", "Hard"),
        (10, "diff_vol", "Hard"),
    ]
    for v_i, (a, ask, diff) in enumerate(cyl_cases):
        svg = svg_cube_in_cylinder(f"{a} cm")
        # Cube edge = a (even so a^3 / 2 is integer!).
        # Cylinder height h = a, base diameter d = a*sqrt(2), so r^2 = a^2 / 2, V_cyl = (a^3 / 2)*pi
        half_c = (a ** 3) // 2
        cube_v = a ** 3
        if ask == "cyl_vol":
            ans_tex = f"{half_c}\\pi"
            d_list = [f"{cube_v}\\pi", f"{cube_v // 4}\\pi", f"{2 * cube_v}\\pi", f"{a * a}\\pi"]
            q_en = (
                f"A cube of edge length {m(a)} cm is inscribed inside the smallest possible right circular cylinder "
                f"(the four top vertices lie on the top rim and the four bottom vertices lie on the bottom rim, as shown). "
                f"What is the **volume of the cylinder** (in \\( \\text{{cm}}^3 \\))?"
            )
            q_ar = (
                f"وُضع مكعب طول حرفه {m(a)} سم داخل أصغر أسطوانة دائرية قائمة ممكنة بحيث تقع رؤوسه الأربعة العلوية على محيط القاعدة العلوية "
                f"ورؤوسه السفلية على محيط القاعدة السفلية كما في الشكل. ما **حجم الأسطوانة** (بالسنتيمتر المكعب \\( \\text{{cm}}^3 \\))؟"
            )
            last_step_en = f"Cylinder volume: {m(f'V = \\pi r^2 h = \\pi \\left(\\frac{{{a*a}}}{{2}}\\right)({a}) = {ans_tex}')}."
            last_step_ar = f"حجم الأسطوانة: {m(f'V = \\pi r^2 h = \\pi \\left(\\frac{{{a*a}}}{{2}}\\right)({a}) = {ans_tex}')}."
        else:
            ans_tex = f"{half_c}\\pi - {cube_v}"
            d_list = [f"{cube_v}\\pi - {cube_v}", f"{cube_v // 4}\\pi - {cube_v}", f"{half_c}\\pi - {a*a}", f"{2*cube_v}\\pi - {cube_v}"]
            q_en = (
                f"A cube of edge length {m(a)} cm fits tightly inside a right circular cylinder of height {m(a)} cm, "
                f"with all {m(8)} vertices touching the circular rims as shown. What is the **volume of the empty space** inside the cylinder outside the cube?"
            )
            q_ar = (
                f"يستقر مكعب طول حرفه {m(a)} سم بإحكام داخل أسطوانة دائرية قائمة ارتفاعها {m(a)} سم بحيث تمس رؤوسه الثمانية حافتي القاعدتين كما في الشكل. "
                f"ما **حجم الفراغ المتبقي** داخل الأسطوانة خارج المكعب؟"
            )
            last_step_en = f"Subtract the cube volume {m(f'{a}^3 = {cube_v}')} from the cylinder volume {m(f'{half_c}\\pi')}: {m(ans_tex)}."
            last_step_ar = f"نطرح حجم المكعب {m(f'{a}^3 = {cube_v}')} من حجم الأسطوانة {m(f'{half_c}\\pi')}: {m(ans_tex)}."

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3g_cyl_{v_i}")
        h_en = "Look from directly above! The top square of side a is inscribed in the circular base, so the circle's DIAMETER equals the square's DIAGONAL a√2!"
        h_ar = "انظر للشكل من الأعلى! الوجه العلوي للمكعب (مربع ضلعه a) محاط بدائرة القاعدة، لذا فإن **قطر الدائرة** يساوي **قطر المربع** a√2!"
        s_en = explain_en(
            "Top-down view secret: when a square of side \\( a \\) is inscribed in a circle, the square's diagonal \\( a\\sqrt{2} \\) is the circle's **diameter**!",
            [
                f"By the Pythagorean theorem on the top face, diagonal {m(f'd = \\sqrt{{{a}^2 + {a}^2}} = {a}\\sqrt{{2}}')} cm.",
                f"So the cylinder's radius is {m(f'r = \\frac{{{a}\\sqrt{{2}}}}{{2}}')}, which means {m(f'r^2 = \\frac{{2 \\times {a*a}}}{{4}} = { (a*a)//2 }')}, and height {m(f'h = {a}')}.",
                last_step_en,
            ],
            f"Since \\( \\frac{{\\pi}}{{2}} \\approx 1.57 > 1 \\), the cylinder volume \\( {half_c}\\pi \\) is strictly greater than the cube volume \\( {cube_v} \\)!",
        )
        s_ar = explain_ar(
            "سر المسقط العلوي: عندما يُحاط مربع ضلعه \\( a \\) بدائرة، فإن **قطر المربع** \\( a\\sqrt{2} \\) هو نفسه **قطر الدائرة**!",
            [
                f"من فيثاغورس على المربع العلوي، طول القطر {m(f'd = {a}\\sqrt{{2}}')} سم.",
                f"إذن نصف قطر قاعدة الأسطوانة {m(f'r = \\frac{{{a}\\sqrt{{2}}}}{{2}}')}، ومنه {m(f'r^2 = {(a*a)//2}')}، وارتفاعها {m(f'h = {a}')}.",
                last_step_ar,
            ],
            f"بما أن \\( \\frac{{\\pi}}{{2}} \\approx 1.57 > 1 \\)، فإن حجم الأسطوانة أكبر فعلاً من حجم المكعب!",
        )
        push(diff, "kmc_g1011_cube_in_cylinder", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 2. Congruent inner triangles △APQ ≅ △CPB in isosceles △ABC (KMC Senior Q6!) (10 Qs)
    # ------------------------------------------------------------------
    cong_cases = [
        (37, "\\angle AQC", "Easy"),
        (35, "\\angle AQC", "Easy"),
        (40, "\\angle AQC", "Medium"),
        (42, "\\angle AQP", "Medium"),
        (38, "\\angle AQP", "Medium"),
        (44, "\\angle PAQ", "Medium"),
        (36, "\\angle PAQ", "Medium"),
        (46, "\\angle AQC", "Hard"),
        (48, "\\angle AQP", "Hard"),
        (50, "\\angle PAQ", "Hard"),
    ]
    for v_i, (alpha, target_ang, diff) in enumerate(cong_cases):
        svg = svg_congruent_inner_triangles(alpha)
        if target_ang == "\\angle AQC":
            ans = 90 + alpha
        elif target_ang == "\\angle AQP":
            ans = 90 - alpha
        else:
            ans = alpha - 30
        distractors = [90 + alpha, 90 - alpha, alpha - 30, 180 - 2 * alpha, 120 - alpha, 2 * alpha]
        distractors = [d for d in distractors if d != ans and d > 0]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_cong_{v_i}", suffix="^\\circ")
        q_en = (
            f"In isosceles triangle {m('ABC')} with {m('AB = BC')} and {m(f'\\angle BAC = \\angle BCA = {alpha}^\\circ')}, "
            f"point {m('P')} lies inside {m('\\triangle ABC')} and point {m('Q')} lies on segment {m('PC')} such that "
            f"{m('\\triangle APQ \\cong \\triangle CPB')} (with {m('A \\leftrightarrow C')}, {m('P \\leftrightarrow P')}, {m('Q \\leftrightarrow B')}). "
            f"What is the measure of {m(target_ang)}?"
        )
        q_ar = (
            f"في المثلث متطابق الضلعين {m('ABC')} حيث {m('AB = BC')} و{m(f'\\angle BAC = \\angle BCA = {alpha}^\\circ')}، "
            f"تقع النقطة {m('P')} داخل المثلث وتقع النقطة {m('Q')} على القطعة {m('PC')} بحيث يتطابق المثلثان "
            f"{m('\\triangle APQ \\cong \\triangle CPB')} (بالتناظر {m('A \\leftrightarrow C')} و{m('P \\leftrightarrow P')} و{m('Q \\leftrightarrow B')}). "
            f"ما قياس الزاوية {m(target_ang)}؟"
        )
        h_en = "Match corresponding sides & angles carefully: AP = CP puts P on the symmetry line through B, and ∠APQ = ∠CPB around P makes all three angles at P equal 120°!"
        h_ar = "طابق الأضلاع والزوايا المتناظرة: AP = CP يضع P على محور التماثل المار بـ B، وتساوي الزوايا الثلاث حول P يجعل كلاً منها 120°!"
        apex_b = 180 - 2 * alpha
        cbp = 90 - alpha
        s_en = explain_en(
            "From \\( \\triangle APQ \\cong \\triangle CPB \\), we get \\( AP = CP \\) and \\( \\angle APQ = \\angle CPB \\). Since \\( AB = CB \\) and \\( AP = CP \\), line \\( BP \\) is the axis of symmetry of the figure!",
            [
                f"In {m('\\triangle ABC')}, {m(f'\\angle ABC = 180^\\circ - 2({alpha}^\\circ) = {apex_b}^\\circ')}. Because {m('BP')} bisects {m('\\angle ABC')}, {m(f'\\angle CBP = \\frac{{{apex_b}^\\circ}}{{2}} = {cbp}^\\circ')}.",
                f"Since {m('Q')} lies on {m('PC')}, {m('\\angle APC = \\angle APQ = \\angle CPB')}; by symmetry {m('\\angle BPA = \\angle CPB')} too, so all 3 angles around {m('P')} are {m('120^\\circ')} and {m('\\angle PAC = \\angle PCA = 30^\\circ')}.",
                f"By congruence {m(f'\\angle AQP = \\angle CBP = {cbp}^\\circ')}, {m(f'\\angle AQC = 180^\\circ - {cbp}^\\circ = {90+alpha}^\\circ')}, and {m(f'\\angle PAQ = \\angle PCB = {alpha}^\\circ - 30^\\circ = {alpha-30}^\\circ')} — giving {m(f'{target_ang} = {ans}^\\circ')}.",
            ],
            f"Angle sum check in {m('\\triangle APQ')}: {m(f'120^\\circ + {alpha-30}^\\circ + {cbp}^\\circ = 180^\\circ')}!",
        )
        s_ar = explain_ar(
            "من التطابق \\( \\triangle APQ \\cong \\triangle CPB \\) نستنتج \\( AP = CP \\) و\\( \\angle APQ = \\angle CPB \\). وبما أن \\( AB = CB \\) و\\( AP = CP \\)، فإن المستقيم \\( BP \\) محور تماثل للشكل!",
            [
                f"زاوية الرأس {m(f'\\angle ABC = 180^\\circ - 2({alpha}^\\circ) = {apex_b}^\\circ')}، وينصّفها {m('BP')} فيكون {m(f'\\angle CBP = {cbp}^\\circ')}.",
                f"بما أن {m('Q')} على {m('PC')} فإن الزوايا الثلاث حول {m('P')} متساوية وتساوي {m('120^\\circ')}، ومنه {m('\\angle PCA = 30^\\circ')}.",
                f"من التطابق: {m(f'\\angle AQP = \\angle CBP = {cbp}^\\circ')}، ومكملتها {m(f'\\angle AQC = {90+alpha}^\\circ')}، و{m(f'\\angle PAQ = {alpha-30}^\\circ')} — إذن {m(f'{target_ang} = {ans}^\\circ')}.",
            ],
            f"تحقق من مجموع زوايا {m('\\triangle APQ')}: {m(f'120^\\circ + {alpha-30}^\\circ + {cbp}^\\circ = 180^\\circ')}!",
        )
        push(diff, "kmc_g1011_congruent_inner_triangles", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 3. Subdivided triangle grid — shaded fraction (KMC page_d-018.png!) (10 Qs)
    # ------------------------------------------------------------------
    tgrid_cases = [
        (3, [(1, 0, "U"), (3, 0, "U"), (3, 2, "U")], "Easy"),
        (3, [(2, 0, "D"), (3, 0, "D"), (3, 1, "D"), (1, 0, "U")], "Easy"),
        (4, [(1, 0, "U"), (2, 0, "D"), (3, 1, "D"), (4, 0, "U"), (4, 3, "U")], "Easy"),
        (4, [(2, 0, "U"), (2, 1, "U"), (3, 0, "D"), (3, 1, "D"), (4, 1, "U"), (4, 2, "U")], "Medium"),
        (4, [(1, 0, "U"), (3, 0, "U"), (3, 1, "U"), (3, 2, "U"), (4, 0, "D"), (4, 1, "D"), (4, 2, "D")], "Medium"),
        (5, [(1, 0, "U"), (3, 1, "U"), (5, 0, "U"), (5, 2, "U"), (5, 4, "U")], "Medium"),
        (5, [(2, 0, "D"), (3, 0, "D"), (3, 1, "D"), (4, 0, "D"), (4, 1, "D"), (4, 2, "D"), (5, 1, "D"), (5, 2, "D")], "Medium"),
        (4, [(1, 0, "U"), (2, 0, "D"), (3, 0, "U"), (3, 2, "U"), (4, 0, "D"), (4, 1, "U"), (4, 2, "D"), (4, 3, "U"), (2, 1, "U")], "Hard"),
        (5, [(1, 0, "U"), (2, 0, "D"), (3, 0, "U"), (3, 2, "U"), (4, 1, "D"), (4, 2, "D"), (5, 0, "U"), (5, 1, "U"), (5, 3, "U"), (5, 4, "U")], "Hard"),
        (5, [(2, 0, "U"), (2, 1, "U"), (3, 1, "U"), (4, 1, "U"), (4, 2, "U"), (5, 0, "D"), (5, 1, "D"), (5, 2, "D"), (5, 3, "D"), (1, 0, "U"), (3, 0, "D")], "Hard"),
    ]
    for v_i, (n, coords, diff) in enumerate(tgrid_cases):
        svg = svg_subdivided_triangle_grid(n, coords)
        k_sh = len(coords)
        tot_u = n * n
        ans = Fraction(k_sh, tot_u)
        distractors = [
            Fraction(k_sh, tot_u - k_sh),
            Fraction(max(1, k_sh - 1), tot_u),
            Fraction(min(tot_u - 1, k_sh + 1), tot_u),
            Fraction(k_sh, n * (n + 1) // 2),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_tg_{v_i}")
        s_tri = n * (v_i + 2)
        q_en = (
            f"Each side of an equilateral triangle {m('ABC')} of side length {m(s_tri)} cm is divided into {m(n)} equal segments, and lines parallel to the sides "
            f"partition {m('\\triangle ABC')} into congruent small triangles, as shown. What **fraction** of the area of {m('\\triangle ABC')} is shaded?"
        )
        q_ar = (
            f"قُسِّم كل ضلع من أضلاع المثلث المتطابق الأضلاع {m('ABC')} الذي طول ضلعه {m(s_tri)} سم إلى {m(n)} قطع متساوية، ورُسمت مستقيمات موازية للأضلاع "
            f"لتقسيم {m('\\triangle ABC')} إلى مثلثات صغيرة متطابقة كما في الشكل. ما **الكسر** الذي يمثّل مساحة الجزء المظلّل من مساحة {m('\\triangle ABC')}؟"
        )
        h_en = f"Dividing each side of a triangle into n = {n} equal parts splits the total area into n² = {tot_u} congruent small triangles (both upright and upside-down)!"
        h_ar = f"تقسيم كل ضلع في مثلث إلى n = {n} أجزاء متساوية يقسم المساحة الكلية إلى n² = {tot_u} مثلثاً صغيراً متطابقاً (المعتدلة والمقلوبة معاً)!"
        row_odds = " + ".join(str(2 * r - 1) for r in range(1, n + 1))
        s_en = explain_en(
            f"Scaling a triangle's sides by \\( 1/{n} \\) scales area by \\( (1/{n})^2 = 1/{tot_u} \\), so \\( \\triangle ABC \\) consists of exactly \\( {n}^2 = {tot_u} \\) equal-area small triangles!",
            [
                f"Verify by rows from top to bottom: {m(f'{row_odds} = {tot_u}')} congruent small triangles.",
                f"Count the shaded small triangles carefully across the rows: there are **{m(k_sh)}** shaded triangles.",
                f"Form the fraction and simplify: {m(f'\\frac{{{k_sh}}}{{{tot_u}}} = {fmt_val(ans)}')}.",
            ],
            f"Trap check: don't forget to count BOTH upright and upside-down triangles in the denominator ({m(tot_u)}, not {m(n*(n+1)//2)})!",
        )
        s_ar = explain_ar(
            f"تصغير أضلاع المثلث بنسبة \\( 1/{n} \\) يصغّر المساحة بنسبة \\( (1/{n})^2 = 1/{tot_u} \\)، لذا يتكون \\( \\triangle ABC \\) من \\( {n}^2 = {tot_u} \\) مثلثاً صغيراً متساوي المساحة!",
            [
                f"نتأكد بجمع عدد المثلثات في الصفوف من الأعلى للأسفل: {m(f'{row_odds} = {tot_u}')} مثلثاً صغيراً.",
                f"نعدّ المثلثات الصغيرة المظلّلة بدقة: عددها **{m(k_sh)}**.",
                f"نقسم ونبسّط الكسر: {m(f'\\frac{{{k_sh}}}{{{tot_u}}} = {fmt_val(ans)}')}.",
            ],
            f"انتبه: المقام يضم المثلثات المعتدلة والمقلوبة معاً ({m(tot_u)}) وليس المعتدلة وحدها!",
        )
        push(diff, "kmc_g1011_subdivided_triangle_grid", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 4. 3x3 Subdivided rectangle corner perimeter/area invariants (10 Qs)
    # ------------------------------------------------------------------
    r33_cases = [
        # (ws=(w0,w1,w2), hs=(h0,h1,h2), mode: 'perim'|'area', diff)
        ((3, 5, 4), (2, 4, 3), "perim", "Easy"),
        ((4, 6, 5), (3, 5, 4), "perim", "Easy"),
        ((5, 4, 7), (3, 6, 5), "perim", "Medium"),
        ((6, 7, 8), (4, 5, 7), "perim", "Medium"),
        ((7, 5, 9), (5, 8, 6), "perim", "Hard"),
        ((2, 5, 3), (3, 4, 4), "area", "Easy"),
        ((3, 4, 5), (2, 5, 6), "area", "Medium"),
        ((4, 5, 6), (3, 4, 5), "area", "Medium"),
        ((5, 3, 8), (3, 7, 5), "area", "Hard"),
        ((6, 4, 9), (4, 5, 6), "area", "Hard"),
    ]
    for v_i, (ws, hs, mode, diff) in enumerate(r33_cases):
        if mode == "perim":
            c00 = 2 * (ws[0] + hs[0])
            c02 = 2 * (ws[2] + hs[0])
            c20 = 2 * (ws[0] + hs[2])
            c22 = 2 * (ws[2] + hs[2])
            mid = 2 * (ws[1] + hs[1])
            assert c00 + c22 == c02 + c20
            ans = c22
            grid = [[str(c00), "", str(c02)], ["", str(mid), ""], [str(c20), "", "?"]]
            svg = svg_subdivided_rect_3x3(grid)
            distractors = [c02 + c20 - mid, ans + 2, max(4, ans - 2), mid + 4]
            q_en = (
                f"A large rectangle is divided into {m(9)} smaller rectangles by lines parallel to its sides, as shown. "
                f"The numbers inside four of the rectangles indicate their **perimeters** ({m(c00)}, {m(c02)}, {m(mid)}, and {m(c20)}). "
                f"What is the perimeter of the shaded bottom-right corner rectangle {m('?')}?"
            )
            q_ar = (
                f"قُسِّم مستطيل كبير إلى {m(9)} مستطيلات أصغر بمستقيمات موازية لأضلاعه كما في الشكل. "
                f"تمثّل الأعداد المكتوبة داخل أربعة منها **محيطاتها** ({m(c00)} و{m(c02)} و{m(mid)} و{m(c20)}). "
                f"ما محيط المستطيل الركني السفلي الأيمن المظلّل {m('?')}؟"
            )
            steps_en = [
                f"Let the column widths be {m('w_1, w_2, w_3')} and row heights be {m('h_1, h_2, h_3')}. Notice the center rectangle {m(mid)} is a **red herring** (extra unused info)!",
                f"Opposite corner perimeters satisfy {m('P_{1,1} + P_{3,3} = 2(w_1+w_3+h_1+h_3) = P_{1,3} + P_{3,1}')}.",
                f"Solve: {m(f'{c00} + ? = {c02} + {c20} = {c02+c20} \\implies ? = {c02+c20} - {c00} = {ans}')}.",
            ]
            steps_ar = [
                f"نفرض عروض الأعمدة {m('w_1, w_2, w_3')} وارتفاعات الصفوف {m('h_1, h_2, h_3')}. لاحظ أن محيط المستطيل الأوسط {m(mid)} **معلومة إضافية لا نحتاجها**!",
                f"مجموع محيطي الركنين المتقابلين متساوٍ: {m('P_{1,1} + P_{3,3} = P_{1,3} + P_{3,1}')}.",
                f"نحسب: {m(f'{c00} + ? = {c02} + {c20} = {c02+c20} \\implies ? = {ans}')}.",
            ]
        else:
            c00 = ws[0] * hs[0]
            c02 = ws[2] * hs[0]
            c20 = ws[0] * hs[2]
            c22 = ws[2] * hs[2]
            mid = ws[1] * hs[1]
            assert c00 * c22 == c02 * c20
            ans = c22
            grid = [[str(c00), "", str(c02)], ["", str(mid), ""], [str(c20), "", "?"]]
            svg = svg_subdivided_rect_3x3(grid)
            distractors = [c02 + c20 - c00, ans + ws[2], max(2, ans - hs[2]), mid + 5]
            q_en = (
                f"A rectangle is divided into a {m('3 \\times 3')} grid of nine smaller rectangles, as shown. "
                f"The numbers inside four of them give their **areas** ({m(c00)}, {m(c02)}, {m(mid)}, and {m(c20)}). "
                f"What is the area of the shaded bottom-right rectangle {m('?')}?"
            )
            q_ar = (
                f"قُسِّم مستطيل إلى شبكة {m('3 \\times 3')} من تسعة مستطيلات أصغر كما في الشكل. "
                f"الأعداد المكتوبة داخل أربعة منها تمثّل **مساحاتها** ({m(c00)} و{m(c02)} و{m(mid)} و{m(c20)}). "
                f"ما مساحة المستطيل المظلّل في الركن السفلي الأيمن {m('?')}؟"
            )
            steps_en = [
                f"Ignore the middle column and middle row! The four corner rectangles have areas {m('w_1 h_1')}, {m('w_3 h_1')}, {m('w_1 h_3')}, and {m('w_3 h_3')}.",
                f"Opposite corner products match: {m(f'A_{{1,1}} \\times A_{{3,3}} = A_{{1,3}} \\times A_{{3,1}} \\implies {c00} \\times ? = {c02} \\times {c20} = {c02*c20}')}.",
                f"Divide by {m(c00)}: {m(f'? = \\frac{{{c02*c20}}}{{{c00}}} = {ans}')}.",
            ]
            steps_ar = [
                f"لا نحتاج إلى المستطيل الأوسط {m(mid)}! فالمستطيلات الركنية الأربعة مساحاتها {m('w_1 h_1')} و{m('w_3 h_1')} و{m('w_1 h_3')} و{m('w_3 h_3')}.",
                f"حاصل ضرب مساحتي كل ركنين متقابلين متساوٍ: {m(f'{c00} \\times ? = {c02} \\times {c20} = {c02*c20}')}.",
                f"نقسم على {m(c00)}: {m(f'? = \\frac{{{c02*c20}}}{{{c00}}} = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_r33_{v_i}")
        h_en = "Mentally delete the middle row and middle column — the four corners form a 2×2 subdivided rectangle!"
        h_ar = "احذف ذهنياً الصف الأوسط والعمود الأوسط — ستجد أن الأركان الأربعة تكوّن مستطيلاً مقسماً 2×2 تماماً!"
        s_en = explain_en("Deleting the middle row and column collapses the four corners into a 2×2 grid, preserving opposite-corner invariants!", steps_en, f"Notice how KMC often includes a center value ({m(mid)}) to test whether you spot the invariant!")
        s_ar = explain_ar("عند تجاهل الصف والعمود الأوسطين تشترك الأركان الأربعة في نفس العروض والارتفاعات الخارجية تماماً كشبكة 2×2!", steps_ar, f"تضع مسابقة كاوست أحياناً قيمة وسطى ({m(mid)}) لاختبار قدرتك على تمييز المعلومات اللازمة فقط!")
        push(diff, "kmc_g1011_rect_3x3_corners", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 5. Right trapezoid circumscribed around a semicircle (10 Qs)
    # ------------------------------------------------------------------
    trap_cases = [
        (1, 9, "radius", "Easy"),
        (2, 8, "radius", "Easy"),
        (4, 9, "area", "Medium"),
        (3, 12, "area", "Medium"),
        (4, 16, "area", "Medium"),
        (2, 8, "area", "Medium"),
        (9, 16, "radius", "Medium"),
        (4, 9, "semi_area", "Hard"),
        (6, 24, "area", "Hard"),
        (9, 16, "area", "Hard"),
    ]
    for v_i, (a, b, ask, diff) in enumerate(trap_cases):
        r = math.isqrt(a * b)
        assert r * r == a * b
        svg = svg_trapezoid_semicircle(str(a), str(b))
        h_leg = 2 * r
        slant = a + b
        trap_area = (a + b) * r  # (a+b)/2 * (2r) = (a+b)*r
        if ask == "radius":
            ans = r
            distractors = [(a + b) // 2, b - a, 2 * r, r + 2]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_trp_{v_i}")
            ask_en = "What is the **radius** of the semicircle?"
            ask_ar = "ما **نصف قطر** نصف الدائرة؟"
            last_en = f"Divide diameter {m(f'AD = {h_leg}')} by {m(2)}: radius {m(f'r = {r}')}."
            last_ar = f"نقسم القطر {m(f'AD = {h_leg}')} على {m(2)}: نصف القطر {m(f'r = {r}')}."
        elif ask == "area":
            ans = trap_area
            distractors = [(a + b) * (b - a) // 2, (a + b) * (a + b) // 2, trap_area * 2, trap_area + a * b]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_trp_{v_i}")
            ask_en = "What is the **area of the right trapezoid**?"
            ask_ar = "ما **مساحة شبه المنحرف القائم**؟"
            last_en = f"Trapezoid area: {m(f'\\frac{{{a} + {b}}}{{2}} \\times {h_leg} = {trap_area}')}."
            last_ar = f"مساحة شبه المنحرف: {m(f'\\frac{{{a} + {b}}}{{2}} \\times {h_leg} = {trap_area}')}."
        else:
            # semi_area = (1/2) pi r^2 = 18 pi for (4, 9)
            assert (r * r) % 2 == 0
            ans_tex = f"{(r * r) // 2}\\pi"
            d_list = [f"{r * r}\\pi", f"{2 * r * r}\\pi", f"{r}\\pi", f"{(a+b)}\\pi"]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3g_trp_{v_i}")
            ask_en = "What is the **area of the shaded semicircle**?"
            ask_ar = "ما **مساحة نصف الدائرة المظلّل**؟"
            last_en = f"Semicircle area with radius {m(f'r = {r}')}: {m(f'\\frac{{1}}{{2}}\\pi r^2 = \\frac{{1}}{{2}}\\pi ({r*r}) = {ans_tex}')}."
            last_ar = f"مساحة نصف الدائرة بنصف قطر {m(f'r = {r}')}: {m(f'\\frac{{1}}{{2}}\\pi ({r*r}) = {ans_tex}')}."

        q_en = (
            f"A semicircle with center {m('O')} has its diameter along the vertical leg of a right trapezoid, "
            f"and is tangent to the top base (length {m(a)}), the slanted side, and the bottom base (length {m(b)}), as shown. "
            f"{ask_en}"
        )
        q_ar = (
            f"نصف دائرة مركزه {m('O')} يقع قطره على الساق الرأسية لشبه منحرف قائم، "
            f"ويمس القاعدة العلوية (طولها {m(a)}) والضلع المائل والقاعدة السفلية (طولها {m(b)}) كما في الشكل. "
            f"{ask_ar}"
        )
        h_en = f"Two tangent segments from an external point to a circle have EQUAL length! So the slanted side has length {a} + {b} = {slant}!"
        h_ar = f"قطعتا المماس المرسومتان من نقطة خارجية لدائرة متساويتان في الطول! إذن طول الضلع المائل يساوي {a} + {b} = {slant}!"
        s_en = explain_en(
            "Equal tangents from the two right-hand corners show the slanted side has length \\( a + b \\). Dropping a vertical altitude creates a right triangle with hypotenuse \\( a + b \\) and horizontal leg \\( b - a \\)!",
            [
                f"By equal tangents, slanted side = {m(f'{a} + {b} = {slant}')}, and horizontal leg difference = {m(f'{b} - {a} = {b - a}')}.",
                f"By the Pythagorean theorem, vertical leg (diameter) {m(f'AD = \\sqrt{{{slant}^2 - {b-a}^2}} = \\sqrt{{{slant**2 - (b-a)**2}}} = {h_leg}')}.",
                last_en,
            ],
            f"Neat algebraic identity: \\( \\sqrt{{(a+b)^2 - (b-a)^2}} = \\sqrt{{4ab}} = 2\\sqrt{{ab}} \\) always!",
        )
        s_ar = explain_ar(
            "من تساوي قطعتي المماس من كل ركن أيمن، طول الضلع المائل يساوي \\( a + b \\). وبإنزال عمود نحصل على مثلث قائم وتره \\( a + b \\) وضلعه الأفقي \\( b - a \\)!",
            [
                f"الوتر المائل = {m(f'{a} + {b} = {slant}')}، وفرق القاعدتين = {m(f'{b} - {a} = {b - a}')}.",
                f"من فيثاغورس، الساق الرأسية (القطر) {m(f'AD = \\sqrt{{{slant}^2 - {b-a}^2}} = {h_leg}')}.",
                last_ar,
            ],
            f"ملاحظة جميلة: \\( \\sqrt{{(a+b)^2 - (b-a)^2}} = 2\\sqrt{{ab}} \\) دائماً!",
        )
        push(diff, "kmc_g1011_trapezoid_semicircle", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 6. Similar triangles parallel strips 1 : 3 : 5 : ... (KMC Senior!) (10 Qs)
    # ------------------------------------------------------------------
    sim_cases = [
        # (n_strips, given_strip_1based, given_area, ask: 'total' or target_strip_1based, diff)
        (3, 1, 5, "total", "Easy"),       # 5 * 9 = 45
        (3, 2, 12, "total", "Easy"),      # unit=4, total=36
        (3, 3, 25, 1, "Medium"),          # unit=5, strip 1 = 5
        (4, 2, 18, "total", "Medium"),    # unit=6, total=96
        (4, 3, 35, "total", "Medium"),    # unit=7, total=112
        (4, 4, 42, 2, "Medium"),          # unit=6, strip 2 = 18
        (5, 3, 20, "total", "Medium"),    # unit=4, total=100
        (5, 4, 35, 5, "Hard"),            # unit=5, strip 5 = 45
        (5, 2, 27, 4, "Hard"),            # unit=9, strip 4 = 63
        (6, 5, 45, "total", "Hard"),      # unit=5, total=180
    ]
    for v_i, (n_st, g_idx, g_area, ask, diff) in enumerate(sim_cases):
        svg = svg_subdivided_apex_triangle(2, min(n_st, 4))
        odd_g = 2 * g_idx - 1
        assert g_area % odd_g == 0
        unit_a = g_area // odd_g
        if ask == "total":
            ans = unit_a * (n_st ** 2)
            ask_en = "what is the **total area** of the entire large triangle?"
            ask_ar = "فما **المساحة الكلية** للمثلث الكبير بالكامل؟"
            last_en = f"Total triangle area has {m(f'{n_st}^2 = {n_st**2}')} parts: {m(f'{n_st**2} \\times {unit_a} = {ans}')}."
            last_ar = f"مساحة المثلث الكلي تمثّل {m(f'{n_st}^2 = {n_st**2}')} جزءاً: {m(f'{n_st**2} \\times {unit_a} = {ans}')}."
        else:
            t_idx = int(ask)
            odd_t = 2 * t_idx - 1
            ans = unit_a * odd_t
            ask_en = f"what is the area of the **{t_idx}th strip** from the top?"
            ask_ar = f"فما مساحة **الشريط رقم {t_idx}** من الأعلى؟"
            last_en = f"Strip #{m(t_idx)} has weight {m(f'2({t_idx})-1 = {odd_t}')}: {m(f'{odd_t} \\times {unit_a} = {ans}')}."
            last_ar = f"الشريط رقم {m(t_idx)} نسبته {m(odd_t)} أجزاء: {m(f'{odd_t} \\times {unit_a} = {ans}')}."

        distractors = [g_area * n_st, ans + unit_a * 2, max(2, ans - unit_a * 2), unit_a * n_st]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_sim_{v_i}")
        odds_str = " : ".join(str(2 * k - 1) for k in range(1, n_st + 1))
        q_en = (
            f"The left and right sides of a triangle are divided into {m(n_st)} equal parts by lines parallel to the base, "
            f"splitting the triangle into {m(n_st)} horizontal strips from top (strip 1, a small triangle) to bottom (strip {m(n_st)}). "
            f"If strip {m(g_idx)} from the top has area {m(g_area)}, {ask_en}"
        )
        q_ar = (
            f"قُسِّم الضلعان الجانبيان لمثلث إلى {m(n_st)} أجزاء متساوية بمستقيمات موازية للقاعدة، "
            f"مما قسّم المثلث إلى {m(n_st)} أشرطة أفقية مرتبة من الأعلى (الشريط 1) إلى الأسفل (الشريط {m(n_st)}). "
            f"إذا كانت مساحة الشريط رقم {m(g_idx)} من الأعلى تساوي {m(g_area)}، {ask_ar}"
        )
        h_en = f"Similar triangles of scale 1, 2, 3, ..., {n_st} have areas 1², 2², 3², ... — subtract consecutive squares to get strip ratios 1 : 3 : 5 : ...!"
        h_ar = f"المثلثات المتشابهة بنسب أطوال 1، 2، 3، ... مساحاتها 1²، 2²، 3²، ... — اطرح المربعات المتتالية لتجد نسب الأشرطة 1 : 3 : 5 : ...!"
        s_en = explain_en(
            f"The top \\( k \\) strips together form a similar triangle of area proportional to \\( k^2 \\). Subtracting \\( k^2 - (k-1)^2 = 2k - 1 \\) gives strip area ratios **{m(odds_str)}**!",
            [
                f"Strip #{m(g_idx)} corresponds to {m(f'2({g_idx}) - 1 = {odd_g}')} unit parts.",
                f"Since its area is {m(g_area)}, {m(1)} unit part (the tiny top triangle) has area {m(f'{g_area} \\div {odd_g} = {unit_a}')}.",
                last_en,
            ],
            f"Sum of odd ratios \\( 1 + 3 + \\dots + {2*n_st-1} = {n_st}^2 = {n_st**2} \\)!",
        )
        s_ar = explain_ar(
            f"أول \\( k \\) أشرطة من الأعلى تكوّن مثلثاً مشابهاً مساحته تتناسب مع \\( k^2 \\)، وبطرح \\( k^2 - (k-1)^2 = 2k - 1 \\) تكون نسب مساحات الأشرطة **{m(odds_str)}**!",
            [
                f"الشريط رقم {m(g_idx)} يمثّل {m(odd_g)} أجزاء، وبما أن مساحته {m(g_area)} فإن قيمة الجزء الواحد = {m(f'{g_area} \\div {odd_g} = {unit_a}')}.",
                last_ar,
            ],
            f"مجموع الأعداد الفردية الأولى يساوي مربع عددها: \\( {n_st}^2 = {n_st**2} \\)!",
        )
        push(diff, "kmc_g1011_similar_apex_layers", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 7. Midpoint nested squares — perimeter & k-step area (10 Qs)
    # ------------------------------------------------------------------
    mid_cases = [
        (8, 1, "perim", "Easy"),
        (12, 1, "perim", "Easy"),
        (16, 2, "area", "Easy"),
        (16, 3, "area", "Medium"),
        (20, 1, "perim", "Medium"),
        (24, 3, "area", "Medium"),
        (32, 4, "area", "Medium"),
        (14, 1, "perim", "Medium"),
        (32, 5, "area", "Hard"),
        (24, 2, "perim", "Hard"),
    ]
    for v_i, (s, k_steps, ask, diff) in enumerate(mid_cases):
        svg = svg_midpoint_square_shaded(f"{s} cm", shade_inner=True)
        if ask == "area":
            orig_a = s * s
            assert orig_a % (2 ** k_steps) == 0
            ans = orig_a // (2 ** k_steps)
            distractors = [orig_a // (2 ** (k_steps - 1)), orig_a // (4 ** k_steps) if orig_a % (4 ** k_steps) == 0 else ans // 2, ans + 8, max(2, ans - 4)]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_mid_{v_i}")
            q_en = (
                f"Starting with a square of side length {m(s)} cm, a new square is formed by connecting the midpoints of its sides. "
                f"This midpoint process is repeated **{m(k_steps)} times** in total. What is the **area** of the {m(f'{k_steps}\\text{{th}}')} inner square (in \\( \\text{{cm}}^2 \\))?"
            )
            q_ar = (
                f"بدءاً من مربع طول ضلعه {m(s)} سم، نرسم مربعاً جديداً بتوصيل منتصفات أضلاعه، "
                f"ونكرر هذه العملية **{m(k_steps)} مرات** إجمالاً. ما **مساحة** المربع الداخلي الناتج بعد المرة رقم {m(k_steps)} (بـ \\( \\text{{cm}}^2 \\))؟"
            )
            steps_en = [
                f"Original square area: {m(f'{s}^2 = {orig_a}\\text{{ cm}}^2')}.",
                f"Connecting the midpoints of ANY square cuts its area in **half** ({m('\\div 2')}) each time!",
                f"After {m(k_steps)} steps, divide by {m(f'2^{{{k_steps}}} = {2**k_steps}')}: {m(f'\\frac{{{orig_a}}}{{{2**k_steps}}} = {ans}\\text{{ cm}}^2')}.",
            ]
            steps_ar = [
                f"مساحة المربع الأصلي: {m(f'{s}^2 = {orig_a}\\text{{ cm}}^2')}.",
                f"توصيل منتصفات أضلاع أي مربع يقسم مساحته إلى **النصف** ({m('\\div 2')}) في كل خطوة!",
                f"بعد {m(k_steps)} خطوات نقسم على {m(f'2^{{{k_steps}}} = {2**k_steps}')}: {m(f'\\frac{{{orig_a}}}{{{2**k_steps}}} = {ans}\\text{{ cm}}^2')}.",
            ]
        else:
            if k_steps == 1:
                # side = (s/2)*sqrt(2), perimeter = 2*s*sqrt(2)
                c_val = 2 * s
                ans_tex = f"{c_val}\\sqrt{{2}}"
                d_list = [f"{s}\\sqrt{{2}}", f"{4 * s}\\sqrt{{2}}", f"{2 * s}", f"{3 * s}"]
                steps_en = [
                    f"Each corner is an isosceles right triangle with legs {m(f'{s}/2 = {s//2}')} cm.",
                    f"By the Pythagorean theorem, one side of the shaded inner square is {m(f'\\sqrt{{({s//2})^2 + ({s//2})^2}} = {s//2}\\sqrt{{2}}')} cm.",
                    f"Multiply by {m(4)} sides: {m(f'4 \\times {s//2}\\sqrt{{2}} = {ans_tex}')} cm.",
                ]
                steps_ar = [
                    f"كل ركن عبارة عن مثلث قائم متطابق الضلعين طول ساقيه {m(f'{s}/2 = {s//2}')} سم.",
                    f"من فيثاغورس، طول ضلع المربع المظلّل الداخلي {m(f'\\sqrt{{({s//2})^2 + ({s//2})^2}} = {s//2}\\sqrt{{2}}')} سم.",
                    f"نضرب في {m(4)} أضلاع: {m(f'4 \\times {s//2}\\sqrt{{2}} = {ans_tex}')} سم.",
                ]
            else:
                # k_steps == 2: side divides by sqrt(2) twice -> divides by 2! Perimeter = 4 * (s/2) = 2s!
                ans_tex = str(2 * s)
                d_list = [f"{s}\\sqrt{{2}}", f"{2 * s}\\sqrt{{2}}", str(s), str(3 * s)]
                steps_en = [
                    f"Each midpoint step multiplies the side length by {m('\\frac{1}{\\sqrt{2}}')}.",
                    f"After {m(2)} steps, the side length is multiplied by {m(f'\\left(\\frac{{1}}{{\\sqrt{{2}}}}\\right)^2 = \\frac{{1}}{{2}}')}, becoming {m(f'{s}/2 = {s//2}')} cm.",
                    f"Perimeter of the 2nd inner square: {m(f'4 \\times {s//2} = {ans_tex}')} cm.",
                ]
                steps_ar = [
                    f"في كل خطوة منتصفات يُضرب طول الضلع في {m('\\frac{1}{\\sqrt{2}}')}.",
                    f"بعد خطوتين يُضرب طول الضلع في {m('\\frac{1}{2}')} ليصبح {m(f'{s}/2 = {s//2}')} سم.",
                    f"محيط المربع الداخلي الثاني: {m(f'4 \\times {s//2} = {ans_tex}')} سم.",
                ]
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3g_mid_{v_i}")
            q_en = (
                f"Starting with a square of side length {m(s)} cm, a midpoint square is drawn inside it"
                + (" (and a second midpoint square inside that)" if k_steps == 2 else "")
                + f". What is the **perimeter** of that {'2nd ' if k_steps == 2 else ''}inner square (in cm)?"
            )
            q_ar = (
                f"بدءاً من مربع طول ضلعه {m(s)} سم، رُسم مربع داخلي بتوصيل منتصفات أضلاعه"
                + (" (ثم مربع ثانٍ بتوصيل منتصفات أضلاع الداخلي)" if k_steps == 2 else "")
                + f". ما **محيط** ذلك المربع الداخلي (بالسنتيمتر)؟"
            )

        h_en = "Every midpoint-square step scales area by 1/2 and scales side length (and perimeter) by 1/√2!"
        h_ar = "كل خطوة لتوصيل المنتصفات تضرب المساحة في 1/2 وتضرب طول الضلع (والمحيط) في 1/√2!"
        s_en = explain_en("Because area scales as the **square** of the length ratio, area ratio \\( \\frac{1}{2} \\) corresponds to length ratio \\( \\frac{1}{\\sqrt{2}} \\)!", steps_en, "Check: squaring \\( \\frac{1}{\\sqrt{2}} \\) gives \\( \\frac{1}{2} \\) every single step.")
        s_ar = explain_ar("بما أن نسبة المساحة تساوي **مربع** نسبة التشابه، فإن نسبة المساحة \\( \\frac{1}{2} \\) تعني أن نسبة الأطوال والمحيطات هي \\( \\frac{1}{\\sqrt{2}} \\)!", steps_ar, "تحقق: تربيع نسبة الطول \\( \\frac{1}{\\sqrt{2}} \\) يعيد نسبة المساحة \\( \\frac{1}{2} \\).")
        push(diff, "kmc_g1011_midpoint_nested_squares", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 8. Curved shaded region perimeter (quarter-minus-semi & two-semis) (9 Qs)
    # ------------------------------------------------------------------
    cp_cases = [
        (6, "quarter_minus_semi", "Easy"),
        (8, "quarter_minus_semi", "Easy"),
        (10, "two_semis_outside", "Easy"),
        (12, "quarter_minus_semi", "Medium"),
        (14, "two_semis_outside", "Medium"),
        (16, "quarter_minus_semi", "Medium"),
        (18, "two_semis_outside", "Medium"),
        (20, "quarter_minus_semi", "Hard"),
        (24, "two_semis_outside", "Hard"),
    ]
    for v_i, (s, mode, diff) in enumerate(cp_cases):
        svg = svg_square_circle_shaded(f"{s} cm", mode)
        if mode == "quarter_minus_semi":
            # Boundary of shaded region: left vertical side (s) + quarter arc of radius s ((1/4)*2*pi*s = (s/2)*pi) + semi arc of diameter s ((1/2)*pi*s = (s/2)*pi) = s + s*pi!
            ans_tex = f"{s} + {s}\\pi"
            d_list = [f"{2 * s} + {s}\\pi", f"{s} + {s // 2}\\pi", f"{s}\\pi", f"{2 * s} + {s // 2}\\pi"]
            q_en = (
                f"In the square of side {m(s)} cm shown, the shaded region is bounded by the left side of the square, "
                f"a quarter-circle arc of radius {m(s)} cm, and a semicircle arc of diameter {m(s)} cm. "
                f"What is the **perimeter** of the shaded region (in cm)?"
            )
            q_ar = (
                f"في المربع الذي طول ضلعه {m(s)} سم الموضح في الشكل، تُحاط المنطقة المظلّلة بالضلع الأيسر للمربع "
                f"وقوس ربع دائرة نصف قطره {m(s)} سم وقوس نصف دائرة قطره {m(s)} سم. "
                f"ما **محيط** المنطقة المظلّلة (بالسنتيمتر)؟"
            )
            steps_en = [
                f"Trace ALL boundary pieces of the shaded shape: (1) straight left side = {m(s)} cm.",
                f"(2) Quarter-circle arc of radius {m(s)}: {m(f'\\frac{{1}}{{4}}(2\\pi \\times {s}) = {s//2}\\pi')}; (3) Semicircle arc of diameter {m(s)}: {m(f'\\frac{{1}}{{2}}(\\pi \\times {s}) = {s//2}\\pi')}.",
                f"Add all three boundary pieces (do NOT subtract arcs when finding perimeter!): {m(f'{s} + {s//2}\\pi + {s//2}\\pi = {ans_tex}')}.",
            ]
            steps_ar = [
                f"نتتبع حدود المنطقة المظلّلة قطعةً قطعة: (1) الضلع الأيسر المستقيم = {m(s)} سم.",
                f"(2) قوس ربع الدائرة: {m(f'\\frac{{1}}{{4}}(2\\pi \\times {s}) = {s//2}\\pi')}؛ و(3) قوس نصف الدائرة السفلي: {m(f'\\frac{{1}}{{2}}(\\pi \\times {s}) = {s//2}\\pi')}.",
                f"نجمع جميع حدود الشكل المظلّل (في المحيط نجمع الأقواس المحيطة ولا نطرحها!): {m(ans_tex)}.",
            ]
        else:
            # Boundary of shaded region: top side (s) + bottom side (s) + 2 inward semicircle arcs of diameter s (pi*s) = 2s + s*pi
            ans_tex = f"{2 * s} + {s}\\pi"
            d_list = [f"{2 * s} - {s}\\pi", f"{4 * s} - {s}\\pi", f"{2 * s} + {2 * s}\\pi", f"{s} + {s}\\pi"]
            q_en = (
                f"Two inward semicircles of diameter {m(s)} cm are cut out from the left and right sides of a square of side {m(s)} cm, as shown. "
                f"What is the **perimeter** of the remaining purple shaded region (in cm)?"
            )
            q_ar = (
                f"قُطع نصفا دائرة إلى الداخل قطر كلٍّ منهما {m(s)} سم من الضلعين الأيسر والأيمن لمربع طول ضلعه {m(s)} سم كما في الشكل. "
                f"ما **محيط** المنطقة البنفسجية المظلّلة المتبقية (بالسنتيمتر)؟"
            )
            steps_en = [
                f"Walk around the boundary of the shaded region: you traverse the top straight side ({m(s)}) and bottom straight side ({m(s)}), giving {m(2*s)} cm.",
                f"Along the left and right sides, you walk along two semicircular arcs of diameter {m(s)}, whose lengths sum to one full circumference {m(f'\\pi \\times {s} = {s}\\pi')} cm.",
                f"Add straight and curved boundaries: {m(ans_tex)} cm.",
            ]
            steps_ar = [
                f"نسير حول حدود المنطقة المظلّلة: نقطع الضلعين المستقيمين العلوي ({m(s)}) والسفلي ({m(s)}) بمجموع {m(2*s)} سم.",
                f"وعلى الجانبين نسير فوق قوسي نصفي الدائرتين، ومجموع طوليهما يساوي محيط دائرة كاملة قطرها {m(s)} أي {m(f'{s}\\pi')} سم.",
                f"نجمع الحدود المستقيمة والمنحنية: {m(ans_tex)} سم.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3g_cp_{v_i}")
        h_en = "Biggest KMC trap: cutting out a bite DECREASES area, but INCREASES (or adds to) perimeter — always ADD every arc on the boundary!"
        h_ar = "أشهر فخ في مسابقات كاوست: اقتطاع جزء من الشكل يُنقص المساحة لكنه **يُضاف** كقوس في المحيط — اجمع دائماً جميع أطوال الحدود المحيطة!"
        s_en = explain_en("Perimeter is the total length of fence needed to enclose the shaded region — every boundary arc is **added**, never subtracted!", steps_en, "Notice we never see a minus sign in a perimeter sum!")
        s_ar = explain_ar("المحيط هو طول السياج المحيط بالمنطقة المظلّلة بالكامل — لذا **نجمع** أطوال جميع الأقواس الحدودية ولا نطرحها أبداً!", steps_ar, "لاحظ أنه لا توجد إشارة طرح أبداً عند جمع أطوال حدود المحيط!")
        push(diff, "kmc_g1011_circle_square_senior", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 9. Intersecting diagonals in a regular n-gon (9 Qs)
    # ------------------------------------------------------------------
    # Chords (0, k) and (1, m) with 1 < k < m < n intersect inside P!
    # By inscribed-angle / arc-sum rule, the angle facing arcs (0..1) and (k..m) has measure
    # (1 + (m - k)) * (180 / n) degrees! Let's verify on regular pentagon (n=5), chords AC (0,2) and BD (1,3):
    # (1 + (3 - 2)) * (180 / 5) = 2 * 36 = 72°! Check: in △APB, ∠PAB = 36°, ∠PBA = 36° -> exterior ∠APD = 72° and ∠APB = 108°! Exact!
    diag_cases = [
        (5, 2, 3, "acute", "Easy"),       # (1 + 1)*36 = 72°
        (6, 2, 4, "acute", "Easy"),       # (1 + 2)*30 = 90°
        (6, 3, 4, "acute", "Medium"),     # (1 + 1)*30 = 60°
        (8, 3, 5, "acute", "Medium"),     # (1 + 2)*22.5? wait 3*22.5=67.5; pick even (1 + m - k)! For n=8, k=2, m=5 -> (1+3)*22.5 = 90°; k=3, m=4 -> (1+1)*22.5 = 45°!
        (8, 2, 5, "acute", "Medium"),     # 4 * 22.5 = 90°
        (9, 3, 5, "acute", "Medium"),     # (1 + 2)*20 = 60°
        (10, 3, 6, "acute", "Medium"),    # (1 + 3)*18 = 72°
        (12, 3, 7, "acute", "Hard"),      # (1 + 4)*15 = 75°
        (12, 4, 7, "obtuse", "Hard"),     # acute = (1+3)*15 = 60°, obtuse = 120°
    ]
    diag_cases[3] = (8, 3, 4, "acute", "Medium")
    for v_i, (n, k, m_v, kind, diff) in enumerate(diag_cases):
        svg = svg_regular_polygon(n, [(0, k), (1, m_v)])
        arc_cnt = 1 + (m_v - k)
        assert (arc_cnt * 180) % n == 0
        ang1 = (arc_cnt * 180) // n
        ac = min(ang1, 180 - ang1)
        ob = 180 - ac
        ans = ac if kind == "acute" else ob
        distractors = [180 - ans if 180 - ans != ans else ans - 15, ans + 15, max(15, ans - 15), 360 // n]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_diag_{v_i}", suffix="^\\circ")
        d1 = f"A{chr(65 + k)}"
        d2 = f"B{chr(65 + m_v)}"
        kind_en = "**acute** (or right) angle" if ac <= 90 and kind == "acute" else "**obtuse** angle"
        kind_ar = "الزاوية **الحادة** (أو القائمة)" if ac <= 90 and kind == "acute" else "الزاوية **المنفرجة**"
        q_en = (
            f"In a regular {m(n)}-sided polygon with consecutive vertices {m('A, B, C, \\dots')}, "
            f"diagonals {m(d1)} and {m(d2)} intersect at an interior point {m('P')}, as shown. "
            f"What is the measure of the {kind_en} formed at {m('P')}?"
        )
        q_ar = (
            f"في مضلع منتظم ذي {m(n)} أضلاع رؤوسه المتتالية {m('A, B, C, \\dots')}، "
            f"يتقاطع القطران {m(d1)} و{m(d2)} في نقطة داخلية {m('P')} كما في الشكل. "
            f"ما قياس {kind_ar} المتكوّنة عند النقطة {m('P')}؟"
        )
        h_en = f"Every regular {n}-gon is inscribed in a circle where each side is a 360°/{n} arc! An interior chord-intersection angle equals HALF the sum of its two intercepted arcs!"
        h_ar = f"كل مضلع منتظم ذي {n} أضلاع يقع داخل دائرة قوس كل ضلع فيها 360°/{n}! الزاوية بين وترين متقاطعين تساوي نصف مجموع القوسين المقابلين لها!"
        s_en = explain_en(
            f"Circumscribe a circle around the regular {m(n)}-gon: each side subtends a central arc of \\( \\frac{{360^\\circ}}{{{n}}} \\), and two intersecting chords form an angle equal to \\( \\text{{(total sides in the two opposite arcs)}} \\times \\frac{{180^\\circ}}{{{n}}} \\)!",
            [
                f"Between {m('A')} and {m('B')} is {m(1)} side, and between {m(chr(65+k))} and {m(chr(65+m_v))} are {m(f'{m_v} - {k} = {m_v - k}')} sides, totaling {m(arc_cnt)} side-arcs.",
                f"Angle facing those arcs: {m(f'{arc_cnt} \\times \\frac{{180^\\circ}}{{{n}}} = {ang1}^\\circ')}.",
                f"Selecting the requested angle at {m('P')} gives **{m(f'{ans}^\\circ')}**.",
            ],
            f"Equivalently, apply the Exterior Angle Theorem to {m('\\triangle APB')}!",
        )
        s_ar = explain_ar(
            f"نحيط المضلع المنتظم بدائرة: يقابل كل ضلع قوساً قياسه \\( \\frac{{360^\\circ}}{{{n}}} \\)، وتكون الزاوية بين وترين متقاطعين مساوية لـ \\( \\text{{(مجموع أضلاع القوسين المتقابلين)}} \\times \\frac{{180^\\circ}}{{{n}}} \\)!",
            [
                f"بين {m('A')} و{m('B')} ضلع واحد ({m(1)})، وبين {m(chr(65+k))} و{m(chr(65+m_v))} يوجد {m(m_v - k)} أضلاع، بمجموع {m(arc_cnt)} أقواس.",
                f"قياس الزاوية المقابلة لهذين القوسين: {m(f'{arc_cnt} \\times \\frac{{180^\\circ}}{{{n}}} = {ang1}^\\circ')}.",
                f"بأخذ الزاوية المطلوبة عند {m('P')} نحصل على **{m(f'{ans}^\\circ')}**.",
            ],
            f"يمكن الوصول للنتيجة نفسها بحساب زوايا المثلث {m('\\triangle APB')} واستخدام الزاوية الخارجية!",
        )
        push(diff, "kmc_g1011_regular_polygon_diag_intersections", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 10. 3D solid scaling percentage change (9 Qs, SVG!)
    # ------------------------------------------------------------------
    sc3d_cases = [
        (10, 10, 0, "vol", "Easy"),       # +10%, +10%, +0% -> 1.21 -> +21%
        (20, 20, 0, "vol", "Easy"),       # 1.44 -> +44%
        (50, 50, 0, "area", "Easy"),      # all edges +50% -> area (1.5)^2 = 2.25 -> +125%
        (10, 10, 10, "vol", "Medium"),    # +33.1%
        (20, 25, -20, "vol", "Medium"),   # 1.2 * 1.25 * 0.8 = 1.20 -> +20%
        (50, 20, -25, "vol", "Medium"),   # 1.5 * 1.2 * 0.75 = 1.35 -> +35%
        (20, 20, 20, "area", "Medium"),   # all edges +20% -> surface area +44%
        (50, 50, 50, "vol", "Hard"),      # (1.5)^3 = 3.375 -> +237.5%
        (25, 20, -10, "vol", "Hard"),     # 1.25 * 1.2 * 0.9 = 1.35 -> +35%
    ]
    for v_i, (p1, p2, p3, ask, diff) in enumerate(sc3d_cases):
        svg = svg_water_tank_3d(f"L ({'+' if p1>=0 else ''}{p1}%)", f"W ({'+' if p2>=0 else ''}{p2}%)", f"H ({'+' if p3>=0 else ''}{p3}%)", 0.65)
        f1, f2, f3 = Fraction(100 + p1, 100), Fraction(100 + p2, 100), Fraction(100 + p3, 100)
        if ask == "area":
            assert p1 == p2
            mult = f1 * f1
            pct = float((mult - 1) * 100)
            ans = int(pct) if pct.is_integer() else pct
            distractors = [p1 * 2, p1 * 3, ans + 10, p1]
            q_en = f"Every edge of a rectangular tank is increased by {m(f'{p1}\\%')}. By what **percentage** does its **total surface area** increase?"
            q_ar = f"زيد طول كل حرف من أحرف خزان متوازي مستطيلات بنسبة {m(f'{p1}\\%')}. فما **النسبة المئوية للزيادة** في **مساحته السطحية الكلية**؟"
            steps_en = [
                f"Increasing every length by {m(f'{p1}\\%')} multiplies every linear dimension by {m(f'{float(f1):g}')}.",
                f"Area scales by the **square** of the linear multiplier: {m(f'({float(f1):g})^2 = {float(mult):g}')}.",
                f"Convert back to percentage increase: {m(f'({float(mult):g} - 1) \\times 100\\% = {fmt_val(ans)}\\%')}.",
            ]
            steps_ar = [
                f"زيادة كل بُعد بنسبة {m(f'{p1}\\%')} تعني ضرب كل طول في المعامل {m(f'{float(f1):g}')}.",
                f"تتضاعف المساحة السطحية بـ **مربع** معامل الطول: {m(f'({float(f1):g})^2 = {float(mult):g}')}.",
                f"نسبة الزيادة المئوية: {m(f'({float(mult):g} - 1) \\times 100\\% = {fmt_val(ans)}\\%')}.",
            ]
        else:
            mult = f1 * f2 * f3
            pct = round(float((mult - 1) * 100), 2)
            ans = int(pct) if pct.is_integer() else pct
            naive = p1 + p2 + p3
            distractors = [naive if naive != ans else ans + 5, round(ans + 10, 1), round(max(1, ans - 5), 1), round(ans + 4, 1)]
            c3_en = f"unchanged ({m('0\\%')})" if p3 == 0 else (f"increased by {m(f'{p3}\\%')}" if p3 > 0 else f"decreased by {m(f'{abs(p3)}\\%')}")
            c3_ar = f"ثابتاً دون تغيير ({m('0\\%')})" if p3 == 0 else (f"زيد بنسبة {m(f'{p3}\\%')}" if p3 > 0 else f"نُقِص بنسبة {m(f'{abs(p3)}\\%')}")
            q_en = (
                f"In the rectangular water tank shown, the length {m('L')} is increased by {m(f'{p1}\\%')}, "
                f"the width {m('W')} is increased by {m(f'{p2}\\%')}, and the height {m('H')} is {c3_en}. "
                f"By what **percentage** does the tank's **volume** increase?"
            )
            q_ar = (
                f"في الخزان المائي الموضح، زيد الطول {m('L')} بنسبة {m(f'{p1}\\%')}، "
                f"وزيد العرض {m('W')} بنسبة {m(f'{p2}\\%')}، وبقي الارتفاع {m('H')} {c3_ar}. "
                f"فما **النسبة المئوية للزيادة** في **حجم** الخزان؟"
            )
            steps_en = [
                f"Convert each percentage change into a decimal multiplier: {m(f'{float(f1):g}')}, {m(f'{float(f2):g}')}, and {m(f'{float(f3):g}')}.",
                f"Multiply the three multipliers to get the new volume factor: {m(f'{float(f1):g} \\times {float(f2):g} \\times {float(f3):g} = {float(mult):g}')}.",
                f"Subtract {m(1)} and convert to percent: {m(f'({float(mult):g} - 1) \\times 100\\% = {fmt_val(ans)}\\%')}.",
            ]
            steps_ar = [
                f"نحوّل كل تغير مئوي إلى معامل ضرب عشري: {m(f'{float(f1):g}')} و{m(f'{float(f2):g}')} و{m(f'{float(f3):g}')}.",
                f"نضرب المعاملات الثلاثة لإيجاد معامل الحجم الجديد: {m(f'{float(f1):g} \\times {float(f2):g} \\times {float(f3):g} = {float(mult):g}')}.",
                f"نطرح {m(1)} ونضرب في {m('100\\%')}: الزيادة = {m(f'{fmt_val(ans)}\\%')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_sc3d_{v_i}", suffix="\\%")
        h_en = "Never simply add percentages! Turn each +p% into multiplier (1 + p/100) and MULTIPLY the factors!"
        h_ar = "لا تجمع النسب المئوية جمعاً عادياً! حوّل كل تغير +p% إلى معامل ضرب (1 + p/100) ثم اضرب المعاملات!"
        s_en = explain_en("Because \\( V = L \\times W \\times H \\), percentage changes act **multiplicatively** via scale factors!", steps_en, f"Test with \\( L=W=H=10 \\) to verify the exact new volume!")
        s_ar = explain_ar("لأن الحجم \\( V = L \\times W \\times H \\)، فإن التغيرات المئوية تُحسَب **بضرب معاملات التغير** لا بجمع النسب!", steps_ar, f"يمكنك فرض \\( L=W=H=10 \\) للتحقق بالأعداد فوراً!")
        push(diff, "kmc_g1011_solid_scaling_percent", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 11. Overlapping rectangles outer perimeter (9 Qs, SVG!)
    # ------------------------------------------------------------------
    # When two axis-aligned rectangles overlap at a corner (as drawn in svg_overlapping_rects!),
    # the outer union boundary loses BOTH the top/left edges of overlap from rect 2 AND bottom/right edges of overlap from rect 1 = full P_overlap!
    ovp_cases = [
        (10, 8, 9, 7, 3, 4, "Easy"),
        (12, 10, 10, 8, 4, 5, "Easy"),
        (14, 9, 12, 11, 5, 4, "Medium"),
        (15, 12, 13, 10, 6, 5, "Medium"),
        (16, 14, 14, 12, 5, 6, "Medium"),
        (18, 12, 15, 11, 7, 5, "Medium"),
        (20, 15, 16, 14, 8, 6, "Hard"),
        (22, 16, 18, 15, 7, 8, "Hard"),
        (25, 18, 20, 16, 9, 7, "Hard"),
    ]
    for v_i, (w1, h1, w2, h2, wo, ho, diff) in enumerate(ovp_cases):
        p1 = 2 * (w1 + h1)
        p2 = 2 * (w2 + h2)
        po = 2 * (wo + ho)
        ans = p1 + p2 - po
        svg = svg_overlapping_rects(f"{w1}×{h1}", f"{w2}×{h2}", f"{wo}×{ho}")
        distractors = [p1 + p2, p1 + p2 - (wo + ho), p1 + p2 - 2 * po, ans + 4]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t3g_ovp_{v_i}")
        q_en = (
            f"A {m(f'{w1} \\times {h1}')} rectangle and a {m(f'{w2} \\times {h2}')} rectangle overlap at a corner in a {m(f'{wo} \\times {ho}')} shaded rectangle, as shown. "
            f"What is the **outer perimeter** of the combined figure?"
        )
        q_ar = (
            f"يتقاطع مستطيل أبعاده {m(f'{w1} \\times {h1}')} ومستطيل أبعاده {m(f'{w2} \\times {h2}')} عند الركن في مستطيل مظلّل أبعاده {m(f'{wo} \\times {ho}')} كما في الشكل. "
            f"ما **المحيط الخارجي** للشكل المدمج؟"
        )
        h_en = "Every segment of the shaded overlap's boundary lies INSIDE the union shape and disappears from the outer perimeter!"
        h_ar = "الأضلاع الأربعة للمستطيل المظلّل المتقاطع تقع جميعها **داخل** الشكل المدمج فتختفي من المحيط الخارجي!"
        s_en = explain_en(
            "When two rectangles overlap across a corner, the 4 sides of the overlap rectangle are the **exact** segments trapped inside the union! So \\( P_{\\text{outer}} = P_1 + P_2 - P_{\\text{overlap}} \\).",
            [
                f"Individual perimeters: {m(f'P_1 = 2({w1}+{h1}) = {p1}')} and {m(f'P_2 = 2({w2}+{h2}) = {p2}')}.",
                f"Perimeter of the {m(f'{wo} \\times {ho}')} overlap (trapped inside): {m(f'P_{{\\text{{ov}}}} = 2({wo}+{ho}) = {po}')}.",
                f"Subtract: {m(f'{p1} + {p2} - {po} = {ans}')}.",
            ],
            f"Alternative bounding-box check: total width is {m(f'{w1}+{w2}-{wo}={w1+w2-wo}')} and total height is {m(f'{h1}+{h2}-{ho}={h1+h2-ho}')}, perimeter {m(f'2({w1+w2-wo}+{h1+h2-ho}) = {ans}')}!",
        )
        s_ar = explain_ar(
            "عند تقاطع مستطيلين عند الركن، تكون الأضلاع الأربعة لمستطيل التقاطع هي بالضبط القطع المحصورة داخل الشكل! لذا \\( P_{\\text{الخارجي}} = P_1 + P_2 - P_{\\text{التقاطع}} \\).",
            [
                f"محيطا المستطيلين: {m(f'P_1 = 2({w1}+{h1}) = {p1}')} و{m(f'P_2 = 2({w2}+{h2}) = {p2}')}.",
                f"محيط مستطيل التقاطع المحصور بالداخل: {m(f'P_{{\\text{{ov}}}} = 2({wo}+{ho}) = {po}')}.",
                f"نطرح: {m(f'{p1} + {p2} - {po} = {ans}')}.",
            ],
            f"تحقق بديل بالإزاحة: العرض الكلي {m(w1+w2-wo)} والارتفاع الكلي {m(h1+h2-ho)}، وضعف مجموعهما يساوي {m(ans)} بالضبط!",
        )
        push(diff, "kmc_g1011_overlapping_rects_perim", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 12. Lattice polygon exact radical perimeter (9 Qs, SVG!)
    # ------------------------------------------------------------------
    radp_cases = [
        (3, 3, [(0, 1), (1, 0), (3, 2), (2, 3)], ["A", "B", "C", "D"], 2, 6, "Easy"),      # 2*sqrt(2) + 4*sqrt(2) = 6*sqrt(2)
        (4, 4, [(0, 2), (2, 0), (4, 2), (2, 4)], ["A", "B", "C", "D"], 2, 8, "Easy"),      # 4 * 2*sqrt(2) = 8*sqrt(2)
        (3, 3, [(0, 1), (2, 0), (3, 2), (1, 3)], ["A", "B", "C", "D"], 5, 4, "Medium"),    # tilted square of side sqrt(5): 4*sqrt(5)
        (5, 4, [(0, 2), (2, 1), (5, 2), (3, 3)], ["A", "B", "C", "D"], 0, 0, "Medium"),    # wait let's keep pure k*sqrt(d)!
        (4, 4, [(0, 1), (3, 0), (4, 3), (1, 4)], ["A", "B", "C", "D"], 10, 4, "Medium"),   # tilted square of side sqrt(10): 4*sqrt(10)
        (5, 5, [(0, 2), (2, 1), (4, 2), (2, 3)], ["A", "B", "C", "D"], 5, 4, "Medium"),    # rhombus of side sqrt(5): 4*sqrt(5) — let's use (6,4) -> 2*sqrt(5) sides -> 8*sqrt(5)!
        (6, 5, [(0, 2), (4, 0), (6, 4), (2, 5)], ["A", "B", "C", "D"], 0, 0, "Hard"),
        (5, 5, [(0, 2), (3, 0), (5, 3), (2, 5)], ["A", "B", "C", "D"], 13, 4, "Hard"),     # tilted square of side sqrt(13): 4*sqrt(13)
        (6, 6, [(0, 2), (4, 0), (6, 4), (2, 6)], ["A", "B", "C", "D"], 5, 8, "Hard"),      # 4 sides of sqrt(16+4)=2*sqrt(5) -> 8*sqrt(5)!
    ]
    # Replace indices 3, 5, 6 with clean pure-radical polygons!
    radp_cases[3] = (5, 3, [(0, 1), (2, 0), (5, 3), (3, 2)], ["A", "B", "C", "D"], 0, 0, "Medium")  # wait let's use exact integer + k*sqrt(d):
    clean_radp = [
        (3, 3, [(0, 1), (1, 0), (3, 2), (2, 3)], ["A", "B", "C", "D"], "6\\sqrt{2}", ["4\\sqrt{2}", "8\\sqrt{2}", "12", "6"], "Easy",
         "AB = CD = \\sqrt{1^2+1^2} = \\sqrt{2},\\; BC = DA = \\sqrt{2^2+2^2} = 2\\sqrt{2}"),
        (4, 4, [(0, 2), (2, 0), (4, 2), (2, 4)], ["A", "B", "C", "D"], "8\\sqrt{2}", ["4\\sqrt{2}", "16", "6\\sqrt{2}", "8"], "Easy",
         "AB = BC = CD = DA = \\sqrt{2^2+2^2} = 2\\sqrt{2}"),
        (3, 3, [(0, 1), (2, 0), (3, 2), (1, 3)], ["A", "B", "C", "D"], "4\\sqrt{5}", ["2\\sqrt{5}", "8\\sqrt{5}", "20", "12"], "Medium",
         "AB = BC = CD = DA = \\sqrt{2^2+1^2} = \\sqrt{5}"),
        (4, 3, [(0, 0), (4, 0), (3, 2), (1, 2)], ["A", "B", "C", "D"], "6 + 2\\sqrt{5}", ["6 + 4\\sqrt{5}", "8 + 2\\sqrt{5}", "10", "6 + \\sqrt{5}"], "Medium",
         "AB = 4,\\; CD = 2,\\; BC = DA = \\sqrt{1^2+2^2} = \\sqrt{5}"),
        (4, 4, [(0, 1), (3, 0), (4, 3), (1, 4)], ["A", "B", "C", "D"], "4\\sqrt{10}", ["2\\sqrt{10}", "8\\sqrt{10}", "16", "40"], "Medium",
         "AB = BC = CD = DA = \\sqrt{3^2+1^2} = \\sqrt{10}"),
        (5, 3, [(0, 0), (3, 0), (5, 2), (2, 2)], ["A", "B", "C", "D"], "6 + 4\\sqrt{2}", ["6 + 2\\sqrt{2}", "10\\sqrt{2}", "14", "8 + 2\\sqrt{2}"], "Medium",
         "AB = CD = 3,\\; BC = DA = \\sqrt{2^2+2^2} = 2\\sqrt{2}"),
        (5, 4, [(0, 0), (5, 0), (4, 3), (1, 3)], ["A", "B", "C", "D"], "8 + 2\\sqrt{10}", ["8 + \\sqrt{10}", "10 + 2\\sqrt{10}", "16", "8 + 4\\sqrt{10}"], "Hard",
         "AB = 5,\\; CD = 3,\\; BC = DA = \\sqrt{1^2+3^2} = \\sqrt{10}"),
        (5, 5, [(0, 2), (3, 0), (5, 3), (2, 5)], ["A", "B", "C", "D"], "4\\sqrt{13}", ["2\\sqrt{13}", "8\\sqrt{13}", "20", "52"], "Hard",
         "AB = BC = CD = DA = \\sqrt{3^2+2^2} = \\sqrt{13}"),
        (6, 6, [(0, 2), (4, 0), (6, 4), (2, 6)], ["A", "B", "C", "D"], "8\\sqrt{5}", ["4\\sqrt{5}", "16\\sqrt{5}", "24", "4\\sqrt{20} + 4"], "Hard",
         "AB = BC = CD = DA = \\sqrt{4^2+2^2} = \\sqrt{20} = 2\\sqrt{5}"),
    ]
    for v_i, (cols, rows, verts, lbls, ans_tex, d_list, diff, edge_work) in enumerate(clean_radp):
        svg = svg_grid_polygon(cols, rows, verts, lbls)
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t3g_radp_{v_i}")
        v_desc = ", ".join(f"{nm}({vx},{vy})" for nm, (vx, vy) in zip(lbls, verts))
        q_en = (
            f"Quadrilateral {m('ABCD')} with vertices {m(v_desc)} is drawn on a {m(f'{cols} \\times {rows}')} grid of {m('1 \\times 1')} unit squares, as shown. "
            f"What is the exact **perimeter** of {m('ABCD')}?"
        )
        q_ar = (
            f"رُسم الشكل الرباعي {m('ABCD')} الذي رؤوسه {m(v_desc)} على شبكة أبعادها {m(f'{cols} \\times {rows}')} من مربعات الوحدة ({m('1 \\times 1')}) كما في الشكل. "
            f"ما **المحيط** الدقيق للشكل {m('ABCD')}؟"
        )
        h_en = "Find each side using √(Δx² + Δy²) and simplify radicals like √8 = 2√2 or √20 = 2√5 before adding!"
        h_ar = "احسب طول كل ضلع بالقانون √(Δx² + Δy²) وبسّط الجذور مثل √8 = 2√2 أو √20 = 2√5 قبل الجمع!"
        s_en = explain_en(
            "Count the horizontal run \\( \\Delta x \\) and vertical rise \\( \\Delta y \\) of each side on the grid and apply \\( \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} \\).",
            [
                f"Side lengths from the grid: {m(edge_work)}.",
                f"Add all four side lengths in simplest radical form to obtain {m(ans_tex)}.",
            ],
            "Always factor out perfect squares inside a square root (e.g. \\( \\sqrt{8} = 2\\sqrt{2} \\), \\( \\sqrt{20} = 2\\sqrt{5} \\)) so like radicals combine!",
        )
        s_ar = explain_ar(
            "نعدّ التغير الأفقي \\( \\Delta x \\) والرأسي \\( \\Delta y \\) لكل ضلع على الشبكة ونطبّق قانون فيثاغورس \\( \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} \\).",
            [
                f"أطوال الأضلاع الأربعة: {m(edge_work)}.",
                f"بجمع أطوال الأضلاع الأربعة في أبسط صورة جذرية نحصل على {m(ans_tex)}.",
            ],
            "تذكّر إخراج المربعات الكاملة من تحت الجذر (مثل \\( \\sqrt{8} = 2\\sqrt{2} \\) و\\( \\sqrt{20} = 2\\sqrt{5} \\)) لجمع الجذور المتشابهة!",
        )
        push(diff, "kmc_g1011_grid_radical_perim", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    assert len(out) == 115, f"Expected 115, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 3 Geometry questions (all with KMC SVGs!) cleanly.")
