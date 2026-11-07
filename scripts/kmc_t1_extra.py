"""KAUST Mathematics Competition (KMC) — Track 1: Grades 6-7
Extended Bank Expansion (300 beginner-friendly, programmatically verified bilingual questions).
Covers 18 visual & conceptual blueprints (50 questions per lesson group across Lessons 1.1–1.6).
Strictly aligned with official KMC Grades 6-7 syllabus (no calculators, zero out-of-scope terms).
"""
from fractions import Fraction
import math

from kmc_common import (
    explain_ar,
    explain_en,
    m,
    make_5_math_options,
    make_kmc_question,
)
from kmc_diagrams_extra import (
    svg_analog_clock,
    svg_cube_stack_3d,
    svg_digit_cards,
    svg_digital_clock,
    svg_dot_pattern,
    svg_fenceposts,
    svg_fraction_grid,
    svg_function_machine,
    svg_magic_square_3x3,
    svg_motion_timeline,
    svg_number_pyramid,
    svg_pan_balance_coins,
    svg_paper_fold,
    svg_pie_chart,
    svg_street_grid,
    svg_tape_bar_split,
    svg_two_jars,
    svg_venn_2,
)

LEVEL = "Track 1: Grades 6-7"


def _gen_group_1_1(next_id) -> list[dict]:
    """Lesson 1.1 group (50 Qs, Topic: 'Number Theory'):
    1. g67-visual-fraction-grid (17 Qs)
    2. g67-bundle-promo-discount (17 Qs)
    3. g67-two-jar-transfer (16 Qs)
    """
    items: list[dict] = []

    # -------------------------------------------------------------------------
    # 1. g67-visual-fraction-grid (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    grid_cases = [
        # (cols, rows, shaded, extra, mode, target, diff, ctx_en, ctx_ar)
        (5, 4, 8, 0, "frac", None, "Easy", "classroom mosaic panel", "لوحة فسيفساء صفية"),
        (6, 4, 9, 0, "frac", None, "Easy", "rectangular chocolate bar", "لوح شوكولاتة مستطيل"),
        (6, 5, 18, 0, "frac", None, "Easy", "garden patio grid", "شبكة بلاط في حديقة"),
        (5, 4, 7, 0, "pct", None, "Easy", "solar sensor board", "لوحة خلايا شمسية"),
        (5, 5, 11, 0, "pct", None, "Easy", "square art canvas", "لوحة فنية مربعة"),
        (8, 5, 14, 0, "pct", None, "Easy", "wall tile pattern", "تصميم بلاط جداري"),
        (5, 4, 5, 0, "more_frac", (3, 5), "Medium", "science display grid", "شبكة عرض علمية"),
        (6, 4, 7, 0, "more_frac", (3, 4), "Medium", "stained-glass window", "نافذة زجاج ملون"),
        (8, 3, 6, 0, "more_frac", (2, 3), "Medium", "rectangular sticker sheet", "ورقة ملصقات مستطيلة"),
        (7, 4, 9, 0, "more_frac", (3, 4), "Medium", "wooden game board", "رقعة لعب خشبية"),
        (5, 6, 9, 0, "more_pct", 70, "Medium", "ceiling light panel", "لوحة إضاءة سقفية"),
        (5, 5, 8, 0, "more_pct", 68, "Medium", "ceramic coaster grid", "شبكة قاعدة خزفية"),
        (8, 5, 13, 0, "more_pct", 65, "Medium", "digital pixel screen", "شاشة نقاط رقمية"),
        (5, 4, 6, 5, "white_pct", None, "Hard", "two-tone quilt block", "قطعة لحاف ثنائية اللون"),
        (6, 4, 7, 5, "more_total_frac", (5, 6), "Hard", "museum floor design", "تصميم أرضية متحف"),
        (6, 5, 8, 7, "more_purple_only", (3, 5), "Hard", "courtyard banner grid", "شبكة لافتة في الساحة"),
        (8, 4, 8, 6, "blue_of_nonpurple", None, "Hard", "laboratory tray grid", "شبكة صينية مختبر"),
    ]
    for cols, rows, shaded, extra, mode, target, diff, ctx_en, ctx_ar in grid_cases:
        qid = next_id()
        tot = cols * rows
        svg = svg_fraction_grid(cols, rows, shaded, extra)

        if mode == "frac":
            ans = Fraction(shaded, tot)
            g = math.gcd(shaded, tot)
            q_en = (
                f"A {ctx_en} is divided into a {m(cols)}-by-{m(rows)} grid of identical cells, "
                f"with {m(shaded)} cells shaded purple as shown. What **simplified fraction** of the entire grid is shaded?"
            )
            q_ar = (
                f"قُسِّمت {ctx_ar} إلى شبكة أبعادها {m(cols)} في {m(rows)} من المربعات المتطابقة، "
                f"وظُلِّلت منها {m(shaded)} مربعات باللون البنفسجي كما في الشكل. ما **الكسر في أبسط صورة** الذي يمثّل الجزء المظلّل من الشبكة كلها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    Fraction(tot - shaded, tot),
                    Fraction(shaded, tot - shaded),
                    Fraction(shaded + 1, tot),
                    Fraction(max(1, shaded - 1), tot),
                ],
                qid,
            )
            hint_en = "Count the total cells (columns × rows), write shaded over total, then divide top and bottom by their greatest common factor."
            hint_ar = "احسب العدد الكلي للمربعات (الأعمدة × الصفوف)، ثم اكتب الكسر وبسّطه بالقسمة على القاسم المشترك الأكبر."
            sol_en = explain_en(
                "A fraction of a grid equals **(number of shaded cells) ÷ (total number of equal cells)**.",
                [
                    f"Find the total number of equal cells: {m(f'{cols} \\times {rows} = {tot}')}.",
                    f"Since {m(shaded)} cells are shaded, the unsimplified fraction is {m(f'\\frac{{{shaded}}}{{{tot}}}')}.",
                    f"Divide numerator and denominator by {m(g)} to simplify: {m(f'\\frac{{{shaded} \\div {g}}}{{{tot} \\div {g}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
                ],
                f"Check: {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {tot} = {shaded}')} shaded cells!",
            )
            sol_ar = explain_ar(
                "كسر الجزء المظلّل يساوي **(عدد المربعات المظلّلة) ÷ (العدد الكلي للمربعات المتساوية)**.",
                [
                    f"نحسب العدد الكلي للمربعات: {m(f'{cols} \\times {rows} = {tot}')} مربعًا.",
                    f"بما أن عدد المربعات المظلّلة هو {m(shaded)}، نكتب الكسر {m(f'\\frac{{{shaded}}}{{{tot}}}')}.",
                    f"نبسّط الكسر بالقسمة على {m(g)}: {m(f'\\frac{{{shaded} \\div {g}}}{{{tot} \\div {g}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
                ],
                f"تحقق: {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {tot} = {shaded}')} مربعات مظلّلة.",
            )

        elif mode == "pct":
            assert (shaded * 100) % tot == 0
            ans = (shaded * 100) // tot
            scale = 100 // tot if 100 % tot == 0 else None
            q_en = (
                f"The {ctx_en} shown is a {m(cols)}-by-{m(rows)} grid of equal squares with {m(shaded)} squares shaded purple. "
                f"What **percentage** of the entire grid is shaded?"
            )
            q_ar = (
                f"تتكوّن {ctx_ar} الموضّحة من شبكة أبعادها {m(cols)} في {m(rows)} من المربعات المتطابقة، وفيها {m(shaded)} مربعًا مظلّلًا بالبنفسجي. "
                f"ما **النسبة المئوية** للجزء المظلّل من الشبكة كلها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [100 - ans, shaded, ans + 5, max(5, ans - 5)], qid, suffix="\\%"
            )
            hint_en = "Percentage means 'out of 100' — multiply the fraction (shaded ÷ total) by 100%."
            hint_ar = "النسبة المئوية تعني «من كل 100» — اضرب الكسر (المظلّل ÷ الكلي) في 100%."
            step2_en = (
                f"Multiply numerator and denominator of {m(f'\\frac{{{shaded}}}{{{tot}}}')} by {m(scale)}: {m(f'\\frac{{{shaded} \\times {scale}}}{{{tot} \\times {scale}}} = \\frac{{{ans}}}{{100}} = {ans}\\%')}."
                if scale
                else f"Convert {m(f'\\frac{{{shaded}}}{{{tot}}}')} to a percentage: {m(f'\\frac{{{shaded}}}{{{tot}}} \\times 100\\% = {ans}\\%')}."
            )
            sol_en = explain_en(
                "Turn the shaded fraction into parts out of 100 to read the percentage right away!",
                [
                    f"The grid has {m(f'{cols} \\times {rows} = {tot}')} equal squares in total, and {m(shaded)} are shaded.",
                    step2_en,
                ],
                f"Check: {m(f'{ans}\\%')} of {m(tot)} is {m(f'\\frac{{{ans}}}{{100}} \\times {tot} = {shaded}')} squares.",
            )
            sol_ar = explain_ar(
                "نحوّل كسر الجزء المظلّل إلى مقام 100 أو نضربه في 100% لإيجاد النسبة المئوية بسهولة.",
                [
                    f"عدد مربعات الشبكة الكلي هو {m(f'{cols} \\times {rows} = {tot}')} مربعًا، والمظلّل منها {m(shaded)}.",
                    f"نحسب النسبة المئوية: {m(f'\\frac{{{shaded}}}{{{tot}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"تحقق: {m(f'{ans}\\%')} من {m(tot)} تساوي {m(f'\\frac{{{ans}}}{{100}} \\times {tot} = {shaded}')} مربعًا.",
            )

        elif mode == "more_frac":
            p, q = target
            assert (tot * p) % q == 0
            goal = (tot * p) // q
            ans = goal - shaded
            q_en = (
                f"In the {m(cols)}-by-{m(rows)} {ctx_en} shown, {m(shaded)} unit squares are currently shaded. "
                f"How many **additional** white squares must be shaded so that **exactly** {m(f'\\frac{{{p}}}{{{q}}}')} of the entire grid is shaded?"
            )
            q_ar = (
                f"في {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} الموضّحة، يوجد حاليًا {m(shaded)} مربعات مظلّلة. "
                f"كم مربعًا أبيض **إضافيًا** يجب تظليله ليصبح الكسر المظلّل مساويًا {m(f'\\frac{{{p}}}{{{q}}}')} من الشبكة كلها بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [goal, tot - goal, ans + 2, max(1, ans - 2)], qid
            )
            hint_en = f"First find how many total squares equal {p}/{q} of {tot}, then subtract the {shaded} squares already shaded."
            hint_ar = f"أوجد أولًا عدد المربعات الذي يمثّل {p}/{q} من {tot}، ثم اطرح المربعات الـ {shaded} المظلّلة أصلًا."
            sol_en = explain_en(
                "Find the **target number of shaded squares** first, then subtract what is already shaded!",
                [
                    f"Total squares in the grid: {m(f'{cols} \\times {rows} = {tot}')}.",
                    f"Find {m(f'\\frac{{{p}}}{{{q}}}')} of {m(tot)}: {m(f'({tot} \\div {q}) \\times {p} = {tot // q} \\times {p} = {goal}')} squares.",
                    f"Subtract the {m(shaded)} squares already shaded: {m(f'{goal} - {shaded} = {ans}')} additional squares.",
                ],
                f"Check: {m(f'{shaded} + {ans} = {goal}')}, and {m(f'\\frac{{{goal}}}{{{tot}}} = \\frac{{{p}}}{{{q}}}')}!",
            )
            sol_ar = explain_ar(
                "نحسب **العدد المستهدف للمربعات المظلّلة** أولًا، ثم نطرح منه المربعات المظلّلة حاليًا!",
                [
                    f"العدد الكلي للمربعات هو {m(f'{cols} \\times {rows} = {tot}')}.",
                    f"نحسب {m(f'\\frac{{{p}}}{{{q}}}')} من {m(tot)}: {m(f'({tot} \\div {q}) \\times {p} = {goal}')} مربعًا.",
                    f"نطرح المربعات المظلّلة أصلًا ({m(shaded)}): {m(f'{goal} - {shaded} = {ans}')} مربعًا إضافيًا.",
                ],
                f"تحقق: {m(f'{shaded} + {ans} = {goal}')}، وبالفعل {m(f'\\frac{{{goal}}}{{{tot}}} = \\frac{{{p}}}{{{q}}}')}.",
            )

        elif mode == "more_pct":
            pct = target
            assert (tot * pct) % 100 == 0
            goal = (tot * pct) // 100
            ans = goal - shaded
            q_en = (
                f"The {m(cols)}-by-{m(rows)} {ctx_en} shown currently has {m(shaded)} shaded squares. "
                f"How many **more** squares need to be shaded so that **exactly** {m(f'{pct}\\%')} of the grid is shaded?"
            )
            q_ar = (
                f"تحتوي {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} حاليًا على {m(shaded)} مربعات مظلّلة. "
                f"كم مربعًا **إضافيًا** يجب تظليله ليصبح {m(f'{pct}\\%')} من الشبكة مظلّلًا بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [goal, tot - goal, ans + 1, max(1, ans - 1)], qid
            )
            hint_en = f"Calculate {pct}% of {tot} squares to get the target count, then subtract {shaded}."
            hint_ar = f"احسب {pct}% من {tot} مربعًا لمعرفة العدد المطلوب، ثم اطرح {shaded}."
            sol_en = explain_en(
                "Convert the target percentage into a concrete square count, then find the gap!",
                [
                    f"The grid contains {m(f'{cols} \\times {rows} = {tot}')} squares in total.",
                    f"Target shaded squares: {m(f'{pct}\\% \\text{{ of }} {tot} = \\frac{{{pct}}}{{100}} \\times {tot} = {goal}')} squares.",
                    f"Additional squares needed: {m(f'{goal} - {shaded} = {ans}')}.",
                ],
                f"Check: {m(f'{shaded} + {ans} = {goal}')} squares, and {m(f'\\frac{{{goal}}}{{{tot}}} \\times 100\\% = {pct}\\%')}.",
            )
            sol_ar = explain_ar(
                "نحوّل النسبة المئوية المستهدفة إلى عدد مربعات محدد، ثم نحسب الفرق!",
                [
                    f"إجمالي مربعات الشبكة هو {m(f'{cols} \\times {rows} = {tot}')} مربعًا.",
                    f"العدد المستهدف للمربعات المظلّلة: {m(f'\\frac{{{pct}}}{{100}} \\times {tot} = {goal}')} مربعًا.",
                    f"عدد المربعات الإضافية المطلوبة: {m(f'{goal} - {shaded} = {ans}')}.",
                ],
                f"تحقق: {m(f'{shaded} + {ans} = {goal}')}، و{m(f'\\frac{{{goal}}}{{{tot}}} \\times 100\\% = {pct}\\%')}.",
            )

        elif mode == "white_pct":
            colored = shaded + extra
            white = tot - colored
            assert (white * 100) % tot == 0
            ans = (white * 100) // tot
            q_en = (
                f"In the {m(cols)}-by-{m(rows)} {ctx_en} shown, {m(shaded)} cells are colored purple and {m(extra)} cells are colored sky-blue. "
                f"What **percentage** of the entire grid remains **uncolored (white)**?"
            )
            q_ar = (
                f"في {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} الموضّحة، لُوِّنت {m(shaded)} مربعات بالبنفسجي و{m(extra)} مربعات بالأزرق الفاتح. "
                f"ما **النسبة المئوية** للمربعات التي بقيت **بيضاء غير ملوّنة** من الشبكة كلها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [100 - ans, (shaded * 100) // tot, (extra * 100) // tot, white], qid, suffix="\\%"
            )
            hint_en = "Add the purple and sky-blue squares together, subtract from the total grid size to get the white squares, then convert to a percentage."
            hint_ar = "اجمع المربعات البنفسجية والزرقاء، واطرح الناتج من العدد الكلي لمعرفة المربعات البيضاء، ثم حوّلها إلى نسبة مئوية."
            sol_en = explain_en(
                "Count how many cells stay white first, then express that count out of 100%!",
                [
                    f"Total cells: {m(f'{cols} \\times {rows} = {tot}')}. Colored cells: {m(f'{shaded} + {extra} = {colored}')}.",
                    f"Uncolored (white) cells: {m(f'{tot} - {colored} = {white}')}.",
                    f"Percentage white: {m(f'\\frac{{{white}}}{{{tot}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"Check: colored is {m(f'{100 - ans}\\%')} and white is {m(f'{ans}\\%')}, totaling {m('100\\%')}!",
            )
            sol_ar = explain_ar(
                "نوجد عدد المربعات البيضاء أولًا ثم نحوّله إلى نسبة مئوية من إجمالي الشبكة!",
                [
                    f"العدد الكلي للمربعات: {m(f'{cols} \\times {rows} = {tot}')}، والملوّن منها: {m(f'{shaded} + {extra} = {colored}')}.",
                    f"عدد المربعات البيضاء المتبقية: {m(f'{tot} - {colored} = {white}')}.",
                    f"النسبة المئوية للأبيض: {m(f'\\frac{{{white}}}{{{tot}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"تحقق: الملوّن {m(f'{100 - ans}\\%')} والأبيض {m(f'{ans}\\%')}، ومجموعهما {m('100\\%')}.",
            )

        elif mode == "more_total_frac":
            p, q = target
            goal = (tot * p) // q
            colored = shaded + extra
            ans = goal - colored
            q_en = (
                f"The {m(cols)}-by-{m(rows)} {ctx_en} shown has {m(shaded)} purple tiles and {m(extra)} sky-blue tiles, while the rest are white. "
                f"How many white tiles must be colored so that colored tiles cover **exactly** {m(f'\\frac{{{p}}}{{{q}}}')} of the whole grid?"
            )
            q_ar = (
                f"تحتوي {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} على {m(shaded)} بلاطات بنفسجية و{m(extra)} بلاطات زرقاء فاتحة، والباقي أبيض. "
                f"كم بلاطة بيضاء يجب تلوينها لتغطي البلاطات الملوّنة {m(f'\\frac{{{p}}}{{{q}}}')} من الشبكة كلها بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [goal - shaded, goal, tot - colored, ans + 2], qid
            )
            hint_en = "Both purple and sky-blue count as colored tiles! Subtract their sum from the target number of colored tiles."
            hint_ar = "كل من البلاطات البنفسجية والزرقاء تُعد ملوّنة! اطرح مجموعهما من العدد المستهدف للبلاطات الملوّنة."
            sol_en = explain_en(
                "Combine both existing colors before subtracting from the target colored count!",
                [
                    f"Total grid size: {m(f'{cols} \\times {rows} = {tot}')} tiles. Target colored tiles: {m(f'\\frac{{{p}}}{{{q}}} \\times {tot} = {goal}')}.",
                    f"Tiles already colored (purple + sky-blue): {m(f'{shaded} + {extra} = {colored}')}.",
                    f"White tiles left to color: {m(f'{goal} - {colored} = {ans}')}.",
                ],
                f"Check: {m(f'{colored} + {ans} = {goal}')}, and {m(f'\\frac{{{goal}}}{{{tot}}} = \\frac{{{p}}}{{{q}}}')}.",
            )
            sol_ar = explain_ar(
                "نجمع اللونين الموجودين معًا أولًا قبل الطرح من العدد المستهدف للبلاطات الملوّنة!",
                [
                    f"حجم الشبكة الكلي: {m(f'{cols} \\times {rows} = {tot}')} بلاطة، والمطلوب تلوينه: {m(f'\\frac{{{p}}}{{{q}}} \\times {tot} = {goal}')} بلاطة.",
                    f"البلاطات الملوّنة حاليًا: {m(f'{shaded} + {extra} = {colored}')} بلاطة.",
                    f"عدد البلاطات البيضاء التي يجب تلوينها: {m(f'{goal} - {colored} = {ans}')}.",
                ],
                f"تحقق: {m(f'{colored} + {ans} = {goal}')}، و{m(f'\\frac{{{goal}}}{{{tot}}} = \\frac{{{p}}}{{{q}}}')}.",
            )

        elif mode == "more_purple_only":
            p, q = target
            goal = (tot * p) // q
            ans = goal - shaded
            assert tot - shaded - extra >= ans
            q_en = (
                f"In the {m(cols)}-by-{m(rows)} {ctx_en} shown, {m(shaded)} squares are purple, {m(extra)} squares are sky-blue, and the rest are white. "
                f"How many **white** squares must be painted purple so that **purple squares alone** form {m(f'\\frac{{{p}}}{{{q}}}')} of the entire grid?"
            )
            q_ar = (
                f"في {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} الموضّحة، توجد {m(shaded)} مربعات بنفسجية و{m(extra)} مربعات زرقاء فاتحة والباقي أبيض. "
                f"كم مربعًا **أبيض** يجب طلاؤه بالبنفسجي لكي تشكّل **المربعات البنفسجية وحدها** {m(f'\\frac{{{p}}}{{{q}}}')} من الشبكة كلها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [goal - (shaded + extra), goal, tot - shaded - extra, ans + 3], qid
            )
            hint_en = "Read carefully: sky-blue squares do NOT count as purple! Compare the target purple count directly with the current 8 purple squares."
            hint_ar = "اقرأ بعناية: المربعات الزرقاء لا تُحسب ضمن البنفسجية! قارن العدد المطلوب للبنفسجي بعدد المربعات البنفسجية الحالي فقط."
            sol_en = explain_en(
                "Watch out for the extra-info trap: sky-blue squares are **not** purple, so only the {0} purple squares count toward our goal!".format(shaded),
                [
                    f"Total squares in the grid: {m(f'{cols} \\times {rows} = {tot}')}.",
                    f"Target purple squares: {m(f'\\frac{{{p}}}{{{q}}} \\times {tot} = {goal}')}.",
                    f"Since {m(shaded)} squares are purple right now (and there are {m(tot - shaded - extra)} white squares available), paint {m(f'{goal} - {shaded} = {ans}')} white squares purple.",
                ],
                f"Check: {m(f'{shaded} + {ans} = {goal}')} purple squares out of {m(tot)}, which simplifies to {m(f'\\frac{{{p}}}{{{q}}}')}!",
            )
            sol_ar = explain_ar(
                "انتبه لفخ المعطيات الزائدة: المربعات الزرقاء **ليست** بنفسجية، لذا نحسب ما ينقصنا فوق المربعات البنفسجية الحالية فقط!",
                [
                    f"العدد الكلي للمربعات: {m(f'{cols} \\times {rows} = {tot}')} مربعًا.",
                    f"عدد المربعات البنفسجية المطلوب: {m(f'\\frac{{{p}}}{{{q}}} \\times {tot} = {goal}')} مربعًا.",
                    f"لدينا {m(shaded)} مربعات بنفسجية حاليًا (ويوجد {m(tot - shaded - extra)} مربعًا أبيض متاحًا)، إذن نطلي {m(f'{goal} - {shaded} = {ans}')} مربعات بيضاء بالبنفسجي.",
                ],
                f"تحقق: {m(f'{shaded} + {ans} = {goal}')} مربعًا بنفسجيًا من أصل {m(tot)} أي {m(f'\\frac{{{p}}}{{{q}}}')}.",
            )

        else:  # blue_of_nonpurple
            non_purple = tot - shaded
            ans = Fraction(extra, non_purple)
            q_en = (
                f"A {m(cols)}-by-{m(rows)} {ctx_en} has {m(shaded)} purple cells, {m(extra)} sky-blue cells, and the remaining cells white, as shown. "
                f"What **simplified fraction** of the **non-purple** cells are colored sky-blue?"
            )
            q_ar = (
                f"تحتوي {ctx_ar} ذات الأبعاد {m(cols)} في {m(rows)} على {m(shaded)} مربعات بنفسجية و{m(extra)} مربعات زرقاء فاتحة والباقي أبيض كما في الشكل. "
                f"ما **الكسر في أبسط صورة** الذي تمثّله المربعات الزرقاء الفاتحة من بين المربعات **غير البنفسجية**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    Fraction(extra, tot),
                    Fraction(extra, non_purple - extra),
                    Fraction(shaded, tot),
                    Fraction(extra + 2, non_purple),
                ],
                qid,
            )
            hint_en = "The denominator is NOT the whole grid — first subtract the purple cells to find how many non-purple cells exist!"
            hint_ar = "المقام هنا ليس الشبكة كلها — اطرح المربعات البنفسجية أولًا لمعرفة عدد المربعات غير البنفسجية!"
            sol_en = explain_en(
                "'Of the non-purple cells' tells us the **new whole (denominator)** is only the cells that are NOT purple!",
                [
                    f"Total cells: {m(f'{cols} \\times {rows} = {tot}')}. Non-purple cells: {m(f'{tot} - {shaded} = {non_purple}')}.",
                    f"Out of those {m(non_purple)} non-purple cells, {m(extra)} are sky-blue.",
                    f"Simplify the fraction: {m(f'\\frac{{{extra}}}{{{non_purple}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
                ],
                f"Check: {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {non_purple} = {extra}')} sky-blue cells!",
            )
            sol_ar = explain_ar(
                "عبارة «من بين المربعات غير البنفسجية» تعني أن **المقام الجديد** هو عدد المربعات غير البنفسجية فقط!",
                [
                    f"إجمالي المربعات {m(f'{cols} \\times {rows} = {tot}')}، فغير البنفسجية عددها {m(f'{tot} - {shaded} = {non_purple}')}.",
                    f"من بين هذه الـ {m(non_purple)} مربعًا، يوجد {m(extra)} مربعات زرقاء فاتحة.",
                    f"نبسّط الكسر: {m(f'\\frac{{{extra}}}{{{non_purple}}} = \\frac{{{ans.numerator}}}{{{ans.denominator}}}')}.",
                ],
                f"تحقق: {m(f'\\frac{{{ans.numerator}}}{{{ans.denominator}}} \\times {non_purple} = {extra}')} مربعات زرقاء.",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-visual-fraction-grid",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 2. g67-bundle-promo-discount (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    promo_cases = [
        # (N, M, price, val, mode, diff, item_en, item_ar, shop_en, shop_ar)
        (3, 1, 12, 8, "cost_k", "Easy", "notebooks", "دفترًا", "campus bookstore", "مكتبة الحرم الجامعي"),
        (2, 1, 15, 10, "cost_k", "Easy", "fruit smoothies", "كوب عصير", "juice kiosk", "كشك العصائر"),
        (4, 1, 10, 12, "cost_k", "Easy", "sketchpad packs", "كراسة رسم", "art supply shop", "متجر أدوات الرسم"),
        (3, 2, 8, 16, "cost_k", "Easy", "granola bars", "قطعة شوفان", "school canteen", "مقصف المدرسة"),
        (5, 1, 6, 20, "cost_k", "Easy", "gel pens", "قلم حبر", "stationery store", "قرطاسية الحي"),
        (4, 2, 9, 15, "cost_k", "Easy", "mini puzzles", "أحجية صغيرة", "toy corner", "ركن الألعاب"),
        (3, 1, 10, 100, "max_items", "Medium", "storybooks", "قصص", "book fair stall", "جناح معرض الكتاب"),
        (2, 1, 8, 90, "max_items", "Medium", "muffins", "كعكات", "bakery counter", "مخبز الحي"),
        (4, 1, 12, 175, "max_items", "Medium", "geometry sets", "علب هندسة", "student co-op", "تعاونية الطلاب"),
        (3, 2, 7, 80, "max_items", "Medium", "juice cartons", "علب عصير", "supermarket", "المتجر التمويني"),
        (5, 2, 6, 100, "max_items", "Medium", "highlighters", "أقلام تظليل", "office shop", "متجر المكتبيات"),
        (4, 2, 15, 200, "max_items", "Medium", "sports socks", "جوارب رياضية", "sports outlet", "متجر الرياضة"),
        (3, 1, 9, 130, "max_items", "Medium", "yogurt cups", "علب زبادي", "dairy shop", "متجر الألبان"),
        (3, 1, 20, 4, "eff_pct_full", "Hard", "science magazines", "مجلات علمية", "reading club", "نادي القراءة"),
        (4, 1, 25, 5, "eff_pct_full", "Hard", "board markers", "أقلام سبورة", "teacher store", "متجر المعلم"),
        (3, 2, 18, 5, "eff_pct_full", "Hard", "honey jars", "عبوات عسل", "farmers market", "سوق المزارعين"),
        (3, 1, 15, 10, "eff_pct_partial", "Hard", "graph notebooks", "دفاتر مربعات", "stationery center", "مركز القرطاسية"),
    ]
    for N, M, price, val, mode, diff, item_en, item_ar, shop_en, shop_ar in promo_cases:
        qid = next_id()
        bundle = N + M

        if mode == "cost_k":
            K = val
            q_cnt, rem = divmod(K, bundle)
            assert rem < N
            paid = q_cnt * N + rem
            ans = paid * price
            q_en = (
                f"A {shop_en} sells {item_en} for {m(price)} riyals each with a special offer: "
                f"**\"Buy {m(N)}, get {m(M)} free.\"** How many riyals does it cost to take home **exactly** {m(K)} {item_en}?"
            )
            q_ar = (
                f"يبيع {shop_ar} القطعة الواحدة بسعر {m(price)} ريالات مع عرض خاص: "
                f"**«اشترِ {m(N)} واحصل على {m(M)} مجانًا»**. كم ريالًا يدفع المشتري ليحصل على {m(K)} {item_ar} بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    K * price,
                    (K - M) * price,
                    (paid + 1) * price,
                    max(price, (paid - 1) * price),
                ],
                qid,
            )
            hint_en = f"Group the {K} items into packs of {N} + {M} = {bundle}. Each full pack of {bundle} only costs the price of {N} items!"
            hint_ar = f"قسّم الـ {K} قطعة إلى مجموعات من {N} + {M} = {bundle}. كل مجموعة كاملة تكلف ثمن {N} قطع فقط!"
            sol_en = explain_en(
                f"Under **\"Buy {m(N)}, get {m(M)} free\"**, every bundle of {m(f'{N} + {M} = {bundle}')} items only requires paying for {m(N)} items!",
                [
                    f"Divide {m(K)} into bundles of {m(bundle)}: {m(f'{K} = {q_cnt} \\times {bundle} + {rem}')} leftover item(s).",
                    f"Number of items you actually pay for: {m(f'{q_cnt} \\times {N} + {rem} = {paid}')} items (the other {m(K - paid)} are free).",
                    f"Multiply by {m(price)} riyals per item: {m(f'{paid} \\times {price} = {ans}')} riyals.",
                ],
                f"Check: paying for {m(paid)} items earns {m(f'({paid} \\div {N}) \\text{{ floor}} \\times {M} = {q_cnt * M}')} free items, giving {m(f'{paid} + {q_cnt * M} = {K}')} items!",
            )
            sol_ar = explain_ar(
                f"في عرض **«اشترِ {m(N)} واحصل على {m(M)} مجانًا»**، كل حزمة من {m(f'{N} + {M} = {bundle}')} قطع ندفع فيها ثمن {m(N)} قطع فقط!",
                [
                    f"نقسّم الـ {m(K)} إلى حزم من {m(bundle)}: {m(f'{K} = {q_cnt} \\times {bundle} + {rem}')}.",
                    f"عدد القطع المدفوعة فعليًا: {m(f'{q_cnt} \\times {N} + {rem} = {paid}')} قطعة (والقطع الـ {m(K - paid)} الباقية مجانية).",
                    f"التكلفة الكلية: {m(f'{paid} \\times {price} = {ans}')} ريالًا.",
                ],
                f"تحقق: دفع ثمن {m(paid)} قطعة يمنح {m(q_cnt * M)} مجانية، والمجموع {m(f'{paid} + {q_cnt * M} = {K}')}.",
            )

        elif mode == "max_items":
            budget = val
            paid = budget // price
            free = (paid // N) * M
            ans = paid + free
            trap_div_bundle = paid + (paid // bundle) * M
            q_en = (
                f"At a {shop_en}, {item_en} cost {m(price)} riyals each under the promotion **\"Buy {m(N)}, get {m(M)} free.\"** "
                f"What is the **maximum** total number of {item_en} (including free ones) a student can get with {m(budget)} riyals?"
            )
            q_ar = (
                f"في {shop_ar}، تُباع {item_ar} بسعر {m(price)} ريالات للواحدة ضمن عرض **«اشترِ {m(N)} واحصل على {m(M)} مجانًا»**. "
                f"ما **أكبر** عدد كلي من {item_ar} (شاملًا المجانية) يمكن لطالب الحصول عليه بمبلغ {m(budget)} ريالًا؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    paid,
                    trap_div_bundle if trap_div_bundle != ans else ans - 1,
                    ans + M,
                    ans + 1,
                ],
                qid,
            )
            hint_en = f"First find how many items {budget} riyals can buy at {price} riyals each; then every {N} paid items earn {M} bonus items!"
            hint_ar = f"احسب أولًا كم قطعة يمكنك شراؤها بمبلغ {budget} ريالًا، ثم تذكّر أن كل {N} قطع مدفوعة تمنحك {M} مجانًا!"
            sol_en = explain_en(
                "Count the **paid items** your budget affords first, then count how many **groups of {0}** are inside those paid items!".format(N),
                [
                    f"How many items can {m(budget)} riyals pay for? {m(f'{budget} \\div {price} = {paid}')} paid items (with {m(budget % price)} riyal(s) left over).",
                    f"Group the {m(paid)} paid items into sets of {m(N)}: {m(f'{paid} \\div {N} = {paid // N}')} full sets (remainder {m(paid % N)}).",
                    f"Each full set gives {m(M)} free item(s): {m(f'{paid // N} \\times {M} = {free}')} free items. Total = {m(f'{paid} + {free} = {ans}')}!",
                ],
                f"Common trap: divide paid items by {m(N)} (NOT by {m(bundle)}) to count the free bonuses!",
            )
            sol_ar = explain_ar(
                "نحسب **عدد القطع المدفوعة** التي يكفيها المبلغ أولًا، ثم نعدّ كم مجموعة من {0} توجد داخلها!".format(N),
                [
                    f"عدد القطع التي يمكن دفع ثمنها: {m(f'{budget} \\div {price} = {paid}')} قطعة (ويتبقى {m(budget % price)} ريالات لا تكفي لقطعة أخرى).",
                    f"عدد المجموعات الكاملة من {m(N)} داخل الـ {m(paid)} قطعة مدفوعة هو {m(paid // N)} مجموعات.",
                    f"القطع المجانية = {m(f'{paid // N} \\times {M} = {free}')}، إذن الإجمالي الأقصى = {m(f'{paid} + {free} = {ans}')}.",
                ],
                f"تنبيه مهم: نقسم القطع المدفوعة على {m(N)} (وليس على {m(bundle)}) لحساب الهدايا المجانية!",
            )

        elif mode == "eff_pct_full":
            assert (M * 100) % bundle == 0
            ans = (M * 100) // bundle
            wrong_pct = round(M * 100 / N)
            q_en = (
                f"A {shop_en} runs a **\"Buy {m(N)}, get {m(M)} free\"** offer on identical {item_en} (priced at {m(price)} riyals each). "
                f"If a customer takes {m(bundle)} {item_en} using this offer, what **effective percentage discount** off the regular price of {m(bundle)} items did they receive?"
            )
            q_ar = (
                f"يقدّم {shop_ar} عرض **«اشترِ {m(N)} واحصل على {m(M)} مجانًا»** على {item_ar} متماثلة (سعر الواحدة {m(price)} ريالًا). "
                f"إذا أخذ زبون {m(bundle)} منها مستفيدًا من العرض، فما **نسبة الخصم الفعلية** التي حصل عليها مقارنة بالسعر الأصلي للـ {m(bundle)} قطع؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [wrong_pct, 100 - ans, ans + 5, max(5, ans - 10)], qid, suffix="\\%"
            )
            hint_en = f"You take home {N} + {M} = {bundle} items in total, and {M} of those {bundle} items are free! Write {M}/{bundle} as a percentage."
            hint_ar = f"أنت تأخذ {N} + {M} = {bundle} قطع في المجموع، ومنها {M} مجانية! حوّل الكسر {M}/{bundle} إلى نسبة مئوية."
            sol_en = explain_en(
                f"Never divide {m(M)} by {m(N)}! Percentage discount compares what you **save** to the **regular value of all {m(bundle)} items you take home**.",
                [
                    f"Regular value of {m(bundle)} items: {m(f'{bundle} \\times {price} = {bundle * price}')} riyals.",
                    f"Amount saved ({m(M)} free item(s)): {m(f'{M} \\times {price} = {M * price}')} riyals.",
                    f"Effective discount: {m(f'\\frac{{{M * price}}}{{{bundle * price}}} \\times 100\\% = \\frac{{{M}}}{{{bundle}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"Quick shortcut: {m(M)} free out of {m(f'{N} + {M} = {bundle}')} items taken home is always {m(f'\\frac{{{M}}}{{{bundle}}} = {ans}\\%')}!",
            )
            sol_ar = explain_ar(
                f"لا تقسم {m(M)} على {m(N)}! نسبة الخصم تقاس بقسمة **قيمة التوفير** على **السعر الأصلي لجميع القطع الـ {m(bundle)} المستلمة**.",
                [
                    f"السعر الأصلي لـ {m(bundle)} قطع هو {m(f'{bundle} \\times {price} = {bundle * price}')} ريالًا.",
                    f"مقدار التوفير ({m(M)} مجانًا) هو {m(f'{M} \\times {price} = {M * price}')} ريالًا.",
                    f"نسبة الخصم الفعلية: {m(f'\\frac{{{M}}}{{{bundle}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"قاعدة سريعة: {m(M)} مجانًا من أصل {m(bundle)} قطع مستلمة تعادل دائمًا {m(f'\\frac{{{M}}}{{{bundle}}} = {ans}\\%')}!",
            )

        else:  # eff_pct_partial
            K = val
            q_cnt, rem = divmod(K, bundle)
            paid = q_cnt * N + rem
            reg = K * price
            act = paid * price
            saved = reg - act
            assert (saved * 100) % reg == 0
            ans = (saved * 100) // reg
            q_en = (
                f"A {shop_en} sells {item_en} at {m(price)} riyals each under **\"Buy {m(N)}, get {m(M)} free.\"** "
                f"Rami needs **exactly** {m(K)} {item_en}. What overall **percentage discount** does he save compared to paying full price for all {m(K)} {item_en}?"
            )
            q_ar = (
                f"يبيع {shop_ar} دفاتر المربعات بسعر {m(price)} ريالًا للدفتر ضمن عرض **«اشترِ {m(N)} واحصل على {m(M)} مجانًا»**. "
                f"يحتاج رامي إلى {m(K)} دفاتر بالضبط. ما **نسبة الخصم الإجمالية** التي يوفرها مقارنة بالسعر الأصلي للـ {m(K)} دفاتر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [25, 30, 15, 10], qid, suffix="\\%"
            )
            hint_en = f"Out of {K} notebooks, find how many free ones Rami earns, then divide (free notebooks ÷ {K}) × 100%."
            hint_ar = f"من بين الـ {K} دفاتر، احسب كم دفترًا مجانيًا يحصل عليه رامي، ثم اقسم (المجاني ÷ {K}) × 100%."
            sol_en = explain_en(
                f"Because {m(K)} is not a multiple of {m(bundle)}, the leftover {m(rem)} notebooks get no discount—so compute total free items divided by {m(K)}!",
                [
                    f"Group {m(K)} into bundles of {m(bundle)}: {m(f'{K} = {q_cnt} \\times {bundle} + {rem}')}. Rami gets {m(q_cnt * M)} free notebooks and pays for {m(paid)}.",
                    f"Regular cost of {m(K)} notebooks: {m(f'{K} \\times {price} = {reg}')} riyals; Rami pays {m(f'{paid} \\times {price} = {act}')} riyals, saving {m(saved)} riyals.",
                    f"Overall percentage discount: {m(f'\\frac{{{saved}}}{{{reg}}} \\times 100\\% = \\frac{{{q_cnt * M}}}{{{K}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"Notice: {m(f'{ans}\\%')} is slightly less than the full-bundle {m('25\\%')} because the last {m(rem)} notebooks were bought at full price!",
            )
            sol_ar = explain_ar(
                f"لأن {m(K)} ليس مضاعفًا للعدد {m(bundle)}، فإن الدفترين الإضافيين يُشتريان بالسعر الكامل—لذا نقسم إجمالي المجاني على {m(K)}!",
                [
                    f"نقسّم {m(K)} إلى حزم من {m(bundle)}: {m(f'{K} = {q_cnt} \\times {bundle} + {rem}')}، فيحصل رامي على {m(q_cnt * M)} مجانًا ويدفع ثمن {m(paid)} دفاتر.",
                    f"السعر الأصلي {m(reg)} ريالًا، والمدفوع {m(act)} ريالًا، أي وفّر {m(saved)} ريالًا.",
                    f"نسبة الخصم الإجمالية: {m(f'\\frac{{{saved}}}{{{reg}}} \\times 100\\% = {ans}\\%')}.",
                ],
                f"تحقق: {m(q_cnt * M)} مجانًا من أصل {m(K)} تساوي {m(f'\\frac{{{q_cnt * M}}}{{{K}}} = {ans}\\%')}.",
            )

        if mode == "cost_k":
            sub_en = f"Take {val} items → Cost = ?"
            sub_ar = f"شراء {val} قطع ← التكلفة = ؟"
        elif mode == "max_items":
            sub_en = f"Budget {val} riyals → Max = ?"
            sub_ar = f"مبلغ {val} ريال ← الأقصى = ؟"
        elif mode == "eff_pct_full":
            sub_en = f"Take {bundle} items → Discount = ?%"
            sub_ar = f"أخذ {bundle} قطع ← الخصم = ؟%"
        else:
            sub_en = f"Take {val} items → Discount = ?%"
            sub_ar = f"أخذ {val} قطع ← الخصم = ؟%"
        svg_en = svg_tape_bar_split(
            [(N, f"Pay {N}"), (M, f"Free {M} (?)")],
            total_lbl=f"Buy {N}, Free {M} ({price} ea.)",
            sub_lbl=sub_en,
        )
        svg_ar = svg_tape_bar_split(
            [(N, f"ادفع {N}"), (M, f"مجانًا {M} (؟)")],
            total_lbl=f"اشترِ {N} + {M} مجانًا ({price} ريال)",
            sub_lbl=sub_ar,
        )
        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-bundle-promo-discount",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # -------------------------------------------------------------------------
    # 3. g67-two-jar-transfer (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    jar_cases = [
        # (va, vb, p, q, mode, diff, liq_en, liq_ar)
        (600, 250, 1, 3, "vol_b", "Easy", "orange juice", "عصير البرتقال"),
        (800, 300, 1, 4, "vol_b", "Easy", "apple cider", "عصير التفاح"),
        (750, 180, 2, 5, "vol_b", "Easy", "lemonade", "عصير الليمون"),
        (900, 350, 1, 6, "vol_b", "Easy", "berry nectar", "رحيق التوت"),
        (640, 220, 3, 8, "vol_b", "Easy", "mango juice", "عصير المانجو"),
        (600, 200, 1, 3, "ratio_ab", "Medium", "water", "الماء"),
        (720, 240, 1, 4, "ratio_ab", "Medium", "milk", "الحليب"),
        (500, 300, 2, 5, "ratio_ab", "Medium", "iced tea", "الشاي المثلج"),
        (840, 260, 2, 7, "ratio_ab", "Medium", "grape juice", "عصير العنب"),
        (450, 250, 1, 3, "ratio_ab", "Medium", "pomegranate juice", "عصير الرمان"),
        (320, 600, 1, 5, "ratio_ba", "Medium", "rose syrup", "شراب الورد"),
        (250, 750, 1, 5, "ratio_ba", "Medium", "olive oil", "زيت الزيتون"),
        (600, 200, 1, 3, "double_4", "Hard", "distilled water", "الماء المقطر"),
        (540, 180, 1, 3, "double_6", "Hard", "peach juice", "عصير الخوخ"),
        (360, 360, 1, 4, "back_equal", "Hard", "mint lemonade", "ليمون بالنعناع"),
        (400, 400, 1, 5, "back_equal", "Hard", "pineapple juice", "عصير الأناناس"),
    ]
    for va, vb, p, q, mode, diff, liq_en, liq_ar in jar_cases:
        qid = next_id()
        cap = max(va, vb, 900)

        if mode == "vol_b":
            poured = (va * p) // q
            ans = vb + poured
            svg_en = svg_two_jars(f"A ({va} mL)", va / cap, f"B ({vb} mL)", vb / cap, f"{p}/{q} of A")
            svg_ar = svg_two_jars(f"أ ({va} مل)", va / cap, f"ب ({vb} مل)", vb / cap, f"{p}/{q} من أ")
            q_en = (
                f"Jar A contains {m(va)} mL of {liq_en} and Jar B contains {m(vb)} mL. "
                f"If {m(f'\\frac{{{p}}}{{{q}}}')} of the {liq_en} in Jar A is poured into Jar B, how many milliliters are now in **Jar B**?"
            )
            q_ar = (
                f"يحتوي الوعاء (أ) على {m(va)} مل من {liq_ar}، ويحتوي الوعاء (ب) على {m(vb)} مل. "
                f"إذا سكبنا {m(f'\\frac{{{p}}}{{{q}}}')} ما في الوعاء (أ) إلى الوعاء (ب)، فكم مليلترًا يصبح في **الوعاء (ب)**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [va - poured, poured, vb + (vb * p) // q, ans + 50], qid
            )
            hint_en = f"Calculate {p}/{q} of {va} mL to find the poured amount, then add it to {vb} mL."
            hint_ar = f"احسب {p}/{q} من {va} مل لمعرفة الكمية المسكوبة، ثم أضفها إلى {vb} مل."
            sol_en = explain_en(
                "Find the exact milliliters poured out of Jar A first, then add that amount to Jar B!",
                [
                    f"Amount poured from Jar A: {m(f'\\frac{{{p}}}{{{q}}} \\times {va} = {poured}')} mL.",
                    f"Add to Jar B's initial volume: {m(f'{vb} + {poured} = {ans}')} mL.",
                ],
                f"Total liquid conservation check: Jar A now has {m(va - poured)} mL and Jar B has {m(ans)} mL; {m(f'{va - poured} + {ans} = {va + vb}')} mL!",
            )
            sol_ar = explain_ar(
                "نحسب كمية السائل المسكوبة من الوعاء (أ) أولًا، ثم نضيفها إلى كمية الوعاء (ب) الابتدائية!",
                [
                    f"الكمية المسكوبة من (أ): {m(f'\\frac{{{p}}}{{{q}}} \\times {va} = {poured}')} مل.",
                    f"الكمية الجديدة في (ب): {m(f'{vb} + {poured} = {ans}')} مل.",
                ],
                f"تحقق بحفظ المجموع الكلي: بقي في (أ) {m(va - poured)} مل وفي (ب) {m(ans)} مل، ومجموعهما {m(va + vb)} مل كما بدأنا!",
            )

        elif mode in ("ratio_ab", "ratio_ba"):
            if mode == "ratio_ab":
                poured = (va * p) // q
                na, nb = va - poured, vb + poured
                svg_en = svg_two_jars(f"A ({va} mL)", va / cap, f"B ({vb} mL)", vb / cap, f"{p}/{q} of A")
                svg_ar = svg_two_jars(f"أ ({va} مل)", va / cap, f"ب ({vb} مل)", vb / cap, f"{p}/{q} من أ")
                act_en = f"{m(f'\\frac{{{p}}}{{{q}}}')} of the liquid in Jar A is poured into Jar B"
                act_ar = f"سكبنا {m(f'\\frac{{{p}}}{{{q}}}')} ما في الوعاء (أ) إلى الوعاء (ب)"
            else:
                poured = (vb * p) // q
                na, nb = va + poured, vb - poured
                svg_en = svg_two_jars(f"A ({va} mL)", va / cap, f"B ({vb} mL)", vb / cap, "")
                svg_ar = svg_two_jars(f"أ ({va} مل)", va / cap, f"ب ({vb} مل)", vb / cap, "")
                act_en = f"{m(f'\\frac{{{p}}}{{{q}}}')} of the liquid in Jar B is poured into Jar A"
                act_ar = f"سكبنا {m(f'\\frac{{{p}}}{{{q}}}')} ما في الوعاء (ب) إلى الوعاء (أ)"
            g = math.gcd(na, nb)
            ra, rb = na // g, nb // g
            ans_str = f"{ra} : {rb}"
            g0 = math.gcd(va, vb)
            distractors = [
                f"{rb} : {ra}" if rb != ra else "2 : 1",
                f"{va // g0} : {vb // g0}",
                f"{ra + 1} : {rb}",
                f"{ra} : {rb + 1}",
                f"{ra + 1} : {rb + 2}",
            ]
            q_en = (
                f"Jar A starts with {m(va)} mL of {liq_en} and Jar B starts with {m(vb)} mL. "
                f"After {act_en}, what is the **simplified ratio** of the volume in Jar A to the volume in Jar B?"
            )
            q_ar = (
                f"في البداية يحتوي الوعاء (أ) على {m(va)} مل من {liq_ar} والوعاء (ب) على {m(vb)} مل. "
                f"بعد أن {act_ar}، ما **النسبة في أبسط صورة** بين حجم السائل في (أ) إلى حجمه في (ب)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans_str, distractors, qid)
            hint_en = "Update BOTH jars (subtract from the giver, add to the receiver!) before simplifying the ratio A : B."
            hint_ar = "حدّث حجم كلا الوعاءين (اطرح من المانح وأضف إلى المستقبِل!) قبل تبسيط النسبة أ : ب."
            sol_en = explain_en(
                "Track both jars carefully: whatever leaves one jar enters the other, keeping the total volume constant!",
                [
                    f"Transferred volume: {m(f'{poured}')} mL.",
                    f"New volumes: Jar A has {m(na)} mL and Jar B has {m(nb)} mL.",
                    f"Divide both terms of {m(f'{na} : {nb}')} by their greatest common factor {m(g)} to get {m(f'{ra} : {rb}')}.",
                ],
                f"Check: {m(f'{na} + {nb} = {va + vb}')} mL total, and {m(f'{na} \\div {g} = {ra}')}, {m(f'{nb} \\div {g} = {rb}')}.",
            )
            sol_ar = explain_ar(
                "نتتبّع الوعاءين معًا: الكمية المطروحة من أحدهما تُضاف كاملة إلى الآخر بحيث يبقى المجموع ثابتًا!",
                [
                    f"الكمية المنقولة تساوي {m(poured)} مل.",
                    f"الحجمان الجديدان: في (أ) {m(na)} مل، وفي (ب) {m(nb)} مل.",
                    f"نبسّط النسبة {m(f'{na} : {nb}')} بالقسمة على القاسم المشترك الأكبر {m(g)} فنحصل على {m(f'{ra} : {rb}')}.",
                ],
                f"تحقق: المجموع {m(f'{na} + {nb} = {va + vb}')} مل لم يتغير، وأبسط صورة هي {m(f'{ra} : {rb}')}.",
            )

        elif mode.startswith("double_"):
            q2 = int(mode.split("_")[1])
            p1 = (va * p) // q
            mid_a, mid_b = va - p1, vb + p1
            p2 = mid_b // q2
            ans = mid_a + p2
            svg_en = svg_two_jars(f"A ({va} mL)", va / cap, f"B ({vb} mL)", vb / cap, "")
            svg_ar = svg_two_jars(f"أ ({va} مل)", va / cap, f"ب ({vb} مل)", vb / cap, "")
            q_en = (
                f"Jar A holds {m(va)} mL of {liq_en} and Jar B holds {m(vb)} mL. First, {m(f'\\frac{{{p}}}{{{q}}}')} of Jar A is poured into Jar B. "
                f"Next, {m(f'\\frac{{1}}{{{q2}}}')} of the **new** total in Jar B is poured back into Jar A. How many milliliters end up in **Jar A**?"
            )
            q_ar = (
                f"يحتوي الوعاء (أ) على {m(va)} مل من {liq_ar} والوعاء (ب) على {m(vb)} مل. سُكب أولًا {m(f'\\frac{{{p}}}{{{q}}}')} ما في (أ) إلى (ب)، "
                f"ثم سُكب {m(f'\\frac{{1}}{{{q2}}}')} الكمية **الجديدة** في (ب) عائدًا إلى (أ). كم مليلترًا يصبح في **الوعاء (أ)** في النهاية؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [mid_a, mid_b - p2, mid_a + vb // q2, va], qid
            )
            hint_en = "Do the two pours one step at a time! Make sure the second fraction is taken from Jar B's NEW volume, not its starting volume."
            hint_ar = "نفّذ عمليتي السكب خطوة بخطوة! انتبه إلى أن الكسر الثاني يُحسب من كمية (ب) الجديدة وليس الابتدائية."
            sol_en = explain_en(
                "Make a mini state table after Pour 1 and after Pour 2 so you never mix up old and new volumes!",
                [
                    f"**Pour 1:** {m(f'\\frac{{{p}}}{{{q}}} \\times {va} = {p1}')} mL moves A → B. Now Jar A = {m(mid_a)} mL and Jar B = {m(f'{vb} + {p1} = {mid_b}')} mL.",
                    f"**Pour 2:** {m(f'\\frac{{1}}{{{q2}}} \\times {mid_b} = {p2}')} mL moves B → A.",
                    f"Final Jar A volume: {m(f'{mid_a} + {p2} = {ans}')} mL (and Jar B has {m(mid_b - p2)} mL).",
                ],
                f"Total check: {m(f'{ans} + {mid_b - p2} = {va + vb}')} mL, matching {m(f'{va} + {vb}')} mL!",
            )
            sol_ar = explain_ar(
                "نسجّل الكميتين بعد كل خطوة سكب حتى لا نخلط بين الحجم القديم والحجم الجديد!",
                [
                    f"**السكب الأول:** ينتقل {m(f'\\frac{{{p}}}{{{q}}} \\times {va} = {p1}')} مل من (أ) إلى (ب)، فيصبح في (أ) {m(mid_a)} مل وفي (ب) {m(mid_b)} مل.",
                    f"**السكب الثاني:** ينتقل {m(f'\\frac{{1}}{{{q2}}} \\times {mid_b} = {p2}')} مل من (ب) عائدًا إلى (أ).",
                    f"الكمية النهائية في (أ): {m(f'{mid_a} + {p2} = {ans}')} مل.",
                ],
                f"تحقق: {m(f'{ans} + {mid_b - p2} = {va + vb}')} مل، وهو نفس المجموع الأصلي تمامًا!",
            )

        else:  # back_equal: after pouring 1/q of A into B, both equal `va`
            final_v = va
            assert (final_v * q) % (q - p) == 0
            orig_a = (final_v * q) // (q - p)
            poured = orig_a - final_v
            ans = final_v - poured
            svg_en = svg_two_jars("A (? mL)", 0.78, "B (? mL)", 0.42, f"{p}/{q} of A")
            svg_ar = svg_two_jars("أ (؟ مل)", 0.78, "ب (؟ مل)", 0.42, f"{p}/{q} من أ")
            q_en = (
                f"After pouring {m(f'\\frac{{{p}}}{{{q}}}')} of the {liq_en} from Jar A into Jar B, "
                f"**both** jars end up holding **exactly** {m(final_v)} mL each! How many milliliters were in **Jar B originally**?"
            )
            q_ar = (
                f"بعد سكب {m(f'\\frac{{{p}}}{{{q}}}')} كمية {liq_ar} من الوعاء (أ) إلى الوعاء (ب)، "
                f"أصبح في **كل** من الوعاءين {m(final_v)} مل بالضبط! كم مليلترًا كان في **الوعاء (ب) في البداية**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    final_v - final_v // q,
                    orig_a,
                    poured,
                    ans + 40,
                ],
                qid,
            )
            hint_en = f"Jar A kept {q - p}/{q} of its original liquid, and that remaining part equals {final_v} mL! Find original Jar A first."
            hint_ar = f"بقي في الوعاء (أ) كسر قدره {q - p}/{q} من كميته الأصلية وهو يساوي {final_v} مل! أوجد كمية (أ) الأصلية أولًا."
            sol_en = explain_en(
                f"Work backwards from Jar A! Pouring away {m(f'\\frac{{{p}}}{{{q}}}')} of Jar A leaves {m(f'\\frac{{{q - p}}}{{{q}}}')} of Jar A.",
                [
                    f"Since {m(f'\\frac{{{q - p}}}{{{q}}}')} of Jar A equals {m(final_v)} mL, 1 part is {m(f'{final_v} \\div {q - p} = {final_v // (q - p)}')} mL, and original Jar A had {m(f'{q} \\times {final_v // (q - p)} = {orig_a}')} mL.",
                    f"So the amount poured into Jar B was {m(f'{orig_a} - {final_v} = {poured}')} mL.",
                    f"Because Jar B ended at {m(final_v)} mL after receiving {m(poured)} mL, it started with {m(f'{final_v} - {poured} = {ans}')} mL!",
                ],
                f"Forward check: {m(f'\\frac{{{p}}}{{{q}}} \\times {orig_a} = {poured}')} mL; A becomes {m(f'{orig_a} - {poured} = {final_v}')} mL and B becomes {m(f'{ans} + {poured} = {final_v}')} mL!",
            )
            sol_ar = explain_ar(
                f"نعمل عكسيًا بدءًا من الوعاء (أ)! بعد سكب {m(f'\\frac{{{p}}}{{{q}}}')} منه يتبقى فيه {m(f'\\frac{{{q - p}}}{{{q}}}')} من كميته الأصلية.",
                [
                    f"بما أن {m(f'\\frac{{{q - p}}}{{{q}}}')} من (أ) يساوي {m(final_v)} مل، فإن الحصة الواحدة = {m(final_v // (q - p))} مل، وكمية (أ) الأصلية = {m(orig_a)} مل.",
                    f"إذن الكمية التي سُكبت إلى (ب) هي {m(f'{orig_a} - {final_v} = {poured}')} مل.",
                    f"وبما أن (ب) وصل إلى {m(final_v)} مل بعد إضافة {m(poured)} مل، فقد كان فيه أصلًا {m(f'{final_v} - {poured} = {ans}')} مل!",
                ],
                f"تحقق للأمام: سكب {m(poured)} مل من {m(orig_a)} يترك {m(final_v)} مل، وإضافتها إلى {m(ans)} تعطي {m(final_v)} مل!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-two-jar-transfer",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(items) == 50
    return items


def _gen_group_1_2(next_id) -> list[dict]:
    """Lesson 1.2 group (50 Qs, Topic: 'Number Theory'):
    4. g67-digital-clock-palindromes (17 Qs)
    5. g67-venn-two-clubs (17 Qs)
    6. g67-missing-digit-div-346 (16 Qs)
    """
    items: list[dict] = []

    def _is_pal_min(t_min: int) -> bool:
        h, mm = divmod(t_min % 1440, 60)
        s = f"{h:02d}{mm:02d}"
        return s == s[::-1]

    def _str_to_min(ts: str) -> int:
        hh, mm = ts.split(":")
        return int(hh) * 60 + int(mm)

    def _min_to_str(t_min: int) -> str:
        h, mm = divmod(t_min % 1440, 60)
        return f"{h:02d}:{mm:02d}"

    # -------------------------------------------------------------------------
    # 4. g67-digital-clock-palindromes (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    clock_cases = [
        # (time_str, mode, param, diff, place_en, place_ar)
        ("12:05", "next_pal", None, "Easy", "library wall", "جدار المكتبة"),
        ("13:14", "next_pal", None, "Easy", "train platform", "رصيف القطار"),
        ("21:00", "next_pal", None, "Easy", "study desk", "مكتب الدراسة"),
        ("03:08", "next_pal", None, "Easy", "observatory dome", "قبة المرصد"),
        ("14:19", "next_pal", None, "Easy", "science lab", "مختبر العلوم"),
        ("22:07", "next_pal", None, "Easy", "airport lounge", "صالة المطار"),
        ("05:50", "next_pal", None, "Medium", "campus shuttle stop", "موقف حافلات الجامعة"),
        ("15:55", "next_pal", None, "Medium", "sports hall", "الصالة الرياضية"),
        ("05:56", "next_pal", None, "Medium", "harbor tower", "برج الميناء"),
        ("23:32", "next_pal", None, "Medium", "control room", "غرفة التحكم"),
        ("01:10", "between_pal", "03:30", "Medium", "weather station", "محطة الأرصاد"),
        ("11:11", "between_pal", "14:41", "Medium", "museum lobby", "بهو المتحف"),
        ("10:00", "count_window", "15:59", "Medium", "lecture auditorium", "قاعة المحاضرات"),
        ("14:00", "digit_sum_hr", 12, "Hard", "robotics workshop", "ورشة الروبوتات"),
        ("23:00", "digit_sum_hr", 15, "Hard", "night clinic", "العيادة المسائية"),
        ("08:00", "digit_sum_hr", 18, "Hard", "school entrance", "مدخل المدرسة"),
        ("00:00", "all_day_pals", None, "Hard", "central plaza", "الساحة المركزية"),
    ]
    for time_str, mode, param, diff, place_en, place_ar in clock_cases:
        qid = next_id()
        svg_en = svg_digital_clock(time_str, "24-hour display")
        svg_ar = svg_digital_clock(time_str, "نظام 24 ساعة")
        t0 = _str_to_min(time_str)

        if mode == "next_pal":
            wait = 1
            while not _is_pal_min(t0 + wait):
                wait += 1
            ans = wait
            next_ts = _min_to_str(t0 + wait)
            distractors = (
                [70, 61, ans - 60, ans + 10]
                if ans > 100
                else [ans + 10, max(1, ans - 2), ans + 4, ans + 11]
            )
            q_en = (
                f"A {m(24)}-hour digital clock on the {place_en} currently reads **{time_str}** (`HH:MM`). "
                f"After how many minutes will it **next** display a palindromic time (reading the same forwards and backwards, ignoring the colon)?"
            )
            q_ar = (
                f"تشير ساعة رقمية بنظام {m(24)} ساعة في {place_ar} حاليًا إلى **{time_str}** (`HH:MM`). "
                f"بعد كم دقيقة ستُظهر الساعة **أقرب** وقت متناظر تالٍ (يُقرأ من اليسار إلى اليمين كما يُقرأ من اليمين إلى اليسار دون النقطتين)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
            gap_note_en = (
                f"Watch out! Hours `06`–`09` and `16`–`19` cannot form palindromes because minutes `60`–`90` do not exist on a clock! So the next valid palindrome is **{next_ts}**."
                if ans > 60
                else f"Test the reversed hour digits first: reversing `{time_str[:2]}` gives minutes `{next_ts[3:]}` (or wrap past `23:59` to `00:00`), so the next palindrome is **{next_ts}**."
            )
            gap_note_ar = (
                f"انتبه للفخ الشهير! الساعات `06`–`09` و`16`–`19` لا تكوّن أوقاتًا متناظرة لأن الدقائق لا يمكن أن تكون `60` أو أكثر! إذن أقرب وقت متناظر تالٍ هو **{next_ts}**."
                if ans > 60
                else f"اعكس رقمي الساعة لاختبار الدقائق الموافقة (أو انتقل بعد منتصف الليل إلى `00:00`)، فيكون أقرب وقت متناظر تالٍ هو **{next_ts}**."
            )
            hint_en = "Reverse the two hour digits HH to see the matching MM — and remember minutes must stay between 00 and 59!"
            hint_ar = "اعكس رقمي الساعة لمعرفة الدقائق المقابلة — وتذكّر أن الدقائق يجب أن تكون بين 00 و59 فقط!"
            sol_en = explain_en(
                "A 4-digit clock time `ab:ba` is a palindrome only when the reversed hour `ba` is a valid minute (`00` to `59`)!",
                [
                    gap_note_en,
                    f"Compute the elapsed minutes from **{time_str}** to **{next_ts}**: {m(f'{ans}')} minutes.",
                ],
                f"Check: adding {m(ans)} minutes to **{time_str}** lands on **{next_ts}**, whose digits `{next_ts.replace(':', '')}` read the same both ways!",
            )
            sol_ar = explain_ar(
                "يكون الوقت `ab:ba` متناظرًا فقط عندما تكون الدقائق المعكوسة `ba` صحيحة (أي من `00` إلى `59`)!",
                [
                    gap_note_ar,
                    f"نحسب عدد الدقائق من **{time_str}** حتى **{next_ts}** فنجده {m(ans)} دقيقة.",
                ],
                f"تحقق: إضافة {m(ans)} دقيقة إلى **{time_str}** تعطينا **{next_ts}**، وأرقامه `{next_ts.replace(':', '')}` متناظرة تمامًا.",
            )

        elif mode == "between_pal":
            end_str = param
            t1 = _str_to_min(end_str)
            ans = t1 - t0
            dh = int(end_str[:2]) - int(time_str[:2])
            dm_ = int(end_str[3:]) - int(time_str[3:])
            q_en = (
                f"A {m(24)}-hour digital clock in the {place_en} shows the palindromic time **{time_str}**. "
                f"How many minutes pass from **{time_str}** until the clock shows the later palindromic time **{end_str}** on the same day?"
            )
            q_ar = (
                f"تُظهر ساعة رقمية بنظام {m(24)} ساعة في {place_ar} الوقت المتناظر **{time_str}**. "
                f"كم دقيقة تمرّ من **{time_str}** حتى تُظهر الساعة الوقت المتناظر اللاحق **{end_str}** في اليوم نفسه؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [dh * 60, dh * 100 + dm_, ans - 10, ans + 10], qid
            )
            hint_en = "Convert the hour difference to minutes (× 60) and add the minute difference — remember 1 hour = 60 minutes, not 100!"
            hint_ar = "حوّل فرق الساعات إلى دقائق بالضرب في 60 ثم أضف فرق الدقائق — تذكّر أن الساعة 60 دقيقة وليست 100!"
            sol_en = explain_en(
                "Subtract hours and minutes separately, converting each hour into **60 minutes**!",
                [
                    f"From `{time_str[:2]}:{time_str[3:]}` to `{end_str[:2]}:{time_str[3:]}` is {m(dh)} hours = {m(f'{dh} \\times 60 = {dh * 60}')} minutes.",
                    f"From `{end_str[:2]}:{time_str[3:]}` to `{end_str}` is an additional {m(dm_)} minutes.",
                    f"Total elapsed time: {m(f'{dh * 60} + {dm_} = {ans}')} minutes.",
                ],
                f"Trap check: subtracting `{end_str.replace(':', '')} - {time_str.replace(':', '')}` as base-10 integers gives the wrong answer because hours have 60 minutes!",
            )
            sol_ar = explain_ar(
                "نحسب فرق الساعات وفرق الدقائق كلًا على حدة، مع تحويل كل ساعة إلى **60 دقيقة**!",
                [
                    f"من `{time_str}` إلى `{end_str[:2]}:{time_str[3:]}` تمرّ {m(dh)} ساعات = {m(f'{dh} \\times 60 = {dh * 60}')} دقيقة.",
                    f"ومن `{end_str[:2]}:{time_str[3:]}` إلى `{end_str}` تمرّ {m(dm_)} دقيقة إضافية.",
                    f"إجمالي الدقائق المنقضية: {m(f'{dh * 60} + {dm_} = {ans}')} دقيقة.",
                ],
                f"انتبه: طرح الأرقام كأعداد عشرية عادية يعطي إجابة خاطئة لأن الساعة 60 دقيقة وليست 100!",
            )

        elif mode == "count_window":
            end_str = param
            t1 = _str_to_min(end_str)
            pals = [_min_to_str(t) for t in range(t0, t1 + 1) if _is_pal_min(t)]
            ans = len(pals)
            q_en = (
                f"The {m(24)}-hour digital clock in the {place_en} starts at **{time_str}** as shown. "
                f"How many **palindromic** times (`HH:MM` reading the same forwards and backwards) appear from **{time_str}** to **{end_str}** inclusive?"
            )
            q_ar = (
                f"تبدأ ساعة رقمية بنظام {m(24)} ساعة في {place_ar} من الوقت **{time_str}** كما في الشكل. "
                f"كم وقتًا **متناظرًا** (`HH:MM` يُقرأ من الجهتين بنفس الترتيب) يظهر في الفترة من **{time_str}** إلى **{end_str}** شاملة الطرفين؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans - 1, ans + 1, ans + 2, ans + 4], qid
            )
            hint_en = "Each hour HH can produce at most ONE palindrome (by reversing its digits to get MM). Test each hour 10, 11, 12, 13, 14, 15!"
            hint_ar = "كل ساعة HH تعطي على الأكثر وقتًا متناظرًا واحدًا عند عكس رقميها! اختبر الساعات 10، 11، 12، 13، 14، 15."
            sol_en = explain_en(
                "Once the hour `HH` is fixed, there is **at most one** choice for `MM` (the reverse of `HH`), and we just check whether `MM < 60`!",
                [
                    f"Test every hour from `10` through `15`: reversing `10..15` gives minutes `01, 11, 21, 31, 41, 51`, all strictly less than `60`.",
                    f"List them all: **{', '.join(pals)}**.",
                    f"That gives {m(ans)} palindromic displays in total.",
                ],
                f"Every listed time lies between `{time_str}` and `{end_str}`, and no other minute in any of those hours can match!",
            )
            sol_ar = explain_ar(
                "عند تثبيت الساعة `HH` توجد **طريقة واحدة على الأكثر** لاختيار الدقائق `MM` (وهي عكس رقمي الساعة) بشرط أن تكون أقل من `60`!",
                [
                    f"نختبر الساعات من `10` إلى `15`: عكسها يعطي الدقائق `01، 11، 21، 31، 41، 51` وجميعها أقل من `60`.",
                    f"الأوقات المتناظرة هي: **{', '.join(pals)}**.",
                    f"إذن العدد الكلي يساوي {m(ans)} أوقات متناظرة.",
                ],
                f"تحقق: جميع الأوقات الستة تقع بين `{time_str}` و`{end_str}` ولا توجد أي دقيقة أخرى تحقق التناظر.",
            )

        elif mode == "digit_sum_hr":
            target_sum = param
            hh = int(time_str[:2])
            h_sum = (hh // 10) + (hh % 10)
            need_m = target_sum - h_sum
            valid_mm = [
                f"{mm:02d}"
                for mm in range(60)
                if (mm // 10) + (mm % 10) == need_m
            ]
            ans = len(valid_mm)
            q_en = (
                f"A {m(24)}-hour digital clock in the {place_en} reads **{time_str}**. "
                f"During the one-hour period from **{hh:02d}:00** to **{hh:02d}:59** inclusive, how many times is the **sum of all four displayed digits** equal to {m(target_sum)}?"
            )
            q_ar = (
                f"تشير ساعة رقمية بنظام {m(24)} ساعة في {place_ar} إلى **{time_str}**. "
                f"خلال الساعة الممتدة من **{hh:02d}:00** إلى **{hh:02d}:59** (شاملة الطرفين)، كم مرة يساوي **مجموع الأرقام الأربعة الظاهرة** العدد {m(target_sum)}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, ans - 1, need_m + 1, ans + 2], qid
            )
            hint_en = f"The hour digits `{hh:02d}` stay fixed with sum {h_sum}, so you only need two-digit minutes `m1 m2` (with 0 ≤ m1 ≤ 5 and 0 ≤ m2 ≤ 9) whose digits add to {need_m}!"
            hint_ar = f"رقما الساعة `{hh:02d}` ثابتان ومجموعهما {h_sum}، لذا ابحث عن الدقائق `m1 m2` (حيث 0 ≤ m1 ≤ 5 و0 ≤ m2 ≤ 9) التي مجموع رقميها {need_m}!"
            sol_en = explain_en(
                "Subtract the fixed hour-digit sum first, then list valid tens digits `0..5` for the minutes!",
                [
                    f"The hour `{hh:02d}` contributes {m(f'{hh // 10} + {hh % 10} = {h_sum}')}, so the two minute digits must sum to {m(f'{target_sum} - {h_sum} = {need_m}')}.",
                    f"Remember the tens digit of minutes can only be `0, 1, 2, 3, 4,` or `5`, while the ones digit must be `0..9`.",
                    f"Valid minute pairs `MM`: **{', '.join(valid_mm)}** — which is {m(ans)} times in total.",
                ],
                f"Notice why `6` or higher cannot be the tens digit of minutes: minutes stop at `59`!",
            )
            sol_ar = explain_ar(
                "نطرح مجموع رقمي الساعة الثابتين أولًا، ثم نختبر رقم عشرات الدقائق من `0` إلى `5` فقط!",
                [
                    f"الساعة `{hh:02d}` مجموع رقميها {m(f'{hh // 10} + {hh % 10} = {h_sum}')}، إذن يجب أن يكون مجموع رقمي الدقائق {m(f'{target_sum} - {h_sum} = {need_m}')}.",
                    f"عشرات الدقائق تقع بين `0` و`5` فقط، وآحادها بين `0` و`9`.",
                    f"الدقائق الصالحة هي: **{', '.join(valid_mm)}**، وعددها {m(ans)} مرات.",
                ],
                f"تنبيه: لا يمكن لعشرات الدقائق أن تكون `6` أو أكبر لأن الدقائق تنتهي عند `59`!",
            )

        else:  # all_day_pals
            all_pals = [_min_to_str(t) for t in range(1440) if _is_pal_min(t)]
            ans = len(all_pals)
            assert ans == 16
            q_en = (
                f"A {m(24)}-hour digital clock in the {place_en} runs from **00:00** to **23:59** every day. "
                f"In one full {m(24)}-hour day, how many different `HH:MM` displays are **palindromes** (reading the exact same four digits forwards and backwards)?"
            )
            q_ar = (
                f"تعمل ساعة رقمية بنظام {m(24)} ساعة في {place_ar} من **00:00** حتى **23:59** يوميًا. "
                f"خلال يوم كامل مدته {m(24)} ساعة، كم قراءة مختلفة بصيغة `HH:MM` تكون **متناظرة** (تُقرأ أرقامها الأربعة بنفس الترتيب من الجهتين)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [24, 15, 18, 12], qid
            )
            hint_en = "Check which of the 24 hours (00 to 23) have a ones digit < 6 so that reversing HH gives a valid minute < 60!"
            hint_ar = "افحص أي الساعات من 00 إلى 23 يكون رقم آحادها أصغر من 6 حتى يصبح معكوسها دقائق أقل من 60!"
            sol_en = explain_en(
                "For `ab:ba` to be a valid 24-hour time, the reversed hour `ba` must be `< 60`, which means the ones digit `b` of the hour must be `0, 1, 2, 3, 4,` or `5`!",
                [
                    f"When `a = 0` (`00`–`09`): `b` can be `0..5` (`00:00` to `05:50`) → {m(6)} times (`06`–`09` fail because `60`–`90` are invalid minutes!).",
                    f"When `a = 1` (`10`–`19`): `b` can be `0..5` (`10:01` to `15:51`) → {m(6)} times.",
                    f"When `a = 2` (`20`–`23`): all four hours `20:02, 21:12, 22:22, 23:32` have `b < 6` → {m(4)} times. Total = {m('6 + 6 + 4 = 16')}!",
                ],
                f"Check: {m(24)} total hours minus the {m(8)} impossible hours (`06,07,08,09` and `16,17,18,19`) = {m(16)} palindromes!",
            )
            sol_ar = explain_ar(
                "لكي يكون الوقت `ab:ba` صحيحًا، يجب أن تكون الدقائق `ba` أقل من `60`، أي أن آحاد الساعة `b` يجب أن يكون من `0` إلى `5` فقط!",
                [
                    f"عند `a = 0` (`00`–`09`): تصلح `00:00` إلى `05:50` → {m(6)} مرات (بينما تفشل `06`–`09`!).",
                    f"عند `a = 1` (`10`–`19`): تصلح `10:01` إلى `15:51` → {m(6)} مرات.",
                    f"عند `a = 2` (`20`–`23`): تصلح الساعات الأربع `20:02، 21:12، 22:22، 23:32` → {m(4)} مرات. الإجمالي = {m('6 + 6 + 4 = 16')}!",
                ],
                f"تحقق سريع: {m(24)} ساعة مطروحًا منها {m(8)} ساعات مستحيلة (`06..09` و`16..19`) = {m(16)} قراءة متناظرة!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-digital-clock-palindromes",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # -------------------------------------------------------------------------
    # 5. g67-venn-two-clubs (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    venn_cases = [
        # (only_a, both, only_b, neither, mode, diff, ca_en, cb_en, ca_ar, cb_ar)
        (11, 7, 9, 0, "both_no_out", "Easy", "Math", "Robotics", "الرياضيات", "الروبوتات"),
        (13, 6, 8, 0, "both_no_out", "Easy", "Art", "Coding", "الفنون", "البرمجة"),
        (10, 9, 12, 0, "both_no_out", "Easy", "Chess", "Science", "الشطرنج", "العلوم"),
        (9, 5, 11, 4, "total_regions", "Easy", "Astronomy", "Drama", "الفلك", "المسرح"),
        (12, 8, 7, 5, "total_regions", "Easy", "Calligraphy", "Reading", "الخط العربي", "القراءة"),
        (8, 6, 10, 3, "total_regions", "Easy", "Origami", "Music", "الأوريغامي", "الموسيقى"),
        (10, 7, 8, 5, "both_with_out", "Medium", "Math", "Art", "الرياضيات", "الفنون"),
        (12, 9, 6, 4, "both_with_out", "Medium", "Robotics", "Chess", "الروبوتات", "الشطرنج"),
        (14, 6, 9, 6, "both_with_out", "Medium", "Science", "Coding", "العلوم", "البرمجة"),
        (11, 8, 10, 3, "both_with_out", "Medium", "Debate", "Photography", "المناظرة", "التصوير"),
        (13, 7, 9, 4, "only_one", "Medium", "Math", "Astronomy", "الرياضيات", "الفلك"),
        (10, 8, 11, 5, "only_one", "Medium", "Robotics", "Art", "الروبوتات", "الفنون"),
        (15, 6, 8, 3, "only_one", "Medium", "Coding", "Botany", "البرمجة", "النبات"),
        (11, 6, 9, 5, "find_neither", "Hard", "Math", "Physics", "الرياضيات", "الفيزياء"),
        (13, 8, 7, 6, "find_neither", "Hard", "Chess", "Robotics", "الشطرنج", "الروبوتات"),
        (12, 5, 10, 4, "double_only_b", "Hard", "Art", "Poetry", "الفنون", "الشعر"),
        (9, 6, 12, 5, "double_only_b", "Hard", "Science", "Geography", "العلوم", "الجغرافيا"),
    ]
    for only_a, both, only_b, neither, mode, diff, ca_en, cb_en, ca_ar, cb_ar in venn_cases:
        qid = next_id()
        na = only_a + both
        nb = only_b + both
        union = only_a + both + only_b
        tot = union + neither

        if mode == "both_no_out":
            ans = both
            svg_en = svg_venn_2(f"{ca_en} ({na})", f"{cb_en} ({nb})", "", "?", "", "")
            svg_ar = svg_venn_2(f"{ca_ar} ({na})", f"{cb_ar} ({nb})", "", "؟", "", "")
            q_en = (
                f"Every one of the {m(tot)} students in a workshop belongs to the {ca_en} club, the {cb_en} club, or both. "
                f"If {m(na)} students are in the {ca_en} club and {m(nb)} are in the {cb_en} club, how many students belong to **both** clubs?"
            )
            q_ar = (
                f"ينتمي كل طالب من طلاب ورشة عددهم {m(tot)} طالبًا إلى نادي {ca_ar} أو نادي {cb_ar} أو كليهما معًا. "
                f"إذا كان في نادي {ca_ar} {m(na)} طالبًا وفي نادي {cb_ar} {m(nb)} طالبًا، فكم طالبًا ينتمي إلى **الناديين معًا**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [only_a, only_b, abs(na - nb) if abs(na - nb) != ans else ans + 3, ans + 2], qid
            )
            hint_en = f"Adding {na} + {nb} counts students in BOTH clubs twice! Subtract the total {tot} to find the overlap."
            hint_ar = f"جمع {na} + {nb} يحسب المشتركين في الناديين مرتين! اطرح العدد الكلي {tot} لإيجاد التقاطع."
            sol_en = explain_en(
                "When you add the sizes of two overlapping clubs, every student in **both** clubs gets counted **twice**!",
                [
                    f"Add the two club counts: {m(f'{na} + {nb} = {na + nb}')}.",
                    f"Compare with the {m(tot)} actual students: the extra {m(f'{na + nb} - {tot} = {ans}')} counts are the students in **both** clubs!",
                ],
                f"Check the 3 regions: only {ca_en} = {m(only_a)}, both = {m(ans)}, only {cb_en} = {m(only_b)}; sum = {m(f'{only_a} + {ans} + {only_b} = {tot}')}!",
            )
            sol_ar = explain_ar(
                "عند جمع عدد أعضاء الناديين معًا، يُحسب الطلاب المشتركون في **الناديين معًا** مرتين!",
                [
                    f"نجمع عددي الناديين: {m(f'{na} + {nb} = {na + nb}')}.",
                    f"نطرح العدد الفعلي للطلاب ({m(tot)}): {m(f'{na + nb} - {tot} = {ans}')} طلاب في الناديين معًا.",
                ],
                f"تحقق: {ca_ar} فقط = {m(only_a)}، معًا = {m(ans)}، {cb_ar} فقط = {m(only_b)}، والمجموع = {m(tot)}.",
            )

        elif mode == "total_regions":
            ans = tot
            svg_en = svg_venn_2(ca_en, cb_en, str(only_a), str(both), str(only_b), str(neither))
            svg_ar = svg_venn_2(ca_ar, cb_ar, str(only_a), str(both), str(only_b), str(neither))
            q_en = (
                f"The Venn diagram shows how a grade's students joined the {ca_en} and {cb_en} clubs: "
                f"{m(only_a)} are in {ca_en} only, {m(both)} are in **both** clubs, {m(only_b)} are in {cb_en} only, and {m(neither)} are in **neither** club. "
                f"How many students are in the grade in total?"
            )
            q_ar = (
                f"يوضّح شكل فن توزيع طلاب صف على ناديي {ca_ar} و{cb_ar}: "
                f"{m(only_a)} في {ca_ar} فقط، و{m(both)} في **الناديين معًا**، و{m(only_b)} في {cb_ar} فقط، و{m(neither)} خارج الناديين. "
                f"كم إجمالي عدد طلاب الصف؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [union, ans + both, ans - both, ans + 3], qid
            )
            hint_en = "The four regions in the Venn diagram do NOT overlap — just add all four numbers once!"
            hint_ar = "المناطق الأربع في شكل فن منفصلة ولا تتداخل — اجمع الأعداد الأربعة مرة واحدة فقط!"
            sol_en = explain_en(
                "Because the Venn diagram already separates **only A**, **both**, **only B**, and **neither**, every student sits in **exactly one** of the four regions!",
                [
                    f"Students in at least one club: {m(f'{only_a} + {both} + {only_b} = {union}')}.",
                    f"Add the {m(neither)} students outside both circles: {m(f'{union} + {neither} = {ans}')} students.",
                ],
                f"Trap check: do NOT add {m(both)} twice — '{ca_en} only' ({m(only_a)}) already excludes the overlap!",
            )
            sol_ar = explain_ar(
                "بما أن شكل فن يفصل بين **الأول فقط** و**كليهما** و**الثاني فقط** و**خارجهما**، فكل طالب يقع في منطقة واحدة فقط!",
                [
                    f"عدد المشتركين في نادٍ واحد على الأقل: {m(f'{only_a} + {both} + {only_b} = {union}')}.",
                    f"نضيف الطلاب الـ {m(neither)} خارج الدائرتين: {m(f'{union} + {neither} = {ans}')} طالبًا.",
                ],
                f"تنبيه: لا تجمع {m(both)} مرتين لأن المنطقة المكتوب فيها {m(only_a)} تمثّل «{ca_ar} فقط»!",
            )

        elif mode == "both_with_out":
            ans = both
            svg_en = svg_venn_2(f"{ca_en} ({na})", f"{cb_en} ({nb})", "", "?", "", str(neither))
            svg_ar = svg_venn_2(f"{ca_ar} ({na})", f"{cb_ar} ({nb})", "", "؟", "", str(neither))
            q_en = (
                f"In a class of {m(tot)} students, {m(na)} belong to the {ca_en} club, {m(nb)} belong to the {cb_en} club, "
                f"and {m(neither)} belong to **neither** club. How many students belong to **both** clubs?"
            )
            q_ar = (
                f"في صف يضم {m(tot)} طالبًا، ينتمي {m(na)} طالبًا إلى نادي {ca_ar}، وينتمي {m(nb)} طالبًا إلى نادي {cb_ar}، "
                f"بينما لا ينتمي {m(neither)} طلاب إلى **أيٍّ من الناديين**. كم طالبًا ينتمي إلى **الناديين معًا**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [na + nb - tot, ans + neither, only_a, ans + 2], qid
            )
            hint_en = f"First subtract the {neither} students in neither club from {tot} to find how many are in at least one club!"
            hint_ar = f"اطرح أولًا الـ {neither} طلاب الذين خارج الناديين من {tot} لمعرفة عدد المشتركين في نادٍ واحد على الأقل!"
            sol_en = explain_en(
                "Remove the 'neither' students first to find the union of the two circles, then find the overlap!",
                [
                    f"Students in **at least one** club: {m(f'{tot} - {neither} = {union}')}.",
                    f"Sum of the two club rosters: {m(f'{na} + {nb} = {na + nb}')}.",
                    f"Overlap (counted twice): {m(f'{na + nb} - {union} = {ans}')} students.",
                ],
                f"Check: {m(f'{only_a} + {ans} + {only_b} + {neither} = {tot}')} students in all!",
            )
            sol_ar = explain_ar(
                "نستبعد أولًا الطلاب غير المشتركين لمعرفة مجموع الدائرتين، ثم نحسب التقاطع!",
                [
                    f"عدد الطلاب في **نادٍ واحد على الأقل**: {m(f'{tot} - {neither} = {union}')}.",
                    f"مجموع قائمتي الناديين: {m(f'{na} + {nb} = {na + nb}')}.",
                    f"عدد المشتركين في الناديين معًا: {m(f'{na + nb} - {union} = {ans}')}.",
                ],
                f"تحقق: {m(f'{only_a} + {ans} + {only_b} + {neither} = {tot}')} طالبًا.",
            )

        elif mode == "only_one":
            ans = only_a + only_b
            svg_en = svg_venn_2(f"{ca_en} ({na})", f"{cb_en} ({nb})", "?", str(both), "?", str(neither))
            svg_ar = svg_venn_2(f"{ca_ar} ({na})", f"{cb_ar} ({nb})", "؟", str(both), "؟", str(neither))
            q_en = (
                f"Among a group of students, {m(na)} are in the {ca_en} club, {m(nb)} are in the {cb_en} club, "
                f"and {m(both)} are in **both** clubs (with {m(neither)} in neither). How many students belong to **exactly one** of the two clubs?"
            )
            q_ar = (
                f"في مجموعة طلاب، يوجد {m(na)} في نادي {ca_ar}، و{m(nb)} في نادي {cb_ar}، "
                f"و{m(both)} في **الناديين معًا** (و{m(neither)} خارج الناديين). كم طالبًا ينتمي إلى **نادٍ واحد فقط** من الناديين؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [union, na + nb, ans + neither, only_a], qid
            )
            hint_en = f"Find '{ca_en} only' ({na} − {both}) and '{cb_en} only' ({nb} − {both}), then add them together!"
            hint_ar = f"احسب «{ca_ar} فقط» ({na} − {both}) و«{cb_ar} فقط» ({nb} − {both}) ثم اجمعهما!"
            sol_en = explain_en(
                "'At least one' includes the middle overlap, whereas '**exactly one**' excludes the middle overlap from **both** circles!",
                [
                    f"Students in {ca_en} **only**: {m(f'{na} - {both} = {only_a}')}.",
                    f"Students in {cb_en} **only**: {m(f'{nb} - {both} = {only_b}')}.",
                    f"Students in **exactly one** club: {m(f'{only_a} + {only_b} = {ans}')}.",
                ],
                f"Notice: {m(f'{na} + {nb} - {both} = {union}')} gives 'at least one' — you must subtract {m(both)} **twice** to get 'exactly one' ({m(ans)})!",
            )
            sol_ar = explain_ar(
                "عبارة «نادٍ واحد فقط» تستبعد منطقة التقاطع الوسطى من **كلتا** الدائرتين!",
                [
                    f"طلاب {ca_ar} **فقط**: {m(f'{na} - {both} = {only_a}')}.",
                    f"طلاب {cb_ar} **فقط**: {m(f'{nb} - {both} = {only_b}')}.",
                    f"طلاب **نادٍ واحد فقط**: {m(f'{only_a} + {only_b} = {ans}')} طالبًا.",
                ],
                f"انتبه: طرح {m(both)} مرة واحدة يعطي {m(union)} («نادٍ واحد على الأقل»)، بينما المطلوب «نادٍ واحد فقط» وهو {m(ans)}!",
            )

        elif mode == "find_neither":
            ans = neither
            ex_one = only_a + only_b
            svg_en = svg_venn_2(f"{ca_en} ({na})", f"{cb_en} ({nb})", "", "", "", "?")
            svg_ar = svg_venn_2(f"{ca_ar} ({na})", f"{cb_ar} ({nb})", "", "", "", "؟")
            q_en = (
                f"In a cohort of {m(tot)} students, {m(na)} joined the {ca_en} club, {m(nb)} joined the {cb_en} club, "
                f"and **exactly** {m(ex_one)} students belong to **only one** of the two clubs. How many students belong to **neither** club?"
            )
            q_ar = (
                f"في دفعة مكوّنة من {m(tot)} طالبًا، التحق {m(na)} بنادي {ca_ar} و{m(nb)} بنادي {cb_ar}، "
                f"وكان عدد المنتمين إلى **نادٍ واحد فقط** يساوي {m(ex_one)} طالبًا بالضبط. كم طالبًا لا ينتمي إلى **أيٍّ من الناديين**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [both, ans + both, max(1, tot - na - nb + both), ans + 2], qid
            )
            hint_en = f"Adding {na} + {nb} counts 'only one' once and 'both' TWICE! Subtract {ex_one} and divide by 2 to find 'both'."
            hint_ar = f"المجموع {na} + {nb} يحسب أصحاب النادي الواحد مرة وأصحاب الناديين مرتين! اطرح {ex_one} واقسم على 2 لإيجاد المشتركين."
            sol_en = explain_en(
                "Compare `|A| + |B|` with `'only one'`: their difference equals **twice** the overlap!",
                [
                    f"Sum of club lists: {m(f'{na} + {nb} = {na + nb}')}. Since 'only one' accounts for {m(ex_one)}, twice the overlap is {m(f'{na + nb} - {ex_one} = {2 * both}')}, so **both** = {m(both)}.",
                    f"Total in at least one club = 'only one' + 'both' = {m(f'{ex_one} + {both} = {union}')}.",
                    f"Students in **neither** club: {m(f'{tot} - {union} = {ans}')}.",
                ],
                f"Check: {m(only_a)} ({ca_en} only) + {m(both)} (both) + {m(only_b)} ({cb_en} only) + {m(ans)} (neither) = {m(tot)}!",
            )
            sol_ar = explain_ar(
                "عند مقارنة مجموع القائمتين بعدد طلاب «النادي الواحد فقط»، يكون الفرق مساويًا **ضعف** منطقة التقاطع!",
                [
                    f"مجموع القائمتين {m(f'{na} + {nb} = {na + nb}')}. نطرح {m(ex_one)} فنجد ضعف المشتركين = {m(2 * both)}، أي المشتركون في الناديين = {m(both)}.",
                    f"إجمالي المشتركين في نادٍ على الأقل = {m(f'{ex_one} + {both} = {union}')}.",
                    f"غير المشتركين في أي نادٍ: {m(f'{tot} - {union} = {ans}')}.",
                ],
                f"تحقق: {m(f'{only_a} + {both} + {only_b} + {ans} = {tot}')} طالبًا بالضبط.",
            )

        else:  # double_only_b (here only_b == 2 * both!)
            assert only_b == 2 * both
            ans = nb
            svg_en = svg_venn_2(f"{ca_en} ({na})", f"{cb_en} (?)", "", "x", "2x", str(neither))
            svg_ar = svg_venn_2(f"{ca_ar} ({na})", f"{cb_ar} (؟)", "", "x", "2x", str(neither))
            q_en = (
                f"Out of {m(tot)} students, {m(neither)} are in neither club and {m(na)} are in the {ca_en} club. "
                f"The number of students in **{cb_en} only** is **twice** the number of students in **both** clubs (as shown by `2x` and `x`). "
                f"How many students in total belong to the **{cb_en} club**?"
            )
            q_ar = (
                f"من بين {m(tot)} طالبًا، يوجد {m(neither)} خارج الناديين و{m(na)} طالبًا في نادي {ca_ar}. "
                f"إذا كان عدد طلاب **{cb_ar} فقط** يساوي **ضعف** عدد طلاب **الناديين معًا** (`2x` و`x` كما في الشكل)، "
                f"فكم إجمالي عدد أعضاء **نادي {cb_ar}**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [only_b, both, ans + 3, ans - 2], qid
            )
            hint_en = f"Notice that ({ca_en} circle) + ({cb_en} only) covers ALL {union} club members without overlap! Subtract {na} from {union} to get 2x right away."
            hint_ar = f"لاحظ أن (دائرة {ca_ar} كاملة) + ({cb_ar} فقط) تغطي جميع المشتركين الـ {union} دون تكرار! اطرح {na} من {union} لإيجاد 2x فورًا."
            sol_en = explain_en(
                f"Use the whole {ca_en} circle ({m(na)}) plus the `{cb_en} only` crescent (`2x`): together they equal all {m(union)} active students!",
                [
                    f"Students in at least one club: {m(f'{tot} - {neither} = {union}')}.",
                    f"Subtract the entire {ca_en} circle ({m(na)}) to isolate **{cb_en} only**: {m(f'2x = {union} - {na} = {only_b}')}, so {m(f'x = {both}')}.",
                    f"Total in {cb_en} club = {m(f'x + 2x = {both} + {only_b} = {ans}')} students.",
                ],
                f"Check: {ca_en} only = {m(f'{na} - {both} = {only_a}')}; {m(f'{only_a} + {both} + {only_b} + {neither} = {tot}')}!",
            )
            sol_ar = explain_ar(
                f"دائرة {ca_ar} كاملة ({m(na)}) مع هلال «{cb_ar} فقط» (`2x`) يشكّلان معًا اتحاد الدائرتين ({m(union)}) دون أي تداخل!",
                [
                    f"عدد المشتركين في نادٍ واحد على الأقل: {m(f'{tot} - {neither} = {union}')}.",
                    f"نطرح دائرة {ca_ar} كاملة ({m(na)}) فنجد **{cb_ar} فقط**: {m(f'2x = {union} - {na} = {only_b}')}، ومنها {m(f'x = {both}')}.",
                    f"إجمالي أعضاء نادي {cb_ar} = {m(f'x + 2x = {both} + {only_b} = {ans}')} طالبًا.",
                ],
                f"تحقق: {ca_ar} فقط = {m(only_a)}، والمجموع الكلي {m(f'{only_a} + {both} + {only_b} + {neither} = {tot}')} طالبًا.",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-venn-two-clubs",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # -------------------------------------------------------------------------
    # 6. g67-missing-digit-div-346 (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    div_cases = [
        # (pattern, divisor, ask_mode, diff, place_en, place_ar)
        ("73d", 4, "max", "Easy", "ones digit", "رقم الآحاد"),
        ("5d2", 4, "min", "Easy", "tens digit", "رقم العشرات"),
        ("4d2", 6, "max", "Easy", "tens digit", "رقم العشرات"),
        ("82d", 6, "min", "Easy", "ones digit", "رقم الآحاد"),
        ("61d", 4, "min", "Easy", "ones digit", "رقم الآحاد"),
        ("5d6", 6, "sum", "Medium", "tens digit", "رقم العشرات"),
        ("27d4", 4, "count", "Medium", "tens digit", "رقم العشرات"),
        ("3d52", 6, "sum", "Medium", "hundreds digit", "رقم المئات"),
        ("73d", 6, "sum", "Medium", "ones digit", "رقم الآحاد"),
        ("41d6", 4, "sum", "Medium", "tens digit", "رقم العشرات"),
        ("5d4", 12, "max", "Medium", "tens digit", "رقم العشرات"),
        ("8d16", 12, "count", "Medium", "hundreds digit", "رقم المئات"),
        ("25d2", 12, "sum", "Hard", "tens digit", "رقم العشرات"),
        ("61d8", 12, "max", "Hard", "tens digit", "رقم العشرات"),
        ("472d", 12, "unique", "Hard", "ones digit", "رقم الآحاد"),
        ("94d6", 12, "unique", "Hard", "tens digit", "رقم العشرات"),
    ]
    ask_labels = {
        "max": ("What is the **largest** possible value of the digit \\( d \\)?", "ما **أكبر** قيمة ممكنة للرقم \\( d \\)؟"),
        "min": ("What is the **smallest** possible value of the digit \\( d \\)?", "ما **أصغر** قيمة ممكنة للرقم \\( d \\)؟"),
        "sum": ("What is the **sum** of all possible digits \\( d \\)?", "ما **مجموع** جميع القيم الممكنة للرقم \\( d \\)؟"),
        "count": ("**How many** different single digits \\( d \\) (from \\( 0 \\) to \\( 9 \\)) make this true?", "**كم** قيمة مختلفة للرقم \\( d \\) (من \\( 0 \\) إلى \\( 9 \\)) تحقق ذلك؟"),
        "unique": ("What is the value of the digit \\( d \\)?", "ما قيمة الرقم \\( d \\)؟"),
    }
    rule_notes = {
        4: (
            "A number is divisible by **4** if and only if the number formed by its **last two digits** is divisible by 4!",
            "يقبل العدد القسمة على **4** إذا وفقط إذا كان العدد المكوّن من **آخر رقمين (الآحاد والعشرات)** يقبل القسمة على 4!",
        ),
        6: (
            "A number is divisible by **6** if and only if it is **even** (divisible by 2) AND the **sum of its digits** is divisible by **3**!",
            "يقبل العدد القسمة على **6** إذا وفقط إذا كان **زوجيًا** (يقبل على 2) وكان **مجموع أرقامه** يقبل القسمة على **3**!",
        ),
        12: (
            "A number is divisible by **12** if and only if it is divisible by **both 3 and 4** (digit sum divisible by 3, AND last two digits divisible by 4)!",
            "يقبل العدد القسمة على **12** إذا وفقط إذا قبل القسمة على **3 و4 معًا** (مجموع أرقامه يقبل على 3، وآخر رقمين يقبلان على 4)!",
        ),
    }
    for pat, div_by, ask_mode, diff, place_en, place_ar in div_cases:
        qid = next_id()
        valid_ds = [d for d in range(10) if int(pat.replace("d", str(d))) % div_by == 0]
        assert len(valid_ds) >= 1
        if ask_mode == "max":
            ans = max(valid_ds)
        elif ask_mode == "min":
            ans = min(valid_ds)
        elif ask_mode == "sum":
            ans = sum(valid_ds)
        elif ask_mode == "count":
            ans = len(valid_ds)
        else:
            assert len(valid_ds) == 1
            ans = valid_ds[0]

        ndig = len(pat)
        disp_num = f"\\overline{{{pat}}}"
        ask_en, ask_ar = ask_labels[ask_mode]
        idea_en, idea_ar = rule_notes[div_by]
        known_sum = sum(int(ch) for ch in pat if ch != "d")

        q_en = (
            f"The {m(ndig)}-digit integer {m(disp_num)} (where {m('d')} represents the hidden {place_en} from {m(0)} to {m(9)}) "
            f"is divisible by {m(div_by)}. {ask_en}"
        )
        q_ar = (
            f"العدد المكوّن من {m(ndig)} أرقام {m(disp_num)} (حيث {m('d')} يمثّل {place_ar} المفقود من {m(0)} إلى {m(9)}) "
            f"يقبل القسمة على {m(div_by)}. {ask_ar}"
        )
        distractors = [
            ans + 1,
            max(0, ans - 1),
            ans + 2,
            ans + 3,
            max(0, ans - 2),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans, distractors, qid)
        v_list = ", ".join(str(x) for x in valid_ds)
        nums_list = ", ".join(pat.replace("d", str(x)) for x in valid_ds)

        hint_en = idea_en.replace("**", "")
        hint_ar = idea_ar.replace("**", "")
        sol_en = explain_en(
            idea_en,
            [
                f"Known digits add up to {m(known_sum)}, and the last two digits have the form `{pat[-2:]}`.",
                f"Testing digits {m('d \\in \\{0, 1, \\dots, 9\\}')} against the rule for {m(div_by)} gives the valid choice(s): {m(f'd \\in \\{{{v_list}\\}}')} (forming `{nums_list}`).",
                f"Read off the requested answer from {m(f'\\{{{v_list}\\}}')}: **{m(ans)}**.",
            ],
            f"Direct division check: `{pat.replace('d', str(valid_ds[-1]))} ÷ {div_by} = {int(pat.replace('d', str(valid_ds[-1]))) // div_by}` with remainder `0`!",
        )
        sol_ar = explain_ar(
            idea_ar,
            [
                f"مجموع الأرقام المعلومة يساوي {m(known_sum)}، وآخر رقمين على الصورة `{pat[-2:]}`.",
                f"بتطبيق شرط القسمة على {m(div_by)} لجميع القيم من `0` إلى `9` نجد القيم الصالحة: {m(f'd \\in \\{{{v_list}\\}}')} (الأعداد `{nums_list}`).",
                f"إذن الإجابة المطلوبة من المجموعة {m(f'\\{{{v_list}\\}}')} هي **{m(ans)}**.",
            ],
            f"تحقق بالقسمة: `{pat.replace('d', str(valid_ds[-1]))} ÷ {div_by} = {int(pat.replace('d', str(valid_ds[-1]))) // div_by}` والباقي صفر!",
        )

        ask_short_map = {
            "max": ("Max d = ?", "أكبر d = ؟"),
            "min": ("Min d = ?", "أصغر d = ؟"),
            "sum": ("Sum of d = ?", "مجموع d = ؟"),
            "count": ("Count of d = ?", "عدد قيم d = ؟"),
            "unique": ("Digit d = ?", "الرقم d = ؟"),
        }
        note_en, note_ar = ask_short_map[ask_mode]
        svg_en = svg_digit_cards(list(pat), badge_lbl=f"Divisible by {div_by}", note_lbl=note_en)
        svg_ar = svg_digit_cards(list(pat), badge_lbl=f"يقبل القسمة على {div_by}", note_lbl=note_ar)
        items.append(
            make_kmc_question(
                qid, LEVEL, "Number Theory", diff, "g67-missing-digit-div-346",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(items) == 50
    return items


def _gen_group_1_3(next_id) -> list[dict]:
    """Lesson 1.3 group (50 Qs, Topic: 'Algebra'):
    7. g67-dot-array-growth (17 Qs)
    8. g67-function-machine-2step (17 Qs)
    9. g67-additive-number-pyramid (16 Qs)
    """
    items: list[dict] = []

    # -------------------------------------------------------------------------
    # 7. g67-dot-array-growth (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    svg_dot_L = svg_dot_pattern("L")
    svg_dot_cross = svg_dot_pattern("cross")

    dot_cases = [
        # (shape, p1, p2, mode, diff, obj_en, obj_ar)
        ("L", 15, None, "dots", "Easy", "black dots", "نقطة سوداء"),
        ("L", 22, None, "dots", "Easy", "mosaic tiles", "بلاطة فسيفساء"),
        ("L", 30, None, "dots", "Easy", "pearl buttons", "زرًا لؤلؤيًا"),
        ("cross", 12, None, "dots", "Easy", "blue LEDs", "مصباحًا أزرق"),
        ("cross", 18, None, "dots", "Easy", "glass marbles", "كرة زجاجية"),
        ("cross", 25, None, "dots", "Easy", "stepping stones", "حجرًا دائريًا"),
        ("L", 57, None, "step", "Medium", "counters", "قرصًا"),
        ("L", 83, None, "step", "Medium", "pebbles", "حصاة"),
        ("cross", 65, None, "step", "Medium", "pins", "دبوسًا"),
        ("cross", 97, None, "step", "Medium", "stars", "نجمة"),
        ("L", 14, 23, "diff", "Medium", "dots", "نقطة"),
        ("cross", 10, 17, "diff", "Medium", "dots", "نقطة"),
        ("cross", 15, 26, "diff", "Medium", "beads", "خرزة"),
        ("L", 12, 18, "sum_two", "Hard", "magnets", "قطعة مغناطيس"),
        ("cross", 9, 14, "sum_two", "Hard", "blue pegs", "وتدًا أزرق"),
        ("cross", 110, None, "max_box", "Hard", "beads", "خرزة"),
        ("L", 100, None, "max_box", "Hard", "ceramic dots", "قرصًا خزفيًا"),
    ]
    for shape, p1, p2, mode, diff, obj_en, obj_ar in dot_cases:
        qid = next_id()
        k = 2 if shape == "L" else 4
        svg = svg_dot_L if shape == "L" else svg_dot_cross
        sh_en = "L-shaped" if shape == "L" else "cross-shaped"
        sh_ar = "على شكل حرف L" if shape == "L" else "على شكل علامة زائد (+)"
        f1, f2, f3 = k + 1, 2 * k + 1, 3 * k + 1

        if mode == "dots":
            n = p1
            ans = k * n + 1
            q_en = (
                f"In the {sh_en} pattern shown, Step (1) has {m(f1)} {obj_en}, Step (2) has {m(f2)}, and Step (3) has {m(f3)}. "
                f"How many {obj_en} are in **Step ({m(n)})**?"
            )
            q_ar = (
                f"في النمط المرسوم {sh_ar}، تحتوي الخطوة (1) على {m(f1)}، والخطوة (2) على {m(f2)}، والخطوة (3) على {m(f3)}. "
                f"كم {obj_ar} في **الخطوة ({m(n)})**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [k * n, (k + 1) * n, ans + k, ans - k], qid
            )
            hint_en = f"Spot the central corner dot (1 dot), plus {k} arms that each have n dots in Step (n)!"
            hint_ar = f"لاحظ النقطة المركزية الثابتة (نقطة واحدة)، بالإضافة إلى {k} أذرع في كل ذراع منها n نقطة في الخطوة (n)!"
            sol_en = explain_en(
                f"Separate the **1 fixed center dot** from the **{m(k)} growing arms**: in Step {m('n')}, each arm has {m('n')} dots, giving **{m(f'{k}n + 1')}**!",
                [
                    f"Check the rule {m(f'{k}n + 1')}: Step 1 → {m(f'{k}(1)+1={f1}')}, Step 2 → {m(f'{k}(2)+1={f2}')}, Step 3 → {m(f'{k}(3)+1={f3}')}.",
                    f"Substitute {m(f'n = {n}')}: {m(f'{k} \\times {n} + 1 = {k * n} + 1 = {ans}')}.",
                ],
                f"Check: adding {m(k)} dots per step for {m(n - 1)} steps after {m(f1)} gives {m(f'{f1} + {k} \\times {n - 1} = {ans}')}!",
            )
            sol_ar = explain_ar(
                f"افصل **النقطة المركزية الثابتة (1)** عن **الأذرع الـ {m(k)} المتزايدة**: في الخطوة {m('n')} يحوي كل ذراع {m('n')} نقطة، فتكون القاعدة **{m(f'{k}n + 1')}**!",
                [
                    f"نتأكد من القاعدة {m(f'{k}n + 1')}: عند {m('n=1,2,3')} نحصل على {m(f'{f1}، {f2}، {f3}')}.",
                    f"نعوّض {m(f'n = {n}')}: {m(f'{k} \\times {n} + 1 = {k * n} + 1 = {ans}')}.",
                ],
                f"تحقق: البداية {m(f1)} مضافًا إليها {m(f'{k} \\times {n - 1}')} تعطي {m(ans)}.",
            )

        elif mode == "step":
            D = p1
            assert (D - 1) % k == 0
            ans = (D - 1) // k
            q_en = (
                f"The {sh_en} pattern grows steadily: Step (1) has {m(f1)} {obj_en}, Step (2) has {m(f2)}, and Step (3) has {m(f3)}. "
                f"Which **step number** uses **exactly** {m(D)} {obj_en}?"
            )
            q_ar = (
                f"ينمو النمط الموضّح {sh_ar} بانتظام: الخطوة (1) بها {m(f1)}، والخطوة (2) بها {m(f2)}، والخطوة (3) بها {m(f3)}. "
                f"ما **رقم الخطوة** التي تتكوّن من {m(D)} {obj_ar} بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, ans - 1, D // f1, ans + 2], qid
            )
            hint_en = f"Set {k}n + 1 = {D}: subtract the 1 center dot first, then divide equally among the {k} arms!"
            hint_ar = f"اكتب المعادلة {k}n + 1 = {D}: اطرح النقطة المركزية (1) أولًا، ثم اقسم الباقي بالتساوي على الأذرع الـ {k}!"
            sol_en = explain_en(
                f"Use the arm-plus-center structure: remove the **1 center {obj_en[:-1] if obj_en.endswith('s') else 'dot'}**, and divide the rest among the **{m(k)} equal arms**!",
                [
                    f"In Step {m('n')}, total count = {m(f'{k}n + 1')}. Set {m(f'{k}n + 1 = {D}')}.",
                    f"Subtract {m(1)}: {m(f'{k}n = {D - 1}')}.",
                    f"Divide by {m(k)}: {m(f'n = {D - 1} \\div {k} = {ans}')}.",
                ],
                f"Check: {m(f'{k} \\times {ans} + 1 = {k * ans} + 1 = {D}')}!",
            )
            sol_ar = explain_ar(
                f"استخدم بنية الشكل: استبعد **النقطة المركزية الواحدة** أولًا، ثم اقسم الباقي على **الأذرع الـ {m(k)} المتساوية**!",
                [
                    f"القاعدة للخطوة {m('n')} هي {m(f'{k}n + 1')}، فنكتب {m(f'{k}n + 1 = {D}')}.",
                    f"نطرح {m(1)} من الطرفين: {m(f'{k}n = {D - 1}')}.",
                    f"نقسم على {m(k)}: {m(f'n = {D - 1} \\div {k} = {ans}')}.",
                ],
                f"تحقق: {m(f'{k} \\times {ans} + 1 = {D}')} تمامًا.",
            )

        elif mode == "diff":
            a, b = p1, p2
            ans = k * (b - a)
            q_en = (
                f"In the {sh_en} pattern shown (Step 1 has {m(f1)}, Step 2 has {m(f2)}, Step 3 has {m(f3)}), "
                f"how many **more** {obj_en} are in **Step ({m(b)})** than in **Step ({m(a)})**?"
            )
            q_ar = (
                f"في النمط المرسوم {sh_ar} (الخطوة 1 بها {m(f1)}، والخطوة 2 بها {m(f2)}، والخطوة 3 بها {m(f3)})، "
                f"بكم يزيد عدد العناصر في **الخطوة ({m(b)})** عن **الخطوة ({m(a)})**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, (b - a) * f1, ans - k, ans + k], qid
            )
            hint_en = f"Every single step adds +{k} dots! How many steps apart are Step ({a}) and Step ({b})?"
            hint_ar = f"كل خطوة جديدة تضيف +{k}! كم خطوة تفصل بين الخطوة ({a}) والخطوة ({b})؟"
            sol_en = explain_en(
                f"You don't even need to compute both totals separately—each step adds **{m(k)}**, and the `+ 1` center cancels out when subtracting!",
                [
                    f"Number of steps from Step ({m(a)}) to Step ({m(b)}): {m(f'{b} - {a} = {b - a}')} steps.",
                    f"Multiply by {m(k)} per step: {m(f'{b - a} \\times {k} = {ans}')}.",
                ],
                f"Full check: Step ({m(b)}) has {m(k * b + 1)} and Step ({m(a)}) has {m(k * a + 1)}; {m(f'{k * b + 1} - {k * a + 1} = {ans}')}!",
            )
            sol_ar = explain_ar(
                f"كل خطوة جديدة تضيف **{m(k)}** بالضبط، وعند الطرح تُحذف الـ `+ 1` المشتركة مباشرة!",
                [
                    f"فرق رقمي الخطوتين: {m(f'{b} - {a} = {b - a}')} خطوات.",
                    f"نضرب في الزيادة الثابتة {m(k)}: {m(f'{b - a} \\times {k} = {ans}')}.",
                ],
                f"تحقق كامل: {m(f'({k * b + 1}) - ({k * a + 1}) = {ans}')}.",
            )

        elif mode == "sum_two":
            a, b = p1, p2
            da, db = k * a + 1, k * b + 1
            ans = da + db
            q_en = (
                f"Sara builds **two separate** figures from the {sh_en} pattern shown: **Step ({m(a)})** and **Step ({m(b)})** side by side. "
                f"How many {obj_en} does she need **altogether**?"
            )
            q_ar = (
                f"تبني سارة شكلين **منفصلين** جنبًا إلى جنب وفق النمط الموضّح {sh_ar}: **الخطوة ({m(a)})** و**الخطوة ({m(b)})**. "
                f"كم {obj_ar} تحتاج إليها **إجمالًا** لبناء الشكلين معًا؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans - 1, ans - 2, k * (a + b), ans + k], qid
            )
            hint_en = f"Compute Step ({a}) = {k}({a}) + 1 and Step ({b}) = {k}({b}) + 1 separately — remember BOTH figures have their own center dot!"
            hint_ar = f"احسب الخطوة ({a}) والخطوة ({b}) كلًا على حدة — وتذكّر أن لكل شكل منهما نقطة مركزية مستقلة!"
            sol_en = explain_en(
                f"Because the two figures are **separate**, each one has its own `+ 1` center dot (so do NOT just compute `{k}({a}+{b}) + 1`!)!",
                [
                    f"Step ({m(a)}) needs {m(f'{k} \\times {a} + 1 = {da}')} {obj_en}.",
                    f"Step ({m(b)}) needs {m(f'{k} \\times {b} + 1 = {db}')} {obj_en}.",
                    f"Add them together: {m(f'{da} + {db} = {ans}')}.",
                ],
                f"Notice why {m(ans - 1)} is a classic trap: {m(f'{k}({a} + {b}) + 1 = {ans - 1}')} forgets the second figure's center dot!",
            )
            sol_ar = explain_ar(
                "بما أن الشكلين **منفصلان**، فإن لكل شكل منهما نقطته المركزية `+ 1` الخاصة به!",
                [
                    f"الخطوة ({m(a)}) تحتاج {m(f'{k} \\times {a} + 1 = {da}')}.",
                    f"الخطوة ({m(b)}) تحتاج {m(f'{k} \\times {b} + 1 = {db}')}.",
                    f"المجموع الكلي للشكلين معًا: {m(f'{da} + {db} = {ans}')}.",
                ],
                f"انتبه للفخ {m(ans - 1)}: فهو ينسى إضافة `+ 1` للشكل الثاني!",
            )

        else:  # max_box
            box = p1
            ans = (box - 1) // k
            used = k * ans + 1
            left = box - used
            q_en = (
                f"Tariq has a box of {m(box)} {obj_en} and wants to build **one** complete figure from the {sh_en} pattern shown "
                f"(Step 1 uses {m(f1)}, Step 2 uses {m(f2)}, Step 3 uses {m(f3)}). What is the **largest** step number {m('n')} he can build?"
            )
            q_ar = (
                f"لدى طارق علبة فيها {m(box)} {obj_ar} ويريد بناء شكل **واحد** مكتمل من النمط الموضّح {sh_ar} "
                f"(الخطوة 1 تستخدم {m(f1)}، والخطوة 2 تستخدم {m(f2)}، والخطوة 3 تستخدم {m(f3)}). ما **أكبر** رقم خطوة {m('n')} يمكنه بناؤها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, box // k, ans - 1, box // f1], qid
            )
            hint_en = f"Solve {k}n + 1 ≤ {box} in whole numbers: set aside 1 for the center, then see how many full sets of {k} fit in {box - 1}!"
            hint_ar = f"حل المتباينة {k}n + 1 ≤ {box}: احجز قطعة واحدة للمركز، ثم انظر كم مجموعة كاملة من {k} تكفيها الـ {box - 1} المتبقية!"
            sol_en = explain_en(
                f"Set aside **1 piece for the center**, then divide the remaining {m(box - 1)} pieces into complete sets of **{m(k)}**!",
                [
                    f"Step {m('n')} requires {m(f'{k}n + 1 \\le {box}')}, so {m(f'{k}n \\le {box - 1}')}.",
                    f"Divide {m(box - 1)} by {m(k)}: {m(f'{box - 1} = {k} \\times {ans} + {left}')}.",
                    f"So the largest complete step is **Step ({m(ans)})**, using {m(used)} pieces (with {m(left)} left over).",
                ],
                f"Check: Step ({m(ans + 1)}) would require {m(k * (ans + 1) + 1)} pieces, which exceeds {m(box)}!",
            )
            sol_ar = explain_ar(
                f"نحجز **قطعة واحدة للمركز** أولًا، ثم نقسم الـ {m(box - 1)} الباقية إلى مجموعات كاملة من **{m(k)}**!",
                [
                    f"تحتاج الخطوة {m('n')} إلى {m(f'{k}n + 1 \\le {box}')}، أي {m(f'{k}n \\le {box - 1}')}.",
                    f"بقسمة {m(box - 1)} على {m(k)} نحصل على {m(ans)} والباقي {m(left)}.",
                    f"إذن أكبر خطوة مكتملة هي **الخطوة ({m(ans)})** وتستهلك {m(used)} قطعة.",
                ],
                f"تحقق: الخطوة ({m(ans + 1)}) تحتاج {m(k * (ans + 1) + 1)} قطعة وهذا أكبر من {m(box)}!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-dot-array-growth",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 8. g67-function-machine-2step (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    def _apply_op(v: int, op: tuple[str, int]) -> int:
        kind, c = op
        if kind == "add":
            return v + c
        if kind == "sub":
            return v - c
        if kind == "mul":
            return v * c
        assert v % c == 0
        return v // c

    def _op_lbl(op: tuple[str, int]) -> str:
        sym = {"add": "+", "sub": "−", "mul": "×", "div": "÷"}[op[0]]
        return f"{sym} {op[1]}"

    def _inv_desc_en(op: tuple[str, int]) -> str:
        inv = {"add": f"subtract {m(op[1])}", "sub": f"add {m(op[1])}", "mul": f"divide by {m(op[1])}", "div": f"multiply by {m(op[1])}"}
        return inv[op[0]]

    def _inv_desc_ar(op: tuple[str, int]) -> str:
        inv = {"add": f"نطرح {m(op[1])}", "sub": f"نجمع {m(op[1])}", "mul": f"نقسم على {m(op[1])}", "div": f"نضرب في {m(op[1])}"}
        return inv[op[0]]

    fm_std_cases = [
        # (x, op1, op2, mode, diff)
        (7, ("mul", 4), ("add", 5), "fwd", "Easy"),
        (9, ("add", 6), ("mul", 3), "fwd", "Easy"),
        (12, ("sub", 5), ("mul", 6), "fwd", "Easy"),
        (36, ("div", 4), ("add", 11), "fwd", "Easy"),
        (8, ("mul", 5), ("sub", 13), "fwd", "Easy"),
        (24, ("add", 12), ("div", 3), "fwd", "Easy"),
        (8, ("mul", 3), ("add", 7), "bwd", "Medium"),
        (11, ("add", 5), ("mul", 4), "bwd", "Medium"),
        (9, ("mul", 6), ("sub", 8), "bwd", "Medium"),
        (15, ("sub", 6), ("mul", 5), "bwd", "Medium"),
        (28, ("div", 4), ("add", 9), "bwd", "Medium"),
        (14, ("add", 10), ("div", 3), "bwd", "Medium"),
        (12, ("mul", 4), ("div", 3), "bwd", "Medium"),
    ]
    for x, op1, op2, mode, diff in fm_std_cases:
        qid = next_id()
        mid = _apply_op(x, op1)
        y = _apply_op(mid, op2)
        l1, l2 = _op_lbl(op1), _op_lbl(op2)

        if mode == "fwd":
            ans = y
            svg = svg_function_machine(str(x), l1, l2, "?")
            wrong_order = (
                (x + op2[1]) * op1[1]
                if op1[0] == "mul" and op2[0] == "add"
                else (x + op1[1] * op2[1] if op1[0] == "add" and op2[0] == "mul" else ans + 6)
            )
            q_en = (
                f"A two-step number machine takes the input {m(x)}, applies **{l1}** in the first box, "
                f"and then applies **{l2}** in the second box as shown. What **output** number comes out?"
            )
            q_ar = (
                f"تستقبل آلة الأعداد ذات الخطوتين المدخل {m(x)}، فتطبّق عليه العملية **{l1}** في الصندوق الأول، "
                f"ثم العملية **{l2}** في الصندوق الثاني كما في الشكل. ما العدد **المخرج** النهائي؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [wrong_order, mid, ans + op2[1], max(1, ans - op1[1])], qid
            )
            hint_en = "Follow the arrows strictly from left to right: finish Box 1 completely before feeding that result into Box 2!"
            hint_ar = "اتبع الأسهم بالترتيب من اليسار إلى اليمين: احسب ناتج الصندوق الأول أولًا ثم أدخله في الصندوق الثاني!"
            sol_en = explain_en(
                "A function machine processes numbers **in pipeline order** (Box 1 first, then Box 2 on that intermediate result)!",
                [
                    f"**Box 1 ({l1}):** starting from {m(x)}, we get {m(mid)}.",
                    f"**Box 2 ({l2}):** applying {l2} to {m(mid)} gives **{m(ans)}**.",
                ],
                f"Order matters: swapping the two boxes would give a completely different result!",
            )
            sol_ar = explain_ar(
                "تعمل آلة الأعداد **بتسلسل الأسهم** (الصندوق الأول أولًا، ثم يدخل ناتجه مباشرة في الصندوق الثاني)!",
                [
                    f"**الصندوق الأول ({l1}):** نطبّق العملية على {m(x)} فنحصل على {m(mid)}.",
                    f"**الصندوق الثاني ({l2}):** نطبّق العملية على {m(mid)} فنحصل على **{m(ans)}**.",
                ],
                f"تحقق: السير خطوة بخطوة مع الأسهم يضمن عدم الخلط في ترتيب العمليات.",
            )
        else:
            ans = x
            svg = svg_function_machine("?", l1, l2, str(y))
            q_en = (
                f"When a mystery input number enters the two-step machine (**{l1}** followed by **{l2}**) as shown, "
                f"the final output is {m(y)}. What was the **input** number?"
            )
            q_ar = (
                f"عند إدخال عدد مجهول في آلة الخطوتين (**{l1}** يتبعها **{l2}**) الموضّحة في الشكل، "
                f"كان المخرج النهائي {m(y)}. ما العدد **المدخل** الذي بدأنا به؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [mid, ans + op1[1], max(1, ans - 2), ans + 3], qid
            )
            hint_en = f"Work backwards from {y}! Undo the LAST box ({l2}) first, then undo the FIRST box ({l1})."
            hint_ar = f"اعمل عكسيًا بدءًا من {y}! اعكس عملية الصندوق الأخير ({l2}) أولًا، ثم اعكس عملية الصندوق الأول ({l1})."
            sol_en = explain_en(
                "Just like untying shoes before taking off socks, **undo the last box first** using opposite operations!",
                [
                    f"Start at the output {m(y)} and undo **{l2}** ({_inv_desc_en(op2)}): we get the middle number {m(mid)}.",
                    f"Now undo **{l1}** ({_inv_desc_en(op1)}) on {m(mid)}: we get the starting input **{m(ans)}**.",
                ],
                f"Forward check: {m(ans)} → ({l1}) → {m(mid)} → ({l2}) → {m(y)}. Exact match!",
            )
            sol_ar = explain_ar(
                "للرجوع إلى البداية، **نعكس العملية الأخيرة أولًا** ثم العملية الأولى باستخدام العمليات العكسية!",
                [
                    f"نبدأ من المخرج {m(y)} ونعكس **{l2}** ({_inv_desc_ar(op2)}) فنحصل على العدد الأوسط {m(mid)}.",
                    f"ثم نعكس **{l1}** ({_inv_desc_ar(op1)}) على {m(mid)} فنجد العدد المدخل **{m(ans)}**.",
                ],
                f"تحقق للأمام: {m(ans)} ← ({l1}) ← {m(mid)} ← ({l2}) ← {m(y)}. مطابق تمامًا!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-function-machine-2step",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # 4 Hard function-machine items (2 hidden-constant two-input + 2 self-balancing input)
    fm_hard_cases = [
        ("hidden1", 5, 23, 11, 3, 8),   # [x 3] -> [+ k]: in=5 => 23 (k=8); in=11 => 41
        ("hidden2", 6, 44, 10, 4, 5),   # [+ k] -> [x 4]: in=6 => 44 (k=5); in=10 => 60
        ("bal1", 6, 3, 5, 9, 0),        # [+ 6] -> [x 3] = 5n => 3n+18=5n => n=9
        ("bal2", 4, 15, 1, 5, 0),       # [x 4] -> [- 15] = n => 3n=15 => n=5
    ]
    for kind, a, b, c, d_val, k_val in fm_hard_cases:
        qid = next_id()
        if kind == "hidden1":
            ans = a * 0 + c * d_val + k_val  # 11*3 + 8 = 41
            assert a * d_val + k_val == b
            svg = svg_function_machine("x", f"× {d_val}", "+ k", "y")
            q_en = (
                f"The two-step machine shown multiplies any input {m('x')} by {m(d_val)} and then adds a fixed secret number {m('k')}. "
                f"When {m(f'x = {a}')} enters, the output is {m(b)}. What output comes out when {m(f'x = {c}')} enters the same machine?"
            )
            q_ar = (
                f"تضرب الآلة الموضّحة أي عدد مدخل {m('x')} في {m(d_val)} ثم تضيف عددًا ثابتًا سريًا {m('k')}. "
                f"عندما دخل العدد {m(f'x = {a}')} خرج الناتج {m(b)}. ما المخرج الناتج عند إدخال {m(f'x = {c}')} في الآلة نفسها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [c * d_val, k_val, (c + k_val) * d_val, ans + 3], qid
            )
            hint_en = f"First plug in x = {a} to uncover the secret constant k ({a} × {d_val} + k = {b}), then run x = {c} through!"
            hint_ar = f"عوّض أولًا x = {a} لاكتشاف قيمة الثابت k ({a} × {d_val} + k = {b})، ثم احسب المخرج عند x = {c}!"
            sol_en = explain_en(
                "Use the first test run to unlock the secret number `k`, then run the second input straight through!",
                [
                    f"From input {m(a)}: {m(f'{a} \\times {d_val} + k = {a * d_val} + k = {b}')}, so {m(f'k = {b} - {a * d_val} = {k_val}')}.",
                    f"Now feed {m(f'x = {c}')} into `× {d_val}` then `+ {k_val}`: {m(f'{c} \\times {d_val} + {k_val} = {c * d_val} + {k_val} = {ans}')}.",
                ],
                f"Notice: increasing input by {m(f'{c} - {a} = {c - a}')} increases output by {m(f'{c - a} \\times {d_val} = {(c - a) * d_val}')}, and {m(f'{b} + {(c - a) * d_val} = {ans}')}!",
            )
            sol_ar = explain_ar(
                "نستخدم التجربة الأولى لكشف العدد السري `k`، ثم نطبّق الآلة على المدخل الجديد!",
                [
                    f"من المدخل {m(a)}: {m(f'{a} \\times {d_val} + k = {b}')}، أي {m(f'{a * d_val} + k = {b}')} ومنها {m(f'k = {k_val}')}.",
                    f"الآن ندخل {m(f'x = {c}')}: {m(f'{c} \\times {d_val} + {k_val} = {c * d_val} + {k_val} = {ans}')}.",
                ],
                f"تحقق سريع: زاد المدخل بمقدار {m(c - a)} فيزيد المخرج بمقدار {m(f'{c - a} \\times {d_val} = {(c - a) * d_val}')}، و{m(f'{b} + {(c - a) * d_val} = {ans}')}!",
            )
        elif kind == "hidden2":
            assert (a + k_val) * d_val == b
            ans = (c + k_val) * d_val
            svg = svg_function_machine("x", "+ k", f"× {d_val}", "y")
            q_en = (
                f"The two-step machine shown adds a fixed secret number {m('k')} to the input {m('x')}, and then multiplies the result by {m(d_val)}. "
                f"When {m(f'x = {a}')} enters, the output is {m(b)}. What is the output when {m(f'x = {c}')} enters?"
            )
            q_ar = (
                f"تضيف الآلة الموضّحة عددًا ثابتًا سريًا {m('k')} إلى المدخل {m('x')}، ثم تضرب الناتج في {m(d_val)}. "
                f"عندما دخل العدد {m(f'x = {a}')} خرج الناتج {m(b)}. ما المخرج عند إدخال {m(f'x = {c}')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [c * d_val + k_val, b + (c - a), ans - d_val, ans + d_val], qid
            )
            hint_en = f"Divide {b} by {d_val} first to find ({a} + k), solve for k, and then evaluate ({c} + k) × {d_val}!"
            hint_ar = f"اقسم {b} على {d_val} أولًا لمعرفة قيمة ({a} + k)، واستنتج k ثم احسب ({c} + k) × {d_val}!"
            sol_en = explain_en(
                "Undo `× 4` on the first test run to uncover `k`, then run `x = 10` forward!",
                [
                    f"Since {m(f'({a} + k) \\times {d_val} = {b}')}, divide by {m(d_val)}: {m(f'{a} + k = {b // d_val}')}, so {m(f'k = {k_val}')}.",
                    f"For {m(f'x = {c}')}: {m(f'({c} + {k_val}) \\times {d_val} = {c + k_val} \\times {d_val} = {ans}')}.",
                ],
                f"Trap check: don't write {m(f'{c} \\times {d_val} + {k_val} = {c * d_val + k_val}')} — `+ k` happens **before** `× {d_val}`!",
            )
            sol_ar = explain_ar(
                "نعكس الضرب في التجربة الأولى لمعرفة `k`، ثم نطبّق الآلة بالترتيب الصحيح على `x = 10`!",
                [
                    f"بما أن {m(f'({a} + k) \\times {d_val} = {b}')}، نقسم على {m(d_val)} فنجد {m(f'{a} + k = {b // d_val}')}، إذن {m(f'k = {k_val}')}.",
                    f"عند {m(f'x = {c}')}: {m(f'({c} + {k_val}) \\times {d_val} = {c + k_val} \\times {d_val} = {ans}')}.",
                ],
                f"انتبه للترتيب: الجمع مع `{k_val}` يتم **قبل** الضرب في `{d_val}`!",
            )
        elif kind == "bal1":
            ans = d_val  # 9
            assert (ans + a) * b == c * ans
            svg = svg_function_machine("n", f"+ {a}", f"× {b}", f"{c}n")
            q_en = (
                f"A positive number {m('n')} enters the machine shown (**+ {a}** followed by **× {b}**), "
                f"and the output turns out to be **exactly {m(c)} times** the starting number ({m(f'{c}n')}). What is {m('n')}?"
            )
            q_ar = (
                f"يدخل عدد موجب {m('n')} في الآلة الموضّحة (**+ {a}** يتبعها **× {b}**)، "
                f"فيخرج الناتج مساويًا **{m(c)} أمثال** العدد الأصلي ({m(f'{c}n')}) بالضبط. ما قيمة {m('n')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [a, ans + 3, ans - 3, a * b], qid
            )
            hint_en = f"Write the machine's output as {b}(n + {a}) = {b}n + {a * b}, and set it equal to {c}n!"
            hint_ar = f"اكتب مخرج الآلة على الصورة {b}(n + {a}) = {b}n + {a * b} وساوِه بالمقدار {c}n!"
            sol_en = explain_en(
                "Translate the two boxes into an algebraic expression and balance both sides!",
                [
                    f"After `+ {a}` we have {m(f'n + {a}')}; after `× {b}` we have {m(f'{b}(n + {a}) = {b}n + {a * b}')}.",
                    f"Set this equal to {m(f'{c}n')}: {m(f'{b}n + {a * b} = {c}n')}.",
                    f"Subtract {m(f'{b}n')} from both sides: {m(f'{c - b}n = {a * b}')}, so {m(f'n = {ans}')}.",
                ],
                f"Check: {m(f'({ans} + {a}) \\times {b} = {ans + a} \\times {b} = {(ans + a) * b}')}, which equals {m(f'{c} \\times {ans} = {c * ans}')}!",
            )
            sol_ar = explain_ar(
                "نعبّر عن خطوتي الآلة جبريًا ثم نوازن الطرفين!",
                [
                    f"بعد `+ {a}` يصبح المقدار {m(f'n + {a}')}، وبعد `× {b}` يصبح {m(f'{b}(n + {a}) = {b}n + {a * b}')}.",
                    f"نساوي الناتج بالمخرج {m(f'{c}n')}: {m(f'{b}n + {a * b} = {c}n')}.",
                    f"نطرح {m(f'{b}n')} من الطرفين: {m(f'{c - b}n = {a * b}')}، ومنها {m(f'n = {ans}')}.",
                ],
                f"تحقق: {m(f'({ans} + {a}) \\times {b} = {(ans + a) * b}')}، وهو يساوي {m(f'{c} \\times {ans} = {c * ans}')} بالضبط!",
            )
        else:  # bal2
            ans = d_val  # 5
            assert ans * a - b == ans
            svg = svg_function_machine("n", f"× {a}", f"− {b}", "n")
            q_en = (
                f"When a certain number {m('n')} enters the machine shown (**× {a}** followed by **− {b}**), "
                f"the output equals the **exact same number {m('n')}** that went in! What is {m('n')}?"
            )
            q_ar = (
                f"عند إدخال عدد معيّن {m('n')} في الآلة الموضّحة (**× {a}** يتبعها **− {b}**)، "
                f"كان المخرج مساويًا **للعدد {m('n')} نفسه** تمامًا! ما قيمة {m('n')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 2, ans - 1, b, a * 2], qid
            )
            hint_en = f"Write {a}n − {b} = n: if {a}n is {b} more than n, then ({a - 1})n must equal {b}!"
            hint_ar = f"اكتب المعادلة {a}n − {b} = n: هذا يعني أن الفرق {a - 1}n يساوي {b}!"
            sol_en = explain_en(
                f"If multiplying `n` by {m(a)} and subtracting {m(b)} brings you right back to `n`, then the extra `{a - 1}n` equals {m(b)}!",
                [
                    f"Write the machine equation: {m(f'{a}n - {b} = n')}.",
                    f"Subtract {m('n')} and add {m(b)}: {m(f'{a - 1}n = {b}')}.",
                    f"Divide by {m(a - 1)}: {m(f'n = {b} \\div {a - 1} = {ans}')}.",
                ],
                f"Check: {m(f'{ans} \\times {a} - {b} = {ans * a} - {b} = {ans}')} — out comes {m(ans)} again!",
            )
            sol_ar = explain_ar(
                f"إذا كان ضرب `n` في {m(a)} ثم طرح {m(b)} يعيدنا إلى `n` نفسه، فإن الزيادة `{a - 1}n` تساوي {m(b)}!",
                [
                    f"نكتب معادلة الآلة: {m(f'{a}n - {b} = n')}.",
                    f"نرتّب المعادلة فنجد: {m(f'{a - 1}n = {b}')}.",
                    f"نقسم على {m(a - 1)}: {m(f'n = {b} \\div {a - 1} = {ans}')}.",
                ],
                f"تحقق: {m(f'{ans} \\times {a} - {b} = {ans * a} - {b} = {ans}')} فعلًا!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", "Hard", "g67-function-machine-2step",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 9. g67-additive-number-pyramid (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    pyr_cases = [
        # (a, b, c, mode, diff)
        (4, 7, 5, "top", "Easy"),
        (6, 9, 8, "top", "Easy"),
        (3, 11, 6, "top", "Easy"),
        (8, 5, 12, "top", "Easy"),
        (9, 10, 4, "top", "Easy"),
        (5, 8, 7, "center", "Medium"),
        (9, 6, 11, "center", "Medium"),
        (4, 12, 8, "center", "Medium"),
        (7, 15, 6, "center", "Medium"),
        (6, 9, 10, "corner_r", "Medium"),
        (11, 7, 13, "corner_r", "Medium"),
        (8, 12, 5, "corner_l", "Medium"),
        (9, 7, 11, "chain_a", "Hard"),
        (13, 8, 6, "chain_a", "Hard"),
        (6, 8, 10, "consec_x", "Hard"),
        (11, 9, 11, "sym_x", "Hard"),
    ]
    for a, b, c, mode, diff in pyr_cases:
        qid = next_id()
        ml, mr = a + b, b + c
        top = ml + mr
        assert top == a + 2 * b + c

        if mode == "top":
            ans = top
            svg = svg_number_pyramid("?", "", "", str(a), str(b), str(c))
            q_en = (
                f"In the additive number pyramid shown, every brick above the bottom row equals the **sum of the two bricks directly below it**, "
                f"and the bottom row reads {m(a)}, {m(b)}, and {m(c)}. What number belongs in the **top** brick `{m('?')}`?"
            )
            q_ar = (
                f"في هرم الأعداد الجمعي الموضّح، كل لبنة فوق الصف السفلي تساوي **مجموع اللبنتين اللتين تحتها مباشرة**، "
                f"وأعداد الصف السفلي هي {m(a)} و{m(b)} و{m(c)}. ما العدد الذي يوضع في اللبنة **العليا** `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [a + b + c, ans + b, ml, ans - 2], qid
            )
            hint_en = f"Fill the middle row first ({a} + {b} on the left and {b} + {c} on the right), then add those two together!"
            hint_ar = f"املأ الصف الأوسط أولًا ({a} + {b} يسارًا و{b} + {c} يمينًا)، ثم اجمع العددين معًا!"
            sol_en = explain_en(
                f"Notice why the middle bottom brick {m(b)} gets counted **twice**: it feeds into **both** middle-row bricks (`Top = a + 2b + c`)!",
                [
                    f"Middle-left brick: {m(f'{a} + {b} = {ml}')}. Middle-right brick: {m(f'{b} + {c} = {mr}')}.",
                    f"Top brick: {m(f'{ml} + {mr} = {ans}')}.",
                ],
                f"Shortcut check: {m(f'{a} + 2 \\times {b} + {c} = {a} + {2 * b} + {c} = {ans}')} (whereas {m(a + b + c)} forgets the second {m(b)})!",
            )
            sol_ar = explain_ar(
                f"لاحظ أن اللبنة الوسطى {m(b)} تدخل في جمع **كلتا** لبنتي الصف الأوسط، لذا تُحسب **مرتين** (`القمة = أ + 2ب + ج`)!",
                [
                    f"اللبنة الوسطى اليسرى: {m(f'{a} + {b} = {ml}')}، واللبنة الوسطى اليمنى: {m(f'{b} + {c} = {mr}')}.",
                    f"لبنة القمة: {m(f'{ml} + {mr} = {ans}')}.",
                ],
                f"تحقق بالقاعدة السريعة: {m(f'{a} + 2 \\times {b} + {c} = {ans}')}.",
            )

        elif mode == "center":
            ans = b
            svg = svg_number_pyramid(str(top), "", "", str(a), "?", str(c))
            q_en = (
                f"In this additive number pyramid (each brick is the sum of the two bricks directly below it), "
                f"the top brick is {m(top)} and the two bottom corner bricks are {m(a)} and {m(c)}. What number belongs in the **bottom-center** brick `{m('?')}`?"
            )
            q_ar = (
                f"في هرم الأعداد الجمعي الموضّح (كل لبنة تساوي مجموع اللبنتين تحتها مباشرة)، "
                f"قيمة القمة {m(top)} وركنا الصف السفلي هما {m(a)} و{m(c)}. ما العدد المفقود في **وسط الصف السفلي** `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [top - a - c, ans + 2, max(1, ans - 2), (top - a) // 2], qid
            )
            hint_en = "Call the bottom-center brick b: the middle row is (a + b) and (b + c), so the top brick equals a + 2b + c!"
            hint_ar = "سمِّ اللبنة الوسطى b: عندئذ يكون الصف الأوسط (a + b) و(b + c)، فتكون القمة مساوية a + 2b + c!"
            sol_en = explain_en(
                "Use the pyramid superpower: **Top = Left Corner + 2 × Center + Right Corner**!",
                [
                    f"Let the missing center brick be {m('b')}. Then the middle bricks are {m(f'{a} + b')} and {m(f'b + {c}')}.",
                    f"Adding them gives the top: {m(f'{a} + 2b + {c} = {top}')}, so {m(f'2b = {top} - {a + c} = {2 * b}')}.",
                    f"Divide by {m(2)}: {m(f'b = {2 * b} \\div 2 = {ans}')}.",
                ],
                f"Check: middle row becomes {m(ml)} and {m(mr)}, and {m(f'{ml} + {mr} = {top}')}!",
            )
            sol_ar = explain_ar(
                "استخدم القاعدة الذهبية للهرم الثلاثي: **القمة = الركن الأيسر + 2 × الوسط + الركن الأيمن**!",
                [
                    f"نفرض أن لبنة الوسط هي {m('b')}، فيكون الصف الأوسط {m(f'{a} + b')} و{m(f'b + {c}')}.",
                    f"مجموعهما يعطي القمة: {m(f'{a} + 2b + {c} = {top}')}، إذن {m(f'2b = {top} - {a + c} = {2 * b}')}.",
                    f"بالقسمة على {m(2)} نجد {m(f'b = {ans}')}.",
                ],
                f"تحقق: الصف الأوسط يصبح {m(ml)} و{m(mr)}، ومجموعهما {m(top)} بالضبط!",
            )

        elif mode in ("corner_r", "corner_l"):
            if mode == "corner_r":
                ans = c
                svg = svg_number_pyramid(str(top), "", "", str(a), str(b), "?")
                known_lbl_en, known_lbl_ar = f"left ({m(a)}) and middle ({m(b)})", f"اليسرى ({m(a)}) والوسطى ({m(b)})"
            else:
                ans = a
                svg = svg_number_pyramid(str(top), "", "", "?", str(b), str(c))
                known_lbl_en, known_lbl_ar = f"middle ({m(b)}) and right ({m(c)})", f"الوسطى ({m(b)}) واليمنى ({m(c)})"
            q_en = (
                f"In the additive number pyramid shown, each upper brick equals the sum of the two bricks directly below it. "
                f"Given top brick {m(top)} and bottom {known_lbl_en} bricks, what is the missing bottom corner brick `{m('?')}`?"
            )
            q_ar = (
                f"في هرم الأعداد الجمعي الموضّح، كل لبنة علوية تساوي مجموع اللبنتين تحتها مباشرة. "
                f"إذا علمت أن القمة {m(top)} واللبنتين السفليتين {known_lbl_ar}، فما قيمة لبنة الركن المفقودة `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + b, max(1, ans - 2), ans + 3, mr if mode == "corner_r" else ml], qid
            )
            hint_en = "Fill the middle-row brick above the two known bottom numbers first, subtract from the top to get the other middle brick, then subtract b!"
            hint_ar = "احسب أولًا لبنة الصف الأوسط فوق العددين المعلومين، ثم اطرحها من القمة لمعرفة لبنة الوسط الأخرى، ومنها استنتج الركن!"
            sol_en = explain_en(
                "Climb up on the known side, cross over at the top, and climb down to the unknown corner!",
                [
                    f"Using {m(f'a + 2b + c = {top}')} with middle brick {m(f'b = {b}')} ({m(f'2b = {2 * b}')}):",
                    f"Subtract {m(2 * b)} and the known corner ({m(top - 2 * b - ans)}) from {m(top)}: `{m('?')} = {m(f'{top} - {2 * b} - {top - 2 * b - ans} = {ans}')}`.",
                ],
                f"Check: bottom row `{a}, {b}, {c}` → middle row `{ml}, {mr}` → top `{top}`!",
            )
            sol_ar = explain_ar(
                "نطبّق قاعدة `القمة = الركن الأيسر + 2 × الوسط + الركن الأيمن` (أو نصعد من الجهة المعلومة ثم ننزل للمجهولة)!",
                [
                    f"بما أن لبنة الوسط {m(b)} تُحسب مرتين ({m(f'2 \\times {b} = {2 * b}')})، نطرح {m(2 * b)} والركن المعلوم ({m(top - 2 * b - ans)}) من القمة {m(top)}.",
                    f"نجد لبنة الركن المفقودة: {m(f'{top} - {2 * b} - {top - 2 * b - ans} = {ans}')}.",
                ],
                f"تحقق: الصف السفلي `{a}، {b}، {c}` يعطي الصف الأوسط `{ml}، {mr}` وقمته `{top}`!",
            )

        elif mode == "chain_a":
            ans = a
            svg = svg_number_pyramid(str(top), str(ml), "", "?", "", str(c))
            q_en = (
                f"In the additive pyramid shown (each brick is the sum of the two bricks directly beneath it), "
                f"the top brick is {m(top)}, the middle-left brick is {m(ml)}, and the bottom-right brick is {m(c)}. "
                f"What number goes in the **bottom-left** brick `{m('?')}`?"
            )
            q_ar = (
                f"في هرم الأعداد الجمعي الموضّح (كل لبنة تساوي مجموع اللبنتين تحتها مباشرة)، "
                f"القمة تساوي {m(top)}، واللبنة الوسطى اليسرى {m(ml)}، والركن السفلي الأيمن {m(c)}. "
                f"ما العدد الذي يوضع في **الركن السفلي الأيسر** `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [b, mr, ans + 2, max(1, ans - 2)], qid
            )
            hint_en = f"Step 1: middle-right = {top} − {ml}. Step 2: bottom-center = middle-right − {c}. Step 3: bottom-left = {ml} − bottom-center!"
            hint_ar = f"الخطوة 1: الوسطى اليمنى = {top} − {ml}. الخطوة 2: وسط القاعدة = الوسطى اليمنى − {c}. الخطوة 3: الركن الأيسر = {ml} − وسط القاعدة!"
            sol_en = explain_en(
                "Unlock one blank brick at a time from top-right down to bottom-center, then over to bottom-left!",
                [
                    f"**Middle-right brick:** {m(f'{top} - {ml} = {mr}')}.",
                    f"**Bottom-center brick:** {m(f'{mr} - {c} = {b}')}.",
                    f"**Bottom-left brick `?`:** {m(f'{ml} - {b} = {ans}')}.",
                ],
                f"Check: `{ans}, {b}, {c}` → `{ml}, {mr}` → `{top}`. Every single brick checks out!",
            )
            sol_ar = explain_ar(
                "نكشف اللبنات الفارغة واحدة تلو الأخرى بالترتيب من القمة نزولًا إلى القاعدة!",
                [
                    f"**اللبنة الوسطى اليمنى:** {m(f'{top} - {ml} = {mr}')}.",
                    f"**لبنة وسط القاعدة:** {m(f'{mr} - {c} = {b}')}.",
                    f"**الركن السفلي الأيسر `؟`:** {m(f'{ml} - {b} = {ans}')}.",
                ],
                f"تحقق: القاعدة `{ans}، {b}، {c}` تعطي `{ml}، {mr}` ثم القمة `{top}`!",
            )

        elif mode == "consec_x":
            ans = a  # 6, with b=8, c=10 => x, x+2, x+4
            svg = svg_number_pyramid(str(top), "", "", "x", "x + 2", "x + 4")
            q_en = (
                f"In the additive number pyramid shown, the bottom row contains three consecutive even numbers "
                f"{m('x')}, {m('x + 2')}, and {m('x + 4')}, and the top brick equals {m(top)}. What is the value of {m('x')}?"
            )
            q_ar = (
                f"في هرم الأعداد الجمعي الموضّح، يحتوي الصف السفلي على ثلاثة أعداد زوجية متتالية هي "
                f"{m('x')} و{m('x + 2')} و{m('x + 4')}، وقيمة لبنة القمة تساوي {m(top)}. ما قيمة {m('x')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [b, c, ans + 1, ans - 2], qid
            )
            hint_en = f"Using Top = left + 2(middle) + right gives x + 2(x + 2) + (x + 4) = 4x + 8 = {top}!"
            hint_ar = f"بتطبيق قاعدة القمة = الأيسر + 2(الأوسط) + الأيمن نحصل على 4x + 8 = {top}!"
            sol_en = explain_en(
                "Express the middle row and top brick in terms of `x`!",
                [
                    f"Middle-left = {m('x + (x + 2) = 2x + 2')}; middle-right = {m('(x + 2) + (x + 4) = 2x + 6')}.",
                    f"Top brick = {m(f'(2x + 2) + (2x + 6) = 4x + 8 = {top}')}.",
                    f"Subtract {m(8)} and divide by {m(4)}: {m(f'4x = {top - 8}')} → {m(f'x = {ans}')}.",
                ],
                f"Check: `{ans}, {ans + 2}, {ans + 4}` → `{2 * ans + 2}, {2 * ans + 6}` → `{top}`!",
            )
            sol_ar = explain_ar(
                "نعبّر عن الصف الأوسط ثم القمة بدلالة `x` فتنحل المعادلة بسهولة!",
                [
                    f"الصف الأوسط هو {m('2x + 2')} و{m('2x + 6')}.",
                    f"القمة تساوي مجموعهما: {m(f'4x + 8 = {top}')}.",
                    f"نطرح {m(8)} ثم نقسم على {m(4)}: {m(f'4x = {top - 8}')} ومنها {m(f'x = {ans}')}.",
                ],
                f"تحقق: الأعداد `{ans}، {ans + 2}، {ans + 4}` تعطي الصف الأوسط `{ml}، {mr}` والقمة `{top}`!",
            )

        else:  # sym_x: x, b, x
            ans = a
            svg = svg_number_pyramid(str(top), "", "", "x", str(b), "x")
            q_en = (
                f"In the symmetric additive pyramid shown, both outer bottom bricks equal the same number {m('x')}, "
                f"the bottom-center brick is {m(b)}, and the top brick is {m(top)}. What is the value of {m('x')}?"
            )
            q_ar = (
                f"في الهرم الجمعي المتماثل الموضّح، يتساوى ركنا القاعدة ويساوي كل منهما {m('x')}، "
                f"ولبنة وسط القاعدة {m(b)}، والقمة {m(top)}. ما قيمة {m('x')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ml, (top - b) // 2, ans + 2, ans - 2], qid
            )
            hint_en = f"Because the pyramid is symmetric, both middle-row bricks are equal! Each middle brick is {top} ÷ 2 = {top // 2}."
            hint_ar = f"بما أن الهرم متماثل، فإن لبنتي الصف الأوسط متساويتان، وكل واحدة منهما تساوي {top} ÷ 2 = {top // 2}!"
            sol_en = explain_en(
                f"Symmetry makes this super clean: both middle bricks equal {m(f'x + {b}')}, so each one is half of {m(top)}!",
                [
                    f"Divide the top brick {m(top)} into two equal middle bricks: {m(f'{top} \\div 2 = {ml}')}.",
                    f"Since {m(f'x + {b} = {ml}')}, subtract {m(b)}: {m(f'x = {ml} - {b} = {ans}')}.",
                ],
                f"Check: `{ans}, {b}, {ans}` → `{ml}, {ml}` → `{top}`!",
            )
            sol_ar = explain_ar(
                f"التماثل يختصر الحل فورًا: لبنتا الصف الأوسط متساويتان وتساوي كل منهما {m(f'x + {b}')} أي نصف القمة {m(top)}!",
                [
                    f"قيمة كل لبنة في الصف الأوسط: {m(f'{top} \\div 2 = {ml}')}.",
                    f"وبما أن {m(f'x + {b} = {ml}')}، نطرح {m(b)} فنجد {m(f'x = {ml} - {b} = {ans}')}.",
                ],
                f"تحقق: `{ans}، {b}، {ans}` تعطي `{ml}، {ml}` ومجموعهما `{top}`!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-additive-number-pyramid",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    assert len(items) == 50
    return items


def _gen_group_1_4(next_id) -> list[dict]:
    """Lesson 1.4 group (50 Qs, Topic: 'Algebra'):
    10. g67-fencepost-tree-spacing (17 Qs)
    11. g67-opposite-meet-trains (17 Qs)
    12. g67-heads-legs-two-values (16 Qs)
    """
    items: list[dict] = []

    # -------------------------------------------------------------------------
    # 10. g67-fencepost-tree-spacing (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    fp_cases = [
        # (p1, p2, p3, mode, diff, ctx_en, ctx_ar)
        (120, 8, 0, "one_cnt", "Easy", "palm trees along one side of a straight walkway", "نخلة على جانب واحد من ممر مستقيم"),
        (180, 12, 0, "one_cnt", "Easy", "solar lamp-posts along one edge of a straight promenade", "عمود إنارة شمسي على حافة ممشى مستقيم"),
        (150, 6, 0, "one_cnt", "Easy", "wooden fenceposts along a straight garden border", "وتد خشبي على طول حدود حديقة مستقيمة"),
        (240, 15, 0, "one_cnt", "Easy", "banners along one side of a straight parade road", "راية على جانب واحد من طريق استعراض مستقيم"),
        (19, 5, 0, "one_len", "Easy", "olive trees", "شجرة زيتون"),
        (25, 4, 0, "one_len", "Easy", "stone bollards", "عمودًا حجريًا"),
        (140, 10, 0, "both_cnt", "Medium", "trees along **both** sides of a straight avenue", "شجرة على **كلا جانبي** شارع مستقيم"),
        (160, 8, 0, "both_cnt", "Medium", "streetlights along **both** sides of a straight bridge", "عمود إنارة على **كلا جانبي** جسر مستقيم"),
        (210, 15, 0, "both_cnt", "Medium", "flags along **both** sides of a straight campus mall", "علمًا على **كلا جانبي** ساحة جامعية مستقيمة"),
        (400, 16, 0, "loop_cnt", "Medium", "markers around a **closed circular** running track", "علامة حول مضمار جري **دائري مغلق**"),
        (360, 12, 0, "loop_cnt", "Medium", "lanterns around the perimeter of a **closed** pond path", "فانوسًا حول مسار بركة **مغلق**"),
        (22, 150, 0, "both_gap", "Medium", "lamp-posts", "عمود إنارة"),
        (34, 240, 0, "both_gap", "Medium", "flagpoles", "سارية علم"),
        (5, 24, 11, "jogger", "Hard", "Omar", "عمر"),
        (7, 30, 16, "jogger", "Hard", "Lina", "لينا"),
        (180, 9, 0, "no_ends", "Hard", "cedar saplings", "شتلة أرز"),
        (120, 10, 3, "roses", "Hard", "rose bushes", "شجيرة ورد"),
    ]
    for p1, p2, p3, mode, diff, ctx_en, ctx_ar in fp_cases:
        qid = next_id()
        if mode == "one_cnt":
            L, d = p1, p2
            gaps = L // d
            ans = gaps + 1
            svg_en = svg_fenceposts(f"{d} m", f"{L} m")
            svg_ar = svg_fenceposts(f"{d} م", f"{L} م")
            q_en = (
                f"Workers plant {ctx_en} of length {m(L)} m, placing one every {m(d)} m **including both ends**. "
                f"How many are placed in total?"
            )
            q_ar = (
                f"يضع العمال {ctx_ar} طوله {m(L)} م بحيث تكون المسافة بين كل اثنين متتاليين {m(d)} م **مع وضع واحد عند كل طرف من الطرفين**. "
                f"كم عددها الإجمالي؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [gaps, gaps - 1, ans + 1, 2 * ans], qid
            )
            hint_en = "Fencepost rule: on a straight segment with posts at BOTH ends, Posts = Gaps + 1!"
            hint_ar = "قاعدة الأعمدة والمسافات: على خط مستقيم يشمل الطرفين، عدد الأعمدة = عدد المسافات + 1!"
            sol_en = explain_en(
                "Dividing length by spacing counts **gaps**, and since both ends get a post, **Posts = Gaps + 1**!",
                [
                    f"Number of {m(d)}-m gaps in {m(L)} m: {m(f'{L} \\div {d} = {gaps}')} gaps.",
                    f"Add {m(1)} for the starting post at `0 m`: {m(f'{gaps} + 1 = {ans}')}.",
                ],
                f"Mini test: a {m(2 * d)}-m path with spacing {m(d)} m has {m(2)} gaps (`0, {d}, {2 * d}`), which is {m('2 + 1 = 3')} posts!",
            )
            sol_ar = explain_ar(
                "قسمة الطول الكلي على المسافة البينية تعطي **عدد المسافات**، وبما أن الطرفين مشمولان فإن **العدد = المسافات + 1**!",
                [
                    f"عدد المسافات البينية: {m(f'{L} \\div {d} = {gaps}')} مسافة.",
                    f"نضيف {m(1)} لنقطة البداية: {m(f'{gaps} + 1 = {ans}')}.",
                ],
                f"تحقق مصغّر: مسار طوله {m(2 * d)} م بمسافات {m(d)} م يحوي مسافتين وثلاث نقاط (`0، {d}، {2 * d}`).",
            )

        elif mode == "one_len":
            N, d = p1, p2
            gaps = N - 1
            ans = gaps * d
            svg_en = svg_fenceposts(f"{d} m", "? m")
            svg_ar = svg_fenceposts(f"{d} م", "؟ م")
            q_en = (
                f"A straight walkway has {m(N)} {ctx_en} planted in a single row from the very start to the very end, "
                f"with {m(d)} m between every two consecutive {ctx_en}. What is the total length (in meters) of the walkway?"
            )
            q_ar = (
                f"اصطفت {m(N)} {ctx_ar} في صف مستقيم واحد من بداية الممر حتى نهايته تمامًا، "
                f"بمسافة ثابتة قدرها {m(d)} م بين كل اثنتين متتاليتين. ما الطول الكلي للممر بالأمتار؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [N * d, (N + 1) * d, (N - 2) * d, ans + d // 2 + 2], qid
            )
            hint_en = f"Between {N} posts in a row, there are only {N} − 1 = {gaps} gaps (not {N} gaps)!"
            hint_ar = f"بين {N} عنصرًا في صف واحد، يوجد {N} − 1 = {gaps} مسافة فقط (وليس {N} مسافة)!"
            sol_en = explain_en(
                f"**Gaps = Posts − 1**: {m(N)} items in a line create **{m(gaps)} intervals** between the first and the last!",
                [
                    f"Count the intervals: {m(f'{N} - 1 = {gaps}')} gaps.",
                    f"Multiply by {m(d)} m per gap: {m(f'{gaps} \\times {d} = {ans}')} m.",
                ],
                f"Notice why {m(N * d)} m is too big: the {m(N)}th item marks the end of the {m(gaps)}th gap without starting a new gap!",
            )
            sol_ar = explain_ar(
                f"**عدد المسافات = عدد العناصر − 1**: وجود {m(N)} عنصرًا في خط مستقيم يصنع **{m(gaps)} مسافة** بين الأول والأخير!",
                [
                    f"عدد المسافات البينية: {m(f'{N} - 1 = {gaps}')} مسافة.",
                    f"الطول الكلي: {m(f'{gaps} \\times {d} = {ans}')} مترًا.",
                ],
                f"انتبه: ضرب {m(N)} في {m(d)} يعطي {m(N * d)} م وهو خطأ شائع لأن العنصر الأخير ينهي المسافة ولا يبدأ مسافة جديدة!",
            )

        elif mode == "both_cnt":
            L, d = p1, p2
            one = L // d + 1
            ans = 2 * one
            svg_en = svg_fenceposts(f"{d} m", f"{L} m")
            svg_ar = svg_fenceposts(f"{d} م", f"{L} م")
            q_en = (
                f"City planners install {ctx_en} of length {m(L)} m, spaced every {m(d)} m **including both ends on each side**. "
                f"How many are installed altogether?"
            )
            q_ar = (
                f"يتم تركيب {ctx_ar} طوله {m(L)} م بمسافة {m(d)} م بين كل اثنين متتاليين **مع شمول الطرفين في كل جانب**. "
                f"كم العدد الكلي الذي يتم تركيبه في الجانبين معًا؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [2 * (L // d), one, 2 * (L // d) + 1, ans + 2], qid
            )
            hint_en = "Count ONE side carefully using (L ÷ d + 1), then multiply the entire result by 2 for both sides!"
            hint_ar = "احسب جانبًا واحدًا أولًا بالقاعدة (الطول ÷ المسافة + 1)، ثم اضرب الناتج كاملًا في 2 لكلا الجانبين!"
            sol_en = explain_en(
                "Find the count on **one** side first (`gaps + 1`), then **double** it because BOTH sides have two endpoints!",
                [
                    f"On one side: {m(f'{L} \\div {d} + 1 = {L // d} + 1 = {one}')}.",
                    f"On both sides together: {m(f'2 \\times {one} = {ans}')}.",
                ],
                f"Trap alert: {m(2 * (L // d) + 1)} adds `+ 1` only once instead of adding `+ 1` on **each** side!",
            )
            sol_ar = explain_ar(
                "نحسب العدد في **جانب واحد** أولًا (`المسافات + 1`)، ثم نضاعفه لأن **لكل جانب** نقطة بداية ونقطة نهاية!",
                [
                    f"في الجانب الواحد: {m(f'{L} \\div {d} + 1 = {L // d} + 1 = {one}')}.",
                    f"في الجانبين معًا: {m(f'2 \\times {one} = {ans}')}.",
                ],
                f"تنبيه: القيمة {m(2 * (L // d) + 1)} تضيف `1` مرة واحدة فقط، والصحيح إضافة `1` لكل جانب!",
            )

        elif mode == "loop_cnt":
            L, d = p1, p2
            ans = L // d
            svg_en = svg_fenceposts(f"{d} m", f"loop {L} m")
            svg_ar = svg_fenceposts(f"{d} م", f"مسار مغلق {L} م")
            q_en = (
                f"Organizers place {ctx_en} of total perimeter {m(L)} m, spacing them equally every {m(d)} m all the way around. "
                f"How many are needed?"
            )
            q_ar = (
                f"يضع المنظمون {ctx_ar} محيطه الكلي {m(L)} م على مسافات متساوية قدرها {m(d)} م على امتداد المسار كله. "
                f"كم عددها الإجمالي؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, ans - 1, ans + 2, 2 * ans], qid
            )
            hint_en = "Around a CLOSED loop, the end meets the start — so Posts = Gaps (do NOT add 1)!"
            hint_ar = "حول مسار **مغلق**، تنطبق نقطة النهاية على نقطة البداية — لذا عدد العلامات = عدد المسافات تمامًا (دون + 1)!"
            sol_en = explain_en(
                "When you bend a straight fence into a **closed loop**, the two endposts merge into one—so **Posts = Gaps**!",
                [
                    f"Divide the loop perimeter {m(L)} m by the spacing {m(d)} m: {m(f'{L} \\div {d} = {ans}')}.",
                    f"Because the path closes on itself, no extra `+ 1` post is needed: total = **{m(ans)}**.",
                ],
                f"Mini test: a {m(3 * d)}-m triangle with a post every {m(d)} m has {m(3)} corners and {m(3)} sides ({m('3 = 3')}, not {m(4)})!",
            )
            sol_ar = explain_ar(
                "في أي مسار **مغلق** تندمج نقطة النهاية مع نقطة البداية، فيكون **عدد العناصر = عدد المسافات** بالضبط دون إضافة 1!",
                [
                    f"نقسم المحيط الكلي {m(L)} م على المسافة {m(d)} م: {m(f'{L} \\div {d} = {ans}')}.",
                    f"بما أن المسار مغلق فلا نضيف `1`: الإجمالي = **{m(ans)}**.",
                ],
                f"مثال سريع: مثلث محيطه {m(3 * d)} م بعلامة كل {m(d)} م له {m(3)} أضلاع و{m(3)} رؤوس تمامًا!",
            )

        elif mode == "both_gap":
            N, L = p1, p2
            one = N // 2
            gaps = one - 1
            ans = L // gaps
            svg_en = svg_fenceposts("? m", f"{L} m")
            svg_ar = svg_fenceposts("؟ م", f"{L} م")
            q_en = (
                f"A straight {m(L)}-m bridge has {m(N)} {ctx_en} in total—equally spaced along **both** sides, including the ends of each side. "
                f"What is the distance (in meters) between two adjacent {ctx_en} on the same side?"
            )
            q_ar = (
                f"يوجد على جسر مستقيم طوله {m(L)} م إجمالي {m(N)} {ctx_ar} موزّعة بالتساوي على **كلا الجانبين** شاملة طرفي كل جانب. "
                f"كم مترًا المسافة بين كل اثنين متجاورين في الجانب الواحد؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [L // one, ans + 3, max(2, ans - 3), ans + 5], qid
            )
            hint_en = f"First divide {N} by 2 to see how many stand on ONE side ({one}), then subtract 1 to get the {gaps} gaps!"
            hint_ar = f"اقسم أولًا {N} على 2 لمعرفة العدد في الجانب الواحد ({one})، ثم اطرح 1 لإيجاد عدد المسافات ({gaps})!"
            sol_en = explain_en(
                "Peel the problem back in reverse: **both sides → one side → gaps → spacing**!",
                [
                    f"Posts on **one** side: {m(f'{N} \\div 2 = {one}')}.",
                    f"Gaps on one side: {m(f'{one} - 1 = {gaps}')} equal gaps.",
                    f"Spacing per gap: {m(f'{L} \\div {gaps} = {ans}')} m.",
                ],
                f"Check forward: {m(f'{L} \\div {ans} + 1 = {one}')} per side, times {m(2)} sides = {m(N)}!",
            )
            sol_ar = explain_ar(
                "نعكس الخطوات بهدوء: **الجانبان معًا ← جانب واحد ← عدد المسافات ← طول المسافة الواحدة**!",
                [
                    f"العدد في **الجانب الواحد**: {m(f'{N} \\div 2 = {one}')}.",
                    f"عدد المسافات في الجانب الواحد: {m(f'{one} - 1 = {gaps}')} مسافة.",
                    f"طول المسافة الواحدة: {m(f'{L} \\div {gaps} = {ans}')} م.",
                ],
                f"تحقق للأمام: {m(f'({L} \\div {ans} + 1) \\times 2 = {one} \\times 2 = {N}')}!",
            )

        elif mode == "jogger":
            p_mid, t1, p_end = p1, p2, p3
            g1 = p_mid - 1
            g2 = p_end - 1
            sec_per_gap = t1 // g1
            ans = g2 * sec_per_gap
            svg_en = svg_fenceposts("1 gap", f"Post 1 → Post {p_end}")
            svg_ar = svg_fenceposts("مسافة 1", f"عمود 1 ← عمود {p_end}")
            q_en = (
                f"{ctx_en} jogs at a constant speed along a straight row of equally spaced lamp-posts. "
                f"Starting at the {m(1)}st lamp-post, {ctx_en} reaches the {m(p_mid)}th lamp-post in {m(t1)} seconds. "
                f"At the same speed, how many seconds in total does it take {ctx_en} to go from the {m(1)}st lamp-post to the {m(p_end)}th lamp-post?"
            )
            q_ar = (
                f"يجري {ctx_ar} بسرعة ثابتة بمحاذاة صف مستقيم من أعمدة الإنارة المتساوية التباعد. "
                f"انطلق من العمود رقم {m(1)} فوصل إلى العمود رقم {m(p_mid)} خلال {m(t1)} ثانية. "
                f"بالسرعة نفسها، كم ثانية يستغرقها إجمالًا للوصول من العمود رقم {m(1)} إلى العمود رقم {m(p_end)}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    (t1 * p_end) // p_mid if (t1 * p_end) % p_mid == 0 else ans - sec_per_gap,
                    p_end * sec_per_gap,
                    ans - sec_per_gap,
                    ans + sec_per_gap,
                ],
                qid,
            )
            hint_en = f"Running from Post 1 to Post {p_mid} covers only {p_mid} − 1 = {g1} gaps (NOT {p_mid} gaps)!"
            hint_ar = f"الجري من العمود 1 إلى العمود {p_mid} يقطع {p_mid} − 1 = {g1} مسافات فقط (وليس {p_mid} مسافات)!"
            sol_en = explain_en(
                "Time is proportional to **distance (gaps)**, NOT post numbers! Always subtract 1 to count gaps from Post 1!",
                [
                    f"From Post {m(1)} to Post {m(p_mid)} is {m(f'{p_mid} - 1 = {g1}')} gaps, so each gap takes {m(f'{t1} \\div {g1} = {sec_per_gap}')} seconds.",
                    f"From Post {m(1)} to Post {m(p_end)} is {m(f'{p_end} - 1 = {g2}')} gaps.",
                    f"Total time: {m(f'{g2} \\times {sec_per_gap} = {ans}')} seconds.",
                ],
                f"Notice the classic KMC trap: Post {m(p_end)} is NOT {m(f'{p_end}/{p_mid}')} as far—it is {m(f'{g2}/{g1}')} as many gaps!",
            )
            sol_ar = explain_ar(
                "الزمن يتناسب مع **عدد المسافات المقطوعة** لا مع أرقام الأعمدة! اطرح 1 دائمًا لحساب المسافات من العمود الأول!",
                [
                    f"من العمود {m(1)} إلى العمود {m(p_mid)} توجد {m(f'{p_mid} - 1 = {g1}')} مسافات، أي كل مسافة تستغرق {m(f'{t1} \\div {g1} = {sec_per_gap}')} ثوانٍ.",
                    f"ومن العمود {m(1)} إلى العمود {m(p_end)} توجد {m(f'{p_end} - 1 = {g2}')} مسافة.",
                    f"الزمن الكلي: {m(f'{g2} \\times {sec_per_gap} = {ans}')} ثانية.",
                ],
                f"تحقق: {m(g2)} مسافة × {m(sec_per_gap)} ثوانٍ = {m(ans)} ثانية بالضبط.",
            )

        elif mode == "no_ends":
            L, d = p1, p2
            gaps = L // d
            ans = gaps - 1
            svg_en = svg_fenceposts(f"{d} m", f"{L} m")
            svg_ar = svg_fenceposts(f"{d} م", f"{L} م")
            q_en = (
                f"Two stone gateposts stand {m(L)} m apart at the two ends of a straight wall. "
                f"Gardeners plant {ctx_en} every {m(d)} m along the wall, **excluding both ends** (since the stone gateposts already occupy the ends). "
                f"How many {ctx_en} are planted?"
            )
            q_ar = (
                f"يقف عمودا بوابة حجريان عند طرفي سور مستقيم طوله {m(L)} م. "
                f"يزرع البستانيون {ctx_ar} كل {m(d)} م على امتداد السور **دون الزراعة عند الطرفين** (لوجود عمودي البوابة). "
                f"كم {ctx_ar} تتم زراعتها؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [gaps, gaps + 1, ans - 1, ans + 3], qid
            )
            hint_en = "With BOTH endpoints occupied by gateposts, only the interior division points get saplings: Interior Points = Gaps − 1!"
            hint_ar = "عندما يكون الطرفان مشغولين بعمودي البوابة، تُزرع الشتلات في النقاط الداخلية فقط: النقاط الداخلية = المسافات − 1!"
            sol_en = explain_en(
                "Compare the three spacing cases on `g` gaps: both ends → `g + 1`; closed loop → `g`; **neither end (interior only) → `g − 1`**!",
                [
                    f"Number of {m(d)}-m gaps between the gateposts: {m(f'{L} \\div {d} = {gaps}')}.",
                    f"Including both ends would give {m(gaps + 1)} positions; removing the {m(2)} stone gateposts leaves {m(f'{gaps + 1} - 2 = {ans}')} saplings.",
                ],
                f"Mini test: two gateposts {m(2 * d)} m apart ({m(2)} gaps) have just {m('2 - 1 = 1')} midpoint sapling between them!",
            )
            sol_ar = explain_ar(
                "احفظ الحالات الثلاث لعدد المسافات `g`: بالطرفين `g + 1`، مسار مغلق `g`، **ودون الطرفين (داخليًا فقط) `g − 1`**!",
                [
                    f"عدد المسافات طول كل منها {m(d)} م هو {m(f'{L} \\div {d} = {gaps}')}.",
                    f"لو شملنا الطرفين لحصلنا على {m(gaps + 1)} موضعًا؛ نستبعد الطرفين ({m(2)}) فيتبقى {m(f'{gaps + 1} - 2 = {ans}')} شتلة.",
                ],
                f"مثال صغير: بمسافتين فقط توجد نقطة منتصف واحدة (`2 − 1 = 1`) بين عمودي البوابة!",
            )

        else:  # roses
            L, d, per_gap = p1, p2, p3
            gaps = L // d
            palms = gaps + 1
            ans = gaps * per_gap
            svg_en = svg_fenceposts(f"{d} m", f"{L} m")
            svg_ar = svg_fenceposts(f"{d} م", f"{L} م")
            q_en = (
                f"Along one side of a {m(L)}-m straight garden path, palm trees are planted every {m(d)} m **including both ends** ({m(palms)} palms in all). "
                f"Then {m(per_gap)} {ctx_en} are planted in **every gap** between consecutive palm trees. How many {ctx_en} are planted?"
            )
            q_ar = (
                f"على جانب واحد من ممر حديقة مستقيم طوله {m(L)} م، زُرعت نخلات كل {m(d)} م **بما في ذلك الطرفان** ({m(palms)} نخلة إجمالًا). "
                f"ثم زُرعت {m(per_gap)} من شجيرات الورد في **كل مسافة** بين نخلتين متتاليتين. كم {ctx_ar} زُرعت؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [palms * per_gap, (gaps - 1) * per_gap, ans + per_gap + 1, gaps], qid
            )
            hint_en = f"Rose bushes go inside the GAPS, not on the {palms} palm trees! Count how many gaps exist between {palms} palms."
            hint_ar = f"شجيرات الورد تُزرع في **المسافات** لا فوق النخلات الـ {palms}! احسب عدد المسافات أولًا ثم اضرب في {per_gap}."
            sol_en = explain_en(
                f"Don't multiply by the {m(palms)} palm trees—the rose bushes sit inside the **{m(gaps)} gaps**!",
                [
                    f"Number of {m(d)}-m gaps in {m(L)} m (and between {m(palms)} palms): {m(f'{L} \\div {d} = {gaps}')} gaps.",
                    f"With {m(per_gap)} rose bushes per gap: {m(f'{gaps} \\times {per_gap} = {ans}')} rose bushes.",
                ],
                f"Notice the trap: {m(f'{palms} \\times {per_gap} = {palms * per_gap}')} wrongly plants an extra set after the last palm tree!",
            )
            sol_ar = explain_ar(
                f"لا تضرب في عدد النخلات ({m(palms)})—بل اضرب في **عدد المسافات البينية ({m(gaps)})**!",
                [
                    f"عدد المسافات بين {m(palms)} نخلة هو {m(f'{palms} - 1 = {gaps}')} مسافة.",
                    f"بوضع {m(per_gap)} شجيرات في كل مسافة: {m(f'{gaps} \\times {per_gap} = {ans}')} شجيرة ورد.",
                ],
                f"انتبه للفخ {m(palms * per_gap)}: فهو يفترض خطأً وجود مسافة إضافية بعد النخلة الأخيرة!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-fencepost-tree-spacing",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    # -------------------------------------------------------------------------
    # 11. g67-opposite-meet-trains (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    meet_cases = [
        # (D, v1, v2, extra, mode, diff, veh_en, veh_ar, u_d, u_v, u_t_en, u_t_ar)
        (360, 50, 40, 0, "time", "Easy", "trains", "قطاران", "km", "km/h", "hours", "ساعات"),
        (420, 65, 75, 0, "time", "Easy", "express buses", "حافلتان سريعتان", "km", "km/h", "hours", "ساعات"),
        (90, 16, 14, 0, "time", "Easy", "cyclists", "درّاجان", "km", "km/h", "hours", "ساعات"),
        (550, 52, 58, 0, "time", "Easy", "cargo trains", "قطارا شحن", "km", "km/h", "hours", "ساعات"),
        (84, 13, 15, 0, "time", "Easy", "ferry boats", "قاربان", "km", "km/h", "hours", "ساعات"),
        (600, 72, 78, 0, "time", "Easy", "passenger trains", "قطارا ركاب", "km", "km/h", "hours", "ساعات"),
        (330, 60, 50, 0, "dist_a", "Medium", "trains", "قطاران", "km", "km/h", "hours", "ساعات"),
        (480, 75, 85, 0, "dist_a", "Medium", "coaches", "حافلتان", "km", "km/h", "hours", "ساعات"),
        (105, 18, 17, 0, "dist_a", "Medium", "cyclists", "درّاجان", "km", "km/h", "hours", "ساعات"),
        (500, 65, 55, 3, "apart_t", "Medium", "trains", "قطاران", "km", "km/h", "hours", "ساعات"),
        (420, 48, 42, 4, "apart_t", "Medium", "delivery vans", "شاحنتان", "km", "km/h", "hours", "ساعات"),
        (135, 42, 48, 0, "time_min", "Medium", "shuttle buses", "حافلتا نقل", "km", "km/h", "minutes", "دقيقة"),
        (84, 34, 38, 0, "time_min", "Medium", "patrol boats", "زورقان", "km", "km/h", "minutes", "دقيقة"),
        (410, 50, 70, 1, "head_start", "Hard", "trains", "قطاران", "km", "km/h", "hours", "ساعات"),
        (510, 60, 70, 2, "head_start", "Hard", "intercity buses", "حافلتان", "km", "km/h", "hours", "ساعات"),
        (450, 82, 68, 3, "faster_v", "Hard", "trains", "قطاران", "km", "km/h", "hours", "ساعات"),
        (112, 17, 11, 4, "faster_v", "Hard", "cyclists", "درّاجان", "km", "km/h", "hours", "ساعات"),
    ]
    for D, v1, v2, extra, mode, diff, veh_en, veh_ar, u_d, u_v, u_t_en, u_t_ar in meet_cases:
        qid = next_id()
        vsum = v1 + v2

        if mode == "time":
            ans = D // vsum
            svg = svg_motion_timeline("A", "B", f"{D} {u_d}", f"{v1} {u_v}", f"{v2} {u_v}", meet=True)
            q_en = (
                f"Two {veh_en} start at the same moment from stations A and B, which are {m(D)} {u_d} apart, "
                f"and travel directly toward each other at {m(v1)} {u_v} and {m(v2)} {u_v}. After how many {u_t_en} do they meet?"
            )
            q_ar = (
                f"انطلق {veh_ar} في اللحظة نفسها من المحطتين A وB المسافة بينهما {m(D)} كم، "
                f"متجهين أحدهما نحو الآخر بسرعتي {m(v1)} كم/س و{m(v2)} كم/س. بعد كم ساعة يلتقيان؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    D // abs(v1 - v2) if v1 != v2 and D // abs(v1 - v2) != ans else ans + 3,
                    ans + 1,
                    max(1, ans - 1),
                    ans + 2,
                ],
                qid,
            )
            hint_en = f"Moving toward each other means their gap shrinks by ({v1} + {v2}) = {vsum} {u_d} every hour!"
            hint_ar = f"الحركة في اتجاهين متعاكسين تعني أن المسافة بينهما تتناقص بمقدار ({v1} + {v2}) = {vsum} كم في كل ساعة!"
            sol_en = explain_en(
                "When two travelers move **toward each other**, add their speeds to get the **closing speed**!",
                [
                    f"Combined closing speed: {m(f'{v1} + {v2} = {vsum}')} {u_v}.",
                    f"Time to close {m(D)} {u_d}: {m(f'{D} \\div {vsum} = {ans}')} {u_t_en}.",
                ],
                f"Check: in {m(ans)} {u_t_en}, A covers {m(ans * v1)} {u_d} and B covers {m(ans * v2)} {u_d}; {m(f'{ans * v1} + {ans * v2} = {D}')} {u_d}!",
            )
            sol_ar = explain_ar(
                "عند التحرك **باتجاهين متقابلين**، نجمع السرعتين للحصول على **سرعة الاقتراب المشتركة**!",
                [
                    f"سرعة الاقتراب في الساعة الواحدة: {m(f'{v1} + {v2} = {vsum}')} كم/س.",
                    f"زمن الالتقاء: {m(f'{D} \\div {vsum} = {ans}')} ساعات.",
                ],
                f"تحقق: يقطع الأول {m(ans * v1)} كم والثاني {m(ans * v2)} كم، ومجموعهما {m(D)} كم تمامًا!",
            )

        elif mode == "dist_a":
            t_meet = D // vsum
            ans = v1 * t_meet
            svg = svg_motion_timeline("A", "B", f"{D} km", f"{v1} km/h", f"{v2} km/h", meet=True)
            q_en = (
                f"Two {veh_en} leave points A and B ({m(D)} km apart) simultaneously, traveling toward each other at "
                f"{m(v1)} km/h (from A) and {m(v2)} km/h (from B). How many kilometers **from A** do they meet?"
            )
            q_ar = (
                f"انطلق {veh_ar} في الوقت نفسه من النقطتين A وB (المسافة بينهما {m(D)} كم) متجهين أحدهما نحو الآخر بسرعتي "
                f"{m(v1)} كم/س (من A) و{m(v2)} كم/س (من B). على بُعد كم كيلومترًا **من النقطة A** يلتقيان؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [v2 * t_meet, D // 2, ans + v1, max(10, ans - 20)], qid
            )
            hint_en = "Step 1: Find how many hours until they meet (D ÷ (v1 + v2)). Step 2: Multiply that meeting time by A's speed!"
            hint_ar = "الخطوة 1: احسب زمن الالتقاء بقسمة المسافة على مجموع السرعتين. الخطوة 2: اضرب الزمن في سرعة المنطلق من A!"
            sol_en = explain_en(
                "Find the **shared meeting time** first, then multiply by the speed of the traveler starting at A!",
                [
                    f"Closing speed: {m(f'{v1} + {v2} = {vsum}')} km/h → meeting time: {m(f'{D} \\div {vsum} = {t_meet}')} hours.",
                    f"Distance traveled from A in {m(t_meet)} hours: {m(f'{v1} \\times {t_meet} = {ans}')} km.",
                ],
                f"Check: B travels {m(f'{v2} \\times {t_meet} = {v2 * t_meet}')} km, and {m(f'{ans} + {v2 * t_meet} = {D}')} km!",
            )
            sol_ar = explain_ar(
                "نوجد **زمن الالتقاء** أولًا، ثم نضربه في سرعة المتحرك المنطلق من النقطة A!",
                [
                    f"سرعة الاقتراب {m(f'{v1} + {v2} = {vsum}')} كم/س، فزمن الالتقاء = {m(f'{D} \\div {vsum} = {t_meet}')} ساعات.",
                    f"المسافة المقطوعة من A: {m(f'{v1} \\times {t_meet} = {ans}')} كم.",
                ],
                f"تحقق: يقطع الثاني من B مسافة {m(v2 * t_meet)} كم، ومجموع المسافتين {m(f'{ans} + {v2 * t_meet} = {D}')} كم!",
            )

        elif mode == "apart_t":
            t = extra
            closed = t * vsum
            ans = D - closed
            svg = svg_motion_timeline("A", "B", f"{D} km", f"{v1} km/h", f"{v2} km/h", meet=True)
            q_en = (
                f"Two {veh_en} start {m(D)} km apart at A and B and travel toward each other at {m(v1)} km/h and {m(v2)} km/h. "
                f"How many kilometers apart are they after **{m(t)} hours**?"
            )
            q_ar = (
                f"بدأ {veh_ar} الحركة من النقطتين A وB المسافة بينهما {m(D)} كم باتجاهين متقابلين بسرعتي {m(v1)} كم/س و{m(v2)} كم/س. "
                f"كم كيلومترًا تصبح المسافة الفاصلة بينهما بعد مرور **{m(t)} ساعات**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [closed, D - t * v1, D - t * v2, ans + 30], qid
            )
            hint_en = f"Find the combined distance both cover in {t} hours, then subtract from {D} km!"
            hint_ar = f"احسب مجموع ما يقطعه الاثنان معًا خلال {t} ساعات، ثم اطرحه من المسافة الأصلية {D} كم!"
            sol_en = explain_en(
                f"Every hour shrinks the gap by {m(f'{v1} + {v2} = {vsum}')} km!",
                [
                    f"Total distance closed in {m(t)} hours: {m(f'{t} \\times ({v1} + {v2}) = {t} \\times {vsum} = {closed}')} km.",
                    f"Remaining gap between them: {m(f'{D} - {closed} = {ans}')} km.",
                ],
                f"Notice: since {m(f'{closed} < {D}')}, they have not met yet, leaving {m(ans)} km between them!",
            )
            sol_ar = explain_ar(
                f"في كل ساعة تتناقص الفجوة بينهما بمقدار {m(f'{v1} + {v2} = {vsum}')} كم!",
                [
                    f"المسافة التي قطعاها معًا في {m(t)} ساعات: {m(f'{t} \\times {vsum} = {closed}')} كم.",
                    f"المسافة المتبقية بينهما: {m(f'{D} - {closed} = {ans}')} كم.",
                ],
                f"تحقق: بما أن {m(f'{closed} < {D}')} فلم يلتقيا بعد، والفجوة الفاصلة {m(ans)} كم.",
            )

        elif mode == "time_min":
            assert (D * 60) % vsum == 0
            ans = (D * 60) // vsum
            svg = svg_motion_timeline("A", "B", f"{D} km", f"{v1} km/h", f"{v2} km/h", meet=True)
            q_en = (
                f"Two {veh_en} leave terminals A and B ({m(D)} km apart) at the same instant, heading toward each other "
                f"at {m(v1)} km/h and {m(v2)} km/h. After how many **minutes** do they meet?"
            )
            q_ar = (
                f"انطلق {veh_ar} في اللحظة نفسها من المحطتين A وB (المسافة بينهما {m(D)} كم) متقابلين بسرعتي "
                f"{m(v1)} كم/س و{m(v2)} كم/س. بعد كم **دقيقة** يلتقيان؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 10, ans - 10, (D * 100) // vsum, ans + 15], qid
            )
            hint_en = f"Find the time in hours as a fraction ({D}/{vsum}), then multiply by 60 minutes per hour!"
            hint_ar = f"اكتب الزمن بالساعات على صورة كسر ({D}/{vsum})، ثم اضربه في 60 دقيقة لكل ساعة!"
            sol_en = explain_en(
                "Keep the time as a clean fraction of an hour and multiply by **60** to convert straight into minutes!",
                [
                    f"Closing speed: {m(f'{v1} + {v2} = {vsum}')} km/h.",
                    f"Time in hours: {m(f'\\frac{{{D}}}{{{vsum}}}')} hour(s).",
                    f"Convert to minutes: {m(f'\\frac{{{D}}}{{{vsum}}} \\times 60 = {ans}')} minutes.",
                ],
                f"Check: in {m(ans)} minutes ({m(f'\\frac{{{ans}}}{{60}}')} h), combined distance is {m(f'{vsum} \\times \\frac{{{ans}}}{{60}} = {D}')} km!",
            )
            sol_ar = explain_ar(
                "اكتب الزمن بالساعات في صورة كسر ثم اضربه في **60** لتحصل على الدقائق دون كسور عشرية معقدة!",
                [
                    f"سرعة الاقتراب المشتركة: {m(f'{v1} + {v2} = {vsum}')} كم/س.",
                    f"الزمن بالساعات يساوي {m(f'\\frac{{{D}}}{{{vsum}}}')} ساعة.",
                    f"الزمن بالدقائق: {m(f'\\frac{{{D}}}{{{vsum}}} \\times 60 = {ans}')} دقيقة.",
                ],
                f"تحقق: في {m(ans)} دقيقة يقطعان معًا {m(f'{vsum} \\times \\frac{{{ans}}}{{60}} = {D}')} كم بالضبط!",
            )

        elif mode == "head_start":
            h_early = extra
            solo = h_early * v1
            rem = D - solo
            assert rem % vsum == 0
            ans = rem // vsum
            svg = svg_motion_timeline("A", "B", f"{D} km", f"{v1} km/h", f"{v2} km/h", meet=True)
            h_word = "hour" if h_early == 1 else "hours"
            h_word_ar = "ساعة واحدة" if h_early == 1 else f"{h_early} ساعات" if h_early >= 3 else "ساعتين"
            q_en = (
                f"Stations A and B are {m(D)} km apart. The first of two {veh_en} leaves A toward B at {m(v1)} km/h; "
                f"**{m(h_early)} {h_word} later**, the second leaves B toward A at {m(v2)} km/h. "
                f"How many hours **after the second departs** do they meet?"
            )
            q_ar = (
                f"المسافة بين المحطتين A وB هي {m(D)} كم. انطلق الأول من {veh_ar} من A نحو B بسرعة {m(v1)} كم/س، "
                f"**وبعد {h_word_ar}** انطلق الثاني من B نحو A بسرعة {m(v2)} كم/س. "
                f"بعد كم ساعة **من انطلاق الثاني** يلتقيان؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + h_early, D // vsum if D % vsum == 0 else ans + 2, ans - 1, ans + 3], qid
            )
            hint_en = f"First subtract the {solo} km that the first traveler covers alone during its {h_early}-hour head start!"
            hint_ar = f"اطرح أولًا المسافة ({solo} كم) التي يقطعها الأول بمفرده قبل انطلاق الثاني!"
            sol_en = explain_en(
                "Freeze the clock at the moment the second traveler starts: subtract the head-start distance first!",
                [
                    f"Distance covered by A alone in {m(h_early)} {h_word}: {m(f'{h_early} \\times {v1} = {solo}')} km.",
                    f"Remaining gap when B departs: {m(f'{D} - {solo} = {rem}')} km.",
                    f"Now both move toward each other at {m(f'{v1} + {v2} = {vsum}')} km/h, meeting in {m(f'{rem} \\div {vsum} = {ans}')} hours.",
                ],
                f"Read carefully: {m(ans + h_early)} hours is A's total travel time, whereas B travels for **{m(ans)}** hours!",
            )
            sol_ar = explain_ar(
                "نحسب الموقف لحظة انطلاق الثاني: نطرح مسافة التبكير أولًا ثم نقسم المسافة المتبقية على مجموع السرعتين!",
                [
                    f"ما قطعه الأول بمفرده: {m(f'{h_early} \\times {v1} = {solo}')} كم، فيتبقى {m(f'{D} - {solo} = {rem}')} كم.",
                    f"بعد انطلاق الثاني تصبح سرعة الاقتراب {m(f'{v1} + {v2} = {vsum}')} كم/س.",
                    f"يلتقيان بعد {m(f'{rem} \\div {vsum} = {ans}')} ساعات من انطلاق الثاني.",
                ],
                f"انتبه لقراءة المطلوب: زمن الأول الكلي هو {m(ans + h_early)} ساعات، أما زمن الثاني فهو **{m(ans)}** ساعات!",
            )

        else:  # faster_v
            t = extra
            vdiff = v1 - v2
            ans = v1
            svg = svg_motion_timeline("A", "B", f"{D} km", "v + " + str(vdiff), "v", meet=True)
            q_en = (
                f"Two {veh_en} start simultaneously from A and B ({m(D)} km apart), travel toward each other, and meet in {m(t)} hours. "
                f"If the faster one travels {m(vdiff)} km/h faster than the slower one, what is the speed (in km/h) of the **faster** one?"
            )
            q_ar = (
                f"انطلق {veh_ar} في اللحظة نفسها من A وB (المسافة بينهما {m(D)} كم) باتجاهين متقابلين فالتقيا بعد {m(t)} ساعات. "
                f"إذا كانت سرعة الأسرع تزيد بمقدار {m(vdiff)} كم/س على سرعة الأبطأ، فكم سرعة **الأسرع** (بالكم/س)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [v2, vsum, vsum // 2 + vdiff, ans - 4], qid
            )
            hint_en = f"Divide {D} km by {t} hours to get the SUM of their speeds ({vsum} km/h), then use Sum = {vsum} and Difference = {vdiff}!"
            hint_ar = f"اقسم {D} كم على {t} ساعات لإيجاد **مجموع** السرعتين ({vsum} كم/س)، ثم استخدم المجموع = {vsum} والفرق = {vdiff}!"
            sol_en = explain_en(
                "Divide distance by meeting time to get the **sum of speeds**, then use **(Sum + Difference) ÷ 2** for the larger number!",
                [
                    f"Combined closing speed: {m(f'v_1 + v_2 = {D} \\div {t} = {vsum}')} km/h.",
                    f"Since {m(f'v_1 - v_2 = {vdiff}')}, adding both equations gives {m(f'2v_1 = {vsum} + {vdiff} = {vsum + vdiff}')}.",
                    f"Divide by {m(2)}: faster speed {m(f'v_1 = {ans}')} km/h (and slower speed {m(f'v_2 = {v2}')} km/h).",
                ],
                f"Check: {m(f'({ans} + {v2}) \\times {t} = {vsum} \\times {t} = {D}')} km, and {m(f'{ans} - {v2} = {vdiff}')} km/h!",
            )
            sol_ar = explain_ar(
                "نقسم المسافة على زمن الالتقاء لإيجاد **مجموع السرعتين**، ثم نحسب الأكبر بالقاعدة **(المجموع + الفرق) ÷ 2**!",
                [
                    f"مجموع السرعتين: {m(f'v_1 + v_2 = {D} \\div {t} = {vsum}')} كم/س.",
                    f"وبما أن الفرق {m(vdiff)} كم/س، فإن السرعة الأكبر = {m(f'({vsum} + {vdiff}) \\div 2 = {ans}')} كم/س.",
                ],
                f"تحقق: السريعة {m(ans)} والبطيئة {m(v2)}، مجموعهما {m(vsum)} وفارقهما {m(vdiff)} وفي {m(t)} ساعات يقطعان {m(D)} كم!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-opposite-meet-trains",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 12. g67-heads-legs-two-values (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    hl_cases = [
        # (n_tot, w_low, w_high, cnt_high, ask_which, diff, low_en, high_en, tot_u_en, low_ar, high_ar, tot_u_ar, scene_en, scene_ar)
        (18, 2, 3, 7, "high", "Easy", "bicycles (2 wheels)", "tricycles (3 wheels)", "wheels", "دراجات ثنائية (عجلتان)", "دراجات ثلاثية (3 عجلات)", "عجلة", "park rack", "موقف الحديقة"),
        (24, 2, 3, 9, "low", "Easy", "bicycles (2 wheels)", "tricycles (3 wheels)", "wheels", "دراجات ثنائية (عجلتان)", "دراجات ثلاثية (3 عجلات)", "عجلة", "courtyard shed", "مظلة الساحة"),
        (15, 5, 10, 6, "high", "Easy", "5-riyal notes", "10-riyal notes", "riyals", "أوراق فئة 5 ريالات", "أوراق فئة 10 ريالات", "ريالًا", "Tariq's wallet", "محفظة طارق"),
        (20, 5, 10, 8, "low", "Easy", "5-riyal notes", "10-riyal notes", "riyals", "أوراق فئة 5 ريالات", "أوراق فئة 10 ريالات", "ريالًا", "charity jar", "صندوق التبرعات"),
        (16, 3, 5, 7, "high", "Easy", "3-seat benches", "5-seat benches", "seats", "مقاعد ثلاثية (3 أشخاص)", "مقاعد خماسية (5 أشخاص)", "مقعدًا", "campus garden", "حديقة الجامعة"),
        (22, 2, 4, 8, "high", "Medium", "ostriches (2 legs)", "gazelles (4 legs)", "legs", "نعامات (رجلان)", "غزلان (4 أرجل)", "رجلًا", "wildlife reserve", "محمية طبيعية"),
        (26, 2, 4, 11, "low", "Medium", "ducks (2 legs)", "sheep (4 legs)", "legs", "بطات (رجلان)", "خراف (4 أرجل)", "رجلًا", "countryside farm", "مزرعة ريفية"),
        (20, 3, 5, 9, "high", "Medium", "3-point questions", "5-point questions", "points", "أسئلة من 3 درجات", "أسئلة من 5 درجات", "درجة", "math contest paper", "اختبار مسابقة رياضيات"),
        (25, 3, 5, 12, "low", "Medium", "3-point puzzles", "5-point puzzles", "points", "ألغاز من 3 نقاط", "ألغاز من 5 نقاط", "نقطة", "logic challenge", "تحدي المنطق"),
        (18, 10, 50, 5, "high", "Medium", "10-riyal notes", "50-riyal notes", "riyals", "أوراق فئة 10 ريالات", "أوراق فئة 50 ريالًا", "ريالًا", "cashier drawer", "درج الصندوق"),
        (14, 4, 6, 6, "high", "Medium", "4-person tables", "6-person tables", "diners", "طاولات رباعية (4 كراسي)", "طاولات سداسية (6 كراسي)", "مقعدًا", "dining hall", "قاعة الطعام"),
        (30, 2, 5, 11, "low", "Medium", "2-kg bags", "5-kg bags", "kilograms", "أكياس زنة 2 كجم", "أكياس زنة 5 كجم", "كيلوجرامًا", "date harvest store", "مخزن التمور"),
        (24, 2, 4, 15, "diff_hl", "Hard", "geese (2 legs)", "camels (4 legs)", "legs", "إوزات (رجلان)", "جمال (4 أرجل)", "رجلًا", "oasis paddock", "حظيرة الواحة"),
        (28, 5, 10, 19, "diff_hl", "Hard", "5-riyal vouchers", "10-riyal vouchers", "riyals", "قسائم فئة 5 ريالات", "قسائم فئة 10 ريالات", "ريالًا", "prize envelope", "مظروف الجوائز"),
        (20, -1, 4, 16, "quiz_right", "Hard", "wrong answers (−1 pt)", "correct answers (+4 pts)", "points", "إجابات خاطئة (−1 نقطة)", "إجابات صحيحة (+4 نقاط)", "نقطة", "KMC warm-up round", "جولة تدريبية لمسابقة كاوست"),
        (25, -2, 5, 19, "quiz_right", "Hard", "wrong answers (−2 pts)", "correct answers (+5 pts)", "points", "إجابات خاطئة (−2 نقطة)", "إجابات صحيحة (+5 نقاط)", "نقطة", "science bowl quiz", "مسابقة العلوم"),
    ]
    for n_tot, w_low, w_high, cnt_high, ask_which, diff, low_en, high_en, tot_u_en, low_ar, high_ar, tot_u_ar, scene_en, scene_ar in hl_cases:
        qid = next_id()
        cnt_low = n_tot - cnt_high
        total_val = cnt_low * w_low + cnt_high * w_high
        step_gap = w_high - w_low

        if ask_which in ("high", "low", "diff_hl"):
            base_all_low = n_tot * w_low
            extra_val = total_val - base_all_low
            assert extra_val == cnt_high * step_gap
            if ask_which == "high":
                ans = cnt_high
                ask_en = f"How many **{high_en.split(' (')[0]}** are there?"
                ask_ar = f"كم عدد **{high_ar.split(' (')[0]}**؟"
                other_v = cnt_low
            elif ask_which == "low":
                ans = cnt_low
                ask_en = f"How many **{low_en.split(' (')[0]}** are there?"
                ask_ar = f"كم عدد **{low_ar.split(' (')[0]}**؟"
                other_v = cnt_high
            else:
                ans = abs(cnt_high - cnt_low)
                ask_en = f"How many **more** {high_en.split(' (')[0]} than {low_en.split(' (')[0]} are there?"
                ask_ar = f"بكم يزيد عدد {high_ar.split(' (')[0]} على عدد {low_ar.split(' (')[0]}؟"
                other_v = cnt_high

            q_en = (
                f"In a {scene_en}, there are {m(n_tot)} items in total made up of {low_en} and {high_en}. "
                f"Together they account for **exactly** {m(total_val)} {tot_u_en}. {ask_en}"
            )
            q_ar = (
                f"في {scene_ar}، يوجد إجمالي {m(n_tot)} من {low_ar} و{high_ar}، "
                f"ويبلغ مجموع قيمها معًا {m(total_val)} {tot_u_ar} بالضبط. {ask_ar}"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [other_v, ans + 2, max(1, ans - 2), n_tot // 2 if n_tot // 2 != ans else ans + 3], qid
            )
            hint_en = f"Assume ALL {n_tot} were the smaller type ({n_tot} × {w_low} = {base_all_low}). Each swap to the larger type adds +{step_gap}!"
            hint_ar = f"افرض أولًا أن جميع الـ {n_tot} من النوع الأصغر ({n_tot} × {w_low} = {base_all_low}). كل استبدال بالنوع الأكبر يضيف +{step_gap}!"
            sol_en = explain_en(
                f"Use the KMC **\"Assume All Are One Type\"** trick: start with all {m(n_tot)} at {m(w_low)} each, and see how many swaps of `+{step_gap}` reach {m(total_val)}!",
                [
                    f"If all {m(n_tot)} were `{w_low}`-unit items, the total would be {m(f'{n_tot} \\times {w_low} = {base_all_low}')} {tot_u_en}.",
                    f"We are short by {m(f'{total_val} - {base_all_low} = {extra_val}')} {tot_u_en}, and each swap to a `{w_high}`-unit item adds {m(f'{w_high} - {w_low} = {step_gap}')}.",
                    f"So there are {m(f'{extra_val} \\div {step_gap} = {cnt_high}')} of the larger type and {m(f'{n_tot} - {cnt_high} = {cnt_low}')} of the smaller type → answer = **{m(ans)}**.",
                ],
                f"Check: {m(f'{cnt_low} \\times {w_low} + {cnt_high} \\times {w_high} = {cnt_low * w_low} + {cnt_high * w_high} = {total_val}')}!",
            )
            sol_ar = explain_ar(
                f"نطبّق حيلة **«افرض أن الكل من النوع الأصغر»**: نبدأ بافتراض أن الـ {m(n_tot)} كلها بقيمة {m(w_low)} ثم نحسب عدد الاستبدالات!",
                [
                    f"لو كانت جميعها من فئة {m(w_low)} لكان المجموع {m(f'{n_tot} \\times {w_low} = {base_all_low}')}.",
                    f"الزيادة الفعلية تساوي {m(f'{total_val} - {base_all_low} = {extra_val}')}، وكل استبدال بالفئة الأكبر يضيف {m(f'{w_high} - {w_low} = {step_gap}')}.",
                    f"إذن عدد الفئة الأكبر = {m(f'{extra_val} \\div {step_gap} = {cnt_high}')}، وعدد الفئة الأصغر = {m(f'{n_tot} - {cnt_high} = {cnt_low}')}، والإجابة المطلوبة هي **{m(ans)}**.",
                ],
                f"تحقق: {m(f'{cnt_low} \\times {w_low} + {cnt_high} \\times {w_high} = {total_val}')} بالضبط.",
            )
        else:  # quiz_right with negative penalty w_low < 0
            ans = cnt_high
            max_pts = n_tot * w_high
            lost_pts = max_pts - total_val
            loss_per_wrong = w_high - w_low  # e.g. 4 - (-1) = 5!
            assert lost_pts == cnt_low * loss_per_wrong
            pen = abs(w_low)
            q_en = (
                f"In a {scene_en} of {m(n_tot)} questions, each correct answer earns {m(f'+{w_high}')} points, "
                f"each wrong answer deducts {m(pen)} point(s) ({m(w_low)}), and a student answered **every** question, scoring {m(total_val)} points. "
                f"How many questions did the student answer **correctly**?"
            )
            q_ar = (
                f"في {scene_ar} المكوّنة من {m(n_tot)} سؤالًا، تمنح الإجابة الصحيحة {m(f'+{w_high}')} نقاط، "
                f"وتخصم الإجابة الخاطئة {m(pen)} من النقاط ({m(w_low)})، وقد أجاب طالب عن **جميع** الأسئلة فحصل على {m(total_val)} نقطة. "
                f"كم سؤالًا أجاب عنه **إجابة صحيحة**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    n_tot - lost_pts // w_high if lost_pts % w_high == 0 else ans + 1,
                    cnt_low,
                    ans - 1,
                    ans + 2,
                ],
                qid,
            )
            hint_en = f"Start from a perfect score ({n_tot} × {w_high} = {max_pts})! Watch out: turning 1 right answer into 1 wrong answer loses {w_high} + {pen} = {loss_per_wrong} points!"
            hint_ar = f"ابدأ من الدرجة الكاملة ({n_tot} × {w_high} = {max_pts})! انتبه: كل إجابة خاطئة بديلة عن صحيحة تُفقد الطالب {w_high} + {pen} = {loss_per_wrong} نقاط!"
            sol_en = explain_en(
                f"Penalty trap alert: changing a `+{w_high}` correct answer into a `−{pen}` wrong answer drops your score by **`{w_high} + {pen} = {loss_per_wrong}`** points (not just `{w_high}`)!",
                [
                    f"Perfect score for all {m(n_tot)} right: {m(f'{n_tot} \\times {w_high} = {max_pts}')} points.",
                    f"Points lost below perfect: {m(f'{max_pts} - {total_val} = {lost_pts}')} points.",
                    f"Number of wrong answers: {m(f'{lost_pts} \\div {loss_per_wrong} = {cnt_low}')}, so correct answers = {m(f'{n_tot} - {cnt_low} = {ans}')}!",
                ],
                f"Check: {m(f'{ans} \\times {w_high} - {cnt_low} \\times {pen} = {ans * w_high} - {cnt_low * pen} = {total_val}')} points!",
            )
            sol_ar = explain_ar(
                f"انتبه لفخ الخصم: استبدال إجابة صحيحة (`+{w_high}`) بإجابة خاطئة (`−{pen}`) يُنقص المجموع بمقدار **`{w_high} + {pen} = {loss_per_wrong}`** نقاط!",
                [
                    f"الدرجة الكاملة لو كانت كل الإجابات صحيحة: {m(f'{n_tot} \\times {w_high} = {max_pts}')} نقطة.",
                    f"مجموع النقاط المفقودة: {m(f'{max_pts} - {total_val} = {lost_pts}')} نقطة.",
                    f"عدد الأخطاء = {m(f'{lost_pts} \\div {loss_per_wrong} = {cnt_low}')}، إذن الإجابات الصحيحة = {m(f'{n_tot} - {cnt_low} = {ans}')}!",
                ],
                f"تحقق: {m(f'{ans} \\times {w_high} - {cnt_low} \\times {pen} = {total_val}')} نقطة بالضبط!",
            )

        if ask_which in ("high", "low", "diff_hl"):
            svg_en = svg_pan_balance_coins(
                f"Total items = {n_tot}",
                f"Type 1: {w_low} ea.",
                f"Type 2: {w_high} ea.",
                sub_lbl=f"Total = {total_val} → ?",
            )
            svg_ar = svg_pan_balance_coins(
                f"إجمالي العدد = {n_tot}",
                f"النوع 1: {w_low} للواحد",
                f"النوع 2: {w_high} للواحد",
                sub_lbl=f"المجموع = {total_val} ← ؟",
            )
        else:
            svg_en = svg_pan_balance_coins(
                f"Questions = {n_tot}",
                f"Wrong: −{pen} pt",
                f"Right: +{w_high} pts",
                sub_lbl=f"Score = {total_val} → ?",
            )
            svg_ar = svg_pan_balance_coins(
                f"الأسئلة = {n_tot}",
                f"خطأ: −{pen} نقطة",
                f"صح: +{w_high} نقاط",
                sub_lbl=f"المجموع = {total_val} ← ؟",
            )
        items.append(
            make_kmc_question(
                qid, LEVEL, "Algebra", diff, "g67-heads-legs-two-values",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg_en, diagram_ar=svg_ar,
            )
        )

    assert len(items) == 50
    return items


def _gen_group_1_5(next_id) -> list[dict]:
    """Lesson 1.5 group (50 Qs, Topic: 'Geometry'):
    13. g67-folded-paper-angle (17 Qs)
    14. g67-clock-hands-angle (17 Qs)
    15. g67-glued-cube-stack-area (16 Qs)
    """
    items: list[dict] = []

    # -------------------------------------------------------------------------
    # 13. g67-folded-paper-angle (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    fold_cases = [
        # (val, mode, diff, sheet_en, sheet_ar)
        (52, "str_fwd", "Easy", "rectangular sheet of paper", "ورقة مستطيلة"),
        (57, "str_fwd", "Easy", "origami note card", "بطاقة أوريغامي مستطيلة"),
        (62, "str_fwd", "Easy", "notebook page", "صفحة دفتر مستطيلة"),
        (65, "str_fwd", "Easy", "poster strip", "شريط ورقي مستطيل"),
        (68, "str_fwd", "Easy", "craft cardstock", "بطاقة ورق مقوّى"),
        (71, "str_fwd", "Easy", "envelope flap sheet", "ورقة غلاف مستطيلة"),
        (48, "str_rev", "Medium", "rectangular paper strip", "شريط ورق مستطيل"),
        (58, "str_rev", "Medium", "drawing sheet", "ورقة رسم مستطيلة"),
        (72, "str_rev", "Medium", "greeting card", "بطاقة تهنئة مستطيلة"),
        (36, "str_rev", "Medium", "bookmark strip", "فاصل كتاب ورقي مستطيل"),
        (24, "c90_fwd", "Medium", "square index card", "بطاقة فهرسة مربعة"),
        (29, "c90_fwd", "Medium", "rectangular art sheet", "ورقة فنية مستطيلة"),
        (33, "c90_fwd", "Medium", "gift-wrap corner", "ركن ورقة تغليف مستطيلة"),
        (26, "c90_rev", "Hard", "rectangular folder cover", "غلاف ملف مستطيل"),
        (38, "c90_rev", "Hard", "stiff cardboard sheet", "لوح كرتون مستطيل"),
        (55, "right_edge", "Hard", "rectangular test sheet", "ورقة اختبار مستطيلة"),
        (60, "equal_x_alpha", "Hard", "rectangular origami sheet", "ورقة أوريغامي مستطيلة"),
    ]
    for val, mode, diff, sheet_en, sheet_ar in fold_cases:
        qid = next_id()
        if mode == "str_fwd":
            alpha = val
            ans = 180 - 2 * alpha
            svg = svg_paper_fold(f"{alpha}°", "x°")
            q_en = (
                f"The top-right corner of a {sheet_en} is folded down along the red crease as shown. "
                f"If the crease makes an angle of {m(f'{alpha}^\\circ')} with the dashed original top edge, "
                f"what is the measure of angle {m('x^\\circ')} between the remaining top edge and the folded edge?"
            )
            q_ar = (
                f"طُوِي الركن العلوي الأيمن من {sheet_ar} إلى الأسفل حول خط الطي الأحمر كما في الشكل. "
                f"إذا كان خط الطي يصنع زاوية قياسها {m(f'{alpha}^\\circ')} مع الحافة العلوية الأصلية المتقطعة، "
                f"فما قياس الزاوية {m('x^\\circ')} المحصورة بين الحافة العلوية المتبقية والحافة المطوية؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [180 - alpha, abs(90 - alpha), alpha, ans + 10], qid, suffix="^\\circ"
            )
            hint_en = f"Folding copies the {alpha}° angle onto the other side of the red crease! Then all three angles along the straight top edge sum to 180°."
            hint_ar = f"الطيّ ينسخ الزاوية {alpha}° تمامًا على الجهة الأخرى من خط الطي! ومجموع الزوايا الثلاث على الحافة المستقيمة يساوي 180°."
            sol_en = explain_en(
                "Golden rule of paper folding: **a folded flap reflects across the crease**, so both angles next to the crease equal **α**!",
                [
                    f"Before folding, the angle between the dashed top edge and the crease is {m(f'{alpha}^\\circ')}; after folding, the flap turns by **another** {m(f'{alpha}^\\circ')}, covering {m(f'2 \\times {alpha}^\\circ = {2 * alpha}^\\circ')}.",
                    f"Along the straight top edge ({m('180^\\circ')}), subtract {m(f'{2 * alpha}^\\circ')}: {m(f'x = 180^\\circ - {2 * alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"Check: {m(f'{ans}^\\circ + {alpha}^\\circ + {alpha}^\\circ = 180^\\circ')} (a straight line)!",
            )
            sol_ar = explain_ar(
                "القاعدة الذهبية لطيّ الورق: **الجزء المطوي هو انعكاس للأصلي حول خط الطي**، لذا تتساوى الزاويتان حول خط الطي وتساوي كل منهما **α**!",
                [
                    f"الزاوية الأصلية {m(f'{alpha}^\\circ')} ومثيلتها بعد الطي {m(f'{alpha}^\\circ')} تغطيان معًا {m(f'2 \\times {alpha}^\\circ = {2 * alpha}^\\circ')}.",
                    f"بما أن الحافة العلوية خط مستقيم ({m('180^\\circ')})، فإن {m(f'x = 180^\\circ - {2 * alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"تحقق: {m(f'{ans}^\\circ + {alpha}^\\circ + {alpha}^\\circ = 180^\\circ')} تمامًا!",
            )

        elif mode == "str_rev":
            x_ang = val
            ans = (180 - x_ang) // 2
            svg = svg_paper_fold("α°", f"{x_ang}°")
            q_en = (
                f"When the top-right corner of a {sheet_en} is folded along the red crease as shown, "
                f"the angle between the left part of the top edge and the folded flap edge is {m(f'{x_ang}^\\circ')}. "
                f"What is the crease angle {m('\\alpha^\\circ')}?"
            )
            q_ar = (
                f"عند طيّ الركن العلوي الأيمن من {sheet_ar} حول خط الطي الأحمر كما في الشكل، "
                f"كانت الزاوية بين الجزء الأيسر من الحافة العلوية وحافة الجزء المطوي تساوي {m(f'{x_ang}^\\circ')}. "
                f"ما قياس زاوية الطي {m('\\alpha^\\circ')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [180 - x_ang, 90 - x_ang // 2, ans + 6, ans - 6], qid, suffix="^\\circ"
            )
            hint_en = f"Along the straight top edge (180°), {x_ang}° + α + α = 180°! Subtract {x_ang}° from 180° and divide by 2."
            hint_ar = f"على الحافة العلوية المستقيمة (180°)، لدينا {x_ang}° + α + α = 180°! اطرح {x_ang}° من 180° ثم اقسم على 2."
            sol_en = explain_en(
                "The original corner angle and its folded twin are **equal** (`α` and `α`), sharing whatever is left of `180°`!",
                [
                    f"Along the straight top edge: {m(f'{x_ang}^\\circ + 2\\alpha = 180^\\circ')}.",
                    f"Subtract {m(f'{x_ang}^\\circ')}: {m(f'2\\alpha = {180 - x_ang}^\\circ')}.",
                    f"Divide by {m(2)}: {m(f'\\alpha = {180 - x_ang}^\\circ \\div 2 = {ans}^\\circ')}.",
                ],
                f"Check: {m(f'{x_ang}^\\circ + {ans}^\\circ + {ans}^\\circ = 180^\\circ')}!",
            )
            sol_ar = explain_ar(
                "زاوية الطي الأصلية وتوأمتها المنعكسة **متساويتان** (`α` و`α`) وتتقاسمان ما يتبقى من الزاوية المستقيمة `180°`!",
                [
                    f"على الخط المستقيم العلوي: {m(f'{x_ang}^\\circ + 2\\alpha = 180^\\circ')}.",
                    f"نطرح {m(f'{x_ang}^\\circ')}: {m(f'2\\alpha = {180 - x_ang}^\\circ')}.",
                    f"نقسم على {m(2)}: {m(f'\\alpha = {ans}^\\circ')}.",
                ],
                f"تحقق: {m(f'{x_ang}^\\circ + {ans}^\\circ + {ans}^\\circ = 180^\\circ')}!",
            )

        elif mode == "c90_fwd":
            alpha = val
            ans = 90 - 2 * alpha
            svg = svg_paper_fold(f"{alpha}°", "")
            q_en = (
                f"A {sheet_en} has a {m('90^\\circ')} corner. A straight crease starting right at that {m('90^\\circ')} vertex folds the top edge inward "
                f"at an angle of {m(f'{alpha}^\\circ')} to the crease. What angle of the original {m('90^\\circ')} corner remains **uncovered**?"
            )
            q_ar = (
                f"تحتوي {sheet_ar} على ركن قائم قياسه {m('90^\\circ')}. طُوِيت الحافة العلوية إلى الداخل حول خط طي يمر برأس الزاوية القائمة نفسها "
                f"ويصنع معها زاوية {m(f'{alpha}^\\circ')}. ما قياس الجزء المتبقي **غير المغطى** من الزاوية القائمة {m('90^\\circ')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [90 - alpha, 180 - 2 * alpha, alpha, ans + 8], qid, suffix="^\\circ"
            )
            hint_en = f"Inside the 90° corner, the original strip ({alpha}°) folds onto an equal {alpha}° strip, using up 2 × {alpha}° of the 90°!"
            hint_ar = f"داخل الزاوية القائمة 90°، تستهلك الطية ضعف الزاوية (2 × {alpha}°)؛ اطرح ذلك من 90°!"
            sol_en = explain_en(
                f"Inside a {m('90^\\circ')} corner, folding an angle {m('\\alpha')} across the crease covers **both** {m('\\alpha')} (folded away) and another {m('\\alpha')} (landed on)!",
                [
                    f"Total angle used up inside the {m('90^\\circ')} corner: {m(f'2 \\times {alpha}^\\circ = {2 * alpha}^\\circ')}.",
                    f"Remaining uncovered angle: {m(f'90^\\circ - {2 * alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"Check: {m(f'{alpha}^\\circ + {alpha}^\\circ + {ans}^\\circ = 90^\\circ')}!",
            )
            sol_ar = explain_ar(
                f"عند الطيّ من رأس زاوية قائمة {m('90^\\circ')}، يُستهلك مقدار {m('\\alpha')} قبل خط الطي ومقدار {m('\\alpha')} مطابق بعده!",
                [
                    f"مجموع الزاويتين المتطابقتين حول خط الطي: {m(f'2 \\times {alpha}^\\circ = {2 * alpha}^\\circ')}.",
                    f"الزاوية المتبقية غير المغطاة من الـ {m('90^\\circ')}: {m(f'90^\\circ - {2 * alpha}^\\circ = {ans}^\\circ')}.",
                ],
                f"تحقق: {m(f'{alpha}^\\circ + {alpha}^\\circ + {ans}^\\circ = 90^\\circ')}!",
            )

        elif mode == "c90_rev":
            beta = val
            ans = (90 - beta) // 2
            svg = svg_paper_fold("α°", "")
            q_en = (
                f"One edge of a {m('90^\\circ')} corner of a {sheet_en} is folded inward along a crease passing through that corner vertex, "
                f"leaving an uncovered angle of {m(f'{beta}^\\circ')} inside the {m('90^\\circ')} corner. What is the crease angle {m('\\alpha^\\circ')}?"
            )
            q_ar = (
                f"طُوِيت إحدى حافتي زاوية قائمة ({m('90^\\circ')}) في {sheet_ar} إلى الداخل حول خط طي يمر برأس الزاوية القائمة، "
                f"فبقي جزء غير مغطى قياسه {m(f'{beta}^\\circ')} من الزاوية القائمة. ما قياس زاوية الطي {m('\\alpha^\\circ')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [90 - beta, (180 - beta) // 2, ans + 5, ans - 4], qid, suffix="^\\circ"
            )
            hint_en = f"Since α + α + {beta}° = 90°, subtract {beta}° from 90° and divide by 2!"
            hint_ar = f"بما أن α + α + {beta}° = 90°، اطرح {beta}° من 90° ثم اقسم الناتج على 2!"
            sol_en = explain_en(
                f"The two equal folded angles {m('\\alpha')} plus the uncovered {m(f'{beta}^\\circ')} together build the original {m('90^\\circ')} right angle!",
                [
                    f"Write the corner equation: {m(f'2\\alpha + {beta}^\\circ = 90^\\circ')}.",
                    f"Subtract {m(f'{beta}^\\circ')}: {m(f'2\\alpha = {90 - beta}^\\circ')} → divide by {m(2)}: {m(f'\\alpha = {ans}^\\circ')}.",
                ],
                f"Check: {m(f'{ans}^\\circ + {ans}^\\circ + {beta}^\\circ = 90^\\circ')}!",
            )
            sol_ar = explain_ar(
                f"الزاويتان المتساويتان {m('\\alpha')} حول خط الطي مع الزاوية المتبقية {m(f'{beta}^\\circ')} تكوّنان الزاوية القائمة {m('90^\\circ')}!",
                [
                    f"نكتب المعادلة: {m(f'2\\alpha + {beta}^\\circ = 90^\\circ')}.",
                    f"نطرح {m(f'{beta}^\\circ')} ونقسم على {m(2)}: {m(f'\\alpha = {90 - beta}^\\circ \\div 2 = {ans}^\\circ')}.",
                ],
                f"تحقق: {m(f'{ans}^\\circ + {ans}^\\circ + {beta}^\\circ = 90^\\circ')}!",
            )

        elif mode == "right_edge":
            alpha = val  # 55 -> beta_q = 35 -> along right vertical edge: 180 - 2(35) = 110
            beta_q = 90 - alpha
            ans = 180 - 2 * beta_q
            svg = svg_paper_fold(f"{alpha}°", "")
            q_en = (
                f"In the {sheet_en} shown, the top-right {m('90^\\circ')} corner is folded along the red crease, which makes an angle of "
                f"{m(f'{alpha}^\\circ')} with the dashed top edge. What angle does the folded flap's right edge make with the **lower vertical right edge** of the sheet?"
            )
            q_ar = (
                f"في {sheet_ar} الموضّحة، طُوِي الركن العلوي الأيمن القائم ({m('90^\\circ')}) حول خط الطي الأحمر الذي يصنع زاوية "
                f"{m(f'{alpha}^\\circ')} مع الحافة العلوية المتقطعة. ما قياس الزاوية بين حافة الطية والجزء السفلي المتبقي من **الحافة الرأسية اليمنى** للورقة؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [180 - 2 * alpha, 90 + beta_q, 2 * beta_q, ans - 10], qid, suffix="^\\circ"
            )
            hint_en = f"First use the dashed right triangle (90° corner) to find the crease angle at the right edge (90° − {alpha}° = {beta_q}°), then apply 180° − 2({beta_q}°)!"
            hint_ar = f"استخدم المثلث القائم المتقطع أولًا لإيجاد زاوية خط الطي عند الحافة اليمنى (90° − {alpha}° = {beta_q}°)، ثم طبّق 180° − 2({beta_q}°)!"
            sol_en = explain_en(
                "Step from the top crease end to the right crease end using the `90°` corner triangle, then use `180° − 2β`!",
                [
                    f"In the dashed right-angled corner triangle, the acute angle at the right vertical edge is {m(f'\\beta = 90^\\circ - {alpha}^\\circ = {beta_q}^\\circ')}.",
                    f"Folding reflects {m(f'\\beta = {beta_q}^\\circ')} across the crease, covering {m(f'2 \\times {beta_q}^\\circ = {2 * beta_q}^\\circ')} along the straight vertical edge.",
                    f"Remaining angle along the vertical right edge: {m(f'180^\\circ - {2 * beta_q}^\\circ = {ans}^\\circ')}.",
                ],
                f"Neat identity: {m(f'180^\\circ - 2(90^\\circ - \\alpha) = 2\\alpha = 2 \\times {alpha}^\\circ = {ans}^\\circ')}!",
            )
            sol_ar = explain_ar(
                "ننتقل من أعلى خط الطي إلى أسفله عبر المثلث القائم الركني، ثم نطبّق قاعدة الزاوية المستقيمة `180°`!",
                [
                    f"في مثلث الركن القائم المتقطع، زاوية خط الطي مع الحافة الرأسية اليمنى تساوي {m(f'90^\\circ - {alpha}^\\circ = {beta_q}^\\circ')}.",
                    f"عند الطيّ تتكرر هذه الزاوية مرتين بمجموع {m(f'2 \\times {beta_q}^\\circ = {2 * beta_q}^\\circ')}.",
                    f"الزاوية المتبقية على الحافة الرأسية المستقيمة: {m(f'180^\\circ - {2 * beta_q}^\\circ = {ans}^\\circ')}.",
                ],
                f"ملاحظة جميلة: {m(f'180^\\circ - 2(90^\\circ - \\alpha) = 2\\alpha = {ans}^\\circ')} دائمًا!",
            )

        else:  # equal_x_alpha: x == alpha => 3*alpha = 180 => 60
            ans = 60
            svg = svg_paper_fold("α°", "α°")
            q_en = (
                f"The top-right corner of a {sheet_en} is folded along the red crease as shown. "
                f"Surprisingly, the remaining angle on the left of the straight top edge equals the crease angle {m('\\alpha^\\circ')} itself! "
                f"What is the value of {m('\\alpha^\\circ')}?"
            )
            q_ar = (
                f"طُوِي الركن العلوي الأيمن من {sheet_ar} حول خط الطي الأحمر كما في الشكل، "
                f"فكانت الزاوية المتبقية على يسار الحافة العلوية المستقيمة مساوية لزاوية الطي {m('\\alpha^\\circ')} نفسها! "
                f"ما قياس {m('\\alpha^\\circ')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [45, 30, 72, 90], qid, suffix="^\\circ"
            )
            hint_en = "Count how many equal copies of α meet along the straight 180° top edge: one on the left, plus TWO from the fold!"
            hint_ar = "عدّ كم زاوية متساوية قياس كل منها α تجتمع على الحافة المستقيمة 180°: واحدة يسارًا واثنتان من الطيّ!"
            sol_en = explain_en(
                "Three equal copies of `α` tile the entire `180°` straight top edge!",
                [
                    f"Folding makes the middle flap angle equal to {m('\\alpha')}, matching the original right angle {m('\\alpha')}.",
                    f"Together with the left angle {m('\\alpha')}, all three form a straight line: {m('\\alpha + \\alpha + \\alpha = 3\\alpha = 180^\\circ')}.",
                    f"Divide by {m(3)}: {m('\\alpha = 60^\\circ')}.",
                ],
                f"Trap check: {m('90^\\circ')} forgets the third angle, and {m('45^\\circ')} divides `90°` instead of `180°`!",
            )
            sol_ar = explain_ar(
                "تجتمع **ثلاث نسخ متساوية** من `α` لتشكّل معًا الزاوية المستقيمة `180°` على الحافة العلوية!",
                [
                    f"يعطي الانعكاس حول خط الطي زاويتين قياس كل منهما {m('\\alpha')}، وتنضم إليهما الزاوية اليسرى {m('\\alpha')}.",
                    f"نحصل على: {m('3\\alpha = 180^\\circ')}.",
                    f"بالقسمة على {m(3)} نجد {m('\\alpha = 60^\\circ')}.",
                ],
                f"تحقق: {m('60^\\circ + 60^\\circ + 60^\\circ = 180^\\circ')} على خط مستقيم واحد!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Geometry", diff, "g67-folded-paper-angle",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 14. g67-clock-hands-angle (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    analog_cases = [
        # (h, mins, diff, loc_en, loc_ar)
        (2, 0, "Easy", "classroom", "الفصل الدراسي"),
        (5, 0, "Easy", "kitchen", "المطبخ"),
        (8, 0, "Easy", "school hall", "بهو المدرسة"),
        (4, 30, "Easy", "library", "المكتبة"),
        (2, 30, "Easy", "art studio", "مرسم الفنون"),
        (6, 30, "Easy", "train station", "محطة القطار"),
        (3, 20, "Medium", "science lab", "مختبر العلوم"),
        (4, 20, "Medium", "principal's office", "مكتب الإدارة"),
        (7, 20, "Medium", "museum gallery", "صالة المتحف"),
        (1, 12, "Medium", "study room", "غرفة المذاكرة"),
        (5, 40, "Medium", "gymnasium", "الصالة الرياضية"),
        (9, 10, "Medium", "reception desk", "مكتب الاستقبال"),
        (8, 24, "Medium", "campus tower", "برج الجامعة"),
        (11, 20, "Hard", "observatory", "المرصد الفلكي"),
        (12, 48, "Hard", "city hall", "مبنى البلدية"),
        (10, 16, "Hard", "harbor office", "مكتب الميناء"),
        (3, 36, "Hard", "lecture theater", "مدرج المحاضرات"),
    ]
    for h, mins, diff, loc_en, loc_ar in analog_cases:
        qid = next_id()
        assert mins % 2 == 0
        min_ang = 6 * mins
        hr_base = (h % 12) * 30
        hr_creep = mins // 2
        hr_ang = hr_base + hr_creep
        raw_diff = abs(hr_ang - min_ang)
        ans = min(raw_diff, 360 - raw_diff)

        naive_raw = abs(hr_base - min_ang)
        naive = min(naive_raw, 360 - naive_raw)
        wrong_dir_raw = abs((hr_base - hr_creep) - min_ang)
        wrong_dir = min(wrong_dir_raw, 360 - wrong_dir_raw)

        svg = svg_analog_clock(h, mins, "?")
        t_disp = f"{h}:{mins:02d}"
        q_en = (
            f"The analog wall clock in the {loc_en} shows **{t_disp}** as illustrated. "
            f"What is the **smaller angle** (in degrees) between the hour hand and the minute hand at **{t_disp}**?"
        )
        q_ar = (
            f"تشير ساعة الحائط العقربية في {loc_ar} إلى الساعة **{t_disp}** كما في الشكل. "
            f"ما قياس **الزاوية الصغرى** (بالدرجات) بين عقرب الساعات وعقرب الدقائق عند الساعة **{t_disp}**؟"
        )
        distractors = [
            naive if naive != ans else ans + 15,
            wrong_dir if wrong_dir != ans else ans + 10,
            360 - ans if 360 - ans != ans and 360 - ans < 360 else ans + 30,
            ans + 6,
            max(5, ans - 6),
        ]
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, distractors, qid, suffix="^\\circ"
        )
        hint_en = (
            "Each hour gap is 360° ÷ 12 = 30°, each minute tick is 6°, and don't forget: the hour hand creeps forward 0.5° every minute!"
        )
        hint_ar = (
            "المسافة بين كل رقمين متتاليين 30°، وكل دقيقة 6°، ولا تنسَ أن عقرب الساعات يتحرك نصف درجة (0.5°) في كل دقيقة!"
        )
        sol_en = explain_en(
            "Measure both hands clockwise from **12 o'clock**: the minute hand moves **6° per minute**, while the hour hand moves **30° per hour + 0.5° per minute**!",
            [
                f"**Minute hand** at `{mins:02d}` minutes: {m(f'{mins} \\times 6^\\circ = {min_ang}^\\circ')} from `12`.",
                f"**Hour hand** at `{t_disp}`: {m(f'{h % 12} \\times 30^\\circ + {mins} \\times 0.5^\\circ = {hr_base}^\\circ + {hr_creep}^\\circ = {hr_ang}^\\circ')} from `12`.",
                f"Difference = {m(f'|{hr_ang}^\\circ - {min_ang}^\\circ| = {raw_diff}^\\circ')}; taking the smaller angle (at most {m('180^\\circ')}) gives **{m(f'{ans}^\\circ')}**.",
            ],
            f"Trap check: forgetting the hour hand's {m(f'{hr_creep}^\\circ')} extra movement would give {m(f'{naive}^\\circ')}!" if mins > 0 else f"Check: {m(f'{ans}^\\circ \\le 180^\\circ')} is indeed the smaller of {m(f'{raw_diff}^\\circ')} and {m(f'{360 - raw_diff}^\\circ')}.",
        )
        sol_ar = explain_ar(
            "نقيس زاوية كل عقرب من الرقم **12**: عقرب الدقائق يتحرك **6° لكل دقيقة**، وعقرب الساعات يتحرك **30° لكل ساعة + 0.5° لكل دقيقة**!",
            [
                f"**عقرب الدقائق** عند الدقيقة `{mins:02d}`: {m(f'{mins} \\times 6^\\circ = {min_ang}^\\circ')}.",
                f"**عقرب الساعات** عند `{t_disp}`: {m(f'{h % 12} \\times 30^\\circ + {mins} \\times 0.5^\\circ = {hr_base}^\\circ + {hr_creep}^\\circ = {hr_ang}^\\circ')}.",
                f"الفرق بينهما = {m(f'|{hr_ang}^\\circ - {min_ang}^\\circ| = {raw_diff}^\\circ')}، والزاوية الصغرى (أقل من أو تساوي {m('180^\\circ')}) هي **{m(f'{ans}^\\circ')}**.",
            ],
            f"تنبيه: إغفال حركة عقرب الساعات الإضافية ({m(f'{hr_creep}^\\circ')}) يوقع في الفخ الشائع!" if mins > 0 else f"تحقق: {m(f'{ans}^\\circ')} هي الزاوية الصغرى بين العقربين.",
        )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Geometry", diff, "g67-clock-hands-angle",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 15. g67-glued-cube-stack-area (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    dirs6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def _voxel_sa(cols: tuple[int, ...], include_bottom: bool) -> int:
        cubes = {(i, 0, z) for i, h in enumerate(cols) for z in range(h)}
        cnt = 0
        for x, y, z in cubes:
            for dx, dy, dz in dirs6:
                if (x + dx, y + dy, z + dz) not in cubes:
                    if not include_bottom and dz == -1 and z == 0:
                        continue
                    cnt += 1
        return cnt

    cube_cases = [
        # (cols, mode, diff, tag_en, tag_ar)
        ((2, 1), "incl", "Easy", "wooden", "خشبية"),
        ((3, 1), "incl", "Easy", "plastic", "بلاستيكية"),
        ((3, 2), "incl", "Easy", "acrylic", "أكريليكية"),
        ((3, 2, 1), "incl", "Easy", "ceramic", "خزفية"),
        ((2, 2, 1), "incl", "Easy", "foam", "إسفنجية"),
        ((4, 2, 1), "incl", "Medium", "maple", "قيقب خشبية"),
        ((4, 3, 1), "incl", "Medium", "marble", "رخامية"),
        ((4, 3, 2), "incl", "Medium", "glass", "زجاجية"),
        ((3, 2, 1), "excl", "Medium", "clay", "طينية"),
        ((4, 2, 2), "excl", "Medium", "resin", "راتنجية"),
        ((3, 3, 2), "excl", "Medium", "stone", "حجرية"),
        ((5, 3, 1), "excl", "Medium", "aluminum", "معدنية"),
        ((4, 3, 2, 1), "incl", "Hard", "ivory", "عاجية"),
        ((4, 3, 2, 1), "excl", "Hard", "granite", "جرانيتية"),
        ((3, 2, 1), "edge2_incl", "Hard", "oak", "خشب البلوط"),
        ((4, 3, 2), "hidden_faces", "Hard", "magnetic", "مغناطيسية"),
    ]
    for cols, mode, diff, tag_en, tag_ar in cube_cases:
        qid = next_id()
        assert all(cols[i] >= cols[i + 1] for i in range(len(cols) - 1)) and cols[-1] >= 1
        k_cols = len(cols)
        n_cubes = sum(cols)
        h_max = cols[0]
        sa_all = _voxel_sa(cols, include_bottom=True)
        sa_top_sides = _voxel_sa(cols, include_bottom=False)
        assert sa_all == 2 * k_cols + 2 * h_max + 2 * n_cubes
        assert sa_top_sides == k_cols + 2 * h_max + 2 * n_cubes

        svg = svg_cube_stack_3d(cols)
        cols_str = ", ".join(str(c) for c in cols)

        if mode == "incl":
            ans = sa_all
            q_en = (
                f"A solid sculpture is glued together from {m(n_cubes)} identical {m('1\\text{ cm}')} {tag_en} unit cubes "
                f"arranged in a single row of column heights {m(f'({cols_str})')} as shown. "
                f"What is its **total surface area** in {m('\\text{cm}^2')} (**including** the bottom faces)?"
            )
            q_ar = (
                f"صُنع مجسّم صلب بلصق {m(n_cubes)} مكعبات وحدة {tag_ar} متطابقة طول حرف كل منها {m('1\\text{ سم}')} "
                f"في صف واحد بارتفاعات أعمدة {m(f'({cols_str})')} كما في الشكل. "
                f"ما **المساحة السطحية الكلية** للمجسّم بـ {m('\\text{سم}^2')} (**شاملةً** أوجه القاعدة السفلية)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sa_top_sides, 6 * n_cubes, ans - 2, ans + 2], qid
            )
            hint_en = "Count from all 6 views (Front, Back, Left, Right, Top, Bottom): opposite views have EQUAL areas when there are no hidden pockets!"
            hint_ar = "احسب المساحة من الاتجاهات الستة (أمام، خلف، يسار، يمين، أعلى، أسفل): كل اتجاهين متقابلين لهما نفس المساحة تمامًا!"
            sol_en = explain_en(
                "Use the **6-View Projection Trick**: count squares visible from Top + Bottom, Left + Right, and Front + Back!",
                [
                    f"**Front + Back:** each shows all {m(n_cubes)} cubes → {m(f'2 \\times {n_cubes} = {2 * n_cubes}')} {m('\\text{cm}^2')}.",
                    f"**Top + Bottom:** looking straight down (or up) shows {m(k_cols)} column tops (and {m(k_cols)} bottoms) → {m(f'2 \\times {k_cols} = {2 * k_cols}')} {m('\\text{cm}^2')}.",
                    f"**Left + Right:** tallest column has height {m(h_max)}, and stepping down from {m(h_max)} exposes {m(h_max)} on the right too → {m(f'2 \\times {h_max} = {2 * h_max}')} {m('\\text{cm}^2')}. Total = {m(f'{2 * n_cubes} + {2 * k_cols} + {2 * h_max} = {ans}')} {m('\\text{cm}^2')}.",
                ],
                f"Notice: {m(sa_top_sides)} forgets the {m(k_cols)} bottom faces, and {m(6 * n_cubes)} forgets glued inner faces!",
            )
            sol_ar = explain_ar(
                "استخدم **حيلة المساقط الستة**: احسب الأوجه الظاهرة من (أمام + خلف) و(أعلى + أسفل) و(يسار + يمين)!",
                [
                    f"**الأمام + الخلف:** يظهر في كلٍّ منهما {m(n_cubes)} مربعات → {m(f'2 \\times {n_cubes} = {2 * n_cubes}')} {m('\\text{سم}^2')}.",
                    f"**الأعلى + الأسفل:** يظهر {m(k_cols)} من الأعلى و{m(k_cols)} من الأسفل → {m(f'2 \\times {k_cols} = {2 * k_cols}')} {m('\\text{سم}^2')}.",
                    f"**اليسار + اليمين:** أقصى ارتفاع {m(h_max)} من اليسار ومثله {m(h_max)} من اليمين → {m(f'2 \\times {h_max} = {2 * h_max}')} {m('\\text{سم}^2')}. المجموع = **{m(ans)}** {m('\\text{سم}^2')}.",
                ],
                f"تحقق: جمع الاتجاهات الستة أسرع وأدق بكثير من عدّ المكعبات واحدًا تلو الآخر!",
            )

        elif mode == "excl":
            ans = sa_top_sides
            q_en = (
                f"A tower of {m(n_cubes)} glued {m('1\\text{ cm}')} {tag_en} cubes stands flat on a table in a single row of heights {m(f'({cols_str})')} as shown. "
                f"If all exposed outer faces are painted **without lifting the tower** (so the bottom faces touching the table are **not** painted), "
                f"what area in {m('\\text{cm}^2')} gets painted?"
            )
            q_ar = (
                f"يرتكز مجسّم مكوّن من {m(n_cubes)} مكعبات وحدة {tag_ar} ملصوقة (حرف كل منها {m('1\\text{ سم}')}) بارتفاعات {m(f'({cols_str})')} على طاولة مسطحة كما في الشكل. "
                f"إذا طُلِيت جميع الأوجه الخارجية المكشوفة **دون رفع المجسّم عن الطاولة** (أي لا تُطلى الأوجه الملامسة للطاولة)، "
                f"فكم المساحة المطلية بـ {m('\\text{سم}^2')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sa_all, ans - k_cols, ans + 2, 6 * n_cubes - k_cols], qid
            )
            hint_en = f"Count Front + Back (2 × {n_cubes}), Left + Right (2 × {h_max}), and ONLY the Top ({k_cols}) — skip the {k_cols} floor faces!"
            hint_ar = f"احسب الأمام + الخلف (2 × {n_cubes})، واليسار + اليمين (2 × {h_max})، والأعلى فقط ({k_cols}) — واستبعد أوجه القاعدة الـ {k_cols}!"
            sol_en = explain_en(
                "Count the 5 painted directions (Front, Back, Left, Right, and Top), leaving out the Bottom faces on the table!",
                [
                    f"**Front + Back:** {m(f'2 \\times {n_cubes} = {2 * n_cubes}')} {m('\\text{cm}^2')}.",
                    f"**Left + Right:** {m(f'2 \\times {h_max} = {2 * h_max}')} {m('\\text{cm}^2')}.",
                    f"**Top only** (looking straight down): {m(k_cols)} {m('\\text{cm}^2')}. Painted area = {m(f'{2 * n_cubes} + {2 * h_max} + {k_cols} = {ans}')} {m('\\text{cm}^2')}.",
                ],
                f"Check: total surface area with bottom is {m(sa_all)}, minus {m(k_cols)} floor squares = {m(ans)} {m('\\text{cm}^2')}!",
            )
            sol_ar = explain_ar(
                "نحسب الاتجاهات الخمسة المكشوفة للطلاء (الأمام، الخلف، اليسار، اليمين، والأعلى فقط) ونستبعد القاعدة الملامسة للطاولة!",
                [
                    f"**الأمام + الخلف:** {m(f'2 \\times {n_cubes} = {2 * n_cubes}')} {m('\\text{سم}^2')}.",
                    f"**اليسار + اليمين:** {m(f'2 \\times {h_max} = {2 * h_max}')} {m('\\text{سم}^2')}.",
                    f"**الأعلى فقط:** {m(k_cols)} {m('\\text{سم}^2')}. المساحة المطلية = {m(f'{2 * n_cubes} + {2 * h_max} + {k_cols} = {ans}')} {m('\\text{سم}^2')}.",
                ],
                f"تحقق: المساحة الكلية بالقاعدة {m(sa_all)} نطرح منها {m(k_cols)} أوجه سفلية فنحصل على {m(ans)} {m('\\text{سم}^2')}!",
            )

        elif mode == "edge2_incl":
            ans = sa_all * 4
            q_en = (
                f"The stepped block shown is glued from {m(n_cubes)} identical {tag_en} cubes in column heights {m(f'({cols_str})')}, "
                f"where **each cube has edge length {m('2\\text{ cm}')}**. What is the **total surface area** (including the bottom) in {m('\\text{cm}^2')}?"
            )
            q_ar = (
                f"صُنع المجسّم المدرّج الموضّح بلصق {m(n_cubes)} مكعبات متطابقة من {tag_ar} بارتفاعات أعمدة {m(f'({cols_str})')}، "
                f"حيث **طول حرف كل مكعب {m('2\\text{ سم}')}**. ما **المساحة السطحية الكلية** للمجسّم (شاملة القاعدة) بـ {m('\\text{سم}^2')}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sa_all * 2, sa_all, sa_top_sides * 4, ans + 8], qid
            )
            hint_en = f"First count how many square cube-faces are exposed ({sa_all}), then multiply by the area of ONE square face (2 cm × 2 cm = 4 cm², NOT 2 cm²)!"
            hint_ar = f"عدّ أولًا عدد الأوجه المربعة المكشوفة ({sa_all})، ثم اضرب في مساحة الوجه المربع الواحد (2 × 2 = 4 سم² وليس 2 سم²)!"
            sol_en = explain_en(
                "Count exposed square faces first, then multiply by **`2 × 2 = 4 cm²`** per square face!",
                [
                    f"Number of exposed cube faces (including bottom): {m(f'2({n_cubes}) + 2({k_cols}) + 2({h_max}) = {sa_all}')} faces.",
                    f"Each cube face is a {m('2\\text{ cm} \\times 2\\text{ cm}')} square of area {m('4\\text{ cm}^2')}.",
                    f"Total surface area: {m(f'{sa_all} \\times 4 = {ans}\\text{{ cm}}^2')}.",
                ],
                f"Trap check: multiplying by {m(2)} ({m(sa_all * 2)}) scales length instead of **area** ({m('2^2 = 4')})!",
            )
            sol_ar = explain_ar(
                "نعدّ الأوجه المربعة المكشوفة أولًا، ثم نضرب في مساحة الوجه الواحد وهي **`2 × 2 = 4 سم²`**!",
                [
                    f"عدد الأوجه المربعة المكشوفة (شاملة الأسفل): {m(f'2({n_cubes}) + 2({k_cols}) + 2({h_max}) = {sa_all}')} وجهًا.",
                    f"مساحة الوجه المربع الواحد = {m('2 \\times 2 = 4\\text{ سم}^2')}.",
                    f"المساحة السطحية الكلية: {m(f'{sa_all} \\times 4 = {ans}\\text{{ سم}}^2')}.",
                ],
                f"انتبه: الضرب في {m(2)} بدلًا من {m(4)} خطأ شائع لأن المساحة تتضاعف بمربع طول الضلع ({m('2^2 = 4')})!",
            )

        else:  # hidden_faces
            tot_faces_before = 6 * n_cubes
            ans = tot_faces_before - sa_all
            q_en = (
                f"Nine {m('1\\text{ cm}')} {tag_en} cubes (originally having {m(f'{n_cubes} \\times 6 = {tot_faces_before}')} unit square faces in total) "
                f"are glued face-to-face into the stepped tower of heights {m(f'({cols_str})')} shown. "
                f"How many **unit square faces** are now **hidden inside** the glued joints?"
            )
            q_ar = (
                f"لدينا {m(n_cubes)} مكعبات {tag_ar} طول حرف كل منها {m('1\\text{ سم}')} (لها أصلًا {m(f'{n_cubes} \\times 6 = {tot_faces_before}')} وجهًا مربعًا في المجموع)، "
                f"لُصِقت وجهًا لوجه لتكوين المجسّم المدرّج ذي الارتفاعات {m(f'({cols_str})')} الموضّح. "
                f"كم **وجهًا مربعًا** أصبح **مخفيًا بالداخل** عند مواضع الالتصاق؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans // 2, sa_all, ans + 2, ans - 2], qid
            )
            hint_en = f"Every glued contact hides TWO unit faces (one on each touching cube)! Or simply compute {tot_faces_before} − (outer surface area {sa_all})."
            hint_ar = f"كل موضع تلاصق يخفي **وجهين** (وجهًا من كل مكعب)! أو اطرح المساحة السطحية الخارجية ({sa_all}) من مجموع الأوجه الأصلي ({tot_faces_before})."
            sol_en = explain_en(
                "Hidden faces = **(Total faces before gluing) − (Outer surface area after gluing)** (and notice it is always even because each glue joint hides 2 faces!)!",
                [
                    f"Before gluing, {m(n_cubes)} cubes have {m(f'{n_cubes} \\times 6 = {tot_faces_before}')} unit faces.",
                    f"Outer surface area (all 6 directions): {m(f'2({n_cubes}) + 2({k_cols}) + 2({h_max}) = {sa_all}')} exposed faces.",
                    f"Hidden glued faces: {m(f'{tot_faces_before} - {sa_all} = {ans}')} faces.",
                ],
                f"Joint-count check: vertical glue joints = {m('3 + 2 + 1 = 6')}; horizontal glue joints = {m('3 + 2 = 5')}; {m('(6 + 5) \\times 2 = 22')} hidden faces!",
            )
            sol_ar = explain_ar(
                "الأوجه المخفية = **(مجموع الأوجه قبل اللصق) − (المساحة السطحية الخارجية بعد اللصق)** (وهي دائمًا عدد زوجي لأن كل تلاصق يخفي وجهين)!",
                [
                    f"قبل اللصق، مجموع الأوجه يساوي {m(f'{n_cubes} \\times 6 = {tot_faces_before}')} وجهًا.",
                    f"الأوجه الخارجية المكشوفة من الاتجاهات الستة: {m(f'2({n_cubes}) + 2({k_cols}) + 2({h_max}) = {sa_all}')} وجهًا.",
                    f"عدد الأوجه المخفية بالداخل: {m(f'{tot_faces_before} - {sa_all} = {ans}')} وجهًا.",
                ],
                f"تحقق بعدّ المفاصل: {m(11)} موضع تلاصق × {m(2)} وجه لكل موضع = {m(22)} وجهًا مخفيًا!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Geometry", diff, "g67-glued-cube-stack-area",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    assert len(items) == 50
    return items


def _gen_group_1_6(next_id) -> list[dict]:
    """Lesson 1.6 group (50 Qs):
    16. g67-magic-square-3x3 (17 Qs, Topic: 'Combinatorics & Logic')
    17. g67-shortest-street-grid (17 Qs, Topic: 'Combinatorics & Logic')
    18. g67-pie-chart-sectors (16 Qs, Topic: 'Data & Probability')
    """
    items: list[dict] = []

    # -------------------------------------------------------------------------
    # 16. g67-magic-square-3x3 (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    lo_shu_bases = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    ]

    def _make_magic(center: int, step: int, orient: int) -> list[list[int]]:
        base = lo_shu_bases[orient % 4]
        sq = [[center + step * (base[r][c] - 5) for c in range(3)] for r in range(3)]
        s = 3 * center
        for r in range(3):
            assert sum(sq[r]) == s
        for c in range(3):
            assert sum(sq[r][c] for r in range(3)) == s
        assert sq[0][0] + sq[1][1] + sq[2][2] == s
        assert sq[0][2] + sq[1][1] + sq[2][0] == s
        assert len({sq[r][c] for r in range(3) for c in range(3)}) == 9
        return sq

    magic_cases = [
        # (center, step, orient, mode, diff)
        (7, 1, 0, "sum_from_c", "Easy"),
        (9, 2, 1, "sum_from_c", "Easy"),
        (12, 2, 2, "sum_from_c", "Easy"),
        (6, 1, 3, "c_from_row", "Easy"),
        (10, 2, 0, "c_from_row", "Easy"),
        (15, 3, 1, "c_from_row", "Easy"),
        (8, 1, 0, "opp_cell", "Medium"),
        (11, 2, 1, "opp_cell", "Medium"),
        (14, 3, 2, "opp_cell", "Medium"),
        (16, 2, 3, "opp_cell", "Medium"),
        (9, 1, 0, "shared_rc", "Medium"),
        (13, 2, 1, "shared_rc", "Medium"),
        (17, 3, 2, "shared_rc", "Medium"),
        (10, 1, 0, "sparse_chain", "Hard"),
        (13, 2, 1, "sparse_chain", "Hard"),
        (15, 2, 2, "sparse_chain", "Hard"),
        (18, 3, 3, "sparse_chain", "Hard"),
    ]
    for center, step, orient, mode, diff in magic_cases:
        qid = next_id()
        sq = _make_magic(center, step, orient)
        S = 3 * center

        if mode == "sum_from_c":
            ans = S
            cells = [
                [str(sq[0][0]), "", ""],
                ["", str(center), str(sq[1][2])],
                ["", "", ""],
            ]
            svg = svg_magic_square_3x3(cells)
            q_en = (
                f"In the {m(3)}-by-{m(3)} magic square shown (where every row, every column, and both main diagonals have the same sum), "
                f"the center cell is {m(center)}, the top-left cell is {m(sq[0][0])}, and the middle-right cell is {m(sq[1][2])}. "
                f"What is the **magic sum** of each row, column, and diagonal?"
            )
            q_ar = (
                f"في المربع السحري ذي الأبعاد {m(3)} في {m(3)} الموضّح (حيث تتساوى مجاميع كل صف وكل عمود والقطرين الرئيسين)، "
                f"الخلية الوسطى هي {m(center)}، والركن العلوي الأيسر {m(sq[0][0])}، ويمين الوسط {m(sq[1][2])}. "
                f"ما **المجموع السحري** لكل صف أو عمود أو قطر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [2 * center + sq[0][0], 4 * center, ans + 3, ans - 3], qid
            )
            hint_en = "Golden 3×3 Magic Square theorem: the magic sum S is ALWAYS equal to 3 × (the center number)!"
            hint_ar = "القاعدة الذهبية للمربع السحري 3×3: المجموع السحري يساوي دائمًا 3 × (العدد الموجود في المركز)!"
            sol_en = explain_en(
                "In **any** 3×3 magic square, the magic sum equals **3 × Center**!",
                [
                    f"Why? Adding the middle row, middle column, and both diagonals gives {m('4S')}, which equals all 9 cells ({m('3S')}) plus {m(3)} extra copies of the center—so {m('S = 3 \\times \\text{center}')}!",
                    f"Multiply the center {m(center)} by {m(3)}: {m(f'S = 3 \\times {center} = {ans}')}.",
                ],
                f"Check: bottom-right must be {m(f'{ans} - {sq[0][0]} - {center} = {sq[2][2]}')}, and the whole square completes with row sum {m(ans)}!",
            )
            sol_ar = explain_ar(
                "في **أي** مربع سحري بأبعاد 3×3، يساوي المجموع السحري دائمًا **3 × عدد المركز**!",
                [
                    f"عند جمع الصف الأوسط والعمود الأوسط والقطرين نحصل على {m('4S = 3S + 3 \\times \\text{المركز}')}، ومنها {m('S = 3 \\times \\text{المركز}')}.",
                    f"نضرب عدد المركز {m(center)} في {m(3)}: {m(f'S = 3 \\times {center} = {ans}')}.",
                ],
                f"تحقق: يمكن إكمال جميع الخلايا التسع بحيث يكون مجموع كل خط {m(ans)} بالضبط!",
            )

        elif mode == "c_from_row":
            ans = center
            r0 = sq[0]
            cells = [
                [str(r0[0]), str(r0[1]), str(r0[2])],
                ["", "?", ""],
                ["", "", ""],
            ]
            svg = svg_magic_square_3x3(cells)
            q_en = (
                f"In the {m(3)}-by-{m(3)} magic square shown, every row, column, and main diagonal has the same sum, "
                f"and the top row contains {m(r0[0])}, {m(r0[1])}, and {m(r0[2])}. What number belongs in the **center** cell `{m('?')}`?"
            )
            q_ar = (
                f"في المربع السحري ذي الأبعاد {m(3)} في {m(3)} الموضّح، يتساوى مجموع كل صف وعمود وقطر رئيس، "
                f"ويحتوي الصف العلوي على الأعداد {m(r0[0])} و{m(r0[1])} و{m(r0[2])}. ما العدد الذي يوضع في خلية **المركز** `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [S, ans + step, ans - step, (r0[0] + r0[2]) // 2 if (r0[0] + r0[2]) // 2 != ans else ans + 2], qid
            )
            hint_en = "Add the three numbers in the top row to get the magic sum S, then divide S by 3 to get the center!"
            hint_ar = "اجمع أعداد الصف العلوي الثلاثة لإيجاد المجموع السحري S، ثم اقسم S على 3 لإيجاد عدد المركز!"
            sol_en = explain_en(
                "Add the complete top row to get the magic sum `S`, then divide by `3` because **`Center = S ÷ 3`**!",
                [
                    f"Top-row magic sum: {m(f'S = {r0[0]} + {r0[1]} + {r0[2]} = {S}')}.",
                    f"Center cell: {m(f'{S} \\div 3 = {ans}')}.",
                ],
                f"Check: {m(f'3 \\times {ans} = {S}')}, matching the top row sum!",
            )
            sol_ar = explain_ar(
                "نجمع الصف العلوي المكتمل لمعرفة المجموع السحري `S`، ثم نقسم على `3` لأن **`المركز = S ÷ 3`**!",
                [
                    f"مجموع الصف العلوي: {m(f'S = {r0[0]} + {r0[1]} + {r0[2]} = {S}')}.",
                    f"عدد خلية المركز: {m(f'{S} \\div 3 = {ans}')}.",
                ],
                f"تحقق: {m(f'3 \\times {ans} = {S}')} وهو مطابق لمجموع الصف العلوي!",
            )

        elif mode == "opp_cell":
            ans = sq[2][2]
            cells = [
                [str(sq[0][0]), "", str(sq[0][2])],
                ["", str(center), ""],
                ["", "", "?"],
            ]
            svg = svg_magic_square_3x3(cells)
            q_en = (
                f"In the {m(3)}-by-{m(3)} magic square shown, the top-left corner is {m(sq[0][0])}, the top-right corner is {m(sq[0][2])}, "
                f"and the center cell is {m(center)}. What number goes in the **bottom-right** corner `{m('?')}`?"
            )
            q_ar = (
                f"في المربع السحري ذي الأبعاد {m(3)} في {m(3)} الموضّح، الركن العلوي الأيسر {m(sq[0][0])}، والركن العلوي الأيمن {m(sq[0][2])}، "
                f"وخلية المركز {m(center)}. ما العدد الذي يوضع في **الركن السفلي الأيمن** `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sq[2][0], sq[0][1], ans + step, max(1, ans - step)], qid
            )
            hint_en = f"Since the center is {center}, any two cells opposite each other across the center must add up to 2 × {center} = {2 * center}!"
            hint_ar = f"بما أن المركز {center}، فإن أي خليتين متقابلتين عبر المركز مجموعهما دائمًا 2 × {center} = {2 * center}!"
            sol_en = explain_en(
                f"With center {m(center)}, the magic sum is {m(f'3 \\times {center} = {S}')}, so any pair opposite across the center sums to **{m(f'2 \\times {center} = {2 * center}')}**!",
                [
                    f"Along the main diagonal: {m(f'{sq[0][0]} + {center} + ? = 3 \\times {center} = {S}')}.",
                    f"Subtract {m(f'{sq[0][0]} + {center} = {sq[0][0] + center}')}: {m(f'? = {S} - {sq[0][0] + center} = {ans}')}.",
                ],
                f"Check: {m(f'{sq[0][0]} + {center} + {ans} = {S}')}!",
            )
            sol_ar = explain_ar(
                f"بما أن المركز {m(center)} فإن المجموع السحري {m(f'3 \\times {center} = {S}')}، ومجموع أي ركنين متقابلين قطريًا يساوي **{m(f'2 \\times {center} = {2 * center}')}**!",
                [
                    f"على القطر الرئيس: {m(f'{sq[0][0]} + {center} + ? = {S}')}.",
                    f"إذن قيمة الركن المطلوب: {m(f'? = {S} - ({sq[0][0]} + {center}) = {ans}')}.",
                ],
                f"تحقق: {m(f'{sq[0][0]} + {center} + {ans} = {S}')} تمامًا!",
            )

        elif mode == "shared_rc":
            # Show r0c0, r0c1 (leaving r0c2 blank!) and r1c2, and ask r2c2 = ?
            ans = sq[2][2]
            cells = [
                [str(sq[0][0]), str(sq[0][1]), ""],
                ["", "", str(sq[1][2])],
                ["", "", "?"],
            ]
            svg = svg_magic_square_3x3(cells)
            q_en = (
                f"In the {m(3)}-by-{m(3)} magic square shown, every row, column, and main diagonal has the same sum. "
                f"Given {m(sq[0][0])} and {m(sq[0][1])} in the top row and {m(sq[1][2])} in the right column, what number belongs in `{m('?')}`?"
            )
            q_ar = (
                f"في المربع السحري ذي الأبعاد {m(3)} في {m(3)} الموضّح، يتساوى مجموع كل صف وعمود وقطر رئيس. "
                f"إذا علمت العددين {m(sq[0][0])} و{m(sq[0][1])} في الصف العلوي والعدد {m(sq[1][2])} في العمود الأيمن، فما قيمة `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sq[0][2], center, ans + step, max(1, ans - step)], qid
            )
            hint_en = "Compare the Top Row and the Right Column: they SHARE the blank top-right corner! So the other two cells in each must have the SAME sum!"
            hint_ar = "قارن الصف العلوي بالعمود الأيمن: هما يشتركان في الركن العلوي الأيمن الفارغ! إذن مجموع الخليتين الباقيتين في كل منهما متساوٍ!"
            sol_en = explain_en(
                "**Shared-Corner Trick**: you don't even need the magic sum! The top row and right column share the top-right cell, so their remaining pairs have **equal sums**!",
                [
                    f"Let the blank top-right corner be {m('k')}. Since Top Row = Right Column: {m(f'{sq[0][0]} + {sq[0][1]} + k = k + {sq[1][2]} + ?')}.",
                    f"Cancel {m('k')} from both sides: {m(f'{sq[0][0]} + {sq[0][1]} = {sq[1][2]} + ?')}.",
                    f"So {m(f'? = {sq[0][0] + sq[0][1]} - {sq[1][2]} = {ans}')}!",
                ],
                f"Check with full magic sum {m(S)}: top-right {m(f'k = {sq[0][2]}')}, and {m(f'{sq[0][2]} + {sq[1][2]} + {ans} = {S}')}!",
            )
            sol_ar = explain_ar(
                "**حيلة الركن المشترك**: يشترك الصف العلوي والعمود الأيمن في الخلية العلوية اليمنى، لذا يتساوى مجموع الخليتين الأخريين في كلٍّ منهما دون حاجة لمعرفة المجموع السحري!",
                [
                    f"نسمّي الركن العلوي الأيمن المشترك {m('k')}، فيكون: {m(f'{sq[0][0]} + {sq[0][1]} + k = k + {sq[1][2]} + ?')}.",
                    f"نحذف {m('k')} من الطرفين: {m(f'{sq[0][0] + sq[0][1]} = {sq[1][2]} + ?')}.",
                    f"إذن {m(f'? = {sq[0][0] + sq[0][1]} - {sq[1][2]} = {ans}')}!",
                ],
                f"تحقق: المجموع السحري {m(S)}، والركن العلوي الأيمن {m(sq[0][2])}، ومجموع العمود الأيمن {m(f'{sq[0][2]} + {sq[1][2]} + {ans} = {S}')}!",
            )

        else:  # sparse_chain: given ONLY r0c0, center, r1c2 -> ask r2c0 = ?
            ans = sq[2][0]
            cells = [
                [str(sq[0][0]), "", ""],
                ["", str(center), str(sq[1][2])],
                ["?", "", ""],
            ]
            svg = svg_magic_square_3x3(cells)
            q_en = (
                f"Only three numbers are shown in this {m(3)}-by-{m(3)} magic square: top-left {m(sq[0][0])}, center {m(center)}, "
                f"and middle-right {m(sq[1][2])}. If every row, column, and main diagonal has the same sum, what number goes in `{m('?')}`?"
            )
            q_ar = (
                f"تظهر ثلاثة أعداد فقط في هذا المربع السحري ({m(3)} في {m(3)}): الركن العلوي الأيسر {m(sq[0][0])}، والمركز {m(center)}، "
                f"ويمين الوسط {m(sq[1][2])}. إذا تساوى مجموع كل صف وعمود وقطر رئيس، فما العدد الذي يوضع في `{m('?')}`؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [sq[2][2], sq[0][2], ans + step, max(1, ans - step)], qid
            )
            hint_en = f"1) Magic sum S = 3 × {center} = {S}. 2) Main diagonal gives bottom-right. 3) Right column gives top-right. 4) Anti-diagonal gives `?`!"
            hint_ar = f"1) المجموع السحري = 3 × {center} = {S}. 2) القطر الرئيس يعطي الركن السفلي الأيمن. 3) العمود الأيمن يعطي العلوي الأيمن. 4) القطر الآخر يعطي `؟`!"
            sol_en = explain_en(
                "Unlock the magic sum from the center first, then hop **Main Diagonal → Right Column → Anti-Diagonal**!",
                [
                    f"**Magic sum:** {m(f'S = 3 \\times {center} = {S}')}.",
                    f"**Bottom-right corner** (from main diagonal): {m(f'{S} - {sq[0][0]} - {center} = {sq[2][2]}')}.",
                    f"**Top-right corner** (from right column): {m(f'{S} - {sq[1][2]} - {sq[2][2]} = {sq[0][2]}')}.",
                    f"**Bottom-left `?`** (from anti-diagonal): {m(f'{S} - {sq[0][2]} - {center} = {ans}')}!",
                ],
                f"Check: anti-diagonal {m(f'{sq[0][2]} + {center} + {ans} = {S}')}!",
            )
            sol_ar = explain_ar(
                "نوجد المجموع السحري من المركز أولًا، ثم ننتقل بخطوات متسلسلة: **القطر الرئيس ← العمود الأيمن ← القطر العكسي**!",
                [
                    f"**المجموع السحري:** {m(f'S = 3 \\times {center} = {S}')}.",
                    f"**الركن السفلي الأيمن** (من القطر الرئيس): {m(f'{S} - {sq[0][0]} - {center} = {sq[2][2]}')}.",
                    f"**الركن العلوي الأيمن** (من العمود الأيمن): {m(f'{S} - {sq[1][2]} - {sq[2][2]} = {sq[0][2]}')}.",
                    f"**الركن السفلي الأيسر `؟`** (من القطر العكسي): {m(f'{S} - {sq[0][2]} - {center} = {ans}')}!",
                ],
                f"تحقق: مجموع القطر العكسي {m(f'{sq[0][2]} + {center} + {ans} = {S}')} تمامًا!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Combinatorics & Logic", diff, "g67-magic-square-3x3",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 17. g67-shortest-street-grid (17 Qs: 6 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    def _dp_paths(cols: int, rows: int, blocked: tuple = None) -> int:
        dp = {}
        for c in range(cols + 1):
            for r in range(rows + 1):
                if blocked is not None and (c, r) == blocked:
                    dp[(c, r)] = 0
                elif c == 0 and r == 0:
                    dp[(c, r)] = 1
                else:
                    dp[(c, r)] = dp.get((c - 1, r), 0) + dp.get((c, r - 1), 0)
        return dp[(cols, rows)]

    path_cases = [
        # (cols, rows, pt, mode, diff, who_en, who_ar)
        (2, 2, None, "plain", "Easy", "Noura walks", "تمشي نورة"),
        (3, 1, None, "plain", "Easy", "A delivery robot rolls", "يتحرك روبوت توصيل"),
        (3, 2, None, "plain", "Easy", "Sami cycles", "يقود سامي دراجته"),
        (2, 3, None, "plain", "Easy", "An ant crawls", "تزحف نملة"),
        (4, 1, None, "plain", "Easy", "Maha jogs", "تجري مها"),
        (4, 2, None, "plain", "Easy", "Faisal walks", "يسير فيصل"),
        (3, 3, None, "plain", "Medium", "A campus shuttle drives", "تسير حافلة الجامعة"),
        (5, 2, None, "plain", "Medium", "Huda skates", "تتزلج هدى"),
        (4, 3, None, "plain", "Medium", "Yasser bikes", "يركب ياسر دراجته"),
        (6, 2, None, "plain", "Medium", "A patrol rover moves", "تتحرك عربة استطلاع"),
        (4, 3, (2, 1), "check", "Medium", "Reem walks", "تمشي ريم"),
        (4, 4, (2, 2), "check", "Medium", "Khalid cycles", "يقود خالد دراجته"),
        (5, 3, (3, 2), "check", "Medium", "Amal walks", "تسير أمل"),
        (3, 3, (1, 1), "block", "Hard", "Ziad walks", "يسير زياد"),
        (4, 2, (2, 1), "block", "Hard", "Layla bikes", "تقود ليلى دراجتها"),
        (4, 3, (2, 2), "block", "Hard", "Badr jogs", "يجري بدر"),
        (5, 2, (3, 1), "block", "Hard", "Dana walks", "تمشي دانة"),
    ]
    for cols, rows, pt, mode, diff, who_en, who_ar in path_cases:
        qid = next_id()
        tot_unblocked = math.comb(cols + rows, rows)
        assert _dp_paths(cols, rows, None) == tot_unblocked

        if mode == "plain":
            ans = tot_unblocked
            svg = svg_street_grid(cols, rows)
            q_en = (
                f"{who_en} along the {m(cols)}-by-{m(rows)} street grid shown from corner **A** (bottom-left) to corner **B** (top-right), "
                f"moving **only Right (East) or Up (North)** along the grid lines. How many different shortest paths from A to B are there?"
            )
            q_ar = (
                f"{who_ar} على شبكة الشوارع ذات الأبعاد {m(cols)} في {m(rows)} الموضّحة من الركن **A** (أسفل اليسار) إلى الركن **B** (أعلى اليمين)، "
                f"مع التحرك **يمينًا (شرقًا) أو لأعلى (شمالًا) فقط** على خطوط الشبكة. كم مسارًا أقصر مختلفًا يوجد من A إلى B؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans,
                [
                    cols * rows if cols * rows != ans else ans + 2,
                    cols + rows if cols + rows != ans else ans + 3,
                    ans + cols,
                    max(2, ans - 2),
                ],
                qid,
            )
            hint_en = f"Every shortest path takes {cols} Right steps and {rows} Up steps ({cols + rows} steps total) — or label intersections by adding the numbers from left and below!"
            hint_ar = f"كل مسار أقصر يتكوّن من {cols} خطوات يمينًا و{rows} خطوات لأعلى ({cols + rows} خطوات إجمالًا) — أو اجمع أعداد التقاطعات من اليسار والأسفل!"
            sol_en = explain_en(
                f"Every shortest path consists of **{m(cols)} Right steps** and **{m(rows)} Up steps** in some order ({m(cols + rows)} steps total)!",
                [
                    f"Method 1 (Intersection Addition): label `1` along the bottom and left edges from A, and set each intersection equal to `(ways from left) + (ways from below)` until reaching B = **{m(ans)}**.",
                    f"Method 2 (Choosing Up steps): choose which {m(rows)} of the {m(cols + rows)} steps go Up: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {ans}')}.",
                ],
                f"Both Pascal's corner-addition method and {m(f'\\binom{{{cols + rows}}}{{{rows}}}')} give {m(ans)} paths!",
            )
            sol_ar = explain_ar(
                f"كل مسار أقصر يتطلّب **{m(cols)} خطوات يمينًا** و**{m(rows)} خطوات لأعلى** بأي ترتيب ({m(cols + rows)} خطوات إجمالًا)!",
                [
                    f"الطريقة 1 (جمع التقاطعات): نكتب `1` على الحافتين السفلية واليسرى انطلاقًا من A، وعند كل تقاطع نجمع العددين (من اليسار + من الأسفل) حتى نصل إلى B = **{m(ans)}**.",
                    f"الطريقة 2 (التوافيق): نختار مواقع خطوات الصعود الـ {m(rows)} من أصل {m(cols + rows)} خطوات: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {ans}')}.",
                ],
                f"تحقق: الطريقتان تعطيان {m(ans)} مسارًا بالضبط!",
            )

        elif mode == "check":
            pc, pr = pt
            w1 = math.comb(pc + pr, pr)
            w2 = math.comb((cols - pc) + (rows - pr), rows - pr)
            ans = w1 * w2
            svg = svg_street_grid(cols, rows)
            q_en = (
                f"{who_en} on the {m(cols)}-by-{m(rows)} street grid shown from **A** `(0, 0)` to **B** `({cols}, {rows})`, "
                f"moving only Right or Up. How many shortest paths **pass through** the checkpoint intersection **P`({pc}, {pr})`** "
                f"({m(pc)} blocks Right and {m(pr)} block(s) Up from A)?"
            )
            q_ar = (
                f"{who_ar} على شبكة الشوارع ذات الأبعاد {m(cols)} في {m(rows)} من **A** `(0, 0)` إلى **B** `({cols}, {rows})` "
                f"مع التحرك يمينًا أو لأعلى فقط. كم مسارًا أقصر **يمرّ عبر** نقطة التوقف **P`({pc}, {pr})`** "
                f"(على بُعد {m(pc)} وحدات يمينًا و{m(pr)} وحدات لأعلى من A)؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [w1 + w2, tot_unblocked, tot_unblocked - ans, ans + 4], qid
            )
            hint_en = "Split the journey into Stage 1 (A → P) and Stage 2 (P → B), then MULTIPLY the number of ways for each stage!"
            hint_ar = "قسّم الرحلة إلى مرحلتين: الأولى (A ← P) والثانية (P ← B)، ثم **اضرب** عدد طرق المرحلتين معًا!"
            sol_en = explain_en(
                "By the **Multiplication Principle**, `(Paths A → B via P) = (Paths A → P) × (Paths P → B)`!",
                [
                    f"**Stage 1 (`A → P`):** {m(pc)} Right and {m(pr)} Up → {m(f'\\binom{{{pc + pr}}}{{{pr}}} = {w1}')} ways.",
                    f"**Stage 2 (`P → B`):** {m(cols - pc)} Right and {m(rows - pr)} Up → {m(f'\\binom{{{(cols - pc) + (rows - pr)}}}{{{rows - pr}}} = {w2}')} ways.",
                    f"Multiply the two stages: {m(f'{w1} \\times {w2} = {ans}')} shortest paths.",
                ],
                f"Sanity check: {m(f'{ans} < {tot_unblocked}')} (must be less than all {m(tot_unblocked)} unrestricted paths—and remember to **multiply**, not add {m(f'{w1} + {w2}')}!).",
            )
            sol_ar = explain_ar(
                "بمبدأ العدّ الضربي: **(عدد المسارات عبر P) = (مسارات A ← P) × (مسارات P ← B)**!",
                [
                    f"**المرحلة الأولى (`A ← P`):** {m(pc)} يمينًا و{m(pr)} لأعلى → {m(f'\\binom{{{pc + pr}}}{{{pr}}} = {w1}')} طرق.",
                    f"**المرحلة الثانية (`P ← B`):** {m(cols - pc)} يمينًا و{m(rows - pr)} لأعلى → {m(f'\\binom{{{(cols - pc) + (rows - pr)}}}{{{rows - pr}}} = {w2}')} طرق.",
                    f"نضرب المرحلتين معًا: {m(f'{w1} \\times {w2} = {ans}')} مسارًا.",
                ],
                f"انتبه: نضرب {m(f'{w1} \\times {w2}')} ولا نجمع {m(f'{w1} + {w2}')} لأن أي طريق في المرحلة الأولى يقترن بأي طريق في الثانية!",
            )

        else:  # block
            bc, br = pt
            through_x = math.comb(bc + br, br) * math.comb((cols - bc) + (rows - br), rows - br)
            ans = tot_unblocked - through_x
            assert _dp_paths(cols, rows, blocked=pt) == ans
            svg = svg_street_grid(cols, rows, blocked=pt)
            q_en = (
                f"{who_en} from **A** `(0, 0)` to **B** `({cols}, {rows})` along the {m(cols)}-by-{m(rows)} street grid shown, "
                f"moving only Right or Up, while avoiding the closed intersection marked **`×`** at `({bc}, {br})`. "
                f"How many shortest paths from A to B avoid **`×`**?"
            )
            q_ar = (
                f"{who_ar} من **A** `(0, 0)` إلى **B** `({cols}, {rows})` على شبكة الشوارع ({m(cols)} في {m(rows)}) الموضّحة "
                f"يمينًا أو لأعلى فقط، مع تجنّب التقاطع المغلق المشار إليه بالعلامة **`×`** عند `({bc}, {br})`. "
                f"كم مسارًا أقصر من A إلى B يتجنّب التقاطع **`×`**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [tot_unblocked, through_x, ans + 2, max(1, ans - 2)], qid
            )
            hint_en = "Complementary counting: (Valid paths) = (All paths A → B) − (Forbidden paths passing through ×)!"
            hint_ar = "استخدم العدّ العكسي (المتمم): (المسارات المسموحة) = (جميع المسارات من A إلى B) − (المسارات المارة عبر ×)!"
            sol_en = explain_en(
                "Count **all** paths without restrictions first, then subtract the paths that hit **`×`** (or set **`× = 0`** in the corner-addition grid)!",
                [
                    f"All shortest paths without the roadblock: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {tot_unblocked}')}.",
                    f"Paths hitting `×({bc}, {br})`: {m(f'\\binom{{{bc + br}}}{{{br}}} \\times \\binom{{{(cols - bc) + (rows - br)}}}{{{rows - br}}} = {through_x}')}.",
                    f"Valid paths avoiding `×`: {m(f'{tot_unblocked} - {through_x} = {ans}')}.",
                ],
                f"Grid DP check: setting intersection `({bc}, {br}) = 0` and summing `left + below` across the grid confirms **{m(ans)}**!",
            )
            sol_ar = explain_ar(
                "نحسب **جميع** المسارات أولًا، ثم نطرح المسارات التي تمرّ بالتقاطع المغلق **`×`** (أو نضع `0` عند `×` أثناء جمع التقاطعات)!",
                [
                    f"إجمالي المسارات دون إغلاق: {m(f'\\binom{{{cols + rows}}}{{{rows}}} = {tot_unblocked}')}.",
                    f"المسارات المارة عبر `×({bc}, {br})`: {m(f'\\binom{{{bc + br}}}{{{br}}} \\times \\binom{{{(cols - bc) + (rows - br)}}}{{{rows - br}}} = {through_x}')}.",
                    f"المسارات السليمة المتجنبة لـ `×`: {m(f'{tot_unblocked} - {through_x} = {ans}')}.",
                ],
                f"تحقق بجمع الشبكة: وضع القيمة `0` عند التقاطع المغلق وجمع (اليسار + الأسفل) يعطي **{m(ans)}** بالضبط!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Combinatorics & Logic", diff, "g67-shortest-street-grid",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    # -------------------------------------------------------------------------
    # 18. g67-pie-chart-sectors (16 Qs: 5 Easy, 7 Medium, 4 Hard)
    # -------------------------------------------------------------------------
    pie_cases = [
        # Easy (5): 3 pct_to_deg, 2 deg_to_cnt
        ("pct_to_deg", "Easy", 25, 0, [(0.25, "25%"), (0.35, "35%"), (0.40, "40%")], "swimming", "السباحة", "sports survey", "استبيان الرياضة"),
        ("pct_to_deg", "Easy", 35, 0, [(0.35, "35%"), (0.25, "25%"), (0.40, "40%")], "fiction books", "قصص الخيال", "reading poll", "استطلاع القراءة"),
        ("pct_to_deg", "Easy", 15, 0, [(0.15, "15%"), (0.45, "45%"), (0.40, "40%")], "cycling", "ركوب الدراجة", "commute chart", "مخطط المواصلات"),
        ("deg_to_cnt", "Easy", 120, 90, [(1 / 3, "120°"), (5 / 12, "150°"), (1 / 4, "90°")], "robotics", "الروبوتات", "STEM camp", "مخيم العلوم"),
        ("deg_to_cnt", "Easy", 72, 125, [(0.20, "72°"), (0.40, "144°"), (0.40, "144°")], "astronomy", "الفلك", "science fair", "معرض العلوم"),
        # Medium (7): 3 missing_cnt, 2 total_from_sec, 2 diff_sec
        ("miss_pct_cnt", "Medium", 200, 20, [(0.35, "35%"), (0.25, "25%"), (0.20, "20%"), (0.20, "?")], "art", "الفنون", "elective poll", "استبيان النشاط"),
        ("miss_pct_cnt", "Medium", 160, 15, [(0.40, "40%"), (0.25, "25%"), (0.20, "20%"), (0.15, "?")], "mango", "المانجو", "juice survey", "استطلاع العصائر"),
        ("miss_deg_cnt", "Medium", 120, 108, [(0.25, "90°"), (1 / 3, "120°"), (42 / 360, "42°"), (0.30, "?")], "chess", "الشطرنج", "board-game vote", "تصويت الألعاب"),
        ("tot_from_deg", "Medium", 108, 45, [(0.30, "108°"), (0.45, "162°"), (0.25, "90°")], "football", "كرة القدم", "PE poll", "استبيان التربية البدنية"),
        ("tot_from_deg", "Medium", 80, 32, [(2 / 9, "80°"), (4 / 9, "160°"), (1 / 3, "120°")], "violin", "الكمان", "music club", "نادي الموسيقى"),
        ("diff_deg", "Medium", 180, 60, [(4 / 9, "160°"), (5 / 18, "100°"), (5 / 18, "100°")], "blue over green", "الأزرق على الأخضر", "color vote", "تصويت الألوان"),
        ("diff_pct", "Medium", 240, 15, [(0.45, "45%"), (0.30, "30%"), (0.25, "25%")], "bus over walk", "الحافلة على المشي", "school travel", "وسيلة الذهاب للمدرسة"),
        # Hard (4): mixed angle + percent clues!
        ("mix_tot", "Hard", 20, 180, [(0.25, "90°"), (0.35, "35%"), (104 / 360, "104°"), (40 / 360, "?")], "drama", "المسرح", "talent show", "عرض المواهب"),
        ("mix_tot2", "Hard", 28, 160, [(0.25, "90°"), (0.30, "30%"), (11 / 40, "99°"), (7 / 40, "?")], "calligraphy", "الخط العربي", "culture day", "يوم الثقافة"),
        ("mix_sec", "Hard", 36, 240, [(0.25, "90°"), (0.40, "144°"), (0.20, "20%"), (0.15, "?")], "tennis", "التنس", "club signup", "التسجيل بالأندية"),
        ("mix_sec2", "Hard", 27, 180, [(1 / 3, "120°"), (0.30, "30%"), (13 / 60, "78°"), (0.15, "?")], "coding", "البرمجة", "summer academy", "الأكاديمية الصيفية"),
    ]
    for idx_p, (mode, diff, p1, p2, slices, cat_en, cat_ar, poll_en, poll_ar) in enumerate(pie_cases):
        qid = next_id()
        svg = svg_pie_chart(slices)

        if mode == "pct_to_deg":
            pct = p1
            ans = (pct * 360) // 100
            q_en = (
                f"In the {poll_en} pie chart shown, **{cat_en}** accounts for {m(f'{pct}\\%')} of all responses. "
                f"What is the **central angle** (in degrees) of the {cat_en} sector?"
            )
            q_ar = (
                f"في القطاعات الدائرية الخاصة بـ{poll_ar} الموضّحة، يمثّل قطاع **{cat_ar}** نسبة {m(f'{pct}\\%')} من جميع المشاركين. "
                f"ما قياس **الزاوية المركزية** (بالدرجات) لقطاع {cat_ar}؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [pct, pct * 2, 180 - ans if 180 - ans != ans else ans + 18, ans + 18], qid, suffix="^\\circ"
            )
            hint_en = f"A full circle has 360°, so find {pct}% of 360°: ({pct} ÷ 100) × 360°!"
            hint_ar = f"الدائرة الكاملة 360°، لذا احسب {pct}% من 360° أي ({pct} ÷ 100) × 360°!"
            sol_en = explain_en(
                "In any pie chart, **100% corresponds to 360°** (so every `5%` is `18°` and every `10%` is `36°`)!",
                [
                    f"Multiply the sector's fraction of the circle by {m('360^\\circ')}: {m(f'\\frac{{{pct}}}{{100}} \\times 360^\\circ = {ans}^\\circ')}.",
                ],
                f"Check: {m(f'\\frac{{{ans}^\\circ}}{{360^\\circ}} \\times 100\\% = {pct}\\%')}!",
            )
            sol_ar = explain_ar(
                "في التمثيل بالقطاعات الدائرية تقابل **100% زاوية كاملة قدرها 360°** (أي كل `5%` تقابل `18°` وكل `10%` تقابل `36°`)!",
                [
                    f"نضرب النسبة في {m('360^\\circ')}: {m(f'\\frac{{{pct}}}{{100}} \\times 360^\\circ = {ans}^\\circ')}.",
                ],
                f"تحقق: {m(f'\\frac{{{ans}^\\circ}}{{360^\\circ}} \\times 100\\% = {pct}\\%')} تمامًا!",
            )

        elif mode == "deg_to_cnt":
            deg, N = p1, p2
            ans = (N * deg) // 360
            g = math.gcd(deg, 360)
            q_en = (
                f"A {poll_en} surveyed {m(N)} students, and the **{cat_en}** sector in the pie chart has a central angle of {m(f'{deg}^\\circ')}. "
                f"How many students chose **{cat_en}**?"
            )
            q_ar = (
                f"شمل {poll_ar} إجمالي {m(N)} طالبًا، فكان قياس الزاوية المركزية لقطاع **{cat_ar}** في الدائرة {m(f'{deg}^\\circ')}. "
                f"كم طالبًا اختار **{cat_ar}**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 5, max(5, ans - 5), deg // 2, N - ans], qid
            )
            hint_en = f"Simplify the fraction ({deg}° ÷ 360°) first, then multiply by the {N} students!"
            hint_ar = f"بسّط كسر الدائرة ({deg}° ÷ 360°) أولًا، ثم اضرب في عدد الطلاب الـ {N}!"
            sol_en = explain_en(
                "Turn the central angle into a **simplified fraction of 360°**, then multiply by total students!",
                [
                    f"Fraction of the circle: {m(f'\\frac{{{deg}}}{{360}} = \\frac{{{deg // g}}}{{{360 // g}}}')}.",
                    f"Multiply by {m(N)} students: {m(f'\\frac{{{deg // g}}}{{{360 // g}}} \\times {N} = {ans}')} students.",
                ],
                f"Check: each student corresponds to {m(f'\\frac{{360^\\circ}}{{{N}}}')}, so {m(ans)} students span {m(f'{deg}^\\circ')}!",
            )
            sol_ar = explain_ar(
                "نحوّل الزاوية المركزية إلى **كسر مبسّط من 360°** ثم نضربه في إجمالي عدد الطلاب!",
                [
                    f"كسر القطاع من الدائرة: {m(f'\\frac{{{deg}}}{{360}} = \\frac{{{deg // g}}}{{{360 // g}}}')}.",
                    f"عدد الطلاب: {m(f'\\frac{{{deg // g}}}{{{360 // g}}} \\times {N} = {ans}')} طالبًا.",
                ],
                f"تحقق: {m(f'\\frac{{{ans}}}{{{N}}} \\times 360^\\circ = {deg}^\\circ')} بالضبط!",
            )

        elif mode == "miss_pct_cnt":
            N, rem_pct = p1, p2
            ans = (N * rem_pct) // 100
            p_known = [int(s[1].rstrip("%")) for s in slices[:-1]]
            q_en = (
                f"In a {poll_en} of {m(N)} students, the first three sectors of the pie chart represent "
                f"{m(f'{p_known[0]}\\%')}, {m(f'{p_known[1]}\\%')}, and {m(f'{p_known[2]}\\%')}, and the remaining `{m('?')}` sector is **{cat_en}**. "
                f"How many students chose **{cat_en}**?"
            )
            q_ar = (
                f"في {poll_ar} شمل {m(N)} طالبًا، تمثّل القطاعات الثلاثة الأولى نسب "
                f"{m(f'{p_known[0]}\\%')} و{m(f'{p_known[1]}\\%')} و{m(f'{p_known[2]}\\%')}، ويمثّل القطاع المتبقي `{m('?')}` **{cat_ar}**. "
                f"كم طالبًا اختار **{cat_ar}**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [rem_pct, ans + 8, max(4, ans - 6), (N * p_known[1]) // 100], qid
            )
            hint_en = f"All sectors add to 100%! Subtract ({p_known[0]} + {p_known[1]} + {p_known[2]})% from 100% first, then take that percentage of {N}."
            hint_ar = f"مجموع النسب 100%! اطرح مجموع النسب الثلاث من 100% أولًا، ثم احسب تلك النسبة من {N} طالبًا."
            sol_en = explain_en(
                "Find the missing percentage out of `100%` first, then convert that percentage into students!",
                [
                    f"Known percentages sum to {m(f'{p_known[0]}\\% + {p_known[1]}\\% + {p_known[2]}\\% = {100 - rem_pct}\\%')}.",
                    f"Remaining percentage for {cat_en}: {m(f'100\\% - {100 - rem_pct}\\% = {rem_pct}\\%')}.",
                    f"Number of students: {m(f'\\frac{{{rem_pct}}}{{100}} \\times {N} = {ans}')} students.",
                ],
                f"Read carefully: {m(rem_pct)} is the **percentage**, whereas **{m(ans)}** is the actual student count out of {m(N)}!",
            )
            sol_ar = explain_ar(
                "نوجد النسبة المئوية المتبقية من `100%` أولًا، ثم نضربها في العدد الكلي للطلاب!",
                [
                    f"مجموع النسب المعلومة: {m(f'{p_known[0]}\\% + {p_known[1]}\\% + {p_known[2]}\\% = {100 - rem_pct}\\%')}.",
                    f"نسبة قطاع {cat_ar}: {m(f'100\\% - {100 - rem_pct}\\% = {rem_pct}\\%')}.",
                    f"عدد الطلاب: {m(f'\\frac{{{rem_pct}}}{{100}} \\times {N} = {ans}')} طالبًا.",
                ],
                f"انتبه: العدد {m(rem_pct)} هو النسبة المئوية، أما عدد الطلاب الفعلي من أصل {m(N)} فهو **{m(ans)}**!",
            )

        elif mode == "miss_deg_cnt":
            N, rem_deg = p1, p2  # 120 students, angles 90, 120, 42 -> rem = 108 -> 120 * 108 / 360 = 36
            ans = (N * rem_deg) // 360
            q_en = (
                f"In a {poll_en} of {m(N)} students, three sectors have central angles {m('90^\\circ')}, {m('120^\\circ')}, and {m('42^\\circ')}, "
                f"and the fourth sector `{m('?')}` represents **{cat_en}**. How many students chose **{cat_en}**?"
            )
            q_ar = (
                f"في {poll_ar} شمل {m(N)} طالبًا، قياسات الزوايا المركزية لثلاثة قطاعات هي {m('90^\\circ')} و{m('120^\\circ')} و{m('42^\\circ')}، "
                f"ويمثّل القطاع الرابع `{m('?')}` **{cat_ar}**. كم طالبًا اختار **{cat_ar}**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [rem_deg, 30, 40, 24], qid
            )
            hint_en = f"Subtract 90° + 120° + 42° = 252° from 360° to find the missing angle ({rem_deg}°), then multiply ({rem_deg}/360) × {N}!"
            hint_ar = f"اطرح 90° + 120° + 42° = 252° من 360° لإيجاد الزاوية المفقودة ({rem_deg}°)، ثم اضرب ({rem_deg}/360) × {N}!"
            sol_en = explain_en(
                "All central angles around the center of a pie chart add up to **360°**!",
                [
                    f"Missing central angle: {m(f'360^\\circ - (90^\\circ + 120^\\circ + 42^\\circ) = 360^\\circ - 252^\\circ = {rem_deg}^\\circ')}.",
                    f"Students in {cat_en}: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {N} = \\frac{{{rem_deg}}}{{3}} = {ans}')} students.",
                ],
                f"Notice how clean {m('120 / 360 = 1/3')} is: every {m('3^\\circ')} represents {m(1)} student ({m('108 \\div 3 = 36')})!",
            )
            sol_ar = explain_ar(
                "مجموع الزوايا المركزية حول مركز الدائرة يساوي دائمًا **360°**!",
                [
                    f"الزاوية المفقودة: {m(f'360^\\circ - (90^\\circ + 120^\\circ + 42^\\circ) = 360^\\circ - 252^\\circ = {rem_deg}^\\circ')}.",
                    f"عدد طلاب {cat_ar}: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {N} = {ans}')} طالبًا.",
                ],
                f"ملاحظة سريعة: بما أن {m(120)} طالبًا يقابلون {m('360^\\circ')} فكل {m('3^\\circ')} تمثّل طالبًا واحدًا ({m('108 \\div 3 = 36')})!",
            )

        elif mode == "tot_from_deg":
            deg, k_stu = p1, p2
            ans = (k_stu * 360) // deg
            g = math.gcd(deg, 360)
            q_en = (
                f"In the {poll_en} pie chart shown, the **{cat_en}** sector has a central angle of {m(f'{deg}^\\circ')} "
                f"and represents **exactly** {m(k_stu)} students. How many students took part in the **entire** {poll_en}?"
            )
            q_ar = (
                f"في التمثيل الدائري لـ{poll_ar} الموضّح، تبلغ الزاوية المركزية لقطاع **{cat_ar}** {m(f'{deg}^\\circ')} "
                f"وتمثّل {m(k_stu)} طالبًا بالضبط. كم إجمالي عدد الطلاب المشاركين في الاستبيان **كاملًا**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans - 20, ans + 20, k_stu * 3, ans + 30], qid
            )
            hint_en = f"Since {deg}° out of 360° equals {k_stu} students, find how many degrees 1 student gets (or divide {k_stu} by {deg // g}/{360 // g})!"
            hint_ar = f"بما أن {deg}° من أصل 360° تقابل {k_stu} طالبًا، بسّط الكسر {deg}/360 = {deg // g}/{360 // g} ثم أوجد الكل!"
            sol_en = explain_en(
                "Work backwards from the known slice: find **1 unit part** first, then scale up to the whole circle!",
                [
                    f"Fraction of the circle for {cat_en}: {m(f'\\frac{{{deg}}}{{360}} = \\frac{{{deg // g}}}{{{360 // g}}}')}.",
                    f"Since {m(deg // g)} parts equal {m(k_stu)} students, {m(1)} part = {m(f'{k_stu} \\div {deg // g} = {k_stu // (deg // g)}')} students.",
                    f"Whole survey ({m(360 // g)} parts): {m(f'{360 // g} \\times {k_stu // (deg // g)} = {ans}')} students.",
                ],
                f"Check: {m(f'\\frac{{{deg}}}{{360}} \\times {ans} = {k_stu}')} students!",
            )
            sol_ar = explain_ar(
                "نعمل عكسيًا من القطاع المعلوم: نوجد قيمة **الجزء الواحد** أولًا ثم نضرب في أجزاء الدائرة كلها!",
                [
                    f"كسر القطاع من الدائرة: {m(f'\\frac{{{deg}}}{{360}} = \\frac{{{deg // g}}}{{{360 // g}}}')}.",
                    f"بما أن {m(deg // g)} أجزاء تساوي {m(k_stu)} طالبًا، فالجزء الواحد = {m(k_stu // (deg // g))} طلاب.",
                    f"إجمالي الطلاب ({m(360 // g)} أجزاء): {m(f'{360 // g} \\times {k_stu // (deg // g)} = {ans}')} طالبًا.",
                ],
                f"تحقق: {m(f'\\frac{{{deg}}}{{360}} \\times {ans} = {k_stu}')} طالبًا بالضبط!",
            )

        elif mode == "diff_deg":
            N, deg_diff = p1, p2  # N=180, angles 160° vs 100° -> diff 60° -> 180 * 60 / 360 = 30
            ans = (N * deg_diff) // 360
            q_en = (
                f"In a {poll_en} of {m(N)} students, the Blue sector has central angle {m('160^\\circ')} and the Green sector has central angle {m('100^\\circ')} "
                f"(with Red also {m('100^\\circ')}). How many **more** students voted for Blue than for Green?"
            )
            q_ar = (
                f"في {poll_ar} شمل {m(N)} طالبًا، بلغت الزاوية المركزية للون الأزرق {m('160^\\circ')} وللون الأخضر {m('100^\\circ')} "
                f"(وللأحمر {m('100^\\circ')}). بكم يزيد عدد المصوّتين للأزرق على المصوّتين للأخضر؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [deg_diff, 80, 50, ans + 10], qid
            )
            hint_en = f"Shortcut: subtract the angles FIRST (160° − 100° = 60° = 1/6 of the circle), then take 1/6 of {N}!"
            hint_ar = f"اختصار ذكي: اطرح الزاويتين أولًا (160° − 100° = 60° = سدس الدائرة)، ثم احسب سدس الـ {N} طالبًا!"
            sol_en = explain_en(
                "Subtract the central angles **before** converting to students to save half the arithmetic!",
                [
                    f"Angle difference: {m('160^\\circ - 100^\\circ = 60^\\circ')}, which is {m('\\frac{60}{360} = \\frac{1}{6}')} of the circle.",
                    f"Student difference: {m(f'\\frac{{1}}{{6}} \\times {N} = {ans}')} students.",
                ],
                f"Full check: Blue = {m(80)} students and Green = {m(50)} students; {m('80 - 50 = 30')}!",
            )
            sol_ar = explain_ar(
                "نطرح الزاويتين المركزيتين **أولًا** قبل التحويل إلى عدد طلاب لاختصار نصف الحسابات!",
                [
                    f"فرق الزاويتين: {m('160^\\circ - 100^\\circ = 60^\\circ')}، أي {m('\\frac{60}{360} = \\frac{1}{6}')} الدائرة.",
                    f"فرق عدد الطلاب: {m(f'\\frac{{1}}{{6}} \\times {N} = {ans}')} طالبًا.",
                ],
                f"تحقق كامل: الأزرق {m(80)} والأخضر {m(50)}، والفرق {m('80 - 50 = 30')} طالبًا!",
            )

        elif mode == "diff_pct":
            N, pct_diff = p1, p2  # N=240, 45% vs 30% -> 15% of 240 = 36
            ans = (N * pct_diff) // 100
            q_en = (
                f"In a {poll_en} survey of {m(N)} students, {m('45\\%')} ride the bus, {m('30\\%')} walk, and {m('25\\%')} come by car. "
                f"How many **more** students ride the bus than walk?"
            )
            q_ar = (
                f"في استبيان {poll_ar} لعدد {m(N)} طالبًا، يركب {m('45\\%')} الحافلة، ويمشي {m('30\\%')}، ويأتي {m('25\\%')} بالسيارة. "
                f"بكم يزيد عدد ركّاب الحافلة على الذين يمشون؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [pct_diff, 108, 72, ans + 12], qid
            )
            hint_en = f"Subtract the percentages first (45% − 30% = 15%), then calculate 15% of {N}!"
            hint_ar = f"اطرح النسبتين أولًا (45% − 30% = 15%)، ثم احسب 15% من {N}!"
            sol_en = explain_en(
                "Take the difference of percentages first (`45% − 30% = 15%`), then multiply by the total!",
                [
                    f"Percentage gap: {m('45\\% - 30\\% = 15\\%')}.",
                    f"Compute {m('15\\%')} of {m(N)}: {m(f'10\\% = {N // 10}')} and {m(f'5\\% = {N // 20}')}, so {m(f'{N // 10} + {N // 20} = {ans}')} students.",
                ],
                f"Check: Bus = {m(108)}, Walk = {m(72)}, and {m('108 - 72 = 36')}!",
            )
            sol_ar = explain_ar(
                "نطرح النسبتين المئويتين أولًا (`45% − 30% = 15%`) ثم نضرب في العدد الكلي!",
                [
                    f"فرق النسبتين: {m('45\\% - 30\\% = 15\\%')}.",
                    f"نحسب {m('15\\%')} من {m(N)}: {m('10\\% = 24')} و{m('5\\% = 12')}، إذن المجموع {m('24 + 12 = 36')} طالبًا.",
                ],
                f"تحقق: الحافلة {m(108)} والمشي {m(72)}، والفرق {m('108 - 72 = 36')}!",
            )

        elif mode in ("mix_tot", "mix_tot2"):
            k_rem, ans = p1, p2
            pct_mid = 35 if mode == "mix_tot" else 30
            ang3 = 104 if mode == "mix_tot" else 99
            ang_mid = (pct_mid * 360) // 100
            rem_deg = 360 - (90 + ang_mid + ang3)
            assert (ans * rem_deg) == k_rem * 360
            q_en = (
                f"In a {poll_en} pie chart, the four sectors have measures {m('90^\\circ')}, {m(f'{pct_mid}\\%')}, {m(f'{ang3}^\\circ')}, "
                f"and the remaining sector **{cat_en}** `{m('?')}`, which contains **exactly** {m(k_rem)} students. "
                f"How many students participated in the **entire** {poll_en}?"
            )
            q_ar = (
                f"في التمثيل الدائري لـ{poll_ar}، مقادير القطاعات الأربعة هي: زاوية {m('90^\\circ')}، ونسبة {m(f'{pct_mid}\\%')}، وزاوية {m(f'{ang3}^\\circ')}، "
                f"والقطاع المتبقي **{cat_ar}** `{m('?')}` الذي يضم {m(k_rem)} طالبًا بالضبط. "
                f"كم إجمالي عدد الطلاب المشاركين في الاستبيان **كاملًا**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans - 20, ans + 20, rem_deg * 2, ans + 40], qid
            )
            hint_en = f"Convert {pct_mid}% into degrees ({ang_mid}°) so ALL sectors are in degrees! Subtract (90° + {ang_mid}° + {ang3}°) from 360° to find the {cat_en} angle."
            hint_ar = f"حوّل {pct_mid}% إلى درجات ({ang_mid}°) لتتوحّد الوحدات بالدرجات! ثم اطرح مجموع الزوايا الثلاث من 360°."
            sol_en = explain_en(
                "Unify mixed units into **degrees** (out of `360°`) first, find the remaining angle, and scale up!",
                [
                    f"Convert {m(f'{pct_mid}\\%')} to degrees: {m(f'\\frac{{{pct_mid}}}{{100}} \\times 360^\\circ = {ang_mid}^\\circ')}.",
                    f"Remaining angle for {cat_en}: {m(f'360^\\circ - (90^\\circ + {ang_mid}^\\circ + {ang3}^\\circ) = {rem_deg}^\\circ')}.",
                    f"Since {m(f'{rem_deg}^\\circ')} represents {m(k_rem)} students, total students = {m(f'{k_rem} \\times \\frac{{360}}{{{rem_deg}}} = {ans}')}!",
                ],
                f"Check: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {ans} = {k_rem}')} students!",
            )
            sol_ar = explain_ar(
                "نوحّد الوحدات المختلطة إلى **درجات** (من أصل `360°`) أولًا، ثم نوجد الزاوية المتبقية ومنها العدد الكلي!",
                [
                    f"نحوّل {m(f'{pct_mid}\\%')} إلى درجات: {m(f'\\frac{{{pct_mid}}}{{100}} \\times 360^\\circ = {ang_mid}^\\circ')}.",
                    f"زاوية قطاع {cat_ar}: {m(f'360^\\circ - (90^\\circ + {ang_mid}^\\circ + {ang3}^\\circ) = {rem_deg}^\\circ')}.",
                    f"بما أن {m(f'{rem_deg}^\\circ')} تقابل {m(k_rem)} طالبًا، فالإجمالي = {m(f'{k_rem} \\times \\frac{{360}}{{{rem_deg}}} = {ans}')} طالبًا!",
                ],
                f"تحقق: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {ans} = {k_rem}')} طالبًا تمامًا!",
            )

        else:  # mix_sec / mix_sec2: given total N, mixed angles/pcts -> find remaining sector student count
            ans, N = p1, p2
            if mode == "mix_sec":
                # 90° (25%), 144° (40%), 20% -> rem = 15% of 240 = 36
                a1, a2, p3 = 90, 144, 20
                rem_deg = 360 - (90 + 144 + 72)
                assert rem_deg == 54 and (N * rem_deg) // 360 == ans
                clue_en = f"{m('90^\\circ')}, {m('144^\\circ')}, and {m('20\\%')}"
                clue_ar = f"{m('90^\\circ')} و{m('144^\\circ')} و{m('20\\%')}"
                p3_deg = 72
            else:
                # 120°, 30% (108°), 78° -> rem = 54° (15%) of 180 = 27
                a1, a2, p3 = 120, 78, 30
                p3_deg = 108
                rem_deg = 360 - (120 + 108 + 78)
                assert rem_deg == 54 and (N * rem_deg) // 360 == ans
                clue_en = f"{m('120^\\circ')}, {m('30\\%')}, and {m('78^\\circ')}"
                clue_ar = f"{m('120^\\circ')} و{m('30\\%')} و{m('78^\\circ')}"

            q_en = (
                f"A {poll_en} surveyed {m(N)} students across four choices. Three sectors measure {clue_en}, "
                f"and the fourth sector `{m('?')}` is **{cat_en}**. How many students signed up for **{cat_en}**?"
            )
            q_ar = (
                f"شمل {poll_ar} عدد {m(N)} طالبًا موزّعين على أربعة خيارات. مقادير ثلاثة قطاعات منها هي {clue_ar}، "
                f"والقطاع الرابع `{m('?')}` هو **{cat_ar}**. كم طالبًا سجّل في **{cat_ar}**؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [rem_deg, 15, ans + 9, ans - 6], qid
            )
            hint_en = f"Convert {p3}% into {p3_deg}° so all three known slices are in degrees, subtract from 360°, then multiply by {N} / 360!"
            hint_ar = f"حوّل النسبة {p3}% إلى {p3_deg}° لتصبح القطاعات الثلاثة بالدرجات، واطرحها من 360° ثم اضرب في {N} / 360!"
            sol_en = explain_en(
                "Convert percentages and angles to the **same unit** (`360°`), find the fourth slice, and compute its share of `N`!",
                [
                    f"Convert {m(f'{p3}\\%')} to degrees: {m(f'\\frac{{{p3}}}{{100}} \\times 360^\\circ = {p3_deg}^\\circ')}.",
                    f"Fourth sector angle: {m(f'360^\\circ - ({a1}^\\circ + {a2}^\\circ + {p3_deg}^\\circ) = {rem_deg}^\\circ')} (which is {m('15\\%')} of the circle).",
                    f"Students in {cat_en}: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {N} = {ans}')} students.",
                ],
                f"Check: {m('15\\%')} of {m(N)} is {m(f'0.15 \\times {N} = {ans}')} students!",
            )
            sol_ar = explain_ar(
                "نوحّد النسب والزوايا إلى **درجات من 360°**، ثم نحسب زاوية القطاع الرابع ونصيبه من الطلاب!",
                [
                    f"نحوّل {m(f'{p3}\\%')} إلى درجات: {m(f'\\frac{{{p3}}}{{100}} \\times 360^\\circ = {p3_deg}^\\circ')}.",
                    f"زاوية قطاع {cat_ar}: {m(f'360^\\circ - ({a1}^\\circ + {a2}^\\circ + {p3_deg}^\\circ) = {rem_deg}^\\circ')} (أي {m('15\\%')} من الدائرة).",
                    f"عدد الطلاب: {m(f'\\frac{{{rem_deg}}}{{360}} \\times {N} = {ans}')} طالبًا.",
                ],
                f"تحقق: {m('15\\%')} من {m(N)} تساوي {m(ans)} طالبًا بالضبط!",
            )

        items.append(
            make_kmc_question(
                qid, LEVEL, "Data & Probability", diff, "g67-pie-chart-sectors",
                q_en, q_ar, opts_en, opts_ar, cidx, cans,
                hint_en, hint_ar, sol_en, sol_ar, diagram_en=svg,
            )
        )

    assert len(items) == 50
    return items


def generate_t1_extra() -> list[dict]:
    """Generate 300 verified Track 1 (Grades 6-7) KMC expansion questions across 18 blueprints."""
    idx = 1

    def next_id() -> str:
        nonlocal idx
        qid = f"KAUST-G67-X{idx:03d}"
        idx += 1
        return qid

    items = (
        _gen_group_1_1(next_id)
        + _gen_group_1_2(next_id)
        + _gen_group_1_3(next_id)
        + _gen_group_1_4(next_id)
        + _gen_group_1_5(next_id)
        + _gen_group_1_6(next_id)
    )
    assert len(items) == 300, f"Expected 300 Track 1 extra items, got {len(items)}"
    return items
