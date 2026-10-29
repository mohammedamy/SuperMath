"""KAUST Mathematics Competition (KMC) — Track 1: Grades 6-7
Pillar 2: Algebra, Growing Patterns, Balance Scales & Word Equations (110 questions).
Strictly aligned with official KMC Grades 6-7 syllabus (no calculators).
"""
from kmc_common import m, explain_en, explain_ar, make_5_math_options, make_kmc_question
from kmc_diagrams import (
    svg_matchstick_squares,
    svg_matchstick_triangles,
    svg_balance_scales,
    svg_number_strip,
    svg_number_line_jumps,
)

LEVEL = "Track 1: Grades 6-7"


def generate_t1_algebra() -> list[dict]:
    items = []
    idx = 1

    def next_id():
        nonlocal idx
        qid = f"KAUST-G67-A{idx:03d}"
        idx += 1
        return qid

    # 1. Adjacent matchstick squares: 3n + 1 = S (10 variants with KMC matchstick SVG!) — KMC G6-7 Sample Q2
    msq_cases = [
        (100, "squares_from_sticks"), (76, "squares_from_sticks"), (121, "squares_from_sticks"),
        (64, "squares_from_sticks"), (151, "squares_from_sticks"), (88, "squares_from_sticks"),
        (20, "sticks_from_squares"), (25, "sticks_from_squares"), (30, "sticks_from_squares"),
        (40, "sticks_from_squares"),
    ]
    svg_msq = svg_matchstick_squares((1, 2, 3))
    for val_in, mode in msq_cases:
        qid = next_id()
        if mode == "squares_from_sticks":
            sticks = val_in
            assert (sticks - 1) % 3 == 0
            ans = (sticks - 1) // 3
            q_en = (
                f"The figure shows a row of adjacent squares built from identical sticks: Figure (1) uses {m(4)} sticks, "
                f"Figure (2) uses {m(7)} sticks, Figure (3) uses {m(10)} sticks, and so on. "
                f"How many squares are in the figure built from **exactly** {m(sticks)} sticks?"
            )
            q_ar = (
                f"يبيّن الشكل صفًا من المربعات المتجاورة المصنوعة من أعواد متطابقة: الشكل (1) يحتاج {m(4)} أعواد، "
                f"والشكل (2) يحتاج {m(7)} أعواد، والشكل (3) يحتاج {m(10)} أعواد، وهكذا. "
                f"كم مربعًا في الشكل المصنوع من {m(sticks)} عودًا بالضبط؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, ans - 1, sticks // 4, ans + 2], qid
            )
            sol_en = explain_en(
                "Start with the **leftmost vertical stick** (that is 1 stick), and notice that **every square adds 3 more sticks** (top, bottom, and right)!",
                [
                    f"Test the pattern on the first figures: Figure (1) has {m('1 + 3 \\times 1 = 4')} sticks; Figure (2) has {m('1 + 3 \\times 2 = 7')} sticks; Figure (3) has {m('1 + 3 \\times 3 = 10')} sticks. So {m('n')} squares need {m('3n + 1')} sticks.",
                    f"Set up the simple equation {m(f'3n + 1 = {sticks}')}.",
                    f"Subtract {m(1)} from both sides: {m(f'3n = {sticks - 1}')}. Now divide by {m(3)}: {m(f'n = {sticks - 1} \\div 3 = {ans}')} squares.",
                ],
                f"Check: {m(f'3 \\times {ans} + 1 = {3*ans} + 1 = {sticks}')} sticks! (Dividing {m(f'{sticks} \\div 4')} ignores shared middle sticks.)",
            )
            sol_ar = explain_ar(
                "نبدأ بالعود الرأسي الأول في أقصى اليسار (عود واحد)، ثم نلاحظ أن **كل مربع جديد يضيف 3 أعواد فقط** (علوي وسفلي وأيمن) لأنه يشترك في الضلع الأيسر مع جاره!",
                [
                    f"نتأكد من القاعدة: الشكل (1) به {m('1 + 3(1) = 4')}، والشكل (2) به {m('1 + 3(2) = 7')}، إذن {m('n')} مربعًا تحتاج {m('3n + 1')} عودًا.",
                    f"نكتب المعادلة: {m(f'3n + 1 = {sticks}')}.",
                    f"نطرح {m(1)} من الطرفين فنحصل على {m(f'3n = {sticks - 1}')}، ثم نقسم على {m(3)}: {m(f'n = {sticks - 1} \\div 3 = {ans}')} مربعًا.",
                ],
                f"تحقق: {m(f'3 \\times {ans} + 1 = {sticks}')} عودًا بالضبط.",
            )
        else:
            n_sq = val_in
            ans = 3 * n_sq + 1
            q_en = (
                f"The figure shows adjacent squares made from identical sticks: Figure (1) has {m(1)} square and uses {m(4)} sticks, "
                f"Figure (2) has {m(2)} squares and uses {m(7)} sticks, and so on. "
                f"How many sticks are needed to build Figure ({m(n_sq)}) containing {m(n_sq)} squares in a single row?"
            )
            q_ar = (
                f"يوضّح الشكل مربعات متجاورة مصنوعة من أعواد متطابقة: الشكل (1) يحوي مربعًا واحدًا من {m(4)} أعواد، "
                f"والشكل (2) يحوي مربعين من {m(7)} أعواد، وهكذا. "
                f"كم عودًا يلزم لبناء الشكل ({m(n_sq)}) المكوّن من {m(n_sq)} مربعًا في صف واحد؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [4 * n_sq, 3 * n_sq, ans + 3, ans - 2], qid
            )
            sol_en = explain_en(
                "Instead of counting 4 sticks per square (which double-counts shared walls), notice that after the 1st stick on the far left, each square needs just **3 sticks**!",
                [
                    f"The first square uses {m(4)} sticks, and each of the remaining {m(n_sq - 1)} squares adds {m(3)} new sticks.",
                    f"Write the rule: total sticks {m(f'= 1 + 3 \\times {n_sq}')}.",
                    f"Multiply then add: {m(f'3 \\times {n_sq} = {3*n_sq}')}, and {m(f'{3*n_sq} + 1 = {ans}')} sticks.",
                ],
                f"Notice why {m(4 * n_sq)} is too big: there are {m(n_sq - 1)} shared inner walls, and {m(f'{4*n_sq} - {n_sq - 1} = {ans}')}!",
            )
            sol_ar = explain_ar(
                "بدلًا من ضرب عدد المربعات في 4 (وهو ما يحسب الأضلاع المشتركة مرتين)، نلاحظ أن كل مربع بعد العود الأيسر الأول يحتاج **3 أعواد فقط**!",
                [
                    f"المربع الأول يحتاج {m(4)} أعواد، وكل مربع من المربعات الـ {m(n_sq - 1)} التالية يضيف {m(3)} أعواد جديدة.",
                    f"وبصورة أبسط: عدد الأعواد لـ {m(n_sq)} مربعًا يساوي {m(f'3 \\times {n_sq} + 1')}.",
                    f"نحسب الناتج: {m(f'{3*n_sq} + 1 = {ans}')} عودًا.",
                ],
                f"تحقق بطريقة أخرى: {m(f'4 \\times {n_sq} = {4*n_sq}')} نطرح منها {m(n_sq - 1)} ضلعًا مشتركًا فنحصل على {m(ans)} عودًا.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g67-matchstick-squares",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Notice that each new square shares 1 vertical stick with its neighbor, so every square adds 3 sticks after the first!",
            "لاحظ أن كل مربع جديد يشترك في ضلع مع المربع السابق، فيضيف 3 أعواد فقط!",
            sol_en, sol_ar, diagram_en=svg_msq
        ))

    # 2. Matchstick triangle strip: 2n + 1 sticks (10 variants with KMC matchstick-triangle SVG!)
    mtri_cases = [
        (51, "tris"), (75, "tris"), (99, "tris"), (63, "tris"), (85, "tris"),
        (18, "sticks"), (24, "sticks"), (35, "sticks"), (42, "sticks"), (29, "sticks"),
    ]
    svg_mtri = svg_matchstick_triangles((1, 2, 3))
    for val_in, mode in mtri_cases:
        qid = next_id()
        if mode == "tris":
            sticks = val_in
            ans = (sticks - 1) // 2
            q_en = (
                f"Triangles are built in a continuous strip using identical sticks as shown: Figure (1) has {m(1)} triangle ({m(3)} sticks), "
                f"Figure (2) has {m(2)} triangles ({m(5)} sticks), and Figure (3) has {m(3)} triangles ({m(7)} sticks). "
                f"How many unit triangles are formed when **all** {m(sticks)} sticks are used?"
            )
            q_ar = (
                f"تُبنى مثلثات متجاورة في شريط متصل باستخدام أعواد متطابقة كما في الشكل: الشكل (1) به مثلث واحد ({m(3)} أعواد)، "
                f"والشكل (2) به مثلثان ({m(5)} أعواد)، والشكل (3) به {m(3)} مثلثات ({m(7)} أعواد). "
                f"كم مثلثًا صغيرًا يتكوّن عند استخدام {m(sticks)} عودًا بالكامل؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [ans + 1, ans - 1, sticks // 3, ans + 2], qid
            )
            sol_en = explain_en(
                "The first triangle uses 3 sticks, and each additional triangle shares 1 slanted side with the previous triangle, so it needs only **2 more sticks**!",
                [
                    f"Write the stick formula for {m('n')} triangles: {m('1 + 2n')} sticks (check: for {m('n=1,2,3')} we get {m('3,5,7')}).",
                    f"Set {m(f'2n + 1 = {sticks}')} and subtract {m(1)} from both sides: {m(f'2n = {sticks - 1}')}.",
                    f"Divide by {m(2)}: {m(f'n = {sticks - 1} \\div 2 = {ans}')} triangles.",
                ],
                f"Check: {m(f'2 \\times {ans} + 1 = {ans*2} + 1 = {sticks}')} sticks!",
            )
            sol_ar = explain_ar(
                "المثلث الأول يحتاج 3 أعواد، وكل مثلث جديد يشترك في ضلع مع سابقه فيضيف **عودين فقط**!",
                [
                    f"قاعدة عدد الأعواد لـ {m('n')} مثلثًا هي {m('2n + 1')} (تحقق: عند {m('n=1,2,3')} نحصل على {m('3,5,7')}).",
                    f"نضع المعادلة {m(f'2n + 1 = {sticks}')}، ونطرح {m(1)} من الطرفين: {m(f'2n = {sticks - 1}')}.",
                    f"نقسم على {m(2)} فنجد عدد المثلثات: {m(f'n = {sticks - 1} \\div 2 = {ans}')}.",
                ],
                f"تحقق: {m(f'2 \\times {ans} + 1 = {sticks}')} عودًا تمامًا.",
            )
        else:
            n_t = val_in
            ans = 2 * n_t + 1
            q_en = (
                f"In the stick pattern shown, Figure (1) uses {m(3)} sticks for {m(1)} triangle, Figure (2) uses {m(5)} sticks for {m(2)} triangles, "
                f"and Figure (3) uses {m(7)} sticks for {m(3)} triangles. How many sticks are needed for Figure ({m(n_t)}) with {m(n_t)} triangles?"
            )
            q_ar = (
                f"في نمط الأعواد الموضّح، يحتاج الشكل (1) إلى {m(3)} أعواد لمثلث واحد، والشكل (2) إلى {m(5)} أعواد لمثلثين، "
                f"والشكل (3) إلى {m(7)} أعواد لثلاثة مثلثات. كم عودًا يلزم للشكل ({m(n_t)}) المكوّن من {m(n_t)} مثلثًا؟"
            )
            opts_en, opts_ar, cidx, cans = make_5_math_options(
                ans, [3 * n_t, 2 * n_t, ans + 2, ans - 2], qid
            )
            sol_en = explain_en(
                "Notice the numbers of sticks increase by **+2 each time**: 3, 5, 7, 9, ... That means 2 sticks per triangle plus 1 starting stick!",
                [
                    f"For {m('n')} triangles, the formula is {m('2n + 1')} sticks.",
                    f"Substitute {m(f'n = {n_t}')}: {m(f'2 \\times {n_t} + 1 = {2*n_t} + 1 = {ans}')}.",
                ],
                f"Check via shared sides: {m(n_t)} separate triangles would take {m(3*n_t)} sticks, minus {m(n_t - 1)} shared inner sticks = {m(ans)}.",
            )
            sol_ar = explain_ar(
                "نلاحظ أن عدد الأعواد يزداد بمقدار **2 في كل مرة**: 3، 5، 7، ... أي عودان لكل مثلث زائد عود البداية!",
                [
                    f"القاعدة العامة لعدد الأعواد في الشكل ذي {m('n')} مثلثًا هي {m('2n + 1')}.",
                    f"نعوّض {m(f'n = {n_t}')}: {m(f'2 \\times {n_t} + 1 = {2*n_t} + 1 = {ans}')} عودًا.",
                ],
                f"تحقق: {m(f'3 \\times {n_t} = {3*n_t}')} مطروحًا منها {m(n_t - 1)} ضلعًا مشتركًا يعطي {m(ans)} عودًا.",
            )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g67-matchstick-triangles",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Each new triangle shares one stick with its neighbor, so it adds only 2 sticks.",
            "كل مثلث جديد يشترك في عود واحد مع جاره، لذا يضيف عودين فقط.",
            sol_en, sol_ar, diagram_en=svg_mtri
        ))

    # 3. Balanced two-scale shape puzzles (10 variants with KMC balance-scale SVG!) — KMC G6-7 Sample Q10
    # Scale 1: c1 circles = s1 squares; Scale 2: s2 squares = t2 triangles. Ask: how many triangles balance ask_c circles?
    scale_cases = [
        (3, 2, 1, 3, 2),   # 3C = 2S, 1S = 3T => 3C = 6T => 1C = 2T => 2C = 4T
        (2, 3, 1, 2, 2),   # 2C = 3S, 1S = 2T => 2C = 6T => 2C = 6T
        (4, 2, 1, 4, 3),   # 4C = 2S, 1S = 4T => 4C = 8T => 1C = 2T => 3C = 6T
        (3, 4, 2, 3, 2),   # 3C = 4S, 2S = 3T => 4S = 6T => 3C = 6T => 1C = 2T => 2C = 4T
        (2, 4, 1, 3, 1),   # 2C = 4S => 1C = 2S; 1S = 3T => 1C = 6T
        (3, 2, 2, 6, 4),   # 3C = 2S, 2S = 6T => 3C = 6T => 1C = 2T => 4C = 8T
        (2, 3, 3, 4, 4),   # 2C = 3S, 3S = 4T => 2C = 4T => 4C = 8T
        (4, 3, 1, 4, 2),   # 4C = 3S, 1S = 4T => 3S = 12T => 4C = 12T => 1C = 3T => 2C = 6T
        (3, 1, 1, 6, 2),   # 3C = 1S, 1S = 6T => 3C = 6T => 1C = 2T => 2C = 4T
        (2, 2, 1, 5, 3),   # 2C = 2S => 1C = 1S = 5T => 3C = 15T
    ]
    for c1, s1, s2, t2, ask_c in scale_cases:
        qid = next_id()
        # 1 square = t2 / s2 triangles; 1 circle = (s1 / c1) * (t2 / s2) triangles
        num = ask_c * s1 * t2
        den = c1 * s2
        assert num % den == 0
        ans = num // den
        per_c = (s1 * t2) // (c1 * s2)
        svg = svg_balance_scales(c1, s1, s2, t2)
        c_word = "circle" if ask_c == 1 else "circles"
        c_word_ar = "دائرة واحدة" if ask_c == 1 else (f"دائرتين" if ask_c == 2 else f"{ask_c} دوائر")
        q_en = (
            f"Both scales in the figure are perfectly balanced (the left scale balances {m(c1)} orange circle(s) with {m(s1)} green square(s), "
            f"and the right scale balances {m(s2)} green square(s) with {m(t2)} purple triangle(s)). "
            f"How many triangles are needed to balance {m(ask_c)} {c_word}?"
        )
        q_ar = (
            f"الميزانان في الشكل متزنان تمامًا (الميزان الأيسر يوازن {m(c1)} من الدوائر البرتقالية مع {m(s1)} من المربعات الخضراء، "
            f"والميزان الأيمن يوازن {m(s2)} من المربعات الخضراء مع {m(t2)} من المثلثات البنفسجية). "
            f"كم مثلثًا يلزم لموازنة {c_word_ar}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [per_c if per_c != ans else ans + 2, ans + 2, max(1, ans - 2), s1 * t2 if s1 * t2 != ans else ans + 3, ans + 4], qid
        )
        mul_s = s1 // s2 if s1 % s2 == 0 else 1
        sol_en = explain_en(
            "Replace the green squares with their equivalent weight in triangles so we can compare circles directly to triangles!",
            [
                f"Look at the right scale: {m(s2)} square(s) balance {m(t2)} triangles.",
                f"Scale that up to match the {m(s1)} square(s) on the left scale: {m(s1)} square(s) equal {m(f'\\frac{{{s1}}}{{{s2}}} \\times {t2} = {(s1*t2)//s2}')} triangles.",
                f"Since the left scale shows {m(c1)} circles = {m(s1)} squares, we now know {m(c1)} circles = {m((s1*t2)//s2)} triangles, so {m(1)} circle = {m(f'{(s1*t2)//s2} \\div {c1} = {per_c}')} triangles.",
                f"Finally, for {m(ask_c)} {c_word}, multiply: {m(f'{ask_c} \\times {per_c} = {ans}')} triangles.",
            ],
            f"Give each triangle weight {m(1)}: then 1 circle weighs {m(per_c)}, and {m(ask_c)} {c_word} weigh {m(ans)} triangles!",
        )
        sol_ar = explain_ar(
            "نستبدل المربعات الخضراء بما يكافئها من المثلثات حتى نربط بين وزن الدوائر ووزن المثلثات مباشرة!",
            [
                f"من الميزان الأيمن: {m(s2)} من المربعات تعادل {m(t2)} مثلثات.",
                f"إذن {m(s1)} من المربعات (الموجودة في الميزان الأيسر) تعادل {m((s1*t2)//s2)} مثلثات.",
                f"وبما أن {m(c1)} دوائر توازن تلك المربعات، فإن {m(c1)} دوائر = {m((s1*t2)//s2)} مثلثات، أي الدائرة الواحدة = {m(per_c)} مثلثات.",
                f"لموازنة {c_word_ar} نضرب: {m(f'{ask_c} \\times {per_c} = {ans}')} مثلثات.",
            ],
            f"لو افترضنا وزن المثلث = {m(1)}، فإن وزن الدائرة = {m(per_c)}، ووزن المطلوب = {m(ans)} مثلثات.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g67-balance-scales",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Use the second scale to rewrite the squares on the first scale in terms of triangles!",
            "استخدم الميزان الثاني لاستبدال المربعات في الميزان الأول بعدد مكافئ من المثلثات!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 4. Five-cell sliding-sum number strip (10 variants with KMC strip SVG!) — KMC G6-7 Sample Q20
    # Strip: [L, a, b, c, R], sum1 = L+a+b, sum2 = a+b+c, sum3 = b+c+R => c = sum2 - (sum1 - L), b = sum3 - R - c
    strip_cases = [
        (10, 130, 100, 200, 300, "Abrar", "أبرار"),
        (15, 85, 90, 140, 210, "Salma", "سلمى"),
        (20, 90, 110, 160, 220, "Mazen", "مازن"),
        (12, 70, 80, 130, 175, "Joud", "جود"),
        (25, 110, 120, 180, 250, "Rayan", "ريان"),
        (18, 95, 100, 150, 215, "Hala", "حلا"),
        (30, 120, 150, 210, 280, "Ziad", "زياد"),
        (14, 66, 90, 125, 160, "Lama", "لمى"),
        (22, 88, 105, 155, 205, "Bader", "بدر"),
        (16, 104, 96, 160, 240, "farah", "فرح"),
    ]
    for L_v, R_v, s1, s2, s3, nm_e, nm_a in strip_cases:
        qid = next_id()
        nm_e_cap = nm_e.capitalize()
        ab = s1 - L_v
        c_val = s2 - ab
        b_val = s3 - R_v - c_val
        a_val = ab - b_val
        assert L_v + a_val + b_val == s1 and a_val + b_val + c_val == s2 and b_val + c_val + R_v == s3
        svg = svg_number_strip([str(L_v), "", "?", "", str(R_v)])
        q_en = (
            f"{nm_e_cap} wants to fill the three empty cells in the strip so that the sum of the **first three** cells is {m(s1)}, "
            f"the sum of the **middle three** cells is {m(s2)}, and the sum of the **last three** cells is {m(s3)}. "
            f"What number must go in the **center** cell marked {m('?')}?"
        )
        q_ar = (
            f"يريد/تريد {nm_a} ملء الخلايا الثلاث الفارغة في الشريط بحيث يكون مجموع **الخلايا الثلاث الأولى** {m(s1)}، "
            f"ومجموع **الخلايا الثلاث الوسطى** {m(s2)}، ومجموع **الخلايا الثلاث الأخيرة** {m(s3)}. "
            f"ما العدد الذي يجب وضعه في **الخلية الوسطى** المشار إليها بعلامة {m('?')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            b_val, [a_val, c_val, b_val + 10, b_val - 10], qid
        )
        sol_en = explain_en(
            "Name the three empty cells `a, b, c` from left to right, so the whole row is "
            f"{m(f'{L_v},\\; a,\\; b,\\; c,\\; {R_v}')}. Our goal is to find the middle cell {m('b')}!",
            [
                f"**First three cells:** {m(f'{L_v} + a + b = {s1}')}. Subtract {m(L_v)} to get {m(f'a + b = {s1} - {L_v} = {ab}')}.",
                f"**Middle three cells:** {m(f'(a + b) + c = {s2}')}. Since we just found {m(f'a + b = {ab}')}, substitute it in: {m(f'{ab} + c = {s2}')}, so {m(f'c = {s2} - {ab} = {c_val}')}.",
                f"**Last three cells:** {m(f'b + c + {R_v} = {s3}')}. Substitute {m(f'c = {c_val}')}: {m(f'b + {c_val + R_v} = {s3}')}, so {m(f'b = {s3} - {c_val + R_v} = {b_val}')}.",
            ],
            f"Full strip check: {m(f'[{L_v}, {a_val}, {b_val}, {c_val}, {R_v}]')} gives sums {m(s1)}, {m(s2)}, and {m(s3)}!",
        )
        sol_ar = explain_ar(
            f"نسمّي الخلايا الفارغة بالترتيب {m('a, b, c')} فيصبح الشريط: {m(f'{L_v},\\; a,\\; b,\\; c,\\; {R_v}')}، والمطلوب إيجاد الخلية الوسطى {m('b')}.",
            [
                f"**الثلاث الأولى:** {m(f'{L_v} + a + b = {s1}')}، ومنها نطرح {m(L_v)} فنجد {m(f'a + b = {s1} - {L_v} = {ab}')}.",
                f"**الثلاث الوسطى:** {m(f'(a + b) + c = {s2}')}، نعوّض {m(f'a + b = {ab}')} فنجد {m(f'c = {s2} - {ab} = {c_val}')}.",
                f"**الثلاث الأخيرة:** {m(f'b + c + {R_v} = {s3}')}، نعوّض {m(f'c = {c_val}')} فنحصل على {m(f'b = {s3} - {c_val} - {R_v} = {b_val}')}.",
            ],
            f"الشريط المكتمل هو {m(f'[{L_v}, {a_val}, {b_val}, {c_val}, {R_v}]')} ومجاميعه المتتالية هي {m(s1)} و {m(s2)} و {m(s3)} بالضبط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-sliding-number-strip",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Call the empty cells a, b, c. First find (a + b) from the first three cells, then use that to find c from the middle three!",
            "سمِّ الخلايا الفارغة a, b, c؛ أوجد (a + b) من الثلاث الأولى ثم استخدمه لإيجاد c من الثلاث الوسطى!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 5. Alternating number-line frog/robot jumps (+F right, -B left) (10 variants with KMC number-line SVG!) — KMC G6-7 Sample Q21
    jump_cases = [
        (5, 3, 20),   # parity trap! 20 is even -> 20 jumps! (At jump 17 it's at 16+5=21, jumping over 20!)
        (4, 2, 17),   # odd never reached? Wait: let's simulate exact first landing!
        (5, 2, 17),   # +5, -2: pos: 0, 5, 3, 8, 6, 11, 9, 14, 12, 17 -> jump 9!
        (6, 4, 18),   # +6, -4: pos: 0, 6, 2, 8, 4, 10, 6, 12, 8, 14, 10, 16, 12, 18 -> jump 13!
        (4, 1, 19),   # +4, -1: gain 3 per 2 jumps: 0,4,3,7,6,10,9,13,12,16,15,19 -> jump 11!
        (5, 3, 15),   # +5, -3: 0,5,2,7,4,9,6,11,8,13,10,15 -> jump 11!
        (7, 4, 22),   # +7, -4: 0,7,3,10,6,13,9,16,12,19,15,22 -> jump 11!
        (6, 3, 21),   # +6, -3: 0,6,3,9,6,12,9,15,12,18,15,21 -> jump 11!
        (5, 3, 18),   # +5, -3: even 18: at jump 15 -> 14+5=19 (misses 18!), at jump 16 -> 16, jump 17 -> 21, jump 18 -> 18!
        (4, 3, 10),   # +4, -3: gain 1 per 2 jumps: at jump 12 -> 6, jump 13 -> 10!
        (7, 5, 21),   # +7, -5: gain 2 per 2 jumps: jump 14 -> 14, jump 15 -> 21!
    ]
    # Pick 10 clean reachable cases (skip index 1 which was 4,2,17 unreachable)
    jump_cases = [c for c in jump_cases if c != (4, 2, 17)]
    assert len(jump_cases) == 10
    for fwd, back, target in jump_cases:
        qid = next_id()
        # Exact step-by-step simulation!
        pos = 0
        ans = None
        trace = [0]
        for j in range(1, 200):
            pos += fwd if j % 2 == 1 else -back
            trace.append(pos)
            if pos == target:
                ans = j
                break
        assert ans is not None, (fwd, back, target)
        svg = svg_number_line_jumps(fwd, back, target)
        gain = fwd - back
        q_en = (
            f"A frog starts at {m(0)} on a number line and jumps alternately: **{m(fwd)} units to the right**, "
            f"then **{m(back)} units to the left**, then {m(fwd)} right, {m(back)} left, and so on. "
            f"After how many individual jumps does it **land directly on** {m(target)} for the first time?"
        )
        q_ar = (
            f"يقف ضفدع عند الصفر ({m(0)}) على خط الأعداد ويقفز بالتناوب: **{m(fwd)} وحدات إلى اليمين**، "
            f"ثم **{m(back)} وحدات إلى اليسار**، وهكذا بالترتيب. "
            f"بعد كم قفزة منفردة يقف على العدد {m(target)} لأول مرة؟"
        )
        naive = (target // gain) * 2
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans - 2, ans + 2, naive if naive != ans else ans + 1, ans - 1, ans + 3], qid
        )
        first_few = " \\to ".join(map(str, trace[:min(8, ans + 1)]))
        sol_en = explain_en(
            f"Every pair of jumps (1 forward + 1 backward = **2 jumps**) moves the frog forward by a net gain of {m(f'{fwd} - {back} = {gain}')} units—but watch out! The frog can reach {m(target)} **on a forward jump** before stepping back, OR it might leap *over* {m(target)} without landing on it!",
            [
                f"After {m('2k')} jumps ({m('k')} pairs), the frog stands at {m(f'{gain}k')}. On the next (odd) jump {m('2k + 1')}, it lands at {m(f'{gain}k + {fwd}')}.",
                f"Track the landing positions carefully: {m(first_few + (' \\to \\dots' if ans >= 8 else ''))}.",
                (
                    f"Can {m(target)} be hit on an odd jump {m(f'{gain}k + {fwd} = {target}')}? Since {m(f'{target} - {fwd} = {target - fwd}')} IS divisible by {m(gain)} ({m(f'k = {(target-fwd)//gain}')}), at jump {m(f'2({(target-fwd)//gain}) = {ans-1}')} the frog is at {m(target - fwd)}, and on jump #{m(ans)} it leaps {m(f'+{fwd}')} directly onto {m(target)}!"
                    if (target - fwd) % gain == 0 else
                    f"Notice {m(f'{target} - {fwd} = {target - fwd}')} is NOT a multiple of {m(gain)}, so the frog jumps *over* {m(target)} on odd jumps without touching it! Instead, it lands on {m(target)} after {m(f'k = {target // gain}')} full forward-back pairs, which is {m(f'2 \\times {target // gain} = {ans}')} jumps."
                ),
            ],
            f"Position after jump #{m(ans - 1)} is {m(trace[ans - 1])}, and jump #{m(ans)} lands squarely on {m(trace[ans])}!",
        )
        sol_ar = explain_ar(
            f"كل زوج من القفزات (قفزة للأمام ثم قفزة للخلف = **قفزتين**) يقدّم الضفدع بمقدار صافي {m(f'{fwd} - {back} = {gain}')} وحدات، لكن يجب الانتباه لما إذا كان يصل إلى {m(target)} في القفزة الأمامية مباشرة أم يقفز فوقه!",
            [
                f"بعد {m('2k')} قفزة يقف الضفدع عند {m(f'{gain}k')}، وفي القفزة الفردية التالية رقم {m('2k + 1')} يصل إلى {m(f'{gain}k + {fwd}')}.",
                f"نتابع أوائل المواقع بالترتيب: {m(first_few + (' \\to \\dots' if ans >= 8 else ''))}.",
                (
                    f"نختبر القفزة الفردية: {m(f'{target} - {fwd} = {target - fwd}')} يقبل القسمة على {m(gain)} ({m(f'k = {(target-fwd)//gain}')})؛ إذن بعد {m(ans - 1)} قفزة يكون عند {m(target - fwd)}، وفي القفزة رقم {m(ans)} يتقدّم {m(fwd)} فيقف مباشرة على {m(target)}!"
                    if (target - fwd) % gain == 0 else
                    f"نلاحظ أن {m(f'{target} - {fwd} = {target - fwd}')} لا يقبل القسمة على {m(gain)}، أي أنه يتجاوز {m(target)} في القفزة الفردية دون الوقوف عليه! لذا يقف عليه بعد {m(f'k = {target // gain}')} أزواج كاملة، أي بعد {m(f'2 \\times {target // gain} = {ans}')} قفزة."
                ),
            ],
            f"عند القفزة رقم {m(ans - 1)} يكون عند {m(trace[ans - 1])}، وبالقفزة رقم {m(ans)} يقف تمامًا على {m(trace[ans])}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Hard", "g67-frog-alternating-jumps",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the net gain per 2 jumps ({fwd} - {back} = {gain}), and check carefully whether {target} is hit on an odd jump or an even jump!",
            f"احسب التقدم الصافي لكل قفزتين ({fwd} - {back} = {gain})، ثم تحقق هل يقف على {target} في قفزة فردية أم زوجية!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 6. "Thought of a number" linear word riddles (10 variants) — KMC G6-7 Sample Q5
    thought_cases = [
        (3, -7, 2, 4, "Huda", "هدى"),
        (4, -9, 2, 7, "Omar", "عمر"),
        (5, -12, 3, 6, "Layan", "ليان"),
        (3, 8, 5, -10, "Sami", "سامي"),
        (4, 5, 6, -17, "Maha", "مها"),
        (6, -15, 4, 7, "Nawaf", "نواف"),
        (5, -8, 2, 19, "Abeer", "عبير"),
        (4, -11, 3, 4, "Khaled", "خالد"),
        (7, -20, 4, 13, "Jana", "جنى"),
        (3, 14, 5, -12, "Talal", "طلال"),
    ]
    for m1, c1, m2, c2, nm_e, nm_a in thought_cases:
        qid = next_id()
        # m1 * x + c1 = m2 * x + c2
        ans = (c2 - c1) // (m1 - m2)
        assert m1 * ans + c1 == m2 * ans + c2 and ans > 0
        op1_e = f"subtracted {abs(c1)}" if c1 < 0 else f"added {c1}"
        op1_a = f"طرح/طرحت {abs(c1)}" if c1 < 0 else f"أضاف/أضافت {c1}"
        op2_e = f"{c2} more than {m2} times the number" if c2 > 0 else f"{abs(c2)} less than {m2} times the number"
        op2_a = f"يزيد بمقدار {c2} على {m2} أضعاف العدد" if c2 > 0 else f"ينقص بمقدار {abs(c2)} عن {m2} أضعاف العدد"
        q_en = (
            f"{nm_e} thought of a secret number, multiplied it by {m(m1)}, and then {op1_e}. "
            f"The final result was {op2_e}. What was the secret number?"
        )
        q_ar = (
            f"فكّر/فكّرت {nm_a} في عدد سري، فضربه في {m(m1)} ثم {op1_a}، فكان الناتج النهائي {op2_a}. "
            f"ما العدد السري؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 2, max(1, ans - 2), ans + 4, abs(c1) + abs(c2)], qid
        )
        lhs_s = f"{m1}x - {abs(c1)}" if c1 < 0 else f"{m1}x + {c1}"
        rhs_s = f"{m2}x + {c2}" if c2 > 0 else f"{m2}x - {abs(c2)}"
        res_v = m1 * ans + c1
        sol_en = explain_en(
            "Call the unknown number `x` and translate both halves of the sentence into simple algebra—then collect `x` on one side and numbers on the other!",
            [
                f"First expression (multiply by {m(m1)}, then {op1_e}): {m(lhs_s)}.",
                f"Second expression ({op2_e}): {m(rhs_s)}.",
                f"Set them equal: {m(f'{lhs_s} = {rhs_s}')}. Collect the {m('x')}-terms on one side and the constants on the other: {m(f'{abs(m1-m2)}x = {abs(c2-c1)}')}, so {m(f'x = {abs(c2-c1)} \\div {abs(m1-m2)} = {ans}')}.",
            ],
            f"Plug {m(f'x = {ans}')} back in: {m(f'{m1} \\times {ans} + ({c1}) = {res_v}')}, and {m(f'{m2} \\times {ans} + ({c2}) = {res_v}')}—an exact match!",
        )
        sol_ar = explain_ar(
            "نرمز للعدد المجهول بالرمز `x` ونحوّل العبارة اللفظية إلى معادلة بسيطة، ثم نجمع الحدود التي تحوي `x` في طرف والأعداد في الطرف الآخر!",
            [
                f"الطرف الأول من الوصف يُكتب: {m(lhs_s)}.",
                f"الطرف الثاني من الوصف يُكتب: {m(rhs_s)}.",
                f"نساوي الطرفين: {m(f'{lhs_s} = {rhs_s}')}، وبترتيب الحدود نحصل على {m(f'{abs(m1-m2)}x = {abs(c2-c1)}')}، ومنها {m(f'x = {abs(c2-c1)} \\div {abs(m1-m2)} = {ans}')}.",
            ],
            f"تحقق بالتعويض عن {m(f'x = {ans}')}: كلا الطرفين يعطي القيمة {m(res_v)} تمامًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Easy", "g67-thought-of-number",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Let the number be x, write {lhs_s} = {rhs_s}, and solve for x.",
            f"افرض العدد x واكتب المعادلة {lhs_s} = {rhs_s} ثم أوجد قيمة x.",
            sol_en, sol_ar
        ))

    # 7. Restaurant / hall tables with 3, 4, or 6 chairs (10 variants) — KMC G6-7 Sample Q19
    # Parameterize directly by (t_sm, t_md, t_lg, c_sm, c_md, c_lg) so every count is exact!
    table_cases = [
        (4, 6, 6, 3, 4, 6),
        (5, 5, 5, 3, 4, 6),
        (6, 5, 7, 3, 4, 6),
        (3, 5, 6, 2, 4, 6),
        (6, 6, 8, 3, 5, 6),
        (7, 4, 6, 3, 4, 5),
        (5, 7, 7, 2, 3, 5),
        (4, 5, 6, 3, 5, 8),
        (8, 6, 8, 3, 4, 6),
        (5, 4, 7, 2, 5, 6),
    ]
    for t_sm, t_md, t_lg, c_sm, c_md, c_lg in table_cases:
        qid = next_id()
        n_tot = t_sm + t_md + t_lg
        cap_sm_md = t_sm * c_sm + t_md * c_md
        cap_lg = t_lg * c_lg
        cap_all = cap_sm_md + cap_lg
        t_rem = t_sm + t_md
        num_md = cap_sm_md - c_sm * t_rem
        assert num_md == t_md * (c_md - c_sm)
        ans = t_sm
        q_en = (
            f"In a dining hall, there are {m(n_tot)} tables in total. Each table seats {m(c_sm)}, {m(c_md)}, or {m(c_lg)} people. "
            f"All tables seating {m(c_sm)} or {m(c_md)} people together hold {m(cap_sm_md)} people, while the entire hall holds {m(cap_all)} people. "
            f"How many tables seat **exactly** {m(c_sm)} people?"
        )
        q_ar = (
            f"في قاعة طعام توجد {m(n_tot)} طاولة، كل طاولة تتسع لـ {m(c_sm)} أو {m(c_md)} أو {m(c_lg)} أشخاص. "
            f"الطاولات التي تتسع لـ {m(c_sm)} أو {m(c_md)} أشخاص تستوعب معًا {m(cap_sm_md)} شخصًا، بينما تستوعب القاعة كلها {m(cap_all)} شخصًا. "
            f"كم عدد الطاولات التي تتسع لـ {m(c_sm)} أشخاص **بالضبط**؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [t_md, t_lg, ans + 1, max(1, ans - 1), t_rem], qid
        )
        sol_en = explain_en(
            f"First peel away the {m(c_lg)}-seat tables using the difference in people, then use the 'assume all are the smaller type' trick (no heavy algebra needed!) on the remaining tables!",
            [
                f"**Find the {m(c_lg)}-seat tables:** They hold the remaining {m(f'{cap_all} - {cap_sm_md} = {cap_lg}')} people, so there are {m(f'{cap_lg} \\div {c_lg} = {t_lg}')} such tables.",
                f"**Remaining tables:** {m(f'{n_tot} - {t_lg} = {t_rem}')} tables seat either {m(c_sm)} or {m(c_md)} people (holding {m(cap_sm_md)} people altogether).",
                f"**Assume all {m(t_rem)} tables had {m(c_sm)} chairs:** That would seat {m(f'{t_rem} \\times {c_sm} = {t_rem * c_sm}')} people — which is short by {m(f'{cap_sm_md} - {t_rem * c_sm} = {num_md}')} seats.",
                f"Upgrading one table from {m(c_sm)} to {m(c_md)} adds {m(c_md - c_sm)} seat(s), so there are {m(f'{num_md} \\div {c_md - c_sm} = {t_md}')} tables of {m(c_md)} chairs, leaving {m(f'{t_rem} - {t_md} = {ans}')} tables of {m(c_sm)} chairs!",
            ],
            f"Check: {m(f'{ans}\\times{c_sm} + {t_md}\\times{c_md} + {t_lg}\\times{c_lg} = {ans*c_sm} + {t_md*c_md} + {t_lg*c_lg} = {cap_all}')} seats across {m(f'{ans}+{t_md}+{t_lg}={n_tot}')} tables!",
        )
        sol_ar = explain_ar(
            f"نبدأ باستبعاد الطاولات الكبيرة ذات {m(c_lg)} مقاعد من فرق السعة، ثم نحل الطاولات المتبقية بطريقة الافتراض البسيطة دون معادلات معقدة!",
            [
                f"**عدد طاولات الـ {m(c_lg)} مقاعد:** تستوعب {m(f'{cap_all} - {cap_sm_md} = {cap_lg}')} شخصًا، فعددها {m(f'{cap_lg} \\div {c_lg} = {t_lg}')} طاولات.",
                f"**الطاولات المتبقية:** عددها {m(f'{n_tot} - {t_lg} = {t_rem}')} طاولة (بها {m(c_sm)} أو {m(c_md)} مقاعد وتستوعب {m(cap_sm_md)} شخصًا).",
                f"**نفترض مؤقتًا أن الـ {m(t_rem)} طاولة كلها بـ {m(c_sm)} مقاعد:** عندئذ تستوعب {m(f'{t_rem} \\times {c_sm} = {t_rem * c_sm}')} شخصًا، ويبقى نقص قدره {m(f'{cap_sm_md} - {t_rem * c_sm} = {num_md}')} مقعدًا.",
                f"كل طاولة بـ {m(c_md)} مقاعد تضيف {m(c_md - c_sm)} فوق الـ {m(c_sm)}، لذا عدد طاولات الـ {m(c_md)} مقاعد هو {m(f'{num_md} \\div {c_md - c_sm} = {t_md}')}، ويبقى لطاولات الـ {m(c_sm)} مقاعد: {m(f'{t_rem} - {t_md} = {ans}')} طاولات.",
            ],
            f"تحقق: {m(f'{ans}\\times{c_sm} + {t_md}\\times{c_md} + {t_lg}\\times{c_lg} = {cap_all}')} شخصًا ومجموع الطاولات {m(n_tot)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-three-table-sizes",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Subtract {cap_sm_md} from {cap_all} first to find how many people sit at the {c_lg}-seat tables!",
            f"اطرح {cap_sm_md} من {cap_all} أولًا لتعرف كم شخصًا يجلسون على طاولات الـ {c_lg} مقاعد!",
            sol_en, sol_ar
        ))

    # 8. Road signposts / collinear towns distance puzzle (10 variants) — KMC G6-7 Practice Set 2 Q3
    # Signpost 1 (between A and B): "A: d1 km, B: d2 km" => AB = d1 + d2.
    # Signpost 2 (further toward C, between B and C): "A: d3 km, C: d4 km" => AC = d3 + d4 => BC = AC - AB!
    sign_cases = [
        (2, 4, 9, 5),   # AB = 6, Sign2 at 9 from A (so 3 past B), C is 5 ahead => AC = 14, BC = 8
        (3, 5, 11, 6),  # AB = 8, AC = 17, BC = 9
        (4, 3, 10, 7),  # AB = 7, AC = 17, BC = 10
        (2, 6, 12, 4),  # AB = 8, AC = 16, BC = 8 -> wait let's ask distance from Sign2 to B or BC! Let's ask BC!
        (5, 4, 13, 8),  # AB = 9, AC = 21, BC = 12
        (3, 7, 14, 5),  # AB = 10, AC = 19, BC = 9
        (6, 5, 15, 9),  # AB = 11, AC = 24, BC = 13
        (4, 8, 17, 6),  # AB = 12, AC = 23, BC = 11
        (5, 6, 16, 7),  # AB = 11, AC = 23, BC = 12
        (7, 3, 14, 10), # AB = 10, AC = 24, BC = 14
    ]
    for d1, d2, d3, d4 in sign_cases:
        qid = next_id()
        AB = d1 + d2
        AC = d3 + d4
        ans = AC - AB
        q_en = (
            f"Towns {m('A')}, {m('B')}, and {m('C')} lie in that order along one straight desert highway. "
            f"A traveler between {m('A')} and {m('B')} passes Signpost 1, which reads: *{m('A')}: {m(d1)} km behind, {m('B')}: {m(d2)} km ahead*. "
            f"Later, between {m('B')} and {m('C')}, Signpost 2 reads: *{m('A')}: {m(d3)} km behind, {m('C')}: {m(d4)} km ahead*. "
            f"What is the distance in kilometers between Town {m('B')} and Town {m('C')}?"
        )
        q_ar = (
            f"تقع المدن {m('A')} ثم {m('B')} ثم {m('C')} بهذا الترتيب على طريق مستقيم واحد. "
            f"بين {m('A')} و {m('B')} توجد اللافتة الأولى ومكتوب عليها: *{m('A')} خلفك بـ {m(d1)} كم، و {m('B')} أمامك بـ {m(d2)} كم*. "
            f"وبعد تجاوز {m('B')} نحو {m('C')} توجد اللافتة الثانية ومكتوب عليها: *{m('A')} خلفك بـ {m(d3)} كم، و {m('C')} أمامك بـ {m(d4)} كم*. "
            f"كم المسافة بالكيلومتر بين المدينة {m('B')} والمدينة {m('C')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [AB, AC, d3 - AB + d2, ans + 2, abs(ans - 3)], qid
        )
        sol_en = explain_en(
            "Draw a straight line with points `A — B — C`! Signpost 1 tells us the total distance `AB`, and Signpost 2 tells us the total distance `AC`.",
            [
                f"**From Signpost 1 (between A and B):** {m('A')} is {m(d1)} km behind and {m('B')} is {m(d2)} km ahead, so the distance from {m('A')} to {m('B')} is {m(f'AB = {d1} + {d2} = {AB}')} km.",
                f"**From Signpost 2 (between B and C):** {m('A')} is {m(d3)} km behind and {m('C')} is {m(d4)} km ahead, so the total distance from {m('A')} to {m('C')} is {m(f'AC = {d3} + {d4} = {AC}')} km.",
                f"**Subtract to get BC:** Since {m('B')} sits on the straight road between {m('A')} and {m('C')}, {m(f'BC = AC - AB = {AC} - {AB} = {ans}')} km.",
            ],
            f"Check at Signpost 2: it is {m(f'{d3} - {AB} = {d3 - AB}')} km past {m('B')}, plus {m(d4)} km to {m('C')} gives {m(f'{d3 - AB} + {d4} = {ans}')} km!",
        )
        sol_ar = explain_ar(
            "تخيّل خطًا مستقيمًا عليه النقاط `A — B — C`؛ اللافتة الأولى تعطينا المسافة الكلية `AB`، واللافتة الثانية تعطينا المسافة الكلية `AC`!",
            [
                f"**من اللافتة الأولى (بين A و B):** المسافة بين {m('A')} و {m('B')} هي {m(f'AB = {d1} + {d2} = {AB}')} كم.",
                f"**من اللافتة الثانية (بين B و C):** المسافة الكلية بين {m('A')} و {m('C')} هي {m(f'AC = {d3} + {d4} = {AC}')} كم.",
                f"**نطرح لإيجاد BC:** بما أن {m('B')} تقع بينهما على نفس الخط المستقيم، فإن {m(f'BC = AC - AB = {AC} - {AB} = {ans}')} كم.",
            ],
            f"تحقق آخر: اللافتة الثانية تبعد عن {m('B')} مسافة {m(f'{d3} - {AB} = {d3 - AB}')} كم، يضاف إليها {m(d4)} كم حتى {m('C')} فيكون المجموع {m(ans)} كم.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-road-signposts",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Use Signpost 1 to find the distance from A to B, and Signpost 2 to find the whole distance from A to C.",
            "استخدم اللافتة الأولى لإيجاد المسافة بين A و B، واللافتة الثانية لإيجاد المسافة الكلية بين A و C.",
            sol_en, sol_ar
        ))

    # 9. Symmetric purchases (pens & notebooks: finding 1 pen + 1 notebook without heavy systems!) (10 variants)
    sym_shop = [
        (3, 5, 46, 5, 3, 42, "notebooks", "pens", "دفاتر", "أقلام"),
        (2, 4, 34, 4, 2, 38, "folders", "markers", "ملفات", "أقلام تظليل"),
        (4, 3, 53, 3, 4, 52, "juice boxes", "sandwiches", "علب عصير", "شطائر"),
        (5, 2, 41, 2, 5, 36, "erasers", "rulers", "مماحٍ", "مساطر"),
        (3, 4, 57, 4, 3, 55, "apples", "mangoes", "تفاحات", "حبات مانجو"),
        (2, 5, 47, 5, 2, 37, "stickers", "keychains", "ملصقات", "ميداليات مفاتيح"),
        (4, 6, 76, 6, 4, 84, "brushes", "paint tubes", "فُرش رسم", "أنابيب ألوان"),
        (3, 7, 68, 7, 3, 62, "cookies", "muffins", "بسكويتات", "كعكات"),
        (5, 4, 71, 4, 5, 73, "tennis balls", "wristbands", "كرات تنس", "أربطة معصم"),
        (2, 6, 54, 6, 2, 42, "pencils", "sketchpads", "أقلام رصاص", "كراسات رسم"),
    ]
    for a1, b1, c1, a2, b2, c2, it1_e, it2_e, it1_a, it2_a in sym_shop:
        qid = next_id()
        k_sum = a1 + a2
        assert b1 + b2 == k_sum and (c1 + c2) % k_sum == 0
        ans = (c1 + c2) // k_sum
        q_en = (
            f"At the school stationery shop, {m(a1)} {it1_e} and {m(b1)} {it2_e} cost {m(c1)} riyals altogether, "
            f"while {m(a2)} {it1_e} and {m(b2)} {it2_e} cost {m(c2)} riyals altogether. "
            f"How many riyals does **1 of each** ({m(1)} item + {m(1)} item) cost together?"
        )
        q_ar = (
            f"في مكتبة المدرسة، ثمن {m(a1)} {it1_a} و {m(b1)} {it2_a} معًا هو {m(c1)} ريالًا، "
            f"وثمن {m(a2)} {it1_a} و {m(b2)} {it2_a} معًا هو {m(c2)} ريالًا. "
            f"كم ريالًا يبلغ ثمن **قطعة واحدة من كل نوع معًا**؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 2, max(2, ans - 2), abs(c1 - c2), ans + 4], qid
        )
        sol_en = explain_en(
            "Don't waste time finding the price of each item separately! Notice what happens when you **put both shopping baskets together**!",
            [
                f"Add the two purchases together: you get {m(f'{a1} + {a2} = {k_sum}')} {it1_e} AND {m(f'{b1} + {b2} = {k_sum}')} {it2_e}.",
                f"Add the two total costs: {m(f'{c1} + {c2} = {c1 + c2}')} riyals.",
                f"Since {m(k_sum)} of each item cost {m(c1 + c2)} riyals, divide by {m(k_sum)} to get the cost of {m(1)} of each: {m(f'{c1 + c2} \\div {k_sum} = {ans}')} riyals!",
            ],
            f"Symmetry shortcut: {m(k_sum)} pairs cost {m(c1 + c2)} riyals, so {m(1)} pair costs {m(ans)} riyals.",
        )
        sol_ar = explain_ar(
            "لا حاجة لإيجاد سعر كل صنف على حدة! لاحظ الجمال في المسألة عند **جمع المشتريتين معًا في سلة واحدة**!",
            [
                f"بجمع المشتريتين معًا نحصل على {m(f'{a1} + {a2} = {k_sum}')} من الصنف الأول و {m(f'{b1} + {b2} = {k_sum}')} من الصنف الثاني.",
                f"نجمع السعرين الكليين: {m(f'{c1} + {c2} = {c1 + c2}')} ريالًا.",
                f"بما أن {m(k_sum)} أزواج (قطعة من الأول + قطعة من الثاني) ثمنها {m(c1 + c2)} ريالًا، نقسم على {m(k_sum)} فنجد ثمن الزوج الواحد: {m(f'{c1 + c2} \\div {k_sum} = {ans}')} ريالًا.",
            ],
            f"تحقق سريع: {m(f'{k_sum} \\times {ans} = {c1 + c2}')} ريالًا.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-symmetric-basket-sum",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Try adding the two purchases together — look at how many of each item you get!",
            "جرّب جمع المشتريتين معًا ولاحظ كم قطعة ستحصل عليها من كل نوع!",
            sol_en, sol_ar
        ))

    # 10. Age difference invariance puzzles (10 variants)
    age_cases = [
        (36, 8, 3, "A father", "his son", "الأب", "ابنه"),
        (34, 10, 3, "A mother", "her daughter", "الأم", "ابنتها"),
        (42, 12, 3, "An uncle", "his nephew", "العم", "ابن أخيه"),
        (30, 6, 4, "An older sister", "her little brother", "الأخت الكبرى", "أخيها الصغير"),
        (40, 12, 2, "A coach", "a young player", "المدرب", "اللاعب الناشئ"),
        (45, 9, 3, "An aunt", "her niece", "الخالة", "ابنة أختها"),
        (38, 10, 2, "A teacher", "a student", "المعلم", "الطالب"),
        (50, 14, 3, "A grandfather's youngest son", "his grandson", "الوالد", "الابن"),
        (32, 8, 3, "An older brother", "his younger brother", "الأخ الأكبر", "أخيه الأصغر"),
        (48, 12, 3, "A father", "his daughter", "الأب", "ابنته"),
    ]
    for a_old, a_yng, mult, p1_e, p2_e, p1_a, p2_a in age_cases:
        qid = next_id()
        diff = a_old - a_yng
        assert diff % (mult - 1) == 0
        target_yng = diff // (mult - 1)
        ans = target_yng - a_yng
        assert ans > 0
        q_en = (
            f"Today, {p1_e.lower()} is {m(a_old)} years old and {p2_e} is {m(a_yng)} years old. "
            f"In how many years from now will {p1_e.lower()} be **exactly {m(mult)} times** as old as {p2_e}?"
        )
        q_ar = (
            f"عمر {p1_a} اليوم {m(a_old)} سنة، وعمر {p2_a} هو {m(a_yng)} سنوات. "
            f"بعد كم سنة من الآن يصبح عمر {p1_a} مساويًا **لـ {m(mult)} أضعاف** عمر {p2_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [target_yng, ans + 2, max(1, ans - 2), ans + 4], qid
        )
        sol_en = explain_en(
            "Golden Rule of Age Problems: **The age difference between two people NEVER changes!** Every year, both grow older by 1 year.",
            [
                f"Find the constant age difference today: {m(f'{a_old} - {a_yng} = {diff}')} years.",
                f"When the older person is {m(mult)} times as old as the younger ({m(f'{mult}\\text{{ parts}}')} vs {m('1\\text{ part}')}), the age difference equals {m(f'{mult} - 1 = {mult - 1}')} part(s).",
                f"So {m(f'{mult - 1}')} part(s) = {m(diff)} years, meaning the younger person's future age (1 part) will be {m(f'{diff} \\div {mult - 1} = {target_yng}')} years.",
                f"Since the younger person is {m(a_yng)} today, this happens in {m(f'{target_yng} - {a_yng} = {ans}')} years!",
            ],
            f"Check in {m(ans)} years: their ages will be {m(a_old + ans)} and {m(a_yng + ans)}, and {m(f'{mult} \\times {a_yng + ans} = {a_old + ans}')}!",
        )
        sol_ar = explain_ar(
            "القاعدة الذهبية في مسائل الأعمار: **الفرق بين عمرَي شخصين يبقى ثابتًا دائمًا لا يتغير بمرور السنين!**",
            [
                f"نحسب فرق العمر الثابت بينهما اليوم: {m(f'{a_old} - {a_yng} = {diff}')} سنة.",
                f"عندما يصبح الأكبر {m(mult)} أضعاف الأصغر ({m(mult)} أجزاء مقابل جزء واحد)، فإن فرق العمر يمثل {m(f'{mult} - 1 = {mult - 1}')} أجزاء.",
                f"إذن عمر الأصغر في المستقبل (الجزء الواحد) يساوي {m(f'{diff} \\div {mult - 1} = {target_yng}')} سنة.",
                f"بما أن عمر الأصغر اليوم {m(a_yng)}، فإن عدد السنوات المتبقية هو {m(f'{target_yng} - {a_yng} = {ans}')} سنوات.",
            ],
            f"تحقق بعد {m(ans)} سنوات: يصبح العمران {m(a_old + ans)} و {m(a_yng + ans)}، وبالفعل {m(f'{mult} \\times {a_yng + ans} = {a_old + ans}')}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-age-difference-invariant",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Notice that the age gap ({a_old} - {a_yng} = {diff} years) stays the same forever!",
            f"تذكّر أن فرق العمر بينهما ({a_old} - {a_yng} = {diff} سنة) يبقى ثابتًا لا يتغير!",
            sol_en, sol_ar
        ))

    # 11. Catching-up / relative speed walking & cycling puzzles (10 variants)
    chase_cases = [
        (60, 100, 12, "Hassan", "his brother", "حسن", "أخوه"),      # head start 12*60=720 m, gap closes at 40 m/min => 18 min
        (50, 90, 8, "Noura", "her sister", "نورة", "أختها"),        # 400 / 40 = 10 min
        (80, 120, 10, "Saeed", "Fahad", "سعيد", "فهد"),             # 800 / 40 = 20 min
        (70, 105, 10, "Rami", "Kareem", "رامي", "كريم"),            # 700 / 35 = 20 min
        (60, 90, 15, "Yara", "Dina", "يارا", "دينا"),               # 900 / 30 = 30 min
        (75, 125, 8, "Adel", "Majed", "عادل", "ماجد"),              # 600 / 50 = 12 min
        (50, 75, 10, "Tala", "Reema", "تالا", "ريما"),              # 500 / 25 = 20 min
        (80, 100, 5, "Bilal", "Anas", "بلال", "أنس"),               # 400 / 20 = 20 min
        (65, 95, 6, "Lينا", "Sara", "لينا", "سارة"),                # fix en name below
        (90, 150, 10, "Waleed", "Hamza", "وليد", "حمزة"),           # 900 / 60 = 15 min
    ]
    chase_cases[8] = (65, 95, 6, "Lina", "Sara", "لينا", "سارة")
    for v1, v2, lead_min, p1_e, p2_e, p1_a, p2_a in chase_cases:
        qid = next_id()
        dist_lead = v1 * lead_min
        gap_rate = v2 - v1
        assert dist_lead % gap_rate == 0
        ans = dist_lead // gap_rate
        q_en = (
            f"{p1_e} leaves home walking along a straight park path at {m(v1)} meters per minute. "
            f"Exactly {m(lead_min)} minutes later, {p2_e} leaves the **same** home along the **same** path cycling slowly at {m(v2)} meters per minute. "
            f"How many minutes after {p2_e} starts will {p2_e} catch up to {p1_e}?"
        )
        q_ar = (
            f"غادر/غادرت {p1_a} المنزل ماشيًا في مسار مستقيم بسرعة ثابتة قدرها {m(v1)} مترًا في الدقيقة. "
            f"وبعد {m(lead_min)} دقائق بالضبط، انطلق/انطلقت {p2_a} من **المنزل نفسه** وعلى **المسار نفسه** بسرعة {m(v2)} مترًا في الدقيقة. "
            f"بعد كم دقيقة من انطلاق {p2_a} سيلحق بـ {p1_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + lead_min, max(2, ans - 4), ans + 5, dist_lead // v2 + 1], qid
        )
        sol_en = explain_en(
            "Break catch-up problems into two easy questions: **(1) How big is the head start?** and **(2) How many meters closer do they get each minute?**",
            [
                f"**Head start distance:** In {m(lead_min)} minutes at {m(v1)} m/min, {p1_e} gets {m(f'{lead_min} \\times {v1} = {dist_lead}')} meters ahead.",
                f"**Catch-up speed:** Each minute, {p2_e} moves {m(v2)} m while {p1_e} moves {m(v1)} m, so the gap shrinks by {m(f'{v2} - {v1} = {gap_rate}')} meters per minute.",
                f"**Time to close the gap:** Divide the head start by the catch-up rate: {m(f'{dist_lead} \\div {gap_rate} = {ans}')} minutes.",
            ],
            f"Distance check after {m(ans)} minutes of {p2_e} moving: {p2_e} travels {m(f'{ans} \\times {v2} = {ans*v2}')} m, and {p1_e} travels {m(f'({lead_min}+{ans}) \\times {v1} = {(lead_min+ans)*v1}')} m — exact same spot!",
        )
        sol_ar = explain_ar(
            "نحل مسائل اللحاق بخطوتين واضحتين: **(1) كم المسافة التي سبق بها الأول؟** ثم **(2) بكم مترًا تتقلص المسافة بينهما في كل دقيقة؟**",
            [
                f"**مسافة التقدّم المبدئية:** خلال {m(lead_min)} دقائق بسرعة {m(v1)} م/د، قطع {p1_a} مسافة {m(f'{lead_min} \\times {v1} = {dist_lead}')} مترًا.",
                f"**سرعة تقليص الفجوة:** في كل دقيقة يقطع {p2_a} مسافة {m(v2)} م ويقطع {p1_a} مسافة {m(v1)} م، فيقترب منه بمقدار {m(f'{v2} - {v1} = {gap_rate}')} مترًا في الدقيقة.",
                f"**زمن اللحاق:** نقسم المسافة الفاصلة على معدل الاقتراب: {m(f'{dist_lead} \\div {gap_rate} = {ans}')} دقيقة.",
            ],
            f"تحقق من المسافة: خلال {m(ans)} دقيقة يقطع {p2_a} مسافة {m(ans*v2)} م، ويكون {p1_a} قد مشى {m(lead_min + ans)} دقيقة فقطع {m((lead_min+ans)*v1)} م أيضًا!",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Algebra", "Medium", "g67-catch-up-chase",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"First multiply {lead_min} × {v1} to find the head-start gap, then divide by ({v2} - {v1}).",
            f"اضرب {lead_min} × {v1} أولًا لإيجاد المسافة الفاصلة، ثم اقسمها على فرق السرعتين ({v2} - {v1}).",
            sol_en, sol_ar
        ))

    assert len(items) == 110, f"Expected 110 items, got {len(items)}"
    return items


if __name__ == "__main__":
    qs = generate_t1_algebra()
    print(f"Generated {len(qs)} Track 1 Algebra questions cleanly.")
