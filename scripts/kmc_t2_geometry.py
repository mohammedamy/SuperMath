"""Track 2 (Grades 8-9) — Geometry (115 authentic KMC problems, 100% with SVGs)."""
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
    svg_grid_polygon,
    svg_inscribed_corner_triangle_in_rect,
    svg_overlapping_rects,
    svg_painted_cube_3d,
    svg_parallel_zigzag,
    svg_regular_polygon,
    svg_square_circle_shaded,
    svg_square_equilateral,
    svg_subdivided_rect_2x2,
)

LEVEL = "Track 2: Grades 8-9"
TOPIC = "Geometry"


def generate() -> list[dict]:
    out: list[dict] = []
    idx = 1

    def push(diff, bp, q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg_en, svg_ar=None):
        nonlocal idx
        qid = f"KMC-T2-GEO-{idx:03d}"
        idx += 1
        out.append(
            make_kmc_question(
                qid, LEVEL, TOPIC, diff, bp,
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                h_en, h_ar, s_en, s_ar, svg_en, svg_ar,
            )
        )

    # ------------------------------------------------------------------
    # 1. Subdivided 2x2 rectangle perimeters (10 Qs)
    # ------------------------------------------------------------------
    p22_cases = [
        (4, 6, 3, 5, "br", "Easy"),
        (5, 7, 4, 6, "br", "Easy"),
        (6, 9, 3, 7, "bl", "Easy"),
        (4, 8, 5, 9, "tr", "Medium"),
        (7, 5, 6, 8, "tl", "Medium"),
        (8, 11, 4, 9, "br", "Medium"),
        (9, 6, 7, 10, "bl", "Medium"),
        (5, 12, 6, 8, "tr", "Medium"),
        (10, 7, 5, 11, "tl", "Hard"),
        (11, 8, 9, 13, "br", "Hard"),
    ]
    for v_i, (w1, w2, h1, h2, miss, diff) in enumerate(p22_cases):
        vals = {
            "tl": 2 * (w1 + h1),
            "tr": 2 * (w2 + h1),
            "bl": 2 * (w1 + h2),
            "br": 2 * (w2 + h2),
        }
        assert vals["tl"] + vals["br"] == vals["tr"] + vals["bl"]
        ans = vals[miss]
        lbls = {k: (f"P = ?" if k == miss else f"P = {v}") for k, v in vals.items()}
        svg = svg_subdivided_rect_2x2(lbls["tl"], lbls["tr"], lbls["bl"], lbls["br"])
        known = [v for k, v in vals.items() if k != miss]
        distractors = [ans + 2, ans - 2, ans + 4, sum(known) // 3, abs(known[0] + known[1] - known[2]) + 6]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_p22_{v_i}")
        if miss in ("tl", "br"):
            opp = "br" if miss == "tl" else "tl"
            eq_en = f"P_{{\\text{{TL}}}} + P_{{\\text{{BR}}}} = P_{{\\text{{TR}}}} + P_{{\\text{{BL}}}} \\implies ? + {vals[opp]} = {vals['tr']} + {vals['bl']} = {vals['tr']+vals['bl']}"
            sub_en = f"? = {vals['tr']+vals['bl']} - {vals[opp]} = {ans}"
        else:
            opp = "bl" if miss == "tr" else "tr"
            eq_en = f"P_{{\\text{{TR}}}} + P_{{\\text{{BL}}}} = P_{{\\text{{TL}}}} + P_{{\\text{{BR}}}} \\implies ? + {vals[opp]} = {vals['tl']} + {vals['br']} = {vals['tl']+vals['br']}"
            sub_en = f"? = {vals['tl']+vals['br']} - {vals[opp]} = {ans}"

        q_en = (
            f"A large rectangle is divided into four smaller rectangles by two lines parallel to its sides, as shown. "
            f"Three of the smaller rectangles have perimeters {m(known[0])}, {m(known[1])}, and {m(known[2])}. "
            f"What is the perimeter of the fourth (shaded) rectangle?"
        )
        q_ar = (
            f"قُسِّم مستطيل كبير إلى أربعة مستطيلات أصغر بواسطة مستقيمين موازيين لأضلاعه كما في الشكل. "
            f"محيطات ثلاثة من هذه المستطيلات هي {m(known[0])} و{m(known[1])} و{m(known[2])}. "
            f"ما محيط المستطيل الرابع (المظلّل)؟"
        )
        h_en = "Compare the sum of perimeters of two opposite corner rectangles! Both pairs use every width and height piece twice."
        h_ar = "قارن مجموع محيطي مستطيلين متقابلين قطرياً! فكلا الزوجين يجمع كل عرض وكل ارتفاع مرتين بالضبط."
        s_en = explain_en(
            "When a rectangle is split into a 2×2 grid of widths \\( w_1, w_2 \\) and heights \\( h_1, h_2 \\), opposite corners have the **same perimeter sum**: \\( P_{\\text{TL}} + P_{\\text{BR}} = 2(w_1+w_2+h_1+h_2) = P_{\\text{TR}} + P_{\\text{BL}} \\).",
            [
                f"Write the opposite-corner perimeter balance: {m(eq_en)}.",
                f"Subtract to isolate the missing perimeter: {m(sub_en)}.",
            ],
            f"Check: \\( {vals['tl']} + {vals['br']} = {vals['tl']+vals['br']} \\) and \\( {vals['tr']} + {vals['bl']} = {vals['tr']+vals['bl']} \\). They match!",
        )
        s_ar = explain_ar(
            "عند تقسيم مستطيل إلى شبكة 2×2 بعرضين \\( w_1, w_2 \\) وارتفاعين \\( h_1, h_2 \\)، يكون **مجموع محيطي كل ركنين متقابلين متساوياً**: \\( P_{\\text{TL}} + P_{\\text{BR}} = P_{\\text{TR}} + P_{\\text{BL}} \\).",
            [
                f"نكتب معادلة تساوي مجموع المحيطات المتقابلة: {m(eq_en)}.",
                f"نطرح لإيجاد المحيط المجهول: {m(sub_en)}.",
            ],
            f"تحقق: \\( {vals['tl']} + {vals['br']} = {vals['tl']+vals['br']} \\) وكذلك \\( {vals['tr']} + {vals['bl']} = {vals['tr']+vals['bl']} \\).",
        )
        push(diff, "kmc_g89_rect_2x2_perim", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 2. Subdivided 2x2 rectangle areas (10 Qs)
    # ------------------------------------------------------------------
    a22_cases = [
        (3, 5, 2, 4, "br", "Easy"),
        (4, 6, 3, 5, "br", "Easy"),
        (2, 7, 3, 6, "bl", "Easy"),
        (5, 8, 3, 6, "tr", "Medium"),
        (6, 9, 4, 6, "tl", "Medium"),
        (4, 10, 5, 7, "br", "Medium"),
        (6, 8, 5, 9, "bl", "Medium"),
        (7, 9, 4, 8, "tr", "Medium"),
        (8, 12, 5, 9, "tl", "Hard"),
        (9, 15, 6, 10, "br", "Hard"),
    ]
    for v_i, (w1, w2, h1, h2, miss, diff) in enumerate(a22_cases):
        vals = {
            "tl": w1 * h1,
            "tr": w2 * h1,
            "bl": w1 * h2,
            "br": w2 * h2,
        }
        assert vals["tl"] * vals["br"] == vals["tr"] * vals["bl"]
        ans = vals[miss]
        lbls = {k: ("?" if k == miss else str(v)) for k, v in vals.items()}
        svg = svg_subdivided_rect_2x2(lbls["tl"], lbls["tr"], lbls["bl"], lbls["br"])
        known = [v for k, v in vals.items() if k != miss]
        distractors = [ans + w2, max(1, ans - w1), vals["tl"] + vals["br"] - vals["tr"] if miss != "br" else vals["tr"] + vals["bl"] - vals["tl"], ans + 6, ans + 4]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_a22_{v_i}")
        if miss in ("tl", "br"):
            opp = "br" if miss == "tl" else "tl"
            prod_other = vals["tr"] * vals["bl"]
            step1 = f"A_{{\\text{{TL}}}} \\times A_{{\\text{{BR}}}} = A_{{\\text{{TR}}}} \\times A_{{\\text{{BL}}}} \\implies ? \\times {vals[opp]} = {vals['tr']} \\times {vals['bl']} = {prod_other}"
            step2 = f"? = \\frac{{{prod_other}}}{{{vals[opp]}}} = {ans}"
        else:
            opp = "bl" if miss == "tr" else "tr"
            prod_other = vals["tl"] * vals["br"]
            step1 = f"A_{{\\text{{TR}}}} \\times A_{{\\text{{BL}}}} = A_{{\\text{{TL}}}} \\times A_{{\\text{{BR}}}} \\implies ? \\times {vals[opp]} = {vals['tl']} \\times {vals['br']} = {prod_other}"
            step2 = f"? = \\frac{{{prod_other}}}{{{vals[opp]}}} = {ans}"

        q_en = (
            f"A rectangle is partitioned into four smaller rectangles by two perpendicular segments, as shown. "
            f"The areas of three of the smaller rectangles are {m(known[0])}, {m(known[1])}, and {m(known[2])}. "
            f"What is the area of the shaded fourth rectangle?"
        )
        q_ar = (
            f"قُسِّم مستطيل إلى أربعة مستطيلات أصغر بقطعتين متعامدتين كما في الشكل. "
            f"مساحات ثلاثة من المستطيلات الصغيرة هي {m(known[0])} و{m(known[1])} و{m(known[2])}. "
            f"ما مساحة المستطيل الرابع المظلّل؟"
        )
        h_en = "For areas in a 2×2 grid, multiply opposite corners: (Top-Left) × (Bottom-Right) = (Top-Right) × (Bottom-Left)!"
        h_ar = "في مساحات شبكة 2×2، حاصل ضرب مساحتي كل ركنين متقابلين متساوٍ: (أعلى يسار × أسفل يمين) = (أعلى يمين × أسفل يسار)!"
        s_en = explain_en(
            "Because \\( (w_1 h_1)(w_2 h_2) = w_1 w_2 h_1 h_2 = (w_2 h_1)(w_1 h_2) \\), the **product of opposite corner areas** is always equal!",
            [
                f"Set the products of opposite areas equal: {m(step1)}.",
                f"Divide cleanly to find the missing area: {m(step2)}.",
            ],
            f"Notice the top-to-bottom area ratio is \\( {vals['tl']}:{vals['bl']} \\) on the left and \\( {vals['tr']}:{vals['br']} \\) on the right — identical!",
        )
        s_ar = explain_ar(
            "بما أن \\( (w_1 h_1)(w_2 h_2) = (w_2 h_1)(w_1 h_2) \\)، فإن **حاصل ضرب مساحتي كل ركنين متقابلين** يكون متساوياً دائماً!",
            [
                f"نساوي حاصلي ضرب المساحات المتقابلة: {m(step1)}.",
                f"نقسم لإيجاد المساحة المطلوبة: {m(step2)}.",
            ],
            f"لاحظ أن نسبة المساحة العلوية إلى السفلية هي \\( {vals['tl']}:{vals['bl']} \\) يساراً و\\( {vals['tr']}:{vals['br']} \\) يميناً — متطابقتان تماماً!",
        )
        push(diff, "kmc_g89_rect_2x2_area", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 3. Square + circular/semicircular shaded regions (10 Qs)
    # ------------------------------------------------------------------
    sc_cases = [
        (4, "inscribed_outside", "Easy"),
        (6, "inscribed_outside", "Easy"),
        (8, "quarter_minus_semi", "Medium"),
        (10, "two_semis_outside", "Medium"),
        (12, "quarter_minus_semi", "Medium"),
        (12, "inscribed_outside", "Medium"),
        (14, "two_semis_outside", "Medium"),
        (16, "quarter_minus_semi", "Hard"),
        (18, "inscribed_outside", "Hard"),
        (20, "quarter_minus_semi", "Hard"),
    ]
    for v_i, (s, mode, diff) in enumerate(sc_cases):
        svg = svg_square_circle_shaded(f"{s} cm", mode)
        r = s // 2
        if mode in ("inscribed_outside", "two_semis_outside"):
            sq_a = s * s
            pi_c = r * r
            ans_tex = f"{sq_a} - {pi_c}\\pi"
            d_list = [
                f"{sq_a} - {s * s}\\pi",
                f"{sq_a} - {2 * pi_c}\\pi",
                f"{sq_a} - {r}\\pi",
                f"{sq_a // 2} - {pi_c}\\pi",
            ]
            desc_en = (
                f"a circle is inscribed tangent to all four sides of a square of side length {m(s)} cm"
                if mode == "inscribed_outside"
                else f"two inward semicircles of diameter {m(s)} cm are drawn on two opposite sides of a square of side length {m(s)} cm"
            )
            desc_ar = (
                f"رُسمت دائرة داخلية تمس الأضلاع الأربعة لمربع طول ضلعه {m(s)} سم"
                if mode == "inscribed_outside"
                else f"رُسم نصفا دائرة إلى الداخل قطراهما ضلعان متقابلان في مربع طول ضلعه {m(s)} سم"
            )
            why_en = (
                f"The circle has diameter {m(s)} cm, so its radius is {m(f'r = {r}')} cm and its area is {m(f'\\pi r^2 = {pi_c}\\pi')}."
                if mode == "inscribed_outside"
                else f"Two semicircles of radius {m(f'r = {r}')} cm combine to equal one full circle of area {m(f'\\pi r^2 = {pi_c}\\pi')}."
            )
            why_ar = (
                f"قطر الدائرة يساوي {m(s)} سم، إذن نصف قطرها {m(f'r = {r}')} سم ومساحتها {m(f'\\pi r^2 = {pi_c}\\pi')}."
                if mode == "inscribed_outside"
                else f"نصفا الدائرة اللذان نصف قطر كلٍّ منهما {m(f'r = {r}')} سم يكوّنان معاً دائرة كاملة مساحتها {m(f'\\pi r^2 = {pi_c}\\pi')}."
            )
            steps_en = [
                f"Area of the square: {m(f'{s}^2 = {sq_a}\\text{{ cm}}^2')}.",
                why_en,
                f"Subtract the unshaded circular area from the square: {m(ans_tex)}.",
            ]
            steps_ar = [
                f"مساحة المربع: {m(f'{s}^2 = {sq_a}\\text{{ cm}}^2')}.",
                why_ar,
                f"نطرح المساحة الدائرية غير المظللة من مساحة المربع: {m(ans_tex)}.",
            ]
        else:
            # quarter_minus_semi: (1/4) pi s^2 - (1/2) pi (s/2)^2 = (1/8) pi s^2
            assert (s * s) % 8 == 0
            q_coeff = (s * s) // 4
            sm_coeff = (r * r) // 2
            ans_c = (s * s) // 8
            ans_tex = f"{ans_c}\\pi"
            d_list = [f"{q_coeff}\\pi", f"{ans_c * 2}\\pi", f"{ans_c + 4}\\pi", f"{max(1, ans_c - 2)}\\pi"]
            desc_en = (
                f"a quarter-circle of radius {m(s)} cm is centered at the bottom-left corner of a square of side {m(s)} cm, "
                f"and an unshaded semicircle of diameter {m(s)} cm is drawn on the bottom side"
            )
            desc_ar = (
                f"رُسم ربع دائرة نصف قطره {m(s)} سم مركزه الركن السفلي الأيسر لمربع طول ضلعه {m(s)} سم، "
                f"ورُسم نصف دائرة غير مظلل قطره الضلع السفلي ({m(s)} سم)"
            )
            steps_en = [
                f"Area of the large quarter-circle (radius {m(s)}): {m(f'\\frac{{1}}{{4}}\\pi ({s})^2 = {q_coeff}\\pi')}.",
                f"The bottom semicircle has diameter {m(s)}, so its radius is {m(r)}, giving area {m(f'\\frac{{1}}{{2}}\\pi ({r})^2 = {sm_coeff}\\pi')}.",
                f"Subtract the white semicircle from the quarter-circle: {m(f'{q_coeff}\\pi - {sm_coeff}\\pi = {ans_tex}')}.",
            ]
            steps_ar = [
                f"مساحة ربع الدائرة الكبير (نصف قطره {m(s)}): {m(f'\\frac{{1}}{{4}}\\pi ({s})^2 = {q_coeff}\\pi')}.",
                f"نصف الدائرة السفلي قطره {m(s)} أي نصف قطره {m(r)}، فمساحته {m(f'\\frac{{1}}{{2}}\\pi ({r})^2 = {sm_coeff}\\pi')}.",
                f"نطرح مساحة نصف الدائرة الأبيض من ربع الدائرة: {m(f'{q_coeff}\\pi - {sm_coeff}\\pi = {ans_tex}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t2g_sc_{v_i}")
        q_en = f"In the figure shown, {desc_en}. What is the area of the shaded region (in \\( \\text{{cm}}^2 \\))?"
        q_ar = f"في الشكل الموضح، {desc_ar}. ما مساحة المنطقة المظللة (بالسنتيمتر المربع \\( \\text{{cm}}^2 \\))؟"
        h_en = "Break the figure into familiar shapes (square, circle, quarter-circle, semicircle) and subtract the white parts from the outer region."
        h_ar = "جزّئ الشكل إلى أشكال مألوفة (مربع، دائرة، ربع دائرة، نصف دائرة) واطرح الأجزاء البيضاء من المنطقة الأكبر."
        s_en = explain_en("Find the area of the larger enclosing shape first, then subtract the unshaded circular pieces.", steps_en, f"Using \\( \\pi \\approx 3.14 \\), the result {m(ans_tex)} is positive and smaller than the square's area.")
        s_ar = explain_ar("نحسب مساحة الشكل الخارجي أولاً ثم نطرح الأجزاء الدائرية البيضاء غير المظللة.", steps_ar, f"بالتعويض التقريبي \\( \\pi \\approx 3.14 \\) نتحقق أن الناتج {m(ans_tex)} موجب وأصغر من مساحة المربع.")
        push(diff, "kmc_g89_square_circle_shaded", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 4. Running track / stadium perimeter & area (10 Qs)
    # ------------------------------------------------------------------
    stad_cases = [
        (50, 20, "perim", "Easy"),
        (60, 30, "perim", "Easy"),
        (40, 14, "perim", "Easy"),
        (80, 40, "perim", "Medium"),
        (100, 50, "perim", "Medium"),
        (20, 10, "area", "Medium"),
        (30, 12, "area", "Medium"),
        (40, 16, "area", "Medium"),
        (50, 20, "area", "Hard"),
        (60, 24, "area", "Hard"),
    ]
    for v_i, (L, D, ask, diff) in enumerate(stad_cases):
        svg = svg_square_circle_shaded(f"{L} m", "stadium")
        r = D // 2
        if ask == "perim":
            ans_tex = f"{2 * L} + {D}\\pi"
            d_list = [
                f"{2 * L + 2 * D} + {D}\\pi",
                f"{2 * L} + {2 * D}\\pi",
                f"{L} + {D}\\pi",
                f"{2 * L} + {r * r}\\pi",
            ]
            q_en = (
                f"A school running track consists of a central {m(L)} m by {m(D)} m rectangle with two semicircles of diameter {m(D)} m "
                f"attached to its two ends (shown dashed). What is the **outer perimeter** of the track (in meters)?"
            )
            q_ar = (
                f"يتكون مضمار جري مدرسي من مستطيل أوسط أبعاده {m(L)} م × {m(D)} م مع نصفي دائرتين قطر كلٍّ منهما {m(D)} م "
                f"متصلين بطرفيه (الموضحين بخط متقطع). ما **المحيط الخارجي** للمضمار (بالأمتار)؟"
            )
            h_en = "Do NOT include the two dashed interior segments! The outer boundary is 2 straight sides + 2 curved semicircular arcs."
            h_ar = "لا تحسب القطعتين المتقطعتين الداخليتين! المحيط الخارجي يتكون من ضلعين مستقيمين + قوسي نصفي الدائرتين."
            s_en = explain_en(
                "Two semicircular arcs of diameter \\( D \\) combine into one full circle of circumference \\( \\pi D \\), while the dashed interior segments are inside the shape, not on its boundary.",
                [
                    f"Sum of the two straight outer sides: {m(f'2 \\times {L} = {2*L}')} m.",
                    f"Combined length of the two semicircular ends (one full circle of diameter {m(D)}): {m(f'\\pi \\times {D} = {D}\\pi')} m.",
                    f"Total outer perimeter: {m(ans_tex)} m.",
                ],
                f"Common KMC trap avoided: we did NOT add the two interior dashed segments of length {m(D)} m!",
            )
            s_ar = explain_ar(
                "قوسا نصفي الدائرتين اللذان قطراهما \\( D \\) يكوّنان معاً محيط دائرة كاملة \\( \\pi D \\)، بينما الخطان المتقطعان يقعان داخل الشكل فلا يدخلان في المحيط.",
                [
                    f"مجموع الضلعين المستقيمين الخارجيين: {m(f'2 \\times {L} = {2*L}')} م.",
                    f"مجموع قوسي نصفي الدائرتين (محيط دائرة كاملة قطرها {m(D)}): {m(f'\\pi \\times {D} = {D}\\pi')} م.",
                    f"المحيط الخارجي الكلي: {m(ans_tex)} م.",
                ],
                f"تجنبنا الفخ الشهير: لم نُضف الضلعين المتقطعين الداخليين اللذين طول كل منهما {m(D)} م!",
            )
        else:
            rect_a = L * D
            circ_c = r * r
            ans_tex = f"{rect_a} + {circ_c}\\pi"
            d_list = [
                f"{rect_a} + {D * D}\\pi",
                f"{rect_a} + {2 * circ_c}\\pi",
                f"{rect_a} + {D}\\pi",
                f"{2 * L + 2 * D} + {circ_c}\\pi",
            ]
            q_en = (
                f"A stadium field is formed by a {m(L)} m by {m(D)} m rectangle together with two outer semicircles of diameter {m(D)} m "
                f"on its left and right ends, as shown. What is the **total area** of the stadium field (in \\( \\text{{m}}^2 \\))?"
            )
            q_ar = (
                f"يتكون ملعب من مستطيل أبعاده {m(L)} م × {m(D)} م مع نصفي دائرتين خارجيتين قطر كلٍّ منهما {m(D)} م "
                f"على طرفيه الأيمن والأيسر كما في الشكل. ما **المساحة الكلية** للملعب (بالمتر المربع \\( \\text{{m}}^2 \\))؟"
            )
            h_en = "Glue the two semicircles together into one complete circle of radius D/2, then add the rectangle's area!"
            h_ar = "ادمج نصفي الدائرتين معاً لتكوين دائرة كاملة نصف قطرها D/2، ثم أضف مساحة المستطيل!"
            s_en = explain_en(
                "Total area = (Area of central rectangle) + (Area of one full circle of radius \\( r = D/2 \\)).",
                [
                    f"Area of the central rectangle: {m(f'{L} \\times {D} = {rect_a}\\text{{ m}}^2')}.",
                    f"Radius of each semicircle: {m(f'r = {D} \\div 2 = {r}')} m, so the two semicircles together have area {m(f'\\pi r^2 = \\pi({r})^2 = {circ_c}\\pi\\text{{ m}}^2')}.",
                    f"Add both parts: {m(ans_tex)}.",
                ],
                f"Remember to halve the diameter {m(D)} to get radius {m(r)} before squaring!",
            )
            s_ar = explain_ar(
                "المساحة الكلية = (مساحة المستطيل الأوسط) + (مساحة دائرة كاملة نصف قطرها \\( r = D/2 \\)).",
                [
                    f"مساحة المستطيل الأوسط: {m(f'{L} \\times {D} = {rect_a}\\text{{ m}}^2')}.",
                    f"نصف قطر كل نصف دائرة: {m(f'r = {D} \\div 2 = {r}')} م، فتكون مساحة نصفي الدائرتين معاً {m(f'\\pi r^2 = {circ_c}\\pi\\text{{ m}}^2')}.",
                    f"نجمع الجزأين: {m(ans_tex)}.",
                ],
                f"انتبه لقسمة القطر {m(D)} على 2 للحصول على نصف القطر {m(r)} قبل التربيع!",
            )
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, d_list, f"t2g_stad_{v_i}")
        push(diff, "kmc_g89_stadium_track", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 5. Regular polygon chord & interior angles (10 Qs)
    # ------------------------------------------------------------------
    # In a regular n-gon A_0 A_1 ... A_{n-1}, angle A_j A_0 A_k (for 1 <= j < k <= n-1)
    # equals (k - j) * (180 / n) degrees! Let's verify: for n=5, j=2, k=3 -> (1)*36 = 36°!
    poly_cases = [
        (5, "regular pentagon", "خماسي منتظم", 1, 2, "BAC", "Easy"),       # ∠BAC in ABCDE: j=1(B), k=2(C) -> 36°
        (5, "regular pentagon", "خماسي منتظم", 2, 3, "CAD", "Easy"),       # ∠CAD in ABCDE: 36°
        (6, "regular hexagon", "سداسي منتظم", 1, 3, "BAD", "Easy"),        # ∠BAD in ABCDEF: (3-1)*30 = 60°
        (6, "regular hexagon", "سداسي منتظم", 2, 4, "CAE", "Medium"),      # ∠CAE in ABCDEF: (4-2)*30 = 60°
        (8, "regular octagon", "ثماني منتظم", 2, 4, "CAE", "Medium"),      # ∠CAE: 2 * 22.5 = 45°
        (8, "regular octagon", "ثماني منتظم", 1, 5, "BAF", "Medium"),      # ∠BAF: 4 * 22.5 = 90°
        (9, "regular nonagon (9-gon)", "تساعي منتظم", 2, 5, "CAF", "Medium"),  # 3 * 20 = 60°
        (10, "regular decagon (10-gon)", "عشاري منتظم", 2, 5, "CAF", "Hard"),  # 3 * 18 = 54°
        (12, "regular dodecagon (12-gon)", "ثاني عشري منتظم (12 ضلعاً)", 2, 5, "CAF", "Hard"),  # 3 * 15 = 45°
        (12, "regular dodecagon (12-gon)", "ثاني عشري منتظم (12 ضلعاً)", 3, 7, "DAH", "Hard"),  # 4 * 15 = 60°
    ]
    for v_i, (n, name_en, name_ar, j, k, ang_lbl, diff) in enumerate(poly_cases):
        assert ((k - j) * 180) % n == 0
        ans = ((k - j) * 180) // n
        chords = []
        if j > 1:
            chords.append((0, j))
        if k < n - 1:
            chords.append((0, k))
        svg = svg_regular_polygon(n, chords)
        int_ang = ((n - 2) * 180) // n
        unit_ang = Fraction(180, n)
        distractors = [ans + 15, max(10, ans - 12), int_ang // 2, ans + 18, 180 - int_ang]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_rpoly_{v_i}", suffix="^\\circ")
        verts_str = "".join(chr(65 + i) for i in range(min(n, 8))) + ("..." if n > 8 else "")
        q_en = (
            f"In the {name_en} {m(verts_str)} shown, diagonals are drawn from vertex {m('A')}. "
            f"What is the measure of {m(f'\\angle {ang_lbl}')}?"
        )
        q_ar = (
            f"في الـ{name_ar} {m(verts_str)} الموضح في الشكل، رُسمت أقطار من الرأس {m('A')}. "
            f"ما قياس الزاوية {m(f'\\angle {ang_lbl}')}؟"
        )
        h_en = f"From vertex A, the {n - 3} diagonals divide the interior angle at A into {n - 2} equal slices!"
        h_ar = f"الأقطار المرسومة من الرأس A تقسم الزاوية الداخلية عند A إلى {n - 2} زوايا متساوية تماماً!"
        s_en = explain_en(
            f"In a regular \\( n \\)-gon, drawing all diagonals from one vertex splits its interior angle \\( \\frac{{(n-2)\\times 180^\\circ}}{{n}} \\) into \\( n - 2 \\) **equal** angles of \\( \\frac{{180^\\circ}}{{n}} \\) each (one for each side opposite \\( A \\)).",
            [
                f"Each single-side slice from {m('A')} measures {m(f'\\frac{{180^\\circ}}{{{n}}} = {fmt_val(unit_ang)}^\\circ')}.",
                f"Between ray {m(f'A{chr(65+j)}')} and ray {m(f'A{chr(65+k)}')}, there are {m(f'{k} - {j} = {k-j}')} consecutive side slices.",
                f"Multiply: {m(f'\\angle {ang_lbl} = {k-j} \\times {fmt_val(unit_ang)}^\\circ = {ans}^\\circ')}.",
            ],
            f"All {m(n - 2)} slices at {m('A')} sum to {m(f'{n-2} \\times {fmt_val(unit_ang)}^\\circ = {int_ang}^\\circ')}, the exact interior angle of a {name_en}!",
        )
        s_ar = explain_ar(
            f"في المضلع المنتظم ذي \\( n \\) أضلاع، تقسم جميع الأقطار الخارجة من رأس واحد الزاوية الداخلية \\( \\frac{{(n-2)\\times 180^\\circ}}{{n}} \\) إلى \\( n - 2 \\) زوايا **متساوية** قياس كل منها \\( \\frac{{180^\\circ}}{{n}} \\).",
            [
                f"قياس الزاوية المقابلة لضلع واحد من الرأس {m('A')} هو {m(f'\\frac{{180^\\circ}}{{{n}}} = {fmt_val(unit_ang)}^\\circ')}.",
                f"بين الشعاعين {m(f'A{chr(65+j)}')} و{m(f'A{chr(65+k)}')} يوجد {m(f'{k} - {j} = {k-j}')} أضلاع متتالية.",
                f"نضرب: {m(f'\\angle {ang_lbl} = {k-j} \\times {fmt_val(unit_ang)}^\\circ = {ans}^\\circ')}.",
            ],
            f"مجموع الزوايا الجزئية الـ {m(n - 2)} عند الرأس {m('A')} يساوي {m(f'{int_ang}^\\circ')}، وهي الزاوية الداخلية الصحيحة تماماً!",
        )
        push(diff, "kmc_g89_regular_polygon_chords", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 6. Square ABCD + Equilateral triangle ABE angle chasing (10 Qs)
    # ------------------------------------------------------------------
    sq_eq_cases = [
        (True, "\\angle DAE", 30, "Easy",
         "\\angle DAB = 90^\\circ \\text{ and } \\angle BAE = 60^\\circ",
         "\\angle DAE = 90^\\circ - 60^\\circ = 30^\\circ"),
        (True, "\\angle ADE", 75, "Easy",
         "AD = AB = AE \\implies \\triangle ADE \\text{ is isosceles with apex } \\angle DAE = 30^\\circ",
         "\\angle ADE = \\frac{180^\\circ - 30^\\circ}{2} = 75^\\circ"),
        (True, "\\angle EDC", 15, "Medium",
         "\\angle ADE = 75^\\circ \\text{ inside } \\angle ADC = 90^\\circ",
         "\\angle EDC = 90^\\circ - 75^\\circ = 15^\\circ"),
        (True, "\\angle DEC", 150, "Medium",
         "\\triangle DEC \\text{ is isosceles with } \\angle EDC = \\angle ECD = 15^\\circ",
         "\\angle DEC = 180^\\circ - 15^\\circ - 15^\\circ = 150^\\circ"),
        (True, "\\angle DEB", 135, "Hard",
         "\\angle AED = 75^\\circ \\text{ and } \\angle AEB = 60^\\circ \\text{ meet along ray } EA",
         "\\angle DEB = 75^\\circ + 60^\\circ = 135^\\circ"),
        (False, "\\angle DAE", 150, "Easy",
         "\\angle DAB = 90^\\circ \\text{ and } \\angle BAE = 60^\\circ \\text{ share side } AB \\text{ on opposite sides}",
         "\\angle DAE = 90^\\circ + 60^\\circ = 150^\\circ"),
        (False, "\\angle ADE", 15, "Medium",
         "AD = AB = AE \\implies \\triangle ADE \\text{ is isosceles with apex } \\angle DAE = 150^\\circ",
         "\\angle ADE = \\frac{180^\\circ - 150^\\circ}{2} = 15^\\circ"),
        (False, "\\angle EDC", 75, "Medium",
         "\\angle ADE = 15^\\circ \\text{ inside } \\angle ADC = 90^\\circ",
         "\\angle EDC = 90^\\circ - 15^\\circ = 75^\\circ"),
        (False, "\\angle DEC", 30, "Medium",
         "\\triangle DEC \\text{ is isosceles with } \\angle EDC = \\angle ECD = 75^\\circ",
         "\\angle DEC = 180^\\circ - 75^\\circ - 75^\\circ = 30^\\circ"),
        (False, "\\angle DEB", 45, "Hard",
         "\\angle AEB = 60^\\circ \\text{ and } \\angle AED = 15^\\circ \\text{ inside } \\angle AEB",
         "\\angle DEB = 60^\\circ - 15^\\circ = 45^\\circ"),
    ]
    for v_i, (inside, target_ang, ans, diff, key_fact, final_eq) in enumerate(sq_eq_cases):
        svg = svg_square_equilateral(inside=inside)
        pos_en = "inside" if inside else "outside"
        pos_ar = "داخل" if inside else "خارج"
        distractors = [15, 30, 45, 60, 75, 120, 135, 150]
        distractors = [d for d in distractors if d != ans]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_sqeq_{v_i}", suffix="^\\circ")
        q_en = (
            f"An equilateral triangle {m('ABE')} is constructed **{pos_en}** the square {m('ABCD')} on side {m('AB')}, as shown. "
            f"Segments {m('DE')} and {m('CE')} are drawn. What is the measure of {m(target_ang)}?"
        )
        q_ar = (
            f"رُسم مثلث متطابق الأضلاع {m('ABE')} **{pos_ar}** المربع {m('ABCD')} على الضلع {m('AB')} كما في الشكل، "
            f"ورُسمت القطعتان {m('DE')} و{m('CE')}. ما قياس الزاوية {m(target_ang)}؟"
        )
        h_en = "Hidden equal-sides secret: since ABCD is a square and ABE is equilateral, AD = AB = AE! So triangle ADE is isosceles!"
        h_ar = "السر الهندسي المخفي: بما أن ABCD مربع وABE متطابق الأضلاع، فإن AD = AB = AE! إذن المثلث ADE متطابق الضلعين!"
        s_en = explain_en(
            "In square + equilateral-triangle puzzles, always spot the **hidden isosceles triangle**: both \\( AD \\) and \\( AE \\) equal \\( AB \\), so \\( AD = AE \\)!",
            [
                f"In square {m('ABCD')} every angle is {m('90^\\circ')}, and in equilateral {m('\\triangle ABE')} every angle is {m('60^\\circ')}.",
                f"Use the equal sides {m('AD = AB = AE')}: {m(key_fact)}.",
                f"Compute the target angle: {m(final_eq)}.",
            ],
            f"By left-right symmetry of the figure, triangles {m('ADE')} and {m('BCE')} are congruent, confirming {m(f'{target_ang} = {ans}^\\circ')}.",
        )
        s_ar = explain_ar(
            "في مسائل المربع مع المثلث متطابق الأضلاع، المفتاح دائماً هو اكتشاف **المثلث متطابق الضلعين المخفي**: لأن \\( AD = AB \\) و\\( AE = AB \\)، فإن \\( AD = AE \\)!",
            [
                f"في المربع {m('ABCD')} كل زاوية {m('90^\\circ')}، وفي المثلث متطابق الأضلاع {m('\\triangle ABE')} كل زاوية {m('60^\\circ')}.",
                f"نستفيد من تساوي الضلعين {m('AD = AE')}: {m(key_fact)}.",
                f"نحسب الزاوية المطلوبة: {m(final_eq)}.",
            ],
            f"من التماثل الأيمن والأيسر للشكل، يتطابق المثلثان {m('ADE')} و{m('BCE')}، مما يؤكد أن {m(f'{target_ang} = {ans}^\\circ')}.",
        )
        push(diff, "kmc_g89_square_equilateral_angles", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 7. Grid polygon perimeter via Pythagorean theorem (10 Qs)
    # ------------------------------------------------------------------
    gp_cases = [
        # (cols, rows, vertices, labels, diff) — every edge has integer length!
        (4, 3, [(0, 0), (4, 0), (4, 3)], ["A", "B", "C"], "Easy"),                        # 4 + 3 + 5 = 12
        (6, 4, [(0, 0), (6, 0), (3, 4)], ["A", "B", "C"], "Easy"),                        # 6 + 5 + 5 = 16
        (7, 4, [(0, 0), (4, 0), (7, 4), (3, 4)], ["A", "B", "C", "D"], "Easy"),           # 4 + 5 + 4 + 5 = 18
        (8, 4, [(0, 0), (8, 0), (5, 4), (3, 4)], ["A", "B", "C", "D"], "Medium"),         # 8 + 5 + 2 + 5 = 20
        (6, 8, [(3, 0), (6, 4), (3, 8), (0, 4)], ["A", "B", "C", "D"], "Medium"),         # rhombus 4*5 = 20
        (9, 4, [(0, 0), (9, 0), (6, 4), (0, 4)], ["A", "B", "C", "D"], "Medium"),         # right trap 9 + 5 + 6 + 4 = 24
        (8, 6, [(0, 0), (8, 0), (8, 6)], ["A", "B", "C"], "Medium"),                      # 8 + 6 + 10 = 24
        (12, 5, [(0, 0), (12, 0), (12, 5)], ["A", "B", "C"], "Medium"),                   # 12 + 5 + 13 = 30
        (10, 8, [(0, 0), (10, 0), (7, 4), (7, 8), (0, 8)], ["A", "B", "C", "D", "E"], "Hard"),  # 10+5+4+7+8=34? wait E(0,8)->A(0,0) is 8!
        (12, 9, [(0, 0), (12, 0), (9, 4), (9, 9), (0, 9)], ["A", "B", "C", "D", "E"], "Hard"),  # 12+5+5+9+9=40!
    ]
    for v_i, (cols, rows, verts, lbls, diff) in enumerate(gp_cases):
        edges = []
        for i in range(len(verts)):
            x1, y1 = verts[i]
            x2, y2 = verts[(i + 1) % len(verts)]
            d = math.hypot(x2 - x1, y2 - y1)
            assert abs(d - round(d)) < 1e-9, f"Non-integer edge {d}"
            edges.append((lbls[i] + lbls[(i + 1) % len(verts)], abs(x2 - x1), abs(y2 - y1), int(round(d))))
        ans = sum(e[3] for e in edges)
        svg = svg_grid_polygon(cols, rows, verts, lbls)
        distractors = [ans - 2, ans + 2, ans + 4, sum(e[1] + e[2] for e in edges), max(6, ans - 3)]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_gper_{v_i}")
        poly_nm = "".join(lbls)
        edge_desc_en = ", ".join(
            f"{m(f'{nm} = {ln}')}" if (dx == 0 or dy == 0) else f"{m(f'{nm} = \\sqrt{{{dx}^2 + {dy}^2}} = {ln}')}"
            for nm, dx, dy, ln in edges
        )
        sum_expr = " + ".join(str(e[3]) for e in edges) + f" = {ans}"
        v_desc = ", ".join(f"{nm}({vx},{vy})" for nm, (vx, vy) in zip(lbls, verts))
        q_en = (
            f"Polygon {m(poly_nm)} with vertices {m(v_desc)} is drawn on a grid of {m('1\\text{ cm} \\times 1\\text{ cm}')} unit squares, as shown. "
            f"What is the **perimeter** of polygon {m(poly_nm)} (in cm)?"
        )
        q_ar = (
            f"رُسم المضلع {m(poly_nm)} الذي رؤوسه {m(v_desc)} على شبكة مربعات طول ضلع كل مربع وحدة منها {m('1\\text{ cm}')} كما في الشكل. "
            f"ما **محيط** المضلع {m(poly_nm)} (بالسنتيمتر)؟"
        )
        h_en = "Count grid units directly along horizontal/vertical sides, and use the Pythagorean theorem a² + b² = c² for slanted sides!"
        h_ar = "عُدّ وحدات الشبكة مباشرة للأضلاع الأفقية والعمودية، واستخدم نظرية فيثاغورس a² + b² = c² للأضلاع المائلة!"
        s_en = explain_en(
            "On a unit grid, a slanted segment going \\( \\Delta x \\) units across and \\( \\Delta y \\) units up has length \\( \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} \\) by the Pythagorean theorem.",
            [
                f"Find each side length from the grid: {edge_desc_en}.",
                f"Add all side lengths around the boundary: {m(sum_expr)} cm.",
            ],
            "Never count grid steps 'manhattan-style' (across + up) as the slanted length — the hypotenuse is shorter than the sum of its legs!",
        )
        s_ar = explain_ar(
            "على شبكة الوحدات، القطعة المائلة التي تمتد \\( \\Delta x \\) أفقياً و\\( \\Delta y \\) رأسياً يكون طولها \\( \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} \\) حسب نظرية فيثاغورس.",
            [
                f"نوجد طول كل ضلع من الشبكة: {edge_desc_en}.",
                f"نجمع أطوال جميع الأضلاع حول المحيط: {m(sum_expr)} سم.",
            ],
            "تجنب جمع الخطوات الأفقية والرأسية مباشرة كطول للضلع المائل؛ فالوتر أقصر من مجموع ضلعي القائمة!",
        )
        push(diff, "kmc_g89_grid_pythag_perim", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 8. Grid quadrilateral / non-convex polygon area (10 Qs)
    # ------------------------------------------------------------------
    ga_cases = [
        (4, 4, [(0, 1), (3, 0), (4, 3), (1, 4)], ["A", "B", "C", "D"], "Easy"),       # 16 - 4*(1.5) = 10
        (5, 4, [(0, 1), (4, 0), (5, 3), (1, 4)], ["A", "B", "C", "D"], "Easy"),       # 20 - 2*(2) - 2*(1.5) = 13
        (5, 5, [(0, 2), (3, 0), (5, 3), (2, 5)], ["A", "B", "C", "D"], "Medium"),     # 25 - 4*(3) = 13
        (6, 4, [(0, 1), (5, 0), (6, 3), (2, 4)], ["A", "B", "C", "D"], "Medium"),     # 24 - 2.5 - 1.5 - 2 - 3 = 15
        (6, 5, [(0, 2), (4, 0), (6, 3), (2, 5)], ["A", "B", "C", "D"], "Medium"),     # 30 - 4 - 3 - 6 - 3 = 14
        (6, 6, [(0, 2), (4, 0), (6, 4), (2, 6)], ["A", "B", "C", "D"], "Medium"),     # 36 - 4*(4) = 20
        (6, 4, [(0, 0), (6, 2), (0, 4), (2, 2)], ["A", "B", "C", "D"], "Medium"),     # arrowhead: (1/2)*4*6 - (1/2)*4*2 = 12 - 4 = 8
        (6, 6, [(0, 0), (6, 3), (0, 6), (2, 3)], ["A", "B", "C", "D"], "Hard"),       # arrowhead: (1/2)*6*6 - (1/2)*6*2 = 18 - 6 = 12
        (7, 5, [(0, 1), (5, 0), (7, 4), (2, 5)], ["A", "B", "C", "D"], "Hard"),       # 35 - 2.5 - 4 - 2.5 - 4 = 22
        (8, 6, [(0, 2), (6, 0), (8, 4), (2, 6)], ["A", "B", "C", "D"], "Hard"),       # 48 - 6 - 4 - 6 - 4 = 28
    ]
    for v_i, (cols, rows, verts, lbls, diff) in enumerate(ga_cases):
        # Shoelace exact area
        twice_a = abs(sum(
            verts[i][0] * verts[(i + 1) % len(verts)][1] - verts[(i + 1) % len(verts)][0] * verts[i][1]
            for i in range(len(verts))
        ))
        ans = Fraction(twice_a, 2)
        assert ans.denominator == 1
        ans_int = int(ans)
        box_a = cols * rows
        cut_a = box_a - ans_int
        svg = svg_grid_polygon(cols, rows, verts, lbls)
        distractors = [ans_int + 2, max(2, ans_int - 2), ans_int + 4, box_a - cut_a // 2, ans_int + 1]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_int, distractors, f"t2g_garea_{v_i}")
        poly_nm = "".join(lbls)
        v_desc = ", ".join(f"{nm}({vx},{vy})" for nm, (vx, vy) in zip(lbls, verts))
        q_en = (
            f"The shaded quadrilateral {m(poly_nm)} with vertices {m(v_desc)} lies on grid intersections of a {m(f'{cols} \\times {rows}')} unit grid, "
            f"where each small square has area {m('1')}. What is the **area** of {m(poly_nm)}?"
        )
        q_ar = (
            f"تقع رؤوس الشكل الرباعي المظلّل {m(poly_nm)} التي إحداثياتها {m(v_desc)} على تقاطعات شبكة أبعادها {m(f'{cols} \\times {rows}')}، "
            f"حيث مساحة كل مربع صغير تساوي {m('1')}. ما **مساحة** الشكل {m(poly_nm)}؟"
        )
        h_en = "Box-and-subtract trick: take the full outer grid rectangle and subtract the unshaded right triangles around the shaded shape!"
        h_ar = "حيلة الإحاطة والطرح: احسب مساحة مستطيل الشبكة الكامل ثم اطرح مساحات المثلثات البيضاء المحيطة بالشكل المظلّل!"
        s_en = explain_en(
            "Tilted shapes on a grid are easiest to measure by **enclosing them in a rectangle** and subtracting the unshaded right triangles outside.",
            [
                f"Area of the enclosing {m(f'{cols} \\times {rows}')} grid rectangle: {m(f'{cols} \\times {rows} = {box_a}')}.",
                f"Using {m('\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}')} on each unshaded outer triangle, their total area is {m(cut_a)}.",
                f"Subtract from the rectangle: {m(f'{box_a} - {cut_a} = {ans_int}')}.",
            ],
            f"Pick's theorem check (interior lattice points + half boundary points − 1) also yields {m(ans_int)}!",
        )
        s_ar = explain_ar(
            "أسهل طريقة لحساب مساحة شكل مائل على الشبكة هي **إحاطته بمستطيل** ثم طرح مساحات المثلثات القائمة غير المظللة خارجه.",
            [
                f"مساحة مستطيل الشبكة المحيط ({m(f'{cols} \\times {rows}')}): {m(f'{cols} \\times {rows} = {box_a}')}.",
                f"بحساب مساحة كل مثلث أبيض خارجي بالقانون {m('\\frac{1}{2} \\times \\text{القاعدة} \\times \\text{الارتفاع}')} نجد أن مجموع مساحاتها البيضاء هو {m(cut_a)}.",
                f"نطرح من مساحة المستطيل: {m(f'{box_a} - {cut_a} = {ans_int}')}.",
            ],
            f"بالتحقق عبر قانون بيك لنقاط الشبكة نحصل أيضاً على المساحة {m(ans_int)} بالضبط!",
        )
        push(diff, "kmc_g89_grid_polygon_area", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 9. Overlapping two rectangles / squares (Inclusion-Exclusion) (10 Qs)
    # ------------------------------------------------------------------
    ov_cases = [
        (36, 25, 9, "union", "Easy"),
        (48, 30, 12, "union", "Easy"),
        (64, 49, 16, "union", "Easy"),
        (50, 40, 15, "ov", "Medium"),
        (81, 36, 18, "ov", "Medium"),
        (72, 45, 20, "unshaded", "Medium"),
        (60, 44, 14, "unshaded", "Medium"),
        (100, 64, 25, "union", "Medium"),
        (90, 56, 22, "ov", "Hard"),
        (121, 81, 36, "unshaded", "Hard"),
    ]
    for v_i, (a1, a2, ov, mode, diff) in enumerate(ov_cases):
        union_a = a1 + a2 - ov
        unsh_a = a1 + a2 - 2 * ov
        if mode == "union":
            ans = union_a
            svg = svg_overlapping_rects(f"Area {a1}", f"Area {a2}", str(ov))
            distractors = [a1 + a2, unsh_a, union_a + ov // 2 + 2, max(1, union_a - 4)]
            q_en = (
                f"Two rectangles of areas {m(a1)} and {m(a2)} overlap in a smaller shaded rectangle of area {m(ov)}, as shown. "
                f"What is the **total area covered** by the combined figure?"
            )
            q_ar = (
                f"يتقاطع مستطيلان مساحتاهما {m(a1)} و{m(a2)} في مستطيل أصغر مظلّل مساحته {m(ov)} كما في الشكل. "
                f"ما **المساحة الكلية المغطّاة** بالشكل المدمج؟"
            )
            steps_en = [
                f"Adding the two full areas {m(f'{a1} + {a2} = {a1+a2}')} counts the overlap **twice**.",
                f"Subtract the overlap **once** so every point is counted once: {m(f'{a1+a2} - {ov} = {ans}')}.",
            ]
            steps_ar = [
                f"جمع المساحتين كاملتين {m(f'{a1} + {a2} = {a1+a2}')} يحسب منطقة التقاطع **مرتين**.",
                f"نطرح مساحة التقاطع **مرة واحدة** فقط: {m(f'{a1+a2} - {ov} = {ans}')}.",
            ]
        elif mode == "ov":
            ans = ov
            svg = svg_overlapping_rects(f"Area {a1}", f"Area {a2}", "?")
            distractors = [ov * 2, abs(a1 - a2), ov + 5, max(1, ov - 4)]
            q_en = (
                f"Two rectangles have areas {m(a1)} and {m(a2)}. When placed overlapping as shown, "
                f"the total area they cover on the table is {m(union_a)}. What is the area of their shaded overlap?"
            )
            q_ar = (
                f"مستطيلان مساحتاهما {m(a1)} و{m(a2)}. عند وضعهما متقاطعين كما في الشكل، "
                f"بلغت المساحة الكلية التي يغطيانها على الطاولة {m(union_a)}. ما مساحة منطقة التقاطع المظلّلة؟"
            )
            steps_en = [
                f"Sum of individual areas without overlap: {m(f'{a1} + {a2} = {a1+a2}')}.",
                f"The amount lost when overlapping equals the overlap area: {m(f'{a1+a2} - {union_a} = {ans}')}.",
            ]
            steps_ar = [
                f"مجموع مساحتي المستطيلين منفردين: {m(f'{a1} + {a2} = {a1+a2}')}.",
                f"الفرق بين هذا المجموع والمساحة المغطاة هو مساحة التقاطع بالضبط: {m(f'{a1+a2} - {union_a} = {ans}')}.",
            ]
        else:
            ans = unsh_a
            svg = svg_overlapping_rects(f"Area {a1}", f"Area {a2}", str(ov))
            distractors = [union_a, a1 + a2, unsh_a + ov, max(1, unsh_a - 6)]
            q_en = (
                f"Two rectangles of areas {m(a1)} and {m(a2)} overlap in a dark-purple region of area {m(ov)}, as shown. "
                f"What is the sum of the areas of the **two non-overlapping parts**?"
            )
            q_ar = (
                f"يتقاطع مستطيلان مساحتاهما {m(a1)} و{m(a2)} في منطقة بنفسجية داكنة مساحتها {m(ov)} كما في الشكل. "
                f"ما مجموع مساحتي **الجزأين غير المتقاطعين**؟"
            )
            steps_en = [
                f"Non-overlapping part of first rectangle: {m(f'{a1} - {ov} = {a1 - ov}')}.",
                f"Non-overlapping part of second rectangle: {m(f'{a2} - {ov} = {a2 - ov}')}.",
                f"Add the two non-overlapping parts: {m(f'{a1 - ov} + {a2 - ov} = {ans}')}.",
            ]
            steps_ar = [
                f"الجزء غير المتقاطع من المستطيل الأول: {m(f'{a1} - {ov} = {a1 - ov}')}.",
                f"الجزء غير المتقاطع من المستطيل الثاني: {m(f'{a2} - {ov} = {a2 - ov}')}.",
                f"نجمع الجزأين غير المتقاطعين: {m(f'{a1 - ov} + {a2 - ov} = {ans}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_ov_{v_i}")
        h_en = "Watch out whether the overlap is removed once (total covered area) or from BOTH rectangles (non-overlapping parts)!"
        h_ar = "انتبه: هل نطرح منطقة التقاطع مرة واحدة (المساحة الكلية المغطاة) أم نطرحها من كلا المستطيلين (الأجزاء غير المتقاطعة)؟"
        s_en = explain_en("By the Inclusion-Exclusion Principle, \\( A_{\\text{total}} = A_1 + A_2 - A_{\\text{overlap}} \\), whereas \\( A_{\\text{non-overlap}} = (A_1 - A_{\\text{ov}}) + (A_2 - A_{\\text{ov}}) \\).", steps_en, f"Check: \\( {a1-ov} + {ov} + {a2-ov} = {union_a} \\) total covered area.")
        s_ar = explain_ar("حسب مبدأ التضمين والإقصاء: \\( A_{\\text{الكلية}} = A_1 + A_2 - A_{\\text{التقاطع}} \\)، بينما الأجزاء غير المتقاطعة تساوي \\( (A_1 - A_{\\text{التقاطع}}) + (A_2 - A_{\\text{التقاطع}}) \\).", steps_ar, f"تحقق: \\( {a1-ov} + {ov} + {a2-ov} = {union_a} \\) وهي المساحة الكلية المغطاة.")
        push(diff, "kmc_g89_overlapping_rects", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 10. Parallel-line zigzag angle puzzles (9 Qs)
    # ------------------------------------------------------------------
    zz_cases = [
        (35, 48, "mid", "Easy"),
        (42, 53, "mid", "Easy"),
        (29, 64, "mid", "Easy"),
        (38, 47, "bot", "Medium"),
        (51, 62, "top", "Medium"),
        (44, 59, "reflex", "Medium"),
        (37, 68, "reflex", "Medium"),
        (56, 49, "bot", "Hard"),
        (63, 54, "reflex", "Hard"),
    ]
    for v_i, (a_top, a_bot, mode, diff) in enumerate(zz_cases):
        a_mid = a_top + a_bot
        if mode == "mid":
            ans = a_mid
            svg = svg_parallel_zigzag(f"{a_top}°", "?°", f"{a_bot}°")
            q_en = f"Lines {m('L_1')} and {m('L_2')} are parallel. A bent path meets {m('L_1')} at {m(f'{a_top}^\\circ')} and {m('L_2')} at {m(f'{a_bot}^\\circ')}, as shown. What is the acute/obtuse bend angle {m('?^\\circ')}?"
            q_ar = f"المستقيمان {m('L_1')} و{m('L_2')} متوازيان. يلتقي مسار منكسر مع {m('L_1')} بزاوية {m(f'{a_top}^\\circ')} ومع {m('L_2')} بزاوية {m(f'{a_bot}^\\circ')} كما في الشكل. ما قياس زاوية الانكسار {m('?^\\circ')}؟"
            step_calc = f"? = {a_top}^\\circ + {a_bot}^\\circ = {ans}^\\circ"
        elif mode == "bot":
            ans = a_bot
            svg = svg_parallel_zigzag(f"{a_top}°", f"{a_mid}°", "?°")
            q_en = f"Lines {m('L_1')} and {m('L_2')} are parallel. Given the top angle {m(f'{a_top}^\\circ')} and the middle bend angle {m(f'{a_mid}^\\circ')}, what is the bottom angle {m('?^\\circ')}?"
            q_ar = f"المستقيمان {m('L_1')} و{m('L_2')} متوازيان. إذا كانت الزاوية العلوية {m(f'{a_top}^\\circ')} وزاوية الانكسار الوسطى {m(f'{a_mid}^\\circ')}، فما قياس الزاوية السفلية {m('?^\\circ')}؟"
            step_calc = f"{a_top}^\\circ + ? = {a_mid}^\\circ \\implies ? = {a_mid}^\\circ - {a_top}^\\circ = {ans}^\\circ"
        elif mode == "top":
            ans = a_top
            svg = svg_parallel_zigzag("?°", f"{a_mid}°", f"{a_bot}°")
            q_en = f"Lines {m('L_1')} and {m('L_2')} are parallel. Given the middle bend angle {m(f'{a_mid}^\\circ')} and the bottom angle {m(f'{a_bot}^\\circ')}, what is the top angle {m('?^\\circ')}?"
            q_ar = f"المستقيمان {m('L_1')} و{m('L_2')} متوازيان. إذا كانت زاوية الانكسار الوسطى {m(f'{a_mid}^\\circ')} والزاوية السفلية {m(f'{a_bot}^\\circ')}، فما قياس الزاوية العلوية {m('?^\\circ')}؟"
            step_calc = f"? + {a_bot}^\\circ = {a_mid}^\\circ \\implies ? = {a_mid}^\\circ - {a_bot}^\\circ = {ans}^\\circ"
        else:
            ans = 360 - a_mid
            svg = svg_parallel_zigzag(f"{a_top}°", f"{a_mid}°", f"{a_bot}°")
            q_en = f"Lines {m('L_1')} and {m('L_2')} are parallel, and the zigzag forms angles of {m(f'{a_top}^\\circ')} and {m(f'{a_bot}^\\circ')} with {m('L_1')} and {m('L_2')}. What is the **reflex (outer) angle** on the right side of the middle vertex?"
            q_ar = f"المستقيمان {m('L_1')} و{m('L_2')} متوازيان، ويشكّل المسار المنكسر زاويتين قياساهما {m(f'{a_top}^\\circ')} و{m(f'{a_bot}^\\circ')} مع {m('L_1')} و{m('L_2')}. ما قياس **الزاوية المنعكسة (الخارجية)** على يمين الرأس الأوسط؟"
            step_calc = f"\\text{{Inner bend}} = {a_top}^\\circ + {a_bot}^\\circ = {a_mid}^\\circ \\implies \\text{{Reflex}} = 360^\\circ - {a_mid}^\\circ = {ans}^\\circ"

        distractors = [180 - a_mid if 180 - a_mid > 0 else a_mid + 15, ans + 10, max(10, ans - 10), abs(a_top - a_bot) + 20, ans + 20]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_zz_{v_i}", suffix="^\\circ")
        h_en = "Draw an auxiliary line through the middle vertex parallel to L₁ and L₂! It splits the middle bend into two alternate-interior ('Z') angles."
        h_ar = "ارسم مستقيماً مساعداً يمر بالرأس الأوسط موازياً لـ L₁ وL₂! سيقسم زاوية الانكسار إلى زاويتين متبادلتين داخلياً (حرف Z)."
        s_en = explain_en(
            "Drawing a third parallel line \\( L_3 \\) right through the bend splits the bend angle into two alternate-interior angles equal to the top and bottom angles!",
            [
                f"Upper alternate-interior angle = {m(f'{a_top}^\\circ' if mode != 'top' else '?')}; lower alternate-interior angle = {m(f'{a_bot}^\\circ' if mode != 'bot' else '?')}.",
                f"Apply the zigzag sum rule: {m(step_calc)}.",
            ],
            f"Check: top ({m(f'{a_top}^\\circ')}) + bottom ({m(f'{a_bot}^\\circ')}) = inner bend ({m(f'{a_mid}^\\circ')}).",
        )
        s_ar = explain_ar(
            "رسم مستقيم ثالث \\( L_3 \\) يمر برأس الانكسار ويوازي المستقيمين يقسم زاوية الانكسار إلى زاويتين متبادلتين داخلياً تساويان الزاويتين العلوية والسفلية!",
            [
                f"الزاوية المتبادلة العلوية = {m(f'{a_top}^\\circ' if mode != 'top' else '?')}، والزاوية المتبادلة السفلية = {m(f'{a_bot}^\\circ' if mode != 'bot' else '?')}.",
                f"نطبق قاعدة المسار المنكسر: {m(step_calc)}.",
            ],
            f"تحقق: الزاوية العلوية ({m(f'{a_top}^\\circ')}) + الزاوية السفلية ({m(f'{a_bot}^\\circ')}) = زاوية الانكسار الداخلية ({m(f'{a_mid}^\\circ')}).",
        )
        push(diff, "kmc_g89_parallel_zigzag", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 11. Corner-inscribed shaded triangle in rectangle (8 Qs)
    # ------------------------------------------------------------------
    ct_cases = [
        (10, 6, 4, 2, "Easy"),
        (12, 8, 4, 4, "Easy"),
        (10, 8, 4, 3, "Medium"),
        (14, 10, 6, 4, "Medium"),
        (15, 8, 5, 4, "Medium"),
        (16, 10, 6, 5, "Medium"),
        (18, 12, 6, 4, "Hard"),
        (20, 12, 8, 6, "Hard"),
    ]
    for v_i, (L, W, ct, cr, diff) in enumerate(ct_cases):
        # Rectangle L x W. Shaded triangle vertices: A(0,0), P(L - ct, W), Q(L, W - cr)
        # Wait: let's check svg_inscribed_corner_triangle_in_rect(L, W, cut_top, cut_right)!
        # Let's check: top-left segment is L - ct, top-right is ct; right-top is cr, right-bottom is W - cr!
        t1 = Fraction((L - ct) * W, 2)
        t2 = Fraction(ct * cr, 2)
        t3 = Fraction(L * (W - cr), 2)
        ans = L * W - (t1 + t2 + t3)
        assert ans.denominator == 1
        ans_int = int(ans)
        svg = svg_inscribed_corner_triangle_in_rect(L, W, ct, cr)
        distractors = [ans_int + 4, max(2, ans_int - 4), (L * W) // 2, ans_int + 2]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_int, distractors, f"t2g_ct_{v_i}")
        q_en = (
            f"In the {m(f'{L} \\times {W}')} rectangle {m('ABCD')} shown, point {m('P')} lies on {m('DC')} at distance {m(ct)} from {m('C')}, "
            f"and point {m('Q')} lies on {m('BC')} at distance {m(cr)} from {m('C')}. What is the area of the shaded triangle {m('APQ')}?"
        )
        q_ar = (
            f"في المستطيل {m('ABCD')} ذي الأبعاد {m(f'{L} \\times {W}')} الموضح في الشكل، تقع النقطة {m('P')} على {m('DC')} على بُعد {m(ct)} من {m('C')}، "
            f"وتقع النقطة {m('Q')} على {m('BC')} على بُعد {m(cr)} من {m('C')}. ما مساحة المثلث المظلّل {m('APQ')}؟"
        )
        h_en = "Subtract the areas of the three unshaded right triangles (ADP, PCQ, and ABQ) from the rectangle's total area!"
        h_ar = "اطرح مساحات المثلثات القائمة الثلاثة البيضاء (ADP وPCQ وABQ) من المساحة الكلية للمستطيل!"
        s_en = explain_en(
            "Instead of searching for a slanted base and height of \\( \\triangle APQ \\), subtract the **three unshaded right triangles** from the rectangle!",
            [
                f"Rectangle area: {m(f'{L} \\times {W} = {L*W}')}. Also {m(f'DP = {L} - {ct} = {L-ct}')} and {m(f'BQ = {W} - {cr} = {W-cr}')}.",
                f"Areas of the 3 white right triangles: {m(f'\\triangle ADP = \\frac{{1}}{{2}}({W})({L-ct}) = {fmt_val(t1)}')}, "
                f"{m(f'\\triangle PCQ = \\frac{{1}}{{2}}({ct})({cr}) = {fmt_val(t2)}')}, and {m(f'\\triangle ABQ = \\frac{{1}}{{2}}({L})({W-cr}) = {fmt_val(t3)}')}.",
                f"Subtract from {m(L*W)}: {m(f'{L*W} - ({fmt_val(t1)} + {fmt_val(t2)} + {fmt_val(t3)}) = {ans_int}')}.",
            ],
            f"Sum of all four regions: {m(f'{fmt_val(t1)} + {fmt_val(t2)} + {fmt_val(t3)} + {ans_int} = {L*W}')}.",
        )
        s_ar = explain_ar(
            "بدلاً من البحث عن قاعدة وارتفاع مائلين للمثلث \\( \\triangle APQ \\)، نطرح مساحات **المثلثات القائمة الثلاثة البيضاء** من مساحة المستطيل!",
            [
                f"مساحة المستطيل: {m(f'{L} \\times {W} = {L*W}')}، ولدينا {m(f'DP = {L} - {ct} = {L-ct}')} و{m(f'BQ = {W} - {cr} = {W-cr}')}.",
                f"مساحات المثلثات البيضاء الثلاثة: {m(f'\\triangle ADP = {fmt_val(t1)}')}, و{m(f'\\triangle PCQ = {fmt_val(t2)}')}, و{m(f'\\triangle ABQ = {fmt_val(t3)}')}.",
                f"نطرح المجموع من مساحة المستطيل: {m(f'{L*W} - ({fmt_val(t1)} + {fmt_val(t2)} + {fmt_val(t3)}) = {ans_int}')}.",
            ],
            f"مجموع المناطق الأربع يعيد مساحة المستطيل الكاملة {m(L*W)} بالضبط.",
        )
        push(diff, "kmc_g89_corner_triangle_rect", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    # ------------------------------------------------------------------
    # 12. Painted n x n x n cube surface & face counts (8 Qs)
    # ------------------------------------------------------------------
    pc_cases = [
        (3, "at_least_2", "Easy"),
        (4, "at_least_2", "Easy"),
        (5, "at_least_2", "Medium"),
        (4, "at_most_1", "Medium"),
        (5, "at_most_1", "Medium"),
        (3, "unpainted_faces", "Medium"),
        (4, "unpainted_faces", "Hard"),
        (5, "frac_painted", "Hard"),
    ]
    for v_i, (n, mode, diff) in enumerate(pc_cases):
        svg = svg_painted_cube_3d(min(n, 4))
        if mode == "at_least_2":
            ans = 12 * (n - 2) + 8
            distractors = [12 * (n - 2), 6 * (n - 2) ** 2 + 8, n ** 3 - (n - 2) ** 3, ans + 4]
            q_en = f"The outside of a {m(f'{n} \\times {n} \\times {n}')} wooden cube is painted completely purple, and it is then cut into {m(n**3)} unit cubes ({m('1 \\times 1 \\times 1')}). How many unit cubes have **at least 2** painted faces?"
            q_ar = f"طُلِي السطح الخارجي لمكعب خشبي أبعاده {m(f'{n} \\times {n} \\times {n}')} باللون البنفسجي بالكامل، ثم قُطِّع إلى {m(n**3)} مكعباً صغيراً ({m('1 \\times 1 \\times 1')}). كم مكعباً صغيراً له **وجهان مطليان على الأقل**؟"
            steps_en = [
                f"'At least 2 painted faces' means **2 painted faces** (edge cubes) OR **3 painted faces** (corner cubes).",
                f"There are {m('8')} corner cubes (3 faces) and {m(f'12 \\times ({n}-2) = {12*(n-2)}')} edge cubes (2 faces).",
                f"Total: {m(f'8 + {12*(n-2)} = {ans}')}.",
            ]
            steps_ar = [
                f"عبارة «وجهان مطليان على الأقل» تعني **وجهين مطليين** (مكعبات الحواف) أو **3 أوجه مطلية** (مكعبات الرؤوس).",
                f"يوجد {m('8')} مكعبات في الرؤوس، و{m(f'12 \\times ({n}-2) = {12*(n-2)}')} مكعباً على الحواف الـ 12.",
                f"المجموع: {m(f'8 + {12*(n-2)} = {ans}')}.",
            ]
        elif mode == "at_most_1":
            c0 = (n - 2) ** 3
            c1 = 6 * (n - 2) ** 2
            ans = c0 + c1
            distractors = [c1, c0, n ** 3 - 8, ans + 6]
            q_en = f"A {m(f'{n} \\times {n} \\times {n}')} cube is painted on all six outer faces and cut into {m(n**3)} unit cubes. How many unit cubes have **at most 1** painted face?"
            q_ar = f"طُلِيت الأوجه الستة الخارجية لمكعب أبعاده {m(f'{n} \\times {n} \\times {n}')} ثم قُطِّع إلى {m(n**3)} مكعباً صغيراً. كم مكعباً صغيراً له **وجه واحد مطلي على الأكثر**؟"
            steps_en = [
                f"'At most 1' means **0 painted faces** (completely inside) OR **1 painted face** (face-centers).",
                f"0 painted faces: {m(f'({n}-2)^3 = {c0}')}; 1 painted face: {m(f'6 \\times ({n}-2)^2 = {c1}')}.",
                f"Add them: {m(f'{c0} + {c1} = {ans}')}.",
            ]
            steps_ar = [
                f"عبارة «وجه واحد على الأكثر» تعني **0 من الأوجه المطلية** (الداخلية) أو **وجهاً واحداً مطلياً** (مراكز الأوجه).",
                f"0 أوجه مطلية: {m(f'({n}-2)^3 = {c0}')}؛ ووجه واحد مطلي: {m(f'6 \\times ({n}-2)^2 = {c1}')}.",
                f"نجمع العددين: {m(f'{c0} + {c1} = {ans}')}.",
            ]
        elif mode == "unpainted_faces":
            tot_f = 6 * (n ** 3)
            pnt_f = 6 * (n ** 2)
            ans = tot_f - pnt_f
            distractors = [pnt_f, tot_f, ans - 6 * n, (n - 2) ** 3 * 6]
            q_en = f"A {m(f'{n} \\times {n} \\times {n}')} painted cube is cut into {m(n**3)} unit cubes. Counting all {m('6')} faces of every unit cube, how many small square unit faces are **unpainted**?"
            q_ar = f"قُطِّع مكعب مطلي أبعاده {m(f'{n} \\times {n} \\times {n}')} إلى {m(n**3)} مكعباً صغيراً. عند عدّ الأوجه الستة لكل مكعب صغير، كم وجهاً مربعاً صغيراً **غير مطلي**؟"
            steps_en = [
                f"There are {m(n**3)} unit cubes, and each has {m(6)} faces, giving {m(f'6 \\times {n**3} = {tot_f}')} unit faces in total.",
                f"Before cutting, the big cube's outer surface had {m(f'6 \\times {n}^2 = {pnt_f}')} painted unit squares.",
                f"Subtract painted faces from total faces: {m(f'{tot_f} - {pnt_f} = {ans}')} unpainted unit faces.",
            ]
            steps_ar = [
                f"لدينا {m(n**3)} مكعباً صغيراً، ولكل مكعب {m(6)} أوجه، أي {m(f'6 \\times {n**3} = {tot_f}')} وجهاً صغيراً إجمالاً.",
                f"قبل التقطيع، كان السطح الخارجي للمكعب الكبير يتكون من {m(f'6 \\times {n}^2 = {pnt_f}')} مربعاً صغيراً مطلياً.",
                f"نطرح الأوجه المطلية من الكل: {m(f'{tot_f} - {pnt_f} = {ans}')} وجهاً غير مطلي.",
            ]
        else:
            ans = Fraction(1, n)
            distractors = [Fraction(1, n * n), Fraction(2, n), Fraction(n - 1, n), Fraction(6, n ** 3)]
            q_en = f"A {m(f'{n} \\times {n} \\times {n}')} cube is painted on the outside and cut into {m(n**3)} unit cubes. What **fraction of the total surface area** of all {m(n**3)} unit cubes is painted?"
            q_ar = f"طُلِي مكعب أبعاده {m(f'{n} \\times {n} \\times {n}')} من الخارج ثم قُطِّع إلى {m(n**3)} مكعباً صغيراً. ما **الكسر الذي يمثل الجزء المطلي** من مجموع المساحات السطحية لجميع المكعبات الصغيرة؟"
            steps_en = [
                f"Total unit faces across all {m(n**3)} cubes: {m(f'6 \\times {n}^3 = {6 * n**3}')}.",
                f"Painted unit faces (the original outer surface): {m(f'6 \\times {n}^2 = {6 * n**2}')}.",
                f"Divide painted by total: {m(f'\\frac{{6 \\times {n}^2}}{{6 \\times {n}^3}} = \\frac{{1}}{{{n}}}')}.",
            ]
            steps_ar = [
                f"إجمالي الأوجه الصغيرة لجميع المكعبات الـ {m(n**3)}: {m(f'6 \\times {n}^3 = {6 * n**3}')}.",
                f"الأوجه المطلية (السطح الخارجي الأصلي): {m(f'6 \\times {n}^2 = {6 * n**2}')}.",
                f"نقسم المطلي على الكلي: {m(f'\\frac{{6 \\times {n}^2}}{{6 \\times {n}^3}} = \\frac{{1}}{{{n}}}')}.",
            ]

        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, f"t2g_pc_{v_i}")
        h_en = "Classify unit cubes by location (8 corners, 12(n−2) edges, 6(n−2)² face-centers, (n−2)³ interior) — or count total unit faces 6n³ vs painted outer faces 6n²!"
        h_ar = "صنّف المكعبات حسب موقعها (8 رؤوس، 12(n−2) حواف، 6(n−2)² مراكز أوجه، (n−2)³ داخلية) — أو قارن إجمالي الأوجه 6n³ بالأوجه الخارجية المطلية 6n²!"
        s_en = explain_en("Visualizing the 3D painted cube either by cube positions or by total unit faces makes the count completely systematic.", steps_en, f"Note that \\( 8 + 12({n}-2) + 6({n}-2)^2 + ({n}-2)^3 = {n}^3 = {n**3} \\) unit cubes in total.")
        s_ar = explain_ar("تصنيف المكعبات الصغيرة حسب موقعها أو مقارنة عدد الأوجه الكلي بالأوجه الخارجية يجعل العد منظماً ودقيقاً.", steps_ar, f"ملاحظة: مجموع الفئات الأربع يساوي \\( {n}^3 = {n**3} \\) مكعباً صغيراً بالضبط.")
        push(diff, "kmc_g89_painted_cube_surface", q_en, q_ar, opts_en, opts_ar, cidx, cans, h_en, h_ar, s_en, s_ar, svg)

    assert len(out) == 115, f"Expected 115, got {len(out)}"
    return out


if __name__ == "__main__":
    qs = generate()
    print(f"Generated {len(qs)} Track 2 Geometry questions (all with KMC SVGs!) cleanly.")
