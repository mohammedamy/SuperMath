"""Olympiad Study Academy Lessons for Tier 1 (Grades 7–8) and Tier 2 (Grades 9–10): OLYM-L1-01..06 & OLYM-L2-01..06."""
from fractions import Fraction

from olympiad_common import (
    dm,
    m,
    make_olympiad_lesson,
    olym_concept,
    olym_worked_example,
    svg_angle_bisector_tri,
    svg_area_identity_square,
    svg_bar_chart,
    svg_circle_chords,
    svg_cyclic_quad,
    svg_digit_slots,
    svg_factor_tree,
    svg_function_machine,
    svg_graph_cycle_chords,
    svg_grid_polygon,
    svg_median_tri,
    svg_number_strip,
    svg_olym_bipartite_graph,
    svg_olym_board_coloring,
    svg_olym_cyclic_ptolemy,
    svg_olym_divisibility_lattice,
    svg_olym_func_mapping,
    svg_olym_incircle_excircle,
    svg_olym_inequality_curve,
    svg_olym_nine_point_euler,
    svg_olym_pigeonhole_boxes,
    svg_olym_radical_axis,
    svg_olym_spiral_homothety,
    svg_olym_tetrahedron_3d,
    svg_painted_cube_3d,
    svg_parabola_roots,
    svg_parallel_similar_tri,
    svg_power_of_point,
    svg_regular_polygon,
    svg_right_tri_incircle,
    svg_stu_ceva_triangle,
    svg_stu_cone_frustum,
    svg_stu_cube_corner_cut,
    svg_stu_dyck_grid,
    svg_stu_mirror_bounce,
    svg_stu_sphere_in_cylinder,
    svg_subdivided_apex_triangle,
    svg_subdivided_rect_2x2,
    svg_venn_2,
    svg_venn_3,
)

T1 = "Tier 1: Junior Olympiad (Grades 7-8)"
T2 = "Tier 2: Intermediate Olympiad (Grades 9-10)"


def _lesson_l1_01() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-01",
        level=T1,
        unit_num="1.1",
        topic="Number Theory",
        title_en="Divisors, GCD–LCM & Diophantine Factoring",
        title_ar="القواسم والقاسم المشترك الأكبر والتحليل الديوفانتي",
        summary_en=(
            "Master prime-power divisor counting and summation, Euclidean GCD–LCM structure, "
            "modular exponent cycles, and Simon's Favorite Factoring Trick for two-variable integer equations."
        ),
        summary_ar=(
            "إتقان عدّ القواسم وجمعها عبر التحليل الأولي، وبنية القاسم المشترك الأكبر والمضاعف المشترك الأصغر، "
            "ودورات البواقي المعيارية، وحيلة التحليل الديوفانتي لمعادلات الأعداد الصحيحة في متغيرين."
        ),
        goals_en=[
            f"Compute divisor count {m(r'\\tau(n)')} and divisor sum {m(r'\\sigma(n)')} under parity or divisibility constraints.",
            f"Decompose integer pairs via {m('a = gx, \\; b = gy')} with {m(r'\\gcd(x,y)=1')} and {m(r'\\gcd(a,b)\\operatorname{lcm}(a,b)=ab')}.",
            "Find remainders of huge powers by tracking repeating modular cycles.",
            f"Factor bilinear integer equations {m('xy + ax + by = c')} by completing the rectangle.",
        ],
        goals_ar=[
            f"حساب عدد القواسم {m(r'\\tau(n)')} ومجموعها {m(r'\\sigma(n)')} مع شروط الزوجية أو قابلية القسمة.",
            f"تحليل أزواج الأعداد الصحيحة بصيغة {m('a = gx, \\; b = gy')} حيث {m(r'\\gcd(x,y)=1')} واستخدام {m(r'\\gcd(a,b)\\operatorname{lcm}(a,b)=ab')}.",
            "إيجاد بواقي القوى الكبيرة عبر تتبع الدورات الدورية في الحساب المعياري.",
            f"تحليل المعادلات الصحيحة الثنائية {m('xy + ax + by = c')} بإكمال المستطيل الجبري.",
        ],
        concepts=[
            olym_concept(
                title_en="Prime Factorization, Divisor Count & Sum",
                title_ar="التحليل إلى عوامل أولية وعدّ القواسم ومجموعها",
                body_en=(
                    f"Every integer {m('n > 1')} factors uniquely as {m(r'n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}')}. "
                    f"A positive divisor chooses each exponent {m('e_i \\in \\{0,1,\\dots,a_i\\}')} independently, giving {m(r'\tau(n)')} choices. "
                    f"Expanding the product of geometric series {m('(1 + p_i + \\dots + p_i^{a_i})')} yields the sum of all positive divisors {m(r'\sigma(n)')}."
                ),
                body_ar=(
                    f"كل عدد صحيح {m('n > 1')} يتحلل بصورة وحيدة إلى {m(r'n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}')}. "
                    f"يُحدَّد كل قاسم موجب باختيار الأس {m('e_i \\in \\{0,1,\\dots,a_i\\}')} باستقلالية، مما يعطي {m(r'\tau(n)')} قاسماً. "
                    f"وعند فك جداء المتسلسلات الهندسية {m('(1 + p_i + \\dots + p_i^{a_i})')} نحصل على مجموع جميع القواسم الموجبة {m(r'\sigma(n)')}."
                ),
                formula_en=dm(r"\tau(n) = \prod_{i=1}^{k}(a_i + 1), \qquad \sigma(n) = \prod_{i=1}^{k}\frac{p_i^{a_i+1}-1}{p_i-1}"),
                caption_ar="صيغتا عدد القواسم ومجموع القواسم الموجبة:",
                formula_math_ar=dm(r"\tau(n) = \prod_{i=1}^{k}(a_i + 1), \qquad \sigma(n) = \prod_{i=1}^{k}\frac{p_i^{a_i+1}-1}{p_i-1}"),
                diagram_en=svg_factor_tree("360", "8 = 2³", "45", "9 = 3²", "5¹"),
            ),
            olym_concept(
                title_en="Euclidean Algorithm, Bézout & GCD–LCM Structure",
                title_ar="خوارزمية إقليدس وهوية بيزو وبنية القاسم والمضاعف",
                body_en=(
                    f"Repeatedly applying {m(r'\gcd(a,b) = \gcd(b, a - qb)')} strips multiples without changing common divisors and guarantees integers {m('u,v')} "
                    f"with {m(r'au + bv = \gcd(a,b)')}. Writing {m('a = gx')} and {m('b = gy')} where {m(r'g = \gcd(a,b)')} forces {m(r'\gcd(x,y)=1')} "
                    f"and {m(r'\operatorname{lcm}(a,b) = gxy')}."
                ),
                body_ar=(
                    f"تطبيق العلاقة {m(r'\gcd(a,b) = \gcd(b, a - qb)')} متكرراً يحافظ على القواسم المشتركة ويضمن وجود عددين صحيحين {m('u,v')} "
                    f"يحققان {m(r'au + bv = \gcd(a,b)')}. وبوضع {m('a = gx')} و{m('b = gy')} حيث {m(r'g = \gcd(a,b)')} ينتج أن {m(r'\gcd(x,y)=1')} "
                    f"وأن {m(r'\operatorname{lcm}(a,b) = gxy')}."
                ),
                formula_en=dm(r"\gcd(a,b)\cdot\operatorname{lcm}(a,b) = ab, \qquad au + bv = \gcd(a,b)"),
                caption_ar="العلاقة الجوهرية بين القاسم المشترك الأكبر والمضاعف المشترك الأصغر:",
                formula_math_ar=dm(r"\gcd(a,b)\cdot\operatorname{lcm}(a,b) = ab, \qquad au + bv = \gcd(a,b)"),
                diagram_en=svg_olym_divisibility_lattice("lcm(a,b)", "a = gx", "b = gy", "gcd = g"),
            ),
            olym_concept(
                title_en="Modular Cycles & Simon's Favorite Factoring Trick",
                title_ar="الدورات المعيارية وحيلة التحليل بإكمال المستطيل",
                body_en=(
                    f"Modulo {m('m')}, powers {m('a^k \\bmod m')} eventually repeat; finding {m('a^d \\equiv \\pm 1 \\pmod{m}')} collapses huge exponents immediately. "
                    f"For bilinear equations {m('xy + ax + by = c')}, add {m('ab')} to both sides so the left side factors into {m('(x+b)(y+a) = c + ab')}, "
                    "reducing an infinite search to a finite list of divisor pairs."
                ),
                body_ar=(
                    f"في الحساب المعياري لمقياس {m('m')}، تتكرر قوى {m('a^k \\bmod m')} دورياً؛ وإيجاد أصغر أس يحقق {m('a^d \\equiv \\pm 1 \\pmod{m}')} يختصر الأسس الضخمة فوراً. "
                    f"وفي المعادلات الثنائية {m('xy + ax + by = c')}، نضيف {m('ab')} للطرفين ليتحلل الطرف الأيسر إلى {m('(x+b)(y+a) = c + ab')}، "
                    "مما يحول البحث غير المنتهي إلى حصر أزواج قواسم عدد ثابت."
                ),
                formula_en=dm(r"xy + ax + by = c \iff (x + b)(y + a) = c + ab"),
                caption_ar="قاعدة إكمال المستطيل لتحليل المعادلات الديوفانتية:",
                formula_math_ar=dm(r"xy + ax + by = c \iff (x + b)(y + a) = c + ab"),
                diagram_en=svg_subdivided_rect_2x2("xy", "ax", "by", "ab"),
            ),
        ],
        traps_en=[
            f"Multiplying raw exponents {m('a_1 a_2 \\cdots a_k')} instead of {m('(a_1+1)(a_2+1)\\cdots(a_k+1)')} omits the zero-power choice {m('p_i^0 = 1')}.",
            f"When factoring {m(r'\operatorname{lcm}(a,b)/\gcd(a,b) = xy')}, forgetting {m(r'\gcd(x,y)=1')} includes invalid non-coprime factor pairs!",
            f"In {m('(x+b)(y+a) = N')}, always test whether each divisor pair actually satisfies domain bounds such as {m('x, y \\ge 1')} (or also check negative divisors if all integers are allowed).",
        ],
        traps_ar=[
            f"ضرب الأسس مباشرة {m('a_1 a_2 \\cdots a_k')} بدلاً من {m('(a_1+1)(a_2+1)\\cdots(a_k+1)')} يُغفل خيار الأس الصفري {m('p_i^0 = 1')}.",
            f"عند تحليل النسبة {m(r'\operatorname{lcm}(a,b)/\gcd(a,b) = xy')}، نسيان شرط التباين الأولي {m(r'\gcd(x,y)=1')} يؤدي لقبول أزواج خاطئة!",
            f"في المعادلة {m('(x+b)(y+a) = N')}، تحقق دائماً من قيود المجال مثل {m('x, y \\ge 1')} (ولا تنسَ القواسم السالبة إذا طُلبت جميع الحلول الصحيحة).",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-01-EX1",
                title_en="Restricted Divisor Counting",
                title_ar="عدّ القواسم المقيدة بشروط",
                q_en=f"How many positive divisors of {m('N = 162{,}000')} are **odd** multiples of {m('15')}?",
                q_ar=f"كم قاسماً موجباً للعدد {m('N = 162{,}000')} يكون عدداً **فردياً** ومضاعفاً للعدد {m('15')}؟",
                correct_val=12,
                distractors=[60, 20, 15, 9],
                idea_en="Factor N into primes, lock the exponent of 2 to zero for oddness, and enforce exponents at least 1 on 3 and 5.",
                steps_en=[
                    f"Factor {m('162{,}000 = 162 \\times 1000 = (2 \\cdot 3^4)(2^3 \\cdot 5^3) = 2^4 \\cdot 3^4 \\cdot 5^3')}.",
                    f"Any positive divisor has the form {m('d = 2^a \\cdot 3^b \\cdot 5^c')} with {m('0 \\le a \\le 4')}, {m('0 \\le b \\le 4')}, and {m('0 \\le c \\le 3')}.",
                    f"For {m('d')} to be odd, {m('a = 0')} ({m('1')} choice). For {m('15 = 3^1 \\cdot 5^1')} to divide {m('d')}, we need {m('b \\in \\{1,2,3,4\\}')} ({m('4')} choices) and {m('c \\in \\{1,2,3\\}')} ({m('3')} choices).",
                    f"Multiply independent choices: {m('1 \\times 4 \\times 3 = 12')} divisors.",
                ],
                check_en=f"Dividing {m('162{,}000')} by {m('2^4 = 16')} leaves odd part {m('10{,}125 = 3^4 \\cdot 5^3')}; dividing by {m('15')} leaves {m('3^3 \\cdot 5^2')}, which has {m('(3+1)(2+1) = 12')} divisors.",
                idea_ar="حلّل العدد إلى عوامله الأولية، وثبّت أس العدد 2 عند الصفر لضمان الفردية، واشترط أن يكون أس كل من 3 و5 واحداً على الأقل.",
                steps_ar=[
                    f"نحلل العدد: {m('162{,}000 = 162 \\times 1000 = (2 \\cdot 3^4)(2^3 \\cdot 5^3) = 2^4 \\cdot 3^4 \\cdot 5^3')}.",
                    f"كل قاسم موجب يكتب على الصورة {m('d = 2^a \\cdot 3^b \\cdot 5^c')} حيث {m('0 \\le a \\le 4')} و{m('0 \\le b \\le 4')} و{m('0 \\le c \\le 3')}.",
                    f"ليكون {m('d')} فردياً يجب أن يكون {m('a = 0')} (خيار واحد)، وليقبل القسمة على {m('15 = 3 \\cdot 5')} نحتاج {m('b \\in \\{1,2,3,4\\}')} ({m('4')} خيارات) و{m('c \\in \\{1,2,3\\}')} ({m('3')} خيارات).",
                    f"نضرب عدد الخيارات المستقلة: {m('1 \\times 4 \\times 3 = 12')} قاسماً.",
                ],
                check_ar=f"الجزء الفردي هو {m('3^4 \\cdot 5^3')}، وبقسمته على {m('15')} يتبقى {m('3^3 \\cdot 5^2')} وعدد قواسمه {m('(3+1)(2+1) = 12')}.",
                diagram_en=svg_factor_tree("162000", "2⁴", "3⁴·5³", "15 | d", "d = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-01-EX2",
                title_en="Minimizing Sum Given GCD and LCM",
                title_ar="تصغير المجموع بمعلومية القاسم والمضاعف",
                q_en=(
                    f"Positive integers {m('a')} and {m('b')} satisfy {m(r'\gcd(a,b) = 14')} and {m(r'\operatorname{lcm}(a,b) = 840')}. "
                    f"What is the **smallest** possible value of {m('a + b')}?"
                ),
                q_ar=(
                    f"عددان صحيحان موجبان {m('a')} و{m('b')} يحققان {m(r'\gcd(a,b) = 14')} و{m(r'\operatorname{lcm}(a,b) = 840')}. "
                    f"ما **أصغر** قيمة ممكنة للمجموع {m('a + b')}؟"
                ),
                correct_val=238,
                distractors=[224, 266, 322, 854],
                idea_en="Factor out the GCD so the reduced integers x and y are coprime with product 840 / 14 = 60, then pick the closest coprime pair.",
                steps_en=[
                    f"Set {m('a = 14x')} and {m('b = 14y')} with {m(r'\gcd(x,y) = 1')}.",
                    f"Then {m(r'\operatorname{lcm}(a,b) = 14xy = 840')}, which gives {m('xy = 60')}.",
                    f"List factor pairs of {m('60')}: {m('(1,60), (2,30), (3,20), (4,15), (5,12), (6,10)')}. Discard {m('(2,30)')} and {m('(6,10)')} because their GCD is {m('2 \\ne 1')}.",
                    f"Among coprime pairs, {m('(5,12)')} minimizes {m('x + y = 5 + 12 = 17')}, giving {m('a + b = 14 \\times 17 = 238')}.",
                ],
                check_en=f"For {m('a = 70')} and {m('b = 168')}: {m(r'\gcd(70,168) = 14')}, {m(r'\operatorname{lcm}(70,168) = 840')}, and {m('70 + 168 = 238')}.",
                idea_ar="أخرج القاسم المشترك الأكبر عاملاً مشتركاً ليكون العددان المختزلان أوليين نسبياً حاصل ضربهما 60، ثم اختر أقرب زوج أولي نسبياً.",
                steps_ar=[
                    f"نضع {m('a = 14x')} و{m('b = 14y')} مع الشرط {m(r'\gcd(x,y) = 1')}.",
                    f"بذلك يكون {m(r'\operatorname{lcm}(a,b) = 14xy = 840')}، ومنه {m('xy = 60')}.",
                    f"أزواج عوامل العدد {m('60')} هي {m('(1,60), (2,30), (3,20), (4,15), (5,12), (6,10)')}؛ نستبعد {m('(2,30)')} و{m('(6,10)')} لأن قاسمهما المشترك {m('2 \\ne 1')}.",
                    f"أصغر مجموع لزوج أولي نسبياً هو {m('5 + 12 = 17')}، ومنه أصغر قيمة للمجموع هي {m('14 \\times 17 = 238')}.",
                ],
                check_ar=f"للعددين {m('70')} و{m('168')}: القاسم المشترك الأكبر {m('14')}، والمضاعف المشترك الأصغر {m('840')}، ومجموعهما {m('70 + 168 = 238')}.",
                diagram_en=svg_olym_divisibility_lattice("lcm = 840", "a + b = ?", "a, b", "gcd = 14"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-01-EX3",
                title_en="Modular Exponent Cycles",
                title_ar="دورات الأسس في الحساب المعياري",
                q_en=f"What is the remainder when {m('7^{2026} + 3^{2026}')} is divided by {m('13')}?",
                q_ar=f"ما باقي قسمة العدد {m('7^{2026} + 3^{2026}')} على {m('13')}؟",
                correct_val=7,
                distractors=[0, 3, 4, 10],
                idea_en="Reduce powers of 7 and 3 modulo 13 using short cycles where powers hit 1 or −1.",
                steps_en=[
                    f"For base {m('3')}: {m('3^3 = 27 \\equiv 1 \\pmod{13}')}. Since {m('2026 = 3 \\times 675 + 1')}, we get {m('3^{2026} \\equiv 3^1 \\equiv 3 \\pmod{13}')}.",
                    f"For base {m('7')}: {m('7^2 = 49 \\equiv -3 \\pmod{13}')}, so {m('7^6 = (7^2)^3 \\equiv (-3)^3 = -27 \\equiv -1 \\pmod{13}')} and {m('7^{12} \\equiv 1 \\pmod{13}')}.",
                    f"Divide the exponent by {m('12')}: {m('2026 = 12 \\times 168 + 10')}. Thus {m('7^{2026} \\equiv 7^{10} = 7^6 \\cdot (7^2)^2 \\equiv (-1)(-3)^2 = -9 \\equiv 4 \\pmod{13}')}.",
                    f"Add the residues: {m('7^{2026} + 3^{2026} \\equiv 4 + 3 = 7 \\pmod{13}')}.",
                ],
                check_en=f"Notice {m('7 \\equiv -6')} and {m('7^{10} = 49^5 \\equiv (-3)^5 = -243 = -19 \\times 13 + 4 \\equiv 4 \\pmod{13}')}; {m('4 + 3 = 7 < 13')}.",
                idea_ar="اختزل قوى العددين 7 و3 بمقياس 13 عبر إيجاد أصغر أس يجعل الباقي مساوياً 1 أو −1.",
                steps_ar=[
                    f"للأساس {m('3')}: لدينا {m('3^3 = 27 \\equiv 1 \\pmod{13}')}، وبما أن {m('2026 = 3 \\times 675 + 1')} فإن {m('3^{2026} \\equiv 3^1 \\equiv 3 \\pmod{13}')}.",
                    f"للأساس {m('7')}: لدينا {m('7^2 = 49 \\equiv -3 \\pmod{13}')}، ومنه {m('7^6 \\equiv (-3)^3 = -27 \\equiv -1 \\pmod{13}')} وبالتالي {m('7^{12} \\equiv 1 \\pmod{13}')}.",
                    f"نقسم الأس على {m('12')}: {m('2026 = 12 \\times 168 + 10')}، فيكون {m('7^{2026} \\equiv 7^{10} = 7^6 \\cdot (7^2)^2 \\equiv (-1)(9) = -9 \\equiv 4 \\pmod{13}')}.",
                    f"نجمع الباقيين: {m('4 + 3 = 7 \\pmod{13}')}.",
                ],
                check_ar=f"نتحقق أن {m('7^{10} \\equiv (-3)^5 = -243 = -19 \\times 13 + 4 \\equiv 4 \\pmod{13}')}، والمجموع {m('4 + 3 = 7')}.",
                diagram_en=svg_digit_slots(["7²⁰²⁶", "+3²⁰²⁶", "mod 13", "r = ?"], top_note="Residue Cycle mod 13"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-01-EX4",
                title_en="Simon's Favorite Factoring Trick",
                title_ar="حيلة التحليل الديوفانتي",
                q_en=f"How many ordered pairs of **positive** integers {m('(x, y)')} satisfy {m('xy - 3x + 5y = 47')}?",
                q_ar=f"كم زوجاً مرتباً من الأعداد الصحيحة **الموجبة** {m('(x, y)')} يحقق المعادلة {m('xy - 3x + 5y = 47')}؟",
                correct_val=3,
                distractors=[6, 4, 5, 2],
                idea_en="Subtract 15 from both sides to factor into (x + 5)(y − 3) = 32, then enforce x ≥ 1 and y ≥ 1.",
                steps_en=[
                    f"Subtract {m('15')} from both sides: {m('xy - 3x + 5y - 15 = 47 - 15 = 32')}.",
                    f"Factor by grouping: {m('(x + 5)(y - 3) = 32')}.",
                    f"Since {m('x \\ge 1')}, the first factor satisfies {m('x + 5 \\ge 6')}, and since {m('32 > 0')}, {m('y - 3')} is also positive.",
                    f"The divisors of {m('32')} that are at least {m('6')} are {m('8, 16, 32')}, giving {m('(x,y) = (3,7), (11,5), (27,4)')} — exactly {m('3')} pairs.",
                ],
                check_en=f"Test all three: {m('3(7)-9+35=47')}, {m('11(5)-33+25=47')}, and {m('27(4)-81+20=47')}; the next divisor {m('x+5=4')} gives {m('x=-1 \\notin \\mathbb{Z}^+')}.",
                idea_ar="اطرح 15 من الطرفين لتحليل المعادلة إلى (x + 5)(y − 3) = 32، ثم طبّق شرطي الإيجابية x ≥ 1 و y ≥ 1.",
                steps_ar=[
                    f"نطرح {m('15')} من الطرفين: {m('xy - 3x + 5y - 15 = 47 - 15 = 32')}.",
                    f"نحلل بالتجميع: {m('(x + 5)(y - 3) = 32')}.",
                    f"بما أن {m('x \\ge 1')} فإن العامل الأول يحقق {m('x + 5 \\ge 6')}، وبما أن الناتج موجب فإن {m('y - 3 > 0')}.",
                    f"قواسم العدد {m('32')} التي لا تقل عن {m('6')} هي {m('8, 16, 32')}، وتعطي الأزواج {m('(3,7), (11,5), (27,4)')}، أي {m('3')} أزواج بالضبط.",
                ],
                check_ar=f"بالتعويض: {m('21-9+35=47')} و{m('55-33+25=47')} و{m('108-81+20=47')}؛ أما القاسم {m('x+5=4')} فيعطي {m('x=-1')} وهو مرفوض.",
                diagram_en=svg_subdivided_rect_2x2("xy", "−3x", "+5y", "? = −15"),
            ),
        ],
        blueprints=[
            "olym_t1_nt_divisors_tau_sigma",
            "olym_t1_nt_gcd_lcm_bezout",
            "olym_t1_nt_modular_cycles",
            "olym_t1_nt_factoring_diophantine",
        ],
    )


def _lesson_l1_02() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-02",
        level=T1,
        unit_num="1.2",
        topic="Algebra",
        title_en="Telescoping Sums, Symmetric Identities & Recurrences",
        title_ar="المجاميع المتداخلة والمتطابقات المتماثلة والعلاقات التكرارية",
        summary_en=(
            "Collapse long series by telescoping differences, evaluate symmetric power sums via elementary symmetric polynomials, "
            "denest compound surds, and uncover hidden periodicity in linear recurrences."
        ),
        summary_ar=(
            "تبسيط المتسلسلات الطويلة بالحذف المتداخل، وحساب مجاميع القوى المتماثلة، "
            "وفك الجذور المركبة، واكتشاف الدورية الخفية في المتتاليات التكرارية الخطية."
        ),
        goals_en=[
            f"Rewrite rational and radical summands as {m('u_k - u_{k+d}')} to cancel interior terms.",
            f"Express {m('x^2+y^2+z^2')} and {m('x^3+y^3+z^3')} in terms of {m('e_1, e_2, e_3')} using Gauss's identity.",
            f"Denest nested square roots {m(r'\sqrt{(u+v) \pm 2\sqrt{uv}}')} while respecting principal root signs.",
            "Detect periodic cycles and block-sum invariants in linear recurrence sequences.",
        ],
        goals_ar=[
            f"إعادة كتابة حدود المجاميع الكسرية والجذرية بصورة فروق {m('u_k - u_{k+d}')} لحذف الحدود الداخلية.",
            f"التعبير عن {m('x^2+y^2+z^2')} و{m('x^3+y^3+z^3')} بدلالة {m('e_1, e_2, e_3')} ومتطابقة غاوس التكعيبية.",
            f"فك الجذور المتداخلة {m(r'\sqrt{(u+v) \pm 2\sqrt{uv}}')} مع مراعاة إشارة الجذر التربيعي الموجب.",
            "اكتشاف الدورات المتكررة ومجاميع الكتل الثابتة في المتتاليات المعرّفة تكرارياً.",
        ],
        concepts=[
            olym_concept(
                title_en="Partial Fractions & Telescoping Cancellation",
                title_ar="الكسور الجزئية والحذف المتداخل",
                body_en=(
                    f"When a sum has dozens of terms, look for a difference representation {m('t_k = u_k - u_{k+1}')}. "
                    f"Every interior term cancels cleanly, leaving only the head {m('u_1')} and tail {m('-u_{n+1}')}. "
                    f"For rational denominators {m('k(k+d)')} or radical denominators {m(r'\sqrt{k}+\sqrt{k+d}')}, scale by {m('1/d')}."
                ),
                body_ar=(
                    f"عندما تحتوي المتسلسلة على حدود كثيرة، ابحث عن كتابة الحد العام كفرق {m('t_k = u_k - u_{k+1}')}. "
                    f"عندئذٍ تُحذف جميع الحدود الوسطى ويبقى الحد الأول {m('u_1')} والحد الأخير {m('-u_{n+1}')} فقط. "
                    f"وفي المقامات من الشكل {m('k(k+d)')} أو {m(r'\sqrt{k}+\sqrt{k+d}')} لا تنسَ الضرب في المعامل {m('1/d')}."
                ),
                formula_en=dm(r"\frac{1}{k(k+d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k+d}\right), \qquad \sum_{k=1}^{n}(u_k - u_{k+1}) = u_1 - u_{n+1}"),
                caption_ar="قاعدة التجزئة والحذف المتداخل (التلسكوبي):",
                formula_math_ar=dm(r"\frac{1}{k(k+d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k+d}\right), \qquad \sum_{k=1}^{n}(u_k - u_{k+1}) = u_1 - u_{n+1}"),
                diagram_en=svg_number_strip(["u₁−u₂", "u₂−u₃", "⋯", "−uₙ₊₁"]),
            ),
            olym_concept(
                title_en="Symmetric Polynomials & Gauss's Cubic Identity",
                title_ar="كثيرات الحدود المتماثلة ومتطابقة غاوس التكعيبية",
                body_en=(
                    f"Let {m('e_1 = x+y+z')}, {m('e_2 = xy+yz+zx')}, and {m('e_3 = xyz')}. "
                    f"Squaring {m('e_1')} gives {m('x^2+y^2+z^2 = e_1^2 - 2e_2')}, and Gauss's identity links the sum of cubes directly to {m('e_1, e_2, e_3')} without ever solving for individual variables."
                ),
                body_ar=(
                    f"بوضع {m('e_1 = x+y+z')} و{m('e_2 = xy+yz+zx')} و{m('e_3 = xyz')}، "
                    f"نجد بتربيع {m('e_1')} أن {m('x^2+y^2+z^2 = e_1^2 - 2e_2')}، وتربط متطابقة غاوس مجموع المكعبات مباشرة بالقيم {m('e_1, e_2, e_3')} دون الحاجة لإيجاد قيم المتغيرات منفردة."
                ),
                formula_en=dm(r"x^3 + y^3 + z^3 - 3xyz = (x+y+z)\!\left(x^2 + y^2 + z^2 - xy - yz - zx\right)"),
                caption_ar="متطابقة غاوس لمجموع ثلاثة مكعبات:",
                formula_math_ar=dm(r"x^3 + y^3 + z^3 - 3xyz = (x+y+z)\!\left(x^2 + y^2 + z^2 - xy - yz - zx\right)"),
                diagram_en=svg_area_identity_square("x", "y + z"),
            ),
            olym_concept(
                title_en="Denesting Radicals & Recurrence Cycles",
                title_ar="فك الجذور المركبة ودورات العلاقات التكرارية",
                body_en=(
                    f"To denest {m(r'\sqrt{A \pm 2\sqrt{B}}')}, find non-negative {m('u \\ge v')} with {m('u + v = A')} and {m('uv = B')}; "
                    f"then {m(r'\sqrt{A \pm 2\sqrt{B}} = \sqrt{u} \pm \sqrt{v}')}. "
                    f"For linear recurrences like {m('a_{n+2} = c_1 a_{n+1} + c_2 a_n')}, compute the first several state pairs {m('(a_n, a_{n+1})')} to spot exact periods or telescoping sums."
                ),
                body_ar=(
                    f"لفك الجذر المتداخل {m(r'\sqrt{A \pm 2\sqrt{B}}')}، نبحث عن عددين {m('u \\ge v \\ge 0')} يحققان {m('u + v = A')} و{m('uv = B')}؛ "
                    f"فيكون الناتج {m(r'\sqrt{u} \pm \sqrt{v}')}. "
                    f"وفي العلاقات التكرارية الخطية {m('a_{n+2} = c_1 a_{n+1} + c_2 a_n')}، نحسب الحدود الأولى لتحديد طول الدورة أو المجاميع المتداخلة."
                ),
                formula_en=dm(r"\sqrt{(u+v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \qquad (u \ge v \ge 0)"),
                caption_ar="متطابقة فك الجذر التربيعي المزدوج:",
                formula_math_ar=dm(r"\sqrt{(u+v) \pm 2\sqrt{uv}} = \sqrt{u} \pm \sqrt{v} \qquad (u \ge v \ge 0)"),
                diagram_en=svg_function_machine("aₙ, aₙ₋₁", "c₁·aₙ", "+c₂·aₙ₋₁", "aₙ₊₁"),
            ),
        ],
        traps_en=[
            f"Omitting the factor {m('1/d')} in {m(r'\frac{1}{k(k+d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k+d}\right)')} inflates the sum {m('d')}-fold!",
            f"Always write {m(r'\sqrt{(\sqrt{u}-\sqrt{v})^2} = |\sqrt{u}-\sqrt{v}|')} with the larger surd first so the square root stays non-negative.",
            f"Do not assume {m('x^3+y^3+z^3 = 3xyz')} forces {m('x=y=z')}; for distinct reals it holds whenever {m('x+y+z = 0')}.",
        ],
        traps_ar=[
            f"نسيان المعامل {m('1/d')} عند تجزئة {m(r'\frac{1}{k(k+d)} = \frac{1}{d}\!\left(\frac{1}{k} - \frac{1}{k+d}\right)')} يضاعف الناتج {m('d')} مرات خطأً!",
            f"تذكر دائماً أن {m(r'\sqrt{(\sqrt{u}-\sqrt{v})^2} = |\sqrt{u}-\sqrt{v}|')}، لذا ضع الجذر الأكبر أولاً ليبقى الناتج غير سالب.",
            f"لا تفترض أن {m('x^3+y^3+z^3 = 3xyz')} تعني بالضرورة {m('x=y=z')}؛ فهي تتحقق لأعداد مختلفة متى كان {m('x+y+z = 0')}.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-02-EX1",
                title_en="Odd-Denominator Telescoping Series",
                title_ar="متسلسلة متداخلة بمقامات فردية",
                q_en=f"Evaluate the exact value of {m(r'S = \frac{1}{1\cdot 3} + \frac{1}{3\cdot 5} + \frac{1}{5\cdot 7} + \cdots + \frac{1}{99\cdot 101}')}.",
                q_ar=f"أوجد القيمة الدقيقة للمجموع {m(r'S = \frac{1}{1\cdot 3} + \frac{1}{3\cdot 5} + \frac{1}{5\cdot 7} + \cdots + \frac{1}{99\cdot 101}')}.",
                correct_val=Fraction(50, 101),
                distractors=[Fraction(100, 101), Fraction(49, 101), Fraction(50, 99), Fraction(99, 101)],
                idea_en="Split each fraction with step d = 2 so all interior odd reciprocals cancel in pairs.",
                steps_en=[
                    f"Use {m(r'\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\!\left(\frac{1}{2k-1} - \frac{1}{2k+1}\right)')} for {m('k = 1, 2, \\dots, 50')}.",
                    f"Factor out {m('1/2')}: {m(r'S = \frac{1}{2}\!\left[\left(1 - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \cdots + \left(\frac{1}{99} - \frac{1}{101}\right)\right]')}.",
                    f"Every interior fraction cancels, leaving {m(r'S = \frac{1}{2}\!\left(1 - \frac{1}{101}\right) = \frac{1}{2}\cdot\frac{100}{101} = \frac{50}{101}')}.",
                ],
                check_en=f"Test the first two terms: {m(r'\frac{1}{3} + \frac{1}{15} = \frac{6}{15} = \frac{2}{5}')}, matching {m(r'\frac{k}{2k+1}')} at {m('k=50 \\implies \\frac{50}{101}')}.",
                idea_ar="جزّئ كل كسر بمعامل فرق خطوة مقداره 2 لتنحذف جميع المقلوبات الفردية الوسطى مثنى مثنى.",
                steps_ar=[
                    f"نستخدم المتطابقة {m(r'\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\!\left(\frac{1}{2k-1} - \frac{1}{2k+1}\right)')} للقيم {m('k = 1, 2, \\dots, 50')}.",
                    f"نخرج {m('1/2')} عاملاً مشتركاً: {m(r'S = \frac{1}{2}\!\left[\left(1 - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \cdots + \left(\frac{1}{99} - \frac{1}{101}\right)\right]')}.",
                    f"تحذف جميع الحدود الوسطى فيبقى {m(r'S = \frac{1}{2}\!\left(1 - \frac{1}{101}\right) = \frac{1}{2}\cdot\frac{100}{101} = \frac{50}{101}')}.",
                ],
                check_ar=f"للحدين الأولين {m(r'\frac{1}{3}+\frac{1}{15}=\frac{2}{5}')} وفق النمط {m(r'\frac{k}{2k+1}')}، وعند {m('k=50')} نحصل على {m(r'\frac{50}{101}')}.",
                diagram_en=svg_number_strip(["1/1·3", "1/3·5", "⋯", "S = ?"]),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-02-EX2",
                title_en="Cubic Power Sum via Gauss's Identity",
                title_ar="مجموع المكعبات عبر متطابقة غاوس",
                q_en=(
                    f"Real numbers {m('x, y, z')} satisfy {m('x + y + z = 5')}, {m('xy + yz + zx = 2')}, and {m('xyz = -8')}. "
                    f"What is the value of {m('x^3 + y^3 + z^3')}?"
                ),
                q_ar=(
                    f"أعداد حقيقية {m('x, y, z')} تحقق {m('x + y + z = 5')} و{m('xy + yz + zx = 2')} و{m('xyz = -8')}. "
                    f"ما قيمة المقدار {m('x^3 + y^3 + z^3')}؟"
                ),
                correct_val=71,
                distractors=[95, 119, 79, 63],
                idea_en="First compute x² + y² + z² from e₁² − 2e₂, then substitute directly into Gauss's cubic identity.",
                steps_en=[
                    f"Compute the sum of squares: {m('x^2 + y^2 + z^2 = (x+y+z)^2 - 2(xy+yz+zx) = 5^2 - 2(2) = 21')}.",
                    f"Apply Gauss's identity: {m('x^3 + y^3 + z^3 - 3xyz = (x+y+z)(x^2+y^2+z^2 - (xy+yz+zx))')}.",
                    f"Substitute known values: {m('x^3 + y^3 + z^3 - 3(-8) = 5(21 - 2) = 95')}.",
                    f"Solve for the cubic sum: {m('x^3 + y^3 + z^3 = 95 - 24 = 71')}.",
                ],
                check_en=f"The triple {m('(-1, 2, 4)')} has sum {m('5')}, pairwise sum {m('-2-4+8=2')}, product {m('-8')}, and {m('(-1)^3 + 2^3 + 4^3 = -1 + 8 + 64 = 71')}.",
                idea_ar="احسب أولاً مجموع المربعات من العلاقة e₁² − 2e₂ ثم عوّض مباشرة في متطابقة غاوس التكعيبية.",
                steps_ar=[
                    f"نحسب مجموع المربعات: {m('x^2 + y^2 + z^2 = (x+y+z)^2 - 2(xy+yz+zx) = 5^2 - 2(2) = 21')}.",
                    f"نطبق متطابقة غاوس: {m('x^3 + y^3 + z^3 - 3xyz = (x+y+z)(x^2+y^2+z^2 - (xy+yz+zx))')}.",
                    f"نعوض القيم المعطاة: {m('x^3 + y^3 + z^3 - 3(-8) = 5(21 - 2) = 95')}.",
                    f"نطرح {m('24')} من الطرفين: {m('x^3 + y^3 + z^3 = 95 - 24 = 71')}.",
                ],
                check_ar=f"الثلاثية الحقيقية {m('(-1, 2, 4)')} تحقق جميع الشروط، ومجموع مكعباتها {m('(-1)^3 + 2^3 + 4^3 = -1 + 8 + 64 = 71')}.",
                diagram_en=svg_olym_func_mapping(["e₁ = 5", "e₂ = 2", "e₃ = −8"], ["∑x² = 21", "3xyz = −24", "∑x³ = ?"], note="Symmetric Sums"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-02-EX3",
                title_en="Denesting Paired Compound Radicals",
                title_ar="فك الجذور التربيعية المركبة",
                q_en=f"Simplify the exact value of {m(r'E = \sqrt{12 + 2\sqrt{27}} + \sqrt{7 - 2\sqrt{12}}')}.",
                q_ar=f"أوجد القيمة الدقيقة المبسطة للمقدار {m(r'E = \sqrt{12 + 2\sqrt{27}} + \sqrt{7 - 2\sqrt{12}}')}.",
                correct_val=5,
                distractors=[1, 6, r"5 + 2\sqrt{3}", r"1 + 2\sqrt{3}"],
                idea_en="Write each radicand in the form (√u ± √v)² with u > v so both square roots extract cleanly.",
                steps_en=[
                    f"For {m(r'\sqrt{12 + 2\sqrt{27}}')}, note {m('9 + 3 = 12')} and {m('9 \\times 3 = 27')}, so {m(r'12 + 2\sqrt{27} = (\sqrt{9} + \sqrt{3})^2 = (3 + \sqrt{3})^2')}.",
                    f"For {m(r'\sqrt{7 - 2\sqrt{12}}')}, note {m('4 + 3 = 7')} and {m('4 \\times 3 = 12')}, so {m(r'7 - 2\sqrt{12} = (\sqrt{4} - \sqrt{3})^2 = (2 - \sqrt{3})^2')}.",
                    f"Since {m('2 = \\sqrt{4} > \\sqrt{3}')}, {m(r'\sqrt{(2-\sqrt{3})^2} = 2 - \sqrt{3} > 0')}.",
                    f"Sum the simplified radicals: {m(r'E = (3 + \sqrt{3}) + (2 - \sqrt{3}) = 5')}.",
                ],
                check_en=f"Numerically, {m(r'\sqrt{12 + 10.392} \approx 4.732')} and {m(r'\sqrt{7 - 6.928} \approx 0.268')}; their sum is {m('4.732 + 0.268 = 5')}.",
                idea_ar="أعد كتابة ما تحت كل جذر على الصورة (√u ± √v)² مع اختيار u > v لكي يخرج الجذر التربيعي بقيمة موجبة.",
                steps_ar=[
                    f"في الحد الأول {m(r'\sqrt{12 + 2\sqrt{27}}')} نلاحظ أن {m('9 + 3 = 12')} و{m('9 \\times 3 = 27')}، إذن المقدار هو {m(r'(\sqrt{9}+\sqrt{3})^2 = (3+\sqrt{3})^2')}.",
                    f"في الحد الثاني {m(r'\sqrt{7 - 2\sqrt{12}}')} نلاحظ أن {m('4 + 3 = 7')} و{m('4 \\times 3 = 12')}، إذن المقدار هو {m(r'(2-\sqrt{3})^2')}.",
                    f"بما أن {m('2 = \\sqrt{4} > \\sqrt{3}')} فإن الجذر الموجب يساوي {m(r'2 - \sqrt{3}')}.",
                    f"نجمع الحدين: {m(r'E = (3 + \sqrt{3}) + (2 - \sqrt{3}) = 5')}.",
                ],
                check_ar=f"عددياً: {m(r'\sqrt{22.392} \approx 4.732')} و{m(r'\sqrt{0.072} \approx 0.268')}، ومجموعهما {m('5')} تماماً.",
                diagram_en=svg_function_machine("√(12+2√27)", "+√(7−2√12)", "Denest", "E = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-02-EX4",
                title_en="Periodicity in a Linear Recurrence",
                title_ar="الدورية في علاقة تكرارية خطية",
                q_en=(
                    f"A sequence satisfies {m('a_1 = 2')}, {m('a_2 = 5')}, and {m('a_{n+2} = a_{n+1} - a_n')} for all {m('n \\ge 1')}. "
                    f"What is the sum {m('a_1 + a_2 + a_3 + \\cdots + a_{2026}')}?"
                ),
                q_ar=(
                    f"متتالية تحقق {m('a_1 = 2')} و{m('a_2 = 5')} والعلاقة {m('a_{n+2} = a_{n+1} - a_n')} لكل {m('n \\ge 1')}. "
                    f"ما قيمة المجموع {m('a_1 + a_2 + a_3 + \\cdots + a_{2026}')}؟"
                ),
                correct_val=8,
                distractors=[10, 7, 2, 0],
                idea_en="Compute the first 8 terms to uncover a period-6 cycle whose block sum is zero.",
                steps_en=[
                    f"Generate terms: {m('a_1 = 2')}, {m('a_2 = 5')}, {m('a_3 = 3')}, {m('a_4 = -2')}, {m('a_5 = -5')}, {m('a_6 = -3')}, {m('a_7 = 2 = a_1')}, {m('a_8 = 5 = a_2')}.",
                    f"The sequence repeats with period {m('6')}, and each block of {m('6')} consecutive terms sums to {m('2 + 5 + 3 - 2 - 5 - 3 = 0')}.",
                    f"Divide {m('2026')} by {m('6')}: {m('2026 = 6 \\times 337 + 4')}. The first {m('2022')} terms form {m('337')} zero-sum blocks.",
                    f"Sum the remaining {m('4')} terms: {m('a_1 + a_2 + a_3 + a_4 = 2 + 5 + 3 + (-2) = 8')}.",
                ],
                check_en=f"Telescoping {m('a_k = a_{k+1} - a_{k+2}')} gives {m('\\sum_{k=1}^{2026} a_k = a_2 - a_{2028} + a_1 - a_2')}? Directly: {m('a_2 - a_{2027} + a_{2026}')}: here {m('a_{2027}=a_5=-5')}, Wait: {m('\\sum_{k=1}^{n} a_k = a_2 + a_{n} - a_{n+1} = 5 + (-2) - (-5) = 8')}!",
                idea_ar="احسب الحدود الثمانية الأولى لاكتشاف دورة طولها 6 مجموع كل كتلة كاملة فيها يساوي صفراً.",
                steps_ar=[
                    f"نحسب الحدود الأولى: {m('a_1 = 2')}, {m('a_2 = 5')}, {m('a_3 = 3')}, {m('a_4 = -2')}, {m('a_5 = -5')}, {m('a_6 = -3')}, ثم {m('a_7 = 2')} و{m('a_8 = 5')}.",
                    f"المتتالية دورية بطول دورة {m('6')}، ومجموع كل {m('6')} حدود متتالية يساوي {m('2 + 5 + 3 - 2 - 5 - 3 = 0')}.",
                    f"نقسم {m('2026')} على {m('6')}: {m('2026 = 6 \\times 337 + 4')}، فتلاشي أول {m('2022')} حداً بعضها.",
                    f"نجمع الحدود الأربعة المتبقية: {m('2 + 5 + 3 + (-2) = 8')}.",
                ],
                check_ar=f"بالتحقق التلسكوبي من {m('a_k = a_{k+1} - a_{k+2}')} نجد أن المجموع يساوي {m('a_2 - a_{n+1} + a_n')}؟ بل لـ {m('n=4')}: {m('2+5+3-2 = 8')}.",
                diagram_en=svg_digit_slots(["a₁=2", "a₂=5", "a₃=3", "∑=?"], top_note="aₙ₊₂ = aₙ₊₁ − aₙ"),
            ),
        ],
        blueprints=[
            "olym_t1_alg_telescoping_series",
            "olym_t1_alg_symmetric_identities",
            "olym_t1_alg_nested_radicals_ratios",
            "olym_t1_alg_linear_recurrences_seq",
        ],
    )


def _lesson_l1_03() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-03",
        level=T1,
        unit_num="1.3",
        topic="Inequalities",
        title_en="Trivial Inequality, Two-Variable AM–GM & Triangle Bounds",
        title_ar="متباينة المربعات والمتوسط الحسابي–الهندسي ومتباينة المثلث",
        summary_en=(
            "Build inequality mastery from the non-negativity of squares, two-variable AM–GM optimization, "
            "triangle side bounds with Ravi's substitution, and discrete integer smoothing."
        ),
        summary_ar=(
            "بناء مهارات المتباينات انطلاقاً من عدم سالبية المربعات، وتحسين المقادير بمتباينة المتوسط الحسابي–الهندسي، "
            "وقيود أضلاع المثلث وتعويض رافي، والتنعيم المتقطع للأعداد الصحيحة."
        ),
        goals_en=[
            f"Complete sums of squares {m('\\sum (L_i)^2 + C \\ge C')} to prove global minima over all real numbers.",
            f"Apply two-variable AM–GM {m('a + b \\ge 2\\sqrt{ab}')} by shifting variables to cancel denominators.",
            "Count integer triangles of fixed perimeter and apply Ravi's tangency substitution.",
            "Optimize integer products with fixed sum via discrete smoothing.",
        ],
        goals_ar=[
            f"إكمال مجاميع المربعات {m('\\sum (L_i)^2 + C \\ge C')} لإثبات القيم الصغرى الشاملة على الأعداد الحقيقية.",
            f"تطبيق متباينة المتوسط الحسابي–الهندسي {m('a + b \\ge 2\\sqrt{ab}')} مع إزاحة المتغيرات لاختصار المقامات.",
            "عدّ المثلثات ذات الأضلاع الصحيحة لمحيط ثابت واستخدام تعويض رافي لقطع التماس.",
            "تعظيم جداءات الأعداد الصحيحة ذات المجموع الثابت باستراتيجية التقريب المتقطع.",
        ],
        concepts=[
            olym_concept(
                title_en="The Trivial Inequality & Sum-of-Squares Completion",
                title_ar="المتباينة البديهية وإكمال مجموع المربعات",
                body_en=(
                    f"The bedrock of all Olympiad inequalities over {m(r'\mathbb{R}')} is {m('X^2 \\ge 0')}, with equality iff {m('X = 0')}. "
                    f"Rewriting a quadratic expression as {m('(L_1)^2 + (L_2)^2 + k')} proves {m('k')} is the exact minimum provided {m('L_1 = 0')} and {m('L_2 = 0')} can hold simultaneously."
                ),
                body_ar=(
                    f"حجر الأساس لجميع متباينات الأولمبياد على {m(r'\mathbb{R}')} هو أن {m('X^2 \\ge 0')} مع تحقق المساواة إذا وفقط إذا كان {m('X = 0')}. "
                    f"وعند كتابة مقدار تربيعي بصورة {m('(L_1)^2 + (L_2)^2 + k')} فإن {m('k')} هي القيمة الصغرى الدقيقة متى أمكن تحقيق {m('L_1 = L_2 = 0')} معاً."
                ),
                formula_en=dm(r"a^2 + b^2 \ge 2ab, \qquad a^2 + b^2 + c^2 - ab - bc - ca = \frac{1}{2}\!\left[(a-b)^2 + (b-c)^2 + (c-a)^2\right] \ge 0"),
                caption_ar="متطابقة مجموع فروق المربعات غير السالبة:",
                formula_math_ar=dm(r"a^2 + b^2 \ge 2ab, \qquad a^2 + b^2 + c^2 - ab - bc - ca = \frac{1}{2}\!\left[(a-b)^2 + (b-c)^2 + (c-a)^2\right] \ge 0"),
                diagram_en=svg_area_identity_square("a", "b"),
            ),
            olym_concept(
                title_en="Two-Variable AM–GM & Domain Shifting",
                title_ar="متباينة المتوسط الحسابي–الهندسي وإزاحة المجال",
                body_en=(
                    f"For strictly positive reals {m('u, v > 0')}, {m('(u + v)/2 \\ge \\sqrt{uv}')}, geometrically visible in a semicircle where radius {m('(u+v)/2')} "
                    f"exceeds altitude {m('\\sqrt{uv}')}. To minimize {m('c(x) + k/(x - x_0)')} for {m('x > x_0')}, shift {m('c(x)')} to expose {m('(x - x_0)')} so the product becomes constant."
                ),
                body_ar=(
                    f"لكل عددين حقيقيين موجبين تماماً {m('u, v > 0')} يتحقق {m('(u + v)/2 \\ge \\sqrt{uv}')}، وهو ما يظهر هندسياً في نصف الدائرة حيث نصف القطر {m('(u+v)/2')} "
                    f"أكبر من أو يساوي العمود {m('\\sqrt{uv}')}. ولتصغير {m('c(x) + k/(x - x_0)')} عند {m('x > x_0')} نعيد تشكيل الحد الخطي ليظهر العامل {m('(x - x_0)')} فيصبح الجداء ثابتاً."
                ),
                formula_en=dm(r"\frac{u + v}{2} \ge \sqrt{uv} \quad (u, v > 0), \qquad \text{equality} \iff u = v"),
                caption_ar="متباينة المتوسط الحسابي والهندسي لمتغيرين موجبين:",
                formula_math_ar=dm(r"\frac{u + v}{2} \ge \sqrt{uv} \quad (u, v > 0), \qquad u = v"),
                diagram_en=svg_olym_inequality_curve("u", "v", "AM ≥ GM"),
            ),
            olym_concept(
                title_en="Triangle Bounds, Ravi Substitution & Discrete Smoothing",
                title_ar="قيود المثلث وتعويض رافي والتقريب المتقطع",
                body_en=(
                    f"In any triangle of perimeter {m('P = a + b + c')}, the longest side satisfies {m('c < P/2')}. "
                    f"Setting {m('a = y+z, b = z+x, c = x+y')} with {m('x,y,z > 0')} automatically encodes all three triangle inequalities. "
                    f"For positive integers with fixed sum, replacing {m('(a, b)')} where {m('b - a \\ge 2')} by {m('(a+1, b-1)')} strictly increases {m('ab')} by {m('b - a - 1 > 0')}."
                ),
                body_ar=(
                    f"في أي مثلث محيطه {m('P = a + b + c')} يحقق أطول ضلع {m('c < P/2')}. "
                    f"ويضمن تعويض رافي {m('a = y+z, b = z+x, c = x+y')} حيث {m('x,y,z > 0')} تحقق متباينات المثلث الثلاث تلقائياً. "
                    f"ولأعداد صحيحة موجبة بمجموع ثابت، فإن استبدال {m('(a+1, b-1)')} بالزوج {m('(a, b)')} عندما {m('b - a \\ge 2')} يزيد الجداء بمقدار {m('b - a - 1 > 0')}."
                ),
                formula_en=dm(r"\max(a,b,c) < \frac{a+b+c}{2}, \qquad (a+1)(b-1) - ab = b - a - 1"),
                caption_ar="قيد أطول ضلع في المثلث وخطوة التنعيم المتقطع:",
                formula_math_ar=dm(r"\max(a,b,c) < \frac{a+b+c}{2}, \qquad (a+1)(b-1) - ab = b - a - 1"),
                diagram_en=svg_olym_incircle_excircle("y + z", "z + x", "x + y", "x, y, z > 0"),
            ),
        ],
        traps_en=[
            "Never apply AM–GM before verifying both terms are strictly positive on the specified domain.",
            "Always solve the equality equation u = v to verify the optimal point actually lies inside the allowed interval!",
            f"When counting triangles of perimeter {m('P')}, exclude degenerate triples with {m('a + b = c')} (so {m('c < P/2')}, strict inequality).",
        ],
        traps_ar=[
            "لا تطبّق متباينة المتوسط الحسابي–الهندسي قبل التأكد من أن كلا الحدين موجب تماماً في المجال المعطى.",
            "حلّ دائماً معادلة المساواة u = v للتأكد من أن نقطة القيمة المثلى تقع فعلاً داخل المجال المسموح!",
            f"عند عدّ المثلثات ذات المحيط {m('P')}، استبعد الحالات المنحلة التي يكون فيها {m('a + b = c')} (أي يجب أن يكون {m('c < P/2')} متباينة صارمة).",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-03-EX1",
                title_en="Two-Variable Quadratic Minimum",
                title_ar="القيمة الصغرى لمقدار تربيعي في متغيرين",
                q_en=(
                    f"Over all real numbers {m('x')} and {m('y')}, what is the **minimum** value of "
                    f"{m('P(x, y) = 2x^2 + y^2 - 2xy - 6x - 4y + 35')}?"
                ),
                q_ar=(
                    f"على جميع الأعداد الحقيقية {m('x')} و{m('y')}، ما **أصغر** قيمة ممكنة للمقدار "
                    f"{m('P(x, y) = 2x^2 + y^2 - 2xy - 6x - 4y + 35')}؟"
                ),
                correct_val=6,
                distractors=[4, 5, 10, 35],
                idea_en="Eliminate y inside one square first by grouping y² − 2xy − 4y, then complete the remaining square in x.",
                steps_en=[
                    f"Collect all terms containing {m('y')}: {m('y^2 - 2(x + 2)y = (y - x - 2)^2 - (x + 2)^2')}.",
                    f"Substitute back into {m('P(x,y)')}: {m('P = 2x^2 - 6x + 35 + (y - x - 2)^2 - (x^2 + 4x + 4)')}.",
                    f"Simplify the remaining {m('x')}-quadratic: {m('x^2 - 10x + 31 = (x - 5)^2 + 6')}.",
                    f"Thus {m('P(x,y) = (y - x - 2)^2 + (x - 5)^2 + 6 \\ge 6')}, achieved simultaneously when {m('x = 5')} and {m('y = 7')}.",
                ],
                check_en=f"Evaluate {m('P(5, 7) = 2(25) + 49 - 70 - 30 - 28 + 35 = 50 + 49 - 128 + 35 = 6')}.",
                idea_ar="اجمع الحدود المحتوية على المتغير y أولاً داخل مربع كامل واحد، ثم أكمل المربع للمقدار التربيعي المتبقي في x.",
                steps_ar=[
                    f"نجمع حدود {m('y')}: {m('y^2 - 2(x + 2)y = (y - x - 2)^2 - (x + 2)^2')}.",
                    f"نعوض في {m('P(x,y)')}: {m('P = 2x^2 - 6x + 35 + (y - x - 2)^2 - (x^2 + 4x + 4)')}.",
                    f"نبسط المقدار المتبقي في {m('x')}: {m('x^2 - 10x + 31 = (x - 5)^2 + 6')}.",
                    f"إذن {m('P(x,y) = (y - x - 2)^2 + (x - 5)^2 + 6 \\ge 6')}، وتتحقق المساواة عند {m('x = 5')} و{m('y = 7')}.",
                ],
                check_ar=f"بالتعويض عند {m('(5,7)')}: {m('50 + 49 - 70 - 30 - 28 + 35 = 6')}.",
                diagram_en=svg_parabola_roots("x = 5", "y = 7", "min = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-03-EX2",
                title_en="Shifted Two-Variable AM–GM",
                title_ar="متباينة المتوسط الحسابي–الهندسي مع الإزاحة",
                q_en=f"For real numbers {m('x > 3')}, what is the **minimum** possible value of {m(r'f(x) = 4x + \frac{25}{x - 3}')}?",
                q_ar=f"لكل عدد حقيقي {m('x > 3')}، ما **أصغر** قيمة ممكنة للمقدار {m(r'f(x) = 4x + \frac{25}{x - 3}')}؟",
                correct_val=32,
                distractors=[20, 29, 34, 8],
                idea_en="Rewrite 4x as 4(x − 3) + 12 so the variable factor (x − 3) > 0 cancels cleanly in AM–GM.",
                steps_en=[
                    f"Decompose {m('4x = 4(x - 3) + 12')}, giving {m(r'f(x) = 4(x - 3) + \frac{25}{x - 3} + 12')}.",
                    f"Since {m('x > 3')}, both {m('4(x - 3)')} and {m('25/(x - 3)')} are strictly positive; apply AM–GM: {m(r'4(x - 3) + \frac{25}{x - 3} \ge 2\sqrt{4(x - 3)\cdot\frac{25}{x - 3}} = 2\sqrt{100} = 20')}.",
                    f"Add the constant {m('12')}: {m('f(x) \\ge 20 + 12 = 32')}.",
                    f"Verify equality: {m('4(x - 3) = 25/(x - 3) \\implies x - 3 = 5/2 \\implies x = 11/2 > 3')}, which is valid!",
                ],
                check_en=f"At {m('x = 5.5')}, {m('f(5.5) = 4(5.5) + 25/2.5 = 22 + 10 = 32')}; at {m('x = 4')}, {m('f(4) = 16 + 25 = 41 > 32')}.",
                idea_ar="أعد كتابة 4x على الصورة 4(x − 3) + 12 ليختصر العامل الموجب (x − 3) عند تطبيق متباينة المتوسط الحسابي–الهندسي.",
                steps_ar=[
                    f"نكتب {m('4x = 4(x - 3) + 12')} فيصبح {m(r'f(x) = 4(x - 3) + \frac{25}{x - 3} + 12')}.",
                    f"بما أن {m('x > 3')} فإن الحدين المتغيرين موجبان، وبتطبيق AM–GM نجد {m(r'4(x - 3) + \frac{25}{x - 3} \ge 2\sqrt{100} = 20')}.",
                    f"نضيف الثابت {m('12')}: {m('f(x) \\ge 20 + 12 = 32')}.",
                    f"نتحقق من المساواة: {m('(x - 3)^2 = 25/4 \\implies x = 11/2 > 3')} وهي ضمن المجال المسموح.",
                ],
                check_ar=f"عند {m('x = 5.5')} نجد {m('4(5.5) + 25/2.5 = 22 + 10 = 32')}، وعند {m('x = 4')} نجد {m('41 > 32')}.",
                diagram_en=svg_olym_inequality_curve("4(x−3)", "25/(x−3)", "min = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-03-EX3",
                title_en="Counting Integer Triangles by Longest Side",
                title_ar="عدّ المثلثات ذات الأضلاع الصحيحة",
                q_en=(
                    f"How many non-congruent triangles have **integer** side lengths {m('a \\le b \\le c')} "
                    f"and perimeter {m('a + b + c = 17')}?"
                ),
                q_ar=(
                    f"كم مثلثاً غير متطابق أطوال أضلاعه **أعداد صحيحة** {m('a \\le b \\le c')} "
                    f"ومحيطه {m('a + b + c = 17')}؟"
                ),
                correct_val=8,
                distractors=[6, 7, 9, 10],
                idea_en="Bound the longest side c tightly between ⌈17/3⌉ = 6 and ⌊(17−1)/2⌋ = 8, then count valid pairs (a, b) for each c.",
                steps_en=[
                    f"By the triangle inequality {m('c < a + b = 17 - c')}, we get {m('2c < 17 \\implies c \\le 8')}. Also {m('3c \\ge a + b + c = 17 \\implies c \\ge 6')}.",
                    f"Case {m('c = 8')}: {m('a + b = 9')} with {m('a \\le b \\le 8')} gives {m('(1,8,8), (2,7,8), (3,6,8), (4,5,8)')} ({m('4')} triangles).",
                    f"Case {m('c = 7')}: {m('a + b = 10')} with {m('a \\le b \\le 7')} gives {m('(3,7,7), (4,6,7), (5,5,7)')} ({m('3')} triangles).",
                    f"Case {m('c = 6')}: {m('a + b = 11')} with {m('a \\le b \\le 6')} gives {m('(5,6,6)')} ({m('1')} triangle). Total: {m('4 + 3 + 1 = 8')}.",
                ],
                check_en=f"Alcuin's formula for odd perimeter {m('P = 17')} gives {m('\\operatorname{round}((17+3)^2 / 48) = \\operatorname{round}(400/48) = 8')}.",
                idea_ar="احصر أطول ضلع c بين 6 و8 باستخدام متباينة المثلث، ثم افرز الأزواج الصحيحة (a, b) لكل حالة.",
                steps_ar=[
                    f"من متباينة المثلث {m('c < a + b = 17 - c')} نجد {m('2c < 17 \\implies c \\le 8')}، ومن {m('3c \\ge 17')} نجد {m('c \\ge 6')}.",
                    f"عندما {m('c = 8')}: {m('a + b = 9')} مع {m('b \\le 8')} يعطي {m('(1,8,8), (2,7,8), (3,6,8), (4,5,8)')} ({m('4')} مثلثات).",
                    f"عندما {m('c = 7')}: {m('a + b = 10')} مع {m('b \\le 7')} يعطي {m('(3,7,7), (4,6,7), (5,5,7)')} ({m('3')} مثلثات).",
                    f"عندما {m('c = 6')}: {m('a + b = 11')} مع {m('b \\le 6')} يعطي {m('(5,6,6)')} (مثلث واحد). المجموع الكلي: {m('4 + 3 + 1 = 8')}.",
                ],
                check_ar=f"قاعدة ألكوين للمحيط الفردي تعطي أقرب عدد صحيح للكسر {m('(17+3)^2/48 = 400/48 \\approx 8.33')} وهو {m('8')}.",
                diagram_en=svg_olym_incircle_excircle("a", "b", "c ≤ 8", "P=17, N=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-03-EX4",
                title_en="Discrete Smoothing for Maximum Integer Product",
                title_ar="تعظيم جداء الأعداد الصحيحة بالتنعيم المتقطع",
                q_en=(
                    f"Positive integers {m('x_1, x_2, x_3, x_4')} satisfy {m('x_1 + x_2 + x_3 + x_4 = 22')}. "
                    f"What is the **maximum** possible value of their product {m('x_1 x_2 x_3 x_4')}?"
                ),
                q_ar=(
                    f"أعداد صحيحة موجبة {m('x_1, x_2, x_3, x_4')} تحقق {m('x_1 + x_2 + x_3 + x_4 = 22')}. "
                    f"ما **أكبر** قيمة ممكنة لحاصل ضربها {m('x_1 x_2 x_3 x_4')}؟"
                ),
                correct_val=900,
                distractors=[875, 864, 960, 625],
                idea_en="Smooth any two integers differing by 2 or more closer together until all four numbers differ by at most 1.",
                steps_en=[
                    f"If {m('x_j - x_i \\ge 2')}, replacing {m('(x_i, x_j)')} with {m('(x_i+1, x_j-1)')} preserves the sum {m('22')} and increases {m('x_i x_j')} by {m('x_j - x_i - 1 \\ge 1')}.",
                    f"Therefore, at the maximum product, no two integers can differ by more than {m('1')}.",
                    f"Divide {m('22')} as evenly as possible among {m('4')} integers: {m('22 = 4 \\times 5 + 2 = 5 + 5 + 6 + 6')}.",
                    f"Compute the maximum product: {m('5 \\times 5 \\times 6 \\times 6 = 900')}.",
                ],
                check_en=f"Nearby integer partitions yield smaller products: {m('4 \\cdot 6 \\cdot 6 \\cdot 6 = 864 < 900')} and {m('5 \\cdot 5 \\cdot 5 \\cdot 7 = 875 < 900')}.",
                idea_ar="قرّب أي عددين الفرق بينهما 2 أو أكثر خطوة بخطوة حتى يصبح الفرق بين أي عددين في المجموعة 1 على الأكثر.",
                steps_ar=[
                    f"إذا كان {m('x_j - x_i \\ge 2')} فإن استبدال {m('(x_i+1, x_j-1)')} بالزوج {m('(x_i, x_j)')} يحفظ المجموع {m('22')} ويزيد الجداء بمقدار {m('x_j - x_i - 1 \\ge 1')}.",
                    f"لذلك تتحقق القيمة العظمى عندما لا يزيد الفرق بين أي عددين على {m('1')}.",
                    f"نقسم {m('22')} بالتساوي قدر الإمكان على {m('4')} أعداد صحيحة: {m('22 = 5 + 5 + 6 + 6')}.",
                    f"نحسب الجداء الأعظمي: {m('5 \\times 5 \\times 6 \\times 6 = 900')}.",
                ],
                check_ar=f"التقسيمات المجاورة تعطي جداءات أصغر: {m('4 \\cdot 6^3 = 864')} و{m('5^3 \\cdot 7 = 875')} وكلاهما أصغر من {m('900')}.",
                diagram_en=svg_bar_chart([("x₁", 5, "5"), ("x₂", 5, "5"), ("x₃", 6, "6"), ("x₄", 6, "?")], y_max=8),
            ),
        ],
        blueprints=[
            "olym_t1_ineq_squares_nonneg",
            "olym_t1_ineq_two_var_amgm",
            "olym_t1_ineq_triangle_bounds",
            "olym_t1_ineq_discrete_smoothing",
        ],
    )


def _lesson_l1_04() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-04",
        level=T1,
        unit_num="1.4",
        topic="Geometry",
        title_en="Angle Chasing, Area Ratios, Similarity & Incircles",
        title_ar="ملاحقة الزوايا ونسب المساحات والتشابه والدوائر الداخلية",
        summary_en=(
            "Master cyclic-quadrilateral angle chasing, cevian base-to-area ratios, "
            "parallel similarity with right-triangle altitudes, and incircle tangent segments."
        ),
        summary_ar=(
            "إتقان ملاحقة الزوايا في الرباعيات الدائرية، ونسب المساحات على القواعد، "
            "والتشابه مع ارتفاع المثلث القائم، وقطع المماسات للدائرة الداخلية."
        ),
        goals_en=[
            f"Use inscribed-angle and cyclic-quadrilateral supplementary properties {m('\\angle A + \\angle C = 180^\\circ')}.",
            f"Translate base ratios into area ratios {m('[ABD]:[ADC] = BD:DC')} for triangles sharing an altitude.",
            f"Apply parallel-line similarity and right-triangle altitude relations {m('h^2 = pq')}.",
            f"Compute incircle tangent lengths {m('x = s - a')} and right-triangle inradii {m('r = (a + b - c)/2')}.",
        ],
        goals_ar=[
            f"توظيف خواص الزوايا المحيطية وتكامل الزوايا المتقابلة في الرباعي الدائري {m('\\angle A + \\angle C = 180^\\circ')}.",
            f"تحويل نسب القواعد إلى نسب مساحات {m('[ABD]:[ADC] = BD:DC')} للمثلثات المشتركة في الارتفاع.",
            f"تطبيق تشابه المستقيمات المتوازية وعلاقة الارتفاع في المثلث القائم {m('h^2 = pq')}.",
            f"حساب أطوال القطع المماسة للدائرة الداخلية {m('x = s - a')} ونصف قطرها في المثلث القائم {m('r = (a + b - c)/2')}.",
        ],
        concepts=[
            olym_concept(
                title_en="Cyclic Quadrilaterals & Equal Inscribed Angles",
                title_ar="الرباعيات الدائرية وتساوي الزوايا المحيطية",
                body_en=(
                    f"Four points {m('A, B, C, D')} lie on a circle if and only if opposite angles sum to {m('180^\\circ')} "
                    f"or a chord subtends equal angles {m('\\angle ADB = \\angle ACB')} on the same arc."
                ),
                body_ar=(
                    f"تقع النقاط الأربع {m('A, B, C, D')} على دائرة واحدة إذا وفقط إذا كان مجموع كل زاويتين متقابلتين {m('180^\\circ')} "
                    f"أو تساوت الزاويتان المحيطيتان {m('\\angle ADB = \\angle ACB')} المشتركتان في القوس."
                ),
                rule_en=dm(r"\angle A + \angle C = 180^\circ, \qquad \angle ADB = \angle ACB"),
                rule_ar=dm(r"\angle A + \angle C = 180^\circ, \qquad \angle ADB = \angle ACB"),
                diagram_en=svg_cyclic_quad("α", "180°−α"),
            ),
            olym_concept(
                title_en="Shared-Altitude Area Ratios & Similarity",
                title_ar="نسب المساحات للمثلثات المشتركة بالارتفاع والتشابه",
                body_en=(
                    f"A cevian {m('AD')} splits {m('\\triangle ABC')} into two triangles of equal height, so their areas are proportional to their bases. "
                    f"Meanwhile, a line {m('DE \\parallel BC')} creates similar triangles whose areas scale by the square of the linear ratio."
                ),
                body_ar=(
                    f"يقسم المستقيم السيفي {m('AD')} المثلث {m('\\triangle ABC')} إلى مثلثين لهما الارتفاع نفسه، فتكون نسبة مساحتيهما مساوية لنسبة قاعدتيهما. "
                    f"بينما يصنع المستقيم الموازي {m('DE \\parallel BC')} مثلثين متشابهين تتناسب مساحتاهما مع مربع نسبة التشابه."
                ),
                rule_en=dm(r"\frac{[ABD]}{[ADC]} = \frac{BD}{DC}, \qquad \frac{[ADE]}{[ABC]} = \left(\frac{AD}{AB}\right)^2"),
                rule_ar=dm(r"\frac{[ABD]}{[ADC]} = \frac{BD}{DC}, \qquad \frac{[ADE]}{[ABC]} = \left(\frac{AD}{AB}\right)^2"),
                diagram_en=svg_parallel_similar_tri("AD", "DB", "DE", "BC"),
            ),
            olym_concept(
                title_en="Incircle Tangent Decomposition & Inradius",
                title_ar="تحليل القطع المماسة للدائرة الداخلية ونصف قطرها",
                body_en=(
                    f"Equal tangents from each vertex to the incircle have lengths {m('x = s - a')}, {m('y = s - b')}, and {m('z = s - c')}, "
                    f"where {m('s = (a+b+c)/2')}. Every triangle satisfies {m('[ABC] = r \\cdot s')}, and for a right triangle {m('r = (a + b - c)/2')}."
                ),
                rule_en=dm(r"AE = AF = s - a, \qquad [ABC] = r \cdot s, \qquad r_{\perp} = \frac{a + b - c}{2}"),
                body_ar=(
                    f"المماسات المرسومة من كل رأس إلى الدائرة الداخلية متساوية وأطوالها {m('x = s - a')} و{m('y = s - b')} و{m('z = s - c')} "
                    f"حيث {m('s = (a+b+c)/2')}. وتتحقق دائماً العلاقة {m('[ABC] = r \\cdot s')}، وفي المثلث القائم {m('r = (a + b - c)/2')}."
                ),
                rule_ar=dm(r"AE = AF = s - a, \qquad [ABC] = r \cdot s, \qquad r_{\perp} = \frac{a + b - c}{2}"),
                diagram_en=svg_olym_incircle_excircle("a", "b", "c", "s − a"),
            ),
        ],
        traps_en=[
            f"Confusing the linear similarity ratio {m('k')} with the area ratio {m('k^2')} when a parallel segment cuts a triangle.",
            f"Writing {m('AD / AB = BD / BC')} instead of {m('AD / AB = DE / BC')} when applying parallel-line similarity.",
            f"Using {m('r = (a+b-c)/2')} on a non-right triangle instead of {m('r = [ABC]/s')}.",
        ],
        traps_ar=[
            f"الخلط بين نسبة التشابه الخطية {m('k')} ونسبة المساحة {m('k^2')} عند قطع المثلث بمستقيم موازٍ للقاعدة.",
            f"كتابة {m('AD / AB = BD / BC')} بدلاً من {m('AD / AB = DE / BC')} في تشابه المثلثات.",
            f"استعمال صيغة المثلث القائم {m('r = (a+b-c)/2')} في مثلث غير قائم بدلاً من {m('r = [ABC]/s')}.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-04-EX1",
                title_en="Cyclic Quadrilateral Diagonal Angle Chasing",
                title_ar="ملاحقة الزوايا في رباعي دائري",
                q_en=(
                    f"In cyclic quadrilateral {m('ABCD')}, {m('\\angle ABC = 68^\\circ')} and {m('\\angle ACD = 38^\\circ')}. "
                    f"What is the measure of {m('\\angle CAD')} in degrees?"
                ),
                q_ar=(
                    f"في الرباعي الدائري {m('ABCD')}، قياس {m('\\angle ABC = 68^\\circ')} وقياس {m('\\angle ACD = 38^\\circ')}. "
                    f"ما قياس الزاوية {m('\\angle CAD')} بالدرجات؟"
                ),
                correct_val=30,
                distractors=[28, 34, 42, 74],
                idea_en="Find ∠ADC using supplementary opposite angles in a cyclic quadrilateral, then use the angle sum of △ACD.",
                steps_en=[
                    f"Since {m('ABCD')} is cyclic, opposite angles sum to {m('180^\\circ')}: {m('\\angle ADC = 180^\\circ - 68^\\circ = 112^\\circ')}.",
                    f"In {m('\\triangle ACD')}, the interior angles sum to {m('180^\\circ')}.",
                    f"Thus {m('\\angle CAD = 180^\\circ - 112^\\circ - 38^\\circ = 30^\\circ')}.",
                ],
                check_en=f"Angle sum in {m('\\triangle ACD')}: {m('112^\\circ + 38^\\circ + 30^\\circ = 180^\\circ')}.",
                idea_ar="أوجد الزاوية المقابلة في الرباعي الدائري ثم استعمل مجموع زوايا المثلث.",
                steps_ar=[
                    f"بما أن الرباعي دائري فإن {m('\\angle ADC = 180^\\circ - \\angle ABC = 112^\\circ')}.",
                    f"في المثلث {m('\\triangle ACD')} يكون {m('\\angle CAD = 180^\\circ - 112^\\circ - 38^\\circ = 30^\\circ')}.",
                ],
                check_ar=f"المجموع: {m('112^\\circ + 38^\\circ + 30^\\circ = 180^\\circ')}.",
                diagram_en=svg_cyclic_quad("68°", "∠CAD=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-04-EX2",
                title_en="Two-Stage Cevian Area Partition",
                title_ar="تقسيم المساحة عبر القطع السيفية على مرحلتين",
                q_en=(
                    f"In {m('\\triangle ABC')} of area {m('120')}, point {m('D')} lies on {m('BC')} with {m('BD:DC = 2:3')}, "
                    f"and point {m('E')} lies on {m('AD')} with {m('AE:ED = 3:1')}. What is the area of {m('\\triangle ABE')}?"
                ),
                q_ar=(
                    f"في المثلث {m('\\triangle ABC')} الذي مساحته {m('120')}، تقع النقطة {m('D')} على {m('BC')} بحيث {m('BD:DC = 2:3')}، "
                    f"وتقع النقطة {m('E')} على {m('AD')} بحيث {m('AE:ED = 3:1')}. ما مساحة المثلث {m('\\triangle ABE')}؟"
                ),
                correct_val=36,
                distractors=[24, 30, 45, 48],
                idea_en="First find [ABD] as a fraction of [ABC], then find [ABE] as a fraction of [ABD].",
                steps_en=[
                    f"Since {m('BD:DC = 2:3')}, {m('\\triangle ABD')} has {m('\\frac{2}{2+3} = \\frac{2}{5}')} of the area of {m('\\triangle ABC')}: {m('[ABD] = \\frac{2}{5} \\times 120 = 48')}.",
                    f"On segment {m('AD')}, {m('AE:ED = 3:1')}, so {m('\\triangle ABE')} has {m('\\frac{3}{3+1} = \\frac{3}{4}')} of {m('[ABD]')}.",
                    f"Multiply: {m('[ABE] = \\frac{3}{4} \\times 48 = 36')}.",
                ],
                check_en=f"The remaining piece {m('[DBE] = 48 - 36 = 12')}, and {m('36:12 = 3:1')}.",
                idea_ar="احسب مساحة المثلث ABD أولاً كنسبة من ABC، ثم مساحة ABE كنسبة من ABD.",
                steps_ar=[
                    f"بما أن {m('BD:DC = 2:3')}، فإن {m('[ABD] = \\frac{2}{5} \\times 120 = 48')}.",
                    f"وبما أن {m('AE:ED = 3:1')}، فإن {m('[ABE] = \\frac{3}{4} [ABD] = \\frac{3}{4} \\times 48 = 36')}.",
                ],
                check_ar=f"المساحة المتبقية {m('[DBE] = 12')} والنسبة {m('36:12 = 3:1')}.",
                diagram_en=svg_subdivided_apex_triangle(2, 2),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-04-EX3",
                title_en="Right-Triangle Altitude to the Hypotenuse",
                title_ar="الارتفاع النازل على الوتر في المثلث القائم",
                q_en=(
                    f"In right triangle {m('ABC')} with {m('\\angle C = 90^\\circ')}, the altitude {m('CD')} to hypotenuse {m('AB')} "
                    f"divides {m('AB')} into segments {m('AD = 9')} and {m('DB = 16')}. What is the perimeter of {m('\\triangle ABC')}?"
                ),
                q_ar=(
                    f"في المثلث القائم {m('ABC')} في {m('C')}، يقسم الارتفاع {m('CD')} النازل على الوتر {m('AB')} "
                    f"الوترَ إلى جزأين {m('AD = 9')} و{m('DB = 16')}. ما محيط المثلث {m('\\triangle ABC')}؟"
                ),
                correct_val=60,
                distractors=[48, 56, 62, 72],
                idea_en="Use leg-projection similarity relations AC² = AD·AB and BC² = DB·AB.",
                steps_en=[
                    f"The hypotenuse has length {m('AB = 9 + 16 = 25')}.",
                    f"By right-triangle similarity, {m('AC = \\sqrt{AD \\cdot AB} = \\sqrt{9 \\times 25} = 15')}.",
                    f"Similarly, {m('BC = \\sqrt{DB \\cdot AB} = \\sqrt{16 \\times 25} = 20')}.",
                    f"The perimeter is {m('15 + 20 + 25 = 60')}.",
                ],
                check_en=f"Altitude {m('CD = \\sqrt{9 \\times 16} = 12')}, and {m('15^2 + 20^2 = 225 + 400 = 625 = 25^2')}.",
                idea_ar="استخدم علاقتي مسقطَي الضلعين القائمين على الوتر لإيجاد طولي الضلعين ثم المحيط.",
                steps_ar=[
                    f"طول الوتر {m('AB = 9 + 16 = 25')}.",
                    f"من تشابه المثلثات القائمة: {m('AC = \\sqrt{9 \\times 25} = 15')} و{m('BC = \\sqrt{16 \\times 25} = 20')}.",
                    f"إذن محيط المثلث هو {m('15 + 20 + 25 = 60')}.",
                ],
                check_ar=f"الارتفاع {m('CD = 12')} و{m('15^2 + 20^2 = 25^2')}.",
                diagram_en=svg_right_tri_incircle("15", "20", "9+16", "P=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-04-EX4",
                title_en="Incircle Tangent Segment & Heron Inradius",
                title_ar="طول مماس الدائرة الداخلية ونصف قطرها",
                q_en=(
                    f"A triangle {m('ABC')} has side lengths {m('AB = 13')}, {m('BC = 14')}, and {m('CA = 15')}. "
                    f"Its incircle touches {m('BC')} at {m('D')} and has inradius {m('r')}. What is the value of {m('BD + r')}?"
                ),
                q_ar=(
                    f"مثلث {m('ABC')} أطوال أضلاعه {m('AB = 13')} و{m('BC = 14')} و{m('CA = 15')}. "
                    f"تمس دائرته الداخلية الضلع {m('BC')} في {m('D')} ونصف قطرها {m('r')}. ما قيمة {m('BD + r')}؟"
                ),
                correct_val=10,
                distractors=[9, 11, 12, 14],
                idea_en="Compute the semiperimeter s, then use BD = s - AC and r = [ABC]/s.",
                steps_en=[
                    f"The semiperimeter is {m('s = (13 + 14 + 15)/2 = 21')}.",
                    f"The tangent segment from {m('B')} to the incircle has length {m('BD = s - AC = 21 - 15 = 6')}.",
                    f"By Heron's formula, {m('[ABC] = \\sqrt{21 \\cdot 8 \\cdot 7 \\cdot 6} = 84')}, so {m('r = 84 / 21 = 4')}.",
                    f"Therefore {m('BD + r = 6 + 4 = 10')}.",
                ],
                check_en=f"Note also {m('DC = s - AB = 21 - 13 = 8')}, and {m('BD + DC = 6 + 8 = 14 = BC')}.",
                idea_ar="احسب نصف المحيط s ثم استعمل BD = s - AC ونصف القطر r = [ABC]/s.",
                steps_ar=[
                    f"نصف المحيط هو {m('s = (13 + 14 + 15)/2 = 21')}.",
                    f"طول قطعة المماس من الرأس {m('B')} هو {m('BD = s - AC = 21 - 15 = 6')}.",
                    f"من صيغة هيرون {m('[ABC] = 84')}، ومنه {m('r = 84 / 21 = 4')}، فيكون {m('BD + r = 6 + 4 = 10')}.",
                ],
                check_ar=f"مجموع الجزأين على القاعدة: {m('BD + DC = 6 + 8 = 14 = BC')}.",
                diagram_en=svg_olym_incircle_excircle("14", "15", "13", "BD+r=?"),
            ),
        ],
        blueprints=[
            "olym_t1_geo_angle_chasing_cyclic",
            "olym_t1_geo_area_ratios_bases",
            "olym_t1_geo_similarity_pythagoras",
            "olym_t1_geo_incircle_tangents",
        ],
    )


def _lesson_l1_05() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-05",
        level=T1,
        unit_num="1.5",
        topic="Geometry",
        title_en="Reflections, Polygons, Pick's Theorem & 3D Solids",
        title_ar="الانعكاس والمضلعات ومبرهنة بيك والمجسمات ثلاثية الأبعاد",
        summary_en=(
            "Solve shortest-path reflection problems, regular-polygon angle and diagonal counts, "
            "lattice-polygon areas via Pick's theorem, and 3D cube/polyhedron geometry."
        ),
        summary_ar=(
            "حل مسائل أقصر مسار بالانعكاس، وزوايا وأقطار المضلعات المنتظمة، "
            "ومساحات المضلعات الشبكية بمبرهنة بيك، وهندسة المكعبات والمجسمات."
        ),
        goals_en=[
            f"Unfold reflection paths across mirrors so that {m('AP + PB = A\\x27B')} becomes a straight segment.",
            f"Calculate interior angles and diagonal counts {m('n(n-3)/2')} in convex {m('n')}-gons.",
            f"Compute lattice-polygon areas using Pick's formula {m('A = I + B/2 - 1')}.",
            f"Analyze painted cubes, Euler's polyhedron formula {m('V - E + F = 2')}, and unfolded surface paths.",
        ],
        goals_ar=[
            f"فرد مسارات الانعكاس عبر المرايا بحيث يتحول المجموع {m('AP + PB')} إلى قطعة مستقيمة {m('A\\x27B')}.",
            f"حساب الزوايا الداخلية وعدد الأقطار {m('n(n-3)/2')} في المضلعات المحدبة.",
            f"إيجاد مساحة المضلع الشبكي باستخدام صيغة بيك {m('A = I + B/2 - 1')}.",
            f"تحليل المكعبات المطلية وصيغة أويلر للمجسمات {m('V - E + F = 2')} وأقصر المسارات على الأسطح.",
        ],
        concepts=[
            olym_concept(
                title_en="Heron's Shortest-Path Reflection Principle",
                title_ar="مبدأ هيرون لأقصر مسار بالانعكاس",
                body_en=(
                    f"To minimize {m('AP + PB')} as {m('P')} varies on a line {m('\\ell')}, reflect {m('A')} across {m('\\ell')} to {m('A\\x27')}. "
                    f"Because {m('AP = A\\x27P')}, the minimum equals the straight-line distance {m('A\\x27B')}."
                ),
                body_ar=(
                    f"لتصغير المجموع {m('AP + PB')} عندما تتحرك {m('P')} على مستقيم {m('\\ell')}، اعكس {m('A')} حول {m('\\ell')} إلى {m('A\\x27')}. "
                    f"وبما أن {m('AP = A\\x27P')} فإن القيمة الصغرى تساوي طول القطعة المستقيمة {m('A\\x27B')}."
                ),
                rule_en=dm(r"\min_{P \in \ell}(AP + PB) = A'B = \sqrt{(\Delta x)^2 + (y_A + y_B)^2}"),
                rule_ar=dm(r"\min_{P \in \ell}(AP + PB) = A'B = \sqrt{(\Delta x)^2 + (y_A + y_B)^2}"),
                diagram_en=svg_stu_mirror_bounce("Δx", "y₁+y₂", "A'B"),
            ),
            olym_concept(
                title_en="Polygon Diagonals & Pick's Lattice Theorem",
                title_ar="أقطار المضلعات ومبرهنة بيك الشبكية",
                body_en=(
                    f"A convex {m('n')}-gon hasinterior angle sum {m('(n-2)\\cdot 180^\\circ')} and {m('n(n-3)/2')} diagonals. "
                    f"A simple polygon whose vertices lie on integer lattice points has area {m('A = I + B/2 - 1')}."
                ),
                body_ar=(
                    f"مجموع الزوايا الداخلية لمضلع محدب ذي {m('n')} أضلاع هو {m('(n-2)\\cdot 180^\\circ')} وعدد أقطاره {m('n(n-3)/2')}. "
                    f"ومساحة أي مضلع رؤوسه نقاط شبكية صحيحة تُعطى بصيغة بيك {m('A = I + B/2 - 1')}."
                ),
                rule_en=dm(r"D_n = \frac{n(n-3)}{2}, \qquad A_{\text{Pick}} = I + \frac{B}{2} - 1"),
                rule_ar=dm(r"D_n = \frac{n(n-3)}{2}, \qquad A_{\text{Pick}} = I + \frac{B}{2} - 1"),
                diagram_en=svg_grid_polygon(5, 4, [(0, 0), (4, 0), (3, 3), (1, 3)], ["A", "B", "C", "D"]),
            ),
            olym_concept(
                title_en="Painted Cubes & Surface Unfolding in 3D",
                title_ar="المكعبات المطلية وفرد الأسطح ثلاثية الأبعاد",
                body_en=(
                    f"An {m('n \\times n \\times n')} painted cube cut into unit cubes has {m('8')} three-face, {m('12(n-2)')} two-face, "
                    f"{m('6(n-2)^2')} one-face, and {m('(n-2)^3')} unpainted cubes. Shortest surface paths unfold adjacent faces into a plane."
                ),
                body_ar=(
                    f"المكعب المطلي بحجم {m('n \\times n \\times n')} ينقسم إلى {m('8')} مكعبات بثلاثة أوجه مطلية، و{m('12(n-2)')} بوجهين، "
                    f"و{m('6(n-2)^2')} بوجه واحد، و{m('(n-2)^3')} بدون طلاء. وأقصر مسار على السطح ينتج من فرد الأوجه المتجاورة في مستوٍ واحد."
                ),
                rule_en=dm(r"N_3 = 8, \quad N_2 = 12(n-2), \quad N_1 = 6(n-2)^2, \quad N_0 = (n-2)^3"),
                rule_ar=dm(r"N_3 = 8, \quad N_2 = 12(n-2), \quad N_1 = 6(n-2)^2, \quad N_0 = (n-2)^3"),
                diagram_en=svg_painted_cube_3d(4),
            ),
        ],
        traps_en=[
            f"Counting boundary lattice points on a segment from {m('(x_1,y_1)')} to {m('(x_2,y_2)')} by guessing instead of using {m('\\gcd(|x_2-x_1|, |y_2-y_1|)')}.",
            f"Forgetting to subtract the {m('n')} polygon sides from {m('\\binom{n}{2}')} when counting diagonals.",
            f"Computing a 3D surface path using space distance {m('\\sqrt{a^2+b^2+c^2}')} instead of the planar unfolded hypotenuse {m('\\sqrt{a^2+(b+c)^2}')}.",
        ],
        traps_ar=[
            f"تخمين عدد النقاط الشبكية على ضلع بدلاً من حساب {m('\\gcd(|x_2-x_1|, |y_2-y_1|)')}.",
            f"نسيان طرح أضلاع المضلع {m('n')} من {m('\\binom{n}{2}')} عند حساب عدد الأقطار.",
            f"حساب أقصر مسار على سطح متوازي مستطيلات باستعمال القطر الفضائي بدلاً من وتر الشبكة المفردة {m('\\sqrt{a^2+(b+c)^2}')}.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-05-EX1",
                title_en="Shortest Reflection Path Across a River",
                title_ar="أقصر مسار انعكاس عبر خط مستقيم",
                q_en=(
                    f"Points {m('A(0, 3)')} and {m('B(12, 6)')} lie on the same side of the {m('x')}-axis. "
                    f"A point {m('P')} is chosen on the {m('x')}-axis to minimize {m('AP + PB')}. What is this minimum length?"
                ),
                q_ar=(
                    f"تقع النقطتان {m('A(0, 3)')} و{m('B(12, 6)')} في الجهة نفسها من محور السينات. "
                    f"اختيرت نقطة {m('P')} على محور السينات لتصغير المجموع {m('AP + PB')}. ما أصغر قيمة ممكنة لهذا الطول؟"
                ),
                correct_val=15,
                distractors=[13, 14, 17, 21],
                idea_en="Reflect A(0,3) across the x-axis to A'(0,-3) and compute the straight-line distance A'B.",
                steps_en=[
                    f"Reflecting {m('A(0, 3)')} across the {m('x')}-axis gives {m('A\\x27(0, -3)')} with {m('AP = A\\x27P')} for every {m('P')} on the axis.",
                    f"Thus {m('AP + PB = A\\x27P + PB \\ge A\\x27B')} by the triangle inequality.",
                    f"Compute {m('A\\x27B = \\sqrt{(12 - 0)^2 + (6 - (-3))^2} = \\sqrt{144 + 81} = \\sqrt{225} = 15')}.",
                ],
                check_en=f"The optimal point {m('P(4, 0)')} gives {m('AP = 5')} and {m('PB = 10')}, summing to {m('15')}.",
                idea_ar="اعكس النقطة A(0,3) حول محور السينات إلى A'(0,-3) واحسب المسافة المستقيمة A'B.",
                steps_ar=[
                    f"انعكاس {m('A(0, 3)')} حول محور السينات هو {m('A\\x27(0, -3)')} حيث {m('AP = A\\x27P')}.",
                    f"أقصر مسار يساوي طول القطعة المستقيمة {m('A\\x27B = \\sqrt{12^2 + (6 + 3)^2} = \\sqrt{144 + 81} = 15')}.",
                ],
                check_ar=f"عند النقطة {m('P(4,0)')} يكون {m('AP = 5')} و{m('PB = 10')} ومجموعهما {m('15')}.",
                diagram_en=svg_stu_mirror_bounce("12", "3+6", "min=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-05-EX2",
                title_en="Convex Polygon Diagonal & Interior Angle Relation",
                title_ar="علاقة أقطار المضلع المحدب وزواياه",
                q_en=(
                    f"A regular polygon has exactly {m('54')} diagonals. "
                    f"What is the measure, in degrees, of each interior angle of this polygon?"
                ),
                q_ar=(
                    f"مضلع منتظم له {m('54')} قطراً بالضبط. "
                    f"ما قياس كل زاوية داخلية في هذا المضلع بالدرجات؟"
                ),
                correct_val=150,
                distractors=[140, 144, 156, 160],
                idea_en="Solve n(n-3)/2 = 54 for the number of sides n, then compute 180° - 360°/n.",
                steps_en=[
                    f"Set {m('\\frac{n(n - 3)}{2} = 54')}, so {m('n(n - 3) = 108')}.",
                    f"Since {m('12 \\times 9 = 108')}, the polygon has {m('n = 12')} sides (a dodecagon).",
                    f"Each exterior angle is {m('360^\\circ / 12 = 30^\\circ')}, so each interior angle is {m('180^\\circ - 30^\\circ = 150^\\circ')}.",
                ],
                check_en=f"Check: {m('12 \\times 9 / 2 = 54')} diagonals and interior sum {m('10 \\times 180^\\circ = 1800^\\circ = 12 \\times 150^\\circ')}.",
                idea_ar="حل المعادلة n(n-3)/2 = 54 لإيجاد عدد الأضلاع n ثم احسب الزاوية الداخلية.",
                steps_ar=[
                    f"من {m('n(n - 3)/2 = 54')} نجد {m('n(n - 3) = 108')}، ومنه {m('n = 12')}.",
                    f"قياس الزاوية الخارجية {m('360^\\circ / 12 = 30^\\circ')}، فتكون الزاوية الداخلية {m('180^\\circ - 30^\\circ = 150^\\circ')}.",
                ],
                check_ar=f"التحقق: {m('12 \\times 9 / 2 = 54')} قطراً.",
                diagram_en=svg_regular_polygon(8, [(0, 3), (0, 4), (1, 5)]),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-05-EX3",
                title_en="Interior Lattice Points via Pick's Theorem",
                title_ar="إيجاد النقاط الشبكية الداخلية بمبرهنة بيك",
                q_en=(
                    f"A lattice triangle has vertices at {m('O(0, 0)')}, {m('A(8, 0)')}, and {m('B(4, 6)')}. "
                    f"How many lattice points with integer coordinates lie **strictly inside** {m('\\triangle OAB')}?"
                ),
                q_ar=(
                    f"مثلث شبكي رؤوسه {m('O(0, 0)')} و{m('A(8, 0)')} و{m('B(4, 6)')}. "
                    f"كم نقطة شبكية ذات إحداثيات صحيحة تقع **داخل** المثلث {m('\\triangle OAB')} تماماً؟"
                ),
                correct_val=19,
                distractors=[18, 20, 21, 24],
                idea_en="Compute the area A = ½·base·height and the boundary points B via GCDs, then solve I = A - B/2 + 1.",
                steps_en=[
                    f"The area of {m('\\triangle OAB')} is {m('A = \\frac{1}{2} \\times 8 \\times 6 = 24')}.",
                    f"Count boundary lattice points on each side using {m('\\gcd(|\\Delta x|, |\\Delta y|)')}: {m('\\gcd(8,0) + \\gcd(4,6) + \\gcd(4,6) = 8 + 2 + 2 = 12')}.",
                    f"By Pick's Theorem, {m('I = A - \\frac{B}{2} + 1 = 24 - 6 + 1 = 19')}.",
                ],
                check_en=f"Check Pick's formula: {m('19 + 12/2 - 1 = 24')}.",
                idea_ar="احسب المساحة A وعدد نقاط المحيط B عبر القاسم المشترك الأكبر ثم طبّق صيغة بيك.",
                steps_ar=[
                    f"مساحة المثلث هي {m('A = \\frac{1}{2} \\times 8 \\times 6 = 24')}.",
                    f"عدد النقاط الشبكية على المحيط: {m('B = \\gcd(8,0) + \\gcd(4,6) + \\gcd(4,6) = 8 + 2 + 2 = 12')}.",
                    f"بتطبيق مبرهنة بيك: {m('I = A - B/2 + 1 = 24 - 6 + 1 = 19')}.",
                ],
                check_ar=f"التحقق: {m('19 + 6 - 1 = 24')}.",
                diagram_en=svg_grid_polygon(5, 4, [(0, 0), (4, 0), (2, 3)], ["O", "A", "B"]),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-05-EX4",
                title_en="Painted Cube Unit-Cube Classification",
                title_ar="تصنيف المكعبات الصغيرة في مكعب مطلي",
                q_en=(
                    f"The entire surface of a {m('5 \\times 5 \\times 5')} wooden cube is painted red, and it is then cut into {m('125')} unit cubes. "
                    f"How many of these unit cubes have **at most one** red face?"
                ),
                q_ar=(
                    f"طُلي السطح الخارجي لمكعب خشبي أبعاده {m('5 \\times 5 \\times 5')} باللون الأحمر ثم قُطع إلى {m('125')} مكعباً صغيراً. "
                    f"كم مكعباً صغيراً منها يمتلك **وجهاً أحمر واحداً على الأكثر**؟"
                ),
                correct_val=81,
                distractors=[54, 64, 72, 93],
                idea_en="Sum the 0-face interior cubes (n-2)³ and the 1-face center cubes 6(n-2)² for n = 5.",
                steps_en=[
                    f"For {m('n = 5')}, the interior unpainted cubes form a {m('3 \\times 3 \\times 3')} core: {m('N_0 = (5-2)^3 = 27')}.",
                    f"The cubes with exactly one painted face lie in the {m('3 \\times 3')} interior of each of the {m('6')} faces: {m('N_1 = 6(5-2)^2 = 54')}.",
                    f"The total with at most one red face is {m('N_0 + N_1 = 27 + 54 = 81')}.",
                ],
                check_en=f"The remaining cubes have 2 or 3 red faces: {m('12(3) + 8 = 44')}, and {m('81 + 44 = 125')}.",
                idea_ar="اجمع المكعبات الداخلية غير المطلية (n-2)³ ومكعبات مراكز الأوجه ذات الوجه الواحد 6(n-2)² عند n = 5.",
                steps_ar=[
                    f"عند {m('n = 5')}: عدد المكعبات بدون أي وجه أحمر هو {m('(5-2)^3 = 27')}.",
                    f"وعدد المكعبات ذات وجه أحمر واحد هو {m('6(5-2)^2 = 54')}.",
                    f"المجموع الكلي: {m('27 + 54 = 81')}.",
                ],
                check_ar=f"المكعبات المتبقية (وجهان أو 3 أوجه): {m('36 + 8 = 44')} و{m('81 + 44 = 125')}.",
                diagram_en=svg_painted_cube_3d(5),
            ),
        ],
        blueprints=[
            "olym_t1_geo_reflections_shortest",
            "olym_t1_geo_polygons_diagonals",
            "olym_t1_geo_lattice_picks_area",
            "olym_t1_geo_3d_cubes_pyramids",
        ],
    )


def _lesson_l1_06() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L1-06",
        level=T1,
        unit_num="1.6",
        topic="Combinatorics",
        title_en="Stars & Bars, Pigeonhole Principle, Parity & Inclusion–Exclusion",
        title_ar="النجوم والفواصل ومبدأ برج الحمام والزوجية والتضمين والإقصاء",
        summary_en=(
            "Count integer distributions via Stars and Bars, force guaranteed collisions with Dirichlet's Pigeonhole Principle, "
            "prove impossibility via parity and coloring invariants, and apply Inclusion–Exclusion."
        ),
        summary_ar=(
            "عدّ التوزيعات الصحيحة بطريقة النجوم والفواصل، وإثبات الحتميات بمبدأ برج الحمام، "
            "واستخدام متباينات الزوجية والتلوين، وتطبيق مبدأ التضمين والإقصاء."
        ),
        goals_en=[
            f"Count solutions to {m('x_1 + \\cdots + x_k = n')} via {m('\\binom{n-1}{k-1}')} (positive) and {m('\\binom{n+k-1}{k-1}')} (non-negative).",
            f"Apply the generalized Pigeonhole Principle {m('\\lceil N/k \\rceil')} to worst-case selection and residue classes.",
            f"Use checkerboard coloring and parity invariants to analyze tilings and game states.",
            f"Apply 2-set and 3-set Inclusion–Exclusion and small derangement numbers {m('D_n')}.",
        ],
        goals_ar=[
            f"عدّ حلول {m('x_1 + \\cdots + x_k = n')} عبر {m('\\binom{n-1}{k-1}')} للموجبة و{m('\\binom{n+k-1}{k-1}')} لغير السالبة.",
            f"تطبيق مبدأ برج الحمام المعمم {m('\\lceil N/k \\rceil')} في مسائل أسوأ الحالات وبواقي القسمة.",
            f"توظيف تلوين رقعة الشطرنج وثوابت الزوجية لتحليل التبليط وحالات الألعاب.",
            f"تطبيق مبدأ التضمين والإقصاء لمجموعتين وثلاث مجموعات وحساب التباديل الخالية من النقاط الثابتة {m('D_n')}.",
        ],
        concepts=[
            olym_concept(
                title_en="Stars & Bars Bijection with Lower Bounds",
                title_ar="تقابل النجوم والفواصل مع القيود الدنيا",
                body_en=(
                    f"The number of non-negative integer solutions to {m('x_1 + x_2 + \\cdots + x_k = n')} is {m('\\binom{n+k-1}{k-1}')}. "
                    f"If each variable has a lower bound {m('x_i \\ge c_i')}, substitute {m('y_i = x_i - c_i \\ge 0')} first."
                ),
                body_ar=(
                    f"عدد الحلول الصحيحة غير السالبة للمعادلة {m('x_1 + x_2 + \\cdots + x_k = n')} هو {m('\\binom{n+k-1}{k-1}')}. "
                    f"وإذا خضع كل متغير لقيد أدنى {m('x_i \\ge c_i')} نعوّض {m('y_i = x_i - c_i \\ge 0')} أولاً."
                ),
                rule_en=dm(r"\#\big(x_1+\cdots+x_k=n,\; x_i \ge 0\big) = \binom{n+k-1}{k-1}"),
                rule_ar=dm(r"\#\big(x_1+\cdots+x_k=n,\; x_i \ge 0\big) = \binom{n+k-1}{k-1}"),
                diagram_en=svg_digit_slots(["★★", "|", "★★★", "|", "★"], top_note="Stars & Bars: C(n+k−1, k−1)"),
            ),
            olym_concept(
                title_en="Dirichlet's Pigeonhole Principle & Worst-Case Bounds",
                title_ar="مبدأ برج الحمام لديريكليه وحدود أسوأ الحالات",
                body_en=(
                    f"If {m('N')} objects are placed into {m('k')} boxes, at least one box contains at least {m('\\lceil N/k \\rceil')} objects. "
                    f"To guarantee {m('m')} items in the same box, we need {m('N = k(m - 1) + 1')} items."
                ),
                body_ar=(
                    f"إذا وُضع {m('N')} عنصراً في {m('k')} صناديق، فإن صندوقاً واحداً على الأقل يحوي {m('\\lceil N/k \\rceil')} عنصراً أو أكثر. "
                    f"ولضمان وجود {m('m')} عناصر في الصندوق نفسه نحتاج إلى {m('N = k(m - 1) + 1')} عنصراً."
                ),
                rule_en=dm(r"N_{\min} = k(m - 1) + 1 \implies \max_i |B_i| \ge m"),
                rule_ar=dm(r"N_{\min} = k(m - 1) + 1 \implies \max_i |B_i| \ge m"),
                diagram_en=svg_olym_pigeonhole_boxes(4, "N = k(m−1)+1", "≥ m in 1 box"),
            ),
            olym_concept(
                title_en="Parity Coloring & Inclusion–Exclusion",
                title_ar="تلوين الزوجية ومبدأ التضمين والإقصاء",
                body_en=(
                    f"Every domino on a checkerboard covers one black and one white square. "
                    f"For overlapping sets, Inclusion–Exclusion alternates sums of intersections: "
                    f"{m('|A \\cup B \\cup C| = \\sum |A| - \\sum |A \\cap B| + |A \\cap B \\cap C|')}."
                ),
                body_ar=(
                    f"كل قطعة دومينو على رقعة شطرنج تغطي مربعاً أسود ومربعاً أبيض. "
                    f"وللمجموعات المتداخلة يتناوب مبدأ التضمين والإقصاء بين الجمع والطرح: "
                    f"{m('|A \\cup B \\cup C| = \\sum |A| - \\sum |A \\cap B| + |A \\cap B \\cap C|')}."
                ),
                rule_en=dm(r"|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |B\cap C| - |C\cap A| + |A\cap B\cap C|"),
                rule_ar=dm(r"|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |B\cap C| - |C\cap A| + |A\cap B\cap C|"),
                diagram_en=svg_olym_board_coloring(4, 4, 2, "1 Domino = 1B + 1W"),
            ),
        ],
        traps_en=[
            f"Applying {m('\\binom{n+k-1}{k-1}')} when variables must be strictly positive ({m('x_i \\ge 1')}) without subtracting {m('1')} from each variable first.",
            f"Answering {m('k(m-1)')} instead of {m('k(m-1) + 1')} in worst-case Pigeonhole problems.",
            f"Subtracting pairwise intersections in 3-set Inclusion–Exclusion without adding back the triple intersection {m('|A \\cap B \\cap C|')}.",
        ],
        traps_ar=[
            f"استعمال {m('\\binom{n+k-1}{k-1}')} للمتغيرات الموجبة تماماً ({m('x_i \\ge 1')}) دون طرح {m('1')} من كل متغير أولاً.",
            f"الاكتفاء بالعدد {m('k(m-1)')} بدلاً من {m('k(m-1) + 1')} في مسائل أسوأ الحالات لبرج الحمام.",
            f"طرح التقاطعات الثنائية في مبدأ التضمين والإقصاء لثلاث مجموعات دون إعادة جمع التقاطع الثلاثي {m('|A \\cap B \\cap C|')}.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L1-06-EX1",
                title_en="Stars and Bars with Lower-Bound Constraints",
                title_ar="النجوم والفواصل مع قيود دنيا على المتغيرات",
                q_en=(
                    f"How many ordered quadruples of integers {m('(x_1, x_2, x_3, x_4)')} satisfy "
                    f"{m('x_1 + x_2 + x_3 + x_4 = 15')} with {m('x_1 \\ge 1')}, {m('x_2 \\ge 2')}, {m('x_3 \\ge 0')}, and {m('x_4 \\ge 3')}?"
                ),
                q_ar=(
                    f"كم رباعية مرتبة من الأعداد الصحيحة {m('(x_1, x_2, x_3, x_4)')} تحقق "
                    f"{m('x_1 + x_2 + x_3 + x_4 = 15')} بشرط {m('x_1 \\ge 1')} و{m('x_2 \\ge 2')} و{m('x_3 \\ge 0')} و{m('x_4 \\ge 3')}؟"
                ),
                correct_val=220,
                distractors=[165, 210, 286, 364],
                idea_en="Shift each variable by its minimum value so all new variables are non-negative.",
                steps_en=[
                    f"Let {m('y_1 = x_1 - 1')}, {m('y_2 = x_2 - 2')}, {m('y_3 = x_3')}, and {m('y_4 = x_4 - 3')}, so each {m('y_i \\ge 0')}.",
                    f"The new sum is {m('y_1 + y_2 + y_3 + y_4 = 15 - (1 + 2 + 0 + 3) = 9')}.",
                    f"By Stars and Bars for {m('n = 9')} and {m('k = 4')}, the count is {m('\\binom{9 + 4 - 1}{4 - 1} = \\binom{12}{3} = 220')}.",
                ],
                check_en=f"Evaluate {m('\\binom{12}{3} = \\frac{12 \\times 11 \\times 10}{6} = 220')}.",
                idea_ar="أزح كل متغير بمقدار حده الأدنى لتصبح المتغيرات الجديدة غير سالبة.",
                steps_ar=[
                    f"نضع {m('y_1 = x_1 - 1')} و{m('y_2 = x_2 - 2')} و{m('y_3 = x_3')} و{m('y_4 = x_4 - 3')} بحيث {m('y_i \\ge 0')}.",
                    f"يصبح المجموع المتبقي {m('y_1 + y_2 + y_3 + y_4 = 15 - 6 = 9')}.",
                    f"بقاعدة النجوم والفواصل: {m('\\binom{9 + 4 - 1}{4 - 1} = \\binom{12}{3} = 220')}.",
                ],
                check_ar=f"الحساب المباشر: {m('12 \\times 11 \\times 10 / 6 = 220')}.",
                diagram_en=svg_digit_slots(["y₁≥0", "y₂≥0", "y₃≥0", "y₄≥0"], top_note="Σyᵢ = 9 → C(12,3)=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-06-EX2",
                title_en="Pigeonhole Pairing for a Target Sum",
                title_ar="مبدأ برج الحمام لأزواج ذات مجموع ثابت",
                q_en=(
                    f"From the set {m('S = \\{1, 2, 3, \\dots, 30\\}')}, what is the minimum number of distinct integers that must be chosen "
                    f"to guarantee that at least two chosen integers have a sum of {m('31')}?"
                ),
                q_ar=(
                    f"من المجموعة {m('S = \\{1, 2, 3, \\dots, 30\\}')}، ما أقل عدد من الأعداد الصحيحة المختلفة التي يجب اختيارها "
                    f"لضمان وجود عددين من الأعداد المختارة مجموعهما {m('31')}؟"
                ),
                correct_val=16,
                distractors=[14, 15, 17, 18],
                idea_en="Partition {1, ..., 30} into 15 complementary pigeonhole pairs summing to 31.",
                steps_en=[
                    f"Group {m('S')} into {m('15')} pairs summing to {m('31')}: {m('\\{1,30\\}, \\{2,29\\}, \\dots, \\{15,16\\}')}.",
                    f"Choosing {m('15')} numbers can avoid a pair (for example, choosing {m('1, 2, \\dots, 15')}).",
                    f"By the Pigeonhole Principle, choosing {m('15 + 1 = 16')} numbers forces at least two into the same pair, so their sum is {m('31')}.",
                ],
                check_en=f"Worst case is {m('15')} numbers (one per pair); the {m('16')}th number completes a sum of {m('31')}.",
                idea_ar="قسّم الأعداد إلى 15 زوجاً متكاملاً مجموع كل زوج منها 31.",
                steps_ar=[
                    f"نقسّم المجموعة إلى {m('15')} زوجاً: {m('\\{1,30\\}, \\{2,29\\}, \\dots, \\{15,16\\}')}.",
                    f"في أسوأ حالة نختار {m('15')} عدداً (عدداً واحداً من كل زوج).",
                    f"بمبدأ برج الحمام، اختيار العدد الـ {m('16')} يضمن وقوع عددين في زوج واحد مجموعهما {m('31')}.",
                ],
                check_ar=f"المجموعة {m('\\{1,2,\\dots,15\\}')} من {m('15')} عنصراً لا تحوي أي زوج مجموعه {m('31')}.",
                diagram_en=svg_olym_pigeonhole_boxes(5, "15 sum-pairs {k, 31−k}", "Min pick = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-06-EX3",
                title_en="Board Parity & Domino Tiling Excess",
                title_ar="تلوين الزوجية وفائض التبليط بالدومينو",
                q_en=(
                    f"From an {m('8 \\times 8')} chessboard with alternating black and white squares, three squares of the **same color** are removed. "
                    f"What is the maximum number of {m('1 \\times 2')} dominoes that can be placed on the remaining {m('61')} squares without overlap?"
                ),
                q_ar=(
                    f"من رقعة شطرنج أبعادها {m('8 \\times 8')} ملونة بالتناوب بالأسود والأبيض، حُذفت {m('3')} مربعات من **اللون نفسه**. "
                    f"ما أكبر عدد من قطع الدومينو {m('1 \\times 2')} التي يمكن وضعها على المربعات الـ {m('61')} المتبقية دون تداخل؟"
                ),
                correct_val=29,
                distractors=[30, 28, 27, 31],
                idea_en="Count the remaining black and white squares; each domino requires one square of each color.",
                steps_en=[
                    f"An {m('8 \\times 8')} board starts with {m('32')} black and {m('32')} white squares.",
                    f"Removing {m('3')} squares of the same color leaves {m('29')} squares of that color and {m('32')} of the opposite color.",
                    f"Since every domino covers exactly {m('1')} black and {m('1')} white square, at most {m('29')} dominoes can be placed.",
                ],
                check_en=f"29 dominoes cover {m('29')} black and {m('29')} white squares ({m('58')} squares total), which is achievable.",
                idea_ar="احسب عدد المربعات المتبقية من كل لون؛ فكل قطعة دومينو تتطلب مربعاً واحداً من كل لون.",
                steps_ar=[
                    f"تحوي الرقعة في الأصل {m('32')} مربعاً أسود و{m('32')} مربعاً أبيض.",
                    f"بعد حذف {m('3')} مربعات من اللون نفسه يتبقى {m('29')} مربعاً من هذا اللون و{m('32')} من اللون الآخر.",
                    f"بما أن كل قطعة دومينو تغطي مربعاً من كل لون، فإن أكبر عدد ممكن من القطع هو {m('29')}.",
                ],
                check_ar=f"{m('29')} قطعة تغطي {m('29')} مربعاً من كل لون بإجمالي {m('58')} مربعاً.",
                diagram_en=svg_olym_board_coloring(4, 4, 2, "29B & 32W → max = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L1-06-EX4",
                title_en="Three-Set Inclusion–Exclusion on Coprime Count",
                title_ar="مبدأ التضمين والإقصاء لثلاث مجموعات",
                q_en=(
                    f"How many positive integers from {m('1')} to {m('120')} inclusive are divisible by **none** of {m('2')}, {m('3')}, or {m('5')}?"
                ),
                q_ar=(
                    f"كم عدداً صحيحاً موجباً من {m('1')} إلى {m('120')} (شاملاً الطرفين) **لا يقبل القسمة** على أيٍّ من {m('2')} أو {m('3')} أو {m('5')}؟"
                ),
                correct_val=32,
                distractors=[28, 30, 36, 40],
                idea_en="Apply 3-set Inclusion–Exclusion (or Euler's product 120·(1-1/2)(1-1/3)(1-1/5)).",
                steps_en=[
                    f"Let {m('A_2, A_3, A_5')} be the multiples of {m('2, 3, 5')} in {m('\\{1, \\dots, 120\\}')}: sizes are {m('60, 40, 24')}.",
                    f"Pairwise intersections have sizes {m('|A_2 \\cap A_3| = 20')}, {m('|A_2 \\cap A_5| = 12')}, {m('|A_3 \\cap A_5| = 8')}, and triple intersection {m('|A_2 \\cap A_3 \\cap A_5| = 4')}.",
                    f"By PIE, {m('|A_2 \\cup A_3 \\cup A_5| = (60+40+24) - (20+12+8) + 4 = 88')}.",
                    f"Thus {m('120 - 88 = 32')} integers are divisible by none of {m('2, 3, 5')}.",
                ],
                check_en=f"Euler totient check: {m('120 \\times \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{4}{5} = 32')}.",
                idea_ar="طبّق مبدأ التضمين والإقصاء لثلاث مجموعات ثم اطرح الاتحاد من 120.",
                steps_ar=[
                    f"أعداد مضاعفات {m('2, 3, 5')} هي {m('60, 40, 24')}، والتقاطعات الثنائية {m('20, 12, 8')}، والتقاطع الثلاثي {m('4')}.",
                    f"حجم الاتحاد: {m('(60+40+24) - (20+12+8) + 4 = 88')}.",
                    f"الأعداد التي لا تقبل القسمة على أي منها: {m('120 - 88 = 32')}.",
                ],
                check_ar=f"باستخدام دالة أويلر: {m('120 \\times \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{4}{5} = 32')}.",
                diagram_en=svg_venn_3("2", "3", "5", {"A": 28, "B": 16, "C": 8, "AB": 16, "BC": 4, "AC": 8, "ABC": 4, "out": "?"}),
            ),
        ],
        blueprints=[
            "olym_t1_comb_stars_bars_bijections",
            "olym_t1_comb_pigeonhole_dirichlet",
            "olym_t1_comb_parity_coloring",
            "olym_t1_comb_inclusion_exclusion",
        ],
    )


def _lesson_l2_01() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-01",
        level=T2,
        unit_num="2.1",
        topic="Number Theory",
        title_en="Euler's Totient, Chinese Remainder Theorem, Legendre's Formula & Pell/Pythagorean Equations",
        title_ar="دالة أويلر ومبرهنة الباقي الصينية وصيغة ليجاندر ومعادلات بيل وفيثاغورس",
        summary_en=(
            "Reduce large modular exponents with Fermat–Euler, solve simultaneous congruences via CRT, "
            "compute exact prime valuations of factorials with Legendre's formula, and parameterize Pythagorean/Pell equations."
        ),
        summary_ar=(
            "اختزال الأسس المعيارية الكبيرة بمبرهنة فيرما-أويلر، وحل التطابقات الآنية بمبرهنة الباقي الصينية، "
            "وحساب أسس العوامل الأولية للمضاريب بصيغة ليجاندر، وتمثيل معادلات فيثاغورس وبيل."
        ),
        goals_en=[
            f"Compute Euler's totient {m('\\varphi(n) = n \\prod (1 - 1/p)')} and reduce exponents modulo {m('\\varphi(n)')}.",
            f"Solve simultaneous congruences {m('x \\equiv a_i \\pmod{m_i}')} for pairwise coprime moduli.",
            f"Evaluate {m('v_p(n!) = \\sum_{k \\ge 1} \\lfloor n/p^k \\rfloor = \\frac{n - s_p(n)}{p - 1}')} using Legendre's formula.",
            f"Generate primitive Pythagorean triples {m('(m^2-n^2, 2mn, m^2+n^2)')} and Pell solutions {m('x^2 - dy^2 = 1')}.",
        ],
        goals_ar=[
            f"حساب دالة أويلر {m('\\varphi(n) = n \\prod (1 - 1/p)')} واختزال الأسس بترديد {m('\\varphi(n)')}.",
            f"حل الأنظمة المعيارية الآنية {m('x \\equiv a_i \\pmod{m_i}')} للمقاسات المتباينة مثنى مثنى.",
            f"حساب {m('v_p(n!) = \\sum_{k \\ge 1} \\lfloor n/p^k \\rfloor = \\frac{n - s_p(n)}{p - 1}')} بصيغة ليجاندر.",
            f"توليد ثلاثيات فيثاغورس الأولية {m('(m^2-n^2, 2mn, m^2+n^2)')} وحلول معادلة بيل {m('x^2 - dy^2 = 1')}.",
        ],
        concepts=[
            olym_concept(
                title_en="Euler's Totient Function & Euler–Fermat Theorem",
                title_ar="دالة أويلر ومبرهنة أويلر-فيرما",
                body_en=(
                    f"For any integer {m('n = p_1^{a_1} \\cdots p_k^{a_k}')}, the count of integers in {m('\\{1,\\dots,n\\}')} coprime to {m('n')} "
                    f"is {m('\\varphi(n)')}. Whenever {m('\\gcd(a, n) = 1')}, {m('a^{\\varphi(n)} \\equiv 1 \\pmod{n}')}."
                ),
                body_ar=(
                    f"لأي عدد صحيح {m('n = p_1^{a_1} \\cdots p_k^{a_k}')}، عدد الأعداد في {m('\\{1,\\dots,n\\}')} الأولية نسبياً مع {m('n')} "
                    f"هو {m('\\varphi(n)')}. وإذا كان {m('\\gcd(a, n) = 1')} فإن {m('a^{\\varphi(n)} \\equiv 1 \\pmod{n}')}."
                ),
                rule_en=dm(r"\varphi(n) = n\prod_{p \mid n}\left(1 - \frac{1}{p}\right), \qquad \gcd(a,n)=1 \implies a^{\varphi(n)} \equiv 1 \pmod n"),
                rule_ar=dm(r"\varphi(n) = n\prod_{p \mid n}\left(1 - \frac{1}{p}\right), \qquad \gcd(a,n)=1 \implies a^{\varphi(n)} \equiv 1 \pmod n"),
                diagram_en=svg_olym_divisibility_lattice("n = p^a q^b", "φ(p^a)", "φ(q^b)", "a^φ(n) ≡ 1"),
            ),
            olym_concept(
                title_en="Chinese Remainder Theorem (CRT) & Legendre's Formula",
                title_ar="مبرهنة الباقي الصينية وصيغة ليجاندر للمضروب",
                body_en=(
                    f"Pairwise coprime congruences have a unique solution modulo {m('M = m_1 m_2 \\cdots m_k')}. "
                    f"For any prime {m('p')}, the exact exponent of {m('p')} dividing {m('n!')} is given by Legendre's floor sum."
                ),
                body_ar=(
                    f"أنظمة التطابقات ذات المقاسات الأولية نسبياً مثنى مثنى لها حل وحيد بترديد الجداء {m('M = m_1 m_2 \\cdots m_k')}. "
                    f"ولأي عدد أولي {m('p')}، يُعطى الأس الدقيق للعدد {m('p')} في تحليل {m('n!')} بمجموع ليجاندر."
                ),
                rule_en=dm(r"v_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - s_p(n)}{p - 1}"),
                rule_ar=dm(r"v_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor = \frac{n - s_p(n)}{p - 1}"),
                diagram_en=svg_function_machine("n!", "⌊n/p⌋+⌊n/p²⌋+…", "(n−s_p(n))/(p−1)", "v_p(n!)"),
            ),
            olym_concept(
                title_en="Primitive Pythagorean Triples & Pell Recurrence",
                title_ar="ثلاثيات فيثاغورس الأولية وعلاقة بيل التراجعية",
                body_en=(
                    f"Coprime {m('m > n > 0')} of opposite parity generate all primitive Pythagorean triples {m('(m^2-n^2, 2mn, m^2+n^2)')}. "
                    f"For Pell's equation {m('x^2 - dy^2 = 1')}, all positive solutions come from powers {m('(x_1 + y_1\\sqrt{d})^k')}."
                ),
                body_ar=(
                    f"يولّد العددان الأوليان نسبياً {m('m > n > 0')} مختلفا الزوجية جميع ثلاثيات فيثاغورس الأولية {m('(m^2-n^2, 2mn, m^2+n^2)')}. "
                    f"وفي معادلة بيل {m('x^2 - dy^2 = 1')} تنتج جميع الحلول الموجبة من القوى {m('(x_1 + y_1\\sqrt{d})^k')}."
                ),
                rule_en=dm(r"(a,b,c) = (m^2-n^2,\, 2mn,\, m^2+n^2), \qquad x_k + y_k\sqrt{d} = (x_1 + y_1\sqrt{d})^k"),
                rule_ar=dm(r"(a,b,c) = (m^2-n^2,\, 2mn,\, m^2+n^2), \qquad x_k + y_k\sqrt{d} = (x_1 + y_1\sqrt{d})^k"),
                diagram_en=svg_right_tri_incircle("m²−n²", "2mn", "m²+n²", "r=n(m−n)"),
            ),
        ],
        traps_en=[
            f"Reducing an exponent modulo {m('n')} instead of modulo {m('\\varphi(n)')}, or applying Euler's theorem when {m('\\gcd(a,n) > 1')}.",
            f"Stopping at {m('\\lfloor n/5 \\rfloor')} when counting trailing zeros of {m('n!')} and forgetting higher powers {m('\\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor')}.",
            f"Forgetting that {m('m, n')} must have opposite parity and {m('\\gcd(m,n)=1')} for a Pythagorean triple to be primitive.",
        ],
        traps_ar=[
            f"اختزال الأس بترديد {m('n')} بدلاً من {m('\\varphi(n)')}، أو تطبيق مبرهنة أويلر عندما يكون {m('\\gcd(a,n) > 1')}.",
            f"الاكتفاء بالحد الأول {m('\\lfloor n/5 \\rfloor')} عند حساب الأصفار الطرفية للمضروب ونسيان {m('\\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor')}.",
            f"نسيان شرط اختلاف الزوجية و{m('\\gcd(m,n)=1')} لكي تكون ثلاثية فيثاغورس أولية.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-01-EX1",
                title_en="Euler's Totient & Modular Power Reduction",
                title_ar="دالة أويلر واختزال القوى المعيارية",
                q_en=(
                    f"What is the value of {m('\\varphi(300)')}, the number of positive integers at most {m('300')} "
                    f"that are relatively prime to {m('300')}?"
                ),
                q_ar=(
                    f"ما قيمة {m('\\varphi(300)')}، أي عدد الأعداد الصحيحة الموجبة التي لا تزيد على {m('300')} "
                    f"والأولية نسبياً مع {m('300')}؟"
                ),
                correct_val=80,
                distractors=[60, 72, 96, 100],
                idea_en="Factor 300 = 2²·3·5² and apply Euler's product formula.",
                steps_en=[
                    f"Prime factorization gives {m('300 = 2^2 \\cdot 3^1 \\cdot 5^2')}, so the distinct prime factors are {m('2, 3, 5')}.",
                    f"Apply {m('\\varphi(300) = 300 \\left(1 - \\frac{1}{2}\\right)\\left(1 - \\frac{1}{3}\\right)\\left(1 - \\frac{1}{5}\\right)')}.",
                    f"Multiply: {m('300 \\times \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{4}{5} = 80')}.",
                ],
                check_en=f"Multiplicative check: {m('\\varphi(4)\\varphi(3)\\varphi(25) = 2 \\times 2 \\times 20 = 80')}.",
                idea_ar="حلّل 300 = 2²·3·5² وطبّق صيغة جداء أويلر.",
                steps_ar=[
                    f"العوامل الأولية المميزة للعدد {m('300 = 2^2 \\cdot 3 \\cdot 5^2')} هي {m('2, 3, 5')}.",
                    f"نحسب {m('\\varphi(300) = 300 \\times \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{4}{5} = 80')}.",
                ],
                check_ar=f"التحقق الضربي: {m('\\varphi(4)\\varphi(3)\\varphi(25) = 2 \\times 2 \\times 20 = 80')}.",
                diagram_en=svg_olym_divisibility_lattice("300", "2²·3", "5²", "φ(300)=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-01-EX2",
                title_en="Chinese Remainder Theorem Three-Modulus System",
                title_ar="نظام تطابقات ثلاثي بمبرهنة الباقي الصينية",
                q_en=(
                    f"Find the smallest positive integer {m('x')} such that {m('x \\equiv 2 \\pmod{5}')}, "
                    f"{m('x \\equiv 3 \\pmod{7}')}, and {m('x \\equiv 4 \\pmod{9}')}."
                ),
                q_ar=(
                    f"أوجد أصغر عدد صحيح موجب {m('x')} يحقق {m('x \\equiv 2 \\pmod{5}')} "
                    f"و{m('x \\equiv 3 \\pmod{7}')} و{m('x \\equiv 4 \\pmod{9}')}."
                ),
                correct_val=157,
                distractors=[122, 148, 167, 193],
                idea_en="Notice 2x ≡ -1 modulo 5, 7, and 9!",
                steps_en=[
                    f"Observe the pattern: {m('2(2) = 4 \\equiv -1 \\pmod{5}')}, {m('2(3) = 6 \\equiv -1 \\pmod{7}')}, and {m('2(4) = 8 \\equiv -1 \\pmod{9}')}.",
                    f"Hence {m('2x + 1')} is divisible by {m('\\operatorname{lcm}(5, 7, 9) = 315')}.",
                    f"The smallest positive solution occurs at {m('2x + 1 = 315')}, which gives {m('x = 157')}.",
                ],
                check_en=f"Check remainders of {m('157')}: {m('157 = 31\\cdot 5 + 2 = 22\\cdot 7 + 3 = 17\\cdot 9 + 4')}.",
                idea_ar="لاحظ أن 2x + 1 يقبل القسمة على كل من 5 و7 و9 معاً.",
                steps_ar=[
                    f"نلاحظ أن {m('2x \\equiv -1')} بترديد كل من {m('5')} و{m('7')} و{m('9')}.",
                    f"إذن {m('2x + 1')} مضاعف للعدد {m('5 \\times 7 \\times 9 = 315')}.",
                    f"أصغر حل موجب ينتج عند {m('2x + 1 = 315')}، ومنه {m('x = 157')}.",
                ],
                check_ar=f"بواقي {m('157')} على {m('5, 7, 9')} هي {m('2, 3, 4')} على الترتيب.",
                diagram_en=svg_number_strip(["mod 5: 2", "mod 7: 3", "mod 9: 4", "x = ?"]),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-01-EX3",
                title_en="Legendre's p-adic Valuation on Factorials",
                title_ar="صيغة ليجاندر لأس العامل الأولي في المضروب",
                q_en=(
                    f"What is the largest integer {m('k')} such that {m('3^k')} divides {m('100!')}?"
                ),
                q_ar=(
                    f"ما أكبر عدد صحيح {m('k')} يجعل {m('3^k')} يقسم المضروب {m('100!')}؟"
                ),
                correct_val=48,
                distractors=[44, 46, 49, 50],
                idea_en="Sum the floors ⌊100/3^j⌋ for j = 1, 2, 3, 4.",
                steps_en=[
                    f"By Legendre's formula, {m('v_3(100!) = \\lfloor 100/3 \\rfloor + \\lfloor 100/9 \\rfloor + \\lfloor 100/27 \\rfloor + \\lfloor 100/81 \\rfloor')}.",
                    f"Evaluate each floor: {m('33 + 11 + 3 + 1 = 48')}.",
                ],
                check_en=f"In base 3, {m('100 = 10201_3')} has digit sum {m('s_3(100) = 4')}, so {m('(100 - 4)/(3 - 1) = 48')}.",
                idea_ar="اجمع الأجزاء الصحيحة ⌊100/3^j⌋ لقوى العدد 3 التي لا تتجاوز 100.",
                steps_ar=[
                    f"بصيغة ليجاندر: {m('v_3(100!) = \\lfloor 100/3 \\rfloor + \\lfloor 100/9 \\rfloor + \\lfloor 100/27 \\rfloor + \\lfloor 100/81 \\rfloor')}.",
                    f"نحسب المجموع: {m('33 + 11 + 3 + 1 = 48')}.",
                ],
                check_ar=f"مجموع أرقام 100 في الأساس 3 هو 4، ومنه {m('(100-4)/2 = 48')}.",
                diagram_en=svg_function_machine("100!", "33+11+3+1", "v₃(100!)", "k = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-01-EX4",
                title_en="Second Positive Solution to Pell's Equation",
                title_ar="الحل الموجب الثاني لمعادلة بيل",
                q_en=(
                    f"The fundamental positive integer solution to Pell's equation {m('x^2 - 3y^2 = 1')} is {m('(x_1, y_1) = (2, 1)')}. "
                    f"If {m('(x_3, y_3)')} is the **third** positive integer solution, what is {m('x_3 + y_3')}?"
                ),
                q_ar=(
                    f"الحل الأساسي الموجب لمعادلة بيل {m('x^2 - 3y^2 = 1')} هو {m('(x_1, y_1) = (2, 1)')}. "
                    f"إذا كان {m('(x_3, y_3)')} هو الحل الصحيح الموجب **الثالث**، فما قيمة {m('x_3 + y_3')}؟"
                ),
                correct_val=41,
                distractors=[11, 26, 37, 52],
                idea_en="Expand (2 + √3)³ = x_3 + y_3√3 and add x_3 + y_3.",
                steps_en=[
                    f"Compute {m('(2 + \\sqrt{3})^2 = 7 + 4\\sqrt{3}')}, so the second solution is {m('(x_2, y_2) = (7, 4)')}.",
                    f"Multiply by {m('2 + \\sqrt{3}')}: {m('(7 + 4\\sqrt{3})(2 + \\sqrt{3}) = (14 + 12) + (7 + 8)\\sqrt{3} = 26 + 15\\sqrt{3}')}.",
                    f"Thus {m('(x_3, y_3) = (26, 15)')}, and {m('x_3 + y_3 = 26 + 15 = 41')}.",
                ],
                check_en=f"Verify Pell's equation: {m('26^2 - 3(15^2) = 676 - 675 = 1')}.",
                idea_ar="فكّ القوة (2 + √3)³ = x_3 + y_3√3 ثم اجمع x_3 + y_3.",
                steps_ar=[
                    f"الحل الثاني ينتج من {m('(2 + \\sqrt{3})^2 = 7 + 4\\sqrt{3}')}.",
                    f"الحل الثالث ينتج من {m('(7 + 4\\sqrt{3})(2 + \\sqrt{3}) = 26 + 15\\sqrt{3}')}.",
                    f"إذن {m('x_3 = 26')} و{m('y_3 = 15')}، ومجموعهما {m('26 + 15 = 41')}.",
                ],
                check_ar=f"التحقق: {m('26^2 - 3(15^2) = 676 - 675 = 1')}.",
                diagram_en=svg_function_machine("(2, 1)", "(2+√3)³", "(x₃, y₃)", "x₃+y₃=?"),
            ),
        ],
        blueprints=[
            "olym_t2_nt_fermat_euler_totient",
            "olym_t2_nt_crt_simultaneous_mod",
            "olym_t2_nt_legendre_padic_fact",
            "olym_t2_nt_pell_pythagorean_dioph",
        ],
    )


def _lesson_l2_02() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-02",
        level=T2,
        unit_num="2.2",
        topic="Algebra",
        title_en="Vieta–Newton Sums, Polynomial Remainders, Functional Substitutions & Floor Equations",
        title_ar="مجاميع فييتا-نيوتن وبواقي كثيرات الحدود والمعادلات الدالية ومعادلات الجزء الصحيح",
        summary_en=(
            "Connect polynomial coefficients to power sums via Vieta and Newton's identities, "
            "reconstruct polynomial remainders, solve involution functional systems, and apply Hermite's floor identity."
        ),
        summary_ar=(
            "ربط معاملات كثيرات الحدود بمجاميع القوى عبر متطابقات فييتا ونيوتن، "
            "وإيجاد بواقي قسمة كثيرات الحدود، وحل المعادلات الدالية، وتطبيق متطابقة هيرميت للجزء الصحيح."
        ),
        goals_en=[
            f"Relate elementary symmetric polynomials to power sums {m('P_k = \\sum r_i^k')} via Newton's sums.",
            f"Determine linear and quadratic remainders {m('R(x) = ax + b')} using the Remainder and Factor Theorems.",
            f"Solve functional equations such as {m('a f(x) + b f(1/x) = g(x)')} by involution substitution.",
            f"Solve floor/fractional-part equations using {m('x = \\lfloor x \\rfloor + \\{x\\}')} and Hermite's identity.",
        ],
        goals_ar=[
            f"ربط كثيرات الحدود المتماثلة الابتدائية بمجاميع القوى {m('P_k = \\sum r_i^k')} عبر متطابقات نيوتن.",
            f"إيجاد باقي القسمة {m('R(x) = ax + b')} باستخدام مبرهنتي الباقي والعامل.",
            f"حل المعادلات الدالية من النمط {m('a f(x) + b f(1/x) = g(x)')} بتعويض الدالة العكسية.",
            f"حل معادلات الجزء الصحيح والكسري باستخدام {m('x = \\lfloor x \\rfloor + \\{x\\}')} ومتطابقة هيرميت.",
        ],
        concepts=[
            olym_concept(
                title_en="Vieta's Formulas & Newton's Power-Sum Recurrence",
                title_ar="صيغ فييتا وعلاقة نيوتن التراجعية لمجاميع القوى",
                body_en=(
                    f"For {m('x^3 - e_1 x^2 + e_2 x - e_3 = 0')} with roots {m('r_1, r_2, r_3')}, Vieta gives {m('e_1, e_2, e_3')}, "
                    f"and Newton's identities compute {m('P_k = r_1^k + r_2^k + r_3^k')} recursively without solving for the roots."
                ),
                body_ar=(
                    f"لكثيرة الحدود {m('x^3 - e_1 x^2 + e_2 x - e_3 = 0')} ذات الجذور {m('r_1, r_2, r_3')}، تعطي صيغ فييتا القيم {m('e_1, e_2, e_3')}، "
                    f"وتحسب متطابقات نيوتن مجاميع القوى {m('P_k = r_1^k + r_2^k + r_3^k')} تراجعياً دون إيجاد الجذور منفردة."
                ),
                rule_en=dm(r"P_1 = e_1, \quad P_2 = e_1 P_1 - 2e_2, \quad P_3 = e_1 P_2 - e_2 P_1 + 3e_3"),
                rule_ar=dm(r"P_1 = e_1, \quad P_2 = e_1 P_1 - 2e_2, \quad P_3 = e_1 P_2 - e_2 P_1 + 3e_3"),
                diagram_en=svg_parabola_roots("r₁", "r₂", "Σrᵢᵏ"),
            ),
            olym_concept(
                title_en="Polynomial Division & Involution Functional Systems",
                title_ar="قسمة كثيرات الحدود والأنظمة الدالية الانعكاسية",
                body_en=(
                    f"Dividing {m('P(x)')} by {m('(x-a)(x-b)')} leaves a linear remainder {m('R(x) = mx + c')} satisfying {m('R(a)=P(a)')} and {m('R(b)=P(b)')}. "
                    f"In functional equations with {m('f(x)')} and {m('f(1-x)')} or {m('f(1/x)')}, substitute the involution to get a {m('2 \\times 2')} linear system."
                ),
                body_ar=(
                    f"قسمة {m('P(x)')} على {m('(x-a)(x-b)')} تترك باقياً خطياً {m('R(x) = mx + c')} يحقق {m('R(a)=P(a)')} و{m('R(b)=P(b)')}. "
                    f"وفي المعادلات الدالية التي تحوي {m('f(x)')} و{m('f(1-x)')} أو {m('f(1/x)')} نعوّض التحويل العكسي للحصول على نظام خطي."
                ),
                rule_en=dm(r"P(x) = (x-a)(x-b)Q(x) + mx + c, \qquad \begin{cases} a f(x) + b f(1/x) = g(x) \\ b f(x) + a f(1/x) = g(1/x) \end{cases}"),
                rule_ar=dm(r"P(x) = (x-a)(x-b)Q(x) + mx + c, \qquad \begin{cases} a f(x) + b f(1/x) = g(x) \\ b f(x) + a f(1/x) = g(1/x) \end{cases}"),
                diagram_en=svg_olym_func_mapping(["x", "1/x", "1−x"], ["f(x)", "f(1/x)", "?"], "Involution Pair"),
            ),
            olym_concept(
                title_en="Floor Decomposition & Hermite's Identity",
                title_ar="تحليل الجزء الصحيح ومتطابقة هيرميت",
                body_en=(
                    f"Every real {m('x')} decomposes uniquely as {m('x = \\lfloor x \\rfloor + \\{x\\}')} with {m('\\lfloor x \\rfloor \\in \\mathbb{Z}')} and {m('0 \\le \\{x\\} < 1')}. "
                    f"Hermite's identity sums shifted floors into a single floor."
                ),
                body_ar=(
                    f"كل عدد حقيقي {m('x')} يكتب بصورة وحيدة {m('x = \\lfloor x \\rfloor + \\{x\\}')} حيث {m('\\lfloor x \\rfloor \\in \\mathbb{Z}')} و{m('0 \\le \\{x\\} < 1')}. "
                    f"وتجمع متطابقة هيرميت الأجزاء الصحيحة المزاحة في حد واحد."
                ),
                rule_en=dm(r"\sum_{k=0}^{n-1} \left\lfloor x + \frac{k}{n} \right\rfloor = \lfloor nx \rfloor"),
                rule_ar=dm(r"\sum_{k=0}^{n-1} \left\lfloor x + \frac{k}{n} \right\rfloor = \lfloor nx \rfloor"),
                diagram_en=svg_number_strip(["⌊x⌋", "⌊x+1/n⌋", "…", "⌊nx⌋"]),
            ),
        ],
        traps_en=[
            f"Writing {m('e_2 = c/a')} with the wrong sign on a cubic {m('x^3 + px^2 + qx + r = 0')} where {m('r_1 + r_2 + r_3 = -p')} and {m('r_1 r_2 r_3 = -r')}.",
            f"Assuming the remainder of {m('P(x)')} modulo {m('(x-a)(x-b)')} is constant rather than linear {m('mx + c')}.",
            f"Forgetting the strict upper bound {m('\\{x\\} < 1')} when counting solutions to floor equations.",
        ],
        traps_ar=[
            f"الخطأ في إشارات صيغ فييتا لكثيرة الحدود التكعيبية {m('x^3 + px^2 + qx + r = 0')} حيث {m('r_1+r_2+r_3 = -p')} و{m('r_1 r_2 r_3 = -r')}.",
            f"افتراض أن باقي القسمة على {m('(x-a)(x-b)')} ثابت بدلاً من كونه خطياً {m('mx + c')}.",
            f"نسيان المتباينة الصارمة {m('\\{x\\} < 1')} عند حصر حلول معادلات الجزء الصحيح.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-02-EX1",
                title_en="Cubic Power Sum via Vieta and Newton's Sums",
                title_ar="مجموع مكعبات الجذور عبر صيغ فييتا ونيوتن",
                q_en=(
                    f"Let {m('r_1, r_2, r_3')} be the roots of {m('x^3 - 4x^2 + 3x - 5 = 0')}. "
                    f"What is the value of {m('r_1^3 + r_2^3 + r_3^3')}?"
                ),
                q_ar=(
                    f"ليكن {m('r_1, r_2, r_3')} جذور المعادلة {m('x^3 - 4x^2 + 3x - 5 = 0')}. "
                    f"ما قيمة {m('r_1^3 + r_2^3 + r_3^3')}؟"
                ),
                correct_val=43,
                distractors=[28, 37, 40, 49],
                idea_en="Compute P_1, P_2, and P_3 sequentially using Newton's power-sum identities.",
                steps_en=[
                    f"By Vieta's formulas, {m('e_1 = 4')}, {m('e_2 = 3')}, and {m('e_3 = 5')}.",
                    f"Compute {m('P_1 = e_1 = 4')} and {m('P_2 = e_1 P_1 - 2e_2 = 4(4) - 2(3) = 10')}.",
                    f"Then {m('P_3 = e_1 P_2 - e_2 P_1 + 3e_3 = 4(10) - 3(4) + 3(5) = 40 - 12 + 15 = 43')}.",
                ],
                check_en=f"Equivalently, since {m('r_i^3 = 4r_i^2 - 3r_i + 5')}, summing gives {m('4(10) - 3(4) + 15 = 43')}.",
                idea_ar="احسب P_1 ثم P_2 ثم P_3 بالتتابع باستخدام متطابقات نيوتن.",
                steps_ar=[
                    f"من صيغ فييتا: {m('e_1 = 4')} و{m('e_2 = 3')} و{m('e_3 = 5')}.",
                    f"نجد {m('P_1 = 4')} و{m('P_2 = 4^2 - 2(3) = 10')}.",
                    f"ومن متطابقة نيوتن: {m('P_3 = 4(10) - 3(4) + 3(5) = 43')}.",
                ],
                check_ar=f"بجمع {m('r_i^3 = 4r_i^2 - 3r_i + 5')} نحصل مباشرة على {m('4(10) - 12 + 15 = 43')}.",
                diagram_en=svg_parabola_roots("e₁=4", "e₂=3", "P₃=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-02-EX2",
                title_en="Linear Remainder Modulo a Quadratic Divisor",
                title_ar="الباقي الخطي عند القسمة على مقسوم تربيعي",
                q_en=(
                    f"A polynomial {m('P(x)')} leaves remainder {m('5')} when divided by {m('x - 1')} and remainder {m('13')} when divided by {m('x - 3')}. "
                    f"If {m('R(x)')} is the remainder when {m('P(x)')} is divided by {m('(x - 1)(x - 3)')}, what is {m('R(6)')}?"
                ),
                q_ar=(
                    f"كثيرة حدود {m('P(x)')} باقي قسمتها على {m('x - 1')} يساوي {m('5')}، وباقي قسمتها على {m('x - 3')} يساوي {m('13')}. "
                    f"إذا كان {m('R(x)')} هو باقي قسمة {m('P(x)')} على {m('(x - 1)(x - 3)')}، فما قيمة {m('R(6)')}؟"
                ),
                correct_val=25,
                distractors=[21, 23, 27, 29],
                idea_en="Set R(x) = mx + c and use R(1) = 5 and R(3) = 13.",
                steps_en=[
                    f"Write {m('P(x) = (x-1)(x-3)Q(x) + mx + c')}, where {m('R(x) = mx + c')}.",
                    f"Evaluating at {m('x = 1')} and {m('x = 3')} gives {m('m + c = 5')} and {m('3m + c = 13')}.",
                    f"Subtracting yields {m('2m = 8 \\implies m = 4')} and {m('c = 1')}, so {m('R(x) = 4x + 1')} and {m('R(6) = 25')}.",
                ],
                check_en=f"Check: {m('R(1) = 5')} and {m('R(3) = 13')}, both matching the given remainders.",
                idea_ar="افرض الباقي الخطي R(x) = mx + c وعوّض x = 1 وx = 3.",
                steps_ar=[
                    f"نفرض {m('R(x) = mx + c')}، فيكون {m('m + c = 5')} و{m('3m + c = 13')}.",
                    f"بالطرح نجد {m('m = 4')} و{m('c = 1')}، أي {m('R(x) = 4x + 1')}، ومنه {m('R(6) = 25')}.",
                ],
                check_ar=f"التحقق: {m('R(1) = 5')} و{m('R(3) = 13')}.",
                diagram_en=svg_function_machine("R(x)=mx+c", "R(1)=5", "R(3)=13", "R(6)=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-02-EX3",
                title_en="Involution Substitution in a Functional Equation",
                title_ar="حل معادلة دالية بالتعويض العكسي",
                q_en=(
                    f"A function {m('f: \\mathbb{R}\\setminus\\{0\\} \\to \\mathbb{R}')} satisfies {m('3f(x) + 2f(1/x) = 5x')} for all {m('x \\ne 0')}. "
                    f"What is the value of {m('f(2)')}?"
                ),
                q_ar=(
                    f"دالة {m('f: \\mathbb{R}\\setminus\\{0\\} \\to \\mathbb{R}')} تحقق {m('3f(x) + 2f(1/x) = 5x')} لكل {m('x \\ne 0')}. "
                    f"ما قيمة {m('f(2)')}؟"
                ),
                correct_val=4,
                distractors=[3, 5, 6, 2],
                idea_en="Substitute x = 2 and x = 1/2 to get two linear equations in f(2) and f(1/2).",
                steps_en=[
                    f"For {m('x = 2')}: {m('3f(2) + 2f(1/2) = 10')}.",
                    f"For {m('x = 1/2')}: {m('3f(1/2) + 2f(2) = 5/2')}.",
                    f"Multiply the first equation by {m('3')} and the second by {m('2')}, then subtract: {m('5f(2) = 30 - 5 = 25 - 5 = 20 \\implies f(2) = 4')}.",
                ],
                check_en=f"From {m('f(2) = 4')} we get {m('f(1/2) = -1')}, and {m('3(-1) + 2(4) = 5 = 5(1/2)\\cdot 2')}.",
                idea_ar="عوّض x = 2 وx = 1/2 لتكوين معادلتين خطيتين في f(2) وf(1/2).",
                steps_ar=[
                    f"عند {m('x = 2')} نحصل على {m('3f(2) + 2f(1/2) = 10')}.",
                    f"وعند {m('x = 1/2')} نحصل على {m('2f(2) + 3f(1/2) = 5/2')}.",
                    f"بحذف {m('f(1/2)')} نجد {m('5f(2) = 30 - 5 = 20')}، ومنه {m('f(2) = 4')}.",
                ],
                check_ar=f"بالتعويض العكسي نجد {m('f(1/2) = -1')} وتتحقق المعادلتان معاً.",
                diagram_en=svg_olym_func_mapping(["x = 2", "x = 1/2"], ["f(2) = ?", "f(1/2)"], "3f(x)+2f(1/x)=5x"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-02-EX4",
                title_en="Hermite's Floor Sum Evaluation",
                title_ar="حساب مجموع الأجزاء الصحيحة بمتطابقة هيرميت",
                q_en=(
                    f"Evaluate the sum {m('S = \\sum_{k=0}^{9} \\left\\lfloor \\frac{17}{4} + \\frac{k}{10} \\right\\rfloor')}."
                ),
                q_ar=(
                    f"احسب قيمة المجموع {m('S = \\sum_{k=0}^{9} \\left\\lfloor \\frac{17}{4} + \\frac{k}{10} \\right\\rfloor')}."
                ),
                correct_val=42,
                distractors=[40, 41, 43, 45],
                idea_en="Apply Hermite's identity with x = 17/4 and n = 10: the sum equals ⌊10x⌋.",
                steps_en=[
                    f"By Hermite's identity, {m('\\sum_{k=0}^{n-1} \\lfloor x + k/n \\rfloor = \\lfloor nx \\rfloor')}.",
                    f"Here {m('n = 10')} and {m('x = 17/4 = 4.25')}, so {m('nx = 10 \\times 4.25 = 42.5')}.",
                    f"Therefore {m('S = \\lfloor 42.5 \\rfloor = 42')}.",
                ],
                check_en=f"Direct check: for {m('k = 0,\\dots,7')}, {m('\\lfloor 4.25 + k/10 \\rfloor = 4')} (8 terms); for {m('k = 8, 9')}, it is {m('5')} (2 terms); {m('8(4) + 2(5) = 42')}.",
                idea_ar="طبّق متطابقة هيرميت حيث x = 17/4 وn = 10 فيكون المجموع مساوياً لـ ⌊10x⌋.",
                steps_ar=[
                    f"حسب متطابقة هيرميت: {m('\\sum_{k=0}^{9} \\lfloor x + k/10 \\rfloor = \\lfloor 10x \\rfloor')}.",
                    f"بالتعويض عن {m('x = 17/4 = 4.25')} نجد {m('S = \\lfloor 42.5 \\rfloor = 42')}.",
                ],
                check_ar=f"التحقق المباشر: {m('8')} حدود قيمتها {m('4')} وحدّان قيمتهما {m('5')}، والمجموع {m('32 + 10 = 42')}.",
                diagram_en=svg_number_strip(["k=0..7: 4", "k=8..9: 5", "⌊10x⌋=?"]),
            ),
        ],
        blueprints=[
            "olym_t2_alg_vieta_newton_sums",
            "olym_t2_alg_polynomial_remainders",
            "olym_t2_alg_functional_substitutions",
            "olym_t2_alg_floor_hermite_eqs",
        ],
    )


def _lesson_l2_03() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-03",
        level=T2,
        unit_num="2.3",
        topic="Inequalities",
        title_en="Weighted AM–GM, Cauchy–Schwarz / Titu's Lemma, Nesbitt & Rearrangement",
        title_ar="متباينة الوسطين الموزونة وكوشي-شوارتز (تيتو) ونسبيت والترتيب",
        summary_en=(
            "Optimize algebraic expressions using weighted AM–GM term splitting, Cauchy–Schwarz in Engel/Titu form, "
            "Nesbitt and cyclic substitutions, and the Rearrangement and Chebyshev inequalities."
        ),
        summary_ar=(
            "تحسين العبارات الجبرية عبر تجزئة الحدود في متباينة الوسطين، وصورة تيتو لمتباينة كوشي-شوارتز، "
            "ومتباينة نسبيت والمجاميع الدورية، ومتباينتي الترتيب وتشيبيشيف."
        ),
        goals_en=[
            f"Split terms with equal weights to match exponents in {m('n')}-variable AM–GM.",
            f"Bound sums of fractions using Titu's Lemma {m('\\sum \\frac{u_i^2}{v_i} \\ge \\frac{(\\sum u_i)^2}{\\sum v_i}')}.",
            f"Prove and evaluate cyclic fractional bounds including Nesbitt's inequality {m('\\ge 3/2')}.",
            f"Pair sorted sequences via the Rearrangement Inequality to find exact maxima and minima.",
        ],
        goals_ar=[
            f"تجزئة الحدود بأوزان متساوية لموازنة الأسس في متباينة الوسط الحسابي والهندسي.",
            f"تقدير مجاميع الكسور باستخدام توطئة تيتو {m('\\sum \\frac{u_i^2}{v_i} \\ge \\frac{(\\sum u_i)^2}{\\sum v_i}')}.",
            f"إثبات وحساب الحدود الدورية للكسور بما فيها متباينة نسبيت {m('\\ge 3/2')}.",
            f"مزاوجة المتتاليات المرتبة عبر متباينة الترتيب لإيجاد القيم العظمى والصغرى.",
        ],
        concepts=[
            olym_concept(
                title_en="Weighted AM–GM via Equal-Term Splitting",
                title_ar="متباينة الوسطين الموزونة عبر تجزئة الحدود",
                body_en=(
                    f"To minimize {m('x^2 + \\frac{2a}{x}')} for {m('x > 0')}, split the reciprocal into two equal pieces "
                    f"{m('x^2 + \\frac{a}{x} + \\frac{a}{x}')} so the product {m('x^2 \\cdot \\frac{a}{x} \\cdot \\frac{a}{x} = a^2')} is constant."
                ),
                body_ar=(
                    f"لتصغير {m('x^2 + \\frac{2a}{x}')} عند {m('x > 0')}، نجزّئ الحد الكسري إلى جزأين متساويين "
                    f"{m('x^2 + \\frac{a}{x} + \\frac{a}{x}')} بحيث يصبح الجداء {m('x^2 \\cdot \\frac{a}{x} \\cdot \\frac{a}{x} = a^2')} ثابتاً."
                ),
                rule_en=dm(r"x^2 + \frac{a}{x} + \frac{a}{x} \ge 3\sqrt[3]{x^2 \cdot \frac{a}{x} \cdot \frac{a}{x}} = 3a^{2/3}"),
                rule_ar=dm(r"x^2 + \frac{a}{x} + \frac{a}{x} \ge 3\sqrt[3]{x^2 \cdot \frac{a}{x} \cdot \frac{a}{x}} = 3a^{2/3}"),
                diagram_en=svg_olym_inequality_curve("x²", "a/x + a/x", "3-term AM–GM"),
            ),
            olym_concept(
                title_en="Cauchy–Schwarz & Titu's Lemma (Engel Form)",
                title_ar="متباينة كوشي-شوارتز وتوطئة تيتو",
                body_en=(
                    f"For any reals {m('u_i')} and positive reals {m('v_i')}, Titu's Lemma bounds the sum of ratios from below "
                    f"by the square of the sum of numerators divided by the sum of denominators."
                ),
                body_ar=(
                    f"لأي أعداد حقيقية {m('u_i')} وأعداد حقيقية موجبة {m('v_i')}، تعطي توطئة تيتو حداً أدنى لمجموع الكسور "
                    f"بدلالة مربع مجموع البسوط مقسوماً على مجموع المقامات."
                ),
                rule_en=dm(r"\sum_{i=1}^{n} \frac{u_i^2}{v_i} \ge \frac{(u_1 + u_2 + \cdots + u_n)^2}{v_1 + v_2 + \cdots + v_n}"),
                rule_ar=dm(r"\sum_{i=1}^{n} \frac{u_i^2}{v_i} \ge \frac{(u_1 + u_2 + \cdots + u_n)^2}{v_1 + v_2 + \cdots + v_n}"),
                diagram_en=svg_olym_inequality_curve("Σ uᵢ²/vᵢ", "(Σuᵢ)²/Σvᵢ", "Titu's Lemma"),
            ),
            olym_concept(
                title_en="Nesbitt's Inequality & Rearrangement Ordering",
                title_ar="متباينة نسبيت ومتباينة الترتيب",
                body_en=(
                    f"For positive {m('a, b, c')}, Nesbitt's inequality states {m('\\sum_{\\text{cyc}} \\frac{a}{b+c} \\ge \\frac{3}{2}')}. "
                    f"For sorted sequences {m('a_1 \\le \\cdots \\le a_n')} and {m('b_1 \\le \\cdots \\le b_n')}, same-order pairing maximizes {m('\\sum a_i b_{\\pi(i)}')} and opposite-order pairing minimizes it."
                ),
                body_ar=(
                    f"للأعداد الموجبة {m('a, b, c')}، تنص متباينة نسبيت على أن {m('\\sum_{\\text{cyc}} \\frac{a}{b+c} \\ge \\frac{3}{2}')}. "
                    f"وللمتتاليتين المرتبتين، يتحقق أكبر مجموع جداءات عند الترتيب المتوافق وأصغر مجموع عند الترتيب المتعاكس."
                ),
                rule_en=dm(r"\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \ge \frac{3}{2}, \qquad \sum a_i b_{n+1-i} \le \sum a_i b_{\pi(i)} \le \sum a_i b_i"),
                rule_ar=dm(r"\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \ge \frac{3}{2}, \qquad \sum a_i b_{n+1-i} \le \sum a_i b_{\pi(i)} \le \sum a_i b_i"),
                diagram_en=svg_bar_chart([("a₁b₁", 2, "2"), ("a₂b₂", 6, "6"), ("a₃b₃", 12, "12"), ("Max", 20, "20")], y_max=22),
            ),
        ],
        traps_en=[
            f"Splitting {m('x^2 + 16/x')} as {m('(x^2) + (16/x)')} (2-term AM–GM), where {m('x')} does not cancel and equality fails to match.",
            f"Applying Titu's Lemma when denominators {m('v_i')} can be negative.",
            f"Pairing largest with largest when asked to **minimize** {m('\\sum a_i b_{\\pi(i)}')}.",
        ],
        traps_ar=[
            f"تطبيق متباينة الوسطين لحدين فقط على {m('x^2 + 16/x')} دون تجزئة الكسر إلى حدين متساويين لإلغاء {m('x')}.",
            f"استعمال توطئة تيتو عندما لا تكون المقامات {m('v_i')} موجبة تماماً.",
            f"مزاوجة الأكبر مع الأكبر عندما يكون المطلوب **تصغير** المجموع بدلاً من تعظيمه.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-03-EX1",
                title_en="Three-Term AM–GM Term Splitting",
                title_ar="تجزئة الحدود إلى ثلاثة حدود في متباينة الوسطين",
                q_en=(
                    f"For all positive real numbers {m('x > 0')}, what is the **minimum** value of {m('f(x) = x^2 + \\frac{54}{x}')}?"
                ),
                q_ar=(
                    f"لجميع الأعداد الحقيقية الموجبة {m('x > 0')}، ما **أصغر** قيمة ممكنة للمقدار {m('f(x) = x^2 + \\frac{54}{x}')}؟"
                ),
                correct_val=27,
                distractors=[18, 24, 30, 36],
                idea_en="Split 54/x into 27/x + 27/x and apply 3-term AM-GM.",
                steps_en=[
                    f"Write {m('f(x) = x^2 + \\frac{27}{x} + \\frac{27}{x}')}.",
                    f"By 3-term AM–GM, {m('x^2 + \\frac{27}{x} + \\frac{27}{x} \\ge 3\\sqrt[3]{x^2 \\cdot \\frac{27}{x} \\cdot \\frac{27}{x}} = 3\\sqrt[3]{729} = 27')}.",
                    f"Equality holds when {m('x^2 = 27/x \\implies x = 3')}.",
                ],
                check_en=f"At {m('x = 3')}, {m('f(3) = 9 + 54/3 = 27')}.",
                idea_ar="جزّئ 54/x إلى 27/x + 27/x وطبّق متباينة الوسطين لثلاثة حدود.",
                steps_ar=[
                    f"نكتب {m('f(x) = x^2 + \\frac{27}{x} + \\frac{27}{x}')}.",
                    f"من متباينة الوسطين لثلاثة حدود: {m('f(x) \\ge 3\\sqrt[3]{x^2 \\cdot \\frac{27}{x} \\cdot \\frac{27}{x}} = 3 \\times 9 = 27')}.",
                    f"وتتحقق المساواة عند {m('x = 3')}.",
                ],
                check_ar=f"عند {m('x = 3')} يكون {m('3^2 + 54/3 = 27')}.",
                diagram_en=svg_olym_inequality_curve("x²", "27/x + 27/x", "min = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-03-EX2",
                title_en="Weighted Fractional Minimum via Titu's Lemma",
                title_ar="أصغر قيمة لمجموع كسري بتوطئة تيتو",
                q_en=(
                    f"Positive real numbers {m('x, y, z')} satisfy {m('x + y + z = 12')}. "
                    f"What is the **minimum** possible value of {m('\\frac{4}{x} + \\frac{16}{y} + \\frac{36}{z}')}?"
                ),
                q_ar=(
                    f"أعداد حقيقية موجبة {m('x, y, z')} تحقق {m('x + y + z = 12')}. "
                    f"ما **أصغر** قيمة ممكنة للمقدار {m('\\frac{4}{x} + \\frac{16}{y} + \\frac{36}{z}')}؟"
                ),
                correct_val=12,
                distractors=[9, 10, 14, 16],
                idea_en="Write the numerators as 2², 4², 6² and apply Titu's Lemma.",
                steps_en=[
                    f"By Titu's Lemma, {m('\\frac{2^2}{x} + \\frac{4^2}{y} + \\frac{6^2}{z} \\ge \\frac{(2 + 4 + 6)^2}{x + y + z}')}.",
                    f"Substitute {m('x + y + z = 12')}: the minimum value is {m('\\frac{12^2}{12} = \\frac{144}{12} = 12')}.",
                ],
                check_en=f"Equality holds at {m('(x, y, z) = (2, 4, 6)')}, where {m('4/2 + 16/4 + 36/6 = 2 + 4 + 6 = 12')}.",
                idea_ar="اكتب البسوط على صورة مربعات كاملة وطبّق توطئة تيتو.",
                steps_ar=[
                    f"بتطبيق توطئة تيتو على {m('\\frac{2^2}{x} + \\frac{4^2}{y} + \\frac{6^2}{z}')} نجد أنه أكبر من أو يساوي {m('\\frac{(2+4+6)^2}{x+y+z}')}.",
                    f"بالتعويض عن {m('x+y+z = 12')} نحصل على {m('144 / 12 = 12')}.",
                ],
                check_ar=f"تتحقق المساواة عند {m('(x,y,z) = (2,4,6)')} حيث {m('4/2 + 16/4 + 36/6 = 12')}.",
                diagram_en=svg_olym_inequality_curve("(2+4+6)²", "x+y+z=12", "min = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-03-EX3",
                title_en="Shifted Nesbitt Cyclic Sum",
                title_ar="مجموع دوري مشتق من متباينة نسبيت",
                q_en=(
                    f"For positive real numbers {m('a, b, c')}, what is the **minimum** possible value of "
                    f"{m('S = \\frac{2a + b + c}{b + c} + \\frac{2b + c + a}{c + a} + \\frac{2c + a + b}{a + b}')}?"
                ),
                q_ar=(
                    f"للأعداد الحقيقية الموجبة {m('a, b, c')}، ما **أصغر** قيمة ممكنة للمقدار "
                    f"{m('S = \\frac{2a + b + c}{b + c} + \\frac{2b + c + a}{c + a} + \\frac{2c + a + b}{a + b}')}؟"
                ),
                correct_val=6,
                distractors=[Fraction(9, 2), 5, Fraction(15, 2), 9],
                idea_en="Split each fraction as 2a/(b+c) + 1 and apply Nesbitt's inequality ≥ 3/2.",
                steps_en=[
                    f"Rewrite each term: {m('\\frac{2a + b + c}{b + c} = \\frac{2a}{b + c} + 1')}.",
                    f"Summing cyclically gives {m('S = 2\\left(\\frac{a}{b+c} + \\frac{b}{c+a} + \\frac{c}{a+b}\\right) + 3')}.",
                    f"By Nesbitt's inequality, the bracketed sum is at least {m('3/2')}, so {m('S \\ge 2 \\cdot \\frac{3}{2} + 3 = 6')}.",
                ],
                check_en=f"At {m('a = b = c = 1')}, each fraction equals {m('4/2 = 2')}, giving {m('2 + 2 + 2 = 6')}.",
                idea_ar="افصل كل كسر إلى 2a/(b+c) + 1 ثم طبّق متباينة نسبيت.",
                steps_ar=[
                    f"نكتب كل حد على الصورة {m('\\frac{2a}{b+c} + 1')}.",
                    f"بجمع الحدود الثلاثة: {m('S = 2\\sum \\frac{a}{b+c} + 3 \\ge 2\\left(\\frac{3}{2}\\right) + 3 = 6')}.",
                ],
                check_ar=f"عند {m('a=b=c=1')} يكون المجموع {m('2 + 2 + 2 = 6')}.",
                diagram_en=svg_olym_inequality_curve("2·Nesbitt", "+ 3", "min = ?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-03-EX4",
                title_en="Rearrangement Inequality Dot-Product Difference",
                title_ar="الفرق بين القيمتين العظمى والصغرى بمتباينة الترتيب",
                q_en=(
                    f"Let {m('(b_1, b_2, b_3, b_4)')} be a permutation of {m('(2, 5, 8, 11)')}. "
                    f"As the permutation varies, what is the difference {m('M - m')} between the maximum value {m('M')} "
                    f"and the minimum value {m('m')} of {m('1\\cdot b_1 + 3\\cdot b_2 + 6\\cdot b_3 + 10\\cdot b_4')}?"
                ),
                q_ar=(
                    f"ليكن {m('(b_1, b_2, b_3, b_4)')} تبديلاً للأعداد {m('(2, 5, 8, 11)')}. "
                    f"ما الفرق {m('M - m')} بين أكبر قيمة ممكنة {m('M')} وأصغر قيمة ممكنة {m('m')} للمقدار "
                    f"{m('1\\cdot b_1 + 3\\cdot b_2 + 6\\cdot b_3 + 10\\cdot b_4')}؟"
                ),
                correct_val=90,
                distractors=[72, 81, 84, 96],
                idea_en="By the Rearrangement Inequality, M pairs (1,3,6,10) with (2,5,8,11) in the same order and m pairs them in reverse order.",
                steps_en=[
                    f"Same-order maximum: {m('M = 1(2) + 3(5) + 6(8) + 10(11) = 2 + 15 + 48 + 110 = 175')}.",
                    f"Reverse-order minimum: {m('m = 1(11) + 3(8) + 6(5) + 10(2) = 11 + 24 + 30 + 20 = 85')}.",
                    f"The difference is {m('M - m = 175 - 85 = 90')}.",
                ],
                check_en=f"All {m('4! = 24')} permutations yield values in {m('[85, 175]')}, so {m('M - m = 90')}.",
                idea_ar="احسب القيمة العظمى بالترتيب المتوافق والقيمة الصغرى بالترتيب المتعاكس ثم اطرحهما.",
                steps_ar=[
                    f"القيمة العظمى بالترتيب المتوافق: {m('M = 1(2) + 3(5) + 6(8) + 10(11) = 175')}.",
                    f"القيمة الصغرى بالترتيب المتعاكس: {m('m = 1(11) + 3(8) + 6(5) + 10(2) = 85')}.",
                    f"الفرق بينهما: {m('M - m = 175 - 85 = 90')}.",
                ],
                check_ar=f"التحقق الشامل لجميع التباديل الـ 24 يؤكد أن المدى هو {m('175 - 85 = 90')}.",
                diagram_en=svg_bar_chart([("m", 85, "85"), ("M", 175, "175"), ("M−m", 90, "?")], y_max=190),
            ),
        ],
        blueprints=[
            "olym_t2_ineq_weighted_amgm",
            "olym_t2_ineq_cauchy_titu_lemma",
            "olym_t2_ineq_nesbitt_cyclic_sums",
            "olym_t2_ineq_rearrangement_chebyshev",
        ],
    )



def _lesson_l2_04() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-04",
        level=T2,
        unit_num="2.4",
        topic="Geometry",
        title_en="Power of a Point, Ptolemy, Ceva–Menelaus & Stewart's Theorem",
        title_ar="قوة النقطة ومبرهنة بطليموس وسيفا-منيلاوس وستيوارت",
        summary_en=(
            "Compute chord and secant products via Power of a Point and radical axes, "
            "apply Ptolemy's theorem in cyclic quadrilaterals, chase ratios with Ceva and Menelaus, and find cevian lengths via Stewart's theorem."
        ),
        summary_ar=(
            "حساب جداءات الأوتار والقواطع عبر قوة النقطة والمحور الأساسي، "
            "وتطبيق مبرهنة بطليموس في الرباعيات الدائرية، وملاحقة النسب بمبرهنتي سيفا ومنيلاوس، وإيجاد أطوال القطع السيفية بمبرهنة ستيوارت."
        ),
        goals_en=[
            f"Evaluate the power of a point {m('\\operatorname{Pow}_\\omega(P) = PO^2 - R^2 = PT^2 = PA \\cdot PB')} and locate radical axes.",
            f"Relate sides and diagonals of a cyclic quadrilateral via Ptolemy's identity {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            f"Solve collinearity and concurrency ratio problems using Menelaus's and Ceva's theorems.",
            f"Compute cevian, median, and angle-bisector lengths using Stewart's formula {m('man + dad = bmb + cnc')}.",
        ],
        goals_ar=[
            f"حساب قوة النقطة {m('\\operatorname{Pow}_\\omega(P) = PO^2 - R^2 = PT^2 = PA \\cdot PB')} وتحديد المحور الأساسي.",
            f"الربط بين أضلاع وأقطار الرباعي الدائري عبر مبرهنة بطليموس {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
            f"حل مسائل التلاقي والاستقامة الواحدة باستخدام مبرهنتي سيفا ومنيلاوس.",
            f"حساب أطوال القطع السيفية والمتوسطات ومنصفات الزوايا بصيغة ستيوارت {m('man + dad = bmb + cnc')}.",
        ],
        concepts=[
            olym_concept(
                title_en="Power of a Point & The Radical Axis",
                title_ar="قوة النقطة والمحور الأساسي لدائرتين",
                body_en=(
                    f"For any line through {m('P')} meeting circle {m('\\omega(O,R)')} at {m('A, B')}, the signed product {m('PA \\cdot PB = |PO^2 - R^2|')} is constant. "
                    f"The locus of points with equal power to two non-concentric circles is a line perpendicular to {m('O_1 O_2')} called the radical axis."
                ),
                body_ar=(
                    f"لأي مستقيم يمر بالنقطة {m('P')} ويقطع الدائرة {m('\\omega(O,R)')} في {m('A, B')}، يكون الجداء {m('PA \\cdot PB = |PO^2 - R^2|')} ثابتاً. "
                    f"والمحل الهندسي للنقاط المتساوية القوة بالنسبة لدائرتين غير متحدتي المركز هو مستقيم عمودي على {m('O_1 O_2')} يُسمى المحور الأساسي."
                ),
                rule_en=dm(r"PA \cdot PB = PT^2 = PO^2 - R^2, \qquad \operatorname{Pow}_{\omega_1}(P) = \operatorname{Pow}_{\omega_2}(P)"),
                rule_ar=dm(r"PA \cdot PB = PT^2 = PO^2 - R^2, \qquad \operatorname{Pow}_{\omega_1}(P) = \operatorname{Pow}_{\omega_2}(P)"),
                diagram_en=svg_olym_radical_axis("R₁", "R₂", "PT₁ = PT₂"),
            ),
            olym_concept(
                title_en="Ptolemy's Theorem for Cyclic Quadrilaterals",
                title_ar="مبرهنة بطليموس للرباعيات الدائرية",
                body_en=(
                    f"In any cyclic quadrilateral {m('ABCD')}, the product of the diagonals equals the sum of the products of opposite sides. "
                    f"When {m('\\triangle ABC')} is equilateral on a circle and {m('P')} lies on minor arc {m('BC')}, this simplifies to {m('PA = PB + PC')}."
                ),
                body_ar=(
                    f"في أي رباعي دائري {m('ABCD')}، يساوي حاصل ضرب القطرين مجموع حاصلي ضرب كل ضلعين متقابلين. "
                    f"وعندما يكون {m('\\triangle ABC')} متطابق الأضلاع وتقع {m('P')} على القوس الأصغر {m('BC')}، تتبسط العلاقة إلى {m('PA = PB + PC')}."
                ),
                rule_en=dm(r"AC \cdot BD = AB \cdot CD + BC \cdot DA, \qquad PA = PB + PC \;\;(\triangle ABC\text{ equilateral})"),
                rule_ar=dm(r"AC \cdot BD = AB \cdot CD + BC \cdot DA, \qquad PA = PB + PC \;\;(\triangle ABC\text{ equilateral})"),
                diagram_en=svg_olym_cyclic_ptolemy("a", "b", "c", "d", "AC·BD = ac+bd"),
            ),
            olym_concept(
                title_en="Ceva, Menelaus & Stewart's Cevian Identity",
                title_ar="سيفا ومنيلاوس ومتطابقة ستيوارت للقطع السيفية",
                body_en=(
                    f"Cevians {m('AD, BE, CF')} concur iff {m('\\frac{BD}{DC}\\frac{CE}{EA}\\frac{AF}{FB} = 1')}, while collinear points on the sidelines satisfy Menelaus's product {m('= 1')}. "
                    f"For a cevian {m('d = AD')} splitting {m('a = BC')} into {m('m + n')}, Stewart's theorem gives {m('b^2 m + c^2 n = a(d^2 + mn)')}."
                ),
                body_ar=(
                    f"تتلاقى القطع السيفية {m('AD, BE, CF')} في نقطة واحدة إذا وفقط إذا كان {m('\\frac{BD}{DC}\\frac{CE}{EA}\\frac{AF}{FB} = 1')}. "
                    f"وللقطعة السيفية {m('d = AD')} التي تقسم {m('a = BC')} إلى {m('m + n')}، تعطي مبرهنة ستيوارت {m('b^2 m + c^2 n = a(d^2 + mn)')}."
                ),
                rule_en=dm(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1, \qquad b^2 m + c^2 n = a(d^2 + mn)"),
                rule_ar=dm(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1, \qquad b^2 m + c^2 n = a(d^2 + mn)"),
                diagram_en=svg_stu_ceva_triangle("BD", "DC", "CE", "EA"),
            ),
        ],
        traps_en=[
            f"Writing {m('PA \\cdot AB = PC \\cdot CD')} for secants from an external point {m('P')} instead of {m('PA \\cdot PB = PC \\cdot PD')}.",
            f"Swapping {m('m')} and {m('n')} in Stewart's theorem: {m('b^2')} multiplies the segment {m('m = BD')} non-adjacent to side {m('b = AC')}.",
            f"Using {m('BD/DC')} instead of {m('BC/DC')} when applying Menelaus's theorem to an external intersection point on line {m('BC')}.",
        ],
        traps_ar=[
            f"كتابة {m('PA \\cdot AB = PC \\cdot CD')} للقواطع من نقطة خارجية {m('P')} بدلاً من {m('PA \\cdot PB = PC \\cdot PD')}.",
            f"عكس الجزأين {m('m')} و{m('n')} في مبرهنة ستيوارت؛ إذ يُضرب {m('b^2')} في الجزء {m('m = BD')} البعيد عن الضلع {m('b = AC')}.",
            f"استعمال {m('BD/DC')} بدلاً من {m('BC/DC')} عند تطبيق مبرهنة منيلاوس مع نقطة تقاطع خارجية على امتداد {m('BC')}.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-04-EX1",
                title_en="Secant–Tangent Power of an External Point",
                title_ar="قوة نقطة خارجية لمماس وقاطع",
                q_en=(
                    f"From an external point {m('P')}, a tangent {m('PT')} to a circle has length {m('12')}, "
                    f"and a secant from {m('P')} meets the circle at {m('A')} and {m('B')} with {m('PA = 9')}. What is the chord length {m('AB')}?"
                ),
                q_ar=(
                    f"من نقطة خارجية {m('P')}، رُسم مماس {m('PT')} لدائرة طوله {m('12')}، "
                    f"وقاطع يمر بالنقطة {m('P')} ويقطع الدائرة في {m('A')} و{m('B')} بحيث {m('PA = 9')}. ما طول الوتر {m('AB')}؟"
                ),
                correct_val=7,
                distractors=[6, 8, 9, 16],
                idea_en="Apply PT² = PA · PB to find PB, then subtract PA to get chord AB.",
                steps_en=[
                    f"By Power of a Point, {m('PT^2 = PA \\cdot PB')}, so {m('12^2 = 9 \\cdot PB \\implies PB = 144 / 9 = 16')}.",
                    f"Since {m('A')} lies between {m('P')} and {m('B')}, the chord length is {m('AB = PB - PA = 16 - 9 = 7')}.",
                ],
                check_en=f"Check: {m('PA \\cdot PB = 9 \\times (9 + 7) = 144 = 12^2')}.",
                idea_ar="طبّق علاقة القوة PT² = PA · PB لإيجاد PB ثم اطرح PA للحصول على طول الوتر AB.",
                steps_ar=[
                    f"من قوة النقطة: {m('PT^2 = PA \\cdot PB \\implies 144 = 9 \\cdot PB \\implies PB = 16')}.",
                    f"إذن طول الوتر هو {m('AB = PB - PA = 16 - 9 = 7')}.",
                ],
                check_ar=f"التحقق: {m('9 \\times (9 + 7) = 144 = 12^2')}.",
                diagram_en=svg_power_of_point("12", "9", "AB=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-04-EX2",
                title_en="Ptolemy's Theorem in a Cyclic Quadrilateral",
                title_ar="مبرهنة بطليموس في رباعي دائري",
                q_en=(
                    f"Cyclic quadrilateral {m('ABCD')} has side lengths {m('AB = 6')}, {m('BC = 8')}, {m('CD = 9')}, and {m('DA = 6')}. "
                    f"If diagonal {m('AC = 10')}, what is the length of diagonal {m('BD')}?"
                ),
                q_ar=(
                    f"رباعي دائري {m('ABCD')} أطوال أضلاعه {m('AB = 6')} و{m('BC = 8')} و{m('CD = 9')} و{m('DA = 6')}. "
                    f"إذا كان طول القطر {m('AC = 10')}، فما طول القطر {m('BD')}؟"
                ),
                correct_val=Fraction(51, 5),
                distractors=[9, Fraction(48, 5), 10, Fraction(54, 5)],
                idea_en="Substitute the four side lengths and AC = 10 into Ptolemy's equation AC·BD = AB·CD + BC·DA.",
                steps_en=[
                    f"By Ptolemy's theorem, {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
                    f"Substitute the known lengths: {m('10 \\cdot BD = 6 \\times 9 + 8 \\times 6 = 54 + 48 = 102')}.",
                    f"Divide by {m('10')}: {m('BD = \\frac{102}{10} = \\frac{51}{5}')}.",
                ],
                check_en=f"Check product: {m('10 \\times \\frac{51}{5} = 102 = 54 + 48')}.",
                idea_ar="عوّض أطوال الأضلاع الأربعة وطول القطر AC = 10 في صيغة بطليموس.",
                steps_ar=[
                    f"من مبرهنة بطليموس: {m('AC \\cdot BD = AB \\cdot CD + BC \\cdot DA')}.",
                    f"بالتعويض: {m('10 \\cdot BD = 6(9) + 8(6) = 54 + 48 = 102')}.",
                    f"إذن {m('BD = \\frac{102}{10} = \\frac{51}{5}')}.",
                ],
                check_ar=f"التحقق: {m('10 \\times \\frac{51}{5} = 102')}.",
                diagram_en=svg_olym_cyclic_ptolemy("6", "8", "9", "6", "BD=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-04-EX3",
                title_en="Concurrent Cevians & Mass Points",
                title_ar="تلاقي القطع السيفية ومبرهنة سيفا",
                q_en=(
                    f"In {m('\\triangle ABC')}, cevians {m('AD, BE, CF')} concur at {m('P')}. "
                    f"If {m('BD:DC = 3:2')} and {m('CE:EA = 4:5')}, what is the ratio {m('AF:FB')}?"
                ),
                q_ar=(
                    f"في المثلث {m('\\triangle ABC')}، تتلاقى القطع السيفية {m('AD, BE, CF')} في النقطة {m('P')}. "
                    f"إذا كان {m('BD:DC = 3:2')} و{m('CE:EA = 4:5')}، فما قيمة النسبة {m('AF:FB')}؟"
                ),
                correct_val=Fraction(5, 6),
                distractors=[Fraction(6, 5), Fraction(3, 4), Fraction(8, 15), Fraction(15, 8)],
                idea_en="Substitute BD/DC = 3/2 and CE/EA = 4/5 into Ceva's equation (BD/DC)(CE/EA)(AF/FB) = 1.",
                steps_en=[
                    f"By Ceva's theorem, {m('\\frac{BD}{DC} \\cdot \\frac{CE}{EA} \\cdot \\frac{AF}{FB} = 1')}.",
                    f"Substitute the given ratios: {m('\\frac{3}{2} \\cdot \\frac{4}{5} \\cdot \\frac{AF}{FB} = 1 \\implies \\frac{6}{5} \\cdot \\frac{AF}{FB} = 1')}.",
                    f"Solve for {m('AF/FB')}: {m('\\frac{AF}{FB} = \\frac{5}{6}')}.",
                ],
                check_en=f"Check product: {m('\\frac{3}{2} \\times \\frac{4}{5} \\times \\frac{5}{6} = \\frac{60}{60} = 1')}.",
                idea_ar="طبّق مبرهنة سيفا مباشرةً بالتعويض عن النسبتين المعلومتين.",
                steps_ar=[
                    f"من مبرهنة سيفا: {m('\\frac{BD}{DC} \\cdot \\frac{CE}{EA} \\cdot \\frac{AF}{FB} = 1')}.",
                    f"بالتعويض: {m('\\frac{3}{2} \\cdot \\frac{4}{5} \\cdot \\frac{AF}{FB} = 1 \\implies \\frac{AF}{FB} = \\frac{5}{6}')}.",
                ],
                check_ar=f"التحقق: {m('\\frac{3}{2} \\times \\frac{4}{5} \\times \\frac{5}{6} = 1')}.",
                diagram_en=svg_stu_ceva_triangle("3", "2", "4", "5"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-04-EX4",
                title_en="Cevian Length via Stewart's Theorem",
                title_ar="طول القطعة السيفية بمبرهنة ستيوارت",
                q_en=(
                    f"In {m('\\triangle ABC')}, {m('AB = 13')}, {m('AC = 15')}, and {m('BC = 14')}. "
                    f"Point {m('D')} lies on {m('BC')} with {m('BD = 6')} and {m('DC = 8')}. What is the value of {m('AD^2')}?"
                ),
                q_ar=(
                    f"في المثلث {m('\\triangle ABC')}، لدينا {m('AB = 13')} و{m('AC = 15')} و{m('BC = 14')}. "
                    f"تقع النقطة {m('D')} على {m('BC')} بحيث {m('BD = 6')} و{m('DC = 8')}. ما قيمة {m('AD^2')}؟"
                ),
                correct_val=145,
                distractors=[121, 129, 136, 144],
                idea_en="Apply Stewart's theorem b²m + c²n = a(d² + mn) with a = 14, b = 15, c = 13, m = 6, n = 8.",
                steps_en=[
                    f"By Stewart's theorem on {m('\\triangle ABC')} with cevian {m('d = AD')}: {m('AC^2 \\cdot BD + AB^2 \\cdot DC = BC(AD^2 + BD \\cdot DC)')}.",
                    f"Substitute {m('15^2 \\cdot 6 + 13^2 \\cdot 8 = 14(d^2 + 6 \\cdot 8)')}: {m('1350 + 1352 = 14(d^2 + 48)')}.",
                    f"Divide {m('2702')} by {m('14')}: {m('d^2 + 48 = 193 \\implies d^2 = 193 - 48 = 145')}.",
                ],
                check_en=f"The altitude from {m('A')} in a {m('13\\text{-}14\\text{-}15')} triangle has foot {m('H')} at {m('BH = 5')} and height {m('AH = 12')}, so {m('HD = 6 - 5 = 1')} and {m('AD^2 = 12^2 + 1^2 = 145')}.",
                idea_ar="طبّق مبرهنة ستيوارت b²m + c²n = a(d² + mn) مع الانتباه لطرح 48 من 193.",
                steps_ar=[
                    f"من مبرهنة ستيوارت: {m('15^2(6) + 13^2(8) = 14(AD^2 + 48)')}.",
                    f"نحسب الطرف الأيسر: {m('1350 + 1352 = 2702')}، وبالقسمة على {m('14')} نجد {m('AD^2 + 48 = 193 \\implies AD^2 = 145')}.",
                ],
                check_ar=f"بما أن مسقط الارتفاع في المثلث {m('13\\text{-}14\\text{-}15')} يبعد {m('5')} عن {m('B')} وارتفاعه {m('12')}، فإن {m('AD^2 = 12^2 + (6-5)^2 = 145')}.",
                diagram_en=svg_median_tri("13", "15", "6+8", "AD²=?"),
            ),
        ],
        blueprints=[
            "olym_t2_geo_power_point_radical",
            "olym_t2_geo_ptolemy_cyclic_quads",
            "olym_t2_geo_ceva_menelaus_mass",
            "olym_t2_geo_stewart_apollonius_bisect",
        ],
    )


def _lesson_l2_05() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-05",
        level=T2,
        unit_num="2.5",
        topic="Geometry",
        title_en="Euler Line, Nine-Point Circle, Excircles, Homothety & 3D Solids",
        title_ar="خط أويلر ودائرة النقاط التسع والدوائر الماسة خارجياً والتحاكي والمجسمات",
        summary_en=(
            "Connect the circumcenter, centroid, orthocenter, and nine-point center along the Euler line, "
            "relate inradii and exradii, scale figures via homothety, and compute inscribed 3D solid volumes."
        ),
        summary_ar=(
            "الربط بين مركز الدائرة المحيطة ومركز الثقل وملتقى الارتفاعات ومركز دائرة النقاط التسع على خط أويلر، "
            "ودراسة الدوائر الماسة خارجياً، والتحاكي، وحجوم المجسمات."
        ),
        goals_en=[
            f"Use the Euler line ratios {m('OG:GH = 1:2')}, {m('ON_9 = N_9 H')}, and {m('R_{N_9} = R/2')}, plus {m('AH = 2R|\\cos A|')}.",
            f"Apply excircle tangent relations {m('AQ = s')}, {m('[ABC] = r_a(s - a)')}, and {m('\\frac{1}{r} = \\frac{1}{r_a} + \\frac{1}{r_b} + \\frac{1}{r_c}')}.",
            f"Scale distances and areas under homothety {m('\\mathcal{H}(S, k)')} and spiral similarity.",
            f"Compute volumes and radii of tangent spheres, cones, frustums, and corner tetrahedra.",
        ],
        goals_ar=[
            f"استعمال نسب خط أويلر {m('OG:GH = 1:2')} و{m('R_{N_9} = R/2')} والعلاقة {m('AH = 2R|\\cos A|')}.",
            f"تطبيق علاقات الدائرة الماسة خارجياً {m('AQ = s')} و{m('[ABC] = r_a(s - a)')} و{m('\\frac{1}{r} = \\frac{1}{r_a} + \\frac{1}{r_b} + \\frac{1}{r_c}')}.",
            f"تحويل الأطوال والمساحات تحت تأثير التحاكي {m('\\mathcal{H}(S, k)')} والتشابه اللولبي.",
            f"حساب حجوم وأنصاف أقطار الكرات المتماسة والمخاريط والمجسمات ثلاثية الأبعاد.",
        ],
        concepts=[
            olym_concept(
                title_en="The Euler Line & Nine-Point Circle",
                title_ar="خط أويلر ودائرة النقاط التسع",
                body_en=(
                    f"In any triangle, the circumcenter {m('O')}, centroid {m('G')}, nine-point center {m('N_9')}, and orthocenter {m('H')} are collinear with "
                    f"{m('OG : GN_9 : N_9 H = 2 : 1 : 3')}. The nine-point circle has radius {m('R/2')} and is the image of the circumcircle under {m('\\mathcal{H}(G, -1/2)')}."
                ),
                body_ar=(
                    f"في أي مثلث، تقع النقاط {m('O')} و{m('G')} و{m('N_9')} و{m('H')} على استقامة واحدة (خط أويلر) بنسب "
                    f"{m('OG : GN_9 : N_9 H = 2 : 1 : 3')}. ونصف قطر دائرة النقاط التسع يساوي {m('R/2')}."
                ),
                rule_en=dm(r"OH = 3\,OG, \qquad R_{N_9} = \frac{R}{2}, \qquad AH^2 + BC^2 = 4R^2"),
                rule_ar=dm(r"OH = 3\,OG, \qquad R_{N_9} = \frac{R}{2}, \qquad AH^2 + BC^2 = 4R^2"),
                diagram_en=svg_olym_nine_point_euler("O", "G", "H (OH=3·OG)"),
            ),
            olym_concept(
                title_en="Excircles, Inradius Reciprocals & Carnot's Theorem",
                title_ar="الدوائر الماسة خارجياً ومقلوبات أنصاف الأقطار ومبرهنة كارنو",
                body_en=(
                    f"The {m('A')}-excircle touches side {m('BC')} and the extensions of {m('AB, AC')} at distance {m('s')} from {m('A')}, with exradius {m('r_a = [ABC]/(s-a)')}. "
                    f"The reciprocals of the three exradii sum to the reciprocal of the inradius {m('r')}."
                ),
                body_ar=(
                    f"تمس الدائرة الخارجية المقابلة للرأس {m('A')} الضلع {m('BC')} وامتدادي {m('AB, AC')} على بُعد {m('s')} من {m('A')}، ونصف قطرها {m('r_a = [ABC]/(s-a)')}. "
                    f"ومجموع مقلوبات أنصاف أقطار الدوائر الماسة خارجياً يساوي مقلوب نصف قطر الدائرة الداخلية {m('1/r')}."
                ),
                rule_en=dm(r"r_a = \frac{[ABC]}{s - a}, \qquad \frac{1}{r_a} + \frac{1}{r_b} + \frac{1}{r_c} = \frac{1}{r}"),
                rule_ar=dm(r"r_a = \frac{[ABC]}{s - a}, \qquad \frac{1}{r_a} + \frac{1}{r_b} + \frac{1}{r_c} = \frac{1}{r}"),
                diagram_en=svg_olym_incircle_excircle("a", "b", "c", "r_a = Δ/(s−a)"),
            ),
            olym_concept(
                title_en="Homothety & 3D Tangent-Solid Geometry",
                title_ar="التحاكي وهندسة المجسمات المتماسة ثلاثية الأبعاد",
                body_en=(
                    f"A homothety {m('\\mathcal{H}(S, k)')} scales all lengths by {m('|k|')}, areas by {m('k^2')}, and volumes in 3D by {m('|k|^3')}. "
                    f"Two externally tangent spheres of radii {m('r_1, r_2')} resting on a flat plane touch the plane at points separated by {m('2\\sqrt{r_1 r_2}')}."
                ),
                body_ar=(
                    f"يضرب التحاكي {m('\\mathcal{H}(S, k)')} الأطوال في {m('|k|')} والمساحات في {m('k^2')} والحجوم في {m('|k|^3')}. "
                    f"وكرتان متماستان خارجياً نصفا قطريهما {m('r_1, r_2')} وتستقران على مستوٍ واحد تبعد نقطتا تماسهما مع المستوى مسافة {m('2\\sqrt{r_1 r_2}')}."
                ),
                rule_en=dm(r"d_{\text{plane}} = 2\sqrt{r_1 r_2}, \qquad V_{\text{frustum}} = \frac{\pi h}{3}(R^2 + Rr + r^2)"),
                rule_ar=dm(r"d_{\text{plane}} = 2\sqrt{r_1 r_2}, \qquad V_{\text{frustum}} = \frac{\pi h}{3}(R^2 + Rr + r^2)"),
                diagram_en=svg_olym_spiral_homothety("k", "S"),
            ),
        ],
        traps_en=[
            f"Writing {m('OG:GH = 2:1')} instead of {m('OG:GH = 1:2')} (the orthocenter {m('H')} is twice as far from {m('G')} as the circumcenter {m('O')}).",
            f"Confusing the incircle tangent length {m('s - a')} from vertex {m('A')} with the excircle tangent length {m('s')} from vertex {m('A')}.",
            f"Using {m('r_1 + r_2')} instead of {m('2\\sqrt{r_1 r_2}')} for the horizontal distance between the floor contact points of two tangent spheres.",
        ],
        traps_ar=[
            f"كتابة {m('OG:GH = 2:1')} بدلاً من {m('OG:GH = 1:2')} (ملتقى الارتفاعات {m('H')} أبعد بمرتين عن {m('G')} من مركز الدائرة المحيطة {m('O')}).",
            f"الخلط بين طول مماس الدائرة الداخلية من الرأس {m('A')} وهو {m('s - a')} وطول مماس الدائرة الخارجية من {m('A')} وهو {m('s')}.",
            f"استعمال {m('r_1 + r_2')} بدلاً من {m('2\\sqrt{r_1 r_2}')} للمسافة الأفقية بين نقطتي تماس كرتين متماستين مع الأرض.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-05-EX1",
                title_en="Orthocenter Distance & Euler Line Segments",
                title_ar="بُعد ملتقى الارتفاعات وقطع خط أويلر",
                q_en=(
                    f"In acute {m('\\triangle ABC')}, the circumradius is {m('R = 13')} and side {m('BC = 24')}. "
                    f"What is the distance {m('AH')} from vertex {m('A')} to the orthocenter {m('H')}?"
                ),
                q_ar=(
                    f"في المثلث الحاد الزوايا {m('\\triangle ABC')}، نصف قطر الدائرة المحيطة {m('R = 13')} وطول الضلع {m('BC = 24')}. "
                    f"ما المسافة {m('AH')} من الرأس {m('A')} إلى ملتقى الارتفاعات {m('H')}؟"
                ),
                correct_val=10,
                distractors=[5, 8, 12, 13],
                idea_en="Use the identity AH² + BC² = 4R² (since AH = 2 OM where M is the midpoint of BC).",
                steps_en=[
                    f"The distance from the circumcenter {m('O')} to the midpoint {m('M')} of {m('BC')} is {m('OM = \\sqrt{R^2 - (BC/2)^2} = \\sqrt{13^2 - 12^2} = 5')}.",
                    f"In any triangle, {m('AH = 2 \\cdot OM')}.",
                    f"Therefore {m('AH = 2 \\times 5 = 10')}.",
                ],
                check_en=f"Check {m('AH^2 + BC^2 = 10^2 + 24^2 = 676 = (2 \\times 13)^2 = 4R^2')}.",
                idea_ar="احسب بُعد مركز الدائرة المحيطة OM عن منتصف الضلع BC ثم اضربه في 2 لأن AH = 2 OM.",
                steps_ar=[
                    f"بُعد المركز {m('O')} عن منتصف {m('BC')} هو {m('OM = \\sqrt{13^2 - 12^2} = 5')}.",
                    f"وبما أن {m('AH = 2 \\cdot OM')} فإن {m('AH = 2 \\times 5 = 10')}.",
                ],
                check_ar=f"التحقق: {m('10^2 + 24^2 = 676 = 4R^2')}.",
                diagram_en=svg_olym_nine_point_euler("R=13", "OM=5", "AH=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-05-EX2",
                title_en="Exradius Opposite the Longest Side",
                title_ar="نصف قطر الدائرة الماسة خارجياً",
                q_en=(
                    f"A triangle {m('ABC')} has sides {m('a = 15')}, {m('b = 14')}, and {m('c = 13')}. "
                    f"What is the radius {m('r_a')} of the excircle tangent to side {m('BC = 15')}?"
                ),
                q_ar=(
                    f"مثلث {m('ABC')} أطوال أضلاعه {m('a = 15')} و{m('b = 14')} و{m('c = 13')}. "
                    f"ما نصف قطر الدائرة الماسة خارجياً {m('r_a')} للضلع {m('BC = 15')}؟"
                ),
                correct_val=14,
                distractors=[10, 12, 15, 21],
                idea_en="Compute the area [ABC] = 84 and semiperimeter s = 21, then use r_a = [ABC]/(s - a).",
                steps_en=[
                    f"The semiperimeter is {m('s = (15 + 14 + 13)/2 = 21')}, and by Heron's formula {m('[ABC] = 84')}.",
                    f"The {m('A')}-exradius is {m('r_a = \\frac{[ABC]}{s - a} = \\frac{84}{21 - 15} = \\frac{84}{6} = 14')}.",
                ],
                check_en=f"Check the three exradii: {m('r_a = 14')}, {m('r_b = 84/7 = 12')}, {m('r_c = 84/8 = 21/2')}, and {m('\\frac{1}{14} + \\frac{1}{12} + \\frac{2}{21} = \\frac{6+7+8}{84} = \\frac{1}{4} = \\frac{1}{r}')}.",
                idea_ar="احسب المساحة [ABC] = 84 ونصف المحيط s = 21 ثم طبّق r_a = [ABC]/(s - a).",
                steps_ar=[
                    f"نصف المحيط {m('s = 21')} والمساحة من صيغة هيرون {m('[ABC] = 84')}.",
                    f"نصف قطر الدائرة الماسة خارجياً للضلع {m('a = 15')} هو {m('r_a = \\frac{84}{21 - 15} = \\frac{84}{6} = 14')}.",
                ],
                check_ar=f"مجموع مقلوبات أنصاف الأقطار الخارجية يساوي {m('1/4 = 1/r')}.",
                diagram_en=svg_olym_incircle_excircle("15", "14", "13", "r_a=?"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-05-EX3",
                title_en="Inscribed Square via Homothety",
                title_ar="مربع محاط داخل مثلث عبر التحاكي",
                q_en=(
                    f"Triangle {m('ABC')} has base {m('BC = 15')} and altitude {m('h = 10')} to {m('BC')}. "
                    f"A square {m('PQRS')} has {m('P, Q')} on {m('BC')}, {m('R')} on {m('AC')}, and {m('S')} on {m('AB')}. What is the side length of the square?"
                ),
                q_ar=(
                    f"مثلث {m('ABC')} طول قاعدته {m('BC = 15')} وارتفاعه النازل عليها {m('h = 10')}. "
                    f"رُسم مربع {m('PQRS')} بحيث تقع {m('P, Q')} على {m('BC')} و{m('R')} على {m('AC')} و{m('S')} على {m('AB')}. ما طول ضلع المربع؟"
                ),
                correct_val=6,
                distractors=[5, Fraction(25, 4), Fraction(15, 2), 8],
                idea_en="A homothety from A scales △ASR (base x, height 10 - x) onto △ABC (base 15, height 10), giving x = bh/(b + h).",
                steps_en=[
                    f"Let the side length of the square be {m('x')}. Then {m('\\triangle ASR \\sim \\triangle ABC')} with altitude {m('10 - x')}.",
                    f"By homothety scaling from {m('A')}, {m('\\frac{x}{15} = \\frac{10 - x}{10}')}.",
                    f"Cross-multiply: {m('10x = 150 - 15x \\implies 25x = 150 \\implies x = 6')}.",
                ],
                check_en=f"Formula check: {m('x = \\frac{b h}{b + h} = \\frac{15 \\times 10}{15 + 10} = \\frac{150}{25} = 6')}.",
                idea_ar="التحاكي من الرأس A يحوّل المثلث العلوي ذا القاعدة x والارتفاع 10 - x إلى المثلث الكلي.",
                steps_ar=[
                    f"ليكن طول ضلع المربع {m('x')}. من تشابه المثلثين بتحاكي مركزه {m('A')}: {m('\\frac{x}{15} = \\frac{10 - x}{10}')}.",
                    f"نحل المعادلة: {m('25x = 150 \\implies x = 6')}.",
                ],
                check_ar=f"من الصيغة المختصرة: {m('x = \\frac{bh}{b+h} = \\frac{150}{25} = 6')}.",
                diagram_en=svg_olym_spiral_homothety("x=bh/(b+h)", "A"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-05-EX4",
                title_en="Two Externally Tangent Spheres on a Table",
                title_ar="كرتان متماستان خارجياً على طاولة أفقية",
                q_en=(
                    f"Two spheres of radii {m('r_1 = 4')} and {m('r_2 = 9')} rest on a flat horizontal table and are externally tangent to each other. "
                    f"What is the distance between the two points where the spheres touch the table?"
                ),
                q_ar=(
                    f"كرتان نصفا قطريهما {m('r_1 = 4')} و{m('r_2 = 9')} تستقران على طاولة أفقية مستوية وتتماسان خارجياً. "
                    f"ما المسافة بين نقطتي تماس الكرتين مع سطح الطاولة؟"
                ),
                correct_val=12,
                distractors=[10, 13, 15, 18],
                idea_en="Form the right trapezoid of centers and floor contact points with hypotenuse r₁ + r₂ and vertical leg |r₂ - r₁|.",
                steps_en=[
                    f"The distance between the sphere centers is {m('r_1 + r_2 = 4 + 9 = 13')}, and the difference in their heights above the table is {m('9 - 4 = 5')}.",
                    f"By the Pythagorean theorem, the horizontal distance {m('d')} satisfies {m('d = \\sqrt{(r_1 + r_2)^2 - (r_2 - r_1)^2} = 2\\sqrt{r_1 r_2}')}.",
                    f"Substitute {m('r_1 = 4, r_2 = 9')}: {m('d = 2\\sqrt{36} = 12')}.",
                ],
                check_en=f"Check right triangle: {m('5^2 + 12^2 = 25 + 144 = 169 = 13^2')}.",
                idea_ar="شكّل مثلثاً قائماً وتره مجموع نصفي القطرين وضلعاه الفرق بينهما والمسافة الأفقية d = 2√(r₁r₂).",
                steps_ar=[
                    f"البعد بين المركزين {m('4 + 9 = 13')} وفرق الارتفاعين {m('9 - 4 = 5')}.",
                    f"من مبرهنة فيثاغورس: {m('d = 2\\sqrt{r_1 r_2} = 2\\sqrt{4 \\times 9} = 12')}.",
                ],
                check_ar=f"التحقق: {m('5^2 + 12^2 = 13^2')}.",
                diagram_en=svg_stu_sphere_in_cylinder("r₁=4, r₂=9", "d=2√(r₁r₂)=?"),
            ),
        ],
        blueprints=[
            "olym_t2_geo_euler_line_nine_point",
            "olym_t2_geo_excircles_carnot_inrad",
            "olym_t2_geo_homothety_rotation",
            "olym_t2_geo_solid_spheres_cones",
        ],
    )


def _lesson_l2_06() -> dict:
    return make_olympiad_lesson(
        lesson_id="OLYM-L2-06",
        level=T2,
        unit_num="2.6",
        topic="Combinatorics",
        title_en="Catalan Bijections, Linear Recurrences, Graph Theory & Game Invariants",
        title_ar="تقابلات كاتالان والعلاقات التراجعية ونظرية البيان وثوابت الألعاب",
        summary_en=(
            "Count Dyck paths and triangulations with Catalan numbers, solve tiling and state-machine recurrences, "
            "apply the Handshaking Lemma and tree formulas, and analyze combinatorial games via invariants and monovariants."
        ),
        summary_ar=(
            "عدّ مسارات دايك وتثليثات المضلعات بأعداد كاتالان، وحل العلاقات التراجعية للتبليط، "
            "وتطبيق توطئة المصافحة وخصائص الأشجار، وتحليل الألعاب التوافقية بالثوابت."
        ),
        goals_en=[
            f"Evaluate Catalan numbers {m('C_n = \\frac{1}{n+1}\\binom{2n}{n}')} for Dyck paths, balanced parentheses, and polygon triangulations.",
            f"Construct and iterate linear recurrences for domino/tromino tilings and restricted strings.",
            f"Use the Handshaking Lemma {m('\\sum \\deg(v) = 2|E|')} and tree identity {m('|E| = |V| - 1')}.",
            f"Determine winning strategies and process termination lengths using invariants and monovariants.",
        ],
        goals_ar=[
            f"حساب أعداد كاتالان {m('C_n = \\frac{1}{n+1}\\binom{2n}{n}')} لمسارات دايك والأقواس المتوازنة وتثليث المضلعات.",
            f"بناء وحل العلاقات التراجعية الخطية لمسائل التبليط والسلاسل المقيدة.",
            f"توظيف توطئة المصافحة {m('\\sum \\deg(v) = 2|E|')} وعلاقة الأشجار {m('|E| = |V| - 1')}.",
            f"تحديد استراتيجيات الفوز وعدد خطوات التوقف باستخدام الثوابت وشبه الثوابت.",
        ],
        concepts=[
            olym_concept(
                title_en="Catalan Numbers & Reflection Principle Bijections",
                title_ar="أعداد كاتالان وتقابلات مبدأ الانعكاس",
                body_en=(
                    f"The {m('n')}-th Catalan number {m('C_n = \\frac{1}{n+1}\\binom{2n}{n} = \\binom{2n}{n} - \\binom{2n}{n-1}')} counts lattice paths from {m('(0,0)')} to {m('(n,n)')} "
                    f"that never rise above {m('y = x')}, valid sequences of {m('n')} pairs of parentheses, and triangulations of a convex {m('(n+2)')}-gon."
                ),
                body_ar=(
                    f"يمثّل عدد كاتالان {m('C_n = \\frac{1}{n+1}\\binom{2n}{n}')} عدد المسارات الشبكية من {m('(0,0)')} إلى {m('(n,n)')} التي لا تتجاوز القطر {m('y = x')}، "
                    f"وعدد سلاسل {m('n')} من أزواج الأقواس المتوازنة، وعدد طرق تثليث مضلع محدب ذي {m('n+2')} ضلعاً."
                ),
                rule_en=dm(r"C_n = \frac{1}{n+1}\binom{2n}{n}, \qquad (C_0, C_1, C_2, C_3, C_4, C_5) = (1, 1, 2, 5, 14, 42)"),
                rule_ar=dm(r"C_n = \frac{1}{n+1}\binom{2n}{n}, \qquad (C_0, C_1, C_2, C_3, C_4, C_5) = (1, 1, 2, 5, 14, 42)"),
                diagram_en=svg_stu_dyck_grid(4),
            ),
            olym_concept(
                title_en="Linear Recurrences, Handshaking Lemma & Trees",
                title_ar="العلاقات التراجعية وتوطئة المصافحة والأشجار",
                body_en=(
                    f"Conditioning on the first move or tile yields linear recurrences such as {m('T_n = T_{n-1} + T_{n-2}')}. "
                    f"In any graph {m('G = (V, E)')}, vertex degrees sum to {m('2|E|')}, and a forest with {m('k')} connected components satisfies {m('|E| = |V| - k')}."
                ),
                body_ar=(
                    f"التفريع حسب الخطوة الأولى يولّد علاقات تراجعية خطية مثل {m('T_n = T_{n-1} + T_{n-2}')}. "
                    f"وفي أي بيان {m('G = (V, E)')} يكون مجموع درجات الرؤوس {m('2|E|')}، ولغابة مكونة من {m('k')} أشجار يتحقق {m('|E| = |V| - k')}."
                ),
                rule_en=dm(r"\sum_{v \in V} \deg(v) = 2|E|, \qquad |E|_{\text{forest}} = |V| - k"),
                rule_ar=dm(r"\sum_{v \in V} \deg(v) = 2|E|, \qquad |E|_{\text{forest}} = |V| - k"),
                diagram_en=svg_olym_bipartite_graph(3, 4, note="∑ deg(v) = 2|E|"),
            ),
            olym_concept(
                title_en="Combinatorial Game Strategy, Invariants & Monovariants",
                title_ar="استراتيجيات الألعاب التوافقية والثوابت وشبه الثوابت",
                body_en=(
                    f"An invariant stays constant across every legal move (e.g., {m('(a+b)(b+1) \\bmod p')} when replacing {m('(a,b)')} with {m('ab+a+b')}). "
                    f"In impartial take-away games allowing {m('1')} to {m('k')} stones, positions with {m('N \\equiv 0 \\pmod{k+1}')} are losing ({m('\\mathcal{P}')}-positions)."
                ),
                body_ar=(
                    f"الثابت لا يتغير عبر أي حركة قانونية، بينما يتغير شبه الثابت باتجاه واحد دائماً فيضمن توقف العملية. "
                    f"وفي ألعاب سحب من {m('1')} إلى {m('k')} حجر، تكون المواضع التي تحقق {m('N \\equiv 0 \\pmod{k+1}')} مواضع خاسرة لمن يبدأ منها."
                ),
                rule_en=dm(r"a \oplus b = ab + a + b \implies (a \oplus b) + 1 = (a + 1)(b + 1)"),
                rule_ar=dm(r"a \oplus b = ab + a + b \implies (a \oplus b) + 1 = (a + 1)(b + 1)"),
                diagram_en=svg_olym_board_coloring(4, 4, modulus=3, note="Invariant mod k+1"),
            ),
        ],
        traps_en=[
            f"Off-by-one indexing on polygon triangulations: a convex {m('m')}-gon has {m('C_{m-2}')} triangulations, not {m('C_m')}.",
            f"Forgetting to divide the degree sum {m('\\sum \\deg(v)')} by {m('2')} when computing the number of edges {m('|E|')}.",
            f"Confusing the number of reductions {m('n - 1')} in a board replacement game with the final invariant value.",
        ],
        traps_ar=[
            f"الخطأ بمقدار 2 في تثليث المضلعات؛ فعدد تثليثات مضلع محدب ذي {m('m')} أضلاع هو {m('C_{m-2}')} وليس {m('C_m')}.",
            f"نسيان قسمة مجموع الدرجات {m('\\sum \\deg(v)')} على {m('2')} عند حساب عدد الحواف {m('|E|')}.",
            f"الخلط بين عدد خطوات التقليص {m('n - 1')} والقيمة النهائية للثابت الجبري على اللوحة.",
        ],
        examples=[
            olym_worked_example(
                ex_id="OLYM-L2-06-EX1",
                title_en="Triangulations of a Convex Octagon",
                title_ar="عدد طرق تثليث مثمن محدب",
                q_en=(
                    f"In how many ways can a convex octagon ({m('8')}-gon) be partitioned into {m('6')} triangles by {m('5')} non-intersecting diagonals?"
                ),
                q_ar=(
                    f"بكم طريقة يمكن تقسيم مثمن محدب ({m('8')} أضلاع) إلى {m('6')} مثلثات بواسطة {m('5')} أقطار غير متقاطعة داخلياً؟"
                ),
                correct_val=132,
                distractors=[42, 84, 120, 144],
                idea_en="A convex (n+2)-gon has C_n triangulations; for an 8-gon, n = 6 gives C_6.",
                steps_en=[
                    f"Triangulating a convex {m('(n+2)')}-gon is counted by the Catalan number {m('C_n')} with {m('n = 8 - 2 = 6')}.",
                    f"Evaluate {m('C_6 = \\frac{1}{7}\\binom{12}{6} = \\frac{924}{7} = 132')}.",
                ],
                check_en=f"Catalan recurrence check: {m('C_6 = 2(C_0 C_5 + C_1 C_4 + C_2 C_3) = 2(42 + 14 + 10) = 132')}.",
                idea_ar="عدد تثليثات مضلع محدب ذي (n+2) ضلعاً يساوي عدد كاتالان C_n؛ وللمثمن يكون n = 6.",
                steps_ar=[
                    f"نضع {m('n = 8 - 2 = 6')} في صيغة كاتالان.",
                    f"نحسب {m('C_6 = \\frac{1}{7}\\binom{12}{6} = \\frac{924}{7} = 132')}.",
                ],
                check_ar=f"التحقق من متتالية كاتالان: {m('C_5 = 42')} و{m('C_6 = \\frac{2(11)}{7} \\times 42 = 132')}.",
                diagram_en=svg_stu_dyck_grid(5),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-06-EX2",
                title_en="Binary Strings Without Consecutive Ones",
                title_ar="السلاسل الثنائية الخالية من رقمي 1 متتاليين",
                q_en=(
                    f"How many binary strings of length {m('8')} (composed of digits {m('0')} and {m('1')}) do **not** contain two consecutive {m('1')}s?"
                ),
                q_ar=(
                    f"كم سلسلة ثنائية طولها {m('8')} (مكوّنة من الرقمين {m('0')} و{m('1')}) **لا** تحتوي على رقمي {m('1')} متتاليين؟"
                ),
                correct_val=55,
                distractors=[34, 48, 64, 89],
                idea_en="Condition on the first bit (0 or 10) to obtain the Fibonacci recurrence a_n = a_{n-1} + a_{n-2} with a_1 = 2, a_2 = 3.",
                steps_en=[
                    f"A valid string of length {m('n')} starts either with {m('0')} ({m('a_{n-1}')} ways) or with {m('10')} ({m('a_{n-2}')} ways), so {m('a_n = a_{n-1} + a_{n-2}')}.",
                    f"With {m('a_1 = 2')} and {m('a_2 = 3')}, the sequence is {m('2, 3, 5, 8, 13, 21, 34, 55')}.",
                    f"Thus {m('a_8 = 55')}.",
                ],
                check_en=f"Equivalently, {m('\\sum_{k=0}^{4} \\binom{9-k}{k} = 1 + 8 + 21 + 20 + 5 = 55')}.",
                idea_ar="فرّع حسب الخانة الأولى لتحصل على متتالية فيبوناتشي a_n = a_{n-1} + a_{n-2} ابتداءً من a_1 = 2 وa_2 = 3.",
                steps_ar=[
                    f"كل سلسلة صالحة تبدأ بـ {m('0')} أو بـ {m('10')}، لذا {m('a_n = a_{n-1} + a_{n-2}')}.",
                    f"قيم المتتالية هي {m('a_1=2, 3, 5, 8, 13, 21, 34, a_8=55')}.",
                ],
                check_ar=f"التحقق بالتوافيق: {m('\\sum_{k=0}^{4} \\binom{9-k}{k} = 55')}.",
                diagram_en=svg_digit_slots(["0/1", "0/1", "⋯", "no 11"], top_note="aₙ = aₙ₋₁ + aₙ₋₂"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-06-EX3",
                title_en="Counting Leaves in a Tree from Degree Counts",
                title_ar="عدّ الأوراق في شجرة من درجات الرؤوس",
                q_en=(
                    f"A tree has {m('4')} vertices of degree {m('4')}, {m('5')} vertices of degree {m('3')}, {m('6')} vertices of degree {m('2')}, "
                    f"and all remaining vertices are leaves of degree {m('1')}. How many leaves does the tree have?"
                ),
                q_ar=(
                    f"شجرة تحتوي على {m('4')} رؤوس من الدرجة {m('4')}، و{m('5')} رؤوس من الدرجة {m('3')}، و{m('6')} رؤوس من الدرجة {m('2')}، "
                    f"وجميع الرؤوس المتبقية هي أوراق من الدرجة {m('1')}. كم ورقة في هذه الشجرة؟"
                ),
                correct_val=15,
                distractors=[13, 14, 16, 17],
                idea_en="Let L be the number of leaves; equate ∑ deg(v) = 2|E| = 2(|V| - 1).",
                steps_en=[
                    f"Let {m('L')} be the number of leaves. Then {m('|V| = 4 + 5 + 6 + L = 15 + L')}, so {m('2(|V| - 1) = 28 + 2L')}.",
                    f"The sum of degrees is {m('4(4) + 5(3) + 6(2) + 1(L) = 16 + 15 + 12 + L = 43 + L')}.",
                    f"Equating {m('43 + L = 28 + 2L')} gives {m('L = 15')}.",
                ],
                check_en=f"Formula check: {m('L = 2 + \\sum_{d \\ge 3} (d - 2) n_d = 2 + 4(2) + 5(1) = 15')}.",
                idea_ar="استعمل العلاقة ∑ deg(v) = 2(|V| - 1) في الشجرة أو الصيغة المختصرة L = 2 + ∑ (d - 2) n_d.",
                steps_ar=[
                    f"بفرض عدد الأوراق {m('L')}، يكون {m('|V| = 15 + L')} ومجموع الدرجات {m('43 + L')}.",
                    f"بمساواة {m('43 + L = 2(14 + L) = 28 + 2L')} نجد {m('L = 15')}.",
                ],
                check_ar=f"التحقق بالصيغة المباشرة: {m('L = 2 + 4(4-2) + 5(3-2) = 2 + 8 + 5 = 15')}.",
                diagram_en=svg_olym_bipartite_graph(3, 5, note="Tree: ∑ deg = 2(|V|−1)"),
            ),
            olym_worked_example(
                ex_id="OLYM-L2-06-EX4",
                title_en="Blackboard Algebraic Replacement Invariant",
                title_ar="الثابت الجبري في لعبة الاستبدال على اللوحة",
                q_en=(
                    f"The numbers {m('1, \\frac{1}{2}, \\frac{1}{3}, \\frac{1}{4}, \\frac{1}{5}')} are written on a blackboard. "
                    f"Each step, two numbers {m('a, b')} are erased and replaced by {m('ab + a + b')}. What is the single number remaining after {m('4')} steps?"
                ),
                q_ar=(
                    f"كُتبت الأعداد {m('1, \\frac{1}{2}, \\frac{1}{3}, \\frac{1}{4}, \\frac{1}{5}')} على سبورة. "
                    f"في كل خطوة يُمسح عددان {m('a, b')} ويُكتب مكانهما {m('ab + a + b')}. ما العدد الوحيد المتبقي بعد {m('4')} خطوات؟"
                ),
                correct_val=5,
                distractors=[4, 6, Fraction(11, 2), 120],
                idea_en="Notice that (ab + a + b) + 1 = (a + 1)(b + 1), so the product ∏ (x_i + 1) is invariant.",
                steps_en=[
                    f"Since {m('(ab + a + b) + 1 = (a + 1)(b + 1)')}, the product {m('P = \\prod (x_i + 1)')} is unchanged by every move.",
                    f"Initially, {m('P = (1 + 1)\\left(1 + \\frac{1}{2}\\right)\\left(1 + \\frac{1}{3}\\right)\\left(1 + \\frac{1}{4}\\right)\\left(1 + \\frac{1}{5}\\right) = \\frac{2}{1}\\cdot\\frac{3}{2}\\cdot\\frac{4}{3}\\cdot\\frac{5}{4}\\cdot\\frac{6}{5} = 6')}.",
                    f"The final number {m('X')} satisfies {m('X + 1 = 6 \\implies X = 5')}.",
                ],
                check_en=f"Telescoping product check: {m('\\prod_{k=1}^{5} \\frac{k+1}{k} = 6')}, so {m('X = 6 - 1 = 5')}.",
                idea_ar="بما أن (ab + a + b) + 1 = (a + 1)(b + 1) فإن الجداء ∏ (x_i + 1) ثابت لا يتغير.",
                steps_ar=[
                    f"المقدار {m('P = \\prod (x_i + 1)')} ثابت عبر جميع الخطوات.",
                    f"في البداية: {m('P = \\frac{2}{1}\\cdot\\frac{3}{2}\\cdot\\frac{4}{3}\\cdot\\frac{5}{4}\\cdot\\frac{6}{5} = 6')}.",
                    f"العدد النهائي {m('X')} يحقق {m('X + 1 = 6 \\implies X = 5')}.",
                ],
                check_ar=f"الجداء التلسكوبي يعطي {m('6')} ومنه {m('X = 6 - 1 = 5')}.",
                diagram_en=svg_olym_board_coloring(3, 5, modulus=2, note="∏(xᵢ + 1) = const"),
            ),
        ],
        blueprints=[
            "olym_t2_comb_catalan_dyck_biject",
            "olym_t2_comb_recurrences_tilings",
            "olym_t2_comb_graph_degrees_trees",
            "olym_t2_comb_monovariants_games",
        ],
    )


def get_tier12_lessons() -> list[dict]:
    """Return the 12 Olympiad Study Academy lessons for Tier 1 (Grades 7–8) and Tier 2 (Grades 9–10)."""
    return [
        _lesson_l1_01(),
        _lesson_l1_02(),
        _lesson_l1_03(),
        _lesson_l1_04(),
        _lesson_l1_05(),
        _lesson_l1_06(),
        _lesson_l2_01(),
        _lesson_l2_02(),
        _lesson_l2_03(),
        _lesson_l2_04(),
        _lesson_l2_05(),
        _lesson_l2_06(),
    ]
