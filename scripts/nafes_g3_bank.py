"""ETEC Nafes KSA Grade 3 Question Bank (360 Programmatically Verified 4-Option Questions, 24 Blueprints x 15)."""
from fractions import Fraction

from nafes_common import (
    explain_ar,
    explain_en,
    m,
    make_4_bilingual_options,
    make_nafes_q,
    make_nafes_question,
    svg_balance_scales,
    svg_bar_chart,
    svg_column_cryptarithm,
    svg_cube_stack_3d,
    svg_digital_clock,
    svg_dot_pattern,
    svg_fraction_grid,
    svg_function_machine,
    svg_kang_necklace_beads,
    svg_kang_staircase_perimeter,
    svg_matchstick_squares,
    svg_matchstick_triangles,
    svg_nafes_analog_clock,
    svg_nafes_fraction_bars,
    svg_nafes_function_table,
    svg_nafes_pictograph,
    svg_nafes_place_value_blocks,
    svg_nafes_sar_money,
    svg_nafes_spinner,
    svg_number_strip,
    svg_number_triangle_puzzle,
    svg_painted_cube_3d,
    svg_polyomino,
    svg_regular_polygon,
    svg_two_jars,
)
try:
    from nafes_lessons_g3 import (
        svg_g3_equal_groups,
        svg_g3_equation_balance,
        svg_g3_grid_rect,
        svg_g3_marble_bag,
        svg_g3_metric_card,
        svg_g3_number_line,
        svg_g3_solid_3d,
        svg_g3_symmetry_fig,
        svg_g3_tally_table,
    )
except ImportError:
    from scripts.nafes_lessons_g3 import (
        svg_g3_equal_groups,
        svg_g3_equation_balance,
        svg_g3_grid_rect,
        svg_g3_marble_bag,
        svg_g3_metric_card,
        svg_g3_number_line,
        svg_g3_solid_3d,
        svg_g3_symmetry_fig,
        svg_g3_tally_table,
    )

LEVEL = "Grade 3"


def _make_bilingual_q(
    qid: str,
    topic: str,
    difficulty: str,
    blueprint: str,
    q_en: str,
    q_ar: str,
    pairs: list[tuple[str, str]],
    correct_pair_idx: int,
    hint_en: str,
    hint_ar: str,
    idea_en: str,
    steps_en: list[str],
    check_en: str,
    idea_ar: str,
    steps_ar: list[str],
    check_ar: str,
    diagram_en: str,
) -> dict:
    opts_en, opts_ar, cidx, cans = make_4_bilingual_options(pairs, correct_pair_idx, qid)
    return make_nafes_question(
        qid=qid,
        level=LEVEL,
        topic=topic,
        difficulty=difficulty,
        blueprint=blueprint,
        q_en=q_en,
        q_ar=q_ar,
        opts_en=opts_en,
        opts_ar=opts_ar,
        correct_idx=cidx,
        correct_answer=cans,
        hint_en=hint_en,
        hint_ar=hint_ar,
        sol_en=explain_en(idea_en, steps_en, check_en),
        sol_ar=explain_ar(idea_ar, steps_ar, check_ar),
        diagram_en=diagram_en,
    )


# ==============================================================================
# Topic 1: Numbers & Operations (G3-NUM-01 .. G3-NUM-08)
# ==============================================================================


def _gen_g3_num_01(next_id) -> list[dict]:
    """G3-NUM-01: 4-digit place value, expanded form & digit values."""
    tp, bp = "Numbers & Operations", "G3-NUM-01"
    out = []

    # Easy (5): Place-value blocks & digit values
    easy_specs = [
        ("Fahad", "فهد", 3, 2, 4, 7, "blocks"),
        ("Maha", "مها", 4, 0, 6, 5, "blocks"),
        ("Rakan", "راكان", 5, 8, 3, 1, "hundreds"),
        ("Lina", "لينا", 7, 4, 9, 2, "thousands"),
        ("Badr", "بدر", 6, 3, 5, 0, "tens"),
    ]
    for nm_en, nm_ar, th, hu, te, on, mode in easy_specs:
        num = th * 1000 + hu * 100 + te * 10 + on
        diag = svg_nafes_place_value_blocks(th, hu, te, on)
        if mode == "blocks":
            alt1 = th * 100 + hu * 10 + te if hu == 0 else th * 1000 + te * 100 + hu * 10 + on
            if hu == 0:
                alt1 = th * 100 + te * 10 + on
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Easy", bp,
                f"In Grade 3 math lab, {nm_en} models a number using {m(th)} thousands, {m(hu)} hundreds, {m(te)} tens, and {m(on)} ones as shown. What number did {nm_en} model?",
                f"في معمل الرياضيات للصف الثالث مثّل {nm_ar} عدداً باستعمال {m(th)} ألوف و{m(hu)} مئات و{m(te)} عشرات و{m(on)} آحاد كما في الشكل. ما العدد الذي مثّله {nm_ar}؟",
                num, [alt1, th * 1000 + te * 100 + hu * 10 + on, th * 1000 + hu * 100 + on * 10 + te],
                "Write one digit in each place from thousands down to ones.",
                "اكتب رقماً واحداً في كل منزلة من الألوف حتى الآحاد.",
                "Combine thousands, hundreds, tens, and ones in order.",
                [f"Thousands = {m(th)}, Hundreds = {m(hu)}, Tens = {m(te)}, Ones = {m(on)}.", f"Standard form = {m(num)}."],
                f"{m(f'{th*1000} + {hu*100} + {te*10} + {on} = {num}')}.",
                "نرتّب الأرقام من الألوف إلى الآحاد حسب الجدول المنزلي.",
                [f"الألوف {m(th)}، المئات {m(hu)}، العشرات {m(te)}، الآحاد {m(on)}.", f"الصيغة القياسية هي {m(num)}."],
                f"{m(f'{th*1000} + {hu*100} + {te*10} + {on} = {num}')}.",
                diagram_en=diag,
            ))
        else:
            place_map = {
                "thousands": (th, th * 1000, "thousands", "الألوف"),
                "hundreds": (hu, hu * 100, "hundreds", "المئات"),
                "tens": (te, te * 10, "tens", "العشرات"),
            }
            dig, val, p_en, p_ar = place_map[mode]
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Easy", bp,
                f"{nm_en} wrote the ticket number {m(num)} for the school festival. What is the **place value** of the digit {m(dig)} in {m(num)}?",
                f"كتب {nm_ar} رقم التذكرة {m(num)} لمهرجان المدرسة. ما **القيمة المنزلية** للرقم {m(dig)} في العدد {m(num)}؟",
                val, [dig, dig * 10 if val != dig * 10 else dig * 100, dig * 1000 if val != dig * 1000 else dig * 100],
                f"Find which column holds {m(dig)} and multiply by that column's unit value.",
                f"حدّد منزلة الرقم {m(dig)} لتعرف قيمته المنزلية.",
                f"The digit {m(dig)} stands in the {p_en} place.",
                [f"In {m(num)}, the digit {m(dig)} is in the {p_en} column.", f"So its value is {m(val)}."],
                f"Reading {m(num)} confirms {m(val)} in the {p_en} place.",
                f"الرقم {m(dig)} يقع في منزلة {p_ar}.",
                [f"في العدد {m(num)} يقع الرقم {m(dig)} في عمود {p_ar}.", f"إذن قيمته المنزلية هي {m(val)}."],
                f"تفكيك العدد يؤكد أن قيمة الرقم هي {m(val)}.",
                diagram_en=diag,
            ))

    # Medium (5): Expanded form (including zero placeholders & scrambled addends)
    med_specs = [
        ("Amal", "أمل", 5000, 300, 0, 9, ["5000", "+ 300", "+ 9"]),
        ("Tariq", "طارق", 8000, 0, 70, 4, ["8000", "+ 70", "+ 4"]),
        ("Noura", "نورة", 2000, 900, 40, 0, ["40", "+ 2000", "+ 900"]),
        ("Ziyad", "زياد", 6000, 500, 80, 3, ["80", "+ 3", "+ 6000", "+ 500"]),
        ("Hessa", "حصة", 9000, 100, 0, 6, ["6", "+ 9000", "+ 100"]),
    ]
    for nm_en, nm_ar, v_th, v_hu, v_te, v_on, cards in med_specs:
        ans = v_th + v_hu + v_te + v_on
        expr = " ".join(cards)
        d1 = (v_th // 10) + v_hu + v_te + v_on
        d2 = (v_th) + (v_hu if v_hu else v_te * 10) + (v_on * 10 if v_te == 0 else v_on)
        d3 = ans + 90
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"During a Grade 3 place-value game, {nm_en} drew the sum cards {m(expr)}. What 4-digit number do {nm_en}'s cards make in standard form?",
            f"في لعبة القيمة المنزلية للصف الثالث سحبت/سحب {nm_ar} بطاقات الجمع {m(expr)}. ما العدد بالصيغة القياسية؟",
            ans, [d1, d2, d3],
            "Sort the addends into thousands, hundreds, tens, and ones, putting 0 for any missing place.",
            "رتّب القيم حسب الألوف والمئات والعشرات والآحاد وضع صفراً للمنزلة الغائبة.",
            "Match each card to its place-value slot from 1,000s down to 1s.",
            [
                f"Thousands = {m(v_th // 1000)}, Hundreds = {m(v_hu // 100)}, Tens = {m(v_te // 10)}, Ones = {m(v_on)}.",
                f"Standard form = {m(ans)}.",
            ],
            f"Adding {m(f'{v_th} + {v_hu} + {v_te} + {v_on}')} equals {m(ans)}.",
            "نضع كل بطاقة في منزلتها الصحيحة من الألوف حتى الآحاد.",
            [
                f"الألوف = {m(v_th // 1000)}، المئات = {m(v_hu // 100)}، العشرات = {m(v_te // 10)}، الآحاد = {m(v_on)}.",
                f"العدد بالصيغة القياسية هو {m(ans)}.",
            ],
            f"مجموع البطاقات يساوي {m(ans)}.",
            diagram_en=svg_number_strip(cards),
        ))

    # Hard (5): Digit-card smallest/largest 4-digit numbers & place-value riddles
    hard_specs = [
        ("Saud", "سعود", ["4", "0", "7", "2"], "smallest", 2047, [247, 2407, 7420]),
        ("Dana", "دانة", ["1", "8", "0", "5"], "smallest", 1058, [158, 1508, 8510]),
        ("Faisal", "فيصل", ["3", "9", "1", "6"], "greatest", 9631, [9613, 9361, 1369]),
        ("Joud", "جود", ["6", "0", "9", "3"], "smallest", 3069, [369, 3609, 9630]),
        ("Yasser", "ياسر", ["2", "7", "0", "8"], "greatest", 8720, [8702, 8270, 2078]),
    ]
    for nm_en, nm_ar, digs, goal, ans, dists in hard_specs:
        g_ar = "أصغر" if goal == "smallest" else "أكبر"
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            f"{nm_en} has the four digit cards shown below and uses each card once. What is the **{goal} 4-digit number** {nm_en} can build?",
            f"لدى {nm_ar} بطاقات الأرقام الأربع الموضحة أدناه ويستعمل كل بطاقة مرة واحدة. ما **{g_ar} عدد من 4 أرقام** يمكن تكوينه؟",
            ans, dists,
            "Remember a 4-digit number cannot start with 0 in the thousands place!",
            "تذكّر أن العدد المكوّن من 4 أرقام لا يمكن أن يبدأ بالصفر في منزلة الألوف!",
            "Arrange digits from left (thousands) to right (ones) while keeping thousands non-zero.",
            [
                f"The available digits are {m(', '.join(digs))}.",
                f"Choosing each place carefully from thousands to ones gives {m(ans)}.",
            ],
            f"{m(ans)} uses all four cards once and has {m(4)} full digits.",
            "نرتّب الأرقام من منزلة الألوف يساراً إلى الآحاد يميناً دون وضع الصفر في الألوف.",
            [
                f"الأرقام المتاحة هي {m('، '.join(digs))}.",
                f"الاختيار الصحيح من اليسار إلى اليمين يعطي العدد {m(ans)}.",
            ],
            f"العدد {m(ans)} يستعمل البطاقات الأربع كلها ويتكون من 4 منازل.",
            diagram_en=svg_number_strip(digs),
        ))
    return out



def _gen_g3_num_02(next_id) -> list[dict]:
    """G3-NUM-02: Comparing, ordering & rounding 3-digit and 4-digit numbers."""
    tp, bp = "Numbers & Operations", "G3-NUM-02"
    out = []

    # Easy (5): Direct rounding to nearest 10, 100, or 1,000
    easy_specs = [
        ("Huda", "هدى", 367, 10, "ten", "عشرة", 370, [360, 300, 400], 360, 370),
        ("Majed", "ماجد", 542, 100, "hundred", "مئة", 500, [540, 550, 600], 500, 600),
        ("Rema", "ريما", 850, 100, "hundred", "مئة", 900, [800, 840, 860], 800, 900),
        ("Nawaf", "نواف", 4718, 1000, "thousand", "ألف", 5000, [4000, 4700, 4800], 4000, 5000),
        ("Salma", "سلمى", 2384, 10, "ten", "عشرة", 2380, [2390, 2300, 2400], 2380, 2390),
    ]
    for nm_en, nm_ar, val, unit, u_en, u_ar, ans, dists, lo, hi in easy_specs:
        mid = (lo + hi) // 2
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} recorded {m(val)} steps on a school walkathon badge. What is {m(val)} rounded to the nearest **{u_en}**?",
            f"سجّل/سجّلت {nm_ar} العدد {m(val)} خطوة في يوم المشي المدرسي. ما تقريب العدد {m(val)} إلى أقرب **{u_ar}**؟",
            ans, dists,
            f"Check whether {m(val)} is before or at/past the halfway point {m(mid)}.",
            f"تحقّق هل يقع العدد {m(val)} قبل نقطة المنتصف {m(mid)} أم عندها/بعدها.",
            f"Locate {m(val)} between {m(lo)} and {m(hi)} using the halfway mark {m(mid)}.",
            [f"Halfway between {m(lo)} and {m(hi)} is {m(mid)}.", f"Comparing {m(val)} with {m(mid)} rounds it to {m(ans)}."],
            f"{m(val)} is closer to {m(ans)} (or at the midpoint rounding up).",
            f"نحدّد موقع {m(val)} بين {m(lo)} و{m(hi)} بالنسبة لنقطة المنتصف {m(mid)}.",
            [f"نقطة المنتصف بين {m(lo)} و{m(hi)} هي {m(mid)}.", f"إذن يقترب العدد {m(val)} إلى {m(ans)}."],
            f"التقريب الصحيح إلى أقرب {u_ar} هو {m(ans)}.",
            diagram_en=svg_g3_number_line([(lo, str(lo)), (mid, str(mid)), (hi, str(hi))], mark_pos=val, mark_lbl=str(val), lo=lo, hi=hi),
        ))

    # Medium (5): Comparing 4 4-digit numbers in tables
    med_specs = [
        ("Abha Reading Cup", "مسابقة القراءة في أبها", [("3A", 4729), ("3B", 4792), ("3C", 4297), ("3D", 4789)], "greatest", "الأكبر", 4792, [4789, 4729, 4297]),
        ("Taif Rose Saplings", "شتلات ورد الطائف", [("Farm 1", 3615), ("Farm 2", 3165), ("Farm 3", 3651), ("Farm 4", 3156)], "least", "الأصغر", 3156, [3165, 3615, 3651]),
        ("Jeddah Aquarium Visitors", "زوار فقيه أكواريوم بجدة", [("Sun", 6084), ("Mon", 6804), ("Tue", 6408), ("Wed", 6840)], "greatest", "الأكبر", 6840, [6804, 6408, 6084]),
        ("Madinah Date Crates", "صناديق تمور المدينة", [("Lot A", 5390), ("Lot B", 5309), ("Lot C", 5093), ("Lot D", 5039)], "least", "الأصغر", 5039, [5093, 5309, 5390]),
        ("Dammam Recycling Points", "نقاط التدوير في الدمام", [("Team 1", 7462), ("Team 2", 7624), ("Team 3", 7642), ("Team 4", 7426)], "greatest", "الأكبر", 7642, [7624, 7462, 7426]),
    ]
    for ctx_en, ctx_ar, rows, goal_en, goal_ar, ans, dists in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"The table shows four counts recorded during the {ctx_en}. Which number in the table is the **{goal_en}**?",
            f"يبيّن الجدول أربعة أعداد مسجلة في {ctx_ar}. أي عدد في الجدول هو **{goal_ar}**؟",
            ans, dists,
            "Compare thousands first, then hundreds, then tens, then ones.",
            "قارن منزلة الألوف أولاً، ثم المئات، ثم العشرات، ثم الآحاد.",
            "Compare digits from left to right across all four 4-digit numbers.",
            [f"All four numbers share the same thousands digit.", f"Comparing hundreds, tens, and ones gives {m(ans)} as the {goal_en} number."],
            f"{m(ans)} wins when compared place-by-place from the left.",
            "نقارن الأرقام من أقصى اليسار (الألوف فالمئات فالعشرات فالآحاد).",
            ["جميع الأعداد الأربعة متساوية في منزلة الألوف.", f"بمقارنة المئات ثم العشرات ثم الآحاد نجد أن العدد {goal_ar} هو {m(ans)}."],
            f"المقارنة المنزلية تؤكد أن الإجابة {m(ans)}.",
            diagram_en=svg_nafes_function_table(["Group", "Count"], [[k, v] for k, v in rows]),
        ))

    # Hard (5): Boundary rounding reasoning
    hard_specs = [
        ("What is the **smallest** whole number that rounds **up** to \\( 600 \\) when rounded to the nearest hundred?",
         "ما **أصغر** عدد كلي يُقرَّب إلى **الأعلى** ليصبح \\( 600 \\) عند تقريبه إلى أقرب مئة؟",
         550, [549, 551, 595], 500, 600, 550),
        ("What is the **greatest** whole number that rounds **down** to \\( 430 \\) when rounded to the nearest ten?",
         "ما **أكبر** عدد كلي يُقرَّب إلى **الأسفل** ليصبح \\( 430 \\) عند تقريبه إلى أقرب عشرة؟",
         434, [435, 429, 439], 430, 440, 434),
        ("What is the **smallest** whole number that rounds **up** to \\( 3000 \\) when rounded to the nearest thousand?",
         "ما **أصغر** عدد كلي يُقرَّب إلى **الأعلى** ليصبح \\( 3000 \\) عند تقريبه إلى أقرب ألف؟",
         2500, [2499, 2550, 2900], 2000, 3000, 2500),
        ("What is the **greatest** whole number that rounds **down** to \\( 800 \\) when rounded to the nearest hundred?",
         "ما **أكبر** عدد كلي يُقرَّب إلى **الأسفل** ليصبح \\( 800 \\) عند تقريبه إلى أقرب مئة؟",
         849, [850, 845, 799], 800, 900, 849),
        ("What is the **smallest** whole number that rounds **up** to \\( 1290 \\) when rounded to the nearest ten?",
         "ما **أصغر** عدد كلي يُقرَّب إلى **الأعلى** ليصبح \\( 1290 \\) عند تقريبه إلى أقرب عشرة؟",
         1285, [1284, 1286, 1294], 1280, 1290, 1285),
    ]
    for q_en, q_ar, ans, dists, lo, hi, mk in hard_specs:
        mid = (lo + hi) // 2
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Test the digit right next to the rounding place: 5..9 round up, while 0..4 stay down!",
            "افحص الرقم المجاور لمنزلة التقريب: الأرقام 5..9 تقرّب للأعلى والأرقام 0..4 تبقى للأسفل!",
            "Check the exact halfway boundary on the number line.",
            [f"The halfway point between {m(lo)} and {m(hi)} is {m(mid)}.", f"Testing the boundary gives {m(ans)}."],
            f"Rounding {m(ans)} confirms it lands on the target value, while moving 1 step crosses the boundary.",
            "نفحص حدّ المنتصف الدقيق على خط الأعداد.",
            [f"نقطة المنتصف بين {m(lo)} و{m(hi)} هي {m(mid)}.", f"بتجربة الحد الفاصل نجد العدد {m(ans)}."],
            f"تقريب {m(ans)} يحقق الشرط بدقة تامة.",
            diagram_en=svg_g3_number_line([(lo, str(lo)), (hi, str(hi))], mark_pos=mk, mark_lbl="?", lo=lo, hi=hi),
        ))
    return out


def _gen_g3_num_03(next_id) -> list[dict]:
    """G3-NUM-03: Multi-digit addition with regrouping & two-step primary story totals."""
    tp, bp = "Numbers & Operations", "G3-NUM-03"
    out = []

    # Easy (5): Column addition with regrouping
    easy_specs = [
        ("Adel", "عادل", 248, 175),
        ("Lama", "لمى", 369, 254),
        ("Sami", "سامي", 457, 386),
        ("Wafa", "وفاء", 518, 297),
        ("Yazeed", "يزيد", 635, 189),
    ]
    for nm_en, nm_ar, a, b in easy_specs:
        ans = a + b
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} solves the Grade 3 addition card shown below: {m(f'{a} + {b}')}. What is the correct sum?",
            f"يحل/تحل {nm_ar} بطاقة الجمع الموضحة أدناه: {m(f'{a} + {b}')}. ما ناتج الجمع الصحيح؟",
            ans, [ans - 10, ans - 100, ans + 10],
            "Add ones first, regroup 10 ones into 1 ten, and remember every carried 1!",
            "اجمع الآحاد أولاً وأعد تجميع كل 10 في المنزلة التالية ولا تنسَ الواحد المحمول!",
            "Add place-by-place from ones to hundreds with regrouping.",
            [f"Add ones: {m(f'{a % 10} + {b % 10} = {(a % 10) + (b % 10)}')}, regrouping {m(1)} ten.", f"Complete tens and hundreds to get {m(ans)}."],
            f"{m(f'{ans} - {b} = {a}')}.",
            "نجمع عمودياً من الآحاد إلى المئات مع إعادة التجميع.",
            [f"مجموع الآحاد {m(f'{a % 10} + {b % 10} = {(a % 10) + (b % 10)}')} مع حمل {m(1)} للعشرات.", f"نكمل جمع العشرات والمئات فنحصل على {m(ans)}."],
            f"التحقق بالطرح: {m(f'{ans} - {b} = {a}')}.",
            diagram_en=svg_column_cryptarithm([str(a), str(b)], "?"),
        ))

    # Medium (5): 4-digit story addition
    med_specs = [
        ("Al-Ahsa Palm Grove", "مزرعة نخيل في الأحساء", "Week 1", "Week 2", 1468, 1375, "baskets of dates", "سلة تمر"),
        ("Tabuk School Book Drive", "حملة الكتب في تبوك", "Grade 2", "Grade 3", 1285, 1649, "books", "كتاباً"),
        ("Hail Olive Press", "معصرة زيتون في حائل", "Morning", "Evening", 2356, 1874, "bottles", "عبوة"),
        ("Yanbu Shells Exhibit", "معرض الأصداف في ينبع", "Hall A", "Hall B", 1749, 1586, "shells", "صدفة"),
        ("Najran Citrus Orchard", "بستان حمضيات في نجران", "Truck 1", "Truck 2", 2467, 2385, "oranges", "برتقالة"),
    ]
    for ctx_en, ctx_ar, r1, r2, a, b, item_en, item_ar in med_specs:
        ans = a + b
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"At the {ctx_en}, {r1} delivered {m(a)} {item_en} and {r2} delivered {m(b)} {item_en}. How many {item_en} were delivered altogether?",
            f"في {ctx_ar} جُمع في الدفعة الأولى {m(a)} {item_ar} وفي الدفعة الثانية {m(b)} {item_ar}. ما المجموع الكلي؟",
            ans, [ans - 100, ans - 10, ans + 90],
            "Line up thousands, hundreds, tens, and ones, then add with regrouping.",
            "رتّب المنازل عمودياً من الآحاد إلى الألوف ثم اجمع مع إعادة التجميع.",
            "Sum the two 4-digit deliveries column by column.",
            [f"Add {m(f'{a} + {b}')} starting from the ones place.", f"Regrouping across ones, tens, and hundreds yields {m(ans)}."],
            f"{m(f'{ans} - {a} = {b}')}.",
            "نجمع العددين الرباعيين منزلةً بمنزلة مع إعادة التجميع.",
            [f"نجمع {m(f'{a} + {b}')} بدءاً من منزلة الآحاد.", f"بعد إعادة التجميع نحصل على المجموع {m(ans)}."],
            f"التحقق: {m(f'{ans} - {a} = {b}')}.",
            diagram_en=svg_nafes_function_table(["Batch", "Amount"], [[r1, a], [r2, b], ["Total", "?"]], highlight_cell=(2, 1)),
        ))

    # Hard (5): Two-step primary story totals ("A and B where B = A + d")
    hard_specs = [
        ("Rayyan", "ريان", "Anas", "أنس", 245, 68, "stickers", "ملصقاً"),
        ("Class 3A", "الصف 3أ", "Class 3B", "الصف 3ب", 318, 75, "plastic bottles", "عبوة بلاستيكية"),
        ("Mona", "منى", "Sara", "سارة", 186, 49, "beads", "خرزة"),
        ("Bakery A", "المخبز الأول", "Bakery B", "المخبز الثاني", 425, 87, "pies", "فطيرة"),
        ("Shelf 1", "الرف الأول", "Shelf 2", "الرف الثاني", 274, 58, "magazines", "مجلة"),
    ]
    for n1_en, n1_ar, n2_en, n2_ar, a, diff_v, it_en, it_ar in hard_specs:
        b = a + diff_v
        ans = a + b
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            f"{n1_en} has {m(a)} {it_en}. {n2_en} has {m(diff_v)} **more** {it_en} than {n1_en}. How many {it_en} do {n1_en} and {n2_en} have **in all**?",
            f"لدى {n1_ar} {m(a)} {it_ar}، ولدى {n2_ar} ما يزيد بمقدار {m(diff_v)} على ما لدى {n1_ar}. كم المجموع الكلي معهما **معاً**؟",
            ans, [b, ans - 10, a + diff_v + diff_v],
            f"Two steps! First find how many {n2_en} has, then add both amounts together.",
            f"مسألة من خطوتين! أوجد أولاً ما لدى {n2_ar} ثم اجمع المقدارين معاً.",
            f"Find {n2_en}'s count first, then add it to {n1_en}'s count.",
            [f"{n2_en} has {m(f'{a} + {diff_v} = {b}')}.", f"Together they have {m(f'{a} + {b} = {ans}')}."],
            f"{m(b)} is just {n2_en}'s share; adding {m(a)} gives the combined total {m(ans)}.",
            f"نحسب نصيب {n2_ar} أولاً ثم نجمعه مع نصيب {n1_ar}.",
            [f"ما لدى {n2_ar} = {m(f'{a} + {diff_v} = {b}')}.", f"المجموع الكلي معهما = {m(f'{a} + {b} = {ans}')}."],
            f"لا تتوقف عند الخطوة الأولى ({m(b)})؛ المجموع الكلي هو {m(ans)}.",
            diagram_en=svg_number_strip([f"{a}", f"{a} + {diff_v}", "Total = ?"]),
        ))
    return out


def _gen_g3_num_04(next_id) -> list[dict]:
    """G3-NUM-04: Multi-digit subtraction across zeros & finding missing addends/differences."""
    tp, bp = "Numbers & Operations", "G3-NUM-04"
    out = []

    # Easy (5): 3-digit subtraction with regrouping
    easy_specs = [
        ("Khaled", "خالد", 542, 186, "marbles", "كرة زجاجية"),
        ("Abeer", "عبير", 631, 275, "pages", "صفحة"),
        ("Talal", "طلال", 724, 368, "points", "نقطة"),
        ("Nada", "ندى", 853, 479, "seeds", "بذرة"),
        ("Hamad", "حمد", 915, 548, "tickets", "تذكرة"),
    ]
    for nm_en, nm_ar, tot, sub_v, it_en, it_ar in easy_specs:
        ans = tot - sub_v
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} had {m(tot)} {it_en} and used {m(sub_v)} of them. How many {it_en} does {nm_en} have left?",
            f"كان مع {nm_ar} {m(tot)} {it_ar}، استعمل منها {m(sub_v)}. كم بقي مع {nm_ar}؟",
            ans, [ans + 10, ans + 100, abs((tot // 100 - sub_v // 100) * 100 + abs((tot % 100) - (sub_v % 100)))],
            "Regroup 1 ten as 10 ones and 1 hundred as 10 tens before subtracting.",
            "أعد تجميع عشرة إلى 10 آحاد ومئة إلى 10 عشرات قبل الطرح.",
            "Subtract ones, tens, and hundreds with regrouping.",
            [f"Compute {m(f'{tot} - {sub_v}')} by regrouping from tens and hundreds.", f"The difference is {m(ans)}."],
            f"Inverse addition check: {m(f'{ans} + {sub_v} = {tot}')}.",
            "نطرح مع إعادة التجميع من العشرات والمئات.",
            [f"نحسب {m(f'{tot} - {sub_v}')} بعد إعادة التجميع.", f"الباقي يساوي {m(ans)}."],
            f"التحقق بالجمع العكسي: {m(f'{ans} + {sub_v} = {tot}')}.",
            diagram_en=svg_number_strip([f"{tot} total", f"- {sub_v}", "= ?"]),
        ))

    # Medium (5): Subtracting across zeros
    med_specs = [
        ("School Canteen", "المقصف المدرسي", 500, 263, "juice boxes", "علبة عصير"),
        ("Al-Ula Museum Gift Shop", "متجر متحف العلا", 700, 384, "postcards", "بطاقة بريدية"),
        ("Riyadh Zoo Gate", "بوابة حديقة الحيوان بالرياض", 900, 547, "maps", "خريطة"),
        ("Jazan Mango Stand", "ركن المانجو في جازان", 1000, 468, "mangoes", "ثمرة مانجو"),
        ("Qassim Bakery", "مخبز القصيم", 804, 359, "loaves", "رغيفاً"),
    ]
    for ctx_en, ctx_ar, tot, sub_v, it_en, it_ar in med_specs:
        ans = tot - sub_v
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"The {ctx_en} started the morning with {m(tot)} {it_en} and gave out {m(sub_v)} {it_en}. How many {it_en} remain?",
            f"بدأ {ctx_ar} الصباح بوجود {m(tot)} {it_ar} ووزّع منها {m(sub_v)}. كم بقي لديه؟",
            ans, [ans + 10, ans + 90, ans - 10],
            f"Regroup across the zeros in {m(tot)} before subtracting!",
            f"أعد التجميع عبر الأصفار في العدد {m(tot)} قبل إجراء الطرح!",
            "Decompose across zeros so tens become 9 and ones become 10 (or 14).",
            [f"Set up {m(f'{tot} - {sub_v}')} and regroup across the zero place.", f"Subtracting each column gives {m(ans)}."],
            f"Check by adding: {m(f'{ans} + {sub_v} = {tot}')}.",
            "نعيد التجميع عبر منزلة الصفر ثم نطرح كل منزلة بدقة.",
            [f"نرتّب عملية الطرح {m(f'{tot} - {sub_v}')} ونفك عبر الصفر.", f"ناتج الطرح يساوي {m(ans)}."],
            f"التحقق بالجمع: {m(f'{ans} + {sub_v} = {tot}')}.",
            diagram_en=svg_g3_number_line([(0, "0"), (sub_v, str(sub_v)), (tot, str(tot))], arc=(sub_v, tot, "+ ?"), lo=0, hi=tot),
        ))

    # Hard (5): Two-step combine-then-subtract & missing subtrahend
    hard_specs = [
        ("Auditorium A", "مسرح المدرسة", 800, 275, 268, "seats", "مقعداً"),
        ("Charity Warehouse", "مستودع الجمعية", 900, 346, 289, "food baskets", "سلة غذائية"),
        ("Sports Store", "متجر الرياضة", 700, 218, 245, "balls", "كرة"),
        ("Library Catalog", "فهرس المكتبة", 1000, 364, 378, "books", "كتاباً"),
        ("Greenhouse", "المشتل الزراعي", 650, 195, 228, "flowerpots", "أصيص زهور"),
    ]
    for ctx_en, ctx_ar, tot, p1, p2, it_en, it_ar in hard_specs:
        used = p1 + p2
        ans = tot - used
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            f"The {ctx_en} has {m(tot)} {it_en} in total. Morning visitors took {m(p1)} {it_en} and afternoon visitors took {m(p2)} {it_en}. How many {it_en} are still left?",
            f"يوجد في {ctx_ar} إجمالاً {m(tot)} {it_ar}، أُخذ منها صباحاً {m(p1)} ومساءً {m(p2)}. كم بقي في {ctx_ar}؟",
            ans, [used, tot - p1, ans + 10],
            "Add the morning and afternoon amounts first, then subtract their sum from the total.",
            "اجمع ما أُخذ صباحاً ومساءً أولاً، ثم اطرح المجموع من العدد الكلي.",
            "Combine both parts taken, then subtract from the starting total.",
            [f"Total taken = {m(f'{p1} + {p2} = {used}')}.", f"Remaining = {m(f'{tot} - {used} = {ans}')}."],
            f"{m(f'{p1} + {p2} + {ans} = {tot}')}.",
            "نجمع الدفعتين المأخوذتين أولاً ثم نطرح المجموع من الإجمالي.",
            [f"مجموع ما أُخذ = {m(f'{p1} + {p2} = {used}')}.", f"المتبقي = {m(f'{tot} - {used} = {ans}')}."],
            f"التحقق: {m(f'{p1} + {p2} + {ans} = {tot}')}.",
            diagram_en=svg_nafes_function_table(["Stage", "Count"], [["Start Total", tot], ["Morning", p1], ["Afternoon", p2], ["Left", "?"]], highlight_cell=(3, 1)),
        ))
    return out



def _gen_g3_num_05(next_id) -> list[dict]:
    """G3-NUM-05: Multiplication via equal groups, rectangular arrays & multiplication facts (0–10)."""
    tp, bp = "Numbers & Operations", "G3-NUM-05"
    out = []

    # Easy (5): Equal groups, arrays & zero property
    easy_specs = [
        ("Turki", "تركي", 3, 6, "groups", "baskets", "سلال", "apples", "تفاحات"),
        ("Leen", "لين", 4, 7, "array", "rows", "صفوف", "counters", "قطع عدّ"),
        ("Mishal", "مشعل", 5, 0, "groups", "trays", "صوانٍ", "cups", "أكواب"),
        ("Ghaida", "غيداء", 6, 5, "array", "rows", "صفوف", "stars", "نجمات"),
        ("Bandar", "بندر", 4, 8, "groups", "boxes", "علب", "erasers", "ممحايات"),
    ]
    for nm_en, nm_ar, g, k, mode, g_en, g_ar, it_en, it_ar in easy_specs:
        ans = g * k
        dists = [g + k, max(1, ans - g), ans + g] if k > 0 else [g, 1, g * 2]
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} arranged {m(g)} equal {g_en} with {m(k)} {it_en} in each one. How many {it_en} are there altogether?",
            f"رتّب/رتّبت {nm_ar} العدد {m(g)} من {g_ar} المتساوية وفي كل واحدة {m(k)} {it_ar}. كم المجموع الكلي؟",
            ans, dists,
            "Multiply the number of equal groups by the number in each group.",
            "اضرب عدد المجموعات المتساوية في عدد العناصر داخل كل مجموعة.",
            f"Use multiplication {m(f'{g} \\times {k}')}.",
            [f"There are {m(g)} {g_en} of {m(k)} each.", f"Multiply: {m(f'{g} \\times {k} = {ans}')}."],
            f"Repeated addition of {m(k)} ({m(g)} times) gives {m(ans)}.",
            f"نستعمل حقيقة الضرب {m(f'{g} \\times {k}')}.",
            [f"لدينا {m(g)} من {g_ar} وفي كل منها {m(k)}.", f"حاصل الضرب {m(f'{g} \\times {k} = {ans}')}."],
            f"الجمع المتكرر للعدد {m(k)} يعطي {m(ans)}.",
            diagram_en=svg_g3_equal_groups(g, k, mode=mode, caption=f"{g} x {k}"),
        ))

    # Medium (5): Everyday multiplication word problems up to 10x10
    med_specs = [
        ("Umm Khalid baked \\( 7 \\) trays of maamoul cookies with \\( 8 \\) cookies on each tray. How many cookies did she bake?",
         "خبزت أم خالد \\( 7 \\) صوانٍ من المعمول وفي كل صينية \\( 8 \\) حبات. كم حبة معمول خبزت؟", 7, 8, "array"),
        ("A school minibus lot has \\( 9 \\) vans, and each van carries \\( 6 \\) students to the science fair. How many students ride in total?",
         "انطلقت \\( 9 \\) حافلات صغيرة إلى معرض العلوم، وفي كل حافلة \\( 6 \\) طلاب. كم طالباً ركب إجمالاً؟", 9, 6, "groups"),
        ("A classroom bookshelf has \\( 8 \\) shelves with \\( 9 \\) encyclopedias on each shelf. How many encyclopedias are on the bookshelf?",
         "في خزانة الصف \\( 8 \\) رفوف وعلى كل رف \\( 9 \\) موسوعات علمية. كم موسوعة في الخزانة؟", 8, 9, "array"),
        ("For National Day, \\( 7 \\) groups of students each waved \\( 10 \\) green flags. How many green flags did they wave altogether?",
         "في احتفال اليوم الوطني لوّحت \\( 7 \\) مجموعات طلابية بكل مجموعة \\( 10 \\) أعلام خضراء. كم علماً لوّحوا جميعاً؟", 7, 10, "groups"),
        ("A gardener in Taif planted \\( 6 \\) equal rows with \\( 7 \\) rose bushes in every row. How many rose bushes did he plant?",
         "زرع مزارع في الطائف \\( 6 \\) صفوف متساوية وفي كل صف \\( 7 \\) شجيرات ورد. كم شجيرة زرع؟", 6, 7, "array"),
    ]
    for q_en, q_ar, g, k, mode in med_specs:
        ans = g * k
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, [g + k, ans - k, ans + g],
            "Multiply the number of groups/rows by the count in each one.",
            "اضرب عدد الصفوف أو المجموعات في العدد داخل كل صف.",
            f"Compute {m(f'{g} \\times {k}')}.",
            [f"Number of groups = {m(g)}, size of each group = {m(k)}.", f"Total = {m(f'{g} \\times {k} = {ans}')}."],
            f"{m(f'{ans} \\div {g} = {k}')}.",
            f"نحسب ناتج {m(f'{g} \\times {k}')}.",
            [f"عدد المجموعات {m(g)} وفي كل مجموعة {m(k)}.", f"المجموع الكلي = {m(f'{g} \\times {k} = {ans}')}."],
            f"التحقق بالقسمة: {m(f'{ans} \\div {g} = {k}')}.",
            diagram_en=svg_g3_equal_groups(g, k, mode=mode, caption=f"{g} groups of {k}"),
        ))

    # Hard (5): Two-step multiplication + extra or array difference
    hard_specs = [
        ("Nasser bought \\( 4 \\) packs of \\( 8 \\) markers each, plus \\( 5 \\) single markers. How many markers does Nasser have in all?",
         "اشترى ناصر \\( 4 \\) علب أقلام في كل علبة \\( 8 \\) أقلام، بالإضافة إلى \\( 5 \\) أقلام مفردة. كم قلماً مع ناصر إجمالاً؟",
         37, [32, 17, 52], "4 x 8 + 5", 4, 8, "Multiply 4 by 8 first, then add the 5 extra markers.", "اضرب 4 في 8 أولاً ثم أضف 5 أقلام مفردة."),
        ("Deema glued stickers on \\( 6 \\) pages with \\( 6 \\) stickers per page, and still has \\( 9 \\) stickers left over. How many stickers did she start with?",
         "ألصقت ديمة ملصقات في \\( 6 \\) صفحات بواقع \\( 6 \\) ملصقات في كل صفحة، وبقي معها \\( 9 \\) ملصقات. كم ملصقاً كان معها في البداية؟",
         45, [36, 21, 54], "6 x 6 + 9", 6, 6, "Multiply 6 pages by 6 stickers, then add the 9 remaining stickers.", "اضرب 6 في 6 أولاً ثم اجمع 9 ملصقات متبقية."),
        ("Sara arranged \\( 7 \\) rows of \\( 6 \\) seashells, while Hind arranged \\( 5 \\) rows of \\( 8 \\) seashells. How many **more** seashells did Sara arrange than Hind?",
         "رتّبت سارة \\( 7 \\) صفوف في كل صف \\( 6 \\) صدفات، ورتّبت هند \\( 5 \\) صفوف في كل صف \\( 8 \\) صدفات. بكم **تزيد** صدفات سارة على صدفات هند؟",
         2, [42, 40, 4], "42 - 40", 7, 6, "Find Sara's product (7 × 6) and Hind's product (5 × 8), then subtract.", "احسب حاصل ضرب سارة (7 × 6) وحاصل ضرب هند (5 × 8) ثم اطرح."),
        ("An art teacher has \\( 5 \\) boxes of \\( 9 \\) paintbrushes each. If \\( 7 \\) paintbrushes are drying in the sink, how many dry brushes remain in the boxes?",
         "لدى معلم التربية الفنية \\( 5 \\) علب في كل علبة \\( 9 \\) فُرَش تلوين. إذا أُخذت \\( 7 \\) فُرَش لغسلها، فكم فرشاة بقيت في العلب؟",
         38, [45, 21, 52], "5 x 9 - 7", 5, 9, "Find 5 × 9 first, then subtract the 7 brushes in the sink.", "أوجد ناتج 5 × 9 أولاً ثم اطرح 7 فُرَش."),
        ("Zaid bought \\( 3 \\) notebooks at \\( 7 \\) SAR each and \\( 2 \\) rulers at \\( 4 \\) SAR each. How many Riyals did Zaid spend in all?",
         "اشترى زيد \\( 3 \\) دفاتر بسعر \\( 7 \\) ريالات للدفتر و\\( 2 \\) مسطرة بسعر \\( 4 \\) ريالات للمسطرة. كم ريالاً دفع زيد إجمالاً؟",
         29, [21, 25, 33], "3x7 + 2x4", 3, 7, "Multiply to find the cost of notebooks and the cost of rulers, then add.", "اضرب لإيجاد ثمن الدفاتر وثمن المساطر ثم اجمع الناتجين."),
    ]
    for q_en, q_ar, ans, dists, expr_lbl, g, k, h_en, h_ar in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists, h_en, h_ar,
            "Complete the multiplication step(s) first before adding or subtracting.",
            [f"First compute the equal-groups product ({m(f'{g} \\times {k} = {g*k}')}).", f"Then combine the second step ({m(expr_lbl)}) to obtain {m(ans)}."],
            f"Evaluating {m(expr_lbl)} step-by-step confirms {m(ans)}.",
            "ننفّذ عملية الضرب للمجموعات المتساوية أولاً ثم نجري الجمع أو الطرح.",
            [f"نحسب حاصل ضرب المجموعات المتساوية أولاً ({m(f'{g} \\times {k} = {g*k}')}).", f"ثم نكمل الخطوة الثانية ({m(expr_lbl)}) فنحصل على {m(ans)}."],
            f"مراجعة الخطوتين معاً تؤكد أن الناتج {m(ans)}.",
            diagram_en=svg_g3_equal_groups(g, k, mode="array", caption=expr_lbl),
        ))
    return out


def _gen_g3_num_06(next_id) -> list[dict]:
    """G3-NUM-06: Division as equal sharing, grouping & inverse multiplication fact families."""
    tp, bp = "Numbers & Operations", "G3-NUM-06"
    out = []

    # Easy (5): Fair sharing
    easy_specs = [
        ("Faris", "فارس", 24, 4, "plates", "أطباق", "dates", "تمرات"),
        ("Arwa", "أروى", 35, 5, "bags", "أكياس", "cookies", "كعكات"),
        ("Sultan", "سلطان", 48, 6, "boxes", "صناديق", "toy blocks", "مكعبات"),
        ("Raghad", "رغد", 27, 3, "vases", "مزهريات", "flowers", "زهرات"),
        ("Mazen", "مازن", 40, 8, "tables", "طاولات", "pencils", "أقلام"),
    ]
    for nm_en, nm_ar, tot, g, c_en, c_ar, it_en, it_ar in easy_specs:
        ans = tot // g
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} shares {m(tot)} {it_en} equally among {m(g)} {c_en}. How many {it_en} go into each one?",
            f"وزّع/وزّعت {nm_ar} العدد {m(tot)} من {it_ar} بالتساوي على {m(g)} {c_ar}. كم يوضع في كل واحد؟",
            ans, [ans - 1, ans + 1, tot - g],
            f"Think: what number multiplied by {m(g)} equals {m(tot)}?",
            f"فكّر: ما العدد الذي إذا ضربناه في {m(g)} كان الناتج {m(tot)}؟",
            f"Divide {m(tot)} equally by {m(g)}.",
            [f"Division sentence: {m(f'{tot} \\div {g} = \\square')}.", f"Since {m(f'{g} \\times {ans} = {tot}')}, the answer is {m(ans)}."],
            f"{m(f'{g} \\times {ans} = {tot}')}.",
            f"نقسم {m(tot)} بالتساوي على {m(g)}.",
            [f"جملة القسمة: {m(f'{tot} \\div {g} = \\square')}.", f"بما أن {m(f'{g} \\times {ans} = {tot}')} فإن الناتج {m(ans)}."],
            f"التحقق بالضرب: {m(f'{g} \\times {ans} = {tot}')}.",
            diagram_en=svg_g3_equal_groups(g, ans, mode="groups", caption=f"{tot} shared into {g} equal groups"),
        ))

    # Medium (5): Grouping & inverse fact families
    med_specs = [
        ("A baker puts \\( 54 \\) cupcakes into boxes of \\( 9 \\) cupcakes each. How many boxes does the baker fill?",
         "يضع خباز \\( 54 \\) كعكة في علب تتسع كل علبة لعدد \\( 9 \\) كعكات. كم علبة يملأ الخباز؟", 54, 9),
        ("In the fact-family triangle shown, the top product is \\( 63 \\) and one factor is \\( 7 \\). What is the missing factor \\( ? \\) so that \\( 63 \\div 7 = ? \\)?",
         "في مثلث الحقائق المترابطة الموضح، حاصل الضرب في الأعلى \\( 63 \\) وأحد العاملين \\( 7 \\). ما العامل المفقود \\( ? \\) بحيث يكون \\( 63 \\div 7 = ? \\)؟", 63, 7),
        ("Coach Kareem forms teams of \\( 8 \\) players from \\( 56 \\) Grade 3 students. How many equal teams does he form?",
         "كوّن المدرب كريم فرقاً من \\( 56 \\) طالباً في الصف الثالث بحيث يضم كل فريق \\( 8 \\) لاعبين. كم فريقاً متساوياً كوّن؟", 56, 8),
        ("A librarian stacks \\( 72 \\) workbooks into neat piles of \\( 9 \\) workbooks each. How many piles does she make?",
         "رتّبت أمينة المكتبة \\( 72 \\) كراسة في رزم متساوية تضم كل رزمة \\( 9 \\) كراسات. كم رزمة كوّنت؟", 72, 9),
        ("In the fact-family triangle shown, the top product is \\( 42 \\) and one factor is \\( 6 \\). What missing partner completes \\( 42 \\div 6 = ? \\)?",
         "في مثلث الحقائق المترابطة، العدد العلوي \\( 42 \\) وأحد العاملين \\( 6 \\). ما العدد المفقود الذي يكمل \\( 42 \\div 6 = ? \\)؟", 42, 6),
    ]
    for q_en, q_ar, tot, div_v in med_specs:
        ans = tot // div_v
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, [ans - 1, ans + 1, ans + 2],
            f"Use the multiplication table of {m(div_v)} to solve {m(f'{tot} \\div {div_v}')}.",
            f"استعمل جدول ضرب العدد {m(div_v)} لإيجاد ناتج {m(f'{tot} \\div {div_v}')}.",
            f"Use inverse multiplication for {m(f'{tot} \\div {div_v}')}.",
            [f"Ask: {m(f'{div_v} \\times \\square = {tot}')}.", f"Because {m(f'{div_v} \\times {ans} = {tot}')}, the quotient is {m(ans)}."],
            f"{m(f'{ans} \\times {div_v} = {tot}')}.",
            f"نستعمل حقيقة الضرب العكسية لحل {m(f'{tot} \\div {div_v}')}.",
            [f"نسأل: {m(f'{div_v} \\times \\square = {tot}')}.", f"بما أن {m(f'{div_v} \\times {ans} = {tot}')} فناتج القسمة {m(ans)}."],
            f"{m(f'{ans} \\times {div_v} = {tot}')}.",
            diagram_en=svg_number_triangle_puzzle(str(tot), str(div_v), "?", "÷", "÷", "×"),
        ))

    # Hard (5): Two-step combine/subtract then divide equally
    hard_specs = [
        ("Grandfather picked \\( 45 \\) figs from his garden, kept \\( 9 \\) figs for breakfast, and shared the rest equally among \\( 4 \\) grandchildren. How many figs did each grandchild receive?",
         "قطف الجد \\( 45 \\) حبة تين من حديقته، احتفظ بـ \\( 9 \\) حبات للفطور، ووزّع الباقي بالتساوي على \\( 4 \\) أحفاد. كم حبة أخذ كل حفيد؟",
         9, [11, 8, 36], "45 - 9 = 36", "36 \\div 4 = 9", 4, 9),
        ("Laila collected \\( 18 \\) red shells and \\( 22 \\) white shells on Half Moon Bay, then packed them equally into \\( 5 \\) gift jars. How many shells are in each jar?",
         "جمعت ليلى \\( 18 \\) صدفة حمراء و\\( 22 \\) صدفة بيضاء من شاطئ نصف القمر، ثم وزّعتها بالتساوي في \\( 5 \\) قوارير. كم صدفة في كل قارورة؟",
         8, [7, 9, 40], "18 + 22 = 40", "40 \\div 5 = 8", 5, 8),
        ("A canteen tray holds \\( 50 \\) sandwiches. After \\( 8 \\) teachers each take \\( 1 \\) sandwich, the remaining sandwiches are placed equally onto \\( 6 \\) plates. How many sandwiches are on each plate?",
         "في صينية المقصف \\( 50 \\) شطيرة؛ أخذ \\( 8 \\) معلمين شطيرة لكل واحد، ووُزّع الباقي بالتساوي على \\( 6 \\) أطباق. كم شطيرة في كل طبق؟",
         7, [6, 8, 42], "50 - 8 = 42", "42 \\div 6 = 7", 6, 7),
        ("Two Grade 3 classes donated \\( 26 \\) and \\( 28 \\) storybooks, which were arranged equally onto \\( 9 \\) reading shelves. How many storybooks went on each shelf?",
         "تبرع فصلان في الصف الثالث بـ \\( 26 \\) و\\( 28 \\) قصة، ورُتّبت القصص بالتساوي على \\( 9 \\) رفوف. كم قصة وُضعت على كل رف؟",
         6, [5, 7, 54], "26 + 28 = 54", "54 \\div 9 = 6", 9, 6),
        ("Waleed had \\( 64 \\) SAR. He spent \\( 16 \\) SAR on a geometry set and used the rest to buy \\( 6 \\) identical notebooks. How many Riyals did each notebook cost?",
         "كان مع وليد \\( 64 \\) ريالاً؛ اشترى علبة هندسة بسعر \\( 16 \\) ريالاً واشترى بالباقي \\( 6 \\) دفاتر متماثلة. كم ريالاً سعر الدفتر الواحد؟",
         8, [7, 9, 48], "64 - 16 = 48", "48 \\div 6 = 8", 6, 8),
    ]
    for q_en, q_ar, ans, dists, st1, st2, g, per_g in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "First find the total to be shared, then divide by the number of equal groups.",
            "أوجد أولاً المقدار الصافي المراد توزيعه، ثم اقسمه بالتساوي على عدد المجموعات.",
            "Solve in two clean steps: combine/subtract first, then divide equally.",
            [f"Step 1 quantity to share: {m(st1)}.", f"Step 2 equal division: {m(st2)}."],
            f"{m(f'{g} \\times {per_g} = {g * per_g}')}, matching the shared total.",
            "ننفّذ المسألة في خطوتين: نحسب المقدار الكلي أولاً ثم نقسم بالتساوي.",
            [f"الكمية المراد توزيعها: {m(st1)}.", f"القسمة بالتساوي: {m(st2)}."],
            f"التحقق بالضرب: {m(f'{g} \\times {per_g} = {g * per_g}')}.",
            diagram_en=svg_g3_equal_groups(g, per_g, mode="groups", caption=f"{g} equal shares of ?"),
        ))
    return out



def _gen_g3_num_07(next_id) -> list[dict]:
    """G3-NUM-07: Unit & proper fractions of shaded shapes, fraction strips & number lines."""
    tp, bp = "Numbers & Operations", "G3-NUM-07"
    out = []

    # Easy (5): Naming shaded fraction of strips & grids
    easy_specs = [
        ("Asma", "أسماء", 1, 4, "strip", [Fraction(1, 3), Fraction(3, 4), Fraction(1, 5)]),
        ("Karam", "كرم", 2, 5, "strip", [Fraction(3, 5), Fraction(2, 3), Fraction(1, 5)]),
        ("Shaden", "شادن", 5, 6, "grid_6", [Fraction(1, 6), Fraction(5, 8), Fraction(1, 5)]),
        ("Anwar", "أنور", 3, 8, "strip", [Fraction(5, 8), Fraction(3, 5), Fraction(1, 8)]),
        ("Tala", "تالا", 7, 10, "grid_10", [Fraction(3, 10), Fraction(7, 8), Fraction(1, 10)]),
    ]
    for nm_en, nm_ar, num, den, kind, dists in easy_specs:
        diag = (
            svg_fraction_grid(3, 2, num) if kind == "grid_6"
            else svg_fraction_grid(5, 2, num) if kind == "grid_10"
            else svg_nafes_fraction_bars(num, den, None, None, "?")
        )
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} shaded {m(num)} out of {m(den)} equal parts of the figure shown. What fraction of the whole figure is **shaded**?",
            f"ظلّل/ظلّلت {nm_ar} {m(num)} من أصل {m(den)} أجزاء متطابقة في الشكل الموضح. ما الكسر الذي يمثّل الجزء **المظلل**؟",
            Fraction(num, den), dists,
            "Put the number of shaded parts on top (numerator) and all equal parts on the bottom (denominator).",
            "ضع عدد الأجزاء المظللة في البسط (أعلى) وجميع الأجزاء المتطابقة في المقام (أسفل).",
            "Write shaded parts over total equal parts.",
            [f"Shaded parts = {m(num)}, total equal parts = {m(den)}.", f"Shaded fraction = {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"Numerator {m(num)} out of denominator {m(den)} matches the diagram.",
            "نكتب عدد الأجزاء المظللة في البسط والعدد الكلي للأجزاء المتطابقة في المقام.",
            [f"المظلل = {m(num)}، وإجمالي الأجزاء المتطابقة = {m(den)}.", f"الكسر المظلل = {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"البسط {m(num)} والمقام {m(den)} يطابقان الرسم.",
            diagram_en=diag,
        ))

    # Medium (5): Fractions on a 0-to-1 number line & unshaded fractions
    med_specs = [
        ("Point \\( P \\) marks a spot on the number line divided into \\( 4 \\) equal jumps between \\( 0 \\) and \\( 1 \\). What fraction does red point \\( P \\) represent?",
         "تقع النقطة الحمراء \\( P \\) على خط الأعداد المقسّم إلى \\( 4 \\) أجزاء متساوية بين \\( 0 \\) و\\( 1 \\). ما الكسر الذي تمثّله النقطة \\( P \\)؟",
         3, 4, [Fraction(1, 4), Fraction(3, 5), Fraction(1, 3)], "line"),
        ("Between \\( 0 \\) and \\( 1 \\), the number line is split into \\( 5 \\) equal intervals. Which fraction is located at the red dot \\( P \\)?",
         "قُسّم خط الأعداد بين \\( 0 \\) و\\( 1 \\) إلى \\( 5 \\) مسافات متطابقة. ما الكسر الذي تمثّله النقطة الحمراء \\( P \\)؟",
         4, 5, [Fraction(1, 5), Fraction(3, 5), Fraction(3, 4)], "line"),
        ("The segment from \\( 0 \\) to \\( 1 \\) is divided into \\( 8 \\) equal parts. What fraction does the red point \\( P \\) show?",
         "قُسّمت المسافة من \\( 0 \\) إلى \\( 1 \\) إلى \\( 8 \\) أجزاء متساوية. ما الكسر الذي تشير إليه النقطة الحمراء \\( P \\)؟",
         5, 8, [Fraction(3, 8), Fraction(5, 6), Fraction(7, 8)], "line"),
        ("A rectangular pie is cut into \\( 6 \\) equal slices and \\( 5 \\) slices are shaded. What unit fraction of the pie is **unshaded**?",
         "قُسّمت فطيرة مستطيلة إلى \\( 6 \\) قطع متطابقة وظُلّلت \\( 5 \\) قطع منها. ما كسر الوحدة الذي يمثّل الجزء **غير المظلل**؟",
         1, 6, [Fraction(5, 6), Fraction(1, 5), Fraction(1, 8)], "bar_unshaded"),
        ("A ribbon strip is divided into \\( 10 \\) equal parts and \\( 7 \\) parts are colored blue. What fraction of the ribbon is **still white (unshaded)**?",
         "قُسّم شريط إلى \\( 10 \\) أجزاء متساوية ولُوّنت \\( 7 \\) أجزاء بالأزرق. ما الكسر الذي يمثّل الجزء **الأبيض غير الملون**؟",
         3, 10, [Fraction(7, 10), Fraction(3, 8), Fraction(1, 10)], "bar_unshaded"),
    ]
    for q_en, q_ar, num, den, dists, kind in med_specs:
        if kind == "line":
            ticks = [(i, "0" if i == 0 else ("1" if i == den else "")) for i in range(den + 1)]
            diag = svg_g3_number_line(ticks, mark_pos=num, mark_lbl="P", lo=0, hi=den)
        else:
            diag = svg_nafes_fraction_bars(den - num, den, None, None, f"{den - num}/{den} shaded")
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, Fraction(num, den), dists,
            "Count equal intervals carefully—never count tick marks without checking spaces!",
            "عدّ المسافات أو الأجزاء المتساوية بدقة وتأكّد من المطلوب (النقطة أو غير المظلل)!",
            f"Identify {m(num)} target parts out of {m(den)} equal parts of 1 whole.",
            [f"One whole is split into {m(den)} equal parts.", f"The target count is {m(num)}, giving {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"{m(f'\\frac{{{num}}}{{{den}}}')} lies between {m(0)} and {m(1)}.",
            f"نحدّد {m(num)} أجزاء مطلوبة من أصل {m(den)} أجزاء متطابقة.",
            [f"الواحد الصحيح مقسّم إلى {m(den)} أجزاء متساوية.", f"عدد الأجزاء المطلوبة {m(num)}، فيكون الكسر {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"الكسر {m(f'\\frac{{{num}}}{{{den}}}')} يقع بين {m(0)} و{m(1)}.",
            diagram_en=diag,
        ))

    # Hard (5): Fraction of a multi-color set (complement to total 6, 8, or 10)
    hard_specs = [
        ("A fruit basket holds \\( 8 \\) apples in all: \\( 3 \\) are red, \\( 2 \\) are yellow, and the rest are green. What fraction of all the apples are **green**?",
         "في سلة فاكهة \\( 8 \\) تفاحات: \\( 3 \\) حمراء و\\( 2 \\) صفراء والباقي خضراء. ما الكسر الذي يمثّل التفاح **الأخضر** من السلة كلها؟",
         3, 8, [Fraction(5, 8), Fraction(1, 4), Fraction(3, 5)], [("Red", 3, "#fca5a5"), ("Yellow", 2, "#fde047"), ("Green", 3, "#86efac")]),
        ("A pencil cup holds \\( 10 \\) pens: \\( 4 \\) blue pens, \\( 3 \\) black pens, and the rest red pens. What fraction of the pens are **red**?",
         "في حافظة مكتب \\( 10 \\) أقلام: \\( 4 \\) زرقاء و\\( 3 \\) سوداء والباقي حمراء. ما الكسر الذي يمثّل الأقلام **الحمراء**؟",
         3, 10, [Fraction(7, 10), Fraction(3, 8), Fraction(1, 10)], [("Blue", 4, "#93c5fd"), ("Black", 3, "#cbd5e1"), ("Red", 3, "#fca5a5")]),
        ("On a plate of \\( 6 \\) pastries, \\( 2 \\) have cheese, \\( 3 \\) have thyme, and the rest have honey. What fraction of the pastries have **honey**?",
         "في طبق \\( 6 \\) فطائر: \\( 2 \\) بالجبن و\\( 3 \\) بالزعتر والباقي بالعسل. ما الكسر الذي يمثّل فطائر **العسل**؟",
         1, 6, [Fraction(5, 6), Fraction(1, 5), Fraction(2, 3)], [("Cheese", 2, "#fef08a"), ("Thyme", 3, "#86efac"), ("Honey", 1, "#fdba74")]),
        ("Hanan's bracelet has \\( 8 \\) beads in total: \\( 2 \\) gold, \\( 1 \\) white, and the rest purple. What fraction of the beads are **purple**?",
         "في سوار حنان \\( 8 \\) خرزات: \\( 2 \\) ذهبيتان و\\( 1 \\) بيضاء والباقي بنفسجية. ما الكسر الذي يمثّل الخرزات **البنفسجية**؟",
         5, 8, [Fraction(3, 8), Fraction(5, 6), Fraction(1, 8)], [("Gold", 2, "#fde047"), ("White", 1, "#f8fafc"), ("Purple", 5, "#d8bfe6")]),
        ("A mini aquarium has \\( 10 \\) fish: \\( 2 \\) striped, \\( 1 \\) spotted, and the rest orange. What fraction of all the fish are **orange**?",
         "في حوض صغير \\( 10 \\) سمكات: \\( 2 \\) مخططتان و\\( 1 \\) منقطة والباقي برتقالية. ما الكسر الذي يمثّل السمك **البرتقالي**؟",
         7, 10, [Fraction(3, 10), Fraction(7, 8), Fraction(3, 5)], [("Striped", 2, "#bae6fd"), ("Spotted", 1, "#e2e8f0"), ("Orange", 7, "#fdba74")]),
    ]
    for q_en, q_ar, num, den, dists, bag_items in hard_specs:
        known = den - num
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, Fraction(num, den), dists,
            f"First subtract the known items from {m(den)} to find the remaining count, then write it over {m(den)}.",
            f"اطرح الأعداد المعلومة من الإجمالي {m(den)} أولاً ثم اكتب الباقي في البسط والمقام {m(den)}.",
            f"Find the remaining count out of {m(den)} total items.",
            [f"Remaining target items = {m(f'{den} - {known} = {num}')}.", f"Fraction of the whole group = {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"{m(f'{known} + {num} = {den}')} items in all.",
            f"نحسب العدد المتبقي من أصل {m(den)} ثم نكتبه على صورة كسر.",
            [f"عدد العناصر المطلوبة = {m(f'{den} - {known} = {num}')}.", f"الكسر المطلوب = {m(f'\\frac{{{num}}}{{{den}}}')}."],
            f"التحقق: {m(f'{known} + {num} = {den}')}.",
            diagram_en=svg_g3_marble_bag(bag_items, f"Total = {den}"),
        ))
    return out


def _gen_g3_num_08(next_id) -> list[dict]:
    """G3-NUM-08: Comparing fractions (same denominator or same numerator) & adding/subtracting like fractions."""
    tp, bp = "Numbers & Operations", "G3-NUM-08"
    out = []

    # Easy (5): Same-denominator addition & comparison
    easy_specs = [
        ("Yara ate \\( \\frac{1}{5} \\) of a melon in the morning and \\( \\frac{2}{5} \\) in the evening. What fraction of the melon did Yara eat in all?",
         "أكلت يارا \\( \\frac{1}{5} \\) البطيخة صباحاً و\\( \\frac{2}{5} \\) مساءً. ما الكسر الذي يمثّل ما أكلته يارا إجمالاً؟",
         Fraction(3, 5), [Fraction(2, 5), Fraction(3, 10), Fraction(4, 5)], 1, 5, 2, 5, "add"),
        ("Bader painted \\( \\frac{2}{8} \\) of a poster green and \\( \\frac{3}{8} \\) blue. What fraction of the poster did Bader paint altogether?",
         "لوّن بدر \\( \\frac{2}{8} \\) اللوحة بالأخضر و\\( \\frac{3}{8} \\) بالأزرق. ما الكسر الذي يمثّل الجزء الملوّن كله؟",
         Fraction(5, 8), [Fraction(1, 8), Fraction(5, 10), Fraction(7, 8)], 2, 8, 3, 8, "add"),
        ("Maha walked \\( \\frac{3}{10} \\) km before rest and \\( \\frac{4}{10} \\) km after rest. What total fraction of a kilometer did she walk?",
         "مشت مها \\( \\frac{3}{10} \\) كم قبل الاستراحة و\\( \\frac{4}{10} \\) كم بعدها. ما الكسر الكلي لما مشته؟",
         Fraction(7, 10), [Fraction(1, 10), Fraction(7, 8), Fraction(9, 10)], 3, 10, 4, 10, "add"),
        ("Look at the fraction strips for sixths. Which fraction among \\( \\frac{1}{6}, \\frac{2}{6}, \\frac{4}{6}, \\frac{5}{6} \\) is the **greatest**?",
         "انظر إلى أشرطة الأسداس. أي كسر من الكسور \\( \\frac{1}{6}، \\frac{2}{6}، \\frac{4}{6}، \\frac{5}{6} \\) هو **الأكبر**؟",
         Fraction(5, 6), [Fraction(1, 6), Fraction(1, 3), Fraction(2, 3)], 5, 6, 1, 6, "cmp"),
        ("Nabil drank \\( \\frac{1}{4} \\) liter of milk at breakfast and \\( \\frac{2}{4} \\) liter at dinner. What fraction of a liter did he drink in total?",
         "شرب نبيل \\( \\frac{1}{4} \\) لتر حليب في الفطور و\\( \\frac{2}{4} \\) لتر في العشاء. ما الكسر الكلي لما شربه؟",
         Fraction(3, 4), [Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)], 1, 4, 2, 4, "add"),
    ]
    for q_en, q_ar, ans, dists, n1, d1, n2, d2, mode in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "When denominators match, compare or add only the top numerators and keep the bottom denominator unchanged!",
            "عندما يتساوى المقام نقارن أو نجمع البسطين فقط ويبقى المقام كما هو!",
            "Use the same-denominator rule for like fractions.",
            [f"Both fractions are measured in parts of {m(d1)}.", f"Result = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            "Notice the denominator never doubles when adding like parts.",
            "نطبّق قاعدة الكسور المتشابهة ذات المقام الواحد.",
            [f"الكسران مقسّمان إلى أجزاء من المقام {m(d1)}.", f"الناتج الصحيح هو {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            "المقام يصف حجم الجزء ويبقى ثابتاً دون جمع.",
            diagram_en=svg_nafes_fraction_bars(n1, d1, n2, d2),
        ))

    # Medium (5): Same-numerator comparison & like-fraction subtraction
    med_specs = [
        ("Four identical cakes are sliced differently. Which fraction gives the **smallest** piece: \\( \\frac{1}{2}, \\frac{1}{4}, \\frac{1}{6}, \\) or \\( \\frac{1}{10} \\)?",
         "قُسّمت أربع كعكات متطابقة بطرق مختلفة. أي كسر يعطي **أصغر** قطعة: \\( \\frac{1}{2} \\) أم \\( \\frac{1}{4} \\) أم \\( \\frac{1}{6} \\) أم \\( \\frac{1}{10} \\)؟",
         Fraction(1, 10), [Fraction(1, 2), Fraction(1, 4), Fraction(1, 6)], 1, 2, 1, 10),
        ("Salwa compares \\( \\frac{2}{3}, \\frac{2}{5}, \\frac{2}{8}, \\) and \\( \\frac{2}{10} \\) using fraction strips. Which of these fractions is the **greatest**?",
         "تقارن سلوى بين الكسور \\( \\frac{2}{3} \\) و\\( \\frac{2}{5} \\) و\\( \\frac{2}{8} \\) و\\( \\frac{2}{10} \\) بأشرطة الكسور. أي كسر منها هو **الأكبر**؟",
         Fraction(2, 3), [Fraction(2, 5), Fraction(1, 4), Fraction(1, 5)], 2, 3, 2, 8),
        ("A water bottle was \\( \\frac{7}{8} \\) full. After PE class, \\( \\frac{4}{8} \\) of the bottle was drunk. What fraction of the bottle is still full?",
         "كانت قارورة ماء ممتلئة بمقدار \\( \\frac{7}{8} \\)، وشُرب منها \\( \\frac{4}{8} \\) بعد حصة الرياضة. ما الكسر المتبقي في القارورة؟",
         Fraction(3, 8), [Fraction(5, 8), Fraction(1, 8), Fraction(3, 4)], 7, 8, 4, 8),
        ("Adnan had \\( \\frac{9}{10} \\) of a sticker sheet and gave \\( \\frac{6}{10} \\) to his sister. What fraction of the sheet does Adnan still have?",
         "كان مع عدنان \\( \\frac{9}{10} \\) ورقة ملصقات فأعطى أخته \\( \\frac{6}{10} \\) منها. ما الكسر المتبقي مع عدنان؟",
         Fraction(3, 10), [Fraction(7, 10), Fraction(1, 10), Fraction(3, 5)], 9, 10, 6, 10),
        ("Which unit fraction is **greater** than \\( \\frac{1}{5} \\): \\( \\frac{1}{3}, \\frac{1}{6}, \\frac{1}{8}, \\) or \\( \\frac{1}{10} \\)?",
         "أي كسر وحدة مما يلي **أكبر** من \\( \\frac{1}{5} \\): \\( \\frac{1}{3} \\) أم \\( \\frac{1}{6} \\) أم \\( \\frac{1}{8} \\) أم \\( \\frac{1}{10} \\)؟",
         Fraction(1, 3), [Fraction(1, 6), Fraction(1, 8), Fraction(1, 10)], 1, 3, 1, 5),
    ]
    for q_en, q_ar, ans, dists, n1, d1, n2, d2 in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "With equal numerators, smaller denominators mean larger slices; with equal denominators, subtract numerators!",
            "عند تساوي البسط فالمقام الأصغر يعطي جزءاً أكبر، وعند تساوي المقام نطرح البسطين!",
            "Compare slice sizes or subtract like numerators.",
            [f"Compare the strips {m(f'{n1}/{d1}')} and {m(f'{n2}/{d2}')}.", f"That gives {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            "Visualizing the fraction strips confirms the exact size order.",
            "نقارن طولي الشريطين أو نطرح البسطين مع ثبات المقام.",
            [f"بمقارنة الشريطين {m(f'{n1}/{d1}')} و{m(f'{n2}/{d2}')}.", f"نجد أن الإجابة الصحيحة هي {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            "رسم أشرطة الكسور يؤكد النتيجة بصرياً.",
            diagram_en=svg_nafes_fraction_bars(n1, d1, n2, d2),
        ))

    # Hard (5): Completing 1 whole after two fractional parts (1 - a/d - b/d)
    hard_specs = [
        ("Ali read \\( \\frac{2}{8} \\) of a storybook on Sunday and \\( \\frac{3}{8} \\) on Monday. What fraction of the whole book is **still left** for Ali to read?",
         "قرأ علي \\( \\frac{2}{8} \\) كتاب القصص يوم الأحد و\\( \\frac{3}{8} \\) يوم الإثنين. ما الكسر **المتبقي** من الكتاب ليقرأه علي؟",
         Fraction(3, 8), [Fraction(5, 8), Fraction(1, 8), Fraction(3, 5)], 5, 8),
        ("A farmer planted tomatoes in \\( \\frac{1}{5} \\) of his field and cucumbers in \\( \\frac{2}{5} \\) of the same field. What fraction of the whole field remains **unplanted**?",
         "زرع مزارع الطماطم في \\( \\frac{1}{5} \\) حقله والخيار في \\( \\frac{2}{5} \\) الحقل نفسه. ما الكسر **المتبقي دون زراعة** من الحقل؟",
         Fraction(2, 5), [Fraction(3, 5), Fraction(1, 5), Fraction(3, 10)], 3, 5),
        ("In a school mural, \\( \\frac{2}{6} \\) is colored sky-blue and \\( \\frac{3}{6} \\) is colored desert-gold. What fraction of the whole mural is **left to color**?",
         "في جدارية مدرسية لُوّن \\( \\frac{2}{6} \\) بالأزرق و\\( \\frac{3}{6} \\) بالذهبي. ما الكسر **المتبقي** من الجدارية دون تلوين؟",
         Fraction(1, 6), [Fraction(5, 6), Fraction(1, 5), Fraction(1, 3)], 5, 6),
        ("Mariam used \\( \\frac{3}{10} \\) of a ribbon for a gift box and \\( \\frac{4}{10} \\) for a card. What fraction of the whole ribbon does she have **left**?",
         "استعملت مريم \\( \\frac{3}{10} \\) شريط الزينة لعلبة هدية و\\( \\frac{4}{10} \\) لبطاقة تهنئة. ما الكسر **المتبقي** من الشريط؟",
         Fraction(3, 10), [Fraction(7, 10), Fraction(1, 10), Fraction(3, 8)], 7, 10),
        ("A pizza is cut into \\( 8 \\) equal slices. Father eats \\( \\frac{3}{8} \\) and Mother eats \\( \\frac{4}{8} \\). What fraction of the whole pizza remains on the tray?",
         "قُسّمت فطيرة بيتزا إلى \\( 8 \\) قطع متطابقة؛ أكل الأب \\( \\frac{3}{8} \\) وأكلت الأم \\( \\frac{4}{8} \\). ما الكسر المتبقي من الفطيرة؟",
         Fraction(1, 8), [Fraction(7, 8), Fraction(3, 8), Fraction(1, 6)], 7, 8),
    ]
    for q_en, q_ar, ans, dists, used_n, den in hard_specs:
        rem_n = ans.numerator
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            f"Write 1 whole as {m(f'{den}/{den}')}, add the two used fractions, and subtract from {m(f'{den}/{den}')}.",
            f"اكتب الواحد الصحيح على صورة {m(f'{den}/{den}')} ثم اطرح مجموع الكسرين المستعملين منه.",
            f"Add the two parts first, then subtract from {m(f'\\frac{{{den}}}{{{den}}}')}.",
            [f"Used altogether = {m(f'\\frac{{{used_n}}}{{{den}}}')}.", f"Remaining = {m(f'\\frac{{{den}}}{{{den}}} - \\frac{{{used_n}}}{{{den}}} = \\frac{{{rem_n}}}{{{den}}}')}."],
            f"{m(f'\\frac{{{used_n}}}{{{den}}} + \\frac{{{rem_n}}}{{{den}}} = \\frac{{{den}}}{{{den}}} = 1')} whole.",
            f"نجمع الجزأين أولاً ثم نطرح المجموع من الواحد الصحيح {m(f'\\frac{{{den}}}{{{den}}}')}.",
            [f"المجموع المستعمل = {m(f'\\frac{{{used_n}}}{{{den}}}')}.", f"المتبقي = {m(f'\\frac{{{den}}}{{{den}}} - \\frac{{{used_n}}}{{{den}}} = \\frac{{{rem_n}}}{{{den}}}')}."],
            f"التحقق: {m(f'\\frac{{{used_n}}}{{{den}}} + \\frac{{{rem_n}}}{{{den}}} = 1')}.",
            diagram_en=svg_nafes_fraction_bars(used_n, den, rem_n, den, f"{used_n}/{den} used", "? left"),
        ))
    return out



# ==============================================================================
# Topic 2: Algebra (G3-ALG-01 .. G3-ALG-04)
# ==============================================================================


def _gen_g3_alg_01(next_id) -> list[dict]:
    """G3-ALG-01: Skip-counting & arithmetic number patterns."""
    tp, bp = "Algebra", "G3-ALG-01"
    out = []

    # Easy (5): Next term in skip-counting sequences
    easy_specs = [
        ("Hassan", "حسان", [15, 20, 25, 30], 5, 35),
        ("Najla", "نجلاء", [12, 16, 20, 24], 4, 28),
        ("Rami", "رامي", [130, 140, 150, 160], 10, 170),
        ("Bushra", "بشرى", [21, 24, 27, 30], 3, 33),
        ("Marwan", "مروان", [400, 500, 600, 700], 100, 800),
    ]
    for nm_en, nm_ar, terms, step, ans in easy_specs:
        seq_str = ", ".join(str(x) for x in terms) + ", ?"
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} skip-counts along the number strip: {m(seq_str)}. What number comes next?",
            f"يعدّ/تعدّ {nm_ar} قفزياً على شريط الأعداد: {m(seq_str)}. ما العدد التالي في النمط؟",
            ans, [ans - 1, ans + step, ans - step + 2],
            f"Find how much is added from one box to the next.",
            "أوجد مقدار الزيادة الثابتة من خانة إلى الخانة التي تليها.",
            f"The pattern adds {m(f'+{step}')} at every step.",
            [f"Each jump adds {m(step)} ({m(f'{terms[0]} + {step} = {terms[1]}')}).", f"Next term = {m(f'{terms[-1]} + {step} = {ans}')}."],
            f"{m(f'{ans} - {terms[-1]} = {step}')}.",
            f"القاعدة هي إضافة {m(step)} في كل خطوة.",
            [f"الفرق بين كل حدين متتاليين هو {m(f'+{step}')}.", f"الحد التالي = {m(f'{terms[-1]} + {step} = {ans}')}."],
            f"{m(f'{ans} - {terms[-1]} = {step}')}.",
            diagram_en=svg_number_strip([str(x) for x in terms] + ["?"]),
        ))

    # Medium (5): Missing middle term (increasing & decreasing)
    med_specs = [
        ("Aseel", "أسيل", ["18", "25", "?", "39", "46"], "+7", 32, [31, 33, 34]),
        ("Othman", "عثمان", ["74", "68", "?", "56", "50"], "-6", 62, [60, 61, 64]),
        ("Danah", "دانة", ["125", "150", "175", "?", "225"], "+25", 200, [185, 195, 205]),
        ("Samer", "سامر", ["92", "84", "?", "68", "60"], "-8", 76, [74, 75, 78]),
        ("Waad", "وعد", ["350", "400", "?", "500", "550"], "+50", 450, [425, 440, 475]),
    ]
    for nm_en, nm_ar, cells, rule, ans, dists in med_specs:
        seq_str = ", ".join(cells)
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"In {nm_en}'s pattern card {m(seq_str)}, one middle number is missing. What number belongs in place of {m('?')}?",
            f"في بطاقة النمط لدى {nm_ar}: {m(seq_str)}، يوجد عدد مفقود في الوسط. ما العدد الذي يحل محل {m('?')}؟",
            ans, dists,
            "Check both known neighbor pairs to find the constant step, then test your answer forward to the next box!",
            "احسب القفزة من زوجين معلومين ثم طبّقها وتأكّد من الوصول إلى العدد الذي يليه!",
            f"Apply the constant step {m(rule)} across the missing middle slot.",
            [f"Known neighbors show the constant rule {m(rule)}.", f"Applying {m(rule)} gives {m(ans)}."],
            f"Continuing {m(rule)} from {m(ans)} lands right on the next term in the strip.",
            f"نطبّق القفزة الثابتة {m(rule)} لإيجاد الحد الأوسط.",
            [f"الحدود المعلومة تُظهر القاعدة الثابتة {m(rule)}.", f"بتطبيق القاعدة نجد العدد المفقود {m(ans)}."],
            f"استمرار تطبيق {m(rule)} على {m(ans)} يوصلنا للحد التالي تماماً.",
            diagram_en=svg_number_strip(cells),
        ))

    # Hard (5): Alternating two-step rules & multi-week story patterns
    hard_specs = [
        ("Look at the two-step jumping rule on the strip: \\( 10, 16, 14, 20, 18, ? \\) (add \\( 6 \\), then subtract \\( 2 \\), repeating). What number comes next?",
         "انظر إلى نمط القفزتين المتناوبتين: \\( 10, 16, 14, 20, 18, ? \\) (اجمع \\( 6 \\) ثم اطرح \\( 2 \\) بالتناوب). ما العدد التالي؟",
         24, [16, 22, 26], ["10", "16", "14", "20", "18", "?"], "+6 then -2"),
        ("A pattern alternates **add \\( 10 \\)**, then **add \\( 5 \\)**: \\( 15, 25, 30, 40, 45, ? \\). What is the next number?",
         "يتبع نمط عددي القاعدة المتناوبة (**اجمع \\( 10 \\)** ثم **اجمع \\( 5 \\)**): \\( 15, 25, 30, 40, 45, ? \\). ما العدد التالي؟",
         55, [50, 60, 65], ["15", "25", "30", "40", "45", "?"], "+10 then +5"),
        ("Jana saves \\( 12 \\) SAR in Week 1, \\( 19 \\) SAR in Week 2, and \\( 26 \\) SAR in Week 3, adding \\( 7 \\) SAR each week. How many Riyals will she save in **Week 6**?",
         "تدّخر جنى \\( 12 \\) ريالاً في الأسبوع 1، و\\( 19 \\) ريالاً في الأسبوع 2، و\\( 26 \\) ريالاً في الأسبوع 3 بزيادة \\( 7 \\) ريالات أسبوعياً. كم ريالاً تدّخر في **الأسبوع 6**؟",
         47, [40, 42, 54], ["W1:12", "W2:19", "W3:26", "W6:?"], "+7 per week"),
        ("A seedling is \\( 18 \\) cm tall in Month 1 and grows \\( 6 \\) cm every month (\\( 18, 24, 30, \\dots \\)). How tall in centimeters will it be in **Month 7**?",
         "طول شتلة \\( 18 \\) سم في الشهر 1 وتنمو \\( 6 \\) سم كل شهر (\\( 18, 24, 30, \\dots \\)). كم سنتيمتراً يصبح طولها في **الشهر 7**؟",
         54, [48, 42, 60], ["M1:18", "M2:24", "M3:30", "M7:?"], "+6 per month"),
        ("A number frog starts at \\( 50 \\) and alternates **subtract \\( 8 \\)**, then **add \\( 3 \\)**: \\( 50, 42, 45, 37, 40, ? \\). Where does it land next?",
         "يبدأ ضفدع الأعداد عند \\( 50 \\) ويتناوب بين **طرح \\( 8 \\)** ثم **جمع \\( 3 \\)**: \\( 50, 42, 45, 37, 40, ? \\). على أي عدد يقفز تالياً؟",
         32, [35, 43, 29], ["50", "42", "45", "37", "40", "?"], "-8 then +3"),
    ]
    for q_en, q_ar, ans, dists, cells, rule_lbl in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Write each step carefully up to the target position so you do not stop one step early!",
            "اكتب الحدود خطوةً بخطوة حتى تصل إلى الموضع المطلوب دون التوقف مبكراً!",
            f"Extend the rule ({rule_lbl}) step-by-step to the target term.",
            [f"Follow the rule ({rule_lbl}) from the given terms.", f"Extending to the requested position gives {m(ans)}."],
            f"Double-checking every jump confirms {m(ans)}.",
            f"نوسّع قاعدة النمط ({rule_lbl}) خطوةً بخطوة حتى الحد المطلوب.",
            [f"نتتبّع القاعدة ({rule_lbl}) بدءاً من الحدود المعطاة.", f"عند الوصول للحد المطلوب نحصل على {m(ans)}."],
            f"مراجعة جميع القفزات تؤكد أن الناتج {m(ans)}.",
            diagram_en=svg_number_strip(cells),
        ))
    return out


def _gen_g3_alg_02(next_id) -> list[dict]:
    """G3-ALG-02: Repeating visual/shape patterns & growing tile steps."""
    tp, bp = "Algebra", "G3-ALG-02"
    out = []

    # Easy (5): Next bead/shape in a repeating pattern
    easy_specs = [
        (["R", "R", "B", "R", "R", "B", "R", "R", "?"],
         [("Blue (B)", "أزرق (B)"), ("Red (R)", "أحمر (R)"), ("Yellow (Y)", "أصفر (Y)"), ("Green (G)", "أخضر (G)")],
         "Red, Red, Blue", "أحمر، أحمر، أزرق"),
        (["Y", "G", "P", "Y", "G", "P", "Y", "?"],
         [("Green (G)", "أخضر (G)"), ("Yellow (Y)", "أصفر (Y)"), ("Purple (P)", "بنفسجي (P)"), ("Red (R)", "أحمر (R)")],
         "Yellow, Green, Purple", "أصفر، أخضر، بنفسجي"),
        (["B", "Y", "Y", "B", "Y", "Y", "?"],
         [("Blue (B)", "أزرق (B)"), ("Yellow (Y)", "أصفر (Y)"), ("Green (G)", "أخضر (G)"), ("White (W)", "أبيض (W)")],
         "Blue, Yellow, Yellow", "أزرق، أصفر، أصفر"),
        (["G", "R", "W", "B", "G", "R", "W", "?"],
         [("Blue (B)", "أزرق (B)"), ("Green (G)", "أخضر (G)"), ("Red (R)", "أحمر (R)"), ("White (W)", "أبيض (W)")],
         "Green, Red, White, Blue", "أخضر، أحمر، أبيض، أزرق"),
        (["P", "P", "Y", "G", "P", "P", "Y", "?"],
         [("Green (G)", "أخضر (G)"), ("Purple (P)", "بنفسجي (P)"), ("Yellow (Y)", "أصفر (Y)"), ("Blue (B)", "أزرق (B)")],
         "Purple, Purple, Yellow, Green", "بنفسجي، بنفسجي، أصفر، أخضر"),
    ]
    for beads, pairs, core_en, core_ar in easy_specs:
        seq_txt = " - ".join(beads)
        out.append(_make_bilingual_q(
            next_id(), tp, "Easy", bp,
            f"Rawan strings colored beads in the repeating pattern **{seq_txt}**. Which bead color goes at **?**?",
            f"تنظم روان خرزات ملونة وفق النمط المتكرر **{seq_txt}**. ما لون الخرزة في موضع **?**؟",
            pairs, 0,
            "Circle the repeating core block from the start of the necklace!",
            "ضع خطاً تحت وحدة النمط المتكررة من بداية السلسلة!",
            f"The repeating core is ({core_en}).",
            [f"Core unit: {core_en}.", f"Matching the position of '?' inside the core gives {pairs[0][0]}."],
            "Reading the whole bead sequence aloud sounds smooth and rhythmic.",
            f"وحدة النمط المتكررة هي ({core_ar}).",
            [f"تتكرر الوحدة ({core_ar}) بانتظام.", f"الموضع '?' يقابل {pairs[0][1]}."],
            "قراءة النمط من البداية تؤكد تطابق التكرار.",
            svg_kang_necklace_beads(beads),
        ))

    # Medium (5): Growing stick/dot/cube patterns
    med_specs = [
        ("Look at the row of connected matchstick squares: Step (1) uses \\( 4 \\) sticks, Step (2) uses \\( 7 \\) sticks, and Step (3) uses \\( 10 \\) sticks. How many sticks are needed for **Step (4)**?",
         "انظر إلى مربعات الأعواد المتلاصقة: الشكل (1) فيه \\( 4 \\) أعواد، والشكل (2) فيه \\( 7 \\) أعواد، والشكل (3) فيه \\( 10 \\) أعواد. كم عوداً يلزم لبناء **الشكل (4)**؟",
         13, [12, 14, 16], svg_matchstick_squares((1, 2, 3)), "+3 sticks per square"),
        ("In the connected matchstick triangles shown, Step (1) uses \\( 3 \\) sticks, Step (2) uses \\( 5 \\) sticks, and Step (3) uses \\( 7 \\) sticks. How many sticks are in **Step (5)**?",
         "في مثلثات الأعواد المتجاورة، الشكل (1) يستعمل \\( 3 \\) أعواد، والشكل (2) \\( 5 \\) أعواد، والشكل (3) \\( 7 \\) أعواد. كم عوداً في **الشكل (5)**؟",
         11, [9, 10, 15], svg_matchstick_triangles((1, 2, 3)), "+2 sticks per step"),
        ("In the L-shaped dot growth pattern, Step (1) has \\( 3 \\) dots, Step (2) has \\( 5 \\) dots, and Step (3) has \\( 7 \\) dots. How many dots are in **Step (4)**?",
         "في نمط النقاط على شكل حرف L، الشكل (1) فيه \\( 3 \\) نقاط، والشكل (2) فيه \\( 5 \\) نقاط، والشكل (3) فيه \\( 7 \\) نقاط. كم نقطة في **الشكل (4)**؟",
         9, [8, 10, 11], svg_dot_pattern("L"), "+2 dots per step"),
        ("In the cross dot pattern shown, Step (1) has \\( 5 \\) dots, Step (2) has \\( 9 \\) dots, and Step (3) has \\( 13 \\) dots. How many dots will **Step (4)** have?",
         "في نمط النقاط المتقاطعة الموضح، الشكل (1) يحوي \\( 5 \\) نقاط، والشكل (2) يحوي \\( 9 \\) نقاط، والشكل (3) يحوي \\( 13 \\) نقطة. كم نقطة في **الشكل (4)**؟",
         17, [15, 16, 21], svg_dot_pattern("cross"), "+4 dots per step"),
        ("Noura builds growing cube columns: Column 1 has \\( 2 \\) cubes, Column 2 has \\( 4 \\) cubes, and Column 3 has \\( 6 \\) cubes. How many cubes will **Column 5** have?",
         "تبني نورة أعمدة مكعبات متنامية: العمود 1 فيه \\( 2 \\)، والعمود 2 فيه \\( 4 \\)، والعمود 3 فيه \\( 6 \\). كم مكعباً في **العمود 5**؟",
         10, [8, 9, 12], svg_cube_stack_3d((2, 4, 6)), "+2 cubes per column"),
    ]
    for q_en, q_ar, ans, dists, diag, rule_lbl in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Count how many new pieces are added at each step and continue that constant jump!",
            "احسب عدد القطع المضافة في كل خطوة جديدة واستمر بالقفزة الثابتة نفسها!",
            f"Turn the visual figures into a number sequence ({rule_lbl}).",
            [f"Each new figure adds a constant amount ({rule_lbl}).", f"Extending to the requested figure gives {m(ans)}."],
            f"Checking the sequence step-by-step confirms {m(ans)}.",
            f"نحوّل الأشكال المرسومة إلى متتابعة عددية ({rule_lbl}).",
            [f"كل شكل جديد يضيف مقداراً ثابتاً ({rule_lbl}).", f"بتكملة الخطوات نصل إلى {m(ans)}."],
            f"مراجعة الحدود بالترتيب تؤكد أن الناتج {m(ans)}.",
            diagram_en=diag,
        ))

    # Hard (5): Position & count reasoning in repeating patterns
    hard_specs = [
        ("A classroom border repeats the 3-shape unit **Star, Star, Moon** over and over. How many **Stars** appear in the first \\( 12 \\) shapes?",
         "يتكرر شريط زينة الصف بوحدة من 3 أشكال: **نجمة، نجمة، هلال** باستمرار. كم **نجمة** تظهر في أول \\( 12 \\) شكلاً؟",
         8, [4, 6, 9], ["★", "★", "☾", "★", "★", "☾"]),
        ("Tiles along a hallway repeat the 4-color core **Blue, Green, Yellow, Red**. If \\( 16 \\) tiles are laid in order, how many **Blue** tiles are used?",
         "يتكرر بلاط الممر بوحدة من 4 ألوان: **أزرق، أخضر، أصفر، أحمر**. إذا وُضعت \\( 16 \\) بلاطة بالترتيب، فكم بلاطة **زرقاء** استُعملت؟",
         4, [3, 5, 8], ["B", "G", "Y", "R", "B", "G"]),
        ("Stickers repeat in a cycle of 5: **Heart, Heart, Heart, Circle, Circle**. Out of the first \\( 15 \\) stickers, how many are **Hearts**?",
         "تتكرر الملصقات في دورة من 5 أشكال: **قلب، قلب، قلب، دائرة، دائرة**. من بين أول \\( 15 \\) ملصقاً، كم ملصقاً على شكل **قلب**؟",
         9, [3, 6, 10], ["♥", "♥", "♥", "●", "●"]),
        ("Lamps on a festival string repeat **Red, Yellow, Green** (a cycle of \\( 3 \\)). If item 1 is Red, item 2 is Yellow, and item 3 is Green, how many full cycles fit in \\( 18 \\) lamps?",
         "تتكرر مصابيح الزينة بالترتيب **أحمر، أصفر، أخضر** (دورة من \\( 3 \\)). كم دورة كاملة تتكرر في شريط طوله \\( 18 \\) مصباحاً؟",
         6, [3, 5, 9], ["R", "Y", "G", "R", "Y", "G"]),
        ("In a growing square frame pattern, Figure 1 uses \\( 4 \\) tiles, Figure 2 uses \\( 8 \\) tiles, and Figure 3 uses \\( 12 \\) tiles. How many tiles do **Figure 1, Figure 2, and Figure 3 use altogether**?",
         "في نمط إطارات مربعة، الشكل 1 فيه \\( 4 \\) بلاطات، والشكل 2 فيه \\( 8 \\) بلاطات، والشكل 3 فيه \\( 12 \\) بلاطة. كم بلاطة استُعملت في **الأشكال الثلاثة معاً**؟",
         24, [16, 20, 28], ["Fig1: 4", "Fig2: 8", "Fig3: 12"]),
    ]
    for q_en, q_ar, ans, dists, strip_items in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Find how many complete repeating groups fit, then multiply by the count in 1 group (or sum the figures).",
            "أوجد عدد الوحدات المتكررة الكاملة ثم اضرب في عدد الشكل المطلوب داخل الوحدة الواحدة (أو اجمع حدود الأشكال).",
            "Group the pattern into equal repeating blocks (or sum the three step counts).",
            ["Break the total length into complete repeating cycles (or list each figure's count).", f"Computing the total target items gives {m(ans)}."],
            f"Counting group-by-group confirms {m(ans)}.",
            "نقسّم النمط إلى دورات متساوية (أو نجمع قيم الأشكال الثلاثة).",
            ["نحدّد عدد الدورات الكاملة ومحتوى كل دورة.", f"بحساب المطلوب نجد الناتج {m(ans)}."],
            f"التحقق بالعدّ المباشر يؤكد الناتج {m(ans)}.",
            diagram_en=svg_number_strip(strip_items),
        ))
    return out



def _gen_g3_alg_03(next_id) -> list[dict]:
    """G3-ALG-03: Input-output rule tables (+ k, - k, x k, ÷ k)."""
    tp, bp = "Algebra", "G3-ALG-03"
    out = []

    # Easy (5): Direct + k and x k input-output tables
    easy_specs = [
        ("Add 8", "+ 8", [[5, 13], [9, 17], [14, "?"]], 22, [20, 21, 24], "جمع 8"),
        ("Multiply by 3", "x 3", [[4, 12], [7, 21], [9, "?"]], 27, [12, 24, 30], "الضرب في 3"),
        ("Add 15", "+ 15", [[10, 25], [20, 35], [32, "?"]], 47, [42, 45, 57], "جمع 15"),
        ("Multiply by 5", "x 5", [[3, 15], [6, 30], [8, "?"]], 40, [13, 35, 45], "الضرب في 5"),
        ("Subtract 6", "- 6", [[18, 12], [25, 19], [31, "?"]], 25, [24, 26, 37], "طرح 6"),
    ]
    for r_en, sym, rows, ans, dists, r_ar in easy_specs:
        inp = rows[2][0]
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"The function table uses the rule **{r_en}**. What Output number belongs at {m('?')} when the Input is {m(inp)}?",
            f"يتبع جدول المدخلات والمخرجات القاعدة **{r_ar}**. ما قيمة المخرجة عند {m('?')} عندما تكون المدخلة {m(inp)}؟",
            ans, dists,
            f"Apply the rule ({sym}) directly to the Input {m(inp)}.",
            f"طبّق القاعدة ({r_ar}) مباشرة على المدخلة {m(inp)}.",
            f"Apply ({sym}) to Input {m(inp)}.",
            [f"Check Row 1: {m(rows[0][0])} becomes {m(rows[0][1])}.", f"Apply the same rule to {m(inp)} to get {m(ans)}."],
            f"Row 2 ({m(rows[1][0])} -> {m(rows[1][1])}) follows the exact same rule.",
            f"نطبّق قاعدة ({r_ar}) على المدخلة {m(inp)}.",
            [f"نتأكد من الصف الأول: {m(rows[0][0])} تصبح {m(rows[0][1])}.", f"بتطبيق القاعدة نفسها على {m(inp)} نحصل على {m(ans)}."],
            f"الصف الثاني يؤكد ثبات القاعدة.",
            diagram_en=svg_nafes_function_table(["Input", "Output"], rows, highlight_cell=(2, 1)),
        ))

    # Medium (5): Discover hidden rule (- k, x k, ÷ k) from 3 rows
    med_specs = [
        ("Multiply by 7", "× 7", [[2, 14], [5, 35], [8, 56], [9, "?"]], 63, [61, 64, 72], "الضرب في 7"),
        ("Divide by 4", "÷ 4", [[12, 3], [24, 6], [36, 9], [28, "?"]], 7, [6, 8, 24], "القسمة على 4"),
        ("Subtract 14", "- 14", [[30, 16], [42, 28], [55, 41], [63, "?"]], 49, [47, 51, 77], "طرح 14"),
        ("Multiply by 8", "× 8", [[3, 24], [6, 48], [7, 56], [10, "?"]], 80, [64, 70, 88], "الضرب في 8"),
        ("Divide by 6", "÷ 6", [[18, 3], [30, 5], [48, 8], [54, "?"]], 9, [7, 8, 48], "القسمة على 6"),
    ]
    for r_en, sym, rows, ans, dists, r_ar in med_specs:
        inp = rows[3][0]
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"All rows in the input-output table follow the **same hidden rule**. What Output replaces {m('?')} when the Input is {m(inp)}?",
            f"تتبع جميع الصفوف في جدول المدخلات والمخرجات **القاعدة نفسها**. ما المخرجة التي تحل محل {m('?')} عند المدخلة {m(inp)}؟",
            ans, dists,
            "Test your candidate rule on Row 1, Row 2, AND Row 3 before computing Row 4!",
            "اختبر القاعدة على الصفوف الثلاثة المعلومة أولاً قبل حساب الصف الرابع!",
            f"Discover the hidden rule ({r_en}) across all three given rows.",
            [f"Testing Rows 1–3 shows every Input uses ({sym}) to produce its Output.", f"For Input {m(inp)}, applying ({sym}) gives {m(ans)}."],
            f"All four rows satisfy ({sym}) consistently.",
            f"نستنتج القاعدة الخفية ({r_ar}) من الصفوف الثلاثة الأولى.",
            [f"بفحص الصفوف 1–3 نجد أن كل مدخلة تخضع لعملية ({r_ar}).", f"بتطبيقها على {m(inp)} نحصل على {m(ans)}."],
            "القاعدة صحيحة في جميع الصفوف الأربعة.",
            diagram_en=svg_nafes_function_table(["Input", "Output"], rows, highlight_cell=(3, 1)),
        ))

    # Hard (5): Working backward for missing Input + two-step function machines
    hard_specs = [
        ("table_in", "In the input-output table shown, every row multiplies the Input by \\( 9 \\). What **Input** number replaces \\( ? \\) to give Output \\( 72 \\)?",
         "في جدول المدخلات والمخرجات تضرب الآلة كل مدخلة في \\( 9 \\). ما **المدخلة** التي تحل محل \\( ? \\) لتعطي المخرجة \\( 72 \\)؟",
         8, [7, 9, 63], svg_nafes_function_table(["Input", "Output"], [[3, 27], [6, 54], ["?", 72]], highlight_cell=(2, 0))),
        ("table_in", "Every row in the table adds \\( 19 \\) to the Input. What **Input** number replaces \\( ? \\) when the Output is \\( 53 \\)?",
         "في الجدول الموضح تضيف القاعدة \\( 19 \\) إلى كل مدخلة. ما قيمة **المدخلة** مكان \\( ? \\) عندما تكون المخرجة \\( 53 \\)؟",
         34, [32, 36, 72], svg_nafes_function_table(["Input", "Output"], [[10, 29], [25, 44], ["?", 53]], highlight_cell=(2, 0))),
        ("machine", "A two-step number machine takes Input \\( 6 \\), first **multiplies by \\( 4 \\)**, and then **adds \\( 5 \\)**. What Output comes out?",
         "تأخذ آلة الأعداد المدخلة \\( 6 \\)، فتضربها أولاً **في \\( 4 \\)** ثم **تجمع \\( 5 \\)**. ما عدد المخرجة النهائية؟",
         29, [24, 34, 54], svg_function_machine("6", "x 4", "+ 5", "?")),
        ("machine", "A two-step number machine takes Input \\( 9 \\), first **multiplies by \\( 3 \\)**, and then **subtracts \\( 7 \\)**. What Output comes out?",
         "تأخذ آلة الأعداد المدخلة \\( 9 \\)، فتضربها أولاً **في \\( 3 \\)** ثم **تطرح \\( 7 \\)**. ما عدد المخرجة النهائية؟",
         20, [18, 27, 34], svg_function_machine("9", "x 3", "- 7", "?")),
        ("table_in", "In the table shown, every row divides the Input by \\( 5 \\). What **Input** number replaces \\( ? \\) so that its Output is \\( 8 \\)?",
         "في الجدول الموضح تقسم القاعدة كل مدخلة على \\( 5 \\). ما **المدخلة** مكان \\( ? \\) لتكون المخرجة \\( 8 \\)؟",
         40, [13, 35, 45], svg_nafes_function_table(["Input", "Output"], [[15, 3], [30, 6], ["?", 8]], highlight_cell=(2, 0))),
    ]
    for kind, q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Use the inverse operation when working backward for an Input, or follow the two machine boxes in exact left-to-right order!",
            "استعمل العملية العكسية لإيجاد المدخلة، أو نفّذ صندوقي الآلة بالترتيب من اليسار إلى اليمين!",
            "Work step-by-step through the machine or invert the rule to recover the Input.",
            ["Identify the exact operation(s) linking Input and Output.", f"Computing carefully yields {m(ans)}."],
            f"Plugging {m(ans)} forward into the rule reproduces the exact Output.",
            "نتتبّع خطوتي الآلة بالترتيب أو نستعمل العملية العكسية لإيجاد المدخلة.",
            ["نحدّد العملية الرابطة بين المدخلة والمخرجة بدقة.", f"نحسب الناتج فنجد {m(ans)}."],
            f"تعويض {m(ans)} في القاعدة يعطي المخرجة الصحيحة تماماً.",
            diagram_en=diag,
        ))
    return out


def _gen_g3_alg_04(next_id) -> list[dict]:
    """G3-ALG-04: Missing-number equations & visual toy balance scales."""
    tp, bp = "Algebra", "G3-ALG-04"
    out = []

    # Easy (5): One-step missing-number sentences on balance pans
    easy_specs = [
        ("\\square + 18 = 45", "[ ] + 18", "45", 27, [23, 37, 63], "45 - 18 = 27"),
        ("52 - \\square = 19", "52 - [ ]", "19", 33, [31, 43, 71], "52 - 19 = 33"),
        ("7 \\times \\square = 49", "7 x [ ]", "49", 7, [6, 8, 42], "49 \\div 7 = 7"),
        ("\\square \\div 6 = 8", "[ ] ÷ 6", "8", 48, [14, 42, 54], "8 \\times 6 = 48"),
        ("9 \\times \\square = 72", "9 x [ ]", "72", 8, [7, 9, 63], "72 \\div 9 = 8"),
    ]
    for eq_tex, l_pan, r_pan, ans, dists, inv_tex in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"Find the missing number {m('\\square')} that keeps the equation balanced: {m(eq_tex)}.",
            f"أوجد العدد المفقود {m('\\square')} الذي يجعل الجملة العددية متوازنة: {m(eq_tex)}.",
            ans, dists,
            "Use the inverse operation to isolate the missing box!",
            "استعمل العملية العكسية لإيجاد العدد داخل المربع!",
            "Use inverse arithmetic so both sides equal the same value.",
            [f"Start from {m(eq_tex)}.", f"Compute {m(inv_tex)}, so {m(f'\\square = {ans}')}."],
            f"Substituting {m(ans)} back into {m(eq_tex)} makes both sides equal.",
            "نستعمل العملية العكسية لتتساوى كفتا الجملة العددية.",
            [f"ننطلق من الجملة {m(eq_tex)}.", f"نحسب {m(inv_tex)} فيكون {m(f'\\square = {ans}')}."],
            f"تعويض {m(ans)} يجعل الطرفين متساويين.",
            diagram_en=svg_g3_equation_balance(l_pan, r_pan, "Equal sides"),
        ))

    # Medium (5): Two-side balanced equations (a + b = □ + c, a × b = □ × c)
    med_specs = [
        ("26 + 19 = \\square + 20", "26 + 19", "[ ] + 20", 25, [24, 26, 45], "45"),
        ("6 \\times 4 = 3 \\times \\square", "6 x 4", "3 x [ ]", 8, [6, 7, 24], "24"),
        ("50 - 14 = \\square + 16", "50 - 14", "[ ] + 16", 20, [18, 22, 36], "36"),
        ("8 \\times 3 = 6 \\times \\square", "8 x 3", "6 x [ ]", 4, [3, 5, 24], "24"),
        ("37 + 18 = 40 + \\square", "37 + 18", "40 + [ ]", 15, [13, 17, 55], "55"),
    ]
    for eq_tex, l_pan, r_pan, ans, dists, side_val in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            f"Both sides of {m(eq_tex)} have the **same value**. What number belongs in {m('\\square')}?",
            f"طرفا الجملة العددية {m(eq_tex)} متساويان في القيمة. ما العدد الذي يوضع في {m('\\square')}؟",
            ans, dists,
            "First calculate the complete side that has no missing box!",
            "احسب قيمة الطرف المعلوم بالكامل أولاً ثم أوجد العدد المفقود في الطرف الآخر!",
            f"Evaluate the known side ({m(side_val)}) first, then solve for {m('\\square')}.",
            [f"The known left side equals {m(side_val)}.", f"Match the right side to {m(side_val)} to get {m(f'\\square = {ans}')}."],
            f"Both pans equal {m(side_val)} when {m(f'\\square = {ans}')}.",
            f"نحسب قيمة الطرف المعلوم ({m(side_val)}) أولاً ثم نوجد قيمة {m('\\square')}.",
            [f"قيمة الطرف الأيسر المعلوم تساوي {m(side_val)}.", f"بمساواة الطرف الأيمن بالقيمة {m(side_val)} نجد {m(f'\\square = {ans}')}."],
            f"تتساوى الكفتان عند القيمة {m(side_val)}.",
            diagram_en=svg_g3_equation_balance(l_pan, r_pan, f"Both sides = {side_val}"),
        ))

    # Hard (5): Visual toy balance scales (shape substitution & multi-block pans)
    hard_specs = [
        ("Look at the two balanced toy scales: on Scale 1, **1 orange ball** balances **2 green cubes**; on Scale 2, **1 green cube** balances **3 purple pyramids**. How many **purple pyramids** balance **1 orange ball**?",
         "انظر إلى ميزاني الألعاب المتعادلين: في الميزان 1 تتعادل **كرة برتقالية واحدة** مع **مكعبين أخضرين**، وفي الميزان 2 يتعادل **مكعب أخضر واحد** مع **3 أهرامات بنفسجية**. كم **هرماً بنفسجياً** يعادل **كرة برتقالية واحدة**؟",
         6, [3, 5, 8], svg_balance_scales(1, 2, 1, 3)),
        ("On Scale 1, **1 orange ball** balances **3 green cubes**; on Scale 2, **1 green cube** balances **2 purple pyramids**. How many **purple pyramids** balance **2 orange balls**?",
         "في الميزان 1 تتعادل **كرة برتقالية واحدة** مع **3 مكعبات خضراء**، وفي الميزان 2 يتعادل **مكعب أخضر واحد** مع **هرمين بنفسجيين**. كم **هرماً بنفسجياً** يعادل **كرتين برتقاليتين**؟",
         12, [6, 8, 10], svg_balance_scales(1, 3, 1, 2)),
        ("A classroom scale is balanced: the left pan holds **3 identical mystery blocks plus a \\( 6 \\) g weight**, and the right pan holds **\\( 27 \\) g**. How many grams does **1 mystery block** weigh?",
         "ميزان الصف متعادل: الكفة اليسرى عليها **3 مكعبات متماثلة مع ثقل \\( 6 \\) جم**، والكفة اليمنى عليها **\\( 27 \\) جم**. كم جراماً كتلة **المكعب الواحد**؟",
         7, [6, 8, 9], svg_g3_equation_balance("3 x [ ] + 6", "27", "Remove 6 g from both pans first")),
        ("A balanced scale has **4 identical gift boxes plus \\( 5 \\) g** on the left pan and **\\( 37 \\) g** on the right pan. What is the mass in grams of **1 gift box**?",
         "على الكفة اليسرى لميزان متعادل **4 علب متماثلة مع ثقل \\( 5 \\) جم**، وعلى الكفة اليمنى **\\( 37 \\) جم**. ما كتلة **العلبة الواحدة** بالجرام؟",
         8, [7, 9, 32], svg_g3_equation_balance("4 x [ ] + 5", "37", "Balanced pans")),
        ("On Scale 1, **2 orange balls** balance **4 green cubes**; on Scale 2, **1 green cube** balances **2 purple pyramids**. How many **purple pyramids** balance **1 orange ball**?",
         "في الميزان 1 تتعادل **كرتان برتقاليتان** مع **4 مكعبات خضراء**، وفي الميزان 2 يتعادل **مكعب أخضر واحد** مع **هرمين بنفسجيين**. كم **هرماً بنفسجياً** يعادل **كرة برتقالية واحدة**؟",
         4, [2, 6, 8], svg_balance_scales(2, 4, 1, 2)),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Trade equal weights step-by-step (or take away the extra gram weight from both pans first, then divide equally)!",
            "استبدل الأوزان المتساوية خطوةً بخطوة (أو ارفع الثقل الإضافي من الكفتين معاً ثم اقسم بالتساوي)!",
            "Keep the scale balanced by removing equal weights or substituting equal shapes.",
            ["Simplify one step on the balanced pans first.", f"Dividing or substituting equally gives {m(ans)}."],
            f"Testing {m(ans)} keeps both sides of the scale in exact balance.",
            "نحافظ على توازن الميزان بحذف الأثقال المتساوية أو استبدال القطع المتكافئة.",
            ["نبسّط العلاقة على كفتي الميزان أولاً.", f"بالقسمة أو الاستبدال المتساوي نجد الناتج {m(ans)}."],
            f"التعويض بالقيمة {m(ans)} يبقي الميزان متعادلاً تماماً.",
            diagram_en=diag,
        ))
    return out



# ==============================================================================
# Topic 3: Geometry & Measurement (G3-GEO-01 .. G3-GEO-08)
# ==============================================================================


def _gen_g3_geo_01(next_id) -> list[dict]:
    """G3-GEO-01: Reading analog clocks to 5-minute & 1-minute marks."""
    tp, bp = "Geometry", "G3-GEO-01"
    out = []

    # Easy (5): First-half-hour 5-minute marks
    easy_specs = [
        ("morning assembly", "الطابور الصباحي", 7, 15, [("7:15", "7:15"), ("3:07", "3:07"), ("7:03", "7:03"), ("8:15", "8:15")]),
        ("math lesson", "حصة الرياضيات", 9, 30, [("9:30", "9:30"), ("6:45", "6:45"), ("9:06", "9:06"), ("10:30", "10:30")]),
        ("art break", "استراحة الرسم", 10, 20, [("10:20", "10:20"), ("4:50", "4:50"), ("10:04", "10:04"), ("11:20", "11:20")]),
        ("library time", "وقت المكتبة", 11, 5, [("11:05", "11:05"), ("1:55", "1:55"), ("11:01", "11:01"), ("12:05", "12:05")]),
        ("lunch bell", "جرس الغداء", 1, 25, [("1:25", "1:25"), ("5:05", "5:05"), ("1:05", "1:05"), ("2:25", "2:25")]),
    ]
    for ctx_en, ctx_ar, hr, mn, pairs in easy_specs:
        num_on_dial = mn // 5
        out.append(_make_bilingual_q(
            next_id(), tp, "Easy", bp,
            f"The analog clock shows the time for {ctx_en}. What time does the clock display?",
            f"تُظهر الساعة ذات العقارب وقت {ctx_ar}. كم تشير الساعة في الشكل؟",
            pairs, 0,
            "Read the short red hour hand first, then skip-count by 5s to the long blue minute hand!",
            "اقرأ عقرب الساعات القصير أولاً، ثم عدّ بالخمسات حتى عقرب الدقائق الطويل!",
            f"Short hand is past {m(hr)}; long hand points to {m(num_on_dial)} ({m(f'{num_on_dial} \\times 5 = {mn}')} min).",
            [f"Hour hand shows hour {m(hr)}.", f"Minute hand at {m(num_on_dial)} gives {m(mn)} minutes -> **{pairs[0][0]}**."],
            "Hour and minute hands never swap roles!",
            f"العقرب القصير يدل على الساعة {m(hr)} والطويل عند {m(num_on_dial)} أي {m(mn)} دقيقة.",
            [f"الساعة هي {m(hr)}.", f"الدقائق {m(f'{num_on_dial} \\times 5 = {mn}')}، إذن الوقت **{pairs[0][1]}**."],
            "تأكّدنا من التمييز بين عقرب الساعات القصير وعقرب الدقائق الطويل.",
            svg_nafes_analog_clock(hr, mn),
        ))

    # Medium (5): Late-hour 5-minute marks (:35, :40, :45, :50, :55)
    med_specs = [
        ("homework club", "نادي الواجبات", 3, 40, [("3:40", "3:40"), ("4:40", "4:40"), ("8:20", "8:20"), ("3:08", "3:08")]),
        ("swimming practice", "تدريب السباحة", 5, 50, [("5:50", "5:50"), ("6:50", "6:50"), ("10:30", "10:30"), ("5:10", "5:10")]),
        ("Quran recitation circle", "حلقة تحفيظ القرآن", 4, 35, [("4:35", "4:35"), ("5:35", "5:35"), ("7:20", "7:20"), ("4:07", "4:07")]),
        ("family tea", "جلسة الشاي العائلية", 6, 55, [("6:55", "6:55"), ("7:55", "7:55"), ("11:35", "11:35"), ("6:11", "6:11")]),
        ("museum tour", "جولة المتحف", 8, 45, [("8:45", "8:45"), ("9:45", "9:45"), ("9:40", "9:40"), ("8:09", "8:09")]),
    ]
    for ctx_en, ctx_ar, hr, mn, pairs in med_specs:
        nxt_hr = 12 if hr == 11 else (1 if hr == 12 else hr + 1)
        dial_n = mn // 5
        out.append(_make_bilingual_q(
            next_id(), tp, "Medium", bp,
            f"Look carefully at the clock for {ctx_en}, where the short hour hand lies between {m(hr)} and {m(nxt_hr)}. What time is shown?",
            f"انظر بدقة إلى ساعة {ctx_ar} حيث يقع عقرب الساعات القصير بين {m(hr)} و{m(nxt_hr)}. كم تشير الساعة؟",
            pairs, 0,
            f"Even though the short hand is close to {m(nxt_hr)}, it has NOT reached {m(nxt_hr)} yet!",
            f"رغم اقتراب العقرب القصير من {m(nxt_hr)} فإنه لم يصل إليها بعد؛ تبقى الساعة {m(hr)}!",
            f"The hour is still {m(hr)}, and the minute hand on {m(dial_n)} means {m(mn)} minutes.",
            [f"Between {m(hr)} and {m(nxt_hr)} means the hour is still {m(hr)}.", f"Minute hand at {m(dial_n)} gives {m(f'{dial_n} \\times 5 = {mn}')} -> **{pairs[0][0]}**."],
            f"In {m(60 - mn)} minutes it will reach {nxt_hr}:00.",
            f"الساعة لا تزال {m(hr)} وعقرب الدقائق عند {m(dial_n)} يعطي {m(mn)} دقيقة.",
            [f"وقوع العقرب بين {m(hr)} و{m(nxt_hr)} يعني الساعة {m(hr)}.", f"الدقائق = {m(f'{dial_n} \\times 5 = {mn}')}، فالوقت **{pairs[0][1]}**."],
            f"بعد {m(60 - mn)} دقائق ستصل الساعة إلى {nxt_hr}:00.",
            svg_nafes_analog_clock(hr, mn),
        ))

    # Hard (5): Exact 1-minute marks
    hard_specs = [
        (2, 17, 3, 2, [("2:17", "2:17"), ("2:15", "2:15"), ("3:12", "3:12"), ("2:22", "2:22")]),
        (6, 23, 4, 3, [("6:23", "6:23"), ("6:20", "6:20"), ("4:32", "4:32"), ("6:28", "6:28")]),
        (8, 38, 7, 3, [("8:38", "8:38"), ("9:38", "9:38"), ("8:35", "8:35"), ("7:43", "7:43")]),
        (10, 42, 8, 2, [("10:42", "10:42"), ("11:42", "11:42"), ("10:40", "10:40"), ("8:52", "8:52")]),
        (11, 54, 10, 4, [("11:54", "11:54"), ("12:54", "12:54"), ("11:50", "11:50"), ("10:59", "10:59")]),
    ]
    for hr, mn, d_num, extra_ticks, pairs in hard_specs:
        base_m = d_num * 5
        out.append(_make_bilingual_q(
            next_id(), tp, "Hard", bp,
            f"On this precision classroom clock, the minute hand has passed the {m(d_num)} mark by **{m(extra_ticks)} small minute ticks**. What exact time does the clock show?",
            f"على ساعة الصف الدقيقة تجاوز عقرب الدقائق الرقم {m(d_num)} بمقدار **{m(extra_ticks)} شرطات صغيرة**. ما الوقت الدقيق الذي تعرضه الساعة؟",
            pairs, 0,
            f"Skip-count by 5s up to {m(d_num)} ({m(base_m)} minutes), then count on {m(extra_ticks)} single minutes!",
            f"عدّ بالخمسات حتى الرقم {m(d_num)} ({m(base_m)} دقيقة) ثم أضف {m(extra_ticks)} دقائق مفردة!",
            f"Add {m(extra_ticks)} single-minute ticks to {m(base_m)} minutes.",
            [f"Hour = {m(hr)} (the hour hand has not reached the next hour).", f"Minutes = {m(f'{base_m} + {extra_ticks} = {mn}')} -> **{pairs[0][0]}**."],
            f"{m(f'{d_num} \\times 5 + {extra_ticks} = {mn}')} minutes past {m(hr)}.",
            f"نضرب {m(d_num)} في 5 ثم نضيف {m(extra_ticks)} دقائق مفردة.",
            [f"الساعة الصغرى هي {m(hr)}.", f"الدقائق = {m(f'{base_m} + {extra_ticks} = {mn}')}، أي الوقت **{pairs[0][1]}**."],
            f"التحقق: {m(f'{base_m} + {extra_ticks} = {mn}')} دقيقة.",
            svg_nafes_analog_clock(hr, mn),
        ))
    return out


def _gen_g3_geo_02(next_id) -> list[dict]:
    """G3-GEO-02: Elapsed time, start/finish times & calendar weeks/days."""
    tp, bp = "Geometry", "G3-GEO-02"
    out = []

    # Easy (5): Same-hour elapsed minutes & calendar weeks/days
    easy_specs = [
        ("Art class starts at 9:10 AM and ends at 9:50 AM. How many minutes long is art class?",
         "تبدأ حصة التربية الفنية الساعة 9:10 صباحاً وتنتهي الساعة 9:50 صباحاً. كم دقيقة مدة الحصة؟",
         40, [30, 45, 60], svg_nafes_analog_clock(9, 10, "Starts 9:10 -> Ends 9:50")),
        ("Saleh's family visits Abha for \\( 3 \\) full weeks. How many **days** is \\( 3 \\) weeks?",
         "تقضي أسرة صالح إجازة في أبها لمدة \\( 3 \\) أسابيع كاملة. كم **يوماً** تساوي \\( 3 \\) أسابيع؟",
         21, [14, 18, 28], svg_nafes_function_table(["Weeks", "Days"], [[1, 7], [2, 14], [3, "?"]], highlight_cell=(2, 1))),
        ("Reading club begins at 10:15 AM and finishes at 10:45 AM. How many minutes does reading club last?",
         "يبدأ نادي القراءة الساعة 10:15 صباحاً وينتهي الساعة 10:45 صباحاً. كم دقيقة يستمر النادي؟",
         30, [25, 35, 60], svg_nafes_analog_clock(10, 15, "10:15 to 10:45")),
        ("A school science project lasts \\( 2 \\) weeks and \\( 4 \\) days. How many **days** is that altogether?",
         "يستمر مشروع العلوم المدرسي لمدة أسبوعين و\\( 4 \\) أيام. كم **يوماً** مدة المشروع كلها؟",
         18, [11, 14, 24], svg_nafes_function_table(["Part", "Days"], [["2 weeks", 14], ["Extra days", 4], ["Total", "?"]], highlight_cell=(2, 1))),
        ("A cartoon movie starts at 4:05 PM and ends at 4:55 PM. How many minutes did the movie run?",
         "يبدأ فلم كرتوني الساعة 4:05 عصراً وينتهي الساعة 4:55 عصراً. كم دقيقة استغرق الفلم؟",
         50, [40, 45, 55], svg_digital_clock("04:55", "Started at 04:05")),
    ]
    for q_en, q_ar, ans, dists, diag in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "Remember: 1 hour = 60 minutes, and 1 week = 7 days!",
            "تذكّر: الساعة الواحدة = 60 دقيقة، والأسبوع الواحد = 7 أيام!",
            "Subtract start minutes from finish minutes, or multiply weeks by 7.",
            ["Use 1 week = 7 days or subtract minutes within the same hour.", f"Result = {m(ans)}."],
            f"Counting forward confirms {m(ans)}.",
            "نطرح دقائق البداية من النهاية في الساعة نفسها، أو نضرب عدد الأسابيع في 7.",
            ["نطبّق العلاقة المباشرة للوقت أو الأيام.", f"الناتج يساوي {m(ans)}."],
            f"التحقق بالعد التصاعدي يؤكد {m(ans)}.",
            diagram_en=diag,
        ))

    # Medium (5): Crossing the hour mark (elapsed minutes & finish time)
    med_specs = [
        ("num", "Faisal boarded the Riyadh Metro at 4:35 PM and stepped off at 5:15 PM. How many **minutes** did his ride take?",
         "ركب فيصل قطار الرياض الساعة 4:35 عصراً ونزل الساعة 5:15 عصراً. كم **دقيقة** استغرقت رحلته؟",
         40, [20, 50, 80], svg_g3_number_line([(0, "4:35"), (25, "5:00"), (40, "5:15")], arc=(0, 25, "+25m"), mark_pos=40, mark_lbl="+15m", lo=0, hi=40)),
        ("num", "Mother put a cake in the oven at 6:45 PM and took it out at 7:20 PM. How many **minutes** did the cake bake?",
         "وضعت الأم الكعكة في الفرن الساعة 6:45 مساءً وأخرجتها الساعة 7:20 مساءً. كم **دقيقة** استغرق خبز الكعكة؟",
         35, [25, 45, 75], svg_g3_number_line([(0, "6:45"), (15, "7:00"), (35, "7:20")], arc=(0, 15, "+15m"), mark_pos=35, mark_lbl="+20m", lo=0, hi=35)),
        ("time", "Football practice starts at 3:40 PM and lasts \\( 35 \\) minutes. At what time does football practice end?",
         "يبدأ تدريب كرة القدم الساعة 3:40 عصراً ويستمر \\( 35 \\) دقيقة. متى ينتهي التدريب؟",
         [("4:15 PM", "4:15 عصراً"), ("4:05 PM", "4:05 عصراً"), ("3:75 PM", "3:75 عصراً"), ("4:25 PM", "4:25 عصراً")],
         svg_nafes_analog_clock(3, 40, "Start: 3:40 + 35 min")),
        ("time", "Heba starts painting at 1:50 PM and paints for \\( 40 \\) minutes. At what time does she finish?",
         "بدأت هبة التلوين الساعة 1:50 ظهراً واستمرت \\( 40 \\) دقيقة. في أي ساعة انتهت؟",
         [("2:30 PM", "2:30 ظهراً"), ("2:20 PM", "2:20 ظهراً"), ("2:40 PM", "2:40 ظهراً"), ("1:90 PM", "1:90 ظهراً")],
         svg_nafes_analog_clock(1, 50, "Start: 1:50 + 40 min")),
        ("num", "The school bus left at 6:50 AM and arrived at school at 7:25 AM. How many **minutes** was the bus trip?",
         "انطلقت الحافلة المدرسية الساعة 6:50 صباحاً ووصلت إلى المدرسة الساعة 7:25 صباحاً. كم **دقيقة** استغرقت الرحلة؟",
         35, [25, 45, 75], svg_g3_number_line([(0, "6:50"), (10, "7:00"), (35, "7:25")], arc=(0, 10, "+10m"), mark_pos=35, mark_lbl="+25m", lo=0, hi=35)),
    ]
    for item in med_specs:
        if item[0] == "num":
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Medium", bp,
                q_en, q_ar, ans, dists,
                "Hop to the whole o'clock hour first (60 minutes per hour!), then add the remaining minutes.",
                "اقفز أولاً إلى تمام الساعة التالية (تذكّر أن الساعة 60 دقيقة!) ثم أضف الدقائق المتبقية.",
                "Bridge across the whole hour mark.",
                ["Count minutes up to the next whole hour.", f"Add the minutes past the hour to get {m(ans)} minutes."],
                f"Never subtract clock numbers as base-100; {m(ans)} minutes is exact.",
                "نجزّئ الزمن عبر تمام الساعة الكاملة.",
                ["نحسب الدقائق حتى تمام الساعة التالية.", f"نضيف الدقائق بعد الساعة فنحصل على {m(ans)} دقيقة."],
                f"مجموع القفزتين يساوي {m(ans)} دقيقة.",
                diagram_en=diag,
            ))
        else:
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Medium", bp,
                q_en, q_ar, pairs, 0,
                "Add enough minutes to reach the next o'clock hour first, then add the rest!",
                "أضف ما يكمل الساعة التالية أولاً، ثم أضف بقية الدقائق!",
                "Bridge forward across the whole hour.",
                ["Use part of the minutes to reach the next whole hour.", f"Add the leftover minutes to land on **{pairs[0][0]}**."],
                "Counting backward from the finish time returns to the start time.",
                "نتقدم أولاً إلى تمام الساعة التالية ثم نضيف الدقائق المتبقية.",
                ["نكمّل الدقائق إلى الساعة التالية أولاً.", f"نضيف الباقي فنصل إلى **{pairs[0][1]}**."],
                "العد التنازلي من وقت النهاية يعيدنا إلى وقت البداية.",
                diag,
            ))

    # Hard (5): Working backward for start time, two-part durations & calendar dates
    hard_specs = [
        ("time", "Adel arrived at school at **7:15 AM** after a **\\( 35 \\)-minute** walk and ride. At what time did Adel leave home?",
         "وصل عادل إلى المدرسة الساعة **7:15 صباحاً** بعد رحلة استغرقت **\\( 35 \\) دقيقة**. في أي ساعة غادر عادل منزله؟",
         [("6:40 AM", "6:40 صباحاً"), ("6:45 AM", "6:45 صباحاً"), ("6:35 AM", "6:35 صباحاً"), ("7:50 AM", "7:50 صباحاً")],
         svg_digital_clock("07:15", "Arrived after 35 min")),
        ("time", "Reem finished her homework at **5:20 PM**. She spent **\\( 25 \\) minutes** on math and **\\( 20 \\) minutes** on Arabic. At what time did Reem **start** her homework?",
         "أنهت ريم واجباتها الساعة **5:20 عصراً** بعد أن قضت **\\( 25 \\) دقيقة** في الرياضيات و**\\( 20 \\) دقيقة** في لغتي. متى **بدأت** ريم واجباتها؟",
         [("4:35 PM", "4:35 عصراً"), ("4:45 PM", "4:45 عصراً"), ("4:25 PM", "4:25 عصراً"), ("5:05 PM", "5:05 عصراً")],
         svg_digital_clock("05:20", "Finished after 25m + 20m")),
        ("num", "Today is **4 Shawwal**. The Grade 3 field trip is scheduled **\\( 2 \\) weeks and \\( 5 \\) days** after today. On what day number of Shawwal is the field trip?",
         "اليوم هو **4 شوال**. ستُقام رحلة الصف الثالث بعد **أسبوعين و\\( 5 \\) أيام** من اليوم. في أي يوم من شهر شوال ستقام الرحلة؟",
         23, [18, 21, 25], svg_nafes_function_table(["Item", "Days"], [["Start date", 4], ["2 weeks", 14], ["Extra days", 5], ["Trip date", "?"]], highlight_cell=(3, 1))),
        ("num", "Mansour read for \\( 25 \\) minutes, rested for \\( 10 \\) minutes, and then solved puzzles for \\( 35 \\) minutes. How many **minutes** did all three activities take in total?",
         "قرأ منصور لمدة \\( 25 \\) دقيقة، ثم استراح \\( 10 \\) دقائق، ثم حل ألغازاً لمدة \\( 35 \\) دقيقة. كم **دقيقة** استغرقت الأنشطة الثلاثة معاً؟",
         70, [60, 65, 80], svg_number_strip(["25 min", "+ 10 min", "+ 35 min", "= ?"])),
        ("num", "A train journey lasts **\\( 1 \\) hour and \\( 25 \\) minutes**. How many **minutes** is the entire train journey?",
         "تستغرق رحلة القطار **ساعة واحدة و\\( 25 \\) دقيقة**. كم **دقيقة** تبلغ مدة الرحلة كاملة؟",
         85, [65, 75, 125], svg_nafes_function_table(["Part", "Minutes"], [["1 hour", 60], ["Extra", 25], ["Total", "?"]], highlight_cell=(2, 1))),
    ]
    for item in hard_specs:
        if item[0] == "time":
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Hard", bp,
                q_en, q_ar, pairs, 0,
                "Count backward to the whole hour first, then subtract the remaining minutes from 60!",
                "ارجع بالزمن إلى تمام الساعة أولاً ثم اطرح الدقائق المتبقية من 60!",
                "Work backward across the o'clock boundary.",
                ["Step back to the whole hour first.", f"Step back the remaining minutes to get **{pairs[0][0]}**."],
                "Adding the elapsed duration forward lands right back on the finish time.",
                "نعود بالزمن إلى الخلف عبر تمام الساعة.",
                ["نطرح الدقائق بعد تمام الساعة أولاً.", f"نطرح الباقي من 60 فنصل إلى **{pairs[0][1]}**."],
                "جمع المدة مع وقت البداية يعيدنا إلى وقت النهاية.",
                diag,
            ))
        else:
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Hard", bp,
                q_en, q_ar, ans, dists,
                "Convert hours or weeks first (1 hr = 60 min, 1 week = 7 days), then add all parts!",
                "حوّل الساعات أو الأسابيع أولاً (1 ساعة = 60 دقيقة، 1 أسبوع = 7 أيام) ثم اجمع الأجزاء!",
                "Convert units cleanly before summing.",
                ["Convert the larger time unit (hour or weeks) into minutes or days.", f"Sum all parts to obtain {m(ans)}."],
                f"Re-checking each part confirms {m(ans)}.",
                "نوحّد وحدة الزمن أولاً ثم نجمع جميع الأجزاء.",
                ["نحوّل الوحدة الكبرى إلى دقائق أو أيام.", f"بجمع المقادير نحصل على {m(ans)}."],
                f"مراجعة الخطوات تؤكد أن الناتج {m(ans)}.",
                diagram_en=diag,
            ))
    return out



def _gen_g3_geo_03(next_id) -> list[dict]:
    """G3-GEO-03: Counting Saudi Riyal (SAR) bills & coins, shopping totals & exact change."""
    tp, bp = "Geometry", "G3-GEO-03"
    out = []

    # Easy (5): Counting Saudi Riyal bills & coins
    easy_specs = [
        ("Amjad", "أمجد", [50, 20, 5, 2, 1]),
        ("Reemas", "ريماس", [100, 50, 10, 5, 2]),
        ("Qusai", "قصي", [20, 20, 10, 5, 2, 2]),
        ("Lujain", "لجين", [500, 100, 20, 10, 5]),
        ("Meshari", "مشاري", [50, 10, 10, 5, 2, 1, 1]),
    ]
    for nm_en, nm_ar, money in easy_specs:
        ans = sum(money)
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            f"{nm_en} counts the Saudi Riyal bills and coins in the wallet shown below. How many Riyals (SAR) does {nm_en} have in total?",
            f"يعدّ/تعدّ {nm_ar} الأوراق النقدية والعملات المعدنية بالريال السعودي الموضحة أدناه. كم ريالاً في المحفظة إجمالاً؟",
            ans, [ans - 5, ans + 5, ans + 10],
            "Add from the largest banknote down to the 2 SAR and 1 SAR coins.",
            "ابدأ بجمع الفئة الورقية الأكبر نزولاً حتى عملتي 2 ريال و1 ريال.",
            "Sum the Saudi Riyal bills and coins from largest to smallest.",
            [f"Values shown: {m(' + '.join(str(x) for x in money))}.", f"Total = {m(ans)} SAR."],
            f"Recounting coins first then bills also gives {m(ans)} SAR.",
            "نجمع الفئات تنازلياً من الأكبر إلى الأصغر.",
            [f"القيم المعروضة: {m(' + '.join(str(x) for x in money))}.", f"المجموع الكلي = {m(ans)} ريالاً."],
            f"إعادة العد تؤكد أن المبلغ {m(ans)} ريالاً.",
            diagram_en=svg_nafes_sar_money(money, "Count the total SAR"),
        ))

    # Medium (5): Shopping totals & exact change
    med_specs = [
        ("Layla buys a storybook for \\( 24 \\) SAR and colored pencils for \\( 18 \\) SAR, paying with a \\( 50 \\) SAR bill. How many Riyals should she get in change?",
         "اشترت ليلى قصة بسعر \\( 24 \\) ريالاً وألواناً بسعر \\( 18 \\) ريالاً، ودفعت ورقة من فئة \\( 50 \\) ريالاً. كم ريالاً تستردّ باقياً؟",
         8, [6, 12, 42], [50], "Paid 50 SAR | Cost 24 + 18"),
        ("Badr buys a football for \\( 46 \\) SAR and water bottle for \\( 19 \\) SAR, paying with a \\( 100 \\) SAR bill. How many Riyals of change does he receive?",
         "اشترى بدر كرة قدم بسعر \\( 46 \\) ريالاً وقارورة ماء بسعر \\( 19 \\) ريالاً، ودفع ورقة من فئة \\( 100 \\) ريال. كم ريالاً الباقي؟",
         35, [25, 45, 65], [100], "Paid 100 SAR | Cost 46 + 19"),
        ("Mona buys \\( 3 \\) sandwiches at \\( 9 \\) SAR each and a juice for \\( 6 \\) SAR. How many Riyals does her meal cost altogether?",
         "اشترت منى \\( 3 \\) شطائر بسعر \\( 9 \\) ريالات للشطيرة وعصيراً بسعر \\( 6 \\) ريالات. كم ريالاً ثمن الوجبة كلها؟",
         33, [18, 27, 36], [20, 10, 2, 1], "3 x 9 + 6 SAR"),
        ("Saad pays \\( 200 \\) SAR for a backpack costing \\( 85 \\) SAR and shoes costing \\( 78 \\) SAR. How many Riyals does he get back?",
         "دفع سعد \\( 200 \\) ريال لشراء حقيبة بسعر \\( 85 \\) ريالاً وحذاء بسعر \\( 78 \\) ريالاً. كم ريالاً يستردّ باقياً؟",
         37, [27, 47, 163], [100, 100], "Paid 200 SAR | Cost 85 + 78"),
        ("Hadi has one \\( 50 \\) SAR bill, one \\( 10 \\) SAR bill, and one \\( 5 \\) SAR bill. After buying a board game for \\( 48 \\) SAR, how many Riyals does he have left?",
         "مع هادي ورقة من فئة \\( 50 \\) ريالاً وورقة من فئة \\( 10 \\) ريالات وورقة من فئة \\( 5 \\) ريالات. اشترى لعبة لوحية بسعر \\( 48 \\) ريالاً؛ كم ريالاً بقي معه؟",
         17, [12, 23, 27], [50, 10, 5], "Wallet: 65 SAR | Game: 48 SAR"),
    ]
    for q_en, q_ar, ans, dists, bills, cap in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Combine the item prices (or bills) first, then subtract to find the exact change!",
            "اجمع ثمن المشتريات (أو النقود) أولاً ثم اطرح لإيجاد الباقي بدقة!",
            "Add total cost/money first, then subtract.",
            ["Compute the sum of prices or wallet bills first.", f"Complete the calculation to get {m(ans)} SAR."],
            f"Adding change plus cost matches the amount paid.",
            "نحسب المجموع أولاً ثم نكمل الطرح لإيجاد الباقي.",
            ["نجمع أثمان المشتريات أو فئات النقود أولاً.", f"نحسب المطلوب فنحصل على {m(ans)} ريالاً."],
            "جمع الباقي مع ثمن المشتريات يعطي المبلغ المدفوع تماماً.",
            diagram_en=svg_nafes_sar_money(bills, cap),
        ))

    # Hard (5): Multi-step SAR reasoning (saving gap & unit price from change)
    hard_specs = [
        ("Khalid has the bills shown (\\( 50 + 20 + 5 = 75 \\) SAR) and wants to buy a science kit for \\( 92 \\) SAR. How many **more** Riyals does Khalid need?",
         "مع خالد الأوراق النقدية الموضحة (\\( 50 + 20 + 5 = 75 \\) ريالاً) ويريد شراء حقيبة علوم بسعر \\( 92 \\) ريالاً. كم ريالاً **إضافياً** يحتاج خالد؟",
         17, [15, 23, 27], [50, 20, 5], "Target: 92 SAR"),
        ("Faisal bought \\( 4 \\) identical puzzle books, paid with a \\( 50 \\) SAR bill, and received \\( 14 \\) SAR in change. How many Riyals did **1 puzzle book** cost?",
         "اشترى فيصل \\( 4 \\) دفاتر ألغاز متماثلة ودفع ورقة \\( 50 \\) ريالاً فاستردّ \\( 14 \\) ريالاً باقياً. كم ريالاً سعر **الدفتر الواحد**؟",
         9, [8, 11, 36], [50], "Paid 50 SAR | Change 14 SAR"),
        ("Dalia bought \\( 3 \\) identical paint sets, paid with a \\( 50 \\) SAR bill, and got \\( 26 \\) SAR in change. What was the price in SAR of **1 paint set**?",
         "اشترت داليا \\( 3 \\) علب ألوان متماثلة ودفعت \\( 50 \\) ريالاً فاستردّت \\( 26 \\) ريالاً باقياً. كم ريالاً سعر **العلبة الواحدة**؟",
         8, [7, 9, 24], [50], "Paid 50 SAR | Change 26 SAR"),
        ("Tariq has \\( 100 \\) SAR. He buys \\( 2 \\) tickets at \\( 15 \\) SAR each and \\( 3 \\) snacks at \\( 8 \\) SAR each. How many Riyals does Tariq have left?",
         "مع طارق \\( 100 \\) ريال؛ اشترى تذكرتين بسعر \\( 15 \\) ريالاً للتذكرة و\\( 3 \\) وجبات خفيفة بسعر \\( 8 \\) ريالات للوجبة. كم ريالاً بقي مع طارق؟",
         46, [44, 54, 56], [100], "30 + 24 spent from 100 SAR"),
        ("Sara saved \\( 5 \\) bills of \\( 10 \\) SAR and \\( 6 \\) coins of \\( 2 \\) SAR. After donating \\( 25 \\) SAR, how many Riyals remain in her savings box?",
         "ادّخرت سارة \\( 5 \\) ورقات من فئة \\( 10 \\) ريالات و\\( 6 \\) عملات من فئة \\( 2 \\) ريال، ثم تبرعت بمبلغ \\( 25 \\) ريالاً. كم ريالاً بقي في حصالتها؟",
         37, [27, 47, 62], [10, 10, 10, 10, 10, 2, 2, 2], "5x10 + 6x2 - 25"),
    ]
    for q_en, q_ar, ans, dists, bills, cap in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Work step-by-step: find the total spent or total saved first, then divide or subtract!",
            "حل خطوةً بخطوة: أوجد أولاً المبلغ المصروف أو المدّخر ثم اقسم أو اطرح!",
            "Solve the two-step Saudi Riyal problem systematically.",
            ["Find the intermediate SAR amount (spent or saved).", f"Complete the second step to obtain {m(ans)} SAR."],
            f"Checking the prices and change back against the total confirms {m(ans)} SAR.",
            "ننفّذ المسألة المالية على خطوتين واضحتين.",
            ["نحسب المبلغ الوسيط (المصروف أو المدّخر) أولاً.", f"نكمل الخطوة الثانية فنحصل على {m(ans)} ريالاً."],
            f"مراجعة المشتريات والباقي تؤكد صحة الناتج {m(ans)}.",
            diagram_en=svg_nafes_sar_money(bills, cap),
        ))
    return out


def _gen_g3_geo_04(next_id) -> list[dict]:
    """G3-GEO-04: Metric length (cm, m, km), mass (g, kg) & liquid capacity (mL, L)."""
    tp, bp = "Geometry", "G3-GEO-04"
    out = []

    # Easy (5): Direct metric conversions & unit sense
    easy_specs = [
        ("num", "A classroom whiteboard is \\( 3 \\) meters wide. How many **centimeters** is \\( 3 \\) meters?",
         "عرض سبورة الصف \\( 3 \\) أمتار. كم **سنتيمتراً** يساوي \\( 3 \\) أمتار؟",
         300, [30, 3000, 103], svg_g3_metric_card("length", "3 m = ? cm", "1 m = 100 cm", 0.7)),
        ("num", "A sack of Basmati rice has a mass of \\( 5 \\) kilograms. How many **grams** is \\( 5 \\) kilograms?",
         "كتلة كيس أرز بسمتي \\( 5 \\) كيلوجرامات. كم **جراماً** تساوي \\( 5 \\) كيلوجرامات؟",
         5000, [50, 500, 505], svg_g3_metric_card("mass", "5 kg = ? g", "1 kg = 1,000 g")),
        ("num", "A family water jug holds \\( 4 \\) liters. How many **milliliters** is \\( 4 \\) liters?",
         "تتسع قارورة ماء عائلية لعدد \\( 4 \\) لترات. كم **مللتراً** تساوي \\( 4 \\) لترات؟",
         4000, [40, 400, 1400], svg_g3_metric_card("capacity", "4 L = ? mL", "1 L = 1,000 mL", 0.8)),
        ("unit", "Which metric unit is **most appropriate** to measure the highway distance from Riyadh to Dammam?",
         "ما الوحدة المترية **الأنسب** لقياس المسافة بين مدينتي الرياض والدمام؟",
         [("Kilometer (km)", "الكيلومتر (كم)"), ("Centimeter (cm)", "السنتيمتر (سم)"), ("Gram (g)", "الجرام (جم)"), ("Milliliter (mL)", "المللتر (مل)")],
         svg_g3_metric_card("length", "Riyadh <-> Dammam", "City-to-city distance", 0.95)),
        ("unit", "Which metric unit is **most appropriate** to measure the liquid in a small cough-syrup spoon?",
         "ما الوحدة المترية **الأنسب** لقياس سعة ملعقة دواء صغيرة؟",
         [("Milliliter (mL)", "المللتر (مل)"), ("Liter (L)", "اللتر (ل)"), ("Kilogram (kg)", "الكيلوجرام (كجم)"), ("Meter (m)", "المتر (م)")],
         svg_g3_metric_card("capacity", "Small spoon", "Tiny liquid amount", 0.2)),
    ]
    for item in easy_specs:
        if item[0] == "num":
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Easy", bp,
                q_en, q_ar, ans, dists,
                "Remember: 1 m = 100 cm, while 1 kg = 1,000 g and 1 L = 1,000 mL!",
                "تذكّر: 1 م = 100 سم، بينما 1 كجم = 1,000 جم و1 ل = 1,000 مل!",
                "Multiply by the exact metric conversion factor.",
                ["Recall the conversion factor (100 for cm/m, 1,000 for g/kg and mL/L).", f"Multiply to get {m(ans)}."],
                f"Checking the number of zeros confirms {m(ans)}.",
                "نضرب في معامل التحويل المتري الصحيح.",
                ["نستحضر علاقة التحويل (100 للسنتيمتر، 1,000 للجرام والمللتر).", f"ناتج التحويل هو {m(ans)}."],
                f"مراجعة عدد الأصفار تؤكد {m(ans)}.",
                diagram_en=diag,
            ))
        else:
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Easy", bp,
                q_en, q_ar, pairs, 0,
                "Match length to cm/m/km, mass to g/kg, and liquid capacity to mL/L!",
                "اربط الطول بـ (سم/م/كم)، والكتلة بـ (جم/كجم)، والسعة السائلة بـ (مل/ل)!",
                "Choose the unit that matches both the property (length/mass/capacity) and object scale.",
                ["Check whether we are measuring distance, weight, or liquid volume.", f"Select **{pairs[0][0]}**."],
                "Other options measure either the wrong attribute or a mismatched scale.",
                "نختار الوحدة المناسبة لنوع القياس وحجم الشيء المقاس.",
                ["نحدّد هل نقيس طولاً أم كتلة أم سعة سائلة.", f"الوحدة الأنسب هي **{pairs[0][1]}**."],
                "بقية الخيارات إما لوصف مختلف أو لحجم غير مناسب.",
                diag,
            ))

    # Medium (5): Compound metric conversions
    med_specs = [
        ("A jump rope is \\( 2 \\) meters and \\( 45 \\) centimeters long. How many **centimeters** long is the jump rope in all?",
         "طول حبل قفز \\( 2 \\) متر و\\( 45 \\) سنتيمتراً. كم **سنتيمتراً** طول الحبل كله؟",
         245, [65, 2045, 254], svg_g3_metric_card("length", "2 m 45 cm", "Convert to cm", 0.65)),
        ("A watermelon weighs \\( 3 \\) kilograms and \\( 600 \\) grams. What is its mass in **grams**?",
         "كتلة بطيخة \\( 3 \\) كيلوجرامات و\\( 600 \\) جرام. ما كتلتها **بالجرام**؟",
         3600, [360, 603, 900], svg_g3_metric_card("mass", "3 kg 600 g", "Convert to g")),
        ("A thermos holds \\( 1 \\) liter and \\( 750 \\) milliliters of mint tea. How many **milliliters** is that altogether?",
         "تتسع حافظة شاي لـ \\( 1 \\) لتر و\\( 750 \\) مللتراً. كم **مللتراً** سعتها الإجمالية؟",
         1750, [751, 850, 1075], svg_g3_metric_card("capacity", "1 L 750 mL", "Convert to mL", 0.75)),
        ("A cycling track is \\( 4 \\) kilometers and \\( 300 \\) meters long. How many **meters** long is the track?",
         "طول مضمار دراجات \\( 4 \\) كيلومترات و\\( 300 \\) متر. كم **متراً** طول المضمار؟",
         4300, [430, 700, 3004], svg_g3_metric_card("length", "4 km 300 m", "1 km = 1,000 m", 0.85)),
        ("A box of dates weighs \\( 2 \\) kilograms and \\( 80 \\) grams. What is its total mass in **grams**?",
         "كتلة علبة تمر \\( 2 \\) كيلوجرام و\\( 80 \\) جراماً. كم كتلتها الكلية **بالجرام**؟",
         2080, [280, 2800, 1080], svg_g3_metric_card("mass", "2 kg 80 g", "Watch the placeholder zero!")),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Convert the larger unit first, then add the extra smaller units!",
            "حوّل الوحدة الكبرى أولاً ثم أضف الوحدات الصغرى الإضافية!",
            "Convert the whole meters/kilograms/liters, then add the remaining part.",
            ["Convert the main unit using 1 m = 100 cm or 1,000 for km/kg/L.", f"Add the extra units to obtain {m(ans)}."],
            f"Decomposing {m(ans)} back gives the exact original compound measurement.",
            "نحوّل الوحدة الكبرى أولاً ثم نجمع معها الجزء الأصغر.",
            ["نحوّل الأمتار أو الكيلوجرامات أو اللترات إلى الوحدة الصغرى.", f"نجمع المقدارين فنحصل على {m(ans)}."],
            f"إعادة تفكيك {m(ans)} تطابق المعطيات تماماً.",
            diagram_en=diag,
        ))

    # Hard (5): Multi-step metric subtraction & pouring problems
    hard_specs = [
        ("A \\( 3 \\)-liter cooler is full of water. Students fill \\( 4 \\) bottles of \\( 500 \\) mL each from the cooler. How many **milliliters** of water remain in the cooler?",
         "حافظة ماء سعتها \\( 3 \\) لترات مملوءة بالكامل؛ ملأ الطلاب منها \\( 4 \\) قوارير سعة كل قارورة \\( 500 \\) مل. كم **مللتراً** بقي في الحافظة؟",
         1000, [500, 1500, 2000], svg_two_jars("3 L = 3000 mL", 0.9, "4 x 500 mL", 0.65, "Pour")),
        ("Tailor Hamad has a \\( 2 \\)-meter ribbon. He cuts off one piece of \\( 65 \\) cm and another piece of \\( 50 \\) cm. How many **centimeters** of ribbon are left?",
         "لدى الخياط حمد شريط طوله \\( 2 \\) متر، قصّ منه قطعة طولها \\( 65 \\) سم وقطعة أخرى طولها \\( 50 \\) سم. كم **سنتيمتراً** بقي من الشريط؟",
         85, [75, 95, 115], svg_g3_metric_card("length", "2 m = 200 cm", "Cut 65 cm and 50 cm", 0.55)),
        ("A baker has a \\( 4 \\)-kilogram bag of flour and uses \\( 1350 \\) grams for bread and \\( 900 \\) grams for pies. How many **grams** of flour remain?",
         "لدى خباز كيس دقيق كتلته \\( 4 \\) كجم، استعمل منه \\( 1350 \\) جم للخبز و\\( 900 \\) جم للفطائر. كم **جراماً** بقي في الكيس؟",
         1750, [1650, 2250, 2650], svg_g3_metric_card("mass", "4 kg = 4,000 g", "Used 1,350 g + 900 g")),
        ("Jug A holds \\( 2 \\) liters of milk and Jug B holds \\( 1450 \\) milliliters of milk. By how many **milliliters** does Jug A exceed Jug B?",
         "في الإبريق (أ) \\( 2 \\) لتر من الحليب وفي الإبريق (ب) \\( 1450 \\) مللتراً. بكم **مللتراً** يزيد الإبريق (أ) على الإبريق (ب)؟",
         550, [450, 650, 1448], svg_two_jars("Jug A: 2 L", 0.85, "Jug B: 1450 mL", 0.62, "Compare")),
        ("Ali walks \\( 1 \\) kilometer from home toward the park. After walking \\( 640 \\) meters, how many **meters** does he still have left?",
         "يمشي علي مسافة \\( 1 \\) كيلومتر من بيته إلى الحديقة؛ قطع منها \\( 640 \\) متراً. كم **متراً** بقي عليه ليصل؟",
         360, [260, 440, 460], svg_g3_metric_card("length", "1 km = 1,000 m", "Walked 640 m", 0.64)),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Convert liters/kilograms/meters/kilometers into the smaller unit FIRST so every number shares the same unit!",
            "حوّل الوحدة الكبرى إلى الصغرى أولاً حتى تصبح جميع الأعداد بالوحدة نفسها ثم اطرح!",
            "Convert to common smaller metric units, then subtract what was used.",
            ["Rewrite the starting total in smaller units (cm, m, g, or mL).", f"Subtract the used amount(s) to find {m(ans)} remaining."],
            f"Adding the remaining {m(ans)} back to the used amount restores the exact starting total.",
            "نوحّد الوحدات إلى الوحدة الصغرى أولاً ثم نطرح الكمية المستعملة.",
            ["نحوّل المقدار الكلي إلى الوحدة الصغرى المكافئة.", f"بطرح المستعمل نحصل على الباقي {m(ans)}."],
            f"جمع الباقي {m(ans)} مع المستعمل يعيد المقدار الأصلي.",
            diagram_en=diag,
        ))
    return out



def _gen_g3_geo_05(next_id) -> list[dict]:
    """G3-GEO-05: Perimeter of rectangles, squares & composite grid figures."""
    tp, bp = "Geometry", "G3-GEO-05"
    out = []

    # Easy (5): Perimeter of rectangles & squares
    easy_specs = [
        ("A rectangular bulletin board is \\( 6 \\) cm long and \\( 4 \\) cm wide on a scale drawing. What is its **perimeter** in centimeters?",
         "لوحة إعلانات مستطيلة طولها \\( 6 \\) سم وعرضها \\( 4 \\) سم في الرسم. ما **محيطها** بالسنتيمتر؟",
         6, 4, "cm", 20, [10, 24, 16]),
        ("A square prayer mat tile has each side equal to \\( 5 \\) units on the grid. What is its **perimeter** in units?",
         "بلاطة مربعة طول كل ضلع من أضلاعها \\( 5 \\) وحدات على الشبكة. ما **محيطها** بالوحدات؟",
         5, 5, "units", 20, [10, 25, 15]),
        ("A rectangular flowerbed is \\( 8 \\) m long and \\( 3 \\) m wide. How many meters of fence are needed for its **perimeter**?",
         "حوض زهور مستطيل طوله \\( 8 \\) م وعرضه \\( 3 \\) م. كم متراً من السياج يلزم لإحاطة **محيطه**؟",
         8, 3, "m", 22, [11, 24, 19]),
        ("Each side of a square picture frame measures \\( 7 \\) cm. What is the **perimeter** of the frame in centimeters?",
         "إطار صورة مربع طول ضلعه \\( 7 \\) سم. ما **محيط** الإطار بالسنتيمتر؟",
         7, 7, "cm", 28, [14, 49, 21]),
        ("A school vegetable plot is \\( 9 \\) m long and \\( 4 \\) m wide. What is its **perimeter** in meters?",
         "حوض زراعي مدرسي مستطيل طوله \\( 9 \\) م وعرضه \\( 4 \\) م. ما **محيطه** بالمتر؟",
         9, 4, "m", 26, [13, 36, 22]),
    ]
    for q_en, q_ar, L, W, u_lbl, ans, dists in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "Add ALL FOUR outer sides (Length + Width + Length + Width), not just two sides!",
            "اجمع أطوال الأضلاع الأربعة الخارجية كلها (الطول + العرض + الطول + العرض)!",
            f"Sum all four sides: {m(f'{L} + {W} + {L} + {W}')}.",
            [f"Opposite sides of a rectangle/square are equal ({m(L)} and {m(W)}).", f"Perimeter = {m(f'{L} + {W} + {L} + {W} = {ans}')}."],
            f"{m(f'2 \\times ({L} + {W}) = {ans}')}, whereas area would be {m(L * W)}.",
            f"نجمع الأضلاع الأربعة: {m(f'{L} + {W} + {L} + {W}')}.",
            [f"الأضلاع المتقابلة متطابقة ({m(L)} و{m(W)}).", f"المحيط = {m(f'{L} + {W} + {L} + {W} = {ans}')}."],
            f"تأكّدنا من جمع الأضلاع الأربعة لا ضلعين فقط.",
            diagram_en=svg_g3_grid_rect(L, W, top_lbl=f"{L} {u_lbl}", side_lbl=f"{W} {u_lbl}"),
        ))

    # Medium (5): Perimeter of composite grid figures
    med_specs = [
        ("The shaded plus-shape is made of \\( 5 \\) unit squares of side \\( 1 \\) cm. What is the **perimeter** of the plus-shape in centimeters?",
         "يتكون الشكل المتصالب المظلل من \\( 5 \\) مربعات طول ضلع كل منها \\( 1 \\) سم. ما **محيط** الشكل بالسنتيمتر؟",
         12, [5, 10, 20], svg_polyomino([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], "1 square side = 1 cm")),
        ("Look at the staircase polygon with bottom width \\( 8 \\) cm and left height \\( 6 \\) cm. What is its **perimeter** in centimeters?",
         "انظر إلى الشكل المدرّج الذي قاعدته السفلية \\( 8 \\) سم وارتفاعه الأيسر \\( 6 \\) سم. ما **محيطه** بالسنتيمتر؟",
         28, [14, 24, 48], svg_kang_staircase_perimeter("8 cm", "6 cm", steps=3)),
        ("On a \\( 1 \\)-unit grid, the shaded T-shape covers a top row of \\( 3 \\) squares and a middle stem of \\( 2 \\) squares below it. What is its **perimeter**?",
         "على شبكة وحدتها \\( 1 \\)، يغطي حرف T المظلل صفاً علوياً من \\( 3 \\) مربعات وعموداً أوسط من مربعين أسفله. ما **محيط** الشكل؟",
         12, [5, 10, 14], svg_g3_grid_rect(3, 3, shaded_cells=[(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)], caption="Count outer unit edges")),
        ("On a \\( 1 \\)-meter grid, an L-shaped walkway covers \\( 6 \\) squares inside a \\( 4 \\times 3 \\) frame as shown. What is its **perimeter** in meters?",
         "على شبكة وحدتها \\( 1 \\) م، يغطي ممر على شكل حرف L \\( 6 \\) مربعات كما في الشكل. ما **محيطه** بالمتر؟",
         14, [6, 12, 16], svg_g3_grid_rect(4, 3, shaded_cells=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2)], caption="1 unit = 1 m")),
        ("Four \\( 1 \\) cm unit squares are glued in a single straight row (\\( 4 \\times 1 \\)). What is the **perimeter** of the strip in centimeters?",
         "رُصّت \\( 4 \\) مربعات متطابقة طول ضلع كل منها \\( 1 \\) سم في صف واحد مستقيم (\\( 4 \\times 1 \\)). ما **محيط** الشريط بالسنتيمتر؟",
         10, [4, 8, 16], svg_g3_grid_rect(4, 1, top_lbl="4 cm", side_lbl="1 cm")),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Count ONLY the outer boundary unit segments—never count shared interior lines!",
            "عدّ قطع الإطار الخارجي فقط ولا تحسب الخطوط المشتركة داخل الشكل!",
            "Trace the outer border all the way around back to your starting corner.",
            ["Walk around the outside edges one segment at a time.", f"Summing all outer segments gives {m(ans)}."],
            "Interior grid lines do not belong to the outer perimeter.",
            "نتتبّع الإطار الخارجي حول الشكل حتى نعود إلى نقطة البداية.",
            ["نجمع أطوال القطع الخارجية المحيطة بالشكل.", f"المجموع الكلي للمحيط يساوي {m(ans)}."],
            "الخطوط الداخلية المشتركة لا تدخل في المحيط.",
            diagram_en=diag,
        ))

    # Hard (5): Missing side from given perimeter & glued squares
    hard_specs = [
        ("A rectangular painting has a **perimeter of \\( 26 \\) cm** and a length of \\( 8 \\) cm. What is its **width** in centimeters?",
         "لوحة فنية مستطيلة **محيطها \\( 26 \\) سم** وطولها \\( 8 \\) سم. كم سنتيمتراً يبلغ **عرضها**؟",
         5, [9, 10, 18], svg_g3_grid_rect(8, 5, top_lbl="8 cm", side_lbl="? cm", caption="Perimeter = 26 cm")),
        ("Omar bends a \\( 36 \\) cm wire into a **square** with four equal sides. How many centimeters long is **one side** of the square?",
         "ثنى عمر سلكاً طوله \\( 36 \\) سم ليشكّل **مربعاً** متطابق الأضلاع. كم سنتيمتراً طول **الضلع الواحد**؟",
         9, [6, 8, 18], svg_g3_grid_rect(6, 6, top_lbl="? cm", caption="Square perimeter = 36 cm")),
        ("A rectangular playground has a **perimeter of \\( 30 \\) m** and a width of \\( 6 \\) m. What is its **length** in meters?",
         "ملعب مستطيل **محيطه \\( 30 \\) م** وعرضه \\( 6 \\) م. كم متراً يبلغ **طوله**؟",
         9, [5, 12, 24], svg_g3_grid_rect(9, 6, top_lbl="? m", side_lbl="6 m", caption="Perimeter = 30 m")),
        ("A stepped garden terrace fits inside an \\( 11 \\) m by \\( 7 \\) m corner as shown. What is the **perimeter** of the stepped terrace in meters?",
         "مدرّج حديقة يمتد على قاعدة \\( 11 \\) م وارتفاع \\( 7 \\) م كما في الشكل. ما **محيط** المدرّج بالمتر؟",
         36, [18, 29, 77], svg_kang_staircase_perimeter("11 m", "7 m", steps=4)),
        ("Two identical squares of side \\( 4 \\) cm are placed side-by-side sharing one edge to make an \\( 8 \\) cm by \\( 4 \\) cm rectangle. What is the **perimeter** of the new rectangle?",
         "وُضع مربعان متطابقان طول ضلع كل منهما \\( 4 \\) سم متجاورين يشتركان في ضلع واحد لتكوين مستطيل \\( 8 \\) سم × \\( 4 \\) سم. ما **محيط** المستطيل الناتج؟",
         24, [16, 28, 32], svg_g3_grid_rect(8, 4, top_lbl="8 cm", side_lbl="4 cm", caption="Two 4x4 squares joined")),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "For a rectangle, Length + Width equals HALF of the perimeter!",
            "في المستطيل يساوي (الطول + العرض) نصف المحيط تماماً!",
            "Use the perimeter relationship of all four outer sides.",
            ["Use Perimeter = 2 × (Length + Width) or 4 × Side.", f"Solving step-by-step gives {m(ans)}."],
            f"Checking all outer edges with {m(ans)} matches the stated geometry.",
            "نستعمل قانون المحيط للأضلاع الخارجية الأربعة.",
            ["نطبّق العلاقة: المحيط = 2 × (الطول + العرض) أو 4 × الضلع.", f"بحل الخطوة نجد الناتج {m(ans)}."],
            f"التحقق بجمع الأضلاع الخارجية يؤكد {m(ans)}.",
            diagram_en=diag,
        ))
    return out


def _gen_g3_geo_06(next_id) -> list[dict]:
    """G3-GEO-06: Area of rectangles & rectilinear shapes by counting unit squares."""
    tp, bp = "Geometry", "G3-GEO-06"
    out = []

    # Easy (5): Rectangular grid area
    easy_specs = [
        ("A mosaic mat covers \\( 5 \\) columns and \\( 4 \\) rows of unit squares. What is its **area** in square units?",
         "تغطي سجادة فسيفساء \\( 5 \\) أعمدة و\\( 4 \\) صفوف من المربعات. ما **مساحتها** بالوحدات المربعة؟", 5, 4),
        ("A glass window pane is \\( 7 \\) units long and \\( 3 \\) units wide on the grid. What is its **area** in square units?",
         "لوح زجاجي طوله \\( 7 \\) وحدات وعرضه \\( 3 \\) وحدات على الشبكة. ما **مساحته** بالوحدات المربعة؟", 7, 3),
        ("A square chessboard section measures \\( 6 \\) units by \\( 6 \\) units. How many **unit squares** cover its area?",
         "رقعة مربعة أبعادها \\( 6 \\) وحدات في \\( 6 \\) وحدات. كم **وحدة مربعة** تبلغ مساحتها؟", 6, 6),
        ("A classroom poster covers \\( 8 \\) units by \\( 4 \\) units on the wall grid. What is its **area** in square units?",
         "تغطي لوحة حائط \\( 8 \\) وحدات طولاً و\\( 4 \\) وحدات عرضاً. ما **مساحتها** بالوحدات المربعة؟", 8, 4),
        ("A solar panel model has \\( 9 \\) columns and \\( 3 \\) rows of square cells. What is its **area** in square cells?",
         "يتكون نموذج لوح شمسي من \\( 9 \\) أعمدة و\\( 3 \\) صفوف من المربعات. ما **مساحته** بالوحدات المربعة؟", 9, 3),
    ]
    for q_en, q_ar, c, r in easy_specs:
        ans = c * r
        perim = 2 * (c + r)
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, [c + r, perim, ans + c],
            "Area counts the unit squares INSIDE: multiply columns by rows!",
            "المساحة هي عدد الوحدات المربعة في الداخل: اضرب عدد الأعمدة في عدد الصفوف!",
            f"Multiply {m(c)} by {m(r)} to count all unit squares.",
            [f"Each of the {m(r)} rows contains {m(c)} unit squares.", f"Area = {m(f'{c} \\times {r} = {ans}')} square units."],
            f"Do not confuse area ({m(ans)}) with perimeter ({m(perim)})!",
            f"نضرب {m(c)} في {m(r)} لحساب جميع المربعات المظللة.",
            [f"يوجد {m(r)} صفوف وفي كل صف {m(c)} مربعات.", f"المساحة = {m(f'{c} \\times {r} = {ans}')} وحدة مربعة."],
            f"انتبه للفرق بين المساحة ({m(ans)}) والمحيط ({m(perim)}).",
            diagram_en=svg_g3_grid_rect(c, r, top_lbl=f"{c}", side_lbl=f"{r}"),
        ))

    # Medium (5): Counting unit squares in composite rectilinear shapes
    u_cells = [(0, 0), (3, 0), (0, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2)]
    l_cells = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
    t_cells = [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3)]
    step_cells = [(0, 3), (0, 2), (1, 3), (0, 1), (1, 2), (2, 3), (0, 0), (1, 1), (2, 2), (3, 3)]
    ring_cells = [(c, r) for c in range(4) for r in range(4) if c in (0, 3) or r in (0, 3)]
    med_specs = [
        ("Count the blue unit squares in the L-shaped tile figure on the \\( 4 \\times 4 \\) grid. What is its **area** in square units?",
         "عدّ المربعات الزرقاء في الشكل المظلل على حرف L داخل شبكة \\( 4 \\times 4 \\). ما **مساحته** بالوحدات المربعة؟",
         7, [8, 12, 16], svg_g3_grid_rect(4, 4, shaded_cells=l_cells, caption="Count shaded unit squares")),
        ("What is the **area** in square units of the U-shaped shaded figure on the \\( 4 \\times 3 \\) grid?",
         "ما **مساحة** الشكل المظلل على حرف U بالوحدات المربعة على شبكة \\( 4 \\times 3 \\)؟",
         8, [7, 10, 12], svg_g3_grid_rect(4, 3, shaded_cells=u_cells, caption="Count shaded unit squares")),
        ("What is the **area** in square units of the T-shaped shaded figure on the \\( 3 \\times 4 \\) grid?",
         "ما **مساحة** الشكل المظلل على حرف T بالوحدات المربعة على شبكة \\( 3 \\times 4 \\)؟",
         6, [5, 7, 12], svg_g3_grid_rect(3, 4, shaded_cells=t_cells, caption="Count shaded unit squares")),
        ("A staircase design shades \\( 4, 3, 2, \\) and \\( 1 \\) squares across the columns of a \\( 4 \\times 4 \\) grid. What is the **shaded area** in square units?",
         "يظلّل تصميم مدرّج \\( 4 \\) ثم \\( 3 \\) ثم \\( 2 \\) ثم \\( 1 \\) من المربعات في شبكة \\( 4 \\times 4 \\). ما **مساحة** الجزء المظلل؟",
         10, [9, 12, 16], svg_g3_grid_rect(4, 4, shaded_cells=[(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)])),
        ("A square frame shades the outer border of a \\( 4 \\times 4 \\) grid while leaving the center \\( 2 \\times 2 \\) white. What is the **shaded area**?",
         "إطار مربع يظلّل الحافة الخارجية لشبكة \\( 4 \\times 4 \\) ويترك الوسط \\( 2 \\times 2 \\) أبيض. ما **مساحة** الإطار المظلل؟",
         12, [8, 14, 16], svg_g3_grid_rect(4, 4, shaded_cells=ring_cells, caption="16 total - 4 white center")),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Count each shaded square once, row by row or column by column!",
            "عدّ كل مربع مظلل مرة واحدة صفاً بعد صف أو عموداً بعد عمود!",
            "Count all shaded unit squares inside the figure.",
            ["Group the shaded squares by rows or columns.", f"Adding the counts gives {m(ans)} square units."],
            f"Recounting by columns confirms {m(ans)} shaded squares.",
            "نعدّ جميع المربعات المظللة بتقسيمها إلى صفوف أو أعمدة.",
            ["نجمع عدد المربعات المظللة في كل صف.", f"المساحة الكلية تساوي {m(ans)} وحدات مربعة."],
            f"إعادة العد بالأعمدة تؤكد وجود {m(ans)} مربعات مظللة.",
            diagram_en=diag,
        ))

    # Hard (5): Area-perimeter bridges & courtyard cutouts
    fountain_cells = [(c, r) for c in range(6) for r in range(5) if not (2 <= c <= 3 and 1 <= r <= 2)]
    hard_specs = [
        ("A **square** patio has a **perimeter of \\( 24 \\) m**. What is the **area** of the patio in square meters?",
         "فناء **مربع** الشكل **محيطه \\( 24 \\) م**. ما **مساحة** الفناء بالمتر المربع؟",
         36, [12, 24, 48], svg_g3_grid_rect(6, 6, caption="Square with perimeter 24 m")),
        ("A rectangular carpet has an **area of \\( 42 \\) square meters** and a length of \\( 7 \\) m. What is its **width** in meters?",
         "سجادة مستطيلة **مساحتها \\( 42 \\) متراً مربعاً** وطولها \\( 7 \\) م. كم متراً يبلغ **عرضها**؟",
         6, [5, 7, 14], svg_g3_grid_rect(7, 6, top_lbl="7 m", side_lbl="? m", caption="Area = 42 sq m")),
        ("A \\( 6 \\times 5 \\) tiled courtyard leaves a \\( 2 \\times 2 \\) white fountain unshaded inside. How many unit squares are **shaded** around the fountain?",
         "ساحة مبلّطة أبعادها \\( 6 \\times 5 \\) تُرك في وسطها نافورة بيضاء \\( 2 \\times 2 \\). كم وحدة مربعة **مظللة** حول النافورة؟",
         26, [22, 28, 30], svg_g3_grid_rect(6, 5, shaded_cells=fountain_cells, caption="6x5 minus 2x2")),
        ("Rug A measures \\( 5 \\) m by \\( 5 \\) m, and Rug B measures \\( 6 \\) m by \\( 4 \\) m. By how many square meters is Rug A's **area** greater than Rug B's **area**?",
         "سجادة (أ) أبعادها \\( 5 \\) م × \\( 5 \\) م، وسجادة (ب) أبعادها \\( 6 \\) م × \\( 4 \\) م. بكم متراً مربعاً تزيد **مساحة** (أ) على **مساحة** (ب)؟",
         1, [0, 2, 25], svg_g3_grid_rect(5, 5, top_lbl="5 m", side_lbl="5 m", caption="Compare 5x5 vs 6x4")),
        ("A **square** herb garden has an **area of \\( 49 \\) square meters**. What is its **perimeter** in meters?",
         "حديقة أعشاب **مربعة** الشكل **مساحتها \\( 49 \\) متراً مربعاً**. ما **محيطها** بالمتر؟",
         28, [7, 14, 49], svg_g3_grid_rect(7, 7, caption="Square with area 49 sq m")),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Find the missing side length first (using Area = L × W or Perimeter = 4 × Side), then compute what the question asks!",
            "أوجد طول الضلع أولاً من القانون المناسب (المساحة أو المحيط) ثم احسب المقدار المطلوب!",
            "Connect side length, perimeter, and area in two logical steps.",
            ["Use the given area or perimeter to determine the side dimensions.", f"Compute the target quantity to get {m(ans)}."],
            f"Testing {m(ans)} against both area and perimeter formulas confirms consistency.",
            "نربط بين طول الضلع والمحيط والمساحة في خطوتين واضحتين.",
            ["نستخرج طول الضلع من المعلومة المعطاة أولاً.", f"نحسب المطلوب النهائي فنجد {m(ans)}."],
            f"التحقق بالقانونين يؤكد صحة الناتج {m(ans)}.",
            diagram_en=diag,
        ))
    return out



def _gen_g3_geo_07(next_id) -> list[dict]:
    """G3-GEO-07: 2D polygons (sides, vertices, right angles) & 3D solids (faces, edges, vertices)."""
    tp, bp = "Geometry", "G3-GEO-07"
    out = []

    # Easy (5): Polygon sides/vertices/right angles & basic 3D solid naming
    easy_specs = [
        ("num", "How many **sides** does the regular **hexagon** shown below have?",
         "كم **ضلعاً** للمضلع **السداسي** الموضح أدناه؟",
         6, [5, 7, 8], svg_regular_polygon(6)),
        ("num", "How many **vertices (corners)** does the **octagon** road-sign shape shown below have?",
         "كم **رأساً (زاوية)** للشكل **الثماني** الموضح أدناه؟",
         8, [6, 7, 10], svg_regular_polygon(8)),
        ("num", "How many **right angles** (square corners) does a **rectangle** have?",
         "كم **زاوية قائمة** في **المستطيل**؟",
         4, [2, 3, 8], svg_g3_symmetry_fig("rectangle", "NONE", "Rectangle corners")),
        ("num", "How many **vertices** does the **pentagon** shown below have?",
         "كم **رأساً** للمضلع **الخماسي** الموضح أدناه؟",
         5, [4, 6, 7], svg_regular_polygon(5)),
        ("bi", "Which 3D solid has **2 flat circular faces**, a curved side, and **0 vertices** as shown?",
         "ما المجسم ثلاثي الأبعاد الذي له **قاعدتان دائريتان مستويتان** وسطح منحنٍ و**صفر من الرؤوس** كما في الشكل؟",
         [("Cylinder", "الأسطوانة"), ("Cone", "المخروط"), ("Sphere", "الكرة"), ("Cube", "المكعب")],
         svg_g3_solid_3d("cylinder", "2 circular faces, 0 vertices")),
    ]
    for item in easy_specs:
        if item[0] == "num":
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Easy", bp,
                q_en, q_ar, ans, dists,
                "Count each straight side or corner vertex once around the polygon!",
                "عدّ كل ضلع مستقيم أو رأس زاوية مرة واحدة حول المضلع!",
                "Count the geometric feature directly on the polygon.",
                ["Start at the top and count clockwise around the shape.", f"Total count = {m(ans)}."],
                f"In any closed polygon, number of sides equals number of vertices ({m(ans)}).",
                "نعدّ السمة الهندسية باتجاه عقارب الساعة حول المضلع.",
                ["نبدأ من الرأس العلوي ونعدّ بالترتيب.", f"العدد الكلي = {m(ans)}."],
                f"في أي مضلع يتساوى عدد الأضلاع وعدد الرؤوس.",
                diagram_en=diag,
            ))
        else:
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Easy", bp,
                q_en, q_ar, pairs, 0,
                "Think of a soup can: two flat circles (top and bottom) and no sharp corners!",
                "تخيّل علبة العصير المعدنية: قاعدتان دائريتان ولا يوجد أي رأس مدبب!",
                "Match the face and vertex properties to the 3D solid.",
                ["A cone has 1 circle and 1 vertex; a sphere has 0 flat faces.", "Two circular faces and 0 vertices define a **Cylinder**."],
                "Cylinder matches all three clues.",
                "نطابق عدد الأوجه الدائرية والرؤوس مع المجسم.",
                ["المخروط له قاعدة واحدة ورأس واحد، والكرة ليس لها أوجه مستوية.", "الأسطوانة لها قاعدتان دائريتان وصفر من الرؤوس."],
                "الوصف ينطبق على الأسطوانة تماماً.",
                diag,
            ))

    # Medium (5): Faces, edges & vertices of 3D solids
    med_specs = [
        ("How many **edges** does the **rectangular prism** (tissue box shape) shown below have?",
         "كم **حرفاً** لـ **متوازي المستطيلات** (علبة المناديل) الموضح أدناه؟",
         12, [6, 8, 10], svg_g3_solid_3d("prism", "Rectangular prism")),
        ("How many **vertices** does a **cube** have?",
         "كم **رأساً** لـ **المكعب**؟",
         8, [6, 10, 12], svg_g3_solid_3d("cube", "Cube")),
        ("How many **faces** (including the square base) does a **square pyramid** have?",
         "كم **وجهاً** (شاملةً القاعدة المربعة) لـ **الهرم الرباعي**؟",
         5, [4, 6, 8], svg_g3_solid_3d("pyramid", "Square pyramid")),
        ("How many **vertices** (sharp points) does the **cone** shown below have?",
         "كم **رأساً** لـ **المخروط** الموضح أدناه؟",
         1, [0, 2, 3], svg_g3_solid_3d("cone", "Cone")),
        ("How many **flat faces** does a **sphere** (ball shape) have?",
         "كم **وجهاً مستوياً** لـ **الكرة** الموضحة أدناه؟",
         0, [1, 2, 6], svg_g3_solid_3d("sphere", "Sphere")),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Separate flat faces, straight edges, and corner vertices carefully!",
            "ميّز بدقة بين الأوجه المستوية والأحرف المستقيمة والرؤوس!",
            "Count the requested 3D attribute (faces, edges, or vertices).",
            ["Inspect top, bottom, and side parts of the 3D solid.", f"The exact count is {m(ans)}."],
            f"Standard Grade 3 solid property check confirms {m(ans)}.",
            "نحصي الخاصية المطلوبة (أوجه أو أحرف أو رؤوس) في المجسم ثلاثي الأبعاد.",
            ["نفحص القاعدة العلوية والسفلية والجوانب.", f"العدد الصحيح هو {m(ans)}."],
            f"خصائص المجسمات القياسية تؤكد {m(ans)}.",
            diagram_en=diag,
        ))

    # Hard (5): Solid riddles & combined polygon/solid reasoning
    hard_specs = [
        ("bi", "Mystery Solid Riddle: *'I have \\( 5 \\) faces: \\( 1 \\) face is a square and \\( 4 \\) faces are triangles. I have \\( 8 \\) edges and \\( 5 \\) vertices.'* Which 3D solid am I?",
         "لغز المجسم: *«لي \\( 5 \\) أوجه: وجه واحد مربع و\\( 4 \\) أوجه مثلثة، ولي \\( 8 \\) أحرف و\\( 5 \\) رؤوس»*. ما هذا المجسم؟",
         [("Square pyramid", "هرم رباعي"), ("Cube", "مكعب"), ("Rectangular prism", "متوازي مستطيلات"), ("Cone", "مخروط")],
         svg_g3_solid_3d("pyramid", "Mystery 3D solid")),
        ("num", "How many **more edges** does a **cube** have than a **square pyramid**?",
         "بكم **يزيد عدد أحرف المكعب** على **عدد أحرف الهرم الرباعي**؟",
         4, [1, 3, 6], svg_g3_solid_3d("cube", "Cube (12 edges) vs Pyramid (8 edges)")),
        ("num", "Salma draws **\\( 2 \\) pentagons** and **\\( 1 \\) triangle** with no shared sides. How many **sides** did Salma draw altogether?",
         "رسمت سلمى **مضلعين خماسيين** و**مثلثاً واحداً** منفصلة عن بعضها. كم **ضلعاً** رسمت سلمى إجمالاً؟",
         13, [8, 11, 15], svg_regular_polygon(5)),
        ("num", "Tariq places **\\( 2 \\) separate wooden cubes** on his desk. How many **faces** do the two cubes have in total?",
         "وضع طارق **مكعبين خشبيين منفصلين** على طاولته. كم **وجهاً** للمكعبين معاً؟",
         12, [6, 10, 16], svg_g3_solid_3d("cube", "2 separate cubes")),
        ("num", "Huda draws **\\( 3 \\) hexagons** and **\\( 1 \\) square** separately in her art book. How many **vertices** do all four polygons have together?",
         "رسمت هدى **\\( 3 \\) سداسيات** و**مربعاً واحداً** منفصلة في كراسة الرسم. كم **رأساً** للأشكال الأربعة معاً؟",
         22, [10, 18, 24], svg_regular_polygon(6)),
    ]
    for item in hard_specs:
        if item[0] == "bi":
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Hard", bp,
                q_en, q_ar, pairs, 0,
                "Which solid stands on a square base with 4 triangle sides meeting at 1 top apex?",
                "ما المجسم الذي يرتكز على قاعدة مربعة وتلتقي أوجهه المثلثة الأربعة في قمة واحدة؟",
                "Match 1 square base + 4 triangular faces to the square pyramid.",
                ["A cube and rectangular prism have 6 rectangular/square faces, not 5.", "1 square + 4 triangles = 5 faces -> **Square pyramid**."],
                "5 faces, 8 edges, and 5 vertices all match a square pyramid.",
                "قاعدة مربعة واحدة و4 أوجه مثلثة تحدّد الهرم الرباعي.",
                ["للمكعب ومتوازي المستطيلات 6 أوجه وليس 5.", "إذن المجسم هو **هرم رباعي**."],
                "له 5 أوجه و8 أحرف و5 رؤوس.",
                diag,
            ))
        else:
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Hard", bp,
                q_en, q_ar, ans, dists,
                "Recall each shape's side/face/edge count first, then multiply and add/subtract!",
                "تذكّر عدد أضلاع أو أوجه أو أحرف كل شكل أولاً ثم نفّذ الضرب والجمع أو الطرح!",
                "Combine the geometric counts of each shape step-by-step.",
                ["Write down the exact attribute count for each named shape.", f"Combine them as asked to obtain {m(ans)}."],
                f"Re-checking each individual polygon/solid confirms {m(ans)}.",
                "نكتب خاصية كل شكل هندسي على حدة ثم نجمع أو نطرح حسب المطلوب.",
                ["نحدّد عدد الأضلاع أو الأوجه أو الأحرف لكل شكل.", f"نحسب الناتج الكلي فنجد {m(ans)}."],
                f"مراجعة كل شكل بمفرده تؤكد الناتج {m(ans)}.",
                diagram_en=diag,
            ))
    return out


def _gen_g3_geo_08(next_id) -> list[dict]:
    """G3-GEO-08: Lines of symmetry, congruent figures & counting unit cubes in 3D stacks."""
    tp, bp = "Geometry", "G3-GEO-08"
    out = []

    # Easy (5): Counting unit cubes in 3D stacks & basic symmetry check
    easy_specs = [
        ("num", "How many unit cubes make up the 3-column tower shown (column heights \\( 3, 2, 2 \\))?",
         "كم مكعب وحدة يتكون منه المجسم ذو الأعمدة الثلاثة الموضح (بارتفاعات \\( 3، 2، 2 \\))؟",
         7, [5, 6, 8], svg_cube_stack_3d((3, 2, 2))),
        ("num", "Count all unit cubes in the stepped stack with column heights \\( 4, 2, 1 \\).",
         "كم مكعب وحدة في المجسم المدرّج الذي ارتفاعات أعمدته \\( 4، 2، 1 \\)؟",
         7, [6, 8, 9], svg_cube_stack_3d((4, 2, 1))),
        ("num", "How many unit cubes are glued together in the stack with column heights \\( 3, 3, 2 \\)?",
         "كم مكعب وحدة في المجسم المتراصّ ذي الارتفاعات \\( 3، 3، 2 \\)؟",
         8, [6, 7, 9], svg_cube_stack_3d((3, 3, 2))),
        ("num", "How many **lines of symmetry** does the butterfly polygon shown below have?",
         "كم **محور تماثل** لشكل الفراشة المضلع الموضح أدناه؟",
         1, [0, 2, 4], svg_g3_symmetry_fig("butterfly", "V", "Fold along vertical dashed line")),
        ("bi", "Look at the two blue squares drawn side-by-side with the **exact same shape and size**. How do we describe these two squares?",
         "انظر إلى المربعين الأزرقين المرسومين جنباً إلى جنب ولهما **الشكل نفسه والقياس نفسه تماماً**. ماذا نسمّي هذين المربعين؟",
         [("Congruent figures", "شكلان متطابقان"), ("Different-sized figures", "شكلان مختلفا القياس"), ("3D spheres", "كرتان ثلاثيتا الأبعاد"), ("Open curves", "منحنيان مفتوحان")],
         svg_g3_symmetry_fig("congruent_pair", "NONE", "Same shape and same size")),
    ]
    for item in easy_specs:
        if item[0] == "num":
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Easy", bp,
                q_en, q_ar, ans, dists,
                "Count every column from bottom to top—or test vertical and horizontal folds!",
                "عدّ كل عمود من الأسفل للأعلى، أو اختبر الطيّ الرأسي والأفقي!",
                "Sum the column heights or check matching fold halves.",
                ["Check each column (or fold line) carefully.", f"Result = {m(ans)}."],
                f"Direct visual check confirms {m(ans)}.",
                "نجمع ارتفاعات الأعمدة أو نختبر تطابق نصفي الشكل عند الطي.",
                ["نفحص كل عمود أو محور طي بعناية.", f"الناتج الصحيح = {m(ans)}."],
                f"التحقق البصري المباشر يؤكد {m(ans)}.",
                diagram_en=diag,
            ))
        else:
            _, q_en, q_ar, pairs, diag = item
            out.append(_make_bilingual_q(
                next_id(), tp, "Easy", bp,
                q_en, q_ar, pairs, 0,
                "Same shape AND same size is the exact definition of congruence!",
                "تساوي الشكل والقياس معاً هو تعريف التطابق!",
                "Figures with identical shape and size are congruent.",
                ["Both figures are squares with equal side lengths.", "Therefore they are **Congruent figures**."],
                "Sliding one onto the other covers it with zero overlap left out.",
                "الشكلان اللذان يتفقان في الشكل والقياس متطابقان.",
                ["كلاهما مربع وبنفس طول الضلع.", "إذن هما **شكلان متطابقان**."],
                "عند وضع أحدهما فوق الآخر ينطبقان تماماً.",
                diag,
            ))

    # Medium (5): Counting exact lines of symmetry & 4-column stacks
    med_specs = [
        ("How many **lines of symmetry** does a **square** have in all?",
         "كم **محور تماثل** لـ **المربع** إجمالاً؟",
         4, [1, 2, 8], svg_g3_symmetry_fig("square", "ALL4", "Vertical, horizontal & 2 diagonals")),
        ("How many **lines of symmetry** does a **non-square rectangle** (length longer than width) have?",
         "كم **محور تماثل** لـ **مستطيل غير مربع** (طوله أكبر من عرضه)؟",
         2, [1, 4, 0], svg_g3_symmetry_fig("rectangle", "BOTH", "Vertical & horizontal midlines")),
        ("How many **lines of symmetry** does the horizontal right-pointing **arrow** shape shown below have?",
         "كم **محور تماثل** لشكل **السهم** المتجه يميناً الموضح أدناه؟",
         1, [0, 2, 4], svg_g3_symmetry_fig("arrow", "H", "Horizontal fold line")),
        ("How many **lines of symmetry** does an **unequal-arm L-shape** tile (long vertical arm, shorter horizontal arm) have?",
         "كم **محور تماثل** لبلاطة على شكل حرف **L غير متساوي الذراعين**؟",
         0, [1, 2, 4], svg_g3_symmetry_fig("L_tile", "NONE", "Unequal arms")),
        ("How many unit cubes are in the 4-column tower with heights \\( 4, 4, 2, \\) and \\( 1 \\)?",
         "كم مكعب وحدة في المجسم المكون من 4 أعمدة ارتفاعاتها \\( 4، 4، 2، 1 \\)؟",
         11, [9, 10, 12], svg_cube_stack_3d((4, 4, 2, 1))),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Test vertical, horizontal, and diagonal fold lines—both halves must overlap 100%!",
            "اختبر الطي الرأسي والأفقي والقطري؛ يجب أن ينطبق النصفان بنسبة 100%!",
            "Count valid symmetry axes (or sum all column heights).",
            ["Test each candidate fold line (or column height).", f"Exact count = {m(ans)}."],
            f"Remember a non-square rectangle has {m(2)} symmetry lines while a square has {m(4)}.",
            "نختبر جميع خطوط الطي الممكنة (أو نجمع ارتفاعات الأعمدة).",
            ["نتحقق من انطباق النصفين تماماً عند الطي.", f"العدد الصحيح هو {m(ans)}."],
            f"مراجعة خصائص التماثل تؤكد الناتج {m(ans)}.",
            diagram_en=diag,
        ))

    # Hard (5): Spatial cube completion & 3D block counting
    hard_specs = [
        ("Look at the complete \\( 2 \\times 2 \\times 2 \\) solid cube shown below. How many small unit cubes build a full \\( 2 \\times 2 \\times 2 \\) cube?",
         "انظر إلى المكعب الكامل \\( 2 \\times 2 \\times 2 \\) الموضح أدناه. كم مكعب وحدة صغيراً يكوّن مكعباً كاملاً أبعاده \\( 2 \\times 2 \\times 2 \\)؟",
         8, [4, 6, 12], svg_painted_cube_3d(2)),
        ("Rakan wants to build a full \\( 2 \\times 2 \\times 2 \\) cube (\\( 8 \\) unit cubes), and he already has a stack of \\( 5 \\) unit cubes (heights \\( 2, 2, 1 \\)). How many **more** unit cubes does he need?",
         "يريد راكان بناء مكعب كامل \\( 2 \\times 2 \\times 2 \\) (مكوّن من \\( 8 \\) مكعبات وحدة)، ولديه حالياً \\( 5 \\) مكعبات (بارتفاعات \\( 2، 2، 1 \\)). كم مكعباً **إضافياً** يحتاج؟",
         3, [2, 4, 5], svg_cube_stack_3d((2, 2, 1))),
        ("A rectangular box holds \\( 2 \\) layers, with \\( 6 \\) unit cubes in each layer (\\( 12 \\) cubes when full). If \\( 7 \\) unit cubes are already inside, how many **more** unit cubes are needed to fill it?",
         "صندوق يتسع لطبقتين في كل طبقة \\( 6 \\) مكعبات وحدة (أي \\( 12 \\) مكعباً عند امتلائه). إذا وُضعت فيه \\( 7 \\) مكعبات، فكم مكعباً **إضافياً** يلزم لملئه؟",
         5, [4, 6, 12], svg_cube_stack_3d((3, 2, 2))),
        ("Look at the \\( 3 \\times 3 \\times 3 \\) Rubik-style cube made of \\( 3 \\) equal layers of \\( 9 \\) unit cubes each. How many unit cubes are in the **entire** \\( 3 \\times 3 \\times 3 \\) cube?",
         "انظر إلى المكعب \\( 3 \\times 3 \\times 3 \\) المكوّن من \\( 3 \\) طبقات متساوية في كل طبقة \\( 9 \\) مكعبات صغيرة. كم مكعب وحدة في المجسم **كله**؟",
         27, [9, 18, 24], svg_painted_cube_3d(3)),
        ("A regular **pentagon** has \\( 5 \\) lines of symmetry and a **square** has \\( 4 \\) lines of symmetry. What is the **sum** of their lines of symmetry?",
         "للمضلع **الخماسي المنتظم** \\( 5 \\) محاور تماثل ولـ **المربع** \\( 4 \\) محاور تماثل. ما **مجموع** محاور التماثل للشكلين معاً؟",
         9, [1, 8, 20], svg_regular_polygon(5)),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Count layer-by-layer (including hidden interior cubes!), then subtract or add as needed!",
            "عدّ طبقةً بعد طبقة (مع تذكّر المكعبات الداخلية المخفية!) ثم اطرح أو اجمع حسب المطلوب!",
            "Count 3D layers systematically (or sum symmetry axes).",
            ["Find the total cubes per layer times number of layers.", f"Complete the comparison or sum to get {m(ans)}."],
            f"Layer-by-layer accounting confirms {m(ans)}.",
            "نحسب عدد المكعبات في كل طبقة ونضرب في عدد الطبقات ثم نكمل الخطوة المطلوبة.",
            ["نحدّد العدد الكلي للمكعبات (شاملاً المخفية في الداخل).", f"بحساب المطلوب نصل إلى {m(ans)}."],
            f"الحساب الطبقي يؤكد صحة الإجابة {m(ans)}.",
            diagram_en=diag,
        ))
    return out



# ==============================================================================
# Topic 4: Data & Probability (G3-DAT-01 .. G3-DAT-04)
# ==============================================================================


def _gen_g3_dat_01(next_id) -> list[dict]:
    """G3-DAT-01: Reading pictographs (whole & half symbols; keys 2, 4, 5, 10)."""
    tp, bp = "Data & Probability", "G3-DAT-01"
    out = []

    # Easy (5): Whole-symbol pictographs with keys 2, 4, 5, 10
    easy_specs = [
        ("In the library pictograph, **each circle stands for \\( 5 \\) books**. How many books did **Sara** read?",
         "في لوحة التمثيل بالرموز للمكتبة **يمثّل كل رمز دائري \\( 5 \\) كتب**. كم كتاباً قرأت **سارة**؟",
         20, [4, 15, 25], [("Sara", 4.0), ("Maha", 3.0), ("Lina", 5.0)], "Key: Each circle = 5 books"),
        ("In the orchard pictograph, **each circle stands for \\( 10 \\) palm trees**. How many palm trees are in **Field B**?",
         "في التمثيل بالرموز للمزرعة **يمثّل كل رمز \\( 10 \\) نخلات**. كم نخلة في **الحقل ب**؟",
         60, [6, 50, 70], [("Field A", 4.0), ("Field B", 6.0), ("Field C", 3.0)], "Key: Each circle = 10 trees"),
        ("In the art room pictograph, **each circle stands for \\( 2 \\) stars**. How many stars did **Ali** earn?",
         "في لوحة النجوم **يمثّل كل رمز دائري \\( 2 \\) نجمة**. كم نجمة حصل عليها **علي**؟",
         14, [7, 12, 16], [("Ali", 7.0), ("Sami", 5.0), ("Badr", 4.0)], "Key: Each circle = 2 stars"),
        ("In the bakery pictograph, **each circle stands for \\( 4 \\) pies**. How many pies were sold on **Monday**?",
         "في تمثيل المخبز **يمثّل كل رمز دائري \\( 4 \\) فطائر**. كم فطيرة بيعت يوم **الإثنين**؟",
         24, [6, 20, 28], [("Sun", 5.0), ("Mon", 6.0), ("Tue", 3.0)], "Key: Each circle = 4 pies"),
        ("In the recycling pictograph, **each circle stands for \\( 5 \\) cans**. How many cans did **Team 1** collect?",
         "في تمثيل التدوير **يمثّل كل رمز \\( 5 \\) علب**. كم علبة جمع **الفريق 1**؟",
         35, [7, 30, 40], [("Team 1", 7.0), ("Team 2", 4.0), ("Team 3", 6.0)], "Key: Each circle = 5 cans"),
    ]
    for q_en, q_ar, ans, dists, rows, key_lbl in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "Read the Key at the bottom first, then multiply the number of circles by the key value!",
            "اقرأ المفتاح أسفل اللوحة أولاً ثم اضرب عدد الرموز في قيمة المفتاح!",
            "Multiply the symbol count by the pictograph key.",
            ["Count the full symbols in the target row.", f"Multiply by the key value to obtain {m(ans)}."],
            "Always multiply by the key instead of reporting raw icon count.",
            "نضرب عدد الرموز في قيمة المفتاح الموضح أسفل التمثيل.",
            ["نعدّ الرموز في الصف المطلوب.", f"نضرب في قيمة الرمز الواحد فنحصل على {m(ans)}."],
            "تأكّدنا من استعمال قيمة المفتاح لا عدد الرموز المجرد.",
            diagram_en=svg_nafes_pictograph(rows, key_lbl),
        ))

    # Medium (5): Half-symbols & two-row comparisons
    med_specs = [
        ("In the fruit pictograph, **each full circle = \\( 4 \\) apples** (so a half-circle = \\( 2 \\)). How many apples are in **Basket A** (\\( 4 \\) full circles and \\( 1 \\) half-circle)?",
         "في تمثيل الفاكهة **كل دائرة كاملة = \\( 4 \\) تفاحات** (ونصف الدائرة = \\( 2 \\)). كم تفاحة في **السلة أ** (\\( 4 \\) دوائر كاملة ونصف دائرة)؟",
         18, [16, 17, 20], [("Basket A", 4.5), ("Basket B", 3.0), ("Basket C", 2.5)], "Key: Each circle = 4 apples"),
        ("In the reading pictograph, **each full circle = \\( 10 \\) pages**. How many pages did **Noura** read (\\( 3 \\) full circles and \\( 1 \\) half-circle)?",
         "في تمثيل القراءة **كل دائرة كاملة = \\( 10 \\) صفحات**. كم صفحة قرأت **نورة** (\\( 3 \\) دوائر كاملة ونصف دائرة)؟",
         35, [30, 31, 40], [("Noura", 3.5), ("Reem", 2.0), ("Huda", 4.0)], "Key: Each circle = 10 pages"),
        ("In the sports pictograph, **each full circle = \\( 2 \\) goals**. How many **more** goals did **Red Team** (\\( 5 \\) full circles and \\( 1 \\) half-circle) score than **Blue Team** (\\( 3 \\) full circles)?",
         "في تمثيل الأهداف **كل دائرة كاملة = هدفين (\\( 2 \\))**. بكم هدفاً **يزيد** **الفريق الأحمر** (\\( 5 \\) دوائر كاملة ونصف دائرة) على **الفريق الأزرق** (\\( 3 \\) دوائر كاملة)؟",
         5, [2, 6, 11], [("Red", 5.5), ("Blue", 3.0), ("Green", 4.0)], "Key: Each circle = 2 goals"),
        ("In the garden pictograph, **each full circle = \\( 4 \\) flowers**. How many flowers are in **Row 1** (\\( 2 \\) full circles and \\( 1 \\) half-circle) and **Row 2** (\\( 3 \\) full circles) **altogether**?",
         "في تمثيل الحديقة **كل دائرة كاملة = \\( 4 \\) زهرات**. كم زهرة في **الصف 1** (دائرتان كاملتان ونصف دائرة) و**الصف 2** (\\( 3 \\) دوائر كاملة) **معاً**؟",
         22, [10, 20, 24], [("Row 1", 2.5), ("Row 2", 3.0), ("Row 3", 1.5)], "Key: Each circle = 4 flowers"),
        ("In the shells pictograph, **each full circle = \\( 8 \\) shells**. How many shells did **Ziyad** collect (\\( 2 \\) full circles and \\( 1 \\) half-circle)?",
         "في تمثيل الأصداف **كل دائرة كاملة = \\( 8 \\) صدفات**. كم صدفة جمع **زياد** (دائرتان كاملتان ونصف دائرة)؟",
         20, [16, 18, 24], [("Ziyad", 2.5), ("Anas", 3.0), ("Fahad", 1.5)], "Key: Each circle = 8 shells"),
    ]
    for q_en, q_ar, ans, dists, rows, key_lbl in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "A half-circle stands for HALF of the key value! Compute each row's value first.",
            "نصف الدائرة يساوي نصف قيمة المفتاح! احسب قيمة كل صف أولاً ثم اجمع أو اطرح.",
            "Evaluate whole symbols plus half-symbols using the key.",
            ["Multiply full circles by the key and add half the key for any half-circle.", f"Combine as asked to get {m(ans)}."],
            f"Checking whole + half values confirms {m(ans)}.",
            "نحسب قيمة الرموز الكاملة ونصف الرمز باستعمال المفتاح.",
            ["نضرب الرموز الكاملة في المفتاح ونضيف نصف المفتاح لنصف الرمز.", f"نحسب المطلوب فنحصل على {m(ans)}."],
            f"مراجعة قيم الصفوف تؤكد {m(ans)}.",
            diagram_en=svg_nafes_pictograph(rows, key_lbl),
        ))

    # Hard (5): Multi-row totals & hidden-key pictograph reasoning
    hard_specs = [
        ("In the pictograph, **each full circle = \\( 4 \\) stickers**. How many stickers did **All Three Students** collect altogether (\\( 3 \\) full and \\( 1 \\) half, \\( 2 \\) full and \\( 1 \\) half, and \\( 2 \\) full circles)?",
         "في التمثيل بالرموز **كل دائرة كاملة = \\( 4 \\) ملصقات**. كم ملصقاً جمع **الطلاب الثلاثة معاً** (\\( 3 \\) دوائر ونصف، ودائرتان ونصف، ودائرتان كاملتان)؟",
         32, [8, 28, 30], [("Omar", 3.5), ("Saad", 2.5), ("Rami", 2.0)], "Key: Each circle = 4 stickers"),
        ("In this pictograph, the key was smudged, but we know **Grade 3A** planted **\\( 15 \\) trees** shown by **\\( 3 \\) full circles**. Using the same key, how many trees did **Grade 3B** plant with **\\( 5 \\) full circles**?",
         "في هذا التمثيل بالرموز مُسح المفتاح، لكننا نعلم أن **الصف 3أ** زرع **\\( 15 \\) شجرة** ممثلة بـ **\\( 3 \\) دوائر كاملة**. كم شجرة زرع **الصف 3ب** الممثل بـ **\\( 5 \\) دوائر كاملة**؟",
         25, [20, 30, 17], [("3A (15)", 3.0), ("3B (?)", 5.0), ("3C", 2.0)], "Key: ? trees per circle"),
        ("In a pictograph where **3 full circles represent \\( 12 \\) cupcakes**, how many cupcakes do **4 full circles and 1 half-circle** represent?",
         "في تمثيل بالرموز تمثّل فيه **3 دوائر كاملة \\( 12 \\) كعكة**، كم كعكة تمثّلها **4 دوائر كاملة ونصف دائرة**؟",
         18, [16, 17, 20], [("Tray 1", 3.0), ("Tray 2", 4.5)], "3 circles = 12 cupcakes"),
        ("In the pictograph (**1 circle = \\( 10 \\) Riyals**), **Hessa** saved \\( 4 \\) full circles and \\( 1 \\) half-circle, and **Amal** saved \\( 2 \\) full circles and \\( 1 \\) half-circle. How many **more** Riyals did Hessa save than Amal?",
         "في التمثيل بالرموز (**كل دائرة = \\( 10 \\) ريالات**)، ادّخرت **حصة** \\( 4 \\) دوائر كاملة ونصف دائرة وادّخرت **أمل** دائرتين كاملتين ونصف دائرة. بكم ريالاً **يزيد** ما ادّخرته حصة على أمل؟",
         20, [15, 25, 70], [("Hessa", 4.5), ("Amal", 2.5), ("Mona", 3.0)], "Key: Each circle = 10 SAR"),
        ("In the pictograph (**1 circle = \\( 6 \\) dates**), **Bowl 1** has \\( 3 \\) full circles and \\( 1 \\) half-circle, and **Bowl 2** has \\( 2 \\) full circles and \\( 1 \\) half-circle. How many dates are in **both bowls together**?",
         "في التمثيل بالرموز (**كل دائرة = \\( 6 \\) تمرات**)، في **الطبق 1** \\( 3 \\) دوائر كاملة ونصف دائرة وفي **الطبق 2** دائرتان كاملتان ونصف دائرة. كم تمرة في **الطبقين معاً**؟",
         36, [30, 33, 42], [("Bowl 1", 3.5), ("Bowl 2", 2.5)], "Key: Each circle = 6 dates"),
    ]
    for q_en, q_ar, ans, dists, rows, key_lbl in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Find the value of 1 full circle (and 1 half-circle) first, then compute each row!",
            "أوجد أولاً قيمة الدائرة الكاملة (ونصف الدائرة) ثم احسب قيمة كل صف!",
            "Determine the symbol value and combine the row amounts.",
            ["Find 1 circle's value (divide known row if key is hidden) and note two halves make 1 whole circle.", f"Compute the requested total/difference = {m(ans)}."],
            f"Recalculating row-by-row confirms {m(ans)}.",
            "نحدّد قيمة الرمز الواحد أولاً ثم نجمع أو نطرح قيم الصفوف.",
            ["نحسب قيمة الرمز الكامل ونصف الرمز.", f"بحساب المطلوب نصل إلى الناتج {m(ans)}."],
            f"مراجعة حساب كل صف تؤكد {m(ans)}.",
            diagram_en=svg_nafes_pictograph(rows, key_lbl),
        ))
    return out


def _gen_g3_dat_02(next_id) -> list[dict]:
    """G3-DAT-02: Reading bar charts & answering 'how many more / altogether' questions."""
    tp, bp = "Data & Probability", "G3-DAT-02"
    out = []

    # Easy (5): Direct bar height reading & two-bar sums
    easy_specs = [
        ("The bar chart shows favorite fruits in Grade 3: Dates (\\( 16 \\)), Apples (\\( 12 \\)), Bananas (\\( 14 \\)), Oranges (\\( 8 \\)). How many students chose **Bananas**?",
         "يوضّح التمثيل بالأعمدة الفاكهة المفضلة لطلاب الصف الثالث: التمر (\\( 16 \\))، التفاح (\\( 12 \\))، الموز (\\( 14 \\))، البرتقال (\\( 8 \\)). كم طالباً اختار **الموز**؟",
         14, [8, 12, 16], [("Dates", 16, "16"), ("Apple", 12, "12"), ("Banan", 14, "14"), ("Orang", 8, "8")], 20),
        ("The bar chart shows pets owned by students: Cats (\\( 15 \\)), Birds (\\( 11 \\)), Fish (\\( 9 \\)), Turtles (\\( 5 \\)). How many students chose **Cats and Turtles together**?",
         "يبيّن التمثيل بالأعمدة الحيوانات الأليفة: القطط (\\( 15 \\))، الطيور (\\( 11 \\))، الأسماك (\\( 9 \\))، السلاحف (\\( 5 \\)). كم طالباً اختار **القطط والسلاحف معاً**؟",
         20, [10, 15, 24], [("Cats", 15, "15"), ("Birds", 11, "11"), ("Fish", 9, "9"), ("Turtl", 5, "5")], 20),
        ("The bar chart shows books borrowed each day: Sun (\\( 10 \\)), Mon (\\( 18 \\)), Tue (\\( 14 \\)), Wed (\\( 12 \\)). On Monday, how many books were borrowed?",
         "يوضّح التمثيل بالأعمدة الكتب المستعارة يومياً: الأحد (\\( 10 \\))، الإثنين (\\( 18 \\))، الثلاثاء (\\( 14 \\))، الأربعاء (\\( 12 \\)). كم كتاباً استُعير يوم **الإثنين**؟",
         18, [10, 12, 14], [("Sun", 10, "10"), ("Mon", 18, "18"), ("Tue", 14, "14"), ("Wed", 12, "12")], 20),
        ("The bar chart shows art colors picked: Blue (\\( 13 \\)), Green (\\( 17 \\)), Red (\\( 9 \\)), Yellow (\\( 7 \\)). How many picked **Red and Yellow altogether**?",
         "يوضّح التمثيل بالأعمدة الألوان المختارة: الأزرق (\\( 13 \\))، الأخضر (\\( 17 \\))، الأحمر (\\( 9 \\))، الأصفر (\\( 7 \\)). كم طالباً اختار **الأحمر والأصفر معاً**؟",
         16, [2, 18, 22], [("Blue", 13, "13"), ("Green", 17, "17"), ("Red", 9, "9"), ("Yellw", 7, "7")], 20),
        ("The bar chart shows goals scored by four classes: 3A (\\( 6 \\)), 3B (\\( 12 \\)), 3C (\\( 9 \\)), 3D (\\( 15 \\)). What is the **highest** number of goals scored by one class?",
         "يبيّن التمثيل بالأعمدة أهداف أربعة فصول: 3أ (\\( 6 \\))، 3ب (\\( 12 \\))، 3ج (\\( 9 \\))، 3د (\\( 15 \\)). ما **أعلى** عدد أهداف سجّله فصل واحد؟",
         15, [6, 9, 12], [("3A", 6, "6"), ("3B", 12, "12"), ("3C", 9, "9"), ("3D", 15, "15")], 16),
    ]
    for q_en, q_ar, ans, dists, bars, ym in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "Read the height above the named bar(s) carefully!",
            "اقرأ القيمة أعلى العمود المطلوب (أو العمودين معاً) بدقة!",
            "Read the bar height(s) from the chart.",
            ["Locate the named category along the bottom axis.", f"Read (or sum) the bar value(s) to get {m(ans)}."],
            f"Axis scale and bar label match {m(ans)}.",
            "نقرأ ارتفاع العمود المطلوب من التمثيل البياني.",
            ["نحدّد الصنف المطلوب على المحور الأفقي.", f"نقرأ القيمة (أو نجمع العمودين) فنحصل على {m(ans)}."],
            f"تدريج المحور يؤكد القيمة {m(ans)}.",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        ))

    # Medium (5): "How many more / fewer" & 4-bar totals
    med_specs = [
        ("The bar chart shows science projects: Plants (\\( 19 \\)), Magnets (\\( 11 \\)), Weather (\\( 14 \\)), Rocks (\\( 8 \\)). How many **more** projects were on **Plants** than on **Rocks**?",
         "يبيّن التمثيل بالأعمدة مشاريع العلوم: النباتات (\\( 19 \\))، المغناطيس (\\( 11 \\))، الطقس (\\( 14 \\))، الصخور (\\( 8 \\)). بكم **يزيد** عدد مشاريع **النباتات** على **الصخور**؟",
         11, [8, 13, 27], [("Plant", 19, "19"), ("Magn", 11, "11"), ("Weath", 14, "14"), ("Rocks", 8, "8")], 20),
        ("The bar chart shows sandwiches sold: Cheese (\\( 22 \\)), Egg (\\( 15 \\)), Tuna (\\( 9 \\)), Honey (\\( 14 \\)). How many sandwiches were sold **in all** across the four types?",
         "يوضّح التمثيل بالأعمدة الشطائر المبيعة: جبن (\\( 22 \\))، بيض (\\( 15 \\))، تونة (\\( 9 \\))، عسل (\\( 14 \\)). كم شطيرة بيعت **إجمالاً** من الأنواع الأربعة؟",
         60, [46, 50, 58], [("Chees", 22, "22"), ("Egg", 15, "15"), ("Tuna", 9, "9"), ("Honey", 14, "14")], 24),
        ("The bar chart shows seashells found: Laila (\\( 24 \\)), Salma (\\( 17 \\)), Dana (\\( 13 \\)), Joud (\\( 19 \\)). How many **fewer** seashells did **Dana** find than **Laila**?",
         "يبيّن التمثيل بالأعمدة الأصداف التي جمعتها الطالبات: ليلى (\\( 24 \\))، سلمى (\\( 17 \\))، دانة (\\( 13 \\))، جود (\\( 19 \\)). بكم **يقل** ما جمعته **دانة** عما جمعته **ليلى**؟",
         11, [7, 13, 37], [("Laila", 24, "24"), ("Salma", 17, "17"), ("Dana", 13, "13"), ("Joud", 19, "19")], 24),
        ("The bar chart shows museum visitors by hour: 9 AM (\\( 12 \\)), 10 AM (\\( 18 \\)), 11 AM (\\( 15 \\)), 12 PM (\\( 9 \\)). How many visitors entered **altogether** during those four hours?",
         "يوضّح التمثيل بالأعمدة زوار المتحف: 9 ص (\\( 12 \\))، 10 ص (\\( 18 \\))، 11 ص (\\( 15 \\))، 12 م (\\( 9 \\)). كم زائراً دخل **إجمالاً** في الساعات الأربع؟",
         54, [45, 52, 56], [("9AM", 12, "12"), ("10AM", 18, "18"), ("11AM", 15, "15"), ("12PM", 9, "9")], 20),
        ("The bar chart shows stickers earned: Fahad (\\( 21 \\)), Sami (\\( 14 \\)), Adel (\\( 18 \\)), Rami (\\( 12 \\)). How many **more** stickers did **Fahad** earn than **Sami**?",
         "يبيّن التمثيل بالأعمدة الملصقات: فهد (\\( 21 \\))، سامي (\\( 14 \\))، عادل (\\( 18 \\))، رامي (\\( 12 \\)). بكم **يزيد** ما حصل عليه **فهد** على **سامي**؟",
         7, [6, 9, 35], [("Fahad", 21, "21"), ("Sami", 14, "14"), ("Adel", 18, "18"), ("Rami", 12, "12")], 24),
    ]
    for q_en, q_ar, ans, dists, bars, ym in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "'How many more / fewer' means SUBTRACT; 'in all / altogether' means ADD!",
            "«بكم يزيد / يقل» تعني الطرح، و«إجمالاً / معاً» تعني الجمع!",
            "Read the bar heights and add or subtract as asked.",
            ["Extract the exact numbers above the relevant bars.", f"Compute the sum or difference to get {m(ans)}."],
            f"Double-checking the bar values confirms {m(ans)}.",
            "نستخرج القيم من الأعمدة ثم نجمع أو نطرح حسب السؤال.",
            ["نحدّد قيم الأعمدة المطلوبة من الرسم.", f"نحسب الناتج فنجد {m(ans)}."],
            f"مراجعة الأعداد على الأعمدة تؤكد {m(ans)}.",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        ))

    # Hard (5): Missing '?' bar from total & combined-pair bar comparisons
    hard_specs = [
        ("A total of **\\( 50 \\) students** voted for four school clubs: Science (\\( 16 \\)), Art (\\( 12 \\)), Sports (\\( ? \\)), and Coding (\\( 8 \\)). What number belongs on the missing **Sports** bar?",
         "صوّت **\\( 50 \\) طالباً** لأربعة أندية مدرسية: العلوم (\\( 16 \\))، الفنون (\\( 12 \\))، الرياضة (\\( ? \\))، البرمجة (\\( 8 \\)). ما العدد المفقود لعمود **الرياضة**؟",
         14, [12, 16, 36], [("Sci", 16, "16"), ("Art", 12, "12"), ("Sport", 14, "?"), ("Code", 8, "8")], 20),
        ("Across four days, a shop sold **\\( 64 \\) lanterns** in all: Sun (\\( 15 \\)), Mon (\\( 19 \\)), Tue (\\( ? \\)), Wed (\\( 13 \\)). How many lanterns were sold on **Tuesday**?",
         "باع متجر خلال أربعة أيام **\\( 64 \\) فانوساً** إجمالاً: الأحد (\\( 15 \\))، الإثنين (\\( 19 \\))، الثلاثاء (\\( ? \\))، الأربعاء (\\( 13 \\)). كم فانوساً بيع يوم **الثلاثاء**؟",
         17, [15, 19, 47], [("Sun", 15, "15"), ("Mon", 19, "19"), ("Tue", 17, "?"), ("Wed", 13, "13")], 20),
        ("Look at the bar chart of seedlings planted: Mon (\\( 18 \\)), Tue (\\( 15 \\)), Wed (\\( 11 \\)), Thu (\\( 14 \\)). How many **more** seedlings were planted on **Mon and Tue together** than on **Wed and Thu together**?",
         "في تمثيل شتلات الأشجار: الإثنين (\\( 18 \\))، الثلاثاء (\\( 15 \\))، الأربعاء (\\( 11 \\))، الخميس (\\( 14 \\)). بكم **يزيد** مجموع **الإثنين والثلاثاء معاً** على مجموع **الأربعاء والخميس معاً**؟",
         8, [6, 10, 25], [("Mon", 18, "18"), ("Tue", 15, "15"), ("Wed", 11, "11"), ("Thu", 14, "14")], 20),
        ("A survey of **\\( 45 \\) Grade 3 students** recorded favorite snacks: Dates (\\( 14 \\)), Nuts (\\( 9 \\)), Fruit (\\( ? \\)), Yogurt (\\( 10 \\)). How many chose **Fruit**?",
         "شمل استطلاع **\\( 45 \\) طالباً** حول الوجبة الخفيفة: التمر (\\( 14 \\))، المكسرات (\\( 9 \\))، الفواكه (\\( ? \\))، الزبادي (\\( 10 \\)). كم طالباً اختار **الفواكه**؟",
         12, [10, 13, 33], [("Dates", 14, "14"), ("Nuts", 9, "9"), ("Fruit", 12, "?"), ("Yogrt", 10, "10")], 16),
        ("Points scored in four rounds: R1 (\\( 20 \\)), R2 (\\( 16 \\)), R3 (\\( 12 \\)), R4 (\\( 15 \\)). How many **more** points were scored in **R1 and R2 together** than in **R3 and R4 together**?",
         "نقاط أربع جولات: ج1 (\\( 20 \\))، ج2 (\\( 16 \\))، ج3 (\\( 12 \\))، ج4 (\\( 15 \\)). بكم **يزيد** مجموع **ج1 وج2 معاً** على مجموع **ج3 وج4 معاً**؟",
         9, [7, 11, 27], [("R1", 20, "20"), ("R2", 16, "16"), ("R3", 12, "12"), ("R4", 15, "15")], 24),
    ]
    for q_en, q_ar, ans, dists, bars, ym in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Sum the known bars first, then subtract from the grand total (or subtract the second pair's sum)!",
            "اجمع الأعمدة المعلومة أولاً ثم اطرح من الإجمالي الكلي (أو اطرح مجموع الزوج الثاني)!",
            "Combine known bar values first, then subtract.",
            ["Add the known bar counts carefully.", f"Subtract to obtain {m(ans)}."],
            f"All bar counts add back to the stated grand total (or pair difference {m(ans)}).",
            "نجمع القيم المعلومة أولاً ثم نطرح لإيجاد المطلوب.",
            ["نحسب مجموع الأعمدة المعلومة.", f"نطرح فنحصل على {m(ans)}."],
            f"مراجعة المجاميع تؤكد الناتج {m(ans)}.",
            diagram_en=svg_bar_chart(bars, y_max=ym),
        ))
    return out



def _gen_g3_dat_03(next_id) -> list[dict]:
    """G3-DAT-03: Frequency & tally tables and two-attribute classroom tables."""
    tp, bp = "Data & Probability", "G3-DAT-03"
    out = []

    # Easy (5): Reading single category tally counts
    easy_specs = [
        ("In the tally table of favorite subjects, **Math** has \\( 3 \\) crossed bundles of five and \\( 4 \\) single marks. How many students chose **Math**?",
         "في جدول الإشارات للمواد المفضلة حصلت **الرياضيات** على \\( 3 \\) حِزم خماسية و\\( 4 \\) إشارات مفردة. كم طالباً اختار **الرياضيات**؟",
         19, [15, 16, 24], "Subject", [("Math", 19), ("Science", 13), ("Art", 11)]),
        ("In the tally chart of favorite birds, **Falcon** has \\( 4 \\) crossed bundles of five and \\( 1 \\) single mark. How many votes did **Falcon** get?",
         "في جدول الإشارات للطيور حصل **الصقر** على \\( 4 \\) حِزم خماسية وإشارة مفردة واحدة. كم صوتاً نال **الصقر**؟",
         21, [17, 20, 25], "Bird", [("Falcon", 21), ("Pigeon", 12), ("Parrot", 9)]),
        ("In the tally table of recess games, **Tag** has \\( 2 \\) crossed bundles of five and \\( 3 \\) single marks. How many students chose **Tag**?",
         "في جدول إشارات ألعاب الفسحة حصلت لعبة **المطاردة** على حزمتين خماسيتين و\\( 3 \\) إشارات مفردة. كم طالباً اختارها؟",
         13, [11, 12, 15], "Game", [("Tag", 13), ("Rope", 16), ("Ball", 10)]),
        ("In the tally chart of ice-cream flavors, **Vanilla** has \\( 3 \\) full crossed bundles of five and \\( 0 \\) extra marks. How many chose **Vanilla**?",
         "في جدول نكهات المثلجات حصلت **الفانيلا** على \\( 3 \\) حِزم خماسية كاملة دون إشارات إضافية. كم طالباً اختار **الفانيلا**؟",
         15, [12, 18, 20], "Flavor", [("Vanilla", 15), ("Mango", 11), ("Berry", 7)]),
        ("In the tally chart of transport to school, **Bus** has \\( 4 \\) crossed bundles of five and \\( 3 \\) single marks. How many students ride the **Bus**?",
         "في جدول وسيلة الذهاب للمدرسة حصلت **الحافلة** على \\( 4 \\) حِزم خماسية و\\( 3 \\) إشارات مفردة. كم طالباً يركب **الحافلة**؟",
         23, [19, 20, 24], "Way", [("Bus", 23), ("Car", 14), ("Walk", 6)]),
    ]
    for q_en, q_ar, ans, dists, hdr, rows in easy_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Easy", bp,
            q_en, q_ar, ans, dists,
            "Count each crossed bundle as 5, then add any leftover single marks!",
            "احسب كل حزمة خماسية بـ 5 ثم أضف الإشارات المفردة المتبقية!",
            "Multiply crossed bundles by 5 and add leftover single strokes.",
            ["Each crossed bundle represents 5 tally marks.", f"Adding the bundles and single marks gives {m(ans)}."],
            f"Skip-counting by fives confirms {m(ans)}.",
            "نضرب عدد الحِزم في 5 ثم نجمع الإشارات المفردة.",
            ["كل حزمة مشطوبة تساوي 5 إشارات.", f"بجمع الحِزم مع المفردات نحصل على {m(ans)}."],
            f"العد القفزي بالخمسات يؤكد الناتج {m(ans)}.",
            diagram_en=svg_g3_tally_table(hdr, rows),
        ))

    # Medium (5): Comparing tally categories & summing whole tally charts
    med_specs = [
        ("In the tally chart of library books: Stories has \\( 18 \\) marks, Science has \\( 12 \\) marks, and History has \\( 9 \\) marks. How many books were tallied **in all**?",
         "في جدول إشارات كتب المكتبة: القصص \\( 18 \\)، والعلوم \\( 12 \\)، والتاريخ \\( 9 \\). كم كتاباً سُجّل **إجمالاً**؟",
         39, [30, 37, 41], "Type", [("Stories", 18), ("Science", 12), ("History", 9)]),
        ("In the tally chart of art supplies: Markers has \\( 22 \\) marks and Crayons has \\( 14 \\) marks. How many **more** votes did **Markers** get than **Crayons**?",
         "في جدول الأدوات الفنية: الأقلام الملونة \\( 22 \\) إشارة والشمعية \\( 14 \\) إشارة. بكم **تزيد** أصوات **الأقلام الملونة** على **الشمعية**؟",
         8, [6, 12, 36], "Supply", [("Markers", 22), ("Crayons", 14), ("Paints", 10)]),
        ("In the tally chart of weather days in Rajab: Sunny has \\( 16 \\) marks, Cloudy has \\( 8 \\) marks, and Rainy has \\( 6 \\) marks. How many days were recorded **altogether**?",
         "في جدول حالة الطقس: مشمس \\( 16 \\)، غائم \\( 8 \\)، ممطر \\( 6 \\). كم يوماً رُصدت **جميعاً**؟",
         30, [24, 28, 32], "Weather", [("Sunny", 16), ("Cloudy", 8), ("Rainy", 6)]),
        ("In the tally chart of pastry choices: Cheese has \\( 19 \\) marks and Zaatar has \\( 11 \\) marks. How many **fewer** students chose **Zaatar** than **Cheese**?",
         "في جدول الفطائر: الجبن \\( 19 \\) إشارة والزعتر \\( 11 \\) إشارة. بكم **يقل** من اختاروا **الزعتر** عمن اختاروا **الجبن**؟",
         8, [7, 9, 30], "Pastry", [("Cheese", 19), ("Zaatar", 11), ("Spinach", 7)]),
        ("In the tally chart of classroom helpers: Board has \\( 9 \\) marks, Books has \\( 14 \\) marks, and Plants has \\( 11 \\) marks. How many helpers were tallied **altogether**?",
         "في جدول مهام الصف: السبورة \\( 9 \\)، الكتب \\( 14 \\)، النباتات \\( 11 \\). كم طالباً في الجدول **إجمالاً**؟",
         34, [25, 32, 36], "Task", [("Board", 9), ("Books", 14), ("Plants", 11)]),
    ]
    for q_en, q_ar, ans, dists, hdr, rows in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Read each tally row carefully (bundles of 5 + singles), then add or subtract as asked!",
            "احسب قيمة كل صف من الإشارات أولاً ثم اجمع أو اطرح حسب المطلوب!",
            "Convert each tally row to a number, then combine.",
            ["Verify the numeric count of each row.", f"Compute the total or difference = {m(ans)}."],
            f"Re-checking the tally bundles confirms {m(ans)}.",
            "نحوّل الإشارات إلى أعداد ثم نجمع أو نطرح.",
            ["نتأكد من العدد المقابل لكل صف.", f"نحسب المجموع أو الفرق فنجد {m(ans)}."],
            f"مراجعة الحِزم الخماسية تؤكد {m(ans)}.",
            diagram_en=svg_g3_tally_table(hdr, rows),
        ))

    # Hard (5): Two-attribute classroom tables & missing tally row
    hard_specs = [
        ("The two-way classroom table shows club sign-ups for Grade 3A and Grade 3B. How many students signed up for **Science Club in both classes together**?",
         "يوضّح الجدول المزدوج تسجيل طلاب الصفين 3أ و3ب في الأندية. كم طالباً سجّل في **نادي العلوم من الفصلين معاً**؟",
         29, [25, 27, 31],
         svg_nafes_function_table(["Class", "Science", "Art"], [["3A", 16, 11], ["3B", 13, 14]])),
        ("Using the two-way table of morning vs. afternoon library borrows, how many **more** books were borrowed on **Monday** (total) than on **Sunday** (total)?",
         "من الجدول المزدوج لاستعارة الكتب صباحاً ومساءً، بكم **يزيد** مجموع استعارة يوم **الإثنين** على مجموع يوم **الأحد**؟",
         7, [5, 9, 25],
         svg_nafes_function_table(["Day", "Morning", "Afternoon"], [["Sun", 14, 11], ["Mon", 19, 13]])),
        ("All **\\( 36 \\) students** in Grade 3 voted in the tally chart: Football got \\( 15 \\) votes, Swimming got \\( 12 \\) votes, and Running got \\( ? \\) votes. How many tally marks belong in **Running**?",
         "صوّت جميع طلاب الصف الثالث وعددهم **\\( 36 \\) طالباً**: كرة القدم \\( 15 \\)، السباحة \\( 12 \\)، الجري \\( ? \\). كم إشارة توضع أمام **الجري**؟",
         9, [7, 11, 27],
         svg_g3_tally_table("Sport", [("Football", 15), ("Swimming", 12), ("Running", 9)], hide_idx=2)),
        ("In the two-attribute snack table, every row adds to its Row Total. What number replaces **?** for Grade 3B Juice?",
         "في جدول الوجبات المزدوج يمثّل العمود الأخير مجموع كل صف. ما العدد الذي يحل محل **?** لعصير الصف 3ب؟",
         14, [12, 16, 26],
         svg_nafes_function_table(["Class", "Milk", "Juice", "Total"], [["3A", 15, 13, 28], ["3B", 12, "?", 26]], highlight_cell=(1, 2))),
        ("All **\\( 40 \\) camp students** chose one craft: Pottery got \\( 14 \\) tallies, Weaving got \\( 11 \\) tallies, and Painting got \\( ? \\) tallies. How many chose **Painting**?",
         "اختار **\\( 40 \\) طالباً** في المخيم نشاطاً واحداً: الفخار \\( 14 \\)، النسيج \\( 11 \\)، الرسم \\( ? \\). كم طالباً اختار **الرسم**؟",
         15, [13, 16, 25],
         svg_g3_tally_table("Craft", [("Pottery", 14), ("Weaving", 11), ("Painting", 15)], hide_idx=2)),
    ]
    for q_en, q_ar, ans, dists, diag in hard_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Hard", bp,
            q_en, q_ar, ans, dists,
            "Read the exact row and column headers first, then add the known parts or subtract from the total!",
            "اقرأ عناوين الصفوف والأعمدة بدقة، ثم اجمع المعلوم أو اطرحه من الإجمالي الكلي!",
            "Combine row/column entries systematically to find the target count.",
            ["Identify the exact cells needed from the table.", f"Add or subtract to obtain {m(ans)}."],
            f"Checking row and column totals confirms {m(ans)}.",
            "نستخرج القيم المطلوبة من خلايا الجدول ثم نجمع أو نطرح.",
            ["نحدّد الصف والعمود المقصودين بدقة.", f"نحسب الناتج فنجد {m(ans)}."],
            f"مراجعة مجاميع الجدول تؤكد {m(ans)}.",
            diagram_en=diag,
        ))
    return out


def _gen_g3_dat_04(next_id) -> list[dict]:
    """G3-DAT-04: Likelihood words (certain/more likely/equally likely/impossible) & simple fraction probability."""
    tp, bp = "Data & Probability", "G3-DAT-04"
    out = []

    # Easy (5): Likelihood vocabulary on marble jars & spinners
    easy_specs = [
        ("A jar contains **\\( 8 \\) red marbles** and **\\( 0 \\) other colors**. Without looking, Nora picks \\( 1 \\) marble. How likely is she to pick a **red** marble?",
         "يحتوي وعاء على **\\( 8 \\) كرات حمراء فقط** ولا يوجد أي لون آخر. سحبت نورة كرة دون النظر؛ ما وصف احتمال سحب كرة **حمراء**؟",
         [("Certain", "أكيد"), ("More likely", "أكثر احتمالاً"), ("Equally likely", "متساوي الإمكانية"), ("Impossible", "مستحيل")],
         svg_g3_marble_bag([("Red", 8, "#fca5a5")], "All 8 marbles are red")),
        ("A spinner is divided into \\( 6 \\) equal sectors: \\( 3 \\) **Blue** and \\( 3 \\) **Yellow**. How likely is the pointer to land on **Blue** compared with **Yellow**?",
         "قُسّم قرص دوّار إلى \\( 6 \\) أجزاء متطابقة: \\( 3 \\) **زرقاء** و\\( 3 \\) **صفراء**. ما وصف احتمال الوقوف على **الأزرق** مقارنةً **بالأصفر**؟",
         [("Equally likely", "متساوي الإمكانية"), ("Certain", "أكيد"), ("Impossible", "مستحيل"), ("Less likely", "أقل احتمالاً")],
         svg_nafes_spinner(["Blue", "Yellow", "Blue", "Yellow", "Blue", "Yellow"], "3 Blue, 3 Yellow")),
        ("A bag holds **\\( 9 \\) blue cubes** and **\\( 2 \\) green cubes**. Without looking, Adel draws \\( 1 \\) cube. Picking a **blue** cube is:",
         "في كيس **\\( 9 \\) مكعبات زرقاء** و**مكعبان أخضران**. سحب عادل مكعباً دون النظر؛ سحب مكعب **أزرق** يُوصف بأنه:",
         [("More likely", "أكثر احتمالاً"), ("Certain", "أكيد"), ("Less likely", "أقل احتمالاً"), ("Impossible", "مستحيل")],
         svg_g3_marble_bag([("Blue", 9, "#93c5fd"), ("Green", 2, "#86efac")], "9 Blue, 2 Green")),
        ("A spinner has \\( 4 \\) equal sectors labeled **1, 2, 3, 4**. How likely is spinning the number **9**?",
         "قرص دوّار مقسّم إلى \\( 4 \\) أجزاء متطابقة مرقّمة **1، 2، 3، 4**. ما وصف احتمال وقوف المؤشر على العدد **9**؟",
         [("Impossible", "مستحيل"), ("Less likely", "أقل احتمالاً"), ("Equally likely", "متساوي الإمكانية"), ("Certain", "أكيد")],
         svg_nafes_spinner(["1", "2", "3", "4"], "Numbers 1 to 4")),
        ("A jar has **\\( 2 \\) purple marbles** and **\\( 8 \\) orange marbles**. Picking a **purple** marble without looking is:",
         "في وعاء **كرتان بنفسجيتان** و**\\( 8 \\) كرات برتقالية**. سحب كرة **بنفسجية** دون النظر يُوصف بأنه:",
         [("Less likely", "أقل احتمالاً"), ("Impossible", "مستحيل"), ("More likely", "أكثر احتمالاً"), ("Certain", "أكيد")],
         svg_g3_marble_bag([("Purple", 2, "#d8bfe6"), ("Orange", 8, "#fdba74")], "2 Purple, 8 Orange")),
    ]
    for q_en, q_ar, pairs, diag in easy_specs:
        out.append(_make_bilingual_q(
            next_id(), tp, "Easy", bp,
            q_en, q_ar, pairs, 0,
            "All = Certain, Zero = Impossible, Half = Equally likely, Most (but not all) = More likely, Few (but > 0) = Less likely!",
            "الكل = أكيد، الصفر = مستحيل، النصف = متساوي الإمكانية، الأغلب = أكثر احتمالاً، الأقل (أكبر من صفر) = أقل احتمالاً!",
            "Compare the count of matching outcomes to the total outcomes.",
            ["Count how many items match the event versus other items.", f"Select **{pairs[0][0]}**."],
            "Be careful never to confuse 'More likely' with 'Certain' or 'Less likely' with 'Impossible'!",
            "نقارن عدد النواتج المطابقة بإجمالي النواتج الممكنة.",
            ["نحصي عدد القطع المطابقة للحدث.", f"الوصف الدقيق هو **{pairs[0][1]}**."],
            "انتبه للفرق بين (أكثر احتمالاً وأكيد) وبين (أقل احتمالاً ومستحيل).",
            diag,
        ))

    # Medium (5): Simple fraction probability on spinners & marble jars
    med_specs = [
        ("The spinner has \\( 5 \\) equal sectors: \\( 3 \\) **Green** and \\( 2 \\) **Red**. What fraction expresses the probability of landing on **Green**?",
         "قرص دوّار مقسّم إلى \\( 5 \\) أجزاء متطابقة: \\( 3 \\) **خضراء** و\\( 2 \\) **حمراء**. ما الكسر الذي يمثّل احتمال الوقوف على **الأخضر**؟",
         Fraction(3, 5), [Fraction(2, 5), Fraction(1, 5), Fraction(3, 8)],
         svg_nafes_spinner(["Green", "Green", "Red", "Green", "Red"], "5 equal sectors")),
        ("A bag holds \\( 8 \\) identical marbles: \\( 5 \\) **Blue** and \\( 3 \\) **Yellow**. What fraction gives the probability of picking a **Yellow** marble?",
         "في كيس \\( 8 \\) كرات متماثلة: \\( 5 \\) **زرقاء** و\\( 3 \\) **صفراء**. ما الكسر الذي يمثّل احتمال سحب كرة **صفراء**؟",
         Fraction(3, 8), [Fraction(5, 8), Fraction(3, 5), Fraction(1, 8)],
         svg_g3_marble_bag([("Blue", 5, "#93c5fd"), ("Yellow", 3, "#fde047")], "8 marbles total")),
        ("The spinner is split into \\( 6 \\) equal sectors labeled **A, A, A, A, A, B**. What fraction gives the probability of landing on **B**?",
         "قُسّم قرص دوّار إلى \\( 6 \\) أجزاء متطابقة مكتوب عليها **A, A, A, A, A, B**. ما الكسر الذي يمثّل احتمال الوقوف على **B**؟",
         Fraction(1, 6), [Fraction(5, 6), Fraction(1, 5), Fraction(1, 8)],
         svg_nafes_spinner(["A", "A", "A", "A", "A", "B"], "6 equal sectors")),
        ("A box holds \\( 10 \\) fruit cards: \\( 7 \\) **Apple** cards and \\( 3 \\) **Fig** cards. What fraction gives the probability of drawing an **Apple** card?",
         "في علبة \\( 10 \\) بطاقات: \\( 7 \\) بطاقات **تفاح** و\\( 3 \\) بطاقات **تين**. ما الكسر الذي يمثّل احتمال سحب بطاقة **تفاح**؟",
         Fraction(7, 10), [Fraction(3, 10), Fraction(7, 8), Fraction(3, 5)],
         svg_g3_marble_bag([("Apple", 7, "#fca5a5"), ("Fig", 3, "#d8bfe6")], "10 cards total")),
        ("The spinner has \\( 4 \\) equal sectors: \\( 1 \\) **Star** and \\( 3 \\) **Moons**. What fraction gives the probability of landing on a **Moon**?",
         "قرص دوّار من \\( 4 \\) أجزاء متطابقة: جزء **نجمة** و\\( 3 \\) أجزاء **هلال**. ما الكسر الذي يمثّل احتمال الوقوف على **هلال**؟",
         Fraction(3, 4), [Fraction(1, 4), Fraction(1, 3), Fraction(3, 5)],
         svg_nafes_spinner(["Star", "Moon", "Moon", "Moon"], "4 equal sectors")),
    ]
    for q_en, q_ar, ans, dists, diag in med_specs:
        out.append(make_nafes_q(
            next_id(), LEVEL, tp, "Medium", bp,
            q_en, q_ar, ans, dists,
            "Write matching outcomes on top (numerator) and ALL equal outcomes on the bottom (denominator)!",
            "اكتب عدد النواتج المطلوبة في البسط وإجمالي النواتج الممكنة كلها في المقام!",
            "Form the fraction: favorable outcomes over total equal outcomes.",
            [f"Favorable count = {m(ans.numerator)}, total equal outcomes = {m(ans.denominator)}.", f"Probability = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"Denominator {m(ans.denominator)} includes ALL outcomes, not just the other color.",
            "نكتب احتمال الحدث ككسر بسطه النواتج المطلوبة ومقامه جميع النواتج المتساوية.",
            [f"عدد النواتج المطلوبة = {m(ans.numerator)} من أصل {m(ans.denominator)}.", f"الاحتمال = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
            f"المقام {m(ans.denominator)} يمثّل المجموع الكلي للنواتج.",
            diagram_en=diag,
        ))

    # Hard (5): Combined outcomes ("A or B") & balancing marble bags for equal likelihood
    hard_specs = [
        ("frac", "A spinner has \\( 8 \\) equal sectors: \\( 2 \\) **Red**, \\( 3 \\) **Blue**, and \\( 3 \\) **Yellow**. What fraction gives the probability of landing on **Red OR Blue**?",
         "قرص دوّار ذو \\( 8 \\) أجزاء متطابقة: \\( 2 \\) **أحمر** و\\( 3 \\) **أزرق** و\\( 3 \\) **أصفر**. ما الكسر الذي يمثّل احتمال الوقوف على **أحمر أو أزرق**؟",
         Fraction(5, 8), [Fraction(3, 8), Fraction(1, 4), Fraction(5, 6)],
         svg_nafes_spinner(["Red", "Red", "Blue", "Blue", "Blue", "Yel", "Yel", "Yel"], "8 equal sectors")),
        ("frac", "A jar holds \\( 10 \\) marbles: \\( 4 \\) **Green**, \\( 3 \\) **White**, and \\( 3 \\) **Pink**. What fraction gives the probability of picking a **Green OR White** marble?",
         "في وعاء \\( 10 \\) كرات: \\( 4 \\) **خضراء** و\\( 3 \\) **بيضاء** و\\( 3 \\) **وردية**. ما الكسر الذي يمثّل احتمال سحب كرة **خضراء أو بيضاء**؟",
         Fraction(7, 10), [Fraction(3, 10), Fraction(2, 5), Fraction(7, 8)],
         svg_g3_marble_bag([("Green", 4, "#86efac"), ("White", 3, "#f8fafc"), ("Pink", 3, "#fbcfe8")], "10 marbles total")),
        ("num", "A bag currently holds **\\( 7 \\) blue marbles** and **\\( 3 \\) yellow marbles**. How many **yellow** marbles must be added to the bag so that picking blue and picking yellow become **equally likely**?",
         "في كيس حالياً **\\( 7 \\) كرات زرقاء** و**\\( 3 \\) كرات صفراء**. كم كرة **صفراء** يجب إضافتها ليصبح سحب الأزرق والأصفر **متساوي الإمكانية**؟",
         4, [2, 3, 7],
         svg_g3_marble_bag([("Blue", 7, "#93c5fd"), ("Yellow", 3, "#fde047")], "Make Blue = Yellow")),
        ("num", "A mystery box holds **\\( 9 \\) green blocks** and **\\( 4 \\) orange blocks**. How many **orange** blocks must be added so that drawing green and drawing orange are **equally likely**?",
         "في صندوق **\\( 9 \\) مكعبات خضراء** و**\\( 4 \\) مكعبات برتقالية**. كم مكعباً **برتقالياً** يجب إضافته ليصبح اللونان **متساويي الإمكانية**؟",
         5, [4, 6, 9],
         svg_g3_marble_bag([("Green", 9, "#86efac"), ("Orange", 4, "#fdba74")], "Make Green = Orange")),
        ("frac", "A number wheel has \\( 5 \\) equal sectors numbered **1, 2, 3, 4, 5**. What fraction gives the probability of spinning an **odd number**?",
         "قرص أعداد مقسّم إلى \\( 5 \\) أجزاء متطابقة مرقّمة **1، 2، 3، 4، 5**. ما الكسر الذي يمثّل احتمال الوقوف على **عدد فردي**؟",
         Fraction(3, 5), [Fraction(2, 5), Fraction(1, 5), Fraction(4, 5)],
         svg_nafes_spinner(["1", "2", "3", "4", "5"], "Odd numbers: 1, 3, 5")),
    ]
    for item in hard_specs:
        if item[0] == "frac":
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Hard", bp,
                q_en, q_ar, ans, dists,
                "Count ALL sectors/marbles that satisfy the condition, and divide by the total count!",
                "اجمع جميع الأجزاء أو الكرات التي تحقق الشرط في البسط، وضع العدد الكلي في المقام!",
                "Count all matching outcomes over the total equal outcomes.",
                [f"Count of matching outcomes = {m(ans.numerator)} out of {m(ans.denominator)} total.", f"Probability = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
                f"Remaining non-matching outcomes = {m(ans.denominator - ans.numerator)}, summing to {m(ans.denominator)}.",
                "نحصي جميع النواتج المطابقة للشرط ونضعها فوق إجمالي النواتج.",
                [f"عدد النواتج المطابقة = {m(ans.numerator)} من أصل {m(ans.denominator)}.", f"الاحتمال = {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}}')}."],
                f"مجموع النواتج المطابقة وغير المطابقة يساوي {m(ans.denominator)}.",
                diagram_en=diag,
            ))
        else:
            _, q_en, q_ar, ans, dists, diag = item
            out.append(make_nafes_q(
                next_id(), LEVEL, tp, "Hard", bp,
                q_en, q_ar, ans, dists,
                "'Equally likely' means both colors must have the EXACT SAME number of items!",
                "«متساوي الإمكانية» يعني تساوي عدد الكرات أو المكعبات من اللونين تماماً!",
                "Subtract the smaller count from the larger count so both colors match.",
                ["Equally likely requires equal counts of both colors.", f"Subtracting the two counts gives {m(ans)} items to add."],
            f"Adding {m(ans)} makes both color counts identical.",
                "نجعل عددي اللونين متساويين بطرح العدد الأصغر من الأكبر.",
                ["تساوي الإمكانية يتطلب تساوي العددين.", f"بطرح العددين نجد أنه يلزم إضافة {m(ans)}."],
                f"عند إضافة {m(ans)} يصبح العددان متساويين تماماً.",
                diagram_en=diag,
            ))
    return out


def build_grade3_bank() -> list[dict]:
    """Build all 360 ETEC Nafes Grade 3 questions (24 blueprints x 15 = 120 Easy + 120 Medium + 120 Hard)."""
    counter = [0]

    def next_id() -> str:
        counter[0] += 1
        return f"NAFS-G3-{counter[0]:03d}"

    generators = [
        _gen_g3_num_01, _gen_g3_num_02, _gen_g3_num_03, _gen_g3_num_04,
        _gen_g3_num_05, _gen_g3_num_06, _gen_g3_num_07, _gen_g3_num_08,
        _gen_g3_alg_01, _gen_g3_alg_02, _gen_g3_alg_03, _gen_g3_alg_04,
        _gen_g3_geo_01, _gen_g3_geo_02, _gen_g3_geo_03, _gen_g3_geo_04,
        _gen_g3_geo_05, _gen_g3_geo_06, _gen_g3_geo_07, _gen_g3_geo_08,
        _gen_g3_dat_01, _gen_g3_dat_02, _gen_g3_dat_03, _gen_g3_dat_04,
    ]
    bank: list[dict] = []
    for gen in generators:
        chunk = gen(next_id)
        assert len(chunk) == 15, f"{gen.__name__} produced {len(chunk)} items (expected 15)"
        bank.extend(chunk)
    assert len(bank) == 360, f"Expected 360 Grade 3 items, got {len(bank)}"
    return bank
