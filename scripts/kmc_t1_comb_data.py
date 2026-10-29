"""KAUST Mathematics Competition (KMC) — Track 1: Grades 6-7
Pillar 4: Combinatorics, Logic, Cube Folding, Spinners & Data Analysis (110 questions).
Strictly aligned with official KMC Grades 6-7 syllabus (no calculators).
"""
from fractions import Fraction
import math
from kmc_common import (
    m, explain_en, explain_ar, make_5_math_options, make_5_bilingual_options, make_kmc_question
)
from kmc_diagrams import (
    svg_subdivided_apex_triangle,
    svg_cube_net,
    svg_spinner,
    svg_bar_chart,
)

LEVEL = "Track 1: Grades 6-7"


def generate_t1_comb_data() -> list[dict]:
    items = []
    idx = 1

    def next_id():
        nonlocal idx
        qid = f"KAUST-G67-C{idx:03d}"
        idx += 1
        return qid

    # 1. Counting ALL triangles in subdivided apex figure (10 variants with KMC triangle SVG!) — KMC G6-7 Sample Q8
    # n_base_parts = b => b+1 rays from apex => C(b+1, 2) = b*(b+1)//2 ways to pick 2 rays, times n_levels horizontal bases!
    tri_cnt_cases = [
        (3, 2),  # 6 * 2 = 12 (exact KMC Sample Q8!)
        (2, 2),  # 3 * 2 = 6
        (3, 1),  # 6 * 1 = 6
        (4, 1),  # 10 * 1 = 10
        (4, 2),  # 10 * 2 = 20
        (2, 3),  # 3 * 3 = 9
        (3, 3),  # 6 * 3 = 18
        (5, 1),  # 15 * 1 = 15
        (4, 3),  # 10 * 3 = 30
        (5, 2),  # 15 * 2 = 30
    ]
    for nb, nlv in tri_cnt_cases:
        qid = next_id()
        per_lv = nb * (nb + 1) // 2
        ans = per_lv * nlv
        svg = svg_subdivided_apex_triangle(nb, nlv)
        q_en = (
            f"In the figure shown, {m(nb - 1)} interior segments are drawn from the top vertex to the base "
            f"(splitting the base into {m(nb)} parts)"
            + (f", and {m(nlv - 1)} horizontal line(s) cut across all of them." if nlv > 1 else ".")
            + " How many triangles **of all sizes** are there in the figure?"
        )
        q_ar = (
            f"في الشكل الموضّح، رُسمت {m(nb - 1)} قطع مستقيمة داخلية من الرأس العلوي إلى القاعدة "
            f"(فقسّمت القاعدة إلى {m(nb)} أجزاء)"
            + (f"، كما قطعها {m(nlv - 1)} مستقيم أفقي." if nlv > 1 else ".")
            + " كم مثلثًا **(بجميع الأحجام)** يوجد في الشكل؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [nb * nlv, per_lv if per_lv != ans else ans + 2, ans - nb, ans + nb, ans + 4], qid
        )
        sum_parts = " + ".join(str(k) for k in range(nb, 0, -1))
        sol_en = explain_en(
            "Don't just count the tiny single-slice triangles! **Every triangle in this figure shares the top vertex**, and can combine 1, 2, 3, ... adjacent slices side-by-side!",
            [
                f"**Count triangles on ONE horizontal base first:** With {m(nb)} base slices, there are {m(nb)} single-slice triangles, {m(nb-1)} two-slice triangles, ..., down to {m(1)} full-width triangle: {m(f'{sum_parts} = {per_lv}')} triangles per horizontal line.",
                (
                    f"**Multiply by the {m(nlv)} horizontal base levels** (including the bottom base and {m(nlv-1)} upper cross-line(s)): {m(f'{per_lv} \\times {nlv} = {ans}')} triangles altogether!"
                    if nlv > 1 else
                    f"Since there is only {m(1)} horizontal base line, the total number of triangles is {m(ans)}."
                ),
            ],
            f"Common trap: counting only the {m(nb * nlv)} smallest pieces misses the wider combined triangles!",
        )
        sol_ar = explain_ar(
            "لا تعدّ المثلثات الصغيرة المنفردة فقط! **كل مثلث في الشكل رأسه في الأعلى** ويمكن أن يتكون من شريحة واحدة أو شريحتين متجاورتين أو أكثر!",
            [
                f"**نعدّ المثلثات فوق خط أفقي واحد أولًا:** مع وجود {m(nb)} شرائح، لدينا {m(f'{sum_parts} = {per_lv}')} مثلثات فوق كل خط أفقي.",
                (
                    f"**نضرب في عدد الخطوط الأفقية ({m(nlv)})** لأن كل خط أفقي يصلح قاعدة لنفس العدد من المثلثات: {m(f'{per_lv} \\times {nlv} = {ans}')} مثلثًا."
                    if nlv > 1 else
                    f"وبما أنه يوجد خط قاعدة أفقي واحد فقط، فإن إجمالي عدد المثلثات هو {m(ans)}."
                ),
            ],
            f"تجنّب الخطأ الشائع بالاكتفاء بـ {m(nb * nlv)} قطعة صغيرة؛ فالمثلثات المدمجة ترفع العدد إلى {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "g67-count-subdivided-triangles",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"First count all triangles (1-slice, 2-slice, ...) using the bottom base ({sum_parts}), then multiply by the number of horizontal lines!",
            f"عدّ أولًا جميع المثلثات (من شريحة، شريحتين، ...) على القاعدة السفلية ({sum_parts})، ثم اضرب في عدد الخطوط الأفقية!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 2. Flattened 6-square cube nets — opposite face when folded (10 variants with KMC cube-net SVG!) — Practice Set 1 Q5
    # Standard nets where opposite pairs are exact:
    # Net A (cross): (1,0)=T, (0,1)=L, (1,1)=Base, (2,1)=R, (3,1)=TopLid, (1,2)=B -> opposites: (T,B), (L,R), (Base,TopLid)
    # Net B (T-net): (0,0)=A, (1,0)=B, (2,0)=C, (1,1)=D, (1,2)=E, (1,3)=F -> opposites: (A,C), (B,E), (D,F)
    # Net C (Z/step): (0,0)=A, (1,0)=B, (1,1)=C, (2,1)=D, (2,2)=E, (3,2)=F -> opposites: (A,D), (B,E), (C,F)
    net_cases = [
        ([(1,0,"1"),(0,1,"2"),(1,1,"3"),(2,1,"4"),(3,1,"5"),(1,2,"6")], "2", "4", ["1","3","4","5","6"]),
        ([(1,0,"1"),(0,1,"2"),(1,1,"3"),(2,1,"4"),(3,1,"5"),(1,2,"6")], "3", "5", ["1","2","4","5","6"]),
        ([(1,0,"A"),(0,1,"B"),(1,1,"C"),(2,1,"D"),(3,1,"E"),(1,2,"F")], "A", "F", ["B","C","D","E","F"]),
        ([(0,0,"1"),(1,0,"2"),(2,0,"3"),(1,1,"4"),(1,2,"5"),(1,3,"6")], "2", "5", ["1","3","4","5","6"]),
        ([(0,0,"1"),(1,0,"2"),(2,0,"3"),(1,1,"4"),(1,2,"5"),(1,3,"6")], "4", "6", ["1","2","3","5","6"]),
        ([(0,0,"K"),(1,0,"A"),(1,1,"U"),(2,1,"S"),(2,2,"T"),(3,2,"M")], "K", "S", ["A","U","S","T","M"]),
        ([(0,0,"K"),(1,0,"A"),(1,1,"U"),(2,1,"S"),(2,2,"T"),(3,2,"M")], "A", "T", ["K","U","S","T","M"]),
        ([(0,0,"1"),(1,0,"2"),(1,1,"3"),(2,1,"4"),(2,2,"5"),(3,2,"6")], "3", "6", ["1","2","4","5","6"]),
        ([(0,0,"P"),(0,1,"Q"),(1,1,"R"),(2,1,"S"),(3,1,"T"),(2,2,"U")], "P", "U", ["Q","R","S","T","U"]),
        ([(0,0,"P"),(0,1,"Q"),(1,1,"R"),(2,1,"S"),(3,1,"T"),(2,2,"U")], "R", "T", ["P","Q","S","T","U"]),
    ]
    for cells_lbl, ask_f, opp_f, five_choices in net_cases:
        qid = next_id()
        svg = svg_cube_net(cells_lbl)
        c_orig = five_choices.index(opp_f)
        pairs = [(m(ch) if ch.isdigit() else ch, m(ch) if ch.isdigit() else ch) for ch in five_choices]
        opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, c_orig, qid)
        f_disp = m(ask_f) if ask_f.isdigit() else f"**{ask_f}**"
        o_disp = m(opp_f) if opp_f.isdigit() else f"**{opp_f}**"
        pos_str = ", ".join(f"{lbl}({c},{r})" for c, r, lbl in cells_lbl)
        q_en = (
            f"The figure shows a flattened net of {m(6)} squares at grid positions {m(pos_str)} that folds into a closed cube. "
            f"When folded into a cube, which face lies **directly opposite** the face marked {f_disp}?"
        )
        q_ar = (
            f"يبيّن الشكل شبكة مسطّحة مكوّنة من {m(6)} مربعات في المواقع {m(pos_str)} تُطوى لتكوّن مكعبًا مغلقًا. "
            f"عند طيّ الشبكة، أيُّ وجه سيقع **مقابلًا تمامًا** للوجه المكتوب عليه {f_disp}؟"
        )
        sol_en = explain_en(
            "Cube-Net Shortcut: **1) Along any straight strip of 3 squares, the two end squares (skipping 1 square between them) ALWAYS fold to opposite faces!** **2) An 'Z-knight' step (1 over, 2 along) also lands on the opposite face!**",
            [
                f"Pick one central square in the net as the **flat floor (base)** of the cube and fold its immediate neighbors straight up by {m('90^\\circ')} to become the vertical walls.",
                f"Notice that two faces sharing an edge or folding to touch at a corner are *adjacent*, never opposite.",
                f"Following the 'skip-one-square' folding rule from {f_disp}, the face that lands parallel and directly across from {f_disp} is {o_disp}!",
            ],
            f"Mental fold check: if {f_disp} sits on the bottom, {o_disp} folds over two {m('90^\\circ')} creases ({m('180^\\circ')} total) to become the top lid!",
        )
        sol_ar = explain_ar(
            "قاعدة طيّ شبكة المكعب السريعة: **في أي صف أو عمود مستقيم من 3 مربعات، المربعان الطرفيان (بينهما مربع واحد فاصل) يتقابلان دائمًا بعد الطي!**",
            [
                f"نثبّت أحد المربعات الوسطى ليكون **قاعدة المكعب**، ثم نطوي المربعات المجاورة له بزاوية قائمة ({m('90^\\circ')}) لتصبح الجدران الأربعة.",
                f"أي مربعين يشتركان في ضلع واحد يصبحان متجاورين متعامدين لا متقابلين.",
                f"بتتبع الطيّ بمقدار طيّتين قائمتين ({m('180^\\circ')}) بدءًا من الوجه {f_disp}، نجد أن الوجه الموازي والمقابل له تمامًا هو {o_disp}.",
            ],
            f"تحقق ذهني: لو جعلنا الوجه {f_disp} في الأسفل، سينطوي الوجه {o_disp} ليصبح السقف العلوي المقابل له مباشرة.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "g67-cube-net-opposite",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "In a straight row of 3 squares on a cube net, the 1st and 3rd squares always fold to opposite faces! Pick a base square and fold its walls up.",
            "في أي صف مستقيم من 3 مربعات في شبكة المكعب، يتقابل المربع الأول والثالث دائمًا بعد الطي! اختر مربعًا كقاعدة واطوِ الجدران حوله.",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 3. Spinner sector area probability (10 variants with KMC spinner SVG!) — KMC G6-7 Sample Q14
    spinner_cases = [
        ([(0.5, "1"), (0.25, "2"), (0.125, "3"), (0.125, "4")], "an **even** number", "عدد **زوجي**", "37.5\\%", ["50\\%", "25\\%", "62.5\\%", "75\\%"],
         "2 (quarter = 2/8) and 4 (eighth = 1/8), summing to 3/8 = 37.5%", "العددان الزوجيان هما 2 (ربع = 2/8) و 4 (ثُمن = 1/8)، ومجموعهما 3/8 = 37.5%"),
        ([(0.5, "1"), (0.25, "2"), (0.125, "3"), (0.125, "4")], "an **odd** number", "عدد **فردي**", "62.5\\%", ["50\\%", "75\\%", "37.5\\%", "25\\%"],
         "1 (half = 4/8) and 3 (eighth = 1/8), summing to 5/8 = 62.5%", "العددان الفرديان هما 1 (نصف = 4/8) و 3 (ثُمن = 1/8)، ومجموعهما 5/8 = 62.5%"),
        ([(0.5, "2"), (0.25, "3"), (0.25, "5")], "a **prime** number", "عدد **أولي**", "1", ["\\frac{3}{4}", "\\frac{1}{2}", "\\frac{2}{3}", "\\frac{1}{4}"],
         "2, 3, and 5 are ALL prime numbers (remember 2 is the smallest prime!), covering the whole disc = 1", "الأعداد 2 و 3 و 5 كلها أعداد أولية (تذكّر أن 2 عدد أولي!)، فتغطي القرص كاملًا = 1"),
        ([(0.5, "3"), (0.25, "4"), (0.125, "5"), (0.125, "6")], "a number **greater than 3**", "عدد **أكبر من 3**", "\\frac{1}{2}", ["\\frac{3}{4}", "\\frac{3}{8}", "\\frac{5}{8}", "\\frac{1}{4}"],
         "sectors 4 (1/4), 5 (1/8), and 6 (1/8) make up everything except sector 3 (1/2), giving 1 - 1/2 = 1/2", "الأعداد الأكبر من 3 هي 4 و 5 و 6 وتغطي النصف المتبقي من القرص أي 1/2"),
        ([(0.25, "1"), (0.25, "2"), (0.25, "3"), (0.125, "4"), (0.125, "5")], "an **even** number", "عدد **زوجي**", "\\frac{3}{8}", ["\\frac{2}{5}", "\\frac{1}{2}", "\\frac{1}{4}", "\\frac{5}{8}"],
         "even sectors are 2 (1/4 = 2/8) and 4 (1/8), giving 2/8 + 1/8 = 3/8", "الأعداد الزوجية هي 2 (ربع = 2/8) و 4 (ثُمن = 1/8)، والمجموع 3/8"),
        ([(1/3, "2"), (1/3, "3"), (1/6, "4"), (1/6, "6")], "an **even** number", "عدد **زوجي**", "\\frac{2}{3}", ["\\frac{3}{4}", "\\frac{1}{2}", "\\frac{5}{6}", "\\frac{1}{3}"],
         "even sectors are 2 (1/3 = 2/6), 4 (1/6), and 6 (1/6), summing to 4/6 = 2/3", "الأعداد الزوجية هي 2 (ثلث = 2/6) و 4 (سُدس) و 6 (سُدس)، ومجموعها 4/6 = 2/3"),
        ([(1/2, "5"), (1/6, "2"), (1/6, "4"), (1/6, "7")], "an **odd** number", "عدد **فردي**", "\\frac{2}{3}", ["\\frac{1}{2}", "\\frac{3}{4}", "\\frac{5}{6}", "\\frac{1}{3}"],
         "odd sectors are 5 (1/2 = 3/6) and 7 (1/6), summing to 4/6 = 2/3", "العددان الفرديان هما 5 (نصف = 3/6) و 7 (سُدس = 1/6)، ومجموعهما 4/6 = 2/3"),
        ([(0.25, "3"), (0.5, "6"), (0.125, "7"), (0.125, "8")], "a **multiple of 3**", "**مضاعف للعدد 3**", "75\\%", ["50\\%", "62.5\\%", "25\\%", "87.5\\%"],
         "multiples of 3 are 3 (25%) and 6 (50%), summing to 25% + 50% = 75%", "مضاعفات 3 هي 3 (ربع = 25%) و 6 (نصف = 50%)، ومجموعهما 75%"),
        ([(0.5, "1"), (0.25, "4"), (0.125, "9"), (0.125, "6")], "a **perfect square** (1, 4, or 9)", "**مربع كامل** (1 أو 4 أو 9)", "\\frac{7}{8}", ["\\frac{3}{4}", "\\frac{5}{8}", "\\frac{1}{2}", "\\frac{3}{5}"],
         "1 (4/8), 4 (2/8), and 9 (1/8) are all perfect squares, leaving only 6 (1/8) out: 1 - 1/8 = 7/8", "الأعداد 1 (4/8) و 4 (2/8) و 9 (1/8) كلها مربعات كاملة، ومجموعها 7/8"),
        ([(0.5, "10"), (0.25, "15"), (0.125, "20"), (0.125, "22")], "a **multiple of 10**", "**مضاعف للعدد 10**", "62.5\\%", ["50\\%", "75\\%", "37.5\\%", "25\\%"],
         "multiples of 10 are 10 (half = 50%) and 20 (eighth = 12.5%), giving 50% + 12.5% = 62.5%", "مضاعفات 10 هي 10 (50%) و 20 (12.5%)، ومجموعهما 62.5%"),
    ]
    desc_fractions_en = {0.5: "1/2", 0.25: "1/4", 0.125: "1/8", round(1/3, 4): "1/3", round(1/6, 4): "1/6"}
    for sectors, cond_e, cond_a, ans_tex, dist_tex, reason_e, reason_a in spinner_cases:
        qid = next_id()
        svg = svg_spinner(sectors)
        sec_list_e = ", ".join(f"sector {lbl} covers {m(desc_fractions_en[round(f,4)])}" for f, lbl in sectors)
        sec_list_a = "، ".join(f"القطاع {lbl} يمثّل {m(desc_fractions_en[round(f,4)])}" for f, lbl in sectors)
        q_en = (
            f"A fair circular spinner is divided into sectors of different sizes as shown ({sec_list_e} of the disc). "
            f"When spun once, what is the probability that the pointer stops on {cond_e}?"
        )
        q_ar = (
            f"قُسِّم قرص دوّار منتظم إلى قطاعات مختلفة المساحة كما في الشكل ({sec_list_a} من القرص). "
            f"عند تدوير المؤشر مرة واحدة، ما احتمال أن يتوقف عند {cond_a}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(ans_tex, dist_tex, qid)
        sol_en = explain_en(
            "Important Spinner Rule: **Probability depends on the AREA (fraction of the circle) of each sector**, NOT just on counting how many sectors match!",
            [
                f"List the sectors that satisfy '{cond_e}' and write each one's fraction of the full circle.",
                f"Here: {reason_e}.",
                f"Combine those fractions using a common denominator to get the exact probability: {m(ans_tex)}.",
            ],
            f"Trap alert: counting sectors equally would fail because bigger sectors are landed on more often!",
        )
        sol_ar = explain_ar(
            "قاعدة مهمة في القرص الدوّار: **الاحتمال يعتمد على مساحة كل قطاع (كسوره من الدائرة)**، وليس على مجرد عدّ الأرقام لأن القطاعات غير متساوية المساحة!",
            [
                f"نحدّد القطاعات التي تحقق الشرط ({cond_a}) ونكتب الكسر الذي يمثّله كل قطاع.",
                f"تفصيل الحل: {reason_a}.",
                f"بتوحيد المقامات وجمع المساحات المطلوبة نحصل على الاحتمال {m(ans_tex)}.",
            ],
            f"تجنّب قسمة عدد القطاعات على العدد الكلي لأن مساحات القطاعات متفاوتة.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Data & Probability", "Medium", "g67-spinner-area-prob",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Add the fractions of the circle covered by the matching sectors — don't treat unequal sectors as equal!",
            "اجمع كسور الدائرة التي تغطيها القطاعات المطلوبة، ولا تعامل القطاعات المختلفة المساحة وكأنها متساوية!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 4. Bar chart with missing '?' bar given average (10 variants with KMC bar chart SVG!) — Practice Set 2 Q1
    bar_cases = [
        ([12, 18, 14, None, 21], 16, ["Sun", "Mon", "Tue", "Wed", "Thu"], "books borrowed from the library", "الكتب المستعارة من المكتبة"),
        ([10, 15, None, 19, 14], 15, ["Sun", "Mon", "Tue", "Wed", "Thu"], "cups of juice sold", "أكواب العصير المباعة"),
        ([8, None, 14, 10, 16], 12, ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"], "math puzzles solved", "الألغاز المحلولة"),
        ([20, 14, 18, None], 17, ["W1", "W2", "W3", "W4"], "trees planted each week", "الأشجار المزروعة أسبوعيًا"),
        ([15, 22, None, 19, 24], 20, ["Sun", "Mon", "Tue", "Wed", "Thu"], "visitors to the science club", "زوار النادي العلمي"),
        ([9, 13, 11, None, 17], 13, ["G6A", "G6B", "G6C", "G7A", "G7B"], "students in the honor roll", "طلاب لوحة الشرف"),
        ([16, None, 24, 20], 19, ["Q1", "Q2", "Q3", "Q4"], "points scored per quarter", "النقاط المسجّلة في كل ربع"),
        ([11, 17, 13, 19, None], 15, ["Sun", "Mon", "Tue", "Wed", "Thu"], "notebooks sold", "الدفاتر المباعة"),
        ([25, 18, None, 22, 30], 23, ["D1", "D2", "D3", "D4", "D5"], "laps swum", "الأشواط المقطوعة سباحة"),
        ([14, 10, 18, None, 16], 14, ["Mon", "Tue", "Wed", "Thu", "Fri"], "boxes packed", "الصناديق المعبّأة"),
    ]
    for vals, mean_v, x_lbls, ctx_e, ctx_a in bar_cases:
        qid = next_id()
        n_b = len(vals)
        tot_needed = n_b * mean_v
        known = [v for v in vals if v is not None]
        known_sum = sum(known)
        ans = tot_needed - known_sum
        assert ans > 0
        bars_arg = [
            (xl, (v if v is not None else ans), (str(v) if v is not None else "?"))
            for xl, v in zip(x_lbls, vals)
        ]
        svg = svg_bar_chart(bars_arg)
        q_en = (
            f"The bar chart shows the number of {ctx_e} across {m(n_b)} entries, where one bar is missing its value ({m('?')}). "
            f"If the **mean (average)** across all {m(n_b)} entries is {m(mean_v)}, what value belongs on the bar marked {m('?')}?"
        )
        q_ar = (
            f"يبيّن التمثيل بالأعمدة عدد {ctx_a} في {m(n_b)} فترات، مع وجود عمود واحد قيمته مجهولة ({m('?')}). "
            f"إذا كان **المتوسط الحسابي** لجميع الفترات الـ {m(n_b)} يساوي {m(mean_v)}، فما القيمة المفقودة المشار إليها بـ {m('?')}؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [mean_v if mean_v != ans else ans + 3, ans + 2, max(1, ans - 2), ans + 4, ans - 3 if ans > 4 else ans + 5], qid
        )
        known_str = " + ".join(map(str, known))
        sol_en = explain_en(
            "Remember the golden formula for averages: **Total Sum = Average × Number of Bars**!",
            [
                f"**Find the required Total Sum:** Multiply the average {m(mean_v)} by the {m(n_b)} bars: {m(f'{mean_v} \\times {n_b} = {tot_needed}')}.",
                f"**Add the {m(n_b - 1)} known bars:** {m(f'{known_str} = {known_sum}')}.",
                f"**Subtract to uncover the missing bar:** {m(f'{tot_needed} - {known_sum} = {ans}')}.",
            ],
            f"Check: {m(f'({known_sum} + {ans}) \\div {n_b} = {tot_needed} \\div {n_b} = {mean_v}')}!",
        )
        sol_ar = explain_ar(
            "تذكّر العلاقة الأساسية للمتوسط الحسابي: **المجموع الكلي = المتوسط × عدد الأعمدة**!",
            [
                f"**نحسب المجموع الكلي المطلوب:** نضرب المتوسط {m(mean_v)} في عدد الأعمدة {m(n_b)}: {m(f'{mean_v} \\times {n_b} = {tot_needed}')}.",
                f"**نجمع القيم المعلومة:** {m(f'{known_str} = {known_sum}')}.",
                f"**نطرح لإيجاد القيمة المجهولة:** {m(f'{tot_needed} - {known_sum} = {ans}')}.",
            ],
            f"تحقق: {m(f'({known_sum} + {ans}) \\div {n_b} = {mean_v}')} بالضبط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Data & Probability", "Easy", "g67-barchart-missing-mean",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Multiply the mean ({mean_v}) by {n_b} to get the total of all bars, then subtract the known bars!",
            f"اضرب المتوسط ({mean_v}) في {n_b} لإيجاد المجموع الكلي لجميع الأعمدة، ثم اطرح مجموع الأعمدة المعلومة!",
            sol_en, sol_ar, diagram_en=svg
        ))

    # 5. Weighted / combined group averages (10 variants) — KMC G6-7 Sample Q12
    wmean_cases = [
        (20, 70, 5, 80),    # (1400 + 400)/25 = 72
        (15, 76, 5, 88),    # (1140 + 440)/20 = 79
        (12, 80, 8, 90),    # (960 + 720)/20 = 84
        (18, 65, 6, 85),    # (1170 + 510)/24 = 70
        (10, 82, 15, 92),   # (820 + 1380)/25 = 88
        (24, 75, 6, 90),    # (1800 + 540)/30 = 78
        (16, 70, 4, 95),    # (1120 + 380)/20 = 75
        (14, 84, 7, 75),    # (1176 + 525)/21 = 81
        (21, 80, 9, 70),    # (1680 + 630)/30 = 77
        (12, 68, 4, 84),    # (816 + 336)/16 = 72
    ]
    for n1, m1, n2, m2 in wmean_cases:
        qid = next_id()
        s1, s2 = n1 * m1, n2 * m2
        ntot = n1 + n2
        assert (s1 + s2) % ntot == 0
        ans = (s1 + s2) // ntot
        naive_avg = (m1 + m2) // 2 if (m1 + m2) % 2 == 0 else m1 + 3
        q_en = (
            f"The mean (average) score of {m(n1)} students on a math quiz is {m(m1)}. "
            f"Then {m(n2)} more students, whose mean score is {m(m2)}, join the group. "
            f"What is the overall mean score of all {m(ntot)} students?"
        )
        q_ar = (
            f"متوسط درجات {m(n1)} طالبًا في اختبار رياضيات هو {m(m1)}، ثم انضمّ إليهم {m(n2)} طلاب متوسط درجاتهم {m(m2)}. "
            f"ما المتوسط الحسابي لدرجات جميع الطلاب البالغ عددهم {m(ntot)} طالبًا؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [naive_avg if naive_avg != ans else ans + 2, ans + 1, ans - 1, ans + 3], qid
        )
        sol_en = explain_en(
            "Never just average the two averages (`(m₁ + m₂) ÷ 2`) when the two groups have **different sizes**! Always find the **total points** of each group first!",
            [
                f"**Total points of the first {m(n1)} students:** {m(f'{n1} \\times {m1} = {s1}')}.",
                f"**Total points of the {m(n2)} new students:** {m(f'{n2} \\times {m2} = {s2}')}.",
                f"**Combined total divided by all {m(ntot)} students:** {m(f'({s1} + {s2}) \\div {ntot} = {s1 + s2} \\div {ntot} = {ans}')}.",
            ],
            f"Notice {m(ans)} sits closer to {m(m1 if n1 > n2 else m2)} because that group has more students ({m(max(n1, n2))} vs {m(min(n1, n2))})!",
        )
        sol_ar = explain_ar(
            "احذر من جمع المتوسطين وقسمتهما على 2 مباشرة لأن **عدد طلاب المجموعتين مختلف**! يجب حساب **مجموع الدرجات** لكل مجموعة أولًا.",
            [
                f"**مجموع درجات المجموعة الأولى ({m(n1)} طالبًا):** {m(f'{n1} \\times {m1} = {s1}')}.",
                f"**مجموع درجات المجموعة الثانية ({m(n2)} طلاب):** {m(f'{n2} \\times {m2} = {s2}')}.",
                f"**المتوسط الكلي للـ {m(ntot)} طالبًا:** نقسم المجموع الكلي على العدد الكلي: {m(f'({s1} + {s2}) \\div {ntot} = {s1 + s2} \\div {ntot} = {ans}')}.",
            ],
            f"منطقيًا، المتوسط الكلي {m(ans)} أقرب إلى متوسط المجموعة الأكبر عددًا!",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Data & Probability", "Easy", "g67-combined-group-mean",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the total score of the {n1} students and the total score of the {n2} students, add them, and divide by {ntot}.",
            f"احسب مجموع درجات الـ {n1} طالبًا ومجموع درجات الـ {n2} طلاب، ثم اجمعهما واقسم على {ntot}.",
            sol_en, sol_ar
        ))

    # 6. Selfie / club-team double-counting squeeze (10 variants) — KMC G6-7 Sample Q23
    # F friends; each appears lo or hi times; each photo has K friends -> lo*F <= K*P <= hi*F with UNIQUE multiple of K strictly inside (or uniquely achievable)!
    squeeze_cases = [
        (8, 2, 3, 5, 4, "Eman", "selfies with her friends", "friends", "إيمان", "صورة مع صديقاتها", "صديقات"), # 16..24, mult of 5: 20 -> P=4
        (9, 2, 3, 7, 3, "Noura", "group photos", "classmates", "نورة", "صورة جماعية", "زميلات"),             # 18..27, mult of 7: 21 -> P=3
        (10, 2, 3, 7, 4, "Tariq", "team rounds", "players", "طارق", "جولة تدريبية", "لاعبين"),               # 20..30, mult of 7: 21 or 28 -> wait! 21 & 28 both in 20..30! Let's assert UNIQUE multiple!
        (7, 2, 3, 5, 4, "Salma", "club sessions", "members", "سلمى", "جلسة نشاط", "عضوات"),                  # 14..21, mult of 5: 15,20 -> wait! Let's check exact uniqueness!
        (8, 3, 4, 7, 4, "Rayan", "debate panels", "students", "ريان", "حلقة نقاش", "طلاب"),                  # 24..32, mult of 7: 28 ONLY! -> P=4!
        (6, 3, 4, 5, 4, "Lina", "lab groups", "partners", "لينا", "مجموعة مختبر", "زميلات"),                 # 18..24, mult of 5: 20 ONLY! -> P=4!
        (10, 3, 4, 9, 4, "Omar", "matches", "teammates", "عمر", "مباراة مصغّرة", "زملاء"),                   # 30..40, mult of 9: 36 ONLY! -> P=4!
        (9, 3, 4, 8, 4, "Maha", "art tables", "friends", "مها", "طاولة رسم", "صديقات"),                      # 27..36, mult of 8: 32 ONLY! -> P=4!
        (7, 3, 4, 5, 5, "Faisal", "coding sprints", "peers", "فيصل", "فريق برمجة", "زملاء"),                 # 21..28, mult of 5: 25 ONLY! -> P=5!
        (11, 2, 3, 8, 3, "Huda", "reading circles", "students", "هدى", "حلقة قراءة", "طالبات"),              # 22..33, mult of 8: 24,32 -> let's adjust!
    ]
    # Replace non-unique ones with 100% strictly unique multiples!
    squeeze_cases[2] = (7, 2, 3, 6, 3, "Tariq", "team rounds", "players", "طارق", "جولة تدريبية", "لاعبين")     # 14..21, mult of 6: 18 ONLY! -> P=3!
    squeeze_cases[3] = (10, 2, 3, 9, 3, "Salma", "club sessions", "members", "سلمى", "جلسة نشاط", "عضوات")     # 20..30, mult of 9: 27 ONLY! -> P=3!
    squeeze_cases[9] = (11, 2, 3, 9, 3, "Huda", "reading circles", "students", "هدى", "حلقة قراءة", "طالبات")  # 22..33, mult of 9: 27 ONLY! -> P=3!
    for F, lo_c, hi_c, K, ans, nm_e, ev_e, peop_e, nm_a, ev_a, peop_a in squeeze_cases:
        qid = next_id()
        lo_tot, hi_tot = F * lo_c, F * hi_c
        mults = [p for p in range(1, 50) if lo_tot <= K * p <= hi_tot]
        assert mults == [ans], (F, lo_c, hi_c, K, mults)
        q_en = (
            f"{nm_e} organized several {ev_e} with {m(F)} {peop_e}. "
            f"Each of the {m(F)} {peop_e} participated in **either {m(lo_c)} or {m(hi_c)}** of them, "
            f"and every single one had **exactly {m(K)}** of those {peop_e}. "
            f"How many {ev_e} were there in total?"
        )
        q_ar = (
            f"نظّم/نظّمت {nm_a} عددًا من ({ev_a}) بمشاركة {m(F)} من الـ{peop_a}. "
            f"ظهر كل واحد من الـ {m(F)} في **{m(lo_c)} أو {m(hi_c)}** منها، "
            f"وفي كل واحدة منها شارك **{m(K)} بالضبط** من هؤلاء الـ{peop_a}. "
            f"كم كان العدد الكلي لـ ({ev_a})؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans - 1, ans + 1, ans + 2, ans + 3], qid
        )
        sol_en = explain_en(
            "Count **total appearances** in two ways! If there are `p` groups of `K` people each, the total number of appearances is `K × p` (a multiple of `K`), AND it must lie between the minimum and maximum possible appearances of the `F` people!",
            [
                f"**Method 1 (by groups):** Let {m('p')} be the number of {ev_e}. Since each has {m(K)} {peop_e}, total appearances {m(f'= {K}p')} (must be a multiple of {m(K)}!).",
                f"**Method 2 (by individuals):** If all {m(F)} appeared {m(lo_c)} times, total = {m(f'{F}\\times{lo_c}={lo_tot}')}; if all appeared {m(hi_c)} times, total = {m(f'{F}\\times{hi_c}={hi_tot}')}. So {m(f'{lo_tot} \\le {K}p \\le {hi_tot}')}.",
                f"**Spot the unique multiple of {m(K)}:** Between {m(lo_tot)} and {m(hi_tot)}, the **only** multiple of {m(K)} is {m(K * ans)}, so {m(f'{K}p = {K*ans}')} and {m(f'p = {ans}')}!",
            ],
            f"Check: {m(K * ans)} total appearances across {m(F)} people means {m(hi_tot - K*ans)} people appear {m(lo_c)} times and {m(K*ans - lo_tot)} appear {m(hi_c)} times — works cleanly!",
        )
        sol_ar = explain_ar(
            "نحسب **إجمالي مرات الظهور بطريقتين**! إذا كان العدد المطلوب `p` وفي كل مرة `K` أشخاص، فالمجموع `K × p` (من مضاعفات `K`)، وهو محصور بين أقل وأكبر عدد ممكن لمشاركات الأفراد!",
            [
                f"**من جهة المجموعات:** في كل مرة يوجد {m(K)}، إذن إجمالي المشاركات يساوي {m(f'{K}p')} (أي يجب أن يقبل القسمة على {m(K)}).",
                f"**من جهة الأفراد:** أقل مجموع ممكن هو {m(f'{F} \\times {lo_c} = {lo_tot}')}، وأكبر مجموع ممكن هو {m(f'{F} \\times {hi_c} = {hi_tot}')}. إذن {m(f'{lo_tot} \\le {K}p \\le {hi_tot}')}.",
                f"**نستخرج مضاعف {m(K)} الوحيد في هذه الفترة:** العدد الوحيد من مضاعفات {m(K)} بين {m(lo_tot)} و {m(hi_tot)} هو {m(K * ans)}، ومنه {m(f'p = {K*ans} \\div {K} = {ans}')}!",
            ],
            f"تحقق: {m(K * ans)} مشاركة تتوزع بسهولة بحيث يشارك بعض الـ {m(F)} بمقدار {m(lo_c)} مرات والبقية {m(hi_c)} مرات.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "g67-double-counting-squeeze",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Find the minimum ({F} × {lo_c}) and maximum ({F} × {hi_c}) total appearances, then look for a multiple of {K} between them!",
            f"احسب أقل مجموع ظهور ({F} × {lo_c}) وأكبر مجموع ظهور ({F} × {hi_c})، ثم ابحث عن مضاعف للعدد {K} بينهما!",
            sol_en, sol_ar
        ))

    # 7. Five-statement family logic puzzle (only ONE statement is false!) (10 variants) — KMC G6-7 Sample Q15
    # Family really has B boys and G girls (son_name is 1 boy, dau_name is 1 girl):
    # True facts: total = B+G; son has B-1 brothers and G sisters; daughter has G-1 sisters and B brothers.
    # False statement gives B+1 boys (says son has B brothers instead of B-1)!
    logic_families = [
        (2, 3, "Suhaib", "Hazem", "Rana", "صهيب", "حازم", "رنا"),
        (3, 2, "adel", "Sami", "Lina", "عادل", "سامي", "لينا"),
        (2, 4, "Majed", "Omar", "Huda", "ماجد", "عمر", "هدى"),
        (3, 4, "Nasser", "Tariq", "Maha", "ناصر", "طارق", "مها"),
        (4, 2, "Waleed", "Faisal", "Noura", "وليد", "فيصل", "نورة"),
        (3, 3, "Kareem", "Ziad", "Salma", "كريم", "زياد", "سلمى"),
        (4, 3, "Bader", "Rayan", "Jana", "بدر", "ريان", "جنى"),
        (2, 2, "Hamad", "Anas", "Reem", "حمد", "أنس", "ريم"),
        (5, 2, "Yasser", "Bilal", "Dana", "ياسر", "بلال", "دانة"),
        (2, 5, "Talal", "Mazen", "Yara", "طلال", "مازن", "يارا"),
    ]
    for B, G, dad_e, son_e, dau_e, dad_a, son_a, dau_a in logic_families:
        qid = next_id()
        dad_e = dad_e.capitalize()
        tot_c = B + G
        # Pair index 0 is the ONLY FALSE statement (says son has B brothers => B+1 boys, contradicting daughter has B brothers!)
        pairs = [
            (f"My son {son_e} has {B} brother(s).", f"لابني {son_a} {B} من الإخوة الذكور."),
            (f"I have {tot_c} children in total.", f"لديّ {tot_c} من الأبناء والبنات إجمالًا."),
            (f"My daughter {dau_e} has {G - 1} sister(s).", f"لابنتي {dau_a} {G - 1} من الأخوات."),
            (f"My daughter {dau_e} has {B} brother(s).", f"لابنتي {dau_a} {B} من الإخوة الذكور."),
            (f"My son {son_e} has {G} sister(s).", f"لابني {son_a} {G} من الأخوات."),
        ]
        opts_en, opts_ar, cidx, cans = make_5_bilingual_options(pairs, 0, qid)
        q_en = (
            f"{dad_e} made the five statements below about his children, and **exactly ONE** of the five statements is **false** "
            f"(while the other four are completely true). Which statement is the **false** one?"
        )
        q_ar = (
            f"قال {dad_a} العبارات الخمس التالية عن أبنائه وبناته، وكانت **عبارة واحدة فقط** منها **خاطئة** "
            f"(بينما العبارات الأربع الأخرى صحيحة تمامًا). أيُّ عبارة هي **الخاطئة**؟"
        )
        sol_en = explain_en(
            "Look for **two statements that directly contradict each other** about the number of boys! Since only ONE statement is false, the false one MUST be one of those two, and all other three statements MUST be 100% true!",
            [
                f"**Spot the contradiction:** Saying *'{son_e} has {B} brother(s)'* means there are {m(f'{B} + 1 = {B+1}')} boys (counting {son_e} himself!), whereas saying *'{dau_e} has {B} brother(s)'* means there are {m(B)} boys! They cannot both be true, so one of them is the single lie.",
                f"**Use the other three statements (guaranteed true!):** Total children {m(f'= {tot_c}')}, and {son_e} has {m(G)} sister(s) (which also agrees with {dau_e} having {m(G-1)} sister(s): {m(f'1 + {G-1} = {G}')} girls).",
                f"**Find the true number of boys:** {m(f'{tot_c} - {G} = {B}')} boys! That matches *'{dau_e} has {B} brother(s)'* and proves *'My son {son_e} has {B} brother(s)'* is the **false** statement (he actually has {m(B-1)} brother(s)).",
            ],
            f"Family check: {m(B)} boys and {m(G)} girls -> total {m(tot_c)}; {son_e} has {m(B-1)} brother(s) and {m(G)} sister(s); {dau_e} has {m(G-1)} sister(s) and {m(B)} brother(s)!",
        )
        sol_ar = explain_ar(
            "ابحث أولًا عن **عبارتين متناقضتين** حول عدد الأولاد الذكور! بما أن عبارة واحدة فقط خاطئة، فلا بد أن تكون الكذبة إحداهما، وتكون بقية العبارات الثلاث **صحيحة حتمًا**!",
            [
                f"**تحديد التناقض:** عبارة *(لابني {son_a} {B} من الإخوة)* تعني أن عدد الذكور مع {son_a} نفسه هو {m(f'{B} + 1 = {B+1}')}، بينما عبارة *(لابنتي {dau_a} {B} من الإخوة)* تعني أن عدد الذكور هو {m(B)}! إذن إحداهما هي الخاطئة.",
                f"**الاستفادة من العبارات المؤكدة الصحة:** مجموع الأبناء {m(tot_c)}، وعدد البنات هو {m(G)} (لأن لـ{son_a} {m(G)} أخوات، ولـ{dau_a} {m(G-1)} من الأخوات بالإضافة إليها).",
                f"**حساب عدد الذكور الحقيقي:** {m(f'{tot_c} - {G} = {B}')} من الذكور! هذا يطابق عبارة {dau_a} ويثبت أن العبارة الخاطئة هي *(لابني {son_a} {B} من الإخوة الذكور)* لأن له {m(B-1)} فقط.",
            ],
            f"تحقق: مع وجود {m(B)} أولاد و {m(G)} بنات تصدق أربع عبارات وتفشل واحدة فقط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "g67-one-false-statement-family",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Remember to count {son_e} himself when counting boys, and {dau_e} herself when counting girls! Which two statements disagree on the number of boys?",
            f"لا تنسَ احتساب {son_a} نفسه ضمن الذكور و{dau_a} نفسها ضمن البنات! أي عبارتين تختلفان في عدد الذكور؟",
            sol_en, sol_ar
        ))

    # 8. Forming 3-digit EVEN/ODD numbers without repeating digits (10 variants)
    perm_digit_cases = [
        ([1, 2, 3, 4], "even"),         # 2 even choices for ones * 3 * 2 = 12
        ([1, 2, 3, 4, 5], "even"),      # 2 * 4 * 3 = 24
        ([1, 2, 3, 4, 5], "odd"),       # 3 * 4 * 3 = 36
        ([2, 3, 5, 7, 8], "even"),      # 2 * 4 * 3 = 24
        ([2, 4, 6, 7], "odd"),          # 1 * 3 * 2 = 6
        ([1, 3, 4, 6, 8], "odd"),       # 2 * 4 * 3 = 24
        ([1, 2, 4, 6, 8, 9], "odd"),    # 2 * 5 * 4 = 40
        ([2, 3, 4, 6, 9], "even"),      # 3 * 4 * 3 = 36
        ([1, 3, 5, 6], "even"),         # 1 * 3 * 2 = 6 -> wait same 6 as case 4? Different stem!
        ([1, 2, 5, 7, 9], "odd"),       # 4 * 4 * 3 = 48
    ]
    for digs, parity in perm_digit_cases:
        qid = next_id()
        n_d = len(digs)
        valid_ones = [d for d in digs if (d % 2 == 0 if parity == "even" else d % 2 == 1)]
        k_ones = len(valid_ones)
        ans = k_ones * (n_d - 1) * (n_d - 2)
        par_ar = "**زوجيًا**" if parity == "even" else "**فرديًا**"
        d_str = ", ".join(map(str, digs))
        q_en = (
            f"Using only the digits {m(d_str)} **without repeating any digit**, "
            f"how many different three-digit **{parity}** numbers can be formed?"
        )
        q_ar = (
            f"باستخدام الأرقام {m(d_str)} فقط **دون تكرار أي رقم**، "
            f"كم عددًا مختلفًا مكوّنًا من ثلاث خانات ويكون {par_ar} يمكن تكوينه؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [n_d * (n_d - 1) * (n_d - 2), k_ones * n_d * n_d, ans + 6, max(2, ans - 6)], qid
        )
        sol_en = explain_en(
            "Rule for Restricted Digits: **Always fill the restricted slot FIRST!** A number is even or odd based solely on its **ones (units) digit**.",
            [
                f"**Step A — Ones place (the restriction):** From {{{d_str}}}, the {parity} digits are {{{', '.join(map(str, valid_ones))}}}, giving **{m(k_ones)} choice(s)** for the ones digit.",
                f"**Step B — Hundreds place:** Since 1 digit is now used and repetition is forbidden, **{m(n_d - 1)} choices** remain from the {m(n_d)} digits.",
                f"**Step C — Tens place:** With 2 digits already used, **{m(n_d - 2)} choices** remain. Multiply the choices: {m(f'{k_ones} \\times {n_d - 1} \\times {n_d - 2} = {ans}')} numbers!",
            ],
            f"Total 3-digit numbers without restriction would be {m(f'{n_d}\\times{n_d-1}\\times{n_d-2} = {n_d*(n_d-1)*(n_d-2)}')}, and {m(f'\\frac{{{k_ones}}}{{{n_d}}}')} of them end in a {parity} digit = {m(ans)}!",
        )
        sol_ar = explain_ar(
            "قاعدة الخانات المشروطة: **ابدأ دائمًا بالخانة صاحبة الشرط أولًا!** كون العدد زوجيًا أو فرديًا يتحدد من **خانة الآحاد** فقط.",
            [
                f"**اختيار خانة الآحاد أولًا:** الأرقام التي تحقق الشرط من {{{d_str}}} هي {{{', '.join(map(str, valid_ones))}}}، وعددها **{m(k_ones)}** خيارات.",
                f"**اختيار خانة المئات:** بعد حجز رقم للآحاد ومنع التكرار يتبقى أمامنا **{m(n_d - 1)}** خيارات.",
                f"**اختيار خانة العشرات:** بعد حجز رقمين يتبقى **{m(n_d - 2)}** خيارات. نضرب عدد الخيارات معًا: {m(f'{k_ones} \\times {n_d - 1} \\times {n_d - 2} = {ans}')} عددًا.",
            ],
            f"مجموع الأعداد الممكنة كلها بدون شرط هو {m(n_d*(n_d-1)*(n_d-2))}، ونصيب خانة الآحاد المطلوبة منها يعطي {m(ans)} عددًا بالضبط.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "g67-three-digit-parity-no-repeat",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Fill the ONES place first so the number is guaranteed to be {parity}, then fill the hundreds and tens places!",
            "ابدأ بملء خانة الآحاد أولًا لضمان تحقق شرط الزوجية/الفردية، ثم اختر المئات فالعشرات!",
            sol_en, sol_ar
        ))

    # 9. Round-robin tournament / handshakes n(n-1)/2 (10 variants)
    rr_cases = [
        (8, "chess players in a KAUST school club play one game against every other player", "games are played", "لاعبو شطرنج في نادي المدرسة يلعب كل واحد منهم مباراة واحدة ضد كل لاعب آخر", "مباراة تُلعب"),
        (9, "friends at an Eid gathering shake hands once with every other friend", "handshakes occur", "أصدقاء في لقاء العيد يصافح كل واحد منهم الآخرين مرة واحدة", "مصافحة تحدث"),
        (10, "robotics teams compete so that every pair of teams meets once", "matches take place", "فرق روبوتات يتواجه كل فريقين منها مرة واحدة", "مواجهة تقام"),
        (7, "points are marked on a circle and every pair of points is joined by a straight chord", "chords are drawn", "نقاط على دائرة وُصلت كل نقطتين منها بوتر مستقيم", "وترًا يُرسم"),
        (11, "table-tennis players play one match against each of the others", "matches are played", "لاعبو كرة طاولة يلعب كل واحد منهم مباراة واحدة مع كل منافس آخر", "مباراة تُلعب"),
        (12, "cities are connected so a direct bus route runs between every pair of cities", "bus routes exist", "مدن يربط بين كل مدينتين منها خط حافلات مباشر", "خط حافلات يوجد"),
        (6, "colors of paint are available and a student mixes 2 different colors at a time", "two-color mixes are possible", "ألوان طلاء يمزج الطالب لونين مختلفين منها في كل مرة", "خلطة ثنائية اللون يمكن تكوينها"),
        (13, "diplomats at a summit greet every other diplomat once", "greetings take place", "مندوبًا في قمة يسلّم كل منهم على الآخر مرة واحدة", "تحية متبادلة تحدث"),
        (14, "volleyball teams play a single round-robin league (each pair plays once)", "league games are scheduled", "فريق كرة طائرة يلعب كل فريقين منها مباراة واحدة", "مباراة تُجدول"),
        (15, "students in a seminar exchange one study card per pair of students", "pair exchanges happen", "طالبًا في حلقة دراسية يتبادل كل طالبين منهم بطاقة واحدة", "عملية تبادل ثنائية تحدث"),
    ]
    for n_p, ctx_e, ask_e, ctx_a, ask_a in rr_cases:
        qid = next_id()
        ans = n_p * (n_p - 1) // 2
        q_en = f"Suppose {m(n_p)} {ctx_e}. How many {ask_e} in total?"
        q_ar = f"يوجد {m(n_p)} {ctx_a}. كم {ask_a} في المجموع الكلي؟"
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [n_p * (n_p - 1), n_p * n_p // 2, ans + n_p, ans - (n_p - 1)], qid
        )
        sol_en = explain_en(
            "Don't forget to **divide by 2**! When `A` pairs with `B`, that is the **exact same pair** as `B` pairing with `A`!",
            [
                f"Each of the {m(n_p)} items/people pairs up with the other {m(f'{n_p} - 1 = {n_p - 1}')} partners.",
                f"Multiplying {m(f'{n_p} \\times {n_p - 1} = {n_p*(n_p-1)}')} counts **every pair twice** (once from each side!).",
                f"Divide by {m(2)} to count each pair once: {m(f'\\frac{{{n_p} \\times {n_p - 1}}}{{2}} = {ans}')}.",
            ],
            f"You can also add step-by-step: {m(f'{n_p-1} + {n_p-2} + \\dots + 1 = {ans}')}!",
        )
        sol_ar = explain_ar(
            "لا تنسَ **القسمة على 2**! لأن لقاء الأول مع الثاني هو **نفس اللقاء** بين الثاني والأول ولا يُحسب مرتين!",
            [
                f"كل واحد من الـ {m(n_p)} يرتبط مع الـ {m(f'{n_p} - 1 = {n_p - 1}')} الآخرين.",
                f"حاصل الضرب {m(f'{n_p} \\times {n_p - 1} = {n_p*(n_p-1)}')} يحسب **كل زوج مرتين**.",
                f"نقسم على {m(2)} لإلغاء التكرار: {m(f'\\frac{{{n_p} \\times {n_p - 1}}}{{2}} = {ans}')}.",
            ],
            f"يمكن التحقق بالجمع التراكمي أيضًا: {m(f'{n_p-1} + {n_p-2} + \\dots + 1 = {ans}')}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Easy", "g67-pairs-handshakes",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Each of the {n_p} meets {n_p - 1} others, then divide by 2 so you don't count A-with-B and B-with-A separately!",
            f"اضرب {n_p} في ({n_p} - 1) ثم اقسم الناتج على 2 حتى لا تحسب كل زوج مرتين!",
            sol_en, sol_ar
        ))

    # 10. Counting ALL rectangles (including squares) in an m x n grid (10 variants)
    rect_cnt_cases = [
        (2, 2), (2, 3), (2, 4), (3, 3), (3, 4),
        (2, 5), (3, 5), (4, 4), (2, 6), (4, 5),
    ]
    for r, c in rect_cnt_cases:
        qid = next_id()
        sr = r * (r + 1) // 2
        sc = c * (c + 1) // 2
        ans = sr * sc
        q_en = (
            f"A rectangular grid is divided into {m(r)} rows and {m(c)} columns of unit squares ({m(r * c)} small squares in total). "
            f"How many rectangles **of all sizes** (remember: every square is also a rectangle!) can be traced along the grid lines?"
        )
        q_ar = (
            f"قُسِّمت شبكة مستطيلة إلى {m(r)} صفوف و {m(c)} أعمدة من المربعات الصغيرة ({m(r * c)} مربعًا صغيرًا). "
            f"كم مستطيلًا **بجميع الأحجام** (تذكّر أن كل مربع يُعدّ مستطيلًا أيضًا!) يمكن تحديده على خطوط الشبكة؟"
        )
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [r * c, sr + sc, ans - r * c if ans - r * c > 0 else ans + 4, ans + sr], qid
        )
        sum_r = " + ".join(str(k) for k in range(1, r + 1))
        sum_c = " + ".join(str(k) for k in range(1, c + 1))
        sol_en = explain_en(
            "Every rectangle on a grid is determined by choosing a **vertical height span** from the rows and a **horizontal width span** from the columns—so multiply the number of row-spans by the number of column-spans!",
            [
                f"**Count possible row heights** in {m(r)} rows: {m(f'{sum_r} = {sr}')} ways.",
                f"**Count possible column widths** in {m(c)} columns: {m(f'{sum_c} = {sc}')} ways.",
                f"**Multiply them together:** {m(f'{sr} \\times {sc} = {ans}')} rectangles of all sizes!",
            ],
            f"Check on tiny grids: {m('1\\times1')} gives {m(1)}; {m('2\\times2')} gives {m('3\\times3=9')} (4 small + 4 dominoes + 1 big). Here {m(f'{sr}\\times{sc} = {ans}')}!",
        )
        sol_ar = explain_ar(
            "يتحدد أي مستطيل على الشبكة باختيار **امتداد رأسي** من الصفوف و**امتداد أفقي** من الأعمدة؛ لذا نضرب عدد امتدادات الصفوف في عدد امتدادات الأعمدة!",
            [
                f"**عدد الامتدادات الرأسية** في {m(r)} صفوف هو: {m(f'{sum_r} = {sr}')}.",
                f"**عدد الامتدادات الأفقية** في {m(c)} أعمدة هو: {m(f'{sum_c} = {sc}')}.",
                f"**نضرب العددين معًا:** {m(f'{sr} \\times {sc} = {ans}')} مستطيلًا بجميع المقاسات.",
            ],
            f"مجرّد عدّ المربعات الصغيرة {m(r*c)} يغفل المستطيلات المدمجة؛ العدد الكامل هو {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Hard", "g67-count-grid-rectangles",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            f"Add (1 + ... + {r}) for the rows and (1 + ... + {c}) for the columns, then multiply those two sums!",
            f"اجمع (1 + ... + {r}) للصفوف واجمع (1 + ... + {c}) للأعمدة، ثم اضرب الناتجين معًا!",
            sol_en, sol_ar
        ))

    # 11. Two-digit positive integers with restricted digit difference |tens - ones| (10 variants) — KMC Junior Q7
    diff_cases = [
        ("at_most", 1, "differ by **at most 1**", "لا يزيد الفرق بين رقمي خانتيه على **1**"),  # exact KMC Q7 = 26!
        ("exact", 0, "have **equal** tens and units digits", "يتساوى فيه رقم الآحاد مع رقم العشرات"),
        ("exact", 1, "have tens and units digits that differ by **exactly 1**", "يكون الفرق بين رقم العشرات ورقم الآحاد **1 بالضبط**"),
        ("exact", 2, "have tens and units digits that differ by **exactly 2**", "يكون الفرق بين رقم العشرات ورقم الآحاد **2 بالضبط**"),
        ("exact", 3, "have tens and units digits that differ by **exactly 3**", "يكون الفرق بين رقم العشرات ورقم الآحاد **3 بالضبط**"),
        ("exact", 5, "have tens and units digits that differ by **exactly 5**", "يكون الفرق بين رقم العشرات ورقم الآحاد **5 بالضبط**"),
        ("exact", 7, "have tens and units digits that differ by **exactly 7**", "يكون الفرق بين رقم العشرات ورقم الآحاد **7 بالضبط**"),
        ("exact", 8, "have tens and units digits that differ by **exactly 8**", "يكون الفرق بين رقم العشرات ورقم الآحاد **8 بالضبط**"),
        ("at_least", 7, "have tens and units digits that differ by **at least 7**", "يكون الفرق بين رقمي خانتيه **7 على الأقل**"),
        ("at_least", 8, "have tens and units digits that differ by **at least 8**", "يكون الفرق بين رقمي خانتيه **8 على الأقل**"),
    ]
    for mode, k_val, cond_e, cond_a in diff_cases:
        qid = next_id()
        matches = []
        for n_v in range(10, 100):
            t_d, u_d = n_v // 10, n_v % 10
            df = abs(t_d - u_d)
            ok = (df <= k_val) if mode == "at_most" else ((df == k_val) if mode == "exact" else (df >= k_val))
            if ok:
                matches.append(n_v)
        ans = len(matches)
        q_en = f"How many two-digit positive integers (from {m(10)} to {m(99)}) {cond_e}?"
        q_ar = f"كم عددًا صحيحًا موجبًا مكوّنًا من خانتين (من {m(10)} إلى {m(99)}) {cond_a}؟"
        opts_en, opts_ar, cidx, cans = make_5_math_options(
            ans, [ans + 1, ans - 1, ans + 2, max(1, ans - 2), ans + 4], qid
        )
        sample_s = ", ".join(map(str, matches[:6])) + (", \\dots" if len(matches) > 6 else "")
        sol_en = explain_en(
            "In a two-digit number `AB`, remember the **tens digit `A` can be `1` through `9`** (`A` cannot be `0`!), while the **units digit `B` can be `0` through `9`**!",
            [
                f"Test each tens digit {m('A = 1, 2, \\dots, 9')} systematically and count valid units digits {m('B \\in \\{0,1,\\dots,9\\}')}.",
                f"Notice carefully when {m('0')} works in the units place (for example {m(10)} is valid if difference {m(1)} is allowed, whereas {m('01')} is NOT a two-digit number!).",
                f"Listing/summing across {m('A = 1')} to {m('9')} gives: {m(sample_s)} — a total of **{m(ans)}** two-digit numbers!",
            ],
            f"Watch out for {m('A=9')} or {m('B=0')} boundary cases—checking the ends prevents off-by-1 errors ({m(ans)} total)!",
        )
        sol_ar = explain_ar(
            "في أي عدد من خانتين `AB`، تذكّر أن **رقم العشرات `A` يأخذ القيم من `1` إلى `9` فقط** (لا يمكن أن يكون صفرًا!)، بينما **رقم الآحاد `B` يأخذ القيم من `0` إلى `9`**!",
            [
                f"نفحص قيم خانة العشرات بالترتيب {m('A = 1, 2, \\dots, 9')} ونعدّ قيم الآحاد {m('B')} المناسبة لكلٍّ منها.",
                f"ننتبه عند الصفر: فالعدد مثل {m(10)} مقبول لأن الصفر في الآحاد، أما {m('01')} فليس عددًا من خانتين!",
                f"بجمع الحالات لجميع قيم {m('A')} نحصل على الأعداد: {m(sample_s)} وعددها الكلي **{m(ans)}** عددًا.",
            ],
            f"مراجعة طرفَي الأرقام ({m(0)} و {m(9)}) تحميك من الخطأ بزيادة أو نقصان {m(1)}؛ الجواب الدقيق هو {m(ans)}.",
        )
        items.append(make_kmc_question(
            qid, LEVEL, "Combinatorics & Logic", "Medium", "g67-two-digit-diff",
            q_en, q_ar, opts_en, opts_ar, cidx, cans,
            "Check each tens digit from 1 to 9 (tens cannot be 0, while ones CAN be 0) and count matching ones digits!",
            "جرّب كل رقم للعشرات من 1 إلى 9 (العشرات لا تساوي 0، أما الآحاد فيمكن أن تساوي 0) وعدّ الخيارات المتاحة!",
            sol_en, sol_ar
        ))

    assert len(items) == 110, f"Expected 110 items, got {len(items)}"
    return items


if __name__ == "__main__":
    qs = generate_t1_comb_data()
    print(f"Generated {len(qs)} Track 1 Combinatorics & Data questions cleanly.")
