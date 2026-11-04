"""ETEC Nafes KSA Grade 9 (الصف الثالث المتوسط) Question Bank — 360 Verified 4-Option (A–D) MCQs.

Covers all 24 official Grade 9 blueprints (15 questions per blueprint: 5 Easy [Knowing],
5 Medium [Applying], 5 Hard [Reasoning] = 120 Easy + 120 Medium + 120 Hard = 360 questions),
with 360/360 (100%) XML-valid SVG diagram coverage and 100% programmatic verification.
"""
from fractions import Fraction
import math

from nafes_common import (
    dm,
    explain_ar,
    explain_en,
    m,
    make_4_bilingual_options,
    make_nafes_q,
    make_nafes_question,
    svg_area_identity_square,
    svg_bar_chart,
    svg_function_machine,
    svg_midpoint_square_shaded,
    svg_motion_timeline,
    svg_nafes_box_plot,
    svg_nafes_coordinate_line,
    svg_nafes_function_table,
    svg_nafes_pie_chart,
    svg_nafes_spinner,
    svg_number_strip,
    svg_parabola_roots,
    svg_pipe_tank,
    svg_regular_polygon,
    svg_shaded_triangle_in_rect,
    svg_square_circle_shaded,
    svg_venn_2,
)
from nafes_lessons_g9 import (
    svg_g9_code_slots,
    svg_g9_histogram,
    svg_g9_marble_bag,
    svg_g9_parallel_transversal,
    svg_g9_real_number_line,
    svg_g9_right_triangle,
    svg_g9_sector_or_ring,
    svg_g9_similar_triangles,
    svg_g9_solid_3d,
)

LEVEL = "Grade 9"


def _qid(idx: int) -> str:
    return f"NAFS-G9-{idx:03d}"


# ==============================================================================
# UNIT 3.1 (G9-NUM-01 .. G9-NUM-04): Real Numbers, Radicals, Exponents & Sci Not
# ==============================================================================

def _gen_num_01(start_idx: int) -> list[dict]:
    """G9-NUM-01: Rational vs irrational, integer bounds of sqrt(n) & ordering real numbers."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Nearest integer to sqrt(n)
    easy_roots = [
        (29, "NEOM solar voltage sensor", "مستشعر جهد شمسي في نيوم"),
        (68, "Riyadh Metro acoustic meter", "مقياس صوتي في قطار الرياض"),
        (118, "Abha weather station barometer", "بارومتر محطة أرصاد أبها"),
    ]
    for n, ctx_en, ctx_ar in easy_roots:
        qid = _qid(cur); cur += 1
        lo = math.isqrt(n)
        hi = lo + 1
        ans = lo if (n - lo * lo) < (hi * hi - n) else hi
        assert (n - lo * lo) != (hi * hi - n)
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-01",
            f"A {ctx_en} records a reading of {m(rf'\sqrt{{{n}}}')} units. Which integer on the real number line is closest to {m(rf'\sqrt{{{n}}}')}?",
            f"يسجّل {ctx_ar} قراءة مقدارها {m(rf'\sqrt{{{n}}}')} وحدة. ما العدد الصحيح الأقرب إلى {m(rf'\sqrt{{{n}}}')} على خط الأعداد؟",
            ans, [lo - 1, hi if ans == lo else lo, hi + 1],
            f"Compare {m(str(n))} with the two consecutive perfect squares {m(str(lo*lo))} and {m(str(hi*hi))}.",
            f"قارن العدد {m(str(n))} بالمربعين الكاملين المتتاليين {m(str(lo*lo))} و{m(str(hi*hi))}.",
            f"Trap {m(str(n))} between {m(f'{lo}^2')} and {m(f'{hi}^2')}, then pick the closer square.",
            [
                f"Since {m(f'{lo}^2 = {lo*lo}')} and {m(f'{hi}^2 = {hi*hi}')}, we have {m(rf'{lo} < \sqrt{{{n}}} < {hi}')}.",
                f"Distances: {m(f'{n} - {lo*lo} = {n - lo*lo}')} versus {m(f'{hi*hi} - {n} = {hi*hi - n}')}, so {m(rf'\sqrt{{{n}}}')} is closest to {m(str(ans))}.",
            ],
            f"{m(f'{(lo + 0.5)**2:g}')} confirms which side of the midpoint {m(f'{lo}.5')} the root lies on.",
            f"نحصر {m(str(n))} بين {m(f'{lo}^2')} و{m(f'{hi}^2')} ونختار الأقرب.",
            [
                f"لدينا {m(f'{lo*lo} < {n} < {hi*hi}')} أي {m(rf'{lo} < \sqrt{{{n}}} < {hi}')}.",
                f"الفرق عن {m(str(lo*lo))} هو {m(str(n - lo*lo))} وعن {m(str(hi*hi))} هو {m(str(hi*hi - n))}، فالأقرب هو {m(str(ans))}.",
            ],
            f"مقارنة المربع مع {m(f'{(lo + 0.5)**2:g}')} تؤكد أن التقريب الصحيح هو {m(str(ans))}.",
            diagram_en=svg_g9_real_number_line([lo - 1, lo, hi, hi + 1], math.sqrt(n), f"√{n}", f"{lo*lo} < {n} < {hi*hi}"),
        ))

    # Easy 4-5: Identifying irrational numbers
    irrat_cases = [
        ("Grade 9 calibration set A", "مجموعة المعايرة (أ) للصف الثالث المتوسط", r"\sqrt{24}", [r"\sqrt{81}", r"\frac{7}{11}", r"0.\overline{6}"], 24),
        ("KAUST robotics benchmark set B", "مجموعة معيار الروبوتات (ب)", r"\sqrt{50}", [r"-\sqrt{144}", r"3.25", r"-\frac{9}{4}"], 50),
    ]
    for ctx_en, ctx_ar, corr_s, dists, rad_n in irrat_cases:
        qid = _qid(cur); cur += 1
        assert math.isqrt(rad_n) ** 2 != rad_n
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-01",
            f"In {ctx_en}, which of the following real numbers is **irrational**?",
            f"في {ctx_ar}، أي الأعداد الحقيقية الآتية يُعدّ **عدداً غير نسبي**؟",
            corr_s, dists,
            "An irrational square root has a positive integer radicand that is NOT a perfect square.",
            "الجذر التربيعي لعدد صحيح موجب ليس مربعاً كاملاً يكون عدداً غير نسبي.",
            "Check whether each number can be written as a ratio of two integers.",
            [
                f"Terminating decimals, repeating decimals, fractions, and roots of perfect squares are all rational.",
                f"Because {m(str(rad_n))} is not a perfect square, {m(corr_s)} has a non-terminating, non-repeating decimal expansion and is **irrational**.",
            ],
            f"No integer squared equals {m(str(rad_n))}.",
            "نختبر إمكانية كتابة كل عدد في صورة كسر من عددين صحيحين.",
            [
                "الكسور الاعتيادية والعشرية المنتهية والدورية وجذور المربعات الكاملة كلها أعداد نسبية.",
                f"العدد {m(str(rad_n))} ليس مربعاً كاملاً، لذا {m(corr_s)} **عدد غير نسبي**.",
            ],
            f"لا يوجد عدد صحيح مربعه {m(str(rad_n))}.",
            diagram_en=svg_nafes_function_table(["Set", "Examples"], [["Rational (Q)", "Fractions, 0.666..., √81"], ["Irrational (I)", f"√{rad_n}, π"]]),
        ))

    # Medium 6-8: Counting integers strictly between sqrt(a) and sqrt(b)
    interval_cases = [
        (11, 70, "thermal tolerance band in a Tabuk greenhouse", "نطاق التحمل الحراري في بيت محمي بتبوك"),
        (20, 105, "drone altitude window at Qiddiya test field", "نافذة ارتفاع طائرة مسيّرة في ميدان القدية"),
        (30, 150, "salinity index range at Jubail desalination lab", "مدى مؤشر الملوحة في مختبر تحلية الجبيل"),
    ]
    for a, b, ctx_en, ctx_ar in interval_cases:
        qid = _qid(cur); cur += 1
        ints = [k for k in range(1, 30) if a < k * k < b]
        ans = len(ints)
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-01",
            f"The {ctx_en} requires an integer setting {m('k')} such that {m(rf'\sqrt{{{a}}} < k < \sqrt{{{b}}}')}. How many integers {m('k')} satisfy this inequality?",
            f"يتطلب {ctx_ar} ضبط تدريج صحيح {m('k')} يحقق المتباينة {m(rf'\sqrt{{{a}}} < k < \sqrt{{{b}}}')}. كم عدداً صحيحاً {m('k')} يحقق هذا الشرط؟",
            ans, [ans - 1, ans + 1, ans + 2],
            f"Square the inequality to find integers {m('k > 0')} with {m(f'{a} < k^2 < {b}')}.",
            f"ربّع أطراف المتباينة لإيجاد الأعداد الصحيحة الموجبة التي تحقق {m(f'{a} < k^2 < {b}')}.",
            f"Find {m(r'\lceil \sqrt{a} \rceil')} through {m(r'\lfloor \sqrt{b} \rfloor')}.",
            [
                f"Since {m(f'{ints[0]-1}^2 = {(ints[0]-1)**2} \\le {a} < {ints[0]}^2 = {ints[0]**2}')}, the smallest integer is {m(str(ints[0]))}.",
                f"Since {m(f'{ints[-1]}^2 = {ints[-1]**2} < {b} \\le {ints[-1]+1}^2 = {(ints[-1]+1)**2}')}, the largest integer is {m(str(ints[-1]))}.",
                f"Counting from {m(str(ints[0]))} to {m(str(ints[-1]))} gives {m(f'{ints[-1]} - {ints[0]} + 1 = {ans}')} integers.",
            ],
            f"Valid integers: {m(', '.join(map(str, ints)))} ({m(str(ans))} values).",
            f"نحدد أول وآخر مربع كامل يقع بين {m(str(a))} و{m(str(b))}.",
            [
                f"أصغر عدد صحيح هو {m(str(ints[0]))} لأن {m(f'{ints[0]}^2 = {ints[0]**2} > {a}')}، وأكبرها {m(str(ints[-1]))} لأن {m(f'{ints[-1]}^2 = {ints[-1]**2} < {b}')}.",
                f"عدد القيم الصحيحة هو {m(f'{ints[-1]} - {ints[0]} + 1 = {ans}')}.",
            ],
            f"القيم هي: {m(', '.join(map(str, ints)))}.",
            diagram_en=svg_g9_real_number_line([ints[0] - 1, ints[0], ints[-1], ints[-1] + 1], (ints[0] + ints[-1]) / 2, "? integers", f"√{a} < k < √{b}"),
        ))

    # Medium 9-10: Ordering real numbers (greatest & least)
    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-01",
        f"Four AlUla telescope mirrors have focal ratios {m('4.6')}, {m(r'\sqrt{23}')}, {m(r'\frac{9}{2}')}, and {m(r'\sqrt{19}')}. Which value is the **greatest**?",
        f"أربع مرايا تلسكوبية في العلا نسبها البؤرية {m('4.6')} و{m(r'\sqrt{23}')} و{m(r'\frac{9}{2}')} و{m(r'\sqrt{19}')}. أي هذه القيم هي **الأكبر**؟",
        r"\sqrt{23}", ["4.6", r"\frac{9}{2}", r"\sqrt{19}"],
        "Square all four positive numbers to compare them without decimal guesswork.",
        "ربّع الأعداد الموجبة الأربعة لمقارنتها بدقة دون تقريب عشوائي.",
        "For positive real numbers, the largest number has the largest square.",
        [
            f"Compute squares: {m('4.6^2 = 21.16')}, {m(r'(\sqrt{23})^2 = 23')}, {m('(9/2)^2 = 4.5^2 = 20.25')}, and {m(r'(\sqrt{19})^2 = 19')}.",
            f"Since {m('23 > 21.16 > 20.25 > 19')}, the greatest value is {m(r'\sqrt{23}')}.",
        ],
        f"{m(r'\sqrt{23} \approx 4.796 > 4.6')}.",
        "للأعداد الموجبة، العدد الأكبر هو صاحب المربع الأكبر.",
        [
            f"نربّع القيم: {m('4.6^2 = 21.16')}، {m(r'(\sqrt{23})^2 = 23')}، {m('4.5^2 = 20.25')}، و{m('19')}.",
            f"أكبر المربعات هو {m('23')}، إذن {m(r'\sqrt{23}')} هي القيمة الأكبر.",
        ],
        f"{m(r'\sqrt{23} \approx 4.80 > 4.6')}.",
        diagram_en=svg_g9_real_number_line([4, 5], math.sqrt(23), "√23 ≈ 4.80", "Squares: 19 < 20.25 < 21.16 < 23"),
    ))

    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-01",
        f"A Hail cooling chamber logs four night temperatures (°C): {m('-3.4')}, {m(r'-\sqrt{13}')}, {m(r'-\frac{7}{2}')}, and {m(r'-\sqrt{10}')}. Which temperature is the **lowest**?",
        f"سجّلت غرفة تبريد في حائل أربع درجات حرارة ليلية (°س): {m('-3.4')} و{m(r'-\sqrt{13}')} و{m(r'-\frac{7}{2}')} و{m(r'-\sqrt{10}')}. أي درجة هي **الأقل**؟",
        r"-\sqrt{13}", ["-3.4", r"-\frac{7}{2}", r"-\sqrt{10}"],
        "Among negative numbers, the one with the largest absolute value lies farthest left (lowest).",
        "بين الأعداد السالبة، العدد ذو القيمة المطلقة الأكبر هو الأصغر قيمةً.",
        "Square the magnitudes and remember negative order reverses magnitude order.",
        [
            f"Squared magnitudes: {m('3.4^2 = 11.56')}, {m('13')}, {m('3.5^2 = 12.25')}, and {m('10')}.",
            f"Since {m(r'\sqrt{13} \approx 3.606')} has the largest magnitude, {m(r'-\sqrt{13}')} is the lowest temperature.",
        ],
        f"{m(r'-\sqrt{13} < -3.5 < -3.4 < -\sqrt{10}')}.",
        "نقارن مربعات القيم المطلقة ثم نعكس الترتيب للإشارة السالبة.",
        [
            f"مربعات القيم المطلقة هي: {m('11.56')} و{m('13')} و{m('12.25')} و{m('10')}.",
            f"بما أن {m('13')} هي الأكبر، فإن {m(r'-\sqrt{13}')} هي الدرجة الأقل.",
        ],
        f"{m(r'-\sqrt{13} \approx -3.61 < -3.5')}.",
        diagram_en=svg_g9_real_number_line([-4, -3], -math.sqrt(13), "−√13", "−√13 < −3.5 < −3.4 < −√10"),
    ))

    # Hard 11-15: Reasoning with bounds & irrational counts
    hard_bounds = [
        (90, 42, "NEOM laser bench"),
        (130, 55, "Diriyah structural survey"),
    ]
    for r1, r2, ctx_en in hard_bounds:
        qid = _qid(cur); cur += 1
        a = math.isqrt(r1); b = a + 1
        c = math.isqrt(r2); d = c + 1
        ans = a + d
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-01",
            f"In a {ctx_en}, consecutive integers {m('a, b')} satisfy {m(rf'a < \sqrt{{{r1}}} < b')} and consecutive integers {m('c, d')} satisfy {m(rf'c < \sqrt{{{r2}}} < d')}. What is the value of {m('a + d')}?",
            f"في تجربة قياس هندسية، إذا كان العددان الصحيحان المتتاليان {m('a, b')} يحققان {m(rf'a < \sqrt{{{r1}}} < b')} والعددان المتتاليان {m('c, d')} يحققان {m(rf'c < \sqrt{{{r2}}} < d')}، فما قيمة {m('a + d')}؟",
            ans, [a + c, b + d, b + c + 2],
            f"Find the lower integer bound {m('a')} of {m(rf'\sqrt{{{r1}}}')} and the upper integer bound {m('d')} of {m(rf'\sqrt{{{r2}}}')}.",
            f"أوجد الحد الأدنى {m('a')} للجذر الأول والحد الأعلى {m('d')} للجذر الثاني ثم اجمعهما.",
            "Bound each root between consecutive squares carefully.",
            [
                f"Since {m(f'{a}^2 = {a*a} < {r1} < {b*b} = {b}^2')}, we get {m(f'a = {a}')} and {m(f'b = {b}')}.",
                f"Since {m(f'{c}^2 = {c*c} < {r2} < {d*d} = {d}^2')}, we get {m(f'c = {c}')} and {m(f'd = {d}')}.",
                f"Therefore {m(f'a + d = {a} + {d} = {ans}')}.",
            ],
            f"Check: {m(f'a = {a}')} (lower) + {m(f'd = {d}')} (upper) = {m(str(ans))}.",
            "نحصر كل جذر بين مربعين كاملين متتاليين بدقة.",
            [
                f"بما أن {m(f'{a*a} < {r1} < {b*b}')} فإن {m(f'a = {a}')}.",
                f"وبما أن {m(f'{c*c} < {r2} < {d*d}')} فإن {m(f'd = {d}')}، ومنه {m(f'a + d = {ans}')}.",
            ],
            f"تحقق: {m(f'{a} + {d} = {ans}')}.",
            diagram_en=svg_number_strip([f"{a} < √{r1} < {b}", f"{c} < √{r2} < {d}", "a + d = ?"]),
        ))

    irrat_count_cases = [
        (6, 8, "ETEC Grade 9 number-theory challenge"),
        (5, 7, "Riyadh STEM Olympiad warm-up"),
    ]
    for lo_i, hi_i, ctx_en in irrat_count_cases:
        qid = _qid(cur); cur += 1
        lo_sq, hi_sq = lo_i * lo_i, hi_i * hi_i
        total_between = hi_sq - lo_sq - 1
        sq_inside = [k * k for k in range(lo_i + 1, hi_i)]
        ans = sum(1 for n in range(lo_sq + 1, hi_sq) if math.isqrt(n) ** 2 != n)
        assert ans == total_between - len(sq_inside)
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-01",
            f"In an {ctx_en}, for how many integers {m('n')} is {m(r'\sqrt{n}')} an **irrational** number satisfying {m(rf'{lo_i} < \sqrt{{n}} < {hi_i}')}?",
            f"كم عدداً صحيحاً {m('n')} يجعل {m(r'\sqrt{n}')} **عدداً غير نسبي** يحقق المتباينة {m(rf'{lo_i} < \sqrt{{n}} < {hi_i}')}؟",
            ans, [total_between, ans - 1, total_between + 1],
            f"Square the inequality to get {m(f'{lo_sq} < n < {hi_sq}')}, then exclude any perfect squares inside that interval!",
            f"ربّع المتباينة لتحصل على {m(f'{lo_sq} < n < {hi_sq}')} ثم استبعد المربعات الكاملة الواقعة بينهما!",
            "Count all integers strictly inside the squared interval and subtract perfect squares.",
            [
                f"Squaring gives {m(f'{lo_sq} < n < {hi_sq}')}, which contains {m(f'{hi_sq} - {lo_sq} - 1 = {total_between}')} integers ({m(f'{lo_sq+1}')} through {m(f'{hi_sq-1}')}).",
                f"Inside this interval, {m(f'{lo_i+1}^2 = {(lo_i+1)**2}')} gives a rational root {m(str(lo_i+1))}.",
                f"Excluding that {m('1')} perfect square leaves {m(f'{total_between} - 1 = {ans}')} integers yielding irrational roots.",
            ],
            f"{m(f'{ans} + 1 = {total_between}')} total integers in {m(f'({lo_sq}, {hi_sq})')}.",
            "نحسب جميع الأعداد الصحيحة المحصورة ثم نطرح المربعات الكاملة لأن جذورها نسبية.",
            [
                f"بتربيع المتباينة نجد {m(f'{lo_sq} < n < {hi_sq}')}، وعدد الأعداد الصحيحة بينهما {m(f'{hi_sq} - {lo_sq} - 1 = {total_between}')}.",
                f"نستبعد المربع الكامل {m(str((lo_i+1)**2))} لأن جذره {m(str(lo_i+1))} عدد نسبي، فيتبقى {m(f'{total_between} - 1 = {ans}')}.",
            ],
            f"عدد القيم الصحيحة غير المربعة هو {m(str(ans))}.",
            diagram_en=svg_g9_real_number_line([lo_i, lo_i + 1, hi_i], lo_i + 0.5, "? irrational √n", f"Exclude n = {(lo_i+1)**2}"),
        ))

    # Hard 15: Sum of two irrational roots integer part
    qid = _qid(cur); cur += 1
    val15 = math.sqrt(31) + math.sqrt(18)
    ans15 = int(math.floor(val15))
    assert ans15 == 9 and 9.7 < val15 < 9.9
    qs.append(make_nafes_q(
        qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-01",
        f"A robotics arm extends a total length of {m(r'L = \sqrt{31} + \sqrt{18}')} cm. What is the greatest integer less than {m('L')}?",
        f"يمتد ذراع روبوتي بطول كلي قدره {m(r'L = \sqrt{31} + \sqrt{18}')} سم. ما أكبر عدد صحيح أصغر من {m('L')}؟",
        ans15, [8, 10, 7],
        f"Estimate {m(r'\sqrt{31}')} (just above {m('5.5')}) and {m(r'\sqrt{18}')} (just above {m('4.2')}) rather than only using integer bounds!",
        f"قدّر كلاً من {m(r'\sqrt{31}')} (أكبر قليلاً من {m('5.5')}) و{m(r'\sqrt{18}')} (أكبر قليلاً من {m('4.2')})!",
        "Use half-integer / one-decimal squares to tighten the interval around the sum.",
        [
            f"Check one-decimal squares: {m('5.5^2 = 30.25 < 31 < 31.36 = 5.6^2')}, so {m(r'5.5 < \sqrt{31} < 5.6')}.",
            f"Similarly, {m('4.2^2 = 17.64 < 18 < 18.49 = 4.3^2')}, so {m(r'4.2 < \sqrt{18} < 4.3')}.",
            f"Adding bounds gives {m('9.7 < L < 9.9')}, so {m('L')} lies strictly between {m('9')} and {m('10')}, making {m('9')} the greatest integer less than {m('L')}.",
        ],
        f"Notice integer bounds alone ({m('5 + 4 = 9')} to {m('6 + 5 = 11')}) are too wide; decimal squares prove {m('L < 9.9 < 10')}.",
        "نحصر كل جذر بمنزلة عشرية واحدة لكي لا يتجاوز المجموع عدداً صحيحاً بالخطأ.",
        [
            f"لدينا {m('5.5^2 = 30.25 < 31 < 5.6^2')} أي {m(r'5.5 < \sqrt{31} < 5.6')}.",
            f"وكذلك {m('4.2^2 = 17.64 < 18 < 4.3^2')} أي {m(r'4.2 < \sqrt{18} < 4.3')}.",
            f"بجمع المتباينتين نجد {m('9.7 < L < 9.9')}، فأكبر عدد صحيح أصغر من {m('L')} هو {m('9')}.",
        ],
        f"القيمة التقريبية {m('5.57 + 4.24 = 9.81')} تقع بين {m('9')} و{m('10')}.",
        diagram_en=svg_g9_real_number_line([7, 8, 10, 11], val15, "L = √31 + √18", "Greatest integer < L ?"),
    ))
    return qs


def _gen_num_02(start_idx: int) -> list[dict]:
    """G9-NUM-02: Simplifying, adding, subtracting & multiplying square-root radicals."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Simplify sqrt(k^2 * b)
    simp_cases = [
        (5, 3, "solar cell diagonal", "قطر خلية شمسية"),
        (7, 2, "laser path length", "طول مسار ليزر"),
        (6, 5, "rover wheel strut", "دعامة عجلة عربة استكشاف"),
    ]
    for k, b, ctx_en, ctx_ar in simp_cases:
        qid = _qid(cur); cur += 1
        n = k * k * b
        ans_s = rf"{k}\sqrt{{{b}}}"
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-02",
            f"A {ctx_en} measures {m(rf'\sqrt{{{n}}}')} cm. Write {m(rf'\sqrt{{{n}}}')} in simplest radical form.",
            f"يبلغ {ctx_ar} {m(rf'\sqrt{{{n}}}')} سم. اكتب {m(rf'\sqrt{{{n}}}')} في أبسط صورة جذرية.",
            ans_s, [rf"{b}\sqrt{{{k}}}", rf"{k*k}\sqrt{{{b}}}", rf"{k+1}\sqrt{{{b}}}"],
            f"Factor {m(str(n))} as {m(f'{k*k} \\times {b}')} using the largest perfect square {m(str(k*k))}.",
            f"حلّل العدد {m(str(n))} إلى {m(f'{k*k} \\times {b}')} باستخراج المربع الكامل {m(str(k*k))}.",
            f"Use {m(r'\sqrt{k^2 b} = k\sqrt{b}')}.",
            [
                f"Factor out the largest perfect square: {m(f'{n} = {k*k} \\times {b} = {k}^2 \\times {b}')}.",
                f"Take the square root of {m(f'{k}^2')}: {m(rf'\sqrt{{{n}}} = {k}\sqrt{{{b}}}')}.",
            ],
            f"Squaring back: {m(rf'({k}\sqrt{{{b}}})^2 = {k*k} \times {b} = {n}')}.",
            f"نستخرج الجذر التربيعي للمربع الكامل {m(str(k*k))}.",
            [
                f"نكتب {m(f'{n} = {k*k} \\times {b}')}.",
                f"إذن {m(rf'\sqrt{{{n}}} = \sqrt{{{k*k}}} \cdot \sqrt{{{b}}} = {k}\sqrt{{{b}}}')}.",
            ],
            f"بالتربيع العكسي: {m(f'{k*k} \\times {b} = {n}')}.",
            diagram_en=svg_function_machine(f"√{n}", f"√({k*k} × {b})", f"√{k*k} · √{b}", "?"),
        ))

    # Easy 4-5: Exact integer product sqrt(a) * sqrt(b)
    prod_easy = [
        (12, 27, "Riyadh Metro rectangular panel area", "مساحة لوح مستطيل في قطار الرياض"),
        (8, 50, "NEOM mirror array area", "مساحة مصفوفة مرآة في نيوم"),
    ]
    for a, b, ctx_en, ctx_ar in prod_easy:
        qid = _qid(cur); cur += 1
        ans = math.isqrt(a * b)
        assert ans * ans == a * b
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-02",
            f"The {ctx_en} equals {m(rf'\sqrt{{{a}}} \times \sqrt{{{b}}}')} {m(r'\text{cm}^2')}. What is this product as an exact integer?",
            f"تساوي {ctx_ar} المقدار {m(rf'\sqrt{{{a}}} \times \sqrt{{{b}}}')} سم². ما قيمة هذا الناتج كعدد صحيح دقيق؟",
            ans, [ans // 2, ans + 6, a + b],
            f"Multiply under one radical: {m(rf'\sqrt{{{a} \times {b}}}')}.",
            f"اضرب تحت جذر واحد: {m(rf'\sqrt{{{a} \times {b}}}')}.",
            f"Apply {m(r'\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}')}.",
            [
                f"Combine radicands: {m(rf'\sqrt{{{a}}} \times \sqrt{{{b}}} = \sqrt{{{a * b}}}')}.",
                f"Since {m(f'{ans}^2 = {a * b}')}, {m(rf'\sqrt{{{a * b}}} = {ans}')}.",
            ],
            f"Check via simplified radicals: {m(f'({ans})^2 = {a * b}')}.",
            f"نضرب ما تحت الجذرين ثم نأخذ الجذر التربيعي.",
            [
                f"{m(rf'\sqrt{{{a}}} \times \sqrt{{{b}}} = \sqrt{{{a * b}}} = {ans}')}.",
            ],
            f"تحقق: {m(f'{ans} \\times {ans} = {a * b}')}.",
            diagram_en=svg_number_strip([f"√{a}", f"× √{b}", f"= √{a*b}", "= ?"]),
        ))

    # Medium 6-10: Combining 3 like radicals
    comb_cases = [
        (2, 4, 1, 9, 1, 1, 3, "optical bench cable"),
        (3, 4, 2, 9, 1, 25, 2, "Yanbu pipe joint"),
        (4, 9, 1, 16, 2, 4, 5, "Abha bridge brace"),
        (5, 4, 2, 9, 3, 4, 7, "KAUST sensor mast"),
        (2, 25, 3, 4, 1, 9, 6, "Diriyah courtyard border"),
    ]
    for c1, sq1, c2, sq2, c3, sq3, b, ctx_en in comb_cases:
        qid = _qid(cur); cur += 1
        k1, k2, k3 = math.isqrt(sq1), math.isqrt(sq2), math.isqrt(sq3)
        r1, r2, r3 = sq1 * b, sq2 * b, sq3 * b
        coeff = c1 * k1 + c2 * k2 - c3 * k3
        ans_s = rf"{coeff}\sqrt{{{b}}}"
        expr = rf"{c1}\sqrt{{{r1}}} + {c2}\sqrt{{{r2}}} - {c3}\sqrt{{{r3}}}" if c3 > 1 else rf"{c1}\sqrt{{{r1}}} + {c2}\sqrt{{{r2}}} - \sqrt{{{r3}}}"
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-02",
            f"A {ctx_en} has net length {m(expr)} cm. Simplify this expression completely.",
            f"طول عنصر هندسي في المختبر يساوي {m(expr)} سم. بسّط هذه العبارة الجذرية في أبسط صورة.",
            ans_s, [rf"{coeff + 2*c3*k3}\sqrt{{{b}}}", rf"{coeff - 2}\sqrt{{{b}}}", rf"{c1 + c2 - c3}\sqrt{{{r1 + r2 - r3}}}"],
            f"Rewrite each radical as a multiple of {m(rf'\sqrt{{{b}}}')} before combining.",
            f"اكتب كل حد كمضاعف للجذر {m(rf'\sqrt{{{b}}}')} ثم اجمع واطرح المعاملات.",
            f"Extract perfect squares so every term contains {m(rf'\sqrt{{{b}}}')}.",
            [
                f"Simplify each term: {m(rf'{c1*k1}\sqrt{{{b}}} + {c2*k2}\sqrt{{{b}}} - {c3*k3}\sqrt{{{b}}}')}.",
                f"Combine coefficients: {m(f'({c1*k1} + {c2*k2} - {c3*k3})\\sqrt{{{b}}} = {coeff}\\sqrt{{{b}}}')}.",
            ],
            f"Coefficients check: {m(f'{c1*k1} + {c2*k2} - {c3*k3} = {coeff}')}.",
            f"نبسّط كل جذر ليصبح مضاعفاً لـ {m(rf'\sqrt{{{b}}}')}.",
            [
                f"بعد التبسيط: {m(rf'{c1*k1}\sqrt{{{b}}} + {c2*k2}\sqrt{{{b}}} - {c3*k3}\sqrt{{{b}}}')}.",
                f"بجمع وطرح المعاملات نحصل على {m(ans_s)}.",
            ],
            f"تحقق المعاملات: {m(f'{c1*k1} + {c2*k2} - {c3*k3} = {coeff}')}.",
            diagram_en=svg_function_machine(f"√{r1}, √{r2}, √{r3}", f"factor √{b}", f"{c1*k1}+{c2*k2}−{c3*k3}", "?"),
        ))

    # Hard 11-13: Conjugate & square radical identities
    conj_cases = [
        (r"(\sqrt{13} + \sqrt{5})(\sqrt{13} - \sqrt{5})", 8, [18, 6, 64], "13 - 5 = 8", "(√13 + √5)(√13 − √5)"),
        (r"(2\sqrt{6} + 3)(2\sqrt{6} - 3)", 15, [3, 21, 33], "24 - 9 = 15", "(2√6 + 3)(2√6 − 3)"),
        (r"(\sqrt{7} + \sqrt{3})^2 - 2\sqrt{21}", 10, [4, 14, 21], "7 + 2√21 + 3 - 2√21 = 10", "(√7 + √3)² − 2√21"),
    ]
    for idx_c, (expr, ans, dists, note, diag_lbl) in enumerate(conj_cases, 1):
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-02",
            f"In ETEC Grade 9 algebra benchmark #{idx_c}, evaluate the exact integer value of {m(expr)}.",
            f"في معيار الجبر للصف الثالث المتوسط (#{idx_c})، أوجد القيمة الصحيحة الدقيقة للمقدار {m(expr)}.",
            ans, dists,
            "Use special-product identities (difference of squares or square of a sum) to cancel radicals!",
            "استخدم متطابقة الفرق بين مربعين أو مربع المجموع لاختصار الجذور الصمّاء!",
            "Expand carefully using Grade 9 special products.",
            [
                f"Apply the algebraic identity directly to {m(expr)}.",
                f"Simplifying the radical terms yields {m(note)}, so the exact value is {m(str(ans))}.",
            ],
            f"All irrational radical terms cancel cleanly, leaving the integer {m(str(ans))}.",
            "نطبّق المتطابقة الجبرية فتختفي الحدود غير النسبية.",
            [
                f"بفك المقدار {m(expr)} وتبسيط الحدود المتشابهة نحصل على {m(str(ans))}.",
            ],
            f"الناتج الصحيح الدقيق هو {m(str(ans))}.",
            diagram_en=svg_number_strip([diag_lbl, "Special product", "= ?"]),
        ))

    # Hard 14-15: Radical equations for unknown n
    rad_eqs = [
        (r"\sqrt{n} + \sqrt{4n} + \sqrt{9n} = 30", 6, 30, 25, [5, 15, 36], "√n + √4n + √9n"),
        (r"\sqrt{16x} - \sqrt{x} = 18", 3, 18, 36, [6, 12, 81], "√16x − √x"),
    ]
    for eq_s, k_sum, rhs, ans, dists, diag_lhs in rad_eqs:
        qid = _qid(cur); cur += 1
        root_v = rhs // k_sum
        assert root_v * root_v == ans
        var = "n" if "n" in eq_s else "x"
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-02",
            f"If the positive integer {m(var)} satisfies {m(eq_s)}, what is the value of {m(var)}?",
            f"إذا كان العدد الصحيح الموجب {m(var)} يحقق المعادلة الجذرية {m(eq_s)}، فما قيمة {m(var)}؟",
            ans, dists,
            f"Factor {m(rf'\sqrt{{{var}}}')} out of every term first, solve for {m(rf'\sqrt{{{var}}}')}, and remember to square at the end!",
            f"استخرج {m(rf'\sqrt{{{var}}}')} عاملاً مشتركاً أولاً، ثم ربّع الطرفين في الخطوة الأخيرة!",
            f"Combine like radicals in {m(rf'\sqrt{{{var}}}')}, then square both sides.",
            [
                f"Simplify coefficients of {m(rf'\sqrt{{{var}}}')} to get {m(rf'{k_sum}\sqrt{{{var}}} = {rhs}')}.",
                f"Divide by {m(str(k_sum))}: {m(rf'\sqrt{{{var}}} = {root_v}')}, then square both sides: {m(f'{var} = {root_v}^2 = {ans}')}.",
            ],
            f"Substitute {m(f'{var} = {ans}')} back into {m(eq_s)} to verify {m(str(rhs))}.",
            f"نوحد الجذور بدلالة {m(rf'\sqrt{{{var}}}')} ثم نربّع الناتج.",
            [
                f"بتبسيط الجذور نحصل على {m(rf'{k_sum}\sqrt{{{var}}} = {rhs} \implies \sqrt{{{var}}} = {root_v}')}.",
                f"بتربيع الطرفين: {m(f'{var} = {ans}')}.",
            ],
            f"التعويض بـ {m(str(ans))} يحقق المعادلة {m(f'= {rhs}')}.",
            diagram_en=svg_number_strip([diag_lhs, f"= {rhs}", f"{var} = ?"]),
        ))
    return qs


def _gen_num_03(start_idx: int) -> list[dict]:
    """G9-NUM-03: Integer & zero/negative laws of exponents."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Direct exponent rules
    easy_exp = [
        (r"3^2 \times 3^3", 243, [81, 27, 15], "3^{2+3} = 3^5 = 243", "3² × 3³"),
        (r"\frac{5^7}{5^4}", 125, [25, 15, 625], "5^{7-4} = 5^3 = 125", "5⁷ ÷ 5⁴"),
        (r"(2^2)^3", 64, [32, 16, 12], "2^{2 \\times 3} = 2^6 = 64", "(2²)³"),
        (r"7^0 + 4^{-1}", Fraction(5, 4), [Fraction(1, 4), Fraction(3, 4), -3], "1 + 1/4 = 5/4", "7⁰ + 4⁻¹"),
        (r"3^{-2}", Fraction(1, 9), [-9, -6, Fraction(1, 6)], "1 / 3^2 = 1/9", "3⁻²"),
    ]
    for idx_e, (expr, ans, dists, step_s, lbl_s) in enumerate(easy_exp, 1):
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-03",
            f"In a Grade 9 digital memory check (#{idx_e}), what is the exact value of {m(expr)}?",
            f"في فحص ذاكرة رقمية للصف الثالث المتوسط (#{idx_e})، ما القيمة الدقيقة للمقدار {m(expr)}؟",
            ans, dists,
            "Apply the laws of integer, zero, and negative exponents carefully.",
            "طبّق قوانين الأسس الصحيحة والأس الصفري والسالب بدقة.",
            "Use product, quotient, power, zero, or negative-exponent rules.",
            [f"Applying the exponent law directly gives {m(step_s)}."],
            f"Verified exact value: {m(str(ans))}.",
            "نطبّق قانون الأسس المناسب مباشرة.",
            [f"بتطبيق قاعدة الأسس نحصل على: {m(step_s)}."],
            f"القيمة الدقيقة المؤكدة هي {m(str(ans))}.",
            diagram_en=svg_number_strip(["Input", lbl_s, "Law of Exponents", "= ?"]),
        ))

    # Medium 6-10: Multi-step quotients and negative fractional powers
    med_exp = [
        (r"\frac{3^4 \times (3^2)^3}{3^7}", 27, [9, 81, 18], "3^{4+6-7} = 3^3 = 27", "3⁴·(3²)³ ÷ 3⁷"),
        (r"\frac{2^{-3} \times 2^8}{2^2}", 8, [4, 16, 2], "2^{-3+8-2} = 2^3 = 8", "2⁻³·2⁸ ÷ 2²"),
        (r"\left(\frac{2}{3}\right)^{-3}", Fraction(27, 8), [Fraction(8, 27), Fraction(-27, 8), Fraction(9, 4)], "(3/2)^3 = 27/8", "(2/3)⁻³"),
        (r"\frac{6^5}{2^5 \times 3^3}", 9, [3, 18, 27], "(2^5 \\cdot 3^5)/(2^5 \\cdot 3^3) = 3^2 = 9", "6⁵ ÷ (2⁵·3³)"),
        (r"(4^{-1} + 2^{-1})^{-1}", Fraction(4, 3), [Fraction(3, 4), 6, Fraction(1, 6)], "(1/4 + 1/2)^{-1} = (3/4)^{-1} = 4/3", "(4⁻¹ + 2⁻¹)⁻¹"),
    ]
    for idx_m, (expr, ans, dists, step_s, lbl_s) in enumerate(med_exp, 1):
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-03",
            f"A SDAIA signal processor evaluates component #{idx_m} as {m(expr)}. Simplify this expression to an exact value.",
            f"يحسب معالج إشارات رقمي قيمة المكوّن رقم {idx_m} وفق العبارة {m(expr)}. أوجد القيمة المبسطة الدقيقة.",
            ans, dists,
            "Rewrite powers with common prime bases or reciprocals before simplifying.",
            "وحّد الأساسات أو اقلب الكسور ذات الأس السالب قبل التبسيط.",
            "Combine exponents systematically using product, power, and reciprocal rules.",
            [f"Simplify step-by-step: {m(step_s)}."],
            f"Result verified by direct fraction arithmetic.",
            "نبسّط القوى خطوةً بخطوة وفق قوانين الأسس.",
            [f"بالتبسيط المتدرج نجد: {m(step_s)}."],
            "النتيجة محققة حسابياً.",
            diagram_en=svg_function_machine(lbl_s, "Combine exponents", "Evaluate power", "?"),
        ))

    # Hard 11-15: Base-matching equations & equal-power sums
    hard_exp = [
        (f"Solve for {m('x')}: {m('4^{x + 1} = 2^{10}')}.", f"أوجد قيمة {m('x')} في المعادلة الأسية {m('4^{x + 1} = 2^{10}')}.", 4, [3, 5, 9], "2^{2(x+1)} = 2^{10} \\implies 2x + 2 = 10 \\implies x = 4", "4^(x+1) = 2¹⁰"),
        (f"Solve for {m('x')}: {m('9^{x - 1} \\times 3^4 = 3^{10}')}.", f"ما قيمة {m('x')} التي تحقق {m('9^{x - 1} \\times 3^4 = 3^{10}')}؟", 4, [3, 5, 6], "3^{2(x-1)+4} = 3^{10} \\implies 2x + 2 = 10 \\implies x = 4", "9^(x−1)·3⁴ = 3¹⁰"),
        (f"Solve for {m('x')}: {m('8^x = 4^6')}.", f"إذا كان {m('8^x = 4^6')}، فما قيمة {m('x')}؟", 4, [3, 6, 8], "2^{3x} = 2^{12} \\implies 3x = 12 \\implies x = 4", "8ˣ = 4⁶"),
        (f"If {m('2^{10} + 2^{10} = 2^k')}, what is the exponent {m('k')}?", f"إذا كان {m('2^{10} + 2^{10} = 2^k')}، فما قيمة الأس {m('k')}؟", 11, [20, 10, 12], "2 \\times 2^{10} = 2^{1+10} = 2^{11} \\implies k = 11", "2¹⁰ + 2¹⁰ = 2ᵏ"),
        (f"If {m('3^8 + 3^8 + 3^8 = 3^m')}, what is the exponent {m('m')}?", f"إذا كان {m('3^8 + 3^8 + 3^8 = 3^m')}، فما قيمة الأس {m('m')}؟", 9, [24, 8, 27], "3 \\times 3^8 = 3^{1+8} = 3^9 \\implies m = 9", "3⁸ + 3⁸ + 3⁸ = 3ᵐ"),
    ]
    for q_en, q_ar, ans, dists, step_s, lbl_s in hard_exp:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-03",
            q_en, q_ar, ans, dists,
            "Express every term using the same prime base, or factor out the repeated power!",
            "اكتب جميع الحدود بنفس الأساس الأولي، أو استخرج القوة المتكررة عاملاً مشتركاً!",
            "Match prime bases so exponents can be equated directly.",
            [f"Rewrite using a common prime base: {m(step_s)}."],
            f"Substituting {m(str(ans))} makes both sides identical.",
            "نوحد الأساس الأولي في الطرفين ثم نساوي الأسس.",
            [f"بتوحيد الأساس نجد: {m(step_s)}."],
            f"التعويض بالقيمة {m(str(ans))} يجعل الطرفين متساويين تماماً.",
            diagram_en=svg_number_strip([lbl_s, "Common prime base", f"Answer = ?"]),
        ))
    return qs


def _gen_num_04(start_idx: int) -> list[dict]:
    """G9-NUM-04: Scientific notation conversions & products/quotients."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Standard <-> Scientific notation
    sci_easy = [
        ("NEOM solar farm daily output of 6,400,000 Wh", "إنتاج محطة طاقة شمسية في نيوم وقدره 6,400,000 واط·ساعة", r"6.4 \times 10^6", [r"64 \times 10^5", r"6.4 \times 10^5", r"0.64 \times 10^7"]),
        ("Red Sea coral microbe diameter of 0.00042 m", "قطر كائن مجهري بحري وقدره 0.00042 متر", r"4.2 \times 10^{-4}", [r"4.2 \times 10^{-5}", r"42 \times 10^{-5}", r"4.2 \times 10^4"]),
        ("Saudi fiber-optic packet count of 93,000,000", "عدد حزم بيانات ألياف ضوئية وقدره 93,000,000", r"9.3 \times 10^7", [r"9.3 \times 10^6", r"93 \times 10^6", r"9.3 \times 10^8"]),
        ("silica membrane pore width of 0.0000075 m", "عرض مسام غشاء تحلية وقدره 0.0000075 متر", r"7.5 \times 10^{-6}", [r"7.5 \times 10^{-5}", r"75 \times 10^{-7}", r"7.5 \times 10^{-7}"]),
        ("standard decimal value of 3.08 × 10⁴ meters", "القيمة القياسية للعدد 3.08 × 10⁴ متراً", 30800, [3080, 308000, 3800]),
    ]
    for ctx_en, ctx_ar, ans, dists in sci_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-04",
            f"Express the {ctx_en} in the requested standard/scientific form.",
            f"عبّر عن {ctx_ar} بالصيغة العلمية أو القياسية الصحيحة.",
            ans, dists,
            f"Count how many places the decimal point shifts so the coefficient lies in {m('[1, 10)')}.",
            f"عُدّ عدد المنازل التي تتحركها الفاصلة العشرية ليكون المعامل بين {m('1')} وأقل من {m('10')}.",
            f"Standard scientific notation requires {m(r'1 \le |a| < 10')}.",
            [f"Moving the decimal point cleanly yields {m(str(ans))}."],
            "Coefficient and power of 10 verified.",
            f"نحرك الفاصلة العشرية لتحقيق شرط المعامل {m('1 \\le |a| < 10')}.",
            [f"بتحريك الفاصلة بعدد المنازل الصحيح نحصل على {m(str(ans))}."],
            "تم التحقق من المعامل وأس العشرة.",
            diagram_en=svg_nafes_function_table(["Quantity", "Target Form"], [[ctx_en[:24], "?"]], highlight_cell=(0, 1)),
        ))

    # Medium 6-10: Products and quotients in scientific notation
    sci_med = [
        (r"(5 \times 10^4)(6 \times 10^3)", r"3 \times 10^8", [r"30 \times 10^7", r"3 \times 10^7", r"1.1 \times 10^8"], "30 × 10⁷ = 3 × 10⁸"),
        (r"(8 \times 10^{-3})(2.5 \times 10^7)", r"2 \times 10^5", [r"20 \times 10^4", r"2 \times 10^4", r"2 \times 10^{-21}"], "20 × 10⁴ = 2 × 10⁵"),
        (r"\frac{9.6 \times 10^8}{3.2 \times 10^3}", r"3 \times 10^5", [r"3 \times 10^{11}", r"3 \times 10^4", r"6.4 \times 10^5"], "(9.6/3.2) × 10^{8-3}"),
        (r"\frac{1.8 \times 10^5}{6 \times 10^{-2}}", r"3 \times 10^6", [r"0.3 \times 10^7", r"3 \times 10^7", r"3 \times 10^2"], "0.3 × 10⁷ = 3 × 10⁶"),
        (r"(4.5 \times 10^{-4})(4 \times 10^{-2})", r"1.8 \times 10^{-5}", [r"18 \times 10^{-6}", r"1.8 \times 10^{-6}", r"1.8 \times 10^{-7}"], "18 × 10⁻⁶ = 1.8 × 10⁻⁵"),
    ]
    for idx_s, (expr, ans, dists, note) in enumerate(sci_med, 1):
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-04",
            f"In physics lab calculation #{idx_s}, write {m(expr)} in **standard scientific notation**.",
            f"في حساب فيزيائي رقم {idx_s}، اكتب ناتج {m(expr)} بالصيغة العلمية القياسية.",
            ans, dists,
            f"Operate on coefficients and powers of {m('10')} separately, then adjust the coefficient into {m('[1, 10)')}!",
            f"أجرِ العملية على المعاملات وأسس {m('10')}، ثم اضبط المعامل ليكون في الفترة {m('[1, 10)')}!",
            "Normalize any coefficient outside [1, 10).",
            [f"Compute raw result and normalize: {m(note)}, giving {m(ans)}."],
            f"Coefficient lies in {m('[1, 10)')}.",
            "نحسب الناتج الأولي ثم نضبط الفاصلة العشرية للصيغة القياسية.",
            [f"التبسيط يعطي {m(note)} أي {m(ans)}."],
            "المعامل يحقق شرط الصيغة العلمية القياسية.",
            diagram_en=svg_function_machine("Compute raw", note.split("=")[0].strip(), "Normalize [1,10)", "?"),
        ))

    # Hard 11-15: Sums, differences & ratio comparisons in scientific notation
    sci_hard = [
        (f"Evaluate {m(r'(4.2 \times 10^6) + (8 \times 10^5)')} in standard scientific notation.",
         f"أوجد ناتج الجمع {m(r'(4.2 \times 10^6) + (8 \times 10^5)')} بالصيغة العلمية القياسية.",
         r"5 \times 10^6", [r"1.22 \times 10^7", r"5 \times 10^{11}", r"4.28 \times 10^6"], "4.2×10⁶ + 0.8×10⁶ = 5×10⁶"),
        (f"Evaluate {m(r'(6.5 \times 10^7) - (5 \times 10^6)')} in standard scientific notation.",
         f"أوجد ناتج الطرح {m(r'(6.5 \times 10^7) - (5 \times 10^6)')} بالصيغة العلمية القياسية.",
         r"6 \times 10^7", [r"1.5 \times 10^7", r"6 \times 10^6", r"6.45 \times 10^7"], "6.5×10⁷ − 0.5×10⁷ = 6×10⁷"),
        (f"Reservoir A holds {m(r'7.2 \times 10^8')} L of water and Reservoir B holds {m(r'1.8 \times 10^6')} L. How many times as much water does A hold as B?",
         f"سعة الخزان (أ) تساوي {m(r'7.2 \times 10^8')} لتر وسعة الخزان (ب) تساوي {m(r'1.8 \times 10^6')} لتر. كم مرة تعادل سعة (أ) سعة (ب)؟",
         400, [40, 4000, 4], "(7.2/1.8) × 10² = 400"),
        (f"A rectangular solar zone in Tabuk is {m(r'5 \times 10^3')} m long and {m(r'2.4 \times 10^3')} m wide. What is its area in {m(r'\text{m}^2')} in scientific notation?",
         f"منطقة ألواح شمسية مستطيلة في تبوك طولها {m(r'5 \times 10^3')} م وعرضها {m(r'2.4 \times 10^3')} م. ما مساحتها بالمتر المربع بالصيغة العلمية؟",
         r"1.2 \times 10^7", [r"12 \times 10^6", r"1.2 \times 10^6", r"7.4 \times 10^6"], "12 × 10⁶ = 1.2 × 10⁷"),
        (f"Light travels {m(r'3 \times 10^8')} m/s. How many meters does light travel in {m('5')} minutes ({m('300')} seconds), in scientific notation?",
         f"تبلغ سرعة الضوء {m(r'3 \times 10^8')} م/ث. كم متراً يقطع الضوء في {m('5')} دقائق ({m('300')} ثانية) بالصيغة العلمية؟",
         r"9 \times 10^{10}", [r"1.5 \times 10^9", r"9 \times 10^9", r"900 \times 10^8"], "3×10⁸ × 3×10² = 9×10¹⁰"),
    ]
    for q_en, q_ar, ans, dists, note in sci_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-04",
            q_en, q_ar, ans, dists,
            "Match powers of 10 before adding/subtracting, or divide/multiply powers cleanly.",
            "وحّد قوى العدد 10 قبل الجمع أو الطرح، واضبط المعامل في الضرب والقسمة.",
            "Rewrite terms with a common power of 10 or apply scientific-notation product/quotient laws.",
            [f"Step calculation: {m(note)}, giving {m(str(ans))}."],
            "Verified by converting both sides to standard value.",
            "نوحد قوى العشرة ثم نبسّط المعامل.",
            [f"الحساب خطوة بخطوة: {m(note)} فنحصل على {m(str(ans))}."],
            "تم التحقق من صحة الناتج.",
            diagram_en=svg_number_strip([note.split("=")[0].strip(), "= ?"]),
        ))
    return qs


# ==============================================================================
# UNIT 3.2 (G9-NUM-05 .. G9-NUM-08): Percents, Variation, Work/Motion & Mixtures
# ==============================================================================

def _gen_num_05(start_idx: int) -> list[dict]:
    """G9-NUM-05: Percent increase/decrease, VAT (15%) / discount chains & reverse original price."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Single VAT / discount / percent change
    easy_pct = [
        ("A Riyadh bookstore lists a scientific calculator at 400 SAR before 15% VAT. What is the final price in SAR including VAT?",
         "يعرض متجر بالرياض آلة حاسبة علمية بسعر 400 ريال قبل ضريبة القيمة المضافة (15%). ما السعر النهائي شاملاً الضريبة بالريال؟",
         460, [415, 440, 340], "", "400 × 1.15 = 460", ("400 SAR", "+15% VAT", "Final price", "? SAR")),
        ("A lab microscope priced at 1,200 SAR is sold at a 25% seasonal discount. What is the sale price in SAR?",
         "مجهر مختبر سعره 1,200 ريال يُباع بخصم موسمي نسبته 25%. ما سعر البيع بعد الخصم بالريال؟",
         900, [950, 800, 300], "", "1200 × 0.75 = 900", ("1,200 SAR", "−25% sale", "Sale price", "? SAR")),
        ("An engineering tablet costs 800 SAR before 15% VAT. How much VAT alone (in SAR) is added to the bill?",
         "جهاز لوحي هندسي سعره 800 ريال قبل ضريبة القيمة المضافة 15%. كم ريالاً تبلغ قيمة الضريبة المضافة وحدها؟",
         120, [920, 80, 150], "", "800 × 0.15 = 120", ("800 SAR", "15% VAT", "VAT amount", "? SAR")),
        ("Monthly solar output rose from 250 MWh to 300 MWh. What is the percentage increase?",
         "ارتفع الإنتاج الشهري لمحطة شمسية من 250 إلى 300 ميجاواط·ساعة. ما النسبة المئوية للزيادة؟",
         25, [50, 16, 20], r"\%", "(50 / 250) × 100% = 20%", ("250 MWh", "→ 300 MWh", "% increase", "? %")),
        ("Water loss in an irrigation pipe dropped from 600 L/day to 450 L/day. What is the percentage decrease?",
         "انخفض الفاقد المائي في أنبوب ري من 600 لتر يومياً إلى 450 لتراً يومياً. ما النسبة المئوية للنقصان؟",
         25, [20, 33, 15], r"\%", "(150 / 600) × 100% = 25%", ("600 L/d", "→ 450 L/d", "% decrease", "? %")),
    ]
    easy_pct[3] = (
        "Monthly solar output rose from 250 MWh to 300 MWh. What is the percentage increase?",
        "ارتفع الإنتاج الشهري لمحطة شمسية من 250 إلى 300 ميجاواط·ساعة. ما النسبة المئوية للزيادة؟",
        20, [50, 16, 25], r"\%", "(50 / 250) × 100% = 20%", ("250 MWh", "→ 300 MWh", "% increase", "? %"),
    )
    for q_en, q_ar, ans, dists, sfx, step_s, fm_args in easy_pct:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-05",
            q_en, q_ar, ans, dists,
            "Divide change by the ORIGINAL value, or multiply by (1 ± rate).",
            "اقسم مقدار التغير على القيمة الأصلية، أو اضرب في المعامل (1 ± النسبة).",
            "Apply direct percentage multiplier relative to the initial amount.",
            [f"Compute directly: {m(step_s)}."],
            f"Verified exact result: {m(str(ans) + sfx)}.",
            "نطبّق قانون النسبة المئوية على القيمة الأصلية.",
            [f"بحساب النسبة مباشرة: {m(step_s)}."],
            f"الناتج المؤكد هو {m(str(ans) + sfx)}.",
            suffix=sfx,
            diagram_en=svg_function_machine(*fm_args),
        ))

    # Medium 6-10: Chained discount + VAT & single-step reverse original price
    med_pct = [
        ("A 2,000 SAR robotics kit gets a 10% student discount, then 15% VAT is added to the discounted price. What is the final amount paid in SAR?",
         "حقيبة روبوتات سعرها 2,000 ريال خضعت لخصم طلابي 10% ثم أُضيفت ضريبة القيمة المضافة 15% على السعر بعد الخصم. كم يدفع المشتري بالريال؟",
         2070, [2100, 2000, 1800], "2000 × 0.90 × 1.15 = 2070", ("2,000 SAR", "−10% disc.", "+15% VAT", "? SAR")),
        ("A 1,000 SAR sensor array receives a 20% discount followed by 15% VAT. What is the final invoice total in SAR?",
         "مصفوفة مستشعرات سعرها 1,000 ريال خُفضت بنسبة 20% ثم أُضيفت ضريبة 15%. ما إجمالي الفاتورة النهائية بالريال؟",
         920, [950, 960, 850], "1000 × 0.80 × 1.15 = 920", ("1,000 SAR", "−20% disc.", "+15% VAT", "? SAR")),
        ("A 5,000 SAR 3D printer is discounted by 30%, then 15% VAT is applied. What is the final price in SAR?",
         "طابعة ثلاثية الأبعاد سعرها 5,000 ريال خُصم منها 30% ثم أُضيفت ضريبة 15%. ما السعر النهائي بالريال؟",
         4025, [4250, 3500, 4150], "5000 × 0.70 × 1.15 = 4025", ("5,000 SAR", "−30% disc.", "+15% VAT", "? SAR")),
        ("A customer paid 575 SAR for a spare part **including** 15% VAT. What was the pre-tax price in SAR?",
         "دفع عميل 575 ريالاً ثمناً لقطعة غيار **شاملاً** ضريبة القيمة المضافة 15%. فما سعر القطعة قبل الضريبة بالريال؟",
         500, [488, 515, 490], "575 ÷ 1.15 = 500", ("Pre-tax ?", "+15% VAT", "Invoice", "575 SAR")),
        ("After a 15% discount, a telescope costs 680 SAR. What was its original price before the discount in SAR?",
         "بيع تلسكوب بمبلغ 680 ريالاً بعد خصم نسبته 15%. ما سعره الأصلي قبل الخصم بالريال؟",
         800, [782, 795, 820], "680 ÷ 0.85 = 800", ("Original ?", "−15% sale", "Sale price", "680 SAR")),
    ]
    for q_en, q_ar, ans, dists, step_s, fm_args in med_pct:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-05",
            q_en, q_ar, ans, dists,
            "Multiply successive decimal factors (never add percentages), and divide by the factor to reverse!",
            "اضرب المعاملات العشرية المتتابعة، واقسم على المعامل لإيجاد السعر الأصلي!",
            "Use multiplicative percent factors.",
            [f"Calculation: {m(step_s)}."],
            "Forward multiplication check confirms the exact SAR invoice.",
            "نستخدم المعامل الضربي للتغير المئوي.",
            [f"الحساب الدقيق: {m(step_s)}."],
            "التحقق العكسي يؤكد صحة المبلغ بالريال.",
            diagram_en=svg_function_machine(*fm_args),
        ))

    # Hard 11-15: Reverse chained percent & net compound change
    hard_pct = [
        ("A workstation gets a 20% discount and then 15% VAT, resulting in a final bill of 1,656 SAR. What was the original price in SAR?",
         "خضع جهاز حاسوب لخصم 20% ثم أُضيفت ضريبة القيمة المضافة 15% فبلغت الفاتورة النهائية 1,656 ريالاً. ما السعر الأصلي بالريال؟",
         1800, [1740, 1900, 1600], "", "1656 ÷ (0.80 × 1.15) = 1656 ÷ 0.92 = 1800", ("Original ?", "−20% disc.", "+15% VAT", "1,656 SAR")),
        ("During two clearance rounds, a solar battery's price is reduced by 20% and then by an additional 10% to reach 1,512 SAR. What was its initial price in SAR?",
         "في جولتي تخفيض متتاليتين، خُفّض سعر بطارية شمسية بنسبة 20% ثم بنسبة إضافية 10% فأصبح 1,512 ريالاً. ما سعرها الابتدائي بالريال؟",
         2100, [2160, 2000, 1980], "", "1512 ÷ (0.80 × 0.90) = 1512 ÷ 0.72 = 2100", ("Initial ?", "−20% (R1)", "−10% (R2)", "1,512 SAR")),
        ("An oscilloscope receives a 10% discount followed by 15% VAT, giving a final price of 2,484 SAR. What was its original price in SAR?",
         "حصل جهاز راسم إشارة على خصم 10% ثم ضريبة 15% فأصبح سعره النهائي 2,484 ريالاً. ما سعره الأصلي بالريال؟",
         2400, [2360, 2500, 2250], "", "2484 ÷ (0.90 × 1.15) = 2484 ÷ 1.035 = 2400", ("Original ?", "−10% disc.", "+15% VAT", "2,484 SAR")),
        ("A stock index rises by 25% in Quarter 1 and drops by 20% in Quarter 2. What is the net percentage change over the two quarters?",
         "ارتفع مؤشر بنسبة 25% في الربع الأول ثم انخفض بنسبة 20% في الربع الثاني. ما صافي التغير المئوي خلال الربعين؟",
         0, [5, -5, 2], r"\%", "1.25 × 0.80 = 1.00 ⇒ 0%", ("100%", "+25% (Q1)", "−20% (Q2)", "Net Δ% ?")),
        ("Factory output increases by 40% in year 1 and decreases by 25% in year 2. What is the net percentage increase over the two years?",
         "زاد إنتاج مصنع بنسبة 40% في السنة الأولى ثم انخفض بنسبة 25% في السنة الثانية. ما نسبة الزيادة الصافية خلال السنتين؟",
         5, [15, 10, 8], r"\%", "1.40 × 0.75 = 1.05 ⇒ +5%", ("100%", "+40% (Yr 1)", "−25% (Yr 2)", "Net Δ% ?")),
    ]
    for q_en, q_ar, ans, dists, sfx, step_s, fm_args in hard_pct:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-05",
            q_en, q_ar, ans, dists,
            "Compute the combined product of the two multipliers first!",
            "احسب حاصل ضرب المعاملين العشريين أولاً!",
            "Combine both percentage stages into one composite multiplier.",
            [f"Composite multiplier step: {m(step_s)}."],
            "Verified by applying both stages sequentially to the initial value.",
            "ندمج المرحلتين في معامل ضربي واحد.",
            [f"خطوة المعامل المركب: {m(step_s)}."],
            "بالتجريب الأمامي على القيمة الأصلية يتطابق الناتج.",
            suffix=sfx,
            diagram_en=svg_function_machine(*fm_args),
        ))
    return qs


def _gen_num_06(start_idx: int) -> list[dict]:
    """G9-NUM-06: Direct variation (y = kx) & inverse variation (xy = k)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Direct variation y = kx
    dir_easy = [(4, 36, 7), (6, 45, 10), (5, 65, 8)]
    for idx_d, (x1, y1, x2) in enumerate(dir_easy, 1):
        qid = _qid(cur); cur += 1
        ans = (y1 * x2) // x1
        assert y1 * x2 == ans * x1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-06",
            f"In direct-variation experiment #{idx_d}, {m('y')} varies directly with {m('x')}. If {m(f'y = {y1}')} when {m(f'x = {x1}')}, what is {m('y')} when {m(f'x = {x2}')}?",
            f"في تجربة تغير طردي رقم {idx_d}، تتغير {m('y')} طردياً مع {m('x')}. إذا كانت {m(f'y = {y1}')} عندما {m(f'x = {x1}')}، فما قيمة {m('y')} عندما {m(f'x = {x2}')}؟",
            ans, [ans + 9, ans - 6, (x1 * y1) // max(1, x2)],
            f"In direct variation, the ratio {m('y / x')} remains constant.",
            f"في التغير الطردي تكون النسبة {m('y / x')} ثابتة.",
            f"Use {m('y_1 / x_1 = y_2 / x_2')}.",
            [f"Set up {m(rf'\frac{{{y1}}}{{{x1}}} = \frac{{y}}{{{x2}}} \implies y = \frac{{{y1} \times {x2}}}{{{x1}}} = {ans}')}."],
            f"{m(f'{y1}/{x1} = {ans}/{x2}')}.",
            f"نطبق تناسب التغير الطردي {m('y_1 / x_1 = y_2 / x_2')}.",
            [f"نجد {m(rf'y = \frac{{{y1} \times {x2}}}{{{x1}}} = {ans}')}."],
            f"النسبتان متساويتان.",
            diagram_en=svg_nafes_function_table(["x", "y (Direct)"], [[str(x1), str(y1)], [str(x2), "?"]], highlight_cell=(1, 1)),
        ))

    # Easy 4-5: Inverse variation xy = k
    inv_easy = [(6, 14, 7), (8, 15, 10)]
    for idx_i, (x1, y1, x2) in enumerate(inv_easy, 1):
        qid = _qid(cur); cur += 1
        ans = (x1 * y1) // x2
        assert x1 * y1 == ans * x2
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-06",
            f"In inverse-variation test #{idx_i}, {m('y')} varies inversely with {m('x')}. If {m(f'y = {y1}')} when {m(f'x = {x1}')}, what is {m('y')} when {m(f'x = {x2}')}?",
            f"في اختبار تغير عكسي رقم {idx_i}، تتغير {m('y')} عكسياً مع {m('x')}. إذا كانت {m(f'y = {y1}')} عندما {m(f'x = {x1}')}، فما قيمة {m('y')} عندما {m(f'x = {x2}')}؟",
            ans, [(y1 * x2) // max(1, x1), ans + 4, ans - 3],
            f"In inverse variation, the product {m('x \\cdot y')} stays constant.",
            f"في التغير العكسي يكون حاصل الضرب {m('x \\cdot y')} ثابتاً.",
            f"Use {m('x_1 y_1 = x_2 y_2')}.",
            [f"Constant product {m(f'k = {x1} \\times {y1} = {x1*y1}')}, so {m(f'y = {x1*y1} \\div {x2} = {ans}')}."],
            f"{m(f'{x1} \\times {y1} = {x2} \\times {ans} = {x1*y1}')}.",
            f"نطبق قانون التغير العكسي {m('x_1 y_1 = x_2 y_2')}.",
            [f"حاصل الضرب {m(f'{x1} \\times {y1} = {x1*y1}')}، ومنه {m(f'y = {x1*y1} \\div {x2} = {ans}')}."],
            f"التحقق: {m(f'{x2} \\times {ans} = {x1*y1}')}.",
            diagram_en=svg_nafes_function_table(["x", "y (Inverse)"], [[str(x1), str(y1)], [str(x2), "?"]], highlight_cell=(1, 1)),
        ))

    # Medium 6-10: Applied gears, workers, solar wattage, pipes, shadows
    med_var = [
        ("A driving gear with 36 teeth rotates at 150 rpm and meshes with a driven gear of 45 teeth. At how many rpm does the driven gear rotate?",
         "يدور ترس قائد ذو 36 سناً بسرعة 150 دورة/دقيقة ويتعشق مع ترس مقاد ذي 45 سناً. كم دورة في الدقيقة يدور الترس المقاد؟",
         120, [180, 135, 100], "36 × 150 = 45 × R ⇒ R = 120", ["36 teeth @ 150 rpm", "45 teeth", "? rpm"]),
        ("At a Diriyah heritage wall, 15 masons finish a restoration section in 12 days. How many days would 20 masons working at the same rate need?",
         "يُنهي 15 بنّاءً ترميم جدار تراثي في الدرعية خلال 12 يوماً. كم يوماً يحتاج 20 بنّاءً يعملون بالمعدل نفسه؟",
         9, [16, 8, 10], "15 × 12 = 20 × d ⇒ d = 9", ["15 masons → 12 d", "20 masons", "? days"]),
        ("A NEOM solar panel array of area 18 m² generates 3,600 W under peak sun (direct variation). How many watts does a 25 m² array of the same type generate?",
         "تولّد مصفوفة شمسية في نيوم مساحتها 18 م² قدرة 3,600 واط (تغير طردي). كم واط تولّد مصفوفة مماثلة مساحتها 25 م²؟",
         5000, [4500, 4800, 5400], "(3600 / 18) × 25 = 5000", ["18 m² → 3,600 W", "25 m²", "? W"]),
        ("Six identical Yanbu transfer pipes fill a storage tank in 14 hours. How many hours will 7 identical pipes take to fill the same tank?",
         "تملأ 6 أنابيب متماثلة خزاناً في ينبع خلال 14 ساعة. كم ساعة تستغرق 7 أنابيب مماثلة لملء الخزان نفسه؟",
         12, [16, 10, 11], "6 × 14 = 7 × t ⇒ t = 12", ["6 pipes → 14 h", "7 pipes", "? h"]),
        ("Under Hooke's spring law (direct variation), a 12 N load stretches a lab spring by 9 cm. How many centimeters will a 20 N load stretch it?",
         "وفق قانون النابض (تغير طردي)، قوة 12 نيوتن تطيل نابضاً بمقدار 9 سم. كم سنتيمتراً تطيله قوة مقدارها 20 نيوتن؟",
         15, [12, 16, 18], "(9 / 12) × 20 = 15", ["12 N → 9 cm", "20 N", "? cm"]),
    ]
    for q_en, q_ar, ans, dists, step_s, diag_cells in med_var:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-06",
            q_en, q_ar, ans, dists,
            "Decide first whether increasing the first quantity increases (direct) or decreases (inverse) the second!",
            "حدد أولاً هل زيادة الكمية الأولى تزيد الثانية (طردي) أم تنقصها (عكسي)!",
            "Model with y/x = k (direct) or x·y = k (inverse).",
            [f"Set up and solve: {m(step_s)}."],
            "Physical direction of change matches the answer.",
            "نحدد نوع التغير ثم نطبّق المعادلة المناسبة.",
            [f"بتطبيق العلاقة: {m(step_s)}."],
            "اتجاه التغير الفيزيائي يتوافق مع الناتج.",
            diagram_en=svg_number_strip(diag_cells),
        ))

    # Hard 11-15: Additional workers needed, 3-gear chain, inverse-square/multi-step variation
    hard_var = [
        ("A contractor employs 12 technicians to wire a Riyadh Metro station in 15 days. How many **additional** technicians must join from day 1 to finish in 10 days?",
         "عيّن مقاول 12 فنياً لتمديد كابلات محطة قطار الرياض في 15 يوماً. كم فنياً **إضافياً** يجب إضافتهم منذ البداية لإنهاء العمل في 10 أيام؟",
         6, [18, 8, 5], "12 × 15 = 180; 180 ÷ 10 = 18 total; 18 − 12 = 6 additional"),
        ("Eight robotic welders complete a chassis batch in 18 hours. How many **more** welders are needed to finish the same batch in 12 hours?",
         "تُنهي 8 روبوتات لحام دفعة هياكل في 18 ساعة. كم روبوتاً **إضافياً** يلزم لإنهاء الدفعة نفسها في 12 ساعة؟",
         4, [12, 6, 3], "8 × 18 = 144; 144 ÷ 12 = 12 total; 12 − 8 = 4 more"),
        ("Gear A (48 teeth) turns at 100 rpm and drives Gear B (32 teeth), which drives Gear C (60 teeth). At how many rpm does Gear C turn?",
         "ترس (أ) ذو 48 سناً يدور بسرعة 100 دورة/دقيقة ويدير الترس (ب) ذا 32 سناً الذي يدير الترس (ج) ذا 60 سناً. كم سرعة دوران الترس (ج)؟",
         80, [150, 120, 75], "48 × 100 = 60 × R_C ⇒ R_C = 80"),
    ]
    for q_en, q_ar, ans, dists, step_s in hard_var:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-06",
            q_en, q_ar, ans, dists,
            "Watch whether the question asks for the ADDITIONAL count rather than the new total!",
            "انتبه جيداً: هل المطلوب العدد الكلي الجديد أم العدد الإضافي فقط!",
            "Use constant product k = x·y, then subtract initial count if asked for additional units.",
            [f"Compute step-by-step: {m(step_s)}."],
            "Total × time equals the original work product.",
            "نحسب العدد الكلي من التغير العكسي ثم نطرح العدد الابتدائي عند طلب الإضافي.",
            [f"الحل المتدرج: {m(step_s)}."],
            "حاصل الضرب الكلي ثابت.",
            diagram_en=svg_nafes_function_table(["Scenario", "Product = k"], [["Initial", step_s.split(";")[0].split("⇒")[0].strip()], ["Target", "?"]], highlight_cell=(1, 1)),
        ))

    # Hard 14
    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-06",
        f"Quantity {m('y')} varies inversely with {m('x')} such that {m('xy = 120')}. By how much does {m('y')} **decrease** when {m('x')} increases from {m('6')} to {m('15')}?",
        f"تتغير {m('y')} عكسياً مع {m('x')} بحيث {m('xy = 120')}. ما مقدار **النقصان** في قيمة {m('y')} عندما تزداد {m('x')} من {m('6')} إلى {m('15')}؟",
        12, [8, 20, 9],
        f"Compute {m('y_1 = 120/6')} and {m('y_2 = 120/15')}, then find {m('y_1 - y_2')}.",
        f"احسب {m('y_1 = 120/6')} و{m('y_2 = 120/15')} ثم أوجد الفرق {m('y_1 - y_2')}.",
        "Evaluate y at both endpoints and subtract.",
        [f"At {m('x = 6')}, {m('y_1 = 120 / 6 = 20')}; at {m('x = 15')}, {m('y_2 = 120 / 15 = 8')}.", f"Decrease: {m('20 - 8 = 12')}."],
        f"{m('20 - 12 = 8')} and {m('15 \\times 8 = 120')}.",
        "نحسب قيمتي y قبل وبعد التغير ثم نطرحهما.",
        [f"عند {m('x=6')} تكون {m('y_1=20')}، وعند {m('x=15')} تكون {m('y_2=8')}، فمقدار النقصان {m('20 - 8 = 12')}."],
        f"{m('15 \\times 8 = 120')}.",
        diagram_en=svg_nafes_function_table(["x", "y = 120/x"], [["6", "20"], ["15", "8"], ["Δy", "?"]], highlight_cell=(2, 1)),
    ))

    # Hard 15
    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-06",
        f"Variable {m('z')} varies directly with {m('x')} and inversely with {m('y')} ({m('z = kx/y')}). If {m('z = 18')} when {m('x = 6')} and {m('y = 4')}, what is {m('z')} when {m('x = 10')} and {m('y = 15')}?",
        f"يتغير المتغير {m('z')} طردياً مع {m('x')} وعكسياً مع {m('y')} وفق العلاقة {m('z = kx/y')}. إذا كانت {m('z = 18')} عندما {m('x = 6')} و{m('y = 4')}، فما قيمة {m('z')} عندما {m('x = 10')} و{m('y = 15')}؟",
        8, [12, 6, 45],
        f"Solve for the constant {m('k = zy / x')} first, then substitute {m('x = 10, y = 15')}.",
        f"أوجد ثابت التناسب {m('k = zy / x')} أولاً، ثم عوّض بـ {m('x = 10')} و{m('y = 15')}.",
        "Find k from initial values, then evaluate z.",
        [f"From {m('18 = k(6)/4')}, we get {m('k = 12')}.", f"Then {m('z = 12(10) / 15 = 120 / 15 = 8')}."],
        f"{m('z y / x = 8 \\times 15 / 10 = 12 = 18 \\times 4 / 6')}.",
        "نحسب ثابت التناسب المشترك k ثم نعوّض بالقيم الجديدة.",
        [f"ثابت التناسب {m('k = (18 \\times 4)/6 = 12')}، ومنه {m('z = (12 \\times 10)/15 = 8')}."],
        f"النسبة {m('zy/x = 12')} ثابتة في الحالتين.",
        diagram_en=svg_nafes_function_table(["x", "y", "z = kx/y"], [["6", "4", "18"], ["10", "15", "?"]], highlight_cell=(1, 2)),
    ))
    return qs


def _gen_num_07(start_idx: int) -> list[dict]:
    """G9-NUM-07: Combined work rates (1/a + 1/b = 1/t) & relative motion (d = vt)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Two pipes/workers together
    work_easy = [
        (4, 12, "3D printer A and 3D printer B", "الطابعة (أ) والطابعة (ب)"),
        (10, 15, "Pump A and Pump B at Yanbu", "المضخة (أ) والمضخة (ب) في ينبع"),
        (20, 30, "Harvester A and Harvester B in Al-Jouf", "الحصادة (أ) والحصادة (ب) في الجوف"),
    ]
    for a, b, n_en, n_ar in work_easy:
        qid = _qid(cur); cur += 1
        ans = (a * b) // (a + b)
        assert (a * b) % (a + b) == 0
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-07",
            f"Working alone, {n_en} finish a job in {m(str(a))} hours and {m(str(b))} hours, respectively. How many hours do they take working together?",
            f"ينجز {n_ar} عملاً منفردين في {m(str(a))} ساعات و{m(str(b))} ساعة على الترتيب. كم ساعة يستغرقان معاً لإنجاز العمل؟",
            ans, [(a + b) // 2, a + b, ans + 2],
            f"Add hourly rates {m(f'1/{a} + 1/{b} = 1/t')}.",
            f"اجمع معدلي الإنجاز في الساعة {m(f'1/{a} + 1/{b} = 1/t')}.",
            f"Combined time satisfies {m('t = ab / (a + b)')}.",
            [f"{m(rf'\frac{{1}}{{t}} = \frac{{1}}{{{a}}} + \frac{{1}}{{{b}}} = \frac{{{a+b}}}{{{a*b}}} = \frac{{1}}{{{ans}}} \implies t = {ans}')} hours."],
            f"{m(f'{ans}/{a} + {ans}/{b} = 1')} whole job.",
            f"نجمع المعدلين {m(f'1/{a} + 1/{b}')} ثم نقلب الكسر.",
            [f"{m(rf'\frac{{1}}{{t}} = \frac{{{b}+{a}}}{{{a*b}}} = \frac{{1}}{{{ans}}} \implies t = {ans}')} ساعات."],
            f"مجموع ما ينجزانه في {m(str(ans))} ساعات يساوي {m('1')}.",
            diagram_en=svg_pipe_tank(f"+1/{a} hr⁻¹", f"+1/{b} hr⁻¹"),
        ))

    # Easy 4-5: Opposite motion meeting time
    mot_easy = [
        ("Riyadh", "Dammam", 450, 80, 70),
        ("Jeddah", "Madinah", 420, 110, 100),
    ]
    for c1, c2, dist, v1, v2 in mot_easy:
        qid = _qid(cur); cur += 1
        ans = dist // (v1 + v2)
        assert dist % (v1 + v2) == 0
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-07",
            f"Two trains depart simultaneously from {c1} and {c2}, {m(str(dist))} km apart, moving toward each other at {m(str(v1))} km/h and {m(str(v2))} km/h. After how many hours do they meet?",
            f"انطلق قطاران في اللحظة نفسها من محطتين المسافة بينهما {m(str(dist))} كم باتجاهين متقابلين بسرعتي {m(str(v1))} كم/س و{m(str(v2))} كم/س. بعد كم ساعة يلتقيان؟",
            ans, [ans + 1, dist // max(1, abs(v1 - v2)), ans + 2],
            f"Add their speeds ({m(f'{v1} + {v2}')} km/h) to get the closing speed!",
            f"اجمع السرعتين ({m(f'{v1} + {v2}')} كم/س) للحصول على سرعة الاقتراب!",
            "Meeting time equals initial distance divided by sum of speeds.",
            [f"Closing speed is {m(f'{v1} + {v2} = {v1+v2}')} km/h, so {m(f't = {dist} \\div {v1+v2} = {ans}')} hours."],
            f"Distances covered: {m(f'{v1*ans} + {v2*ans} = {dist}')} km.",
            "سرعة الاقتراب تساوي مجموع السرعتين.",
            [f"سرعة الاقتراب {m(f'{v1+v2}')} كم/س، فالزمن {m(f'{dist} \\div {v1+v2} = {ans}')} ساعات."],
            f"مجموع المسافتين {m(f'{v1*ans} + {v2*ans} = {dist}')} كم.",
            diagram_en=svg_motion_timeline(c1, c2, f"{dist} km", f"{v1} km/h", f"{v2} km/h", meet=True),
        ))

    # Medium 6-8: Inlet minus drain pipe
    pipe_med = [(6, 12, "desalination basin"), (4, 12, "cooling tower"), (8, 24, "irrigation cistern")]
    for a, b, ctx_en in pipe_med:
        qid = _qid(cur); cur += 1
        ans = (a * b) // (b - a)
        assert (a * b) % (b - a) == 0
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-07",
            f"An inlet pipe fills an empty {ctx_en} in {m(str(a))} hours, while an open drain empties a full basin in {m(str(b))} hours. If both are open together, how many hours does it take to fill the basin?",
            f"يمتلئ حوض فارغ عبر أنبوب تغذية في {m(str(a))} ساعات، ويُفرّغ عبر أنبوب تصريف في {m(str(b))} ساعة. إذا فُتح الأنبوبان معاً، فكم ساعة يستغرق امتلاء الحوض؟",
            ans, [(a * b) // (a + b), b - a, ans + 4],
            f"Subtract the drain rate from the fill rate: {m(f'1/{a} - 1/{b} = 1/t')}.",
            f"اطرح معدل التفريغ من معدل الملء: {m(f'1/{a} - 1/{b} = 1/t')}.",
            "Net hourly fill fraction is 1/a − 1/b.",
            [f"Net rate: {m(rf'\frac{{1}}{{{a}}} - \frac{{1}}{{{b}}} = \frac{{{b-a}}}{{{a*b}}} = \frac{{1}}{{{ans}}}')}, so {m(f't = {ans}')} hours."],
            f"In {m(str(ans))} hours, inlet adds {m(f'{ans//a}')} tanks and drain removes {m(f'{ans/b:g}')}, leaving {m('1')} full tank.",
            "المعدل الصافي يساوي معدل الملء ناقص معدل التفريغ.",
            [f"{m(rf'\frac{{1}}{{{a}}} - \frac{{1}}{{{b}}} = \frac{{1}}{{{ans}}} \implies t = {ans}')} ساعة."],
            "الفرق في الحجم خلال الزمن يساوي سعة حوض كامل.",
            diagram_en=svg_pipe_tank(f"+1/{a} hr⁻¹", f"−1/{b} hr⁻¹"),
        ))

    # Medium 9-10: Same-direction chase
    chase_med = [(45, 75, 90), (60, 80, 100)]
    for gap, v1, v2 in chase_med:
        qid = _qid(cur); cur += 1
        ans = gap // (v2 - v1)
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-07",
            f"A patrol vehicle moving at {m(str(v2))} km/h pursues a freight truck {m(str(gap))} km ahead moving in the same direction at {m(str(v1))} km/h. In how many hours does it catch up?",
            f"تتحرك مركبة دورية بسرعة {m(str(v2))} كم/س خلف شاحنة تبعد عنها {m(str(gap))} كم وتتحرك في الاتجاه نفسه بسرعة {m(str(v1))} كم/س. بعد كم ساعة تلحق بها؟",
            ans, [gap // 5, ans + 1, ans + 2],
            f"In same-direction pursuit, relative speed is the difference {m(f'{v2} - {v1}')} km/h.",
            f"في الحركة بنفس الاتجاه، السرعة النسبية هي الفرق {m(f'{v2} - {v1}')} كم/س.",
            "Divide initial lead distance by speed difference.",
            [f"Relative catch-up speed is {m(f'{v2} - {v1} = {v2-v1}')} km/h, so {m(f't = {gap} \\div {v2-v1} = {ans}')} hours."],
            f"In {m(str(ans))} hours, {m(f'{v2*ans} - {v1*ans} = {gap}')} km.",
            "نقسم المسافة الفاصلة على فرق السرعتين.",
            [f"فرق السرعتين {m(f'{v2-v1}')} كم/س، فالزمن {m(f'{gap} \\div {v2-v1} = {ans}')} ساعات."],
            f"فرق المسافتين يساوي {m(str(gap))} كم.",
            diagram_en=svg_motion_timeline("Patrol", "Truck", f"Gap {gap} km", f"{v2} km/h", f"{v1} km/h", meet=False),
        ))

    # Hard 11-15: Unknown solo rate, 3-worker rate, harmonic round-trip speed, partial work
    hard_wm = [
        ("Technician A and Technician B together calibrate a lab in 6 hours. If A alone takes 10 hours, how many hours would B take working alone?",
         "يعاير الفنيان (أ) و(ب) مختبراً معاً في 6 ساعات. إذا كان (أ) وحده يستغرق 10 ساعات، فكم ساعة يستغرق (ب) وحده؟",
         15, [4, 12, 16], "1/b = 1/6 − 1/10 = 2/30 = 1/15 ⇒ b = 15", ["A + B: 6 h", "A alone: 10 h", "B alone: ? h"]),
        ("Three servers process a dataset alone in 6, 12, and 4 hours respectively. How many hours do all three take running in parallel?",
         "تعالج 3 خوادم قاعدة بيانات منفردة في 6 و12 و4 ساعات على الترتيب. كم ساعة تستغرق الخوادم الثلاثة معاً؟",
         2, [3, 4, 1], "1/6 + 1/12 + 1/4 = 6/12 = 1/2 ⇒ t = 2", ["6 h, 12 h, 4 h", "Parallel", "Total: ? h"]),
        ("A delivery van drives from Abha to Khamis Mushait at 60 km/h and returns along the exact same route at 90 km/h. What is its average speed (in km/h) for the entire round trip?",
         "قطعت حافلة المسافة ذهاباً بسرعة 60 كم/س وعادت على الطريق نفسه بسرعة 90 كم/س. ما السرعة المتوسطة للرحلة كاملةً (كم/س)؟",
         72, [75, 70, 78], "2 × 60 × 90 / (60 + 90) = 10800 / 150 = 72", ["Go: 60 km/h", "Back: 90 km/h", "Avg: ? km/h"]),
        ("A rover drives from Station P to Q at 40 km/h and returns along the same path at 60 km/h. What is its round-trip average speed in km/h?",
         "تحركت عربة استكشاف من المحطة P إلى Q بسرعة 40 كم/س وعادت على المسار نفسه بسرعة 60 كم/س. ما سرعتها المتوسطة ذهاباً وإياباً؟",
         48, [50, 45, 52], "2 × 40 × 60 / (40 + 60) = 4800 / 100 = 48", ["Go: 40 km/h", "Back: 60 km/h", "Avg: ? km/h"]),
        ("Pump A can fill a tank in 8 hours and Pump B in 12 hours. Pump A runs alone for 2 hours, then both run together. How many **more** hours are needed to finish filling the tank?",
         "تملأ المضخة (أ) خزاناً في 8 ساعات وتملؤه (ب) في 12 ساعة. عملت (أ) وحدها ساعتين ثم فُتحتا معاً. كم ساعة **إضافية** تلزم لإكمال ملء الخزان؟",
         Fraction(18, 5), [4, 3, Fraction(16, 5)], "Remaining 3/4 ÷ (1/8 + 1/12) = (3/4) ÷ (5/24) = 18/5", ["A: 2 h solo", "Then A + B", "Extra: ? h"]),
    ]
    for q_en, q_ar, ans, dists, step_s, diag_cells in hard_wm:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-07",
            q_en, q_ar, ans, dists,
            "Never average speeds directly on a round trip — divide total distance by total time, or subtract/add unit rates!",
            "لا تجمع السرعتين وتقسم على 2 في رحلة الذهاب والإياب، بل اقسم المسافة الكلية على الزمن الكلي!",
            "Apply total distance / total time or unit-rate conservation.",
            [f"Exact rate equation: {m(step_s)}."],
            "Verified by checking total work = 1 (or total round-trip distance = 2d).",
            "نطبّق معادلة المعدلات الكسرية أو المسافة الكلية على الزمن الكلي.",
            [f"الحساب الدقيق: {m(step_s)}."],
            "متحقق بالتعويض المباشر.",
            diagram_en=svg_number_strip(diag_cells),
        ))
    return qs


def _gen_num_08(start_idx: int) -> list[dict]:
    """G9-NUM-08: Ratio partitioning (a : b : c) & weighted mixture concentrations."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: 3-part ratio partitioning
    rat_easy = [
        (2, 3, 5, 240, "largest", "الأكبر", 2),
        (3, 4, 5, 180, "smallest", "الأصغر", 0),
        (1, 3, 4, 320, "middle", "الأوسط", 1),
        (2, 5, 7, 280, "largest", "الأكبر", 2),
        (3, 5, 7, 450, "smallest", "الأصغر", 0),
    ]
    for a, b, c, tot, which_en, which_ar, pick_i in rat_easy:
        qid = _qid(cur); cur += 1
        parts = (a, b, c)
        unit = tot // (a + b + c)
        ans = parts[pick_i] * unit
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Easy", "G9-NUM-08",
            f"A research grant of {m(str(tot))} thousand SAR is divided among three labs in the ratio {m(f'{a} : {b} : {c}')}. What is the **{which_en}** share (in thousand SAR)?",
            f"قُسّمت منحة بحثية قدرها {m(str(tot))} ألف ريال بين ثلاثة مختبرات بنسبة {m(f'{a} : {b} : {c}')}. كم يبلغ النصيب **{which_ar}** (بآلاف الريالات)؟",
            ans, [unit, (parts[(pick_i + 1) % 3]) * unit, (parts[(pick_i + 2) % 3]) * unit],
            f"Add the ratio parts ({m(f'{a}+{b}+{c} = {a+b+c}')}) to find the value of 1 part!",
            f"اجمع أجزاء النسبة ({m(f'{a}+{b}+{c} = {a+b+c}')}) لإيجاد قيمة الجزء الواحد!",
            "Divide total by sum of ratio parts, then multiply by the target part.",
            [f"Sum of parts = {m(str(a+b+c))}, so 1 part = {m(f'{tot} \\div {a+b+c} = {unit}')}.", f"Target share = {m(f'{parts[pick_i]} \\times {unit} = {ans}')}."],
            f"Shares sum to {m(f'{a*unit} + {b*unit} + {c*unit} = {tot}')}.",
            "نقسم المجموع الكلي على مجموع الأجزاء ثم نضرب في الجزء المطلوب.",
            [f"قيمة الجزء الواحد {m(f'{tot} \\div {a+b+c} = {unit}')}، والنصيب المطلوب {m(f'{parts[pick_i]} \\times {unit} = {ans}')}."],
            f"مجموع الأنصبة الثلاثة يساوي {m(str(tot))}.",
            diagram_en=svg_nafes_pie_chart([(f"Part {a}", a), (f"Part {b}", b), (f"Part {c}", c)], f"Total = {tot}"),
        ))

    # Medium 6-10: Weighted mixtures & ratio from difference
    mix_med = [
        (4, 15, 6, 35, "acid solution"),
        (3, 10, 7, 30, "saline solution"),
        (2, 50, 6, 18, "ethanol reagent"),
    ]
    for v1, c1, v2, c2, name_en in mix_med:
        qid = _qid(cur); cur += 1
        ans = (v1 * c1 + v2 * c2) // (v1 + v2)
        assert (v1 * c1 + v2 * c2) % (v1 + v2) == 0
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-08",
            f"A technician mixes {m(str(v1))} L of a {m(f'{c1}\\%')} {name_en} with {m(str(v2))} L of a {m(f'{c2}\\%')} {name_en}. What is the concentration percentage of the mixture?",
            f"خلط فني {m(str(v1))} لتر من محلول تركيزه {m(f'{c1}\\%')} مع {m(str(v2))} لتر من محلول مماثل تركيزه {m(f'{c2}\\%')}. ما نسبة تركيز المزيج الناتج؟",
            ans, [(c1 + c2) // 2, ans + 4, ans - 3],
            f"Compute total pure solute {m(f'({v1}\\times{c1} + {v2}\\times{c2})')} divided by total volume {m(str(v1+v2))} L.",
            f"احسب مجموع المادة النقية مقسوماً على الحجم الكلي {m(str(v1+v2))} لتر.",
            "Weighted concentration = total solute / total volume.",
            [f"{m(rf'c = \frac{{{v1}({c1}) + {v2}({c2})}}{{{v1} + {v2}}} = \frac{{{v1*c1 + v2*c2}}}{{{v1+v2}}} = {ans}\%')}"],
            f"Pure solute is {m(f'{(v1*c1 + v2*c2)/100:g}')} L out of {m(str(v1+v2))} L.",
            "نطبق قانون المتوسط المرجح للتراكيز.",
            [f"التركيز الجديد {m(rf'\frac{{{v1*c1 + v2*c2}}}{{{v1+v2}}} = {ans}\%')}"],
            "الناتج يقع بين التركيزين بنسبة عكسية للحجمين.",
            suffix=r"\%",
            diagram_en=svg_nafes_function_table(["Batch", "Liters", "Conc."], [["1", str(v1), f"{c1}%"], ["2", str(v2), f"{c2}%"], ["Mix", str(v1+v2), "?"]], highlight_cell=(2, 2)),
        ))

    diff_rat = [(3, 5, 9, 36), (2, 7, 11, 45)]
    for a, b, c, diff_ca in diff_rat:
        qid = _qid(cur); cur += 1
        unit = diff_ca // (c - a)
        tot = (a + b + c) * unit
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Medium", "G9-NUM-08",
            f"Three copper-zinc-tin alloy bars have masses in the ratio {m(f'{a} : {b} : {c}')}. If the heaviest bar is {m(str(diff_ca))} g heavier than the lightest bar, what is the **total** mass (in g) of all three bars?",
            f"ثلاث سبائك كتلتها بنسبة {m(f'{a} : {b} : {c}')}. إذا كانت السبيكة الأثقل تزيد عن الأخف بمقدار {m(str(diff_ca))} جم، فما الكتلة **الكلية** للسبائك الثلاث بالجرام؟",
            tot, [c * unit, b * unit, tot - 2 * unit],
            f"The difference of {m(str(diff_ca))} g corresponds to {m(f'{c} - {a} = {c-a}')} ratio parts!",
            f"الفرق {m(str(diff_ca))} جم يقابل فرق الأجزاء {m(f'{c} - {a} = {c-a}')}!",
            "Find 1 part from the difference, then multiply by (a + b + c).",
            [f"1 part = {m(f'{diff_ca} \\div ({c} - {a}) = {unit}')} g.", f"Total mass = {m(f'({a}+{b}+{c}) \\times {unit} = {tot}')} g."],
            f"Heaviest {m(str(c*unit))} g minus lightest {m(str(a*unit))} g = {m(str(diff_ca))} g.",
            "نقسم الفرق المعطى على فرق الأجزاء ثم نضرب في مجموع الأجزاء.",
            [f"قيمة الجزء {m(f'{diff_ca} \\div {c-a} = {unit}')} جم، والمجموع الكلي {m(f'{a+b+c} \\times {unit} = {tot}')} جم."],
            f"{m(f'{c*unit} - {a*unit} = {diff_ca}')} جم.",
            diagram_en=svg_bar_chart([("Bar A", a, f"{a}k"), ("Bar B", b, f"{b}k"), ("Bar C", c, f"{c}k")]),
        ))

    # Hard 11-15: Dilution with pure water, adding pure salt, chained ratios a:b & b:c
    hard_mix = [
        ("How many liters of **pure water** (0% salt) must be added to 12 L of a 25% salt solution to dilute it to a 15% salt solution?",
         "كم لتراً من **الماء النقي** (تركيز 0%) يجب إضافته إلى 12 لتراً من محلول ملحي تركيزه 25% ليصبح تركيزه 15%؟",
         8, [20, 6, 10], "Pure salt = 3 L; 3 / (12 + w) = 0.15 ⇒ 12 + w = 20 ⇒ w = 8", ["12 L @ 25%", "+ ? L water", "→ 15% salt"]),
        ("How many grams of **pure salt** (100%) must be dissolved into 180 g of a 10% salt solution to raise its concentration to 25%?",
         "كم جراماً من **الملح النقي** (100%) يجب إذابته في 180 جم من محلول ملحي تركيزه 10% ليرتفع التركيز إلى 25%؟",
         36, [27, 45, 30], "(18 + s) / (180 + s) = 1/4 ⇒ 72 + 4s = 180 + s ⇒ 3s = 108 ⇒ s = 36", ["180 g @ 10%", "+ ? g salt", "→ 25% salt"]),
        ("In a STEM competition, the ratio of Grade 7 to Grade 8 students is 2 : 3, and the ratio of Grade 8 to Grade 9 students is 4 : 5. If there are 105 students in total, how many are in Grade 9?",
         "في مسابقة علمية، نسبة طلاب الأول المتوسط إلى الثاني 2 : 3، ونسبة الثاني إلى الثالث المتوسط 4 : 5. إذا كان المجموع الكلي 105 طلاب، فكم طالباً في الصف الثالث المتوسط؟",
         45, [36, 24, 50], "Unify B: 8 : 12 : 15 (sum 35); 105 ÷ 35 = 3; Grade 9 = 15 × 3 = 45", ["G7:G8 = 2:3", "G8:G9 = 4:5", "G9 = ? / 105"]),
        ("Tank X and Tank Y hold fuel in the ratio 5 : 3. After transferring 18 L from X to Y, both tanks hold equal volumes. What is the combined volume (in L) of both tanks?",
         "خزانان النسبة بين ما فيهما من وقود 5 : 3. بعد نقل 18 لتراً من الأول إلى الثاني تساوت الكميتان. ما السعة الإجمالية للوقود في الخزانين باللتر؟",
         144, [72, 90, 120], "5k − 18 = 3k + 18 ⇒ 2k = 36 ⇒ k = 18; Total = 8k = 144", ["X : Y = 5 : 3", "Move 18 L → equal", "Total = ? L"]),
        ("Alloy A is 40% silver and Alloy B is 70% silver. How many grams of Alloy B must be melted with 60 g of Alloy A to produce a 58% silver alloy?",
         "سبيكة (أ) تحوي 40% فضة وسبيكة (ب) تحوي 70% فضة. كم جراماً من السبيكة (ب) يجب صهره مع 60 جم من (أ) لإنتاج سبيكة تركيزها 58%؟",
         90, [80, 75, 100], "0.40(60) + 0.70m = 0.58(60 + m) ⇒ 24 + 0.70m = 34.8 + 0.58m ⇒ 0.12m = 10.8 ⇒ m = 90", ["60 g @ 40%", "+ ? g @ 70%", "→ 58% Ag"]),
    ]
    for q_en, q_ar, ans, dists, step_s, diag_cells in hard_mix:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Numbers & Operations", "Hard", "G9-NUM-08",
            q_en, q_ar, ans, dists,
            "Track the invariant quantity (pure salt, pure water, total sum, or common middle term)!",
            "تتبّع المقدار الثابت (كمية الملح، الماء النقي، المجموع الكلي، أو الحد الأوسط المشترك)!",
            "Set up an invariant conservation equation and solve cleanly.",
            [f"Conservation equation: {m(step_s)}."],
            "Substituting back confirms exact target ratio/concentration.",
            "نكتب معادلة حفظ المادة النقية أو توحيد النسب ثم نحلها.",
            [f"المعادلة والحل: {m(step_s)}."],
            "التحقق بالتعويض يؤكد النسبة المطلوبة تماماً.",
            diagram_en=svg_number_strip(diag_cells),
        ))
    return qs


# ==============================================================================
# UNIT 3.3 (G9-ALG-01 .. G9-ALG-04): Linear Equations, Slope/Systems & Quadratics
# ==============================================================================

def _gen_alg_01(start_idx: int) -> list[dict]:
    """G9-ALG-01: Multi-step linear equations, absolute-value equations & linear inequalities."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Linear equations ax + b = cx + d
    lin_easy = [(5, -7, 2, 11), (7, 3, 4, 27), (9, -4, 4, 31)]
    for a, b, c, d in lin_easy:
        qid = _qid(cur); cur += 1
        ans = (d - b) // (a - c)
        assert a * ans + b == c * ans + d
        b_s = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        d_s = f"+ {d}" if d >= 0 else f"- {abs(d)}"
        eq_s = f"{a}x {b_s} = {c}x {d_s}"
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Easy", "G9-ALG-01",
            f"Solve the linear equation {m(eq_s)} for {m('x')}.",
            f"حل المعادلة الخطية {m(eq_s)} لإيجاد قيمة {m('x')}.",
            ans, [ans - 2, ans + 2, (d + b) // max(1, a - c)],
            f"Subtract {m(f'{c}x')} from both sides and move constants to the right.",
            f"اطرح {m(f'{c}x')} من الطرفين وانقل الثوابت إلى الطرف الآخر.",
            "Collect variable terms on one side and constants on the other.",
            [f"{m(f'({a} - {c})x = {d} - ({b}) \\implies {a-c}x = {d-b} \\implies x = {ans}')}."],
            f"LHS = {m(str(a*ans + b))}, RHS = {m(str(c*ans + d))}.",
            "نجمع حدود المتغير في طرف والثوابت في الطرف المقابل.",
            [f"{m(f'{a-c}x = {d-b} \\implies x = {ans}')}."],
            f"الطرف الأيمن والأيسر كلاهما يساوي {m(str(a*ans + b))}.",
            diagram_en=svg_function_machine(eq_s, f"{a-c}x = {d-b}", f"÷ {a-c}", "x = ?"),
        ))

    # Easy 4-5: Basic |x - a| = d and basic inequality
    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Algebra", "Easy", "G9-ALG-01",
        f"What is the **positive** solution of the absolute-value equation {m('|x - 4| = 9')}?",
        f"ما قيمة الحل **الموجب** لمعادلة القيمة المطلقة {m('|x - 4| = 9')}؟",
        13, [-5, 5, 9],
        "Set x − 4 = 9 and x − 4 = −9, then choose the positive solution.",
        "ضع x − 4 = 9 أو x − 4 = −9 ثم اختر الحل الموجب.",
        "Distance of x from 4 on the number line is 9.",
        [f"{m('x - 4 = 9 \\implies x = 13')}, or {m('x - 4 = -9 \\implies x = -5')}; the positive solution is {m('13')}."],
        f"{m('|13 - 4| = |9| = 9')}.",
        "نفك القيمة المطلقة إلى حالتين موجبة وسالبة.",
        [f"إما {m('x = 13')} وإما {m('x = -5')}، فالحل الموجب هو {m('13')}."],
        f"{m('|13 - 4| = 9')}.",
        diagram_en=svg_g9_real_number_line([-6, 0, 4, 14], 4, "center = 4", "|x − 4| = 9 → x > 0 ?"),
    ))

    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Algebra", "Easy", "G9-ALG-01",
        f"What is the greatest integer {m('x')} that satisfies the inequality {m('3x - 5 \\le 16')}?",
        f"ما أكبر عدد صحيح {m('x')} يحقق المتباينة {m('3x - 5 \\le 16')}؟",
        7, [6, 8, 5],
        "Add 5 to both sides, then divide by 3.",
        "أضف 5 للطرفين ثم اقسم على 3.",
        "Isolate x using inverse operations.",
        [f"{m('3x \\le 21 \\implies x \\le 7')}, so the greatest integer solution is {m('7')}."],
        f"{m('3(7) - 5 = 16 \\le 16')}, while {m('3(8) - 5 = 19 > 16')}.",
        "نعزل المتغير x بإضافة 5 ثم القسمة على 3.",
        [f"{m('3x \\le 21 \\implies x \\le 7')}، فأكبر عدد صحيح هو {m('7')}."],
        f"عند {m('x=7')} يكون الطرف الأيسر {m('16')}.",
        diagram_en=svg_g9_real_number_line([4, 5, 6, 8, 9], 6.5, "3x − 5 ≤ 16", "max integer x = ?", ray_dir=-1, closed_dot=True),
    ))

    # Medium 6-10: Distributive equations, |ax+b|=c sum/diff, negative inequality flip
    med_alg1 = [
        (f"Solve {m('4(x - 2) = 2(x + 5)')} for {m('x')}.", f"أوجد قيمة {m('x')} في المعادلة {m('4(x - 2) = 2(x + 5)')}.", 9, [7, 1, 6], "4x − 8 = 2x + 10 ⇒ 2x = 18 ⇒ x = 9", ["4(x − 2) = 2(x + 5)", "x = ?"]),
        (f"Solve {m('3(2x + 1) - 4 = 4x + 9')} for {m('x')}.", f"أوجد قيمة {m('x')} في المعادلة {m('3(2x + 1) - 4 = 4x + 9')}.", 5, [4, 6, 3], "6x − 1 = 4x + 9 ⇒ 2x = 10 ⇒ x = 5", ["3(2x + 1) − 4 = 4x + 9", "x = ?"]),
        (f"What is the **sum** of the two solutions of {m('|2x - 6| = 10')}?", f"ما **مجموع** حلي المعادلة {m('|2x - 6| = 10')}؟", 6, [8, -2, 10], "x = 8 and x = −2 ⇒ 8 + (−2) = 6", ["|2x − 6| = 10", "x₁ + x₂ = ?"]),
        (f"What is the positive **difference** between the two solutions of {m('|3x + 2| = 13')}?", f"ما **الفرق الموجب** بين حلي المعادلة {m('|3x + 2| = 13')}؟", Fraction(26, 3), [Fraction(22, 3), 8, Fraction(13, 3)], "x₁ = 11/3, x₂ = −5 ⇒ 11/3 − (−5) = 26/3", ["|3x + 2| = 13", "|x₁ − x₂| = ?"]),
        (f"What is the **greatest** integer {m('x')} satisfying {m('-4x + 9 \\ge 25')}?", f"ما **أكبر** عدد صحيح {m('x')} يحقق المتباينة {m('-4x + 9 \\ge 25')}؟", -4, [-3, 4, -5], "−4x ≥ 16 ⇒ x ≤ −4 (sign flips!)", ["−4x + 9 ≥ 25", "max int x = ?"]),
    ]
    for q_en, q_ar, ans, dists, step_s, diag_cells in med_alg1:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Medium", "G9-ALG-01",
            q_en, q_ar, ans, dists,
            "Distribute parentheses carefully, split absolute value into ±c, and flip ≤/≥ when dividing by a negative!",
            "فك الأقواس بدقة، واقسم القيمة المطلقة لحالتين، واعكس إشارة المتباينة عند القسمة على سالب!",
            "Solve systematically using linear/absolute-value/inequality properties.",
            [f"Algebraic reduction: {m(step_s)}."],
            "Direct substitution confirms every step.",
            "نبسّط المعادلة أو المتباينة خطوة بخطوة.",
            [f"خطوات الحل: {m(step_s)}."],
            "التعويض المباشر يؤكد صحة الحل.",
            diagram_en=svg_number_strip(diag_cells),
        ))

    # Hard 11-15: Compound inequality count, tariff comparison, parameter in equation
    hard_alg1 = [
        (f"How many **integers** {m('x')} satisfy the compound inequality {m('-7 < 2x - 3 \\le 9')}?",
         f"كم عدداً **صحيحاً** {m('x')} يحقق المتباينة المركبة {m('-7 < 2x - 3 \\le 9')}؟",
         8, [7, 9, 6], "−4 < 2x ≤ 12 ⇒ −2 < x ≤ 6 ⇒ x ∈ {−1,0,1,2,3,4,5,6} (8 integers)", ["−7 < 2x − 3 ≤ 9", "# integers = ?"]),
        (f"Cloud Plan A charges {m('45')} SAR/month plus {m('2')} SAR/GB; Plan B charges {m('15')} SAR/month plus {m('5')} SAR/GB. What is the **smallest integer** number of GB for which Plan A is **strictly cheaper** than Plan B?",
         f"الباقة السحابية (أ) تكلفتها {m('45')} ريالاً شهرياً بالإضافة إلى {m('2')} ريال لكل جيجابايت، والباقة (ب) {m('15')} ريالاً شهرياً بالإضافة إلى {m('5')} ريالات لكل جيجابايت. ما **أصغر عدد صحيح** من الجيجابايت يجعل الباقة (أ) **أرخص تماماً** من (ب)؟",
         11, [10, 9, 12], "45 + 2g < 15 + 5g ⇒ 30 < 3g ⇒ g > 10 ⇒ smallest integer is 11", ["A: 45 + 2g", "B: 15 + 5g", "min g (A < B) = ?"]),
        (f"For how many real values of {m('x')} does {m('3|x - 4| + 11 = 5')} hold?",
         f"كم عدداً حقيقياً {m('x')} يحقق المعادلة {m('3|x - 4| + 11 = 5')}؟",
         0, [1, 2, 4], "3|x − 4| = −6 ⇒ |x − 4| = −2 < 0 (no real solutions → 0)", ["3|x − 4| + 11 = 5", "# solutions = ?"]),
        (f"Three consecutive odd integers have a sum of {m('81')}. What is the **largest** of the three integers?",
         f"ثلاثة أعداد فردية متتالية مجموعها {m('81')}. ما **أكبر** هذه الأعداد الثلاثة؟",
         29, [27, 25, 31], "(n − 2) + n + (n + 2) = 81 ⇒ 3n = 81 ⇒ n = 27 ⇒ largest = 29", ["3 consec. odd", "Sum = 81", "Largest = ?"]),
        (f"If {m('x = 3')} is the solution of {m('5x - k = 2(x + k) - 3')}, what is the value of {m('k')}?",
         f"إذا كان {m('x = 3')} حلاً للمعادلة {m('5x - k = 2(x + k) - 3')}، فما قيمة الثابت {m('k')}؟",
         4, [3, 5, 6], "15 − k = 6 + 2k − 3 ⇒ 15 − k = 3 + 2k ⇒ 3k = 12 ⇒ k = 4", ["5x − k = 2(x + k) − 3", "x = 3", "k = ?"]),
    ]
    for q_en, q_ar, ans, dists, step_s, diag_cells in hard_alg1:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Hard", "G9-ALG-01",
            q_en, q_ar, ans, dists,
            "Pay close attention to strict (<) vs inclusive (≤) bounds and remember |u| ≥ 0 always!",
            "انتبه جيداً للفرق بين (<) و(≤)، وتذكّر أن القيمة المطلقة لا يمكن أن تساوي عدداً سالباً!",
            "Translate constraints into exact algebraic inequalities/equations.",
            [f"Exact derivation: {m(step_s)}."],
            "Boundary values verified directly.",
            "نصوغ المعادلة أو المتباينة الجبرية ونفحص القيم الحدية.",
            [f"الاستنتاج الجبري: {m(step_s)}."],
            "تم التحقق من القيم الحدية.",
            diagram_en=svg_number_strip(diag_cells),
        ))
    return qs


def _gen_alg_02(start_idx: int) -> list[dict]:
    """G9-ALG-02: Slope, parallel/perpendicular slopes, y = mx + b & 2x2 linear systems."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Slope between two points
    slope_pts = [((-2, 1), (2, 9)), ((-3, 5), (3, -1)), ((1, -2), (5, 4))]
    for (x1, y1), (x2, y2) in slope_pts:
        qid = _qid(cur); cur += 1
        ans = Fraction(y2 - y1, x2 - x1)
        m_flt = float(ans)
        b_flt = y1 - m_flt * x1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Easy", "G9-ALG-02",
            f"What is the slope of the line passing through {m(f'A({x1}, {y1})')} and {m(f'B({x2}, {y2})')}?",
            f"ما ميل المستقيم المار بالنقطتين {m(f'A({x1}, {y1})')} و{m(f'B({x2}, {y2})')}؟",
            ans, [Fraction(x2 - x1, y2 - y1), -ans, Fraction(y2 + y1, x2 - x1)],
            f"Use {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')} (change in y over change in x).",
            f"استخدم قانون الميل {m(r'm = \frac{y_2 - y_1}{x_2 - x_1}')}.",
            "Divide vertical rise by horizontal run.",
            [f"{m(rf'm = \frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \frac{{{y2 - y1}}}{{{x2 - x1}}}')}, which simplifies to {m(str(ans))}."],
            "Sign of slope matches the upward/downward tilt of the plotted line.",
            "نقسم التغير الصادي على التغير السيني.",
            [f"{m(rf'm = \frac{{{y2 - y1}}}{{{x2 - x1}}}')}."],
            "إشارة الميل تطابق اتجاه المستقيم على الرسم.",
            diagram_en=svg_nafes_coordinate_line([(x1, y1, f"A({x1},{y1})"), (x2, y2, f"B({x2},{y2})")], line_kb=(m_flt, b_flt), max_coord=10),
        ))

    # Easy 4-5: Parallel & perpendicular slopes
    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Algebra", "Easy", "G9-ALG-02",
        f"What is the slope of any line **perpendicular** to {m(r'y = \frac{3}{4}x - 5')}?",
        f"ما ميل أي مستقيم **عمودي** على المستقيم {m(r'y = \frac{3}{4}x - 5')}؟",
        Fraction(-4, 3), [Fraction(3, 4), Fraction(4, 3), Fraction(-3, 4)],
        "Perpendicular slopes are negative reciprocals (m₁ · m₂ = −1).",
        "المستقيمان المتعامدان ميل أحدهما مقلوب معكوس الآخر (حاصل ضربهما −1).",
        "Flip the fraction and negate its sign.",
        [f"The given slope is {m('m_1 = 3/4')}, so the perpendicular slope is {m('m_2 = -4/3')}."],
        f"{m('(3/4)(-4/3) = -1')}.",
        "نقلب الكسر ونعكس إشارته.",
        [f"ميل المستقيم المعطى {m('3/4')}، فميل العمودي عليه {m('-4/3')}."],
        f"حاصل ضرب الميلين {m('-1')}.",
        diagram_en=svg_nafes_coordinate_line([(0, -1, "")], line_kb=(0.75, -1), line2_kb=(-4 / 3, 1), max_coord=5),
    ))

    qid = _qid(cur); cur += 1
    qs.append(make_nafes_q(
        qid, LEVEL, "Algebra", "Easy", "G9-ALG-02",
        f"Line {m(r'\ell')} is **parallel** to {m('6x + 2y = 10')}. What is the slope of line {m(r'\ell')}?",
        f"المستقيم {m(r'\ell')} **يوازي** المستقيم {m('6x + 2y = 10')}. ما ميل المستقيم {m(r'\ell')}؟",
        -3, [3, 6, Fraction(1, 3)],
        "Solve 6x + 2y = 10 for y first to put it into y = mx + b form!",
        "ضع المعادلة في صورة الميل والمقطع y = mx + b أولاً!",
        "Isolate y to read slope m; parallel lines share the same slope.",
        [f"{m('2y = -6x + 10 \\implies y = -3x + 5')}, so parallel lines also have slope {m('-3')}."],
        "Testing (0, 5) and (1, 2) gives slope (2−5)/(1−0) = −3.",
        "نعزل المتغير y فنجد معامل x هو الميل.",
        [f"{m('y = -3x + 5')}، وبما أن المستقيمين متوازيان فميله {m('-3')}."],
        "الموازي له الميل نفسه.",
        diagram_en=svg_nafes_coordinate_line([(0, 5, ""), (1, 2, "")], line_kb=(-3, 5), line2_kb=(-3, 1), max_coord=6),
    ))

    # Medium 6-10: y-intercept b & 2x2 linear systems
    med_alg2 = [
        (f"A line with slope {m('m = -2')} passes through {m('(3, 4)')}. What is its {m('y')}-intercept {m('b')} in {m('y = mx + b')}?",
         f"مستقيم ميله {m('m = -2')} ويمر بالنقطة {m('(3, 4)')}. ما قيمة مقطعه الصادي {m('b')} في المعادلة {m('y = mx + b')}؟",
         10, [-2, 6, -10], "4 = −2(3) + b ⇒ b = 10", [(3, 4, "(3,4)")], (-2, 10)),
        (f"Solve the system {m('x + y = 9')} and {m('2x - y = 6')}. What is the value of {m('x')}?",
         f"في نظام المعادلتين {m('x + y = 9')} و{m('2x - y = 6')}، ما قيمة {m('x')}؟",
         5, [4, 3, 6], "Add equations: 3x = 15 ⇒ x = 5", [(5, 4, "(x, y)")], (-1, 9)),
        (f"Solve the system {m('3x + 2y = 19')} and {m('x - 2y = 1')}. What is {m('x + y')}?",
         f"إذا كان {m('(x, y)')} حل النظام {m('3x + 2y = 19')} و{m('x - 2y = 1')}، فما قيمة {m('x + y')}؟",
         7, [5, 2, 9], "4x = 20 ⇒ x = 5, y = 2 ⇒ x + y = 7", [(5, 2, "(x, y)")], (-1.5, 9.5)),
        (f"Solve the system {m('y = 3x - 2')} and {m('2x + y = 13')}. What is the value of {m('y')}?",
         f"في النظام {m('y = 3x - 2')} و{m('2x + y = 13')}، ما قيمة الإحداثي {m('y')}؟",
         7, [3, 5, 9], "2x + (3x − 2) = 13 ⇒ 5x = 15 ⇒ x = 3 ⇒ y = 7", [(3, 7, "(x, y)")], (3, -2)),
        (f"What is the {m('x')}-intercept of the line {m('3x - 4y = 24')}?",
         f"ما المقطع السيني للمستقيم الذي معادلته {m('3x - 4y = 24')}؟",
         8, [-6, 6, -8], "Set y = 0: 3x = 24 ⇒ x = 8", [(8, 0, "(?, 0)"), (0, -6, "(0,-6)")], (0.75, -6)),
    ]
    for q_en, q_ar, ans, dists, step_s, pts, kb in med_alg2:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Medium", "G9-ALG-02",
            q_en, q_ar, ans, dists,
            "Use substitution, elimination, or set y = 0 / x = 0 for intercepts.",
            "استخدم الحذف أو التعويض، أو ضع y = 0 لإيجاد المقطع السيني.",
            "Apply slope-intercept and linear elimination directly.",
            [f"{m(step_s)}."],
            "Point satisfies both equations.",
            "نطبق طريقة الحذف أو التعويض المباشر.",
            [f"{m(step_s)}."],
            "النقطة تحقق المعادلتين معاً.",
            diagram_en=svg_nafes_coordinate_line(pts, line_kb=kb, max_coord=10),
        ))

    # Hard 11-15: Unknown parameter for slope/parallel system & word-problem systems
    hard_alg2 = [
        (f"For what value of {m('k')} does the line through {m('(-1, k)')} and {m('(3, 10)')} have slope {m('2')}?",
         f"ما قيمة {m('k')} التي تجعل ميل المستقيم المار بالنقطتين {m('(-1, k)')} و{m('(3, 10)')} يساوي {m('2')}؟",
         2, [4, 18, -2], "(10 − k) / (3 − (−1)) = 2 ⇒ 10 − k = 8 ⇒ k = 2"),
        (f"For what value of {m('a')} does the linear system {m('ax + 3y = 12')} and {m('4x + 6y = 9')} have **no solution** (parallel distinct lines)?",
         f"ما قيمة الثابت {m('a')} التي تجعل نظام المعادلتين {m('ax + 3y = 12')} و{m('4x + 6y = 9')} **عديم الحل** (مستقيمين متوازيين)؟",
         2, [4, -2, 8], "Slopes equal: −a/3 = −4/6 ⇒ a = 2 (while 12/3 ≠ 9/6)"),
        (f"At Qiddiya Science Expo, {m('3')} adult tickets and {m('2')} student tickets cost {m('130')} SAR, while {m('1')} adult ticket and {m('2')} student tickets cost {m('70')} SAR. What is the price of {m('1')} student ticket in SAR?",
         f"في معرض علمي بالقدية، ثمن {m('3')} تذاكر كبار و{m('2')} تذكرة طلاب هو {m('130')} ريالاً، وثمن تذكرة كبير واحدة و{m('2')} تذكرة طلاب هو {m('70')} ريالاً. كم ريالاً ثمن تذكرة الطالب الواحدة؟",
         20, [30, 25, 15], "Subtract: 2A = 60 ⇒ A = 30; 30 + 2S = 70 ⇒ S = 20"),
        (f"Faisal has {m('18')} banknotes consisting only of {m('10')}-SAR and {m('50')}-SAR bills worth {m('460')} SAR in total. How many {m('50')}-SAR bills does he have?",
         f"لدى فيصل {m('18')} ورقة نقدية من فئتي {m('10')} ريالات و{m('50')} ريالاً مجموع قيمتها {m('460')} ريالاً. كم ورقة لديه من فئة {m('50')} ريالاً؟",
         7, [11, 8, 6], "x + y = 18, 10x + 50y = 460 ⇒ 40y = 280 ⇒ y = 7"),
        (f"Line {m('L')} passes through {m('(4, 5)')} and is perpendicular to {m('y = -2x + 1')}. What is the {m('y')}-intercept of line {m('L')}?",
         f"يمر المستقيم {m('L')} بالنقطة {m('(4, 5)')} ويعامد المستقيم {m('y = -2x + 1')}. ما المقطع الصادي للمستقيم {m('L')}؟",
         3, [7, 13, -3], "m_L = +1/2; 5 = (1/2)(4) + b ⇒ 5 = 2 + b ⇒ b = 3"),
    ]
    for q_en, q_ar, ans, dists, step_s in hard_alg2:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Hard", "G9-ALG-02",
            q_en, q_ar, ans, dists,
            "Translate parallel/perpendicular conditions into slope equations, or eliminate one variable cleanly!",
            "ترجم شرط التوازي أو التعامد إلى علاقة ميل، أو احذف أحد المتغيرين بطرح المعادلتين!",
            "Formulate linear equations and solve by elimination/slope properties.",
            [f"{m(step_s)}."],
            "Verified against all given conditions.",
            "نكوّن المعادلة الخطية ونحلها بالحذف أو قانون الميل.",
            [f"{m(step_s)}."],
            "متحقق من جميع الشروط.",
            diagram_en=svg_nafes_coordinate_line([(0, 3, ""), (4, 5, "")], line_kb=(0.5, 3), line2_kb=(-2, 1), max_coord=6),
        ))
    return qs


def _gen_alg_03(start_idx: int) -> list[dict]:
    """G9-ALG-03: Polynomial addition/multiplication & special-product identities."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Polynomial add/subtract & direct special products
    poly_easy = [
        (f"Simplify {m('(4x^2 + 5x - 3) - (x^2 - 2x + 4)')}.",
         f"بسّط طرح كثيرتي الحدود {m('(4x^2 + 5x - 3) - (x^2 - 2x + 4)')}.",
         r"3x^2 + 7x - 7", [r"3x^2 + 3x + 1", r"3x^2 + 3x - 7", r"5x^2 + 7x - 7"], "(4−1)x² + (5−(−2))x + (−3−4)", "x", "2"),
        (f"Expand the special product {m('(x + 6)^2')}.",
         f"فك المربع الكامل {m('(x + 6)^2')}.",
         r"x^2 + 12x + 36", [r"x^2 + 36", r"x^2 + 6x + 36", r"x^2 + 12x + 12"], "a² + 2ab + b²", "x", "6"),
        (f"Expand the difference-of-squares product {m('(3x - 5)(3x + 5)')}.",
         f"أوجد ناتج الضرب {m('(3x - 5)(3x + 5)')}.",
         r"9x^2 - 25", [r"9x^2 + 25", r"3x^2 - 25", r"9x^2 - 30x + 25"], "(3x)² − 5²", "3x", "5"),
        (f"Multiply {m('2x(3x^2 - 4x + 5)')}.",
         f"أوجد ناتج ضرب وحيدة الحد في كثيرة الحدود: {m('2x(3x^2 - 4x + 5)')}.",
         r"6x^3 - 8x^2 + 10x", [r"6x^2 - 8x + 10", r"5x^3 - 8x^2 + 10x", r"6x^3 + 8x^2 + 10x"], "Distribute 2x", "2x", "3x"),
        (f"Expand {m('(x - 7)^2')}.",
         f"أوجد مفكوك {m('(x - 7)^2')}.",
         r"x^2 - 14x + 49", [r"x^2 - 49", r"x^2 + 14x + 49", r"x^2 - 7x + 49"], "x² − 2(7)x + 49", "x", "7"),
    ]
    for q_en, q_ar, ans, dists, note, la, lb in poly_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Easy", "G9-ALG-03",
            q_en, q_ar, ans, dists,
            "Distribute negative signs across all terms, and include ±2ab when squaring binomials!",
            "وزّع الإشارة السالبة على جميع حدود القوس الثاني، ولا تنسَ الحد الأوسط ±2ab!",
            "Combine like powers of x or apply special-product identities.",
            [f"Applying {m(note)} gives {m(ans)}."],
            "Checked numerically by substituting x = 2.",
            "نجمع الحدود المتشابهة أو نطبّق المتطابقة الشهيرة.",
            [f"بتطبيق {m(note)} نحصل على {m(ans)}."],
            "متحقق بالتعويض العددي عند x = 2.",
            diagram_en=svg_area_identity_square(la, lb),
        ))

    # Medium 6-10: Binomial products, numerical special identities, missing coefficient
    poly_med = [
        (f"A rectangular solar panel has length {m('(2x + 5)')} cm and width {m('(x + 3)')} cm. Which polynomial represents its area?",
         f"لوح شمسي مستطيل طوله {m('(2x + 5)')} سم وعرضه {m('(x + 3)')} سم. أي كثيرة حدود تمثل مساحته؟",
         r"2x^2 + 11x + 15", [r"2x^2 + 8x + 15", r"2x^2 + 15", r"3x^2 + 11x + 15"], "2x² + 6x + 5x + 15"),
        (f"Using the difference-of-squares identity, what is the exact value of {m('54^2 - 46^2')}?",
         f"باستخدام متطابقة الفرق بين مربعين، ما القيمة الدقيقة للمقدار {m('54^2 - 46^2')}؟",
         800, [64, 1000, 80], "(54 − 46)(54 + 46) = 8 × 100 = 800"),
        (f"Using {m('(100 + 3)(100 - 3)')}, what is the exact product {m('103 \\times 97')}?",
         f"باستخدام متطابقة الفرق بين مربعين {m('(100 + 3)(100 - 3)')}، ما ناتج {m('103 \\times 97')}؟",
         9991, [9997, 9981, 10009], "100² − 3² = 10000 − 9 = 9991"),
        (f"If {m('(3x - 4)^2 = 9x^2 + kx + 16')} for all {m('x')}, what is the integer {m('k')}?",
         f"إذا كان {m('(3x - 4)^2 = 9x^2 + kx + 16')} لجميع قيم {m('x')}، فما قيمة العدد الصحيح {m('k')}؟",
         -24, [24, -12, 12], "k = −2(3)(4) = −24"),
        (f"Simplify {m('(x + 4)^2 - (x - 4)^2')}.",
         f"بسّط العبارة الجبرية {m('(x + 4)^2 - (x - 4)^2')}.",
         r"16x", [r"8x", r"2x^2 + 32", r"32"], "(x² + 8x + 16) − (x² − 8x + 16) = 16x"),
    ]
    for q_en, q_ar, ans, dists, note in poly_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Medium", "G9-ALG-03",
            q_en, q_ar, ans, dists,
            "Use FOIL / special products (a−b)(a+b) = a² − b² and (a+b)² − (a−b)² = 4ab!",
            "استخدم ضرب ثنائيات الحد ومتطابقة الفرق بين مربعين!",
            "Expand or factor via Grade 9 polynomial identities.",
            [f"Identity step: {m(note)}."],
            "Verified by direct substitution.",
            "نطبّق المتطابقة التربيعية المناسبة.",
            [f"خطوة التبسيط: {m(note)}."],
            "متحقق بالتعويض المباشر.",
            diagram_en=svg_area_identity_square("a", "b"),
        ))

    # Hard 11-15: Symmetric algebraic identities
    poly_hard = [
        (f"If {m('a + b = 9')} and {m('ab = 16')}, what is the value of {m('a^2 + b^2')}?",
         f"إذا كان {m('a + b = 9')} و{m('ab = 16')}، فما قيمة {m('a^2 + b^2')}؟",
         49, [81, 65, 113], "(a + b)² − 2ab = 81 − 32 = 49"),
        (f"If {m('x - y = 5')} and {m('xy = 14')}, what is the value of {m('x^2 + y^2')}?",
         f"إذا كان {m('x - y = 5')} و{m('xy = 14')}، فما قيمة {m('x^2 + y^2')}؟",
         53, [25, 39, 11], "(x − y)² + 2xy = 25 + 28 = 53"),
        (f"If {m('x^2 - y^2 = 72')} and {m('x + y = 12')}, what is the value of {m('x - y')}?",
         f"إذا كان {m('x^2 - y^2 = 72')} و{m('x + y = 12')}، فما قيمة {m('x - y')}؟",
         6, [8, 12, 60], "(x − y)(x + y) = 72 ⇒ 12(x − y) = 72 ⇒ x − y = 6"),
        (f"For a nonzero real number {m('x')}, if {m(r'x + \frac{1}{x} = 5')}, what is the value of {m(r'x^2 + \frac{1}{x^2}')}?",
         f"لأي عدد حقيقي غير صفري {m('x')}، إذا كان {m(r'x + \frac{1}{x} = 5')}، فما قيمة {m(r'x^2 + \frac{1}{x^2}')}؟",
         23, [25, 27, 21], "(x + 1/x)² = x² + 2 + 1/x² = 25 ⇒ 23"),
        (f"If {m('(2x + m)(x - 3) = 2x^2 + nx - 15')} holds for all {m('x')}, what is {m('m + n')}?",
         f"إذا كانت المتطابقة {m('(2x + m)(x - 3) = 2x^2 + nx - 15')} صحيحة لجميع قيم {m('x')}، فما قيمة {m('m + n')}؟",
         4, [6, -1, 5], "−3m = −15 ⇒ m = 5; n = m − 6 = −1 ⇒ m + n = 4"),
    ]
    for q_en, q_ar, ans, dists, note in poly_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Hard", "G9-ALG-03",
            q_en, q_ar, ans, dists,
            "Square the known sum/difference without solving for individual variables!",
            "ربّع المجموع أو الفرق المعطى مباشرة دون الحاجة لإيجاد كل متغير على حدة!",
            "Use (a ± b)² = a² ± 2ab + b² and a² − b² = (a − b)(a + b).",
            [f"Identity manipulation: {m(note)}."],
            "Algebraic identity holds identically.",
            "نستعمل المتطابقات التربيعية لإيجاد المقدار المطلوب مباشرة.",
            [f"التبسيط: {m(note)}."],
            "متحقق جبرياً.",
            diagram_en=svg_area_identity_square("x", "1/x" if "1/x" in note else "y"),
        ))
    return qs


def _gen_alg_04(start_idx: int) -> list[dict]:
    """G9-ALG-04: Factoring trinomials x^2 + bx + c = 0, roots & parabola vertex."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Factoring x^2 + bx + c = 0 & axis of symmetry
    quad_easy = [
        (f"What is the **larger** root of {m('x^2 - 7x + 12 = 0')}?",
         f"ما قيمة الجذر **الأكبر** للمعادلة التربيعية {m('x^2 - 7x + 12 = 0')}؟",
         4, [3, -4, 7], "(x − 3)(x − 4) = 0 ⇒ roots 3, 4", "r₁", "r₂ = ?", "(3.5, −0.25)"),
        (f"What is the **positive** root of {m('x^2 + 2x - 15 = 0')}?",
         f"ما الجذر **الموجب** للمعادلة {m('x^2 + 2x - 15 = 0')}؟",
         3, [5, -5, -3], "(x + 5)(x − 3) = 0 ⇒ roots −5, 3", "r₁ < 0", "r₂ > 0 ?", "(−1, −16)"),
        (f"What is the equation's axis-of-symmetry {m('x')}-value for the parabola {m('y = x^2 - 8x + 9')}?",
         f"ما قيمة {m('x')} لمعادلة محور التماثل للقطع المكافئ {m('y = x^2 - 8x + 9')}؟",
         4, [-4, 8, -8], "x = −(−8) / (2·1) = 4", "r₁", "r₂", "(x = ?, −7)"),
        (f"What is the **sum** of the two solutions of {m('(x - 6)(x + 2) = 0')}?",
         f"ما **مجموع** حلي المعادلة {m('(x - 6)(x + 2) = 0')}؟",
         4, [-4, 8, -12], "Roots are 6 and −2; 6 + (−2) = 4", "−2", "6", "(2, −16)"),
        (f"Factor {m('x^2 - 9x + 20')} completely.",
         f"حلّل ثلاثية الحدود {m('x^2 - 9x + 20')} تحليلاً تاماً.",
         r"(x - 4)(x - 5)", [r"(x + 4)(x + 5)", r"(x - 2)(x - 10)", r"(x - 4)(x + 5)"], "−4 + (−5) = −9, (−4)(−5) = 20", "4", "5", "(4.5, −0.25)"),
    ]
    for q_en, q_ar, ans, dists, note, r1, r2, v_lbl in quad_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Easy", "G9-ALG-04",
            q_en, q_ar, ans, dists,
            "Find two integers whose sum is b and product is c, or use x = −b / (2a).",
            "ابحث عن عددين مجموعهما b وحاصل ضربهما c، أو استخدم x = −b / (2a).",
            "Factor the quadratic or apply the axis-of-symmetry formula.",
            [f"{m(note)}."],
            "Substituting back confirms zero residual.",
            "نحلّل العبارة التربيعية إلى عاملين خطيين أو نطبّق قانون محور التماثل.",
            [f"{m(note)}."],
            "بالتعويض المباشر تتحقق المعادلة.",
            diagram_en=svg_parabola_roots(r1, r2, v_lbl),
        ))

    # Medium 6-10: Projectile max height, vertex min, rectangle dimensions from area
    quad_med = [
        (f"A flare launched at Qiddiya follows height {m('h(t) = -5t^2 + 20t + 4')} meters after {m('t')} seconds. What is the **maximum height** (in m) reached by the flare?",
         f"تُعطى ارتفاع إشارة ضوئية بعد {m('t')} ثانية بالدالة {m('h(t) = -5t^2 + 20t + 4')} متراً. ما **أقصى ارتفاع** تصل إليه الإشارة بالمتر؟",
         24, [20, 2, 28], "t_v = −20/(−10) = 2 s; h(2) = −20 + 40 + 4 = 24 m"),
        (f"A rectangular lab table has length {m('3')} m more than its width and area {m('40\\text{ m}^2')}. What is its **length** in meters?",
         f"طاولة مختبر مستطيلة يزيد طولها على عرضها بمقدار {m('3')} أمتار ومساحتها {m('40')} م². ما **طول** الطاولة بالأمتار؟",
         8, [5, 10, 7], "w(w + 3) = 40 ⇒ w = 5 ⇒ length = 8 m"),
        (f"What is the minimum value of {m('y = 2x^2 - 12x + 23')}?",
         f"ما القيمة الصغرى للدالة التربيعية {m('y = 2x^2 - 12x + 23')}؟",
         5, [3, 11, -5], "x_v = 12 / 4 = 3; y(3) = 18 − 36 + 23 = 5"),
        (f"What is the positive difference {m('|r_1 - r_2|')} between the two roots of {m('x^2 - 4x - 21 = 0')}?",
         f"ما الفرق الموجب {m('|r_1 - r_2|')} بين جذري المعادلة {m('x^2 - 4x - 21 = 0')}؟",
         10, [4, 7, 11], "(x − 7)(x + 3) = 0 ⇒ roots 7 and −3 ⇒ |7 − (−3)| = 10"),
        (f"Solve {m('2x^2 - 7x + 3 = 0')} and find the **larger** root.",
         f"أوجد الجذر **الأكبر** للمعادلة التربيعية {m('2x^2 - 7x + 3 = 0')}.",
         3, [Fraction(1, 2), -3, 2], "(2x − 1)(x − 3) = 0 ⇒ roots 1/2 and 3 ⇒ larger is 3"),
    ]
    for q_en, q_ar, ans, dists, note in quad_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Medium", "G9-ALG-04",
            q_en, q_ar, ans, dists,
            "Evaluate the vertex at x = −b/(2a), or factor and reject negative geometric lengths!",
            "احسب الرأس عند x = −b/(2a)، أو حلّل واستبعد الأطوال السالبة!",
            "Use quadratic factoring or vertex optimization.",
            [f"{m(note)}."],
            "Verified by plugging back into the original quadratic.",
            "نستخدم التحليل أو إحداثيي رأس القطع المكافئ.",
            [f"{m(note)}."],
            "متحقق بالتعويض في المعادلة الأصلية.",
            diagram_en=svg_parabola_roots("r₁", "r₂", "Vertex"),
        ))

    # Hard 11-15: Single repeated root (discriminant = 0), Vieta root-parameter, perimeter optimization
    quad_hard = [
        (f"For what positive constant {m('c')} does {m('x^2 - 14x + c = 0')} have **exactly one** (repeated) real solution?",
         f"ما قيمة الثابت الموجب {m('c')} التي تجعل للمعادلة {m('x^2 - 14x + c = 0')} **حلاً حقيقياً وحيداً** (مكرراً)؟",
         49, [14, 28, 196], "c = (−14 / 2)² = (−7)² = 49 (discriminant b² − 4ac = 0)"),
        (f"If {m('x = 6')} is one root of {m('x^2 + kx - 18 = 0')}, what is the **other** root?",
         f"إذا كان {m('x = 6')} أحد جذري المعادلة {m('x^2 + kx - 18 = 0')}، فما قيمة الجذر **الآخر**؟",
         -3, [3, -6, 2], "Product of roots = −18 ⇒ 6 · r₂ = −18 ⇒ r₂ = −3"),
        (f"A farmer encloses a rectangular garden using {m('36')} m of fencing for all four sides. What is the **maximum possible area** (in {m(r'\text{m}^2')}) of the garden?",
         f"يحيط مزارع حديقة مستطيلة بسياج طوله الكلي {m('36')} متراً للأضلاع الأربعة. ما **أكبر مساحة ممكنة** للحديقة بالمتر المربع؟",
         81, [72, 80, 90], "L + W = 18 ⇒ A(W) = W(18 − W) = −W² + 18W; max at W = 9 ⇒ A = 81"),
        (f"How many real solutions does the quadratic equation {m('3x^2 - 4x + 5 = 0')} have?",
         f"كم حلاً حقيقياً للمعادلة التربيعية {m('3x^2 - 4x + 5 = 0')}؟",
         0, [1, 2, 3], "Discriminant Δ = (−4)² − 4(3)(5) = 16 − 60 = −44 < 0 ⇒ 0 real solutions"),
        (f"The parabola {m('y = ax^2 + bx + 8')} crosses the {m('x')}-axis at {m('x = 2')} and {m('x = 4')}. What is {m('a + b')}?",
         f"يقطع القطع المكافئ {m('y = ax^2 + bx + 8')} محور السينات عند {m('x = 2')} و{m('x = 4')}. ما قيمة {m('a + b')}؟",
         -5, [-6, 5, -7], "a(x − 2)(x − 4) = a(x² − 6x + 8); since 8a = 8 ⇒ a = 1, b = −6 ⇒ a + b = −5"),
    ]
    for q_en, q_ar, ans, dists, note in quad_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Algebra", "Hard", "G9-ALG-04",
            q_en, q_ar, ans, dists,
            "Use the discriminant b² − 4ac, root-product c/a, or factored form a(x − r₁)(x − r₂)!",
            "استخدم المميز b² − 4ac، أو حاصل ضرب الجذرين c/a، أو الصورة المحللة!",
            "Apply quadratic structure (discriminant, root relations, or vertex symmetry).",
            [f"{m(note)}."],
            "Verified algebraically.",
            "نوظّف خصائص المعادلة التربيعية والمميز.",
            [f"{m(note)}."],
            "متحقق جبرياً.",
            diagram_en=svg_parabola_roots("2", "4", "Vertex"),
        ))
    return qs


# ==============================================================================
# UNIT 3.4 (G9-GEO-01 .. G9-GEO-04): Pythagoras, Coordinates, Areas & 3D Volumes
# ==============================================================================

def _gen_geo_01(start_idx: int) -> list[dict]:
    """G9-GEO-01: Pythagorean theorem in right triangles, ladders, rectangles & diagonals."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Find hypotenuse c
    for a, b, ctx_en, ctx_ar in [(6, 8, "solar support frame", "إطار دعامة شمسية"), (9, 12, "metro ramp", "منحدر محطة مترو"), (8, 15, "robotics gantry", "جسر روبوتي")]:
        qid = _qid(cur); cur += 1
        c = math.isqrt(a * a + b * b)
        assert a * a + b * b == c * c
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-01",
            f"A right-triangular {ctx_en} has perpendicular legs of {m(str(a))} m and {m(str(b))} m. What is the length of its hypotenuse in meters?",
            f"{ctx_ar} على شكل مثلث قائم الزاوية طولا ساقيه {m(str(a))} م و{m(str(b))} م. ما طول وتره بالأمتار؟",
            c, [a + b, c - 2, c + 2],
            f"Apply {m('c = \\sqrt{a^2 + b^2}')}.",
            f"طبّق قانون فيثاغورس {m('c = \\sqrt{a^2 + b^2}')}.",
            "Sum the squares of the two legs and take the square root.",
            [f"{m(f'c = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a*a} + {b*b}}} = \\sqrt{{{c*c}}} = {c}')} m."],
            f"{m(f'{a}^2 + {b}^2 = {c*c} = {c}^2')}.",
            "نجمع مربعي الساقين ثم نأخذ الجذر التربيعي.",
            [f"{m(f'c = \\sqrt{{{a*a} + {b*b}}} = {c}')} م."],
            f"{m(f'{a*a} + {b*b} = {c*c}')}.",
            diagram_en=svg_g9_right_triangle(f"{a} m", f"{b} m", "c = ?"),
        ))

    # Easy 4-5: Find unknown leg a = sqrt(c^2 - b^2)
    for b, c in [(7, 25), (12, 20)]:
        qid = _qid(cur); cur += 1
        a = math.isqrt(c * c - b * b)
        assert a * a + b * b == c * c
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-01",
            f"In a right triangle with hypotenuse {m(str(c))} cm and one leg {m(str(b))} cm, what is the length of the other leg in cm?",
            f"في مثلث قائم الزاوية طول وتره {m(str(c))} سم وطول أحد ساقيه {m(str(b))} سم، ما طول الساق الأخرى بالسنتيمتر؟",
            a, [c - b, a - 2, a + 4],
            f"Subtract squares: {m(f'a = \\sqrt{{{c}^2 - {b}^2}}')}.",
            f"اطرح المربعين: {m(f'a = \\sqrt{{{c}^2 - {b}^2}}')}.",
            "Subtract the known leg squared from the hypotenuse squared.",
            [f"{m(f'a = \\sqrt{{{c*c} - {b*b}}} = \\sqrt{{{a*a}}} = {a}')} cm."],
            f"{m(f'{a}^2 + {b}^2 = {c}^2')}.",
            "نطرح مربع الساق المعلومة من مربع الوتر.",
            [f"{m(f'a = \\sqrt{{{c*c} - {b*b}}} = {a}')} سم."],
            f"{m(f'{a*a} + {b*b} = {c*c}')}.",
            diagram_en=svg_g9_right_triangle("a = ?", f"{b} cm", f"{c} cm"),
        ))

    # Medium 6-10: Rectangle diagonal, square area from diagonal, isosceles altitude, drone displacement, screen width
    med_pyth = [
        (f"A rectangular solar collector measures {m('12')} m by {m('16')} m. What is the length of its diagonal brace in meters?",
         f"مجمّع شمسي مستطيل أبعاده {m('12')} م و{m('16')} م. ما طول دعامته القطرية بالأمتار؟",
         20, [28, 18, 22], "√(12² + 16²) = √(144 + 256) = √400 = 20", "12 m", "16 m", "d = ?"),
        (f"A square silicon wafer has a diagonal of length {m('10')} cm. What is the **area** of the square in {m(r'\text{cm}^2')}?",
         f"رقاقة سيليكون مربعة الشكل طول قطرها {m('10')} سم. ما **مساحة** المربع بالـ سم²؟",
         50, [100, 25, 40], "s² + s² = 10² ⇒ 2s² = 100 ⇒ Area s² = 50", "s", "s", "10 cm"),
        (f"An isosceles triangle has two equal sides of {m('13')} cm and a base of {m('10')} cm. What is its **area** in {m(r'\text{cm}^2')}?",
         f"مثلث متطابق الضلعين طول كل من ساقيه {m('13')} سم وطول قاعدته {m('10')} سم. ما **مساحته** بالـ سم²؟",
         60, [65, 120, 48], "Half-base = 5 ⇒ height h = √(13² − 5²) = 12 ⇒ Area = ½(10)(12) = 60", "h = 12", "5 cm", "13 cm"),
        (f"A survey drone flies {m('9')} km due north and then {m('40')} km due east. How many km is it in a straight line from its launch pad?",
         f"طارت طائرة مسح مسيّرة {m('9')} كم شمالاً ثم {m('40')} كم شرقاً. كم كيلومتراً تبعد بخط مستقيم عن نقطة الإطلاق؟",
         41, [49, 39, 45], "√(9² + 40²) = √(81 + 1600) = √1681 = 41", "9 km", "40 km", "d = ?"),
        (f"A {m('34')}-inch display monitor (diagonal {m('34')} in) has height {m('16')} in. What is its width in inches?",
         f"شاشة عرض طول قطرها {m('34')} بوصة وارتفاعها {m('16')} بوصة. ما عرض الشاشة بالبوصة؟",
         30, [18, 28, 32], "√(34² − 16²) = √(1156 − 256) = √900 = 30", "16 in", "w = ?", "34 in"),
    ]
    for q_en, q_ar, ans, dists, note, la, lb, lc in med_pyth:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-01",
            q_en, q_ar, ans, dists,
            "Spot the hidden right triangle formed by the diagonal or altitude!",
            "استخرج المثلث القائم المخفي الذي يصنعه القطر أو الارتفاع العمودي!",
            "Apply the Pythagorean theorem to the embedded right triangle.",
            [f"{m(note)}."],
            "Pythagorean triple check passed.",
            "نطبّق نظرية فيثاغورس على المثلث القائم.",
            [f"{m(note)}."],
            "متحقق عبر ثلاثيات فيثاغورس.",
            diagram_en=svg_g9_right_triangle(la, lb, lc),
        ))

    # Hard 11-15: Two poles, 3D cuboid diagonal, algebraic triple, rhombus diagonals, sliding ladder
    hard_pyth = [
        (f"Two vertical towers of heights {m('11')} m and {m('23')} m stand on level ground {m('16')} m apart. What is the straight-line cable length (in m) connecting their tops?",
         f"برجان رأسيان ارتفاعاهما {m('11')} م و{m('23')} م يقفان على أرض أفقية والمسافة بين قاعدتيهما {m('16')} م. ما طول الكابل المستقيم الواصل بين قمتيهما بالأمتار؟",
         20, [28, 18, 24], "Δh = 23 − 11 = 12; d = √(16² + 12²) = √400 = 20"),
        (f"A rectangular shipping crate measures {m('3')} m by {m('4')} m by {m('12')} m. What is the length (in m) of the longest straight rod that fits diagonally from one corner to the opposite space corner?",
         f"صندوق شحن على شكل متوازي مستطيلات أبعاده {m('3')} م و{m('4')} م و{m('12')} م. ما طول أطول قضيب مستقيم يمكن وضعه قطرياً داخل الصندوق بالأمتار؟",
         13, [12, 15, 19], "√(3² + 4² + 12²) = √(9 + 16 + 144) = √169 = 13"),
        (f"A right triangle has legs {m('x')} cm and {m('(x + 7)')} cm, and hypotenuse {m('(x + 8)')} cm. What is {m('x')}?",
         f"مثلث قائم الزاوية طولا ساقيه {m('x')} سم و{m('(x + 7)')} سم وطول وتره {m('(x + 8)')} سم. ما قيمة {m('x')}؟",
         5, [6, 3, 8], "x² + (x+7)² = (x+8)² ⇒ x² − 2x − 15 = 0 ⇒ x = 5 (5-12-13)"),
        (f"A rhombus has side length {m('10')} cm and one diagonal of length {m('12')} cm. What is the **area** of the rhombus in {m(r'\text{cm}^2')}?",
         f"معين طول ضلعه {m('10')} سم وطول أحد قطريه {m('12')} سم. ما **مساحة** المعين بالـ سم²؟",
         96, [120, 48, 80], "Half-diagonals: √(10² − 6²) = 8 ⇒ d₂ = 16 ⇒ Area = ½(12)(16) = 96"),
        (f"A {m('25')}-m ladder leans against a vertical wall with its foot {m('7')} m from the wall. If the foot slides outward until it is {m('15')} m from the wall, by how many meters does the top of the ladder slide **down**?",
         f"يستند سلم طوله {m('25')} م إلى جدار رأسي وتبعد قاعدته {m('7')} م عن الجدار. إذا انزلقت قاعدته مبتعدة حتى أصبحت على بُعد {m('15')} م، فكم متراً تنخفض قمة السلم؟",
         4, [8, 20, 6], "Initial height √(625−49) = 24 m; new height √(625−225) = 20 m ⇒ drop = 24 − 20 = 4 m"),
    ]
    for q_en, q_ar, ans, dists, note in hard_pyth:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-01",
            q_en, q_ar, ans, dists,
            "Construct the right triangle of height-difference, perpendicular half-diagonals, or before/after ladder states!",
            "ارسم المثلث القائم الناتج من فرق الارتفاعين، أو أنصاف أقطار المعين المتعامدة، أو حالتي السلم!",
            "Decompose the geometric configuration into exact Pythagorean triples.",
            [f"{m(note)}."],
            "All right-triangle side squares balance.",
            "نحلل الشكل الهندسي إلى مثلث قائم ونطبق فيثاغورس.",
            [f"{m(note)}."],
            "مجموع مربعي الساقين يطابق مربع الوتر.",
            diagram_en=svg_g9_right_triangle("Δy", "Δx", "Hypotenuse"),
        ))
    return qs


def _gen_geo_02(start_idx: int) -> list[dict]:
    """G9-GEO-02: Coordinate distance & midpoint (including finding missing endpoint)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-3: Midpoint M
    mid_easy = [((-4, 2), (6, 8)), ((1, -5), (7, 3)), ((-6, -2), (-2, 4))]
    for (x1, y1), (x2, y2) in mid_easy:
        qid = _qid(cur); cur += 1
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        ans_s = f"({mx}, {my})"
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-02",
            f"What are the coordinates of the midpoint of segment {m('AB')} with {m(f'A({x1}, {y1})')} and {m(f'B({x2}, {y2})')}?",
            f"ما إحداثيا نقطة منتصف القطعة المستقيمة {m('AB')} حيث {m(f'A({x1}, {y1})')} و{m(f'B({x2}, {y2})')}؟",
            ans_s, [f"({(x2-x1)//2}, {(y2-y1)//2})", f"({x1+x2}, {y1+y2})", f"({my}, {mx})"],
            "Average the x-coordinates and average the y-coordinates.",
            "احسب متوسط الإحداثيين السينيين ومتوسط الإحداثيين الصاديين.",
            "Use M = ((x₁ + x₂)/2, (y₁ + y₂)/2).",
            [f"{m(rf'M = \left(\frac{{{x1}+{x2}}}{{2}}, \frac{{{y1}+{y2}}}{{2}}\right) = ({mx}, {my})')}."],
            "Midpoint lies halfway between A and B on both axes.",
            "نجمع الإحداثيات ونقسم على 2.",
            [f"{m(f'M = ({mx}, {my})')}."],
            "النقطة تتوسط المسافة أفقياً ورأسياً.",
            diagram_en=svg_nafes_coordinate_line([(x1, y1, "A"), (mx, my, "M"), (x2, y2, "B")], max_coord=9),
        ))

    # Easy 4-5: Distance d
    dist_easy = [((-1, 2), (2, 6), 5), ((-3, -1), (2, 11), 13)]
    for (x1, y1), (x2, y2), ans in dist_easy:
        qid = _qid(cur); cur += 1
        assert (x2 - x1) ** 2 + (y2 - y1) ** 2 == ans * ans
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-02",
            f"What is the exact distance between {m(f'P({x1}, {y1})')} and {m(f'Q({x2}, {y2})')} on the coordinate plane?",
            f"ما المسافة الدقيقة بين النقطتين {m(f'P({x1}, {y1})')} و{m(f'Q({x2}, {y2})')} في المستوى الإحداثي؟",
            ans, [abs(x2 - x1) + abs(y2 - y1), ans - 1, ans + 2],
            f"Apply {m(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')}.",
            f"استخدم قانون المسافة {m(r'd = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')}.",
            "Find Δx and Δy, then compute √(Δx² + Δy²).",
            [f"{m(f'\\Delta x = {abs(x2-x1)}')}, {m(f'\\Delta y = {abs(y2-y1)}')}, so {m(f'd = \\sqrt{{{abs(x2-x1)}^2 + {abs(y2-y1)}^2}} = {ans}')}."],
            f"{m(f'{abs(x2-x1)}^2 + {abs(y2-y1)}^2 = {ans}^2')}.",
            "نحسب فرق السينات وفرق الصادات ثم نطبّق قانون المسافة.",
            [f"{m(f'd = \\sqrt{{{(x2-x1)**2} + {(y2-y1)**2}}} = {ans}')}."],
            f"مربع المسافة يساوي {m(str(ans*ans))}.",
            diagram_en=svg_nafes_coordinate_line([(x1, y1, "P"), (x2, y2, "Q")], max_coord=12),
        ))

    # Medium 6-10: Missing endpoint B = 2M - A & circle radius/diameter
    med_coord = [
        (f"Point {m('M(2, 5)')} is the midpoint of {m('AB')}. If {m('A(-3, 1)')}, what is {m('x_B + y_B')} for endpoint {m('B(x_B, y_B)')}?",
         f"إذا كانت {m('M(2, 5)')} منتصف القطعة {m('AB')} وكانت {m('A(-3, 1)')}، فما قيمة {m('x_B + y_B')} للطرف {m('B')}؟",
         16, [7, 9, 12], "B = (2(2)−(−3), 2(5)−1) = (7, 9) ⇒ 7 + 9 = 16", [(-3, 1, "A"), (2, 5, "M"), (7, 9, "B")]),
        (f"If {m('M(-1, 3)')} is the midpoint of {m('CD')} and {m('C(4, 8)')}, what are the coordinates of {m('D')}?",
         f"إذا كانت {m('M(-1, 3)')} منتصف {m('CD')} وكانت {m('C(4, 8)')}، فما إحداثيا النقطة {m('D')}؟",
         "(-6, -2)", ["(1.5, 5.5)", "(-5, -5)", "(6, -2)"], "x_D = −2 − 4 = −6; y_D = 6 − 8 = −2", [(4, 8, "C"), (-1, 3, "M"), (-6, -2, "D?")]),
        (f"A circle has center {m('C(2, -1)')} and passes through {m('P(8, 7)')}. What is the **diameter** of the circle?",
         f"دائرة مركزها {m('C(2, -1)')} وتمر بالنقطة {m('P(8, 7)')}. ما طول **قطر** الدائرة؟",
         20, [10, 14, 28], "r = √(6² + 8²) = 10 ⇒ diameter = 2r = 20", [(2, -1, "C"), (8, 7, "P")]),
        (f"Vertices of right triangle {m('ABC')} are {m('A(1, 1)')}, {m('B(7, 1)')}, and {m('C(1, 9)')}. What is the **perimeter** of {m(r'\triangle ABC')}?",
         f"رؤوس المثلث القائم {m('ABC')} هي {m('A(1, 1)')} و{m('B(7, 1)')} و{m('C(1, 9)')}. ما **محيط** المثلث؟",
         24, [14, 16, 48], "AB = 6, AC = 8, BC = √(6² + 8²) = 10 ⇒ P = 6 + 8 + 10 = 24", [(1, 1, "A"), (7, 1, "B"), (1, 9, "C")]),
        (f"Segment {m('PQ')} with {m('P(-5, 4)')} and {m('Q(3, -2)')} is a diameter of a circle. What is the **radius** of this circle?",
         f"القطعة {m('PQ')} حيث {m('P(-5, 4)')} و{m('Q(3, -2)')} هي قطر في دائرة. ما طول **نصف قطر** هذه الدائرة؟",
         5, [10, 7, 25], "PQ = √(8² + (−6)²) = 10 ⇒ radius = 10 / 2 = 5", [(-5, 4, "P"), (3, -2, "Q")]),
    ]
    for q_en, q_ar, ans, dists, note, pts in med_coord:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-02",
            q_en, q_ar, ans, dists,
            "Watch carefully whether the question asks for radius vs diameter, or missing endpoint 2M − A!",
            "انتبه جيداً هل المطلوب نصف القطر أم القطر الكامل، واستخدم 2M − A للطرف المجهول!",
            "Combine coordinate distance and midpoint formulas.",
            [f"{m(note)}."],
            "Coordinates and distances verified.",
            "نطبّق قانوني المسافة ونقطة المنتصف.",
            [f"{m(note)}."],
            "متحقق هندسياً.",
            diagram_en=svg_nafes_coordinate_line(pts, max_coord=10),
        ))

    # Hard 11-15: Unknown y for given distance, square area from opposite vertices, equidistant point on x-axis
    hard_coord = [
        (f"For what value of {m('y > 2')} is the distance between {m('(1, 2)')} and {m('(7, y)')} equal to {m('10')}?",
         f"ما قيمة {m('y > 2')} التي تجعل المسافة بين النقطتين {m('(1, 2)')} و{m('(7, y)')} تساوي {m('10')}؟",
         10, [8, 6, 12], "6² + (y − 2)² = 10² ⇒ (y − 2)² = 64 ⇒ y − 2 = 8 ⇒ y = 10"),
        (f"Two opposite vertices of a square are {m('A(-1, 2)')} and {m('C(5, 8)')}. What is the **area** of the square?",
         f"رأسان متقابلان في مربع هما {m('A(-1, 2)')} و{m('C(5, 8)')}. ما **مساحة** المربع؟",
         36, [72, 18, 24], "Diagonal² = 6² + 6² = 72; Area = d² / 2 = 72 / 2 = 36"),
        (f"Point {m('P(x, 0)')} on the {m('x')}-axis is equidistant from {m('A(1, 3)')} and {m('B(5, 5)')}. What is {m('x')}?",
         f"تقع النقطة {m('P(x, 0)')} على محور السينات على بُعدين متساويين من {m('A(1, 3)')} و{m('B(5, 5)')}. ما قيمة {m('x')}؟",
         5, [3, 4, 6], "(x−1)² + 9 = (x−5)² + 25 ⇒ −2x + 10 = −10x + 50 ⇒ 8x = 40 ⇒ x = 5"),
        (f"On segment {m('AB')} with {m('A(0, 0)')} and {m('B(12, 8)')}, {m('M')} is the midpoint of {m('AB')} and {m('N')} is the midpoint of {m('MB')}. What is {m('x_N + y_N')}?",
         f"على القطعة {m('AB')} حيث {m('A(0, 0)')} و{m('B(12, 8)')}، {m('M')} منتصف {m('AB')} و{m('N')} منتصف {m('MB')}. ما قيمة {m('x_N + y_N')}؟",
         15, [10, 14, 16], "M = (6, 4); N = ((6+12)/2, (4+8)/2) = (9, 6) ⇒ 9 + 6 = 15"),
        (f"The vertices of parallelogram {m('ABCD')} in order are {m('A(1, 2)')}, {m('B(6, 3)')}, {m('C(8, 7)')}, and {m('D(x, y)')}. Since diagonals bisect each other, what is {m('x + y')}?",
         f"رؤوس متوازي الأضلاع {m('ABCD')} بالترتيب هي {m('A(1, 2)')} و{m('B(6, 3)')} و{m('C(8, 7)')} و{m('D(x, y)')}. بما أن القطرين ينصّف كلٌّ منهما الآخر، فما قيمة {m('x + y')}؟",
         9, [11, 7, 10], "A + C = B + D ⇒ (9, 9) = (6 + x, 3 + y) ⇒ D = (3, 6) ⇒ x + y = 9"),
    ]
    for q_en, q_ar, ans, dists, note in hard_coord:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-02",
            q_en, q_ar, ans, dists,
            "Square the distance formula to remove radicals, or use the fact that parallelogram diagonals share the same midpoint!",
            "ربّع قانون المسافة للتخلص من الجذر، أو استخدم تساوي منتصف القطرين في متوازي الأضلاع!",
            "Apply coordinate geometry invariants.",
            [f"{m(note)}."],
            "Exact coordinate equality verified.",
            "نطبّق خواص الهندسة الإحداثية.",
            [f"{m(note)}."],
            "متحقق بالتعويض المباشر.",
            diagram_en=svg_nafes_coordinate_line([(1, 2, "A"), (5, 5, "B")], max_coord=10),
        ))
    return qs


def _gen_geo_03(start_idx: int) -> list[dict]:
    """G9-GEO-03: Shaded composite areas involving circles, sectors, semicircles & polygons."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Sectors, semicircles & concentric rings
    area_easy = [
        (f"What is the exact area (in {m(r'\text{cm}^2')}) of a {m('90^\\circ')} circular sector of radius {m('8')} cm?",
         f"ما المساحة الدقيقة (بالـ سم²) لقطاع دائري زاويته المركزية {m('90^\\circ')} ونصف قطره {m('8')} سم؟",
         r"16\pi", [r"64\pi", r"8\pi", r"32\pi"], "(90/360) × π(8²) = 16π", svg_g9_sector_or_ring("r = 8", "90°", 90)),
        (f"What is the exact area (in {m(r'\text{cm}^2')}) of a {m('60^\\circ')} sector in a circle of radius {m('6')} cm?",
         f"ما المساحة الدقيقة (بالـ سم²) لقطاع دائري زاويته {m('60^\\circ')} ونصف قطره {m('6')} سم؟",
         r"6\pi", [r"36\pi", r"12\pi", r"3\pi"], "(60/360) × 36π = 6π", svg_g9_sector_or_ring("r = 6", "60°", 60)),
        (f"Using {m(r'\pi = \frac{22}{7}')}, what is the area (in {m(r'\text{m}^2')}) of a semicircle of **diameter** {m('14')} m?",
         f"باعتبار {m(r'\pi = \frac{22}{7}')}، ما مساحة نصف دائرة طول **قطرها** {m('14')} م بالمتر المربع؟",
         77, [154, 44, 308], "r = 7; ½ × (22/7) × 49 = 77", svg_g9_sector_or_ring("r = 7", "180°", 180)),
        (f"A circular walkway lies between two concentric circles of radii {m('10')} m and {m('6')} m. What is the walkway's area in {m(r'\text{m}^2')}?",
         f"ممر دائري محصور بين دائرتين متحدتي المركز نصفا قطريهما {m('10')} م و{m('6')} م. ما مساحة الممر بالمتر المربع؟",
         r"64\pi", [r"16\pi", r"136\pi", r"8\pi"], "π(10² − 6²) = 64π", svg_g9_sector_or_ring("R = 10", "r = 6", ring=True)),
        (f"What is the shaded triangle's area (in {m(r'\text{cm}^2')}) inside a {m('18')} cm by {m('10')} cm rectangle when its base is the full bottom edge and its apex touches the top edge?",
         f"ما مساحة المثلث المظلل (بالـ سم²) المرسوم داخل مستطيل أبعاده {m('18')} سم و{m('10')} سم إذا كانت قاعدته الضلع السفلي كاملاً ورأسه على الضلع العلوي؟",
         90, [180, 45, 56], "½ × 18 × 10 = 90", svg_shaded_triangle_in_rect(18, 10)),
    ]
    for q_en, q_ar, ans, dists, note, diag in area_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-03",
            q_en, q_ar, ans, dists,
            "Use Sector = (θ/360)πr², Ring = π(R² − r²), and remember r = d/2!",
            "استخدم قانون القطاع (θ/360)πr²، والحلقة π(R² − r²)، وتذكّر أن نصف القطر نصف القطر الكامل!",
            "Apply standard circular/composite area formulas.",
            [f"{m(note)}."],
            "Units and radius checked.",
            "نطبّق قانون المساحة الدائرية مباشرة.",
            [f"{m(note)}."],
            "تم التحقق من نصف القطر والوحدات.",
            diagram_en=diag,
        ))

    # Medium 6-10: Square minus circle, midpoint square, stadium, two semicircles
    area_med = [
        (f"A circle is inscribed in a square of side {m('20')} cm. Using {m(r'\pi \approx 3.14')}, what is the shaded corner area outside the circle (in {m(r'\text{cm}^2')})?",
         f"دائرة مرسومة داخل مربع طول ضلعه {m('20')} سم وتمس أضلاعه. باعتبار {m(r'\pi \approx 3.14')}، ما المساحة المظللة خارج الدائرة وداخل المربع بالـ سم²؟",
         86, [314, 114, 43], "20² − 3.14(10²) = 400 − 314 = 86", svg_square_circle_shaded("20 cm", "inscribed_outside")),
        (f"The midpoints of the four sides of a square of side {m('12')} cm are joined to form an inner shaded square. What is the area of the inner square in {m(r'\text{cm}^2')}?",
         f"وُصلت منتصفات أضلاع مربع طول ضلعه {m('12')} سم لتكوين مربع داخلي مظلل. ما مساحة المربع الداخلي بالـ سم²؟",
         72, [144, 36, 96], "Inner square is half of outer square: 12² / 2 = 144 / 2 = 72", svg_midpoint_square_shaded("12 cm", shade_inner=True)),
        (f"From a square plate of side {m('14')} cm, two inward semicircles of diameter {m('14')} cm on opposite sides are cut out ({m(r'\pi = 22/7')}). What area (in {m(r'\text{cm}^2')}) remains?",
         f"من صفيحة مربعة طول ضلعها {m('14')} سم، قُطع نصفا دائرتين قطراهما {m('14')} سم من ضلعين متقابلين ({m(r'\pi = 22/7')}). كم سم² تبقى من الصفيحة؟",
         42, [119, 154, 49], "Two semicircles = 1 full circle (r = 7): 196 − 154 = 42", svg_square_circle_shaded("14 cm", "two_semis_outside")),
        (f"An athletic field consists of a {m('50')} m by {m('14')} m rectangle capped by two outer semicircles on the {m('14')}-m ends ({m(r'\pi = 22/7')}). What is its total area in {m(r'\text{m}^2')}?",
         f"ملعب يتكون من مستطيل أبعاده {m('50')} م و{m('14')} م ينتهي بنصفي دائرتين على الضلعين اللذين طولهما {m('14')} م ({m(r'\pi = 22/7')}). ما المساحة الكلية للملعب بالمتر المربع؟",
         854, [700, 777, 1316], "Rect 50×14 = 700 + full circle (22/7)(7²) = 154 ⇒ 854", svg_square_circle_shaded("50 m", "stadium")),
        (f"What is the exact area (in {m(r'\text{cm}^2')}) of a {m('120^\\circ')} sector in a circle of radius {m('9')} cm?",
         f"ما المساحة الدقيقة (بالـ سم²) لقطاع دائري زاويته {m('120^\\circ')} في دائرة نصف قطرها {m('9')} سم؟",
         r"27\pi", [r"81\pi", r"18\pi", r"9\pi"], "(120/360) × 81π = 27π", svg_g9_sector_or_ring("r = 9", "120°", 120)),
    ]
    for q_en, q_ar, ans, dists, note, diag in area_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-03",
            q_en, q_ar, ans, dists,
            "Combine identical semicircles into a full circle and subtract cutouts from the outer region!",
            "ادمج نصفي الدائرتين المتطابقتين في دائرة كاملة واطرح الأجزاء المفرغة من المساحة الكلية!",
            "Decompose composite area into elementary shapes.",
            [f"{m(note)}."],
            "Component areas sum cleanly to the bounding figure.",
            "نقسّم الشكل المركب إلى مساحات أساسية بسيطة.",
            [f"{m(note)}."],
            "مجموع الأجزاء يساوي المساحة الكلية.",
            diagram_en=diag,
        ))

    # Hard 11-15: Square inscribed in circle, quarter-circle minus triangle, perimeter of stadium, sector angle from area
    area_hard = [
        (f"A square is inscribed **inside** a circle of radius {m('6')} cm (so the circle's diameter is the square's diagonal). What is the shaded area between the circle and the square?",
         f"مربع مرسوم **داخل** دائرة نصف قطرها {m('6')} سم (قطر الدائرة هو قطر المربع). ما مساحة المنطقة المحصورة بين الدائرة والمربع؟",
         r"36\pi - 72", [r"36\pi - 36", r"12\pi - 72", r"36\pi - 144"], "Circle = 36π; square diagonal d = 12 ⇒ Area = d²/2 = 72", svg_g9_sector_or_ring("R = 6", "d = 12", ring=True)),
        (f"In a quarter-circle OAB of radius {m('10')} cm ({m(r'\angle AOB = 90^\circ')}), chord {m('AB')} cuts off right triangle {m('OAB')}. Using {m(r'\pi \approx 3.14')}, what is the area of the circular segment outside {m(r'\triangle OAB')} (in {m(r'\text{cm}^2')})?",
         f"في ربع دائرة {m('OAB')} نصف قطرها {m('10')} سم، الوتر {m('AB')} يحصر المثلث القائم {m('OAB')}. باعتبار {m(r'\pi \approx 3.14')}، ما مساحة القطعة الدائرية المحصورة بين القوس والوتر بالـ سم²؟",
         28.5, [78.5, 50, 14.25], "¼(3.14)(100) − ½(10)(10) = 78.5 − 50 = 28.5", svg_g9_sector_or_ring("r = 10", "90°", 90)),
        (f"Four quarter-circles of radius {m('7')} cm are centered at the four corners of a {m('14')} cm square ({m(r'\pi = 22/7')}). What is the area of the central unshaded star region in {m(r'\text{cm}^2')}?",
         f"أربعة أرباع دوائر نصف قطر كلٍّ منها {m('7')} سم مراكزها رؤوس مربع طول ضلعه {m('14')} سم ({m(r'\pi = 22/7')}). ما مساحة المنطقة الوسطى المحصورة بينها بالـ سم²؟",
         42, [154, 49, 28], "4 quarter-circles = 1 full circle of r = 7 (154); 196 − 154 = 42", svg_square_circle_shaded("14 cm", "inscribed_outside")),
        (f"A sector in a circle of radius {m('12')} cm has area {m(r'24\pi\text{ cm}^2')}. What is the sector's central angle in degrees?",
         f"قطاع دائري في دائرة نصف قطرها {m('12')} سم مساحته {m(r'24\pi')} سم². ما قياس زاويته المركزية بالدرجات؟",
         60, [30, 45, 72], "(θ/360) × 144π = 24π ⇒ θ = 360 / 6 = 60°", svg_g9_sector_or_ring("r = 12", "θ = ?", 60)),
        (f"What is the **perimeter** (in m) of a stadium track formed by a {m('60')} m by {m('28')} m rectangle with two outer semicircles on the {m('28')}-m widths ({m(r'\pi = 22/7')})?",
         f"ما **محيط** مضمار جري (بالمتر) يتكون من مستطيل طوله {m('60')} م وعرضه {m('28')} م مع نصفي دائرتين خارجيتين على العرضين ({m(r'\pi = 22/7')})؟",
         208, [264, 176, 308], "2 straight 60 m sides (120) + 1 full circle circumference πd = (22/7)(28) = 88 ⇒ 208 m", svg_square_circle_shaded("60 m", "stadium")),
    ]
    for q_en, q_ar, ans, dists, note, diag in area_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-03",
            q_en, q_ar, ans, dists,
            "Exclude interior dashed edges when finding outer perimeter, and use d²/2 for a square inscribed in a circle!",
            "استبعد الأضلاع الداخلية المتقطعة عند حساب المحيط الخارجي، واستخدم d²/2 لمساحة المربع داخل دائرة!",
            "Synthesize circle, sector, and polygon area/perimeter relationships.",
            [f"{m(note)}."],
            "Geometric decomposition verified.",
            "نربط خواص الدائرة والمربع والقطاع الدائري.",
            [f"{m(note)}."],
            "متحقق هندسياً.",
            diagram_en=diag,
        ))
    return qs


def _gen_geo_04(start_idx: int) -> list[dict]:
    """G9-GEO-04: Volume & surface area of cylinders, cones, pyramids & spheres."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Direct 3D solid formulas
    sol_easy = [
        (f"What is the exact volume (in {m(r'\text{cm}^3')}) of a cylinder with radius {m('4')} cm and height {m('7')} cm?",
         f"ما الحجم الدقيق (بالـ سم³) لأسطوانة نصف قطر قاعدتها {m('4')} سم وارتفاعها {m('7')} سم؟",
         r"112\pi", [r"28\pi", r"56\pi", r"196\pi"], "π(4²)(7) = 112π", svg_g9_solid_3d("cylinder", "r = 4", "h = 7")),
        (f"What is the exact volume (in {m(r'\text{cm}^3')}) of a cone with radius {m('3')} cm and height {m('8')} cm?",
         f"ما الحجم الدقيق (بالـ سم³) لمخروط دائري قائم نصف قطره {m('3')} سم وارتفاعه {m('8')} سم؟",
         r"24\pi", [r"72\pi", r"16\pi", r"8\pi"], "⅓π(3²)(8) = 24π", svg_g9_solid_3d("cone", "r = 3", "h = 8")),
        (f"A square pyramid at an AlUla exhibit has base side {m('6')} m and perpendicular height {m('10')} m. What is its volume in {m(r'\text{m}^3')}?",
         f"مجسم هرمي رباعي منتظم طول ضلع قاعدته المربعة {m('6')} م وارتفاعه العمودي {m('10')} م. ما حجمه بالمتر المكعب؟",
         120, [360, 60, 180], "⅓ × 6² × 10 = 120", svg_g9_solid_3d("pyramid", "s = 6", "h = 10")),
        (f"What is the exact volume (in {m(r'\text{cm}^3')}) of a sphere of radius {m('3')} cm?",
         f"ما الحجم الدقيق (بالـ سم³) لكرة نصف قطرها {m('3')} سم؟",
         r"36\pi", [r"12\pi", r"27\pi", r"108\pi"], "(4/3)π(3³) = 36π", svg_g9_solid_3d("sphere", "r = 3")),
        (f"What is the exact **surface area** (in {m(r'\text{cm}^2')}) of a sphere of radius {m('5')} cm?",
         f"ما **المساحة السطحية** الدقيقة (بالـ سم²) لكرة نصف قطرها {m('5')} سم؟",
         r"100\pi", [r"25\pi", r"50\pi", r"500\pi"], "4π(5²) = 100π", svg_g9_solid_3d("sphere", "r = 5")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sol_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-04",
            q_en, q_ar, ans, dists,
            "Use V_cyl = πr²h, V_cone = ⅓πr²h, V_pyr = ⅓Bh, V_sph = (4/3)πr³, S_sph = 4πr².",
            "طبّق قوانين الحجوم والمساحة السطحية للمجسمات الدورانية والهرم.",
            "Substitute r and h into the 3D solid formula.",
            [f"{m(note)}."],
            "Formula and exponent dimensions verified.",
            "نعوّض بنصف القطر والارتفاع في القانون.",
            [f"{m(note)}."],
            "تم التحقق من القانون والأبعاد.",
            diagram_en=diag,
        ))

    # Medium 6-10: Cylinder lateral/total area, cone with slant height, missing height, hemisphere
    sol_med = [
        (f"Using {m(r'\pi = \frac{22}{7}')}, what is the **lateral** surface area (in {m(r'\text{cm}^2')}) of a cylinder with radius {m('7')} cm and height {m('10')} cm?",
         f"باعتبار {m(r'\pi = \frac{22}{7}')}، ما **المساحة الجانبية** (بالـ سم²) لأسطوانة نصف قطرها {m('7')} سم وارتفاعها {m('10')} سم؟",
         440, [220, 748, 1540], "2πrh = 2 × (22/7) × 7 × 10 = 440", svg_g9_solid_3d("cylinder", "r = 7", "h = 10")),
        (f"What is the **total** surface area (in {m(r'\text{cm}^2')}) of a closed cylinder with radius {m('3')} cm and height {m('7')} cm?",
         f"ما **المساحة الكلية** (بالـ سم²) لأسطوانة مغلقة نصف قطرها {m('3')} سم وارتفاعها {m('7')} سم؟",
         r"60\pi", [r"42\pi", r"51\pi", r"63\pi"], "2πr(r + h) = 6π(10) = 60π", svg_g9_solid_3d("cylinder", "r = 3", "h = 7")),
        (f"A right circular cone has base radius {m('5')} cm and **slant height** {m('13')} cm. What is its exact volume in {m(r'\text{cm}^3')}?",
         f"مخروط دائري قائم نصف قطر قاعدته {m('5')} سم وطول **راسمه (ارتفاعه المائل)** {m('13')} سم. ما حجمه الدقيق بالـ سم³؟",
         r"100\pi", [r"300\pi", r"65\pi", r"325\pi"], "h = √(13² − 5²) = 12 ⇒ V = ⅓π(25)(12) = 100π", svg_g9_solid_3d("cone", "r = 5", "l = 13")),
        (f"A cylindrical storage silo has volume {m(r'250\pi\text{ m}^3')} and base radius {m('5')} m. What is its height in meters?",
         f"صومعة أسطوانية حجمها {m(r'250\pi')} م³ ونصف قطر قاعدتها {m('5')} م. ما ارتفاعها بالأمتار؟",
         10, [50, 5, 25], "π(25)h = 250π ⇒ h = 10", svg_g9_solid_3d("cylinder", "r = 5", "h = ?")),
        (f"An AlUla observatory dome is a hemisphere of radius {m('6')} m. What is the interior volume of the hemisphere in {m(r'\text{m}^3')}?",
         f"قبة مرصد في العلا على شكل **نصف كرة** نصف قطرها {m('6')} م. ما حجمها الداخلي بالمتر المكعب؟",
         r"144\pi", [r"288\pi", r"72\pi", r"48\pi"], "(2/3)π(6³) = (2/3)(216π) = 144π", svg_g9_solid_3d("sphere", "r = 6", caption="Hemisphere")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sol_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-04",
            q_en, q_ar, ans, dists,
            "Distinguish lateral area (2πrh) from total area (2πrh + 2πr²), and perpendicular height h from slant height l!",
            "ميّز بين المساحة الجانبية والكلية، وبين الارتفاع العمودي h والارتفاع المائل (الراسم) l!",
            "Solve for any intermediate dimension first, then evaluate the volume/area formula.",
            [f"{m(note)}."],
            "Verified.",
            "نوجد البُعد الوسيط إن لزم ثم نطبّق القانون.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Hard 11-15: Volume conservation (melting), scaling, cylinder-to-cone pouring, water rise
    sol_hard = [
        (f"A solid metal sphere of radius {m('6')} cm is melted and recast into identical solid cones each of radius {m('3')} cm and height {m('8')} cm. How many cones are produced?",
         f"صُهرت كرة معدنية مصمتة نصف قطرها {m('6')} سم وأُعيد تشكيلها إلى مخاريط متماثلة نصف قطر كل منها {m('3')} سم وارتفاعه {m('8')} سم. كم مخروطاً ينتج؟",
         12, [4, 9, 36], "V_sph = (4/3)π(216) = 288π; V_cone = ⅓π(9)(8) = 24π ⇒ 288π / 24π = 12", svg_g9_solid_3d("sphere", "R = 6")),
        (f"If the radius of a cylinder is **doubled** and its height is **tripled**, its volume is multiplied by what factor?",
         f"إذا **ضوعف** نصف قطر قاعدة أسطوانة مرتين و**ضوعف** ارتفاعها {m('3')} مرات، فبكم مرة يتضاعف حجمها؟",
         12, [6, 18, 24], "π(2r)²(3h) = 4 × 3 πr²h = 12 V", svg_g9_solid_3d("cylinder", "2r", "3h")),
        (f"A full cylindrical pitcher of radius {m('6')} cm and height {m('15')} cm pours water into empty conical cups of the **same radius** {m('6')} cm and height {m('5')} cm. How many conical cups can it completely fill?",
         f"إبريق أسطواني مملوء بالماء نصف قطره {m('6')} سم وارتفاعه {m('15')} سم يُفرغ في أكواب مخروطية لها **نفس نصف القطر** {m('6')} سم وارتفاع كل منها {m('5')} سم. كم كوباً يمتلئ تماماً؟",
         9, [3, 6, 15], "V_cyl / V_cone = (π·36·15) / (⅓π·36·5) = 15 / (5/3) = 9", svg_g9_solid_3d("cone", "r = 6", "h = 5")),
        (f"A cylindrical beaker of radius {m('4')} cm contains water. When a solid metal sphere of radius {m('3')} cm is completely submerged in the water, by how many centimeters does the water level rise?",
         f"مخبار أسطواني نصف قطره {m('4')} سم يحوي ماءً. عند غمر كرة معدنية نصف قطرها {m('3')} سم بالكامل في الماء، كم سنتيمتراً يرتفع مستوى سطح الماء؟",
         Fraction(9, 4), [3, Fraction(3, 4), Fraction(9, 2)], "π(4²) Δh = (4/3)π(3³) = 36π ⇒ 16 Δh = 36 ⇒ Δh = 9/4 cm", svg_g9_solid_3d("cylinder", "r = 4", "Δh = ?")),
        (f"A sphere is inscribed tightly inside a right cylinder (so cylinder radius {m('r')} and height {m('2r')}). What is the ratio of the sphere's volume to the cylinder's volume?",
         f"كرة مرسومة داخل أسطوانة قائمة بحيث تمس قاعدتيها وجانبها (ارتفاع الأسطوانة {m('2r')}). ما نسبة حجم الكرة إلى حجم الأسطوانة؟",
         Fraction(2, 3), [Fraction(1, 3), Fraction(3, 4), Fraction(1, 2)], "[(4/3)πr³] / [πr²(2r)] = (4/3) / 2 = 2/3", svg_g9_solid_3d("cylinder", "r", "h = 2r")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sol_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-04",
            q_en, q_ar, ans, dists,
            "Equate volumes before and after melting/submerging, and remember r is squared in cylinders and cubed in spheres!",
            "ساوِ الحجم قبل وبعد الصهر أو الغمر، وتذكّر أن نصف القطر يُربّع في الأسطوانة ويُكعّب في الكرة!",
            "Apply 3D volume conservation and scaling laws.",
            [f"{m(note)}."],
            "π cancels cleanly in every ratio.",
            "نطبّق مبدأ حفظ الحجم والنسب الهندسية.",
            [f"{m(note)}."],
            "يُختصر الرمز π في الطرفين.",
            diagram_en=diag,
        ))
    return qs


# ==============================================================================
# UNIT 3.5 (G9-GEO-05 .. G9-GEO-08): Parallel Angles, Polygons, Similarity & Transf.
# ==============================================================================

def _gen_geo_05(start_idx: int) -> list[dict]:
    """G9-GEO-05: Parallel lines with transversals & triangle exterior angle theorem."""
    from nafes_common import svg_parallel_zigzag
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Direct angle rules
    ang_easy = [
        (f"Two parallel lines are cut by a transversal. If one alternate interior angle is {m('73^\\circ')}, what is the other alternate interior angle in degrees?",
         f"يقطع مستقيم مستقيمين متوازيين. إذا كان قياس إحدى الزاويتين المتبادلتين داخلياً {m('73^\\circ')}، فما قياس الأخرى بالدرجات؟",
         73, [107, 17, 146], "Alternate interior angles are equal → 73°", svg_g9_parallel_transversal("73°", "?°", "alt_int")),
        (f"A transversal crosses two parallel lines. If one co-interior (same-side interior) angle measures {m('68^\\circ')}, what is the other co-interior angle in degrees?",
         f"يقطع قاطع مستقيمين متوازيين. إذا كان قياس إحدى الزاويتين المتحالفتين {m('68^\\circ')}، فما قياس الزاوية المتحالفة معها بالدرجات؟",
         112, [68, 22, 122], "180° − 68° = 112°", svg_g9_parallel_transversal("68°", "?°", "co_int")),
        (f"Two parallel rails are crossed by a diagonal beam forming a corresponding angle of {m('115^\\circ')}. What is the matching corresponding angle in degrees?",
         f"قضيبان متوازيان تقطعهما عارضة مائلة بزاوية متناظرة قياسها {m('115^\\circ')}. ما قياس الزاوية المتناظرة المطابقة لها بالدرجات؟",
         115, [65, 75, 57], "Corresponding angles are congruent → 115°", svg_g9_parallel_transversal("115°", "?°", "corr")),
        (f"In a triangle, two remote interior angles measure {m('54^\\circ')} and {m('63^\\circ')}. What is the measure of the opposite exterior angle in degrees?",
         f"في مثلث، قياسا زاويتين داخليتين بعيدتين هما {m('54^\\circ')} و{m('63^\\circ')}. ما قياس الزاوية الخارجية المقابلة لهما بالدرجات؟",
         117, [63, 126, 107], "54° + 63° = 117°", svg_g9_parallel_transversal("54°", "63°", "ext_tri", "?°")),
        (f"An exterior angle of a triangle measures {m('134^\\circ')}, and one of its remote interior angles is {m('58^\\circ')}. What is the other remote interior angle in degrees?",
         f"قياس زاوية خارجية لمثلث {m('134^\\circ')}، وإحدى الزاويتين الداخليتين البعيدتين {m('58^\\circ')}. ما قياس الزاوية الداخلية البعيدة الأخرى بالدرجات؟",
         76, [46, 66, 86], "134° − 58° = 76°", svg_g9_parallel_transversal("58°", "?°", "ext_tri", "134°")),
    ]
    for q_en, q_ar, ans, dists, note, diag in ang_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-05",
            q_en, q_ar, ans, dists,
            "Alternate interior and corresponding angles are equal; co-interior angles sum to 180°; exterior angle = sum of remote interiors!",
            "المتبادلتان والمتناظرتان متطابقتان، والمتحالفتان مجموعهما 180°، والخارجية تساوي مجموع البعيدتين!",
            "Apply parallel-line or exterior-angle theorem.",
            [f"{m(note)}."],
            "Angle sum checked.",
            "نطبّق علاقة الزوايا المناسبة مباشرة.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Medium 6-10: Algebraic parallel & exterior angle equations
    ang_med = [
        (f"Across parallel lines, alternate interior angles measure {m('(4x - 10)^\\circ')} and {m('(2x + 34)^\\circ')}. What is {m('x')}?",
         f"بين مستقيمين متوازيين، زاويتان متبادلتان داخلياً قياساهما {m('(4x - 10)^\\circ')} و{m('(2x + 34)^\\circ')}. ما قيمة {m('x')}؟",
         22, [12, 26, 78], "4x − 10 = 2x + 34 ⇒ 2x = 44 ⇒ x = 22", svg_g9_parallel_transversal("4x − 10°", "2x + 34°", "alt_int")),
        (f"Corresponding angles on parallel lines measure {m('(5x - 16)^\\circ')} and {m('(3x + 20)^\\circ')}. Find the **actual angle measure** in degrees.",
         f"زاويتان متناظرتان على مستقيمين متوازيين قياساهما {m('(5x - 16)^\\circ')} و{m('(3x + 20)^\\circ')}. أوجد **قياس الزاوية الفعلي** بالدرجات.",
         74, [18, 106, 68], "5x − 16 = 3x + 20 ⇒ x = 18 ⇒ angle = 3(18) + 20 = 74°", svg_g9_parallel_transversal("5x − 16°", "3x + 20°", "corr")),
        (f"Co-interior angles between parallel lines are {m('(2x + 10)^\\circ')} and {m('(3x + 20)^\\circ')}. What is the measure of the **smaller** angle in degrees?",
         f"زاويتان متحالفتان بين مستقيمين متوازيين قياساهما {m('(2x + 10)^\\circ')} و{m('(3x + 20)^\\circ')}. ما قياس الزاوية **الصغرى** بالدرجات؟",
         70, [30, 110, 60], "5x + 30 = 180 ⇒ x = 30 ⇒ angles 70° and 110°", svg_g9_parallel_transversal("2x + 10°", "3x + 20°", "co_int")),
        (f"In a triangle, an exterior angle is {m('(4x + 8)^\\circ')} and its two remote interior angles are {m('(2x - 4)^\\circ')} and {m('56^\\circ')}. What is {m('x')}?",
         f"في مثلث، زاوية خارجية قياسها {m('(4x + 8)^\\circ')} والداخليتان البعيدتان {m('(2x - 4)^\\circ')} و{m('56^\\circ')}. ما قيمة {m('x')}؟",
         22, [26, 20, 30], "4x + 8 = 2x + 52 ⇒ 2x = 44 ⇒ x = 22", svg_g9_parallel_transversal("2x − 4°", "56°", "ext_tri", "4x + 8°")),
        (f"Two co-interior angles between parallel lines are in the ratio {m('4 : 5')}. What is the measure of the **larger** angle in degrees?",
         f"النسبة بين قياسي زاويتين متحالفتين بين مستقيمين متوازيين هي {m('4 : 5')}. ما قياس الزاوية **الكبرى** بالدرجات؟",
         100, [80, 90, 120], "4k + 5k = 180° ⇒ k = 20° ⇒ 5k = 100°", svg_g9_parallel_transversal("4k", "5k", "co_int")),
    ]
    for q_en, q_ar, ans, dists, note, diag in ang_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-05",
            q_en, q_ar, ans, dists,
            "Check whether the question asks for x or for the substituted angle in degrees!",
            "تأكد هل السؤال يطلب قيمة المتغير x أم قياس الزاوية بعد التعويض!",
            "Solve for x and evaluate the target angle if required.",
            [f"{m(note)}."],
            "Verified.",
            "نحل المعادلة الجبرية ونعوض لإيجاد الزاوية المطلوبة.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Hard 11-15: Zigzag M-angles & multi-step triangle/parallel reasoning
    ang_hard = [
        (f"Between parallel lines {m(r'L_1 \parallel L_2')}, a two-segment zigzag forms acute angles of {m('38^\\circ')} with {m('L_1')} and {m('47^\\circ')} with {m('L_2')}. What is the vertex bend angle {m(r'\theta')} in degrees?",
         f"بين المستقيمين المتوازيين {m(r'L_1 \parallel L_2')}، يشكّل مسار منكسر زاوية {m('38^\\circ')} مع {m('L_1')} وزاوية {m('47^\\circ')} مع {m('L_2')}. ما قياس زاوية الرأس الوسطى بالدرجات؟",
         85, [95, 75, 9], "Auxiliary parallel through bend splits θ into 38° + 47° = 85°", svg_parallel_zigzag("38°", "?°", "47°")),
        (f"In a zigzag between parallel lines {m(r'L_1 \parallel L_2')}, the top angle is {m('42^\\circ')} and the middle bend angle is {m('96^\\circ')}. What is the bottom acute angle with {m('L_2')} in degrees?",
         f"في مسار منكسر بين متوازيين، الزاوية العلوية {m('42^\\circ')} وزاوية الانكسار الوسطى {m('96^\\circ')}. ما قياس الزاوية السفلية مع {m('L_2')} بالدرجات؟",
         54, [48, 58, 42], "96° − 42° = 54°", svg_parallel_zigzag("42°", "96°", "?°")),
        (f"Two exterior angles of a triangle measure {m('115^\\circ')} and {m('130^\\circ')}. What is the measure of the **third interior** angle of the triangle in degrees?",
         f"قياسا زاويتين خارجيتين لمثلث هما {m('115^\\circ')} و{m('130^\\circ')}. ما قياس **الزاوية الداخلية الثالثة** للمثلث بالدرجات؟",
         65, [115, 55, 75], "Third exterior = 360° − (115° + 130°) = 115° ⇒ third interior = 180° − 115° = 65°", svg_g9_parallel_transversal("?°", "50°", "ext_tri", "115°")),
        (f"In isosceles {m(r'\triangle ABC')} with {m('AB = AC')}, an exterior angle at base vertex {m('C')} measures {m('128^\\circ')}. What is the vertex angle {m(r'\angle A')} in degrees?",
         f"في المثلث متطابق الضلعين {m('ABC')} حيث {m('AB = AC')}، قياس الزاوية الخارجية عند الرأس {m('C')} يساوي {m('128^\\circ')}. ما قياس زاوية الرأس {m(r'\angle A')} بالدرجات؟",
         76, [52, 64, 74], "∠C = 180° − 128° = 52° = ∠B ⇒ ∠A = 180° − 104° = 76°", svg_g9_parallel_transversal("52°", "?°", "ext_tri", "128°")),
        (f"Parallel lines {m(r'L_1 \parallel L_2')} are cut by two transversals intersecting on {m('L_1')} at {m('90^\\circ')}. If one transversal makes a {m('34^\\circ')} interior angle with {m('L_2')}, what acute interior angle does the other transversal make with {m('L_2')}?",
         f"يتقاطع قاطعان متعامدان ({m('90^\\circ')}) على المستقيم {m('L_1')} الموازي لـ {m('L_2')}. إذا صنع أحدهما زاوية داخلية {m('34^\\circ')} مع {m('L_2')}، فما الزاوية الداخلية الحادة التي يصنعها القاطع الآخر مع {m('L_2')}؟",
         56, [34, 66, 46], "Right triangle between L₁ and L₂: 180° − 90° − 34° = 56°", svg_g9_parallel_transversal("90°", "34°", "alt_int")),
    ]
    for q_en, q_ar, ans, dists, note, diag in ang_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-05",
            q_en, q_ar, ans, dists,
            "Draw an auxiliary parallel through any zigzag vertex, or use exterior sum = 360°!",
            "ارسم مستقيماً مساعداً موازياً عند رأس الزاوية المنكسرة، أو استخدم مجموع الزوايا الخارجية = 360°!",
            "Combine parallel-line alternate angles with triangle angle sums.",
            [f"{m(note)}."],
            "All angle sums verified.",
            "نربط التبادل الداخلي بمجموع زوايا المثلث.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))
    return qs


def _gen_geo_06(start_idx: int) -> list[dict]:
    """G9-GEO-06: Polygon interior/exterior angle sums & regular polygon sides."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Interior sums & regular angles
    poly_easy = [
        (5, "pentagon", "المضلع الخماسي", "sum_int", 540, [360, 720, 600]),
        (7, "heptagon", "المضلع السباعي", "sum_int", 900, [720, 1080, 1260]),
        (10, "decagon", "المضلع العشاري", "sum_int", 1440, [1800, 1260, 1620]),
        (8, "regular octagon", "الثماني المنتظم", "ext_one", 45, [40, 60, 135]),
        (6, "regular hexagon", "السداسي المنتظم", "int_one", 120, [60, 108, 135]),
    ]
    for n, nm_en, nm_ar, mode, ans, dists in poly_easy:
        qid = _qid(cur); cur += 1
        if mode == "sum_int":
            q_en = f"What is the sum of the interior angles of a convex {nm_en} ({m(f'n = {n}')}) in degrees?"
            q_ar = f"ما مجموع قياسات الزوايا الداخلية في {nm_ar} المحدب ({m(f'n = {n}')}) بالدرجات؟"
            note = f"({n} − 2) × 180° = {ans}°"
        elif mode == "ext_one":
            q_en = f"What is the measure of one **exterior** angle of a {nm_en} in degrees?"
            q_ar = f"ما قياس الزاوية **الخارجية** الواحدة في {nm_ar} بالدرجات؟"
            note = f"360° ÷ {n} = {ans}°"
        else:
            q_en = f"What is the measure of one **interior** angle of a {nm_en} in degrees?"
            q_ar = f"ما قياس الزاوية **الداخلية** الواحدة في {nm_ar} بالدرجات؟"
            note = f"180° − (360° ÷ {n}) = {ans}°"
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-06",
            q_en, q_ar, ans, dists,
            "Use S = (n − 2) × 180° and e = 360° / n.",
            "استخدم القانون (n − 2) × 180° للمجموع، و360° ÷ n للزاوية الخارجية.",
            "Apply polygon angle formulas.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق قانون زوايا المضلع مباشرة.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_regular_polygon(min(n, 9)),
        ))

    # Medium 6-10: Sides from sum, regular 10/12-gon interior, missing angle of pentagon
    poly_med = [
        (f"The sum of the interior angles of a convex polygon is {m('1{,}080^\\circ')}. How many sides does it have?",
         f"مضلع محدب مجموع قياسات زواياه الداخلية {m('1{,}080^\\circ')}. ما عدد أضلاعه؟",
         8, [6, 7, 10], "(n − 2) × 180 = 1080 ⇒ n − 2 = 6 ⇒ n = 8", 8),
        (f"The sum of the interior angles of a convex polygon is {m('1{,}800^\\circ')}. How many sides does it have?",
         f"مضلع محدب مجموع زواياه الداخلية {m('1{,}800^\\circ')}. كم ضلعاً له؟",
         12, [10, 11, 14], "1800 ÷ 180 + 2 = 10 + 2 = 12", 8),
        (f"What is the measure of each interior angle of a regular {m('12')}-gon (dodecagon) in degrees?",
         f"ما قياس كل زاوية داخلية في مضلع منتظم ذي {m('12')} ضلعاً بالدرجات؟",
         150, [144, 140, 160], "180° − 360°/12 = 180° − 30° = 150°", 8),
        (f"Each interior angle of a regular polygon is {m('144^\\circ')}. How many sides does the polygon have?",
         f"قياس كل زاوية داخلية في مضلع منتظم {m('144^\\circ')}. فما عدد أضلاعه؟",
         10, [8, 9, 12], "e = 180° − 144° = 36° ⇒ n = 360° / 36° = 10", 9),
        (f"Four interior angles of a convex pentagon measure {m('100^\\circ, 115^\\circ, 95^\\circ,')} and {m('120^\\circ')}. What is the fifth interior angle in degrees?",
         f"أربع زوايا داخلية في خماسي محدب قياساتها {m('100^\\circ, 115^\\circ, 95^\\circ, 120^\\circ')}. ما قياس الزاوية الخامسة بالدرجات؟",
         110, [105, 130, 90], "540° − (100 + 115 + 95 + 120)° = 540° − 430° = 110°", 5),
    ]
    for q_en, q_ar, ans, dists, note, npoly in poly_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-06",
            q_en, q_ar, ans, dists,
            "Remember to add 2 after dividing interior sum by 180°, or use n = 360° / (180° − I)!",
            "تذكّر إضافة 2 بعد قسمة مجموع الزوايا الداخلية على 180°، أو استخدم الزاوية الخارجية المكملة!",
            "Invert the interior/exterior polygon formula.",
            [f"{m(note)}."],
            "Verified.",
            "نعوّض في قانون المضلع ونحل المعادلة.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_regular_polygon(npoly),
        ))

    # Hard 11-15: Interior = k * exterior, tiling gap angle, algebraic quadrilateral, diagonals
    poly_hard = [
        (f"In a regular polygon, each interior angle is **3 times** each exterior angle. How many sides does the polygon have?",
         f"في مضلع منتظم، قياس الزاوية الداخلية يساوي **3 أمثال** قياس الزاوية الخارجية. ما عدد أضلاع هذا المضلع؟",
         8, [6, 9, 10], "3e + e = 180° ⇒ e = 45° ⇒ n = 360° / 45° = 8"),
        (f"In a regular polygon, each interior angle is **5 times** each exterior angle. How many sides does the polygon have?",
         f"في مضلع منتظم، قياس كل زاوية داخلية يساوي **5 أمثال** قياس زاويته الخارجية. كم عدد أضلاعه؟",
         12, [10, 15, 9], "6e = 180° ⇒ e = 30° ⇒ n = 360° / 30° = 12"),
        (f"In a Diriyah mosaic, a regular hexagon and a square share one edge without overlapping. What is the exterior gap angle (less than {m('180^\\circ')}) between their adjacent outer sides at a shared vertex?",
         f"في فسيفساء هندسية، يشترك سداسي منتظم ومربع في ضلع واحد دون تداخل. ما قياس الزاوية الخارجية المحصورة بين ضلعيهما المتجاورين عند الرأس المشترك؟",
         150, [120, 135, 160], "Full turn 360° − 120° − 90° = 150°"),
        (f"The four interior angles of a convex quadrilateral are {m('x^\\circ, (x+20)^\\circ, (2x-10)^\\circ,')} and {m('(2x-10)^\\circ')}. What is the **largest** angle in degrees?",
         f"زوايا رباعي محدب هي {m('x^\\circ, (x+20)^\\circ, (2x-10)^\\circ, (2x-10)^\\circ')}. ما قياس **أكبر** زاوية فيه بالدرجات؟",
         110, [60, 80, 120], "6x = 360 ⇒ x = 60 ⇒ angles 60°, 80°, 110°, 110° ⇒ largest 110°"),
        (f"A regular polygon has each exterior angle equal to {m('40^\\circ')}. How many **diagonals** {m(r'\frac{n(n-3)}{2}')} does this polygon have?",
         f"مضلع منتظم قياس كل زاوية خارجية فيه {m('40^\\circ')}. كم **قطراً** {m(r'\frac{n(n-3)}{2}')} لهذا المضلع؟",
         27, [9, 36, 20], "n = 360/40 = 9 ⇒ diagonals = 9 × 6 / 2 = 27"),
    ]
    for q_en, q_ar, ans, dists, note in poly_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-06",
            q_en, q_ar, ans, dists,
            "At any vertex I + e = 180°, and around a mosaic point angles sum to 360°!",
            "عند أي رأس يكون مجموع الداخلية والخارجية 180°، وحول أي نقطة تلتقي عندها المضلعات المجموع 360°!",
            "Combine supplementary vertex relations with 360° exterior sums.",
            [f"{m(note)}."],
            "Verified.",
            "نربط تكامل الزاويتين الداخلية والخارجية بمجموع الزوايا حول نقطة.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_regular_polygon(8, [(0, 3), (1, 5)]),
        ))
    return qs


def _gen_geo_07(start_idx: int) -> list[dict]:
    """G9-GEO-07: Similar triangles (linear ratio k vs area ratio k^2, shadows & midsegments)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Missing side, midsegment, perimeter scaling
    sim_easy = [
        (f"Triangles {m('ABC')} and {m('DEF')} are similar with {m('AB = 6')} cm, {m('BC = 9')} cm, and {m('DE = 10')} cm. What is {m('EF')} in cm?",
         f"المثلثان {m('ABC')} و{m('DEF')} متشابهان، وفيهما {m('AB = 6')} سم و{m('BC = 9')} سم و{m('DE = 10')} سم. ما طول {m('EF')} بالسنتيمتر؟",
         15, [13, 12, 18], "6 / 10 = 9 / EF ⇒ EF = 90 / 6 = 15", svg_g9_similar_triangles("6", "9", "10", "?")),
        (f"In {m(r'\triangle ABC')}, segment {m('MN')} joins the midpoints of {m('AB')} and {m('AC')}. If {m('BC = 26')} cm, what is {m('MN')} in cm?",
         f"في المثلث {m('ABC')}، القطعة المنصّفة {m('MN')} تصل بين منتصفي {m('AB')} و{m('AC')}. إذا كان {m('BC = 26')} سم، فما طول {m('MN')} بالسنتيمتر؟",
         13, [26, 52, 12], "Midsegment MN = ½ BC = 13", svg_g9_similar_triangles("1", "MN = ?", "2", "26", nested=True)),
        (f"Two similar triangles have scale factor {m('k = 3')}. If the smaller triangle has perimeter {m('18')} cm, what is the perimeter of the larger triangle in cm?",
         f"مثلثان متشابهان معامل التشابه بينهما {m('k = 3')}. إذا كان محيط الأصغر {m('18')} سم، فما محيط الأكبر بالسنتيمتر؟",
         54, [162, 27, 36], "Perimeter scales linearly by k = 3 ⇒ 3 × 18 = 54", svg_g9_similar_triangles("1", "P = 18", "3", "P = ?")),
        (f"A {m('2')}-m vertical post casts a {m('3')}-m shadow at the same moment a palm tree casts a {m('12')}-m shadow. How tall is the palm tree in meters?",
         f"عمود رأسي طوله {m('2')} م يصنع ظلاً طوله {m('3')} م في اللحظة نفسها التي تصنع فيها نخلة ظلاً طوله {m('12')} م. ما ارتفاع النخلة بالأمتار؟",
         8, [18, 6, 9], "h / 12 = 2 / 3 ⇒ h = 8 m", svg_g9_similar_triangles("2 m", "3 m", "h = ?", "12 m")),
        (f"If two similar triangles have side ratio {m('3 : 4')}, what is the ratio of their **areas** (smaller to larger)?",
         f"إذا كانت نسبة التشابه بين ضلعين متناظرين في مثلثين متشابهين {m('3 : 4')}، فما نسبة **مساحة** الأصغر إلى الأكبر؟",
         Fraction(9, 16), [Fraction(3, 4), Fraction(6, 8), Fraction(27, 64)], "(3/4)² = 9/16", svg_g9_similar_triangles("3", "A₁", "4", "A₂")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sim_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-07",
            q_en, q_ar, ans, dists,
            "Perimeters and sides scale by k, whereas areas scale by k²!",
            "الأضلاع والمحيطات تتناسب مع k، أما المساحات فتتناسب مع المربع k²!",
            "Apply linear or area similarity proportions.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق تناسب التشابه.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Medium 6-10: Nested parallel DE || BC, shadow heights, area calculation
    sim_med = [
        (f"In {m(r'\triangle ABC')}, {m('DE \\parallel BC')} with {m('D')} on {m('AB')} and {m('E')} on {m('AC')}. If {m('AD = 6')} cm, {m('DB = 3')} cm, and {m('BC = 15')} cm, what is {m('DE')} in cm?",
         f"في المثلث {m('ABC')}، {m('DE \\parallel BC')} حيث {m('AD = 6')} سم و{m('DB = 3')} سم و{m('BC = 15')} سم. ما طول {m('DE')} بالسنتيمتر؟",
         10, [7.5, 12, 9], "AB = 6 + 3 = 9 ⇒ DE / 15 = 6 / 9 ⇒ DE = 10", svg_g9_similar_triangles("6", "DE = ?", "9", "15", nested=True)),
        (f"Two similar triangles have areas {m('25\\text{ cm}^2')} and {m('64\\text{ cm}^2')}. If a side of the smaller triangle is {m('15')} cm, what is the corresponding side of the larger triangle in cm?",
         f"مثلثان متشابهان مساحتاهما {m('25')} سم² و{m('64')} سم². إذا كان طول ضلع في الأصغر {m('15')} سم، فما طول نظيره في الأكبر بالسنتيمتر؟",
         24, [38.4, 20, 32], "k = √(64/25) = 8/5 ⇒ 15 × (8/5) = 24", svg_g9_similar_triangles("15", "A=25", "?", "A=64")),
        (f"At Qiddiya, a {m('1.8')}-m engineer stands {m('8')} m from a mirror on flat ground, seeing the top of a tower {m('40')} m beyond the mirror. What is the tower's height in meters?",
         f"يقف مهندس طوله {m('1.8')} م على بُعد {m('8')} م من مرآة أرضية فيرى قمة برج يبعد {m('40')} م خلف المرآة. ما ارتفاع البرج بالأمتار؟",
         9, [7.2, 10.8, 12], "h / 40 = 1.8 / 8 ⇒ h = 1.8 × 5 = 9 m", svg_g9_similar_triangles("1.8 m", "8 m", "h = ?", "40 m")),
        (f"Midsegment {m('MN')} of {m(r'\triangle ABC')} has length {m('(2x + 3)')} cm, while parallel base {m('BC')} has length {m('(5x - 2)')} cm. What is {m('x')}?",
         f"في المثلث {m('ABC')}، طول القطعة المنصّفة {m('MN')} هو {m('(2x + 3)')} سم وطول الضلع الموازي {m('BC')} هو {m('(5x - 2)')} سم. ما قيمة {m('x')}؟",
         8, [5, 6, 4], "2(2x + 3) = 5x − 2 ⇒ 4x + 6 = 5x − 2 ⇒ x = 8", svg_g9_similar_triangles("1", "2x+3", "2", "5x−2", nested=True)),
        (f"Two similar triangles have perimeters {m('24')} cm and {m('36')} cm. If the larger triangle has area {m('54\\text{ cm}^2')}, what is the smaller triangle's area in {m(r'\text{cm}^2')}?",
         f"مثلثان متشابهان محيطاهما {m('24')} سم و{m('36')} سم. إذا كانت مساحة الأكبر {m('54')} سم²، فما مساحة الأصغر بالـ سم²؟",
         24, [36, 18, 27], "Side ratio = 24/36 = 2/3 ⇒ Area ratio = 4/9 ⇒ (4/9) × 54 = 24", svg_g9_similar_triangles("P=24", "A=?", "P=36", "A=54")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sim_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-07",
            q_en, q_ar, ans, dists,
            "In nested triangles, remember the full side is AD + DB, NOT DB alone!",
            "في المثلثات المتداخلة، تذكّر أن ضلع المثلث الكبير هو المجموع AD + DB وليس DB وحده!",
            "Set up exact full-side proportions or take square roots of area ratios.",
            [f"{m(note)}."],
            "Verified.",
            "نستخدم النسبة الكاملة للأضلاع أو جذر نسبة المساحتين.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Hard 11-15: Trapezoid band area in nested triangle, medial triangle, lamp-post shadow
    sim_hard = [
        (f"In {m(r'\triangle ABC')} of area {m('50\\text{ cm}^2')}, {m('DE \\parallel BC')} with {m('AD : DB = 2 : 3')}. What is the area (in {m(r'\text{cm}^2')}) of **trapezoid** {m('BCED')}?",
         f"في المثلث {m('ABC')} الذي مساحته {m('50')} سم²، {m('DE \\parallel BC')} بحيث {m('AD : DB = 2 : 3')}. ما مساحة **شبه المنحرف** {m('BCED')} بالـ سم²؟",
         42, [8, 30, 32], "AD / AB = 2 / 5 ⇒ Area(ADE) = (4/25)(50) = 8 ⇒ Trapezoid = 50 − 8 = 42", svg_g9_similar_triangles("2", "ADE", "5", "ABC=50", nested=True)),
        (f"Joining the three side midpoints of {m(r'\triangle ABC')} forms medial triangle {m('DEF')}. If {m(r'\text{Area}(\triangle ABC) = 68\text{ cm}^2')}, what is {m(r'\text{Area}(\triangle DEF)')} in {m(r'\text{cm}^2')}?",
         f"وُصلت منتصفات أضلاع المثلث {m('ABC')} الثلاثة لتكوين المثلث الأوسط {m('DEF')}. إذا كانت مساحة {m('ABC')} تساوي {m('68')} سم²، فما مساحة {m('DEF')} بالـ سم²؟",
         17, [34, 22, 16], "k = 1/2 ⇒ Area(DEF) = (1/4) × 68 = 17", svg_g9_similar_triangles("1", "DEF=?", "2", "ABC=68", nested=True)),
        (f"A {m('6')}-m streetlamp stands behind a {m('1.5')}-m student who is {m('9')} m away from the lamp's base. How long (in m) is the student's shadow on the ground?",
         f"عمود إنارة ارتفاعه {m('6')} م يقف على بُعد {m('9')} م خلف طالب طوله {m('1.5')} م. ما طول ظل الطالب على الأرض بالأمتار؟",
         3, [2.25, 4.5, 6], "s / (s + 9) = 1.5 / 6 = 1/4 ⇒ 4s = s + 9 ⇒ 3s = 9 ⇒ s = 3 m", svg_g9_similar_triangles("1.5 m", "s = ?", "6 m", "s + 9", nested=True)),
        (f"In right {m(r'\triangle ABC')} ({m(r'\angle C = 90^\circ')}), altitude {m('CD')} to hypotenuse {m('AB')} creates segments {m('AD = 4')} cm and {m('DB = 9')} cm. By right-triangle similarity, what is {m('CD')} in cm?",
         f"في المثلث القائم {m('ABC')} عند {m('C')}، العمود {m('CD')} النازل على الوتر يقسمه إلى {m('AD = 4')} سم و{m('DB = 9')} سم. بتشابه المثلثات القائمة، ما طول {m('CD')} بالسنتيمتر؟",
         6, [5, 6.5, 13], "△ACD ~ △CBD ⇒ CD / 4 = 9 / CD ⇒ CD² = 36 ⇒ CD = 6", svg_g9_right_triangle("CD = ?", "9 cm", "hyp")),
        (f"Chords {m('AB')} and {m('CD')} intersect at {m('P')} inside a circle, forming similar triangles {m(r'\triangle APC \sim \triangle DPB')}. If {m('AP = 6')}, {m('PB = 8')}, and {m('CP = 4')}, what is {m('PD')}?",
         f"يتقاطع الوتران {m('AB')} و{m('CD')} داخل دائرة في {m('P')} فيتكون مثلثان متشابهان. إذا كان {m('AP = 6')} و{m('PB = 8')} و{m('CP = 4')}، فما طول {m('PD')}؟",
         12, [10, 3, 14], "AP · PB = CP · PD ⇒ 6 × 8 = 4 × PD ⇒ PD = 12", svg_g9_similar_triangles("6", "4", "PD=?", "8")),
    ]
    for q_en, q_ar, ans, dists, note, diag in sim_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-07",
            q_en, q_ar, ans, dists,
            "Set up full-triangle ratios (s / (s + 9), AD / (AD + DB), or geometric mean CD² = AD·DB)!",
            "اكتب نسبة التشابه للمثلث الكامل مثل AD/(AD+DB) أو s/(s+9)!",
            "Exploit triangle similarity ratios and area subtraction.",
            [f"{m(note)}."],
            "Verified.",
            "نستنتج التناسب الدقيق من تشابه المثلثين.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))
    return qs


def _gen_geo_08(start_idx: int) -> list[dict]:
    """G9-GEO-08: Coordinate transformations (translations, reflections, rotations & dilations)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Single coordinate transformation
    tr_easy = [
        (f"Point {m('A(2, -3)')} is translated {m('4')} units right and {m('5')} units up. What are the coordinates of {m(r'A^\prime')}?",
         f"أُزيحت النقطة {m('A(2, -3)')} بمقدار {m('4')} وحدات يميناً و{m('5')} وحدات للأعلى. ما إحداثيا صورتها {m(r'A^\prime')}؟",
         "(6, 2)", ["(-2, 2)", "(6, -8)", "(7, 1)"], "(2+4, −3+5) = (6, 2)", [(2, -3, "A"), (6, 2, "A'")]),
        (f"What is the image of {m('B(-5, 4)')} after reflection across the **{m('x')}-axis**?",
         f"ما صورة النقطة {m('B(-5, 4)')} بالانعكاس حول **محور السينات** {m('x')}؟",
         "(-5, -4)", ["(5, 4)", "(5, -4)", "(4, -5)"], "(x, y) → (x, −y) = (−5, −4)", [(-5, 4, "B"), (-5, -4, "B'")]),
        (f"What is the image of {m('C(3, -6)')} after reflection across the **{m('y')}-axis**?",
         f"ما صورة النقطة {m('C(3, -6)')} بالانعكاس حول **محور الصادات** {m('y')}؟",
         "(-3, -6)", ["(3, 6)", "(-3, 6)", "(-6, 3)"], "(x, y) → (−x, y) = (−3, −6)", [(3, -6, "C"), (-3, -6, "C'")]),
        (f"What is the image of {m('D(4, -2)')} after a {m('180^\\circ')} rotation about the origin?",
         f"ما صورة النقطة {m('D(4, -2)')} بدوران زاويته {m('180^\\circ')} حول نقطة الأصل؟",
         "(-4, 2)", ["(2, -4)", "(-4, -2)", "(4, 2)"], "(x, y) → (−x, −y) = (−4, 2)", [(4, -2, "D"), (-4, 2, "D'")]),
        (f"What is the image of {m('E(-2, 3)')} under a dilation centered at the origin with scale factor {m('k = 3')}?",
         f"ما صورة النقطة {m('E(-2, 3)')} بتمدد مركزه نقطة الأصل ومعامله {m('k = 3')}؟",
         "(-6, 9)", ["(1, 6)", "(-6, 3)", "(6, -9)"], "(3x, 3y) = (−6, 9)", [(-2, 3, "E"), (-6, 9, "E'")]),
    ]
    for q_en, q_ar, ans, dists, note, pts in tr_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Easy", "G9-GEO-08",
            q_en, q_ar, ans, dists,
            "Apply the coordinate mapping rule directly to (x, y).",
            "طبّق قاعدة التحويل الإحداثي مباشرة على (x, y).",
            "Use exact coordinate transformation rules.",
            [f"{m(note)}."],
            "Quadrant check passed.",
            "نطبّق قاعدة التحويل الهندسي.",
            [f"{m(note)}."],
            "موقع الربع الإحداثي صحيح.",
            diagram_en=svg_nafes_coordinate_line(pts, max_coord=9),
        ))

    # Medium 6-10: Reflection y=x, 90° CCW rotation, translation vector, fractional dilation, 90° CW
    tr_med = [
        (f"What is the image of {m('P(-3, 7)')} after reflection across the line {m('y = x')}?",
         f"ما صورة النقطة {m('P(-3, 7)')} بالانعكاس حول المستقيم {m('y = x')}؟",
         "(7, -3)", ["(3, -7)", "(-7, 3)", "(-3, -7)"], "(x, y) → (y, x) = (7, −3)", [(-3, 7, "P"), (7, -3, "P'")]),
        (f"Point {m('Q(5, 2)')} is rotated {m('90^\\circ')} **counterclockwise** about the origin. What are the coordinates of {m(r'Q^\prime')}?",
         f"دُوّرت النقطة {m('Q(5, 2)')} بزاوية {m('90^\\circ')} **عكس عقارب الساعة** حول نقطة الأصل. ما إحداثيا {m(r'Q^\prime')}؟",
         "(-2, 5)", ["(2, -5)", "(-5, -2)", "(2, 5)"], "(x, y) → (−y, x) = (−2, 5)", [(5, 2, "Q"), (-2, 5, "Q'")]),
        (f"A translation maps {m('A(-2, 5)')} to {m(r'A^\prime(3, 1)')}. What is the image of {m('B(0, -2)')} under the **same** translation?",
         f"انسحاب ينقل النقطة {m('A(-2, 5)')} إلى {m(r'A^\prime(3, 1)')}. ما صورة النقطة {m('B(0, -2)')} بالانسحاب **نفسه**؟",
         "(5, -6)", ["(-5, 2)", "(3, -6)", "(5, 2)"], "Vector = (+5, −4) ⇒ B' = (0+5, −2−4) = (5, −6)", [(-2, 5, "A"), (3, 1, "A'"), (5, -6, "B'")]),
        (f"Segment {m('AB')} of length {m('12')} units undergoes a dilation with scale factor {m('k = \\frac{3}{4}')}. What is the length of image {m(r'A^\prime B^\prime')}?",
         f"قطعة مستقيمة {m('AB')} طولها {m('12')} وحدة خضعت لتمدد معامله {m('k = \\frac{3}{4}')}. ما طول صورتها {m(r'A^\prime B^\prime')}؟",
         9, [16, 8, 6], "12 × (3/4) = 9", [(0, 0, "O"), (4, 0, "A'"), (6, 0, "A")]),
        (f"Point {m('R(3, -4)')} is rotated {m('90^\\circ')} **clockwise** about the origin. What are the coordinates of {m(r'R^\prime')}?",
         f"دُوّرت النقطة {m('R(3, -4)')} بزاوية {m('90^\\circ')} **مع عقارب الساعة** حول نقطة الأصل. ما إحداثيا {m(r'R^\prime')}؟",
         "(-4, -3)", ["(4, 3)", "(-3, 4)", "(4, -3)"], "(x, y) → (y, −x) = (−4, −3)", [(3, -4, "R"), (-4, -3, "R'")]),
    ]
    for q_en, q_ar, ans, dists, note, pts in tr_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Medium", "G9-GEO-08",
            q_en, q_ar, ans, dists,
            "90° CCW maps (x, y) → (−y, x), 90° CW maps (x, y) → (y, −x), and y = x swaps coordinates!",
            "دوران 90° عكس الساعة يعطي (−y, x)، ومع الساعة (y, −x)، والانعكاس حول y=x يبدل الإحداثيين!",
            "Apply coordinate transformation rules step-by-step.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق قاعدة الدوران أو الانعكاس أو الانسحاب.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_nafes_coordinate_line(pts, max_coord=8),
        ))

    # Hard 11-15: Reflection across x = k, composite transformations, reverse pre-image, dilation area
    tr_hard = [
        (f"Point {m('P(-1, 4)')} is reflected across the vertical line {m('x = 3')}. What is the {m('x')}-coordinate of its image {m(r'P^\prime')}?",
         f"انعكست النقطة {m('P(-1, 4)')} حول المستقيم الرأسي {m('x = 3')}. ما الإحداثي السيني لصورتها {m(r'P^\prime')}؟",
         7, [1, 5, -7], "Midpoint x is 3: (−1 + x') / 2 = 3 ⇒ x' = 7"),
        (f"Triangle {m('ABC')} has area {m('10')} square units. After a dilation centered at the origin with scale factor {m('k = 3')}, what is the **area** of {m(r'\triangle A^\prime B^\prime C^\prime')}?",
         f"مساحة المثلث {m('ABC')} تساوي {m('10')} وحدات مربعة. بعد تمدد معامله {m('k = 3')}، ما **مساحة** المثلث الصورة {m(r'A^\prime B^\prime C^\prime')}؟",
         90, [30, 60, 270], "Area scales by k² = 3² = 9 ⇒ 9 × 10 = 90"),
        (f"Point {m('M(x, y)')} is translated by {m('(x - 3, y + 5)')} and then reflected across the {m('x')}-axis to land at {m('(4, -2)')}. What is {m('x + y')} for the **original** point {m('M')}?",
         f"أُزيحت النقطة {m('M(x, y)')} وفق القاعدة {m('(x - 3, y + 5)')} ثم انعكست حول محور السينات لتستقر عند {m('(4, -2)')}. ما قيمة {m('x + y')} للنقطة **الأصلية** {m('M')}؟",
         4, [6, 2, 10], "Before x-axis reflection: (4, 2); x − 3 = 4 ⇒ x = 7; y + 5 = 2 ⇒ y = −3 ⇒ x + y = 4"),
        (f"Point {m('K(2, 5)')} is rotated {m('90^\\circ')} counterclockwise about the origin and then reflected across the {m('y')}-axis. What is the product of the coordinates of the final image?",
         f"دُوّرت النقطة {m('K(2, 5)')} بزاوية {m('90^\\circ')} عكس عقارب الساعة حول الأصل ثم انعكست حول محور الصادات. ما حاصل ضرب إحداثيي الصورة النهائية؟",
         10, [-10, 7, -7], "(2, 5) → (−5, 2) → (5, 2) ⇒ 5 × 2 = 10"),
        (f"Reflecting a point across the {m('x')}-axis and then immediately across the {m('y')}-axis is equivalent to a single rotation about the origin of how many degrees?",
         f"انعكاس نقطة حول محور السينات متبوعاً مباشرة بانعكاس حول محور الصادات يكافئ دوراناً مفرداً حول نقطة الأصل بزاوية كم درجة؟",
         180, [90, 270, 360], "(x, y) → (x, −y) → (−x, −y), which is a 180° rotation"),
    ]
    for q_en, q_ar, ans, dists, note in tr_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Geometry", "Hard", "G9-GEO-08",
            q_en, q_ar, ans, dists,
            "Work backward in reverse order for pre-images, and remember dilations multiply area by k²!",
            "اعكس ترتيب التحويلات عند الرجوع للنقطة الأصلية، وتذكّر أن التمدد يضرب المساحة في k²!",
            "Compose coordinate mappings or invert step-by-step.",
            [f"{m(note)}."],
            "Forward check reproduces the final image.",
            "نركّب التحويلات خطوة بخطوة أو نعكسها.",
            [f"{m(note)}."],
            "التطبيق الأمامي يعيد نفس الصورة النهائية.",
            diagram_en=svg_nafes_coordinate_line([(-1, 4, "P"), (3, 4, "x=3"), (7, 4, "P'")], max_coord=8),
        ))
    return qs


# ==============================================================================
# UNIT 3.6 (G9-DAT-01 .. G9-DAT-04): Box Plots, Histograms/Tables, P&C & Prob.
# ==============================================================================

def _gen_dat_01(start_idx: int) -> list[dict]:
    """G9-DAT-01: Box-and-whisker plots: median, Q1, Q3, IQR, range & quartile %."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Reading 5-number summary, Range & IQR
    bp_easy = [
        (32, 46, 58, 71, 88, "IQR", "المدى الربيعي", 25, [56, 12, 13]),
        (15, 28, 39, 52, 65, "Range", "المدى الكلي", 50, [24, 39, 37]),
        (40, 54, 67, 79, 92, "Median", "الوسيط", 67, [54, 79, 66]),
        (10, 22, 35, 48, 60, "Q3", "الربيع الأعلى", 48, [22, 35, 26]),
        (50, 62, 70, 84, 95, "IQR", "المدى الربيعي", 22, [45, 14, 70]),
    ]
    for mn, q1, med, q3, mx, ask_en, ask_ar, ans, dists in bp_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Easy", "G9-DAT-01",
            f"The box-and-whisker plot shows scores with Min {m(str(mn))}, {m(f'Q_1 = {q1}')}, Median {m(str(med))}, {m(f'Q_3 = {q3}')}, and Max {m(str(mx))}. What is the **{ask_en}**?",
            f"يمثّل الصندوق وطرفاه درجات حدّها الأدنى {m(str(mn))} و{m(f'Q_1 = {q1}')} والوسيط {m(str(med))} و{m(f'Q_3 = {q3}')} والأعلى {m(str(mx))}. ما قيمة **{ask_ar}**؟",
            ans, dists,
            "Remember IQR = Q₃ − Q₁ and Range = Max − Min.",
            "تذكّر أن المدى الربيعي Q₃ − Q₁ والمدى الكلي Max − Min.",
            "Read the five-number summary directly from the box plot.",
            [f"From the plotted summary, the requested statistic is {m(str(ans))}."],
            "Verified directly against the five-number summary.",
            "نقرأ القيمة مباشرة من الملخص الخماسي.",
            [f"القيمة المطلوبة من الرسم تساوي {m(str(ans))}."],
            "متحقق.",
            diagram_en=svg_nafes_box_plot(mn, q1, med, q3, mx, f"Summary: {mn}, {q1}, {med}, {q3}, {mx}"),
        ))

    # Medium 6-10: Quartile percentages & computing IQR from ordered data
    bp_med = [
        (f"In a Grade 9 cohort of {m('80')} students, scores have {m('Q_1 = 60')}, Median {m('72')}, and {m('Q_3 = 84')}. Approximately how many students scored **at least** {m('60')}?",
         f"في دفعة من {m('80')} طالباً بالصف الثالث المتوسط، كان {m('Q_1 = 60')} والوسيط {m('72')} و{m('Q_3 = 84')}. كم طالباً تقريباً حصل على {m('60')} درجة **فأكثر**؟",
         60, [20, 40, 64], "Above Q₁ lies 75% of data: 0.75 × 80 = 60", svg_nafes_box_plot(42, 60, 72, 84, 96, "N = 80 students")),
        (f"For {m('120')} tested batteries, lifespans have Min {m('18')}, {m('Q_1 = 24')}, Median {m('30')}, {m('Q_3 = 38')}, Max {m('46')} hours. About how many batteries lasted between {m('24')} and {m('38')} hours?",
         f"لـ {m('120')} بطارية مختبرة، كان {m('Q_1 = 24')} و{m('Q_3 = 38')}. كم بطارية تقريباً استمرت بين {m('24')} و{m('38')} ساعة؟",
         60, [30, 90, 48], "Box [Q₁, Q₃] holds middle 50%: 0.50 × 120 = 60", svg_nafes_box_plot(18, 24, 30, 38, 46, "N = 120 batteries")),
        (f"What is the interquartile range ({m(r'\text{IQR}')}) of the ordered dataset {m('12, 15, 18, 22, 25, 29, 34')}?",
         f"ما المدى الربيعي ({m(r'\text{IQR}')}) للبيانات المرتبة {m('12, 15, 18, 22, 25, 29, 34')}؟",
         14, [22, 11, 17], "Median = 22; lower half {12,15,18} ⇒ Q₁ = 15; upper half {25,29,34} ⇒ Q₃ = 29 ⇒ IQR = 14", svg_nafes_box_plot(12, 15, 22, 29, 34, "7-value dataset")),
        (f"What is the interquartile range ({m(r'\text{IQR}')}) of the {m('9')} temperatures {m('14, 16, 17, 19, 21, 24, 26, 28, 33')}?",
         f"ما المدى الربيعي لدرجات الحرارة التسع {m('14, 16, 17, 19, 21, 24, 26, 28, 33')}؟",
         10.5, [19, 9, 12], "Q₁ = (16+17)/2 = 16.5; Q₃ = (26+28)/2 = 27 ⇒ IQR = 27 − 16.5 = 10.5", svg_nafes_box_plot(14, 16.5, 21, 27, 33, "9 temperatures")),
        (f"In a box plot of {m('60')} seedlings' heights, {m('Q_3 = 45')} cm. Approximately how many seedlings are taller than {m('45')} cm?",
         f"في تمثيل بالصندوق وطرفيه لأطوال {m('60')} شتلة، كان الربيع الأعلى {m('Q_3 = 45')} سم. كم شتلة تقريباً يزيد طولها على {m('45')} سم؟",
         15, [45, 30, 20], "Top whisker above Q₃ holds 25%: 0.25 × 60 = 15", svg_nafes_box_plot(20, 31, 38, 45, 56, "N = 60 seedlings")),
    ]
    for q_en, q_ar, ans, dists, note, diag in bp_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Medium", "G9-DAT-01",
            q_en, q_ar, ans, dists,
            "Each section of a box plot represents 25% of observations!",
            "كل قسم من أقسام الصندوق وطرفيه الأربعة يمثّل 25% من البيانات!",
            "Use quartile percentages (25%, 50%, 75%) or split around the median.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق نسب الأرباع أو نحسب وسيطي النصفين الأدنى والأعلى.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Hard 11-15: Shift invariance of IQR, scale effect on IQR, upper outlier fence, missing Q1
    bp_hard = [
        (f"A Grade 9 physics test has median {m('68')} and {m(r'\text{IQR} = 16')}. If the teacher adds {m('5')} bonus points to **every** student's score, what is the new {m(r'\text{IQR}')}?",
         f"اختبار فيزياء وسيطه {m('68')} ومداه الربيعي {m('16')}. إذا أضاف المعلم {m('5')} درجات إضافية **لكل** طالب، فما قيمة المدى الربيعي الجديد؟",
         16, [21, 73, 11], "Adding 5 shifts both Q₁ and Q₃ by +5, so (Q₃+5) − (Q₁+5) = 16 (unchanged!)"),
        (f"Dataset X has {m('Q_1 = 20')} and {m('Q_3 = 34')}. If every value in X is multiplied by {m('3')}, what is the {m(r'\text{IQR}')} of the scaled dataset?",
         f"مجموعة بيانات فيها {m('Q_1 = 20')} و{m('Q_3 = 34')}. إذا ضُربت كل قيمة في {m('3')}، فما المدى الربيعي للبيانات الجديدة؟",
         42, [14, 17, 102], "Original IQR = 14; multiplying by 3 scales spread by 3 ⇒ 3 × 14 = 42"),
        (f"Using the standard outlier rule {m(r'Q_3 + 1.5 \times \text{IQR}')}, what is the upper outlier threshold for a dataset with {m('Q_1 = 56')}, Median {m('65')}, and {m('Q_3 = 76')}?",
         f"باستخدام قاعدة القيم المتطرفة العليا {m(r'Q_3 + 1.5 \times \text{IQR}')}، ما الحد الأعلى للقيم غير المتطرفة لبيانات فيها {m('Q_1 = 56')} و{m('Q_3 = 76')}؟",
         106, [96, 100, 86], "IQR = 76 − 56 = 20 ⇒ 76 + 1.5(20) = 76 + 30 = 106"),
        (f"Class A has {m('(Q_1, \\text{Med}, Q_3) = (58, 70, 82)')} and Class B has {m('(64, 75, 80)')}. By how much does Class A's {m(r'\text{IQR}')} exceed Class B's {m(r'\text{IQR}')}?",
         f"في الفصل (أ) {m('(Q_1, \\text{Med}, Q_3) = (58, 70, 82)')} وفي الفصل (ب) {m('(64, 75, 80)')}. بكم يزيد المدى الربيعي للفصل (أ) على الفصل (ب)؟",
         8, [5, 16, 24], "IQR_A = 82 − 58 = 24; IQR_B = 80 − 64 = 16 ⇒ 24 − 16 = 8"),
        (f"A symmetric box plot has range {m('44')}, minimum {m('18')}, and {m(r'\text{IQR} = 20')}. If both whiskers have equal length, what is {m('Q_3')}?",
         f"تمثيل متماثل بالصندوق وطرفيه مداه الكلي {m('44')} وحدّه الأدنى {m('18')} ومداه الربيعي {m('20')}. إذا كان الطرفان متساويي الطول، فما قيمة {m('Q_3')}؟",
         50, [40, 48, 52], "Max = 62; whiskers sum to 44 − 20 = 24 ⇒ each whisker = 12 ⇒ Q₃ = 62 − 12 = 50"),
    ]
    for q_en, q_ar, ans, dists, note in bp_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Hard", "G9-DAT-01",
            q_en, q_ar, ans, dists,
            "Adding a constant preserves spread (IQR), while multiplying by k scales spread by |k|!",
            "إضافة عدد ثابت لا تغيّر المدى الربيعي، بينما الضرب في موجب k يضرب المدى الربيعي في k!",
            "Analyze spread transformations, outlier fences, and box-plot symmetry.",
            [f"{m(note)}."],
            "Verified.",
            "نحلل خصائص التشتت والتماثل في الصندوق وطرفيه.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_nafes_box_plot(18, 30, 40, 50, 62, "Quartile Spread Analysis"),
        ))
    return qs


def _gen_dat_02(start_idx: int) -> list[dict]:
    """G9-DAT-02: Weighted means, grouped histograms & two-way contingency tables."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Histogram reading, two-way totals, basic weighted mean
    dat2_easy = [
        (f"In the histogram of daily wind speeds with bins {m('10\\text{–}20')} ({m('6')}), {m('20\\text{–}30')} ({m('11')}), {m('30\\text{–}40')} ({m('9')}), and {m('40\\text{–}50')} ({m('4')}), how many days had wind speed **at least** {m('20')} km/h?",
         f"في المدرج التكراري لسرعة الرياح للفئات {m('10\\text{–}20')} ({m('6')})، {m('20\\text{–}30')} ({m('11')})، {m('30\\text{–}40')} ({m('9')})، {m('40\\text{–}50')} ({m('4')})، كم يوماً بلغت السرعة {m('20')} كم/س **فأكثر**؟",
         24, [11, 13, 30], "11 + 9 + 4 = 24", svg_g9_histogram([("10–20", 6, "6"), ("20–30", 11, "11"), ("30–40", 9, "9"), ("40–50", 4, "4")], "Wind Speed (km/h)")),
        (f"In a histogram with bin counts {m('5, 14, 18, 13')}, what percentage of observations fall in the **last** bin ({m('13')})?",
         f"في مدرج تكراري تكرارات فئاته {m('5, 14, 18, 13')}، ما النسبة المئوية للبيانات الواقعة في الفئة **الأخيرة** ({m('13')})؟",
         26, [13, 25, 30], "Total = 50 ⇒ (13 / 50) × 100% = 26%", svg_g9_histogram([("A", 5, "5"), ("B", 14, "14"), ("C", 18, "18"), ("D", 13, "13")])),
        (f"In a two-way table of {m('100')} students, {m('34')} boys and {m('26')} girls prefer Solar Club, while {m('16')} boys and {m('24')} girls prefer Space Club. What is the **joint** relative frequency of girls who prefer Space Club?",
         f"في جدول مزدوج لـ {m('100')} طالب وطالبة، يفضّل نادي الفضاء {m('16')} طالباً و{m('24')} طالبة، ونادي الطاقة {m('34')} طالباً و{m('26')} طالبة. ما التكرار النسبي **المشترك** للطالبات المفضلات لنادي الفضاء؟",
         Fraction(6, 25), [Fraction(12, 25), Fraction(3, 5), Fraction(2, 5)], "24 / 100 = 6/25", svg_nafes_function_table(["Group", "Solar", "Space"], [["Boys", "34", "16"], ["Girls", "26", "24"]], highlight_cell=(1, 2))),
        (f"A student scores {m('80')} on quizzes (weight {m('1')}) and {m('92')} on the final exam (weight {m('3')}). What is the weighted mean score?",
         f"حصل طالب على {m('80')} في الاختبارات القصيرة (بوزن {m('1')}) و{m('92')} في الاختبار النهائي (بوزن {m('3')}). ما المتوسط المرجح لدرجته؟",
         89, [86, 88, 90], "(1×80 + 3×92) / (1 + 3) = 356 / 4 = 89", svg_nafes_function_table(["Part", "Score", "Weight"], [["Quiz", "80", "1"], ["Final", "92", "3"]])),
        (f"In a histogram of {m('40')} lab samples, three bins have counts {m('8')}, {m('15')}, and {m('x')}, and the fourth bin has {m('6')}. What is {m('x')}?",
         f"في مدرج تكراري لـ {m('40')} عينة مختبرية، تكرارات أربع فئات هي {m('8')} و{m('15')} و{m('x')} و{m('6')}. ما قيمة {m('x')}؟",
         11, [9, 12, 13], "40 − (8 + 15 + 6) = 11", svg_g9_histogram([("1", 8, "8"), ("2", 15, "15"), ("3", 11, "?"), ("4", 6, "6")])),
    ]
    for q_en, q_ar, ans, dists, note, diag in dat2_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Easy", "G9-DAT-02",
            q_en, q_ar, ans, dists,
            "Sum the relevant bars/cells and divide by the appropriate total!",
            "اجمع الفئات أو الخلايا المطلوبة واقسم على المجموع المناسب!",
            "Apply frequency and weighted-mean definitions.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق تعريف التكرار النسبي أو المتوسط المرجح.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Medium 6-10: Percentage weighted courses & conditional probabilities from two-way tables
    dat2_med = [
        (f"Course grades weight homework {m('20\\%')}, midterm {m('30\\%')}, and final {m('50\\%')}. Sara earns {m('95')}, {m('80')}, and {m('86')}, respectively. What is her weighted course average?",
         f"تتوزع درجة مقرر بوزن {m('20\\%')} للواجبات و{m('30\\%')} للفصلي و{m('50\\%')} للنهائي. حصلت سارة على {m('95')} و{m('80')} و{m('86')} على الترتيب. ما معدلها المرجح؟",
         86, [87, 85, 88], "0.20(95) + 0.30(80) + 0.50(86) = 19 + 24 + 43 = 86"),
        (f"In a two-way table, {m('24')} Grade 8 and {m('36')} Grade 9 students ride the Metro, while {m('16')} Grade 8 and {m('14')} Grade 9 students ride the Bus. **Given** a student rides the Metro, what is the probability they are in Grade 9?",
         f"في جدول مزدوج، يستخدم المترو {m('24')} طالباً من الثاني المتوسط و{m('36')} من الثالث، والحافلة {m('16')} من الثاني و{m('14')} من الثالث. **علماً** بأن الطالب يستخدم المترو، فما احتمال أنه في الثالث المتوسط؟",
         Fraction(3, 5), [Fraction(2, 5), Fraction(18, 25), Fraction(9, 25)], "Metro total = 24 + 36 = 60 ⇒ 36 / 60 = 3/5"),
        (f"In the same survey ({m('36')} Grade 9 Metro, {m('14')} Grade 9 Bus), **given** that a student is in Grade 9, what is the probability they ride the Bus?",
         f"في المسح ذاته ({m('36')} مترو و{m('14')} حافلة لطلاب الثالث المتوسط)، **علماً** بأن الطالب في الثالث المتوسط، فما احتمال استخدامه للحافلة؟",
         Fraction(7, 25), [Fraction(7, 45), Fraction(7, 15), Fraction(18, 25)], "Grade 9 total = 36 + 14 = 50 ⇒ 14 / 50 = 7/25"),
        (f"A frequency table records quiz scores: score {m('7')} ({m('4')} students), score {m('8')} ({m('5')} students), score {m('9')} ({m('7')} students), and score {m('10')} ({m('4')} students). What is the mean score?",
         f"جدول تكراري لدرجات اختبار قصير: الدرجة {m('7')} ({m('4')} طلاب)، {m('8')} ({m('5')} طلاب)، {m('9')} ({m('7')} طلاب)، {m('10')} ({m('4')} طلاب). ما المتوسط الحسابي للدرجات؟",
         8.55, [8.5, 8.75, 9.0], "(28 + 40 + 63 + 40) / 20 = 171 / 20 = 8.55"),
        (f"In a grouped histogram of {m('60')} solar panels' efficiencies: {m('16\\text{–}18\\%')} ({m('9')}), {m('18\\text{–}20\\%')} ({m('21')}), {m('20\\text{–}22\\%')} ({m('18')}), {m('22\\text{–}24\\%')} ({m('12')}). What percentage of panels have efficiency **at least** {m('20\\%')}?",
         f"في مدرج تكراري لكفاءة {m('60')} لوحاً شمسياً: {m('16\\text{–}18\\%')} ({m('9')})، {m('18\\text{–}20\\%')} ({m('21')})، {m('20\\text{–}22\\%')} ({m('18')})، {m('22\\text{–}24\\%')} ({m('12')}). ما النسبة المئوية للألواح التي كفاءتها {m('20\\%')} فأكثر؟",
         50, [30, 45, 55], "(18 + 12) / 60 × 100% = 50%"),
    ]
    for q_en, q_ar, ans, dists, note in dat2_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Medium", "G9-DAT-02",
            q_en, q_ar, ans, dists,
            "For conditional probability P(A | B), divide ONLY by the total of condition B!",
            "في الاحتمال المشروط P(A | B)، اقسم فقط على مجموع الفئة المشروطة B!",
            "Compute weighted sums or restrict to the conditioned row/column.",
            [f"{m(note)}."],
            "Verified.",
            "نحسب المجموع المرجح أو نقسم على المجموع الهامشى للشرط.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_nafes_function_table(["Condition", "Count"], [["Target", note.split("⇒")[0][:20]], ["Result", "?"]], highlight_cell=(1, 1)),
        ))

    # Hard 11-15: Target final exam score, missing frequency from mean, combined group mean
    dat2_hard = [
        (f"Coursework ({m('40\\%')}) and the final exam ({m('60\\%')}) determine the final grade. Omar has {m('80')} in coursework; what score must he earn on the final exam to achieve an overall weighted average of {m('89')}?",
         f"تتكون الدرجة النهائية من أعمال السنة ({m('40\\%')}) والاختبار النهائي ({m('60\\%')}). حصل عمر على {m('80')} في أعمال السنة؛ فما الدرجة التي يحتاجها في النهائي ليحقق معدلاً مرجحاً قدره {m('89')}؟",
         95, [98, 92, 94], "0.40(80) + 0.60F = 89 ⇒ 32 + 0.60F = 89 ⇒ 0.60F = 57 ⇒ F = 95"),
        (f"Section A ({m('20')} students) has mean score {m('78')}, and Section B ({m('30')} students) has mean score {m('88')}. What is the combined mean score of all {m('50')} students?",
         f"متوسط درجات الشعبة (أ) ({m('20')} طالباً) هو {m('78')}، ومتوسط الشعبة (ب) ({m('30')} طالباً) هو {m('88')}. ما المتوسط الحسابي لجميع الطلاب الخمسين معاً؟",
         84, [83, 85, 82], "(20×78 + 30×88) / 50 = (1560 + 2640) / 50 = 4200 / 50 = 84"),
        (f"In a frequency table, values {m('2, 4, 6, 8')} occur with frequencies {m('3, 5, k, 2')}, respectively. If the mean of the dataset is {m('5')}, what is {m('k')}?",
         f"في جدول تكراري، تتكرر القيم {m('2, 4, 6, 8')} بالتكرارات {m('3, 5, k, 2')} على الترتيب. إذا كان المتوسط الحسابي {m('5')}، فما قيمة {m('k')}؟",
         8, [6, 5, 4], "(6 + 20 + 6k + 16) / (10 + k) = 5 ⇒ 42 + 6k = 50 + 5k ⇒ k = 8"),
        (f"Of {m('200')} tested sensors, {m('140')} are from Plant A ({m('90\\%')} pass) and {m('60')} are from Plant B ({m('80\\%')} pass). **Given** that a randomly chosen sensor **failed**, what is the probability it came from Plant B?",
         f"من بين {m('200')} مستشعر، أُنتج {m('140')} في المصنع (أ) (نسبة الاجتياز {m('90\\%')}) و{m('60')} في المصنع (ب) (نسبة الاجتياز {m('80\\%')}). **علماً** بأن مستشعراً مختاراً **فشل**، فما احتمال أنه من المصنع (ب)؟",
         Fraction(6, 13), [Fraction(12, 60), Fraction(7, 13), Fraction(3, 50)], "Failed A = 14, Failed B = 12 ⇒ Total failed = 26 ⇒ 12 / 26 = 6/13"),
        (f"The mean of {m('8')} numbers is {m('15')}. When one number is removed, the mean of the remaining {m('7')} numbers becomes {m('13')}. What number was removed?",
         f"المتوسط الحسابي لـ {m('8')} أعداد يساوي {m('15')}. عند حذف أحد الأعداد أصبح متوسط الأعداد السبعة المتبقية {m('13')}. ما العدد الذي حُذف؟",
         29, [27, 25, 17], "8×15 − 7×13 = 120 − 91 = 29"),
    ]
    for q_en, q_ar, ans, dists, note in dat2_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Hard", "G9-DAT-02",
            q_en, q_ar, ans, dists,
            "Convert every mean into a total sum (Sum = N × Mean), or build the exact 2×2 count table!",
            "حوّل كل متوسط إلى مجموع كلي (المجموع = العدد × المتوسط)، أو كوّن جدول الأعداد الفعلي!",
            "Use total-sum conservation and two-way count reconstruction.",
            [f"{m(note)}."],
            "Verified.",
            "نستخدم حفظ المجموع الكلي وإعادة بناء الجدول المزدوج.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_nafes_function_table(["Step", "Equation"], [["Model", note.split("⇒")[0][:22]], ["Answer", "?"]], highlight_cell=(1, 1)),
        ))
    return qs


def _gen_dat_03(start_idx: int) -> list[dict]:
    """G9-DAT-03: Permutations P(n, r) vs Combinations C(n, r)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Direct P(n,r), C(n,r) & n!
    pc_easy = [
        (f"What is the value of the permutation {m('P(6, 2)')}?",
         f"ما قيمة التباديل {m('P(6, 2)')}؟",
         math.perm(6, 2), [math.comb(6, 2), 12, 36], "6 × 5 = 30", ["6", "5"]),
        (f"What is the value of the combination {m('C(7, 2)')}?",
         f"ما قيمة التوافيق {m('C(7, 2)')}؟",
         math.comb(7, 2), [math.perm(7, 2), 14, 28], "(7 × 6) / 2 = 21", ["7", "6"]),
        (f"In how many ways can {m('5')} distinct textbooks be arranged in a row on a shelf?",
         f"بكم طريقة يمكن ترتيب {m('5')} كتب دراسية مختلفة في صف واحد على رف؟",
         math.factorial(5), [25, 60, 24], "5! = 5 × 4 × 3 × 2 × 1 = 120", ["5", "4", "3", "2", "1"]),
        (f"Seven runners compete in a race with no ties. In how many ways can Gold, Silver, and Bronze medals be awarded?",
         f"يتنافس {m('7')} عدّائين في سباق دون تعادل. بكم طريقة يمكن توزيع الميداليات الذهبية والفضية والبرونزية؟",
         math.perm(7, 3), [math.comb(7, 3), 21, 343], "P(7, 3) = 7 × 6 × 5 = 210", ["7", "6", "5"]),
        (f"A student chooses {m('2')} elective workshops from {m('9')} available workshops. How many unordered pairs are possible?",
         f"يختار طالب ورشتين تدريبيتين من بين {m('9')} ورش متاحة دون ترتيب. بكم طريقة يمكنه الاختيار؟",
         math.comb(9, 2), [math.perm(9, 2), 18, 45], "C(9, 2) = (9 × 8) / 2 = 36", ["9", "8"]),
    ]
    for q_en, q_ar, ans, dists, note, slots in pc_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Easy", "G9-DAT-03",
            q_en, q_ar, ans, dists,
            "Use P(n, r) when positions/medals differ, and C(n, r) when order does not matter!",
            "استخدم التباديل عندما يهم الترتيب، والتوافيق عندما لا يهم الترتيب!",
            "Apply permutation or combination counting.",
            [f"{m(note)}."],
            "Verified via math.perm / math.comb.",
            "نطبّق قانون التباديل أو التوافيق.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_g9_code_slots(slots),
        ))

    # Medium 6-10: PIN codes, committees, round-robin matches, role assignments
    pc_med = [
        (f"A laboratory door uses a {m('4')}-digit passkey formed from digits {m('\\{1, 2, 3, 4, 5, 6\\}')} **without repetition**. How many distinct passkeys exist?",
         f"قفل باب مختبر يتكون من {m('4')} أرقام مختلفة تُختار من المجموعة {m('\\{1, 2, 3, 4, 5, 6\\}')} **دون تكرار**. كم رمزاً سرياً مختلفاً يمكن تكوينه؟",
         math.perm(6, 4), [math.comb(6, 4), 1296, 120], "P(6, 4) = 6 × 5 × 4 × 3 = 360", ["6", "5", "4", "3"]),
        (f"An ETEC school council forms a {m('3')}-student committee from {m('9')} nominees (all members equal). How many committees can be formed?",
         f"يُشكّل مجلس طلابي لجنة من {m('3')} طلاب متساوي المهام من بين {m('9')} مرشحين. كم لجنة مختلفة يمكن تشكيلها؟",
         math.comb(9, 3), [math.perm(9, 3), 27, 126], "C(9, 3) = (9 × 8 × 7) / 6 = 84", ["9", "8", "7"]),
        (f"Ten robotics teams compete in a single round-robin league where every team plays every other team **exactly once**. How many matches are played?",
         f"تشارك {m('10')} فرق روبوت في دوري من دور واحد بحيث يلاعب كل فريق بقية الفرق **مرة واحدة فقط**. كم مباراة تُقام في الدوري؟",
         math.comb(10, 2), [math.perm(10, 2), 20, 50], "C(10, 2) = (10 × 9) / 2 = 45", ["10", "9"]),
        (f"From {m('6')} finalists, a club elects a President, a Vice-President, and a Secretary (no person holds two roles). How many outcomes exist?",
         f"من بين {m('6')} مرشحين، ينتخب نادٍ رئيساً ونائباً للرئيس وأميناً للسر. بكم طريقة مختلفة يمكن شغل المناصب الثلاثة؟",
         math.perm(6, 3), [math.comb(6, 3), 18, 216], "P(6, 3) = 6 × 5 × 4 = 120", ["6", "5", "4"]),
        (f"A badge code has {m('2')} distinct letters from {m('\\{A, B, C, D, E\\}')} followed by {m('2')} distinct digits from {m('\\{1, 2, 3, 4\\}')}. How many badge codes exist?",
         f"يتكون رمز بطاقة من حرفين مختلفين من {m('\\{A, B, C, D, E\\}')} يتبعهما رقمان مختلفان من {m('\\{1, 2, 3, 4\\}')}. كم رمزاً مختلفاً يمكن تكوينه؟",
         math.perm(5, 2) * math.perm(4, 2), [math.comb(5, 2) * math.comb(4, 2), 32, 400], "P(5,2) × P(4,2) = 20 × 12 = 240", ["5", "4", "4", "3"]),
    ]
    for q_en, q_ar, ans, dists, note, slots in pc_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Medium", "G9-DAT-03",
            q_en, q_ar, ans, dists,
            "Distinct roles/codes require permutations; equal-role committees/matches require combinations!",
            "المناصب والأرقام السرية تتطلب تباديل، أما اللجان والمباريات فتتطلب توافيق!",
            "Count stages via multiplication principle, permutations, or combinations.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق مبدأ العد الأساسي والتباديل أو التوافيق.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_g9_code_slots(slots),
        ))

    # Hard 11-15: Sub-group combinations, constrained PINs, C(n,2)=28, P/C ratio, adjacent block
    pc_hard = [
        (f"A science delegation must consist of {m('2')} teachers chosen from {m('5')} teachers AND {m('2')} students chosen from {m('6')} students. How many distinct delegations can be formed?",
         f"يتكون وفد علمي من معلمَين يُختاران من بين {m('5')} معلمين، وطالبَين يُختاران من بين {m('6')} طلاب. بكم طريقة يمكن تكوين الوفد؟",
         math.comb(5, 2) * math.comb(6, 2), [math.comb(5, 2) + math.comb(6, 2), 600, 120], "C(5,2) × C(6,2) = 10 × 15 = 150"),
        (f"At a conference, every participant shakes hands once with every other participant. If {m('28')} handshakes occur in total, how many participants are there?",
         f"في مؤتمر علمي صافح كل مشارك جميع المشاركين الآخرين مرة واحدة فقط. إذا بلغ إجمالي المصافحات {m('28')} مصافحة، فكم عدد المشاركين؟",
         8, [7, 9, 14], "C(n, 2) = n(n − 1)/2 = 28 ⇒ n(n − 1) = 56 ⇒ n = 8"),
        (f"For any integer {m('n \\ge 4')}, what is the exact value of the ratio {m(r'\frac{P(n, 4)}{C(n, 4)}')}?",
         f"لأي عدد صحيح {m('n \\ge 4')}، ما القيمة الدقيقة للنسبة {m(r'\frac{P(n, 4)}{C(n, 4)}')}؟",
         24, [4, 12, 16], "P(n, 4) / C(n, 4) = 4! = 24"),
        (f"How many **even** {m('3')}-digit numbers with **distinct** digits can be formed using only digits from {m('\\{1, 2, 3, 4, 5\\}')}?",
         f"كم عدداً **زوجياً** من {m('3')} أرقام **مختلفة** يمكن تكوينه من الأرقام {m('\\{1, 2, 3, 4, 5\\}')}؟",
         24, [60, 12, 30], "Ones digit ∈ {2, 4} (2 choices); remaining two slots P(4, 2) = 12 ⇒ 2 × 12 = 24"),
        (f"Five speakers ({m('A, B, C, D, E')}) are scheduled in {m('5')} sequential slots. In how many schedules do {m('A')} and {m('B')} speak **consecutively** (in either order)?",
         f"خمسة متحدثين ({m('A, B, C, D, E')}) يُرتبون في {m('5')} فقرات متتالية. في كم جدولاً يتحدث {m('A')} و{m('B')} **متتاليين** (بأي ترتيب)؟",
         48, [24, 120, 36], "Treat {AB} as 1 block: 4! × 2! = 24 × 2 = 48"),
    ]
    for q_en, q_ar, ans, dists, note in pc_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Hard", "G9-DAT-03",
            q_en, q_ar, ans, dists,
            "Fill the most restricted slot first (like the even ones digit), or group adjacent items into a single super-block!",
            "ابدأ بالخانة المقيدة أولاً (كخانة الآحاد الزوجية)، أو ادمج العنصرين المتجاورين في كتلة واحدة!",
            "Apply constrained combinatorics and factorial identities.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق قواعد العد المقيد وخصائص التوافيق.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=svg_g9_code_slots(["Slot 1", "Slot 2", "Slot 3"], "Constrained Counting"),
        ))
    return qs


def _gen_dat_04(start_idx: int) -> list[dict]:
    """G9-DAT-04: Independent vs dependent compound probability & unions P(A U B)."""
    qs: list[dict] = []
    cur = start_idx

    # Easy 1-5: Independent coin/die/spinner & mutually exclusive
    pr_easy = [
        (f"A fair coin is tossed and a fair {m('6')}-sided die is rolled. What is the probability of getting Heads **and** a number greater than {m('4')}?",
         f"أُلقيت قطعة نقد متوازنة ورُمي مكعب أرقام منتظم ({m('1\\text{–}6')}). ما احتمال ظهور الشعار **و**عدد أكبر من {m('4')}؟",
         Fraction(1, 6), [Fraction(1, 3), Fraction(1, 12), Fraction(5, 6)], "(1/2) × (2/6) = 1/6", svg_nafes_spinner(["1", "2", "3", "4", "5", "6"], "Coin × Die")),
        (f"A spinner with {m('5')} equal sectors labeled {m('1')} to {m('5')} is spun **twice**. What is the probability of landing on {m('5')} both times?",
         f"أُدير قرص دوّار مقسم إلى {m('5')} قطاعات متطابقة مرقمة من {m('1')} إلى {m('5')} **مرتين**. ما احتمال استقرار المؤشر على {m('5')} في المرتين معاً؟",
         Fraction(1, 25), [Fraction(2, 5), Fraction(1, 5), Fraction(2, 25)], "(1/5) × (1/5) = 1/25", svg_nafes_spinner(["1", "2", "3", "4", "5"], "2 independent spins")),
        (f"A bag holds {m('4')} red, {m('5')} green, and {m('3')} yellow tokens. In a single draw, what is the probability of drawing a red **or** yellow token?",
         f"يحوي كيس {m('4')} أقراص حمراء و{m('5')} خضراء و{m('3')} صفراء. عند سحب قرص واحد، ما احتمال أن يكون أحمر **أو** أصفر؟",
         Fraction(7, 12), [Fraction(1, 12), Fraction(5, 12), Fraction(1, 3)], "(4 + 3) / 12 = 7/12", svg_g9_marble_bag([("Red", 4, "#fca5a5"), ("Green", 5, "#86efac"), ("Yellow", 3, "#fde68a")])),
        (f"If the probability of rain in Abha tomorrow is {m(r'\frac{3}{8}')}, what is the probability that it will **not** rain?",
         f"إذا كان احتمال هطول المطر في أبها غداً هو {m(r'\frac{3}{8}')}، فما احتمال **عدم** هطول المطر؟",
         Fraction(5, 8), [Fraction(3, 8), Fraction(1, 8), Fraction(3, 5)], "1 − 3/8 = 5/8", svg_nafes_pie_chart([("Rain", 3), ("No Rain", 5)])),
        (f"Two fair coins are tossed together. What is the probability of getting **at least one** Head?",
         f"أُلقيت قطعتا نقد متوازنتان معاً. ما احتمال ظهور الشعار **مرة واحدة على الأقل**؟",
         Fraction(3, 4), [Fraction(1, 2), Fraction(1, 4), Fraction(2, 3)], "1 − P(TT) = 1 − 1/4 = 3/4", svg_nafes_spinner(["HH", "HT", "TH", "TT"], "3 of 4 outcomes")),
    ]
    for q_en, q_ar, ans, dists, note, diag in pr_easy:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Easy", "G9-DAT-04",
            q_en, q_ar, ans, dists,
            "Multiply probabilities for independent 'AND' events; add probabilities for mutually exclusive 'OR' events!",
            "اضرب الاحتمالات للحوادث المستقلة (و)، واجمعها للحوادث المتنافية (أو)!",
            "Apply elementary compound and complement probability rules.",
            [f"{m(note)}."],
            "Probability lies in [0, 1] and is reduced.",
            "نطبّق قاعدة الضرب أو الجمع أو المتممة.",
            [f"{m(note)}."],
            "الكسر في أبسط صورة.",
            diagram_en=diag,
        ))

    # Medium 6-10: Without replacement & overlapping unions P(A U B)
    pr_med = [
        (f"A jar contains {m('6')} green marbles and {m('4')} white marbles. Two marbles are drawn **without replacement**. What is the probability that both are green?",
         f"وعاء به {m('6')} كرات خضراء و{m('4')} بيضاء. سُحبت كرتان **دون إرجاع**. ما احتمال أن تكونا خضراوين معاً؟",
         Fraction(1, 3), [Fraction(9, 25), Fraction(2, 5), Fraction(3, 10)], "(6/10) × (5/9) = 30/90 = 1/3", svg_g9_marble_bag([("Green", 6, "#86efac"), ("White", 4, "#f1f5f9")], "Without replacement")),
        (f"A box has {m('5')} gold cards and {m('3')} silver cards. Two cards are drawn **without replacement**. What is the probability that the first is gold and the second is silver?",
         f"صندوق به {m('5')} بطاقات ذهبية و{m('3')} فضية. سُحبت بطاقتان **دون إرجاع**. ما احتمال أن تكون الأولى ذهبية والثانية فضية؟",
         Fraction(15, 56), [Fraction(15, 64), Fraction(15, 28), Fraction(5, 14)], "(5/8) × (3/7) = 15/56", svg_g9_marble_bag([("Gold", 5, "#fde68a"), ("Silver", 3, "#e2e8f0")], "1st Gold, 2nd Silver")),
        (f"One card is drawn at random from cards numbered {m('1')} through {m('12')}. What is the probability that the number is **even OR a multiple of 3**?",
         f"سُحبت بطاقة عشوائياً من بطاقات مرقمة من {m('1')} إلى {m('12')}. ما احتمال أن يحمل الرقم **عدداً زوجياً أو مضاعفاً للعدد 3**؟",
         Fraction(2, 3), [Fraction(5, 6), Fraction(1, 2), Fraction(7, 12)], "(6 + 4 − 2) / 12 = 8 / 12 = 2/3", svg_venn_2("Even (6)", "Mult. 3 (4)", "4", "2", "2", "Out: 4")),
        (f"Sensor A detects a fault independently with probability {m(r'\frac{4}{5}')}, and Sensor B with probability {m(r'\frac{3}{4}')}. What is the probability that **both** sensors detect the fault?",
         f"يكتشف المستشعر (أ) عطلاً باحتمال مستقل {m(r'\frac{4}{5}')}، والمستشعر (ب) باحتمال {m(r'\frac{3}{4}')}. ما احتمال أن يكتشف المستشعران **معاً** العطل؟",
         Fraction(3, 5), [Fraction(7, 9), Fraction(19, 20), Fraction(1, 20)], "(4/5) × (3/4) = 3/5", svg_venn_2("A (4/5)", "B (3/4)", "1/5", "3/5", "3/20")),
        (f"In a class of {m('30')} students, {m('18')} study Robotics, {m('14')} study AI, and {m('8')} study both. What is the probability a randomly chosen student studies Robotics **or** AI?",
         f"في فصل من {m('30')} طالباً، يدرس {m('18')} الروبوت و{m('14')} الذكاء الاصطناعي و{m('8')} المجالين معاً. ما احتمال أن يدرس طالب مختار عشوائياً الروبوت **أو** الذكاء الاصطناعي؟",
         Fraction(4, 5), [Fraction(11, 15), Fraction(2, 3), Fraction(13, 15)], "(18 + 14 − 8) / 30 = 24 / 30 = 4/5", svg_venn_2("Robotics", "AI", "10", "8", "6", "Out: 6")),
    ]
    for q_en, q_ar, ans, dists, note, diag in pr_med:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Medium", "G9-DAT-04",
            q_en, q_ar, ans, dists,
            "Subtract P(A ∩ B) for overlapping unions, and reduce total by 1 on the second draw without replacement!",
            "اطرح التقاطع P(A ∩ B) في الحوادث غير المتنافية، وأنقص المقام 1 في السحب دون إرجاع!",
            "Apply dependent multiplication or inclusion-exclusion.",
            [f"{m(note)}."],
            "Verified.",
            "نطبّق قانون الاحتمال المشروط أو الشمول والإقصاء.",
            [f"{m(note)}."],
            "متحقق.",
            diagram_en=diag,
        ))

    # Hard 11-15: At least one hit, two different colors in either order, unknown count from compound prob
    pr_hard = [
        (f"Two independent drones attempt a landing with success probabilities {m(r'\frac{3}{5}')} and {m(r'\frac{3}{4}')}. What is the probability that **at least one** drone lands successfully?",
         f"طائرتان مسيرتان مستقلتان احتمال نجاح هبوط الأولى {m(r'\frac{3}{5}')} والثانية {m(r'\frac{3}{4}')}. ما احتمال نجاح هبوط **واحدة منهما على الأقل**؟",
         Fraction(9, 10), [Fraction(9, 20), Fraction(4, 5), Fraction(17, 20)], "1 − P(both fail) = 1 − (2/5)(1/4) = 1 − 1/10 = 9/10"),
        (f"A pouch contains {m('4')} blue and {m('3')} red chips. Two chips are drawn at random **without replacement**. What is the probability that the two chips have **different colors**?",
         f"كيس به {m('4')} رقائق زرقاء و{m('3')} حمراء. سُحبت رقيقتان عشوائياً **دون إرجاع**. ما احتمال أن تكون الرقيقتان من **لونين مختلفين**؟",
         Fraction(4, 7), [Fraction(2, 7), Fraction(12, 49), Fraction(3, 7)], "P(BR) + P(RB) = (4/7)(3/6) + (3/7)(4/6) = 24/42 = 4/7"),
        (f"A tray holds {m('10')} microchips, of which {m('3')} are defective. If {m('2')} microchips are selected **without replacement**, what is the probability that **neither** is defective?",
         f"تحوي صينية {m('10')} شرائح إلكترونية منها {m('3')} معيبة. عند سحب شريحتين **دون إرجاع**، ما احتمال أن تكون الشريحتان **سليمتين معاً**؟",
         Fraction(7, 15), [Fraction(49, 100), Fraction(1, 15), Fraction(8, 15)], "(7/10) × (6/9) = 42 / 90 = 7/15"),
        (f"Events {m('A')} and {m('B')} satisfy {m('P(A) = 0.55')}, {m('P(B) = 0.40')}, and {m('P(A \\cup B) = 0.75')}. What is {m('P(A \\cap B)')} as a simplified fraction?",
         f"إذا كان {m('P(A) = 0.55')} و{m('P(B) = 0.40')} و{m('P(A \\cup B) = 0.75')}، فما قيمة {m('P(A \\cap B)')} في أبسط صورة كسرية؟",
         Fraction(1, 5), [Fraction(3, 20), Fraction(1, 4), Fraction(19, 20)], "0.55 + 0.40 − 0.75 = 0.20 = 1/5"),
        (f"A box contains {m('r')} red balls and {m('2')} white balls. When {m('2')} balls are drawn **without replacement**, the probability that both are red is {m(r'\frac{2}{5}')}. What is {m('r')}?",
         f"يحتوي صندوق على {m('r')} كرات حمراء وكرتين بيضاوين. عند سحب كرتين **دون إرجاع** كان احتمال أن تكونا حمراوين معاً يساوي {m(r'\frac{2}{5}')}. ما قيمة {m('r')}؟",
         4, [3, 5, 6], "(r / (r+2)) · ((r−1) / (r+1)) = 2/5 ⇒ (4/6)(3/5) = 12/30 = 2/5 ⇒ r = 4"),
    ]
    for q_en, q_ar, ans, dists, note in pr_hard:
        qid = _qid(cur); cur += 1
        qs.append(make_nafes_q(
            qid, LEVEL, "Data & Probability", "Hard", "G9-DAT-04",
            q_en, q_ar, ans, dists,
            "Remember 'different colors' includes BOTH orders (BR + RB), and 'at least one' = 1 − P(none)!",
            "تذكّر أن 'لونين مختلفين' يشمل الترتيبين معاً (أزرق ثم أحمر + أحمر ثم أزرق)، و'على الأقل واحد' = 1 − احتمال العدم!",
            "Use complement probability, ordered-case addition, or algebraic probability equations.",
            [f"{m(note)}."],
            "Verified by exact Fraction arithmetic.",
            "نطبّق احتمال المتممة أو جمع الحالات الممكنة.",
            [f"{m(note)}."],
            "متحقق بحساب الكسور الدقيق.",
            diagram_en=svg_g9_marble_bag([("Group 1", 4, "#93c5fd"), ("Group 2", 3, "#fca5a5")], "Compound Event Reasoning"),
        ))
    return qs


def build_grade9_bank() -> list[dict]:
    """Build and return all 360 verified Grade 9 ETEC Nafes questions (NAFS-G9-001 .. NAFS-G9-360)."""
    generators = [
        _gen_num_01, _gen_num_02, _gen_num_03, _gen_num_04,
        _gen_num_05, _gen_num_06, _gen_num_07, _gen_num_08,
        _gen_alg_01, _gen_alg_02, _gen_alg_03, _gen_alg_04,
        _gen_geo_01, _gen_geo_02, _gen_geo_03, _gen_geo_04,
        _gen_geo_05, _gen_geo_06, _gen_geo_07, _gen_geo_08,
        _gen_dat_01, _gen_dat_02, _gen_dat_03, _gen_dat_04,
    ]
    bank: list[dict] = []
    cur = 1
    for gen in generators:
        batch = gen(cur)
        assert len(batch) == 15, f"Generator {gen.__name__} produced {len(batch)} != 15 items"
        bank.extend(batch)
        cur += 15
    assert len(bank) == 360
    return bank
